#!/usr/bin/env bash
# Publish a browsable copy of the site to a Tigris bucket (plain object
# storage, no directory-index mapping).
#
#   bash site/publish-tigris.sh [bucket] [prefix]
#   defaults: bucket=oidm-public prefix=oidm-knowledge
#
# Builds with a bucket-specific Quartz config (baseUrl under the bucket host,
# single-page navigation and popovers off, since those fetch extensionless
# URLs), flattens every internal link to an explicit .html path, then uploads
# with the Tigris CLI. Result: https://<bucket>.t3.storage.dev/<prefix>/index.html
set -euo pipefail

BUCKET="${1:-oidm-public}"
PREFIX="${2:-oidm-knowledge}"

SITE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SITE_DIR/.." && pwd)"
TMP_CONFIG="$(mktemp --suffix=.yaml)"
trap 'rm -f "$TMP_CONFIG"' EXIT

python3 - "$SITE_DIR/quartz.config.yaml" "$TMP_CONFIG" "$BUCKET" "$PREFIX" <<'EOF'
import re, sys
src, dst, bucket, prefix = sys.argv[1:]
s = open(src).read()
s = re.sub(r'^(\s*)baseUrl:.*$', rf'\1baseUrl: {bucket}.t3.storage.dev/{prefix}', s, flags=re.M)
s = re.sub(r'^(\s*)enableSPA:.*$', r'\1enableSPA: false', s, flags=re.M)
s = re.sub(r'^(\s*)enablePopovers:.*$', r'\1enablePopovers: false', s, flags=re.M)
open(dst, 'w').write(s)
EOF

echo "==> Building with bucket config"
QUARTZ_CONFIG="$TMP_CONFIG" bash "$SITE_DIR/build.sh"

echo "==> Flattening links for object storage"
python3 "$REPO_ROOT/tools/flatten_site_links.py" "$REPO_ROOT/public"

echo "==> Uploading to t3://$BUCKET/$PREFIX/"
t3 cp -r "$REPO_ROOT/public/" "t3://$BUCKET/$PREFIX/"

echo "==> Published: https://$BUCKET.t3.storage.dev/$PREFIX/index.html"
