---
type: Glossary Term
title: Tag
description: A free-text clinical category attached to a finding model for organization and retrieval, distinct from the typed structured metadata that is replacing it.
tags: [glossary, semantic-foundation, finding-models]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: fm-py
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/finding_model.py
    title: TagSequence field description in the findingmodel package
  - id: overview
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/oifm-overview.md
    title: "Finding Models: Overview, anatomy of a finding model"
  - id: metadata-rewrite
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/canonical-structured-metadata-and-enrichment-rewrite.md
    title: Canonical structured metadata and enrichment rewrite, feature/metadata-cleanup branch
---

# Tag

"Tags that might be used to categorize the finding among other findings."[^fm-py] Tags are an optional list of free-text strings on a [finding model](/glossary/finding-model.md). The authoring guidance describes them as "clinical categories (anatomy, modality, etiology) for organization and retrieval."[^overview]

Tags are untyped and unvalidated. A real definition in the corpus carries `["ultrasound", "CT", "US", "XR", "urological", "obstructive", "diagnosis"]`, mixing modality abbreviations, two spellings of the same modality, a subspecialty, an etiology, and an entity type in one list. The metadata rewrite addresses this inconsistency.

## Synonyms and near-synonyms

- **Structured metadata field** is the typed successor. The documented rewrite adds `body_regions`, `subspecialties`, `etiologies`, `entity_type`, `applicable_modalities`, `expected_time_course`, `age_profile`, and `sex_specificity` as optional fields with closed value sets.[^metadata-rewrite]
- **Facet** was the earlier name for that same idea under an eight-facet scheme; it is superseded by the field set above.
- **[Index code](/glossary/index-code.md)** is not a tag. It points into an external ontology; a tag does not.
- **Category** in a [finding taxonomy](/glossary/finding-taxonomy.md) is a separate per-row anatomic grouping, not this field.

## Identifier form

None. Tags are bare strings with no registry.

## Where it is used

[Finding model format](/semantic-foundation/finding-models/finding-model-format.md) and [Enrichment pipeline](/semantic-foundation/finding-models/enrichment-pipeline.md).

## Conflicts

Tags and the new typed fields overlap: a tag reading `CT` and an `applicable_modalities` entry of `CT` say the same thing in two places. The rewrite specifies that structured metadata should be the model's own state rather than sidecar output, but it does not say what becomes of the existing tag lists, and nothing has landed on `main`.[^metadata-rewrite]

[^fm-py]: TagSequence field description in the findingmodel package
[^overview]: "Finding Models: Overview"
[^metadata-rewrite]: Canonical structured metadata and enrichment rewrite
