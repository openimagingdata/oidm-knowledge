---
type: Concept
title: Finding models and CDEs
description: One content in two collections - the common graph being drafted for both, the OIFM and RadElement formats that hold it today, what the inclusive collection contains, and the authoring and review principles behind it.
tags: [foundation-context, finding-models, cde, radelement, next-gen-schema]
status: draft
generated: { by: claude-opus-5/2026-09-22-restructure/draft-foundation, at: 2026-09-22T00:00:00Z }
sources:
  - id: joint-notes
    resource: docs/plans/restructure-joint-notes.md
    title: "Restructure joint working notes, carrying the project lead's decisions of 2026-09-22"
    last_modified: 2026-09-22
  - id: build-plan
    resource: knowledge/plans/2026-09-20-knowledgebase-build-plan.md
    title: "Knowledgebase build plan, carrying the project lead's content direction of 2026-09-21"
    last_modified: 2026-09-21
  - id: cde-00
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/00-current-understanding.md
    title: "Next-Generation CDE Schema: Current Understanding, ACR-RSNA-CDEs next-gen-2026 at 44836c1, 2026-09-15"
    last_modified: 2026-09-15
  - id: cde-01
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/01-what-the-vocabulary-must-express.md
    title: "What the Vocabulary Must Express, ACR-RSNA-CDEs next-gen-2026 at 44836c1, 2026-09-15"
    last_modified: 2026-09-15
  - id: cde-03
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/03-draft-structures.md
    title: "Draft Structures for Worked Examples, ACR-RSNA-CDEs next-gen-2026 at 44836c1, 2026-09-15"
    last_modified: 2026-09-15
  - id: cde-07
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/07-relationship-family.md
    title: "The Finding and Diagnosis Relationship Family, ACR-RSNA-CDEs next-gen-2026 at 44836c1, 2026-09-15"
    last_modified: 2026-09-15
  - id: cde-08
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/08-worked-examples.md
    title: "Worked Examples: Acute Pyelonephritis, Pleural Effusion, and One Report, ACR-RSNA-CDEs next-gen-2026 at 44836c1, 2026-09-15"
    last_modified: 2026-09-15
  - id: cde-10
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/10-decision-record-2026-09-02.md
    title: "Decision Record, 2 to 15 September 2026, ACR-RSNA-CDEs next-gen-2026 at 44836c1"
    last_modified: 2026-09-15
  - id: cde-11
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/11-anatomy-axis.md
    title: "The Anatomy Axis, Current State, ACR-RSNA-CDEs next-gen-2026 at 44836c1, 2026-09-15"
    last_modified: 2026-09-15
  - id: cde-context
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/CONTEXT.md
    title: "CDE vocabulary, CONTEXT.md, ACR-RSNA-CDEs next-gen-2026 at 44836c1, 2026-09-15"
    last_modified: 2026-09-15
  - id: cde-schema
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/cde.schema.json
    title: "cde.schema.json, the published CDE set and element schema, ACR-RSNA-CDEs at 44836c1"
    last_modified: 2026-09-15
  - id: oifm-metadata-fields
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/oifm-metadata-fields.md
    title: "Finding Model Structured Metadata Fields, ACR-RSNA-CDEs next-gen-2026 at 44836c1"
    last_modified: 2026-09-15
  - id: oifm-v2-draft
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/oifm-schema-v2-draft.md
    title: "FindingModel Source Schema v2 Draft, April 2026, copied on ACR-RSNA-CDEs next-gen-2026 at 44836c1"
    last_modified: 2026-09-15
  - id: oifm-schema
    resource: https://github.com/openimagingdata/findingmodels/blob/a30c3c95fa3943e7340ce87575f4b1b926987eb8/schema/finding_model_schema.md
    title: "Finding Model Schema, findingmodels taxonomy-export-2026-08-15 at a30c3c9"
    last_modified: 2026-08-15
  - id: ids-json
    resource: https://github.com/openimagingdata/findingmodels/blob/a30c3c95fa3943e7340ce87575f4b1b926987eb8/ids.json
    title: "ids.json, the identifier registry, findingmodels taxonomy-export-2026-08-15 at a30c3c9"
    last_modified: 2026-08-15
  - id: lists-readme
    resource: https://github.com/openimagingdata/findingmodels/blob/a30c3c95fa3943e7340ce87575f4b1b926987eb8/lists/README.md
    title: "Exam-oriented finding taxonomies README, findingmodels taxonomy-export-2026-08-15 at a30c3c9"
    last_modified: 2026-08-15
  - id: cleanup-plan
    resource: https://github.com/openimagingdata/findingmodels/blob/a30c3c95fa3943e7340ce87575f4b1b926987eb8/docs/plans/definition_cleanup.md
    title: "Definition Cleanup Plan, findingmodels taxonomy-export-2026-08-15 at a30c3c9"
    last_modified: 2026-08-15
  - id: upstream-proposals
    resource: https://github.com/openimagingdata/findingmodels/blob/a30c3c95fa3943e7340ce87575f4b1b926987eb8/docs/plans/findingmodel-upstream-proposals.md
    title: "Candidate upstream issues for the findingmodel library, findingmodels taxonomy-export-2026-08-15 at a30c3c9"
    last_modified: 2026-08-15
  - id: oifm-prompts
    resource: https://github.com/openimagingdata/findingmodels/tree/a30c3c95fa3943e7340ce87575f4b1b926987eb8/prompts/fragments
    title: "Authoring prompt fragments, findingmodels taxonomy-export-2026-08-15 at a30c3c9"
    last_modified: 2026-08-15
  - id: oifm-skills
    resource: https://github.com/openimagingdata/findingmodels/tree/a30c3c95fa3943e7340ce87575f4b1b926987eb8/.claude/skills
    title: "finding-author, finding-batch, and finding-review skill files, findingmodels taxonomy-export-2026-08-15 at a30c3c9"
    last_modified: 2026-08-15
  - id: prompt-research
    resource: https://github.com/openimagingdata/findingmodels/blob/a30c3c95fa3943e7340ce87575f4b1b926987eb8/docs/plans/prompt_length_research.md
    title: "Prompt Length and Instruction Complexity: Research and Recommendations, 2026-03-22, findingmodels at a30c3c9"
    last_modified: 2026-03-22
  - id: chestct-spec
    resource: https://github.com/openimagingdata/findingmodels/blob/0472a467/PROJECT_SPECIFICATION.md
    title: "Chest CT conversion project specification, findingmodels content/chestcts at 0472a46"
    last_modified: 2026-08-15
  - id: metadata-rewrite
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a/docs/canonical-structured-metadata-and-enrichment-rewrite.md
    title: "Canonical Structured Metadata and Enrichment Rewrite, findingmodel feature/metadata-cleanup at 1942b06"
    last_modified: 2026-06-23
  - id: metadata-fields-doc
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a/docs/metadata/subspecialties.md
    title: "Subspecialty policy and field standards, findingmodel feature/metadata-cleanup at 1942b06"
    last_modified: 2026-06-23
  - id: metadata-prompts
    resource: https://github.com/openimagingdata/findingmodel/tree/1942b06a/packages/findingmodel-ai/src/findingmodel_ai/metadata/prompts
    title: "Metadata assignment prompts, findingmodel feature/metadata-cleanup at 1942b06"
    last_modified: 2026-06-23
  - id: adr-0002
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a/docs/adr/0002-split-agent-assignment-architecture.md
    title: "ADR 0002, split agent assignment architecture, findingmodel feature/metadata-cleanup at 1942b06"
    last_modified: 2026-06-23
  - id: human-review
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a/docs/metadata/enrichment/human-review-and-writeback.md
    title: "Human review and writeback, findingmodel feature/metadata-cleanup at 1942b06"
    last_modified: 2026-06-23
  - id: staging-readme
    resource: https://github.com/openimagingdata/CDEStaging/blob/b814a102655054ac08b3c118cb1977a387655a8b/README.md
    title: "CDEStaging README at b814a10"
    last_modified: 2025-12-01
  - id: staging-extraction
    resource: https://github.com/openimagingdata/CDEStaging/blob/b814a102655054ac08b3c118cb1977a387655a8b/docs/report_extraction_process.md
    title: "Report extraction process, CDEStaging at b814a10"
    last_modified: 2025-12-01
  - id: staging-catalogs
    resource: https://github.com/openimagingdata/CDEStaging/tree/b814a102655054ac08b3c118cb1977a387655a8b/report_representation
    title: "Negative statements, uncovered findings, and missing attributes catalogs, CDEStaging at b814a10"
    last_modified: 2025-12-01
  - id: board-role-tagging
    resource: internal project board, not published
    title: "Open Imaging Data Model project board (internal), undated; schema idea only"
  - id: status-deck-2026-01
    resource: sources/gamma-2026-status-update.md
    title: "Open Imaging Data Model 2026 Status Update, January 2026, extract"
    last_modified: 2026-01-01
  - id: ipl-webinar
    resource: sources/bucket/text/ipl-webinar-deck.md
    title: "The Imaging Problem List as an Accelerator for Radiology AI Applications, SIIM Enterprise Imaging webinar, 15 July 2026"
    last_modified: 2026-07-15
