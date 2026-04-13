#!/bin/bash

# Claude Coding Harness - Launcher Guide
# Choose which backend to run

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║       Claude Coding Harness - Choose Your Backend              ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

echo "This harness has TWO implementations to demonstrate different"
echo "architectural approaches:"
echo ""

echo "  🐍 PYTHON Backend (Recommended for speed)"
echo "     • Uses Python built-ins: Path.read_text(), Path.iterdir()"
echo "     • Fast, direct file access"
echo "     • Run: ./run-python-tools.sh"
echo ""

echo "  🐚 BASH Backend (Shows system integration)"
echo "     • Uses shell commands: cat, ls, sed"
echo "     • Slower (subprocess overhead)"
echo "     • Demonstrates subprocess execution"
echo "     • Run: ./run-bash.sh"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

read -p "Which backend? (python/bash) [python]: " choice
choice=${choice:-python}

case "$choice" in
    python)
        echo "Launching Python backend..."
        echo ""
        exec ./run-python-tools.sh
        ;;
    bash)
        echo "Launching Bash backend..."
        echo ""
        exec ./run-bash.sh
        ;;
    *)
        echo "Invalid choice. Run with: ./run-python-tools.sh or ./run-bash.sh"
        exit 1
        ;;
esac
