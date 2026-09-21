---
type: Reference
title: Ontologies used
description: Every external terminology OIDM touches, who governs it, the shape of its identifiers, the field and structure that carries it, and which lookup tool resolves it.
tags: [semantic-foundation, terminologies, reference, coding]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:30:00Z }
sources:
  - id: radlex
    resource: https://radlex.org/
    title: RadLex, the RSNA radiology lexicon
  - id: radlex-owl
    resource: https://github.com/RSNA/RadLex/blob/d53bd9c666ebaef280f82a4eed02e755a1552d30/RadLex.owl
    title: RadLex OWL file, RSNA RadLex repository, main branch
  - id: snomed
    resource: https://www.snomed.org/
    title: SNOMED International
  - id: fma
    resource: https://bioportal.bioontology.org/ontologies/FMA
    title: Foundational Model of Anatomy on BioPortal
  - id: umls
    resource: https://www.nlm.nih.gov/research/umls/index.html
    title: Unified Medical Language System, US National Library of Medicine
  - id: mesh
    resource: https://www.nlm.nih.gov/mesh/meshhome.html
    title: Medical Subject Headings, US National Library of Medicine
  - id: loinc
    resource: https://loinc.org/
    title: LOINC, Regenstrief Institute
  - id: playbook
    resource: https://loinc.org/committee/radiology/
    title: LOINC/RSNA Radiology Playbook, Regenstrief Institute
  - id: radelement
    resource: https://radelement.org/
    title: RadElement, the ACR/RSNA common data element registry
  - id: gamuts
    resource: https://gamuts.net/
    title: Radiology Gamuts Ontology
  - id: dicom
    resource: https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_D.htm
    title: DICOM Controlled Terminology, DCM code set, NEMA
  - id: fm-corpus
    resource: https://github.com/openimagingdata/findingmodels/tree/4475ac1bcb591f1a0951b2082b59208def173a5d/defs
    title: The 2,382 finding model definitions, findingmodels main branch
  - id: al-data
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/data/body_parts.json
    title: Curated anatomic location dataset, version 1.0.0-rc.1
  - id: al-current
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/notebooks/data/anatomic_locations_noembed.json
    title: Current anatomic location export, findingmodel main branch
  - id: molu-config
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/src/med_ontology_lookup/config.py
    title: Default ontologies and source abbreviation maps, med-ontology-lookup
  - id: molu-roadmap
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/docs/product-roadmap.md
    title: med-ontology-lookup product roadmap, domain profiles and licensing
  - id: current-understanding
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/00-current-understanding.md
    title: Current understanding of the next-generation vocabulary work, ACR-RSNA-CDEs next-gen-2026 branch
  - id: fhir-sample
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/sample_data/example1/chest-ct-fhir.json
    title: Raw FHIR DiagnosticReport input sample, imaging-problem-list main branch
  - id: cde-schema
    resource: https://github.com/openimagingdata/openimagingdata.org/blob/fb431dfc81801a5a8e621c0e8bf2acd20f74be7d/schemas/schema_differences.md
    title: Differences between the CDE set schema and the RadElement API
---

# How to read this

OIDM mints its own identifiers for two things only: [finding models](/glossary/finding-model.md) and their [attributes](/glossary/attribute.md), under the `OIFM` and `OIFMA` schemes. Everything else it points at. This page lists every external terminology that appears somewhere in the OIDM repositories, says who governs it, what its identifiers look like, which field carries it, and whether the [`molu`](/semantic-foundation/terminologies/med-ontology-lookup.md) lookup tool can resolve it.

Counts are from the corpus and datasets at the commits pinned in the sources. Finding model counts are occurrences of an [index code](/glossary/index-code.md) across all 2,382 definitions, not distinct concepts.

| Terminology | Governed by | Identifier form | Where OIDM uses it | Resolved by `molu` |
|---|---|---|---|---|
| [RadLex](/glossary/radlex.md) | RSNA | `RID` plus digits | Anatomic location primary key; index codes on findings, attributes, values | Yes, `RADLEX` |
| [SNOMED CT](/glossary/snomed-ct.md) | SNOMED International | Numeric concept id | Index codes; anatomic location cross-reference; FHIR category and conclusion codes | Yes, `SNOMEDCT`, crosswalk source `SNOMEDCT_US` |
| [FMA](/glossary/fma.md) | Distributed through BioPortal | Bare number | Anatomic location cross-reference; basis of the location type classification | Yes, `FMA` |
| [UMLS](/glossary/umls.md) | US National Library of Medicine | `C` plus seven digits | Crosswalk hub; anatomic location cross-reference | Yes, through UMLS Terminology Services |
| MeSH | US National Library of Medicine | Tree numbers such as `A07.231.114.145` | Anatomic location cross-reference only | No |
| [LOINC](/glossary/loinc.md) | Regenstrief Institute | Digits, hyphen, check digit | Exam type code on the Exam Finding List; a few index codes | Yes, `LOINC`, crosswalk source `LNC` |
| [LOINC/RSNA Radiology Playbook](/glossary/loinc-rsna-radiology-playbook.md) | Regenstrief Institute and RSNA jointly | LOINC codes; legacy `RPID` | Named in exam type goals only | Not as a distinct source |
| [RadElement](/glossary/radelement.md) | ACR and RSNA | `RDES` and `RDE` plus digits | Index codes on CDE-derived finding models; CDE set and element identity | No |
| [Radiology Gamuts Ontology](/glossary/gamuts.md) | Published at gamuts.net | Gamut identifiers; `GMTS` as an OIDM organization code | Index codes; source of the largest block of finding model content | No |
| DICOM Controlled Terminology | NEMA | Numeric `DCM` codes | Series, instance, and SOP identity in raw FHIR input samples | No |
| ICD-10-CM and ICD-10-PCS | National and international maintainers | Alphanumeric | Named in the lookup tool's non-radiology profiles only | Not in the default profile |

