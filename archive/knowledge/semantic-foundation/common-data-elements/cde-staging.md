---
type: Project Profile
title: CDE staging
description: Candidate CDE definitions, report coverage gaps, and their conversion into finding models.
tags: [semantic-foundation, cde, radelement, repositories, content]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
stale_after: 2027-09-21
sources:
  - id: readme
    resource: https://github.com/openimagingdata/CDEStaging/blob/b814a102655054ac08b3c118cb1977a387655a8b/README.md
    title: CDEStaging README, purpose and layout
  - id: authoring
    resource: https://github.com/openimagingdata/CDEStaging/blob/b814a102655054ac08b3c118cb1977a387655a8b/docs/Authoring.md
    title: CDEStaging docs/Authoring.md, a stub pointing at the upstream schema
  - id: extraction-process
    resource: https://github.com/openimagingdata/CDEStaging/blob/b814a102655054ac08b3c118cb1977a387655a8b/docs/report_extraction_process.md
    title: Manual Report Extraction, the mini-observation worked example
  - id: negatives
    resource: https://github.com/openimagingdata/CDEStaging/blob/b814a102655054ac08b3c118cb1977a387655a8b/report_representation/negative_statements.md
    title: Composite Negative Statements, a corpus organized by organ system
  - id: uncovered
    resource: https://github.com/openimagingdata/CDEStaging/blob/b814a102655054ac08b3c118cb1977a387655a8b/report_representation/uncovered_findings.md
    title: Uncovered findings, extracted findings with no matching definition
  - id: missing-attrs
    resource: https://github.com/openimagingdata/CDEStaging/blob/b814a102655054ac08b3c118cb1977a387655a8b/report_representation/missing_attributes.md
    title: Missing attributes, report phrases existing definitions cannot carry
  - id: roadmap
    resource: https://github.com/openimagingdata/CDEStaging/blob/b814a102655054ac08b3c118cb1977a387655a8b/definitions/upmedic/roadmap.md
    title: Chest CT Findings roadmap, a prioritization table linking findings to RDES and RadLex codes
  - id: cardiomegaly
    resource: https://github.com/openimagingdata/CDEStaging/blob/b814a102655054ac08b3c118cb1977a387655a8b/definitions/upmedic/Cardiomegaly.cde.md
    title: Cardiomegaly.cde.md, an example of the coded markdown convention
  - id: issue-1
    resource: https://github.com/openimagingdata/CDEStaging/issues/1
    title: CDEStaging issue 1, Differences between radelement.org API schema and published Relax NG schema
  - id: issue-11
    resource: https://github.com/openimagingdata/CDEStaging/issues/11
    title: CDEStaging issue 11, Please Remove Plurality and values from Harmonized Pulmonary Nodule
  - id: fm-issue-15
    resource: https://github.com/openimagingdata/findingmodels/issues/15
    title: findingmodels issue 15, Bring in CDE Staging MD content
  - id: chestcts-convert
    resource: https://github.com/openimagingdata/findingmodels/blob/0472a4673fe476ec5335e6b3a1197faa70480426/scripts/cdestaging_ct_chest_to_finding_model.py
    title: CDEStaging CT chest conversion script on the content/chestcts branch of findingmodels
  - id: chestcts-triage
    resource: https://github.com/openimagingdata/findingmodels/blob/0472a4673fe476ec5335e6b3a1197faa70480426/scripts/triage_cdestaging_sources.py
    title: CDEStaging triage script on the content/chestcts branch of findingmodels
---

# What it is

`CDEStaging` collects candidate [common data element](/glossary/cde.md) definitions before formal review. Its README calls it "a staging area for definitions of radiology common data elements (CDEs) in JSON format ... prior to their entering the review pipeline."[^readme] The stated goal is "A multi-vendor project to generate a near-complete set of CDE Sets to represent the findings in chest CT reports."[^readme]

