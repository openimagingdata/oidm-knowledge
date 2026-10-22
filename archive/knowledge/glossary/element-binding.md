---
type: Glossary Term
title: Element binding
description: The relationship in the next-generation CDE vocabulary that connects a definition to a DataElement it uses, optionally restricting the values in that use.
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
  - id: fm-py
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/finding_model.py
    title: Attribute ownership in FindingModelFull
---

# Element binding

"A relationship connecting a definition to a DataElement it uses. A FindingClass's binding may restrict that use to a subset of the element's permissible values without changing the shared element or its other bindings."[^cde-context]

The binding is what makes element reuse safe. One severity element can serve many [FindingClasses](/glossary/finding-class.md). A binding can narrow permissible values, set [selection cardinality](/glossary/data-element.md), and record modality applicability. The descriptor's intrinsic modality limit "is distinct from its binding-specific applicability and is not an overridable default."[^cde-context]

An [AnatomicLocation](/glossary/anatomic-location.md) can also bind directly to DataElements and Measurements "describing that anatomy without requiring a FindingClass," so normal anatomy can have properties without a finding.[^cde-context] IHE IDR already supports that shape, encoding an observation whose target is an anatomic entity with a property as its code.[^idr]

## Synonyms and near-synonyms

- **`HAS_ELEMENT`** is the edge name used in the working definition graph.
- **Binding** alone usually means this, but "value binding" and "terminology binding" mean something different in FHIR.
- OIFM has no equivalent. An [attribute](/glossary/attribute.md) is a member of exactly one [finding model](/glossary/finding-model.md) and cannot be shared or restricted.[^fm-py]

## Identifier form

None published. Edges in the prototype graph carry properties such as modality, narrowing, exclusivity, and rank.

## Where it is used

[Next-generation vocabulary](/semantic-foundation/common-data-elements/next-generation-vocabulary.md) and [Finding model format evolution](/roadmap/finding-model-format-evolution.md).

## Conflicts

IHE IDR expresses the same relationship as `Observation.hasMember` on a finding set and notes that those edges are untyped, so a report edge that cites which vocabulary relationship it expresses would need a FHIR extension.[^idr]

[^cde-context]: CDE vocabulary, next-generation working glossary
[^idr]: IHE IDR Phase II extract
[^fm-py]: Attribute ownership in FindingModelFull
