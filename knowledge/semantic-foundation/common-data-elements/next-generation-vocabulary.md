---
type: Concept
title: Next-generation CDE vocabulary
description: What the next-gen-2026 branch of the ACR-RSNA-CDEs repository defines, covering the working vocabulary, the graph shape, the anatomy axis, the display grammar, and the alpha implementation, recorded as in-progress design work in an allied project.
tags: [semantic-foundation, cde, next-generation, graph, radlex, allied-project]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T18:00:00Z }
sources:
  - id: context
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/CONTEXT.md
    title: CDE vocabulary, the working glossary at the root of the next-gen-2026 branch
  - id: doc00
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/00-current-understanding.md
    title: Next-Generation CDE Schema, Current Understanding
  - id: doc03
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/03-draft-structures.md
    title: Draft Structures for Worked Examples, the node and edge catalog
  - id: doc04
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/04-anatomy-gaps.md
    title: Anatomic Locations Gaps and Node Requests
  - id: doc06
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/06-next-steps.md
    title: Next Steps and Open Threads
  - id: doc07
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/07-relationship-family.md
    title: The Finding and Diagnosis Relationship Family
  - id: doc09
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/09-mat-and-tree.md
    title: The Mat and the Tree, the display grammar
  - id: doc11
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/11-anatomy-axis.md
    title: The Anatomy Axis, Current State
  - id: alpha-shape
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/alpha/SHAPE.md
    title: The shape of the knowledge graph, generated from the alpha build of 2026-09-14
  - id: alpha-readme
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/alpha/README.md
    title: RadElement next-generation alpha, anatomy architecture and rebuild instructions
  - id: oifm-v2
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/oifm-schema-v2-draft.md
    title: FindingModel Source Schema v2 Draft, a copy of the upstream gist
  - id: plan
    resource: /plans/2026-09-20-knowledgebase-build-plan.md
    title: Knowledgebase build plan, which places these ideas in the roadmap for finding models and the Imaging Problem List
---

# What this document is

A redesign of the ACR and RSNA [common data element](/glossary/cde.md) model is being drafted on the `next-gen-2026` branch of `RSNA/ACR-RSNA-CDEs`. This document records what that branch defines, read at commit `44836c1` of 2026-09-15.

It is in-progress design work in an allied project. It is not an Open Imaging Data Model (OIDM) specification, it has no open pull request, and its own root glossary says the definitions "express our current ideas ... not a jointly settled integration model."[^context] Nothing here is implemented in any OIDM repository. It is documented because the ideas are named as direction for OIDM's own next steps.

The branch's working documents state the framing plainly: the project defines the **vocabulary** of radiology results, meaning the terms available for saying what was seen and how it is characterized, and not the **grammar** by which an individual result is assembled. The grammar comes from the IHE Imaging Diagnostic Report profile.[^doc00] See [IHE IDR alignment](/data-structures/ihe-idr-alignment.md).

# The working vocabulary

The branch keeps a root `CONTEXT.md` defining the terms in use. Each definition below is quoted or condensed from it.[^context]

| Term | Definition |
|---|---|
| [DataElement](/glossary/data-element.md) | "A categorical descriptor whose permissible values may be ordered or unordered." Semantic ordering is explicit and distinct from display order |
| Categorization | A distinction expressed either by a categorizing DataElement or by a taxonomy of named classes, "not both for the same distinction in the same model" |
| [Measurement](/glossary/measurement.md) | "A quantitative descriptor, distinct from a DataElement." Its measurement method is optional and unspecified by default |
| [Element binding](/glossary/element-binding.md) | A relationship connecting a definition to a DataElement it uses. A binding may restrict the use to a subset of the element's permissible values "without changing the shared element or its other bindings" |
| Selection cardinality | The permitted number of values selected for a DataElement in a use, such as single or multiple selection. Distinct from value ordering and from component counts |
| Modality applicability | The modalities on which a finding can be seen or a descriptor evaluated. A descriptor's intrinsic limit "is distinct from its binding-specific applicability and is not an overridable default" |
| Unspecified modality applicability | Omission alone "means neither applicability to every modality nor exclusion from every modality" |
| [AssessmentScheme](/glossary/assessment-scheme.md) | A distinct definition of an assessment system whose descriptive dimensions are ordinary DataElements linked to the scheme |
| [AnatomicLocation](/glossary/anatomic-location.md) | An anatomical reference identified by its [RadLex identity](/glossary/radlex-id.md), able to bind directly to DataElements and Measurements without a FindingClass |
| Component-of scope | The finding classes a component class belongs inside, stated on the component class. "A class with a component-of scope is never reported on its own" |
| Lesion family | A group of related lesion types, usually specific to a location. Component classes are lesion-family specific |
| Standard clinical metadata | "The seven facts on a class: modality, body region, subspecialty, sex, age, time course, and etiology" |
| [Anatomic scope](/glossary/anatomic-scope.md) | The eligible anatomical places, tissue types, or structure types for a definition. A plain list matches any one target by default |
| Anatomy scope specifier | A concept used to identify eligible anatomy. How the families connect to the location hierarchy "remains open" |
| Tissue-type scope | A scope family exemplified by pulmonary parenchyma, hepatic parenchyma, and subcutaneous fat |
| Structure-type scope | A scope family exemplified by solid organs, vessels with artery and vein subtypes, muscles, tendons, and ligaments |

