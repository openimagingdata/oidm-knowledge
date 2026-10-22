---
type: Overview
title: What is OIDM
description: The mission of the Open Imaging Data Model, the problem it addresses, its three layers, who it serves, and where its work lives.
tags: [overview, orientation]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:34:50Z }
sources:
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026
  - id: site-about
    resource: https://www.openimagingdata.org/
    title: openimagingdata.org, project site and tagline
  - id: site-findings
    resource: https://www.openimagingdata.org/findings-cdes-and-observations/
    title: "Findings, CDEs, and Observations, 2023-06-24"
  - id: ipl-readme
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/README.md
    title: imaging-problem-list README on the dev branch
  - id: fm-schema
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/schema/finding_model_schema.md
    title: Finding model schema, prose mirror, findingmodels repository
---

# What OIDM is

The [Open Imaging Data Model (OIDM)](/glossary/oidm.md) is an open project that represents imaging exam results as structured data. The project site describes its purpose as "defining unified data structures to integrate new functionality into imaging informatics platforms."[^site-about] The January 2026 status deck calls this standardizing "the DNA of imaging IT."[^deck]

OIDM provides a controlled vocabulary, data structures, and tools that produce and consume them. Stable identifiers connect findings and their attributes across individual [observations](/glossary/observation.md) and longitudinal patient records. The tools apply the vocabulary and structures to real reports.

# The problem: results locked in narrative

Imaging reports are usually narrative text. To determine whether a pulmonary nodule was present on the latest chest CT, how large it was, or whether it grew, downstream systems must interpret that text. Each system interprets it differently.

Radiologists reconstruct finding histories from old reports because prior findings cannot be retrieved reliably. Recommendations cannot be tracked to completion. Quality metrics and registry submissions require manual abstraction. Artificial intelligence tools and radiologists express findings differently, preventing comparison. Vendors address these problems with private schemas that other systems cannot reuse.

OIDM gives each finding a coded identity, location, and attributes in a queryable structure. The 2023 site post states the approach: "Radiology findings can be represented in a standard format based on FHIR Observations semantically labeled with ACR/RSNA Common Data Element identifiers."[^site-findings]

# Three layers

The project and this knowledgebase organize the work into three layers.

**Semantic foundation.** [Finding models](/glossary/finding-model.md) define findings with descriptions, synonyms, and attributes. Each has an [Open Imaging Finding Model (OIFM)](/glossary/oifm.md) identifier.[^fm-schema] The layer also includes [anatomic locations](/glossary/anatomic-location.md) keyed by RadLex identifiers, [common data elements](/glossary/cde.md) published through RadElement, [exam types](/glossary/exam-type.md), and external terminologies. See [semantic-foundation](/semantic-foundation/).

**Data structures.** An [Observation](/glossary/observation.md) records one finding in one exam, with its location and attribute values. An [Exam Finding List](/glossary/exam-finding-list.md) collects an exam's observations in one queryable structure.[^ipl-readme] An [Imaging Problem List](/glossary/imaging-problem-list.md) groups observations across a patient's exams by finding. An [Imaging Persona](/glossary/imaging-persona.md) is the stated goal of adding clinical context. See [data-structures](/data-structures/).

**Applications.** Tools include a finding model authoring application, a catalog site, an Imaging Problem List viewer, a report extraction and coding platform, and a terminology lookup library. See [applications](/applications/).

Each layer depends on the one below it through shared identifiers. [Architecture](/overview/architecture.md) explains those connections. [Vision](/overview/vision.md) explains the design rationale.

# Who this is for

- Developers building imaging informatics software need formats and libraries to read and write them.
- Informaticists need to understand finding models, their relationship to common data elements, and identifiers for anatomic structures.
- Standards bodies and committees evaluate vocabulary and data structures for formal standardization.
- Agents extract, code, or author content. This knowledgebase is an Open Knowledge Format bundle with machine-readable frontmatter to support that work.

# Where things live

OIDM spans repositories in the `openimagingdata` GitHub organization and allied projects. Several repositories keep current work on branches other than `main`. [The repository map](/repositories/repository-map.md) lists their roles, status, and branches of record.

It describes and links to catalogs; it does not copy them. Installation instructions, API usage, and developer workflows stay with the code.

# Getting involved

See [Getting involved](/overview/getting-involved.md) for participation channels, repositories, issues, and content contributions. See [the authoring guide](/guides/authoring-guide.md) for knowledgebase conventions.

[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
[^site-about]: openimagingdata.org, project site and tagline
[^site-findings]: "Findings, CDEs, and Observations", 2023-06-24
[^ipl-readme]: imaging-problem-list README on the dev branch
[^fm-schema]: Finding model schema, prose mirror, findingmodels repository
