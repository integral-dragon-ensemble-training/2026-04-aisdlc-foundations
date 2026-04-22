# 050 Apply Small AI-Assisted Change

## Objective

Apply one small, reviewable improvement on the participant branch.

## Claude Prompt

```text
Apply the selected change plan on branch workshop-3-using-ai-to-inspect-and-improve/<first-last-kebab>.

Constraints:
- keep the diff small
- do not combine unrelated cleanup
- preserve behavior unless explicitly approved
- update docs or tests if needed
- run the narrowest relevant validation
- summarize exactly what changed
- do not merge or push unless I approve
```

## Output

- branch diff
- validation result
- remaining uncertainty

