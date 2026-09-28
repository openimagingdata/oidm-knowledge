# Restructure around the team's ideas

Status: Proposed. Updated 2026-09-22 after reading the SIIM 2026 presentation. Restructuring has not started.

## Purpose

Recover the team's idea work scattered across the repositories and give each distinct idea a clear, stable home that the team can build out. Readers should understand the ideas, their relationships, their sources, and what remains unsettled.

Explore code, data models, examples, design notes, discussions, and unfinished branches for the ideas they embody. Consolidate related work across repositories into an account of the idea, with links back to the evidence. The repositories remain the place to inspect files and implementation details. Repository coverage is not a measure of completeness.

This plan replaces the sentence-shortening approach for the next revision. The previous editorial passes remain recorded as completed work.

## Content rules

- Capture both explicitly discussed ideas and ideas demonstrated by the team's implementations and examples. Use concise explanations with direct source references.
- Describe what code or an example actually represents or does. Attribute it to that implementation. Do not invent the team's motivation, intended generality, or agreement with another approach.
- Treat the existing generated pages as leads to sources. They are not evidence that the team endorsed a claim.
- Distinguish a stated goal, a working proposal, and an implemented example. Human verification of an account does not establish consensus on its subject.
- Preserve attributed disagreements when they affect an idea. Do not reconcile them through agent reasoning.
- Give each idea one explanatory home. Other pages link to it.
- Keep an example only when it explains something the prose cannot explain as clearly.
- Remove inferred benefits, causal histories, design conclusions, and questions invented by agents unless a team source supports them.
- Omit file catalogs, branch censuses, commit distances, issue inventories, package tours, dataset statistics, and development chronology from the core text. Cite a specific artifact when it provides evidence.
- Avoid copied schemas and full source extracts. Retain unique team-authored material that has no other durable home before removing its current page.

