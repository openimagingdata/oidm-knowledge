---
type: Glossary Term
title: Body region
description: A coarse anatomic grouping such as thorax or abdomen, used to scope findings, to fall back when no structure is named, and to filter views.
tags: [glossary, semantic-foundation, anatomy]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: al-enums
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/anatomic-locations/src/anatomic_locations/models/enums.py
    title: AnatomicRegion enumeration in the anatomic-locations package
  - id: metadata-rewrite
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/canonical-structured-metadata-and-enrichment-rewrite.md
    title: Canonical structured metadata and enrichment rewrite, BodyRegion value set
  - id: rules
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/anatomic-location-assignment-rules.md
    title: Anatomic location assignment rules, exam-scoped region fallback
  - id: extraction
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/initial-extraction-plan.md
    title: Initial extraction plan, FindingLocation body_region values
---

# Body region

A coarse anatomic grouping, one level above an organ and well above a named structure. Regions do three jobs in OIDM: they classify an [anatomic location](/glossary/anatomic-location.md), they carry broad anatomy on a [finding model](/glossary/finding-model.md) where precise anatomy belongs in `anatomic_locations`, and they provide the fallback when a finding names no anatomic structure at all.

The fallback rule is explicit. Only findings with no anatomic noun, such as "soft tissue mass" or "generalized osteoporosis," fall back to the exam-scoped coarse region, and the grain is "the coarse region, not a soft-tissue substructure." The rule also states that "organ always wins over exam-region" whenever the finding has a real target organ, including edge-of-exam cases: "no consolidation" on an abdominal CT codes to lung, never to abdomen.[^rules]

## Synonyms and near-synonyms

- **Region** and **anatomic region** are the same thing; `region` is the field name on a location.
- **[Body system](/glossary/anatomic-location.md)** is orthogonal. Cardiovascular is a system, thorax is a region.
- **Category** in a [finding taxonomy](/glossary/finding-taxonomy.md) row is described as "an independent anatomic grouping" and behaves like a region but is not the same list.
- **Exam-scoped region** means a region chosen from the exam type rather than from the report text.

## Identifier form

No identifier. Regions are enumerated strings, and the fallback rule maps each one to a [RadLex RID](/glossary/radlex-id.md), for example abdomen to `RID56`, thorax to `RID1243`, head to `RID9080`.[^rules]

## Where it is used

[Data model](/semantic-foundation/anatomic-locations/data-model.md), [Finding model format](/semantic-foundation/finding-models/finding-model-format.md), and [Imaging Problem List viewer](/applications/imaging-problem-list-viewer.md).

## Conflicts

Four different region lists are in use and none is a superset of the others. The anatomic-locations package enumerates Head, Neck, Thorax, Abdomen, Pelvis, Upper Extremity, Lower Extremity, Breast, and Body.[^al-enums] The documented finding-model metadata field uses head, neck, chest, breast, abdomen, pelvis, spine, upper_extremity, lower_extremity, and whole_body, with legacy title-cased values normalizing and the legacy alias `ALL` mapping to whole_body.[^metadata-rewrite] The extraction schema uses chest, abdomen, pelvis, head, neck, spine, upper extremity, lower extremity, and breast.[^extraction] The viewer filters on Chest, Abdomen, Pelvis/GU, Musculoskeletal, and Head/Neck. Thorax and chest, and the presence or absence of spine, are the recurring mismatches.

[^al-enums]: AnatomicRegion enumeration
[^metadata-rewrite]: Canonical structured metadata and enrichment rewrite
[^rules]: Anatomic location assignment rules
[^extraction]: Initial extraction plan
