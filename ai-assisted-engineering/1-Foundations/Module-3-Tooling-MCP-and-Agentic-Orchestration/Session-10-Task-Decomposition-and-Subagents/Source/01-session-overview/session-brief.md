# Session Brief

## Session 10

## Task Decomposition and Subagents

### Purpose

Teach students how to break large requests into bounded delegated tasks and use subagents to isolate work, control tool access, and keep the main session context clean.

### Why this session matters

Monolithic prompts fail because they overload context, mix concerns, and hide risk. Subagents help only if the work is decomposed well. The real skill is not delegation syntax. It is task slicing.

### Learning outcomes

By the end of this session, students should be able to:

- explain why large undifferentiated prompts perform poorly
- decompose a complex request into isolated subagent-sized tasks
- define clear inputs, outputs, and boundaries for delegated work
- choose when to use the main conversation versus a subagent
- describe how subagent isolation improves context management and reviewability

### Core ideas

#### 1. Decomposition is upstream quality control

If the task boundary is unclear, the delegated work will also be unclear. Good subagent behavior starts with good task design.

#### 2. Subagents isolate context on purpose

Verbose test output, large research results, and narrow specialist analysis do not always belong in the main conversation. Subagents keep that noise local and return a summary.

#### 3. Bounded work improves accuracy

A narrow delegated task with defined scope, tools, and expected output is easier to execute correctly than one giant prompt that mixes research, implementation, testing, and review.

#### 4. Tool restrictions matter

Subagents are valuable not only because they split work, but because they can operate with tighter permissions, different tools, and a more focused role.

#### 5. Not every task should use a subagent

Quick, tightly interactive tasks often belong in the main conversation. Subagents are best for self-contained work that can return a concise result.

### Engineering implications

- decomposition quality should be treated as a first-class engineering skill
- subagents help preserve context budget when output would otherwise be noisy
- task inputs and outputs should be explicit before delegation
- specialized roles and tighter tool scopes reduce risk
- Session 10 prepares the cohort for Session 11, where multiple workers run in parallel

### 23-minute flow

- `00:00-04:00`: Why giant prompts fail
- `04:00-09:00`: What makes a good subagent task
- `09:00-14:00`: Inputs, outputs, scope, and permissions
- `14:00-18:00`: Live subagent delegation demo
- `18:00-21:00`: When not to delegate
- `21:00-23:00`: Debrief and bridge to Session 11

### Key takeaway

Subagents are useful because they create isolation. But isolation only helps when the human decomposes the work into bounded units that can be delegated and reviewed cleanly.
