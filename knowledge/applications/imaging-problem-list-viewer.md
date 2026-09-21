---
type: Project Profile
title: Imaging Problem List viewer
description: The deployed browser application that renders Imaging Problem Lists, its three-level drill-down and status sections, and the anatomy-first second-generation viewer being built on the development branch.
tags: [applications, ipl, viewer, anatomy, frontend]
status: draft
generated: { by: claude-opus-5/claude-code, at: 2026-09-21T17:00:00Z }
stale_after: 2027-09-21
sources:
  - id: ipl-main-readme
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/viewer/README.md
    title: imaging-problem-list viewer README, main branch
  - id: ipl-main-claude
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/CLAUDE.md
    title: imaging-problem-list domain model notes, main branch
  - id: ipl-deploy
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/06f64a7893b444b761dc069ed86140a081195eac/DEPLOYMENT.md
    title: imaging-problem-list deployment guide, main branch
  - id: ipl-status-commit
    resource: https://github.com/openimagingdata/imaging-problem-list/commit/06f64a7893b444b761dc069ed86140a081195eac
    title: "imaging-problem-list commit 06f64a7, \"Display findings in status-based sections instead of filtering\", 2025-11-18"
  - id: viewer-v2-plan
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/viewer-v2-anatomy-dashboard.md
    title: viewer_v2 anatomy-aware IPL viewer plan, imaging-problem-list dev branch
  - id: anat-plan
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/docs/plans/anatomic-location-efl-ipl.md
    title: Anatomic locations for Exam Finding Lists and Imaging Problem Lists plan, imaging-problem-list dev branch
  - id: ipl-dev-claude
    resource: https://github.com/openimagingdata/imaging-problem-list/blob/36fa30c7383bf687d7bc17815282a93e123a56cb/CLAUDE.md
    title: imaging-problem-list domain model notes, dev branch
---

# Purpose

The viewer is the demonstration that an [Imaging Problem List](/glossary/imaging-problem-list.md) is worth assembling. It takes the reorganization of a patient's findings by finding rather than by date and puts it on screen, so that "has this finding ever been described, and is it present now" is a glance instead of a chart review. The January 2026 status deck names an Imaging Problem List browser among the demonstration applications of the applications pillar.

Two viewers exist. The deployed one is on `main`. A second-generation, anatomy-first viewer called `viewer_v2` sits on `dev` and is not deployed.

# The deployed viewer

## What a user does with it

Navigation is three levels deep, held entirely in client-side state.[^ipl-main-readme]

1. **Patient level.** The [Imaging Problem List](/data-structures/imaging-problem-list.md): every finding described across the patient's exams. A dropdown switches patients, and a `?patient=` query parameter selects one directly.
2. **Exam level.** Clicking through a finding's exam entry opens that exam's [Exam Finding List](/data-structures/exam-finding-list.md).
3. **Report level.** From there, the raw report text the findings came from.

Findings are grouped into sections by temporal status rather than filtered by it. Status filtering existed and was removed in favor of status-labeled sections on 2025-11-18.[^ipl-status-commit] Four statuses are computed in the browser from each finding's observation list sorted by date, never stored in the data.

| Status | Meaning |
|---|---|
| Current | [Present](/glossary/presence.md) on the most recent exam that mentions it |
| Always | Present on every observation |
| Resolved | Present in the past, absent now |
| Never | Never described as present |

A [body region](/glossary/body-region.md) filter offers chest, abdomen, pelvis and genitourinary, musculoskeletal, and head and neck. It is driven by a static lookup table of 98 finding-to-region entries, which replaced an earlier keyword-matching approach. Clicking a finding's exam group opens a popover listing every observation of that finding in that report, not just the first, grouped by report identifier. Exam type names are shortened for display through a second lookup table, so "MR Brain WO and W contrast IV" reads as "MR Brain w/wo". The design is dark-mode-first, with the preference kept in browser local storage.

## Data it reads

Static files only, laid out by patient and exam.

```text
data/patients.json
data/patients/<patient-id>/patient.json
data/patients/<patient-id>/ipl.json
data/patients/<patient-id>/exams/<exam-id>/efl.json
data/patients/<patient-id>/exams/<exam-id>/report.txt
data/finding_region_mappings.json
data/exam_type_mappings.json
```

The deployed bundle carries two patients: one with 10 exams and 98 aggregated Imaging Problem List findings, and one with 2 exams.[^ipl-main-readme] Those files are generated from the sample data described in [sample data](/data-structures/sample-data.md) by scripts in the repository. No server, no API, no database.

## Language model use

None in the viewer. Everything it renders was produced upstream.

## Architecture

One page of Alpine.js state, with Tailwind and Flowbite loaded from a content delivery network and no build step at all. Status computation, region filtering, and popover assembly are plain JavaScript over the loaded JSON.

## Deployment

