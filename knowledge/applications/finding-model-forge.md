---
type: Project Profile
title: Finding Model Forge
description: The web application at fmf.oidm.org where contributors author finding model definitions through an AI-assisted wizard and move them through a draft review lifecycle.
tags: [applications, finding-models, authoring, llm, mongodb]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
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

Finding Model Forge is the authoring front end of the Open Imaging Data Model (OIDM). It exists so that a radiologist who is not a programmer can create a [finding model](/glossary/finding-model.md) definition, have identifiers and standard codes assigned automatically, and put the result in front of reviewers. The January 2026 status deck names it as the tool behind the claim that finding models are a rapid-innovation workbench ahead of formal [common data element](/glossary/cde.md) adoption.[^deck]

The application is a FastAPI web wrapper around the `findingmodel` Python library, which supplies the actual generation, similarity search, and identifier assignment.[^forge-readme] The library is documented under [the finding models area](/semantic-foundation/finding-models/authoring-workflow.md); this profile covers the application.

# What a user does with it

Sign-in is GitHub OAuth. After that the creation flow is two steps followed by draft editing, streamlined from an earlier five-step wizard.[^forge-workflow] The whole flow happens inside one page: the server returns HTTP 303 responses, HTMX intercepts them and swaps content into a single container, and the browser never navigates. The creation-workflow document is emphatic about this because it changes how the flow is tested.

| Stage | User action | What the server does |
|---|---|---|
| 1. Basic information | Enter the finding name, press "Generate Description" | Generates a description from the name |
| 2. Description refinement | Review or edit the description, optionally add synonyms, press "Check for Similar" | Runs a semantic similarity search against existing models; shows near-matches, or creates a draft if there are none |
| 3. Draft editing | Edit description, manage synonyms, write the attributes in markdown; press "Update & Preview" | Autosaves as you type, then generates the full finding model JSON including identifiers and standard codes |
| 4. Preview and submission | Review the generated model, press "Submit Draft" | Moves the draft to `submitted` and locks editing |

The finding name is read-only once the draft exists. A creation session tracks progress through the first two steps and expires after an hour of inactivity. Drafts appear on the user's profile page, where editing can be resumed; resuming a name that was already submitted lands on the final display view instead of the editor.[^forge-draft]

# The draft object and its lifecycle

A draft is the unit of work. It carries the owning user, the finding name, the human inputs (description, synonyms, attributes markdown), the server-generated finding model JSON, a status, and an action log of timestamped entries recording who did what.[^forge-draft]

```text
draft ──submit──▶ submitted ──▶ under-review ──▶ added
                                             └──▶ declined
```

Five statuses exist: `draft`, `submitted`, `under-review`, `added`, and `declined`. Submission locks further editing; everything after it is administrative review. A peer-review layer sits alongside this lifecycle on the development branch: a public draft state lets other contributors read and comment on a draft before it is submitted, and a comment feature is scoped to drafts in the submitted, under-review, added, and declined states. Both are stated as serving collaborative refinement rather than approval gating.[^forge-public-review][^forge-comments]

# Data it reads and writes

MongoDB holds drafts, users, and organizations, accessed asynchronously through Motor.[^forge-db] Redis provides a caching layer for user and finding model data; the implementation always calls the cache, and the calls become safe no-ops when Redis is unavailable.[^forge-draft] Two DuckDB files supplied by the `findingmodel` library must be present in the platform data directory, one for finding models and one for [anatomic locations](/glossary/anatomic-location.md), which is how similarity search and code lookup work offline of any web service.[^forge-readme]

The output format is the finding model JSON defined by [the finding model format](/semantic-foundation/finding-models/finding-model-format.md), carrying an [OIFM identifier](/glossary/oifm.md) and per-[attribute](/glossary/attribute.md) identifiers. Drafts store the generated JSON inline; the definitive corpus lives in the separate content repository described in [the content catalog](/semantic-foundation/finding-models/content-catalog.md).

# Language model use

Three generation steps are documented, with the timeouts the application budgets for them.[^forge-workflow]

| Step | Task | Budgeted time |
|---|---|---|
| Stage 1 | Generate a description from the finding name | 2 to 5 seconds, with a default description as fallback |
| Stage 2 | Semantic similarity search against existing models | 15 to 30 seconds |
| Stage 3 | Generate the complete finding model JSON, including identifier assignment and standard codes | 30 to 90 seconds |

All three are calls into the `findingmodel` library rather than code in this repository.

# Architecture

