# Session 1 — Resources

Curated readings and example repositories for Day 1: **What Good Looks Like**.

---

## Readings

### Martin Fowler — Technical Debt

Link: <https://martinfowler.com/bliki/TechnicalDebt.html>

Why use it:

- Good framing for the debt metaphor.
- Useful for explaining "interest" in future change.

### Martin Fowler — Technical Debt Quadrant

Link: <https://martinfowler.com/bliki/TechnicalDebtQuadrant.html>

Why use it:

- Helps students think beyond simplistic "good vs bad" design decisions.

### The C4 Model

Link: <https://c4model.com/>

Why use it:

- Lightweight approach to architecture diagrams.
- Strong fit for "maps of your code" teaching.

### arc42 Documentation

Link: <https://arc42.org/documentation/>

Why use it:

- Pragmatic structure for architecture communication and technical documentation.

### Development Container Specification

Link: <https://devcontainers.github.io/implementors/spec/>

Why use it:

- Solid reference point for reproducible developer setup.

### VS Code Dev Containers Tutorial

Link: <https://code.visualstudio.com/docs/devcontainers/tutorial>

Why use it:

- Approachable walkthrough for reproducible setup.
- Good supporting material if students ask "what would this look like in practice?"

---

## Example repositories

Public GitHub repositories suitable for Day 1 repo tours and the scorecard exercise.

### cookiecutter/cookiecutter-django

Link: <https://github.com/cookiecutter/cookiecutter-django>

**Best for** — docs and project scaffolding, production-minded defaults, pre-commit and workflow discussion.

**What to show** — README structure, docs links, contribution guidance, visible quality tooling.

**Caveat** — template-oriented rather than a single application with a small surface area.

### fastapi/full-stack-fastapi-template

Link: <https://github.com/fastapi/full-stack-fastapi-template>

**Best for** — modern full-stack structure, Docker-based local setup, GitHub Actions, migration-related discussion, release-minded application structure.

**What to show** — root README, `.github/workflows`, container and local-dev docs, backend migration guidance, how the project is organized across frontend/backend/infrastructure concerns.

**Caveat** — big enough that students can get lost unless you guide the tour.

### open-telemetry/opentelemetry-demo

Link: <https://github.com/open-telemetry/opentelemetry-demo>

**Best for** — observability, distributed tracing, runtime understanding, cross-service visibility.

**What to show** — README, local run instructions, dashboards or demo docs, service map, telemetry-oriented files or docs.

**Caveat** — distributed systems complexity may be high for some audiences.

### spring-petclinic/spring-petclinic-microservices

Link: <https://github.com/spring-petclinic/spring-petclinic-microservices>

**Best for** — microservice architecture discussion, metrics and dashboards, operational visibility.

**What to show** — repo structure, local startup guidance, Grafana/Prometheus references, tracing and service discovery elements.

**Caveat** — framework and stack specificity may limit generality for some teams.

### devcontainers/templates

Link: <https://github.com/devcontainers/templates>

**Best for** — reproducible developer setup, demonstrating what "clean machine onboarding" can look like.

**What to show** — template catalog, shape of template folders, how devcontainer usage lowers setup variance.

**Caveat** — not an application repo; use it as a pattern library, not as a system tour.

### sqlalchemy/alembic

Link: <https://github.com/sqlalchemy/alembic>

**Best for** — schema migration discipline, migration-as-code discussion.

**What to show** — purpose and role of migration tooling, how migration files are reviewed and versioned conceptually.

**Caveat** — tool-specific, so frame it as an example of a broader principle.
