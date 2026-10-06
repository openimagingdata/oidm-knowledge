# History

Completed work on the website, newest first. Page and figure work before 2026-10-05 is recorded in the repository's `DEV_LOG.md`.

## 2026-10-06

- Renamed `site/pages/` to `site/content/`: it holds the website's source Markdown and figures (Quartz's own name for its input). Earlier entries use the new name.
- Cleaned up `site/` to hold only the website. Extracted the project lead's page guidance verbatim from the planning records in git history into `guidance.md`, in place of six restored plan files. Removed the tracked review renders (regenerable) and the material drafts (still at `knowledge/drafts/` in `9725105`). Stripped the pages' frontmatter to `title` and `description`, since `site/content/` is website content, not an OKF bundle; page text unchanged. Moved the figures' `.excalidraw` sources to `tools/diagrams/excalidraw/` and the candidate figures to ignored `scratch/review/candidates/`. Split the plan into `CURRENT_TASK.md`, `ROADMAP.md`, and this file.
- Moved the brand assets to `assets/brand/` at the repository root, since the site and the diagram tooling both use them; all 16 checksums match.
- Figure output paths are now configuration: `tools/diagrams/figures.toml` maps each figure to its builder, `.excalidraw`, and SVG; builders look up their path by name, and `render_excalidraw.py --figure <name>` renders one. Every builder rebuilt byte-identical; the two-planes render matched the published SVG.

## 2026-10-05

- Moved all outward-facing page work out of the knowledge graph into `site/`, at the project lead's direction, so the pages and the graph cannot be confused. The five agreed pages and their embedded figures went to `site/content/` in the pillar layout by git moves (prose unchanged; link and citation paths only). The figure builders write to the new paths; the two-planes figure rebuilt byte-identical. Graph-side links repointed, path changes only; `task check` clean.
