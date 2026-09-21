---
type: Concept
title: Vision
description: Why OIDM pursues object-oriented imaging results, what that unlocks across the imaging life cycle, and what the project has proposed next.
tags: [overview, vision, strategy]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T15:00:00Z }
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

The January 2026 status deck frames the project's goal as "standardizing the DNA of imaging IT" and titles itself "Realizing Object-Oriented Imaging Results."[^deck] The metaphor is deliberate. An imaging result today is a document. The proposition is that it should instead be a set of objects: each finding an addressable thing with a type, a location, attributes, and an identity that persists across exams.

The earlier site posts set the technical form of that proposition. A finding is "a standard format based on FHIR Observations semantically labeled with ACR/RSNA Common Data Element identifiers."[^site-findings] The wider model is described as "a superstructure on top of these FHIR definitions to both organize them and enable more straightforward programmatic access to the data," with an explicit analogy: "the relationship between OIDM and FHIR might be that between the browser's DOM and HTML."[^site-structure] FHIR supplies the resources; OIDM supplies the object model over them that software can actually program against.

# What object-oriented results unlock

The deck names three consequences.[^deck]

**A unified reading toolset.** Picture archiving and communication systems, reporting software, and artificial intelligence tools currently each hold their own partial, private representation of what an exam showed. A shared object model lets one representation serve all three, so a finding created in one tool is legible in the next.

**Integrated data sources.** Radiologists, the electronic medical record, and artificial intelligence tools all produce statements about a patient's imaging. When each produces the same kind of object, they can be merged, compared, and attributed rather than kept in separate lanes. The deck lists correlating artificial intelligence observations against radiologist observations as an explicit validation use case.

**Downstream longitudinal utility.** Once findings are objects with identity, a patient's imaging history becomes queryable. The core query the deck names for the [Imaging Problem List](/glossary/imaging-problem-list.md) is whether a given finding was present on the most recent study, with dynamic tracking of appearance, disappearance, and change.

# The workbench relationship between finding models and CDEs

The deck's most specific strategic claim concerns the relationship between [finding models](/glossary/finding-model.md) and formal [common data elements](/glossary/cde.md). It calls the Open Imaging Finding Model corpus "the CDE workbench."[^deck]

The reasoning is about velocity and governance. Common data elements published through RadElement are formally reviewed, versioned, and governed by the ACR and RSNA, which is what makes them worth adopting and also what makes them slow to create. Finding models are authored quickly, with language model assistance, through [Finding Model Forge](https://fmf.oidm.org) and agent-driven batch workflows. The deck positions that speed as a feature: finding models are a "rapid innovation / proving ground before ACR/RSNA CDE adoption," carrying "exploratory metadata" in the form of "rich definitions w/ embedded relationships and semantic tags that can graduate to standards."[^deck]

The finding model corpus therefore serves two purposes at once. It is programmatic knowledge, described in the deck as "ground-level info for tool access + LLM context engineering," usable today by extraction and reporting tools. And it is a staging ground whose proven definitions become candidates for formal common data elements. The relationship is treated in depth in [Finding models and CDEs](/semantic-foundation/finding-models/finding-models-and-cdes.md).

# The Imaging Problem List across the imaging life cycle

The deck argues that structured results pay off at every stage of an imaging encounter, not only at reporting.[^deck]

| Stage | Stated application |
|---|---|
| Planning | MRI safety screening, mobility assessment, prior authorization |
| Intra-exam | Rules-based protocoling |
| Interpretation | Findings-oriented views in the picture archiving system, real-time quality control |
| Post-interpretation | Passive screening, research cohorts, outcomes tracking |

The same point appears in the 2023 framework post, which proposes a plugin-container architecture in which a reporting tool hosts small programs, supplies them with "all the relevant contextual information, about the findings in the current report, about prior reports, about the exams that were being reported on," re-runs them whenever the report context changes, and lets them issue commands back to insert text, request input, raise alerts, or send data onward.[^site-plugin] That architecture only works if the context handed to the plugins is structured, which is what the data structures layer provides.

# Why not just let the language model read the report

Large language models can read narrative reports well, which raises the obvious objection that structure is unnecessary. The deck answers it with three arguments.[^deck]

**Context engineering.** A model answers better when given the relevant findings directly than when given a stack of prior reports to re-read. Structured results are how the right context gets selected and delivered.

**Deterministic logic.** Some decisions must not be probabilistic. MRI safety checks and protocol selection are rule evaluations over facts. They need facts with known types and known codes, not an inference drawn fresh from prose on each run.

**Citable common context.** When several systems act on the same patient, they need to be acting on the same stated facts, with a shared reference that can be pointed at and audited. A model's private reading of a report is neither shared nor citable.

The argument is not that language models are unsuited to the work. They do the extraction: the deck's own premise is that the Imaging Problem List is "automatically extractable from narrative report text via LLMs."[^deck] The argument is about where the model sits. It converts prose into objects once, and everything downstream operates on the objects.

# The proposed working group

The deck's call to action is a proposal, not an existing body. It proposes that the ACR co-host an "ACR-OIDM Structured Imaging Results Working Group," bringing together expert and vendor participants.[^deck] Three principles are stated for it: structure first, with mapping to FHIR and other standards following rather than leading; vendor-driven innovation, with reporting software vendors building on the result; and an academic-vendor "big tent" that the project would host and moderate.

The deck lists four ACR priorities the working group would serve: recommendation tracking, validation of artificial intelligence tools by correlating their observations against radiologist observations, quality metrics, and support for the *-RADS reporting systems. The stated next steps are to convene that group, run a use-case pipeline feeding the CDE group, and standardize the result.

As of this writing the working group is a proposal recorded in the deck. Nothing in the source repositories records it as convened. Stated goals for each area are collected under [roadmap](/roadmap/).

# Evidence offered so far

The vision has been argued in a peer-reviewed venue. A 2024 site post announces a manuscript in the Journal of the American Medical Informatics Association titled "Standardizing imaging findings representation: harnessing Common Data Elements semantics and Fast Healthcare Interoperability Resources structures," whose position the post summarizes as "CDE-labeled Observations should be the universal representation for exchanging and consuming content in radiology reports," worked through a pulmonary nodule case study together with guidance on adoption challenges.[^site-benchmark]

[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
[^site-structure]: "Data Model: Structure and Function", 2024-01-25
[^site-findings]: "Findings, CDEs, and Observations", 2023-06-24
[^site-benchmark]: "Benchmarking a Vision", 2024-07-01
[^site-plugin]: "OIDM-Based Next-gen Reporting Assistance Framework", 2023-07-16
