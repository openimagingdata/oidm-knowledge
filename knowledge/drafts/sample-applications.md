---
type: Concept
title: Sample Applications
description: Applications that author shared definitions, display imaging histories, extract and review findings, and demonstrate structured exchange.
tags: [applications, authoring, imaging-history, extraction, interoperability]
status: draft
generated: { by: codex/2026-09-22-restructure-sample-applications, at: 2026-09-22T13:52:23Z }
sources:
  - id: forge-workflow
    resource: https://github.com/openimagingdata/FindingModelForge/blob/15d9ebcf64734b889081feed4d645a0afca67e61/docs/finding-model-creation-workflow.md
    title: Finding Model Forge creation workflow, dev snapshot of 2026-01-02
  - id: forge-drafts
    resource: https://github.com/openimagingdata/FindingModelForge/blob/15d9ebcf64734b889081feed4d645a0afca67e61/docs/DRAFT_WORKFLOW.md
    title: Finding Model Forge draft lifecycle, dev snapshot of 2026-01-02
  - id: catalog-loader
    resource: https://github.com/openimagingdata/finding-models-site/blob/6298fa3b900bb46b488f82d0a5b9aab06f70ca69/src/data/loadFindingModels.ts
    title: Finding model catalog loader, main snapshot of 2025-06-19
  - id: catalog-page
    resource: https://github.com/openimagingdata/finding-models-site/blob/6298fa3b900bb46b488f82d0a5b9aab06f70ca69/src/pages/models/%5Bslug%5D.astro
    title: Finding model catalog detail page, main snapshot of 2025-06-19
  - id: findingmodel-cli
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/README.md
    title: Findingmodel command-line tools, main snapshot of 2026-03-04
  - id: anatomy-cli
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/docs/anatomic-locations.md
    title: Anatomic locations command-line tools, main snapshot of 2026-03-04
  - id: viewer-one
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/viewer/app.js
    title: IPL viewer implementation, main snapshot of 2025-11-18
  - id: viewer-one-notes
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/CLAUDE.md
    title: IPL viewer notes, main snapshot of 2025-11-18
  - id: viewer-demos
    resource: https://oidm-public.t3.tigrisfiles.io/oidm-knowledge-sources/IPL%20Webinar%20Deck.html
    title: SIIM IPL webinar, 2026-07-15, live prototype slides 26 and 33
  - id: viewer-two
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/viewer-v2-anatomy-dashboard.md
    title: Anatomy viewer implementation and design, dev snapshot of 2026-07-22
  - id: viewer-metadata
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/viewer_v2/src/App.tsx
    title: Anatomy viewer instance, definition, and anatomy panels, dev snapshot of 2026-07-22
  - id: extraction-platform
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/README.md
    title: Extraction and persistence platform, dev snapshot of 2026-07-22
  - id: extraction-internals
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/extraction-internals.md
    title: Extraction and reviewer contracts, dev snapshot of 2026-07-22
  - id: coding-design
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/coding-agent-design.md
    title: Independent coding pipeline design, updated 2026-03-16
  - id: validator-prompt
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/prompts/validator_prompt_example.md
    title: Chunk reviewer prompt and failure taxonomy, dev snapshot of 2026-07-22
  - id: human-review
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/extraction-reviewer-ux.md
    title: Standalone extraction reviewer, implementation review of 2026-07-20
  - id: evaluation-plan
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/extractor-evals-redesign.md
    title: Extractor evaluation redesign, scope decision of 2026-07-07
  - id: local-policy
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/src/finding_extractor/llm/policy.py
    title: Local inference policy implementation, dev snapshot of 2026-07-22
  - id: local-limits
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/local-only-future-tightening.md
    title: Local-only operation, documented limits and deferred checks, dev snapshot of 2026-07-22
  - id: early-pipeline
    resource: https://github.com/openimagingdata/IPL-MVP-ExtractionAndLabeling/blob/b06948fa417aeff0a6a4b97729c915b3ce5d5ed4/README.md
    title: Earlier extraction and labeling pipeline, main snapshot of 2025-10-20
  - id: early-prompt
    resource: https://github.com/openimagingdata/IPL-MVP-ExtractionAndLabeling/blob/b06948fa417aeff0a6a4b97729c915b3ce5d5ed4/config.py
    title: Earlier extraction prompt and matching threshold, main snapshot of 2025-10-20
  - id: siim-rendering
    resource: https://www.openimagingdata.org/siim-update/
    title: OIDM SIIM Update, completed template-rendering demonstration, 2023-06-26
  - id: template-demo
    resource: https://github.com/openimagingdata/CDETemplateDemo/blob/e09f2553de58b2c88ea26e9673750a62803d4dbc/mapper-logic/src/mappers/obsToMustache.ts
    title: CDE Template Demo observation-to-template renderer, master snapshot of 2023-06-15
  - id: siim-search
    resource: https://www.openimagingdata.org/siim-2024-update-hackathon-edition/
    title: OIDM SIIM 2024 Update, completed ontology-search demonstration, 2024-07-02
  - id: rsna-team-demo
    resource: https://www.openimagingdata.org/2024-new-year-update/
    title: OIDM 2024 New Year Update, reporting framework and AI in Practice demonstrations, 2024-01-12
  - id: nodule-workflow
    resource: Internal source archive, Pulm Nodule Demo Project working board, schema and workflow portions only
    title: Pulm Nodule Demo Project, undated working board, schema and workflow content
