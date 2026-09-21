---
type: Glossary Term
title: OIDM organization code
description: The three or four letter uppercase segment inside an OIFM or OIFMA identifier that names the organization which minted it.
tags: [glossary, semantic-foundation, identifiers]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: contributor-py
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/contributor.py
    title: OrganizationCodeField pattern in the findingmodel package
  - id: orgs
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/data/base_organizations.jsonl
    title: Base organization registry in the findingmodel package
  - id: fm-py
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/finding_model.py
    title: OIFM and OIFMA identifier generation in the findingmodel package
---

# OIDM organization code

The middle segment of an OIFM or OIFMA identifier, matching `^[A-Z]{3,4}$`, naming the organization that minted the identifier. The generator builds an identifier by uppercasing the source code and appending six random digits, so the code is chosen by the authoring organization rather than assigned centrally.[^fm-py] The same value serves as an organization's `code` and as a person's `organization_code` in the [contributor](/glossary/contributor.md) registry.[^contributor-py]

Seven codes ship in the base registry.[^orgs]

| Code | Organization |
|---|---|
| `GMTS` | Radiology Gamuts Ontology |
| `OIDM` | Open Imaging Data Model |
| `CDE` | ACR/RSNA Common Data Elements Project |
| `MGB` | MassGeneral Brigham |
| `MSFT` | Microsoft |
| `RSNA` | Radiological Society of North America |
| `ACR` | American College of Radiology |

Five of them appear in the published corpus of 2,382 definitions: `GMTS` on 1,933, `OIDM` on 256, `CDE` on 115, `MGB` on 47, and `MSFT` on 31.

## Synonyms and near-synonyms

- **Source code** is the argument name in the identifier generator.
- **Namespace** and **prefix** are informal descriptions; the true prefix is `OIFM_` or `OIFMA_`.
- The code is not a provenance record of who did the work. It records which organization's namespace the identifier came from.

## Identifier form

Three or four uppercase letters, embedded as `OIFM_<CODE>_######` and `OIFMA_<CODE>_######`.

## Where it is used

[Identifiers](/semantic-foundation/finding-models/identifiers.md) and [Content catalog](/semantic-foundation/finding-models/content-catalog.md).

[^contributor-py]: OrganizationCodeField pattern
[^orgs]: Base organization registry
[^fm-py]: OIFM and OIFMA identifier generation
