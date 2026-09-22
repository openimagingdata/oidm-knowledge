---
type: Concept
title: SDKs
description: The tools that wrap the data structures and resolve their codes into Foundation Context, plus the libraries that help author that context.
tags: [sdks, foundation-context, findingmodel, anatomic-locations, terminologies]
status: draft
generated: { by: claude-opus-5/2026-09-22-restructure/draft-sdks, at: 2026-09-22T13:20:00Z }
stale_after: 2027-09-22
sources:
  - id: notes
    resource: Joint working notes for the restructure, docs/plans/restructure-joint-notes.md
    title: "Decisions of 2026-09-22: the five pillars, in the project lead's words"
  - id: siim
    resource: https://oidm-public.t3.tigrisfiles.io/oidm-knowledge-sources/SIIM%202026%20Reports-of-the-Future.pptx
    title: SIIM 2026 annual meeting talk, June 2026, Mass General Brigham, slides 13-15
  - id: gamma
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026, applications pillar and call to action
  - id: fm-readme
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/README.md
    title: findingmodel package README, released snapshot 2026-03-04
  - id: fm-mcp
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/docs/mcp_server.md
    title: Finding Model MCP server guide, released snapshot 2026-03-04
  - id: fm-ai
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel-ai/README.md
    title: findingmodel-ai package README, released snapshot 2026-03-04
  - id: fm-rewrite
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/canonical-structured-metadata-and-enrichment-rewrite.md
    title: Canonical Structured Metadata and Enrichment Rewrite, metadata-cleanup snapshot 2026-06-29
  - id: adr-schema
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/adr/0001-lean-metadata-docs-schema-is-spec.md
    title: Architecture decision record 0001, metadata-cleanup snapshot 2026-06-29
  - id: adr-dualdb
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/adr/0003-dual-db-pre-post-metadata-release.md
    title: Architecture decision record 0003, metadata-cleanup snapshot 2026-06-29
  - id: al-readme
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/anatomic-locations/README.md
    title: anatomic-locations package README, released snapshot 2026-03-04
  - id: bpi-ts
    resource: https://github.com/talkasab/BodyPartIndex.ts/blob/dec578e10293d722e6136802cc5dfda2599f0f45/README.md
    title: BodyPartIndex.ts README, last changed 2022-12-18
  - id: bpi-py
    resource: https://github.com/talkasab/BodyPartIndex.py/blob/388ae0a6da92f5ee4cf36620bbeeabe223938471/README.md
    title: BodyPartIndex.py README, last changed 2024-02-03
  - id: bpi-todo
    resource: https://github.com/talkasab/BodyPartIndex.py/blob/388ae0a6da92f5ee4cf36620bbeeabe223938471/TODO.md
    title: BodyPartIndex.py open work list, updated 2024-02-03
  - id: molu-readme
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/9cc3eec2c7af32e366e3f05e027b223b4a870077/README.md
    title: med-ontology-lookup README, snapshot 2026-09-18
  - id: molu-roadmap
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/9cc3eec2c7af32e366e3f05e027b223b4a870077/docs/product-roadmap.md
    title: "Product direction: an agent-ready medical terminology graph gateway, 2026-08-16"
  - id: molu-review
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/9cc3eec2c7af32e366e3f05e027b223b4a870077/docs/project-review-and-proposal.md
    title: med-ontology-lookup project review and proposal, 2026-09-03
  - id: ipl-issue
    resource: https://github.com/openimagingdata/imaging-problem-list/issues/1
    title: "imaging-problem-list issue #1, Create System of Data Models, open and unassigned as of 2026-09-22"
  - id: ipl-coding
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/coding-agent-design.md
    title: Coding Agent Design, development snapshot, document last updated 2026-03-16
---

# What an SDK is in this project

The project lead defined this pillar on 2026-09-22 as "the tools that wrap the data structures and enable developers working in the application layer to manipulate instances in real-world applications (and some around helping with definition of the foundation context, obviously)".[^notes] Some of what sits here serves developers building applications, and some serves the people and agents who author the shared definitions those applications resolve against.

The June 2026 SIIM talk gives the pillar a single shared job, under the heading "Resolve, don't reinvent": an Observation carries a code, the code is a pointer, and the pointer resolves into Foundation Context. The slide states the goal directly, "OIDM SDKs make resolution easy and standardized — every app pulls the same context the same way", and names two families of consumer. Determinative tools want "reliable, machine-readable rules" for "safety checks, protocoling, quality metrics". Generative agents want "grounding that reduces hallucination" and "a citable, shared context across apps".[^siim] The preceding slide makes the case by example: for a pulmonary nodule, an abdominal aortic aneurysm and a renal calculus, "none of it was in the patient's record — all of it came from resolving the codes, the same way for every finding".[^siim] The talk's closing ask lists three items, the third being "Build against SDKs".[^siim] That is a stated goal as of June 2026, not a description of a finished toolkit.

