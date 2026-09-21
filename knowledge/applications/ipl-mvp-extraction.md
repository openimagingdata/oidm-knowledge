---
type: Project Profile
title: IPL MVP extraction and labeling
description: The 2025 four-stage prototype that extracted findings from reports and matched them to finding models by embedding similarity, its measured results, and why it was superseded.
tags: [applications, extraction, llm, embeddings, lineage]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
stale_after: 2027-09-21
sources:
  - id: mvp-readme
    resource: https://github.com/openimagingdata/IPL-MVP-ExtractionAndLabeling/blob/b06948fa417aeff0a6a4b97729c915b3ce5d5ed4/README.md
    title: IPL-MVP-ExtractionAndLabeling README, main branch
    last_modified: 2025-10-20
  - id: mvp-schemas
    resource: https://github.com/openimagingdata/IPL-MVP-ExtractionAndLabeling/blob/b06948fa417aeff0a6a4b97729c915b3ce5d5ed4/src/schemas.py
    title: IPL-MVP-ExtractionAndLabeling extraction and mapping schemas, main branch
  - id: mvp-fhir
    resource: https://github.com/openimagingdata/IPL-MVP-ExtractionAndLabeling/blob/5ea6720e114d3e2cdded5c39ecc5a2eb108e97fb/FHIR_Example_Structure
    title: Persistent FHIR resources design note, IPL-MVP-ExtractionAndLabeling Persistent_FHIR_Resources branch
  - id: mvp-pydantic
    resource: https://github.com/openimagingdata/IPL-MVP-ExtractionAndLabeling/blob/f4b39ca60f4a61da31a704cd944b5375a50b3cd2/step1_extract.py
    title: Typed-agent port of the extraction step, IPL-MVP-ExtractionAndLabeling pydantic branch
  - id: mvp-ms
    resource: https://github.com/openimagingdata/IPL-MVP-ExtractionAndLabeling/tree/4bab557d1a6effa11887dec038c1dba8786046bf/data
    title: Longitudinal multiple sclerosis sample series, IPL-MVP-ExtractionAndLabeling MS-example branch
---

# Purpose

This repository was the first end-to-end attempt at the [Imaging Problem List](/glossary/imaging-problem-list.md) goal: read radiology reports, pull findings out of them, and attach each finding to a standard [finding model](/glossary/finding-model.md) definition, so that a finding could be tracked across a patient's studies. Its own framing is longitudinal monitoring of radiologic findings using common data elements.[^mvp-readme]

It is superseded. [The report extraction platform](/applications/report-extraction-platform.md) on the `imaging-problem-list` development branch does everything this does and the things this could not. This profile records what it established and what it measured, because both shaped the design that replaced it. The wider sequence is in [extraction approaches](/history/extraction-approaches.md).

# What a user does with it

Four scripts run in order from a local Python environment, with a human reviewing between the machine steps.[^mvp-readme]

| Step | Script | Input and output |
|---|---|---|
| 1 | `step1_extract.py` | Reports in JSON Lines to extracted findings in JSON Lines |
| 1A | `step0_review_extracted.py` | Human inspection of the extracted findings before mapping |
| 2 | `step2_map.py` | Extracted findings plus finding models to mapped findings with confidence scores |
| 3 | `step3_review_mappings.py` | A human-readable mapping summary as a CSV |

A single configuration file holds the models, the file paths, the extraction prompt, and the similarity threshold.

# The data and the schema

The schema is deliberately thin. A finding is a name and a boolean [presence](/glossary/presence.md); a mapping adds the matched finding model identifier and name, a confidence score, and a status.[^mvp-schemas]

```python
class Finding(BaseModel):
    name: str
    present: bool

class MappedFinding(BaseModel):
    extracted_finding_name: str
    present: bool
    matched_finding_model_id: str
    matched_finding_model_name: str
    confidence_score: float
    status: str
```

It produces neither an [Exam Finding List](/glossary/exam-finding-list.md) nor an Imaging Problem List, and no FHIR output at all; the README lists generating FHIR Observation resources as a future enhancement.[^mvp-readme] There is no location, no size, no severity, and no [change from prior](/glossary/change-from-prior.md).

