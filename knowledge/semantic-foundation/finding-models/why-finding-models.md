---
type: Concept
title: Why finding models
description: Why the finding is OIDM's unit of data, what a finding model definition carries, what it deliberately is not, and how downstream structures consume it.
tags: [semantic-foundation, finding-models, oifm, concept]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
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

A radiology report is prose. Somewhere inside it a radiologist has asserted that a thing is there, or is not there, or is bigger than it was. The Open Imaging Data Model (OIDM) takes that assertion as its atom, and a [finding model](/glossary/finding-model.md) is the reusable definition of one such assertion type.

The reason to define findings rather than reports is stated plainly in the overview note that governs authoring: finding models "turn that unstructured language into structured, machine-accessible observation objects, each linked to a rich knowledge base of clinical context."[^oifm-overview] An agent reads a report, matches each finding it recognizes to a definition, and emits an [Observation](/glossary/observation.md) tagged with the finding type and the values of its [attributes](/glossary/attribute.md).

The second reason is time. "A radiology report is a snapshot, but the findings it describes persist across exams. A pleural effusion seen today may be the same one from last week, now larger."[^oifm-overview] Two reports written a year apart by two radiologists at two institutions can only be compared if both name the same thing the same way. That shared naming is what a finding model supplies, and it is why the [Imaging Problem List](/glossary/imaging-problem-list.md) can organize a patient's history by finding rather than by date.

# What a finding is, and is not

The scope is broader than pathology. The overview note counts as findings: pathologic entities, physiologic observations, devices and hardware, postsurgical states, anatomic variants, and image quality problems. It also refuses to separate description from diagnosis. "Diagnostic terms are first-class findings, do not question whether a diagnosis 'should' be a finding."[^oifm-overview] Both "bilateral perihilar opacities" and "pulmonary edema" are modeled, because radiologists write both.

The test is whether a radiologist would write "there is X" or "no X" as a standalone statement. That test excludes a state of a finding ("stable cardiac silhouette"), a qualified version of one ("large pleural effusion"), normal anatomy, radiographic signs and interpretation techniques, exam metadata, clinical history, and recommendations. The guiding principle is that "a finding is a noun phrase; everything else is an attribute."[^oifm-overview] The full treatment, with its worked examples of too broad, too narrow, and right level, is in [the overview extract](/references/oifm-overview-extract.md).

Negative assertions are inside the scope, not outside it. When a report says "no fracture," that is an active observation recorded as [presence](/glossary/presence.md) absent, which means the finding was looked for and not found. Models therefore have to exist at the breadth where radiologists make those sweeping statements, which is why "chest wall fracture" and "upper abdominal abnormality" are legitimate models.

# What the definition carries

A finding model is a knowledge base entry, not a label. Each definition carries a canonical name, a description written for a radiologist audience, synonyms covering the ways the same observation gets expressed, [tags](/glossary/tag.md) for browsing, [index codes](/glossary/index-code.md) linking to SNOMED CT, RadLex, and the Radiology Gamuts Ontology, optional [anatomic locations](/glossary/anatomic-location.md), [contributors](/glossary/contributor.md), and the attribute list.[^oifm-overview][^fm-model]

Attributes are the characterization axes. Two are near-universal and come first by convention: presence, with the values absent, present, indeterminate, and unknown, then [change from prior](/glossary/change-from-prior.md). After those come the domain-specific axes, size, severity, density, morphology, enhancement pattern, and whatever else the finding needs. Each choice value gets its own code, so a stored Observation can cite not just the finding and the attribute but the specific value chosen. Every identifier in that chain is machine-generated and never written by hand. The field-level specification is in [the format document](/semantic-foundation/finding-models/finding-model-format.md).

Quality in these definitions is load-bearing rather than cosmetic. "A sloppy synonym maps the wrong concept to an observation; a nonsensical attribute propagates meaningless data; a poorly scoped model conflates distinct clinical entities. Errors here don't just look bad, they cause incorrect downstream reasoning about patient care."[^oifm-overview]

# What a finding model is not

It is not a report template. Templates were the earlier approach to structured reporting, and a finding model does not prescribe what a report contains or in what order. It defines one finding and leaves composition to whatever produces the report.

It is not a common data element, at least not yet. The January 2026 status deck frames finding models as "the CDE workbench": rapid, language-model-assisted content creation acting as "a proving ground for formal common data elements," carrying "rich definitions with embedded relationships and semantic tags that can graduate to standards."[^deck] The relationship runs from finding model toward [common data element](/glossary/cde.md), not the other way, and it is worked through in [finding models and CDEs](/semantic-foundation/finding-models/finding-models-and-cdes.md).

It is also not an instance. The definition says what a pleural effusion is and how one is characterized. It says nothing about any particular patient. That separation is the whole point of the layering described in [architecture](/overview/architecture.md).

# How the definitions get used

Downstream structures reference finding models only by identifier. An [Exam Finding List](/glossary/exam-finding-list.md) entry carries a `findingCode` holding the model's OIFM identifier, an optional anatomic location, and an `attributes` array in which each element pairs an OIFMA attribute identifier with a value code drawn from that attribute's permitted values.[^efl-example] Nothing in the Exam Finding List repeats the definition; a reader that wants to know what `OIFM_GMTS_016552` means resolves it against the content repository.

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

The same identifiers flow upward into the Imaging Problem List, which groups a patient's observations by finding code across exams. The details of both structures are in [the Exam Finding List document](/data-structures/exam-finding-list.md).

An older statement of the same idea, from the 2023 site post that predates the finding model format, describes a radiology finding as a FHIR Observation "semantically labeled with ACR/RSNA Common Data Element identifiers," with the set identifier naming the finding type and element identifiers naming the attributes.[^site-post] The shape survived; what changed is that OIDM now mints its own identifiers for the definitions that no common data element covers.

[^oifm-overview]: "Finding Models: Overview", findingmodels repository
[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
[^site-post]: "Findings, CDEs, and Observations", openimagingdata.org, 2023-06-24
[^fm-model]: FindingModelFull definition, findingmodel repository, main branch
[^efl-example]: imaging-problem-list README, main branch
