---
type: Reference
title: Technical imaging findings
description: A draft catalog of modality-specific technical finding language, CT attenuation, MR signal, enhancement, ultrasound echogenicity, and nuclear medicine, with the search-term guidance for coding each, migrated from the imaging-problem-list development branch.
tags: [data-structures, technical-finding, coding, terminology, migrated, draft]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
sources:
  - id: tech
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/technical-imaging-findings.md
    title: docs/technical-imaging-findings.md, imaging-problem-list dev branch, the origin of this document
---

# About this document

This is a near-verbatim migration of `docs/technical-imaging-findings.md` from the `imaging-problem-list` repository's development branch.[^tech] The source marks itself **Draft, needs review against the finding ontology for coverage assessment**, and that status carries over: the catalog has not been audited against the finding model corpus, and its closing questions are open. Wording and structure follow the original.

Radiology reports frequently describe findings using modality-specific technical language rather than clinical diagnoses. These [technical findings](/glossary/technical-finding.md) describe what the radiologist observes on the images, including signal characteristics, density, enhancement patterns, and echogenicity, without necessarily committing to an underlying pathological process.

The original states three purposes for the catalog: ensuring the finding ontology has coverage for these observation-level concepts, guiding search term generation when coding technical findings, and identifying gaps where new ontology entries may be needed.

# CT attenuation-based findings

Computed tomography measures tissue density in Hounsfield units. Findings are often described relative to surrounding tissue.

| Technical term | Meaning | Example report language |
|---|---|---|
| Hypodense or hypoattenuating lesion | Lower density than surrounding tissue | "hypodense lesion in the liver" |
| Hyperdense or hyperattenuating lesion | Higher density than surrounding tissue | "hyperdense focus in the right kidney" |
| Fat-containing lesion | Contains macroscopic fat, negative Hounsfield units | "fat-containing adrenal lesion" |
| Calcified lesion or calcification | Contains calcium, high Hounsfield units | "calcified granuloma in the lung" |
| Hypoattenuating parenchyma | Diffuse low attenuation of an organ | "diffuse decreased hepatic attenuation" |
| Ground-glass opacity | Hazy increased lung attenuation | "ground-glass opacity in the right lower lobe" |

**Search term considerations.** "Hypodense liver lesion" should be searched as "liver lesion", "focal liver lesion", or "hepatic lesion". The attenuation descriptor is a characteristic of the lesion, not the finding category itself.

# MR signal-based findings

Magnetic resonance imaging characterizes tissue by signal intensity on different pulse sequences.

| Technical term | Meaning | Example report language |
|---|---|---|
| T2 signal abnormality | Abnormal signal on T2-weighted images | "T2 hyperintense focus in the white matter" |
| T1 signal abnormality | Abnormal signal on T1-weighted images | "T1 shortening in the posterior pituitary" |
| Diffusion restriction | High signal on diffusion-weighted imaging with low apparent diffusion coefficient | "focus of restricted diffusion in the left cerebellum" |
| Susceptibility artifact or blooming | Signal dropout on gradient-echo or susceptibility-weighted sequences | "susceptibility artifact suggesting hemorrhage" |
| Marrow signal abnormality | Abnormal bone marrow signal | "marrow signal abnormality in L3 vertebral body" |
| White matter signal abnormality | Abnormal signal in cerebral white matter | "scattered white matter T2 hyperintensities" |
| Enhancement, post-contrast | Abnormal gadolinium uptake | "enhancing lesion in the right frontal lobe" |

**Search term considerations.** "Marrow signal abnormality" should be searched as exactly that, because it is the observation. Do not reinterpret it as "bone marrow edema" or "marrow infiltration", which are specific diagnoses that may or may not be the cause.

# Enhancement and opacification patterns

Enhancement describes how tissue takes up contrast agent over time. Relevant to computed tomography, magnetic resonance, and angiographic studies.

