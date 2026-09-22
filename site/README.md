# Site

Renders `knowledge/` (the OKF bundle) as a static [Quartz](https://quartz.jzhao.xyz) site.

Quartz itself is not vendored in this repository — only our config and two small
plugins live here. `build.sh` clones Quartz at a pinned commit into `site/.quartz-src/`
(gitignored) at build time and points it at `knowledge/`.

## What's here

| Path | Purpose |
|---|---|
| `quartz.config.yaml` | Site config: theme, plugins, layout |
| `okf-meta-plugin/` | Component that renders OKF frontmatter as a badge row |
| `okf-lightbox-plugin/` | Component that adds a click-to-zoom image viewer |
| `build.sh` | Clones Quartz, wires up the plugins, builds |

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

## okf-lightbox-plugin

A Quartz component plugin (hand-written ESM in `dist/`, no build step, no external
dependency) that turns every diagram image in an article into a click-to-zoom overlay,
so wide SVGs squeezed into the text column can be inspected without leaving the page.

- Clicking an `article img` (or its wrapping link) opens the image in a full-viewport
  overlay: mouse wheel or pinch to zoom around the cursor/touch point, drag to pan,
  double-click to reset, Esc/click-outside/close-button to dismiss.
- The plain link is still the fallback — middle-click or Ctrl/Cmd-click bypasses the
  overlay and opens the image in a new tab as normal, and the overlay's own "Open full
  size" button does the same (that one's the true 1:1 resolution, in a new tab).
- The overlay itself opens at `scale = 0.92 * viewportWidth / imageWidth` — width-driven
  only, no height term, floored at whatever scale the image was already rendering at
  inline so opening it can never look like a regression. It opens scrolled to the top of
  the diagram rather than vertically centered, since the point is reading top-to-bottom;
  height overflow is normal and the stage pans. This is deliberately *not* a min(width,
  height) "fit the whole image" calculation: these diagrams are all portrait (taller
  than wide) while browser viewports are landscape, so a height term is almost always
  the binding constraint and produces an overlay image *narrower* than the already
  size-squeezed inline column — exactly backwards from the point of clicking in.
  Double-click and the Reset button return to this same fitted scale, not literal 1:1.
- The `naturalW`/`naturalH` this is computed from is the image's real intrinsic
  resolution, not the CSS-squeezed inline size and not `<img>.naturalWidth` either.
  Every diagram SVG in this bundle has a `viewBox` but no `width`/`height` attribute, so
  `<img>.naturalWidth` reports the CSS default-object-size fallback (~300px) rather than
  the SVG's actual dimensions — the plugin fetches the SVG and reads its `width`/`height`
  or `viewBox` directly instead of trusting `naturalWidth`.
- The component itself renders no markup — it only registers a component so Quartz
  collects its CSS and client script (see `componentResources.ts` in Quartz core) and
  is declared with `layout.position: afterBody`, which is part of Quartz's *shared*
  layout and so applies to every page type, not just `content` pages.
- The click handler is registered on `document` in the capture phase specifically so it
  runs before Quartz's SPA router's click listener on `window` — otherwise a click on
  the image's wrapping `<a class="internal internal-link">` would be treated as page
  navigation to the raw `.svg` file. The overlay element is re-appended to `document.body`
  on Quartz's `nav` event, since Quartz's SPA router (`micromorph`) diffs and can strip
  dynamically-added body elements not present in the freshly-fetched page.
- The script ships as `beforeDOMLoaded`, not `afterDOMLoaded`, on purpose. In a
  production build Quartz code-splits every component's `afterDOMLoaded` script into
  its own hashed file and loads them all in parallel via dynamic `import()`, awaited as
  a group before the SPA router itself initializes. That leaves a real window — narrow,
  but observed in practice on the deployed site — where a user can click a diagram
  before that chunk has loaded and registered its click interceptor, so the click falls
  through to the SPA router uncontested and silently navigates to the raw SVG.
  `beforeDOMLoaded` scripts are always bundled into one single, blocking `prescript.js`
  loaded synchronously in `<head>` before the body is even parsed, so registering the
  interceptor there guarantees it exists before anything on the page is clickable at
  all. The overlay DOM itself is still built lazily, on the first real open, which is
  safe since a real click implies the body has already rendered.
- The backdrop scrim is a fixed dark color rather than derived from `--light`/`--dark`:
  those are foreground/background *role* tokens that swap literal colors between light
  and dark mode (in dark mode `--dark` is a near-white text color), so using either for
  a dimming backdrop would invert in dark mode. Toolbar buttons and hint text do use
  the theme variables and correctly adapt.

## Link resolution

The bundle uses two link styles the OKF spec allows: bundle-absolute links (`/dir/file.md`) in concept documents and `./file.md` links in directory indexes. Quartz's `markdownLinkResolution` handles one style at a time, so `build.sh` first runs `tools/prepare_site_content.py`, which copies `knowledge/` to a temporary directory outside the repository (Quartz skips gitignored paths) and rewrites every internal link to the bundle-absolute form. Quartz then builds from that copy with `markdownLinkResolution: absolute`. The bundle in git is never modified.

## Hosting: Cloudflare Workers static assets

`site/wrangler.jsonc` defines an assets-only Worker named `oidm-knowledge` that serves `public/`. Its `html_handling: auto-trailing-slash` gives exactly the clean URLs Quartz links to (`/glossary/oifm` serves `glossary/oifm.html`, `/glossary/` serves the folder index), so no link rewriting is needed anywhere. `task deploy` builds and deploys; `task preview` serves the build locally through Wrangler. Continuous deployment on push to `main` is in `.github/workflows/deploy.yml` and needs the repository secrets `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`. Worker logic (comments, endpoints) can be added to the same Worker later without changing the site build.

The earlier object-storage publishing path (link flattening plus a bucket upload) was removed once Cloudflare became the host.
