---
type: Concept
title: Imaging Persona
description: "The fourth level of the hierarchy, a stated goal with no artifact: the clinical context around a patient's Imaging Problem List, and the life-cycle uses the 2026 deck gives for it."
tags: [data-structures, imaging-persona, roadmap, concept-only]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:34:50Z }
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

The [Imaging Persona](/glossary/imaging-persona.md) is a goal named only in the January 2026 status deck as the fourth level of [the data structure hierarchy](/data-structures/hierarchy.md).[^deck] No schema, no sample, no code. Everything below is what the deck states.[^deck]

# What the deck describes

The slide "Imaging Persona (big picture)" names four context categories for a patient's [Imaging Problem List](/data-structures/imaging-problem-list.md).[^deck]

| Category | Contents named |
|---|---|
| Clinical context | orders, indications |
| Medical baseline | problem list, allergies, laboratory results |
| Specialized history | oncology, treatments |
| Surgical history | operative records, pathology, implants |

These categories add context beyond imaging results. Three of the four categories come from the electronic medical record rather than from radiology, which makes the persona as much an integration claim as a data structure.

# Why: the imaging life cycle

A separate slide names uses of the Imaging Problem List across the imaging life cycle that need additional context.[^deck]

| Stage | Uses the deck names |
|---|---|
| Planning | magnetic resonance safety, mobility, prior authorization |
| Intra-exam | rules-based protocoling |
| Interpretation | findings-oriented views in the picture archiving system, real-time quality control |
| Post-interpretation | passive screening, research, outcomes |

Read against the four categories, the dependency is concrete. Magnetic resonance safety screening is a question about implants, which is surgical history. Prior authorization needs the order and indication, which is clinical context. Rules-based protocoling needs prior findings and the clinical question. Passive screening needs the medical baseline to assess a finding's relevance to the patient. A problem list alone answers none of these; a problem list plus that context answers all four.

The 2024 site post describes the model as organizing observations, current report text, imaging studies, patient, order, prior studies, tracked observations, and electronic health record data.[^site-structure] The persona corresponds to the patient context in that list.

# A related unimplemented idea

An unmerged branch of the early extraction prototype contains `FHIR_Example_Structure`, a design note on persistent findings. Each finding becomes "a **tracked entity** with a FHIR ID that persists," so later reports of the same lesion add dated values to the existing resource.[^ipl-mvp-fhir] Its timeline shows one liver lesion at 1.6 cm, 2.1 cm, and 2.8 cm across three reports. Example queries are "show me the timeline for liver lesion" and "how has the renal calculus changed?".

It is a different idea from the persona. It addresses identity of a finding over time, which the current [Imaging Problem List](/data-structures/imaging-problem-list.md) approximates by grouping on finding code and location rather than by tracking a lesion. This is the repositories' only written design for durable patient imaging resources, a possible basis for a persona. It remains on an unmerged, single-commit branch of a superseded prototype. See [IPL-MVP extraction](/applications/ipl-mvp-extraction.md).

# What would have to be decided

Nothing about the persona has been specified, so this section states only what the deck leaves open rather than proposing answers. The deck leaves storage versus query-time assembly, ownership of each context category, encoding, and maintenance unspecified. See [open questions](/roadmap/open-questions.md) and [the 2026 roadmap](/roadmap/roadmap-2026.md).

[^deck]: "Open Imaging Data Model 2026 Status Update", January 2026
[^ipl-mvp-fhir]: FHIR_Example_Structure, IPL-MVP-ExtractionAndLabeling, Persistent_FHIR_Resources branch
[^site-structure]: "Data Model: Structure and Function", openimagingdata.org, 2024-01-25
