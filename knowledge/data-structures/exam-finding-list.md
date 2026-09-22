---
type: Data Structure
title: Exam Finding List
description: Findings from one exam, their fields and sources, and planned FHIR and IHE encodings.
tags: [data-structures, exam-finding-list, loinc, fhir, provenance]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:34:50Z }
sources:
  - id: ipl-main
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/README.md
    title: imaging-problem-list README, main branch, the stable specification
  - id: ipl-main-claude
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/CLAUDE.md
    title: imaging-problem-list domain model notes, main branch
  - id: ipl-claude-dev
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/CLAUDE.md
    title: imaging-problem-list domain model notes, dev branch
  - id: efl-sample
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/sample_data/example2/xr_shoulder_20210522_efl.json
    title: An Exam Finding List with anatomic locations, imaging-problem-list dev branch
  - id: efl-diagram
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/exam-finding-list.png
    title: exam-finding-list.png, the diagram in the imaging-problem-list README
  - id: excel-script
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/scripts/generate_efl_from_excel.py
    title: generate_efl_from_excel.py, the Exam Finding List generator
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: "Open Imaging Data Model 2026 Status Update, January 2026"
---

# Definition

"In the context of an imaging exam, a list of the findings declared as present/absent on that exam."[^ipl-main] An [Exam Finding List](/glossary/exam-finding-list.md) combines an exam's identity with its [observations](/data-structures/observation.md). It is the second level of [the hierarchy](/data-structures/hierarchy.md).

The imaging-problem-list README states two requirements. The list "must also have basic information (keyed by a curated list of [LOINC](/glossary/loinc.md) codes) about what exam this is." And "the same finding type may be declared as present multiple times; each time is a separate entry in the EFL."[^ipl-main]

# Fields

The JSON fields follow the stable specification on `main`, with the development branch's addition marked.[^ipl-main-claude][^efl-sample]

| Field | Type | Required | Notes |
|---|---|---|---|
| `$schema` | URL string | present in samples | Points at `github.com/openimagingdata/imaging-problem-list/schema/exam-problem-list-schema.json`. No such file exists; see below. |
| `diagnosticReportId` | UUID string | yes | identity of the report this list came from. The [Imaging Problem List](/data-structures/imaging-problem-list.md) points back at it. |
| `patientInfo.patientIdentifier` | string | yes | medical record number |
| `patientInfo.patientDOB` | date string | yes | birth date |
| `examInfo.studyIdentifier` | string | yes | the exam's own identifier |
| `examInfo.studyDateTime` | ISO 8601 timestamp | yes | when the exam happened; this is what orders observations over time |
| `examInfo.studyLoincCode` | LOINC code | yes | the [exam type](/glossary/exam-type.md), for example `26158-6` for a left shoulder radiograph |
| `examInfo.studyDescription` | string | yes | display name of the exam |
| `findings[]` | array | yes | one entry per observation instance |
| `findings[].observationId` | string | yes | unique within this list |
| `findings[].findingCode` | `OIFM_[A-Z]{3,4}_[0-9]{6}` | yes | the [OIFM](/glossary/oifm.md) identifier |
| `findings[].findingDescription` | string | yes | the finding model's display name |
| `findings[].attributes[]` | array | yes | each with `attributeCode`, `attributeDescription`, `attributeValueCode`, `attributeValueDescription` |
| `findings[].anatomicLocation` | `{locationId, locationDisplay}` | optional, **development branch only** | a [RadLex identifier](/glossary/radlex-id.md) from the `anatomic-locations` package, "omitted when the finding is not anatomically localizable"[^ipl-claude-dev] |
| `findings[].reportText` | string | optional | verbatim quote from the report |

`anatomicLocation` is the only field the development branch adds. Data produced against the stable specification does not carry it, and the stable branch's own sample files do not have it.

See [the Exam Finding List example](/references/exam-finding-list-example.md) for a sample record and field walkthrough.

## The exam header

The LOINC code identifies the exam type, allowing queries such as "was this looked for on a chest study?" The ten sample exams use seven LOINC codes covering radiography, computed tomography, ultrasound, and magnetic resonance. The imaging-problem-list README requires a curated list of codes, the purpose of the [exam types](/semantic-foundation/exam-types/) work. No such list has been published.

## Repeatable findings

