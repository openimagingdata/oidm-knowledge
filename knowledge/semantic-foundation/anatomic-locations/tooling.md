---
type: Guide
title: Anatomic location tooling
description: Lookup, search, and hierarchy traversal through current and older anatomic location tools.
tags: [semantic-foundation, anatomic-locations, tooling, cli, guide]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
stale_after: 2027-09-21
sources:
  - id: fm-docs
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/docs/anatomic-locations.md
    title: Anatomic locations guide, findingmodel main, the CLI and Python API reference
  - id: fm-pkg-readme
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/anatomic-locations/README.md
    title: anatomic-locations package README, findingmodel main
  - id: fm-normalized
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/tasks/done/anatomic-locations-normalized-schema.md
    title: Rich anatomic location DuckDB with relationships, the manifest and distribution design
  - id: fm-mcp
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel/src/findingmodel/mcp_server.py
    title: findingmodel MCP server, tool definitions
  - id: fm-ai-readme
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel-ai/README.md
    title: findingmodel-ai package README, AI-assisted anatomic location discovery
  - id: bpi-py
    resource: https://github.com/talkasab/BodyPartIndex.py/blob/388ae0a6da92f5ee4cf36620bbeeabe223938471/README.md
    title: BodyPartIndex.py README
  - id: bpi-ts
    resource: https://github.com/talkasab/BodyPartIndex.ts/blob/dec578e10293d722e6136802cc5dfda2599f0f45/README.md
    title: BodyPartIndex.ts README
  - id: al-code
    resource: https://github.com/talkasab/anatomiclocations.org/blob/1f39fa45f621cef947a3f3ef1f869334cfa5c841/docs/code.markdown
    title: anatomiclocations.org code page, the JSON download
  - id: ipl-rules
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/anatomic-location-assignment-rules.md
    title: Anatomic location assignment rules, imaging-problem-list dev
---

# Which tool to reach for

| You want | Use |
|---|---|
| To look up or search [anatomic locations](/glossary/anatomic-location.md) in Python, or from a shell | The `anatomic-locations` package and its CLI |
| The same from TypeScript or JavaScript | `@talkasab/body_part_index`, against the older dataset |
| The raw data, no dependency | The JSON download from the project site |
| To curate the set itself | The `manage-anatomic-locations` skill in `findingmodel`, and [laterality conventions](/semantic-foundation/anatomic-locations/laterality-conventions.md) |

See the package README and guide for installation and configuration.[^fm-pkg-readme][^fm-docs]

# The anatomic-locations package

`pip install anatomic-locations`. The database downloads automatically on first use and there is no setup step.[^fm-pkg-readme] Lookup accepts a [RadLex identifier](/glossary/radlex-id.md), a description, or a synonym, all case-insensitive.

```python
from anatomic_locations import AnatomicLocationIndex

index = AnatomicLocationIndex()
location = index.get("RID2772")   # by identifier
location = index.get("kidney")    # by description
location = index.get("renal")     # by synonym
print(location.description)       # "kidney"
print(location.region.value)      # "Abdomen"
```

The package provides four capabilities.

**Direct lookup and code lookup.** `get()` accepts identifiers, descriptions, or synonyms. `find_by_code(system, code)` accepts [SNOMED CT](/glossary/snomed-ct.md), [FMA](/glossary/fma.md), or RadLex codes. Assignment rules prefer direct lookup for a named organ to avoid search misses such as "prostate" returning salivary glands.[^ipl-rules]

**Hierarchy traversal.** `get_containment_ancestors()` and `get_containment_descendants()` on a location, plus `get_children_of()` on the index. Both the containment and the part-of hierarchies are backed by materialized paths, so these are not recursive queries.

**[Laterality](/glossary/laterality.md) variants.** `get_laterality_variants()` returns a mapping from a `Laterality` member to the corresponding location, so a generic structure yields its left and right records.

```python
lymph_node = index.get("RID1517")
variants = lymph_node.get_laterality_variants()
# Laterality.LEFT  -> RID1517_RID5824, left axillary lymph node
# Laterality.RIGHT -> RID1517_RID5825, right axillary lymph node
```

