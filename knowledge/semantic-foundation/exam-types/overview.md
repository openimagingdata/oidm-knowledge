---
type: Concept
title: Exam types
description: What an exam type is meant to become in OIDM, the goals stated for it since 2022, what the LOINC/RSNA Radiology Playbook actually is, and the three places exam type codes do work today.
tags: [semantic-foundation, exam-types, loinc, playbook, anatomy]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:30:00Z }
sources:
  - id: plan
    resource: scope:grilling-session-2026-09-20
    title: Exam type goals stated by the project lead in the 2026-09-20 planning interview, recorded in the knowledgebase build plan
  - id: al-site
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/docs/index.markdown
    title: anatomiclocations.org site homepage, roadmap section
  - id: site-structure
    resource: https://www.openimagingdata.org/data-model-structure-and-function/
    title: "Data Model: Structure and Function, openimagingdata.org, 2024-01-25"
  - id: current-understanding
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/00-current-understanding.md
    title: Current understanding of the next-generation vocabulary work, ACR-RSNA-CDEs next-gen-2026 branch
  - id: molu-roadmap
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/docs/product-roadmap.md
    title: med-ontology-lookup product roadmap, domain profiles and the Playbook section
  - id: ipl-readme
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/README.md
    title: imaging-problem-list README, the Exam Finding List specification
  - id: ipl-claude
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/CLAUDE.md
    title: imaging-problem-list domain model and data standards, dev branch
  - id: ipl-rules
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/anatomic-location-assignment-rules.md
    title: Anatomic location assignment rules, imaging-problem-list dev branch
  - id: viewer-map
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/viewer/data/exam_type_mappings.json
    title: Viewer exam type display mapping table, imaging-problem-list dev branch
  - id: oifm-overview
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/oifm-overview.md
    title: "Finding Models: Overview, ACR-RSNA-CDEs next-gen-2026 branch"
---

# Greenfield

[Exam types](/glossary/exam-type.md) are the one part of the OIDM semantic foundation with no artifact behind them. There is no exam type registry, no curated code list, no exam-to-body-part mapping, and no code anywhere in the OIDM repositories that parses an exam name into modality and anatomy axes. What exists is a goal that has been written down three times across four years, a short list of building blocks that a future exam type layer could stand on, and three working places where a bare [LOINC](/glossary/loinc.md) code already does real work.

This document states the goals as goals and the facts as facts. It proposes nothing. The building blocks are catalogued separately in [existing building blocks](/semantic-foundation/exam-types/existing-building-blocks.md), and the area's direction is tracked in [the exam types roadmap](/roadmap/exam-types.md).

# The goal as the project lead states it

In the 2026-09-20 planning interview that produced [the knowledgebase build plan](/plans/2026-09-20-knowledgebase-build-plan.md), the project lead described the intended exam type work in three parts.[^plan]

1. **Wrapper tooling around an existing knowledge graph.** The graph is the one represented by the [LOINC/RSNA Radiology Playbook](/glossary/loinc-rsna-radiology-playbook.md) together with [RadLex](/glossary/radlex.md), rather than a new vocabulary built from scratch.
2. **A set of preferred high-level entries.** Names at the granularity clinicians and systems actually use, such as CT Chest, MRI Brain, and X-ray Knee, marked as the preferred entry among the many Playbook codes that describe variants of the same study.
3. **Tight coupling to [anatomic locations](/glossary/anatomic-location.md).** Each exam type would carry typed edges to the structures it covers, distinguishing anatomy that is always included, which may be expressed as a hierarchy rather than a flat list, anatomy that is usually included, and anatomy that is possibly included and must be checked.

The third part is what makes the artifact more than a code list. It answers the question a report reader and an extraction pipeline both need answered: given this study, what could have been assessed?

# The same goal, stated earlier

The idea predates the current work by several years, in nearly the same words.

The curated anatomic location set's roadmap lists, among content tasks, "work on a companion for exam types based on LOINC/RadLex Playbook exam definitions that specify all *included* body parts for the exam."[^al-site] The source spells LOINC as "LOIC" and RadLex as "Radlex"; the intent is unambiguous from the surrounding list. That page has not changed since January 2023.

The site post "Data Model: Structure and Function" of 2024-01-25 names two utility libraries alongside the core model: anatomic locations for standardized body part terminology, and an exam type library based on the LOINC and RSNA Playbook, linked to anatomic locations.[^site-structure] Neither statement has produced an artifact. The anatomic location library was built; the exam type library was not. See [site articles](/history/site-articles.md) for the post in context.

