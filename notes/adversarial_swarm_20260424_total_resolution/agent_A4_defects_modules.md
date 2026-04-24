# Agent A4: CY3 Holomorphic Defects, Endpoint Modules, Trace, and Module-Level Hall Comparison

Date: 2026-04-24.

Owned scope: issue 4 in the total-resolution swarm. This report attacks
the live defect definition and trace proposition in
`chapters/theory/cy3_chain_level_bridge.tex` and compares CFG ordinary
Chern--Simons only as trace grammar.

Files intentionally changed: this report only.

## Executive Verdict

The current manuscript statement is structurally honest: it defines the
right holomorphic defect target and states only a formal conditional
trace theorem. I cannot turn it into an unconditional global existence
theorem from the data currently present in the repository.

The obstruction is not cosmetic. A global holomorphic perfect defect is
not a finite-dimensional CFG Wilson-line module transported into six
real dimensions. It is a compact/dualizable object in a stratified
holomorphic `E_{1 subset 3}` factorisation-module category whose local
curve action remembers normal holomorphic modes, Dolbeault compact
supports, endpoint duality, CY orientation, and Cech/Ran descent. The
local `C^3`, `gl_1` codimension-2 OPE engine verifies the normal
completion and the level
```tex
  J(z)J(w) \sim \frac{\Psi}{(z-w)^2},
  \qquad
  \Psi=-\sigma_2=-(h_1h_2+h_1h_3+h_2h_3),
```
but it does not construct global perfect modules, endpoint/puncture
descent, Hall modules, or Borcherds/DT traces.

The strongest truthful result is a two-stage conditional theorem:

1. The holomorphic defect category exists as the totalisation of local
   `E_{1 subset 3}` module categories once the Stage-1 algebra `F_X`,
   normal-completed local actions, transition functors, and endpoint
   one-sided module categories are supplied on the DWR/Ran nerve.
2. Perfect trace classes exist for compact/dualizable trace-class
   objects in that category.
3. Hall/DT/Borcherds trace comparison requires a module-level lift of
   `Theta_{hCS->Hall}^{or}` and vanishing of the module obstruction
   tuple defined below.

CFG 2026 proves the corresponding ordinary real 3-dimensional theorem:
a filtered `E_3` algebra from BV quantised ordinary Chern--Simons,
perfect modules from finite-dimensional `U_hbar(g)` representations,
and equality of factorisation-homology traces with
Reshetikhin--Turaev link invariants. That is the grammar. It is not the
CY3 holomorphic construction.

Primary external anchor used:
`https://arxiv.org/abs/2602.12412`.

## Local Anchors

- `chapters/theory/cy3_chain_level_bridge.tex:500`: warning forbidding a
  CFG shortcut from ordinary CS to CY3 hCS/Hall.
- `chapters/theory/cy3_chain_level_bridge.tex:520`: live definition of
  holomorphic perfect defects.
- `chapters/theory/cy3_chain_level_bridge.tex:539`: normal-completed
  curve algebra
  `Omega_c^{0,*}(D_z,J_hol^infty(l_C|_C) hat tensor Symhat(N^vee))[1]`.
- `chapters/theory/cy3_chain_level_bridge.tex:559`: formal holomorphic
  defect trace proposition.
- `chapters/theory/cy3_chain_level_bridge.tex:592`: explicit statement
  that Hall traces require vanishing cycles, orientation square roots,
  charge/HN completions, and Thom--Sebastiani compatibility.
- `chapters/theory/cy3_chain_level_bridge.tex:602`: open hCS-to-Hall
  comparison.
- `chapters/theory/cy3_chain_level_bridge.tex:660`: base
  hCS--Hall descent obstruction complex.
- `chapters/theory/cy_to_chiral.tex:518`: witnessed admissible
  specialisation datum; the trace theorem must use this datum before
  applying Stage 2.
- `compute/lib/hcs_codim2_defect_ope.py:1`: local codimension-2 defect
  OPE witness on `C^3`.
- `compute/tests/test_hcs_codim2_defect_ope.py:1`: tests for the local
  OPE witness.

## Attack-Heal Cycle 1: Existence of the Global Category

