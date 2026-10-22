---
type: Project Profile
title: Finding Model Forge
description: The application at fmf.oidm.org for authoring finding models with AI assistance and reviewing drafts.
tags: [applications, finding-models, authoring, llm, mongodb]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:34:50Z }
stale_after: 2027-09-21
sources:
  - id: forge-readme
    resource: https://github.com/openimagingdata/FindingModelForge/blob/15d9ebcf64734b889081feed4d645a0afca67e61/README.md
    title: FindingModelForge README, dev branch
  - id: forge-workflow
    resource: https://github.com/openimagingdata/FindingModelForge/blob/15d9ebcf64734b889081feed4d645a0afca67e61/docs/finding-model-creation-workflow.md
    title: Finding model creation workflow, FindingModelForge dev branch
    last_modified: 2025-08-31
  - id: forge-draft
    resource: https://github.com/openimagingdata/FindingModelForge/blob/15d9ebcf64734b889081feed4d645a0afca67e61/docs/DRAFT_WORKFLOW.md
    title: Finding model draft workflow, FindingModelForge dev branch
  - id: forge-db
    resource: https://github.com/openimagingdata/FindingModelForge/blob/15d9ebcf64734b889081feed4d645a0afca67e61/docs/database.md
    title: MongoDB collections and access, FindingModelForge dev branch
  - id: forge-public-review
    resource: https://github.com/openimagingdata/FindingModelForge/blob/15d9ebcf64734b889081feed4d645a0afca67e61/tasks/done/PRD-public-draft-review.md
    title: Public draft review feature requirements, FindingModelForge dev branch
  - id: forge-comments
    resource: https://github.com/openimagingdata/FindingModelForge/blob/15d9ebcf64734b889081feed4d645a0afca67e61/tasks/done/comments-feature-prd.md
    title: Comments feature requirements, FindingModelForge dev branch
  - id: forge-iteration
    resource: https://github.com/openimagingdata/FindingModelForge/blob/af357f8decf029d99863ece63f03e1a7e86c18e5/tasks/model_iteration_feature_plan.md
    title: Model iteration feature implementation plan, FindingModelForge feature/model-editing branch
    last_modified: 2025-11-27
  - id: forge-issue-13
    resource: https://github.com/openimagingdata/FindingModelForge/issues/13
    title: FindingModelForge issue 13, "Implement model editing", opened 2025-10-16
  - id: forge-zold
    resource: https://github.com/openimagingdata/FindingModelForge/tree/f55dc858e1e3c3fde64ccd0d53b46ec07374ede6/zOld/plans
    title: FindingModelForge zOld/plans, the superseded application's planning notes
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026
---

# Purpose

