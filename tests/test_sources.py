import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.sources import SourceError, load_manifest, recover, target_path


class SourceRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.payload = b'original source bytes\n'
        self.item = {
            'id': 'deck-original', 'source_id': 'deck', 'path': 'nested/deck.txt',
            'bucket_key': 'remote/deck.txt', 'size': len(self.payload),
            'sha256': hashlib.sha256(self.payload).hexdigest(), 'role': 'original',
            'description': 'Original deck', 'added_at': '2026-10-02T00:00:00Z',
            'derived_from': [],
        }
        self.data = {
            'schema_version': 1, 'bucket': 'test-bucket',
            'sources': [{'id': 'deck', 'title': 'Deck', 'sensitivity': 'internal', 'handling': 'Paraphrase'}],
            'files': [self.item],
        }

    def load(self, data):
        path = self.root / 'manifest.json'
        path.write_text(json.dumps(data))
        return load_manifest(path)

    def test_paths_and_cli_globs_rejected_before_download(self):
        for value in ['../escape', '/absolute', 'a/../../escape', 'a//b', 'a/./b', 'a\\b', '*.pdf', 'a?[0]', '-r', 'a\nb']:
            for field in ['path', 'bucket_key']:
                with self.subTest(value=value, field=field):
                    data = copy.deepcopy(self.data)
                    data['files'][0][field] = value
                    with self.assertRaises(SourceError):
                        self.load(data)

    def test_unknown_source_duplicate_and_derivative_cycle_rejected(self):
        data = copy.deepcopy(self.data)
        data['files'][0]['source_id'] = 'missing'
        with self.assertRaises(SourceError): self.load(data)
        data = copy.deepcopy(self.data)
        data['files'].append(copy.deepcopy(self.item))
        with self.assertRaises(SourceError): self.load(data)
        data = copy.deepcopy(self.data)
        second = {**self.item, 'id': 'derived', 'path': 'b.txt', 'bucket_key': 'b.txt', 'role': 'extracted-text', 'derived_from': ['deck-original']}
        data['files'][0]['derived_from'] = ['derived']
        data['files'].append(second)
        with self.assertRaisesRegex(SourceError, 'cycle'): self.load(data)

    def test_verified_download_is_published_and_repeat_skips_network(self):
        def fetch(bucket, item, destination): destination.write_bytes(self.payload)
        with patch('tools.sources.download', side_effect=fetch) as mock:
            self.assertEqual(recover(self.root, 'test-bucket', self.item), 'downloaded')
            self.assertEqual(recover(self.root, 'test-bucket', self.item), 'present')
            mock.assert_called_once()
        self.assertEqual((self.root / self.item['path']).read_bytes(), self.payload)

    def test_corrupt_download_never_published_and_temp_removed(self):
        with patch('tools.sources.download', side_effect=lambda b, i, p: p.write_bytes(b'corrupt')):
            with self.assertRaisesRegex(SourceError, 'checksum mismatch'):
                recover(self.root, 'test-bucket', self.item)
        self.assertFalse((self.root / self.item['path']).exists())
        self.assertEqual(list(self.root.rglob('.source-download-*')), [])

    def test_existing_conflict_is_preserved_without_download(self):
        target = self.root / self.item['path']
        target.parent.mkdir(); target.write_bytes(b'local edits')
        with patch('tools.sources.download') as mock:
            with self.assertRaisesRegex(SourceError, 'refusing to overwrite'):
                recover(self.root, 'test-bucket', self.item)
            mock.assert_not_called()
        self.assertEqual(target.read_bytes(), b'local edits')

    def test_failed_transfer_cleans_partial_file(self):
        def fail(bucket, item, destination):
            destination.write_bytes(b'partial')
            raise SourceError('connection failed')
        with patch('tools.sources.download', side_effect=fail):
            with self.assertRaises(SourceError): recover(self.root, 'test-bucket', self.item)
        self.assertFalse((self.root / self.item['path']).exists())
        self.assertEqual(list(self.root.rglob('.source-download-*')), [])

    def test_symlink_parent_and_file_rejected(self):
        other = self.root / 'outside'; other.mkdir()
        (self.root / 'nested').symlink_to(other, target_is_directory=True)
        with self.assertRaisesRegex(SourceError, 'symlink'): target_path(self.root, self.item)
        (self.root / 'nested').unlink(); (self.root / 'nested').mkdir()
        (self.root / self.item['path']).symlink_to(other / 'absent')
        with self.assertRaisesRegex(SourceError, 'symlink'): target_path(self.root, self.item)

    def test_concurrent_destination_is_not_overwritten(self):
        def fetch(bucket, item, destination):
            destination.write_bytes(self.payload)
            (self.root / item['path']).write_bytes(b'concurrent edit')
        with patch('tools.sources.download', side_effect=fetch):
            with self.assertRaisesRegex(SourceError, 'appeared during download'):
                recover(self.root, 'test-bucket', self.item)
        self.assertEqual((self.root / self.item['path']).read_bytes(), b'concurrent edit')


if __name__ == '__main__':
    unittest.main()
