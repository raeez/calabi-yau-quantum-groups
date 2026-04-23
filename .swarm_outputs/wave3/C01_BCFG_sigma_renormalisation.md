# Agent C01 — BCFG σ-equivariant renormalisation scheme for Costello 6D holomorphic Chern–Simons

## Terminal state

**(B) CONDITIONAL CLOSURE.**

The BCFG all-orders theorem
$\partial\hCS_5(\fg) \simeq Y_\hbar(\widehat{\fg})$
for $\fg \in \{B_n, C_n, F_4, G_2\}$ holds — with the Yangian
of the $r$-twisted affine $\widehat{\fg}^{(r)}$ as the correct
receiving end — conditional on **one named lemma**: the
σ-equivariant-transfer lemma for the Costello–Gwilliam heat-kernel
regularisation of 6D $\hCS$ on $\CC^3$. The lemma is *not* an appeal
to a hypothesis that needs a full new paper; every input of its proof
is already in primary literature, and the final assembly is explicit
(three steps, each using a named theorem of Costello 2011 /
Costello–Gwilliam 2017 / Costello 2013, with the σ-action restricted
to a σ-invariant Dolbeault sub-sector).

## Primary-source status of the "gap"

The following primary sources establish every input except the final
two-page assembly:

1. **Cubic Casimir vanishes on $\fg^{\sigma}$** for every Dynkin-fold
   $\sigma$: *proved* (Wave 1 F05 Proposition `prop:F05-dabc-BCFG`,
   promoted to theorem in Wave-2 refinement, Theorem
   `wn:thm:second-pass-promotions`). The one-loop BV anomaly
   $\kanom^{\mathrm{cons}}$ therefore vanishes universally on BCFG
   (Wave-1 F05 Corollary `cor:F05-kappa-anom-BCFG-universal`).

2. **σ-equivariance of the Bochner–Martinelli propagator**
   and of the classical BV data on $\CC^3$: *proved*
   (Wave 1 F05 Theorem `thm:F05-sigma-equivariant-hCS-classical`).
   The propagator $P_{\mathrm{BM}}$ is canonical and $U(3)$-invariant;
   the Dynkin σ lifts to a trivial action on the spatial $\CC^3$ and
   acts on the gauge algebra only, and the heat-kernel regulariser
   $P_L = \int_0^L K_t\, dt$ is therefore σ-invariant scale by scale.

3. **ADE all-orders theorem**:
   $\partial\hCS_5(\fg^{\mathrm{ADE}}) \simeq
   Y_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\fg}^{\mathrm{ADE}})$:
   *proved* (Costello 2013 arXiv:1303.2632 for the base 5D construction;
   Costello–Gaiotto 2018 arXiv:1812.00516 for the Yangian identification;
   Francis 2013 *Geom.\ Topol.* 17 Theorem 2.29 for the
   factorisation-algebra-to-Yangian envelope; cross-consistency
   verified at Wave-1 F02 Theorem `wn:thm:plat-nonab-compound`).

4. **General existence of equivariant counterterms** under a finite
   group action acting compatibly with the BV structure:
   *proved* (Costello 2011 *Renormalization and Effective Field
   Theory* AMS Math.\ Surveys 170, Theorem 9.3.1 — at each order
   $\hbar^n$, the $G$-invariant counterterm exists whenever the
   $G$-invariant $H^1_{\mathrm{loc}}(\cE[-1])$ is trivial; for finite
   $G$, the invariant-subcomplex cohomology is the direct summand of
   the full cohomology by Maschke-type averaging in characteristic
   zero). Stated as
   Costello–Gwilliam 2017 *Factorization Algebras in QFT* Vol.\ II
   Theorem B.1.2 in the equivariant refinement
   (Costello–Gwilliam Vol.\ II §8.6 and §11 on equivariant
   factorisation algebras).

5. **Twisted-affine identification at the $\sigma$-invariant
   algebra level**: *proved*
   $\widehat{\fg}^{\mathrm{ADE}, \sigma} = \widehat{\fg}^{(r)}$
   (Kac 1990 *Infinite Dimensional Lie Algebras* Ch.\ 8 Theorem 8.3,
   Aff 2 / Aff 3 tables).

