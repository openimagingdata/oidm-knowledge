---
type: Roadmap
title: Imaging Problem List data model system
description: "The stated goals for the Observation, Exam Finding List, and Imaging Problem List layer: the formal model system asked for in issue 1, the eight active plans on the development branch, the anatomic-compatibility follow-on, and the FHIR and IHE alignments that are documented but unimplemented."
tags: [roadmap, data-structures, ipl, observation, fhir, ihe]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T19:00:00Z }
stale_after: 2027-09-21
sources:
  - id: issue-1
    resource: https://github.com/openimagingdata/imaging-problem-list/issues/1
    title: imaging-problem-list issue 1, "Create System of Data Models", opened 2026-01-28
  - id: plan
    resource: /plans/2026-09-20-knowledgebase-build-plan.md
    title: Knowledgebase build plan, recording the project lead's statements of 2026-09-20 and 2026-09-21
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: "Open Imaging Data Model 2026 Status Update, January 2026"
  - id: ipl-main
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/README.md
    title: imaging-problem-list README, main branch, the stable specification
  - id: anat-plan
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/anatomic-location-efl-ipl.md
    title: Anatomic locations for Exam Finding Lists and Imaging Problem Lists, imaging-problem-list dev branch
  - id: anat-rules
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/anatomic-location-assignment-rules.md
    title: Anatomic location assignment rules, imaging-problem-list dev branch
  - id: evals
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/extractor-evals-redesign.md
    title: Extractor evaluation redesign, imaging-problem-list dev branch
  - id: viewer-v2
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/viewer-v2-anatomy-dashboard.md
    title: Anatomy dashboard viewer plan, imaging-problem-list dev branch
  - id: reviewer-workflows
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/extraction-reviewer-workflows.md
    title: Extraction reviewer workflows, imaging-problem-list dev branch
  - id: idr-extract
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md
    title: IHE Imaging Diagnostic Report Phase II extract, ACR-RSNA-CDEs next-gen-2026 branch
  - id: fhir-design-note
    resource: https://github.com/openimagingdata/IPL-MVP-ExtractionAndLabeling/tree/Persistent_FHIR_Resources
    title: Persistent FHIR resources design note, IPL-MVP-ExtractionAndLabeling
---

# The goals as the project lead states them

In the 2026-09-20 planning interview that produced [the knowledgebase build plan](/plans/2026-09-20-knowledgebase-build-plan.md), the project lead described the Imaging Problem List work in four parts: define data structures for [Observations](/glossary/observation.md) and their relationships; manage and collate those observations across a patient's history; design the applications that use them; and publish the result as standard formats.[^plan]

The January 2026 deck states the same layer as the second strategic pillar, an ordered hierarchy from the atomic Observation through the [Exam Finding List](/glossary/exam-finding-list.md) and the [Imaging Problem List](/glossary/imaging-problem-list.md) to the [Imaging Persona](/glossary/imaging-persona.md), and names the Imaging Problem List as "a standard format for structured imaging results, automatically extractable from narrative report text."[^deck] The structures as they exist today are documented under [data structures](/data-structures/); what follows is what has been stated about where they go.

# Issue 1: a formal system of data models

The one open issue in the `imaging-problem-list` repository, opened 2026-01-28, is titled "Create System of Data Models" and is unclaimed by any plan. Its substance in full:[^issue-1]

- Models are needed for **Observation**, with an **Extracted Observation** subtype raised as a question, for the **Exam Finding List**, and for the **Imaging Problem List**.
- They are to be **Pydantic** models.
- With **extensive annotation to generate JSON schemas**.
- Using **camelCase aliases in export** against **snake_case object attributes** internally.

Each element of that corresponds to a gap that exists today. There is no Observation model, no JSON Schema, and no standalone Observation record; the structure exists only inside the Exam Finding List JSON and, separately, inside the extraction pipeline's own models. Both the Exam Finding List and Imaging Problem List sample files carry a `$schema` URL that resolves to nothing. And the camelCase against snake_case split is the convention the existing sample data already follows without a model to enforce it.

The Extracted Observation subtype the issue floats maps onto a distinction the pipeline already makes in practice, between what a language model produced and what has been coded. See [Observation](/data-structures/observation.md).

# The eight active plans as direction

Eight plans are active on the `dev` branch of `imaging-problem-list`, and together they are the working direction for the layer. They are summarized with dates and status in [the report extraction platform profile](/applications/report-extraction-platform.md). Four of them state goals that reach beyond tooling.

**Human review as the instrument of record.** The reviewer integration plan makes one offline, no-build-step review tool the primary instrument for extraction quality assurance and for adjudicating gold cases, and sequences the evaluation redesign behind it.[^reviewer-workflows]

