# Current task: the site build is on dev, awaiting the project lead's look and commit

The public website now builds from `site/content/` and is deployed to dev: https://oidm-knowledge-dev.talkasab.workers.dev (2026-10-06). How the build works is in [README.md](README.md); what was done, in [HISTORY.md](HISTORY.md); what comes next, in [ROADMAP.md](ROADMAP.md); the project lead's words, in [guidance.md](guidance.md). The approach as agreed is kept at the end of this file.

`site/content/` is the website's source Markdown and the SVG figures it embeds. It is **not** an OKF bundle: OKF rules and validators do not apply to it. A page carries `title`, `description`, and, once the project lead has reviewed it, a `verified` stamp. Citations are footnotes in the page text.

## State (2026-10-22)

- Nothing from the build work is committed. Each commit waits on the project lead's explicit yes. Nothing is staged while the index is shared with the Codex session that owns the root files; that session coordinates index ownership before any staging.
- Commit order agreed with that session on 2026-10-22: the site commit first, then the knowledge-graph reset last. Then `bootstrap` is pushed (with approval), a new pull request into `main` is opened, CI runs, and the project lead reviews and merges it. A main ruleset requires one approving review and blocks force-pushes and deletion. The local pre-push hook refuses any push involving `main`, so agents never push or merge `main`. No new worktrees for now.
- The site commit holds:
  - everything under `site/`, including this file and the other three records;
  - `.github/workflows/deploy.yml`;
  - the deletion of `tools/prepare_site_content.py`;
  - the root `Taskfile.yml` integration (`includes: site:`), prepared by the Codex session;
  - the site-only parts of `README.md`, `CHANGELOG.md`, `docs/HANDOFF.md` and `DEV_LOG.md`, also prepared by that session.
- The graph and archive state and the contributor updates go in the graph commit.
- The site build needs nothing from `knowledge/`. A staging build from a copy holding only `site/` and `assets/brand/` succeeded on 2026-10-22.
- Suggested commit message:

  ```
  Build the public website from site/content/ with its own navigation and review gate

  - Navigation ordered by site/navigation.yaml replaces Quartz's explorer
  - "DRAFT / Awaiting Review" banner on dev and staging; production refuses unstamped pages
  - Site check, verify tool, and Taskfile under site/, run from the root as task site:...
  - Deploy workflow triggers on site/**, assets/brand/** and itself; OIDM logo and favicon added
  ```

- Before committing, run `task site:check` and `task site:build`. Both passed on 2026-10-22.
- The implementation report and review screenshots are in the ignored `scratch/review/site-build/` (`REPORT.md`), from `codex-impl-2`.
- Deploying to dev from a Claude session worked on 2026-10-06: `task -t site/Taskfile.yml deploy`, or `task site:deploy` with the root include.

## Next, proposed: page comments with Giscus (awaiting the project lead's yes)

The project lead asked on 2026-10-08 whether comments can run on all three sites, with each comment clearly showing which site it came from (`guidance.md`). The proposal:

- Quartz's `@quartz-community/comments` plugin, already in `quartz.config.yaml` and switched off, using Giscus (GitHub Discussions).
- One Discussions category per environment: "Comments: dev", "Comments: staging", "Comments: production". `build.sh` sets the category for its `--target`, and the comment box is labelled with the environment.
- Mapping: `pathname`, so each page has one thread per environment. The default, `url`, would also split threads by host.
- The plugin does not pass Giscus's `data-term`, so the `specific` mapping is unavailable. A thread shared across environments could not show where a comment came from, which is why there is one category per environment.
- Consequence: comments are separate per environment, and dev comments do not appear on production.
- Production is public: anyone with a GitHub account can comment there, and moderation happens in GitHub Discussions.
- The project lead's steps:
  1. Turn on Discussions for `openimagingdata/oidm-knowledge`.
  2. Create the three categories.
  3. Install the giscus GitHub app on the repository.
- Then: read the repository and category IDs from giscus.app, wire them in, and confirm on dev that threads land in the right category.
- The alternative offered was Hypothesis with a private group: comments anchored to passages, private, and needing a Hypothesis account. It was recommended for draft review. The project lead's follow-up asked about all three sites, which reads as Giscus; confirm before building.

## Open with the project lead

- Look at dev and say yes to the commit (above).
- Giscus, as proposed above.
- The agreed pages' footnotes say his guidance is "recorded verbatim in the layout plan". That plan is now only in git history; the same words are in `guidance.md`. The footnotes are agreed text, so they are unchanged until he decides.
- Figure acceptances: see the Figures table in the roadmap.

