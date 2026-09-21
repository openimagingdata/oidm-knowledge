---
type: Reference
title: Site articles
description: The fifteen posts published on openimagingdata.org between June 2023 and March 2025, plus the About page, each dated, linked, and summarized.
tags: [history, site, articles, reference]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T02:00:00Z }
sources:
  - id: rss
    resource: https://openimagingdata.org/rss/
    title: openimagingdata.org RSS feed, 15 posts, fetched 2026-09-21
  - id: about
    resource: https://www.openimagingdata.org/about/
    title: openimagingdata.org About page, fetched 2026-09-21
---

# What the site is

`openimagingdata.org` is the project's public site, a hosted blog whose title is "Open Imaging Data Model" and whose tagline is "Defining unified data structures to integrate new functionality into imaging informatics platforms." It carries two static pages, Home and About, and fifteen posts running from 2023-06-24 to 2025-03-10.[^rss] Every date and summary below was verified against the live page on 2026-09-21. Individual authors are not named here, per the conventions in [the authoring guide](/guides/authoring-guide.md).

The site replaced the earlier repository-hosted site in June 2023; see [lineage repositories](/history/lineage-repositories.md).

# Posts, newest first

## 2025-03-10, [Leveraging Common Data Elements (CDEs) to Enhance Radiology Reporting](https://www.openimagingdata.org/leveraging-common-data-elements-cdes-to-enhance-radiology-reporting/)

A guest post from a reporting software vendor arguing that standardized data points improve clinical decision-making and data quality in radiology reporting. It describes integrating CDEs with radiology information systems and PACS while adhering to HL7, FHIR, and FHIRcast. The stated payoff is efficiency, advanced analytics, and better outcomes from structured data. This is the most recent post on the site.

## 2024-07-02, [SIIM 2024 Update: Hackathon Edition](https://www.openimagingdata.org/siim-2024-update-hackathon-edition/)

Reports the completed hackathon tool, which automatically associates concepts from common ontologies with CDE set definitions using full-text and semantic search across Anatomic Locations, RadLex, and SNOMED CT. The demonstration included a working front end that searched all three simultaneously and returned results ranked by six different search methods. The project was not selected by the judges but won the Audience Choice award.

## 2024-07-01, [Benchmarking a Vision](https://www.openimagingdata.org/benchmarking-a-vision/)

Announces a manuscript in the Journal of the American Medical Informatics Association titled "Standardizing imaging findings representation: harnessing Common Data Elements semantics and Fast Healthcare Interoperability Resources structures." The paper presents the framework for representing findings as CDE-labeled FHIR Observations, with a pulmonary nodule case study. Its claim, quoted in the post, is that CDE-labeled Observations should be the universal representation for exchanging and consuming radiology report content.

## 2024-06-20, [Attaching Ontology Links to Common Data Elements](https://www.openimagingdata.org/attaching-ontology-links-to-common-data-elements/)

Describes the problem the hackathon set out to solve: matching CDEs to ontology codes in SNOMED CT, RadLex, and Anatomic Locations was being done by hand. The plan was to curate representative examples and train a tool to reproduce the selection automatically. No results are presented; the post invites feedback at the upcoming demonstration.

## 2024-06-18, [AI-Powered Chest CT Reporting: Transforming Radiologist Observations into Standardized Data](https://www.openimagingdata.org/creating-common-data-elements-for-chest-cts-how-ai-is-revolutionizing-radiology-reporting/)

Reports using a large language model to generate common data element definitions from anonymized chest CT reports, by converting report text into semantic vectors, ranking relevant sections, and having radiologists review the generated definitions. More than 200 CDE definitions came out of the pilot. They were published to GitHub for community review, which is the origin of the chest CT content later carried in `CDEStaging`.

## 2024-06-17, [Counting Down to SIIM](https://www.openimagingdata.org/counting-down-to-siim/)

A short lead-up post promising daily updates before the conference. It previews three topics: making CDEs at scale, a demonstration tool for creating FHIR Observations, and a hackathon project associating CDEs with RadLex and SNOMED CT concepts.

## 2024-06-05, [SIIM In-Person Meeting](https://www.openimagingdata.org/siim-in-person-meeting/)

Sets the agenda for an in-person meeting at SIIM on 2024-06-28. Topics include updates on the CDE committee's RadElement and MARVAL sites and their review procedures, chest CT CDE content feeding FHIR Observations, the TypeScript and Python libraries, and progress on anatomic locations. The group also planned to take part in the hackathon project linking CDEs to SNOMED CT, RadLex, and Anatomic Locations.

## 2024-05-15, [SIIM Hackathon Project](https://www.openimagingdata.org/siim-hackathon-project/)

States the hackathon plan: add connections between CDE sets and important ontologies, specifically SNOMED CT, RadLex, and Anatomic Locations, automatically or at least semi-automatically. The method was semantic search over foundation-model vector representations, with Python and TypeScript tools proposing candidate links for language models to assess and experts to review. The argument is that richer interconnection strengthens CDE adoption and clinical information exchange.

