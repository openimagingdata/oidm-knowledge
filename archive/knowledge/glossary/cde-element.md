---
type: Glossary Term
title: CDE element
description: One property inside a published CDE set, carrying an RDE identifier and a value set, integer, or float definition.
tags: [glossary, semantic-foundation, cde]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: schema-diff
    resource: https://github.com/openimagingdata/openimagingdata.org/blob/fb431dfc81801a5a8e621c0e8bf2acd20f74be7d/schemas/schema_differences.md
    title: Differences between the CDE Set schema and the RadElement API
  - id: fhir-sample
    resource: https://github.com/openimagingdata/FHIRSamples/blob/9ae2fa934298e51789e355c9f4e0b71fabf6b5aa/lung_ca_screening_example/example1OIDMradiologist.json
    title: Radiologist finding Observation with RDE-coded components
  - id: lineage-ts
    resource: https://github.com/openimagingdata/OpenImagingDataModel.ts/blob/7c97c33a23323358caa542973dc30d46b618d8a2/packages/cde_set/data/guide_to_elements.md
    title: Guide to CDE element fields in the OpenImagingDataModel.ts reference implementation
  - id: cde-context
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/CONTEXT.md
    title: CDE vocabulary, next-generation working glossary
---

# CDE element

A property in a published [CDE set](/glossary/cde-set.md), with a question and permissible answers. Its definition names the property, declares its value type, and lists categorical values. The schema distinguishes a `value_set` from `integer_values` and `float_values`, the latter carrying bounds and a step.[^schema-diff]

In a [CDE-labeled FHIR Observation](/glossary/cde-labeled-fhir-observation.md), the parent's `code` identifies the set. Each component's `code` identifies an element, and its value identifies the chosen answer, such as `RDE1717.1` for element `RDE1717`.[^fhir-sample] The dot-suffixed value code convention is the same one OIFM uses for [attribute values](/glossary/attribute-value.md).

## Synonyms and near-synonyms

- **[Attribute](/glossary/attribute.md)** is the OIFM counterpart, scoped to one finding model rather than shared.
- **[Data element](/glossary/data-element.md)** is the next-generation vocabulary's node type, explicitly shared across definitions and reached through an [element binding](/glossary/element-binding.md).[^cde-context]
- **Element** unqualified usually means this, but in the RelaxNG schema it also means an XML element.
- **[Measurement](/glossary/measurement.md)** is the next-generation term for the quantitative case, which RadElement handles as a float element.

## Identifier form

`RDE` followed by digits, for example `RDE1717`. Value codes append a dot and an index, for example `RDE1717.1`.[^fhir-sample]

## Where it is used

[CDEs and RadElement](/semantic-foundation/common-data-elements/cdes-and-radelement.md) and [FHIR mapping](/data-structures/fhir-mapping.md).

## Conflicts

The published element schema and the RadElement API differ: `parent_set`, `images`, `biological_sex`, `age_range`, `modality`, and `references` appear in the schema without API counterparts, while `url` and `question` appear in the API without schema counterparts.[^schema-diff] Reconciling the two is a long-standing open issue in the staging repository.

[^schema-diff]: Differences between the CDE Set schema and the RadElement API
[^fhir-sample]: Radiologist finding Observation with RDE-coded components
[^lineage-ts]: Guide to CDE element fields
[^cde-context]: CDE vocabulary, next-generation working glossary
