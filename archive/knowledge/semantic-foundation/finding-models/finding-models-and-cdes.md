---
type: Concept
title: Finding models and common data elements
description: "The workbench relationship: finding models as fast exploratory definitions that can graduate into governed ACR and RSNA common data elements, and the vocabularies both have to fit."
tags: [semantic-foundation, finding-models, cde, radelement, concept]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
sources:
  - id: deck
    resource: https://gamma.app/docs/Open-Imaging-Data-Model-2026-Status-Update:-Realizing-Object-Oriented-Imaging-Results-yfxzx4q9zssafal
    title: "Open Imaging Data Model 2026 Status Update: Realizing Object-Oriented Imaging Results, January 2026"
  - id: site-post
    resource: https://www.openimagingdata.org/findings-cdes-and-observations/
    title: "Findings, CDEs, and Observations, openimagingdata.org, 2023-06-24"
  - id: ids-json
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/ids.json
    title: ids.json, the identifier registry, findingmodels main branch
  - id: example
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/defs/cervical_rib.fm.json
    title: cervical_rib.fm.json, a CDE-sourced finding model, findingmodels main branch
  - id: staging-readme
    resource: https://github.com/openimagingdata/CDEStaging/blob/main/README.md
    title: CDEStaging README
  - id: staging-extraction
    resource: https://github.com/openimagingdata/CDEStaging/blob/main/docs/report_extraction_process.md
    title: Report extraction process, CDEStaging repository
  - id: cde-context
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/CONTEXT.md
    title: CDE vocabulary, CONTEXT.md, ACR-RSNA-CDEs next-gen-2026 branch
  - id: idr-extract
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/notes/ihe-idr-extract.md
    title: IHE IDR Phase II extract for the CDE vocabulary, ACR-RSNA-CDEs next-gen-2026 branch
  - id: cleanup-plan
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/docs/plans/definition_cleanup.md
    title: Definition Cleanup Plan, findingmodels main branch
---

# The workbench

Most people meet these two things in the wrong order and assume that a [finding model](/glossary/finding-model.md) is a lightweight copy of a [common data element](/glossary/cde.md). The relationship runs the other way.

The January 2026 status deck gives the framing a name. Under the heading "OIFM: the CDE workbench" it describes finding models as offering "rapid innovation and a proving ground, ahead of ACR and RSNA CDE adoption," providing "programmatic knowledge" as ground-level information for tools and for language model context, and carrying "exploratory metadata," meaning "rich definitions with embedded relationships and semantic tags that can graduate to standards." The executive summary calls the same idea the "workbench effect": language-model-powered, high-velocity content creation acting as a proving ground for formal common data elements.[^deck]

Two properties make this work. Finding models are cheap to create, because the authoring path described in [the authoring workflow](/semantic-foundation/finding-models/authoring-workflow.md) is largely machine-assisted. And they are ungoverned, because nobody has to approve one before it exists. A corpus of 2,382 definitions accumulated in a few years, which no committee process could have produced in that time.

The cost is the mirror image. A finding model carries no governance, no review record, no version, and no commitment that it will not change. That is exactly what a common data element supplies and what makes the graduation direction the useful one.

# Where common data elements live

[RadElement](/glossary/radelement.md) is the published home, operated by the RSNA and the ACR. Its content is organized as [CDE sets](/glossary/cde-set.md) with identifiers of the form `RDES###` and [CDE elements](/glossary/cde-element.md) with identifiers of the form `RDE####`. A set names a finding type; its elements name the attributes of that finding.

That pairing predates the finding model format. The 2023 site post states the original idea directly: "Radiology findings can be represented in a standard format based on FHIR Observations semantically labeled with ACR/RSNA Common Data Element identifiers," with the set identifier naming the observation type and element identifiers naming the individual attributes. Its worked example encodes "solid nodule measuring 6 mm in the right lower lobe" as an Observation coded `RDES195` for pulmonary nodule, with components for composition, size, and location.[^site-post] The deeper treatment of the vocabulary itself is in [common data elements and RadElement](/semantic-foundation/common-data-elements/cdes-and-radelement.md).

# How common-data-element content came into the corpus

115 of the 2,382 finding models carry the organization code `CDE`, meaning they were derived from ACR and RSNA common data element content.[^ids-json] They are the second-largest non-Gamuts source after OIDM's own definitions, and they make the mechanism visible. A CDE-derived model is an ordinary finding model with an `Organization` contributor naming the ACR/RSNA Common Data Elements Project and an [index code](/glossary/index-code.md) in the `RADELEMENT` system pointing back at the set it came from.[^example]

```json
"contributors": [
  { "name": "ACR/RSNA Common Data Elements Project", "code": "CDE", "url": "https://radelement.org/" }
],
"index_codes": [
  { "system": "RADELEMENT", "code": "RDES101", "display": "cervical rib" }
]
```

