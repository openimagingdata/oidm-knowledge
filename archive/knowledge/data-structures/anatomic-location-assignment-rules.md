---
type: Reference
title: Anatomic location assignment rules
description: Migrated rules for assigning anatomy, laterality, and specificity to Exam Finding List observations.
tags: [data-structures, anatomic-location, laterality, coding, migrated]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: anat-rules
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/anatomic-location-assignment-rules.md
    title: docs/anatomic-location-assignment-rules.md, imaging-problem-list dev branch, the origin of this document
  - id: anat-plan
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/anatomic-location-efl-ipl.md
    title: Anatomic location for Exam Finding Lists and Imaging Problem Lists, the plan whose Step 3b is the open follow-on
  - id: anat-pkg
    resource: https://pypi.org/project/anatomic-locations/
    title: The anatomic-locations package, the RID-coded index these rules resolve against
---

# About this document

Migrated near-verbatim from `docs/anatomic-location-assignment-rules.md` on `imaging-problem-list`'s development branch.[^anat-rules] Wording and structure follow the original; only terminology and links have been adjusted for this knowledgebase. The rules were agreed for a correction pass over the `sample_data/example2` findings and are "the intended spec for tuning the automated location-coding step later."

The subject is how an `anatomicLocation` of `{locationId, locationDisplay}`, a [RadLex identifier](/glossary/radlex-id.md) from the [`anatomic-locations`](https://pypi.org/project/anatomic-locations/) index, is assigned to each [observation](/data-structures/observation.md) in an [Exam Finding List](/data-structures/exam-finding-list.md).[^anat-pkg]

# Precedence ladder

Apply per observation, in order.

1. **Explicit anatomy in the report text or section context wins.** Use the most specific structure stated, sided only if a side is stated. Section headers count as context. Under a `Chest Wall:` heading, "No soft tissue mass" resolves to *chest wall*; as a bare `Soft Tissues:` paragraph it stays the coarse region, per step 3.
2. **Else, if the finding has a definable target organ or structure**, use that organ at the finding's own anatomic-noun granularity, never finer, applying the laterality rules below.
3. **Else**, meaning no anatomic noun at all, as in "soft tissue mass" or "generalized osteoporosis", fall back to the **exam-scoped coarse region** (thorax, abdomen, head, and so on), sided only if the exam is sided.

**Organ always wins over exam-region** when the finding has a real target organ, especially in edge-of-exam cases. "No consolidation" or "lung bases clear" on an abdominal computed tomography resolves to **lung**, never "abdomen".

# Laterality

Source priority for [laterality](/glossary/laterality.md): **explicit text side, then sided-exam side, then generic and unsided**.

- A **non-sided exam never introduces a side.** On a computed tomography of the abdomen, "adrenal glands unremarkable" resolves to *adrenal gland*, generic, not "left adrenal gland". "No hydronephrosis" with no side resolves to *kidney*, generic.
- A **sided exam sides the finding.** "XR Shoulder - left" plus "humerus fracture" resolves to *left humerus*.
- **Resolve laterality against the full report section, not the finding's isolated quote.** A finding's `reportText` is one verbatim snippet, and the side is often stated only in the section header or an earlier sentence of the same section, not in that snippet. When the section establishes a side, it applies to every finding in the section unless a later sentence contradicts it. This is precedence rule 1, text and section context wins, applied to laterality.

**Worked example, a real miss now fixed.** A chest computed tomography `Shoulders:` section reads "The **left** glenohumeral joint demonstrates a moderate joint effusion. The humeral head is in a high-riding position. Calcifications are noted in the region of the rotator cuff insertion." The high-riding-head and calcific-tendinopathy findings carry snippets with no side, but the section establishes **left**, so they resolve to `left glenohumeral joint` and `left supraspinatus tendon`, not the generic structures.

**Pitfall.** Reviewing or coding from the isolated `reportText` silently drops section laterality and under-calls findings to the generic structure. Always read the snippet against its section.

**Still do not infer a side across exams or from clinical priors.** If this report's section gives no side, stay generic even when another exam localized the same problem. An ultrasound snippet reading "parapelvic cysts" with no side stays *kidney* even though a prior computed tomography said "left kidney".

# Bilateral findings

- **Positive bilateral, separable**, meaning discrete independent lesions or structures per side, **splits into two findings**, one left and one right, each duplicating the original attributes and report text. Example: bilateral maxillary mucosal thickening becomes left and right maxillary sinus. Bilateral renal calculi were already separate observations in the source data and are not re-split.
- **Positive bilateral, inseparable process**, meaning a single diffuse entity named as one, an "-osis", a "disease", a confluent process, resolves to a **generic, unsided** structure. Example: bilateral cerebral small-vessel disease resolves to *cerebral hemisphere*, generic, not split.
- **Spatially contiguous** findings crossing the midline resolve to a **single finding with an unsided** structure.
- **Generic absent**, as in "No adrenal nodule" on a paired organ with no side stated, resolves to the **generic organ**, never a side.

Operational test for separable against inseparable: if you could meaningfully say "the left one is larger or newer", it is separable; if it is a named diffuse entity, it is inseparable.

# Specificity

The target's granularity **matches the finding's anatomic noun, capped by the report, never finer**.

- "humerus fracture", from a cleared-bones statement, resolves to *humerus*, not "head of humerus".
- "upper extremity fracture" resolves to *upper extremity*, a real body-part structure, sided by exam, not left blank.
- Region-named findings such as "upper extremity", "skull", and "spine" resolve to their body-part structure. They are step-2 targets, **not** the exam-region fallback.

# Exam-scoped region fallback

Only for findings with **no anatomic noun**, such as "soft tissue mass" or "generalized osteoporosis".

- The grain is the **coarse region**, not a soft-tissue substructure. "No soft tissue mass" on a chest computed tomography resolves to *thorax*, not "chest wall" or "musculature of thorax", unless report section context names the substructure, in which case step 1 applies.
- Exam to region map, by RadLex identifier: computed tomography of the abdomen or abdomen and pelvis resolves to *abdomen* `RID56`; chest computed tomography or radiography to *thorax* `RID1243`; magnetic resonance of the brain to *head* `RID9080`; shoulder to *shoulder* `RID39518`. A combined abdomen and pelvis study defaults to *abdomen* unless the text points pelvic.
- **Diffuse findings with a textual predominance keep the text location**, per step 1. "Osteopenia, especially in the thoracic spine" resolves to *thoracic vertebral column*; a bare "Diffuse osteopenia" resolves to the exam region.

# Resolution and validation

- For a **named target organ**, resolve by direct lookup, meaning `AnatomicLocationIndex.get` or an exact match, **not** flaky semantic search. This avoids retrieval misses such as "prostate" returning salivary glands. Derive sided identifiers from the generic entry through its `left_id` and `right_id`.
- Every assigned `locationId` must exist in the ontology. Structures absent from the ontology, such as *basal cistern* or *dural venous sinus*, are left unassigned rather than forced to a wrong code.

# Known limitation

Parent-child or generic-versus-specific pairs for the *same finding code across exams*, such as "lung" against "lower lobe of right lung", or "kidney" against "left kidney", still produce separate [Imaging Problem List](/data-structures/imaging-problem-list.md) groups. Deciding whether such observations are the same problem or distinct is the **anatomic-compatibility reconciliation** step, Step 3b of the anatomic location plan.[^anat-plan] That step has not been started.

# Related

The [anatomic locations](/semantic-foundation/anatomic-locations/) area covers the underlying data model, the laterality triads these rules derive sided identifiers from, and the tooling. The pipeline that applies these rules is described in [finding and location coding](/applications/finding-and-location-coding.md).

[^anat-rules]: docs/anatomic-location-assignment-rules.md, imaging-problem-list dev branch
[^anat-plan]: Anatomic location for Exam Finding Lists and Imaging Problem Lists, dev branch
[^anat-pkg]: The anatomic-locations package
