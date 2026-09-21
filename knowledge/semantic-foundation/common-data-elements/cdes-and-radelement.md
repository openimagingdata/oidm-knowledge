---
type: Concept
title: CDEs and RadElement
description: What ACR and RSNA common data elements are, where they are published and schematized, where the two published schema descriptions disagree, and how the Open Imaging Data Model uses them today.
tags: [semantic-foundation, cde, radelement, schema, fhir]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T18:00:00Z }
sources:
  - id: radelement-site
    resource: https://radelement.org/
    title: RadElement, "Common Data Elements (CDEs) for Radiology"
  - id: radelement-api
    resource: https://api3.rsna.org/radelement/v1/sets
    title: RadElement public sets API, read 2026-09-21
  - id: cde-readme
    resource: https://github.com/openimagingdata/common_data_elements/blob/35536d8c858bcd33e730a00c919edaef2e310a0b/README.md
    title: common_data_elements README, the RadElement snapshot and its schema versions
  - id: cde-schema-10
    resource: https://github.com/openimagingdata/common_data_elements/blob/35536d8c858bcd33e730a00c919edaef2e310a0b/schema/cde.schema-1.0.json
    title: cde.schema-1.0.json, common_data_elements repository
  - id: cde-schema-11
    resource: https://github.com/openimagingdata/common_data_elements/blob/35536d8c858bcd33e730a00c919edaef2e310a0b/schema/cde.schema-1.1.json
    title: cde.schema-1.1.json, common_data_elements repository
  - id: acr-schema
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/ea4d2716820a731716dd97c77a3dae523ca38152/cde.schema.json
    title: cde.schema.json on the master branch of ACR-RSNA-CDEs, the schema CDEStaging names as canonical
  - id: acr-schema-ng
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/cde.schema.json
    title: cde.schema.json on the next-gen-2026 branch of ACR-RSNA-CDEs, byte-identical to the master copy
  - id: staging-readme
    resource: https://github.com/openimagingdata/CDEStaging/blob/b814a102655054ac08b3c118cb1977a387655a8b/README.md
    title: CDEStaging README, pointing at ACR-RSNA-CDEs for the canonical schema
  - id: fhirsamples
    resource: https://github.com/openimagingdata/FHIRSamples/tree/9ae2fa934298e51789e355c9f4e0b71fabf6b5aa/lung_ca_screening_example
    title: FHIRSamples lung cancer screening example, CDE-coded FHIR Observations
  - id: sbo-model
    resource: https://github.com/openimagingdata/findingmodels/blob/a30c3c95fa3943e7340ce87575f4b1b926987eb8/defs/small_bowel_obstruction.fm.json
    title: Small Bowel Obstruction finding model, OIFM_CDE_000178, carrying a RADELEMENT index code
  - id: ipl-mvp
    resource: https://github.com/openimagingdata/IPL-MVP-ExtractionAndLabeling/blob/b06948fa417aeff0a6a4b97729c915b3ce5d5ed4/data/finding_models.json
    title: IPL-MVP-ExtractionAndLabeling curated finding model list, keyed by OIFM identifier
---

# What a common data element is

A [common data element (CDE)](/glossary/cde.md) is a governed definition of a radiology finding, or of one property of a finding, authored and balloted through the ACR and RSNA common data elements programme. The programme publishes at [RadElement](/glossary/radelement.md), whose banner describes it as "Common Data Elements (CDEs) for Radiology" and which browses its content by radiology subspecialty.[^radelement-site]

The model has three levels, and the word "CDE" is used loosely for all of them.

| Level | Identifier | What it is |
|---|---|---|
| [CDE set](/glossary/cde-set.md) | `RDES###` | A whole finding, such as Pulmonary Nodule (`RDES195`) |
| [CDE element](/glossary/cde-element.md) | `RDE####` | One property inside a set, such as the nodule's attenuation |
| Value | `RDE####.n` | One permitted answer to an element |

Both the set and the element carry a name, a description, a version, a status, index codes into external terminologies, specialties, and a status history. A set owns an ordered list of elements; an element owns a value set, a numeric range with units, or a free-text or date type.

The public API at `api3.rsna.org/radelement/v1/sets` listed 281 sets on 2026-09-21: 191 published, 89 proposed, and 1 retired, with set numbers running from `RDES2` to `RDES441`.[^radelement-api]

