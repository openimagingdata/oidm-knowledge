#!/usr/bin/env python3
"""Build the Foundation Context "mini-network" diagram (v6 layout).

A small illustrative graph -- not exhaustive -- showing the three sectors of
Foundation Context (finding/diagnosis definitions, anatomic locations, exam
types) and a sample of the relationships within and across them, drawn from
the ACR-RSNA-CDEs next-gen graph, the RSNA Playbook, and the June 2026 SIIM
talk.

Layout: three full-width horizontal BANDS stacked top to bottom, each laid
out left-to-right (not as a deep tree), so nearly every cross-sector edge is
a short vertical between adjacent bands. Two edges (pulmonary nodule -> lung,
pleural effusion -> pleural space) are plumb-straight drops: their sources and
targets share an x-coordinate on purpose. Because of that, "thorax" is offset
left of "lung" (it doesn't need to share lung's column, just sit near it) so
it doesn't block the straight drop coming down through its own row.

    +--------------------------------------------------------+
    | Band 1 -- Sector 1: Finding / diagnosis definitions    |
    +--------------------------------------------------------+
    (gap, short "scoped to" verticals cross here)
    +--------------------------------------------------------+
    | Band 2 -- Sector 2: Anatomic locations                 |
    +--------------------------------------------------------+
    (gap, short "covers"/"included"/"edge (usually)" verticals)
    +--------------------------------------------------------+
    | Band 3 -- Sector 3: Exam types                         |
    +--------------------------------------------------------+
    +--------------------------------------------------------+
    | Legend                                                  |
    +--------------------------------------------------------+

The only long edges are pulmonary nodule -> CT Chest ("seen on") and
pulmonary nodule -> CT Thoracic spine ("possibly seen on", dashed), which
run down the left and right margins respectively, outside all three bands,
each in its own lane, jogging in only at the very end.

v6 changes: canvas narrowed from 1200px to 955px. Every x-coordinate below
was recomputed from measured text widths rather than estimated -- the
rendering font is `Helvetica, Segoe UI Emoji` as resolved by headless
Chromium, and the widths used here came from canvas `measureText` in that
same browser (see the note on Sector 3 below). Box widths are therefore
`measured text width + 20` (box() pads 10px each side), and the layout is
packed to a few pixels of slack in places, so changing a label's TEXT means
re-measuring, not just nudging a coordinate.

Sector 3 and the "two lines per Playbook member" request: the five Playbook
members cannot all carry their name on one line inside a <=960px canvas.
Their names measure 131 / 137 / 188 / 243 / 187 px at 13px, so five one-line
names plus box padding and gaps need ~1030px of row; the row has ~830px
between the grey "further nodes" dots and the right margin lane. The three
"CT Chest ..." members do fit on one line and are set that way (name, then
code); "CTA Chest vessels WO and W contrast IV" and "CT Thoracic spine W
contrast IV" wrap their name over two lines and keep the code on the last
line. Shrinking text below 13px or abbreviating the Playbook names were the
only other ways to make all five one-line, and both were rejected.

Output: knowledge/drafts/foundation-network.excalidraw; render with
render_excalidraw.py (see tools/diagrams/README.md).
"""
from __future__ import annotations

from excalib import TITLE, SUBTITLE, BODY, LINE, els, base, text, box, find, edge_point, arrow, save

# ---------------------------------------------------------------- palette
FINDING = ("#d1fae5", "#059669", "#064e3b")     # light green: finding
DIAGNOSIS = ("#6ee7b7", "#059669", "#064e3b")   # darker green: diagnosis (subtly different fill)
ASSESS = ("#e9d5ff", "#7e22ce", "#4c1d95")      # purple diamond: assessment scheme
ANATOMY = ("#bfdbfe", "#1d4ed8", "#1e3a8a")     # light blue: anatomic location
EXAM = ("#fde68a", "#b45309", "#78350f")        # light amber: exam type
GREY = ("#e5e7eb", "#9ca3af", "#4b5563")        # unlabeled / de-emphasized nodes
CROSS = "#be123c"                               # thick colored line: cross-sector relationship
BAND_BG = "#f8fafc"                             # sector band fill; label backings inside a band use it

# ---------------------------------------------------------------- helpers (local to this builder)
def region(id_: str, x: float, y: float, w: float, h: float, title: str) -> None:
    """Faint background rectangle with a title, drawn first so nodes sit on top."""
    r = base("rectangle", id_, x, y, w, h, "#e2e8f0", BAND_BG, sw=1)
    r["roundness"] = {"type": 3}
    els.append(r)
    els.append(text(id_ + "_title", x + 14, y + 10, title, size=15, color=TITLE))


