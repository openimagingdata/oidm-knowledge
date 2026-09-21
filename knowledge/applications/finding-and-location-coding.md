---
type: Concept
title: Finding and location coding
description: How extracted findings are assigned OIFM finding codes and RadLex anatomic location codes, as a deterministic index lookup followed by language model term generation and selection.
tags: [applications, coding, anatomic-locations, llm, extraction]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
stale_after: 2027-09-21
sources:
  - id: coding-design
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/coding-agent-design.md
    title: Coding agent design, imaging-problem-list dev branch
    last_modified: 2026-03-16
  - id: coding-prompts
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/coding-agent-prompts.md
    title: Coding agent prompt catalog, imaging-problem-list dev branch
  - id: coding-archive
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/archive/finding-and-location-code-assignment-plan.md
    title: Finding and location code assignment plan, version 3, archived, imaging-problem-list dev branch
    last_modified: 2026-02-19
  - id: anat-rules
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/anatomic-location-assignment-rules.md
    title: Anatomic location assignment rules, imaging-problem-list dev branch
  - id: anat-plan
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/anatomic-location-efl-ipl.md
    title: Anatomic locations for Exam Finding Lists and Imaging Problem Lists plan, imaging-problem-list dev branch
    last_modified: 2026-06-10
---

# Why coding is its own step

[Extraction](/glossary/extraction.md) asks what the report says. Coding asks which existing definition that corresponds to. Keeping them apart is the central design decision of the current pipeline: extraction output persists without codes, and coding is triggered separately, can be re-run with different models, and never re-reads the report.[^coding-design] Two earlier designs did it inside extraction and were retired.

The two axes are coded independently. A finding gets an [OIFM identifier](/glossary/oifm.md) naming a [finding model](/glossary/finding-model.md) definition. Its location, when the report gives one, gets a [RadLex identifier](/glossary/radlex-id.md) from the [anatomic locations](/glossary/anatomic-location.md) data set. Either can succeed while the other fails.

# The pipeline

Coding operates on the flat merged finding list of a completed extraction rather than on report chunks. Each finding already carries its name, [presence](/glossary/presence.md), location fields, verbatim quote, and source section, and the design states that this is sufficient context; chunk-level ambiguity was already resolved during extraction.[^coding-design]

Five phases, of which two involve language model calls.

| Phase | What happens |
|---|---|
| 1. Fast path | Exact or synonym lookup in the finding index by name, and in the anatomic location index by specific anatomy. Findings that resolve skip the rest for that axis |
| 2. Term generation | Two agents, one for findings and one for locations, generate two or three diverse search terms for each finding that missed the fast path |
| 3. Index search | Batch embedding search over all terms at once; results are distributed back per finding, deduplicated, and capped |
| 4. Code selection | Two agents, one for findings and one for locations, choose from the candidate set, running concurrently under a semaphore |
| 5. Assembly | Fast-path and selected results merge into one coding bundle per finding |

Four agents in total. Term generation and selection use different models on the stated ground that proposing search synonyms needs no reasoning while judging candidate fit does; traces showed reasoning tokens spent on term generation with no quality benefit.

Every phase catches its own failures and degrades rather than aborting. A term generation failure falls back to using the finding name as the search term. A search failure or a selection failure marks that finding unresolved. One finding's failure does not block the others.

The prompts carry the exam information, modality, body part, and study description, because it disambiguates both terms and candidates, and deliberately omit the full report text; testing found identical results with 22 percent fewer input tokens without it.[^coding-prompts]

## What the fast path is worth

In prototype testing on chest radiograph extractions, exact and synonym lookup resolved 13 of 16 unique finding names and 12 of 15 unique locations with no model call at all.[^coding-design] The same testing found that a purely deterministic top-candidate choice was not adequate for locations: location assignment needs contextual reasoning even when the finding code resolves deterministically.

# The coding record

Each finding carries a coding bundle holding one finding code and a list of location codes. The list is plural because a finding can span sides or structures, so "lungs" resolves to both the left and the right lung.[^coding-design]

```python
class FindingCodingBundle(StrictBaseModel):
    finding_code: FindingCode = Field(default_factory=FindingCode)
    location_codes: list[LocationCode] = Field(default_factory=list)
```

Both code objects record not only the answer but how it was reached and, when it failed, why.

| Field | Finding code | Location code |
|---|---|---|
| `status` | `coded` or `unmapped` | `coded` or `unmapped` |
| identifier | `oifm_id`, `oifm_name` | `location_id`, `location_name` |
| `method` | `fast-path`, `llm`, or `unresolved` | same three values |
| `reason` | why it is unresolved | why it is unresolved |
| `reasoning` | the model's explanation of the choice or the rejection | same |
| `candidates` | the alternates that were considered | the alternates that were considered |
| `closest_candidate_id` | the nearest miss when unresolved | not carried |

