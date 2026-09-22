---
type: Reference
title: Open questions
description: Every conflict between sources and every unverified fact found while building this knowledgebase, grouped by area, with the sources on each side and the owner where one is indicated, plus the defects found in source documents.
tags: [roadmap, open-questions, conflicts, gaps]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: "Open Imaging Data Model 2026 Status Update, January 2026"
  - id: prose-schema
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/schema/finding_model_schema.md
    title: Finding Model Schema, prose mirror, findingmodels main branch
  - id: fm-code
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/finding_model.py
    title: finding_model.py, released Pydantic definitions, findingmodel main branch
  - id: fm-metadata-types
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/packages/findingmodel/src/findingmodel/types/metadata.py
    title: types/metadata.py, findingmodel feature/metadata-cleanup branch
  - id: fm-optimization
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/docs/enrichment-pipeline-optimization-proposal.md
    title: Finding enrichment pipeline optimization proposal, findingmodel main branch
  - id: fm-adr2
    resource: https://github.com/openimagingdata/findingmodel/blob/1942b06a91d6a5c5eefe10f99a7273e41e24be01/docs/adr/0002-split-agent-assignment-architecture.md
    title: ADR 0002, split-agent assignment architecture, findingmodel feature/metadata-cleanup branch
  - id: fm-issue-42
    resource: https://github.com/openimagingdata/findingmodel/issues/42
    title: findingmodel issue 42, identifiers silently regenerated on round trip
  - id: fm-issue-39
    resource: https://github.com/openimagingdata/findingmodel/issues/39
    title: findingmodel issue 39, laterality assigned backwards in the anatomic location build
  - id: cde-metadata-note
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/oifm-metadata-fields.md
    title: OIFM metadata fields note, ACR-RSNA-CDEs next-gen-2026 branch
  - id: idr-extract
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md
    title: IHE Imaging Diagnostic Report Phase II extract, ACR-RSNA-CDEs next-gen-2026 branch
  - id: cde-context
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/CONTEXT.md
    title: CDE vocabulary working glossary, ACR-RSNA-CDEs next-gen-2026 branch
  - id: cde-axis
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/11-anatomy-axis.md
    title: The anatomy axis, current state, ACR-RSNA-CDEs next-gen-2026 branch
  - id: cde-gaps
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/04-anatomy-gaps.md
    title: Anatomic locations gaps and node requests, ACR-RSNA-CDEs next-gen-2026 branch
  - id: cde-schema-canonical
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/cde.schema.json
    title: cde.schema.json at the root of ACR-RSNA-CDEs, named canonical by CDEStaging
  - id: cde-schema-11
    resource: https://github.com/openimagingdata/common_data_elements/blob/35536d8c858bcd33e730a00c919edaef2e310a0b/schema/cde.schema-1.1.json
    title: cde.schema-1.1.json, common_data_elements repository
  - id: cdestaging-issue-1
    resource: https://github.com/openimagingdata/CDEStaging/issues/1
    title: CDEStaging issue 1, differences between the RadElement API schema and the published RelaxNG schema
  - id: cdestaging-authoring
    resource: https://github.com/openimagingdata/CDEStaging/blob/b814a102655054ac08b3c118cb1977a387655a8b/docs/Authoring.md
    title: CDEStaging authoring guide stub
  - id: ipl-issue-1
    resource: https://github.com/openimagingdata/imaging-problem-list/issues/1
    title: imaging-problem-list issue 1, "Create System of Data Models"
  - id: ipl-claude-dev
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/CLAUDE.md
    title: imaging-problem-list domain model notes, dev branch
  - id: coding-design
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/coding-agent-design.md
    title: Coding agent design, imaging-problem-list dev branch
  - id: coding-archive
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/archive/finding-and-location-code-assignment-plan.md
    title: Finding and location code assignment plan, archived, imaging-problem-list dev branch
  - id: anat-rules
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/anatomic-location-assignment-rules.md
    title: Anatomic location assignment rules, imaging-problem-list dev branch
  - id: cleanup
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/docs/plans/definition_cleanup.md
    title: Definition Cleanup Plan, findingmodels main branch
  - id: lists-readme
    resource: https://github.com/openimagingdata/findingmodels/blob/a30c3c95fa3943e7340ce87575f4b1b926987eb8/lists/README.md
    title: MGB exam-oriented sub-taxonomies README, findingmodels taxonomy-export-2026-08-15 branch
  - id: anat-data
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/notebooks/data/anatomic_locations_noembed.json
    title: anatomic_locations_noembed.json, the current anatomic location source data
  - id: anat-normalized
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/tasks/done/anatomic-locations-normalized-schema.md
    title: Anatomic locations normalized schema plan, completed, findingmodel main branch
  - id: anat-docs
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/docs/anatomic-locations.md
    title: Anatomic locations package documentation, findingmodel main branch
  - id: radlex-issue-3
    resource: https://github.com/RSNA/RadLex/issues/3
    title: RSNA/RadLex issue 3, "Add Anatomic Locations"
  - id: forge-issue-13
    resource: https://github.com/openimagingdata/FindingModelForge/issues/13
    title: FindingModelForge issue 13, "Implement model editing"
  - id: fm-issue-15
    resource: https://github.com/openimagingdata/findingmodels/issues/15
    title: findingmodels issue 15, "Bring in CDE Staging MD content"
  - id: plan
    resource: /plans/2026-09-20-knowledgebase-build-plan.md
    title: Knowledgebase build plan, the record of the 2026-09-20 and 2026-09-21 planning sessions
