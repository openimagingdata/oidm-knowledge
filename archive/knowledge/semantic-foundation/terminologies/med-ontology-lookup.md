---
type: Project Profile
title: med-ontology-lookup
description: Medical terminology lookup, crosswalks, provider failures, planned features, and integration status.
tags: [semantic-foundation, terminologies, tooling, project-profile]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
stale_after: 2027-09-21
sources:
  - id: readme
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/README.md
    title: med-ontology-lookup README, install, API keys, and CLI usage
  - id: models
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/src/med_ontology_lookup/models.py
    title: Concept, collection, and provider failure models, med-ontology-lookup
  - id: detect
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/src/med_ontology_lookup/detect.py
    title: Input kind detection, med-ontology-lookup
  - id: config
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/src/med_ontology_lookup/config.py
    title: Default ontologies and source abbreviation maps, med-ontology-lookup
  - id: skill
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/skills/med-ontology-lookup/SKILL.md
    title: Agent skill for the molu command line tool
  - id: roadmap
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/docs/product-roadmap.md
    title: med-ontology-lookup product roadmap, the terminology gateway framing
  - id: review
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/docs/project-review-and-proposal.md
    title: Project review and proposal, the six-phase delivery sequence and the delegated authentication design
  - id: backlog
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/docs/plans/2026-09-05-github-issue-backlog.md
    title: GitHub issue backlog, one tracking issue and eleven focused issues
  - id: failures
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/a1fd3ae7ca6a28bb7e5af6838fe4167938084389/docs/plans/2026-09-14-typed-provider-failures.md
    title: Typed provider failures and operation-aware fallback, design and fallback policy
  - id: fm-issue-34
    resource: https://github.com/openimagingdata/findingmodel/issues/34
    title: findingmodel issue 34, move the BioOntology client into oidm-common
  - id: enrichment-plan
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/docs/finding-enrichment-implementation-plan.md
    title: Finding enrichment implementation plan, findingmodel main branch
---

# What it is

`med-ontology-lookup` is a Python library and CLI, `molu`, for medical terms and codes in [RadLex](/glossary/radlex.md), [SNOMED CT](/glossary/snomed-ct.md), [FMA](/glossary/fma.md), [LOINC](/glossary/loinc.md), and [UMLS](/glossary/umls.md). It calls BioPortal and UMLS Terminology Services REST APIs.[^readme] Its role is phrase-to-code lookup for tasks such as [index code](/glossary/index-code.md) assignment to [finding models](/glossary/finding-model.md), anatomic coding, and enrichment. Package integration remains pending, as described below.

The roadmap calls it "the small, dependable layer that lets people and agents resolve medical language to versioned concepts, inspect the clinically relevant part of an ontology graph, and translate identifiers without learning each terminology provider's API."[^roadmap]

See `openimagingdata/med-ontology-lookup`'s README for installation and API keys.[^readme]

# Providers and credentials

Two backends, selected by which keys are present.

| Provider | Reached through | Supplies | Key |
|---|---|---|---|
| BioPortal | `data.bioontology.org` | Multi-ontology class search, concept retrieval, one-hop hierarchy | `BIOPORTAL_API_KEY`, with `BIOONTOLOGY_API_KEY` accepted as an alias |
| UMLS Terminology Services | `uts-ws.nlm.nih.gov` | CUI resolution and crosswalk | `UMLS_API_KEY`, requiring a UMLS licence |

Either key works alone, with reduced capability; crosswalk and CUI resolution need UMLS, and multi-ontology search and hierarchy need BioPortal. With both set, search queries both APIs and merges the results.[^readme] The default BioPortal ontologies are `RADLEX`, `SNOMEDCT`, `FMA`, and `LOINC`, and the default crosswalk targets are the UMLS source abbreviations `SNOMEDCT_US`, `FMA`, `RADLEX`, and `LNC`.[^config] The tool does not read a `.env` file itself; keys must already be in the environment.

# Operations

| Operation | What it does |
|---|---|
| `search` | Free-text search across the profile's ontologies, with per-ontology queries so that SNOMED CT does not crowd out RadLex |
| `lookup` | Auto-detects whether the input is a term, a source code, or a CUI, then routes accordingly |
| `get` | Retrieves one concept by CUI, RadLex identifier, SNOMED CT code, or FMA identifier |
| `crosswalk` | Translates through UMLS CUIs to codes in other source vocabularies |
| `parents` and `children` | One hop up or down the hierarchy, for structural checks |
| Semantic type filters | `-t` keeps untyped hits, `-T` requires a type match |

