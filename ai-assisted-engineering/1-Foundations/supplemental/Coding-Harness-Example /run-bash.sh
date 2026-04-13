#!/bin/bash

# Run Claude Coding Harness with BASH backend
# Uses: cat, ls, sed (shell commands)

set -e  # Exit if any command fails

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/venv"

echo "🚀 Claude Coding Harness - BASH Backend"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
else
    echo "✓ Virtual environment exists"
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Install dependencies
echo "📚 Installing dependencies..."
pip install -q anthropic python-dotenv

# Run with Bash backend
echo "▶️  Starting harness with Bash backend...\n"
HARNESS_BACKEND=bash python "$SCRIPT_DIR/me-code.py"
