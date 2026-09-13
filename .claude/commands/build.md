---
description: "Build Vol III, run tests"
---

# Build Vol III

Run from the root of the assigned isolated worktree. Read
`.agents/skills/vol3-build-surface/SKILL.md` before building.
Run one build at a time in that worktree. The build script isolates auxiliary
files and leaves other worktrees' processes alone.

`make fast` builds the legacy `main.tex` entry point. Use `make platonic`
when the changed source belongs to the integrated manuscript instead.
Inspect the selected target's exit status and logs before treating it as verified.

```bash
set -e
make fast
python3 -m pytest compute/tests/ -x --tb=short -q
```

If a build started by this task needs termination, use its recorded tool handle
or launch PID. Check that PID's command, start time, parent, and working directory
against the original launch record. For a recorded shell PID, inspect with:

```bash
ps -p "$build_pid" -o pid=,ppid=,lstart=,command=
lsof -a -p "$build_pid" -d cwd
```

Only after confirming ownership, request graceful termination through the tool
handle or `kill -TERM "$build_pid"`. Recheck that same handle or PID to confirm
its state. Never terminate processes by name or stop another task's build.
Retain build and test failures with their original output and exit status.