---

# The project's position

The project lead ruled on 2026-09-22, in the working notes both drafting sessions share:

> "A 'CDE' and a 'Finding Model' are the same thing, but they're in different repos. Open Imaging Finding Models are in the OIDM-maintained repo, and are intended to be very INCLUSIVE, can almost be drafts. Common Data Elements live in the ACR/RSNA repository, and are intended to be WELL-REVIEWED. They're more like something published. They BOTH should soon be using the schema and classes being defined in the CDE schema re-write, with FindingClass, DataElement, Measurement, etc."[^joint-notes]

And, in the same set of decisions:

> "OIFMs VERY soon need to get re-organized around the graph-based approach we're developing in the next-gen-schema effort in CDEs. They're currently document-oriented and we need to fix that SOON."[^joint-notes]

The common model is explained once here. Inclusive and well-reviewed describe *collections*, not items: nothing here says a given [finding model](../glossary/finding-model.md) is a draft, or a given [CDE set](../glossary/cde-set.md) well reviewed. Both the shared schema and the reorganization are stated intent, the latter a change of organization rather than added fields, and no migration is done.

# The common graph

Both collections are meant to converge on the next-generation CDE vocabulary on the `next-gen-2026` branch of `ACR-RSNA-CDEs`, at commit `44836c1` of 2026-09-15. These structures "capture our working ideas and prototype choices, not a settled model."[^cde-03] The branch's decision record marks provenance; two labels are carried here. **OWNER**: the project lead stated it, quoted verbatim. **CLAUDE DEFAULT**: an assistant chose it, unreviewed.[^cde-10]

