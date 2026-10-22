---
type: Reference
title: Existing building blocks for exam types
description: Everything that exists today across the OIDM repositories that a future exam type layer could stand on, with its source, its status, and what it does not do.
tags: [semantic-foundation, exam-types, loinc, playbook, reference]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:30:00Z }
sources:
  - id: molu-roadmap
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/docs/product-roadmap.md
    title: med-ontology-lookup product roadmap, domain profiles and the LOINC/RSNA Radiology Playbook section
  - id: molu-detect
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/src/med_ontology_lookup/detect.py
    title: Input kind detection, med-ontology-lookup
  - id: molu-config
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/src/med_ontology_lookup/config.py
    title: Default ontologies and source abbreviation maps, med-ontology-lookup
  - id: radlex-owl
    resource: https://github.com/RSNA/RadLex/blob/d53bd9c666ebaef280f82a4eed02e755a1552d30/RadLex.owl
    title: RadLex OWL file, RSNA RadLex repository, main branch
  - id: ipl-efl
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/sample_data/example2/ct_abdomen_20210826_efl.json
    title: Exam Finding List sample with a LOINC-coded exam header, imaging-problem-list dev branch
  - id: viewer-map
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/viewer/data/exam_type_mappings.json
    title: Viewer exam type display mapping table, imaging-problem-list dev branch
  - id: ipl-rules
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/anatomic-location-assignment-rules.md
    title: Anatomic location assignment rules, imaging-problem-list dev branch
  - id: region-map
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/viewer/data/finding_region_mappings.json
    title: Finding to body region mapping table, imaging-problem-list dev branch
  - id: templates
    resource: https://github.com/openimagingdata/template_extraction/tree/4d947d7e7557ce6187a35d592f8199d3abb673cf/templates
    title: RadReport template corpus, template_extraction repository
  - id: cde-schema
    resource: https://github.com/openimagingdata/openimagingdata.org/blob/fb431dfc81801a5a8e621c0e8bf2acd20f74be7d/schemas/schema_differences.md
    title: Differences between the CDE set schema and the RadElement API, openimagingdata.org repository
---

# What this catalogues

No exam type artifact exists; see [exam types](/semantic-foundation/exam-types/overview.md) for the goals that have been stated for one. This page lists what does exist, so that a future effort starts from an accurate inventory rather than from scratch. Every row is a fact about a file or a running behaviour, with its source pinned. Nothing here is a design.

| Building block | Where it lives | Status |
|---|---|---|
| The `radiology` domain profile, making the Playbook first-class | `med-ontology-lookup` product roadmap | Written design, not implemented |
| LOINC search, code detection, and crosswalk | `med-ontology-lookup` library and CLI | Implemented |
| Playbook provenance strings on RadLex concepts | RadLex OWL file | Present as free text, not as links |
| LOINC-coded exam headers on Exam Finding Lists | `imaging-problem-list` specification and sample data | Implemented, eight distinct codes in the data |
| Exam type display shortening table | `imaging-problem-list` viewer | Implemented, keyed by description string |
| Exam-scoped coarse region fallback and sided-exam laterality | `imaging-problem-list` assignment rules | Written rules, applied by the coding pass |
| A corpus of 281 real exam-named report templates | `template_extraction` | Raw text, uncoded |
| LOINC permitted as an index code system, plus modality and body part fields | CDE set schema and RadElement API | External schema, already in use |

# The radiology profile design

The most developed written design for exam type support is in the terminology tool's product roadmap, which proposes replacing an ever-growing default search with named, inspectable domain profiles. The `radiology` profile is the default one, and LOINC belongs in it because radiology "orderables live in the LOINC/RSNA Radiology Playbook, while findings, anatomy, and report language live in RadLex."[^molu-roadmap]

The profile is specified as RadLex, LOINC weighted toward the Playbook, [SNOMED CT](/glossary/snomed-ct.md), and [FMA](/glossary/fma.md), with [UMLS](/glossary/umls.md) as the crosswalk hub, covering findings, anatomy, and imaging procedures or orderables. A separate `laboratory` profile would use the rest of LOINC without the Playbook bias, and a `billing-us` profile holding CPT and ICD codes is kept explicitly out of the radiology default and gated on licensing.

