# Agent 05 Report: Costello BV-BRST / Holomorphic-CS Examiner

Date: 2026-04-24.

Owned file: `notes/adversarial_swarm_20260424_cfg_e3/agent_05_costello_bv_hcs.md`.

Scope: adversarial examination of the BV-BRST construction of six-real-dimensional holomorphic Chern-Simons observables on CY3 inputs, and its relation to Costello--Francis--Gwilliam (CFG) topological Chern-Simons filtered `E_3` observables in arXiv:2602.12412.

No manuscript file was edited.

## Executive Verdict

CFG Section 4 proves an ordinary three-dimensional Chern-Simons theorem: a level `lambda in hbar H^3(g)[[hbar]]` gives a perturbative BV quantization and a filtered `E_3` deformation of the locally constant algebra `C^*(g)`. That object is the topological/locally constant associated model. It is not the CY3 avatar.

The Vol III CY3 avatar is the Dolbeault/chiral local Lie algebra and its chiral CE/factorization observables. On a polydisc `U subset X`,
[
  E_hCS(U) = Omega^{0,*}(U,g)[1],             Q = dbar,
]
with compactly supported local Lie algebra
[
  L_hCS,c(U) = Omega^{0,*}_c(U,g),
  \qquad
  [alpha tensor x, beta tensor y]
  =
  (alpha wedge beta) tensor [x,y].
]
The classical observables are completed Chevalley--Eilenberg cochains
[
  Obs_hCS^cl(U)
  =
  C^*_{Lie}(L_hCS,c(U))
  =
  widehat{Sym}(L_hCS,c(U)^vee[-1]),
]
with differential `dbar^vee + d_CE`. The CY3 chiralized object is better recorded as
[
  CE^*_{dbar,chir}(L_hCS,c, O_X)
]
or the corresponding Costello--Gwilliam factorization envelope, with structure maps for disjoint polydiscs. Its pointwise holomorphic jet model is
[
  g[[z_1,z_2,z_3]]
]
after Dolbeault cohomology, not just the finite-dimensional Lie algebra `g`.

The comparison to Hall/CoHA is still the open map
[
  Theta_{hCS -> Hall}^{or}: Obs_hCS^q(-,g) -> CoHA_crit^{or}(-).
]
CFG cannot supply this map. It can only serve as a topological associated/locally constant analogy after one deliberately forgets the Dolbeault, holomorphic-jet, and multidirectional OPE data.

## Sources Read

CFG 2026 arXiv source, official URL: https://arxiv.org/abs/2602.12412.

CFG Section 4 anchors from extracted source:

- Lines 1391--1399: main proposition, level `lambda` produces a filtered `E_3` deformation of `A^cl = C^*(g)`.
- Lines 1501--1517: ordinary CS local Lie algebra `g^M = Omega^*(M,g)` with de Rham differential.
- Lines 1526--1559: BV ghosts, fields, antifields, antighosts, shifted symplectic pairing, and CME.
- Lines 1706--1710: Poincare quasi-isomorphism gives filtered `E_3` quasi-isomorphism to `C^*(g)`.
- Lines 1717--1752: deformation complex and obstruction/level calculation.
- Lines 1816--1864: quantum observables, BV Laplacian filtration, locally constant factorization algebra.
- Lines 1938--1949 and 2047--2117: `P_3` bracket computed via the `S^2` binary-operation class and the BV Laplacian.

CFG Appendix A anchors:

- Lines 3535--3541: configuration-space compactification resolves Feynman singularities.
- Lines 3670--3766: propagator extension to compactified configuration spaces and graph-weight integrals.
- Lines 3785--3851: QME, BV Laplacian, Stokes cancellation, separating/nonseparating edge cancellation.
- Lines 3860--3869: hbar-dependent invariant pairings give levels.
- Lines 4013--4047 and 4081--4109: defect QME obstruction and framing anomaly.

Local Vol III anchors:

- `chapters/theory/cy3_chain_level_bridge.tex:11`: hCS BV complex on CY3.
- `chapters/theory/cy3_chain_level_bridge.tex:45`: typed CY3 bridge; `PhiFA_3 -> CoHA_crit -> Y^+ -> D(Y^+) -> W_{1+infty}`.
- `chapters/theory/cy3_chain_level_bridge.tex:203`: anomaly gate, quartic not cubic.
- `chapters/theory/cy3_chain_level_bridge.tex:227`: no CFG shortcut.
- `chapters/theory/cy3_chain_level_bridge.tex:241`: open hCS-to-Hall comparison.
- `chapters/theory/quantum_chiral_algebras.tex:20`: hCS observables as conditional `E_3` Dolbeault-chiral CE algebra.
- `chapters/theory/quantum_chiral_algebras.tex:372`: chiral CE chains/cochains and bar/CE comparison.
- `chapters/theory/quantum_chiral_algebras.tex:3549`: `Obs_hCS(C^3)` as holomorphic CE complex of `Omega^{0,*}(C^3,g)[1]`.
- `notes/wave12_a5_hCS_BV_BRST_explicit.tex:38`: abelian hCS fields on `C^3`.
- `notes/wave12_a5_hCS_BV_BRST_explicit.tex:122`: Bochner--Martinelli propagator.
- `notes/wave14_i1_hCS_nonabelian_anomaly.tex:38`: QME gap and Costello obstruction cocycle.
- `notes/wave14_i1_hCS_nonabelian_anomaly.tex:100`: flat `C^3` one-loop anomaly vanishing claim.
- `notes/wave14_i1_hCS_nonabelian_anomaly.tex:171`: compact/noncompact split.
- `notes/wave12_f3_feynman_coefficients_costello.tex:124`: heat-kernel/BM propagator.
- `notes/wave12_f3_feynman_coefficients_costello.tex:200`: BM uniqueness modulo BV-exact terms.
- `notes/wave12_f3_feynman_coefficients_costello.tex:314`: counterterm algorithm on `C^3`.
- `notes/wave12_f3_feynman_coefficients_costello.tex:497`: six-dimensional `E_3` reading.
- `notes/theory_6d_hcs_chiral_qg.tex:311`: chain-level `S^3`-framing bottleneck.
- `compute/lib/s3_framing_chain_level.py:1`: CY3 gives native `E_1`, not braided `E_2`.
- `compute/lib/swiss_cheese_cy3_e1.py:1`: CY3-derived `E_1` chiral algebra and ordered bar.
- `compute/lib/btz_cy3_e1_engine.py:1`: BTZ shadow engine, lane-scalar cautions.
- `compute/lib/chiral_ce_complex.py:1`: chiral CE complex, `B(U^ch(L)) = CE_*(L)`.

## Actual hCS/BV Object

Let `X` be a CY3 with holomorphic volume form `Omega_X` and metric Lie algebra `g`.

Fields:
[
  E_hCS(X,g) = Omega^{0,*}(X,g)[1].
]

Differential:
[
  Q_hCS = dbar.
]

Bracket on the unshifted local Lie algebra:
[
  [alpha tensor x, beta tensor y]
  =
  (alpha wedge beta) tensor [x,y]_g.
]

BV pairing:
[
  omega_BV(alpha,beta)
  =
  int_X Omega_X wedge <alpha,beta>_g,
]
where only the `(0,3)` Dolbeault component contributes to the integral.

Classical action:
[
  I_hCS(alpha)
  =
  int_X Omega_X wedge
  (1/2 <alpha,dbar alpha> + 1/6 <alpha,[alpha,alpha]>).
]

Classical observables on a polydisc `U`:
[
  Obs_hCS^cl(U)
  =
  C^*_{Lie}(Omega^{0,*}_c(U,g))
  =
  widehat{Sym}(Omega^{0,*}_c(U,g)^vee[-1]),
]
with CE differential dual to `dbar` and to the bracket above.

Holomorphic jet model at `p in U`:
[
  H^0_{dbar}(L_hCS,p)
  =
  g[[z_1,z_2,z_3]],
]
so the collision algebra records jets in all three holomorphic variables. The multidirectional OPE/factorization singularities live on the diagonals of `U^n`, with local coordinates
[
  z_i^{(a)} - z_i^{(b)}, \qquad i=1,2,3.
]
The one-variable OPE kernel `1/(z-w)` appears only after a curve specialization or Omega-background reduction; it is not the raw CY3 hCS observable.

Quantum observables:
[
  Obs_hCS^q(U)
]
are the Costello--Gwilliam perturbative factorization algebra with effective action, BV Laplacian, counterterms, anomaly class, and factorization maps
[
  Obs(D_1) tensor ... tensor Obs(D_n) -> Obs(D)
]
for disjoint polydiscs `D_i subset D`. The product is built by extension by zero classically and by Wick/BV contraction with the Dolbeault propagator quantum mechanically.

CE-to-chiral CE/enveloping passage:

- For a strict Lie conformal algebra `L`, `B(U^ch(L)) = CE_*(L)`.
- For the CY3 Dolbeault local Lie algebra, the corresponding object is a three-holomorphic-direction factorization envelope/chiral CE complex
[
  CE^*_{dbar,chir}(L_hCS,c,O_X),
]
not ordinary finite-dimensional `C^*(g)`.
- CFG's `C^*(g)` is therefore an associated locally constant/topological model, obtained only after collapsing the spatial dependence and replacing Dolbeault locality by de Rham/topological locality.

## Attack-Heal Cycle 1: CFG Shortcut to `C^*(g)`

Attack: Treat CFG Section 4 as proving that the CY3 avatar is the filtered `E_3` algebra `C^*(g)` and then identify that with the output of `Phi_3`.

Failure mode: CFG uses the ordinary de Rham local Lie algebra
[
  g^M = Omega^*(M,g)
]
on a real 3-manifold and proves a locally constant filtered `E_3` deformation of `C^*(g)`. The proof explicitly passes through the Poincare quasi-isomorphism. This has erased the holomorphic variables, Dolbeault differential, and jet algebra. It cannot see `g[[z_1,z_2,z_3]]`.

Heal: State CFG as the topological associated model. The CY3 object is
[
  CE^*_{dbar,chir}(Omega^{0,*}_c(-,g),O_X),
]
with factorization over polydiscs and holomorphic jets in three variables. The only permissible bridge is:
[
  Obs_hCS^q
  -> associated locally constant/topological shadow
  ~ CFG-like C^*(g),
]
and this loses CY3 holomorphic data.

Status: CFG theorem is valid for ordinary 3d CS. The CY3 identification remains conditional/open at the Dolbeault-chiral level.

## Attack-Heal Cycle 2: QME and Anomaly

Attack: Import CFG's no-obstruction argument `H^1(Def_CS)=H^4(g)=0` into six-dimensional hCS and conclude the QME closes for all CY3s.

Failure mode: CFG's obstruction complex is ordinary 3d CS on `R^3`, with `Def_CS ~ C^{>=1}_{Lie}(g)[3]`. The CY3 hCS obstruction is a holomorphic local Lie algebra cohomology problem. In complex dimension 3 the local anomaly slot is quartic in the Lie algebra inputs, not the cubic/level slot of lower-dimensional descendants.

Internal tension found: `notes/wave14_i1_hCS_nonabelian_anomaly.tex` records a flat `C^3` vanishing argument through a `ch_3`/triangle-looking density, while the current bridge and quantum-chiral chapter correct the CY3 local anomaly slot to invariant-polynomial degree 4. The flat `C^3` vanishing survives this tension because the tangent bundle is trivial and the local translation-invariant obstruction is absent in either normalization. The compact formula does not survive as theorem-grade unless rewritten in the quartic Costello--Li local Lie algebra cohomology slot.

Heal:

- Theorem-level local statement in current notes: on flat `C^3`, the one-loop Costello obstruction cocycle vanishes after separating the Casimir wave-function counterterm from the genuine `H^1` anomaly class.
- Heuristic/conditional compact statement: on compact CY3s the global anomaly depends on global characteristic-class data and a quartic invariant polynomial. `K3 x E` is expected to be unobstructed at this one-loop level by product/Kunneth vanishing after the correct quartic class is identified, but a general compact CY3 with nonzero topological contribution requires a Green--Schwarz-type trivialization or a separate Costello--Li theorem.

Status:

- QME on flat `C^3`: theorem-grade within the local note package, pending primary-source citation polishing if moved into manuscript.
- QME on generic compact CY3: conjectural/conditional; do not use the older `ch_3` compact formula as a theorem.
- CFG no-obstruction argument: not transferable without replacing the deformation complex.

## Attack-Heal Cycle 3: BV Laplacian and the `E_3` Bracket

Attack: Use CFG's explicit `P_3` bracket computation to assert the same `E_3` bracket for hCS observables.

Failure mode: CFG's bracket descends along the `S^2` family of binary operations in the framed little 3-disks operad for a locally constant factorization algebra on `R^3`. Its first-order bracket is controlled by a level pairing `lambda` and the BV Laplacian on de Rham fields. In hCS, the BV Laplacian contracts Dolbeault fields using a holomorphic propagator. The singularities are along complex diagonals in `C^3`, and the factorization product is over polydiscs, not just topological balls.

Heal: Keep two layers separate.