Detection is deliberately conservative: anything ambiguous stays a term so that search still works. A CUI is `C` followed by seven or more digits; RadLex is `RID` plus digits; FMA needs an explicit prefix; LOINC is one to seven digits, a hyphen, and one or two digits; a bare six to eighteen digit integer is treated as SNOMED CT.[^detect]

Results are typed. A `Concept` carries `concept_id`, `code`, `ontology`, `pref_label`, `synonyms`, `definition`, `semantic_types`, `cuis`, an `obsolete` flag, a user interface link, and the backend that produced it.[^models]

# Typed provider failures

The distinguishing design decision is that a failure is a result, not a silent fallback. A `ProviderFailure` carries a `FailureCategory`, including `not_found`, `authentication`, `authorization`, `licensing`, `rate_limited`, `timeout`, `unavailable`, and `invalid_response`, and a `ProviderOperation` naming which call failed.[^models] The policy is that only absence of a result or an unsupported operation may trigger a fallback to another provider; authentication, licensing, rate limit, timeout, and upstream unavailability stay visible instead of being disguised as an empty answer.[^failures]

An unlicensed SNOMED CT or UMLS caller gets a licensing failure rather than an apparent missing concept.

# Agent skill

The portable skill at `skills/med-ontology-lookup/` instructs agents to classify input, search free text first, and use the CLI instead of scraping BioPortal or UMLS.[^skill] Coding workflows in other repositories use it.

# Stated direction

Two documents state where the project is going. Both are planning documents in the repository, not released behaviour.

The **project review and proposal** sets out a six-phase delivery sequence after a governance phase: an offline baseline and provider-failure contract; trustworthy lookup contracts covering backend selection, identity, bounded collections, and provenance; delegated authentication with live contract checks and diagnostics; release preparation with an explicit publication checkpoint; an agent-ready terminology workflow; and bounded graph context with typed mappings.[^review] It also contains the delegated authentication design: a mode in which the tool reaches providers through a proxy so that upstream API keys need not live in client environments, with the guarantee that credentials are absent from final outgoing requests and that the authentication method is never inferred from a hostname.[^review][^backlog]

The **issue backlog** turns that sequence into one tracking issue and eleven focused issues, in dependency order: offline CI, typed provider failures, explicit backend selection and readiness, shared identifier normalization, bounded collection semantics, request and terminology provenance, ambiguity-preserving UMLS expansion, direct and delegated provider endpoints, opt-in live contract checks, bounded provider diagnostics, and hardened release preparation.[^backlog]

The **product roadmap** adds the domain profile design, including the `radiology` default profile that would make the [LOINC/RSNA Radiology Playbook](/glossary/loinc-rsna-radiology-playbook.md) first-class. That part is catalogued under [existing building blocks for exam types](/semantic-foundation/exam-types/existing-building-blocks.md) because it is the only written exam-type design in any OIDM repository.

# Status

Read at `main`, commit `a1fd3ae`, dated 2026-09-20.

- There are no unmerged branches. The two named feature branches were merged and are now ancestors of `main`.
- Typed provider failures shipped on 2026-09-20.
- Offline continuous integration is implementation-complete but uncommitted, living in a sibling worktree and awaiting authorization to publish.
- Of the twelve backlog issues, only typed provider failures is closed; the tracking issue and ten others remain open, plus one filed outside the sequence for bounded, credential-safe caching.
- Delegated authentication is designed and not built.

# Relation to the rest of OIDM

The `findingmodel` enrichment pipeline performs ontology and anatomic searches concurrently, a completed phase.[^enrichment-plan] It uses its own BioOntology client. Issue 34 requests moving that client and search protocol to `oidm-common`, with a hard break requiring an environment-only API key.[^fm-issue-34]

Neither `findingmodel` nor `findingmodels` links to this repository, and no OIDM package depends on it. Integration is a direction, not an implemented dependency. See [the repository map](/repositories/repository-map.md).

[^readme]: med-ontology-lookup README
[^models]: Concept and provider failure models, med-ontology-lookup
[^detect]: Input kind detection, med-ontology-lookup
[^config]: Default ontologies and source abbreviation maps, med-ontology-lookup
[^skill]: Agent skill for the molu command line tool
[^roadmap]: med-ontology-lookup product roadmap
[^review]: Project review and proposal
[^backlog]: GitHub issue backlog
[^failures]: Typed provider failures and operation-aware fallback
[^fm-issue-34]: findingmodel issue 34
[^enrichment-plan]: Finding enrichment implementation plan, findingmodel main branch
