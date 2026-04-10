---
name: vol3-build-surface
description: Use when the task depends on LaTeX builds, build logs, warning classification, targeted pytest runs, or deciding whether a Vol III change is actually verified. Do not use for purely conceptual work with no executable verification surface.
---

# Vol III Build Surface

Build output is evidence only after the surface is stable enough to trust.

## Standard prelude

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
```

Then choose the narrowest command that can falsify the change:

- `make fast`
- targeted `python3 -m pytest ...`
- direct log inspection
- cross-volume builds only when the claim really propagates across volumes

## Classification rules

- Fatal LaTeX error: actionable immediately.
- Undefined or stale reference: either a real label drift or a pass-order artifact; rerun only after classifying which.
- Build-log warning counts are not trustworthy on a corrupted aux surface.
- PDF/log noise in the worktree is not mathematical evidence.
- Test oracle mismatches are mathematics bugs or convention bugs until proved otherwise.
- Current Vol III dirty hotspots include `kappa_ch` versus `kappa_BKM`, local `P^2` class `M`, and restored level prefixes in CY `r`-matrices; read the live diff before trusting an old warning count.

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
