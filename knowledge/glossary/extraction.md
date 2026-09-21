---
type: Glossary Term
title: Extraction
description: Deriving structured findings from narrative radiology report text with a language model, producing findings, presence, location, and attributes with verbatim quotes.
tags: [glossary, applications, extraction]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
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

Deriving structured findings from narrative radiology report text using a language model. It is the first half of the pipeline that turns a report into OIDM data: "an agent reads a radiology report and identifies findings mentioned in the text," and each finding is then matched to a definition.[^overview] The deck states the goal that an [Imaging Problem List](/glossary/imaging-problem-list.md) be "automatically extractable from narrative report text via LLMs."[^deck]

Extraction output is uncoded. Its schema names a finding, asserts presence as one of `present`, `absent`, `indeterminate`, or `possible`, gives an optional location of body region, specific anatomy, and laterality, a list of key-value attributes with standard keys such as size, acuity, change from prior, severity, count, and morphology, and a verbatim `report_text` quote.[^extraction-plan] Assigning identifiers is a separate job; see [coding](/glossary/coding.md).

Three design decisions shape the current implementation: long reports are semantically chunked and extracted concurrently then merged and deduplicated, output quotes are validated as verbatim both during and after generation, and a reviewer sub-agent can flag issues and trigger targeted re-extraction of specific chunks.[^ipl-claude]

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

The failure modes extraction guards against are stated in the validator prompt and are worth naming as part of the definition: content unsupported by the chunk text, which is hallucination; report text describing a finding that no structure represents, which is a missed finding; a finding described as present when it is not, or absent when it is possible; a finding name more specific than the text supports; incorrect representation of a blanket negative; and wrong, too specific, or too general location information.[^validator] Separately, the extraction presence value set does not match the finding model one; see [presence](/glossary/presence.md).

[^extraction-plan]: Initial extraction plan
[^ipl-claude]: imaging-problem-list architecture notes
[^validator]: Validator prompt example
[^overview]: "Finding Models: Overview"
[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
