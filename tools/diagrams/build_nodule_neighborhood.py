#!/usr/bin/env python3
"""Build the "pulmonary nodule neighborhood" diagram (v3).

One FindingClass and everything that hangs off it, drawn as nodes and labeled
edges. The point of the figure is the SHAPE of the neighborhood -- which kinds
of thing attach to a finding definition, and by which named relationship --
not the content of any one node, so every node carries only its name plus its
node kind on a small second line.

v2 IS ILLUSTRATIVE, NOT A DUMP OF THE GRAPH
-------------------------------------------
v1 drew only edges committed to the CDE graph. v2 reflects updates the
project's clinical expert intends for that graph, so some nodes, names and
edges below do not exist at the pin. The figure says so on a caption line
under the legend, and the two lists in the next section say exactly which is
which. Nothing here was invented by the builder: every "intended" item came
from the project lead by way of the brief for this version.

SOURCE OF THE COMMITTED DATA
----------------------------
~/ACR-RSNA-CDEs, branch next-gen-2026, pinned commit
b541b74c22a33b64834309244569a60d06de79e4, file (read with `git show`, i.e.
the committed copy, not the working tree):

    docs/next-gen-schema/alpha/graph/definition-graph.json

Centre node: FC-000005 "pulmonary nodule" (node: FindingClass).

COMMITTED AT b541b74 -- 15 of the 22 edges drawn
------------------------------------------------
  SUBTYPE_OF        2   FC-000006 solid pulmonary nodule -> FC-000005
                        FC-000007 part-solid pulmonary nodule -> FC-000005
  HAS_COMPONENT     1   FC-000007 -> FC-000009 solid component of part-solid
                        pulmonary nodule  (the graph also carries the inverse
                        COMPONENT_OF, not drawn)
  HAS_DATA_ELEMENT  3   FC-000005 -> DE-000001 presence, DE-000004
                        calcification, DE-000015 interval change
  HAS_MEASUREMENT   2   FC-000005 -> MS-000003 mean diameter,
                        MS-000001 long-axis diameter
  ASSESSED_BY       1   FC-000005 -> AS-000001 Lung-RADS
  SCOPED_TO         1   FC-000005 -> RID1301 lung
                        props: kind=region, strength=required
  SEEN_ON           3   FC-000005 -> CT, XR, MR  (the graph also has US and
                        PET on this finding; those two are not drawn)
  IN_SUBSPECIALTY   1   FC-000005 -> CH
  MAY_MANIFEST_AS   0   see below -- both drawn manifestation edges are
                        intended, neither is committed in the form drawn.
  plus SUBTYPE_OF   2   drawn but NOT committed (see below), for 22 total.

INTENDED, NOT AT THE PIN -- 7 edges and the nodes they need
------------------------------------------------------------
  Renamed data elements. "composition" replaces DE-000002 attenuation on this
    finding, and "margin" replaces DE-000039 pulmonary margin. Both
    HAS_DATA_ELEMENT edges are committed under the old names. A separate node
    already named "composition" (DE-000006) exists in the graph for other
    findings, so the rename points at a name the vocabulary already uses.
  Dropped measurement. MS-000006 lesion count is a committed HAS_MEASUREMENT
    target of FC-000005; removing it is the intended change.
  Renamed subtype. "ground glass nodule" renames FC-000008 non-solid
    pulmonary nodule. FC-000025 "ground-glass opacity" is a DIFFERENT node
    that stays where it is.
  Grouping node. "pulmonary parenchymal abnormality" and BOTH SUBTYPE_OF
    edges into it (from pulmonary nodule and from pulmonary granuloma) are
    intended. The alpha contains no Grouping nodes at all at this commit.
  Diagnosis "pulmonary neoplasm" and its MAY_MANIFEST_AS -> pulmonary nodule.
    No such node exists at the pin. The committed diagnoses that reach this
    family are DX-000004 lung cancer, which manifests as all three SUBTYPES,
    and DX-000009 metastatic disease, the only one with a direct edge into
    FC-000005 (that was the diagnosis v1 drew).
  Retargeted manifestation. DX-000002 pulmonary granuloma is committed, but
    its MAY_MANIFEST_AS points at FC-000006 solid pulmonary nodule, not at
    the parent. Pointing it at FC-000005 is the intended change.
  AssessmentScheme "Fleischner criteria" and its ASSESSED_BY edge. Not at the
    pin; the five committed schemes are Lung-RADS, ACR TI-RADS, LI-RADS,
    Bosniak classification and BI-RADS assessment.

Two labels are committed content shown in a reader-friendly form rather than
changed content. The Subspecialty node's `name` is the code "CH" and its
`definition` is "Chest Radiology"; the box shows the definition, since "CH"
alone says nothing. The Modality nodes carry RadLex definitions (Computed
Tomography, Projection Radiography, Magnetic Resonance Imaging) that do not
fit half-size boxes, so those three show the committed ids only.

Not drawn at all, by instruction: values, time course, etiology. Also left
out: HAS_ANATOMIC_REFINEMENT_RULE -> ARR-000001, whose target is a node kind
outside the nine the legend names.

RELATIONSHIP NAMES
------------------
Every edge label is the committed `edge` string from definition-graph.json,
and all nine agree with the relationship table on
knowledge/drafts/next-generation-schema.md. The older names that circulate
elsewhere in the same repository are NOT used: HAS_ELEMENT (for
HAS_DATA_ELEMENT) and MAY_HAVE_COMPONENT (for HAS_COMPONENT), both of which
survive in graph/core.jsonl and in the retired 2026-09-03 fc-neighborhood
diagram. The schema page flags that older pair itself.

LAYOUT
------
About 1050 x 820. v1 packed eight arrows out of the centre node's right edge
into a 180px corridor; v2 has fewer targets there (five data elements, two
measurements) AND a corridor half again as wide, so the fan opens at roughly
39px of label pitch instead of 26px. The centre node sits mid-canvas with the
Grouping directly above it, the two assessment schemes up and to the right,
the two diagnoses up and to the left, the subtype row below, and the
context nodes -- lung, three modalities, the subspecialty -- down the left
margin.

Two routing facts hold the left margin together. The diagnosis that also
points UP at the Grouping (granuloma) sits ABOVE the one that only points at
the nodule (neoplasm); reversing them makes the two arrows cross. And the
SCOPED_TO arrow leaves the centre node BELOW the point where the neoplasm's
manifestation arrow arrives, which is what keeps those two apart.

Every arrow is emitted before every label plate: the plates are opaque and
mask the lines they lie across, so an arrow drawn after a plate would cut
through the label's text.

Text widths are measured, not estimated (see tools/diagrams/README.md): the
render font is `Helvetica, Segoe UI Emoji` as resolved by headless Chromium,
and every box width and plate width below comes from canvas measureText() at
the same size in that browser.

Colours follow build_foundation_network.py so the figures name the same kinds
the same way: FINDING green, DIAGNOSIS darker green, ASSESS purple,
ANATOMY blue, GREY modality. Four kinds are local to this figure: DataElement
takes the lightest step of excalib's ROSE ramp, Measurement the lightest step
of VIOLET, Grouping a paler green than FINDING with a dashed stroke (it is a
container, not a finding you would report), and Subspecialty a desaturated
grey-violet that reads as metadata next to both.

v3 change: the two AssessmentScheme nodes are OVALS, not diamonds. A diamond
reads as a flowchart decision, which is not what an assessment scheme is.
Same purple fill and stroke, same 190x92 envelope, labels still centred, and
the legend swatch is an oval to match. Both ASSESSED_BY arrows are drawn by
ray() so their heads land on the ellipse outline rather than on a
bounding-box extreme; see that helper for why excalib.arrow() cannot.

Excalidraw has no italic font variant -- fontFamily is an integer code with
no style axis -- so the caption under the legend is set small and grey rather
than italic.

Output: knowledge/drafts/nodule-neighborhood.excalidraw; render with
render_excalidraw.py (see tools/diagrams/README.md).
"""
from __future__ import annotations

