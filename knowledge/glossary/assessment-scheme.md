---
type: Glossary Term
title: AssessmentScheme
description: A definition of a standardized assessment system whose dimensions are ordinary data elements, distinct from the findings it assesses.
tags: [glossary, semantic-foundation, cde, next-generation]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: cde-context
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/CONTEXT.md
    title: CDE vocabulary, next-generation working glossary
  - id: overview
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/oifm-overview.md
    title: "Finding Models: Overview, scoring systems as findings"
  - id: idr
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md
    title: IHE IDR Phase II extract for the CDE vocabulary
  - id: fhir-sample
    resource: https://github.com/openimagingdata/FHIRSamples/blob/9ae2fa934298e51789e355c9f4e0b71fabf6b5aa/lung_ca_screening_example/example1OIDMradiologistLungRADS.json
    title: Lung-RADS assessment Observation derived from a finding Observation
---

# AssessmentScheme

"A distinct definition of an assessment system whose descriptive dimensions are ordinary DataElements linked to the scheme, analogous to a FindingClass with its descriptors. The scheme is distinct from any one dimension or that dimension's permissible values."[^cde-context] Lung-RADS, TI-RADS, BI-RADS, and LI-RADS are the systems this node type covers.

The scheme is distinct from its category values and the findings it assesses. OIDM's authoring guidance states: "scoring systems and structured assessments are valid findings, but should be modeled separately from the observations they assess," because "different radiologists might describe the same nodule but assign different risk categories, and systems need to reason about both independently."[^overview]

The lineage FHIR samples implement this separation. A Lung-RADS Observation carries the category as a component and is `derivedFrom` both the imaging study and the radiologist's pulmonary nodule Observation.[^fhir-sample] IHE IDR calls the pattern a Summary or Derived Observation, with the value in the parent and the children referenced by `derivedFrom`.[^idr]

## Synonyms and near-synonyms

- **Scoring system**, **structured assessment**, and **the -RADS systems** are informal names for the same class of artifact.
- **Assessment category** is the value a scheme produces, not the scheme.
- In OIFM there is no separate type: a scheme is modelled as an ordinary [finding model](/glossary/finding-model.md), and a published example is the CDE set `RDES267` for Lung-RADS categorization.

## Identifier form

None of its own. Published assessment content carries ordinary `RDES` or `OIFM` identifiers.

## Where it is used

[Next-generation vocabulary](/semantic-foundation/common-data-elements/next-generation-vocabulary.md), [FHIR mapping](/data-structures/fhir-mapping.md), and [Roadmap 2026](/roadmap/roadmap-2026.md), which names *-RADS support as a stated ACR priority.

[^cde-context]: CDE vocabulary, next-generation working glossary
[^overview]: "Finding Models: Overview"
[^idr]: IHE IDR Phase II extract
[^fhir-sample]: Lung-RADS assessment Observation
