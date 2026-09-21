#!/usr/bin/env python3
"""Stage the OKF bundle for the site build.

Copies `knowledge/` to a staging directory and rewrites every internal markdown
link to the bundle-absolute form (`/dir/file.md`). The bundle itself uses two
link styles the OKF spec allows: bundle-absolute links in concept documents and
`./file.md` links in directory indexes. Quartz resolves either style correctly
on its own but not both at once, so the site builds from this normalized copy.
The bundle in git is untouched.

Usage:  python3 tools/prepare_site_content.py [--src knowledge] [--dest site/staged-content]
"""
from __future__ import annotations

import argparse
import os
import re
import shutil

LINK = re.compile(r"(\]\()(?!(?:https?:|mailto:|#|/))([^)\s]+)(\s+\"[^\"]*\")?(\))")
FENCE = re.compile(r"```.*?```", re.S)


def rewrite(text: str, rel_dir: str) -> str:
    # Leave fenced code untouched by splitting on fences.
    parts, last, out = [], 0, []
    for m in FENCE.finditer(text):
        parts.append((text[last:m.start()], False))
        parts.append((m.group(0), True))
        last = m.end()
    parts.append((text[last:], False))
    for chunk, is_fence in parts:
        if is_fence:
            out.append(chunk)
            continue

        def sub(m: re.Match) -> str:
            target = m.group(2)
            path, _, frag = target.partition("#")
            resolved = os.path.normpath(os.path.join(rel_dir, path)) if path else ""
            if resolved in (".", ""):
                resolved = ""
            new = "/" + resolved.replace(os.sep, "/")
            if path.endswith("/") and not new.endswith("/"):
                new += "/"
            if frag:
                new += "#" + frag
            return f"{m.group(1)}{new}{m.group(3) or ''}{m.group(4)}"

        out.append(LINK.sub(sub, chunk))
    return "".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="knowledge")
    ap.add_argument("--dest", default="site/staged-content")
    args = ap.parse_args()
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    src, dest = os.path.join(root, args.src), os.path.join(root, args.dest)
    if os.path.isdir(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)
    n = 0
    for dirpath, _, files in os.walk(dest):
        for name in files:
            if not name.endswith(".md"):
                continue
            p = os.path.join(dirpath, name)
            rel_dir = os.path.relpath(dirpath, dest)
            rel_dir = "" if rel_dir == "." else rel_dir
            with open(p, encoding="utf-8") as fh:
                text = fh.read()
            new = rewrite(text, rel_dir)
            if new != text:
                with open(p, "w", encoding="utf-8") as fh:
                    fh.write(new)
                n += 1
    print(f"staged {args.src} -> {args.dest}; rewrote links in {n} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
