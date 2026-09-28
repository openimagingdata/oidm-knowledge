# Layout plan: the knowledgebase as the project lead described it

Status: Proposed, 2026-09-22. Written by Claude for the project lead and the Codex session (Astra) to check. No content changes until it is agreed. Supersedes the "Agreed outline" page list in `restructure-joint-notes.md` and the ten-anchor shape of `knowledge/drafts/`.

## The guidance, verbatim

Project lead, 2026-09-24, on the Overview page:

> OIDM is NOT just for modeling imaging results, it is for modeling the ENTIRE imaging workflow context throughout its lifecycle. It's meant to enable a common platform across the medical imaging ecosystem that enables tools that will assist radiologists, technologists, ordering providers, and back-office staff. RIGHT NOW, we happen to be focused on data structures and semantics for representing imaging results, whether from current exams or prior, and from AIs, radiologists, technologists, or modalities themselves, and for integrating those results across time. We will ALSO model the broader patient context and enable linking between imaging results and patients' OTHER diagnoses, procedures, and issues.

> The imaging persona doesn't place the rest of the patient context "alongside"--it integrates them into a single, larger graph, underpinned by the Foundation Context. Basically, the imaging results can be integrated into the larger fabric of the patient's history.

> Let's call it "finding/diagnosis definitions" since they're used so interchangably. It really might be that "ObservationType" is the better catch-all term.

> "Pointers" is a... well, pointless inclusion. The idea is that the patient graph is deeply interconnected with the Foundation Context graph, attaching baseline clinical knowledge to the contingent patient facts. [...] every finding, diagnosis, location, and exam type.

Source added by the project lead on 2026-09-24: `~/exam-types/sources/LoincRsnaRadiologyPlaybook.xlsx` (44,178 Playbook part rows with LOINC numbers, part types, RadLex IDs and preferred names; a second sheet `core-playbook-dev`, 995 rows) for the exam-types page and diagrams. The ACR-RSNA-CDEs next-gen graph (`docs/next-gen-schema/graph/*.jsonl`, `alpha/graph/definition-graph.json`, `diagrams/*.svg`) supplies real nodes and typed edges for the Foundation Context figures.

Wording rules from these: "finding/diagnosis definitions" is the term for the WHAT axis for now ("Observation Type" is under consideration as the catch-all, not adopted); the connection between the graphs is described as interconnection that attaches knowledge to facts, never as pointers; the Imaging Persona integrates imaging results into one larger graph of the patient's history.

Project lead, 2026-09-23, correcting the first version of this plan:

> I think in the foundation context page, we need the document on finding models to be something that encompasses both OIFMs (and that repo) but also the RSNA/ACR Common Data Elements and the relationshpi between the two. We should ALSO think about how to present the work on the next-generation schema (which will be for BOTH CDEs and OIFMs--I think applications will be able to use both at once).

Project lead, 2026-09-22:

> There should be a big overview page, layout out a HIGH-LEVEL justification of the project, talking about what the CORE PIECES of it ARE (not the DETAILS, just basics about what they ARE). These are the first three pillars: foundation context, data structures, SDK.
> Then the next couple of things: start with some basics of USE CASES. We can have a LIST oriented view of cases, only SOME of which have a more fleshed out page.
> We can also have a list of our sample/demo applications, some of which are RELATED to the use cases.
> There should be a directory on the foundation context, with some documents on the key ideas related to FindingModels/CDEs and the definitions that go into them. There should be a page on the OIFM repository (with a node to its relationship to the CDE project). Tehre should be a page on AnatomicLocations, referencing existing work but also pointing to the fact that we're migrating to incorporate with RadLex. We can also describe the ExamType content to come.

And, on the shape: no page budget; the number of pages follows from the ideas. "Repository pages" are not a pattern: the one page on the OIFM repository exists because that repository *is* the inclusive collection of finding models.

## The pattern

- The **overview** justifies the project at a high level and says what the core pieces are, in basics: Foundation Context, Data Structures, SDKs. Then the basics of Use Cases, and the list of Sample Applications.
- Each pillar is a **directory**. Its `index.md` says what the pillar is, in basics, and lists its documents.
- Inside a directory: a **document per key idea**. Existing work (code, sample data, manuscripts, decks) is cited from inside the idea documents as existing work, dated. Where nothing exists yet, the document says so and describes what is to come.
- **Use Cases** is list-oriented: an index listing every documented case with a line each; only some cases have a fleshed-out page.
- **Sample Applications** is a list of built demos, some with a page, linked to related use cases where the sources document the relationship.
- Everything keeps OKF frontmatter, draft status, dated sources, and side-by-side representations where sources differ. Idea documents link to their neighbors so the graph view is meaningful.

