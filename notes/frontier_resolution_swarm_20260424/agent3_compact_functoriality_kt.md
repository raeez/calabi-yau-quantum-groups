# Agent 3: Compact CY3 PhiFA3 Functoriality and KT Formality

Date: 2026-04-24

## Claim Attacked

Global compact CY3 Stage-1 `PhiFA_3` functoriality and all-loop
Kontsevich--Tamarkin formality were tested against the strongest
chain-level requirement: every compact higher-loop BV obstruction must
come with an explicit primitive/nullhomotopy in the completed
renormalised deformation complex.  One-loop cancellation, local
formality on `R^3`, or cyclic `A_infty` data alone is not a witness.

## Verdict

The scoped obstruction complexes do not already contain geometric
nullhomotopies for compact CY3 higher obstructions.  They contain formal
receptacles and, in `cy3_chain_level_bridge.tex`, a universal primitive
envelope which adjoins primitives abstractly.  That is a valid formal
criterion, not a compact analytic construction.

The precise conditional criterion is:

For each loop order `ell`, let `o_ell(X,g,F)` be the renormalised BV
obstruction cocycle in the completed local functional/deformation
complex fixed by the compact CY3, gauge algebra, and Stage-1 formality
point.  Compact `PhiFA_3(D^b(Coh(X)))_F` exists through loop order `L`
only if for every `1 <= ell <= L` there is a DWR- and RG-compatible
primitive `h_ell` with `d_BV h_ell = o_ell`.

For `K3 x E`, `chi(K3 x E)=0` kills the one-loop Euler anomaly, but the
Atiyah tower pulls back from the K3 factor and is not killed by that
Euler calculation.  For the quintic, the two-loop target is the
Kodaira--Spencer slot `H^1(Q,T_Q) ~= H^{2,1}(Q)`, dimension `101`, not
the Kahler line and not an integral of `c_2(T_Q)^2`.

## Local Anchors

- `chapters/theory/cyclic_ainf.tex`: Stage-1 three-cocycle theorem is now
  conditional on a fixed Stage-1 `E_3` formality point and Costello--Li
  holomorphic witness.
- `chapters/theory/cyclic_ainf.tex`: added
  `prop:cycainf-compact-higher-loop-primitive-criterion`.
- `chapters/theory/cyclic_ainf.tex`: `K3 x E` all-loop KT formality now
  uses the primitive criterion and no longer claims a contractible
  `GRT_1(Q)` ambiguity.
- `chapters/theory/cy3_chain_level_bridge.tex`: object-level Stage-1
  envelope is explicitly separated from morphism-level functoriality and
  compact higher-loop nullhomotopies.
- `chapters/theory/m3_b2_obstruction.tex`: compact BV obstruction is now
  formal/perturbative only after a Cech contracting homotopy is supplied.
- `compute/tests/test_compact_cy3_e1_chain.py`: added executable
  all-loop gate showing that one-loop cancellation is not an all-loop
  certificate for `K3 x E` or the quintic.

## Proof/Obstruction

The proof is deformation-theoretic.  The compact hCS/BV theory is built
inductively in a complete filtered dg Lie algebra of local functionals.
At loop order `ell`, lower counterterms have already been fixed; the
failure of the QME/descent/factorisation equations is a closed
degree-one cocycle `o_ell`.  Adding a counterterm changes it by a
boundary.  Therefore the step closes exactly when `o_ell` is exact and
a primitive has been chosen compatibly on the DWR nerve.

The existing tests verify only the lower-level facts:

- Formal/local models have zero strict obstruction.
- Non-formal cyclic models have nonzero strict `[m_3,B^(2)]`.
- `K3 x E` and the quintic have non-vacuous higher targets, so higher
  loop vanishing is not forced by dimension.

No scoped file supplies the actual compact `h_ell` primitives.

## Files Changed

- `chapters/theory/cyclic_ainf.tex`
- `chapters/theory/cy3_chain_level_bridge.tex`
- `chapters/theory/m3_b2_obstruction.tex`
- `compute/tests/test_compact_cy3_e1_chain.py`
- `notes/frontier_resolution_swarm_20260424/agent3_compact_functoriality_kt.md`

## Tests Run

`python3 -m pytest compute/tests/test_compact_cy3_e1_chain.py compute/tests/test_ks_cyclic_minimal_obs_ainf.py compute/tests/test_obs_ainf_counterexample_search.py -q -m "not slow"`

Result: 198 passed, 1 deselected.

## Remaining Open Questions

1. Construct the actual compact higher-loop primitives `h_ell` for
   `K3 x E`, starting at `ell=2`, or prove a nonzero obstruction class.
2. Compute the quintic two-loop graph projection to `H^1(Q,T_Q)` and
   compare it with the image of local BV counterterms.
3. Prove morphism-level `PhiFA_3(f)` compatibility for compact kernels:
   braces, cyclic BV, envelope, holomorphic twist, DWR descent, and
   convolution cells must all commute.
