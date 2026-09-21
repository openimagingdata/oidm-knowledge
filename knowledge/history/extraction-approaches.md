---
type: History
title: Extraction approaches
description: Seven successive attempts at turning radiology report text into structured findings, from a template corpus in 2024 to the current extraction platform, and what each one established.
tags: [history, extraction, llm, findings]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T02:00:00Z }
sources:
  - id: template-extraction
    resource: https://github.com/openimagingdata/template_extraction/tree/4d947d7e7557ce6187a35d592f8199d3abb673cf/templates
    title: template_extraction, a corpus of 281 RadReport templates
  - id: sar
    resource: https://github.com/openimagingdata/SARTemplatesToCDEs/blob/3c15322eb1e0ba211558444207f56d8cd1b08c30/README.md
    title: SARTemplatesToCDEs README, the template to CDE set conversion goal
  - id: refiner
    resource: https://github.com/openimagingdata/ReportFindingRefiner/blob/3efd785aea30c455a3afd120d62da2c6af3d662d/README.md
    title: ReportFindingRefiner README, the retrieval-augmented extraction architecture
  - id: get-ontology
    resource: https://github.com/openimagingdata/get_ontology_findings/blob/574ec5e0afac2f4fbb97b4b68b6cf075337782cb/README.md
    title: get_ontology_findings README
  - id: cde-process
    resource: https://github.com/openimagingdata/CDEStaging/blob/b814a102655054ac08b3c118cb1977a387655a8b/docs/report_extraction_process.md
    title: CDEStaging docs/report_extraction_process.md, manual report extraction worked example
  - id: cde-negatives
    resource: https://github.com/openimagingdata/CDEStaging/blob/b814a102655054ac08b3c118cb1977a387655a8b/report_representation/negative_statements.md
    title: CDEStaging report_representation/negative_statements.md
  - id: cde-uncovered
    resource: https://github.com/openimagingdata/CDEStaging/blob/b814a102655054ac08b3c118cb1977a387655a8b/report_representation/uncovered_findings.md
    title: CDEStaging report_representation/uncovered_findings.md
  - id: mvp
    resource: https://github.com/openimagingdata/IPL-MVP-ExtractionAndLabeling/blob/b06948fa417aeff0a6a4b97729c915b3ce5d5ed4/README.md
    title: IPL-MVP-ExtractionAndLabeling README, the four-stage pipeline
  - id: ipl-initial-plan
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/initial-extraction-plan.md
    title: imaging-problem-list initial-extraction-plan.md on dev, the extraction schema
  - id: ipl-validator
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/prompts/validator_prompt_example.md
    title: imaging-problem-list validator prompt example on dev
  - id: ipl-evals
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/extractor-evals-redesign.md
    title: imaging-problem-list docs/plans/extractor-evals-redesign.md on dev
---

# The problem, restated each time

Every one of these efforts answers the same question: given free-text radiology report language, produce structured findings that carry standard codes. They differ in what they start from, what they produce, and how they judge whether the result is right. Read in order, they converge on three conclusions that the current platform treats as settled: extraction must work on real report prose rather than templates, it must produce explicit negatives as well as positives, and it must be judged on faithfulness to the source text rather than on how many findings it emits.

# 1. Templates as the source, 2024 to 2025

**SARTemplatesToCDEs** (2023-12 to 2024-03) proposed using a language model to convert Society of Abdominal Radiology reporting templates into CDE sets, starting with rectal cancer staging.[^sar] No conversion code was committed. Its lasting artifact is a hand-written itemized redesign of one CDE set; see [lineage repositories](/history/lineage-repositories.md).

**template_extraction** (2025-06) took the same starting point at scale, accumulating 281 RadReport templates spanning CT, MR, ultrasound, nuclear medicine, and fluoroscopy across neuro, musculoskeletal, chest, abdomen, genitourinary, and cardiac imaging, plus oncology staging templates and two CDE-labeled test templates.[^template-extraction] The script that reads them is short. The corpus is the asset, and it remains unused: it is a candidate vocabulary for [exam types](/semantic-foundation/exam-types/overview.md) as much as for findings, since the templates are named by exam.

