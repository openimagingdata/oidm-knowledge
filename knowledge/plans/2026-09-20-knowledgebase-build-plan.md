---
type: Plan
title: Knowledgebase build plan
description: How the oidm-knowledge repository is scaffolded, populated from the source repositories, cross-linked, validated, and published.
tags: [plan, meta]
status: draft
generated: { by: claude-fable-5-1/claude-code, at: 2026-09-20T22:30:00Z }
sources:
  - id: charter
    resource: scope:grilling-session-2026-09-20
    title: Decisions from the 2026-09-20 planning interview with the project lead
  - id: inventories
    resource: scope:seven-inventory-reports-2026-09-20
    title: Read-only inventories of all source repositories, the Gamma status deck, and the openimagingdata.org site
---

# Purpose

Build `oidm-knowledge` as the canonical, public, high-level documentation for the Open Imaging Data Model (OIDM). Non-code documentation migrates here from the working repositories; those repositories will later reference this one. The bundle follows the Open Knowledge Format (OKF) 0.2 so that people and agents can both read it.

This plan is itself part of the bundle. It is updated as phases complete and marked complete at the end.

# Decisions already made

These were settled with the project lead on 2026-09-20 and are not re-opened here.

| Area | Decision |
|---|---|
| Role of this repo | Canonical high-level documentation. Migrate, don't mirror. Working repos keep code documentation only. |
| Format | OKF 0.2 bundle in `knowledge/`. Root `index.md` carries `okf_version: "0.2"`. |
| Tooling | scaccogatto/okf-skills (installed under `.agents/skills/`) for authoring and validation, plus a port of the stricter checker from the ACR-RSNA-CDEs `next-gen-2026` branch as a second CI gate. |
| Doc types | Inherit the `next-gen-2026` vocabulary and extend it (see Conventions). |
| Trust signals | Every agent-written doc carries `generated`. `status: draft` until the project lead verifies it as `human:talkasab`, then `status: stable`. Migrated human-written docs carry `sources` pointing at their origin. |
| Site | Rendered site from day one. Not MkDocs Material. Recommendation below: Quartz 5, runner-up Astro Starlight. |
| Repo | `openimagingdata/oidm-knowledge`, public, CC-BY-4.0. Plan, `CHANGELOG.md`, `DEV_LOG.md`, `CONTRIBUTING.md`, agent authoring guide. |
| Organization | Three layers: semantic foundation, data structures, applications. Per-repo index as secondary lookup. Balanced audience: each area gets a narrative "why" and a technical "how". |
| Content stance | Facts and stated goals only. No design proposals yet. Catalogs described and linked, never copied. Organizations named, individuals not. |
| Sources | All openimagingdata repos including lineage; the openimagingdata.org site; the January 2026 status deck; the anatomic-location repos and the newer data inside `findingmodel`; RSNA/ACR-RSNA-CDEs and RSNA/RadLex as allied external projects with OIDM-relevant parts of `next-gen-2026` migrated; IPL-MVP-ExtractionAndLabeling. Excluded: ladybug, composer-prototype, MGB clinical-guidance repos. Manuscripts to follow from the project lead. |
| Process | Source repos cloned read-only into the home directory. Sonnet for inventory and extraction, Opus for synthesis, the main session for review and cross-linking. The project lead approves this plan before any synthesis or bundle writing. |

# The project lead's stated goals

Recorded verbatim from the 2026-09-20 request that started this work, so that documents citing `scope:grilling-session-2026-09-20` have a written source. Wording lightly normalized for spelling only.