**Hybrid search.** `search()` and `search_batch()` are async and combine full-text search with vector search over embeddings. Semantic search turns on when an OpenAI key is present; without one, search falls back to keyword-only, which handles exact terms well and can miss conceptual matches on multi-word queries.[^fm-docs]

# The CLI

The `anatomic-locations` command takes either an identifier or a name at every subcommand.

| Command | What it does |
|---|---|
| `search "posterior cruciate ligament"` | Hybrid search, printing identifier, name, region, and laterality |
| `hierarchy stomach` | Ancestors above and descendants below the location, as a tree |
| `children stomach` | Direct containment children, as a table |
| `ancestors stomach` | Containment ancestors, nearest to root |
| `descendants "abdominal cavity"` | Containment descendants |
| `laterality "axillary lymph node"` | The sided variants of a generic location |
| `code SNOMED 64033007` | Reverse lookup from an external code |
| `stats` | Database path, record counts, region and code totals |

```console
$ anatomic-locations hierarchy stomach

whole body - RID39569
    └── abdomen - RID56
        └── peritoneal cavity - RID397
            └── ▶ stomach - RID114 ◀
                ├── gastric fundus - RID116
                └── pylorus - RID122
```

# Where the database comes from

The JSON source is built into a DuckDB file published to remote storage. A central `manifest.json` references it alongside the finding model index. The package downloads and caches the database on first use, then checks the manifest for updates.[^fm-normalized] Use `ANATOMIC_DB_PATH` or the `db_path` constructor argument for a pinned or locally rebuilt database.[^fm-pkg-readme]

# What is not exposed

The MCP server in `findingmodel` offers three tools, all for finding models: search, get, and count. There is no anatomic location tool on it.[^fm-mcp] An agent that needs locations calls the package directly or goes through `findingmodel-ai`, which exposes `find_anatomic_locations` for AI-assisted discovery.[^fm-ai-readme]

# The older wrapper libraries

Both wrappers read the 2,890-record dataset described in [lineage and current implementation](/semantic-foundation/anatomic-locations/lineage-and-current-implementation.md), not the current one. Use them when you need the original data or a JavaScript runtime.

`@talkasab/body_part_index` installs from npm with the data bundled. It can also be constructed with a local JSON file of the same shape, and with a table of local codes mapped to RadLex identifiers, so an institution's own body-part codes resolve through `get()` alongside SNOMED and FMA codes.[^bpi-ts]

```typescript
import { BodyPartIndex } from '@talkasab/body_part_index';

const index = new BodyPartIndex();
const bodyPart = index.get('RID294');           // uterine adnexa
bodyPart?.getContainedBy();                     // RID2507, pelvis
bodyPart?.getPartOf();                          // RID270, female genital system
const left = bodyPart?.getLeft();               // RID294_RID5824
```

The TypeScript library provides `isContained`, `isPartOf`, immediate and full children, and full ancestors for both hierarchies.[^bpi-ts]

`BodyPartIndex.py` is the Python counterpart. Its README states that installation from PyPI is pending, so it is used from source or with a local data file. It offers `get()` by identifier or code, `get_by_code()`, `search()` over names and synonyms, `is_contained()`, the laterality triad through `left`, `right`, and `unsided`, and a `snomed_code` property that falls back to the unsided version and then the immediate parent when the sided record carries no code of its own.[^bpi-py]

# The raw data

The project site publishes a JSON file, JSON Schema, and changelog under the ISC license.[^al-code] This requires no library dependency. See [the data model](/semantic-foundation/anatomic-locations/data-model.md) and [the verbatim record format reference](/references/anatomic-location-json-schema.md).

[^fm-docs]: Anatomic locations guide, findingmodel main
[^fm-pkg-readme]: anatomic-locations package README
[^fm-normalized]: Rich anatomic location DuckDB with relationships
[^fm-mcp]: findingmodel MCP server
[^fm-ai-readme]: findingmodel-ai package README
[^bpi-py]: BodyPartIndex.py README
[^bpi-ts]: BodyPartIndex.ts README
[^al-code]: anatomiclocations.org code page
[^ipl-rules]: Anatomic location assignment rules, imaging-problem-list dev
