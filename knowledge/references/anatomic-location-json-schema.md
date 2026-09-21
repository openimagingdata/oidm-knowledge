---
type: Reference
title: Anatomic location record format
description: The two JSON record formats for anatomic locations, the original anatomiclocations.org body part schema and the current anatomic-locations package format, with a real record from each.
tags: [references, anatomic-locations, schema, radlex]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: al-schema
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/data/body_parts_schema.json
    title: body_parts_schema.json, anatomiclocations.org repository
  - id: al-data
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/data/body_parts.json
    title: body_parts.json, anatomiclocations.org curated body part set
  - id: fm-json-schema
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/.claude/skills/manage-anatomic-locations/reference/json-schema.md
    title: Anatomic Locations Source JSON field reference, findingmodel repository
  - id: fm-location-model
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/anatomic-locations/src/anatomic_locations/models/location.py
    title: AnatomicLocation model, anatomic-locations package, findingmodel repository
  - id: fm-enums
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/anatomic-locations/src/anatomic_locations/models/enums.py
    title: Anatomic location enumerations, anatomic-locations package, findingmodel repository
  - id: fm-source-data
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/notebooks/data/anatomic_locations_noembed.json
    title: anatomic_locations_noembed.json, the current curated anatomic location set
  - id: build-plan
    resource: https://github.com/openimagingdata/oidm-knowledge/blob/main/knowledge/plans/2026-09-20-knowledgebase-build-plan.md
    title: Knowledgebase build plan, source map and work edge
---

# Provenance and status

Two record formats for [anatomic locations](/glossary/anatomic-location.md) coexist in OIDM, and this document holds both. The first is the original schema from the `anatomiclocations.org` repository, read at commit `1f39fa4`, which validates a curated set of 2,890 body parts keyed by [RadLex](/glossary/radlex.md) identifier. The second is the format used by the `anatomic-locations` package inside the `findingmodel` repository, read at commit `75afd39` on `main`, which covers 2,926 records and adds classification, dual hierarchies, and explicit [laterality](/glossary/laterality.md). The build plan names the newer package and its dataset as the current anatomic data, and the older set as lineage.[^build-plan] Field tables here are compiled from the schema file and the model source; the records shown are copied unchanged from the published data.

# Lineage A: the anatomiclocations.org body part schema

The file `data/body_parts_schema.json` is a JSON Schema draft-06 document.[^al-schema] It validates `data/body_parts.json`, which declares `$version` `1.0.0-rc.1` and carries 2,890 entries under `bodyParts`.[^al-data] Every object sets `additionalProperties: false`, so the field list is closed.

## Container

| Field | Type | Required |
|---|---|---|
| `$schema` | string | yes |
| `$version` | string | yes |
| `bodyParts` | array of `BodyPartElement` | yes |

## BodyPartElement

| Field | Type | Required | Notes |
|---|---|---|---|
| `radlexId` | `RadlexID` | yes | the entry's own identifier |
| `description` | string | yes | display name |
| `containedById` | `RadlexID` | yes | the structure that spatially contains this one |
| `partOfId` | `RadlexID` | no | mereological parent, distinct from containment |
| `leftId` | `RadlexID` | no | left variant, present on the unsided entry |
| `rightId` | `RadlexID` | no | right variant, present on the unsided entry |
| `unsidedId` | string | no | back-reference from a sided entry to its unsided form |
| `sexSpecific` | string | no | one of `Male` or `Female` |
| `synonyms` | array of string | no | |
| `codes` | array of `Code` | no | |

`RadlexID` is constrained to the pattern `^RID\d+(_RID\d+)*$`, which admits both a plain RadLex identifier and the compound form used for sided variants. `unsidedId` is the one field declared as a plain string rather than as a `RadlexID`, so the pattern is not enforced on it. A `Code` is a closed object of `system` and `code`, both required, with no display name.

Across the 2,890 entries, 1,611 carry a `leftId`, 1,584 carry an `unsidedId`, 990 carry a `partOfId`, and 2,282 carry at least one code. The code systems present are SNOMED, FMA, UMLS, and MESH.

