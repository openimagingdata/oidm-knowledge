# Data Structures, Use Cases, and Sample Applications drafts

Status: Drafting and Codex's cross-review pass complete. Authorized by the project lead on 2026-09-22 through the drafting assignment and review handoff from Fable.

## Scope

Follow the agreed outline in `restructure-joint-notes.md` and the sources behind `idea-placement.md`. Create three concise pillar anchors in `knowledge/drafts/`: `data-structures.md`, `use-cases.md`, and `sample-applications.md`. Claude owns Foundation Context and SDKs. Existing pages and navigation remain until cross-review and replacement.

## Steps

1. Record this plan and the file ownership before drafting. Done.
2. Read the underlying sources, preserve dated related representations and their actual status, and draft the three anchors. Every substantive claim needs a source. Use draft status and session-specific `generated.by`.
3. Check coverage against the placement table, review source fidelity and prose, and run OKF validation and link checks. Update this plan with results and any remaining issues.
4. Hand the drafts to Claude for cross-review. Update the development log and bundle log to distinguish completed drafting from pending replacement and publication. Review the documentation for an accurate final state.

No commits or publication are included in this drafting assignment.

## Drafting results, 2026-09-22

- Created Data Structures, Use Cases, and Sample Applications in `knowledge/drafts/`, with draft status and session-specific authorship. Added their links to the shared draft index. Body counts, excluding frontmatter and footnote definitions, are 1,311, 680, and 713 words respectively, 2,704 total. Counts use whitespace-separated body tokens, including Markdown link syntax.
- Data Structures covers the 24 assigned ideas with the two graphs at its center. An independent review checked pinned CDE/IPL sources and the clean JDIM manuscript pages. Fixed unresolved coding, durable-identity limitations, the manuscript's human-review boundary, the deck's internally differing status labels, and the extraction review contract. Manuscript text was paraphrased.
- Use Cases covers the application half of Patient Context and the documented proposals. Corrected the inventory's webinar grouping: quality surveillance and research are separate application families; breast imaging is a separate planned example.
- Sample Applications distinguishes implemented work from evaluation plans and proposed exchange workflows. Public RSNA material supports the built interoperability demonstrations. The board's unique proposed element-role tagging was handed to Claude for Foundation Context or SDKs.
- Verified all citation IDs against frontmatter sources and all cited pinned Git paths against the local source repositories. Whitespace checks pass. Both bundle validators report no issues in these three pages. The latest full-bundle check still reports links and index entries for Claude's drafts as those files arrive; the combined gate must be rerun after drafting finishes.
- Sent all three pages to Claude for source cross-review. Updated the bundle and development logs. No changelog entry is warranted for staged, unpublished drafts. Existing pages have not been replaced by this session.

## Remaining shared work

Both sessions' cross-reviews have been delivered. Claude is applying findings to his pages; replacement of old pages and publication remain steps in the joint plan. These drafts carry no human verification stamp.

## Cross-review handoff, 2026-09-22

Status: Complete for Codex's assigned pass, following the owner's relayed handoff.

1. Record this review phase before further work. Done.
2. Review Claude's seven drafts against their cited sources. Write one findings file per page in `sources/review/drafts-<page>.md`; do not edit Claude's pages. Distinguish factual errors from optional detail and substantiate every requested correction.
3. Resolve the incoming reviews of the three Codex drafts against primary evidence. Apply supported corrections to those three pages only; record any review findings that the sources do not support. Preserve a lean reading path.
4. Check citations, links, and bundle conformance. Append the handoff and update this plan and the development log with the completed scope and remaining work. Replacement, commits, and publication remain outside this pass.

### Results

- Reviewed all seven Claude drafts against primary sources, assisted by three agents. Findings are in `sources/review/drafts-<page>.md`. No Claude page was edited by this session. Material corrections include commit/date mismatches, overstated implementation claims, dropped proposal provenance, and compatible source statements presented as conflicts.
- Addressed incoming findings in the three Codex pages. Dispositions are in `sources/review/drafts-{data-structures,use-cases,sample-applications}-response.md`, including supported corrections and reasons for rejecting unsupported portions. Claude withdrew the signed-report-scope finding after checking the manuscript evidence.
- Data Structures now uses the deck's calculus example to explain the graph connection and preserves dated differences in aggregation, status, entity resolution, and transport. Use Cases distinguishes the sources' application groupings and proposal status. Sample Applications links the working examples and uses team evidence for the demonstrated work. Manuscripts remain paraphrased and descriptively cited; reviewer correspondence was not used.
- Revised body counts are 1,551, 767, and 756 words respectively (3,074 total), using the same counting method as the initial results. Source corrections account for the additions; the initial counts above describe the first drafts.
- Strict OKF validation passes; the bundle checker reports 144 documents, 125 concepts, zero errors and zero warnings. All three pages retain draft status and session authorship; every footnote matches a declared source. Pinned source paths and application links were checked during review. Whitespace checks pass.
- Updated the shared handoff, development log, and bundle log. No reader-facing changelog entry is needed for staged, unpublished drafts. No commit, replacement, or publication by this session.
