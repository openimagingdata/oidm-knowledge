---
type: Reference
title: Laterality conventions
description: Sided location identifiers and references, with rules for assigning laterality to findings.
tags: [semantic-foundation, anatomic-locations, laterality, reference, migrated]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: fm-laterality
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/.claude/skills/manage-anatomic-locations/reference/laterality-conventions.md
    title: Laterality conventions, manage-anatomic-locations skill reference, findingmodel
  - id: ipl-rules
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/anatomic-location-assignment-rules.md
    title: Anatomic location assignment rules, imaging-problem-list dev
  - id: bpi-py
    resource: https://github.com/talkasab/BodyPartIndex.py/blob/388ae0a6da92f5ee4cf36620bbeeabe223938471/README.md
    title: BodyPartIndex.py README, the three-version convention
  - id: bpi-ts
    resource: https://github.com/talkasab/BodyPartIndex.ts/blob/dec578e10293d722e6136802cc5dfda2599f0f45/README.md
    title: BodyPartIndex.ts README, the three-version convention
  - id: fm-issues
    resource: https://github.com/openimagingdata/findingmodel/issues/39
    title: findingmodel issue 39, determine_laterality assigns left and right backwards
---

# Two questions

[Laterality](/glossary/laterality.md) has two sets of rules. Curation defines sided records in the [anatomic location](/glossary/anatomic-location.md) set, as described in the migrated curation convention below.[^fm-laterality] Coding assigns those records to findings using the extraction platform's rules.[^ipl-rules]

# Compound identifier pattern

Lateralized locations use [RadLex](/glossary/radlex.md) modifier identifiers appended to the base identifier.

| Modifier | RID | Compound identifier pattern |
|---|---|---|
| Left | `RID5824` | `{base_RID}_RID5824` |
| Right | `RID5825` | `{base_RID}_RID5825` |

For the pulmonary hilum, `RID34566`: generic `RID34566`, left `RID34566_RID5824`, right `RID34566_RID5825`.

# The three-entry pattern

For every lateralized structure, create three entries. The wrapper libraries state the same convention from the consumer's side: "for cases where the body part is sided, the index contains three versions: an unsided version, a left-sided version, and a right-sided version. All of these are aware of each other."[^bpi-py][^bpi-ts]

## Generic, unsided entry

Has both `leftRef` and `rightRef` pointing to the lateralized variants.

```json
{
  "_id": "RID34566",
  "description": "pulmonary hilum",
  "snomedId": "46750007",
  "snomedDisplay": "Structure of hilum of lung",
  "containedByRef": {"id": "RID1301", "display": "lung"},
  "leftRef": {"id": "RID34566_RID5824", "display": "left pulmonary hilum"},
  "rightRef": {"id": "RID34566_RID5825", "display": "right pulmonary hilum"},
  "synonyms": ["hilum", "lung hilum", "hilum of lung"]
}
```

## Left entry

Identifier `{base}_RID5824`. Has `rightRef`, its counterpart, and `unsidedRef`, back to the generic. `containedByRef` points to the left version of the container when one exists.

```json
{
  "_id": "RID34566_RID5824",
  "description": "left pulmonary hilum",
  "snomedId": "1650005",
  "snomedDisplay": "Structure of hilum of left lung",
  "containedByRef": {"id": "RID1326", "display": "left lung"},
  "rightRef": {"id": "RID34566_RID5825", "display": "right pulmonary hilum"},
  "unsidedRef": {"id": "RID34566", "display": "pulmonary hilum"},
  "synonyms": ["left hilum", "left lung hilum", "hilum of left lung"]
}
```

## Right entry

Identifier `{base}_RID5825`. Has `leftRef`, its counterpart, and `unsidedRef`. `containedByRef` points to the right version of the container, here `RID1302`, right lung.

# How the build system reads laterality

| References present | Laterality value | Explanation |
|---|---|---|
| `leftRef` and `rightRef` | `generic` | Has both sides, so it is the generic form |
| `leftRef` only | `right` | Points at its left counterpart, so this is the right variant |
| `rightRef` only | `left` | Points at its right counterpart, so this is the left variant |
| `unsidedRef` only | `generic` | Maps to generic |
| None | `nonlateral` | Not a lateralized structure |

A reference points to the counterpart. A left entry has `rightRef` and `unsidedRef`, but no `leftRef`.

Open issue 39 in the finding model repository reports that the build's `determine_laterality()` assigns left and right backwards.[^fm-issues]

# Containment and synonyms for sided entries

When the containing structure is itself lateralized, each variant points to the matching side. Generic to the generic container, left to the left container, right to the right container. When the container is not lateralized, the mediastinum for example, all three entries point to the same container.

Synonyms follow a consistent pattern. Generic `["hilum", "lung hilum", "hilum of lung"]`, left `["left hilum", "left lung hilum", "hilum of left lung"]`, right the same with "right."

# Assigning a side to a finding

The precedence is stated as explicit text side, then sided-exam side, then generic unsided.[^ipl-rules]

- **A non-sided exam never introduces a side.** On a CT abdomen, "adrenal glands unremarkable" resolves to the generic adrenal gland, not to a left one. "No hydronephrosis" with no side stated resolves to the generic kidney.
- **A sided exam sides the finding.** A left shoulder radiograph plus "humerus fracture" resolves to the left humerus.
- **Resolve laterality against the full report section, not the finding's isolated quote.** A finding's report text is one verbatim snippet, and the side is often stated only in a section header or an earlier sentence. When a section establishes a side it applies to every finding in that section unless a later sentence contradicts it. Coding from the isolated snippet silently drops section laterality and under-calls findings to the generic structure.
- **Never infer a side across exams or from clinical priors.** If this report's section gives no side, the finding stays generic even when a prior exam localized the same problem.

## Bilateral findings

| Case | Result |
|---|---|
| Positive bilateral, separable, meaning discrete independent lesions per side | Split into two findings, one left and one right, each duplicating the original attributes and report text |
| Positive bilateral, inseparable, meaning a single diffuse entity named as one | Generic unsided structure, not split |
| Spatially contiguous finding crossing the midline | Single finding, unsided structure |
| Generic absent, as in "no adrenal nodule" on a paired organ with no side | Generic organ, never a side |

The operational test for separable against inseparable: if you could meaningfully say "the left one is larger or newer," it is separable; if it is a named diffuse entity, it is inseparable.[^ipl-rules]

See [anatomic location assignment rules](/data-structures/anatomic-location-assignment-rules.md) for the full precedence, specificity, and exam-region rules.

# Known limitation

Generic and specific location pairs for the same finding code across exams, "kidney" against "left kidney" for instance, still produce separate [Imaging Problem List](/glossary/imaging-problem-list.md) groups. Deciding whether such observations are the same problem is recorded as an unresolved anatomic-compatibility reconciliation step.[^ipl-rules]

[^fm-laterality]: Laterality conventions, manage-anatomic-locations skill reference, findingmodel
[^ipl-rules]: Anatomic location assignment rules, imaging-problem-list dev
[^bpi-py]: BodyPartIndex.py README
[^bpi-ts]: BodyPartIndex.ts README
[^fm-issues]: findingmodel issue 39
