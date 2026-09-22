#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Mark bundle documents as verified by a human, or report review status.

  uv run tools/verify.py knowledge/glossary/oifm.md [more paths...]   mark verified
  uv run tools/verify.py --by human:someone knowledge/...             different reviewer
  uv run tools/verify.py --status                                     counts per directory
  uv run tools/verify.py --list knowledge/glossary                    draft documents under a directory

Marking adds a `verified` entry with the current UTC time, sets `status: stable`,
and leaves everything else in the frontmatter untouched (text edit, not a YAML
round-trip, so key order and quoting survive).
"""
from __future__ import annotations

import argparse
import datetime as dt
import glob
import os
import re
import sys

import yaml

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)


def load(path: str) -> tuple[str, dict, str]:
    text = open(path, encoding="utf-8").read()
    m = FM.match(text)
    if not m:
        raise SystemExit(f"{path}: no frontmatter")
    return text, yaml.safe_load(m.group(1)) or {}, m.group(1)


def mark(path: str, by: str) -> None:
    text, data, fm = load(path)
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    entry = f"  - {{ by: {by}, at: {now} }}"
    if "verified" in data:
        # append to an existing list (normalize a single mapping to a list)
        if isinstance(data["verified"], dict):
            fm = re.sub(r"^verified:.*$", f"verified:\n  - {{ by: {data['verified']['by']}, at: {data['verified']['at']} }}\n{entry}", fm, count=1, flags=re.M)
        else:
            fm = re.sub(r"^(verified:\n(?:  - .*\n?)*)", lambda m: m.group(1).rstrip("\n") + "\n" + entry + "\n", fm, count=1, flags=re.M)
    else:
        # insert after generated, else at the end
        if re.search(r"^generated:.*$", fm, flags=re.M):
            fm = re.sub(r"^(generated:.*)$", r"\1\nverified:\n" + entry, fm, count=1, flags=re.M)
        else:
            fm = fm.rstrip("\n") + "\nverified:\n" + entry
    if re.search(r"^status:.*$", fm, flags=re.M):
        fm = re.sub(r"^status:.*$", "status: stable", fm, count=1, flags=re.M)
    else:
        fm += "\nstatus: stable"
    head = FM.match(text)
    assert head is not None
    new = "---\n" + fm + "\n---\n" + text[head.end():]
    open(path, "w", encoding="utf-8").write(new)
    print(f"verified {os.path.relpath(path, REPO)} by {by} at {now}")


def concepts(root: str) -> list[str]:
    out = []
    for p in sorted(glob.glob(os.path.join(root, "**", "*.md"), recursive=True)):
        if os.path.basename(p) in ("index.md", "log.md"):
            continue
        out.append(p)
    return out


def status_report(bundle: str) -> None:
    rows: dict[str, list[int]] = {}
    for p in concepts(bundle):
        _, data, _ = load(p)
        d = os.path.relpath(os.path.dirname(p), bundle)
        d = d.split(os.sep)[0] if d != "." else "."
        row = rows.setdefault(d, [0, 0])
        row[1] += 1
        if data.get("status", "stable") == "stable" and data.get("verified"):
            row[0] += 1
    total_v = sum(r[0] for r in rows.values()); total = sum(r[1] for r in rows.values())
    print(f"{'directory':28} verified / total")
    for d, (v, n) in sorted(rows.items()):
        print(f"{d:28} {v:3} / {n}")
    print(f"{'all':28} {total_v:3} / {total}")


def list_drafts(root: str) -> None:
    for p in concepts(root):
        _, data, _ = load(p)
        if not data.get("verified"):
            print(os.path.relpath(p, REPO))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--by", default="human:talkasab")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--list", metavar="DIR")
    a = ap.parse_args()
    if a.status:
        status_report(os.path.join(REPO, "knowledge")); return 0
    if a.list:
        list_drafts(os.path.join(REPO, a.list)); return 0
    if not a.paths:
        ap.print_help(); return 2
    for p in a.paths:
        mark(os.path.join(REPO, p) if not os.path.isabs(p) else p, a.by)
    return 0


if __name__ == "__main__":
    sys.exit(main())
