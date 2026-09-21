---
type: Glossary Term
title: LOINC
description: Logical Observation Identifiers Names and Codes, the system OIDM uses to identify exam types on Exam Finding Lists and reports.
tags: [glossary, semantic-foundation, terminologies, exam-types]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: loinc
    resource: https://loinc.org/
    title: LOINC, Regenstrief Institute
  - id: ipl-claude
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/CLAUDE.md
    title: imaging-problem-list domain model, data standards, dev branch
  - id: ipl-readme
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/README.md
    title: imaging-problem-list README, curated list of LOINC codes
  - id: roadmap
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/docs/product-roadmap.md
    title: med-ontology-lookup product roadmap, radiology profile
  - id: fhir-sample
    resource: https://github.com/openimagingdata/FHIRSamples/blob/9ae2fa934298e51789e355c9f4e0b71fabf6b5aa/lung_ca_screening_example/example1OIDMreport.json
    title: Lung screening DiagnosticReport coded with LOINC
---

# LOINC

Logical Observation Identifiers Names and Codes, the Regenstrief Institute's system for identifying laboratory and clinical observations, including imaging procedures.[^loinc] In OIDM, LOINC's job is [exam type](/glossary/exam-type.md) identification, not finding identification.

An [Exam Finding List](/glossary/exam-finding-list.md) carries the exam's LOINC code as `examInfo.studyLoincCode`, described as "LOINC codes: Used for exam type identification (e.g., '72133-2' = CT Abdomen and Pelvis Without Contrast)."[^ipl-claude] The specification says the structure "must also have basic information (keyed by a curated list of LOINC codes) about what exam this is."[^ipl-readme] The lineage FHIR sample codes its DiagnosticReport the same way, with `87279-6 CT Chest for Screening`.[^fhir-sample]

The division of labour is stated in the terminology roadmap: radiology "orderables live in the LOINC/RSNA Radiology Playbook, while findings, anatomy, and report language live in RadLex."[^roadmap]

## Synonyms and near-synonyms

- **[LOINC/RSNA Radiology Playbook](/glossary/loinc-rsna-radiology-playbook.md)** is the radiology part of LOINC, governed separately.
- **Orderable** and **procedure code** describe what a radiology LOINC code names.
- **`studyLoincCode`** and **`exam_type_code`** are the field names that hold one.
- **[RadElement](/glossary/radelement.md)** codes are not LOINC codes, though both can appear as index code systems.

## Identifier form

Digits, a hyphen, and a check digit, for example `72133-2`. The lookup tooling auto-detects the form with a pattern of one to seven digits, a hyphen, and one or two digits.

## Where it is used

[Exam types overview](/semantic-foundation/exam-types/overview.md), [Existing building blocks](/semantic-foundation/exam-types/existing-building-blocks.md), and [Exam Finding List](/data-structures/exam-finding-list.md).

## Conflicts

The "curated list of LOINC codes" the specification refers to does not exist as an artifact. Exam types are documented as goals and as building blocks, not as a published catalog; see [Exam types](/roadmap/exam-types.md).

[^loinc]: LOINC, Regenstrief Institute
[^ipl-claude]: imaging-problem-list domain model, dev branch
[^ipl-readme]: imaging-problem-list README
[^roadmap]: med-ontology-lookup product roadmap
[^fhir-sample]: Lung screening DiagnosticReport
