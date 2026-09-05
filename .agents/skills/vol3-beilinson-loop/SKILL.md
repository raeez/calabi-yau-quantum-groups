---
name: vol3-beilinson-loop
description: Use when auditing, rectifying, falsifying, converging, or pressure-testing theorem, proof, formula, status, or scope material in the Calabi-Yau Quantum Groups repository. Trigger on audit, rectify, red-team, Beilinson, theorem status, proof gap, convergence, or "is this actually proved?" tasks.
---

# Vol III Beilinson Loop

Read `AGENTS.md` first. This skill is the triggered deep workflow for hostile mathematical review.

## Surface

Work on the live manuscript surface:

- `main.tex`
- currently `\input`-ed files
- the dirty git diff
- relevant build logs
- the narrowest relevant `compute/tests/` slice

## Passes

Cover these review dimensions as applicable, without a fixed pass count:

- `RED`: logic, formulas, signs, hypotheses, scope, status honesty
- `BLUE`: collisions across intro/chapter/examples/appendices/compute/tests/README/other volumes
- `GREEN`: missing definitions, dangling references, frontier gaps, and over-advertised objects

## Rectification Rules

- Fix in dependency order.
- Re-read local context before each edit.
- After each material fix, run the narrowest falsifying verification.
- Propagate verified shared changes in assigned repositories. Return exact downstream obligations elsewhere.
- Treat `AP40`, `AP43`, `AP-CY6`, `AP-CY7`, `AP-CY8`, and `AP49` as mandatory checks.

## Exit Rule

Report the supported outcome:

- `CONVERGED`: no known actionable findings remain within the requested scope on the modified surface and the relevant verification passes.
- `BLOCKED`: exact unresolved obligation, supporting evidence, attempted routes, and next discriminating step named.

A bounded investigation may finish with the exact unresolved obligation, tried routes, evidence, and next discriminating step. Do not report an unresolved theorem as proved.
