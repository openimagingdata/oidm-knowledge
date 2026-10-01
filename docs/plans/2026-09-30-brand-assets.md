# Brand assets from Tigris

Status: complete, 2026-09-30.

Bring the useful OIDM and Anatomic Locations brand assets from `t3://oidm-public/logos/` into the repository and record what the supplied style guide supports for website presentation.

1. Read the style guide and inspect the logo variants alongside the site's asset pipeline.
2. Import a small selection of original SVG and PNG assets, plus the guide, with source paths and checksums.
3. Document colors, typography, variant selection, and use in site content and diagrams. Distinguish supplied rules from suggested applications.
4. Check file integrity and site asset handling. Update the site and diagram documentation, changelog, and development log, then mark this plan complete.

The work prepares assets and guidance. Applying a new site theme or changing the existing diagrams is a separate task.

## Result

- Imported 16 unmodified SVG and transparent PNG assets into `knowledge/assets/brand/`, plus the original two-page guide in `docs/brand/`.
- Recorded source URIs and checksums in `docs/brand/manifest.json`. The guide's light-blue RGB and hex values disagree; the SVG artwork supports the hex value `#49b5ea`.
- Wrote `docs/brand/README.md` with source-backed guidance, separate application suggestions, and site/diagram usage examples. Updated the site and diagram READMEs, changelog, and development log.
- Local Quartz build passed. All 16 built assets match the imported bytes, all 17 source-file checksums match the manifest, and all eight SVGs embed unchanged through `excalib.image()`.
- Strict OKF validation and the house bundle checker passed with zero errors or warnings. `git diff --check` passed. No theme changes, diagram changes, deployment, or commit were made for this task.
