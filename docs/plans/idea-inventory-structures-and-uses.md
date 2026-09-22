# Idea inventory: observations, imaging history, applications, and OIDM's purpose

Status: Working inventory for step 1 of `restructure-around-project-ideas.md`. Not a published page. No idea pages written.

Scope: 41 distinct ideas (A1-A26 structures, B1-B11 applications, C1-C4 purpose). Area covered: observations and imaging history (Observation, Exam Finding List, Imaging Problem List, Imaging Persona, status and trajectory, succession and linking, provenance and review, application-layer structures versus transport expressions, extraction and coding of findings from reports); the applications and uses the team wants to demonstrate; OIDM's stated purpose and the relationship among its parts.

## How to read this

Each idea carries a **statement** in the team's own terms, a **status** (stated goal / working proposal / implemented example; several entries where an idea exists at more than one status), **evidence** as precise pointers, **related ideas**, **unresolved** alternatives with attribution, and **undetermined** where the sources do not settle a question.

Evidence conventions and short names used throughout:

| Short name | What it is | Pin |
|---|---|---|
| IPL repo `main` | `openimagingdata/imaging-problem-list`, branch `main` | `06f64a7` (2025-11-18) |
| IPL repo `dev` | same repo, `origin/dev` | `36fa30c` (2026-07-22) |
| JDIM IPL manuscript | "The Imaging Problem List: A Standards-Based Framework for Longitudinal Tracking of Imaging Findings", JDIM-D-26-02980 **R1, under review** | `sources/bucket/JDIM-D-26-02980_R1.pdf`; clean manuscript pp.3-32; printed page numbers cited below |
| JACR IPL manuscript | "Follow-Up Chest CT Reporting Is Mostly Re-Documentation…", **prepared for submission**, blinded | `sources/bucket/text/jacr-ipl-manuscript.md`; supplement `…/jacr-ipl-supplement.md` |
| SIIM webinar | "The Imaging Problem List as an Accelerator for Radiology AI Applications", SIIM Enterprise Imaging Webinar, delivered 2026-07-15, **public** | `sources/bucket/text/ipl-webinar-deck.md`, cited by slide number |
| January 2026 deck | "OIDM 2026 Status Update: Realizing Object-Oriented Imaging Results" | `sources/gamma-2026-status-update.md` |
| Email notes | Project lead's notes on the revised IPL manuscript, 2026-09-19 | `sources/email/2026-09-19-ipl-manuscript-notes.md` |
| Board *n* | Excalidraw board *n* as transcribed | `sources/excalidraw-diagrams.md` |
| example2 study | File-by-file code read of the dev-branch sample data and viewers, 2026-09-21 | `sources/ipl-example2-study.md` |
| Site post | openimagingdata.org Ghost post, dated | live site |

Other pins: `IPL-MVP-ExtractionAndLabeling` `main` `b06948f` (2025-10-20), branch `origin/Persistent_FHIR_Resources` `5ea6720`; `OpenImagingDataModel.py` `main` `455e5b6` (2024-11-13); `FHIRSamples` `main` `9ae2fa9` (2024-03-13); `UseCases` `main` `71a90d2` (2024-02-26); `CDETemplateDemo` `master` `e09f255` (2023-06-15); `FindingModelForge` `main` `f55dc85` (2025-08-20), `origin/dev` `15d9ebc` (2026-01-02).

Board sensitivity. Boards 1, 2, 6, 7, 10, 11 and 15 carry named individuals, meeting attendee lists, or vendor-collaboration histories per the sensitivity section of `sources/excalidraw-diagrams.md`. Only schema and data-model ideas are drawn from them here, with organizations named and people, dates tied to people, and meeting histories omitted. Boards 4, 8, 12, 13 and 14 are flagged low or moderate sensitivity with no named individuals. Board 8 is the one flagged as exhibit-ready and public-facing. Response-to-reviewer correspondence in both JDIM PDFs was identified and not read for content, and is cited nowhere.

## Prompts as primary sources

The prompts the team wrote carry its operational definitions: what counts as a finding, how presence, negation, hedging, laterality and location are decided, and what a valid extraction is. They are cited here as documents in their own right, by file and constant name, not as "the repository". All are on IPL repo `dev` `36fa30c` unless stated.

| Document or prompt | What it governs |
|---|---|
| `src/finding_extractor/extractor/prompt.py` | The extraction system prompt, assembled from named blocks: `ROLE_BLOCK`, `CORE_INSTRUCTIONS_BLOCK`, `DEDUPLICATION_BLOCK`, `PRESENCE_BLOCK`, `ATTRIBUTES_BLOCK`, `LOCATION_BLOCK`, `NON_FINDING_BLOCK`, `OUTPUT_FORMAT_BLOCK`; plus `CHUNK_ROLE_BLOCK` and `CHUNK_RULES_BLOCK` for the chunk sub-agent |
| `src/finding_extractor/coding/prompt.py` | Four coding prompts: `FINDING_TERM_SYSTEM`, `LOCATION_TERM_SYSTEM`, `FINDING_CODE_SELECTOR_SYSTEM`, `LOCATION_CODE_SELECTOR_SYSTEM`, each with numbered rules |
| `prompts/validator_prompt_example.md` | The chunk reviewer's system prompt, user-prompt template, and structured response shape |
| `docs/coding-agent-prompts.md` ("Coding Agent Prompts — Draft v2") | The same four coding prompts with a "Design Notes" section explaining why there are four and what each unresolved reason signals |
| `docs/coding-agent-design.md` | The coding pipeline's phases, rationale and tuned parameters |
| `docs/report-sections.md` | The canonical report-section vocabulary, alias table, and detection rules |
| `docs/extraction-internals.md` | Sectioning and chunking behavior, the chunk contract, the reviewer contract |
| `docs/anatomic-location-assignment-rules.md` | The location precedence ladder, laterality, bilateral and specificity rules |
| `docs/technical-imaging-findings.md` | The catalog of modality-specific technical terms and the rule against reinterpreting them |
| `initial-extraction-plan.md` | The original model design and the post-extraction validation design |
| `docs/plans/extractor-evals-redesign.md`, `extraction-reviewer-ux.md`, `extraction-reviewer-workflows.md` | Evaluation honesty, the reviewer instrument, gold adjudication |
| `config.py` in `IPL-MVP-ExtractionAndLabeling` `main` `b06948f` | `EXTRACTION_SYSTEM_PROMPT`, the two-field ancestor of the current model |

Code behavior is reported as what the software does, in the idea's terms, with a pointer. Installation and usage documentation is not reproduced.

---

# Part A. Observations and imaging history

## A1. Observation as the atomic unit of an imaging result

**Statement.** One Observation records one finding asserted on one exam: *what* (a coded finding type), *where* (an anatomic location), and *attributes* (presence indicators, change from prior, measurements, lesion characteristics). The January 2026 deck calls it "the atomic unit" with a "universal structure across systems."

**Status.** Stated goal (deck); implemented example (every EFL entry in the sample data); working proposal (the typed class model on Board 4).

**Evidence.**
- January 2026 deck, "Observation object (atomic unit)": "What + Where + Attributes: finding tag + anatomic location + lesion characteristics. Presence indicators, change from prior, measurements. Universal structure across systems." — the deck's own definition of the unit.
- IPL repo `dev` `36fa30c`, `CLAUDE.md` "Domain Model": each EFL finding "has an OIFM code, description, and attributes (presence/absence, change from prior)" plus an optional `anatomicLocation` of `{locationId, locationDisplay}`. — the shape as the repo states it.
- example2 study §1.2: across all 276 EFL entries in `sample_data/example2`, the keys actually used are exactly `observationId`, `findingCode`, `findingDescription`, `attributes[]`, optional `anatomicLocation`, optional `reportText`; every `attributes[]` array has exactly one member and it is always `presence`. — what the implemented example actually carries, as against what the model allows.
- Board 4 ("OIDM Object Model"), class-diagram cluster: `Observation` with `id`, `code` (CDE Set ID), `body_site`, `tracking_id`, `components[]`; `Observation Value` with `code` (CDE Element ID) and `value`. — a typed class proposal including a tracking identifier.
- `OpenImagingDataModel.py` `main` `455e5b6`, `openimagingdatamodel/observation/observation.py`: `Observation` with `id`, `identifier`, `code`, `status`, `subject`, `bodySite`, `derivedFrom`, `component` as a discriminated union of codeable-concept / string / integer / boolean variants; the class docstring states "The Observation class is the model for FHIR Observation objects", and a code comment records a deliberate divergence, that "the FHIR spec has all fields optional, but we require system and code". — the 2024 reference implementation's shape.
- Site post "Findings, CDEs, and Observations", 2023-06-24: "Each `Observation` is labeled with a ACR/RSNA Common Data Element (CDE) Set ID to indicate what kind of finding it is, and the value for each attribute of the finding is labeled with a CDE Element ID." — the definition of "CDE-labeled".
- `IPL-MVP-ExtractionAndLabeling` `main` `b06948f`, `src/schemas.py`: the ancestor `Finding` model is two fields, `name` ("Lowercase finding name") and `present` (bool). `config.py` `EXTRACTION_SYSTEM_PROMPT` asks for "all radiologic findings mentioned" as `{"name", "present"}` pairs, listing pathological findings, anatomical variations, incidental findings and "Negative findings (explicitly stated as absent)". — the minimal starting point the current model grew from.

**What the code implements.** `src/finding_extractor/models.py` on IPL repo `dev` `36fa30c` defines the current extraction-side Observation as `Finding` with `finding_name`, `presence`, `location` (a separate `FindingLocation` of `body_region`, `specific_anatomy`, `laterality`), `attributes` (a list of open key/value `FindingAttribute`), `report_text` and `source_section`. `initial-extraction-plan.md` records why location is its own structure rather than an attribute: it is "**separate from other attributes** because location is often implied by the exam type rather than stated explicitly." The same plan records the decision to leave the attribute key open: constraining it "would reject valid but uncommon attributes."

**Related.** A2, A4, A12, A21, A25, C2.

**Unresolved.** The deck names measurements and lesion characteristics as attributes; example2 populates only presence. Whether the gap is a data-collection artifact or a model position is not stated in any source read.

**Undetermined.** No committed JSON Schema or Pydantic model for Observation exists in any repository read; `$schema` URLs in the sample files resolve to nothing (example2 study §1.2, IPL repo `main` `CLAUDE.md` "Schema Reference").

## A2. Two-level architecture: Exam Finding List, then Imaging Problem List

**Statement.** Findings are represented at two levels. The Exam Finding List (EFL) is the list of findings declared present or absent on one examination. The Imaging Problem List (IPL) is the patient-level aggregation of EFL observations across examinations into longitudinal entries. The JDIM manuscript states the reason: "A radiologist observes one examination at a time, but their judgments (is this new, is this the same finding) span examinations, so we designed the IPL as a two-level data model."

**Status.** Working proposal (manuscript, webinar, deck); implemented example (repo, sample data, viewers).

**Evidence.**
- JDIM IPL manuscript, Methods, "Structure of the Imaging Problem List", printed p.6: the two-level rationale quoted above, and "The first level is the Exam Finding List (EFL): the observations recorded on a single imaging examination."
- JDIM IPL manuscript, printed p.7: "The second level is the IPL itself: a patient-level aggregation of EFL observations across examinations into longitudinal finding entries."
- IPL repo `main` `06f64a7`, `README.md`: EFL is "In the context of an imaging exam, a list of the findings declared as present/absent on that exam"; IPL is "In the context of a patient, the list of findings that have been described as present/absent in exams of the patient." — the repository's own two-level statement, unchanged on `dev`.
- January 2026 deck, strategic pillar 2: "atomic Observation -> Exam Finding List -> IPL -> 'Imaging Persona'." — a four-level hierarchy, of which two levels are built.
- SIIM webinar slide 17 ("Two-level model") and slide 16 (pipeline: "reports → structured extraction → per-exam EFLs → temporal aggregation → the IPL → five downstream application families").
- IPL repo `dev` `36fa30c`, `scripts/generate_ipl_from_efls.py`: deterministic aggregation of all `*_efl.json` in a directory into one IPL, no model calls (example2 study §3.3).

**Related.** A1, A3, A5, C2.

**Unresolved.** The deck's hierarchy has four levels; the manuscript and repository define two. Imaging Persona (A16) is named only in the deck and the boards.

## A3. The faithful-translation constraint on the Exam Finding List

**Statement.** The EFL is a near one-to-one translation of what the radiologist asserted on one examination, with no comparison across examinations and no extrapolation beyond the report text. The webinar states the consequence: "nothing invented enters the foundation," which is what lets every derived layer be trusted without re-verification against the source text. The JACR manuscript states the same requirement for its extraction tool: "Our tool was built to transcribe, not interpret."

**Status.** Working proposal (manuscript, webinar); implemented example with a measured failure mode (JACR extraction tool); implemented example (verbatim-quote validation in the extraction platform).

**Evidence.**
- JDIM IPL manuscript, printed p.6: "The EFL is intended to be a near one-to-one translation of what the radiologist asserted on one examination, with no comparison across examinations and no extrapolation beyond the report text."
- SIIM webinar slide 17 speaker notes: "That is the source of trust: nothing invented enters the foundation… Put inference in the foundation and you contaminate everything above it."
- SIIM webinar slide 18 speaker notes: "nothing on the right exceeds the sentence it came from: no comparison across exams, no inference."
- JACR IPL manuscript, Discussion: "The record's fundamental building block, the extracted finding, has to stay true to what the board-certified radiologist said… inferring what the radiologist probably meant would introduce unpredictability into the extractions."
- JACR IPL manuscript, Results, "Extraction and matching validity": for at least 3.6% of findings (111 of 3,056) the tool supplied an assertion the radiologist did not write, recording lymph node enlargement for a neutrally stated measurement. The Discussion calls this out: "The label was technically correct, but the tool should still not have supplied the inference." — a measured violation of the constraint by the team's own tool, reported against itself.
- The extraction system prompt states the rule three times. `CORE_INSTRUCTIONS_BLOCK` item 5: "**When quoting report text, BE EXACT** — verbatim excerpts only, never paraphrase". `OUTPUT_FORMAT_BLOCK` closes with "Remember: QUOTE MUST BE VERBATIM. Do not paraphrase or summarize the report text." `CHUNK_RULES_BLOCK` item 6 requires the quote be "a substring copied from the TARGET CHUNK that supports the finding."
- `CHUNK_ROLE_BLOCK` sets an evidence boundary for the chunk sub-agent: "Work only on the TARGET CHUNK text. Adjacent context is advisory only and must not be used as extraction evidence." `prompts/validator_prompt_example.md` repeats it for the reviewer: "Evidence boundary: only REPORT_CHUNK is evidence; surrounding context is advisory."
- `initial-extraction-plan.md`, "Post-Extraction Validation", names the verbatim check as "the most common extraction failure mode", and its addendum promotes it from a post-hoc report to an enforcement point: an `@agent.output_validator` that raises `ModelRetry` so a paraphrase triggers a retry rather than a warning. The rationale is recorded as "the single biggest extraction-quality win."
- `docs/report-sections.md` records a design point that protects the rule: the auto-detected section hint "is placed **before** the report delimiters, so verbatim validation against the original text is unaffected."
- example2 study §1.2: every EFL observation carries `reportText`, a verbatim quote from the report Markdown.

**What the code implements.** Verbatim quoting is enforced at run time, not merely requested: IPL repo `dev` `36fa30c` `CLAUDE.md` records "Validated both as a PydanticAI output validator and post-hoc," and the reviewer's failure taxonomy has a `hallucination` category for "clinically meaningful content unsupported by the chunk text" (A26). `initial-extraction-plan.md` also specifies a coverage check that compares the union of every `report_text` and `non_finding_text.text` against the full report "to surface any text the agent skipped entirely," so the extraction accounts for the whole report rather than only the parts it recognized.

**Related.** A5, A8, A10, A23, A26, B2, B4.

## A4. Entry identity is the finding code plus the anatomic site

