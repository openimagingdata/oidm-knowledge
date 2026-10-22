---
type: Glossary Term
title: FMA
description: The Foundational Model of Anatomy, used in OIDM as a cross-reference on anatomic locations and as the basis of the location type classification.
tags: [glossary, semantic-foundation, terminologies, anatomy]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: fma
    resource: https://bioportal.bioontology.org/ontologies/FMA
    title: Foundational Model of Anatomy on BioPortal
  - id: al-code
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/docs/code.markdown
    title: anatomiclocations.org data file description, cross-ontology codes
  - id: al-enums
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/anatomic-locations/src/anatomic_locations/models/enums.py
    title: LocationType enumeration, derived from FMA top-level organization
  - id: molu
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/docs/product-roadmap.md
    title: med-ontology-lookup product roadmap, domain profiles
---

# FMA

The Foundational Model of Anatomy, a reference ontology of human anatomy.[^fma] FMA cross-references appear on [anatomic locations](/glossary/anatomic-location.md), covering 1,643 of the 2,890 curated records. It is the second most common system after [SNOMED CT](/glossary/snomed-ct.md).[^al-code] Its top-level organization supplies the shape of the `location_type` classification in the newer package, which maps material anatomical entity to structure, immaterial anatomical entity to space and region, body part to body_part, organ system to system, and set or collection to group.[^al-enums]

FMA is also one of the five terminologies the `molu` lookup tool spans, and the planned `anatomy` profile names FMA first, with the note that "RadLex imaging anatomy sits next to FMA."[^molu]

## Synonyms and near-synonyms

- **Foundational Model of Anatomy** is the expansion.
- **`FMA`** is the `system` string in an [index code](/glossary/index-code.md) and the source abbreviation in the lookup tooling.
- **[RadLex](/glossary/radlex.md)** is the primary anatomy identifier source in OIDM; FMA is a cross-reference.
- **Uberon** is a different anatomy ontology, named only in the planned `anatomy` profile.

## Identifier form

A numeric identifier, carried in OIDM as a bare number with `system: "FMA"`, for example `265256` for uterine adnexa.[^al-code]

## Where it is used

[Ontologies used](/semantic-foundation/terminologies/ontologies-used.md), [Data model](/semantic-foundation/anatomic-locations/data-model.md), and [med-ontology-lookup](/semantic-foundation/terminologies/med-ontology-lookup.md).

[^fma]: Foundational Model of Anatomy on BioPortal
[^al-code]: anatomiclocations.org data file description
[^al-enums]: LocationType enumeration
[^molu]: med-ontology-lookup product roadmap
