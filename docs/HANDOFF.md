# Handoff: everything an agent needs to work on this repository

Written 2026-10-01 by the Claude session that has worked with the project lead since 2026-09-20. Read this first, then the plans it points to. The project lead is the only person named in this repository; everyone else is an organization.

## What this is

A public knowledgebase for the Open Imaging Data Model (OIDM), in four layers (`docs/plans/2026-10-01-sources-and-layers.md`):

1. **Raw sources**: a private Tigris bucket `oidm-knowledge-sources`, mirrored to gitignored `raw-sources/` (today still `sources/`), with a tracked manifest. Not in the repo.
2. **References**: `knowledge/references/`, one OKF Reference per source with a detailed summary, key quotes where allowed, and figures. Figures from unpublished or internal sources are redrawn with the diagram tooling, never reproduced.
3. **The knowledge bundle**: `knowledge/`, the comprehensive team-facing OKF 0.2 bundle (115 concepts as of 2026-09-21), public only because the repository is. Reorganizing it under the five pillars is Astra's track.
4. **The presentation**: `pages/` (not yet created; the agreed pages are still in `knowledge/drafts/`), the outward pages distilled from the bundle, the only thing the public site builds. Layout in `docs/plans/2026-09-22-layout-plan.md`; status in `docs/plans/restructure-dashboard.md`.

## The structure of the ideas

Five named pillars, always used by name and never numbered: **Foundation Context** (the shared, curated clinical knowledge: finding/diagnosis definitions, anatomic locations, exam types, and the relationships among them), **Data Structures** (the patient side: Observation, Exam Finding List, Imaging Problem List, Imaging Persona, and how the patient graph and the foundation graph are woven together), **SDKs**, **Use Cases** (the team's documented possible applications), **Sample Applications** (what was actually built). An Overview page sits above them.

Rulings that govern content, all from the project lead and recorded verbatim in `docs/plans/restructure-joint-notes.md` ("Decisions of 2026-09-22") and `docs/plans/2026-09-22-layout-plan.md` ("The guidance, verbatim"):

- A CDE and a finding model are the same kind of content in two collections: Open Imaging Finding Models (inclusive, beta channel, maintained by the OIDM project) and ACR/RSNA Common Data Elements (well-reviewed, release channel, radelement.org). Both are moving onto the next-generation graph schema being developed in the CDE project; reorganizing OIFM around it is an immediate priority.
- OIDM models the whole imaging workflow context across its lifecycle; the current focus is data structures and semantics for imaging results. The Imaging Persona integrates imaging results into one larger graph of the patient's history, underpinned by Foundation Context.
- Nothing is formally specified. Never call any source "the specification" or "canonical". Show each source's version side by side, dated and attributed; never reconcile disagreements.
- Terminology: "finding/diagnosis definitions" for the WHAT axis ("Observation Type" is under consideration, not adopted); "Foundation Context" and "Patient Context"; the two graphs are "woven together" or "interconnected", never "pointers"; "connective tissue" only in the SIIM 2026 deck's sense (relationships and citations between foundation concepts). Measurements name a kind of quantity, not a unit. Use "defines" for node types, not "is a". Use the schema's own relationship names (MAY_MANIFEST_AS, ASSESSED_BY, ...) and its specificity words (pathognomonic, highly suggestive, suggestive).
- Organizations only. The reporting vendor stays generic; the organizations behind the 47 and 31 finding models stay generalized. Manuscripts under review: paraphrase, cite as under review, never quote, never touch reviewer correspondence. Internal boards: schema ideas only, no live links, no people, meetings, or vendor logistics. The project lead's own deck and the ACR-RSNA-CDEs repository figures may be reused.
- Repository documents, plans, prompts, skills, ADRs, and code are team artifacts and first-class sources; carry each source's own status, date, and provenance labels (the CDE decision record's OWNER / CLAUDE DEFAULT). Only an agent's own inference is kept out.
- Read only committed files at a pinned commit in the CDE repository; its working tree holds uncommitted decisions (S53 to S67) and newer graph files that cannot be cited until committed.
- The old 48-term glossary is dropped; a new one grows from the presentation pages as terms earn entries.

## How work is done