# RadLex

The radiology lexicon published by the RSNA, and the terminology OIDM leans on hardest. It supplies the primary key for [anatomic locations](/glossary/anatomic-location.md) in the form of a [RadLex ID](/glossary/radlex-id.md), and it is the second most common index code system in the finding model corpus, with 25,765 occurrences.[^fm-corpus] Presence values across the corpus are coded with it, for example `RID28472` for present and `RID28473` for absent.

The ontology ships as an OWL file in the RSNA repository, which the next-generation vocabulary analysis identifies as the authoritative artifact going forward.[^radlex-owl][^current-understanding] That analysis also records the licence position: RadLex is "actively governed, and freely licensed for commercial and non-commercial use."[^current-understanding] In OIDM data the `system` string is `RADLEX`; in FHIR encodings the system URI is `http://www.radlex.org`.[^fhir-sample] Details of the relationship in both directions, including the open RSNA issue to fold the OIDM anatomic set into RadLex, are in [RadLex integration](/semantic-foundation/anatomic-locations/radlex-integration.md).

# SNOMED CT

The general clinical terminology, and by raw count the most used index code system in the finding model corpus at 27,773 occurrences.[^fm-corpus] It is a secondary coding system rather than a key: findings, attributes, and [attribute values](/glossary/attribute-value.md) carry SNOMED codes alongside RadLex ones, and the FHIR lineage samples use `http://snomed.info/sct` for a report's category and conclusion codes.[^fhir-sample]

On anatomic locations SNOMED is a cross-reference. The curated 2022 dataset carries 1,732 SNOMED codes across 2,890 records; the current export carries a `snomedId` on 1,782 of 2,926 records.[^al-data][^al-current]

The `system` string is inconsistent in the corpus. `SNOMED` appears 27,773 times and `SNOMEDCT` 89 times for the same terminology.[^fm-corpus] The lookup tooling uses `SNOMEDCT` as the BioPortal acronym and `SNOMEDCT_US` as the UMLS source abbreviation.[^molu-config] SNOMED CT is licensed, which is why the tooling treats it as a credentialed backend and keeps "licensed SNOMED/UMLS behavior opt-in and visible."[^molu-roadmap]

# FMA

The Foundational Model of Anatomy, a reference ontology of human anatomy distributed through BioPortal.[^fma] In OIDM it is an anatomic cross-reference, present on 1,643 of the 2,890 records in the curated dataset and 1,649 of the 2,926 in the current export, in both cases the most common entry in the `codes` array.[^al-data][^al-current] Its top-level organization also shapes the location type classification in the current package. Codes are carried as bare numbers with `system: "FMA"`, for example `265256` for uterine adnexa.

# UMLS

The National Library of Medicine's integration of source vocabularies under shared concept unique identifiers.[^umls] OIDM uses it for two jobs. It is the hub the lookup tool crosswalks through, resolving a concept to its CUIs and then translating to other vocabularies, with the default crosswalk targets set to `SNOMEDCT_US`, `FMA`, `RADLEX`, and `LNC`.[^molu-config] And it is an anatomic cross-reference, on 578 of the 2,890 curated records and 580 of the 2,926 current ones.[^al-data][^al-current]

UMLS requires a licence and an API key from UMLS Terminology Services. The lookup roadmap is explicit that a CUI link is evidence rather than proof, and that translation should preserve "mapping direction, scope, provenance, and strength instead of treating every cross-reference as equivalence."[^molu-roadmap]

# MeSH

Medical Subject Headings, also from the National Library of Medicine.[^mesh] MeSH has exactly one role in OIDM: an anatomic location cross-reference, the least common of the four, on 232 of the 2,890 curated records and 233 of the 2,926 current ones, carried as MeSH tree numbers such as `A07.231.114.145` rather than descriptor identifiers.[^al-data][^al-current] No OIDM tool resolves MeSH, and it is not among the terminologies the lookup library queries.

