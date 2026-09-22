---
type: Concept
title: Standards the foundation layers over
description: Which existing standard each Foundation Context axis layers over, the role each terminology plays, the external citations the deck names, and search recall as the gate.
tags: [foundation-context, terminologies, radlex, snomed, loinc, fma]
status: draft
generated: { by: claude-opus-5/2026-09-22-restructure/draft-axes, at: 2026-09-22T12:53:11Z }
sources:
  - id: siim2026
    resource: t3://oidm-public/oidm-knowledge-sources/SIIM%202026%20Reports-of-the-Future.pptx
    title: Structured Results and Context for Next-Generation Imaging Resulting Tools, SIIM 2026 annual meeting talk, June 2026, Mass General Brigham, slides 8 and 12
  - id: jdim-al
    resource: "Anatomic Locations Index: A Spatial Containment Hierarchy for Localizing Imaging Findings, manuscript under review at the Journal of Digital Imaging and Informatics in Medicine, 2026"
    title: Manuscript under review, Methods "Term selection" and Discussion; reviewer correspondence not used
  - id: cde-radlex-baseline
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/05-radlex-baseline.md
    title: "RadLex Baseline: Synonyms and External References, ACR-RSNA-CDEs next-gen-2026 branch"
  - id: radlex-search
    resource: https://github.com/RSNA/RadLex/blob/5162a65db531c8170139656f8a8ed27d96b6dd20/docs/plans/hybrid-fts-search.md
    title: Hybrid exact and BM25 full-text search over the RadLex graph, shipped and verified 2026-08-20
  - id: molu-roadmap
    resource: https://github.com/openimagingdata/med-ontology-lookup/blob/9cc3eec2c7af32e366e3f05e027b223b4a870077/docs/product-roadmap.md
    title: "Product direction: an agent-ready medical terminology graph gateway, med-ontology-lookup, research date 2026-08-16"
---

# One axis, one standard

The June 2026 SIIM talk presents Foundation Context as three axes, each described as an OIDM layer over something that already exists, adding imaging-specific knowledge rather than reinventing it. A code on an Observation is a pointer into one of these axes; the axes also point to each other and out to external references.[^siim2026]

| Axis | Question | Layers over |
|---|---|---|
| Observation Type | what was found | CDE and OIFM definitions |
| Anatomic Location | where it is | a [RadLex](/glossary/radlex.md)-anchored body map |
| Exam Type | how it was seen | [LOINC Playbook](/glossary/loinc-rsna-radiology-playbook.md) study types |

The talk's own label for the first axis is Observation Type; this bundle explains that axis under [finding models and CDEs](./finding-models-and-cdes.md). See [anatomic locations](./anatomic-locations.md) and [exam types](./exam-types.md) for what the other two layers add.

# What each terminology is for

The manuscript under review states why RadLex was chosen as the foundation: coverage of anatomy at the level of detail radiologists report, governance by the RSNA providing a defined pathway for contributing terms back, and stable identifiers. It recommends [SNOMED CT](/glossary/snomed-ct.md) as the cross-reference for enterprise coding, citing a 2024 HIMSS-SIIM assessment, and argues that adoption can proceed through existing bindings, since DICOM's anatomic region sequence and FHIR's body site value sets already bind to SNOMED CT. On that argument the index sits above the coding scheme rather than competing with it. [FMA](/glossary/fma.md), MeSH, and [UMLS](/glossary/umls.md) are additional cross-reference targets.[^jdim-al] The terminology gateway's roadmap assigns LOINC and the Playbook the orderables, while findings, anatomy, and report language stay with RadLex.[^molu-roadmap]

Two sources differ on SNOMED CT's place. The manuscript treats it as the enterprise coding target to cross-reference.[^jdim-al] The next-generation vocabulary work, checking the published RadLex release directly, found effectively no SNOMED CT mapping in it: six codes from the retired pre-CT SNOMED against 33,404 FMA references. It records that this contradicts a committee assumption, and treats the gap as something the vocabulary must carry itself or resolve upstream.[^cde-radlex-baseline]

# External citations

The talk's "connective tissue" slide names two kinds of outward link: citations to Radiopaedia and Wikipedia, and references to SNOMED, RadLex, LOINC, FMA, ICD, and CPT.[^siim2026] The gateway roadmap keeps ICD and CPT out of the radiology default: ICD's billing-oriented labels would crowd out findings, and CPT is licensed, available only through UMLS when the caller's license covers it, so a failed CPT call must report a license problem rather than an absence of hits.[^molu-roadmap]

# Search recall is the gate

A lookup that fails silently is worse than one that fails loudly, because an agent then concludes the concept is missing and proposes a duplicate. The RadLex search plan names that false-gap outcome as the worst failure mode the project has, and sets the target as recall good enough that a miss is real evidence of an ontology gap rather than evidence of unlucky phrasing. Its design keeps exact label and synonym tiers as the confidence signal and adds full-text relevance as the recall layer, emitting a categorical match type rather than a score, because scores are not comparable across queries.[^radlex-search] The gateway roadmap states a related boundary: a shared concept identifier is evidence of connection, not proof of exact equivalence.[^molu-roadmap] The tool itself belongs to the SDKs pillar; see [SDKs](./sdks.md).

[^siim2026]: SIIM 2026 annual meeting talk, June 2026, Mass General Brigham
[^jdim-al]: Anatomic Locations Index manuscript, under review at the Journal of Digital Imaging and Informatics in Medicine, 2026
[^cde-radlex-baseline]: RadLex Baseline, ACR-RSNA-CDEs next-gen-2026
[^radlex-search]: Hybrid full-text search over the RadLex graph, RSNA RadLex
[^molu-roadmap]: Product direction, med-ontology-lookup, 2026-08-16
