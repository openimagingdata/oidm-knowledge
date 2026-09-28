---
type: Concept
title: Data Structures
description: Observations connect a patient's imaging results to shared definitions and to one another across reports and examinations.
tags: [data-structures, observation, foundation-context, imaging-problem-list]
status: draft
generated: { by: codex/2026-09-22-restructure, at: 2026-09-22T13:54:25Z }
sources:
  - id: siim-context
    resource: https://oidm-public.t3.tigrisfiles.io/oidm-knowledge-sources/SIIM%202026%20Reports-of-the-Future.pptx
    title: Reports of the Future, June 2026, slides 4–8 and 12
  - id: report-graph
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/03-draft-structures.md
    title: Next-generation CDE draft structures, section 5, snapshot 2026-09-15
  - id: report-decisions
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/plans/2026-09-03-report-plane-example.md
    title: Report-plane example, owner decisions and Claude defaults, 2026-09-03
  - id: two-graph-example
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/08-worked-examples.md#4-one-report-two-planes
    title: Pyelonephritis worked example, snapshot 2026-09-15
  - id: ipl-manuscript
    resource: Imaging Problem List manuscript, JDIM-D-26-02980 R1, under review at JDIM in 2026; clean manuscript and figures held in the source collection
    title: Imaging Problem List manuscript, JDIM-D-26-02980 R1, under review, read 2026-09-22
  - id: webinar
    resource: https://oidm-public.t3.tigrisfiles.io/oidm-knowledge-sources/IPL%20Webinar%20Deck.html
    title: Imaging Problem List SIIM webinar, 2026-07-15
  - id: cde-decisions
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/10-decision-record-2026-09-02.md
    title: CDE decision record, S19–S26, snapshot 2026-09-15
  - id: sample-efls
    resource: https://github.com/openimagingdata/imaging-problem-list/tree/36fa30c7383bf687d7bc17815282a93e123a56cb/sample_data/example2
    title: Example2 Exam Finding Lists, development snapshot 2026-07-22
  - id: technical-findings
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/technical-imaging-findings.md
    title: Technical imaging findings, draft reference at 2026-07-22
  - id: domain-notes
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/CLAUDE.md
    title: IPL domain notes, development snapshot 2026-07-22
  - id: extraction-prompt
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/src/finding_extractor/extractor/prompt.py
    title: Extraction prompt, development snapshot 2026-07-22
  - id: coding-prompt
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/src/finding_extractor/coding/prompt.py
    title: Finding and location coding prompts, development snapshot 2026-07-22
  - id: extraction-review
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/prompts/validator_prompt_example.md
    title: Chunk reviewer contract, development snapshot 2026-07-22
  - id: anatomy-rules
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/anatomic-location-assignment-rules.md
    title: Anatomic location assignment rules, development snapshot 2026-07-22
  - id: ipl-generator
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/scripts/generate_ipl_from_efls.py
    title: EFL aggregation into an IPL, development snapshot 2026-07-22
  - id: sample-ipl
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/sample_data/example2/MRN0000001_ipl.json
    title: Synthetic patient IPL, development snapshot 2026-07-22
  - id: viewer-status
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/scripts/build_viewer_v2_data.py
    title: Anatomy viewer data builder, development snapshot 2026-07-22
  - id: ipl-readme
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/README.md
    title: IPL README, development snapshot 2026-07-22
  - id: jacr-study
    resource: Follow-Up Chest CT Reporting Is Mostly Re-Documentation, manuscript prepared for submission in 2026, held in the source collection
    title: Follow-Up Chest CT Reporting Is Mostly Re-Documentation, prepared for submission, read 2026-09-22
  - id: owner-notes
    resource: Project lead's manuscript notes, 2026-09-19, sources/email/2026-09-19-ipl-manuscript-notes.md
    title: Observations, finding identity, and structures versus transport, 2026-09-19
  - id: context-board
    resource: https://link.excalidraw.com/l/AxEw4sqe6bu/1sEx11UZ3gq
    title: OIDM Object Model board, January 2024 proposal, transcribed 2026-09-21
  - id: report-board
    resource: Structured Report Representation, internal working board, schema content transcribed in the local source collection
    title: Structured Report Representation board, schema proposals from 2025
  - id: outcome-board
    resource: https://link.excalidraw.com/l/AxEw4sqe6bu/68X9qfSP5qA
    title: Outcome Tracking Schema board, transcribed 2026-09-21
  - id: idr-extract
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md
    title: Team extract of the IHE IDR Phase II public-comment draft, read 2026-08-21