1. Topological associated layer: after forgetting Dolbeault locality, CFG explains how a BV Laplacian can create a nontrivial filtered `E_3` deformation.
2. CY3 Dolbeault layer: the quantum differential on
[
  CE^*_{dbar,chir}(L_hCS,c,O_X)[[hbar]]
]
is `dbar^vee + d_CE + hbar Delta_BV + counterterms`, where `Delta_BV` is built from the CY pairing and the Dolbeault heat/BM kernel.

Status: CFG supplies a model for the topological shadow. It does not compute the Dolbeault/chiral `E_3` bracket of hCS.

## Attack-Heal Cycle 4: Bochner--Martinelli Kernel

Attack: Treat the Bochner--Martinelli kernel either as a unique canonical propagator on every CY3 or as an arbitrary representative whose choice invalidates Feynman coefficients.

Failure mode: Both extremes are false. On flat `C^3`, BM is the heat-kernel/Euclidean gauge-fixing representative of the `dbar` homotopy kernel. Other BV-compatible propagators differ by homotopies and finite counterterms. On a compact CY3 there is no global translation-invariant BM kernel; the heat-kernel construction depends on metric/gauge fixing and harmonic projection.

Heal:

- Flat `C^3`: BM is theorem-grade as the scale-limit representative of the `dbar` propagator, modulo BV-exact/counterterm changes. Its local formula controls multidirectional collisions in `(z_1,z_2,z_3)`.
- Compact CY3: replace "BM kernel" by "Costello heat-kernel propagator for `dbar` with harmonic projection"; any statement about global coefficients must include gauge-fixing independence and anomaly cancellation.

Status: BM kernel is a flat local representative, not a compact CY3 theorem by itself.

## Attack-Heal Cycle 5: Holomorphic Locality and Multidirectional OPE

Attack: Collapse hCS locality to a one-variable vertex algebra OPE, or directly identify `Obs_hCS(C^3)` with `W_{1+infty}`.

Failure mode: Raw hCS on `C^3` is a holomorphic factorization algebra in three complex variables. A local observable supported near a point has holomorphic jets in `z_1,z_2,z_3`; collisions of several polydiscs see all relative coordinate differences. The BM kernel is a three-variable Dolbeault kernel. A one-variable OPE appears only after choosing a curve/defect/Omega-background reduction.

Heal: Record the correct chain:
[
  Obs_hCS^q(C^3,g)
  -> CE^*_{dbar,chir}(g[[z_1,z_2,z_3]])
  -> (curve/Omega or defect specialization)
  -> one-variable chiral algebra.
]
On the Hall side the proved algebraic core is
[
  CoHA(C^3) = Y^+(widehat{gl}_1),
]
and `W_{1+infty}` appears only after Drinfeld doubling and Fock/evaluation representation.

Status: three-variable holomorphic locality is theorem-level for the local model; one-variable vertex algebra statements are specialized avatars.

## Attack-Heal Cycle 6: Compact versus Noncompact CY3

Attack: Prove compact CY3 hCS quantization by citing flat `C^3` or CFG.

Failure mode: Noncompact/flat and compact/global theories have different analytic surfaces.

- On `C^3`, Dolbeault cohomology is locally trivial and translation-invariant heat/BM kernels are available.
- On a compact CY3, harmonic representatives, global Chern classes, determinant lines, compact-support conventions, and anomaly cancellation enter.
- CFG is ordinary topological CS on `R^3`, not hCS on a compact complex threefold.

Heal:

- Noncompact flat `C^3`: hCS BV-BRST and local factorization observables are credible theorem-grade, anomaly-gated and supported by local heat/BM calculations.
- Toric noncompact charts: local hCS may be glued only with explicit overlap and orientation data.
- Compact CY3: keep `ClaimStatusConjectured` or `ClaimStatusConditional` unless a Costello--Li style compact quantization theorem, anomaly trivialization, and orientation-preserving Hall comparison are supplied.

Status: compact CY3 is the dangerous zone. No manuscript should inherit flat `C^3` or CFG theorem status for generic compact CY3.

## Attack-Heal Cycle 7: hCS-to-Hall Comparison

Attack: Identify the quantum hCS observables with the critical CoHA because both are CY3-local and both produce `E_1`/`E_3`-flavored structures.

Failure mode: The objects live in different models before comparison.

- hCS side: BV/factorization observables of the Dolbeault local Lie algebra.
- Hall side: Borel--Moore homology of critical loci with vanishing cycles, shifts, Tate twists, and orientation local systems.
- The comparison must preserve orientation data, BV bracket/Hall product, Thom--Sebastiani, completions, equivariance, compact support, and local descent.

