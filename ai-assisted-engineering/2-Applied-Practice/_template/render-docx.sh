#!/bin/bash
# Render a markdown file to a .docx file using pandoc.
# Usage: ./render-docx.sh <input.md> <output.docx>
set -euo pipefail
INPUT_MD="${1:?usage: $0 <input.md> <output.docx>}"
OUTPUT_DOCX="${2:?usage: $0 <input.md> <output.docx>}"
pandoc "$INPUT_MD" -o "$OUTPUT_DOCX" \
    --from=gfm \
    --to=docx \
    --standalone \
    --toc=false
echo "Rendered: $OUTPUT_DOCX"
