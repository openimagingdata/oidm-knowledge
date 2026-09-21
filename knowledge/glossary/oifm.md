---
type: Glossary Term
title: OIFM
description: Open Imaging Finding Model, the OIDM specification for a finding definition, and the prefix of the identifiers that specification mints.
tags: [glossary, semantic-foundation, finding-models]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: fm-py
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/finding_model.py
    title: FindingModelFull and the OIFM identifier pattern in the findingmodel package
  - id: fm-schema
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/schema/finding_model_schema.md
    title: Finding model schema, prose mirror, findingmodels repository
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026
---

# OIFM

**Open Imaging Finding Model (OIFM).** The OIDM specification that defines what a [finding model](/glossary/finding-model.md) is: a named radiology finding with a description, optional synonyms and tags, a list of characterizing [attributes](/glossary/attribute.md), optional [anatomic locations](/glossary/anatomic-location.md) and [index codes](/glossary/index-code.md), and optional [contributors](/glossary/contributor.md).[^fm-schema] The canonical statement of the format is the `FindingModelFull` Pydantic model in the `findingmodel` package.[^fm-py]

"OIFM" is also the literal prefix of the identifier minted for each finding model, which is why the two senses are easy to confuse. The deck expands the acronym as "Open Imaging Finding Models" when counting content, reporting nearly 3,000 definitions.[^deck]

## Synonyms and near-synonyms

- **Finding model** is the everyday name for one instance of the thing OIFM specifies. This knowledgebase says "Open Imaging Finding Model (OIFM)" on first use and "finding model" thereafter.
- **OIFM ID** means only the identifier, never the specification.
- **OIFMA** is the sibling prefix for [attribute](/glossary/attribute.md) identifiers, not a separate specification.
- **CDE Set** is the RadElement-published counterpart of a finding definition, governed separately. See [CDE set](/glossary/cde-set.md).

## Identifier form

`OIFM_[A-Z]{3,4}_[0-9]{6}`, for example `OIFM_GMTS_016552`. The middle segment is the [organization code](/glossary/oidm-organization-code.md) of the contributing organization; the six digits are randomly generated, not sequential.[^fm-py]

## Where it is used

[Finding model format](/semantic-foundation/finding-models/finding-model-format.md) documents the fields, [Identifiers](/semantic-foundation/finding-models/identifiers.md) the ID scheme, and [Content catalog](/semantic-foundation/finding-models/content-catalog.md) the published corpus.

[^fm-py]: FindingModelFull and the OIFM identifier pattern in the findingmodel package
[^fm-schema]: Finding model schema, prose mirror, findingmodels repository
[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