- **Open Imaging Finding Models.** "Definition formats, needs overhaul for increased metadata and interesting relationship/graph work coming from CDEs." "Tooling for working with these, using them, probably needs corresponding overhaul." "Actual content efforts."
- **ACR/RSNA Common Data Elements.** "Should dovetail with the OIFM work."
- **FindingModelForge.** "An authoring tool for creating OIFMs / CDEs."
- **Imaging Problem List.** "A format for representing a patient's imaging history." "Define appropriate data structures for representing both observations in radiology reports and their relationships." "Manage them (and appropriately collate them) across the patient's imaging history." "Design interesting applications that use this tool and demonstrate how this works." "Create standard data structure formats, etc. for working with these."
- **Anatomic Locations.** "There are repos, and this will be blended in with RadLex." "Also needs tooling for people working with them."
- **Exam types.** "Needs wrapper tooling around the knowledge graph represented by RadLex LOINC playbook." "Need to define the PREFERRED high-level entries like 'CT Chest', 'MRI Brain', 'X-ray Knee'." "Need to TIGHTLY wrap up with Anatomic Locations, including edges for both 'always included' (which can include hierarchies) as well as 'usually included' (for edge things) and something like 'POSSIBLY included, would have to check'."
- **Content direction (2026-09-21).** "In findingmodels, there's a recent taxonomy branch with new files in lists that's the immediate direction for all of the content, probably replacing a lot of the Gamuts-based models." The taxonomies are to be called the "MGB exam-oriented sub-taxonomies."

# Source map

Inventory reports for every source live in the session scratchpad and are summarized here. "Read from" names the branch that represents current state.