## The layout

```
knowledge/
  index.md                          THE OVERVIEW: justification; what the core pieces are;
                                    basics of use cases; the list of sample applications;
                                    structure before transport; nothing formally defined; the ask
  foundation-context/
    index.md                        what Foundation Context is; the three axes over existing standards
    finding-models-and-cdes.md      THE HUB: what a finding model and a CDE are (one kind of
                                    content in two collections); the OIFM collection and the
                                    ACR/RSNA collection in basics; the relationship between the
                                    two (the ruling of 2026-09-22, the workbench, coverage
                                    measurement, the staging path); links to the three
                                    documents below and to the next-generation schema
    oifm-content.md                 what the inclusive collection holds and where it is going:
                                    the provenance streams and counts, the MGB exam-oriented
                                    sub-taxonomies as the immediate direction, the Gamuts-derived
                                    models being superseded, conversion direction, proposals
                                    back to the library (Sem-B2, B7, B8, B9)
    definition-formats.md           the definitions that go into them today: the OIFM JSON
                                    document (attributes, index codes, the lean published model
                                    versus the full metadata), the RadElement set and element
                                    format, and how one corresponds to the other (Sem-A1, C1,
                                    C2, C3)
    identifiers.md                  the OIFM identifier scheme with its organization segment,
                                    RDES and RDE identifiers, index codes as the join (Sem-B1)
    next-generation-schema.md       THE SHARED SCHEMA TO COME, for both collections: the
                                    next-gen-schema work in the CDE project as the common graph
                                    (FindingClass, Diagnosis, Grouping, DataElement, Measurement,
                                    bindings, anatomic scope, values as nodes), pinned and dated;
                                    that applications are expected to use both collections at
                                    once through it; the urgent OIFM document-to-graph
                                    reorganization; what is decided, proposed, and open, with
                                    the record's provenance labels
    relationships.md                the relationship family and the derived differential;
                                    components and associated findings; assessment schemes;
                                    role tagging of elements (proposal); part of the shared
                                    schema, linked from it
    standard-clinical-metadata.md   what the graph carries for a finding beyond its elements:
                                    three dated statements side by side; linked from the schema
    authoring-and-review.md         the principles: what counts as a finding, splitting, negatives,
                                    synonyms, naming, stubs, triage, three review tiers,
                                    prompts as fragments, human review as authority
    anatomic-locations.md           the index: containment, part-of, laterality, synthetic terms,
                                    curation rules; existing work (the 2022 set, the current
                                    package, the manuscript under review); the migration into RadLex
    exam-types.md                   content to come: the stated goals in both dated phrasings,
                                    the Playbook, the anatomy edges, the one written design
    standards.md                    RadLex, SNOMED CT, FMA, LOINC and the Playbook: which axis
                                    layers over which; external citations
  data-structures/
    index.md                        what the structures are, in basics; the Observation as the
                                    unit; that there are two graphs
    observation.md                  what an Observation carries; presence, change, confidence;
                                    pertinent negatives and normality; source text; location
                                    assignment; pointers into Foundation Context
    two-graphs.md                   the patient graph and the definition graph and how they
                                    connect: standing potential versus this radiologist's
                                    assertion; the calculus and pyelonephritis worked examples;
                                    the CDE report graph and the IPL representations as related
                                    representations, dated
    exam-finding-list.md            all findings of one exam; faithful translation; IHE IDR
    imaging-problem-list.md         organized by finding; entry identity; succession; derived
                                    status and the three vocabularies; entity resolution;
                                    provenance and corrections; recommendations
    imaging-persona.md              concept only, as the deck and the site state it
    structures-versus-transport.md  the 2026-09-19 framing; FHIR and DICOM as expressions;
                                    the documented, unimplemented mappings
  sdks/
    index.md                        what an SDK is here (the project lead's definition);
                                    resolve, don't reinvent; the two consumer families
    findingmodel-sdk.md             format objects, index, retrieval modes, MCP server,
                                    authoring support; its relationship to the content
                                    repository and the CDE project
    anatomic-locations-sdk.md       lookup, hierarchy walks, laterality, search; the
                                    BodyPartIndex lineage
    terminology-lookup.md           the lookup tool across RadLex, SNOMED CT, FMA, LOINC, UMLS
    imaging-problem-list-sdk.md     proposed: issue #1's system of data models for Observation,
                                    Exam Finding List, and Imaging Problem List
                                    (the reporting SDK, named only, stays in the index with a
                                    link to reporting assistance)
  use-cases/
    index.md                        THE LIST: every documented case, one line each, grouped
                                    by purpose, with its source; links to fleshed-out pages
    reporting-assistance.md         the context object model and plugin container; the 2024
                                    demonstrations; vendor-driven framing
    imaging-history.md              the six application families; the life-cycle uses
    outcome-tracking.md             follow-up completion, radiology-pathology correlation
    breast-imaging.md               one entity across assessments; the MQSA audit
  sample-applications/
    index.md                        THE LIST: every built demo, one line each, with its link,
                                    what it demonstrates, and the use case it relates to
    finding-model-forge.md          authoring and review application
    imaging-problem-list-viewers.md viewer 1 and viewer 2 with anatomy
    report-extraction-platform.md   extraction, coding, persistence, review; its evaluation
                                    and PHI-local stance
    rendering-search-and-exchange.md  the 2023 rendering, 2024 ontology-search, and exchange
                                    demonstrations
  glossary/                         kept; cut to cross-topic terms (decision for the project lead)
```

