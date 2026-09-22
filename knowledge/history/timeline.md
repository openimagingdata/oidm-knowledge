---
type: History
title: Timeline
description: Dated OIDM milestones from anatomic-location work in 2022 through current work in September 2026.
tags: [history, timeline]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: gh-org
    resource: https://github.com/openimagingdata
    title: Repository creation and push dates from the GitHub API, read 2026-09-21
  - id: rss
    resource: https://openimagingdata.org/rss/
    title: openimagingdata.org RSS feed, 15 posts, read 2026-09-21
  - id: old-repo-readme
    resource: https://github.com/openimagingdata/openimagingdata.org/blob/fb431dfc81801a5a8e621c0e8bf2acd20f74be7d/README.md
    title: openimagingdata.org repository README, still titled "Open Radiology Data Model"
  - id: benchmarking
    resource: https://www.openimagingdata.org/benchmarking-a-vision/
    title: Site post "Benchmarking a Vision", 2024-07-01, announcing the JAMIA manuscript
  - id: hackathon
    resource: https://www.openimagingdata.org/siim-2024-update-hackathon-edition/
    title: Site post "SIIM 2024 Update - Hackathon Edition", 2024-07-02
  - id: monorepo-pr
    resource: https://github.com/openimagingdata/findingmodel/pull/36
    title: findingmodel pull request 36, monorepo split into five packages, merged 2026-01-30
  - id: taxonomy-readme
    resource: https://github.com/openimagingdata/findingmodels/blob/a30c3c95fa3943e7340ce87575f4b1b926987eb8/lists/README.md
    title: findingmodels lists/README.md describing the MGB exam-oriented sub-taxonomies
  - id: radlex-issue-3
    resource: https://github.com/RSNA/RadLex/issues/3
    title: RSNA/RadLex issue 3, "Add Anatomic Locations", opened 2026-08-10
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026
---

# Prologue: 2022

Anatomic-location work began before OIDM. The TypeScript wrapper was created on 2022-02-02, the Python wrapper on 2022-07-19, and the curated dataset and site on 2022-12-14.[^gh-org] Version `1.0.0-rc.1` added a version field and SNOMED links in December 2022. The set reached 2,890 records. The last substantive site commit added a hierarchy tree view on 2023-01-10. See [the anatomic location lineage](/semantic-foundation/anatomic-locations/lineage-and-current-implementation.md).

# 2023: naming, schema, and the first demonstrations

| Date | Event |
|---|---|
| 2023-02-20 | The `openimagingdata.org` repository is created under the name **Open Radiology Data Model**, pointing at the domain `openraddata.org`.[^old-repo-readme] |
| 2023-02-21 to 2023-05-01 | The CDE Set and CDE Element JSON schema is drafted in that repository, followed by an Observation schema, sample Observations, and a written gap analysis between the schema and the RadElement API. |
| 2023-02-27 | `CDEStaging` is created as a staging area for rapidly drafted common data element definitions.[^gh-org] |
| 2023-04-27 | `OpenImagingDataModel.ts` is created, the first reference implementation. |
| 2023-05-31 | `CDETemplateDemo` is created, rendering a CDE-labeled Observation into report prose. See [CDE template rendering](/history/cde-template-rendering.md). |
| by 2023-06-21 | The public site's About page carries the name **Open Imaging Data Model**. The rename from Open Radiology Data Model therefore happened between February and June 2023; the old repository's README was never updated and still carries the old name.[^old-repo-readme] |
| 2023-06-24 | First site post, "Findings, CDEs, and Observations", which sets out the founding claim that a radiology finding is a FHIR Observation labeled with CDE codes.[^rss] |
| 2023-06-26 | "SIIM Update" reports an in-person meeting and a hackathon demonstration of a web service that turns a CDE-tagged FHIR Observation into customizable report prose. |
| 2023-06-27 | The site repository's CNAME is deleted in its last commit; the public site moves to a hosted blog at `openimagingdata.org`. |
| 2023-07-16 | "OIDM-Based Next-gen Reporting Assistance Framework" proposes a plugin container in which assistance scripts run against standardized report context. |
| 2023-08-14 | "How to Get Involved" lists the participation channels: site registration, meetings, a Slack channel, working groups, and demo projects. |
| 2023-09-07 | `UseCases` is created to collect application ideas. See [the use case catalog](/history/use-cases.md). |
| 2023-10-22 | Last commit on the TypeScript reference implementation's default branch. |
| 2023-12-30 | `SARTemplatesToCDEs` is created to convert Society of Abdominal Radiology templates into CDE sets. |