**Statement.** One IPL entry is one finding in one patient, identified principally by finding code plus anatomic site. A diagnosis or category the radiologist assigns, such as a LI-RADS category, is an attribute recorded on the observation rather than a separate identity, so a lesion whose category is revised stays one entry and the revision becomes part of its trajectory.

**Status.** Working proposal (manuscript); implemented example (the dev-branch grouping key).

**Evidence.**
- JDIM IPL manuscript, printed p.8: "Each IPL entry is one finding in one patient. Its identity rests principally on two fields, the finding code and the anatomic site… A diagnosis or category, such as LI-RADS LR-3, is the radiologist's interpretation, recorded on the observation, so a hepatic lesion whose LI-RADS category the radiologist revises on subsequent imaging stays one entry and the revision becomes part of its trajectory."
- IPL repo `dev` `36fa30c`, `CLAUDE.md`: the IPL "Groups observations by finding type **and** anatomic location (`locationId`) across exams… consumers key on the IPL finding `id`, not `finding_type_code`."
- IPL repo `dev` `36fa30c`, `scripts/generate_ipl_from_efls.py`, in-code comment: "A finding code at two distinct anatomic locations… becomes two separate IPL entries" (example2 study §3.3).
- example2 study §1.3: 123 IPL entries over 276 observations; every observation folded into an entry shares that entry's `{locationId, locationDisplay}` exactly, which follows mechanically from the grouping key.
- JDIM IPL manuscript, printed p.6: "A finer gradation the radiologist states, such as a BI-RADS assessment category, is recorded as an attribute of the observation."

**Related.** A2, A10, A12, A13.

**Unresolved.** Entry identity in the worked exemplar was still moving between sources. See A5's entity-count difference.

## A5. Status is derived from the observation history, never stored — and three vocabularies disagree

**Statement.** An entry's status is computed from its observation history by fixed rules and recomputed whenever the history changes, so no model judgment is stored as clinical fact and an application can tell what a radiologist stated from what the system computed. Trajectory is likewise a read of the history rather than a stored field. Three sources name three different status vocabularies.

**Status.** Working proposal (manuscript, webinar); implemented example (both viewers compute status; the second stores a precomputed copy).

**Evidence.**
- JDIM IPL manuscript, printed p.8: "The IPL entry status has one of four values programmatically derived from the observation history, recomputed whenever that history changes." Active = most recent observation present and new or changed; Stable = present and unchanged; Resolved = an earlier observation present and the most recent absent; Excluded = explicitly reported absent at some point and never observed present, "a tracked pertinent negative, such as 'no pneumothorax'" (printed p.9).
- JDIM IPL manuscript, printed p.9: "A reader or an application reads an entry's trajectory from its observation history… **The entry has no trajectory element of its own.**"
- JDIM IPL manuscript, printed p.11: "What the IPL then displays, from an entry's status to its trajectory, is computed by fixed rules from the linked observations, so no model judgment is stored as clinical fact."
- SIIM webinar slide 21 speaker notes: status is derived at read time with two top-level values mirroring "the clinical problem list's active/resolved model", and **within Active** a trajectory of "appearing, progressing, regressing, fluctuating", "the finer read from the measurements."
- IPL repo `main` `06f64a7`, `CLAUDE.md` "Temporal Status Tracking": three states — Present, Resolved, Not Present/Ruled Out — with filters All / Currently Present / Resolved / Ever Present / Ruled Out.
- IPL repo `dev` `36fa30c`, `CLAUDE.md`: "Tracks temporal status: currently present, resolved, never-present/ruled-out" — three states named.
- IPL repo `dev` `36fa30c`, `docs/plans/viewer-v2-anatomy-dashboard.md`, "Status Semantics": four values — `current`, `always`, `resolved`, `never_present`.
- example2 study §2.1 and §3.4: viewer v1's `computeFindingStatus` and `build_viewer_v2_data.py`'s `compute_status` implement the identical four-branch algorithm; v1 labels the fourth branch `never`, viewer_v2 labels it `never_present`; viewer_v2 also adds `unknown` for an entry with no observations. Viewer_v2 **stores** the result in `viewerMetadata.statusByFindingId` in its generated bundle rather than computing it in the browser.
- example2 study §1.3: the canonical `sample_data/example2/MRN0000001_ipl.json` has **no `status` field at all**.

**Related.** A2, A4, A7, B1.

**Unresolved — four attributed positions on status.**

| Source | Vocabulary |
|---|---|
| JDIM IPL manuscript (under review) | Active, Stable, Resolved, Excluded; no trajectory element |
| SIIM webinar, 2026-07-15 (public) | Active, Resolved; trajectory within Active: appearing, progressing, regressing, fluctuating |
| IPL repo `main` and `dev` `CLAUDE.md` prose | Present/current, Resolved, Never-present/ruled out (three) |
| IPL repo `dev` viewer_v2 plan and both viewers' code | current, always, resolved, never_present (plus `unknown` in code) |

**Unresolved — the exemplar entity count.** The same synthetic patient (64-year-old, cirrhosis, 15 exams, 4 modalities, 2017-2024) yields 223 observations in 41 entries in the JDIM manuscript abstract and 225 observations in 43 entries in the SIIM webinar (slide 24). `sources/bucket/REPORT.md` §7 attributes the difference to the webinar version splitting acute from healed rib fractures and acute L4 compression fracture from chronic L4 compression deformity into separate rows, where the manuscript keeps each as one entry with an internal acute-to-healed trajectory. This is an unresolved entity-identity rule, not a counting error.

**Undetermined.** Whether the deliberate storage of status in viewer_v2's generated bundle is a considered exception to "never stored" or a build-pipeline convenience is not stated in the viewer plan.

## A6. The succession link

**Statement.** One entry tracks one physical entity across its whole course. When a resolved finding leaves a different entity behind, the new entity gets its own entry and is connected to the resolved one by a succession link rather than mutating the original. The manuscript's example is a pneumonia and the residual scarring it leaves.

**Status.** Working proposal only.

**Evidence.**
- JDIM IPL manuscript, printed p.8: "The entry's succession link connects a resolved entry, such as a pneumonia, to the entry for the distinct finding it left behind, such as the residual scarring."
- JDIM IPL manuscript, printed p.9: "One entry tracks one physical entity in the patient across its whole course, including observations that report it absent. The scarring a pneumonia leaves behind is a different entity from the pneumonia, so it gets its own entry but is associated with the resolved pneumonia by a succession link."
- SIIM webinar slide 22 speaker notes: "the pneumonia Resolves, and its scarring enters as its own distinct entry rather than mutating the original."
- `sources/bucket/REPORT.md` §4: Figure 2 of the manuscript shows a dashed succession-link arrow from resolved pneumonia to its scarring sequela on the patient timeline.
- example2 study §1.4: "There is no succession/supersede/merge field anywhere connecting these two entries" — the implemented sample data has no succession link.

**Related.** A5, A7, A13.

**Undetermined.** Whether the acute-to-healed fracture case belongs to succession or to within-entry time course. The manuscript treats evolution as "the stated time course within one entry" (printed p.11); the webinar exemplar splits it into two entries (A5, entity-count difference).

## A7. Per-observation provenance and review status, and corrections as provenance operations

**Statement.** Each observation records where it came from, whether a radiologist has reviewed it, any change a radiologist made to what a model produced, and the original report text. For a model source, provenance records the model's identity and version, its inputs, its output, and any confidence it provides. Review status is "unreviewed" or "affirmed"; a later affirmation or rejection supersedes an earlier one with both retained. Merging entries, splitting an entry, and marking an observation in error are logged as provenance operations, not statuses.

**Status.** Working proposal (manuscript, webinar); a lineage precedent that overloads a different field; not implemented in the sample data.

**Evidence.**
- JDIM IPL manuscript, printed p.10: "Provenance records, for each observation, where it came from, whether a radiologist has reviewed it, any change a radiologist made to what a model produced, and the original report text… The review status is 'unreviewed' or 'affirmed'… A later affirmation or rejection supersedes an earlier one, with both retained in provenance. Observations within one entry may differ in source and review status, so each has its own provenance."
- JDIM IPL manuscript, printed p.9: "When two entries are discovered to be one finding, when one entry is determined to be two separate entities, or when an observation was entered in error, the record is corrected by merging, splitting, or marking the observation, and each correction is logged in provenance. Merging, splitting, and marking are provenance operations, not statuses."
- SIIM webinar slide 46 speaker notes: "every machine-generated observation is marked unreviewed until a radiologist affirms it; LLM is an enumerated provenance source, so this is not a bolt-on."
- IPL repo `main` `06f64a7`, `README.md`: the EFL specification asks that "each Observation should include some kind of provenance marker." No field is named.
- `FHIRSamples` `main` `9ae2fa9`: the same lung-screening finding appears twice, once as an AI observation with FHIR `status` `preliminary` and once as the radiologist's with `status` `final`, the resources otherwise identical — the only implemented precedent, and it overloads the FHIR `status` field rather than carrying a provenance structure.
- example2 study §2.2: "No clinical confidence, hedge, review-status, or provenance field exists anywhere in either viewer's data model or rendering code."
- IPL repo `dev` `36fa30c`, `README.md` "Extraction Persistence": the platform stores each extraction run with its report link, timestamp, model, reasoning setting and full JSON payload, and represents reviewer edits as correction objects (`add_finding`, `update_finding`, `comment`) — provenance implemented for the *extraction pipeline*, not for the IPL data structure.

**Related.** A3, A8, B2, B4.

## A8. Entity resolution is the open problem; graduated-confidence linking is the proposal

**Statement.** Matching observations across examinations is the unsolved step. Simple matching on finding code plus site suffices when a finding is the only one of its type at its location. For harder cases the team proposes graduated-confidence linking: a radiologist's explicit comparison to a specific prior makes a high-confidence link; code plus location plus temporal plausibility makes a medium-confidence link; spatial proximity alone makes a low-confidence link; below any threshold the observations stay separate entries. Both manuscripts state that a false split costs redundancy while a false merge corrupts a trajectory.

**Status.** Working proposal (linking model); implemented example (code-plus-site matching only); measured limitation (JACR).

**Evidence.**
- JDIM IPL manuscript, printed p.11: "The simplest linking logic is matching on code and site… This suffices when a finding is the only one of its type at its location: one aortic aneurysm, one instance of hepatic steatosis, one set of coronary artery calcifications. **The exemplar in Results uses this matching alone.**"
- JDIM IPL manuscript, printed p.12: the three confidence levels, verbatim as summarized above, and "When confidence is insufficient at any level, the observations would be kept as separate IPL entries."
- SIIM webinar slide 13: "report → extraction · solved → findings → same entity? · open → one tracked entity", with slide 23 speaker notes: "never a merge on weak evidence. A false split costs a little redundancy; a false merge corrupts a trajectory. Be honest that the current prototype links on finding code alone; matching is the open frontier."
- JACR IPL manuscript, Results: 181 of 2,232 findings (8.1%) "could not be matched to a single earlier finding", mostly where a patient had several findings of one type in one location; these receive no grade but stay in the denominator, making the reported burden a lower bound. "Deciding whether two descriptions name one finding or two is entity resolution."
- JACR IPL manuscript, Take Home Points: "The remaining implementation work is entity resolution, deciding when two descriptions on different CTs name the same finding."
- JACR IPL manuscript, Table 2: four ordered matching rules (Name, Site, Match, Ambiguity) plus a fifth for grading, each with its stated error direction; "Every matching rule fails toward keeping findings separate, because wrongly merging two findings manufactures a re-documentation."
- JDIM IPL manuscript, printed p.19: "The IPL is an application-layer data model over the CDE-labeled FHIR Observations… DICOM Structured Reports are a natural source of EFL observations, and the DICOM tracking identifier marks observations as referring to one finding without defining how they are matched, collected, or used."

**Related.** A4, A9, A13, A19.

**Unresolved.** The JACR rules and the JDIM graduated-confidence model are two different formulations of the same step, developed for different purposes (a locked measurement instrument versus a proposed linking model), and no source reconciles them.

## A9. One finding may be described by several observations in one report, and by different codes across reports

**Statement.** The same finding is often described more than once in a single report, in the findings section and again in the impression, and the EFL records one observation per finding per examination while preserving each sentence that contributed to it. Across reports, observations of one finding may use different but related codes: more or less specific terms, a diagnosis substituted for a finding or the reverse, or the entity's own evolution such as acute rib fractures becoming healed rib fractures.

**Status.** Working proposal (manuscript); measured difficulty (JACR); explicit direction from the project lead.

**Evidence.**
- Email notes, point 1: "The same finding is often described by more than one observation in a single report (findings section and impression). Found in the JACR chest CT work; aggregating observations into one or several findings was hard for the LLM. To be included in the manuscript."
- Email notes, point 2: "Observations of one finding across reports may use different but related codes: more or less specific terms; a diagnosis substituted for a finding or vice versa; the entity's evolution over time (acute rib fractures becoming healed rib fractures). **The manuscript should make clear how the IPL structure accounts for finding versus diagnosis.**"
- JDIM IPL manuscript, printed p.6: "A report may describe one finding twice, in the findings section and again in the impression. The EFL records one observation per finding per examination and preserves each sentence that contributed to it, so reconciling repeated descriptions within a report is part of producing the EFL."
- JDIM IPL manuscript, printed p.11: "The terms may be broader or narrower (a hepatic lesion on one report, a hepatic cyst on the next), substitute a diagnosis for the finding it rests on (pneumonia for consolidation), or follow the finding's evolution (an acute fracture, then a healed one). Evolution is the stated time course within one entry. Matching the other two would draw on the relationships among codes that a finding vocabulary defines, so that codes related at the vocabulary level can be matched at the patient level."
- JACR IPL manuscript, Methods, "Rules for aggregating findings across CTs": the worked emphysema case — "one patient's emphysema was called 'centrilobular paraseptal emphysema', then 'emphysematous change', then 'emphysema', then 'centrilobular emphysema'."
- example2 study §1.4: `ipl-finding-102` "pancreatic lesion" folds two separate EFL observations from the same 2021-08-26 exam (`pancreatic_lesion_0` and `pancreatic_mass_0`) into one entry — the implemented case of two observations of one finding in one report.
- SIIM webinar slide 42: the breast case, where at biopsy "the entity transitions from mass-as-observation to fibroadenoma-as-diagnosis" while remaining one entity across five exams.
- JACR supplement, S2, gives the study's operational definition: "An observation is what the radiologist sees on the image… A diagnosis is what the radiologist concludes those observations represent, and it is not itself visible"; the diagnosis attaches to the observation it interprets and carries the radiologist's stated confidence, so one abnormality is not counted twice.

**What the code implements.** The extraction prompt's `DEDUPLICATION_BLOCK` is the working resolution of the one-finding-many-observations problem inside a single report. It makes the body text primary ("The Findings (or Comment/Body) section contains the detailed descriptions. Extract all findings from there first"), extracts from the impression only what the body does not already carry ("**Impression: extract UNIQUE items only** — If the Impression/Conclusion contains a diagnosis or finding that has NO corresponding description in the body text, extract it as a finding… Do NOT re-extract findings already covered by a body-text finding"), records where each finding came from in a `source_section` field valued `findings`, `impression`, `both` or null, and settles conflicts in favor of the body: "**Body text is authoritative** — When a finding appears in both sections, use the body text for details… The body section has the specifics; the impression is a summary." A separate rule handles repetition within one section: "**One entry per distinct finding instance** — If the same finding is described in multiple paragraphs within the body text, extract it once using the most detailed description." `CHUNK_RULES_BLOCK` item 7 handles the opposite case, where one sentence names a general finding and then instances of it: extract "both the general finding and each specific instance, and apply this for both present and absent statements."

**Related.** A4, A8, A11, A23, A24, A26, and the finding-model vocabulary relationships covered by the semantic inventory.