| Source | Role | Read from | Key migration candidates |
|---|---|---|---|
| findingmodel | OIFM library, `anatomic-locations` package, CLIs, MCP server | `main` (2026-03) for released state; `dev` and `feature/metadata-cleanup` (2026-06-29) for the work edge | `docs/anatomic-locations.md`, `docs/manifest_schema.md`, `.claude/skills/manage-anatomic-locations/reference/*`, `tasks/done/anatomic-locations-normalized-schema.md`, enrichment PRD and plans, schema-versioning notes, `notebooks/data/anatomic_locations_noembed.json` (2,926 records, current anatomic data); on the work edge: `docs/canonical-structured-metadata-and-enrichment-rewrite.md`, ADRs 0001 to 0003, `tasks/canonical-structured-metadata-implementation-plan.md`, `docs/plans/metadata-enrichment-current-plan.md` |
| findingmodels | Content: 2,382 finding model definitions (1,933 Gamuts-derived, 256 OIDM, 115 CDE, 47 MGB, 31 MSFT), `ids.json`, MGB exam-oriented sub-taxonomies | `taxonomy-export-2026-08-15` (one commit ahead of `main`) for content direction; `main` for the corpus; content branches for in-flight batches | `schema/finding_model_schema.md`, `lists/README.md` and the six taxonomy CSVs (3,789 rows, 1,028 matched), `docs/plans/definition_cleanup.md`, `docs/plans/rebuild-finding-skills.md`, `docs/plans/findingmodel-upstream-proposals.md`; on branches: `content/chestcts` PLAN and batch progress, `findingmodels-metadata` plan history and schema changes, `content/headcts` |
| med-ontology-lookup | `molu` terminology lookup across RadLex, SNOMED CT, FMA, LOINC, UMLS | `main` (2026-09-20); no unmerged branches; offline-CI work uncommitted in a worktree | `docs/product-roadmap.md` (contains the only written exam-type design), `docs/project-review-and-proposal.md` (six-phase design), `docs/plans/2026-09-05-github-issue-backlog.md` |
| FindingModelForge | Authoring web app at fmf.oidm.org | `dev` (2026-01) is ahead of stale `main`; `feature/model-editing` (2025-11) | `docs/finding-model-creation-workflow.md`, `docs/DRAFT_WORKFLOW.md`, `docs/feature_finding_model_draft_saving.md`, `zOld/plans/*` (history), issue #13 model editing |
| CDEStaging | 259 informally authored CDE definitions upstream of RadElement | `main` (2025-11); all recent work lands on `main`; 11 topic branches from 2024 never merged | `docs/report_extraction_process.md`, `report_representation/{negative_statements,uncovered_findings,missing_attributes}.md`, `definitions/upmedic/roadmap.md`; the unmerged `report_representation` and `gamuts_work` branches noted in history |
| finding-models-site | Static catalog reader for findingmodels | `main` | Nothing beyond a profile entry |
| imaging-problem-list | Exam Finding List and Imaging Problem List spec, viewer, sample data; on `dev`, a full extraction, coding, persistence, and review platform | `dev` (2026-07-21, 258 commits ahead of `main`) for current state; `main` for the stable spec; the one feature branch is empty | `README.md`, `CLAUDE.md` (domain model), `docs/anatomic-location-assignment-rules.md`, `docs/technical-imaging-findings.md`, `docs/plans/anatomic-location-efl-ipl.md`, `docs/archive/finding-and-location-code-assignment-plan.md`, `initial-extraction-plan.md`, `docs/plans/viewer-v2-anatomy-dashboard.md`, `docs/plans/extractor-evals-redesign.md`, the extraction-reviewer plans, `prompts/validator_prompt_example.md`, issue #1 "Create System of Data Models", both PNG diagrams, sample data |
| IPL-MVP-ExtractionAndLabeling | Early 4-stage extraction and mapping pipeline | `main` (2025-10); three single-commit experiment branches | `README.md`; `FHIR_Example_Structure` on `Persistent_FHIR_Resources` (a design note without a `.md` extension) |
| ACR-RSNA-CDEs | Allied external project. `next-gen-2026` holds the project lead's next-generation vocabulary work | `next-gen-2026` (2026-09-15) | `CONTEXT.md` glossary terms; `notes/oifm-overview.md`, `notes/oifm-metadata-fields.md`, `notes/oifm-schema-v2-draft.md`, `notes/ihe-idr-extract.md`, `notes/hood-taxonomies-profile-2026-09-01.md`; the ideas in `docs/next-gen-schema/00, 01, 03, 07, 11` summarized as goals; `docs/check_bundle.py` conventions. Committee minutes and email extracts stay in the CDE repo. |
| RadLex (RSNA) | Allied external project: ontology (`RadLex.owl`, 46,899 RIDs) and a search pipeline repo | `main`; GitHub issue #3 "Add Anatomic Locations" | `docs/plans/hybrid-fts-search.md` (referenced, not migrated) |
| anatomiclocations.org, BodyPartIndex.py, BodyPartIndex.ts | Original curated anatomic location set (2,890 nodes) and wrapper libraries | `main` of each (2022 to 2024) | `docs/index.markdown` (rationale, exam-type roadmap line), `docs/code.markdown`, `data/body_parts_schema.json`, `BodyPartIndex.py/TODO.md` |
| OpenImagingDataModel.py and .ts | Lineage reference implementations | `main` | `observation.py` and `finding_model.py` shapes as FHIR precedent; Zod schemas as early types |
| FHIRSamples | Lineage: lung screening DiagnosticReport plus chained CDE-coded Observations | `main` | All JSON examples as FHIR mapping precedent |
| UseCases | Lineage: ~25 use case ideas and the six RSNA value categories | `main` | `Index.md`, `README.md` |
| openimagingdata.org (repo) | Lineage: old site scaffold and schema fixtures | `main` | `schemas/schema_differences.md`, sample JSON |
| openimagingdata.org (Ghost site) | 15 posts (2023-06 to 2025-03) and an About page | live | "Findings, CDEs, and Observations", "Data Model: Structure and Function", "Benchmarking a Vision", "OIDM-Based Next-gen Reporting Assistance Framework", the SIIM 2024 posts |
| CDETemplateDemo, SARTemplatesToCDEs, template_extraction, ReportFindingRefiner, get_ontology_findings, ontology_tools, common_data_elements | Lineage | `main` | `SARTemplatesToCDEs/RectalCAStaging/Changes_vs_RDES11.md`, `ReportFindingRefiner/README.md`, `common_data_elements/README.md` and schema versions; the rest as one-paragraph history entries |
| Gamma deck, January 2026 | Vision and roadmap | live | Whole deck as a Presentation Extract |

# The work edge

The project lead asked that the knowledgebase reflect the entire work edge, not only default branches. Branch-level inventories on 2026-09-21 established the following. Documents that describe current state cite the branch and pin the commit they read.

