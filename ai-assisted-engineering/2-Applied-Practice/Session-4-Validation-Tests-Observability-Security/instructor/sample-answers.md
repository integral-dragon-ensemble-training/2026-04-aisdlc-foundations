# Session 4 — Sample Answer Guidance

Use these notes while reviewing student work from Exercises 6 and 7 and the three lightweight activities.

---

## Strong Day 4 validation analyses usually include

- Criticism of shallow coverage metrics.
- Attention to runtime verification, not just pre-merge tests.
- Awareness of observability and security as part of change safety.
- A demand for evidence before merge, applied consistently.

## Common weak patterns across Day 4

- Equating coverage with confidence.
- "Add more logs" as the observability answer.
- Approving AI-generated changes because the summary sounds intelligent.
- Rejecting AI-generated changes without naming what evidence would make them acceptable.
- Treating security scanning as polish.

---

## Exercise 6 — Observability Gap Review

### A strong answer looks like

- Tied to an actual workflow. Names a specific request path ("the claims submission endpoint") not a generic one.
- Distinguishes useful signal from noise. Good answers will say what they *would not* log.
- Includes *how the telemetry would be used*. Each proposed metric or log has a question it answers and an audience.
- Addresses correlation and traceability across service boundaries, not just single-service logging.

### A weak answer looks like

- "Add structured logs" with no specifics.
- A dashboard proposal with no use case.
- No acknowledgement of cost (log volume, cardinality, retention).
- Treating tracing and metrics as interchangeable.

### Calibration examples

- Student proposes adding a correlation ID to all logs in the payment path, wiring it through the fraud-check call, and surfacing it in error responses. **Strong.** Names a concrete question it answers ("where did this request fail?") and a use case (support triage).
- Student proposes "improving logging." **Weak.** Generic. Redirect to naming one specific log line, the context it carries, and who reads it.

---

## Exercise 7 — AI-Assisted Refactoring Review

### A strong answer looks like

- Specific about risk. Names the failure mode, not "could break things."
- Aware of missing validation. States what tests or runtime checks are absent.
- Willing to cut scope. Rewrites a too-broad diff into a smaller one the reviewer would approve.
- Decision with rationale, not decision alone.

### A weak answer looks like

- Approves because "the AI's reasoning looks solid."
- Rejects with no path to acceptance.
- Ignores deployment or runtime consequences.
- Treats assumptions the AI *stated* as automatically verified.

### Decision calibration

- **Approve** — scope is small, tests exist, assumptions are stated and verifiable, security and ops impact are acknowledged.
- **Narrow** — the idea is sound but the diff sprawls, or tests cover happy path only, or one part of the change is well-evidenced and another is not.
- **Reject** — assumptions are unverified, security-sensitive areas are touched without review, or the validation plan is absent. "Reject" should be paired with a named list of what would unlock approval.

---

## Lightweight — Confidence or Theater?

| Signal | Theater risk | Real-confidence conditions |
|---|---|---|
| 92% coverage | High | Only meaningful if assertions verify behavior and failure modes. |
| Green CI, no meaningful assertions | High | Valuable only when the test suite is risk-relevant and stable. |
| Uptime-only dashboard | High | Adds little about correctness; pair with behavior metrics. |
| `/version` endpoint | Medium | Useful *with* deployment-marker discipline and verification. |
| Structured error logs with request IDs | Low | Real signal when correlation works end-to-end. |

---

## Lightweight — Where Would You Put the Log?

Strong answers typically:

- Log at boundary crossings (inbound request, outbound call, persistence).
- Measure the few metrics that actually drive decisions (latency, error rate, fraud rate).
- Trace across the service-to-service hop, not within a single function.
- Treat retries, timeouts, and downstream failures as first-class events.

Weak answers usually:

- Log every function entry/exit.
- Confuse metrics and logs.
- Add tracing "everywhere" without naming what it would answer.

---

## Lightweight — Score the Diff

Use the five dimensions from the exercise. Typical patterns:

- **Scope control** is where AI-generated PRs most often fail. Sprawl is common.
- **Validation plan** is second. Tests are often named in the summary but not present in the diff.
- **Operational awareness** is often absent entirely.
- Students who score high on **Clarity** are usually reading the summary rather than the diff. Redirect them to verify against the code.
