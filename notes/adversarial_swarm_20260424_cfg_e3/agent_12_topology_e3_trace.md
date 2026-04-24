# Agent 12: Algebraic-Topology E3 Trace Examination

Date: 2026-04-24.

Owned file: `notes/adversarial_swarm_20260424_cfg_e3/agent_12_topology_e3_trace.md`.

Scope: Costello--Francis--Gwilliam 2026, arXiv:2602.12412, Sections 1.3, 1.8, and 2, against the Vol III chain-level `\Phi_3` / holomorphic CY3 factorization trace problem. No manuscript file was edited.

## Sources Read

Primary source:

- Costello--Francis--Gwilliam, *Chern--Simons factorization algebras and knot polynomials*, arXiv:2602.12412v1, official arXiv source and HTML. Sections read: 1.3, 1.8, 2; auxiliary source lines for the `C^*(\g)` model and trace theorem checked in the extracted `2025draft.tex`.

CFG anchors:

- Section 1.3: locally constant factorization algebras on `\mathbb R^3` are `E_3`-algebras by Lurie HA 5.4.5.9; classical CS disc observables are the filtered CE algebra `C^*(\g)`; quantum observables are a filtered `E_3` deformation of `C^*(\g)`.
- Section 1.8: for an `E_3` algebra `A`, left `A`-modules form an `E_2`-monoidal category; perfect modules give tangle TFTs by the Tangle Hypothesis; factorization homology computes the Reshetikhin--Turaev link invariants.
- Section 2: for an `E_n` algebra `A`, a perfect `A`-module `V`, and a framed link `K subset M`, the trace class
  `tr(V) in HH_*(A)^{\otimes \pi_0 K} ~= \int_{K x R^{n-1}} A`
  maps to `\int_M A`; in the CS case this trace equals the RT invariant.

Local anchors:

- `chapters/theory/cy3_chain_level_bridge.tex:45`: CY3 many-variable chiral CE model.
- `chapters/theory/cy3_chain_level_bridge.tex:98`: ordinary `C^\bullet(\g)` is obtained only after the locally constant shadow.
- `chapters/theory/cy3_chain_level_bridge.tex:294`: no CFG shortcut.
- `chapters/theory/cy3_chain_level_bridge.tex:317`: open hCS-to-Hall comparison.
- `chapters/theory/cy_to_chiral.tex:221`: two-stage `\PhiFA_d` / `\SpCh_{\Sigma_{d-1},C}` definition.
- `chapters/theory/cy_to_chiral.tex:271`: native curve-level output is `E_1` at `d >= 3`.
- `chapters/theory/cy_to_chiral.tex:280`: Stage 1 is a three-step assembly; holomorphic twist is the chain-level obstruction at `d >= 3`.
- `chapters/theory/cy_to_chiral.tex:4899`: `d=3` residual issues: hCS-to-Hall, parameter choice, global `G(\cC)`.
- `chapters/theory/en_factorization.tex:50`: `\SpCh` as framed factorization homology over `\Sigma_{d-1}`.
- `chapters/theory/en_factorization.tex:567`: CFG is ordinary 3d CS analogue, not 6d hCS-to-Hall theorem.
- `chapters/theory/en_factorization.tex:607`: topological `E_3` from 6d holomorphic theory remains conjectural/comparison-dependent.
- `chapters/theory/quantum_chiral_algebras.tex:20`: hCS observables as Dolbeault--chiral CE object; quantum statement requires BV renormalization and anomaly cancellation.
- `chapters/theory/quantum_chiral_algebras.tex:3641`: on `\mathbb C^3`, hCS observables are modeled as `CE^\bullet_{\bar\partial,\chir}` with Bochner--Martinelli OPE and `E_3` composition.
- `chapters/theory/braided_factorization.tex:26`: at `d=3`, braiding applies to the Drinfeld centre, not to the algebra itself.
- `chapters/theory/hochschild_calculus.tex:2886`: `E_2` lives on `Z(\Rep^{E_1}(A))`; naive `E_2` on the `d=3` algebra is killed.
- `chapters/theory/phi_universal_trace_platonic.tex:169`: the Vol III trace is a factorization-homology module trace, not an upstream Fourier--Mukai trace.

## Executive Verdict

CFG proves a topological theorem:

```tex
\Obs^{q}_{CS}(\mathbb R^3,\g,\lambda)
  =: \mathcal A^\lambda
```

is a locally constant filtered `E_3` factorization algebra deforming the filtered Lie cochain algebra

