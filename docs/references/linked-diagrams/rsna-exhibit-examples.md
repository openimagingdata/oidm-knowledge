---
type: Reference
title: "RSNA exhibit examples"
description: "Comparable observations, multiple producers, AI discrepancies"
tags: ["foundation-context", "data-structures", "use-cases"]
status: draft
generated: { by: codex/gpt-6/2026-10-01-linked-diagrams, at: 2026-10-01 }
sources:
  - id: board
    resource: sources/linked-diagrams/19Qjzb9AmAT/
    title: "Figures for RSNA Edu Exhibit"
---

# RSNA exhibit examples

The exhibit panels illustrate how definitions, Observation values, FHIR representations, and generated clinical sentences fit together. Pulmonary nodule is the expanded example, with presence, composition, size, and location connected to the corresponding components. Other examples include acute aortic syndrome, stroke, and diverticulitis.[^board]

A source panel feeds one Observation representation from dictation/reporting, DICOM SR, exam metadata, current and prior report extraction, longitudinal findings, and AI. The AI-monitoring panel compares two descriptions of the same finding: the radiologist's nodule is 6.0 mm with a composition value, while the model's is 7.5 mm and omits composition.[^board]

For our work, these are useful teaching examples of shared semantics making data from different producers comparable. The AI discrepancy is a specific Use Cases illustration, not a reported performance result. The panels use an earlier component-based definition representation. They can inform a new explanation of the graph approach without being presented as the current schema or as proof of an operational monitoring application.

Pillar connections: Foundation Context; Data Structures; Use Cases. Related working pages: [Data structures](../../../knowledge/drafts/data-structures.md), [Next generation schema](../../../knowledge/drafts/next-generation-schema.md), [Use cases](../../../knowledge/drafts/use-cases.md).

Source captured 2026-10-01: [PNG](../../../sources/linked-diagrams/19Qjzb9AmAT/original.png) · [SVG](../../../sources/linked-diagrams/19Qjzb9AmAT/original.svg) · [Source contents](../../../sources/linked-diagrams/19Qjzb9AmAT/scene-contents.json) · [Text elements](../../../sources/linked-diagrams/19Qjzb9AmAT/text-elements.json) · [Capture metadata](../../../sources/linked-diagrams/19Qjzb9AmAT/metadata.json).

[^board]: The captured board, especially Figure 1; Figure 2; Figure 3; Figure 4; Figure 5. Inspect the full-resolution PNG/SVG for layout and embedded material; text-elements.json records searchable text with element IDs and coordinates. Capture date does not establish when an undated proposal was written.
