---
type: Reference
title: Finding model schema
description: The Open Imaging Finding Model record format as specified in the findingmodels repository, reconciled field by field against the Pydantic definitions that validate it.
tags: [references, oifm, finding-models, schema]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: fm-schema
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/schema/finding_model_schema.md
    title: Finding Model Schema, prose specification, findingmodels repository
    last_modified: 2025-06-17
  - id: fm-pydantic
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/finding_model.py
    title: finding_model.py, released Pydantic definitions, findingmodel main branch
  - id: fm-contributor
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/contributor.py
    title: contributor.py, Person and Organization definitions, findingmodel main branch
  - id: oidm-common-indexcode
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/oidm-common/src/oidm_common/models/index_code.py
    title: IndexCode definition, oidm-common package, findingmodel main branch
  - id: edge-models
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/packages/findingmodel/src/findingmodel/types/models.py
    title: types/models.py on the feature/metadata-cleanup branch, findingmodel repository
  - id: edge-metadata
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/packages/findingmodel/src/findingmodel/types/metadata.py
    title: types/metadata.py on the feature/metadata-cleanup branch, findingmodel repository
  - id: edge-rewrite
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/canonical-structured-metadata-and-enrichment-rewrite.md
    title: Canonical Structured Metadata and Enrichment Rewrite, findingmodel work edge
---

# Provenance and status

The specification below is migrated near-verbatim from `schema/finding_model_schema.md` in the `findingmodels` repository, last changed on 2025-06-17 and read here at commit `4475ac1` on `main`.[^fm-schema] Its structure and wording are the author's; only dash punctuation was normalized to house style and the term "user" was left as written. That file is a prose mirror, not an executable schema. The record format that software actually enforces is the set of Pydantic models in the `findingmodel` repository, and the two have drifted. The reconciliation section states every difference. A third section records fields that exist only on the `feature/metadata-cleanup` work-edge branch and are not in any released version.

# Finding Model Schema

## Overview

This schema describes radiology findings, their [attributes](/glossary/attribute.md), and how they are structured for the Open Imaging Data Model (OIDM). It enables semantic tagging and standardization for use in imaging reports and research.

## Main Finding Model Object

### Required Fields

- **oifm_id**: *Type: string*, *Pattern: `^OIFM_[A-Z]{3,4}_[0-9]{6}$`*. Unique ID for the [finding model](/glossary/finding-model.md).
- **name**: *Type: string*, *Minimum length: 5*. Short, descriptive name for the finding model.
- **description**: *Type: string*, *Minimum length: 5*. One or two sentences describing the finding.
- **attributes**: *Type: array of `Attribute` objects (see below)*. List of attributes (choice or numeric) to characterize the finding.

### Optional Fields

- **synonyms**: *Type: array of strings*. Other terms used to describe the finding.
- **tags**: *Type: array of strings*. Tags for categorizing the finding.
- **contributors**: *Type: array of `Person` or `Organization` objects*. Users or organizations who contributed.
- **index_codes**: *Type: array of `IndexCode` objects*. Links to standard ontologies (for example SNOMED, RadLex).

## Attribute Types

### 1. Choice Attribute (`ChoiceAttributeIded`)

A selectable attribute with predefined values (for example severity, shape).

- **oifma_id**: Unique attribute ID (pattern: `^OIFMA_[A-Z]{3,4}_[0-9]{6}$`)
- **name**: Short, descriptive name.
- **description**: Optional. Description of the attribute.
- **type**: Always `"choice"`.
- **values**: Array of `ChoiceValueIded` objects (see below).
- **required**: Boolean. Whether always required.
- **max_selected**: Integer. Maximum values selectable (default: 1).
- **index_codes**: Array of `IndexCode` objects. Optional. Links to ontologies.

#### Choice Value (`ChoiceValueIded`)

