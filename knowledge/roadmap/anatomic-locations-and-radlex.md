---
type: Roadmap
title: Anatomic locations and RadLex
description: "The stated goals for the anatomic location set: incorporation into RadLex as an overlay, the node requests owed to the RadLex anatomy track, the two unreconciled datasets, the tooling items carried forward from the original libraries, and the body region enumerations that disagree."
tags: [roadmap, anatomic-locations, radlex, laterality, tooling]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T19:00:00Z }
stale_after: 2027-09-21
sources:
  - id: radlex-issue-3
    resource: https://github.com/RSNA/RadLex/issues/3
    title: RSNA/RadLex issue 3, "Add Anatomic Locations", opened 2026-08-10
  - id: cde-axis
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/11-anatomy-axis.md
    title: The anatomy axis, current state, ACR-RSNA-CDEs next-gen-2026 branch
  - id: cde-gaps
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/04-anatomy-gaps.md
    title: Anatomic locations gaps and node requests, ACR-RSNA-CDEs next-gen-2026 branch
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: "Open Imaging Data Model 2026 Status Update, January 2026"
  - id: bpi-todo
    resource: https://github.com/talkasab/BodyPartIndex.py/blob/388ae0a6da92f5ee4cf36620bbeeabe223938471/TODO.md
    title: BodyPartIndex.py TODO list, updated 2024-02-03
  - id: al-site
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/docs/index.markdown
    title: anatomiclocations.org site homepage and roadmap
  - id: plan
    resource: /plans/2026-09-20-knowledgebase-build-plan.md
    title: Knowledgebase build plan, recording the project lead's statements and the 2026-09-21 branch inventories
  - id: graph-research
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/tasks/anatomic-locations-graph-research.md
    title: Anatomic locations graph representation research note, findingmodel main branch
  - id: hierarchy-related
    resource: https://github.com/openimagingdata/findingmodel/blob/504a42aad771926f5fb91fd69fe0b637f4aef211/tasks/anatomic-hierarchy-aware-related-models.md
    title: Anatomic-hierarchy-aware related models task, findingmodel dev branch
  - id: fm-issue-39
    resource: https://github.com/openimagingdata/findingmodel/issues/39
    title: findingmodel issue 39, laterality assigned backwards in the build
  - id: fm-issue-38
    resource: https://github.com/openimagingdata/findingmodel/issues/38
    title: findingmodel issue 38, anatomic location search returns irrelevant results for multi-word queries
---

# Incorporation into RadLex

The January 2026 deck states that the [anatomic locations](/glossary/anatomic-location.md) are "being formally incorporated into RadLex by an RSNA committee."[^deck] The evidence for that statement is one tracking issue, `RSNA/RadLex` issue 3, "Add Anatomic Locations," opened 2026-08-10 and open. Its exit criterion is a single line: "100% coverage of the Anatomic Locations terminology in RadLex."[^radlex-issue-3]

No code, commit message, or document inside the `RSNA/RadLex` repository mentions anatomic locations, body parts, or OIDM. The relationship exists at the issue level; the ontology content is not there yet. The issue has no comments and no sub-issues. See [RadLex integration](/semantic-foundation/anatomic-locations/radlex-integration.md).

# The overlay agreement

A more specific agreement, dated 13 September 2026, is recorded in the next-generation vocabulary work on the `next-gen-2026` branch of `ACR-RSNA-CDEs`. The anatomic locations file is **an overlay on [RadLex](/glossary/radlex.md)**, not a replacement and not the sole source: RadLex concepts and predicates sit underneath, and the file adds identifiers RadLex lacks, its own containment and part-of hierarchies, and [laterality](/glossary/laterality.md).[^cde-axis]

Two consequences are already written into that vocabulary. An anatomic location carries one identifier, its [RadLex identifier](/glossary/radlex-id.md), and a RadLex code is never shown beside it, because the location code is the RadLex code. And the compound identifiers for sided variants that RadLex lacks, such as `RID1363_RID5825`, are an acknowledged exception the RadLex track is expected to remove by minting real identifiers.[^cde-axis]

The same record states that the overlay file is "the basis of the RadLex anatomy axis going forward," because the RadLex anatomy track is editing it rather than the published release.[^cde-axis]

Two framings of the relationship are therefore in force, and nobody has reconciled them. The issue's exit criterion, full coverage of the terminology in RadLex, reads as absorption. The September agreement describes an overlay that RadLex edits in place. The two are compatible but not identical, and no source says which governs. It is carried in [open questions](/roadmap/open-questions.md).

The scale of the sided-variant exception is worth stating with it: 1,016 of the 2,926 records carry a composite identifier, so more than a third of the set is not resolvable as a RadLex identifier until real ones are minted.

# What is owed in each direction

The gap log on that branch is the tracking artifact, kept deliberately separate from the wider design discussion so it can move independently.[^cde-gaps] The full list of node requests, with the reason and date for each, is reproduced in [RadLex integration](/semantic-foundation/anatomic-locations/radlex-integration.md). Two items are worth naming here because they are structural rather than individual concepts.

