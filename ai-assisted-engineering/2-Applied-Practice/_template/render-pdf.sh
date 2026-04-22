#!/bin/bash
# Render HTML slide deck to PDF using headless Chrome.
# Usage: ./render-pdf.sh <input.html> <output.pdf>
#
# Expects a deck where each <section class="slide"> is one 1280x720 slide
# stacked vertically when the deck.html is opened in "print" mode. The HTML
# itself should include an @media print stylesheet that lays out one slide
# per landscape page.

set -euo pipefail

INPUT_HTML="${1:?usage: $0 <input.html> <output.pdf>}"
OUTPUT_PDF="${2:?usage: $0 <input.html> <output.pdf>}"

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [[ ! -x "$CHROME" ]]; then
    echo "Google Chrome not found at $CHROME" >&2
    exit 1
fi

ABS_INPUT="$(cd "$(dirname "$INPUT_HTML")" && pwd)/$(basename "$INPUT_HTML")"
ABS_OUTPUT="$(cd "$(dirname "$OUTPUT_PDF")" && pwd)/$(basename "$OUTPUT_PDF")"

"$CHROME" \
    --headless \
    --disable-gpu \
    --no-pdf-header-footer \
    --print-to-pdf-no-header \
    --virtual-time-budget=10000 \
    --hide-scrollbars \
    --no-sandbox \
    --run-all-compositor-stages-before-draw \
    --no-default-browser-check \
    --print-to-pdf="$ABS_OUTPUT" \
    "file://$ABS_INPUT" 2>/dev/null

echo "Rendered: $ABS_OUTPUT"
