---
type: Worked Example
title: Exam Finding List example
description: A real Exam Finding List from the imaging-problem-list sample data, trimmed to five findings, with a field-by-field walkthrough.
tags: [references, data-structures, exam-finding-list, worked-example]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: efl-sample
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/sample_data/example2/xr_shoulder_20210522_efl.json
    title: xr_shoulder_20210522_efl.json, imaging-problem-list dev branch
  - id: efl-report
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/sample_data/example2/xr_shoulder_20210522.md
    title: xr_shoulder_20210522.md, the synthetic report the findings were extracted from
  - id: ipl-claude
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/CLAUDE.md
    title: imaging-problem-list domain model notes, dev branch
  - id: ipl-readme
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/README.md
    title: imaging-problem-list README, main branch
---

# Provenance and status

The record below is copied from `sample_data/example2/xr_shoulder_20210522_efl.json` in the `imaging-problem-list` repository, read at commit `36fa30c` on the `dev` branch, and trimmed from nine findings to five. Nothing else was changed. The patient is synthetic: the sample data set is written test data, and the identifier, birth date, and report text do not belong to a real person. The `dev` branch is the current state of that repository, and it is the branch on which findings carry an `anatomicLocation`. There is no published JSON Schema behind the `$schema` URL in the file; the repository contains no such file, and a formal model layer for these structures is an open issue rather than existing work.

# The record

The exam is a left shoulder radiograph, and the findings were extracted from the synthetic report stored alongside it.[^efl-report]

```json
{
  "$schema": "https://github.com/openimagingdata/imaging-problem-list/schema/exam-problem-list-schema.json",
  "diagnosticReportId": "f2b9b789-cb68-48c1-a09c-a1c34ddef340",
  "patientInfo": {
    "patientIdentifier": "MRN0000001",
    "patientDOB": "1961-01-01"
  },
  "examInfo": {
    "studyIdentifier": "XR_SHOULDER_20210522",
    "studyDateTime": "2021-05-22T10:00:00Z",
    "studyLoincCode": "26158-6",
    "studyDescription": "XR Shoulder - left"
  },
  "findings": [
    {
      "observationId": "acromioclavicular_degenerative_changes_1",
      "findingCode": "OIFM_GMTS_025663",
      "findingDescription": "degenerative joint changes",
      "attributes": [
        {
          "attributeCode": "OIFMA_GMTS_265084",
          "attributeDescription": "presence",
          "attributeValueCode": "OIFMA_GMTS_265084.1",
          "attributeValueDescription": "present"
        }
      ],
      "anatomicLocation": {
        "locationId": "RID42239",
        "locationDisplay": "left acromioclavicular joint"
      },
      "reportText": "Mild degenerative changes of the acromioclavicular joint with joint space narrowing and small osteophytes."
    },
    {
      "observationId": "calcific_tendinopathy_1",
      "findingCode": "OIFM_GMTS_031526",
      "findingDescription": "calcification in a tendon",
      "attributes": [
        {
          "attributeCode": "OIFMA_GMTS_261480",
          "attributeDescription": "presence",
          "attributeValueCode": "OIFMA_GMTS_261480.1",
          "attributeValueDescription": "present"
        }
      ],
      "anatomicLocation": {
        "locationId": "RID41117",
        "locationDisplay": "left supraspinatus tendon"
      },
      "reportText": "Amorphous calcifications are present in the region of the supraspinatus tendon insertion on the greater tuberosity, consistent with calcific tendonitis."
    },
    {
      "observationId": "bone_fracture_clavicle_0",
      "findingCode": "OIFM_OIDM_842151",
      "findingDescription": "clavicle fracture",
      "attributes": [
        {
          "attributeCode": "OIFMA_OIDM_914237",
          "attributeDescription": "presence",
          "attributeValueCode": "OIFMA_OIDM_914237.0",
          "attributeValueDescription": "absent"
        }
      ],
      "anatomicLocation": {
        "locationId": "RID41741",
        "locationDisplay": "left clavicle"
      },
      "reportText": "The humeral head, glenoid, clavicle, and scapula demonstrate normal bone density without fracture or lytic lesion."
    },
    {
      "observationId": "glenohumeral_dislocation_0",
      "findingCode": "OIFM_CDE_000229",
      "findingDescription": "humerus dislocation",
      "attributes": [
        {
          "attributeCode": "OIFMA_CDE_001468",
          "attributeDescription": "presence",
          "attributeValueCode": "OIFMA_CDE_001468.0",
          "attributeValueDescription": "absent"
        }
      ],
      "anatomicLocation": {
        "locationId": "RID42241",
        "locationDisplay": "left glenohumeral joint"
      },
      "reportText": "No dislocation or subluxation."
    },
    {
      "observationId": "soft_tissue_mass_0",
      "findingCode": "OIFM_OIDM_299401",
      "findingDescription": "soft tissue mass",
      "attributes": [
        {
          "attributeCode": "OIFMA_OIDM_818812",
          "attributeDescription": "presence",
          "attributeValueCode": "OIFMA_OIDM_818812.0",
          "attributeValueDescription": "absent"
        }
      ],
      "anatomicLocation": {
        "locationId": "RID39518_RID5824",
        "locationDisplay": "left shoulder"
      },
      "reportText": "The visualized soft tissues are unremarkable on radiograph."
    }
  ]
}
```

