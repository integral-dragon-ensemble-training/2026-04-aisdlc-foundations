# Reading and Resources

## Session 16

## Auditability and Workflow Narration

Verified on 2026-04-13. Primary sources are prioritized.

### Core references

- Claude Code Docs, Monitoring usage
  https://code.claude.com/docs/en/monitoring-usage
  Why it matters: shows current event and prompt correlation signals, event-level analysis, and audit-trail-oriented telemetry guidance that can support reconstructable workflows.

- Claude Code Docs, Data usage
  https://code.claude.com/docs/en/data-usage
  Why it matters: documents what Claude Code logs, what may be retained, and how session and telemetry data behave across local and cloud execution.

- Claude Code Docs, Checkpointing
  https://code.claude.com/docs/en/checkpointing
  Why it matters: explains how Claude Code tracks file edits and allows rewind/undo, which is helpful context for preserving change history and reconstruction.

### Strongly recommended

- Claude Code Docs, Zero data retention
  https://code.claude.com/docs/en/zero-data-retention
  Why it matters: important for understanding administrative controls, audit logs, and retention behavior in enterprise environments.

- NIST AI RMF Playbook
  https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook
  Why it matters: current NIST guidance on using the AI RMF with documented practices and trustworthiness considerations across the AI lifecycle.

- NIST AI RMF Playbook, Govern
  https://airc.nist.gov/airmf-resources/playbook/govern/
  Why it matters: emphasizes transparent policies, procedures, documentation, and accountability mechanisms that support auditability.

- NIST AI RMF Playbook, Measure
  https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook/Measure
  Why it matters: documents measurement, transparency, and documentation practices that help teams make AI behavior reviewable and measurable.

- NIST Special Publication 800-53 Revision 5
  https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf
  Why it matters: primary federal source for audit and accountability controls, including event logging and audit support expectations.

### Suggested follow-through

Take one AI-assisted change and answer:

- What evidence would let another engineer reconstruct the decision path?
- What should be captured in the PR narration versus the session log?
- What would an auditor still ask for after reading the code itself?
