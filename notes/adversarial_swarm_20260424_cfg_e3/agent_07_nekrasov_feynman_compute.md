# Agent 07: Nekrasov Perturbative/Feynman-Compute Examiner

Scope: chain-level `\Phi_3` on CY3, Costello-Francis-Gwilliam 2026
arXiv:2602.12412, Appendix A, and the local CY3 / hCS / factorization /
`S^3` compute surface.

Owned file only:
`notes/adversarial_swarm_20260424_cfg_e3/agent_07_nekrasov_feynman_compute.md`.
No manuscript files edited.

## Sources Read

Primary source:

- Costello-Francis-Gwilliam, *Chern-Simons factorization algebras and knot
  polynomials*, arXiv:2602.12412v1, submitted 2026-02-12:
  https://arxiv.org/abs/2602.12412.
- CFG Appendix A, *Explicit quantizations via the configuration space method*:
  https://arxiv.org/pdf/2602.12412, Appendix A.1-A.2.

Local anchors:

- `chapters/theory/cy3_chain_level_bridge.tex:11`: hCS BV complex
  `\Omega^{0,\bullet}(X,\mathfrak g)[1]`.
- `chapters/theory/cy3_chain_level_bridge.tex:45`: typed bridge
  `\PhiFA_3 -> CoHA_crit -> Y^+ -> D(Y^+) -> W_{1+\infty}`.
- `chapters/theory/cy3_chain_level_bridge.tex:227`: no CFG shortcut.
- `chapters/theory/cy3_chain_level_bridge.tex:244`: open
  `\Theta_{\hCS\to\Hall}^{or}` problem.
- `chapters/theory/quantum_chiral_algebras.tex:3480`: hCS on `C^3`
  as an `E_3` Dolbeault chain complex with Bochner-Martinelli propagator.
- `notes/wave12_f2_bv_brst_to_chiral_ce.tex:388`: 6d hCS BV complex
  and reduction to chiral CE.
- `chapters/theory/cy_to_chiral.tex:221`: native holomorphic
  factorization algebra and specialisation functor.
- `chapters/theory/cy_to_chiral.tex:242`: two-stage factorisation
  `\Phi_d = \SpCh_{\Sigma_{d-1},C}\circ\PhiFA_d`.
- `chapters/theory/cy_to_chiral.tex:4691`: conditional framed
  object-level `d=3` theorem.
- `compute/lib/dolbeault_cy3_homotopy.py`.
- `compute/lib/s3_framing_chain_level.py`.
- `compute/lib/hopf_fibration_s3_framing.py`.
- `compute/lib/cy3_chain_framing.py`.
- `compute/lib/hcs_codim2_defect_ope.py`.
- `compute/lib/hcs_vs_sigma_adversarial.py`.
- `compute/lib/k3_hcs_6d_oneloop.py`.
- `compute/lib/k3_hcs_6d_twoloop.py`.
- `compute/lib/k3_hcs_6d_threeloop.py`.
- `compute/lib/k3_hcs_6d_fourloop.py`.
- `compute/lib/factorization_categories_chiral.py`.
- Matching tests under `compute/tests/test_*cy3*.py`,
  `compute/tests/test_*hcs*.py`, `compute/tests/test_*factorization*.py`,
  `compute/tests/test_*s3*.py`.

## Executive Verdict

CFG is a strong topological `E_3` test oracle, not a proof of the CY3
chain-level avatar.

The dangerous collapse is:

```tex
\Obs_{\CY_3} \leadsto C^*(\mathfrak g).
```

This is false unless an explicit forgetful functor to the locally constant
associated model has already been named. CFG's `C^*(\mathfrak g)` is the
ordinary 3d Chern-Simons local-constant model. The Vol III CY3 object is the
many-variable Dolbeault-chiral CE/enveloping factorization object:

```tex
\CE^\bullet_{\bar\partial,\chir}
  \bigl(\Omega^{0,\bullet}_c(X,\mathfrak g)[1],\mathcal O_X\bigr),
```

with holomorphic jets in `z_1,z_2,z_3`, Bochner-Martinelli or heat-kernel
propagators, multidirectional OPE/factorization over polydiscs, and only
then pushforward/specialisation to an `E_1` chiral algebra on a curve.

Computational status:

- `C^3` toric/defect evidence is strong and test-backed.
- The `S^3` and Hopf-framing tests correctly keep `d=3` native output
  `E_1`, with `E_2` recovered through the Drinfeld center.
