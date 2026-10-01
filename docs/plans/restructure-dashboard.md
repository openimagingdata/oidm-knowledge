# Restructure dashboard

Updated 2026-09-28 (two-planes figure added) by Claude. Layout per [the layout plan](/docs/plans/2026-09-22-layout-plan.md). Paths are repo-relative; Links open in peruse. Current figure renders are copied to [docs/plans/renders/](/docs/plans/renders/) so peruse can show them; the deck images under `sources/` stay gitignored until that is fixed.

Status words: **agreed** = text settled with the project lead and on disk; **in discussion** = text proposed in conversation, not yet agreed; **material only** = the Tuesday ten-page draft holds the reviewed source material, page not yet written in the new layout; **not started**; **done** = figure accepted by Claude, awaiting the project lead; **needs pass** = known defects listed.

## Pages

| Page | Status | Where to look |
|---|---|---|
| **Overview** (root) | agreed; Astra-reviewed; two-planes figure embedded; pillars stack to follow once B3 is accepted | [knowledge/drafts/overview.md](/knowledge/drafts/overview.md) |
| **Foundation Context** index | agreed; both figures embedded | [knowledge/drafts/foundation-context.md](/knowledge/drafts/foundation-context.md) |
| Finding Models and Common Data Elements (hub) | **agreed and written**; Astra-reviewed, six provenance findings applied; prose byte-identical to the agreed text | [knowledge/drafts/finding-models-and-cdes-hub.md](/knowledge/drafts/finding-models-and-cdes-hub.md); material for the children in [knowledge/drafts/finding-models-and-cdes.md](/knowledge/drafts/finding-models-and-cdes.md) |
| OIFM content | material only | [knowledge/drafts/finding-models-and-cdes.md](/knowledge/drafts/finding-models-and-cdes.md), "What the inclusive collection holds" |
| Definition formats | material only | same file, "The two formats" |
| Identifiers | material only | same file, identifiers paragraph |
| Next-generation schema | **agreed and written**; Astra-reviewed, six provenance findings applied; prose byte-identical; CDE figure embedded | [knowledge/drafts/next-generation-schema.md](/knowledge/drafts/next-generation-schema.md) |
| Relationships | **agreed and written**; Astra-reviewed; the project lead's four prose decisions applied; figure (nodule neighborhood) pending accept | [knowledge/drafts/relationships.md](/knowledge/drafts/relationships.md) |
| Standard clinical metadata | material only | same file, "What the graph should carry" |
| Authoring and review | material only | same file, "Authoring and review" table |
| Anatomic locations | material only; Tuesday draft cross-reviewed and corrected | [knowledge/drafts/anatomic-locations.md](/knowledge/drafts/anatomic-locations.md) |
| Exam types | material only; cross-reviewed | [knowledge/drafts/exam-types.md](/knowledge/drafts/exam-types.md) |
| Standards | material only; cross-reviewed | [knowledge/drafts/standards.md](/knowledge/drafts/standards.md) |
| **Data Structures** index | not started | material in [knowledge/drafts/data-structures.md](/knowledge/drafts/data-structures.md) (Astra) |
| Observation | material only | same file |
| The two graphs | material only | same file, two-graphs section; in the ACR-RSNA-CDEs repository: `docs/next-gen-schema/03-draft-structures.md` §5 and `08-worked-examples.md` §4 |
| Exam Finding List | material only | same file |
| Imaging Problem List | material only | same file |
| Imaging Persona | material only | same file |
| Structures versus transport | material only | same file |
| **SDKs** index | not started | material in [knowledge/drafts/sdks.md](/knowledge/drafts/sdks.md) |
| Finding model SDK | material only | same file |
| Anatomic locations SDK | material only | same file |
| Terminology lookup | material only | same file |
| Imaging Problem List SDK (proposed) | material only | same file |
| **Use Cases** index (the list) | not started | material in [knowledge/drafts/use-cases.md](/knowledge/drafts/use-cases.md) (Astra) |
| Reporting assistance | material only | same file |
| Imaging history | material only | same file |
| Outcome tracking | material only | same file |
| Breast imaging | material only | same file |
| **Sample Applications** index (the list) | not started | material in [knowledge/drafts/sample-applications.md](/knowledge/drafts/sample-applications.md) (Astra) |
| Finding Model Forge | material only | same file |
| Imaging Problem List viewers | material only | same file |
| Report extraction platform | material only | same file |
| Rendering, search, and exchange | material only | same file |
| Glossary | decided 2026-09-29: dropped; rebuilt from the new pages as terms earn entries; directory removed at the replace step | [knowledge/glossary/](/knowledge/glossary/) (48 terms, obsolete) |

## Figures

