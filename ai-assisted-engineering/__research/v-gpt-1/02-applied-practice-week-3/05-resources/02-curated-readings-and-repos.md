ChatGPT Folder > AI-SDLC Applied Practice Course Bundle > applied-practice/05-resources/02-curated-readings-and-repos.md

# Curated Readings and Repositories

This is a practical, instructor-focused reading list organized by course theme.

## Day 1 — What Good Looks Like

### Martin Fowler — Technical Debt
Link: https://martinfowler.com/bliki/TechnicalDebt.html

Why use it:
- good framing for the debt metaphor,
- useful for explaining “interest” in future change.

### Martin Fowler — Technical Debt Quadrant
Link: https://martinfowler.com/bliki/TechnicalDebtQuadrant.html

Why use it:
- helps students think beyond simplistic “good vs bad” design decisions.

### The C4 Model
Link: https://c4model.com/

Why use it:
- lightweight approach to architecture diagrams,
- strong fit for “maps of your code” teaching.

### arc42 Documentation
Link: https://arc42.org/documentation/

Why use it:
- pragmatic structure for architecture communication and technical documentation.

### Development Container Specification
Link: https://devcontainers.github.io/implementors/spec/

Why use it:
- solid reference point for reproducible developer setup.

### VS Code Dev Containers Tutorial
Link: https://code.visualstudio.com/docs/devcontainers/tutorial

Why use it:
- approachable walkthrough for reproducible setup,
- good supporting material if students ask “what would this look like in practice?”

---

## Day 2 — Technical Debt as Friction

### Martin Fowler — Code Smell
Link: https://martinfowler.com/bliki/CodeSmell.html

Why use it:
- useful for distinguishing local code smells from broader project debt.

### Twelve-Factor App
Link: https://12factor.net/

Why use it:
- especially useful for configuration, dev/prod parity, logs, and operational discipline.

### Principles of Technical Documentation (arc42)
Link: https://arc42.org/principles-of-technical-documentation

Why use it:
- good source for explaining why documentation quality is part of engineering quality.

---

## Day 3 — Using AI to Inspect and Improve

### Claude Code Overview
Link: https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview

Why use it:
- official description of an agentic coding workflow operating across files and tools.

### Gemini Code Assist Overview
Link: https://docs.cloud.google.com/gemini/docs/codeassist/overview

Why use it:
- useful official reference for contextual coding assistance and enterprise framing.

### GitHub Copilot Cloud Agent
Link: https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent

Why use it:
- useful for discussing repository research, planning, and branch-based change workflows.

### Anthropic Prompting Best Practices
Link: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-of-thought

Why use it:
- supports the lesson on prompt shape, structure, and clarity.

---

## Day 4 — Validation: Tests, Observability, Security

### The Practical Test Pyramid
Link: https://martinfowler.com/articles/practical-test-pyramid.html

Why use it:
- helps explain balanced testing without pretending all systems should test the same way.

### Test Pyramid (Martin Fowler)
Link: https://martinfowler.com/bliki/TestPyramid.html

Why use it:
- concise foundational read for automated testing strategy.

### OpenTelemetry Observability Primer
Link: https://opentelemetry.io/docs/concepts/observability-primer/

Why use it:
- straightforward framing of telemetry, reliability, logs, traces, and metrics.

### OpenTelemetry Signals
Link: https://opentelemetry.io/docs/concepts/signals/

Why use it:
- concise breakdown of traces, metrics, logs, and related concepts.

### GitHub Actions: Continuous Integration
Link: https://docs.github.com/en/actions/get-started/continuous-integration

Why use it:
- clear CI baseline reference for build/test automation.

### GitHub Code Scanning
Link: https://docs.github.com/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/about-code-scanning

Why use it:
- baseline security automation reference.

### Dependabot Alerts
Link: https://docs.github.com/code-security/dependabot/dependabot-alerts/about-dependabot-alerts

Why use it:
- good entry point for dependency risk discussion.

### Dependency Review Action
Link: https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/configuring-the-dependency-review-action

Why use it:
- concrete example of PR-time supply-chain controls.

### OWASP Top 10 (2025)
Link: https://owasp.org/www-project-top-ten/

Why use it:
- current baseline awareness reference for application security discussion.

### SLSA
Link: https://slsa.dev/

Why use it:
- useful advanced reference when discussing supply-chain maturity and provenance.

---

## Day 5 — Making It Repeatable

### Semantic Versioning
Link: https://semver.org/

Why use it:
- useful baseline reference for release meaning and compatibility signaling.

### Conventional Commits
Link: https://www.conventionalcommits.org/en/v1.0.0/

Why use it:
- helps connect commit hygiene to release automation and clarity.

### semantic-release
Link: https://github.com/semantic-release/semantic-release

Why use it:
- concrete example of automated release discipline.

### release-please
Link: https://github.com/googleapis/release-please

Why use it:
- practical, review-oriented release automation example.

---

## Public GitHub repositories worth showing

### cookiecutter/cookiecutter-django
Link: https://github.com/cookiecutter/cookiecutter-django

Why use it:
- strong example of a production-minded template,
- visible docs,
- pre-commit integration,
- testing guidance,
- deployment-oriented structure.

### fastapi/full-stack-fastapi-template
Link: https://github.com/fastapi/full-stack-fastapi-template

Why use it:
- useful for Dockerized setup, GitHub Actions, and migration-oriented full-stack structure.

### open-telemetry/opentelemetry-demo
Link: https://github.com/open-telemetry/opentelemetry-demo

Why use it:
- excellent observability teaching repo,
- distributed system examples,
- good for showing traces, metrics, and dashboards.

### spring-petclinic/spring-petclinic-microservices
Link: https://github.com/spring-petclinic/spring-petclinic-microservices

Why use it:
- good for teaching microservice structure, runtime telemetry, and operational visibility.

### devcontainers/templates
Link: https://github.com/devcontainers/templates

Why use it:
- useful for showing what reproducible setup patterns can look like.

### actions/starter-workflows
Link: https://github.com/actions/starter-workflows

Why use it:
- easy way to show students what good CI starting points look like.

### sqlalchemy/alembic
Link: https://github.com/sqlalchemy/alembic

Why use it:
- concrete example/reference for migration discipline in Python ecosystems.

### pre-commit/pre-commit-hooks
Link: https://github.com/pre-commit/pre-commit-hooks

Why use it:
- visible, practical example of pre-commit quality checks.
