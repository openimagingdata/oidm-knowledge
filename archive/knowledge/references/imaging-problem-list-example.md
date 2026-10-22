---
type: Worked Example
title: Imaging Problem List example
description: Two findings from a real Imaging Problem List in the imaging-problem-list sample data, with the grouping key and the temporal status derivation as the dev branch implements them.
tags: [references, data-structures, imaging-problem-list, worked-example]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: ipl-sample
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/sample_data/example2/MRN0000001_ipl.json
    title: MRN0000001_ipl.json, imaging-problem-list dev branch
  - id: ipl-claude
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/CLAUDE.md
    title: imaging-problem-list domain model notes, dev branch
  - id: viewer-app
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/viewer/app.js
    title: viewer/app.js, the status derivation and observation grouping, dev branch
  - id: ipl-readme
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/README.md
    title: imaging-problem-list README, main branch
---

# Provenance and status

The two findings below are copied unchanged from `sample_data/example2/MRN0000001_ipl.json` in the `imaging-problem-list` repository, read at commit `36fa30c` on the `dev` branch. That file holds 123 findings for one synthetic patient across ten exams; two are shown. The patient is synthetic, and so are the identifiers, dates, and report text. This is the same synthetic patient as the [Exam Finding List example](/references/exam-finding-list-example.md), and the first observation of the first finding here is the same observation that appears in that record. The status derivation described below is the one the viewer implements on `dev`; it is application behavior, not a field stored in the file. As with the Exam Finding List, the `$schema` URL in the file points at nothing published.

# Two findings

The file opens with a patient block and then a flat list of findings.

```json
{
  "$schema": "http://example.com/schemas/imaging_problem_list.json",
  "patient": { "id": "MRN0000001", "name": "John Doe", "dob": "1961-01-01" },
  "findings": [ ... ]
}
```

## A finding that was absent, then present, and stayed present

```json
{
  "id": "ipl-finding-116",
  "finding_type_code": "OIFM_OIDM_842151",
  "finding_type_display": "clavicle fracture",
  "anatomicLocation": {
    "locationId": "RID41741",
    "locationDisplay": "left clavicle"
  },
  "observations": [
    {
      "report_id": "f2b9b789-cb68-48c1-a09c-a1c34ddef340",
      "observation_id": "bone_fracture_clavicle_0",
      "exam_date": "2021-05-22",
      "exam_type_code": "26158-6",
      "exam_type_display": "XR Shoulder - left",
      "presence": "absent",
      "anatomicLocation": { "locationId": "RID41741", "locationDisplay": "left clavicle" },
      "reportText": "The humeral head, glenoid, clavicle, and scapula demonstrate normal bone density without fracture or lytic lesion."
    },
    {
      "report_id": "785eae28-f4b4-4268-9730-79292c7eff53",
      "observation_id": "clavicle_fracture_1",
      "exam_date": "2021-06-14",
      "exam_type_code": "30745-4",
      "exam_type_display": "XR Chest",
      "presence": "present",
      "anatomicLocation": { "locationId": "RID41741", "locationDisplay": "left clavicle" },
      "reportText": "An old healed left mid-clavicular fracture is identified."
    },
    {
      "report_id": "2887d285-2326-48fd-b950-b50a3a7fa13b",
      "observation_id": "clavicle_fracture_1",
      "exam_date": "2022-03-15",
      "exam_type_code": "30745-4",
      "exam_type_display": "XR Chest",
      "presence": "present",
      "anatomicLocation": { "locationId": "RID41741", "locationDisplay": "left clavicle" },
      "reportText": "An old healed fracture of the left mid-clavicle is identified."
    },
    {
      "report_id": "aabb5f5e-2a58-492e-a13b-f7840a9d4eb7",
      "observation_id": "clavicle_fracture_1",
      "exam_date": "2022-09-22",
      "exam_type_code": "29252-4",
      "exam_type_display": "CT Chest WO contrast",
      "presence": "present",
      "anatomicLocation": { "locationId": "RID41741", "locationDisplay": "left clavicle" },
      "reportText": "An old healed fracture of the left clavicle at the mid-shaft is identified with smooth corticated margins."
    }
  ]
}
```

## A finding that was never present

```json
{
  "id": "ipl-finding-003",
  "finding_type_code": "OIFM_CDE_000076",
  "finding_type_display": "pneumonia",
  "anatomicLocation": { "locationId": "RID1301", "locationDisplay": "lung" },
  "observations": [
    {
      "report_id": "19506144-0132-40e7-8d60-26ac5642df0b",
      "observation_id": "pneumonia_0",
      "exam_date": "2021-08-26",
      "exam_type_code": "36952-0",
      "exam_type_display": "CT Abdomen and Pelvis WO contrast",
      "presence": "absent",
      "anatomicLocation": { "locationId": "RID1301", "locationDisplay": "lung" },
      "reportText": "The visualized portions of the lower lungs are clear."
    },
    {
      "report_id": "2887d285-2326-48fd-b950-b50a3a7fa13b",
      "observation_id": "pneumonia_0",
      "exam_date": "2022-03-15",
      "exam_type_code": "30745-4",
      "exam_type_display": "XR Chest",
      "presence": "absent",
      "anatomicLocation": { "locationId": "RID1301", "locationDisplay": "lung" },
      "reportText": "The lungs are well expanded and clear. No focal consolidation, pleural effusion, or pneumothorax. No definite pulmonary nodule identified on radiograph."
    }
  ]
}
```

