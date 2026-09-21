---
type: Roadmap
title: Roadmap 2026
description: The project-level direction stated in the January 2026 status deck, the working group and use-case pipeline it proposes, and a per-repository summary of what is currently in flight.
tags: [roadmap, deck, working-group, acr, work-edge]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T19:00:00Z }
stale_after: 2027-09-21
sources:
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: "Open Imaging Data Model 2026 Status Update: Realizing Object-Oriented Imaging Results, January 2026"
  - id: plan
    resource: /plans/2026-09-20-knowledgebase-build-plan.md
    title: Knowledgebase build plan, recording the branch inventories of 2026-09-21 and the project lead's statements
  - id: repo-map
    resource: /repositories/repository-map.md
    title: Repository map, work edge section
  - id: fm-metadata-rewrite
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/canonical-structured-metadata-and-enrichment-rewrite.md
    title: Canonical Structured Metadata and Enrichment Rewrite, findingmodel feature/metadata-cleanup branch
  - id: lists-readme
    resource: https://github.com/openimagingdata/findingmodels/blob/a30c3c95fa3943e7340ce87575f4b1b926987eb8/lists/README.md
    title: MGB exam-oriented sub-taxonomies README, findingmodels taxonomy-export-2026-08-15 branch
  - id: ipl-issue-1
    resource: https://github.com/openimagingdata/imaging-problem-list/issues/1
    title: imaging-problem-list issue 1, "Create System of Data Models"
  - id: radlex-issue-3
    resource: https://github.com/RSNA/RadLex/issues/3
    title: RSNA/RadLex issue 3, "Add Anatomic Locations"
---

# What this document is

This is the project-level direction for the Open Imaging Data Model (OIDM), as stated by its sources. The single most complete statement is the January 2026 status deck, extracted in full at [status update, January 2026](/references/status-update-2026-01.md).[^deck] Below the deck sit the working repositories, whose direction is visible in their unmerged branches, plan documents, and open issues.

Nothing here is a proposal. Each goal is attributed to the deck, an issue, or a plan document that states it. Where a goal has no artifact behind it, that is said. Per-area goals live in the five area roadmaps linked from [the roadmap index](/roadmap/); unresolved conflicts between sources are collected in [open questions](/roadmap/open-questions.md).

# The three strategic pillars

The deck organizes the whole project under three pillars.[^deck]

1. **Semantic foundation.** [Finding models](/glossary/finding-model.md) feeding [common data elements](/glossary/cde.md), and [anatomic location](/glossary/anatomic-location.md) definitions.
2. **Data structures.** The atomic [Observation](/glossary/observation.md), then the [Exam Finding List](/glossary/exam-finding-list.md), then the [Imaging Problem List](/glossary/imaging-problem-list.md), then the [Imaging Persona](/glossary/imaging-persona.md).
3. **Applications.** An Open Imaging Reporting SDK enabling vendor-driven innovation, plus demonstration applications including an Imaging Problem List browser and early draft-generation tools.

The deck's executive summary states the foundational content as a language-model-built curated anatomic location index plus "nearly 3,000" Open Imaging Finding Models (OIFMs), and names the "workbench effect" as the mechanism: high-velocity language-model-powered content creation acting as a proving ground for formal common data elements.[^deck] The corpus count the deck gives does not match the count in the repository; see [open questions](/roadmap/open-questions.md).

# The working group proposal

The deck's call to action names an **ACR-OIDM Structured Imaging Results Working Group**, to be co-hosted with the American College of Radiology (ACR) as an expert and vendor data structure working group. Two conditions ride with it: **structure first**, with FHIR and other standards following, and **vendor-driven** adoption, the deck's example being reporting software development kits from a reporting vendor.[^deck]

The deck states four ACR priorities the work supports.[^deck]

| Priority | What the deck says it needs from OIDM |
|---|---|
| Recommendation tracking | Structured imaging results carried forward across exams |
| Artificial intelligence validation | Correlating artificial intelligence Observations against radiologist Observations |
| Quality metrics | Queryable structured results |
| *-RADS support | Representation of the assessment reporting systems |

No record of the working group being convened exists in any repository read for this knowledgebase. It is a stated intention.

# Next steps as the deck states them

Three, in the deck's own words: host and moderate an academic and vendor "big tent"; run a **use-case pipeline feeding the CDE group**; standardize the result.[^deck]

