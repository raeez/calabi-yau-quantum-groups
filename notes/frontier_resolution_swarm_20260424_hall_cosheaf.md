# Frontier resolution lane 1: compact Hall cosheaf and hCS-to-Hall descent

Date: 2026-04-24.

## Claim Attacked

Attacked claim: for compact `K3 x E`, the local DWR/Cech/Ran Hall
package already constructs the compact oriented critical Hall cosheaf,
the full-nerve
`\Theta^{or}_{hCS->Hall}`, and the identity
`Dec(T_DWR(path)) = Ad_KS(path)`, hence closes the compact CY3 apex
unconditionally.

Verdict: false as an unconditional statement.  The strongest truthful
result is a supplied-datum theorem.  The local sources prove a descent
criterion and a finite-first wall-crossing compatibility once the
oriented critical atlas, coherent orientation branch, locally finite HN
completion, local stationary-phase Maurer-Cartan maps, and motivic
integration functoriality have been supplied.

## Proved Core

1. `working_notes.tex` defines the compact CY3 bridge package
   `\mathfrak D_X` with DWR/Cech/Ran cover, oriented critical Hall
   atlas, orientation branch, HN completion, motivic integration,
   hCS-to-Hall MC solution, and later Hall-BKM/double data
   (`working_notes.tex:2786`).  Its obstruction vector separates the
   Hall-cosheaf coordinates from the global `Theta` coordinates
   (`working_notes.tex:2815`).

2. The apex closure theorem is an equivalence criterion, not an
   existence theorem: if the whole obstruction vector vanishes, the
   listed objects exist and commute with descent, completion, and
   wall-crossing; conversely, such objects force the vector to vanish
   (`working_notes.tex:2840`).  The primitive questions immediately
   afterward still require construction of
   `\mathfrak U, \mathfrak C, o_X, HN` and of `\theta`
   (`working_notes.tex:2913`).

3. The hCS-to-Hall comparison is still an explicit open problem at the
   source level (`chapters/theory/cy3_chain_level_bridge.tex:1039`).
   The proved theorem is the descent criterion: chartwise
   quasi-isomorphisms extend to a global orientation-preserving morphism
   iff the obstruction tuple vanishes and the resulting degree-zero MC
   class is invertible in `H^0` on every DWR object
   (`chapters/theory/cy3_chain_level_bridge.tex:1152`).

4. The compact Hall cosheaf construction in `sec_10_unifying.tex` is
   conditional on atlas, orientation, and locally finite HN data
   (`chapters/theory/gluing/sec_10_unifying.tex:578`).  The cosheaf
   axioms are exactly the vanishing of
   `(o_atlas, o_or, o_HN, o_TS)`
   (`chapters/theory/gluing/sec_10_unifying.tex:660`).

5. The full-nerve equations for `Theta` and the wall-crossing identity
   are conditional on `theta`, motivic integration, and the HN
   completion (`chapters/theory/gluing/sec_10_unifying.tex:671`).
   Finite truncations give
   `Int^{mot}_{N,R} T^{DWR}_{wp,N,R} =
   Ad_{KS_{wp,N,R}} Int^{mot}_{N,R}`; local HN finiteness is what
   permits the inverse limit to
   `Dec(T_DWR(wp)) = Ad_KS(wp)` (`chapters/theory/gluing/sec_10_unifying.tex:697`).

## Obstruction Coordinates

| Coordinate | Status | Reason |
|---|---|---|
| `o_atlas` | Survives. | No full oriented `(-1)`-shifted critical atlas on every DWR/Cech/Ran simplex is constructed. The formula becomes a cosheaf only after this atlas glues. |
| `o_or` | Partly normalized, still survives globally. | `K3 x E` has the product volume-form branch on the product-compatible locus, but triple-overlap orientation transport remains input data. It also reappears in the `Theta` comparison. |
| `o_HN` | Survives. | The HN sector completion must be locally finite for the cosheaf and for the inverse limit in wall crossing. The tests record this gate; they do not construct the finiteness theorem. |
| `o_TS` | Survives globally. | Thom-Sebastiani gives the required structure map once the atlas and orientation data exist, but coherence over triple disjoint configurations and compatibility with the comparison map are not supplied unconditionally. |
| `o_MC` | Survives. | No compact `K3 x E` stationary-phase map `theta` is constructed. The descent theorem only says what happens after a degree-zero MC solution is supplied. |
| `o_gr` | Survives. | Single-chart shifts/Tate twists can be fixed, but global compatibility of `s(tau,gamma)` and `t(tau,gamma)` under the comparison is part of the obstruction tuple. |
| `o_fact` | Survives. | The local product and Hall convolution are named; a global BV-product-to-Hall-convolution natural transformation on the full Ran nerve is not constructed. |
| descent `= KS` | Killed conditionally. | For a supplied motivic Hall cosheaf with functorial motivic integration and locally finite HN completion, the equality follows finite-first and then by inverse limit. It does not kill the preceding coordinates. |

## Proposed Final Theorem Statement

**Conditional theorem.**  Let `X = K3 x E`, fix a chamber-sector pair
`(sigma,S)`, and suppose there are:

- a DWR/Cech/Ran cover `\mathfrak U`;
- an oriented `(-1)`-shifted critical Hall atlas `\mathfrak C` on every
  simplex of the nerve;