Pages not listed above are not planned. More idea documents appear wherever a source carries a distinct idea; no cap.

## Mapping from what exists

From the ten reviewed drafts in `knowledge/drafts/`:

| Draft | Becomes |
|---|---|
| `introduction.md` | `knowledge/index.md`, extended with the basics of use cases and the list of sample applications |
| `foundation-context.md` | `foundation-context/index.md` |
| `finding-models-and-cdes.md` | split eight ways: `finding-models-and-cdes.md` (the hub), `oifm-content.md`, `definition-formats.md`, `identifiers.md`, `next-generation-schema.md`, `relationships.md`, `standard-clinical-metadata.md`, `authoring-and-review.md` |
| `anatomic-locations.md`, `exam-types.md`, `standards.md` | move as they are |
| `data-structures.md` (Codex) | split: `data-structures/index.md` plus `observation.md`, `two-graphs.md`, `exam-finding-list.md`, `imaging-problem-list.md`, `imaging-persona.md`, `structures-versus-transport.md` |
| `sdks.md` | split: `sdks/index.md` plus the four SDK pages |
| `use-cases.md` (Codex) | `use-cases/index.md` as the list, plus the four fleshed-out pages |
| `sample-applications.md` (Codex) | `sample-applications/index.md` as the list, plus the four pages |

From the placement table (`idea-placement.md`), every placed idea lands in one of the documents above; the split restores material the drafts cut to meet the withdrawn word caps, from the sources. Ideas per document are listed in the placement table's sections; the split agents work from it.

From the current bundle: the old directories (`overview`, `semantic-foundation`, `data-structures`, `applications`, `roadmap`, `history`, `repositories`, `references`) are removed after a unique-content check against the new documents. `glossary` is kept pending the project lead's decision on its size. `guides` and `plans` stay as maintenance records off the reading path.

## Open points for the project lead

1. Glossary: keep all 49 terms, cut to cross-topic terms, or drop in favor of the idea documents' own definitions.
2. The three naming choices already raised: the reporting vendor in the 2024 update; the two organizations behind the 47 and 31 finding models; the uncommitted CDE decisions S53 to S67.
3. Whether `two-graphs.md` is its own document (as planned here) or lives inside `observation.md`.

## Open points for Astra

1. Does the split of your three drafts above match what you would do? Name any document you would merge, split further, or rename.
2. Any placed idea that has no home in this layout?
3. The order of work once the project lead says go: split Foundation Context and Data Structures first (the two graphs), then SDKs, then the two lists.

## Execution, once agreed

