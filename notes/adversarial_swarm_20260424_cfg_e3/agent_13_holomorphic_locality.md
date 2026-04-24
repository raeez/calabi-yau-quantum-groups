# Agent 13: Holomorphic Locality and Many-Variable Chiralization

Date: 2026-04-24.

Assigned surface: holomorphic factorization locality and many-variable chiralization for the CY3 stage-one object `\PhiFA_3`, compared only where valid with Costello--Francis--Gwilliam 2026, arXiv:2602.12412.

Files edited: only this report.

Manuscript files not edited.

## Executive Verdict

The claim

```tex
\PhiFA_3(\cC)|_P = C^\ast(\mathfrak g)
```

is false except after applying a locally constant/topological shadow functor that erases the CY3 holomorphic data. The correct local object on a holomorphic polydisc

```tex
P = D_1 \times D_2 \times D_3 \subset X,\qquad
(z_1,z_2,z_3)
```

is the Dolbeault local Lie algebra with holomorphic jets and its continuous/chiral Chevalley--Eilenberg observable algebra:

```tex
\mathfrak L_X(P)
  =
\Omega^{0,\bullet}_c
  \bigl(P,J^\infty_{\mathrm{hol},z_1,z_2,z_3}\mathfrak l_X\bigr)[1],
\qquad
d_{\mathfrak L}=\bar\partial+d_{\mathfrak l},
```

```tex
\Obs_X^{\mathrm{cl}}(P)
  =
C^\bullet_{\mathrm{Lie,cont}}\bigl(\mathfrak L_X(P),\mathbb C\bigr)
  =
\widehat{\mathrm{Sym}}\bigl(\mathfrak L_X(P)^\vee[-1]\bigr),
\qquad
d=d_{\mathrm{CE}}+\bar\partial^\vee+d_{\mathfrak l}^\vee.
```

On the loci where hCS realizes stage one, the factorization-envelope form is

```tex
\PhiFA_3(\cC)|_P
  \simeq
U^{\mathrm{fact},E_3}_{P}
  \bigl(J^\infty_{\mathrm{hol}}\mathfrak L_X\bigr),
\qquad
B_{E_3}\bigl(\PhiFA_3(\cC)|_P\bigr)
  \simeq
\mathrm{CE}^{\mathrm{ch},E_3}_*
  \bigl(J^\infty_{\mathrm{hol}}\mathfrak L_X\bigr).
```

The locally constant shadow is the further operation

```tex
\Omega^{0,\bullet}(P)\to H^\bullet_{\bar\partial}(P)\simeq\mathbb C,
\qquad
J^\infty_{\mathrm{hol}}\mathfrak L_X\to \mathfrak g_x,
\qquad
\Obs_X^{\mathrm{cl}}(P)\to C^\bullet(\mathfrak g_x).
```

Costello--Francis--Gwilliam 2026 proves the last topological pattern for ordinary 3d Chern--Simons. It does not prove the CY3 hCS-to-Hall comparison, it does not construct the critical CoHA, and it does not replace the Dolbeault/chiral CE object by ordinary `C^*(g)`.

## Source Anchors

Primary source, CFG:

- Costello--Francis--Gwilliam, *Chern--Simons factorization algebras and knot polynomials*, arXiv:2602.12412, submitted 2026-02-12, `https://arxiv.org/abs/2602.12412`.
- CFG Theorem 1.1: BV quantization of ordinary Chern--Simons gives a filtered `E_3`-algebra `A^\lambda`; Drinfeld--Jimbo representations give perfect modules; factorization-homology trace equals the Reshetikhin--Turaev invariant.
- CFG Introduction / Section 1.3: ordinary topological CS observables are locally constant on real 3-balls; by Lurie, locally constant factorization algebras on `\mathbb R^3` are `E_3`-algebras.
- CFG Introduction / Section 1.4 and Section 4.2, Lemma 4.3: the classical local model for ordinary CS is `C^\ast(\mathfrak g)`, obtained from the Poincare quasi-isomorphism for `\Omega^\ast(\mathbb R^3)\otimes\mathfrak g`.
- CFG Section 4.4, Proposition 4.6 and Lemma 4.7: quantum observables form a locally constant filtered `E_3` factorization algebra.
- CFG Section 3: filtered Koszul duality identifies `Perf_{C^\ast\mathfrak g}` with finite-dimensional `U\mathfrak g` modules in the ordinary semisimple setting.

