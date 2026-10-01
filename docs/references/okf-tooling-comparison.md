# Choosing OKF skills and search tools

Reviewed 2026-10-01. Follow-up to [the origins review](okf-tooling-review.md). Keep OKF; compare tooling without changing the installation.

## The current skills are defensible, but not proven best

The September 20 development log records a comparison between scaccogatto's v0.2 toolkit and the v0.1 skill linked from okf.md. That establishes a version-based selection. It does not establish a comprehensive comparison or prove that the first search result drove the decision.

Current primary-source comparison:

| Candidate | Evidence and fit |
|---|---|
| [scaccogatto/okf-skills](https://github.com/scaccogatto/okf-skills) | Our installed toolkit. OKF 0.2 author/maintain/consume, migration, deterministic validator, graph rendering, and history backfill. Uses PyYAML. Good fit with our Python/uv tooling and existing tasks. Current upstream also has MCP, a CI action, plugin hooks, and backfill agent definitions. |
| [lorsabyan/okf-skill](https://github.com/lorsabyan/okf-skill) | Credible v0.2 alternative. Validator, trust/freshness reports, index generator, tests against pinned Google sample bundles, and scheduled spec-drift checks. More validation coverage in the trial below. Its dependency-free parser deliberately handles a YAML subset rather than full YAML. Its skill imposes relative-only links and index-organizing conventions that differ from our current policy. |
| [serradura/okf](https://github.com/serradura/okf) | Broader v0.2 toolkit: separate validate/lint commands, ranked search, trust/status filtering, multi-bundle registry, graph, CLI/library, and optional MCP/TUI. A serious candidate for a unified toolchain, but introduces Ruby or Docker and replaces more of our workflow. Reviewed docs, not executed here. |
| [parkscloud/okf-author](https://github.com/parkscloud/okf-author) and [catancs/okf-skill](https://github.com/catancs/okf-skill) | Current documentation still targets v0.1. Their authoring defaults do not address our v0.2 trust/provenance workflow. No reason to switch to them for this bundle. |
| [copperbox/okf-mcp](https://github.com/copperbox/okf-mcp) | Extensive multi-bundle navigation, remote loading, packing, repair, and authoring tools. Current documentation describes v0.1 validation and timestamp/citations write conventions. Read capabilities merit separate evaluation; avoid adopting its write path for our v0.2 workflow without verification. |

Recommendation: retain the current authoring and visualization skills provisionally. Evaluate lorsabyan's validator alongside ours before deciding whether to replace validation. Evaluate serradura if we want one tool for multi-bundle search, filtering, lint, and graph navigation. Installing overlapping authoring skills together risks conflicting instructions.

## What the validator trial actually shows

I ran the [lorsabyan fixture corpus](https://github.com/lorsabyan/okf-skill/tree/main/benchmark) against our installed validator, current scaccogatto upstream at `8e3187875e66051bb52f91a5ed27342e2c3208da`, and lorsabyan's current validator. The corpus contains 19 deliberately problematic bundles and 10 clean bundles. It was authored by one candidate's maintainer and is a small test, not independent proof of overall superiority.

| Validator | Problem cases reported without crashing | Clean cases accepted without additional reports |
|---|---|---|
| Installed scaccogatto | 13/19 | 10/10 |
| Current scaccogatto | 13/19 | 10/10 |
| lorsabyan | 19/19 | 10/10 |

To make the comparison meaningful, I excluded scaccogatto's missing-title and missing-tags warnings, which occur in the unchanged baseline too. Both tools then have a silent baseline. The corpus itself was unchanged. Lorsabyan's clock was pinned to July 30; scaccogatto's checker does not report calendar staleness. The scores count any report, not necessarily the correct diagnosis. Scope differs: scaccogatto intentionally leaves some curation checks to other tools, and our house checker already covers index coverage and stale dates.

Both scaccogatto versions crash when PyYAML parses an impossible unquoted date. Other unreported cases cover missing indexes, passed stale dates, an undefined/unattributed footnote, an attested computation with no computation, and a dead path-valued field. The crash needs a fix; broader checking needs a policy choice. It is not enough to update the upstream pin and assume these are resolved.

On the actual bundle, our validator passes with 129 concepts and zero issues. Lorsabyan reports zero errors and 15 warnings for source locators written relative to the repository rather than the bundle. Those are path-contract differences to resolve before replacing the validation gate. Strict mode fails on those warnings.

The alternative index generator's `--check` proposes changes to all 18 indexes. Inspection shows that it reconstructs headings and recognized list entries but drops surrounding prose. Its preservation promise covers entries, not entire documents. Our root index contains introductory and review-status prose. Do not run this generator in write mode on our indexes without a preservation fix.

## Useful upstream additions, in priority order

1. **Pinned updates and drift detection.** Record the toolkit revision, refresh the canonical spec source, and borrow the [lorsabyan scheduled drift-check pattern](https://github.com/lorsabyan/okf-skill/blob/main/README.md#maintenance). Comparing specification content matters because upstream changed timestamp guidance without changing `okf_version`.
2. **Reuse upstream fixtures and tests.** Keep generic conformance covered by upstream tests; test our policy separately. Include the impossible-date case when evaluating an update. Report or contribute the generic validator fix upstream rather than maintaining an unnoticed local fork.
3. **Use the validator's existing JSON output.** It is already installed. CI can consume the report rather than parse terminal output. The [upstream composite action](https://github.com/scaccogatto/okf-skills/blob/main/action.yml) packages validation and a JSON report. It would simplify wiring, not add new validation capability. Pin its commit if adopted.
4. **Complete backfill packaging when needed.** Our backfill skill references `agents/event-analyzer.md` and the `okf:bundle-weaver` agent. Those definitions are not in the installed payload. Vendor the matching definitions or use the reviewed full plugin for a history reconstruction. Do not run backfill on this established bundle just to use the feature.
5. **Expose an upstream MCP reader only for clients that benefit.** The [scaccogatto server](https://github.com/scaccogatto/okf-skills/blob/main/servers/okf_mcp.py) offers search/read/neighbors, including internal source edges. Codex already has file tools; adding MCP does not automatically improve retrieval. For remote clients, configure the actual `knowledge/` path instead of the default `.okf/`.
6. **Trial native OKF filtering for team queries.** Serradura's search supports OKF `--trust` and `--status` directly. That is useful for questions constrained to reviewed content and deserves comparison with a generic search index.

The full plugin's enforced-upkeep hook only checks that the knowledge log changed alongside code. It does not prove that affected concepts were updated accurately. Our house checker also rejects its root-index `upkeep` field. Adopting that hook is a separate workflow decision, not a prerequisite for better tooling.

## QMD is a candidate, not the selected search tool

There are 257 files across `knowledge/` and `docs/` at the review snapshot, including non-Markdown assets. This is small enough to establish a file-search baseline before adding a model-backed index.

| Need | First candidate | Why / limit |
|---|---|---|
| Known names, exact identifiers, citation IDs | `rg` plus designed indexes | Already available, searches current files, and gives paths/lines. Use as the baseline. |
| Neighbors, backlinks, trust/status constraints | Native OKF tooling | Preserves graph and metadata semantics. Compare serradura and the existing toolkit's MCP reader. |
| Natural-language questions that use different vocabulary | [QMD](https://github.com/tobi/qmd) | Local BM25, vector retrieval, reranking, CLI/MCP, and an existing `qmd bench` command. Quality on OIDM is unmeasured. |
| Section navigation with frontmatter filters | [doctree-mcp](https://github.com/joesaby/doctree-mcp) | BM25 plus heading-tree navigation and frontmatter facets without embedding models. Its own competitive claims are not independent benchmark evidence. |
| Searching original PDFs, decks, websites, and repositories | [docs-mcp-server](https://github.com/arabold/docs-mcp-server) | Broader ingestion formats and sources. More relevant than Markdown-only retrieval if raw-source access is central. Extraction quality, source locators, and indexing scope need testing. |
| People searching the public website | Quartz search | Already integrated. A local agent-search tool is not a replacement for the public-site search experience. |

QMD's full pipeline downloads three local models totaling about 2 GB. Index refresh and embedding refresh must be managed. Keyword-only mode avoids the model pipeline, but then the comparison is against existing exact search and lighter BM25 tools.

More importantly, [QMD metadata filtering](https://github.com/tobi/qmd#metadata-filtering) requires an opt-in `qmd.metadata` block with flat typed values. It does not automatically derive trust or freshness from our nested `verified` and `sources` fields. An adapter could produce those filters, but that would add code. Keep retrieval separate from the decision about whether a claim is verified and current.

Choose search with real tasks: exact terminology, paraphrased concepts, questions requiring multiple linked pages, source lookup, reviewed-only constraints, and absent-answer cases. Label the expected evidence files first. Compare the current agent/file workflow, native OKF search, and QMD or doctree; add broad-source ingestion only if required. Measure evidence recall, citation correctness, refresh after an edit, resource use, and whether extra tool calls help. QMD already provides a benchmark runner, so there is no reason to invent one before trying it.

No search engine was installed or benchmarked in this review. The validator trial does not establish retrieval quality or authoring quality. The right search choice remains open until its intended consumer and actual failures are clear.
