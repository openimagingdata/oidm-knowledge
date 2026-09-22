# Repository review

Status: Complete (2026-09-21)

## Purpose

Explain the repository's purpose, structure, current work, and verification state.

## Steps

- [x] Record this review plan in the repository.
- [x] Read project guidance, the OKF skill, and core documentation.
- [x] Examine the knowledge bundle, publishing tools, and uncommitted work.
- [x] Run relevant local verification and investigate any failures.
- [x] Review documentation for accuracy, record findings here, and mark the review complete.

This review preserves existing work and does not publish or commit changes. Update reference documentation and active logs if the review results in changes that need documenting; a review alone does not warrant a user-facing changelog entry.

## Repository purpose and state

The repository is the intended canonical public knowledgebase for the Open Imaging Data Model. Its product is an OKF 0.2 Markdown bundle, rendered as a static site. Application implementations and vocabulary catalogs live in the source repositories documented by the bundle.

- `knowledge/`: 115 concepts, 17 indexes, and one change log. All 115 concepts have `status: draft`; none has a `verified` entry.
- Coverage: 48 glossary terms, 21 semantic foundation concepts, 10 data structure documents, seven applications, seven roadmap documents, eight references, six history documents, four overview documents, two guides, one repository map, and one build plan.
- The original build plan records phases 0–5 as done and phase 6 (integration and human review) as in progress. Its open-question register contains 90 numbered questions and 21 defect rows, including four local bundle rows.
- Git: branch `main`, two commits, HEAD `313d085`. No remote URL is configured in this checkout; `remote.pushdefault=parent` does not define a remote. GitHub publication cannot be inferred from the workflows or README alone.
- Existing uncommitted work replaces three Mermaid diagrams with Excalidraw sources and SVG renders, adds Python diagram builders/rendering helpers and `links.txt`, ignores `sources/`, and extends the development log.

## Publishing and verification

`Taskfile.yml` provides check, build, serve, publish, and graph-generation tasks. `site/build.sh` stages normalized Markdown links, builds with pinned Quartz, and emits `public/`. The custom plugin displays OKF trust and provenance metadata. `task publish` validates, builds with a bucket configuration, rewrites links for literal object keys, and uploads to Tigris. A separate workflow is configured for GitHub Pages.

The pinned upstream [Quartz package manifest](https://github.com/jackyzha0/quartz/blob/97a2d05f80c4c50534959b1d0d41cc4b3895625e/package.json) confirms version 5.0.0 and Node >=22, consistent with the local documentation. The development log records a Starlight experiment and a pending generator decision; the repository still implements Quartz.

Checks performed:

- OKF strict validator: passes, 115 concepts, no issues.
- House-rules checker: passes, 133 documents, zero errors and zero warnings.
- `bash site/build.sh`: succeeds, processes all 133 Markdown files, emits 546 files (245 HTML files).
- Three Excalidraw JSON files load and their corresponding SVG files parse as XML. This is structural validation, not a visual review.
- The build reports that the staging directory is outside a Git repository. This matches the staging design and means Git-derived content dates are unavailable there. npm also reports two install scripts not covered by `allowScripts`; neither prevented this build.

The build regenerated ignored `public/` using the default GitHub Pages configuration. It did not upload anything. No live-site or browser interaction checks were performed, and the review did not independently re-audit the external OIDM repositories or manuscript claims.

## Work awaiting integration

The ignored `sources/bucket/REPORT.md` inventories manuscripts, supporting files, a reporting-schema deck, and a webinar deck; extracted text and figures are present. `sources/excalidraw-diagrams.md` contains transcriptions and gap assessments for 15 canvases. No concept currently references `sources/bucket`, the source bucket prefix, or the imported manuscript identifiers. These imports provide material for a further synthesis pass; their substantive claims still need source review.

The source report documents extraction limits, including incomplete transcription of one PDF. Its existence should not be read as a complete verification of every imported document. Raw sources remain outside the public bundle.

## Concrete follow-up findings

1. **Human review remains the release gate.** Clean structural validation does not establish factual accuracy. The original build plan should remain in progress until its verification and release tasks actually finish.
2. **Deployment does not depend on validation.** `.github/workflows/site.yml` builds and deploys independently of `.github/workflows/validate.yml`; a failed validation workflow does not itself block this deployment. Its path filter also omits the `tools/` scripts used by the build, so changes only to those scripts do not trigger deployment.
3. **The advertised live reload misses source edits.** `site/build.sh` copies content once, then serves that temporary directory. The pinned Quartz watcher watches `argv.directory`; no process mirrors subsequent edits from `knowledge/` into the staging copy. This finding follows from the scripts and watcher implementation; it was not exercised in a browser.
4. **Direct publishing bypasses the documented validation step.** `task publish` has the validation dependency, but `bash site/publish-tigris.sh` does not run either checker. `site/README.md` currently presents both entry points as equivalent, including validation.
5. **Some status documentation needs reconciliation.** The open-question register still lists the SDK URL and eight-versus-ten exam count as bundle defects, although the referenced files contain the corrected URL and ten exams. The source-transcription introduction still says three diagrams although the body covers 15. The development log's source-extraction entry describes work as underway even though an inventory now exists.
6. **Diagram reproduction instructions need consolidation.** The new renderer's usage text refers to a `.claude/skills/excalidraw-diagram/references` location absent from this checkout, and there is no diagram task or local dependency declaration accompanying those instructions.

Suggested next sequence: reconcile the imported sources with the draft bundle, review and resolve the resulting factual questions, then complete the generator decision and publishing workflow fixes before the first reviewed release. No implementation changes were made as part of this examination.

## Documentation closeout

Recorded the review and verification in `DEV_LOG.md`. Left the original build plan in progress because its human review remains outstanding. No reader-facing behavior changed, so no changelog entry was added.
