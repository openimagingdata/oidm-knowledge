#!/usr/bin/env python3
"""Build the "two planes" overview figure for the knowledgebase root page.

The one-picture version of the whole model: Patient Context and Foundation
Context as two tilted planes, one above the other, with every fact recorded
about this patient attached downward to the shared knowledge of what such a
thing is.

  +---------------------------------------------------------------+  TEAL
  |  Patient Context     ,-------- found on --------------.       |
  |   [CT chest WO] <-found on- [pulmonary nodule]  [pleural eff] |
  +---------------------------------------------------------------+
     | is a      | is a    | located at   | is a     | located at    <- rose
  +---------------------------------------------------------------+  AMBER
  |  Foundation Context                                           |
  |  [CT Chest WO contrast]  [pulm nodule def]  [pleural eff def] |  tier 1
  |     |member of family    |seen on |occurs at      |occurs at  |
  |  [CT Chest] -modality-> [CT]      |               |           |  tier 2
  |     |covers                       |               |           |
  |  [thorax] -contains-> [lung] -> [upper lobe]  [pleural space] |  tier 3
  |     `------------------ contains ------------------^          |
  +---------------------------------------------------------------+

Geometry: both planes are the same parallelogram -- top edge offset SKEW px
to the right of the bottom edge -- so the pair reads as two isometric sheets
seen from slightly above. Because the top edge is inset, anything placed near
a plane's top must clear `left_edge(y)`, which is what `lx()` computes; every
x-coordinate below was checked against it rather than eyeballed.

Constraints that drove the layout and are easy to break by nudging a number:

1. The lower plane's header ("Foundation Context" + subtitle) occupies
   x = 68..283 at y = 264..308, so the leftmost cross-plane edge has to come
   down at x >= ~300 to miss it. Tier 1 therefore starts at x=120 and the
   plane's left flank carries the grey "knowledge continues" nodes instead.
2. Five cross-plane edges, and none may cross another, so their x-order is the
   same where they leave the upper plane (300 / 490 / 602 / 720 / 866) and
   where they land (300 / 490 / 602 / 720 / 856). Four are plumb; the fifth
   leans 10px to clear the effusion definition's right edge. Two of them run
   past tier 1 into tier 3 and thread the gaps between tier 1's boxes -- x=602
   uses the 32px gap between the two definitions -- so those boxes cannot be
   moved together, and neither definition can be widened.
3. With two findings in the upper plane, the second is too far right for a
   straight "found on" edge back to the exam. Its edge runs ABOVE the row, in
   the lane at y=72: every cross-plane edge leaves a node's BOTTOM, so the
   band between the header and the row is the one place nothing crosses.
4. The foundation plane is three tiers and the vertical axis is generality:
   what the patient's data attaches to sits in tier 1, and each tier below is
   the more general thing. The exam axis (Playbook entry -> family -> modality)
   and the anatomy axis (upper lobe <- lung <- thorax) both read that way,
   which is why the family, not the specific entry, covers the thorax.
5. The pleural space is the thorax's second anatomic branch, but it sits at the
   far right, under the effusion's definition. Its "contains" edge is drawn as
   a lane BELOW tier 3 rather than a long horizontal through it, which would
   have to cross both lung and the upper lobe.
6. Arrowheads are drawn by excalib.tri_head(), not by Excalidraw's built-in
   ones: the built-ins take their size from the line's strokeWidth, which
   forces a thick rose edge to carry an outsized head. HEAD_R and HEAD_G set
   the two sizes directly.

Text widths are measured, not estimated (see tools/diagrams/README.md): every
box width below is `measured width + padding` from canvas `measureText` at
`<size>px Helvetica, Segoe UI Emoji` in headless Chromium.

Icons: Health Icons (CC0/MIT, outline, filled-path art -- rendered at 32px)
for the x-ray and lungs glyphs; Lucide (ISC/MIT, stroke art -- 28px) for
layers, book-open, clipboard-list, clipboard and tag. See icons/LICENSES.md.

Output: knowledge/drafts/two-planes.excalidraw; render with render_excalidraw.py.
"""
from __future__ import annotations

from excalib import (els, base, text, image, save, tri_head,
                     AMBER, TEAL, ROSE, CAPTION)