**Unresolved — finding versus diagnosis.** Four positions are on record, none reconciled:
- JDIM IPL manuscript (printed p.8): a diagnosis is an attribute of the observation, not a separate identity.
- The project lead, 2026-09-19 (email notes, point 2): the structure's account of finding versus diagnosis is not yet clear enough and should be made explicit in the manuscript.
- IHE Imaging Diagnostic Report Phase II public-comment draft, as extracted on `RSNA/ACR-RSNA-CDEs` `next-gen-2026` (`knowledge/data-structures/ihe-idr-alignment.md` and its cited extract): positive clinical findings are FHIR `Condition`, negatives are `Observation`.
- The working default recorded in that same extract: "every assertion in a radiology report, diagnoses included, is encoded as an `Observation`", because "'consistent with pneumonia' is a radiologist's assertion, not an established clinical condition."
- The next-generation CDE vocabulary's worked example deck tags each observation FINDING / DIAGNOSIS / GROUPING and links them with report-plane edges `SUPPORTS` and `ASSOCIATED_WITH` (`sources/bucket/text/next-gen-reporting-schema.md`; `sources/bucket/REPORT.md` §6) — a fifth treatment, from the allied CDE workstream.

## A10. Presence is binary; confidence and hedging are a separate axis

**Statement.** Presence is present or absent. Confidence is definite or hedged, recording whether the radiologist committed plainly or professed uncertainty. The hedge is recorded on whichever assertion the radiologist softened, the finding's presence or one of its attributes, and the exact wording is preserved. The webinar states the design reason: a top-level "indeterminate" fuses which way the radiologist leaned with how firmly they said it.

**Status.** Working proposal (manuscript, webinar); a contrary implemented example.

**Evidence.**
- JDIM IPL manuscript, printed p.6: "Presence is present or absent, and confidence is definite or hedged, recording whether the radiologist committed plainly or professed uncertainty."
- JDIM IPL manuscript, printed p.7: "A hedge is recorded on whichever assertion the radiologist softened, whether the finding's presence ('possible pneumonia') or attribute ('likely acute'), and the preserved report text retains the exact words."
- SIIM webinar slide 19 speaker notes: "Rule 4 in particular: binary presence plus per-axis confidence is more faithful and more elegant than a top-level 'indeterminate', which fused which way the radiologist leaned with how firmly."
- SIIM webinar slide 20 speaker notes: "'Possible' hedges the presence axis: presence stays binary, the hedge is recorded per-axis; the stated chronicity (acute) is recorded as stated, never inferred."
- example2 study §1.2 and §1.4: the implemented sample data uses a **three-value** presence vocabulary — `present` (113), `absent` (160), `indeterminate` (3) — with no separate confidence field; "Indeterminate is a real third presence state… distinct from present/absent, and it participates in status computation exactly like `absent` does."
- JACR IPL manuscript, Outcomes: hedged findings are reported separately from the primary outcome (42 of 57 hedged chronic findings re-documented with no change, versus 951 of 1,229 unhedged).

**What the code implements.** The extraction prompt's `PRESENCE_BLOCK` defines a **four-value** presence vocabulary and, unusually, states the test for applying it. The values: "**present**: The finding is explicitly stated as present"; "**absent**: The finding is explicitly stated as absent (e.g., 'no ascites', 'normal hilar contours', 'unremarkable')"; "**indeterminate**: Cannot be determined from the report"; "**possible**: Hedged/uncertain language ('raising the possibility of', 'suggestive of', 'cannot exclude')". The test separates a hedged *observation* from a hedged *interpretation*: "When the imaging observation itself is definitively seen but the interpretive label uses hedging, the finding is **present** — e.g., 'decreased attenuation suggestive of fatty infiltration' → hepatic steatosis is **present** (the decreased attenuation IS observed)… When the finding/diagnosis itself is uncertain, use **possible**… Key test: Is the imaging observation definitively seen, or is the diagnosis itself uncertain?" This is the finding-versus-diagnosis distinction of A9 operating as a presence rule. `initial-extraction-plan.md` fixes the same four values as a `Literal` on the model so an out-of-vocabulary value fails validation.

**Related.** A3, A5, A9, A23.

**Unresolved — three positions on presence, not two.**

| Source | Presence vocabulary |
|---|---|
| JDIM IPL manuscript, printed p.6, and SIIM webinar slide 19 | Binary present/absent, with confidence definite/hedged as a separate per-axis value; an explicit argument against a fused top-level "indeterminate" |
| Extraction prompt `PRESENCE_BLOCK`, and `initial-extraction-plan.md` | Four values: present, absent, indeterminate, possible — where "possible" is hedging and "indeterminate" is "cannot be determined from the report" |
| example2 sample data (example2 study §1.2) | Three values in use: present, absent, indeterminate; no `possible` and no separate confidence field |

The extractor's split of "possible" from "indeterminate" keeps hedging distinct from unassessability, which is closer to the manuscript's intent than the sample data is, but it still puts both on the presence axis rather than a second one. No source states which vocabulary is meant to win.

## A11. Pertinent negatives are first-class entries

**Statement.** A finding the radiologist explicitly reports absent is recorded as an observation with presence absent, not omitted, and an entry that has only ever been reported absent is a tracked pertinent negative. A finding the report does not mention has no observation on that EFL at all, and adds nothing to its entry's status.

**Status.** Working proposal (manuscript, webinar); implemented example (the sample data is majority-absent).

**Evidence.**
- SIIM webinar slide 18 speaker notes: "Walk the pertinent negative first: 'no filling defect' is captured as pulmonary embolism, absent; negatives are first-class entries, not omissions."
- JDIM IPL manuscript, printed p.9: "'Excluded' means at some point the radiologist explicitly reported the finding absent and no other observation recorded it present (a tracked pertinent negative, such as 'no pneumothorax')."
- JDIM IPL manuscript, printed p.7: "A finding the report does not mention has no observation on that EFL." And printed p.9: "A report that does not mention a finding adds no observation to its entry, so the entry's status is unchanged."
- example2 study §1.2: of 276 observations in the sample data, 160 are `absent` — the majority.
- JDIM IPL manuscript, printed p.16: cross-subspecialty value depends on it — "that history, including what radiologists excluded on earlier examinations, is available without manual retrieval and could spare repeat examinations."
- SIIM webinar slide 20 speaker notes: on an absent row, "the stated temporal word marks the negation scope: 'no NEW consolidation' is not the same assertion as 'no consolidation.'"
- Board 1 (internal; schema content only), "Exam Finding List" table: rows for negative findings carry a count of 0 and are starred, with the report text highlighted in two colors for positives and explicit negatives.
- JACR IPL manuscript, Methods: by contrast the JACR study **excluded** statements of normality and analyzed positively reported findings only.

**What the code implements.** Negation is a first-class extraction target, not a filter. The extraction prompt's `CORE_INSTRUCTIONS_BLOCK` item 2 requires extracting "ALL findings — including present, absent, possible, and indeterminate findings". The coding prompts keep negation out of the concept: `FINDING_TERM_SYSTEM` rule 5 says "If a finding is a normal-variant or absent finding (e.g., 'no ascites'), generate terms for the finding itself (e.g., 'ascites', 'peritoneal fluid'), not for the negation", and `FINDING_CODE_SELECTOR_SYSTEM` rule 6 states flatly "The finding's `presence` does NOT affect code selection." The anatomic-location work applies the same separation: `docs/plans/anatomic-location-efl-ipl.md` records that "**Absent findings still get anatomy** — presence doesn't gate location ('No hydronephrosis' → kidney, 'adrenal glands are unremarkable' → adrenal)."

**Related.** A5, A3, A10, A23, A25.

**Unresolved.** The JDIM/webinar model makes explicit negatives first-class; the JACR measurement excludes normal statements. The two have different purposes and no source reconciles the scope difference.

## A12. Every finding carries a standardized anatomic location, assigned by explicit rules

**Statement.** Each observation is anchored to a single anatomic location identifier from the RadLex-derived Anatomic Locations index, and a written precedence ladder decides which location: explicit anatomy in the report text or section context wins; otherwise the finding's own target organ at its own anatomic-noun granularity; otherwise the exam-scoped coarse region. Laterality follows explicit text, then a sided exam, then generic, and is resolved against the whole report section rather than the finding's isolated quote.

**Status.** Working proposal (the written rules); implemented example (the enrichment pass and the coding pipeline).

**Evidence.**
- IPL repo `dev` `36fa30c`, `docs/anatomic-location-assignment-rules.md`: the three-step precedence ladder, the laterality source priority, the bilateral-finding rules (separable positives split into left and right; an inseparable diffuse process stays generic and unsided; a contiguous midline finding stays one unsided finding; a generic absent finding on a paired organ never takes a side), and the specificity rule that "the target's granularity matches the finding's anatomic noun, capped by the report — never finer." Includes the worked left-shoulder section-laterality example and the explicit warning that "reviewing or coding from the isolated `reportText` silently drops section laterality."
- IPL repo `dev` `36fa30c`, `docs/plans/anatomic-location-efl-ipl.md`, status header: COMPLETE 2026-06-10; "EFLs in `sample_data/example2` enriched with `anatomicLocation`… (260/275 localized)"; the locked decision that the indicator is "RID id + display name only… a single location per observation."
- example2 study §3.2: `enrich_efl_anatomy.py` runs each finding through the *production* coding pipeline `finding_extractor.coding.runtime.run_coding` rather than a sample-data heuristic, and writes a per-decision review CSV including unresolved cases.
- January 2026 deck, "Anatomic Locations": "Anatomy baked into OIFM definitions and Observation objects."
- SIIM webinar slide 31 speaker notes: "Every finding is anchored to a specific RadLex Anatomic Locations code, and the containment hierarchy rolls it up to a top-level body region."

**What the code implements.** The two location prompts encode the rules the assignment document states in prose. `LOCATION_TERM_SYSTEM` rule 2 keeps the anatomy separate from the finding: "Name the ANATOMIC STRUCTURE, not the finding. For a finding in the 'right lower lobe', the terms should be 'right lower lobe', 'lower lobe of right lung' — NOT 'right lower lobe opacity'." Rule 3 supplies the fallback when the report says nothing: "If location is null, infer from the exam info (body_part, modality) and report context." Rule 7 encodes a structural fact about the index that the anatomy work established: "When laterality is 'bilateral' OR the anatomy is inherently bilateral (e.g., 'lung bases', 'kidneys', 'adrenal glands'), generate SEPARATE terms for each side. The index stores lateralized entries individually — there is no entry for 'kidneys', only 'left kidney' and 'right kidney'." Rule 8 asks for a parent term one level up alongside the specific one, which is what makes a near-miss recoverable. `LOCATION_CODE_SELECTOR_SYSTEM` presents each candidate with its region, laterality, containment parent and part-of parent, so both hierarchies are visible at the moment of choice, and rule 4 states "LATERALITY MATTERS. Never select the wrong side."

The extraction prompt fixes a nine-value `body_region` vocabulary — chest, abdomen, pelvis, head, neck, spine, upper extremity, lower extremity, breast (`LOCATION_BLOCK`) — as a coarse axis beneath the free-text `specific_anatomy` that the coding step later resolves to an identifier. `ATTRIBUTES_BLOCK` keeps the axes from collapsing: "Do NOT use 'location' as an attribute key — location belongs in FindingLocation fields."

**Related.** A4, A13, A25, B1, and the anatomic-locations ideas in the semantic inventory.

**Unresolved — one location per observation, or several.** `docs/plans/anatomic-location-efl-ipl.md` records the locked decision as "a single location per observation", and instructs the enrichment pass that "If `run_coding` returns multiple `location_codes` for an observation, take the first/primary coded one to honor the single-location decision." But `LOCATION_CODE_SELECTOR_SYSTEM` rule 2 says "MULTIPLE LOCATIONS are allowed when a finding genuinely spans more than one distinct structure. Do NOT select redundant ancestor/descendant pairs," and `docs/coding-agent-prompts.md` Design Notes confirm the coding bundle carries `location_codes` as a list. The coding tool models a finding that spans structures; the Exam Finding List does not carry one.

**Undetermined.** The rules document says these "were agreed for the `sample_data/example2` correction pass and are the intended spec for tuning the automated location-coding step later"; whether they have been applied beyond example2 is not stated.

## A13. Anatomic-compatibility reconciliation is unresolved, and the sample data shows the cost

**Statement.** Because grouping keys on the exact location identifier, the same finding coded generically on one exam and specifically on another produces two unconnected entries. Deciding whether a generic-versus-specific pair for one finding code names the same problem is the anatomic-compatibility reconciliation step, and it has not been started.

**Status.** Stated open problem (the rules document names it and defers it); demonstrated failure in the implemented example.

**Evidence.**
- IPL repo `dev` `36fa30c`, `docs/anatomic-location-assignment-rules.md`, known-limitation section, quoted in `knowledge/roadmap/ipl-data-model-system.md`: "Parent/child or generic-vs-specific pairs for the *same finding code across exams* (e.g. 'lung' vs 'lower lobe of right lung'; 'kidney' vs 'left kidney') still produce separate IPL groups. Deciding whether such observations are the same problem or distinct is the **anatomic-compatibility reconciliation** step."
- IPL repo `dev` `36fa30c`, `docs/plans/anatomic-location-efl-ipl.md`: "**Follow-on:** Step 3b anatomic-compatibility reconciliation and the fresh anatomy-aware viewer remain future phases."
- example2 study §1.4, two live instances: renal cystic disease `OIFM_GMTS_016635` splits into `ipl-finding-046` at generic kidney `RID205` (one ultrasound observation whose text never states a side) and `ipl-finding-047` at left kidney `RID29663` (three CT observations), where the report text is visibly tracking one lesion's size across all four; and hepatic lesion `OIFM_OIDM_160831` splits into `ipl-finding-089` (segment 6, one observation) and `ipl-finding-090` (generic liver, four observations) including a 2023-01-18 sentence that explicitly refers back to the segment-6 lesion and still lands in the other group. "There is no succession/supersede/merge field anywhere connecting these two entries."

**Related.** A4, A6, A8, A12.

## A14. Permanent findings, and the need to rank entries before display

**Statement.** Some findings a patient is expected to have on every subsequent examination indefinitely — degenerative change, calcification, healed injury, congenital variant, biologically inert lesion, postsurgical change, implanted device, irreversible process, structural remodeling. Whether a finding is permanent is a declared attribute of the finding type, not something inferred from observing a series. Because most of an accumulated record goes unmentioned at any one examination, an IPL has to rank its entries before displaying them, and permanence is one measured signal for that ranking.

**Status.** Implemented example (a locked study taxonomy attribute with measured results); stated design implication.

**Evidence.**
- JACR IPL manuscript, Methods: "Permanent findings are those a patient is expected to have on every subsequent CT indefinitely, such as a healed rib fracture or postsurgical change, which distinguishes them from chronic findings followed for change such as an enlarging aortic aneurysm. **The label comes from the finding itself, not from observing the series.**"
- `sources/bucket/REPORT.md` §2 lists the nine declared permanent categories from the manuscript's taxonomy.
- JACR IPL manuscript, Table 3: 607 of 993 findings re-documented with no change were permanent (61.1%); 69 of 103 findings that dropped out of documentation and returned were permanent (67.0%); 371 of 765 new-to-series findings were permanent findings documented for the first time (48.5%).
- JACR IPL manuscript, Discussion: "Compiled from a patient's entire imaging history, most of the record goes unmentioned at any one examination. An IPL would therefore have to rank its entries before displaying them, and whether a finding is permanent is one measured signal for that ranking."
- JACR IPL manuscript, Table 3, IPL coverage at the fourth CT: the fourth report re-documented 19.1% (308 of 1,615) of the entries in an IPL built from the first three CTs; permanent entries were re-documented at 34.1%, nearly twice that rate.

**Related.** A15, B5, A22.

## A15. Foundation context: four per-finding dimensions that tell an agent what to expect

**Statement.** Four additional dimensions carried on a finding's definition — where it is anatomically, what type of finding it is (a hierarchical, multi-valued etiology taxonomy), how long it lasts, and whether it is transient or permanent — are what let an agent judge whether a finding should still be present on a new examination. The webinar states these belong to a forward schema and are not carried by the published definitions.

