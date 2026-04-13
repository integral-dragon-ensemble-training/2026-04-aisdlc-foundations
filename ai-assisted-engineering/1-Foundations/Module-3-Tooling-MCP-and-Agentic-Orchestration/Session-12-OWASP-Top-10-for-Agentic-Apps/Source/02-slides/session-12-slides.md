# Session 12
## OWASP Top 10 for Agentic Apps
### The threat model shifts from bad text to bad action

---

# A hallucination is not the same as a breach

- A wrong answer is a content failure.
- A compromised action is an operational failure.
- Agentic systems require both content review and action control.

---

# The agentic attack surface expands fast

- prompt injection
- indirect prompt injection
- tool misuse
- identity spoofing
- memory poisoning
- insecure output handling

---

# Why prompt filtering is insufficient

- The dangerous instruction might arrive through a document, ticket, or tool result.
- The harmful action might happen after the model has reasoned correctly about the wrong thing.
- Safety has to live at the execution layer, not only at the prompt layer.

---

# The security question changed

- Not just: "Did the model say something unsafe?"
- Also: "What was the model allowed to do?"
- And: "What state or system did it touch?"

---

# Threat modeling must include tools and state

- reads from external systems
- writes to repositories
- data-bearing memory
- task handoffs
- privileged API calls

---

# Identity and authority matter

- Who is the agent?
- What can it access?
- Which actions are read-only?
- Which actions require explicit approval?

---

# Common control layers

- prompt and instruction hygiene
- permissions and sandboxing
- tool server controls
- authorization and identity
- human review and auditability

---

# Typical failure pattern

1. A malicious instruction enters through a tool or file.
2. The agent trusts the untrusted context.
3. The agent uses an overbroad tool permission.
4. A real system changes state or leaks data.

---

# Threat modeling exercise

- Map the attack path.
- Identify the earliest control that failed.
- Name the layer that should have stopped it.
- Do not stop at "the model was confused."

---

# The enterprise rule

- If the agent can act, security must govern the action.
- If the agent can write, write access must be bounded.
- If the agent can reach data, authorization must be explicit.

---

# No CLI demo today

- This session is a tabletop security exercise.
- The point is architectural clarity, not a feature demo.
- The next module turns these concerns into operational guardrails.

---

# Key takeaway

- Agentic systems move the risk from bad output to bad action.
- Security has to move with it.

---

# Bridge to Module 04

- Module 03 expanded capability and coordination.
- Module 04 tightens the controls around permissions, governance, and auditability.