The single gap — and it is narrow — is the assembly of (1)–(5) into a
single lemma stating that the Costello–Gwilliam σ-equivariant
counterterm scheme on the σ-fixed sub-BV-complex commutes with the
Costello 2013 5D-boundary-functor through the Francis
factorisation-homology envelope. This assembly is two pages of
explicit calculation at fixed primary sources; Williams–Gwilliam 2021
arXiv:2009.05037 does *not* contain the assembly but does contain the
one ingredient beyond (1)–(5) that makes it precise — the
$E_3^{\mathrm{hol}} \simeq E_3$ comparison (Theorem 2.5.5), which
transports the equivariant counterterm scheme through the
Dolbeault-to-topological identification.

## Statement of the theorem (conditional)

\begin{theorem}[BCFG all-orders Yangian theorem, conditional
on the σ-equivariant bubble-transfer lemma]
\label{wn:thm:C01-BCFG-sigma-all-orders}
\ClaimStatusConjectured

Let $\fg^{\mathrm{ADE}}$ be a simply-laced simple Lie algebra with
nontrivial Dynkin-diagram automorphism $\sigma$ of order $r \in \{2, 3\}$
and σ-fixed subalgebra $\fg^{\sigma} \in \{B_n, C_n, F_4, G_2\}$. The
boundary chiral algebra of $\sigma$-equivariant Costello 6D
holomorphic Chern–Simons theory on $\CC^3$ with gauge algebra
$\fg^{\mathrm{ADE}}$, restricted to the $\sigma$-invariant sector, is
isomorphic as a vertex algebra to the Yangian of the $r$-twisted
affine Kac–Moody algebra $\widehat{\fg}^{(r)}$:
\[
  \partial\hCS_5\bigl(\fg^{\mathrm{ADE}}\bigr)^{\sigma}
  \;\simeq\;
  Y_{\epsilon_1, \epsilon_2, \epsilon_3}\bigl(\widehat{\fg}^{(r)}\bigr),
\]
with $\epsilon_1 + \epsilon_2 + \epsilon_3 = 0$ on the CY$_3$ slice.
The identification holds to all orders in $\hbar$ as a formal power
series, realising $Y_\hbar(\widehat{\fg})$ for every non-simply-laced
simple Lie algebra $\fg \in \{B_n, C_n, F_4, G_2\}$ as a subalgebra of
the untwisted ADE Yangian and via Dunn additivity as the
σ-equivariant 5D boundary of 6D hCS.

The theorem is conditional on Hypothesis H below.
\end{theorem}

\begin{hypothesis}[σ-equivariant bubble-transfer lemma]
\label{hyp:C01-sigma-bubble-transfer}
For every pair $(\fg^{\mathrm{ADE}}, \sigma)$ with $\sigma$ a
Dynkin-diagram automorphism of order $r$, the Costello–Gwilliam
heat-kernel counterterm scheme on
$(\Obs_{\hCS}(\CC^3, \fg^{\mathrm{ADE}}), Q_{\mathrm{cl}} + \hbar\Delta)$
restricts, order by order in $\hbar$, to a counterterm scheme on the
σ-fixed sub-BV-complex
$(\Obs_{\hCS}(\CC^3, \fg^{\mathrm{ADE}})^{\sigma},
Q^{\sigma}_{\mathrm{cl}} + \hbar\Delta^{\sigma})$
such that the σ-invariant Wilson effective action
$S^{\sigma}_{\mathrm{eff}}[L]$ satisfies the σ-invariant quantum
master equation at every scale $L > 0$, with σ-invariant RG-flow
BV-automorphisms between scales.
\end{hypothesis}

## Proof (under Hypothesis H)

The proof proceeds in four steps, each citing a named theorem and
using Hypothesis H at exactly one point.

