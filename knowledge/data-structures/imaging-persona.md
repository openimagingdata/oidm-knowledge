---
type: Concept
title: Imaging Persona
description: "The fourth level of the hierarchy, a stated goal with no artifact: the clinical context around a patient's Imaging Problem List, and the life-cycle uses the 2026 deck gives for it."
tags: [data-structures, imaging-persona, roadmap, concept-only]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
sources:
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: "Open Imaging Data Model 2026 Status Update: Realizing Object-Oriented Imaging Results, January 2026"
  - id: ipl-mvp-fhir
    resource: https://github.com/openimagingdata/IPL-MVP-ExtractionAndLabeling/blob/5ea6720e114d3e2cdded5c39ecc5a2eb108e97fb/FHIR_Example_Structure
    title: FHIR_Example_Structure, a longitudinal FHIR persistence design note on the IPL-MVP-ExtractionAndLabeling Persistent_FHIR_Resources branch
  - id: site-structure
    resource: https://www.openimagingdata.org/data-model-structure-and-function/
    title: '"Data Model: Structure and Function", openimagingdata.org, 2024-01-25'
---

# Status first

The [Imaging Persona](/glossary/imaging-persona.md) is a goal. It is named in the January 2026 status deck as the fourth level of [the data structure hierarchy](/data-structures/hierarchy.md) and appears nowhere else in the project. No schema, no sample, no code. Everything below is what the deck states.[^deck]

# What the deck describes

The deck's slide is headed "Imaging Persona (big picture)" and gives four categories of context that would surround a patient's [Imaging Problem List](/data-structures/imaging-problem-list.md).[^deck]

| Category | Contents named |
|---|---|
| Clinical context | orders, indications |
| Medical baseline | problem list, allergies, laboratory results |
| Specialized history | oncology, treatments |
| Surgical history | operative records, pathology, implants |

None of that is imaging results. The Imaging Problem List is the structure the project builds; the persona is the argument that a problem list on its own does not answer the questions radiology actually gets asked. Three of the four categories come from the electronic medical record rather than from radiology, which makes the persona as much an integration claim as a data structure.

# Why: the imaging life cycle

The deck argues for it through a separate slide on what the Imaging Problem List enables at each stage of the imaging life cycle. The uses named there are the ones that need context the problem list does not carry.[^deck]

| Stage | Uses the deck names |
|---|---|
| Planning | magnetic resonance safety, mobility, prior authorization |
| Intra-exam | rules-based protocoling |
| Interpretation | findings-oriented views in the picture archiving system, real-time quality control |
| Post-interpretation | passive screening, research, outcomes |

Read against the four categories, the dependency is concrete. Magnetic resonance safety screening is a question about implants, which is surgical history. Prior authorization is a question about the order and the indication. Rules-based protocoling needs both the prior imaging findings and the clinical question. Passive screening needs the medical baseline to know whether a finding matters for this patient. A problem list alone answers none of these; a problem list plus that context answers all four.

The 2024 site post on the data model made a related claim earlier and in wider terms, listing observations, current report text, imaging studies, patient, order, prior studies, tracked observations, and electronic health record data as the elements the model organizes.[^site-structure] The persona is that list narrowed to the patient-context half and given a name.

# A related unimplemented idea

One adjacent design note exists in the repositories, on an unmerged branch of the early extraction prototype. `FHIR_Example_Structure` sketches longitudinal persistence of findings: each finding becomes "a **tracked entity** with a FHIR ID that persists," so a second report describing the same liver lesion links to the existing resource and adds a new dated value rather than creating a second finding.[^ipl-mvp-fhir] The note's worked timeline shows one lesion at 1.6 cm, 2.1 cm, and 2.8 cm across three reports, and its query examples are "show me the timeline for liver lesion" and "how has the renal calculus changed?".

It is a different idea from the persona. It addresses identity of a finding over time, which the current [Imaging Problem List](/data-structures/imaging-problem-list.md) approximates by grouping on finding code and location rather than by tracking a lesion. It is recorded here because it is the only written treatment anywhere in the repositories of persisting a patient's imaging story as durable resources, which is the substrate a persona would need. It sits on a single-commit branch of a superseded prototype and was never merged; see [IPL-MVP extraction](/applications/ipl-mvp-extraction.md).

# What would have to be decided

Nothing about the persona has been specified, so this section states only what the deck leaves open rather than proposing answers. The deck does not say whether the persona is a stored structure or a query-time assembly, which systems own each of the four context categories, how it would be encoded, or who would maintain it. Those questions are carried in [open questions](/roadmap/open-questions.md) and the direction in [the 2026 roadmap](/roadmap/roadmap-2026.md).

[^deck]: "Open Imaging Data Model 2026 Status Update", January 2026
[^ipl-mvp-fhir]: FHIR_Example_Structure, IPL-MVP-ExtractionAndLabeling, Persistent_FHIR_Resources branch
[^site-structure]: "Data Model: Structure and Function", openimagingdata.org, 2024-01-25
