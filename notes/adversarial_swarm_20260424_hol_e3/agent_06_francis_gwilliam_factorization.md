# Agent 06 -- Francis-Gwilliam Factorization

Date: 2026-04-24.

Scope: compare the Costello--Francis--Gwilliam topological Chern--Simons
factorization-homology theorem with the CY3 holomorphic Stage-1
`E_3` object in `chapters/theory/cy3_chain_level_bridge.tex`.  No
chapter or compute file was edited.

## Verdict

CFG 2026 supplies a theorem-grade model for ordinary real 3-dimensional
Chern--Simons theory: perturbative BV quantization gives a filtered
`E_3` algebra `A_lambda`, its classical local model is
`C^*(g)` after the Poincare contraction on a real 3-ball, and perfect
modules attached to finite-dimensional `U_hbar(g)` representations
produce Reshetikhin--Turaev link traces by factorization homology.

CFG does not supply the CY3 holomorphic `E_3` object.  The CY3 object in
the bridge is the Dolbeault/chiral CE factorization algebra on a
holomorphic polydisc
`P = D_1 x D_2 x D_3`:

```tex
\mathfrak L_{\mathcal C}(P)
  =
\Omega_c^{0,\bullet}
\bigl(P,J^\infty_{\mathrm{hol},z_1,z_2,z_3}
\mathfrak l_{\mathcal C}\bigr)[1],
\qquad
d_{\mathfrak L}=\bar\partial+d_{\mathfrak l},
```

```tex
\Obs_{\mathcal C}^{cl}(P)
  =
C^\bullet_{\mathrm{Lie,cont}}
  \bigl(\mathfrak L_{\mathcal C}(P),\mathbb C\bigr).
```

The ordinary `C^*(g)` is only the locally constant associated model
after

```tex
\Omega^{0,\bullet}(P)\simeq\mathbb C,
\qquad
J^\infty_{\mathrm{hol}}\mathfrak l_{\mathcal C}
  \rightsquigarrow H^\bullet(\mathfrak l_{\mathcal C,x}),
```

and in the constant hCS chart this becomes `C^*(g)`.  Before that
forgetful operation, replacing the CY3 object by `C^*(g)` is false.

Local anchors:

- `chapters/theory/cy3_chain_level_bridge.tex:45`: many-variable
  Dolbeault/chiral CE normal form.
- `chapters/theory/cy3_chain_level_bridge.tex:102`: `C^\bullet(g)` only
  after the locally constant shadow.
- `chapters/theory/cy3_chain_level_bridge.tex:301`: no CFG shortcut.
- `chapters/theory/cy3_chain_level_bridge.tex:324`: open
  orientation-preserving `Theta_{hCS->Hall}^{or}` comparison.
- `chapters/theory/cy3_chain_level_bridge.tex:547`: conditional
  Stage-1 envelope theorem.
- `chapters/theory/cy3_chain_level_bridge.tex:611`: side-by-side with
  CFG.
- `notes/adversarial_swarm_20260424_cfg_e3/SYNTHESIS.md:14`: CFG
  theorem-grade scope for real 3d CS.
- `notes/adversarial_swarm_20260424_cfg_e3/SYNTHESIS.md:20`: CY3 data
  retained and not present in CFG.
- `notes/adversarial_swarm_20260424_cfg_e3/SYNTHESIS.md:70`: claims
  killed by the previous swarm.
- `notes/adversarial_swarm_20260424_cfg_e3/SYNTHESIS.md:173`: open
  obligations.

Primary-source anchors:

- Costello--Francis--Gwilliam 2026, arXiv:2602.12412, Theorem 1.1:
  filtered `E_3` algebra by BV quantization of CS for semisimple
  `g`, perfect modules from `U_hbar(g)` representations, and equality
  with RT link invariants.
- CFG 2026, Proposition 4.1: a level
  `lambda in hbar H^3(g)[[hbar]]` produces a nontrivial deformation
  `A_lambda` of `A_cl = C^*(g)` as a filtered `E_3` algebra.
- CFG 2026, Section 4.2 and Lemma 4.3: for `M = R^3`,
  `C^*(Omega^*(R^3) tensor g) ~= C^*(g)` by the Poincare
  quasi-isomorphism, and the locally constant factorization algebra
  defines the filtered `E_3` algebra.
- CFG 2026, Proposition 4.6: BV quantization gives a factorization
  algebra of quantum observables reducing mod `hbar` to the classical
  observable factorization algebra.

## Side-by-side theorem spine

