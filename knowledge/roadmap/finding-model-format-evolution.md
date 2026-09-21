---
type: Roadmap
title: Finding model format evolution
description: "The stated goals for where the Open Imaging Finding Model record format is going: the canonical structured-metadata rewrite, the source schema version 2 draft, relationship and graph ideas from the next-generation CDE work, versioning, and the discrepancies a revision would have to settle."
tags: [roadmap, finding-models, schema, metadata, relationships, versioning]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T19:00:00Z }
stale_after: 2027-09-21
sources:
  - id: rewrite
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/canonical-structured-metadata-and-enrichment-rewrite.md
    title: Canonical Structured Metadata and Enrichment Rewrite, findingmodel feature/metadata-cleanup branch
  - id: impl-plan
    resource: https://github.com/openimagingdata/findingmodel/blob/504a42aad771926f5fb91fd69fe0b637f4aef211/tasks/canonical-structured-metadata-implementation-plan.md
    title: Canonical structured metadata implementation plan, findingmodel dev branch
  - id: tempo
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/plans/holistic-etiology-tempo-prompt-improvement-2026-06-03.md
    title: Holistic etiology and tempo prompt improvement, findingmodel feature/metadata-cleanup branch
  - id: v2-draft
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/oifm-schema-v2-draft.md
    title: FindingModel Source Schema v2 Draft, dated 2026-04-20, ACR-RSNA-CDEs next-gen-2026 branch
  - id: doc07
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/07-relationship-family.md
    title: The finding and diagnosis relationship family, ACR-RSNA-CDEs next-gen-2026 branch
  - id: plan
    resource: /plans/2026-09-20-knowledgebase-build-plan.md
    title: Knowledgebase build plan, recording the project lead's statements of 2026-09-20 and 2026-09-21
  - id: issue-29
    resource: https://github.com/openimagingdata/findingmodel/issues/29
    title: findingmodel issue 29, "Schema versioning future plan"
  - id: issue-30
    resource: https://github.com/openimagingdata/findingmodel/issues/30
    title: findingmodel issue 30, "Versioning, packaging, and publishing"
  - id: schema-versioning-task
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/tasks/schema-versioning-future.md
    title: Schema versioning future work plan, findingmodel main branch
  - id: issue-25
    resource: https://github.com/openimagingdata/findingmodel/issues/25
    title: findingmodel issue 25, "Facets implementation (8-facet classification)"
  - id: status
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/tasks/STATUS.md
    title: Task status summary, findingmodel main branch
  - id: issue-5
    resource: https://github.com/openimagingdata/findingmodel/issues/5
    title: findingmodel issue 5, "Expand to multiple versions of FindingModel"
  - id: issue-42
    resource: https://github.com/openimagingdata/findingmodel/issues/42
    title: findingmodel issue 42, add_ids_to_model silently regenerates an existing identifier on round trip
  - id: schema-chestcts
    resource: https://github.com/openimagingdata/findingmodels/blob/0472a4673fe476ec5335e6b3a1197faa70480426/schema/findingmodel_full_schema.json
    title: findingmodel_full_schema.json, findingmodels content/chestcts branch
  - id: schema-metadata
    resource: https://github.com/openimagingdata/findingmodels/blob/dcc6c4cfe9f359e5ae582f898ff3dbcf48a3be4f/schema/finding_model_schema.md
    title: Finding model schema prose mirror with metadata fields, findingmodels findingmodels-metadata branch
  - id: prose-schema
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/schema/finding_model_schema.md
    title: Finding Model Schema, prose mirror, findingmodels main branch
---

# What this document collects

The released Open Imaging Finding Model (OIFM) record format is described in [the finding model format](/semantic-foundation/finding-models/finding-model-format.md). This document collects the goals that have been stated for changing it, with the source that states each one. Nothing here is implemented on `main` of any repository, and nothing here is a proposal by this knowledgebase.

Four separate threads are in play, and they are not coordinated with each other: a metadata rewrite on a `findingmodel` branch, a source schema version 2 draft circulating in the common data element work, relationship and graph ideas coming out of the next-generation CDE vocabulary, and a versioning plan for packages and database artifacts.

# The canonical structured-metadata rewrite

The most advanced thread. The design document on `feature/metadata-cleanup` states the goal as making structured metadata "canonical `FindingModel` state rather than disposable enrichment output," supporting structured browse and related-model retrieval on top of it, and keeping review and provenance artifacts out of the canonical model JSON.[^rewrite]