---

# How to use this list

Every entry below is a disagreement between sources, or a fact this knowledgebase could not verify. Nothing here is resolved, and nothing here is a recommendation. Each entry names the sources on each side and links to the bundle document that records the detail. "Who decides" is filled in only where a source indicates an owner; where it is blank, no source names one.

These were collected by the ten agents who wrote the rest of the bundle and then deduplicated, so an entry may have been raised from several directions at once. The last section lists defects in source documents, which could become issues in their home repositories, and is separate from the design questions above it.

# Finding models

| # | The discrepancy | Sources | Who decides |
|---:|---|---|---|
| 1 | Corpus size. The deck says "nearly 3,000" Open Imaging Finding Models (OIFMs); `findingmodels` at `main` holds 2,382 definitions. | Deck[^deck] against the identifier registry and `defs/`. See [content catalog](/semantic-foundation/finding-models/content-catalog.md) | Project lead, since the deck is the claim |
| 2 | Choice value code indexing. The prose schema mirror numbers the first choice value `.1`; the released validator writes the attribute identifier plus a zero-based index, so the first value is `.0`, and the stored corpus follows the code. | Prose mirror[^prose-schema] against `finding_model.py`[^fm-code]. See [finding model format](/semantic-foundation/finding-models/finding-model-format.md) | `findingmodel`, which holds the enforcing code |
| 3 | The prose mirror omits `anatomic_locations` from the full model entirely, and states none of the length or cardinality constraints the code enforces: at least one attribute, at least two choice values, index code and contributor field lengths and patterns. | Same two sources. See [the finding model schema reference](/references/finding-model-schema.md) | `findingmodels`, which holds the document |
| 4 | Subspecialty codes disagree. The metadata note lists sixteen, including `AB` for abdominal and `VI` for vascular and interventional; the branch code defines seventeen with neither, adding `NM`, `SQ`, and `VA`. | Metadata note[^cde-metadata-note] against `types/metadata.py`[^fm-metadata-types] | |
| 5 | Etiology code count disagrees. The same note lists twenty-five; the branch code defines twenty-seven, adding a bare `vascular` and a bare `cardiac`. | Same two sources | |
| 6 | Presence value codes are positional, not semantic. Their meaning depends on value order. 2,223 of the 2,261 published definitions with a presence attribute order the values absent, present, indeterminate, unknown; 38 do not. Consumer documentation states "`.1` = present, `.0` = absent" as if universal. | The published corpus against `imaging-problem-list` domain notes on both branches[^ipl-claude-dev]. See [presence](/glossary/presence.md) | |
| 7 | The 38 exceptions break down as 27 MassGeneral Brigham contributions and 10 derived from common data elements, putting present, unknown, or normal first. | The corpus itself | |
| 8 | The presence value set is not shared across layers. Finding models use absent, present, indeterminate, unknown. The extraction schema uses present, absent, indeterminate, possible. `possible` has no finding-model counterpart and `unknown` has no extraction counterpart, and nothing documents how an extracted `possible` becomes a coded value. | Finding model definitions against the extraction models on `imaging-problem-list` `dev`. See [Observation](/data-structures/observation.md) | |
| 9 | `finding_type` in the sub-taxonomies is a two-way observation against diagnosis split; `entity_type` in the metadata rewrite has seven values. Same distinction, two vocabularies. | Sub-taxonomy README[^lists-readme] against `types/metadata.py`[^fm-metadata-types] | |
| 10 | Tags and the new typed metadata fields overlap, for example a tag `CT` beside `applicable_modalities: [CT]`. The rewrite does not say what becomes of existing tag lists. | Metadata rewrite design document. See [format evolution](/roadmap/finding-model-format-evolution.md) | |
| 11 | The rewrite's rule that canonical `index_codes` be exact or clinically substitutable matches does not hold over the existing corpus, which predates it. Nothing has landed on `main`. | Metadata rewrite against the corpus | |
| 12 | The enrichment architecture is chosen twice, in opposite directions, with neither document acknowledging the other. The optimization proposal on `main` recommends collapsing the intermediate calls into one unified classifier; the decision record on the work-edge branch chooses seven focused agents instead, accepting more model calls for per-field tunability. | Optimization proposal[^fm-optimization] against ADR 0002[^fm-adr2]. See [the enrichment pipeline](/semantic-foundation/finding-models/enrichment-pipeline.md) | |
| 13 | Taxonomy rows do not map one-to-one onto finding models. The README states an identifier "can appear on two rows where those earlier writebacks mapped two findings onto one model." Nothing states whether that is to be corrected during triage or preserved as a real many-to-one mapping. | Sub-taxonomy README[^lists-readme]. See [the sub-taxonomies](/semantic-foundation/finding-models/finding-taxonomies.md) | |
| 14 | Identifier lifecycle is undefined. Nothing documents deprecation, retirement, supersession, or versioning of a published OIFM or OIFMA identifier, and the released format has no version field. The only stated mechanism is the `lifecycle` object in the version 2 draft. | The released format[^fm-code] against the version 2 draft. See [identifiers](/semantic-foundation/finding-models/identifiers.md) | |
| 15 | Identifiers are silently regenerated on a round trip through the base class, which the issue calls a silent data-integrity hazard. Four candidate fixes are proposed and none is chosen. Open since 2026-04-18. | Issue 42[^fm-issue-42] | `findingmodel` |
| 16 | Gamuts reclassification. 1,933 of 2,382 definitions came from differential-diagnosis lists, so many name diagnoses. The cleanup plan lists gamuts reclassification as the one step that "needs broader design discussion about what model types we support," and says of the 71 "with"-clause patterns that the genuine differential constructs "may need a different model type or to be deprecated as finding models and preserved as gamuts references only." | Definition cleanup plan[^cleanup]. See [content direction](/roadmap/finding-model-content-direction.md) | Stated as needing design discussion; no owner named |
| 17 | The same plan flags CDE-derived measurement protocols and scoring systems as needing reclassification because they have no presence or absence. No model type exists for them. | Definition cleanup plan[^cleanup]. See [finding models and CDEs](/semantic-foundation/finding-models/finding-models-and-cdes.md) | |
| 18 | Change from prior is required by authoring guidance but missing from part of the corpus. The cleanup plan proposes adding presence and change from prior to 124 models. Consumers cannot assume the attribute exists. | Definition cleanup plan[^cleanup] against the corpus | |
| 19 | Three schema extensions to the finding model JSON schema exist on three unmerged `findingmodels` branches, diverging from each other, with nothing landed on `main` and no pull request on any of them. | The three branches. See [format evolution](/roadmap/finding-model-format-evolution.md) | |
| 20 | `findingmodels` issue 15 is answered by unmerged work. The triage and conversion scripts on the CT chest branch read the staged source directory and write validated definitions, but nothing proposes merging them. Whether that closes the issue as filed is unresolved. | Issue 15[^fm-issue-15] against the branch. Same shape as entry 57 | `findingmodels` |

