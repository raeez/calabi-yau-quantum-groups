# Agent 11: Kontsevich-Soibelman Formality and Deformation Examiner

Date: 2026-04-24.

Owned file: `notes/adversarial_swarm_20260424_cfg_e3/agent_11_kontsevich_soibelman_formality.md`.

Scope: chain-level `Phi` on CY3, especially the formality and deformation
steps behind
[
  \Phi_3^{(\Sigma_2,C)}
  =
  \operatorname{SpCh}_{\Sigma_2,C}\circ \Phi^{\mathrm{FA}}_3,
]
compared with Costello-Francis-Gwilliam 2026, arXiv:2602.12412.

No manuscript file was edited.

## Executive Verdict

CFG proves a theorem for ordinary real 3-dimensional Chern-Simons theory:
BV quantization produces a locally constant filtered `E_3` factorization
algebra whose classical associated model is ordinary Lie cochains
`C^*(g)`. That theorem is useful as a topological associated model and as
a normal-form test for filtered `E_3` deformation theory. It is not the
CY3 avatar.

The Vol III CY3 avatar is the many-variable Dolbeault/chiral CE and
factorization-enveloping object. On a holomorphic polydisc
`P = D_1 x D_2 x D_3` it retains
[
  \Omega^{0,*}_c(P,g)[1],
  \qquad \bar\partial,
  \qquad
  J^\infty_{\mathrm{hol}} \Omega^{0,*}_c(P,g),
]
holomorphic jets in `z_1,z_2,z_3`, products over disjoint polydiscs, and
multidirectional residues along all partial diagonals. The ordinary
`C^*(g)` appears only after the locally constant contraction
[
  \Omega^{0,*}(P)\simeq C,\qquad
  J^\infty_{\mathrm{hol}}L_{\hCS}\rightsquigarrow g.
]

Agent 11 verdict: the formality/deformation bridge survives only in a
stratified form.

1. Kontsevich-Tamarkin/Fresse-Willwacher `E_3` formality is theorem-level.
2. The formality choice is a `GRT_1`-torsor, not a literal point before
   quotienting.
3. Costello-Gwilliam topological locality is theorem-level for the
   topological factorization algebra step.
4. The holomorphic/Dolbeault refinement at CY3 is conditional on the
   stated chain-level framing, anomaly, and renormalization hypotheses.
5. The hCS-to-Hall comparison `Theta_{hCS->Hall}` is open; without it,
   KS wall-crossing compatibility remains a Hall-side theorem, not a
   theorem about `PhiFA_3`.

## Sources Read

Primary CFG source:

- Costello-Francis-Gwilliam, *Chern-Simons factorization algebras and knot
  polynomials*, arXiv:2602.12412v1, submitted 2026-02-12,
  https://arxiv.org/abs/2602.12412.
- Extracted arXiv source `2025draft.tex`: lines 343-397 identify the
  locally constant topological `E_3` algebra and `C^*(g)` model; lines
  1701-1710 give the Poincare quasi-isomorphism to `C^*(g)`; lines
  1717-1754 compute the deformation complex as reduced Lie cochains
  shifted by 3, with obstruction `H^4(g)` and deformation `H^3(g)`;
  lines 1861-1874 prove the quantum observables are locally constant;
  lines 1901-1935 push along `T x R -> R`; lines 1940-1949 compute the
  first-order `-2`-shifted Poisson bracket; lines 3670-3725 build the
  real configuration-space compactification and propagator.

Local anchors:

- `chapters/theory/cy_to_chiral.tex:242-269`: two-stage factorization is
  conditional on verified loci and admissible specialization.
- `chapters/theory/cy_to_chiral.tex:280-298`: Stage 1 has three distinct
  steps; the holomorphic step is the CY3 chain-level obstruction.
- `chapters/theory/cy_to_chiral.tex:306-325`: rational `E_3` formality
  and the `GRT_1(Q)` torsor.
- `chapters/theory/cy3_chain_level_bridge.tex:45-109`: many-variable
  Dolbeault/chiral CE model and the explicit warning that `C^*(g)` is
  only a topological associated model.
- `chapters/theory/cy3_chain_level_bridge.tex:294-365`: no CFG shortcut
  and the open hCS-to-Hall comparison.
- `chapters/theory/quantum_chiral_algebras.tex:8-32`: hCS observables are
  a Stage-1 model, not the Hall algebra or curve-specialized algebra.
- `chapters/examples/coha_wall_crossing_platonic.tex:414-535`: KS
  wall-crossing is MC gauge on the motivic/classical Hall dgLA.
- Existing swarm reports 01-06 in this directory, read for collision
  avoidance and consistency.

## Status Matrix

