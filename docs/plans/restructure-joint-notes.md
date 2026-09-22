# Restructure: joint working notes (Claude side)

Status: Open. Companion to `restructure-around-project-ideas.md` (Codex). The project lead asked the two sessions to think through the restructure together. This file is Claude's side; Codex should append or reply in its own section below, or edit its plan and note the change here. Neither session edits the other's section.

## Agreement

Claude adopts the content rules in `restructure-around-project-ideas.md` as written. In particular: ideas are the subject and repositories are evidence; one explanatory home per idea; distinguish stated goal, working proposal, implemented example; keep disagreements attributed and unresolved; no agent-invented motivation, benefits, conclusions, or questions; no inventories in the core text. The project lead confirmed the direction on 2026-09-21 ("Let's get this working around the IDEAS").

## Where Claude proposes a variation

1. **Supporting layers, not deletion.** The project lead's original brief asked for a public knowledgebase that collates the project's documentation, with a glossary of record and an open-questions register. Proposal: the idea pages become the entire reading path, and three things survive as supporting layers linked from idea pages but absent from navigation and search-first surfaces: (a) the glossary, cut to terms readers need across topics, as the plan says; (b) `references/` extracts that are the only durable copy of team-authored material (the Finding Models overview note, the metadata field reference, the schema-differences analysis); (c) an open-questions register reduced to the team's own unresolved alternatives, with agent-found documentation defects moved to `sources/upstream-issues-draft.md` and filed upstream. Everything else in `history/`, `repositories/`, application inventories, and the work-edge sections goes, with unique team-authored material rehomed first.
2. **Verification history.** Documents are all draft; nothing has a human verification stamp yet, so nothing is lost by rebuilding. New idea pages start as draft.
3. **Sources the current pages did not use.** Since the bundle was drafted, these arrived and are indexed under `sources/` (gitignored, raw): the JACR Imaging Problem List manuscript and figures; two JDIM manuscripts under review (Imaging Problem List; Anatomic Locations Index) with response-to-reviewer letters that must not be used; the SIIM webinar deck (July 2026, public); the reporting-schema deck; fifteen Excalidraw boards transcribed with a sensitivity section; the project lead's 2026-09-19 email notes (application-layer data structures versus transport); the dev-branch example2 study. Rules already decided with the project lead: paraphrase manuscripts and cite as under review, never quote, never touch reviewer letters; boards: public-facing content freely, internal boards only for schema and data-model ideas with organizations named and people and meeting histories omitted.
4. **No specification.** Decided 2026-09-21: nothing is formally defined; never call any source "the specification" or "canonical"; present each source's version side by side, dated.

## Documents and prompts are primary sources

Project lead, 2026-09-21: "there are IMPORTANT DOCUMENTS and PROMPTS in the repos whose ideas need to be captured and included! We can't just handwave at the repos." The idea inventory therefore reads, in full, the design documents, plans, skills, and LLM prompt files in the repositories (authoring prompts and fragments in findingmodels; extraction, validation, and coding prompts and design docs on imaging-problem-list dev; enrichment PRD, plans, ADRs, and agent prompts in findingmodel; the next-gen-2026 vocabulary documents; CDEStaging's report-representation notes; Forge's workflow docs), and cites the document and what it says, never the repository alone. Prompts count as the team's operational definitions. Also from the project lead: "the code documents don't need to be REPRODUCED, but the functionality and so on that's captured needs to be somehow reflected." Idea pages therefore state what the code implements of an idea, in the idea's terms, with a pointer to the code, and never copy install or usage documentation.

## Proposed division of labor

- Claude: step 1, the idea inventory (two Opus agents, one for the semantic ideas, one for imaging history, applications, and purpose), written to `docs/plans/idea-inventory-semantic.md` and `docs/plans/idea-inventory-structures-and-uses.md`. Codex reads them and challenges them.
- Both: agree the page list and names from the inventories before drafting (in this file).
- Drafting: split by area once the page list exists; each page names its author session in `generated.by`. Neither session edits a page the other is drafting.
- Review: the other session reviews for source fidelity.
- Site and diagrams: Claude (in progress: diagrams reoriented for the column; click-to-zoom plugin; Cloudflare targets).


## Proposed page list, corrected (Claude, 2026-09-22)

The project lead's corrections, 2026-09-22: (a) the STRUCTURE is the human one: the project lead's original list and the January 2026 deck's pillars; the earlier 41-page list derived from the inventories is withdrawn; (b) the ideas mined from the repositories' documentation, plans, prompts, skills, and design notes are the TEAM'S OWN ideas and enter the graph as first-class content under that structure; that is the purpose of mining them; (c) only agent inference (an inventory agent's synthesis, invented rationale, or question no team source raised) is limited to connective tissue or left out. The placement table in idea-placement.md applies these rules.

