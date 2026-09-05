---
name: vol3-pre-edit-verification
description: Use before editing any high-risk Vol III formula, theorem status, d=3 existence claim, compute oracle, or cross-volume convention bridge. This is the Codex-native analogue of the Claude-side pre-edit verification templates.
---

# Vol III Pre-Edit Verification

Before changing a high-risk claim, establish the evidence listed in the relevant template below. Record a concise decision and source anchors outside the manuscript. The templates are optional formats.

If proof support is missing or a boundary check fails, investigate and repair it before promoting the claim. Continue independent authorized work.

## Triggers

- `r`-matrix or OPE/lambda-bracket edit
- `kappa` or modular-characteristic edit
- bar/cobar/desuspension formula
- theorem environment or claim-status edit touching d=3 objects
- shadow-class or SC-formality edit
- `MF(W)` CY-dimension edit
- cross-volume Part reference or copied formula
- compute/test oracle update

## Templates

### `r`-matrix

```text
## PRE-EDIT: r-matrix
family:
formula:
level parameter:
k=0 check:
source:
wrong variants avoided:
verdict:
```

### `kappa`

```text
## PRE-EDIT: kappa
object:
approved subscript:
formula:
source:
boundary checks:
wrong variants avoided:
verdict:
```

### d=3 status / existence

```text
## PRE-EDIT: d=3 status
statement:
depends on unconstructed object?:
environment:
claim status:
dependency chain:
verdict:
```

### shadow class

```text
## PRE-EDIT: shadow class
object:
leading-order evidence:
full-tower evidence:
claimed class:
shallower-class failure:
verdict:
```

### `MF(W)` dimension

```text
## PRE-EDIT: MF(W)
W: A^n -> A^1 with n =
claimed CY dimension:
n-2 check:
example sanity check:
verdict:
```

### compute oracle

```text
## PRE-EDIT: compute oracle
claim:
path 1:
path 2:
path 3:
source and normalization:
engine/test independence:
verdict:
```

## Non-negotiables

- This block belongs in commentary, not in manuscript files.
- Use live source, not remembered formulas.
- If evidence rejects the proposed claim, repair the argument or identify the unresolved obligation before promotion.