## Boundaries

- **The other track.** The knowledge graph (`knowledge/`, `archive/`, `docs/`, `DEV_LOG.md`, `CHANGELOG.md`, the root `Taskfile.yml` and `README.md`) is a separate track. A Codex session in the Herdr workspace `oidm-knowledge` owns those files. On 2026-10-22 it was pane `w3:p2`; rediscover it with `herdr pane list`.
- **Its files.** Do not edit them. Hand root changes, including site pointers, to that session through Herdr.
- **The index.** While the checkout is shared, that session stages. This session edits only site files and checks what is staged.
- **Commits.** Commit only on the project lead's explicit yes, one concrete commit at a time, with the paths agreed in the State section above.
- **Implementation.** It goes to a `codex-impl` Codex tab in the `oidm-knowledge` workspace, from a written brief. Review the screenshots and code before deploying.

## The approach as agreed (2026-10-06; implemented)

Kept as the record of what was decided and why. The build as it now works is described in [README.md](README.md). For commits and coordination, the State and Boundaries sections above are authoritative; the handoff and commit steps below are historical.

**Input.** `build.sh` builds `site/content/` directly, with `markdownLinkResolution: relative`; no staging copy, no link rewriting. `tools/prepare_site_content.py` is deleted. `index.md` (the Overview) is the landing page; Quartz does this for a root `index.md`.

**Build target.** `build.sh --target dev|staging|production`, default `dev`, so a build is a draft unless production is asked for by name. The script exports `SITE_TARGET` and sets `baseUrl` for the target. The site Taskfile passes the target in each deploy task.

**"DRAFT / Awaiting Review".** A new local component shows the banner at the top of every page, on every page type, unless `SITE_TARGET=production`. It reads the variable at build time, and an unset target counts as a draft. Quartz has no built-in banner or announcement component.

**Production gate.** A site check, `site/tools/check_site.py`, which `build.sh` runs before Quartz so no build can skip it:

- every page has `title` and `description`;
- every relative link and figure points at a file in `site/content/`;
- no Mermaid blocks;
- for `production` only, every page has a `verified` stamp. One missing stamp fails the build and names the page.

`verify.py` is reworked as `site/tools/verify.py`. It writes the stamp and nothing else (no `status`), lists unverified pages, and reports verified/total. It covers `site/content/` only. Placeholder pages need stamps too before a production build.

**Navigation (agreed 2026-10-06, after the project lead rejected both explorer routes; "make it look GOOD").** Quartz's explorer is replaced by our own navigation component, rendered at build time. It does not reorder the explorer.

- **Why not the explorer.** The explorer builds its tree in the browser from the search index. That index carries only slug, title, links, tags, and text, so frontmatter cannot reach it. Its only ordering hook is a function shipped to the browser as text. Two upstream requests for frontmatter ordering, quartz#2125 and quartz#2363, were closed at the v5 release without being implemented.
- **The order lives in one data file, `site/navigation.yaml`.** It is a nested list of page paths: the Overview, then the five pillars in order (Foundation Context, Data Structures, SDKs, Use Cases, Sample Applications), each with its pages in order. There is no function and no number scheme, and nothing in Quartz is patched.
- **What the component renders.** A Quartz component receives every page and its frontmatter at build time. It reads the file and renders a nested list of links in the left column, labelled with each page's `title`. The current page is marked and its pillar is open. It is plain HTML, works without JavaScript, and on narrow screens collapses behind a toggle.
- **The site check covers it.** It fails if a page is missing from the file, or if an entry has no page.
- **Later, optional:** offer frontmatter ordering to the explorer upstream, drafted for the project lead's review first.

**Duplicate title.** Exclude `@quartz-community/article-title` on content and folder pages; the page's own heading stays as written. The `reader-mode` excludes are fixed to full names at the same time.

**Folder listings.** Hidden with one CSS rule, `.page-listing { display: none }` (agreed 2026-10-06). Each pillar's index is agreed text that lists its own pages, in its own order.

**Plugins.** Plugins move to `site/plugins/`.

- `okf-meta-plugin` is removed; the pages carry nothing it renders.
- `okf-lightbox-plugin` becomes `site/plugins/lightbox/`, unchanged in behavior.
- The banner, the header logo, and the navigation go in a new `site/plugins/site-chrome/`.
- A `site/.gitignore` re-includes `plugins/*/dist/`, so the plugin code is tracked without touching the root `.gitignore`.
- `build.sh` links preact into each plugin that needs it, as it does now for one.

