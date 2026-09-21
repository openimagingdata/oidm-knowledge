---
type: Glossary Term
title: Exam type
description: The kind of imaging study an exam is, coded with LOINC today and intended to become a first-class OIDM artifact linking modality, technique, and included body parts.
tags: [glossary, semantic-foundation, exam-types]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: ipl-claude
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/CLAUDE.md
    title: imaging-problem-list domain model, data standards, dev branch
  - id: al-site
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/docs/index.markdown
    title: anatomiclocations.org roadmap, exam type companion
  - id: roadmap
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/docs/product-roadmap.md
    title: med-ontology-lookup product roadmap, radiology profile and Playbook
  - id: rules
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/anatomic-location-assignment-rules.md
    title: Anatomic location assignment rules, exam-scoped region fallback
  - id: overview
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/oifm-overview.md
    title: "Finding Models: Overview, scope matched to exam type"
---

# Exam type

The kind of imaging study an exam is: modality, body part, technique, and contrast, taken together. Today OIDM identifies an exam type by a [LOINC](/glossary/loinc.md) code carried on the exam header, for example `72133-2` for CT Abdomen and Pelvis Without Contrast.[^ipl-claude]

Exam type does more work than labelling. It bounds what a finding model should cover: "the scope of a finding model should match what's assessable on a given exam type, not broader."[^overview] It supplies the fallback [body region](/glossary/body-region.md) when a finding names no anatomic structure, and it supplies laterality when the exam itself is sided.[^rules]

The stated goal is a first-class exam-type artifact rather than a bare code. The earliest written form asks for "a companion for exam types based on LOINC/RadLex Playbook exam definitions that specify all included body parts for the exam."[^al-site] The most developed written design sits in the terminology tool's roadmap, which makes the [LOINC/RSNA Radiology Playbook](/glossary/loinc-rsna-radiology-playbook.md) first-class in a default radiology profile and plans Playbook-weighted ranking for orderable queries.[^roadmap]

## Synonyms and near-synonyms

- **Study type**, **procedure**, and **orderable** name the same thing from ordering, performing, and terminology points of view.
- **Exam description** is the free-text label, not the coded type; viewers map long descriptions to short display names.
- **Modality** is one axis of an exam type, not the whole of it.
- **Protocol** is how the exam is acquired, a level below the exam type.

## Identifier form

A LOINC code today. Legacy `RPID` Playbook identifiers are recognized in the planned design but not in current data.

## Where it is used

[Exam types overview](/semantic-foundation/exam-types/overview.md), [Existing building blocks](/semantic-foundation/exam-types/existing-building-blocks.md), and [Exam Finding List](/data-structures/exam-finding-list.md).

## Conflicts

No exam-type artifact exists. There is no published curated LOINC list, no exam-to-body-parts mapping, and no code that parses modality or body-part axes, even though three separate documents across three repositories describe the same goal. The area is documented as goals plus existing building blocks; see [Exam types](/roadmap/exam-types.md).

[^ipl-claude]: imaging-problem-list domain model, dev branch
[^al-site]: anatomiclocations.org roadmap
[^roadmap]: med-ontology-lookup product roadmap
[^rules]: Anatomic location assignment rules
[^overview]: "Finding Models: Overview"
