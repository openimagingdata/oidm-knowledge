---
type: Overview
title: Introduction
description: What the Open Imaging Data Model is, the two contexts it distinguishes, the five pillars of the work, and how the project expects agreement to happen.
tags: [overview, orientation, foundation-context, patient-context]
status: draft
generated: { by: claude-opus-5/2026-09-22-restructure/draft-intro, at: 2026-09-22T12:53:46Z }
sources:
  - id: owner-notes
    resource: Project lead's notes on the revised Imaging Problem List manuscript, 2026-09-19, sources/email/2026-09-19-ipl-manuscript-notes.md
    title: Structures versus transport, and what OIDM defines, 2026-09-19
  - id: siim-deck
    resource: https://oidm-public.t3.tigrisfiles.io/oidm-knowledge-sources/SIIM%202026%20Reports-of-the-Future.pptx
    title: "Structured Results and Context for Next-Generation Imaging Resulting Tools, SIIM 2026 annual meeting talk, June 2026, Mass General Brigham"
  - id: jan-deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026
  - id: site-about
    resource: https://www.openimagingdata.org/
    title: openimagingdata.org, project site and tagline
  - id: site-findings
    resource: https://www.openimagingdata.org/findings-cdes-and-observations/
    title: "Findings, CDEs, and Observations, 2023-06-24"
  - id: site-data-model
    resource: https://www.openimagingdata.org/data-model-structure-and-function/
    title: "Data Model: Structure and Function, 2024-01-25"
  - id: site-benchmarking
    resource: https://www.openimagingdata.org/benchmarking-a-vision/
    title: "Benchmarking a Vision, 2024-07-01"
  - id: joint-notes
    resource: docs/plans/restructure-joint-notes.md
    title: Restructure joint working notes, the project lead's decisions of 2026-09-22
  - id: build-plan
    resource: knowledge/plans/2026-09-20-knowledgebase-build-plan.md
    title: Knowledgebase build plan, decisions added 2026-09-21
---

# What OIDM is

The Open Imaging Data Model (OIDM) defines, in the project lead's words of 2026-09-19, "a system of defined data structures for representing imaging exam result information", "intended to be used within applications to both read and create result data".[^owner-notes] The project site states the purpose as "defining unified data structures to integrate new functionality into imaging informatics platforms". The January 2026 status update titles the goal "Realizing Object-Oriented Imaging Results" and calls it "standardizing the DNA of imaging IT".[^site-about][^jan-deck]

The June 2026 talk states why the result should be data. A finished report "is where the value should begin": a report's findings are written for a human reader, then locked in narrative text. Structuring them makes them reusable in two directions — forward to clinicians, "driving treatment decisions, follow-up, and care coordination", and forward to the next radiologist reading the subsequent exam, "what was there before, where, and whether it changed".[^siim-deck]

That talk was given from Mass General Brigham. The finding definitions the model points at exist in two collections: the inclusive collection the Open Imaging Data Model organization maintains on GitHub, and the well-reviewed Common Data Element collection of the American College of Radiology and the Radiological Society of North America. The January 2026 update describes the first as a "workbench", a "proving ground before ACR/RSNA CDE adoption".[^jan-deck][^joint-notes]

# The two contexts

The June 2026 talk names the two halves that next-generation tools need: "the structured result, and the knowledge to interpret it."[^siim-deck]

| | Patient Context | Foundation Context |
|---|---|---|
| Scope | One per patient | One layer shared by every patient |
| Contents | Observations, Exam Finding List, Imaging Problem List | Definitions, relationships, citations |
| How it changes | With the patient's clinical evolution | By open authoring and versioning |
| Privacy | Protected health information | Open, not patient-specific |
| Example | "8 mm nodule, RUL, new" | "what a pulmonary nodule is" |

