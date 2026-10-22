---
type: Reference
title: Finding model identifiers
description: Finding, attribute, and value identifier formats, generation, validation, and stability limits.
tags: [semantic-foundation, finding-models, oifm, identifiers, reference]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: fm-model
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/finding_model.py
    title: finding_model.py, identifier patterns and generators, findingmodel main branch
  - id: base-orgs
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/data/base_organizations.jsonl
    title: base_organizations.jsonl, the seeded organization registry, findingmodel main branch
  - id: ids-json
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/ids.json
    title: ids.json, the identifier registry, findingmodels repository
  - id: validator
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/scripts/validator.py
    title: validator.py, duplicate detection and registry regeneration, findingmodels repository
  - id: fm-claude
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/CLAUDE.md
    title: CLAUDE.md, repository conventions, findingmodels repository
  - id: issue42
    resource: https://github.com/openimagingdata/findingmodel/issues/42
    title: "Issue 42: add_ids_to_model silently regenerates existing oifm_id when a model is round-tripped through FindingModelBase"
---

# The grammar

Pydantic fields enforce three identifier formats.[^fm-model]

| Identifier | Regular expression | Example | Enforced on |
|---|---|---|---|
| Finding model | `^OIFM_[A-Z]{3,4}_[0-9]{6}$` | `OIFM_CDE_000101` | `FindingModelFull.oifm_id` |
| Attribute | `^OIFMA_[A-Z]{3,4}_[0-9]{6}$` | `OIFMA_CDE_000632` | `ChoiceAttributeIded.oifma_id`, `NumericAttributeIded.oifma_id` |
| Choice value | `^OIFMA_[A-Z]{3,4}_[0-9]{6}\.\d+$` | `OIFMA_CDE_000632.1` | `ChoiceValueIded.value_code` |

The digit count is a module constant, `ID_LENGTH`, set to 6 and interpolated into all three patterns, so the three move together if it ever changes.

`OIFMA_CDE_000632.1` identifies value 1 of attribute `000632` under organization `CDE`. A globally unique attribute identifier also identifies its parent finding through the registry.

# The organization segment

The three-or-four-letter block names the contributing organization. It is the same code that appears as `Organization.code` and `Person.organization_code`, both constrained to `^[A-Z]{3,4}$`. See [OIDM organization code](/glossary/oidm-organization-code.md).

Seven organizations ship in the package's seeded registry.[^base-orgs]

| Code | Organization |
|---|---|
| `MSFT` | Microsoft |
| `MGB` | MassGeneral Brigham |
| `GMTS` | Radiology Gamuts Ontology |
| `RSNA` | Radiological Society of North America |
| `ACR` | American College of Radiology |
| `CDE` | ACR/RSNA Common Data Elements Project |
| `OIDM` | Open Imaging Data Model |

Five of the seven appear in the published corpus. Counting the 2,382 registered finding model identifiers in `ids.json` on `main` by their organization segment gives the following distribution, and the 5,709 registered attribute identifiers give the second column.[^ids-json]

| Code | Finding models | Attributes |
|---|---:|---:|
| `GMTS` | 1,933 | 3,867 |
| `OIDM` | 256 | 512 |
| `CDE` | 115 | 831 |
| `MGB` | 47 | 378 |
| `MSFT` | 31 | 121 |
| Total | 2,382 | 5,709 |

The organization segment records provenance, not ownership of the concept. A `GMTS` identifier means the definition entered the corpus from the Radiology Gamuts Ontology import; a `CDE` identifier means it was derived from an ACR and RSNA common data element. The content breakdown is in [the content catalog](/semantic-foundation/finding-models/content-catalog.md).

# Minting

Digits are random, not sequential. `generate_oifm_id(source)` and `generate_oifma_id(source)` uppercase the organization code they are given and append six digits drawn one at a time from a uniform random draw.[^fm-model] There is no central allocator and no reservation step. Collisions are prevented after the fact by the registry rather than before the fact by coordination.

Identifiers are never written by hand. The authoring tools call the generators; the repository conventions state that `ids.json` is auto-generated and must never be edited manually.[^fm-claude]

# The registry and its check

`ids.json` at the root of the `findingmodels` repository is a flat, regenerated map with two members.[^ids-json]

```json
{
  "oifm_ids": { "OIFM_CDE_000101": "cervical_rib.fm.json" },
  "attribute_ids": { "OIFMA_CDE_000632": ["cervical_rib.fm.json", "Presence"] }
}
```

`oifm_ids` maps each finding identifier to the file that defines it. `attribute_ids` maps each attribute identifier to a pair of file name and attribute name. Value codes are not registered separately, because they are derived from the attribute identifier.

`scripts/validator.py` rebuilds the registry from `defs/`, validates each file, and rejects repeated finding or attribute identifiers.[^validator] This is the sole collision check. Every commit's pre-commit hook runs it and stages the registry, markdown renders, and corpus index.

# Round-trip regeneration, issue 42

Validating a registered model through `FindingModelBase`, which has no `oifm_id`, silently drops its finding and attribute identifiers. The helper then generates new ones.[^issue42]

The issue, open since 2026-04-18, describes this as "a silent data-integrity hazard for any workflow that loads an existing `.fm.json` as a dict, needs to mutate it, and wants ID allocation for just the new part." It was hit in a review flow that added a change-from-prior attribute to a legacy model carrying only presence; the published finding identifier and the existing attribute identifier were both regenerated, and external references to them would have become dangling. The workaround shipped in the content work operates on the dictionary directly and allocates only the identifiers genuinely missing, building value codes from the attribute identifier by hand. Four candidate fixes are enumerated in the issue and none has been chosen.

# Stability

The documented stability rules are:

- An identifier, once minted and committed, names one definition file, and the validator enforces that no second file claims it.
- The registry admits that an identifier can legitimately appear on more than one row of an external list. The [MGB exam-oriented sub-taxonomies](/semantic-foundation/finding-models/finding-taxonomies.md) note that "an ID can appear on two rows where those earlier writebacks mapped two findings onto one model." That is a property of those files, not of the registry.
- Nothing in the repository documents a deprecation, retirement, or supersession mechanism for an identifier. There is no version field on a finding model in the released format, and schema versioning is an open task rather than a shipped feature.
- The round-trip defect above is the known exception to stability in practice, and it is unresolved.

Exam Finding Lists reference definitions by identifier and display string, so identifier changes break stored [Observation](/glossary/observation.md) links. The content repository supplies identity to the catalog site, which reads `defs/` through a git submodule, and to the extraction platform's registry lookups. See [the repository map](/repositories/repository-map.md).

[^fm-model]: finding_model.py, findingmodel main branch
[^base-orgs]: base_organizations.jsonl, findingmodel main branch
[^ids-json]: ids.json, findingmodels repository
[^validator]: validator.py, findingmodels repository
[^fm-claude]: CLAUDE.md, findingmodels repository
[^issue42]: Issue 42, findingmodel repository