from excalib import (BODY, LINE, CAPTION, els, base, text, find, edge_point, arrow,
                     tri_head, save)

# ---------------------------------------------------------------- palette
# (fill, stroke, text, mid) -- "mid" is the tone for the small kind line.
FINDING = ("#d1fae5", "#059669", "#064e3b", "#047857")    # FindingClass
GROUPING = ("#ecfdf5", "#10b981", "#065f46", "#059669")   # Grouping (dashed)
DIAGNOSIS = ("#6ee7b7", "#059669", "#064e3b", "#047857")  # Diagnosis
ASSESS = ("#e9d5ff", "#7e22ce", "#4c1d95", "#7e22ce")     # AssessmentScheme (oval)
ANATOMY = ("#bfdbfe", "#1d4ed8", "#1e3a8a", "#1d4ed8")    # AnatomicLocation
GREY = ("#e5e7eb", "#6b7280", "#374151", "#4b5563")       # Modality
DATAEL = ("#ffe4e6", "#be123c", "#881337", "#be123c")     # DataElement (ROSE, lightest)
MEAS = ("#ede9fe", "#6d28d9", "#4c1d95", "#6d28d9")       # Measurement (VIOLET, lightest)
SUBSPEC = ("#e5e3ee", "#78748f", "#3c3a52", "#5d5a78")    # Subspecialty (grey-violet)