- **Pages**: the project lead and the Claude session agree the page text line by line in conversation (one page at a time, actual content, not descriptions). The project lead's words go verbatim into the layout plan's "guidance" section so pages can cite them. An **Opus** sub-agent then writes the page from the agreed text (frontmatter, citations verified against pinned sources, validation) and must not reword it. **Astra** (the Codex session in this workspace's second tab) reviews for source fidelity, writing findings to `sources/review/drafts-<page>.md`; the writer applies footnote findings and writes dispositions to `drafts-<page>-response.md`; prose questions go back to the project lead.
- **Figures**: design agreed in conversation, built by an Opus sub-agent as an Excalidraw builder in `tools/diagrams/` (helpers in `excalib.py`; icons and licenses in `tools/diagrams/icons/`), rendered and LOOKED AT before reporting; the Claude session looks again; the project lead accepts. Renders for review go in `docs/plans/renders/` (tracked) because `sources/` is gitignored and peruse will not open it. Conventions in `tools/diagrams/README.md`: shared palette by node kind, assessment schemes as purple ovals (never diamonds), solid small arrowheads, schema relationship names on boxed labels, 13px minimum text, no Mermaid, no "pointer".
- **Models**: implementation runs in Opus sub-agents (always pass the model explicitly) or in the codex-impl tabs; never Sonnet for judgment work; never the Fable session itself without explicit clearance. Review every tool or approach choice with the project lead before adopting it.
- **Astra**: find its pane with `herdr pane list` (the codex pane whose cwd is this repo), read it before sending, send with `herdr pane run <pane> "<one-line pointer>"`, and record handoffs in `docs/plans/restructure-joint-notes.md` under "Handoffs". Never ask the project lead to relay. Never commit Astra's uncommitted work unasked; group commits by what belongs together, not by author.
- **Review surface**: the project lead reads files in peruse (`http://agent-dev:7440/p/oidm-knowledge/`); root-absolute links (`/knowledge/...`) resolve there. Keep `docs/plans/restructure-dashboard.md` current whenever a status changes.
- **Git**: branch `bootstrap`, pushed; PR #1 from `bootstrap` into `main` (which the project lead merges). A global pre-push hook refuses any push to `main`; this checkout has `remote.pushDefault=parent`, so push with the remote named: `git push origin bootstrap`. Never commit without the project lead's explicit yes; propose a concise message first. Never delete or overwrite a file you did not create (`links.txt` is the project lead's).
- **Validation**: `task check` runs the OKF 0.2 validator (`.agents/skills/validate/scripts/okf_validate.py knowledge --strict`) and the house checker (`tools/check_bundle.py`: index coverage, link resolution, trust-signal shape, denylist in gitignored `tools/denylist.txt`). Both must be clean before a commit. Index entries use `* [Title](./file.md) - description` with the description identical to the frontmatter; quote YAML descriptions containing colons.

## The site

Quartz 5.0.0 (pinned commit in `site/build.sh`) with YAML config in `site/`, local plugins `site/okf-meta-plugin` (frontmatter badges) and `site/okf-lightbox-plugin` (click-to-zoom), staged by `tools/prepare_site_content.py`; hosted as Cloudflare Workers static assets (`site/wrangler.jsonc`), targets dev (`task deploy`, https://oidm-knowledge-dev.talkasab.workers.dev), staging (`task deploy:staging`, also on push to `main` via `.github/workflows/deploy.yml`, needs `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` secrets, not yet set), prod (`task deploy:prod`; production domain knowledge.openimagingdata.org, not yet configured). Credentials are in the environment "to be cleaned up later". The permission classifier has refused `task deploy` from the Claude session once; the project lead can run it.

Decided 2026-10-01, not yet built: the public site builds from `pages/` only, the Overview as landing page, the explorer ordered by the five pillars; a separate internal Worker builds the bundle from `knowledge/`; dev and staging stamp "DRAFT / Awaiting Review" on every page; production refuses any page without a `verified` entry (`task verify -- <paths>` stamps it). The current deployed site is the 2026-09-21 bundle and does not match the plan.

## Where the sources are

- Repositories cloned read-only under `~/`: findingmodel, findingmodels, med-ontology-lookup, ACR-RSNA-CDEs (branch next-gen-2026), RadLex, imaging-problem-list (dev is current), FindingModelForge, CDEStaging, IPL-MVP-ExtractionAndLabeling, anatomiclocations.org, BodyPartIndex.py/.ts, UseCases, FHIRSamples, and the lineage repositories. Pins used so far are recorded in each page's sources.
- `~/exam-types/sources/LoincRsnaRadiologyPlaybook.xlsx`: Playbook entries (LongCommonName column) for exam-type names; a second sheet `core-playbook-dev` may be the project lead's working set.
- `sources/` (gitignored, to become `raw-sources/`): `bucket/` (manuscripts, decks, the AI-evolution essay, extracted text under `bucket/text/`, the reading in `bucket/REPORT.md`), `siim2026/` (the SIIM 2026 deck, its text and images), `excalidraw-diagrams.md` (15 boards with sensitivity flags), `email/2026-09-19-ipl-manuscript-notes.md`, `ipl-example2-study.md`, `review/` (every review and response file), `upstream-issues-draft.md` (22 drafted issues for the source repositories, awaiting the project lead).
- The SIIM 2026 deck (June 2026, public) is the central framing source; the January 2026 status update and the July 2026 webinar are the others; the openimagingdata.org posts are team sources.

## State on 2026-10-01

Agreed, written, reviewed (in `knowledge/drafts/`): `overview.md`, `foundation-context.md`, `finding-models-and-cdes-hub.md`, `next-generation-schema.md`, `relationships.md`. Figures: two-planes (accepted), three-axes v6, mini-network v8, two-collections v1, pillars v8 (castellated B3), nodule neighborhood v3, all awaiting the project lead's accept except two-planes; the pillars stack is not yet embedded in the Overview and the nodule figure is not yet placed (relationships page, and in place of the dated figure on the schema page). The standard-clinical-metadata page text is proposed in conversation and not yet agreed; it should carry the project lead's 2026-09-30 thought that time course and etiology may be properties of the edge to a diagnosis. The remaining pages of the layout plan have reviewed source material in the superseded Tuesday drafts (same directory) but are not written. Astra's brand-asset work (`docs/brand/`, `knowledge/assets/`, `docs/plans/2026-09-30-brand-assets.md`) is in progress and uncommitted.

Open with the project lead: the figure accepts above; the metadata text; CI secrets; the upstream issue drafts; the CDE decisions S53 to S67 to commit in the CDE repository.

## Memory for Claude sessions

Claude sessions in this project directory also load `~/.claude/projects/-home-talkasab-oidm-knowledge/memory/MEMORY.md`, which indexes the same rules as feedback notes. This file is the version other agents can read.