def dot(id_: str, cx: float, cy: float, r: float, fill=GREY[0], stroke=GREY[1]) -> dict:
    e = base("ellipse", id_, cx - r, cy - r, 2 * r, 2 * r, stroke, fill, sw=1)
    els.append(e)
    return e


def diamond(id_: str, x: float, y: float, w: float, h: float, label: str, colors, size=13) -> dict:
    fill, stroke, tcolor = colors
    d = base("diamond", id_, x, y, w, h, stroke, fill)
    t = text(id_ + "_t", x + w * 0.2, y + h * 0.32, label, size=size, color=tcolor, align="center", w=w * 0.6, container=id_)
    t["height"] = h * 0.36
    d["boundElements"] = [{"id": t["id"], "type": "text"}]
    els.extend([d, t])
    return d


def faint(id_: str, x1: float, y1: float, x2: float, y2: float) -> None:
    ln = base("arrow", id_, x1, y1, x2 - x1, y2 - y1, "#9ca3af", "transparent", sw=1)
    ln.update({"points": [[0, 0], [x2 - x1, y2 - y1]], "startBinding": None, "endBinding": None,
               "startArrowhead": None, "endArrowhead": None, "boundElements": None, "opacity": 40})
    els.append(ln)


def mpath(id_: str, pts: list[tuple[float, float]], color: str, dashed=False, sw=3,
          label: str | None = None, label_pos: tuple[float, float] | None = None, label_color=BODY,
          label_w: float | None = None, label_bg_color: str = "#ffffff") -> None:
    """Multi-point routed arrow (elbow arrow() only supports 3 points).

    label_w: MEASURED text width in px. The backing box is sized from it, so
    passing a measured value (rather than a char-count estimate) is what keeps
    a margin-lane label from pushing the canvas wider than the bands.
    label_bg_color: BAND_BG for a label that lands inside a sector band, white
    for one in a band gap -- a white patch on the tinted band is visible.
    """
    x0, y0 = pts[0]
    rel = [[px - x0, py - y0] for px, py in pts]
    ar = base("arrow", id_, x0, y0, pts[-1][0] - x0, pts[-1][1] - y0, color, "transparent", dashed=dashed, sw=sw)
    ar.update({"points": rel, "startBinding": None, "endBinding": None,
               "startArrowhead": None, "endArrowhead": "arrow", "boundElements": None})
    els.append(ar)
    if label:
        lw = label_w if label_w is not None else max(len(ln_) for ln_ in label.split("\n")) * 13 * 0.62
        lx, ly = label_pos
        lh = len(label.split("\n")) * 13 * 1.25
        bg = base("rectangle", id_ + "_bg", lx - lw / 2 - 5, ly - 3, lw + 10, lh + 6, "transparent", label_bg_color, sw=0)
        els.append(bg)
        els.append(text(id_ + "_l", lx - lw / 2, ly, label, size=13, color=label_color, align="center", w=lw))


def label_bg(id_: str, cx: float, cy: float, label: str, w: float, size=13, color=BODY,
             bg_color: str = "#f8fafc") -> None:
    """A standalone edge label with an opaque backing box so it never sits on
    top of node text or an edge. w: MEASURED text width in px (see mpath).
    bg_color defaults to the band fill, since every one of these sits inside a
    band; pass white for a label placed in a band gap."""
    lines = label.split("\n")
    bw = w + 10
    bh = len(lines) * size * 1.25 + 6
    bg = base("rectangle", id_ + "_bg", cx - bw / 2, cy - bh / 2, bw, bh, "transparent", bg_color, sw=0)
    els.append(bg)
    els.append(text(id_ + "_t", cx - bw / 2 + 5, cy - bh / 2 + 3, label, size=size, color=color, align="center", w=w))


# ---------------------------------------------------------------- canvas / bands
CONTENT_W = 935          # + 2 x 10px export padding = 955px canvas
LANE_L = 8               # "seen on" lane, left margin
LANE_R = 912             # "possibly seen on" lane, just inside the right edge