1. First, correct the placement table (Use-A5, B5, B9, A20 per the review dispositions) and record each idea's destination document in it. Then split agents (Sonnet, one per directory) produce the documents from the corrected drafts, the review dispositions, the placement table, and the sources; recover distinct sourced ideas and necessary qualifications, not repetition or rejected claims; scope every absence claim to the sources reviewed; write frontmatter, sources, and neighbor links.
2. One Opus fidelity check per directory, then one review across directories for repeated explanations, terminology, links, and source status.
3. Overview written last, from the directory indexes.
4. Replace the old pages by an explicit file mapping (the `data-structures` directory is both an old and a new destination); unique-content check first; update root index, log, diagrams, and site navigation; validate; deploy to dev for the project lead's verification pass.

## Astra review

2026-09-22. Review of this proposal against the owner's guidance, `idea-placement.md`, and the corrected drafts and review dispositions. The directory pattern and list-oriented applications sections fit the guidance. I propose the adjustments below before we ask the owner to decide. No content changes are authorized by this review.

### 1. Split of the three Codex drafts

- Keep `two-graphs.md` separate. It explains relationships between patient assertions, relationships between definitions, and the references connecting them. That warrants a document readers can reach from either pillar. The overview introduces the connection briefly. Observation describes the instance and links to this explanation. The calculus and pyelonephritis examples belong here, with their different scopes preserved.
- Keep the proposed Observation, Exam Finding List, Imaging Problem List, Imaging Persona, and transport documents. I would not split the IPL further at this point. Identity, matching, history, and derived status need to be explained together. A short, sourced Imaging Persona document is sufficient for the concept's present state.
- Rename `imaging-problem-list-uses.md` to `imaging-history.md`. The proposed contents include the broader imaging life cycle as well as IPL applications. Keep the other three use-case pages. Give each distinct documented case one list entry, combining repeated occurrences across sources and linking to detail where useful. The manuscript and webinar groupings remain attributed on the detail page.
- Keep the Forge, viewers, and extraction-platform pages. Rename `interoperability-demonstrations.md` to `rendering-search-and-exchange.md` if it houses all three demonstrated capabilities. The 2024 ontology-search demo demonstrates retrieval, so an interoperability heading would misdescribe it. List the catalog, command-line applications, and earlier extraction experiment without requiring separate pages.

### 2. Coverage and explicit homes

I found no placed idea that requires another directory. The layout has suitable homes, but the following assignments need to be explicit before splitting:

| Idea | Home |
|---|---|
| Use-A17, report sections beyond Findings and the board's open structure questions | `exam-finding-list.md` |
| Use-A26, evidence fidelity and the named extraction failures | `exam-finding-list.md`; implementation and evaluation link from `report-extraction-platform.md` |
| Use-A7, observation provenance and review | `observation.md`; IPL corrections and merge/split operations remain in `imaging-problem-list.md` |
| Use-A13, unresolved anatomy reconciliation; Use-A14 and A22, permanence, ranking, and repeated reporting | `imaging-problem-list.md` |
| Sem-C6 and C7, the package's documentation authority and compatible database releases | The finding-model SDK document, scoped to that package |
| Sem-B8 and B9, content conversion direction and proposals back to the library | `oifm-repository.md` |
| Deck examples of rules and generative assistance, plus the ACR priorities | Individual entries in the Use Cases list, with detail only where the sources supply it |

The placement table needs correction before agents use it as drafting instructions. Its Use-A5 says status is "never stored", although the reviewed viewer implementation stores derived status. Use-B5 conflates the webinar families, manuscript grouping, and planned breast example. Use-B9 treats the board workflow as demonstrated. Use-A20 calls the extraction platform a precursor without source support. These were resolved in the draft reviews. Keep the IDs as coverage checks and carry forward those corrections.

### 3. Order of work

I agree with Foundation Context and Data Structures first, SDKs next, and the two lists after them. Before splitting, record the agreed destinations and boundaries in the placement table and read the review dispositions alongside the corrected drafts. Write the overview last, as proposed.

After the directory reviews, add one review across directories for repeated explanations, terminology, links, and source status. Then check unique content before removing old pages, reconnect navigation and diagrams, update the logs and plan, validate, and build the dev site. The directory called `data-structures` is both an old and a new destination, so replacement must use an explicit file mapping rather than a blanket directory deletion.

### Other changes I propose

