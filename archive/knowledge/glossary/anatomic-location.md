---
type: Glossary Term
title: Anatomic location
description: A curated anatomic concept identified by a RadLex identifier, placed in containment and part-of hierarchies with laterality variants and cross-ontology codes.
tags: [glossary, semantic-foundation, anatomy]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: al-site
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/docs/index.markdown
    title: anatomiclocations.org site homepage, rationale and approach
  - id: al-code
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/docs/code.markdown
    title: anatomiclocations.org data file description
  - id: al-package
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/anatomic-locations/src/anatomic_locations/models/location.py
    title: AnatomicLocation model in the anatomic-locations package
  - id: cde-context
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/CONTEXT.md
    title: CDE vocabulary, next-generation working glossary
---

# Anatomic location

A discrete anatomic concept, curated for imaging use and identified by a [RadLex identifier](/glossary/radlex-id.md). The project site states that "standard identifiers for discrete anatomic locations would enable numerous levels of interoperability if applied broadly," but existing ontologies are unsuited to that job because they lack needed terms, carry too many degenerate ones, and have limited anatomic organization. The project describes its approach: "we are curating a subset of anatomic concepts from existing ontologies and shaping them into a usable collection of anatomic identifiers for informatics interoperability."[^al-site]

Two implementations exist. The original curated set holds 2,890 nodes with `radlexId`, `description`, `containedById`, `partOfId`, a `leftId`/`rightId`/`unsidedId` triad, `sexSpecific`, `synonyms`, and `codes` into [SNOMED CT](/glossary/snomed-ct.md), [FMA](/glossary/fma.md), [UMLS](/glossary/umls.md), and MeSH.[^al-code] The newer `anatomic-locations` package normalizes the same material into a richer model with `region`, `location_type`, `body_system`, `structure_type`, a `laterality` enum, precomputed containment and part-of paths, and `left_variant`/`right_variant`/`generic_variant` references.[^al-package]

## Synonyms and near-synonyms

- **Body part** is the older term, surviving in `body_parts.json` and in the two wrapper libraries.
- **ACR Common anatomic location** refers to the same set through its `acrCommonId` cross-reference.
- **bodySite** is the FHIR field that carries one.
- **[Body region](/glossary/body-region.md)** is coarser: a region is a grouping, a location is a structure.
- **[Anatomic scope](/glossary/anatomic-scope.md)** is a constraint on a definition, not a place.

## Identifier form

A [RadLex RID](/glossary/radlex-id.md). Sided variants in the original set use composite identifiers matching `^RID\d+(_RID\d+)*$`, for example `RID294_RID5824` for the left uterine adnexa.[^al-code]

## Where it is used

[Why anatomic locations](/semantic-foundation/anatomic-locations/why-anatomic-locations.md), [Data model](/semantic-foundation/anatomic-locations/data-model.md), and [Anatomic location assignment rules](/data-structures/anatomic-location-assignment-rules.md).

## Conflicts

The two lineages differ in count, field names, and laterality representation and are not synchronized. See [Lineage and current implementation](/semantic-foundation/anatomic-locations/lineage-and-current-implementation.md). The next-generation CDE vocabulary defines AnatomicLocation as "an anatomical reference identified by its RadLex identity, with temporary sided-variant exceptions governed by the anatomy track," treating sided variants as provisional, whereas the OIDM sets make them first-class nodes.[^cde-context]

[^al-site]: anatomiclocations.org site homepage
[^al-code]: anatomiclocations.org data file description
[^al-package]: AnatomicLocation model in the anatomic-locations package
[^cde-context]: CDE vocabulary, next-generation working glossary
