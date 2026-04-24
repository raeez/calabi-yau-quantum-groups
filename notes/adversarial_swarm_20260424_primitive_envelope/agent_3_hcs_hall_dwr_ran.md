# Agent 3 Report: hCS--Hall DWR/Ran Primitive Envelope

Date: 2026-04-24

Scope: attack the platonic ideal resolution of the hCS-to-Hall bridge in
`chapters/theory/cy3_chain_level_bridge.tex`, against the compute oracle
`compute/lib/cy3_platonic_bridge.py` and the local normal-form witnesses.

## Attacked Claim

The dangerous reading is:

> The universal primitive envelope has constructed actual chartwise
> hCS-to-Hall quasi-isomorphisms on the DWR/Ran nerve, together with the
> five nullhomotopies for Maurer--Cartan, orientation, grading,
> Thom--Sebastiani, and factorisation.

## Verdict

False as an analytic/geometric construction. True only as a formal
obstruction envelope.

The manuscript mostly states the scope honestly: the hCS-to-Hall
comparison is an open problem and the K3 x E DWR/Ran theorem is
conditional on supplied comparison data. The compute oracle confirms the
same split: it can freely adjoin primitive symbols and make finite
normal-form tests pass, but it does not realise the primitives as actual
renormalised hCS-to-Hall maps or DWR/Ran nullhomotopies.

The only constructed hCS-to-Hall map I found is the positive torus-fixed
abelian finite-mode C3 shuffle chart. It does not extend to the full
renormalised hCS factorisation algebra and does not descend over a
non-affine DWR cover.

## Failure Mode

1. `compute/lib/cy3_bridge_normal_form.py:1` says directly that the module
   "does not construct the missing hCS-to-Hall map." The gate
   `hcs_hall_chart_map` is only a required typed gate
   (`compute/lib/cy3_bridge_normal_form.py:58`), and global hCS--Hall
   closure additionally requires DWR cover, MC descent, orientation,
   grading/Tate, Thom--Sebastiani, and factorisation descent
   (`compute/lib/cy3_bridge_normal_form.py:133`).

2. `compute/lib/cy3_platonic_bridge.py` constructs formal placeholders.
   `construct_oriented_dwr_ran_map` assigns strings
   `Theta_hCS_to_Hall^or[...]` to all simplices and installs
   `NullHomotopy(name, 0, 0)` for the five obstruction names
   (`compute/lib/cy3_platonic_bridge.py:305`). This checks coverage and
   equality of residuals to boundaries, but it never builds source/target
   complexes, a renormalised differential, a Hall correspondence, or a
   chain homotopy.

3. The universal primitive envelope is explicitly formal:
   `universal_formal_primitive_system` freely adjoins certificates with
   `obstruction_residual=1`, `boundary_of_primitive=1`, and
   `analytic_realisation=False`
   (`compute/lib/cy3_platonic_bridge.py:720`). Therefore
   `formal_global_primitive_closure()` is expected to be true while
   `analytic_global_primitive_closure()` is false
   (`compute/lib/cy3_platonic_bridge.py:747`).

4. The aggregate package can report `is_exact()` because it uses the
   formal DWR map and zero formal nullhomotopies
   (`compute/lib/cy3_platonic_bridge.py:763`, `compute/lib/cy3_platonic_bridge.py:837`).
   The later API correctly protects global theorem status:
   `unconditional_global_theorem_claims()` returns `()`
   (`compute/lib/cy3_platonic_bridge.py:828`).

5. The test suite encodes the same formal/analytic distinction:
   `test_frontier_realisation_separates_normal_form_from_global_theorem`
   checks that global theorem closure is false
   (`compute/tests/test_cy3_platonic_bridge.py:148`), and
   `test_universal_primitive_envelope_does_not_fake_analytic_realisation`
   checks that analytic closure is false with all global obligations still
   remaining (`compute/tests/test_cy3_platonic_bridge.py:208`).

## Manuscript Anchors

- Open problem: `chapters/theory/cy3_chain_level_bridge.tex:1039` asks to
  construct the quasi-isomorphic oriented comparison datum on the whole
  DWR/Ran nerve and lists the seven required properties.
- Descent obstruction: `chapters/theory/cy3_chain_level_bridge.tex:1099`
  defines the total Cech convolution dg Lie algebra and the five-component
  obstruction tuple.
- Descent criterion: `chapters/theory/cy3_chain_level_bridge.tex:1152`
  proves that chartwise quasi-isomorphisms extend globally iff the
  obstruction tuple vanishes and the degree-zero MC element is invertible
  on every DWR object.
- Formal primitive envelope: `chapters/theory/cy3_chain_level_bridge.tex:2149`
  proves the free dg extension `d h_{j,a}=o_{j,a}` and states that
  analytic realisation is the remaining condition.
- Local C3 status: `chapters/theory/cy3_chain_level_bridge.tex:2579`
  is conditional on a supplied chartwise hCS--Hall map; `:2925` proves
  only the fixed abelian finite-mode chart; `:2983` leaves
  renormalised extension and descent.
- K3 x E DWR/Ran status: `chapters/theory/cy3_chain_level_bridge.tex:3266`
  is conditional on supplied chartwise quasi-isomorphisms and vanishing of
  the five obstruction classes.
- Toric CoHA guardrail: `chapters/examples/toric_cy3_coha.tex:83`
  isolates orientation, compact support, shifts, Tate twists, and
  completion as extra data for hCS comparison; `:120` says the C3 Hall
  object is a positive-half shadow, not the factorisation algebra itself;
  `:290` keeps CoHA associative and separate from chiral/OPE structure.

## Exact Missing Primitives