Neither scope family, the glossary notes, by itself prescribes a separate graph node type.[^context]

# The graph shape

The model is a graph rather than a document format. Nodes carry only scalars; everything shared is a node, and everything pointing at something shared is an edge. Flat text forms are serializations of the graph, not the model.[^doc03]

[FindingClass](/glossary/finding-class.md) and Diagnosis are separate node types. The branch records the separation as a structural decision, and the relationship documents state what is left to distinguish them: with one unrestricted taxonomy spanning both labels, the only structural difference is which relationship types a node can source.[^doc07] A third negative-only node type, Grouping, exists so that a statement such as "no renal abnormality" has something to point at.[^doc03]

Relationships are explicit and typed, and each carries its own identifier so that a report-level assertion can cite the standing potential it expresses.[^doc03] Eight relationship pairs plus a catch-all make up the finding and diagnosis family.[^doc07]

| Relationship | Character |
|---|---|
| `SUBTYPE_OF` | Taxonomy. Never propagates another outgoing edge |
| `MAY_HAVE_COMPONENT` | Compositional. The target occurs as a described sub-part |
| `MAY_CAUSE` | Causal. The source produces the target as a distinct second entity |
| `MAY_MANIFEST_AS` | Evidential. The diagnosis shows itself as the target |
| `OCCURS_WITH` | Symmetric association, asserting nothing about cause or sequence |
| `MAY_PROGRESS_TO` | Temporal. Identity-preserving evolution |
| `ASSESSED_BY` | Interpretive. A standardized scheme applies to the source |
| `MAY_BE_RELATED_TO` | Symmetric catch-all, "a triage queue, not a home" |

Keeping manifestation and causation apart is the load-bearing distinction. Manifestation is constitutive: a striated nephrogram is pyelonephritis appearing on imaging, not a second disease. Causation is consequential: a renal abscess is a new thing pyelonephritis made. The stated test is whether a clinician would say the source "got better" or that "a complication resolved."[^doc07]

Manifestation edges carry two optional, independent properties. **Typicality** adopts the HPO and Orphanet frequency scale verbatim, with its percentage anchors, from `obligate` at 100 percent down to `very_rare` at 1 to 4 percent and `excluded` at zero. **Specificity** has three ordered values, `pathognomonic`, `highly_suggestive`, and `suggestive`, and is omitted entirely when no judgment is recorded.[^doc07]

The **differential is a derived view, not an edge**. It is computed by traversing the manifestation relation from a finding to the diagnoses that can produce it, filtering by context edges such as age stage, modality, and anatomic scope, and ranking by specificity then typicality. No `DIFFERENTIAL_OF` edge type exists. The cited precedent is the [Radiology Gamuts Ontology](/glossary/gamuts.md), which derives every differential from is-a and may-cause links alone.[^doc07]

# The anatomy axis

RadLex is the substrate. The branch's position, recorded in its anatomy summary, is that the anatomic locations data behind the published `anatomic-locations` package, 2,926 locations each keyed by a RadLex identifier, is **an overlay on RadLex**, not a replacement and not the sole source, and is **the basis of the RadLex anatomy axis going forward**, because the RadLex anatomy track is editing it rather than the published release.[^doc11] The file is pointed at and pinned to a commit, not copied. A location's identifier is its RadLex identifier, and no separate RadLex code is written beside it.[^doc11]

A gap log tracks what the overlay cannot yet express and what should be requested upstream.[^doc04] The major shortcoming is recorded as the absence of any is-a relation over locations and the absence of structure-type nodes, so a scope statement of the form "applies to tendons" cannot currently be made. The log's running node request list names lung parenchyma, perirenal space with its sided forms, pericardial space, subarachnoid space, and real RadLex identifiers for the 1,016 compound sided variants the file mints locally.[^doc04] An interim layer derived from RadLex 4.3's own is-a hierarchy is proposed to cover the gap until the overlay ships one.[^doc11]

See [RadLex integration](/semantic-foundation/anatomic-locations/radlex-integration.md) and [lineage and current implementation](/semantic-foundation/anatomic-locations/lineage-and-current-implementation.md) for the OIDM side of the same data.

# The display grammar