| Slot | CFG/topological CS | CY3 holomorphic Stage 1 |
|---|---|---|
| Space | real `R^3`, ordinary topological CS | complex CY3 `X`, holomorphic polydiscs `D_1 x D_2 x D_3` |
| Fields | `Omega^*(M) tensor g` around the trivial flat bundle | `Omega_c^{0,*}(P,J^\infty_hol l_C)[1]` with `dbar+d_l` |
| Classical observables | `C^*(Omega^*(M) tensor g)`, locally `C^*(g)` on `R^3` | continuous Dolbeault/chiral CE cochains on `mathfrak L_C(P)` |
| Local constancy | theorem-grade: de Rham complex is locally constant | not locally constant until the shadow is explicitly applied |
| `E_3` source | locally constant factorization algebra gives a framed 3-disk algebra | conditional holomorphic `E_3` factorization algebra in `E_3-HolFA(X)` |
| Quantization | filtered deformation `A_lambda` of `C^*(g)` | hCS quantization anomaly-gated; quartic slot in complex dimension 3 |
| Modules/traces | perfect `A_lambda` modules yield RT traces for links in `R^3` | holomorphic perfect defect/module category remains an open obligation |
| Hall target | absent | `Theta_{hCS->Hall}^{or}` is open and must land in oriented critical CoHA |
| `W_{1+infty}` | absent | only after `CoHA(C^3)=Y^+`, Drinfeld double, and Fock/evaluation |

## ATTACK -> HEAL cycles

### Cycle 1 -- The false `Phi^{FA}_3 = C^*(g)` shortcut

ATTACK.  Use CFG Proposition 4.1 to assert that the CY3 Stage-1
factorization algebra is `C^*(g)` as a filtered `E_3` algebra.

FAILURE MODE.  CFG's `C^*(g)` is obtained from
`C^*(Omega^*(R^3) tensor g)` by Poincare contraction on a real
3-ball.  The CY3 local model is
`C^\bullet_Lie,cont(mathfrak L_C(P), C)` with
`mathfrak L_C(P)=Omega_c^{0,*}(P,J^\infty_hol l_C)[1]`.  The
Dolbeault differential, holomorphic jets, compact-support convention,
and three-variable residue calculus are still present.  The manuscript
already records that `C^\bullet(g)` appears only after the locally
constant shadow.

HEAL.  The theorem-grade statement is:

```tex
\Phi^{FA}_3(\mathcal C)|_P
  \simeq U^{fact,E_3}_P(\mathfrak L_{\mathcal C})
```

on the loci where the hCS realization is available.  Applying the
shadow
`Omega^{0,*}(P) ~= C` and
`J^\infty_hol l_C -> H^*(l_{C,x})` gives
`C^*(H^*(l_{C,x}))`, and only in the constant hCS chart gives
`C^*(g)`.  CFG proves the associated locally constant topological
model, not the CY3 holomorphic object.

Status recommendation: keep `ClaimStatusConditional` for the Stage-1
envelope and `ClaimStatusDefinitional` for the no-shortcut warning.

### Cycle 2 -- The false locally constant theorem for holomorphic CY3

ATTACK.  Transfer CFG Lemma 4.3 directly: because the real CS
observable factorization algebra is locally constant, the CY3
holomorphic factorization algebra should also be locally constant and
hence determined by its value on one polydisc.

FAILURE MODE.  CFG local constancy is a consequence of the de Rham
Poincare lemma for `Omega^*(R^3)`.  The CY3 object is holomorphic:
singularities sit on partial diagonals in
`z_1,z_2,z_3`, and OPE coefficients are iterated residues indexed by
`alpha in N^3`.  The holomorphic jet sheaf is not discarded by the
Stage-1 construction.  Collapsing it before specialization erases the
chiral data the bridge is built to retain.

HEAL.  The correct comparison is two-step:

1. CFG supplies the topological factorization-envelope grammar:
   `E_3-Alg(Ch) -> FAct(R^3;Ch)`.
2. Costello--Li holomorphic twisting and the CY form supply the extra
   Dolbeault refinement landing in `E_3-HolFA(X)`.

The manuscript's formula

```tex
\PhiFA_3(\mathcal C)
  =
\mathrm{Hol}_X(\mathcal U^{FA}(\HH^\bullet(\mathcal C)))
```

is therefore not a CFG theorem by itself.  It is a conditional Stage-1
CY3 statement using Costello--Gwilliam locality plus Costello--Li
holomorphic twisting and the local CY3 CE normal form.

Status recommendation: do not mark the holomorphic Stage-1 theorem as
proved by CFG; leave it conditional on the Stage-1 verified locus.

### Cycle 3 -- The false CFG proof of `Theta_{hCS->Hall}`

ATTACK.  Use CFG factorization homology traces and the theorem
`CoHA(C^3)=Y^+` to declare the hCS-to-Hall comparison map constructed.