| Bridge | Status | Verdict |
|---|---:|---|
| `C_*(D_3;Q) -> Ger_3` formality | Theorem, proved elsewhere | Kontsevich-Tamarkin/Fresse-Willwacher supplies the operadic formality input. |
| Formality choice for Stage 1 | Theorem, proved elsewhere | A `GRT_1(Q)` torsor. "Contractible choice" is correct only after quotienting by the torsor action. |
| Hochschild/Gerstenhaber data -> pointwise `E_3` algebra | Proposition under H1-H3 | Valid as Stage-1 step (a); not yet a holomorphic factorization algebra. |
| Pointwise `E_3` algebra -> topological `E_3` factorization algebra | Proposition/Theorem under Costello-Gwilliam locality | Valid as Stage-1 step (b). Depends on the topological factorization-envelope/locality hypotheses. |
| Topological `E_3` FA -> holomorphic `E_3` hFA on CY3 | Conditional proposition / conjectural at chain level outside verified loci | Requires Dolbeault operator, CY form, BV data, anomaly cancellation, and the `S^3` framing package. |
| hCS classical observables -> Dolbeault/chiral CE | Conditional theorem | Classical model is defensible; quantum model requires BV renormalization and anomaly cancellation. |
| CFG `C^*(g)` -> CY3 avatar | Rejected as theorem | CFG `C^*(g)` is only the locally constant/topological associated model. |
| CFG deformation complex `C_Lie^{>=1}(g)[3]` -> CY3 MC deformation complex | Rejected as direct import | The CY3 complex is local Dolbeault/BV/BCOV, not reduced finite Lie cohomology. |
| `Theta_{hCS->Hall}` | Open problem | First missing lemma for non-formal compact CY3. |
| KS wall-crossing as MC gauge | Theorem on Hall side | Applies to `PhiFA_3` only after `Theta_{hCS->Hall}` and orientation/descent compatibilities are constructed. |
| Stage-2 `SpCh_{Sigma_2,C}` pushforward | Conditional proposition | Must be applied to the Dolbeault/chiral object before taking locally constant shadows. CFG torus pushforward is a model, not the CY3 proof. |

## Attack-Heal Cycles

### Cycle 1: `E_3` formality is not a literal contractible point

Attack. The sentence "Stage 1 is pinned up to contractible choice by
Kontsevich-Tamarkin formality" can be false if read before quotienting:
the formality maps form a `GRT_1(Q)` torsor. Distinct associators give
distinct formality data, although equivalent after passing to the
appropriate homotopy quotient.

Heal. Split the statement.

[
  C_*(D_3;Q)\simeq Ger_3
]
is theorem-level. The moduli of choices is a `GRT_1(Q)` torsor. A
Stage-1 construction may be called canonical only after the torsor action
has been quotiented, or after a specific associator/graph-integral point
has been fixed.

Status. Theorem for operadic formality. Proposition under a fixed
formality datum for the Stage-1 implementation.

### Cycle 2: CFG `C^*(g)` cannot replace the CY3 Dolbeault object

Attack. CFG identifies classical observables on a real 3-ball with
`C^*(g)` because flat bundles on the ball are trivial and Poincare
contracts the de Rham complex. Importing this as the CY3 local algebra
erases the holomorphic variables.

Heal. Keep the forgetful sequence explicit:
[
  CE^{\mathrm{ch},E_3}_{*,\bar\partial}
  (J^\infty_{\mathrm{hol}}L_{\hCS}(P))
  \longrightarrow
  CE_*(g)
]
exists only after the locally constant contraction. The arrow loses
`z_1,z_2,z_3` jets, Dolbeault differential, polydisc factorization, and
three-directional residues. The theorem-level CY3 object is the
left-hand side, not the right-hand side.

Status. CFG theorem for ordinary 3d CS. Rejected as a theorem about
`PhiFA_3`.

### Cycle 3: Costello-Gwilliam-Li locality has three separate gates

Attack. The phrase "KT formality + CGL locality" can hide three different
maps:
[
  HH^*(C) -> E_3\mathrm{-Alg},\qquad
  E_3\mathrm{-Alg} -> FactAlg^{top}_{E_3}(X),\qquad
  FactAlg^{top}_{E_3}(X) -> E_3HolFA(X).
]
The first two are not the third. The third is precisely where Dolbeault
and CY data enter.

Heal. Retain the three-step decomposition from `cy_to_chiral.tex`.
Step (a) is KT/Fresse-Willwacher formality. Step (b) is
Costello-Gwilliam topological locality. Step (c) is Costello-Li
holomorphic/BV refinement with `Omega_X`, `barpartial_X`, gauge fixing,
counterterms, and anomaly cancellation. For `d=3`, step (c) is the
chain-level CY-A3 obstruction, not a formal consequence of CFG.

Status. Theorem/proposition for (a) and (b) under stated hypotheses.
Conditional proposition for (c) on verified CY3 loci; conjectural/open in
the non-formal compact case.

### Cycle 4: CFG deformation complex is the wrong MC complex for CY3

Attack. CFG's deformation complex is
[
  Def_{CS}\simeq C^{>=1}_{Lie}(g)[3],
]
so the obstruction/deformation groups are `H^4(g)` and `H^3(g)`. For
semisimple `g`, `H^4(g)=0`. This cannot be transported to CY3 hCS
without changing the complex.

