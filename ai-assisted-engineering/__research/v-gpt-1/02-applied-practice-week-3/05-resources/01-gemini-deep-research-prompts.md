ChatGPT Folder > AI-SDLC Applied Practice Course Bundle > applied-practice/05-resources/01-gemini-deep-research-prompts.md

# Gemini Deep Research Prompts

This file contains ready-to-use prompts for extending or refreshing the course research.

## Prompt 1 — Full Research Brief

```text
Before writing the full report, first determine the most logical 5-day progression for the course and the best grouping of topics. Then use that structure consistently throughout the rest of the report.

I need you to act like a senior software architecture educator and research analyst. Your job is to produce a high-quality research report that I can directly use to create a one-week short course on AI-SDLC (AI-assisted Software Development Life Cycle) for working software engineers.

This is not a generic “AI coding” course. The central thesis of the course is:

AI coding assistants such as Claude Code, Gemini, ChatGPT, and similar tools are most valuable not merely for generating new features, but for helping engineering teams understand, prioritize, and systematically pay down technical debt that slows down delivery, reduces confidence, and makes systems hard to change.

I need material for:
1. slide content,
2. class discussion material,
3. student exercises,
4. recommended readings,
5. GitHub repositories or code examples that demonstrate the principles in practice.

The course is 5 days, 1 hour per day, aimed at practicing engineers or advanced technical staff.

Please organize the report into these sections:
- Executive summary
- Refined teaching framework
- Five-day course outline
- Slide-building material
- Student exercises
- Recommended readings and online resources
- GitHub repositories and code examples
- AI-SDLC teaching guidance
- Practical rubrics and reusable artifacts
- Final recommendation

Important framing:
I want the course to emphasize what “good” looks like in a healthy software project, including:
- accurate and useful documentation,
- architecture clarity and diagrams,
- reproducible local setup,
- ability to build on a clean machine,
- meaningful local or isolated testability,
- reliable build and packaging workflows,
- test strategy that creates confidence,
- stable test data and mock/isolation strategy,
- database schema versioning and migration discipline,
- semantic versioning or clear release conventions,
- observability through logs, traces, metrics, and deployment verification,
- secure defaults, secret handling, and security scanning,
- linting, static analysis, and code quality automation.

I do NOT want you to accept this list uncritically.
Improve it, group it better, identify gaps, and point out what should be reframed.

Use current, credible, practical sources.
Prefer respected engineering sources over generic AI hype.
Be opinionated when appropriate, but grounded.
Distinguish universal principles from context-dependent practices.
Include specific examples, not just abstractions.
```

## Prompt 2 — Convert Research into Instructor Assets

```text
Using the report you just created, now convert it into instructor-ready course design material.

Create:
1. a final 5-day lesson plan,
2. a slide outline for each day,
3. an instructor cheat sheet with key talking points,
4. a student handout version,
5. a list of exercises with answer guidance,
6. a prioritized list of the best external resources and GitHub examples.

Requirements:
- Keep the 5-day narrative coherent.
- Remove duplication.
- Make each day realistic for a 1-hour class.
- Separate must-teach from nice-to-have.
- Flag anything too advanced or too long for this format.
- Present the answer in a way that can immediately be used to create slides and class materials.
```

## Prompt 3 — Public Repo Comparison

```text
Compare 4–6 public GitHub repositories as teaching examples for an AI-SDLC course focused on technical debt reduction and software project health.

Evaluate each repository for:
- documentation quality,
- architecture clarity,
- reproducible setup,
- testing strategy,
- migration or schema discipline,
- CI/CD discipline,
- release/versioning visibility,
- observability examples,
- security and dependency hygiene,
- teaching usefulness for a one-hour class.

For each repo, explain:
- what it demonstrates well,
- what students should inspect,
- what screenshots or snippets I could pull into slides,
- and any caveats such as size, complexity, or framework specificity.
```

## Prompt 4 — Generate a Class Exercise Packet

```text
Create a set of 8 practical exercises for a one-week AI-SDLC course for working engineers.

The course thesis is:
AI-assisted engineering is most valuable when it helps teams see, reduce, and systematically pay down the friction and technical debt that make software hard to change.

I need exercises in these categories:
- codebase inspection,
- technical debt identification,
- documentation critique,
- architecture mapping,
- AI prompt usage,
- testing improvement,
- observability gap analysis,
- staged modernization planning.

For each exercise, include:
- title,
- objective,
- format,
- time,
- instructions,
- expected output,
- how AI should be used,
- what a good answer looks like,
- common weak patterns.
```