The recorded [owner statements](../../knowledge/plans/2026-09-20-knowledgebase-build-plan.md#the-project-leads-stated-goals) orient the investigation. The [decisions added on 2026-09-21](../../knowledge/plans/2026-09-20-knowledgebase-build-plan.md#decisions-added-2026-09-21) require dated, attributed versions of unsettled structures and distinguish data structures from transport formats. The repository work itself, along with manuscripts, decks, and working notes, supplies the substance. A lack of polished explanatory prose is a reason to investigate the implementation, not to discard the idea.

## Direction from the SIIM 2026 presentation

The owner supplied [Structured Results and Context for Next-Generation Imaging Resulting Tools](https://oidm-public.t3.tigrisfiles.io/oidm-knowledge-sources/SIIM%202026%20Reports-of-the-Future.pptx) to guide this restructuring. Read all 15 slides, speaker notes, and embedded diagrams. Slide references below use file order because printed slide numbers repeat.

The deck's central distinction is Patient Context and Foundation Context. Patient Context records observations and imaging history for a particular patient. Foundation Context supplies shared definitions, relationships, and references. Clinical history changes with the patient; shared knowledge develops through authoring and versioning. Codes connect the patient's observations to that knowledge. The opening purpose is reuse by clinicians and by the next radiologist, with support for subsequent reporting. These points appear in slides 3–8 and 12–15.

The editorial implication is to lead with that purpose and connection, then explain the ideas that make it possible. The three axes of Foundation Context are Observation Type, Anatomic Location, and Exam Type. Their relationships deserve an explicit explanation alongside the axes. Repository work supplies the evidence and further development of these ideas. This deck guides the reading path without excluding ideas documented elsewhere.

Preserve the deck's qualifications. Slide 9's notes treat "Observation Type" as a possible name and some attributes as illustrative. Slide 10 distinguishes existing anatomy content from unpopulated enrichment. Slide 14 describes SDK-mediated access and intended uses; it does not establish which capabilities have shipped or prove the stated benefits. The conceptual figures are not formal schemas. Preserve source-specific formulations, including the deck's focused/included/edge anatomy and other sources' always/usually/possibly wording, until the team reconciles them.

## Connection to the CDE two-plane model

The CDE work gives this distinction a concrete graph expression. Its [two-plane account](https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/03-draft-structures.md#5-two-planes-reports-point-into-the-vocabulary) describes shared definitions and their relationships, plus report-specific observations and their relationships. The definition plane supplies part of Foundation Context; the observation plane represents the imaging assertions within Patient Context. These correspondences guide the explanation without declaring the two projects' models identical.

Observations point to definitions for their subjects, locations, and data elements. Their relationships express assertions about the particular case. A definition-space potential and a radiologist's case-specific interpretation have different meanings. The [owner's report-plane decisions](https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/plans/2026-09-03-report-plane-example.md#owner-decisions-taken-in-this-session-copy-these-into-10-verbatim) explicitly say that report edges do not point to the vocabulary relationships they parallel. Keep provisional edge names separate from those owner decisions.

Use this connection to organize recovered ideas and their relationships. For example, anatomic scope and a particular observation's location belong in one connected explanation. Shared presence definitions and explicit negative observations belong in another. A few existing report examples can show these connections without repeating their definitions or creating an exhaustive example catalog.

## Proposed reading structure

Use the following sequence as a provisional reading path. Determine the actual idea pages after investigating the source work. An idea developed across several repositories gets one home. A distinct idea may need its own page even when several ideas share one repository.

| Area | Material to recover and explain |
|---|---|
| Purpose and reuse | Why the team wants imaging findings to remain useful after the report, for subsequent care and the next interpretation. Introduce Patient Context and Foundation Context together. |
| Patient Context | Observations carrying codes and patient-specific attributes, connected by case-specific relationships; their organization by exam and across imaging history; their place alongside other clinical context. Recover the actual source alternatives for EFL, IPL, and Imaging Persona. Distinguish transport expressions from the structures. |
| Foundation Context | The three connected axes: observation types, anatomy, and exam types. Recover finding-model and CDE work, metadata, anatomic hierarchies and laterality, preferred exam families, and anatomy coverage. Explain each axis once, with a separate page only where its distinct idea work warrants one. |
| Relationships and code resolution | How observation codes refer to shared definitions; relationships within and between axes; external references; the proposed shared access through SDKs. Preserve the distinction between a general relationship and what is asserted about a patient. |
| Tools using the combined context | The team's intended uses in reporting, follow-up, longitudinal review, rule-based tools, and generative assistance. Link implementation examples to the ideas they demonstrate. Attribute proposed benefits and distinguish available capabilities from goals. |

Each idea page should explain what the idea is, the problem or use it addresses where the sources establish that, the approach embodied in the work, its relationship to other ideas, and meaningful unresolved alternatives. Include a small example only when it helps explain the idea. Use stable descriptive names so later idea work can extend the same pages.

Put each idea's stated direction and substantive open questions beside its explanation. Add a compact shared glossary only for terms readers need across topics. Consolidate aliases. Source references belong beside the claims they support.

Set a small page and word budget after the idea investigation, before drafting. Include the introduction, glossary, and supporting notes in that budget. A page needs a distinct idea worth developing, not a corresponding source file. Start with the shortest explanation that makes the idea understandable and connects it to its evidence. Do not expand a page to fill a template or move excess text into appendices. The intended change is a substantially smaller authored account, not another sentence-trimming pass.

## Treatment of existing material

| Current material | Planned treatment |
|---|---|
| Overview, glossary, conceptual pages | Rebuild around the ideas recovered in step 1. Merge repeated definitions and delete superseded explanations. |
| Roadmaps and open questions | Retain explicit team directions and meaningful source disagreements within their topics. Remove agent research tasks and documentation defects from the public narrative. |
| Application profiles and repository map | Investigate the ideas embodied in the applications and connect them to their conceptual homes. Retain a short use and implementation link where helpful. Remove inventories and operational documentation. |
| History | Keep a historical fact only when it explains a team idea or an explicitly recorded decision. Link to the original account. |
| References and examples | Link to durable originals. Keep only indispensable examples and unique team-authored material, counted within the content budget. |
| Build plans, migration ledger, authoring instructions, editorial reports | Keep maintenance records outside the published reading path. Consolidate active instructions and mark superseded plans. Preserve provenance without presenting it as project exposition. |

Delete superseded generated pages after checking their unique content and links. Do not reproduce them as a new public archive or appendices. Use repository history for recovery once the owner authorizes a commit. Preserve unrelated concurrent edits throughout.

## Execution sequence

### 1. Recover the idea work

- [x] Write this plan before changing content.
- [x] Read the owner-supplied SIIM 2026 deck, notes, and diagrams; revise the proposed reading path around Patient Context and Foundation Context.
- [x] Read the CDE two-plane explanation and recorded owner decisions; incorporate their connection to the deck without merging distinct relationship meanings.
- [ ] Use the existing source map to find relevant code, models, worked examples, design notes, discussions, and branch work. Read the artifacts that contain the idea work rather than repeating a file census.
- [ ] Read across repositories to recover how an idea has been expressed, attempted, or developed. Include manuscripts and decks. Inspect implementation behavior when prose leaves the idea implicit.
- [ ] Make a temporary, compact list of distinct ideas with source locations, related ideas, and status. Where relevant, identify their role in the definition plane, observation plane, connections between them, or tools using them. Separate explicit intent from demonstrated behavior. Record disagreements and uncertain interpretation.
- [ ] Check every current page for a unique, sourced team idea before marking it for consolidation or removal. Do not carry agent-generated claims forward by default or mistake an implementation detail for the underlying idea.
- [ ] Identify unique team-authored material and give it a durable home before removing any wrapper page.
- [ ] Trace the deck's ideas and connections into the repository work. Preserve what that work adds, including disagreements with the presentation, without treating every depicted capability as implemented.
- [ ] Derive the proposed idea pages from this investigation. Check the reading structure and content budget against them.

Completion condition: the distinct ideas found in the work have proposed homes and supporting evidence. Uncertain interpretation is explicit. No inferred intention has become a team position, and ideas have not been excluded merely because they lack a written statement.

### 2. Draft the smaller account

- [ ] Write the idea pages from the source investigation. Use the old pages to locate evidence, not as outlines to shorten.
- [ ] Add only necessary definitions, examples, and source references. Use a few existing report examples to explain relationships within and between the planes. Keep unsettled alternatives side by side where needed.
- [ ] Check each section for duplication and for agent-added interpretation.
- [ ] Record progress and unresolved attribution questions in this plan.

Completion condition: the pages form a coherent reading path within the budget established after discovery, with no repository inventory chapters or hidden overflow. Check any conflict between brevity and retaining a distinct idea against its source rather than silently discarding it.

### 3. Replace and reconnect

- [ ] Replace the old reading structure and remove superseded pages after the unique-content check.
- [ ] Update indexes, diagrams, internal links, and provenance references to match the new organization. Inspect existing incoming links before deciding which moved URLs need redirects.
- [ ] Keep maintenance records accessible to maintainers while excluding them from the published reading path. Check the current site configuration before implementing that separation.
- [ ] Preserve source attribution and human verification history accurately. Rewritten content remains draft pending review; do not carry a verification stamp onto materially changed claims as if they were reviewed.
- [ ] Update authoring guidance to enforce these content rules and prevent future repository inventories.

Completion condition: obsolete pages no longer compete with the new account; retained links and provenance resolve.

### 4. Review and close

- [ ] Have one reviewer trace retained claims to team sources and another check duplication, scope, and reading order. Their task is fidelity and clarity, not adding ideas.
- [ ] Check that the new account retains the distinct sourced ideas identified in step 1. Report unresolved attribution rather than guessing.
- [ ] Run strict OKF validation, the house checker, the site build, and link/navigation checks. Resolve failures caused by the new structure.
- [ ] Update this plan, relevant reference instructions, `DEV_LOG.md`, `CHANGELOG.md`, and the bundle log. Keep the changelog focused on the changed reading experience.
- [ ] Report final page and word counts alongside the source-fidelity review. Mark restructuring complete only after the content and documentation checks pass.

No commits, publishing, or restructuring are authorized by the request to create this plan.

## Acceptance criteria

- A reader can follow the team's ideas through concise pages organized around concepts and their relationships.
- The introduction explains the deck's Patient Context/Foundation Context distinction, how they connect, and the team's intended uses. The three Foundation Context axes and their relationships have clear homes.
- The pages recover substantive idea work from the repositories, including ideas embodied in code and examples. They provide stable homes for further development.
- Every substantive claim is attributable to source evidence. Implementation behavior and explicit team intent remain distinguishable.
- Each idea has one explanatory home. Unsettled alternatives remain attributed and unresolved.
- No agent-created proposal, inference, or research question is presented as the team's position.
- Supporting material stays within the same scope and size constraints. Relocating bulk text does not count as reducing it.
- The site and bundle checks pass, and maintenance records describe the final state.
