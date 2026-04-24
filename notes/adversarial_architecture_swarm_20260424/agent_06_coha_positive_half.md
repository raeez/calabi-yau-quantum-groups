# Agent 06: CoHA / Y^+ / Drinfeld Double

Scope: hostile audit of the CoHA positive-half lane against the failure modes
CoHA = W_{1+\infty}, unsupported Drinfeld doubles, missing equivariance
hypotheses, and CY-C overreach.

Files read:

- `CLAUDE.md`
- `AGENTS.md`
- `chapters/examples/toric_cy3_coha.tex`
- `chapters/examples/coha_wall_crossing_platonic.tex`
- `chapters/examples/cy_c_six_routes_convergence.tex`
- `chapters/examples/cy_c_six_routes_generator_level_platonic.tex`
- `chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex`
- `compute/lib/coha_e1_sector_engine.py`
- `compute/lib/coha_chart_explicit.py`
- `compute/lib/coha_non_cy_threefold.py`
- `compute/lib/coha_gluing_morphisms.py`
- `compute/lib/coha_drinfeld_bulk.py`
- `compute/lib/c3_envelope_comparison.py`
- `/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex`

Verdict:

The mathematical spine is mostly recoverable if every statement is kept at the
object level:

1. `CoHA(C^3) = Y^+(\widehat{\mathfrak{gl}}_1)` is an associative `E_1`
   positive-half statement.
2. `D(Y^+) = Y` is the full Yangian / Drinfeld-double statement, requiring a
   non-degenerate Hopf pairing.
3. `W_{1+\infty}` is a vertex-algebra / representation-target statement, not
   an isomorphic copy of the CoHA.
4. General toric statements require toric equivariance, CY3 quiver-with-potential
   hypotheses, and a proved pairing.
5. CY-C should be stated as a stratified pentagon / colimit convergence
   conjecture, not as an unqualified six-way isomorphism.

## ATTACK_1: CoHA = W_{1+\infty} relapse

Claim attacked: `CoHA(C^3)` is the same vertex algebra as `W_{1+\infty}`.

Failure mode:

- The manuscript already has the correct guard in
  `chapters/examples/toric_cy3_coha.tex:93-133`:
  `CoHA(C^3) = Y^+`, then `Y^+ -> Y`, then an evaluation representation on a
  `W_{1+\infty}` vacuum module. Lines `125-129` explicitly separate
  `CoHA(C^3) != Y`, `Y != W_{1+\infty}`, and
  `CoHA(C^3) != W_{1+\infty}`.
- `chapters/examples/toric_cy3_coha.tex:136-150` repeats the structural
  separation: the full Yangian appears only after the Drinfeld double.
- `chapters/examples/coha_wall_crossing_platonic.tex:1349-1417` gives the
  best local formulation: `Y^+` is not the full Yangian; the double supplies
  the missing `Y^0` and `Y^-` pieces.
- Stale compute prose still attacks the spine:
  `compute/lib/c3_envelope_comparison.py:3-9` says the factorization envelope,
  `W_{1+\infty}`, and `CoHA Y^+` should give the same vertex algebra.
  `compute/lib/c3_envelope_comparison.py:1002-1009` then says all three
  produce the same Heisenberg VOA while separately admitting that `CoHA`
  acts on a larger plane-partition space.
  `compute/lib/coha_e1_sector_engine.py:21-23` says
  `CoHA = Y^+`, `chiral = W_{1+\infty}` without the double/evaluation
  qualifier.
  `compute/lib/coha_non_cy_threefold.py:1388-1405` describes a direct
  `CoHA -> VA` state-field map, which is stronger than the manuscript's
  current object-level statement.

Executable check:

- `verify_character_factorization(12)` gives `factorization_match True`.
- `M(q)/P(q)` begins `[1, 0, 1, 2, 4, 6, 12, 18, 33]`.
- `compare_characters(12)` reports `macmahon_differs_from_euler True` with
  first difference at weight `2`.
- Prefixes: `Y^+ / CoHA` MacMahon coefficients `[1, 1, 3, 6, 13]`; W-algebra
  partition coefficients `[1, 1, 2, 3, 5]`.
- `AffineYangianGL1.verify_coha_isomorphism()` returns `True` for
  `Y^+ = CoHA(C^3)` at the character level.

## HEAL_1

Precise object-level statement:

`CoHA(C^3)` is `Y^+(\widehat{\mathfrak{gl}}_1)` as an associative
positive-half Hall algebra, with MacMahon character. The full affine Yangian is
the Drinfeld double
`D(Y^+) = Y^+ \otimes Y^0 \otimes Y^-`. The vertex algebra
`W_{1+\infty}` appears as an evaluation / Fock representation target of the
full doubled Yangian, with ordinary partition vacuum character at `N=1`.
Character equality or shared currents do not identify the CoHA with the vertex
algebra.

Status recommendation:

- Keep the manuscript guards.
- Later integration should rewrite the stale compute docstrings/comments in
  `c3_envelope_comparison.py`, `coha_e1_sector_engine.py`, and
  `coha_non_cy_threefold.py` so executable checks and prose say the same thing.

## ATTACK_2: unsupported Drinfeld doubles

Claim attacked: every positive-half CoHA in the toric/CY-C lane has a proved
Drinfeld double identified with a full affine (super) Yangian and hence an
`E_2` braided representation category.

Failure mode:

- `chapters/examples/coha_wall_crossing_platonic.tex:1371-1416` correctly
  states the scope: for general toric CY3 the double requires a non-degenerate
  Hopf pairing; this is proved for `C^3`, proved or modelled in specific
  examples, and conditional in general.
- `chapters/examples/toric_cy3_coha.tex:1431-1434` marks the toric chiral
  quantum group theorem conditional, but component (III) at
  `1478-1497` reads too strongly unless the reader imports the conditional
  warning.
- `chapters/examples/toric_cy3_coha.tex:1612-1631` gives the correct guard:
  `C^3` is proved; for general toric CY3 the Drinfeld-center-to-full-Yangian
  identification is CY-C restricted to the toric case.
- `chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex:542-589`
  claims `G(X)` for local `P^3` as `ClaimStatusProvedHere`, including a Hopf
  algebra double. But `Tot(K_{P^3})` has complex dimension `4`, not `3`;
  it is not a non-compact CY3. The proof invokes CY3 quiver-with-potential
  theorems across a dimension mismatch.
- `chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex:643-681`
  gives a stable-transfer theorem with the right ingredients
  (torus action, local type, equivariant parameter ring), but the Hopf
  conclusion still depends on the pairing and on the CY3 dimension.

## HEAL_2

Precise object-level statement:

For a CY3 quiver with potential in a toric equivariant regime,
`H(Q,W) = Y^+(\widehat{\mathfrak g}_Q)` is the positive-half theorem.
The Drinfeld double `D(H)` is a Hopf algebra and identifies with a full affine
super Yangian only when the Joyce / Hall pairing is constructed and
non-degenerate in the stated completion. The `E_2` braided category is then
`Rep^{E_2}(D(H))` or the Drinfeld center of `Rep^{E_1}(H)`, not a structure on
the positive half alone.

Status recommendation:

- General toric: `ClaimStatusConditional` unless the pairing and completion are
  named.
- `C^3`: proved on the cited SV / PR / center comparison.
- Local `P^3`: remove from CY3 examples or restate as CY4 with the correct
  `E_n` shift; do not use it as a CY3 CoHA witness.

## ATTACK_3: missing equivariance hypotheses

Claim attacked: the CoHA/Yangian/shuffle and stable-envelope statements survive
without toric or reduced equivariant hypotheses.

Failure mode:

- `chapters/examples/toric_cy3_coha.tex:1933-1968` explicitly lists where the
  toric hypothesis enters: existence of the CoHA realization, RSYZ
  identification, MO stable envelopes, and chart gluing.
- `compute/lib/coha_chart_explicit.py:829-856` hard-codes the shuffle product
  over equivariant parameters and the CY condition on the weights.
- `chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex:643-652`
  assumes an algebraic torus action and local toric/Fano type before the
  stable transfer.
- `chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex:754-791`
  correctly blocks compact CY3 transfer by absence of torus action and
  finite-quiver equivariance.
- Vol I cross-anchor
  `/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:5271-5281`
  contains a separate dimension-label hazard: local `P^2` is listed under a
  `CY-4` parenthetical, while Vol III treats `Tot(K_{P^2})` as a toric CY3.

## HEAL_3

Precise object-level statement:

The shuffle/Yangian CoHA statements require a toric or otherwise specified
equivariant stratum. For compact non-toric CY3s, the CoHA-quiver presentation
is not available by default; the stage-1 object is the factorization-envelope
or framed categorical output, and any stable-envelope / R-matrix / Drinfeld
double assertion must name its replacement equivariance source.

Status recommendation:

- Add or preserve hypotheses: smooth toric CY3 without compact 4-cycles;
  CY3 quiver with potential; algebraic torus action; equivariant cohomology
  base; non-degenerate Hopf pairing; chosen completion.
- Cross-volume integration should repair the local `P^2` dimension label in
  Vol I and exclude local `P^3` from CY3 CoHA evidence.

## ATTACK_4: CY-C six-way-isomorphism overreach

Claim attacked: CY-C says the six routes are pairwise isomorphic chiral algebras.

Failure mode:

- `chapters/examples/cy_c_six_routes_convergence.tex:87-90` still states a
  pairwise isomorphism of six route outputs.
- `chapters/examples/cy_c_six_routes_generator_level_platonic.tex:111-116`
  says route `R_2` is a BKM / automorphic source, not a chiral algebra; its
  bridge to `R_3` is character-level only.
- `chapters/examples/cy_c_six_routes_generator_level_platonic.tex:190-205`
  proves that no simultaneous isomorphisms can hold among the chiral route
  outputs because `rho^R` would force `3 = 24`.
- `chapters/examples/cy_c_six_routes_generator_level_platonic.tex:216-225`
  replaces six-way isomorphism by a conditional pentagon colimit.
- `chapters/examples/cy_c_six_routes_generator_level_platonic.tex:267-301`
  gives the correct conditional theorem: three strata, named intertwiners,
  colimit identification.
- `chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex:1237-1250`
  correctly restricts CY-C to the isotrivially fibred stratum where all six
  routes have inputs.

## HEAL_4

Precise object-level statement:

CY-C at generator level is not six-way isomorphism. It is a stratified diagram:
`R_2` is an automorphic / BKM character source, the five chiral outputs form a
pentagon with injections, surjections, and isomorphisms, and
`G(K3 x E)` is the conditional colimit / braided-center target after the named
intertwiners are constructed. Braided `E_2` convergence remains stronger than
the `E_1` chiral pentagon and is open beyond the abelian K3 level.

Status recommendation:

- Rewrite the central conjecture in `cy_c_six_routes_convergence.tex:87-90`
  to match the generator-level replacement.
- `thm:cy-c-abelian-K3` at
  `chapters/examples/cy_c_six_routes_convergence.tex:563-585` should be
  `ClaimStatusConditional`, not bare `ProvedHere`, because its last sentence
  is conditional on the Vol II K3 Heisenberg + ADE-enhanced cell-closure
  theorem.

## ATTACK_5: character identity promoted to structural identity on K3 x E

Claim attacked: `CoHA_{K3 x E}` or its character identity already constructs
the Hall-Drinfeld double / chiral BKM object.

Failure mode:

- `chapters/examples/toric_cy3_coha.tex:2124-2170` proves or records a
  character identity:
  `chi_gr(CoHA_{K3 x E}) = Z_DT^red(K3 x E) = 1/Phi_10`.
  The proof explicitly says the transport to `H_{Delta_5}` requires the
  K3-fibre Hall-Borcherds comparison and the CY3 hCS-to-Hall comparison.
- `chapters/examples/toric_cy3_coha.tex:2173-2184` correctly warns that a
  character identity does not identify the CoHA with a vertex algebra.
- `chapters/examples/toric_cy3_coha.tex:1970-1986` is stronger: it describes
  the non-toric Hall-Drinfeld double and its `Delta_5` classification as if
  Davison integrality plus the derived CY3 structure already supplies the full
  object.
- `chapters/examples/cy_c_six_routes_convergence.tex:1566-1568` calls the
  Hall-Drinfeld double conjectural but also says it is established as a
  theorem in the platonic chapter. That mixed status should be resolved at
  the exact object level.
- Vol I cross-anchor
  `/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:5250-5266`
  is consistent on the four K3 x E invariants but is only a scalar /
  coefficient anchor; it does not prove the CoHA-to-BKM structural lift.

## HEAL_5

Precise object-level statement:

For `K3 x E`, the reduced DT / Igusa character identity is a character-level
theorem. The Hall-Drinfeld double
`D_hbar(Y_hbar^Hall(CoHA_{K3 x E}))` is the candidate quantum-group object
for the CY-C meeting point only after the Hall-Borcherds comparison, the
hCS-to-Hall comparison, the pairing/completion data, and the braided-center
identification are supplied. Until then, the correct status is conjectural or
conditional, even when all scalar checks pass.

