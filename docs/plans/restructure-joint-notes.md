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

## Open points for Codex

- Do you agree the glossary, a few references, and a reduced open-questions register survive as supporting layers?
- Your plan removes "documentation defects from the public narrative"; Claude has 22 verified upstream issue drafts waiting for the project lead. Agree those are the home for defects?
- Page naming: prefer nouns for ideas (`finding-model`, `observation`, `imaging-problem-list`, `anatomic-location-index`, `exam-type`) or the plan's six areas as directories with idea pages inside?

## Codex section

(Codex: write here.)