- **value_code**: Unique code for the value (pattern: `^OIFMA_[A-Z]{3,4}_[0-9]{6}\.\d+$`)
- **name**: Name of the value.
- **description**: Optional.
- **index_codes**: Optional array of `IndexCode` objects.

### 2. Numeric Attribute (`NumericAttributeIded`)

A range or measurement attribute (for example size, number of findings).

- **oifma_id**: Unique attribute ID.
- **name**: Short, descriptive name.
- **description**: Optional.
- **type**: Always `"numeric"`.
- **minimum**: Optional integer or number.
- **maximum**: Optional integer or number.
- **unit**: Optional string (unit of measure).
- **required**: Boolean.
- **index_codes**: Optional array of `IndexCode` objects.

## Supporting Types

### `IndexCode`

Links to standard ontology codes (for example SNOMED, RadLex). See [index code](/glossary/index-code.md).

- **system**: Name of the system (for example "SNOMED").
- **code**: Code in the system.
- **display**: Optional display name.

### `Person`

Contributor details.

- **github_username**: Required.
- **email**: Required.
- **name**: Required.
- **organization_code**: Required.
- **url**: Optional.

### `Organization`

- **name**: Required.
- **code**: Required, 3-4 uppercase letters.
- **url**: Optional.

## Example Structure

```json
{
  "oifm_id": "OIFM_ABCD_123456",
  "name": "Pulmonary Nodule",
  "description": "A round or oval growth in the lung.",
  "attributes": [
    {
      "type": "choice",
      "oifma_id": "OIFMA_ABCD_123456",
      "name": "Shape",
      "values": [
        { "value_code": "OIFMA_ABCD_123456.1", "name": "Round" },
        { "value_code": "OIFMA_ABCD_123456.2", "name": "Oval" }
      ]
    },
    {
      "type": "numeric",
      "oifma_id": "OIFMA_ABCD_654321",
      "name": "Size (cm)",
      "minimum": 0,
      "maximum": 10,
      "unit": "cm"
    }
  ]
}
```

# Reconciliation with the Pydantic source of truth

The released definitions live in `packages/findingmodel/src/findingmodel/finding_model.py`, read at commit `75afd39` on `main`.[^fm-pydantic] Two classes matter. `FindingModelBase` is a definition without registry identifiers, used while authoring. `FindingModelFull` is the registered form, and it is what the prose specification above describes. The tables record what the code enforces and mark each difference from the prose.

## FindingModelFull

| Field | Type | Required | Constraints in code | Difference from the prose specification |
|---|---|---|---|---|
| `oifm_id` | string | yes | pattern `^OIFM_[A-Z]{3,4}_[0-9]{6}$` | none |
| `name` | string | yes | `min_length=5` | none |
| `description` | string | yes | `min_length=5` | none |
| `synonyms` | sequence of string or null | no | `min_length=1` if present | the prose does not state the non-empty constraint |
| `tags` | sequence of string or null | no | `min_length=1` if present | the prose does not state the non-empty constraint |
| `anatomic_locations` | list of `IndexCode` or null | no | `min_length=1` if present | **absent from the prose specification entirely** |
| `contributors` | list of `Person` or `Organization`, or null | no | none | none |
| `attributes` | sequence of `AttributeIded` | yes | `min_length=1`, discriminated on `type` | the prose does not state that at least one attribute is required |
| `index_codes` | list of `IndexCode` or null | no | `min_length=1` if present | the prose does not state the non-empty constraint |

`FindingModelBase` carries `name`, `description`, `synonyms`, `tags`, and `attributes` with the same constraints, and has no `oifm_id`, `anatomic_locations`, `contributors`, or `index_codes`. Its attributes are the un-identified `ChoiceAttribute` and `NumericAttribute` variants.

## Attributes

