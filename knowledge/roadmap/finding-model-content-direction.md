---
type: Roadmap
title: Finding model content direction
description: Exam-oriented content priorities, unmatched taxonomy rows, unmerged batches, and corpus cleanup plans.
tags: [roadmap, finding-models, content, taxonomy, gamuts, cleanup]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
stale_after: 2027-09-21
sources:
  - id: plan
    resource: /plans/2026-09-20-knowledgebase-build-plan.md
    title: Knowledgebase build plan, recording the project lead's statement of 2026-09-21
  - id: lists-readme
    resource: https://github.com/openimagingdata/findingmodels/blob/a30c3c95fa3943e7340ce87575f4b1b926987eb8/lists/README.md
    title: MGB exam-oriented sub-taxonomies README, findingmodels taxonomy-export-2026-08-15 branch
  - id: cleanup
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/docs/plans/definition_cleanup.md
    title: Definition Cleanup Plan, findingmodels main branch
  - id: rebuild-skills
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/docs/plans/rebuild-finding-skills.md
    title: Rebuild finding skills plan, findingmodels main branch
  - id: chest-progress
    resource: https://github.com/openimagingdata/findingmodels/blob/0472a4673fe476ec5335e6b3a1197faa70480426/docs/cdestaging_ct_chest_batch_progress.md
    title: CDEStaging CT chest batch progress, findingmodels content/chestcts branch
  - id: chest-plan
    resource: https://github.com/openimagingdata/findingmodels/blob/0472a4673fe476ec5335e6b3a1197faa70480426/PLAN.md
    title: Three-agent pipeline plan, findingmodels content/chestcts branch
  - id: headct-plan
    resource: https://github.com/openimagingdata/findingmodels/blob/42dfeb7627d486a7a698f8c619eee71b1e7d2a02/docs/plans/soft-tissue-headct-batch.md
    title: Soft tissue head CT batch plan, findingmodels content/headcts branch
  - id: data-history
    resource: https://github.com/openimagingdata/findingmodels/blob/dcc6c4cfe9f359e5ae582f898ff3dbcf48a3be4f/docs/plans/metadata-enrichment-plan-history-2026-05-24.md
    title: Metadata enrichment plan history, findingmodels findingmodels-metadata branch
  - id: issue-15
    resource: https://github.com/openimagingdata/findingmodels/issues/15
    title: findingmodels issue 15, "Bring in CDE Staging MD content"
  - id: issue-16
    resource: https://github.com/openimagingdata/findingmodels/issues/16
    title: findingmodels issue 16, "Add Knee MRI findings"
  - id: issue-19
    resource: https://github.com/openimagingdata/findingmodels/issues/19
    title: findingmodels issue 19, "Bring in abdomen CT findings"
  - id: issue-20
    resource: https://github.com/openimagingdata/findingmodels/issues/20
    title: findingmodels issue 20, "Incorporate Chest CT green findings, CXR devices/postop lists"
  - id: issue-25
    resource: https://github.com/openimagingdata/findingmodels/issues/25
    title: findingmodels issue 25, "Incorporate CDE definitions from RadElement as FindingModel objects"
  - id: ids-json
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/ids.json
    title: ids.json, the identifier registry, findingmodels main branch
---

# The stated direction

The project lead stated on 2026-09-21, recorded in [the knowledgebase build plan](/plans/2026-09-20-knowledgebase-build-plan.md), that the MGB exam-oriented sub-taxonomies are the immediate direction for all [finding model](/glossary/finding-model.md) content, and that they are expected to replace many of the [Gamuts](/glossary/gamuts.md)-derived models that currently make up 1,933 of the corpus's 2,382 definitions.[^plan]

That is a change in how content is chosen. The Gamuts import brought in whatever the source ontology contained, which is a differential-diagnosis ontology, so a large share of the resulting definitions name diagnoses rather than findings. The sub-taxonomies instead enumerate what a radiologist reading a particular [exam type](/glossary/exam-type.md) actually reports, organized by that exam type. The artifacts themselves, their columns, counts, and hierarchy semantics, are described in [the sub-taxonomies reference](/semantic-foundation/finding-models/finding-taxonomies.md).