# Common data elements and the next-generation vocabulary

| # | The discrepancy | Sources | Who decides |
|---:|---|---|---|
| 21 | The canonical common data element schema is claimed in two repositories under three filenames, and the version named canonical is ahead of the data published beside it. The schema at the root of `ACR-RSNA-CDEs` is what the staging repository names canonical, and it is byte-identical to `cde.schema-1.1.json` in `common_data_elements`, whose own 145 set definitions conform to version 1.0. | Canonical schema[^cde-schema-canonical] against the 1.1 copy[^cde-schema-11]. See [CDEs and RadElement](/semantic-foundation/common-data-elements/cdes-and-radelement.md) | ACR and RSNA, as the governing bodies |
| 22 | All three of those files declare the same `$id`, pinned to `v1.0.0`, so no consumer can distinguish the versions by identifier. Should 1.1 get its own? | The three schema files | `common_data_elements` and the CDE repository |
| 23 | `biological_sex` and `age_range` remain unreconciled between the RelaxNG schema and the JSON Schema in force. `biological_sex` is defined in 1.0 and dropped in 1.1; `age_range` appears in neither. The staging repository's issue 1 has tracked this since 2023-02-27 with no activity and is its oldest open item. | CDEStaging issue 1[^cdestaging-issue-1]. See [CDE staging](/semantic-foundation/common-data-elements/cde-staging.md) | `CDEStaging`, through issue 1 |
| 24 | Published definitions conform to schema 1.0 while 1.1 exists and is described as published but not in force. | `common_data_elements` README against its definitions | |
| 25 | The CDE Set schema constrains an index code `system` to RadLex, SNOMED CT, or LOINC. The RadElement API does not, and OIFM does not. | CDE Set schema against the API and `IndexCode`[^fm-code] | |
| 26 | No coding system identifier is settled for RadElement. Three forms are in use: a URL in the lineage FHIR samples, a bare `RADELEMENT` string in finding model index codes, and a proposed base in the next-generation notes. The IHE profile asks the same question from its side.[^idr-extract] | Three repositories plus the profile extract. See [RadElement](/glossary/radelement.md) | The profile extract puts the question to the RadElement side |
| 27 | Nomenclature: "attribute" in OIFM, "DataElement" in the next-generation vocabulary, "element" in RadElement, for the same concept. The scoping differs too: an OIFM attribute belongs to one model, a DataElement is shared through element bindings. Committee minutes record the debate as unresolved. | `CONTEXT.md`[^cde-context] against the finding model format. See [data element](/glossary/data-element.md) | Recorded as a committee question |
| 28 | `Measurement` is a distinct node type in the next-generation vocabulary and has no counterpart type in OIFM, which uses a numeric attribute. Measurement method is not representable in OIFM at all. | `CONTEXT.md`[^cde-context] against the finding model format. See [measurement](/glossary/measurement.md) | |
| 29 | The next-generation vocabulary has no settled status and names its own open structural questions: subtype propagation, the conditionality fork, whether two node types for Finding and Diagnosis are still warranted, and how the tissue-type and structure-type scope families connect to the anatomic location hierarchy. Its glossary states the definitions "express our current ideas ... not a jointly settled integration model." | `CONTEXT.md`[^cde-context] and the branch's handoff document. See [the next-generation vocabulary](/semantic-foundation/common-data-elements/next-generation-vocabulary.md) | The build plan records the project lead's approval to publish the terms as draft[^plan] |
| 30 | The staged definitions do not follow the schema the repository points at. Of 150 JSON definition files, the ones inspected carry a finding name, a description, and attributes typed choice or numeric, which is the finding model attribute shape rather than the CDE set shape, although the README describes them as common data elements in JSON format. | The definitions against the README. See [CDE staging](/semantic-foundation/common-data-elements/cde-staging.md) | |
| 31 | No mechanical path exists from the staging repository to RadElement. Nothing describes a route from a staged definition to a submitted one; the process is manual curation. | The repository. See [CDE staging](/semantic-foundation/common-data-elements/cde-staging.md) | |
| 32 | Unverified: whether any documented process moves content between the staging repository, RadElement, and the finding model corpus. None was found in either repository, so the bundle describes the observed traffic instead of inferring a pipeline. | Not found in any source | |
| 33 | The CDE-labeled FHIR Observation pattern is implemented only in the lineage samples and in the documented mapping, not in any working extraction pipeline. Neither the early extraction prototype nor the current platform contains any RadElement code anywhere; the prototype maps to finding model identifiers instead. This bears on the deck's CDE-labeling claims. | The two extraction repositories against the deck[^deck]. See [FHIR mapping](/data-structures/fhir-mapping.md) | |

