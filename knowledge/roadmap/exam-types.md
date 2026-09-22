---
type: Roadmap
title: Exam types roadmap
description: Exam type goals, the unimplemented Playbook profile design, and unresolved ownership and data questions.
tags: [roadmap, exam-types, loinc, playbook, anatomy]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
stale_after: 2027-09-21
sources:
  - id: plan
    resource: /plans/2026-09-20-knowledgebase-build-plan.md
    title: Knowledgebase build plan, recording the project lead's exam type goals stated in the 2026-09-20 planning interview
  - id: al-site
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/docs/index.markdown
    title: anatomiclocations.org site homepage and roadmap
  - id: site-structure
    resource: https://www.openimagingdata.org/data-model-structure-and-function/
    title: "Data Model: Structure and Function, openimagingdata.org, 2024-01-25"
  - id: molu-roadmap
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/docs/product-roadmap.md
    title: med-ontology-lookup product roadmap, the domain profiles and Playbook section
  - id: molu-backlog
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/docs/plans/2026-09-05-github-issue-backlog.md
    title: GitHub issue backlog, med-ontology-lookup
  - id: ipl-readme
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/README.md
    title: imaging-problem-list README, the Exam Finding List specification
  - id: viewer-map
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/viewer/data/exam_type_mappings.json
    title: Viewer exam type display mapping table, imaging-problem-list dev branch
  - id: current-understanding
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/00-current-understanding.md
    title: Current understanding of the next-generation vocabulary work, ACR-RSNA-CDEs next-gen-2026 branch
---

# The state of the area

Open Imaging Data Model (OIDM) has no [exam type](/glossary/exam-type.md) registry, curated code list, exam-to-body-part map, or code that parses exam names into modality and anatomy. The goal appears three times across four years. One design is unimplemented, and three existing uses rely on bare [LOINC](/glossary/loinc.md) codes.

See [exam types](/semantic-foundation/exam-types/overview.md) and [existing building blocks](/semantic-foundation/exam-types/existing-building-blocks.md) for current capabilities.

# The goal as the project lead states it

In the 2026-09-20 planning interview recorded in [the knowledgebase build plan](/plans/2026-09-20-knowledgebase-build-plan.md), the project lead described the intended work in three parts.[^plan]

1. **Wrapper tooling around an existing knowledge graph**, namely the graph represented by the [LOINC/RSNA Radiology Playbook](/glossary/loinc-rsna-radiology-playbook.md) together with [RadLex](/glossary/radlex.md), rather than a new vocabulary.
2. **A set of preferred high-level entries**, at the granularity clinicians and systems actually use, the examples given being CT Chest, MRI Brain, and X-ray Knee, each marked as the preferred entry among the many Playbook codes describing variants of the same study.
3. **Tight coupling to [anatomic locations](/glossary/anatomic-location.md)**, with typed edges from an exam type to the structures it covers, distinguishing anatomy that is **always included**, which may be expressed as a hierarchy rather than a flat list, anatomy that is **usually included**, and anatomy that is **possibly included and must be checked**.

The anatomy links would tell readers and extraction tools what a study could have assessed.

# The same goal, stated earlier

The idea predates the current work in nearly the same words, twice.

The curated anatomic location set's roadmap lists, among content tasks, work on "a companion for exam types based on LOINC/RadLex Playbook exam definitions that specify all *included* body parts for the exam." That page has not changed since January 2023.[^al-site]

The site post "Data Model: Structure and Function" of 2024-01-25 names two utility libraries alongside the core model: anatomic locations for standardized body part terminology, and an exam type library based on the LOINC and RSNA Playbook, linked to anatomic locations.[^site-structure] The anatomic location library was built. The exam type library was not. The post is summarized in [site articles](/history/site-articles.md).

# The one written design

The terminology tool's product roadmap proposes named, inspectable domain profiles in place of a growing default search. Its `radiology` profile makes the Playbook first-class: RadLex, LOINC weighted toward the Playbook, [SNOMED CT](/glossary/snomed-ct.md), and [FMA](/glossary/fma.md), with [UMLS](/glossary/umls.md) as the crosswalk hub.[^molu-roadmap]

Four Playbook-specific implications are stated in it: rank procedure and orderable queries toward Playbook terms and finding queries toward the other vocabularies; teach the crosswalk the Playbook correspondences, linking a LOINC code to its historic `RPID` and to RadLex anatomy and modality attributes, recording that in the mapping provenance; detect `RPID` codes as well as LOINC-shaped codes; and do not treat every LOINC hit as radiology.[^molu-roadmap]

None of it is built. The repository's issue backlog follows a six-phase design as one tracking issue plus eleven focused ones, of which only typed provider failures is closed; the profile mechanism is part of that backlog, not a released capability.[^molu-backlog] See [med-ontology-lookup](/semantic-foundation/terminologies/med-ontology-lookup.md).

The next-generation vocabulary analysis records two constraints. The Playbook is "actively governed, and freely licensed for commercial and non-commercial use," shipping twice yearly under joint Regenstrief Institute and RSNA governance, and it "is a separate artifact" from RadLex.[^current-understanding] Current Playbook content carries ordinary LOINC codes; `RPID` identifiers are legacy and appear only as historical codes a crosswalk would need to recognize.[^molu-roadmap]

# What is unanswered

Four questions have no answer in any source, and are carried in [open questions](/roadmap/open-questions.md).

**The curated list does not exist.** The Exam Finding List specification requires exam information "keyed by a curated list of LOINC codes."[^ipl-readme] That list has never been published. Every producer of an Exam Finding List today chooses its own code.

**LOINC descriptions are inconsistent in the data.** Across the twelve sample Exam Finding Lists, one code, `29252-4`, carries two different description strings in different files, and two different codes, `36952-0` and `72133-2`, carry descriptions naming the same study, an abdomen and pelvis CT without contrast. Both are the kind of thing a curated list would resolve, and neither is resolved.

**Preferred display names exist only as an application convenience.** The viewer shortens long exam descriptions through a seven-entry lookup table keyed by the description string rather than by the LOINC code, so two description strings in the data fall through unshortened.[^viewer-map] This is the closest thing in the repositories to a preferred name per exam type.

**Nothing checks finding model scope against an exam type.** The authoring guidance states that "the scope of a finding model should match what's assessable on a given exam type, not broader." That rule is applied by judgment today, because no coded artifact exists to check against. See [exam types](/semantic-foundation/exam-types/overview.md).

Who owns this area is also unstated. No repository claims it, no issue tracks it, and the three statements of the goal come from three different repositories.

[^plan]: Exam type goals stated by the project lead in the 2026-09-20 planning interview
[^al-site]: anatomiclocations.org roadmap
[^site-structure]: "Data Model: Structure and Function", 2024-01-25
[^molu-roadmap]: med-ontology-lookup product roadmap
[^molu-backlog]: GitHub issue backlog, med-ontology-lookup
[^ipl-readme]: imaging-problem-list README, main branch
[^viewer-map]: Viewer exam type display mapping table, dev branch
[^current-understanding]: Current understanding, ACR-RSNA-CDEs next-gen-2026