Four implications for the Playbook are stated.[^molu-roadmap]

- Rank procedure and orderable queries toward LOINC Playbook terms, and finding and anatomy queries toward RadLex, SNOMED CT, and FMA.
- Teach the crosswalk the Playbook correspondences, linking a LOINC code to its historic `RPID` and to RadLex anatomy and modality attributes, and say so in the mapping provenance.
- Detect `RPID` codes as well as LOINC-shaped codes.
- Do not treat every LOINC hit as radiology; prefer the Playbook or radiology class when the profile is `radiology`.

None of this is built. The roadmap is a planning document in the repository, not a released capability. See [med-ontology-lookup](/semantic-foundation/terminologies/med-ontology-lookup.md) for what the tool does today.

# LOINC handling that is implemented

LOINC is one of the four BioPortal ontologies the lookup tool queries by default, alongside RadLex, SNOMED CT, and FMA, and it maps to the UMLS source abbreviation `LNC` for crosswalks.[^molu-config] The auto-detecting `molu lookup` command recognizes a LOINC code by shape, using a pattern of one to seven digits, a hyphen, and one or two digits, and returns it with LOINC as the ontology hint.[^molu-detect]

What is absent is equally worth recording. There is no `RPID` pattern in the detector, no Playbook weighting in ranking, no profile mechanism, and no parsing of a LOINC radiology code into its modality, body part, or technique axes.

# Playbook provenance inside RadLex

RadLex records where a concept came from in a free-text `Source` annotation. In the RadLex OWL file published in the RSNA repository, 997 of 3,116 `Source` annotation values mention the Playbook, written 23 different ways. The plain value `Playbook` accounts for 913 of them; the rest combine it with another source, as in `LOINC, Playbook`, `LI-RADS, Playbook`, or `Fleischner Society, Playbook`, and three are the misspelling `PLaybook`.[^radlex-owl]

This is provenance, not linkage. The annotation says a concept entered RadLex by way of the Playbook. It carries no LOINC code, no `RPID`, and no relationship that could be traversed from an exam type to the anatomy it covers.

# LOINC codes in the sample data

The `imaging-problem-list` repository carries twelve Exam Finding Lists as sample data, duplicated into the viewer's data directory, and the Imaging Problem Lists built from them. Eight distinct LOINC codes appear. The counts below are of Exam Finding Lists in `sample_data`, which are the same twelve exams the viewer serves, and of observation entries across all Imaging Problem List files in the repository.

| LOINC code | Description in the data | Exam Finding Lists | Observation entries |
|---|---|---|---|
| `36952-0` | CT Abdomen and Pelvis WO contrast | 3 | 312 |
| `36813-4` | CT Abdomen and Pelvis W contrast IV | 1 | 144 |
| `30745-4` | XR Chest | 2 | 120 |
| `29252-4` | CT Chest WO contrast, also CT Chest Without Contrast | 2 | 107 |
| `24587-8` | MR Brain WO and W contrast IV | 1 | 68 |
| `24558-9` | US Abdomen | 1 | 63 |
| `26158-6` | XR Shoulder - left | 1 | 27 |
| `72133-2` | CT Abdomen and Pelvis Without Contrast | 1 | 12 |

Two inconsistencies are visible in that table and are recorded here as facts about the data. One code, `29252-4`, carries two different description strings in different files. And two different codes, `36952-0` and `72133-2`, carry descriptions that name the same study, an abdomen and pelvis CT without contrast. Both are the kind of thing a curated exam type list would resolve; neither is resolved today. They are raised in [open questions](/roadmap/open-questions.md).

An exam header looks like this in an Exam Finding List.[^ipl-efl]

```json
"examInfo": {
  "studyIdentifier": "CT_ABDOMEN_20210826",
  "studyDateTime": "2021-08-26T10:00:00Z",
  "studyLoincCode": "36952-0",
  "studyDescription": "CT Abdomen and Pelvis WO contrast"
}
```

