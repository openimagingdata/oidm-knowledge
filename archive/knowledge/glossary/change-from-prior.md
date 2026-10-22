---
type: Glossary Term
title: Change from prior
description: The companion second attribute of a finding model, recording how the finding compares with the previous exam.
tags: [glossary, semantic-foundation, data-structures]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: overview
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/oifm-overview.md
    title: "Finding Models: Overview, required change-from-prior attribute"
  - id: ipl-readme
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/README.md
    title: imaging-problem-list README, FHIR components carrying change from prior
  - id: extraction
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/initial-extraction-plan.md
    title: Initial extraction plan, change_from_prior attribute key
  - id: cleanup
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/docs/plans/definition_cleanup.md
    title: Definition cleanup plan, missing standard attributes
---

# Change from prior

How a finding compares with the previous exam. Authoring guidance makes it the required second [attribute](/glossary/attribute.md) of a [finding model](/glossary/finding-model.md), after [presence](/glossary/presence.md), with values "unchanged, stable, new, resolved, plus clinically appropriate direction-of-change pairs (larger/smaller for masses, worsened/improved for diseases, increased/decreased for quantities)."[^overview]

The attribute exists because a finding is not a snapshot. "Findings exist in time. A radiology report is a snapshot, but the findings it describes persist across exams. A pleural effusion seen today may be the same one from last week, now larger."[^overview] Change from prior records this comparison on a single [observation](/glossary/observation.md). The documented FHIR mapping calls for both change-from-prior and presence components.[^ipl-readme]

Change from prior is also what distinguishes an attribute value from a finding. "Stable cardiac silhouette" is not a finding, because "stable" is a change-from-prior value on a cardiac finding.[^overview]

## Synonyms and near-synonyms

- **Interval change** and **temporal change** are clinical equivalents.
- **`change_from_prior`** is the key name in the extraction schema, one of the standard attribute keys alongside size, acuity, severity, count, and morphology.[^extraction]
- **Temporal status** on an [Imaging Problem List](/glossary/imaging-problem-list.md) is different: it is computed across all observations of a finding rather than asserted on one.
- **Tracking identity** is a further step again, linking the same physical entity across reports, which OIDM does not currently do.

## Identifier form

An ordinary `OIFMA_[A-Z]{3,4}_[0-9]{6}` attribute identifier with dot-suffixed value codes.

## Where it is used

[Finding model format](/semantic-foundation/finding-models/finding-model-format.md), [Observation](/data-structures/observation.md), and [Imaging Problem List](/data-structures/imaging-problem-list.md).

## Conflicts

Guidance requires this attribute, but some models lack it. The open cleanup plan schedules addition of missing presence and change-from-prior attributes to 124 models. Consumers cannot assume the attribute exists.[^cleanup] Direction-of-change pairs vary by finding, so no single enumeration covers the corpus.

[^overview]: "Finding Models: Overview"
[^ipl-readme]: imaging-problem-list README
[^extraction]: Initial extraction plan
[^cleanup]: Definition cleanup plan
