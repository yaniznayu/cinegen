#!/usr/bin/env bash
# Usage: agents/codex_task.sh <task.md> [effort]
set -euo pipefail
TASK="${1:?task file required}"
EFFORT="${2:-medium}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PREFIX="You are a worker on the CineGen repo. Implement the task below, run its test command, and finish with a short summary of changed files and test results."
{ printf '%s\n\n' "$PREFIX"; cat "$TASK"; } | codex exec --sandbox workspace-write -C "$ROOT" -c "model_reasoning_effort=$EFFORT" -
cd "$ROOT"
git status --short
git diff --stat
