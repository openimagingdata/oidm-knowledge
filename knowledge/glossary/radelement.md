---
type: Glossary Term
title: RadElement
description: The ACR and RSNA registry that publishes common data element sets and elements, and the coding system their identifiers belong to.
tags: [glossary, semantic-foundation, terminologies, cde]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: cde-repo
    resource: https://github.com/openimagingdata/common_data_elements/blob/35536d8c858bcd33e730a00c919edaef2e310a0b/README.md
    title: common_data_elements repository README
  - id: radelement
    resource: https://radelement.org/
    title: RadElement, the ACR/RSNA common data element registry
  - id: idr
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md
    title: IHE IDR Phase II extract for the CDE vocabulary
  - id: index-fixture
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/plans/index-code-target-fixture-integration-2026-06-23.md
    title: Index code target fixture integration, feature/metadata-cleanup branch
---

# RadElement

The ACR and RSNA registry that publishes [CDE sets](/glossary/cde-set.md) and [CDE elements](/glossary/cde-element.md), at `radelement.org`.[^radelement] It is both the place definitions are published and the coding system their identifiers belong to: FHIR encodings in the OIDM lineage use `https://radelement.org` as the coding `system` alongside an `RDES` or `RDE` code.[^cde-repo]

RadElement is downstream of authoring. Informal definitions are drafted in `CDEStaging`, harmonized, and submitted; published sets are mirrored back into the `common_data_elements` repository "as stored and maintained in the ACR/RSNA RadElement web site."[^cde-repo]

## Synonyms and near-synonyms

- **[CDE](/glossary/cde.md)** names the programme and its definitions. RadElement names the registry and the coding system.
- **ACR/RSNA Common Data Elements Project** is the organization name behind it, registered in finding model content under the [organization code](/glossary/oidm-organization-code.md) `CDE`.
- **`RADELEMENT`** is the `system` string used in a finding model [index code](/glossary/index-code.md), as distinct from the URL form used in FHIR.

## Identifier form

`RDES###` for sets and `RDE####` for elements, with dot-suffixed value codes.

## Where it is used

[CDEs and RadElement](/semantic-foundation/common-data-elements/cdes-and-radelement.md) and [Ontologies used](/semantic-foundation/terminologies/ontologies-used.md).

## Conflicts

There is no settled coding-system URI for RadElement codes. IHE IDR asks the question directly, "What is the Coding System identifier for Radelement codes?", and the next-generation work records it as open.[^idr] In practice three forms are in use: `https://radelement.org` in FHIR samples, `RADELEMENT` as an index code system string, and a proposed `RDE2` base in the next-generation notes. Separately, RadElement coverage was found missing from ontology search during metadata enrichment, which made `index_codes` the weakest-scoring field in that pipeline.[^index-fixture]

[^cde-repo]: common_data_elements repository README
[^radelement]: RadElement registry
[^idr]: IHE IDR Phase II extract
[^index-fixture]: Index code target fixture integration
