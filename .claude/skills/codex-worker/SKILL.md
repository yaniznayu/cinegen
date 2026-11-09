---
name: codex-worker
description: Delegate heavy coding to Codex CLI via a task file and agents/codex_task.ps1.
---
# Codex worker

1. Copy `agents/tasks/000-template.md` to `agents/tasks/NNN-slug.md`; fill Goal / Acceptance criteria / Test command / Notes.
2. Run `pwsh agents/codex_task.ps1 agents/tasks/NNN-slug.md -Effort medium` (Git Bash: `agents/codex_task.sh <task> medium`).
3. Review `git diff` and test results yourself.
4. Never let Codex commit; the manager commits after review.
5. If Codex fails twice, escalate to Opus (see agents/ROUTING.md).
