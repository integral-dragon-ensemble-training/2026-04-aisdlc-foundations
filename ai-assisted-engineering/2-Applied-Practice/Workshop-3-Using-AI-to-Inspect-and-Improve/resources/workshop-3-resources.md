# Workshop 3 — Resources

Curated readings for Workshop 3. These anchor the workshop's teaching points about what AI coding tools are actually designed to do, how to shape prompts for real engineering work, and what expected capabilities look like across Claude Code, Gemini Code Assist, and GitHub Copilot's coding agent.

## Claude Code Overview

**Link:** https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview

**Why use it**

- Official description of an agentic coding workflow operating across files and tools.
- Good reference for framing what "Inspect / Explain / Propose / Scaffold" look like in a real tool's feature set.
- Useful for discussing where in-terminal agentic coding fits relative to IDE-embedded assistants.

## Gemini Code Assist Overview

**Link:** https://docs.cloud.google.com/gemini/docs/codeassist/overview

**Why use it**

- Useful official reference for contextual coding assistance and enterprise framing (repository-aware context, access controls, admin posture).
- Good companion reading for teams already in Google Cloud environments.
- Clarifies what "enterprise" coding assistance means in terms of context grounding and workspace integration.

## GitHub Copilot Cloud Agent

**Link:** https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent

**Why use it**

- Useful for discussing repository research, planning, and branch-based change workflows.
- Concrete example of a coding agent that operates asynchronously against a repo and produces a reviewable PR — directly reinforces the workshop's "small, scoped, reviewable" framing.
- Good anchor for the discussion on human review rules when AI is producing PRs, not snippets.

## Anthropic Prompting Best Practices — Chain of Thought

**Link:** https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-of-thought

**Why use it**

- Supports the lesson on prompt shape, structure, and clarity.
- Directly informs the Prompt Tightening lightweight exercise and the Codebase Analysis Prompt Template.
- Useful reference for teaching how to extract explicit reasoning and uncertainty from an AI response.

## How to use these in-workshop

- **Pre-workshop (optional):** skim the overview pages for whichever tool your team uses in practice.
- **During Slide 3 (prompt shape):** the Anthropic prompting doc is the natural companion.
- **After Exercise 4 (architecture map):** compare the first-pass map the AI produced to what the tool's documentation claims it is designed to do — fluency vs. capability.
- **After the workshop:** pick one tool and commit to a single concrete workflow for the coming week, rather than sampling all three superficially.

## Related assets

- **Participant Prompt Template for Codebase Analysis** — `exercises/workshop-3-prompt-template.md`
- **Workshop 3 Exercises** — `exercises/workshop-3-exercises.md`
- **Workshop 3 Slides** — `slides/workshop-3-slides.html`
