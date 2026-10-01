---
type: Reference
title: "Structured report representation"
description: "Complex findings, report sections, source-independent representations"
tags: ["data-structures", "foundation-context", "sdks"]
status: draft
generated: { by: codex/gpt-6/2026-10-01-linked-diagrams, at: 2026-10-01 }
sources:
  - id: board
    resource: sources/linked-diagrams/9Jgo8oKswiE/
    title: "Structured Report Representation"
---

# Structured report representation

The board's notes ask how to represent more than simple findings: technique, the radiologist's understanding of patient history, comparisons, complex subparts, causative relationships, grouped findings, broad anatomic negatives, diagnoses, differentials, recommendations, and communication. They distinguish these needs through concrete examples and a chest CT report/finding-list pair.[^board]

Another discussion calls for appropriate FHIR representation patterns and a handbook for choosing among them. It says representations should be interchangeable across sources, including modality data, AI, technologists, radiologists, and extraction from prior reports. Further notes propose experiments, stronger definition content, and clinical demonstration scenarios.[^board]

For our work, this is a source for the Observation layer's structural requirements and developer guidance. The common target representation is the reusable idea. Exact FHIR patterns, impression structures, probabilities, grouping, and recommendation forms remain questions on this board. The newer two-graph and shared-schema work supplies the current organizing context.

Pillar connections: Data Structures; Foundation Context; SDKs. Related working pages: [Data structures](../../../knowledge/drafts/data-structures.md), [Relationships](../../../knowledge/drafts/relationships.md), [Sdks](../../../knowledge/drafts/sdks.md).

Source captured 2026-10-01: [PNG](../../../sources/linked-diagrams/9Jgo8oKswiE/original.png) · [SVG](../../../sources/linked-diagrams/9Jgo8oKswiE/original.svg) · [Source contents](../../../sources/linked-diagrams/9Jgo8oKswiE/scene-contents.json) · [Text elements](../../../sources/linked-diagrams/9Jgo8oKswiE/text-elements.json) · [Capture metadata](../../../sources/linked-diagrams/9Jgo8oKswiE/metadata.json).

[^board]: The captured board, especially Report Finding List. Inspect the full-resolution PNG/SVG for layout and embedded material; text-elements.json records searchable text with element IDs and coordinates. Capture date does not establish when an undated proposal was written.