- **findingmodels.** The MGB exam-oriented sub-taxonomies on `taxonomy-export-2026-08-15` are the immediate direction for all content and are expected to replace many of the Gamuts-derived models, which make up 1,933 of the 2,382 current definitions. Rows without a matched OIFM ID are the next triage task. Three content pipelines (`content/chestcts` as the live CT-chest front, `content/headcts`, `km`) and a metadata-enrichment branch touching 78 models are in flight, none merged. The finding model schema is being extended on three uncoordinated branches with nothing landed on `main`.
- **findingmodel.** The live thread is the canonical structured-metadata rewrite on `feature/metadata-cleanup` and `dev`: eight new optional fields (body regions, subspecialties, etiologies, entity type, applicable modalities, expected time course, age profile, sex specificity), a multi-agent enrichment architecture, and a dual-database release plan. The older eight-facet specification is superseded. The branch's own readiness assessment is not yet passing. Twenty-four open issues map one-to-one onto task plans.
- **imaging-problem-list.** `dev` is current. Eight active plans center on human-review tooling, an honesty-first evaluation redesign, an anatomy-aware viewer, and local-model strategy. Anatomic-location coding of findings has landed. Issue #1, a formal Pydantic model layer for Observation, Exam Finding List, and Imaging Problem List with JSON Schema export, is broader than any current plan and unclaimed.
- **med-ontology-lookup.** No unmerged branches. A twelve-issue backlog follows the six-phase design document. Offline CI is implemented but uncommitted.
- **CDEStaging, IPL-MVP-ExtractionAndLabeling, FindingModelForge.** Work lands on `main` in CDEStaging with stale 2024 topic branches never merged. IPL-MVP has three single-commit experiments, including a longitudinal FHIR-persistence design note. Forge's `dev` and `feature/model-editing` branches are ahead of `main`.

Facts worth stating up front because they shape the writing:

- The taxonomies-over-Gamuts direction and the metadata rewrite are stated as current direction in the finding model documents and the roadmap, sourced to their branches.
- Two anatomic location lineages coexist: the 2022 `anatomiclocations.org` set with wrapper libraries, and the newer `anatomic-locations` package inside `findingmodel` with laterality and dual hierarchies. The knowledgebase documents both and states which is current.
- The FHIR mapping for Exam Finding Lists and Imaging Problem Lists is documented but implemented nowhere. The knowledgebase says so.
- No exam-type artifact exists. The area is documented as goals plus existing building blocks.
- The "Open Imaging Reporting SDK" named in the deck has no artifact. It appears only in the roadmap.
- The Hood finding taxonomies are named after their author in the source repo. The knowledgebase refers to them as "the MGB exam-oriented sub-taxonomies" and credits the contributing institution, per the organizations-only rule. The project lead may override.

# Target bundle structure

One concept per file. Directory names are stable identifiers; file names are kebab-case. Every directory has an `index.md`. Roughly 90 documents.

