# Session Brief

## Session 13

## Zero Trust and Permission Boundaries

### Purpose

Teach students how to apply Zero Trust thinking to agentic workflows by narrowing permissions, approving actions explicitly, and treating the agent as a privileged but untrusted system component.

### Why this session matters

Once an agent can read files, call tools, or make changes, it is no longer a harmless text surface. The team has to control what the agent may touch, what it may not touch, and what must be approved before execution. Permissioning is not friction; it is the control plane.

### Learning outcomes

By the end of this session, students should be able to:

- explain why the agent should be treated like an untrusted third-party contractor
- distinguish permission scope from model quality
- identify where tool whitelists, approval modes, and RBAC fit in the control stack
- describe why `--dangerously-skip-permissions` is an unsafe anti-pattern
- articulate how Zero Trust applies to local agentic workflows

### Core ideas

#### 1. Trust is bounded, not assumed

Zero Trust means the agent does not receive broad trust simply because it runs locally or appears helpful. Every capability needs an explicit boundary.

#### 2. The agent is privileged, not trusted

The agent often needs file access, shell access, or connector access to be useful. That does not make it trustworthy. It means the environment must constrain what it can do.

#### 3. Permissions are a design choice

The team decides whether an action is allowed, denied, or gated by approval. That choice should be documented, repeatable, and auditable.

#### 4. RBAC should include AI identities

If the agent can act on behalf of a person or project, its identity must be governed like any other privileged identity. Human convenience is not a sufficient access policy.

#### 5. Skipping permissions is not a productivity strategy

The temptation to bypass checks for speed creates exactly the class of failure enterprise controls exist to prevent. Faster unsafe behavior is still unsafe behavior.

### Engineering implications

- tool whitelists should be as narrow as practical
- approval modes should be used for anything that can write, mutate, or trigger downstream impact
- AI identities should have explicit ownership and scope
- the safest default is deny first, then allow only when justified
- Session 13 sets the control baseline for the remaining security and governance sessions

### 23-minute flow

- `00:00-04:00`: Why Zero Trust applies to agents
- `04:00-09:00`: Permission boundaries and least privilege
- `09:00-14:00`: RBAC, approval modes, and AI identities
- `14:00-18:00`: Live blocked-execution demo
- `18:00-21:00`: What not to do with `--dangerously-skip-permissions`
- `21:00-23:00`: Debrief and bridge to Session 14

### Key takeaway

If the system cannot explain why the agent is allowed to do something, the agent should not be doing it.