## Node types

| Node type | What it is, and its status in the source |
|---|---|
| [FindingClass](../glossary/finding-class.md) | the named thing a report describes, carrying an `entity_type`; working proposal, exercised as graph data |
| Diagnosis | a separate node type (external reviewer, 2026-08-25); only which relationships it can source distinguishes it |
| Grouping | negative-only nodes such as `renal abnormality`, parenting findings and diagnoses; OWNER inclination |
| [DataElement](../glossary/data-element.md) | a categorical descriptor with an explicitly ordered or unordered value set |
| [Measurement](../glossary/measurement.md) | a quantitative descriptor with quantity type, units, optional method; a distinct type (OWNER) |
| [AssessmentScheme](../glossary/assessment-scheme.md) | a scheme whose dimensions are linked DataElements (OWNER) |

Values are first-class, their ids derived from their element; [anatomic locations](../glossary/anatomic-location.md) are keyed by RadLex identity; standard clinical metadata values are shared concept nodes, not free text (OWNER).[^cde-03][^cde-10]

## Edges are the content

The draft heads its edge section "Edges — the actual content of the model."[^cde-03] An [element binding](../glossary/element-binding.md) runs from a FindingClass, or directly from an AnatomicLocation, to a DataElement, and may restrict that use to a subset of the element's values without changing the shared element (OWNER), a restriction on meaning rather than presentation. There are no required elements: OWNER, "THERE IS NO SUCH THING AS A REQUIRED ELEMENT."[^cde-10] Reuse is in-degree; and a location binding elements directly (OWNER) lets normal anatomy be described with no FindingClass.[^cde-03][^cde-01]

