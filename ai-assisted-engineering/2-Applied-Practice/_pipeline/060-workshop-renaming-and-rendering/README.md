# 060 Workshop Renaming And Rendering

This stage documents the terminology and artifact cleanup pass.

## Primary Commits

- `45ce5e0` - `Rename Session -> Workshop across Applied Practice; drop time framing`
- `ec2e741` - `Fix Excalidraw text labels; add PNG renders and render script`

## Transformation

The course moved away from one-hour session framing and toward workshop framing.

The pass changed:

- `Session-*` directories to `Workshop-*`
- `session-N-*` filenames to `workshop-N-*`
- `student-handout` language to `participant-handout`
- "student" language to "participant" language
- tight one-hour/day framing to more flexible workshop framing

The later diagram pass fixed Excalidraw text rendering and added PNG renders so diagrams could be consumed without opening the source files.

## Rerun Checks

Run these checks after a terminology or rendering pass:

```bash
rg -n "Session|session|student|Student|one-hour|1 hour|five-day|Day [1-5]" ai-assisted-engineering/2-Applied-Practice
```

Some matches may be legitimate in historical or internal source material, but participant-facing workshop material should use the current language.

Also inspect rendered assets when diagrams are touched:

```bash
find ai-assisted-engineering/2-Applied-Practice -type f \( -name "*.png" -o -name "*.pdf" -o -name "*.excalidraw" \) | sort
```

## Naming Rule Going Forward

Use "Workshop" for participant-facing Applied Practice units.

Use "Session" only when:

- preserving historical source material
- quoting original generated content
- describing a classroom schedule where "session" is explicitly correct

