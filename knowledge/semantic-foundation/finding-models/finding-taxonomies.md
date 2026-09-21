---
type: Reference
title: MGB exam-oriented sub-taxonomies
description: The six exam-oriented finding hierarchies contributed by MassGeneral Brigham, their columns and hierarchy semantics, their row and match counts, and the triage they call for.
tags: [semantic-foundation, finding-models, taxonomy, content, reference]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
sources:
  - id: lists-readme
    resource: https://github.com/openimagingdata/findingmodels/blob/a30c3c95fa3943e7340ce87575f4b1b926987eb8/lists/README.md
    title: MGB exam-oriented sub-taxonomies README, findingmodels taxonomy-export-2026-08-15 branch
  - id: xr-chest
    resource: https://github.com/openimagingdata/findingmodels/blob/a30c3c95fa3943e7340ce87575f4b1b926987eb8/lists/xr_chest_findings.csv
    title: xr_chest_findings.csv, findingmodels taxonomy-export-2026-08-15 branch
  - id: ct-head
    resource: https://github.com/openimagingdata/findingmodels/blob/a30c3c95fa3943e7340ce87575f4b1b926987eb8/lists/ct_head_findings.csv
    title: ct_head_findings.csv, findingmodels taxonomy-export-2026-08-15 branch
  - id: ids-json
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/ids.json
    title: ids.json, the identifier registry, findingmodels main branch
  - id: build-plan
    resource: /plans/2026-09-20-knowledgebase-build-plan.md
    title: Knowledgebase build plan, recording the project lead's statement of 2026-09-21
---

# What they are

The MGB exam-oriented sub-taxonomies are six hierarchies of radiology finding names, contributed by MassGeneral Brigham and exported into the `findingmodels` repository on 2026-08-15. They live on the branch `taxonomy-export-2026-08-15`, read here at commit `a30c3c9`, which replaces the repository's earlier `lists/` directory wholesale and adds no finding model definitions of its own.[^lists-readme]

Each file is a comma-separated table. Together they hold 3,789 rows, of which 1,028 already carry the identifier of an existing [finding model](/glossary/finding-model.md).

| File | Modality and region | Rows | OIFM identifiers filled | Top-level rows |
|---|---|---:|---:|---:|
| `xr_chest_findings.csv` | radiography, chest | 403 | 305 | 23 |
| `xr_msk_findings.csv` | radiography, musculoskeletal | 259 | 40 | 16 |
| `ct_head_findings.csv` | CT, head | 520 | 449 | 34 |
| `ct_chest_abdomen_pelvis_findings.csv` | CT, chest, abdomen, pelvis | 2,064 | 207 | 68 |
| `mg_breast_findings.csv` | mammography, breast | 198 | 5 | 25 |
| `mri_spine_findings.csv` | MRI, spine | 345 | 22 | 19 |
| Total | | 3,789 | 1,028 | 185 |

# Columns

```
name,category,parent,synonyms,finding_type,finding_cluster,oifm_id
```

| Column | Meaning |
|---|---|
| `name` | the row key, in lower snake case, unique within its file, so there is no separate identifier column |
| `category` | an independent anatomic grouping, explicitly "not part of the hierarchy" |
| `parent` | the `name` of the parent row; blank means top level |
| `synonyms` | alternate terms, comma-separated inside the field |
| `finding_type` | separates an observation from a diagnosis |
| `finding_cluster` | a grouping used on 103 of the 3,789 rows |
| `oifm_id` | the identifier of an existing finding model, where one matched |

# Hierarchy semantics

Each file is one hierarchy, expressed by `parent` pointing at another row's `name` within the same file. "Parents are generic, children add specificity," and the worked example given is `lung_abnormality`, then `airspace_opacity`, then `air_bronchogram`.[^lists-readme] A row with an empty `parent` is a root; there are 185 roots across the six files.

Two columns sit deliberately outside that tree. `category` groups rows anatomically without implying containment, so the chest radiograph file assigns rows to `lung`, `airway`, `pleura`, `mediastinal`, `cardiac`, `osseous`, `soft_tissue`, `diaphragm`, `abdomen`, `devices`, and `image_quality`. `finding_cluster` is populated only where rows belong to a named group.

`finding_type` carries one of two values across the corpus, with a substantial number of rows leaving it blank.

| Value | Rows |
|---|---:|
| `observation` | 2,443 |
| `diagnosis` | 932 |
| blank | 414 |

That split mirrors the distinction the finding model work elsewhere calls entity type, where a finding is what you see and a diagnosis is what you conclude. Blank rows are mostly the generic parents, which exist to hold a subtree rather than to be reported.

Two real rows show the shape:

```csv
name,category,parent,synonyms,finding_type,finding_cluster,oifm_id
airway_abnormality,airway,,,,,OIFM_OIDM_449436
airspace_opacity,lung,lung_abnormality,"Air space opacity,Infiltrate,Airspace disease",observation,,OIFM_CDE_000225
```

The first is a top-level parent with no `finding_type`. The second is a child of `lung_abnormality`, typed as an observation, carrying three synonyms and matched to a definition that entered the corpus from the common data element work.

# Matching status and the triage task

No identifiers were minted during the export. Filled rows were matched by exact name against `ids.json` across all branches, plus identifiers previously written back into the old lists.[^lists-readme] The README records a consequence of those earlier writebacks: "An ID can appear on two rows where those earlier writebacks mapped two findings onto one model."

The match rate varies enormously by file. Head CT is 86 percent matched and chest radiography 76 percent, because both areas have had content batches run against them. Mammography is 3 percent matched and the combined chest, abdomen, and pelvis CT file 10 percent, against 2,064 rows.

The README names the next task in one sentence: "Blank rows are the ones needing triage." That is 2,761 rows. Triage means deciding, for each, whether an existing model covers it under a different name, whether it needs a new model, or whether it is not a finding at all. No plan document in the repository yet assigns that work.

# Why this matters

The project lead stated on 2026-09-21 that the sub-taxonomies are the immediate direction for all finding model content, and that they are expected to replace many of the Gamuts-derived models that currently make up 1,933 of the corpus's 2,382 definitions. That statement is recorded in [the knowledgebase build plan](/plans/2026-09-20-knowledgebase-build-plan.md).[^build-plan]

This is a change in how content gets chosen. The Gamuts import brought in whatever the source ontology contained. The sub-taxonomies instead enumerate what a radiologist reading a particular exam type actually reports, organized by the exam type. A finding model corpus built against them would be scoped to assessable anatomy per modality, which is the scoping rule the authoring guidance already states. The stated direction, and what depends on it, is in [the content direction roadmap](/roadmap/finding-model-content-direction.md).

The glossary entry for the artifact type is [finding taxonomy](/glossary/finding-taxonomy.md). The files themselves are on the branch and are not copied into this knowledgebase.

[^lists-readme]: MGB exam-oriented sub-taxonomies README, taxonomy-export-2026-08-15 branch
[^xr-chest]: xr_chest_findings.csv, taxonomy-export-2026-08-15 branch
[^ct-head]: ct_head_findings.csv, taxonomy-export-2026-08-15 branch
[^ids-json]: ids.json, findingmodels main branch
[^build-plan]: Knowledgebase build plan, recording the project lead's statement of 2026-09-21
