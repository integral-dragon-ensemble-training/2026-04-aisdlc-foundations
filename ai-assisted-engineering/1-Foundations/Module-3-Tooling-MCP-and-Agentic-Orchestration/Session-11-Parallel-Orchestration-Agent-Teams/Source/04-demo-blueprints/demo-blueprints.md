# Demo Blueprints

## Session 11

## Parallel Orchestration: Agent Teams

### Demo 01

## Same problem, different orchestration model

### Goal

Show students when a team is justified and when a simpler mechanism is better.

### Suggested flow

1. Present one task that is mostly sequential.
2. Present one task with three independent analysis tracks.
3. Ask Claude to explain which should use a single session, subagents, or an agent team.
4. Challenge the answer based on cost and coordination overhead.

### Teaching points

- orchestration choice should follow task shape
- more agents is not automatically better
- team value comes from parallel independence

### Demo 02

## Create a small agent team with explicit roles

### Goal

Show the mechanics of team creation and role definition.

### Suggested flow

1. Enable agent teams.
2. Ask Claude to create a 3-agent team:
   - one UX lens
   - one API/architecture lens
   - one QA or skeptic lens
3. Let the lead generate the shared task list.
4. Inspect how work is assigned and claimed.

### Teaching points

- the lead coordinates
- teammates operate in separate contexts
- the task list is part of the system, not an afterthought

### Demo 03

## Intervene, steer, and clean up

### Goal

Show that orchestration requires active management.

### Suggested flow

1. Send a redirect to one teammate.
2. Ask the lead to wait for teammates rather than doing the work itself.
3. Shut down a teammate.
4. Clean up the team correctly through the lead.

### Teaching points

- unattended teams drift
- cleanup is part of operational discipline
- Session 11 is about control, not spectacle
