---
type: Data Structure
title: Observation
description: "The atomic unit of OIDM: one finding, seen or explicitly excluded, on one exam, with its location and attribute values, as it exists today inside an Exam Finding List and in the extraction pipeline."
tags: [data-structures, observation, presence, extraction]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
sources:
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: "Open Imaging Data Model 2026 Status Update: Realizing Object-Oriented Imaging Results, January 2026"
  - id: ipl-main-claude
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/CLAUDE.md
    title: imaging-problem-list domain model notes, main branch
  - id: ipl-claude-dev
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/CLAUDE.md
    title: imaging-problem-list domain model notes, dev branch
  - id: efl-sample
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/sample_data/example2/xr_shoulder_20210522_efl.json
    title: An Exam Finding List with anatomic locations, imaging-problem-list dev branch
  - id: extract-models
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/src/finding_extractor/models.py
    title: Extraction Pydantic models, imaging-problem-list dev branch
  - id: extract-plan
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/initial-extraction-plan.md
    title: Initial extraction plan, imaging-problem-list dev branch
  - id: lineage-obs
    resource: https://github.com/openimagingdata/OpenImagingDataModel.py/blob/455e5b68d730ea8829083d73064de0ec316d3c4a/openimagingdatamodel/observation/observation.py
    title: Observation model, OpenImagingDataModel.py
  - id: fhir-sample
    resource: https://github.com/openimagingdata/FHIRSamples/blob/9ae2fa934298e51789e355c9f4e0b71fabf6b5aa/lung_ca_screening_example/example1OIDMaifinding.json
    title: An AI-produced finding Observation, FHIRSamples lung cancer screening example
  - id: issue1
    resource: https://github.com/openimagingdata/imaging-problem-list/issues/1
    title: imaging-problem-list issue 1, "Create System of Data Models"
---

# What an observation is

An [observation](/glossary/observation.md) is one finding, seen or explicitly excluded, on one exam. The deck frames it as "what + where + attributes": a finding tag, an [anatomic location](/glossary/anatomic-location.md), and lesion characteristics, carrying presence indicators, change from prior, and measurements, in "a universal structure across systems."[^deck]

Two of those three parts point at the [semantic foundation](/semantic-foundation/). The "what" is a [finding model](/glossary/finding-model.md) identifier. The "where" is a RadLex identifier. Only the "how" is local to the observation, and even there each [attribute](/glossary/attribute.md) and each chosen value carry codes from the finding model's own definition.

A negative observation is an observation. Absence is recorded the same way presence is, with a presence attribute whose value is `absent`, because a radiologist stating "no fracture" has actively looked and not found. That commitment is what makes the [Imaging Problem List](/data-structures/imaging-problem-list.md) able to distinguish a finding nobody checked for from one that was checked for and ruled out.

# The concrete form today

There is no standalone Observation record. An observation is one entry in the `findings` array of an [Exam Finding List](/data-structures/exam-finding-list.md).[^ipl-main-claude]

| Field | Type | Required | What it carries |
|---|---|---|---|
| `observationId` | string | yes | identity within this list. Repeat instances get separate identifiers. |
| `findingCode` | `OIFM_[A-Z]{3,4}_[0-9]{6}` | yes | the [OIFM](/glossary/oifm.md) identifier of the finding model |
| `findingDescription` | string | yes | the finding model's display name |
| `attributes[]` | array | yes | one entry per characterized attribute; see below |
| `anatomicLocation` | `{locationId, locationDisplay}` | optional, development branch only | a [RadLex identifier](/glossary/radlex-id.md) from the `anatomic-locations` package, omitted when the finding is not anatomically localizable[^ipl-claude-dev] |
| `reportText` | string | optional | the verbatim span of the report the observation came from |

Each entry in `attributes[]` carries four fields: `attributeCode`, an `OIFMA_[A-Z]{3,4}_[0-9]{6}` identifier; `attributeDescription`, its display name; `attributeValueCode`, the attribute code plus a dot suffix; and `attributeValueDescription`.

```json
{
  "observationId": "acromioclavicular_degenerative_changes_1",
  "findingCode": "OIFM_GMTS_025663",
  "findingDescription": "degenerative joint changes",
  "attributes": [
    {
      "attributeCode": "OIFMA_GMTS_265084",
      "attributeDescription": "presence",
      "attributeValueCode": "OIFMA_GMTS_265084.1",
      "attributeValueDescription": "present"
    }
  ],
  "anatomicLocation": {
    "locationId": "RID42239",
    "locationDisplay": "left acromioclavicular joint"
  },
  "reportText": "Mild degenerative changes of the acromioclavicular joint with joint space narrowing and small osteophytes."
}
```

That record is the first finding of a left shoulder radiograph in the sample data.[^efl-sample] A full list in context is in [the Exam Finding List example](/references/exam-finding-list-example.md).

## Presence and the dot codes

[Presence](/glossary/presence.md) is the attribute every observation carries. Its values in the sample data are `present`, `absent`, and `indeterminate`.

Value codes are positional, not semantic: a value code is the attribute identifier plus a dot and the value's zero-based position in the finding model's value list. Consuming code in the extraction repository documents the standard ordering as "`.1` = present, `.0` = absent."[^ipl-claude-dev] That ordering holds for the large majority of published finding models but not all of them, so a consumer that hard-codes `.1` as present is wrong for the minority that order their values differently. The [presence glossary entry](/glossary/presence.md) records the counts and the conflict.