```tex
C^*(\g)=\Sym(\g^\vee[-1]),\qquad
F^i C^*(\g)=\Sym^{\ge i}(\g^\vee[-1]).
```

For a perfect `\mathcal A^\lambda`-module `V`, CFG's trace class in factorization homology over a framed link computes the Reshetikhin--Turaev invariant.

This is not the CY3 avatar. The CY3 avatar is the Dolbeault--chiral CE / enveloping factorization algebra in three holomorphic variables:

```tex
\mathfrak L_{\hCS}(P)
  = \Omega^{0,\bullet}_c(P,\g)[1],
\qquad
\Obs^{cl}_{\hCS}(P)
  =
C^\bullet_{\Lie,cont}(\mathfrak L_{\hCS}(P),\mathbb C),
```

or, after holomorphic jets,

```tex
\PhiFA_3(\cC)|_P
  \simeq
U^{\mathrm{fact},E_3}_{P}
\bigl(J^\infty_{\mathrm{hol}}\mathfrak L_{\hCS}\bigr),
\qquad
B_{E_3}(\PhiFA_3(\cC)|_P)
  \simeq
\mathrm{CE}^{\mathrm{ch},E_3}_*
\bigl(J^\infty_{\mathrm{hol}}\mathfrak L_{\hCS}\bigr).
```

It remembers holomorphic jets in `z_1,z_2,z_3`, multidirectional OPE residues on polydiscs, the Dolbeault differential, and the CE-to-chiral CE/enveloping factorization algebra. CFG's `C^*(\g)` is only the locally constant/topological associated model obtained after forgetting all of this structure.

## Attack/Heal Cycles

### Cycle 1: Local Constancy Implies `E_3`

Attack. Import CFG Section 1.3 literally: locally constant factorization algebras on `\mathbb R^3` are `E_3` algebras, hence CY3 hCS observables are ordinary `E_3` algebras of the same kind.

Failure mode. CFG uses real topological local constancy: for balls `D subset D'`, `Obs(D) -> Obs(D')` is a quasi-isomorphism. The CY3 object is holomorphic and Dolbeault-local. Ball inclusions are not the full structure; the object sees holomorphic polydiscs, partial diagonals, jets, and the Dolbeault resolution.

Heal. The surviving statement is:

```tex
\text{holomorphic factorization over polydiscs}
  + \text{Costello--Li/Gwilliam--Williams comparison}
  => \text{holomorphic } E_3 \text{ coherence on Stage 1}.
```

This is not Lurie's locally constant classification by itself. It requires the holomorphic comparison and the Dolbeault/Ran/Weiss descent hypotheses.

No-go condition. Any proof that uses only `Obs(D) ~= Obs(D')` for real balls and then replaces the CY3 object by `C^*(\g)` has left the CY3 problem.

### Cycle 2: `C^*(\g)` as the Source Algebra

Attack. Since CFG identifies classical local CS observables on a 3-ball with `C^*(\g)`, treat `C^*(\g)` as the chain-level `\PhiFA_3` local model.

Failure mode. The Vol III source explicitly says `C^\bullet(\g)` appears only after the locally constant shadow:

```tex
\Omega^{0,\bullet}(P) \simeq \mathbb C,\qquad
J^\infty_{\mathrm{hol}}\mathfrak L_{\hCS}\rightsquigarrow\mathfrak g.
```

Before this forgetful operation the local algebra has `\g[[z_1,z_2,z_3]]`-type holomorphic jets and OPE residues in three independent complex directions.

Heal. The repaired dictionary is:

```tex
\CE^\bullet_{\bar\partial,\chir}
\bigl(\Omega^{0,\bullet}_c(P,\g)[1],\mathcal O_P\bigr)
  -> \text{locally constant shadow}
  -> C^*(\g).
```

The first object is CY3. The last object is CFG's associated topological model.

No-go condition. `\PhiFA_3(\cC)|_P = C^*(\g)` is false unless the statement explicitly says "after taking the locally constant associated model / constant-mode shadow".

### Cycle 3: `E_3` Modules and Braided Categories

Attack. CFG says left modules over an `E_3` algebra form an `E_2`-monoidal category; therefore the CY3 chiral output should be natively braided.

Failure mode. CFG's conclusion concerns the module category of the topological `E_3` algebra. Vol III's curve-specialized output at `d=3` is native `E_1`. The `E_2` structure lives on the Drinfeld centre of the `E_1` module category:

```tex
\cZ(\Rep^{E_1}(A_\cC)),
```

