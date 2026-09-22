---
type: Glossary Term
title: Exam Finding List
description: All findings declared present or absent on one imaging exam, in one queryable structure keyed to the exam and the report.
tags: [glossary, data-structures, ipl]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: ipl-readme
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/README.md
    title: imaging-problem-list README, Exam Finding List definition
  - id: ipl-claude
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/CLAUDE.md
    title: imaging-problem-list domain model, dev branch
  - id: efl-sample
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/sample_data/example1/sample_efl.json
    title: Exam Finding List sample data
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026
---

# Exam Finding List

"In the context of an imaging exam, a list of the findings declared as present/absent on that exam."[^ipl-readme] It is the second level of the OIDM data structure hierarchy, grouping every [observation](/glossary/observation.md) from one exam under that exam's identity.

The structure carries a `diagnosticReportId`, `patientInfo`, an `examInfo` block holding the study identifier, date and time, [LOINC](/glossary/loinc.md) code and description, and a `findings` array. Each finding carries an `observationId`, a `findingCode` in `OIFM_XXXX_######` form with its description, an `attributes` array of [attribute](/glossary/attribute.md) code, value code, and display text, an optional `anatomicLocation` of `locationId` and `locationDisplay`, and an optional verbatim `reportText`.[^ipl-claude][^efl-sample]

Two properties are stated as requirements rather than conveniences. The exam header must be keyed by a curated list of LOINC codes, and "the same finding type may be declared present multiple times; each time is a separate entry."[^ipl-readme] The deck adds that an Exam Finding List can be "sourced from dictation, AI tools, interpretation-time interfaces," so each observation should carry a [provenance](/glossary/provenance.md) marker.[^deck]

## Synonyms and near-synonyms

- **EFL** is the abbreviation used throughout the source repository.
- **[FHIR DiagnosticReport](/glossary/fhir-diagnostic-report.md)** is its documented interchange encoding.
- **Report** is the narrative document; the Exam Finding List is the structured result derived from or produced alongside it.
- **[Imaging Problem List](/glossary/imaging-problem-list.md)** is the patient-level aggregation of many of these.

## Identifier form

None of its own beyond `diagnosticReportId`, a UUID string in the sample data.

## Where it is used

[Hierarchy](/data-structures/hierarchy.md), [Exam Finding List](/data-structures/exam-finding-list.md), and [Exam Finding List example](/references/exam-finding-list-example.md).

## Conflicts

The README abbreviates Imaging Problem List as "IFL" in one heading, a typographical error rather than a second name. The `anatomicLocation` field exists only on the development branch, so data produced against the stable specification will not carry it. No JSON Schema is published; the schema URL referenced in the sample files does not resolve.

[^ipl-readme]: imaging-problem-list README
[^ipl-claude]: imaging-problem-list domain model, dev branch
[^efl-sample]: Exam Finding List sample data
[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
