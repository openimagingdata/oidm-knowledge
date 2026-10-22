---
type: Concept
title: Metadata enrichment pipeline
description: How finding model definitions get structured metadata assigned by language models, what shipped, what the canonical rewrite on the work edge changes, and why it has not been released.
tags: [semantic-foundation, finding-models, enrichment, metadata, concept]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: prd
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/docs/finding-enrichment-prd.md
    title: Finding Enrichment System product requirements document, findingmodel main branch
  - id: impl-plan
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/docs/finding-enrichment-implementation-plan.md
    title: Finding enrichment implementation plan, findingmodel main branch
  - id: optimization
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/docs/enrichment-pipeline-optimization-proposal.md
    title: Finding enrichment pipeline optimization proposal, findingmodel main branch
  - id: rewrite
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/canonical-structured-metadata-and-enrichment-rewrite.md
    title: Canonical Structured Metadata and Enrichment Rewrite, findingmodel feature/metadata-cleanup branch
  - id: adr2
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/adr/0002-split-agent-assignment-architecture.md
    title: ADR 0002, split-agent assignment architecture, findingmodel feature/metadata-cleanup branch
  - id: adr3
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/adr/0003-dual-db-pre-post-metadata-release.md
    title: ADR 0003, dual-database pre and post metadata release, findingmodel feature/metadata-cleanup branch
  - id: agent-arch
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/metadata/enrichment/enrichment-agent-architecture.md
    title: Enrichment agent architecture, findingmodel feature/metadata-cleanup branch
  - id: current-plan
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/plans/metadata-enrichment-current-plan.md
    title: Metadata enrichment cleanup plan, findingmodel feature/metadata-cleanup branch
  - id: tempo
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/plans/holistic-etiology-tempo-prompt-improvement-2026-06-03.md
    title: Holistic etiology and tempo prompt improvement, findingmodel feature/metadata-cleanup branch
  - id: index-codes
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/plans/index-code-target-fixture-integration-2026-06-23.md
    title: Index code target fixture integration, findingmodel feature/metadata-cleanup branch
  - id: data-history
    resource: https://github.com/openimagingdata/findingmodels/blob/dcc6c4cfe9f359e5ae582f898ff3dbcf48a3be4f/docs/plans/metadata-enrichment-plan-history-2026-05-24.md
    title: Metadata enrichment plan history, findingmodels findingmodels-metadata branch
  - id: regression-floor
    resource: https://github.com/openimagingdata/findingmodels/blob/dcc6c4cfe9f359e5ae582f898ff3dbcf48a3be4f/evals/regression_floor/README.md
    title: Metadata regression floor eval set, findingmodels findingmodels-metadata branch
---

# The problem

Authors supply [finding model](/glossary/finding-model.md) names, descriptions, synonyms, and [attributes](/glossary/attribute.md). Ontology codes, locations, body regions, subspecialties, modalities, and finding-versus-diagnosis classification are often missing. A language-model pipeline proposes these metadata across the 2,382-definition corpus.

Two generations of that pipeline exist. The first shipped and is on `main`. The second is a rewrite on the work edge that has not been released.

# What shipped

The enrichment system on `main` accepts a finding name or an OIFM identifier, looks it up in the index, and returns a structured result carrying SNOMED CT and RadLex codes, body regions, etiologies, modalities, subspecialties, and anatomic locations.[^prd] Its stated goals were to automate enrichment, reuse the existing ontology and anatomic search tools, produce human-reviewable output, and "enable future integration into FindingModel schema and database workflows." Explicit non-goals for the first version were direct database updates, schema modification, batch processing, and command-line integration.

The requirements document records phases 1 through 8 complete as of 2025-11-25, covering the data models, index lookup, ontology search, a structured-output agent, orchestration, a script interface, 57 unit tests, and 8 integration tests. Phase 9, manual validation and iteration, is marked not started.[^prd]

Its architecture was five language-model calls taking roughly 25 to 30 seconds per finding: an index lookup, then parallel ontology and anatomic searches each consisting of query generation, a database search, and a categorization or selection step, then one final classification agent.[^optimization] An optimization proposal on the same branch analyzed that pipeline and recommended collapsing it into a single unified classifier fed by raw search results, restructuring the prompts with explicit tags and worked examples, and adding domain-specific guidance. It records the observed quality problems plainly: overuse of a catch-all body region value, inconsistent subspecialty assignment, and over-selection of etiologies.

The decisive limitation was structural rather than about quality. Enrichment produced a sidecar result object. The metadata never became part of the finding model, so it could not be stored, searched, or browsed.

# The canonical rewrite

The design document on `feature/metadata-cleanup` states the case for starting over: the repository had two older enrichment pathways, one program-orchestrated and one agentic, and "neither older pathway is acceptable as the canonical future implementation because both produce sidecar enrichment output instead of making structured metadata part of `FindingModel`." The new direction is to build one metadata-assignment tool from scratch, salvage only the useful search and prompt pieces, and remove both older pathways with no compatibility shims.[^rewrite]