# 2024: SIIM, ontology linking, and the manuscript

| Date | Event |
|---|---|
| 2024-01-12 | "2024 New Year Update" reports an assisted-reporting framework demonstrated at RSNA by an industry collaborator, expansion of chest CT CDE content with the ACR and RSNA CDE committee, and plans for an open toolkit, anatomic location indexing through ACR Commons, and outcome tracking.[^rss] |
| 2024-01-25 | "Data Model: Structure and Function" describes OIDM as a superstructure on FHIR, comparable to how a browser's document object model relates to HTML, and names two utility libraries: anatomic locations, and an exam type library based on the LOINC and RSNA Playbook linked to anatomic locations. |
| 2024-01-29 | Meeting summary for the 2024-01-26 data model and library meeting: links to IHE and HL7, PACS and workflow applications, and whether the model is a protocol or a runtime. |
| 2024-02-26 | Last commit to `UseCases`. |
| 2024-03-08 | `OpenImagingDataModel.py` is created; its `observation.py` becomes the canonical FHIR Observation shape in the lineage. |
| 2024-03-11 | Last commit to `SARTemplatesToCDEs`, leaving a detailed itemized redesign of one CDE set as its most substantial artifact. |
| 2024-03-12 to 2024-03-13 | `FHIRSamples` is created and completed: a lung cancer screening DiagnosticReport with three chained CDE-coded Observations. |
| 2024-05-15 | "SIIM Hackathon Project" states the plan to link CDE sets automatically to SNOMED CT, RadLex, and Anatomic Locations using semantic search and foundation model embeddings. |
| 2024-06-05 | "SIIM In-Person Meeting" sets an agenda covering RadElement and MARVAL review procedures, chest CT CDE content feeding FHIR Observations, the TypeScript and Python libraries, and anatomic locations. |
| 2024-06-17 | "Counting Down to SIIM". |
| 2024-06-18 | "AI-Powered Chest CT Reporting" reports that a large language model generated more than 200 CDE definitions from anonymized chest CT reports, reviewed by radiologists and published to GitHub. |
| 2024-06-20 | "Attaching Ontology Links to Common Data Elements" describes automating what had been manual code selection across SNOMED CT, RadLex, and Anatomic Locations. |
| 2024-07-01 | "Benchmarking a Vision" announces a manuscript in the Journal of the American Medical Informatics Association, "Standardizing imaging findings representation: harnessing Common Data Elements semantics and Fast Healthcare Interoperability Resources structures", with a pulmonary nodule case study, arguing that CDE-labeled Observations should be the universal representation for radiology report content.[^benchmarking] |
| 2024-07-02 | "SIIM 2024 Update: Hackathon Edition" reports a working tool that associates ontology concepts with CDE set definitions across Anatomic Locations, RadLex, and SNOMED CT using six ranked search methods, and that it won the Audience Choice award.[^hackathon] |
| 2024-10-31 | `FindingModelForge` is created, the authoring application later deployed at `fmf.oidm.org`. |
| 2024-12-31 | `ReportFindingRefiner` is created, the most complete of the report-to-structure extraction pipelines. See [extraction approaches](/history/extraction-approaches.md). |

# 2025: finding models become the content spine

| Date | Event |
|---|---|
| 2025-02-21 | `common_data_elements` is created to hold a periodic snapshot of RadElement definitions and the CDE schema versions.[^gh-org] |
| 2025-03-02 | `ontology_tools` is created and never gets past a README naming three target ontologies. |
| 2025-03-10 | "Leveraging Common Data Elements (CDEs) to Enhance Radiology Reporting", a guest post from a reporting vendor, is the most recent post on the site.[^rss] |
| 2025-03-26 | `findingmodels` is created and the first finding model definitions are committed the same day. |
| 2025-03-27 | `get_ontology_findings` is created to match RadLex entries to imaging findings. |
| 2025-04-14 | `findingmodel` is created as the library for the Open Imaging Finding Model (OIFM) format. |
| 2025-05-23 | Last commit to `ReportFindingRefiner`. |
| 2025-06-05 | `template_extraction` is created; it accumulates a corpus of 281 RadReport templates. |
| 2025-06-19 | `finding-models-site` is created as a static catalog reader over the `findingmodels` corpus. |
| 2025-08-04 | `imaging-problem-list` is created. |
| 2025-08-22 to 2025-08-23 | The first Exam Finding List sample data is committed. |
| 2025-09-04 | The first Imaging Problem List is assembled from a separate report and Exam Finding List. |
| 2025-10-18 | `IPL-MVP-ExtractionAndLabeling` is created; by 2025-10-31 it has a four-stage extraction and mapping pipeline and three unmerged experiment branches. |
| 2025-11-13 | The first full worked example lands in `imaging-problem-list` along with a lightweight viewer. |
| 2025-11-18 | Last commit on the `imaging-problem-list` stable branch; `dev` continues from here. |
| 2025-11-25 | Last commit to `CDEStaging`. |

