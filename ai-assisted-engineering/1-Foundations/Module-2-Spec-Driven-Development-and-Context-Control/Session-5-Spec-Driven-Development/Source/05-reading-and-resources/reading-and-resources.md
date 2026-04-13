# Reading and Resources

## Session 05

## Spec-Driven Development

Verified on 2026-04-09. Primary sources are prioritized.

### Core references

- Thoughtworks Technology Radar Vol. 33
  https://www.thoughtworks.com/content/dam/thoughtworks/documents/radar/2025/11/tr_technology_radar_vol_33_en.pdf
  Why it matters: Thoughtworks explicitly distinguishes context engineering from prompt wording and describes a reverse-engineering to design to forward-engineering loop that is directly useful for spec-first work.

- Anthropic, "Scaling agentic coding across your organization"
  https://resources.anthropic.com/hubfs/Scaling%20agentic%20coding%20across%20your%20organization.pdf?hsLang=en
  Why it matters: includes concrete examples of weak versus well-structured Claude Code requests and reinforces why structured inputs improve downstream reliability.

- Anthropic, Claude Code overview
  https://code.claude.com/docs/en/overview
  Why it matters: frames Claude Code as a tool that plans, edits, verifies, and works through the terminal rather than a chat toy. Useful for tying SDD to the actual harness students are using.

### Strongly recommended

- Addy Osmani, "Vibe coding is not the same as AI-Assisted engineering"
  https://medium.com/@addyosmani/vibe-coding-is-not-the-same-as-ai-assisted-engineering-3f81088d5b98
  Why it matters: sharp language for the mindset shift away from prompt-and-pray workflows and toward structured engineering.

- Addy Osmani, "Comprehension Debt — the hidden cost of AI generated code"
  https://medium.com/@addyosmani/comprehension-debt-the-hidden-cost-of-ai-generated-code-285a25dac57e
  Why it matters: useful for explaining why specs, review discipline, and small diffs matter even when the AI output looks fluent.

### Suggested follow-through

Take one real ticket and read it against this checklist:

- Does it specify success in observable terms?
- Does it capture constraints the agent must not violate?
- Does it define what is out of scope?
- Could a reviewer tell whether the work passed without asking the original author?
