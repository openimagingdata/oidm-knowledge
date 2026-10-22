#!/usr/bin/env python3
"""Recover and verify source artifacts from a reviewed manifest using the Tigris CLI."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import tempfile

REPO = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = REPO / 'docs/sources-manifest.json'


class SourceError(Exception):
    pass


def relative_path(value: object) -> str:
    if not isinstance(value, str) or not value or '\\' in value:
        raise SourceError('Artifact paths must be nonempty POSIX relative paths')
    p = PurePosixPath(value)
    if p.is_absolute() or any(s in ('', '.', '..') for s in value.split('/')):
        raise SourceError('Artifact paths must not escape the source directory')
    if any(c in value for c in '*?[]{}\x00\r\n') or value.startswith('-'):
        raise SourceError('Artifact paths must be literal, not CLI patterns')
    return value


def load_manifest(path: Path) -> dict:
    try:
        data = json.loads(path.read_text())
    except (OSError, ValueError) as exc:
        raise SourceError(f'Cannot read manifest: {path}') from exc
    if not isinstance(data, dict) or data.get('schema_version') != 1:
        raise SourceError('Unsupported manifest schema_version')
    if not re.fullmatch(r'[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]', str(data.get('bucket', ''))):
        raise SourceError('Invalid bucket name')
    if not isinstance(data.get('sources'), list) or not isinstance(data.get('files'), list):
        raise SourceError('Manifest requires sources and files lists')
    source_ids = set()
    for source in data['sources']:
        if not isinstance(source, dict) or not re.fullmatch(r'[a-z0-9][a-z0-9-]*', str(source.get('id', ''))):
            raise SourceError('Invalid source ID')
        if source['id'] in source_ids:
            raise SourceError('Duplicate source ID')
        source_ids.add(source['id'])
        if source.get('sensitivity') not in ('public', 'restricted-until-published', 'internal'):
            raise SourceError(f'Invalid sensitivity for {source["id"]}')
        if not source.get('title') or not source.get('handling'):
            raise SourceError(f'Missing title or handling for {source["id"]}')
    ids, paths, keys = set(), set(), set()
    for item in data['files']:
        if not isinstance(item, dict):
            raise SourceError('Invalid artifact entry')
        if not re.fullmatch(r'[a-z0-9][a-z0-9-]*', str(item.get('id', ''))):
            raise SourceError('Invalid artifact ID')
        path_value = relative_path(item.get('path'))
        key = relative_path(item.get('bucket_key'))
        if item['id'] in ids or path_value in paths or key in keys:
            raise SourceError('Duplicate artifact ID, path, or bucket key')
        ids.add(item['id']); paths.add(path_value); keys.add(key)
        if item.get('source_id') not in source_ids:
            raise SourceError(f'Unknown source for {item["id"]}')
        if type(item.get('size')) is not int or item['size'] < 0:
            raise SourceError(f'Invalid size for {item["id"]}')
        if not re.fullmatch(r'[0-9a-f]{64}', str(item.get('sha256', ''))):
            raise SourceError(f'Invalid SHA-256 for {item["id"]}')
        if item.get('role') not in ('original', 'capture', 'extracted-text', 'extracted-figure', 'normalized-figure', 'capture-metadata'):
            raise SourceError(f'Invalid role for {item["id"]}')
        if not item.get('description') or not item.get('added_at'):
            raise SourceError(f'Missing description or added_at for {item["id"]}')
    # Parent artifacts are explicit and must belong to the same source.
    by_id = {item['id']: item for item in data['files']}
    for item in data['files']:
        parents = item.get('derived_from', [])
        if not isinstance(parents, list) or not all(isinstance(p, str) for p in parents):
            raise SourceError('derived_from must be an artifact-ID list')
        for parent in parents:
            if parent not in ids or parent == item['id'] or by_id[parent]['source_id'] != item['source_id']:
                raise SourceError(f'Invalid parent for {item["id"]}')
        if item['role'] not in ('original', 'capture') and not parents:
            raise SourceError(f'Derivative has no parent: {item["id"]}')
    def visit(id_: str, stack: set[str], done: set[str]) -> None:
        if id_ in stack:
            raise SourceError('Derivative cycle')
        if id_ in done:
            return
        for parent in by_id[id_].get('derived_from', []):
            visit(parent, stack | {id_}, done)
        done.add(id_)
    done: set[str] = set()
    for id_ in ids:
        visit(id_, set(), done)
    if not ids or source_ids != {item['source_id'] for item in data['files']}:
        raise SourceError('Every source must have at least one artifact')
    return data


def target_path(root: Path, item: dict) -> Path:
    path = root / item['path']
    # The configured root may itself be a symlink; artifact paths inside it may not.
    current = root
    for part in PurePosixPath(item['path']).parts:
        current = current / part
        if current.is_symlink():
            raise SourceError(f'Artifact path contains a symlink: {item["id"]}')
    return path


def matches(path: Path, item: dict) -> bool:
    if not path.is_file() or path.stat().st_size != item['size']:
        return False
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest() == item['sha256']


def download(bucket: str, item: dict, destination: Path) -> None:
    try:
        result = subprocess.run(
            ['t3', 'cp', f't3://{bucket}/{item["bucket_key"]}', str(destination)],
            capture_output=True, text=True, timeout=300,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise SourceError(f'Download failed for {item["id"]}; check t3 credentials and connectivity') from exc
    if result.returncode:
        raise SourceError(f'Download failed for {item["id"]}; check t3 credentials and bucket access')


def recover(root: Path, bucket: str, item: dict) -> str:
    target = target_path(root, item)
    if target.exists():
        if matches(target, item):
            return 'present'
        raise SourceError(f'Existing file differs; refusing to overwrite {item["id"]}')
    target.parent.mkdir(parents=True, exist_ok=True)
    target_path(root, item)
    fd, temporary = tempfile.mkstemp(prefix='.source-download-', dir=target.parent)
    os.close(fd)
    temp = Path(temporary)
    try:
        download(bucket, item, temp)
        if not matches(temp, item):
            raise SourceError(f'Download checksum mismatch for {item["id"]}')
        # Publish only verified bytes, without replacing a file created concurrently.
        try:
            os.link(temp, target)
        except FileExistsError as exc:
            if not target.is_symlink() and matches(target, item):
                return 'present'
            raise SourceError(f'Destination appeared during download: {item["id"]}') from exc
        return 'downloaded'
    finally:
        temp.unlink(missing_ok=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('action', choices=['manifest', 'check', 'pull'])
    ap.add_argument('--manifest', type=Path, default=DEFAULT_MANIFEST)
    ap.add_argument('--root', type=Path, default=Path(os.environ.get('OIDM_SOURCES_DIR', '~/data/oidm-knowledge-sources')).expanduser())
    ap.add_argument('--source', action='append', default=[], help='Select a source ID; repeat for several sources')
    ap.add_argument('--jobs', type=int, choices=range(1, 17), default=4, metavar='1..16')
    args = ap.parse_args()
    try:
        data = load_manifest(args.manifest)
        source_ids = {s['id'] for s in data['sources']}
        if set(args.source) - source_ids:
            raise SourceError('Unknown source ID: ' + ', '.join(sorted(set(args.source) - source_ids)))
        items = [f for f in data['files'] if not args.source or f['source_id'] in args.source]
        if args.action == 'manifest':
            print(f'Manifest valid: {len(data["sources"])} sources, {len(data["files"])} artifacts')
            return 0
        root = args.root.expanduser().resolve()
        missing = []
        for item in items:
            target = target_path(root, item)
            if target.exists():
                if not matches(target, item):
                    raise SourceError(f'Existing file differs; refusing to overwrite {item["id"]}')
            else:
                missing.append(item)
        if args.action == 'check':
            if missing:
                raise SourceError(f'{len(missing)} missing artifacts: ' + ', '.join(i['id'] for i in missing))
            print(f'Verified {len(items)} artifacts by size and SHA-256')
            return 0
        if missing and not shutil.which('t3'):
            raise SourceError('Install the Tigris CLI (t3) before pulling sources')
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            list(pool.map(lambda item: recover(root, data['bucket'], item), missing))
        print(f'Verified {len(items)} artifacts; downloaded {len(missing)}, already present {len(items) - len(missing)}')
        return 0
    except (SourceError, OSError) as exc:
        print(f'Source error: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
