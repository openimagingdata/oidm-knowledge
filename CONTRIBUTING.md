# Contributing

Thank you for helping document the Open Imaging Data Model. This repository holds the canonical high-level documentation; code documentation stays in the working repositories.

## Before you write

Read the [authoring guide](knowledge/guides/authoring-guide.md). It defines the document types, the frontmatter every file needs, the trust workflow, how links work, and how to migrate a document from a working repository. Agents follow the same guide.

## Ground rules

- **Facts and stated goals.** Document what exists and what the project has said it intends. Design proposals go through a separate review and are typed as such.
- **One concept per file.** Put it in the right directory and list it in that directory's `index.md`.
- **Sources.** Say what you read, pinned to a commit. Attribute specific claims with footnotes.
- **People.** Name organizations, not individuals. The project lead is the only named person.
- **Catalogs.** Describe and link. Do not copy finding model, anatomic location, or CDE catalogs into this repository.

## Workflow

1. Branch from `main`.
2. Write or edit under `knowledge/`. New agent-written documents start with `status: draft`.
3. Update the directory `index.md`, add a line to `knowledge/log.md`, and, for migrations, a row in the migration ledger.
4. Run both checkers and fix every error:

   ```bash
   uv run .agents/skills/validate/scripts/okf_validate.py knowledge --strict
   uv run tools/check_bundle.py
   ```

5. Open a pull request. Continuous integration runs the same checks.
6. The project lead reviews. Accepted documents gain a `verified` entry and `status: stable`.

## Reader-facing changes

Add a concise bullet to `CHANGELOG.md` under Unreleased when a change alters what a reader will find: new areas, renamed or moved documents, deprecated content. Engineering detail goes in `DEV_LOG.md`.