Contributions are organized by contributor. The README says provisional definitions go in the `definitions` directory "with separate folders for participating vendors."[^readme] Three folders are named after participating vendors, five carry a contributor prefix combined with a modality and body region (CT chest, CT abdomen and pelvis, chest radiograph, knee MRI, and O-RADS), and one holds location value lists.

Branch of record is `main`, at commit `b814a10` of 2025-11-25. See [the repository map](/repositories/repository-map.md).

# What is in it

The `definitions/` tree holds 463 files at that commit.

| Form | Count | Where |
|---|---:|---|
| Markdown definitions and finding lists | 259 | every contributor folder, plus two chest CT and knee MRI list files at the top level |
| JSON definitions | 150 | 103 in the CT chest folder, 46 in one vendor folder, 1 elsewhere |
| Plain text value and location lists | 39 | the locations folder and one vendor folder |
| PDF source material | 15 | the O-RADS folder |

The largest single collection is the CT chest folder, with 206 markdown files and 103 JSON files.

The JSON files use a name, description, and `choice` or `numeric` attributes with named values. This resembles a [finding model](/glossary/finding-model.md), rather than a [CDE set](/glossary/cde-set.md) conforming to `cde.schema.json`. All content is a pre-submission draft in its author's chosen format.

# Two authoring conventions

The markdown definitions use two unreconciled conventions.

**Coded `.cde.md` files.** Fourteen files in one vendor folder follow a structured convention: a `# Finding:` heading, a `source` and a `coding` bullet carrying a [RadLex identifier](/glossary/radlex-id.md), then one `##` section per [attribute](/glossary/attribute.md), with coded values, numeric attributes declared as `float` with a unit, and multi-select attributes marked in the heading.[^cardiomegaly]

```markdown
# Finding: Cardiomegaly
* source:
* coding: RID1385

## Presence
* present, coding: RID5791
* absent

## Cardiothoracic ratio (CTR)
* description: Ratio of the width of the cardiac silhouette and the thoracic cavity
* float: cardiac width ... cm
* float: thoracic cavity width ... cm
* float: ratio: ...

## chamber enlargement (multiselect)
* right atrium
* left atrium
* left ventricle
* right ventricle
```

**Per-region finding lists.** The five region folders use a plainer bullet-list convention: a finding name as the title, then `##` sections grouping bolded attribute names with their options separated by slashes. No codes, no types, no units.

```markdown
# Aberrant Subclavian Artery

## Identification

- **Presence of Aberrant Subclavian Artery**: Present / Absent

## Characteristics

- **Side of Origin**: Right / Left
- **Course**: Retroesophageal / Pretracheal / Other
```

The chest radiograph and knee MRI folders contain bare finding lists, one name per line, without attributes.

`docs/Authoring.md` is a two-sentence stub pointing to the upstream schema. It says "the authoring guide will be hosted here as well."[^authoring] The guide was never written.

# The report representation work

Four documents record what the definitions fail to capture from report text.

**The extraction process.** `docs/report_extraction_process.md` converts a chest CT report into "a list of mini-observations" containing a finding, attribute, and value.[^extraction-process] Its closing notes call for matching names to the definitions and cataloguing blanket negatives such as "Lungs are clear". The next two documents address those tasks.

**Composite negative statements.** A corpus of roughly 830 words of real negative and composite report sentences, grouped by organ system, collected to work out how absent findings should be modeled.[^negatives] Many are not simple negations. "Absence of intravenous contrast limits sensitivity for detecting solid organ findings" is a statement about the exam, not about a finding, and it recurs throughout the abdomen section.

**Uncovered findings.** A gap list of findings pulled out of reports for which no definition exists, each with the attributes the report gave it.[^uncovered] Entries range from ordinary findings with no definition yet, such as pulmonary edema and lymphadenopathy, to compound ones such as "post treatment squamous cells carcinoma" with an appearance attribute.

**Missing attributes.** The complementary list: report phrases whose finding does have a definition, but whose attributes that definition cannot carry.[^missing-attrs] Each entry links to the definition file it fails against. The recurring gap is anatomic detail below the level the definition models, such as a sclerotic change at T6 or a nodule in the left fissure.

