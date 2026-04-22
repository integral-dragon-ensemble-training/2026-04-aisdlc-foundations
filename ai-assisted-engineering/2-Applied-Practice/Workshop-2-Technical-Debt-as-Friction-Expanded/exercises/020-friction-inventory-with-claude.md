# 020 Friction Inventory With Claude

## Objective

Use Claude Code to collect friction evidence from the target repository.

## Claude Prompt

```text
Inspect the target repository for repeated change friction.

Look across:
- documentation and discoverability
- architecture boundaries
- reproducible setup
- tests and quality confidence
- build and release process
- data/schema/environment discipline
- observability and operations
- security and supply chain
- workflow and collaboration

For each friction item:
- cite concrete evidence by file/path or missing artifact
- describe who pays the cost
- describe when and how often the cost is paid
- explain what type of change it slows
- mark uncertainty clearly

Do not edit files. Produce a proposed friction register first.
```

## Output

- friction register draft
- evidence list
- uncertainty list

