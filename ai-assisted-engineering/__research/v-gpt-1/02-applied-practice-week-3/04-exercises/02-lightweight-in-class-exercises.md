ChatGPT Folder > AI-SDLC Applied Practice Course Bundle > applied-practice/04-exercises/02-lightweight-in-class-exercises.md

# Lightweight In-Class Exercises

These are 10–15 minute activities that can be inserted anywhere.

## 1. Smell or Debt?

Give students a list of examples and ask:
- is this a code smell,
- a broader technical debt item,
- both,
- or neither?

Good examples:
- misleading README,
- no traceability in logs,
- flaky end-to-end test,
- giant service class,
- unversioned DB change.

## 2. Confidence or Theater?

Show a project signal and ask if it increases true confidence:
- 92% code coverage,
- green CI with no meaningful assertions,
- one dashboard with uptime only,
- post-deploy version endpoint,
- structured error logs with request IDs.

## 3. Rewrite or Stage It?

Present a bad but common engineering situation and ask students to choose:
- rewrite,
- staged refactor,
- documentation first,
- testing first,
- observability first.

## 4. Prompt Tightening

Give a weak AI prompt like:
“Analyze this codebase and improve it.”

Ask students to rewrite it with:
- scope,
- criteria,
- output structure,
- uncertainty requirements,
- validation expectations.

## 5. Missing Artifact Drill

Ask: “What artifact would most reduce confusion here?”
Options:
- README section,
- architecture diagram,
- migration guide,
- runbook,
- test fixture strategy,
- PR template.

## 6. Where Would You Put the Log?

Give a small request flow and ask:
- what would you log,
- what would you measure,
- what would you trace,
- what would be noise?

## 7. Is This a Good AI Task?

Present tasks and ask students to sort them into:
- strong fit for AI,
- acceptable with review,
- poor fit / high risk.

## 8. One Better Question

Give students an AI answer and ask:
“What one follow-up question would make this answer materially better?”

## 9. Score the Diff

Show a hypothetical AI-generated PR summary and ask students to rate it for:
- scope control,
- validation plan,
- clarity,
- operational awareness,
- confidence level.

## 10. The Highest-Interest Debt

Each student writes down one debt item from their own environment and explains:
- category,
- who pays the interest,
- how often,
- why it matters.
