---
type: Format Specification
title: Anatomic location data model
description: The record model for an anatomic location in both lineages, its identifier scheme, its two hierarchies, its laterality triads, its classification fields, and its external codes, with verified counts.
tags: [semantic-foundation, anatomic-locations, schema, radlex, laterality]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
sources:
  - id: al-schema
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/data/body_parts_schema.json
    title: body_parts_schema.json, anatomiclocations.org
  - id: al-data
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/data/body_parts.json
    title: body_parts.json, release 1.0.0-rc.1, 2,890 curated body parts
  - id: al-code
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/docs/code.markdown
    title: anatomiclocations.org data file description, the two hierarchies
  - id: fm-json-schema
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/.claude/skills/manage-anatomic-locations/reference/json-schema.md
    title: Anatomic Locations source JSON field reference, findingmodel
  - id: fm-source-data
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/notebooks/data/anatomic_locations_noembed.json
    title: anatomic_locations_noembed.json, 2,926 records, the current curated set
  - id: fm-location-model
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/anatomic-locations/src/anatomic_locations/models/location.py
    title: AnatomicLocation runtime model, anatomic-locations package
  - id: fm-enums
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/anatomic-locations/src/anatomic_locations/models/enums.py
    title: Anatomic location enumerations, anatomic-locations package
  - id: fm-normalized
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/tasks/done/anatomic-locations-normalized-schema.md
    title: Rich anatomic location DuckDB with relationships, the plan that designed the normalized model
  - id: cde-axis
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/11-anatomy-axis.md
    title: The anatomy axis, current state, ACR-RSNA-CDEs next-gen-2026
---

# Scope

This document describes the record: what an [anatomic location](/glossary/anatomic-location.md) carries and what each field means. The verbatim JSON Schema and the full runtime field list live in [the anatomic location record format reference](/references/anatomic-location-json-schema.md). Two datasets exist and are not reconciled with each other, so both are described here; [lineage and current implementation](/semantic-foundation/anatomic-locations/lineage-and-current-implementation.md) says which is current and why.

| Dataset | Records | Version | Field naming |
|---|---|---|---|
| `body_parts.json`, the original curated set | 2,890 | `1.0.0-rc.1` | `radlexId`, `containedById`, `leftId` |
| `anatomic_locations_noembed.json`, the current curated set | 2,926 | undeclared | `_id`, `containedByRef`, `leftRef` |

# The identifier

Every record is keyed by a [RadLex identifier](/glossary/radlex-id.md). The original schema constrains it to the pattern `^RID\d+(_RID\d+)*$`, which admits both a plain identifier and a composite one.[^al-schema]

A composite identifier is how a sided variant is named. RadLex has modifier concepts for left (`RID5824`) and right (`RID5825`), and a sided structure joins the base to the modifier with an underscore. The left uterine adnexa is `RID294_RID5824`; the right is `RID294_RID5825`. Of the 2,926 current records, 1,910 carry a plain RadLex identifier and 1,016 are composite. The original set has 1,880 plain identifiers among its 2,890 records.

Composite identifiers are a local convention, not RadLex content. The next-generation vocabulary work records them as "the exception the RadLex track will remove by minting real ids."[^cde-axis]

# Descriptive fields

| Field | Both lineages | Meaning |
|---|---|---|
| `description` | required | Lowercase display name, one per record |
| `synonyms` | optional | Clinical shorthand; 1,126 records in the original set, 1,156 in the current one |
| `definition` | current set only | A brief definition with its source in brackets, on 278 records |
| `sexSpecific` | optional | `Male` or `Female`; 110 records in both sets |

`sexSpecific` is present in the current data but absent from that lineage's field reference, along with a stray `anatomicLocationsId` on a single record.

# The two hierarchies

Every record carries a containment parent. The distinction between the two hierarchies is stated on the original project's code page: the contained-by hierarchy is "physically contained in," as a kidney is in the retroperitoneum, and the part-of hierarchy is "a component of a larger structure or system," as the adnexa are part of the female genital system.[^al-code] See [contained by and part of](/glossary/contained-by-and-part-of.md).

| Relation | Original field | Current field | Coverage in the current set |
|---|---|---|---|
| Spatial parent | `containedById` (required) | `containedByRef` | 2,926, every record |
| Spatial children | not stored | `containsRefs` | 186 |
| Mereological parent | `partOfId` | `partOfRef` | 1,123 |
| Mereological children | not stored | `hasPartsRefs` | 334 |