The unresolved reasons are the part worth reading closely, because they are designed to report gaps rather than to hide them.

| Finding reason | Meaning |
|---|---|
| `too_specific` | The candidates narrow beyond what the report states |
| `too_broad` | The candidates are too general to be useful |
| `wrong_concept` | The candidates are different clinical entities |
| `definition_mismatch` | A candidate's name matches but its definition differs, which flags a gap in the ontology |
| `no_candidates` | The search returned nothing |
| `coding_error` | A model or infrastructure failure |

| Location reason | Meaning |
|---|---|
| `no_candidate_match` | The location is known but no candidate fits, which flags a gap in the index |
| `location_unknown` | The location cannot be determined from the available context |
| `no_candidates` | The search returned nothing |
| `coding_error` | A model or infrastructure failure |

Two of these, `definition_mismatch` and `no_candidate_match`, exist specifically so that an unresolved finding becomes evidence about content coverage rather than noise. They are the pipeline's channel back to [the content catalog](/semantic-foundation/finding-models/content-catalog.md) and [the anatomic location data model](/semantic-foundation/anatomic-locations/data-model.md).

The model's own explanation is persisted with the extraction but never written to logs or trace attributes, because it can quote report content.

# Where the location comes from

Choosing a code is the second half of the problem. The first is deciding which anatomic structure the report actually asserts, and that is governed by a written precedence ladder, applied per observation and agreed during a correction pass over the sample data.[^anat-rules] In summary:

1. **Explicit anatomy in the report text or section context wins.** Use the most specific structure stated, sided only if a side is stated. A section heading counts as context.
2. **Otherwise use the finding's own target organ**, at the finding's anatomic granularity and never finer.
3. **Otherwise fall back to the exam-scoped coarse region**, sided only if the exam is sided.

An organ always beats the exam region when the finding has a real target organ, so "lung bases clear" on an abdominal study codes to lung rather than abdomen. Laterality is resolved against the whole report section rather than the isolated quote, because the side is often stated only in a heading; but a side is never inferred from a different exam or from clinical priors. Bilateral findings split into left and right when the lesions are separable and stay generic and unsided when the process is one diffuse entity. A structure absent from the ontology is left unassigned rather than forced to a wrong code. The full rules, including the worked examples and the exam-to-region map, are in [the assignment rules reference](/data-structures/anatomic-location-assignment-rules.md).

The rules name one limitation they do not solve. A generic location and a specific one for the same finding code across exams, "kidney" and "left kidney", still produce separate [Imaging Problem List](/glossary/imaging-problem-list.md) groups. Deciding whether those are one problem or two is called anatomic-compatibility reconciliation and is an open follow-on.[^anat-plan]

# The review artifact

Coding decisions are reviewable as a spreadsheet, not only as JSON. The enrichment script that ran the sample Exam Finding Lists through the production pipeline writes a review CSV of every location decision alongside the enriched files. In the completed pass of 2026-06-10, 260 of 275 findings received a location, and the regenerated [Imaging Problem List](/data-structures/imaging-problem-list.md) was regrouped by finding code together with location identifier.[^anat-plan]

# Earlier designs, now archived

Three generations exist in the repository, and only the third is current.

| Generation | Shape | Status |
|---|---|---|
| Per-finding deterministic then adjudication | One deterministic attempt per finding, then an adjudicating model call | Retired |
| Version 3, batch per chunk | Fast path, then three model calls per report chunk: generate search terms for findings and locations together, select finding codes, select location codes | Marked completed 2026-02-19, then superseded |
| Current, flat merged finding list | Fast path, then four agents across two phases, operating on the merged finding list rather than per chunk | Current, implementation complete on `dev` |

The move from version 3 to the current design changed both the unit of work, from chunk to merged finding list, and the agent count, from three to four, by splitting term generation into separate finding and location agents so each could use a cheaper model.[^coding-archive][^coding-design]

# Where this sits

Coding is a stage of [the report extraction platform](/applications/report-extraction-platform.md) and runs as its own asynchronous job. Its inputs are the finding model corpus and the anatomic location data set, and its output is what makes an [Observation](/glossary/observation.md) interoperable at all: without codes, an extracted finding is text. See [the architecture overview](/overview/architecture.md) for why the identifiers are the joints of the whole system.

[^coding-design]: Coding agent design, imaging-problem-list dev branch
[^coding-prompts]: Coding agent prompt catalog, imaging-problem-list dev branch
[^coding-archive]: Finding and location code assignment plan, version 3, archived
[^anat-rules]: Anatomic location assignment rules, imaging-problem-list dev branch
[^anat-plan]: Anatomic locations for Exam Finding Lists and Imaging Problem Lists plan