**Honesty-first evaluation.** The evaluation redesign was descoped rather than discarded after three and a half months without implementation, on the stated ground that the full plan's ceremony made it unstartable. Version one scores quote-first matching and attribute values rather than raw finding yield, with frozen run configurations, per-case artifacts, a ten-case adjudicated gold set, and a non-blocking scorecard. The motivating failure is stated plainly: a model-selection round picked a local default on throughput and yield alone, which cannot distinguish real recall gains from fabricated findings.[^evals]

**Anatomy-first presentation, with the data structure held canonical.** The second-generation viewer plan states a design principle that constrains the data model rather than the interface: the viewer trusts the Imaging Problem List as canonical, and anatomy grouping is presentation-only and "must never merge/split IPL findings."[^viewer-v2]

**Local-only operation.** Protected health information stays on local models, with remaining hardening items shelved behind explicit reopen triggers.

# The anatomic-compatibility reconciliation follow-on

The most concrete open problem in the structure itself. Anatomic-location coding of findings landed on 2026-06-10, and the Imaging Problem List grouping key changed from finding code alone to finding code plus location identifier. The plan that did that work is marked complete for its core scope with one follow-on not started: step 3b, anatomic-compatibility reconciliation.[^anat-plan]

The assignment rules state what is unresolved:[^anat-rules]

> Parent/child or generic-vs-specific pairs for the *same finding code across exams* (e.g. "lung" vs "lower lobe of right lung"; "kidney" vs "left kidney") still produce separate IPL groups. Deciding whether such observations are the same problem or distinct is the **anatomic-compatibility reconciliation** step.

This is a data model question, not a display question, because the grouping key is part of the structure. It depends on the containment and part-of hierarchies described in [the anatomic location data model](/semantic-foundation/anatomic-locations/data-model.md).

# FHIR, documented and unimplemented

The mapping is stated in the specification on `main`: a report containing a list of [FHIR Condition](/glossary/fhir-condition.md) objects labeled with the finding identifier, each containing FHIR Observations documenting which exams the finding was recorded on, with exam date and LOINC-coded exam type.[^ipl-main]

No code in any repository produces a Condition resource, and no current plan claims to. The full picture, including the lineage precedents that do implement a FHIR encoding, is in [FHIR mapping](/data-structures/fhir-mapping.md). One lineage experiment states an adjacent goal: a design note on an unmerged `IPL-MVP-ExtractionAndLabeling` branch proposes persistent FHIR Observations with stable identifiers, so repeated mentions of a finding across reports link to one entity rather than creating new ones.[^fhir-design-note] It carries no file extension and adds no code.

# IHE Imaging Diagnostic Report alignment

The deck states that the Exam Finding List "connects to the IHE Imaging Diagnostic Report (IDR) FHIR representation."[^deck] That connection is a goal. No OIDM repository implements or references the profile; what exists is a full extract of the Phase II public comment draft on the `next-gen-2026` branch of `ACR-RSNA-CDEs`.[^idr-extract]

Four differences between the profile and current OIDM encodings are recorded in that extract, all listed as items to raise during public comment and none resolved: whether attributes ride in `Observation.component` or in `hasMember`; a vocabulary collision on the words "finding" and "observation"; whether a diagnosis is a FHIR Observation or a FHIR Condition; and whether [laterality](/glossary/laterality.md) lives in the location identifier or in a separate field. The profile also puts three questions back to the RadElement side, including what the coding system identifier for RadElement codes is. All are carried in [IHE IDR alignment](/data-structures/ihe-idr-alignment.md) and in [open questions](/roadmap/open-questions.md).

# What has no plan behind it

The [Imaging Persona](/data-structures/imaging-persona.md), the fourth level of the hierarchy, is named in the deck with four context categories and has no specification, no code, and no issue. The [provenance](/glossary/provenance.md) marker the Exam Finding List specification asks for on every Observation is not specified anywhere, and the only precedent for it is a lineage convention that overloads the FHIR `status` field. Attribute codes are assigned by no coding pipeline, so an extraction-derived Exam Finding List carries uncoded attribute keys apart from presence. These are recorded in [open questions](/roadmap/open-questions.md).

[^issue-1]: imaging-problem-list issue 1, "Create System of Data Models"
[^plan]: Knowledgebase build plan, recording the project lead's stated goals
[^deck]: "Open Imaging Data Model 2026 Status Update", January 2026
[^ipl-main]: imaging-problem-list README, main branch
[^anat-plan]: Anatomic locations for Exam Finding Lists and Imaging Problem Lists, dev branch
[^anat-rules]: Anatomic location assignment rules, dev branch
[^evals]: Extractor evaluation redesign, dev branch
[^viewer-v2]: Anatomy dashboard viewer plan, dev branch
[^reviewer-workflows]: Extraction reviewer workflows, dev branch
[^idr-extract]: IHE Imaging Diagnostic Report Phase II extract, next-gen-2026 branch
[^fhir-design-note]: Persistent FHIR resources design note, IPL-MVP-ExtractionAndLabeling
