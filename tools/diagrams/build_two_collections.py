#!/usr/bin/env python3
"""Build the "one kind of content, two collections" figure for the Finding
Models and Common Data Elements hub page.

Finding/diagnosis definitions are one kind of content held in two collections
that differ only in how they are released. The figure says that three times
over: the two panels carry the same green as the finding/diagnosis definition
nodes in build_two_planes.py (excalib's FINDING palette, via FIND below), the
band between them reads as a beta-to-release gradient, and the amber band
underneath is the one schema both are moving onto.

  +--------------------------+  ~~~~~~~  +--------------------------+  GREEN
  | (tag) Open Imaging       |  graduate |  (tag) ACR/RSNA Common   |
  |       Finding Models     |  ------>  |        Data Elements     |
  |  inclusive . beta ...    | [gradient]|  well-reviewed . release |
  |  [hydronephrosis][renal] |  <------  |  [abdominal aortic an.]  |
  |          [pulm nodule]---+-- index --+->[pulm nodule]           |
  +--------------------------+  codes    +--------------------------+
            | moving onto                          | moving onto
  +---------------------------------------------------------------+  AMBER
  |                   the next-generation schema                   |
  |     one graph of interconnected concepts for both collections  |
  +---------------------------------------------------------------+

Constraints that drove the layout and are easy to break by nudging a number:

1. The gap between the panels is 172px and it has to hold both band labels at
   13px, so every line of them is wrapped to <= 143px ("definition keeps its
   OIFM" is the widest). Widening the panels to fit their own text on fewer
   lines narrows this gap and breaks the labels instead.
2. The gap is a five-item vertical stack -- label, arrow, gradient bar, arrow,
   label -- and the dotted index-codes link has to clear all of it. That is why
   the two "pulmonary nodule" nodes are the BOTTOM row of each panel and the
   other examples are the top row: the link then runs at y=220, below the band
   stack, and crosses nothing.
3. Those two nodes face each other across the gap -- the left one is flush to
   its panel's right padding, the right one flush to its panel's left padding --
   so the link is a short straight run rather than a line across two panels.
4. Arrowheads are drawn by excalib.tri_head(), not Excalidraw's built-ins,
   which take their size from the line's strokeWidth; HEAD sets it directly so
   the thin band arrows keep small solid heads.
5. The amber band's title is centred rather than carrying an icon in the left
   corner like the panels do: the two "moving onto" arrows come down at the
   panel centres (x=182 and x=718) and would crowd a left-aligned header.

Text widths are measured, not estimated (see tools/diagrams/README.md): every
width below is `measureText` at `<size>px Helvetica, Segoe UI Emoji` in
headless Chromium.

Icons: Lucide (ISC) tag, the same glyph build_two_planes.py and
build_three_axes.py use for a finding/diagnosis definition. See icons/LICENSES.md.

Output: knowledge/drafts/two-collections.excalidraw; render with render_excalidraw.py.
"""
from __future__ import annotations

from excalib import els, base, text, image, save, tri_head, AMBER, CAPTION

# ---------------------------------------------------------------- palette
# The finding/diagnosis definition green, straight from build_two_planes.py's
# KIND_DEF / build_foundation_network.py's FINDING: the panels ARE that node
# kind, drawn large.
FIND = {"band": "#d1fae5", "block": "#a7f3d0", "stroke": "#059669",
        "text": "#064e3b", "mid": "#047857"}
# Beta -> release, seven steps of one hue so the band reads as a single ramp.
RAMP = ["#ecfdf5", "#d1fae5", "#a7f3d0", "#6ee7b7", "#34d399", "#10b981", "#059669"]

W = 900            # canvas width
ICON = 26          # Lucide stroke art
PAD = 18           # panel inner padding
HEAD = 9.0         # filled arrowhead length (band + "moving onto" arrows)

PANEL_Y, PANEL_H = 0, 272
LW = RW = 364                      # panel width
RX = W - RW                        # right panel x  (536)
GAP_L, GAP_R = LW, RX              # 364 .. 536
GAP_C = (GAP_L + GAP_R) / 2        # 450

ROW_A_Y, ROW_B_Y, ROW_H = 144, 200, 40
AMBER_Y, AMBER_H = 320, 92

_uid = [0]


