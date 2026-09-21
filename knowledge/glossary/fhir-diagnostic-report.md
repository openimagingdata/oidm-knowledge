---
type: Glossary Term
title: FHIR DiagnosticReport
description: The HL7 FHIR resource for a diagnostic report, used in OIDM as the interchange encoding of an Exam Finding List.
tags: [glossary, data-structures, fhir]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: fhir
    resource: https://www.hl7.org/fhir/diagnosticreport.html
    title: DiagnosticReport resource, HL7 FHIR
  - id: ipl-readme
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/README.md
    title: imaging-problem-list README, FHIR representation
  - id: fhir-sample
    resource: https://github.com/openimagingdata/FHIRSamples/blob/9ae2fa934298e51789e355c9f4e0b71fabf6b5aa/lung_ca_screening_example/example1OIDMreport.json
    title: Lung screening DiagnosticReport sample
  - id: idr-extract
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md
    title: IHE IDR Phase II extract for the CDE vocabulary
---

# FHIR DiagnosticReport

The HL7 FHIR resource for a diagnostic report.[^fhir] In OIDM it is the documented interchange encoding of an [Exam Finding List](/glossary/exam-finding-list.md): "DiagnosticReport containing a list of Observation objects, with a finding code on each Observation and a list of components with attribute codes and values (especially present/absent and change from prior)."[^ipl-readme] In an [Imaging Problem List](/glossary/imaging-problem-list.md), DiagnosticReports are what each observation points back to, giving the exam date and [LOINC](/glossary/loinc.md) exam type.[^ipl-readme]

The lineage sample shows the shape with real data: a report with a SNOMED and HL7 category, a LOINC `code`, an inline `ImagingStudy`, `result` references to three [Observations](/glossary/observation.md), and `conclusion` with SNOMED `conclusionCode`.[^fhir-sample]

## Synonyms and near-synonyms

- **Report** and **radiology report** usually mean the narrative document; this is the resource that carries it plus its structured results.
- **`diagnosticReportId`** is the Exam Finding List field that holds its identifier.
- **[Imaging Diagnostic Report (IHE IDR)](/glossary/imaging-diagnostic-report.md)** is the profile that constrains this resource for radiology; it is not the resource.
- **ImagingStudy** is a separate resource for the study itself, present inline in the lineage samples.

## Identifier form

A FHIR resource identifier. The Exam Finding List samples use UUID strings.

## Where it is used

[FHIR mapping](/data-structures/fhir-mapping.md), [Exam Finding List](/data-structures/exam-finding-list.md), and [IHE IDR alignment](/data-structures/ihe-idr-alignment.md).

## Conflicts

The mapping is documented and unimplemented. No FHIR resource classes exist in the extraction platform's source, and a search for DiagnosticReport across it returns nothing; the only real FHIR documents in the repository are two input samples. Those input samples also do not use the presence and change-from-prior component pattern the specification prescribes, because that pattern describes the output.[^ipl-readme] Separately, IHE IDR would encode the attribute layer with `hasMember` rather than components.[^idr-extract]

[^fhir]: DiagnosticReport resource, HL7 FHIR
[^ipl-readme]: imaging-problem-list README
[^fhir-sample]: Lung screening DiagnosticReport sample
[^idr-extract]: IHE IDR Phase II extract
