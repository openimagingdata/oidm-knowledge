---
type: Concept
title: FHIR mapping
description: Everything OIDM has documented about representing its data structures in FHIR, from the CDE-labeled Observation pattern of the lineage repositories to the current Exam Finding List and Imaging Problem List mappings, and the plain fact that no current code emits FHIR.
tags: [data-structures, fhir, observation, cde, mapping]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
sources:
  - id: ipl-main
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/README.md
    title: imaging-problem-list README, main branch, where both mappings are stated
  - id: ipl-claude-dev
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/CLAUDE.md
    title: imaging-problem-list domain model notes, dev branch
  - id: lineage-obs
    resource: https://github.com/openimagingdata/OpenImagingDataModel.py/blob/455e5b68d730ea8829083d73064de0ec316d3c4a/openimagingdatamodel/observation/observation.py
    title: Observation model, OpenImagingDataModel.py
  - id: fhir-report
    resource: https://github.com/openimagingdata/FHIRSamples/blob/9ae2fa934298e51789e355c9f4e0b71fabf6b5aa/lung_ca_screening_example/example1OIDMreport.json
    title: The lung cancer screening DiagnosticReport, FHIRSamples
  - id: fhir-ai
    resource: https://github.com/openimagingdata/FHIRSamples/blob/9ae2fa934298e51789e355c9f4e0b71fabf6b5aa/lung_ca_screening_example/example1OIDMaifinding.json
    title: The AI-produced finding Observation, FHIRSamples
  - id: fhir-lungrads
    resource: https://github.com/openimagingdata/FHIRSamples/blob/9ae2fa934298e51789e355c9f4e0b71fabf6b5aa/lung_ca_screening_example/example1OIDMradiologistLungRADS.json
    title: The Lung-RADS assessment Observation, FHIRSamples
  - id: powerscribe
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/sample_data/example1/powerscribe-fhir.json
    title: powerscribe-fhir.json, a real input DiagnosticReport in the imaging-problem-list sample data
  - id: site-findings
    resource: https://www.openimagingdata.org/findings-cdes-and-observations/
    title: '"Findings, CDEs, and Observations", openimagingdata.org, 2023-06-24'
  - id: site-about
    resource: https://www.openimagingdata.org/about/
    title: openimagingdata.org About page
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: "Open Imaging Data Model 2026 Status Update, January 2026"
---

# The stance

OIDM's position on FHIR is stated in the deck's call to action as two words: **structure first**, with FHIR and other standards following.[^deck] The project builds "functional data structures that can then be expressed in FHIR and other standards" rather than starting from the standard and working back. That ordering explains the state of everything below: the mappings are written down carefully, they have precedent in working examples, and no current code produces them.

# The founding pattern: the CDE-labeled FHIR Observation

The project began from FHIR rather than beside it. Its About page defines the unit of radiology data as a "[CDE-labeled FHIR Observation](/glossary/cde-labeled-fhir-observation.md) object", and the 2023 post that set the direction works the idea through with a pulmonary nodule.[^site-about][^site-findings]

## The worked example

`FHIRSamples` holds four hand-built resources for a lung cancer screening scenario. They remain the clearest statement of the pattern.

**The report.** A [FHIR DiagnosticReport](/glossary/fhir-diagnostic-report.md) with `category` coded in SNOMED CT and HL7 v2 table 0074, `code` coded as [LOINC](/glossary/loinc.md) `87279-6` for a screening chest computed tomography, an inline `ImagingStudy`, `result` referencing three Observations, and a `conclusion` with a SNOMED `conclusionCode`.[^fhir-report]

**The finding.** An [Observation](/glossary/observation.md) whose `code` is a [CDE set](/glossary/cde-set.md) identifier under the `https://radelement.org` system, `RDES195` for pulmonary nodule, with `derivedFrom` pointing at the imaging study and `component` entries whose codes are individual [CDE element](/glossary/cde-element.md) identifiers and whose `valueCodeableConcept` gives the chosen value code.[^fhir-ai]

```json
{
  "resourceType": "Observation",
  "code": { "coding": [{ "system": "https://radelement.org", "code": "RDES195", "display": "Pulmonary Nodule" }] },
  "status": "preliminary",
  "derivedFrom": [{ "reference": "ImagingStudy/example1OIDMstudy" }],
  "component": [
    { "code": { "coding": [{ "code": "RDE1717" }] },
      "valueCodeableConcept": { "coding": [{ "code": "RDE1717.1" }] } }
  ]
}
```

Three patterns come out of it.

**Set code, element code, value code.** The chain from `RDES195` to `RDE1717` to `RDE1717.1`, all through one coding system, is what "CDE-labeled" means concretely. The current [Exam Finding List](/data-structures/exam-finding-list.md) uses the identical chain with a different vocabulary: `OIFM` identifier, `OIFMA` identifier, dot-suffixed value code.

**Status carries provenance.** The example has the same finding twice, once as an AI observation with `status` `preliminary` and once as the radiologist's with `status` `final`. The two resources are otherwise identical. Distinguishing a machine-produced finding from a confirmed one is a field value, not a separate resource type.[^fhir-ai] That is the closest precedent for the "provenance marker" the Exam Finding List specification asks for, and it is also exactly the ACR priority the deck names, correlating artificial intelligence observations against radiologist observations.[^deck]

