---
type: Reference
title: "Longitudinal integration discussions"
description: "Tracked identity, per-exam findings, relevance filtering"
tags: ["data-structures", "foundation-context", "use-cases"]
status: draft
generated: { by: codex/gpt-6/2026-10-01-linked-diagrams, at: 2026-10-01 }
sources:
  - id: board
    resource: sources/linked-diagrams/1PrQV4pohsD/
    title: "ACR OIDM\u2194\ufe0eEpic Connections"
---

# Longitudinal integration discussions

The board's discussions connect coded findings, longitudinal lesion tracking, anatomy-based relevance, and EHR/reporting/viewer access. The breast-imaging sketch gives multiple study-specific findings one shared lesion identity and raises questions about current status, disappearance, and changes over time.[^board]

The board asks who assigns tracking identifiers, whether FHIR Condition could represent a longitudinal finding, how a tracked lesion might have several classifications, and how unverified results might be managed. It proposes using exam/anatomy coverage to decide which prior lesions should be considered during a current study. The reporting-assistant example reminds the radiologist to update relevant prior findings.[^board]

For our work, this is a source for persistent patient entities, per-exam observations, and context-based retrieval. The current Data Structures page should lead the explanation. A question about Condition, or an individual's “yes” in the notes, does not establish an adopted FHIR mapping. The named organizations and vendor roles document the discussion's context, not completed cross-system deployment.

Pillar connections: Data Structures; Foundation Context; Use Cases. Related working pages: [Data structures](../../../knowledge/drafts/data-structures.md), [Exam types](../../../knowledge/drafts/exam-types.md), [Use cases](../../../knowledge/drafts/use-cases.md).

Source captured 2026-10-01: [PNG](../../../sources/linked-diagrams/1PrQV4pohsD/original.png) · [SVG](../../../sources/linked-diagrams/1PrQV4pohsD/usable.svg) · [Source contents](../../../sources/linked-diagrams/1PrQV4pohsD/scene-contents.json) · [Text elements](../../../sources/linked-diagrams/1PrQV4pohsD/text-elements.json) · [Capture metadata](../../../sources/linked-diagrams/1PrQV4pohsD/metadata.json).

[^board]: The captured board, especially Longitudinal Tracking; Breast Imaging Lesions Data Model. Inspect the full-resolution PNG/SVG for layout and embedded material; text-elements.json records searchable text with element IDs and coordinates. Capture date does not establish when an undated proposal was written.