The branch specifies two generated pictures, both deterministic SVG built from the canonical graph.[^doc09] The **mat** is the view of one context object one hop out: the object is drawn in full with a fixed card frame of seven zones, a title line with name and identifier, an anatomy line, definition and synonyms, an attribute table, dotted containers each labelled with one relationship read from the context object's side, a mappings line of external codes with their preferred terms, and a bottom stat row of seven fixed cells for modality, region, subspecialty, sex, age, course, and etiology; everything connected to the object arrives as a mini-card inside the relevant container, edges carrying typicality or specificity draw as a dotted box around the mini-card with those values on its bottom border, and there are no wires or arrowheads at all, because containment replaces them. The **tree** is the zoomed-out is-a view of a family: one mini-card per row, indented by subsumption, rooted at a grouping node, with a click layer on the site that boxes every related card. The stated reason for both is that the committee approving the vocabulary is made of radiologists, so a picture earns its place when one of them can look at a real clinical family and either agree or point at what is wrong.[^doc09]

# The alpha implementation

An alpha implementation contributed by a collaborating reviewer sits under `docs/next-gen-schema/alpha/` and is treated as an external subtree by the branch's own bundle checker. Its generated shape documentation, built on 2026-09-14, reports a definition graph of **347 nodes and 758 edges** across eleven node types.[^alpha-shape]

| Node type | Count |
|---|---:|
| Value | 155 |
| FindingClass | 45 |
| DataElement | 36 |
| AnatomicLocation | 28 |
| Diagnosis | 25 |
| Subspecialty | 19 |
| Measurement | 16 |
| Etiology | 10 |
| Modality | 7 |
| AssessmentScheme | 5 |
| AnatomicRefinementRule | 1 |

The 45 FindingClasses compile to flat JSON shapes with references resolved, which the shape document names as the vendor-facing deliverable; the OWL serializations are described as a design-time checking instrument rather than something consumers reason over. The document states directly that "there are no instances."[^alpha-shape] The alpha's README states that RadLex is the single source of truth for anatomy, that the generated ontology imports the configured RadLex release directly, and that the model creates no parallel CDE anatomy hierarchy and no CDE replacements for RadLex anatomy predicates; it was built and verified against RadLex release 4.3.[^alpha-readme] The branch's handoff document names the alpha as the foundation for the work going forward and lists resolving structural differences, anatomic locations first, as the active direction.[^doc06]

# A stated direction for finding models

The branch's `notes/` directory carries a copy of a FindingModel source schema version 2 draft, dated 2026-04-20 and marked "a proposed authoring schema, not an implementation-complete contract yet."[^oifm-v2] It proposes splitting a [finding model](/glossary/finding-model.md) into a source file and a hydrated output, moving shared attributes such as presence and change from prior into canonical attribute files that a source model references instead of redefining, storing only the authored side of a relationship and deriving inverses from a relationship-type registry, and adding a quantity-kind registry and per-model history sidecars.

The relationship documents note that this registry exists only in the version 2 draft, and that the live `findingmodels` repository implements no relationship mechanism at all.[^doc07] The draft is a stated direction, not a shipped format.

# Why this matters for OIDM

The knowledgebase build plan places these ideas in the roadmap rather than in the specification: the relationship and graph ideas from this CDE work are listed among the inputs to the finding model format evolution roadmap, alongside the canonical metadata rewrite and schema versioning, and the Imaging Problem List data model work is tracked separately as its own roadmap entry.[^plan] See [finding model format evolution](/roadmap/finding-model-format-evolution.md) and [the Imaging Problem List data model system](/roadmap/ipl-data-model-system.md).

Three points of contact are concrete today. The vocabulary terms above are already in this knowledgebase's [glossary](/glossary/index.md), because OIDM documents use several of them. The anatomy overlay named as the basis of the RadLex anatomy axis is OIDM's own anatomic locations data. And the finding model schema version 2 draft is an OIDM artifact circulated in the CDE work, not a CDE artifact.

[^context]: CDE vocabulary, the working glossary at the root of the next-gen-2026 branch
[^doc00]: Next-Generation CDE Schema, Current Understanding
[^doc03]: Draft Structures for Worked Examples, the node and edge catalog
[^doc04]: Anatomic Locations Gaps and Node Requests
[^doc06]: Next Steps and Open Threads
[^doc07]: The Finding and Diagnosis Relationship Family
[^doc09]: The Mat and the Tree, the display grammar
[^doc11]: The Anatomy Axis, Current State
[^alpha-shape]: The shape of the knowledge graph, generated from the alpha build of 2026-09-14
[^alpha-readme]: RadElement next-generation alpha, anatomy architecture and rebuild instructions
[^oifm-v2]: FindingModel Source Schema v2 Draft
[^plan]: Knowledgebase build plan