# LOINC and the Radiology Playbook

LOINC is the Regenstrief Institute's system for identifying laboratory and clinical observations, including imaging procedures.[^loinc] In OIDM its main job is [exam type](/glossary/exam-type.md) identification on the [Exam Finding List](/glossary/exam-finding-list.md) exam header, covered in [exam types](/semantic-foundation/exam-types/overview.md).

LOINC also appears, sparingly, as an index code system: 23 occurrences across the whole finding model corpus, on two definitions.[^fm-corpus] Those two are instructive about what LOINC is good for in this context. The Glasgow Coma Scale model codes its attributes with LOINC observation codes such as `9267-6` for eye opening, and its values with LOINC answer-list codes such as `LA6553-7` for no eye opening. The [CDE set](/glossary/cde-set.md) schema likewise admits `LOINC` as one of three permitted index code systems.[^cde-schema]

The [Radiology Playbook](/glossary/loinc-rsna-radiology-playbook.md) is the radiology portion, governed jointly by the Regenstrief Institute and the RSNA, shipping twice yearly, freely licensed, and a separate artifact from RadLex.[^current-understanding][^playbook] Nothing in OIDM consumes it today. Its legacy `RPID` identifiers were folded into LOINC, so new procedure codes take LOINC form.[^molu-roadmap]

# RadElement

The ACR and RSNA registry that publishes [CDE sets](/glossary/cde-set.md) and [CDE elements](/glossary/cde-element.md).[^radelement] It is both a publication venue and a coding system. `RADELEMENT` appears 115 times as an index code system in the finding model corpus, exactly on the CDE-derived definitions.[^fm-corpus] In FHIR encodings the lineage uses `https://radelement.org` as the coding system with an `RDES` or `RDE` code.

RadElement is the one terminology in this table that OIDM both consumes and feeds. No OIDM lookup tool resolves it, and there is no settled coding-system URI for its codes; both points are covered in [CDEs and RadElement](/semantic-foundation/common-data-elements/cdes-and-radelement.md).

# Radiology Gamuts Ontology

An ontology of radiologic differential diagnosis lists, published at gamuts.net.[^gamuts] It plays two roles at once. As a coding system, `GAMUTS` appears 1,935 times in the corpus, essentially once per Gamuts-derived definition.[^fm-corpus] As a contributing organization it holds the [organization code](/glossary/oidm-organization-code.md) `GMTS`, which is the middle segment of 1,933 of the 2,382 finding model identifiers. See [content catalog](/semantic-foundation/finding-models/content-catalog.md) for what that content is and [finding model content direction](/roadmap/finding-model-content-direction.md) for where it is headed.

# DICOM Controlled Terminology

The `DCM` code set from the DICOM standard, with the system URI `http://dicom.nema.org/resources/ontology/DCM`.[^dicom] It appears in OIDM only in the raw FHIR reports used as extraction input, where it labels imaging identity components such as `113607` Series Number and `113609` Instance Number.[^fhir-sample] It is not used anywhere in the OIDM data structures themselves. Two other vocabularies appear in those same input samples and nowhere else: HL7 terminology code systems for report category and identifier type, and UCUM for units.

# ICD

ICD does not appear in any OIDM data structure or definition. It is named once, in the lookup tool's profile design, which places ICD-10-CM and ICD-10-PCS in `clinical` and `billing-us` profiles, notes they are available through BioPortal and UMLS "under the UMLS license," and keeps them deliberately out of the radiology default.[^molu-roadmap] It is listed here so that a reader who expects diagnosis coding to be part of OIDM can see that it is not.

[^radlex]: RadLex, the RSNA radiology lexicon
[^radlex-owl]: RadLex OWL file, RSNA RadLex repository
[^snomed]: SNOMED International
[^fma]: Foundational Model of Anatomy on BioPortal
[^umls]: Unified Medical Language System
[^mesh]: Medical Subject Headings
[^loinc]: LOINC, Regenstrief Institute
[^playbook]: LOINC/RSNA Radiology Playbook
[^radelement]: RadElement registry
[^gamuts]: Radiology Gamuts Ontology
[^dicom]: DICOM Controlled Terminology, DCM code set
[^fm-corpus]: The 2,382 finding model definitions, findingmodels main branch
[^al-data]: Curated anatomic location dataset, version 1.0.0-rc.1
[^al-current]: Current anatomic location export, findingmodel main branch
[^molu-config]: Default ontologies and source abbreviation maps, med-ontology-lookup
[^molu-roadmap]: med-ontology-lookup product roadmap
[^current-understanding]: Current understanding, ACR-RSNA-CDEs next-gen-2026
[^fhir-sample]: Raw FHIR DiagnosticReport input sample
[^cde-schema]: Differences between the CDE set schema and the RadElement API
