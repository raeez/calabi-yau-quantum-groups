# Compact oriented critical CoHA resolution

Date: 2026-04-24.

## Claim attacked

Attacked claim: the compact critical Hall/CoHA construction on
`K3 x E` follows from local PTVV/BBJ critical charts, the product
volume form, finite KS wall-crossing, or local Thom--Sebastiani.

Verdict: false as an unconditional construction.  These inputs kill
local pieces only.  The compact oriented critical Hall cosheaf exists
on the full DWR/Cech/Ran nerve exactly after the four primitive
obstructions
`(o_atlas, o_or, o_HN, o_TS)` vanish.

## Construction/failure mode

The added manuscript criterion isolates the compact Hall primitive from
the later hCS-to-Hall, Hall-BKM, and Hall-Drinfeld-double primitives.

| Coordinate | Status | Failure mode if not supplied |
|---|---|---|
| `o_atlas` | primitive | PTVV/BBJ gives local `(-1)`-shifted critical charts, not coherent refinement charts on every DWR/Cech/Ran simplex. |
| `o_or` | primitive | `Omega_K3 wedge Omega_E` fixes the CY trace branch, not the determinant-line square roots on all semistable charts and Hall extension correspondences. |
| `o_HN` | primitive | finite KS products do not pass to the compact completed Hall cosheaf without local HN finiteness / vanishing of the inverse-limit defect. |
| `o_TS` | primitive | local Thom--Sebastiani does not give global associativity across transported orientation lines and all triple disjoint Ran configurations. |

## File anchors

- `chapters/theory/gluing/sec_9_obstructions.tex:1246` adds the
  compact oriented critical Hall cosheaf subsection.
- `chapters/theory/gluing/sec_9_obstructions.tex:1257` defines the
  compact oriented critical Hall datum.
- `chapters/theory/gluing/sec_9_obstructions.tex:1323` states the
  iff criterion for the compact oriented critical Hall cosheaf.
- `chapters/theory/gluing/sec_9_obstructions.tex:1405` states the
  no-shortcut corollary.
- `chapters/theory/gluing/sec_9_obstructions.tex:2142` records the
  result in the section summary.

## Exact theorem added

`thm:compact-oriented-critical-hall-cosheaf-criterion`:
for `X = K3 x E` and fixed `(sigma,S)`, the completed vanishing-cycle
Borel-Moore assignment

```tex
tau |-> \widehat{\oplus}_{gamma}
H^{BM}_{G_{tau,gamma}}(Crit(f_{tau,gamma}),
phi_{f_{tau,gamma}}\otimes L_{tau,gamma})[s](t)
```

extends to a completed oriented critical Hall cosheaf of associative
algebras on the full DWR/Cech/Ran nerve if and only if

```tex
o_atlas = o_or = o_HN = o_TS = 0.
```

The theorem explicitly does not construct
`Theta^{or}_{hCS->Hall}`, the Hall-BKM comparison, or the compact
Hall-Drinfeld double.

## Verification run

Ran:

```bash
rg -n "label\\{(def:compact-oriented-critical-hall-datum|thm:compact-oriented-critical-hall-cosheaf-criterion|cor:no-shortcut-compact-hall|sec:compact-oriented-critical-hall-cosheaves)\\}" chapters/theory/gluing/sec_9_obstructions.tex
rg -n -F "o_{\\mathrm{atlas}}" chapters/theory/gluing/sec_9_obstructions.tex
rg -n -F "o_{\\mathrm{or}}" chapters/theory/gluing/sec_9_obstructions.tex
rg -n -F "o_{\\mathrm{HN}}" chapters/theory/gluing/sec_9_obstructions.tex
rg -n -F "o_{\\mathrm{TS}}" chapters/theory/gluing/sec_9_obstructions.tex
pytest compute/tests/test_compact_hall_construction_package.py -q
```

Result: labels and all four obstruction coordinates are present;
`12 passed in 0.06s`.  Full `make fast` was not run.

## Remaining primitive obligations

1. Construct the oriented critical atlas on every DWR/Cech/Ran simplex.
2. Construct the global determinant-line square-root branch with
   extension-correspondence transport.
3. Prove local HN finiteness for the compact charge/radius completion.
4. Prove full Thom--Sebastiani coherence with orientation transport on
   iterated Hall products and disjoint Ran configurations.
5. Only after these four are supplied should the next primitives
   `o_MC`, `o_gr`, `o_fact`, Hall-BKM, and double data be attacked.