Heal: Preserve the open map
[
  Theta_{hCS -> Hall}^{or}: Obs_hCS^q(-,g) -> CoHA_crit^{or}(-)
]
as the first missing lemma. On `C^3`, the target normalization should reduce to the KS/SV positive-half model `Y^+`, not directly to `W_{1+infty}`.

Status: open. This is the central frontier, not a bookkeeping issue.

## Attack-Heal Cycle 8: Compute Surface Overclaim

Attack: Treat the requested compute engines as proving chain-level `Phi_3` for general CY3.

Failure mode: The compute files verify discrete structural constraints, examples, and toy/chart models. They do not construct the Dolbeault-chiral hCS-to-Hall quasi-isomorphism for compact CY3s.

Heal: Use the compute output as sanity checks only.

Observed API values:

- `EnFromFraming.native_en(3) = E_1`.
- `EnFromFraming.has_braiding(3) = False`.
- `JordanQuiverS3Framing().full_verification()["all_paths_pass"] = True`.
- `ConifoldS3Framing().full_verification()["all_paths_pass"] = True`.
- `master_s3_framing_verification()["all_pass"] = True`.
- `all_cy3_shadow_data()["K3 x E"].kappa_BKM = 5`.
- `all(consistency_checks().values()) = True` for the BTZ engine.

Status: compute confirms the E1/no-native-braiding discipline and example-level arithmetic. It does not close the CY3 compact hCS theorem.

## Verification Commands

Targeted tests requested by the prompt:

```bash
python3 -m pytest compute/tests/test_s3_framing_chain_level.py compute/tests/test_swiss_cheese_cy3_e1.py compute/tests/test_btz_cy3_e1_engine.py -q
```

Result:

```text
359 passed in 0.96s
```

Explicit API probe:

```text
native_en_d3= E_1
has_braiding_d3= False
jordan_all_paths_pass= True
conifold_all_paths_pass= True
master_all_pass= True
shadow_names= ['C^3', 'K3 x E', 'local P^2', 'quintic', 'resolved conifold']
k3xe_kappa_BKM= 5
btz_consistency_all= True
```

## Recommendations to the Integrator

1. Keep `chapters/theory/cy3_chain_level_bridge.tex:227` ("No CFG shortcut") intact and strengthen it, if manuscript editing is later authorized, by explicitly saying that `C^*(g)` is only the locally constant/topological associated model.

2. In any CY3 hCS statement, write the object as
[
  CE^*_{dbar,chir}(Omega^{0,*}_c(-,g),O_X)
]
or as the Costello--Gwilliam factorization observables of the Dolbeault local Lie algebra. Do not write only `C^*(g)`.

3. Separate theorem/heuristic status:

- Theorem/conditional theorem: classical hCS BV complex and classical CE observables; flat `C^3` local quantum observables when anomaly cancellation/QME is verified.
- Heuristic/conditional: generic compact CY3 quantum hCS and compact hCS-to-Hall comparison.
- Open: `Theta_{hCS -> Hall}^{or}`.

4. State the BV Laplacian as a Dolbeault/BM heat-kernel contraction on hCS fields. CFG's BV Laplacian computation is a useful model, not the hCS computation.

5. Preserve the `E_1` output discipline at `d=3`. The `E_3` structure belongs to the ambient holomorphic factorization algebra of local observables; the CY-to-chiral output at the curve-specialized/chiral stage is `E_1`, with `E_2` recovered through centers or separate geometric machinery.

6. For compact/noncompact CY3s, require explicit anomaly and orientation data before upgrading status. `C^3` and toric chart evidence is not a compact theorem.

## Final Classification

CONVERGED with caveats.

No fatal contradiction was found in the local hCS BV-BRST construction on flat `C^3` when it is stated as a Dolbeault/chiral CE factorization algebra. The fatal overclaim would be to replace it by CFG's ordinary `C^*(g)` or to use CFG as the hCS-to-Hall comparison. The correct healed statement is:

[
  Obs_hCS^q(C^3,g)
  \text{ is a Dolbeault/chiral CE factorization algebra with holomorphic jets in }
  z_1,z_2,z_3,
]
whose locally constant/topological shadow can be compared with CFG-style filtered `E_3` Chern-Simons observables, while the Hall comparison and compact CY3 extension remain open/conditional.
