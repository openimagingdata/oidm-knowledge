---
type: Concept
title: IHE IDR alignment
description: What the IHE Imaging Diagnostic Report profile specifies for encoding findings as FHIR Observations, the deck's claim that the Exam Finding List connects to it, and the fact that no OIDM repository mentions it.
tags: [data-structures, ihe, idr, fhir, alignment, goal]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
sources:
  - id: idr-extract
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md
    title: IHE IDR Phase II extract, ACR-RSNA-CDEs next-gen-2026 branch, read from the supplement 2026-08-21
  - id: idr-supplement
    resource: https://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_Suppl_IDR_PhII_Rev1-2_PC_2026-03-04.pdf
    title: IHE Radiology Technical Framework Supplement, Imaging Diagnostic Report (IDR), Phase II, Rev. 1.2, Draft for Public Comment, 4 March 2026
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: "Open Imaging Data Model 2026 Status Update, January 2026"
  - id: ipl-main
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/README.md
    title: imaging-problem-list README, main branch
---

# Status first

This is a stated goal, not existing work. The January 2026 deck's slide on the [Exam Finding List](/data-structures/exam-finding-list.md) ends with one line: it "connects to IHE Imaging Diagnostic Report (IDR) FHIR representation."[^deck] That is the entire claim from the OIDM side. Searching the `imaging-problem-list` repository for "IHE" or "IDR" returns nothing on any branch, and no OIDM repository references the profile.

What does exist is a careful reading of the profile from the allied vocabulary work: a 72-page public-comment supplement, read directly and extracted on the `next-gen-2026` branch of `ACR-RSNA-CDEs`.[^idr-extract][^idr-supplement] That extract is the source for everything below, and it was written to test a different model, the next-generation CDE vocabulary, against the profile. It is the best available statement of what alignment would involve.

# What the profile is

The [Imaging Diagnostic Report](/glossary/imaging-diagnostic-report.md) profile is an IHE Radiology technical framework supplement specifying how a diagnostic imaging report and the findings in it are encoded as FHIR resources. Phase II Revision 1.2 went out for public comment on 4 March 2026.

Its information model, which the supplement says is "heavily influenced by modelling in SNOMED and DICOM", defines three terms.

| IDR term | IDR's definition | Encoded as |
|---|---|---|
| Body Structure | "encompasses both anatomical structures and morphologic abnormalities (like a lesion, cyst, inflammation, aneurysm, fracture or abscess)"; paired anatomy carries laterality | `BodyStructure` |
| (Imaging) Observation | "a feature or characteristic that is visible in an image, [which] may serve as the basis for determination that a finding is present and/or it may further characterize a finding" | FHIR `Observation` |
| (Clinical) Finding | "the determination that a clinical entity is present or absent, or the assessment that a clinical entity is normal or abnormal, with varying degrees of certainty" | positive findings as [FHIR Condition](/glossary/fhir-condition.md), negative findings as `Observation` |

The profile's own illustration: "the presence of a tumor is a finding, a recorded diameter of the tumor is an observation, a determination that the tumor is benign is a finding."[^idr-extract]

# The observation grammar

Every IDR observation has a target entity and content, split across five slots. This is the grammar an [Exam Finding List](/data-structures/exam-finding-list.md) would have to fit.

| Slot | FHIR location | Rule stated in the supplement |
|---|---|---|
| Anatomy | `Observation.bodyStructure.includedStructure.structure` | "fully pre-coordinated except for the laterality" |
| [Laterality](/glossary/laterality.md) | `...includedStructure.laterality` | a separate field, "if .structure is a paired structure" |
| Pathologic entity | `...includedStructure.morphology` | "shall not unnecessarily pre-coordinate the associated anatomy" |
| The property | `Observation.code` | "minimal pre-coordination of the property" |
| The value | `Observation.value` | units recorded in the value; two observations may share a code and use different units |

Worked rows from the supplement's own table show the shape. "Spiculated lesion in the lower lobe of the left lung" becomes structure *lung lower lobe*, laterality *left*, morphology *lesion*, with codes *Presence* and *Shape* carrying values *Detected* and *Spiculated*. "Liver contour is smooth" becomes structure *liver*, no morphology, code *Contour*, value *Smooth*, which makes an observation on a normal structure a first-class pattern rather than an edge case.[^idr-extract]

For grouped findings, IDR says that "Observation.code of the root finding shall identify the root of the finding set", and that "when encoding CDE Sets from radelement.org, it is preferred to use the CDE Set code here". The elements are reached through `Observation.hasMember`, and the associated observations do not reference the root.[^idr-extract]

# Where OIDM and IDR differ

Four differences are recorded in the extract. None of them has been worked through on the OIDM side; all are listed there as items to raise during public comment.

**Components against hasMember.** IDR states that `Observation.component` "is not used", because FHIR limits components to values "not useful on their own" and using it "has the potential to significantly complicate queries". Every OIDM encoding that carries attributes uses components: the documented Exam Finding List mapping says so explicitly, "a list of components with attribute codes and values", and both lineage FHIR samples implement it that way.[^ipl-main] This is the sharpest of the four, because it is the mechanism rather than a vocabulary choice. See [FHIR mapping](/data-structures/fhir-mapping.md).

**The word "observation" means different things.** IDR's observation is "a feature or characteristic that is visible in an image", closer to a single attribute value than to an OIDM [Observation](/glossary/observation.md), which is a whole finding with its location and attributes. IDR's "finding" is narrower too: it is the presence or absence determination, not the named entity. The extract flags this as a vocabulary collision, and notes that the next-generation vocabulary work moved away from the word "observation" for exactly this reason.

**Observation against Condition for diagnoses.** IDR routes positive clinical findings to Condition. The working default recorded in the extract runs the other way: "every assertion in a radiology report, diagnoses included, is encoded as an `Observation`", on the grounds that "'consistent with pneumonia' is a radiologist's assertion, not an established clinical condition". If that default holds, `Condition.evidence` as the finding-to-diagnosis link has nowhere to attach.

**Laterality placement.** IDR keeps laterality as a separate field beside an unsided structure code. OIDM's [anatomic location](/glossary/anatomic-location.md) identifiers are sided, with composite identifiers such as `RID39518_RID5824` for a left shoulder. A stated mapping between a sided identifier and the pair of unsided identifier plus laterality is needed so both directions round-trip.

# What IDR is asking

The extract also records three questions IDR puts to the RadElement side, which are requirements on any alignment: what extensibility is permitted when encoding [CDE sets](/glossary/cde-set.md), and in particular whether additional sub-observations may be included; what the coding system identifier for RadElement codes is; and whether a presence value belongs in the parent of a grouped observation or as its first child.[^idr-extract]

# Where this stands

| Claim | Evidence |
|---|---|
| The Exam Finding List connects to IDR | The deck states it; no repository implements or references it[^deck] |
| IDR's grammar is understood | A full extract of the Phase II supplement exists on the `next-gen-2026` branch[^idr-extract] |
| The differences are identified | Four, listed above, all recorded as items to raise, none resolved |
| Anything is built | No |

The profile extract itself is not migrated into this bundle; it lives on the `next-gen-2026` branch of `ACR-RSNA-CDEs` and is linked above. The unresolved items are carried in [open questions](/roadmap/open-questions.md).

[^idr-extract]: IHE IDR Phase II extract, ACR-RSNA-CDEs next-gen-2026 branch
[^idr-supplement]: IHE Imaging Diagnostic Report Phase II public comment draft, 4 March 2026
[^deck]: "Open Imaging Data Model 2026 Status Update", January 2026
[^ipl-main]: imaging-problem-list README, main branch