- Compact CY3 evidence remains conditional at the BV/OPE completion and
  hCS-to-Hall comparison gates.
- The K3 x E multi-loop hCS engines are useful perturbative witnesses, but
  direct probing found a red flag: `k3_hcs_6d_twoloop.ybe_at_hbar5`
  reports `two_loop_verification_passed = false`, and the one-to-four-loop
  modules have no matching pytest files. They must not be cited as verified
  theorem-level evidence until a targeted test oracle is added.

## Attack-Heal Cycles

### Cycle 1: CFG Appendix A as a CY3 hCS proof

Attack: Use CFG Appendix A to assert that BV quantization already gives the
CY3 `E_3` holomorphic factorization algebra.

Failure mode: CFG quantizes ordinary 3d Chern-Simons on real configuration
spaces. Its local cochains are quasi-isomorphic to `C^*(\mathfrak g)` after
passing to the locally constant model. Appendix A supplies configuration
space Feynman weights and QME boundary-face control; it does not supply
Dolbeault fields, holomorphic jets in three variables, the
Bochner-Martinelli kernel, or chiral CE/enveloping factorization.

Heal: Import CFG only as a graph/QME normal form: Stokes boundary terms,
configuration-space compactification, and renormalized action satisfying QME.
The CY3 analogue must replace ordinary de Rham/topological fields with
`\Omega^{0,\bullet}(X,\mathfrak g)[1]`, `\bar\partial`, holomorphic volume,
and chiral CE.

Testable invariant: a valid CY3 import must contain a field-complex tag
`Dolbeault`, a three-coordinate jet set `{z_1,z_2,z_3}`, and a named
forgetful functor before any `C^*(\mathfrak g)` comparison.

Verdict: CFG is formal evidence, not a source theorem for `\PhiFA_3`.

### Cycle 2: Dolbeault homotopy versus ordinary CE collapse

Attack: The local model is acyclic, so replace Dolbeault-chiral CE by ordinary
Lie cochains.

Failure mode: The compute surface explicitly treats the CY-A_3 gap as
analytic, not algebraic. `dolbeault_cy3_homotopy.py` keeps the
`\bar\partial` complex and gives Cech/Gepner/spectral substitutes. The direct
compute probe returned:

```text
verify_cech_sdr(quintic): sdr_verified=True, h^2=True, h i=0, p h=0.
analyze_quintic(): analytic_gap_closed=True, most_promising=Cech.
```

This closes a coefficient-level contracting-homotopy problem in that module.
It does not by itself prove global OPE sewing or hCS-to-Hall comparison.

Additional failure: `hopf_fibration_s3_framing.py` distinguishes compact
non-perturbative BV convergence from perturbative coefficient control:

```text
quintic: obs_bv_perturbative=True, obs_bv_nonperturbative=False.
K3_x_E: obs_bv_perturbative=True, obs_bv_nonperturbative=False.
```

Heal: Split the statement into three statuses:

- Cech SDR: computed.
- Perturbative BV trivialization: conditional evidence.
- Non-perturbative OPE/sewing and hCS-to-Hall comparison: open/conditional.

Proposed test: `test_compact_bv_status_not_overclosed`, asserting that
`analyze_quintic().analytic_gap_closed` cannot be used to set
`obs_bv_nonperturbative=True` for compact CY3.

Verdict: ordinary `C^*(\mathfrak g)` is only the associated locally constant
shadow. The CY3 chain object remains Dolbeault/chiral.

### Cycle 3: `S^3` framing as native braiding

Attack: Since CFG constructs an `E_3` algebra and perfect modules yield
braided structures, the CY3 chiral algebra should be natively `E_2`.

Failure mode: Local tests and manuscript anchors agree that `d=3` specializes
to native `E_1`; the braided structure comes from the Drinfeld center of the
`E_1` representation category. The broad test run included
`test_s3_framing_chain_level.py` and `test_hopf_fibration_s3_framing.py`;
the direct probe returned:

```text
master_s3_framing_verification()["all_pass"] = True
en_from_framing: d1=E_infty, d2=E_2, d3=E_1, d4=E_1.
```

Heal: Keep the two levels separate:

```tex
\PhiFA_3(\mathcal C) \in E_3\text{-HolFA}(X),
\qquad
\SpCh_{\Sigma_2,C}(\PhiFA_3(\mathcal C)) \in E_1\text{-ChirAlg}(C).
```

The non-symmetric quantum-group braiding is a center operation, not native
braiding of the CY3 chiral algebra.

