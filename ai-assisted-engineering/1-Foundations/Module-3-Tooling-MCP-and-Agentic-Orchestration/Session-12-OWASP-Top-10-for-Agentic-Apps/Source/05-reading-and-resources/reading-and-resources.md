# Reading and Resources

## Session 12

## OWASP Top 10 for Agentic Apps

Verified on 2026-04-13. Primary sources are prioritized.

### Core references

- OWASP GenAI Security Project, Agentic Security Initiative
  https://genai.owasp.org/initiatives/agentic-security-initiative/
  Why it matters: official project page for the OWASP Top 10 for Agentic Applications and the broader agentic security workstream.

- OWASP GenAI Security Project, OWASP Top 10 for Agentic Applications for 2026
  https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
  Why it matters: the current official OWASP artifact for the 2026 agentic risks and mitigations discussed in this session.

- Anthropic, Claude Code Security
  https://code.claude.com/docs/en/security
  Why it matters: current official guidance on security safeguards, permission-based architecture, and why approval and scoped permissions matter for agentic tools.

### Strongly recommended

- Anthropic, Identity and Access Management
  https://code.claude.com/docs/en/iam
  Why it matters: documents permission tiers and the current permission model for Claude Code, which is useful for thinking about agent privilege and review boundaries.

- Anthropic, Connect Claude Code to tools via MCP
  https://code.claude.com/docs/en/mcp
  Why it matters: clarifies the tool access surface that makes agentic systems more capable and therefore more security-sensitive.

- NIST SP 800-207, Zero Trust Architecture
  https://csrc.nist.gov/pubs/sp/800/207/final
  Why it matters: the canonical zero trust reference for treating systems as explicit trust boundaries rather than relying on network location or implicit trust.

- OWASP GenAI Security Project, GenAI Red Teaming Initiative
  https://genai.owasp.org/initiatives/genai-red-teaming-initiative/
  Why it matters: useful for framing the session as a practical threat-modeling and red-team exercise rather than a purely theoretical discussion.

### Suggested follow-through

Take one agentic workflow in your environment and answer:

- What is the first point where data or instructions can be poisoned?
- Which tool or memory boundary is the highest-value control point?
- What would be the earliest sign that an agent had moved from content risk into action risk?