# Anatomic locations

| # | The discrepancy | Sources | Who decides |
|---:|---|---|---|
| 34 | Two datasets, both current in their own lineage: 2,890 records published at anatomiclocations.org, last changed 2023-01-08, and 2,926 records in the `findingmodel` export, last changed 2026-03-02. The 36-record difference has never been reconciled record by record and no document says what the extra records are. No process syncs them in either direction. | The two data files. See [lineage and current implementation](/semantic-foundation/anatomic-locations/lineage-and-current-implementation.md) | The build plan names the newer set as current; reconciliation is unassigned |
| 35 | Two framings of the RadLex relationship are in force. Issue 3's exit criterion, full coverage of the terminology in RadLex, reads as absorption. The 13 September 2026 agreement describes the file as an overlay that the RadLex anatomy track edits in place and calls it "the basis of the RadLex anatomy axis going forward." Compatible but not identical. | Issue 3[^radlex-issue-3] against the anatomy axis record[^cde-axis]. See [the anatomy roadmap](/roadmap/anatomic-locations-and-radlex.md) | RSNA and the anatomy track |
| 36 | RadLex incorporation has no ontology evidence. No code, commit, or document in the RadLex repository mentions anatomic locations, and issue 3 has no comments and no sub-issues, although the deck states the incorporation as happening. | Deck[^deck] against the RadLex repository | RSNA, through issue 3 |
| 37 | Composite sided identifiers are a local convention, not RadLex content: 1,016 of 2,926 records carry one. Until real identifiers are minted, any consumer treating a location identifier as a resolvable RadLex identifier fails on more than a third of the set. | The data[^anat-data] and the anatomy axis record[^cde-axis]. See [the data model](/semantic-foundation/anatomic-locations/data-model.md) | The anatomy axis record assigns this to the RadLex anatomy track |
| 38 | Sided variants are modelled three ways. The next-generation glossary defines an anatomic location as RadLex identity "with temporary sided-variant exceptions"; OIDM makes sided variants first-class composite nodes; the IHE profile keeps laterality in a separate field beside an unsided code. A round-trip mapping is owed and unwritten. | `CONTEXT.md`[^cde-context], the anatomic data, and the profile extract[^idr-extract]. See [laterality](/glossary/laterality.md) | |
| 39 | Anatomic location code system casing. The metadata note says `system="ANATOMICLOCATIONS"`; the package code emits `system="anatomic_locations"`; real Exam Finding List and Imaging Problem List data uses bare RadLex identifiers with no system at all. | Metadata note[^cde-metadata-note], the package code, and the sample data | |
| 40 | RadLex has no physical-containment axis. The "contained by" hierarchy is an OIDM curation product built alongside RadLex's part-of relations. The IHE profile's query design assumes traversal over "an anatomical tree" without saying which axis. | RadLex OWL against the anatomic data and the profile extract[^idr-extract]. See [contained by and part of](/glossary/contained-by-and-part-of.md) | |
| 41 | Four incompatible body region enumerations are in use, in the anatomic locations package, the metadata rewrite, the extraction schema, and the viewer filter. Thorax against chest, and whether spine is a region, are the recurring mismatches. | Four sources. See [body region](/glossary/body-region.md) | |
| 42 | The curation field reference lists `"Spine"` among common region values, but no record uses it and the runtime region enumeration has no spine member, while other OIDM layers do use a spine region. Deliberate removal or omission is unstated. | Curation skill reference against the data[^anat-data] | |
| 43 | The classification fields `location_type`, `body_system`, and `structure_type` are defined on the runtime model and empty in every record. The next-generation anatomy axis independently names the absent is-a relation "the major shortcoming" for scope statements of the form "applies to tendons." | The data[^anat-data] and the anatomy axis record[^cde-axis] | Recorded as needing a derived is-a overlay from the RadLex track |
| 44 | External-code coverage is uneven and the lineages disagree on where SNOMED CT lives. The current set promotes it to its own field pair on 1,782 records; the original keeps it inside a general codes list on 1,732. 608 current records carry no code at all. | The two data files. See [the data model](/semantic-foundation/anatomic-locations/data-model.md) | |
| 45 | `acrCommonId` is named two ways in the same repository: the curation field reference calls it an ACR Common identifier, the completed schema plan calls it an ACR Common Data Element identifier. It has the widest coverage of any code field, 2,025 of 2,926, and appears nowhere in the original lineage. | Curation reference against the schema plan[^anat-normalized] | |
| 46 | `lung` is contained by `pleural space` in the current data. Anatomically odd, and any check that walks containment upward from a lung location passes through it. | The data[^anat-data], flagged in the gap log[^cde-gaps] | |
| 47 | The laterality build reads the curation convention backwards, inverting the left and right references, which is exactly the inversion the migrated convention warns about. Open as issue 39, unassigned. | Issue 39[^fm-issue-39]. See [laterality conventions](/semantic-foundation/anatomic-locations/laterality-conventions.md) | `findingmodel` |
| 48 | Counts in the completed normalized-schema plan differ from the current file: 2,901 entries against 2,926, part-of references 1,101 against 1,123, and per-region counts differing by a few dozen. Almost certainly two snapshots rather than a contradiction, but nothing records what changed or when. | The plan[^anat-normalized] against the data[^anat-data] | |
| 49 | Unverified: whether the six named node requests in the gap log have been carried to the RadLex anatomy track anywhere outside that log, since issue 3 has no comments. | The gap log[^cde-gaps] against issue 3[^radlex-issue-3] | |
| 50 | Unverified: whether the wrapper library ever reached PyPI. Its README says installation is pending and the site roadmap still lists publishing as open. Also unverified: whether the anatomic locations database manifest and its remote storage are public, since only the JSON source URL appears in the plan. | The README and site roadmap | |
| 51 | Moving the three original anatomic location repositories to the `openimagingdata` organization was a TODO in 2024 and has not happened. | The TODO list. See [the anatomy roadmap](/roadmap/anatomic-locations-and-radlex.md) | |