# Walkthrough

## Exam envelope

| Field | Value in this record | What it carries |
|---|---|---|
| `diagnosticReportId` | a UUID | the identity of the report this list came from. The [Imaging Problem List](/glossary/imaging-problem-list.md) uses it to point back at the source exam. |
| `patientInfo.patientIdentifier` | `MRN0000001` | the synthetic medical record number that ties this exam to one patient |
| `patientInfo.patientDOB` | `1961-01-01` | synthetic birth date |
| `examInfo.studyIdentifier` | `XR_SHOULDER_20210522` | the exam's own identifier |
| `examInfo.studyDateTime` | `2021-05-22T10:00:00Z` | when the exam happened, which is what orders observations over time |
| `examInfo.studyLoincCode` | `26158-6` | the [exam type](/glossary/exam-type.md), keyed by a curated list of LOINC codes |
| `examInfo.studyDescription` | `XR Shoulder - left` | human-readable exam name |

The repository's own description of the structure is short: an Exam Finding List is "a list of the findings declared as present/absent on that exam", with basic information about the exam keyed by a curated list of LOINC codes.[^ipl-readme] In FHIR terms, the envelope is a **DiagnosticReport** and each finding is an **Observation**.

## One finding

Each entry in `findings` is one [Observation](/glossary/observation.md): one finding type, asserted about one place, on this exam.

| Field | Example value | What it carries |
|---|---|---|
| `observationId` | `bone_fracture_clavicle_0` | unique within this list. The trailing number distinguishes repeated instances of the same finding type, so three kidney stones produce three entries. |
| `findingCode` | `OIFM_OIDM_842151` | the [Open Imaging Finding Model (OIFM)](/glossary/oifm.md) identifier of the [finding model](/glossary/finding-model.md) this observation instantiates |
| `findingDescription` | `clavicle fracture` | the finding model's name, carried along so the record reads without a lookup |
| `attributes` | one entry here | the [attribute](/glossary/attribute.md) values that characterize the finding |
| `anatomicLocation` | `{RID41741, left clavicle}` | the standardized [anatomic location](/glossary/anatomic-location.md), by RadLex identifier. Optional, and omitted when a finding is not anatomically localizable. |
| `reportText` | the sentence from the report | the verbatim span the finding was extracted from, which is the provenance marker |

## Attribute values

An attribute entry is four fields: the attribute's `OIFMA` code, its name, the code of the chosen value, and that value's name. The value code is the attribute code plus a dot and an index, and the index is assigned by position starting at zero. For presence, `.0` is absent and `.1` is present, which is why `OIFMA_OIDM_914237.0` reads as absent and `OIFMA_GMTS_265084.1` reads as present. The identifier scheme is set out in the [finding model schema](/references/finding-model-schema.md).

## Absence is an assertion

Three of these five findings are absent, and that is the point of the structure rather than an artifact of it. The radiologist wrote "no dislocation or subluxation" and "the visualized soft tissues are unremarkable", and each of those statements is an active observation that the finding was looked for and not found. Keeping absences makes the difference between a finding that was never assessed and one that was assessed and ruled out, which is what the [Imaging Problem List example](/references/imaging-problem-list-example.md) turns into a temporal status.

## Contributing organizations in the identifiers

The three-to-four letter segment in the middle of each identifier is the code of the organization that contributed the definition. This trimmed record alone draws on three: `GMTS` for the Gamuts-derived models, `OIDM` for models authored by the project, and `CDE` for models derived from common data elements. The finding codes and attribute codes in one observation always share the same organization code, because an attribute belongs to the model that defines it.

## Repeated finding types and coarse scope

Two of the findings in the full record, which this excerpt trims, use the same finding code `OIFM_GMTS_025663` for degenerative joint changes at two different joints, distinguished only by `anatomicLocation` and by the trailing number on `observationId`. That is the reason the Imaging Problem List groups on finding code and location together rather than on finding code alone.[^ipl-claude] The soft tissue mass entry shows the other end of the scale: its location is `RID39518_RID5824`, the left shoulder as a region rather than a discrete structure, because the report's assertion was about the region.

[^efl-sample]: xr_shoulder_20210522_efl.json, imaging-problem-list dev branch
[^efl-report]: xr_shoulder_20210522.md, the synthetic report the findings were extracted from
[^ipl-claude]: imaging-problem-list domain model notes, dev branch
[^ipl-readme]: imaging-problem-list README, main branch
