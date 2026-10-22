---
type: Glossary Term
title: OIDM
description: The Open Imaging Data Model, the project and the family of specifications it publishes for representing imaging exam results as structured data.
tags: [glossary, overview, oidm]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026
  - id: site
    resource: https://www.openimagingdata.org/
    title: openimagingdata.org, project site and tagline
  - id: old-name
    resource: https://github.com/openimagingdata/openimagingdata.org/blob/fb431dfc81801a5a8e621c0e8bf2acd20f74be7d/README.md
    title: openimagingdata.org repository README, carrying the superseded project name
  - id: orgs
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/data/base_organizations.jsonl
    title: Base organization registry in the findingmodel package
---

# OIDM

**Open Imaging Data Model (OIDM).** The open project that defines how the results of an imaging exam are represented as data rather than as prose, and the family of specifications, content catalogs, and tools it publishes. The project site states the purpose as "defining unified data structures to integrate new functionality into imaging informatics platforms."[^site] The January 2026 status deck calls the same ambition "standardizing the DNA of imaging IT" and organizes the work into three layers: a semantic foundation, a hierarchy of data structures, and applications built on them.[^deck]

OIDM is also a registered organization code in finding model content, where `OIDM` identifies the project itself as the contributing organization on a definition.[^orgs]

## Synonyms and near-synonyms

- **Open Radiology Data Model** is the superseded name of the same project, still visible in the old site repository README and its former domain.[^old-name] It appears in this knowledgebase only in [history](/history/).
- **openimagingdata** is the GitHub organization that holds most OIDM repositories. It names the organization, not the data model.
- **OIFM** is not a synonym. [OIFM](/glossary/oifm.md) is one specification inside OIDM, covering finding model definitions.

## Identifier form

None as a term. As an [organization code](/glossary/oidm-organization-code.md) it is the four-letter segment `OIDM` in identifiers such as `OIFM_OIDM_371000`.

## Where it is used

[What is OIDM](/overview/what-is-oidm.md) gives the orientation, [Vision](/overview/vision.md) the rationale, and [Architecture](/overview/architecture.md) the way the layers fit. [The repository map](/repositories/repository-map.md) lists every repository that carries OIDM work.

[^site]: openimagingdata.org, project site and tagline
[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
[^old-name]: openimagingdata.org repository README
[^orgs]: Base organization registry in the findingmodel package