HEAD = 10.0        # solid tri_head length, independent of line weight
KIND_SIZE = 11     # the small second line inside every node


# ---------------------------------------------------------------- helpers
def kind_box(id_, x, y, w, h, name, kind, pal, size=14, lines=None, dashed=False,
             kind_size=KIND_SIZE):
    """A node: rounded rect, name centred, node kind on a small line under it.
    `lines` overrides the name's line breaks (list of strings)."""
    fill, stroke, tcol, mid = pal
    r = base("rectangle", id_, x, y, w, h, stroke, fill, dashed=dashed)
    r["roundness"] = {"type": 3}
    els.append(r)
    nl = lines or [name]
    block = len(nl) * size * 1.25 + 3 + kind_size * 1.25
    ty = y + (h - block) / 2
    els.append(text(id_ + "_n", x + 8, ty, "\n".join(nl), size=size, color=tcol,
                    align="center", w=w - 16))
    els.append(text(id_ + "_k", x + 8, ty + len(nl) * size * 1.25 + 3, kind,
                    size=kind_size, color=mid, align="center", w=w - 16))
    return r


def oval_node(id_, x, y, w, h, name, kind, pal, size=14):
    """Same two-line content as kind_box, in an ellipse. v3 change: these were
    diamonds through v2, which read as flowchart decisions. Same fill, stroke
    and size envelope; only the outline changed.

    The text column is the middle 72% of the width. An ellipse is widest at
    its vertical centre and the two-line block reaches only +-17px from it,
    where the half-width is still 93% of the semi-axis, so 72% clears the
    curve with room to spare (a diamond only allowed 60%)."""
    fill, stroke, tcol, mid = pal
    d = base("ellipse", id_, x, y, w, h, stroke, fill)
    els.append(d)
    block = size * 1.25 + 3 + KIND_SIZE * 1.25
    ty = y + (h - block) / 2
    els.append(text(id_ + "_n", x + w * 0.14, ty, name, size=size, color=tcol,
                    align="center", w=w * 0.72))
    els.append(text(id_ + "_k", x + w * 0.14, ty + size * 1.25 + 3, kind,
                    size=KIND_SIZE, color=mid, align="center", w=w * 0.72))
    return d


