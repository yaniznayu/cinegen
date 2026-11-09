# Task routing policy

| Worker | Use for |
|---|---|
| Fable (Claude, manager) | Briefs, review, decisions only. No heavy coding. |
| Codex CLI (gpt-6-astra) | Heavy coding: UE Python, Blender scripts, integrations. |
| Sonnet subagents | Research, docs, small scripts, running tests. |
| Opus | Architecture decisions, or after Codex fails twice on a task. |

## Tracking

Tasks live in `agents/tasks/NNN-slug.md` with sections: Goal / Acceptance criteria / Test command / Notes.
Copy `agents/tasks/000-template.md`. Run Codex with `agents/codex_task.ps1 <task.md> [-Effort medium]`.
Workers never commit; the manager reviews the diff and commits.
