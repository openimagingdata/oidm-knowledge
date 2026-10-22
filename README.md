# OIDM knowledge

Source-grounded, high-level documentation for the Open Imaging Data Model (OIDM): the finding models, common data elements, anatomic locations, and exam types that form its semantic foundation; the Observation, Exam Finding List, Imaging Problem List, and Imaging Persona data structures built on them; and the applications that use them.

The content is an [Open Knowledge Format](https://okf.md) 0.2 bundle in [`knowledge/`](knowledge/index.md). Start at the [root index](knowledge/index.md), then the overview and the glossary. Working repositories in the [openimagingdata](https://github.com/openimagingdata) organization keep code documentation and reference this repository for everything else.

## Current work

Follow the [single implementation plan](docs/plans/implementation.md) for current
decisions and the proposed reconstruction. The existing generated bundle is
retained in this commit; its planned move to a temporary archive is a separate
change. New concept drafting remains paused pending the recorded plan review.

Owner guidance and historical source evidence are preserved in
[project direction](docs/references/project-direction.md) and
[the idea inventory](docs/references/idea-coverage.md). Temporary review previews
live in ignored `scratch/review/`, exposed locally through `.peruseshow`.
Website content in `site/content/` builds independently of the knowledge bundle.
Its build, checks, and review tools use `task site:...`; see the
[site instructions](site/README.md) and [roadmap](site/ROADMAP.md).

## Reading it

- Browse on GitHub from [`knowledge/index.md`](knowledge/index.md).
- Source notes: [15 linked diagram summaries](docs/references/linked-diagrams/index.md), with source locators and connections to the five pillars.
- Website: `task site:check` checks its content and navigation; `task site:build` renders `site/content/` with Quartz into `public/`. Use `task site:deploy` for dev, `task site:deploy:staging` for staging, and `task site:deploy:prod` for the public website. See [site instructions](site/README.md) for deployment and production review requirements.
- Agents: read `knowledge/index.md` first, follow links only into what the task needs, and weigh `status`, `verified`, and `stale_after` in each document's frontmatter.

## Contributing

Original documents and diagram captures are kept in private storage. See
[Recover and verify source material](docs/sources.md) for the manifest and
`task sources:pull`, `task sources:check`, and `task sources:manifest` commands.
`task check` also validates the manifest without accessing private files.

See [CONTRIBUTING.md](CONTRIBUTING.md) and the [reconstruction instructions](docs/knowledge-authoring.md). `task check` runs both bundle checkers and source-manifest validation. The bundle checkers can also run directly:

```bash
uv run .agents/skills/validate/scripts/okf_validate.py knowledge --strict
uv run tools/check_bundle.py
```

Root `task verify`, `task review-status`, and `task review-list` apply to knowledge documents. Use the separate `task site:verify`, `task site:review-status`, and `task site:review-list` commands for website pages. Verification records an actual human review.

## Layout

| Path | Purpose |
|---|---|
| `knowledge/` | The OKF bundle |
| `Taskfile.yml` | Knowledge checks and review, source-file commands, visualization, and included `site:...` tasks |
| `site/` | Independent website content, tasks, checks, review tools, plugins, and Cloudflare deployment |
| `tools/` | Knowledge checks and review, source-file commands, and diagram builders |
| `.agents/skills/` | Installed OKF skills (author, validate, visualize, backfill) |
| `CHANGELOG.md` | Reader-facing changes |
| `DEV_LOG.md` | Engineering narrative |

## License

Content is licensed under [CC BY 4.0](LICENSE).