Attack. The definition
```tex
  M \in HolMod_{F_X}(X,C,S)
```
is not itself an existence theorem. To prove existence, one must build
the local `E_{1 subset 3}` module categories on every normal chart and
prove that restriction along DWR inclusions preserves the module
structure, compact objects, duals, and finite Tor-amplitude. None of
this follows from CFG because CFG is locally constant on real 3-balls,
where the classical local model collapses to `C^*(g)`. Here the local
model retains holomorphic jets in three variables and normal formal
modes.

Heal. The construction that can honestly be stated is:
```tex
  HolMod_{F_X}(X,C,S)
  :=
  Tot Cech_DWR(
    U_I |-> Mod^{hol}_{E_{1 subset 3}}(
      F_X|_{U_I}, L^hat_{X,C}|_{U_I}, {M_p}_{p in S cap U_I}
    )
  ).
```
This is a definition of an infinity category under the following
explicit hypotheses:

- `F_X` is already constructed as a Stage-1 `E_3` holomorphic
  factorisation algebra on the framed CY3 locus.
- The local normal-completed curve algebras
  ```tex
    L^hat_{X,C}(D_z)
    =
    Omega_c^{0,*}(D_z,
      J_hol^infty(l_C|_C) hat tensor Symhat(N_{C/X}^vee))[1]
  ```
  act on the curve coefficients.
- Pullback along every DWR refinement is a continuous exact
  `E_{1 subset 3}` module functor.
- The descent totalisation is taken in presentable stable infinity
  categories, and the compact/dualizable subcategory is preserved by the
  transition functors.

Status recommendation: the category exists conditionally from these
data. Non-emptiness of the perfect trace-class subcategory remains a
separate theorem/obstruction problem.

## Attack-Heal Cycle 2: Perfectness

Attack. Compactness and dualisability are not automatic in
normal-completed holomorphic modules. Completion can destroy compactness.
Infinite normal jets can destroy finite Tor-amplitude. Endpoint duals
can fail to glue even when the underlying curve module glues.

Heal. The correct perfectness condition is not merely "finite
representation" but the conjunction:
```tex
  M in HolMod_{F_X}(X,C,S) is perfect
```
if and only if:

1. each local curve module is compact in the local holomorphic
   factorisation-module category;
2. each local module is finite over the completed algebra
   `U^{fact,E_1}(L^hat_{X,C})`;
3. the completed tensor product is nuclear/projective enough that
   continuous duals preserve the required evaluation maps;
4. local Tor-amplitude is finite and uniformly bounded on DWR
   intersections;
5. endpoint objects `M_p,M_p^vee` satisfy zigzag identities in the
   one-sided module category;
6. CY orientation data identify the left and right traces without a
   residual determinant-line sign;
7. the object is trace-class for the continuous Dolbeault complex.

This condition is the holomorphic CY3 analogue of CFG perfectness. It is
not a corollary of CFG perfectness.

## Attack-Heal Cycle 3: Endpoint and Puncture Data

Attack. The manuscript currently names endpoint objects and zigzag
identities. That is necessary but not sufficient for CY3 punctures. A
class-S or K3xE puncture carries monodromy, nearby-cycle, flavour, and
normal-mode residue data. A CFG line endpoint is not a CY3 puncture.

Heal. A CY3 endpoint/puncture datum at `p in S` should be the tuple
```tex
  P_p =
  (M_p, M_p^vee, ev_p, coev_p,
   rho_p, R_p, nu_p, o_p, m_p)
```
where:

- `M_p,M_p^vee` are compact one-sided modules for the punctured local
  algebra on `D_z^* x formal N_{C/X,p}`;
- `ev_p` and `coev_p` satisfy the zigzag identities;
- `rho_p` is the monodromy/nearby-cycle action around the puncture;
- `R_p` records the normal-mode residue operation;
- `nu_p` is the flavour or class-S label when present;
- `o_p` is the orientation-line square-root choice induced from the
  local Hall/DT orientation problem;
- `m_p` is the charge/completion convention.

The endpoint obstruction is the failure of this tuple to be invariant
under restriction around the punctured DWR nerve and under collision of
punctures. It lives in the module obstruction complex below.

Status recommendation: the current definition is acceptable as a first
definition; a future manuscript theorem should add the above puncture
datum before claiming class-S or K3xE module traces.

## Attack-Heal Cycle 4: Trace Theorem

Attack. A formal trace in stratified factorisation homology is not a
Hall, DT, RT, or Borcherds trace. The current proposition already says
this. The only additional pressure point is that "factorisation
homology gives a trace class" still depends on trace-classness and
dualisability in the completed holomorphic module category.

