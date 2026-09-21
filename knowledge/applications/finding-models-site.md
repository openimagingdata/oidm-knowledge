---
type: Project Profile
title: Finding model catalog site
description: The static Astro site that renders the finding model corpus as browsable pages, building it from the content repository pulled in as a git submodule.
tags: [applications, finding-models, catalog, astro]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
stale_after: 2027-09-21
sources:
  - id: site-config
    resource: https://github.com/openimagingdata/finding-models-site/blob/6298fa3b900bb46b488f82d0a5b9aab06f70ca69/astro.config.mjs
    title: finding-models-site Astro configuration, main branch
  - id: site-loader
    resource: https://github.com/openimagingdata/finding-models-site/blob/6298fa3b900bb46b488f82d0a5b9aab06f70ca69/src/data/loadFindingModels.ts
    title: finding-models-site build-time model loader, main branch
  - id: site-index
    resource: https://github.com/openimagingdata/finding-models-site/blob/6298fa3b900bb46b488f82d0a5b9aab06f70ca69/src/pages/index.astro
    title: finding-models-site home page, main branch
  - id: site-submodule
    resource: https://github.com/openimagingdata/finding-models-site/blob/6298fa3b900bb46b488f82d0a5b9aab06f70ca69/.gitmodules
    title: finding-models-site submodule declaration, main branch
  - id: site-deploy
    resource: https://github.com/openimagingdata/finding-models-site/blob/6298fa3b900bb46b488f82d0a5b9aab06f70ca69/.github/workflows/deploy.yml
    title: finding-models-site GitHub Pages deployment workflow, main branch
---

# Purpose

The catalog site is the public reading surface for the [finding model](/glossary/finding-model.md) corpus. It answers one question, "what definitions exist and what is in them," without requiring a reader to install anything, clone a repository, or read JSON. [Finding Model Forge](/applications/finding-model-forge.md) writes definitions; this site displays them.

# What a user does with it

Three things, from the home page.[^site-index]

- **Browse the catalog.** A "Browse Finding Models" link leads to a list page, and each entry leads to a detail page for one definition.
- **Start authoring.** A "Launch Finding Model Forge" link goes to the sign-in page at `fmf.oidm.org`.
- **Report a problem.** A "Submit Issue" link opens a new issue against the `findingmodels` content repository, so corrections go to the content rather than to the site.

A search box is present on the home page but is not wired to anything; it is markup only.

# Data it reads

The site holds no content of its own. The `findingmodels` content repository is attached as a git submodule at `external/findingmodels`.[^site-submodule] At build time, a loader module reads every `.json` file in that submodule's `defs/` directory, parses each one, and derives the page slug from the file name.[^site-loader] There is no database, no API call, and no runtime fetch. A definition appears on the site only after the submodule pointer is advanced and the site is rebuilt.

```typescript
const modelDir = path.resolve('./external/findingmodels/defs');
```

That single line is the whole coupling between the site and the corpus, and it is why the content repository stays the source of truth for finding model identity. The corpus itself is described in [the content catalog](/semantic-foundation/finding-models/content-catalog.md) and the format in [the finding model format](/semantic-foundation/finding-models/finding-model-format.md).

# Language model use

None. The site is a deterministic renderer.

# Architecture

Astro 5 in static output mode, with Tailwind CSS 4 applied through the Astro Vite plugin and pnpm as the package manager.[^site-config] Four source files carry the whole application: a layout, a home page, a model list page, and a model detail page parameterized by slug. The configuration sets a base path of `/finding-models-site/`, which is what makes the published URLs resolve under the project's GitHub Pages subpath.

# Deployment

Live at [openimagingdata.github.io/finding-models-site](https://openimagingdata.github.io/finding-models-site/), verified responding on 2026-09-21. A GitHub Actions workflow triggers on every push to `main`, checks the repository out with submodules, installs with pnpm, runs the Astro build, and publishes `dist/` to GitHub Pages.[^site-deploy] Because the workflow fires on pushes to this repository rather than on changes in the content repository, new definitions reach the site only when someone updates the submodule pointer here.

# Repository and branch of record

`finding-models-site` in the `openimagingdata` organization; see [the repository map](/repositories/repository-map.md).

| Property | Value |
|---|---|
| Branch of record | `main`, the only branch |
| Tip commit | `6298fa3`, 2025-06-19 |
| Open issues | None |
| Open pull requests | None |
| Status | Maintenance: it is the current artifact for its purpose, with no commits since June 2025 |

The repository's README is the unmodified Astro starter boilerplate and describes nothing project-specific.

# What it realizes

The catalog site is the simplest realization of the claim that a [finding model](/glossary/finding-model.md) definition is a portable file rather than a database row. It needs no service, no credentials, and no synchronization, and it proves that a consumer can read the corpus by reading files. The same property is what lets the extraction platform resolve [OIFM identifiers](/glossary/oifm.md) against a published registry file; see [the architecture overview](/overview/architecture.md).

[^site-config]: finding-models-site Astro configuration, main branch
[^site-loader]: finding-models-site build-time model loader, main branch
[^site-index]: finding-models-site home page, main branch
[^site-submodule]: finding-models-site submodule declaration, main branch
[^site-deploy]: finding-models-site GitHub Pages deployment workflow, main branch
