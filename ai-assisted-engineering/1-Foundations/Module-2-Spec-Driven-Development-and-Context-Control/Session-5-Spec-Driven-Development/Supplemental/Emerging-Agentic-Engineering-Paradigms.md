# Emerging Agentic Engineering Paradigms

This is optional presenter material for Session 05.

It extends the landscape overview with additional paradigms that are showing real traction in public materials, even if the labels are not all fully settled.

## Short answer

Yes. There are several other paradigms worth naming.

The main ones I would add are:

- eval-driven agent development
- scenario-spec or verification-corpus development
- policy-as-code for agent delivery
- multi-agent orchestration as a delivery model
- background automation or always-on agent operations

These are not all mutually exclusive with spec-driven development or harness engineering.

The cleaner way to teach them is:

`Each paradigm places the control surface in a different place.`

## 1. Eval-driven agent development

### Core idea

The central question is not:

`Did we write a good prompt?`

It is:

`Can we measure whether the agent is behaving correctly over time?`

### What makes it different

- the agent is judged against graders, traces, scorecards, regression suites, or task-level evaluations
- evaluation becomes part of development, not just post hoc QA
- the unit of quality becomes repeatable agent behavior, not isolated output quality

### Why it matters

This is one of the strongest antidotes to AI theater.

If a team cannot evaluate the agent's behavior repeatedly, the team does not really control the workflow.

### Best fit

- production agents
- repeated operational tasks
- CI or issue-triage flows
- environments where trust has to be earned empirically

### Primary signal

- OpenAI's public materials on agent evals, internal agents, and agent-building tools push strongly in this direction.

## 2. Scenario-spec or verification-corpus development

### Core idea

The most important artifact is not just the implementation spec.

It is the scenario set that defines correct behavior and catches failure modes.

### What makes it different

- success is expressed through scenario specs, examples, failure cases, and verification corpora
- reviews validate behavior against those scenarios
- the test corpus becomes part of the delivery language, not just the implementation tail

### Why it matters

This is especially relevant when teams are worried about hidden regressions, business-logic misses, and shallow correctness.

It shifts the discussion from:

`What should the code look like?`

to:

`What situations must the system survive?`

### Best fit

- high-risk workflows
- QA-heavy teams
- teams that already think in examples, fixtures, and acceptance tests

### Primary signal

- Dark Factory leans hard into scenario specs.
- Anthropic and OpenAI increasingly describe systems where checks, validation loops, and behavioral tests do more governing than prompt cleverness.

## 3. Policy-as-code for agent delivery

### Core idea

The enduring system is not just code and not just specs.

It is the set of encoded rules that determine what agents may do, how they are checked, and what gets blocked automatically.

### What makes it different

- organizational rules become enforceable artifacts
- approval modes, sandboxes, path restrictions, hooks, and compliance checks are first-class
- governance moves from tribal memory into executable controls

### Why it matters

This is often the real enterprise unlock.

Many organizations do not need more model sophistication first.
They need stronger encoded constraints.

### Best fit

- regulated environments
- healthcare, finance, enterprise platforms
- teams trying to scale safe usage across many developers

### Primary signal

- Anthropic's permission and configuration model
- OpenAI's harness framing
- Paul Duvall's AI development patterns

## 4. Multi-agent orchestration as a delivery model

### Core idea

The agent is no longer one assistant in one thread.

The delivery unit becomes a coordinated system of agents with specialized roles, isolated contexts, and explicit handoffs.

### What makes it different

- planning, coding, review, QA, and narration can be split across roles
- work happens in parallel
- routing and handoff design become core engineering tasks

### Why it matters

This model changes throughput economics.

The constraint becomes less "can one model do this?" and more "how should the work be partitioned and supervised?"

### Best fit

- larger tasks with clean isolation boundaries
- teams comfortable with review workflows
- organizations optimizing for throughput rather than individual augmentation

### Primary signal

- Anthropic's recent material on scaling agentic coding
- OpenAI's Codex positioning around delegating parallel work and automations

## 5. Background automation or always-on agent operations

### Core idea

Some engineering work should not wait for a person to start a chat.

The agent should operate continuously in the background against specific classes of work.

### What makes it different

- agents monitor queues, logs, alerts, CI failures, or issue streams
- they can triage, propose fixes, summarize drift, or prepare patches proactively
- the emphasis is not code generation by request, but operational flow coverage

### Why it matters

This is where "agent" stops meaning "smart autocomplete" and starts meaning "active software-delivery participant."

### Best fit

- CI triage
- alert clustering
- repetitive PR preparation
- issue backlogs
- operational hygiene loops

### Primary signal

- OpenAI's current Codex framing around automations
- broader movement toward persistent, monitored engineering agents

## How these differ from the earlier paradigms

### Assisted coding

- center of gravity: human operator
- main value: immediate productivity

### Spec-driven development

- center of gravity: explicit intent and acceptance criteria
- main value: convergence and legibility

### Harness engineering

- center of gravity: system design around the model
- main value: reliability and enforceability

### Dark factory

- center of gravity: high-autonomy execution pipeline
- main value: throughput and automation depth

### The new additions

- eval-driven: center of gravity is measurement
- scenario-spec: center of gravity is behavioral verification
- policy-as-code: center of gravity is encoded governance
- multi-agent orchestration: center of gravity is task partitioning
- background automation: center of gravity is persistent operations

## A simple way to present this live

Instead of saying:

`Here are a bunch of competing buzzwords`

say:

`Here are the main places teams are trying to locate control in AI-assisted delivery.`

Then walk through these seven control surfaces:

1. the operator
2. the spec
3. the harness
4. the eval system
5. the policy layer
6. the orchestration model
7. the autonomous runtime

That gives the audience a much stronger conceptual map.

## My recommendation

For Ensemble, I would keep the visible teaching emphasis on:

- spec-driven development
- harness engineering
- reviewability and controls

And I would mention the others as emerging patterns so students understand the broader field without feeling like the course is chasing buzzwords.

If you want one sentence:

`Spec-driven development is about making intent legible, harness engineering is about making it enforceable, and eval-driven delivery is about proving it still works.`

## Sources

- OpenAI, [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)
- OpenAI, [Unlocking the Codex harness: how we built the App Server](https://openai.com/index/unlocking-the-codex-harness/)
- OpenAI, [Inside our in-house data agent](https://openai.com/index/inside-our-in-house-data-agent/)
- OpenAI Platform Docs, [Agent evals](https://platform.openai.com/docs/guides/agent-evals)
- Anthropic, [Scaling Agentic Coding Across Your Organization](https://resources.anthropic.com/scaling-agentic-coding)
- GitHub Blog, [Spec-driven development with AI: Get started with a new open source toolkit](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)
- Microsoft for Developers, [Diving Into Spec-Driven Development With GitHub Spec Kit](https://developer.microsoft.com/blog/spec-driven-development-spec-kit)
- Paul Duvall, [AI Development Patterns](https://github.com/PaulDuvall/ai-development-patterns)
- Dark Factory, [Lights-out software development](https://godarkfactory.com/)