Local manuscript anchors:

- `chapters/theory/cy3_chain_level_bridge.tex:45-109`: many-variable chiral CE model; ordinary `C^\bullet(\mathfrak g)` appears only after locally constant shadow.
- `chapters/theory/cy3_chain_level_bridge.tex:294-311`: explicit no-CFG-shortcut warning.
- `chapters/theory/cy3_chain_level_bridge.tex:317-360`: `\Theta_{\hCS\to\Hall}^{or}` remains the open hCS-to-Hall comparison with Dolbeault locality, Weiss descent, orientation, completion, and Thom--Sebastiani conditions.
- `chapters/theory/cy_to_chiral.tex:221-293`: two-stage factorization and three-step stage-one assembly.
- `chapters/theory/cy_to_chiral.tex:377-402`: CFG side-by-side table and non-rigidification warning.
- `chapters/theory/cy_to_chiral.tex:4856-4883`: at `d=3`, non-symmetric braiding is not the `E_3 -> E_2` restriction; it is recovered through the Drinfeld center after the `E_1` specialization.
- `chapters/theory/cy_to_chiral.tex:5031-5046`: bar--CE identification for chiral envelopes.
- `chapters/theory/cy_to_chiral.tex:5100-5105`: the chiral envelope does not raise the `E_n` level; at `d=3` the output is `E_1`.
- `chapters/theory/en_factorization.tex:2372-2399`: `\mathbb R^3` CS and `\mathbb C^3` hCS share the operadic label `E_3` but have different geometry and different braiding sources.
- `chapters/theory/en_factorization.tex:2642-2666`: topological `E_3` on `\mathbb R^3`, holomorphic-topological `E_1` on `\mathbb C\times\mathbb R`, and chain-level `E_3` framing on `S^3` are distinct sectors.

## True Local Object

For a holomorphic polydisc `P = D_1 x D_2 x D_3`, the CY3 local object is a factorization cosheaf in the Dolbeault/Weiss/Ran topology. The value on `P` is not a finite-dimensional CE algebra. It is a completed functional algebra on compactly supported Dolbeault fields and holomorphic jets.

Local Lie algebra:

```tex
\mathfrak L_X(P)
 =
\Omega_c^{0,\bullet}
 \bigl(P,J^\infty_{\mathrm{hol},z_1,z_2,z_3}\mathfrak l_X\bigr)[1],
```

with bracket

```tex
[\alpha,\beta]_{\mathfrak L}
 =
\alpha\wedge\beta\otimes[-,-]_{\mathfrak l_X}.
```

Classical observables:

```tex
\Obs_X^{\mathrm{cl}}(P)
 =
C^\bullet_{\mathrm{Lie,cont}}(\mathfrak L_X(P),\mathbb C)
 =
\prod_{n\ge 0}
\mathrm{Sym}^n_{\mathrm{cont}}
 \bigl(\mathfrak L_X(P)^\vee[-1]\bigr).
```

Chiral chains:

```tex
\mathrm{CE}^{\mathrm{ch},E_3}_*
\bigl(J^\infty_{\mathrm{hol}}\mathfrak L_X\bigr)(P)
 =
\bigoplus_{n\ge 0}
\Bigl(
J^\infty_{\mathrm{hol}}\mathfrak L_X(P)^{\boxtimes n}
\otimes \omega_{\mathrm{Conf}_n(P)}
\Bigr)_{\mathrm{coinv}}
```

with differential

```tex
d_{\mathrm{tot}}
 =
\bar\partial + d_{\mathfrak l} + d_{\mathrm{CE}}
 + d_{\mathrm{OPE},1}+d_{\mathrm{OPE},2}+d_{\mathrm{OPE},3}.
```

OPE kernel in three holomorphic variables:

```tex
a(z)b(w)
\sim
\sum_{\alpha\in\mathbb N^3}
\frac{(a_{(\alpha)}b)(w)}
{(z_1-w_1)^{\alpha_1+1}
 (z_2-w_2)^{\alpha_2+1}
 (z_3-w_3)^{\alpha_3+1}},
```

