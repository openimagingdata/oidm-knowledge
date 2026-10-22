---
type: Glossary Term
title: LOINC/RSNA Radiology Playbook
description: The jointly governed radiology part of LOINC that names imaging orderables along modality, anatomy, and technique axes.
tags: [glossary, semantic-foundation, terminologies, exam-types]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: playbook
    resource: https://loinc.org/committee/radiology/
    title: LOINC/RSNA Radiology Playbook, Regenstrief Institute
  - id: roadmap
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/docs/product-roadmap.md
    title: med-ontology-lookup product roadmap, Playbook as first-class in the radiology profile
  - id: current-understanding
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/00-current-understanding.md
    title: Current understanding, next-gen-2026 branch, Playbook governance
  - id: al-site
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/docs/index.markdown
    title: anatomiclocations.org roadmap, exam type companion
---

# LOINC/RSNA Radiology Playbook

The radiology portion of [LOINC](/glossary/loinc.md), developed jointly by the Regenstrief Institute and the RSNA, which names imaging orderables along axes such as modality, anatomy, and technique.[^playbook] It is "actively governed, and freely licensed for commercial and non-commercial use. The Playbook ships twice yearly under joint Regenstrief/RSNA governance, but it is a separate artifact" from [RadLex](/glossary/radlex.md).[^current-understanding]

In OIDM the Playbook is the stated basis for [exam types](/glossary/exam-type.md), and it appears only in design documents. The terminology roadmap makes it "first-class in `radiology`," with planned detection of LOINC codes and legacy `RPID` Playbook identifiers. Orderable queries would favor Playbook terms, and finding and anatomy queries would favor RadLex. Crosswalk provenance would record Playbook, RPID, and RadLex anatomy correspondences.[^roadmap] The earliest statement of the idea is older still: the curated anatomic location set's roadmap calls for "a companion for exam types based on LOINC/RadLex Playbook exam definitions that specify all included body parts for the exam."[^al-site]

## Synonyms and near-synonyms

- **Playbook** and **RSNA Playbook** are the short forms.
- **RadLex Playbook** is the historical name; its `RPID` identifiers persist as legacy codes.
- **[LOINC](/glossary/loinc.md)** is the containing system; the Playbook is the radiology subset with its own governance.
- **[Exam type](/glossary/exam-type.md)** is the OIDM concept the Playbook is meant to supply identifiers for.

## Identifier form

LOINC codes for current content; `RPID` followed by digits for legacy Playbook identifiers.

## Where it is used

[Exam types overview](/semantic-foundation/exam-types/overview.md), [Existing building blocks](/semantic-foundation/exam-types/existing-building-blocks.md), and [Exam types](/roadmap/exam-types.md).

## Conflicts

Nothing in OIDM consumes the Playbook today. Playbook support is planned in the terminology tool but unimplemented, no modality or body-part axis parsing exists, and RadLex merely cites "Playbook" as free-text provenance on individual concepts rather than linking to it.[^current-understanding]

[^playbook]: LOINC/RSNA Radiology Playbook
[^roadmap]: med-ontology-lookup product roadmap
[^current-understanding]: Current understanding, next-gen-2026 branch
[^al-site]: anatomiclocations.org roadmap