An Open Imaging Data Model project board approaches reuse from the consuming side, proposing **role tagging**: tag each element definition with a standard SNOMED or RadLex code naming its role or purpose — presence, location, size and its several measures such as diameters, volumes and segmentation data, modality-specific measures such as radiodensity, echogenicity and MR signal, and contrast behavior — so a consuming system can find the right element across CDE sets by role, looking up the element carrying the SNOMED code for volume measurement instead of hard-coding set-specific element identifiers. A working proposal, undated, no implementation cited.[^board-role-tagging] The next-generation graph reaches reuse by another route, one shared DataElement node bound by many classes;[^cde-03] no source says the two were coordinated.

## Anatomic scope, not location

**Anatomic scope** is the project lead's agreed term of 2026-09-10 for "the statement of where a kind of finding belongs, which may be a place (kidney) or a kind of structure (muscle, not otherwise specified)."[^cde-10][^cde-context] "Location" is the wrong word, the requirements document argues, because the statement ranges over three kinds of thing and only two are spatial: a named structure checked by identity or descent, a region checked by containment, and a structure type such as tendons checked taxonomically, "not spatial at all." Its strength varies too.[^cde-01] A class is scoped to the unsided organ while a specific [Observation](../glossary/observation.md) sits in a sided one, the is-a relation satisfying the scope (OWNER).[^cde-10] Two scope families, tissue types and structure types, are to be developed (OWNER); the taxonomic kind waits on an is-a relation the data lacks.[^cde-11]

## The relationship family and the derived differential

A catalog called "tentative, explicitly non-comprehensive" proposes seven relationship pairs plus a catch-all: subtype, component, causation, manifestation, co-occurrence, progression, assessment. Manifestation and causation stay strictly apart — a striated nephrogram *is* pyelonephritis appearing on imaging, while a renal abscess is a second entity it produced — tested by whether a clinician would say the source "got better" or "a complication resolved." Manifestation edges take two optional properties: a typicality scale adopted verbatim from the HPO and Orphanet frequency scale, and a three-value specificity scale omitted when uninformative, an absent property meaning no judgment was recorded. The differential is a derived view, not an edge type: the diagnoses reachable over the manifestation inverse, on the Radiology Gamuts Ontology's precedent.[^cde-07] Whether the causal pair takes typicality is a CLAUDE DEFAULT; an `expected` property on causal edges, a CLAUDE INVENTION.[^cde-10][^cde-08]

The finding-model side proposes the same mechanism differently: an April 2026 source-schema draft has a model store only the assertions authored on it, tooling deriving the inverse and symmetric views from a registry of relationship types.[^oifm-v2-draft] Verified on 2026-09-01, that registry exists only in the draft and the live corpus "implements no relationship mechanism at all."[^cde-07]

## Assessments, components, and measurements

A scoring system is a valid definition but a different one from what it scores: a nodule model captures what the nodule looks like and a Lung-RADS model the risk category, because different radiologists can describe the same nodule identically and assign different categories.[^oifm-prompts] That is an `assessment` value in the metadata entity-type enumeration today;[^metadata-prompts] in the next-generation design it is its own definition type with edges to ordinary DataElements (OWNER).[^cde-10][^cde-07]

An independence test separates components from associated findings. An **associated finding** has its own lifecycle — pneumonia and pleural effusion each occur alone — and is one multichoice attribute, presence-level only, its values naming real finding models. A **component** is an intrinsic part, such as the solid component of a mixed pulmonary nodule, extracted into its own model.[^oifm-prompts] The chest CT content branch forbids an associated-findings attribute outright, contradicting that rule.[^chestct-spec] The next-generation design moved twice: one component relationship carrying counts, with the terms **component-of scope** and **lesion family** (OWNER, September 2026), then on 2026-09-16 withdrawn for the external reviewer's two edges.[^cde-10][^cde-context]

