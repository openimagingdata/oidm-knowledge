---
type: Concept
title: Open Imaging Reporting SDK
description: The vendor-facing reporting toolkit named as a strategic pillar in the 2026 status deck, its 2023 plugin-container precursor, and the fact that no artifact exists.
tags: [applications, reporting, roadmap, vendors]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
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

No artifact exists. There is no repository, package, specification, issue, or branch for an Open Imaging Reporting SDK in any repository read for this knowledgebase, and the project lead confirms it as concept only. It appears in this bundle as stated direction, and every document that mentions it says so. The glossary entry is [Open Imaging Reporting SDK](/glossary/open-imaging-reporting-sdk.md); the goal itself is recorded in [the 2026 roadmap](/roadmap/roadmap-2026.md).

What follows is what has actually been said about it, and the two pieces of working code that show what parts of it would look like.

# What the deck says

The January 2026 status update organizes the project into three pillars. The third is applications, and the deck states it as "an Open Imaging Reporting SDK enabling vendor-driven innovation", alongside demonstration applications including an Imaging Problem List browser and early draft-generation tools.[^deck]

The call to action returns to it in the same terms. The deck asks for an ACR-OIDM structured imaging results working group, for structure first with FHIR and other standards following, and for the work to be vendor-driven, giving reporting software development kits from a reporting vendor as the example of what that means. The SDK is therefore named as something vendors would build on or build, not as something the project commits to shipping.

# The 2023 precursor

The idea is not new, and the earliest statement of it is more specific than the deck's. A site post of 2023-07-16 proposes a reporting assistance framework built as a plugin container inside the reporting tool.[^site-framework]

Its shape, as stated:

- Developers author plugins in an ordinary programming language, the post naming JavaScript.
- The container gives every plugin a standard data structure, defined by OIDM, holding the relevant context: the findings in the current report, prior reports, and the exams being reported on.
- Each plugin inspects that context and issues standard commands back to the reporting system. The four named are inserting generated text into the report, requesting more information from the radiologist, alerting the radiologist to a problem, and sending data to an external system.
- The container re-runs every plugin whenever the context changes, whether because new machine-generated data arrived or because the radiologist edited the report.

The post describes the result as a suite of assistant scripts continually reviewing the data around a radiologist and issuing commands to assist. That is a plugin architecture rather than a library, which is the main way it differs from what the deck's shorthand suggests. The post is summarized among [the site articles](/history/site-articles.md).

# The About page promise

The About page, last modified 2023-06-21, commits the project to maintaining programming interfaces in at least three languages, TypeScript and JavaScript, Python, and C#.[^site-about] Two of the three were begun and both are now lineage; no C# library was ever written. See [lineage repositories](/history/lineage-repositories.md).

The libraries that do exist, `findingmodel` with its anatomic locations package and `med-ontology-lookup`, are semantic-foundation tools. They resolve definitions and codes. They are not a reporting toolkit and are not presented as one; see [the terminology lookup profile](/semantic-foundation/terminologies/med-ontology-lookup.md).

# The one working precedent

`CDETemplateDemo`, written in 2023 and untouched since, is the only code in the project that does anything a reporting SDK would have to do. It takes a [CDE-labeled FHIR Observation](/glossary/cde-labeled-fhir-observation.md), flattens its components into a dictionary keyed by display name, derives boolean flags including explicit present and absent flags, and renders the result through a text template so that one template produces a full sentence for a present finding and a short clause for an absent one.[^cde-demo] It was demonstrated at SIIM in June 2023 as a web service.

That is structured data to report prose, without a language model. It is the half of the 2023 framework that the plugins would call when they insert generated text. The full account is in [CDE template rendering](/history/cde-template-rendering.md).

# What would have to exist

Stated only as what the sources describe, not as a design. The 2023 post names a standard report-context data structure defined by OIDM; today the closest thing to it is the [Exam Finding List](/data-structures/exam-finding-list.md), which covers the findings of one exam, and the [Imaging Problem List](/data-structures/imaging-problem-list.md), which covers a patient's history. Neither carries the current report text, the order, or the prior reports that the post's context structure and the About page's wider scope both call for, and the [Imaging Persona](/glossary/imaging-persona.md), which is the deck's name for that surrounding clinical context, is itself concept only. The rendering half has a working precedent and no maintained implementation. The plugin container half has no implementation at all.

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