def ray(id_, src, s_side, s_frac, dst, label, t):
    """A straight arrow from a box edge to a point ON an ellipse's outline.

    excalib.arrow() lands on the destination's BOUNDING BOX, which for an
    ellipse means the head stops at whichever of the four extreme points the
    named side picks -- fine for a vertical or horizontal approach, wrong for
    a diagonal one, which is what both ASSESSED_BY arrows are. This instead
    solves for the boundary point along the line from the ellipse's centre to
    the source, so each head meets the curve square on. `t` places the label
    along the same line, so moving an endpoint moves its label with it."""
    a, b = find(src), find(dst)
    x1, y1 = edge_point(a, s_side, s_frac)
    cx, cy = b["x"] + b["width"] / 2, b["y"] + b["height"] / 2
    rx, ry = b["width"] / 2, b["height"] / 2
    dx, dy = x1 - cx, y1 - cy
    k = 1.0 / ((dx / rx) ** 2 + (dy / ry) ** 2) ** 0.5
    x2, y2 = cx + dx * k, cy + dy * k
    ln = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 or 1.0
    ex = x2 - (x2 - x1) / ln * HEAD * 0.55      # stop short so the head's base sits on the line
    ey = y2 - (y2 - y1) / ln * HEAD * 0.55
    ar = base("arrow", id_, x1, y1, ex - x1, ey - y1, LINE, "transparent", sw=2)
    ar.update({"points": [[0, 0], [ex - x1, ey - y1]], "startBinding": None,
               "endBinding": None, "startArrowhead": None, "endArrowhead": None,
               "boundElements": None})
    els.append(ar)
    tri_head(id_ + "_h", (x2, y2), (x1, y1), LINE, size=HEAD)
    lab("l_" + id_, x1 + t * (x2 - x1), y1 + t * (y2 - y1), label)


def edge(id_, src, s_side, dst, d_side, s_frac=0.5, d_frac=0.5, elbow=None):
    """excalib.arrow() with its open head replaced by a fixed-size solid one."""
    arrow(id_, src, s_side, dst, d_side, s_frac=s_frac, d_frac=d_frac,
          color=LINE, sw=2, elbow=elbow)
    a = find(id_)
    a["endArrowhead"] = None
    tip = (a["x"] + a["points"][-1][0], a["y"] + a["points"][-1][1])
    frm = (a["x"] + a["points"][-2][0], a["y"] + a["points"][-2][1])
    tri_head(id_ + "_h", tip, frm, LINE, size=HEAD)


def plate(id_, cx, cy, s, w, size=13, pad_x=6, pad_y=4):
    """An edge label on an opaque white plate centred on (cx, cy), so it masks
    the line it sits on. `w` is the MEASURED text width."""
    bw, bh = w + 2 * pad_x, size * 1.25 + 2 * pad_y
    r = base("rectangle", id_, cx - bw / 2, cy - bh / 2, bw, bh, "transparent", "#ffffff", sw=0)
    r["roundness"] = {"type": 3}
    els.append(r)
    els.append(text(id_ + "_t", cx - bw / 2 + pad_x, cy - bh / 2 + pad_y, s,
                    size=size, color=BODY, align="center", w=w))


# Measured label widths at 13px Helvetica (headless Chromium).
LW = {"MAY_MANIFEST_AS": 124.7, "ASSESSED_BY": 94.7, "SUBTYPE_OF": 86.0,
      "HAS_DATA_ELEMENT": 135.3, "HAS_MEASUREMENT": 135.1, "SCOPED_TO": 79.9,
      "SEEN_ON": 62.1, "HAS_COMPONENT": 118.5, "IN_SUBSPECIALTY": 117.5}

LABELS: list[tuple[str, float, float, str]] = []


def lab(id_, cx, cy, name):
    """Queue an edge label; all of them are flushed after every arrow is drawn."""
    LABELS.append((id_, cx, cy, name))


# ================================================================== nodes
# centre node and the Grouping directly above it
kind_box("fc", 400, 270, 240, 80, "pulmonary nodule", "FindingClass", FINDING, size=17)
kind_box("gr", 320, 25, 250, 70, "pulmonary parenchymal abnormality", "Grouping",
         GROUPING, dashed=True)

# diagnoses, upper-left. granuloma is ABOVE neoplasm because granuloma also
# points UP at the Grouping; the other order makes those two arrows cross.
kind_box("dx_gran", 20, 30, 165, 62, "pulmonary granuloma", "Diagnosis", DIAGNOSIS)
kind_box("dx_neo", 20, 140, 165, 62, "pulmonary neoplasm", "Diagnosis", DIAGNOSIS)

# assessment schemes, upper-right
oval_node("as_lr", 600, 14, 190, 92, "Lung-RADS", "AssessmentScheme", ASSESS)
oval_node("as_fl", 845, 14, 190, 92, "Fleischner criteria", "AssessmentScheme", ASSESS)

# subtypes (row below the centre node; smaller boxes, 13px names)
kind_box("s1", 300, 500, 140, 80, "solid pulmonary nodule", "FindingClass", FINDING,
         size=13, lines=["solid", "pulmonary nodule"])