Measurement, method, and interpretation are three things. "Peak systolic velocity is 350 cm/s" and "this represents hemodynamically significant stenosis" have different truth conditions, and the reason given for separating them is durability: thresholds move while measurands do not, so a stored interpretation becomes wrong when criteria are revised. Confidence belongs to the interpretation, and measurements must stand alone.[^cde-01][^cde-10]

## What the graph should carry for a finding

Three sources say what a definition carries beyond its elements:

| Source, dated | What it says |
|---|---|
| Next-generation vocabulary, OWNER term of 2026-09-10 | **Standard clinical metadata**, seven facts on a class: modality, body region, subspecialty, sex, age, time course, etiology — edges to shared concept nodes, three of them RadLex nodes and the rest on provisional codes (OWNER)[^cde-10][^cde-03] |
| SIIM Enterprise Imaging webinar, 15 July 2026 | Four dimensions that let an agent judge whether a finding *should still be there* on a new exam: where it is anatomically, what type it is, how long it lasts, whether it is transient or permanent — "the forward, AI-populated schema, not yet carried by the published definitions"[^ipl-webinar] |
| Metadata rewrite in `findingmodel`, metadata branch | Eight optional fields — body regions, subspecialties, etiologies, entity type, applicable modalities, expected time course, age profile, sex specificity — typed on the model classes, making metadata "canonical `FindingModel` state rather than disposable enrichment output"[^metadata-rewrite] |

# The two collections today

## The two formats

A finding model is one JSON document: identifier, name, description, and attributes, plus optional synonyms, tags, contributors, and index codes. An attribute is either a choice attribute, whose values each carry their own code, or a numeric attribute with bounds and a unit.[^oifm-schema] Identifiers carry provenance — `OIFM_{ORG}_{six digits}` for a model, `OIFMA_{ORG}_{six digits}` for an attribute — the middle segment naming the contributing organization, so institutions mint independently.[^oifm-metadata-fields][^ids-json] The published [CDE set](../glossary/cde-set.md) is the corresponding container: an `RDES` identifier, descriptive and governance fields, and its elements; a [CDE element](../glossary/cde-element.md) carries an `RDE` identifier, its parent set, a definition and question, and either an enumerated value set or a numeric range.[^cde-schema]

The published finding model is lean: the eight metadata fields above are typed on the development and metadata branches and absent from the released one, whose readiness assessment is recorded as not yet passing.[^metadata-rewrite] They are specified by the near-miss they exclude: subspecialty is which service would *read and report* the finding, not which orders the study; expected time course is how long a finding stays visible on imaging, "not the clinical duration of the underlying disease."[^metadata-fields-doc] An [index code](../glossary/index-code.md) must be an exact match or clinically substitutable near-equivalent for the whole model concept — policy carried by prompts and review, enforced nowhere at runtime.[^metadata-rewrite]

## How they correspond

By design: a finding model to a CDE set, an attribute to an element, choice values to a value set, index codes the join. In practice it runs one way. 115 of 2,382 finding models carry the `CDE` organization code, with a contributor record naming the ACR/RSNA project and a RadElement index code pointing at their set.[^ids-json]

The January 2026 status deck calls this "OIFM: the CDE workbench," a proving ground whose exploratory metadata "can graduate to standards."[^status-deck-2026-01] The CDE branch states the other half: the finding model effort "is roughly one iteration ahead," its models "can be treated as drafts for this project's FindingClasses," and bringing them over "is a review step, not a bulk import." How the crossover works is open between a shared identity space and a maintained crosswalk, and the document chooses neither.[^cde-00]

Coverage is measured by running real reports against the definitions. The staging repository calls itself "a staging area for definitions ... prior to their entering the review pipeline," and its extraction note works one report into mini-observations.[^staging-readme][^staging-extraction] Three catalogs record what the definitions could not carry — composite negative statements, uncovered findings, missing attributes — dated 2024 to 2025, with no recorded disposition.[^staging-catalogs]