BAND1 = dict(x=0, y=70, w=CONTENT_W, h=300)                              # bottom 370
GAP1 = 70
BAND2 = dict(x=0, y=BAND1["y"] + BAND1["h"] + GAP1, w=CONTENT_W, h=370)  # 440, bottom 810
GAP2 = 70
BAND3 = dict(x=0, y=BAND2["y"] + BAND2["h"] + GAP2, w=CONTENT_W, h=300)  # 880, bottom 1180
LEGEND = dict(x=0, y=BAND3["y"] + BAND3["h"] + 30, w=CONTENT_W, h=190)   # 1210

els.append(text("maintitle", 0, 8, "Foundation Context: a mini-network", size=20, color=TITLE))
els.append(text("subtitle", 0, 34, "three sectors of shared, curated knowledge — illustrative, not exhaustive", size=13, color=SUBTITLE))

region("rA", **BAND1, title="Sector 1 — Finding / diagnosis definitions")
region("rB", **BAND2, title="Sector 2 — Anatomic locations")
find("rB_title")["x"] += 40  # keep clear of the "seen on" lane running down x=8
region("rC", **BAND3, title="Sector 3 — Exam types")
els.append(text("rC_tag", BAND3["x"] + 14, BAND3["y"] + 30, "(content to come)", size=13, color=BODY))
region("rL", **LEGEND, title="Legend")

# ================================================================== BAND 1: Finding / diagnosis definitions
# Row 1, left to right: lung cancer, pulmonary nodule, Lung-RADS, pleural
# effusion. Row 2, under pulmonary nodule: the three subtypes, spread wide for
# label room; solid component hangs below-right of part-solid, offset so it
# doesn't block pulmonary nodule's straight column down to lung. Grey "more"
# nodes sit at the far left of row 2.
COL_PN = 345     # pulmonary nodule / lung share this column (straight drop)
COL_PE = 708     # pleural effusion / pleural space share this one

lung_cancer = box("lung_cancer", 20, 110, 140, 42, "lung cancer", DIAGNOSIS, size=14)
pulm_nodule = box("pulm_nodule", 272, 100, 146, 54, "pulmonary\nnodule", FINDING, size=14)   # center 345
lungrads = diamond("lungrads", 492, 95, 125, 75, "Lung-RADS", ASSESS, size=13)
pleural_effusion = box("pleural_effusion", 637, 110, 142, 42, "pleural effusion", FINDING, size=13)  # center 708

solid_nodule = box("solid_nodule", 120, 210, 105, 70, "solid\npulmonary\nnodule", FINDING, size=13)
partsolid_nodule = box("partsolid_nodule", 235, 210, 100, 70, "part-solid\npulmonary\nnodule", FINDING, size=13)
nonsolid_nodule = box("nonsolid_nodule", 530, 210, 100, 70, "non-solid\npulmonary\nnodule", FINDING, size=13)
solid_component = box("solid_component", 365, 295, 118, 38, "solid component", FINDING, size=13)

dot("gA1", 50, 235, 15)
dot("gA2", 75, 270, 13)
dot("gA3", 55, 295, 12)
faint("fA_12", 50, 235, 75, 270)
faint("fA_13", 50, 235, 55, 295)
faint("fA_into", 75, 270, 120, 245)  # gA2 -> solid pulmonary nodule (nearest labeled node)

# The two left-hand "subtype of" labels sit BELOW the "seen on" lane's top
# horizontal (y=166) and to the LEFT of the red column at x=345; the right-hand
# one sits ABOVE the "possibly seen on" lane's top horizontal (y=190). That is
# what keeps the red pulmonary-nodule -> lung vertical off all three of them.
arrow("e_solid_sub", "solid_nodule", "top", "pulm_nodule", "bottom", None, s_frac=0.5, d_frac=0.15)
arrow("e_partsolid_sub", "partsolid_nodule", "top", "pulm_nodule", "bottom", None, s_frac=0.4, d_frac=0.5)
arrow("e_nonsolid_sub", "nonsolid_nodule", "top", "pulm_nodule", "bottom", None, s_frac=0.2, d_frac=0.9)
# All three "subtype of" labels are white-backed and placed by hand: their own
# edges are diagonals that would otherwise run through the text, and the left
# two have to stay clear of the "seen on" lane above (y=166) and the red
# pulmonary-nodule column at x=345.
label_bg("l_solid_sub", 205, 189, "subtype of", 60.0)
label_bg("l_partsolid_sub", 290, 189, "subtype of", 60.0)
label_bg("l_nonsolid_sub", 487, 169, "subtype of", 60.0)
arrow("e_partsolid_comp", "partsolid_nodule", "bottom", "solid_component", "top", "has component", s_frac=0.6, d_frac=0.3,
      label_size=13, label_dx=60)
