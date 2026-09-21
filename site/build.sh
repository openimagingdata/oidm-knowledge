#!/usr/bin/env bash
# Build the OIDM knowledge Quartz site.
#
# Quartz itself is NOT vendored in this repository. This script clones the
# pinned Quartz commit into site/.quartz-src (gitignored), points it at our
# config and plugin, and builds knowledge/ into public/ at the repo root.
#
# Usage (from the repository root):
#   bash site/build.sh          # one-shot production build -> public/
#   bash site/build.sh serve    # local dev server with live reload
#
# See site/README.md for details and how to bump the pinned commit.
set -euo pipefail

QUARTZ_REPO="https://github.com/jackyzha0/quartz.git"
QUARTZ_SHA="97a2d05f80c4c50534959b1d0d41cc4b3895625e"

MODE="${1:-build}"

SITE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SITE_DIR/.." && pwd)"
QUARTZ_SRC="$SITE_DIR/.quartz-src"
BUNDLE_DIR="$REPO_ROOT/knowledge"
CONTENT_DIR="${TMPDIR:-/tmp}/oidm-knowledge-staged-$$"   # normalized copy of the bundle outside the repo (Quartz skips gitignored paths); see tools/prepare_site_content.py
trap 'rm -rf "$CONTENT_DIR"' EXIT
OUTPUT_DIR="$REPO_ROOT/public"

echo "==> Quartz checkout"
if [ ! -d "$QUARTZ_SRC/.git" ]; then
  echo "Cloning Quartz into ${QUARTZ_SRC#"$REPO_ROOT"/} ..."
  git clone --quiet "$QUARTZ_REPO" "$QUARTZ_SRC"
fi
git -C "$QUARTZ_SRC" fetch --quiet origin "$QUARTZ_SHA" || true
git -C "$QUARTZ_SRC" checkout --quiet "$QUARTZ_SHA"

CONFIG_FILE="${QUARTZ_CONFIG:-$SITE_DIR/quartz.config.yaml}"   # override with QUARTZ_CONFIG=<path> (used by publish-tigris.sh)
echo "==> Copying ${CONFIG_FILE#"$REPO_ROOT"/} into the checkout"
cp "$CONFIG_FILE" "$QUARTZ_SRC/quartz.config.yaml"

echo "==> npm ci"
( cd "$QUARTZ_SRC" && npm ci )

echo "==> Linking preact into the plugin's own node_modules"
# The okf-meta-plugin package is symlinked in place by `quartz plugin
# install`, not copied. Node resolves module specifiers against a symlinked
# file's REAL path, so a bare "preact" import inside the plugin does not see
# Quartz's own node_modules even though the plugin is declared right next to
# it in quartz.config.yaml. Symlinking preact into the plugin's own
# node_modules/ fixes the "Cannot find package 'preact'" resolution error
# without vendoring a copy of preact in this repo.
PREACT_SRC="$QUARTZ_SRC/node_modules/preact"
PLUGIN_NODE_MODULES="$SITE_DIR/okf-meta-plugin/node_modules"
if [ -d "$PREACT_SRC" ] && [ ! -e "$PLUGIN_NODE_MODULES/preact" ]; then
  mkdir -p "$PLUGIN_NODE_MODULES"
  ln -s "$PREACT_SRC" "$PLUGIN_NODE_MODULES/preact"
fi

echo "==> Installing plugins declared in quartz.config.yaml"
( cd "$QUARTZ_SRC" && npx quartz plugin install --from-config )

echo "==> Staging bundle with normalized links"
python3 "$REPO_ROOT/tools/prepare_site_content.py" --src knowledge --dest "$CONTENT_DIR"

echo "==> Building"
if [ "$MODE" = "serve" ]; then
  ( cd "$QUARTZ_SRC" && exec npx quartz build --serve -d "$CONTENT_DIR" -o "$OUTPUT_DIR" )
else
  ( cd "$QUARTZ_SRC" && npx quartz build -d "$CONTENT_DIR" -o "$OUTPUT_DIR" )
  echo "==> Built to ${OUTPUT_DIR#"$REPO_ROOT"/}"
fi
