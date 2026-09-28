#!/usr/bin/env python3
"""Build the "two planes" overview figure for the knowledgebase root page.

The one-picture version of the whole model: Patient Context and Foundation
Context as two tilted planes, one above the other, with every fact recorded
about this patient attached downward to the shared knowledge of what such a
thing is.

  +-----------------------------------------------------+   TEAL
  |  Patient Context -- this patient . this exam        |   (upper plane)
  |     [CT chest] <--found on-- [pulmonary nodule]     |
  +-----------------------------------------------------+
       | is a              | is a       | located at        <- thick rose
  +-----------------------------------------------------+   AMBER
  |  Foundation Context -- shared, curated knowledge    |   (lower plane)
  |   [exam type]           [definition]                |   tier 1
  |       | covers            | occurs at               |
  |   [thorax] --contains--> [lung] --contains--> [upper|   tier 2
  |                                          lobe of ...]   (the anatomy chain)
  +-----------------------------------------------------+

Geometry: both planes are the same parallelogram -- top edge offset SKEW px
to the right of the bottom edge -- so the pair reads as two isometric sheets
seen from slightly above. Because the top edge is inset, anything placed near
a plane's top must clear `left_edge(y)`, which is what `lx()` computes; every
x-coordinate below was checked against it rather than eyeballed.

Two constraints drove the layout and are easy to break by nudging a number:

1. The lower plane's header ("Foundation Context" + subtitle) occupies
   x = 68..283 at y = 314..358. The exam -> exam type cross-plane edge is the
   leftmost near-vertical line in the figure, so it has to come down at
   x >= ~305 to miss that header. That is why the lower plane's node row
   starts at x=215 rather than being centred, and why the left flank of the
   plane is filled with the grey "knowledge continues" nodes instead.
2. The three cross-plane edges must not cross each other, so their x-order
   has to be the same where they leave the upper plane and where they land:
   308 / 545 / 660 at the top, 308 / 545 / 712 at the bottom. Two of the
   three are therefore plumb (exam -> exam type, finding -> definition); the
   third leans 52px right over 349px of drop to reach the end of the anatomy
   chain, and that lean is what sets the definition node's right edge -- it
   has to pass to the RIGHT of that node, not through it.
3. The anatomy is a containment chain on its own tier, below the exam type
   and the finding definition: thorax contains lung contains upper lobe of
   right lung. The exam type covers the whole region (thorax); the finding
   definition occurs at lung; the patient's actual finding is located at the
   one lobe. Reading the picture downward and then along tier 2 is the point
   of the figure, so tier 2 is a single straight row, not a fan.

Text widths are measured, not estimated (see tools/diagrams/README.md): every
box width below is `measured width + padding` from canvas `measureText` at
`<size>px Helvetica, Segoe UI Emoji` in headless Chromium.

Icons: Health Icons (CC0/MIT, outline, filled-path art -- rendered at 32px)
for the x-ray and lungs glyphs; Lucide (ISC/MIT, stroke art -- 28px) for
layers, book-open, clipboard-list, clipboard and tag. See icons/LICENSES.md.

Output: knowledge/drafts/two-planes.excalidraw; render with render_excalidraw.py.
"""
from __future__ import annotations

from excalib import els, base, text, image, save, AMBER, TEAL, ROSE, CAPTION

# ---------------------------------------------------------------- constants
SKEW = 55          # how far each plane's top edge sits right of its bottom edge
PW = 830           # plane width, measured along an edge
ICON = 28          # Lucide (stroke art)
ICON_FILLED = 32   # Health Icons (filled-path art, optically smaller at equal size)

CROSS = ROSE["stroke"]      # deep rose: the cross-plane attachments
FAINT = "#a8a29e"           # warm grey: "the knowledge continues" edges
GREY_FILL, GREY_STROKE = "#e7e5e4", "#a8a29e"
REL = "#78716c"             # grey relationship edges inside the lower plane

P1_Y, P1_H = 0, 185         # upper plane (Patient Context)
P2_Y, P2_H = 300, 305       # lower plane (Foundation Context); gap of 115 between

_uid = [0]


def uid(prefix: str) -> str:
    _uid[0] += 1
    return f"{prefix}{_uid[0]}"


def lx(y: float, py: float, ph: float) -> float:
    """Left edge of a plane at height y -- the top edge is SKEW px further right."""
    return SKEW * (1 - (y - py) / ph)


