#!/usr/bin/env python3
"""Build the data-structure ladder: Observation, Exam Finding List, Imaging
Problem List, Imaging Persona, with the fields each carries and its status.
Recomposed as a vertical ladder (Observation on top, Imaging Persona at the
bottom) with each box's field list set to its right, to fit a ~900px column.
Title/subtitle are left for the page text.
Output: knowledge/data-structures/hierarchy.excalidraw"""
from excalib import PRIMARY, SECONDARY, TERTIARY, EXTERNAL, PLANNED, TITLE, SUBTITLE, BODY, LINE, els, base, text, box, find, arrow, hline, save

BOX_X = 0
BOX_W, BOX_H = 250, 70
TICK_W = 30                          # short connector from box's right edge to its field list
FIELD_X = BOX_X + BOX_W + TICK_W
ARROW_GAP = 74                        # vertical space between one box's bottom and the next box's top
FIELD_SIZE, STATUS_SIZE = 14, 13
CONTENT_W = FIELD_X + 460             # keeps field-list lines within this width

rows = [
    ("obs", "Observation\none finding, one exam", PRIMARY, False,
     ["findingCode (OIFM)", "findingDescription", "anatomicLocation (RID)", "attributes[] with value codes", "reportText"],
     "JSON in use; no published schema", SUBTITLE),
    ("efl", "Exam Finding List\nevery observation of one exam", PRIMARY, False,
     ["diagnosticReportId", "patientInfo", "examInfo with LOINC exam code", "findings[]: the observations"],
     "JSON in use; no published schema", SUBTITLE),
    ("ipl", "Imaging Problem List\none patient, keyed by finding", PRIMARY, False,
     ["patient", "findings[] keyed by", "(findingCode, locationId)", "each with dated observations[]", "status derived, not stored"],
     "JSON in use; grouping changed on dev", SUBTITLE),
    ("persona", "Imaging Persona\nplus clinical context", PLANNED, True,
     ["clinical context (orders, indications)", "medical baseline (problems, labs)", "specialized history (oncology)", "surgical history (operative, implants)"],
     "concept only, no artifact", PLANNED[2]),
]
arrow_labels = ["per exam", "all exams", "with context"]

y = 40
prev_id = None
for i, (bid, label, colors, dashed, fields, status, status_color) in enumerate(rows):
    box(bid, BOX_X, y, BOX_W, BOX_H, label, colors, dashed=dashed)

    field_h = len(fields) * FIELD_SIZE * 1.25
    fld_text = "\n".join(fields)
    els.append(text(f"{bid}_fields", FIELD_X, y, fld_text, size=FIELD_SIZE, color="#374151"))
    els.append(text(f"{bid}_status", FIELD_X, y + field_h + 8, status, size=STATUS_SIZE, color=status_color))
    tick = base("line", f"{bid}_tick", BOX_X + BOX_W, y + BOX_H / 2, TICK_W, 0, LINE, "transparent", sw=1)
    tick.update({"points": [[0, 0], [TICK_W, 0]], "boundElements": None})
    els.append(tick)

    content_h = max(BOX_H, field_h + 8 + STATUS_SIZE * 1.25)
    if prev_id is not None:
        arrow(f"a_{prev_id}_{bid}", prev_id, "bottom", bid, "top", arrow_labels[i - 1],
              label_dx=BOX_W / 2 + 14, label_dy=-12, dashed=dashed)
    prev_id, y = bid, y + content_h + ARROW_GAP

Y_NOTE = y - ARROW_GAP + 40
els.append(text("note", 0, Y_NOTE, "Codes come from the semantic foundation: OIFM and OIFMA identifiers from finding\nmodels, RID from anatomic locations, LOINC for the exam.", size=13, color=BODY))

save("knowledge/data-structures/hierarchy.excalidraw")
