#!/usr/bin/env python3
"""Make a Quartz build browsable from plain object storage.

Quartz links pages in the "clean URL" style (`../glossary/oifm`, `./glossary/`)
and relies on the web server to map those to `oifm.html` and `index.html`.
Object storage such as a Tigris bucket serves keys literally, so this script
post-processes the finished build in three ways:

1. Rewrites every internal `href` in the emitted HTML to the explicit file
   (`../glossary/oifm.html`, `./glossary/index.html`).
2. Injects a small script into every page that applies the same rule in the
   browser to links the explorer sidebar and search build at runtime, both at
   creation (mutation observer) and at click time (capture-phase handler).
3. Patches the emitted JavaScript so direct navigations (`window.location.href
   = url`, used by the graph view on node click, `window.location.assign`) and
   the search panel's page-preview fetch pass through the same rule.

Run it on the output directory after `site/build.sh`; it is idempotent.

Usage:  python3 tools/flatten_site_links.py public
"""
from __future__ import annotations

import glob
import os
import re
import sys

HREF = re.compile(r'(href=")([^"#?]+)([#?][^"]*)?(")')
SKIP = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|//|#)", re.I)
HAS_EXT = re.compile(r"\.[A-Za-z0-9]{1,8}$")
MARKER = "okf-bucket-links"

CLIENT_SCRIPT = f"""<script id="{MARKER}">
(function () {{
  var SKIP = /^(?:[a-z][a-z0-9+.-]*:|\\/\\/|#)/i, HAS_EXT = /\\.[A-Za-z0-9]{{1,8}}$/;
  function fix(t) {{
    if (!t) return t;
    if (/^https?:\\/\\//i.test(t)) {{
      try {{ var u = new URL(t); if (u.origin !== window.location.origin) return t;
        u.pathname = fix(u.pathname); return u.toString(); }} catch (e) {{ return t; }}
    }}
    if (SKIP.test(t)) return t;
    var i = t.search(/[#?]/), path = i < 0 ? t : t.slice(0, i), rest = i < 0 ? "" : t.slice(i);
    if (path.endsWith("/")) return path + "index.html" + rest;
    var last = path.slice(path.lastIndexOf("/") + 1);
    if (last && !HAS_EXT.test(last)) return path + ".html" + rest;
    return t;
  }}
  window.__okfHref = fix;
  function fixAnchor(a) {{
    var h = a.getAttribute("href"); if (!h) return;
    var f = fix(h); if (f !== h) a.setAttribute("href", f);
  }}
  function fixAll(root) {{
    (root.querySelectorAll ? root.querySelectorAll("a[href]") : []).forEach(fixAnchor);
  }}
  document.addEventListener("click", function (e) {{
    var a = e.target && e.target.closest && e.target.closest("a[href]");
    if (a) fixAnchor(a);
  }}, true);
  new MutationObserver(function (muts) {{
    muts.forEach(function (m) {{
      m.addedNodes.forEach(function (n) {{ if (n.nodeType === 1) {{ if (n.matches && n.matches("a[href]")) fixAnchor(n); fixAll(n); }} }});
      if (m.type === "attributes" && m.target.matches && m.target.matches("a[href]")) fixAnchor(m.target);
    }});
  }}).observe(document.documentElement, {{ childList: true, subtree: true, attributes: true, attributeFilter: ["href"] }});
  if (document.readyState !== "loading") fixAll(document); else document.addEventListener("DOMContentLoaded", function () {{ fixAll(document); }});
}})();
</script>"""

JS_PATCHES = [
    # new URL(resolve(slug), window.location.origin).toString()   (search preview fetch)
    (re.compile(r"(?<!\)\()(new URL\(([^()]*\([^()]*\)[^()]*),window\.location\.origin\)\.toString\(\))"),
     r"(window.__okfHref||function(x){return x})(\1)"),
    # window.location.href = <expr>   (graph node click)
    (re.compile(r"window\.location\.href\s*=\s*(?!\(window\.__okfHref)([A-Za-z_$][\w$]*)"),
     r"window.location.href=(window.__okfHref||function(x){return x})(\1)"),
    # window.location.assign(<expr>)  (spaNavigate fallback when SPA is off)
    (re.compile(r"window\.location\.assign\((?!\(window\.__okfHref)([A-Za-z_$][\w$]*)\)"),
     r"window.location.assign((window.__okfHref||function(x){return x})(\1))"),
]


def fix(target: str) -> str:
    if SKIP.match(target):
        return target
    if target.endswith("/"):
        return target + "index.html"
    last = target.rsplit("/", 1)[-1]
    if last and not HAS_EXT.search(last):
        return target + ".html"
    return target


def process_html(path: str) -> tuple[int, bool]:
    with open(path, encoding="utf-8") as fh:
        html = fh.read()
    n = 0

    def sub(m: re.Match) -> str:
        nonlocal n
        new = fix(m.group(2))
        if new != m.group(2):
            n += 1
        return f"{m.group(1)}{new}{m.group(3) or ''}{m.group(4)}"

    new_html = HREF.sub(sub, html)
    injected = False
    if MARKER not in new_html and "</head>" in new_html:
        new_html = new_html.replace("</head>", CLIENT_SCRIPT + "\n</head>", 1)
        injected = True
    if new_html != html:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new_html)
    return n, injected


def process_js(path: str) -> int:
    with open(path, encoding="utf-8", errors="surrogateescape") as fh:
        js = fh.read()
    total = 0
    for pat, repl in JS_PATCHES:
        js, k = pat.subn(repl, js)
        total += k
    if total:
        with open(path, "w", encoding="utf-8", errors="surrogateescape") as fh:
            fh.write(js)
    return total


def main(out_dir: str) -> int:
    n_links = n_files = n_inject = 0
    for path in glob.glob(os.path.join(out_dir, "**", "*.html"), recursive=True):
        n, injected = process_html(path)
        n_links += n
        n_files += 1 if (n or injected) else 0
        n_inject += 1 if injected else 0
    n_js = sum(process_js(p) for p in glob.glob(os.path.join(out_dir, "**", "*.js"), recursive=True))
    print(f"flattened {n_links} links in {n_files} files, injected client fix into {n_inject} pages, patched {n_js} direct navigations under {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "public"))
