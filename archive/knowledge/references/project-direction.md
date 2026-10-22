---
type: Reference
title: Project direction and source-review record
description: Dated project-lead guidance and the source-review snapshot retained from the original planning records.
tags: [provenance, project-direction]
status: draft
generated: { by: codex/gpt-6, at: 2026-10-02T21:35:54Z }
sources:
  - id: owner-sessions
    resource: scope:project-lead-planning-sessions-2026-09-20-through-2026-10-02
    title: Project-lead statements recorded in the original build, layout, and layer plans
  - id: original-records
    resource: https://github.com/openimagingdata/oidm-knowledge/tree/7f5e816aae6defedf675ba0cd517fbe3219cab41/docs/plans
    title: Planning records before consolidation
---

# Project direction and source-review record

This reference preserves evidence cited by the knowledge pages. It is not an execution plan. Dates identify when a statement was recorded; source-review observations are historical and require rechecking before claims of current implementation. The single implementation plan is maintained outside the bundle in `docs/plans/implementation.md`.

Later decisions govern current work. The October pipeline retains the knowledge bundle separately from presentation pages. The October 2 clarification makes the bundle repository-only, superseding the proposed internal website. The old page-replacement instructions, page budgets, agent assignments, and deployment instructions are retired.

## The project lead's stated goals, September 20–21

Recorded verbatim from the 2026-09-20 request that started this work, so that documents citing `scope:grilling-session-2026-09-20` have a written source. Only spelling was normalized.

- **Open Imaging Finding Models.** "Definition formats, needs overhaul for increased metadata and interesting relationship/graph work coming from CDEs." "Tooling for working with these, using them, probably needs corresponding overhaul." "Actual content efforts."
- **ACR/RSNA Common Data Elements.** "Should dovetail with the OIFM work."
- **FindingModelForge.** "An authoring tool for creating OIFMs / CDEs."
- **Imaging Problem List.** "A format for representing a patient's imaging history." "Define appropriate data structures for representing both observations in radiology reports and their relationships." "Manage them (and appropriately collate them) across the patient's imaging history." "Design interesting applications that use this tool and demonstrate how this works." "Create standard data structure formats, etc. for working with these."
- **Anatomic Locations.** "There are repos, and this will be blended in with RadLex." "Also needs tooling for people working with them."
- **Exam types.** "Needs wrapper tooling around the knowledge graph represented by RadLex LOINC playbook." "Need to define the PREFERRED high-level entries like 'CT Chest', 'MRI Brain', 'X-ray Knee'." "Need to TIGHTLY wrap up with Anatomic Locations, including edges for both 'always included' (which can include hierarchies) as well as 'usually included' (for edge things) and something like 'POSSIBLY included, would have to check'."
- **Content direction (2026-09-21).** "In findingmodels, there's a recent taxonomy branch with new files in lists that's the immediate direction for all of the content, probably replacing a lot of the Gamuts-based models." The taxonomies are to be called the "MGB exam-oriented sub-taxonomies."

## Content decisions, September 21

| Topic | Decision |
|---|---|
| Manuscripts in the bucket | Paraphrase facts, structures, and numbers; cite as "manuscript under review at JDIM, 2026" or "prepared for submission"; never quote; reviewer correspondence never reproduced or paraphrased. |
| Excalidraw boards | Publish the public-facing boards (object model, structured report sections, outcome tracking, exhibit figures, lineage, use-case notes). From internal boards, publish only schema and data-model ideas with organizations named; people, meeting histories, and vendor demo logistics omitted; the rest recorded as reviewed and held. |
| Diagrams | No Mermaid. Excalidraw files rendered to SVG beside each document. Per diagram, a builder is the source until the file is hand-edited, after which the builder is retired (tools/diagrams/README.md). |
| Vendor name in the deck extract | Generalized to "a reporting vendor". |
| Upstream defects | Drafted for the project lead's review before any issue is filed. |
| No specification exists | The project is in a coalescing phase; nothing is formally defined. The knowledgebase presents each source's current version of a structure side by side (repo branch and commit, manuscript under review, deck or webinar, board), dated and attributed, and states disagreements (for example the three Imaging Problem List status vocabularies) without resolving them. Words like "specification" or "canonical model" are not used for any of them. |
| Data structures versus transport | Per the project lead's 2026-09-19 manuscript notes: OIDM defines a system of data structures for imaging exam result information used inside applications; FHIR and DICOM are transport expressions designed separately and guided by the structures. The data-structure documents are to be reframed accordingly. |