It adds eight optional fields to both finding model classes: `body_regions`, `subspecialties`, `etiologies`, `entity_type`, `applicable_modalities`, `expected_time_course`, `age_profile`, and `sex_specificity`. Their permitted values are listed in [the format document](/semantic-foundation/finding-models/finding-model-format.md); the pipeline that populates them is described in [the enrichment pipeline](/semantic-foundation/finding-models/enrichment-pipeline.md).

Two constraints ride with it. Canonical `index_codes` are narrowed to exact or clinically substitutable matches, with broader, narrower, and merely related candidates diverted to a separate review artifact. And model-level entries in `index_codes` and `anatomic_locations` are rejected when `display` is empty.[^rewrite]

**Status as the branch reports it.** The execution plan on `dev` records slices 1 through 8 and 9-A complete, with slice 9-B, migrating the MCP and command-line callers plus a bulk backfill, and slice 10, backfill, fixtures, and final documentation, remaining.[^impl-plan] The branch's own readiness assessment fails: the 2026-06-03 prompt-improvement document raises expected time course to between 0.76 and 0.78 and etiologies to between 0.91 and 0.93, then states that overall readiness remains a failure because age profile and index codes are below the quality floor.[^tempo]

# The source schema version 2 draft

A separate and broader draft, dated 2026-04-20 and marked "a proposed authoring schema, not an implementation-complete contract yet," is kept in the `next-gen-2026` branch of `ACR-RSNA-CDEs` as a copy of an upstream gist.[^v2-draft] It proposes a different decomposition of the format than the metadata rewrite does, and the two have not been reconciled.

| Proposal | What the draft says |
|---|---|
| Source against hydrated models | A source `.fm.json` is authored; a hydrated model is the fully resolved form after canonical references expand. Runtime APIs and indexing operate on hydrated models |
| Canonical attribute reuse | `presence` and `change from prior` are defined once in `<OIFMA_ID>.attribute.json` files and referenced, not redefined. A reference may override the description and value descriptions, not the structure |
| Authored relationships | `related_models` holds only the assertions authored on that model, each naming a `relationship_type` from a registry. Tooling derives inverses; authors do not maintain both sides |
| Lifecycle | `status` of `active` or `deprecated`, with `deprecated_reason`, `replaced_by_oifm_id`, and `deprecated_at` |
| History sidecars | A per-model `.history.jsonl` with typed events carrying actor kind, actor identifier, source system and tool, model version, summary, target schema version, and a content hash |
| Registries | `relationship_types.json` and `quantity_kinds.json` alongside the corpus |
| `schema_version` on the record | Required, `"2.0"` for version 2 source files |

The draft also lists explicit removals and changes against the current shape: drop `required`; replace the numeric `unit` with `quantity_kind` plus optional `common_units`; add `synonyms` to attributes and choice values; add model-level `references`; add `lifecycle` and `related_models`; allow canonical attribute references; and keep hydrated output close to the current structure.[^v2-draft]

Five decisions are left open in the draft itself, including whether runtime APIs expose both the authored and the effective relationship views, where registry files live, and whether canonical attributes may be numeric or carry index codes.[^v2-draft]

# Relationships and the graph, from the CDE work

The project lead's stated goal for the format, recorded in [the knowledgebase build plan](/plans/2026-09-20-knowledgebase-build-plan.md), is increased metadata plus the relationship and graph work coming out of the common data element effort.[^plan]

That effort is described in [the next-generation vocabulary](/semantic-foundation/common-data-elements/next-generation-vocabulary.md). Three of its ideas bear directly on the finding model format.

- **Typed, identified relationships.** Eight relationship pairs plus a catch-all, each carrying its own identifier so a report-level assertion can cite the standing potential it expresses.[^doc07]
- **The differential as a derived view.** Computed by traversing manifestation edges and filtering by context, with no `DIFFERENTIAL_OF` edge type.[^doc07]
- **Properties on edges.** Typicality on the HPO and Orphanet frequency scale, and a three-value specificity, both optional and independent.[^doc07]

The relationship documents record the gap plainly: the registry exists only in the version 2 draft, and the live `findingmodels` repository implements no relationship mechanism at all.[^doc07]

# Versioning

Two open issues cover versioning, and both are about packages and database artifacts rather than about the record format.

**Issue 30, versioning, packaging, and publishing**, asks for a semantic versioning policy across the monorepo packages, a build and publish pipeline covering tags, changelog, and release notes, and maintainer documentation.[^issue-30]

