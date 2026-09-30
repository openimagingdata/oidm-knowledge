---
type: Overview
title: Finding Models and Common Data Elements
description: "Definitions of findings and diagnoses as the anchor for everything the project knows about them, held in two cross-linked collections: the beta channel and the release channel."
tags: [foundation-context, finding-models, cdes, radelement, next-gen-schema]
status: draft
generated: { by: claude-opus-5/2026-09-29-restructure/hub-page, at: 2026-09-29T21:32:33Z }
sources:
  - id: lead-hub
    resource: docs/plans/2026-09-22-layout-plan.md
    title: The project lead's statements of 2026-09-23 to 2026-09-29 on this page - the anchor idea, the two collections, the beta and release channels, the cross-links, document-oriented today, and one next-generation schema for both (recorded verbatim in the layout plan)
    last_modified: 2026-09-29
  - id: lead-2026-09-22
    resource: docs/plans/restructure-joint-notes.md
    title: The project lead's decisions of 2026-09-22 - a common data element and a finding model are the same content, the inclusive collection and the well-reviewed collection, and the urgent move off document orientation (quoted in the restructure joint notes)
    last_modified: 2026-09-22
  - id: build-plan
    resource: knowledge/plans/2026-09-20-knowledgebase-build-plan.md
    title: Knowledgebase build plan, carrying the project lead's content direction of 2026-09-21 on the exam-oriented sub-taxonomies
    last_modified: 2026-09-21
  - id: oifm-repo
    resource: https://github.com/openimagingdata/findingmodels/tree/4475ac1bcb591f1a0951b2082b59208def173a5d
    title: "Open Imaging Finding Models repository, main at 4475ac1 (snapshot of 2026-04-28): the README, the schema (schema/finding_model.schema.json and the explanatory schema/finding_model_schema.md), the 2,382 per-definition files under defs/, and ids.json (2,382 definitions across five organization segments, 115 of them under the CDE code)"
    last_modified: 2026-04-28
  - id: oifm-authoring
    resource: https://github.com/openimagingdata/findingmodels/tree/4475ac1bcb591f1a0951b2082b59208def173a5d/scripts/finding_authoring
    title: "The finding model authoring scripts and prompt fragments, findingmodels main at 4475ac1: create_model.py, which builds a stub with standard attributes, identifiers and codes, and prompts/fragments/enrichment.md, the optional later enrichment step applied through fix_stub.py"
    last_modified: 2026-04-20
  - id: oifm-cde-def
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/defs/acute_aortic_syndrome.fm.json
    title: "Acute Aortic Syndrome, OIFM_CDE_000126: a finding model derived from a Common Data Element, credited to the ACR/RSNA Common Data Elements Project and carrying its RadElement identity as an index code (findingmodels main at 4475ac1)"
    last_modified: 2025-11-17
  - id: oifm-taxonomies
    resource: https://github.com/openimagingdata/findingmodels/blob/a30c3c95fa3943e7340ce87575f4b1b926987eb8/lists/README.md
    title: The six per-exam finding taxonomies and their coverage ledger, findingmodels taxonomy-export-2026-08-15 at a30c3c9, exported 2026-08-15
    last_modified: 2026-08-15
  - id: radelement
    resource: https://radelement.org
    title: The published ACR/RSNA Common Data Element collection and its public API, whose sets are attributed to the American College of Radiology and the Radiological Society of North America
  - id: cde-nextgen
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/b541b74c22a33b64834309244569a60d06de79e4/docs/next-gen-schema/00-current-understanding.md
    title: "Next-Generation CDE Schema: Current Understanding, ACR-RSNA-CDEs next-gen-2026 at b541b74 - the graph as the internal representation, the finding models as drafts for FindingClasses, and bringing them over as a review step"
  - id: cde-schema
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/b541b74c22a33b64834309244569a60d06de79e4/cde.schema.json
    title: The current Common Data Element schema, ACR-RSNA-CDEs next-gen-2026 at b541b74 - a JSON Schema whose root is a nested element_set document
    last_modified: 2024-11-19
  - id: cde-staging
    resource: https://github.com/openimagingdata/CDEStaging/tree/b814a102655054ac08b3c118cb1977a387655a8b
    title: "CDE staging repository, main at b814a10: the staging area ahead of the review pipeline, the manual report extraction process, and the three gap catalogs recording what real report language could not be represented"
  - id: status-2026-01
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: "Open Imaging Data Model 2026 Status Update: Realizing Object-Oriented Imaging Results, January 2026 - \"OIFM: the CDE workbench\" and the workbench effect"
  - id: siim-2026
    resource: https://oidm-public.t3.tigrisfiles.io/oidm-knowledge-sources/SIIM%202026%20Reports-of-the-Future.pptx
    title: Structured Results and Context for Next-Generation Imaging Resulting Tools, SIIM 2026 annual meeting talk, June 2026, Mass General Brigham - slide 9 notes on the high-velocity workbench
    last_modified: 2026-06-11
---

# Finding Models and Common Data Elements

