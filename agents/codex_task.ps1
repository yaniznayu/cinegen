param(
    [Parameter(Mandatory = $true)][string]$TaskFile,
    [string]$Effort = "medium"
)
$ErrorActionPreference = "Stop"
$root = (Resolve-Path "$PSScriptRoot\..").Path
$task = Get-Content -Raw -Path $TaskFile
$prefix = "You are a worker on the CineGen repo. Implement the task below, run its test command, and finish with a short summary of changed files and test results."
"$prefix`n`n$task" | codex exec --sandbox workspace-write -C $root -c "model_reasoning_effort=$Effort" -
Set-Location $root
git status --short
git diff --stat
