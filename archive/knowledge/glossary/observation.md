---
type: Glossary Term
title: Observation
description: The atomic unit of OIDM data, one finding seen or excluded on one exam, with its anatomic location and attribute values.
tags: [glossary, data-structures]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026, Observation object
  - id: ipl-claude
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/CLAUDE.md
    title: imaging-problem-list domain model, dev branch
  - id: lineage-obs
    resource: https://github.com/openimagingdata/OpenImagingDataModel.py/blob/455e5b68d730ea8829083d73064de0ec316d3c4a/openimagingdatamodel/observation/observation.py
    title: Observation model in the OpenImagingDataModel.py reference implementation
  - id: idr
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md
    title: IHE IDR Phase II extract for the CDE vocabulary
  - id: issue1
    resource: https://github.com/openimagingdata/imaging-problem-list/issues/1
    title: imaging-problem-list issue 1, Create System of Data Models
---

# Observation

The atomic unit of OIDM data: one finding, seen or explicitly excluded, on one exam. The 2026 deck describes it as "what + where + attributes," a finding tag plus an [anatomic location](/glossary/anatomic-location.md) plus lesion characteristics, carrying presence indicators, change from prior, and measurements in "a universal structure across systems."[^deck]

In the current [Exam Finding List](/glossary/exam-finding-list.md) format an observation is one entry in the `findings` array, with an `observationId`, a `findingCode` and description, an `attributes` array, an optional `anatomicLocation`, and an optional verbatim `reportText`. Repeat instances are separate observations: "the same finding type may appear multiple times, for example multiple kidney stones, and each gets its own entry with a unique `observationId`."[^ipl-claude]

The 2024 reference implementation's `Observation` class states "the Observation class is the model for FHIR Observation objects," with `code`, `status`, `subject`, `bodySite`, `derivedFrom`, and a discriminated union of components.[^lineage-obs]

## Synonyms and near-synonyms

- **Finding instance** and **extracted finding** name the same thing at different stages; issue 1 proposes an Extracted Observation subtype for the pipeline case.[^issue1]
- **[FHIR Observation](/glossary/cde-labeled-fhir-observation.md)** is the interchange encoding, not the OIDM object.
- **[Finding model](/glossary/finding-model.md)** is the definition; an observation is an occurrence of it.
- IHE IDR uses "observation" more narrowly, for "a feature or characteristic that is visible in an image," closer to a single attribute value than to this whole object.[^idr]

## Identifier form

No cross-system identifier. `observationId` is unique within its Exam Finding List.

## Where it is used

[Hierarchy](/data-structures/hierarchy.md), [Observation](/data-structures/observation.md), and [Exam Finding List](/data-structures/exam-finding-list.md).

## Conflicts

There is no published Observation schema. Issue 1 calls for Pydantic models for Observation, Exam Finding List, and Imaging Problem List with JSON Schema export, and the schema URL referenced in sample files does not yet resolve.[^issue1] The name also collides with IHE IDR's narrower sense, which the next-generation notes flag explicitly as a vocabulary collision.[^idr]

[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
[^ipl-claude]: imaging-problem-list domain model, dev branch
[^lineage-obs]: Observation model in OpenImagingDataModel.py
[^idr]: IHE IDR Phase II extract
[^issue1]: imaging-problem-list issue 1