The definitions being resolved into are described in [Foundation Context](./foundation-context.md); the structures being wrapped are in [Data Structures](./data-structures.md).

# Capabilities that exist today

## Resolving and searching finding models

The `findingmodel` package gives a developer the finding model format as objects, with identifiers, attributes and index codes on the loaded object, and an index that resolves a name, a synonym or an identifier to a definition. It also ships a Model Context Protocol server that exposes the same index to agents as three tools: search, retrieve by identifier or name, and index statistics. Implemented example, released snapshot 2026-03-04.[^fm-readme][^fm-mcp]

Over that corpus the team separated three retrieval modes rather than overloading one. Query-driven search combines full-text and vector retrieval, with metadata filters pushed into candidate generation before ranking. Browse is filter-only with pagination, and explicitly replaces an earlier arrangement where an empty search string carried tag filters. Related-model lookup is deterministic with no language model, scoring metadata overlap with configurable weights, anatomic location weighted highest, then index codes, then entity type, then body region and the remaining facets. Filters are OR within a facet and AND across facets, while tags keep all-of semantics. The rewrite document records the weights as provisional and says they "must be tuned against a gold case set before release".[^fm-rewrite] Implemented example on the development and metadata branches, metadata-cleanup snapshot 2026-06-29; absent from the released snapshot.

## Helping author the Foundation Context

The same workspace carries the authoring half of the project lead's definition. A developer can generate a finding's basic information from its name, add detail with citations, turn a Markdown outline into a model, and create a stub model to start from. Implemented example, released snapshot 2026-03-04.[^fm-ai] The metadata rewrite adds one entrypoint for metadata assignment that returns the updated model together with a separate review artifact holding raw candidates, normalization notes and review-oriented reasoning; its design rules keep query generation, candidate gathering, normalization and fallback behaviour in code, leaving the model-facing step to classify typed input into typed output. The document records that entrypoint as implemented in the working tree it describes; working proposal, metadata-cleanup snapshot 2026-06-29.[^fm-rewrite]

Reusable authoring capability belongs here. The content itself, and the rules for reviewing it, are in [Finding models and CDEs](./finding-models-and-cdes.md); the authoring applications built on top are in [Sample Applications](./sample-applications.md).[^notes]

## The SDK's own recorded decisions

Two architecture decision records state how this SDK treats its own documentation and its own releases. They are decisions about that package, recorded by the team on its metadata-cleanup branch, and nothing about them is a project-wide rule.[^adr-schema][^adr-dualdb]

The first is titled "Metadata docs are a lean decision/policy record; the Pydantic schema is the spec". Its decision is that the metadata documents hold judgments and rules, while field types, patterns, the code object's shape and value-normalization behaviour live in the models and are read from code. The stated cause is that hand-maintained structural documents drift and produce stale content, with a prior consolidation named as the example that "lost and duplicated exactly this kind of detail". Architecture decision, metadata-cleanup snapshot 2026-06-29.[^adr-schema]

The second publishes two database artifacts built from the same enriched source commit: one in the legacy shape readable by the currently published runtime, and one metadata-aware, carrying structured-metadata columns, enriched JSON and a provenance table. The stated reason is that existing consumers keep working unchanged while metadata-aware consumers get the new data, "rather than forcing a breaking single-DB migration". Architecture decision, partly implemented, metadata-cleanup snapshot 2026-06-29.[^adr-dualdb]

## Resolving anatomic locations

The `anatomic-locations` package gives a developer lookup by identifier, description or synonym, all case-insensitive; traversal of the parent and child hierarchy; laterality variants; and hybrid full-text and semantic search, including a batch path that takes several queries in one embedding call. Implemented example, released snapshot 2026-03-04.[^al-readme] The location set itself is in [Anatomic locations](./anatomic-locations.md).

Its dated predecessors are two wrapper libraries over the 2022 anatomic location set. Both give a developer retrieval by a RadLex, SNOMED or FMA code, the containing and part-of parents of a location, a test of whether one location is contained by another, and the three-way sided arrangement in which the index holds an unsided, a left and a right version of a sided part, each aware of the others. The TypeScript library documents walks in both directions, immediate and full, for both relations; the corresponding section of the Python library's README is an empty stub. Implemented examples, last changed 2022-12-18 for the TypeScript library and 2024-02-03 for the Python one.[^bpi-ts][^bpi-py] The Python library's open work list, updated 2024-02-03, records intent never carried out there: move the repository to the openimagingdata organization, adopt the ACR Common codes, acknowledge the DICOM codes, and rework the body part as a Pydantic model.[^bpi-todo]

## Resolving terminology

