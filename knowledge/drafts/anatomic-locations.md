---
type: Concept
title: Anatomic locations
description: The curated anatomic location index as a reference layer - identity, containment, part-of, laterality, synthetic terms, curation rules, the RadLex overlay, and the two dated implementations.
tags: [foundation-context, anatomic-locations, radlex, laterality, containment]
status: draft
generated: { by: claude-opus-5/2026-09-22-restructure/draft-axes, at: 2026-09-22T12:53:11Z }
sources:
  - id: jdim-al
    resource: "Anatomic Locations Index: A Spatial Containment Hierarchy for Localizing Imaging Findings, manuscript under review at the Journal of Digital Imaging and Informatics in Medicine, 2026"
    title: Manuscript under review, read as the blinded manuscript body only; reviewer correspondence not used
  - id: siim2026
    resource: t3://oidm-public/oidm-knowledge-sources/SIIM%202026%20Reports-of-the-Future.pptx
    title: Structured Results and Context for Next-Generation Imaging Resulting Tools, SIIM 2026 annual meeting talk, June 2026, Mass General Brigham, slides 8, 10 and 12
  - id: al-site
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/docs/index.markdown
    title: Anatomic Locations project site homepage, rationale, features and roadmap, unchanged since January 2023
  - id: fm-data
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/notebooks/data/anatomic_locations_noembed.json
    title: anatomic_locations_noembed.json, the current curated set, 2,926 records
  - id: fm-fields
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/.claude/skills/manage-anatomic-locations/reference/json-schema.md
    title: Anatomic locations source JSON field reference, including the SNOMED CT SEP triad rule
  - id: fm-laterality
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/.claude/skills/manage-anatomic-locations/reference/laterality-conventions.md
    title: Laterality conventions, the compound identifier pattern and the three-entry rule
  - id: fm-skill
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/.claude/skills/manage-anatomic-locations/SKILL.md
    title: The manage-anatomic-locations skill and its lookup, sampling and validation scripts
  - id: fm-package
    resource: https://github.com/openimagingdata/findingmodel/tree/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/anatomic-locations
    title: The anatomic-locations package, version 0.2.5, its runtime model, index and command line
  - id: fm-doc
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/docs/anatomic-locations.md
    title: Anatomic locations usage document, findingmodel
  - id: fm-normalized
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/tasks/done/anatomic-locations-normalized-schema.md
    title: Rich anatomic location DuckDB with relationships, the plan that designed the normalized model, completed 2025-12-31
  - id: al-libs
    resource: https://github.com/talkasab/BodyPartIndex.py/blob/388ae0a6da92f5ee4cf36620bbeeabe223938471/README.md
    title: BodyPartIndex.py README, the Python wrapper library, last commit 2024-02-03; companion TypeScript library at BodyPartIndex.ts dec578e1, 2022-12-18
  - id: cde-anatomy-axis
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/11-anatomy-axis.md
    title: The Anatomy Axis, Current State, ACR-RSNA-CDEs next-gen-2026 branch, dated 15 September 2026
  - id: cde-understanding
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/00-current-understanding.md
    title: Current Understanding, ACR-RSNA-CDEs next-gen-2026 branch, the laterality and substrate statements
  - id: cde-alpha
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/12-alpha-structural-comparison.md
    title: Alpha structural comparison, ACR-RSNA-CDEs next-gen-2026 branch, open decision areas ST06 and ST08
  - id: radlex-issue
    resource: https://github.com/RSNA/RadLex/issues/3
    title: "RSNA RadLex issue 3, Add Anatomic Locations, opened 2026-08-10, open"
  - id: radlex-skill
    resource: https://github.com/RSNA/RadLex/blob/5162a65db531c8170139656f8a8ed27d96b6dd20/.claude/skills/radlex-concepts/SKILL.md
    title: The radlex-concepts skill, the two-phase extract and propose loop with its validation rules
  - id: radlex-suggest
    resource: https://github.com/RSNA/RadLex/blob/5162a65db531c8170139656f8a8ed27d96b6dd20/.pi/skills/suggest-new-concepts.md
    title: The suggest-new-concepts skill, acceptance rules for a proposed concept
