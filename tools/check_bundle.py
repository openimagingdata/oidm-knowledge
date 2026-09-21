#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""House-rules checker for the oidm-knowledge OKF bundle.

Runs alongside the OKF conformance validator (okf_validate.py) and enforces the
stricter conventions this repository adopted from the ACR-RSNA-CDEs
`next-gen-2026` bundle checker: controlled `type` vocabulary, index coverage,
link resolution, markdown sanity, trust-signal hygiene, and a leak sweep.

Run from the repo root:  uv run tools/check_bundle.py [--bundle knowledge]
Exit status is non-zero on any ERROR; warnings do not fail the run.
"""
from __future__ import annotations

import argparse
import datetime as dt
import glob
import os
import re
import subprocess
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

ALLOWED_TYPES = {
    # inherited from ACR-RSNA-CDEs next-gen-2026
    "Reference", "Analysis", "Decision Record", "Proposal", "Playbook", "Worked Example",
    "Presentation Extract", "Meeting Notes", "Draft Specification", "Gap Log", "Exploration",
    # added for this bundle
    "Overview", "Concept", "Glossary Term", "Format Specification", "Data Structure",
    "Project Profile", "Guide", "Roadmap", "History", "Source Extract", "Plan",
}
ALLOWED_STATUS = {"draft", "stable", "deprecated"}
RESERVED = {"index.md", "log.md"}
ACTOR = re.compile(r"^(human:[^\s/]+|process:[^\s/]+|[^\s/]+/[^\s]+)$")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def frontmatter(text: str) -> str | None:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else None


try:
    import yaml as _yaml  # type: ignore
except ImportError:  # structural fallback, top-level keys only
    _yaml = None


def parse_fm(s: str) -> dict:
    if _yaml is not None:
        data = _yaml.safe_load(s)
        return data if isinstance(data, dict) else {}
    warn("PyYAML not installed; nested frontmatter checks are skipped (run with `uv run`)")
    d: dict = {}
    for line in s.split("\n"):
        if line.count('"') % 2 or line.count("{") != line.count("}") or line.count("[") != line.count("]"):
            raise ValueError(f"unbalanced: {line!r}")
        m = re.match(r"^([A-Za-z_]\w*):\s*(.*)$", line)
        if m:
            d[m.group(1)] = m.group(2)
    return d


def strip_fences(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def actor_ok(value: object) -> bool:
    return isinstance(value, str) and bool(ACTOR.match(value))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundle", default="knowledge", help="bundle directory relative to repo root")
    ap.add_argument("--denylist", default="tools/denylist.txt", help="gitignored file, one term per line")
    args = ap.parse_args()

    bundle = os.path.join(REPO, args.bundle)
    if not os.path.isdir(bundle):
        print(f"ERROR bundle directory not found: {bundle}")
        return 1

    md_files = sorted(
        os.path.relpath(p, bundle)
        for p in glob.glob(os.path.join(bundle, "**", "*.md"), recursive=True)
    )
    concepts = [f for f in md_files if os.path.basename(f) not in RESERVED]
    indexes = [f for f in md_files if os.path.basename(f) == "index.md"]
    logs = [f for f in md_files if os.path.basename(f) == "log.md"]
    descs: dict[str, str] = {}
    today = dt.date.today()

    # 1. frontmatter and trust signals
    for f in md_files:
        text = read(os.path.join(bundle, f))
        fm = frontmatter(text)
        if f in logs:
            if fm is not None:
                err(f"{f}: log.md must not carry frontmatter (OKF §9)")
            if not re.search(r"^## \d{4}-\d{2}-\d{2}", text, re.M):
                err(f"{f}: log.md needs date headings (## YYYY-MM-DD)")
            continue
        if f in indexes:
            if f == "index.md":
                if fm is None:
                    err("index.md: bundle-root index should declare okf_version")
                else:
                    try:
                        keys = set(parse_fm(fm))
                    except Exception as e:  # noqa: BLE001
                        err(f"index.md: frontmatter unparseable: {e}")
                        keys = set()
                    if keys - {"okf_version"}:
                        err(f"index.md: root index frontmatter may contain only okf_version, has {sorted(keys)}")
            elif fm is not None:
                err(f"{f}: non-root index.md must not carry frontmatter (OKF §8)")
            continue
        if fm is None:
            err(f"{f}: missing frontmatter")
            continue
        try:
            data = parse_fm(fm)
        except Exception as e:  # noqa: BLE001
            err(f"{f}: frontmatter unparseable: {e}")
            continue
        t = data.get("type")
        if not t:
            err(f"{f}: frontmatter has no `type`")
        elif t not in ALLOWED_TYPES:
            err(f"{f}: type {t!r} is not in the controlled vocabulary (see guides/authoring-guide.md)")
        for k in ("title", "description"):
            if not data.get(k):
                err(f"{f}: frontmatter lacks `{k}`")
        descs[f] = str(data.get("description", "")).strip().strip('"')
        status = data.get("status", "stable")
        if status not in ALLOWED_STATUS:
            err(f"{f}: status {status!r} is not draft|stable|deprecated")
        gen = data.get("generated")
        if not isinstance(gen, dict) or not gen.get("by") or not gen.get("at"):
            err(f"{f}: `generated: {{by, at}}` is required on every concept document")
        elif not actor_ok(gen.get("by")):
            err(f"{f}: generated.by {gen.get('by')!r} does not follow the actor convention (OKF §7)")
        ver = data.get("verified")
        if ver is not None:
            entries = ver if isinstance(ver, list) else [ver]
            for v in entries:
                if not isinstance(v, dict) or not actor_ok(v.get("by")) or not v.get("at"):
                    err(f"{f}: malformed `verified` entry {v!r}")
            human = any(isinstance(v, dict) and str(v.get("by", "")).startswith("human:") for v in entries)
            if human and status == "draft":
                warn(f"{f}: human-verified but still status: draft")
        elif status == "stable":
            warn(f"{f}: status stable without any `verified` entry")
        sa = data.get("stale_after")
        if sa is not None:
            try:
                d = sa if isinstance(sa, dt.date) else dt.date.fromisoformat(str(sa))
                if d <= today:
                    warn(f"{f}: stale_after {d} has passed")
            except ValueError:
                err(f"{f}: stale_after {sa!r} is not an ISO date")
        if "timestamp" in data:
            warn(f"{f}: legacy v0.1 `timestamp` present; use generated.at")
        srcs = data.get("sources")
        if srcs is not None:
            if not isinstance(srcs, list):
                err(f"{f}: `sources` must be a list")
            else:
                for s in srcs:
                    if not isinstance(s, dict) or not s.get("resource"):
                        err(f"{f}: a `sources` entry has no `resource`")
                    elif not s.get("id"):
                        warn(f"{f}: a `sources` entry has no `id` (needed for footnote citations)")

    # 2. headings and fences
    for f in md_files:
        text = read(os.path.join(bundle, f))
        if text.count("```") % 2:
            err(f"{f}: unbalanced ``` code fence")
        body = strip_fences(text)
        for _ in re.finditer(r"^(#+)\s*$", body, re.M):
            err(f"{f}: empty heading")

    # 3. links
    for f in md_files:
        body = strip_fences(read(os.path.join(bundle, f)))
        for m in re.finditer(r"\]\(([^)]+)\)", body):
            tgt = m.group(1).strip().split(" ")[0]
            if re.match(r"^(https?:|mailto:|#)", tgt):
                continue
            path = tgt.split("#")[0]
            if not path:
                continue
            if path.startswith("/"):
                resolved = os.path.normpath(os.path.join(bundle, path.lstrip("/")))
            else:
                resolved = os.path.normpath(os.path.join(bundle, os.path.dirname(f), path))
            if not os.path.exists(resolved):
                err(f"{f}: broken link -> {tgt}")

    # 4. index coverage: every directory has an index listing its concepts and subdirectories
    dirs = sorted({os.path.dirname(f) for f in md_files})
    for d in dirs:
        idx = os.path.join(d, "index.md") if d else "index.md"
        if idx not in indexes:
            err(f"{d or '.'}: directory has no index.md")
            continue
        text = read(os.path.join(bundle, idx))
        listed: dict[str, tuple[str, str]] = {}
        for m in re.finditer(r"^\*\s+\[([^\]]+)\]\(([^)]+)\)\s*-\s*(.*)$", text, re.M):
            target = m.group(2)
            key = os.path.normpath(os.path.join(d, target)) if not target.startswith("/") else os.path.normpath(target.lstrip("/"))
            listed[key] = (m.group(1), m.group(3).strip())
        for p, (title, _) in listed.items():
            if not os.path.exists(os.path.join(bundle, p)):
                err(f"{idx}: entry '{title}' points at missing {p}")
        for c in concepts:
            if os.path.dirname(c) == d and os.path.normpath(c) not in listed:
                err(f"{idx}: concept {os.path.basename(c)} is not listed")
        for sub in dirs:
            if sub and os.path.dirname(sub) == d and os.path.normpath(sub) not in listed:
                err(f"{idx}: subdirectory {os.path.basename(sub)}/ is not listed")
        for p, (_, desc) in listed.items():
            if p in descs and desc and descs[p] and desc != descs[p]:
                warn(f"{idx}: description for {os.path.basename(p)} differs from its frontmatter")

    # 5. leak sweep (emails, denylisted terms) across the bundle and root docs
    deny_path = os.path.join(REPO, args.denylist)
    deny = []
    if os.path.exists(deny_path):
        deny = [l.strip() for l in read(deny_path).splitlines() if l.strip() and not l.startswith("#")]
    else:
        warn(f"no {args.denylist} — name sweep skipped (emails still checked)")
    sweep = [os.path.join(bundle, f) for f in md_files]
    sweep += [os.path.join(REPO, x) for x in ("README.md", "CONTRIBUTING.md", "CHANGELOG.md", "DEV_LOG.md") if os.path.exists(os.path.join(REPO, x))]
    for p in sweep:
        text = read(p)
        rel = os.path.relpath(p, REPO)
        for m in EMAIL.finditer(text):
            if m.group(0).endswith("@anthropic.com"):
                continue
            err(f"{rel}: email address present: {m.group(0)}")
        low = text.lower()
        for term in deny:
            if term.lower() in low:
                err(f"{rel}: denylisted term present: {term!r}")
    tracked = subprocess.run(["git", "ls-files", args.denylist], capture_output=True, text=True, cwd=REPO).stdout.strip()
    if tracked:
        err(f"{args.denylist} is tracked by git; it must stay ignored")

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(md_files)} documents · {len(concepts)} concepts · {len(errors)} errors · {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