That index code is the join. A stored [Observation](/glossary/observation.md) citing an OIFM identifier can be resolved to a RadElement set identifier by reading the definition, which is what lets a finding-model-based pipeline emit common-data-element-labeled output.

Importing in this direction has costs that the corpus is still paying. The definition cleanup plan records that the imported CDE and MGB models use title case where the conventions call for lowercase, and that 124 models, mostly CDE-derived, lack [presence](/glossary/presence.md) as their first attribute because the source content jumped straight to clinical attributes. It also flags a category of CDE entries that are measurement protocols or scoring systems rather than observations, which "don't have presence/absence because they're not observations, they're quantification tools," and marks them for reclassification.[^cleanup-plan]

# The informal staging path

Between an idea and a RadElement submission sits `CDEStaging`, which describes itself as "a staging area for definitions of radiology common data elements (CDEs) in JSON format... prior to their entering the review pipeline."[^staging-readme] It holds 259 informally authored definitions in two coexisting markdown conventions, contributed from several sources, and is profiled in [CDE staging](/semantic-foundation/common-data-elements/cde-staging.md).

Its role relative to finding models is real but undocumented as a process. The repository's own extraction-process note observes the need to align finding, attribute, and value names with the finding definitions, and works an example converting report language into what it calls "mini-observations," each a finding with an attribute and a value.[^staging-extraction] No document in that repository describes an automated route between staging, RadElement, and the finding model corpus. What exists instead is traffic: the largest in-flight content batch in `findingmodels`, on `content/chestcts`, converts CDEStaging chest CT source material into finding models, and an open issue asks for the rest of the staging markdown content. Staged definitions are being consumed as finding model source material as well as being pushed toward RadElement.

# What the next generation adds

Work on the `next-gen-2026` branch of the `ACR-RSNA-CDEs` repository is redesigning the common data element vocabulary itself. It introduces a separation between a [finding class](/glossary/finding-class.md) and a diagnosis, a [data element](/glossary/data-element.md) distinct from a [measurement](/glossary/measurement.md), explicit [element bindings](/glossary/element-binding.md) that let a class restrict a shared element to a subset of its values, [assessment schemes](/glossary/assessment-scheme.md) as first-class definitions, and an [anatomic scope](/glossary/anatomic-scope.md) axis anchored on RadLex.[^cde-context] Its working vocabulary is explicit that these express "our current ideas for the reviewer's foundation, not a jointly settled integration model." The full account is in [the next-generation vocabulary](/semantic-foundation/common-data-elements/next-generation-vocabulary.md).

Several of those distinctions have counterparts in the finding model work, which suggests the two are converging on the same problems from opposite ends. The finding-versus-diagnosis split is the most important axis in the structured metadata rewrite's `entity_type` field. Measurement and assessment appear there as entity types too. Shared, bindable elements are what the finding model format does not have: every attribute belongs to exactly one finding, which is why the corpus holds 5,709 attribute identifiers for 2,382 findings and why presence is redefined 2,382 times.

# The grammar both have to fit

Whatever either vocabulary settles on has to serialize into the representation that implementers are being asked to build. The IHE Imaging Diagnostic Report Phase II public-comment draft is that target, and an extract of it on the CDE branch reads it as "the grammar this vocabulary must fit."[^idr-extract]

The draft splits an observation into a target entity and content, with anatomy in a body structure field "fully pre-coordinated except for the laterality," laterality separate, the pathologic entity in a morphology field that "shall not unnecessarily pre-coordinate the associated anatomy," the property in the observation code, and the value alongside. It states a preference that lands directly on this relationship: when encoding CDE sets from RadElement, "it is preferred to use the CDE Set code here," such as `RDES195` for pulmonary nodule, with the set's elements referenced as members.

That preference is for common data element codes, not OIFM codes. A finding model that has not graduated has no set identifier to put in that slot. This is the practical reason the graduation path matters rather than a matter of standards etiquette, and it is worked through in [IHE IDR alignment](/data-structures/ihe-idr-alignment.md).

The extract also flags a vocabulary collision worth carrying: in the draft, a "finding" is the determination that something is present or absent, and an "observation" is a characteristic visible in an image. Both terms mean something else in OIDM. The [glossary](/glossary/) records which sense this knowledgebase uses.

[^deck]: Open Imaging Data Model 2026 Status Update, January 2026
[^site-post]: "Findings, CDEs, and Observations", openimagingdata.org, 2023-06-24
[^ids-json]: ids.json, findingmodels main branch
[^example]: cervical_rib.fm.json, findingmodels main branch
[^staging-readme]: CDEStaging README
[^staging-extraction]: Report extraction process, CDEStaging repository
[^cde-context]: CDE vocabulary, CONTEXT.md, ACR-RSNA-CDEs next-gen-2026 branch
[^idr-extract]: IHE IDR Phase II extract, ACR-RSNA-CDEs next-gen-2026 branch
[^cleanup-plan]: Definition Cleanup Plan, findingmodels main branch