Falsification point: any theorem statement saying the specialized CY3 output
is natively `E_2` fails the compute and manuscript surface.

Verdict: CFG reinforces the module-category route to braiding; it does not
change Vol III's `d=3 -> E_1` discipline.

### Cycle 4: hCS defect OPE on `C^3`

Attack: The `C^3` hCS defect computation proves the whole CY3 functor.

Failure mode: `hcs_codim2_defect_ope.py` proves a local toric defect model:
6d hCS on `C^3`, a codimension-2 defect on `C_{z_1}`, normal variables
`(z_2,z_3)`, and Omega-background parameters. It does not construct compact
CY3 `\PhiFA_3`, K3 x E Borcherds output, or the hCS-to-Hall map.

Direct compute evidence:

```text
run_full_derivation()["all_ok"] = True
self-dual (1,0,-1): Psi=1
SV N=2 (1,-2,1): Psi=3
generic (1,-3,2): Psi=7
J_{(1)}J = Psi, T_{(3)}T = 1/2, r-pole = OPE-pole - 1.
```

Heal: Use this as the local Nekrasov/Costello witness for the toric
polydisc/OPE mechanism. Do not identify it with compact CY3 or with the Hall
side until `\Theta_{\hCS\to\Hall}^{or}` is built.

Proposed tests:

- `test_bochnermartinelli_kernel_three_variables`: verifies a genuine
  three-variable Dolbeault propagator, not a one-dimensional OPE kernel.
- `test_polydisc_factorization_arity_three`: verifies associativity over
  disjoint polydiscs in three holomorphic directions with shuffle signs.
- `test_forgetful_to_locally_constant_model_named`: ordinary
  `C^*(\mathfrak g)` appears only after an associated-model projection.

Verdict: strong local/toric support. No compact CY3 theorem.

### Cycle 5: K3 x E multi-loop hCS coefficients

Attack: The one-to-four-loop engines prove the K3 x E quantum toroidal or
Borcherds output.

Failure mode: The loop files are perturbative engines, not theorem oracles.
No pytest files match `k3_hcs_6d_oneloop.py`,
`k3_hcs_6d_twoloop.py`, `k3_hcs_6d_threeloop.py`, or
`k3_hcs_6d_fourloop.py`. A direct probe gives mixed evidence:

```text
one-loop A1: YBE residual 6.119755e-06 at hbar=0.01,
             ybe_preserved_at_hbar3=True.

two-loop A1:
  A2_wave2_square_formula = 169.0
  A2_total_normalised = 168.66666666666666
  two_loop_YBE_residual = 6.107390e-06
  two_loop_verification_passed = False.

three-loop A1:
  A3_total = 2187.3166666666666.

four-loop A1:
  A4_total = 28311.319444444445.
```

The two-loop failure is decisive for status: the multi-loop chain is not
verified as a YBE-restoring perturbative expansion in the current compute
surface.

Heal: Keep these modules as perturbative evidence and proposed coefficient
templates. Add tests before citation:

- `test_k3_hcs_twoloop_ybe_passes_on_grid`: require
  `two_loop_verification_passed=True` over a small `(u,v,\hbar)` grid.
- `test_k3_hcs_loop_modules_have_pytest_coverage`: fail if a loop engine has
  no matching test file or no direct imported test case.
- `test_loop_coefficients_exact_rationals`: verify `A2`, `A3`, `A4` as exact
  rational expressions, not only floats.
- `test_graph_automorphism_denominators`: fish, sunset, `K_4`, `K_5`
  denominators match declared automorphism factors.
- `test_cfg_appendix_a_qme_boundary_faces`: each counterterm is tied to a
  boundary-face/Stokes term or a named BRST-exact obstruction.

Verdict: one-loop evidence is usable. Two-loop and higher are unverified and
currently red at the direct YBE check.

### Cycle 6: CFG trace theorem as CY3 character theorem

Attack: CFG proves the factorization-homology trace equals the
Reshetikhin-Turaev invariant; therefore CY3 traces equal Borcherds
denominators or quantum-toroidal characters.

Failure mode: CFG requires a perfect module over the constructed ordinary
3d CS `E_3` algebra. Vol III compact CY3 needs perfect/trace-class modules
for the specialized `E_1` chiral algebra after the Dolbeault-chiral CE and
holomorphic pushforward are built. The local factorization-category landscape
keeps the statuses separate:

