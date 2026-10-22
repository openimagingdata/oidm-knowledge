# OIDM knowledge

Source-grounded, high-level documentation for the Open Imaging Data Model (OIDM): the finding models, common data elements, anatomic locations, and exam types that form its semantic foundation; the Observation, Exam Finding List, Imaging Problem List, and Imaging Persona data structures built on them; and the applications that use them.

The repository-only knowledge graph is an [Open Knowledge Format](https://okf.md) 0.2 bundle in [`knowledge/`](knowledge/index.md). It currently contains its index and change log; concept reconstruction has not started. The old generated bundle is temporarily held in [`archive/knowledge/`](archive/README.md) to check fresh drafts for useful omissions, and will be deleted after recovery is complete. Working repositories in the [openimagingdata](https://github.com/openimagingdata) organization retain their code documentation.

## Current work

Follow the [source-to-pages implementation plan](docs/plans/implementation.md) for private source storage, detailed references, and the repository knowledge graph. The outward-facing pages and website are a separate track in `site/`, planned in [site/ROADMAP.md](site/ROADMAP.md). The website builds only `site/content/`, which is independent Markdown content rather than an OKF bundle. See [site instructions](site/README.md) for its checks, review process, and deployment.

Owner guidance and historical evidence remain in [project direction](docs/references/project-direction.md) and [idea coverage](docs/references/idea-coverage.md).

Local review renders and working research live in ignored `scratch/review/`, exposed through `.peruseshow`. Accepted assets remain tracked with the content. Private source files live at `~/data/oidm-knowledge-sources`; an ignored `sources` symlink preserves existing local citations. All 307 objects in the `oidm-knowledge-sources` Tigris bucket have been checksum-verified. Use the [source instructions](docs/sources.md) and `task sources:pull` / `task sources:check` for the manifest-selected collection.

## Reading it

- Browse on GitHub from [`knowledge/index.md`](knowledge/index.md).
- Source notes: [15 linked diagram summaries](docs/references/linked-diagrams/index.md), with source locators and connections to the five pillars.
- Website: `task site:check` checks its content and navigation; `task site:build` renders `site/content/` with Quartz into `public/`. Use `task site:deploy` for dev, `task site:deploy:staging` for staging, and `task site:deploy:prod` for the public website. See [site instructions](site/README.md) for deployment and production review requirements.
- Agents: read `knowledge/index.md` first, follow links only into what the task needs, and weigh `status`, `verified`, and `stale_after` in each document's frontmatter.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [Writing the new knowledge graph](docs/knowledge-authoring.md). `task check` runs both bundle checkers and validates the source manifest. The bundle checkers can also run directly:

```bash
uv run .agents/skills/validate/scripts/okf_validate.py knowledge --strict
uv run tools/check_bundle.py
```

Root `task verify`, `task review-status`, and `task review-list` apply to the knowledge graph. Use `task site:verify`, `task site:review-status`, and `task site:review-list` for website pages. Verification commands record actual human review.

## Layout

| Path | Purpose |
|---|---|
| `knowledge/` | The new repository-only OKF graph, reconstructed from fresh documents |
| `archive/knowledge/` | Temporary old generated bundle for recovery; delete when recovery is complete |
| `Taskfile.yml` | Knowledge checks, source recovery, review tools, visualization, and included `site:...` tasks |
| `site/` | Independent website content, tasks, checks, review tools, Quartz configuration, and Cloudflare deployment |
| `tools/` | Knowledge house-rules checker, verification tool, source recovery, and diagram builders |
| `.agents/skills/` | Installed OKF skills (author, validate, visualize, backfill) |
| `CHANGELOG.md` | Reader-facing changes |
| `DEV_LOG.md` | Engineering narrative |

## License

Content is licensed under [CC BY 4.0](LICENSE).
