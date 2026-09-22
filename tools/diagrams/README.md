# Diagrams

Diagrams in the bundle are Excalidraw files rendered to SVG and placed beside the document that embeds them (`knowledge/<dir>/<name>.excalidraw` and `<name>.svg`). Mermaid is not used.

## Source-of-truth rule

Per diagram, one of two things is the source:

- **Builder-generated.** `build_<name>.py` in this directory writes the `.excalidraw` file. Edit the builder, not the file. Iterate by rendering and looking at the PNG.
- **Hand-edited.** Once anyone edits a `.excalidraw` file directly (in Excalidraw or as JSON), that file becomes the source. Retire its builder in the same change: delete `build_<name>.py` and add the diagram to the list below.

Hand-edited diagrams (builders retired): none yet.

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

`excalib.py` holds the shared palette and element helpers (boxes, bound text, straight and elbowed arrows, lines).