# What the Playbook actually is

The Playbook is a real, governed, external artifact, which is why every statement of the goal reaches for it rather than proposing a new vocabulary.

It is the radiology portion of LOINC, developed jointly by the Regenstrief Institute and the RSNA, naming imaging orderables along axes such as modality, anatomy, and technique. The next-generation vocabulary analysis records it as "actively governed, and freely licensed for commercial and non-commercial use," shipping "twice yearly under joint Regenstrief/RSNA governance," and stresses that it "is a separate artifact" from RadLex itself.[^current-understanding] RadLex cites the Playbook as free-text provenance on individual concepts, but carries no link to it.

Two consequences matter for anyone reading exam type material in these repositories. Current Playbook content is identified by ordinary LOINC codes, not by a separate scheme: "RadLex Playbook (RPID) was folded into LOINC; new procedure codes are LOINC format, not new RPIDs."[^molu-roadmap] Legacy `RPID` identifiers therefore appear only as historical codes that a crosswalk would need to recognize. And the division of labour between the two RSNA-associated vocabularies is explicit: radiology "orderables live in the LOINC/RSNA Radiology Playbook, while findings, anatomy, and report language live in RadLex."[^molu-roadmap]

# How exam types are used today

Three uses exist now. All three run on a bare LOINC code with no exam type object behind it.

**As the exam header of an [Exam Finding List](/glossary/exam-finding-list.md).** The specification requires that the structure "must also have basic information (keyed by a curated list of LOINC codes) about what exam this is."[^ipl-readme] In the data this is `examInfo.studyLoincCode` beside `studyIdentifier`, `studyDateTime`, and a free-text `studyDescription`; the domain notes give `72133-2` for CT Abdomen and Pelvis Without Contrast as the worked example.[^ipl-claude] The [Imaging Problem List](/glossary/imaging-problem-list.md) carries the same pair forward on every observation as `exam_type_code` and `exam_type_display`, which is how a finding's time course is labelled by study. The curated list of LOINC codes that the specification refers to has never been published.

**As the fallback [body region](/glossary/body-region.md) for a finding with no anatomy.** The anatomic location assignment rules used by the extraction and coding platform put the exam at the bottom of a three-step precedence ladder. Explicit anatomy in the report text or section context wins; otherwise the finding's own target organ; otherwise, for findings with no anatomic noun at all such as "soft tissue mass" or "generalized osteoporosis," the rules "fall back to the exam-scoped coarse region (thorax, abdomen, head, ...), sided only if the exam is sided."[^ipl-rules] The exam also supplies [laterality](/glossary/laterality.md) under a stated source priority of explicit text side, then sided-exam side, then generic, so that a left shoulder radiograph sides its findings while an abdominal CT never introduces a side. The rules carry a small exam-to-region table of RadLex identifiers, reproduced in [existing building blocks](/semantic-foundation/exam-types/existing-building-blocks.md).

**As a display label.** The viewer shortens long exam descriptions for its timeline through a lookup table, turning "MR Brain WO and W contrast IV" into "MR Brain w/wo."[^viewer-map] The table is keyed by the description string, not by the LOINC code.

# Exam type as the boundary of a finding model's scope

Exam types also bound the semantic foundation's other axis. The finding model overview states the rule directly: "the scope of a finding model should match what's assessable on a given exam type, not broader." Its examples are that "fracture" is too broad because it spans the whole body, "chest wall fracture" is appropriately scoped to what is visible on a chest radiograph, and "upper abdominal abnormality" is appropriately scoped for chest CT because the upper abdomen is in the field of view.[^oifm-overview] The full passage is preserved in [the finding model overview extract](/references/oifm-overview-extract.md).

That rule is applied today by judgment. Nothing checks a [finding model](/glossary/finding-model.md)'s scope against a coded exam type, because no artifact exists to check it against.

[^plan]: Exam type goals stated by the project lead in the 2026-09-20 planning interview
[^al-site]: anatomiclocations.org roadmap
[^site-structure]: "Data Model: Structure and Function", 2024-01-25
[^current-understanding]: Current understanding, ACR-RSNA-CDEs next-gen-2026
[^molu-roadmap]: med-ontology-lookup product roadmap
[^ipl-readme]: imaging-problem-list README, main branch
[^ipl-claude]: imaging-problem-list domain model, dev branch
[^ipl-rules]: Anatomic location assignment rules, imaging-problem-list dev branch
[^viewer-map]: Viewer exam type display mapping table
[^oifm-overview]: "Finding Models: Overview", ACR-RSNA-CDEs next-gen-2026