The original set stores parent pointers only and lets a library derive children. The current set stores both directions as `{id, display}` reference objects, so a consumer can read a node's children without indexing the whole file. Containment is a rooted tree from `RID39569`, whole body. The part-of relation covers fewer than half the records and is not a tree.

Two data defects are visible in the current file and are worth knowing before traversing it. 111 records carry a `partOfRef` pointing at themselves, and one carries a self-referential `leftRef`. The build process already expects self-referential containment at the root, which is legitimate, but self-referential part-of on 111 nodes is not.[^fm-normalized]

# Laterality triads

A sided structure is represented by three records, not by a flag on one. The generic record carries `leftRef` and `rightRef`; each sided record carries `unsidedRef` back to the generic one and a reference to its counterpart. The full convention, including the containment and synonym rules for sided entries, is in [laterality conventions](/semantic-foundation/anatomic-locations/laterality-conventions.md). See also [laterality](/glossary/laterality.md).

| Field | Original set | Current set |
|---|---|---|
| Left variant | `leftId`, 1,611 | `leftRef`, 1,625 |
| Right variant | `rightId`, 1,611 | `rightRef`, 1,625 |
| Generic variant | `unsidedId`, 1,584 | `unsidedRef`, 1,597 |

# Classification

The current set adds a `region` to every record, one of nine values. The runtime model exposes it as an `AnatomicRegion` enumeration with exactly those nine members.[^fm-enums]

| Region | Records | Region | Records |
|---|---|---|---|
| Head | 869 | Abdomen | 212 |
| Upper Extremity | 582 | Pelvis | 152 |
| Lower Extremity | 579 | Breast | 46 |
| Neck | 235 | Body | 25 |
| Thorax | 226 | | |

The field reference for the curation format lists `"Spine"` among the common region values, but no record uses it and the runtime enumeration has no spine member.

Three further classification fields exist on the runtime model and are empty in the data: `location_type` (structure, space, region, body part, system, group), `body_system` (ten systems), and `structure_type` (roughly forty finer types, set only when the location type is structure).[^fm-location-model] The next-generation vocabulary analysis confirms this, recording that "the package's structure-type, body-system, and location-type fields exist but are empty in this data," and names the absence of a type relation over locations as "the major shortcoming" for scope statements of the form "applies to tendons."[^cde-axis] See [anatomic scope](/glossary/anatomic-scope.md).

# External codes

Both sets cross-reference other terminologies. The original set puts every code in one `codes` array of `{system, code}`. The current set promotes SNOMED CT to its own pair of fields with a display name, adds an ACR Common identifier, and leaves the rest in `codes`.

| Code | Original set | Current set |
|---|---|---|
| [SNOMED CT](/glossary/snomed-ct.md) | 1,732 in `codes` | 1,782 as `snomedId` with `snomedDisplay` |
| [FMA](/glossary/fma.md) | 1,643 | 1,649 |
| [UMLS](/glossary/umls.md) | 578 | 580 |
| MeSH | 232 | 233 |
| ACR Common | absent | 2,025 as `acrCommonId` |
| Any code at all | 2,282 of 2,890 | 2,318 of 2,926 |

SNOMED coding follows one rule without exception: of the Structure, Entire, and Part concepts in a SNOMED anatomy triad, use the "Structure of" concept, because that is what SNOMED intends for finding sites and procedure sites.[^fm-json-schema]

# A real record

The current format, unchanged from the data file. It shows containment, part-of, a synonym, three codes, and a definition with its source.

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

# From record to usable object

The curation format is what an editor changes. The package that consumes it normalizes each record into an `AnatomicLocation` object, resolves the reference objects, adds a laterality enum, and precomputes a materialized containment path and part-of path so that ancestry, descendants, and the "is X inside Y" test are string comparisons rather than recursive walks.[^fm-normalized] A location converts to an [index code](/glossary/index-code.md) with system `anatomic_locations`, its RadLex identifier as the code, and its description as the display, which is the form it takes when attached to a [finding model](/glossary/finding-model.md).[^fm-location-model]

[^al-schema]: body_parts_schema.json, anatomiclocations.org
[^al-data]: body_parts.json, release 1.0.0-rc.1
[^al-code]: anatomiclocations.org data file description
[^fm-json-schema]: Anatomic Locations source JSON field reference, findingmodel
[^fm-source-data]: anatomic_locations_noembed.json, the current curated set
[^fm-location-model]: AnatomicLocation runtime model, anatomic-locations package
[^fm-enums]: Anatomic location enumerations, anatomic-locations package
[^fm-normalized]: Rich anatomic location DuckDB with relationships
[^cde-axis]: The anatomy axis, current state, ACR-RSNA-CDEs next-gen-2026
