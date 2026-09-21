---
type: Glossary Term
title: Finding model
description: A machine-readable definition of one radiology finding, its synonyms, and the attributes a radiologist uses to characterize it.
tags: [glossary, semantic-foundation, finding-models]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: fm-py
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/finding_model.py
    title: FindingModelBase and FindingModelFull docstrings in the findingmodel package
  - id: overview
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/oifm-overview.md
    title: "Finding Models: Overview, copy of the upstream authoring guidance"
  - id: lineage
    resource: https://github.com/openimagingdata/OpenImagingDataModel.py/blob/455e5b68d730ea8829083d73064de0ec316d3c4a/openimagingdatamodel/cde_set/finding_model.py
    title: The earlier FindingModel class in the OpenImagingDataModel.py reference implementation
  - id: claude-md
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/CLAUDE.md
    title: findingmodels repository conventions
---

# Finding model

A finding model is "the definition of a radiology finding what the finding is such as might be included in a textbook along with definitions of the relevant attributes that a radiologist might use to characterize the finding in a radiology report."[^fm-py] The same sentence, near-verbatim, defines the concept in the 2024 reference implementation, so the definition has been stable across the project's lifetime.[^lineage]

A finding model is a definition, not an occurrence. The occurrence of a finding on one exam is an [observation](/glossary/observation.md). The definition is what gives that occurrence a coded identity and tells a consuming system what the attribute values mean.

The authoring guidance defines an imaging finding broadly as "any observation a radiologist makes about an image and documents in a report," covering pathology, physiologic observations, devices and hardware, postsurgical states, anatomic variants, and image quality observations. The working test is whether a radiologist would write "there is X" or "no X" as a standalone statement.[^overview]

## Synonyms and near-synonyms

- **Open Imaging Finding Model (OIFM)** is the formal name; see [OIFM](/glossary/oifm.md) for the specification-versus-identifier distinction.
- **Finding definition** and **finding type** are used loosely for the same thing; "finding type" also appears in [Imaging Problem List](/glossary/imaging-problem-list.md) field names.
- **[CDE set](/glossary/cde-set.md)** is the governed RadElement counterpart. A finding model is faster to author and not balloted.
- **[FindingClass](/glossary/finding-class.md)** is the next-generation vocabulary's counterpart node type, with attributes factored out into shared elements.
- **Finding** alone means the clinical thing observed, not the definition.

## Identifier form

`OIFM_[A-Z]{3,4}_[0-9]{6}`. Definitions live one per file as `defs/<snake_case_name>.fm.json`, and `ids.json` maps every identifier to its file.[^claude-md]

## Where it is used

[Why finding models](/semantic-foundation/finding-models/why-finding-models.md), [Finding model format](/semantic-foundation/finding-models/finding-model-format.md), [Content catalog](/semantic-foundation/finding-models/content-catalog.md), and [Finding models and CDEs](/semantic-foundation/finding-models/finding-models-and-cdes.md).

[^fm-py]: FindingModelBase docstring in the findingmodel package
[^overview]: "Finding Models: Overview", upstream authoring guidance
[^lineage]: FindingModel class in OpenImagingDataModel.py
[^claude-md]: findingmodels repository conventions
