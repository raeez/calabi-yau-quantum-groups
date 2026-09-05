---
name: vol3-build-surface
description: Use when the task depends on LaTeX builds, build logs, warning classification, targeted pytest runs, or deciding whether a Vol III change is actually verified. Do not use for purely conceptual work with no executable verification surface.
---

# Vol III Build Surface

Build output is evidence only after the surface is stable enough to trust.

## Isolated verification

Run builds after a coherent authorized change, in the assigned worktree. No additional build opt-in is needed.
Run one build at a time in that worktree because output and logs are shared within it.
The existing `scripts/build.sh` uses isolated auxiliary directories. From the worktree, `make fast` builds legacy `main.tex`.
The current default target, `make platonic`, builds `platonic/main.tex`. Choose the entry point containing the changed source.
Inspect its actual input graph. A legacy build does not verify the integrated manuscript.
Do not invoke release, iCloud, publication, cleanup, or cross-repository targets as a local verification shortcut.
Never use process-name killing. If necessary, stop only a process created by this task, after checking its PID and ownership.
Request graceful termination first and confirm its state before considering forced termination of that same owned process.

Choose the narrowest falsifying check:

- the applicable explicit local Make target
- targeted `python3 -m pytest compute/tests/<affected-test>.py`
- direct log inspection
- cross-volume builds only in assigned worktrees when the claim requires them

## Classification rules

- Fatal LaTeX error: actionable immediately.
- Undefined or stale reference: either a real label drift or a pass-order artifact; rerun only after classifying which.
- Build-log warning counts are not trustworthy on a corrupted aux surface.
- PDF/log noise in the worktree is not mathematical evidence.
- Test oracle mismatches are mathematics bugs or convention bugs until proved otherwise.
- Read the live diff and input graph before trusting historical warning counts.

## Workflow

1. Stabilize the build surface.
2. Run the narrowest falsifying build/test command.
3. Classify failures into:
   - manuscript error
   - compute error
   - convention mismatch
   - stale aux/log artifact
   - expected cross-volume warning
4. Fix only after classification.

## Reporting standard

- Paraphrase the decisive failure signature.
- Distinguish persistent failures from pass-1 noise.
- If concurrent workers or stale artifacts make the logs race-prone, say so explicitly.
