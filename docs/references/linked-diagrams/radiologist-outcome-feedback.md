---
type: Reference
title: "Radiologist outcome feedback"
description: "Patient/anatomy/time-based outcome feedback"
tags: ["use-cases", "foundation-context", "data-structures"]
status: draft
generated: { by: codex/gpt-6/2026-10-01-linked-diagrams, at: 2026-10-01 }
sources:
  - id: board
    resource: sources/linked-diagrams/5QMQ1J2FYT3/
    title: "Radiologist Outcome Feedback"
---

# Radiologist outcome feedback

The outcome-feedback proposals ask for later pathology, imaging, or procedures relevant to a patient and body part, either as a notification or a digest of cases a radiologist read within a chosen timeframe. A proposed interface captures requests from the current study, shows new results and cases being awaited, and lets the user choose alert preferences.[^board]

The earlier material uses anatomy tags on pathology specimens and exam-type coverage to find relevant imaging. Later prostate and MSK examples connect pathology extraction, patient identity, anatomy, exam metadata, and time intervals. The biopsy/result sketch keeps cases in a waiting state until an appropriate pathology result arrives, then extracts data and notifies the relevant radiologists.[^board]

For our work, this is a concrete application idea built from shared anatomy, exam definitions, patient events, and longitudinal association. It supplies a stronger anchor than a generic claim about outcome dashboards. The proposed notification tools, matching rules, and architecture diagrams do not by themselves establish that a sample application was built.

Pillar connections: Use Cases; Foundation Context; Data Structures. Related working pages: [Use cases](../../../knowledge/drafts/use-cases.md), [Anatomic locations](../../../knowledge/drafts/anatomic-locations.md), [Exam types](../../../knowledge/drafts/exam-types.md), [Data structures](../../../knowledge/drafts/data-structures.md).

Source captured 2026-10-01: [PNG](../../../sources/linked-diagrams/5QMQ1J2FYT3/original.png) · [SVG](../../../sources/linked-diagrams/5QMQ1J2FYT3/original.svg) · [Source contents](../../../sources/linked-diagrams/5QMQ1J2FYT3/scene-contents.json) · [Text elements](../../../sources/linked-diagrams/5QMQ1J2FYT3/text-elements.json) · [Capture metadata](../../../sources/linked-diagrams/5QMQ1J2FYT3/metadata.json).

[^board]: The captured board, especially Proposal for Outcome Tracking; Prostate RadPath; MSK RadPath; Path Result ↔ Biopsy Procedure. Inspect the full-resolution PNG/SVG for layout and embedded material; text-elements.json records searchable text with element IDs and coordinates. Capture date does not establish when an undated proposal was written.