## 2024-01-29, [OIDM Data Model/Library Meeting Summary 2024-01-26](https://www.openimagingdata.org/oidm-data-model-library/)

A summary of the 2024-01-26 meeting, covering how imaging data standards connect with IHE and HL7 protocols and how the model would be applied in PACS viewers and workflow managers. Participants debated whether the model should function as a protocol or as a microservices runtime, and discussed event hooks and AI findings metadata alongside DICOM resources. The next step named was working through clinical report examples and encoding their findings as CDE-labeled FHIR Observations.

## 2024-01-25, [Data Model: Structure and Function](https://www.openimagingdata.org/data-model-structure-and-function/)

The clearest statement of what OIDM is structurally. It describes the model as covering the whole reporting context, observations, patient data, imaging studies, and clinical history, and says the model makes extensive use of FHIR definitions while providing a superstructure on top for easier programmatic access, comparing that relationship to how a browser's document object model relates to HTML. It names two utility libraries: anatomic locations for standardized body part terminology, and an exam type library based on the LOINC and RSNA Playbook linked to anatomic locations. That exam type library has never been built; see [exam types](/semantic-foundation/exam-types/overview.md).

## 2024-01-12, [2024 New Year Update](https://www.openimagingdata.org/2024-new-year-update/)

Reports an assisted reporting framework incorporating AI demonstrated at RSNA by an industry collaborator, and expansion of chest CT common data element content in collaboration with the ACR and RSNA CDE committee. It states plans for an open-standard toolkit for assisted reporting systems, introducing anatomic location indexing through ACR Commons, and new applications for outcome tracking and integration with electronic health records and PACS.

## 2023-08-14, [How to Get Involved](https://www.openimagingdata.org/how-to-get-involved/)

Lists six engagement channels: registering on the site for newsletters and comments, joining meetings, joining the project's channel in a Slack workspace, participating in working groups on use cases and standards, contributing to demonstration projects, and helping identify related initiatives. It also gives a direct contact address. See [getting involved](/overview/getting-involved.md) for current channels.

## 2023-07-16, [OIDM-Based Next-gen Reporting Assistance Framework](https://www.openimagingdata.org/oidm-based-next-gen-reporting-assistance/)

Proposes a plugin architecture in which developers write assistance scripts that run inside a reporting tool's container. A script reads standardized data structures holding the report context, and can insert generated text into the report, ask the radiologist for more information, alert the radiologist to a problem, or send data to an external system. The container re-runs the scripts whenever the report context changes, which makes the assistance continuous rather than one-shot. This is the earliest statement of the direction later named the reporting SDK; see [the reporting SDK](/applications/reporting-sdk.md).

## 2023-06-26, [SIIM Update](https://www.openimagingdata.org/siim-update/)

Announces the site itself and summarizes an in-person SIIM meeting on cooperation with other initiatives and roadmap planning. It reports a hackathon demonstration of a web service that takes a radiology finding encoded as a FHIR Observation with CDE tags and generates customizable prose, with sample templates in the project's GitHub repository. That demonstration is `CDETemplateDemo`; see [CDE template rendering](/history/cde-template-rendering.md). Organizations named include IHE, HIMSS and SIIM, the ACR Data Science Institute, and an industry collaborator.

## 2023-06-24, [Findings, CDEs, and Observations](https://www.openimagingdata.org/findings-cdes-and-observations/)

The founding post. It argues that a radiology finding can be standardized as a FHIR Observation labeled with ACR and RSNA common data element identifiers: the Observation's code carries the CDE set identifier naming the finding type, and each attribute becomes a component carrying a CDE element identifier and a value. Its worked example is a solid 6 mm nodule in the right lower lobe, labeled with the pulmonary nodule CDE set code and element codes for composition and size. Everything in [the data structures layer](/data-structures/hierarchy.md) descends from this claim.

# The About page

The About page states the mission: establish common data structures representing the data associated with clinical radiology exams, so that a standard framework for third-party apps can be developed and integrated into imaging informatics tools such as reporting software, PACS viewers, worklist managers, and data exploration systems.[^about] It defines the project's focus as radiology reports describing findings, diagnoses, and recommendations, with individual findings represented as CDE-labeled FHIR Observation objects, and extends the scope beyond findings to the whole data context: report metadata, report text, prior reports, and electronic medical record information.

It also commits to programming interfaces in three languages, TypeScript and JavaScript, Python, and C#. Two of the three exist as lineage repositories and neither is current; no C# library was ever created. See [lineage repositories](/history/lineage-repositories.md).

The page was last modified 2023-06-21 and has not been revised since, so it predates finding models, the Exam Finding List, and the Imaging Problem List. Where it differs from current documents, the current documents govern.

[^rss]: openimagingdata.org RSS feed, 15 posts, fetched 2026-09-21
[^about]: openimagingdata.org About page, fetched 2026-09-21
