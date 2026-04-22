# Repository Health Scorecard Skill

Use this as the content for a Claude Code skill, repo-local AI instruction, or reusable prompt.

## Purpose

Assess a repository against practical project health categories so engineers can identify friction, prioritize improvements, and make AI-assisted work safer and more effective.

## Core Rule

You are an evidence collector and improvement assistant. You may propose scores, but humans make the final scoring decision.

Do not infer confidence from polished wording. Use repository evidence.

## Scoring Scale

Score each category from 1 to 5:

- `1`: materially weak, missing, misleading, or risky
- `2`: present but fragile, inconsistent, or hard to trust
- `3`: workable but incomplete or uneven
- `4`: strong with minor gaps
- `5`: clear, current, repeatable, and easy for a new engineer to use

## Categories

1. Documentation and discoverability
2. Architecture clarity and boundaries
3. Reproducible developer setup
4. Testability and quality confidence
5. Build, deploy, and release discipline
6. Data, schema, and environment discipline
7. Observability and operational insight
8. Security, secrets, and supply chain hygiene
9. Workflow and collaboration discipline

## Evidence Rules

For each category:

- inspect relevant files and folders
- cite concrete artifacts by path
- separate evidence from inference
- name uncertainty explicitly
- explain why the score matters for future change
- suggest one small improvement if the score is low

Do not:

- score based on vibes
- assume a file is correct because it exists
- invent missing architecture
- equate test count with confidence
- treat absence of evidence as proof of absence without saying so
- recommend broad rewrites

## Output Format

```markdown
# Repository Health Scorecard

## Summary

- Overall score:
- Strongest categories:
- Weakest categories:
- Top three change-friction risks:
- Highest-leverage next improvement:

## Category Scores

| Category | Score | Evidence | Uncertainty | Improvement Candidate |
| --- | ---: | --- | --- | --- |
| Documentation and discoverability | | | | |
| Architecture clarity and boundaries | | | | |
| Reproducible developer setup | | | | |
| Testability and quality confidence | | | | |
| Build, deploy, and release discipline | | | | |
| Data, schema, and environment discipline | | | | |
| Observability and operational insight | | | | |
| Security, secrets, and supply chain hygiene | | | | |
| Workflow and collaboration discipline | | | | |

## Evidence Reviewed

- Files:
- Scripts:
- Workflows:
- Tests:
- Docs:
- Other:

## Top Three Weak Areas

1.
2.
3.

## Recommended Next Step

State one small improvement that would reduce real change friction.
```

## Improvement Guidance By Category

Documentation and discoverability:

- update README accuracy
- add setup path
- add architecture notes
- add glossary or runbook

Architecture clarity and boundaries:

- generate current-state component map
- document ownership and responsibilities
- identify dependency direction
- add a lightweight diagram

Reproducible developer setup:

- document tool versions
- add environment template
- add setup validation command
- propose devcontainer or bootstrap script

Testability and quality confidence:

- inventory tests and confidence gaps
- suggest behavior-focused tests
- add lockdown tests before refactoring
- reduce brittle or shallow tests

Build, deploy, and release discipline:

- document build commands
- summarize CI workflow
- add release checklist
- identify artifact/version visibility gaps

Data, schema, and environment discipline:

- document migration path
- identify seed/test data strategy
- flag environment drift risks
- propose review checklist for schema changes

Observability and operational insight:

- inspect logging patterns
- identify missing correlation or request context
- draft operational runbook
- propose deployment verification steps

Security, secrets, and supply chain hygiene:

- inspect secret handling patterns
- identify dependency scanning signals
- flag unsafe defaults
- propose baseline security checklist

Workflow and collaboration discipline:

- inspect PR templates and contribution docs
- summarize review conventions
- identify oversized-change risks
- propose small-change workflow improvements

