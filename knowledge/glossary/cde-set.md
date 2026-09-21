---
type: Glossary Term
title: CDE set
description: A published RadElement definition of one finding, grouping the elements that characterize it under an RDES identifier.
tags: [glossary, semantic-foundation, cde]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: cde-repo
    resource: https://github.com/openimagingdata/common_data_elements/blob/35536d8c858bcd33e730a00c919edaef2e310a0b/README.md
    title: common_data_elements repository README and set listing
  - id: schema-diff
    resource: https://github.com/openimagingdata/openimagingdata.org/blob/fb431dfc81801a5a8e621c0e8bf2acd20f74be7d/schemas/schema_differences.md
    title: Differences between the CDE Set schema and the RadElement API
  - id: idr
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md
    title: IHE IDR Phase II extract for the CDE vocabulary
  - id: fhir-sample
    resource: https://github.com/openimagingdata/FHIRSamples/blob/9ae2fa934298e51789e355c9f4e0b71fabf6b5aa/lung_ca_screening_example/example1OIDMradiologist.json
    title: Radiologist finding Observation coded with a CDE set
---

# CDE set

A published definition of one radiology finding on [RadElement](/glossary/radelement.md), grouping the [CDE elements](/glossary/cde-element.md) that characterize it. Roughly 140 sets are listed in the OIDM mirror of the published definitions, from Acute Aortic Syndrome to TI-RADS, each named and carrying an `RDES` identifier.[^cde-repo]

A set carries identity and governance fields as well as its elements: `id`, `name`, `description`, `set_version`, `schema_version`, `current_status`, and `status_history`. The mirror notes that its definitions conform to version 1.0 of the CDE schema rather than the newer version 1.1.[^cde-repo]

In FHIR encodings the set identifier is what labels the parent Observation. The lineage sample codes a radiologist's finding as `RDES195 Pulmonary Nodule` with `system` `https://radelement.org`, and IHE IDR states that "when encoding CDE Sets from radelement.org, it is preferred to use the CDE Set code here."[^fhir-sample][^idr]

## Synonyms and near-synonyms

- **Finding set** is IHE IDR's term for the same grouping pattern.[^idr]
- **[Finding model](/glossary/finding-model.md)** is the OIDM counterpart at the same granularity.
- **[FindingClass](/glossary/finding-class.md)** is the next-generation replacement node type.
- **Element set** is the name used in the JSON schema itself.

## Identifier form

`RDES` followed by digits, for example `RDES195` (Pulmonary Nodule), `RDES267` (Lung-RADS categorization), `RDES11` (MR Rectal Tumor Imaging).

## Where it is used

[CDEs and RadElement](/semantic-foundation/common-data-elements/cdes-and-radelement.md) and [FHIR mapping](/data-structures/fhir-mapping.md).

## Conflicts

The published RelaxNG set schema and the RadElement JSON API disagree in structure and in field presence: `images`, `modality`, `biological_sex`, and `age_range` appear in the schema but not the API, while `url` and `body_parts` appear in the API but not the schema.[^schema-diff] IHE IDR separately records open questions about whether CDE sets may be extended with additional sub-observations and what coding system URI identifies RadElement codes.[^idr]

[^cde-repo]: common_data_elements repository README
[^schema-diff]: Differences between the CDE Set schema and the RadElement API
[^idr]: IHE IDR Phase II extract
[^fhir-sample]: Radiologist finding Observation coded with a CDE set
