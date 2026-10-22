---
type: Format Specification
title: Finding model format
description: Released finding model fields, validation rules, examples, and unreleased metadata extensions.
tags: [semantic-foundation, finding-models, oifm, schema, format]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: fm-model
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/finding_model.py
    title: finding_model.py, released Pydantic definitions, findingmodel main branch
  - id: fm-contributor
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/contributor.py
    title: contributor.py, Person and Organization definitions, findingmodel main branch
  - id: index-code
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/oidm-common/src/oidm_common/models/index_code.py
    title: IndexCode definition, oidm-common package, findingmodel main branch
  - id: prose-schema
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/schema/finding_model_schema.md
    title: Finding Model Schema, prose mirror, findingmodels repository
    last_modified: 2025-06-17
  - id: example
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/defs/cervical_rib.fm.json
    title: cervical_rib.fm.json, findingmodels repository
  - id: fm-claude
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/CLAUDE.md
    title: CLAUDE.md, repository conventions, findingmodels repository
  - id: edge-models
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/packages/findingmodel/src/findingmodel/types/models.py
    title: types/models.py, feature/metadata-cleanup branch, findingmodel repository
  - id: edge-rewrite
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/canonical-structured-metadata-and-enrichment-rewrite.md
    title: Canonical Structured Metadata and Enrichment Rewrite, findingmodel feature/metadata-cleanup branch
---

# Where the format lives

There is no standalone JSON Schema file that governs the Open Imaging Finding Model (OIFM). The record format is a set of Pydantic classes in the `findingmodel` package, and those classes are the thing software enforces.[^fm-model] A prose mirror is maintained separately in the content repository as `schema/finding_model_schema.md`.[^prose-schema] The two have drifted, and the differences are reconciled line by line in [the finding model schema reference](/references/finding-model-schema.md), which this document summarizes rather than repeats.

Stored definitions are JSON files named `<snake_case_name>.fm.json` under `defs/` in the content repository, one finding per file.[^fm-claude]

# Two classes

| Class | Has identifiers | Used for |
|---|---|---|
| `FindingModelBase` | no | a definition while it is being authored, before registration |
| `FindingModelFull` | yes | the registered form, which is what `.fm.json` files hold |

`FindingModelBase` carries `name`, `description`, `synonyms`, `tags`, and `attributes`, and its attributes are the un-identified `ChoiceAttribute` and `NumericAttribute` variants. `FindingModelFull` adds `oifm_id`, `anatomic_locations`, `contributors`, and `index_codes`, and its attributes are the `Ided` variants.[^fm-model]

This split is the cause of a known data-integrity hazard. Round-tripping a registered model through `FindingModelBase` silently discards its identifiers, after which the identifier-adding helper mints fresh ones. That behavior is open as issue 42 and is described in [identifiers](/semantic-foundation/finding-models/identifiers.md).

## FindingModelFull

| Field | Type | Required | Constraints |
|---|---|---|---|
| `oifm_id` | string | yes | pattern `^OIFM_[A-Z]{3,4}_[0-9]{6}$` |
| `name` | string | yes | at least 5 characters |
| `description` | string | yes | at least 5 characters |
| `synonyms` | list of string, or null | no | non-empty if present |
| `tags` | list of string, or null | no | non-empty if present |
| `anatomic_locations` | list of `IndexCode`, or null | no | non-empty if present |
| `contributors` | list of `Person` or `Organization`, or null | no | none |
| `attributes` | list of `AttributeIded` | yes | at least one, discriminated on `type` |
| `index_codes` | list of `IndexCode`, or null | no | non-empty if present |

The prose mirror omits `anatomic_locations` entirely and does not state that at least one attribute is required.

# Attributes

An [attribute](/glossary/attribute.md) is one characterization axis. Two variants exist, discriminated by the `type` literal.

| Field | Choice | Numeric | Required | Constraints |
|---|---|---|---|---|
| `oifma_id` | yes | yes | yes, on the `Ided` variants | pattern `^OIFMA_[A-Z]{3,4}_[0-9]{6}$` |
| `name` | yes | yes | yes | 3 to 100 characters |
| `description` | yes | yes | no | 5 to 500 characters |
| `type` | `"choice"` | `"numeric"` | yes | the union discriminator |
| `values` | yes | no | yes for choice | at least two |
| `required` | yes | yes | no, default `false` | boolean |
| `max_selected` | yes | no | no, default `1` | integer, at least 1 |
| `minimum` | no | yes | no | integer, float, or null |
| `maximum` | no | yes | no | integer, float, or null |
| `unit` | no | yes | no | string or null |
| `index_codes` | yes | yes | no, `Ided` variants only | non-empty if present |

Validators require at least two choice values and generate value codes. They also repair `max_selected`: missing or falsy values become 1. Values above the number of choices, or the literal string `"all"`, become the number of choices.

A `ChoiceValueIded` has `value_code` matching `^OIFMA_[A-Z]{3,4}_[0-9]{6}\.\d+$`, a `name`, an optional `description`, and optional `index_codes`. A validator overwrites each `value_code` with `<oifma_id>.<index>` counting from zero, so the first value of an attribute ends in `.0`, the second in `.1`, and so on. The prose mirror's example numbers values from `.1`, which does not match what the code writes or what the stored corpus contains. Real presence attributes carry `.0` for absent and `.1` for present.

# Supporting types