arrow("e_manifest", "lung_cancer", "right", "pulm_nodule", "left", "may manifest as", s_frac=0.4, d_frac=0.35,
      label_size=13, label_dy=-26)
arrow("e_progress", "nonsolid_nodule", "left", "partsolid_nodule", "right", "may progress to", s_frac=0.5, d_frac=0.5,
      dashed=True, label_size=13, label_dy=-24)
arrow("e_assessed", "pulm_nodule", "right", "lungrads", "left", "assessed by", s_frac=0.25, d_frac=0.4,
      label_size=13, label_dx=6, label_dy=-24)
# pleural_effusion intentionally has no edge to pulm_nodule -- just a neighbor
# solid_component intentionally has no cross-sector "scoped to" edge -- only
# pulmonary nodule, lung cancer, and pleural effusion are scoped to anatomy

# ================================================================== BAND 2: Anatomic locations
# thorax sits center-left, offset from lung's own column, on purpose: it leaves
# x=345 clear so pulmonary nodule's edge can drop straight into lung without
# detouring around thorax, AND leaves x=300 clear for lung cancer's arrival at
# lung's top-left. pleural space is pulled right, under pleural effusion, so
# ITS edge can also be a straight drop.
BY = BAND2["y"]
thorax = box("thorax", 160, BY + 40, 110, 42, "thorax", ANATOMY, size=14)                 # 160-270
pleural_space = box("pleural_space", 654, BY + 40, 108, 44, "pleural\nspace", ANATOMY, size=13)   # center 708
upper_abdomen = box("upper_abdomen", 777, BY + 40, 115, 42, "upper abdomen", GREY, dashed=True, size=13)  # ends 892, lane at 912

right_lung = box("right_lung", 150, BY + 110, 105, 40, "right lung", ANATOMY, size=13)
lung = box("lung", 280, BY + 110, 130, 42, "lung", ANATOMY, size=14)                      # center 345
left_lung = box("left_lung", 435, BY + 110, 105, 40, "left lung", ANATOMY, size=13)

# Row 3 is pushed down to BY+220 to open a clear horizontal corridor at BY+200
# for the labels, and the gap between the two row-3 boxes (278..310) is the
# corridor the red "included" edge climbs to reach lung's bottom-left.
upper_lobe = box("upper_lobe", 140, BY + 220, 138, 42, "upper lobe of\nright lung", ANATOMY, size=13)
lung_parenchyma = box("lung_parenchyma", 310, BY + 220, 120, 44, "lung\nparenchyma", ANATOMY, size=13)

dot("gB1", 50, BY + 250, 15)
dot("gB2", 75, BY + 285, 13)
dot("gB3", 55, BY + 310, 12)
faint("fB_12", 50, BY + 250, 75, BY + 285)
faint("fB_13", 50, BY + 250, 55, BY + 310)
faint("fB_into", 75, BY + 285, 140, BY + 245)  # gB2 -> upper lobe of right lung (nearest labeled node)

arrow("e_rlung_lung", "right_lung", "right", "lung", "left", None, s_frac=0.5, d_frac=0.3)
arrow("e_llung_lung", "left_lung", "left", "lung", "right", None, s_frac=0.5, d_frac=0.7)
arrow("e_ulobe_rlung", "upper_lobe", "top", "right_lung", "bottom", None, s_frac=0.4, d_frac=0.4)
# lung parenchyma's edge runs into lung's BOTTOM-RIGHT (x=394), leaving the
# space under lung's center free for "laterality", which now sits between the
# red "included" arrowhead (x=294) and that edge -- on neither of them.
arrow("e_parenchyma_lung", "lung_parenchyma", "top", "lung", "bottom", None, s_frac=0.7, d_frac=0.88)
arrow("e_pspace_thorax", "pleural_space", "left", "thorax", "right", None, s_frac=0.5, d_frac=0.5)

label_bg("l_ulobe_rlung", 197, BY + 172, "contained by", 73.7)
label_bg("l_laterality", 345, BY + 172, "laterality", 48.4)
label_bg("l_parenchyma_lung", 487, BY + 172, "part of", 36.9)
label_bg("l_pspace_thorax", 480, BY + 55, "contained by", 73.7)

