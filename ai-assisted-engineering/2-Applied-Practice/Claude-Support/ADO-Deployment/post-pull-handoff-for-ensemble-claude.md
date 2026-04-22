# Post-Pull Handoff For Ensemble Claude

Use this after the GitHub course repository has been pulled down inside the Ensemble environment.

## What To Tell Ensemble Claude

```text
You are helping deploy the latest AI-SDLC Applied Practice support material into the Ensemble ADO repos.

First, read:

ai-assisted-engineering/2-Applied-Practice/Claude-Support/ADO-Deployment/deployment-instructions-for-claude.md

Then do the following:

1. Confirm the local path to this pulled GitHub course repo.
2. Confirm the local path to the ADO `aisdlc-resources` repo.
3. Confirm the local path to the ADO `course-work` repo.
4. Verify the architecture diagram skill already exists at:
   aisdlc-resources/skills/AISDLC-tech-diagrams/
5. Tell me whether that skill is installed for Claude Code or only present on disk.
6. Verify whether `course-work-exercises` exists and whether you should copy starter exercises there.
7. Deploy only the approved participant-facing material.
8. Do not copy internal-only folders:
   _pipeline/
   _overview-internal/
   _template/
   _instructor-cheat-sheet/
   __research/
9. Show me the proposed copy plan before executing it.
10. After copying, provide positive proof: source path, destination paths, folders copied, folders excluded, git status for each ADO repo, and commit/push result if I approve commit/push.

Do not overwrite the AISDLC-tech-diagrams skill unless I explicitly ask.
Do not merge or push anything until I approve.
```

## Quick Verification Commands

Run only after paths are confirmed:

```bash
test -d "<aisdlc-resources>/skills/AISDLC-tech-diagrams" && find "<aisdlc-resources>/skills/AISDLC-tech-diagrams" -maxdepth 2 -type f | sort
```

```bash
test -d "<course-work>/participant-work" && find "<course-work>/participant-work" -maxdepth 2 -type d | sort
```

```bash
git -C "<aisdlc-resources>" status --short --branch
git -C "<course-work>" status --short --branch
```

Replace bracketed paths after the instructor confirms the actual local paths.

