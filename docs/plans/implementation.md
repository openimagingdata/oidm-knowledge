# Source-to-pages implementation plan

Updated 2026-10-17. This is the single implementation planning record. This
worktree is preparing three separate commits from the accumulated changes in
the original checkout. The complete conceptual outline and owner decisions
remain preserved there and will be incorporated during documentation
consolidation. No knowledge drafting is authorized by this reconciliation.

## Reconcile the accumulated changes

The owner assigned the following work to this branch, in this order. Each
commit requires separate explicit permission. Website work belongs to the
owner's Claude session, including deployment configuration and website task
routing outside `site/`.

1. Prepare the commands to download and verify original source files, with the
   manifest, tests, CI integration, and instructions. Review and validate this
   change independently before requesting permission to commit it.
2. Consolidate planning and reference documents, preserving recorded owner
   guidance and accounting for removed plans and relocated previews. Keep the
   documents accurate for the intermediate checkout, where the original
   knowledge bundle still exists. Update this plan, references, handoff, and
   relevant logs for that state.
3. Move the old knowledge bundle into its temporary archive and establish the
   fresh graph's index and log. Preserve the outline, approvals, and unanswered
   workflow question without starting drafting. Do this last, and update the
   documentation and logs to describe the actual reset.

Create and manage the separate worktree through Worktrunk, starting from the
original checkout's current commit, `9085d85`. Copy selected changes instead of
stashing the shared checkout. Split changes in shared files by purpose. Do not
copy website changes into this branch or make edits in the original checkout.
Before later removing duplicate changes from the original checkout, verify
their preservation and coordinate that removal with the owner.

After each phase, run the relevant checks and review the documentation. Record
completed work in `DEV_LOG.md` and reader-facing behavior in `CHANGELOG.md`.
Do not claim that a planned later change has already occurred in this branch.

## Original source files

The private source collection is at `~/data/oidm-knowledge-sources`, backed by
the private `oidm-knowledge-sources` Tigris bucket. The tracked manifest selects
118 artifacts in 25 source groups. Original files and private inventories
remain outside Git. Read [source instructions](../sources.md) for commands,
metadata, selection, and handling rules.

Historical verification on October 2 compared all 307 remote objects against
local sizes and SHA-256 hashes. It does not grant publication permission or
approve source claims. Never read or summarize reviewer correspondence.

The command implementation validates the manifest without credentials,
checks local bytes, and downloads missing selected artifacts. Downloads are
verified before placement and never overwrite differing local files. The
commands do not write to the bucket. The ignored `sources` compatibility
symlink is created explicitly by the operator.

## Reconciliation progress

- [x] Create `reconcile-knowledge` from the original checkout's current commit.
- [x] Record the three-commit sequence before transferring changes.
- [x] Prepare and validate the original-file download and verification change.
- [x] Obtain permission for the first commit.
- [ ] Create the first commit and incorporate it into the original branch before proceeding.
- [ ] Prepare, validate, and obtain permission for documentation consolidation.
- [ ] Prepare, validate, and obtain permission for the knowledge reset last.
- [ ] Review documentation for the final state and account for remaining changes.

The owner approved proceeding with the prepared first change and reconciling
it into the original checkout before starting the next group. The original
checkout retains all changes. Preparation made no commit, stash, knowledge
reset, website edit, deployment, or human verification stamp.

First-change checks on October 17 pass: eight tests, all 118 local file sizes
and SHA-256 hashes, strict OKF conformance, house checks, manifest validation,
task argument routing, local documentation links, and whitespace. The installed
Tigris CLI 3.17.0 supports the documented commands. No live download was repeated
for this commit preparation; the tests exercise downloads with simulated data.

The initial house check reported an absent ignored name-check configuration.
Copied that local configuration from the original checkout, without adding it
to Git, and reran the checks with zero errors or warnings.