**Status.** Stated direction (webinar), attributed to a forward schema rather than the committed corpus.

**Evidence.**
- SIIM webinar slide 28 speaker notes: "the committed, published finding model is lean: 2,458 definitions with id, name, description, synonyms, tags, attributes, and index codes. None of the four foundation-context dimensions are first-class fields there. FindingModelFull is the forward schema that adds them… these fields are the forward, AI-populated schema, not yet carried by the published definitions." Slide text names `body_regions · anatomic_locations`, `entity_type · etiologies`, `expected_time_course`, `subspecialties · applicable_modalities`, `sex_specificity · age_profile`.
- SIIM webinar slide 29 speaker notes: "this tells an agent whether a finding should still be there. Expect the AAA on every future exam and track its growth; treat a resolved PE as gone; know the ovarian cyst clears and recurs with the cycle so you don't link every cyst into one thread."
- SIIM webinar slide 30: the etiology taxonomy, hierarchical and multi-valued, listed verbatim — `inflammatory`, `inflammatory:infectious`, `neoplastic:{benign,malignant,metastatic,potential}`, `traumatic:{acute,sequela}`, `vascular:{ischemic,hemorrhagic,thrombotic,aneurysmal}`, `iatrogenic:{post-operative,post-radiation,device,medication-related}`, `degenerative`, `metabolic`, `congenital`, `developmental`, `autoimmune`, `toxic`, `mechanical`, `idiopathic`, `normal-variant`; "a subdural hematoma is both traumatic:acute and vascular:hemorrhagic."
- example2 study §3.5 and §2.2: `viewer/data/enriched_findings.json` (97 entries) already carries `body_regions[]`, `modalities[]`, `subspecialties[]`, `etiologies[]` as `"category:subtype"` strings and `anatomic_location{id,text}`, and viewer_v2's "Definition data" panel renders them — a partial implemented instance of the forward schema, for 97 of the finding codes used.

**Related.** A8, A14, B1, and the finding-model metadata ideas in the semantic inventory.

**Undetermined.** This inventory did not read the `findingmodel` repository; the relationship between `FindingModelFull` and the metadata-cleanup work belongs to the semantic inventory.

## A16. Imaging Persona and the reporting data context object model

**Statement.** Beyond the patient's imaging findings sits the surrounding clinical context. The January 2026 deck names it Imaging Persona with four categories: clinical context (orders, indications), medical baseline (problem list, allergies, laboratory results), specialized history (oncology, treatments), and surgical history (operative records, pathology, implants). Two boards give the same idea a fuller, differently named shape as an object model spanning Patient, Order, ImagingStudy, CurrentReportText, PriorReports, TrackedObservations, EHR Data, and Observations.

**Status.** Stated goal (deck); working proposal (boards); no schema, sample, or code.

**Evidence.**
- January 2026 deck, "Imaging Persona (big picture)": the four categories verbatim.
- January 2026 deck, strategic pillar 2: Persona is the fourth level of the hierarchy after the IPL.
- Board 4 ("OIDM Object Model", low sensitivity), central mind map: branches Patient (identifiers, DOB, sex/gender, referrer), Order (indications, order questions and responses, timestamps, imaging studies), PriorReports (report text, observations), TrackedObservations (observation types, observations), EHR Data (lab values, pathology reports, problems/diagnoses, allergies, operative notes, clinical notes), ImagingStudy(s) (identifier, resource information, DICOM metadata, timestamps), CurrentReportText (status, authors, "Text (DOM)", timestamps), Observations (identifier, observation type as a CDE Set ID, tracking ID, body part, components). Hand annotations map Patient/Order and EHR Data to FHIR, ImagingStudyType to the LOINC/RadLex Playbook, and BodyPart to Anatomic Locations.
- Board 9 ("OIDM Big Picture"), "Reporting Data Context Object Model" frame: nine fields — patient demographics, order information, EHR information (problem lists, labs, vitals, operative notes, pathology), current report, prior radiology reports, longitudinal findings, AI-generated data, DICOM-SR data, NLP-extracted data. The board states this frame is a duplicate of Board 4's mind map.
- Board 14 ("ACR OIDM", low sensitivity), Reference Implementations component list names "Tracked Observations" as a first-class component alongside Anatomic Locations, Exam Types, CDE Sets/Elements, Observations, Imaging Exams, Imaging Reports and EMR Items.
- Site post "Data Model: Structure and Function", 2024-01-25: the model organizes observations, current report text, imaging studies, patient, order, prior studies, tracked observations, and EHR data.
- Board 1 (internal; schema content only): proposes representing non-imaging clinical data in the same structure — "Implants; Operations — e.g., appendectomy, if there's a record of it can add it to the IPL under the same semantic identifier that would be used when a radiologist describes post-appendectomy findings in an abdomen CT report."

**Related.** A1, A17, B8, C2.

**Unresolved.** Three names for overlapping things: "Imaging Persona" (deck), "OIDM Data Context Model" / "OIDM Object Model" (Boards 4 and 9), "Reporting Data Context Object Model" (Board 9). No source states whether these are the same structure.

**Undetermined.** Storage versus query-time assembly, ownership of each context category, encoding, and maintenance are unspecified in every source read.

## A17. Report sections beyond Findings are unmodeled

**Statement.** The finding/Observation pattern covers the Findings section. Impression, diagnoses and differential diagnoses, recommendations, communication, comparison, technique, clinical history and indication, and limitations are enumerated as sections that also need representation, with the open question of whether impression-level statements are Observations too or a distinct structure that links back to finding Observations.

**Status.** Stated open questions, recorded on a board; nothing built.

**Evidence.**
- Board 6 ("Structured Report Representation", internal; schema content only), note "2025-03-06 Report Structures to Represent": the eight sections listed verbatim, with "Findings (already covered)".
- Board 6, "Impression" box: the impression is "usually a numbered/bulleted list, often ordered by priority/severity", "can reference findings by number or implicitly", "may state a diagnosis or differential rather than restating a finding directly", and "can group multiple findings under one summary statement."
- Board 6, note "2025-04-09": "Should Impression items be OIDM Observations too, or a different structure entirely (linking back to Finding Observations)? Need a way to represent 'grouped' findings with a common cause/diagnosis. Causative relationships between findings?"
- Board 9, "Report Representation" work thread: "Have good FHIR structure for simple findings — working on more complex situations: Complex/associated findings, Diagnoses based on findings, Differential diagnoses, Recommendations."

**What the code implements.** A canonical section vocabulary exists and is used, even though only two sections yield findings. `docs/report-sections.md` gives seven canonical names with their aliases: `findings` (aliases comment, body), `impression` (conclusion), `technique`, `indication` (clinical information), `clinical_history` (history), `comparison`, and `recommendation` (clinical correlation). Detection is "best-effort, deterministic" regex over header patterns in priority order, using "a **whitelist approach** to avoid matching subsection headers like `**Liver:**` or `**Lungs:**`" — so body-system subheads inside the findings section are deliberately not mistaken for report sections. The detected structure is persisted with the report and backfilled lazily for reports stored before the feature existed.

`docs/extraction-internals.md` records the consequence: "extraction proceeds only on `findings` and `impression` sections", with an inference step for reports that have no findings header ("infers an implicit findings block immediately before first impression when plausible"). Everything else in the report is not discarded but classified: the extraction prompt's `NON_FINDING_BLOCK` assigns each remaining span one of seven categories — metadata, technique, indication, comparison, clinical_history, impression, other — and `initial-extraction-plan.md` states the purpose: "This lets us account for every piece of text in the report — findings go into `ExtractedFinding.report_text`, everything else goes here." So the sections Board 6 lists as unrepresented are, in the implementation, recognized and labeled but not yet turned into structure.

**Related.** A9, A18, A26, C2.

## A18. Recommendation structure, and a live-versus-closed axis on IPL entries

**Statement.** A follow-up recommendation is a structure of its own: the exam (possibly with protocol, with anatomy important), a timeframe, the finding or target with optional conditionality, and a citation such as Fleischner, the ACR incidental-findings papers, or a *-RADS system. When a recommended finding is an IPL entry the recommendation attaches to that entry and the radiologist closes it when a later examination shows resolution. One board proposes the IPL itself as the display surface, with entries that are "live" versus "inactive/not being acted on/closed."