# Where the definitions live in OIDM

The `common_data_elements` repository is the Open Imaging Data Model (OIDM) local snapshot of that registry. Its README describes it as "a periodically updated version of the Common Data Element definitions as stored and maintained in the ACR/RSNA RadElement web site," formatted as JSON for easy consumption.[^cde-readme] At commit `35536d8` it holds 145 set definitions under `definitions/`, one file per set named `RDES###.cde.json`, and the README indexes all 145 alphabetically by clinical topic with their set identifiers.

The snapshot is data, not code. It is used as a reference corpus rather than as a dependency, and it is not regenerated automatically. See [the repository map](/repositories/repository-map.md) for its status.

# The schema, and the two places that claim it

Stated plainly: the canonical CDE JSON Schema exists in two repositories, under three filenames, and all three declare the same identifier.

- `RSNA/ACR-RSNA-CDEs` carries `cde.schema.json` at its repository root. `CDEStaging` names this file as the canonical schema and points authors at it.[^staging-readme] The file is byte-identical on the `master` branch and on the `next-gen-2026` branch, so the next-generation work has not changed it.[^acr-schema][^acr-schema-ng]
- `common_data_elements` carries `schema/cde.schema-1.0.json` and `schema/cde.schema-1.1.json`, and its README says the schemas are the ones "maintained at the development repo."[^cde-readme]

The upstream `cde.schema.json` is byte-identical to `cde.schema-1.1.json`, the newer of the two local copies. The definitions in the snapshot conform to version 1.0, which the README states explicitly.[^cde-readme] So the schema published as canonical upstream is a version ahead of the data published beside it.

All three files are JSON Schema draft-07 and all three declare the same `$id`:

```json
"$schema": "http://json-schema.org/draft-07/schema#",
"$ref": "#/definitions/element_set",
"$id": "https://github.com/ACR-RSNA-CDEs/blob/v1.0.0/cde.schema.json"
```

Version 1.1 did not update the identifier, so a consumer cannot tell the two versions apart by `$id`. The `schema_version` property inside a set or element is the only version signal, and its definition is identical in both files: a semantic version string, with no enumeration of permitted values.

## What changed between 1.0 and 1.1

Version 1.1 renames `status` to `current_status` and `history` to `status_history`, drops `index_codes` and the status history from the required list, and adds `images` and `modalities` to both the set and the element. The element gains `body_parts`. At the definitions level, 1.1 drops `event`, `biological_sex`, and `boolean_value`, and adds `modality`. [The schema comparison reference](/references/cde-schema-differences.md) has the field-by-field tables.

## RelaxNG against the API

Before the JSON Schema versions, the same object was described twice: by a RelaxNG schema kept with the set definitions, and by the de facto JSON the RadElement API returns. A 2023 note catalogued where the two disagreed, and that catalogue is migrated in full to [the schema comparison reference](/references/cde-schema-differences.md).

The differences fall into four groups: array wrapper naming, where the RelaxNG schema wraps repeated children in a container element and the API returns a plain array; `index_code.url` against the API's `href`; an [index code](/glossary/index-code.md) `system` enumeration constrained in the schema and apparently unconstrained in the API; and presence mismatches on `modality`, `biological_sex`, `age_range`, `parent_set`, `question`, `references`, and `body_parts`.

The JSON Schema versions close part of the gap and leave part of it open. `images`, `modalities`, `url`, and `body_parts` are now schema properties. `biological_sex` is defined in 1.0 and dropped in 1.1, and `age_range` appears in neither, so both remain unreconciled. That gap is the subject of `CDEStaging` issue 1, "Differences between radelement.org API schema and published Relax NG schema," open since 2023.

# CDE-labeled FHIR Observations

The idea that ties CDEs to the rest of OIDM is the [CDE-labeled FHIR Observation](/glossary/cde-labeled-fhir-observation.md): one radiology finding expressed as a FHIR [Observation](/glossary/observation.md) whose codes come from a CDE set, its elements, and their values.