# The viewer display table

The viewer shortens exam descriptions for its timeline through a seven-entry lookup table, mapping "MR Brain WO and W contrast IV" to "MR Brain w/wo", "CT Abdomen and Pelvis WO contrast" to "CT AbdPel wo", and similarly for the other five.[^viewer-map] The table is keyed by the description string rather than the LOINC code, so the two description strings that appear in the data without an entry, "CT Chest Without Contrast" and "CT Abdomen and Pelvis Without Contrast", fall through unshortened. This is the closest thing in the repositories to a preferred display name per exam type, and it is a presentation convenience of one application.

# The exam-scoped region fallback

The anatomic location assignment rules define a small exam-to-region map in RadLex identifiers, used only when a finding has no anatomic noun at all.[^ipl-rules]

| Exam | Coarse region | RadLex identifier |
|---|---|---|
| CT Abdomen, CT Abdomen and Pelvis | abdomen | `RID56` |
| CT Chest, XR Chest | thorax | `RID1243` |
| MR Brain | head | `RID9080` |
| Shoulder | shoulder | `RID39518` |

The table is explicitly partial, ending in "etc.", and it is keyed by exam name rather than by LOINC code. The rules attach three conditions to it: a combined abdomen and pelvis exam defaults to abdomen unless the text points pelvic; the grain is the coarse region and not a substructure, so "no soft tissue mass" on a chest CT resolves to thorax rather than chest wall; and a finding with a named target organ always takes the organ over the exam region, "especially edge-of-exam cases," so "lung bases clear" on an abdominal CT resolves to lung. Laterality follows the same shape, with a sided exam siding its findings and a non-sided exam never introducing a side.

A companion table in the viewer maps finding names to body regions, with `"regions": "ALL"` for findings such as atherosclerosis that can appear anywhere.[^region-map] It runs on finding names rather than codes and is an application data file, not part of the specification.

# The RadReport template corpus

The `template_extraction` repository holds 281 radiology report templates as plain text files, each named for the exam it belongs to.[^templates] The names are real-world exam vocabulary at the granularity a department uses: "CT Chest PE", "CT Abdomen & Pelvis w Contrast", "MRA Neck", "US Pelvis", "Cardiac MRI: Adenosine Stress Protocol", "XRay Wrist-Hand - Avulsion Fracture". Some are procedure-specific rather than exam-specific, such as "Chest Tube Removal" or "AAST Liver Injury Grade".

The corpus is uncoded. No LOINC code, Playbook identifier, or body part list is attached to any template; the repository's purpose was extracting finding definitions from the template bodies, described in [extraction approaches](/history/extraction-approaches.md). Its value here is as a vocabulary of exam names that a curated preferred-entry list would have to cover.

# LOINC in the CDE schema

The [CDE set](/glossary/cde-set.md) schema used upstream of [RadElement](/glossary/radelement.md) already admits LOINC as a coding system: the RelaxNG schema "specifies that `<system>` may be `RADLEX`, `SNOMEDCT`, or `LOINC`," while the RadElement API does not appear to constrain the value.[^cde-schema] The same comparison records that the set definition carries a complex `modality` structure in the schema and a `body_parts` field in the API, the two axes an exam type would coordinate. The full extract is at [CDE set schema versus the RadElement API](/references/cde-schema-differences.md).

[^molu-roadmap]: med-ontology-lookup product roadmap
[^molu-detect]: Input kind detection, med-ontology-lookup
[^molu-config]: Default ontologies and source abbreviation maps, med-ontology-lookup
[^radlex-owl]: RadLex OWL file, RSNA RadLex repository
[^ipl-efl]: Exam Finding List sample, imaging-problem-list dev branch
[^viewer-map]: Viewer exam type display mapping table
[^ipl-rules]: Anatomic location assignment rules, imaging-problem-list dev branch
[^region-map]: Finding to body region mapping table
[^templates]: RadReport template corpus, template_extraction repository
[^cde-schema]: Differences between the CDE set schema and the RadElement API
