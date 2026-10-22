---
type: Reference
title: Use case catalog
description: The roughly 25 ideas from UseCases, with source attribution and six value-category tags.
tags: [history, use-cases, reference]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: usecases-index
    resource: https://github.com/openimagingdata/UseCases/blob/71a90d2ab2efeee4c4303dc0aef27ed3d70a6c99/Index.md
    title: UseCases Index.md, the living list of use case ideas
  - id: usecases-readme
    resource: https://github.com/openimagingdata/UseCases/blob/71a90d2ab2efeee4c4303dc0aef27ed3d70a6c99/README.md
    title: UseCases README.md, the intended process and the six value categories
---

# What this is

The `UseCases` repository began in September 2023 to collect Open Imaging Data Model (OIDM) application ideas. Each index entry had a name and one-sentence description, with mature ideas intended to become separate files.[^usecases-index] None did. The last commit was 2024-02-26. This catalog reorganizes all entries without additions.

Entries marked as contributed by the RSNA Reporting Informatics Committee are so marked in the source. The numbers after each entry are the value categories defined in the next section, exactly as the source assigns them. Four of the repository's seven headings, Protocoling System, AI Pipeline, PACS Viewing, and Data Exploration, are placeholders with no entries.

# Value categories

Six categories, taken from the RSNA Reporting Informatics Committee's use case work, are used to tag each entry.[^usecases-readme]

| ID | Value category | Such as |
|---|---|---|
| 1 | Reporting efficiency | Pre-populating reports with relevant data |
| 2 | Care team communication | Disease-specific contextual information, reports, or macros; clinical decision support for referring physicians and specialists |
| 3 | Operations, quality, and safety | Business intelligence; revenue cycle; critical findings communication; error prevention; follow-up recommendation tracking; outcomes tracking for quality assurance, quality improvement, and continuing education |
| 4 | Research | Registries |
| 5 | Public health | Disease prevalence in a population; benchmarking diagnostic performance of imaging tests at population level |
| 6 | Education | Teaching file generation; pathology-specific report macros as teaching tools for trainees and for physicians who see a given pathology rarely |

# Workflow and worklist

- **Applying prior DEXA scan data.** Levels excluded on a prior bone density study are excluded automatically on the current study, and the reason is passed downstream to the dictation software.

# Assisted reporting

Most entries came from the RSNA Reporting Informatics Committee, as marked below.

- **Stroke notification** (RSNA Reporting Informatics Committee). Automated communication to the stroke team when findings of stroke are reported. (2, 3)
- **Problem list update** (RSNA Reporting Informatics Committee). Findings in a radiology report automatically update the electronic medical record problem list. (3)
- **ACR GRID registry population.** Findings in a report automatically populate registry fields. (1, 3)
- **Public health infectious disease database** (RSNA Reporting Informatics Committee). Report impressions combine with other record data to populate a public health database. (1, 5)
- **Testicular torsion notification.** Automated communication to the urology team when findings of testicular torsion are reported. (2, 3)
- **Prior comparison and problem list retrieval** (RSNA Reporting Informatics Committee). Findings from prior reports, including incidentals, are compiled for the reporting radiologist to review while dictating. (1, 2, 3)
- **Deep vein thrombosis and pulmonary embolism messaging** (RSNA Reporting Informatics Committee). A message to the primary care team to order anticoagulation when those findings are reported. (2, 3)
- **Follow-up manager** (RSNA Reporting Informatics Committee). Automated compilation of incidental-finding follow-up recommendations from impression or recommendation sections, with reminders to ordering physicians, and optional retrieval of prior recommendations to check whether the follow-up study was performed and what it showed. (2, 3)
- **Report summary and action list** (RSNA Reporting Informatics Committee). A list of actionable items to guide the ordering team on next steps for acute and incidental findings. (2, 3)
- **Organ and body part auto-update** (RSNA Reporting Informatics Committee). The report updates automatically for post-surgical or congenitally absent organs based on the medical record. (1, 3)
- **Practice guideline template manager** (RSNA Reporting Informatics Committee). A template manager for the common reporting systems such as BI-RADS, TI-RADS, LI-RADS, and CAD-RADS, optionally with lay-language translation of categories and accompanying CDE sets to make the guidance machine readable. (1, 2, 3, 4)
- **Reason for exam standardization** (RSNA Reporting Informatics Committee). Standardizing the reason for exam, ideally automatically, and encoding it as machine-readable metadata. (1, 3, 4, 5, 6)
- **Reason for exam, detailed** (RSNA Reporting Informatics Committee). Capturing the specific clinical question a referring specialist needs answered, alongside the short reason-for-exam field, since a character-limited field cannot hold it. (2, 3)
- **Export to a research database** (RSNA Reporting Informatics Committee). Primary findings and numeric measurements exported as structured coded data, for instance tracking the same lymph node over time into an OMOP database, or tumor measurements during treatment. (3, 4, 5)
- **Implanted devices** (RSNA Reporting Informatics Committee). Automatic population of implanted devices, intentional and unintentional, for pre-procedure screening, protocolling, and reporting, allowing reconciliation of unexpected or missing items. (1, 2, 3)

# Uncategorized

These entries carry no value category tags in the source.

- **Spine numbering with transitional anatomy.** Reference prior labeling automatically, or produce a report with alternative numbering according to a surgeon's preference, and feed surgical reports back as confirmation.
- **Comparison case retrieval.** For findings with highly variable appearance such as renal cell carcinoma or melanoma, retrieve similar prior cases from the terms being dictated, ideally across sites, to support the reader and to teach trainees.
- **Aortic measurement auto-population.** Populate current and prior thoracic and abdominal aortic measurements and classify interval change and caliber without manual steps.
- **Teaching file and case search.** Trainee teaching files, case search, and literature search.
- **Biopsy and scan follow-up tracking.**
- **SWIM initiative tie-in.**
- **Dictation dictionary population.** Populate a reporting system's findings-mode dictionary.
- **Surgical, imaging, and pathology correlation.** Automate what is now manual comparison of imaging reports against operative notes, and surface discordant cases for feedback.
- **Laterality and body part order reconciliation.** Flag orders whose laterality or body part contradicts the progress note before the study reaches the radiologist.
- **Cross-reference laboratory data.** Use record data to support an imaging inference, for example checking recent hemoglobin when non-contrast chest CT shows blood pool less dense than myocardium.

# How the catalog was meant to work

The unfinished process was to collect ideas, define metadata for mature cases, and store them in hierarchical Markdown or JSON files.[^usecases-readme] The README leaves three questions open: what information to capture, whether to use prose or data, and whether coded inputs such as laboratory LOINC codes are needed.

The categories the README proposes for organizing cases are workflow and list oriented, AI pipeline oriented, reporting oriented, image-viewer oriented, data exploration and outcome oriented, multi-category, and miscellaneous. The index uses a slightly different set of headings, listed above.

[The 2026 roadmap](/roadmap/roadmap-2026.md) describes related applications and use-case submissions to the CDE group without reusing this catalog.

[^usecases-index]: UseCases Index.md, the living list of use case ideas
[^usecases-readme]: UseCases README.md, the intended process and the six value categories
