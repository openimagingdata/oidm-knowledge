---
type: Data Structure
title: Imaging Problem List
description: The per-patient structure that reorganizes a patient's imaging findings by finding rather than by date, its fields, its grouping key, the temporal status computed over it, and what it is meant to become in FHIR.
tags: [data-structures, imaging-problem-list, anatomic-location, fhir]
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
  - id: ipl-sample
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/sample_data/example2/MRN0000001_ipl.json
    title: MRN0000001_ipl.json, the anatomy-grouped Imaging Problem List sample, dev branch
  - id: ipl-script
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/scripts/generate_ipl_from_efls.py
    title: generate_ipl_from_efls.py, the Imaging Problem List generator, dev branch
  - id: viewer-app
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/viewer/app.js
    title: viewer/app.js, the temporal status derivation, dev branch
  - id: ipl-diagram
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/imaging-problem-list-process.png
    title: imaging-problem-list-process.png, the pipeline diagram in the README
  - id: anat-rules
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/anatomic-location-assignment-rules.md
    title: Anatomic location assignment rules, imaging-problem-list dev branch
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: "Open Imaging Data Model 2026 Status Update, January 2026"
---

# Definition

"In the context of a patient, the list of findings that have been described as present/absent in exams of the patient."[^ipl-main] An [Imaging Problem List](/glossary/imaging-problem-list.md) is the third level of [the hierarchy](/data-structures/hierarchy.md) and the project's signature structure. It takes every [Exam Finding List](/data-structures/exam-finding-list.md) for one patient and re-keys the [observations](/data-structures/observation.md) inside them by finding.

That single change of key is the whole point. The deck states the core query the structure exists to answer: "was finding X present on the most recent study?"[^deck] Against a stack of reports organized by date that question is a search. Against a problem list it is a lookup.

# Fields

| Field | Type | Notes |
|---|---|---|
| `$schema` | URL string | points at `http://example.com/schemas/imaging_problem_list.json`; nothing is published there |
| `patient.id` | string | medical record number |
| `patient.name` | string | display name |
| `patient.dob` | date string | birth date |
| `findings[]` | array | one entry per grouped finding |
| `findings[].id` | string | identity within this list, for example `ipl-finding-116`. This, not the finding code, is the stable key.[^ipl-claude-dev] |
| `findings[].finding_type_code` | `OIFM_[A-Z]{3,4}_[0-9]{6}` | the [OIFM](/glossary/oifm.md) identifier |
| `findings[].finding_type_display` | string | the finding model's display name |
| `findings[].anatomicLocation` | `{locationId, locationDisplay}` | **development branch only**; the second half of the grouping key |
| `findings[].observations[]` | array | every time this finding was documented, oldest first |
| `observations[].report_id` | UUID string | the `diagnosticReportId` of the source Exam Finding List |
| `observations[].observation_id` | string | the `observationId` within that list |
| `observations[].exam_date` | date string | from the source exam's `studyDateTime` |
| `observations[].exam_type_code` | [LOINC](/glossary/loinc.md) code | from the source exam header |
| `observations[].exam_type_display` | string | exam display name |
| `observations[].presence` | string | `present`, `absent`, or `indeterminate` in the sample data, flattened from the source attribute code and value code pair |
| `observations[].anatomicLocation` | `{locationId, locationDisplay}` | **development branch only**; repeats the finding's location |
| `observations[].reportText` | string | the verbatim span, carried through so the timeline reads without fetching the source exams |

Note the field naming: the problem list uses snake_case for its own fields while carrying camelCase forward on the fields copied from the Exam Finding List, so `finding_type_code` and `anatomicLocation` sit in the same object. Two worked entries are in [the Imaging Problem List example](/references/imaging-problem-list-example.md).

# The grouping key

On the stable branch, observations group by finding code alone. On the development branch the key is the pair of finding code and [anatomic location](/glossary/anatomic-location.md) identifier, with the rationale stated in the repository's own domain notes:

> Groups observations by finding type **and** anatomic location (`locationId`) across exams, preserving references to each source report, so one finding code at distinct sites (e.g. ascending vs. abdominal aortic aneurysm) yields separate entries; consumers key on the IPL finding `id`, not `finding_type_code`.[^ipl-claude-dev]

The generator implements it directly, keying on the tuple of finding code and location identifier, with observations that have no location grouping under a null location.[^ipl-script]

The effect on real data is large. The same ten exams for one synthetic patient produce 98 problem list entries when grouped by finding code alone and 123 when grouped by finding code and location.[^ipl-sample] The observation count is unchanged; the grouping is finer.

This is why the documented rule is that consumers key on `id`. A finding code is no longer unique within a list.

# Temporal status

Status is **computed at display time, not stored**. No status field exists in the file. The viewer derives it per finding from the observation list.[^viewer-app]

