---
type: Reference
title: "Imaging context object model"
description: "Patient/exam/report context, provenance, platform operations"
tags: ["data-structures", "foundation-context", "sdks"]
status: draft
generated: { by: codex/gpt-6/2026-10-01-linked-diagrams, at: 2026-10-01 }
sources:
  - id: board
    resource: sources/linked-diagrams/1sEx11UZ3gq/
    title: "OIDM Object Model"
---

# Imaging context object model

The central map brings patient identity, orders, studies, current and prior reports, tracked observations, and other EHR information into one imaging context. Observations include identification, classification, tracking, anatomy, and coded values. Study-type branches distinguish modality, focused anatomy, included anatomy, laterality, and contrast information.[^board]

The board's discussion proposes standard content with wrapper libraries and asks about an integrated runtime or microservices, event hooks, platform commands, report text during authoring, image connections, and provenance. It explicitly asks how to record who has seen, approved, changed, or rejected an Observation. A class sketch separately shows the then-proposed CDE and Observation structures.[^board]

For our work, this anchors the breadth of patient and application context and the need for developer operations around it. The current Data Structures and SDK pillars can draw on those questions. “ObservationType,” nested CDE classes, and the historic standards notes retain their original context; they do not supersede the owner's current finding/diagnosis definitions or the shared graph schema.

Pillar connections: Data Structures; Foundation Context; SDKs. Related working pages: [Data structures](../../../knowledge/drafts/data-structures.md), [Sdks](../../../knowledge/drafts/sdks.md), [Overview](../../../knowledge/drafts/overview.md).

Source captured 2026-10-01: [PNG](../../../sources/linked-diagrams/1sEx11UZ3gq/original.png) · [SVG](../../../sources/linked-diagrams/1sEx11UZ3gq/original.svg) · [Source contents](../../../sources/linked-diagrams/1sEx11UZ3gq/scene-contents.json) · [Text elements](../../../sources/linked-diagrams/1sEx11UZ3gq/text-elements.json) · [Capture metadata](../../../sources/linked-diagrams/1sEx11UZ3gq/metadata.json).

[^board]: The captured board, especially OIDM Data Context mind map; Stuff in CDE Set to get to later; For Next Time. Inspect the full-resolution PNG/SVG for layout and embedded material; text-elements.json records searchable text with element IDs and coordinates. Capture date does not establish when an undated proposal was written.
