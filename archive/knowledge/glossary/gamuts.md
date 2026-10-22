---
type: Glossary Term
title: Gamuts
description: The Radiology Gamuts Ontology, source of the largest single block of finding model definitions and of the GMTS organization code.
tags: [glossary, semantic-foundation, terminologies, content]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: gamuts
    resource: https://gamuts.net/
    title: Radiology Gamuts Ontology
  - id: orgs
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/data/base_organizations.jsonl
    title: Base organization registry in the findingmodel package
  - id: claude-md
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/CLAUDE.md
    title: findingmodels repository conventions, common ontologies
  - id: cleanup
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/docs/plans/definition_cleanup.md
    title: Definition cleanup plan, findingmodels repository
---

# Gamuts

The Radiology Gamuts Ontology, a published ontology of radiologic differential diagnosis lists, at `gamuts.net`.[^gamuts] OIDM uses it as an [index code](/glossary/index-code.md) system listed alongside SNOMED and RadLex as one of the common ontologies,[^claude-md] and it is a registered contributing organization whose [organization code](/glossary/oidm-organization-code.md) is `GMTS`.[^orgs]

Gamuts is the single largest source of finding model content. Of the 2,382 definitions published in the corpus, 1,933 carry an `OIFM_GMTS_` identifier, credited to the Radiology Gamuts Ontology as the contributing organization. They were produced by a script that scrapes gamut pages, structures the terms with a language model, and emits them for conversion into definitions.

## Synonyms and near-synonyms

- **Radiology Gamuts Ontology** is the full name; **gamut** alone means one differential list.
- **`GMTS`** is the organization code and the middle segment of the identifiers.
- **`GAMUTS`** is the `system` string when a gamut concept is cited as an index code.
- **[Finding taxonomy](/glossary/finding-taxonomy.md)** is the newer content source expected to supersede much of this material.

## Identifier form

Finding models derived from this source carry `OIFM_GMTS_######`, for example `OIFM_GMTS_016552` for urinary tract calculus.

## Where it is used

[Content catalog](/semantic-foundation/finding-models/content-catalog.md), [Finding model content direction](/roadmap/finding-model-content-direction.md), and [Ontologies used](/semantic-foundation/terminologies/ontologies-used.md).

## Conflicts

A gamut is a differential diagnosis list, so Gamuts-derived definitions carry diagnoses where OIDM's authoring guidance would sometimes want an observation. The open definition cleanup plan lists "gamuts reclassification" as a step that "needs design discussion," the only step without an agreed approach.[^cleanup] The content roadmap expects the MGB exam-oriented sub-taxonomies to replace many of these definitions.

[^gamuts]: Radiology Gamuts Ontology
[^orgs]: Base organization registry
[^claude-md]: findingmodels repository conventions
[^cleanup]: Definition cleanup plan
