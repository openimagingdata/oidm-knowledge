---
type: Project Profile
title: Report extraction platform
description: The extraction, coding, persistence, evaluation, and human-review platform on the imaging-problem-list development branch that turns narrative radiology reports into coded findings.
tags: [applications, extraction, llm, ipl, evaluation, phi]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
stale_after: 2027-09-21
sources:
  - id: dev-readme
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/README.md
    title: imaging-problem-list README, dev branch
  - id: dev-claude
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/CLAUDE.md
    title: imaging-problem-list architecture notes, dev branch
  - id: initial-plan
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/initial-extraction-plan.md
    title: Initial extraction plan and schema, imaging-problem-list dev branch
  - id: validator
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/prompts/validator_prompt_example.md
    title: Chunk-level validator prompt, imaging-problem-list dev branch
  - id: eval-usage
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/eval-usage.md
    title: Evaluation harness user guide, imaging-problem-list dev branch
  - id: evals-redesign
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/extractor-evals-redesign.md
    title: Extractor evals redesign plan, imaging-problem-list dev branch
    last_modified: 2026-07-07
  - id: review-workflow
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/human-review-workflow.md
    title: Human review workflow for gold extractions, imaging-problem-list dev branch
  - id: reviewer-plan
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/extraction-reviewer.md
    title: Standalone extraction reviewer plan, imaging-problem-list dev branch
  - id: reviewer-workflows
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/extraction-reviewer-workflows.md
    title: Extraction reviewer integration and workflow plan, imaging-problem-list dev branch
    last_modified: 2026-07-07
  - id: reviewer-ux
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/extraction-reviewer-ux.md
    title: Extraction reviewer UX evaluation plan, imaging-problem-list dev branch
    last_modified: 2026-07-20
  - id: ui-review-ux
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/extractor-ui-review-ux.md
    title: Extractor UI review UX evaluation and redesign plan, imaging-problem-list dev branch
    last_modified: 2026-07-19
  - id: local-hardening
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/archive/local-only-mode-hardening.md
    title: Local-only mode hardening plan, imaging-problem-list dev branch
    last_modified: 2026-04-12
  - id: local-tightening
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/local-only-future-tightening.md
    title: Future local-only tightening plan, imaging-problem-list dev branch
  - id: mlx
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/local-model-mlx-reassessment.md
    title: Local model reassessment plan, imaging-problem-list dev branch
    last_modified: 2026-07-01
  - id: thinking
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/pydantic-ai-thinking-capability-simplification.md
    title: Reasoning plumbing simplification plan, imaging-problem-list dev branch
---

# Purpose

The extraction platform turns narrative radiology report text into structured, coded findings that can be assembled into an [Exam Finding List](/glossary/exam-finding-list.md) and then an [Imaging Problem List](/glossary/imaging-problem-list.md). It is the seventh and current attempt at that problem in this project; the six before it, and what each established, are in [extraction approaches](/history/extraction-approaches.md).

It lives on the `dev` branch of `imaging-problem-list`, 258 commits ahead of `main` as of tip commit `36fa30c`, 2026-07-22. `main` remains the stable data-structure specification and the deployed [viewer](/applications/imaging-problem-list-viewer.md). Nothing described here has merged.

# What a user does with it

Four command-line entry points and one web interface.[^dev-readme]

| Entry point | What it does |
|---|---|
| `finding-extractor` | Extract findings from one report, choosing model and reasoning level |
| `finding-extractor-batch` | Run a directory of reports, interactively or detached, with resume |
| `finding-extractor-code` | Run the post-extraction coding pipeline over a saved extraction |
| `finding-extractor-eval` | Score extraction quality against a dataset |
| Extractor web interface | Submit a report, browse reports, open an extraction result, and review it |

The documented human path for producing trustworthy output is a four-step loop: batch-generate one candidate extraction file per report, have a reviewer overread and correct each one, copy the corrected file to a gold file name, and validate every gold file against the extraction model.[^review-workflow] Installation and configuration stay with the code.

# The data

**Input.** Plain report text. A helper script splits a spreadsheet of reports into one text file each, stripping attestation and boilerplate lines.

**Extraction output.** The schema, set out in the original extraction plan, is a finding name, a [presence](/glossary/presence.md) value, an optional location, a list of attributes, and the verbatim report text the finding came from.[^initial-plan]

| Field | Type | Note |
|---|---|---|
| `finding_name` | string | Standard terminology, not raw report phrasing |
| `presence` | `present`, `absent`, `indeterminate`, `possible` | `possible` exists for hedged language such as "raising the possibility of" or "cannot exclude" |
| `location` | body region, specific anatomy, [laterality](/glossary/laterality.md) | Optional |
| `attributes` | key and value pairs | Standard keys: size, acuity, change from prior, severity, count, morphology |
| `report_text` | string | The verbatim quote supporting the finding |