kind_box("s2", 450, 500, 140, 80, "part-solid pulmonary nodule", "FindingClass", FINDING,
         size=13, lines=["part-solid", "pulmonary nodule"])
kind_box("s3", 600, 500, 140, 80, "ground glass nodule", "FindingClass", FINDING,
         size=13, lines=["ground glass", "nodule"])

# the component hanging off part-solid
kind_box("sc", 400, 630, 240, 70, "solid component", "FindingClass", FINDING, size=13,
         lines=["solid component of", "part-solid pulmonary nodule"])

# context nodes down the left margin
kind_box("an", 60, 290, 140, 60, "lung", "AnatomicLocation", ANATOMY)
kind_box("sp", 40, 370, 170, 60, "chest radiology", "Subspecialty", SUBSPEC)
for i, (mid_, nm) in enumerate([("md_ct", "CT"), ("md_xr", "XR"), ("md_mr", "MR")]):
    kind_box(mid_, 55, 480 + i * 48, 90, 38, nm, "Modality", GREY, size=13, kind_size=9)

# data elements and measurements, right column
COL_X, COL_W, ROW_H = 845, 190, 48
DE_NAMES = ["presence", "composition", "margin", "calcification", "interval change"]
for i, nm in enumerate(DE_NAMES):
    kind_box(f"de{i}", COL_X, 150 + i * 66, COL_W, ROW_H, nm, "DataElement", DATAEL)
for i, nm in enumerate(["mean diameter", "long-axis diameter"]):
    kind_box(f"ms{i}", COL_X, 510 + i * 66, COL_W, ROW_H, nm, "Measurement", MEAS)

# ================================================================== edges
# SUBTYPE_OF into the Grouping: from the centre node (plumb vertical) and from
# the granuloma (near-horizontal, in the 135px gap that fits its plate).
edge("e_gr_fc", "fc", "top", "gr", "bottom", s_frac=0.50, d_frac=0.80)
edge("e_gr_gn", "dx_gran", "right", "gr", "left", s_frac=0.50, d_frac=0.50)
lab("l_gr_fc", 520, 180, "SUBTYPE_OF")
lab("l_gr_gn", 252, 60, "SUBTYPE_OF")

# MAY_MANIFEST_AS x2, both into the centre node's left edge
edge("e_mma_gn", "dx_gran", "right", "fc", "left", s_frac=0.87, d_frac=0.15)
edge("e_mma_neo", "dx_neo", "right", "fc", "left", s_frac=0.50, d_frac=0.55)
lab("l_mma_gn", 292, 183, "MAY_MANIFEST_AS")
lab("l_mma_neo", 292, 242, "MAY_MANIFEST_AS")

# ASSESSED_BY x2, drawn by ray() so each head meets the oval's curve square
# on rather than stopping at a bounding-box extreme. Both run up and to the
# right; the Fleischner one passes well below the Lung-RADS oval and above
# the first data element.
ray("e_asb_lr", "fc", "top", 0.62, "as_lr", "ASSESSED_BY", 0.34)
ray("e_asb_fl", "fc", "top", 0.80, "as_fl", "ASSESSED_BY", 0.66)

# SUBTYPE_OF x3: each subtype -> the centre node (arrows point UP into it).
# The three plates are staggered along their arrows; level with each other
# they would collide, and the right one also has to stay clear of the
# measurement labels, so it rides high.
edge("e_st1", "s1", "top", "fc", "bottom", d_frac=0.35)
edge("e_st2", "s2", "top", "fc", "bottom", d_frac=0.50)
edge("e_st3", "s3", "top", "fc", "bottom", d_frac=0.72)
lab("l_st1", 410, 448, "SUBTYPE_OF")
lab("l_st2", 520, 425, "SUBTYPE_OF")
lab("l_st3", 592, 380, "SUBTYPE_OF")

# HAS_COMPONENT: part-solid -> solid component. The drop is only 50px, so the
# plate sits BESIDE the arrow; centred on it, it would cover the whole shaft.
edge("e_hc", "s2", "bottom", "sc", "top")
lab("l_hc", 625, 605, "HAS_COMPONENT")

