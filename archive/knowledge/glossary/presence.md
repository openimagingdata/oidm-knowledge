---
type: Glossary Term
title: Presence
description: The near-universal first attribute of a finding model, asserting that a finding was present, absent, indeterminate, or unknown, and the dot-code convention that encodes those values.
tags: [glossary, semantic-foundation, data-structures]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: overview
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/oifm-overview.md
    title: "Finding Models: Overview, required presence attribute"
  - id: fm-py
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/finding_model.py
    title: Value-code generation in the findingmodel package
  - id: ipl-claude
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/CLAUDE.md
    title: imaging-problem-list domain model, attribute code convention
  - id: extraction
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/initial-extraction-plan.md
    title: Initial extraction plan, presence literal values
  - id: idr
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md
    title: IHE IDR Phase II extract, presence in the parent or as first child
---

# Presence

The assertion that a finding was present, absent, indeterminate, or unknown on an exam. Authoring guidance makes it the required first [attribute](/glossary/attribute.md) of every [finding model](/glossary/finding-model.md), with the value set "absent, present, indeterminate, unknown."[^overview]

"Findings must cover negative assertions. When a radiologist states 'no fracture' or 'upper abdomen is unremarkable,' that's an active observation of absence that needs to be captured... The `presence: absent` observation is clinically meaningful, it means the finding was looked for and not found."[^overview]

Value codes append a dot and the value's zero-based position in the attribute's value list.[^fm-py] The standard ordering gives `.0` absent, `.1` present, `.2` indeterminate, `.3` unknown, which is the convention consuming code documents: "`.1` = present, `.0` = absent."[^ipl-claude] Across the 2,382 published definitions, 2,261 carry a presence attribute and 2,223 of those use that ordering.

## Synonyms and near-synonyms

- **Presence or absence** and **present/absent** describe the same attribute.
- **Detected** is IHE IDR's value for the same assertion.[^idr]
- **Indeterminate** means the exam could not determine it; **unknown** means it was not assessed. These are distinct values.
- **[Change from prior](/glossary/change-from-prior.md)** is the companion second attribute, not part of presence.

## Identifier form

An ordinary `OIFMA_[A-Z]{3,4}_[0-9]{6}` attribute identifier with dot-suffixed value codes.

## Where it is used

[Finding model format](/semantic-foundation/finding-models/finding-model-format.md), [Exam Finding List](/data-structures/exam-finding-list.md), and [Imaging Problem List](/data-structures/imaging-problem-list.md).

## Conflicts

Three disagreements are live.

1. **The dot code is positional, not semantic.** 38 published definitions order their presence values differently, so `.0` means present rather than absent in those models. Most are CDE-derived or MassGeneral Brigham-contributed. Consuming code that hard-codes `.1` as present is wrong for those definitions.
2. **The value set is not shared with extraction.** The extraction schema uses `present`, `absent`, `indeterminate`, and `possible`, where "'possible' covers hedged language like 'raising the possibility of', 'suggestive of', 'cannot exclude'."[^extraction] `possible` has no finding model counterpart and `unknown` has no extraction counterpart.
3. **Spelling and placement vary.** At least one definition spells the value "indeterminant," and IHE IDR records an open question about whether presence should be the first child of a set or the value of the set itself.[^idr]

[^overview]: "Finding Models: Overview"
[^fm-py]: Value-code generation in the findingmodel package
[^ipl-claude]: imaging-problem-list domain model, dev branch
[^extraction]: Initial extraction plan
[^idr]: IHE IDR Phase II extract