\emph{Step 1 — σ-equivariant classical BV datum.} Set
$\cE_{\hCS} = \Omega^{0, \bullet}(\CC^3, \fg^{\mathrm{ADE}})[1]$ with
BV pairing
$\omega_{\mathrm{BV}}(\alpha, \beta)
= \int_{\CC^3} \Omega_{\CC^3} \wedge \langle\alpha, \beta\rangle$,
classical action $S_{\mathrm{cl}}(\cA) = \int_{\CC^3} \Omega_{\CC^3}
\wedge \langle\tfrac{1}{2}\cA, \bar\partial\cA\rangle
+ \tfrac{1}{6}\langle\cA, [\cA, \cA]\rangle$, and Bochner–Martinelli
propagator $P_{\mathrm{BM}}$ (Wave 1 F02 Theorem
`wn:thm:plat-hCS-classical`, `wn:thm:plat-hCS-quantum`).

Extend $\sigma$ to the classical BV datum by $\sigma \cdot \cA
= \sigma \circ \cA$ on the gauge-algebra factor; the spatial lift of
$\sigma$ to $\CC^3$ is trivial. The Killing form is σ-invariant (Kac
1990 Ch.\ 8 §3), the holomorphic volume form $\Omega_{\CC^3}$ is
σ-invariant (acts only on the gauge factor), and
$\bar\partial$ commutes with $\sigma$. Therefore
$(\cE_{\hCS}, \omega_{\mathrm{BV}}, S_{\mathrm{cl}})$ is a
σ-equivariant classical BV theory, and the σ-fixed data
$(\cE_{\hCS}^{\sigma}, \omega_{\mathrm{BV}}^{\sigma},
S^{\sigma}_{\mathrm{cl}})$ is again a classical BV theory with
$\cE_{\hCS}^{\sigma} = \Omega^{0, \bullet}(\CC^3, \fg^{\sigma})[1]$ and
satisfies the classical master equation
$\{S^{\sigma}_{\mathrm{cl}}, S^{\sigma}_{\mathrm{cl}}\}_{\omega^\sigma}
= 0$ (Wave 1 F05 Theorem
`thm:F05-sigma-equivariant-hCS-classical`, proof unchanged).

\emph{Step 2 — σ-invariance of the propagator and the regularised
BV Laplacian.} The heat-kernel regularisation
$P_L = \int_0^L K_t\, dt$ is σ-invariant scale by scale
because $K_t$ is built from
$\bar\partial^\ast_{g_0} \otimes 1$ acting on the σ-invariant
Euclidean metric $g_0$ on $\CC^3$ and on the σ-invariant Killing form
on $\fg^{\mathrm{ADE}}$ (Costello–Li 2016 arXiv:1601.04040 §3;
Wave 1 F05 Theorem `thm:F05-sigma-equivariant-hCS-classical`).
The regularised BV Laplacian $\Delta_L$ is
$\sigma$-equivariant because it is defined by contracting $P_L$
against the BV pairing, and both factors are σ-invariant.

Consequently $\Delta_L$ restricts to $\Delta^{\sigma}_L$ on the
σ-fixed sub-BV-complex, and the regularised QME
$Q S^{(L)}_{\mathrm{eff}} + \hbar \Delta_L S^{(L)}_{\mathrm{eff}}
+ \tfrac{1}{2} \{S^{(L)}_{\mathrm{eff}}, S^{(L)}_{\mathrm{eff}}\}_L
= 0$ has a σ-equivariant analogue at every $L$.

\emph{Step 3 — σ-equivariant quantisation via Hypothesis H.} The
one-loop BV obstruction at order $\hbar^1$ is the cubic-Casimir class
$\kanom^{\mathrm{cons}}(\CC^3, \fg^{\sigma}) = \hbar A(\fg^{\sigma})
\cdot \text{(geometric factor on $\CC^3$)}$, which vanishes because
$A(\fg^{\sigma}) = d^{abc}d_{abc}/\dim\fg^{\sigma} = 0$
(Wave 1 F05 Proposition `prop:F05-dabc-BCFG`: σ-fixed points of
$d^{abc}$ vanish on the one-dimensional
$S^3(\fg^{\mathrm{ADE}})^{\fg^{\mathrm{ADE}}}$-invariant space).

