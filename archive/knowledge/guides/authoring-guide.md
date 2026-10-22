---
type: Guide
title: Authoring guide
description: How humans and agents write, migrate, link, and verify documents in this knowledgebase.
tags: [meta, conventions, okf]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md
    title: Open Knowledge Format specification, version 0.2
  - id: cde-checker
    resource: https://github.com/RSNA/ACR-RSNA-CDEs/blob/next-gen-2026/docs/check_bundle.py
    title: Bundle checker from the ACR-RSNA-CDEs next-gen-2026 branch, whose conventions this bundle inherits
---

# Overview

This repository holds the canonical public, high-level documentation for the Open Imaging Data Model (OIDM). The `knowledge/` directory is an Open Knowledge Format (OKF) 0.2 bundle of Markdown files with YAML frontmatter for people and agents.[^okf-spec] Everything in this guide is enforced by two checkers described at the end.

Follow these rules:

1. One concept per file, typed, described, and sourced.
2. Facts and stated goals only. Proposals belong to a separate workstream and are marked as such when they arrive.
3. Organizations, not individuals. The project lead is named as such; nobody else is named.

# Directory map

| Directory | Holds |
|---|---|
| `overview/` | What OIDM is, the vision, how the layers fit |
| `glossary/` | One term per file; the vocabulary of record |
| `semantic-foundation/` | Finding models, common data elements, anatomic locations, exam types, terminologies |
| `data-structures/` | Observation, Exam Finding List, Imaging Problem List, Imaging Persona, FHIR mapping |
| `applications/` | Tools built on the foundation |
| `roadmap/` | Stated goals and open questions, by area |
| `history/` | Lineage repositories, prior approaches, site articles, use cases |
| `repositories/` | Map of every source repository and its branch of record |
| `references/` | Verbatim and near-verbatim source material (the OKF `references/` convention) |
| `guides/` | This guide and the migration ledger |
| `plans/` | Plans for building and maintaining the knowledgebase |

Each directory needs an `index.md` listing its concepts and subdirectories, one per line. Index entries use the `./` prefix so the site's absolute link resolution keeps them inside the directory:

```markdown
* [Title](./file.md) - description
* [Subdirectory](./subdir/) - description
```

Only the bundle-root index has frontmatter, declaring `okf_version`. Record changes newest first in root `log.md`, under `## YYYY-MM-DD` headings.

# Frontmatter

Copy this template. `type`, `title`, `description`, and `generated` are required by the house checker; OKF itself requires only `type`.

```yaml
---
type: Concept
title: Exam Finding List
description: One sentence saying what this document covers.
tags: [data-structures, ipl]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T14:00:00Z }
stale_after: 2027-09-21
sources:
  - id: ipl-readme
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/<commit>/README.md
    title: imaging-problem-list README
    last_modified: 2025-11-18
---
```

**Types.** `type` must be one of the controlled vocabulary below. It inherits Reference, Analysis, Decision Record, Proposal, Playbook, Worked Example, Presentation Extract, Meeting Notes, Draft Specification, Gap Log, and Exploration from the ACR-RSNA-CDEs next-gen bundle.[^cde-checker] This repository adds Overview, Concept, Glossary Term, Format Specification, Data Structure, Project Profile, Guide, Roadmap, History, Source Extract, and Plan. Reserve Proposal and Decision Record for the proposals workstream.

| Type | Use it for |
|---|---|
| Overview | A top-level orientation page |
| Concept | A narrative explanation of an idea, relationship, or rationale |
| Glossary Term | One term, its definition, its synonyms, and where it is used |
| Format Specification | A file or record format: fields, types, identifiers, examples |
| Data Structure | A data object in the Observation to Imaging Persona hierarchy |
| Project Profile | A repository, tool, or site: purpose, status, branch of record, how to use it |
| Guide | How to do something |
| Reference | Tables, lists, catalogs, extracted specifications |
| Roadmap | Stated goals and direction for an area, with sources |
| History | What was tried before and what survives |
| Source Extract | A migrated or extracted document kept close to verbatim |
| Presentation Extract | A deck or talk, extracted |
| Worked Example | A concrete example with real data |
| Plan | A plan for work on this knowledgebase |

**Status and trust.** Start agent-written documents as `status: draft`. After review, the project lead adds `verified: [{ by: human:talkasab, at: <ISO 8601> }]` and sets `status: stable`. Keep deprecated content, set `status: deprecated`, and note it in `log.md`. Set `stale_after` one year out for project profiles and roadmaps.

**Actors.** Use `<producer>/<version>` for agents or tools, `human:<id>` for people, and `process:<id>` for automation in `generated.by` and `verified[].by`, following the OKF actor convention. Use the `human:` prefix whenever a person authored or signed off; trust tiers key off it. `generated` names the actor that last wrote the document's text; a copy-editing pass by another actor updates it, and the pass is recorded once in log.md.

**Sources.** List what you actually read. Pin GitHub links to a commit, not a branch, so a reader can tell what version was read. Attribute claims with footnote labels matching source `id` values. Put a migrated document's origin first.

# Writing

- Lead with what the thing is and why it exists, then how it works, then where it lives. Each area gets a narrative "why" and a technical "how"; keep them in separate documents when both are long.
- State facts as facts and goals as goals. A goal cites the deck, issue, or plan that states it. Do not draft designs.
- Describe catalogs and point to them. Never copy a catalog into this bundle. Small representative examples are welcome.
- Name the project "Open Imaging Data Model (OIDM)" on first use and "OIDM" after. Name a finding model definition "Open Imaging Finding Model (OIFM)" on first use and "finding model" after. Name repositories by their GitHub name in code font. The old name "Open Radiology Data Model" appears only in history.
- Name organizations. Do not name individuals other than the project lead. A denylist sweep enforces this before publish.
- Link every term to its glossary entry on first use in a document, using bundle-absolute links:

  ```markdown
  [finding model](/glossary/finding-model.md)
  ```

- Link to code and content by commit-pinned GitHub URL, and to deployed tools by their live URL.
- Use short sections, tables for field lists, and fenced code for examples. Keep headings nonempty and code fences balanced.

# Migrating a document from a working repository

1. Confirm it is documentation, not code documentation. Keep installation, API usage, and developer workflow with the code.
2. Copy the substance. Rewrite only for consistency of terms and to remove individual names. Keep the author's structure.
3. Add frontmatter: an appropriate type, `status: draft`, `generated` naming you, and `sources` whose first entry is the origin file at its commit.
4. Add glossary links on first use of terms, and links to related concepts.
5. Add a row to [the migration ledger](/guides/migration-ledger.md): source repo, path, commit, destination path, date, and whether the source should later be replaced with a link.
6. List the document in its directory's `index.md` and add a line to `log.md`.
7. Run both checkers.

# Validation

Run both from the repository root before declaring any change done.

```bash
uv run .agents/skills/validate/scripts/okf_validate.py knowledge --strict
uv run tools/check_bundle.py
```

The first checks OKF 0.2 conformance and warns on legacy fields. The second enforces this guide: type vocabulary, required frontmatter, trust-signal shape, index coverage for every directory, link resolution, balanced fences, and a sweep for email addresses and denylisted names. The project lead maintains the gitignored `tools/denylist.txt`. Continuous integration runs both on pushes to `main` and pull requests.

[^okf-spec]: Open Knowledge Format specification, version 0.2
[^cde-checker]: Bundle checker from the ACR-RSNA-CDEs next-gen-2026 branch