# ---------------------------------------------------------------- helpers
def plane(id_: str, py: float, ph: float, pal: dict) -> None:
    """A tilted parallelogram: a closed Excalidraw line, filled with the band tint."""
    ln = base("line", id_, SKEW, py, PW + SKEW, ph, pal["stroke"], pal["band"], sw=2)
    ln.update({"points": [[0, 0], [PW, 0], [PW - SKEW, ph], [-SKEW, ph], [0, 0]],
               "roundness": None, "boundElements": None})
    els.append(ln)


def header(x: float, y: float, icon_path: str, pal: dict, title: str, subtitle: str,
           filled_icon=False) -> None:
    """Plane title with its icon to the left and a subtitle under it."""
    s = ICON_FILLED if filled_icon else ICON
    image(uid("hicon"), x, y + 2 - (s - ICON) / 2, s, s, icon_path, color=pal["stroke"])
    els.append(text(uid("htitle"), x + ICON + 12, y, title, size=20, color=pal["text"]))
    els.append(text(uid("hsub"), x + ICON + 12, y + 26, subtitle, size=13, color=pal["mid"]))


def node_rect(id_: str, x: float, y: float, w: float, h: float, pal: dict) -> dict:
    r = base("rectangle", id_, x, y, w, h, pal["stroke"], pal["block"], sw=2)
    r["roundness"] = {"type": 3}
    els.append(r)
    return r


def hnode(id_: str, x: float, y: float, w: float, h: float, icon_path: str, pal: dict,
          title: str, sub: str, filled_icon=False) -> dict:
    """Icon on the left, bold-ish title line, lighter second line -- the compact
    style used for the two Patient Context nodes."""
    r = node_rect(id_, x, y, w, h, pal)
    s = ICON_FILLED if filled_icon else ICON
    image(uid("ni"), x + 12 - (s - ICON) / 2, y + (h - s) / 2, s, s, icon_path, color=pal["stroke"])
    tx = x + 12 + ICON + 10
    top = y + (h - (16 * 1.25 + 2 + 13 * 1.25)) / 2
    els.append(text(uid("nt"), tx, top, title, size=16, color=pal["text"], w=w - (tx - x) - 10))
    els.append(text(uid("ns"), tx, top + 16 * 1.25 + 2, sub, size=13, color=pal["mid"],
                    w=w - (tx - x) - 10))
    return r


def vnode(id_: str, x: float, y: float, w: float, h: float, icon_path: str, pal: dict,
          title: str, desc: str, filled_icon=False) -> dict:
    """Icon centred on top, title, then a lighter descriptor -- the Foundation
    Context style, matching build_pillars.py's icon blocks."""
    r = node_rect(id_, x, y, w, h, pal)
    s = ICON_FILLED if filled_icon else ICON
    top = y + (h - (ICON + 6 + 15 * 1.25 + 2 + 13 * 1.25)) / 2
    image(uid("ni"), x + w / 2 - s / 2, top - (s - ICON) / 2, s, s, icon_path, color=pal["stroke"])
    ty = top + ICON + 6
    els.append(text(uid("nt"), x + 8, ty, title, size=15, color=pal["text"], align="center", w=w - 16))
    els.append(text(uid("nd"), x + 8, ty + 15 * 1.25 + 2, desc, size=13, color=pal["mid"],
                    align="center", w=w - 16))
    return r


def chip(id_: str, x: float, y: float, w: float, h: float, pal: dict, title: str,
         title_w: float, desc: str | None = None, icon_path: str | None = None,
         filled_icon=False) -> dict:
    """A compact node for the anatomy chain: content vertically centred, and
    horizontally either centred text (no icon) or an icon+title group centred
    as a unit. title_w is the MEASURED title width, needed to centre that
    group. Shorter than vnode() so the chain reads as one row of locations
    rather than three more blocks."""
    r = node_rect(id_, x, y, w, h, pal)
    lines_h = 15 * 1.25 + (2 + 13 * 1.25 if desc else 0)
    ty = y + (h - lines_h) / 2
    if icon_path:
        s_ = ICON_FILLED if filled_icon else ICON
        gx = x + (w - (s_ + 10 + title_w)) / 2
        image(uid("ni"), gx, y + (h - s_) / 2, s_, s_, icon_path, color=pal["stroke"])
        els.append(text(uid("nt"), gx + s_ + 10, ty, title, size=15, color=pal["text"], w=title_w))
    else:
        els.append(text(uid("nt"), x + 8, ty, title, size=15, color=pal["text"],
                        align="center", w=w - 16))
    if desc:
        els.append(text(uid("nd"), x + 8, ty + 15 * 1.25 + 2, desc, size=13, color=pal["mid"],
                        align="center", w=w - 16))
    return r


