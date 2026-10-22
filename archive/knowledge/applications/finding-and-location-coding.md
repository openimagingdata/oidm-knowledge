---
type: Concept
title: Finding and location coding
description: How deterministic lookup and language models assign OIFM finding codes and RadLex location codes.
tags: [applications, coding, anatomic-locations, llm, extraction]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:34:50Z }
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

[Extraction](/glossary/extraction.md) records what the report says. Coding matches findings to existing definitions. The current pipeline persists uncoded extractions and runs coding separately, without rereading the report. Coding can be rerun with different models.[^coding-design] Two earlier designs did it inside extraction and were retired.

Finding and location codes are independent. A finding receives an [OIFM identifier](/glossary/oifm.md) for its [finding model](/glossary/finding-model.md). A stated location receives a [RadLex identifier](/glossary/radlex-id.md) from the [anatomic locations](/glossary/anatomic-location.md) dataset. Either can succeed while the other fails.

# The pipeline

Coding uses the completed extraction's flat merged finding list. Each finding carries its name, [presence](/glossary/presence.md), location fields, verbatim quote, and source section. The design treats these as sufficient context because extraction has resolved chunk-level ambiguity.[^coding-design]

The pipeline has five phases. Two call language models.

| Phase | What happens |
|---|---|
| 1. Fast path | Exact or synonym lookup in the finding index by name, and in the anatomic location index by specific anatomy. Findings that resolve skip the rest for that axis |
| 2. Term generation | Two agents, one for findings and one for locations, generate two or three diverse search terms for each finding that missed the fast path |
| 3. Index search | Batch embedding search over all terms at once; results are distributed back per finding, deduplicated, and capped |
| 4. Code selection | Two agents, one for findings and one for locations, choose from the candidate set, running concurrently under a semaphore |
| 5. Assembly | Fast-path and selected results merge into one coding bundle per finding |

Four agents perform term generation and selection. Term generation uses a different model because traces showed reasoning tokens added no quality benefit when proposing synonyms. Candidate selection requires reasoning.

Each phase handles its failures. Failed term generation falls back to the finding name. Failed search or selection marks the finding unresolved without blocking other findings.

The prompts carry the exam information, modality, body part, and study description, because it disambiguates both terms and candidates, and deliberately omit the full report text; testing found identical results with 22 percent fewer input tokens without it.[^coding-prompts]

## What the fast path is worth

In chest radiograph prototype tests, exact and synonym lookup resolved 13 of 16 unique finding names and 12 of 15 unique locations without model calls.[^coding-design] Deterministic top-candidate selection was insufficient for locations, which needed contextual reasoning even when finding codes resolved deterministically.

# The coding record

A coding bundle holds one finding code and a list of location codes. Findings can span sides or structures, so "lungs" resolves to both lungs.[^coding-design]

```python
class FindingCodingBundle(StrictBaseModel):
    finding_code: FindingCode = Field(default_factory=FindingCode)
    location_codes: list[LocationCode] = Field(default_factory=list)
```

Both code objects record the result, method, and failure reason.

| Field | Finding code | Location code |
|---|---|---|
| `status` | `coded` or `unmapped` | `coded` or `unmapped` |
| identifier | `oifm_id`, `oifm_name` | `location_id`, `location_name` |
| `method` | `fast-path`, `llm`, or `unresolved` | same three values |
| `reason` | why it is unresolved | why it is unresolved |
| `reasoning` | the model's explanation of the choice or the rejection | same |
| `candidates` | the alternates that were considered | the alternates that were considered |
| `closest_candidate_id` | the nearest miss when unresolved | not carried |

Unresolved reasons distinguish content gaps from processing failures.

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

`definition_mismatch` and `no_candidate_match` identify gaps in [the content catalog](/semantic-foundation/finding-models/content-catalog.md) and [the anatomic location data model](/semantic-foundation/anatomic-locations/data-model.md).

Model explanations persist with the extraction but never enter logs or trace attributes because they can quote report content.

# Where the location comes from

The assignment rules determine the anatomic structure before code selection, governed by a written precedence ladder, applied per observation and agreed during a correction pass over the sample data.[^anat-rules]

1. Use the most specific anatomy stated in the report text or section context. Add a side only when stated.
2. Otherwise use the finding's own target organ, at the finding's anatomic granularity and never finer.
3. Otherwise, use the coarse exam region, sided only if the exam is sided.

An organ always beats the exam region when the finding has a real target organ. For example, "lung bases clear" on an abdominal study codes to lung. Resolve laterality from the whole report section, including its heading. Never infer a side from another exam or clinical priors. Split separable bilateral lesions into left and right, but keep a diffuse bilateral process generic and unsided. Leave structures absent from the ontology unassigned. See [the assignment rules reference](/data-structures/anatomic-location-assignment-rules.md) for examples and the exam-to-region map.

Generic and specific locations for the same finding code across exams, such as "kidney" and "left kidney", still produce separate [Imaging Problem List](/glossary/imaging-problem-list.md) groups. Deciding whether those are one problem or two is called anatomic-compatibility reconciliation and is an open follow-on.[^anat-plan]

# The review artifact

The sample Exam Finding List enrichment script writes a review CSV of every location decision alongside the enriched files. In the 2026-06-10 pass, 260 of 275 findings received a location. The regenerated [Imaging Problem List](/data-structures/imaging-problem-list.md) groups by finding code and location identifier.[^anat-plan]

# Earlier designs, now archived

Three generations exist in the repository, and only the third is current.

| Generation | Shape | Status |
|---|---|---|
| Per-finding deterministic then adjudication | One deterministic attempt per finding, then an adjudicating model call | Retired |
| Version 3, batch per chunk | Fast path, then three model calls per report chunk: generate search terms for findings and locations together, select finding codes, select location codes | Marked completed 2026-02-19, then superseded |
| Current, flat merged finding list | Fast path, then four agents across two phases, operating on the merged finding list rather than per chunk | Current, implementation complete on `dev` |

The current design split term generation into finding and location agents so each could use a cheaper model.[^coding-archive][^coding-design]

# Where this sits

Coding runs as an asynchronous job in [the report extraction platform](/applications/report-extraction-platform.md). It uses the finding model corpus and anatomic location dataset to assign standard identifiers to an [Observation](/glossary/observation.md). See [the architecture overview](/overview/architecture.md).

[^coding-design]: Coding agent design, imaging-problem-list dev branch
[^coding-prompts]: Coding agent prompt catalog, imaging-problem-list dev branch
[^coding-archive]: Finding and location code assignment plan, version 3, archived
[^anat-rules]: Anatomic location assignment rules, imaging-problem-list dev branch
[^anat-plan]: Anatomic locations for Exam Finding Lists and Imaging Problem Lists plan
