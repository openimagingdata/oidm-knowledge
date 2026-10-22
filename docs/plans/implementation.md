# Source-to-pages implementation plan

Updated 2026-10-19. This remains the single planning record. The owner has approved moving the old bundle to `archive/knowledge` and reconstructing the graph from fresh documents in `knowledge/`. The conceptual outline remains under collaborative development. Do not create parallel restructure plans or dashboards.

## Current task: separate the accumulated changes into commits

The owner paused the content-plan discussion to reconcile the accumulated
working-tree changes. Finish this work before resuming the unanswered review
question or drafting knowledge documents.

1. Original-file download and verification commands: complete in `21e37a0`,
   now on `bootstrap`. The owner approved this first commit. It contains the
   manifest, commands, tests, CI checks, and instructions. All original
   working-file contents were preserved when incorporating it.
2. Planning and reference consolidation: prepared for review, authorized October 19.
   Preserve owner guidance, the approved outline, and the unanswered drafting
   question; account for removed plans and relocated previews. Repair links
   in the proposed commit while leaving the archive move and website changes
   unstaged. Check the complete proposed commit independently of the working
   tree, update this plan and the relevant logs, then request commit permission.
3. Knowledge reset: commit the archive move, fresh index and log, and related
   documentation last. The move already exists in the working tree, but has
   not been committed. Do not start concept drafting.

The owner's Claude session owns the website changes, including deployment
configuration and website task routing outside `site/`. Split shared root
files by purpose; do not stage the website's changes with either remaining
commit.

The temporary `reconcile-knowledge` worktree and branch have been removed at
the owner's request. Continue in this original checkout. The tab created for
the worktree was already closed when checked. No website files were changed.
Keep this plan, the handoff, references, and logs aligned with each proposed
commit and the final state. Each remaining commit needs separate permission.

## Organizing decisions and withdrawn approach

The project lead considers the generated knowledge bundle ‘basically DOA’: useful material is buried in unsupported, unreadable generated prose. Treat it as material to mine critically for relevant, supported ideas. Its structure and apparent coverage are not a foundation to preserve by default.

The owner has approved the five-section organization, document boundaries, starting node, and source approach described below. Preserve those decisions. The node-drafting workflow and remaining execution-plan aspects are still under review. Once repository reconciliation is finished, resume that review one aspect at a time, with short responses and one focused question. Read recorded owner guidance before asking the owner to repeat it. Do not begin drafting yet.

The assistant-selected SIIM 2026 deck-first pilot is withdrawn. That dated presentation is one source among others, not the starting point or organizing authority. Completed planning cleanup and source-storage/tooling work remain complete. Historical maps and agent reviews preserve context, not authorization to resume the withdrawn sequence.

## Intended pipeline

Implement the pipeline **private Tigris sources → detailed references → repository-only OKF knowledge graph → public presentation pages**. The October 2 clarification removes the separate internal website from scope. The intended graph and presentation remain separate layers. This does not endorse the existing generated bundle or settle its replacement organization.

| Layer | Destination | Contract |
|---|---|---|
| Original evidence | Private `oidm-knowledge-sources` bucket; local collection at `~/data/oidm-knowledge-sources` | Preserve originals, extraction artifacts, checksums, source dates, and sensitivity. Track a reviewed `docs/sources-manifest.json`, not raw files or private local inventory metadata. |
| Processed summaries | `knowledge/references/` | Detailed OKF references with source locators, claims, qualifications, and permitted or redrawn figures. |
| Knowledge graph | `knowledge/` | Comprehensive, interconnected idea documents citing references. Publicly readable in Git, but not a separate website. |
| Presentation | `site/content/` | Curated explanations for outsiders. Separate track, planned in `site/ROADMAP.md`; only this directory and its intended assets feed the public site. |

The owner approved five sections: Foundation Context, Data Structures, SDKs, Use Cases, and Sample Applications, with an Overview introducing their connections. Meaningful nested groups and substantive concept documents are approved; individual document scopes and unfinished outline sections remain under discussion. Repository artifacts supply evidence, and the presentation can summarize and cite fuller knowledge accounts.

Supporting material has distinct homes:

