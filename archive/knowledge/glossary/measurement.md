---
type: Glossary Term
title: Measurement
description: A quantitative descriptor, defined in the next-generation CDE vocabulary as distinct from a DataElement and realized in OIFM as a numeric attribute.
tags: [glossary, semantic-foundation, cde, next-generation]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: cde-context
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/CONTEXT.md
    title: CDE vocabulary, next-generation working glossary
  - id: fm-py
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/finding_model.py
    title: NumericAttribute in the findingmodel package
  - id: idr
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md
    title: IHE IDR Phase II extract for the CDE vocabulary
---

# Measurement

"A quantitative descriptor, distinct from a DataElement. Its measurement method is optional and is unspecified by default."[^cde-context] In the next-generation CDE vocabulary a Measurement is its own node type, so a length, a volume, or an angle is not modelled as a categorical element with numeric values.

OIDM's current format expresses the same idea without a separate type. A numeric [attribute](/glossary/attribute.md) is "an attribute of a radiology finding where the radiologist would choose a number from a range," carrying `minimum`, `maximum`, and `unit`.[^fm-py] The measurement method is not represented at all.

The authoring guidance treats a coherent group of related measurements as a valid finding in its own right, giving emphysema quantification and brain volume measurements as examples, where "the finding is the act of performing a structured quantitative assessment, and the attributes are the measurements within it."

## Synonyms and near-synonyms

- **Numeric attribute** is the OIFM realization.
- **Float element** is the RadElement realization, a [CDE element](/glossary/cde-element.md) with bounds and a step.
- **[DataElement](/glossary/data-element.md)** is explicitly not this; the distinction is stated in the definition.
- **Computed property** is IHE IDR's name for a measurement derived from others, such as a volume from diameters, linked by `derivedFrom`.[^idr]

## Identifier form

None of its own in either vocabulary. A numeric attribute carries an ordinary `OIFMA_[A-Z]{3,4}_[0-9]{6}` identifier.

## Where it is used

[Finding model format](/semantic-foundation/finding-models/finding-model-format.md) and [Next-generation vocabulary](/semantic-foundation/common-data-elements/next-generation-vocabulary.md).

## Conflicts

The two models disagree on type. The next-generation vocabulary makes Measurement a first-class node distinct from DataElement; OIFM has no such distinction, only a `type` discriminator on the attribute. A document that says "measurement" must say which model it means.

[^cde-context]: CDE vocabulary, next-generation working glossary
[^fm-py]: NumericAttribute in the findingmodel package
[^idr]: IHE IDR Phase II extract
