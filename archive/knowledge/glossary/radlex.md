---
type: Glossary Term
title: RadLex
description: The RSNA radiology lexicon, the ontology that supplies identifiers for anatomic locations and many finding and attribute codes.
tags: [glossary, semantic-foundation, terminologies]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: radlex
    resource: https://radlex.org/
    title: RadLex, the RSNA radiology lexicon
  - id: molu
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/README.md
    title: med-ontology-lookup README
  - id: baseline
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/05-radlex-baseline.md
    title: RadLex baseline verification, next-gen-2026 branch
  - id: al-site
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/docs/index.markdown
    title: anatomiclocations.org site homepage, why a curated subset
  - id: radlex-issue
    resource: https://github.com/RSNA/RadLex/issues/3
    title: RadLex issue 3, Add Anatomic Locations
---

# RadLex

The radiology lexicon published by the Radiological Society of North America.[^radlex] RadLex is the primary identifier source for OIDM [anatomic locations](/glossary/anatomic-location.md) and a common system for finding and [attribute value](/glossary/attribute-value.md) [index codes](/glossary/index-code.md), for example `RID28472` for present and `RID28473` for absent.

The ontology ships as an OWL file. In the copy read for this knowledgebase it declares roughly 93,900 OWL classes and 46,899 distinct [RID](/glossary/radlex-id.md) identifiers. Anatomy is expressed through OWL restrictions on `Has_Part` and `Part_Of` rather than as a separate containment axis. Provenance is carried on a `Source` annotation holding free text such as "Playbook," "LOINC," or "LI-RADS 2020," and obsolescence through `Replaced_by`.[^baseline]

OIDM's relationship to RadLex runs in both directions. The curated anatomic set exists because RadLex and SNOMED CT alone were judged unsuitable for interoperability, lacking desired terms, carrying degenerate ones, and having limited anatomic organization.[^al-site] In the other direction, RSNA issue 3, "Add Anatomic Locations," is an open upstream tracking issue whose exit criterion is "100% coverage of the Anatomic Locations terminology in RadLex."[^radlex-issue]

## Synonyms and near-synonyms

- **Radiology lexicon** is the expansion.
- **`RADLEX`** is the `system` string in an index code; `http://radlex.org` is the URI form used in FHIR.
- **[RadLex RID](/glossary/radlex-id.md)** is an identifier in RadLex, not the ontology.
- **RadLex Playbook** is a different artifact; see [LOINC/RSNA Radiology Playbook](/glossary/loinc-rsna-radiology-playbook.md).

## Identifier form

`RID` followed by digits. See [RadLex RID](/glossary/radlex-id.md).

## Where it is used

[Ontologies used](/semantic-foundation/terminologies/ontologies-used.md), [RadLex integration](/semantic-foundation/anatomic-locations/radlex-integration.md), and [Anatomic locations and RadLex](/roadmap/anatomic-locations-and-radlex.md). RadLex is one of the five terminologies the `molu` lookup tool spans.[^molu]

[^radlex]: RadLex, the RSNA radiology lexicon
[^molu]: med-ontology-lookup README
[^baseline]: RadLex baseline verification
[^al-site]: anatomiclocations.org site homepage
[^radlex-issue]: RadLex issue 3