# ---------------------------------------------------------------- constants
SKEW = 55          # how far each plane's top edge sits right of its bottom edge
PW = 880           # plane width, measured along an edge
ICON = 28          # Lucide (stroke art)
ICON_FILLED = 32   # Health Icons (filled-path art, optically smaller at equal size)

CROSS = ROSE["stroke"]      # deep rose: the cross-plane attachments
FAINT = "#a8a29e"           # warm grey: "the knowledge continues" edges
GREY_FILL, GREY_STROKE = "#e7e5e4", "#a8a29e"
REL = "#78716c"             # grey relationship edges inside the lower plane

# Node kinds inside the Foundation Context plane. Fills and strokes are taken
# straight from build_foundation_network.py's FINDING / ANATOMY / EXAM / GREY
# so the two figures name the same kinds with the same colours. Each dict keeps
# excalib's band/block/stroke/text/mid shape; only "band" (the plane tint) is
# shared, since every one of these sits on the amber plane. The modality grey
# uses a darker stroke than the mini-network's #9ca3af, which is too faint to
# hold an edge against the amber ground.
KIND_DEF = {"band": AMBER["band"], "block": "#d1fae5", "stroke": "#059669",
            "text": "#064e3b", "mid": "#047857"}      # finding/diagnosis definition
KIND_ANAT = {"band": AMBER["band"], "block": "#bfdbfe", "stroke": "#1d4ed8",
             "text": "#1e3a8a", "mid": "#1d4ed8"}     # anatomic location
KIND_EXAM = AMBER                                      # exam type (already the amber block)
KIND_MOD = {"band": AMBER["band"], "block": "#e5e7eb", "stroke": "#6b7280",
            "text": "#374151", "mid": "#4b5563"}      # modality

P1_Y, P1_H = 0, 190         # upper plane (Patient Context)
P2_Y, P2_H = 250, 440       # lower plane (Foundation Context); 60px gap between
HEAD_R, HEAD_G = 13.0, 10.0  # filled arrowhead length: rose edges, grey/teal edges

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
    """Icon on the left at a fixed inset, title line, lighter second line --
    the style used for the two Patient Context nodes."""
    r = node_rect(id_, x, y, w, h, pal)
    s = ICON_FILLED if filled_icon else ICON
    image(uid("ni"), x + 12 - (s - ICON) / 2, y + (h - s) / 2, s, s, icon_path, color=pal["stroke"])
    tx = x + 12 + ICON + 10
    top = y + (h - (16 * 1.25 + 2 + 13 * 1.25)) / 2
    els.append(text(uid("nt"), tx, top, title, size=16, color=pal["text"], w=w - (tx - x) - 10))
    els.append(text(uid("ns"), tx, top + 16 * 1.25 + 2, sub, size=13, color=pal["mid"],
                    w=w - (tx - x) - 10))
    return r


def chip(id_: str, x: float, y: float, w: float, h: float, pal: dict, title: str,
         desc: str | None = None, icon_path: str | None = None, filled_icon=False,
         text_w: float | None = None) -> dict:
    """The Foundation Context node: content vertically centred, and horizontally
    either centred text (no icon) or an icon + text-column group centred as a
    unit. text_w is the MEASURED width of the widest of title/desc, needed to
    centre that group; with no icon it is not used. Every foundation node is
    the same height, so the three tiers read as three rows of one grid."""
    r = node_rect(id_, x, y, w, h, pal)
    lines_h = 15 * 1.25 + (2 + 13 * 1.25 if desc else 0)
    ty = y + (h - lines_h) / 2
    if icon_path:
        s_ = ICON_FILLED if filled_icon else ICON
        gx = x + (w - (s_ + 10 + text_w)) / 2
        image(uid("ni"), gx, y + (h - s_) / 2, s_, s_, icon_path, color=pal["stroke"])
        els.append(text(uid("nt"), gx + s_ + 10, ty, title, size=15, color=pal["text"], w=text_w))
        if desc:
            els.append(text(uid("nd"), gx + s_ + 10, ty + 15 * 1.25 + 2, desc, size=13,
                            color=pal["mid"], w=text_w))
    else:
        els.append(text(uid("nt"), x + 8, ty, title, size=15, color=pal["text"],
                        align="center", w=w - 16))
        if desc:
            els.append(text(uid("nd"), x + 8, ty + 15 * 1.25 + 2, desc, size=13,
                            color=pal["mid"], align="center", w=w - 16))
    return r