**Assessments are second-order observations.** A fourth resource carries the Lung-RADS category as a component of `RDES267`, and its `derivedFrom` points at both the imaging study **and** the radiologist's finding Observation.[^fhir-lungrads] An assessment built on top of a finding is an Observation referring to an Observation. That is the precedent for any future modelling of the reporting-system categories the roadmap names.

Two absences in the example are worth recording. No `bodySite` appears on the finding Observations, because anatomy was implicit in the CDE definition rather than explicit on the resource. No Patient resource is included; `subject.reference` is a bare reference.

## The Python model

The 2024 reference implementation encodes the same shape in Pydantic. `observation.py` re-implements the FHIR primitives `Identifier`, `Coding`, `CodeableConcept`, and `Reference`, and defines an `Observation` with `resourceType`, `code`, `status`, `subject`, `bodySite` as a `CodeableConcept`, `derivedFrom` as a list of references, and `component` as a discriminated union of codeable-concept, string, integer, and boolean variants named after the FHIR `value[x]` convention.[^lineage-obs] Its docstring says so plainly: "The Observation class is the model for FHIR Observation objects."

`bodySite` is present in the class even though the samples do not use it, which is the field the current model's explicit [anatomic location](/glossary/anatomic-location.md) would occupy. Both are covered in [lineage repositories](/history/lineage-repositories.md).

# The current mappings

Both current structures have a documented FHIR encoding, stated in the `imaging-problem-list` README and repeated in its domain notes on both branches.[^ipl-main][^ipl-claude-dev]

| Structure | Documented FHIR encoding |
|---|---|
| [Exam Finding List](/data-structures/exam-finding-list.md) | "**DiagnosticReport** containing a list of **Observation** objects, with a finding code on each Observation and a list of components with attribute codes and values (especially present/absent and change from prior)" |
| [Imaging Problem List](/data-structures/imaging-problem-list.md) | "**Report** containing a list of **Condition** objects (labeled with the finding identifier), where each Condition object also contains a list of **Observation** objects which document which exams (**DiagnosticReports**) the finding type has been documented on, including the exam date and exam type (LOINC type)" |

Field by field, the Exam Finding List mapping is close to mechanical. `diagnosticReportId` is the DiagnosticReport identifier, `examInfo.studyLoincCode` is its `code`, each `findings[]` entry is one Observation with `findingCode` as its `code`, each `attributes[]` entry is one `component`, and `anatomicLocation` is the `bodySite` the lineage class already has. The problem list mapping introduces one resource that has no OIDM counterpart, the [FHIR Condition](/glossary/fhir-condition.md), standing for one finding type in one patient, and one container, "Report", that is not a FHIR resource name.

# What is actually implemented

Nothing. A search for `DiagnosticReport` or `fhir` across the extraction platform's entire source tree on the development branch returns no matches. No FHIR resource classes exist anywhere in the current Python code, and no OIDM tool emits a FHIR resource.

The only real FHIR documents in the current repositories are two **input** samples, `powerscribe-fhir.json` and `chest-ct-fhir.json`, which are pre-transformation DiagnosticReports carrying contained `Patient`, `ImagingStudy`, and `Observation` resources.[^powerscribe] They are worth reading because they differ from the prescribed output in two instructive ways. Their finding Observations code `bodySite` with [RadLex](/glossary/radlex.md), which the prescribed mapping does not mention. And their components carry DICOM codes for series, instance, and SOP identifiers rather than presence and change-from-prior attribute codes. That is not a contradiction: the component pattern the specification describes applies to the Exam Finding List output, not to the reporting system's input.

| Piece | Status |
|---|---|
| CDE-labeled FHIR Observation pattern | Demonstrated in hand-built lineage samples and a lineage Pydantic class; no current code |
| Exam Finding List as DiagnosticReport plus Observations | Documented; implemented nowhere |
| Imaging Problem List as Conditions plus Observations | Documented; implemented nowhere |
| FHIR resources as pipeline input | Real, two samples, from a commercial reporting system |
| Longitudinal FHIR persistence of findings | A design note on an unmerged branch of a superseded prototype; see [Imaging Persona](/data-structures/imaging-persona.md) |

# The open question underneath

The component pattern that every OIDM encoding uses is the one IHE's Imaging Diagnostic Report profile declines to use. IDR states that `Observation.component` "is not used", because FHIR limits components to values "not useful on their own" and using it "has the potential to significantly complicate queries", preferring a root Observation whose `hasMember` references the associated observations. Since the deck names IDR as the Exam Finding List's target representation, that disagreement sits directly under the mapping. It is set out in [IHE IDR alignment](/data-structures/ihe-idr-alignment.md), along with the other points where the two models differ.

[^ipl-main]: imaging-problem-list README, main branch
[^ipl-claude-dev]: imaging-problem-list domain model notes, dev branch
[^lineage-obs]: Observation model, OpenImagingDataModel.py
[^fhir-report]: The lung cancer screening DiagnosticReport, FHIRSamples
[^fhir-ai]: The AI-produced finding Observation, FHIRSamples
[^fhir-lungrads]: The Lung-RADS assessment Observation, FHIRSamples
[^powerscribe]: powerscribe-fhir.json, imaging-problem-list sample data
[^site-findings]: "Findings, CDEs, and Observations", openimagingdata.org, 2023-06-24
[^site-about]: openimagingdata.org About page
[^deck]: "Open Imaging Data Model 2026 Status Update", January 2026