**Status.** Working proposal (board, manuscript); stated goal (deck's ACR priorities); nothing built.

**Evidence.**
- Board 12 ("Outcome Tracking Schema", no named individuals), "Recommendation Structure" box: "Exam (possibly w/protocol) — Anatomy important here; Facilitate 'one-click to close' (1C2C); Timeframe; Finding/target (± Conditionality, options); Citation (e.g., Fleischner, ACR IFs, *-RADS, etc.)."
- Board 12, "Recognizing Follow-up Exams": "Facilitated orders could have a flag on them indicating they're a response to a recommendation. A given recommendation definition could have the idea of which kinds of exams would be appropriate for closing it."
- Board 12, "Imaging Problem List" box (starred): "Captures findings. Can have the idea of things that are 'live' versus those that are inactive/not being acted on/closed."
- JDIM IPL manuscript, printed p.15: "When a finding recommended for follow-up is an IPL entry, the recommendation is attached to that entry, and the radiologist can close it when a later examination shows resolution. While the finding persists, its observation history is the dated list of examinations a radiologist checks against an external surveillance protocol, such as the Fleischner Society intervals."
- JDIM IPL manuscript, printed p.16: "Because both the recommendation and its closure are in the IPL record, a department could measure follow-up completion from the record instead of by chart abstraction or keyword search."
- January 2026 deck, ACR priorities: recommendation tracking named first.

**Related.** A5, A14, B5, B7.

**Unresolved.** Whether "live versus closed" is a second status axis on an entry or a property of an attached recommendation. Board 12 puts it on the entry; the JDIM manuscript attaches the recommendation to the entry and keeps status derived from observations alone.

## A19. A finding as a persistent tracked entity with a durable identifier

**Statement.** Rather than recomputing groups, each finding becomes a tracked entity with an identifier that persists, so a later report of the same lesion adds a dated value to the existing resource instead of creating a new one. The lineage design note states it plainly: "Each finding becomes a **tracked entity** with a FHIR ID that persists."

**Status.** Working proposal on an unmerged branch of a superseded prototype; the same idea appears as a `tracking_id` field on the object-model board and as a multi-vendor exchange requirement on a demo board; the current implementation approximates it by grouping instead.

**Evidence.**
- `IPL-MVP-ExtractionAndLabeling`, branch `origin/Persistent_FHIR_Resources` `5ea6720`, file `FHIR_Example_Structure` (no extension): a three-step process — extract and map to OIDM codes; for each finding ask "Does this finding already exist in our FHIR database?" and either link and add a new observation value or create a new Observation with a unique ID; then query and visualize. Worked timeline: one liver lesion at 1.6 cm (2022-05-10), 2.1 cm (2022-11-15), 2.8 cm (2024-10-15), each with a `status` of `new` or `growing`. Example queries: "Show me the timeline for liver lesion."
- Board 4, class diagram: `Observation` carries `tracking_id` as a field.
- Board 15 ("Pulm Nodule Demo Project", internal; schema content only), Complete Workflow step 4: "Ideally, prior known nodules is actually a series of Observation objects, all with a common tracking ID." Step 5 asks: "Who adds the tracking ID to the Observation, and how does this get communicated."
- JDIM IPL manuscript, printed p.8: "The entry's tracking identifier links its observations across reports"; printed p.19: the DICOM tracking identifier "marks observations as referring to one finding without defining how they are matched, collected, or used."
- Site post "Data Model: Structure and Function", 2024-01-25: "**Tracked Observations**: An index of the association of the same radiology finding (e.g., a tumor or a fracture)" — the idea in prose, two years before the design note.
- `FHIRSamples` `main` `9ae2fa9`, `example1OIDMradiologist.json`: the finding Observation's `focus[]` carries a body structure and an imaging selection that share the **same** DICOM structured-report `tracking-uid` identifier, with the selection giving study, series and instance identifiers plus an image region. The same-lesion identity mechanism here is a DICOM tracking UID tied to a place on an image.

**What the code implements.** The `FHIR_Example_Structure` note's store is not FHIR and does not claim to be. It is a patient-keyed local JSON document whose keys are invented strings such as `fhir-obs-liver-lesion-001`, each holding the finding name, a SNOMED code, a first-detected date, and an observation list of `{report_date, size_mm, status}` with `status` values `new`, `persistent` and `growing`. Identity across reports is decided by matching the finding name together with the location text, framed in the note as the question "Have we seen a hepatic lesion in segment 8 before?" The note proposes two supporting services, an "OIDM MCP" for mapping a phrase to a standard code and a "FHIR Resource Manager" that it labels "not a real server, just local database."

**Related.** A4, A8, A21, B9.

**Unresolved — two unconnected designs for the same problem.** `FHIRSamples` identifies one lesion across observations with a DICOM tracking UID anchored to an image region; the `FHIR_Example_Structure` note identifies it with an invented string key in a local store, matched on name plus location text. Neither references the other, and the JDIM manuscript's "tracking identifier" (printed p.8) names the function without picking a mechanism. Who owns and assigns the identifier is an open question on Board 15 and is answered nowhere read.

**Unresolved — three coding targets in one family.** The IPL repository codes findings with OIFM identifiers; the `FHIR_Example_Structure` note codes them with SNOMED; `FHIRSamples` and `OpenImagingDataModel.py` code them with RadElement `RDES`/`RDE` identifiers. The RadElement system URI is itself inconsistent across the lineage samples, appearing as `https://radelement.org` and `https://www.radelement.org`, with two misspelled variants in `CDETemplateDemo` `e09f255`. These are lineage artifacts rather than positions, but any statement that the structures carry "a finding code" has to say which.

## A20. A formal system of data models with generated schemas

**Statement.** The structures should exist as annotated Pydantic models from which JSON Schemas are generated, with camelCase aliases on export and snake_case attributes internally, covering Observation (with an Extracted Observation subtype raised as a question), Exam Finding List, and Imaging Problem List.

**Status.** Stated goal, unclaimed by any plan.

**Evidence.**
- `openimagingdata/imaging-problem-list` issue #1, "Create System of Data Models", opened by the project lead, still open with no comments and no assignee as of this reading: "Needs models for: Observation — Extracted Observation sub-type?; Exam Finding List; Imaging Problem List. Pydantic. Extensive annotation to generate JSON schemas. camelCase aliases in export, snake_case object attributes."
- Project lead's stated goals, `knowledge/plans/2026-09-20-knowledgebase-build-plan.md`, Imaging Problem List: "Define appropriate data structures for representing both observations in radiology reports and their relationships"; "Create standard data structure formats, etc. for working with these."
- IPL repo `dev` `36fa30c`, `docs/plans/anatomic-location-efl-ipl.md`, grounding facts: "There is **no Pydantic model or committed JSON schema** for the EFL format, so adding a field is purely additive."
- example2 study §1.2: the `$schema` value in the EFL files points at `https://github.com/openimagingdata/imaging-problem-list/schema/exam-problem-list-schema.json`, which IPL repo `main` `CLAUDE.md` states "doesn't exist yet."

**Related.** A1, A2, A21.

## A21. Application-layer data structures, distinct from transport expressions

**Statement.** OIDM defines a system of data structures for representing imaging exam result information, intended to be used inside applications to both read and create result data. These are not a transport definition: not FHIR, not DICOM. They may eventually need FHIR expressions to travel, and should be designed to allow that, but that is separate from the definition of the structures applications manipulate. Agreeing the structures is what makes it easier to agree what must be conveyed between systems, and the structures guide the design of the FHIR profiles that inter-process communication will require.

**Status.** Explicit direction from the project lead (2026-09-19) and a decision of record (2026-09-21); already partly expressed in the manuscript under review; contradicted by the current repository documentation.

**Evidence.**
- Email notes, point 3: "'Application layer data model' is imprecise. Better: 'a system of defined data structures for representing imaging exam result information', 'intended to be used within applications to both read and create result data'."
- Email notes, point 4: "The structures are NOT a transport definition (not FHIR, not DICOM). They may eventually need FHIR expressions to travel over FHIRcast, and should be designed to allow that, but that is completely separate from the definition of the structures applications manipulate."
- Email notes, point 5: "Agreed structures make it easier to agree on what must be conveyed between systems… The structures GUIDE the design of the FHIR profiles and related artifacts that will need agreement for inter-process communication. This is the motivation for the IPL."
- `knowledge/plans/2026-09-20-knowledgebase-build-plan.md`, "Decisions added 2026-09-21", row "Data structures versus transport": records this as the project's position and directs that the data-structure documents be reframed.
- JDIM IPL manuscript, printed p.7: "The IPL is an application-layer data model: the data structures that applications read and write to represent a patient's imaging findings, **defined independently of any transport protocol**. When systems exchange the record, those structures can be expressed in FHIR, and each element of the model can be carried by a FHIR Release 5 resource (Table 1)… Storage representation, location, versioning, and exchange with reporting, archive, and electronic health record systems are implementation choices. An implementation may store the record in relational, document, or graph form."
- JDIM IPL manuscript, printed p.18: "Shared data structures come first. When systems hold the same structures, what must pass between them to convey a patient's findings is easier to agree on, and the structures guide the FHIR profiles that exchange will require. We offer this model as a starting point for an open, community-developed standard."
- January 2026 deck, call to action: "structure-first (then FHIR etc.)."
- Site post "Data Model: Structure and Function", 2024-01-25: OIDM is "a superstructure on top of these FHIR definitions to both organize them and enable more straightforward programmatic access to the data"; "the relationship between OIDM and FHIR might be that between the browser's DOM and HTML."

**Related.** C1, C2, C3, A22.

**Unresolved — the term itself.** The manuscript under review uses "application-layer data model" in its abstract, its Methods (printed p.7), its Discussion (printed p.19) and its Limitations (printed p.19). The project lead on 2026-09-19 calls that phrase imprecise and proposes replacing it. The manuscript's own gloss already says "defined independently of any transport protocol", so the disagreement is over the label, not obviously over the content.

**Unresolved — the FHIR mapping itself.** Two mappings are on record for the IPL:

| Source | IPL FHIR expression |
|---|---|
| IPL repo `main` `06f64a7` and `dev` `36fa30c`, README and `CLAUDE.md` | "**Report** containing a list of **Condition** objects (labeled with the finding identifier), where each Condition object also contains a list of **Observation** objects" |
| JDIM IPL manuscript, Table 1 (image page 88 of the PDF), as summarized in `sources/bucket/REPORT.md` §4 | EFL observation → `Observation` (CDE-labeled); examination report → `DiagnosticReport`; anatomic site → `BodyStructure`; IPL entry → `List` (or a custom profile); succession link → a `Reference` between Lists or an extension; status → none, derived only; review status → `Provenance` |

"Report" is not a FHIR resource name. Neither mapping is implemented: IPL repo `dev` `36fa30c` has no FHIR resource classes and no code that emits FHIR (`knowledge/data-structures/fhir-mapping.md`, "What is actually implemented").

**Unresolved — components versus hasMember.** OIDM's attribute encoding uses `Observation.component` throughout (IPL repo `main` README; `FHIRSamples` `9ae2fa9`; `OpenImagingDataModel.py` `455e5b6`). The IHE Imaging Diagnostic Report Phase II public-comment draft states `Observation.component` "is not used" and routes elements through `hasMember` instead, while the January 2026 deck names IDR as the EFL's target ("Connects to IHE Imaging Diagnostic Report (IDR) FHIR representation"). Recorded in `knowledge/data-structures/ihe-idr-alignment.md` from the extract on `RSNA/ACR-RSNA-CDEs` `next-gen-2026`; unresolved.

## A22. The re-documentation burden: measured evidence for the Imaging Problem List

**Statement.** A two-site study of 200 serial chest CTs measured how much of a follow-up report re-documents findings an earlier report in the same series already described, and what depth of memory an IPL would need to supply it.

**Status.** Implemented study with results (prepared for submission).

**Evidence.** All from the JACR IPL manuscript, Results and Table 3; 50 patients, four consecutive chest CTs each, two academic sites, report text only, extraction validated against radiologist review.

| Measure | Result |
|---|---|
| Findings on follow-up CTs that were chronic | 57.6% (1,286/2,232), 95% CI 54.5-60.8 |
| Chronic findings asserted without hedging, re-documented with no change (primary outcome) | 77.4% (951/1,229), 95% CI 73.3-81.4 |
| Of content re-documented with no change, share permanent | 61.1% (607/993) |
| Follow-up findings an IPL built from the whole series would account for | 44.5% (993/2,232) |
| Follow-up findings the most recent report alone would account for | 26.7%, at most 31.1% |
| Findings tracked on two or more CTs that dropped out and returned | 18.9% (103/545), two-thirds permanent |
| Fourth-CT findings an IPL built from the first three already lists | 49.6% (308/621) |
| IPL entries the fourth report re-documented | 19.1% (308/1,615) |
| Extraction confirmed against the source report | 98.3% (1,153/1,173) |

Additional evidence: the taxonomy "is built on the Open Imaging Data Model finding vocabulary" and sites were "mapped against the Anatomic Locations index, a RadLex-derived anatomic reference" (Methods), so the study is also a use of the semantic foundation. The supplement (`sources/bucket/text/jacr-ipl-supplement.md`) states the taxonomy is "built on the Open Imaging Data Model chest CT finding taxonomy, with the codes this study added" and that the rule set, taxonomy and analysis code "will be made available in a public repository at publication."

**Related.** A8, A14, B5.

**Undetermined.** Both manuscripts are unpublished. The JACR one carries no manuscript number or cover letter, so its submission status is not confirmed by the file itself.

## A23. Normality is recorded as an absent abnormality

**Statement.** A report sentence saying a structure is normal is not empty of findings. It is translated into the corresponding abnormality, marked absent. "Clear lungs" becomes a pulmonary parenchymal or airspace abnormality, absent; "normal cardiac silhouette" becomes cardiomegaly, absent. A statement covering a whole region at once is a blanket negative, and it must be scoped to an abnormality the sentence actually excludes rather than to an unrelated or over-specific one.

**Status.** Implemented example, encoded in three prompts and given a named failure mode.

**Evidence.**
- Extraction prompt `CORE_INSTRUCTIONS_BLOCK` item 4, "**Normal findings are absent abnormalities**", with three worked mappings: "'clear lungs' → 'pulmonary airspace abnormality', absent"; "'normal cardiac silhouette' → 'cardiomegaly', absent"; "'normal lung volumes' → 'pulmonary volume abnormality', absent".
- `CHUNK_RULES_BLOCK` item 3: "If a structure is described as normal, encode the corresponding abnormal finding as absent. For example, 'clear lungs' implies an absent pulmonary parenchymal abnormality finding."
- `PRESENCE_BLOCK` treats normality wording as a plain absent assertion: absent means "explicitly stated as absent (e.g., 'no ascites', 'normal hilar contours', 'unremarkable')".
- `prompts/validator_prompt_example.md`, user-prompt template: "Explicit negatives should be represented as clinically meaningful absent findings; blanket negatives should map to appropriately scoped absent findings (e.g., 'clear lungs' -> {'finding_name': 'pulmonary parenchymal abnormality', 'presence': 'absent'}), not unrelated or over-specific absent findings." The reviewer's problem taxonomy includes `incorrect_blanket_negative` as one of seven named failure types.
- `FHIRSamples` `main` `9ae2fa9`, `chest_ct_report/findings.md`: the hand extraction records "Consolidation / Absent", "Pleural effusion / Absent", "Pneumothorax / Absent" and star-marks "Pericardium / Normal: No effusion, no thickening, no calcs" as a model apparently missing — the same idea reached by hand in 2024, and the same vocabulary gap.
- `IPL-MVP-ExtractionAndLabeling` `main` `b06948f`, `config.py` `EXTRACTION_SYSTEM_PROMPT`, already asks for "Negative findings (explicitly stated as absent)".

**Related.** A11, A9, A24, A26.

**Unresolved.** The idea has a vocabulary cost that no source resolves: it requires a coded abnormality to exist for every structure a radiologist can call normal, at the right scope. The `FHIRSamples` hand extraction star-marks exactly such gaps, and the `definition_mismatch` and `no_candidate_match` rejection reasons in the coding prompts (A24) are designed to surface them, but nothing states who fills them.

## A24. Coding aims at convergence, so generalizing is allowed and specializing is not

**Statement.** The point of assigning a code is that descriptions referring to the same clinical concept end up with the same label, whether they appear in one report, across one patient's reports, or across patients. That goal makes the two directions of error asymmetric. A slightly more general code is acceptable and often preferred, because it groups equivalents. A more specific code is never acceptable, because the report did not assert that specificity and using it fragments what should be one group. When nothing fits, the finding is left uncoded with a reason, rather than forced.

**Status.** Implemented example, stated as the explicit purpose inside the coding prompts.

**Evidence.**
- `FINDING_TERM_SYSTEM`, opening: "The goal of this process is to assign a common standardized label to all descriptions that refer to the same clinical concept — whether they appear in the same report, across reports for one patient, or across different patients. This means terms should target the general concept, not report-specific details. Being too specific defeats the purpose of grouping equivalent findings together."
- `FINDING_TERM_SYSTEM` rules 2 and 3: "Prefer slightly MORE GENERAL terms over more specific ones… for '3 mm nonobstructing left renal calculus', good search terms would be 'renal calculus', 'urinary tract calculus', 'kidney stone' — NOT 'nonobstructing renal calculus' or '3 mm kidney stone'"; "NEVER propose terms that are MORE SPECIFIC than the extracted finding name. Specificity beyond what the report states risks matching the wrong concept."
- `FINDING_CODE_SELECTOR_SYSTEM` rules 2 and 3 apply the same asymmetry at selection: "A SLIGHTLY MORE GENERAL candidate is acceptable and often preferred… 'urinary tract calculus' is a good match for 'renal calculus' — it groups all urinary stones under one label, and the specific location is captured separately"; "A MORE SPECIFIC candidate is NOT acceptable. 'Staghorn calculus' is NOT a valid match for 'renal calculus' — the report does not assert that level of specificity, and using it would fragment what should be a single group."
- `FINDING_CODE_SELECTOR_SYSTEM` rule 5, refusing to force a match: "If NO candidate is a reasonable match, return null for oifm_id. Do not force a match. An unresolved finding is better than a wrong code." The rejection must be classified as `too_specific`, `too_broad`, `wrong_concept`, or `definition_mismatch`, the last defined as "the candidate's NAME looks like a match, but its description, synonyms, or tags reveal a more specific or different concept than the name suggests."
- `LOCATION_CODE_SELECTOR_SYSTEM`, "Unresolved Reasons", makes the same distinction for anatomy: `no_candidate_match` ("you know where the finding is located, but none of the candidates adequately represent that structure") versus `location_unknown` ("you cannot determine where the finding is located even after considering the report context and exam type").
- `docs/coding-agent-prompts.md`, Design Notes, states what the reasons are for: `no_candidate_match` "flags index gap"; `definition_mismatch` "flags ontology entries needing cleanup". The refusal is a feedback channel into the vocabulary, not only a null.
- `FINDING_TERM_SYSTEM` rules 6 and 7 bound the generalizing: do not generalize to "pure meta-categories like 'finding', 'disease', or 'pathology'… The broadest acceptable term should still name a recognizable clinical concept. Prefer 'abnormality' when generalizing an observation"; and "For FOCAL findings, 'lesion' is the standard generalizing term — a lesion is a focal abnormality. Do not use 'lesion' for diffuse processes."
- `prompts/validator_prompt_example.md` guards the same boundary from the extraction side, with `over_specific_finding_name` among its problem types and the instruction that names "should not be more specific than the chunk supports."
- `docs/coding-agent-design.md` records that a deterministic fast path runs first: an exact or synonym hit in the finding index or the anatomic location index resolves without any model call, so the model is consulted only for what the index did not already settle.

**Related.** A3, A8, A9, A23, A25, and the finding-model index in the semantic inventory.

**Unresolved — technical language.** The two coding prompts pull opposite ways on modality-specific wording. `FINDING_TERM_SYSTEM` rule 8: findings in technical language "should be searched using the technical observation term itself — do not reinterpret as a specific diagnosis or pathological process." `FINDING_CODE_SELECTOR_SYSTEM` rule 8: "When the finding is described in modality-specific technical language (e.g., 'hypodense lesion', 'T2 hyperintense focus'), match based on the underlying clinical concept, not the imaging technique." `docs/technical-imaging-findings.md` sides with the first, warning that "Marrow signal abnormality' should be searched as exactly that — it is the observation. Do NOT reinterpret as 'bone marrow edema' or 'marrow infiltration', which are specific diagnoses that may or may not be the cause." Whether the selector is meant to strip only the modality wrapper or to resolve to a diagnosis is not stated.

## A25. Finding type, anatomic site, and presence are independent axes

**Statement.** What a finding is, where it is, and whether it is present are coded separately and do not condition each other. The type code answers what, the location code answers where, and presence rides on neither.

**Status.** Implemented example, stated as rules in the coding prompts and realized in the pipeline's shape.

**Evidence.**
- `FINDING_CODE_SELECTOR_SYSTEM` rule 7: "Match based on WHAT the finding is, not WHERE it is. Anatomic location is coded separately." Rule 6: "The finding's `presence` does NOT affect code selection."
- `LOCATION_CODE_SELECTOR_SYSTEM` rule 1 mirrors it from the other side: select the candidates "that best represent WHERE the finding is located".
- `docs/coding-agent-design.md`: the pipeline runs finding-code selection and location-code selection as "**parallel LLM calls** within the same concurrency semaphore", each with its own term generator, and `docs/coding-agent-prompts.md` Design Notes record that "A finding can resolve via fast-path on one axis but not the other," so the two axes are tracked independently per finding.
- The extraction prompt keeps the axes apart in the data too: `ATTRIBUTES_BLOCK` forbids "location" as an attribute key, and `initial-extraction-plan.md` makes `FindingLocation` a separate structure rather than one more attribute.
- `docs/plans/anatomic-location-efl-ipl.md`: "presence doesn't gate location" — an absent finding still receives anatomy.
- JDIM IPL manuscript, printed p.8: entry identity rests on the finding code and the anatomic site together, which is only well defined if the two are coded independently (A4).

**Related.** A1, A4, A12, A24.

## A26. A named taxonomy of extraction failures, checked by an independent reviewer

**Statement.** Translating prose into structure has specific, nameable ways of going wrong, and the system checks for them with a second model that reviews each chunk against its source text and can send that chunk back for re-extraction. The failures are enumerated: content asserted that the text does not support, a finding in the text with no structure representing it, the wrong presence, a name more specific than the text supports, a mishandled blanket negative, and wrong or wrongly scoped location.

**Status.** Implemented example.

**Evidence.**
- `prompts/validator_prompt_example.md`, system prompt, lists the "issue patterns that justify re-extraction" verbatim: "extraction structure contains clinically meaningful content unsupported by the chunk text (hallucination)"; "some report text describing a finding is not represented by any extraction data structure (missed finding)"; "a structure describes a finding as being present when it is not, or absent when it is possible (wrong presence)"; "finding name is more specific than described in the chunk text (too specific finding name)"; "incorrect representation of a blanket negative (incorrect blanket negative)"; "wrong or too-specific or general location information (incorrect location)". The structured response uses the type vocabulary `hallucination`, `missed_finding`, `wrong_presence`, `over_specific_finding_name`, `incorrect_blanket_negative`, `incorrect_location`, `other`.
- The same file bounds the reviewer's remit: "Do not request re-extraction for formatting/style differences alone", and the user template tells it "do not perform a fresh extraction" — it judges, it does not replace.
- The reviewer's decision object is one per chunk: `report_chunk_id`, `should_reextract`, `problems[]` each with a finding index, a problem type and a detail, and a `rationale`.
- `docs/extraction-internals.md`, "Reviewer Contract", records an independence requirement in configuration: the reviewer model is "optional override; **must differ from extraction model**". Reviewer feedback "is threaded to retry chunks and appended to the chunk extraction prompt", and "Review timeout is non-fatal — pipeline continues without re-extraction."
- `docs/extraction-internals.md`, chunking: sentence spans are computed first; short sections pass through whole; an impression with list structure is chunked deterministically by grouped list items; otherwise semantic grouping with a sentence-group fallback; a default cap of three sentences per chunk. Each chunk is handed to the sub-agent with preceding and following half-chunk context marked advisory.

**What the code implements.** IPL repo `dev` `36fa30c` runs extraction and review as a per-chunk pipeline with bounded concurrency, so a chunk can be reviewed while other chunks are still being extracted, then merges and deduplicates across chunks before optional whole-output validation (`docs/extraction-internals.md`, "End-to-End Pipeline" and "Stage Status Sequence"). The named stages are preflight, sectionize, extract_exam_info, extract_sections, review, merge_dedupe, validate_output, persist, then completed, completed_with_warnings or failed — and `completed_with_warnings` is a distinct terminal state, so an extraction that raised concerns is neither silently accepted nor thrown away.

**Related.** A3, A23, B2, B4.

---

# Part B. Applications and uses

## B1. The Imaging Problem List viewer, and anatomy as presentation only

**Statement.** Two viewers exist. The first navigates IPL → EFL → report with status and body-region filters. The second is an anatomy-first dashboard: an abstract body-map schematic with burden shown as fill intensity, laterality shown spatially in radiological orientation, and drill-down from region to organ cluster to exact location to finding to observation. Its governing rule is that the viewer trusts the IPL: "Each IPL `finding.id` is the canonical clinical problem row. Anatomy grouping is presentation-only and must never merge or split IPL findings."

**Status.** Implemented example (both deployed); working proposal (the redesign plan's later slices).

**Evidence.**
- IPL repo `main` `06f64a7`, `CLAUDE.md` "IPL Viewer Application": three-level navigation, temporal status tracking, status and body-region filtering, multi-patient support, dark-mode-first "designed for radiologists".
- IPL repo `dev` `36fa30c`, `docs/plans/viewer-v2-anatomy-dashboard.md`: the trust rule quoted above; the status semantics; the anatomy precedence ladder (IPL location first, then index metadata, then cluster config, containment ancestors only as a fallback, `unlocalized` otherwise); the four laterality buckets `left`, `right`, `midline_nonlateral`, `generic_unspecified` with "Generic/unspecified findings must not be folded into left/right counts"; the body-schematic redesign with its explicit record of why the first stacked-card layout failed; and "Anatomy clustering is deterministic presentation metadata. It is not clinical reconciliation."
- Same plan, finding-detail requirement: the detail must separate **instance data** (actual location, status, observations, dates, report evidence) from **definition data** (description, synonyms, typical anatomy, modalities, subspecialties, etiologies, ontology codes) from **anatomy data** (RID, region, cluster, laterality, containment path).
- example2 study §2.2: the implemented `MetadataSections` panels match that three-way separation; drill-down state is mirrored into the URL query string so any view is a shareable link; evidence highlighting is strict Unicode-normalized exact substring matching with an index map back to the unmodified report text, and a miss surfaces as a warning "rather than silently failing or approximating."
- example2 study §2.2: the generated bundle's `manifest.json` carries exactly 7 build-time warnings — 2 `missing_anatomy`, 4 `evidence_not_exact`, 1 `missing_definition` — surfaced in the UI. These are QA signals about the bundle, not clinical confidence.
- SIIM webinar slides 26 and 33: both prototypes driven live by attendees; slide 33 speaker notes name "the honest edge, the banner admitting two findings have no specific anatomy location."
- January 2026 deck: demo at `https://imaging-problem-list.pages.dev`.

**Related.** A5, A12, A13, B5.

**Unresolved.** The two viewers diverge on same-exam duplicate observations: viewer v1 merges them into one row per `report_id`, viewer_v2 lists each separately (example2 study §2.2). Neither behavior is stated as the intended one.

**Undetermined.** `viewer/data/` is not example2: it holds a pre-anatomy 98-entry bundle for the same patient, no script on `dev` writes to it, and 0 of 288 finding entries there carry `anatomicLocation` (example2 study §2.1). Whether the deployed v1 is meant to be retired is not stated.

## B2. The report extraction, coding, persistence and review platform

**Statement.** The dev branch is a working platform that takes report text to coded findings and keeps the human in the loop: chunked multi-provider LLM extraction with verbatim-quote validation, a separate coding step, SQLite persistence with reports deduplicated by content hash and every extraction run stored with its model and settings, reviewer corrections as first-class objects, asynchronous job processing, an API, a batch CLI, and a reviewer UI.

**Status.** Implemented example.

**Evidence.**
- IPL repo `dev` `36fa30c`, `README.md`: providers OpenAI, Anthropic, Google, OpenRouter, Ollama, vLLM; the persistence section (SHA-256 report dedupe; each extraction run stored with report link, timestamp, model, reasoning setting, full JSON payload; corrections as `add_finding`, `update_finding`, `comment`); the Taskfile command surface; the batch extraction CLI.
- IPL repo `dev` `36fa30c`, `CLAUDE.md` "Architecture Notes": chunked extraction with bounded concurrency and a reviewer sub-agent that "can flag issues and trigger targeted re-extraction of specific chunks"; verbatim quote validation; "Post-extraction coding pipeline: After extraction, a separate coding agent maps findings to standardized OIFM codes. This is a distinct step from extraction"; TaskIQ workers over a Redis broker; API returns 202 plus a job ID.
- IPL repo `dev` `36fa30c`, `docs/human-review-workflow.md`: the gold-extraction workflow — batch-generate one candidate extraction per report, human reviewers overread and correct, corrected files become the gold set.
- SIIM webinar slide 16 speaker notes: "the extractor shown is one implementation of many. Many groups will build their own harness; what they share is the data model it targets." — an explicit statement that the platform is not the contribution.

**Related.** A3, A7, B3, B4, C1.

## B3. Coding is an independent job, decoupled from extraction

**Statement.** Assigning OIFM finding codes and anatomic location codes is a separate job from extraction. Extraction output persists without codes; coding is triggered separately and can be re-run with different models or settings. It runs as a five-phase pipeline over the flat merged finding list: fast-path index lookup, parallel LLM term generation for findings and locations, batched index search, parallel per-finding LLM selection, and assembly, with each phase degrading non-fatally.

**Status.** Implemented example with a written design rationale.

**Evidence.**
- IPL repo `dev` `36fa30c`, `docs/coding-agent-design.md`: "Coding assigns OIFM finding codes and anatomic location codes to extracted findings. It is an **independent job** — fully decoupled from extraction." The five phases; the non-fatal per-phase design ("One finding's failure does not block other findings"); four separate prompts; tuned parameters `SEARCH_LIMIT = 6`, `MAX_CANDIDATES = 12`, `MAX_CONCURRENCY = 8`, each with a stated prototype-testing justification; and "Dropping full report text from term generation prompts produced identical results with 22% fewer input tokens."
- IPL repo `dev` `36fa30c`, `docs/plans/anatomic-location-efl-ipl.md`: the location-coding prompt rule that "If location is null, infer from the exam info and report context", and that "presence does not affect coding" — absent findings still get anatomy.
- example2 study §3.2: the sample-data enrichment pass reuses the production coding runtime rather than a one-off heuristic, and works around its name-based grouping by spreading repeated finding names across slots so each observation is coded from its own report text.

**Related.** A12, B2, and the finding-model index ideas in the semantic inventory.

## B4. Honesty-first evaluation of extraction

**Statement.** An extractor evaluation that scores throughput and raw yield cannot distinguish a real recall gain from fabrication. The redesign makes the primary matcher quote-first, scores attribute *values* rather than only keys, freezes run configurations, keeps per-case artifacts, and uses adjudicated gold files rather than reviewed extractor output as the source of truth.

**Status.** Stated direction with a recorded descope decision; version one scoped, not yet reported as implemented.

**Evidence.**
- IPL repo `dev` `36fa30c`, `docs/plans/extractor-evals-redesign.md`, descope note dated 2026-07-07: "recent model-selection rounds (e.g. 2026-05-14, which made gemma4 the local default on '67s avg + 30% more findings') score throughput and raw yield, and cannot distinguish recall gains from fabrication." The plan was "deliberately **descoped rather than discarded**" after 3.5 months with zero implementation, because "The full plan's ceremony… is what made it unstartable."
- Same document, "Current Problems To Fix": the smoke dataset is in-sample because it is built from few-shot prompt examples; "Current gold is too close to reviewed extractor output in the extractor's own schema"; "Attribute scoring only checks keys, not values"; matching applies presence/location/attribute bonuses before those same fields are scored, "which can hide semantic errors."
- Same document, Core Decisions: "Source of truth is adjudicated gold in `*.gold.v1.json` files, not raw `*.extracted.json` output"; gate and benchmark sets "must both be held out from prompt examples."

**What the code implements.** The instrument for producing that gold is a deliberately primitive one. `docs/plans/extraction-reviewer-ux.md` describes `extraction_reviewer/` as "the standalone, single-file HTML review tool — no server, no install, no network at run time," and `docs/plans/extraction-reviewer-workflows.md` records that its vanilla-JavaScript, no-CDN build is "a **sanctioned exception**" to the project's own frontend convention because "the offline `file://` zero-install requirement justifies it" — the tool has to run on a reviewer's machine wherever the reports are. A reviewer walks findings one at a time with keyboard verdicts of approve, flag or unsure, logs findings the extractor missed by highlighting the supporting text in the full report, and exports one review file per extraction. A later round added structured flag targets so a reviewer names which field is wrong rather than only writing a comment: finding name, presence, anatomic site, laterality, size, severity, extent, temporal status, hedged language, and lumps-multiple.

The workflows plan states the intended path from review to gold: a converter applies a review file to its source extraction, passing approved findings through, surfacing flagged ones for correction, and turning missed findings into stubs to fill in, with the result finalized by an adjudicator and ingested by the evaluation harness. That chain, "the reviewer→converter→import-gold pipeline," is named "the documented source-of-truth path for gold."

**Related.** A3, A26, B2.

**Undetermined.** The gold file schema is open: the workflows plan records that the evaluation plan "names `*.gold.v1.json` but doesn't fix the schema; proposal is 'extraction schema + adjudication provenance fields.'"

## B5. Six downstream application families for the Imaging Problem List

**Statement.** The same record supports report pre-population, incidental-finding surveillance, chronic-disease monitoring, cross-subspecialty awareness, quality surveillance and research cohorts, and a breast-imaging case.

**Status.** Stated design implications awaiting evaluation (manuscript's own words); the webinar presents them as a roadmap.

**Evidence.**
- JDIM IPL manuscript abstract: "Pre-populated chronic findings, follow-up tracking, cross-subspecialty awareness, and a substrate for artificial intelligence (AI) reasoning are **design implications awaiting evaluation**."
- JDIM IPL manuscript, printed p.15, "Report Efficiency": "A reporting system built on the IPL could pre-populate confirmed chronic findings for the radiologist's review, so that dictation, or an artificial intelligence (AI) draft, focuses on what is new or changed."
- JDIM IPL manuscript, printed p.15, "Follow-Up Tracking and Safety": "Of lung nodules recommended for follow-up imaging, 40-60% do not receive it on time, and some of those lost to follow-up progress to advanced-stage cancer."
- JDIM IPL manuscript, printed p.16: cross-subspecialty awareness (the adrenal nodule seen on a chest CT five years earlier), and "The IPL and the clinical problem list are complementary: one tracks what imaging observes over time, the other what clinicians diagnose and manage."
- JDIM IPL manuscript, printed p.14-15: "identification for research, quality assurance, and education. The applications that follow are examples of what the model could enable."
- SIIM webinar slides 36-41: the six families named and given one slide each — report pre-population (slide 37: draft opens with each finding flagged pre-filled or new, "Interpretation, not inventory"), incidental-finding surveillance (slide 38: "report content, not exam code, decides completion… same exam code, opposite outcomes"), chronic-disease monitoring (slide 39: "True growth rate: frequent f/u masks it"), cross-subspecialty awareness (slide 40, with per-organ rules and "4.1% of recs avoidable with all priors"), quality surveillance and research cohorts (slide 41).
- SIIM webinar slide 35 speaker notes: ">1.5 M new incidental lung nodules/yr (Gould 2015)… 40-60% of recommended follow-up never happens."
- January 2026 deck, "IPL across imaging life cycle": planning (MRI safety, mobility, pre-authorization); intra-exam (rules-based protocoling); interpretation (findings-oriented PACS views, real-time quality control); post-interpretation (passive screening, research, outcomes).
- Board 1 (internal; content only), "Imaging Problem List" overview box: "MRI safety checks; Protocoling; Interpretation process — Draft report generation, PACS integration, Point-of-care report quality checks; Coding/billing; Drive EMR-side care pathways (CDS hooks); Data mining; Differential displays of reports: specialists, patients; Population health monitoring."

**Related.** A14, A18, B6, B7, B8, B11.

## B6. Breast imaging: one entity across assessments, and an automated MQSA audit

**Statement.** A breast mass tracked as one IPL entity across five examinations and eighteen months, its BI-RADS assessment moving 0 → 3 → 4A → biopsy → 2, with the marker clip becoming a durable re-identification anchor. Two applications are proposed on that record: presenting the IPL to the radiologist while reading, and an automated outcomes audit built from the BI-RADS assessment and any pathologic cancer diagnosis within one year — the data the federally required Mammography Quality Standards Act audit is built from.

**Status.** Stated as planned work, not results, by the source itself.

**Evidence.**
- SIIM webinar slide 42, "Breast IPL": the five-exam sequence with dates and assessments verbatim; "At biopsy the entity transitions from mass-as-observation to fibroadenoma-as-diagnosis, and the marker clip becomes a durable re-identification anchor on every future exam. **Present as planned work, not results;** the monitoring agent is later scope."
- SIIM webinar slide 43 speaker notes: the display-at-interpretation application with its design path ("focus groups with breast radiologists, then iterative usability testing toward a pilot"); and the audit — "for every screening exam the IPL already holds the BI-RADS assessment and any pathologic cancer diagnosis within one year: exactly the data the federally required MQSA audit is built from. Today that audit mixes semi-automated and manual steps, and many facilities audit only mammography; an IPL-derived audit runs continuously across mammography, ultrasound, and MRI. **Present as planned work: design, not results.**"

**Related.** A4, A9, B5, B7.

## B7. Outcome tracking, follow-up completion, and radiology-pathology correlation

**Statement.** A design for closing the loop between what a radiologist reported and what later happened to the patient: what a "future clinical event" record needs, patient factors kept deliberately separate from EHR data, an escalating cascade from per-case feedback up to population statistics, notification and worklist actions, and concrete use cases including diagnostic-yield auditing of the *-RADS systems, feedback to ordering providers, and interventional-radiology outcomes. A companion board works the imaging-to-biopsy-to-pathology link and proposes a shared tracking identifier across imaging Observation, procedure note and pathology report.

**Status.** Working proposal on internal boards, grounded in a published quality-measure article; one named demo project in a governance board; nothing built.

**Evidence.**
- Board 12 ("Outcome Tracking Schema", no named individuals, moderate sensitivity as unpublished design): the "Future Clinical Event" event types (imaging, pathology, operations and procedures, endoscopy/arthroscopy, diagnoses and problem-list items, lab tests, death, registry data, disposition, therapeutic) and result information; the patient-factor box annotated "Keep patient factors separate (from EHR and other sources)" covering demographics, risk factors, medical conditions, socio-economic factors, connectedness with the healthcare system and technology, and allostatic load; the six-step "use cases cascading" from identifying outcome data up to "Track pathways: incidental detection → follow-up study → biopsy/surveillance → treatment → morbidity → survival"; the Actions box (notify leadership/supervisor, notify radiologist immediately or by periodic digest, notify provider or patient of follow-up that has not occurred, create a registry, put on a work queue or dashboard).
- Board 12, "Specific Use Case examples": recommendation completion tracking; "auditing of diagnostic yield of malignancy-related RADS (BI-RADS, PI-RADS, TI-RADS, LI-RADS, Lung-RADS)"; trainee draft-to-final significant-change notification; continuous AI monitoring at aggregate and provider level; ordering-provider feedback on diagnostic yield; IR outcomes.
- Board 12 cites Kadom et al., "Novel Quality Measure Set: Closing the Completion Loop on Radiology Follow-up Recommendations for Noncritical Actionable Incidental Findings", *J Am Coll Radiol* 2022;19:881-890 — a real external source not referenced anywhere in the current bundle.
- Board 7 ("Radiologist Outcome Feedback", internal; schema content only): use cases for outcome tracking (personal performance review, training and education, quality improvement and peer review, research); interface options (passive, active query, aggregate dashboards); the "Path Result ↔ Biopsy Procedure" note — "Could use a shared tracking ID across imaging Observation → procedure note → pathology report."
- Board 14 ("ACR OIDM", low sensitivity), Demo Projects: "Outcome tracking demo" named alongside the templating and pulmonary-nodule demos.
- Board 1 (internal; content only): the cross-source integration idea — assembling an ED visit, a CT finding, an operative note, a pathology finding and a subsequent CT sequela under one concept such as "appendicitis", described as "Multiple channels that feed into a master, integrated knowledge base."

**Related.** A18, A19, B5, B11.

## B8. The reporting assistance framework: a context object model plus a plugin container

**Statement.** A reporting tool hosts plugins in a container. The container supplies an OIDM-defined data context object and accepts a fixed set of commands from the plugins, re-running every plugin whenever the context changes. Two sources give the command list at different depths.

**Status.** Stated goal (deck's applications pillar, named "Open Imaging Reporting SDK"); working proposal (the 2023 site post and the board slide); one working rendering precedent; no container implementation.

**Evidence.**
- January 2026 deck, strategic pillar 3: "Applications: Open Imaging Reporting SDK (vendor-driven innovation); demo apps: IPL Browser, early draft-generation tools."
- Site post "OIDM-Based Next-gen Reporting Assistance Framework", 2023-07-16: plugins written in a language such as JavaScript; the container supplies current findings, prior reports and the exams being reported; plugins issue four kinds of command (insert generated text, request information from the radiologist, alert the radiologist to a problem, send data to an external system); the container re-runs every plugin whenever context changes.
- Board 9 ("OIDM Big Picture"), "Reporting Assistance Framework" frame (described in the transcription as a polished, presentation-quality slide, not hand-drawn): **nine** commands — insert text into report; add/change data in data context; prompt radiologist for data; get EMR data elements; alert radiologist to quality issues; show radiologist images/findings; activate communication tools; package/send data to EMR/registries; request inference on images — against the **nine-field** Reporting Data Context Object Model listed in A16.
- Board 9, "SDK Development" work thread: "Multi-vendor shared work to define the structure of 'apps'; Need defined data structures, program interfaces; Incorporate other defined information; Model is web browser DOM."
- Board 9, "Next-Generation Assisted Reporting Use Cases" mind map (also present on Board 13): branches AI Tool Integration, Quality Checks (coding/MIPS checks; language and structure checks including left/right errors, sex-phenotype errors, anatomy-based errors, report length versus norms, findings-versus-diagnosis placement, undesirable phrases such as "cannot exclude"; "Is asked question answered?"), Specialized Reporting Applications, External Applications, Smart References, Facilitate/Automate Workflows, Report Generation, Longitudinal Reporting, Radiologist Situational Awareness.
- `CDETemplateDemo` `master` `e09f255`: a working web service that flattens a CDE-labeled FHIR Observation into template data keyed by component display name, derives boolean flags including presence and absence, and renders a Mustache text template; sample observations and templates are added as files under `mapper_ui/public/`. The one working precedent for a plugin that inserts generated text, and it uses no language model.
- openimagingdata.org About page, last modified 2023-06-21: programming interfaces promised in TypeScript/JavaScript, Python and C#. `knowledge/applications/reporting-sdk.md` records that the first two became lineage repositories and no C# library was written.

**What the code implements.** `CDETemplateDemo` `master` `e09f255` is the working slice of the "insert generated text" command, and its presence handling is the interesting part. `mapper-logic/src/mappers/jsonToObservation.ts` validates an incoming Observation and flattens its components into a lookup keyed three ways — by element code, by lowercased display name, and by capitalized display name — and `obsToMustache.ts` additionally sets each value string as a boolean flag so a template can branch on it. The commit named "Better presence handling (w/samples)" added a special case: when the component is presence, it sets `presence_present` and `presence_absent` booleans, and the sample template wraps the descriptive sentence in one and adds "There is no pneumothorax." under the other. So one coded Observation and one template render either an affirmative sentence or its negation, which is the rendering counterpart of A11 and A23.

**Related.** A11, A16, A17, A23, B5, C2.

**Unresolved.** The 2023 post names four commands; Board 9's slide names nine. No source states which supersedes the other. The post's own wording is that assistance "would take the form of standard commands generated by the scripts back to the reporting environment, which could then insert generated text into the existing report, ask the radiologist for additional information, alert the radiologist to a particular problem, or send data to an external system", with plugins authored "in a standard programming language, like JavaScript", and the container re-running them because "As the report context changes (more AI data comes in, the radiologist updates the report manually), the reporting tool would re-run each script with the updated data context so it could take appropriate actions."

**Unresolved — no global presence element.** The presence element identifier is per CDE set: `RDE1717` for pulmonary nodule in `FHIRSamples` `9ae2fa9`, `RDE421` for pneumothorax in `CDETemplateDemo` `e09f255`. Any tool that wants to find "the presence element" of an arbitrary set must therefore do what Board 15's "CDE Role Standard Tagging" proposes (B9), and nothing yet does.

**Undetermined.** The project lead confirmed the SDK is concept only; no repository, package, issue or branch for it was found (`knowledge/applications/reporting-sdk.md`, "Status first").

## B9. A multi-vendor interoperability demonstration exchanging CDE-labeled FHIR Observations

**Statement.** A named demonstration project — pulmonary nodules — in which an EHR vendor, reporting vendors, AI vendors and PACS vendors exchange pulmonary-nodule findings encoded as CDE-labeled FHIR Observations over FHIRcast, with a seven-step workflow from AI-generated nodule description through radiologist acceptance, report incorporation, retrieval of prior known nodules, association, and return of both text and Observation objects to the EHR.

**Status.** Working proposal on an internal board; named as a demo project in the governance board; no implementation found.

**Evidence.**
- Board 15 ("Pulm Nodule Demo Project", internal; schema and workflow content only, vendor-partnership framing omitted). Title: "RSNA/ACR AI In Practice Demo Project: Pulmonary Nodules!" Subtitle: "Exchange of radiology findings encoded as CDE-labeled FHIR Observations." Four vendor-role categories are given (EHR, reporting, AI, PACS), each with named example companies; the organizations are recorded in the source and are not reproduced as partnership claims here.
- Board 15, "Basic Principles": "Everywhere, we send data structured as FHIR Observations (including ontology codes). Exchanging everything as FHIRcast."
- Board 15, Complete Workflow, steps 1-7 as transcribed, including step 4's shared tracking ID (see A19) and step 5's open questions about who associates new nodules with prior ones and who adds the tracking ID.
- Board 15, "Smart Annotations": a PACS viewer infers which CDE Set a radiologist is characterizing from the annotation tool used and the anatomy under it, elicits the remaining elements the Set defines, and sends a FHIR Observation with the Set ID and components tagged with element IDs over FHIRcast.
- Board 15, "CDE 'Role' Standard Tagging": use standard SNOMED/RadLex tags on element definitions to mark an element's role or purpose (presence, location, size with its several measures, volumes, segmentation data, modality-specific measures such as radiodensity, echogenicity and MR signal, contrast behavior), so that a viewer needing "the volume element" can find the element carrying SNOMED 118565006 rather than hardcoding element IDs per Set.
- Board 14 ("ACR OIDM"), Demo Projects: "Pulmonary nodule demo (RSNA IAIP project)" and "Templating project (SIIM Hackathon)".
- Board 1 (internal; schema content only): the parallel exchange sketch in which a reporting vendor sends a structured finding list with the report result, an EHR vendor maintains the patient's imaging findings repository and exposes an imaging-problem-list view at interpretation time over FHIRcast, and the reporting vendor reads it back to display history, generate report text and check reports; with the open question of which FHIR resource the EHR should send back ("borrow/adapt FHIR structures for real problem lists? Condition resource?").

**Related.** A19, A21, B8, C3.

**Unresolved.** Board 1 records the IPL maintenance question as genuinely open: EMR-maintained versus dynamically generated by an Assembler service versus cached; "how do we make sure the IPL is dynamically generated, updated/not stored, and cached."

## B10. Local-only operation for protected health information

**Statement.** The extraction platform supports local and on-premises model providers so that protected health information need not leave the institution, with a local-only mode that has been hardened and whose remaining work is shelved behind explicit reopen triggers.

**Status.** Implemented example plus a stated-direction backlog.

**Evidence.**
- IPL repo `dev` `36fa30c`, `README.md`: Ollama ("local models, no API key needed") and vLLM ("OpenAI-compatible deployments") as first-class providers, with `.env.ollama.example` and `.env.vllm.example` at the repository root.
- IPL repo `dev` `36fa30c`, `docs/archive/local-only-mode.md`, `docs/archive/local-only-mode-hardening.md` (archived, i.e. completed) and `docs/plans/local-only-future-tightening.md` (active).
- `knowledge/roadmap/ipl-data-model-system.md`, "Local-only operation": "Protected health information stays on local models, with remaining hardening items shelved behind explicit reopen triggers."
- JACR IPL manuscript, Methods: "The same code and the same language model ran at both sites on each institution's approved deployment" — the practical constraint the local-model work serves.

**Related.** B2, B4.

## B11. The use case catalog and the six value categories

**Statement.** A catalog of application ideas, each tagged with one or more of six value categories taken from the RSNA Reporting Informatics Committee's use-case work: reporting efficiency, care team communication, operations/quality/safety, research, public health, education. The catalog was to grow into per-case files with defined metadata; it never did.

**Status.** Implemented example (the catalog exists and is complete as far as it goes); stated but abandoned process.

**Evidence.**
- `UseCases` `main` `71a90d2`, `Index.md` and `README.md`: the entries and the six value categories, reorganized without additions in `knowledge/history/use-cases.md`. Last commit 2024-02-26; four of the seven headings (Protocoling System, AI Pipeline, PACS Viewing, Data Exploration) are placeholders with no entries. Entries contributed by the RSNA Reporting Informatics Committee are marked as such in the source.
- Board 13 ("OIDM Use Case Brainstorming", no named individuals): the same Value Categories table, confirmed matching; the process questions ("What information should be captured as part of a use case? Do we want a text or data-based format (JSON)?"; "Create a GitHub repository for these?"); the planned artifacts (a README base document with metadata and submission guidelines, an Index.md, per-category directories); the six category axes (workflow/list oriented, AI pipeline oriented, reporting oriented, image-viewer oriented, data exploration/outcome oriented, multi-category); and a circled "Medico-legal Issues" note attached to the "Multiview Reporting" cluster (radiologist view, PCP view, specialty-oriented views, patient view).
- January 2026 deck, next steps: "use-case pipeline -> CDE group" — the catalog's intended downstream consumer.

**Related.** B5, B7, C3.

---

# Part C. OIDM's purpose and the relationship among its parts

## C1. OIDM's stated purpose

**Statement.** The project's own statements of purpose, in order of date: the site describes it as "defining unified data structures to integrate new functionality into imaging informatics platforms"; the January 2026 deck calls the goal "standardizing the DNA of imaging IT" and titles itself "Realizing Object-Oriented Imaging Results"; the project lead's 2026-09-19 formulation is "a system of defined data structures for representing imaging exam result information", "intended to be used within applications to both read and create result data".

**Status.** Stated goal, expressed at three dates with shifting emphasis.

**Evidence.**
- openimagingdata.org project site tagline (cited in `knowledge/overview/what-is-oidm.md`): "defining unified data structures to integrate new functionality into imaging informatics platforms."
- January 2026 deck, title and subtitle.
- Email notes, points 3 and 4 (see A21).
- Board 9 ("OIDM Big Picture"), "Where (i.e., Vision)" statement: "Tools throughout imaging informatics should form an *integrated, open platform*, allowing all to add and inter-connect new functionality leading to more efficient, higher quality patient care."
- Board 14 header: "Project that defines methods and tools that create IT platforms within the imaging ecosystem."
- JDIM IPL manuscript abstract: "Radiologists need a longitudinal record of findings to interpret efficiently and to integrate intelligent tools, and we found no radiology data standard that defines one."
- `sources/bucket/text/ai-evolution-radiology.md` (in-progress working draft, no venue; **paraphrase only, several sentences are objectively incomplete mid-edit**): argues that the limiting factor in radiology AI is not model capability but the absence of a shared, relational "foundation context" specifying findings, diagnoses, anatomy and their relations, comparable to what DICOM and PACS did for images, and that radiologists must author and steward that representation. Per `sources/bucket/REPORT.md` §1, the draft was last saved 2026-08-14 with 219 tracked insertions and 190 deletions.

**Related.** A21, C2, C3.

## C2. The relationship among the parts: three layers, and the DOM analogy

**Statement.** The work organizes into a semantic foundation (finding models and CDEs, anatomic locations, exam types, terminologies), a set of data structures built on it (Observation, Exam Finding List, Imaging Problem List, Imaging Persona), and applications that read and write those structures. Each layer depends on the one below through shared identifiers. The relationship to FHIR is described by analogy: "the relationship between OIDM and FHIR might be that between the browser's DOM and HTML."

**Status.** Stated organization (deck, site); working proposal at the class level (Board 4); the organizing principle of the current bundle.

**Evidence.**
- January 2026 deck, strategic pillars: "1. Semantic foundation: OIFM -> CDEs; Anatomic Location definitions. 2. Data structures: atomic Observation -> Exam Finding List -> IPL -> 'Imaging Persona'. 3. Applications: Open Imaging Reporting SDK; demo apps."
- Site post "Data Model: Structure and Function", 2024-01-25, read live: the model's parts are named one by one — "**Observations:** These are the individual radiology findings that the radiologists is describing in their current report"; "**Current Report Text:** The actual text of the current report, ideal represented as hypertext with tags"; "**Imaging Stud(y|ies)**"; "**Patient**"; "**Order**"; "**Prior Imaging Studies**: Representations of the patient's imaging history, including both report text"; "**Tracked Observations**: An index of the association of the same radiology finding (e.g., a tumor or a fracture)"; "**EHR Data**". On FHIR: "The data model is intended to make extensive use of FHIR definitions in its structuring, but will likely reflect a superstructure", and "An analogy for the relationship between OIDM and FHIR might be that between the browser's DOM and HTML." This is the earliest first-hand statement of the parts list that Board 4 later draws, and it names Tracked Observations as an index of the association of one finding across exams, which is the A19 idea in prose.
- Board 9, "SDK Development" work thread: "Model is web browser DOM" — the same analogy, independently.
- Board 4, hand annotations: FHIR maps to the Patient/Order and EHR Data branches; the LOINC/RadLex Playbook to ImagingStudyType; Anatomic Locations to BodyPart — an explicit statement of which external vocabulary supplies which part.
- Board 9, "OIDM Work Threads" frame, six workstreams: Data Model Toolchain; Anatomic Locations/Exam Types; Data Model Content; SDK Development; Report Representation; Utility Library. The Data Model Content box (highlighted) states the content strategy: "Significant challenge is too few data element definitions; New concept—'stub' data elements: presence, change attributes only; Will allow rapid expansion of database; Iterate to improve models in open crowd-sourced model; ACR/RSNA review as needed; Transform to ACR/RSNA CDEs."
- Board 1 (internal; content only), "Ingredients": "Standard codes for findings (CDEs!) — Don't need complete data models — 'CDE stubs' suffice."
- January 2026 deck, "OIFM: the CDE workbench": finding models as a "Rapid innovation / proving ground before ACR/RSNA CDE adoption", supplying "ground-level info for tool access + LLM context engineering" and "exploratory metadata… that can graduate to standards."
- JDIM IPL manuscript, printed p.19: "The CDEs, the OIDM finding models, and the terminologies they map to (RadLex and SNOMED CT) provide a vocabulary of findings and anatomic sites, not a patient's history." — the clearest statement of the boundary between the semantic foundation and the data structures.
- JDIM IPL manuscript, printed p.6: the EFL finding code "comes from the Open Imaging Data Model (OIDM) finding vocabulary, an open lexicon in the lineage of the RSNA/ACR CDEs."

**Related.** A2, A21, C1, C3; the CDE-workbench relationship belongs primarily to the semantic inventory.

**Unresolved.** The deck's layer-2 hierarchy has four levels; only two are built (A2, A16).

## C3. Structure first, standards after; and how agreement is supposed to happen

**Statement.** Define the data structures first, then express them in FHIR and other standards. Convening is proposed as the mechanism: an ACR-OIDM Structured Imaging Results Working Group co-hosted with the ACR, bringing expert and vendor participants into an "academic-vendor big tent", feeding a use-case pipeline to the CDE group and standardizing the result. The ACR Data Science Institute's role is sketched separately as sponsoring, logistics, volunteer opportunities and demo projects.

**Status.** Proposal recorded in the deck and on a board; nothing in any repository records the working group as convened.

**Evidence.**
- January 2026 deck, call to action: "ACR-OIDM Structured Imaging Results Working Group; structure-first (then FHIR etc.); vendor-driven." ACR priorities named: recommendation tracking, AI validation (correlating AI against radiologist Observations), quality metrics, *-RADS support. Next steps: "host/moderate academic-vendor big tent; use-case pipeline -> CDE group; standardize the result."
- Board 14 ("ACR OIDM", low sensitivity): the ACR Data Science Institute's four branches — Sponsoring (identity, project participation, spread message, show usage with ACR); Logistics (meeting coordination, project management, space at events); Volunteer Opportunities (governance, use cases and future demos, CDE definition and review, CDE indexing, anatomic locations, exam-types-to-anatomy, reference implementations, demo projects, website and documentation, white papers, standard-making via IHE); Demo Projects; Reference Implementations (work with or within existing open-source efforts; grant or paid support; the component list in A16).
- JDIM IPL manuscript, printed p.18: "Vendors are beginning to build longitudinal tracking features with, to our knowledge, no published data model to guide them. Shared data structures come first… We offer this model as a starting point for an open, community-developed standard."
- JDIM IPL manuscript, printed p.17: "The drafters of the Integrating the Healthcare Enterprise (IHE) Imaging Diagnostic Report (IDR) profile included a prior finding catalog use case, conceptualized as an imaging problem list for the reading radiologist, based on earlier presentations of the model described here… The IHE supplement leaves the catalog's information model out of scope, deferred to subsequent work on the model presented here."
- SIIM webinar slide 32 speaker notes: "the adoption path is already forming: the IHE Imaging Diagnostic Report profile names a prior finding catalog as an imaging problem list. This rides existing standards rather than inventing new ones."
- JDIM IPL manuscript, printed p.18, "Adoption": "Pre-populated chronic findings are a natural entry point for IPL adoption… **Affirming must save the radiologist time immediately, because downstream benefits alone are unlikely to sustain adoption.**"

**Related.** A21, B9, C1, C4.

**Undetermined.** Whether the working group has been convened since January 2026. No source read records it.

## C4. Nothing is formally defined yet

**Statement.** The project is in a coalescing phase. No source is the specification; each source's current version of a structure stands beside the others, dated and attributed.

**Status.** Decision of record, 2026-09-21.

**Evidence.**
- `knowledge/plans/2026-09-20-knowledgebase-build-plan.md`, "Decisions added 2026-09-21", row "No specification exists": "The project is in a coalescing phase; nothing is formally defined. The knowledgebase presents each source's current version of a structure side by side (repo branch and commit, manuscript under review, deck or webinar, board), dated and attributed, and states disagreements (for example the three Imaging Problem List status vocabularies) without resolving them. Words like 'specification' or 'canonical model' are not used for any of them."
- Email notes, incorporation targets, last bullet: 16 bundle documents call a repository README or a manuscript "the specification" or similar; the project lead directs replacing these with attributed, dated phrasing.
- SIIM webinar slide 25 speaker notes: "the IPL is an actively-developing framework. Details shown today are being iterated and may change. This honesty invites an informatics audience into an open problem rather than pitching a finished product, and it protects every specific design rule just shown from reading as a fixed claim."
- IPL repo `main` `06f64a7`, `CLAUDE.md`: "This is primarily a data specification and documentation project, not a traditional code repository" — the repository's own self-description, which the 2026-09-21 decision supersedes as a bundle-wide framing.

**Related.** A5, A9, A21.

---

# What could not be determined

1. **The JDIM manuscript's Table 1 FHIR mapping** was read only through `sources/bucket/REPORT.md` §4's summary of the rendered table image (PDF page 88), not from the table itself. The element-by-element mapping in A21 should be re-verified against that page before it is published.
2. **The JACR manuscript's submission status.** The file is a blinded manuscript with a supplement and figures and no manuscript number or cover letter, so "prepared for submission" is the most the file supports.
3. **Whether the webinar's two-value status model supersedes the manuscript's four-value model.** The webinar is later (2026-07-15) than the R1 submission, and its speaker notes say the framework is being iterated, but no source states a supersession.
4. **Who owns and assigns a finding's tracking identifier** (A19). Open on Board 15, unanswered elsewhere.
5. **Whether "Imaging Persona", "OIDM Data Context Model" and "Reporting Data Context Object Model" name one structure or three** (A16).
6. **Whether the `indeterminate` presence value in the sample data is superseded** by the binary-presence-plus-confidence rule (A10).
7. **The relationship between the JACR study's four matching rules and the JDIM graduated-confidence model** (A8).
8. **Board dates.** The transcription carries dated notes on several boards, but the boards themselves are undated working canvases; a dated note inside a board is evidence of when that note was made, not of the board's currency.
9. **Whether the deployed viewer v1 is to be retired** now that its data bundle is orphaned from the generation pipeline (B1).
10. **Finding-model corpus counts and the `FindingModelFull` schema** were not verified at source here; the `findingmodel` and `findingmodels` repositories were out of scope for this inventory and belong to the semantic inventory. A15's 2,458-definition figure comes from the webinar only.
11. **Which presence vocabulary is intended** (A10). Three are in active use across the manuscript, the extraction prompt and the sample data.
12. **Whether the selector is meant to resolve technical language to a diagnosis** (A24). Two rules in the same pair of prompts point opposite ways, and the technical-findings reference sides with one of them.
13. **Whether an observation may carry more than one anatomic location** (A12). The coding tool returns a list; the Exam Finding List decision is a single location.
14. **Who fills the vocabulary gaps** that the blanket-negative rule and the `no_candidate_match` / `definition_mismatch` rejection reasons are designed to surface (A23, A24). The mechanism reports the gap; no source names the process that closes it.
15. **The gold file schema** for adjudicated extractions (B4), recorded as open in the reviewer workflows plan.
16. **FindingModelForge's authoring prompts.** The Forge draft lifecycle is recorded here only as it bears on review and provenance; the prompt text inside the application was not read at source for this inventory, and the Forge idea belongs to the semantic inventory in any case.
17. **`ReportFindingRefiner` and the `openimagingdata.org` repository** (`schemas/`, `docs/`) were named for reading but not reached; they are lineage sources for the schema-differences material already held in `knowledge/references/cde-schema-differences.md`.

---

# Proposed idea pages for this area

Names are nouns. Each page is one explanatory home; other pages link to it.

| Page | One line | Homes ideas |
|---|---|---|
| `observation` | The atomic record of one finding asserted on one exam: what, where, attributes, and the sentence it came from. | A1, A10 (presence and confidence), A11 (negatives) |
| `exam-finding-list` | The per-exam list of findings, and the faithful-translation constraint that makes everything above it trustworthy. | A2 (first level), A3, A9 (observations within one report) |
| `imaging-problem-list` | The patient-level record: entries keyed by finding and site, their observation histories, and what the record is for. | A2 (second level), A4, A22 |
| `entry-status-and-trajectory` | How an entry's state is read from its observation history, and the four vocabularies that disagree about what to call it. | A5, A6 (succession sits beside status) |
| `succession-and-linking` | Connecting observations to entries and entries to each other: entity resolution, graduated-confidence linking, succession, and anatomic-compatibility reconciliation. | A6, A8, A13, A19 |
| `provenance-and-review` | Where each observation came from, who affirmed it, and how corrections are recorded. | A7 |
| `finding-and-diagnosis` | What counts as one finding when reports use different codes, substitute a diagnosis, or describe an entity that evolved; and where technical observation-level language fits. | A9, A17, and the technical-findings reference |
| `negation-and-normality` | Why an explicit negative and a statement of normality both become coded findings, and what that asks of the vocabulary. | A11, A23 |
| `coding-a-finding` | Assigning a finding code and a location code so that equivalent descriptions converge, including when to refuse. | A24, A25 |
| `extraction-quality` | What can go wrong translating prose into structure, how the system checks for it, and how that is measured. | A26, B4 |
| `anatomic-location-of-a-finding` | Why every observation carries a location, how it is assigned, and what the generic-versus-specific gap costs. | A12, A13 (shares with succession-and-linking; this page owns assignment, that page owns reconciliation) |
| `finding-context` | The per-finding dimensions that tell a reader or an agent what to expect next: permanence, expected course, etiology, anatomy. | A14, A15 |
| `imaging-persona` | The clinical context around the imaging record, and the object model that names its parts. | A16 |
| `recommendation-and-follow-up` | Representing a follow-up recommendation, attaching it to an entry, and closing it. | A18 |
| `structures-and-transport` | Why the structures are defined independently of FHIR and DICOM, and how they would be expressed for exchange. | A20, A21 |
| `imaging-problem-list-viewer` | What the viewers show, and the rule that presentation never changes the record. | B1 |
| `extraction-and-coding` | Turning report prose into coded observations, and keeping coding a separate job from extraction. | B2, B3, B10 |
| `applications-of-the-record` | What a longitudinal structured record makes routine: the application families, the breast case, the life-cycle uses. | B5, B6, B11 |
| `outcome-tracking` | Closing the loop from what was reported to what happened. | B7 |
| `reporting-assistance` | The context object a reporting tool supplies and the commands a plugin can issue. | B8 |
| `interoperability-demonstrations` | Exchanging coded findings between systems, and the questions that exposes. | B9 |
| `what-oidm-is` | The purpose, the parts, and how they depend on each other. | C1, C2 |
| `how-agreement-happens` | Structure first, standards after, and the convening that is supposed to produce agreement. | C3, C4 |

Twenty-four pages for this area. The semantic inventory's pages (finding models, CDEs, anatomic locations index, exam types) sit beside them. Three are seams where the two inventories meet and need an ownership decision when the combined list is agreed: `anatomic-location-of-a-finding`, `finding-context`, and `coding-a-finding`, the last because the convergence rules are as much a statement about what the vocabulary is for as about how the coder behaves.

Four of these pages exist because the prompts do. `negation-and-normality`, `coding-a-finding` and `extraction-quality` home ideas that appear in no manuscript, deck or board, only in the instructions the team wrote for its own models; `finding-and-diagnosis` draws its sharpest operational rule from the same place. They are not tooling pages. A rule that says a more specific code is never an acceptable match, or that a normal statement becomes an absent abnormality, is a position about what the data structures mean, written where it had to be executable.

---

# Existing bundle pages holding unique team-authored material that needs a home first

Checked page by page against the sources above. These carry team-authored substance that exists nowhere else in a durable form, so they must be rehomed before removal.

| Page | Unique material | Where it should go |
|---|---|---|
| `data-structures/ihe-idr-alignment.md` | The IDR observation grammar (five slots with the supplement's own rules), the three IDR term definitions, the four unresolved OIDM/IDR differences, and IDR's three questions back to RadElement. Sourced to `notes/ihe-idr-extract.md` on `RSNA/ACR-RSNA-CDEs` `next-gen-2026`, which has not been migrated into this bundle. | `structures-and-transport`, with the finding-versus-diagnosis difference cross-linked to `finding-and-diagnosis` |
| `data-structures/fhir-mapping.md` | The worked `FHIRSamples` analysis: the set-code / element-code / value-code chain, status-as-provenance, and assessments as second-order Observations whose `derivedFrom` points at both the study and the finding Observation. This reading of the samples exists only here. | `structures-and-transport` |
| `data-structures/technical-imaging-findings.md` | Migrated verbatim from IPL repo `dev` `docs/technical-imaging-findings.md`: the catalog of modality-specific technical terms and the rule that a technical observation must not be reinterpreted as the diagnosis that might explain it. Team-authored, draft status stated in the source. | `finding-and-diagnosis`; keep the full catalog as a `references/` extract if it does not fit |
| `data-structures/anatomic-location-assignment-rules.md` | Migrated from IPL repo `dev`: the precedence ladder, laterality rules, bilateral rules and worked misses. Team-authored. | `anatomic-location-of-a-finding`; the long worked examples may belong in `references/` |
| `history/use-cases.md` | The whole `UseCases` catalog reorganized, with the six value categories and the RSNA Reporting Informatics Committee attributions preserved. The upstream repository has been dormant since 2024-02-26. | `applications-of-the-record`, or a `references/` extract linked from it |
| `applications/reporting-sdk.md` | The 2023 site post's plugin-container design and the About page's language commitments, read from sources that are live web pages rather than repository files. | `reporting-assistance` |
| `overview/vision.md` | The DOM/HTML analogy and the deck's three benefits, quoted from site posts that exist only on the live Ghost site. | `what-oidm-is` |
| `references/exam-finding-list-example.md`, `references/imaging-problem-list-example.md` | Real sample JSON with commentary. Keep only what an idea page cannot explain in prose; the example2 study supersedes most of the commentary. | trim into `observation` / `imaging-problem-list`, or keep one minimal extract |
| `references/status-update-2026-01.md` | The January 2026 deck extract. The deck is a live Gamma URL that may change. | keep as a dated `references/` extract |
| `roadmap/open-questions.md` | 5,963 words; contains the team's own unresolved alternatives mixed with agent-found documentation defects. | split: team questions go beside their ideas; defects to `sources/upstream-issues-draft.md` per the joint notes |

Pages in this area found to carry **no** unique team-authored material beyond what the sources above supply, and which can be retired once their ideas have homes: `data-structures/index.md`, `data-structures/hierarchy.md`, `data-structures/sample-data.md`, `data-structures/observation.md`, `data-structures/exam-finding-list.md`, `data-structures/imaging-problem-list.md`, `data-structures/imaging-persona.md`, `applications/index.md`, `applications/imaging-problem-list-viewer.md`, `applications/report-extraction-platform.md`, `applications/finding-and-location-coding.md`, `applications/ipl-mvp-extraction.md`, `overview/architecture.md`, `overview/what-is-oidm.md`, `roadmap/ipl-data-model-system.md`, `history/timeline.md`, `history/lineage-repositories.md`, `history/extraction-approaches.md`, `history/cde-template-rendering.md`, `repositories/repository-map.md`. Each was checked against its cited sources; each restates material that the sources carry directly, which the idea pages will cite instead.