# ================================================================== BAND 3: Exam types
# Row 1: CT Chest (preferred, to come). Row 2, left to right: the four real
# Playbook entries with codes, then CT Thoracic spine (dashed) at the far
# right; grey "more" nodes at the far left. "Region imaged" hangs below
# "CT Chest W contrast IV". Box widths are measured-text + 20 and gaps are 8px
# -- see the module docstring on why only three of the five get a one-line name.
CY = BAND3["y"]
ct_chest = box("ct_chest", 285, CY + 40, 230, 60, "CT Chest\npreferred (to come)", EXAM, size=14)

ct_wo = box("ct_wo", 90, CY + 130, 152, 70, "CT Chest WO contrast\n29252-4", EXAM, size=13)
ct_w = box("ct_w", 250, CY + 130, 158, 70, "CT Chest W contrast IV\n24628-0", EXAM, size=13)
ct_wo_w = box("ct_wo_w", 416, CY + 130, 209, 70, "CT Chest WO and W contrast IV\n30598-7", EXAM, size=13)
ct_cta = box("ct_cta", 633, CY + 130, 151, 70, "CTA Chest vessels\nWO and W contrast IV\n30804-9", EXAM, size=13)
ct_thoracic_spine = box("ct_thoracic_spine", 792, CY + 130, 126, 70, "CT Thoracic spine\nW contrast IV\n24979-7", GREY, dashed=True, size=13)

region_imaged = box("region_imaged", 266, CY + 220, 126, 40, "Region imaged:\nThorax (RID1243)", GREY, size=13)

dot("gC1", 42, CY + 165, 14)
dot("gC2", 64, CY + 198, 12)
faint("fC_12", 42, CY + 165, 64, CY + 198)
faint("fC_into", 42, CY + 165, 90, CY + 165)  # gC1 -> CT Chest WO contrast (nearest labeled node)

arrow("e_wo_family", "ct_wo", "top", "ct_chest", "bottom", "member of family", s_frac=0.5, d_frac=0.1,
      label_size=13, label_dx=-15, label_dy=-20)
arrow("e_w_family", "ct_w", "top", "ct_chest", "bottom", None, s_frac=0.5, d_frac=0.35)
arrow("e_wo_w_family", "ct_wo_w", "top", "ct_chest", "bottom", None, s_frac=0.5, d_frac=0.65)
arrow("e_cta_family", "ct_cta", "top", "ct_chest", "bottom", None, s_frac=0.3, d_frac=0.9)
arrow("e_w_regionimaged", "ct_w", "bottom", "region_imaged", "top", "Playbook part", s_frac=0.5, d_frac=0.5,
      label_size=13, label_dx=107, label_dy=0)

# ================================================================== cross-sector edges (thick, colored)
# Band 1 -> Band 2.
# "pulmonary nodule" and "lung" share x=345 -- a genuinely straight drop, clear
# of row 2's subtypes/solid component (both kept off that column), of all three
# "subtype of" labels, and of thorax (offset left of lung for exactly this
# reason).
mpath("cx_pn_lung",
      [edge_point(find("pulm_nodule"), "bottom", 0.5), edge_point(find("lung"), "top", 0.5)],
      color=CROSS, sw=3, label="scoped to", label_pos=(392, 396), label_w=56.4)

# "lung cancer" drops from its own bottom, one right-angle jog at the midpoint
# of the band gap, then straight down into lung's top-left corner -- 45px left
# of pulmonary nodule's top-center arrival, so the two arrowheads land at
# separate points on "lung", not on top of each other.
mpath("cx_lc_lung",
      [edge_point(find("lung_cancer"), "bottom", 0.5), (90, 405), (300, 405),
       edge_point(find("lung"), "top", 0.15)],
      color=CROSS, sw=3, label="scoped to", label_pos=(195, 393), label_w=56.4)

# "pleural effusion" and "pleural space" also share an x (708) -- straight drop,
# since pleural space was pulled right specifically to sit under it.
mpath("cx_pe_pspace",
      [edge_point(find("pleural_effusion"), "bottom", 0.5), edge_point(find("pleural_space"), "top", 0.5)],
      color=CROSS, sw=3, label="scoped to", label_pos=(748, 286), label_w=56.4, label_bg_color=BAND_BG)

# Band 3 -> Band 2 (pointing up): each uses its own left/right-margin column
# through band 2 so it clears the nodes directly in its way. "included" climbs
# the 32px corridor between the two row-3 boxes rather than cutting across the
# label row, so it crosses neither "contained by" nor the upper-lobe edge.
mpath("cx_ctchest_thorax",
      [edge_point(find("ct_chest"), "top", 0.15), (319.5, 846), (100, 846), (100, BY + 61),
       edge_point(find("thorax"), "left", 0.5)],
      color=CROSS, sw=3, label="covers", label_pos=(66, 814), label_w=38.3)