What this line established: templates give you the vocabulary a specialty society has agreed on, but not the language radiologists actually dictate, and not the negatives.

# 2. Ontologies as the source, 2025

**get_ontology_findings** (2025-03) inverted the direction: look through an existing ontology for entries that correspond to imaging findings, so they can be turned into finding models or common data elements.[^get-ontology] It carries a RadLex export and a minimal script. Its narrow single-ontology scope was widened by `med-ontology-lookup`; see [that project profile](/semantic-foundation/terminologies/med-ontology-lookup.md).

What this line established: an ontology tells you what a finding could be called, not which findings are worth modeling or how they are characterized.

# 3. Real report text, retrieval-augmented, 2024 to 2025

**ReportFindingRefiner** (2024-12 to 2025-05) is the first pipeline built on real report prose.[^refiner] Its architecture is a privacy-first, locally hosted chain: ingest plain-text reports, split each into header, findings, and impression sections, embed the sections with sentence transformers, store them in a local vector database, expose basic, vector, and hybrid search over them, then use a locally run language model to generate a finding model outline from retrieved context and persist it. It separates a search service, a report service, a language model service, and a finding model service, and exposes each step as its own command-line script, including one that generates a finding outline with retrieved context and one without, so the two can be compared.

What this line established: retrieval over a real corpus produces better finding definitions than a template does, local models make report text usable without sending it anywhere, and generating a definition is a different task from extracting an instance.

# 4. Manual extraction as a specification, 2024 to 2025

`CDEStaging` approached extraction by doing it by hand and writing down what broke. Its process document works a chest CT pulmonary angiogram report into a list of what it calls mini-observations, each a finding name with attribute and value lines.[^cde-process] The worked example is short enough to quote:

```markdown
- pulmonary embolism
  - presence: absent
- pulmonary consolidation
  - presence: present
  - location: right lower lobe
- atelectasis
  - presence: present
  - type: linear
  - location: right upper lobe
- pleural effusion
  - presence: present
  - side: right
- pleural effusion
  - presence: absent
  - side: left
```

Two observations in that document set the agenda for everything after it. Finding, attribute, and value names have to match the project's own finding definitions, or the extraction is not interoperable. And blanket negative statements such as "Lungs are clear" need their own catalog, because they assert many findings absent in one phrase.

Three companion files hold the results of that cataloging work. `negative_statements.md` collects composite and negative report statements by organ system. `uncovered_findings.md` lists findings pulled out of reports with no matching definition, a standing gap log.[^cde-uncovered] `missing_attributes.md` collects report phrases whose attributes existing definitions cannot capture.[^cde-negatives] Fifty-seven worked structured extractions sit alongside them. The two branches that carried most of this work, a report-representation branch of 37 commits and a content branch of 33, were never merged; see the work edge section of [the repository map](/repositories/repository-map.md).

What this line established: the hard part is not parsing, it is the vocabulary gap and the treatment of negation. Both are still open; the extraction platform's own validator prompt names "incorrect representation of a blanket negative" as a re-extraction trigger.

# 5. Embedding similarity, 2025

**IPL-MVP-ExtractionAndLabeling** (2025-10) is the first end-to-end run at the Imaging Problem List goal.[^mvp] Four stages, all local Python:

| Stage | What it does |
|---|---|
| `step1_extract.py` | A language model extracts findings from each report as name and presence pairs |
| `step0_review_extracted.py` | A human reviews stage one output |
| `step2_map.py` | Each extracted finding is embedded and matched by cosine similarity against 15 curated neuro finding models, with a configurable threshold of 0.70 |
| `step3_review_mappings.py` | Produces a human-readable mapping summary |

Its output schema is deliberately thin: a finding is a name and a boolean presence; a mapping adds the matched finding model identifier, a confidence score, and a status. It produces neither an [Exam Finding List](/data-structures/exam-finding-list.md) nor an [Imaging Problem List](/data-structures/imaging-problem-list.md), and no FHIR output; the README lists FHIR Observation generation as a future enhancement. Evaluation was informal: 8 sample reports, 87 extracted findings, 5 matched above threshold, 82 flagged for manual review.