FAILURE MODE.  CFG has no Hall target.  It produces a factorization
algebra of topological CS observables and perfect modules used for RT
traces.  It does not produce vanishing-cycle Borel--Moore complexes,
orientation local systems, determinant-line square roots, Tate twists,
charge/HN completions, equivariant-localized completions, or
Thom--Sebastiani coherences.  Chartwise `CoHA(C^3)=Y^+` is only the
algebraic Hall core after the Hall object has already been constructed.

HEAL.  The bridge must keep the dashed arrow dashed:

```tex
\Theta_{\hCS\to\Hall}^{or}:
  \Obs_{\hCS}^{q}(-,\mathfrak g)
  \longrightarrow
  \CoHA_{\mathrm{crit}}^{or}(-).
```

The map must be a morphism in
`FactCosh_Hall^{or,wedge}(X)`, not a slogan-level quasi-isomorphism.
It must preserve orientation data, shifts, Tate twists, completions,
overlap coherences, BV/Hall products after the CY3 shift, and
Thom--Sebastiani.  CFG contributes no proof of this datum.

Status recommendation: keep
`op:cy3-hcs-hall-comparison` open; toric descent remains conditional
on this map.

### Cycle 4 -- The false perfect-module transfer

ATTACK.  Since CFG proves that finite-dimensional `U_hbar(g)`
representations define perfect `A_lambda` modules, treat those modules
as CY3 Hall/BKM/DT modules and use their traces as CY3 BPS traces.

FAILURE MODE.  CFG modules live over the topological CS `E_3` algebra
`A_lambda` and are designed for link defects in `R^3`.  CY3 Hall/BKM/DT
modules would have to know critical CoHA charges, stability, vanishing
cycles, orientation data, Drinfeld doubling, and possibly Fock/evaluation
for the vertex-algebra endpoint.  No functor from CFG perfect modules to
oriented critical-CoHA modules is constructed in CFG or in the current
CY3 bridge.

HEAL.  The theorem-grade transfer allowed by CFG is exactly this:
topological CS `A_lambda` plus a finite-dimensional `U_hbar(g)` module
gives an RT trace by factorization homology.  The CY3 bridge may use
this as a model for what a defect/module theorem should look like, but
the actual CY3 module category remains an open obligation:
construct holomorphic perfect defects with endpoint and puncture data
and compare them to Hall/DT modules through
`Theta_{hCS->Hall}^{or}`.

Status recommendation: any CY3 Hall/BKM/DT module statement based only
on CFG should be downgraded to an open construction, not an expected
theorem.

### Cycle 5 -- The false trace-to-Borcherds implication

ATTACK.  Use CFG's equality between factorization-homology traces and
Reshetikhin--Turaev invariants to infer Borcherds denominators, DT
traces, or black-hole entropy for CY3 targets.

FAILURE MODE.  CFG traces are link invariants in ordinary real
3-dimensional CS.  Borcherds denominators and DT traces require the
Hall/DT side: critical CoHA, positive half, Drinfeld double,
automorphic denominator, and the relevant BPS/duality comparison maps.
None of those structures follows from CFG's RT trace theorem.

HEAL.  The correct implication chain is typed:

```tex
\PhiFA_3(\mathcal C)
  \dashrightarrow
\CoHA_{\mathrm{crit}}(X)
  \to Y^+
  \to D(Y^+)
  \to \mathcal W_{1+\infty}
```

CFG supports only the left-hand factorization-algebra technology and
the topological trace pattern.  The Borcherds/DT/entropy conclusions
can be invoked only after the Hall comparison and the BPS/duality maps
are built.  Until then they remain conditional.

Status recommendation: keep holographic and quantum-gravity readings
conditional unless the BPS/Hall/duality comparison maps are explicitly
constructed.

### Cycle 6 -- The false `E_3 -> E_2` Yangian `R`-matrix

ATTACK.  Treat the nontrivial `S^2` operation in CFG's `E_3` algebra,
or a Dunn restriction from `E_3` to `E_2`, as the Yangian `R`-matrix
needed on the CY3 side.

FAILURE MODE.  CFG's shifted Poisson bracket comes from the `S^2` of
binary operations in `E_3` and is computed by descent of observables in
topological CS.  A Yangian `R`-matrix is representation-theoretic
braiding/half-braiding data.  In the CY3 manuscript the non-symmetric
braiding belongs on the constructed Drinfeld/derived center

```tex
\mathcal Z(\Rep^{E_1}(A_{\mathcal C}))
  \simeq
\Rep^{E_2}(Z^{der}_{ch}(A_{\mathcal C})),
```

not on the final `E_1` chiral algebra as a native `E_2` structure.

HEAL.  The CFG `E_3` operation may motivate the existence of a shifted
Poisson structure on topological observables, but it does not identify
the CY3 Yangian `R`-matrix.  The latter must be produced through the
Drinfeld/derived center or through the Hall--Drinfeld double after the
positive half is constructed.

Status recommendation: never cite CFG or Dunn additivity alone as the
Yangian `R`-matrix proof.

