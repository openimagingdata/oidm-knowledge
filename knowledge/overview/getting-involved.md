---
type: Guide
title: Getting involved
description: Where the OIDM community gathers, which repositories to start with, how to file issues, how content is contributed, and how this knowledgebase is edited.
tags: [overview, community, contributing]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T15:00:00Z }
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

Everything OIDM produces is public. The four durable entry points are the GitHub organization, the project site, the Slack channel, and the deployed tools.

| Channel | Where | What it is for |
|---|---|---|
| GitHub organization | <https://github.com/openimagingdata> | Code, content, specifications, issue trackers |
| Project site | <https://openimagingdata.org> | Articles explaining the model, project news, registration for updates |
| Slack | The Radiology Informatics workspace at <https://info-rad.slack.com>, channel `#openimagingdata` | Discussion between meetings |
| Finding Model Forge | <https://fmf.oidm.org> | Authoring finding models through a browser |
| IPL viewer demo | <https://imaging-problem-list.pages.dev> | Seeing an Imaging Problem List rendered from real sample data |

The site's participation post also invites registration for newsletter updates and article comments, describes working groups on use cases and standards work, and asks for help identifying related projects and venues where the work would have impact.[^site-involved] That post dates from August 2023 and parts of it have aged: it advertises a working group on the TypeScript reference implementation, which is now a lineage repository rather than active work, and its meeting section is a placeholder. Treat the GitHub organization and the Slack channel as the current live channels. The site also carries a contact link for general inquiries.

The largest stated organizational goal is not yet a channel you can join. The January 2026 deck proposes an "ACR-OIDM Structured Imaging Results Working Group" co-hosted with the ACR, bringing expert and vendor participants into one venue, with a use-case pipeline feeding the ACR and RSNA common data element group.[^deck] It is a proposal, not a convened body.

# Repositories to start with

Pick by what you want to do. Every repository, including the lineage ones, is listed with its status and branch of record in [the repository map](/repositories/repository-map.md).

| If you want to | Start at |
|---|---|
| Read or use the finding model content | `openimagingdata/findingmodels`, 2,382 definitions with a prose schema mirror |
| Build against the finding model format | `openimagingdata/findingmodel`, the Python library, CLI tools, and MCP server |
| Understand the data structures | `openimagingdata/imaging-problem-list`, whose `main` branch holds the stable Exam Finding List and Imaging Problem List specification and sample data |
| See extraction from narrative reports | The same repository's `dev` branch, which holds the extraction, coding, persistence, and review platform |
| Look up codes across terminologies | `openimagingdata/med-ontology-lookup`, the `molu` library and CLI |
| Work on the authoring application | `openimagingdata/FindingModelForge` |

Several of these repositories have their current state on a branch other than `main`. Check the repository map before assuming the default branch is the live one.

# Filing issues

Each repository carries its own issue tracker, and issues are where the work edge is visible. File against the repository that owns the thing you are reporting.

- **A wrong, missing, or badly scoped finding model** goes to `openimagingdata/findingmodels`. The public catalog site routes its "Submit Issue" link there.[^catalog-site]
- **A bug or gap in the library, CLI, or anatomic location data** goes to `openimagingdata/findingmodel`.
- **A question about the data structures** goes to `openimagingdata/imaging-problem-list`. Its issue #1, asking for a formal model layer with JSON Schema export for Observation, Exam Finding List, and Imaging Problem List, is open and unclaimed.
- **Terminology lookup behavior** goes to `openimagingdata/med-ontology-lookup`.

Existing open issues are the best statement of what the project knows is missing. They are summarized by area under [roadmap](/roadmap/).

# Contributing content

Content means [finding models](/glossary/finding-model.md) and the [anatomic locations](/glossary/anatomic-location.md) they reference. There are three routes, and they differ in how much of the work you do by hand.

**Through Finding Model Forge.** The browser application is the supported route for authoring a single finding model without cloning anything. You sign in with GitHub, name the finding, generate and edit a description and synonyms, generate the attributes, and the draft autosaves. Submitting locks the draft for review, and a reviewer moves it through under review to added or declined.[^forge] Editing a model after creation is an open issue on that repository, not yet available.

**Through the content repository.** Definitions live as one JSON file per finding, validated on commit, with identifiers issued from a registry that detects duplicates. Batch authoring and review run through agent skills held in that repository. Contributing this way means working with the schema directly; the prose mirror of the schema is the reference.[^fm-content]

**Through staged common data elements.** Candidate definitions authored informally, ahead of formal review, are staged in `openimagingdata/CDEStaging` before entering the ACR and RSNA review pipeline that publishes through RadElement. That path is a manual curation workflow rather than an automated one.

Identifier discipline matters in all three routes. An [OIFM identifier](/glossary/oifm.md) encodes its contributing organization in its letter block, and identifiers are never reissued or regenerated on a round trip. The authoring conventions are covered in [the authoring workflow](/semantic-foundation/finding-models/authoring-workflow.md).

# Contributing to this knowledgebase

This repository is the canonical high-level documentation, written as an Open Knowledge Format bundle so that both people and agents can read it. It describes and links to catalogs; it does not copy them. Code documentation, install steps, and developer workflow stay with the code.

Before editing anything here, read [the authoring guide](/guides/authoring-guide.md). It sets the document types, the required frontmatter, the trust workflow by which a draft becomes verified, the linking conventions, and the procedure for migrating a document out of a working repository. Two checkers run on every push and must pass: an Open Knowledge Format conformance validator and a house-rules checker that enforces the type vocabulary, index coverage, link resolution, and a sweep for names and email addresses.

Two house rules catch newcomers. Facts and stated goals only, with every goal citing the deck, issue, or plan that states it, because design proposals belong to a separate workstream. And organizations, not individuals: the project lead is named as such and nobody else is named.

[^site-involved]: "How to Get Involved", openimagingdata.org, 2023-08-14
[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
[^forge]: Draft workflow, FindingModelForge dev branch
[^catalog-site]: Finding model catalog site home page
[^fm-content]: Finding model schema, prose mirror, findingmodels repository