Heal. The CY3 MC/deformation complex is local Dolbeault/BV/BCOV:
local functionals on `Omega^{0,*}(X,g)[1]`, with the BV bracket
determined by the CY pairing and propagator. The anomaly slot is quartic
for complex dimension 3, and the quantum CE differential includes
[
  \bar\partial^\vee + d_{CE} + \hbar\Delta_{BV}
  + \text{counterterms}.
]
CFG's `H^*(g)[3]` computation is a topological associated-model test,
not the CY3 obstruction theory.

Status. CFG deformation theorem stands. Direct CY3 import rejected.
CY3 deformation statement remains conditional on the Costello-Li
renormalization/anomaly package.

### Cycle 5: The `P_3` bracket is a test, not the multidirectional OPE

Attack. CFG computes a first-order `-2`-shifted Poisson bracket on
`C^*(g)[[hbar]]`, determined by the level pairing on linear observables.
This might be misread as the CY3 OPE law.

Heal. Use CFG's bracket as the topological normal form: a valid CY3
analogue must recover the same degree after forgetting to the locally
constant model. Before forgetting, the bracket is implemented by
Dolbeault/BV contractions and chiral OPE residues in three holomorphic
directions:
[
  a(z)b(w)\sim
  \sum_{\alpha\in N^3}
  (a_{(\alpha)}b)(w)
  (z_1-w_1)^{-\alpha_1-1}
  (z_2-w_2)^{-\alpha_2-1}
  (z_3-w_3)^{-\alpha_3-1}.
]
The CFG `S^2` binary-operation class sees the associated real
little-disks bracket. It does not see the holomorphic polydisc OPE data.

Status. CFG bracket theorem stands. CY3 multidirectional bracket is
conditional on the Dolbeault/chiral CE construction and its PBW/envelope
compatibilities.

### Cycle 6: KS wall-crossing is theorem-level on Hall data, not yet on `PhiFA_3`

Attack. Since KS wall-crossing is an MC gauge equation in the Hall dgLA,
one may try to declare compatibility with `PhiFA_3` automatic.

Heal. The Hall-side theorem is real:
[
  \Theta_{\zeta'}=\exp(\operatorname{ad}_{\alpha_W})(\Theta_\zeta)
]
in the motivic and classical Hall dgLAs, with the motivic/classical
specializations matched. But to transfer this to `PhiFA_3` one must
first construct
[
  \Theta_{hCS->Hall}^{or}:
  Obs^q_{hCS}(-,g)\to CoHA^{or}_{crit}(-)
]
as a morphism of oriented factorization cosheaves, respecting
Dolbeault locality, Weiss descent, determinant square roots,
Thom-Sebastiani, and Hall convolution. That is precisely the open
problem in the local CY3 bridge.

Status. Theorem on Hall side. Conditional/open as a bridge from
`PhiFA_3` to wall-crossing.

### Cycle 7: Stage 2 must push forward the chiral object, not its shadow

Attack. CFG's pushforward along `T x R -> R` proves that a locally
constant topological `E_3` algebra can yield a noncommutative `E_1`
deformation. If copied directly, this would replace
[
  \operatorname{SpCh}_{\Sigma_2,C}(\PhiFA_3(\mathcal C))
]
by a pushforward of `C^*(g)`.

Heal. Stage 2 must be applied before locally constant contraction:
[
  A_C(V)
  =
  \int_{\Sigma_2}^{fact}
  \PhiFA_3(\mathcal C)|_{\Sigma_2\times V}.
]
On the hCS model this means pushing forward the Dolbeault/chiral
envelope
[
  U_C^{fact,E_1}
  R\Gamma_{fact}
  \bigl(\Sigma_2,
  J^\infty_{\mathrm{hol}}L_{\hCS}|_{\Sigma_2\times C}\bigr),
]
then taking the chiral bar/CE object. The topological pushforward of
`C^*(g)` is only a decategorified associated model.

Status. Conditional proposition for `SpCh` under exactness/descent
hypotheses. CFG torus pushforward is only an analogy.

## Final Claim-Status Recommendations

1. `PhiFA_3` Stage 1: keep `ClaimStatusConditional` at CY3 chain level.
   The pointwise `E_3` formality step is theorem-level; the holomorphic
   hFA refinement is conditional.
2. CFG import: cite as "ordinary 3d CS locally constant filtered `E_3`
   model", never as hCS-to-Hall or CY3-to-chiral proof.
3. `C^*(g)`: mark explicitly as locally constant/topological associated
   model. It is not the CY3 object.
4. MC/deformation bridge: theorem for CFG; conditional for CY3
   Dolbeault/BV; direct identification rejected.
5. `Theta_{hCS->Hall}`: keep open. It is the first missing lemma for
   compact non-formal CY3.
6. KS compatibility: theorem inside the motivic Hall dgLA; conditional
   through `PhiFA_3` until `Theta_{hCS->Hall}` is built.
7. Stage 2: conditional on holomorphic pushforward/envelope exactness
   and Weiss/Ran descent. Apply it before taking locally constant
   shadows.

## Files Changed

Only this report.

## Verification

No manuscript build or test suite was run. The task was report-only.
