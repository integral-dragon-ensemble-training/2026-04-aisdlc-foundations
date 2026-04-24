# GPT Image Prompt Guides

These prompt guides are for generating executive-facing visuals that support the Applied Practice story.

## Folder Map

```text
image-prompt-guides/
  README.md
  010-executive-operating-model-visual.md
  020-before-after-insights-visual.md
  030-group-branch-review-visual.md
```

## Model Guidance

Use `gpt-image-2` if available. OpenAI's current image generation documentation describes it as the state-of-the-art GPT Image model and supports generation/editing through the image APIs and image generation tool.

Official references:

- [GPT Image 2 model page](https://developers.openai.com/api/docs/models/gpt-image-2)
- [Image generation guide](https://developers.openai.com/api/docs/guides/image-generation)
- [Image generation tool guide](https://developers.openai.com/api/docs/guides/tools-image-generation)

## General Prompt Pattern

```text
Draw a 16:9 executive presentation visual for [audience] showing [core message].
Use [style].
Show [main elements].
Use only these labels: [label list].
Avoid [things to avoid].
Make it presentation-ready with generous spacing, readable labels, and no dense text.
```

## Quality Checklist

- The visual should make the argument before anyone reads the slide title.
- Labels should be short enough to survive image generation.
- The image should not include fake dashboards with impossible tiny text.
- The image should not imply automatic merging to production.
- The image should show human review and governance, not blind automation.
- If a logo or brand style is required, provide an approved reference image instead of asking the model to invent it.

## Recommended Iteration Loop

1. Generate the first visual with the full prompt.
2. Ask for one edit at a time: spacing, label correction, color palette, or emphasis.
3. If label text is wrong, regenerate with fewer labels.
4. If the image becomes too busy, ask for a simpler infographic version with no more than five labeled elements.