- a coherent Joyce-Kontsevich-Soibelman orientation branch `o_X`,
  product-compatible with `Omega_K3 wedge Omega_E`;
- a locally finite HN completion on strict sectors;
- a functorial motivic integration map to the completed sector quantum
  torus;
- a degree-zero invertible Maurer-Cartan solution
  `theta in M_{hCS,Hall}(\mathfrak U)` whose orientation, grading/Tate,
  Thom-Sebastiani, and factorisation defects vanish.

Then the completed oriented critical Hall cosheaf
`\mathcal H^{mot,or}_{K3 x E,sigma,S}` exists on the full
DWR/Cech/Ran nerve; the local stationary-phase maps descend to a
continuous natural transformation
`\Theta^{or}_{hCS->Hall}` on that nerve; and for every admissible wall
path `wp`,
`Dec(T^{DWR}_{wp}) = Ad_{KS(wp)}` in the completed motivic quantum
torus.  At the Igusa boundary, the decategorified positive geometry
uses the Lorentzian chamber, orientation character, and denominator
normalisation of `Delta_5`, giving
`\kappa_{BKM}(g_{Delta_5}) = c_1(0)/2 = 5`.

This theorem does not construct the compact Hall-Drinfeld double, does
not identify a positive-half homotopy colimit with the double, and does
not turn the hCS-to-Hall comparison into an unconditional compact CY3
closure theorem.

## Proof Skeleton

1. The obstruction ledger in `working_notes.tex` identifies the first
   four coordinates with the Hall cosheaf and the next three with the
   global `Theta` comparison (`working_notes.tex:2828`).

2. Given atlas, orientation, and HN data, the construction in
   `sec_10_unifying.tex` assigns the completed vanishing-cycle
   Borel-Moore group to each DWR object and uses refinement
   correspondences, disjoint Ran factorisation, and Hall extension
   correspondences as structure maps
   (`chapters/theory/gluing/sec_10_unifying.tex:583`).

3. The cosheaf identities are precisely the vanishing of
   `(o_atlas, o_or, o_HN, o_TS)`, so the Hall cosheaf exists under
   those hypotheses (`chapters/theory/gluing/sec_10_unifying.tex:660`).

4. A chartwise family of hCS-to-Hall quasi-isomorphisms is a global
   morphism exactly when it solves the total Cech convolution MC
   equation and preserves orientation, grading, Thom-Sebastiani, and
   factorisation data
   (`chapters/theory/cy3_chain_level_bridge.tex:1099`,
   `chapters/theory/cy3_chain_level_bridge.tex:1152`).

5. Finite charge-height and central-charge-radius truncations make wall
   transport a finite product of Hall extension push-pulls.  Motivic
   integration sends that finite product to the finite KS product; HN
   local finiteness gives the inverse limit
   (`chapters/theory/gluing/sec_10_unifying.tex:723`).

6. The positive-cone theorem is the decategorified support/completion
   consequence of the supplied Hall cosheaf and motivic integration; it
   explicitly leaves the global hCS-to-Hall comparison and the double as
   additional frontier data
   (`chapters/theory/gluing/sec_10_unifying.tex:1705`).

## Primary Source Anchors Needed

The local theorem should not be upgraded beyond the cited local
criterion until these external anchors are checked at theorem/section
level:

- Pantev-Toen-Vaquie-Vezzosi, shifted symplectic structures on derived
  moduli of perfect complexes: source for the `(-1)`-shifted compact
  CY3 critical structure.
- Brav-Bussi-Joyce and Brav-Bussi-Dupont-Joyce-Szendroi: source for
  d-critical charts, orientation data, and compatibility of critical
  atlases.
- Joyce-Upmeier and Kontsevich-Soibelman: source for orientation data
  in DT/Hall constructions and determinant-line square roots.
- Kontsevich-Soibelman, `Stability structures, motivic DT invariants
  and cluster transformations`: source for motivic Hall products,
  wall-crossing, and finite KS products.
- Davison-Meinhardt: source for critical CoHA and vanishing-cycle
  Thom-Sebastiani/PBW technology in the oriented setting.
- Costello-Gwilliam and Costello-Li: source for quantum hCS
  factorisation observables and compact-support conventions.
- Toen-Vezzosi/Lurie descent for sheaves of stable infinity-categories:
  source for the Cech/Ran descent formalism used by the construction.
- Borcherds and Gritsenko-Nikulin: source for the `Delta_5`
  denominator normalisation and the weight formula
  `\kappa_{BKM}=c(0)/2`.

## Computations / Tests Run

Ran:

```bash
pytest compute/tests/test_compact_hall_construction_package.py -q
```

Result: `12 passed in 0.19s`.

The tests verify that no frontier gate is marked unconditional, that
the dependency order is
Hall cosheaf -> Hall-BKM -> compact double, that the double requires
the six extra double data, that `Theta` records the full-nerve
commuting equations, that wall crossing is finite-first, and that the
orientation obstruction overlap is intentional
(`compute/tests/test_compact_hall_construction_package.py:24`).

## Files Changed

Created this report only:

- `notes/frontier_resolution_swarm_20260424_hall_cosheaf.md`
