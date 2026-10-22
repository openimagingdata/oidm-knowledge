---
type: Glossary Term
title: FindingClass
description: The next-generation CDE vocabulary's node type for a finding definition, separated from diagnosis and carrying bindings to shared elements.
tags: [glossary, semantic-foundation, cde, next-generation]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: cde-context
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/CONTEXT.md
    title: CDE vocabulary, next-generation working glossary
  - id: idr
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md
    title: IHE IDR Phase II extract for the CDE vocabulary
  - id: wg-call
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/working-group-call-2026-08-20-extract.md
    title: Working group call extract, 20 August 2026
---

# FindingClass

The next-generation CDE vocabulary's node type for a finding definition: the counterpart of a [CDE set](/glossary/cde-set.md) or an OIDM [finding model](/glossary/finding-model.md) in a graph model. A FindingClass is described by ordinary [DataElements](/glossary/data-element.md) reached through [element bindings](/glossary/element-binding.md), sits in an is-a taxonomy of subtypes, and carries [standard clinical metadata](/glossary/tag.md): "the seven facts on a class: modality, body region, subspecialty, sex, age, time course, and etiology."[^cde-context]

Two scoping mechanisms are defined on classes. [Anatomic scope](/glossary/anatomic-scope.md) states the eligible anatomical places, tissue types, or structure types for the definition. Component-of scope states "the finding classes a component class belongs inside, stated on the component class"; a class with a component-of scope "is never reported on its own," and component classes are specific to a lesion family.[^cde-context]

The separation of Diagnosis from Finding was agreed on a working-group call as a structural decision, making the finding-to-diagnosis link an explicit relationship rather than a blurred single node type.[^wg-call]

## Synonyms and near-synonyms

- **[Finding model](/glossary/finding-model.md)** is the OIDM artifact at the same granularity, with attributes owned rather than bound.
- **[CDE set](/glossary/cde-set.md)** is the currently published counterpart.
- **Diagnosis** is a separate node type in this vocabulary, not a kind of FindingClass.
- **[AssessmentScheme](/glossary/assessment-scheme.md)** is described as "analogous to a FindingClass with its descriptors" but is its own node type.[^cde-context]
- In IHE IDR the same content lands on `bodyStructure.includedStructure.morphology` and on the root `Observation.code` of a finding set.[^idr]

## Identifier form

Working identifiers in the alpha implementation take the form `FC-######`, for example `FC-000005` for pulmonary nodule. These are prototype identifiers, not a published scheme.

## Where it is used

[Next-generation vocabulary](/semantic-foundation/common-data-elements/next-generation-vocabulary.md) and [Finding model format evolution](/roadmap/finding-model-format-evolution.md).

## Conflicts

IHE IDR uses "finding" for the presence-or-absence determination rather than for the named entity, and routes positive clinical findings to [FHIR Condition](/glossary/fhir-condition.md) while negative ones become Observations. The next-generation working default encodes every radiology report assertion, including diagnoses, as an Observation. The notes list this difference for discussion with IHE.[^idr]

[^cde-context]: CDE vocabulary, next-generation working glossary
[^idr]: IHE IDR Phase II extract
[^wg-call]: Working group call extract, 20 August 2026
