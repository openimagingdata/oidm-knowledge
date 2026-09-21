---
type: Glossary Term
title: DataElement
description: In the next-generation CDE vocabulary, a shared categorical descriptor whose permissible values may be ordered, reused across definitions through element bindings.
tags: [glossary, semantic-foundation, cde, next-generation]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: cde-context
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/CONTEXT.md
    title: CDE vocabulary, next-generation working glossary
  - id: idr
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md
    title: IHE IDR Phase II extract for the CDE vocabulary
  - id: siim
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/siim-meeting-extract.md
    title: SIIM meeting minutes extract, nomenclature discussion
---

# DataElement

In the next-generation CDE vocabulary, "a categorical descriptor whose permissible values may be ordered or unordered. Semantic ordering is explicit and is distinct from display order."[^cde-context] A DataElement is a node in the definition graph, not a field inside a finding definition, and it is shared: a [FindingClass](/glossary/finding-class.md) reaches it through an [element binding](/glossary/element-binding.md), which may restrict the use to a subset of the element's permissible values without changing the element or its other bindings.[^cde-context]

Three companion rules shape how a DataElement is used. Selection cardinality states "the permitted number of values selected for a DataElement in a use, such as single or multiple selection," explicitly distinct from value ordering and from whether a report mentions the element. Modality applicability separates a descriptor's intrinsic modality limit from its binding-specific applicability. Categorization requires that a distinction be expressed either by a categorizing DataElement or by a taxonomy of named classes, not both for the same distinction in the same model.[^cde-context]

This vocabulary is a working draft on the `next-gen-2026` branch. It is not a settled integration model, and its own preamble says so.[^cde-context]

## Synonyms and near-synonyms

- **[CDE element](/glossary/cde-element.md)** is the current published counterpart, identified `RDE####`.
- **[Attribute](/glossary/attribute.md)** is the OIFM counterpart, owned by one finding model instead of shared.
- **[Measurement](/glossary/measurement.md)** is deliberately not a DataElement: it is a quantitative descriptor, defined as distinct.[^cde-context]
- In IHE IDR the same slot is `Observation.code`, "the property," with the chosen value in `Observation.value`.[^idr]

## Identifier form

No published form. The working graph uses internal node identifiers, and an `RDE2` URI base is under discussion for the successor coding system.

## Where it is used

[Next-generation vocabulary](/semantic-foundation/common-data-elements/next-generation-vocabulary.md) and [IHE IDR alignment](/data-structures/ihe-idr-alignment.md).

## Conflicts

Committee minutes record an unresolved debate between "element," "attribute," and "data element" as the name for this concept, with OIFM using "attribute" and the next-generation glossary using DataElement.[^siim] IHE IDR's word "observation" also denotes roughly what this vocabulary calls a DataElement value, a collision the IDR extract flags explicitly.[^idr]

[^cde-context]: CDE vocabulary, next-generation working glossary
[^idr]: IHE IDR Phase II extract
[^siim]: SIIM meeting minutes extract