Status recommendation:

- Keep `thm:K3xE-coha-character-igusa` as character-level.
- Mark the structural Hall-Drinfeld double as conditional/conjectural unless
  the cited platonic theorem states the exact double, pairing, associator, and
  representation category.
- Do not call the BKM-side object a Drinfeld Yangian; it is a Hall-Drinfeld
  double candidate, distinct from the self-mirror K3 Yangian branch.

## Verification run

Commands run:

```bash
python3 - <<'PY'
import sys
sys.path.insert(0, 'compute/lib')
from c3_envelope_comparison import verify_character_factorization, compare_characters
from coha_chart_explicit import jordan_character_three_paths
from coha_drinfeld_bulk import AffineYangianGL1, cross_volume_shadow_coha

factor = verify_character_factorization(12)
chars = compare_characters(12)
jordan = jordan_character_three_paths(12)
yang = AffineYangianGL1(12)
shadow = cross_volume_shadow_coha(12)

print('factorization_match', factor['factorization_match'])
print('M_over_P', factor['ratio_coefficients'][:9])
print('walgebra_equals_euler', chars['walgebra_equals_euler_partitions'])
print('macmahon_differs_from_euler', chars['macmahon_differs_from_euler'])
print('first_difference_weight', chars['first_difference_weight'])
print('yangian_chars_prefix', chars['yangian_chars'][:5])
print('walgebra_chars_prefix', chars['walgebra_chars'][:5])
print('jordan_all_match', jordan['all_match'])
print('Yplus_CoHA_match', yang.verify_coha_isomorphism()['match'])
print('shadow_bridge', shadow['bridge'])
print('shadow_coha_M', shadow['coha_character_M'][:5])
print('shadow_yangian_M2P', shadow['yangian_character_M2P'][:5])
PY
```

Output summary:

- `factorization_match True`
- `M_over_P [1, 0, 1, 2, 4, 6, 12, 18, 33]`
- `walgebra_equals_euler True`
- `macmahon_differs_from_euler True`
- `first_difference_weight 2`
- `yangian_chars_prefix [1, 1, 3, 6, 13]`
- `walgebra_chars_prefix [1, 1, 2, 3, 5]`
- `jordan_all_match True`
- `Yplus_CoHA_match True`
- `shadow_bridge Z(Rep(CoHA)) = Rep(Y) = Rep(Drinfeld_double(CoHA))`
- `shadow_coha_M [1, 1, 3, 6, 13]`
- `shadow_yangian_M2P [1, 3, 11, 32, 90]`

Additional narrow check:

```bash
python3 - <<'PY'
import sys
sys.path.insert(0, 'compute/lib')
from coha_e1_sector_engine import jordan_quiver_e1_verification, conifold_e1_verification
j = jordan_quiver_e1_verification(6)
c = conifold_e1_verification(5)
print('jordan_all_verified', j['all_verified'])
print('jordan_character_is_macmahon', j['character_is_macmahon'])
print('jordan_bps_match', j['bps_match'])
print('jordan_chi_matches_inverse_macmahon', j['chi_matches_inverse_macmahon'])
print('jordan_kappa', j['kappa'])
print('conifold_kappa', c.get('kappa'))
```

Output summary:

- `jordan_all_verified True`
- `jordan_character_is_macmahon True`
- `jordan_bps_match True`
- `jordan_chi_matches_inverse_macmahon True`
- `jordan_kappa 1`
- `conifold_kappa 2`

Residual open obligations:

1. Repair stale compute prose that still collapses CoHA, the full Yangian, and
   `W_{1+\infty}`.
2. Reconcile `cy_c_six_routes_convergence.tex:87-90` with the generator-level
   no-six-way-isomorphism theorem.
3. Audit every `ClaimStatusProvedHere` Drinfeld-double claim outside `C^3`
   against the pairing/completion/equivariance hypotheses.
4. Remove or reclassify local `P^3` from the CY3 CoHA evidence lane.
5. Keep K3 x E structural claims below the character identity conditional until
   the Hall-Borcherds and hCS-to-Hall comparisons are actually present.

Files changed:

- `notes/adversarial_architecture_swarm_20260424/agent_06_coha_positive_half.md`
