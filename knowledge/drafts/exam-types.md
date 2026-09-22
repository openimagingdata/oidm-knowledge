---
type: Concept
title: Exam types
description: A stated goal with no artifact - preferred high-level exam entries over the LOINC/RSNA Radiology Playbook, the Playbook properties they would expose, and the anatomy coverage edges in the project lead's two dated phrasings.
tags: [foundation-context, exam-types, loinc, playbook, radlex]
status: draft
generated: { by: claude-opus-5/2026-09-22-restructure/draft-axes, at: 2026-09-22T12:53:11Z }
sources:
  - id: brief
    resource: /plans/2026-09-20-knowledgebase-build-plan.md
    title: The project lead's stated goals, recorded verbatim from the request of 2026-09-20
  - id: siim2026
    resource: t3://oidm-public/oidm-knowledge-sources/SIIM%202026%20Reports-of-the-Future.pptx
    title: Structured Results and Context for Next-Generation Imaging Resulting Tools, SIIM 2026 annual meeting talk, June 2026, Mass General Brigham, slides 8 and 11
  - id: al-site
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/docs/index.markdown
    title: Anatomic Locations project site roadmap, content tasks, unchanged since January 2023
  - id: board-anatomy
    resource: https://link.excalidraw.com/l/AxEw4sqe6bu/4jmRPObEdLq
    title: Common Anatomic Locations working board, Exam Types box, with a discussion checklist dated 2024-05-28
  - id: molu-roadmap
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/9cc3eec2c7af32e366e3f05e027b223b4a870077/docs/product-roadmap.md
    title: "Product direction: an agent-ready medical terminology graph gateway, med-ontology-lookup, research date 2026-08-16, status recommended direction"
  - id: jdim-al
    resource: "Anatomic Locations Index: A Spatial Containment Hierarchy for Localizing Imaging Findings, manuscript under review at the Journal of Digital Imaging and Informatics in Medicine, 2026"
    title: Manuscript under review, Discussion section on scan-protocol coverage; reviewer correspondence not used
  - id: ipl-rules
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/anatomic-location-assignment-rules.md
    title: Anatomic location assignment rules, imaging-problem-list dev branch, the precedence ladder and the exam-scoped region fallback
  - id: ipl-efl
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/sample_data/example2/ct_abdomen_20210826_efl.json
    title: Exam Finding List sample with a LOINC-coded exam header, imaging-problem-list dev branch
---

# Nothing is built

No exam type artifact exists in any OIDM repository. Everything on this page is either a stated goal or a written proposal, each dated. The nearest running behavior is that an [exam type](/glossary/exam-type.md) appears as a bare LOINC code in an Exam Finding List header,[^ipl-efl] and as the last rung of the anatomy precedence ladder: when a report gives no explicit anatomy and the finding has no target organ, the location falls back to the exam-scoped coarse region, sided only if the exam is sided.[^ipl-rules] Both belong to [Data Structures](./data-structures.md).

# Preferred high-level entries over the Playbook

The goal has been stated in nearly the same words across four years, and it is always a wrapper rather than a new vocabulary.

| Date | Statement |
|---|---|
| January 2023 | The project site roadmap lists, under content tasks, a companion for exam types based on LOINC and RadLex Playbook exam definitions that specify all included body parts.[^al-site] |
| 2024 | A working board's Exam Types box lists exam type definitions of the most common exams based on LOINC, with common identifiers.[^board-anatomy] |
| 2026-09-20 | The project lead's brief: exam types need "wrapper tooling around the knowledge graph represented by RadLex LOINC playbook", and the project needs "to define the PREFERRED high-level entries like 'CT Chest', 'MRI Brain', 'X-ray Knee'."[^brief] |
| June 2026 | The SIIM talk shows Exam Type as one of three axes, each an OIDM layer over an existing standard; the exam type axis layers over [LOINC Playbook](/glossary/loinc-rsna-radiology-playbook.md) study types.[^siim2026] |

The brief's word is "PREFERRED": the goal is to mark, among the Playbook's many entries, the high-level ones such as "CT Chest" that the project wants systems to use.[^brief]

# What the layer would expose

The June 2026 talk describes Exam Type as a thin layer on top of the RadLex/LOINC Playbook whose value is access to information the Playbook already holds: timing, contrast, and sidedness among them. It also states that broad families of exams are being grouped together, giving "CT Chest" and "MR Knee" as the examples.[^siim2026] That is the same grouping idea the brief states as preferred high-level entries.[^brief]

# Anatomy coverage edges, in two dated phrasings

The project lead has stated the connection to anatomy twice, in different words, three months apart. Both are recorded here as given; neither supersedes the other on the evidence available.

**2026-09-20, the brief.** Exam types need "to TIGHTLY wrap up with Anatomic Locations, including edges for both 'always included' (which can include hierarchies) as well as 'usually included' (for edge things) and something like 'POSSIBLY included, would have to check'."[^brief]

**June 2026, the SIIM talk.** Under "Connect to Anatomic Locations", the slide lists focused anatomy, included anatomy, and "edge" anatomy, the last qualified as usually versus possible.[^siim2026]

The two overlap but do not map one to one. The talk's *focused* anatomy has no counterpart in the brief, and the brief's *always included* has none in the talk.

The manuscript under review names the same capability from the other side, as something the [anatomic location](/glossary/anatomic-location.md) index does not supply: relating a finding's location to what an examination covers would additionally require a model of scan-protocol coverage. It states the use case that would be served, identifying relevant prior studies that cover overlapping anatomy even when acquired for different clinical purposes.[^jdim-al]

# The imaging region

The 2024 board states the same requirement as defining an imaging region: a "CT chest region" contains the chest, but also what a radiology exam of the chest would include, such as the lower neck, the upper abdomen, and the shoulders.[^board-anatomy] The January 2023 site roadmap puts it as exam definitions specifying all included body parts.[^al-site]

# The one written design

The only written design touching exam types is the terminology gateway's product roadmap, dated 2026-08-16 and labeled a recommended direction rather than a built capability. It proposes named domain profiles in place of an ever-growing default search, with `radiology` as the default profile, and places the Playbook in that default on the stated ground that radiology orderables live in the LOINC/RSNA Radiology Playbook while findings, anatomy, and report language live in RadLex.[^molu-roadmap]

Four Playbook implications are stated: rank procedure and orderable queries toward Playbook terms while ranking finding and anatomy queries toward RadLex, SNOMED CT, and FMA; teach the crosswalk the Playbook correspondences linking a LOINC code to its historic RadLex Playbook identifier and to RadLex anatomy and modality attributes, recording that in the mapping provenance; detect Playbook identifiers as well as LOINC-shaped codes; and prefer Playbook or radiology-class hits rather than treating every LOINC hit as radiology.[^molu-roadmap] The tool itself belongs to the SDKs pillar; see [SDKs](./sdks.md). The standards each axis layers over are covered in [standards](./standards.md).

[^brief]: The project lead's stated goals, 2026-09-20
[^siim2026]: SIIM 2026 annual meeting talk, June 2026, Mass General Brigham
[^al-site]: Anatomic Locations project site roadmap, January 2023
[^board-anatomy]: Common Anatomic Locations working board, Exam Types box
[^molu-roadmap]: Product direction, med-ontology-lookup, 2026-08-16
[^jdim-al]: Anatomic Locations Index manuscript, under review at the Journal of Digital Imaging and Informatics in Medicine, 2026
[^ipl-rules]: Anatomic location assignment rules, imaging-problem-list
[^ipl-efl]: Exam Finding List sample with a LOINC-coded exam header, imaging-problem-list