**From OIDM to RadLex: real identifiers for sided variants.** Raised 2026-09-13, needed by every sided [Observation](/glossary/observation.md).

**From RadLex to OIDM: an is-a relation and structure-type nodes.** Raised 2026-08-19 and restated 2026-09-13 as the top priority. The curated set has no is-a relation and no structure-type nodes, which is recorded as its major shortcoming, because it blocks any scope statement of the form "applies to tendons." RadLex 4.3 has an is-a chain for every one of the 1,910 plain-identifier locations, and the stated work item is a derived, pinned overlay file handed to the anatomic locations track. Two cautions accompany it: RadLex's own release note warns that some is-a categorizations were converted from part-of and may be wrong, and the FMA-style chain is not the clinically useful layer.[^cde-axis]

Coverage of external codes is uneven and is recorded as a gap rather than assigned as work: [SNOMED CT](/glossary/snomed-ct.md) on 1,782 of 2,926 records, with 608 records carrying no codes at all.[^cde-gaps]

# The two datasets

Two lineages coexist and are not synchronized: the original 2,890-node set published at anatomiclocations.org with its two wrapper libraries, and the 2,926-record dataset inside the `anatomic-locations` package in `findingmodel`, which the build plan names as current.[^plan] The differences and the open questions between them are set out in [lineage and current implementation](/semantic-foundation/anatomic-locations/lineage-and-current-implementation.md).

Reconciling the record counts is stated nowhere as work. No document says what the extra 36 records are, and no process syncs edits in either direction.

# Items carried forward from the original libraries

The clearest statement of intent for the original lineage is the TODO list added to `BodyPartIndex.py` on 2024-02-03. None of its items is done in that repository, and several were done independently in the current package.[^bpi-todo]

| Item | Status |
|---|---|
| Move the repository to the `openimagingdata` organization | Not done. The three original repositories remain under the project lead's personal account |
| Update to use the ACR Common codes | Not done anywhere |
| Update to acknowledge the DICOM codes | Not done anywhere |
| Add the ability to track URLs of various kinds | Not done |
| Rework `BodyPart` as a Pydantic model | Done in the current package, not in the original library |
| Reconfigure the index as a proper singleton | Not done |
| Make the website tree browser better, and add a way to submit suggestions about a specific node | Not done. The site still lists a hierarchy browser and search among features not yet built[^al-site] |

The site roadmap additionally lists finishing `BodyPartIndex.py` and publishing it to PyPI, which has not happened.[^al-site]

# Tooling

The project lead stated in the 2026-09-20 planning interview that the area needs tooling for the people who work with anatomic locations, meaning curators and coders rather than library consumers.[^plan] What exists today, the package, its command-line interface, the curation skill, and the older wrappers, is described in [tooling](/semantic-foundation/anatomic-locations/tooling.md).

Four concrete items sit in the `findingmodel` repository against that surface.

- **Hierarchy-aware related models.** A task on `dev` records that `related_models()` requires an exact identifier match today and therefore misses hierarchy-aware relations.[^hierarchy-related]
- **Graph representation research.** A note on `main` works through representing the containment and laterality graph in DuckDB and records why the adjacency-list plus recursive-query alternative was not chosen for a read-only database.[^graph-research]
- **Issue 39**, laterality assigned left and right backwards during the build.[^fm-issue-39]
- **Issue 38**, anatomic location search returning irrelevant results for multi-word queries.[^fm-issue-38]

Search quality is not a side issue for the RadLex relationship. The search and curation pipeline in the RadLex repository lives on an experiment branch rather than on `main`, and its search plan names the failure mode any gap list has to avoid: a concept lookup that silently returns nothing leads a consuming agent to conclude the concept is missing, which pollutes a candidate list with duplicates of concepts the ontology already has. Its stated goal is "recall good enough that a MISS is real evidence of an ontology gap rather than evidence of unlucky phrasing." See [RadLex integration](/semantic-foundation/anatomic-locations/radlex-integration.md).

# Four body region enumerations

[Body region](/glossary/body-region.md) is enumerated four incompatible ways across OIDM: in the anatomic locations package, in the finding model metadata rewrite, in the extraction schema, and in the viewer's filter. Thorax against chest, and whether spine is a region at all, are the recurring mismatches. No document reconciles them and no source assigns the reconciliation. It is carried, with the rest of the area's unresolved items, in [open questions](/roadmap/open-questions.md).

[^radlex-issue-3]: RSNA/RadLex issue 3, "Add Anatomic Locations"
[^cde-axis]: The anatomy axis, current state, next-gen-2026 branch
[^cde-gaps]: Anatomic locations gaps and node requests, next-gen-2026 branch
[^deck]: "Open Imaging Data Model 2026 Status Update", January 2026
[^bpi-todo]: BodyPartIndex.py TODO list, 2024-02-03
[^al-site]: anatomiclocations.org site homepage and roadmap
[^plan]: Knowledgebase build plan
[^graph-research]: Anatomic locations graph representation research note, findingmodel main branch
[^hierarchy-related]: Anatomic-hierarchy-aware related models task, findingmodel dev branch
[^fm-issue-39]: findingmodel issue 39
[^fm-issue-38]: findingmodel issue 38