## Repeat instances

"The same finding type may appear multiple times in one exam (e.g., multiple kidney stones). Each instance gets a separate entry with its own `observationId`."[^ipl-main-claude] Count is therefore expressed by the number of observations, not by a count attribute, at the Exam Finding List level. The problem list re-collapses them: several observations of one finding from one exam display as a single dated row.

# The extraction-time observation

The extraction platform on the development branch has its own Pydantic model for a finding as language models produce it, before any code assignment. It is a different object from the Exam Finding List entry and is worth reading as the pre-coding form of the same thing.[^extract-models]

| Model | Fields |
|---|---|
| `Finding` | `finding_name`, `presence`, `location`, `attributes[]`, `report_text`, `source_section`, `coding` |
| `FindingLocation` | `body_region`, `specific_anatomy`, `laterality` |
| `FindingAttribute` | `key`, `value` |
| `ExtractedReportFindings` | `exam_info`, `findings[]`, `non_finding_text[]` |

Three differences from the coded form matter.

**The presence vocabulary is wider.** `presence` is a `Literal["present", "absent", "indeterminate", "possible"]`, and the design note explains the fourth value: "'possible' covers hedged language like 'raising the possibility of', 'suggestive of', 'cannot exclude'."[^extract-models][^extract-plan] There is no `possible` in the finding model presence value set, so the extra value has no coded counterpart and must be resolved before an Exam Finding List entry can be written.

**Location is free text, not a code.** `FindingLocation` carries a constrained `body_region`, a free-text `specific_anatomy`, and a laterality. Turning that into a `locationId` is the job of the separate post-extraction coding pass, governed by [the anatomic location assignment rules](/data-structures/anatomic-location-assignment-rules.md).

**Attributes are loose key-value pairs.** `FindingAttribute` is a `key` and a `value` as strings, with standard keys named in the model docstring: size, acuity, change from prior, severity, count, and morphology.[^extract-models] Those are not OIFMA codes and carry no value codes.

The model is also where coding results land. A `FindingCodingBundle` on each finding records the chosen OIFM identifier, the method used (`fast-path`, `llm`, or `unresolved`), a reason when unresolved, and the candidate codes that were considered. The pipeline that produces it is described in [finding and location coding](/applications/finding-and-location-coding.md).

The mapping from the extraction model to the Exam Finding List entry is therefore not a rename. It is a coding step:

| Extraction field | Exam Finding List field | How |
|---|---|---|
| `finding_name` | `findingCode`, `findingDescription` | finding coding against the finding model corpus |
| `presence` | an `attributes[]` entry | resolve to the finding model's presence attribute and dot-suffixed value code |
| `location` | `anatomicLocation` | location coding against the `anatomic-locations` index |
| `attributes[]` | remaining `attributes[]` entries | no automated mapping is documented |
| `report_text` | `reportText` | carried through verbatim |

# The FHIR precedent

The 2024 reference implementation modelled an observation as a FHIR `Observation` directly. Its docstring states "the Observation class is the model for FHIR Observation objects," and the class carries `resourceType`, `code`, `status`, `subject`, `bodySite` as a `CodeableConcept`, `derivedFrom` as references, and `component` as a discriminated union of codeable-concept, string, integer, and boolean variants keyed on the FHIR `value[x]` naming convention.[^lineage-obs]

The lung cancer screening samples show the same shape with real codes. A finding observation's `code` is a [CDE set](/glossary/cde-set.md) identifier under `https://radelement.org`, each `component` code is a [CDE element](/glossary/cde-element.md) identifier, and each component's `valueCodeableConcept` gives the chosen value code.[^fhir-sample] In those samples `status` is what separates a machine-produced finding from a radiologist-confirmed one: `preliminary` for the AI observation, `final` for the radiologist's, with no change to the resource type. That distinction is the closest thing in the project's history to a [provenance](/glossary/provenance.md) marker on an observation, and it is what the Exam Finding List specification asks for when it says "each Observation should include some kind of provenance marker." See [FHIR mapping](/data-structures/fhir-mapping.md).

# What is missing

There is no Observation model, no JSON Schema, and no standalone record. Issue 1 in the extraction repository states the gap and the intended shape: Pydantic models for Observation, with a possible "Extracted Observation" subtype, alongside the Exam Finding List and Imaging Problem List, with "extensive annotation to generate JSON schemas" and camelCase aliases on export against snake_case attributes internally.[^issue1] The issue is open and unclaimed by any current plan. The Extracted Observation subtype it floats is exactly the distinction described above, between what a language model produced and what has been coded.

[^deck]: "Open Imaging Data Model 2026 Status Update", January 2026
[^ipl-main-claude]: imaging-problem-list domain model notes, main branch
[^ipl-claude-dev]: imaging-problem-list domain model notes, dev branch
[^efl-sample]: An Exam Finding List with anatomic locations, dev branch
[^extract-models]: Extraction Pydantic models, dev branch
[^extract-plan]: Initial extraction plan, dev branch
[^lineage-obs]: Observation model, OpenImagingDataModel.py
[^fhir-sample]: An AI-produced finding Observation, FHIRSamples
[^issue1]: imaging-problem-list issue 1, "Create System of Data Models"