def uid(prefix: str) -> str:
    _uid[0] += 1
    return f"{prefix}{_uid[0]}"


# ---------------------------------------------------------------- helpers
def panel(id_: str, x: float, w: float, pal: dict) -> dict:
    r = base("rectangle", id_, x, PANEL_Y, w, PANEL_H, pal["stroke"], pal["band"], sw=2)
    r["roundness"] = {"type": 3}
    els.append(r)
    return r


def header(x: float, title: str, title_w: float, blocks: list[list[tuple[str, float]]],
           pal: dict) -> None:
    """Tag icon at the panel's left padding, title beside it, description lines
    aligned to the title (not to the icon). `blocks` groups those lines: the
    channel descriptors and the maintainer are separate blocks, set 7px apart,
    so a descriptor that wraps to two lines still reads as one statement rather
    than running into the maintainer line below it."""
    image(uid("hicon"), x + PAD, PANEL_Y + 16, ICON, ICON, "icons/lucide-tag.svg",
          color=pal["stroke"])
    tx = x + PAD + ICON + 10
    els.append(text(uid("ht"), tx, PANEL_Y + 18, title, size=17, color=pal["text"], w=title_w))
    y = PANEL_Y + 50
    for block in blocks:
        for s, lw in block:
            els.append(text(uid("hs"), tx, y, s, size=13, color=pal["mid"], w=lw))
            y += 13 * 1.25
        y += 7


def node(id_: str, x: float, y: float, label: str, label_w: float, pal: dict) -> dict:
    """A tiny example definition: one 13px line in a small rounded box."""
    w = label_w + 20
    r = base("rectangle", id_, x, y, w, ROW_H, pal["stroke"], pal["block"], sw=2)
    r["roundness"] = {"type": 3}
    els.append(r)
    els.append(text(id_ + "_t", x + 8, y + (ROW_H - 13 * 1.25) / 2, label, size=13,
                    color=pal["text"], align="center", w=w - 16))
    return r


def line(id_: str, pts: list[tuple[float, float]], color: str, sw=2, dashed=False,
         head: float | None = HEAD) -> None:
    """A straight or routed run, finished with a solid triangle whose size is set
    here rather than derived from strokeWidth. head=None draws no head."""
    x0, y0 = pts[0]
    end_pts = list(pts)
    if head:
        tip, frm = pts[-1], pts[-2]
        dx, dy = tip[0] - frm[0], tip[1] - frm[1]
        length = (dx ** 2 + dy ** 2) ** 0.5 or 1.0
        end_pts = list(pts[:-1]) + [(tip[0] - dx / length * head * 0.55,
                                     tip[1] - dy / length * head * 0.55)]
    ex, ey = end_pts[-1]
    ar = base("arrow", id_, x0, y0, ex - x0, ey - y0, color, "transparent",
              dashed=dashed, sw=sw)
    ar.update({"points": [[px - x0, py - y0] for px, py in end_pts],
               "startBinding": None, "endBinding": None, "startArrowhead": None,
               "endArrowhead": None, "boundElements": None})
    els.append(ar)
    if head:
        tri_head(id_ + "_h", pts[-1], pts[-2], color, size=head)


def caption(id_: str, cx: float, y_top: float, lines: list[tuple[str, float]],
            size=13, color=CAPTION) -> None:
    """A centred multi-line label, each line given its MEASURED width so the
    block centres exactly on cx."""
    w = max(lw for _, lw in lines)
    y = y_top
    for s, lw in lines:
        els.append(text(uid(id_), cx - w / 2, y, s, size=size, color=color,
                        align="center", w=w))
        y += size * 1.25


def plate(id_: str, cx: float, cy: float, s: str, w: float, size=13, color=CAPTION,
          fill="#ffffff", pad_x=6, pad_y=3) -> None:
    """An edge label on an opaque plate, centred on (cx, cy), so it masks the
    line it sits on. w is the MEASURED text width."""
    bw, bh = w + 2 * pad_x, size * 1.25 + 2 * pad_y
    r = base("rectangle", id_, cx - bw / 2, cy - bh / 2, bw, bh, "transparent", fill, sw=0)
    r["roundness"] = {"type": 3}
    els.append(r)
    els.append(text(id_ + "_t", cx - bw / 2 + pad_x, cy - bh / 2 + pad_y, s, size=size,
                    color=color, align="center", w=w))


