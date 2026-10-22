---
type: Glossary Term
title: RadLex ID (RID)
description: The identifier form used by RadLex concepts, and the primary key of OIDM anatomic locations.
tags: [glossary, semantic-foundation, terminologies, identifiers]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: al-code
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/data/body_parts_schema.json
    title: body_parts_schema.json, radlexId pattern
  - id: al-package
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/anatomic-locations/src/anatomic_locations/models/location.py
    title: AnatomicLocation id field in the anatomic-locations package
  - id: ipl-claude
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/CLAUDE.md
    title: imaging-problem-list domain model, dev branch
  - id: baseline
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/05-radlex-baseline.md
    title: RadLex baseline verification, next-gen-2026 branch
---

# RadLex ID (RID)

The identifier form used by [RadLex](/glossary/radlex.md) concepts: the letters `RID` followed by digits, for example `RID1301` for lung or `RID50149` for pulmonary nodule. RIDs are the primary key of OIDM [anatomic locations](/glossary/anatomic-location.md): the curated data file keys every record on `radlexId`, and the newer package keys every location on `id` holding the same value.[^al-code][^al-package]

Downstream structures carry the RID directly. An [Exam Finding List](/glossary/exam-finding-list.md) finding's optional `anatomicLocation` is a pair of `locationId` and `locationDisplay`, where the identifier is an RID from the `anatomic-locations` package.[^ipl-claude]

## Synonyms and near-synonyms

- **RID** is the usual short form, and "RadLex ID" the long one.
- **`radlexId`** and **`locationId`** are field names holding one.
- **RPID** is a different scheme, the legacy RadLex Playbook identifier for procedures rather than concepts.
- **`acrCommonId`** is a parallel cross-reference on the same records, not an RID.

## Identifier form

`RID\d+` for a plain concept. Sided variants in the original curated set use a composite form matching `^RID\d+(_RID\d+)*$`, joining the base structure's RID to a laterality concept's RID, for example `RID294_RID5824`.[^al-code] The composite form is an OIDM curation convention and is not itself a RadLex identifier.

## Where it is used

[Data model](/semantic-foundation/anatomic-locations/data-model.md), [Ontologies used](/semantic-foundation/terminologies/ontologies-used.md), and [Exam Finding List](/data-structures/exam-finding-list.md).

## Conflicts

RadLex marks superseded concepts with a `Replaced_by` annotation, so a stored RID can become obsolete without the storing system knowing.[^baseline] Nothing in the OIDM data structures records which RadLex version an identifier was resolved against.

[^al-code]: body_parts_schema.json
[^al-package]: AnatomicLocation id field
[^ipl-claude]: imaging-problem-list domain model, dev branch
[^baseline]: RadLex baseline verification
