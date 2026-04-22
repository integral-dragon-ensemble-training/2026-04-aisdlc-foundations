#!/bin/bash
# Render an .excalidraw file to a sibling .png via SVG (excalidraw_export + rsvg-convert).
# Usage: ./render-excalidraw-png.sh <input.excalidraw> [output.png]
#
# Defaults output to <input-basename>.png next to the input.

set -euo pipefail

INPUT="${1:?usage: $0 <input.excalidraw> [output.png]}"
if [[ ! -f "$INPUT" ]]; then
    echo "Input not found: $INPUT" >&2
    exit 1
fi

ABS_INPUT="$(cd "$(dirname "$INPUT")" && pwd)/$(basename "$INPUT")"
DEFAULT_OUTPUT="${ABS_INPUT%.excalidraw}.png"
OUTPUT="${2:-$DEFAULT_OUTPUT}"
ABS_OUTPUT="$(cd "$(dirname "$OUTPUT")" && pwd)/$(basename "$OUTPUT")"

TMP_SVG="${ABS_INPUT}.svg"
trap 'rm -f "$TMP_SVG"' EXIT

npx --yes excalidraw_export "$ABS_INPUT" >/dev/null 2>&1
rsvg-convert --zoom=2 "$TMP_SVG" -o "$ABS_OUTPUT"

echo "Rendered: $ABS_OUTPUT"
