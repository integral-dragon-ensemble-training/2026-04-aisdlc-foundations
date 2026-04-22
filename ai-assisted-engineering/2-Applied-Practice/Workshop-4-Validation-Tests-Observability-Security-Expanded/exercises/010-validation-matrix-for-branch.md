# 010 Validation Matrix For Branch

## Objective

Map a candidate branch to the evidence required before group review.

## Claude Prompt

```text
We are starting Workshop 4: Validation.

Use my Workshop 3 review packet and candidate branch.

Build a validation matrix for the change.

For each changed file or behavior, identify:
- what could break
- what test evidence exists
- what observability evidence exists
- what security or dependency concern exists
- what manual review is required
- what remains unproven

Do not edit files yet. Show the validation matrix first.
```

## Output

- validation matrix
- unproven-risk list

