---
type: Concept
title: Why anatomic locations
description: Why OIDM curates its own anatomic location set instead of pointing at an existing ontology, and every place those identifiers are used across the model.
tags: [semantic-foundation, anatomic-locations, radlex, rationale]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
sources:
  - id: al-site
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/docs/index.markdown
    title: anatomiclocations.org site homepage, rationale, approach, and roadmap
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026
  - id: fm-model
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/finding_model.py
    title: FindingModelFull definition, findingmodel repository, main
  - id: ipl-anat-plan
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/anatomic-location-efl-ipl.md
    title: Plan to add anatomic-location codes to Exam Finding Lists and an anatomy-aware Imaging Problem List, imaging-problem-list dev
  - id: ipl-rules
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/anatomic-location-assignment-rules.md
    title: Anatomic location assignment rules, imaging-problem-list dev
  - id: viewer-plan
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/viewer-v2-anatomy-dashboard.md
    title: Anatomy-aware viewer plan, imaging-problem-list dev
---

# The problem the set solves

The premise is stated in one sentence on the project site: "Standard identifiers for discrete anatomic locations would enable numerous levels of interoperability if applied broadly."[^al-site] Two systems that agree a lesion sits at `RID2772` agree on the kidney without sharing a database, a vendor, or a schema.

The obvious way to get such identifiers is to adopt an existing anatomy ontology whole. The site says why that was rejected. Attempts to use [RadLex](/glossary/radlex.md) or [SNOMED CT](/glossary/snomed-ct.md) directly run into three problems:[^al-site]

- **Lack of numerous desired terms.** Structures radiologists name every day are missing.
- **Too many unnecessary or degenerate terms.** Several concepts denote the same structure, so a coder has no principled way to choose one and a consumer cannot tell two records mean the same place.
- **Limited anatomic organization.** The hierarchy that exists does not answer the question imaging asks, which is what physically contains what.

# Curation as the answer

The response is a curated subset rather than a new ontology: "We are curating a subset of anatomic concepts from existing ontologies and shaping them into a usable collection of anatomic identifiers for informatics interoperability."[^al-site] The method was to start from RadLex terms already recognized in radiology reports, keep the used and useful ones, place each in an anatomic hierarchy, attach cross-references to other ontologies, and record [laterality](/glossary/laterality.md) and sex phenotype.[^al-site]

Two properties are claimed for the result and are the point of the exercise. It is complete enough, containing "almost all clinically used anatomic terms." It is non-degenerate, with "no uncertainty as to which node represents a structure."[^al-site] Non-degeneracy is what makes the identifier usable as a join key. See [anatomic location](/glossary/anatomic-location.md) for the term itself and [the data model](/semantic-foundation/anatomic-locations/data-model.md) for the record shape.

# Separable identity

Anatomy is one of the two axes of an [Observation](/glossary/observation.md), and the model keeps it separate from the other. The January 2026 status update states the atomic unit as "what plus where plus attributes: finding tag plus anatomic location plus lesion characteristics," and says anatomy is "baked into OIFM definitions and Observation objects."[^deck] The set is "curated to identify where findings are visualized on imaging exams," which is a narrower target than anatomy in general and explains why structures with no imaging appearance are absent.[^deck]

Separating what from where is what lets a single [finding model](/glossary/finding-model.md) for a cyst serve the kidney, the liver, and the breast, and what lets the [Imaging Problem List](/glossary/imaging-problem-list.md) offer "precision filtering via anatomy-embedded definitions."[^deck]

# Where the identifiers are used

| Where | How anatomy appears |
|---|---|
| Finding model definitions | `FindingModelFull.anatomic_locations`, a list of [index codes](/glossary/index-code.md) naming the locations a finding can occupy[^fm-model] |
| [Exam Finding List](/glossary/exam-finding-list.md) observations | An optional `anatomicLocation` object of `locationId` and `locationDisplay`, a single location per observation, added on the extraction platform's development branch[^ipl-anat-plan] |
| Imaging Problem List grouping | Entries are grouped by the pair of finding code and location identifier rather than by finding code alone, so a left and a right lesion are separate problems[^ipl-anat-plan] |
| Finding and location [coding](/glossary/coding.md) | The coding pass generates search terms, searches the location index, and has a selector choose from the returned candidates, with assignment governed by a stated precedence ladder[^ipl-rules] |
| Imaging Problem List viewer | Region and organ-cluster filters, and a body schematic whose zones are driven by the location's region and laterality[^viewer-plan] |

The rule that keeps this honest is stated with the assignment rules: every assigned identifier must exist in the set, and a structure absent from it is left unassigned rather than forced to a wrong code.[^ipl-rules] That discipline turns missing terms into a visible list of requests rather than silent mis-coding. See [RadLex integration](/semantic-foundation/anatomic-locations/radlex-integration.md) for where those requests go.

# What curation costs

A curated set is a maintained artifact, not a free one. The site's own roadmap names the standing content work: review the hierarchy, add, prune, and modify; edit and improve synonyms; complete SNOMED identification.[^al-site] It also names the companion effort that has not been built, "a companion for exam types based on LOINC/RadLex Playbook exam definitions that specify all included body parts for the exam," which remains the earliest written statement of the [exam type](/glossary/exam-type.md) goal.[^al-site] See [exam types](/semantic-foundation/exam-types/overview.md).

[^al-site]: anatomiclocations.org site homepage, rationale, approach, and roadmap
[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
[^fm-model]: FindingModelFull definition, findingmodel repository, main
[^ipl-anat-plan]: Plan to add anatomic-location codes to Exam Finding Lists and an anatomy-aware Imaging Problem List
[^ipl-rules]: Anatomic location assignment rules, imaging-problem-list dev
[^viewer-plan]: Anatomy-aware viewer plan, imaging-problem-list dev
