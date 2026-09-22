---
type: Guide
title: Getting involved
description: Where the OIDM community gathers, which repositories to start with, how to file issues, how content is contributed, and how this knowledgebase is edited.
tags: [overview, community, contributing]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:34:50Z }
sources:
  - id: site-involved
    resource: https://www.openimagingdata.org/how-to-get-involved/
    title: "How to Get Involved, openimagingdata.org, 2023-08-14"
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026
  - id: forge
    resource: https://github.com/openimagingdata/FindingModelForge/blob/15d9ebcf64734b889081feed4d645a0afca67e61/docs/DRAFT_WORKFLOW.md
    title: Draft workflow, FindingModelForge dev branch
  - id: catalog-site
    resource: https://github.com/openimagingdata/finding-models-site/blob/6298fa3b900bb46b488f82d0a5b9aab06f70ca69/src/pages/index.astro
    title: Finding model catalog site home page, with its Submit Issue route
  - id: fm-content
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/schema/finding_model_schema.md
    title: Finding model schema, prose mirror, findingmodels repository
---

# Where the project gathers

OIDM's work is public. These channels provide access to its code, content, tools, and discussions.

| Channel | Where | What it is for |
|---|---|---|
| GitHub organization | <https://github.com/openimagingdata> | Code, content, specifications, issue trackers |
| Project site | <https://openimagingdata.org> | Articles explaining the model, project news, registration for updates |
| Slack | The Radiology Informatics workspace at <https://info-rad.slack.com>, channel `#openimagingdata` | Discussion between meetings |
| Finding Model Forge | <https://fmf.oidm.org> | Authoring finding models through a browser |
| IPL viewer demo | <https://imaging-problem-list.pages.dev> | Seeing an Imaging Problem List rendered from real sample data |

Use GitHub and Slack for current discussions. The site's August 2023 participation post invites newsletter registration and article comments, describes use-case and standards working groups, and seeks related projects and venues.[^site-involved] Some details have aged. The advertised working group on the TypeScript reference implementation concerns a repository now kept for lineage. The meeting section remains a placeholder. The site also has a contact link for general inquiries.

The January 2026 deck proposes an "ACR-OIDM Structured Imaging Results Working Group" co-hosted with the ACR. It would bring together experts and vendors, with a use-case pipeline feeding the ACR and RSNA common data element group.[^deck] The group is not recorded as convened.

# Repositories to start with

Choose a repository by task. [The repository map](/repositories/repository-map.md) lists all repositories, including lineage projects, with their status and branches of record.

| If you want to | Start at |
|---|---|
| Read or use the finding model content | `openimagingdata/findingmodels`, 2,382 definitions with a prose schema mirror |
| Build against the finding model format | `openimagingdata/findingmodel`, the Python library, CLI tools, and MCP server |
| Understand the data structures | `openimagingdata/imaging-problem-list`, whose `main` branch holds the stable Exam Finding List and Imaging Problem List specification and sample data |
| See extraction from narrative reports | The same repository's `dev` branch, which holds the extraction, coding, persistence, and review platform |
| Look up codes across terminologies | `openimagingdata/med-ontology-lookup`, the `molu` library and CLI |
| Work on the authoring application | `openimagingdata/FindingModelForge` |

Check the repository map before starting. Several repositories keep current work on branches other than `main`.

# Filing issues

File issues in the repository that owns the affected content or code.

- Report wrong, missing, or badly scoped finding models to `openimagingdata/findingmodels`. The public catalog's "Submit Issue" link goes there.[^catalog-site]
- Report library, CLI, or anatomic location data problems to `openimagingdata/findingmodel`.
- Ask data structure questions in `openimagingdata/imaging-problem-list`. Its open, unclaimed issue #1 requests a formal model layer with JSON Schema export for Observation, Exam Finding List, and Imaging Problem List.
- Report terminology lookup problems to `openimagingdata/med-ontology-lookup`.

See [roadmap](/roadmap/) for open issues by area.

# Contributing content

Content includes [finding models](/glossary/finding-model.md) and their [anatomic locations](/glossary/anatomic-location.md). Choose one of three contribution routes.

**Finding Model Forge.** To author a single model in the browser, sign in with GitHub and name the finding. Generate and edit its description and synonyms, then generate attributes. The draft autosaves. Submission locks it for review, and a reviewer moves it through under review to added or declined.[^forge] Editing a model after creation is an open issue on that repository, not yet available.

**The content repository.** Definitions are JSON files, one per finding, validated on commit. A registry issues identifiers and detects duplicates. Repository agent skills support batch authoring and review. Use the prose schema mirror when editing definitions directly.[^fm-content]

**Staged common data elements.** Informal candidate definitions go into `openimagingdata/CDEStaging` before formal ACR and RSNA review and publication through RadElement. This is a manual curation workflow.

Identifier discipline matters in all three routes. An [OIFM identifier](/glossary/oifm.md) encodes its contributing organization in its letter block, and identifiers are never reissued or regenerated on a round trip. See [the authoring workflow](/semantic-foundation/finding-models/authoring-workflow.md) for conventions.

# Contributing to this knowledgebase

This repository provides canonical high-level documentation as an Open Knowledge Format bundle for people and agents. It describes and links to catalogs; it does not copy them. Keep installation instructions, API usage, and developer workflows with the code.

Read [the authoring guide](/guides/authoring-guide.md) before editing. It covers document types, frontmatter, draft verification, links, and document migration. Two checkers must pass on every push: the Open Knowledge Format validator and a house checker for types, index coverage, links, names, and email addresses.

Two house rules catch newcomers. Facts and stated goals only, with every goal citing the deck, issue, or plan that states it, because design proposals belong to a separate workstream. And organizations, not individuals: the project lead is named as such and nobody else is named.

[^site-involved]: "How to Get Involved", openimagingdata.org, 2023-08-14
[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
[^forge]: Draft workflow, FindingModelForge dev branch
[^catalog-site]: Finding model catalog site home page
[^fm-content]: Finding model schema, prose mirror, findingmodels repository
