---
type: Project Profile
title: Report extraction platform
description: The platform on imaging-problem-list dev for report extraction, coding, storage, review, and evaluation.
tags: [applications, extraction, llm, ipl, evaluation, phi]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:34:50Z }
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

The platform extracts structured, coded findings from radiology reports for [Exam Finding Lists](/glossary/exam-finding-list.md) and [Imaging Problem Lists](/glossary/imaging-problem-list.md). It is the project's seventh extraction approach. See [extraction approaches](/history/extraction-approaches.md) for its predecessors.

It lives on the `dev` branch of `imaging-problem-list`, 258 commits ahead of `main` as of tip commit `36fa30c`, 2026-07-22. `main` remains the stable data-structure specification and the deployed [viewer](/applications/imaging-problem-list-viewer.md). Nothing described here has merged.

# What a user does with it

The platform has four command-line entry points and a web interface.[^dev-readme]

| Entry point | What it does |
|---|---|
| `finding-extractor` | Extract findings from one report, choosing model and reasoning level |
| `finding-extractor-batch` | Run a directory of reports, interactively or detached, with resume |
| `finding-extractor-code` | Run the post-extraction coding pipeline over a saved extraction |
| `finding-extractor-eval` | Score extraction quality against a dataset |
| Extractor web interface | Submit a report, browse reports, open an extraction result, and review it |

The review workflow batch-generates a candidate extraction file for each report. A reviewer checks and corrects each file, copies it to a gold filename, and validates it against the extraction model.[^review-workflow]

# The data

Input is plain report text. A helper splits a spreadsheet into one file per report and strips attestations and boilerplate.

**Extraction output.** The schema, set out in the original extraction plan, is a finding name, a [presence](/glossary/presence.md) value, an optional location, a list of attributes, and the verbatim report text the finding came from.[^initial-plan]

| Field | Type | Note |
|---|---|---|
| `finding_name` | string | Standard terminology, not raw report phrasing |
| `presence` | `present`, `absent`, `indeterminate`, `possible` | `possible` exists for hedged language such as "raising the possibility of" or "cannot exclude" |
| `location` | body region, specific anatomy, [laterality](/glossary/laterality.md) | Optional |
| `attributes` | key and value pairs | Standard keys: size, acuity, change from prior, severity, count, morphology |
| `report_text` | string | The verbatim quote supporting the finding |

Non-finding text is captured separately.

SQLite stores data through SQLModel, with Alembic migrations. SHA-256 hashes deduplicate report text. Each extraction row records its report, timestamp, model, reasoning setting, and JSON payload, including findings and non-finding text. Separate correction rows hold reviewer proposals for new findings, updates by index or JSON path, and follow-up comments.[^dev-readme]

[Finding and location coding](/applications/finding-and-location-coding.md) populates coding bundles in the same extraction row and updates coded and unresolved counts.

# Language model use

Extraction agents support OpenAI, Anthropic, Google, OpenRouter, Ollama for local models, and vLLM for on-premises deployments.[^dev-readme] A five-level reasoning setting maps to each provider's controls. Some local model families require JSON-schema output instead of tool calling.[^dev-claude]

Three architectural decisions shape the pipeline.[^dev-claude]

- **Chunking.** Long reports are semantically chunked, extracted with bounded concurrency, merged, and deduplicated. A reviewer sub-agent can trigger re-extraction of specific chunks.
- **Verbatim-quote validation.** Exact report quotes are required and validated during generation and afterward.
- **Coding as a separate job.** Coding runs separately after extraction and can be rerun with different models.

## The validator contract

The validator compares each chunk's extraction with its text. It returns the chunk identifier, a re-extraction decision, problems, and rationale. Six problem types justify re-extraction.[^validator]

| Problem type | What it catches |
|---|---|
| `hallucination` | Clinically meaningful content unsupported by the chunk text |
| `missed_finding` | Report text describing a finding that no structure represents |
| `wrong_presence` | Present when it is not, or absent when it is possible |
| `over_specific_finding_name` | A finding name more specific than the text supports |
| `incorrect_blanket_negative` | A blanket negative mapped to the wrong or over-specific absent findings |
| `incorrect_location` | Wrong, too specific, or too general location |