One entry per instance is a deliberate rule, not an artifact. "The same finding type may appear multiple times in one exam (e.g., multiple kidney stones). Each instance gets a separate entry with its own `observationId`."[^ipl-main-claude] The number of entries gives the count. The [Imaging Problem List](/data-structures/imaging-problem-list.md) groups them by source report for display as one timeline row per exam.

# Where the contents come from

An Exam Finding List "can be generated by LLM from an existing report or generated live during exam time; each Observation should include some kind of [provenance](/glossary/provenance.md) marker."[^ipl-main] No provenance field exists in the current format. The marker is a stated requirement without an implementation.

The deck lists dictation, artificial intelligence tools, and interpretation-time interfaces as sources of findings.[^deck] Provenance would distinguish AI-produced and radiologist-dictated observations in the same list. The [FHIR lineage](/data-structures/fhir-mapping.md) used `status`, with `preliminary` for the machine and `final` for the radiologist.

The sample lists come from a spreadsheet. `generate_efl_from_excel.py` reads these columns: Exam Date, Exam Type, Exam Code, Finding, OIDM Finding Model Name, OIDM FMID, Presence OIFMA_ID, Present/Absent, and Text. It groups rows by exam and writes one file per exam with a fresh UUID as the `diagnosticReportId`.[^excel-script] The [report extraction platform](/applications/report-extraction-platform.md) extracts and codes findings from report text.

# The diagram

The README's hand-drawn `exam-finding-list.png` shows a chest computed tomography report beside a findings table.[^efl-diagram] The report's FINDINGS section highlights positive statements in green. These include biapical scarring, subsegmental atelectasis, nine numbered pulmonary nodules, a calcified granuloma, ectatic pulmonary arteries, coronary artery calcifications, a pacing device, colonic diverticular disease, thoracic dextroscoliosis, a T10 compression fracture, and degenerative changes. Pink marks the explicit negatives: "No pleural effusion", "No enlarged supraclavicular, axillary, mediastinal or hilar lymph nodes", and "No pericardial effusion".

The table is headed "Exam Finding List" with Finding, CDE Set ID, and Count columns. Pulmonary nodule has a count of 8, subsegmental atelectasis 2, and the four negatives 0. Zero records an observation of absence. Starred rows mark findings missing from the ontology at the time. The figure uses RadElement `RDES####` [CDE set](/glossary/cde-set.md) codes, predating the use of OIFM identifiers.

# FHIR and IHE

The documented FHIR encoding is "**DiagnosticReport** containing a list of **Observation** objects, with a finding code on each Observation and a list of components with attribute codes and values (especially present/absent and change from prior)."[^ipl-main] One [FHIR DiagnosticReport](/glossary/fhir-diagnostic-report.md), one Observation per finding, attributes as components.

That mapping is documented and implemented nowhere. The extraction platform's source code contains no FHIR resource classes or references to `DiagnosticReport` or `fhir`. Its only FHIR documents are two input samples, and those do not use the documented component pattern, because that pattern describes the output. See [FHIR mapping](/data-structures/fhir-mapping.md).

The deck states that an Exam Finding List "connects to IHE Imaging Diagnostic Report (IDR) FHIR representation."[^deck] No branch of `imaging-problem-list` mentions the [IDR profile](/glossary/imaging-diagnostic-report.md). See [IHE IDR alignment](/data-structures/ihe-idr-alignment.md) for the differences to resolve in pursuing this goal.

# Schema status

There is no published JSON Schema. Every sample's `$schema` URL points to `schema/exam-problem-list-schema.json`, which the repository notes say "doesn't exist yet."[^ipl-main-claude] Prose, samples, and the two scripts that write and read the structure define it. [Issue 1](https://github.com/openimagingdata/imaging-problem-list/issues/1) requests formal models with JSON Schema export. See [the IPL data model system roadmap](/roadmap/ipl-data-model-system.md).

[^ipl-main]: imaging-problem-list README, main branch
[^ipl-main-claude]: imaging-problem-list domain model notes, main branch
[^ipl-claude-dev]: imaging-problem-list domain model notes, dev branch
[^efl-sample]: An Exam Finding List with anatomic locations, dev branch
[^efl-diagram]: exam-finding-list.png, the diagram in the imaging-problem-list README
[^excel-script]: generate_efl_from_excel.py, the Exam Finding List generator
[^deck]: "Open Imaging Data Model 2026 Status Update", January 2026
