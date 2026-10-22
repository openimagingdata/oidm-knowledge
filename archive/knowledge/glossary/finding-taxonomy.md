---
type: Glossary Term
title: Finding taxonomy
description: One of the six MGB exam-oriented sub-taxonomies, per-modality hierarchies of finding names exported as CSV, that now set the content direction for the finding model corpus.
tags: [glossary, semantic-foundation, finding-models, content]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: lists-readme
    resource: https://github.com/openimagingdata/findingmodels/blob/a30c3c95fa3943e7340ce87575f4b1b926987eb8/lists/README.md
    title: MGB exam-oriented sub-taxonomies README, taxonomy-export-2026-08-15 branch
---

# Finding taxonomy

One of the six MGB exam-oriented sub-taxonomies: per-modality hierarchies of radiology finding names, contributed by Mass General Brigham and exported to the `findingmodels` repository on 2026-08-15 as comma-separated files.[^lists-readme] They replaced the repository's earlier `lists/` content wholesale.

Each file is one hierarchy with the columns `name`, `category`, `parent`, `synonyms`, `finding_type`, `finding_cluster`, and `oifm_id`. The unique `name` keys each row within a file. There is no separate row identifier. `parent` holds the parent row's `name`, or is blank for a top-level row. "Parents are generic, children add specificity," as in `lung_abnormality`, then `airspace_opacity`, then `air_bronchogram`. Two columns are outside the hierarchy: `category` is "an independent anatomic grouping, not part of the hierarchy," and `finding_type` "separates an observation from a diagnosis."[^lists-readme]

| File | Rows | OIFM IDs filled |
|---|---:|---:|
| `xr_chest_findings.csv` | 403 | 305 |
| `xr_msk_findings.csv` | 259 | 40 |
| `ct_head_findings.csv` | 520 | 449 |
| `ct_chest_abdomen_pelvis_findings.csv` | 2064 | 207 |
| `mg_breast_findings.csv` | 198 | 5 |
| `mri_spine_findings.csv` | 345 | 22 |
| Total | 3789 | 1028 |

No identifiers were minted during the export. Filled rows were matched by exact name against `ids.json`, and the blank rows are stated to be "the ones needing triage."[^lists-readme]

## Synonyms and near-synonyms

- **Finding list** is the older name for the files these replaced.
- A [finding taxonomy](/glossary/finding-taxonomy.md) row gives a name and hierarchy position. A [finding model](/glossary/finding-model.md) defines the finding and its attributes.
- The taxonomies are named after their author in the source repository. This knowledgebase calls them the MGB exam-oriented sub-taxonomies.

## Identifier form

None. Rows are keyed by `name` and carry an [OIFM](/glossary/oifm.md) identifier only where one already existed.

## Where it is used

[Finding taxonomies](/semantic-foundation/finding-models/finding-taxonomies.md) and [Finding model content direction](/roadmap/finding-model-content-direction.md).

## Conflicts

An identifier "can appear on two rows where those earlier writebacks mapped two findings onto one model," so the mapping from taxonomy row to finding model is not one to one.[^lists-readme] The `finding_type` observation-versus-diagnosis split also overlaps the `entity_type` field the metadata rewrite introduces, which has seven values rather than two.

[^lists-readme]: MGB exam-oriented sub-taxonomies README