where

```tex
a_{(\alpha)}b
 =
\operatorname*{Res}_{z_1=w_1}
\operatorname*{Res}_{z_2=w_2}
\operatorname*{Res}_{z_3=w_3}
\Bigl[
(z_1-w_1)^{\alpha_1}
(z_2-w_2)^{\alpha_2}
(z_3-w_3)^{\alpha_3}
a(z)b(w)\,dz_1\,dz_2\,dz_3
\Bigr],
```

under a chosen iterated-residue convention. This convention must be fixed before a manuscript theorem states a many-variable OPE identity. Without it, the formula is a local normal form, not a complete global theorem.

Factorization product for disjoint polydiscs:

```tex
\mu_{P_1,\ldots,P_n;P}\colon
\widehat\otimes_{i=1}^n \Obs_X(P_i)
\longrightarrow
\Obs_X(P),
\qquad
P_i\cap P_j=\varnothing,\quad \bigsqcup_i P_i\subset P.
```

Descent:

```tex
\Obs_X(P)
\simeq
\operatorname*{hocolim}_{\{P_i\}\in \mathrm{Weiss}(P)}
\Obs_X(P_i),
```

with all tensor products completed and continuous. The descent theorem must be stated for the Dolbeault/Weiss/Ran site, not for the locally constant topology on real balls.

## Attack-Heal Cycle 1: The `C^*(g)` Shortcut

Claim attacked: CFG proves that the CY3 stage-one local object is ordinary `C^*(\mathfrak g)`.

Failure mode: fatal. CFG obtains `C^*(\mathfrak g)` because ordinary CS on a real 3-ball is locally constant and the de Rham complex contracts to constants. CY3 holomorphic locality does not contract the holomorphic jet algebra, the Dolbeault differential, or the partial-diagonal OPE kernels before a shadow functor is applied.

Healed proposition:

```tex
\textbf{Proposition.}
On a holomorphic polydisc P in a CY3 X, the stage-one local object is
\Obs_X(P)=C^\bullet_{\mathrm{Lie,cont}}(\mathfrak L_X(P),\mathbb C)
or equivalently its E_3 chiral envelope.
The ordinary algebra C^\bullet(\mathfrak g_x) is obtained only after
the locally constant shadow
\Omega^{0,\bullet}(P)\to\mathbb C,\quad
J^\infty_{\mathrm{hol}}\mathfrak L_X\to\mathfrak g_x.
```

Concrete formula:

```tex
\Obs_X(P)
 =
C^\bullet_{\mathrm{Lie,cont}}
\bigl(
\Omega_c^{0,\bullet}
(P,J^\infty_{\mathrm{hol}}\mathfrak l_X)[1],
\mathbb C
\bigr)
\not\simeq C^\bullet(\mathfrak g)
```

before the shadow functor.

Manuscript anchors to patch later: keep and strengthen `chapters/theory/cy3_chain_level_bridge.tex:98-109` and `:294-311`; add the phrase "locally constant/topological associated model" wherever `C^\bullet(\mathfrak g)` is imported from CFG.

Primary source anchors: CFG Lemma 4.3 and Lemma 4.7; local anchor `cy3_chain_level_bridge.tex:45-109`.

Claim-status recommendation: Definitional for the local Dolbeault CE object; Proved for CFG ordinary CS; false as a direct CY3 theorem.

## Attack-Heal Cycle 2: Locality Is Not Local Constancy

Claim attacked: Holomorphic factorization locality on `P` is the same as CFG local constancy on real balls.

Failure mode: fatal. Local constancy says extension along inclusions of balls is a quasi-isomorphism. Holomorphic locality says observables form a factorization cosheaf whose products are local over disjoint opens and whose singularities lie on holomorphic partial diagonals. The inclusion of a smaller polydisc into a larger polydisc need not be a quasi-isomorphism before Dolbeault contraction and jet truncation.

Healed proposition:

```tex
\textbf{Proposition.}
\PhiFA_3(\cC) is locally holomorphic and factorizing on the
Dolbeault/Weiss/Ran site. Its structure maps are continuous maps
over disjoint holomorphic polydiscs, and its descent is Weiss descent.
It becomes locally constant only after applying the topological shadow.
```

Concrete formula:

```tex
\mu_{P_1,\ldots,P_n;P}\colon
\widehat\otimes_i
C^\bullet_{\mathrm{Lie,cont}}(\mathfrak L_X(P_i))
\to
C^\bullet_{\mathrm{Lie,cont}}(\mathfrak L_X(P)),
```

with

```tex
\Obs_X(P)
\simeq
\operatorname*{hocolim}_{\mathrm{Weiss}(P)}\Obs_X(P_i).
```

Manuscript anchors to patch later: `chapters/theory/cy3_chain_level_bridge.tex:140-166` defines the Hall-valued factorization-cosheaf target; `:350` requires Dolbeault locality and Weiss descent; the report recommends adding the explicit local product map above near `def:cy3-many-variable-chiral-ce`.

Primary source anchors: CFG Section 1.3 and Lemma 4.7 only for local constancy of ordinary CS; Costello--Gwilliam and Costello--Li are the correct sources for holomorphic locality already cited at `cy_to_chiral.tex:221-293`.

Claim-status recommendation: Conditional/Proved-on-verified-loci for stage-one holomorphic factorization; false if stated as local constancy.

## Attack-Heal Cycle 3: One-Variable Chiral Algebra Is Not Enough

Claim attacked: The CY3 local chiral object can be modelled by a one-variable vertex algebra OPE after choosing a curve.

Failure mode: nonfatal if stated after `\SpCh_{\Sigma_2,C}`; fatal at stage one. Stage one lives over `\mathbb C^3` and has singularities along all partial diagonals in `P^n`. A one-variable OPE is the stage-two curve shadow. Replacing the three-variable residue calculus by a single `z-w` residue destroys two complex directions and hides the `E_3` input.

Healed proposition:

```tex
\textbf{Proposition.}
Before specialization, the CY3 local OPE is a multidirectional
partial-diagonal expansion indexed by \alpha\in\mathbb N^3.
After choosing (\Sigma_2,C), factorization homology along \Sigma_2
and restriction to C produces the E_1 chiral OPE on the reference curve.
```

Concrete formula:

```tex
a(z)b(w)
\sim
\sum_{\alpha\in\mathbb N^3}
\frac{(a_{(\alpha)}b)(w)}
{(z_1-w_1)^{\alpha_1+1}
 (z_2-w_2)^{\alpha_2+1}
 (z_3-w_3)^{\alpha_3+1}},
```

followed by stage two:

```tex
A_\cC^{(\Sigma_2,C)}
 =
\SpCh_{\Sigma_2,C}(\PhiFA_3(\cC))
 =
\left(\int_{\Sigma_2}\PhiFA_3(\cC)\right)\big|_C
\in E_1\text{-}\mathrm{ChirAlg}(C).
```

Manuscript anchors to patch later: `chapters/theory/cy3_chain_level_bridge.tex:84-98` has the three-variable OPE normal form; `chapters/theory/cy_to_chiral.tex:230-238` and `:539-543` define the specialization. Add an explicit sentence that single-variable OPEs are stage-two outputs, not stage-one data.

Primary source anchors: Beilinson--Drinfeld for curve chiral algebras; Costello--Li for holomorphic factorization in several complex variables; CFG does not supply this many-variable OPE.

Claim-status recommendation: Definitional at the level of local normal form; Conditional for global analytic sewing and iterated-residue convention.

## Attack-Heal Cycle 4: CFG Quantization Does Not Prove hCS-to-Hall

Claim attacked: CFG's filtered `E_3` quantization of ordinary CS proves the CY3 hCS-to-Hall comparison and hence the CoHA/Yangian/BKM output.

Failure mode: fatal. CFG quantizes ordinary topological CS for a semisimple finite-dimensional gauge Lie algebra with invariant pairing. The CY3 bridge requires a comparison

```tex
\Theta_{\hCS\to\Hall}^{or}\colon
\Obs_{\hCS}^{q}(-,\mathfrak g)
\to
\CoHA_{\mathrm{crit}}^{or}(-)
```

in an oriented Hall-valued factorization-cosheaf category, with compact-support convention, equivariant parameters, orientation data, Thom--Sebastiani compatibility, completions, and Dolbeault/Weiss descent.

Healed proposition:

```tex
\textbf{Proposition.}
CFG supplies a theorem-grade associated topological model:
C^\ast(\mathfrak g)\leadsto C^\ast_\hbar(\mathfrak g).
The CY3 hCS-to-Hall comparison is a separate open datum
\Theta_{\hCS\to\Hall}^{or}. It cannot be inferred from CFG.
```

Concrete formula:

```tex
\CoHA_{\mathrm{crit}}^{or}(U)
 =
\bigoplus_{\mathbf d}
H^{\mathrm{BM}}_{G_{\mathbf d}}
\left(
\mathrm{Crit}(\mathrm{Tr}W_{\mathbf d}),
\phi_{\mathrm{Tr}W_{\mathbf d}}\otimes\mathscr L_{o_U}
\right)
[s(U,\mathbf d)](t(U,\mathbf d)).
```

Manuscript anchors to patch later: `chapters/theory/cy3_chain_level_bridge.tex:317-360` already states the open problem; preserve it. If manuscript patching is later authorized, add CFG Theorem 1.1 as an analogy only, never as an input to `\Theta_{\hCS\to\Hall}^{or}`.

Primary source anchors: CFG Theorem 1.1, Proposition 4.6, Lemma 4.7; local open problem `cy3_chain_level_bridge.tex:317-360`.

Claim-status recommendation: CFG ordinary CS: ProvedElsewhere. CY3 `\Theta_{\hCS\to\Hall}^{or}`: Open/Conditional. Direct transfer: false.

## Attack-Heal Cycle 5: `E_3` Does Not Give Native Non-Symmetric Braiding on `\Phi_3`

Claim attacked: Since CFG has an `E_3` algebra whose module category is `E_2`-monoidal, the CY3 output `\Phi_3(\cC)` itself is natively `E_2`-braided with the quantum-group `R`-matrix.

Failure mode: fatal. At `d=3`, Vol III's stage-two output is `E_1`-chiral. The topological `E_3 -> E_2` restriction has symmetric braiding because `\pi_1(\mathrm{Conf}_2(\mathbb R^3))=0`. The non-symmetric `R`-matrix appears through the Drinfeld center of the `E_1` representation category on constructed loci.

Healed proposition:

```tex
\textbf{Proposition.}
For a framed CY3 input on the verified object-level locus,
A_\cC^{(\Sigma_2,C)}
=\SpCh_{\Sigma_2,C}(\PhiFA_3(\cC))
\in E_1\text{-}\mathrm{ChirAlg}(C).
The braided category is
\mathcal Z(\mathrm{Rep}^{E_1}(A_\cC^{(\Sigma_2,C)})),
not a native E_2 structure on A_\cC.
```

Concrete formula:

```tex
R_{V_u,V_v}
 =
\sigma_{V_u}(V_v)
\in
\mathrm{End}(V_u\otimes V_v)
```

where `\sigma` is the half-braiding in the Drinfeld center.

Manuscript anchors to patch later: `chapters/theory/cy_to_chiral.tex:4856-4883` is correct and must be preserved; `:5100-5105` should be cited whenever a later passage suggests that a chiral envelope raises `E_1` to `E_2`.

Primary source anchors: CFG Section 1.5 for the ordinary CS module-category pattern; Vol III `cy_to_chiral.tex:4856-4883` for the CY3 mechanism.

Claim-status recommendation: Definitional/ProvedHere on constructed loci; false as a native `E_2` claim on `A_\cC`.

## Attack-Heal Cycle 6: Chartwise Quasi-Isomorphisms Do Not Give Global Descent

Claim attacked: It is enough to identify each local chart with a known algebra (`Y^+`, `C^*(g)`, or a quiver CoHA); global CY3 stage one follows by listing the chartwise quasi-isomorphisms.

Failure mode: nonfatal as evidence, fatal as theorem. Factorization descent needs compatibility under restriction to overlaps, orientation-torsor transport, completed tensor products, Hall correspondences, compact support, and Thom--Sebastiani. A pointwise or chartwise equivalence does not define a morphism of factorization cosheaves.

Healed proposition:

```tex
\textbf{Proposition.}
A CY3 chart comparison is theorem-grade only when the maps
\Theta_U\colon\Obs_X(U)\to\CoHA_{\mathrm{crit}}^{or}(U)
assemble to a continuous natural transformation of factorization
cosheaves preserving orientation, completion, Hall product,
and Thom--Sebastiani coherences.
```

