# Agent 11 - Computational Evidence and Oracle Adversarial Attack-Heal

Date: 2026-04-24. Scope: compute oracles, tests, metadata registry drift, and body anchors for architecture/master-synthesis claims. Report-only. No commits. No destructive git. No code/prose edits outside this report.

## Commands run

- `python3 -m pytest -q compute/tests/test_cy_d_kappa_stratification.py compute/tests/test_kappa_spectrum_reconciliation.py compute/tests/test_kappa_consistency_adversarial.py compute/tests/test_kappa_bkm_adversarial.py compute/tests/test_kappa_bkm_universal.py`
  - Output: `316 passed in 0.41s`.
- `python3 -m pytest -q compute/tests/test_zte_t_matrix_exact.py`
  - Output: `35 passed in 11.06s`.
- `python3 -m pytest -q compute/tests/test_igusa_product_formula.py compute/tests/test_igusa_product.py compute/tests/test_phi01_fourier.py compute/tests/test_phi01_cross.py compute/tests/test_phi01.py compute/tests/test_phi01_shadow_decomposition.py`
  - Output: `214 passed in 4.30s`.
- `python3 compute/scripts/cross_validate_phi01.py`
  - Output: `Passed: 30; Failed: 0; Warnings: 5`. Warnings: live DFT precision deviations at `n=6`; `bkm_shadow_tower.py` docstring says `c(-1)=2` while computation delegates to the correct `c(-1)=1`.
- `python3 compute/scripts/verify_igusa_high_precision.py`
  - Output: sign-correct Delta5 product verified at 7 points to 25-58 digits; naive product ratio is `-1`, absorbed-sign product ratio is `+1`.
- `python3 -m pytest -q compute/tests/test_e1_refined_macmahon_engine.py compute/tests/test_macmahon_shadow_decomposition.py compute/tests/test_coha_drinfeld_bulk.py compute/tests/test_c3_envelope_comparison.py`
  - Output: `259 passed in 2.89s`.
- `python3 -m pytest -q compute/tests/test_k3_yangian_humbert_monodromy_8.py compute/tests/test_local_p2_four_kappa_engine.py compute/tests/test_local_p2_shadow.py compute/tests/test_conifold_chart_gluing.py compute/tests/test_conifold_shadow_transition.py compute/tests/test_fh_mckay_correspondence.py compute/tests/test_cy_d_kappa_stratification.py::TestConifoldNonLocalSurface`
  - Output: `712 passed in 1.34s`.
- `python3 -m pytest -q compute/tests/test_cy_c_six_routes.py`
  - Output: `21 passed in 0.08s`.
- Read-only metadata count script over `main.tex`, `chapters/`, `appendices/`, `standalone/`, and `metadata/claims.jsonl`.
  - Live status counts: `Conditional 117`, `Conjectured 346`, `Heuristic 16`, `Open 4`, `ProvedElsewhere 356`, `ProvedHere 898`, total `1737`.
  - Metadata snapshot: `Conditional 59`, `Conjectured 285`, `Heuristic 10`, `ProvedElsewhere 259`, `ProvedHere 775`, total `1388`.
  - Malformed/composite status occurrences: `main.tex:146`, `chapters/theory/cy_to_chiral.tex:341`, `chapters/examples/cy_c_six_routes_convergence.tex:393`.
- `rg --files compute/tests | rg 'cy_c_six_routes|phi01|igusa|macmahon|coha|c3_envelope|humbert|local_p2|conifold|mckay'`
  - Output confirmed the CY-C body-anchor test `compute/tests/test_cy_c_six_routes.py` exists.
- `git status --short`
  - Output: broad dirty worktree from other agents; this report is the only Agent 11 write.

## ATTACK_1 - K3xE kappa_ch has contradictory passing oracles

Attack. The canonical compact-CY theorem says `kappa_ch(A_X)=sum_q (-1)^q h^{0,q}(X)` and gives `kappa_ch(K3 x E)=0` in `chapters/examples/cy_d_kappa_stratification.tex:350-378` and `411-426`. The current BKM theorem also says the naive decomposition fails already at `N=1`: `5` versus `0+0=0` in `chapters/examples/cy_d_kappa_stratification.tex:2013-2052`.

Stale compute oracles still pass while asserting the older additive/specialisation value:

- `compute/lib/kappa_spectrum_reconciliation.py:30-36`, `172-193`, `346-378`, `486-522`: `kappa_ch(K3xE)=3` and `5=3+2`.
- `compute/tests/test_kappa_spectrum_reconciliation.py:193-198`, `310-322`: asserts `kappa_ch(K3xE)=3` and decomposition holds.
- `compute/lib/kappa_bkm_adversarial.py:1-20`, `190-241`: says `N=1` is the only case where decomposition holds.
- The same pytest command simultaneously passes the canonical supertrace suite and the stale additivity suite: `316 passed`.

Exact failure. The oracles are not merely alternate checks; they expose two meanings under one name, `kappa_ch`: `PhiFA/Hodge-supertrace kappa_ch=0` versus `Heisenberg-Mukai/additive specialisation scalar=3`.

HEAL_1. Split names and tests:

- Rename the additive output to `kappa_Heis_Mukai` or `kappa_ch_specialisation_additive`; do not export it as the compact `kappa_ch`.
- Rewrite `verify_BKM_decomposition_k3e()` as an adversarial negative oracle: `decomposition_holds_N1 = False`, with observed failure `5 != 0 + 0`.
- Update tests in `compute/tests/test_kappa_spectrum_reconciliation.py`, `compute/tests/test_kappa_consistency_adversarial.py`, and `compute/tests/test_kappa_bkm_adversarial.py` so the canonical theorem lane expects `0`; keep `3` only under the renamed specialisation oracle.
- Repair the manuscript drift at `chapters/examples/cy_d_kappa_stratification.tex:1400-1414`, which still writes `{kcat,kch,kBKM,kappa_fibre}(K3 x E)={0,3,5,24}` and says the `N=1` decomposition holds. This contradicts the same file at `350-378` and `2013-2052`.

## ATTACK_2 - BKM constant tables conflate three scopes

Attack. The theorem-level CHL BKM scope is five frame shapes `N in {1,2,3,4,6}` with constants `(10,8,6,4,2)` and weights `(5,4,3,2,1)` in `chapters/examples/cy_d_kappa_stratification.tex:2013-2052`.

The compute engine `compute/lib/diagonal_siegel_cy_orbifolds.py:80-96`, `268-333` stores an eight-order diagonal table with constants `{1:10,2:8,3:6,4:4,5:4,6:2,7:2,8:2}` and weights `{1:5,2:4,3:3,4:2,5:2,6:1,7:1,8:1}`. `compute/tests/test_kappa_bkm_universal.py:136-154` tests this eight-order table as a universal oracle.

But the battle-hardened synthesis distinguishes two different scopes at `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:393-404`: Scope A CHL ladder `(10,8,6,4,2)->(5,4,3,2,1)` and Scope B Gritsenko-Clery eight-form atlas `(10,4,2,2,1,2,1/2,0)->(5,2,1,1,1/2,1,1/4,0)`.

Exact failure. The current compute table is neither the five CHL theorem table nor the Gritsenko-Clery eight-form atlas; it is a third diagonal/Nikulin-orbifold table. Passing tests can therefore certify the wrong eight-row claim.

HEAL_2. Split oracle modules:

- `bkm_chl_frame_shapes.py`: five rows only, `N={1,2,3,4,6}`, constants `(10,8,6,4,2)`.
- `diagonal_nikulin_orbifold_table.py`: current eight-order diagonal table, explicitly not the Gritsenko-Clery eight-form atlas.
- `gritsenko_clery_eight_form_atlas.py`: constants `(10,4,2,2,1,2,1/2,0)` with cover-group labels.
- Update `test_kappa_bkm_universal.py` so theorem `thm:borcherds-weight-kappa-BKM-universal` tests only CHL scope, and add a separate test asserting the diagonal table is not used as the Gritsenko-Clery atlas.

## ATTACK_3 - Delta5 sign is verified by script but not by pytest

Attack. The ordinary pytest in `compute/tests/test_igusa_product_formula.py:1-13` checks the eta identity up to absolute phase and checks only `abs_relative_error < 1e-6` for the Borcherds product. It does not enforce the sign.

The stronger script `compute/scripts/verify_igusa_high_precision.py:1-50` states and verifies the sign-correct identity:

`(1/64) Delta_5(Z) = - exp(pi*i*(z1+z2+z3)) * product`.

