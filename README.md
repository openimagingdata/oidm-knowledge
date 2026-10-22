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
Website work belongs to its separate session and [roadmap](site/ROADMAP.md).

## Reading it

- Browse on GitHub from [`knowledge/index.md`](knowledge/index.md).
- Source notes: [15 linked diagram summaries](docs/references/linked-diagrams/index.md), with source locators and connections to the five pillars.
- Rendered site: `task build` renders it with Quartz into `public/`; `task deploy` publishes it to Cloudflare (Workers static assets, `site/wrangler.jsonc`); pushes to `main` deploy through `.github/workflows/deploy.yml`.
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

## Layout

| Path | Purpose |
|---|---|
| `knowledge/` | The OKF bundle |
| `Taskfile.yml` | `task check`, `task build`, `task serve`, `task deploy`, `task preview`, `task verify`, `task review-status`, `task viz` |
| `site/` | Quartz configuration, badge plugin, build script, Cloudflare Worker config |
| `tools/` | House-rules checker, verification tool, diagram builders, site staging script |
| `.agents/skills/` | Installed OKF skills (author, validate, visualize, backfill) |
| `CHANGELOG.md` | Reader-facing changes |
| `DEV_LOG.md` | Engineering narrative |

## License

Content is licensed under [CC BY 4.0](LICENSE).