The goal is stated as making structured metadata "canonical `FindingModel` state rather than disposable enrichment output," supporting structured browse and related-model retrieval on top of it, and keeping review and provenance artifacts separate from the canonical model JSON. The eight fields this adds to the format, and their permitted values, are listed in [the format document](/semantic-foundation/finding-models/finding-model-format.md).

## Seven agents, not one

Where the optimization proposal recommended one unified classifier, the rewrite went the other way. The rewrite uses seven agents with external prompts and typed outputs: entity type, etiology and tempo, patient applicability, subspecialty domain, modality applicability, ontology decision, and anatomy decision. ADR 0002 states that "focused agents allow concise/clean prompts, per-field evaluation, and targeted tuning of weak fields," at the cost of more calls.[^adr2]

`assign_metadata()` assembles decisions but "never decides a field value itself."[^agent-arch] It gathers ontology and anatomy candidates with a configurable limit defaulting to 15, then asks ontology and anatomy agents to select from them. Entity type, patient applicability, subspecialty, and modality run in parallel. Etiology and tempo run last, depending on and validated against entity type. Two search-agent pairs supply candidates without setting metadata. An auditor provides advice only.

Each agent has a component evaluation for tuning its fields.

## Releasing without breaking anyone

A third decision record covers distribution. Two DuckDB artifacts are published from the same enriched source commit: a legacy-compatible one readable by the currently published runtime, and a metadata-aware one carrying the structured-metadata columns, the enriched JSON, and a provenance table. The reason given is that "existing consumers keep working unchanged while metadata-aware consumers get the new data, rather than forcing a breaking single-DB migration." An optional flip of the default manifest key controls when the metadata-aware database becomes the default.[^adr3]

# Why it has not shipped

The 2026-06-03 prompt-improvement document reports expected time course scores rising from 0.69 to between 0.76 and 0.78 and etiology from 0.74 to between 0.91 and 0.93. Scoring weighted errors asymmetrically by clinical consequence. Age profile and index codes still failed the quality floor, so overall readiness failed.[^tempo]

Index codes scored about 0.674 against a 0.85 floor, the weakest field, and the cause was missing RadElement coverage in the ontology search. Adding it raised the score to about 0.736, still insufficient. Subsequent work separates searchable source codes from carried-forward codes.[^index-codes]

The active plan on the branch is therefore not a corpus run. Its stated goal is to get the branch and the sibling data repository "to a coherent, reviewable, git-clean state so we can move toward supervised corpus enrichment," and it says so explicitly: "The immediate milestone is not a broad corpus run."[^current-plan] Five ordered commits cover documentation consolidation, review-evidence fixtures and gate validation tests, tool and prompt refactoring, data-repository apply tooling, and the approved baseline. The plan also records "No commits are made without explicit permission."

Review evidence covers 150 unique records and 180 events. Current effective statuses are 67 approved and 83 requiring feedback. A follow-up pass updated 21 records, increasing approvals from 46 to 67.

# The data side

The content repository has its own branch for this work, `findingmodels-metadata`, which applies an approved enrichment baseline to 78 existing definitions and adds no new ones. Its approach is evidence-gated rather than output-gated. The branch's consolidated plan history states the operating rules: "Human review is authoritative," generated definition, markdown, and index changes are treated "as untrusted until approved evidence is safely captured," generated source diffs "are not gold," and approved source changes are reapplied "only through an explicit approved-output application path."[^data-history]

The same branch carries a regression floor: a seeded set of reviewed metadata expectations, created 2026-05-05, that every targeted rerun is meant to clear, covering time course, anatomy, measurement scope, device dwell and placement, broad whole-body findings, ontology exactness, pediatric age handling, sex-specific anatomy, and age-neutral cases. Its own README notes that no reviewed PET or molecular imaging case was available, so it is not yet a complete floor for that behavior.[^regression-floor]

Neither branch has merged, and no pull request proposes merging either. The direction as a stated goal is recorded in [format evolution](/roadmap/finding-model-format-evolution.md).

[^prd]: Finding Enrichment System product requirements document, findingmodel main branch
[^impl-plan]: Finding enrichment implementation plan, findingmodel main branch
[^optimization]: Finding enrichment pipeline optimization proposal, findingmodel main branch
[^rewrite]: Canonical Structured Metadata and Enrichment Rewrite, feature/metadata-cleanup branch
[^adr2]: ADR 0002, split-agent assignment architecture
[^adr3]: ADR 0003, dual-database pre and post metadata release
[^agent-arch]: Enrichment agent architecture, feature/metadata-cleanup branch
[^current-plan]: Metadata enrichment cleanup plan, feature/metadata-cleanup branch
[^tempo]: Holistic etiology and tempo prompt improvement, 2026-06-03
[^index-codes]: Index code target fixture integration, 2026-06-23
[^data-history]: Metadata enrichment plan history, findingmodels-metadata branch
[^regression-floor]: Metadata regression floor eval set, findingmodels-metadata branch
