#!/usr/bin/env python3
"""Build the OIDM "three axes of Foundation Context" detail diagram.

A smaller companion to build_pillars.py, zoomed into the Foundation
Context (AMBER) pillar of that stack: the three axes shared knowledge is
organized along -- finding/diagnosis, anatomic location, exam type -- each
a curated layer over an existing external standard. Same AMBER palette and
same icon files as the main stack diagram (from excalib.py / icons/), so
the two figures read as one family.

Landscape, three columns:
  - icon, title, a short "WHAT/WHERE/HOW" tagline
  - a small darker block at the bottom of each column: "layered over: <the
    external standard(s) this axis anchors to>"
  - two double-headed "relationships" connectors between the columns
  - one caption underneath summarizing the pattern

Output: knowledge/drafts/three-axes.excalidraw; render with render_excalidraw.py.
"""
from excalib import els, base, text, image, arrow, boxed_label, save, AMBER, CAPTION

CONTENT_W = 860
ICON = 36
_uid = [0]


def uid(prefix: str) -> str:
    _uid[0] += 1
    return f"{prefix}{_uid[0]}"


def axis_column(id_: str, x: float, y: float, w: float, h: float, icon_path: str,
                 title_lines: list[str], max_title_lines: int, tagline: str,
                 desc_lines: list[str], block_h: float) -> None:
    r = base("rectangle", id_, x, y, w, h, AMBER["stroke"], AMBER["block"], sw=2)
    r["roundness"] = {"type": 3}
    els.append(r)

    cx = x + w / 2
    top = y + 44
    image(uid("coli"), cx - ICON / 2, top, ICON, ICON, icon_path, color=AMBER["stroke"])

    ty = top + ICON + 10
    for ln in title_lines:
        els.append(text(uid("colt"), x + 8, ty, ln, size=17, color=AMBER["text"], align="center", w=w - 16))
        ty += 17 * 1.25
    # tagline sits at a height fixed by the row's max title-line count, not
    # this column's own count, so every column's tagline lines up even when
    # one title wraps to more lines than another.
    tag_y = top + ICON + 10 + max_title_lines * 17 * 1.25 + 10
    els.append(text(uid("coltag"), x + 8, tag_y, tagline, size=14, color=AMBER["mid"], align="center", w=w - 16))

    # small darker block, bottom-anchored, uniform height across the row
    block_w = w - 24
    block_x = x + 12
    block_y = y + h - 38 - block_h
    rb = base("rectangle", uid("colblk"), block_x, block_y, block_w, block_h, AMBER["text"], AMBER["stroke"], sw=1)
    rb["roundness"] = {"type": 3}
    els.append(rb)
    by = block_y + (block_h - len(desc_lines) * 13 * 1.25) / 2 + 2
    for ln in desc_lines:
        els.append(text(uid("colblkt"), block_x + 6, by, ln, size=13, color="#fef3c7", align="center", w=block_w - 12))
        by += 13 * 1.25


# ---------------------------------------------------------------- layout
GAP_COL = 56
COL_W = (CONTENT_W - 2 * GAP_COL) / 3
MAX_TITLE_LINES = 2
BLOCK_H = 8 + 2 * 13 * 1.25 + 8  # tallest "layered over" block is 2 lines

COL_H = (44 + ICON + 10 + MAX_TITLE_LINES * 17 * 1.25 + 10 + 14 * 1.25 + 34 + BLOCK_H + 38)

Y0 = 66
specs = [
    ("axis1", 0, "icons/lucide-tag.svg", ["Finding/diagnosis", "definitions"], "WHAT was found",
     ["layered over: finding models", "· ACR/RSNA CDEs"]),
    ("axis2", COL_W + GAP_COL, "icons/healthicons-lungs.svg", ["Anatomic locations"], "WHERE it is",
     ["layered over: RadLex"]),
    ("axis3", 2 * (COL_W + GAP_COL), "icons/healthicons-xray.svg", ["Exam types"], "HOW it was seen",
     ["layered over: LOINC/RSNA", "Playbook"]),
]
for cid, xpos, ipath, title_lines, tagline, desc_lines in specs:
    axis_column(cid, xpos, Y0, COL_W, COL_H, ipath, title_lines, MAX_TITLE_LINES, tagline, desc_lines, BLOCK_H)

# two double-headed "relationships" connectors between the columns -- short
# (8px clearance from each panel edge, not touching them), with the label
# on its own white box centered above the arrow (6px clearance) so it never
# sits on top of the arrowheads.
arrow_y = Y0 + COL_H / 2
gap1_l, gap1_r = COL_W, COL_W + GAP_COL
gap2_l, gap2_r = 2 * COL_W + GAP_COL, 2 * (COL_W + GAP_COL)

arrow(uid("rel"), "axis1", "right", "axis2", "left", color=AMBER["stroke"], both=True, sw=1.5, inset=8)
boxed_label(uid("rellbl"), (gap1_l + gap1_r) / 2, arrow_y - 6, "relationships", size=13, color=CAPTION)

arrow(uid("rel"), "axis2", "right", "axis3", "left", color=AMBER["stroke"], both=True, sw=1.5, inset=8)
boxed_label(uid("rellbl"), (gap2_l + gap2_r) / 2, arrow_y - 6, "relationships", size=13, color=CAPTION)

# caption underneath all three columns
CAP_Y = Y0 + COL_H + 56
els.append(text(uid("cap"), 0, CAP_Y,
                 "each a curated layer over an existing standard; the axes relate to each other and cite external references",
                 size=13, color=CAPTION, align="center", w=CONTENT_W))

save("knowledge/drafts/three-axes.excalidraw")
