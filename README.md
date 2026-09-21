# OIDM knowledge

Canonical, public, high-level documentation for the Open Imaging Data Model (OIDM): the finding models, common data elements, anatomic locations, and exam types that form its semantic foundation; the Observation, Exam Finding List, Imaging Problem List, and Imaging Persona data structures built on them; and the applications that use them.

The content is an [Open Knowledge Format](https://okf.md) 0.2 bundle in [`knowledge/`](knowledge/index.md). Start at the [root index](knowledge/index.md), then the overview and the glossary. Working repositories in the [openimagingdata](https://github.com/openimagingdata) organization keep code documentation and reference this repository for everything else.

## Reading it

- Browse on GitHub from [`knowledge/index.md`](knowledge/index.md).
- Rendered site: coming in the first release.
- Agents: read `knowledge/index.md` first, follow links only into what the task needs, and weigh `status`, `verified`, and `stale_after` in each document's frontmatter.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and the [authoring guide](knowledge/guides/authoring-guide.md). Two checkers must pass:

```bash
uv run .agents/skills/validate/scripts/okf_validate.py knowledge --strict
uv run tools/check_bundle.py
```

## Layout

| Path | Purpose |
|---|---|
| `knowledge/` | The OKF bundle |
| `tools/` | House-rules checker |
| `.agents/skills/` | Installed OKF skills (author, validate, visualize, backfill) |
| `CHANGELOG.md` | Reader-facing changes |
| `DEV_LOG.md` | Engineering narrative |

## License

Content is licensed under [CC BY 4.0](LICENSE).
