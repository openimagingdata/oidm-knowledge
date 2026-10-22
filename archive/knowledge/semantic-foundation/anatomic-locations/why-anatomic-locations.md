---
type: Concept
title: Why anatomic locations
description: Why OIDM curates anatomic identifiers and where the model uses them.
tags: [semantic-foundation, anatomic-locations, radlex, rationale]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
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

The project site states: "Standard identifiers for discrete anatomic locations would enable numerous levels of interoperability if applied broadly."[^al-site] Systems using `RID2772` agree on the kidney without sharing a database, vendor, or schema.

The site identifies three problems with adopting [RadLex](/glossary/radlex.md) or [SNOMED CT](/glossary/snomed-ct.md) directly:[^al-site]

- **Lack of numerous desired terms.** Structures radiologists name every day are missing.
- **Too many unnecessary or degenerate terms.** Several concepts denote the same structure, so a coder has no principled way to choose one and a consumer cannot tell two records mean the same place.
- **Limited anatomic organization.** The hierarchy that exists does not answer the question imaging asks, which is what physically contains what.

# Curation as the answer

"We are curating a subset of anatomic concepts from existing ontologies and shaping them into a usable collection of anatomic identifiers for informatics interoperability."[^al-site] The project selected useful RadLex terms from radiology reports, organized them in an anatomic hierarchy, and added ontology cross-references, [laterality](/glossary/laterality.md), and sex phenotype.[^al-site]

The site claims coverage of "almost all clinically used anatomic terms." It also claims "no uncertainty as to which node represents a structure."[^al-site] Unambiguous identifiers can serve as join keys. See [anatomic location](/glossary/anatomic-location.md) and [the data model](/semantic-foundation/anatomic-locations/data-model.md).

# Separable identity

An [Observation](/glossary/observation.md) separates the finding from its location. The January 2026 update describes "what plus where plus attributes: finding tag plus anatomic location plus lesion characteristics," with anatomy "baked into OIFM definitions and Observation objects."[^deck] The set is "curated to identify where findings are visualized on imaging exams," excluding structures with no imaging appearance.[^deck]

A single [finding model](/glossary/finding-model.md) for a cyst can therefore apply to the kidney, liver, or breast. The [Imaging Problem List](/glossary/imaging-problem-list.md) uses this separation for "precision filtering via anatomy-embedded definitions."[^deck]

# Where the identifiers are used

| Where | How anatomy appears |
|---|---|
| Finding model definitions | `FindingModelFull.anatomic_locations`, a list of [index codes](/glossary/index-code.md) naming the locations a finding can occupy[^fm-model] |
| [Exam Finding List](/glossary/exam-finding-list.md) observations | An optional `anatomicLocation` object of `locationId` and `locationDisplay`, a single location per observation, added on the extraction platform's development branch[^ipl-anat-plan] |
| Imaging Problem List grouping | Entries are grouped by the pair of finding code and location identifier rather than by finding code alone, so a left and a right lesion are separate problems[^ipl-anat-plan] |
| Finding and location [coding](/glossary/coding.md) | The coding pass generates search terms, searches the location index, and has a selector choose from the returned candidates, with assignment governed by a stated precedence ladder[^ipl-rules] |
| Imaging Problem List viewer | Region and organ-cluster filters, and a body schematic whose zones are driven by the location's region and laterality[^viewer-plan] |

Every assigned identifier must exist in the set. Missing structures stay unassigned to avoid incorrect codes.[^ipl-rules] See [RadLex integration](/semantic-foundation/anatomic-locations/radlex-integration.md) for term requests.

# What curation costs

The site's roadmap calls for reviewing, adding, pruning, and modifying hierarchy nodes, improving synonyms, and completing SNOMED identification.[^al-site] It also proposes "a companion for exam types based on LOINC/RadLex Playbook exam definitions that specify all included body parts for the exam," the earliest written [exam type](/glossary/exam-type.md) goal.[^al-site] It remains unbuilt. See [exam types](/semantic-foundation/exam-types/overview.md).

[^al-site]: anatomiclocations.org site homepage, rationale, approach, and roadmap
[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
[^fm-model]: FindingModelFull definition, findingmodel repository, main
[^ipl-anat-plan]: Plan to add anatomic-location codes to Exam Finding Lists and an anatomy-aware Imaging Problem List
[^ipl-rules]: Anatomic location assignment rules, imaging-problem-list dev
[^viewer-plan]: Anatomy-aware viewer plan, imaging-problem-list dev