mpath("cx_ctchest_lung",
      [edge_point(find("ct_chest"), "top", 0.3), (354, 868), (118, 868), (118, BY + 290), (294, BY + 290),
       edge_point(find("lung"), "bottom", 0.11)],
      color=CROSS, sw=3, label="included", label_pos=(160, 814), label_w=48.4)

mpath("cx_ctchest_abdomen",
      [edge_point(find("ct_chest"), "top", 0.85), (480.5, 846), (834.5, 846),
       edge_point(find("upper_abdomen"), "bottom", 0.5)],
      color=CROSS, dashed=True, sw=2, label="edge (usually)", label_pos=(834.5, 683), label_w=81.7, label_bg_color=BAND_BG)

# The two long edges run down dedicated margin lanes outside all three bands,
# jogging in only once, right at the end. The right lane turns in above band 3's
# exam row, so CT Thoracic spine can use the full width up to the margin.
mpath("cx_pn_ctchest",
      [edge_point(find("pulm_nodule"), "left", 1.0), (272, 166), (LANE_L, 166), (LANE_L, CY + 70),
       edge_point(find("ct_chest"), "left", 0.5)],
      color=CROSS, sw=3, label="seen on", label_pos=(48, 592), label_w=46.3, label_bg_color=BAND_BG)

mpath("cx_pn_ctspine",
      [edge_point(find("pulm_nodule"), "right", 1.0), (418, 190), (LANE_R, 190), (LANE_R, CY + 70), (855, CY + 70),
       edge_point(find("ct_thoracic_spine"), "top", 0.5)],
      color=CROSS, dashed=True, sw=2, label="possibly seen on", label_pos=(872, 392), label_w=96.8)

# ================================================================== legend (full-width strip, 2 columns)
node_rows = [
    ("rect", FINDING, "finding"),
    ("rect", DIAGNOSIS, "diagnosis"),
    ("diamond", ASSESS, "assessment scheme"),
    ("rect", ANATOMY, "anatomic location"),
    ("rect", EXAM, "exam type"),
]
edge_rows = [
    ("dot", GREY, "unlabeled grey = further nodes not shown"),
    ("line", LINE, "solid edge = within-sector relationship"),
    ("thick", CROSS, "colored thick edge = cross-sector relationship"),
    ("dash", LINE, "dashed = possible or planned"),
]

LX1, LX2 = LEGEND["x"] + 24, LEGEND["x"] + CONTENT_W // 2 + 10
LY = LEGEND["y"] + 34

y = LY
for i, (kind, colors, label) in enumerate(node_rows):
    fill, stroke, _tc = colors
    if kind == "rect":
        sw_el = base("rectangle", f"legA{i}", LX1, y, 22, 16, stroke, fill, sw=1)
        sw_el["roundness"] = {"type": 3}
        els.append(sw_el)
    elif kind == "diamond":
        els.append(base("diamond", f"legA{i}", LX1, y - 3, 24, 22, stroke, fill))
    els.append(text(f"legA{i}_l", LX1 + 32, y - 1, label, size=13, color=BODY, w=340))
    y += 28

y = LY
for i, (kind, color, label) in enumerate(edge_rows):
    if kind == "dot":
        dot(f"legB{i}", LX2 + 11, y + 8, 9, fill=color[0], stroke=color[1])
    elif kind == "line":
        els.append(base("line", f"legB{i}", LX2, y + 8, 30, 0, color, "transparent", sw=2))
        find(f"legB{i}")["points"] = [[0, 0], [30, 0]]
        find(f"legB{i}")["boundElements"] = None
    elif kind == "thick":
        els.append(base("line", f"legB{i}", LX2, y + 8, 30, 0, color, "transparent", sw=3))
        find(f"legB{i}")["points"] = [[0, 0], [30, 0]]
        find(f"legB{i}")["boundElements"] = None
    elif kind == "dash":
        els.append(base("line", f"legB{i}", LX2, y + 8, 30, 0, color, "transparent", sw=2, dashed=True))
        find(f"legB{i}")["points"] = [[0, 0], [30, 0]]
        find(f"legB{i}")["boundElements"] = None
    els.append(text(f"legB{i}_l", LX2 + 40, y - 1, label, size=13, color=BODY, w=340))
    y += 28

save("knowledge/drafts/foundation-network.excalidraw")