Live at [imaging-problem-list.pages.dev](https://imaging-problem-list.pages.dev), verified responding on 2026-09-21. Deployment is a Wrangler command that pushes the `viewer/` directory to a Cloudflare Pages project named `imaging-problem-list`; there is no continuous deployment.[^ipl-deploy]

## A documentation discrepancy

The prose in the repository's domain notes and the viewer README still describes an older three-state scheme, present, resolved, and not present or ruled out, while the shipped code computes the four states listed above.[^ipl-main-claude] The code is current. This is recorded in [open questions](/roadmap/open-questions.md).

# viewer_v2, the anatomy-first viewer

A separate React, Vite, TypeScript, and Tailwind static application under `viewer_v2/` on the `dev` branch. Its plan is marked "Body-map redesign implemented; ready for review" and is not archived, so it is in flight.[^viewer-v2-plan]

**The governing rule.** The viewer trusts the Imaging Problem List. Each finding identifier in the list is the canonical clinical problem row, and anatomy grouping is presentation only: it must never merge or split findings. Clinical reconciliation of compatible anatomic locations is explicitly out of scope and belongs to the follow-on step in the anatomic location plan.[^anat-plan]

**What it shows.** A single patient, the ten-exam example, presented anatomy first: an abstract body-map schematic rather than an anatomical illustration, with extremities lateralized so the right side renders on the viewer's left and the left on the viewer's right, and findings with no stated side kept separate from both. Diagram zones show the actual active finding names as clickable chips rather than a count badge. From there the detail pane opens progressively through region, cluster, finding, and observation, with finding timelines, finding-definition metadata, and drill-down to the exam, its Exam Finding List, and the report. The theme is a dark radiology-workstation palette, and the plan states that a light presentation is not acceptable for this version.

**Evidence highlighting.** Quotes are highlighted in the source report by whitespace-normalized exact match only, after folding Unicode compatibility forms, dashes, and smart quotes. No fuzzy matching. A quote that cannot be located is recorded as a warning in the generated data rather than silently dropped.

**Data contract.** The browser reads only generated files under `viewer_v2/public/data/`, never the sample data, the viewer's own data directory, or the anatomic location database. A build script assembles that bundle from the example Imaging Problem List, its Exam Finding Lists, the matching report files, finding display metadata, and the `anatomic-locations` package. Every generated top-level file carries a schema version, and the generator fails on duplicate or missing finding identifiers, observations whose report cannot be resolved, or anatomy that resolves to nothing without an explicit unlocalized fallback. A check task regenerates the bundle and fails if the committed output has drifted.

**Stated caveats in the current pass.** The bundle covers 123 Imaging Problem List findings across 10 exams for one patient. Two findings have no specific location and use the explicit unlocalized fallback. Seven warnings are embedded in the manifest for the interface to surface: four exact-evidence misses, two missing-anatomy fallbacks, and one missing finding definition.

**Deployment.** The plan names a separate Cloudflare Pages project, `ipl-anatomy`, publishing the built output. No site responds at `ipl-anatomy.pages.dev` as of 2026-09-21, and deployment automation beyond the documented build and deploy commands is listed as out of scope for this slice.

# Repository and branch of record

`imaging-problem-list` in the `openimagingdata` organization; see [the repository map](/repositories/repository-map.md).

| Branch | Tip commit | Date | Role |
|---|---|---|---|
| `main` | `06f64a7` | 2025-11-18 | The deployed viewer and the stable data-structure specification |
| `dev` | `36fa30c` | 2026-07-22 | Branch of record for current state, 258 commits ahead; carries `viewer_v2` and the extraction platform |

The same repository holds [the report extraction platform](/applications/report-extraction-platform.md). Its one open issue, number 1, asks for a formal model layer for Observation, Exam Finding List, and Imaging Problem List and is tracked in [the data model roadmap](/roadmap/ipl-data-model-system.md).

# What it realizes

The viewer is the reading end of the [Observation](/glossary/observation.md) to [Exam Finding List](/glossary/exam-finding-list.md) to [Imaging Problem List](/glossary/imaging-problem-list.md) hierarchy described in [the data structures area](/data-structures/hierarchy.md). `viewer_v2` additionally realizes [anatomic location](/glossary/anatomic-location.md) coding as a navigational axis, which is only possible because location codes were added to the findings themselves under [the assignment rules](/data-structures/anatomic-location-assignment-rules.md), and because the Imaging Problem List grouping key on `dev` became the finding code together with the location identifier.[^ipl-dev-claude]

[^ipl-main-readme]: imaging-problem-list viewer README, main branch
[^ipl-main-claude]: imaging-problem-list domain model notes, main branch
[^ipl-deploy]: imaging-problem-list deployment guide, main branch
[^ipl-status-commit]: imaging-problem-list commit 06f64a7, 2025-11-18
[^viewer-v2-plan]: viewer_v2 anatomy-aware IPL viewer plan, imaging-problem-list dev branch
[^anat-plan]: Anatomic locations for Exam Finding Lists and Imaging Problem Lists plan, imaging-problem-list dev branch
[^ipl-dev-claude]: imaging-problem-list domain model notes, dev branch
