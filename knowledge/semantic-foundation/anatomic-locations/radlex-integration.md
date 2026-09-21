---
type: Concept
title: RadLex integration
description: What RadLex is, how the curated anatomic location set relates to it as an overlay, the open RSNA tracking issue for folding the set into RadLex, and the running list of node requests.
tags: [semantic-foundation, anatomic-locations, radlex, rsna, integration]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
sources:
  - id: radlex-issue-3
    resource: https://github.com/RSNA/RadLex/issues/3
    title: RSNA/RadLex issue 3, "Add Anatomic Locations", opened 2026-08-10, open
  - id: radlex-search
    resource: https://github.com/RSNA/RadLex/blob/5162a65db531c8170139656f8a8ed27d96b6dd20/docs/plans/hybrid-fts-search.md
    title: Hybrid exact and BM25 full-text search over the RadLex graph, RSNA/RadLex experiment/kg-radlex-parsing
  - id: radlex-repo
    resource: https://github.com/RSNA/RadLex
    title: RSNA/RadLex repository, ontology file and concept search pipeline
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: Open Imaging Data Model 2026 Status Update, January 2026
  - id: cde-axis
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/11-anatomy-axis.md
    title: The anatomy axis, current state, ACR-RSNA-CDEs next-gen-2026
  - id: cde-gaps
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/04-anatomy-gaps.md
    title: Anatomic locations gaps and node requests, ACR-RSNA-CDEs next-gen-2026
  - id: cde-record
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/10-decision-record-2026-09-02.md
    title: Decision record 2 to 15 September 2026, ACR-RSNA-CDEs next-gen-2026
---

# What RadLex is

[RadLex](/glossary/radlex.md) is RSNA's radiology lexicon, distributed as an OWL ontology file. The release read for this knowledgebase, RadLex 4.3, is a 52 MB RDF/XML document carrying 93,904 `owl:Class` declarations and 46,899 distinct [RadLex identifiers](/glossary/radlex-id.md).

Three features of its structure matter to OIDM:

- **Anatomy is expressed as OWL restrictions, not as a simple parent field.** A concept such as lung, `RID1301`, carries several `subClassOf` restrictions whose `owl:onProperty` is `Has_Part` or `Part_Of`, pointing at child identifiers. Roughly 30,000 triples relate anatomical entities this way. There is no separate physical-containment axis, which is why the curated set builds its own.
- **Provenance is carried on the concept.** A `RID:Source` annotation records free text such as "Playbook", "LOINC", or "LI-RADS 2020", saying where a concept came from.
- **Obsolescence is explicit.** `RID:Replaced_by` points a retired concept at its successor.

The `RSNA/RadLex` repository is not a copy of the ontology alone. Its working branches hold a concept search and curation pipeline that parses the OWL with `rdflib`, writes Parquet triples, builds a DuckDB graph of nodes, edges, and search documents, and drives an agent harness that matches report findings to RadLex concepts and proposes candidate new concepts for review.[^radlex-repo]

# Why search quality is the gating problem

The pipeline's search plan is worth reading because it names the failure mode that any integration has to avoid. Concept lookup failed "silently": a term that should match returned nothing or returned noise, and the consuming agent concluded the concept was missing from RadLex. That false-gap outcome is called the worst failure mode of the project, because it flows straight into proposing a concept and pollutes the candidate file with duplicates of concepts RadLex already has.[^radlex-search]

Two defects produced it. The graph query ranked alphabetically rather than by relevance, so searching `LUL` returned 69 rows with the correct concept, `RID1327` upper lobe of left lung, sorting 67th behind concepts that merely contain the letters. A replacement scorer fixed ranking but matched literal words only, so `part-solid nodule`, `hilar adenopathy`, and `enlarged lymph nodes` all missed.[^radlex-search]

The design keeps exact matching as the confidence signal and adds BM25 underneath as a recall layer, with a per-query relative cutoff because BM25 scores are not comparable across queries. The stated goal is "recall good enough that a MISS is real evidence of an ontology gap rather than evidence of unlucky phrasing." The plan is marked complete, shipped 2026-08-20.[^radlex-search] For OIDM this matters because a gap list handed to RadLex is only as trustworthy as the search that produced it.

# The tracking point

`RSNA/RadLex` issue 3, "Add Anatomic Locations", was opened on 2026-08-10 by RSNA and is open. Its exit criterion is one line: "100% coverage of the Anatomic Locations terminology in RadLex."[^radlex-issue-3]

