---
type: Reference
title: Repository map
description: Every source repository behind OIDM, with its organization, role, status, branch of record, last activity, deployed URL, and the documents in this bundle that cover it.
tags: [repositories, index, meta]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T02:00:00Z }
stale_after: 2027-09-21
sources:
  - id: oidm-org
    resource: https://github.com/openimagingdata
    title: openimagingdata GitHub organization, 21 repositories, read 2026-09-21
  - id: radlex-issue-3
    resource: https://github.com/RSNA/RadLex/issues/3
    title: RSNA/RadLex issue 3, "Add Anatomic Locations", opened 2026-08-10
  - id: build-plan
    resource: /plans/2026-09-20-knowledgebase-build-plan.md
    title: Knowledgebase build plan, source map and work edge sections
  - id: taxonomy-branch
    resource: https://github.com/openimagingdata/findingmodels/blob/a30c3c95fa3943e7340ce87575f4b1b926987eb8/lists/README.md
    title: findingmodels lists/README.md on taxonomy-export-2026-08-15
  - id: ipl-issue-1
    resource: https://github.com/openimagingdata/imaging-problem-list/issues/1
    title: imaging-problem-list issue 1, "Create System of Data Models"
---

# How to read this map

Twenty-six repositories carry the Open Imaging Data Model (OIDM). Twenty-one belong to the `openimagingdata` GitHub organization, three anatomic-location repositories belong to the project lead's personal account, and two belong to RSNA as allied external projects.

Four status values are used.

| Status | Meaning |
|---|---|
| active | Commits in 2026 and work in flight |
| maintenance | Still the current artifact for its purpose, but no recent commits |
| lineage | Superseded by later work; kept for history |
| dead | Never completed and superseded by nothing |

"Branch of record" names the branch that represents current state for readers of this bundle. Where a repository's released state and its work edge differ, both are named. "Last activity" is the repository-wide push date reported by GitHub on 2026-09-21, which can be later than the tip commit on the branch of record when the most recent push landed on another branch.

# The repositories

