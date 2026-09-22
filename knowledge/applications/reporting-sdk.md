---
type: Concept
title: Open Imaging Reporting SDK
description: The proposed vendor-facing reporting SDK, its 2023 plugin framework precursor, and the fact that no artifact exists.
tags: [applications, reporting, roadmap, vendors]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:34:50Z }
stale_after: 2027-09-21
sources:
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026, applications pillar and call to action
  - id: site-framework
    resource: https://www.openimagingdata.org/oidm-based-next-gen-reporting-assistance/
    title: "Site post: OIDM-Based Next-gen Reporting Assistance Framework, 2023-07-16"
  - id: site-about
    resource: https://www.openimagingdata.org/about/
    title: openimagingdata.org About page, last modified 2023-06-21
  - id: cde-demo
    resource: https://github.com/openimagingdata/CDETemplateDemo/blob/e09f2553de58b2c88ea26e9673750a62803d4dbc/mapper-logic/src/mappers/obsToMustache.ts
    title: CDETemplateDemo Observation to template-data mapper, the rendering precedent
---

# Status first

The [Open Imaging Reporting SDK](/glossary/open-imaging-reporting-sdk.md) is concept only, as confirmed by the project lead. No repository, package, specification, issue, or branch for it was found in the repositories read for this knowledgebase. Its goal is recorded in [the 2026 roadmap](/roadmap/roadmap-2026.md).

# What the deck says

The January 2026 status update names "an Open Imaging Reporting SDK enabling vendor-driven innovation" under its applications pillar. It also lists demonstration applications, including an Imaging Problem List browser and early draft-generation tools.[^deck]

The deck calls for an ACR-OIDM structured imaging results working group, structure before FHIR and other standards, and vendor-driven work. Reporting SDKs from a reporting vendor are its example. It does not commit the project to shipping an SDK.

# The 2023 precursor

A 2023-07-16 site post proposes a reporting assistance framework as a plugin container inside the reporting tool.[^site-framework]

The proposal describes this behavior:

- Developers write plugins in a programming language such as JavaScript.
- The container supplies an OIDM-defined structure containing current findings, prior reports, and the exams being reported.
- Plugins inspect that context and issue four kinds of command: insert generated text, request information from the radiologist, alert the radiologist to a problem, or send data to an external system.
- The container reruns every plugin whenever context changes, including after new machine-generated data or a radiologist's edit.

The post describes the result as a suite of assistant scripts continually reviewing the data around a radiologist and issuing commands to assist. That is a plugin architecture rather than a library, which is the main way it differs from what the deck's shorthand suggests. See [the site articles](/history/site-articles.md).

# The About page promise

The About page, last modified 2023-06-21, commits to programming interfaces in TypeScript and JavaScript, Python, and C#.[^site-about] The first two were begun and are now [lineage repositories](/history/lineage-repositories.md). No C# library was written.

`findingmodel`, its anatomic locations package, and `med-ontology-lookup` resolve definitions and codes. They provide no reporting toolkit. See [the terminology lookup profile](/semantic-foundation/terminologies/med-ontology-lookup.md).

# The one working precedent

`CDETemplateDemo`, written in 2023 and unchanged since, is the project's only working precedent for reporting SDK functionality. It flattens a [CDE-labeled FHIR Observation](/glossary/cde-labeled-fhir-observation.md) into a dictionary keyed by component display name, derives boolean flags including presence and absence, and renders a text template. One template produces a full sentence for a present finding and a short clause for an absent one.[^cde-demo] It was demonstrated as a web service at SIIM in June 2023.

The demo generates prose without a language model, demonstrating the rendering needed by plugins that insert text. See [CDE template rendering](/history/cde-template-rendering.md).

# What would have to exist

Stated only as what the sources describe, not as a design. The proposed context structure includes current report text, the order, and prior reports. The [Exam Finding List](/data-structures/exam-finding-list.md) covers one exam's findings, and the [Imaging Problem List](/data-structures/imaging-problem-list.md) covers patient history, but neither carries that full context. The [Imaging Persona](/glossary/imaging-persona.md), the deck's name for surrounding clinical context, is also concept only. Rendering has a working precedent but no maintained implementation. The plugin container has no implementation.

# Where this is recorded

| Claim | Source | Date |
|---|---|---|
| Open Imaging Reporting SDK as the applications pillar | Status deck | January 2026 |
| Vendor-driven reporting SDKs as the call to action | Status deck | January 2026 |
| Plugin container, standard context structure, four commands, continuous re-run | Site post | 2023-07-16 |
| Programming interfaces in TypeScript and JavaScript, Python, and C# | About page | 2023-06-21 |
| Structured Observation rendered to prose through a template | `CDETemplateDemo` | 2023-06 |

[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
[^site-framework]: "OIDM-Based Next-gen Reporting Assistance Framework", 2023-07-16
[^site-about]: openimagingdata.org About page, last modified 2023-06-21
[^cde-demo]: CDETemplateDemo Observation to template-data mapper