def dot(id_: str, cx: float, cy: float, r: float) -> None:
    e = base("ellipse", id_, cx - r, cy - r, 2 * r, 2 * r, GREY_STROKE, GREY_FILL, sw=1)
    e["opacity"] = 70
    els.append(e)


def faint(x1: float, y1: float, x2: float, y2: float) -> None:
    ln = base("line", uid("f"), x1, y1, x2 - x1, y2 - y1, FAINT, "transparent", sw=1)
    ln.update({"points": [[0, 0], [x2 - x1, y2 - y1]], "boundElements": None, "opacity": 60})
    els.append(ln)


def path(id_: str, pts: list[tuple[float, float]], color: str, sw=3, head="arrow") -> None:
    """Multi-point routed arrow; excalib.arrow()'s elbow modes only do 3 points."""
    x0, y0 = pts[0]
    ar = base("arrow", id_, x0, y0, pts[-1][0] - x0, pts[-1][1] - y0, color, "transparent", sw=sw)
    ar.update({"points": [[px - x0, py - y0] for px, py in pts], "startBinding": None,
               "endBinding": None, "startArrowhead": None, "endArrowhead": head,
               "boundElements": None})
    els.append(ar)


def plate(id_: str, cx: float, cy: float, s: str, w: float, size=13, color=CAPTION,
          fill="#ffffff", pad_x=6, pad_y=3) -> None:
    """An edge label on an opaque plate, centred on (cx, cy), so it masks the
    line it sits on. w is the MEASURED text width. fill is the tint the label
    lands on -- a white patch inside a tinted plane is visible, so pass the
    plane's band colour for labels drawn inside a plane."""
    bw, bh = w + 2 * pad_x, size * 1.25 + 2 * pad_y
    r = base("rectangle", id_, cx - bw / 2, cy - bh / 2, bw, bh, "transparent", fill, sw=0)
    r["roundness"] = {"type": 3}
    els.append(r)
    els.append(text(id_ + "_t", cx - bw / 2 + pad_x, cy - bh / 2 + pad_y, s, size=size,
                    color=color, align="center", w=w))


# ================================================================ planes
plane("plane_patient", P1_Y, P1_H, TEAL)
plane("plane_foundation", P2_Y, P2_H, AMBER)

header(67, P1_Y + 12, "icons/lucide-layers.svg", TEAL,
       "Patient Context", "this patient \u00b7 this exam")
header(68, P2_Y + 14, "icons/lucide-book-open.svg", AMBER,
       "Foundation Context", "shared, curated knowledge")

# ================================================================ upper plane: two nodes
# "CT chest" 64.0 / "this patient . 2026-03-04" 140.9 at 16/13px -> 141 + icon
# 28 + pads = 203; 210 used. Placed so that x=308 -- the leftmost column that
# clears the lower plane's header -- falls inside it, making that drop plumb
# (see module docstring, constraint 1).
exam = hnode("exam", 170, 76, 210, 66, "icons/lucide-clipboard-list.svg", TEAL,
             "CT chest", "this patient \u00b7 2026-03-04")
# "pulmonary nodule" 127.2 / "present . 8 mm . new" 122.8 -> 127 + 28 + pads = 189; 196 used.
# x=500 is chosen so that x=545 (the definition node's centre) falls inside it,
# making that cross-plane edge exactly plumb, while leaving the node's right end
# far enough right that the "located at" edge reaches the chain's far node
# without leaning far.
finding = hnode("finding", 500, 100, 196, 66, "icons/lucide-clipboard.svg", TEAL,
                "pulmonary nodule", "present \u00b7 8 mm \u00b7 new")

path("e_found_on", [(500, 133), (386, 111)], TEAL["stroke"], sw=2)
plate("l_found_on", 460, 100, "found on", 50.6, color=TEAL["mid"], fill=TEAL["band"])