| Technical term | Meaning | Example report language |
|---|---|---|
| Enhancing lesion | Lesion that takes up contrast | "enhancing mass in the pancreas" |
| Non-enhancing lesion | Lesion that does not take up contrast | "non-enhancing cystic lesion" |
| Arterial enhancement | Enhancement during arterial phase | "arterially enhancing liver lesion" |
| Washout | Loss of enhancement on delayed phase | "arterial enhancement with washout" |
| Abnormal enhancement | Enhancement pattern different from expected | "abnormal mucosal enhancement" |
| Filling defect | Lack of opacification within a vessel | "filling defect in the pulmonary artery" |
| Abnormal venous opacification | Abnormal contrast pattern in veins | "absent opacification of the left renal vein" |
| Flow abnormality | Abnormal vascular flow pattern | "hepatic venous flow abnormality" |

**Search term considerations.** "Filling defect in the pulmonary artery" is the technical observation; the clinical interpretation might be "pulmonary embolism", but they are distinct concepts. The ontology may have entries at either level. Enhancement-based findings in a specific organ, such as "abnormal hepatic venous enhancement", should be searched using the physiological concept, "hepatic venous flow abnormality", alongside the technical term.

# Ultrasound echogenicity-based findings

Ultrasound characterizes tissue by how it reflects sound waves.

| Technical term | Meaning | Example report language |
|---|---|---|
| Hypoechoic lesion | Less echogenic than surrounding tissue | "hypoechoic lesion in the thyroid" |
| Hyperechoic lesion | More echogenic than surrounding tissue | "hyperechoic liver lesion" |
| Anechoic structure | No internal echoes, fluid-filled | "anechoic cyst in the kidney" |
| Isoechoic lesion | Same echogenicity as surrounding tissue | "isoechoic nodule in the liver" |
| Heterogeneous echotexture | Mixed echogenicity | "heterogeneous echotexture of the thyroid" |
| Increased echogenicity | Diffusely increased echogenicity | "increased hepatic echogenicity" |
| Posterior acoustic shadowing | Sound blocked by dense structure | "echogenic focus with posterior shadowing" |
| Increased vascularity | Abnormal blood flow on Doppler | "increased vascularity on color Doppler" |

**Search term considerations.** "Increased hepatic echogenicity" is the technical observation for what is clinically interpreted as hepatic steatosis. Both the technical term and the clinical interpretation are valid search terms, but they represent different levels of certainty.

# Nuclear medicine and PET findings

| Technical term | Meaning | Example report language |
|---|---|---|
| FDG-avid lesion | Lesion with increased metabolic activity | "FDG-avid lymph node in the mediastinum" |
| Photopenic area | Decreased radiotracer uptake | "photopenic defect in the right lobe of the thyroid" |
| Hot spot or increased uptake | Focal increased radiotracer activity | "increased uptake in the L4 vertebral body" |
| Tracer accumulation | Abnormal radiotracer concentration | "delayed tracer accumulation in the gallbladder fossa" |

# Cross-cutting patterns

Some technical finding patterns span multiple modalities.

- **Focal against diffuse.** Focal findings are discrete, bounded abnormalities, a "lesion". Diffuse findings affect an entire organ or region, a "disease", "abnormality", or "process".
- **Descriptors that narrow but do not diagnose.** Size, shape, margins, multiplicity, and temporal change characterize a finding without specifying what it is.
- **Observation against interpretation.** The same imaging appearance can be described at observation level, "T2 hyperintense marrow signal", or interpretation level, "marrow edema". Reports often mix both. The ontology needs entries at the observation level to capture what is actually seen.

# Open items

The source closes with four unresolved tasks, carried here unchanged.

- Audit the finding ontology against these categories to identify coverage gaps.
- Determine which technical terms resolve through the fast path against those needing a model-driven search.
- Decide whether technical-observation entries and clinical-interpretation entries should be separate or merged in the ontology.
- Add examples of each category to the coding agent prompt if needed after the ontology audit.

The third is a question about the [finding model](/glossary/finding-model.md) corpus rather than about coding, and it is recorded in [open questions](/roadmap/open-questions.md). The coding pipeline that consumes this guidance is described in [finding and location coding](/applications/finding-and-location-coding.md).

[^tech]: docs/technical-imaging-findings.md, imaging-problem-list dev branch
