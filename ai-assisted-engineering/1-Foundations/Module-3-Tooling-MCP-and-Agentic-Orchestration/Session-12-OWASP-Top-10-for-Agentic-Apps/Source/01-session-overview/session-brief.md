# Session Brief

## Session 12

## OWASP Top 10 for Agentic Apps

### Purpose

Teach students how to reason about the agentic threat surface: the shift from malformed text to malformed action once an agent can read data, call tools, and modify state.

### Why this session matters

A hallucination is annoying. An agent that exfiltrates data, mutates a record, or triggers a destructive action is a breach. The security conversation has to move from prompt quality to execution safety, identity, and tool trust.

### Learning outcomes

By the end of this session, students should be able to:

- explain the difference between content risk and action risk
- identify common agentic threats such as prompt injection, tool misuse, identity spoofing, and memory poisoning
- map a risky incident trace to the most likely control failure
- describe why prompt filtering alone is not a security strategy
- articulate the security controls that belong in the agent, tool, and server layers

### Core ideas

#### 1. The threat model changes when the model can act

Text generation risk is not the same as operational risk. Once an agent can access tools or state, the harm surface includes data exfiltration, unauthorized writes, and deceptive side effects.

#### 2. Indirect prompt injection is still a real attack path

Malicious content in a ticket, document, or retrieved page can influence the agent through tools and context. The risk is not confined to the user prompt.

#### 3. Identity and authority matter

An agent interacting with systems needs clear identity, permissions, and boundaries. Treating the agent as a trusted universal operator creates the same mistakes humans make with overprivileged service accounts.

#### 4. Memory and context can be poisoned

Persistent memory, task state, and retrieved context can all be manipulated. Teams need to review what the agent is allowed to remember, trust, and carry forward.

#### 5. Security must follow capability

As soon as a tool can write, mutate, or trigger downstream actions, the control model must tighten. Read-only by default is a good baseline; write access requires explicit justification and monitoring.

### Engineering implications

- threat modeling needs to be built into AI delivery
- model output review is not enough when tools can execute
- permissions, sandboxing, and server-level controls must be explicit
- secure design starts before deployment, not after an incident
- Session 12 sets the frame for the deeper governance controls in Module 04

### 23-minute flow

- `00:00-04:00`: Why agentic security is different
- `04:00-09:00`: Mal-content versus mal-action
- `09:00-14:00`: Common agentic threat classes
- `14:00-18:00`: Live threat-model tabletop
- `18:00-21:00`: Controls by layer
- `21:00-23:00`: Debrief and bridge to Module 04

### Key takeaway

Once the agent can take action, security has to move from content filtering to control of identity, tools, state, and side effects.