No plan document in the `findingmodels` repository yet describes how or when Gamuts-derived models would be superseded. The statement is direction, not a scheduled workstream.

# The triage task

The sub-taxonomy export minted no identifiers. Rows were matched by exact name against the identifier registry across all branches, plus identifiers previously written back into the old lists.[^lists-readme]

| | Rows |
|---|---:|
| Total across the six files | 3,789 |
| Carrying an existing OIFM identifier | 1,028 |
| Blank, awaiting triage | 2,761 |

The README states: "Blank rows are the ones needing triage."[^lists-readme] Match rates are uneven, from 86 percent on head CT and 76 percent on chest radiography down to 10 percent on the combined chest, abdomen, and pelvis CT file and 3 percent on mammography. No plan document assigns the triage work, and no issue tracks it.

# Content batches in flight

Five `findingmodels` branches carry unmerged content work. None has an open pull request. Counts are of new definition files against `main`.

| Branch | Last commit | New definitions | What it is |
|---|---|---:|---|
| `content/chestcts` | 2026-06-19 | 1,822 | CT chest conversion from the `CDEStaging` corpus, using a three-agent merge, create, and review pipeline |
| `content/headcts` | 2026-06-03 | 419 | Head CT batch, reviewed through the terminal review tool, with its own source taxonomy CSV |
| a second head CT review branch | 2026-05-13 | 76 | Overlapping review passes for the extrinsic, orbit, and temporal bone regions, sharing the head CT source taxonomy |
| a clinician-request branch | 2025-12-12 | 59 | A requested batch for an intracranial problem list application |
| `findingmodels-metadata` | 2026-06-01 | 0, modifies 78 | Applies an approved metadata enrichment baseline to existing definitions |

Its plan records the refactor from one monolithic agent into three focused ones with Python-level orchestration, with phases 1 through 3 complete and two follow-ups open: the create agent extracts fewer attributes than the single-agent version did, and the sub-findings schema is unresolved.[^chest-plan] Its progress document is explicit about how far the batch has run: 205 total sources, chunked into 21 groups of 10, with chunk 1 complete and chunks 2 through 21 pending.[^chest-progress]

The head CT branch's one plan document is marked complete for the soft tissue category: four new models created, nine mappings made to existing models, review done, identifiers written back, validator clean.[^headct-plan]

An earlier CT chest branch, `cde_to_finding`, holds 1,915 definitions from the same source corpus and is 103 commits behind `main`. It is superseded by the three-agent branch, not a parallel effort.

# The definition cleanup plan

A draft plan on `main`, still marked "DRAFT - for review," covers cleaning the existing corpus against the authoring conventions. It scopes 2,379 models: 1,934 Gamuts, 264 OIDM already reviewed, 115 from the common data element work, 47 from MassGeneral Brigham, and 19 from Microsoft.[^cleanup]

The plan orders the work as follows.

| Order | Category | Models | Nature of the work |
|---:|---|---:|---|
| 1 | Capitalization and parentheticals | 133 | Mechanical: lowercase names, acronyms and brand names move to synonyms |
| 2 | Missing standard attributes | 124 | Add [presence](/glossary/presence.md) and [change from prior](/glossary/change-from-prior.md) as the first two attributes, with clinically appropriate direction-of-change values |
| 3 | Population qualifiers | 84 | Strip age or population from the name, tag instead, and later migrate the tags to explicit age ranges |
| 4 | Synonym audit | not counted | Run the synonym strictness rules across the corpus |
| 5 | "With" clauses | 71 | Case-by-case clinical judgment |
| 6 | Comma, slash, and and-or compounds | 18 | Individual attention |
| 7 | Gamuts reclassification | to be determined | "needs broader design discussion about what model types we support" |

