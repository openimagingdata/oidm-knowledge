---
type: Reference
title: Sample data
description: Synthetic exam and problem list samples, branch differences, viewer bundles, and generation scripts.
tags: [data-structures, sample-data, reference, synthetic]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: ipl-main-claude
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/CLAUDE.md
    title: imaging-problem-list domain model notes, main branch, which documents the data layout
  - id: sample-main
    resource: https://github.com/openimagingdata/imaging-problem-list/tree/06f64a7893b444b761dc069ed86140a081195eac/sample_data
    title: sample_data on the main branch
  - id: sample-dev
    resource: https://github.com/openimagingdata/imaging-problem-list/tree/36fa30c7383bf687d7bc17815282a93e123a56cb/sample_data
    title: sample_data on the dev branch
  - id: ipl-sample
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/sample_data/example2/MRN0000001_ipl.json
    title: MRN0000001_ipl.json, the anatomy-grouped Imaging Problem List, dev branch
  - id: excel-script
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/scripts/generate_efl_from_excel.py
    title: generate_efl_from_excel.py
  - id: ipl-script
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/scripts/generate_ipl_from_efls.py
    title: generate_ipl_from_efls.py
  - id: enrich-script
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/scripts/enrich_efl_anatomy.py
    title: enrich_efl_anatomy.py, the anatomic location enrichment pass
  - id: viewer2-script
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/scripts/build_viewer_v2_data.py
    title: build_viewer_v2_data.py, the second-generation viewer data bundle builder
---

# All of it is synthetic

Every patient, identifier, date, and line of report text in this data set is written test data. The names, medical record numbers, and birth dates do not belong to real people, and the reports were authored for the project. Counts were read at `06f64a7` on `main` and `36fa30c` on `dev`.

# The three sample sets

| Set | Patients | Contents | Purpose |
|---|---|---|---|
| `example1` | one, Jane Smith, `MRN0000002`, born 1985-06-15 | two Exam Finding Lists with 6 and 7 findings, one Imaging Problem List with 10 entries, and the two source FHIR DiagnosticReports they were derived from | shows the transformation end to end, including the FHIR input |
| `example2` | one, John Doe, `MRN0000001`, born 1961-01-01 | ten exams, ten Exam Finding Lists, ten source reports in markdown, one Imaging Problem List, and a working spreadsheet | the main longitudinal data set |
| `example3` (development branch only) | none, unattributed reports | 31 plain-text radiology reports | extraction input for the batch pipeline and evaluation harness, not Exam Finding Lists |

## example2 in detail

Ten exams over four and a half years, from 2021-05-22 to 2025-10-07, across seven distinct [LOINC](/glossary/loinc.md) [exam types](/glossary/exam-type.md).

| Date | Exam | LOINC |
|---|---|---|
| 2021-05-22 | XR Shoulder, left | `26158-6` |
| 2021-06-14 | XR Chest | `30745-4` |
| 2021-08-26 | CT Abdomen and Pelvis WO contrast | `36952-0` |
| 2022-02-08 | US Abdomen | `24558-9` |
| 2022-03-15 | XR Chest | `30745-4` |
| 2022-09-22 | CT Chest WO contrast | `29252-4` |
| 2022-11-03 | CT Abdomen and Pelvis W contrast IV | `36813-4` |
| 2023-01-18 | CT Abdomen and Pelvis W contrast IV | `36813-4` |
| 2023-01-25 | MR Brain WO and W contrast IV | `24587-8` |
| 2025-10-07 | CT Abdomen and Pelvis WO contrast | `36952-0` |

Findings per exam range from 9 on the shoulder radiograph to 48 on the January 2023 abdominal computed tomography. The [presence](/glossary/presence.md) values that occur are `present`, `absent`, and `indeterminate`.

# What the branches differ on

The branches contain the same exams and nearly the same findings. The development branch adds anatomic enrichment and regroups findings.

| Measure | `main` | `dev` |
|---|---|---|
| Exam Finding Lists in `example2` | 10 | 10 |
| Total observations across them | 275 | 276 |
| Observations carrying an `anatomicLocation` | 0 | 274 |
| Entries in the `example2` Imaging Problem List | 98 | 123 |
| Observations in that problem list | 275 | 276 |