**Live:** [fmf.oidm.org](https://fmf.oidm.org) (sign-in with GitHub).

Finding Model Forge lets radiologists create [finding model](/glossary/finding-model.md) definitions without programming. It assigns identifiers and standard codes automatically and accepts drafts for review. The January 2026 Open Imaging Data Model (OIDM) deck presents it as a tool for developing finding models before formal [common data element](/glossary/cde.md) adoption.[^deck]

The FastAPI application wraps the `findingmodel` Python library for generation, similarity search, and identifier assignment.[^forge-readme] See [the authoring workflow](/semantic-foundation/finding-models/authoring-workflow.md) for the library.

# What a user does with it

Users sign in with GitHub OAuth. Creation has two steps followed by draft editing, replacing an earlier five-step wizard.[^forge-workflow] HTMX intercepts HTTP 303 responses and swaps content within one page without browser navigation.

| Stage | User action | What the server does |
|---|---|---|
| 1. Basic information | Enter the finding name, press "Generate Description" | Generates a description from the name |
| 2. Description refinement | Review or edit the description, optionally add synonyms, press "Check for Similar" | Runs a semantic similarity search against existing models; shows near-matches, or creates a draft if there are none |
| 3. Draft editing | Edit description, manage synonyms, write the attributes in markdown; press "Update & Preview" | Autosaves as you type, then generates the full finding model JSON including identifiers and standard codes |
| 4. Preview and submission | Review the generated model, press "Submit Draft" | Moves the draft to `submitted` and locks editing |

The finding name becomes read-only when a draft is created. Creation sessions track the first two steps and expire after an hour of inactivity. Users resume drafts from their profile page. Submitted drafts open in the final display view.[^forge-draft]

# The draft object and its lifecycle

A draft stores its owner, finding name, description, synonyms, attributes markdown, generated model JSON, status, and a timestamped action log recording who performed each action.[^forge-draft]

```text
draft ──submit──▶ submitted ──▶ under-review ──▶ added
                                             └──▶ declined
```

Five statuses exist: `draft`, `submitted`, `under-review`, `added`, and `declined`. Submission locks further editing; everything after it is administrative review. On `dev`, public drafts allow contributors to read and comment before submission. A separate comment feature covers `submitted`, `under-review`, `added`, and `declined` drafts. Both are stated as serving collaborative refinement rather than approval gating.[^forge-public-review][^forge-comments]

# Data it reads and writes

MongoDB stores drafts, users, and organizations through asynchronous Motor access.[^forge-db] Redis caches user and finding model data. Cache calls become no-ops when Redis is unavailable.[^forge-draft] The `findingmodel` library requires two DuckDB files in the platform data directory, one for finding models and one for [anatomic locations](/glossary/anatomic-location.md), to support similarity search and code lookup without web services.[^forge-readme]

Drafts store generated JSON inline in [the finding model format](/semantic-foundation/finding-models/finding-model-format.md), with [OIFM identifiers](/glossary/oifm.md) and per-[attribute](/glossary/attribute.md) identifiers. The definitive corpus lives in [the content repository](/semantic-foundation/finding-models/content-catalog.md).

# Language model use

The workflow documents three library calls and their time budgets.[^forge-workflow]

| Step | Task | Budgeted time |
|---|---|---|
| Stage 1 | Generate a description from the finding name | 2 to 5 seconds, with a default description as fallback |
| Stage 2 | Semantic similarity search against existing models | 15 to 30 seconds |
| Stage 3 | Generate the complete finding model JSON, including identifier assignment and standard codes | 30 to 90 seconds |

# Architecture

One FastAPI process serves pages and the API. Jinja2 renders templates, Flowbite supplies components, Alpine.js manages client state, and HTMX swaps server-rendered fragments. Project conventions place interactivity in Alpine and HTMX instead of custom JavaScript. Vite builds static assets, which the application resolves through its manifest.[^forge-readme][^forge-draft]

# Deployment

Live at [fmf.oidm.org](https://fmf.oidm.org). The container requires MongoDB, Redis, a GitHub OAuth application, and two DuckDB data files.[^forge-readme]

# Repository and branch of record

`FindingModelForge` in the `openimagingdata` organization. See [the repository map](/repositories/repository-map.md) for how it relates to everything else.

| Branch | Tip commit | Date | State |
|---|---|---|---|
| `main` | `f55dc85` | 2025-08-20 | Stale relative to `dev`; the deployed feature set predates the refactor |
| `dev` | `15d9ebc` | 2026-01-02 | Branch of record, 96 commits ahead of `main`, unmerged |
| `feature/model-editing` | `af357f8` | 2025-11-28 | 60 commits ahead of `main`, unmerged |

Neither long-lived branch has an open pull request as of 2026-09-21.

# What is in flight

**The `dev` refactor.** Ninety-six commits consolidate a service-layer extraction, a router cleanup, standardized HTMX and Alpine patterns, and rebuilt test infrastructure. Its complexity assessment records remaining service and router work. Public drafts and comments are complete on `dev` and absent from `main`.[^forge-public-review][^forge-comments]

**Model editing, issue 13.** The `feature/model-editing` branch lets users request changes in natural language.[^forge-iteration] Model names cannot change, and each user can have one iteration draft per published model. The action log records changes, and manual edits are prohibited. The `model_editor` module in `findingmodel` 0.6.0 preserves [OIFM identifiers](/glossary/oifm.md) and rejects unsafe changes. Sprint 1, natural-language iteration, was complete on 2025-11-27. Sprint 2, markdown-edit iteration, and Sprint 3, enhanced history, have not started.

# Open issues

| Issue | Title | Opened | State |
|---|---|---|---|
| 13 | Implement model editing | 2025-10-16 | Open; partly implemented on `feature/model-editing` |
| 9 | Bring the VPS compose/deploy into repository | 2025-05-30 | Open |
| 7 | Make a dev Docker Compose file | 2025-05-27 | Open |

# History

The superseded application and its plans remain in `zOld/`.[^forge-zold] The plans chose MongoDB with Beanie after considering embedded vector stores, shared the FastAPI process between pages and API, and kept GitHub OAuth authorization in the session. Three mini-sprint lists from November 2024 through April 2025 start with generation from a finding name, then add identifiers, a user table, and searchable [common data element](/glossary/cde.md) content. Most checkboxes remain unchecked, including CSV batch creation and links to eventual CDE codes.

# What it realizes

Forge lets [contributors](/glossary/contributor.md) assign [organization code](/glossary/oidm-organization-code.md) identifiers, write attributes and values, and attach [index codes](/glossary/index-code.md) for external terminologies. See [the architecture overview](/overview/architecture.md) and [the authoring workflow](/semantic-foundation/finding-models/authoring-workflow.md).

[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
[^forge-readme]: FindingModelForge README, dev branch
[^forge-workflow]: Finding model creation workflow, FindingModelForge dev branch
[^forge-draft]: Finding model draft workflow, FindingModelForge dev branch
[^forge-db]: MongoDB collections and access, FindingModelForge dev branch
[^forge-public-review]: Public draft review feature requirements, FindingModelForge dev branch
[^forge-comments]: Comments feature requirements, FindingModelForge dev branch
[^forge-iteration]: Model iteration feature implementation plan, FindingModelForge feature/model-editing branch
[^forge-zold]: FindingModelForge zOld/plans, the superseded application's planning notes