# 2026: monorepo, taxonomies, RadLex, and the next-generation vocabulary

| Date | Event |
|---|---|
| 2026-01 | The status deck **Open Imaging Data Model 2026 Status Update: Realizing Object-Oriented Imaging Results** sets out three strategic pillars, the Observation to Imaging Persona hierarchy, and a call for an ACR-hosted structured imaging results working group.[^deck] See [the extract](/references/status-update-2026-01.md). |
| 2026-01-02 | Last commit on the `FindingModelForge` `dev` branch, which remains unmerged.[^gh-org] |
| 2026-01-30 | `findingmodel` pull request 36 merges, splitting the library into five packages: `findingmodel`, `findingmodel-ai`, `anatomic-locations`, `oidm-common`, and `oidm-maintenance`.[^monorepo-pr] |
| 2026-03-04 | `findingmodel` `main` reaches its released state. |
| 2026-04-11 to 2026-06-29 | The canonical structured-metadata rewrite proceeds on `dev` and then `feature/metadata-cleanup`, adding eight optional metadata fields and a seven-agent assignment architecture. Neither branch has merged. |
| 2026-04-28 | `findingmodels` `main` reaches its current tip with 2,382 definitions. |
| 2026-06-02 to 2026-06-09 | RSNA creates the `RadLex` repository and adds the RadLex 4.3 OWL file. |
| 2026-06-10 | Anatomic-location coding of Exam Finding Lists and regrouping of the Imaging Problem List by finding code plus location complete on the `imaging-problem-list` `dev` branch. |
| 2026-07-22 | Current tip of `imaging-problem-list` `dev`, 258 commits ahead of the stable branch, now a full extraction, coding, persistence, and review platform. See [the report extraction platform](/applications/report-extraction-platform.md). |
| 2026-08-10 | RSNA/RadLex issue 3, "Add Anatomic Locations", is opened with the exit criterion of full coverage of the Anatomic Locations terminology in RadLex.[^radlex-issue-3] |
| 2026-08-15 | The `taxonomy-export-2026-08-15` branch replaces the legacy lists directory in `findingmodels` with six MGB exam-oriented sub-taxonomies, 3,789 rows, of which 1,028 already match an existing finding model identifier by exact name.[^taxonomy-readme] |
| 2026-08-16 to 2026-08-21 | `med-ontology-lookup` is created and published, providing terminology lookup across RadLex, SNOMED CT, FMA, LOINC, and UMLS. |
| 2026-08-21 | The `next-gen-2026` branch opens in the RSNA `ACR-RSNA-CDEs` repository with next-generation schema research notes in Open Knowledge Format. |
| 2026-09-02 to 2026-09-15 | Decisions S30 through S51 are recorded on that branch, covering anatomy families, scope corrections, and the split between prototype and integration work. |
| 2026-09-20 | Latest activity in `med-ontology-lookup`; typed provider failures merge and offline continuous integration remains uncommitted. |
| 2026-09-20 to 2026-09-21 | This knowledgebase is planned and begun. See [the build plan](/plans/2026-09-20-knowledgebase-build-plan.md). |

[^gh-org]: Repository creation and push dates from the GitHub API, read 2026-09-21
[^rss]: openimagingdata.org RSS feed, 15 posts, read 2026-09-21
[^old-repo-readme]: openimagingdata.org repository README, still titled "Open Radiology Data Model"
[^benchmarking]: "Benchmarking a Vision", 2024-07-01, announcing the JAMIA manuscript
[^hackathon]: "SIIM 2024 Update: Hackathon Edition", 2024-07-02
[^monorepo-pr]: findingmodel pull request 36, monorepo split into five packages, merged 2026-01-30
[^taxonomy-readme]: findingmodels lists/README.md describing the MGB exam-oriented sub-taxonomies
[^radlex-issue-3]: RSNA/RadLex issue 3, "Add Anatomic Locations", opened 2026-08-10
[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