### Cycle 7 -- The false direct `CoHA(C^3)=W_{1+infty}` shortcut

ATTACK.  Combine CFG's topological `E_3` algebra with the toric
`C^3` local Hall computation and state directly
`CoHA(C^3)=W_{1+infty}`.

FAILURE MODE.  The local Hall theorem gives
`CoHA(C^3) ~= Y^+(\widehat{gl}_1)`, the positive half.  The
`W_{1+infty}` comparison is reached after Drinfeld doubling and
Fock/evaluation.  CFG does not change the algebra-half discipline: its
`A_lambda` is not the Hall positive half, not the Drinfeld double, and
not the vertex algebra endpoint.

HEAL.  The side-by-side theorem-grade statement is:

```tex
\CoHA(\mathbb C^3)\cong Y^+(\widehat{\mathfrak{gl}}_1),
\qquad
D(Y^+)\to \mathcal W_{1+\infty}.
```

The direct equality with `W_{1+infty}` remains false.  CFG supplies no
additional bridge allowing the positive half to skip doubling.

Status recommendation: keep every `C^3` Hall statement positive-half
first; mention `W_{1+infty}` only after double/evaluation.

## What CFG supplies

1. A theorem-grade perturbative BV quantization of ordinary real
   3-dimensional CS for semisimple `g` with invariant pairing/level.
2. A filtered locally constant `E_3` factorization algebra
   `A_lambda`, deforming `A_cl=C^*(g)`.
3. The classical local observable comparison
   `C^*(Omega^*(R^3) tensor g) ~= C^*(g)` by Poincare contraction.
4. A factorization-homology trace theorem matching RT link invariants.
5. Perfect-module technology for finite-dimensional Drinfeld--Jimbo
   quantum-group representations.
6. A useful grammar for the topological factorization envelope and
   descent of local observables.

## What CFG does not supply

1. No Dolbeault/chiral CE model on a CY3 polydisc.
2. No holomorphic jets in `z_1,z_2,z_3`.
3. No many-variable OPE or iterated-residue calculus.
4. No Costello--Li holomorphic twist landing in `E_3-HolFA(X)`.
5. No CY volume-form rigidification or quartic hCS anomaly analysis.
6. No negative-cyclic CY3 orientation witness or chain-level `S^3`
   framing for a cyclic `A_infty` input.
7. No oriented critical-CoHA target.
8. No `Theta_{hCS->Hall}^{or}`.
9. No Hall shifts, Tate twists, determinant-line square roots, or
   Thom--Sebastiani compatibility.
10. No proof that `CoHA(C^3)` is `W_{1+infty}` directly.
11. No CY3 Hall/BKM/DT perfect module category.
12. No Borcherds denominator, DT trace, or black-hole entropy theorem.

## Claim-status recommendations

- `warn:cy3-no-cfg-shortcut`: keep definitional warning.  It is
  mathematically necessary.
- `thm:cfg-factorization-envelope-stage-one`: keep conditional.
  CFG supports only the topological envelope component; Costello--Li
  holomorphic twisting and the CY3 verified locus are separate inputs.
- `op:cy3-hcs-hall-comparison`: keep open.  CFG does not touch the
  oriented Hall comparison.
- `prop:cy3-local-to-toric-descent-package`: keep conditional on the
  comparison map.
- Any assertion `Phi^{FA}_3(C)=C^*(g)` before the locally constant
  shadow: reject.
- Any assertion CFG proves CY3 Hall/BKM/DT traces: reject.

## Verification performed

- Read `CLAUDE.md` before work.
- Read `AGENTS.md` local swarm/report requirements.
- Read `chapters/theory/cy3_chain_level_bridge.tex`.
- Read `notes/adversarial_swarm_20260424_cfg_e3/SYNTHESIS.md`.
- Checked `bibliography/references.tex` for `CFG2026`.
- Checked arXiv:2602.12412 for Theorem 1.1, Proposition 4.1,
  Lemma 4.3, and Proposition 4.6.
- Did not run manuscript builds; no TeX source was edited.

Files changed:

- `notes/adversarial_swarm_20260424_hol_e3/agent_06_francis_gwilliam_factorization.md`

Remaining open obligations:

1. Prove the continuous Dolbeault/chiral CE to `E_3` bar identification
   with compact-support conventions fixed.
2. Construct `Theta_{hCS->Hall}^{or}` with orientation, shifts, Tate
   twists, completions, overlap coherences, and Thom--Sebastiani.
3. Build CY3 holomorphic perfect defect/module categories with endpoint
   and puncture data.
4. Prove holomorphic pushforward/envelope commutation for
   `SpCh_{\Sigma_2,C}` beyond the verified loci.
5. Keep `C^*(g)` confined to the locally constant associated model.
