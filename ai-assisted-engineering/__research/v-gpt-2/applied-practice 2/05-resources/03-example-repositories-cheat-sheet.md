ChatGPT Folder > AI-SDLC Applied Practice Course Bundle > applied-practice/05-resources/03-example-repositories-cheat-sheet.md

# Example Repositories Cheat Sheet

Use this file when choosing which public repositories to show in class.

## 1. cookiecutter/cookiecutter-django

**Link**
https://github.com/cookiecutter/cookiecutter-django

**Best for**
- docs and project scaffolding,
- production-minded defaults,
- pre-commit and workflow discussion.

**What to show**
- README structure,
- docs links,
- contribution guidance,
- visible quality tooling.

**Course fit**
- Day 1,
- Day 3,
- Day 5.

**Caveat**
- template-oriented rather than a single application with a small surface area.

---

## 2. fastapi/full-stack-fastapi-template

**Link**
https://github.com/fastapi/full-stack-fastapi-template

**Best for**
- modern full-stack structure,
- Docker-based local setup,
- GitHub Actions,
- migration-related discussion,
- release-minded application structure.

**What to show**
- root README,
- `.github/workflows`,
- container and local-dev docs,
- backend migration guidance,
- how the project is organized across frontend/backend/infrastructure concerns.

**Course fit**
- Day 1,
- Day 3,
- Day 4.

**Caveat**
- big enough that students can get lost unless you guide the tour.

---

## 3. open-telemetry/opentelemetry-demo

**Link**
https://github.com/open-telemetry/opentelemetry-demo

**Best for**
- observability,
- distributed tracing,
- runtime understanding,
- cross-service visibility.

**What to show**
- README,
- local run instructions,
- dashboards or demo docs,
- service map,
- telemetry-oriented files or docs.

**Course fit**
- Day 1,
- Day 4.

**Caveat**
- distributed systems complexity may be high for some audiences.

---

## 4. spring-petclinic/spring-petclinic-microservices

**Link**
https://github.com/spring-petclinic/spring-petclinic-microservices

**Best for**
- microservice architecture discussion,
- metrics and dashboards,
- operational visibility.

**What to show**
- repo structure,
- local startup guidance,
- Grafana/Prometheus references,
- tracing and service discovery elements.

**Course fit**
- Day 1,
- Day 4.

**Caveat**
- framework and stack specificity may limit generality for some teams.

---

## 5. devcontainers/templates

**Link**
https://github.com/devcontainers/templates

**Best for**
- reproducible developer setup,
- demonstrating what “clean machine onboarding” can look like.

**What to show**
- template catalog,
- shape of template folders,
- how devcontainer usage lowers setup variance.

**Course fit**
- Day 1,
- Day 5.

**Caveat**
- not an application repo; use it as a pattern library, not as a system tour.

---

## 6. actions/starter-workflows

**Link**
https://github.com/actions/starter-workflows

**Best for**
- CI starting points,
- showing that baseline automation can start simple.

**What to show**
- workflow examples,
- how teams can standardize build/test gates.

**Course fit**
- Day 4,
- Day 5.

**Caveat**
- generic by design; best used as a teaching aid, not as proof of project excellence.

---

## 7. semantic-release / release-please

**Links**
- https://github.com/semantic-release/semantic-release
- https://github.com/googleapis/release-please

**Best for**
- release automation,
- semantic versioning,
- commit hygiene tied to release output.

**What to show**
- README,
- release workflow explanation,
- how changelog and version automation work.

**Course fit**
- Day 5.

**Caveat**
- more useful if your audience already understands CI basics.

---

## 8. sqlalchemy/alembic

**Link**
https://github.com/sqlalchemy/alembic

**Best for**
- schema migration discipline,
- migration-as-code discussion.

**What to show**
- purpose and role of migration tooling,
- how migration files are reviewed and versioned conceptually.

**Course fit**
- Day 1,
- Day 4.

**Caveat**
- tool-specific, so frame it as an example of a broader principle.

---

## Suggested minimum repo set for a 5-day class

If you want to keep it tight, use only these four:

1. `cookiecutter/cookiecutter-django`
2. `fastapi/full-stack-fastapi-template`
3. `open-telemetry/opentelemetry-demo`
4. `actions/starter-workflows`

That gives you:
- docs and setup,
- app structure and migrations,
- observability,
- CI discipline.
