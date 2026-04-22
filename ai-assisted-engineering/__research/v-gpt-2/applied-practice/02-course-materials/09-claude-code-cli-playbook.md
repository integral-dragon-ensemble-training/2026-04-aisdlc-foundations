ChatGPT Folder > aisdlc-applied-practice > AI-SDLC Course Bundle > 09-claude-code-cli-playbook.md

# Claude Code CLI Playbook for This Course

## Teaching principle

Teach Claude Code CLI as a disciplined terminal-based engineering assistant, not as a magic code generator.

The classroom loop is:
1. define the question
2. scope the repo or subsystem
3. ask Claude to inspect or propose
4. review the output
5. change small
6. verify locally
7. document the result

## Minimal onboarding path

### Step 1 — Start in the repo root

```bash
cd your-project
claude
```

### Step 2 — Give it a bounded task

Good opening prompts:
- “Map the high-level architecture of this repository. Identify the main services, entry points, and likely runtime dependencies. Do not change code.”
- “Compare the README setup instructions to the actual build and run scripts. Tell me what looks stale or incomplete.”
- “Identify the top five risks that would slow down a new engineer trying to run this project locally.”

### Step 3 — Force analysis before modification

Examples:
- “Before changing code, explain your model of how this system is put together.”
- “Before proposing fixes, identify the evidence you used from the codebase.”
- “Propose the smallest viable improvement rather than a broad refactor.”

### Step 4 — Make the change bounded

Examples:
- “Add or improve tests only for the auth module. Run the relevant tests and summarize what passed, failed, or could not be validated.”
- “Add version exposure for this API with the smallest change that fits the current architecture.”
- “Improve startup documentation for local development without changing runtime behavior.”

### Step 5 — Review and verify

Examples:
- “Summarize every file changed and why.”
- “List any assumptions you made that still need human validation.”
- “Generate a reviewer checklist for this diff.”

## Stable classroom-friendly workflows

Use these heavily:
- repo analysis
- architecture summaries
- README repair
- local setup gap finding
- test gap analysis
- small test additions
- logging and version visibility suggestions
- PR summary drafting
- reviewer checklist drafting

Use more cautiously:
- large-scale refactors
- sweeping dependency upgrades
- automation that skips review
- preview features
- background or scheduled workflows not central to the class

## Useful prompt patterns by learning goal

### 1. Repo reconnaissance

```text
Inspect this repository and produce:
1. a high-level architecture summary,
2. the likely local run path,
3. the main build/test commands,
4. the top five missing or stale engineering artifacts,
5. the top three technical-debt issues that most reduce changeability.
Do not modify any files yet.
```

### 2. README reality check

```text
Compare the README and any onboarding docs against the actual repository structure and scripts.
Identify anything inaccurate, missing, or ambiguous for a new engineer.
Then propose a corrected README outline.
Do not update files until I approve the outline.
```

### 3. .NET solution mapping

```text
Analyze this .NET solution.
Identify:
- projects and their roles
- API entry points
- infrastructure dependencies
- test projects
- configuration sources
- any missing seams that make testing or local running hard
Return a concise architecture map and a prioritized improvement list.
```

### 4. Python service inspection

```text
Analyze this Python service or utility.
Identify:
- runtime entry points
- dependency management approach
- test setup
- configuration handling
- logging or observability patterns
- the minimum viable local run path
Return the most important changeability risks first.
```

### 5. Testability improvement

```text
Review this module for testability.
Identify why it is hard to test today.
Then propose the smallest set of changes that would improve unit or integration testing without broad redesign.
If you suggest tests, explain what behavior each test would protect.
```

### 6. Observability gap analysis

```text
Inspect this service for observability.
Tell me:
- where logs exist and where they are missing
- whether correlation or traceability is likely to break
- whether version/build information is exposed
- what the smallest useful observability upgrade would be
Prefer additive changes over architecture rewrites.
```

### 7. Release verification

```text
Inspect the project for release and deploy verification gaps.
Can an engineer tell what version is deployed, whether the expected build is running, and whether basic health checks exist?
Propose a small improvement plan with minimal blast radius.
```

### 8. Security and secrets review

```text
Inspect this repo for secrets-handling and security hygiene issues.
Focus on:
- hard-coded secrets
- configuration anti-patterns
- unsafe defaults
- missing scanning or validation hooks
Return findings grouped by severity and confidence.
Do not change code yet.
```

## Non-interactive examples

These are useful for demos and automation-friendly patterns.

```bash
claude "write tests for the auth module, run them, and fix any failures"
```

```bash
git diff main --name-only | claude -p "review these changed files for security issues"
```

```bash
tail -200 app.log | claude -p "identify anomalies, likely failure modes, and what extra logging would help"
```

## Example classroom `CLAUDE.md`

```markdown
# Training Repository Instructions

## Course purpose
This repository is used to practice AI-assisted engineering for technical debt reduction.

## Working style
- Prefer small, reviewable changes.
- Explain findings before making changes.
- Do not do broad refactors unless explicitly asked.
- Favor maintainability and clarity over cleverness.

## Validation rules
- Run the narrowest relevant tests after changes.
- Summarize what was actually validated.
- Call out anything you could not validate locally.

## Documentation rules
- If you update a script, command, or setup flow, check whether README or docs should also change.
- Prefer concrete commands and exact file references.

## Technology notes
- .NET is the primary application stack.
- Python may appear in utilities and scripts.
- Azure deployment and observability context matters.
- Prefer OpenTelemetry-compatible thinking for observability suggestions.

## Security rules
- Never introduce hard-coded secrets.
- Prefer managed identity, environment-based config, or existing secure patterns in the repo.
- Highlight risky assumptions.
```

## Prompting rules to teach students

### Good prompts are:
- bounded
- evidence-seeking
- explicit about “do not change code yet”
- explicit about the desired output shape
- explicit about validation

### Weak prompts are:
- “fix this repo”
- “make this production ready”
- “refactor everything”
- “add observability everywhere”
- “rewrite this architecture”

## Human judgment checkpoints

Always stop and inspect when:
- Claude wants to change many files at once
- the repo has unclear runtime boundaries
- the proposed change crosses multiple services
- migration or data-shape changes are involved
- the test story is unclear
- the deployment path is uncertain
- the repo has compliance or security sensitivity
- the suggested fix smells like a hidden rewrite

## Classroom debrief questions

After every Claude Code CLI exercise, ask:
1. What did Claude understand correctly?
2. What did it infer but not truly prove?
3. What evidence did it use?
4. What would you trust immediately?
5. What would you verify manually?
6. What was the smallest safe next step?
