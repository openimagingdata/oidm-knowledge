---
type: Project Profile
title: Finding model catalog site
description: The static Astro catalog built from finding model definitions in a git submodule.
tags: [applications, finding-models, catalog, astro]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:34:50Z }
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

**Live:** [openimagingdata.github.io/finding-models-site](https://openimagingdata.github.io/finding-models-site/).

The catalog site displays [finding model](/glossary/finding-model.md) definitions without requiring installation or reading JSON. [Finding Model Forge](/applications/finding-model-forge.md) authors the definitions.

# What a user does with it

The home page links to three actions.[^site-index]

- "Browse Finding Models" opens the catalog, with a detail page for each definition.
- "Launch Finding Model Forge" opens sign-in at `fmf.oidm.org`.
- "Submit Issue" opens an issue against the `findingmodels` content repository.

The home page search box has no implemented behavior.

# Data it reads

The `findingmodels` content repository is a git submodule at `external/findingmodels`.[^site-submodule] At build time, the loader parses every `.json` file in `defs/` and derives page slugs from file names.[^site-loader] The site has no database, API calls, or runtime fetches.

```typescript
const modelDir = path.resolve('./external/findingmodels/defs');
```

That single line is the whole coupling between the site and the corpus, and it is why the content repository stays the source of truth for finding model identity. See [the content catalog](/semantic-foundation/finding-models/content-catalog.md) and [the finding model format](/semantic-foundation/finding-models/finding-model-format.md).

# Language model use

None. The site is a deterministic renderer.

# Architecture

The site uses Astro 5 static output, Tailwind CSS 4 through the Astro Vite plugin, and pnpm.[^site-config] Four source files define the layout, home page, model list, and model detail page. The `/finding-models-site/` base path resolves URLs under the GitHub Pages subpath.

# Deployment

Live at [openimagingdata.github.io/finding-models-site](https://openimagingdata.github.io/finding-models-site/), verified responding on 2026-09-21. On pushes to `main`, GitHub Actions checks out the repository with submodules, installs with pnpm, builds, and publishes `dist/`.[^site-deploy] New definitions appear only after the submodule pointer is updated and the site rebuilds.

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

The site reads portable definition files without a service or credentials. The extraction platform similarly resolves [OIFM identifiers](/glossary/oifm.md) against a published registry file. See [the architecture overview](/overview/architecture.md).

[^site-config]: finding-models-site Astro configuration, main branch
[^site-loader]: finding-models-site build-time model loader, main branch
[^site-index]: finding-models-site home page, main branch
[^site-submodule]: finding-models-site submodule declaration, main branch
[^site-deploy]: finding-models-site GitHub Pages deployment workflow, main branch