def dot(id_: str, cx: float, cy: float, r: float) -> None:
    e = base("ellipse", id_, cx - r, cy - r, 2 * r, 2 * r, GREY_STROKE, GREY_FILL, sw=1)
    e["opacity"] = 70
    els.append(e)


def faint(x1: float, y1: float, x2: float, y2: float) -> None:
    ln = base("line", uid("f"), x1, y1, x2 - x1, y2 - y1, FAINT, "transparent", sw=1)
    ln.update({"points": [[0, 0], [x2 - x1, y2 - y1]], "boundElements": None, "opacity": 60})
    els.append(ln)


def path(id_: str, pts: list[tuple[float, float]], color: str, sw=3, head=HEAD_G) -> None:
    """Multi-point routed arrow (excalib.arrow()'s elbow modes only do 3 points),
    finished with excalib.tri_head(): a solid filled triangle whose size is set
    here rather than derived from the line's strokeWidth, so a thick rose edge
    and a thin grey one can carry heads of deliberately chosen sizes."""
    x0, y0 = pts[0]
    tip, frm = pts[-1], pts[-2]
    dx, dy = tip[0] - frm[0], tip[1] - frm[1]
    length = (dx ** 2 + dy ** 2) ** 0.5 or 1.0
    # stop the line a little short so the head's base sits on it, not past it
    end = (tip[0] - dx / length * head * 0.55, tip[1] - dy / length * head * 0.55)
    line_pts = list(pts[:-1]) + [end]
    ar = base("arrow", id_, x0, y0, end[0] - x0, end[1] - y0, color, "transparent", sw=sw)
    ar.update({"points": [[px - x0, py - y0] for px, py in line_pts], "startBinding": None,
               "endBinding": None, "startArrowhead": None, "endArrowhead": None,
               "boundElements": None})
    els.append(ar)
    tri_head(id_ + "_h", tip, frm, color, size=head)


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
       "Patient Context", "this patient · this exam")
header(68, P2_Y + 14, "icons/lucide-book-open.svg", AMBER,
       "Foundation Context", "shared, curated knowledge")

# ================================================================ upper plane: one exam, two findings
# All three sit on one row, so each finding's "found on" edge is short and
# neither crosses the cross-plane drops that leave the row's underside. The
# second finding is too far right for a straight edge back to the exam, so its
# edge runs ABOVE the row, in the lane at y=72 between the header and the nodes
# -- every cross-plane drop leaves a node's BOTTOM, so nothing is up there to
# cross.
ROW1_Y, ROW1_H = 92, 66
exam = hnode("exam", 140, ROW1_Y, 246, ROW1_H, "icons/lucide-clipboard-list.svg", TEAL,
             "CT chest without contrast", "this patient \u00b7 2026-03-04")
nodule = hnode("nodule", 470, ROW1_Y, 196, ROW1_H, "icons/lucide-clipboard.svg", TEAL,
               "pulmonary nodule", "present \u00b7 8 mm \u00b7 new")
effusion = hnode("effusion", 706, ROW1_Y, 176, ROW1_H, "icons/lucide-clipboard.svg", TEAL,
                 "pleural effusion", "absent")
ROW1_B = ROW1_Y + ROW1_H

path("e_found1", [(470, 125), (392, 125)], TEAL["stroke"], sw=2)
plate("l_found1", 431, 125, "found on", 50.6, color=TEAL["mid"], fill=TEAL["band"])
path("e_found2", [(790, ROW1_Y), (790, 72), (250, 72), (250, ROW1_Y - 3)], TEAL["stroke"], sw=2)
plate("l_found2", 560, 72, "found on", 50.6, color=TEAL["mid"], fill=TEAL["band"])

# ================================================================ lower plane, tier 1
# What the patient's own data attaches to: the specific Playbook exam type and
# one definition per finding. Widest lines measure 150.9 / 152.5 / 152.5px;
# with the 32/28px icon, its 10px gutter and 24px of padding that gives 218/216.
T1_Y, T1_H = 322, 62
exam_type = chip("exam_type", 120, T1_Y, 218, T1_H, KIND_EXAM, "CT Chest WO contrast",
                 desc="exam type \u00b7 29252-4", icon_path="icons/healthicons-xray.svg",
                 filled_icon=True, text_w=150.9)
