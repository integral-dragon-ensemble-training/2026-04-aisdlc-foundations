# Agentic Delivery Landscape Overview

This is optional presenter material for framing the Session 05 discussion.

## Working position

Spec-Driven Development is useful, but it is not the only serious pattern on the table, and the field is not settled yet.

That is not just opinion. It is an inference from the fact that major players are using different center-of-gravity terms for roughly adjacent ideas:

- Anthropic talks about [agentic coding](https://resources.anthropic.com/scaling-agentic-coding).
- OpenAI talks about [harness engineering](https://openai.com/index/harness-engineering/).
- GitHub and Microsoft are pushing [spec-driven development](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/) and [Spec Kit](https://developer.microsoft.com/blog/spec-driven-development-spec-kit).
- Emerging tool builders are explicitly using the [dark factory](https://godarkfactory.com/) or lights-out framing.

If you want a clean way to say this live:

`We do not yet have one dominant doctrine. We have a landscape of operating models.`

One useful nuance: Box's public material is less "software dark factory" and more "governed agentic enterprise automation." Their current positioning is strongly about secure MCP-backed content access, permission-respecting agents, and human-oversight patterns inside enterprise workflows rather than a pure no-human-code-touch doctrine.

## A practical taxonomy

### 1. Assisted coding

Human writes or steers most of the implementation.

- AI helps with code generation, review drafts, tests, docs, and debugging.
- Human remains deeply in the loop on code and PR review.
- Lowest organizational disruption.
- Usually the easiest starting point in regulated environments.

### 2. Spec-driven development

The main control point moves upstream into the specification.

- Humans write the requirements, acceptance criteria, and constraints first.
- Agents implement from those specs.
- The promise is less prompt thrash, cleaner decomposition, and easier regeneration or variant exploration.
- GitHub's Spec Kit framing explicitly argues that business logic can be captured in a modern spec, then used to generate plans, tasks, and implementations.

### 3. Harness engineering

The main leverage point is not the prompt or even the spec by itself. It is the total system around the model.

- OpenAI's framing is that the real discipline increasingly lives in scaffolding, feedback loops, tools, invariants, and control systems.
- The harness includes repo structure, validation loops, worktrees, review agents, observability, and encoded rules.
- This view tends to treat prompts and specs as important, but insufficient without the surrounding execution system.

### 4. Dark factory or lights-out software delivery

The strongest autonomy claim in the landscape.

- Humans define roadmap, architecture, conventions, and merge policy.
- Agents implement, review, and sometimes merge with minimal or no direct human code touch.
- Dark Factory's own framing is `Humans design. Agents build.`
- This is the most aggressive model and usually depends on a strong harness, strong specs, and strong guardrails.

## The big variables and trade-offs

### Where is the source of truth?

- Assisted coding: usually the repo plus the human operator's judgment
- Spec-driven: the spec tries to become the durable source of truth
- Harness engineering: the source of truth is distributed across repo artifacts, constraints, tooling, and feedback systems
- Dark factory: the source of truth is the combination of roadmap, specs, architecture rules, and the harness

### Where does human effort move?

- Assisted coding: still largely in implementation and review
- Spec-driven: more effort moves into defining requirements well
- Harness engineering: more effort moves into toolchains, controls, and agent legibility
- Dark factory: more effort moves into portfolio direction, constraints, monitoring, and exception handling

### What is optimized?

- Assisted coding: immediate velocity for individuals
- Spec-driven: convergence and reduced ambiguity
- Harness engineering: reliability and repeatability at scale
- Dark factory: throughput and automation depth

### What breaks first?

- Assisted coding: review burden and inconsistent quality
- Spec-driven: ceremony, stale specs, and weak links to reality if the repo is not read first
- Harness engineering: setup cost, complexity, and organizational readiness
- Dark factory: trust, governance, and silent drift if review/monitoring is weak

## Is the spec the new code?

This is one of the most useful live debates to surface.

### Position A: Yes, the spec becomes the durable asset

Argument:

- code is now cheaper to regenerate than to handcraft
- the real scarce asset is validated intent
- GitHub's SDD ecosystem explicitly leans into the idea that you can capture logic in spec, design fresh architecture, and rebuild without carrying inherited debt

Best use case:

- greenfield systems
- bounded features
- high-variance exploration where multiple implementations are useful

### Position B: No, the repo and harness are still the real system

Argument:

- the running system includes code, tests, logs, CI, observability, lints, permissions, conventions, and feedback loops
- OpenAI's harness engineering write-up argues that the critical work shifts into scaffolding and control systems, not away from them
- specs matter, but they do not replace the rest of the engineering substrate

Best use case:

- mature products
- long-lived codebases
- environments where maintainability, operability, and evolution matter more than regeneration purity

### Position C: The spec is not the new code; it is the new control surface

This is probably the most defensible teaching position for your audience.

- the spec is where intent becomes legible
- the harness is where that intent becomes enforceable
- the repo is where that intent becomes operational

That lets you teach SDD without overstating its finality.

## A framing you can use live

`Spec-driven development is one serious answer to the AI delivery problem, but it is not the whole answer.`

`If your agents are unreliable, you may need better specs.`

`If your agents are inconsistent at scale, you probably need a better harness.`

`If your goal is near-total automation, you are really talking about some version of a dark factory.`

## My recommendation for Ensemble framing

For this audience, I would frame the landscape like this:

- umbrella term: `AI-assisted engineering` or `AI-accelerated software development`
- module-level method: `spec-driven development and context control`
- systems-level lens: `harness engineering`
- frontier autonomy pattern: `dark factory` or `lights-out software delivery`

That gives you one safe enterprise umbrella and three distinct operating models underneath it.

## A simple 2x2 you could sketch live

Axis 1:

- left: human-touch-heavy
- right: high autonomy

Axis 2:

- bottom: loose process
- top: strong constraints and controls

Map it roughly like this:

- bottom-left: ad hoc prompting / vibe coding
- top-left: disciplined assisted coding
- top-middle: spec-driven development
- top-right: dark factory

Then say:

`Harness engineering is not one box on the chart. It is the reason the upper half works at all.`

## Suggested discussion prompts

- If code becomes cheap, what becomes the scarce engineering asset?
- Do we want the source of truth to be the spec, the repo, or the harness?
- What would your security team allow first: better specs, stronger harnesses, or fully lights-out delivery?
- Where does human judgment add the most leverage in your environment today?

## Sources

- Anthropic, [Scaling Agentic Coding Across Your Organization](https://resources.anthropic.com/scaling-agentic-coding)
- OpenAI, [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)
- OpenAI, [Unlocking the Codex harness: how we built the App Server](https://openai.com/index/unlocking-the-codex-harness/)
- GitHub Blog, [Spec-driven development with AI: Get started with a new open source toolkit](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)
- Microsoft for Developers, [Diving Into Spec-Driven Development With GitHub Spec Kit](https://developer.microsoft.com/blog/spec-driven-development-spec-kit)
- Dark Factory, [Lights-out software development](https://godarkfactory.com/)
- Box Blog, [Agentic process automation: The complete guide](https://blog.box.com/agentic-process-automation)
- Box Blog, [The secure content layer for AI: The Box MCP server is now GA with Claude and a growing partner ecosystem](https://blog.box.com/secure-content-layer-ai-box-mcp-server-now-ga-claude-and-growing-partner-ecosystem)
