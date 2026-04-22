ChatGPT Folder > aisdlc-applied-practice > AI-SDLC Course Bundle > 01-gemini-deep-research-prompt.md

# Gemini Deep Research Prompt — Revised for Claude Code CLI, Azure, .NET, and Python

You are acting as a senior software architecture researcher, enterprise engineering effectiveness advisor, AI-assisted software delivery coach, and practical course designer.

I need a rigorous research report that I can directly use to build and teach a one-week class on AI-SDLC.

## Course context

I am teaching a 5-day class.
Each day is 60 minutes long.
The audience is software engineers, tech leads, architects, and senior developers working in real enterprise software environments.

This is not a beginner coding class and not an “AI hype” class.
This is a brownfield, enterprise engineering class.
The audience likely works in codebases with technical debt, incomplete documentation, inconsistent local environments, fragile tests, weak observability, uncertain release verification, and mixed delivery maturity.

## Primary tool context

This course is specifically centered on **Claude Code CLI** as the primary hands-on AI coding tool.

I want the course to teach students how to use Claude Code CLI in practical, disciplined ways to:
- inspect a repository
- map architecture and dependencies
- identify technical debt
- propose safe, incremental improvements
- draft or improve documentation
- generate or improve tests
- tighten local build/run workflows
- improve observability and release visibility
- support safer code review and change planning

Do not treat Claude Code CLI as a side note.
It should be integrated throughout the course as the working instrument students use to practice AI-assisted engineering.

## Company and ecosystem context

The company context is heavily **Azure-oriented**.
The engineering ecosystem is primarily **.NET**, especially for core application and service work.
**Python** is becoming more important and should be included as a meaningful secondary path.

This means:
- prefer Azure-relevant examples when possible
- prefer .NET examples first when teaching core engineering practices
- include Python examples where they are useful and increasingly common
- keep the course principle-first and stack-neutral at the conceptual level
- but make examples concrete enough to feel native to an Azure + .NET shop with growing Python usage

When possible, show parallel implementations or examples in:
- .NET / ASP.NET Core / xUnit / OpenTelemetry / Application Insights / Azure Functions / .NET CLI / .NET Aspire or adjacent tooling where appropriate
- Python / FastAPI or Flask / pytest / OpenTelemetry / Azure SDKs / Python automation scripts where appropriate

## CI/CD and platform nuance

Because this is an Azure-heavy enterprise environment, prefer:
- Azure-native examples
- Azure DevOps-compatible thinking where relevant
- Azure deployment and verification patterns
- Application Insights / Azure Monitor / OpenTelemetry where relevant
- Azure Developer CLI, infrastructure-as-code, or repeatable environment setup patterns where useful

However, if a GitHub repo, blog post, or article is materially stronger as a teaching example, include it and explicitly explain how the principle translates to Azure-centric environments.

## Core thesis

The major value of AI coding assistants is not just generating new features faster.
A major value is helping teams identify, prioritize, and systematically pay down technical debt that makes software hard to change.

I want the course to teach students how to define what “good” looks like in a software project, recognize the debt that blocks it, and use AI tools to improve the system incrementally rather than attempting a risky rewrite or broad refactor all at once.

## Organizing theme

Use this as the course’s core organizing statement:

**AI-assisted engineering is most valuable when it helps teams see, reduce, and systematically pay down the friction and technical debt that make software hard to change.**

## Teaching philosophy

I want the course to hang together as a coherent story, not feel like disconnected topics.
I want the course to move from:
- defining what good looks like
- to diagnosing friction and technical debt
- to making targeted improvements
- to validating improvements through tests, observability, build/release discipline, and security
- to developing a repeatable AI-assisted engineering practice

The tone should be practical, engineering-first, evidence-based, and useful for enterprise teams.

## My initial ideas and seed topics

These are raw starting points, not fixed categories. Improve the structure if needed.

I believe “what good looks like” may include:
- accurate and complete documentation
- architecture clarity
- useful architecture diagrams
- reproducible developer setup on a new laptop
- ability to download the codebase and build it successfully
- ability to run meaningful parts of the system locally
- ideally the ability to run the full system locally, when practical
- strong unit tests
- meaningful test coverage
- integration tests
- end-to-end tests where justified
- ability to isolate dependencies with mocks/fakes/stubs when useful
- ability to build deployable artifacts from a local or dev environment
- database schema versioning and migration discipline
- good test database practices
- versioned or resettable test data
- rollbackable or snapshot-friendly test data approaches where appropriate
- good logging
- metrics and tracing where relevant
- ability to identify the exact deployed version of components
- release/version discipline
- ability to verify what is deployed in QA or pre-production
- ability to inspect logs and traces to follow system activity
- strong secrets handling and minimal unmanaged passwords
- security scanning
- linting
- static analysis
- reliable build automation
- healthy code review and source control practices
- controlled rollbackability and change isolation

