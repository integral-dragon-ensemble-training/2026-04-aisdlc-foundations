# Harness Backends: Python vs Bash

This harness can operate in two modes to demonstrate different implementation approaches:

## Python Backend (Default)

```bash
./run.sh
# or explicitly:
HARNESS_BACKEND=python ./run.sh
```

**How it works:**
- `read_file` uses: `Path.read_text()` (Python built-in)
- `list_files` uses: `Path.iterdir()` (Python built-in)
- `edit_file` uses: `str.replace()` + `Path.write_text()` (Python built-in)

**Execution:**
```
Claude: tool: read_file({"filename": "calculator.py"})
                    ↓
            Python function call
                    ↓
            Direct file system access
                    ↓
            Return result instantly
```

**Advantages:**
- ✅ Faster (no subprocess overhead)
- ✅ Direct Python control
- ✅ Better error handling
- ✅ More precise string matching

---

## Bash Backend

```bash
HARNESS_BACKEND=bash ./run.sh
```

**How it works:**
- `read_file` uses: `cat <file>` (shell command)
- `list_files` uses: `ls -1 <directory>` (shell command)
- `edit_file` uses: `sed -i 's/old/new/'` (shell command)

**Execution:**
```
Claude: tool: read_file({"filename": "calculator.py"})
                    ↓
            Python subprocess.run()
                    ↓
            Fork bash process
                    ↓
            Execute: cat calculator.py
                    ↓
            Capture stdout
                    ↓
            Return result
```

**Advantages:**
- ✅ Shows shell integration
- ✅ Demonstrates cross-language execution
- ✅ Could run ANY shell command (security risk!)
- ✅ Good for teaching subprocess concepts

---

## Comparison Table

| Aspect | Python | Bash |
|--------|--------|------|
| Speed | Faster | Slower (subprocess overhead) |
| Code | In-process | Spawns subprocess |
| Error Handling | Detailed exceptions | Shell exit codes |
| Availability | Python-only | Universal (any shell) |
| Safety | Easier to control | Need shell escaping |
| Real-world | Production preferred | Hybrid systems |

---

## Demo Scenario

Perfect for teaching:

```bash
# Show Python version
./run.sh

# Ask Claude: "List the demo-source directory"
# Then: "Read calculator.py"

# Stop with Ctrl+C
# Check the api-logs to see the responses

# Now run with Bash
HARNESS_BACKEND=bash ./run.sh

# Ask the same question
# Notice the difference in execution!
```

**What students see:**
- Same tool interface, different implementations
- Same results, different execution paths
- Python is cleaner; Bash shows system integration

---

## Implementation Details

### Python Tools
Located in `me-code.py` lines ~180-260
- Direct library calls
- Exception handling
- Type hints

### Bash Tools
Located in `me-code.py` lines ~270-370
- `subprocess.run()` calls
- Shell command strings
- Output parsing

### Selection
Located in `me-code.py` lines ~375-390
```python
BACKEND = get_backend()  # Read HARNESS_BACKEND env var
if BACKEND == "bash":
    # Use bash versions
else:
    # Use python versions (default)
```

---

## Teaching Points

1. **Same interface, different implementations** - The tool names and signatures stay the same
2. **Process spawning** - Bash backend shows what happens when you call subprocess
3. **Error handling** - Compare Python exceptions vs shell exit codes
4. **Performance** - Python backend should be visibly faster
5. **Safety** - Discuss why subprocess needs careful escaping
6. **Real systems** - Many production systems use hybrid Python+Bash

---

## Extending

To add a **third backend** (e.g., Node.js):

```python
def read_file_node(filename: str) -> Dict[str, Any]:
    result = subprocess.run(
        ["node", "-e", f"console.log(require('fs').readFileSync('{filename}', 'utf8'))"],
        capture_output=True,
        text=True,
        check=True
    )
    return {"file_path": str(filename), "content": result.stdout}

# Then in selection:
if BACKEND == "node":
    read_file_tool = read_file_node
    # ... etc
```

This demonstrates how architecture enables flexibility!