---


# What the index is

The [anatomic location](/glossary/anatomic-location.md) index is a curated set of anatomic entities, each keyed by a [RadLex identifier](/glossary/radlex-id.md) and placed in a spatial containment hierarchy. The manuscript under review describes it as a reference and normalization layer, not an automatic labeling algorithm. An identifier may be applied at the examination or series level for the anatomy covered, or at the finding level for where an observation is. Labels may be assigned by hand or generated by rules, language processing, or AI and then normalized, and whatever the route, a person or a downstream check confirms the structure before anything relies on it. The same source states the limit: knowing where a finding is does not establish what kind of process it is, how long it has been present, or whether it is the same lesion recorded elsewhere.[^jdim-al]

How a finding acquires its location is a Data Structures question, covered in [anatomic location assignment rules](../data-structures/anatomic-location-assignment-rules.md).

# Why a curated set

The project site, unchanged since January 2023, argues qualitatively that ontologies holding anatomic terms are poorly suited to underpinning interoperability: too few desired terms, too many unnecessary or degenerate ones, limited anatomic organization. Its approach was to curate a subset of them, starting from [RadLex](/glossary/radlex.md) terms previously recognized in radiology reports.[^al-site]

The manuscript under review replaces that assertion with a measurement. It counts, for [SNOMED CT](/glossary/snomed-ct.md), [FMA](/glossary/fma.md), and RadLex, how completely each populates the containment or part-whole relation it declares, measuring each against its own anatomy term set so no resource is penalized for its coverage. In none of the three can software follow the declared relations from a structure up to a whole-body class, even when every declared relation, its subproperties, and the reversed forms of its inverses are pooled. The stated interpretation is not that the resources are defective but that none was built to answer what encloses the structures radiologists name. The manuscript measures no downstream utility and asks to be read as a descriptive resource paper.[^jdim-al]

# Identity and codes

A location's identifier is its RadLex identifier. The next-generation vocabulary work states the consequence directly: a RadLex code is never listed beside a location, because the location code is the RadLex code.[^cde-anatomy-axis]

In the current curated data, all 2,926 records carry an identifier, a description, a [body region](/glossary/body-region.md), and a containment parent. SNOMED CT concept identifiers appear on 1,782, ACR Common identifiers on 2,025, a further code list of FMA, MeSH, and [UMLS](/glossary/umls.md) entries on 1,750.[^fm-data]

Which SNOMED CT concept to use is a written rule, not a matter of judgment. SNOMED CT carries a Structure-Entire-Part triple for anatomy, and the field reference instructs a curator to always take the "Structure of ..." concept and never the "Entire ..." or "... part" forms, because that is what SNOMED CT intends for finding sites and procedure sites. Where a lateralized code does not exist, the unsided code serves all three entries and the substitution is noted in the change description. Definitions prefer authoritative sources in order: Fleischner Society for thoracic anatomy, then RadLex, MeSH, FMA.[^fm-fields] Lookup, sampling, and validation scripts ship beside the reference.[^fm-skill]

# Containment: one parent, up to the whole body

Every structure has exactly one containing parent, the smallest anatomic entity that encloses it. A structure spanning several subregions takes the smallest region containing the whole of it, so the pancreatic duct is contained by the pancreas rather than by the head, body, neck, tail, or uncinate process individually. The manuscript reports that every chain was verified to reach one root, the whole body, that the longest chain is seven hops, and that the largest share of entries sits at depth three. It records the cost as a limitation: a structure spanning sibling subregions is assigned to their common parent, so the pancreatic duct's course through the subdivisions is not represented, and the grouping is deliberately coarse.[^jdim-al] The project site states the same tree rule publicly.[^al-site]

# Containment is not part-of