# Exam types and terminologies

| # | The discrepancy | Sources | Who decides |
|---:|---|---|---|
| 52 | No exam type artifact exists: no curated LOINC list, no exam-to-body-part map, no modality or body part axis parsing, despite three repositories describing the same goal since 2022. No repository claims the area. | Three repositories. See [the exam types roadmap](/roadmap/exam-types.md) | |
| 53 | The Exam Finding List specification requires exam information "keyed by a curated list of LOINC codes." That list has never been published, so every producer chooses its own code. | The specification. See [Exam Finding List](/data-structures/exam-finding-list.md) | |
| 54 | The 2024-01-25 site post describes an "Exam Type library based on LOINC Playbook" as one of two existing utility libraries. It was never built. | Site post against the repositories. See [site articles](/history/site-articles.md) | |
| 55 | LOINC descriptions are inconsistent in the sample data. One code appears as both "CT Chest WO contrast" and "CT Chest Without Contrast"; two different codes carry descriptions naming the same abdomen and pelvis CT without contrast. | Sample data. See [existing building blocks](/semantic-foundation/exam-types/existing-building-blocks.md) | |
| 56 | The exam-scoped region fallback map is keyed by exam name rather than by LOINC code and is explicitly partial, its list ending in "etc." A coded exam type artifact would have to replace it. | Assignment rules[^anat-rules] | |
| 57 | The finding model corpus uses two system strings for one terminology: `SNOMED` on 27,773 index codes and `SNOMEDCT` on 89. The lookup tooling uses `SNOMEDCT` for BioPortal and `SNOMEDCT_US` for UMLS. | The corpus against the tooling. See [ontologies used](/semantic-foundation/terminologies/ontologies-used.md) | |
| 58 | No source in any repository states who governs FMA, so the bundle says only that it is distributed through BioPortal. | Not found in any source | |
| 59 | Unverified: RadElement set counts come from the public API read 2026-09-21, not from the RadElement site, which renders client-side. Also unverified: whether the `common_data_elements` snapshot of 145 sets is regenerated on any schedule, since its README says "periodically updated" with no cadence. | The API against the site | |

# Data structures