## A real record

The entry for uterine adnexa shows containment, part-of, a laterality pair, sex specificity, a synonym, and three codes.

```json
{
  "radlexId": "RID294",
  "description": "uterine adnexa",
  "containedById": "RID2507",
  "leftId": "RID294_RID5824",
  "rightId": "RID294_RID5825",
  "sexSpecific": "Female",
  "partOfId": "RID270",
  "synonyms": ["adnexa"],
  "codes": [
    { "system": "FMA", "code": "265256" },
    { "system": "SNOMED", "code": "23043003" },
    { "system": "UMLS", "code": "C0001575" }
  ]
}
```

`RID5824` and `RID5825` are the RadLex identifiers for left and right, which is why the sided variants are written as compound identifiers rather than as new numbers.

# Lineage B: the anatomic-locations package format, current

This lineage has two representations of the same information. The curation format is the JSON file that editors change, documented in the repository's own field reference.[^fm-json-schema] The runtime format is the `AnatomicLocation` Pydantic model that the package returns from its index.[^fm-location-model]

## Curation format fields

The source file `notebooks/data/anatomic_locations_noembed.json` is a flat JSON array of 2,926 objects.[^fm-source-data]

| Field | Type | Required | Notes |
|---|---|---|---|
| `_id` | string | yes | RadLex identifier, compound for sided variants |
| `description` | string | yes | lowercase display name |
| `region` | string | no | body region label |
| `snomedId` | string | no | SNOMED CT concept, strongly encouraged |
| `snomedDisplay` | string | no | SNOMED preferred term |
| `acrCommonId` | string | no | ACR Common identifier |
| `codes` | array of `{system, code}` | no | FMA, MESH, UMLS and others |
| `containedByRef` | `{id, display}` | no | immediate spatial container |
| `containsRefs` | array of `{id, display}` | no | indexed structures inside this one |
| `partOfRef` | `{id, display}` | no | mereological parent |
| `hasPartsRefs` | array of `{id, display}` | no | mereological children |
| `leftRef` | `{id, display}` | no | left variant |
| `rightRef` | `{id, display}` | no | right variant |
| `unsidedRef` | `{id, display}` | no | back-reference to the generic entry |
| `synonyms` | array of string | no | clinical shorthand |
| `definition` | string | no | brief definition with its source in brackets |

Two fields appear in the data but not in the field reference: `sexSpecific`, on 110 records, and `anatomicLocationsId`, on a single record. The field reference also lists `"Spine"` among the common `region` values, but no record in the data uses it and the runtime enumeration has no spine member. The nine region values actually present are Head (869), Upper Extremity (582), Lower Extremity (579), Neck (235), Thorax (226), Abdomen (212), Pelvis (152), Breast (46), and Body (25).

The two hierarchy relations are kept deliberately distinct, as documented in the field reference: `containedByRef` is spatial, meaning X is inside Y, while `partOfRef` is mereological, meaning X is a component of Y. See [contained-by and part-of](/glossary/contained-by-and-part-of.md). SNOMED coding follows one rule without exception: of the Structure, Entire, and Part concepts in a SNOMED anatomy triad, always use the "Structure of" concept, because that is what SNOMED intends for finding sites and procedure sites.

Laterality is expressed as a triad. The generic entry carries `leftRef` and `rightRef`; each sided entry carries `unsidedRef` back to the generic. 827 distinct left-sided and 827 distinct right-sided entries are referenced, and every reference resolves to a record in the file. 1,597 records carry an `unsidedRef`.

## A real record

The hypopharynx entry, unchanged from the data file and used as the worked example in the field reference.

```json
{
  "_id": "RID10021",
  "acrCommonId": "4013944",
  "snomedId": "81502006",
  "snomedDisplay": "Hypopharyngeal structure",
  "description": "hypopharynx",
  "region": "Neck",
  "containedByRef": { "id": "RID7488", "display": "neck" },
  "synonyms": ["laryngopharynx"],
  "partOfRef": { "id": "RID13211", "display": "pharynx" },
  "codes": [
    { "system": "FMA", "code": "54880" },
    { "system": "MESH", "code": "A14.724.490" },
    { "system": "UMLS", "code": "C0014540" }
  ],
  "definition": "The portion of the pharynx between the inferior portion of the oropharynx and the larynx. [MeSH]"
}
```