- [Project direction](../references/project-direction.md) preserves dated owner statements and source-review observations used by existing citations.
- [Current owner guidance](../references/knowledge-organization-owner-guidance.md) preserves the original nested outline and later SDK, Applications, terminology, and archive instructions in the owner's words.
- [Claude's outline review](../references/knowledge-outline-claude-review.md) preserves the full initial agent review. Its proposals are distinct from owner decisions and refer to an earlier version of the outline.
- [Idea coverage](../references/idea-coverage.md) accounts for the 87 inventoried ideas and links their historical evidence. It is a reference, not another work queue.
- [Board summaries](../references/linked-diagrams/index.md), [brand guidance](../brand/README.md), and the [tooling comparison](../references/okf-tooling-comparison.md) retain completed research and import results.
- [Clinical-information reconciliation research](../references/clinical-information-reconciliation.md) records primary sources and open questions for Imaging Persona, distinct from the specific SDK capability for longitudinal finding linking.
- `docs/HANDOFF.md` provides working instructions. `DEV_LOG.md` records completed work; `CHANGELOG.md` records reader-facing changes.
- Ignored `scratch/review/` holds review renders and working research. `.peruseshow` exposes that directory locally. Accepted diagram sources and assets remain tracked beside their content.

## Current state

| Work | State | What remains |
|---|---|---|
| Plan consolidation and temporary-file cleanup | Prepared October 2; separate commit under review October 19 | Check preserved guidance, reference links, and preview copies before requesting commit permission. |
| Original source collection | All 307 remote objects match local sizes/SHA-256; manifest and recovery tools complete | 25 source groups / 118 selected artifacts are recoverable; selection does not establish content priority or approval. |
| Board capture | Complete: 15 boards, native exports and metadata retained | Content use awaits the agreed approach; capture dates are not idea dates. |
| Brand import | Complete: 16 assets, style guide, checksum manifest | Theme application is deferred. Preserve assets through the presentation build change. |
| Knowledge graph | Reset prepared in the working tree; archive move and fresh index/log remain outside the planning-consolidation commit | Commit the reset last. Drafting remains paused pending the remaining plan review. |
| Presentation content | Moved to `site/` on 2026-10-05 | Separate track; see `site/ROADMAP.md`. |
| Site | Website-session working-tree changes, excluded from this commit | Claude owns build and task-routing integration. Consult the instructions for the checkout being used; do not assume the `site` task namespace is available before that change is integrated. |

This plan records content agreement separately from publication approval. A review by an agent, or an agreed paragraph, does not itself supply the project's human verification stamp.

## Root task integration with the separate website, October 6

Authorized by the owner-approved site-session handoff. This is separate from the pending review of the knowledge tree's physical organization. Do not edit `site/` or stage another agent's changes.

This records the October 6 work in the shared working tree. Its code changes
and command-routing documentation belong to the website session's separate
commit; they are not included in the planning-consolidation commit.

- [x] Include `site/Taskfile.yml` under the `site` namespace in the root task file; remove duplicate website tasks and hostname variables from the root.
- [x] Keep root verification and review tasks for the OKF graph in `knowledge/`, with descriptions and default review-list scope reflecting that role. Retain `tools/verify.py`.
- [x] Update root documentation to describe the website's implemented `site/content/` input, independent checks and review tools, and `task site:...` commands.
- [x] Check task discovery and dry-run routing without deploying or stamping reviews; run root and site validation, then update the plan and logs for the final state.

Complete. Task 3.54.0 discovers the included namespace, following [Task's include documentation](https://taskfile.dev/docs/guide/includes). Root `task check` passes with zero errors or warnings; `task site:check` passes for 12 pages. Eight dry runs confirm website command routing and separate knowledge and website verification tools. Root review listing defaults to `knowledge/`. Updated documentation links resolve, and all 42 site-owned paths match the recorded baseline. No deployment, review stamping, site edits, or commit occurred.

## Completed work

The records below describe completed cleanup and source infrastructure. Finish separating the accumulated changes into commits before resuming the organizing discussion.

### 0. Consolidate this repository's planning records

- [x] Write this replacement plan before reorganizing the records.
- [x] Integrate the pipeline, current decisions, presentation map, and remaining work here.
- [x] Extract cited owner guidance into a reference and combine the idea inventories into one coverage reference.
- [x] Delete superseded and completed plans after preserving their useful evidence and results.
- [x] Move temporary previews to ignored `scratch/review/`; expose that area through `.peruseshow` and preserve accepted assets.
- [x] Repair references; update the handoff, README, contributor/site guidance, bundle log, development log, and changelog.
- [x] Run strict OKF validation, the house checker, documentation-link checks, and ignore/Peruse checks. Review the final document set.

Done means `docs/plans/` contains this one plan, obsolete execution instructions are removed, and citations still reach their evidence. Consolidation does not establish an approved content organization.

For the separate October 19 consolidation commit, retain `knowledge/plans/`
with the rest of the old bundle. Its removal and any bundle citation repairs
belong to the knowledge reset. The implementation plan here governs current
work; the old bundle's build plan remains historical evidence.

#### Account for the removed planning files

The removed records remain available in Git at `21e37a0`. Their current homes
and dispositions are listed below. Historical source links use pinned commits
so deleting a plan does not silently change the cited evidence.

| Removed records under `docs/plans/` | Preserved material or disposition |
|---|---|
| `2026-09-22-layout-plan.md`, `2026-10-01-sources-and-layers.md`, `restructure-around-project-ideas.md`, `restructure-joint-notes.md`, `idea-placement.md` | Current decisions and the nested outline are in this plan. Owner statements and source qualifications are in `docs/references/project-direction.md`; historical placement and source entries are indexed in `docs/references/idea-coverage.md`. Superseded execution instructions are withdrawn. |
| `idea-inventory-semantic.md`, `idea-inventory-structures-and-uses.md` | All 87 inventoried ideas have entries in `docs/references/idea-coverage.md`, linked to their historical source entries. The inventory is an omission check, not an execution queue. |
| `2026-09-30-brand-assets.md` | Import results are retained in `docs/brand/README.md`; assets, original style guide, and checksums stay in their established locations. |
| `2026-10-01-linked-diagrams.md` | Capture results and qualifications are retained in `docs/references/linked-diagrams/index.md`; all 15 summaries remain. |
| `2026-10-01-okf-tooling-comparison.md`, `2026-10-01-okf-tooling-review.md` | Completed research remains in the corresponding `docs/references/okf-tooling-*.md` reports. No tool migration is authorized. |
| `lean-content-pass.md`, `lean-content-full-review.md`, `lean-content-coverage.tsv` | Historical review results remain in `DEV_LOG.md`; the complete coverage table moves to `docs/references/lean-content-coverage.tsv`. Those editorial passes do not approve the rejected bundle. |
| `repository-review.md`, `restructure-codex-drafts.md`, `restructure-dashboard.md` | Historical assessments, draft-review results, and dispositions remain in `DEV_LOG.md`, the project-direction reference, and Git history. The dashboard and obsolete assignments are retired. Private review records stay outside Git. |
| `renders/*.png` | All 29 tracked previews have identical copies in ignored `scratch/review/renders/`. `.peruseshow` exposes the review directory locally; accepted assets stay tracked. |

The owner's October outline and subsequent clarifications remain verbatim in
`docs/references/knowledge-organization-owner-guidance.md`. Claude's review and
its later correction remain in `docs/references/knowledge-outline-claude-review.md`.
The clinical-reconciliation research remains a reference, not a design decision.
This consolidation does not reopen approvals or approve the unanswered node-review
workflow.

October 19 checks pass on an exported copy of the proposed commit: strict OKF
conformance, house checks, and manifest validation report zero errors or
warnings. All 115 existing concepts and the old bundle's planning files remain
unchanged. All 169 local documentation links, eight pinned Git source paths,
and 87 inventory source anchors resolve. The historical coverage table and
all 29 tracked preview copies match their originals byte for byte. Owner
guidance, the corrected review record, and the full conceptual outline are
unchanged. Website and knowledge-reset paths are excluded from staging.
Commit permission remains pending.

Astra independently reviewed the staged consolidation on October 19 and judged
it ready with minor fixes. The application inventory is now explicitly ongoing
work rather than a prerequisite for the agreed first node. The site state row
now identifies website-session work outside this commit, rather than assuming
its task namespace exists. The handoff's repeated checkpoints were shortened,
and the staged contributor instructions no longer require a migration ledger.
The review found no significant lost decision. This is agent review, not owner
approval of the plan's remaining questions or permission to commit.

Validation completed October 2: both bundle validators pass with zero errors or warnings; 404 local documentation links resolve; all 116 moved previews match their recorded checksums; the Quartz build succeeds. Peruse's local parser confirms the review allowlist and ancestor traversal; its running server was unreachable from this environment, so live UI verification remains unperformed.

### 1. Establish recoverable source storage

Complete, 2026-10-02. [Source instructions](../sources.md), [manifest](../sources-manifest.json), and `tools/sources.py` define the workflow.

- [x] Relocate all 307 files to `~/data/oidm-knowledge-sources`, verify local checksums, and preserve existing paths through the ignored `sources` symlink.
- [x] Download all 307 remote objects to an isolated directory and verify every size and SHA-256 against the local inventory. No remote files changed.
- [x] Classify the full collection. The tracked manifest selects 25 source groups and 118 artifacts. Retain 152 older screenshots, 31 private review files, five working-research files, and one private capture index outside the default source manifest.
- [x] Record source IDs, organizations/dates where known, status, sensitivity, handling rules, and artifact keys, sizes, hashes, added timestamps, roles, and parent relationships. Unknown dates remain unknown; board material defaults to internal handling until publication evidence is available.
- [x] Implement `task sources:manifest`, `task sources:pull`, and `task sources:check`. Pull verifies bytes before adding files and refuses to overwrite differing local content. Manifest validation and recovery tests run in CI without private files or credentials.
- [x] Test recovery of all 118 artifacts into an empty directory using a separate copy of the tool and manifest. A second pull skipped all files. Eight tests cover invalid paths/lineage, corrupt or failed transfers, conflicts, symlinks, and concurrent destination creation.
- [x] Check access evidence: bucket settings disable object ACLs; anonymous HEAD requests to a deck, board capture, and private review object returned 403. This is sampled access verification, not an exhaustive policy audit. No access settings changed.
- [x] Document authentication, local path overrides, source selection, compatibility links, manifest maintenance, and the distinction between storage verification and content approval. Update entrypoints and logs; repository checks pass.

Private `.local-inventory.json`, `.remote-inventory.json`, `.remote-verification.json`, and `.classified-inventory.json` account for the full collection outside Git. `docs/sources-manifest.json` covers the selected source artifacts only. Whole-packet manuscript files remain restricted containers; hash verification did not inspect reviewer correspondence.

## Reconstruction method and temporary archive, October 6

The owner selected `archive/knowledge` as the temporary home for the old generated bundle. Preserve its current files and working-tree edits when moving it. Build the new graph in `knowledge/`, following the owner's nested outline. The outward-facing pages in `site/` remain a separate workstream.

### Write fresh, then check for omissions

1. Define the concept and its place in the owner's outline.
2. Examine the relevant original sources and processed references, identifying supported current thinking and unresolved questions.
3. Write a new knowledge document from an empty file. Do not use an archived document as a template or edit it into the replacement.
4. Check the archived material afterward for relevant ideas or source leads omitted from the fresh draft. Verify anything recovered against its sources before adding it.
5. Connect the new document to related concepts and review substantive questions with the owner, one at a time.

The archived prose, file boundaries, and hierarchy have no organizing authority. Existing source-storage and recovery tools remain complete. Processed references added to `knowledge/references/` must be source-grounded; moving the archive does not approve its generated reference prose.

### Delete the archive when recovery is complete

`archive/knowledge` is temporary. Delete it after the worthwhile, relevant, supported material has been recovered or its source leads incorporated into the new graph. Do not retain it as a permanent second knowledgebase.

Before deletion, review recovery coverage, preserve recorded owner guidance outside the disposable archive, and ensure no active document depends on an archived file. Record deliberately excluded or unsupported material where needed to explain the recovery review; do not copy discarded prose merely to preserve volume. The owner explicitly requested this final deletion. Commits still require separate permission.

The first three completed items below record working-tree preparation on
October 6. They remain outside this planning-consolidation commit and must be
checked again when preparing the knowledge reset.

- [x] Move the existing bundle intact to `archive/knowledge` and verify file preservation: 138 files, 1,181,586 bytes, all SHA-256 checksums unchanged.
- [x] Establish a clean `knowledge/` with its index and change log; no inherited concept prose.
- [x] Update repository instructions and preserve recorded owner guidance in `docs/references/project-direction.md`, outside the disposable archive.
- [ ] Develop the remaining outline and reconstruct knowledge documents using the method above.
- [ ] Review recovery coverage and remove active dependencies on the archive.
- [ ] Delete `archive/knowledge` once the useful material has been recovered; update documentation for the final state.

## Proposed knowledge-node outline, October 5

Status: discussion draft, compiled at the project lead's request for Claude review. Foundation Context and Data Structures follow the owner's supplied outline. SDKs combine the assistant's proposed outline with the owner's subsequent additions. The proposed boundaries between knowledge nodes are assistant suggestions. They do not define a clinical schema or assign file paths. The owner has clarified that Use Cases describe envisioned uses and Sample Applications describe actual implementations, including demos and prototypes. The former Applications grouping is now the working Use Cases outline; the Sample Applications inventory remains to be developed.

### Organizing contract

- Organize by concepts and their relationships, reflecting current thinking. Source artifacts and historical development do not determine the conceptual map. Source dates, pinned revisions, and qualifications still support individual claims.
- Distinguish this repository's OKF knowledge nodes from the clinical graph objects those nodes describe. For example, an OKF node about Measurement explains that clinical definition type; it does not imply one OKF file per clinical measurement definition.
- Each proposed substantive node has one primary home and links to related nodes elsewhere. Section introductions are navigation and synthesis knowledge documents. A public page can distill several knowledge nodes; a knowledge node is not automatically a public page.
- The carefully crafted presentation pages are valuable and are being developed separately by the owner and another agent. Preserve their content and recorded agreements. This outline does not authorize replacing, moving, or editing them.
- Keep shared definitions distinct from patient-specific assertions, and link the two. Keep descriptive characterization distinct from assessment. Preserve proposals, uncertainty, and differing representations within their conceptual knowledge documents.
- Use the owner's current working abbreviation **FDe** for assertion subjects/finding definitions, including diagnoses and other subjects. The exact membership of this umbrella, particularly assessment definitions, is an open modeling question.
- The owner now explicitly describes object references as pointers to definitions, anatomy, and attribute subjects. This supersedes the older prohibition on that word for this discussion; the graphs remain interconnected.

### Foundation Context

The hierarchy below preserves the owner's outline. Indentation supplies the context for each topic. Topics identify the knowledge to capture; their final division into individual OKF files remains under discussion.

* Introduction: Interconnected Knowledge
  - Shared definitions and relationships, separate from assertions about particular findings in a patient's imaging history.
  - How Foundation Context connects to those assertions.
* Assertion Subjects / Finding Definitions, including diagnoses and other subjects, abbreviated FDe
  - Overview of the knowledge graph schema
    - Taxonomy of assertion subjects: findings, diagnoses, assessments, and other subjects
      - Distinctions between subject kinds and their definition types.
      - Assessment definitions describe evaluation criteria; descriptive finding definitions describe what is being evaluated.
    - Properties of FDes
      - Names, synonyms, definitions, identifiers, external codes, and applicable metadata.
    - Relationships between FDes
      - Taxonomic, manifestation, causation, association, progression, component, and assessment relationships.
      - Properties of the relationships themselves.
    - Categorical attributes of FDes: Data Elements
      - Categorical descriptors, their permitted values, and their connections to finding definitions.
    - Measurements of FDes
      - Kinds of quantities used to characterize findings, such as length or CT density, and how Measurement definitions connect to finding definitions.
  - Examples of actual graphs
    - Supported definition-graph examples illustrating the schema and relationships.
    - Identify proposed example content separately from existing graph content.
  - OIFM and ACR/RSNA CDE repositories and their relationship
    - Collections of the same kind of definition content, with different review and release expectations.
    - Shared-schema direction and cross-linked identities.
  - Definition versioning and lifecycle
    - A versioning scheme for managing content updates.
    - Likely deprecation of older nodes with pointers to updated or replacing nodes.
    - Pointers may refer to specific versions of definitions.
    - The owner has established these concepts; the detailed scheme remains to be developed.
  - Using LLMs to drive creation of the system
    - Discovery of proposed definitions and associated information from report corpora.
    - Enrichment, content-guideline checks, and human review.
    - Connect to the SDK knowledge documents of reusable authoring capabilities.
  - Proposed authoring tool: evolution of FindingModelForge
    - Requirements for authoring and reviewing definitions and relationships.
    - Current content-guideline ideas and their ongoing development by the community through content creation and review.
    - Guidelines evolve with authoring experience; they are not a finished prerequisite for creating content.
    - Connect to reusable SDK capabilities and the application knowledge document to be developed later.
* Anatomy
  - Anatomic locations: curation and initial additions
    - Containment and part-of relationships.
    - Sex-specific anatomy, laterality, and other curated information.
  - Incorporating curated anatomic locations into RadLex
    - Integration of the project's curated locations and relationships.
    - Proposed added metadata, including tissue type.
    - Distinguish proposed additions from implemented RadLex content.
  - Relationships to other ontologies
    - SNOMED CT, TA2, FMA, and LOINC.
    - Explain the meaning and scope of mappings without assuming equivalence.
* Exam types
  - RadLex/LOINC Radiology Playbook
    - Exam definitions and existing building blocks.
  - Exam families
    - Preferred high-level examination families and their organization.
    - Review evidence from the owner's `../exam-types` project.
* Overall integration
  - FDe definitions and anatomic scope
    - Which anatomy a definition applies to, distinct from the actual location of a particular finding.
  - FDe definitions and exam types
    - Connections between definitions, modalities, and examination types.
  - Anatomic locations and exam types
    - Anatomy always, usually, or possibly included in an examination.
    - Connect to the proposed application for smarter selection of relevant priors.
  - FDes associated with non-imaging diagnoses and procedures
    - Relationships to clinical diagnoses and procedures, including surgeries.
    - External codes and qualified associations that help retrieve relevant patient history.
    - A likely association in Foundation Context does not establish a fact about a particular patient.

### Data Structures

This hierarchy preserves the owner's four main groups. The overall FHIR conversion knowledge document is added separately, following the owner's subsequent clarification. Specific representations remain nested under the structures they represent.

* Introduction: Developing imaging data structures
  - Explain the proposed structures and their connections to Foundation Context.
  - Ongoing community definition of these structures is an important thread of work.
  - Implementers contribute requirements and refinements grounded in real use of these ideas.
  - Distinguish current proposals, implemented representations, and unresolved design questions.
* Assertions / Observations
  - Overview: an application-layer data structure
    - Assertions about particular findings and other defined subjects.
    - Their connection to shared Foundation Context definitions.
  - What's contained
    - Pointers to FDe definitions and to anatomic locations.
    - Distinguish the identity of a definition from the identity of a particular assertion.
    - Pointers may identify specific definition versions; connect to Foundation content versioning.
  - Attributes
    - Pointers to sub-assertions with DataElement and Measurement subjects.
    - Values, units, presence, and uncertainty.
    - A measured value describes a particular finding, such as a pulmonary nodule's diameter of 8 mm.
    - The exact sub-assertion representation remains to be reviewed.
  - Sub-components
    - Component assertions and their identities, values, and relationships to parent assertions.
    - Connections to component constraints in the corresponding definitions.
  - FHIR representation
    - Observation objects, components, and connections.
    - Representation of attributes, sub-assertions, measured values, and provenance.
    - Connect to the overall bidirectional conversion philosophy and the SDK conversion capability.
  - Provenance and review
    - AI-generated assertions.
    - Technologist- or modality-generated assertions, including possible DICOM SR sources.
    - LLM extraction from report text.
    - LLM generation from radiologist interaction.
    - Radiologist review of AI-based tools, supporting evidence, and corrections.
* Exam Finding List / Imaging Diagnostic Report
  - Exam information
    - Pointer to exam type information.
    - Possible protocol information.
    - Other exam-performance information and pointers to DICOM data.
  - Collection of Assertions / Observations
    - Organization into Findings and Impression sections.
  - Relationships between assertions
    - Findings and diagnoses.
    - Sub-components and associations.
    - Connections from findings to impression assertions.
    - Distinguish relationships asserted about particular findings from general relationships between Foundation definitions.
  - FHIR Imaging Diagnostic Report representation
    - Exam information, assertion collections, sections, and connections.
    - Clarify the relationship between the application structure and the external representation rather than assuming identical objects.
    - Connect to the overall conversion philosophy and the SDK conversion capability.
* Imaging Problem List / Patient Imaging History
  - Finding-based organization
    - Connections to exam-level assertions and their evidence.
  - Basic applications and use as context information
  - Longitudinal tracking
    - Finding identity across examinations and association of observations.
    - Change, derived status, and succession.
    - Keep unresolved identity and status choices visible.
    - Describe how the imaging history represents these connections; link to the separate SDK node on making the connections.
  - FHIR representation
    - Proposed representation of finding identity and longitudinal histories.
    - Exact resources and profiles remain open.
    - Connect to the overall conversion philosophy and the SDK conversion capability.
* Imaging Persona
  - Patient facts relevant to imaging, organized in a standard way
    - Incorporates the Imaging Problem List and integrates wider patient history.
  - Information to include and how to represent it in the Imaging Persona
    - A knowledge node identifying the pieces of imaging-relevant patient information to retrieve and their proposed representations and relationships.
    - Developing these patient concepts and data structures is the first step toward defining the Imaging Persona.
    - The work is currently at a high, imprecise level. Record candidate information and open representation questions without presenting a settled schema.
    - Broader reconciliation of clinical information is a clinical-informatics research question. Use the [focused research reference](../references/clinical-information-reconciliation.md) to inform the discussion; its suggested implications do not settle the representation.
  - Exam-planning information
    - MRI safety, allergies, body habitus, and other relevant facts.
  - Clinical history extraction
    - Imaging-relevant oncology history, treatments, operative notes, and other clinical records.
    - Connect to the SDK capability for LLM-based clinical-history extraction.
  - Pathology results and diagnoses
    - Connections to Imaging Problem List elements.
  - Other non-imaging diagnoses possibly associated with imaging findings
    - Foundation associations help identify relevant documented history.
    - Retain the distinction between likely associations and actual patient facts.
  - Availability via FHIRcast
    - Proposed context integration.
    - Review what FHIRcast supplies and how the underlying data is retrieved.
* Bidirectional FHIR conversion: overall philosophy
  - Relationship between application structures and FHIR representations.
  - Conversion in both directions, preserving meaning, identities, relationships, evidence, and provenance.
  - Handling information without a direct equivalent and making conversion losses explicit.
  - Connect to the specific Observation, Exam Finding List, and Imaging Problem List representation knowledge documents above.

### SDKs

This hierarchy follows the collaborative SDK outline. It describes reusable capabilities and connects them to the concepts they operate on. Named packages appear with the capabilities they implement. The proposed grouping does not establish which capabilities are already implemented.

SDKs describe underlying reusable library code. Use Cases describe envisioned uses of that code; Sample Applications describe software actually implemented, including simple demos and prototypes.

* Introduction: Using OIDM in applications
  - Access shared knowledge and manipulate patient data structures.
  - Support authoring and maintenance of Foundation Context.
  - Identify available implementations and proposed capabilities.
* Accessing Foundation Context
  - Finding-definition search and identity resolution
    - Retrieve definitions by identifier; search names, synonyms, and properties.
    - Resolve collection identities, cross-links, and definition versions.
    - Access specific definition versions and follow deprecation or replacement pointers under the scheme to be developed.
  - Traversing the definition graph
    - Relationships between FDes.
    - Data Elements, Measurements, and assessment definitions.
  - Anatomy access
    - Lookup, containment, laterality, and external ontology mappings.
  - Exam access
    - Exam-family lookup and anatomy-coverage queries.
  - External terminology mappings
    - Retrieve mappings and their qualifications and provenance.
* Authoring and maintaining Foundation Context
  - Definition and relationship authoring
    - Create, edit, and validate definitions and relationships.
    - Support human review and maintain cross-links between OIFM and ACR/RSNA CDE identities.
  - LLM-assisted generation and enrichment
  - LLM-assisted content-guideline checking
    - Check scope, naming, attributes, and relationships against the community's evolving content guidelines.
  - FDe discovery from radiology report corpora
    - Extract proposed definitions and associated attributes, measurements, anatomy, and relationships.
    - Identify coverage gaps and candidates for human review.
  - External ontology authoring tools
    - Search ontologies and inspect concepts and relationships.
    - Propose and validate mappings while retaining qualifications and provenance.
  - Human review, versioning, and provenance
    - Support the proposed content-update, deprecation, and replacement scheme without assuming its detailed design is settled.
* LLM agents: From report text to imaging data
  - Automated extraction of assertions, attributes, measurements, anatomy, and relationships.
  - Organization of Findings and Impression content.
  - Resolution of extracted concepts against Foundation Context.
  - Supporting report text and generation provenance.
  - Automated validation, correction, and radiologist review.
  - Concrete implementation to examine: the imaging-problem-list extraction work.
* Longitudinal linking of imaging findings
  - Proposed dedicated SDK knowledge node for identifying observations of the same imaging finding across a patient's imaging history and making the appropriate connections.
  - Capture the project's preliminary work on this specific problem, with source evidence and remaining questions.
  - Describe the reusable library capability for establishing and maintaining those connections.
  - Link to the Imaging Problem List's representation of finding histories.
  - Keep this specific linking problem distinct from the broader reconciliation of diagnoses, procedures, and other clinical information for Imaging Persona.
* Working with patient data structures
  - Observations and Exam Finding Lists
    - Create, inspect, validate, and update application objects.
    - Manage attributes, sub-assertions, components, and relationships.
    - Associate assertions with exam information.
    - Preserve identities, evidence, and review decisions.
  - Imaging Problem Lists
    - Assemble and query finding-based histories.
    - Use the longitudinal-linking capability and support finding identity, change, and status.
    - Retrieve underlying observations and evidence.
  - Imaging Persona
    - Assemble and query the standard organization of patient facts relevant to imaging.
    - Incorporate imaging history, safety information, diagnoses, treatments, procedures, and pathology.
    - Extract and normalize relevant clinical facts using LLM agents.
      - Clinical notes, operative reports, and pathology reports.
    - Retrieve relevant patient facts using Foundation Context associations.
      - Connections between FDes, clinical diagnoses, procedures, and external codes.
      - The owner's example is cholecystectomy history and related procedure and diagnosis codes.
      - The owner named LOINC and CPT for the procedure example, and ICD, LOINC, and SNOMED CT for diagnoses. These are code-system leads to investigate, not verified code assignments.
      - Verify the appropriate code systems rather than inventing codes or treating mappings as equivalence.
      - Preserve evidence and distinguish documented facts from likely associations.
      - Whether to identify missing information to seek remains unresolved.
* Bidirectional FHIR conversion capabilities
  - Convert Observations to FHIR and back.
  - Convert Exam Finding Lists to FHIR and back.
  - Convert Imaging Problem Lists to FHIR and back.
  - Use the overall philosophy and the specific representation knowledge documents under Data Structures.
  - Preserve identities, relationships, measured values, and provenance; expose unsupported information and losses.

### Use Cases

This working outline describes envisioned uses, combining the assistant's proposed grouping with the owner's additions. Implemented software belongs under Sample Applications and can illustrate these uses. The descriptions of green findings and object-oriented reporting capture the owner's current guidance; supporting board material remains to be checked. The outcome-tracking subdivisions are assistant proposals responding to the owner's request. The detailed boundaries and individual use-case documents remain to be developed.

* Authoring and browsing Foundation Context
  - FindingModelForge and its proposed evolution.
  - Finding-definition catalog and graph exploration.
  - Anatomy browsing site.
    - Explore anatomic locations, their relationships, and associated information.
  - Exam browsing interface.
    - Explore the project's view of exams, including exam families and their linked anatomy.
* Turning reports into structured imaging information
  - Report extraction, coding, and persistence application.
  - Radiologist review and correction interface.
  - Extraction evaluation tools.
* Viewing and using imaging history
  - Imaging Problem List viewers.
  - Anatomy-based navigation through findings and their histories.
  - Proposed smarter selection of relevant prior examinations using exam families and linked anatomy.
  - Proposed Imaging Persona interface incorporating relevant clinical history.
* Reporting assistance
  - Green findings.
    - Start report drafts with the subset of established findings that will always carry forward from prior reports.
    - This is not copying the entire last report. Identifying which findings belong in that subset is a substantive question.
    - The owner identifies an implemented vendor prototype demonstrated at RSNA; record that example under Sample Applications.
    - Locate and review the older Excalidraw board identified by the owner before adding source-derived detail.
  - Object-oriented reporting.
    - Create and work with structured finding objects during interpretation and reporting.
    - Include creation of those objects from within the PACS image-viewing interface.
    - Connect to the assertion structures and SDK capabilities used to create and manipulate them.
  - Context-aware reporting tools and plugins.
  - Rendering structured assertions as report text.
* Outcome tracking
  - Finding-to-outcome tracking.
    - Connect findings to later imaging, biopsy, pathology, diagnoses, and treatment.
  - Recommendation and follow-up tracking.
    - Track recommended actions, completion, overdue follow-up, and unresolved findings.
  - Radiology-pathology correlation.
    - Connect the imaged finding, sampled lesion, and pathology result.
  - Feedback to radiologists.
    - Show subsequent outcomes for findings and assessments they reported.
  - Outcome dashboards and audits.
    - Diagnostic yield, assessment performance, and outcomes across a practice.
    - Monitoring AI-generated findings against subsequent evidence.
  - Connect these applications to longitudinal finding identity, Imaging Persona's clinical information, and Foundation definitions.
* Demonstrating exchange between systems
  - Existing structured-data demonstrations.
  - Proposed workflows connecting imaging, AI, reporting, and clinical systems.

Each use-case knowledge document explains the envisioned use and its connections to Foundation Context, Data Structures, SDKs, and any implemented Sample Applications.

### Sample Applications

Actual implementation is the dividing line between Use Cases and Sample Applications. Simple demonstrations and prototypes count as Sample Applications. Each example describes what was implemented, its status, and the use cases and SDK capabilities it illustrates.

* Green findings vendor prototype
  - The owner reports that a reporting software vendor implemented the feature as a prototype and demonstrated it at RSNA.
  - Connect the implemented example to the reporting-assistance use case above.
  - The vendor, demonstration date, and implementation details remain to be documented from appropriate evidence.

The rest of the Sample Applications inventory remains to be developed from actual implementations, including the imaging-problem-list extraction work already identified above. Do not label proposed browsers or future tools as implemented applications.

### Connections to review across the first three sections

These are relationships between OKF knowledge documents, expressed in prose and links. They do not prescribe clinical edge names.

- **Defines / references:** FDe, anatomy, exam, DataElement, and Measurement knowledge documents connect to the patient structures that reference them.
- **Describes / assesses:** finding characterization connects to assessment definitions and patient assessment assertions without merging them.
- **General association / patient evidence:** Foundation associations guide relevant-history access; only patient evidence establishes a fact about that patient.
- **Structure / capability / implementation:** data structures connect to the SDK capabilities that manipulate them and, later, named implementations and applications.
- **Guideline / check / human decision:** content guidelines connect to LLM checking capabilities and authoring/review records.
- **Mapping / conversion:** each FHIR mapping knowledge document connects to its bidirectional conversion capability and the overall conversion philosophy.

### Open boundaries and recorded review

Claude reviewed the initial first-three-section outline. The [full review](../references/knowledge-outline-claude-review.md) is saved separately, including proposed missing nodes and merges. It predates the owner's corrections and Applications additions; its technical claims need source verification and its proposals are not approved changes. The questions submitted for that review were:

1. Does FDe need separate knowledge documents for subject taxonomy, assessment definitions, and assessment assertions, and are the distinctions clear?
2. Are shared properties, identifiers/versions, scope, relationship properties, and terminology mapping sufficiently explicit?
3. Does the proposed DataElement/Measurement sub-assertion structure preserve the owner's wording without pretending it is a settled implementation?
4. Are EFL and Imaging Diagnostic Report related clearly without assuming they are identical?
5. Does Imaging Persona cover relevant wider history and Foundation-guided access, with likely associations distinct from patient facts?
6. Is the FHIR philosophy/mapping/capability separation useful, and what fidelity or identity questions need recording?
7. Are any candidate nodes merely headings, duplicates, or too broad, and which substantive concepts are missing?

Review is advisory. Incorporating a review is separate from owner approval. Do not reorganize content or edit the crafted pages as part of this review.

### Work status

- [x] Record the owner's first two section outlines and the SDK discussion in this existing plan.
- [x] Make proposed OKF knowledge nodes and cross-section relationships explicit.
- [x] Request and collect Claude review in Herdr pane `wA:p5`; recommendations remain under discussion.
- [ ] Discuss review findings and unresolved boundaries with the owner, one decision at a time.
- [x] Record the proposed Applications branch, including the owner's anatomy/exam browsers, green findings, PACS object creation, and outcome-tracking additions.
- [x] Record the owner's Use Cases versus Sample Applications distinction, the Imaging Persona information-and-representation node, and ongoing community development of data structures and content guidelines.
- [x] Record the owner's preliminary content-versioning concept and proposed dedicated SDK node for longitudinal finding linking.
- [x] Collect current clinical-informatics research on broader clinical-information reconciliation for Imaging Persona; retain primary sources and distinguish research findings from project decisions.
- [ ] Discuss relevant reconciliation findings as the Imaging Persona information and representation work develops.
- [ ] Refine Use Cases and inventory implemented Sample Applications as ongoing content work. Completing that inventory is not a prerequisite for the agreed first node or the remaining execution-plan review.

The five sections and the owner's subsequent additions are recorded above with their hierarchy. Use Cases has a working outline; Sample Applications currently names the green findings prototype and awaits a fuller implementation inventory. Both remain unfinished. The owner's original wording and Claude's initial full review are preserved in separate references. The archive move was authorized and completed under the reconstruction method; substantive node boundaries and remaining review decisions are still under discussion. No publication changes or commits are authorized by this outline.

## Proposed execution plan for the new knowledge tree, October 6

Status: written at the owner's request; review the aspects below one at a time before executing this sequence. The owner has agreed to the Foundation schema overview as the first node and approved the tree structure, document-boundary approach, and evidence and attribution approach. The remaining implementation choices are proposals awaiting discussion. The existing conceptual outline and fresh-writing method remain the foundation. No new knowledge documents or directories have been created by this planning step.

The goal is a readable, source-supported, interconnected OKF knowledge tree reflecting current thinking. It must preserve the owner's conceptual hierarchy while making proposals and unfinished design work explicit. The former deck-first pilot and edit-in-place migration remain withdrawn. Source storage, verification, and recovery are complete; use those tools when needed rather than rebuilding them. Keep all work under `site/` outside this plan, and preserve concurrent working-tree changes. Commits require separate explicit permission.

### First step: save and review this plan

- [x] Write the execution proposal into this existing planning record.
- [x] Agree on the first node with the owner: the Foundation knowledge graph schema overview under Finding Definitions.
- [ ] Review the subsequent expansion sequence with the owner.
- [x] Review the tree structure and knowledge-document boundaries; approved by the owner.
- [x] Review source selection and claim support; approved by the owner.
- [ ] Review the drafting, archive-checking, and linking workflow.
- [ ] Review how unfinished design and implementation status are represented.
- [ ] Review the owner-review and validation process.
- [ ] Review coverage completion and archive deletion.

Present only the current aspect in conversation, with a recommendation and one focused question. Record each answer here, including changes to later aspects. Do not ask the owner to reconfirm recorded decisions. Plan agreement authorizes the agreed execution; substantive questions arising in drafts still return to the owner one at a time.

### Starting point and sequence

Agreed first document: the overview of the Foundation knowledge graph schema, under Assertion Subjects / Finding Definitions. The owner accepted this starting point in the plan review. Explain the kinds of shared definitions and how their relationships fit together. Keep patient assertions identifiable as examples of how definitions are used. Leave detailed subject taxonomy, properties, relationships, Data Elements, and Measurements to their connected documents.

Use this first document to establish an acceptable level of detail, source attribution, and graph connections. Revise it after the related documents exist. Do not make completing the application inventory or settling every schema question a prerequisite for starting.

Proposed subsequent sequence:

1. Expand Foundation Context through FDe subject kinds, properties, relationships, Data Elements, and Measurements. Then cover anatomy, exam types, their integration, the repositories, versioning, and authoring. Keep the owner's nested outline visible. Develop the Foundation introduction as these concepts become concrete.
2. Build Data Structures around assertions, Exam Finding Lists, and Imaging Problem Lists. Include the overall FHIR philosophy and structure-specific mappings. Capture Imaging Persona's information-selection and representation work as an open development thread, informed by clinical-reconciliation research. Explain ongoing community development in the section introduction.
3. Build SDK documents for reusable library capabilities, including Foundation access and authoring, LLM extraction, longitudinal finding linking, patient-structure manipulation, and bidirectional FHIR conversion. Link to the structures and definitions they operate on.
4. Refine Use Cases and inventory actual Sample Applications. Verify what each implementation does and its current status, including simple demos and prototypes. Keep the green findings vendor prototype as an owner-reported implementation until further details have source support. Connect examples to the uses they demonstrate.

This is a dependency-based default, not a requirement to finish an entire section before connecting it to another. Add the related node needed to explain a concept when useful. Adjust the sequence with the owner when evidence or a substantive modeling question warrants it.

### Tree structure and knowledge-document boundaries

Agreed primary directories are `knowledge/foundation-context/`, `knowledge/data-structures/`, `knowledge/sdks/`, `knowledge/use-cases/`, and `knowledge/sample-applications/`. Checked processed references live in `knowledge/references/`. The owner approved preserving meaningful nested groups, using navigation indexes for grouping topics, and creating individual substantive concept documents as their content develops.

Preserve meaningful parent topics in subdirectories, such as finding definitions, anatomy, exam types, and Imaging Persona. Create directories and their indexes as substantive content is added. Do not fill the tree with empty concept documents.

One OKF document explains one substantive concept. An outline bullet can be a document, a subsection, or a navigation grouping; the source-supported content determines that boundary. An OKF node describing Measurement is not an individual clinical Measurement definition. Use plain-English titles and descriptive filenames, with no coded node references.

Before drafting a node, state its title, outline location, purpose, scope, and intended connections in this plan. Keep the current node's entry here rather than creating another planning document. SDK nodes explain reusable library functionality; Sample Applications nodes explain particular implemented software. Cross-link shared concepts instead of repeating their explanation in every section.

The path for the agreed first node is `knowledge/foundation-context/finding-definitions/schema-overview.md`. Individual document scopes will be refined during drafting under the agreed approach. Source selection and claim support have also been approved; the drafting, archive-checking, and linking workflow is the current review aspect.

### Source selection and claim support

Approved by the owner: use current owner guidance for intended direction, identify proposals, support implementation claims with checked sources at recorded revisions, preserve open questions and conflicting representations, and keep detailed source analysis in references with concise citations in concept prose. An idea can be included before implementation when its status is clear.

For each node, first read the relevant recorded owner guidance. Then identify original sources and checked processed references by relevance to the concept. Source artifacts, repository names, and historical pages do not determine the tree.

Pin repository evidence to committed revisions and specific files or sections. Recheck current implementation claims against current committed source. Use official standards documentation and primary research when needed; retain versions, dates, and limitations. Verify source availability before claiming that an implementation or technical detail has been examined.

Create or revise a processed reference only when it adds useful source detail. Keep source quotations and technical specifics there when they would interrupt the conceptual document. Cite substantive claims through reference links and matching source footnotes. Distinguish owner statements, implementation evidence, agent interpretation, and proposed design. Dates qualify the evidence; historical development does not become the organizing principle.

Follow the existing source-handling rules. Never inspect reviewer correspondence. Keep originals and private material outside Git. Paraphrase manuscripts under review, and confirm board publication status before reproducing originals. An unavailable source leaves the associated claim unresolved; use another supported source or ask for the missing information without inventing it.

### Drafting, archive checking, and graph connections

Review checkpoint recorded October 14: this aspect is not yet approved. The last question to the owner was, "Is the end of that cycle the right point for your review?" It refers to completing the scope, evidence, fresh draft, archive check, graph connections, documentation updates, and validation before presenting the node. Await that answer before advancing the plan review. The owner has already approved writing fresh before consulting the archive; do not ask to reapprove that principle.

Repeat this workflow for one node at a time:

1. Define the node's scope and place in the outline; identify the relevant evidence.
2. Write the concept from an empty file using that evidence. Explain the idea, meaningful relationships, supported examples, and unresolved questions. Use headings that fit the concept rather than forcing every document into the same prose template.
3. After the fresh draft exists, inspect relevant archived material for worthwhile omissions and source leads. Verify each proposed addition against its evidence. Do not reuse archived wording or adopt its file boundaries.
4. Add meaningful links to existing related nodes and update those nodes when the reciprocal connection helps understanding. Keep links to unwritten topics as plain-English future work until their target files exist.
5. Update directory indexes, source references, the bundle log, and this plan for the current batch. Check the draft and bring its substantive review question to the owner.

For each node's archive check, record briefly in this plan what useful material was recovered, what remains unresolved, and what was excluded when the reason matters. This supports the final coverage review without creating another knowledgebase or copying discarded prose.

### Unfinished design and implementation status

Treat unresolved concepts as useful knowledge when their intent and open questions can be stated clearly. Do not manufacture complete schemas, APIs, clinical truth-resolution rules, or community consensus.

In particular, keep Foundation versioning and replacement links, assessment representation, Imaging Persona's patient concepts, content guidelines, and exact FHIR mappings at their actual level of development. Separate the project's preliminary longitudinal finding-linking work from broader clinical reconciliation. Explain continuing community refinement grounded in implementation experience.

Use Cases describe envisioned uses. Sample Applications require an actual implementation, including demos and prototypes. Identify what exists, what is proposed, and what has been verified without equating an old prototype with a current supported product.

### Owner review and validation

The assistant researches, drafts, checks, and proposes resolutions. The owner reviews the substantive content and decisions. Present one bounded issue or document portion at a time, including a recommendation and the evidence necessary to assess it. Provide a file link; do not paste a whole draft into the conversation. Explicit corrections to an authorized draft are applied and recorded promptly.

All new agent-written knowledge documents start with `status: draft`. Follow [knowledge-authoring instructions](../knowledge-authoring.md) for `type`, title, description, generation metadata, sources, and footnotes. Human verification records an actual review of the document, not agreement with the outline or an agent's review. Do not apply verification metadata merely because one subsection was discussed.

Run `task check` after each content batch. Also inspect local links, directory-index descriptions, claim attribution, and terminology. Conformance checks establish document structure, not factual support. Run checks appropriate to any changed tooling; this plan does not require site-generation or deployment work. Fix check failures and maintain the relevant documentation in the same batch.

Update this plan and `knowledge/log.md` as nodes are added or changed. Update `DEV_LOG.md` for completed work and `CHANGELOG.md` only for changes relevant to outside readers. Keep the handoff and authoring instructions aligned with the actual state. A batch is ready for review when it has readable content, working connections, source support, explicit unresolved questions, and passing checks.

### Coverage completion and archive deletion

Review coverage against the owner's outline and later recorded guidance. Use the historical idea inventory only as an omission check, after fresh concepts exist. Coverage means relevant supported ideas have a clear home and useful connections; it is not a target file count or a requirement to settle every design question.

Before deleting the temporary archive, confirm that useful material and source leads have been recovered or deliberately excluded, recorded owner guidance survives outside it, and no active documents depend on it. Preserve source originals and recovery tooling. Then delete `archive/knowledge` under the owner's existing instruction and update the plan, archive instructions, handoff, references, and relevant logs.

Finish with a documentation review that reflects the actual reconstructed tree, remaining design questions, and archive state. Mark completed reconstruction work accurately; keep continuing community design work visible. No commit is part of this sequence without the owner's explicit permission for that commit.

## Presentation pages and figures

Everything outward-facing (the agreed pages, their figures, the project lead's page guidance, and the site build) lives in `site/`, with its own roadmap, current task, and history (`site/ROADMAP.md`, `site/CURRENT_TASK.md`, `site/HISTORY.md`). It is a separate track from the knowledge graph and outside its scope. The page map and page and figure status are in `site/ROADMAP.md`; the project lead's page guidance, verbatim, in `site/guidance.md`.

## Content and source rules

- Distinguish stated goals, proposals, implemented examples, and human approval. Do not invent motivation, benefits, consensus, or resolutions to disagreements. Scope absence claims to reviewed sources.
- Repository code, plans, prompts, skills, and design records are eligible sources. Preserve their actual status, date, pinned commit, and explicit provenance labels such as OWNER or CLAUDE DEFAULT.
- No OIDM source is a formal project specification. Use current terms: Foundation Context, Patient Context, and the owner's working FDe terminology. Observation Type remains unadopted. The owner uses pointers for application-object references; describe the broader graphs as interconnected.
- OIFMs and CDEs are the same kind of content in different collections, intended to share the new graph schema. Migration is direction, not a completed implementation. SDKs support authoring and maintenance as well as use.
- Organizations only. Keep the reporting vendor and the organizations behind the 47/31 collections generalized. Paraphrase manuscripts under review; never quote them or read/summarize reviewer correspondence. Internal boards contribute schema ideas, without people, live share links, meeting histories, or vendor logistics.
- Read CDE sources only from committed files at a pinned revision. Decisions S53–S67 were recorded as uncommitted; verify their state before using them, without committing upstream work as part of this plan.
- Figures use Excalidraw and the [diagram conventions](../../tools/diagrams/README.md). Inspect rendered output before review. Keep exact owner-accepted versions distinct from candidates.

## Open decisions and deferred work

Remaining graph work includes developing Use Cases, deciding substantive document boundaries, and addressing relevant review findings one decision at a time. Page wording, figure acceptance, and website release decisions belong to the separate site workstream in `site/ROADMAP.md`.

Source-manifest handling is documented in the completed storage work and source instructions. It does not determine the organizing principle for recovered content.

Defer search-engine adoption, OKF toolkit replacement, broad theme work, comments/feedback tools, and a typed-edge website graph. Preserve the completed tooling reports. Upstream issue drafts and source-repository link-back changes remain separate work for the project lead's review. CI credentials and production domain configuration are deployment prerequisites, not blockers to local organization.

## Maintaining this plan

Maintain the agreed fresh-writing method and current-state table here as reconstruction proceeds. Keep the conceptual outline and remaining decisions current, and retain the reset and completed-work record. Keep source evidence in references, review artifacts in their appropriate tracked/private homes, and historical implementation detail in `DEV_LOG.md`. Update documentation in the same batch as the files it describes. Remove obsolete instructions rather than appending another contradictory section.

Before closing a batch, validate links, indexes, provenance, and any changed build behavior. Review `README.md`, `CONTRIBUTING.md`, `docs/HANDOFF.md`, relevant reference/authoring instructions, and both logs for the final state. Commits require the project lead's explicit permission each time.