Definitions of findings and diagnoses anchor these concepts in a form that associated content can be attached to: a name and synonyms, a definition, the attributes that characterize it, the anatomy it applies to, the modalities that show it, its codes in outside terminologies, and its relationships to other definitions.[^lead-hub][^oifm-repo][^cde-nextgen] Everything the project knows about a kind of finding hangs off this one anchor.[^lead-hub] The project holds these definitions in two collections, and they are the same kind of content.[^lead-2026-09-22]

**Open Imaging Finding Models** are an inclusive collection, maintained by the OIDM project.[^lead-hub][^oifm-repo] The OIFM repository is intended for rapid, community-based prototyping and iteration based on an open-source model, with changes proposed by anyone.[^lead-hub] A definition can start as little more than a name and a stub and be improved over time.[^lead-2026-09-22][^oifm-authoring] The collection holds a few thousand definitions today, drawn from several sources, and is being reorganized around exam-oriented taxonomies of the findings that actually appear in reports.[^oifm-repo][^build-plan][^oifm-taxonomies]

**ACR/RSNA Common Data Elements** are the well-reviewed collection, maintained by the American College of Radiology and the Radiological Society of North America and published through radelement.org.[^lead-hub][^radelement] Entry is a review step, and the project treats the finding models as the workbench where definitions are proved out before that review.[^cde-nextgen][^cde-staging][^status-2026-01][^siim-2026]

**The relationship.** The two collections describe the same ideas and will share the same schema.[^lead-hub][^lead-2026-09-22] The difference is how they are released: finding models are the beta channel, with rapid additions and updates; Common Data Elements are the release channel, reviewed and stable.[^lead-hub] The two are cross-linked and stay that way: when a definition migrates into the CDEs, it continues to be maintained in the OIFM repository and carries a reference to its CDE identity, so an application can resolve either one to the same concept.[^lead-hub][^oifm-cde-def] About a hundred finding models were derived directly from CDEs.[^oifm-repo][^oifm-cde-def] Coverage is measured the same way on both sides, by running real reports against the definitions and recording what they could not represent.[^lead-hub][^cde-staging]

**Where both are going.** The ACR/RSNA CDE project is developing a next-generation, graph-based schema, and both collections are intended to move onto it, so that applications use them together.[^cde-nextgen][^lead-hub] Both CDEs and OIFMs are document-oriented today, and moving them onto that graph is an immediate priority.[^lead-hub][^lead-2026-09-22][^oifm-repo][^cde-schema][^cde-nextgen]

# In this section

- OIFM content: what the inclusive collection holds and where it is going
- Definition formats: what a finding model and a CDE look like today
- Identifiers: the OIFM scheme, RadElement identifiers, and index codes
- The next-generation schema, with relationships and standard clinical metadata
- Authoring and review

