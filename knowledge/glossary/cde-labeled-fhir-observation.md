---
type: Glossary Term
title: CDE-labeled FHIR Observation
description: The project's founding representation of a finding, a FHIR Observation whose code and component codes are drawn from a published CDE set.
tags: [glossary, data-structures, fhir, cde]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: site-findings
    resource: https://www.openimagingdata.org/findings-cdes-and-observations/
    title: "Findings, CDEs, and Observations, 2023-06-24"
  - id: site-about
    resource: https://www.openimagingdata.org/about/
    title: openimagingdata.org About page
  - id: fhir-sample
    resource: https://github.com/openimagingdata/FHIRSamples/blob/9ae2fa934298e51789e355c9f4e0b71fabf6b5aa/lung_ca_screening_example/example1OIDMradiologist.json
    title: Radiologist finding Observation coded with a CDE set and elements
  - id: lineage-obs
    resource: https://github.com/openimagingdata/OpenImagingDataModel.py/blob/455e5b68d730ea8829083d73064de0ec316d3c4a/openimagingdatamodel/observation/observation.py
    title: Observation model in the OpenImagingDataModel.py reference implementation
  - id: idr
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md
    title: IHE IDR Phase II extract for the CDE vocabulary
---

# CDE-labeled FHIR Observation

The project's founding representation of a radiology finding: a FHIR `Observation` whose `code` identifies a [CDE set](/glossary/cde-set.md) and whose `component` codes identify the [CDE elements](/glossary/cde-element.md) inside it, each component's value giving the chosen value code. The phrase comes from the project's own About page and from the 2023 post that set the direction.[^site-about][^site-findings]

The lung screening sample implements it exactly. A radiologist's finding Observation carries `code` as `RDES195 Pulmonary Nodule` with `system` `https://radelement.org`, references the imaging study through `derivedFrom`, and carries element codes such as `RDE1717` in components with `valueCodeableConcept` giving codes such as `RDE1717.1`.[^fhir-sample] The reference implementation models the same shape in Python, with a discriminated union of codeable-concept, string, integer, and boolean components.[^lineage-obs]

## Synonyms and near-synonyms

- **[Observation](/glossary/observation.md)** is the OIDM object; this is one way to encode it.
- **Structured finding** and **coded observation** are looser terms for the same idea.
- The pattern differs from an OIFM-coded observation only in which vocabulary labels it: `RDES`/`RDE` codes here, `OIFM`/`OIFMA` codes in the current [Exam Finding List](/glossary/exam-finding-list.md).

## Identifier form

None of its own. The identifiers are those of the coding systems used, most often RadElement.

## Where it is used

[FHIR mapping](/data-structures/fhir-mapping.md), [Site articles](/history/site-articles.md), and [Lineage repositories](/history/lineage-repositories.md).

## Conflicts

IHE IDR rejects the component pattern for this purpose. It states that `Observation.component` "is not used," because FHIR limits components to values "not useful on their own" and using it "has the potential to significantly complicate queries," preferring a root Observation with `hasMember` references to associated observations.[^idr] Every OIDM artifact that encodes attributes today, including the documented Exam Finding List mapping and these lineage samples, uses components. Reconciling the two is an open item; see [IHE IDR alignment](/data-structures/ihe-idr-alignment.md).

[^site-findings]: "Findings, CDEs, and Observations", 2023-06-24
[^site-about]: openimagingdata.org About page
[^fhir-sample]: Radiologist finding Observation
[^lineage-obs]: Observation model in OpenImagingDataModel.py
[^idr]: IHE IDR Phase II extract
