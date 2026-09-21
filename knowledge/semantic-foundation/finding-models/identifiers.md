---
type: Reference
title: Finding model identifiers
description: The OIFM and OIFMA identifier grammar, the organization-code segment and its registered values, value codes, how identifiers are minted and checked, and what stability is guaranteed.
tags: [semantic-foundation, finding-models, oifm, identifiers, reference]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
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

Three identifier forms carry the whole referencing scheme. Each is enforced by a regular expression on the Pydantic field that holds it.[^fm-model]

| Identifier | Regular expression | Example | Enforced on |
|---|---|---|---|
| Finding model | `^OIFM_[A-Z]{3,4}_[0-9]{6}$` | `OIFM_CDE_000101` | `FindingModelFull.oifm_id` |
| Attribute | `^OIFMA_[A-Z]{3,4}_[0-9]{6}$` | `OIFMA_CDE_000632` | `ChoiceAttributeIded.oifma_id`, `NumericAttributeIded.oifma_id` |
| Choice value | `^OIFMA_[A-Z]{3,4}_[0-9]{6}\.\d+$` | `OIFMA_CDE_000632.1` | `ChoiceValueIded.value_code` |

The digit count is a module constant, `ID_LENGTH`, set to 6 and interpolated into all three patterns, so the three move together if it ever changes.

Reading one of these left to right gives you the whole address. `OIFMA_CDE_000632.1` is value 1 of attribute `000632`, contributed under organization code `CDE`. Because the attribute identifier is globally unique rather than scoped to its finding, an attribute code alone identifies the finding it belongs to, which is what makes the registry lookup in the next section possible.

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

The registry is rebuilt from `defs/` by `scripts/validator.py`, which walks every definition file, validates it, and fails if a finding identifier or an attribute identifier is seen twice.[^validator] That check is the only thing standing between random minting and a collision. A pre-commit hook runs the validator on every commit and stages the regenerated `ids.json`, the markdown renders, and the repository index, so a definition cannot land without the registry landing with it.

# Round-trip regeneration, issue 42

The one documented way to lose an identifier is to round-trip a registered model through `FindingModelBase`. That class has no `oifm_id` field, so validating a stored definition against it silently discards the finding identifier and every attribute identifier. The helper that adds identifiers then sees none present and mints new ones.[^issue42]

The issue, open since 2026-04-18, describes this as "a silent data-integrity hazard for any workflow that loads an existing `.fm.json` as a dict, needs to mutate it, and wants ID allocation for just the new part." It was hit in a review flow that added a change-from-prior attribute to a legacy model carrying only presence; the published finding identifier and the existing attribute identifier were both regenerated, and external references to them would have become dangling. The workaround shipped in the content work operates on the dictionary directly and allocates only the identifiers genuinely missing, building value codes from the attribute identifier by hand. Four candidate fixes are enumerated in the issue and none has been chosen.

# Stability

What is documented amounts to this.

- An identifier, once minted and committed, names one definition file, and the validator enforces that no second file claims it.
- The registry admits that an identifier can legitimately appear on more than one row of an external list. The [MGB exam-oriented sub-taxonomies](/semantic-foundation/finding-models/finding-taxonomies.md) note that "an ID can appear on two rows where those earlier writebacks mapped two findings onto one model." That is a property of those files, not of the registry.
- Nothing in the repository documents a deprecation, retirement, or supersession mechanism for an identifier. There is no version field on a finding model in the released format, and schema versioning is an open task rather than a shipped feature.
- The round-trip defect above is the known exception to stability in practice, and it is unresolved.

Downstream systems rely on this. Exam Finding Lists store nothing but the identifier and a display string, so a changed identifier breaks the link between a stored [Observation](/glossary/observation.md) and its definition. The content repository is the single source of finding model identity for the catalog site, which consumes `defs/` as a git submodule, and for the extraction platform, which resolves identifiers through the published registry. See [the repository map](/repositories/repository-map.md).

[^fm-model]: finding_model.py, findingmodel main branch
[^base-orgs]: base_organizations.jsonl, findingmodel main branch
[^ids-json]: ids.json, findingmodels repository
[^validator]: validator.py, findingmodels repository
[^fm-claude]: CLAUDE.md, findingmodels repository
[^issue42]: Issue 42, findingmodel repository