One FastAPI process serves both the pages and the API. Templates are Jinja2, with Flowbite components for layout, Alpine.js for client state, and HTMX driving every transition as a server-rendered fragment swap; the house rule is to keep interactivity in Alpine and HTMX rather than custom JavaScript. MongoDB through Motor is the store, Redis the cache, and the `findingmodel` library the engine. Static assets are built with Vite and resolved through its manifest.[^forge-readme][^forge-draft]

# Deployment

Live at [fmf.oidm.org](https://fmf.oidm.org). The container needs MongoDB and Redis running alongside it, a GitHub OAuth application for sign-in, and the two DuckDB data files.[^forge-readme] Bringing the deployment compose file into the repository is open issue 9, and a development compose file is open issue 7. Install and run instructions stay with the code; this profile does not repeat them.

# Repository and branch of record

`FindingModelForge` in the `openimagingdata` organization. See [the repository map](/repositories/repository-map.md) for how it relates to everything else.

| Branch | Tip commit | Date | State |
|---|---|---|---|
| `main` | `f55dc85` | 2025-08-20 | Stale relative to `dev`; the deployed feature set predates the refactor |
| `dev` | `15d9ebc` | 2026-01-02 | Branch of record, 96 commits ahead of `main`, unmerged |
| `feature/model-editing` | `af357f8` | 2025-11-28 | 60 commits ahead of `main`, unmerged |

Neither long-lived branch has an open pull request as of 2026-09-21.

# What is in flight

**The `dev` refactor.** Ninety-six commits consolidate a service-layer extraction, a router cleanup, standardization of the HTMX and Alpine patterns, and a rebuilt test infrastructure. The branch's own complexity assessment names what remains in the service and router layers after that work. The peer-review workflow described above, public drafts plus comments, is finished on `dev` and absent from `main`.[^forge-public-review][^forge-comments]

**Model editing, issue 13.** Opened 2025-10-16 and still open. The implementation on `feature/model-editing` answers it with AI-assisted *iterations* rather than manual editing: a user submits a natural-language description of the change they want, and the library applies it.[^forge-iteration] The constraints are explicit. The model name cannot change, one iteration draft exists per user per published model, the existing action log carries the audit trail, and manual edits to an iteration draft are not permitted. It builds on the `model_editor` module added in `findingmodel` 0.6.0, whose guardrails preserve the [OIFM identifiers](/glossary/oifm.md) and reject unsafe changes. Sprint 1, natural-language iteration, is complete as of 2025-11-27. Sprint 2, markdown-edit iteration, and Sprint 3, enhanced history, are not started.

# Open issues

| Issue | Title | Opened | State |
|---|---|---|---|
| 13 | Implement model editing | 2025-10-16 | Open; partly implemented on `feature/model-editing` |
| 9 | Bring the VPS compose/deploy into repository | 2025-05-30 | Open |
| 7 | Make a dev Docker Compose file | 2025-05-27 | Open |

# History

A superseded version of the application survives in the repository under `zOld/`, together with its planning notes.[^forge-zold] Those notes record decisions the current application still reflects: a deliberate commitment to MongoDB with the Beanie object-document mapper after considering embedded vector stores, a front end on the same FastAPI instance as the API, and GitHub OAuth holding authorization in the session. The three mini-sprint task lists from November 2024 through April 2025 show the feature set arriving in order, beginning with generating a finding model from nothing but a finding name, then adding identifiers, a user table, and searchable [common data element](/glossary/cde.md) content. Most of their boxes are still unchecked, including batch creation from a CSV file and links from a finding model to its eventual CDE codes.

# What it realizes

Finding Model Forge is where the [contributor](/glossary/contributor.md) meets the [finding model](/glossary/finding-model.md) format. It assigns [OIFM identifiers](/glossary/oifm.md) with their [organization code](/glossary/oidm-organization-code.md), writes [attributes](/glossary/attribute.md) and their values, and attaches [index codes](/glossary/index-code.md) into external terminologies. Its place in the stack is drawn in [the architecture overview](/overview/architecture.md), and the authoring path it implements is described end to end in [the authoring workflow](/semantic-foundation/finding-models/authoring-workflow.md).

[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
[^forge-readme]: FindingModelForge README, dev branch
[^forge-workflow]: Finding model creation workflow, FindingModelForge dev branch
[^forge-draft]: Finding model draft workflow, FindingModelForge dev branch
[^forge-db]: MongoDB collections and access, FindingModelForge dev branch
[^forge-public-review]: Public draft review feature requirements, FindingModelForge dev branch
[^forge-comments]: Comments feature requirements, FindingModelForge dev branch
[^forge-iteration]: Model iteration feature implementation plan, FindingModelForge feature/model-editing branch
[^forge-zold]: FindingModelForge zOld/plans, the superseded application's planning notes
