#!/bin/bash

# View API logs with proper JSON formatting
# Shows newlines and formatting correctly instead of escaped \n characters

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
API_LOGS_DIR="$SCRIPT_DIR/api-logs"

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "❌ jq is not installed"
    echo ""
    echo "jq is a JSON viewer that displays JSON with proper formatting."
    echo "Install it with:"
    echo "  brew install jq"
    echo ""
    echo "After installing, you can view logs like:"
    echo "  ./view-logs.sh 1      # View call #001"
    echo "  ./view-logs.sh 2      # View call #002"
    exit 1
fi

if [ -z "$1" ]; then
    echo "Usage: ./view-logs.sh <call_number>"
    echo ""
    echo "View API logs with proper JSON formatting."
    echo ""

    # List available logs
    if [ ! -d "$API_LOGS_DIR" ]; then
        echo "No api-logs directory found."
        exit 1
    fi

    call_files=$(find "$API_LOGS_DIR" -name "*-request.json" | sort)

    if [ -z "$call_files" ]; then
        echo "No API logs found."
        exit 1
    fi

    echo "Available logs:"
    for file in $call_files; do
        filename=$(basename "$file")
        call_num="${filename%-request.json}"
        echo "  ./view-logs.sh $call_num"
    done
    exit 0
fi

# Format call number (pad with zeros)
CALL_NUM=$(printf "%03d" "$1")
REQUEST_FILE="$API_LOGS_DIR/$CALL_NUM-request.json"
RESPONSE_FILE="$API_LOGS_DIR/$CALL_NUM-response.json"

if [ ! -f "$REQUEST_FILE" ] && [ ! -f "$RESPONSE_FILE" ]; then
    echo "❌ Call #$1 not found"
    exit 1
fi

# Display request
if [ -f "$REQUEST_FILE" ]; then
    echo "════════════════════════════════════════════════════════════════"
    echo "📤 REQUEST #$1"
    echo "════════════════════════════════════════════════════════════════"
    echo ""
    jq . "$REQUEST_FILE"
    echo ""
fi

# Display response
if [ -f "$RESPONSE_FILE" ]; then
    echo "════════════════════════════════════════════════════════════════"
    echo "📥 RESPONSE #$1"
    echo "════════════════════════════════════════════════════════════════"
    echo ""
    jq . "$RESPONSE_FILE"
    echo ""
fi