```text
C^3 (d=3, toric): proof_status = PROVED for toric (Schiffmann-Vasserot).
K3 x E (d=3): proof_status = CONJECTURAL (CY-A_3).
Quintic (d=3): proof_status = CONJECTURAL (CY-A_3).
```

Heal: Import CFG trace formalism only after constructing:

```tex
\PhiFA_3(\mathcal C)
  -> \SpCh_{\Sigma_2,C}
  -> A_{\mathcal C}^{(\Sigma_2,C)}
  -> \operatorname{Perf}_{A_{\mathcal C}}
  -> \operatorname{Tr}.
```

Falsification point: any trace theorem for K3 x E that does not name the
perfect module or trace-class defect object is under-specified.

Verdict: CFG supplies a target shape for a future theorem, not the theorem.

## Testable Invariants

1. CY3 avatar invariant:
   ordinary `C^*(\mathfrak g)` may appear only under a field
   `associated_locally_constant_model` or an explicit forgetful functor.

2. Dolbeault variable invariant:
   a CY3 hCS object must expose `\bar\partial`, `\Omega_X`, and three
   holomorphic jet variables `z_1,z_2,z_3`.

3. Polydisc OPE invariant:
   the native local product must be over disjoint opens/polydiscs in complex
   dimension three before any curve reduction.

4. Defect OPE invariant:
   `Psi = -sigma_2`; for `(h_1,h_2,h_3)=(1,0,-1),(1,-2,1),(1,-3,2)`, the
   expected values are `1,3,7`.

5. Native-level invariant:
   after Stage 2, `d=3` gives `E_1`, not native `E_2`.

6. Compact BV invariant:
   compact CY3 perturbative BV support does not imply non-perturbative OPE
   convergence or hCS-to-Hall comparison.

7. Loop-engine invariant:
   K3 hCS loop coefficients are not verified unless the YBE residual improves
   at the claimed order and the counterterm test passes.

## Verification Run

Targeted core:

```bash
python3 -m pytest -q \
  compute/tests/test_dolbeault_cy3_homotopy.py \
  compute/tests/test_s3_framing_chain_level.py \
  compute/tests/test_hopf_fibration_s3_framing.py \
  compute/tests/test_cy3_chain_framing.py \
  compute/tests/test_hcs_codim2_defect_ope.py \
  compute/tests/test_factorization_categories_chiral.py \
  compute/tests/test_hcs_vs_sigma_adversarial.py
```

Result:

```text
535 passed in 0.96s
```

Filename-matched broad surface:

```bash
python3 -m pytest -q \
  compute/tests/test_*cy3*.py \
  compute/tests/test_*hcs*.py \
  compute/tests/test_*factorization*.py \
  compute/tests/test_*s3*.py
```

Result:

```text
4730 passed in 38.44s
```

Direct perturbative probe:

```text
cech_sdr.sdr_verified = True
s3_all_pass = True
hcs_full_all_ok = True
one_loop_ybe.ybe_preserved_at_hbar3 = True
two_loop_ybe.two_loop_verification_passed = False
```

## Proposed New Tests

Create `compute/tests/test_cfg_cy3_feynman_guardrails.py` with:

1. `test_plain_ce_is_only_associated_model`.
2. `test_dolbeault_chiral_ce_has_three_jet_variables`.
3. `test_bochnermartinelli_kernel_form_degree`.
4. `test_polydisc_factorization_not_curve_only`.
5. `test_cfg_appendix_a_import_is_qme_template_only`.
6. `test_k3_hcs_twoloop_ybe_passes_on_grid`.
7. `test_k3_hcs_loop_modules_have_pytest_coverage`.
8. `test_compact_bv_status_not_overclosed`.
9. `test_factorization_landscape_k3e_and_quintic_conjectural`.

## Status Recommendations

- `CFG -> \PhiFA_3`: analogy/test-oracle only.
- `C^*(\mathfrak g)`: locally constant associated model only.
- `\Obs_{\hCS}(\C^3)`: local Dolbeault-chiral CE witness, strong for toric
  `C^3`.
- `\Theta_{\hCS\to\Hall}^{or}`: open; do not infer from CFG.
- `K3 x E` quantum-toroidal/Borcherds output: conditional/conjectural until
  hCS-to-Hall, perfect modules, and loop counterterm tests are supplied.
- Multi-loop K3 hCS modules: perturbative evidence, not verified theorem
  evidence; direct two-loop check is currently red.

## Files Changed

- Added this report only.

No manuscript files edited.
