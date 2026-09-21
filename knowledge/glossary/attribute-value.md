---
type: Glossary Term
title: Attribute value
description: One permissible option of a choice attribute, carrying its own dot-suffixed value code and optional ontology codes.
tags: [glossary, semantic-foundation, finding-models]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: fm-py
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/finding_model.py
    title: ChoiceValue, ChoiceValueIded, and the value-code generator
  - id: efl-sample
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/sample_data/example1/sample_efl.json
    title: Exam Finding List sample using attribute value codes
  - id: cde-context
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/CONTEXT.md
    title: CDE vocabulary, next-generation working glossary
---

# Attribute value

One permissible option of a choice [attribute](/glossary/attribute.md): "a value that a radiologist might choose for a choice attribute. For example, the severity of a finding might be severe, or the shape of a finding might be oval."[^fm-py] A value has a `name`, an optional `description`, optional [index codes](/glossary/index-code.md), and a `value_code`.

Value codes are generated, never hand-written. The library appends a dot and the value's zero-based position in the list to the owning attribute's identifier, so the first listed value gets `.0`, the second `.1`, and so on.[^fm-py] Position therefore carries meaning: the same dot suffix means different things in two models that list their values in a different order. See [presence](/glossary/presence.md) for the case where this matters most.

A numeric attribute has no attribute values. Its instance data is a number constrained by `minimum`, `maximum`, and `unit`.

## Synonyms and near-synonyms

- **Value code** and **choice value** are used interchangeably for this concept; "value code" strictly means the identifier.
- **Permissible value** is the next-generation vocabulary's term, where an [element binding](/glossary/element-binding.md) may restrict a shared element to a subset of them.[^cde-context]
- **Value set** is the whole list, not one member.

## Identifier form

`OIFMA_[A-Z]{3,4}_[0-9]{6}\.\d+`, for example `OIFMA_GMTS_707209.1`. Consuming structures store the code and its display text side by side, as `attributeValueCode` and `attributeValueDescription` in an [Exam Finding List](/glossary/exam-finding-list.md).[^efl-sample]

## Where it is used

[Finding model format](/semantic-foundation/finding-models/finding-model-format.md), [Identifiers](/semantic-foundation/finding-models/identifiers.md), and [Exam Finding List](/data-structures/exam-finding-list.md).

[^fm-py]: ChoiceValueIded and the value-code generator in the findingmodel package
[^efl-sample]: Exam Finding List sample data
[^cde-context]: CDE vocabulary, next-generation working glossary
