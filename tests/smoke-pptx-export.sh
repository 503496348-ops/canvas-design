#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP_DIR="${TMPDIR:-/tmp}/canvas-design-pptx-smoke-$$"
SLIDES_DIR="$TMP_DIR/slides"
OUT_FILE="$TMP_DIR/out.pptx"
mkdir -p "$SLIDES_DIR"
trap 'rm -rf "$TMP_DIR"' EXIT

cat > "$SLIDES_DIR/01-title.html" <<'HTML'
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <style>
    * { box-sizing: border-box; }
    body {
      width: 1280px;
      height: 720px;
      margin: 0;
      background: #FEFEF9;
      font-family: Arial, sans-serif;
      overflow: hidden;
    }
    .title { position: absolute; left: 110px; top: 140px; width: 1000px; }
    .title h1 { font-size: 56px; color: #111111; margin: 0; }
    .title p { font-size: 24px; color: #555555; margin-top: 24px; }
  </style>
</head>
<body>
  <div class="title">
    <h1>Editable PPTX smoke test</h1>
    <p>This slide uses editable text elements and fixed 16:9 dimensions.</p>
  </div>
</body>
</html>
HTML

node "$ROOT/scripts/export_deck_pptx.mjs" --slides "$SLIDES_DIR" --out "$OUT_FILE"
test -s "$OUT_FILE"
python3 - <<PY
from pathlib import Path
p = Path("$OUT_FILE")
assert p.stat().st_size > 1000, f"PPTX too small: {p.stat().st_size}"
print(f"PPTX smoke ok: {p} ({p.stat().st_size} bytes)")
PY
