# 010 Import Scorecard And Branch Context

## Objective

Carry Workshop 1 evidence into Workshop 2 so friction analysis starts from known project-health gaps.

## Claude Prompt

```text
We are starting Workshop 2: Technical Debt as Friction.

Use my Workshop 1 coursework artifacts if available.

Set up:
- participant coursework folder: course-work/participant-work/<FirstName LastName>/workshop-2-technical-debt-as-friction/
- target repo branch: workshop-2-technical-debt-as-friction/<first-last-kebab>

Do not merge or push.

Read the Workshop 1 scorecard and summarize:
- weakest categories
- evidence behind low scores
- improvement attempted
- rescore delta
- unresolved uncertainty

Then propose which areas are likely debt/friction leads for Workshop 2.
Show me the summary before writing files.
```

## Output

- Workshop 2 workspace README
- imported Workshop 1 summary
- initial friction leads