not on `A_\cC` itself. The local files state this as a theorem for the `\mathbf H_{\Delta_5}` branch: the naive `E_2` multiplication on `A` is killed by the Francis non-concentration defect and absorbed by the centre.

Heal. The CFG module theorem survives as a categorical pattern:

```tex
E_3\text{ Stage-1 object}
  -> E_2\text{-monoidal defect/module category}
  -> \text{braiding after centre/defect passage}.
```

It does not change the native operadic level of `\Phi_3^{(\Sigma_2,C)}(\cC)`.

No-go condition. Any sentence "CFG proves the CY3 output is `E_2`-chiral" is wrong. The safe sentence is: "CFG models why an `E_3` Stage-1 object can produce braided module categories; in Vol III the `d=3` curve algebra remains `E_1`, and `E_2` is recovered on the Drinfeld centre."

### Cycle 4: Trace and Factorization Homology

Attack. CFG Section 2 defines

```tex
\int_{K\subset M}\tr(V) \in \int_M A
```

from `tr(V) in HH_*(A)^{\otimes \pi_0 K}`, so the CY3 trace should be ordinary Hochschild homology of the same `A=C^*(\g)`.

Failure mode. CFG's trace is a topological trace for framed real links `K subset M`, with coefficients in an `E_n` algebra and a perfect module. The CY3 trace must be a chiral/factorization trace of the Dolbeault--chiral CE/enveloping object after the Stage-2 specialization:

```tex
\Phi_3^{(\Sigma_2,C)}(\cC)
  =
\SpCh_{\Sigma_2,C}(\PhiFA_3(\cC))
  =
\left(\int_{\Sigma_2}\PhiFA_3(\cC)\right)\bigm|_C.
```

The trace complex is the chiral CE/bar complex of the Lie conformal algebra or its module category, not `HH_*(C^*(\g))` unless one has first taken the topological shadow.

Heal. The CY3 analog of the CFG trace has this conditional form:

```tex
\text{dualizable/trace-class defect } M
\in \Rep^{E_1}\bigl(\SpCh_{\Sigma_2,C}(\PhiFA_3(\cC))\bigr)
```

produces a chiral trace class in the factorization homology of the curve-specialized algebra. If one works before Stage 2, the class lives in factorization homology of the holomorphic `E_3` Stage-1 object over the relevant polydisc/cycle geometry.

No-go condition. It is invalid to identify the CY3 trace with CFG's RT trace unless a topological reduction has been performed and the defect/module is proved perfect in the reduced `E_3` category.

### Cycle 5: Framed Links versus Holomorphic Cycles

Attack. Replace CFG's framed link `K subset \mathbb R^3` by a CY3 holomorphic curve or by the pair `(\Sigma_2,C)` and reuse the same `E_{1\subset 3}` theorem.

Failure mode. CFG's Section 2 uses framed `(1 subset n)`-manifolds, the normal framing `K x R^{n-1} -> M`, and `E_{1\subset n}` coefficient systems. Vol III's data are holomorphic/categorical: an admissible cycle `\Sigma_2`, a curve `C`, Dolbeault pushforward, and chiral restriction. The normal bundle is complex-geometric, and anomaly/framing conditions are part of the CY3 theorem.

Heal. The surviving analog is not "links in CY3" but a holomorphic defect/specialization theorem:

```tex
(\Sigma_2,C)\text{ admissible}
  + \PhiFA_3(\cC)\in E_3\text{-HolFA}(X)
  -> \left(\int_{\Sigma_2}\PhiFA_3(\cC)\right)|_C
  \in E_1\text{-ChirAlg}(C).
```

Defects supported on `C` require their own chiral `E_{1\subset 3}` analogue, not the real framed-link theorem unchanged.

No-go condition. A real framed-link theorem cannot be cited as a holomorphic `(\Sigma_2,C)` specialization theorem without proving the comparison of framed real normal data with the holomorphic normal bundle, Dolbeault descent, and anomaly cancellation.

### Cycle 6: The `S^2` Operation and the `R`-Matrix

Attack. CFG's `E_3` binary operations have an `S^2` family and hence produce the `P_3` bracket; identify this with the CY3 quantum-group `R`-matrix.

Failure mode. In CFG the `S^2` class detects the degree `-2` shifted Poisson bracket on `C^*(\g)[[\hbar]]`, controlled by the invariant pairing `\lambda` on linear observables. It is not braid monodromy. In holomorphic CY3, `Conf_2(\mathbb C^3)` has link `S^5` and trivial `\pi_1`; the nontrivial data are Dolbeault/OPE residues, the Bochner--Martinelli kernel, the CY trace pairing, and later the Drinfeld-centre half-braiding.

