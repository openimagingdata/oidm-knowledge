---
type: Glossary Term
title: Extraction
description: Deriving structured findings from narrative radiology report text with a language model, producing findings, presence, location, and attributes with verbatim quotes.
tags: [glossary, applications, extraction]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: extraction-plan
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/initial-extraction-plan.md
    title: Initial extraction plan, extraction schema, imaging-problem-list dev branch
  - id: ipl-claude
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/CLAUDE.md
    title: imaging-problem-list architecture notes, dev branch
  - id: validator
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/prompts/validator_prompt_example.md
    title: Validator prompt example, imaging-problem-list dev branch
  - id: overview
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/oifm-overview.md
    title: "Finding Models: Overview, the pipeline from report to observation"
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026
---

# Extraction

Deriving structured findings from narrative radiology report text using a language model. The authoring overview states: "an agent reads a radiology report and identifies findings mentioned in the text," and each finding is then matched to a definition.[^overview] The deck states the goal that an [Imaging Problem List](/glossary/imaging-problem-list.md) be "automatically extractable from narrative report text via LLMs."[^deck]

The uncoded output contains a finding name, presence as `present`, `absent`, `indeterminate`, or `possible`, and a verbatim `report_text` quote. An optional location records body region, specific anatomy, and laterality. Key-value attributes use standard keys such as size, acuity, change from prior, severity, count, and morphology.[^extraction-plan] Assigning identifiers is a separate job; see [coding](/glossary/coding.md).

The implementation splits long reports into semantic chunks, extracts them concurrently, and merges and deduplicates the results. It validates verbatim quotes during and after generation. A reviewer sub-agent can flag issues and trigger re-extraction of specific chunks.[^ipl-claude]

## Synonyms and near-synonyms

- **Finding extraction** and **report extraction** are the same activity.
- **[Coding](/glossary/coding.md)** is the separate downstream step that assigns identifiers.
- **Mapping** is the older MVP pipeline's word for coding by embedding similarity.
- **Mini-observation** is the staging repository's term for one extracted finding, attribute, and value tuple.

## Identifier form

None. Extracted findings carry names and quotes, not identifiers, until coding runs.

## Where it is used

[Report extraction platform](/applications/report-extraction-platform.md), [IPL MVP extraction](/applications/ipl-mvp-extraction.md), and [Extraction approaches](/history/extraction-approaches.md).

## Conflicts

The failure modes extraction guards against are stated in the validator prompt: hallucinated content unsupported by the chunk, report text describing a finding that no structure represents, which is a missed finding, a finding described as present when it is not, or absent when it is possible, overly specific finding names, misrepresented blanket negatives, and incorrect or overly specific or general locations.[^validator] Separately, the extraction presence value set does not match the finding model one; see [presence](/glossary/presence.md).

[^extraction-plan]: Initial extraction plan
[^ipl-claude]: imaging-problem-list architecture notes
[^validator]: Validator prompt example
[^overview]: "Finding Models: Overview"
[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
