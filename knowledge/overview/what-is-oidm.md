---
type: Overview
title: What is OIDM
description: The mission of the Open Imaging Data Model, the problem it addresses, its three layers, who it serves, and where its work lives.
tags: [overview, orientation]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T15:00:00Z }
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

The [Open Imaging Data Model (OIDM)](/glossary/oidm.md) is an open project that defines how the results of an imaging exam are represented as data rather than as prose. Its stated purpose, in the words of the project site, is "defining unified data structures to integrate new functionality into imaging informatics platforms."[^site-about] The January 2026 status deck puts the same ambition more bluntly: standardizing "the DNA of imaging IT."[^deck]

Concretely, OIDM supplies three things. It supplies a controlled vocabulary of imaging findings and the attributes that characterize them, each carrying a stable identifier. It supplies a small hierarchy of data structures that carry those findings from a single [observation](/glossary/observation.md) up to a longitudinal view of one patient. And it supplies working tools that produce and consume those structures, so that the vocabulary and the structures are exercised against real reports rather than only specified.

# The problem: results locked in narrative

An imaging report is the product of the exam, and it is almost always a block of narrative text. That text is readable by a clinician and opaque to everything else. A downstream system that wants to know whether a pulmonary nodule was present on the most recent chest CT, how large it was, and whether it grew, has to re-read the prose every time, and each system re-reads it differently.

The consequences compound across the imaging life cycle. Prior findings cannot be retrieved reliably at interpretation time, so radiologists reconstruct history by reading old reports. Recommendations made in a report cannot be tracked to completion. Quality metrics and registry submissions require manual abstraction. Findings produced by artificial intelligence tools and findings produced by radiologists cannot be compared, because they are not expressed in the same terms. Each vendor that solves part of this solves it privately, in its own schema, which means the solution does not travel.

OIDM's response is to make the finding, not the report, the unit of data. A finding gets a coded identity, a coded location, coded attributes, and a place in a structure that other systems can query. The 2023 site post that set the direction states it as: "Radiology findings can be represented in a standard format based on FHIR Observations semantically labeled with ACR/RSNA Common Data Element identifiers."[^site-findings]

# Three layers

The project organizes its work into three layers, and this knowledgebase follows that organization.

**Semantic foundation.** The vocabulary layer. It holds [finding models](/glossary/finding-model.md), each a named finding with a description, synonyms, and a list of attributes, identified by an [Open Imaging Finding Model (OIFM)](/glossary/oifm.md) identifier.[^fm-schema] It holds [anatomic locations](/glossary/anatomic-location.md) keyed by RadLex identifiers, [common data elements](/glossary/cde.md) published through RadElement, [exam types](/glossary/exam-type.md), and the external terminologies all of these draw on. See [semantic-foundation](/semantic-foundation/).

**Data structures.** The container layer. An [Observation](/glossary/observation.md) is one finding in one exam, with its location and attribute values. An [Exam Finding List](/glossary/exam-finding-list.md) is every observation from one exam in one queryable structure.[^ipl-readme] An [Imaging Problem List](/glossary/imaging-problem-list.md) reorganizes observations across a patient's exams by finding rather than by date. An [Imaging Persona](/glossary/imaging-persona.md) is the stated goal of surrounding that with clinical context. See [data-structures](/data-structures/).

**Applications.** The tools that make the first two layers real: an authoring application for finding models, a catalog site, a viewer for Imaging Problem Lists, a report extraction and coding platform, and a terminology lookup library. See [applications](/applications/).

Each layer depends on the one below it, and the identifiers are what join them. How the layers and identifier systems connect is laid out in [Architecture](/overview/architecture.md), and the reasoning behind the whole design in [Vision](/overview/vision.md).

# Who this is for

- **Developers** building imaging informatics software who need formats to read and write, and libraries that already speak them.
- **Informaticists** who need to know what a finding model is, how it relates to a common data element, and what identifier to use for an anatomic structure.
- **Standards bodies and committees** evaluating the vocabulary and data structures, and deciding what should graduate into formal standards.
- **Agents** doing extraction, coding, or authoring work, which is why this knowledgebase is an Open Knowledge Format bundle with machine-readable frontmatter on every document.

# Where things live

The work is spread across repositories in the `openimagingdata` GitHub organization plus several allied external projects. Content, code, specifications, and in-flight work do not all live in the same place, and several repositories have their current state on a branch other than `main`. [The repository map](/repositories/repository-map.md) lists every source repository, its role, its status, and its branch of record.

This knowledgebase is the high-level documentation. It describes and links to catalogs; it does not copy them. Installation instructions, API usage, and developer workflow stay with the code.

# Getting involved

Participation channels, the repositories to start with, how to file issues, and how content is contributed are covered in [Getting involved](/overview/getting-involved.md). Conventions for editing this knowledgebase itself are in [the authoring guide](/guides/authoring-guide.md).

[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
[^site-about]: openimagingdata.org, project site and tagline
[^site-findings]: "Findings, CDEs, and Observations", 2023-06-24
[^ipl-readme]: imaging-problem-list README on the dev branch
[^fm-schema]: Finding model schema, prose mirror, findingmodels repository
