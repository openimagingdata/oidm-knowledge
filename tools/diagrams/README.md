# Diagrams

Diagrams in the bundle are Excalidraw files rendered to SVG and placed beside the document that embeds them (`knowledge/<dir>/<name>.excalidraw` and `<name>.svg`). Mermaid is not used.

## Source-of-truth rule

Per diagram, one of two things is the source:

- **Builder-generated.** `build_<name>.py` in this directory writes the `.excalidraw` file. Edit the builder, not the file. Iterate by rendering and looking at the PNG.
- **Hand-edited.** Once anyone edits a `.excalidraw` file directly (in Excalidraw or as JSON), that file becomes the source. Retire its builder in the same change: delete `build_<name>.py` and add the diagram to the list below.

Hand-edited diagrams (builders retired): none yet.

`build_pillars.py` takes a required `--seam a|b|c` choosing how the Data
Structures and Foundation Context bands meet (named attachments, dovetail,
shared membrane) and writes `knowledge/drafts/pillars-<seam>.excalidraw`. The
v3 seam it replaced -- an overlap crossed by twelve alternating threads -- was
rejected, so `knowledge/drafts/pillars.excalidraw` is stale until one of the
three is chosen and made the default.

## Rendering

From the excalidraw-diagram skill's references directory (it holds the Playwright environment):

```bash
cd ~/.claude/skills/excalidraw-diagram/references
uv run python /home/talkasab/oidm-knowledge/tools/diagrams/render_excalidraw.py \
  /home/talkasab/oidm-knowledge/knowledge/<dir>/<name>.excalidraw \
  -o /home/talkasab/oidm-knowledge/sources/<name>-vN.png \
  --svg /home/talkasab/oidm-knowledge/sources/<name>-vN.svg
```

Then view the PNG, fix, re-render, until nothing crosses a box or a label and every label is readable. Copy the accepted SVG beside the document, drop the fixed `width`/`height` attributes on the root `<svg>` and add `style="max-width:100%;height:auto"`, and embed it with an image line plus an italic source line (see `knowledge/overview/architecture.md`).

`render_template.html` loads the Excalidraw library from esm.sh pinned to 0.18.0; the unpinned build had a broken dependency.

## Measuring text instead of estimating it

`excalib.text()` estimates a string's width at `0.58 * fontSize` per character. That is fine for a label floating in open space, but it is wrong by 20-40% for real strings, so a layout packed to the pixel (a narrow canvas, a label that must not touch a lane) cannot be built on it. Measure instead: the render font is `Helvetica, Segoe UI Emoji` as resolved by headless Chromium, so a few lines of Playwright give exact widths.

```python
# from the excalidraw-diagram skill's references directory, under `uv run`
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    pg = p.chromium.launch(headless=True).new_page(); pg.goto("about:blank")
    print(pg.evaluate("""(ss) => { const c = document.createElement('canvas').getContext('2d');
        c.font = '13px Helvetica, Segoe UI Emoji';
        return Object.fromEntries(ss.map(s => [s, c.measureText(s).width])); }""",
        ["CT Chest WO contrast", "upper abdomen"]))
```

Size a box as `measured width + 20` (`box()` pads 10px each side) and pass the measured width to any helper that draws a backing box behind a label (`build_foundation_network.py` has `label_w` / `w` parameters for this). A label backing box that sits inside a tinted band should use the band's fill, not white.

## Inspecting a render closely

Viewing the whole PNG hides label-on-edge collisions. `render_template.html` can be driven directly to screenshot clipped regions at 2x: render as usual, then take the `#root svg` element's bounding box, divide its width by the `viewBox` width to get the scale, and screenshot `clip` rectangles expressed in diagram coordinates times that scale (the export adds 10px of padding on each side). Note that `exportToSvg` sizes the element by the browser's device pixel ratio while the `viewBox` stays in diagram units, so the scale must be read, not assumed.

`excalib.py` holds the shared palette and element helpers (boxes, bound text, straight and elbowed arrows, lines, and image elements for embedded icons -- see below).

## Icons

Project logos and square marks are available in `knowledge/assets/brand/`.
Use the original SVGs with `excalib.image()` and omit its `color` argument.
The [brand notes](../../docs/brand/README.md) give paths, proportions, and
embedding examples. Use these marks to identify the projects in a diagram.

`excalib.image(id_, x, y, w, h, svg_path, color=None)` embeds an SVG file as an Excalidraw `image` element: it reads the file, optionally replaces every `currentColor` in the SVG source with a hex string (so one licensed icon file can be recolored per diagram without editing the file on disk), base64-encodes it into the document's top-level `files` map, and adds an element referencing that `fileId`. `render_template.html` already passed `files` through to `exportToSvg` before this was added, so no renderer change was needed to make icons show up in the rendered PNG/SVG -- this was checked, not assumed.

Icon source files live in `tools/diagrams/icons/`, kept as unmodified originals (recoloring happens at build time, not by editing the files). `icons/LICENSES.md` records where each one came from and its license. When a diagram needs an icon that isn't already there, prefer an existing open set already used in the bundle (Health Icons, Lucide) over adding a new one, to keep icon style consistent across diagrams; add the new file, credit it in `LICENSES.md`, and note in the relevant `build_<name>.py` docstring which set was used for which slot.

## Node shape and color conventions (2026-09-30)

Node kinds share one palette across figures (see excalib): FindingClass and Diagnosis green (Diagnosis darker), Grouping pale green with dashed stroke, AssessmentScheme purple OVAL (never a diamond, which reads as a flowchart decision), AnatomicLocation blue, exam types yellow, Modality grey, DataElement light rose, Measurement light violet, Subspecialty and other metadata Concept nodes grey-violet. Arrowheads are small solid triangles (excalib.tri_head). Edge labels use the schema's committed relationship names in 13px on boxed labels.
