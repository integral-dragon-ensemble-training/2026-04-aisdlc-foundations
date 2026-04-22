# Workshop 4 — Exercises

Two core exercises plus three lightweight in-class activities. Pace them as the workshop allows; the core exercises are the backbone, the lightweight ones are warm-ups and fillers.

---

## Exercise 6 — Observability Gap Review

**Objective**

Evaluate whether the system is diagnosable in runtime.

**Estimated time**

15 minutes

**Format**

Group

**Inputs required**

- A code sample, service flow, or public demo repo.
- An observability checklist (logs, metrics, traces, deployment visibility).

**Instructions**

1. Identify the main request path or business action.
2. Ask what logs, traces, metrics, and deployment markers *should* exist if you had to debug a production incident tomorrow.
3. Review what is actually present.
4. Recommend the top three observability improvements.

**Expected output**

- A gap analysis tied to the actual workflow.
- A ranked list of telemetry improvements.
- A short verification plan describing how each improvement would be confirmed after deployment.

**How AI should be used**

AI can propose missing telemetry and draft logging standards or runbook snippets. Participants evaluate which suggestions carry real signal and which are noise.

**What a good answer looks like**

- Tied to an actual workflow, not generic advice.
- Distinguishes noise from useful signal.
- Includes *how the telemetry would be used* (which question it answers, for whom).

**Common weak patterns**

- "Add more logs" as the whole answer.
- Dashboards without a use case.
- No attention to correlation IDs, request context, or cross-service traceability.

---

## Exercise 7 — AI-Assisted Refactoring Review

**Objective**

Judge whether an AI-proposed change is safe, scoped, and worthwhile.

**Estimated time**

15 minutes

**Format**

Individual or pairs

**Inputs required**

- An AI-generated change proposal or diff.
- The AI-Assisted Refactoring Review Checklist (see `workshop-4-rubric.md`).

**Instructions**

1. Read the proposed change end to end.
2. Identify assumptions and unknowns the model glossed over.
3. Check what validation evidence exists (tests, runtime checks, security impact).
4. Decide: **approve**, **narrow scope and revise**, or **reject pending better evidence**.

**Expected output**

- A review decision with rationale.
- A list of missing evidence that would be required to approve.
- If narrowing, a rewritten, tighter scope that you *would* approve.

**How AI should be used**

Use AI to summarize the change and enumerate risks, but participants make the final decision. Do not let fluent summaries substitute for judgment.

**What a good answer looks like**

- Specific about risk, not hand-wavy.
- Aware of missing validation and willing to name it.
- Willing to cut scope rather than approve on vibe.

**Common weak patterns**

- Approving because the output sounds intelligent.
- Rejecting without identifying what evidence *would* make it acceptable.
- Ignoring deployment or runtime consequences.

---

## Lightweight Exercise — Confidence or Theater?

**Time:** 10 minutes

Show the class each of the following project signals and ask: does this increase *true* confidence, or is it mostly theater?

- 92% code coverage
- Green CI with no meaningful assertions
- One dashboard showing uptime only
- A post-deploy `/version` endpoint
- Structured error logs with request IDs

**Debrief**

- Which signal increases confidence *only if* something else is also true?
- Which signals are cheap to fake and expensive to trust?

---

## Lightweight Exercise — Where Would You Put the Log?

**Time:** 10 minutes

Give participants a small request flow (for example: an API endpoint that receives a payment request, calls a fraud-check service, writes to a database, and returns a receipt). Ask:

- What would you **log**?
- What would you **measure** (metric)?
- What would you **trace**?
- What would be **noise** and should not be added?

**Debrief**

- Which signals help answer "what happened, where, when, and why"?
- Which signals are vanity-only?
- What context (IDs, user, tenant, version) would you always want attached?

---

## Lightweight Exercise — Score the Diff

**Time:** 10–15 minutes

Show the class a hypothetical AI-generated PR summary. Ask participants to rate it on a 1–5 scale in each of:

- **Scope control** — is it doing one thing, or sprawling?
- **Validation plan** — are tests and runtime checks named?
- **Clarity** — can a reviewer explain what changed without re-reading the diff?
- **Operational awareness** — does it acknowledge logs, metrics, deploys, rollback?
- **Confidence level** — does the author state assumptions and uncertainty honestly?

**Debrief**

- Which dimension most often trips up AI-generated PRs?
- What single addition to the PR summary would move the weakest score up the most?
