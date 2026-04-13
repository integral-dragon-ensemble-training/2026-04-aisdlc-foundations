#!/bin/bash

# Run Claude Coding Harness with PYTHON backend
# Uses: Path.read_text(), Path.iterdir(), str.replace()

set -e  # Exit if any command fails

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/venv"

echo "🚀 Claude Coding Harness - PYTHON Backend"
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

# Run with Python backend
echo "▶️  Starting harness with Python backend...\n"
HARNESS_BACKEND=python python "$SCRIPT_DIR/me-code.py"