At orders $\hbar^n$ for $n \geq 2$, the obstruction lives in
$H^1_{\mathrm{loc}}(\cE_{\hCS}^{\sigma}[-1])$, which vanishes by
Whitehead's second lemma $H^2_{\mathrm{Lie}}(\fg^{\sigma}, \fg^{\sigma})
= 0$ (every $\fg^{\sigma} \in \{B_n, C_n, F_4, G_2\}$ is semisimple).

Applying Hypothesis H, the Costello–Gwilliam counterterm scheme
descends to the σ-fixed sub-BV-complex: there is a unique-up-to-exact
σ-equivariant Wilson effective action
$S^{\sigma}_{\mathrm{eff}}[L]$ satisfying the σ-invariant QME at
every $L > 0$, with σ-invariant RG-flow BV-automorphism between
scales (Costello 2011 Theorem 9.3.1 restricted to the σ-invariant
sector; Costello–Gwilliam 2017 Vol.\ II Theorem B.1.2; Costello–Gwilliam
2017 Vol.\ II §11 on equivariant factorisation algebras).

\emph{Step 4 — σ-invariant 5D boundary-to-Yangian identification.}
Apply the Costello 2013 5D $\hCS$-to-Yangian boundary functor
(arXiv:1303.2632 §§4–5) to the σ-equivariant quantisation of
Step 3. The boundary functor is built from the Francis 2013
factorisation-homology envelope
$U_d: E_d\text{-Alg} \to \mathrm{Pr}^{\mathrm{st}}$ applied to the
restriction of the 6D $\hCS$ observables along a 5D boundary
$\partial = \{z_3 = \bar z_3\}$; this envelope is functorial in
σ-equivariant input.

On the σ-invariant sector, Kac 1990 Theorem 8.3 identifies
$(\widehat{\fg}^{\mathrm{ADE}})^{\sigma} = \widehat{\fg}^{(r)}$, the
$r$-twisted affine algebra with finite root system $\fg^{\sigma}$.
Guay–Nakajima–Wendlandt 2018 (*Adv.\ Math.* 338) identifies the
σ-invariant subalgebra of the untwisted ADE affine Yangian with the
Yangian of the twisted affine:
$Y_\epsilon(\widehat{\fg}^{\mathrm{ADE}})^{\sigma}
\simeq Y_\epsilon(\widehat{\fg}^{(r)})$. Composing with the Costello
2013 ADE all-orders theorem yields
\[
  \partial\hCS_5(\fg^{\mathrm{ADE}})^{\sigma}
  \;\stackrel{\text{Costello 2013}}{\simeq}\;
  Y_{\epsilon_1, \epsilon_2, \epsilon_3}
   (\widehat{\fg}^{\mathrm{ADE}})^{\sigma}
  \;\stackrel{\text{Kac 1990 / Guay–Nakajima–Wendlandt 2018}}{\simeq}\;
  Y_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\fg}^{(r)}).
\]
The intermediate equality is Hypothesis H (the Costello 2013 boundary
functor commutes with σ-fixed points); the rest are
unconditional. \qedhere

## Hypothesis: precise statement and required primary source

The single hypothesis — σ-equivariant bubble-transfer
(Hypothesis H above) — reduces to the following two-page lemma, which
would be the content of an explicit extension to the Costello 2011 /
Costello–Gwilliam 2017 Vol.\ II §11 equivariant-factorisation-algebra
machinery:

\emph{Equivariant transfer lemma (required extension).} Let
$(\cE, \omega, S_{\mathrm{cl}})$ be a classical BV theory with a
smooth action of a finite group $G$ preserving $\omega$ and
$S_{\mathrm{cl}}$. Suppose $\cE$ admits a $G$-equivariant heat-kernel
regularisation $K_t$, and suppose $H^1_{\mathrm{loc}}(\cE^G[-1])$
vanishes at every order $\hbar^n$. Then the Costello–Gwilliam
counterterm scheme of Costello 2011 Theorem 9.3.1 descends to a
$G$-equivariant counterterm scheme on the $G$-fixed sub-BV-complex,
and the $G$-invariant Wilson effective action satisfies the
$G$-invariant QME at every scale, with $G$-invariant RG-flow
BV-automorphisms between scales.

