# Site

This directory is the website, a separate track from the knowledge graph in `knowledge/`:

| Path | What it holds |
|---|---|
| `content/` | The website's content: Markdown pages and the SVG figures they embed. Not an OKF bundle. |
| [CURRENT_TASK.md](CURRENT_TASK.md), [ROADMAP.md](ROADMAP.md), [HISTORY.md](HISTORY.md) | The work in hand, what comes next with page and figure status, and what is done. |
| [guidance.md](guidance.md) | The project lead's guidance on the website, verbatim. |
| `build.sh`, `quartz.config.yaml`, `wrangler.jsonc`, the two plugins | The build. |

Figure sources and builders are in `tools/diagrams/`; shared brand assets are in `assets/brand/` at the repository root.

The public website builds the Markdown and SVGs in `site/content/` directly with [Quartz 5](https://quartz.jzhao.xyz). The site uses relative Markdown links and does not stage or rewrite the knowledge bundle.

## Build and targets

Requires Node 22 or newer, npm, git, Python 3.11 or newer, and uv. Task is optional. Run these commands from the repository root:

```bash
bash site/build.sh                          # draft dev build into public/
bash site/build.sh --target staging         # draft staging build
bash site/build.sh --target production      # requires review stamps on every page
bash site/build.sh serve                    # dev server with live reload
SITE_BASE_URL=example.com/path bash site/build.sh --target staging
```

The default target is `dev`. Dev and staging show `DRAFT / Awaiting Review`; production omits the banner. Each target selects its Workers hostname. `SITE_BASE_URL` overrides the hostname and optional base path. The tracked config's `baseUrl` stays unchanged.

`build.sh` runs the site check before accessing Quartz, copies the config into `site/.quartz-src/`, runs `npm ci`, links shared dependencies into the local plugins, installs the plugins, and copies brand assets. Quartz then builds `site/content/` into `public/`. The checkout, build output, and plugin `node_modules/` are gitignored; hand-written plugin `dist/` files are included by `site/.gitignore`.

## Check and review pages

```bash
uv run site/tools/check_site.py
uv run site/tools/check_site.py --target production
uv run site/tools/verify.py --status
uv run site/tools/verify.py --list site/content
uv run site/tools/verify.py site/content/foundation-context/relationships.md
uv run site/tools/verify.py --by human:someone site/content/sdks/index.md
```

The site check requires non-empty `title` and `description` frontmatter on every Markdown page, valid local Markdown link and image targets under `site/content/`, no Mermaid fences, and complete navigation without duplicate entries. It ignores links inside fenced code. Production additionally requires a `verified` entry on every page, including index and placeholder pages. A missing stamp fails the build and names the page.

`verify.py` defaults to reviewer `human:talkasab`. It adds only `verified`, after `description` for a new field, or appends to existing stamps. Other frontmatter and page text retain their formatting. The tool rejects paths outside `site/content/`. Status counts every Markdown page by top-level directory; the root index appears under `.`. Verification records a human review and is run after that review.

## Navigation and site chrome

`navigation.yaml` lists paths relative to `site/content/` in display order, with optional `page` and `pages` groups. Every page appears exactly once. The Overview comes first, followed by Foundation Context, Data Structures, SDKs, Use Cases, and Sample Applications. Link labels default to each page's frontmatter `title`. A page entry can supply a non-empty `label` to override it, as the root entry does with `Overview`:

```yaml
- page: index.md
  label: Overview
```

`plugins/site-chrome/` provides `ReviewBanner`, `SiteLogo`, and `SiteNav`. The pinned Quartz layout loader selects one component per plugin entry, so three config entries use the `SiteChrome` adapter with a component option and their own layout position. All code is hand-written ESM with no build step. The build links Quartz's preact, YAML parser, and shared path utilities into the plugin.

The build exports the absolute `SITE_NAVIGATION_FILE` path so server-rendered navigation does not depend on the checkout's working directory. Direct plugin use defaults to the navigation file relative to the plugin itself. Quartz's `pathToRoot`, `resolveRelative`, and slug helpers keep logo and navigation links valid under a base path. Native `details` toggles expand pillar pages and the phone's Contents panel without JavaScript. A small Quartz `nav` event handler updates active links and pillar expansion after SPA navigation.

The logo uses the color SVG in light mode and the white SVG when Quartz sets `saved-theme="dark"` on the root element. Theme-aware CSS styles navigation, focus states, and the draft banner. The automatic `.page-listing` is hidden; pillar indexes carry their own links. Article-title components are excluded on content and folder pages because the source pages include their own headings. Graph, backlinks, search, table of contents, RSS, sitemap, and existing theme fonts and colors remain configured.

`note-properties` remains enabled to parse frontmatter, with its visible panel suppressed.

## Brand assets

The build copies `assets/brand/oidm/logo-color.svg` and `logo-white.svg` into Quartz's `static/brand/`. It restores Quartz's tracked static files before copying `mark.png` over `static/icon.png`, which the favicon plugin uses to generate `favicon.ico`. Brand files remain shared with diagram tooling rather than duplicated in this directory. See the [brand notes](../docs/brand/README.md).

## Tasks

Run `task -t site/Taskfile.yml <task>` from the repository root. Every task sets its working directory from `TASKFILE_DIR`, and the root Taskfile includes it as `site:`, so `task site:<task>` works from the root as well.

| Task | Action |
|---|---|
| `check` | Validate pages and navigation; accepts `-- --target production` |
| `build`, `serve` | Build or serve the draft dev site; accept build arguments after `--` |
| `preview` | Build and serve through Wrangler's local static-asset server |
| `verify` | Stamp reviewed paths supplied after `--` |
| `review-status`, `review-list` | Count reviews or list unverified pages; list defaults to all content |
| `deploy` | Check, build dev, and deploy to the dev Worker |
| `deploy:staging` | Check, build staging, and deploy to staging |
| `deploy:prod` | Check, build with the production gate, and deploy to the public Worker |

Deploy tasks depend on the site check. `DEV_URL`, `STAGING_URL`, and `PROD_URL` can override the target hostnames.

## Deploy workflow and hosting

`.github/workflows/deploy.yml` runs on pushes to `main` that change `site/**`, `assets/brand/**`, or the workflow itself, and on manual dispatch. It installs Node 22 and uv, caches npm using the build script, config, and plugin manifests, then checks and builds staging. It deploys only to staging when both Cloudflare secrets are set. With either secret unset, it emits a notice and succeeds after the build.

`site/wrangler.jsonc` defines assets-only Cloudflare Workers serving `public/`:

| Target | Worker |
|---|---|
| Dev | `oidm-knowledge-dev` |
| Staging | `oidm-knowledge-staging` |
| Production | `oidm-knowledge` |

Wrangler's `html_handling: auto-trailing-slash` serves clean page URLs and folder indexes. Local previews use `npx wrangler dev --config site/wrangler.jsonc --env dev`. Deployment requires `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`. Worker endpoints can be added later without changing the static build.

## Pinned Quartz

`build.sh` pins `QUARTZ_SHA` to `97a2d05f80c4c50534959b1d0d41cc4b3895625e`. Quartz is cloned into `site/.quartz-src/` rather than vendored. To update the pin, change `QUARTZ_SHA`, review the dependency and workflow cache configuration, then build locally and inspect the result. A new commit can change plugin APIs or config options.

## Lightbox

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
  Every diagram SVG on this site has a `viewBox` but no `width`/`height` attribute, so
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

## Quartz behaviour worth knowing (pinned commit `97a2d05`, checked 2026-10-06)

- Layout `exclude` lists match a plugin's full `source` string (`@quartz-community/article-title`), not its short name.
- The explorer builds its tree in the browser from the content index, which carries only slug, title, links, tags, and text. It can be ordered only by a `sortFn` sent to the browser as text. Upstream requests for frontmatter ordering (quartz#2125, #2363) were closed at the v5 release. This is why `navigation.yaml` and our own component replace it.
- `folder-page` always appends a listing of the folder's pages, with no option to turn it off; the CSS hides it. Turning `folder-page` off would stop folder `index.md` pages from rendering at all.
- `markdownLinkResolution: relative` resolves `./`, `../`, `folder/index.md` and figure links as written in `site/content/`.
- `remove-draft` acts only on `draft: true`.
- Local plugins are symlinked into the checkout, so their bare imports resolve from their real path. `build.sh` links Quartz's `preact`, `@quartz-community/utils` and `yaml` into them.
- The Giscus `comments` plugin passes no `data-term`, so Giscus's `specific` mapping is unavailable.