`med-ontology-lookup` gives a developer one normalized interface over RadLex, SNOMED CT, FMA, LOINC and UMLS, reached through the BioPortal and UMLS Terminology Services interfaces. Its stated version 0.1 capability is free-text search across those vocabularies with results balanced per ontology "so SNOMED does not crowd out RadLex", retrieval of a concept by CUI, RadLex identifier, SNOMED code or FMA identifier, crosswalk through UMLS CUIs into other vocabularies, one-hop parents and children for hierarchy checks, semantic-type filters, auto-detection of whether an input is a term, a code or a CUI, and a portable agent skill carried in the repository. Implemented example, snapshot 2026-09-18.[^molu-readme]

Two team documents state where it should go, and they agree on the destination while differing on what comes first. The product direction of 2026-08-16 calls for "the small, dependable layer that lets people and agents resolve medical language to versioned concepts", with an explicit radiology default profile over RadLex, LOINC including the Playbook, SNOMED CT, FMA and UMLS as the CUI hub, with mapping direction, scope and provenance preserved instead of treating every cross-reference as equivalence, and with equal support for Python, structured command-line output and an agent protocol.[^molu-roadmap] The project review of 2026-09-03 calls the package "a credible alpha nucleus" that "is not ready to expand broadly", and puts hardening first: stop hiding provider failures, stop silently truncating graph-shaped responses, stop presenting ambiguous or weak mappings as unqualified crosswalks, with bounded graph operations added only after those contracts are trustworthy.[^molu-review] Working proposals, both dated. The vocabularies themselves are in [Standards](./standards.md).

# Proposed SDKs

## An Imaging Problem List SDK

Working proposal. Issue #1 on `imaging-problem-list`, "Create System of Data Models", asks for models for Observation with an Extracted Observation sub-type raised as an open question, for the Exam Finding List, and for the Imaging Problem List; written in Pydantic; with "extensive annotation to generate JSON schemas"; and with camelCase aliases in export over snake_case object attributes. The issue was open, uncommented and unassigned as of 2026-09-22, and no plan in the repositories read for this knowledgebase claims it.[^ipl-issue] The structures it would formalize are described in [Data Structures](./data-structures.md).

Its precursor is a Sample Application rather than an SDK. The report extraction, coding, persistence and review platform on the `imaging-problem-list` development branch already separates the job an SDK would expose: its coding design document, last updated 2026-03-16, states that coding "is an **independent job** — fully decoupled from extraction", that extraction output persists without codes, and that coding is triggered separately and can be re-run with different models or settings.[^ipl-coding] The platform itself is covered in [Sample Applications](./sample-applications.md).

## An Open Imaging Reporting SDK

Working proposal, named and no more. The January 2026 status update lists under its applications pillar an "Open Imaging Reporting SDK (vendor-driven innovation)", and its call to action asks for vendor-driven work, naming a reporting vendor's SDKs as the example.[^gamma] No repository, package, issue or branch for it was found in the repositories read for this knowledgebase. What such an SDK would serve is described in [Use Cases](./use-cases.md).

# Where the neighbouring pillars begin

The command-line front ends over these libraries, Finding Model Forge, the finding models catalog site, the Imaging Problem List viewers and the extraction platform are applications built on this layer, not part of it, and they are covered in [Sample Applications](./sample-applications.md). Reusable authoring capability stays here; the content those tools author, and the principles for reviewing it, are in [Finding models and CDEs](./finding-models-and-cdes.md).[^notes]

[^notes]: Joint working notes for the restructure, decisions of 2026-09-22
[^siim]: SIIM 2026 annual meeting talk, June 2026, Mass General Brigham
[^gamma]: Open Imaging Data Model 2026 Status Update, January 2026
[^fm-readme]: findingmodel package README, released snapshot 2026-03-04
[^fm-mcp]: Finding Model MCP server guide, released snapshot 2026-03-04
[^fm-ai]: findingmodel-ai package README, released snapshot 2026-03-04
[^fm-rewrite]: Canonical Structured Metadata and Enrichment Rewrite, metadata-cleanup snapshot 2026-06-29
[^adr-schema]: Architecture decision record 0001, metadata-cleanup snapshot 2026-06-29
[^adr-dualdb]: Architecture decision record 0003, metadata-cleanup snapshot 2026-06-29
[^al-readme]: anatomic-locations package README, released snapshot 2026-03-04
[^bpi-ts]: BodyPartIndex.ts README, last changed 2022-12-18
[^bpi-py]: BodyPartIndex.py README, last changed 2024-02-03
[^bpi-todo]: BodyPartIndex.py open work list, updated 2024-02-03
[^molu-readme]: med-ontology-lookup README, snapshot 2026-09-18
[^molu-roadmap]: Product direction for med-ontology-lookup, 2026-08-16
[^molu-review]: med-ontology-lookup project review and proposal, 2026-09-03
[^ipl-issue]: imaging-problem-list issue #1, Create System of Data Models
[^ipl-coding]: Coding Agent Design, imaging-problem-list development branch, updated 2026-03-16
