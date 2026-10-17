# Recover and verify source material

The [source manifest](sources-manifest.json) selects 118 artifacts in 25 source groups from the private `oidm-knowledge-sources` Tigris bucket. It covers original documents, captured boards, and their extraction artifacts. The [implementation plan](plans/implementation.md) tracks subsequent reference and knowledge work.

## Check the manifest and local files

Use Python 3.11 or later and the repository's Task runner:

```bash
task sources:manifest
task sources:check
```

`manifest` validates the tracked metadata without private files or credentials. `check` compares the selected local files' sizes and SHA-256 hashes. It does not contact Tigris or inspect document text. Missing or changed artifacts cause a nonzero exit.

The default local collection is `~/data/oidm-knowledge-sources`. Override it with `OIDM_SOURCES_DIR` or `--root`:

```bash
task sources:check -- --root /path/to/local/collection
task sources:check -- --source siim-reports-of-the-future-2026
```

Repeat `--source` to select several source IDs. IDs come from the manifest's `sources` list. Without Task, run `python3 tools/sources.py manifest`, `check`, or `pull` with the same options.

## Recover into a new checkout

Install the Tigris CLI and authenticate with an account or access key authorized to read the bucket. Use `t3 login` for interactive login, or your existing credential setup. Do not put credentials into this repository or the manifest.

```bash
t3 credentials test --bucket oidm-knowledge-sources
task sources:pull
task sources:check
```

The pull command downloads only missing manifest entries and verifies each temporary download before adding it to the collection. Matching files are skipped. A differing local file causes failure and is never overwritten; inspect or move your local copy deliberately before retrying. Successfully verified downloads remain available if a later transfer fails. Temporary partial files are removed. There are no remote writes or deletes.

The download uses the installed CLI's [`t3 cp`](https://www.npmjs.com/package/@tigrisdata/cli) command with an explicit remote key for each artifact. Transfers run four at a time by default; use `--jobs 1` for sequential transfers, or any value up to 16. A download failure reports the artifact ID; check authentication and connectivity with the CLI before retrying.

Existing reference links use `sources/` relative to the repository. After recovering into the default location, create the ignored compatibility symlink from the repository root if `sources` does not already exist:

```bash
ln -s "$HOME/data/oidm-knowledge-sources" sources
```

If `sources` already exists, inspect it before changing it. For a custom collection location, link to that location instead. The command does not alter this symlink automatically.

## Read the manifest

Each source has a stable ID, title, organization where known, source date where known, source status, sensitivity, and handling instructions. Unknown organizations/dates remain `null`. Month-only dates reflect the evidence's precision. `added_at` on artifacts is the observed Tigris object timestamp, not the source's authorship date.

Each artifact records its own ID, source ID, local path, bucket key, byte size, SHA-256, role, description, and parent artifact IDs. Paths are relative to the collection. IDs identify the retained record; preserve an existing ID when deliberately relocating its file. The checksum identifies the current expected bytes. `verified_at` records storage-integrity verification, not human acceptance of the source's claims.

Sensitivity controls use of the source, not the bucket's network access. All artifacts remain in private storage, including artifacts of public talks:

- `public`: a public presentation; cite its actual statements and preserve qualifications.
- `restricted-until-published`: unpublished manuscript material; paraphrase only and redraw figures for public references.
- `internal`: source ideas may inform references under their recorded rules; do not reproduce private correspondence, live board URLs, or internal logistics.

Read `handling` before opening an artifact. The JDIM PDF packets and whole-packet text extractions include restricted sections. Use only the specified clean manuscript pages for synthesis. Never read or summarize reviewer correspondence. Hash verification treats files as opaque bytes and grants no permission to read their contents.

Board sensitivity is conservatively `internal` because publication status is not established by capture. Public-facing subject matter does not establish permission to reproduce an original board. The source date and publication status can be corrected when evidence is supplied; retrieval timestamps do not fill those fields. Other source statuses are retained from the existing source inventory and have not been rechecked for publication since that review.

## Retained material outside the source manifest

The bucket contains 307 objects. The manifest selects 118. The other 189 remain untouched:

| Classification | Files | Treatment |
|---|---:|---|
| Older board screenshots | 152 | Retained; use the native captures for new references. |
| Private review findings and responses | 31 | Retained separately from independent source evidence. |
| Working research, combined transcription, and maintenance notes | 5 | Retained for local investigation; not default source inputs. |
| Private capture index | 1 | Retained with live source URLs; not copied into the public manifest. |

Private metadata beside the local collection records the entire collection: `.local-inventory.json`, `.remote-inventory.json`, `.remote-verification.json`, and `.classified-inventory.json`. These are not committed or uploaded by this task. The default pull/check commands intentionally cover only the tracked source manifest; they do not recover the excluded review/research files or promise a complete working-directory mirror.

## Change a source record

Add a source or artifact only after identifying its status, sensitivity, and relationship to retained material. Compare local and remote bytes before replacing an expected checksum. Keep a changed upstream document's prior version when it supplies evidence for existing references. Do not change a manifest hash merely to silence a failed check.

Run `task sources:manifest`, `task sources:check`, and the source-tool tests after editing the manifest or recovery code:

```bash
python3 -m unittest discover -s tests -p test_sources.py
```

Update reference citations when their source version changes. Record meaningful source changes and verification in the existing implementation plan and development log. Uploads remain explicit operations, separate from the pull/check tool.