The use-case pipeline is the one of the three with existing material behind it. The lineage `UseCases` repository holds roughly 25 use case ideas organized against the RSNA value categories, described in [use cases](/history/use-cases.md). The direction the deck states is that such use cases feed the ACR and RSNA common data element group, which is the same direction as the workbench relationship described in [finding models and CDEs](/semantic-foundation/finding-models/finding-models-and-cdes.md).

# The work edge, repository by repository

Branch inventories taken on 2026-09-21 established what follows; the full detail is in [the repository map](/repositories/repository-map.md).[^repo-map] None of the unmerged branches named here has an open pull request.

| Repository | Live thread | In flight | Area roadmap |
|---|---|---|---|
| `findingmodel` | `feature/metadata-cleanup` (tip `1942b06`) on `dev` | Canonical structured-metadata rewrite: eight optional fields, seven typed assignment agents, dual-database release. Readiness assessment not passing[^fm-metadata-rewrite] | [Format evolution](/roadmap/finding-model-format-evolution.md) |
| `findingmodels` | `taxonomy-export-2026-08-15` (tip `a30c3c9`) for direction; five content branches | Six per-modality taxonomy CSVs, 3,789 rows, 1,028 matched; 2,761 rows awaiting triage[^lists-readme]; CT chest, head CT, and metadata batches unmerged | [Content direction](/roadmap/finding-model-content-direction.md) |
| `imaging-problem-list` | `dev` (tip `36fa30c`), 258 commits ahead of `main` | Eight active plans on review tooling, evaluation redesign, anatomy-aware viewer, local models. Issue 1 asks for a formal model layer and is unclaimed[^ipl-issue-1] | [IPL data model system](/roadmap/ipl-data-model-system.md) |
| `med-ontology-lookup` | `main`, no branch ahead | A twelve-issue backlog following the repository's six-phase design; eleven of the twelve are open, plus one filed outside the sequence. The only written exam-type design lives here | [Exam types](/roadmap/exam-types.md) |
| `findingmodel` anatomic-locations package, `anatomiclocations.org`, `BodyPartIndex.py` | Package inside `findingmodel`; the original repositories are quiet | Two unreconciled datasets; RSNA `RadLex` issue 3 tracks incorporation with a 100 percent coverage exit criterion[^radlex-issue-3] | [Anatomic locations and RadLex](/roadmap/anatomic-locations-and-radlex.md) |
| `FindingModelForge` | `dev` and `feature/model-editing`, both unmerged | A peer-review layer finished on `dev`; model editing answered by AI-assisted iteration on its own branch | No area roadmap; see [the Forge profile](/applications/finding-model-forge.md) |
| `CDEStaging` | `main` | All current work lands on `main`; eleven topic branches unmerged, none touched since 2025-03-22 | [Content direction](/roadmap/finding-model-content-direction.md) |
| `IPL-MVP-ExtractionAndLabeling` | `main` | Three single-commit experiments, including a persistent-FHIR-identity design note | [IPL data model system](/roadmap/ipl-data-model-system.md) |

# What the deck names that does not exist

Three items in the deck have no artifact in any repository. They are direction, not status.

- **The Open Imaging Reporting SDK.** Named as one third of the applications pillar. No repository, no code, no specification. See [the reporting SDK](/applications/reporting-sdk.md).
- **The Imaging Persona.** Named with four context categories, clinical context, medical baseline, specialized history, and surgical history. No specification. See [Imaging Persona](/data-structures/imaging-persona.md).
- **The ACR-OIDM working group.** Described above.

A fourth item, [exam types](/glossary/exam-type.md), is not in the deck at all but has been stated as a goal in three places since 2022 with no artifact produced; see [the exam types roadmap](/roadmap/exam-types.md).

The implementation status of every piece of the system, built and unbuilt, is tabulated in [architecture](/overview/architecture.md).

[^deck]: "Open Imaging Data Model 2026 Status Update: Realizing Object-Oriented Imaging Results", January 2026
[^plan]: Knowledgebase build plan
[^repo-map]: Repository map, work edge section
[^fm-metadata-rewrite]: Canonical Structured Metadata and Enrichment Rewrite, feature/metadata-cleanup branch
[^lists-readme]: MGB exam-oriented sub-taxonomies README, taxonomy-export-2026-08-15 branch
[^ipl-issue-1]: imaging-problem-list issue 1, "Create System of Data Models"
[^radlex-issue-3]: RSNA/RadLex issue 3, "Add Anatomic Locations"