| # | The discrepancy | Sources | Who decides |
|---:|---|---|---|
| 60 | Neither the Exam Finding List nor the Imaging Problem List has a published JSON Schema. Both sample files carry a `$schema` URL that resolves to nothing. This is the substance of issue 1.[^ipl-issue-1] | Sample data against the specification. See [the IPL data model roadmap](/roadmap/ipl-data-model-system.md) | `imaging-problem-list`, through issue 1 |
| 61 | Imaging Problem List temporal status exists as four computed states in viewer JavaScript on the development branch, and as a three-state scheme in the prose on `main`. It is neither specified nor stored as a field. Whether it is part of the data model is unresolved. | Viewer code against the domain notes and the viewer README. See [Imaging Problem List](/data-structures/imaging-problem-list.md) | |
| 62 | Imaging Problem List entry counts for the same example patient differ across three artifacts: 98 in the deployed viewer bundle, 131 after the 2026-06-10 regrouping, 123 in the second-generation generated bundle. Probably three snapshots, but no document reconciles them. | Three artifacts on the same repository. See [sample data](/data-structures/sample-data.md) | |
| 63 | The deployed viewer data bundle was never re-enriched. On both branches the viewer's own data directory holds the 98-entry, location-free list, while only the sample directory and the second-generation public data carry the anatomy-grouped version. The live demonstration therefore shows pre-anatomy data. | The two data directories. See [the viewer profile](/applications/imaging-problem-list-viewer.md) | `imaging-problem-list` |
| 64 | Anatomy enrichment counts disagree with the inventory that reported them. Reading the files gives 276 observations on the development branch with 274 carrying a location, against 275 on `main`; the inventory reported 260 of 275. The two unlocated findings are ones the assignment rules deliberately leave unassigned. | The files against the inventory. See [sample data](/data-structures/sample-data.md) | |
| 65 | Attributes ride in `Observation.component` in every OIDM encoding. The IHE profile states that `component` "is not used" and prefers `hasMember`. The deck names the profile as the Exam Finding List's target representation, so the two positions are directly opposed. | The profile extract[^idr-extract] against the documented mapping and the lineage samples. See [IHE IDR alignment](/data-structures/ihe-idr-alignment.md) | The extract lists it as an item to raise during public comment |
| 66 | Three positions on diagnoses. The profile routes positive clinical findings to `Condition` and negatives to `Observation`. The next-generation working default makes every report assertion, diagnoses included, an `Observation`. The Imaging Problem List FHIR mapping does use `Condition`, one per finding type. | The profile extract[^idr-extract], the next-generation notes, and the specification | |
| 67 | Vocabulary collision on "finding" and "observation". The profile's "finding" is the presence determination and its "observation" is closer to a data element value; OIDM's finding model is the named entity and its Observation is the whole coded object. Flagged in the extract; no resolution. | The profile extract[^idr-extract] | |
| 68 | The documented Imaging Problem List FHIR mapping names a container called "Report", which is not a FHIR resource name. The mapping is otherwise resource-accurate. | The specification. See [FHIR mapping](/data-structures/fhir-mapping.md) | |
| 69 | No provenance field is specified anywhere. The Exam Finding List specification requires "some kind of provenance marker," the sample files have none, and the only precedent overloads the FHIR `status` field, `preliminary` for artificial intelligence and `final` for a radiologist. The deck's AI-validation priority depends on this. | Specification, sample data, lineage samples, deck[^deck]. See [provenance](/glossary/provenance.md) | |
| 70 | Coding assigns finding codes and location codes but not attribute codes, so an extraction-derived Exam Finding List carries uncoded attribute keys apart from presence. | The coding design[^coding-design]. See [finding and location coding](/applications/finding-and-location-coding.md) | |
| 71 | Anatomic-compatibility reconciliation. Generic and specific locations for the same finding code across exams produce separate Imaging Problem List groups. Deciding whether they are the same problem is a named, unstarted step. | Assignment rules[^anat-rules] and the anatomic location plan. See [the IPL data model roadmap](/roadmap/ipl-data-model-system.md) | `imaging-problem-list`, as a named follow-on |
| 72 | The technical imaging findings catalog is a draft whose own open question is whether technical-observation and clinical-interpretation entries should be separate or merged in the ontology. No coverage audit has been done. | The draft. See [technical imaging findings](/data-structures/technical-imaging-findings.md) | |
| 73 | The extraction model classes were renamed. The plan specifies one pair of names; the shipped code on the same commit uses another. The inventories and the phase briefs carry the plan's names. The bundle uses the shipped names. | The plan against the code. See [Observation](/data-structures/observation.md) | |

# Applications

