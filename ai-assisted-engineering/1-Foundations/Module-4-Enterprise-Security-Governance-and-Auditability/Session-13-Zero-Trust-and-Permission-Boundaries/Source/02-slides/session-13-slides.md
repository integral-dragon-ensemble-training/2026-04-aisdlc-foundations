# Session 13
## Zero Trust and Permission Boundaries
### Deny by default, approve by policy, and audit the rest

---

# The agent is useful, not trusted

- It may need powerful access to do useful work.
- That does not make it a trusted actor.
- Zero Trust is the right mental model.

---

# Permissioning is the control plane

- tool whitelists
- read/write boundaries
- approval modes
- AI identity scope
- audit trails

These are engineering controls, not admin details.

---

# The dangerous habit to kill

- `--dangerously-skip-permissions`

That is not a shortcut.
It is a direct bypass of the control boundary.

---

# Least privilege should apply to AI identities

- give the agent only the access needed for the task
- scope credentials to the narrowest useful boundary
- separate read-only from write-capable roles
- do not reuse human trust assumptions for machine actors

---

# What Zero Trust means here

- never assume trust because the agent runs locally
- continuously verify boundaries at the tool level
- treat every action as potentially risky until explicitly allowed
- make approval an intentional event

---

# Control layers to name explicitly

- identity
- permissions
- approvals
- tools
- filesystem
- connectors
- audit logs

---

# Read-only is the safe baseline

- read-only analysis can happen with narrower risk
- write access should require explicit justification
- destructive actions should be rare and deliberate

---

# The blocked-execution demo should prove a point

- the agent attempts an action outside scope
- the system denies it
- the denial is expected, not a failure
- the policy is doing its job

---

# Common mistakes

- making the agent broadly privileged because setup is easier
- conflating local convenience with acceptable risk
- storing all permissions in tribal knowledge
- using approval prompts as decoration instead of control

---

# Key takeaway

- A useful agent is still a controlled agent.
- Zero Trust is how you keep that distinction real.

---

# Bridge to Session 14

- Session 13 controls what the agent may do.
- Session 14 controls what external systems the agent may reach and how those systems must defend themselves.