Its run confirmed the naive product ratio is `-1` and the absorbed-sign product ratio is `+1` at 7 points to 25-58 digits. `cross_validate_phi01.py` also found only precision/cosmetic warnings, including the stale `c(-1)=2` docstring in `bkm_shadow_tower.py`; the actual delegated computation gives `c(-1)=1`.

Exact failure. CI-style pytest can pass if the sign regresses, because it only inspects absolute value.

HEAL_3. Add a sign-sensitive pytest:

- Assert `(1/64)*Delta5 / BP_naive` is near `-1`.
- Assert `(1/64)*Delta5 / BP_absorbed` is near `+1`.
- Fix the stale `bkm_shadow_tower.py` docstring factor so the warning disappears.
- Keep the high-precision verifier as a targeted script or a slow pytest marker; do not replace it with the absolute-value test.

## ATTACK_4 - ZTE exact T-matrix is strong but charge-2 scoped

Attack. `compute/lib/zte_t_matrix_exact.py:1-44`, `220-255` is a good exact rational oracle, but it projects to the charge-2 sector before solving. Tests confirm a `36 x 80` system, rank `35`, exact solution, nonzero `O(kappa^4)` remainder, and parameter stability at a second point in `compute/tests/test_zte_t_matrix_exact.py:1-47`, `155-190`, `294-320`, `450-489`.

Exact failure. No failure in the test itself. The adversarial risk is overcitation: a charge-2 `O(kappa^2)` correction with residual `O(kappa^4)` is not an all-charge, all-parameter ZTE theorem.

HEAL_4. Pin oracle scope in names and body anchors:

- Rename theorem-facing references to `zte_t_matrix_exact_charge2_rational`.
- Add tests for singular parameter rejection: repeated spectral parameters and denominator `z+kappa=0`.
- Add one full `16 x 16` smoke residual check, or explicitly state that the oracle certifies only the charge-2 projection.
- Manuscript claims should say "charge-2 sector, exact rational, resolves the linearized `O(kappa^2)` obstruction" unless a larger engine is added.

## ATTACK_5 - CoHA/MacMahon tests count correctly but do not guard the positive-half discipline

Attack. The coefficient tests pass: CoHA/MacMahon group gave `259 passed`. The semantic oracle is weaker.

Problem lines:

- `compute/lib/macmahon_shadow_decomposition.py:6-13` says `A_{C^3}=W_{1+infinity}` if the `d=3` functor exists.
- `compute/lib/coha_drinfeld_bulk.py:30-32` says `Y^+ = CoHA(C^2)`, while the same module's class at `254-263` correctly describes the tripled Jordan/C3 critical CoHA.
- `compute/lib/c3_envelope_comparison.py:18-21`, `47-58` has the better doctrine: `CoHA(C^3)=Y^+(gl_hat_1)`, with `W_{1+infty}` appearing through the generic/N=1 envelope comparison.

Exact failure. Coefficient equality with MacMahon does not certify the algebra-role statement. The current tests can pass while the prose says `CoHA(C^3)=W_{1+infty}` directly, which violates the current cache: CoHA is the positive half; `W_{1+infty}` belongs to the double/envelope side.

HEAL_5. Add a semantic role oracle:

- `coha_c3_role = "positive_half_Y_plus"`.
- `w1infty_role = "drinfeld_double_or_chiral_envelope"`.
- Add tests scanning compute docstrings and manuscript anchors for forbidden direct equalities such as `CoHA(C^3) = W_{1+infty}` unless qualified by "double", "envelope", or "N=1 degeneration".
- Fix `CoHA(C^2)` at `compute/lib/coha_drinfeld_bulk.py:32` to the intended C3/Jordan critical sector, or explain if that line intentionally means the surface CoHA.

## ATTACK_6 - Local P2/conifold BKM column disagrees with compute oracle

Attack. `compute/lib/local_p2_four_kappa_engine.py:260-318` states `kappa_BKM` is undefined for local P2 because toric CY3 lacks the hyperbolic lattice, weak Jacobi input, and BKM denominator formula. `compute/tests/test_local_p2_four_kappa_engine.py:171-180` asserts this. The local/conifold/Humbert command passed `712` tests.

The manuscript currently uses the `kappa_BKM` column for noncompact refined-vertex constants:

- `chapters/examples/cy_d_kappa_stratification.tex:1774-1813`: conifold row `(kch,kcat,kBKM,kchBV)=(+1,0,+1,-1)` and local P2 row `(3/2,0,3/2,-3/2)`.
- `chapters/examples/cy_d_kappa_stratification.tex:1850-1855`: applies `thm:borcherds-weight-kappa-BKM-universal` to the conifold refined vertex.
- `chapters/examples/cy_d_kappa_stratification.tex:2978-3002`: says `kBKM` is the refined topological vertex constant term for conifold/local P2/C3.

Exact failure. Compute says local P2 has no `kappa_BKM`; manuscript reuses the symbol for a noncompact refined topological vertex constant. This is a real compute-vs-prose disagreement, not a missing test.

HEAL_6. Choose one convention explicitly:

- If toric noncompact refined-vertex constants are intended, rename the column to `kappa_vertex` or `kappa_DT`, and reserve `kappa_BKM` for Borcherds denominator products.
- If the manuscript insists on `kappa_BKM`, add a new compute oracle proving the denominator-product sum side, lattice input, and constant term for conifold/local P2. Do not route this through the CHL theorem without a scope bridge.
- Add a cross-test comparing `local_p2_four_kappa_engine.complete_spectrum()["kappa_BKM"]` with the manuscript row; it should fail until the convention is resolved.

## ATTACK_7 - Theorem registry and claim metadata are stale

Attack. `metadata/theorem_registry.md:1-23` is auto-generated `2026-04-23` and records total `1388`, `ProvedHere 775`, `Open 0`. The read-only live scan gives total `1737`, `ProvedHere 898`, `Open 4`. The worktree is also broadly dirty, so line anchors in `metadata/claims.jsonl` are stale.

Additional exact issues:

- `main.tex:146`, `chapters/theory/cy_to_chiral.tex:341`, `chapters/examples/cy_c_six_routes_convergence.tex:393`: composite `ClaimStatusProvedHereConditional`.
- `metadata/claims.jsonl` row for `thm:pairwise-all-proved-closes-CY-C` is `ProvedHere` while its block references `thm:six-routes-isomorphism`.
- `metadata/claims.jsonl` row for `prop:harvey-moore-functorial-residual-structure` over-captures a large block of later labels, showing parser/body-boundary drift.

Exact failure. Registry numbers and some statuses are not reliable during this swarm. They should not be used as architecture evidence until regenerated after integration.

HEAL_7. After the swarm merge, run the metadata generator once and inspect the diff, but do not do that inside this report-only agent. Proposed repairs:

- Teach `scripts/generate_metadata.py` how to classify `ClaimStatusProvedHereConditional`.
- Add parser tests around `cy_c_six_routes_convergence.tex` so a conjecture block cannot swallow dozens of following labels.
- Reclassify theorem rows whose proof is conditional on a conjectured route, or make the hypotheses explicit in the theorem environment title/status.

## Evidence upheld

- ZTE exact rational charge-2 oracle is internally consistent: exact fractions, rank `35`, structural symmetries, nonzero smaller residual.
- Phi01/Delta5 coefficients are well-supported by exact Fourier, DFT, WKB denominator, and shadow-tower delegation; only the pytest sign coverage needs strengthening.
- Humbert order `8`, `hbar^2 * K^{kappa_ch} = -1`, and related K3 B-family checks pass in the targeted Humbert suite.
- CY-C body-anchor file `compute/tests/test_cy_c_six_routes.py` exists and passes.

## Open questions for integration owner

1. Should `kappa_ch(K3 x E)=3` survive only as a renamed specialisation/Heisenberg-Mukai scalar, with compact `kappa_ch=0` everywhere?
2. Should noncompact toric refined-vertex constants be named `kappa_vertex`/`kappa_DT` rather than `kappa_BKM`?
3. Which eight-row BKM table is theorem-facing: diagonal Nikulin-orbifold, singly-twined Mathieu, or Gritsenko-Clery eight-form atlas?
4. Should `verify_igusa_high_precision.py` become a slow pytest marker so Delta5 sign regressions are caught automatically?
5. Should composite statuses such as `ProvedHereConditional` be first-class metadata statuses or rewritten as ordinary `Conditional`/`ProvedHere` with hypotheses?
