# Sources, bundle, and presentation: the three layers

Status: Agreed in principle 2026-10-01 (the four open points answered); execution not yet started. Written by Claude from the project lead's description. Companion: `docs/HANDOFF.md` holds everything else an agent needs.

## The project lead's description, verbatim

> I'd like to have a literal knowledge bundle of OKF files which are mostly for internal team use. They're in a public repo, and anyone can look at them and see what they see, but they're not what we'd present. We'd ALSO like to have a series of interconnected pages that ARE intended as the outward presentation of these ideas, where the knowledge for them is a distillation of the broader knowledgebase to make it more accessible to outsiders.

> I would ALSO like to maintain something like source material. I will create a non-public bucket on tigris for raw source material (presentations, manuscripts, emails, etc.). I (or people I give appropriate credentials to) can access that bucket to fill out a raw-sources directory, but this is NOT in the repo. We will generate DETAILED distilled summaries with key quotes and ESPECIALLY extracted graphics into a references directory. We can cite these in our knowledge bundle as needed, and if required go back and dig into the raw source.

> I would promote "paraphrase and describe figures" to "generate new versions of the figures capturing key points".

## The layers

| Layer | Where | In the repo? | Audience | Content |
|---|---|---|---|---|
| Raw sources | private Tigris bucket, mirrored to `raw-sources/` | no (gitignored); a manifest is | credentialed team | presentations, manuscripts, emails, boards, spreadsheets, as supplied |
| References | `knowledge/references/` | yes | team | one OKF Reference per raw source: detailed distilled summary, key quotes where allowed, figures (extracted or redrawn), pointer to the raw file |
| Knowledge bundle | `knowledge/` | yes | team (public by virtue of the repo) | comprehensive OKF concepts mined from every source, citing references; reorganized under the five pillars over time |
| Presentation | `pages/` | yes | outsiders | the interconnected pages agreed with the project lead, each a distillation citing bundle pages; what the site builds |

Each layer cites the one below it. Nothing on the site links into the raw layer.

## Raw sources

- The bucket is `oidm-knowledge-sources` on Tigris, private; credentials are the project lead's to grant and are never recorded in the repo.
- `raw-sources/` is gitignored. A `raw-sources/MANIFEST.json` (tracked) lists each file: bucket path, size, SHA-256, date added, a one-line description, and a sensitivity class (`public`, `restricted-until-published`, `internal`).
- A task `task sources:pull` mirrors the bucket into the directory with the t3 tool; `task sources:check` verifies the manifest against the directory.
- The current `sources/` directory becomes `raw-sources/` once the bucket exists; its extracted text and the bucket report move with it. Nothing in it is deleted.

## References

One document per raw source, type `Reference`, from a fixed template:

- frontmatter: title; the raw file's manifest id and checksum; producing organization; date; status of the source (public talk, manuscript under review, internal board, email note); sensitivity class; who extracted it and when.
- body: what the source is and why it matters; a detailed distilled summary, section by section; key quotes, each with its location; the source's figures, one subsection each, with the figure file beside the reference; the claims other documents are likely to cite, each with its location; open questions the source raises.
- figures: for `public` sources, extracted as supplied (with the extraction method recorded); for `restricted-until-published` and `internal` sources, redrawn with the diagram tooling as a new figure capturing the key point, the builder recording which source figure it distills. The original stays in the raw layer.
- rules: organizations only, never an individual; reviewer correspondence never summarized or quoted; for a manuscript under review, no quotes until published; vendor names generalized where the project lead has said so.

## Knowledge bundle

Unchanged in role: the comprehensive, team-facing OKF bundle. Changes from this plan:

- Concepts cite references by id instead of gitignored paths or bucket URLs.
- The bundle's own reorganization under the five named pillars (Foundation Context, Data Structures, SDKs, Use Cases, Sample Applications) is a separate track, mostly Astra and agent work, since its readers are the team. Nothing is deleted for being too detailed; the glossary stays dropped per the 2026-09-29 decision.

## Presentation

- The pages agreed with the project lead move from `knowledge/drafts/` to `pages/`, in the directory layout of `docs/plans/2026-09-22-layout-plan.md`, with the Overview at the root.
- The public site builds from `pages/` only. A separate internal site builds from `knowledge/` (the bundle) as its own Cloudflare static Worker, for the team.
- Release gating, decided 2026-10-01: no presentation page reaches the production site until the project lead has reviewed it (`verified` set by `task verify`). Pre-review pages go only to staging, and EVERYTHING deployed to staging carries a visible "DRAFT / Awaiting Review" label on every page. The production build fails if any page lacks a `verified` entry.
- Presentation pages keep frontmatter (status, provenance, sources) and cite bundle pages; the same validators run on both directories.

## Steps, once agreed

1. Manifest and sync task; move `sources/` to `raw-sources/`; gitignore update.
2. Reference template; convert the eight sources already summarized (the two SIIM decks, the January deck, the three manuscripts, the reporting-schema deck, the AI-evolution essay) and the board transcription into references; redraw figures for restricted sources.
3. Re-point bundle citations at the references.
4. Create `pages/`, move the agreed drafts, point the public site build at it, reorder the explorer to the five pillars, make the Overview the landing page.
4a. Site gating: a build-time switch that stamps "DRAFT / Awaiting Review" on every page for dev and staging builds, and a production build that refuses any page without a `verified` entry. Reviewed with the project lead before implementing (tool and approach choices are always reviewed first).
4b. Internal site: a third Worker (`oidm-knowledge-internal`) building the bundle from `knowledge/` with the same banner rule; access control to be decided with the project lead (Cloudflare Access is the obvious candidate; review first).
4c. Deploy the presentation to dev, then staging, for the project lead's verification pass.
5. Dashboard and layout plan updated; DEV_LOG and CHANGELOG entries.

## Decisions, 2026-10-01

- Presentation directory: `pages/`.
- The bundle gets an internal site build on a Cloudflare static Worker.
- Nothing pre-review on production; staging only, every page labeled "DRAFT / Awaiting Review".
- Bucket: `oidm-knowledge-sources` (private).