Alongside them, `report_representation/structured_extractions/` holds 52 worked examples, each pairing a real chest CT report excerpt with its extracted finding list and links into the definition files.

# The prioritization roadmap

One vendor folder holds a roadmap table covering chest CT findings across nine organ-system sections: pulmonary, pleura, cardiovascular, lymphatic and endocrine, musculoskeletal, abdominal, lines and tubes, devices, and post-operative or treatment changes.[^roadmap] It has 100 finding rows. Each row carries the finding name, a frequency judgment of common, uncommon, or rare, a priority column, a status column holding links to any RadElement sets that already cover the finding, an "in V1" flag, and a RadLex identifier.

At the read commit, 22 rows are flagged for version 1, 18 distinct `RDES` sets are referenced, and 19 distinct RadLex identifiers appear. It records which staged findings have governed definitions in [RadElement](/glossary/radelement.md) and mappings to [RadLex](/glossary/radlex.md).

# The path to RadElement

The README and authoring stub point to `RSNA/ACR-RSNA-CDEs` for `cde.schema.json` and a sample set.[^readme][^authoring] The roadmap links existing RadElement sets, but no automated submission pipeline exists. Authors draft, harmonize, and submit through ACR and RSNA review. See [CDEs and RadElement](/semantic-foundation/common-data-elements/cdes-and-radelement.md).

# How it feeds finding models

Finding model conversion is more developed than RadElement submission.

`findingmodels` issue 15, "Bring in CDE Staging MD content," opened 2025-05-28 and still open, asks for a script that takes a markdown file, checks whether a definition already exists for that finding, and either converts it or merges it into the existing definition, reusing element identifiers and synonyms where possible, and adding the appropriate contributor.[^fm-issue-15]

That work exists on the `content/chestcts` branch of `findingmodels`, unmerged at commit `0472a46`. A triage script compares CT chest sources with the finding model search index.[^chestcts-triage] A conversion script uses merge, create, and review agents to write validated JSON.[^chestcts-convert] Both default to the `CDEStaging` CT chest directory. See [finding model content direction](/roadmap/finding-model-content-direction.md).

# Branch state and open issues

All recent work lands directly on `main`. Fourteen topic branches exist alongside it and eleven carry commits that are not on `main`. The largest are a report-representation branch of 37 commits and a content branch of 33 commits, both last touched on 2025-01-23. No branch has a commit after 2025-03-22, and no pull request proposes merging any of them.

Two issues are open.

| Issue | Opened | Subject |
|---|---|---|
| 1 | 2023-02-27 | Differences between the RadElement API schema and the published RelaxNG schema[^issue-1] |
| 11 | 2024-05-06 | A request to remove plurality and values from the harmonized pulmonary nodule definition[^issue-11] |

Issue 1 is the oldest open item in the repository and the same gap catalogued in [the schema comparison reference](/references/cde-schema-differences.md). It has had no activity since it was opened.

[^readme]: CDEStaging README, purpose and layout
[^authoring]: CDEStaging docs/Authoring.md, a stub pointing at the upstream schema
[^extraction-process]: Manual Report Extraction, the mini-observation worked example
[^negatives]: Composite Negative Statements, a corpus organized by organ system
[^uncovered]: Uncovered findings, extracted findings with no matching definition
[^missing-attrs]: Missing attributes, report phrases existing definitions cannot carry
[^roadmap]: Chest CT Findings roadmap, linking findings to RDES and RadLex codes
[^cardiomegaly]: Cardiomegaly.cde.md, an example of the coded markdown convention
[^issue-1]: CDEStaging issue 1
[^issue-11]: CDEStaging issue 11
[^fm-issue-15]: findingmodels issue 15, Bring in CDE Staging MD content
[^chestcts-convert]: CDEStaging CT chest conversion script, content/chestcts branch of findingmodels
[^chestcts-triage]: CDEStaging triage script, content/chestcts branch of findingmodels
