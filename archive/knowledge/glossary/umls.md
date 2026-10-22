---
type: Glossary Term
title: UMLS
description: The Unified Medical Language System, used in OIDM as the hub for translating identifiers between terminologies and as a cross-reference on anatomic locations.
tags: [glossary, semantic-foundation, terminologies]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: umls
    resource: https://www.nlm.nih.gov/research/umls/index.html
    title: Unified Medical Language System, US National Library of Medicine
  - id: molu
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/README.md
    title: med-ontology-lookup README
  - id: roadmap
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/docs/product-roadmap.md
    title: med-ontology-lookup product roadmap, UMLS as hub
  - id: al-code
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/docs/code.markdown
    title: anatomiclocations.org data file description, cross-ontology codes
---

# UMLS

The Unified Medical Language System, the US National Library of Medicine's integration of many source vocabularies under shared concept identifiers.[^umls]

The `molu` lookup tool resolves a concept to its UMLS concept unique identifiers and then translates to codes in other vocabularies. The design makes "UMLS as the CUI hub" part of the default radiology profile, alongside [RadLex](/glossary/radlex.md), [LOINC](/glossary/loinc.md), [SNOMED CT](/glossary/snomed-ct.md), and [FMA](/glossary/fma.md).[^roadmap][^molu] The roadmap is explicit that a crosswalk is not an equivalence: translation should preserve "mapping direction, scope, provenance, and strength instead of treating every cross-reference as equivalence."[^roadmap]

UMLS also supplies cross-reference codes on [anatomic locations](/glossary/anatomic-location.md), present on 578 of the 2,890 records in the curated set.[^al-code]

## Synonyms and near-synonyms

- **CUI**, a concept unique identifier, is one UMLS identifier, not the system.
- **UTS**, the UMLS Terminology Services, is the REST API the lookup tool calls.
- **Metathesaurus** is the UMLS component that holds the source vocabularies.
- **[Index code](/glossary/index-code.md)** with `system: "UMLS"` is how a UMLS reference appears in OIDM data.

## Identifier form

`C` followed by seven digits, for example `C0001575`.

## Where it is used

[Ontologies used](/semantic-foundation/terminologies/ontologies-used.md), [med-ontology-lookup](/semantic-foundation/terminologies/med-ontology-lookup.md), and [Data model](/semantic-foundation/anatomic-locations/data-model.md).

## Conflicts

UMLS requires a licence and API key. The lookup tool's typed failure model exists partly for this reason, separating absence of a result from authentication, authorization, and licensing failures, so the latter stay visible rather than silently falling back.[^molu] A tracked issue also records that co-occurring CUI ambiguity is currently lost rather than preserved.

[^umls]: Unified Medical Language System
[^molu]: med-ontology-lookup README
[^roadmap]: med-ontology-lookup product roadmap
[^al-code]: anatomiclocations.org data file description
