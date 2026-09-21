#!/usr/bin/env python3
"""Build the data-structure ladder: Observation, Exam Finding List, Imaging
Problem List, Imaging Persona, with the fields each carries and its status.
Output: knowledge/data-structures/hierarchy.excalidraw"""
from excalib import PRIMARY, SECONDARY, TERTIARY, EXTERNAL, PLANNED, TITLE, SUBTITLE, BODY, LINE, els, base, text, box, find, arrow, hline, save

W, H, GAP = 280, 74, 150
Y = 130
cols = [60 + i * (W + GAP) for i in range(4)]

els.append(text("title", 60, 40, "From one observation to a patient's imaging history", size=26, color=TITLE))
els.append(text("subtitle", 60, 82, "Each structure to the right contains the ones to its left and adds one more level of context.", size=14, color=BODY))

box("obs", cols[0], Y, W, H, "Observation\none finding, one exam", PRIMARY)
box("efl", cols[1], Y, W, H, "Exam Finding List\nevery observation of one exam", PRIMARY)
box("ipl", cols[2], Y, W, H, "Imaging Problem List\none patient, keyed by finding", PRIMARY)
box("persona", cols[3], Y, W, H, "Imaging Persona\nplus clinical context", PLANNED, dashed=True)

arrow("a1", "obs", "right", "efl", "left", "per exam", label_dy=-26)
arrow("a2", "efl", "right", "ipl", "left", "all exams", label_dy=-26)
arrow("a3", "ipl", "right", "persona", "left", "with context", dashed=True, label_dy=-26)

fields = [
    "findingCode (OIFM)\nfindingDescription\nanatomicLocation (RID)\nattributes[] with value codes\nreportText",
    "diagnosticReportId\npatientInfo\nexamInfo with LOINC exam code\nfindings[]: the observations",
    "patient\nfindings[] keyed by\n(findingCode, locationId)\neach with dated observations[]\nstatus derived, not stored",
    "clinical context (orders, indications)\nmedical baseline (problems, labs)\nspecialized history (oncology)\nsurgical history (operative, implants)",
]
status = ["JSON in use; no published schema", "JSON in use; no published schema", "JSON in use; grouping changed on dev", "concept only, no artifact"]
for i, (f, st) in enumerate(zip(fields, status)):
    x = cols[i]
    ln = base("line", f"tick{i}", x + 18, Y + H, 0, 22, LINE, "transparent", sw=1)
    ln.update({"points": [[0, 0], [0, 22]], "boundElements": None})
    els.append(ln)
    els.append(text(f"fields{i}", x + 10, Y + H + 30, f, size=13, color="#374151"))
    els.append(text(f"status{i}", x + 10, Y + H + 30 + 5 * 13 * 1.25 + 8, st, size=12, color=SUBTITLE if i < 3 else PLANNED[2]))

els.append(text("note", 60, Y + H + 200, "Codes come from the semantic foundation: OIFM and OIFMA identifiers from finding models, RID from anatomic locations, LOINC for the exam.", size=13, color=BODY))
save("knowledge/data-structures/hierarchy.excalidraw")
