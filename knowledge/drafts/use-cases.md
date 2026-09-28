---
type: Concept
title: Use Cases
description: Proposed reporting assistance, longitudinal care, outcome tracking, and information products built on OIDM context and structures.
tags: [use-cases, reporting, imaging-history, outcomes]
status: draft
generated: { by: codex/2026-09-22-restructure-use-cases, at: 2026-09-22T13:53:10Z }
sources:
  - id: reporting-framework
    resource: https://www.openimagingdata.org/oidm-based-next-gen-reporting-assistance/
    title: OIDM-Based Next-gen Reporting Assistance Framework, 2023-07-16
  - id: reporting-board
    resource: "OIDM Big Picture working board, Reporting Assistance Framework and Next-Generation Assisted Reporting Use Cases frames, undated"
    title: OIDM Big Picture, reporting assistance framework and use-case mind map, undated working board
  - id: ipl-webinar
    resource: https://oidm-public.t3.tigrisfiles.io/oidm-knowledge-sources/IPL%20Webinar%20Deck.html
    title: The Imaging Problem List as an Accelerator for Radiology AI Applications, SIIM webinar, 2026-07-15, slides 36–43 and speaker notes
  - id: outcome-schema
    resource: "Outcome Tracking Schema, undated working board, clinical-event, action, and use-case sections"
    title: Outcome Tracking Schema, undated working board, data-model and workflow content
  - id: pathology-link
    resource: "Radiologist Outcome Feedback working board, Path Result and Biopsy Procedure linking proposal, 2025-06-02"
    title: Radiologist Outcome Feedback, shared tracking identifier proposal dated 2025-06-02
  - id: reports-future
    resource: https://oidm-public.t3.tigrisfiles.io/oidm-knowledge-sources/SIIM%202026%20Reports-of-the-Future.pptx
    title: Structured Results and Context for Next-Generation Imaging Resulting Tools, June 2026, slides 13–14
  - id: usecases-index
    resource: https://github.com/openimagingdata/UseCases/blob/71a90d2ab2efeee4c4303dc0aef27ed3d70a6c99/Index.md
    title: Index of Potential Use Cases, snapshot of 2024-02-26
  - id: value-categories
    resource: https://github.com/openimagingdata/UseCases/blob/71a90d2ab2efeee4c4303dc0aef27ed3d70a6c99/README.md
    title: OIDM Use Cases, value categories from the RSNA Reporting Informatics Committee, last changed 2023-09-25
    last_modified: 2023-09-25
  - id: status-deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026, imaging life cycle and ACR priorities
  - id: nodule-exchange
    resource: "Pulm Nodule Demo Project, undated working board, exchange aim and structured workflow"
    title: Pulm Nodule Demo Project, undated working board, structured exchange workflow
  - id: ipl-manuscript
    resource: "The Imaging Problem List: A Standards-Based Framework for Longitudinal Tracking of Imaging Findings, manuscript under review at JDIM, 2026"
    title: Imaging Problem List manuscript under review, clean abstract and Figure 1; reviewer correspondence not used
---

# Use Cases

This page groups documented application ideas by purpose. The July 2026 IPL webinar presents its applications as a roadmap, including breast work explicitly described as planned.[^ipl-webinar] Implemented examples have a separate home in [Sample Applications](/drafts/sample-applications.md).

## Reporting assistance

The July 2023 framework proposes plugins that inspect current findings, prior reports, and exam context. A reporting container would rerun them when context changes. Its four commands would insert text, request information, alert the radiologist, or send data externally.[^reporting-framework] The January 2026 deck names vendor-driven innovation through an Open Imaging Reporting SDK.[^status-deck] The reusable interfaces belong under [SDKs](/drafts/sdks.md).

The undated reporting board proposes a context object including clinical records, longitudinal findings, and AI, DICOM-SR, and text-extracted data. Its nine-command set includes changing context, retrieving clinical data, showing images, activating communication tools, and requesting image inference. Proposed uses include context-specific templates, AI-result review, references, specialized reporting, and checks for laterality errors or unanswered questions.[^reporting-board] Neither source identifies a superseding command set.[^reporting-framework][^reporting-board] These context proposals relate to the Imaging Persona under [Data Structures](/drafts/data-structures.md).

## Imaging history across the care cycle

The July 2026 webinar identifies six IPL application families:[^ipl-webinar]

- Pre-populate reports with known findings for review, distinguishing carried-forward content from new findings.
- Track incidental findings and overdue follow-up. Report content determines completion: an obscured finding still needs follow-up, while a resolved finding closes surveillance.
- Monitor chronic disease across the full history, including growth that looks small between consecutive scans.
- Surface findings across subspecialties, such as an adrenal nodule previously reported on chest CT.
- Check report consistency and recommendation appropriateness for quality surveillance.
- Select research cohorts through structured findings and assessment scores.

