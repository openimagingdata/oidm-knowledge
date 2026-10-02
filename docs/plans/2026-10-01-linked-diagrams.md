# Linked diagram references

Status: complete, 2026-10-01. Capture and summary task only; layer migration awaits the project lead's approval.

Capture every unique URL in `links.txt` as a visual source and a concise, reusable reference to the project's ideas.

1. Identify unique links and retrieve each original diagram, preferably as SVG and PNG. Save captures and provenance under `sources/linked-diagrams/`.
2. Inspect each diagram, using readable detail views for large boards. Check earlier transcriptions against the retrieved source.
3. Write one source-grounded Markdown summary per diagram under `docs/references/linked-diagrams/`, with an index, local artifact paths, and connections to the agreed pillars. Keep share URLs in the gitignored capture manifest and preserve proposal status without meeting histories.
4. Verify link coverage and artifacts, review summaries for unsupported interpretations, update this plan and the development log, and mark completion.

Repeated URLs share one capture and summary. Source boards are historical evidence; they do not override the owner's current terminology or decisions.

## Results

Follow-up complete, 2026-10-02: checked all 15 summaries for live share links and meeting histories and generalized remaining wording in four summaries. Capture dates and local artifact paths remain for provenance. Both repository validators pass (zero errors or warnings); standalone reference conformance has zero errors and 50 external-directory link warnings, with local targets checked separately.

- Captured all 15 unique boards from 17 URL occurrences as native SVG and PNG exports. Preserved source contents, searchable text, timestamps, and checksums under `sources/linked-diagrams/`.
- Visually reviewed every board and wrote 15 draft Reference summaries, with an [index](../references/linked-diagrams/index.md), source locators, pillar connections, and links to related working pages.
- Preserved three XML-invalid native SVGs unchanged and provided normalized `usable.svg` copies alongside them.
- Verified URL coverage, PNG decoding, selected SVG XML, 63 artifact checksums, and every local summary link. OKF conformance reports zero errors; its 50 warnings concern links outside the standalone reference directory, whose targets were separately verified on disk.
- Updated README, DEV_LOG, and CHANGELOG for discoverability and handoff.

The [sources and layers plan](./2026-10-01-sources-and-layers.md) arrived during capture. These short summaries remain staged in `docs/references/linked-diagrams/` until that plan is approved; conversion into its detailed reference template and figure redraws belong to that work. No bundle or presentation files were moved, and no bucket upload or site publication was performed.