## Runtime model fields

`AnatomicLocation` is the object the package hands back. It renames the curation fields, resolves the reference objects into a lightweight `AnatomicRef` of `id` and `display`, and adds classification and materialized paths.

| Field | Type | Default | Notes |
|---|---|---|---|
| `id` | string | required | RadLex identifier |
| `description` | string | required | display name |
| `region` | `AnatomicRegion` or null | null | Head, Neck, Thorax, Abdomen, Pelvis, Upper Extremity, Lower Extremity, Breast, Body |
| `location_type` | `LocationType` | `structure` | structure, space, region, body_part, system, group |
| `body_system` | `BodySystem` or null | null | ten systems, cardiovascular through special_senses |
| `structure_type` | `StructureType` or null | null | around forty types, set only when `location_type` is structure |
| `laterality` | `Laterality` | `nonlateral` | generic, left, right, nonlateral |
| `definition` | string or null | null | |
| `sex_specific` | string or null | null | |
| `synonyms` | list of string | empty | |
| `codes` | list of `IndexCode` | empty | the same [index code](/glossary/index-code.md) type finding models use |
| `references` | list of `WebReference` | empty | educational and documentation links |
| `containment_path` | string or null | null | materialized path from the root |
| `containment_parent` | `AnatomicRef` or null | null | |
| `containment_depth` | integer or null | null | |
| `containment_children` | list of `AnatomicRef` | empty | |
| `partof_path` | string or null | null | materialized path in the part-of hierarchy |
| `partof_parent` | `AnatomicRef` or null | null | |
| `partof_depth` | integer or null | null | |
| `partof_children` | list of `AnatomicRef` | empty | |
| `left_variant` | `AnatomicRef` or null | null | |
| `right_variant` | `AnatomicRef` or null | null | |
| `generic_variant` | `AnatomicRef` or null | null | |

Two computed fields are serialized with the record: `is_bilateral`, true when `laterality` is generic, and `is_lateralized`, true when it is left or right. `LocationType` is a coarse split modeled on the top level of the Foundational Model of Anatomy, separating discrete structures from spaces, regions, macro body parts, organ systems, and named groups. `StructureType` is the finer classification, with members grouped as musculoskeletal, vascular, peripheral neural, brain-specific, organs, lymphatic, anatomical organization, and spatial.[^fm-enums]

The materialized paths are what make hierarchy queries cheap. Containment ancestry, descendants, and the "is X inside Y" test all read `containment_path` rather than walking parent links, and the part-of hierarchy works the same way through `partof_path`.

A location converts to an `IndexCode` with `system` set to `anatomic_locations`, its RadLex identifier as the code, and its description as the display. That is the form an anatomic location takes when it is attached to a [finding model](/glossary/finding-model.md).

# Which is current

The `anatomic-locations` package format is current. It is the format the OIDM tooling reads, it carries the larger and more recently curated dataset, and it adds the classification axes and explicit laterality that the original schema left implicit. The `anatomiclocations.org` schema remains the published format of the original curated set and of the wrapper libraries built on it, and is documented here because that data and those libraries are still reachable.

[^al-schema]: body_parts_schema.json, anatomiclocations.org repository
[^al-data]: body_parts.json, anatomiclocations.org curated body part set
[^fm-json-schema]: Anatomic Locations Source JSON field reference, findingmodel repository
[^fm-location-model]: AnatomicLocation model, anatomic-locations package, findingmodel repository
[^fm-enums]: Anatomic location enumerations, anatomic-locations package, findingmodel repository
[^fm-source-data]: anatomic_locations_noembed.json, the current curated anatomic location set
[^build-plan]: Knowledgebase build plan, source map and work edge
