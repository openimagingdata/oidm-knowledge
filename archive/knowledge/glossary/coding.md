---
type: Glossary Term
title: Coding
description: Assigning finding identifiers and anatomic location identifiers to extracted findings, as a job distinct from extraction.
tags: [glossary, applications, extraction]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: coding-design
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/coding-agent-design.md
    title: Coding agent design, imaging-problem-list dev branch
  - id: rules
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/anatomic-location-assignment-rules.md
    title: Anatomic location assignment rules, imaging-problem-list dev branch
  - id: ipl-claude
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/CLAUDE.md
    title: imaging-problem-list architecture notes, dev branch
  - id: mvp
    resource: https://github.com/openimagingdata/IPL-MVP-ExtractionAndLabeling/blob/b06948fa417aeff0a6a4b97729c915b3ce5d5ed4/README.md
    title: IPL-MVP-ExtractionAndLabeling README, embedding-similarity mapping
---

# Coding

Assigning an [OIFM](/glossary/oifm.md) finding identifier and an [anatomic location](/glossary/anatomic-location.md) identifier to a finding that [extraction](/glossary/extraction.md) produced as free text. "Coding assigns OIFM finding codes and anatomic location codes to extracted findings. It is an independent job, fully decoupled from extraction. Extraction output persists without codes; coding is triggered separately and can be re-run with different models or settings."[^coding-design]

The documented pipeline has five phases, two of which call a language model. Index lookup resolves exact and synonym matches for findings and locations without model calls. For unresolved findings, separate finding and location agents each generate two or three diverse search terms in parallel. Batched index search returns candidates. Selector agents choose finding and location codes in parallel, and assembly combines the results with index matches. Each phase degrades independently, and one finding's failure does not block the others.[^coding-design]

Location coding follows its own precedence rules rather than free judgment; see [anatomic location assignment rules](/data-structures/anatomic-location-assignment-rules.md). Codes are resolved by direct lookup rather than semantic search for a named target organ, "to avoid retrieval misses," and "every assigned `locationId` must exist in the ontology," with unrepresented structures left unassigned rather than forced onto a wrong code.[^rules]

## Synonyms and near-synonyms

- **Labelling** and **mapping** name the same step in the earlier MVP pipeline, which used embedding cosine similarity against a small curated model set with a confidence threshold.[^mvp]
- **[Extraction](/glossary/extraction.md)** is the upstream job and is deliberately separate.
- **Enrichment** is a different activity: it adds metadata to finding model definitions, not codes to observations.
- **Index code assignment** means adding ontology codes to a definition, not coding an observation.

## Identifier form

The output identifiers are `OIFM_[A-Z]{3,4}_[0-9]{6}` for the finding and a [RadLex RID](/glossary/radlex-id.md) for the location.

## Where it is used

[Finding and location coding](/applications/finding-and-location-coding.md) and [Report extraction platform](/applications/report-extraction-platform.md).

## Conflicts

Coding assigns a finding code but not [attribute](/glossary/attribute.md) codes. Extracted attributes remain open key-value pairs, so an [Exam Finding List](/glossary/exam-finding-list.md) built from an extraction carries coded findings and locations with uncoded attribute keys, except for presence.

[^coding-design]: Coding agent design
[^rules]: Anatomic location assignment rules
[^ipl-claude]: imaging-problem-list architecture notes
[^mvp]: IPL-MVP-ExtractionAndLabeling README
