# OKF tooling origins and reuse options

Reviewed 2026-10-01. This is an investigation and recommendation, not a tooling migration. Research used Exa, Ref, upstream documentation, GitHub metadata, and direct file comparisons. Technical-writing and unslop skills guided the report.

The [follow-up comparison](okf-tooling-comparison.md) evaluates other v0.2 skills, runs validator fixtures, and qualifies the initial QMD recommendation. This origins review establishes where our tools came from; it does not establish that they are the best available.

## We adopted the format and core tools

OKF comes from Google Cloud. Its current canonical home is [GoogleCloudPlatform/open-knowledge-format](https://github.com/GoogleCloudPlatform/open-knowledge-format). The [old knowledge-catalog README](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/README.md) explicitly says its OKF directory is a frozen snapshot and directs users to the new repository. Our vendored specification still names the old location.

The four installed skills come from [scaccogatto/okf-skills](https://github.com/scaccogatto/okf-skills): author/maintain/consume, validate/migrate, visualize, and backfill. The development log records their selection on September 20. All 13 files under `.agents/skills/` match upstream commit `d8393f329c97836980566c1cf4e4aa4fe47dc111` byte for byte. That was upstream's latest commit before September 21. This establishes that the installed files are upstream copies with no local edits.

Upstream main was `8e3187875e66051bb52f91a5ed27342e2c3208da`, dated September 28, at review time. Nine installed files differ from that newer revision. Those differences reflect upstream updates, not a local fork. Keep future imports pinned and record their source revision.

## What is specific to this repository

| Component | Origin and coupling |
|---|---|
| `.agents/skills/` | Unmodified upstream generic OKF tooling. Works on other bundles. |
| `tools/check_bundle.py` | Local policy, adapted from ACR-RSNA-CDEs. Fixes the allowed document types, requires title/description/generated metadata, demands index coverage, checks links, and scans for email addresses and locally denylisted terms. Default paths are project-specific. |
| `tools/verify.py` | Local implementation of a reusable review action. Writes verification and stable status; defaults to `knowledge/` and the project lead's actor identity. |
| `site/okf-meta-plugin/` | Local Quartz integration for generic OKF fields. It has no imaging-domain model. |
| `tools/prepare_site_content.py` | Local adapter that normalizes Markdown links for our Quartz build. The transformation is reusable; its default paths are local. |
| `Taskfile.yml`, CI, site config, deployment | Project wiring around external tools. |
| `knowledge/` organization and content | Project-specific terminology, five pillars, references, authoring policies, and review decisions. |

The strict house rules are stronger than OKF conformance. OKF deliberately accepts unknown concept types and missing optional metadata. Our repository chooses a controlled vocabulary and requires richer metadata. Replacing its checker with a generic OKF validator would remove those policies.

## Existing tools worth using

| Tool | Fit and recommendation |
|---|---|
| [okf-skills](https://github.com/scaccogatto/okf-skills/blob/main/README.md) | Best direct fit, already installed. Current upstream also offers a composite CI action and a read-only MCP server with search, read, and graph-neighbor tools. The MCP server existed by the installed revision but was not included in our skill-only installation. Review newer validator/spec/template updates and import a pinned revision. Use MCP when a client cannot access the files directly. |
| [Google's reference implementation](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/README.md) | Canonical spec, a reference producer using ADK/Gemini, BigQuery metadata ingestion plus web enrichment, and a graph viewer. The README calls the producer a proof of concept. Its data-catalog workflow does not directly replace our manuscript, diagram, and repository-source curation. |
| [Quartz](https://quartz.jzhao.xyz/) | Already provides the website, search, backlinks, and graph. Keep reusing it. Our OKF metadata component is a small integration rather than a home-grown site generator. |
| [QMD](https://github.com/tobi/qmd) | Strong adjacent candidate for agent retrieval. Indexes existing Markdown and offers local keyword/vector search, reranking, CLI output, and MCP. It can supplement OKF without changing the document format. It does not replace provenance validation or human review. Evaluate only if retrieval is a concrete problem. |
| [Basic Memory](https://github.com/basicmachines-co/basic-memory) | More extensive Markdown knowledge-management and MCP workflow, including graph traversal and semantic search. Its [knowledge format](https://docs.basicmemory.com/concepts/knowledge-format) adds permalinks, categorized observations, and typed wikilink relations. Those conventions require a compatibility trial against our ordinary Markdown links and OKF metadata. It is a larger workflow change than QMD; do not assume it is a drop-in replacement. |

The direct OKF ecosystem is young. Google's reference producer is explicitly experimental, and okf-skills is pre-1.0. Broader Markdown tools provide more retrieval and publishing functionality, but their support for Markdown does not establish OKF trust or attestation semantics. Popularity alone does not establish suitability.

## Recommended direction

Keep OKF and the upstream skills. Update the vendored source references and skills through a reviewed, pinned import. Keep project policy distinct from the generic validator; reduce duplicated metadata checks where upstream already covers them. Continue using Quartz for presentation. Consider QMD for retrieval before building a custom search service. Basic Memory deserves a trial only if we want its broader shared-memory workflow.

The following differences need attention during that follow-up:

- Current upstream accepts ISO 8601 timestamps in `stale_after`, source `last_modified`, and usage windows, while our older skill/spec uses date-only guidance. The local house checker accepts only date strings for `stale_after`, so an upstream update needs coordinated policy and documentation review.
- `site/okf-meta-plugin/dist/components/index.js` only renders `verified` arrays. OKF also permits a single mapping.
- The same plugin treats a date as stale strictly after that day. Our vendored spec and house checker use on-or-after semantics.
- The house checker permits only `okf_version` in root-index metadata, while the upstream plugin uses an additional `upkeep` opt-in. That is a policy incompatibility if we adopt the plugin's enforced-upkeep mode.

These are findings, not changes made by this review. No tool installation, bundle rewrite, commit, or publication occurred. No reader-facing changelog entry is needed.
