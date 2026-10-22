---
type: Guide
title: Authoring workflow
description: Finding model authoring, review, and validation through Forge, the CLI, and repository skills.
tags: [semantic-foundation, finding-models, authoring, workflow, guide]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:53:02Z }
sources:
  - id: forge-workflow
    resource: https://github.com/openimagingdata/FindingModelForge/blob/15d9ebcf64734b889081feed4d645a0afca67e61/docs/finding-model-creation-workflow.md
    title: Finding model creation workflow, FindingModelForge dev branch
  - id: forge-draft
    resource: https://github.com/openimagingdata/FindingModelForge/blob/15d9ebcf64734b889081feed4d645a0afca67e61/docs/DRAFT_WORKFLOW.md
    title: Finding model draft workflow, FindingModelForge dev branch
  - id: ai-readme
    resource: https://github.com/openimagingdata/findingmodel/blob/75afd39a400419dcfaf7c8d4a34f065b4d804e0d/packages/findingmodel-ai/README.md
    title: findingmodel-ai package README, findingmodel main branch
  - id: skill-author
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/.claude/skills/finding-author/SKILL.md
    title: finding-author skill, findingmodels main branch
  - id: skill-batch
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/.claude/skills/finding-batch/SKILL.md
    title: finding-batch skill, findingmodels main branch
  - id: skill-review
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/.claude/skills/finding-review/SKILL.md
    title: finding-review skill, findingmodels main branch
  - id: core-concept
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/prompts/fragments/core_concept.md
    title: core_concept.md prompt fragment, findingmodels main branch
  - id: precommit
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/.pre-commit-config.yaml
    title: Pre-commit configuration, findingmodels main branch
  - id: cleanup-plan
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/docs/plans/definition_cleanup.md
    title: Definition Cleanup Plan, findingmodels main branch
  - id: rebuild-skills
    resource: https://github.com/openimagingdata/findingmodels/blob/4475ac1bcb591f1a0951b2082b59208def173a5d/docs/plans/rebuild-finding-skills.md
    title: Rebuild finding skills plan, findingmodels main branch
---

# Two front doors

Authors create [finding models](/glossary/finding-model.md) through Forge or repository agent skills. Forge handles one finding with a person driving. Skills support conversational and bulk authoring with human review. Both produce JSON checked by the same validator.

# Finding Model Forge