**Config clean-up.**

- Mermaid off.
- Off, because nothing on the site uses them: `latex`, `canvas-page`, `bases-page`, `tag-page`, and `tag-list`.
- `pageTitle` becomes "Open Imaging Data Model: Knowledge" (the project lead, 2026-10-06).
- The explorer is off, replaced by the navigation above.
- Graph view, backlinks, search, the table of contents, RSS, and the theme stay as they are. Theme and typography are later work.

**Brand assets.**

- `build.sh` copies the files the site uses from `assets/brand/oidm/` into the checkout's `quartz/static/`, so nothing is duplicated in git.
- The square mark replaces Quartz's `icon.png`, from which the favicon plugin makes `favicon.ico`.
- The header shows the full logo, linked to the Overview, in place of the text title: `logo-color` in light mode, `logo-white` in dark.
- The brand guide notes that the mark's legibility at favicon size needs checking; I will look at it.

**Placeholder pages.** These are the seven pages the agreed pages link to. Each has a `title` and a `description`. Its body says what the page will cover, drawn from the agreed pages and the project lead's guidance, then "This page is coming." The project lead agreed the text below on 2026-10-06.

| Page | Title | Proposed body (before "This page is coming.") |
|---|---|---|
| `data-structures/index.md` | Data Structures | The patient-side structures: the Observation, the Exam Finding List, the Imaging Problem List, and the Imaging Persona, and how the patient graph and the Foundation Context graph work together. These structures are still coalescing, so each source's current version will be shown side by side, dated. |
| `sdks/index.md` | SDKs | The tools that wrap the data structures so developers can create, read, and manipulate instances in real applications, and the tools that help author and maintain Foundation Context itself. |
| `use-cases/index.md` | Use Cases | A list of the applications, tools, plugins, and output products an ecosystem built on this foundation could support, with a fuller page for some of them. |
| `sample-applications/index.md` | Sample Applications | The applications the project has actually built, from demonstrations to prototypes, each with the idea it illustrates and the use cases it relates to. |
| `foundation-context/anatomic-locations.md` | Anatomic Locations | The curated index of anatomic locations anchored in RadLex: the existing work, its containment, part-of, and laterality relationships, and its incorporation into RadLex itself. |
| `foundation-context/exam-types.md` | Exam Types | The exam-type content to come: preferred high-level exam types such as CT Chest, MRI Brain, and X-ray Knee over the LOINC/RSNA Radiology Playbook, each tied to the anatomy it always, usually, or possibly includes. |
| `foundation-context/standards.md` | Standards | The standards and references Foundation Context layers over and cites (RadLex, the LOINC/RSNA Radiology Playbook, SNOMED CT, FMA, ICD, CPT, Radiopaedia, and Wikipedia), and what each contributes. |

**Tasks and deploys.**

- Site tasks go in their own `site/Taskfile.yml`. The root Taskfile's tasks belong to the graph (its `check` runs the graph's validators; `sources:*` and `viz` are graph work), and the other track edits that file. The site's check, build, and deploy chain is its own.
- The site tasks are `check`, `build`, `serve`, `preview`, `verify`, `review-status`, `review-list`, and `deploy` (dev), `deploy:staging`, `deploy:prod`. Deploys depend on the site check, not the graph's validators.
- The root `Taskfile.yml` includes it as `site:` (`task site:deploy`), and its old site tasks are removed. The Codex session that owns the root files made this change, and it goes in the site commit (see State). `task -t site/Taskfile.yml deploy` also works.
- The deploy workflow triggers on `site/**`, `assets/brand/**`, and its own file. It builds the staging target, which runs the site check, and skips the deploy step with a notice while the Cloudflare secrets are unset, so pushes do not fail.

**Order of work.**

1. This approach agreed.
2. Implementation in a `codex-impl` tab, from this file.
3. Local build, looked at in a browser in light and dark, desktop and phone width.
4. Deploy to dev (or the project lead runs `task -t site/Taskfile.yml deploy` if the classifier refuses it).
5. The URL to the project lead.
6. `site/README.md`, `ROADMAP.md`, and `HISTORY.md` updated.
7. One commit on his yes. Superseded on 2026-10-22: the site commit also carries the root Taskfile integration and the site parts of the root documentation (see State).

Pointer edits outside `site/` (root `README.md`, `docs/HANDOFF.md`, the root `Taskfile.yml`) go to the Codex session that owns the root files.