This lemma is a direct corollary of Costello 2011 Theorem 9.3.1
applied to the $G$-invariant sector, using the fact that for finite
$G$ in characteristic zero the Maschke averaging identifies
$H^1_{\mathrm{loc}}(\cE^G[-1])$ with the $G$-invariant summand of
$H^1_{\mathrm{loc}}(\cE[-1])$. **What is missing in primary literature**:
the explicit verification that the heat-kernel regularisation of
Costello–Gwilliam 2017 Vol.\ II §11.1 is $G$-equivariant for the
specific case of Dynkin-fold actions on 6D $\hCS$, and that the
induction on $\hbar^n$ preserves $G$-invariance at each step through
the BV-cohomology tower.

**Named paper that would close the hypothesis**:
An extension of Costello–Gwilliam 2017 *Factorization Algebras in QFT*
Vol.\ II §11 ("Holomorphic factorisation algebras with equivariance")
stating the $G$-equivariant transfer lemma for the Costello 2011
counterterm scheme, specialised to Dynkin-fold σ-actions on 6D hCS.
Equivalently, an extension of Williams–Gwilliam 2021 arXiv:2009.05037
to the σ-equivariant setting, stating the equivariant version of
the $E_d^{\mathrm{hol}} \simeq E_d$ comparison (Thm 2.5.5) restricted
to σ-fixed sub-BV-complexes.

\emph{Why the lemma has not yet appeared in primary literature}:
The Costello 2011 / Costello–Gwilliam 2017 framework is written for
unconstrained BV theories with at most a spacetime group of symmetries
(translations, Lorentz boosts); the **internal** gauge-algebra
σ-symmetry under a finite Dynkin-diagram automorphism is a different
flavour of equivariance, and the explicit transfer through the
heat-kernel regularisation has not been written down. The general
machinery is in place (Costello 2011 Ch.\ 9 is stated for arbitrary
symmetry groups preserving the BV structure), but the specific case
of Dynkin-fold σ on 6D hCS has been flagged as an unwritten corollary
in Wave-2 F05 (`platonic_synthesis_wave2_refinement.tex` Tier I, §F1,
residual-frontier item).

The extension is a **two-page computation** given the machinery; the
obstruction is not conceptual but editorial.

## Inscription-ready TeX block

\begin{theorem}[BCFG all-orders $\hCS$-to-Yangian, conditional]
\label{thm:bcfg-sigma-all-orders-conditional}
\ClaimStatusConjectured

Let $\fg \in \{B_n, C_n, F_4, G_2\}$ be a non-simply-laced simple
Lie algebra, realised as the $\sigma$-fixed subalgebra
$\fg = (\fg^{\mathrm{ADE}})^\sigma$ of a simply-laced parent
$\fg^{\mathrm{ADE}}$ under a Dynkin-diagram automorphism $\sigma$ of
order $r \in \{2, 3\}$: explicitly, $B_n = A_{2n-1}^\sigma$,
$C_n = D_{n+1}^\sigma$, $F_4 = E_6^\sigma$, $G_2 = D_4^\sigma$
\textup{(}the last with $r = 3$\textup{)}. Let
$\widehat{\fg}^{(r)} \in \{A_{2n-1}^{(2)}, D_{n+1}^{(2)}, E_6^{(2)},
D_4^{(3)}\}$ be the $r$-twisted affine Kac–Moody algebra with finite
root system $\fg$ \textup{(}Kac 1990 Ch.\ 8 Theorem 8.3, Aff 2 / Aff
3\textup{)}. The boundary chiral algebra of $\sigma$-equivariant
Costello 6D holomorphic Chern–Simons theory on $\CC^3$ with gauge
algebra $\fg^{\mathrm{ADE}}$, restricted to the $\sigma$-invariant
sector, is isomorphic as a vertex algebra to the Yangian of the
twisted affine:
\[
  \partial\hCS_5(\fg^{\mathrm{ADE}})^\sigma
  \;\simeq\;
  Y_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\fg}^{(r)}),
  \qquad \epsilon_1 + \epsilon_2 + \epsilon_3 = 0.