# What the inclusive collection holds, and where it is going

The corpus merges uneven provenance streams. From the identifier registry, 2,382 models come from five sources: 1,933 derived from the Radiology Gamuts Ontology, 256 authored by the project, 115 from ACR and RSNA common data elements, 47 from an institutional contributor, 31 from a vendor.[^ids-json] The cleanup plan traces nine mechanical defect classes to specific streams and notes that some Gamuts-derived entries are differential patterns, not findings.[^cleanup-plan]

The **MGB exam-oriented sub-taxonomies** are the immediate content direction: six per-exam-context finding hierarchies — chest radiograph, musculoskeletal radiograph, head CT, chest/abdomen/pelvis CT, mammography, spine MRI — 3,789 rows, each naming its parent, with "Parents are generic, children add specificity," and an anatomic category as an independent grouping. They double as a coverage ledger: an identifier is filled only where a row matched an existing model by exact name, and "Nothing was minted here." 1,028 rows matched, unevenly — 305 of 403 for chest radiographs against 5 of 198 for mammography — and "Blank rows are the ones needing triage."[^lists-readme] The project lead stated on 2026-09-21: "the immediate direction for all of the content, probably replacing a lot of the Gamuts-based models."[^build-plan] Converting an outside set is a merge with a fixed direction, incoming definitions merging into the corpus and never the reverse, guarded against matching a specific incoming term to a general model; six of twenty-one chunks are converted.[^chestct-spec] The content effort also feeds requirements upstream, a proposals document sizing each entry to one issue on an evidence base of a fourteen-model test batch and a review pass.[^upstream-proposals]

# Authoring and review

Operational definitions live in prompt fragments and skill files.[^oifm-prompts][^oifm-skills]

| Principle | What the sources say |
|---|---|
| What counts as a finding | Would a radiologist write "there is [X]" or "no [X]" as a standalone statement? Devices, postsurgical states, variants and diagnoses count; a state of a finding, a qualified version of another, normal anatomy and radiographic signs do not. |
| Description and diagnosis both count | "Do not question whether a diagnosis 'should' be a finding." Three representations coexist: a `finding_type` column,[^lists-readme] an `entity_type` enumeration,[^metadata-prompts] and a separate Diagnosis node type whose taxonomy rule moved twice (OWNER, September 2026).[^cde-10] |
| Specificity and splitting | Compound names split when one part can be present without the other; a subtype earns its own model when it needs different attributes, so "tension pneumothorax" is not a value on pneumothorax. |
| Negative assertion, presence, change | Broad scoped findings exist so absence can be asserted against something, scoped by what the exam assesses; presence and change from prior are every model's first two attributes. |
| Synonyms | Collection is aggressive, but each must mean the same thing at the same level of specificity: "a bad synonym doesn't just fail to match — it matches the *wrong thing*." |
| Naming | Lowercase with spaces, acronyms expanded and kept as synonyms, eponyms minimized, brand names replaced, and a real anatomic anchor. |
| Stubs, then iteration | Names come from an ontology, from experts, and from a model reading report text; each becomes a stub, gets an identifier at once, and is improved later. |
| Triage before create | Two or three complementary searches run per candidate; the agent judges the pooled results and reports an exact match, no match, or true ambiguity. "Do not forward raw result lists to the user." |
| Review in three tiers, with context isolation | A deterministic linter, then a language-model review applying a checklist the linter deliberately does not attempt, then mandatory human sign-off, with "each finding drafted and reviewed by a fresh sub-agent with no exposure to its neighbors."[^oifm-skills] |
| Prompts as loadable fragments | Skill files are "pure orchestration," and the sizing is measured: instruction-following degrades as instructions accumulate, and prompt middles get less attention than either end. The team read its own review agent as "deep in degradation territory."[^prompt-research] |
| Focused assignment | Seven narrow agents assign metadata under an orchestrator that never decides a field value; search agents propose, assignment agents dispose. A final pass audits rather than enforces, and null is legitimate.[^adr-0002] |
| Human review is the only authority | Only approved records are written back; sub-agent triage is not authority, and generated diffs are not gold.[^human-review] |

