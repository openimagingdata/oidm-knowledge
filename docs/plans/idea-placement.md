# Idea placement table

Step before drafting, per `restructure-joint-notes.md`. Maps every idea in the two inventories —
`idea-inventory-semantic.md` (prefixed `Sem-`) and `idea-inventory-structures-and-uses.md`
(prefixed `Use-`) — to the section that will house it. The two inventories both use letters A-F
for their own sections, so IDs collide between them (`Sem-A1` and `Use-A1` are different ideas);
the `Sem-`/`Use-` prefix disambiguates.

**Count note.** The joint notes and the semantic inventory's own scope line both call this "the
inventories' 70-odd ideas". The semantic inventory (`idea-inventory-semantic.md`) in fact carries
46 numbered ideas (A1-A10, B1-B9, C1-C8, D1-D9, E1-E2, F1-F8) and the structures-and-uses
inventory states its own scope as 41 (A1-A26, B1-B11, C1-C4). That is 87 ideas total, not 72.
This table places all 87.

**Revision history.**
1. First version used a human-stated / linking-prose role split that demoted anything sourced
   from a prompt, skill, design note, ADR, or repo doc to secondary status.
2. The project lead overrode that: ideas mined from the repositories' documentation, plans,
   prompts, skills, ADRs, and design notes are the team's own ideas and belong in the graph as
   first-class content, not as linking prose. The role column became **source kind**: *team
   artifact* (deck, brief, manuscript, webinar, site post, board, repo doc, plan, prompt, skill,
   ADR, README, commit message — anything the team wrote or committed) versus *agent inference*
   (an inventory agent's own synthesis, invented rationale, or a question with no team source).
   Checked against that standard, all 87 ideas carry a cited team-artifact source; none is bare
   agent inference, so the agent-inference column is 0 throughout and nothing was left off a
   section for lacking a team source.
3. A SIIM 2026 deck ("Structured Results and Context for Next-Generation Imaging Resulting
   Tools") arrived and briefly got its own "Relationships and external citations" page under a
   four-pillar structure.
4. **This version (2026-09-22): re-sectioned under the five named pillars from the "Agreed
   outline" in `restructure-joint-notes.md`** — Introduction, Foundation Context, Data
   Structures, SDKs, Use Cases, Sample Applications, Off the reading path — per the owner's
   2026-09-22 decision that pillars are named, never numbered, and that a CDE and a finding
   model are the same content in two collections. The former "Relationships and external
   citations" page is folded into Foundation Context's "Finding models and CDEs" table as the
   common-graph cluster, since the relationship ideas are part of that same graph. Placement
   flags resolved this pass: Sem-F1, F2, F6, Use-A12, Use-A15 (moved or confirmed, no longer
   flagged). Use-A17, Use-A18, Use-B7 stay at their prior placement — one-line reasons in the
   Summary.

---

## Introduction

| ID | Name | Source kind | Notes |
|---|---|---|---|
| Use-C1 | OIDM's stated purpose | team artifact | Site tagline, January 2026 deck title, project lead's 2026-09-19 formulation. |
| Use-C2 | The relationship among the parts: three layers, and the DOM analogy | team artifact | Deck's three strategic pillars; 2024 site post; the DOM/HTML analogy is stated independently on two boards. |
| Use-C3 | Structure first, standards after; and how agreement is supposed to happen | team artifact | Deck's call to action (working group, structure-first); Board 14's ACR Data Science Institute role. |
| Use-C4 | Nothing is formally defined yet | team artifact | Source is the project lead's 2026-09-21 decision of record in `knowledge/plans/2026-09-20-knowledgebase-build-plan.md` — a plan document, a team artifact. States the project's own coalescing-phase status. |

4 ideas.

---

## Foundation Context

### Finding models and CDEs

One table per the 2026-09-22 correction: a CDE and a finding model are the same content, in two
collections (the inclusive OIDM collection and the well-reviewed ACR/RSNA collection), sharing one
common graph. The **Cluster** column mirrors the outline's own grouping: the common graph
(including the relationship ideas formerly tabled separately as "Relationships and external
citations"); the two collections and their relationship; what the inclusive collection contains
and where it is going; authoring, triage, and review; identifiers and metadata rules.

| ID | Name | Cluster | Source kind | Notes |
|---|---|---|---|---|
| Sem-F1 | Anatomic scope, not location | Common graph | team artifact | The next-generation vocabulary's statement of which anatomic locations are congruent with a finding class, and how strongly. Matches the SIIM deck slide 12's "Observation Type anatomy limits" cross-axis category almost verbatim. Prior "?" flag (versus Anatomic Locations) resolved: the common-graph cluster is the single home. |
| Sem-F4 | The finding model relationship registry | Common graph | team artifact | Draft schema in which a model stores only the relationship assertions authored on it, with a registry declaring each type inverse-backed, symmetric, or one-way; corrected by a later document that found it unimplemented. The general mechanism the deck's "within-axis relationships" list (parent/child, causes/caused_by, confused_with, occurs_with) would be instances of. |
| Sem-F5 | The relationship family and the derived differential | Common graph | team artifact | Seven relationship pairs plus a catch-all connecting finding classes and diagnoses, keeping manifestation and causation apart. The deck's worked figure (radiodense urinary calculus `OIFM_GMTS_020556` "may cause" hydronephrosis `OIFM_OIDM_874812`) is a causes/caused_by instance of this family. |
| Sem-F6 | Measurement, method, and interpretation are three things | Common graph | team artifact | Next-gen vocabulary design document. Prior "?" flag (versus staying at Open Imaging Finding Models, since the document itself notes the principle is already written in narrower form in the finding-model guidance) resolved: placed with the common graph alongside Sem-F4/F5, which it shares a document with. |
| Sem-A9 | Assessment schemes modeled apart from what they assess | Common graph | team artifact | `ASSESSED_BY`/`INTERPRETED_FROM` are cross-finding relationship types from the next-gen relationship-family document; matches the deck's "within-axis relationships" category (an edge between two Observation Type nodes). |
| Sem-A10 | Associated findings versus components | Common graph | team artifact | An associated-finding attribute references another finding model by name; a component is extracted into its own model. Matches `occurs_with` (independent co-occurring findings) and the part-of shape the deck's figure applies to anatomy (renal pelvis "part of" kidney), here applied to finding components. |
| Use-A15 | Foundation context: four per-finding dimensions that tell an agent what to expect | Common graph | team artifact | Webinar states this directly (body regions, entity type, expected time course, permanence). Prior "?" flag (versus staying at Imaging Problem List) resolved: this is graph content about what the finding-class definition carries, and overlaps substantially with Sem-C1's "eight fields" below, from the same webinar slides. |
| Sem-F7 | Finding models as the CDE workbench | Collections and their relationship | team artifact | January 2026 deck ("OIFM: the CDE workbench"); project lead's statement that CDE work "should dovetail with the OIFM work"; the "Current Understanding" document. |
| Sem-F8 | Measuring coverage by running real reports against the vocabulary | Collections and their relationship | team artifact | CDEStaging catalogues (`negative_statements.md`, `uncovered_findings.md`, `missing_attributes.md`) and the extraction-process note. |
| Sem-B2 | Corpus as a merge of uneven provenance streams | Content direction | team artifact | The identifier registry and the "Definition Cleanup Plan"; supplies the counts behind Sem-B7's stated direction. |
| Sem-B7 | Exam-oriented finding sub-taxonomies | Content direction | team artifact | The project lead's 2026-09-21 statement that this is "the immediate direction for all of the content," plus the taxonomy README. |
| Sem-B8 | Convert and merge, with a fixed direction | Content direction | team artifact | The chest CT content branch's project specification. |
| Sem-B9 | Content repository proposes changes upstream to the library | Content direction | team artifact | The upstream-proposals plan document. |
| Sem-B3 | Stub creation and iterative improvement | Authoring, triage, review | team artifact | The "OIFM Repo" board's pipeline flowchart and "Community Connect 2024-11-07" note; the `enrichment.md` prompt fragment. |
| Sem-B4 | Triage before create | Authoring, triage, review | team artifact | Prompt fragment (`search_and_triage.md`) and the `finding-author` skill. |
| Sem-B5 | Review in three tiers, with context isolation | Authoring, triage, review | team artifact | Prompt fragments and the `finding-review`/`finding-batch` skills. |
| Sem-B6 | Prompts as loadable fragments, sized against measured degradation | Authoring, triage, review | team artifact | The team's own prompt-length research write-up and the skill files' stated design rule. |
| Sem-C4 | Focused assignment agents, advisory audit, and null as an answer | Authoring, triage, review | team artifact | Architecture decision record (`0002-split-agent-assignment-architecture.md`) and agent prompts. |
| Sem-C5 | Human review is the only authority | Authoring, triage, review | team artifact | Policy document (`human-review-and-writeback.md`) and the plan-history document. |
| Sem-A1 | Finding model | Identifiers and metadata | team artifact | Prompt fragment (`core_concept.md`), the upstream overview document, the schema document, and the "OIFM Repo" Excalidraw board's plain-language explainer panel. |
| Sem-A2 | What counts as a finding | Identifiers and metadata | team artifact | Prompt fragments (`core_concept.md`), the overview document, and an Excalidraw board's earlier draft of the same rule. |
| Sem-A3 | Specificity, splitting, and the right level of abstraction | Identifiers and metadata | team artifact | Prompt fragment (`scope_and_specificity.md`) and the overview document. |
| Sem-A4 | Negative assertion as a first-class finding | Identifiers and metadata | team artifact | Prompt fragments, the creation script, and the next-gen-schema design document; distinct from Use-A11/Use-A23, which are about EFL/Observation-level negation. |
| Sem-A5 | Description and diagnosis both count | Identifiers and metadata | team artifact | Prompt fragment, the `entity_type.md` assignment prompt, and the next-gen-schema design document; distinct from Use-A9's cross-report matching angle on the same finding-vs-diagnosis question. |
| Sem-A6 | Presence and change from prior | Identifiers and metadata | team artifact | Prompt fragment (`presence_and_change.md`) and the creation script. |
| Sem-A7 | Synonyms as the matching surface | Identifiers and metadata | team artifact | Prompt fragments (`synonym_rules.md`, `naming.md`). |
| Sem-A8 | Naming conventions | Identifiers and metadata | team artifact | Prompt fragments and the "Definition Cleanup Plan". |
| Sem-B1 | Identifiers that carry provenance | Identifiers and metadata | team artifact | Metadata-fields reference document, the repository's `CLAUDE.md`, and an Excalidraw board's identifier-format notes. |
| Sem-C1 | Lean published models versus the full metadata schema | Identifiers and metadata | team artifact | Project lead's stated goal ("needs overhaul for increased metadata"); webinar's "Lean vs full" slides; the metadata rewrite document. Two of its eight fields (`applicable_modalities`, and `anatomic_locations` on the base model per Sem-A1) carry cross-axis edges per the deck, but the idea's own subject is the schema as a whole, not those two fields specifically — kept here rather than moved to the common-graph cluster. |
| Sem-C2 | Each metadata field is defined by what it excludes | Identifiers and metadata | team artifact | Policy document (`docs/metadata/subspecialties.md`) and assignment prompts. |
| Sem-C3 | Index codes must be exact | Identifiers and metadata | team artifact | Assignment prompt (`ontology_decision.md`) and the metadata rewrite document. |

31 ideas.

### Anatomic locations

| ID | Name | Source kind | Notes |
|---|---|---|---|
| Sem-D1 | Spatial containment as a single-parent tree to the whole body | team artifact | JDIM manuscript Methods/Results; the project site's homepage states the same rule publicly; the "Current Understanding" document verifies it against the data. |
| Sem-D2 | Containment and part-of are different relations | team artifact | Manuscript and site "code" page; the field-reference skill document. |
| Sem-D3 | Laterality as explicit triads | team artifact | Manuscript Methods, with counts for all 795 bilateral structures; the laterality-conventions reference document. |
| Sem-D4 | Synthetic post-coordinated terms | team artifact | Manuscript Methods gives the counts; the laterality-conventions reference document gives the curation rule. |
| Sem-D5 | Measuring what existing ontologies actually populate | team artifact | Manuscript Methods and Results (the measurement itself, specified to be recomputable). |
| Sem-D6 | An overlay on RadLex, not a competitor | team artifact | The "Anatomy Axis, Current State" document records the 2026-09-13 agreement; the deck's "FMA enrichment" direction (defined but not yet populated: definitions, references, new edges `branch_of`/`bounded_by`/`adjacent_to`) extends this as stated direction — deck-sourced, no separate inventory idea states it. |
| Sem-D7 | The missing is-a and structure-type layer | team artifact | Next-gen-schema design document (`11-anatomy-axis.md`), which itself separates the project lead's scope families from "exploratory ideas from the assistant, not adopted" — a distinction the source document draws, not one this inventory added. |
| Sem-D8 | Curation rules that make the codes usable | team artifact | The field-reference skill document's "SNOMED Coding Guidance". |
| Sem-D9 | A reference layer, not a labeling algorithm | team artifact | Manuscript Discussion states the reference-layer framing directly. |
| Sem-F3 | Contributing terms back, and the two-phase proposal loop | team artifact | Ties directly to Sem-D6/Sem-D7 (the RadLex overlay and its gaps); the `radlex-concepts` skill and the RadLex testing document. |

10 ideas. Tooling (the anatomic-locations package, BodyPartIndex libraries) moves to SDKs per the
outline; no inventory idea's primary subject is that tooling, so nothing moves out of this table.

### Exam types

| ID | Name | Source kind | Notes |
|---|---|---|---|
| Sem-E1 | Preferred high-level exam entries over the Playbook | team artifact | Project lead's stated goals, restated across four years in three documents (site roadmap, board, `med-ontology-lookup` product-roadmap document). |
| Sem-E2 | Exam-to-anatomy inclusion edges and the imaging region | team artifact | Project lead's stated goals; a 2024 board states the same requirement as "defining an imaging region"; the deck (slide 11) restates it as focused/included/edge (usually vs possible) anatomy — same author, two dated phrasings, both belong on this page per the outline. |

2 ideas.

### Standards the foundation layers over and cites

| ID | Name | Source kind | Notes |
|---|---|---|---|
| Sem-F2 | Terminology roles, and search recall as the gate | team artifact | RadLex, SNOMED CT, and LOINC/the Playbook each play a stated role as the terminology OIDM's axes point out to (manuscript "Term selection"; "Hybrid FTS search" design document). Matches the deck's "external citations" category — the deck names SNOMED, RadLex, and LOINC among its own eight (Radiopaedia, Wikipedia, SNOMED, RadLex, LOINC, FMA, ICD, CPT); this idea covers three of those eight and the role each plays. No inventory idea covers Radiopaedia, Wikipedia, FMA, ICD, or CPT — the deck is the only source for those five. Prior "?" flag (cross-cutting Anatomic Locations/Exam Types/ACR-RSNA CDEs) resolved: this page is the single home. |

1 idea. The lookup tool (`med-ontology-lookup`) moves to SDKs per the outline.

Foundation Context total: 31 + 10 + 2 + 1 = **44 ideas.**

---

## Data Structures

The two graphs (Foundation Context and Patient Context) and how they work together are the center
of this pillar.

### Observation

| ID | Name | Source kind | Notes |
|---|---|---|---|
| Use-A1 | Observation as the atomic unit of an imaging result | team artifact | January 2026 deck's own definition of the unit; the repository's `CLAUDE.md`; a 2024 reference implementation. |
| Use-A10 | Presence is binary; confidence and hedging are a separate axis | team artifact | JDIM manuscript and SIIM webinar state the design directly; the extraction prompt's `PRESENCE_BLOCK` gives a contrary implemented example. |
| Use-A11 | Pertinent negatives are first-class entries | team artifact | Manuscript and webinar state the rule directly; the extraction prompt and coding prompts enforce it. |
| Use-A12 | Every finding carries a standardized anatomic location, assigned by explicit rules | team artifact | Repo assignment-rules document (`anatomic-location-assignment-rules.md`) and the coding pipeline prompts. Prior "?" flag resolved: stays here (what an Observation carries — "what plus where") with a cross-link to the Anatomic locations page under Foundation Context, which owns the index those rules resolve against. |
| Use-A23 | Normality is recorded as an absent abnormality | team artifact | Extraction prompt blocks (`CORE_INSTRUCTIONS_BLOCK`, `CHUNK_RULES_BLOCK`), the reviewer prompt, and a 2024 hand-extraction sample. |
| Use-A24 | Coding aims at convergence, so generalizing is allowed and specializing is not | team artifact | Coding prompts (`FINDING_TERM_SYSTEM`, `FINDING_CODE_SELECTOR_SYSTEM`) and the coding-agent design document. |
| Use-A25 | Finding type, anatomic site, and presence are independent axes | team artifact | Coding-prompt rules and the coding-agent design document. |

7 ideas.

### Exam Finding List

| ID | Name | Source kind | Notes |
|---|---|---|---|
| Use-A2 | Two-level architecture: Exam Finding List, then Imaging Problem List | team artifact | JDIM manuscript states the two-level rationale directly; the repository README states the same division. |
| Use-A3 | The faithful-translation constraint on the Exam Finding List | team artifact | Manuscript, webinar, and JACR manuscript (which reports the team's own tool violating the rule); the extraction prompt enforces it three times. |
| Use-A9 | One finding may be described by several observations in one report, and by different codes across reports | team artifact | Project lead's 2026-09-19 email notes (points 1 and 2) state this directly; the extraction prompt's `DEDUPLICATION_BLOCK` is the working resolution. |
| Use-A17 | Report sections beyond Findings are unmodeled | team artifact | Board 6 poses the open question directly; the canonical section vocabulary (`report-sections.md`) is the implemented partial answer. **Stays** (see Summary): reads as an open question more than a settled idea, but it is team-sourced, so it stays on a section page rather than moving to the open-questions register. |
| Use-A26 | A named taxonomy of extraction failures, checked by an independent reviewer | team artifact | Reviewer prompt (`validator_prompt_example.md`) and the extraction-internals design document — the structure rule for how a chunk is checked against its source text. Sample Applications' description of the report extraction platform's failure taxonomy and evaluation practice cites this idea; it is not duplicated as a row there. |

5 ideas.

### Imaging Problem List

| ID | Name | Source kind | Notes |
|---|---|---|---|
| Use-A4 | Entry identity is the finding code plus the anatomic site | team artifact | JDIM manuscript states this directly; the repository's `CLAUDE.md` and generation script confirm it. |
| Use-A5 | Status is derived from the observation history, never stored — and three vocabularies disagree | team artifact | Manuscript, webinar, and the repository's `CLAUDE.md`/viewer-v2 plan each state their own vocabulary. |
| Use-A6 | The succession link | team artifact | Manuscript's worked example (pneumonia and its scarring); webinar restates it. |
| Use-A7 | Per-observation provenance and review status, and corrections as provenance operations | team artifact | Manuscript and webinar state the design directly; the extraction platform's `README.md` implements provenance for the extraction pipeline. |
| Use-A8 | Entity resolution is the open problem; graduated-confidence linking is the proposal | team artifact | Manuscript states the three confidence levels directly; webinar names entity resolution as "the open frontier"; JACR manuscript reports the measured limitation. |
| Use-A13 | Anatomic-compatibility reconciliation is unresolved, and the sample data shows the cost | team artifact | Repo design document (`anatomic-location-assignment-rules.md` known-limitation section) naming the gap. |
| Use-A14 | Permanent findings, and the need to rank entries before display | team artifact | JACR manuscript Methods and measured results. |
| Use-A18 | Recommendation structure, and a live-versus-closed axis on IPL entries | team artifact | Manuscript and Board 12. **Stays** (see Summary): the manuscript attaches the recommendation to the IPL entry structurally, even though the "ACR priorities" bucket under Use Cases also touches recommendation tracking. |
| Use-A19 | A finding as a persistent tracked entity with a durable identifier | team artifact | Boards 4 and 15, a 2024 site post, and the manuscript; an unmerged branch's design note. |
| Use-A22 | The re-documentation burden: measured evidence for the Imaging Problem List | team artifact | JACR manuscript results, the core quantitative case for the IPL. |

10 ideas. (Use-A15, "foundation context: four per-finding dimensions," moved to Foundation
Context's Finding models and CDEs table — see that table's notes.)

### Imaging Persona

| ID | Name | Source kind | Notes |
|---|---|---|---|
| Use-A16 | Imaging Persona and the reporting data context object model | team artifact | January 2026 deck names it directly; two boards give a fuller object model; a 2024 site post; the deck's Global Imaging Persona figure (patient history, vitals, meds, current profile, genetic profile, previous scans around the IPL). The structure half stays here; the use half (the reporting context object model, alongside Use-B8's plugin container) is cited under Use Cases, not duplicated as a row there. |

1 idea.

### Structures versus transport

| ID | Name | Source kind | Notes |
|---|---|---|---|
| Use-A21 | Application-layer data structures, distinct from transport expressions | team artifact | Project lead's 2026-09-19 email notes state this directly; the JDIM manuscript's Methods and Discussion state the same independence; FHIR mapping is documented and unimplemented; the interoperability demonstration (Use-B9, at Sample Applications) is linked here as an example of what would need to travel. |

1 idea.

Data Structures total: 7 + 5 + 10 + 1 + 1 = **24 ideas.**

---

## SDKs

| ID | Name | Source kind | Notes |
|---|---|---|---|
| Sem-C6 | Documents record judgment; the schema is the specification | team artifact | Architecture decision record (`0001-lean-metadata-docs-schema-is-spec.md`). The finding model SDK's documentation practice: what is authoritative (the code/schema) versus what is policy (the docs). |
| Sem-C7 | Two databases from one source commit | team artifact | Architecture decision record (`0003-dual-db-pre-post-metadata-release.md`). The finding model SDK's release strategy: what a developer gets, pre- and post-metadata release. |
| Sem-C8 | Three retrieval modes over the corpus | team artifact | Matches "resolve, don't reinvent": the finding model SDK's format, index, search, enrichment, MCP server. Source: the metadata rewrite document and the package code (`index.py`, `similar.py`, `mcp_server.py`). |
| Use-A20 | A formal system of data models with generated schemas | team artifact | The outline names this directly as the proposed Imaging Problem List SDK: issue #1 (opened by the project lead) and the dev-branch platform as its precursor. |

4 ideas. Use-B3 (coding decoupled from extraction) moved out to Sample Applications this pass — see
that table's notes; the outline treats it as part of what the report extraction platform
demonstrates, not as SDK content on its own.

---

## Use Cases

| ID | Name | Source kind | Notes |
|---|---|---|---|
| Use-B5 | Six downstream application families for the Imaging Problem List | team artifact | Manuscript, webinar, and deck all state the families: report pre-population, incidental-finding surveillance, chronic-disease monitoring, cross-subspecialty awareness, quality surveillance and research cohorts, and the breast case. |
| Use-B6 | Breast imaging: one entity across assessments, and an automated MQSA audit | team artifact | Webinar states this as "planned work, not results" by its own account. |
| Use-B7 | Outcome tracking, follow-up completion, and radiology-pathology correlation | team artifact | Boards 12 and 7, and a published external quality-measure citation. **Stays** (see Summary): grouped here as a use case rather than at Foundation Context or Data Structures, since it is a proposed application built on the record, not part of either graph's own definition. |
| Use-B8 | The reporting assistance framework: a context object model plus a plugin container | team artifact | Deck names it "Open Imaging Reporting SDK"; 2023 site post and Board 9 give the design; `CDETemplateDemo` is a working precedent. Grouped with the use half of Use-A16 (Imaging Persona's reporting data context object model), which is not duplicated as a row here. |
| Use-B11 | The use case catalog and the six value categories | team artifact | `UseCases` repo and Board 13; the six RSNA Reporting Informatics Committee value categories (reporting efficiency, care team communication, operations/quality/safety, research, public health, education). |

5 ideas. Use-B9 (the multi-vendor interoperability demonstration) is a use case in purpose but was
built and shown, so its ID row sits at Sample Applications per the outline; its aim (what the
demonstration was for) is cited here without a duplicate row. ACR priorities (recommendation
tracking, AI validation, quality metrics, RADS support) and the deck's determinative-tools /
generative-agents consumer families are context for this whole table, not separate IDs.

---

## Sample Applications

| ID | Name | Source kind | Notes |
|---|---|---|---|
| Use-B1 | The Imaging Problem List viewer, and anatomy as presentation only | team artifact | The two viewers (IPL viewer 1; IPL viewer 2 with anatomy) named directly by the outline; the deck names the live demo; the design substance comes from the viewer-v2 plan document. |
| Use-B2 | The report extraction, coding, persistence and review platform | team artifact | The repository's `README.md`/`CLAUDE.md`, and the webinar's own framing of the platform as "one implementation of many." |
| Use-B3 | Coding is an independent job, decoupled from extraction | team artifact | Moved here from SDKs this pass. Design rationale document (`docs/coding-agent-design.md`); part of what the report extraction platform demonstrates about its own architecture, per the outline. |
| Use-B4 | Honesty-first evaluation of extraction | team artifact | Evaluation-redesign plan document (`extractor-evals-redesign.md`) and the reviewer-workflow documents — the platform's evaluation practice. Use-A26 (Exam Finding List) is the extraction failure taxonomy this evaluation practice checks against; cited here, not duplicated as a row. |
| Use-B9 | A multi-vendor interoperability demonstration exchanging CDE-labeled FHIR Observations | team artifact | Moved here from Use Cases this pass, as built and shown: Boards 15, 14, and 1. Its purpose is cited under Use Cases without a duplicate row. |
| Use-B10 | Local-only operation for protected health information | team artifact | Implementation and archived hardening documents; a status/deployment detail of the report extraction platform; the JACR manuscript's Methods state the same operating constraint. |

6 ideas.

---

## Off the reading path

Empty. Every one of the 87 catalogued ideas carries a team-artifact source and has been placed
under a section above. No agent-inference-only idea was found among the 87 — that material lives
in the inventories' own "Undetermined" and "What could not be determined" sections, which this
table does not place as separate ideas.

---

## Summary

| Section | Ideas |
|---|---|
| Introduction | 4 |
| Foundation Context — Finding models and CDEs | 31 |
| Foundation Context — Anatomic locations | 10 |
| Foundation Context — Exam types | 2 |
| Foundation Context — Standards the foundation layers over and cites | 1 |
| **Foundation Context total** | **44** |
| Data Structures — Observation | 7 |
| Data Structures — Exam Finding List | 5 |
| Data Structures — Imaging Problem List | 10 |
| Data Structures — Imaging Persona | 1 |
| Data Structures — Structures versus transport | 1 |
| **Data Structures total** | **24** |
| SDKs | 4 |
| Use Cases | 5 |
| Sample Applications | 6 |
| Off the reading path | 0 |
| **Total** | **87** |

Every idea carries a team-artifact source (agent-inference count is 0 throughout, unchanged from
the prior pass).

**Remaining "?" flags, marked stays:**
- **Use-A17** (report sections beyond Findings are unmodeled) — stays at Exam Finding List. It
  reads as an open question (Board 6) more than a settled idea, but it is team-sourced, so it
  belongs on a section page rather than the open-questions register.
- **Use-A18** (recommendation structure, live-versus-closed axis) — stays at Imaging Problem
  List. The manuscript attaches the recommendation to the IPL entry structurally; Use Cases'
  "ACR priorities" bucket touches recommendation tracking too, but the structural claim's one
  home is the data structure it modifies.
- **Use-B7** (outcome tracking, follow-up completion, radiology-pathology correlation) — stays
  at Use Cases. It is a proposed application built on the record (Boards 12 and 7), not part of
  either graph's own definition, so it belongs with the other use cases rather than at
  Foundation Context or Data Structures.

Flags resolved this pass (no longer marked "?"): Sem-F1, Sem-F2, Sem-F6 (all placed in Foundation
Context's Finding models and CDEs table, common-graph cluster, or the standards table for F2);
Use-A12 (stays at Observation with a cross-link note to Anatomic locations); Use-A15 (moved to
Foundation Context's Finding models and CDEs table, common-graph cluster).