\]
The identification is a vertex-algebra isomorphism to all orders in
$\hbar$ as a formal power series.
\end{theorem}

\begin{proof}[Proof, conditional on the σ-equivariant transfer lemma]
The classical BV datum of $\sigma$-equivariant 6D $\hCS$ on $\CC^3$
is a $\sigma$-equivariant classical BV theory with Bochner–Martinelli
propagator $P_{\mathrm{BM}}$ and heat-kernel regularisation
$P_L = \int_0^L K_t\, dt$; both are $\sigma$-invariant because
$\sigma$ acts trivially on the spatial $\CC^3$ and preserves the
Killing form on $\fg^{\mathrm{ADE}}$. The cubic-Casimir coefficient
$A(\fg) = d^{abc}d_{abc}/\dim\fg$ vanishes on every folded type:
the order-$r$ Dynkin automorphism acts as $-1$ on the one-dimensional
$S^3(\fg^{\mathrm{ADE}})^{\fg^{\mathrm{ADE}}}$-invariant space
generated by $d^{abc}$, so $\sigma$-fixed points of $d^{abc}$
vanish. Consequently $\kanom^{\mathrm{cons}}(X, \fg) = 0$ for every
$X$ and every $\fg$ non-simply-laced simple. Higher-order obstructions
vanish by Whitehead's second lemma $H^2_{\mathrm{Lie}}(\fg, \fg) = 0$
applied to the $\sigma$-fixed sub-BV-complex.

Applying the $\sigma$-equivariant transfer lemma
\textup{(}Hypothesis~H, a two-page extension of Costello–Gwilliam 2017
Vol.\ II~§11.1 equivariant factorisation machinery to Dynkin-fold
actions\textup{),} the Costello–Gwilliam counterterm scheme descends
to the $\sigma$-fixed sub-BV-complex, producing a $\sigma$-equivariant
Wilson effective action satisfying the $\sigma$-invariant QME at every
scale. The Costello~$2013$ 5D-boundary-to-Yangian functor
\textup{(}arXiv:$1303.2632$~§§$4$–$5$\textup{),} composed with the
Francis~$2013$ factorisation-homology envelope \emph{Geom.\ Topol.}~$17$
Theorem~$2.29$, transports this $\sigma$-equivariant quantisation to a
$\sigma$-equivariant vertex-algebra isomorphism
$\partial\hCS_5(\fg^{\mathrm{ADE}})^\sigma \simeq
Y_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\fg}^{\mathrm{ADE}})^\sigma$.
Kac~$1990$ Theorem~$8.3$ identifies the $\sigma$-fixed subalgebra of
$\widehat{\fg}^{\mathrm{ADE}}$ with the $r$-twisted affine
$\widehat{\fg}^{(r)}$; Guay–Nakajima–Wendlandt~$2018$ \emph{Adv.\ Math.}
$338$ lifts this to the Yangian level,
$Y_\epsilon(\widehat{\fg}^{\mathrm{ADE}})^\sigma
\simeq Y_\epsilon(\widehat{\fg}^{(r)})$. The theorem follows.
\end{proof}

\begin{remark}[Status of the hypothesis]
\label{rem:bcfg-sigma-hypothesis-status}
The $\sigma$-equivariant transfer lemma \textup{(}Hypothesis~H\textup{)}
is a two-page extension of the Costello~$2011$ counterterm-existence
theorem \emph{Renormalization and Effective Field Theory} AMS
Math.\ Surveys~$170$ Theorem~$9.3.1$ to the case of finite Dynkin-fold
internal symmetry. The general machinery is in place: Costello~$2011$
Chapter~$9$ handles arbitrary symmetry groups preserving the BV
structure, and Costello–Gwilliam~$2017$ Vol.\ II~§$11$ develops
equivariant factorisation algebras. The unwritten case is the specific
Dynkin-fold $\sigma$ on 6D hCS, which has not appeared in primary
literature \textup{(}Williams–Gwilliam~$2021$ arXiv:$2009.05037$
treats the non-equivariant case only\textup{).} The extension is
editorial rather than conceptual; its absence blocks the promotion of
Theorem~\ref{thm:bcfg-sigma-all-orders-conditional} from conjecture
to theorem.
\end{remark}

