---
type: Glossary Term
title: Technical finding
description: A finding stated in modality-specific imaging language, such as a density or signal characteristic, without committing to an underlying diagnosis.
tags: [glossary, semantic-foundation, data-structures]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: tech
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/technical-imaging-findings.md
    title: Technical Imaging Findings reference, imaging-problem-list dev branch
  - id: overview
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/oifm-overview.md
    title: "Finding Models: Overview, description and diagnosis both count as findings"
  - id: lists-readme
    resource: https://github.com/openimagingdata/findingmodels/blob/a30c3c95fa3943e7340ce87575f4b1b926987eb8/lists/README.md
    title: MGB exam-oriented sub-taxonomies README, finding_type column
---

# Technical finding

A finding stated in modality-specific imaging language. "'Technical findings' describe what the radiologist observes on the images, signal characteristics, density, enhancement patterns, echogenicity, without necessarily committing to an underlying pathological process."[^tech]

The reference catalogs them by modality: CT attenuation terms such as hypodense lesion and ground-glass opacity; MR signal terms such as diffusion restriction and marrow signal abnormality; enhancement and opacification patterns such as washout and filling defect; ultrasound echogenicity terms such as anechoic structure and posterior acoustic shadowing; and nuclear medicine terms such as FDG-avid lesion and photopenic area.[^tech]

The distinction that matters for coding is observation versus interpretation. "The same imaging appearance can be described at observation level ('T2 hyperintense marrow signal') or interpretation level ('marrow edema'). Reports often mix both. The ontology needs entries at the observation level to capture what's actually seen." The guidance is specific: "marrow signal abnormality should be searched as exactly that, it is the observation. Do NOT reinterpret as 'bone marrow edema' or 'marrow infiltration', which are specific diagnoses that may or may not be the cause."[^tech]

## Synonyms and near-synonyms

- **Descriptive observation** is the authoring guidance's term for the same half of the split, opposite a diagnosis.[^overview]
- **Imaging observation** in IHE IDR is close but broader.
- **Descriptor** is not the same: "hypodense" alone is a characteristic of a lesion, while "hypodense liver lesion" is a technical finding.
- **`finding_type`** in a [finding taxonomy](/glossary/finding-taxonomy.md) row encodes the same observation-versus-diagnosis split.[^lists-readme]

## Identifier form

None distinct. A technical finding modelled as a [finding model](/glossary/finding-model.md) carries an ordinary OIFM identifier.

## Where it is used

[Technical imaging findings](/data-structures/technical-imaging-findings.md), [Finding and location coding](/applications/finding-and-location-coding.md), and [Why finding models](/semantic-foundation/finding-models/why-finding-models.md).

## Conflicts

The reference is explicitly a draft, and it ends with an unresolved question that matters for the vocabulary: whether "technical-observation entries and clinical-interpretation entries should be separate or merged in the ontology." It also records that the corpus has not yet been audited for coverage of these categories.[^tech]

[^tech]: Technical Imaging Findings reference
[^overview]: "Finding Models: Overview"
[^lists-readme]: MGB exam-oriented sub-taxonomies README
