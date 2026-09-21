"""Shared helpers for building Excalidraw diagrams as JSON (used by build_*.py)."""
from __future__ import annotations

import json
import os

# Palette (tools/diagrams follows the excalidraw-diagram skill palette)
PRIMARY = ("#3b82f6", "#1e3a5f", "#ffffff")      # data structures: fill, stroke, text
SECONDARY = ("#60a5fa", "#1e3a5f", "#1e3a5f")    # applications
TERTIARY = ("#93c5fd", "#1e3a5f", "#1e3a5f")     # semantic foundation
EXTERNAL = ("#fed7aa", "#c2410c", "#7c2d12")     # allied external project
PLANNED = ("#ffffff", "#64748b", "#475569")      # dashed, documented or planned only
TITLE, SUBTITLE, BODY, LINE = "#1e40af", "#3b82f6", "#64748b", "#64748b"

els: list[dict] = []
_seed = 1000


def reset() -> None:
    global _seed
    els.clear()
    _seed = 1000


def seed() -> int:
    global _seed
    _seed += 1
    return _seed


def base(kind: str, id_: str, x: float, y: float, w: float, h: float, stroke: str, fill: str, dashed=False, sw=2) -> dict:
    return {
        "type": kind, "id": id_, "x": x, "y": y, "width": w, "height": h,
        "strokeColor": stroke, "backgroundColor": fill, "fillStyle": "solid",
        "strokeWidth": sw, "strokeStyle": "dashed" if dashed else "solid", "roughness": 0,
        "opacity": 100, "angle": 0, "seed": seed(), "version": 1, "versionNonce": seed(),
        "isDeleted": False, "groupIds": [], "boundElements": [], "link": None, "locked": False,
    }


def text(id_: str, x: float, y: float, s: str, size=16, color=BODY, align="left", w: float | None = None, container: str | None = None, font=2) -> dict:
    lines = s.split("\n")
    est_w = w if w is not None else max(len(l) for l in lines) * size * 0.58
    h = len(lines) * size * 1.25
    t = base("text", id_, x, y, est_w, h, color, "transparent", sw=1)
    t.update({"text": s, "originalText": s, "fontSize": size, "fontFamily": font, "textAlign": align,
              "verticalAlign": "middle" if container else "top", "containerId": container, "lineHeight": 1.25,
              "boundElements": None})
    return t


def box(id_: str, x: float, y: float, w: float, h: float, label: str, colors, dashed=False, size=16) -> dict:
    fill, stroke, tcolor = colors
    r = base("rectangle", id_, x, y, w, h, stroke, fill, dashed=dashed)
    r["roundness"] = {"type": 3}
    t = text(id_ + "_t", x + 10, y + 10, label, size=size, color=tcolor, align="center", w=w - 20, container=id_)
    t["height"] = h - 20
    r["boundElements"] = [{"id": t["id"], "type": "text"}]
    els.extend([r, t])
    return r


def find(id_: str) -> dict:
    return next(e for e in els if e["id"] == id_)


def edge_point(b: dict, side: str, frac: float = 0.5) -> tuple[float, float]:
    x, y, w, h = b["x"], b["y"], b["width"], b["height"]
    return {"top": (x + w * frac, y), "bottom": (x + w * frac, y + h),
            "left": (x, y + h * frac), "right": (x + w, y + h * frac)}[side]


def arrow(id_: str, src: str, s_side: str, dst: str, d_side: str, label: str | None = None, s_frac=0.5, d_frac=0.5,
          color=LINE, dashed=False, label_dx=0.0, label_dy=-22.0, sw=2, both=False, elbow: str | None = None) -> None:
    a, b = find(src), find(dst)
    (x1, y1), (x2, y2) = edge_point(a, s_side, s_frac), edge_point(b, d_side, d_frac)
    ar = base("arrow", id_, x1, y1, x2 - x1, y2 - y1, color, "transparent", dashed=dashed, sw=sw)
    pts = [[0, 0], [x2 - x1, y2 - y1]]
    if elbow == "vertical-first":
        pts = [[0, 0], [0, y2 - y1], [x2 - x1, y2 - y1]]
    elif elbow == "horizontal-first":
        pts = [[0, 0], [x2 - x1, 0], [x2 - x1, y2 - y1]]
    ar.update({"points": pts,
               "startBinding": {"elementId": src, "focus": 0, "gap": 2},
               "endBinding": {"elementId": dst, "focus": 0, "gap": 2},
               "startArrowhead": "arrow" if both else None, "endArrowhead": "arrow", "boundElements": None})
    a["boundElements"].append({"id": id_, "type": "arrow"})
    b["boundElements"].append({"id": id_, "type": "arrow"})
    els.append(ar)
    if label:
        mx, my = (x1 + x2) / 2 + label_dx, (y1 + y2) / 2 + label_dy
        lw = len(label) * 12 * 0.58
        els.append(text(id_ + "_l", mx - lw / 2, my, label, size=12, color=BODY, align="center", w=lw))


def hline(id_: str, x: float, y: float, w: float, dashed=True) -> None:
    ln = base("line", id_, x, y, w, 0, LINE, "transparent", dashed=dashed, sw=1)
    ln.update({"points": [[0, 0], [w, 0]], "boundElements": None})
    els.append(ln)




def save(rel_path: str) -> str:
    out = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", rel_path))
    doc = {"type": "excalidraw", "version": 2, "source": "oidm-knowledge/tools/diagrams",
           "elements": els, "appState": {"viewBackgroundColor": "#ffffff", "gridSize": None}, "files": {}}
    with open(out, "w") as fh:
        json.dump(doc, fh, indent=1)
    print("wrote", out, len(els), "elements")
    return out
