#!/bin/bash

# Clean up API logs directory
# Removes all recorded API requests and responses

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
API_LOGS_DIR="$SCRIPT_DIR/api-logs"

if [ ! -d "$API_LOGS_DIR" ]; then
    echo "✓ No api-logs directory found - nothing to clean"
    exit 0
fi

# Count files
FILE_COUNT=$(find "$API_LOGS_DIR" -type f | wc -l)

if [ "$FILE_COUNT" -eq 0 ]; then
    echo "✓ api-logs directory is empty - nothing to clean"
    exit 0
fi

echo "🗑️  Found $FILE_COUNT files in api-logs/"
read -p "Remove all API logs? (y/N) " -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]; then
    rm -rf "$API_LOGS_DIR"
    echo "✓ Cleaned up api-logs/"
else
    echo "✗ Cancelled"
    exit 1
fi