Heal. The strongest conditional trace theorem is:

```tex
Theorem (conditional holomorphic defect trace).
Let X be a framed CY3, F_X a constructed Stage-1 E_3 holomorphic
factorisation algebra, i:C -> X a holomorphic curve, S subset C finite,
and M in HolMod^{perf}_{F_X}(X,C,S). Assume:

(T1) M is compact and dualisable in the stratified holomorphic module
     category.
(T2) M is trace-class for the completed Dolbeault complexes.
(T3) endpoint duals satisfy the zigzag identities after DWR descent.
(T4) the witnessed specialisation datum s=(Sigma_2,C,...) of
     Definition def:witnessed-admissible-specialisation-datum is fixed.

Then the categorical trace
  Tr^{hol}_{F_X}(M) in int_{(X,C,S)}(F_X,M)
exists. Applying SpCh_s gives a trace class
  SpCh_s Tr^{hol}_{F_X}(M)
in the factorisation homology trace of the E_1 chiral algebra
  A_C=SpCh_s(F_X).
```

Proof skeleton. Local evaluation/coevaluation maps define the trace on
each normal chart. DWR descent glues them because the endpoint zigzags,
compactness, and normal-completed action are part of the descent datum.
Trace-classness makes the continuous Dolbeault trace converge. The
witnessed Stage-2 datum gives the exact pushforward/restriction functor
needed to transport the class to `A_C`.

This is precisely the CY3 holomorphic analogue of the CFG trace grammar,
but not a Hall/DT/Borcherds theorem.

## Attack-Heal Cycle 5: Module-Level hCS-to-Hall Comparison

Attack. Even if the base algebra comparison
`Theta_{hCS->Hall}^{or}` exists, a module comparison does not follow
formally. A module map must compare:

- holomorphic normal-completed `E_{1 subset 3}` modules;
- Hall modules over critical CoHA correspondences;
- endpoint duality and trace maps;
- vanishing-cycle orientation local systems;
- Thom--Sebastiani tensor product for module convolution;
- charge/HN completions and stability chambers.

Heal. Fix a base chartwise algebra comparison
```tex
  theta_i:
  Obs^q_hCS(U_i,g) -> CoHA^{or}_{crit}(U_i)
```
and a holomorphic defect `M`. Let `N` be a candidate Hall module. For
each DWR intersection `U_I`, set
```tex
  N^q_{mod}(U_I)
  :=
  Hom^q_{cont, theta_I-mod}
  (
    M_hol(U_I),
    N_Hall(U_I)
  ).
```
The total module comparison complex is
```tex
  M_{hCS,Hall}^{mod}(U)
  :=
  Tot Cech^bullet(U, N^bullet_{mod}).
```
It is a filtered dg module over the base dg Lie algebra
`M_{hCS,Hall}(U)` of `cy3_chain_level_bridge.tex:660`. Equivalently,
the pair `(theta, eta)` is governed by the semidirect convolution
dg Lie algebra
```tex
  M_{hCS,Hall}^{pair}
  =
  M_{hCS,Hall} lt M_{hCS,Hall}^{mod}.
```
A degree-zero pair `(theta,eta)` is a module comparison datum when
```tex
  d theta + 1/2[theta,theta] = 0,
  d_theta eta = 0,
```
and each `eta_i` is a quasi-isomorphism of local modules after the
chosen completion, orientation, shifts, Tate twists, and charge
convention.

The module obstruction tuple is
```tex
  o_mod(theta,eta)
  =
  (
    o_MC^mod,
    o_or^mod,
    o_end,
    o_punc,
    o_TS^mod,
    o_tr,
    o_comp
  ).
```
Here:

- `o_MC^mod in H^1(M_{hCS,Hall}^{mod})` is the Cech/chain/module-map
  obstruction `d_theta eta`.
- `o_or^mod` is the determinant-line square-root mismatch for the
  module virtual normal complex.
- `o_end` is the failure of endpoint evaluation/coevaluation maps to
  match under `eta`.
- `o_punc` is the mismatch of nearby-cycle monodromy, residue, and
  puncture flavour data.
- `o_TS^mod` is the Thom--Sebastiani associator defect for module
  convolution.
- `o_tr` is the failure of holomorphic and Hall traces to commute with
  evaluation/coevaluation.
