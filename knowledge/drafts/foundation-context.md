---
type: Overview
title: Foundation Context
description: The shared, non-patient-specific layer of definitions, relationships, and citations that imaging results point into, and the work of building its content.
tags: [foundation-context, semantic-foundation, siim-2026, overview]
status: draft
generated: { by: claude-opus-5/2026-09-22-restructure/draft-foundation, at: 2026-09-22T00:00:00Z }
sources:
  - id: siim2026
    resource: sources/bucket/text/siim2026-reports-of-the-future.md
    title: "Structured Results and Context for Next-Generation Imaging Resulting Tools: Creating the Reports of the Future. SIIM 2026 annual meeting talk, June 2026, Mass General Brigham"
    last_modified: 2026-06-01
  - id: joint-notes
    resource: docs/plans/restructure-joint-notes.md
    title: "Restructure joint working notes, carrying the project lead's decisions of 2026-09-22"
    last_modified: 2026-09-22
  - id: cde-context
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/CONTEXT.md
    title: "CDE vocabulary, CONTEXT.md, ACR-RSNA-CDEs next-gen-2026 branch at 44836c1, 2026-09-15"
    last_modified: 2026-09-15
---

# The two halves

The SIIM 2026 annual meeting talk opens on "the two halves that make next-gen tools work: the structured result, and the knowledge to interpret it," and names them **Patient Context**, one patient's imaging results and the clinical context around them, and **Foundation Context**, the one layer of definitions, relationships and citations that every patient's results point into, openly authored, versioned, and not patient-specific.[^siim2026] The [introduction](./introduction.md) sets the two side by side in full.

# What this pillar covers

The project lead's decision of 2026-09-22 sets the boundary, and it is wider than a schema: Foundation Context "includes both the schema/meta-definitions as well as the efforts to build out content."[^joint-notes] Both halves are on this reading path — the shape a definition takes, and the work of writing definitions.

# The stated motivation

The deck's pivot slide states the gap in the structured record. A structured [Observation](../glossary/observation.md) — pulmonary nodule, present — "says it exists, where, and on what exam." It does not say how it associates with other findings, how it is potentially precancerous, which prior exams could show it, what the implications are, or what else it could be. Answering those five questions "needs background knowledge of anatomy, pathology, and imaging technique — knowledge that isn't in the patient's record."[^siim2026]

# Three axes, each layered over a standard

The deck gives Foundation Context three axes, each "an OIDM layer over" something that already exists, "adding imaging-specific knowledge on top of existing standards rather than reinventing them."[^siim2026]

| Axis | The deck's question | Layered over |
|---|---|---|
| Finding definitions — the deck's own label for this axis is "Observation Type" | WHAT was found | CDE and OIFM definitions |
| Anatomic Location | WHERE it is | a RadLex-anchored body map |
| Exam Type | HOW it was seen | LOINC and RadLex Playbook study types |

The deck calls what runs between and out of the axes "the connective tissue": within-axis relationships (parent and child types; causes and caused_by; confused_with, occurs_with), cross-axis statements (anatomy limits on a finding definition, exam-type anatomy associations, modalities), and external citations to Radiopaedia and Wikipedia plus references to SNOMED, RadLex, LOINC, FMA, ICD, and CPT.[^siim2026] The next-generation CDE vocabulary states the same posture for its own terms, and adds that they "express our current ideas for the reviewer's foundation, not a jointly settled integration model."[^cde-context]

# How data structures reach it

The deck keeps the Observation "deliberately small — codes, not knowledge." It carries a semantic tag, "a CDE-style definition (today an OIFM Finding Model)," plus presence, change from prior, and characterization attributes. "A code on an Observation is a pointer into one of these axes — the axes also point to each other, and out to external references." The resolution step is where the knowledge arrives: "Resolve, don't reinvent," code to pointer to resolve, with "OIDM SDKs make resolution easy and standardized — every app pulls the same context the same way." The deck's worked figure resolves one Observation to the finding definition for radiodense urinary calculus (`OIFM_GMTS_020556`), which "may cause" hydronephrosis (`OIFM_OIDM_874812`), each occurring at kidney (`RID205`) and renal pelvis (`RID228`), the renal pelvis part of the kidney.[^siim2026]

# Child sections

* [Finding models and CDEs](./finding-models-and-cdes.md) - the common graph, the two collections that hold it today, what the inclusive collection contains, and the authoring and review principles behind it.
* [Anatomic locations](./anatomic-locations.md) - the WHERE axis: containment, part-of, laterality, and the overlay on RadLex.
* [Exam types](./exam-types.md) - the HOW SEEN axis: exam families over the LOINC and RadLex Playbook, and their anatomy edges.
* [Standards the foundation layers over and cites](./standards.md) - RadLex, SNOMED CT, FMA, LOINC and the Playbook, and the role each plays.

[^siim2026]: SIIM 2026 annual meeting talk, June 2026, Mass General Brigham
[^joint-notes]: Restructure joint working notes, the project lead's decisions of 2026-09-22
[^cde-context]: CDE vocabulary, CONTEXT.md, ACR-RSNA-CDEs next-gen-2026 branch at 44836c1
