---
type: Concept
title: Lineage and current implementation
description: The two anatomic location lineages, the original curated set with its wrapper libraries and the anatomic-locations package inside findingmodel, which one is current, and what remains unreconciled between them.
tags: [semantic-foundation, anatomic-locations, lineage, status]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
sources:
  - id: al-site
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/docs/index.markdown
    title: anatomiclocations.org site homepage and roadmap, last commit on main 2023-01-10
  - id: al-changelog
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/data/CHANGELOG.md
    title: anatomiclocations.org data changelog, sole release 1.0.0-rc.1
  - id: bpi-todo
    resource: https://github.com/talkasab/BodyPartIndex.py/blob/388ae0a6da92f5ee4cf36620bbeeabe223938471/TODO.md
    title: BodyPartIndex.py TODO list, dated 2024-02-03
  - id: bpi-ts
    resource: https://github.com/talkasab/BodyPartIndex.ts/blob/dec578e10293d722e6136802cc5dfda2599f0f45/README.md
    title: BodyPartIndex.ts README, npm package @talkasab/body_part_index
  - id: fm-normalized
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/tasks/done/anatomic-locations-normalized-schema.md
    title: Rich anatomic location DuckDB with relationships, completed 2025-12-31
  - id: fm-docs
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/docs/anatomic-locations.md
    title: Anatomic locations guide, findingmodel main
  - id: fm-source-data
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/notebooks/data/anatomic_locations_noembed.json
    title: anatomic_locations_noembed.json, last changed 2026-03-02
  - id: fm-graph-research
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/tasks/anatomic-locations-graph-research.md
    title: Graph representation in DuckDB research note, findingmodel main
  - id: build-plan
    resource: https://github.com/openimagingdata/oidm-knowledge/blob/main/knowledge/plans/2026-09-20-knowledgebase-build-plan.md
    title: Knowledgebase build plan, source map and work edge
  - id: cde-axis
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/44836c19f4e025cf1684a015ed5cc63c29eaf7f3/docs/next-gen-schema/11-anatomy-axis.md
    title: The anatomy axis, current state, ACR-RSNA-CDEs next-gen-2026
---

# Two lineages

[Anatomic locations](/glossary/anatomic-location.md) exist twice in OIDM. The first lineage is the original curated set published at anatomiclocations.org with two wrapper libraries. The second is the `anatomic-locations` package inside the `findingmodel` repository, with its own data file. They descend from the same curation effort and hold nearly the same concepts, but they are separate artifacts with different field names, different record counts, and no synchronization between them.

| | Original lineage | Current lineage |
|---|---|---|
| Data file | `data/body_parts.json` in `anatomiclocations.org` | `notebooks/data/anatomic_locations_noembed.json` in `findingmodel` |
| Records | 2,890 | 2,926 |
| Declared version | `1.0.0-rc.1`, December 2022 | none |
| Data last changed | 2023-01-08 | 2026-03-02 |
| Consumers | `BodyPartIndex.ts`, `BodyPartIndex.py` | `anatomic-locations` Python package |
| Distribution | one JSON file plus bundled library data | DuckDB database fetched from a manifest |

# The original lineage

Three repositories under the project lead's personal account, all under the ISC license.

`anatomiclocations.org` holds the curated data, its JSON Schema, and a Jekyll site. The data changelog records one release, `1.0.0-rc.1` in December 2022, which added the version field and SNOMED links.[^al-changelog] The last commit on `main` is 2023-01-10, adding a tree view under Hierarchy. Three content-editing branches, `add-data`, `content_update`, and `content_work`, carry JSON edits and were never merged. The site lists a hierarchy browser and a search function as features not yet built.[^al-site]

`BodyPartIndex.ts` is the TypeScript wrapper, published to npm as `@talkasab/body_part_index` with the data bundled in the package. It is the richer of the two wrappers, documenting local-code mapping and every hierarchy accessor.[^bpi-ts] Its last commit on `main` is 2022-12-18.

`BodyPartIndex.py` is the Python wrapper. Its README says installation from PyPI is pending, and the site roadmap still lists "finish BodyPartIndex.py and publish to PyPI" as an open item.[^al-site] Its last commit on `main`, 2024-02-03, added a TODO list that remains the clearest statement of what that lineage intended next: move the repository to the `openimagingdata` organization, adopt ACR Common codes, acknowledge DICOM codes, track URLs, rewrite `BodyPart` as a Pydantic model, and on the website build a better tree browser and a way for people to submit suggestions about a specific node.[^bpi-todo] None of those items is done in that repository. Several were done independently in the other lineage.

