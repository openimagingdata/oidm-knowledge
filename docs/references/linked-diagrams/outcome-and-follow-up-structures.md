---
type: Reference
title: "Outcome and follow-up structures"
description: "Recommendations, later events, completion and pathways"
tags: ["use-cases", "data-structures"]
status: draft
generated: { by: codex/gpt-6/2026-10-01-linked-diagrams, at: 2026-10-01 }
sources:
  - id: board
    resource: sources/linked-diagrams/68X9qfSP5qA/
    title: "Outcome Tracking Schema"
---

# Outcome and follow-up structures

The board brings a radiology report together with future clinical events and potential actions. Events include later imaging, pathology, procedures, diagnoses, laboratory information, and disposition. Actions include notifying radiologists or others, creating registries, and work queues or dashboards. An annotation says patient factors should come from EHR and other sources separately from report information.[^board]

The follow-up proposal describes a recommendation with an exam or protocol, timeframe, finding/target, possible conditions or options, and a citation. Completion could be recognized through linked orders, suitable exam types, and timing; an outcome exam need not be exactly the exam named in the recommendation. It connects this work to an IPL whose findings may be live or inactive.[^board]

For our work, this supplies concrete Use Cases and data requirements for linking recommendations to later events. The cascading-use-cases note moves from individual feedback to practice/population statistics and clinical pathways. These are proposed extensions around shared patient data, not completed capabilities or a settled recommendation schema. The historical patient-factor annotation does not imply separate disconnected graphs in the current Persona.

Pillar connections: Use Cases; Data Structures. Related working pages: [Use cases](../../../knowledge/drafts/use-cases.md), [Data structures](../../../knowledge/drafts/data-structures.md), [Overview](../../../knowledge/drafts/overview.md).

Source captured 2026-10-01: [PNG](../../../sources/linked-diagrams/68X9qfSP5qA/original.png) · [SVG](../../../sources/linked-diagrams/68X9qfSP5qA/original.svg) · [Source contents](../../../sources/linked-diagrams/68X9qfSP5qA/scene-contents.json) · [Text elements](../../../sources/linked-diagrams/68X9qfSP5qA/text-elements.json) · [Capture metadata](../../../sources/linked-diagrams/68X9qfSP5qA/metadata.json).

[^board]: The captured board, especially Future Clinical Event; Actions; Recommendation Structure; Recognizing Follow-up Exams; Issue of use cases cascading; Imaging Problem List. Inspect the full-resolution PNG/SVG for layout and embedded material; text-elements.json records searchable text with element IDs and coordinates. Capture date does not establish when an undated proposal was written.
