# Applications

Tools built on the OIDM semantic foundation and data structures: what each one is for, who uses it, what it reads and writes, where it runs, and what is in flight on its branches. Every profile names its repository and branch of record; the full repository listing is in [the repository map](/repositories/repository-map.md).

* [Finding Model Forge](./finding-model-forge.md) - The web application at fmf.oidm.org where contributors author finding model definitions through an AI-assisted wizard and move them through a draft review lifecycle.
* [Finding model catalog site](./finding-models-site.md) - The static Astro site that renders the finding model corpus as browsable pages, building it from the content repository pulled in as a git submodule.
* [Imaging Problem List viewer](./imaging-problem-list-viewer.md) - The deployed browser application that renders Imaging Problem Lists, its three-level drill-down and status sections, and the anatomy-first second-generation viewer being built on the development branch.
* [Report extraction platform](./report-extraction-platform.md) - The extraction, coding, persistence, evaluation, and human-review platform on the imaging-problem-list development branch that turns narrative radiology reports into coded findings.
* [Finding and location coding](./finding-and-location-coding.md) - How extracted findings are assigned OIFM finding codes and RadLex anatomic location codes, as a deterministic index lookup followed by language model term generation and selection.
* [IPL MVP extraction and labeling](./ipl-mvp-extraction.md) - The 2025 four-stage prototype that extracted findings from reports and matched them to finding models by embedding similarity, its measured results, and why it was superseded.
* [Open Imaging Reporting SDK](./reporting-sdk.md) - The vendor-facing reporting toolkit named as a strategic pillar in the 2026 status deck, its 2023 plugin-container precursor, and the fact that no artifact exists.
