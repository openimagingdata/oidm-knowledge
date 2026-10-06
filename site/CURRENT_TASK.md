# Current task: clean up `site/` (2026-10-06)

Make `site/` hold only the website: its pages, its build, and the records of this work. What comes next is in [ROADMAP.md](ROADMAP.md); what is done, in [HISTORY.md](HISTORY.md); the project lead's words, in [guidance.md](guidance.md).

- [x] Extract the project lead's page guidance verbatim from git history (commit `9725105`) into `guidance.md`; remove `site/history/`.
- [x] Remove `site/renders/` (regenerable) and `site/material/` (the drafts stay at `knowledge/drafts/` in `9725105`).
- [x] Strip the pages' frontmatter to `title` and `description`; page text unchanged.
- [x] Move the `.excalidraw` sources out of `site/content/` to `tools/diagrams/excalidraw/`; candidate figure SVGs to ignored `scratch/review/candidates/`.
- [x] Split the plan into this file, `ROADMAP.md`, and `HISTORY.md`.
- [x] Move the brand assets from `knowledge/assets/brand/` to `assets/brand/` (used by the site and the diagram tooling); update `docs/brand/` paths and manifest (all 16 checksums match at the new paths).
- [x] Figure config: `tools/diagrams/figures.toml` (TOML: read by the standard library, no new dependency) maps each figure to its builder, `.excalidraw` path, and SVG path; builders and the render step read it, nothing hardcoded. Every builder and the two-planes render verified byte-identical; `render_excalidraw.py --figure <name>` renders a configured figure.
- [x] Move this session's work entry from `DEV_LOG.md` to `HISTORY.md`.
- [x] Repoint links into removed files (the board summaries' links to drafts become GitHub URLs pinned at `9725105`).
- [x] Update `site/README.md`, the repository README, the handoff, and the graph plan's pointer to `site/`.
- [x] `task check` clean; 182 local links, the only unresolved ones the seven to unwritten pages.
- [ ] Commit only on the project lead's yes.

Open, for the project lead: the agreed pages' footnotes say the guidance is "recorded verbatim in the layout plan". That plan is now in git history only; the same words are in `guidance.md`. The footnotes are agreed text, so they are unchanged.
