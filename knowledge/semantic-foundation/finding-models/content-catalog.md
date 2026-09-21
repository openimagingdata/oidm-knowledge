---
type: Project Profile
title: Finding model content catalog
description: "The findingmodels repository: what is in the corpus, where its identifiers and generated renders live, the conventions that govern it, how to browse it, and the content batches in flight on unmerged branches."
tags: [semantic-foundation, finding-models, content, repository, project-profile]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
stale_after: 2027-09-21
sources:
  - id: fm-claude
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/CLAUDE.md
    title: CLAUDE.md, repository conventions, findingmodels main branch
  - id: ids-json
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/ids.json
    title: ids.json, the identifier registry, findingmodels main branch
  - id: fm-index
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/index.md
    title: index.md, the generated corpus index, findingmodels main branch
  - id: cleanup-plan
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/docs/plans/definition_cleanup.md
    title: Definition Cleanup Plan, findingmodels main branch
  - id: chestcts
    resource: https://github.com/openimagingdata/findingmodels/blob/0472a4673fe476ec5335e6b3a1197faa70480426/docs/cdestaging_ct_chest_batch_progress.md
    title: CDEStaging CT chest batch progress, findingmodels content/chestcts branch
  - id: headcts
    resource: https://github.com/openimagingdata/findingmodels/blob/42dfeb7627d486a7a698f8c619eee71b1e7d2a02/docs/plans/soft-tissue-headct-batch.md
    title: Soft-tissue head CT batch plan, findingmodels content/headcts branch
  - id: mcp-doc
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/docs/mcp_server.md
    title: Finding Model MCP Server, findingmodel main branch
  - id: base-orgs
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/data/base_organizations.jsonl
    title: base_organizations.jsonl, the seeded organization registry, findingmodel main branch
  - id: site
    resource: https://openimagingdata.github.io/finding-models-site/
    title: Finding models catalog site
---

# What the repository is

`findingmodels` is the content repository of the Open Imaging Data Model (OIDM). It holds finding model definitions and nothing that executes them. The format those definitions obey lives in a different repository, `findingmodel`, and is described in [the format document](/semantic-foundation/finding-models/finding-model-format.md).

Read at commit `4475ac1` on `main`, dated 2026-04-28, the repository contains 2,382 definitions.

| Path | Contents | Generated |
|---|---|---|
| `defs/` | 2,382 `*.fm.json` definitions, one finding each | no, this is the source |
| `text/` | 2,382 markdown renders, one per definition | yes |
| `index.md` | a single table of the whole corpus, roughly 683 KB | yes |
| `ids.json` | the identifier registry, 2,382 finding and 5,709 attribute identifiers | yes |
| `schema/` | the prose schema mirror and a JSON schema file | no |
| `lists/` | the MGB exam-oriented sub-taxonomies | no |
| `prompts/` | authoring prompt fragments consumed by the agent skills | no |
| `scripts/` | the validator and the authoring helper scripts | no |

# Where the content came from

Every identifier carries a three-or-four-letter organization segment recording where the definition entered the corpus. Counting the registry gives the breakdown.[^ids-json]

| Code | Organization | Definitions |
|---|---|---:|
| `GMTS` | Radiology Gamuts Ontology | 1,933 |
| `OIDM` | Open Imaging Data Model | 256 |
| `CDE` | ACR/RSNA Common Data Elements Project | 115 |
| `MGB` | MassGeneral Brigham | 47 |
| `MSFT` | Microsoft | 31 |

Four in five definitions are Gamuts-derived. That fact shapes everything about the corpus's current state: the [Radiology Gamuts Ontology](/glossary/gamuts.md) is a differential-diagnosis resource rather than a finding vocabulary, so its imported entries carry patterns that do not sit comfortably as findings. The [content direction roadmap](/roadmap/finding-model-content-direction.md) records the stated intent that the [MGB exam-oriented sub-taxonomies](/semantic-foundation/finding-models/finding-taxonomies.md) replace many of them.

Two further organizations, `RSNA` and `ACR`, are registered in the package's seeded organization list but have contributed no definitions under their own codes.[^base-orgs] Individual contributors appear on definitions as `Person` records with a GitHub username, an email address, and an organization code; organizations appear as `Organization` records with a name, a code, and a URL.

# Conventions

The repository's own guidance file states the rules that govern changes.[^fm-claude]

