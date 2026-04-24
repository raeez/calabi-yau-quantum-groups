# Agent 5 report: HDYB and protected-trace holography

## Verdict

Attack survives against any reading of the primitive-envelope theorem as an
actual completed Hall-Drinfeld/Super-Yangian/BKM isomorphism or as an actual
pure mathematical holographic functor.  The attack is healed if the theorem is
read exactly as written: a formal free primitive envelope, with analytic
realisation as the remaining condition.

Recommended status:

- `thm:cy3-universal-primitive-envelope`: keep `ProvedHere` only for formal
  obstruction resolution.
- HDYB completed isomorphism: `Conditional` / `Conjectural` until the six
  comparison primitives, plus associator/R-matrix coherence, are constructed.
- Pure mathematical holography: `Conditional` until the complete bridge datum
  is constructed.

## Attacked Claim

The target claim is the platonic ideal resolution in
`chapters/theory/cy3_chain_level_bridge.tex`, especially
`thm:cy3-universal-primitive-envelope`, as applied to:

- the Hall-Drinfeld/Super-Yangian/BKM completed isomorphism;
- the pure mathematical protected-trace holography bridge.

The dangerous overread is: because the universal primitive envelope formally
adjoins primitives, PBW, coproduct, Borcherds-Serre, centre, completion, Hall
pairing, and product/orientation protected-trace coherence have been supplied
as actual completed-isomorphism data.

## Failure Mode

The manuscript blocks the overread, but only if the status parentheticals are
honored.

Local anchors:

- `chapters/theory/cy3_chain_level_bridge.tex:1882-1927`: the platonic
  resolution ledger separates executable normal form from global theorem
  closure.
- `chapters/theory/cy3_chain_level_bridge.tex:2032-2045`: HDYB is controlled
  by a completed double-comparison complex; a denominator identity or
  presentation is not a completed Hopf algebra.
- `chapters/theory/cy3_chain_level_bridge.tex:2047-2060`: pure mathematical
  holography requires a symmetric-monoidal protected-trace coherence complex.
- `chapters/theory/cy3_chain_level_bridge.tex:2116-2129`: local/numerical data
  do not imply compact bridge closure without primitives compatible with
  completion and orientation.
- `chapters/theory/cy3_chain_level_bridge.tex:2149-2205`: the theorem freely
  adjoins generators `h_{j,a}` with `d h_{j,a}=o_{j,a}`; this is formal, not
  analytic construction.
- `chapters/theory/cy3_chain_level_bridge.tex:2208-2236`: the proof kills the
  classes inside the extended complex and then explicitly defers actual
  compact theorem status to realization by named geometric/analytic data.

The compute oracle confirms this split:

- `compute/lib/cy3_platonic_bridge.py:75-109`: global witness requirements
  list the missing HDYB and holography data.
- `compute/lib/cy3_platonic_bridge.py:193-230`: the attack ledger identifies
  the invalid shortcuts and healed data.
- `compute/lib/cy3_platonic_bridge.py:667-760`: the universal primitive system
  sets `analytic_realisation=False` for every primitive certificate.
- `compute/lib/cy3_platonic_bridge.py:800-831`: gate status can close as
  normal form, but `unconditional_global_theorem_claims()` is empty.
- `compute/tests/test_cy3_platonic_bridge.py:148-161` and `199-213`: tests
  enforce separation of normal form from global theorem and formal closure from
  analytic realisation.

## HDYB Witnesses Still Missing

The actual completed isomorphism requires the following algebraic witnesses.
They are not supplied by the formal primitive envelope.

1. PBW filtration comparison: a finite-height associated-graded isomorphism
   between compact Hall primitives and the Borcherds root spaces, with no
   extra primitive generators or relations.
2. Hall coproduct comparison: the Drinfeld-new Hall coproduct with
   semiclassical cobracket equal to the `Delta_5`-regulated Lie bialgebra
   cobracket and associated graded equal to the primitive enveloping
   coproduct.
3. Borcherds-Serre ideal compatibility: the kernel of the current
   presentation is exactly the completed Borcherds-Serre ideal, including the
   quantum corrections of the chosen current presentation.
4. Centre and completion compatibility: no extra central primitives from
   orientation lines, determinant twists, or chambers; same pro-Borcherds-cone
   topology on both sides.
5. Hall pairing nondegeneracy: positive and negative compact halves with the
   radical quotient fixed and normalised against the invariant Borcherds form.
6. Associator and R-matrix coherence: the same Siegel-Borcherds associator
   class and convergent dynamical R-matrix in the chosen topology.

Supporting anchors:

- `chapters/examples/k3e_bkm_chapter.tex:1306-1321`: compact CoHA/Hall-to-
  Borcherds comparison is still a problem.
- `chapters/examples/k3e_bkm_chapter.tex:1372-1423`: PBW, Serre, and primitive
  coproduct are theorem-grade only on the Borcherds finite core; this is not
  the completed double.
- `chapters/examples/k3e_bkm_chapter.tex:1440-1527`: the
  Hall-Drinfeld/Super-Yangian equivalence is a criterion requiring root
  grading, PBW, pairing, coproduct, Serre, centre, and
  completion/associator.
- `chapters/examples/k3e_bkm_chapter.tex:1530-1551`: compact CoHA, if
  constructed, is bialgebra; Hopf structure lives on the Drinfeld double with
  comparison data.
