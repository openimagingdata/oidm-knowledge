---
type: History
title: Lineage repositories
description: The twelve early OIDM repositories, what each one was for, what survives into current work, and what superseded the rest.
tags: [history, lineage, repositories, fhir]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T02:00:00Z }
sources:
  - id: oidm-py-observation
    resource: https://github.com/openimagingdata/OpenImagingDataModel.py/blob/455e5b68d730ea8829083d73064de0ec316d3c4a/openimagingdatamodel/observation/observation.py
    title: OpenImagingDataModel.py observation.py, the FHIR Observation model
  - id: oidm-py-fm
    resource: https://github.com/openimagingdata/OpenImagingDataModel.py/blob/455e5b68d730ea8829083d73064de0ec316d3c4a/openimagingdatamodel/cde_set/finding_model.py
    title: OpenImagingDataModel.py finding_model.py, the earliest FindingModel class
  - id: oidm-ts
    resource: https://github.com/openimagingdata/OpenImagingDataModel.ts/tree/7c97c33a23323358caa542973dc30d46b618d8a2
    title: OpenImagingDataModel.ts, the TypeScript reference implementation with Zod schemas
  - id: fhirsamples
    resource: https://github.com/openimagingdata/FHIRSamples/tree/9ae2fa934298e51789e355c9f4e0b71fabf6b5aa/lung_ca_screening_example
    title: FHIRSamples lung cancer screening example, four FHIR resources
  - id: usecases
    resource: https://github.com/openimagingdata/UseCases/blob/71a90d2ab2efeee4c4303dc0aef27ed3d70a6c99/Index.md
    title: UseCases Index.md, the living list of use case ideas
  - id: old-site-schema
    resource: https://github.com/openimagingdata/openimagingdata.org/blob/fb431dfc81801a5a8e621c0e8bf2acd20f74be7d/schemas/schema_differences.md
    title: openimagingdata.org schemas/schema_differences.md, CDE Set schema versus RadElement API
  - id: template-demo
    resource: https://github.com/openimagingdata/CDETemplateDemo/tree/e09f2553de58b2c88ea26e9673750a62803d4dbc
    title: CDETemplateDemo, Observation to prose rendering
  - id: sar
    resource: https://github.com/openimagingdata/SARTemplatesToCDEs/blob/3c15322eb1e0ba211558444207f56d8cd1b08c30/RectalCAStaging/Changes_vs_RDES11.md
    title: SARTemplatesToCDEs itemized CDE redesign for MR rectal tumor imaging
  - id: template-extraction
    resource: https://github.com/openimagingdata/template_extraction/tree/4d947d7e7557ce6187a35d592f8199d3abb673cf
    title: template_extraction, a corpus of RadReport templates
  - id: refiner
    resource: https://github.com/openimagingdata/ReportFindingRefiner/blob/3efd785aea30c455a3afd120d62da2c6af3d662d/README.md
    title: ReportFindingRefiner README, the retrieval-augmented extraction architecture
  - id: get-ontology
    resource: https://github.com/openimagingdata/get_ontology_findings/blob/574ec5e0afac2f4fbb97b4b68b6cf075337782cb/README.md
    title: get_ontology_findings README
  - id: ontology-tools
    resource: https://github.com/openimagingdata/ontology_tools/blob/8f558aa109f2c2b2773a6ecedfc12750e0bb1785/README.md
    title: ontology_tools README, the entire contents of the repository
  - id: cde-data
    resource: https://github.com/openimagingdata/common_data_elements/blob/35536d8c858bcd33e730a00c919edaef2e310a0b/README.md
    title: common_data_elements README, the RadElement snapshot and its schema versions
---

# Why this document exists

Twelve repositories came before the current three-layer structure. Some are dead ends; several hold the precedent that later work still follows, and one of them is still the project's CDE data source. Each section below gives the repository's purpose, its dates, its status in [the repository map](/repositories/repository-map.md), what survives, and what replaced it.

# The FHIR precedent

Two lineage repositories together define how OIDM maps onto FHIR, and nothing since has replaced them.

**The Observation class.** `OpenImagingDataModel.py` contains an explicit Pydantic re-implementation of the FHIR primitives `Identifier`, `Coding`, `CodeableConcept`, and `Reference`, and an `Observation` resource with `resourceType`, `code`, `status`, `subject`, `bodySite` as a `CodeableConcept`, `derivedFrom` as a list of references, and `component` as a discriminated union keyed on the FHIR `value[x]` naming convention.[^oidm-py-observation] Its docstring states plainly that the class models FHIR Observation objects. This is the direct ancestor of the [Observation](/data-structures/observation.md) in the current hierarchy.

**The worked example.** `FHIRSamples` holds four hand-built resources for a lung cancer screening scenario.[^fhirsamples]

