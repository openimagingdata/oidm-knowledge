---
type: Glossary Term
title: Imaging Diagnostic Report (IHE IDR)
description: The IHE Radiology profile that specifies how a diagnostic imaging report and its findings are encoded as FHIR resources.
tags: [glossary, data-structures, fhir, ihe]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: idr-supplement
    resource: https://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_Suppl_IDR_PhII_Rev1-2_PC_2026-03-04.pdf
    title: IHE Radiology Technical Framework Supplement, Imaging Diagnostic Report Phase II, public comment draft, 4 March 2026
  - id: idr-extract
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md
    title: IHE IDR Phase II extract for the CDE vocabulary
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026
---

# Imaging Diagnostic Report (IHE IDR)

The Integrating the Healthcare Enterprise Radiology profile that specifies how a diagnostic imaging report and the findings inside it are encoded as FHIR resources. Phase II went out for public comment in March 2026.[^idr-supplement] The deck states that an [Exam Finding List](/glossary/exam-finding-list.md) "connects to IHE Imaging Diagnostic Report (IDR) FHIR representation."[^deck]

IDR's information model, "heavily influenced by modelling in SNOMED and DICOM," defines three terms OIDM must map onto. Body Structure "encompasses both anatomical structures and morphologic abnormalities (like a lesion, cyst, inflammation, aneurysm, fracture or abscess)." An imaging observation is "a feature or characteristic that is visible in an image," encoded as a FHIR `Observation`. A clinical finding is "the determination that a clinical entity is present or absent," with positive findings encoded as [FHIR Condition](/glossary/fhir-condition.md) and negative ones as Observations.[^idr-extract]

The observation shape separates anatomy, laterality, morphology, property, and value into distinct slots, with anatomy "fully pre-coordinated except for the laterality." Where a [CDE set](/glossary/cde-set.md) is encoded, "it is preferred to use the CDE Set code" as the root `Observation.code`, with elements reached by `hasMember`.[^idr-extract]

## Synonyms and near-synonyms

- **IDR** is the abbreviation; **IHE Radiology** is the domain that publishes it.
- **[FHIR DiagnosticReport](/glossary/fhir-diagnostic-report.md)** is a resource IDR constrains, not the profile.
- **Finding Set** is IDR's name for a grouped observation, the counterpart of a CDE set instance.

## Identifier form

None. IDR constrains FHIR resources and reuses their identifiers.

## Where it is used

[IHE IDR alignment](/data-structures/ihe-idr-alignment.md) and [FHIR mapping](/data-structures/fhir-mapping.md).

## Conflicts

Three differences are recorded for public comment. IDR's "finding" is the presence determination, not the named entity, and its "observation" is closer to what the next-generation vocabulary calls a data element value. IDR routes positive diagnoses to Condition while the OIDM working default is that every assertion in a report is an Observation. IDR states that `Observation.component` "is not used," which is the mechanism every current OIDM encoding relies on.[^idr-extract] The `imaging-problem-list` repository does not mention IDR. Alignment is documented only in the vocabulary work and the deck.

[^idr-supplement]: IHE Imaging Diagnostic Report Phase II public comment draft
[^idr-extract]: IHE IDR Phase II extract
[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