| Field | Choice | Numeric | Required | Constraints in code |
|---|---|---|---|---|
| `oifma_id` | yes | yes | yes on the Ided variants | pattern `^OIFMA_[A-Z]{3,4}_[0-9]{6}$` |
| `name` | yes | yes | yes | `min_length=3`, `max_length=100` |
| `description` | yes | yes | no | `min_length=5`, `max_length=500` |
| `type` | `"choice"` | `"numeric"` | yes | literal, and the discriminator for the union |
| `values` | yes | no | yes for choice | `min_length=2` |
| `required` | yes | yes | no, defaults `false` | boolean |
| `max_selected` | yes | no | no, defaults `1` | integer, `ge=1` |
| `minimum` | no | yes | no | integer or float or null |
| `maximum` | no | yes | no | integer or float or null |
| `unit` | no | yes | no | string or null |
| `index_codes` | yes | yes | no, Ided variants only | `min_length=1` if present |

Three behaviors of the code are not in the prose specification.

- **A choice attribute needs at least two values.** The prose says only "array of `ChoiceValueIded` objects".
- **`max_selected` is repaired on input.** A validator that runs before parsing sets `max_selected` to `1` when it is missing or falsy, and clamps it to the number of values when it is larger or when the literal string `"all"` is supplied. So `"all"` is accepted as input although it is never a stored value.
- **Value codes are generated, not supplied.** A validator on `ChoiceAttributeIded` overwrites each value's `value_code` with `<oifma_id>.<index>`, indexing from zero. The prose example shows the first value as `.1`, but the code writes `.0` for the first value. Real data follows the code: an absent presence value is `.0` and present is `.1`, as the [Exam Finding List example](/references/exam-finding-list-example.md) shows.

## ChoiceValueIded

| Field | Type | Required | Constraints in code |
|---|---|---|---|
| `value_code` | string | yes | pattern `^OIFMA_[A-Z]{3,4}_[0-9]{6}\.\d+$` |
| `name` | string | yes | none |
| `description` | string or null | no | none |
| `index_codes` | list of `IndexCode` or null | no | `min_length=1` if present |

## IndexCode

`IndexCode` is defined once, in the `oidm-common` package, and is shared by finding models and by [anatomic locations](/glossary/anatomic-location.md).[^oidm-common-indexcode]

| Field | Type | Required | Constraints in code |
|---|---|---|---|
| `system` | string | yes | `min_length=3` |
| `code` | string | yes | `min_length=2` |
| `display` | string or null | no | `min_length=3` if present |

The prose specification omits all three length constraints. `IndexCode` renders as `"{system} {code} {display}"`.

## Person and Organization

Contributors are defined in `contributor.py`.[^fm-contributor] Both classes keep a process-wide registry keyed by `github_username` and by `code`, and both can be loaded from and saved to JSONL.

| Class | Field | Required | Constraints in code |
|---|---|---|---|
| `Organization` | `name` | yes | `min_length=5` |
| `Organization` | `code` | yes | pattern `^[A-Z]{3,4}$` |
| `Organization` | `url` | no | must be a valid HTTP URL |
| `Person` | `github_username` | yes | `min_length=3` |
| `Person` | `email` | yes | must be a valid email address |
| `Person` | `name` | yes | `min_length=3` |
| `Person` | `organization_code` | yes | pattern `^[A-Z]{3,4}$` |
| `Person` | `url` | no | must be a valid HTTP URL |

The prose specification lists these fields correctly but states no constraints. The organization code is the same 3-to-4-letter code that appears inside every OIFM and OIFMA identifier.

## Identifier regexes in one place

| Identifier | Regex | Where it is enforced |
|---|---|---|
| Finding model | `^OIFM_[A-Z]{3,4}_[0-9]{6}$` | `FindingModelFull.oifm_id` |
| Attribute | `^OIFMA_[A-Z]{3,4}_[0-9]{6}$` | `ChoiceAttributeIded.oifma_id`, `NumericAttributeIded.oifma_id` |
| Choice value | `^OIFMA_[A-Z]{3,4}_[0-9]{6}\.\d+$` | `ChoiceValueIded.value_code` |
| Organization code | `^[A-Z]{3,4}$` | `Organization.code`, `Person.organization_code` |

