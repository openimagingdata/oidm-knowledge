---
type: Presentation Extract
title: Status update, January 2026
description: A faithful extract of the January 2026 OIDM status deck, "Realizing Object-Oriented Imaging Results", slide by slide.
tags: [references, deck, vision, roadmap]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T15:00:00Z }
sources:
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: "Open Imaging Data Model 2026 Status Update: Realizing Object-Oriented Imaging Results, January 2026"
---

# About this extract

This is an extract of the January 2026 Open Imaging Data Model (OIDM) status deck, presented by the project lead under the running subtitle "Standardizing the DNA of Imaging IT."[^deck] Sections below follow the deck's slides in order and keep its wording and emphasis. Two departures from the source are noted where they occur: the collaborators slide is reduced to organizations, per this knowledgebase's convention of naming organizations and not individuals, and screenshots are described rather than reproduced.

The deck is the primary statement of OIDM's direction as of early 2026. Where it names something that does not yet exist, this extract keeps the claim as the deck makes it; [Architecture](/overview/architecture.md) states the implementation status of each piece, and [Vision](/overview/vision.md) works through the reasoning.

# Title

**Open Imaging Data Model 2026 Status Update: Realizing Object-Oriented Imaging Results.** January 2026. Standardizing the DNA of Imaging IT.

# Executive summary

- **Foundational content.** A language-model-built curated anatomic location index, plus nearly 3,000 Open Imaging Finding Models (OIFMs).
- **The "workbench effect."** Language-model-powered, high-velocity content creation acts as a proving ground for formal common data elements (ACR and RSNA CDEs).
- **Standardizing history.** A hierarchy of prototype data structures centered on the Imaging Problem List (IPL), developed with vendors. The IPL is a standard format for structured imaging results, automatically extractable from narrative report text using language models.
- **The ACR opportunity.** Co-host an expert and vendor data structure working group. This supports the *-RADS reporting systems, recommendation tracking, and quality metrics.

# Vision

Object-oriented "DNA" for imaging results, enabling:

- A unified reading toolset across picture archiving systems, reporting software, and artificial intelligence tools.
- Integrated data sources: radiologists, the electronic medical record, and artificial intelligence tools.
- Downstream longitudinal utility.

# Strategic pillars

1. **Semantic foundation.** OIFM feeding CDEs; anatomic location definitions.
2. **Data structures.** The atomic Observation, then the Exam Finding List, then the Imaging Problem List, then the "Imaging Persona."
3. **Applications.** An Open Imaging Reporting SDK enabling vendor-driven innovation; demonstration applications including an IPL browser and early draft-generation tools.

# OIFM: the CDE workbench

Referencing Finding Model Forge at <https://fmf.oidm.org>.

- Rapid innovation and a proving ground, ahead of ACR and RSNA CDE adoption.
- **Programmatic knowledge.** Ground-level information for tool access and for language model context engineering.
- **Exploratory metadata.** Rich definitions carrying embedded relationships and semantic tags that can graduate to standards.

The slide carries two screenshots: the OIFM repository, and the "Create Model" screen of Finding Model Forge.

# Anatomic locations

Referencing <https://anatomiclocations.org>.

- Being formally incorporated into RadLex by an RSNA committee.
- Curated to identify where findings are visualized on imaging exams.
- Anatomy is baked into OIFM definitions and into Observation objects.

# Observation object, the atomic unit

- **What, where, and attributes.** A finding tag, an anatomic location, and lesion characteristics.
- Presence indicators, change from prior, and measurements.
- A universal structure across systems.

# Exam Finding List

- All findings from one exam in one queryable structure.
- Sourced from dictation, from artificial intelligence tools, and from interpretation-time interfaces.
- Connects to the IHE Imaging Diagnostic Report (IDR) FHIR representation.

# Imaging Problem List

- Organized by finding, meaning pathology, rather than by chronology.
- The core query: was finding X present on the most recent study?
- Precision filtering by way of anatomy-embedded definitions.
- Dynamic tracking of appearance, disappearance, and change.
- Demonstration at <https://imaging-problem-list.pages.dev>.

# Imaging Persona, the big picture

- Clinical context: orders and indications.
- Medical baseline: problem list, allergies, laboratory results.
- Specialized history: oncology, treatments.
- Surgical history: operative records, pathology, implants.

# The IPL across the imaging life cycle

| Stage | Applications named |
|---|---|
| Planning | MRI safety, mobility, prior authorization |
| Intra-exam | Rules-based protocoling |
| Interpretation | Findings-oriented views in the picture archiving system, real-time quality control |
| Post-interpretation | Passive screening, research, outcomes |

# Why not just let the LLM read it?

- **Context engineering.**
- **Deterministic logic**, for safety checks and protocol selection.
- **Citable common context.**

# Call to action

- An **ACR-OIDM Structured Imaging Results Working Group**.
- **Structure first**, with FHIR and other standards following.
- **Vendor-driven**, for example through reporting software development kits from a reporting vendor.

**ACR priorities served:** recommendation tracking; artificial intelligence validation, by correlating artificial intelligence Observations against radiologist Observations; quality metrics; support for the *-RADS reporting systems.

**Next steps:** host and moderate an academic and vendor "big tent"; run a use-case pipeline feeding the CDE group; standardize the result.

# Collaborators

Reduced to organizations, per this knowledgebase's naming convention. The source slide lists named individuals under each organization.

- **Academic.** Mass General Brigham (MGB); Columbia; Rochester.
- **Standards and regulatory.** The American College of Radiology (ACR); the United States Food and Drug Administration (FDA); the RSNA Reporting Informatics Committee.
- **Industry.** Microsoft; Canon, in connection with IHE; HOPPR; RadPAIR.

[^deck]: "Open Imaging Data Model 2026 Status Update: Realizing Object-Oriented Imaging Results", January 2026