Concrete descent condition:

```tex
\Theta_U\circ \mu^{\hCS}_{U_1,\ldots,U_n;U}
 =
\mu^{\Hall}_{U_1,\ldots,U_n;U}
\circ
(\widehat\otimes_i\Theta_{U_i})
```

for disjoint opens `U_i \subset U`, with analogous cocycle identities on overlaps and triple overlaps.

Manuscript anchors to patch later: `chapters/theory/cy3_chain_level_bridge.tex:140-166` and `:248-267` already make the category and gluing condition explicit. Later manuscript patches should cite these lines before claiming any global CY3 Hall output.

Primary source anchors: local Hall/CoHA source is Kontsevich--Soibelman and Schiffmann--Vasserot on the toric chart; CFG supplies no Hall-valued descent.

Claim-status recommendation: Proved on explicit toric chart core; Conditional/Open for multi-chart compact CY3 descent.

## Attack-Heal Cycle 7: The Topological Shadow Loses Data

Claim attacked: Passing to the locally constant shadow preserves the content needed for CY3 OPE, `\Omega`-background parameters, and Hall/BKM outputs.

Failure mode: fatal. The shadow keeps the coarse `E_3` operadic pattern and constant ghost CE algebra. It forgets holomorphic jets, the Dolbeault differential, residues along partial diagonals, individual `\epsilon_i` or `h_i` parameters, orientation data, and charge/stability completions. It can test a pattern; it cannot prove the CY3 object.

Healed proposition:

```tex
\textbf{Proposition.}
The locally constant shadow functor
\mathrm{LC}\colon \PhiFA_3(\cC)|_P \to C^\bullet(\mathfrak g_x)
is a loss map. Its image retains the ordinary topological E_3 and CE
grammar. It does not retain the holomorphic factorization algebra.
```

Concrete loss map:

```tex
\mathrm{LC}:
C^\bullet_{\mathrm{Lie,cont}}
\bigl(
\Omega_c^{0,\bullet}(P,J^\infty_{\mathrm{hol}}\mathfrak l_X)[1]
\bigr)
\longrightarrow
C^\bullet(\mathfrak g_x).
```

Data lost:

```tex
(z_1,z_2,z_3),\quad
J^\infty_{\mathrm{hol}},\quad
\bar\partial,\quad
d_{\mathrm{OPE},1},d_{\mathrm{OPE},2},d_{\mathrm{OPE},3},\quad
(\epsilon_1,\epsilon_2,\epsilon_3),\quad
\text{orientation/completion/Hall charge data}.
```

Manuscript anchors to patch later: `chapters/theory/en_factorization.tex:2372-2399` and `:2642-2666` should be cited near any CFG comparison. They already distinguish `\mathbb R^3` topological CS from `\mathbb C^3` hCS and from `S^3` chain-level framing.

Primary source anchors: CFG Lemma 4.3 and Lemma 4.7; Vol III `en_factorization.tex:2372-2399`, `:2642-2666`.

Claim-status recommendation: Definitional for the shadow map; false if used as an equivalence before explicitly applying the shadow.

## Patch Anchors for Later Manuscript Work

No manuscript patch is authorized in this agent lane. If the integration owner patches later, the exact targets are:

1. `chapters/theory/cy3_chain_level_bridge.tex:45-109`: add `J^\infty_{\mathrm{hol},z_1,z_2,z_3}\mathfrak l_X` directly to the first displayed local Lie algebra, not only in the later equivalent sentence. Clarify compact-support versus continuous-dual convention.
2. `chapters/theory/cy3_chain_level_bridge.tex:84-98`: fix an iterated-residue or multidimensional residue convention. Without this, the displayed many-variable OPE is a normal form, not a theorem-level operation.
3. `chapters/theory/cy3_chain_level_bridge.tex:98-109`: preserve the statement that `C^\bullet(\mathfrak g)` appears only after locally constant shadow; strengthen with "topological associated model".
4. `chapters/theory/cy3_chain_level_bridge.tex:294-311`: keep the no-CFG-shortcut warning. Add CFG theorem numbers: Theorem 1.1, Lemma 4.3, Proposition 4.6, Lemma 4.7.
5. `chapters/theory/cy_to_chiral.tex:377-402`: weaken any phrase that suggests CFG identifies the same object. The two constructions share the operadic input; the targets differ.
6. `chapters/theory/cy_to_chiral.tex:4856-4883`: keep the Drinfeld-center braiding mechanism as the only non-symmetric `d=3` braiding claim.
7. `chapters/theory/en_factorization.tex:2372-2399`: cite this table whenever importing CFG. The table is the local firewall between real topological CS and complex hCS.