| File | Resource | What it shows |
|---|---|---|
| `example1OIDMreport.json` | DiagnosticReport | Category coded in SNOMED CT and HL7 v2 table 0074, `code` coded LOINC 87279-6 for screening chest CT, an inline ImagingStudy, `result` referencing three Observations, and a SNOMED-coded conclusion |
| `example1OIDMaifinding.json` | Observation | An AI-produced finding, `status` `preliminary`, `code.coding` pointing at `radelement.org` with the CDE set code RDES195 for pulmonary nodule, `derivedFrom` the ImagingStudy, and `component` entries whose codes are individual RDE element codes with the chosen value code as `valueCodeableConcept` |
| `example1OIDMradiologist.json` | Observation | The same finding as confirmed by a radiologist, distinguished only by `status` `final` |
| `example1OIDMradiologistLungRADS.json` | Observation | A second-order assessment Observation that is `derivedFrom` both the ImagingStudy and the radiologist's finding Observation, carrying the Lung-RADS category (RDES267) as a component |

Three patterns come out of this example and recur throughout later work. The chain from CDE set code to element code to value code, all through the `radelement.org` coding system, is what "CDE-labeled FHIR Observation" means concretely. The `status` field is what separates a machine-produced finding from a radiologist-confirmed one, rather than a separate resource type. And the second-order observation, an assessment built on top of a finding observation, is the precedent for any later assessment or category modeling, including the reporting-system categories the [2026 roadmap](/roadmap/roadmap-2026.md) names.

Two absences in the example are worth recording. No `bodySite` coding appears on the finding Observations, because the anatomy was implicit in the CDE definition rather than explicit on the resource. No Patient resource is included; `subject.reference` is a bare reference. Both gaps are addressed in the current model, where [anatomic location](/glossary/anatomic-location.md) is an explicit field. See [FHIR mapping](/data-structures/fhir-mapping.md) for where the current structures stand.

# Reference implementations

**OpenImagingDataModel.ts.** Created 2023-04-27, last commit on the default branch 2023-10-22. A pnpm monorepo with `cde_set`, `observation`, and `findingModel` packages, all typed with Zod schemas.[^oidm-ts] Status: lineage. Its Zod schemas are the cleanest early type definitions for a CDE set, a CDE element, an index code, and a body part, and they are the only place the project expressed these shapes in TypeScript. No FHIR imports appear anywhere in it. Superseded by the Python implementation and then by the `findingmodel` package.

**OpenImagingDataModel.py.** Created 2024-03-08, last commit on the default branch 2024-11-13. Subpackages `cde_set` and `observation`.[^oidm-py-observation] Status: lineage, but the most consequential of the group. Besides the Observation class above, `finding_model.py` defines a `FindingModel` with a name, a description, and a list of attributes discriminated into choice and numeric types with a `required` flag.[^oidm-py-fm] Its docstring, "The definition of a radiology finding ... along with definitions of the relevant attributes that a radiologist might use to characterize the finding in a radiology report", survives verbatim into the current [finding model](/glossary/finding-model.md) class in `findingmodel`. What the early class lacked is exactly what the current format adds: identifiers, synonyms, tags, index codes, anatomic locations, and contributors. Its `set.py`, `element.py`, and `set_factory.py` mirror the RadElement schema. Superseded by the `findingmodel` package.

# Content and schema

**openimagingdata.org (the repository).** Created 2023-02-20, last commit 2023-06-27. Status: lineage. This is where the project's first name lives: the README titles it "Open Radiology Data Model" and points at a domain that no longer serves the project. Two things survive. The `schemas/` directory holds the CDE Set JSON schema and minimal sample CDE set and Observation fixtures. More useful is `schema_differences.md`, a precise gap analysis between the CDE Set RelaxNG schema and the RadElement JSON API: array wrapper naming, `index_code.url` against the API's `href`, a `system` enum constrained in the schema but not the API, authors interleaved in the schema but split into arrays in the API, and presence mismatches on modality, biological sex, age range, parent set, question, references, and body parts.[^old-site-schema] That analysis is still live; the same gap is the subject of an open issue in `CDEStaging`. See [CDEs and RadElement](/semantic-foundation/common-data-elements/cdes-and-radelement.md). Superseded as a site by the hosted blog at the same domain.

**common_data_elements.** Created 2025-02-21, content uploaded 2025-06-04. Status: maintenance, not lineage: this is still the project's local snapshot of RadElement. It holds roughly 140 CDE set definitions as JSON, indexed in the README by clinical topic with their set identifiers, and the canonical `cde.schema-1.0.json` and `cde.schema-1.1.json` files that the gap analysis above refers to.[^cde-data] The README notes that the definitions conform to schema version 1.0, not the newer 1.1.