nodule_def = chip("nodule_def", 370, T1_Y, 216, T1_H, KIND_DEF, "pulmonary nodule",
                  desc="finding/diagnosis definition", icon_path="icons/lucide-tag.svg",
                  text_w=152.5)
effusion_def = chip("effusion_def", 618, T1_Y, 216, T1_H, KIND_DEF, "pleural effusion",
                    desc="finding/diagnosis definition", icon_path="icons/lucide-tag.svg",
                    text_w=152.5)
T1_B = T1_Y + T1_H

# ================================================================ lower plane, tier 2
T2_Y, T2_H = 448, 56
family = chip("family", 130, T2_Y, 168, T2_H, KIND_EXAM, "CT Chest", desc="exam family \u00b7 preferred")
modality = chip("modality", 382, T2_Y, 80, T2_H, KIND_MOD, "CT", desc="modality")
T2_B = T2_Y + T2_H
T2_MID = T2_Y + T2_H / 2

path("r_member", [(200, T1_B), (200, T2_Y - 3)], REL, sw=2)
plate("l_member", 200, T1_B + 32, "member of family", 99.7, color=REL, fill=AMBER["band"])
path("r_modality", [(298, T2_MID), (379, T2_MID)], REL, sw=2)
plate("l_modality", 340, T2_MID, "modality", 48.4, color=REL, fill=AMBER["band"])
# "CT" is a hub: the family reaches it along tier 2, the nodule definition
# straight down from tier 1.
path("r_seen", [(422, T1_B), (422, T2_Y - 3)], REL, sw=2)
plate("l_seen", 422, T1_B + 32, "seen on", 46.3, color=REL, fill=AMBER["band"])

# ================================================================ lower plane, tier 3: anatomy
# thorax contains lung contains upper lobe; thorax also contains the pleural
# space, which sits at the far right under the effusion's definition. That
# second branch is drawn as a lane BELOW the tier rather than a long horizontal
# through it, which would have to cross lung and upper lobe.
T3_Y, T3_H = 568, 62
thorax = chip("thorax", 130, T3_Y, 130, T3_H, KIND_ANAT, "thorax", desc="anatomic location")
lung = chip("lung", 342, T3_Y, 110, T3_H, KIND_ANAT, "lung",
            icon_path="icons/healthicons-lungs.svg", filled_icon=True, text_w=28.4)
upper_lobe = chip("upper_lobe", 554, T3_Y, 185, T3_H, KIND_ANAT, "upper lobe of right lung")
pleural_space = chip("pleural_space", 760, T3_Y, 120, T3_H, KIND_ANAT, "pleural space")
T3_B = T3_Y + T3_H
T3_MID = T3_Y + T3_H / 2

path("r_contains1", [(260, T3_MID), (339, T3_MID)], REL, sw=2)
plate("l_contains1", 301, T3_MID, "contains", 48.4, color=REL, fill=AMBER["band"])
path("r_contains2", [(452, T3_MID), (551, T3_MID)], REL, sw=2)
plate("l_contains2", 503, T3_MID, "contains", 48.4, color=REL, fill=AMBER["band"])
LANE_Y = T3_B + 26
path("r_contains3", [(215, T3_B), (215, LANE_Y), (820, LANE_Y), (820, T3_B + 3)], REL, sw=2)
plate("l_contains3", 500, LANE_Y, "contains", 48.4, color=REL, fill=AMBER["band"])

# The family covers the whole region; each definition occurs at its own
# structure. "occurs at" for the nodule elbows around the modality node rather
# than cutting the corner off it.
path("r_covers", [(200, T2_B), (200, T3_Y - 3)], REL, sw=2)
plate("l_covers", 200, T2_B + 32, "covers", 38.3, color=REL, fill=AMBER["band"])
path("r_occurs1", [(560, T1_B), (560, 550), (440, 550), (440, T3_Y - 3)], REL, sw=2)
plate("l_occurs1", 552, T1_B + 32, "occurs at", 52.7, color=REL, fill=AMBER["band"])
path("r_occurs2", [(790, T1_B), (790, T3_Y - 3)], REL, sw=2)
plate("l_occurs2", 790, T1_B + 32, "occurs at", 52.7, color=REL, fill=AMBER["band"])