---

# Sample Applications

These examples accompany [Foundation Context](./foundation-context.md), [Data Structures](./data-structures.md), and [SDKs](./sdks.md). [Use Cases](./use-cases.md) describes the team's proposed applications. The implementation dates below identify the source versions.

## Authoring and inspecting shared definitions

[Finding Model Forge](https://fmf.oidm.org) provides a browser workflow for authoring [finding models](./finding-models-and-cdes.md). In its January 2026 development version, users review an AI-generated description, check for similar models, and edit attributes before generating a model with identifiers and standard codes. Submission locks the draft for review. The lifecycle distinguishes drafting, submission, review, acceptance into the collection, and rejection.[^forge-workflow][^forge-drafts]

The [catalog site](https://openimagingdata.github.io/finding-models-site/) provides a reading interface to those definitions. Its June 2025 implementation builds pages from the definition files, showing each model's name, description, and raw JSON.[^catalog-loader][^catalog-page]

The March 2026 command-line tools expose other ways to inspect that content. `findingmodel` searches definitions, validates their JSON, and renders Markdown. `anatomic-locations` looks up locations by identifier, name, or synonym and displays containment ancestors and descendants. These are applications of the reusable packages described under [SDKs](./sdks.md).[^findingmodel-cli][^anatomy-cli]

The team's SIIM 2024 hackathon front end demonstrated full-text and semantic search across Anatomic Locations, RadLex, and SNOMED CT, returning ranked candidates from six searches.[^siim-search]

## Viewing a patient's imaging history

The [first Imaging Problem List viewer](https://imaging-problem-list.pages.dev) connects the [longitudinal finding list](./data-structures.md) to individual Exam Finding Lists and report text.[^viewer-demos] In the November 2025 `main` code, status filters distinguish present, resolved, and never-present findings. Its body-region filter uses a curated finding-to-region table, although the repository notes describe keyword inference.[^viewer-one][^viewer-one-notes]

The [second viewer](https://main.ipl-anatomy.pages.dev), also demonstrated in the July 2026 webinar, uses coded anatomy for a body-map display.[^viewer-demos] Its July 2026 development version provides progressive drill-down to findings, observations, and source reports. Its design explicitly prohibits anatomy grouping from merging or splitting IPL entries. Generic or unspecified laterality stays separate from left and right, and unresolved anatomy remains visible as unlocalized.[^viewer-two]

The detail view separates patient instance data, finding-definition metadata, and anatomy metadata. A reader can distinguish the finding's actual site and history from the definition's typical anatomy. The interface also displays warnings for missing definitions, missing anatomy, and evidence text that cannot be matched exactly.[^viewer-metadata][^viewer-two]

## Extracting, coding, and reviewing reports

The July 2026 `imaging-problem-list` development version implements report extraction and persistence for [structured imaging findings](./data-structures.md). It stores each extraction with its report, model, reasoning setting, and output. Reviewer corrections are separate objects for additions, changes, or comments.[^extraction-platform]

Coding is an independent job that can run again over a saved extraction. Exact-name or synonym lookup comes first. Unresolved findings go through search-term generation, index search, and code selection, with finding type and anatomic location handled separately. One finding's coding failure does not block the others.[^coding-design]

Extraction works in report chunks and requires verbatim supporting text. A different model can review each chunk and request targeted re-extraction. Its failure taxonomy covers unsupported content, missed findings, wrong presence, excessive specificity, mishandled blanket negatives, and incorrect location. Review timeouts do not stop the pipeline, and output can complete with explicit warnings.[^extraction-internals][^validator-prompt]

The standalone human-review application opens as a local HTML file without a runtime network connection. Reviewers approve, flag, or mark findings unsure, inspect their evidence in the full report, record missed findings, and export review decisions.[^human-review]

The July 2026 evaluation redesign remains a plan. It rejects raw finding yield as evidence of better recall because fabricated findings can increase yield. The proposed replacement matches evidence quotes first, scores attribute values, freezes run settings, and compares outputs with human-adjudicated gold held out from prompt examples.[^evaluation-plan]

For protected reports, the platform supports local Ollama and approved on-premises vLLM inference. Its local-only policy has documented limits, including undetected cloud aliases and first-use model downloads.[^local-policy][^local-limits]

### Earlier extraction pipeline

The October 2025 MVP separates extraction from vocabulary matching in a smaller experiment. Its prompt requests finding names and binary presence, including explicit negatives, while its README lists negation as unsupported. A second step matches names to a small definition set through embedding similarity and flags results below a threshold for review. Its README reports 5 matches among 87 extracted findings using 15 neuro finding models.[^early-prompt][^early-pipeline]

## Demonstrations of rendering and exchange

At SIIM 2023, the team demonstrated a service that renders CDE-labeled FHIR Observations as prose. Its front end let users edit sample observations and templates to change the output. The [CDE Template Demo implementation](https://github.com/openimagingdata/CDETemplateDemo/tree/e09f2553de58b2c88ea26e9673750a62803d4dbc) renders observation components through Mustache templates.[^siim-rendering][^template-demo]

The team's January 2024 update reports an OIDM-based assisted-reporting demonstration at RSNA and AI in Practice demonstrations presented by OIDM members.[^rsna-team-demo] The more detailed [pulmonary nodule exchange workflow](./use-cases.md) remains a board proposal, with tracking-ID assignment and cross-exam association open.[^nodule-workflow]

[^forge-workflow]: Finding Model Forge creation workflow, dev snapshot of 2026-01-02.
[^forge-drafts]: Finding Model Forge draft lifecycle, dev snapshot of 2026-01-02.
[^catalog-loader]: Catalog loader, main snapshot of 2025-06-19.
[^catalog-page]: Catalog detail page, main snapshot of 2025-06-19.
[^findingmodel-cli]: Findingmodel README, CLI section, main snapshot of 2026-03-04.
[^anatomy-cli]: Anatomic locations guide, CLI commands, main snapshot of 2026-03-04.
[^viewer-one]: IPL viewer code, loadFindingRegionMappings, getBodyRegions, and computeFindingStatus, main snapshot of 2025-11-18.
[^viewer-one-notes]: IPL architecture notes, IPL Viewer Application, main snapshot of 2025-11-18. These notes describe keyword inference, unlike the table lookup in the code at the same commit.
[^viewer-demos]: SIIM IPL webinar, 2026-07-15, slides 26 and 33. The slides identify the two live prototype addresses.
[^viewer-two]: Anatomy viewer plan, implementation notes and anatomy mapping rules, dev snapshot of 2026-07-22.
[^viewer-metadata]: Anatomy viewer application, MetadataSections, ObservationDrilldown, and warning display, dev snapshot of 2026-07-22.
[^extraction-platform]: IPL README, extraction and persistence sections, dev snapshot of 2026-07-22.
[^extraction-internals]: Extraction internals, chunk and reviewer contracts and terminal outcomes, dev snapshot of 2026-07-22.
[^coding-design]: Coding Agent Design, independent-job architecture and failure handling, updated 2026-03-16.
[^validator-prompt]: Validator prompt, issue taxonomy and evidence boundary, dev snapshot of 2026-07-22.
[^human-review]: Extraction Reviewer UX plan, verified implementation update of 2026-07-20.
[^evaluation-plan]: Extractor Evals Redesign Plan, scope decision and core decisions of 2026-07-07.
[^local-policy]: Inference policy, enforce_local_only, dev snapshot of 2026-07-22.
[^local-limits]: Future Local-Only Tightening, deferred alias detection and model-download behavior, dev snapshot of 2026-07-22. The remaining tightening is marked not started.
[^early-pipeline]: IPL-MVP-ExtractionAndLabeling README, mapping workflow and reported experiment, main snapshot of 2025-10-20.
[^early-prompt]: Earlier pipeline configuration, extraction prompt and similarity threshold, main snapshot of 2025-10-20.
[^siim-rendering]: [OIDM SIIM Update](https://www.openimagingdata.org/siim-update/), Hackathon Project, 2023-06-26.
[^template-demo]: CDE Template Demo, obsToMustache renderer, master snapshot of 2023-06-15.
[^siim-search]: [OIDM SIIM 2024 Update](https://www.openimagingdata.org/siim-2024-update-hackathon-edition/), demonstrated search front end and ranked results, 2024-07-02.
[^rsna-team-demo]: [OIDM 2024 New Year Update](https://www.openimagingdata.org/2024-new-year-update/), OIDM Assisted Reporting Framework Enhancements and AI in Practice Demos, 2024-01-12.
[^nodule-workflow]: Pulm Nodule Demo Project board, schema and workflow portions only. Named individuals and collaboration history are omitted.
