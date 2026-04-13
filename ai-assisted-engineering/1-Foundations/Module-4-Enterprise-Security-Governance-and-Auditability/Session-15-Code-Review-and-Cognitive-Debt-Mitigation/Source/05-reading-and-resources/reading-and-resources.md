# Reading and Resources

## Session 15

## Code Review and Cognitive Debt Mitigation

Verified on 2026-04-13. Primary sources are prioritized.

### Core references

- Claude Code Docs, Create custom subagents
  https://code.claude.com/docs/en/sub-agents
  Why it matters: includes the built-in and example `code-reviewer` pattern, a review checklist, and guidance for making review behavior explicit and repeatable.

- Claude Code Docs, Claude Code GitHub Actions
  https://code.claude.com/docs/en/github-actions
  Why it matters: documents project standards, `CLAUDE.md` review criteria, and `/review`-style workflows that reinforce review as an explicit step rather than an afterthought.

- Anthropic, Claude Code Security
  https://code.claude.com/docs/en/security
  Why it matters: useful for framing review discipline as part of secure usage and scoped permissions, not just a style exercise.

### Strongly recommended

- Addy Osmani, "Comprehension Debt — the hidden cost of AI generated code"
  https://medium.com/@addyosmani/comprehension-debt-the-hidden-cost-of-ai-generated-code-285a25dac57e
  Why it matters: directly supports the idea that AI can create code faster than humans can understand it, which is the core cognitive debt problem in this session.

- Automation bias: a systematic review of frequency, effect mediators, and mitigators
  https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/
  Why it matters: a foundational systematic review on automation bias and why humans can overtrust automated outputs even when the automation is wrong.

- Claude Code Overview
  https://code.claude.com/docs/en/overview
  Why it matters: helps anchor the review workflow in the broader reality that Claude Code can edit files and create commits, so human review remains essential.

### Suggested follow-through

Review one AI-assisted diff and answer:

- What structural assumption did you almost accept without proving?
- Which test result was insufficient as evidence?
- What explanation would you give a teammate if you had to defend the review decision later?