```
knowledge/
  index.md                      root listing, okf_version 0.2
  log.md
  overview/
    what-is-oidm.md             Overview: mission, the three layers, who it is for
    vision.md                   Concept: object-oriented imaging results, from the deck and site
    architecture.md             Concept: how the three layers and the repos fit together
    getting-involved.md         Guide
  glossary/                     one term per file, alphabetical index
    oidm.md  oifm.md  finding-model.md  attribute.md  index-code.md  cde.md  cde-set.md
    data-element.md  finding-class.md  measurement.md  anatomic-location.md  laterality.md
    contained-by-and-part-of.md  exam-type.md  observation.md  presence.md
    exam-finding-list.md  imaging-problem-list.md  imaging-persona.md  technical-finding.md
    finding-taxonomy.md  radelement.md  radlex.md  loinc-playbook.md  ...
  semantic-foundation/
    index.md
    finding-models/
      why-finding-models.md               Concept (narrative)
      finding-model-format.md             Format Specification (fields, attribute types, index codes, contributors)
      identifiers.md                      Reference (OIFM and OIFMA ID scheme, ids.json)
      content-catalog.md                  Project Profile (findingmodels repo, how to browse)
      finding-taxonomies.md               Reference (MGB exam-oriented sub-taxonomies, 3,789 rows, matching status)
      authoring-workflow.md               Guide (Forge, findingmodel-ai, agent skills, review)
      enrichment-pipeline.md              Concept (AI enrichment design as documented)
      finding-models-and-cdes.md          Concept (the workbench relationship)
    common-data-elements/
      cdes-and-radelement.md              Concept (CDE sets, elements, schema 1.0 and 1.1, schema-vs-API gaps)
      cde-staging.md                      Project Profile (two authoring conventions, pipeline to RadElement)
      next-generation-vocabulary.md       Concept (FindingClass, DataElement, Measurement, relationships, anatomy axis; status draft; sourced to next-gen-2026)
    anatomic-locations/
      why-anatomic-locations.md           Concept
      data-model.md                       Format Specification (fields, hierarchies, laterality triads, code mappings, counts)
      laterality-conventions.md           Reference (migrated)
      lineage-and-current-implementation.md Concept (two lineages, which is current)
      radlex-integration.md               Concept (RadLex structure, issue #3, overlay agreement)
      tooling.md                          Guide (anatomic-locations CLI and search, wrapper libraries)
    exam-types/
      overview.md                         Concept (goals: preferred entries, LOINC/Playbook wrapper, edges to anatomy)
      existing-building-blocks.md         Reference (med-ontology-lookup roadmap, LOINC in the IPL, template corpus)
    terminologies/
      ontologies-used.md                  Reference (RadLex, SNOMED CT, FMA, LOINC, UMLS, RadElement: roles and ID forms)
      med-ontology-lookup.md              Project Profile
  data-structures/
    index.md
    hierarchy.md                          Concept (Observation, Exam Finding List, Imaging Problem List, Imaging Persona)
    observation.md                        Data Structure
    exam-finding-list.md                  Data Structure (fields, example, provenance)
    imaging-problem-list.md               Data Structure (grouping key, status model, example)
    imaging-persona.md                    Concept (goals only)
    anatomic-location-assignment-rules.md Reference (migrated from imaging-problem-list dev)
    technical-imaging-findings.md         Reference (migrated)
    fhir-mapping.md                       Concept (documented mapping, lineage precedents, implementation status)
    ihe-idr-alignment.md                  Concept
    sample-data.md                        Reference (example patients, counts)
  applications/
    index.md
    finding-model-forge.md                Project Profile
    finding-models-site.md                Project Profile
    imaging-problem-list-viewer.md        Project Profile (viewer and viewer_v2)
    report-extraction-platform.md         Project Profile (imaging-problem-list dev: extraction, coding, persistence, review)
    finding-and-location-coding.md        Concept (the coding pipeline as documented)
    ipl-mvp-extraction.md                 Project Profile
    reporting-sdk.md                      Concept (stated direction, no artifact)
  roadmap/
    index.md
    roadmap-2026.md                       Roadmap (from the deck: working group, pillars, next steps)
    finding-model-format-evolution.md     Roadmap (canonical metadata rewrite, relationships and graph ideas from the CDE work, schema versioning: stated goals only)
    finding-model-content-direction.md    Roadmap (taxonomies as the content spine, Gamuts supersession, in-flight batches, triage)
    ipl-data-model-system.md              Roadmap (issue #1 and the dev-branch direction)
    exam-types.md                         Roadmap
    anatomic-locations-and-radlex.md      Roadmap
    open-questions.md                     Reference (per area)
  history/
    index.md
    timeline.md                           History
    lineage-repositories.md               History (one section per lineage repo, status, what survives)
    extraction-approaches.md              History (template_extraction, SAR templates, ReportFindingRefiner, get_ontology_findings)
    cde-template-rendering.md             History (CDETemplateDemo pattern)
    use-cases.md                          Reference (the use case catalog and value categories)
    site-articles.md                      Reference (the 15 posts, dated, summarized, linked)
  repositories/
    index.md
    repository-map.md                     Reference (every repo: org, role, status, branch of record, links into this bundle)
  references/                             verbatim or near-verbatim material, OKF convention
    status-update-2026-01.md              Presentation Extract (the deck)
    finding-model-schema.md               Reference (prose schema mirror, verbatim)
    anatomic-location-json-schema.md      Reference (verbatim)
    exam-finding-list-example.md          Worked Example (real sample JSON)
    imaging-problem-list-example.md       Worked Example
    oifm-overview-extract.md              Source Extract (from next-gen-2026 notes)
  guides/
    authoring-guide.md                    Guide (for humans and agents: types, frontmatter, trust workflow, links, migration procedure)
    migration-ledger.md                   Reference (every migrated doc: source repo, path, commit, destination, date)
  plans/
    index.md
    2026-09-20-knowledgebase-build-plan.md  this document
```

