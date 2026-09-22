---
type: Project Profile
title: IPL MVP extraction and labeling
description: The superseded 2025 report-extraction prototype, its embedding-based finding matches, and measured limits.
tags: [applications, extraction, llm, embeddings, lineage]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:34:50Z }
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

This was the first end-to-end prototype to extract radiology findings and match them to [finding model](/glossary/finding-model.md) definitions for longitudinal tracking. Its stated goal was an [Imaging Problem List](/glossary/imaging-problem-list.md) using common data elements.[^mvp-readme]

[The report extraction platform](/applications/report-extraction-platform.md) on `imaging-problem-list`'s development branch supersedes it. See [extraction approaches](/history/extraction-approaches.md) for the wider history.

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

A finding has a name and boolean [presence](/glossary/presence.md). A mapping adds the matched model identifier and name, a confidence score, and a status.[^mvp-schemas]

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

The output lacks location, size, severity, and [change from prior](/glossary/change-from-prior.md). It does not produce an [Exam Finding List](/glossary/exam-finding-list.md), Imaging Problem List, or FHIR resources. The README lists FHIR Observation generation as a future enhancement.[^mvp-readme]

The reference set is a local JSON file of 15 curated neurological finding models. Replacing it with a service is listed as a future enhancement.

# Language model use

Extraction and matching call hosted services.[^mvp-readme]

- A general-purpose model reads each report under a system prompt and returns finding names and presence values.
- Matching compares embeddings of extracted names with embeddings of the 15 reference model names by cosine similarity. It accepts the highest match above the configurable 0.70 threshold and flags lower scores for manual review.

Matching uses name similarity without index lookup, candidate generation, or model judgment of candidate fit.

# Architecture

Four standalone Python scripts read and write JSON Lines, using Pydantic validation and cosine similarity over embeddings. There is no service, database, or web interface. A mockups directory holds images for a review and labeling interface that was never built.

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

The README lists binary presence, missing severity and size, a neurological reference set, unsupported negation, and a static threshold as limitations. Unsupported negation prevents the prototype from extracting the explicit negatives expected in an Exam Finding List.

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

**A persistent FHIR design note.** A file without a markdown extension proposes persistent FHIR Observations with stable identifiers, linking repeated mentions of a lesion into one timeline. It sketches extraction and code mapping, resource creation or linking, and timeline queries, organized by patient, resource, and dated observation. It names two unwritten modules and adds no code.[^mvp-fhir] See [FHIR mapping](/data-structures/fhir-mapping.md) for the related grouping question.

**A typed-agent port.** The extraction step uses a typed agent with a declared result type and automatic retries. It replaces a raw client call and manual JSON fence stripping without changing schemas. The commit is a draft, with explanatory prose left in the Python file.[^mvp-pydantic]

**A longitudinal sample series.** Nine reports for one synthetic multiple sclerosis patient replace the eight generic reports. They span initial workup and follow-up from 2019 to 2024, matching the FHIR note's longitudinal use case.[^mvp-ms]

# What it established

Two things carried forward into the current platform. [Presence](/glossary/presence.md) belongs in the extracted record as a first-class field, not as an afterthought. And embedding similarity against a small set of names is not a coding strategy: a 6 percent match rate against 15 definitions is the measurement that motivated a deterministic index lookup with language model candidate selection on top, described in [finding and location coding](/applications/finding-and-location-coding.md).

[^mvp-readme]: IPL-MVP-ExtractionAndLabeling README, main branch
[^mvp-schemas]: IPL-MVP-ExtractionAndLabeling extraction and mapping schemas, main branch
[^mvp-fhir]: Persistent FHIR resources design note, Persistent_FHIR_Resources branch
[^mvp-pydantic]: Typed-agent port of the extraction step, pydantic branch
[^mvp-ms]: Longitudinal multiple sclerosis sample series, MS-example branch