For the hCS--Hall DWR/Ran gate, the missing data are not just two
high-level certificates. They must split into the following actual
objects on the DWR/Ran nerve:

- `theta = {Theta_sigma}`: a degree-zero continuous natural
  transformation in
  `Tot Cech^bullet(U, Hom_cont(Obs_hCS^q, CoHA_crit^or))`.
- `h_MC`: a primitive with
  `d h_MC = d theta + (1/2)[theta, theta]`.
- `h_or`: a Cech primitive trivialising the relative determinant-line
  square-root mismatch.
- `h_gr`: a primitive for the integer shift and Tate-twist mismatch.
- `h_TS`: a homotopy between the two Thom--Sebastiani parenthesisations
  after transport by `theta`.
- `h_fact`: a homotopy showing disjoint-union factorisation compatibility:
  `Theta_{sigma1 sqcup sigma2} mu_BV` equals
  `mu_Hall^{TS,o}(Theta_sigma1 tensor Theta_sigma2)` up to the displayed
  chain homotopy.

The current oracle adjoins these formally. It does not produce them from
renormalised hCS propagators, vanishing-cycle transport, or Hall
correspondences.

## First-Principles Comparison Map

The repair target should be the following map, simplex by simplex.

For a DWR/Ran simplex
`sigma=(i0,...,ip; P1,...,Pr)` with support `|sigma|`, charge vector
`gamma`, and local quiver-with-potential `(Q_sigma,W_sigma)`, define
the component

```tex
\Theta_{\sigma,\gamma}(\mathcal O)
  =
  (p_{\sigma,\gamma})_!
  \left(
    \operatorname{ev}_{\sigma,\gamma}(\mathcal O_{\mathrm{ren}})
    \cap
    \left[\phi_{\operatorname{Tr}W_{\sigma,\gamma}}
      \otimes \mathscr L_{o_{\sigma,\gamma}}\right]
  \right)[s(\sigma,\gamma)](t(\sigma,\gamma)).
```

Here `ev_{sigma,gamma}` evaluates the renormalised hCS observable on the
universal Maurer--Cartan field in the local derived critical chart;
`phi_{Tr W}` is the vanishing-cycle complex; `L_o` is the Joyce/KS
orientation local system; `p_!` is the Hall/stack Borel-Moore pushforward;
and the sum over `gamma` is completed in the charge/HN/equivariant
topology.

On the torus-fixed C3 chart this must reduce to the existing finite
shuffle formula: `J_r -> z_1^r`, extended by the Schiffmann--Vasserot
kernel. On a full chart it must additionally commute with the
renormalised BV differential, not merely the zero differential of the
fixed finite-mode model.

## Obstruction-Killing Criterion

The bridge closes only if the above `Theta_sigma` satisfies all of:

1. Each `Theta_i` on a 0-simplex is a continuous quasi-isomorphism after
   the stated hbar-adic, strong-dual, charge/HN-adic, and equivariant
   completions.
2. The MC residual
   `R_MC = d theta + (1/2)[theta,theta]` is exact in the completed DWR/Ran
   mapping dg Lie algebra, with primitive `h_MC`.
3. The relative orientation, grading/Tate, Thom--Sebastiani, and
   factorisation residuals are exact by the four primitives
   `h_or, h_gr, h_TS, h_fact`.
4. These primitives are compatible with the same completions and
   orientation transports as the maps themselves.
5. The resulting degree-zero MC element is invertible in `H^0` on every
   object of the DWR nerve.

Equivalently: the five classes in
`H^*(g_{hCS,Hall}^{Ran})` must vanish because actual cochains built from
the comparison map have those coboundaries, not because a free dg
extension declared new variables with `d h = o`.

## Recommended Claim Status

- `thm:cy3-universal-primitive-envelope`: keep as `ProvedHere` only with
  the current qualifier "formal obstruction resolution; analytic
  realisation is the exact remaining condition." Do not cite it as an
  hCS--Hall construction theorem.
- Actual hCS--Hall DWR/Ran comparison on K3 x E: `Conditional/Open`
  until the first-principles `Theta_{sigma,gamma}` above is constructed
  and the five primitives are realised on the full nerve.
- `cy3_platonic_bridge.py`: interpret as a normal-form/obstruction-ledger
  oracle. Its `CompleteCY3BridgePackage.is_exact()` should not be used
  without the neighbouring `analytic_global_primitive_closure() is False`
  guard.

## Tests and Computations Run

- `pytest -q compute/tests/test_cy3_platonic_bridge.py compute/tests/test_cy3_bridge_normal_form.py compute/tests/test_c3_hcs_hall_theta.py`
  passed: 36 tests.
- `python3` oracle check:
  `formal_global_primitive_closure == True`;
  `analytic_global_primitive_closure == False`;
  oriented hCS--Hall missing analytic obligations are exactly
  `chartwise hCS-to-Hall quasi-isomorphisms` and
  `MC, orientation, grading, Thom-Sebastiani, factorisation nullhomotopies`.

## Files Changed

- Added this report only:
  `notes/adversarial_swarm_20260424_primitive_envelope/agent_3_hcs_hall_dwr_ran.md`.

## Remaining Open Questions

1. Does the displayed `Theta_{sigma,gamma}` define a continuous chain map
   on the full renormalised hCS observable factorisation algebra?
2. Does it give a quasi-isomorphism on every DWR 0-simplex after the
   specified completions?
3. Can the five primitives be built from BV propagator homotopies,
   orientation-line transports, Tate/shift cochains, Thom--Sebastiani
   comparison, and disjoint-union factorisation, rather than freely
   adjoined?
4. For generic non-toric K3, what replaces the fixed-point C3 shuffle
   formula: a Morse gradient-flow sum, and does it satisfy the same five
   obstruction equations?