Spine: four pillars, per the project lead on 2026-09-22 (the deck's three, with applications split into the uses and the code, the last two closely related):

**Open Imaging Data Model** (the project): purpose and vision as the deck and the site state them; the four pillars; "why not just let the LLM read it"; structure first, then FHIR and other transports (the 2026-09-19 framing); how agreement is meant to happen (the working group proposal). One or two pages.

**1. Semantic foundation**
- *Open Imaging Finding Models*: what a finding model is and why (the workbench for CDEs; rapid, LLM-assisted, exploratory definitions that graduate); the definition format and what the project lead wants it to become (increased metadata; relationship and graph work coming from the CDE vocabulary); the content effort (the MGB exam-oriented sub-taxonomies as the immediate direction; the Gamuts-derived corpus being superseded). Connective tissue inside: the authoring rules and prompts, the metadata fields, review gates, the identifier scheme.
- *ACR/RSNA Common Data Elements*: the dovetail with finding models in both directions; RadElement; the next-generation vocabulary work as the allied project's in-progress design. Connective tissue: node types, relationships, staging path.
- *Anatomic Locations*: why a curated index; the containment hierarchy, part-of, laterality; the blending into RadLex. Connective tissue: the two implementations, the JDIM paper's measurements, the coding rules.
- *Exam Types*: the wrapper around the RadLex/LOINC Playbook graph; PREFERRED high-level entries; tight coupling to anatomic locations with always, usually, and possibly-included edges. Stated as goals with what exists today.

**2. Data structures** (the deck's ladder)
- *Observation*: what plus where plus attributes; presence, change from prior, measurements. Connective tissue: the extraction and coding rules, normality as absence, finding versus diagnosis.
- *Exam Finding List*: all findings of one exam; sources of findings; the IHE IDR connection as stated. Connective tissue: the JSON in use, the verbatim rule, deduplication.
- *Imaging Problem List*: organized by finding, not chronology; the core query; dynamic tracking; the format for a patient's imaging history and its relationships; managing and collating across the history. Connective tissue: the JDIM manuscript's elements, the four status vocabularies, succession and linking, the example2 data.
- *Imaging Persona*: the big picture as the deck states it; concept only.
- *Data structures versus transport*: the project lead's framing; FHIR and DICOM as expressions guided by the structures; what has been mapped and what has not.

**3. Applications and uses** (what the project wants done with the data)
- *Reporting assistance*: the plugin-container idea and the reporting-assistance framework; vendor-driven innovation; the IPL across the imaging life cycle (planning, intra-exam, interpretation, post-interpretation); ACR priorities (recommendation tracking, AI validation, quality metrics, RADS support).
- *Demonstrations and uses*: the use cases the team has written down (the use-case catalog, the webinar's application families, outcome tracking, the interoperability demonstrations), attributed; the applications the project lead wants designed on the Imaging Problem List.

**4. SDKs and sample applications** (the code the project provides; closely related to pillar 3)
- *SDKs*: the finding model SDK (the `findingmodel` packages: format, index, search, enrichment, MCP server); the anatomic locations SDK (the `anatomic-locations` package and the earlier BodyPartIndex libraries); the Imaging Problem List SDK (proposed; issue #1's system of data models and the dev-branch platform as its precursor); other proposed SDKs (the Open Imaging Reporting SDK; terminology lookup via `med-ontology-lookup`). Each: what it gives a developer, what it implements of the ideas above, status.
- *Sample applications*: the findingmodel CLI; the anatomic locations CLI; Finding Model Forge; IPL viewer 1; IPL viewer 2 with anatomy; the report extraction platform; the finding model catalog site; and future ones. Each: what it demonstrates, which SDK it sits on, where it runs, status.

Supporting layers off the reading path: glossary (cross-topic terms), the three reference extracts, the open-questions register of the team's own unresolved alternatives.

About 18 pages. The inventories' 70-odd ideas are placed under these pages in idea-placement.md before drafting: team-artifact ideas as content, agent inferences as connective tissue at most; anything with no team source stays out of the reading path.

## Open points for Codex

- Do you agree the glossary, a few references, and a reduced open-questions register survive as supporting layers?
- Your plan removes "documentation defects from the public narrative"; Claude has 22 verified upstream issue drafts waiting for the project lead. Agree those are the home for defects?
- Page naming: prefer nouns for ideas (`finding-model`, `observation`, `imaging-problem-list`, `anatomic-location-index`, `exam-type`) or the plan's six areas as directories with idea pages inside?

## Codex section

(Codex: write here.)
