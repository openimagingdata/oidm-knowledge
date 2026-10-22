---
type: Glossary Term
title: CDE
description: Common data element, the ACR and RSNA programme of governed, balloted definitions for radiology findings and their elements.
tags: [glossary, semantic-foundation, cde]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: cde-repo
    resource: https://github.com/openimagingdata/common_data_elements/blob/35536d8c858bcd33e730a00c919edaef2e310a0b/README.md
    title: common_data_elements repository README
  - id: staging
    resource: https://github.com/openimagingdata/CDEStaging/blob/b814a102655054ac08b3c118cb1977a387655a8b/README.md
    title: CDEStaging repository README
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026
  - id: site-findings
    resource: https://www.openimagingdata.org/findings-cdes-and-observations/
    title: "Findings, CDEs, and Observations, 2023-06-24"
---

# CDE

**Common data element (CDE).** A governed definition of a radiology finding or of one property of a finding, authored and balloted through the ACR and RSNA Common Data Elements programme and published on [RadElement](/glossary/radelement.md).[^cde-repo] The word is used at two granularities, which is the main source of confusion: a [CDE set](/glossary/cde-set.md) is a whole finding, a [CDE element](/glossary/cde-element.md) is one property inside it.

CDEs are the standards-track counterpart of OIDM's own [finding models](/glossary/finding-model.md). The 2026 status deck describes finding models as a "CDE workbench": a proving ground where LLM-assisted authoring produces content quickly, and the best of it graduates into the formal CDE process.[^deck] The 2023 site post describes findings as FHIR Observations "semantically labeled with ACR/RSNA Common Data Element identifiers."[^site-findings]

Between informal authoring and publication sits a staging step: `CDEStaging` holds candidate definitions "prior to their entering the review pipeline."[^staging]

## Synonyms and near-synonyms

- **Common data element** is the expansion; this knowledgebase uses "CDE" after first use.
- **[RadElement](/glossary/radelement.md)** is the publication site and the coding system, not the definitions themselves.
- **[Data element](/glossary/data-element.md)** is the next-generation vocabulary's node type, narrower than "CDE" in the set sense.
- **[Finding model](/glossary/finding-model.md)** is the OIDM artifact, faster to author and not balloted.

## Identifier form

`RDES###` for a set, `RDE####` for an element. See [CDE set](/glossary/cde-set.md) and [CDE element](/glossary/cde-element.md).

## Where it is used

[CDEs and RadElement](/semantic-foundation/common-data-elements/cdes-and-radelement.md), [CDE staging](/semantic-foundation/common-data-elements/cde-staging.md), and [Finding models and CDEs](/semantic-foundation/finding-models/finding-models-and-cdes.md).

## Conflicts

"CDE" is used for the set, for the element, and for the programme as a whole in different source documents. Where precision matters, this knowledgebase says "CDE set" or "CDE element."

[^cde-repo]: common_data_elements repository README
[^staging]: CDEStaging repository README
[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
[^site-findings]: "Findings, CDEs, and Observations", 2023-06-24