[^lead-hub]: The project lead, 2026-09-23 to 2026-09-29, recorded verbatim in the layout plan: the finding/diagnosis definition as "an unified anchor for the CONCEPT of a finding/diagnosis in a form that can be used to attach associated context: name, synonyms, definition, attributes, etc."; the inclusive collection "maintained by the OIDM project" and "intended for rapid, community-based prototyping and iteration based on an open-source model ... with changes proposed by anyone"; the well-reviewed collection "published through radelement.org"; "they will have the same schema and describe the same ideas", with OIFMs as "beta"/rapid additions and updates and CDEs as "release"/reviewed and stable; the maintained cross-links, where a definition that migrates "will continue to be maintained in the OIFM repo but have a reference to its CDE identity"; "Both CDEs and OIFMs are document-oriented today"; and, on 2026-09-23, one next-generation schema "which will be for BOTH CDEs and OIFMs--I think applications will be able to use both at once".
[^lead-2026-09-22]: The project lead, 2026-09-22, quoted in the restructure joint notes: "A 'CDE' and a 'Finding Model' are the same thing, but they're in different repos", the OIDM-maintained collection "intended to be very INCLUSIVE, can almost be drafts" against the ACR/RSNA collection "intended to be WELL-REVIEWED ... more like something published", both to use the classes being defined in the CDE schema rewrite, and "OIFMs VERY soon need to get re-organized around the graph-based approach ... They're currently document-oriented and we need to fix that SOON."
[^build-plan]: Knowledgebase build plan: the project lead's content direction of 2026-09-21, that the taxonomy branch in the finding models repository is "the immediate direction for all of the content, probably replacing a lot of the Gamuts-based models".
[^oifm-repo]: Open Imaging Finding Models repository, main at 4475ac1, a snapshot of 2026-04-28. The README describes finding models as updatable data models defining open, standard semantic tags for imaging findings and their properties, with relationships to other ontologies; the schema document gives the definition fields (identifier, name, description, synonyms, tags, contributors, attributes, index codes into standard ontologies); `ids.json` holds 2,382 definitions across five organization segments (1,933 GMTS, 256 OIDM, 115 CDE, 47 MGB, 31 MSFT) and 5,709 attribute identifiers. The 115 under the CDE segment are the models derived from Common Data Elements. The January 2026 status update gives the collection as "nearly 3,000". For the document orientation of the collection today: the schema is a JSON Schema for a single self-contained finding model, and the corpus is 2,382 individual files under `defs/`, one per definition.
[^oifm-authoring]: The finding model authoring scripts and prompt fragments, findingmodels main at 4475ac1. `scripts/finding_authoring/create_model.py` creates "a complete finding model stub with IDs and codes", building it from a name and a description with the two standard attributes, then minting identifiers against the index; the single-model path requires a description, so a stub is not name-only. `prompts/fragments/enrichment.md` is the optional later step: it applies where "The existing description is a one-line placeholder and you want a clinically-grounded starting point", drafts a richer description with citations, and writes the reviewed result back through `fix_stub.py`, after which the normal review flow runs again.
[^oifm-cde-def]: Acute Aortic Syndrome, `defs/acute_aortic_syndrome.fm.json` at findingmodels main 4475ac1: `oifm_id` `OIFM_CDE_000126`, contributor "ACR/RSNA Common Data Elements Project", and an index code `system: RADELEMENT`, `code: RDES126` beside its RadLex code. All 115 definitions under the CDE organization segment carry a RadElement index code in the same way. This supports the retained CDE identity and the derivation of those models from Common Data Elements. It is evidence of the reference as it exists today in the direction CDE to finding model; the commitment to maintain the cross-links after a future migration, and to resolution of either identity to the same concept by an application, rests on the project lead's direction.
[^oifm-taxonomies]: The six per-exam finding taxonomies, findingmodels taxonomy-export-2026-08-15 at a30c3c9: chest radiograph, musculoskeletal radiograph, head CT, chest/abdomen/pelvis CT, mammography, and spine MRI, 3,789 rows in all. Each file is one hierarchy in which "Parents are generic, children add specificity", and `finding_type` separates an observation from a diagnosis. The files double as a coverage ledger: an identifier is filled only where a row matched a model that already exists, 1,028 of 3,789 rows, and "Blank rows are the ones needing triage."
[^radelement]: The published ACR/RSNA Common Data Element collection at radelement.org. Its public API returns sets attributed to the American College of Radiology and the Radiological Society of North America. The staging repository and the next-generation schema baseline both name it as the joint ACR/RSNA project's published corpus, public API, and vendor-facing interface.
[^cde-nextgen]: "Next-Generation CDE Schema: Current Understanding", ACR-RSNA-CDEs next-gen-2026 at b541b74, a draft for discussion dated 2026-08-19. §2.2: "The authoritative internal representation is a knowledge graph, not a document tree", following the committee's own move to "a graph model, where findings point to canonical attribute objects". §5.1: the finding model work "has independently built much of this and is roughly one iteration ahead", so "OIFMs can be treated as drafts for this project's FindingClasses", with the caveat that "Bringing models over is a review step, not a bulk import"; its table of what the finding models already answer includes worked metadata vocabularies for body regions, modalities, etiologies, sex specificity, age profile, and expected time course. Modality applicability is a field of the current CDE schema as well. §5.1 also discusses the finding models' file-based design directly, noting that it "makes choices that a graph makes differently".
[^cde-schema]: The current Common Data Element schema, `cde.schema.json` at ACR-RSNA-CDEs next-gen-2026 b541b74, last changed 2024-11-19: a draft-07 JSON Schema whose root is `element_set`, a nested document whose required properties include an `elements` array. This is the document form the collection takes today.
[^cde-staging]: CDE staging repository, main at b814a10: "a staging area for definitions of radiology common data elements in JSON format ... prior to their entering the review pipeline". The manual extraction process works one real pulmonary angiogram report into a list of mini-observations, each a finding with a presence value and its attributes. Three catalogs beside it record what the definitions could not carry. `negative_statements.md` groups real report sentences by body region that assert absence across several structures at once, some bundled with a technique caveat, with no definition links. `uncovered_findings.md` lists findings with their reported attributes and no definition behind them, also with no links. `missing_attributes.md` is the one that links: ten entries, each naming the finding and the attribute the report used and pointing at the definition file that lacked it. The catalogs exist as data; the method is described but not automated, and the same coverage question is asked prospectively as a frequency-and-priority table in the chest CT roadmap. This is evidence of the CDE-side measurement only; that coverage is measured the same way on the finding models side rests on the project lead's direction.
[^status-2026-01]: Open Imaging Data Model 2026 Status Update, January 2026: "OIFM: the CDE workbench" - rapid innovation and a proving ground before ACR/RSNA CDE adoption, with exploratory metadata "that can graduate to standards", named in the executive summary as the "workbench effect". Read from the project's transcription of the deck, `sources/gamma-2026-status-update.md`, which records the original presentation URL and the month but no modification date.
[^siim-2026]: SIIM 2026 annual meeting talk, June 2026, Mass General Brigham, slide 9 notes: "OIFM Finding Models today, ACR/RSNA CDEs next ... OIFM is the high-velocity 'workbench' that proves out content before formal CDE adoption." Read from the project's text extraction of the deck, `sources/bucket/text/siim2026-reports-of-the-future.md`; the presentation file records a modification date of 2026-06-11.