Forge is the hosted authoring front end, deployed at [fmf.oidm.org](https://fmf.oidm.org) and profiled in [applications](/applications/finding-model-forge.md). The workflow documented on its `dev` branch has four stages, all served into one page by content swaps rather than page navigation.[^forge-workflow]

1. **Basic information.** Sign in with GitHub, enter a finding name, and the application generates a description from it.
2. **Description refinement and similarity check.** Review and edit the generated description, optionally add synonyms, then check for similar existing models. If similar models are found they are shown for review; if not, a draft is created immediately.
3. **Draft editing.** The name is read-only; description, synonyms, and an attributes markdown editor are editable, and changes autosave. Generating the preview produces the full finding model JSON.
4. **Preview and submission.** The generated model is displayed with its draft status; submitting locks it.

A draft carries the user, the name, the raw inputs, the server-generated JSON, a status, and an action log. Status moves through `draft`, `submitted`, `under-review`, and then `added` or `declined`. Submitting locks further editing, and resuming a submitted name goes to the final display view.[^forge-draft] Editing a model after it has been published is open as issue 13 and is not implemented on `main`.

# The findingmodel-ai command line

Install `findingmodel-ai` from PyPI and configure an API key for at least one provider.[^ai-readme] Its main authoring commands are:

```bash
findingmodel-ai make-info "pneumothorax"        # name to description and synonyms
findingmodel-ai make-stub-model "pneumothorax"  # a basic model template
findingmodel-ai markdown-to-fm outline.md       # markdown outline to a finding model
```

The same functions are available as a Python API, and an optional web-search key enables a detail pass that returns citations alongside the generated description. Model choice is configurable per agent.

# Agent skills in the content repository

Three skills in `findingmodels/.claude/skills/` handle authoring and review.

| Skill | Use it when | Shape |
|---|---|---|
| `finding-author` | one finding at a time, discussed interactively | search, then either add a synonym to an existing model or draft a new one |
| `finding-batch` | a list, CSV, or directory of source content | triage the whole batch, then draft each finding in an isolated sub-agent |
| `finding-review` | existing definition files named by path, glob, or directory | lint, then review each file in an isolated sub-agent, then human sign-off |

Skills load rules, command cheatsheets, and procedures from `prompts/fragments/` as needed.[^skill-author] Sixteen fragments cover naming, synonyms, scope, presence, change, associated versus component findings, search, triage, lint, quality review, review files, CSV writeback, and review-interface handoff. Every skill starts with `core_concept.md`, whose principles are "a finding is a noun phrase; everything else is an attribute" and "findings exist in time."[^core-concept] At session start, the skill confirms defaults from `defaults.yml` for contributor, organization, identifier source codes, and campaign tags.

Three constraints run through all three skills.

- **Context isolation is mandatory in bulk work.** Each finding in a batch, and each file in a review, is handled by a fresh sub-agent with no exposure to its neighbors, so one finding's drafting cannot contaminate the next.[^skill-batch]
- **Search results are evaluated, not forwarded.** The skill generates two or three complementary search targets, pools the results, judges them itself, and reports one of three outcomes rather than handing the user a raw candidate list.[^skill-author]
- **Review starts from a clean tree.** The review skill refuses to run when `defs/` has uncommitted changes, so its edits can be diffed cleanly. There is no command-line override; the user overrides it conversationally.[^skill-review]

Review runs mechanical lint first, with auto-fix for trivially fixable errors such as underscores in names and self-synonyms, then a quality pass, then a terminal interface where a person approves, requests changes, or reverts through git.

# The gate every route passes

A pre-commit hook runs `uv run scripts/validator.py --with-git-adds` serially on every commit, even without staged definitions.[^precommit] It validates all `defs/` files, rejects duplicate finding or attribute identifiers, reformats JSON, rebuilds `text/`, the corpus index, and `ids.json`, then stages the results. See [identifiers](/semantic-foundation/finding-models/identifiers.md).

Regeneration keeps derived files consistent with definitions. Repository guidance prohibits editing them by hand.

# Requests and cleanup

Content requests arrive as GitHub issues on the content repository. Five of the ten open issues are content batch requests, naming RadElement-derived definitions, chest CT and chest radiograph device lists, abdomen CT findings, knee MRI findings, and CDEStaging source material. Those issues are what the in-flight branches described in [the content catalog](/semantic-foundation/finding-models/content-catalog.md) are working against.

Two plan documents on `main` govern the conventions the workflow applies.

- **The definition cleanup plan**, marked draft and for review, is a conventions pass over the existing corpus rather than new authoring. It sequences the work: lowercase 123 title-cased names and move acronyms to synonyms, add the missing presence and change-from-prior attributes to 124 models that lack them, resolve 84 names carrying population qualifiers, audit synonyms, split or re-attribute 71 names containing a "with" clause, fix punctuation on 18, and finally reclassify the Gamuts entries that are differential-diagnosis patterns rather than findings, which the plan flags as needing a design discussion.[^cleanup-plan]
- **The rebuild finding skills plan** tracks the restructuring of the skill surface into rule fragments, substep fragments, review fragments, relocated scripts, and trigger evaluations. Phases 0 through 8 are done; end-to-end verification and the final plan update remain.[^rebuild-skills]

[^forge-workflow]: Finding model creation workflow, FindingModelForge dev branch
[^forge-draft]: Finding model draft workflow, FindingModelForge dev branch
[^ai-readme]: findingmodel-ai package README, findingmodel main branch
[^skill-author]: finding-author skill, findingmodels main branch
[^skill-batch]: finding-batch skill, findingmodels main branch
[^skill-review]: finding-review skill, findingmodels main branch
[^core-concept]: core_concept.md prompt fragment, findingmodels main branch
[^precommit]: Pre-commit configuration, findingmodels main branch
[^cleanup-plan]: Definition Cleanup Plan, findingmodels main branch
[^rebuild-skills]: Rebuild finding skills plan, findingmodels main branch
