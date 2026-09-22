---
type: Source Extract
title: CDE set schema versus the RadElement API
description: A 2023 CDE schema and API comparison, with notes on later JSON Schema changes.
tags: [references, cde, radelement, schema, source-extract]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: differences
    resource: https://github.com/openimagingdata/openimagingdata.org/blob/fb431dfc81801a5a8e621c0e8bf2acd20f74be7d/schemas/schema_differences.md
    title: Differences between Defined CDE Set Schema and RadElement API, openimagingdata.org repository
    last_modified: 2023-03-28
  - id: rnc
    resource: https://github.com/openimagingdata/openimagingdata.org/blob/fb431dfc81801a5a8e621c0e8bf2acd20f74be7d/schemas/original_cde_set_schema.rnc
    title: original_cde_set_schema.rnc, the RelaxNG CDE set schema the note compares
  - id: cde-schema-10
    resource: https://github.com/openimagingdata/common_data_elements/blob/35536d8c858bcd33e730a00c919edaef2e310a0b/schema/cde.schema-1.0.json
    title: cde.schema-1.0.json, common_data_elements repository
  - id: cde-schema-11
    resource: https://github.com/openimagingdata/common_data_elements/blob/35536d8c858bcd33e730a00c919edaef2e310a0b/schema/cde.schema-1.1.json
    title: cde.schema-1.1.json, common_data_elements repository
  - id: cde-readme
    resource: https://github.com/openimagingdata/common_data_elements/blob/35536d8c858bcd33e730a00c919edaef2e310a0b/README.md
    title: common_data_elements README, stating which schema version the definitions conform to
---

# Provenance and status

This extract preserves `schemas/schema_differences.md` from `openimagingdata.org` at `fb431df`, last changed 2023-03-28. It compares the [CDE set](/glossary/cde-set.md) format in `original_cde_set_schema.rnc` with the JSON returned by the [RadElement](/glossary/radelement.md) API. Its structure and wording are the author's; only dash punctuation was normalized.

The extract is a 2023 snapshot. The closing section compares two later JSON Schema versions. The source contains no individual names.

# Differences between Defined CDE Set Schema and RadElement API

The CDE Set Schema is a RelaxNG schema that defines the structure of a CDE Set. The RadElement API has a de facto JSON schema that defines the structure of a CDE Set. The schemas are similar, but not identical. This document describes the differences between the two schemas.

## Differences

- Structural differences with arrays; for example, the CDE Set schema defines a wrapper element `<images>` with individual `<image>` elements, while the RadElement API defines a JSON array of image objects. Similarly so for `<index_codes>`/`<index_code>`, `<elements>`/`<element>`.
- CDE Set Schema defines a `<url>` element of `<index_code>`, while the API defines an `href` property of the `index_code` object.
- CDE Set Schema specifies that `<system>` may be `RADLEX`, `SNOMEDCT`, or `LOINC`, while the API doesn't appear to constrain it (or constrains it according to its internal database).
- Structure of `authors` is different in the API; `authors` property is an object with a `person` array and an `organization` array, while the CDE Set Schema defines an `<authors>` element with interspersed `<person>` and `<organization>` child elements.

### `Set` Definition Differences

- Present in CDE Set Schema, not in RadElement API
  - `images`
  - `modality` (a complex structure)
  - `biological_sex`
  - `age_range`
- Present in RadElement API, not in CDE Set Schema
  - `url`
  - `body_parts`

### `Element` Definition Differences

- Schema elements without corresponding API properties:
  - `<parent_set>`
  - `<images>`
  - `<biological_sex>`
  - `<age_range>`
  - `<modality>`
- API properties without corresponding schema elements:
  - `url`
  - `question`
- In `<element>`/`<value_set>`, schema has child elements not clearly in API:
  - `<references>`
- In `<element>`/`<float_values>`, `<step>` is defined as an integer; not apparently so in the API (but is the schema right?)

# What the JSON Schema versions changed

The `common_data_elements` repository mirrors RadElement's [common data element](/glossary/cde.md) definitions. At `35536d8`, its `schema/` directory contains versions 1.0 and 1.1, both using JSON Schema draft-07. The README states that definitions conform to 1.0, so 1.1 is published but not in force.[^cde-readme]

Both files declare `$id` as `https://github.com/ACR-RSNA-CDEs/blob/v1.0.0/cde.schema.json`, so the identifier does not distinguish them.

## Changes from 1.0 to 1.1 in the set definition

| Aspect | 1.0 | 1.1 |
|---|---|---|
| Required properties | `id`, `name`, `description`, `set_version`, `status`, `elements`, `history`, `index_codes`, `specialties`, `schema_version` | `id`, `name`, `description`, `set_version`, `current_status`, `elements`, `specialties`, `schema_version` |
| Status fields | `status`, `history` | renamed to `current_status` and `status_history` |
| Added properties | | `images`, `modalities` |
| No longer required | | `index_codes` and the status history |

## Changes in the element definition

| Aspect | 1.0 | 1.1 |
|---|---|---|
| Required properties | `id`, `name`, `element_version`, `status`, `schema_version` | `id`, `name`, `element_version`, `current_status`, `schema_version` |
| Added properties | | `body_parts`, `images`, `modalities` |
| Removed properties | `boolean_value`, `status` | |

At the definitions level, 1.1 drops `event`, `biological_sex`, and `boolean_value` and adds `modality`.

## How this bears on the 2023 catalogue

The JSON Schema versions change three comparisons:

- **`images` and `modality`.** The note lists both as present in the RelaxNG schema and missing from the API. Version 1.1 adds `images` and `modalities` to both the set and the element, moving the JSON side toward the RelaxNG side rather than away from it.
- **`url` and `body_parts`.** The note lists both as API-only. Both are properties of the set in JSON Schema 1.0 and 1.1, and `body_parts` is added to the element in 1.1.
- **`biological_sex` and `age_range`.** These remain unreconciled. `biological_sex` has a definition in 1.0 and is dropped in 1.1; `age_range` appears in neither JSON Schema version. Both were RelaxNG-only in 2023 and are now absent from the schema in force.

One constraint moved the other way. The note records the RelaxNG schema as allowing `RADLEX`, `SNOMEDCT`, and `LOINC` for an [index code](/glossary/index-code.md) system. Both JSON Schema versions add `ACRCOMMON` to that enumeration. Both use `url` on index codes where the API uses `href`.

[^differences]: Differences between Defined CDE Set Schema and RadElement API, openimagingdata.org repository
[^rnc]: original_cde_set_schema.rnc, the RelaxNG CDE set schema the note compares
[^cde-schema-10]: cde.schema-1.0.json, common_data_elements repository
[^cde-schema-11]: cde.schema-1.1.json, common_data_elements repository
[^cde-readme]: common_data_elements README, stating which schema version the definitions conform to