Formatting and style alone do not justify re-extraction. Only the chunk is evidence. Surrounding chunks are advisory. The prompt maps "clear lungs" to an absent "pulmonary parenchymal abnormality", addressing the blanket-negative problem first recorded in `CDEStaging`. See [extraction approaches](/history/extraction-approaches.md).

# Architecture

FastAPI serves the API. Long work is asynchronous: an extraction or coding request returns 202 with a job identifier, TaskIQ workers pull the job through a Redis broker, and the client polls job status. Typed settings use the `IPL_` environment namespace. Logfire spans and structured logs must exclude raw report text and verbatim quotes.[^dev-claude]

Two browser interfaces serve different people.

The connected extractor interface, built like the viewer, uses Alpine.js, Flowbite, and Tailwind from a content delivery network, without a build step. It submits reports, lists them, and shows extraction results.

The standalone reviewer is one HTML file that a non-developer can open locally without installation or network access. Reviewers mark findings approved, flagged, unsure, or missing, add notes, and export a zip of per-file review JSON.[^reviewer-plan] Its vanilla JavaScript and absence of any content delivery network are a deliberate exception to the project's frontend conventions, justified by the requirement that it work from a local file with nothing installed.[^reviewer-workflows] Its plan is complete. It is the primary tool for extraction quality assurance and gold-case adjudication.

# Evaluation

The evaluation harness runs extraction over a named report dataset and scores the output against ground truth. Optional thresholds on finding F1, presence accuracy, and verbatim checks cause a nonzero exit when unmet.[^eval-usage]

On 2026-07-07, the evaluation redesign was deliberately descoped rather than discarded, after three and a half months without implementation. The plan cited thresholds, continuous-integration gates, and a thirty-case benchmark as barriers.[^evals-redesign] A 2026-05-14 selection round had made a local model the default based on average latency and thirty percent more findings. Those measures could not distinguish improved recall from fabricated findings.

Version one retains quote-first matching, attribute-value scoring, frozen run configurations with per-case artifacts, a ten-case gold set, and a non-blocking scorecard task. The redesigned evaluation depends on the gold set adjudicated with the standalone reviewer.[^reviewer-workflows]

# Local models and protected health information

Local-only mode supports the planned protected health information use case. A hardening pass completed 2026-04-12 moved enforcement out of the command-line boundary into a shared preflight helper that every entry point calls, closing gaps where the batch command, the API, and the worker could still reach a cloud provider with local-only set. It also detects cloud-suffixed model names in the local runtime.[^local-hardening] The evaluation command is excluded from this guarantee, on the stated ground that evaluation datasets are curated fixtures rather than patient data.

Deferred hardening items have explicit reopen triggers. Detecting aliases whose definitions point to cloud sources is deferred because runtime inspection is unstable and model-definition parsing is not authoritative.[^local-tightening]

The reassessment plan opened 2026-07-01 calls for new local model comparisons since the May 2026 round. It identifies one candidate family as unverified for radiology extraction because it is tuned for agentic coding.[^mlx]

# Plans in flight

Eight plans are active on `dev`, with statuses and dates recorded below.

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

The sample Exam Finding List location-coding plan was completed on 2026-06-10. Reconciling generic and specific locations across exams remains open because they produce separate Imaging Problem List groups. The table excludes two plans completed in July 2026.

# Open issues

Issue 1, "Create System of Data Models", requests formal [Observation](/glossary/observation.md), Exam Finding List, and Imaging Problem List models with schema export. It is unclaimed. See [the data model roadmap](/roadmap/ipl-data-model-system.md). The single open pull request is empty after its design document moved to a separate repository.

# What it realizes

[Extraction](/glossary/extraction.md) and [coding](/glossary/coding.md) produce [Observations](/glossary/observation.md) for an [Exam Finding List](/data-structures/exam-finding-list.md). [Anatomic locations](/glossary/anatomic-location.md) follow [the assignment rules](/data-structures/anatomic-location-assignment-rules.md), and [OIFM identifiers](/glossary/oifm.md) resolve against [the published registry](/semantic-foundation/finding-models/content-catalog.md). The [provenance](/glossary/provenance.md) requirement that each Observation carry a marker of how it was produced is met here by storing the model, the reasoning setting, and the verbatim quote with every extraction. See [the architecture overview](/overview/architecture.md).

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