[^joint-notes]: Restructure joint working notes, the project lead's decisions of 2026-09-22
[^build-plan]: Knowledgebase build plan, the project lead's content direction of 2026-09-21
[^cde-00]: Next-Generation CDE Schema: Current Understanding, ACR-RSNA-CDEs next-gen-2026 at 44836c1
[^cde-01]: What the Vocabulary Must Express, ACR-RSNA-CDEs next-gen-2026 at 44836c1
[^cde-03]: Draft Structures for Worked Examples, ACR-RSNA-CDEs next-gen-2026 at 44836c1
[^cde-07]: The Finding and Diagnosis Relationship Family, ACR-RSNA-CDEs next-gen-2026 at 44836c1
[^cde-08]: Worked Examples, ACR-RSNA-CDEs next-gen-2026 at 44836c1
[^cde-10]: Decision Record, 2 to 15 September 2026, ACR-RSNA-CDEs next-gen-2026 at 44836c1
[^cde-11]: The Anatomy Axis, Current State, ACR-RSNA-CDEs next-gen-2026 at 44836c1
[^cde-context]: CDE vocabulary, CONTEXT.md, ACR-RSNA-CDEs next-gen-2026 at 44836c1
[^cde-schema]: cde.schema.json, ACR-RSNA-CDEs at 44836c1
[^oifm-metadata-fields]: Finding Model Structured Metadata Fields, ACR-RSNA-CDEs next-gen-2026 at 44836c1
[^oifm-v2-draft]: FindingModel Source Schema v2 Draft, April 2026, copied on ACR-RSNA-CDEs next-gen-2026 at 44836c1
[^oifm-schema]: Finding Model Schema, findingmodels taxonomy-export-2026-08-15 at a30c3c9
[^ids-json]: ids.json, findingmodels taxonomy-export-2026-08-15 at a30c3c9
[^lists-readme]: Exam-oriented finding taxonomies README, findingmodels taxonomy-export-2026-08-15 at a30c3c9
[^cleanup-plan]: Definition Cleanup Plan, findingmodels taxonomy-export-2026-08-15 at a30c3c9
[^upstream-proposals]: Candidate upstream issues for the findingmodel library, findingmodels at a30c3c9
[^oifm-prompts]: Authoring prompt fragments, findingmodels taxonomy-export-2026-08-15 at a30c3c9
[^oifm-skills]: finding-author, finding-batch, and finding-review skill files, findingmodels at a30c3c9
[^prompt-research]: Prompt Length and Instruction Complexity, 2026-03-22, findingmodels at a30c3c9
[^chestct-spec]: Chest CT conversion project specification, findingmodels content/chestcts at 0472a46
[^metadata-rewrite]: Canonical Structured Metadata and Enrichment Rewrite, findingmodel feature/metadata-cleanup at 1942b06
[^metadata-fields-doc]: Subspecialty policy and field standards, findingmodel feature/metadata-cleanup at 1942b06
[^metadata-prompts]: Metadata assignment prompts, findingmodel feature/metadata-cleanup at 1942b06
[^adr-0002]: ADR 0002, split agent assignment architecture, findingmodel feature/metadata-cleanup at 1942b06
[^human-review]: Human review and writeback, findingmodel feature/metadata-cleanup at 1942b06
[^staging-readme]: CDEStaging README at b814a10
[^staging-extraction]: Report extraction process, CDEStaging at b814a10
[^staging-catalogs]: Negative statements, uncovered findings, and missing attributes catalogs, CDEStaging at b814a10
[^board-role-tagging]: Open Imaging Data Model project board (internal), undated; schema idea only
[^status-deck-2026-01]: Open Imaging Data Model 2026 Status Update, January 2026
[^ipl-webinar]: SIIM Enterprise Imaging webinar, 15 July 2026