## Claim-Status Recommendations

- Local polydisc Dolbeault Lie algebra: Definitional.
- Continuous CE cochains on the Dolbeault local Lie algebra: Definitional, with functional-analysis completion convention required.
- Stage-one hCS realization of `\PhiFA_3` on verified loci: Conditional/ProvedHere only under the hypotheses already named in Theorem `thm:cy-to-chiral-d3`.
- Many-variable OPE expansion: Definitional normal form; Conditional as a theorem until the residue convention and sewing/analytic completion are fixed.
- Weiss/factorization descent: Conditional on the Costello--Gwilliam--Li holomorphic factorization framework and the explicit cosheaf category.
- CFG ordinary topological CS filtered `E_3` observables: ProvedElsewhere.
- `C^\bullet(\mathfrak g)` as CY3 stage-one object: reject; true only as locally constant/topological associated model.
- hCS-to-Hall map `\Theta_{\hCS\to\Hall}^{or}`: Open.
- Non-symmetric CY3 braiding: Proved on constructed loci through `\mathcal Z(\mathrm{Rep}^{E_1}(A))`; not native on `A`.

## Computations and Tests Run

Targeted source scans:

```bash
rg -n -e "many-variable chiral CE" -e "Dolbeault" -e "holomorphic jets" \
  -e "partial diagonals" -e "locally constant shadow" \
  chapters/theory/cy3_chain_level_bridge.tex

rg -n -e "Two-stage" -e "Stage" -e "d = 3" -e "Drinfeld center" \
  -e "PhiFA_3" chapters/theory/cy_to_chiral.tex

rg -n -F "CFG" chapters notes
rg -n -F "C^*(g" notes/adversarial_swarm_20260424_cfg_e3 chapters notes
```

CFG source/text fetched to `/tmp` only:

```bash
curl -L https://arxiv.org/e-print/2602.12412 -o /tmp/cfg2602.12412.src
curl -L https://arxiv.org/pdf/2602.12412 -o /tmp/cfg2602.12412.pdf
pdftotext /tmp/cfg2602.12412.pdf /tmp/cfg2602.12412.txt
```

No-cache targeted pytest:

```bash
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider \
  compute/tests/test_holomorphic_cs_chiral_engine.py \
  compute/tests/test_cfg25_e1_chiral_lift.py \
  compute/tests/test_e3_config_space_chiral.py
```

Result:

```text
225 passed in 3.14s
```

## Files Changed

Only:

```text
notes/adversarial_swarm_20260424_cfg_e3/agent_13_holomorphic_locality.md
```

## Remaining Open Obligations

1. Fix a theorem-grade multidimensional residue convention for the three-variable OPE: iterated residue order, coordinate-change invariance, and compatibility with partial diagonals.
2. State the compact-support/continuous-dual convention in the local Lie algebra and CE cochains so that factorization products are continuous maps in the chosen bornological or nuclear Frechet category.
3. Prove or scope Weiss descent for the Dolbeault/Weiss/Ran site in the exact category used by `\mathsf{FactCosh}_{\Hall}^{or,\wedge}(X)`.
4. Construct `\Theta_{\hCS\to\Hall}^{or}` with orientation data, Thom--Sebastiani coherence, equivariant parameters, completion, and anomaly cancellation.
5. Prove compatibility between the three-variable chiral CE bar object and the Hall positive-half model on overlaps, not only on isolated `\mathbb C^3` charts.
6. Keep CFG strictly in the associated-model lane: ordinary 3d topological CS, locally constant `E_3`, filtered deformation of `C^\ast(\mathfrak g)`, perfect modules, RT trace. It is not the CY3 hCS-to-Hall theorem.
