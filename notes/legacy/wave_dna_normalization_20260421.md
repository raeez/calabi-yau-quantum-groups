# Wave/DNA normalization — audit and rename map (2026-04-21)

## Scope

Cross-volume cleanup of bookkeeping vocabulary from manuscript prose,
labels, and filenames per the Chriss--Ginzburg north star
(`CLAUDE.md`). Bookkeeping vocabulary (``Wave N'', ``DNA strand Sk'',
``Pattern N'', ``AP-CY n'', ``HZ-n'', ``cache entry'') belongs in
`notes/`, commit messages, and `memory/` --- never in reader-facing
`.tex` under `chapters/`, `frame/`, `examples/`, `theory/`,
`connections/`, `bibliography/`, `appendices/`.

## Honest counts (before rectification)

| Volume | Manuscript `.tex` | Total `wave|DNA` hits | Inside `\label`/`\ref` | Prose (outside) |
|---|---|---|---|---|
| Vol I   | ~130 | 1191 | 879 | ~312 |
| Vol II  | ~120 |  660 | 576 |  ~84 |
| Vol III |  ~90 |  111 |  64 |  ~47 |

Additional prose-level violations tracked separately:

| Pattern | Vol I | Vol II | Vol III |
|---|---|---|---|
| `[Ww]ave\s*\d+` (prose) | — | — | — |
| `AP\d+` / `AP-CY\d*` | many | few | 4 |
| `Pattern \d+` | ~35 | 1 | 0 |
| `HZ-\d+` | 11 | 6 | 0 |
| `cache entry` | 1 | 0 | 0 |
| `inscrib*` (CG-voice violation) | — | — | — |

Total prose hits across three volumes: ~1156 lines across 179 files.
Label-level renames: 929 unique labels collapse under the normalization
rules below, with 40 collisions resolved by roman-numeral suffix.

## Top prose-hotspot files (for Chriss--Ginzburg rectification)

| Count | File |
|---|---|
| 70 | `chiral-bar-cobar/chapters/theory/derived_langlands.tex` |
| 50 | `chiral-bar-cobar/chapters/theory/chiral_climax_platonic.tex` |
| 45 | `chiral-bar-cobar/chapters/examples/w_algebras_deep.tex` |
| 34 | `chiral-bar-cobar/chapters/theory/theorem_B_scope_platonic.tex` |
| 34 | `chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex` |
| 32 | `calabi-yau-quantum-groups/chapters/theory/modular_trace.tex` |
| 31 | `chiral-bar-cobar/chapters/examples/lattice_foundations.tex` |
| 28 | `chiral-bar-cobar/chapters/frame/part_iv_platonic_introduction.tex` |
| 25 | `chiral-bar-cobar/chapters/connections/concordance.tex` |
| 24 | `chiral-bar-cobar/chapters/theory/shadow_tower_quadrichotomy_platonic.tex` |
| 24 | `chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex` |
| 21 | `chiral-bar-cobar/chapters/examples/deformation_quantization.tex` |

## Normalization rules (label/ref bodies only)

Applied iteratively until fixed-point, inside
`\label{...}`, `\ref{...}`, `\eqref{...}`, `\autoref{...}`,
`\cref{...}`, `\Cref{...}`, `\pageref{...}`, `\nameref{...}`,
`\hyperref[...]{}`:

```
-wave\d+-DNA-(\w)   →  -\1
-DNA-wave\d+-(\w)   →  -\1
-DNA-(\d+)          →  -\1
-DNA-(\w)           →  -\1
-wave\d+-(\w)       →  -\1
-wave\d+-DNA$       →  -supplement
-DNA-wave\d+$       →  -supplement
-wave\d+$           →  -supplement
-DNA$               →  -supplement
(:)wave\d+-(\w)     →  :\2
(:)DNA-(\w)         →  :\2
(:)wave\d+$         →  :supplement
(:)DNA$             →  :supplement
```

Collision resolution: when multiple old labels normalize to the same
target, apply roman-numeral suffixes `-ii`, `-iii`, `-iv`, ordered by
wave number (lower first). When the target is already a clean
pre-existing label, all wave/DNA siblings shift to `-ii`, `-iii`, ...
starting after the existing.

## Full rename map

The complete 929-entry map lives alongside this file in
`wave_dna_rename_map_20260421.txt`. Grep by old label to find its new
target. This preserves the bridge back to wave/DNA-era identifiers for
anyone tracing a claim's origin through commit history.

## Procedure

1. Save this audit + map (done: this file + `wave_dna_rename_map_20260421.txt`).
2. Apply the label rewrite across all three volumes via
   `/tmp/normalize_labels.py --apply`.
3. Compile Vol III to confirm no regressions (and then Vol I, Vol II).
4. Rectify prose-level violations in CG voice, starting with the
   hotspot files above. Each file is handled independently and should
   be a self-contained commit.

## What this does NOT touch

- Prose text outside `\label{...}`/`\ref{...}` (e.g.\ ``following
  Wave~19's synthesis''). These require semantic rewriting in
  Chriss--Ginzburg voice, not mechanical stripping.
- Filenames (e.g.\ `compute/lib/k3_yangian_wave2_*.py`). Renaming these
  cascades into module imports and is deferred.
- `notes/`, `FRONTIER.md`, commit messages, `memory/` --- these are
  the legitimate homes for bookkeeping vocabulary and are out of scope.
