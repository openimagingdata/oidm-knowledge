# Restructure dashboard

Updated 2026-09-28 (two-planes figure added) by Claude. Layout per [the layout plan](/docs/plans/2026-09-22-layout-plan.md). Paths are repo-relative; Links open in peruse. Current figure renders are copied to [docs/plans/renders/](/docs/plans/renders/) so peruse can show them; the deck images under `sources/` stay gitignored until that is fixed.

Status words: **agreed** = text settled with the project lead and on disk; **in discussion** = text proposed in conversation, not yet agreed; **material only** = the Tuesday ten-page draft holds the reviewed source material, page not yet written in the new layout; **not started**; **done** = figure accepted by Claude, awaiting the project lead; **needs pass** = known defects listed.

## Pages

| Page | Status | Where to look |
|---|---|---|
| **Overview** (root) | agreed; Astra-reviewed; pillars figure not yet embedded | [knowledge/drafts/overview.md](/knowledge/drafts/overview.md) |
| **Foundation Context** index | agreed; both figures embedded | [knowledge/drafts/foundation-context.md](/knowledge/drafts/foundation-context.md) |
| Finding models and CDEs (hub) | in discussion: opening three parts revised 2026-09-27, rest as proposed | conversation; material in [knowledge/drafts/finding-models-and-cdes.md](/knowledge/drafts/finding-models-and-cdes.md) |
| OIFM content | material only | [knowledge/drafts/finding-models-and-cdes.md](/knowledge/drafts/finding-models-and-cdes.md), "What the inclusive collection holds" |
| Definition formats | material only | same file, "The two formats" |
| Identifiers | material only | same file, identifiers paragraph |
| Next-generation schema | material only | same file, "The common graph" |
| Relationships | material only | same file, "The relationship family", "Assessments, components" |
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
| Glossary | decision pending: keep, cut, or drop | [knowledge/glossary/](/knowledge/glossary/) (49 terms) |

## Figures

| Figure | For | Status | Where to look |
|---|---|---|---|
| Two planes: a finding, its exam, and the shared knowledge they attach to | Overview (lead figure) | done (v5 on Opus, with the thorax > lung > upper lobe chain); needs your accept, then embed in the Overview | [docs/plans/renders/two-planes-v5.png](/docs/plans/renders/two-planes-v5.png); [knowledge/drafts/two-planes.svg](/knowledge/drafts/two-planes.svg) |
| Five-pillar stack | Overview | v3 on Opus; needs your accept; fence-like seam threads and the "relationships" plate placement are the known nits | [docs/plans/renders/pillars-v3.png](/docs/plans/renders/pillars-v3.png); [knowledge/drafts/pillars.svg](/knowledge/drafts/pillars.svg) |
| Three axes | Foundation Context | done | [docs/plans/renders/three-axes-v1.png](/docs/plans/renders/three-axes-v1.png); embedded in `foundation-context.md` |
| Foundation Context mini-network | Foundation Context | done (v6 on Opus) | [docs/plans/renders/foundation-network-v6.png](/docs/plans/renders/foundation-network-v6.png); embedded in `foundation-context.md` |
| Patient Context / Foundation Context table (deck slide 7) | Overview | needs your permission to embed your own deck figures | [sources/bucket/siim2026/media/ppt/media/image6.png](/sources/bucket/siim2026/media/ppt/media/image6.png) |
| One content, two collections | Finding models and CDEs hub | not started; design proposed in conversation | |
| Definition field table (deck slide 9) | Definition formats | permission question as above | [sources/bucket/siim2026/media/ppt/media/image7.png](/sources/bucket/siim2026/media/ppt/media/image7.png) |
| Kidney field table (deck slide 10) | Anatomic locations | permission question as above | [sources/bucket/siim2026/media/ppt/media/image8.png](/sources/bucket/siim2026/media/ppt/media/image8.png) |
| Containment, part-of, laterality example | Anatomic locations | not started | |
| CT Chest over the Playbook with anatomy edges | Exam types | not started | |
| Data-structure hierarchy | Data Structures index | existing diagram needs revision (Persona as concept, no "pointer") | [knowledge/data-structures/hierarchy.svg](/knowledge/data-structures/hierarchy.svg) |
| Report to Observation (deck slide 4) | Observation | permission question as above | [sources/bucket/siim2026/media/ppt/media/image4.png](/sources/bucket/siim2026/media/ppt/media/image4.png) |
| The two graphs | The two graphs | not started; the CDE repo's `two-planes.svg` and `report-pyelonephritis.svg` are the best existing pictures; permission to reuse from the allied repo is your call | `~/ACR-RSNA-CDEs/docs/next-gen-schema/diagrams/` |
| Foundation-context graph (deck slide 12) | Relationships | permission question as above | [sources/bucket/siim2026/media/ppt/media/image9.png](/sources/bucket/siim2026/media/ppt/media/image9.png) |
| SDK resolution flow | SDKs index | not started | |

## Decisions waiting on the project lead

1. Accept the pillars stack v3, then the embed into the Overview.
2. The hub page text as revised on 2026-09-27.
3. Commit of everything since Tuesday to `bootstrap`.
4. Glossary: keep, cut, or drop.
5. Naming: the reporting vendor in the 2024 update; the two organizations behind the 47 and 31 finding models; commit of CDE decisions S53 to S67.
6. Whether your own deck figures, and figures from the ACR-RSNA-CDEs repository, may be embedded.

## Process

Content agreed in conversation, one page at a time; implementation in Opus sub-agents or the codex-impl tabs; Fable reviews. Astra cross-reviews for source fidelity. Diagrams: Excalidraw builders in [tools/diagrams/](/tools/diagrams/), rendered and looked at before use.