- `chapters/theory/cy3_chain_level_bridge.tex:1751-1800`: the local
  Hall-Borcherds bialgebra datum includes coproduct, associator, dynamical
  R-matrix, CHL equivariance, and denominator normalisation.
- `compute/lib/cy3_platonic_bridge.py:475-508`: the finite oracle records
  booleans for coproduct/pairing/associator/R/CHL data, not explicit maps,
  kernels, centre maps, or topological inverse systems.

Residual manuscript risk: the HDYB primitive list in
`chapters/theory/cy3_chain_level_bridge.tex:2032-2045` names PBW, coproduct,
Serre, centre, completion, and pairing, but the fuller local criterion also
requires associator and R-matrix coherence.  If "completion" is intended to
absorb associator/R data, integration should say so explicitly.

## Holography Witnesses Still Missing

The pure mathematical protected-trace bridge is not produced by the physical
index equality or by the finite oracle.  It requires:

1. an exact charge-preserving functor
   `H_X: BPS_X -> Bdry_X`;
2. Hall convolution to boundary OPE/factorisation product comparison;
3. orientation-line trivialisation compatible with Hall convolution;
4. wall-crossing square sending KS wall-crossing to MC gauge equivalence;
5. bulk coproduct to chiral Drinfeld-centre half-braiding compatibility.

Supporting anchors:

- `chapters/connections/cy_holographic_datum_master.tex:465-503`: definition
  of the complete pure mathematical bridge datum; charge lattice and character
  alone are shadows.
- `chapters/connections/cy_holographic_datum_master.tex:506-525`: the
  holographic bridge gate is conditional on the complete datum.
- `chapters/connections/cy_holographic_datum_master.tex:545-553`: removing
  product, orientation, or wall-crossing coherence breaks the implication.
- `chapters/connections/cy_holographic_datum_master.tex:556-568`: for
  `K3 x E` / CHL the functor, Hall-product/OPE comparison, and
  orientation-line coherence have not been constructed.
- `chapters/examples/k3e_bkm_chapter.tex:13717-13740`: the M-theory parent is
  theorem-grade only at the numerical character level; compact-CoHA character
  reading is conditional.
- `chapters/examples/k3e_bkm_chapter.tex:13753-13770`: the full protected
  local-operator / Super-Yangian statement is conjectural and includes PBW,
  coproduct, Serre, centre, completion, and Hall-pairing compatibilities.

Residual manuscript risk: the pure holography primitive list in
`chapters/theory/cy3_chain_level_bridge.tex:2047-2060` names product,
orientation, and wall-crossing.  The master holography datum also requires
coproduct/Drinfeld-centre half-braiding compatibility
(`chapters/connections/cy_holographic_datum_master.tex:499-501` and
`539-540`).  Integration should either add this explicitly or state that it is
included in the target completed chiral/BKM trace category.

## Cross-Checks

The surrounding quantum-group foundations agree with the attack:

- `chapters/theory/quantum_groups_foundations.tex:172-256`: PBW is a positive
  half theorem on constructed CoHA loci; the completed double needs negative
  half, Cartan, completion, and nondegenerate pairing.
- `chapters/theory/quantum_groups_foundations.tex:688-695`: CY-C at `d=3`
  remains conjectural; the only end-to-end verified local case is `C^3`.
- `chapters/theory/quantum_groups_foundations.tex:703-706`: CoHA supplies the
  positive half; the full quantum group comes through the Drinfeld double.
- `chapters/theory/quantum_groups_foundations.tex:729-785`: `Y^+`, `D(Y^+)`,
  and the Drinfeld centre live at distinct operadic levels.

## Tests and Computations Run

- `python3 -m pytest compute/tests/test_cy3_platonic_bridge.py -q`
  passed: `19 passed in 0.25s`.
- Direct oracle probe with `python3` returned:
  - `normal_form_status["Hall_Drinfeld_Super_Yangian_BKM"] =
    "proved_normal_form"`;
  - `normal_form_status["pure_mathematical_holography"] =
    "proved_normal_form"`;
  - `unconditional_global_theorem_claims = ()`;
  - `all_requested_global_theorems_close = False`;
  - `formal_global_primitive_closure = True`;
  - `analytic_global_primitive_closure = False`;
  - remaining HDYB obligations:
    `PBW filtration comparison`, `Hall coproduct comparison`,
    `Borcherds-Serre ideal compatibility`,
    `centre and completion compatibility`,
    `Hall pairing nondegeneracy`;
  - remaining holography obligations:
    `product-coherent protected trace functor`,
    `orientation-coherent BPS-to-chiral comparison`,
    `wall-crossing preservation`.

## Files Changed

- `notes/adversarial_swarm_20260424_primitive_envelope/agent_5_hdyb_holography.md`
  only.

No manuscript or compute files were edited.

## Remaining Open Questions

1. Should the HDYB global primitive requirement explicitly include
   associator/R-matrix coherence, matching the K3E criterion?
2. Should the pure holography global primitive requirement explicitly include
   coproduct/Drinfeld-centre half-braiding coherence?
3. Can the finite `HallBorcherdsBialgebraDatum` be strengthened from boolean
   flags to typed witnesses for maps, ideals, pairings, centre transport, and
   inverse-system topology without pretending to prove analytic closure?
