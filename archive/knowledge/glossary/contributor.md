---
type: Glossary Term
title: Contributor
description: A person or organization credited on a finding model definition, recorded in a registry keyed by GitHub username or organization code.
tags: [glossary, semantic-foundation, finding-models]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: contributor-py
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/contributor.py
    title: Person and Organization models in the findingmodel package
  - id: orgs
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/data/base_organizations.jsonl
    title: Base organization registry in the findingmodel package
  - id: fm-schema
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/schema/finding_model_schema.md
    title: Finding model schema, prose mirror
---

# Contributor

A person or organization credited on a [finding model](/glossary/finding-model.md) definition. `contributors` is an optional list whose members are one of two types.[^fm-schema]

| Type | Required fields | Optional |
|---|---|---|
| Organization | `name` (at least 5 characters), `code` matching `^[A-Z]{3,4}$` | `url` |
| Person | `github_username`, `email`, `name`, `organization_code` | `url` |

Validation registers organizations by `code` and people by `github_username`. Both types support JSONL import and export.[^contributor-py] Seven organizations ship in the base registry: Microsoft, MassGeneral Brigham, Radiology Gamuts Ontology, the Radiological Society of North America, the American College of Radiology, the ACR/RSNA Common Data Elements Project, and the Open Imaging Data Model.[^orgs]

In the published corpus of 2,382 definitions, organization contributors appear on Gamuts-derived, OIDM-authored, and CDE-derived models, while MassGeneral Brigham and Microsoft contributions are credited to individual people carrying those organization codes.

## Synonyms and near-synonyms

- **Author** is used loosely in authoring tools; `contributors` is the field name.
- **[Organization code](/glossary/oidm-organization-code.md)** is the `code` on an organization and the `organization_code` on a person. It is also the middle segment of every OIFM identifier that organization mints.
- **Source** in a [finding taxonomy](/glossary/finding-taxonomy.md) row means the originating list, not a credited contributor.

## Identifier form

Organizations are keyed by a three or four letter uppercase code such as `MGB`. People are keyed by GitHub username.

## Where it is used

[Finding model format](/semantic-foundation/finding-models/finding-model-format.md) and [Authoring workflow](/semantic-foundation/finding-models/authoring-workflow.md).

## Conflicts

The `Person` type requires an email address, so contributor blocks in published definition files carry personal email addresses. This knowledgebase names organizations only and never reproduces those blocks.

[^contributor-py]: Person and Organization models in the findingmodel package
[^orgs]: Base organization registry
[^fm-schema]: Finding model schema, prose mirror