# Walkthrough

## What changed from the Exam Finding List

An [Exam Finding List](/glossary/exam-finding-list.md) is organized by exam; an [Imaging Problem List](/glossary/imaging-problem-list.md) is organized by finding. The same [Observation](/glossary/observation.md) appears in both. `bone_fracture_clavicle_0` on 2021-05-22 is an entry in the shoulder radiograph's finding list and the first observation under `ipl-finding-116` here, and `report_id` is the `diagnosticReportId` of that exam. Each observation in the problem list also carries the exam date, the LOINC [exam type](/glossary/exam-type.md), the presence value, and the verbatim report text, so the timeline reads without fetching the source exams.

| Field | Where it comes from |
|---|---|
| `report_id` | the `diagnosticReportId` of the Exam Finding List |
| `observation_id` | the `observationId` within that list |
| `exam_date`, `exam_type_code`, `exam_type_display` | the exam envelope of that list |
| `presence` | the value of the presence [attribute](/glossary/attribute.md) on that observation |
| `anatomicLocation` | the observation's [anatomic location](/glossary/anatomic-location.md) |
| `reportText` | the verbatim span the observation came from |

`presence` is flattened from the attribute code and value code pair in the Exam Finding List into a plain string. The values seen in this file are `present`, `absent`, and `indeterminate`.

## The grouping key

Observations are grouped by finding type **and** anatomic location, taking `locationId` as the second half of the key.[^ipl-claude] Both example findings carry an `anatomicLocation` at the finding level, and every observation under them repeats the same location.

The consequence is that one finding code can produce several entries. The [finding model](/glossary/finding-model.md) `OIFM_OIDM_842151` for clavicle fracture would yield a separate entry for a right clavicle fracture, because the location differs. This is why the documented rule is that consumers key on the problem list finding `id`, here `ipl-finding-116`, and not on `finding_type_code`.

The `id` values are positional in this file, running from `ipl-finding-001` upward. They are identifiers within one patient's list, not registry identifiers.

## How status is derived

Temporal status is computed at display time by the viewer, not stored.[^viewer-app] For one finding, the rule reads its observations in full and then only the most recent:

1. No observations at all gives **Unknown**.
2. Sort the observations by exam date, most recent first.
3. If the most recent observation is `present`, and every observation is `present`, and there is more than one, the status is **Always**.
4. If the most recent observation is `present` otherwise, the status is **Current**.
5. If the most recent is not `present` but some earlier observation was, the status is **Resolved**.
6. If no observation was ever `present`, the status is **Never**.

Applying it to the two examples:

| Finding | Observations | Most recent | Ever present | Status |
|---|---|---|---|---|
| `ipl-finding-116`, clavicle fracture | absent 2021-05-22, present 2021-06-14, present 2022-03-15, present 2022-09-22 | present | yes | Current |
| `ipl-finding-003`, pneumonia | absent 2021-08-26, absent 2022-03-15 | absent | no | Never |

The clavicle fracture is **Current** rather than **Always** because of the single absent observation at the front of its history. The distinction is real and clinically legible: the fracture was genuinely not there on the 2021-05-22 shoulder radiograph, and was reported as an old healed fracture from 2021-06-14 onward. Pneumonia is **Never**, which is not the same as having no entry at all. Two exams looked at the lungs and found no pneumonia, and the problem list records that they looked.

The viewer sections a patient's list under these four headings, showing only the headings that have findings, and offers the same four as a filter.

## Grouping observations by exam

Within a finding, the viewer also groups observations by `report_id` so that several observations from one exam collapse into one row, sorted most recent first. A group counts as present if any observation in it is present, and the group's report texts are concatenated. This is what makes repeated instances of one finding type on a single exam, such as several stones in one kidney, read as one entry on the timeline.

## What this maps to in FHIR

The repository states the mapping: an Imaging Problem List is a **Report** containing **Condition** objects labeled with the finding identifier, each holding **Observation** objects that record which **DiagnosticReports** the finding was documented on, with exam date and LOINC exam type.[^ipl-readme] That mapping is documented and is not implemented anywhere in the repository.

[^ipl-sample]: MRN0000001_ipl.json, imaging-problem-list dev branch
[^ipl-claude]: imaging-problem-list domain model notes, dev branch
[^viewer-app]: viewer/app.js, the status derivation and observation grouping, dev branch
[^ipl-readme]: imaging-problem-list README, main branch
