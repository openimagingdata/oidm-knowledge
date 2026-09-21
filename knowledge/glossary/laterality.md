---
type: Glossary Term
title: Laterality
description: The left, right, or unsided character of an anatomic structure or a finding, represented as a triad of linked variants and resolved by a stated precedence.
tags: [glossary, semantic-foundation, anatomy]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T16:00:00Z }
sources:
  - id: bpi
    resource: https://github.com/talkasab/BodyPartIndex.py/blob/388ae0a6da92f5ee4cf36620bbeeabe223938471/README.md
    title: BodyPartIndex.py README, laterality triads
  - id: al-package
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/anatomic-locations/src/anatomic_locations/models/enums.py
    title: Laterality enumeration in the anatomic-locations package
  - id: rules
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/anatomic-location-assignment-rules.md
    title: Anatomic location assignment rules, imaging-problem-list dev branch
  - id: idr
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md
    title: IHE IDR Phase II extract for the CDE vocabulary
---

# Laterality

Whether a structure or a finding is left, right, or neither. The curated anatomic sets represent it structurally: "for cases where the body part is sided, the index contains three versions: an unsided version, a left-sided version, and a right-sided version. All of these are aware of each other."[^bpi] The newer package makes this an enumeration with four values, `generic` for a structure that has left and right variants, `left`, `right`, and `nonlateral` for a structure with no sides at all such as the heart or the spine.[^al-package]

Assigning laterality to a finding follows a stated precedence: explicit side in the text beats a sided exam, which beats the generic unsided structure. A non-sided exam never introduces a side. Laterality must be resolved "against the full report section, not the finding's isolated quote," because the side is often stated only in a section header or an earlier sentence, and a side is never inferred across exams or from clinical priors.[^rules]

Bilateral findings split or do not split by a stated test. Discrete independent lesions per side become two findings; a single diffuse entity named as one, an "-osis" or a "disease," stays generic and unsided. The operational test is whether "you could meaningfully say the left one is larger or newer."[^rules]

## Synonyms and near-synonyms

- **Sidedness** and **side** are informal equivalents.
- **Unsided**, **generic**, and **nonlateral** are not interchangeable: generic means sides exist but none is specified, nonlateral means the structure has no sides.
- **Bilateral** is an assertion about a finding, not a laterality value on a structure.

## Identifier form

In the original set, sided variants take composite identifiers such as `RID294_RID5824`. In the newer package, laterality is an enum field with `left_variant`, `right_variant`, and `generic_variant` references.

## Where it is used

[Laterality conventions](/semantic-foundation/anatomic-locations/laterality-conventions.md), [Data model](/semantic-foundation/anatomic-locations/data-model.md), and [Anatomic location assignment rules](/data-structures/anatomic-location-assignment-rules.md).

## Conflicts

IHE IDR keeps laterality in a separate FHIR field on an unsided structure code, while OIDM's anatomy nodes are themselves sided. The IDR extract lists a stated mapping between the two, sided identifier and unsided identifier plus laterality, as something still needed so both directions round-trip.[^idr] A known defect in the `findingmodel` issue list also reports that laterality is assigned backwards during one database build step.

[^bpi]: BodyPartIndex.py README
[^al-package]: Laterality enumeration in the anatomic-locations package
[^rules]: Anatomic location assignment rules
[^idr]: IHE IDR Phase II extract