| Repository | Organization | Role in OIDM | Status | Branch of record | Last activity | Deployed URL | Covered by |
|---|---|---|---|---|---|---|---|
| [findingmodel](https://github.com/openimagingdata/findingmodel) | openimagingdata | Python library, CLIs, MCP server, and the `anatomic-locations` package for the Open Imaging Finding Model (OIFM) format | active | `main` released state; `dev` and `feature/metadata-cleanup` for the work edge | 2026-06-29 | none | [/semantic-foundation/finding-models/finding-model-format.md](/semantic-foundation/finding-models/finding-model-format.md), [/semantic-foundation/finding-models/enrichment-pipeline.md](/semantic-foundation/finding-models/enrichment-pipeline.md), [/semantic-foundation/anatomic-locations/data-model.md](/semantic-foundation/anatomic-locations/data-model.md), [/semantic-foundation/anatomic-locations/tooling.md](/semantic-foundation/anatomic-locations/tooling.md) |
| [findingmodels](https://github.com/openimagingdata/findingmodels) | openimagingdata | Content repository: 2,382 finding model definitions, the `ids.json` registry, the MGB exam-oriented sub-taxonomies | active | `main` for the corpus; `taxonomy-export-2026-08-15` for content direction | 2026-08-15 | none | [/semantic-foundation/finding-models/content-catalog.md](/semantic-foundation/finding-models/content-catalog.md), [/semantic-foundation/finding-models/finding-taxonomies.md](/semantic-foundation/finding-models/finding-taxonomies.md), [/roadmap/finding-model-content-direction.md](/roadmap/finding-model-content-direction.md) |
| [med-ontology-lookup](https://github.com/openimagingdata/med-ontology-lookup) | openimagingdata | `molu` library and CLI for terminology lookup across RadLex, SNOMED CT, FMA, LOINC, and UMLS | active | `main` | 2026-09-20 | none | [/semantic-foundation/terminologies/med-ontology-lookup.md](/semantic-foundation/terminologies/med-ontology-lookup.md), [/semantic-foundation/exam-types/existing-building-blocks.md](/semantic-foundation/exam-types/existing-building-blocks.md) |
| [imaging-problem-list](https://github.com/openimagingdata/imaging-problem-list) | openimagingdata | Exam Finding List and Imaging Problem List specification, sample data, viewers; on `dev`, a full extraction, coding, persistence, and review platform | active | `dev` for current state; `main` for the stable specification | 2026-07-22 | [imaging-problem-list.pages.dev](https://imaging-problem-list.pages.dev) | [/data-structures/exam-finding-list.md](/data-structures/exam-finding-list.md), [/data-structures/imaging-problem-list.md](/data-structures/imaging-problem-list.md), [/applications/imaging-problem-list-viewer.md](/applications/imaging-problem-list-viewer.md), [/applications/report-extraction-platform.md](/applications/report-extraction-platform.md) |
| [FindingModelForge](https://github.com/openimagingdata/FindingModelForge) | openimagingdata | Web application for authoring finding models, with GitHub sign-in, a creation wizard, drafts, and review | active | `dev`, which is ahead of a stale `main` | 2026-01-02 | [fmf.oidm.org](https://fmf.oidm.org) | [/applications/finding-model-forge.md](/applications/finding-model-forge.md) |
| [CDEStaging](https://github.com/openimagingdata/CDEStaging) | openimagingdata | 259 informally authored common data element definitions upstream of RadElement | maintenance | `main` | 2025-11-25 | none | [/semantic-foundation/common-data-elements/cde-staging.md](/semantic-foundation/common-data-elements/cde-staging.md) |
| [finding-models-site](https://github.com/openimagingdata/finding-models-site) | openimagingdata | Static Astro catalog reader that renders the `findingmodels` corpus | maintenance | `main` | 2025-06-20 | [openimagingdata.github.io/finding-models-site](https://openimagingdata.github.io/finding-models-site/) | [/applications/finding-models-site.md](/applications/finding-models-site.md) |
| [IPL-MVP-ExtractionAndLabeling](https://github.com/openimagingdata/IPL-MVP-ExtractionAndLabeling) | openimagingdata | Four-stage pipeline extracting findings from reports and mapping them to finding models by embedding similarity | lineage | `main`; three single-commit experiment branches | 2025-10-31 | none | [/applications/ipl-mvp-extraction.md](/applications/ipl-mvp-extraction.md), [/history/extraction-approaches.md](/history/extraction-approaches.md) |
| [common_data_elements](https://github.com/openimagingdata/common_data_elements) | openimagingdata | Periodic snapshot of RadElement CDE definitions plus CDE schema versions 1.0 and 1.1 | maintenance | `main` | 2025-06-04 | none | [/semantic-foundation/common-data-elements/cdes-and-radelement.md](/semantic-foundation/common-data-elements/cdes-and-radelement.md) |
| [template_extraction](https://github.com/openimagingdata/template_extraction) | openimagingdata | Corpus of 281 RadReport templates and a script for extracting finding definitions from them | lineage | `main` | 2025-07-03 | none | [/history/extraction-approaches.md](/history/extraction-approaches.md) |
| [ReportFindingRefiner](https://github.com/openimagingdata/ReportFindingRefiner) | openimagingdata | Local-LLM retrieval pipeline over real report text that generates finding model outlines | lineage | `main` | 2025-05-23 | none | [/history/extraction-approaches.md](/history/extraction-approaches.md) |
| [get_ontology_findings](https://github.com/openimagingdata/get_ontology_findings) | openimagingdata | Matching RadLex entries to imaging findings so they can become finding models or CDEs | lineage | `main` | 2025-06-05 | none | [/history/extraction-approaches.md](/history/extraction-approaches.md) |
| [ontology_tools](https://github.com/openimagingdata/ontology_tools) | openimagingdata | Intended multi-ontology search library; never built beyond a README naming three ontologies | dead | `main` | 2025-03-26 | none | [/history/lineage-repositories.md](/history/lineage-repositories.md) |
| [OpenImagingDataModel.py](https://github.com/openimagingdata/OpenImagingDataModel.py) | openimagingdata | Python reference implementation of the FHIR-based Observation, CDE Set, and FindingModel classes | lineage | `main` | 2025-04-11 | none | [/history/lineage-repositories.md](/history/lineage-repositories.md), [/data-structures/fhir-mapping.md](/data-structures/fhir-mapping.md) |
| [OpenImagingDataModel.ts](https://github.com/openimagingdata/OpenImagingDataModel.ts) | openimagingdata | TypeScript reference implementation with Zod schemas for the same classes | lineage | `main` | 2024-11-13 | none | [/history/lineage-repositories.md](/history/lineage-repositories.md) |
| [FHIRSamples](https://github.com/openimagingdata/FHIRSamples) | openimagingdata | Hand-built FHIR JSON for a lung cancer screening scenario: a DiagnosticReport and three chained Observations | lineage | `main` | 2024-03-13 | none | [/history/lineage-repositories.md](/history/lineage-repositories.md), [/data-structures/fhir-mapping.md](/data-structures/fhir-mapping.md) |
| [SARTemplatesToCDEs](https://github.com/openimagingdata/SARTemplatesToCDEs) | openimagingdata | Proof of concept converting Society of Abdominal Radiology reporting templates into CDE sets | lineage | `main` | 2024-03-11 | none | [/history/extraction-approaches.md](/history/extraction-approaches.md) |
| [UseCases](https://github.com/openimagingdata/UseCases) | openimagingdata | Catalog of roughly 25 use case ideas and the six value categories used to tag them | lineage | `main` | 2024-02-26 | none | [/history/use-cases.md](/history/use-cases.md) |
| [openimagingdata.org](https://github.com/openimagingdata/openimagingdata.org) | openimagingdata | Original site scaffold, the CDE Set JSON schema, sample fixtures, and a schema-versus-API gap analysis | lineage | `main` | 2023-06-27 | superseded by [openimagingdata.org](https://www.openimagingdata.org) | [/history/lineage-repositories.md](/history/lineage-repositories.md) |
| [CDETemplateDemo](https://github.com/openimagingdata/CDETemplateDemo) | openimagingdata | Demo rendering a CDE-labeled Observation into report prose through a Mustache template | lineage | `master` | 2023-06-15 | none | [/history/cde-template-rendering.md](/history/cde-template-rendering.md) |
| [dev-secrets](https://github.com/openimagingdata/dev-secrets) | openimagingdata | Encrypted shared development secrets; infrastructure, no OIDM content | maintenance | `main` | 2025-06-02 | none | this map only |
| [anatomiclocations.org](https://github.com/talkasab/anatomiclocations.org) | talkasab, the project lead's personal account | Original curated anatomic location set of 2,890 nodes, its JSON schema, and the Jekyll site | maintenance | `main` | 2024-11-26 | [anatomiclocations.org](https://www.anatomiclocations.org) | [/semantic-foundation/anatomic-locations/lineage-and-current-implementation.md](/semantic-foundation/anatomic-locations/lineage-and-current-implementation.md), [/semantic-foundation/anatomic-locations/why-anatomic-locations.md](/semantic-foundation/anatomic-locations/why-anatomic-locations.md) |
| [BodyPartIndex.py](https://github.com/talkasab/BodyPartIndex.py) | talkasab | Python wrapper over the curated anatomic location set | maintenance | `main` | 2024-02-10 | none | [/semantic-foundation/anatomic-locations/tooling.md](/semantic-foundation/anatomic-locations/tooling.md) |
| [BodyPartIndex.ts](https://github.com/talkasab/BodyPartIndex.ts) | talkasab | TypeScript wrapper over the same set, published to npm | maintenance | `main` | 2023-09-17 | none | [/semantic-foundation/anatomic-locations/tooling.md](/semantic-foundation/anatomic-locations/tooling.md) |
| [ACR-RSNA-CDEs](https://github.com/RSNA/ACR-RSNA-CDEs) | RSNA | Allied external project: the CDE JSON schema, and on `next-gen-2026` the next-generation vocabulary work | active | `next-gen-2026` for the vocabulary work; `master` is the project default | 2026-09-15 | [radelement.org](https://radelement.org) | [/semantic-foundation/common-data-elements/next-generation-vocabulary.md](/semantic-foundation/common-data-elements/next-generation-vocabulary.md), [/references/oifm-overview-extract.md](/references/oifm-overview-extract.md) |
| [RadLex](https://github.com/RSNA/RadLex) | RSNA | Allied external project: the RadLex ontology file and a concept search and curation pipeline | active | `main` | 2026-09-02 | [radlex.org](https://radlex.org) | [/semantic-foundation/anatomic-locations/radlex-integration.md](/semantic-foundation/anatomic-locations/radlex-integration.md), [/semantic-foundation/terminologies/ontologies-used.md](/semantic-foundation/terminologies/ontologies-used.md) |

# How the repositories relate

Content repositories hold definitions and data. Library repositories turn those definitions into typed objects and searchable indexes. Application repositories consume both. Two external terminologies, RadElement and RadLex, sit outside the project and are referenced by code, not vendored into it.

```mermaid
flowchart TD
  subgraph external[External terminologies]
    RE[RadElement<br/>RDES and RDE codes]
    RL[RadLex<br/>RID codes]
    SN[SNOMED CT, FMA,<br/>LOINC, UMLS]
  end

  subgraph content[Content repositories]
    CDS[CDEStaging<br/>259 draft CDE definitions]
    CDE[common_data_elements<br/>RadElement snapshot]
    FMS[findingmodels<br/>2,382 finding models]
    AL[anatomiclocations.org<br/>2,890 anatomic locations]
  end

  subgraph libs[Libraries]
    FM[findingmodel<br/>OIFM format, index, CLIs, MCP]
    ALP[anatomic-locations package<br/>inside findingmodel]
    MOLU[med-ontology-lookup<br/>molu]
    BPI[BodyPartIndex.py and .ts]
  end

  subgraph apps[Applications]
    FMF[FindingModelForge<br/>fmf.oidm.org]
    FSITE[finding-models-site]
    IPL[imaging-problem-list<br/>extraction, coding, viewers]
    MVP[IPL-MVP-ExtractionAndLabeling]
  end

  CDS --> RE
  CDE --> RE
  FMS --> FM
  AL --> BPI
  AL --> ALP
  RL --> ALP
  RL --> MOLU
  SN --> MOLU
  RE --> FMS
  MOLU --> FM
  ALP --> FM
  FM --> FMF
  FMS --> FSITE
  FM --> IPL
  ALP --> IPL
  FMS --> IPL
  FMS --> MVP
  CDS --> FMS
```

Three edges deserve a note. The `findingmodels` corpus is pulled into `finding-models-site` as a git submodule and resolved by `imaging-problem-list` through the published `ids.json` file, so the content repository is the single source of finding model identity. The newer anatomic data lives inside `findingmodel` as the `anatomic-locations` package rather than in the original `anatomiclocations.org` repository, and the two lineages are not synchronized. RSNA/RadLex issue 3, "Add Anatomic Locations", opened 2026-08-10, tracks folding the curated anatomic location set into RadLex itself with an exit criterion of full coverage; that is a GitHub tracking issue, not a code dependency.

# Work edge

Branch inventories taken on 2026-09-21 established what follows. None of the unmerged branches named here has an open pull request.

**findingmodel.** The live thread is the canonical structured-metadata rewrite, on `feature/metadata-cleanup` (tip `1942b06`, 2026-06-29) and its base `dev` (tip `504a42a`, 2026-04-11). It adds eight optional fields to the finding model base class, splits metadata assignment across seven typed agents, and plans a dual-database release so existing consumers do not break. The branch's own readiness assessment still reports a failure: two fields remain below the quality floor. The earlier eight-facet specification on `main` is superseded by this field set. Twenty-four open issues map one to one onto task plans in the repository.

**findingmodels.** Six branches carry unmerged work. `taxonomy-export-2026-08-15` (tip `a30c3c9`) replaces the legacy `lists/` directory with the six MGB exam-oriented sub-taxonomies as CSVs totaling 3,789 rows, of which 1,028 already match an existing finding model identifier by exact name; the remaining rows are named as the next triage task. Two content pipelines add large batches that have never merged: a CT chest conversion branch with 1,822 new definitions and a three-agent merge, create, and review pipeline of which one of twenty-one chunks is complete, and a head CT branch with 419 new definitions plus an overlapping review branch with 76 more. A metadata branch applies an approved enrichment baseline to 78 existing definitions and adds no new ones. A clinician-request branch adds 59 definitions for an intracranial problem list application. The finding model JSON schema is being extended on three of these branches independently, and none of those changes has landed on `main`.

**imaging-problem-list.** `dev` (tip `36fa30c`, 2026-07-22) is 258 commits ahead of `main` (tip `06f64a7`, 2025-11-18) and is current state. Anatomic-location coding of findings has landed, and the Imaging Problem List grouping key changed from finding code alone to finding code plus location. Eight active plans center on human-review tooling, an evaluation redesign that scores quote-first matching rather than raw finding yield, an anatomy-aware viewer, and a reassessment of local model choice. The only open issue, number 1, asks for a formal Pydantic model layer for Observation, Exam Finding List, and Imaging Problem List with JSON Schema export; it is broader than any current plan and unclaimed. The one open pull request is empty after its design document was moved to a separate repository.

**med-ontology-lookup.** No branch is ahead of `main`. A twelve-issue backlog follows the six-phase design in the repository's review and proposal document; nine of those issues are open and unstarted. Offline continuous integration is implemented but sits uncommitted in a working tree, pending authorization to publish.

**CDEStaging.** All current work lands directly on `main`; the most recent commit is 2025-11-25. Fourteen topic branches exist and eleven are unmerged, the largest being a 2024 report-representation branch of 37 commits and a content branch of 33 commits. No branch has a commit after 2025-03-22, and no pull request proposes merging any of them.

**IPL-MVP-ExtractionAndLabeling.** Three single-commit experiment branches pushed within one week of each other in October 2025, none merged: a longitudinal multiple sclerosis sample dataset, a port of the extraction step to a typed agent, and a design note proposing persistent FHIR Observations with stable identifiers so repeat mentions of a finding across reports link to one entity. That design note carries no file extension and adds no code.

**FindingModelForge.** Both `dev` (96 commits ahead of `main`, 2026-01-02) and `feature/model-editing` (60 commits ahead, 2025-11-28) are unmerged. The editing branch implements AI-assisted iteration of published models rather than manual editing; its first sprint is complete and two later sprints are not started. A peer-review workflow with public drafts and comments is finished on `dev` and absent from `main`.