The 71 "with"-clause models are all Gamuts-derived and the plan splits them into three kinds. Some are a finding plus an associated finding that should become two models, as in "arthritis with soft-tissue nodules." Some are a finding plus a qualifier that is really an [attribute](/glossary/attribute.md), as in "bowel wall thickening with heterogeneous enhancement." And some are genuinely Gamuts constructs, radiographic patterns used to narrow a differential, such as "acyanotic congenital heart disease with increased pulmonary vascularity." For that third kind the plan records that they "may be better modeled as gamuts (differential diagnosis patterns) rather than finding models" and flags them for discussion.[^cleanup]

Two standing rules accompany the plan. Changes to Gamuts models preserve the original name as a synonym so existing Gamuts references still resolve. And each phase runs through the mechanical lint plus language-model review process before committing.[^cleanup]

A second open plan on `main`, the finding skills rebuild, has phases 0 through 8 complete and phases 9 and 10, end-to-end verification and the final plan update, outstanding.[^rebuild-skills]

# The evidence-gated metadata branch

The metadata branch in the content repository operates under rules that are themselves a stated direction for how generated content enters the corpus. Its consolidated plan history states that "Human review is authoritative," that generated definition, markdown, and index changes are "untrusted until approved evidence is safely captured," that generated source diffs "are not gold," and that approved changes are reapplied "only through an explicit approved-output application path."[^data-history]

The review evidence it protects: a 150-item pilot review yielding 46 approved and 104 requiring feedback, refined after a 30-item follow-up to 67 approved and 83 requiring feedback.[^data-history] The tooling side of this work is in [the enrichment pipeline](/semantic-foundation/finding-models/enrichment-pipeline.md).

# Open content issues

Five of the ten open `findingmodels` issues are content batches. None is closed by any branch in flight, though two overlap with one.

| Issue | Asks for | Relation to work in flight |
|---|---|---|
| 15 | A script that converts a markdown definition file, merging with an existing model where one exists and reusing identifiers and synonyms, adding the right contributor | Answered by unmerged work. The triage and conversion scripts on the CT chest branch read the same source directory and write validated definitions, but nothing proposes merging them, so whether the issue is closed as filed is unresolved |
| 16 | Knee MRI findings, starting from a spreadsheet and finding an automatable format | No branch |
| 19 | Abdomen CT findings from an MGB-contributed list, checked against the Gamuts content and updated or created as needed | No branch |
| 20 | Chest CT "green" findings plus chest radiograph device and post-operative lists | No branch |
| 25 | A converter from common data element JSON version 1.0 into finding models, with a stated identifier mapping (`RDES195` to `OIFM_CDE_000195`, `RDE1300` to `OIFMA_CDE_001300`), an index code back to the original at every level, and detailed value-mapping rules | Conceptually overlaps the stale CDE-to-finding branch |

Two further open issues, 17 and 32, ask for a static marketing site and a static catalog site for the content; the catalog site exists and is profiled in [the finding models site](/applications/finding-models-site.md).

See [the content catalog](/semantic-foundation/finding-models/content-catalog.md) for organization and browsing, and [identifiers](/semantic-foundation/finding-models/identifiers.md) for writeback rules.[^ids-json] Where sources disagree about corpus counts and content classification, see [open questions](/roadmap/open-questions.md).

[^plan]: Knowledgebase build plan, recording the project lead's statement of 2026-09-21
[^lists-readme]: MGB exam-oriented sub-taxonomies README, taxonomy-export-2026-08-15 branch
[^cleanup]: Definition Cleanup Plan, findingmodels main branch
[^rebuild-skills]: Rebuild finding skills plan, findingmodels main branch
[^chest-plan]: Three-agent pipeline plan, content/chestcts branch
[^chest-progress]: CDEStaging CT chest batch progress, content/chestcts branch
[^headct-plan]: Soft tissue head CT batch plan, content/headcts branch
[^data-history]: Metadata enrichment plan history, findingmodels-metadata branch
[^issue-15]: findingmodels issue 15
[^issue-16]: findingmodels issue 16
[^issue-19]: findingmodels issue 19
[^issue-20]: findingmodels issue 20
[^issue-25]: findingmodels issue 25
[^ids-json]: ids.json, findingmodels main branch