1. No observations gives **Unknown**.
2. Sort the observations by exam date, most recent first.
3. If the most recent is `present`, every observation is `present`, and there is more than one, the status is **Always**.
4. If the most recent is `present` otherwise, the status is **Current**.
5. If the most recent is not `present` but some earlier observation was, the status is **Resolved**.
6. If no observation was ever `present`, the status is **Never**.

The viewer sections a patient's list under those four headings and offers them as a filter.

Two things follow. **Never is not the same as absent from the list.** A finding with only absent observations is a finding that was looked for on named exams and not found, and the list records that it was looked for. **The scheme has four states, not three.** The stable branch's prose still describes an older three-state model of Present, Resolved, and Not Present or Ruled Out.[^ipl-main-claude] That wording is stale relative to the code on both branches, which computes four. The discrepancy is recorded in [the Imaging Problem List glossary entry](/glossary/imaging-problem-list.md).

# What the structure is for

The deck lists four properties beyond the core query.[^deck]

- **Organized by finding, meaning pathology, rather than by chronology.** The reorganization is the feature.
- **Precision filtering by way of anatomy-embedded definitions.** This is what the grouping-key change on the development branch buys, and what the anatomy-aware viewer renders.
- **Dynamic tracking of appearance, disappearance, and change.** The computed status is the first cut at this; measurement trends over time are not modelled.
- A public demonstration at `imaging-problem-list.pages.dev`.

The uses the deck names across the imaging life cycle, from protocoling to passive screening, are covered under [Imaging Persona](/data-structures/imaging-persona.md), because they draw on context beyond imaging results.

# The pipeline diagram

The README carries `imaging-problem-list-process.png`, a hand-drawn pipeline in three stages.[^ipl-diagram] On the left, Report 1 through Report n feed an **Extractor**, drawn as a neural network and fed from below by a database labelled "Findings (CDE 'stub' defs)". The Extractor emits one Findings List per report. Those feed an **Assembler**, also drawn as a neural network, which emits the Imaging Problem List on the right.

The output panel is the argument. Four finding cards, Pulmonary Nodule, Pulmonary Apical Scarring, Subsegmental Atelectasis, and Pleural Effusion, each list their observations by dated exam. Pulmonary Nodule shows "Chest CT 2020-11-23 (x8)", the multiplicity collapsed into one dated row. Pleural Effusion shows five rows of which four are marked "(absent)", which is the negative-as-data claim drawn out: a finding whose entire history is absence still earns a card.

The Assembler as drawn is a learned component. The implementation is not: `generate_ipl_from_efls.py` is deterministic aggregation.[^ipl-script]

# FHIR

The documented encoding is "**Report** containing a list of **Condition** objects (labeled with the finding identifier), where each Condition object also contains a list of **Observation** objects which document which exams (**DiagnosticReports**) the finding type has been documented on, including the exam date and exam type (LOINC type)."[^ipl-main] One [FHIR Condition](/glossary/fhir-condition.md) per problem list entry, with the observation trail underneath it.

The mapping is documented and implemented nowhere. No Condition resource is produced by any code in the repository. Its container is also called a "Report," which is not a FHIR resource name. See [FHIR mapping](/data-structures/fhir-mapping.md).

# Known limitation

Grouping by exact location identifier is too strict when the same problem is described at different granularity on different exams. The assignment rules state the gap:

> Parent/child or generic-vs-specific pairs for the *same finding code across exams* (e.g. "lung" vs "lower lobe of right lung"; "kidney" vs "left kidney") still produce separate IPL groups. Deciding whether such observations are the same problem or distinct is the **anatomic-compatibility reconciliation** step.[^anat-rules]

That step is named in the anatomic location plan and has not been started. It is the most concrete open problem in the structure. The full precedence, laterality, and specificity rules that produce the locations are in [anatomic location assignment rules](/data-structures/anatomic-location-assignment-rules.md).

# How it is produced

`generate_ipl_from_efls.py` reads a directory of `*_efl.json` files, sorted by filename so the chronology follows, takes the patient block from the first one, groups every finding by the key above, and writes one `ipl.json`.[^ipl-script] It is ordinary Python with no model calls. The rendering side is the [Imaging Problem List viewer](/applications/imaging-problem-list-viewer.md); the sample data it runs on is described in [sample data](/data-structures/sample-data.md).

[^ipl-main]: imaging-problem-list README, main branch
[^ipl-main-claude]: imaging-problem-list domain model notes, main branch
[^ipl-claude-dev]: imaging-problem-list domain model notes, dev branch
[^ipl-sample]: MRN0000001_ipl.json, dev branch
[^ipl-script]: generate_ipl_from_efls.py, dev branch
[^viewer-app]: viewer/app.js, the temporal status derivation, dev branch
[^ipl-diagram]: imaging-problem-list-process.png, the pipeline diagram
[^anat-rules]: Anatomic location assignment rules, dev branch
[^deck]: "Open Imaging Data Model 2026 Status Update", January 2026