- `o_comp` is the mismatch of charge/HN completions and stability
  chamber filtrations.

Conditional comparison theorem:

```tex
Assume the base obstruction o(theta)=0 from
Definition def:hcs-hall-descent-obstruction. A chartwise family of
module quasi-isomorphisms eta_i extends to a global module-level
hCS-to-Hall comparison

  Theta^{mod}_{hCS->Hall}(M): M_hol -> N_Hall

if and only if o_mod(theta,eta)=0 and the resulting class is invertible
in H^0(M_{hCS,Hall}^{mod}) on every DWR/Ran simplex. When this holds,
the holomorphic trace maps to the Hall trace:

  Theta^{tr}_{hCS->Hall}(Tr^{hol}_{F_X}(M))
  =
  Tr^{Hall}_{CoHA^{or}_{crit}}(Theta^{mod}_{hCS->Hall}(M)).
```

This is the missing theorem. It is not currently proved because no
candidate `eta` has been constructed for arbitrary CY3 defects, and the
base `theta` is itself still an obstruction problem.

## Local Computable Core

The local `C^3`, `gl_1` witness survives.

Input:
```tex
  X=C^3,\qquad C=C_{z_1},\qquad N_{C/X}=C_{z_2}\oplus C_{z_3},
  \qquad h_1+h_2+h_3=0.
```

Normal-mode expansion:
```tex
  A(z_1,z_2,z_3,\bar z)
  =
  sum_{m,n>=0} A^{(m,n)}(z_1,\bar z_1) z_2^m z_3^n.
```

Defect Heisenberg OPE:
```tex
  J(z)J(w) \sim \frac{\Psi}{(z-w)^2},
  \qquad
  \Psi=-\sigma_2.
```

For `gl_1`, the Virasoro central charge in the witness is `c=1`.
This is verified by `compute/lib/hcs_codim2_defect_ope.py` and
`compute/tests/test_hcs_codim2_defect_ope.py`.

This is evidence for the normal-completed definition at
`cy3_chain_level_bridge.tex:539`. It is not evidence for K3xE global
defects or Hall/Borcherds traces.

## CFG Comparison: Grammar Only

CFG 2026 proves, for ordinary 3d Chern--Simons:

- a filtered `E_3` algebra by BV quantisation of ordinary CS;
- finite-dimensional `U_hbar(g)` representations define perfect
  modules for that algebra;
- factorisation-homology trace over a framed link agrees with the
  Reshetikhin--Turaev invariant.

The CY3 analogue differs at every load-bearing point:

| CFG ordinary CS | CY3 hCS defect lane |
|---|---|
| real 3-ball | complex 3-fold polydisc |
| locally constant model `C^*(g)` | many-variable Dolbeault/chiral CE |
| finite `U_hbar(g)` representation | normal-completed holomorphic module |
| line endpoint | holomorphic puncture with normal residues |
| RT trace | holomorphic factorisation trace |
| no critical CoHA target | Hall comparison needs vanishing cycles/orientations |
| no Borcherds denominator | BKM trace needs additional automorphic comparison |

Therefore CFG should remain cited only as:

```tex
ordinary CS trace grammar and locally constant shadow,
not the construction of CY3 holomorphic perfect defects.
```

## Status Recommendations

1. Keep `def:cy3-holomorphic-perfect-defect` definitional.
2. Keep `prop:cy3-holomorphic-defect-trace` conditional, but a future
   manuscript edit should expand its hypotheses to include trace-class
   continuous duals and endpoint/puncture descent.
3. Add a separate definition of the module obstruction complex if the
   total-resolution integration owner wants issue 4 represented in the
   manuscript at the same level as the base hCS--Hall obstruction.
4. Do not state a K3xE Hall/BKM module trace theorem until both the base
   obstruction `o(theta)` and module obstruction `o_mod(theta,eta)`
   vanish.
5. Use the local codimension-2 OPE witness only as a local theorem for
   the normal-completed model.

## Commands Run

```bash
python3 -m pytest compute/tests/test_hcs_codim2_defect_ope.py compute/tests/test_wilson_stratified_fh.py -q
```

Result:

```text
110 passed in 21.62s
```

## Files Changed

```text
notes/adversarial_swarm_20260424_total_resolution/agent_A4_defects_modules.md
```

No manuscript file was edited by this agent.
