---
type: Data Structure
title: Exam Finding List
description: The per-exam structure that holds every finding declared present or absent on one imaging exam, its full field list on both branches, where its contents come from, and the FHIR and IHE encodings it is meant to reach.
tags: [data-structures, exam-finding-list, loinc, fhir, provenance]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
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

"In the context of an imaging exam, a list of the findings declared as present/absent on that exam."[^ipl-main] An [Exam Finding List](/glossary/exam-finding-list.md) is the second level of [the hierarchy](/data-structures/hierarchy.md): every [observation](/data-structures/observation.md) from one exam, wrapped in that exam's identity.

The specification states two requirements. The list "must also have basic information (keyed by a curated list of [LOINC](/glossary/loinc.md) codes) about what exam this is." And "the same finding type may be declared as present multiple times; each time is a separate entry in the EFL."[^ipl-main]

# Fields

The structure is JSON. The table below is the stable specification on `main`, with the one development-branch addition marked.[^ipl-main-claude][^efl-sample]

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

A trimmed real record, with a field-by-field walkthrough, is in [the Exam Finding List example](/references/exam-finding-list-example.md).

## The exam header

The LOINC code is not decoration. It is the key that lets the problem list say which kind of exam an observation came from, and it is what makes "was this looked for on a chest study?" answerable. The ten sample exams use seven distinct LOINC codes covering radiography, computed tomography, ultrasound, and magnetic resonance. The requirement is stated as a *curated* list of LOINC codes, which is the same need the [exam types](/semantic-foundation/exam-types/) area exists to serve; no such curated list has been published.

## Repeatable findings

One entry per instance is a deliberate rule, not an artifact. "The same finding type may appear multiple times in one exam (e.g., multiple kidney stones). Each instance gets a separate entry with its own `observationId`."[^ipl-main-claude] The count of a finding on an exam is therefore the number of entries. The [Imaging Problem List](/data-structures/imaging-problem-list.md) re-collapses them by source report, so a patient timeline shows one row per exam rather than three rows for three stones.

# Where the contents come from

The specification is explicit that an Exam Finding List has two possible provenances: it "can be generated by LLM from an existing report or generated live during exam time; each Observation should include some kind of [provenance](/glossary/provenance.md) marker."[^ipl-main] No provenance field exists in the current format. The marker is a stated requirement without an implementation.

The deck widens the sources further, listing dictation, artificial intelligence tools, and interpretation-time interfaces as the three origins of the findings in one list.[^deck] That is the case the provenance marker is for: an observation produced by an AI tool and an observation dictated by a radiologist would sit side by side in the same list and need to be told apart. The [FHIR lineage](/data-structures/fhir-mapping.md) solved the same problem with `status`, `preliminary` for the machine and `final` for the radiologist.

In practice today the sample lists were generated from a working spreadsheet. `generate_efl_from_excel.py` reads a worksheet with columns Exam Date, Exam Type, Exam Code, Finding, OIDM Finding Model Name, OIDM FMID, Presence OIFMA_ID, Present/Absent, and Text, groups rows by exam, and writes one file per exam with a fresh UUID as the `diagnosticReportId`.[^excel-script] The live path, from report text through extraction and coding, is the [report extraction platform](/applications/report-extraction-platform.md).

# The diagram

The README carries a hand-drawn figure, `exam-finding-list.png`, that makes the case in one picture.[^efl-diagram] On the left is the FINDINGS section of a chest computed tomography report with two kinds of highlight: green over the positive statements the list should capture, including biapical scarring, subsegmental atelectasis, nine separately numbered pulmonary nodules, a calcified granuloma, ectatic pulmonary arteries, coronary artery calcifications, a pacing device, colonic diverticular disease, thoracic dextroscoliosis, a T10 compression fracture, and degenerative changes; and pink over the explicit negatives, "No pleural effusion", "No enlarged supraclavicular, axillary, mediastinal or hilar lymph nodes", and "No pericardial effusion".

On the right is a table headed "Exam Finding List" with three columns, Finding, CDE Set ID, and Count. Pulmonary nodule carries a count of 8, subsegmental atelectasis 2, and the four negatives carry a count of 0, which is the point: a zero count is a recorded observation of absence, not a missing row. Starred rows mark findings that had no entry in the finding ontology at the time the figure was drawn. The identifiers in the figure are RadElement `RDES####` [CDE set](/glossary/cde-set.md) codes rather than OIFM identifiers, which dates it to before the finding model corpus took that role.

# FHIR and IHE

The documented FHIR encoding is "**DiagnosticReport** containing a list of **Observation** objects, with a finding code on each Observation and a list of components with attribute codes and values (especially present/absent and change from prior)."[^ipl-main] One [FHIR DiagnosticReport](/glossary/fhir-diagnostic-report.md), one Observation per finding, attributes as components.

That mapping is documented and implemented nowhere. No FHIR resource classes exist in the extraction platform's source, and a search across it for `DiagnosticReport` or `fhir` returns nothing. The only real FHIR documents in the repository are two *input* samples, and those do not use the component pattern the specification prescribes, because the pattern describes the output. Full detail is in [FHIR mapping](/data-structures/fhir-mapping.md).

The deck adds a second target: an Exam Finding List "connects to IHE Imaging Diagnostic Report (IDR) FHIR representation."[^deck] The [IDR profile](/glossary/imaging-diagnostic-report.md) is not mentioned anywhere in the `imaging-problem-list` repository, on any branch. The alignment is a stated goal, and the places where the two models would have to be reconciled are set out in [IHE IDR alignment](/data-structures/ihe-idr-alignment.md).

# Schema status

There is no published JSON Schema. Every sample file opens with a `$schema` URL pointing into the repository at `schema/exam-problem-list-schema.json`, and the repository's own notes say plainly that it "doesn't exist yet."[^ipl-main-claude] The structure is defined by the prose above, by the sample data, and by the two scripts that write and read it. A formal model layer with JSON Schema export is [issue 1](https://github.com/openimagingdata/imaging-problem-list/issues/1); see [the IPL data model system roadmap](/roadmap/ipl-data-model-system.md).

[^ipl-main]: imaging-problem-list README, main branch
[^ipl-main-claude]: imaging-problem-list domain model notes, main branch
[^ipl-claude-dev]: imaging-problem-list domain model notes, dev branch
[^efl-sample]: An Exam Finding List with anatomic locations, dev branch
[^efl-diagram]: exam-finding-list.png, the diagram in the imaging-problem-list README
[^excel-script]: generate_efl_from_excel.py, the Exam Finding List generator
[^deck]: "Open Imaging Data Model 2026 Status Update", January 2026