# ================================================================ the two panels
panel("panel_oifm", 0, LW, FIND)
panel("panel_cde", RX, RW, FIND)

header(0, "Open Imaging Finding Models", 226.8,
       [[("inclusive · beta channel ·", 143.8),
         ("rapid additions and updates", 159.7)],
        [("maintained by the OIDM project", 182.8)]], FIND)
header(RX, "ACR/RSNA Common Data Elements", 277.8,
       [[("well-reviewed · release channel · stable", 228.3)],
        [("American College of Radiology ·", 186.4),
         ("Radiological Society of North America ·", 228.2),
         ("radelement.org", 87.4)]], FIND)

# Top row: the examples that live in only one collection. Bottom row: the one
# definition that lives in both, flush to the facing edges so the dotted link
# between them is a short straight run clear of the band stack above.
node("n_hydro", PAD, ROW_A_Y, "hydronephrosis", 88.9, FIND)
node("n_calc", PAD + 88.9 + 20 + 14, ROW_A_Y, "renal calculus", 79.5, FIND)
nod_l = node("n_nodule_l", LW - PAD - (103.3 + 20), ROW_B_Y, "pulmonary nodule", 103.3, FIND)
node("n_aaa", RX + PAD, ROW_A_Y, "abdominal aortic aneurysm", 156.1, FIND)
nod_r = node("n_nodule_r", RX + PAD, ROW_B_Y, "pulmonary nodule", 103.3, FIND)

# ================================================================ the band between
# Five items stacked in the 172px gap: label, arrow, gradient bar, arrow, label.
caption("bl_grad", GAP_C, 28,
        [("definitions proved out", 123.6), ("here graduate to review", 136.6)])
line("b_grad", [(GAP_L + 4, 72), (GAP_R - 4, 72)], FIND["stroke"], sw=2)

BAR_Y, BAR_H = 86, 16
BAR_X, BAR_W = GAP_L + 4, (GAP_R - 4) - (GAP_L + 4)   # the same span as the two arrows
step = BAR_W / len(RAMP)
for i, col in enumerate(RAMP):
    els.append(base("rectangle", uid("ramp"), BAR_X + i * step, BAR_Y, step + 0.5, BAR_H,
                    "transparent", col, sw=0))

line("b_cross", [(GAP_R - 4, 114), (GAP_L + 4, 114)], FIND["stroke"], sw=2)
caption("bl_cross", GAP_C, 124,
        [("cross-links: a migrated", 130.0), ("definition keeps its OIFM", 143.1),
         ("entry and carries its", 113.4), ("CDE identity", 72.2)])

# ================================================================ the shared definition
LINK_Y = ROW_B_Y + ROW_H / 2
line("l_index", [(nod_l["x"] + nod_l["width"], LINK_Y), (nod_r["x"], LINK_Y)],
     FIND["stroke"], sw=2, dashed=True, head=None)
plate("l_index_l", GAP_C, LINK_Y, "index codes", 69.4, color=FIND["mid"])

# ================================================================ the next-generation schema
amber = base("rectangle", "amber", 0, AMBER_Y, W, AMBER_H, AMBER["stroke"], AMBER["band"], sw=2)
amber["roundness"] = {"type": 3}
els.append(amber)

A_TOP = AMBER_Y + (AMBER_H - (17 * 1.25 + 6 + 13 * 1.25)) / 2
els.append(text("a_title", (W - 210.7) / 2, A_TOP, "the next-generation schema",
                size=17, color=AMBER["text"], align="center", w=210.7))
els.append(text("a_sub", (W - 329.5) / 2, A_TOP + 17 * 1.25 + 6,
                "one graph of interconnected concepts for both collections",
                size=13, color=AMBER["mid"], align="center", w=329.5))

for i, cx in enumerate((LW / 2, RX + RW / 2)):
    line(f"m_onto{i}", [(cx, PANEL_Y + PANEL_H + 2), (cx, AMBER_Y - 2)],
         AMBER["stroke"], sw=2)
    els.append(text(uid("m_l"), cx + 12, (PANEL_Y + PANEL_H + AMBER_Y) / 2 - 8,
                    "moving onto", size=13, color=AMBER["mid"], w=70.8))

save("knowledge/drafts/two-collections.excalidraw")