| # | The discrepancy | Sources | Who decides |
|---:|---|---|---|
| 74 | The coding pipeline is described two ways in the same repository at the same commit. An archived plan marked complete describes three language model calls per chunk with one combined search-term generator; the newer design document, implementation marked complete, describes four agents over merged findings with separate finding and location term generators. The newer document is treated as current here. | Archived plan[^coding-archive] against the coding design[^coding-design]. See [finding and location coding](/applications/finding-and-location-coding.md) | `imaging-problem-list` |
| 75 | Draft autosave step numbering is inconsistent in the authoring application. One document says autosave begins on step 4; the other numbers draft editing as stage 3 of four after the wizard was cut from five steps. | Two documents in `FindingModelForge`. See [Finding Model Forge](/applications/finding-model-forge.md) | |
| 76 | Forge issue 13 asks for model editing. The unmerged branch answers it with AI-assisted iteration, and its plan states that manual edits are explicitly not permitted. Whether that closes the issue as filed is unresolved; the branch has no pull request. | Issue 13[^forge-issue-13] against the branch plan | `FindingModelForge` |
| 77 | The second-generation viewer names a Cloudflare Pages project in its plan. That address returned HTTP 404 on 2026-09-21. Either it was never deployed or the project name differs. | The plan against a live check. See [the viewer profile](/applications/imaging-problem-list-viewer.md) | |
| 78 | The early extraction prototype is classed as lineage in the repository map and given an applications project profile by the build plan.[^plan] | Repository map against the build plan | |
| 79 | The finding model catalog site's deployed address is not stated in its repository. The address used here was derived, and one agent confirmed it returns HTTP 200 while another did not fetch it. | The repository against the repository map. See [content catalog](/semantic-foundation/finding-models/content-catalog.md) | |
| 80 | Unverified: whether the authoring application's peer-review layer, complete on its development branch, is live at its deployed address, since the deployed build corresponds to a stale `main`. | Not verifiable from the repository | |
| 81 | Unverified: whether the July 2026 active plans on the extraction platform's development branch have progressed since the 2026-07-22 tip commit. | Not verifiable from the repository | |

# The project narrative

| # | The discrepancy | Sources | Who decides |
|---:|---|---|---|
| 82 | Several goals attributed to the project lead in the phase briefs appear nowhere in the repositories: the detailed exam type goals, the four-part Imaging Problem List goals, the stated need for anatomic location tooling, and the phrasing of the metadata and relationship direction. The build plan records them only as short parentheticals in its target tree. They are cited throughout the roadmap to the 2026-09-20 planning interview and need the project lead to confirm the wording. | The build plan[^plan] against the repositories. Affects [exam types](/roadmap/exam-types.md), [the IPL data model roadmap](/roadmap/ipl-data-model-system.md), and [the anatomy roadmap](/roadmap/anatomic-locations-and-radlex.md) | Project lead |
| 83 | The "precision geography" framing requested in one phase brief does not appear in the deck. The bundle uses the deck's own wording instead. If the phrase is the project lead's, it needs a source before it can be quoted. | The deck extract[^deck] | Project lead |
| 84 | The site's "How to Get Involved" page, dated August 2023, is partly stale: it names a working group that does not match current structure and carries a meeting placeholder. Whether meetings occur is unverified. | The live site. See [getting involved](/overview/getting-involved.md) | Project lead |
| 85 | The deck names a specific reporting vendor as its vendor-driven example. Whether that should be generalized in public documentation is unstated. | Deck[^deck] | Project lead |
| 86 | The About page promises TypeScript and JavaScript, Python, and C# libraries. Two exist only as lineage, and no C# library was ever written. | The live site against the repositories. See [lineage repositories](/history/lineage-repositories.md) | Project lead |
| 87 | The ACR-OIDM Structured Imaging Results Working Group is a call to action in the deck. No record of it being convened exists in any source read here. | Deck[^deck]. See [roadmap 2026](/roadmap/roadmap-2026.md) | ACR and the project lead |
| 88 | The Open Imaging Reporting SDK is a strategic pillar in the deck with no repository, code, or specification. | Deck[^deck]. See [the reporting SDK](/applications/reporting-sdk.md) | |
| 89 | Unverified: the date the project was renamed from Open Radiology Data Model. Evidence bounds it between February and June 2023. | Site and repository history. See [timeline](/history/timeline.md) | |
| 90 | Unverified: Slack workspace activity; the deck carries a month but no day; three lineage repositories have push dates later than their default-branch tips. | Various | |

# Defects to file upstream

Errors in source documents rather than open design questions. Each could become an issue in its home repository. The last four rows are defects in this bundle itself.

