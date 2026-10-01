---
type: Reference
title: "Imaging Problem List"
description: "Per-exam findings, longitudinal association, integrated clinical context"
tags: ["data-structures", "use-cases"]
status: draft
generated: { by: codex/gpt-6/2026-10-01-linked-diagrams, at: 2026-10-01 }
sources:
  - id: board
    resource: sources/linked-diagrams/2jUZLu229km/
    title: "Imaging Problem List"
---

# Imaging Problem List

The board develops a patient-level history of imaging findings from report-level finding lists. Its central flow is reports → Extractor → finding lists → Assembler → Imaging Problem List. The chest CT example retains explicitly absent findings as well as positive ones. The Assembler reorganizes observations by finding across exams.[^board]

The “Maintaining the IPL” note asks whether this should be an EHR-maintained view, a dynamically regenerated and cached representation, or a service available to reporting systems and viewers. Its v2 note adds an important distinction: explicit longitudinal associations may add information beyond merely collecting reports. The appendectomy scenario and “master, integrated knowledge base” note extend the idea to operative, pathology, and other clinical information.[^board]

For our work, this is an anchor for longitudinal patient data and context-sensitive applications: prior-finding displays, draft reporting, MRI safety, quality checks, and downstream care workflows. Read it beside the current Data Structures page and the owner's integrated Persona framing. The board's storage, FHIR representation, and vendor responsibilities are questions and proposals, not evidence of completed integration.

Pillar connections: Data Structures; Use Cases. Related working pages: [Data structures](../../../knowledge/drafts/data-structures.md), [Use cases](../../../knowledge/drafts/use-cases.md), [Overview](../../../knowledge/drafts/overview.md).

Source captured 2026-10-01: [PNG](../../../sources/linked-diagrams/2jUZLu229km/original.png) · [SVG](../../../sources/linked-diagrams/2jUZLu229km/original.svg) · [Source contents](../../../sources/linked-diagrams/2jUZLu229km/scene-contents.json) · [Text elements](../../../sources/linked-diagrams/2jUZLu229km/text-elements.json) · [Capture metadata](../../../sources/linked-diagrams/2jUZLu229km/metadata.json).

[^board]: The captured board, especially Imaging Problem List; Maintaining the IPL; Ingredients; Clinical Scenario. Inspect the full-resolution PNG/SVG for layout and embedded material; text-elements.json records searchable text with element IDs and coordinates. Capture date does not establish when an undated proposal was written.
