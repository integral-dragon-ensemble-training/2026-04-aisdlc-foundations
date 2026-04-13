# Session Brief

## Session 09

## Skills and Deterministic Hooks

### Purpose

Teach students when to use reusable skill-based guidance and when to use deterministic hooks that enforce mandatory checks automatically.

### Why this session matters

Teams often ask the model to "remember" rules that should have been mechanized. That does not scale. Skills are useful for reusable expertise and structured workflow help, but enterprise quality gates need hooks and other deterministic controls.

### Learning outcomes

By the end of this session, students should be able to:

- explain the difference between flexible skill-driven behavior and deterministic hook enforcement
- identify which recurring behaviors belong in a skill versus a hook
- configure a basic hook in shared project settings
- describe how hooks fit into the broader quality and policy pipeline
- avoid relying on the model alone for non-optional checks

### Core ideas

#### 1. Skills and hooks solve different problems

Skills help Claude bring reusable domain knowledge or workflow structure into a task. Hooks run automatically at lifecycle events and can block, transform, or trigger actions without relying on model memory.

#### 2. Flexible guidance is not enforcement

A skill can help Claude perform a review, formatting pass, or architectural pattern consistently. It cannot guarantee that a check happened unless an actual enforcement mechanism exists.

#### 3. Hooks turn standards into behavior

If the team must always run a formatter, lint step, secret scan, or file-protection rule, that should be encoded as a hook instead of treated as a polite reminder.

#### 4. Deterministic controls reduce trust burden

Good controls let engineers trust the process more because critical checks are executed algorithmically. This lowers review fatigue and reduces dependence on perfect prompting.

#### 5. Quality gates belong near the workflow

The earlier a deterministic control runs, the cheaper the failure is to catch. Hooks are valuable because they operate inside the tool lifecycle, not after the fact.

### Engineering implications

- recurring workflow help can be packaged into skills
- mandatory checks should be implemented as hooks or adjacent automation
- teams should differentiate guidance from enforcement in policy discussions
- hooks can block unsafe behavior before damage lands in the repo
- Session 09 is the first explicit move from advisory controls into algorithmic controls

### 23-minute flow

- `00:00-04:00`: Why "remember to check" is not a control
- `04:00-09:00`: Skills versus hooks
- `09:00-14:00`: Hook lifecycle and scope
- `14:00-18:00`: Live hook configuration demo
- `18:00-21:00`: Policy and CI/CD connection
- `21:00-23:00`: Debrief and bridge to Session 10

### Key takeaway

Use skills where reusable judgment helps. Use hooks where mandatory behavior must always occur. Enterprise delivery needs both, but they are not interchangeable.
