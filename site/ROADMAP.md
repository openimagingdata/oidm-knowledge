# Roadmap

What is planned for the website, and where each page and figure stands. The current task is in [CURRENT_TASK.md](CURRENT_TASK.md).

`site/content/` is the website's content: Markdown pages and the SVG figures they embed. It is not an OKF bundle. A page carries `title` and `description`, and the `verified` stamp once the project lead has reviewed it; citations are footnotes in the text. The knowledge graph in `knowledge/` is a separate track; nothing here waits on it.

## Now: build the public site from `site/content/`

Built and on dev (https://oidm-knowledge-dev.talkasab.workers.dev), awaiting the project lead's look and the commit; see [CURRENT_TASK.md](CURRENT_TASK.md). Production stays closed until every page carries his `verified` stamp (`task site:verify`).

## Then: page comments (proposed)

Giscus on all three sites, one Discussions category per environment so every comment shows where it came from. Proposed 2026-10-08, awaiting the project lead's yes; details in [CURRENT_TASK.md](CURRENT_TASK.md).

## Then: the remaining pages

Standard clinical metadata next (text proposed, not agreed; it should carry the 2026-09-30 thought that time course and etiology may be properties of the edge to a diagnosis), then the rest of Foundation Context, then the other pillars. The agreed layout is the 2026-09-22 layout plan; earlier drafts with reviewed source material are at `knowledge/drafts/` in commit `9725105`. The agreed pages already link to seven of the unwritten ones: the four other pillar indexes, anatomic locations, exam types, standards.

## Pages

| Page | Status | File |
|---|---|---|
| Overview | agreed, reviewed; two-planes figure embedded; pillars stack awaits accept | `content/index.md` |
| Foundation Context | agreed; three-axes and mini-network embedded | `content/foundation-context/index.md` |
| Finding Models and Common Data Elements (hub) | agreed, reviewed | `content/foundation-context/finding-models-and-cdes.md` |
| The next-generation schema | agreed, reviewed; dated CDE figure embedded | `content/foundation-context/next-generation-schema.md` |
| Relationships among definitions | agreed, reviewed | `content/foundation-context/relationships.md` |
| Standard clinical metadata | text proposed, not agreed | not written |

## Figures

| Figure | For | Status |
|---|---|---|
| Two planes v10 | Overview | accepted 2026-09-29; embedded |
| Three axes v6 | Foundation Context | embedded; awaits accept |
| Foundation mini-network v8 | Foundation Context | embedded; awaits accept |
| Pillars stack v8 (B3) | Overview | candidate; awaits accept |
| Two collections v1 | hub | candidate; awaits accept |
| Pulmonary nodule neighborhood v3 | Relationships; possibly replaces the dated figure on the schema page | candidate; awaits accept and placement |

Candidate SVGs are in ignored `scratch/review/candidates/`; on acceptance, the figure config points the figure at its page.

## Working rules

Page text is agreed with the project lead line by line and written by an Opus sub-agent that does not reword it. Organizations only; nothing called "the specification"; dated versions side by side. Figures through `tools/diagrams/`, looked at before reporting. Every tool or approach choice reviewed with the project lead first. Commits only on his explicit yes.
