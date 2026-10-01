---
type: Reference
title: "CDE and Observation worked example"
description: "Definitions connected to instance values and clinical text"
tags: ["foundation-context", "data-structures", "sdks"]
status: draft
generated: { by: codex/gpt-6/2026-10-01-linked-diagrams, at: 2026-10-01 }
sources:
  - id: board
    resource: sources/linked-diagrams/ArAkPl5S3kD/
    title: "CDE\u2194\ufe0eObservation"
---

# CDE and Observation worked example

The pulmonary-nodule example connects a CDE definition, its elements and permissible values, a particular Observation, and FHIR JSON. The Observation selects values for presence, composition, size, and location, carries identifiers and anatomy, and supplies a sentence template that renders a clinical description. The arrows make the definition-to-instance interconnection concrete.[^board]

“Where Observation objects can come from” lists current dictation, PACS annotation, prior-report extraction, structured reporting, AI, DICOM SR, and EHR data. The code-system meeting note proposes wrapper implementations and import/export work involving FHIR, DICOM SR, and OMOP, together with vendor demonstrations.[^board]

For our work, this is a compact historical example of Foundation Context informing a patient Observation and developer tools translating representations. It predates the shared graph schema and uses CDE Set/Element structures and fixed example codes. Reuse the conceptual interconnection and multiple-source idea; consult current schema and SDK documents for today's classes and interfaces. The board does not demonstrate an implemented two-graph system or certify the example as conformant with a current FHIR profile.

Pillar connections: Foundation Context; Data Structures; SDKs. Related working pages: [Next generation schema](../../../knowledge/drafts/next-generation-schema.md), [Data structures](../../../knowledge/drafts/data-structures.md), [Sdks](../../../knowledge/drafts/sdks.md).

Source captured 2026-10-01: [PNG](../../../sources/linked-diagrams/ArAkPl5S3kD/original.png) · [SVG](../../../sources/linked-diagrams/ArAkPl5S3kD/original.svg) · [Source contents](../../../sources/linked-diagrams/ArAkPl5S3kD/scene-contents.json) · [Text elements](../../../sources/linked-diagrams/ArAkPl5S3kD/text-elements.json) · [Capture metadata](../../../sources/linked-diagrams/ArAkPl5S3kD/metadata.json).

[^board]: The captured board, especially CDE Set: RDES195; Observation; Template; Where Observation objects can come from; Code System Team. Inspect the full-resolution PNG/SVG for layout and embedded material; text-elements.json records searchable text with element IDs and coordinates. Capture date does not establish when an undated proposal was written.
