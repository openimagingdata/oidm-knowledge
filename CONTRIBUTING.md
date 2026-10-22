# Contributing

This repository holds source-grounded Open Imaging Data Model knowledge and its presentation pages. Code documentation stays in the working repositories.

## Before you write

Start with the [implementation plan](docs/plans/implementation.md) for current destinations, source rules, and review state. Maintain that plan as work progresses rather than adding overlapping task plans.

New knowledge drafting remains paused until the owner completes the remaining execution-plan review. The approved organization and first node do not approve the unanswered review workflow.

Read [Writing the new knowledge graph](docs/knowledge-authoring.md). It describes fresh reconstruction, metadata, links, sources, and review. The old generated bundle is temporarily held in `archive/knowledge`; write new documents from the outline and checked sources, then consult the archive for omissions. Do not edit old prose into replacements. Delete the archive after recovery is complete, as recorded in the implementation plan.

Source collection and recovery instructions are in [Recover and verify source material](docs/sources.md). Run `task sources:manifest` when changing source metadata; recovery code tests run in CI without private data.

## Ground rules

- **Facts and stated goals.** Document what exists and what the project has said it intends. Design proposals go through a separate review and are typed as such.
- **One concept per file.** Put it in the right directory and list it in that directory's `index.md`.
- **Sources.** Say what you read, pinned to a commit. Attribute specific claims with footnotes.
- **People.** Name organizations, not individuals. The project lead is the only named person.
- **Catalogs.** Describe and link. Do not copy finding model, anatomic location, or CDE catalogs into this repository.

## Workflow

1. Branch from `main`.
2. Write or edit under `knowledge/`. New agent-written documents start with `status: draft`.
3. Update the directory `index.md` and add a line to `knowledge/log.md`. Record substantive recovery decisions in the implementation plan as needed.
4. Run both checkers and fix every error:

   ```bash
   uv run .agents/skills/validate/scripts/okf_validate.py knowledge --strict
   uv run tools/check_bundle.py
   ```

5. Open a pull request. Continuous integration runs the same checks.
6. The project lead reviews. Accepted documents gain a `verified` entry and `status: stable`.

## Reader-facing changes

Add a concise bullet to `CHANGELOG.md` under Unreleased when a change alters what a reader will find: new areas, renamed or moved documents, deprecated content. Engineering detail goes in `DEV_LOG.md`.
