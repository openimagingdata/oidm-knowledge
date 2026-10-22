---
type: Glossary Term
title: FHIR Condition
description: The HL7 FHIR resource for a clinical condition, used in the documented Imaging Problem List mapping as the container for one finding type.
tags: [glossary, data-structures, fhir]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: fhir
    resource: https://www.hl7.org/fhir/condition.html
    title: Condition resource, HL7 FHIR
  - id: ipl-readme
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/README.md
    title: imaging-problem-list README, Imaging Problem List FHIR representation
  - id: idr-extract
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md
    title: IHE IDR Phase II extract for the CDE vocabulary
---

# FHIR Condition

The HL7 FHIR resource for a clinical condition, problem, or diagnosis.[^fhir] Its only OIDM use is the documented FHIR mapping of an [Imaging Problem List](/glossary/imaging-problem-list.md), which is "a Report containing a list of Condition objects (labeled with the finding identifier), where each Condition object also contains a list of Observation objects which document which exams (DiagnosticReports) the finding type has been documented on, including the exam date and exam type."[^ipl-readme]

One Condition represents a finding type in one patient. Its [observations](/glossary/observation.md) record evidence across exams.

## Synonyms and near-synonyms

- **Problem** is the clinical word for what a Condition represents.
- **[FHIR DiagnosticReport](/glossary/fhir-diagnostic-report.md)** is the exam-level counterpart in the same mapping.
- **IPL finding entry** is the OIDM object a Condition would encode.
- **Diagnosis** as a [FindingClass](/glossary/finding-class.md) entity type is a vocabulary concept, not this resource.

## Identifier form

A FHIR resource identifier. The mapping labels each Condition with the finding identifier it stands for.

## Where it is used

[FHIR mapping](/data-structures/fhir-mapping.md), [Imaging Problem List](/data-structures/imaging-problem-list.md), and [IHE IDR alignment](/data-structures/ihe-idr-alignment.md).

## Conflicts

Three points are unsettled. The mapping is documented but unimplemented. No OIDM code produces Condition resources. Its container is called a "Report," which is not a FHIR resource name. IHE IDR routes positive clinical findings to Condition and negative ones to Observation, against an OIDM working default that "every assertion in a radiology report, diagnoses included, is encoded as an Observation," partly because "'consistent with pneumonia' is a radiologist's assertion, not an established clinical condition."[^idr-extract] If that default holds, `Condition.evidence` as the finding-to-diagnosis link has nowhere to attach and an Observation-to-Observation equivalent is needed.

[^fhir]: Condition resource, HL7 FHIR
[^ipl-readme]: imaging-problem-list README
[^idr-extract]: IHE IDR Phase II extract