The reference set of finding models is a static local JSON file of 15 curated neurological finding models, not a live read from the content repository. That is the file the repository calls its reference, and swapping it for a real service is named as a future enhancement.

# Language model use

Two calls, both to hosted services.[^mvp-readme]

- **Extraction.** A general-purpose model reads each report under a system prompt and returns findings as name and presence pairs.
- **Matching.** Each extracted finding name is embedded, and the embedding is compared by cosine similarity against the embedded names of the 15 reference models. The highest scoring match above a configurable threshold of 0.70 is accepted; everything below it is flagged for manual review.

Matching is therefore name-to-name similarity. No index lookup, no candidate generation, and no model judgment about whether the candidate actually fits.

# Architecture

Four standalone Python scripts over JSON Lines files, with Pydantic for validation and cosine similarity over embedding vectors. No service, no database, no web interface. A mockups directory holds interface images for a review and labeling tool that was never built.

# Results and limits, as measured

The README reports one informal run.[^mvp-readme]

| Measure | Value |
|---|---|
| Reports processed | 8 |
| Findings extracted | 87 |
| Matched at or above the 0.70 threshold | 5 |
| Flagged for manual review | 82 |
| Reference finding models | 15, neurological |

That is a match rate of roughly 6 percent. The three matches quoted as successes score 0.778, 0.806, and 0.761. There is no labeled evaluation set and no metrics harness.

The README states its own limitations plainly: binary presence and absence only with no severity or size, manually curated reference models limited to neurological findings, no handling of negated findings, and a static threshold. The negation limitation matters most, because explicit negatives are exactly what an Exam Finding List is supposed to carry.

# Repository and branch of record

`IPL-MVP-ExtractionAndLabeling` in the `openimagingdata` organization; see [the repository map](/repositories/repository-map.md).

| Branch | Tip commit | Date | Content |
|---|---|---|---|
| `main` | `b06948f` | 2025-10-20 | Branch of record |
| `Persistent_FHIR_Resources` | `5ea6720` | 2025-10-28 | A design note, no code |
| `pydantic` | `f4b39ca` | 2025-10-28 | The extraction step ported to a typed agent |
| `MS-example` | `4bab557` | 2025-10-31 | A replacement sample dataset |

No open issues and no pull requests, open or closed. Status: lineage.

# The three experiment branches

All three were pushed within one week and none was merged.

**A persistent FHIR design note.** One file, without a markdown extension, proposing that each finding be tracked as a persistent FHIR Observation with a stable identifier, so that repeat mentions of the same lesion across reports attach to one entity with its own timeline. It sketches a three-step pipeline, extract and map to codes, create or link a resource, then query the finding's timeline, and a patient to resource to dated-observation shape. It adds no code and names two modules that were never written.[^mvp-fhir] The idea is a genuine precursor to the grouping question the current Imaging Problem List answers structurally; see [FHIR mapping](/data-structures/fhir-mapping.md).

**A typed-agent port.** The extraction step rewritten to use a typed agent with a declared result type and automatic retries, replacing a raw client call with manual JSON fence stripping. The schemas are unchanged. The commit was captured mid-draft, with explanatory prose left inside the Python file.[^mvp-pydantic]

**A longitudinal sample series.** The eight generic sample reports replaced with nine reports for one synthetic multiple sclerosis patient spanning 2019 to 2024, from an initial workup through follow-up studies.[^mvp-ms] It pairs with the FHIR design note's track-a-finding-over-time use case.

# What it established

Two things carried forward into the current platform. [Presence](/glossary/presence.md) belongs in the extracted record as a first-class field, not as an afterthought. And embedding similarity against a small set of names is not a coding strategy: a 6 percent match rate against 15 definitions is the measurement that motivated a deterministic index lookup with language model candidate selection on top, described in [finding and location coding](/applications/finding-and-location-coding.md).

[^mvp-readme]: IPL-MVP-ExtractionAndLabeling README, main branch
[^mvp-schemas]: IPL-MVP-ExtractionAndLabeling extraction and mapping schemas, main branch
[^mvp-fhir]: Persistent FHIR resources design note, Persistent_FHIR_Resources branch
[^mvp-pydantic]: Typed-agent port of the extraction step, pydantic branch
[^mvp-ms]: Longitudinal multiple sclerosis sample series, MS-example branch