- Three artifacts are auto-generated and must never be hand-edited: `text/*.md`, `index.md`, and `ids.json`. They are rebuilt from `defs/` by `uv run scripts/validator.py`.
- Every finding identifier must be unique, and every attribute identifier must be unique across all files, not merely within one. The validator fails the commit if either check fails.
- Definition files live in `defs/`, end in `.fm.json`, and take a snake_case name derived from the finding name.
- The validator also reformats the JSON in place, so committed definitions share one layout.
- A pre-commit hook runs the validator with `--with-git-adds` on every commit, so the generated files stay in step with the source without a separate step.
- Work reaches `main` by pull request.
- Definitions link to standard ontologies through `index_codes`, and the three named as common are SNOMED CT, RadLex, and the Radiology Gamuts Ontology.

A separate open plan, the definition cleanup plan, catalogs the conventions the existing corpus does not yet meet: title-cased names on 123 mostly `CDE` and `MGB` models, 124 models missing presence as their first attribute, 71 Gamuts models whose names embed a "with" clause, and 84 that embed a population qualifier. It is marked draft and for review.[^cleanup-plan] Its handling is described in [the authoring workflow](/semantic-foundation/finding-models/authoring-workflow.md).

# How to browse

Three routes exist, at different levels of convenience.

- **The repository.** Read `index.md` for the whole corpus as one table, then follow its links into `text/` for a rendered definition or `defs/` for the JSON.
- **The catalog site.** `finding-models-site` is a static Astro site that pulls the content repository in as a git submodule and renders `/models/` and `/models/[slug]` pages at build time. It is published at [openimagingdata.github.io/finding-models-site](https://openimagingdata.github.io/finding-models-site/) and profiled in [applications](/applications/finding-models-site.md).
- **Programmatic search.** The `findingmodel` package ships a Model Context Protocol server, `findingmodel-mcp`, exposing three tools to an agent: hybrid search over the index, retrieval of one model by identifier, name, or synonym, and a count of models, people, and organizations.[^mcp-doc] The same index is reachable from the `findingmodel` command-line interface.

# Content in flight

Six branches carry unmerged content work. None has an open pull request, and none is on `main`. The figures below are branch-to-`main` differences as of the dates given.

| Branch | Tip | New definitions | What it is |
|---|---|---:|---|
| `content/chestcts` | 2026-06-19 | 1,822 | The live CT chest front. Converts CDEStaging chest CT source material through a three-agent merge, create, and review pipeline. |
| `content/headcts` | 2026-06-03 | 419 | Head CT batch, reviewed through a terminal interface, working from a head CT finding list. |
| `km` | 2026-05-13 | 76 | Overlapping head CT review passes for the extrinsic, orbit, and temporal bone regions, sharing the same source list. |
| `bhatia-requests` | 2025-12-12 | 59 | A clinician-requested batch for an intracranial problem list application. |
| `findingmodels-metadata` | 2026-06-01 | 0 | Applies an approved enrichment baseline to 78 existing definitions and adds no new ones. |
| `taxonomy-export-2026-08-15` | 2026-08-15 | 0 | Replaces `lists/` with the six MGB exam-oriented sub-taxonomy files. |

The chest CT branch is the largest by far and the least complete: its own progress document records 205 source items split into 21 chunks of ten, with chunk 1 done and chunks 2 through 21 pending.[^chestcts] The head CT branch's plan document is marked complete for the soft tissue category, which produced four new models and nine mappings onto existing ones, with identifiers written back to the source list and the validator run clean.[^headcts]

Two consequences follow. First, the published corpus of 2,382 understates by roughly 2,400 the number of definitions that have been drafted somewhere. Second, the JSON schema file in `schema/` is being extended independently on three of these branches, with nothing landed on `main`.

Ten issues are open on the repository. Five request further content batches, including RadElement-derived definitions, chest CT and chest radiograph device lists, abdomen CT findings, knee MRI findings, and CDEStaging markdown content. Four cover tooling, including running the validator as a GitHub action and locking `main`. One asks for a static site with a landing page.

[^fm-claude]: CLAUDE.md, findingmodels main branch
[^ids-json]: ids.json, findingmodels main branch
[^fm-index]: index.md, findingmodels main branch
[^cleanup-plan]: Definition Cleanup Plan, findingmodels main branch
[^chestcts]: CDEStaging CT chest batch progress, content/chestcts branch
[^headcts]: Soft-tissue head CT batch plan, content/headcts branch
[^mcp-doc]: Finding Model MCP Server, findingmodel main branch
[^base-orgs]: base_organizations.jsonl, findingmodel main branch
[^site]: Finding models catalog site
