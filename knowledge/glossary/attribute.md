---
type: Glossary Term
title: Attribute
description: A property a radiologist uses to characterize a finding, either a choice attribute with an enumerated value set or a numeric attribute with a range and unit.
tags: [glossary, semantic-foundation, finding-models]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: fm-py
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/finding_model.py
    title: ChoiceAttribute, NumericAttribute, and the OIFMA identifier pattern
  - id: fm-schema
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/schema/finding_model_schema.md
    title: Finding model schema, prose mirror
  - id: cde-context
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/CONTEXT.md
    title: CDE vocabulary, next-generation working glossary
  - id: siim
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/siim-meeting-extract.md
    title: SIIM meeting minutes extract, nomenclature discussion
---

# Attribute

"An attribute that a radiologist would use to characterize a particular finding in a radiology report."[^fm-py] Every [finding model](/glossary/finding-model.md) has at least one attribute. There are exactly two kinds.

| Kind | Discriminator | Distinctive fields |
|---|---|---|
| Choice attribute | `type: "choice"` | `values` (at least two [attribute values](/glossary/attribute-value.md)), `max_selected` (default 1) |
| Numeric attribute | `type: "numeric"` | `minimum`, `maximum`, `unit` |

Both kinds carry `oifma_id`, `name`, an optional `description`, a `required` flag meaning the attribute is used every time the finding is described, and optional [index codes](/glossary/index-code.md).[^fm-schema] A choice attribute is described as one "where the radiologist would choose from a list of options," a numeric attribute as one "where the radiologist would choose a number from a range."[^fm-py]

## Synonyms and near-synonyms

- **[Data element](/glossary/data-element.md)** is the next-generation vocabulary's replacement term. The difference is ownership: an OIFM attribute belongs to one finding model, while a DataElement is shared and reached through an [element binding](/glossary/element-binding.md).
- **[CDE element](/glossary/cde-element.md)** is the RadElement counterpart, identified `RDE####`.
- **[Measurement](/glossary/measurement.md)** is the next-generation counterpart of a numeric attribute, and is deliberately not a DataElement there.
- **Facet** and **structured metadata field** are not attributes. They describe the finding model itself, not an instance of the finding.

## Identifier form

`OIFMA_[A-Z]{3,4}_[0-9]{6}`, unique across the whole corpus, not just within one model.[^fm-schema]

## Where it is used

[Finding model format](/semantic-foundation/finding-models/finding-model-format.md) and [Identifiers](/semantic-foundation/finding-models/identifiers.md).

## Conflicts

Committee discussions left the choice between "element," "attribute," and "data element" unresolved. The next-generation glossary uses DataElement, while OIFM uses "attribute."[^siim][^cde-context] The two words denote nearly the same thing with different scoping rules, so a document must say which vocabulary it is using.

[^fm-py]: ChoiceAttribute and NumericAttribute in the findingmodel package
[^fm-schema]: Finding model schema, prose mirror
[^cde-context]: CDE vocabulary, next-generation working glossary
[^siim]: SIIM meeting minutes extract