# The current lineage

The `anatomic-locations` package lives inside `findingmodel` as one of five workspace packages and is published to PyPI in its own right. Its design was set by a plan completed on 2025-12-31 that replaced the flat export with a normalized model.[^fm-normalized] Four things distinguish it:

- **A rich Pydantic model.** `AnatomicLocation` sits at the same level as `FindingModelFull`, with region, classification fields, a laterality enumeration, and resolved reference objects.
- **Precomputed hierarchies.** Because the database is rebuilt whenever the data changes, containment and part-of ancestry are stored as materialized paths, making ancestors, descendants, and containment tests string comparisons rather than recursive queries.[^fm-normalized] A companion research note recorded why the adjacency-list plus recursive-CTE alternative was not chosen for a read-only database.[^fm-graph-research]
- **DuckDB distribution.** The database is built separately from the JSON source, published to remote storage, referenced from a central `manifest.json` alongside the finding model index, downloaded on first use, version-checked against the manifest, and cached locally.[^fm-normalized]
- **Hybrid search.** Full-text search combined with vector search over embeddings, with keyword-only fallback when no embedding key is available.[^fm-docs]

The JSON source data is hosted outside the repository, with the migration tool reading either a dated URL or a local file.[^fm-normalized] The copy checked into `findingmodel` at `notebooks/data/anatomic_locations_noembed.json` is the version this knowledgebase read, last changed 2026-03-02.

# Which is current

The build plan states it plainly: the `anatomic-locations` package inside `findingmodel` and its 2,926-record dataset are the current anatomic data, and the original set with its wrapper libraries is lineage.[^build-plan] Everything built since uses the package. The extraction and coding platform resolves locations through it, the finding model tooling attaches its identifiers to definitions, and the next-generation vocabulary work points at its data file pinned to a commit rather than at the older one.[^cde-axis]

The original lineage is not dead content. Its data file is still the download the public site offers, its npm package still installs, and both are still reachable at the addresses published in 2022. It is superseded as the working set, not withdrawn.

# What is unresolved

| Question | State |
|---|---|
| Synchronization | No process syncs the two datasets in either direction. Edits to one do not reach the other. |
| Record counts | 2,890 against 2,926. The difference has not been reconciled record by record, and no document states what the extra records are. |
| Repository ownership | Moving the original repositories to the `openimagingdata` organization was listed as a TODO in 2024 and has not happened.[^bpi-todo] |
| Self-referential part-of | 111 records in the current file carry a `partOfRef` pointing at themselves, and one carries a self-referential `leftRef`. The build expects self-referential containment at the root, which is legitimate; this is not. |
| The "Spine" region | The curation field reference lists `"Spine"` among the common region values, but no record uses it and the runtime region enumeration has no spine member. Other parts of OIDM do use a spine region, so it is unclear whether the value was dropped deliberately or never added. |
| Empty classification fields | `location_type`, `body_system`, and `structure_type` are defined on the model and empty in the data, which is recorded elsewhere as the major shortcoming for anatomic scope statements.[^cde-axis] |

These are open questions rather than defects with owners. They are collected with the rest in [open questions](/roadmap/open-questions.md); the direction for the area is in [the anatomic locations and RadLex roadmap](/roadmap/anatomic-locations-and-radlex.md). For how to use either lineage today, see [tooling](/semantic-foundation/anatomic-locations/tooling.md); for the record shapes, see [the data model](/semantic-foundation/anatomic-locations/data-model.md).

[^al-site]: anatomiclocations.org site homepage and roadmap
[^al-changelog]: anatomiclocations.org data changelog
[^bpi-todo]: BodyPartIndex.py TODO list, 2024-02-03
[^bpi-ts]: BodyPartIndex.ts README
[^fm-normalized]: Rich anatomic location DuckDB with relationships
[^fm-docs]: Anatomic locations guide, findingmodel main
[^fm-source-data]: anatomic_locations_noembed.json
[^fm-graph-research]: Graph representation in DuckDB research note
[^build-plan]: Knowledgebase build plan
[^cde-axis]: The anatomy axis, current state, ACR-RSNA-CDEs next-gen-2026
