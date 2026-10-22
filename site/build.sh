#!/usr/bin/env bash
# Build the public OIDM knowledge site from site/content/.
#
# Quartz is not vendored here. This script checks the pages first, clones
# the pinned checkout into site/.quartz-src (gitignored), installs our config
# and local plugins, copies shared brand assets, and builds into public/.
#
# Usage (from any working directory):
#   bash site/build.sh [--target dev|staging|production] [serve]
#   SITE_BASE_URL=example.com/path bash site/build.sh --target staging
#
# Dev is the default draft target. Production requires every page's review
# stamp. See site/README.md for the build and pinned-commit update procedure.
set -euo pipefail

QUARTZ_REPO="https://github.com/jackyzha0/quartz.git"
QUARTZ_SHA="97a2d05f80c4c50534959b1d0d41cc4b3895625e"
TARGET=dev
MODE=build
while [ "$#" -gt 0 ]; do
  case "$1" in
    --target)
      if [ "$#" -lt 2 ]; then echo '--target requires dev, staging, or production' >&2; exit 2; fi
      TARGET="$2"; shift 2 ;;
    serve) MODE=serve; shift ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
done
case "$TARGET" in
  dev) DEFAULT_URL=oidm-knowledge-dev.talkasab.workers.dev ;;
  staging) DEFAULT_URL=oidm-knowledge-staging.talkasab.workers.dev ;;
  production) DEFAULT_URL=oidm-knowledge.talkasab.workers.dev ;;
  *) echo "Invalid target: $TARGET" >&2; exit 2 ;;
esac
export SITE_TARGET="$TARGET"
SITE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SITE_DIR/.." && pwd)"
QUARTZ_SRC="$SITE_DIR/.quartz-src"
CONTENT_DIR="$SITE_DIR/content"
OUTPUT_DIR="$REPO_ROOT/public"
# Components render in Node. An absolute path survives the checkout's cwd
# and local-plugin symlinks, and is never shipped as a browser dependency.
export SITE_NAVIGATION_FILE="$SITE_DIR/navigation.yaml"

echo "==> Checking site ($TARGET)"
uv run "$SITE_DIR/tools/check_site.py" --target "$TARGET"

echo "==> Quartz checkout"
if [ ! -d "$QUARTZ_SRC/.git" ]; then
  echo "Cloning Quartz into ${QUARTZ_SRC#"$REPO_ROOT"/} ..."
  git clone --quiet "$QUARTZ_REPO" "$QUARTZ_SRC"
fi
git -C "$QUARTZ_SRC" fetch --quiet origin "$QUARTZ_SHA"
git -C "$QUARTZ_SRC" checkout --quiet "$QUARTZ_SHA"

CONFIG_FILE="${QUARTZ_CONFIG:-$SITE_DIR/quartz.config.yaml}"
echo "==> Copying ${CONFIG_FILE#"$REPO_ROOT"/} into the checkout"
cp "$CONFIG_FILE" "$QUARTZ_SRC/quartz.config.yaml"
# Override only the checkout's config; the tracked baseUrl stays unchanged.
export SITE_BASE_URL="${SITE_BASE_URL:-$DEFAULT_URL}"
uv run --with pyyaml python - "$QUARTZ_SRC/quartz.config.yaml" <<'PY'
import os,re,sys,yaml
from pathlib import Path
path=Path(sys.argv[1])
quoted=yaml.safe_dump(os.environ['SITE_BASE_URL'],default_style='"').strip()
path.write_text(re.sub(r'^(\s*)baseUrl:.*$',lambda m: m[1]+'baseUrl: '+quoted,path.read_text(),flags=re.M))
PY

echo "==> npm ci"
( cd "$QUARTZ_SRC" && npm ci )

echo "==> Linking shared dependencies into local plugins"
# Local plugins are symlinked, so bare imports resolve from their real paths
# outside Quartz's node_modules. Share Quartz's installed dependencies rather
# than installing or bundling extra copies of preact and the path utilities.
for PLUGIN in "$SITE_DIR"/plugins/*; do
  if node --input-type=commonjs -e 'process.exit(require(process.argv[1]).peerDependencies?.preact ? 0 : 1)' "$PLUGIN/package.json"; then
    mkdir -p "$PLUGIN/node_modules"
    ln -sfn "$QUARTZ_SRC/node_modules/preact" "$PLUGIN/node_modules/preact"
  fi
done
mkdir -p "$SITE_DIR/plugins/site-chrome/node_modules/@quartz-community"
ln -sfn "$QUARTZ_SRC/node_modules/@quartz-community/utils" "$SITE_DIR/plugins/site-chrome/node_modules/@quartz-community/utils"
ln -sfn "$QUARTZ_SRC/node_modules/yaml" "$SITE_DIR/plugins/site-chrome/node_modules/yaml"

echo "==> Installing plugins declared in quartz.config.yaml"
# The plugin move leaves dangling symlinks in older local checkouts. Quartz's
# index generator stats all of them, so discard only broken plugin links.
python3 - "$QUARTZ_SRC/.quartz/plugins" <<'PY'
from pathlib import Path
import sys
for path in Path(sys.argv[1]).glob('*'):
    if path.is_symlink() and not path.exists():
        path.unlink()
PY
( cd "$QUARTZ_SRC" && npx quartz plugin install --from-config )

echo "==> Copying brand assets"
# Restore tracked static files before replacing the icon so repeated builds
# start from Quartz's pinned assets, rather than a previous build's copies.
git -C "$QUARTZ_SRC" checkout -- quartz/static
mkdir -p "$QUARTZ_SRC/quartz/static/brand"
cp "$REPO_ROOT/assets/brand/oidm/logo-color.svg" "$QUARTZ_SRC/quartz/static/brand/logo-color.svg"
cp "$REPO_ROOT/assets/brand/oidm/logo-white.svg" "$QUARTZ_SRC/quartz/static/brand/logo-white.svg"
cp "$REPO_ROOT/assets/brand/oidm/mark.png" "$QUARTZ_SRC/quartz/static/icon.png"

echo "==> Building"
if [ "$MODE" = serve ]; then
  ( cd "$QUARTZ_SRC" && exec npx quartz build --serve -d "$CONTENT_DIR" -o "$OUTPUT_DIR" )
else
  ( cd "$QUARTZ_SRC" && npx quartz build -d "$CONTENT_DIR" -o "$OUTPUT_DIR" )
  echo "==> Built to ${OUTPUT_DIR#"$REPO_ROOT"/}"
fi