Text that is not a finding is captured separately rather than discarded.

**Persistence.** SQLite through SQLModel, with Alembic migrations. Reports are deduplicated by the SHA-256 hash of their text. Each extraction run is its own row carrying the report link, the timestamp, the model, the reasoning setting, and the full JSON payload; findings and non-finding text live nested inside that payload. Reviewer edits are stored as separate correction rows rather than by mutating the extraction, in three shapes: propose a new finding, suggest an update to an existing one by index or JSON path, and leave a comment for follow-up.[^dev-readme]

**Coded output.** Coding writes back into the same extraction row, populating each finding's coding bundle and updating the coded and unresolved counts. See [finding and location coding](/applications/finding-and-location-coding.md).

# Language model use

Extraction is agentic and multi-provider: OpenAI, Anthropic, Google, OpenRouter, Ollama for local models, and vLLM for on-premises deployments.[^dev-readme] A single reasoning knob with five levels is normalized per provider, because each exposes thinking differently, and some local model families need JSON-schema output mode rather than tool calling.[^dev-claude]

Three architectural decisions shape the pipeline.[^dev-claude]

**Chunking.** Long reports are semantically chunked and the chunks extracted concurrently under a bound, then merged and deduplicated. A reviewer sub-agent can flag problems and trigger targeted re-extraction of specific chunks rather than the whole report.

**Verbatim-quote validation.** Extraction output must carry exact quotes from the report, checked both as an output validator during generation and again afterward.

**Coding as a separate job.** Mapping findings to standard codes happens after extraction, in its own pipeline, and can be re-run with different models without re-extracting.

## The validator contract

The chunk-level validator reviews one chunk's extraction against that chunk's text and returns a single decision object: the chunk identifier, whether to re-extract, a list of problems, and a rationale. The prompt names six issue patterns that justify re-extraction, and one rule that does not.[^validator]

| Problem type | What it catches |
|---|---|
| `hallucination` | Clinically meaningful content unsupported by the chunk text |
| `missed_finding` | Report text describing a finding that no structure represents |
| `wrong_presence` | Present when it is not, or absent when it is possible |
| `over_specific_finding_name` | A finding name more specific than the text supports |
| `incorrect_blanket_negative` | A blanket negative mapped to the wrong or over-specific absent findings |
| `incorrect_location` | Wrong, too specific, or too general location |

Formatting and style differences alone are not grounds for re-extraction. The evidence boundary is explicit: only the chunk is evidence, and the surrounding chunks are advisory. The prompt gives one worked mapping, "clear lungs" becoming an absent finding named "pulmonary parenchymal abnormality", which is the treatment of blanket negatives that `CDEStaging` first catalogued as a problem; see [extraction approaches](/history/extraction-approaches.md).

# Architecture

FastAPI serves the API. Long work is asynchronous: an extraction or coding request returns 202 with a job identifier, TaskIQ workers pull the job through a Redis broker, and the client polls job status. Configuration is centralized in typed settings under an `IPL_` environment namespace. Observability is Logfire spans plus structured logging, with a stated rule that raw report text and verbatim quotes never appear in span attributes or log fields.[^dev-claude]

Two browser interfaces serve different people.

**The extractor interface** is the connected one, built like the viewer with Alpine.js, Flowbite, and Tailwind from a content delivery network and no build step. It submits reports, lists them, and shows extraction results.

**The standalone extraction reviewer** is a single self-contained HTML file that a non-developer can open locally with no install and no network, walk through an extraction's findings, and mark each one approved, flagged, unsure, or missing with free-text notes; the reviewer returns a zip of per-file review JSON.[^reviewer-plan] Its vanilla JavaScript and absence of any content delivery network are a deliberate exception to the project's frontend conventions, justified by the requirement that it work from a local file with nothing installed.[^reviewer-workflows] Its plan is marked complete, and it has become the primary instrument for extraction quality assurance and for adjudicating gold cases.

# Evaluation

A harness runs a named dataset of reports through extraction, compares the output against ground truth, and reports scores, with optional thresholds on finding F1, presence accuracy, and verbatim checks that make the command exit non-zero when they are not met.[^eval-usage]

The design of what it scores was rewritten for honesty. On 2026-07-07, after three and a half months with no implementation, the evaluation redesign was deliberately descoped rather than discarded; the full plan's thresholds, continuous-integration gating, and thirty-case benchmark were named as what made it unstartable.[^evals-redesign] The motivation is a specific failure: a model-selection round on 2026-05-14 made a local model the default on average latency and a thirty percent increase in findings produced, and neither number can tell a real recall gain from a fabricated finding.

Version one keeps four things: a quote-first primary matcher, scoring of attribute *values* rather than attribute presence, frozen run configurations with per-case artifacts for reproducibility, a ten-case gold set adjudicated through the standalone reviewer, and a non-blocking scorecard task. The reviewer plan and the evaluation plan are sequenced rather than parallel; the reviewer exists to produce the gold set the evaluation needs.[^reviewer-workflows]

