---
type: Glossary Term
title: Imaging Problem List
description: A patient's imaging findings organized by finding rather than by date, each carrying the observations that support it across exams.
tags: [glossary, data-structures, ipl]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: ipl-readme
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/README.md
    title: imaging-problem-list README, Imaging Problem List definition
  - id: ipl-claude-dev
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/CLAUDE.md
    title: imaging-problem-list domain model, dev branch, grouping key
  - id: ipl-claude-main
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/CLAUDE.md
    title: imaging-problem-list domain model, main branch, temporal status
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026
---

# Imaging Problem List

"In the context of a patient, the list of findings that have been described as present/absent in exams of the patient."[^ipl-readme] It is the third level of the OIDM hierarchy and the project's signature structure: the reorganization of a patient's imaging history by finding rather than by chronology.

Each entry groups the [observations](/glossary/observation.md) of one finding across exams, each observation retaining its source report identifier, exam date, exam type, and presence. The structure it answers is a query: the deck gives the core question as "was finding X present on most recent study?" and lists dynamic tracking of appearance, disappearance, and change as the payoff.[^deck]

Grouping key and temporal status are the two things a consumer must get right. On the development branch, observations group by finding code **and** [anatomic location](/glossary/anatomic-location.md), "so one finding code at distinct sites, for example ascending versus abdominal aortic aneurysm, yields separate entries; consumers key on the IPL finding `id`, not `finding_type_code`."[^ipl-claude-dev] Temporal status is computed from the observation list, not stored.

## Synonyms and near-synonyms

- **IPL** is the abbreviation used throughout the sources.
- **Problem list** in the electronic medical record sense is the clinical analogue this is named after, but it is not the same list.
- **[Imaging Persona](/glossary/imaging-persona.md)** is the next level up, adding clinical context around this.
- **[FHIR Condition](/glossary/fhir-condition.md)** is what the documented mapping uses for each entry.

## Identifier form

Each entry carries an `id` local to the list. That `id`, not the finding code, is the stable key.

## Where it is used

[Hierarchy](/data-structures/hierarchy.md), [Imaging Problem List](/data-structures/imaging-problem-list.md), and [Imaging Problem List viewer](/applications/imaging-problem-list-viewer.md).

## Conflicts

Two documented disagreements. The grouping key differs by branch: the stable specification groups by finding code alone, the development branch by finding code and location.[^ipl-claude-dev] And the temporal status model differs between prose and code: the stable branch's documentation describes three states, present, resolved, and not present or ruled out,[^ipl-claude-main] while the viewer computes four, current, always, resolved, and never. A further known limitation is that generic and specific locations for the same finding code still produce separate entries, which an anatomic-compatibility reconciliation step is meant to address and which has not been started.

[^ipl-readme]: imaging-problem-list README
[^ipl-claude-dev]: imaging-problem-list domain model, dev branch
[^ipl-claude-main]: imaging-problem-list domain model, main branch
[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
