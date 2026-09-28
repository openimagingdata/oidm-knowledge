# Icon sources

Icons used in `build_pillars.py` (the five-pillar stack diagram). Each SVG here is the
**unmodified original** as fetched from its source repository. Recoloring (stroke/fill set
to a band's dark color) and resizing happen at build time in `build_pillars.py`, not by
editing these files, so the licensed originals stay intact and auditable.

## Health Icons

<https://healthicons.org> — outline style. Source repository:
[`resolvetosavelives/healthicons`](https://github.com/resolvetosavelives/healthicons)
(branch `main`). The project site states the icon designs are released under **CC0**
(public domain); the repository's own `LICENSE` file (covering the repo/tooling) is MIT,
copyright Resolve to Save Lives. Either way, reuse with attribution here is unrestricted.

| File | Source path | Used for |
|---|---|---|
| `healthicons-lungs.svg` | `public/icons/svg/outline/body/lungs.svg` | Anatomic locations (Foundation Context) |
| `healthicons-xray.svg` | `public/icons/svg/outline/devices/xray.svg` | Exam types (Foundation Context) |
| `healthicons-person.svg` | `public/icons/svg/outline/people/person.svg` | Imaging Persona (Data Structures) |

Note: Health Icons' outline set has no clipboard/report-style icon (searched the full tree
for "clipboard", "report", "record", "chart", "form", "doc" — nothing fits). Per the brief,
Lucide's `clipboard` and `clipboard-list` are used instead for Observation and Exam Finding
List. No CT-scanner icon exists either; `xray.svg` (x-ray machine) stands in for the exam
types glyph.

## Lucide

<https://lucide.dev>, MIT-family license. Source repository:
[`lucide-icons/lucide`](https://github.com/lucide-icons/lucide) (branch `main`), path
`icons/<name>.svg`. Lucide icons are ISC-licensed by Lucide Icons and Contributors, **except**
a subset carried over from the Feather icon project, which stays under Feather's original MIT
license (Copyright Cole Bemis). Of the icons used here, only `clipboard` is in that
Feather-derived subset.

| File | Source path | Used for | License |
|---|---|---|---|
| `lucide-book-open.svg` | `icons/book-open.svg` | Foundation Context band | ISC |
| `lucide-tag.svg` | `icons/tag.svg` | Finding/diagnosis definitions | ISC |
| `lucide-layers.svg` | `icons/layers.svg` | Data Structures band | ISC |
| `lucide-list.svg` | `icons/list.svg` | Imaging Problem List | ISC |
| `lucide-package.svg` | `icons/package.svg` | SDKs band (code-2 has no matching filename in the current icon set; package is the listed alternative) | ISC |
| `lucide-lightbulb.svg` | `icons/lightbulb.svg` | Use Cases | ISC |
| `lucide-app-window.svg` | `icons/app-window.svg` | Sample Applications | ISC |
| `lucide-clipboard.svg` | `icons/clipboard.svg` | Observation (Health Icons has no equivalent) | MIT (Feather) |
| `lucide-clipboard-list.svg` | `icons/clipboard-list.svg` | Exam Finding List (Health Icons has no equivalent) | ISC |

## Harmonizing style

- All icons are rendered at the same on-page size (~28px at 900px diagram width).
- Lucide icons are stroke-based (`stroke="currentColor"`, `stroke-width="2"`, 24x24 viewBox)
  — the build script replaces `currentColor` with the target band's dark hex.
- Health Icons' outline set is filled-path-based (`fill="currentColor"`, 48x48 viewBox), not
  stroke-based; there is no stroke-width to match, but at matched render size the two sets'
  line weights read the same. The build script replaces `currentColor` with the target hex
  the same way.

The "relationships" glyph (three dots joined by lines, repeated between the Foundation
Context blocks) is hand-drawn with primitive ellipses/lines in `excalib.py`, not sourced
from an icon set — neither Health Icons nor Lucide's `network` icon (which is box-based,
not three dots) matched the brief's description closely enough.

Reused without additions by build_three_axes.py (tag, lungs, xray) and build_two_planes.py (layers, book-open, clipboard-list, clipboard, xray, lungs, tag), 2026-09-28.
