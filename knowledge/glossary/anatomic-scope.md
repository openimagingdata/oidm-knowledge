---
type: Glossary Term
title: Anatomic scope
description: The eligible anatomical places, tissue types, or structure types for a definition, stated as a constraint rather than as a location.
tags: [glossary, semantic-foundation, anatomy, next-generation]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: cde-context
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/CONTEXT.md
    title: CDE vocabulary, next-generation working glossary
  - id: overview
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/oifm-overview.md
    title: "Finding Models: Overview, specificity and scope"
  - id: rules
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/anatomic-location-assignment-rules.md
    title: Anatomic location assignment rules, imaging-problem-list dev branch
---

# Anatomic scope

"The eligible anatomical places, tissue types, or structure types for a definition. A plain list matches any one target by default; explicit combinations can require multiple conditions to hold together."[^cde-context] Scope is a constraint on where a definition may be used, not a statement of where a particular finding was seen.

The next-generation vocabulary names two scope families. Tissue-type scope is "exemplified by pulmonary parenchyma, hepatic parenchyma, and subcutaneous fat." Structure-type scope is "exemplified by solid organs, vessels and their artery/vein subtypes, muscles, tendons, and ligaments." Both are collected under an anatomy scope specifier, and how these families connect to the anatomic location hierarchy is recorded as open.[^cde-context]

OIDM's authoring guidance states the same requirement in prose rather than as a typed field: "broad findings should be scoped to assessable anatomy. The scope of a finding model should match what's assessable on a given exam type, not broader." Fracture is too broad, chest wall fracture is appropriately scoped for a chest radiograph, and upper abdominal abnormality is appropriately scoped for chest CT because the upper abdomen is in the field of view.[^overview]

## Synonyms and near-synonyms

- **Scope** unqualified, in finding-model authoring discussions, usually means this.
- **[Anatomic location](/glossary/anatomic-location.md)** is the instance-level assignment; scope is definition-level eligibility.
- **Component-of scope** is a different constraint: which [FindingClasses](/glossary/finding-class.md) a component class may sit inside.
- **Exam-scoped coarse region** is the fallback rule the extraction pipeline applies when a finding has no anatomic noun at all.[^rules]

## Identifier form

None. Scope is expressed as a list of concepts or scope specifiers.

## Where it is used

[Next-generation vocabulary](/semantic-foundation/common-data-elements/next-generation-vocabulary.md), [Why finding models](/semantic-foundation/finding-models/why-finding-models.md), and [Exam types overview](/semantic-foundation/exam-types/overview.md).

## Conflicts

There is no scope field in the OIFM format. Scope exists only as authoring guidance and as reviewer judgment, so it cannot be checked mechanically the way a typed scope specifier could.

[^cde-context]: CDE vocabulary, next-generation working glossary
[^overview]: "Finding Models: Overview"
[^rules]: Anatomic location assignment rules