Repository root, outside the bundle: `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `DEV_LOG.md`, `LICENSE`, `tools/check_bundle.py`, `site/` (generator config), `.github/workflows/`.

# Conventions

**Frontmatter.** `type`, `title`, `description`, `tags`, `status`, `generated` on every concept document. `sources` whenever content derives from a repo doc, a site post, or the deck, with `resource` as a permalink (commit-pinned GitHub URL where possible). `verified` only when the project lead signs off. `stale_after` on project profiles and roadmap docs, set one year out.

**Document types.** Inherited from `next-gen-2026` and kept: Reference, Analysis, Decision Record, Proposal, Playbook, Worked Example, Presentation Extract, Meeting Notes, Draft Specification, Gap Log, Exploration. Added: Overview, Concept, Glossary Term, Format Specification, Data Structure, Project Profile, Guide, Roadmap, History, Source Extract, Plan. Proposal and Decision Record are reserved for the next workstream. The checker enforces this list.

**Links.** Bundle-relative absolute links (`/glossary/oifm.md`). Every concept links to its glossary terms on first use and to the repository map. External links go to commit-pinned GitHub URLs for files and to the live sites for deployed tools.

**Naming.** "Open Imaging Data Model (OIDM)" for the project, "Open Imaging Finding Model (OIFM)" for a finding model definition, "finding model" thereafter. Repos are named by their GitHub name in code font. The old name "Open Radiology Data Model" appears only in history.

**People.** Organizations only. The project lead is named as such.

**Migration.** A migrated document keeps its substance, gets frontmatter and links, is rewritten only for consistency of terms, and is recorded in the migration ledger with source repo, path, and commit. The follow-up round of source-repo pull requests works from the ledger.

# Tooling and site

**Validation, two gates.** `uv run .agents/skills/validate/scripts/okf_validate.py knowledge --strict` for OKF conformance. `tools/check_bundle.py`, ported from `next-gen-2026`, for the stricter house rules: type vocabulary, index coverage in every directory, link resolution, balanced fences, no empty headings, denylist sweep for emails and individual names. The diagram-freshness rules are dropped until diagrams exist.

**Site.** Quartz 5 is recommended: folder-driven navigation, tag pages, search, arbitrary frontmatter, Mermaid, and a link graph with backlinks, all built in. Its release hygiene is weak (no tag since 2023), so CI pins a commit. Astro Starlight is the runner-up if a more conventional toolchain is preferred. Phase 0 includes a short spike to confirm the Quartz config keys the researcher could not verify against live docs: content path, absolute markdown link resolution, and a frontmatter badge component. Deploy with GitHub Actions to GitHub Pages. Run a link checker over the built output.

# Phases

Each phase ends with validation passing, `log.md` and `DEV_LOG.md` updated, and this plan's phase table updated.

## Phase 0: Scaffold

Done so far: `git init`, LICENSE, `.gitignore`, OKF skills installed, source repos cloned, inventories complete.

Remaining:

1. Initialize the bundle with `okf_init.py`, then replace the placeholder with the directory skeleton and index files above.
2. Write `guides/authoring-guide.md`, root `CONTRIBUTING.md`, and root `README.md`.
3. Port `check_bundle.py` into `tools/` with the type vocabulary and denylist; wire both validators into a GitHub Actions workflow.
4. Spike Quartz in `site/`, confirm the three unverified config points, render the skeleton, and set up Pages deploy.
5. Start `CHANGELOG.md` and `DEV_LOG.md`.

## Phase 1: Spine

Overview, glossary, repository map, history, references. These are written first because every later document links into them.

- Opus synthesis agents, one per directory, each given the relevant inventory reports, the source file paths, the authoring guide, and the deck extract.
- The glossary harvests every definition-like statement the inventories quoted and flags conflicts for the project lead in `roadmap/open-questions.md`.
- The Ghost posts and the deck become extracts in `references/` and summaries in `history/`.

## Phase 2: Semantic foundation

Finding models, common data elements, anatomic locations, exam types, terminologies. Four Opus agents, one per subdirectory. The next-generation vocabulary document is written as facts about what the `next-gen-2026` branch defines, with `status: draft` and sources pointing at the branch.

## Phase 3: Data structures

Observation, Exam Finding List, Imaging Problem List, Imaging Persona, assignment rules, FHIR mapping, IHE alignment, sample data. One Opus agent with the deep imaging-problem-list inventory, both branches' domain docs, the FHIR lineage material, and the deck.

## Phase 4: Applications

Forge, site, viewer, extraction platform, coding pipeline, MVP extraction, reporting SDK. One Opus agent.

## Phase 5: Roadmap

Goals and open questions per area, drawn from the deck, GitHub issues, and plan documents in the repos. Stated as goals, never as proposals. One Opus agent, reviewed closely by the main session for the facts-and-goals-only rule.

## Phase 6: Integration and review

1. Main session cross-link pass: every concept links to its terms, its repositories, its roadmap entries, and its history.
2. Both validators pass under strict mode. Site builds and deploys. Link checker passes.
3. The project lead reviews document by document. Each accepted document gains `verified` and `status: stable`. Rejections go back to the phase's agent with notes.
4. Documentation review: this plan marked complete, `CHANGELOG.md` reflecting the first release, `DEV_LOG.md` current, migration ledger complete.
5. Follow-ups filed as issues: source-repo pull requests replacing migrated docs with links; manuscripts to integrate; the proposals workstream (finding model format evolution, exam types, IPL data model system).

# Phase status

| Phase | Status | Notes |
|---|---|---|
| 0 Scaffold | done | init, license, skills, clones, inventories, skeleton, guide, checker, CI validation and site workflows, Quartz site building from a link-normalized staging copy |
| 1 Spine | done | overview (4), deck extract, glossary (48 terms), repository map, history (6), references (7); conflicts collected for the roadmap phase |
| 2 Semantic foundation | done | finding models (8), CDEs (3), anatomic locations (6), exam types (2), terminologies (2) |
| 3 Data structures | done | 10 documents including two migrations |
| 4 Applications | done | 7 documents |
| 5 Roadmap | done | six roadmap documents plus open questions (90 entries, 21 upstream defects) |
| 6 Integration and review | in progress | validators clean (115 concepts, 0 errors, 0 warnings), site builds, ledger and log merged; awaiting the project lead's document-by-document verification, then CHANGELOG release entry and follow-up issues |

# Questions for the project lead

Answers can come at approval time or during Phase 1.

1. Answered 2026-09-21: the whole work edge is in scope. The imaging-problem-list `dev` branch is current state, `main` is the stable spec, and the findingmodels taxonomy branch is the content direction.
2. FindingModelForge is documented from `dev` and `feature/model-editing` (assumed; not contradicted).
3. Answered 2026-09-21: the per-modality taxonomies are called the "MGB exam-oriented sub-taxonomies"; no author name.
4. Answered 2026-09-21: publish the next-generation vocabulary document as draft, sourced to the branch, no committee material.
5. Answered 2026-09-21: publish the use case catalog with the committee credit.

# Risks

- **Drift while writing.** Source repos are active. Every `sources` entry pins a commit so a reader can tell what version was read.
- **Overreach into proposals.** Phase 5 and the next-generation vocabulary document are the places this is most likely. Review checks for it explicitly.
- **Site generator immaturity.** Quartz pinned by commit; Starlight as the fallback, with content unaffected either way.
- **Individual names in sources.** The denylist sweep catches author names from the source repos before publish.