## Additional topics I want you to evaluate

Please evaluate whether “what good looks like” should also explicitly include:
- maintainability and modularity
- dependency management and supply-chain hygiene
- onboarding time for new engineers
- ADRs / design decision records
- environment parity between local/dev/test/prod
- release verification and rollback
- performance and reliability guardrails
- feature flags or progressive delivery
- ownership boundaries and service boundaries
- data contracts / API contracts
- operational confidence
- AI-assisted codebase analysis workflows
- how to use Claude Code CLI safely in brownfield repositories without creating more debt
- how to write or curate a useful `CLAUDE.md` file for a project or training repo
- custom commands, hooks, or repeatable CLI workflows where useful
- safe use of permission modes, automation, or long-running workflows
- which Claude Code capabilities are stable enough for classroom use versus advanced or preview-only

## Your job

Produce a deep research report that helps me build this course.

### 1. Improve the taxonomy

Do not simply restate my list.
Synthesize it into a better structure.
Group related concepts into a small number of coherent teaching pillars.

A likely shape might include:
- architecture clarity
- reproducibility
- testability
- observability
- safe change

But do not force that model if a better one exists.
If you change it, explain why.

For each pillar, explain:
- why it matters
- what failure looks like
- what technical debt looks like
- how Claude Code CLI can help improve it
- what measurable signals indicate progress

### 2. Design the 5-day course

Create a full 5-day course flow that feels logical and cumulative.

I want:
- 1 or 2 lessons per day
- each day to build on the previous one
- a practical, workshop-friendly structure for a 60-minute session
- suggested time allocation for each day
- a note on what to cut if time runs short

Bias the course toward:
- brownfield improvement
- practical codebase inspection
- small safe improvements
- team habits that increase confidence over time

### 3. For each day and lesson, provide slide-building material

For each lesson, provide:
- lesson title
- short lesson description
- why this lesson belongs in that part of the week
- 3 to 5 learning objectives
- 5 to 8 slide-ready teaching points
- 1 suggested diagram or visual concept
- 3 to 5 common anti-patterns / failure smells
- 1 discussion prompt
- 1 instructor demo idea
- explicit Claude Code CLI usage ideas
- “human judgment required” notes

### 4. Create student exercises with Claude Code CLI deeply integrated

For each day or lesson, create at least one realistic student exercise.

I want exercises where students learn to use Claude Code CLI for practical engineering work, not just ask generic questions.

Examples of the kinds of Claude Code CLI exercises I want:
- analyze a repo and produce a “what good looks like” scorecard
- inspect a .NET solution and map the architecture
- inspect a Python service and identify setup gaps or hidden assumptions
- compare README instructions to actual build/run commands
- find missing or stale documentation
- identify the minimum viable local run path
- add or improve tests
- generate a test plan and then critique it
- review schema migration discipline
- assess test data reset strategies
- add logging, tracing, or version exposure
- identify secrets handling problems
- generate a safe incremental change plan
- draft a PR summary and reviewer checklist
- identify where Claude Code output is helpful versus where it is risky

For each exercise, include:
- title
- learning goal
- estimated duration
- setup / prerequisites
- student instructions
- Claude Code CLI prompt examples
- expected output
- instructor notes / debrief points
- lighter beginner version if needed
- more advanced version if needed

### 5. Create a Claude Code CLI teaching layer

This is important.
Create a dedicated section of the report for how to teach Claude Code CLI well in this course.

Include:
- a minimal classroom-ready Claude Code CLI onboarding path
- example `CLAUDE.md` contents for a training repo
- prompt patterns that work well for repo reconnaissance
- prompt patterns for tests, observability, docs, and release verification
- examples of good prompt scoping
- examples of risky or lazy prompt usage
- guidance on validating Claude’s output
- guidance on when to stop the agent and inspect manually
- guidance on using Claude for planning vs direct code modification
- lightweight workflow patterns for commit, review, and verification