The two are joined by their codes. The talk presents Foundation Context as three curated axes — what was found, where it is, how it was seen — and states the join: "A code on an Observation is a pointer into one of these axes — the axes also point to each other, and out to external references."[^siim-deck] (The deck's tentative name for the first axis is "Observation Type"; its notes say the ACR/RSNA elements "may carry" that name later.) The relationships on each side are different in kind. Between definitions, a relationship is a standing possibility, as in the talk's worked figure where a radiodense urinary calculus "may cause" hydronephrosis. Between observations, a relationship is what this radiologist asserted about these particular observations on this exam. [Data Structures](./data-structures.md) explains the two graphs and how they work together; this page only previews them.

# What a structured Observation cannot answer

The talk's pivot is that "the structures identify — but they don't explain." A structured Observation, "pulmonary nodule, present", says it exists, where, and on what exam. It does not say:[^siim-deck]

- How does it associate with other findings?
- How is it potentially precancerous?
- Which prior exams could show it?
- What are the implications?
- What else could it be?

"Answering these needs background knowledge of anatomy, pathology, and imaging technique — knowledge that isn't in the patient's record."[^siim-deck] That is the stated motivation for Foundation Context.

# The five pillars

The project lead named five parts of the work on 2026-09-22, to be used by name.[^joint-notes]

- **[Foundation Context](./foundation-context.md)**, the semantic layer, "includes both the schema/meta-definitions as well as the efforts to build out content."
- **[Data Structures](./data-structures.md)**, "most ESPECIALLY in the Observation layer, and how there are two graphs and they work together."
- **[SDKs](./sdks.md)**, "the tools that wrap the data structures and enable developers working in the application layer to manipulate instances in real-world applications (and some around helping with definition of the foundation context, obviously)."
- **[Use Cases](./use-cases.md)**, "Imaging all the different kinds of applications/tools/plugins/output products we could create using an ecosystem built around this foundation."
- **[Sample Applications](./sample-applications.md)**, "ACTUAL sample applications we've created to try to illustrate some of these ideas."

# Structure first, transport after

The structures are defined for use inside applications, and are not a transport definition. The project lead's 2026-09-19 notes state that they are "NOT a transport definition (not FHIR, not DICOM)", that they may eventually need FHIR expressions to travel, and that designing for that possibility is "completely separate from the definition of the structures applications manipulate". The stated reason to agree on the structures is that agreed structures make it easier to agree on what must be conveyed between systems, and that they guide the design of the FHIR profiles and related artifacts that inter-process communication will need.[^owner-notes] The January 2026 call to action puts the same ordering as "structure-first (then FHIR etc.)".[^jan-deck]

Earlier project statements put the structures and their FHIR expression together rather than apart. The founding site post of 2023-06-24 represents a finding as a FHIR Observation labeled with Common Data Element identifiers.[^site-findings] The 2024-01-25 post proposes structures over FHIR definitions for programmatic access and offers an analogy: "the relationship between OIDM and FHIR might be that between the browser's DOM and HTML."[^site-data-model] The 2024-07-01 post announces a manuscript presenting CDE-labeled FHIR Observations as the universal representation for exchanging and consuming report content.[^site-benchmarking] [Data Structures](./data-structures.md) carries the current mapping status.

# Nothing is formally defined yet

The project is in a coalescing phase, and nothing is formally defined. This knowledgebase presents each source's current version of a structure beside the others, dated and attributed, and states disagreements without resolving them. No source here is called the specification or the canonical model.[^build-plan]

How agreement is meant to happen is itself a proposal. The January 2026 call to action names an ACR-OIDM Structured Imaging Results Working Group, co-hosted with the American College of Radiology, "vendor-driven", with next steps to "host/moderate academic-vendor big tent; use-case pipeline -> CDE group; standardize the result". It names ACR priorities as recommendation tracking, AI validation, quality metrics, and *-RADS support.[^jan-deck] No source read records the working group as convened.

# The ask

The June 2026 talk closes with three requests: contribute or propose finding definitions (the talk's wording is "Observation Type definitions"); review AI-generated content and connections; build against the SDKs.[^siim-deck]

[^owner-notes]: The project lead, 2026-09-19, points 3, 4, and 5 of the notes on the revised Imaging Problem List manuscript. Held in the local source collection.
[^siim-deck]: SIIM 2026 annual meeting talk, June 2026, Mass General Brigham; slides 1, 3, 6, 7, 8, 12, 14, and 15 with their speaker notes.
[^jan-deck]: Open Imaging Data Model 2026 Status Update, January 2026: executive summary, strategic pillars, the CDE workbench section, and the call to action.
[^site-about]: openimagingdata.org, project site tagline, read 2026-09-21.
[^site-findings]: "Findings, CDEs, and Observations", openimagingdata.org, 2023-06-24.
[^site-data-model]: "Data Model: Structure and Function", openimagingdata.org, 2024-01-25.
[^site-benchmarking]: "Benchmarking a Vision", openimagingdata.org, 2024-07-01.
[^joint-notes]: Restructure joint working notes, "Decisions of 2026-09-22", items 1 and 2, quoting the project lead.
[^build-plan]: Knowledgebase build plan, "Decisions added 2026-09-21", the "No specification exists" row.