**Issue 29, schema versioning future plan**, depends on issue 30 and covers the DuckDB artifacts: add a `_metadata` table carrying schema version, content version, build time, and record count; upgrade the manifest format to version 2 with an entries array per package; add a `REQUIRED_SCHEMA` constant per package with selection logic; and update the publish flow to write the correct manifest entry.[^issue-29] The task plan behind it states the governing rule: "A package version requires exactly ONE schema version," with backward compatibility coming from the manifest keeping old schema databases available. It is marked deferred until after an initial release.[^schema-versioning-task]

Record-format versioning appears only in the version 2 draft's `schema_version` field, and in the dual-database release plan described in [the enrichment pipeline](/semantic-foundation/finding-models/enrichment-pipeline.md), which avoids a breaking migration by publishing a legacy-compatible artifact alongside a metadata-aware one.

# Superseded, and still open as an issue

The original eight-facet classification specification is superseded. Two task documents on `main` carry it, the task status summary marks it "Blocked - needs 4 design decisions" covering scope, required against optional, markdown representation, and search indexing,[^status] and the canonical metadata implementation plan states that it supersedes the facets plan for this workstream.[^impl-plan] Issue 25 remains open against the old design.[^issue-25]

Four other open `findingmodel` issues shape the format rather than the tooling. Issue 5 asks for three model variants: a content-only form for language model extraction, a draft form carrying everything but identifiers and contributors, and the full saveable form.[^issue-5] Issue 3 asks for a human-editable markdown form without identifiers or codes, issue 4 for a tool that folds edits to that markdown back into the JSON while preserving identifiers, and issue 8 for a `FindingObservation` concept holding worked examples of a finding model in use.

# Identifier lifecycle, which no thread covers

Identifier stability is enforced today only against duplicates. Nothing in any repository documents deprecation, retirement, supersession, or versioning of a published OIFM or OIFMA identifier, and the released format carries no version field. The version 2 draft's `lifecycle` object is the only stated mechanism for retiring a model, and it is a draft.

Meanwhile the opposite problem is open as a defect. Issue 42, filed 2026-04-18, records that loading a registered definition through the base class silently discards its identifiers, after which the identifier-adding helper mints fresh ones, which the issue calls "a silent data-integrity hazard" for any workflow that mutates an existing file. Four candidate fixes are proposed in the issue and none has been chosen.[^issue-42]

# Three uncoordinated schema extensions on content branches

The `findingmodels` content repository carries the schema files that mirror the format, and three unmerged branches extend them independently. The metadata branch adds 347 lines to `finding_model.schema.json` and a new section to the prose mirror.[^schema-metadata] The CT chest branch and its ancestor add 200 lines to the same file plus a new 522-line `findingmodel_full_schema.json`.[^schema-chestcts] The older CDE-to-finding branch adds a different 200 lines. None has landed on `main`, and no document reconciles them.

# Discrepancies a revision would have to settle

Two are recorded in the format documentation and are carried in [open questions](/roadmap/open-questions.md) rather than resolved here.

- **Choice value code indexing.** The prose mirror on `main` numbers the first choice value `.1`; the validator in the released code writes `.0`, and the stored corpus follows the code.[^prose-schema]
- **Omissions in the prose mirror.** It omits `anatomic_locations` from the full model entirely, and states none of the length and cardinality constraints the code enforces.[^prose-schema]

The content-side direction, which is separate from the format, is in [the content direction roadmap](/roadmap/finding-model-content-direction.md).

[^rewrite]: Canonical Structured Metadata and Enrichment Rewrite, feature/metadata-cleanup branch
[^impl-plan]: Canonical structured metadata implementation plan, findingmodel dev branch
[^tempo]: Holistic etiology and tempo prompt improvement, 2026-06-03
[^v2-draft]: FindingModel Source Schema v2 Draft, 2026-04-20
[^doc07]: The finding and diagnosis relationship family, next-gen-2026 branch
[^plan]: Knowledgebase build plan
[^issue-29]: findingmodel issue 29, "Schema versioning future plan"
[^issue-30]: findingmodel issue 30, "Versioning, packaging, and publishing"
[^schema-versioning-task]: Schema versioning future work plan, findingmodel main branch
[^issue-25]: findingmodel issue 25, "Facets implementation"
[^status]: Task status summary, findingmodel main branch
[^issue-5]: findingmodel issue 5, "Expand to multiple versions of FindingModel"
[^issue-42]: findingmodel issue 42, identifiers regenerated on round trip
[^schema-chestcts]: findingmodel_full_schema.json, findingmodels content/chestcts branch
[^schema-metadata]: Finding model schema prose mirror with metadata fields, findingmodels-metadata branch
[^prose-schema]: Finding Model Schema, prose mirror, findingmodels main branch