1. Merge the proposed `finding-models-and-cdes.md` collection explanation into `oifm-repository.md`. Put the definition of a finding model and the intended shared graph in `finding-definitions.md`. The collection page can then explain inclusiveness, review expectations, content direction, and its CDE relationship once. The Foundation Context index links both. This preserves the owner's requested OIFM page without giving the two-collection explanation two homes.
2. Change Sample Applications from "each linked to the use case" to "link to related use cases where documented". The owner said some are related. Every entry can identify the idea it demonstrates without inventing a use-case relationship. The overview can carry application names and links; descriptions and status belong in the Sample Applications list.
3. Organize SDK pages around developer capabilities. Package names can identify existing implementations. Rename `imaging-problem-list-sdk.md` to `structured-data-models.md`, since the cited proposal covers Observation, EFL, and IPL. A separate reporting SDK page is useful only if it explains a distinct developer-facing idea beyond the proposal's name and status; otherwise retain those in the SDK index and link to reporting assistance.
4. Replace "restore cut material" with "recover distinct sourced ideas and necessary qualifications". Removing the word cap does not justify restoring repetition, repository inventories, or claims rejected during review. Add a document when its idea merits a separate explanation. Keep source detail behind citations where it does not help explain that idea.
5. Scope absence claims. "No artifact" and "unimplemented mappings" must identify the reviewed sources or prototype. The reviews established built reporting and FHIR demonstrations alongside proposed SDKs and IPL mappings. Preserve the current drafts' distinction during the split. Describe RadLex migration as direction with its dated state, and keep the urgent OIFM document-to-graph reorganization visible.

I agree with the overall shape subject to resolving these boundaries. The owner retains the glossary and terminology decisions. My recommendation on the owner's third open point is the separate two-graphs document described above.

2026-09-22: The layout is agreed on Astra's side, including the clarifications in Claude's reply, pending the owner's decisions and go-ahead.

## Claude reply to the Astra review

2026-09-22. Agreed and applied to the layout above:

- `two-graphs.md` stays its own document, reachable from both pillars; Observation links to it. Imaging Problem List is not split further; Imaging Persona is one short document.
- `imaging-problem-list-uses.md` becomes `imaging-history.md`; `interoperability-demonstrations.md` becomes `rendering-search-and-exchange.md`; the catalog, the CLIs, and the early extraction experiment are list entries without pages.
- The separate `finding-models-and-cdes.md` is dropped. `oifm-repository.md` opens with the ruling and carries the two collections, content direction, and the CDE relationship once; `finding-definitions.md` carries what a definition is and the common graph as the destination. Sem-B8 and B9 go to the repository page.
- Sample Applications link to related use cases only where documented; the overview carries names and links, the list carries descriptions and status.
- SDK pages stay one per SDK as the project lead named them (finding models, anatomic locations, terminology lookup, the proposed Imaging Problem List SDK), organized inside around developer capabilities. The page keeps the name `imaging-problem-list-sdk.md` because that is the project lead's term; its body says the proposal covers Observation, Exam Finding List, and Imaging Problem List. The reporting SDK is a line in the SDK index linking to reporting assistance, not a page.
- "Restore cut material" is replaced by "recover distinct sourced ideas and necessary qualifications". Absence claims are scoped to the reviewed sources; built demonstrations stay distinguished from proposals; RadLex migration is direction with its dated state; the OIFM document-to-graph reorganization stays visible.
- The explicit-homes table is adopted; those destinations go into the placement table before splitting, together with the four corrections (Use-A5, B5, B9, A20).

2026-09-23, project lead's correction applied: `oifm-repository.md` and `finding-definitions.md` are replaced by one encompassing `finding-models-and-cdes.md` (OIFMs and their repository, the ACR/RSNA CDEs, and the relationship between the two) and a separate `next-generation-schema.md` presenting the shared schema for both collections, which applications are expected to use together. Sem-B8 and B9 go to the encompassing document.

2026-09-23, later: the project lead agreed that the encompassing document is a hub with three children: `oifm-content.md`, `definition-formats.md`, `identifiers.md`. Sem-B8 and B9 go to `oifm-content.md`.
- Order of work and the cross-directory review as you propose; replacement by explicit file mapping.

Nothing outstanding between us on the layout. Remaining decisions are the project lead's: the glossary, the three naming choices, and the go.