Heal. The repaired statement is:

```tex
CFG's P_3 bracket is a topological normal form for the degree -2 bracket.
The CY3 bracket must be written in Hochschild/BV/Dolbeault-chiral CE variables,
with the CY trace and multidirectional OPE residues supplying the operation.
The R-matrix appears after the E_1 module-category centre, not from the S^2
class alone.
```

No-go condition. Do not copy CFG's pairing formula for the `P_3` bracket into CY3 unless the finite Lie algebra pairing has been replaced by the CY trace/BV pairing and the Dolbeault-chiral CE complex is still present.

### Cycle 7: RT Link Invariants versus CY3 Automorphic/BPS Traces

Attack. Since CFG's trace equals the Reshetikhin--Turaev invariant, the CY3 trace should directly equal a Borcherds denominator, a K3 x E BKM character, or a quantum-toroidal character.

Failure mode. CFG proves equality with RT invariants for ordinary CS and Drinfeld--Jimbo modules. The CY3 outputs require different data: orientation on critical CoHA, the open `\Theta_{\hCS\to\Hall}` comparison, BPS/DT state spaces, Borcherds products, Drinfeld doubles, and automorphic denominator formulas. None of these is supplied by CFG.

Heal. The safe theorem shape is conditional:

```tex
\text{CY3 chiral trace}
  -> \text{Hall/CoHA trace}
  -> \text{BPS/automorphic character}
```

only after the hCS-to-Hall comparison and the relevant automorphic/Borcherds input are independently constructed.

No-go condition. "CFG proves the `\Delta_5`/BKM/quantum-toroidal CY3 trace" is false. CFG proves the topological RT trace theorem; Vol III must prove the Hall and automorphic identifications separately.

## Repaired Statements

1. Proved CFG statement:

```tex
\Obs^q_{CS}(\mathbb R^3,\g,\lambda)
```

is a locally constant filtered `E_3` algebra deforming `C^*(\g)`. For a perfect module `V`, CFG's factorization-homology trace over framed links equals the RT invariant.

2. Correct CY3 Stage-1 statement:

```tex
\PhiFA_3(\cC)|_P
  \simeq
U^{\mathrm{fact},E_3}_{P}
\bigl(J^\infty_{\mathrm{hol}}\mathfrak L_{\hCS}\bigr)
```

on the loci where hCS realizes `\PhiFA_3`; this is a Dolbeault--chiral CE/enveloping factorization algebra over holomorphic polydiscs. `C^*(\g)` is obtained only by passing to the locally constant shadow.

3. Correct CY3 Stage-2 statement:

```tex
\Phi_3^{(\Sigma_2,C)}(\cC)
  =
\left(\int_{\Sigma_2}\PhiFA_3(\cC)\right)\bigm|_C
  \in E_1\text{-ChirAlg}(C).
```

The native `E_2` braiding at `d=3` lives on `\cZ(\Rep^{E_1}(A_\cC))`, not on `A_\cC`.

4. Correct trace statement:

```tex
\text{trace-class defect/module for } A_\cC
  -> \text{chiral/factorization-homology trace class of } A_\cC.
```

This is CFG-shaped, but it is not CFG's theorem until the CY3 object has been reduced to a locally constant `E_3` model and the module is proved perfect there.

## Claim-Status Recommendations

- CFG topological CS `E_3` trace theorem: proved in CFG for ordinary 3d CS.
- Use of CFG as a formal/topological model for Vol III Stage-1 traces: valid as analogy and test oracle.
- Identification of the CY3 avatar with ordinary `C^*(\g)`: false except after the locally constant shadow is explicitly applied.
- Holomorphic CY3 `E_3` trace theorem: conditional/expected; depends on Dolbeault-chiral CE construction, anomaly cancellation, admissible `(\Sigma_2,C)` specialization, and dualizable trace-class modules.
- CY3 trace equals Hall/Borcherds/quantum-toroidal character: conditional/conjectural unless `\Theta_{\hCS\to\Hall}` and the automorphic comparison are supplied.

## Files Changed

Only this report.

## Verification

No build or tests were run; this was a report-only adversarial pass. Verification consisted of reading CFG primary source Sections 1.3, 1.8, and 2, extracting the arXiv source for formulas, and checking the local `cy_to_chiral`, `cy3_chain_level_bridge`, `en_factorization`, `quantum_chiral_algebras`, `braided_factorization`, `hochschild_calculus`, `modular_trace`, and `phi_universal_trace_platonic` anchors by `rg`/line reads.