Where a structure physically sits and what functional structure it belongs to are different questions, kept in separate fields. The curation guidance tells an editor which to use: the containment reference for "X is inside Y", as the hilum is inside the lung, and the part-of reference for "X is a component of Y", as the stomach is a part of the gastrointestinal tract.[^fm-fields] The manuscript gives the abdominal aorta as the worked case, contained by the retroperitoneum and part of the aorta, and states that the single-parent constraint applies only to containment: a structure may hold zero, one, or more [part-of](/glossary/contained-by-and-part-of.md) associations. The release it describes carries 991;[^jdim-al] the current data carries 1,123.[^fm-data] The next-generation vocabulary work leaves open which hierarchy a given check walks; it must be stated each time.[^cde-anatomy-axis]

# Laterality as explicit triads

Left, right, and unsided variants of a bilateral structure are three distinct entries joined by explicit links, rather than one entry plus a modifier. The unsided entry links to both sided variants; each sided entry links to its counterpart and back to the unsided form; and a sided entry's container points at the sided version of its container where one exists.[^fm-laterality] The manuscript states the reason as an implementation convenience, since the links permit deterministic navigation among corresponding forms without reconstructing a post-coordinated expression at runtime, and reports complete triads for all 795 bilateral structures.[^jdim-al]

The next-generation vocabulary work draws a consequence: laterality is carried by the location rather than by a data element, so there will be no laterality data elements.[^cde-understanding] An external reviewer's alpha implementation instead defines a laterality data element including a bilateral value. The difference is recorded as an open decision area, and the alpha acknowledges that a bilateral value does not resolve whether a report describes one entity or two.[^cde-alpha]

# Synthetic post-coordinated terms

Where a clinically routine localization concept has no pre-coordinated RadLex term, almost always because laterality or enumeration is missing, an identifier is minted by joining existing RadLex identifiers with an underscore, keeping the composition transparent and machine-readable.[^fm-laterality] The manuscript reports three patterns covering all of them: laterality only, 730 terms; enumeration only, 86; enumeration plus laterality, 194, most often for numbered or bilateral structures. Two qualifications accompany the count: it is not evidence that established ontologies lack mechanisms for adding concepts, since the gaps are specific to one lexicon; and systems built on RadLex will not recognize the compound identifiers without an added mapping layer.[^jdim-al] The next-generation vocabulary work names them as the exception the RadLex track will remove by minting real identifiers.[^cde-anatomy-axis]

# An overlay on RadLex, and terms contributed back

The relationship to RadLex is stated as an overlay, not a competitor: RadLex concepts and predicates sit underneath, and the file adds identifiers RadLex lacks, its own two hierarchies, and laterality. The next-generation vocabulary work records this as agreed on 13 September 2026, and states why work proceeds against the file rather than the published RadLex release: the RadLex anatomy track is editing the file, so aiming at the published release is described as editing a three-year-old version of a document others have been editing. The data is pointed to at a pinned commit, not copied.[^cde-anatomy-axis] The manuscript describes incorporation by the RSNA RadLex Committee as underway, covering the terms, and notes that a process for revising and reviewing the hierarchy still needs definition.[^jdim-al] The RadLex repository carries an open issue whose exit criterion is complete coverage of the anatomic locations terminology in RadLex.[^radlex-issue]

Gaps found while using a terminology are fed back rather than patched locally. The RadLex repository's concept skill implements this in two phases. An agent first matches findings in report text to existing concepts, under the rule that a loose keyword overlap is not enough and a broader or related concept does not count as a match. For each unmatched term it proposes a new concept with the closest existing parent, a precise term, a rationale for why the gap is genuine, and typed relationships only where a real existing identifier was found for the other end.[^radlex-suggest] Proposals are validated before anything is written, and a batch fails as a whole.[^radlex-skill] Separately, the next-generation vocabulary work feeds node requests upstream: lung parenchyma, perirenal space and its sided forms, pericardial space, subarachnoid space, and real identifiers for the compound sided variants.[^cde-anatomy-axis]

# What the index does not carry

