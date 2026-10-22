#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Write review stamps for site/content/ pages without rewriting other fields."""
from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path
import sys

import yaml

from check_site import FRONTMATTER, is_verified, read_page

CONTENT = Path(__file__).resolve().parents[1] / "content"
REPO = CONTENT.parents[1]


def scoped_path(value: str, *, directory: bool = False) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = REPO / path
    path = path.resolve()
    if not path.is_relative_to(CONTENT.resolve()):
        raise ValueError(f"{value}: must be under site/content/")
    if directory:
        if not path.is_dir():
            raise ValueError(f"{value}: not a directory")
    elif path.suffix != ".md" or not path.is_file():
        raise ValueError(f"{value}: not a Markdown page")
    return path


def field_span(frontmatter: str, key, value) -> tuple[int, int]:
    start = frontmatter.rfind("\n", 0, key.start_mark.index) + 1
    end = value.end_mark.index
    if value.end_mark.column:
        newline = frontmatter.find("\n", end)
        end = len(frontmatter) if newline < 0 else newline + 1
    # YAML block nodes can end at the next key, after intervening comments.
    # Keep those comments and blank lines outside the edited field.
    for line in reversed(frontmatter[start:end].splitlines(keepends=True)):
        if line.strip() and not line.lstrip().startswith("#"):
            break
        end -= len(line)
    return start, end


def marked_text(path: Path, by: str, now: str) -> str:
    data, _ = read_page(path)
    with path.open(encoding="utf-8", newline="") as source:
        text = source.read()
    match = FRONTMATTER.match(text)
    assert match
    newline = "\r\n" if text.startswith("---\r\n") else "\n"
    fm = match[1] + newline
    root = yaml.compose(fm)
    fields = {key.value: (key, value) for key, value in root.value}
    stamps = data.get("verified") or []
    if isinstance(stamps, dict):
        stamps = [stamps]
    if not isinstance(stamps, list) or any(not isinstance(stamp, dict) for stamp in stamps):
        raise ValueError(f"{path}: verified must be a mapping or a list of mappings")
    replacement = yaml.safe_dump(
        {"verified": [*stamps, {"by": by, "at": now}]},
        sort_keys=False, allow_unicode=True,
    ).replace("\n", newline)
    if "verified" in fields:
        start, end = field_span(fm, *fields["verified"])
        fm = fm[:start] + replacement + fm[end:]
    elif "description" in fields:
        _, end = field_span(fm, *fields["description"])
        fm = fm[:end] + replacement + fm[end:]
    else:
        raise ValueError(f"{path}: missing description")
    return text[:match.start(1)] + fm.removesuffix(newline) + text[match.end(1):]


def report_status() -> None:
    rows = {}
    for path in sorted(CONTENT.rglob("*.md")):
        data, _ = read_page(path)
        relative = path.relative_to(CONTENT)
        directory = relative.parts[0] if len(relative.parts) > 1 else "."
        row = rows.setdefault(directory, [0, 0])
        row[0] += int(is_verified(data))
        row[1] += 1
    print(f"{'directory':28} verified / total")
    for directory, (verified, total) in sorted(rows.items()):
        print(f"{directory:28} {verified:3} / {total}")
    print(f"{'all':28} {sum(row[0] for row in rows.values()):3} / {sum(row[1] for row in rows.values())}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*")
    parser.add_argument("--by", default="human:talkasab")
    parser.add_argument("--status", action="store_true")
    parser.add_argument("--list", metavar="DIR")
    args = parser.parse_args()
    try:
        if args.status:
            report_status()
        elif args.list:
            for path in sorted(scoped_path(args.list, directory=True).rglob("*.md")):
                data, _ = read_page(scoped_path(str(path)))
                if not is_verified(data):
                    print(path.relative_to(REPO))
        elif args.paths:
            if not args.by.strip():
                raise ValueError("--by must be non-empty")
            now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            # Validate all paths and frontmatter before writing any page.
            changes = [(path, marked_text(path, args.by, now)) for path in dict.fromkeys(scoped_path(value) for value in args.paths)]
            for path, text in changes:
                path.write_text(text, encoding="utf-8", newline="")
                print(f"verified {path.relative_to(REPO)} by {args.by} at {now}")
        else:
            parser.print_help()
            return 2
    except (ValueError, OSError, yaml.YAMLError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
