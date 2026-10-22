---
type: Glossary Term
title: Index code
description: A reference from a finding model, attribute, or value to a concept in a standard ontology, carried as system, code, and optional display.
tags: [glossary, semantic-foundation, terminologies]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: index-code
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/oidm-common/src/oidm_common/models/index_code.py
    title: IndexCode model in the oidm-common package
  - id: claude-md
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/CLAUDE.md
    title: findingmodels repository conventions, common ontologies
  - id: metadata-rewrite
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/canonical-structured-metadata-and-enrichment-rewrite.md
    title: Canonical structured metadata and enrichment rewrite, feature/metadata-cleanup branch
  - id: cde-set-schema
    resource: https://github.com/openimagingdata/openimagingdata.org/blob/fb431dfc81801a5a8e621c0e8bf2acd20f74be7d/schemas/schema_differences.md
    title: Differences between the CDE Set schema and the RadElement API
---

# Index code

A "code representing an entry in a standard ontology, e.g., SNOMED or RadLex, which can be applied to a finding or attribute. This is used to standardize the representation of findings and attributes across different systems and to facilitate interoperability between different systems."[^index-code] The fields are `system`, `code`, and an optional `display`.

Index codes may appear on a [finding model](/glossary/finding-model.md), on an [attribute](/glossary/attribute.md), or on an individual [attribute value](/glossary/attribute-value.md). The same type also carries a finding model's `anatomic_locations`, so an [anatomic location](/glossary/anatomic-location.md) reference on a finding model is structurally an index code, usually with `system: "RADLEX"`.[^index-code]

The systems most used in the corpus are [SNOMED CT](/glossary/snomed-ct.md), [RadLex](/glossary/radlex.md), and [Gamuts](/glossary/gamuts.md), with [RadElement](/glossary/radelement.md) appearing on CDE-derived definitions.[^claude-md]

## Synonyms and near-synonyms

- **Coding** in FHIR is the analogous triple of `system`, `code`, and `display`. The [CDE-labeled FHIR Observation](/glossary/cde-labeled-fhir-observation.md) pattern uses it the same way.
- **Standard code** and **ontology code** are informal names for the same thing.
- An [index code](/glossary/index-code.md) references a concept without defining a crosswalk or asserting equivalence across systems.

## Identifier form

None of its own. The code inside follows the referenced system, for example `RID28473` for RadLex or `RDES254` for RadElement.

## Where it is used

[Ontologies used](/semantic-foundation/terminologies/ontologies-used.md) and [Finding model format](/semantic-foundation/finding-models/finding-model-format.md).

## Conflicts

The metadata rewrite in progress requires that an `index_codes` entry "must be an exact match or a clinically substitutable near-equivalent for the full model concept," sending broader, narrower, and complication-specific codes to a separate review artifact instead.[^metadata-rewrite] The corpus on `main` predates that rule. Separately, the CDE Set schema constrains an index code `system` to `RADLEX`, `SNOMEDCT`, or `LOINC` while the RadElement API does not appear to constrain it, and OIFM does not constrain it either.[^cde-set-schema]

[^index-code]: IndexCode model in the oidm-common package
[^claude-md]: findingmodels repository conventions
[^metadata-rewrite]: Canonical structured metadata and enrichment rewrite
[^cde-set-schema]: Differences between the CDE Set schema and the RadElement API
