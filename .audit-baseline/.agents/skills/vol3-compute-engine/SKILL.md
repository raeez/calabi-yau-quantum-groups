---
name: vol3-compute-engine
description: Use when scaffolding, repairing, or extending a Vol III compute engine, test oracle, executable witness, or manuscript-backed numerical claim. Trigger on compute engine, scaffold tests, hardcoded value, oracle, executable witness, or add compute support.
---

# Vol III Compute Engine

Executable mathematics in this repo is part of the proof surface.

## Workflow

1. State the exact claim, invariant, and convention.
2. Record source and normalization in the engine docstring or comments.
3. Prefer exact arithmetic when the claim is exact.
4. Implement the smallest engine that exposes the mathematical claim clearly.
5. Add tests that do not merely replay the engine's own derivation.
6. Run the narrowest `pytest` slice that can falsify the engine.
7. Propagate any shared formula/status change into manuscript prose and cross-volume copies when relevant.

## Test discipline

- At least two independent verification paths for executable oracles.
- Prefer three when the value is load-bearing.
- Never update expected values from engine output.
- If the engine formula changes, audit nearby docstrings, comments, and tests for stale reasoning.

## Current Vol III traps

- `kappa_ch` versus `kappa_BKM` for `K3 x E`
- restored level prefixes in CY `r`-matrices
- local `P^2` is class `M`, not `L`
- `MF(W)` dimension uses `n - 2`
- cross-volume genus-2 graph counts now distinguish `7` total stable strata from `6` edge-bearing Feynman types

## File layout

- engines live under `compute/lib/`
- targeted tests live under `compute/tests/`
- if the result is load-bearing, the manuscript should either cite the engine or be independently auditable against it
