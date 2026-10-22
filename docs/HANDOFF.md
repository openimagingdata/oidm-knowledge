# Working on this repository

## Current checkpoint, October 22, 2026

Pause the knowledge-plan discussion. Original-file download and verification
tooling is committed as `21e37a0`; planning consolidation is committed as
`ea7dfeb`. Both were explicitly approved by the owner.

The current task is to prepare the two remaining commits with Claude through
Herdr: website separation first, then the knowledge reset last. Codex handles
shared root files and coordinates the index; Claude handles website-owned
files. Neither agent may commit without explicit permission for that commit.

The temporary `reconcile-knowledge` branch and worktree have been removed at
the owner's request. Continue in this original checkout. All working files
were preserved when incorporating the first commit. The owner's Claude
session owns website changes, including supporting deployment and task
changes outside `site/`. Keep those out of the knowledge-reset commit.
See [the implementation plan](plans/implementation.md) for the current split.
Do not resume the older checkpoint below or begin drafting yet.

After both changes are committed and checked, publish `bootstrap` with approval
and open a new PR to `main`. GitHub rules require a PR and one approving review;
the local hook reserves merging/updating `main` for the owner. Do not direct-push
or use an API merge to bypass that boundary. Establish the combined current
state on `main` before creating worktrees for subsequent work.

## Knowledge-review checkpoint

After the remaining cleanup commits, resume execution-plan review from the
unanswered question below. Do not restart the organizing discussion or draft
a knowledge document yet.

The owner has approved:

- The Foundation schema overview under Finding Definitions as the first node,
  at `knowledge/foundation-context/finding-definitions/schema-overview.md`.
- Five named sections, meaningful nested groups, navigation indexes, and one
  document per substantive concept. Outline bullets do not automatically become
  files; do not create empty concept stubs.
- Current owner guidance for direction, checked revision-specific sources for
  implementation claims, explicit proposals and open questions, and concise
  citations backed by detailed references.
- Writing fresh from checked sources before consulting the old bundle for
  verified omissions. The deck-first pilot is withdrawn.

The unanswered question is, "Is the end of that cycle the right point for your
review?" The proposed cycle covers scope and evidence, a fresh draft, the
archive check, links and documentation updates, and validation before owner
review. Its review point is not approved. Restore that context before asking
the owner to answer. Then review unfinished-design status, owner review and
validation, coverage and archive deletion, and the expansion sequence, one
focused question at a time.

The complete nested outline and unresolved document boundaries remain in
[the implementation plan](plans/implementation.md). The owner's words are in
[organization guidance](references/knowledge-organization-owner-guidance.md).
Use Cases describe envisioned uses; Sample Applications require actual
implementations, including demos and prototypes. Their unfinished inventory
does not block the agreed first node once the execution-plan review is complete.

The [Claude review record](references/knowledge-outline-claude-review.md)
withdraws its unsupported IDR/FHIR Condition claim. EFL/IDR relationships and
exact FHIR mappings remain open. The requested
[clinical-reconciliation research](references/clinical-information-reconciliation.md)
is complete; it does not settle Imaging Persona's design.

The knowledge reset remains the last cleanup commit. Its archive move is
prepared in the working tree, outside the current proposed commit. Do not
edit the old prose into replacements. Delete the temporary archive only after
useful recovery is complete and active dependencies have been removed.

## Orientation

The intended pipeline is private Tigris originals, detailed references, a repository-only OKF knowledge graph, and public presentation pages. The knowledge graph stays in `knowledge/`; the website builds only the independent Markdown content in `site/content/`. It does not build the knowledge bundle. No internal knowledge website is planned.

Read [project direction](references/project-direction.md) for dated owner statements and terminology, preserved outside the disposable archive. Use [idea coverage](references/idea-coverage.md) for the inventoried concepts, known source-review corrections, and historical evidence. Both are references, not execution instructions.

Completed imports are documented with their artifacts: [brand assets](brand/README.md), [15 board summaries](references/linked-diagrams/index.md), and [OKF tooling research](references/okf-tooling-comparison.md). The board summaries are inputs to evaluate under the eventual agreed approach. Their capture dates are retrieval dates, not idea dates.

## Working rules

- Preserve the record of prior owner text and figure agreements; discuss their use in the new organization rather than silently discarding or automatically migrating them. Record source-fidelity findings separately from editorial preferences and publication approval.
- Check current working-tree changes before edits and preserve concurrent work. Do not infer file ownership or agent assignments from historical session names.
- Use committed CDE files at a pinned revision. Do not cite uncommitted decisions or commit another repository's work to make a citation available.
- Follow the implementation plan's source/sensitivity rules. Never read or summarize reviewer correspondence. Keep originals and private review records out of Git.
- Put generated previews in ignored `scratch/review/`, exposed by `.peruseshow`. Original source artifacts live in `~/data/oidm-knowledge-sources`; the ignored `sources` symlink preserves repository-local paths. Accepted diagram sources and SVGs remain tracked with their pages; follow the [diagram instructions](../tools/diagrams/README.md).
- Do not treat an agent review as human sign-off. Use root `task verify -- <knowledge paths>` only for an actual project-lead review of knowledge documents. Website pages use `task site:verify`; the website has its own production review gate. See its README for the implemented requirements.
- Do not commit without explicit permission for that commit. Update the development log for engineering work and the changelog for reader-facing changes. Keep completed detail out of the current work queue.

## Sources and private review records

Source repositories are cloned under `~/`; their relevant files and historical pins are described by the idea coverage and project-direction references. Recheck a source's committed state before making current implementation claims.

Original manuscripts, decks, extracted text, the board captures, the source report, and private review dispositions live in `~/data/oidm-knowledge-sources`, accessible through the ignored `sources` symlink. The collection is also in the `oidm-knowledge-sources` Tigris bucket. All 307 remote objects passed size/SHA-256 comparison. The private inventories retain complete integrity/classification records. The tracked [source manifest](sources-manifest.json) selects 118 artifacts in 25 source groups; use the [source instructions](sources.md) for pull/check commands. The default recovery excludes private review records and older research captures. On another checkout, configure an ignored `sources` symlink to the authorized local collection after obtaining the files. The review files use `sources/review/drafts-<page>.md` and corresponding response files. The unfiled upstream issue draft also remains there. Generated top-level figure iterations have moved to `scratch/review/iterations/`; former dashboard renders are in `scratch/review/renders/`.

The exam-type source workbook is `~/exam-types/sources/LoincRsnaRadiologyPlaybook.xlsx`. Use `LongCommonName` for exam names; do not infer that the `core-playbook-dev` sheet is a reviewed standard.

## Validation and site

Run `task check` for strict OKF conformance, the house checker, and source-manifest validation. Run `task sources:check` separately against the private local collection. [Writing the new knowledge graph](knowledge-authoring.md) describes reconstruction and metadata conventions. New references must keep working links and source IDs. Index descriptions match the target frontmatter.

The root task file includes `site/Taskfile.yml` under the `site` namespace. Use `task site:check`, `task site:build`, `task site:serve`, `task site:preview`, `task site:deploy`, `task site:deploy:staging`, and `task site:deploy:prod` for the website. Its checks, review tools, and production review gate are independent of the knowledge bundle. Read [site instructions](../site/README.md) for implemented behavior. Local configuration does not prove deployed contents or credentials.