The six digits are generated at random by `generate_oifm_id` and `generate_oifma_id`, which take the organization code and uppercase it. The digit count is a module constant, so all three identifier patterns move together if it ever changes.

# On the work edge, not released

Everything in this section is on the `feature/metadata-cleanup` branch of `findingmodel`, read at commit `1942b06`. None of it is on `main`, and none of it appears in the prose specification. It is recorded here because it is the stated direction for the format, not because it is in effect.

The branch splits `finding_model.py` into `types/models.py`, `types/attributes.py`, and `types/metadata.py`. Attribute and `IndexCode` definitions are unchanged by the split. The design document that governs the work states the goal as making structured metadata "canonical `FindingModel` state rather than disposable enrichment output".[^edge-rewrite]

Eight optional fields are added to both `FindingModelBase` and `FindingModelFull`.[^edge-models]

| Field | Type | Values |
|---|---|---|
| `body_regions` | list of `BodyRegion` or null | head, neck, chest, breast, abdomen, pelvis, spine, upper_extremity, lower_extremity, whole_body |
| `subspecialties` | list of `Subspecialty` or null | BR, CA, CH, ER, GI, GU, HN, IR, MI, MK, NM, NR, OB, OI, PD, SQ, VA |
| `etiologies` | list of `EtiologyCode` or null | 27 codes, many of them colon-separated, from `inflammatory` and `neoplastic:malignant` through `iatrogenic:device` and `normal-variant` |
| `entity_type` | `EntityType` or null | finding, diagnosis, grouping, measurement, assessment, recommendation, technique_issue |
| `applicable_modalities` | list of `Modality` or null | XR, CT, MR, US, PET, NM, MG, RF, DSA |
| `expected_time_course` | `ExpectedTimeCourse` or null | `duration` from hours through permanent, plus `modifiers` from progressive, stable, evolving, resolving, intermittent, fluctuating, recurrent |
| `age_profile` | `AgeProfile` or null | `applicability` is either the literal `all_ages` or a non-empty list of nine MeSH-derived age stages; `more_common_in` is an optional list of the same stages |
| `sex_specificity` | `SexSpecificity` or null | male-specific, female-specific, sex-neutral |

Three further changes ride along.[^edge-metadata]

- **Legacy values normalize on input.** Title-cased body regions normalize to lowercase, `Arm` and `Leg` to `upper_extremity` and `lower_extremity`, and `ALL` to `whole_body`. Modality `CR` and `DX` normalize to `XR`. Etiology `traumatic` and `post-traumatic` normalize to `traumatic:acute` and `traumatic:sequela`. Free-text age labels such as "pediatric" and "elderly" expand to an `AgeProfile`.
- **Model-level codes must carry a display value.** A validator on `FindingModelFull` rejects any entry in `index_codes` or `anatomic_locations` whose `display` is empty.
- **Canonical `index_codes` are narrowed.** The branch restricts them to exact matches or clinically substitutable near-equivalents, and sends broader, narrower, and merely related candidates to a separate enrichment review artifact rather than to the model.

The branch's own readiness assessment is not yet passing, so the field list above should be read as the current shape of unmerged work.

[^fm-schema]: Finding Model Schema, prose specification, findingmodels repository
[^fm-pydantic]: finding_model.py, released Pydantic definitions, findingmodel main branch
[^fm-contributor]: contributor.py, Person and Organization definitions, findingmodel main branch
[^oidm-common-indexcode]: IndexCode definition, oidm-common package, findingmodel main branch
[^edge-models]: types/models.py on the feature/metadata-cleanup branch, findingmodel repository
[^edge-metadata]: types/metadata.py on the feature/metadata-cleanup branch, findingmodel repository
[^edge-rewrite]: Canonical Structured Metadata and Enrichment Rewrite, findingmodel work edge
