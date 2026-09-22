---
type: Concept
title: Vision
description: Why OIDM pursues object-oriented imaging results, what that unlocks across the imaging life cycle, and what the project has proposed next.
tags: [overview, vision, strategy]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:34:50Z }
sources:
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026
  - id: site-structure
    resource: https://www.openimagingdata.org/data-model-structure-and-function/
    title: "Data Model: Structure and Function, 2024-01-25"
  - id: site-findings
    resource: https://www.openimagingdata.org/findings-cdes-and-observations/
    title: "Findings, CDEs, and Observations, 2023-06-24"
  - id: site-benchmark
    resource: https://www.openimagingdata.org/benchmarking-a-vision/
    title: "Benchmarking a Vision, 2024-07-01"
  - id: site-plugin
    resource: https://www.openimagingdata.org/oidm-based-next-gen-reporting-assistance/
    title: "OIDM-Based Next-gen Reporting Assistance Framework, 2023-07-16"
  - id: fmf
    resource: https://fmf.oidm.org
    title: Finding Model Forge, the finding model authoring application
---

# Object-oriented imaging results

The January 2026 status deck calls OIDM's goal "standardizing the DNA of imaging IT" and titles itself "Realizing Object-Oriented Imaging Results."[^deck] It proposes representing each finding as an object with a type, location, attributes, and an identity that persists across exams.

The site posts describe a finding as "a standard format based on FHIR Observations semantically labeled with ACR/RSNA Common Data Element identifiers."[^site-findings] The wider model is "a superstructure on top of these FHIR definitions to both organize them and enable more straightforward programmatic access to the data." The post compares the layers: "the relationship between OIDM and FHIR might be that between the browser's DOM and HTML."[^site-structure] FHIR supplies resources, and OIDM supplies an object model for programmatic access.

# What object-oriented results unlock

The deck names three benefits.[^deck]

**A unified reading toolset.** Picture archiving and communication systems, reporting software, and artificial intelligence tools each hold partial, private representations of exam results. A shared object model would make findings created in one tool readable by the others.

**Integrated data sources.** A common representation would let systems merge, compare, and attribute statements from radiologists, electronic medical records, and artificial intelligence tools. The deck proposes validating artificial intelligence tools by correlating their observations with radiologist observations.

**Downstream longitudinal utility.** Findings with persistent identities would make imaging histories queryable. The deck's core query for the [Imaging Problem List](/glossary/imaging-problem-list.md) is whether a finding was present on the most recent study, with tracking of appearance, disappearance, and change.

# The workbench relationship between finding models and CDEs

The deck calls the [finding models](/glossary/finding-model.md) corpus "the CDE workbench."[^deck] [Common data elements](/glossary/cde.md) published through RadElement undergo formal ACR and RSNA review, versioning, and governance. That process supports adoption but slows creation.

[Finding Model Forge](https://fmf.oidm.org) and agent-driven batch workflows support faster authoring with language model assistance. The deck describes finding models as a "rapid innovation / proving ground before ACR/RSNA CDE adoption." Their "exploratory metadata" includes "rich definitions w/ embedded relationships and semantic tags that can graduate to standards."[^deck]

The corpus supplies knowledge for extraction and reporting tools, described in the deck as "ground-level info for tool access + LLM context engineering." Proven definitions become candidates for formal common data elements. See [Finding models and CDEs](/semantic-foundation/finding-models/finding-models-and-cdes.md).

# The Imaging Problem List across the imaging life cycle

The deck proposes uses for structured results throughout an imaging encounter.[^deck]

| Stage | Stated application |
|---|---|
| Planning | MRI safety screening, mobility assessment, prior authorization |
| Intra-exam | Rules-based protocoling |
| Interpretation | Findings-oriented views in the picture archiving system, real-time quality control |
| Post-interpretation | Passive screening, research cohorts, outcomes tracking |

The 2023 framework post proposes a reporting tool that hosts plugins and supplies "all the relevant contextual information, about the findings in the current report, about prior reports, about the exams that were being reported on." The tool reruns plugins when context changes. Plugins can insert text, request input, raise alerts, or send data onward.[^site-plugin] The data structures layer provides the structured context those plugins need.

# Why not just let the language model read the report

Large language models can read narrative reports, but the deck gives three reasons to retain structured results.[^deck]

**Context engineering.** Models answer better when given relevant findings directly. Structured results let systems select that context from prior reports.

**Deterministic logic.** MRI safety checks and protocol selection require rules over facts with known types and codes. Reinterpreting prose on each run does not provide that consistency.

**Citable common context.** Systems acting on the same patient need shared, auditable facts. A model's private interpretation of a report provides no shared reference.

The deck describes the Imaging Problem List as "automatically extractable from narrative report text via LLMs."[^deck] Language models convert prose into objects once for downstream systems to use.

# The proposed working group

The deck's call to action is a proposal, not an existing body. The deck proposes an "ACR-OIDM Structured Imaging Results Working Group," co-hosted with the ACR and bringing together expert and vendor participants.[^deck] Its principles are to define structures before mapping them to FHIR and other standards, support innovation by reporting software vendors, and host an academic-vendor "big tent" moderated by the project.

The proposed group would address four ACR priorities: recommendation tracking, artificial intelligence validation against radiologist observations, quality metrics, and support for the *-RADS reporting systems. The next steps are to convene the group, run a use-case pipeline feeding the CDE group, and standardize the result.

As of this writing the working group is a proposal recorded in the deck. Nothing in the source repositories records it as convened. Area-specific goals appear under [roadmap](/roadmap/).

# Evidence offered so far

A 2024 site post announces a manuscript in the peer-reviewed Journal of the American Medical Informatics Association titled "Standardizing imaging findings representation: harnessing Common Data Elements semantics and Fast Healthcare Interoperability Resources structures." The post summarizes its position as "CDE-labeled Observations should be the universal representation for exchanging and consuming content in radiology reports." The manuscript presents a pulmonary nodule case study and guidance on adoption challenges.[^site-benchmark]

[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
[^site-structure]: "Data Model: Structure and Function", 2024-01-25
[^site-findings]: "Findings, CDEs, and Observations", 2023-06-24
[^site-benchmark]: "Benchmarking a Vision", 2024-07-01
[^site-plugin]: "OIDM-Based Next-gen Reporting Assistance Framework", 2023-07-16
