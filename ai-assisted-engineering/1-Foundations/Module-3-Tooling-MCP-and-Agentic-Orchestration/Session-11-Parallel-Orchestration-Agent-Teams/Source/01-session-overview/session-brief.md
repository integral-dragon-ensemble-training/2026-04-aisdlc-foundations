# Session Brief

## Session 11

## Parallel Orchestration: Agent Teams

### Purpose

Teach students when and how to use agent teams for genuinely parallel work that benefits from multiple independent Claude sessions coordinating through shared tasks and direct teammate communication.

### Why this session matters

Session 10 taught hierarchical delegation through subagents. Some work still benefits from a stronger coordination model: multiple workers researching, debating, and advancing separate tracks simultaneously. Agent teams introduce that power, but they also introduce coordination overhead, cost, and new failure modes.

### Learning outcomes

By the end of this session, students should be able to:

- explain the difference between subagents and agent teams
- identify when a task truly benefits from parallel teammates
- describe the roles of the lead, teammates, task list, and mailbox
- size teams and tasks to reduce collision and wasted effort
- articulate the main governance risks introduced by multi-agent coordination

### Core ideas

#### 1. Agent teams are for coordination-heavy parallel work

Teams are valuable when different workstreams can advance simultaneously and need to share findings, challenge assumptions, or coordinate across layers.

#### 2. Subagents and teams are not the same mechanism

Subagents report back to the caller in a hierarchical pattern. Agent teams are more independent: teammates can message one another directly, work from a shared task list, and coordinate without routing every update through the lead.

#### 3. Parallelism increases both leverage and cost

More teammates means more concurrent reasoning, more context windows, more tokens, and more coordination. Teams should be used where that tradeoff is justified, not as a default.

#### 4. The lead remains responsible

The lead session decides whether a team should exist, steers the work, reviews plans when required, resolves drift, and cleans up the team. More agents do not remove human oversight; they make good orchestration more important.

#### 5. Team design matters

Parallel work only helps when roles are distinct, file boundaries are separated, and task sizes are self-contained enough to avoid collisions and idle waiting.

### Engineering implications

- team creation should be deliberate and scoped to tasks with real parallel value
- teammate roles should be explicit and non-overlapping
- shared task systems need clean dependencies and ownership boundaries
- cost, permissions, and cleanup should be treated as part of the architecture
- Session 11 expands the orchestration model just before Session 12 secures it

### 23-minute flow

- `00:00-04:00`: Why parallel orchestration exists
- `04:00-09:00`: Agent teams versus subagents
- `09:00-14:00`: Team architecture: lead, teammates, tasks, mailbox
- `14:00-18:00`: Live team-creation demo
- `18:00-21:00`: Costs, collisions, and governance risks
- `21:00-23:00`: Debrief and bridge to Session 12

### Key takeaway

Agent teams are not just “more agents.” They are a coordination system. Use them when teammates need to work in parallel and communicate with one another, and only when the work is worth the added cost and control burden.