## Decisions of September 22

These supersede the four-pillar page list that stood here earlier today. The owner's words are quoted; everything else is the two sessions' shared understanding, confirmed in conversation.

1. **Five named pillars. Use the names, never numbers.** "1. Foundation Context / Semantic layer: includes both the schema/meta-definitions as well as the efforts to build out content. 2. Data Structures, most ESPECIALLY in the Observation layer, and how there are two graphs and they work together. 3. SDKs, the tools that wrap the data structures and enable developers working in the application layer to manipulate instances in real-world applications (and some around helping with definition of the foundation context, obviously). 4. Theoretical Use Cases: Imaging all the different kinds of applications/tools/plugins/output products we could create using an ecosystem built around this foundation. 5. ACTUAL sample applications we've created to try to illustrate some of these ideas." The fourth was then shortened to **Use Cases**. So: **Foundation Context**, **Data Structures**, **SDKs**, **Use Cases**, **Sample Applications**.
2. **A CDE and a finding model are the same content.** "A 'CDE' and a 'Finding Model' are the same thing, but they're in different repos. Open Imaging Finding Models are in the OIDM-maintained repo, and are intended to be very INCLUSIVE, can almost be drafts. Common Data Elements live in the ACR/RSNA repository, and are intended to be WELL-REVIEWED. They're more like something published. They BOTH should soon be using the schema and classes being defined in the CDE schema re-write, with FindingClass, DataElement, Measurement, etc." Consequence: explain the common model once, then the inclusive OIDM collection and the well-reviewed ACR/RSNA collection and their relationship. Collection expectations are not per-item facts. Migration is intended, not complete. The "Observation Type" umbrella name the sessions had floated is withdrawn as unnecessary and was never approved.
3. **The OIFM reorganization around the graph is urgent.** "OIFMs VERY soon need to get re-organized around the graph-based approach we're developing in the next-gen-schema effort in CDEs. They're currently document-oriented and we need to fix that SOON." A change of organization, not added fields. Stated prominently under Foundation Context; current implementation kept distinct from direction; no storage, schema, or migration design invented beyond the source work.
4. **Source eligibility rule.** Repository documents, prompts, plans, skills, ADRs, and code are team artifacts eligible for substantive content. They are not demoted for being agent-assisted, and no statement needs separate human approval to be cited. Committing a document does not make a draft proposal or one implementation project-wide consensus. Each claim carries its source's actual status, date, and any explicit provenance label the source supplies (the CDE decision record's OWNER and CLAUDE DEFAULT, for example). Differences between sources and the owner's later corrections are preserved, not reconciled. No speculative authorship audit.
5. **Terminology.** Foundation Context (shared definitions, relationships, references) and Patient Context (this patient's imaging results plus relevant clinical context), from the SIIM 2026 deck. The CDE report graph, the Imaging Problem List representations, and the broader Patient Context are *related representations* of the Observation idea, never "the same thing serialized differently". Foundation Context and Data Structures correspond to the two graphs at the explanatory level; the report graph is the imaging-assertion part of Patient Context, not a clinical-context schema. The deck's "connective tissue" means relationships and citations between foundation concepts and is used only in that sense. Retained artifact names are used where a source's current files are cited: OIFM finding model, CDE set and element, the next-generation FindingClass, Diagnosis, Grouping, DataElement, Measurement.
6. **Organizing method** (agreed with Codex). The introduction explains the two-graph connection once within the five pillars. Idea anchors carry the recovered substance. Patient-side ideas say which shared definitions they reference; foundation-side ideas say how observations use them; related anchors link both ways. Existing worked examples are used for what each actually shows (the CDE pyelonephritis report and the deck's calculus figure show both graphs; the IPL example2 study is patient-side only; the deck's aneurysm and kidney tables are foundation-side only). Sources attach to ideas; repositories do not become chapters. Redundant generated exposition is deleted after its unique ideas are recovered; unique team-authored material is kept and counted in the budget. A glossary or question register is not a mandate to duplicate content.

## Presentation guidance, September 22–30

Project lead, 2026-09-27 to 2026-09-29, on the Finding Models and Common Data Elements hub page:

> I think what we want to say is that the finding/diagnosis definition is an unified anchor for the CONCEPT of a finding/diagnosis in a form that can be used to attach associated context: name, synonyms, definition, attributes, etc. OIFM are AN inclusive collection, intended for rapid prototyping... ACR/RSNA Common Data Elements (always include the organizations) are the well-reviewed... published through radelement.org. Forget about talking about the current schema's sets and elements--waste of bits.

> "Finding Models and Common Data Elements" / "Definitions of findings and diagnoses anchor these concepts in a form that associated content can..."

> "...maintained by the OIDM project..." / "The OIFM repository is intended for rapid, community-based prototyping and iteration based on an open-source model." / "...with changes proposed by anyone." / Take out "uneven" / "in the project lead's words" is RIGHT OUT. I think the thing to emphasize is that they will have the same schema and describe the same ideas. Major difference is that OIFMs is much more "beta"/rapid additions and updates and CDEs is much more "release"/reviewed and stable.

> I think we should also emphasize that we will maintain cross-links: when something migrates to CDEs, it will continue to be maintained in the OIFM repo but have a reference to its CDE identity. "Both CDEs and OIFMs are document-oriented today, and moving..."

The agreed hub text (2026-09-29) is the one the Opus agent writes verbatim into `site/pages/foundation-context/finding-models-and-cdes.md` (moved 2026-10-05; originally `knowledge/drafts/finding-models-and-cdes-hub.md`).

Project lead, 2026-09-30, on figures: "Let's make the AssessmentSchemes ovals rather than diamonds--those have a flowchart implication that doesn't obtain here." Recorded as a convention in tools/diagrams/README.md.

Project lead, 2026-09-30, four prose decisions on the relationships page: (1) change the associated-findings example to a pair the graph records as OCCURS_WITH; (2) the renal abscess clause becomes "...may have sequela beyond the course of the acute pyelonephritis episode."; (3) "whether or not one causes the other"; (4) use the schema's specificity words: pathognomonic, highly suggestive, suggestive ("they're cooler").

Project lead, 2026-09-30, on the pulmonary nodule neighborhood figure (illustrative; reflects updates the project lead, as the CDE project's clinical expert, intends for the CDE graph): rename "attenuation" to "composition" and "pulmonary margin" to "margin"; drop "lesion count"; "ground glass nodule" for "non-solid pulmonary nodule"; add the Grouping "pulmonary parenchymal abnormality"; add the diagnoses "pulmonary neoplasm" and "pulmonary granuloma" (subtype of the grouping); add "Fleischner criteria" as an assessment scheme; add subspecialty; show SEEN_ON CT, XR, and MR; no values; no time course or etiology for now: "I'm starting to think that may need to be a property of the edge connecting it to a diagnosis. Actually, that's the same for etiology."

Project lead, 2026-09-30, on the relationships page:

> Emphasizing that they're "strictly apart" makes it seem like THAT'S the issue. / Let's just call this subsection "Findings <-> Diagnoses: Manifestation and Causation" / "Pyelonephritis APPEARS AS striated nephrogram..." "when the pyelonephritis resolves, the striation goes with it..." / Next subsection called "Deriving the Differential" / "The schema distinguishes manifestation and causation to enable inference:..." / We should ALSO include the idea of associated findings here, and the properties of the edges themselves that get at how commonly findings/diagnoses are associated in the specified way / Don't include the "HPO and Orphanet" reference / "a pulmonary nodule definition specifies how a pulmonary nodule WILL BE DESCRIBED. The assessment is a separate assertion, defined by the AssessmentScheme definition, which allows for evaluation of the nodule according to the defined criteria." / "...by an ASSESSED_BY edge"

Project lead, 2026-09-30, on the next-generation schema page:

> "Both Open Imaging FInding Models and RSNA/ACR Common Data Elements are moving..." / Show a link to the ACR/RSNA CDE schema repository, on the next-gen-2026 branch. / "...as a graph of interconnected concepts rather than a set of documents." / "Applications will be able to use either or both collections at once via a common SDK based on the new schema." / "FindingClass" defines the properties of the items described in imaging reports. A "Diagnosis" is a separate, closely-related node type, distinguished by a different set of possible relationships. Groupings are broad classes of findings/diagnoses such as "renal abnormality", usually intended to be used in the negative. / For most of these node class definitions, we want to use "defines" rather than "is a" (this is a very tricky but important semantic distinction) / "AssessmentScheme" definitions layout the systems such as Lung-RADS via which a constellation of other findings is evaluated. / "The anatomic scope property of each other node indicates the locations and/or structures in which they may be localized (e.g., "lung parenchyma" for a pulmonary nodule). / "Edges integrate the notes into a rich fabric of interrelated concepts, enabling reliable, reproducible inference." / "Edges bind FindingClass and Diagnosis definitions to their anatomic scope and to the DataElements and Measurements used to specify their attributes. The edges themselves may contain properties that provide additional detail about the relationships between nodes." / Concept nodes as a note below the list, introducing the paragraph that also talks about anatomic scope. / Use the actual table of relationship types as examples. / "Evolution of CDEs and Finding Models: Both CDEs and existing Open Imaging Finding Models will have to migrate from their current JSON document-based organization to a new graph-oriented format, likely using RDF/OWL as an underlying storage format. More ergonomic data structures will also be developed for use in SDKs and via an API."

Project lead, 2026-09-30, on the SDKs (for the pillars figure and the SDKs index): "I think we should also say that the SDKs help AUTHOR and MAINTAIN the underlying foundation context."

Project lead, 2026-09-29, on Measurements (for the three-axes figure and the next-generation schema page):

> Measurements don't have EXPLICIT units, they indicate what KIND of thing they are: length (with appropriate length units, which could be mm, cm, whatever), CT density (HU), or count (unitless), ratio (unitless), velocity (m/s, cm/s), volume (cc, mL, mm^3..., L)

Project lead, 2026-09-24, on the Overview page:

> OIDM is NOT just for modeling imaging results, it is for modeling the ENTIRE imaging workflow context throughout its lifecycle. It's meant to enable a common platform across the medical imaging ecosystem that enables tools that will assist radiologists, technologists, ordering providers, and back-office staff. RIGHT NOW, we happen to be focused on data structures and semantics for representing imaging results, whether from current exams or prior, and from AIs, radiologists, technologists, or modalities themselves, and for integrating those results across time. We will ALSO model the broader patient context and enable linking between imaging results and patients' OTHER diagnoses, procedures, and issues.

> The imaging persona doesn't place the rest of the patient context "alongside"--it integrates them into a single, larger graph, underpinned by the Foundation Context. Basically, the imaging results can be integrated into the larger fabric of the patient's history.

> Let's call it "finding/diagnosis definitions" since they're used so interchangably. It really might be that "ObservationType" is the better catch-all term.

> "Pointers" is a... well, pointless inclusion. The idea is that the patient graph is deeply interconnected with the Foundation Context graph, attaching baseline clinical knowledge to the contingent patient facts. [...] every finding, diagnosis, location, and exam type.

Source added by the project lead on 2026-09-24: `~/exam-types/sources/LoincRsnaRadiologyPlaybook.xlsx` (44,178 Playbook part rows with LOINC numbers, part types, RadLex IDs and preferred names; a second sheet `core-playbook-dev`, 995 rows) for the exam-types page and diagrams. The ACR-RSNA-CDEs next-gen graph (`docs/next-gen-schema/graph/*.jsonl`, `alpha/graph/definition-graph.json`, `diagrams/*.svg`) supplies real nodes and typed edges for the Foundation Context figures.

Wording rules from these: "finding/diagnosis definitions" is the term for the WHAT axis for now ("Observation Type" is under consideration as the catch-all, not adopted); the connection between the graphs is described as interconnection that attaches knowledge to facts, never as pointers; the Imaging Persona integrates imaging results into one larger graph of the patient's history.

Project lead, 2026-09-23, correcting the first version of this plan:

> I think in the foundation context page, we need the document on finding models to be something that encompasses both OIFMs (and that repo) but also the RSNA/ACR Common Data Elements and the relationshpi between the two. We should ALSO think about how to present the work on the next-generation schema (which will be for BOTH CDEs and OIFMs--I think applications will be able to use both at once).

Project lead, 2026-09-22:

> There should be a big overview page, layout out a HIGH-LEVEL justification of the project, talking about what the CORE PIECES of it ARE (not the DETAILS, just basics about what they ARE). These are the first three pillars: foundation context, data structures, SDK.
> Then the next couple of things: start with some basics of USE CASES. We can have a LIST oriented view of cases, only SOME of which have a more fleshed out page.
> We can also have a list of our sample/demo applications, some of which are RELATED to the use cases.
> There should be a directory on the foundation context, with some documents on the key ideas related to FindingModels/CDEs and the definitions that go into them. There should be a page on the OIFM repository (with a node to its relationship to the CDE project). Tehre should be a page on AnatomicLocations, referencing existing work but also pointing to the fact that we're migrating to incorporate with RadLex. We can also describe the ExamType content to come.

And, on the shape: no page budget; the number of pages follows from the ideas. "Repository pages" are not a pattern: the one page on the OIFM repository exists because that repository *is* the inclusive collection of finding models.

## Source pipeline, October 1

> I'd like to have a literal knowledge bundle of OKF files which are mostly for internal team use. They're in a public repo, and anyone can look at them and see what they see, but they're not what we'd present. We'd ALSO like to have a series of interconnected pages that ARE intended as the outward presentation of these ideas, where the knowledge for them is a distillation of the broader knowledgebase to make it more accessible to outsiders.

> I would ALSO like to maintain something like source material. I will create a non-public bucket on tigris for raw source material (presentations, manuscripts, emails, etc.). I (or people I give appropriate credentials to) can access that bucket to fill out a raw-sources directory, but this is NOT in the repo. We will generate DETAILED distilled summaries with key quotes and ESPECIALLY extracted graphics into a references directory. We can cite these in our knowledge bundle as needed, and if required go back and dig into the raw source.

> I would promote "paraphrase and describe figures" to "generate new versions of the figures capturing key points".

## Repository-only knowledge and one plan, October 2

The project lead described the intended pipeline as:

> a Tigris bucket down to processed summaries to a repo-only OKF knowledge graph to the actual pages based on them

The project lead asked to replace conflicting planning documents with one coherent plan, discard superseded instructions, and integrate useful material into a compact set. Temporary files may live in an ignored directory exposed through `.peruseshow` where review is useful.

The old glossary was dropped by the project lead on September 29. New terms grow from the new pages as needed; incoming links must be repaired before removal. The reporting vendor and the organizations behind the 47 and 31 finding models remain generalized. The project lead permitted reuse of the SIIM deck and CDE-repository figures on September 29.

## Source-review snapshot, September 20–22

The following is retained from the original build plan because existing pages cite its inventory and work-edge observations. It is a dated research snapshot, not a fresh source audit or a current work queue. Broad absence claims below describe that review and must be checked against the later idea inventory and corrected drafts before reuse.

Inventory reports for every source live in the session scratchpad and are summarized here. "Read from" names the branch used for current state.

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
| SIIM 2026 deck, June 2026 ("Reports of the Future") | The framing: Patient Context and Foundation Context; the three axes (Observation Type, Anatomic Location, Exam Type) as OIDM layers over CDE/OIFM, RadLex, and the Playbook; relationships and external citations; SDKs that resolve codes; the ask | `sources/bucket/siim2026/` (public talk) | Whole deck; the slide 7 table and the foundation-context graph as figures, at the project lead's discretion |
| oidm-knowledge-sources bucket folder | Manuscripts (JACR IPL; two JDIM under review), the AI-evolution essay, the reporting-schema deck, the July 2026 SIIM webinar deck | `sources/bucket/REPORT.md` | Paraphrase and cite per the manuscripts rule; reviewer correspondence never used |

### The work edge

The project lead asked that the knowledgebase reflect the entire work edge, not only default branches. Cite the branch and pin the commit they read for each account of current state.

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