The 2026 IPL manuscript's Figure 1 groups downstream applications differently: report pre-population, follow-up management, clinical problem lists, combined quality and research, and AI with decision support. Its abstract describes the proposed benefits as awaiting evaluation.[^ipl-manuscript]

The January 2026 deck covers the imaging life cycle: MRI safety, mobility, and pre-authorization during planning; rules-based protocoling during the exam; findings-oriented views and quality checks during interpretation; and passive screening, research, and outcomes afterward.[^status-deck]

## Outcomes and follow-up

The outcome-tracking board proposes connecting reports and recommendations to later imaging, pathology, procedures, and other clinical events. Outputs include individual feedback, overdue-follow-up notifications, review worklists, registries, and aggregate statistics. Named uses include diagnostic-yield audits of malignancy-related *-RADS assessments, trainee report-change notifications, continuous AI monitoring, ordering-provider feedback, and interventional-radiology outcomes.[^outcome-schema]

A June 2025 proposal would link the imaging finding, targeted biopsy, and pathology result through a shared tracking identifier. That link would support radiology-pathology correlation.[^pathology-link] The outcome model also proposes following pathways from incidental detection through investigation, treatment, and later outcomes.[^outcome-schema]

## Breast imaging

The webinar's planned breast example tracks one mass across five exams over eighteen months, through changing BI-RADS assessments, biopsy, and a fibroadenoma diagnosis. The marker clip becomes a re-identification anchor. Proposed applications are a display of findings, assessments, and biopsy outcomes during interpretation, and an automated outcomes audit. The display's proposed design path is focus groups with breast radiologists followed by iterative usability testing toward a pilot. The audit would connect screening assessments with cancer diagnoses within one year, with intended coverage across mammography, ultrasound, and MRI. The source relates this to Mammography Quality Standards Act audit work and explicitly presents design, not results.[^ipl-webinar]

## Rules and generative assistance

The June 2026 Reports of the Future deck distinguishes determinative tools for safety checks, protocoling, and quality metrics from generative agents using shared, citable context. These proposed uses resolve patient finding codes into [Foundation Context](/drafts/foundation-context.md). Its examples connect pulmonary-nodule characteristics to follow-up guidance, track aneurysm diameter against a repair threshold, and relate a renal calculus to hydronephrosis. The deck presents these as intended uses of shared definitions and relationships.[^reports-future]

## Communication and information products

The catalog uses the RSNA Reporting Informatics Committee's six value categories: reporting efficiency; care-team communication; operations, quality, and safety; research; public health; and education.[^value-categories] The index credits the committee for ideas including actionable summaries, critical-finding messages, problem-list updates, research measurements, implant lists, clinical-question capture, and guideline templates with lay-language explanations. Other catalog ideas include registry submissions, teaching files, similar-case retrieval, prior DEXA exclusions, spine-numbering reconciliation, aortic measurement comparisons, and laboratory cross-checks.[^usecases-index]

## Shared priorities and exchange

The January 2026 deck names recommendation tracking, comparison of AI and radiologist observations, quality metrics, and *-RADS support as ACR priorities.[^status-deck]

The pulmonary-nodule exchange design aims to share radiology findings as CDE-labeled FHIR Observations over FHIRcast across AI, image viewing, reporting, and electronic health record systems. Responsibility for associating nodules and assigning tracking identifiers remains open on the board.[^nodule-exchange] See [Sample Applications](/drafts/sample-applications.md) for demonstrated work.

[^reporting-framework]: Reporting assistance proposal, 2023-07-16.
[^reporting-board]: OIDM Big Picture, reporting framework and use-case frames.
[^ipl-webinar]: SIIM IPL webinar, 2026-07-15, slides 36–43 and speaker notes.
[^outcome-schema]: Outcome Tracking Schema, clinical-event, action, and use-case sections.
[^pathology-link]: Radiologist Outcome Feedback, pathology-to-biopsy linking proposal, 2025-06-02.
[^reports-future]: Reports of the Future, June 2026, slides 13–14.
[^usecases-index]: Index of Potential Use Cases, 2024-02-26 snapshot.
[^value-categories]: OIDM Use Cases README, value categories.
[^status-deck]: January 2026 status update, imaging life cycle and ACR priorities.
[^nodule-exchange]: Pulm Nodule Demo Project, complete workflow and open questions.
[^ipl-manuscript]: Imaging Problem List manuscript under review at JDIM, 2026, clean abstract and Figure 1.
