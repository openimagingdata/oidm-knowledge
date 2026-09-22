---
type: Glossary Term
title: SNOMED CT
description: The clinical terminology used in OIDM as a secondary coding system on findings, attribute values, and anatomic locations.
tags: [glossary, semantic-foundation, terminologies]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: snomed
    resource: https://www.snomed.org/
    title: SNOMED International
  - id: molu
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/README.md
    title: med-ontology-lookup README
  - id: claude-md
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/CLAUDE.md
    title: findingmodels repository conventions, common ontologies
  - id: al-code
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/docs/code.markdown
    title: anatomiclocations.org data file description, cross-ontology codes
  - id: fhir-sample
    resource: https://github.com/openimagingdata/FHIRSamples/blob/9ae2fa934298e51789e355c9f4e0b71fabf6b5aa/lung_ca_screening_example/example1OIDMreport.json
    title: Lung screening DiagnosticReport with SNOMED category and conclusion codes
---

# SNOMED CT

The Systematized Nomenclature of Medicine Clinical Terms, the general clinical terminology.[^snomed] OIDM uses it for secondary codes, not primary keys. Alongside [RadLex](/glossary/radlex.md) and [Gamuts](/glossary/gamuts.md), it supplies [index codes](/glossary/index-code.md) on [finding models](/glossary/finding-model.md), [attributes](/glossary/attribute.md), and [attribute values](/glossary/attribute-value.md).[^claude-md] SNOMED CT cross-references appear on 1,732 of 2,890 curated [anatomic locations](/glossary/anatomic-location.md).[^al-code] FHIR lineage samples use it for report category and conclusion codes.[^fhir-sample]

Typical use on a value is the qualifier hierarchy, for example `52101004` for Present and `2667000` for Absent, paired with the equivalent RadLex codes on the same value.

## Synonyms and near-synonyms

- **SNOMED** and **SNOMED-CT** are the same terminology; source documents use all three spellings.
- **`SNOMED`** is the `system` string in a finding model index code, while **`SNOMEDCT`** and **`SNOMEDCT_US`** are the BioPortal and UMLS source abbreviations used by the lookup tooling.[^molu]
- **`snomedId`** and **`snomedDisplay`** are field names in the raw anatomic location export.

## Identifier form

A numeric concept identifier, for example `23043003` for uterine adnexa.

## Where it is used

[Ontologies used](/semantic-foundation/terminologies/ontologies-used.md), [Data model](/semantic-foundation/anatomic-locations/data-model.md), and [med-ontology-lookup](/semantic-foundation/terminologies/med-ontology-lookup.md).

## Conflicts

SNOMED CT requires a licence. The lookup tooling keeps licensed behavior opt-in and visible rather than implicit.[^molu] The curated anatomic set also records "complete SNOMED identification" as unfinished roadmap work, so SNOMED coverage of anatomic locations is partial by design.

[^snomed]: SNOMED International
[^molu]: med-ontology-lookup README
[^claude-md]: findingmodels repository conventions
[^al-code]: anatomiclocations.org data file description
[^fhir-sample]: Lung screening DiagnosticReport
