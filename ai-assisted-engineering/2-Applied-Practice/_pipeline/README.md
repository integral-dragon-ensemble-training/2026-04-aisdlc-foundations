# Applied Practice Pipeline

This folder documents the transformation path that produced the current `2-Applied-Practice` course materials.

The goal is reproducibility by logic, not byte-for-byte determinism. The source prompts, model outputs, integration commits, and polish passes should let Dex or GT rerun the workflow and arrive at a course that is structurally consistent with the current one, even though phrasing and examples may vary.

## Stage Map

| Stage | Transformation | Primary Evidence |
| --- | --- | --- |
| `010-source-inventory` | Identify the source stack and live targets. | Research PDF, `v-gpt-2` bundles, live course tree, git commits. |
| `020-research-prompting` | Move from course intent to deep research and classroom asset prompts. | Gemini deep research and follow-up prompt files. |
| `030-expansion-bundle-selection` | Compare generated bundles and identify the selected source bundle. | `applied-practice 2` matched to `_overview-internal`. |
| `040-live-course-integration` | Convert the selected bundle into the live Applied Practice course. | Commit `b93fb3a` and workshop directories. |
| `050-participant-polish` | Split internal source reference from participant-facing overview. | Commit `cce2be0`. |
| `060-workshop-renaming-and-rendering` | Rename Session language to Workshop language and update rendered assets. | Commits `45ce5e0` and `ec2e741`. |
| `070-rerun-playbook` | Define how to rerun the pipeline consistently. | Replay steps, acceptance criteria, and verification checks. |
| `080-expansion-next-pass` | Prepare the next transformation: one-day workshops to three-to-five-day hands-on workshops. | Expansion constraints and proposed write boundaries. |

## Canonical Source Stack

Use this order when reconstructing or rerunning the work:

1. `ai-assisted-engineering/__research/gemini/ge,-v-2-AI-Assisted Enterprise Software Quality Course.pdf`
2. `ai-assisted-engineering/__research/v-gpt-2/applied-practice/`
3. `ai-assisted-engineering/__research/v-gpt-2/applied-practice 2/`
4. `ai-assisted-engineering/2-Applied-Practice/_overview-internal/`
5. `ai-assisted-engineering/2-Applied-Practice/overview/`
6. `ai-assisted-engineering/2-Applied-Practice/Workshop-*`

The selected source bundle is `applied-practice 2`. The other `applied-practice` folder is still useful because it contains the research prompts and an earlier/alternate bundle, but it should not be treated as the final source of the live course structure.

## Commit Trail

- `b93fb3a` - Added the Applied Practice course, session artifacts, and supplemental materials.
- `cce2be0` - Renamed `overview/` to `_overview-internal/` and added the participant-facing `overview/`.
- `45ce5e0` - Renamed Session to Workshop across Applied Practice and dropped time framing.
- `ec2e741` - Fixed Excalidraw text labels and added PNG renders plus the render script.

## Rerun Principle

When rerunning, preserve the following invariants:

- Brownfield quality improvement is the core course thesis.
- Claude Code and agentic coding workflows are practical tools, not the whole objective.
- The course teaches how to make repositories easier for AI agents and humans to work in.
- Applied work should focus on real project codebases where possible.
- Security, validation, observability, and governance are productivity enablers, not separate compliance appendices.

Accept variation in:

- examples
- slide phrasing
- exercise wording
- exact order of supporting topics
- generated diagrams and rendered artifacts

