# Writing the new knowledge graph

These instructions apply to reconstruction after the separately approved
knowledge reset is committed. They do not authorize drafting now. The existing
bundle and its historical build plan are retained in the planning-consolidation
commit; their relocation is the following change.

The repository-only OKF graph lives in `knowledge/`. Follow the owner's nested conceptual outline and reconstruction method in [the implementation plan](plans/implementation.md).

Write each concept from an empty file, using relevant sources and processed references. After drafting, check `archive/knowledge` for useful omissions and source leads. Verify recovered claims before adding them. The archive's wording, hierarchy, and file boundaries are not templates for the new graph.

## Documents and connections

- Write one substantive concept per Markdown document. Decide its scope from the outline and content, not from old files.
- Use plain-English titles and preserve the outline's parent context. Explain relationships in prose with Markdown links to related concepts.
- Record facts, stated goals, proposals, and unresolved questions with their actual status. Do not resolve disagreements by inference.
- Source substantive claims. Use pinned repository revisions and precise source locators. Preserve the source-handling rules in the implementation plan.
- Keep processed source references in `knowledge/references/`. They must be checked against sources; archived reference prose is not automatically suitable for reuse.
- Keep outward-facing page work in `site/`, planning in `docs/`, and shared assets outside the knowledge graph.

## OKF metadata and navigation

Each concept needs YAML frontmatter with `type`, `title`, `description`, and `generated: { by, at }`. Use a type supported by `tools/check_bundle.py`, such as Concept, Reference, or Data Structure. New agent-written documents have `status: draft`. Record sources in the `sources` list, with an `id` and `resource` for each entry; use matching footnotes for claim attribution. A human verification entry records an actual owner review, not an agent's assessment.

Directory `index.md` files list their documents and subdirectories with matching descriptions. Only the bundle-root index carries frontmatter, containing `okf_version: "0.2"`. Record bundle changes newest first in `knowledge/log.md` under dated headings.

Run `task check` for deterministic OKF validation, the house checker, and source-manifest validation. Commits require explicit permission each time.