`IndexCode` is defined once, in the `oidm-common` package, and is shared by finding models and by anatomic locations.[^index-code] It holds `system` (at least 3 characters), `code` (at least 2 characters), and an optional `display` (at least 3 characters if present). It is the mechanism for [coding](/glossary/coding.md) a definition into an external vocabulary such as [SNOMED CT](/glossary/snomed-ct.md), [RadLex](/glossary/radlex.md), [RadElement](/glossary/radelement.md), or the [Radiology Gamuts Ontology](/glossary/gamuts.md).

Contributors are `Person` or `Organization`.[^fm-contributor] An `Organization` has a `name` of at least 5 characters, a `code` matching `^[A-Z]{3,4}$`, and an optional URL. A `Person` has a GitHub username, an email address, a name, an `organization_code` matching the same pattern, and an optional URL. Both classes keep a process-wide registry and load from JSONL. That organization code is the same letter block that appears inside every OIFM and OIFMA identifier.

# A real definition

`cervical_rib.fm.json` is one of the shortest in the corpus and shows the common shape: an organization contributor, two choice attributes, generated value codes starting at `.0`, and model-level index codes pointing at both RadElement and RadLex.[^example]

```json
{
  "oifm_id": "OIFM_CDE_000101",
  "name": "Cervical Rib",
  "description": "Cervical rib detection on MRI",
  "contributors": [
    { "name": "ACR/RSNA Common Data Elements Project", "code": "CDE", "url": "https://radelement.org/" }
  ],
  "attributes": [
    {
      "oifma_id": "OIFMA_CDE_000632",
      "name": "Presence",
      "type": "choice",
      "values": [
        { "value_code": "OIFMA_CDE_000632.0", "name": "absent" },
        { "value_code": "OIFMA_CDE_000632.1", "name": "present" },
        { "value_code": "OIFMA_CDE_000632.2", "name": "indeterminate" },
        { "value_code": "OIFMA_CDE_000632.3", "name": "unknown" }
      ],
      "required": false,
      "max_selected": 1
    }
  ],
  "index_codes": [
    { "system": "RADELEMENT", "code": "RDES101", "display": "cervical rib" },
    { "system": "RADLEX", "code": "RID2471", "display": "rib" }
  ]
}
```

The example omits the `Laterality` attribute. On every commit, the validator reformats JSON, omits null and absent optional fields, and regenerates markdown, the corpus index, and the identifier registry from `defs/`. Generated files must not be edited manually.[^fm-claude]

# On the work edge, not released

The following is on the `feature/metadata-cleanup` branch of `findingmodel`, read at commit `1942b06`, and on its base `dev`. None of it is on `main`, none of it is in the prose mirror, and no released package carries it. It is recorded because it is the stated direction for the format.

The branch splits `finding_model.py` into `types/models.py`, `types/attributes.py`, and `types/metadata.py`, leaving attribute and `IndexCode` definitions unchanged, and adds eight optional fields to both `FindingModelBase` and `FindingModelFull`.[^edge-models] The design document states the goal as making structured metadata "canonical `FindingModel` state rather than disposable enrichment output."[^edge-rewrite]

| Field | Type | Allowed values in code |
|---|---|---|
| `body_regions` | list of `BodyRegion` | head, neck, chest, breast, abdomen, pelvis, spine, upper_extremity, lower_extremity, whole_body |
| `subspecialties` | list of `Subspecialty` | BR, CA, CH, ER, GI, GU, HN, IR, MI, MK, NM, NR, OB, OI, PD, SQ, VA |
| `etiologies` | list of `EtiologyCode` | 27 codes, many colon-separated, from `inflammatory` and `neoplastic:malignant` through `iatrogenic:device` and `normal-variant` |
| `entity_type` | `EntityType` | finding, diagnosis, grouping, measurement, assessment, recommendation, technique_issue |
| `applicable_modalities` | list of `Modality` | XR, CT, MR, US, PET, NM, MG, RF, DSA |
| `expected_time_course` | `ExpectedTimeCourse` | `duration` from hours to permanent, plus `modifiers` from progressive, stable, evolving, resolving, intermittent, fluctuating, recurrent |
| `age_profile` | `AgeProfile` | `applicability` is `all_ages` or a list of nine MeSH-derived age stages; `more_common_in` is an optional list of the same |
| `sex_specificity` | `SexSpecificity` | male-specific, female-specific, sex-neutral |

The branch also normalizes legacy input. Body regions become lowercase, `Arm` and `Leg` become `upper_extremity` and `lower_extremity`, and `ALL` becomes `whole_body`. Modalities `CR` and `DX` become `XR`, and free-text ages expand into `AgeProfile`.

Model-level `index_codes` and `anatomic_locations` require nonempty `display`. Canonical `index_codes` accept exact or clinically substitutable matches. Broader, narrower, and related candidates go to a separate review artifact.

The branch fails its readiness assessment. [The metadata fields extract](/references/oifm-metadata-fields-extract.md) records three disagreements between its code and prose. See [the enrichment pipeline](/semantic-foundation/finding-models/enrichment-pipeline.md) for assignment and [format evolution](/roadmap/finding-model-format-evolution.md) for planned work.

[^fm-model]: finding_model.py, findingmodel main branch
[^fm-contributor]: contributor.py, findingmodel main branch
[^index-code]: IndexCode definition, oidm-common package
[^prose-schema]: Finding Model Schema, prose mirror, findingmodels repository
[^example]: cervical_rib.fm.json, findingmodels repository
[^fm-claude]: CLAUDE.md, findingmodels repository
[^edge-models]: types/models.py, feature/metadata-cleanup branch
[^edge-rewrite]: Canonical Structured Metadata and Enrichment Rewrite, feature/metadata-cleanup branch
