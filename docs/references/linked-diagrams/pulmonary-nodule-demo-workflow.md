---
type: Reference
title: "Pulmonary-nodule demo workflow and role tagging"
description: "Multi-system nodule workflow, semantic annotations, element roles"
tags: ["use-cases", "data-structures", "sdks", "sample-applications"]
status: draft
generated: { by: codex/gpt-6/2026-10-01-linked-diagrams, at: 2026-10-01 }
sources:
  - id: board
    resource: sources/linked-diagrams/2ZpQ4nXotjV/
    title: "Pulm Nodule Demo Project"
---

# Pulmonary-nodule demo workflow and role tagging

The RSNA/ACR AI in Practice demo board proposes exchanging pulmonary-nodule descriptions among AI, PACS, reporting, and EHR tools using CDE-labeled FHIR Observations and FHIRcast. Its seven-step workflow carries AI output through review and reporting, brings prior nodules into the current context, associates observations over time, and returns structured results and text to the EHR.[^board]

“Smart Annotations” asks a viewer to infer the relevant definition from its tool, anatomy, and permissible measurements, then collect additional descriptors. “CDE 'Role' Standard Tagging” proposes standard codes for element roles such as presence, location, and types of size, so a consumer can find the relevant descriptor without hard-coding a different identifier for each set.[^board]

For our work, this anchors a concrete interoperation use case and the role-tagging proposal already cited in Relationships. Who accepts edits, assigns tracking identity, and communicates those changes remains open on the board. Treat this as a demo design; the Sample Applications pillar needs separate implementation evidence before describing any named vendor workflow as built.

Pillar connections: Use Cases; Data Structures; SDKs; Sample Applications. Related working pages: [Relationships](../../../knowledge/drafts/relationships.md), [Data structures](../../../knowledge/drafts/data-structures.md), [Sdks](../../../knowledge/drafts/sdks.md), [Sample applications](../../../knowledge/drafts/sample-applications.md).

Source captured 2026-10-01: [PNG](../../../sources/linked-diagrams/2ZpQ4nXotjV/original.png) · [SVG](../../../sources/linked-diagrams/2ZpQ4nXotjV/original.svg) · [Source contents](../../../sources/linked-diagrams/2ZpQ4nXotjV/scene-contents.json) · [Text elements](../../../sources/linked-diagrams/2ZpQ4nXotjV/text-elements.json) · [Capture metadata](../../../sources/linked-diagrams/2ZpQ4nXotjV/metadata.json).

[^board]: The captured board, especially Complete Workflow; Questions; Basic Principles; Smart Annotations; CDE 'Role' Standard Tagging. Inspect the full-resolution PNG/SVG for layout and embedded material; text-elements.json records searchable text with element IDs and coordinates. Capture date does not establish when an undated proposal was written.
