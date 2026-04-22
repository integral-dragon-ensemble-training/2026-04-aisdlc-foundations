# Workshop 4 — Curated Readings

Readings for the validation workshop: tests, observability, security, and supply-chain hygiene. These are references for participants who want to go deeper, and for instructors who want to ground claims in primary sources.

---

## Testing

### The Practical Test Pyramid — Martin Fowler
https://martinfowler.com/articles/practical-test-pyramid.html

Why it is on the list: helps explain balanced testing without pretending all systems should test the same way. The right shape depends on the system, the risk, and the feedback cost.

### Test Pyramid — Martin Fowler (bliki)
https://martinfowler.com/bliki/TestPyramid.html

Why it is on the list: the concise foundational read for automated testing strategy. Pair it with the Practical Test Pyramid article above.

---

## Observability

### OpenTelemetry Observability Primer
https://opentelemetry.io/docs/concepts/observability-primer/

Why it is on the list: a straightforward framing of telemetry, reliability, logs, traces, and metrics. Use it to anchor the claim that observability is part of maintainability.

### OpenTelemetry Signals
https://opentelemetry.io/docs/concepts/signals/

Why it is on the list: a concise breakdown of traces, metrics, logs, and related concepts. Good reference when participants ask "what belongs in which signal type?"

---

## CI, Security Scanning, and Supply Chain

### GitHub Actions — Continuous Integration
https://docs.github.com/en/actions/get-started/continuous-integration

Why it is on the list: a clear CI baseline reference for build/test automation. Useful for showing what "automated validation is baseline" looks like in practice.


### GitHub Code Scanning
https://docs.github.com/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/about-code-scanning

Why it is on the list: baseline security automation reference. Shows what code scanning is, when it runs, and what it reports.

### Dependabot Alerts
https://docs.github.com/code-security/dependabot/dependabot-alerts/about-dependabot-alerts

Why it is on the list: a good entry point for dependency risk discussion. Vulnerable dependencies should be visible, not invisible.

### Dependency Review Action
https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/configuring-the-dependency-review-action

Why it is on the list: concrete example of PR-time supply-chain controls. Matches the "gate at PR time, not quarterly audit" framing from the slides.

### OWASP Top 10 (2025)
https://owasp.org/www-project-top-ten/

Why it is on the list: current baseline awareness reference for application security discussion. Useful as the starting vocabulary for "what do we mean by security hygiene?"

### SLSA
https://slsa.dev/

Why it is on the list: useful advanced reference when discussing supply-chain maturity and provenance. Treat this as optional depth for teams already doing the basics.

---

## Repositories worth showing in Workshop 4

### open-telemetry/opentelemetry-demo
https://github.com/open-telemetry/opentelemetry-demo

Why it is on the list: excellent observability teaching repo. Distributed system examples with real traces, metrics, and dashboards. Good counter-example to "just add more logs."

### spring-petclinic/spring-petclinic-microservices
https://github.com/spring-petclinic/spring-petclinic-microservices

Why it is on the list: a realistic microservice structure with runtime telemetry and operational visibility. Good to browse when teaching what "diagnosable in runtime" looks like.

### actions/starter-workflows
https://github.com/actions/starter-workflows

Why it is on the list: an easy way to show participants what good CI starting points look like, including security scanning and dependency review wiring.