Three single-commit branches pushed in one week extend it without merging: a longitudinal multiple sclerosis report series, a port of the extraction step to a typed agent framework, and a design note proposing persistent FHIR Observations with stable identifiers, so that repeat mentions of the same lesion across reports attach to one tracked entity with its own timeline. That note adds no code and names two modules that were never written. See [the project profile](/applications/ipl-mvp-extraction.md).

What this line established: a 6 percent match rate at a 0.70 similarity threshold against 15 models is not a mapping strategy. Code assignment needs the index, not the embedding alone.

# 6. The current extraction platform, 2026

The `dev` branch of `imaging-problem-list` is a full extraction, coding, persistence, and review platform; see [the project profile](/applications/report-extraction-platform.md). Four things distinguish it from everything above.

**A richer extraction schema.** The original plan defines an extracted finding as a finding name, a presence drawn from present, absent, indeterminate, and possible, an optional location with body region, specific anatomy, and laterality, a list of attribute key and value pairs with standard keys for size, acuity, change from prior, severity, count, and morphology, and the verbatim report text it came from.[^ipl-initial-plan] The `possible` value exists specifically to hold hedged language such as "raising the possibility of" or "cannot exclude".

**Coding as a separate stage.** Assigning a finding code and a location code happens after extraction, not during it: a deterministic index lookup first, and only where that fails, three language model calls per report chunk to generate search terms, select a finding code from candidates, and select a location code from candidates. See [finding and location coding](/applications/finding-and-location-coding.md).

**Verbatim-quote validation.** A validator reviews each extraction against the chunk it came from and names the failure modes that justify re-extraction: content unsupported by the chunk text, report text describing a finding that no structure represents, a finding marked present when it is not or absent when it is possible, a finding name more specific than the text supports, incorrect representation of a blanket negative, and wrong or misscoped location information.[^ipl-validator]

**Evaluation redesigned for honesty.** After three and a half months without implementation, the evaluation plan was cut down rather than abandoned. Version one scores quote-first matching and attribute values rather than raw finding yield, uses frozen run configurations with per-case artifacts, and adjudicates a ten-case gold set through the human review tool. The stated motivation is a specific failure: a model-selection round chose a local default on throughput and yield alone, which cannot distinguish a real recall gain from a fabricated finding.[^ipl-evals]

# What carried forward

| From | What survived |
|---|---|
| template_extraction | A 281-template corpus, still unused |
| SARTemplatesToCDEs | One detailed CDE set redesign, and the conclusion that templates are not enough |
| ReportFindingRefiner | Section splitting, retrieval over real reports, local-model privacy |
| get_ontology_findings | The ontology-matching goal, widened into `med-ontology-lookup` |
| CDEStaging | The mini-observation shape, the negative-statement catalog, the uncovered-findings gap log |
| IPL-MVP | Presence as a first-class extracted field; the limits of similarity matching |
| imaging-problem-list `dev` | All of the above, plus separate coding, quote validation, and honesty-first evaluation |

[^template-extraction]: template_extraction, a corpus of 281 RadReport templates
[^sar]: SARTemplatesToCDEs README, the template to CDE set conversion goal
[^refiner]: ReportFindingRefiner README, the retrieval-augmented extraction architecture
[^get-ontology]: get_ontology_findings README
[^cde-process]: CDEStaging docs/report_extraction_process.md, manual report extraction worked example
[^cde-negatives]: CDEStaging report_representation/negative_statements.md
[^cde-uncovered]: CDEStaging report_representation/uncovered_findings.md
[^mvp]: IPL-MVP-ExtractionAndLabeling README, the four-stage pipeline
[^ipl-initial-plan]: imaging-problem-list initial-extraction-plan.md on dev, the extraction schema
[^ipl-validator]: imaging-problem-list validator prompt example on dev
[^ipl-evals]: imaging-problem-list docs/plans/extractor-evals-redesign.md on dev