Two observations in the brain magnetic resonance study lack locations because the ontology has no matching structures. Assignment rules leave them unassigned. Grouping by finding code and location instead of code alone increases the problem list from 98 to 123 entries. See [Imaging Problem List](/data-structures/imaging-problem-list.md).

# File layout

`sample_data/` follows a flat naming convention, with one Exam Finding List per exam named after the exam and date.

```
sample_data/
  example1/
    sample_efl.json          CT abdomen and pelvis, 6 findings
    chest_ct_efl.json        CT chest, 7 findings
    sample_ipl.json          the two aggregated, 10 entries
    powerscribe-fhir.json    the source FHIR DiagnosticReport for the first
    chest-ct-fhir.json       the source FHIR DiagnosticReport for the second
  example2/
    xr_shoulder_20210522.md          the synthetic report
    xr_shoulder_20210522_efl.json    its Exam Finding List
    ... eight more pairs ...
    MRN0000001_ipl.json              all ten aggregated
    findings_with_oifm_ids.xlsx      the working spreadsheet
  example3/                          31 .txt reports, dev branch only
```

The repository notes document the viewer's nested layout.[^ipl-main-claude]

```
viewer/data/
  patients.json                            manifest of all patients
  patients/<patient-id>/
    patient.json                           demographics and exam count
    ipl.json                               the Imaging Problem List
    exams/<report-id>/
      efl.json                             the Exam Finding List
      report.txt                           raw report text
  exam_type_mappings.json                  short display names for exam types
  finding_region_mappings.json             98 finding-to-body-region entries
```

The bundle covers `patient-mrn0000001` with 10 exams and 98 problem list entries, and `patient-mrn0000002` with 2 exams and 10 entries. It was not re-enriched on either branch. The deployed first-generation [viewer](/applications/imaging-problem-list-viewer.md) therefore shows the 98-entry, location-free list.

The second-generation viewer has its own bundle under `viewer_v2/public/data/`, built from `sample_data/example2`, carrying the 123-entry anatomy-grouped list for the one patient, with reports as markdown rather than text and extra files for the anatomy index, anatomy clusters, and finding display information. Its manifest is stamped `viewer-v2-data.1` and records its own source paths and warnings.

## The spreadsheet

`findings_with_oifm_ids.xlsx` is the working sheet for `example2`, with one row per finding per exam. Its columns are Exam Date, Exam Type, Exam Code, Finding, OIDM Finding Model Name, OIDM FMID, Presence OIFMA_ID, Present/Absent, and Text.[^excel-script] It records where the [finding model](/glossary/finding-model.md) and [attribute](/glossary/attribute.md) identifiers were assigned by hand, which is why it is worth keeping alongside the generated JSON.

# Regenerating

Four scripts produce the data, in this order.

| Script | What it does |
|---|---|
| `generate_efl_from_excel.py` | reads the spreadsheet, groups rows by exam, writes one `*_efl.json` per exam with a fresh UUID `diagnosticReportId`[^excel-script] |
| `enrich_efl_anatomy.py` | runs each finding through the production coding pipeline to attach an `anatomicLocation`, and writes a review CSV of every location decision with candidates and unresolved reasons. The pass is additive and idempotent: re-running recomputes and overwrites.[^enrich-script] |
| `generate_ipl_from_efls.py` | reads a directory of `*_efl.json` files sorted by filename, groups by finding code and location identifier, writes one `ipl.json`[^ipl-script] |
| `build_viewer_v2_data.py` | builds the static JSON bundle the second-generation viewer serves[^viewer2-script] |

Only enrichment calls a language model. The other three scripts are deterministic. See the repository for commands.

[^ipl-main-claude]: imaging-problem-list domain model notes, main branch
[^excel-script]: generate_efl_from_excel.py
[^enrich-script]: enrich_efl_anatomy.py
[^ipl-script]: generate_ipl_from_efls.py
[^viewer2-script]: build_viewer_v2_data.py