If there are features that are advanced, preview, or unstable, mark them clearly.
Prefer stable classroom-friendly workflows first.

### 6. Find strong online readings and references

For every day, recommend readings and online resources.

Prefer:
- official Anthropic documentation for Claude Code CLI where appropriate
- official Microsoft documentation where appropriate
- high-quality engineering blogs
- reputable architecture/devops/testing/observability resources
- primary sources over generic listicles

For each resource, include:
- title
- link
- source / publisher
- what it teaches
- why it fits the lesson
- difficulty level
- whether it is Claude-specific, Azure-specific, .NET-specific, Python-specific, or stack-neutral

### 7. Find GitHub repositories or code examples that embody the principles

I need real projects, templates, or reference repos.

Prioritize examples that are useful for this environment:
- Azure-heavy or Azure-compatible
- .NET first when possible
- Python second where useful
- observability, tests, docs, build/run, migrations, release visibility, security, or structure
- brownfield-improvement-friendly examples
- repos that can support Claude Code CLI exercises

For each repo, include:
- repo name
- link
- what principles it demonstrates
- what students should inspect in it
- whether it is production-style, educational, or template-based
- caveats

### 8. Keep the course opinionated but careful

Distinguish between:
- foundational / non-negotiable practices
- strong recommended practices
- advanced or context-dependent practices
- controversial or stack-dependent recommendations

Be explicit where there are trade-offs.

### 9. Keep the course principle-first but concrete

Do not overfit the course to a single language or framework.
Keep the concepts portable.

But when examples are needed, prefer:
- .NET as the primary concrete example path
- Python as the secondary concrete example path
- Azure as the main platform context

### 10. Include the AI-assisted angle throughout

Do not isolate AI into one lesson and then forget it.

For every pillar and every day, include:
- how AI helps identify debt
- how AI helps draft artifacts
- how AI helps inspect dependencies and architecture
- how AI helps propose incremental refactors
- how AI helps improve tests
- how AI helps reason about telemetry gaps
- how AI helps create rollout or debt-paydown plans

Also include risks:
- hallucinated understanding of the codebase
- shallow confidence from generated tests
- hidden coupling
- over-refactoring
- poor repo-specific judgment
- generated code that increases long-term debt

### 11. Give me reusable instructor assets

At the end of the report, create:

#### A. “What Good Looks Like” scorecard
A practical scorecard for evaluating a software project.
It should have 10 to 15 dimensions.
For each dimension, define:
- what good looks like
- what poor looks like
- how to score it
- why it matters
- what kind of debt it reveals

#### B. Technical debt prioritization matrix
A simple rubric to help students decide what debt to fix first.
Include factors like:
- impact on delivery speed
- impact on reliability
- impact on onboarding
- impact on security
- impact on observability
- effort
- blast radius
- suitability for Claude Code CLI-assisted improvement

#### C. Capstone exercise
Design one final exercise where students assess a project or subsystem, identify the top technical debt blockers, and propose an incremental AI-assisted improvement plan using Claude Code CLI.

#### D. Glossary
Create a short glossary of key course terms.

#### E. “Top 10 non-negotiables” list
Create a concise list of the most important software project qualities that should survive even when teams disagree on implementation details.

## Output format

Return the report in well-structured Markdown.

Use this exact top-level structure:

# Executive Summary
# Recommended Course Narrative
# Improved Taxonomy of “What Good Looks Like”
# 5-Day Course Plan
## Day 1
## Day 2
## Day 3
## Day 4
## Day 5
# Claude Code CLI Teaching Layer
# Reusable Instructor Assets
# Suggested GitHub Repositories and Code Examples
# Suggested Readings and Online Resources
# Open Questions / Debates / Tradeoffs
# Final Recommendations

Within each day, clearly separate:
- lesson outline
- slide-building material
- exercises
- resources
- GitHub/code examples
- Claude Code CLI usage notes
- instructor notes

## Quality bar

The final report should be strong enough that I can immediately use it to:
- build a 5-day slide deck
- create student exercises and handouts
- build a repo evaluation rubric
- gather example repos and readings
- teach a coherent story about AI-assisted technical debt reduction in the SDLC
- show students how to use Claude Code CLI in disciplined, practical ways

Avoid generic filler.
Avoid AI hype.
Avoid simplistic “just use AI to code faster” framing.
Keep the focus on engineering quality, technical debt reduction, software changeability, safer delivery, and practical enterprise adoption.