---

# Data Structures

The June 2026 presentation describes a compact Observation with codes pointing to [Foundation Context](./foundation-context.md), plus presence, change from prior, and characterization attributes. Observations belong to Patient Context alongside wider clinical information. Shared knowledge is resolved through their codes.[^siim-context] The July example2 Exam Finding Lists populate only presence in their attribute arrays, a narrower implementation than the deck describes.[^sample-efls]

## Two connected graphs

The next-generation CDE design calls these two graphs “planes”: shared definitions and observations in a report. An observation points to its subject definition, anatomic location, and the data elements whose values it records. It retains source wording and can link to other observations.[^report-graph]

The June deck's calculus figure shows the connection. One patient observation resolves through an SDK to a calculus definition, which may cause hydronephrosis. The definitions connect to kidney and renal pelvis; the figure does not assert hydronephrosis in this patient. Its relationship is general knowledge.[^siim-context]

Relationships between definitions describe general possibilities. Relationships between observations record what this report asserts about this patient. In the [pyelonephritis example](https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/08-worked-examples.md#4-one-report-two-planes), shared definitions connect a diagnosis to its possible manifestations; report observations connect the particular findings to the diagnosis the radiologist states. The absent abscess remains an observation with an absent presence value. The report relationship itself is not negated and does not point to a vocabulary relationship. This is a hypothetical worked example.[^two-graph-example]

The decision record marks that separation as owner decisions S21–S24. The edge name `SUPPORTS` and the convention of retaining the radiologist's wording in `confidence` are Claude defaults S25–S26.[^report-decisions][^cde-decisions] Components use the same distinction: a definition's `MAY_HAVE_COMPONENT` describes a possibility; a report's `HAS_COMPONENT` connects the actual nodule and solid-component observations, each with its own measurements.[^report-graph]

These sources develop related representations with different scope:

| Source and status | What it represents |
|---|---|
| CDE graph draft, snapshot 2026-09-15 | Assertions within one report, linked to definitions and to other assertions, with exact text and spans.[^report-graph] |
| IPL implementation, snapshot 2026-07-22 | Coded observations collected by examination and grouped across examinations using finding code and location.[^ipl-generator] |
| JDIM IPL manuscript, R1 under review, read 2026-09-22 | Longitudinal finding identity, observation histories, provenance, derived status, and proposed linking rules.[^ipl-manuscript] |

## Observations and their evidence

The extraction and coding prompts separate finding type, location, and presence. Absence does not change which finding or anatomy code is appropriate. Normality becomes an appropriately scoped absent abnormality; a blanket negative must not introduce more specific claims than its wording supports. Coding may use a slightly broader concept but must not add specificity, and can leave a finding uncoded or unlocalized with a reason.[^extraction-prompt][^coding-prompt][^extraction-review]

The rules agreed for the example2 correction pass, intended to guide later automated coding, choose explicit report or section anatomy first, then the finding's target structure, then a coarse exam region. They retain section-level laterality, split separable bilateral findings, and keep diffuse or midline findings unsided. The July coding prompt separately allows multiple locations and generates sided terms for bilateral anatomy.[^anatomy-rules][^coding-prompt]

Presence and confidence also differ:

| Source | Representation |
|---|---|
| July 2026 webinar and JDIM R1 manuscript | Present or absent, with a separate hedge on the assertion or attribute it qualifies.[^webinar][^ipl-manuscript] |
| July 2026 extraction prompt | `present`, `absent`, `possible`, `indeterminate`; uncertainty about the finding differs from inability to determine it.[^extraction-prompt] |
| July 2026 example2 data | `present`, `absent`, `indeterminate`, without a separate confidence field.[^sample-ipl] |

For technical descriptions, the term-generation prompt forbids inferring a diagnosis, while the selector asks for the underlying clinical concept. The draft technical-findings reference also distinguishes observed signal abnormalities from diagnoses. These sources do not settle how the selector's broader instruction applies.[^coding-prompt][^technical-findings]

## Exam Finding Lists

The manuscript organizes findings at two levels: an Exam Finding List for one examination and an Imaging Problem List across examinations, because interpretation spans both. The June deck connects the EFL to IHE Imaging Diagnostic Report and places both lists within broader Patient Context.[^ipl-manuscript][^siim-context] The EFL must retain stated comparisons, time course, explicit negatives, and supporting sentences. Silence adds no observation. The JACR study illustrates the fidelity problem: its extractor sometimes turned a neutral measurement into an abnormality the radiologist had not asserted.[^ipl-manuscript][^jacr-study]

The chunk reviewer contract checks both directions: every extracted assertion needs evidence, and every finding in the source needs representation. It names unsupported content, omissions, wrong presence, excess specificity, incorrect blanket negatives, and location errors as reasons to re-extract. The [extraction platform](./sample-applications.md) implements this review workflow.[^extraction-review]

The manuscript combines repeated descriptions into one observation per finding per examination. The project lead's September notes emphasize that one finding may have several observations within a report. The implemented extractor prioritizes detailed body text and adds impression findings only when they are distinct; the IPL aggregator can retain multiple observations from the same exam. These choices remain visible rather than being collapsed into one cardinality rule.[^ipl-manuscript][^owner-notes][^extraction-prompt][^ipl-generator]

The 2025 report-structure board asks how to represent impression, recommendations, communication, comparison, technique, clinical context, and limitations. Its open questions concern impression observations, grouped findings, and causal relationships, also explored in the [two-graph design](#two-connected-graphs). The extractor labels non-finding text without implementing these richer structures.[^report-board][^extraction-prompt][^report-graph]

## Imaging Problem Lists

An Imaging Problem List collects a finding's observations across examinations. The manuscript proposes a persistent entry with a tracking identifier, identified principally by finding code and anatomic site. The project lead's notes require accounting for broader or narrower codes, finding-to-diagnosis changes, and evolution such as an acute fracture becoming healed.[^ipl-manuscript][^owner-notes]

Finding and diagnosis remain distinct modeling choices. JDIM R1 records the diagnosis or assessment on the finding's observation. The September CDE draft also represents a diagnosis as the subject of its own observation, connected to supporting findings. The September 19 notes call for making the IPL's account of that distinction explicit.[^ipl-manuscript][^report-graph][^owner-notes]

Entity resolution remains open: which observations refer to the same finding? The July implementation groups exact code-and-location pairs and regenerates numbered entry IDs from sorted groups; it does not establish durable identity across rebuilds. Generic and specific locations can form separate entries.[^ipl-generator][^anatomy-rules] The JDIM manuscript proposes graduated linking evidence, led by an explicit comparison to a prior finding. The JACR measurement uses ordered matching rules and retains ambiguous cases separately. These serve different purposes and remain distinct formulations.[^ipl-manuscript][^jacr-study]

Status is derived from observations, but the vocabulary varies:

| Source | Status and trajectory |
|---|---|
| JDIM R1 manuscript, under review | Active, Stable, Resolved, Excluded. Trajectory is read from the observation history.[^ipl-manuscript] |
| SIIM webinar, 2026-07-15 | Slide 21 proposes Active or Resolved, with trajectories within Active. Slide 22 also uses Stable in its example.[^webinar] |
| IPL domain notes, 2026-07-22 | Currently present, resolved, never-present or ruled out.[^domain-notes] |
| Anatomy viewer builder, 2026-07-22 | `current`, `always`, `resolved`, `never_present`, stored in the generated bundle. An empty history returns `unknown` and aborts the build.[^viewer-status] |

The manuscript proposes a succession link when one entity leaves another behind, such as resolved pneumonia followed by scarring. For observations in signed reports, it puts provenance and review on each observation, retaining model identity, inputs, output, source text, and subsequent human decisions. Model-produced observations remain unreviewed until a radiologist affirms or rejects them; status follows rules over the observations and links. Merging, splitting, and marking errors are provenance operations, separate from status. The July IPL sample does not carry this proposed provenance or succession structure.[^ipl-manuscript][^sample-ipl]

The JACR study supplies the motivation for retaining the whole history: 77.4% of unhedged chronic findings on follow-up chest CT were repeated without change. Most accumulated IPL entries went unmentioned on an individual exam. The manuscript therefore calls for ranking entries for display, using permanence as one signal. Permanence comes from the finding type, not inference from repeated observations. These are results and implications of a manuscript prepared for submission.[^jacr-study]

Recommendations remain a separate design question. The outcome board proposes an exam or protocol, timeframe, target, conditions, and citation, plus live or closed entries. The JDIM manuscript attaches recommendations and their closure to an entry while deriving finding status from observations. The location of the live/closed distinction remains unresolved.[^outcome-board][^ipl-manuscript]

## Broader context and transport

The June deck places Imaging Persona around imaging results and clinical context. The object-model board's January 2024 proposal includes orders, prior reports, tracked observations, EHR information, studies, and current report text. Their application role appears in [Use Cases](./use-cases.md).[^siim-context][^context-board]

The project lead's September 19 direction is to define structures applications can read and create, then use those structures to guide transport mappings.[^owner-notes]

| Dated source | Documented FHIR mapping |
|---|---|
| IPL README, July 2026 | EFL as `DiagnosticReport` with `Observation` components; IPL as a “Report” containing `Condition` objects and their observations.[^ipl-readme] |
| JDIM R1, under review, read September 2026 | EFL observation as `Observation`, report as `DiagnosticReport`, site as `BodyStructure`, entry as `List` or a custom profile, succession as a reference or extension, review as `Provenance`; status remains derived.[^ipl-manuscript] |
| Team's August 2026 extract of the March IHE IDR draft | IDR routes positive clinical findings to `Condition`, negatives to `Observation`, and Finding Sets through member observations. The team explicitly records its different working default: all report assertions, diagnoses included, as `Observation`.[^idr-extract] |

The July IPL prototype stores its own JSON structure rather than implementing either proposed IPL transport mapping.[^ipl-generator] [Sample Applications](./sample-applications.md) shows implemented examples; [SDKs](./sdks.md) covers developer capabilities around the structures.

[^siim-context]: June 2026 [presentation](https://oidm-public.t3.tigrisfiles.io/oidm-knowledge-sources/SIIM%202026%20Reports-of-the-Future.pptx), slides 4–8 and 12.
[^report-graph]: [Draft structures, section 5](https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/03-draft-structures.md#5-two-planes-reports-point-into-the-vocabulary).
[^report-decisions]: [Report-plane decisions](https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/plans/2026-09-03-report-plane-example.md), owner directions and Claude defaults.
[^two-graph-example]: [Worked example, section 4](https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/08-worked-examples.md#4-one-report-two-planes).
[^ipl-manuscript]: JDIM-D-26-02980 R1, under review, printed pp. 6–12 and 15–16, and Table 1. Paraphrased from the clean manuscript and table, read 2026-09-22; reviewer correspondence excluded.
[^webinar]: SIIM webinar, 2026-07-15, slides 17–23 and their notes, numbered in file order rather than by printed slide labels.
[^cde-decisions]: CDE decision record at `44836c19`, rows S19–S26, including explicit OWNER and CLAUDE DEFAULT labels.
[^sample-efls]: Example2 `*_efl.json` files at `36fa30c`, all 276 observations' attribute arrays inspected.
[^technical-findings]: Technical Imaging Findings draft reference at `36fa30c`, CT, MR, and enhancement search considerations.
[^domain-notes]: IPL `CLAUDE.md` at `36fa30c`, Domain Model and temporal-status descriptions.
[^extraction-prompt]: [Extraction prompt](https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/src/finding_extractor/extractor/prompt.py), core, deduplication, presence, non-finding, and chunk rules.
[^coding-prompt]: [Coding prompts](https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/src/finding_extractor/coding/prompt.py), term generation and code selection.
[^extraction-review]: [Reviewer contract](https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/prompts/validator_prompt_example.md), evidence boundary and named failure types.
[^anatomy-rules]: [Assignment rules](https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/anatomic-location-assignment-rules.md), including the known reconciliation limitation.
[^ipl-generator]: [IPL generator](https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/scripts/generate_ipl_from_efls.py), grouping and observation history.
[^sample-ipl]: [example2 IPL](https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/sample_data/example2/MRN0000001_ipl.json).
[^viewer-status]: [Viewer data builder](https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/scripts/build_viewer_v2_data.py), `compute_status` and `statusByFindingId`.
[^ipl-readme]: [IPL README](https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/README.md), EFL and IPL sections.
[^jacr-study]: JACR manuscript prepared for submission, Methods, Results, and Discussion. Paraphrased from the version read 2026-09-22.
[^owner-notes]: Project lead's manuscript notes, 2026-09-19, points 1–5. Retained in the local source collection.
[^context-board]: OIDM Object Model board, mind map and class diagram, transcription read 2026-09-22.
[^report-board]: Structured Report Representation board, schema questions recorded in 2025, transcription read 2026-09-22.
[^outcome-board]: Outcome Tracking Schema board, Recommendation Structure and Imaging Problem List boxes, transcription read 2026-09-22.
[^idr-extract]: [Team's IHE IDR extract](https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md), sections 1–4 and 6, read from the March 2026 public-comment draft in August 2026.
