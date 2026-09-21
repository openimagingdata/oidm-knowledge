# Site

Renders `knowledge/` (the OKF bundle) as a static [Quartz](https://quartz.jzhao.xyz) site.

Quartz itself is not vendored in this repository — only our config and one small plugin
live here. `build.sh` clones Quartz at a pinned commit into `site/.quartz-src/`
(gitignored) at build time and points it at `knowledge/`.

## What's here

| Path | Purpose |
|---|---|
| `quartz.config.yaml` | Site config: theme, plugins, layout |
| `okf-meta-plugin/` | Component that renders OKF frontmatter as a badge row |
| `build.sh` | Clones Quartz, wires up the plugin, builds |

`site/.quartz-src/` (the Quartz checkout), `public/` (the build output), and any
`node_modules/` under `site/` are gitignored.

## Building locally

From the repository root:

```bash
bash site/build.sh          # one-shot build -> public/
bash site/build.sh serve    # local dev server with live reload
```

Requires Node >=22 (Quartz's own requirement; the deploy workflow uses Node 24) and git.
Output lands in `public/` at the repo root.

## Deploying

`.github/workflows/site.yml` builds and deploys to GitHub Pages on every push to `main`
that touches `knowledge/**` or `site/**`. It runs the exact same `bash site/build.sh` a
contributor runs locally, so CI and local builds can't drift apart.

## The pinned Quartz commit

`build.sh` pins Quartz to one commit (`QUARTZ_SHA`) so the site doesn't move under us
between builds. To bump it:

1. Update `QUARTZ_SHA` in `site/build.sh`.
2. Update the matching `QUARTZ_SHA` value in `.github/workflows/site.yml` (used only as
   an npm cache key there — it doesn't need to match exactly, but keeping it in sync
   avoids a stale cache).
3. Run `bash site/build.sh` locally and check the result before pushing, since a newer
   Quartz commit can change config options or plugin APIs.

## okf-meta-plugin

A Quartz component plugin (hand-written ESM in `dist/`, no build step) that reads a
page's OKF frontmatter and renders it as a small badge row plus a sources list, using
the conventions in [`knowledge/guides/authoring-guide.md`](../knowledge/guides/authoring-guide.md#frontmatter):

- **Type** badge first, then **status** (`draft` / `stable` / `deprecated`).
- A **stale** badge once `stale_after` is in the past.
- One badge per `verified` entry, shown as `by (at)`. An entry whose `by` starts with
  `human:` (a person's sign-off, per the actor convention) gets a distinct
  "human-reviewed" style so it reads differently from an agent or process attestation.
- A **sources** list with each title linked to its `resource`, plus `author` and
  `last_modified` when the source entry has them.

It declares `preact` as a `peerDependency` rather than bundling its own copy, since
Quartz already provides one. Because `quartz plugin install` symlinks a local plugin
in place instead of copying it, Node resolves `import "preact"` against the plugin's
*real* path — which sits outside Quartz's own `node_modules` tree — and fails to find
it. `build.sh` works around this by symlinking Quartz's `preact` into
`okf-meta-plugin/node_modules/preact` after `npm ci`.

Note this Quartz fork moved frontmatter parsing out of core and into the
`note-properties` plugin's transformer. `quartz.config.yaml` keeps that plugin enabled
(with `hidePropertiesView: true`) purely so frontmatter gets parsed at all — its own
visible properties panel is suppressed so it doesn't duplicate okf-meta-plugin's badges.

## Link resolution

The bundle uses two link styles the OKF spec allows: bundle-absolute links (`/dir/file.md`) in concept documents and `./file.md` links in directory indexes. Quartz's `markdownLinkResolution` handles one style at a time, so `build.sh` first runs `tools/prepare_site_content.py`, which copies `knowledge/` to a temporary directory outside the repository (Quartz skips gitignored paths) and rewrites every internal link to the bundle-absolute form. Quartz then builds from that copy with `markdownLinkResolution: absolute`. The bundle in git is never modified.

## Publishing to the Tigris bucket

`task publish` (or `bash site/publish-tigris.sh [bucket] [prefix]`) does everything in one step: validates the bundle, builds with a bucket-specific config (`baseUrl` under the bucket host, client-side navigation and popovers off), rewrites every internal link in the built HTML to an explicit `.html` or `index.html` path with `tools/flatten_site_links.py` (plain object storage serves keys literally, with no clean-URL rewriting), and uploads with the Tigris CLI. Result: `https://<bucket>.t3.storage.dev/<prefix>/index.html`. The GitHub Pages build does not use the flattening step.
