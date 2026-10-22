#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Check public pages, local Markdown targets, navigation, and review stamps."""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml

SITE = Path(__file__).resolve().parents[1]
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", re.S)


def read_page(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        raise ValueError("missing frontmatter")
    data = yaml.safe_load(match[1])
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a mapping")
    return data, text[match.end():]


def is_verified(data: dict) -> bool:
    stamps = data.get("verified")
    if isinstance(stamps, dict):
        stamps = [stamps]
    return isinstance(stamps, list) and any(
        isinstance(stamp, dict) and stamp.get("by") and stamp.get("at")
        for stamp in stamps
    )


def prose_lines(body: str):
    """Ignore fenced code, preserving line numbers for useful diagnostics."""
    fence = None
    for number, line in enumerate(body.splitlines(), 1):
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
            continue
        if marker:
            fence = marker[1]
            if marker[2].strip().split(maxsplit=1)[:1] == ["mermaid"]:
                yield number, None
            continue
        # Inline code is not a Markdown link either.
        yield number, re.sub(r"(`+).*?\1", "", line)


def destination(text: str) -> str | None:
    """Read a Markdown destination, including angle brackets and balanced ()."""
    text = text.lstrip()
    if text.startswith("<"):
        end = text.find(">")
        return text[1:end] if end >= 0 else None
    depth = 0
    out = []
    escaped = False
    for char in text:
        if escaped:
            out.append(char)
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == "(":
            depth += 1
            out.append(char)
        elif char == ")":
            if depth == 0:
                break
            depth -= 1
            out.append(char)
        elif char.isspace() and depth == 0:
            break
        else:
            out.append(char)
    return "".join(out)


def link_targets(lines):
    # Keep line boundaries so destinations wrapped onto the next line work.
    text = "\n".join(line or "" for _, line in lines)
    for number, line in lines:
        if line is None:
            continue
        definition = re.match(r"^\s{0,3}\[([^\]^]+)\]:\s*(.*)$", line)
        if definition:
            # Check the shared destination once, at its definition.
            yield number, destination(definition[2])
    for match in re.finditer(r"(?<!\\)\]\(", text):
        number = lines[text.count("\n", 0, match.start())][0]
        yield number, destination(text[match.end():])


def navigation_pages(value, errors: list[str]):
    if not isinstance(value, list):
        errors.append("navigation.yaml: navigation must be a list")
        return
    for entry in value:
        if isinstance(entry, str):
            yield entry
        elif isinstance(entry, dict) and isinstance(entry.get("page"), str) and set(entry) <= {"page", "pages", "label"}:
            if "label" in entry and (not isinstance(entry["label"], str) or not entry["label"].strip()):
                errors.append(f"navigation.yaml: {entry['page']}: label must be a non-empty string")
            yield entry["page"]
            yield from navigation_pages(entry.get("pages", []), errors)
        else:
            errors.append(f"navigation.yaml: invalid entry {entry!r}")


def check_site(site: Path, target: str) -> list[str]:
    content = (site / "content").resolve()
    pages = sorted(content.rglob("*.md"))
    errors = []
    if not pages:
        errors.append("content/: no Markdown pages found")
    for page in pages:
        name = "content/" + page.relative_to(content).as_posix()
        try:
            data, body = read_page(page)
        except (ValueError, yaml.YAMLError, OSError) as error:
            errors.append(f"{name}: {str(error).splitlines()[0]}")
            continue
        for field in ("title", "description"):
            if not isinstance(data.get(field), str) or not data[field].strip():
                errors.append(f"{name}: missing non-empty {field}")
        if target == "production" and not is_verified(data):
            errors.append(f"{name}: missing verified entry for production")
        lines = list(prose_lines(body))
        for number, line in lines:
            if line is None:
                errors.append(f"{name}: Mermaid fence at body line {number}")
        for number, link in link_targets(lines):
            if not link or link.startswith("#"):
                continue
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            path = unquote(url.path)
            resolved = (content / path.lstrip("/") if path.startswith("/") else page.parent / path).resolve()
            if not resolved.is_relative_to(content) or not resolved.is_file():
                errors.append(f"{name}: broken local target {link!r} at body line {number}")
    try:
        navigation = yaml.safe_load((site / "navigation.yaml").read_text(encoding="utf-8"))
        listed = Counter(navigation_pages(navigation, errors))
        expected = {page.relative_to(content).as_posix() for page in pages}
        for path, count in sorted(listed.items()):
            if path not in expected:
                errors.append(f"navigation.yaml: {path}: page does not exist under content/")
            if count != 1:
                errors.append(f"navigation.yaml: {path}: listed {count} times")
        for path in sorted(expected - listed.keys()):
            errors.append(f"navigation.yaml: {path}: page is not listed")
    except (yaml.YAMLError, OSError) as error:
        errors.append(f"navigation.yaml: {str(error).splitlines()[0]}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", choices=("dev", "staging", "production"), default="dev")
    args = parser.parse_args()
    errors = check_site(SITE, args.target)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Site check passed ({args.target}, {len(list((SITE / 'content').rglob('*.md')))} pages)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