# ================================================================ lower plane, tier 1: exam type + definition
# Both boxes are 190 wide: the widest line in each measures 157.5 and 152.5px,
# so 190 (= ~157 + 2 x 16) fits either with room to spare.
ROW_Y, ROW_H, NW = 372, 97, 190
X_EXAM_T, X_DEF = 215, 450
exam_type = vnode("exam_type", X_EXAM_T, ROW_Y, NW, ROW_H, "icons/healthicons-xray.svg", AMBER,
                  "CT Chest W contrast IV", "exam type", filled_icon=True)
definition = vnode("definition", X_DEF, ROW_Y, NW, ROW_H, "icons/lucide-tag.svg", AMBER,
                   "pulmonary nodule", "finding/diagnosis definition")

# ================================================================ lower plane, tier 2: the anatomy chain
# thorax -> lung -> upper lobe of right lung, one straight row, 82px gaps --
# just wide enough for a "contains" plate (48.4 + 12 = 60.4) with ~11px of
# line showing either side of it. Only "lung" carries the lungs glyph: three
# copies of it would read as three different organs rather than one chain.
CH_Y, CH_H = 515, 62
thorax = chip("thorax", 215, CH_Y, 130, CH_H, AMBER, "thorax", 41.7, desc="anatomic location")
lung = chip("lung", 427, CH_Y, 110, CH_H, AMBER, "lung", 28.4,
            icon_path="icons/healthicons-lungs.svg", filled_icon=True)
upper_lobe = chip("upper_lobe", 619, CH_Y, 185, CH_H, AMBER, "upper lobe of right lung", 153.4)

CH_MID = CH_Y + CH_H / 2
path("r_contains1", [(345, CH_MID), (427, CH_MID)], REL, sw=2)
plate("l_contains1", 386, CH_MID, "contains", 48.4, color=REL, fill=AMBER["band"])
path("r_contains2", [(537, CH_MID), (619, CH_MID)], REL, sw=2)
plate("l_contains2", 578, CH_MID, "contains", 48.4, color=REL, fill=AMBER["band"])

# Tier 1 -> tier 2, in the 46px band between the rows. Both labels sit beside
# their edge rather than on it: the drops are too short to mask.
path("r_covers", [(280, ROW_Y + ROW_H), (280, CH_Y - 3)], REL, sw=2)
plate("l_covers", 320, 492, "covers", 38.3, color=REL, fill=AMBER["band"])
path("r_occurs", [(500, ROW_Y + ROW_H), (482, CH_Y - 3)], REL, sw=2)
plate("l_occurs", 540, 492, "occurs at", 52.7, color=REL, fill=AMBER["band"])

# The knowledge continues: unlabelled nodes on the plane's left flank (kept
# free by pushing tier 1 right, see constraint 1) and in the right flank that
# the definition node leaves open. The right pair's faint edge joins the chain
# to the RIGHT of x=712 so it never crosses the "located at" drop.
for gid, gx, gy, gr in [("g1", 105, 395, 13), ("g2", 66, 437, 10), ("g3", 128, 447, 11),
                        ("g4", 170, 512, 9), ("g5", 806, 455, 12), ("g6", 838, 417, 8)]:
    dot(gid, gx, gy, gr)
faint(105, 395, 66, 437)
faint(105, 395, 128, 447)
faint(128, 447, 170, 512)
faint(118, 398, X_EXAM_T, 410)
faint(838, 417, 806, 455)
faint(798, 466, 778, CH_Y)

# ================================================================ cross-plane attachments
# Three thick rose near-verticals; see constraint 2 for why two are plumb and
# the third leans. None passes through a node or the lower plane's header.
path("x_exam", [(308, 142), (308, ROW_Y - 3)], CROSS, sw=3)
plate("x_exam_l", 308, 240, "is a", 20.2, color=ROSE["text"])
path("x_isa", [(545, 166), (545, ROW_Y - 3)], CROSS, sw=3)
plate("x_isa_l", 545, 240, "is a", 20.2, color=ROSE["text"])
path("x_located", [(660, 166), (711, CH_Y - 4)], CROSS, sw=3)
plate("x_located_l", 671, 240, "located at", 56.4, color=ROSE["text"])

# ================================================================ caption
els.append(text("caption", 0, P2_Y + P2_H + 26,
                "every fact about this patient is attached to the shared knowledge "
                "of what such a thing is",
                size=14, color=CAPTION, align="center", w=PW + SKEW))

save("knowledge/drafts/two-planes.excalidraw")
