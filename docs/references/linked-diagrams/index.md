# Linked diagram references

These 15 short summaries capture the ideas in every unique URL in [links.txt](../../../links.txt). Native SVG and PNG exports, original scene contents, searchable text, and capture metadata are stored under `sources/linked-diagrams/<scene-id>/`. Sources remain outside Git under this repository's existing rules; the summaries are tracked here, and the live source URLs are kept only in the gitignored capture manifest.

These captures are staged here pending approval of the [sources and layers plan](../../plans/2026-10-01-sources-and-layers.md). That plan places distilled references in `knowledge/references/`, keeps raw sources in a private bucket with a gitignored mirror, and separates the team knowledge bundle from presentation pages. This capture task does not move existing content or change the site's build input.

Read these as source references alongside the [current owner guidance](../../plans/2026-09-22-layout-plan.md). Historical class names, checklists, possible architectures, and demo designs retain their original status. A board is evidence of an idea or discussion; completion requires implementation evidence. The pillar connections below are navigation aids for the agreed structure.

| Reference | Ideas to return to | Pillars |
|---|---|---|
| [Imaging Problem List](./imaging-problem-list.md) | Per-exam findings, longitudinal association, integrated clinical context | Data Structures; Use Cases |
| [OIFM authoring and content development](./finding-model-authoring.md) | Inclusive definitions, iterative enrichment, authoring tools | Foundation Context; SDKs; Sample Applications |
| [CDE and Observation worked example](./definition-observation-example.md) | Definitions connected to instance values and clinical text | Foundation Context; Data Structures; SDKs |
| [Imaging context object model](./imaging-context-object-model.md) | Patient/exam/report context, provenance, platform operations | Data Structures; Foundation Context; SDKs |
| [Finding model rules and scope](./finding-model-rules.md) | Naming, anatomic scope, separate associated entities and components | Foundation Context |
| [Structured report representation](./structured-report-representation.md) | Complex findings, report sections, source-independent representations | Data Structures; Foundation Context; SDKs |
| [Radiologist outcome feedback](./radiologist-outcome-feedback.md) | Patient/anatomy/time-based outcome feedback | Use Cases; Foundation Context; Data Structures |
| [RSNA exhibit examples](./rsna-exhibit-examples.md) | Comparable observations, multiple producers, AI discrepancies | Foundation Context; Data Structures; Use Cases |
| [OIDM big picture and application framework](./oidm-big-picture.md) | Shared context, commands, tools, content, application ecosystem | All five pillars |
| [Anatomy and exam coverage](./anatomy-and-exam-coverage.md) | Actual exam coverage, anatomy connections, curated content | Foundation Context; Use Cases |
| [Longitudinal integration discussions](./longitudinal-integration-discussions.md) | Tracked identity, per-exam findings, relevance filtering | Data Structures; Foundation Context; Use Cases |
| [Outcome and follow-up structures](./outcome-and-follow-up-structures.md) | Recommendations, later events, completion and pathways | Use Cases; Data Structures |
| [Use-case development and interaction ideas](./use-case-development.md) | User interactions, report views, spine numbering | Use Cases |
| [Participation, reference work, and demonstrations](./participation-and-demonstrations.md) | Contributing content, tools, reference work, demos | Foundation Context; SDKs; Sample Applications |
| [Pulmonary-nodule demo workflow and role tagging](./pulmonary-nodule-demo-workflow.md) | Multi-system nodule workflow, semantic annotations, element roles | Use Cases; Data Structures; SDKs; Sample Applications |

There are 17 URL occurrences and 15 unique boards. Imaging Problem List and OIFM Repo each occur twice and share one capture and summary. The capture manifest is in `sources/linked-diagrams/manifest.json`.

All boards were retrieved and visually reviewed on 2026-10-01. Each original PNG is a native full-board export at 1×. Three native SVG exports contain XML-invalid entities or control characters. Their untouched `original.svg` files are retained; linked `usable.svg` copies only normalize those characters. Each capture's metadata records that distinction and file checksums. The source-contents response alone lacks separately stored image binaries; the visual exports embed them.

The earlier combined transcription in `sources/excalidraw-diagrams.md` remains available as historical research. These individual summaries were checked against the live exports and text, including corrections to the compact finding-model rules about anatomic scope and component extraction.