The curated set has containment and part-of but no taxonomic relation and no structure-type nodes, so a statement such as "this finding applies to tendons" cannot be made. The next-generation vocabulary work records this as the major shortcoming for that effort and the first thing to resolve. RadLex could supply a first layer without inventing anything, since every plain-identifier location has a taxonomic chain in the published ontology, yielding several hundred locations under each of muscle, artery, vein, tendon, and bone. Two cautions accompany it: RadLex warns that some taxonomic categorizations were converted from part-of and may be wrong, and the deep formal chain is not the clinically useful layer. The same document names two scope families, tissue types and structure types, with their connections to the location hierarchy still open, and separates them from exploratory ideas marked not adopted.[^cde-anatomy-axis]

# Stated direction: enrichment from FMA

The SIIM 2026 talk shows the anatomic location axis as a kidney field table: identity, classification, the two hierarchies, laterality variants, codes. A group of rows is marked defined but not yet populated, under FMA enrichment going forward: definitions imported from FMA under a Creative Commons license, references, new edges for branch-of, bounded-by, and adjacent-to, enumeration updates splitting organ from organ part and adding "Back" to the region list, and a location type recorded as "organ (next-gen; was 'structure')".[^siim2026]

# Two dated implementations

Two implementations coexist; the later one is current.

| | The 2022 to 2024 set | The current package |
|---|---|---|
| Data | `body_parts.json`, 2,890 nodes, release 1.0.0-rc.1, site unchanged since January 2023[^al-site] | `anatomic_locations_noembed.json`, 2,926 records, inside `findingmodel`[^fm-data] |
| Libraries | Python and TypeScript wrappers over the JSON file, last commits 2024-02-03 and 2022-12-18[^al-libs] | One Python package, version 0.2.5, with a command line[^fm-package] |
| Status | Superseded as the working substrate on 2026-09-13[^cde-understanding] | The substrate the next-generation vocabulary points at, pinned to a commit[^cde-anatomy-axis] |

Entity counts differ by release and are not reconciled: 2,890 in the published file, 2,891 in the manuscript, 2,926 in the current data.[^al-site][^jdim-al][^fm-data]

The current package resolves a location by identifier, description, synonym, or external code, walks both hierarchies, filters by region and by the classification fields, and searches by combining full-text and vector retrieval.[^fm-package][^fm-doc] It precomputes containment and part-of paths, so ancestry and containment tests become string comparisons rather than recursive queries, a design written as a plan completed on 2025-12-31.[^fm-normalized] Tooling belongs to the SDKs pillar; see [SDKs](./sdks.md).

[^jdim-al]: Anatomic Locations Index manuscript, under review at the Journal of Digital Imaging and Informatics in Medicine, 2026
[^siim2026]: SIIM 2026 annual meeting talk, June 2026, Mass General Brigham
[^al-site]: Anatomic Locations project site homepage, January 2023
[^fm-data]: anatomic_locations_noembed.json, the current curated set
[^fm-fields]: Anatomic locations source JSON field reference, findingmodel
[^fm-laterality]: Laterality conventions, findingmodel
[^fm-skill]: The manage-anatomic-locations skill, findingmodel
[^fm-package]: The anatomic-locations package, findingmodel
[^fm-doc]: Anatomic locations usage document, findingmodel
[^fm-normalized]: Rich anatomic location DuckDB with relationships, findingmodel
[^al-libs]: BodyPartIndex.py and BodyPartIndex.ts READMEs
[^cde-anatomy-axis]: The Anatomy Axis, Current State, ACR-RSNA-CDEs next-gen-2026
[^cde-understanding]: Current Understanding, ACR-RSNA-CDEs next-gen-2026
[^cde-alpha]: Alpha structural comparison, ACR-RSNA-CDEs next-gen-2026
[^radlex-issue]: RSNA RadLex issue 3, Add Anatomic Locations
[^radlex-skill]: The radlex-concepts skill, RSNA RadLex
[^radlex-suggest]: The suggest-new-concepts skill, RSNA RadLex
