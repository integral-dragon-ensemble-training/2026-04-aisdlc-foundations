# 030 Debt Taxonomy And Interest Rate

## Objective

Classify friction items and estimate interest.

## Claude Prompt

```text
Use the friction register and classify each item.

For each item, assign:
- debt category
- principal: what would need to be changed
- interest: repeated cost if left alone
- evidence strength: strong, partial, weak
- likely owner or team function
- risk if fixed too broadly

Use a 1-5 interest estimate:
1 = low recurring cost
3 = noticeable repeated friction
5 = high recurring cost that slows many changes

Do not change code. Write a reviewed debt taxonomy table to the coursework folder after I approve it.
```

## Output

- classified friction register
- interest estimate
- weak-evidence items separated from strong-evidence items

