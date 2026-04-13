# Session 10
## Task Decomposition and Subagents
### Break the work down before you delegate it

---

# Giant prompts usually fail for structural reasons

- too many goals mixed together
- unclear boundaries
- noisy outputs flooding the main context
- no explicit contract for what should come back

---

# Subagents are not magic; they are isolation tools

- fresh context
- focused role
- optional tool restrictions
- concise return path to the main conversation

---

# The real skill is decomposition

- identify independent work units
- define exact inputs
- define expected outputs
- constrain tools and scope
- sequence the tasks when dependencies exist

---

# Good delegated tasks are narrow and explicit

- "review this auth module for security issues and return a ranked summary"
- "trace failing tests and return only the root causes"
- "map the files touched by this feature and list likely risk areas"

---

# Bad delegated tasks sound like mini projects

- "build the whole feature"
- "fix everything wrong with this repo"
- "refactor the app and improve security"

These are not task boundaries. They are wishful thinking.

---

# Use subagents when isolation helps

- verbose output would pollute the main context
- the work is self-contained
- a tighter permission boundary is useful
- a specialist role improves focus

---

# Stay in the main conversation when continuity matters

- rapid back-and-forth refinement
- tightly coupled planning and implementation
- quick targeted edits
- tasks where startup overhead would dominate

---

# A delegated task needs a contract

- objective
- scope boundary
- allowed tools
- expected deliverable
- stop condition

---

# Live demo: one focused reviewer subagent

1. Define a narrow task.
2. Invoke a reviewer subagent.
3. Let it inspect a bounded area.
4. Bring back only the summary.

---

# Why this improves accuracy and cost

- less irrelevant context
- fewer mixed objectives
- smaller reasoning surface
- clearer human review point

---

# Common failure modes

- delegating before defining inputs and outputs
- using a subagent for work that needs constant interaction
- giving broad permissions to a narrow task
- asking for a summary with no criteria for what matters

---

# Key takeaway

- Subagents work best when the task is atomic.
- Atomic task design is an engineering responsibility, not a model feature.

---

# Bridge to Session 11

- Session 10 is hierarchical delegation.
- Session 11 expands that into coordinated parallel teams with shared state and new failure modes.
