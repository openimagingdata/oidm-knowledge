---
type: Concept
title: Why finding models
description: Why OIDM defines findings, what a finding model contains, and how observations use it.
tags: [semantic-foundation, finding-models, oifm, concept]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:34:50Z }
sources:
  - id: oifm-overview
    resource: https://github.com/openimagingdata/findingmodels/blob/2267d5d0b430ec7117a6da91efe6069da38c0056/prompts/overview.md
    title: "Finding Models: Overview, findingmodels repository"
    last_modified: 2026-04-18
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: "Open Imaging Data Model 2026 Status Update: Realizing Object-Oriented Imaging Results, January 2026"
  - id: site-post
    resource: https://www.openimagingdata.org/findings-cdes-and-observations/
    title: "Findings, CDEs, and Observations, openimagingdata.org, 2023-06-24"
  - id: fm-model
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/finding_model.py
    title: FindingModelFull definition, findingmodel repository, main branch
  - id: efl-example
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/README.md
    title: imaging-problem-list README, main branch, the Exam Finding List specification
---

# The finding is the unit

A radiology report records assertions about findings, including their presence, absence, and change. The Open Imaging Data Model (OIDM) represents each finding type with a reusable [finding model](/glossary/finding-model.md).

Finding models "turn that unstructured language into structured, machine-accessible observation objects, each linked to a rich knowledge base of clinical context."[^oifm-overview] An agent matches report findings to definitions and emits an [Observation](/glossary/observation.md) with a finding type and [attribute](/glossary/attribute.md) values.

"A radiology report is a snapshot, but the findings it describes persist across exams. A pleural effusion seen today may be the same one from last week, now larger."[^oifm-overview] Shared definitions let the [Imaging Problem List](/glossary/imaging-problem-list.md) group observations by finding across exams and institutions.

# What a finding is, and is not

Findings include pathologic entities, physiologic observations, devices and hardware, postsurgical states, anatomic variants, and image quality problems. The authoring overview includes diagnoses: "Diagnostic terms are first-class findings, do not question whether a diagnosis 'should' be a finding."[^oifm-overview] Both "bilateral perihilar opacities" and "pulmonary edema" qualify.

The test is whether a radiologist would write "there is X" or "no X" as a standalone statement. It excludes finding states such as "stable cardiac silhouette", qualified findings such as "large pleural effusion", normal anatomy, radiographic signs, interpretation techniques, exam metadata, clinical history, and recommendations. The principle is that "a finding is a noun phrase; everything else is an attribute."[^oifm-overview] The [overview extract](/references/oifm-overview-extract.md) has examples of appropriate scope.

"No fracture" records an observation with [presence](/glossary/presence.md) absent. The finding was looked for and not found. Broad models such as "chest wall fracture" and "upper abdominal abnormality" support these negative assertions.

# What the definition carries

A definition contains a canonical name, a description for radiologists, synonyms, [tags](/glossary/tag.md), [index codes](/glossary/index-code.md), optional [anatomic locations](/glossary/anatomic-location.md), [contributors](/glossary/contributor.md), and attributes. Tags support browsing; index codes link to SNOMED CT, RadLex, and the Radiology Gamuts Ontology.[^oifm-overview][^fm-model]

Attributes characterize a finding. By convention, most models start with presence, whose values are absent, present, indeterminate, and unknown, then [change from prior](/glossary/change-from-prior.md). Finding-specific attributes follow, such as size, severity, density, morphology, and enhancement pattern. Each choice value has a code so an Observation can identify the finding, attribute, and selected value. Tools generate all identifiers. Authors do not assign them by hand. See the [format document](/semantic-foundation/finding-models/finding-model-format.md).

Definition errors affect downstream interpretation: "A sloppy synonym maps the wrong concept to an observation; a nonsensical attribute propagates meaningless data; a poorly scoped model conflates distinct clinical entities. Errors here don't just look bad, they cause incorrect downstream reasoning about patient care."[^oifm-overview]

# What a finding model is not

A finding model defines one finding. Earlier structured-reporting approaches used templates to prescribe report content and order; finding models leave report composition to the application.

It is not a common data element, at least not yet. The January 2026 deck calls them "the CDE workbench" and "a proving ground for formal common data elements".[^deck] The relationship runs from finding model toward [common data element](/glossary/cde.md), not the other way, and it is worked through in [finding models and CDEs](/semantic-foundation/finding-models/finding-models-and-cdes.md).

A definition describes a finding type, such as pleural effusion. Patient-specific observations reference that definition, as described in the [architecture](/overview/architecture.md).

# How the definitions get used

An [Exam Finding List](/glossary/exam-finding-list.md) entry references the model by its OIFM identifier in `findingCode`. Downstream structures reference finding models only by identifier. It adds an optional anatomic location and an `attributes` array pairing OIFMA attribute identifiers with permitted value codes.[^efl-example] Nothing in the Exam Finding List repeats the definition; a reader that wants to know what `OIFM_GMTS_016552` means resolves it against the content repository.

```json
{
  "findingCode": "OIFM_GMTS_016552",
  "findingDescription": "urinary tract calculus",
  "attributes": [
    {
      "attributeCode": "OIFMA_GMTS_707209",
      "attributeValueCode": "OIFMA_GMTS_707209.1",
      "attributeValueDescription": "present"
    }
  ]
}
```

The Imaging Problem List groups a patient's observations across exams using the same identifiers. See the [Exam Finding List document](/data-structures/exam-finding-list.md).

The 2023 site post described a FHIR Observation "semantically labeled with ACR/RSNA Common Data Element identifiers", with a set identifier for the finding type and element identifiers for its attributes.[^site-post] OIDM now also mints its own identifiers for definitions that no common data element covers.

[^oifm-overview]: "Finding Models: Overview", findingmodels repository
[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
[^site-post]: "Findings, CDEs, and Observations", openimagingdata.org, 2023-06-24
[^fm-model]: FindingModelFull definition, findingmodel repository, main branch
[^efl-example]: imaging-problem-list README, main branch