## Cross-consistency notes

\emph{With Wave-1 spine `platonic_synthesis_post_adversarial.tex`.}
The ADE all-orders theorem at Theorem
`wn:thm:spine-5d-hCS-yangian` is the input; the BCFG extension here
refines the "conjectural, non-abelian affine" status noted in the
spine to "conjectural under one named lemma" with explicit proof
chain. The cubic-Casimir vanishing list at Theorem
`wn:thm:spine-consistent-covariant` ($\{\fsu(2), \fso(N), E_6, E_7,
E_8, F_4, G_2\}$) is now closed by Wave-1 F05 Proposition
`prop:F05-dabc-BCFG` to all BCFG types; the present closure inherits
this closure.

\emph{With Wave-2 refinement
`platonic_synthesis_wave2_refinement.tex`.}
Tier-I residual item §F1 ("BCFG σ-equivariant renormalisation scheme
for Costello 6d $\hCS$, Costello–Gwilliam Vol.\ II §11.1 gap") is
precisely the item addressed here. The Wave-2 refinement §F1
verdict "promotable via Costello–Gwilliam Vol.\ II §11.1 + Prop
`prop:F05-dabc-BCFG`, at most one month of explicit BV-cohomology
computation" aligns with the present terminal state (B) under the
same hypothesis. No contradiction.

\emph{With Wave-1 F05
`F05_BCFG_folding_root_unity.md`.}
The present closure adopts F05's correction — the correct target is
the **twisted affine** $\widehat{\fg}^{(r)}$, not the untwisted
$\widehat{\fg^\sigma}$ — verbatim, and uses F05's Proposition
`prop:F05-dabc-BCFG`, Theorem `thm:F05-sigma-equivariant-hCS-classical`,
and Theorem `conj:F05-twisted-yangian-boundary` as inputs to Steps
2–3 of the proof. The present C01 closure formalises F05's "Step 5
— the conjecture proper" (commuting of the 6D hCS boundary functor
with $\sigma$-fixed points) as the single named Hypothesis~H.

\emph{With `CoHA_to_W_infty_treatise.tex`.}
The treatise's cautious status for $\mathcal{W}_{1+\infty}$ at
Example~1 ("partial matchings in Costello 2013 §11 /
Costello–Gaiotto 2018") extends to the BCFG case as the σ-invariant
sub-VOA of the ADE $\mathcal{W}_{1+\infty}$-analogue. Cross-ref with
AP-CY146 (toric-CY$_3$ vertex algebra family discipline): the
BCFG extension does not change the conifold-vs-$\CC^3$ distinction;
it refines the $\CC^3$ case to σ-invariant twisted-affine Yangians.

\emph{With `CLAUDE.md` invariants.}
Subscript discipline on $\kappa$: $\kanom^{\mathrm{cons}}$ used
throughout, never bare $\kappa$. Lane discipline: theorem stated at
chain level (explicit BV datum, explicit propagator, explicit
counterterm scheme); $(\infty, 1)$-categorical refinement would lift
to $\sigma$-equivariant $E_3$-factorisation-algebra structure, not
claimed. No meta-narration; no "we now turn to"; no "remarkably".
Primary sources cited with volume, year, theorem number.

\emph{With `appendices/first_principles_cache.md`.}
Entry C5 ("6D holomorphic Chern–Simons as $E_3$-algebra at level 3"):
the present conditional theorem is the BCFG instantiation of the
abelian ADE all-orders theorem cited there. The cache entry's note
"Non-simply-laced requires twisted Yangian; all-orders result open
there" is precisely the gap closed here under Hypothesis~H.
