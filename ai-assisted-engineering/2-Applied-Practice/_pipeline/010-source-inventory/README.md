# 010 Source Inventory

This stage identifies the material that must be preserved as the source stack for the current Applied Practice course.

## Inputs

Primary research:

- `ai-assisted-engineering/__research/gemini/ge,-v-2-AI-Assisted Enterprise Software Quality Course.pdf`

GPT/GT-side generated bundles:

- `ai-assisted-engineering/__research/v-gpt-2/applied-practice/`
- `ai-assisted-engineering/__research/v-gpt-2/applied-practice 2/`
- `ai-assisted-engineering/__research/v-gpt-2/applied-practice-v0.1.zip`
- `ai-assisted-engineering/__research/v-gpt-2/applied-practice-course-bundle-v0.1.zip`

Live course outputs:

- `ai-assisted-engineering/2-Applied-Practice/_overview-internal/`
- `ai-assisted-engineering/2-Applied-Practice/overview/`
- `ai-assisted-engineering/2-Applied-Practice/Workshop-*`
- `ai-assisted-engineering/2-Applied-Practice/_template/`

## What Was Learned

The relevant redesign source is the Gemini PDF named `ge,-v-2-AI-Assisted Enterprise Software Quality Course.pdf`, not the older Foundations redesign research.

The live Applied Practice course was created in the same commit that added the Gemini PDF and both `v-gpt-2` bundle candidates. The git evidence points to the following workflow:

1. Gemini research was produced or imported.
2. GPT/GT-side prompts and bundle generation created candidate Applied Practice bundles.
3. The `applied-practice 2` bundle was selected as the stronger classroom source.
4. The selected bundle was integrated into `2-Applied-Practice`.
5. Later commits polished participant-facing materials and renamed Session language to Workshop language.

## Verification Commands

Run from the repository root:

```bash
git log --oneline -- ai-assisted-engineering/2-Applied-Practice ai-assisted-engineering/__research/v-gpt-2 ai-assisted-engineering/__research/gemini
```

```bash
find "ai-assisted-engineering/__research/v-gpt-2" -maxdepth 3 -type f | sort
```

```bash
diff -u \
  "ai-assisted-engineering/__research/v-gpt-2/applied-practice 2/02-course-design/01-five-day-course-map.md" \
  "ai-assisted-engineering/2-Applied-Practice/_overview-internal/five-day-course-map.md"
```

Expected result for the diff: the live internal overview should mostly match the selected bundle, with the generated breadcrumb line removed.

## Output Of This Stage

The output is a known-good source manifest:

- use `applied-practice 2` as the selected source bundle
- use `applied-practice` for research prompts and alternate framing
- use git commits as the integration record
- use the live `2-Applied-Practice` tree as the current truth