# Local models and protected health information

Protected health information is named as the next use case, and the platform's answer is a local-only mode. A hardening pass completed 2026-04-12 moved enforcement out of the command-line boundary into a shared preflight helper that every entry point calls, closing gaps where the batch command, the API, and the worker could still reach a cloud provider with local-only set; it also detects cloud-suffixed model names in the local runtime.[^local-hardening] The evaluation command is explicitly outside the guarantee, on the stated ground that evaluation datasets are curated fixtures rather than patient data.

Remaining hardening items were shelved with explicit reopen triggers rather than left as an open-ended list. The example given is detecting a local model alias whose underlying definition points at a cloud source, deferred because the runtime's inspection surface is unstable and parsing model definition files is not authoritative.[^local-tightening]

Local model choice itself is under reassessment rather than settled. The plan opened 2026-07-01 proposes reassessing wholesale rather than patching documentation, on the grounds that both the runtime and the model generations have moved since the May 2026 round, and it flags one new candidate family as unverified for radiology extraction because it is tuned for agentic coding.[^mlx]

# Plans in flight

Eight plans are active on `dev`. Facts and dates as stated in each document.

| Plan | Date | Status |
|---|---|---|
| Extraction reviewer integration and workflows | created 2026-07-07 | Phase A in progress; the reviewer becomes the primary human-review instrument and feeds gold adjudication |
| Extractor evals redesign | updated 2026-07-07 | Active, descoped to version one |
| Extractor interface review UX | created 2026-07-19 | Proposed; its core finding is that the review page does not show the source report text at all |
| Extraction reviewer UX | created 2026-07-20 | Active; Phase 0 complete 2026-07-20, Phases 1 through 3 remain |
| Local model reassessment | created 2026-07-01 | Planned, not started |
| Future local-only tightening | not dated | Not started, active backlog with per-item reopen triggers |
| Reasoning plumbing simplification | not dated | Fully specified, not started; blocked on a library version bump that would retire roughly 728 lines of per-provider translation code[^thinking] |
| Anatomy-first viewer | not dated | Implemented, ready for review; see [the viewer profile](/applications/imaging-problem-list-viewer.md) |

The anatomic location plan that added location codes to the sample Exam Finding Lists is marked complete as of 2026-06-10, with one follow-on open: reconciling generic against specific locations for the same finding across exams, which today produces separate Imaging Problem List groups. Two plans completed in July 2026 are excluded from the table above.

# Open issues

One, number 1, "Create System of Data Models", asking for a formal model layer for [Observation](/glossary/observation.md), Exam Finding List, and Imaging Problem List with schema export. It is broader than any plan above and unclaimed; see [the data model roadmap](/roadmap/ipl-data-model-system.md). The single open pull request is empty, its design document having been moved to a separate repository.

# What it realizes

This platform is where [extraction](/glossary/extraction.md) and [coding](/glossary/coding.md) become operations rather than ideas. It produces the [Observations](/glossary/observation.md) that fill an [Exam Finding List](/data-structures/exam-finding-list.md), attaches [anatomic locations](/glossary/anatomic-location.md) under [the assignment rules](/data-structures/anatomic-location-assignment-rules.md), and resolves [OIFM identifiers](/glossary/oifm.md) against the published registry described in [the content catalog](/semantic-foundation/finding-models/content-catalog.md). The [provenance](/glossary/provenance.md) requirement that each Observation carry a marker of how it was produced is met here by storing the model, the reasoning setting, and the verbatim quote with every extraction. Its place in the layered system is drawn in [the architecture overview](/overview/architecture.md).

[^dev-readme]: imaging-problem-list README, dev branch
[^dev-claude]: imaging-problem-list architecture notes, dev branch
[^initial-plan]: Initial extraction plan and schema, imaging-problem-list dev branch
[^validator]: Chunk-level validator prompt, imaging-problem-list dev branch
[^eval-usage]: Evaluation harness user guide, imaging-problem-list dev branch
[^evals-redesign]: Extractor evals redesign plan, imaging-problem-list dev branch
[^review-workflow]: Human review workflow for gold extractions, imaging-problem-list dev branch
[^reviewer-plan]: Standalone extraction reviewer plan, imaging-problem-list dev branch
[^reviewer-workflows]: Extraction reviewer integration and workflow plan, imaging-problem-list dev branch
[^local-hardening]: Local-only mode hardening plan, imaging-problem-list dev branch
[^local-tightening]: Future local-only tightening plan, imaging-problem-list dev branch
[^mlx]: Local model reassessment plan, imaging-problem-list dev branch
[^thinking]: Reasoning plumbing simplification plan, imaging-problem-list dev branch