That issue is the whole of the integration as recorded in the RadLex repository. No code, commit message, or document inside the repository mentions anatomic locations, body parts, or OIDM. The relationship exists at the issue level, not yet in the ontology file.

The January 2026 status update states the direction more simply, saying the anatomic locations are "being formally incorporated into RadLex by RSNA committee."[^deck] The issue is the evidence for that statement; the ontology content is not there yet.

# The overlay agreement

The next-generation vocabulary work on the `next-gen-2026` branch of `ACR-RSNA-CDEs` records a more specific agreement, dated 13 September 2026. The anatomic locations file is **an overlay on RadLex**, not a replacement and not the sole source. RadLex concepts and predicates sit underneath; the file adds identifiers RadLex lacks, its own containment and part-of hierarchies, and [laterality](/glossary/laterality.md).[^cde-axis]

The same record states that the file is "the basis of the RadLex anatomy axis going forward," because the RadLex anatomy track is editing it. Aiming at the published RadLex release instead is described as editing a three-year-old version of a document that others have been editing.[^cde-axis]

Two consequences are already written into that vocabulary:

- An anatomic location carries one identifier, its RadLex identifier, and a RadLex code is never shown alongside an anatomic location, because the location code is the RadLex code.[^cde-record]
- The compound identifiers for sided variants that RadLex lacks, such as `RID1363_RID5825` for the right pleural space, are an acknowledged exception that the RadLex track is expected to remove by minting real identifiers.[^cde-axis]

# What RadLex can supply in return

The traffic is not one way. The curated set has no is-a relation and no structure-type nodes, which is recorded as its major shortcoming. RadLex 4.3 has an is-a chain for every one of the 1,910 plain-identifier locations, up to "anatomical entity," and walking it yields a first structure-type layer without inventing anything: 352 locations under muscle organ, 221 under artery, 137 under vein, 115 under tendon, 101 under bone organ, 28 each under joint and nerve, and 26 under lymph node.[^cde-axis]

Two cautions are recorded with that finding. RadLex's own release note warns that some of its is-a categorizations were converted from part-of and may be wrong, so a derived layer needs a clinical skim. And the FMA-style chain, in which a lung is a "lobular organ," is not the clinically useful layer. The work item is a derived, pinned overlay file handed to the anatomic locations track.[^cde-axis]

# The node request list

The gap log on the same branch keeps a running list of specific "we need this node" changes to carry to the RadLex anatomy track, kept deliberately separate from the wider design discussion so it can move independently.[^cde-gaps]

| Request | Needed by | Raised |
|---|---|---|
| `lung parenchyma`, contained by and part of `lung` | consolidation, ground-glass opacity | 2026-09-08 |
| `perirenal space` with left and right forms | the pyelonephritis worked example | 2026-09-14 |
| `pericardial space` | pericardial effusion | 2026-07-28 |
| `subarachnoid space` | subarachnoid hemorrhage | 2026-07-28 |
| Real RadLex identifiers for the compound sided variants | every sided [Observation](/glossary/observation.md) | 2026-09-13 |
| An is-a relation and structure-type nodes | scope of the form "applies to tendons" | 2026-08-19, restated 2026-09-13 as the top priority |

The log also records closures and oddities, which is what makes it useful as a status document rather than a wish list. `pleural space` was found present as `RID1363` with both sided forms and is marked closed. External-code coverage is uneven, with SNOMED CT on 1,782 of 2,926 records and 608 records carrying no codes at all. And `lung` is contained by `pleural space` in the data, which is anatomically odd and which any check that walks containment from a lung location will pass through.[^cde-gaps]

Goals for this area, and who has stated them, are collected in [the anatomic locations and RadLex roadmap](/roadmap/anatomic-locations-and-radlex.md). RadLex's place among the terminologies OIDM uses is described in [ontologies used](/semantic-foundation/terminologies/ontologies-used.md).

[^radlex-issue-3]: RSNA/RadLex issue 3, "Add Anatomic Locations"
[^radlex-search]: Hybrid exact and BM25 full-text search over the RadLex graph
[^radlex-repo]: RSNA/RadLex repository
[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
[^cde-axis]: The anatomy axis, current state, ACR-RSNA-CDEs next-gen-2026
[^cde-gaps]: Anatomic locations gaps and node requests, ACR-RSNA-CDEs next-gen-2026
[^cde-record]: Decision record 2 to 15 September 2026, ACR-RSNA-CDEs next-gen-2026