| Figure | For | Status | Where to look |
|---|---|---|---|
| Two planes: a finding, its exam, and the shared knowledge they attach to | Overview (lead figure) | ACCEPTED by the project lead 2026-09-29 (v10); embedded in the Overview under "The two contexts" | [docs/plans/renders/two-planes-v10.png](/docs/plans/renders/two-planes-v10.png); [knowledge/drafts/two-planes.svg](/knowledge/drafts/two-planes.svg) |
| Five-pillar stack | Overview | v8 on B3: the SDK lane ends in Foundation Context as one tooth "attaches to · authors & maintains"; SDKs subtitle cut; applications joint widened; needs your accept, then replaces pillars.svg and goes into the Overview | [docs/plans/renders/pillars-v8-b3.png](/docs/plans/renders/pillars-v8-b3.png) | [docs/plans/renders/pillars-v3.png](/docs/plans/renders/pillars-v3.png); [knowledge/drafts/pillars.svg](/knowledge/drafts/pillars.svg) |
| Three axes | Foundation Context | v6 on Opus: full-width section bands in all three columns (node kinds; body regions; modalities), columns filled to equal density, measurements length and CT density only; embedded; needs your accept | [docs/plans/renders/three-axes-v6.png](/docs/plans/renders/three-axes-v6.png) |
| Foundation Context mini-network | Foundation Context | v8 on Opus: solid arrowheads, assessment scheme as an oval; embedded; needs your accept | [docs/plans/renders/foundation-network-v8.png](/docs/plans/renders/foundation-network-v8.png); embedded in `foundation-context.md` |
| Patient Context / Foundation Context table (deck slide 7) | Overview | permitted 2026-09-29; redundant with the two-planes figure, not planned | [sources/bucket/siim2026/media/ppt/media/image6.png](/sources/bucket/siim2026/media/ppt/media/image6.png) |
| One content, two collections | Finding models and CDEs hub | v1 on Opus; needs your accept, then embed in the hub | [docs/plans/renders/two-collections-v1.png](/docs/plans/renders/two-collections-v1.png) |
| Definition field table (deck slide 9) | Definition formats | permitted; planned | [sources/bucket/siim2026/media/ppt/media/image7.png](/sources/bucket/siim2026/media/ppt/media/image7.png) |
| Kidney field table (deck slide 10) | Anatomic locations | permitted; planned | [sources/bucket/siim2026/media/ppt/media/image8.png](/sources/bucket/siim2026/media/ppt/media/image8.png) |
| Containment, part-of, laterality example | Anatomic locations | not started | |
| CT Chest over the Playbook with anatomy edges | Exam types | not started | |
| Data-structure hierarchy | Data Structures index | existing diagram needs revision (Persona as concept, no "pointer") | [knowledge/data-structures/hierarchy.svg](/knowledge/data-structures/hierarchy.svg) |
| Report to Observation (deck slide 4) | Observation | permitted; planned | [sources/bucket/siim2026/media/ppt/media/image4.png](/sources/bucket/siim2026/media/ppt/media/image4.png) |
| The two graphs | The two graphs | permitted; planned: the CDE repository's one-report-two-planes (pyelonephritis) figure | `~/ACR-RSNA-CDEs/docs/next-gen-schema/diagrams/` |
| Foundation-context graph (deck slide 12) | Relationships | permitted; planned | [sources/bucket/siim2026/media/ppt/media/image9.png](/sources/bucket/siim2026/media/ppt/media/image9.png) |
| Pulmonary nodule neighborhood (nodes and edges from the pinned CDE graph) | Relationships page; could replace the dated 2026-09-03 figure on the schema page | v3 on Opus: illustrative per the project lead's intended CDE updates; assessment schemes now ovals; needs your accept and a placement decision (relationships page; replace the dated figure on the schema page) | [docs/plans/renders/nodule-neighborhood-v3.png](/docs/plans/renders/nodule-neighborhood-v3.png) |
| SDK resolution flow | SDKs index | not started | |

## Decisions waiting on the project lead

1. Accept the pillars stack v3, then the embed into the Overview.
2. The hub page text as revised on 2026-09-27.
3. Commit of everything since Tuesday to `bootstrap`.
4. Decided 2026-09-29: glossary dropped; rebuilt from the new pages.
5. Decided 2026-09-29: vendor generic; the two organizations generalized. Still open: commit of CDE decisions S53 to S67.
6. Decided 2026-09-29: deck and CDE-repository figures may be used.

## References layer, first content

Astra's 15 board summaries in [docs/references/linked-diagrams/](/docs/references/linked-diagrams/) are the first references-layer content (staged there until the layers plan runs); live board links and meeting names are being removed per the project lead, 2026-10-01.

## Handoff

Everything an agent needs, including the working rules, is in [docs/HANDOFF.md](/docs/HANDOFF.md).

## Layers (2026-10-01)

Three layers, per [the sources-and-layers plan](/docs/plans/2026-10-01-sources-and-layers.md): raw sources (private bucket, gitignored mirror), references (distilled summaries with figures, in `knowledge/references/`), the knowledge bundle (team-facing OKF, `knowledge/`), and the presentation (`pages/`, what the site builds). The pages in this dashboard are the presentation layer; the 115-page bundle is not replaced by them.

## Process

Content agreed in conversation, one page at a time; implementation in Opus sub-agents or the codex-impl tabs; Fable reviews. Astra cross-reviews for source fidelity. Diagrams: Excalidraw builders in [tools/diagrams/](/tools/diagrams/), rendered and looked at before use.
