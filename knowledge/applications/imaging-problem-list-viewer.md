---
type: Project Profile
title: Imaging Problem List viewer
description: The deployed Imaging Problem List browser and the undeployed anatomy-first viewer on dev.
tags: [applications, ipl, viewer, anatomy, frontend]
status: draft
generated: { by: codex/gpt-6, at: 2026-09-21T20:34:50Z }
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

**Live:** the deployed viewer is at [imaging-problem-list.pages.dev](https://imaging-problem-list.pages.dev) (main-branch data, without anatomic locations). The anatomy-first `viewer_v2` on `dev` has no public deployment as of 2026-09-21; the plan's intended address, `ipl-anatomy.pages.dev`, does not respond.

The viewer displays a patient's [Imaging Problem List](/glossary/imaging-problem-list.md) by finding, showing its history and current presence. The January 2026 status deck lists the browser as a demonstration application.

Two viewers exist. The deployed one is on `main`. A second-generation, anatomy-first viewer called `viewer_v2` sits on `dev` and is not deployed.

# The deployed viewer

## What a user does with it

Navigation has three levels, managed in client-side state.[^ipl-main-readme]

1. The patient's [Imaging Problem List](/data-structures/imaging-problem-list.md) shows findings across exams. A dropdown or `?patient=` query parameter selects the patient.
2. A finding's exam entry opens the [Exam Finding List](/data-structures/exam-finding-list.md).
3. The exam view opens the source report text.

Status sections replaced status filtering on 2025-11-18.[^ipl-status-commit] The browser computes four statuses from date-sorted observations without storing them in the data.

| Status | Meaning |
|---|---|
| Current | [Present](/glossary/presence.md) on the most recent exam that mentions it |
| Always | Present on every observation |
| Resolved | Present in the past, absent now |
| Never | Never described as present |

The [body region](/glossary/body-region.md) filter covers chest, abdomen, pelvis and genitourinary, musculoskeletal, and head and neck. A static table of 98 finding-to-region mappings replaced keyword matching. A finding's exam-group popover lists all its observations, grouped by report identifier. A second lookup table shortens exam names, such as "MR Brain WO and W contrast IV" to "MR Brain w/wo". The design prioritizes dark mode and stores the preference in browser local storage.

## Data it reads

The viewer reads static files organized by patient and exam.

```text
data/patients.json
data/patients/<patient-id>/patient.json
data/patients/<patient-id>/ipl.json
data/patients/<patient-id>/exams/<exam-id>/efl.json
data/patients/<patient-id>/exams/<exam-id>/report.txt
data/finding_region_mappings.json
data/exam_type_mappings.json
```

The deployed bundle contains two patients. One has 10 exams and 98 aggregated findings. The other has 2 exams.[^ipl-main-readme] Repository scripts generate the files from [sample data](/data-structures/sample-data.md). The viewer needs no application server, API, or database.

## Language model use

None in the viewer. Everything it renders was produced upstream.

## Architecture

One page manages Alpine.js state, with Tailwind and Flowbite loaded from a content delivery network and no build step. JavaScript computes statuses, filters regions, and assembles popovers from JSON.

## Deployment

Live at [imaging-problem-list.pages.dev](https://imaging-problem-list.pages.dev), verified responding on 2026-09-21. A Wrangler command deploys `viewer/` to the `imaging-problem-list` Cloudflare Pages project. There is no continuous deployment.[^ipl-deploy]

## A documentation discrepancy

The domain notes and viewer README describe an older three-state scheme: present, resolved, and not present or ruled out.[^ipl-main-claude] The shipped code computes the four states above. See [open questions](/roadmap/open-questions.md).

# viewer_v2, the anatomy-first viewer

`viewer_v2/` is a React, Vite, TypeScript, and Tailwind static application on `dev`. Its plan is marked "Body-map redesign implemented; ready for review" and is not archived, so it is in flight.[^viewer-v2-plan]

Each finding identifier in the Imaging Problem List defines one clinical problem row. Anatomy grouping must not merge or split findings. Clinical reconciliation of compatible locations belongs to the follow-on anatomic location work.[^anat-plan]

The viewer presents the ten-exam patient on an abstract body schematic. Right extremities appear on the viewer's left, left extremities on the right, and unsided findings stay separate. Zones show active finding names as clickable chips. The detail pane opens through region, cluster, finding, and observation, with timelines, definition metadata, and links to exams, Exam Finding Lists, and reports. This version requires a dark radiology-workstation palette.

Quotes are highlighted by exact match after whitespace normalization and folding of Unicode compatibility forms, dashes, and smart quotes. There is no fuzzy matching. Unmatched quotes produce warnings in generated data.

The browser reads only generated files under `viewer_v2/public/data/`. A build script combines the example Imaging Problem List, Exam Finding Lists, report files, finding display metadata, and `anatomic-locations` package. Every top-level file has a schema version. Generation fails on duplicate or missing finding identifiers, unresolved report references, or unresolved anatomy without an explicit unlocalized fallback. A check task regenerates the bundle and fails if it differs from committed output.

The bundle contains 123 findings across 10 exams for one patient. Two findings use the unlocalized fallback. The manifest contains seven warnings for display: four exact-evidence misses, two missing-anatomy fallbacks, and one missing finding definition.

The plan names a separate Cloudflare Pages project, `ipl-anatomy`, for the built output. No site responds at `ipl-anatomy.pages.dev` as of 2026-09-21. Further deployment automation is outside the plan's scope.

# Repository and branch of record

`imaging-problem-list` in the `openimagingdata` organization; see [the repository map](/repositories/repository-map.md).

| Branch | Tip commit | Date | Role |
|---|---|---|---|
| `main` | `06f64a7` | 2025-11-18 | The deployed viewer and the stable data-structure specification |
| `dev` | `36fa30c` | 2026-07-22 | Branch of record for current state, 258 commits ahead; carries `viewer_v2` and the extraction platform |

The same repository holds [the report extraction platform](/applications/report-extraction-platform.md). Its one open issue, number 1, asks for a formal model layer for Observation, Exam Finding List, and Imaging Problem List and is tracked in [the data model roadmap](/roadmap/ipl-data-model-system.md).

# What it realizes

The viewer displays the [Observation](/glossary/observation.md), [Exam Finding List](/glossary/exam-finding-list.md), and [Imaging Problem List](/glossary/imaging-problem-list.md) [hierarchy](/data-structures/hierarchy.md). `viewer_v2` groups navigation by [anatomic location](/glossary/anatomic-location.md), using codes assigned under [the assignment rules](/data-structures/anatomic-location-assignment-rules.md). On `dev`, Imaging Problem List groups use both the finding code and location identifier.[^ipl-dev-claude]

[^ipl-main-readme]: imaging-problem-list viewer README, main branch
[^ipl-main-claude]: imaging-problem-list domain model notes, main branch
[^ipl-deploy]: imaging-problem-list deployment guide, main branch
[^ipl-status-commit]: imaging-problem-list commit 06f64a7, 2025-11-18
[^viewer-v2-plan]: viewer_v2 anatomy-aware IPL viewer plan, imaging-problem-list dev branch
[^anat-plan]: Anatomic locations for Exam Finding Lists and Imaging Problem Lists plan, imaging-problem-list dev branch
[^ipl-dev-claude]: imaging-problem-list domain model notes, dev branch