# HAS_DATA_ELEMENT x5 and HAS_MEASUREMENT x2: one fan out of the centre node's
# right edge into the right column, across a 205px corridor.
for i in range(5):
    edge(f"e_de{i}", "fc", "right", f"de{i}", "left", s_frac=0.10 + i * 0.15)
    lab(f"l_de{i}", 742, 226 + i * 39, "HAS_DATA_ELEMENT")
edge("e_ms0", "fc", "right", "ms0", "left", s_frac=0.85)
edge("e_ms1", "fc", "right", "ms1", "left", s_frac=0.95)
lab("l_ms0", 727, 421, "HAS_MEASUREMENT")
lab("l_ms1", 732, 460, "HAS_MEASUREMENT")

# SCOPED_TO -> lung. It leaves the centre node BELOW where the neoplasm's
# manifestation arrow arrives, so the two do not cross.
edge("e_sc", "fc", "left", "an", "right", s_frac=0.875, d_frac=0.50)
lab("l_sc", 300, 330, "SCOPED_TO")

# IN_SUBSPECIALTY -> chest radiology
edge("e_sp", "fc", "bottom", "sp", "right", s_frac=0.05, d_frac=0.50)
lab("l_sp", 311, 375, "IN_SUBSPECIALTY")

# SEEN_ON x3 -> the three modality boxes, a fan off the centre node's bottom
# edge that passes to the right of lung and of the subspecialty box.
for i, (mid_, t) in enumerate([("md_ct", 0.42), ("md_xr", 0.50), ("md_mr", 0.68)]):
    edge(f"e_sn{i}", "fc", "bottom", mid_, "right", s_frac=0.10 + i * 0.08, d_frac=0.50)
    a = find(f"e_sn{i}")
    x1, y1 = a["x"], a["y"]
    x2, y2 = x1 + a["points"][-1][0], y1 + a["points"][-1][1]
    lab(f"l_sn{i}", x1 + t * (x2 - x1), y1 + t * (y2 - y1), "SEEN_ON")

for _id, _cx, _cy, _nm in LABELS:
    plate(_id, _cx, _cy, _nm, LW[_nm])

# ================================================================== legend
LEG_Y, LEG_X0, LEG_X1 = 735, 15, 1035
lg = base("rectangle", "leg", LEG_X0, LEG_Y, LEG_X1 - LEG_X0, 52, "#e2e8f0", "#f8fafc", sw=1)
lg["roundness"] = {"type": 3}
els.append(lg)

# widths measured at 11px; the nine entries need the smaller size to sit in one row
LEGEND = [("FindingClass", FINDING, 63.6, False), ("Grouping", GROUPING, 45.3, True),
          ("Diagnosis", DIAGNOSIS, 48.3, False), ("AssessmentScheme", ASSESS, 100.3, False),
          ("AnatomicLocation", ANATOMY, 87.4, False), ("Modality", GREY, 41.0, False),
          ("DataElement", DATAEL, 63.6, False), ("Measurement", MEAS, 67.3, False),
          ("Subspecialty", SUBSPEC, 62.4, False)]
lx = 32
for i, (name, pal, wpx, dashed) in enumerate(LEGEND):
    fill, stroke, _t, _m = pal
    if name == "AssessmentScheme":
        els.append(base("ellipse", f"lg{i}", lx - 1, LEG_Y + 17, 26, 18, stroke, fill, sw=1))
        sw_w = 26
    else:
        s = base("rectangle", f"lg{i}", lx, LEG_Y + 18, 22, 16, stroke, fill, sw=1, dashed=dashed)
        s["roundness"] = {"type": 3}
        els.append(s)
        sw_w = 22
    els.append(text(f"lg{i}_t", lx + sw_w + 8, LEG_Y + 19, name, size=11, color=BODY, w=wpx))
    lx += sw_w + 8 + wpx + 16

# caption under the legend (Excalidraw has no italic variant; small and grey instead)
els.append(text("cap", (LEG_X0 + LEG_X1) / 2 - 300, LEG_Y + 64,
                "illustrative: reflects pending updates to the CDE graph",
                size=11, color=CAPTION, align="center", w=600))

save("knowledge/drafts/nodule-neighborhood.excalidraw")