`FHIRSamples` implements the pattern concretely in a lung cancer screening scenario.[^fhirsamples] An AI-produced finding Observation carries `code.coding` pointing at the `radelement.org` system with the set code `RDES195` for pulmonary nodule; each `component` entry carries an element code such as `RDE1717` with the chosen value code, for example `RDE1717.1`, as `valueCodeableConcept`. A second Observation repeats the same finding with `status` changed from `preliminary` to `final` to mark radiologist confirmation, and a third is `derivedFrom` both the imaging study and the radiologist's finding, carrying a Lung-RADS category (`RDES267`) as a component.

That chain, set code to element code to value code, all through one coding system, is what "CDE-labeled" means in practice. See [FHIR mapping](/data-structures/fhir-mapping.md) for where the current data structures stand against it, and [lineage repositories](/history/lineage-repositories.md) for the full example.

# How OIDM uses CDEs today

Four uses are visible in the current repositories.

**As an identifier namespace.** The ACR/RSNA Common Data Elements Project is a registered contributing organization in the finding model content, with the [organization code](/glossary/oidm-organization-code.md) `CDE`. Of the 2,382 published [finding model](/glossary/finding-model.md) definitions, 115 carry `OIFM_CDE_######` identifiers, meaning they were minted in that namespace. Their attributes carry `OIFMA_CDE_######` identifiers to match.

**As index codes.** Those same 115 definitions, and only those, carry a `RADELEMENT` [index code](/glossary/index-code.md) linking the finding model back to the set it came from. The whole finding model for small bowel obstruction is indexed like this:[^sbo-model]

```json
{
  "oifm_id": "OIFM_CDE_000178",
  "name": "Small Bowel Obstruction",
  "index_codes": [
    { "system": "RADELEMENT", "code": "RDES178", "display": "small bowel obstruction" }
  ]
}
```

Across the corpus, `RADELEMENT` is the smallest of the index code systems in use, at 115 occurrences against roughly 27,800 SNOMED and 25,800 RadLex codes.

**As a publication target.** `CDEStaging` holds informally authored candidate definitions "prior to their entering the review pipeline," and its finding roadmap links individual chest CT findings to the RadElement sets that already cover them. See [CDE staging](/semantic-foundation/common-data-elements/cde-staging.md).

**As the standards-track counterpart of finding models.** Finding models are authored quickly and are not balloted; CDEs are governed and are. [Finding models and CDEs](/semantic-foundation/finding-models/finding-models-and-cdes.md) covers the relationship.

One thing worth recording because it is easy to assume otherwise: the current extraction prototypes do not label with RadElement codes. `IPL-MVP-ExtractionAndLabeling` maps extracted findings to a curated list of 15 finding models keyed by OIFM identifier, with no `RDES` or `RDE` code anywhere in the repository,[^ipl-mvp] and the `imaging-problem-list` repository contains no RadElement codes either. The CDE-labeled Observation pattern is implemented in the lineage samples and documented, not in the working extraction pipelines.

# The next generation

A redesign of the CDE model is in progress on the `next-gen-2026` branch of `RSNA/ACR-RSNA-CDEs`. It replaces the set and element vocabulary with a graph of [FindingClass](/glossary/finding-class.md), [DataElement](/glossary/data-element.md), [Measurement](/glossary/measurement.md), and related node types. It is design work in an allied project, not an OIDM specification. See [the next-generation vocabulary](/semantic-foundation/common-data-elements/next-generation-vocabulary.md).

[^radelement-site]: RadElement, "Common Data Elements (CDEs) for Radiology"
[^radelement-api]: RadElement public sets API, read 2026-09-21
[^cde-readme]: common_data_elements README, the RadElement snapshot and its schema versions
[^cde-schema-10]: cde.schema-1.0.json, common_data_elements repository
[^cde-schema-11]: cde.schema-1.1.json, common_data_elements repository
[^acr-schema]: cde.schema.json on the master branch of ACR-RSNA-CDEs
[^acr-schema-ng]: cde.schema.json on the next-gen-2026 branch of ACR-RSNA-CDEs
[^staging-readme]: CDEStaging README, pointing at ACR-RSNA-CDEs for the canonical schema
[^fhirsamples]: FHIRSamples lung cancer screening example, CDE-coded FHIR Observations
[^sbo-model]: Small Bowel Obstruction finding model, OIFM_CDE_000178
[^ipl-mvp]: IPL-MVP-ExtractionAndLabeling curated finding model list, keyed by OIFM identifier