# ================================================================ the knowledge continues
# The left cluster sits BELOW tier 1, where the plane's slanted left edge has
# moved far enough left to give a dot clearance; higher up it would straddle
# the border.
for gid, gx, gy, gr in [("g1", 96, 412, 11), ("g2", 62, 448, 9), ("g3", 92, 486, 10),
                        ("g4", 60, 528, 8), ("g5", 676, 452, 12), ("g6", 712, 492, 9)]:
    dot(gid, gx, gy, gr)
faint(96, 412, 62, 448)
faint(96, 412, 92, 486)
faint(92, 486, 60, 528)
faint(104, 404, 124, 388)
faint(66, 535, 130, 590)
faint(676, 452, 712, 492)
faint(676, 440, 676, T1_B)

# ================================================================ cross-plane attachments
# Five thick rose edges. Their x-order is the same where they leave the upper
# plane (300 / 490 / 602 / 720 / 866) and where they land (300 / 490 / 602 /
# 720 / 856), so none crosses another. Four are plumb; the fifth leans 10px to
# clear the effusion definition's right edge. The two that reach tier 3 thread
# the gaps between tier 1's boxes: x=602 runs down the 32px gap between the two
# definitions, which is why those two boxes cannot be moved together.
CX_LABEL_Y = 212
path("x_exam", [(300, ROW1_B), (300, T1_Y - 3)], CROSS, sw=3, head=HEAD_R)
plate("x_exam_l", 300, CX_LABEL_Y, "is a", 20.2, color=ROSE["text"])
path("x_nodule_isa", [(490, ROW1_B), (490, T1_Y - 3)], CROSS, sw=3, head=HEAD_R)
plate("x_nodule_isa_l", 490, CX_LABEL_Y, "is a", 20.2, color=ROSE["text"])
path("x_nodule_loc", [(602, ROW1_B), (602, T3_Y - 3)], CROSS, sw=3, head=HEAD_R)
plate("x_nodule_loc_l", 602, CX_LABEL_Y, "located at", 56.4, color=ROSE["text"])
path("x_effusion_isa", [(720, ROW1_B), (720, T1_Y - 3)], CROSS, sw=3, head=HEAD_R)
plate("x_effusion_isa_l", 720, CX_LABEL_Y, "is a", 20.2, color=ROSE["text"])
path("x_effusion_loc", [(866, ROW1_B), (856, T3_Y - 3)], CROSS, sw=3, head=HEAD_R)
plate("x_effusion_loc_l", 864, CX_LABEL_Y, "located at", 56.4, color=ROSE["text"])

# ================================================================ legend
# One line of swatches under the plane, naming the four node kinds the fills
# stand for. Measured label widths, so the row centres exactly on the canvas.
LEG_ITEMS = [(KIND_DEF, "finding/diagnosis definition", 152.5),
             (KIND_ANAT, "anatomic location", 101.2),
             (KIND_EXAM, "exam type", 60.0),
             (KIND_MOD, "modality", 48.4)]
SW_W, SW_H, SW_GAP, ITEM_GAP = 18, 13, 8, 28
leg_w = sum(SW_W + SW_GAP + w for _, _, w in LEG_ITEMS) + ITEM_GAP * (len(LEG_ITEMS) - 1)
leg_x = (PW + SKEW - leg_w) / 2
LEG_Y = P2_Y + P2_H + 22
for _pal, _label, _w in LEG_ITEMS:
    _r = base("rectangle", uid("leg"), leg_x, LEG_Y + 1.6, SW_W, SW_H,
              _pal["stroke"], _pal["block"], sw=1)
    _r["roundness"] = {"type": 3}
    els.append(_r)
    els.append(text(uid("legt"), leg_x + SW_W + SW_GAP, LEG_Y, _label, size=13, color=CAPTION, w=_w))
    leg_x += SW_W + SW_GAP + _w + ITEM_GAP

# ================================================================ caption
els.append(text("caption", 0, P2_Y + P2_H + 54,
                "every fact about this patient is attached to the shared knowledge "
                "of what such a thing is",
                size=14, color=CAPTION, align="center", w=PW + SKEW))

save("knowledge/drafts/two-planes.excalidraw")