**UseCases.** Created 2023-09-07, last commit 2024-02-26. Status: lineage as an activity, but its content is the fullest enumeration of application ideas anywhere in the project.[^usecases] It holds roughly 25 one-line use case ideas and the six value categories used to tag them. Migrated in full to [the use case catalog](/history/use-cases.md). Nothing superseded it; the deck's application pillar and the [2026 roadmap](/roadmap/roadmap-2026.md) cover related ground without reusing the catalog.

# Demonstrations and conversions

**CDETemplateDemo.** Created 2023-05-31, last commit 2023-06-15, default branch `master`. Status: lineage. A working proof of concept that renders a structured Observation into report prose through a Mustache template.[^template-demo] The pattern survives as the clearest precedent for the reporting SDK direction; see [CDE template rendering](/history/cde-template-rendering.md). Its own Observation shape, a flat string-keyed record of components, is looser than the FHIR-based one and is superseded by it.

**SARTemplatesToCDEs.** Created 2023-12-30, last commit 2024-03-11. Status: lineage, stalled at proof of concept. The stated goal was to use a language model to convert Society of Abdominal Radiology reporting templates into CDE sets, starting with rectal cancer staging. No conversion code was committed. What survives is `Changes_vs_RDES11.md`, an itemized redesign of the MR rectal tumor imaging CDE set against a 2016 baseline: an element renamed, mucinous composition given finer granularity, T-category and sphincter-invasion elements restructured, and new elements for tumor morphology, extramural vascular invasion, tumor deposits, and lymph nodes, each with explicit value sets.[^sar] It remains the most detailed single-CDE-set redesign in the lineage. The conversion approach itself is superseded by the batch content pipelines in `findingmodels`; see [extraction approaches](/history/extraction-approaches.md).

# Extraction and ontology tooling

These four are covered in depth in [extraction approaches](/history/extraction-approaches.md); their status is summarized here.

**template_extraction.** Created 2025-06-05, last commit 2025-06-16. Status: lineage. A short script and a corpus of 281 RadReport templates spanning CT, MR, ultrasound, nuclear medicine, and fluoroscopy across most body regions, plus two CDE-labeled test templates.[^template-extraction] The corpus is the asset; it is an unused candidate vocabulary for exam types as well as findings. Not superseded by anything; the work simply moved to converting CDE staging content instead.

**ReportFindingRefiner.** Created 2024-12-31, last commit 2025-05-23. Status: lineage, and the most mature of the extraction family. A privacy-first pipeline running local models: ingest report text, split into header, findings, and impression sections, embed with sentence transformers, store in a vector database, search, then generate finding model outlines with a local language model and persist them.[^refiner] Superseded by the extraction platform on the `imaging-problem-list` `dev` branch, which pursues the same goal with a chunked, multi-provider, verbatim-quote-validated design.

**get_ontology_findings.** Created 2025-03-27, last commit 2025-03-27. Status: lineage. A minimal script plus a RadLex export, aimed at finding ontology entries that correspond to imaging findings so they can become finding models or CDEs.[^get-ontology] Superseded in scope by `med-ontology-lookup`.

**ontology_tools.** Created 2025-03-02, last commit 2025-03-02. Status: dead. The repository contains a README naming three target ontologies, Anatomic Locations, SNOMED CT, and RadLex, and nothing else.[^ontology-tools] `med-ontology-lookup` is a replacement, not a continuation; there is nothing here to carry forward except the three-ontology scope statement, which that project widened to five.

# What connects them

No lineage repository depends on another as a package, and none names another by URL. The connective tissue is shared external vocabulary: RadElement set and element codes thread through the CDE snapshot, the FHIR samples, the TypeScript sample data, the template demo's sample observations, and the SAR redesign. The CDE set and element shape is independently re-implemented three times. The finding model concept is defined independently in the TypeScript and Python implementations with near-identical shape and reimplemented a third time inside `ReportFindingRefiner`. That independent convergence is why the current format could consolidate them without contradiction.

[^oidm-py-observation]: OpenImagingDataModel.py observation.py, the FHIR Observation model
[^oidm-py-fm]: OpenImagingDataModel.py finding_model.py, the earliest FindingModel class
[^oidm-ts]: OpenImagingDataModel.ts, the TypeScript reference implementation with Zod schemas
[^fhirsamples]: FHIRSamples lung cancer screening example, four FHIR resources
[^usecases]: UseCases Index.md, the living list of use case ideas
[^old-site-schema]: openimagingdata.org schemas/schema_differences.md, CDE Set schema versus RadElement API
[^template-demo]: CDETemplateDemo, Observation to prose rendering
[^sar]: SARTemplatesToCDEs itemized CDE redesign for MR rectal tumor imaging
[^template-extraction]: template_extraction, a corpus of RadReport templates
[^refiner]: ReportFindingRefiner README, the retrieval-augmented extraction architecture
[^get-ontology]: get_ontology_findings README
[^ontology-tools]: ontology_tools README, the entire contents of the repository
[^cde-data]: common_data_elements README, the RadElement snapshot and its schema versions
