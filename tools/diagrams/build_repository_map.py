#!/usr/bin/env python3
"""Build the repository data-flow map: one row per theme so the main flows run
left to right (terminology, content, library, application).
Output: knowledge/repositories/repository-map.excalidraw"""
from excalib import PRIMARY, SECONDARY, TERTIARY, EXTERNAL, PLANNED, TITLE, SUBTITLE, BODY, LINE, els, base, text, box, find, arrow, save

W, H = 250, 60
C = [60, 420, 780, 1140]          # columns, 110px gutters
R = [150, 240, 330, 420]          # rows

els.append(text("title", 60, 40, "How the repositories relate", size=26, color=TITLE))
els.append(text("subtitle", 60, 78, "Read each row left to right: a terminology feeds content, a library packages it, an application uses it.", size=14, color=BODY))
for lbl, x in (("TERMINOLOGIES", C[0]), ("CONTENT", C[1]), ("LIBRARIES", C[2]), ("APPLICATIONS", C[3])):
    els.append(text("hdr_" + lbl.lower(), x, 100, lbl, size=13, color=SUBTITLE))

# row 1: finding models
box("radelement", C[0], R[0], W, H, "RadElement (ACR/RSNA)\nRDES and RDE codes", EXTERNAL, size=14)
box("fms", C[1], R[0], W, H, "findingmodels\n2,382 finding models", TERTIARY, size=14)
box("fm", C[2], R[0], W, H, "findingmodel\nOIFM format, index, CLIs, MCP", SECONDARY, size=14)
box("forge", C[3], R[0], W, H, "Finding Model Forge\nfmf.oidm.org", PRIMARY, size=14)
# row 2: CDE staging and the catalog site
box("cdesnap", C[0], R[1], W, H, "common_data_elements\nRadElement snapshot", TERTIARY, size=14)
box("cdes", C[1], R[1], W, H, "CDEStaging\n259 draft CDE definitions", TERTIARY, size=14)
box("site", C[3], R[1], W, H, "finding-models-site\ncatalog of findingmodels", PRIMARY, size=14)
# row 3: anatomy
box("radlex", C[0], R[2], W, H, "RadLex (RSNA)\nRID codes", EXTERNAL, size=14)
box("alorg", C[1], R[2], W, H, "anatomiclocations.org\n+ BodyPartIndex.py and .ts", TERTIARY, size=14)
box("alpkg", C[2], R[2], W, H, "anatomic-locations package\ninside findingmodel", SECONDARY, size=14)
box("ipl", C[3], R[2], W, H, "imaging-problem-list\nuses finding models and locations", PRIMARY, size=14)
# row 4: terminology lookup
box("others", C[0], R[3], W, H, "SNOMED CT, FMA, LOINC, UMLS\n(and RadLex)", EXTERNAL, size=14)
box("molu", C[2], R[3], W, H, "med-ontology-lookup\nmolu", SECONDARY, size=14)
box("mvp", C[3], R[3], W, H, "IPL-MVP-ExtractionAndLabeling\nsuperseded", PLANNED, dashed=True, size=14)

# horizontal flows
arrow("f1", "radelement", "right", "fms", "left", "CDE-derived")
arrow("f2", "fms", "right", "fm", "left", "definitions")
arrow("f3", "fm", "right", "forge", "left", "engine", s_frac=0.35, d_frac=0.35)
arrow("f4", "radlex", "right", "alorg", "left", "curated subset")
arrow("f5", "alorg", "right", "alpkg", "left", "lineage", dashed=True)
arrow("f6", "alpkg", "right", "ipl", "left", None, s_frac=0.7, d_frac=0.7)
arrow("f7", "others", "right", "molu", "left", "lookups")
# vertical flows
arrow("f8", "radelement", "bottom", "cdesnap", "top", "snapshot", s_frac=0.5, d_frac=0.5, label_dx=42, label_dy=-8)
arrow("f9", "cdes", "top", "fms", "bottom", "content batches", s_frac=0.5, d_frac=0.5, label_dx=70, label_dy=-8)
arrow("f10", "cdes", "left", "radelement", "bottom", None, s_frac=0.5, d_frac=0.75, dashed=True)
els.append(text("f10_l", C[0] + W + 14, R[1] + H + 4, "informal path to submission", size=11, color=BODY))
els.append(text("f5_note", C[1] + 30, R[2] + H + 4, "current data lives in findingmodel", size=11, color=BODY))

# elbowed flows through empty gutters
def elbow(id_, src, dst, pts_abs, label, lx, ly, dashed=False):
    a, b = find(src), find(dst)
    x0, y0 = pts_abs[0]
    ar = base("arrow", id_, x0, y0, pts_abs[-1][0] - x0, pts_abs[-1][1] - y0, LINE, "transparent", dashed=dashed)
    ar.update({"points": [[x - x0, y - y0] for x, y in pts_abs],
               "startBinding": {"elementId": src, "focus": 0, "gap": 2}, "endBinding": {"elementId": dst, "focus": 0, "gap": 2},
               "startArrowhead": None, "endArrowhead": "arrow", "boundElements": None})
    a["boundElements"].append({"id": id_, "type": "arrow"}); b["boundElements"].append({"id": id_, "type": "arrow"})
    els.append(ar)
    if label:
        els.append(text(id_ + "_l", lx, ly, label, size=11, color=BODY))

# findingmodels -> finding-models-site: over the top of the libraries column
elbow("e1", "fms", "site", [(C[1] + W * 0.75, R[0]), (C[1] + W * 0.75, 138), (C[3] + W / 2, 138), (C[3] + W / 2, R[1])],
      "git submodule", C[1] + W + 14, 122)
# fix: the last leg must come down past row 1 into the site box top; run it in the gutter right of column 4 instead
find("e1")["points"] = [[0, 0], [0, 138 - R[0]], [C[3] + W + 30 - (C[1] + W * 0.75), 138 - R[0]],
                        [C[3] + W + 30 - (C[1] + W * 0.75), R[1] + H / 2 - R[0]], [C[3] + W - (C[1] + W * 0.75), R[1] + H / 2 - R[0]]]
# findingmodel -> imaging-problem-list: down the gutter between libraries and applications
elbow("e2", "fm", "ipl", [(C[2] + W, R[0] + H * 0.85), (C[2] + W + 70, R[0] + H * 0.85), (C[2] + W + 70, R[2] + H * 0.3), (C[3], R[2] + H * 0.3)],
      "", 0, 0)
# med-ontology-lookup -> findingmodel: up the same gutter, left of e2
elbow("e3", "molu", "fm", [(C[2] + W, R[3] + H * 0.5), (C[2] + W + 40, R[3] + H * 0.5), (C[2] + W + 40, R[0] + H + 15), (C[2] + W - 30, R[0] + H + 15), (C[2] + W - 30, R[0] + H)],
      "ontology search for enrichment", 0, 0, dashed=True)
lab = find("e3_l"); lw = len("ontology search for enrichment") * 11 * 0.58
cx, cy = C[2] + W + 40 - 12, (R[3] + H * 0.5 + R[0] + H + 15) / 2
lab.update({"x": cx - lw / 2, "y": cy - 7, "width": lw, "angle": -1.5708, "textAlign": "center"})

els.append(text("legend", 60, 520, "Orange: external terminology.  Light blue: content repository.  Mid blue: library.  Dark blue: application.  Dashed: lineage or superseded.", size=12, color=BODY))
save("knowledge/repositories/repository-map.excalidraw")