| Repository | Path | Defect |
|---|---|---|
| `openimagingdata/findingmodels` | `schema/finding_model_schema.md` | Numbers the first choice value `.1` where the code writes `.0`; omits `anatomic_locations` from the full model; states none of the enforced length and cardinality constraints |
| `openimagingdata/findingmodels` | one CDE-derived definition under `defs/` | Spells a presence value "indeterminant" |
| `openimagingdata/findingmodel` | `tasks/STATUS.md` | Dated 2026-01-18 and stale: it predates the facets pivot and all of the `dev` branch work |
| `openimagingdata/findingmodel` | `docs/anatomic-locations.md` | The `stats` example shows 4,847 records and 10 regions; the real dataset has 2,926 and 9 |
| `openimagingdata/findingmodel` | `.claude/skills/manage-anatomic-locations/reference/json-schema.md` | Lists `"Spine"` as a common region value that no record uses and no enumeration defines; omits the `sexSpecific` and `anatomicLocationsId` fields present in the data |
| `openimagingdata/findingmodel` | `notebooks/data/anatomic_locations_noembed.json` | 111 records carry a `partOfRef` pointing at themselves and one carries a self-referential left reference |
| `openimagingdata/imaging-problem-list` | `sample_data/` and the viewer data bundles | Both structures carry a `$schema` URL that resolves to nothing |
| `openimagingdata/imaging-problem-list` | `CLAUDE.md`, `viewer/README.md` on `main` | Describe a three-state temporal scheme where the shipped viewer computes four; state "`.1` = present, `.0` = absent" as if the value codes were semantic |
| `openimagingdata/imaging-problem-list` | `viewer/data/` on both branches | Holds the pre-anatomy 98-entry Imaging Problem List, so the deployed demonstration is stale against the sample data |
| `openimagingdata/imaging-problem-list` | `docs/archive/finding-and-location-code-assignment-plan.md` | Describes a superseded three-call pipeline without saying it is superseded by `docs/coding-agent-design.md` |
| `openimagingdata/FindingModelForge` | `docs/DRAFT_WORKFLOW.md`, `docs/finding-model-creation-workflow.md` | Disagree on the step at which draft autosave begins |
| `openimagingdata/CDEStaging` | `docs/Authoring.md` | Two sentences long, saying the authoring guide "will be hosted here as well." It was never written, while two incompatible markdown conventions are in use in the repository[^cdestaging-authoring] |
| `openimagingdata/CDEStaging` | `README.md` | Describes `definitions/` as holding common data elements in JSON format; the files follow the finding model attribute shape instead |
| `openimagingdata/common_data_elements` | `schema/cde.schema-1.0.json`, `cde.schema-1.1.json` | Both declare the same `$id`, pinned to `v1.0.0`, as does the canonical copy in the CDE repository |
| `openimagingdata/openimagingdata.org` | `schemas/schema_differences.md` | A 2023 snapshot recording gaps that schema 1.1 has since closed |
| `talkasab/anatomiclocations.org` | `docs/index.markdown` | The exam type roadmap line spells LOINC as "LOIC" and RadLex as "Radlex" |
| `RSNA/RadLex` | `RadLex.owl` | Three `Source` annotation values spell Playbook as "PLaybook" |
| `openimagingdata/oidm-knowledge` | `knowledge/glossary/open-imaging-reporting-sdk.md` | Cites a site URL that returns HTTP 404; the working URL, used in three other documents here, ends `oidm-based-next-gen-reporting-assistance/` |
| `openimagingdata/oidm-knowledge` | `knowledge/references/imaging-problem-list-example.md` | Says the example holds 123 findings "across eight exams"; the file has ten distinct report identifiers over ten exam dates |
| `openimagingdata/oidm-knowledge` | `knowledge/repositories/repository-map.md` | Gives last-commit dates for the three anatomic location repositories and for RadLex that do not match their default-branch tips, and names RadLex's branch of record as `main` although the search and curation pipeline exists only on an experiment branch |
| `openimagingdata/oidm-knowledge` | `knowledge/plans/2026-09-20-knowledgebase-build-plan.md` | The target tree sketches the Playbook glossary file as `loinc-playbook.md`; the file written is `loinc-rsna-radiology-playbook.md` and every link uses that name |

[^deck]: "Open Imaging Data Model 2026 Status Update", January 2026
[^prose-schema]: Finding Model Schema, prose mirror, findingmodels main branch
[^fm-code]: finding_model.py, findingmodel main branch
[^fm-metadata-types]: types/metadata.py, feature/metadata-cleanup branch
[^fm-optimization]: Finding enrichment pipeline optimization proposal, findingmodel main branch
[^fm-adr2]: ADR 0002, split-agent assignment architecture
[^fm-issue-42]: findingmodel issue 42
[^fm-issue-39]: findingmodel issue 39
[^cde-metadata-note]: OIFM metadata fields note, next-gen-2026 branch
[^idr-extract]: IHE Imaging Diagnostic Report Phase II extract, next-gen-2026 branch
[^cde-context]: CDE vocabulary working glossary, next-gen-2026 branch
[^cde-axis]: The anatomy axis, current state, next-gen-2026 branch
[^cde-gaps]: Anatomic locations gaps and node requests, next-gen-2026 branch
[^cde-schema-canonical]: cde.schema.json at the root of ACR-RSNA-CDEs
[^cde-schema-11]: cde.schema-1.1.json, common_data_elements repository
[^cdestaging-issue-1]: CDEStaging issue 1
[^cdestaging-authoring]: CDEStaging authoring guide stub
[^ipl-issue-1]: imaging-problem-list issue 1
[^ipl-claude-dev]: imaging-problem-list domain model notes, dev branch
[^coding-design]: Coding agent design, imaging-problem-list dev branch
[^coding-archive]: Finding and location code assignment plan, archived
[^anat-rules]: Anatomic location assignment rules, dev branch
[^cleanup]: Definition Cleanup Plan, findingmodels main branch
[^lists-readme]: MGB exam-oriented sub-taxonomies README
[^anat-data]: anatomic_locations_noembed.json
[^anat-normalized]: Anatomic locations normalized schema plan, completed
[^anat-docs]: Anatomic locations package documentation
[^radlex-issue-3]: RSNA/RadLex issue 3
[^forge-issue-13]: FindingModelForge issue 13
[^fm-issue-15]: findingmodels issue 15
[^plan]: Knowledgebase build plan
