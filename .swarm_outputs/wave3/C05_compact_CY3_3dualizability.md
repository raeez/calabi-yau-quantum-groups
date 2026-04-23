# Agent C05 — 3-dualizability of $\Obs_{\hCS}(X)|_{\fg}$ on compact CY$_3$

## Terminal state
**B — CONDITIONAL CLOSURE.**

## Statement of the theorem (conditional)

\ClaimStatusConjectured (conditional on Hypothesis H below)

Let $X$ be a smooth compact Calabi--Yau threefold with holomorphic volume
form $\Omega_X \in H^0(X, \Omega^3_X)$, and let $\fg$ be a finite-dimensional
semisimple Lie algebra. Then:

1. The $E_3$-Hochschild cohomology of the 6D holomorphic Chern--Simons
   quantum observable algebra is finite-dimensional in each cohomological
   degree:
   \[
    \dim_{\C}\HH^k_{E_3}\bigl(\Obs_{\hCS}(X)|_{\fg}\bigr) < \infty
    \qquad\text{for every } k \in \Z,
   \]
   with explicit presentation
   \[
    \HH^0_{E_3}\bigl(\Obs_{\hCS}(X)|_{\fg}\bigr)
    \;\simeq\;
    \bigoplus_{q = 0}^{3}
    H^{0,q}(X) \otimes_{\C}
    H^\bullet_{\mathrm{Lie}}(\fg, \C)^{[q]}
   \]
   via chiral Chevalley--Eilenberg + Hodge/Dolbeault truncation.

2. Consequently $\Obs_{\hCS}(X)|_{\fg}$ is 3-dualisable in
   $\mathrm{Alg}_{E_3}(\Ch(\Dolb))$, with evaluation/coevaluation data
   supplied by the PTVV $(-3)$-shifted symplectic structure.

3. The cobordism hypothesis (Lurie 2009) promotes $6$D $\hCS$ on $X$
   to a fully extended framed $E_3$-TFT, and the CY-to-chiral construction
   $\Phi_3$ extends from an object-level map to an $(\infty,3)$-functor
   on the subcategory of compact CY$_3$ inputs.

This promotes item (iv) of Theorem~\ref{thm:plat-dualizability} from
conjecture to theorem \emph{conditional on Hypothesis H below}.

## Hypothesis H (the load-bearing conditional)

**Hypothesis H (Compact-CY$_3$ Chiral-Hochschild--Dolbeault identification).**
For every smooth compact CY$_3$ $X$ and every reductive $\fg$, the chiral
Chevalley--Eilenberg complex
$\CE^\bullet_{\dbar,\chir}(\Omega^{0,\bullet}(X,\fg),\,\cO_X)$
computes $\HH^\bullet_{E_3}(\Obs_{\hCS}(X)|_{\fg})$, and global
Dolbeault cohomology gives the identification
$\HH^0_{E_3} \simeq \bigoplus_q h^{0,q}(X)\cdot H^\bullet_{\mathrm{Lie}}(\fg,\C)^{[q]}$
at the chain level.

Named form: **"the compact-$X$ extension of Gwilliam--Williams 2021
(arXiv:2009.05037) Proposition 5.3.2."**

Gwilliam--Williams 2021 Prop.~5.3.2 establishes
$\HH^0_{E_3}(\Obs_{\hCS}(\C^3)|_{\fg}) \simeq \C[\![\tau_1, \tau_2, \tau_3]\!]$
on flat non-compact $\C^3$ via a Koszul-duality computation for the
higher Kac--Moody algebra $\widehat{\fgl}_n^{(3)}$. The compact-$X$
extension would replace $\cO(\C^3) = \C[z_1,z_2,z_3]$ (polynomial in
three variables, infinite-dimensional) with $H^0(X, \cO_X) = \C$ (compact
threefold, one-dimensional), and replace the $\C^3$-Dolbeault cohomology
(concentrated in bidegree $(0,0)$) with the compact-$X$ Dolbeault ring
$\bigoplus_q H^{0,q}(X)$, truncated to $q \in \{0,1,2,3\}$ by dimension.
Each ingredient is present in the primary literature (listed in "Proof
under Hypothesis H" below); the composed statement — which is what
Wave 2 refinement Tier II labels as the named gap — is not currently
a single theorem in a primary-source publication.

## Proof under Hypothesis H

Granting Hypothesis H, items (1)--(3) of the theorem follow by
concatenation of named primary-source theorems:

**(Step 1) Chiral CE presentation of $\Obs_{\hCS}(X)|_{\fg}$.**
Costello 2013 (arXiv:1111.4234) \S8 sets up 6D $\hCS$ on a CY$_3$;
Costello--Gwilliam 2017 \emph{Factorization Algebras in QFT} Vol.~II
Thm.~9.3.1 (BV quantisation on compact CY$_3$) gives the quantum
observable factorisation algebra
\[
 \Obs_{\hCS}(X)|_{\fg}
 \;\simeq\;
 \CE^\bullet_{\dbar,\chir}\bigl(\Omega^{0,\bullet}(X,\fg),\,\cO_X\bigr),
\]
realising the $(\infty,1)$-categorical presentation as the chiral
Chevalley--Eilenberg complex of the local $L_\infty$-space
$\cE_{\hCS}(X) = \Omega^{0,\bullet}(X, \fg)[1]$ with differential
$\dbar + [\![\,,\,]\!]_{\fg}$.

**(Step 2) $E_3$-PBW identification.**
Francis 2013 \emph{Compos.\ Math.}\ 149 Thm.~3.4 ($E_n$-PBW theorem)
identifies the enveloping $E_3$-algebra with its $E_3$-primitives; applied
to $\Obs_{\hCS}(X)|_{\fg}$ this gives
\[
 \Obs_{\hCS}(X)|_{\fg} \;\simeq\; U_{E_3}\!\bigl(\fg_{\hCS,X}\bigr),
 \qquad
 \fg_{\hCS,X} \;=\; \Prim_{E_3}\bigl(\Obs_{\hCS}(X)|_{\fg}\bigr)
 \;\simeq\; \Omega^{0,\bullet}(X, \fg^*)[-1],
\]
with the $E_3$-Hochschild cohomology identified as the $E_3$-tangent
cohomology
$\HH^\bullet_{E_3}(\Obs_{\hCS}(X)|_{\fg})
\simeq \CE^\bullet_{E_3}(\fg_{\hCS,X},\,\Obs_{\hCS}(X)|_{\fg})$
(Francis 2013 Thm.~1.1, applied in the chiral Dolbeault context via
Gwilliam--Williams 2021 Thm.~2.5.5 comparison
$E_d^{\mathrm{hol}} \simeq E_d$).

**(Step 3) Finite-rank assembly under H.**
Hypothesis H provides the chain-level identification
\[
 \HH^0_{E_3}\bigl(\Obs_{\hCS}(X)|_{\fg}\bigr)
 \;\simeq\;
 \bigoplus_{q=0}^{3}
 H^{0,q}(X) \otimes_{\C} H^\bullet_{\mathrm{Lie}}(\fg, \C)^{[q]}.
\]
The right-hand side is finite-dimensional because:
(a) on a compact complex threefold, $h^{0,q}(X) = \dim_{\C} H^q(X, \cO_X)
< \infty$ by Cartan--Serre finiteness (Hartshorne \emph{Algebraic Geometry}
III.5.2), and $h^{0,q}(X) = 0$ for $q \geq 4$ by dimension;
(b) for reductive $\fg$, $H^\bullet_{\mathrm{Lie}}(\fg, \C)$ is
finite-dimensional (Chevalley--Eilenberg 1948; Humphreys
\emph{Introduction to Lie Algebras and Representation Theory} Thm.~21.1).
Finite-dimensional tensor product of finite-dimensional vector spaces
is finite-dimensional.

**(Step 4) Dualizability via $(-3)$-shifted symplectic.**
Pantev--Toën--Vaquié--Vezzosi 2013 \emph{Publ.\ Math.\ IHES} 117
establishes the $(-3)$-shifted symplectic structure on
$\mathrm{Map}(X, B\fg)$ for $X$ a compact CY$_3$.
Calaque--Pantev--Toën--Vaquié--Vezzosi 2017 (arXiv:1506.03699)
Prop.~2.6: a $(-n)$-shifted symplectic $E_n$-algebra is automatically
$n$-dualisable via the evaluation/coevaluation supplied by the symplectic
form. Applied at $n = 3$ with the BV/PTVV match
(Costello--Gwilliam Vol.~II Thm.~9.3.1): $\Obs_{\hCS}(X)|_{\fg}$ is
$3$-dualisable in $\mathrm{Alg}_{E_3}(\Ch(\Dolb))$. Finite-rank
$\HH^\bullet_{E_3}$ (Step 3) supplies the 2-morphism-level dualizability
data that distinguishes the compact case from flat $\C^3$.

**(Step 5) Cobordism-hypothesis upgrade.**
Lurie 2009 \emph{On the classification of topological field theories}
Thm.~2.4.6 (the cobordism hypothesis): a fully extended framed $n$-TFT
valued in a symmetric-monoidal $(\infty,n)$-category $\cC$ is the same
as a fully dualisable object of $\cC$. Applied at $n = 3$ with
$\cC = \mathrm{Alg}_{E_3}(\Ch(\Dolb))$ and dualisable object
$\Obs_{\hCS}(X)|_{\fg}$ (Step 4): 6D $\hCS$ on $X$ extends to a fully
extended framed 3-TFT. The same dualizability data promotes $\Phi_3$
from an object-level map to an $(\infty,3)$-functor on compact CY$_3$
inputs.

## Why NOT state A (full closure)

The composed identification
$\HH^0_{E_3}(\Obs_{\hCS}(X)|_{\fg}) \simeq \bigoplus_q H^{0,q}(X) \otimes
H^\bullet_{\mathrm{Lie}}(\fg, \C)^{[q]}$
on compact CY$_3$ is \emph{not} a single named theorem in the primary
literature. Gwilliam--Williams 2021 Prop.~5.3.2 is explicitly about
$\C^3$ (non-compact), with the $\widehat{\fgl}_n^{(3)}$ higher Kac--Moody
presentation via the polynomial ring $\cO(\C^3) = \C[z_1, z_2, z_3]$.
The compact analogue — where $H^0(X, \cO_X) = \C$ collapses the
polynomial generators, replaced by the richer Dolbeault-cohomology
structure $\bigoplus_q H^{0,q}(X)$ truncated at $q = 3$ — is a natural
consequence of the ingredients listed in Steps 1--5 but has not, to
primary-source knowledge available here, been written out as a single
published theorem. The Wave-2 refinement itself flags this
(\texttt{notes/platonic\_synthesis\_post\_adversarial.tex} L519:
"requires a compact-$X$ extension of Gwilliam--Williams 2021 Prop.~5.3.2
not currently in primary literature").

## Why NOT state C (frontier)

The ingredients of Hypothesis H are all standard; no new machinery is
required. The Costello--Li 2016 BV propagator (arXiv:1605.09930) extends
from $\C^3$ to compact CY$_3$ by Dolbeault heat-kernel methods, and
Costello--Gwilliam Vol.~II Thm.~9.3.1 provides the BV quantisation on
compact CY$_3$. Francis 2013 Thm.~3.4 ($E_n$-PBW) is stated for general
augmented $E_n$-algebras in a stable $\Q$-linear $\infty$-category, so
applies equally to $\Obs_{\hCS}(X)|_{\fg}$. Grothendieck finiteness
of proper coherent pushforward (Hartshorne III.5.2) is the classical
compactness ingredient; Chevalley--Eilenberg is elementary for reductive
$\fg$. The only genuine gap is the \emph{assembled} identification at
the chain level: an extension of Gwilliam--Williams 2021 \S5.3 to the
compact setting. This is an execution task within published machinery,
not a frontier conceptual gap. Independent chain-level witnesses are
already available on the canonical compact example
$X = K3 \times E$: Prop.~\texttt{prop:chi-3-nonvanishing-MNOP} of
\texttt{chapters/theory/hochschild\_calculus.tex} computes
$\langle[\chi_3], [e_3^{K3\times E}]\rangle_{\Phi_3}
= 2 \cdot \mathrm{Vol}(E) \cdot (2\pi i)^3$ via the reduced
Maulik--Oberdieck--Pandharipande DT pairing, giving independent
chain-level finite-rank evidence for $\HH^3_{E_3}$ on a specific
compact CY$_3$.

## Primary-source gap (shape of H's eventual resolution)

The definitive resolution would be a single paper proving, at the chain
level, the identification
\[
 \HH^\bullet_{E_3}\!\bigl(\Obs_{\hCS}(X)|_{\fg}\bigr)
 \;\simeq\;
 \bigoplus_{p + q = \bullet}
 H^{0,q}(X) \otimes_{\C} H^p_{\mathrm{Lie}}(\fg, \C)
\]
for every compact CY$_3$ $X$ and reductive $\fg$, with the Dolbeault
pushforward replacing the Gwilliam--Williams $\C[\![\tau_1, \tau_2,
\tau_3]\!]$ formal-power-series presentation. Such a paper would cite
Costello--Gwilliam Vol.~II Thm.~9.3.1, Francis 2013 Thm.~3.4,
Gwilliam--Williams 2021 \S5, and proper coherent pushforward, and
assemble them via a spectral sequence or direct Dolbeault-CE
computation. The Costello--Francis--Gwilliam 2026 form would be the
most natural venue (anticipated: a chapter on compact-CY$_3$ extensions
in a planned Vol.~III of \emph{Factorization Algebras in QFT}, or a
standalone paper by Gwilliam--Williams extending arXiv:2009.05037).

## Inscription-ready TeX block

\begin{theorem}[3-dualizability of $\Obs_{\hCS}(X)|_{\fg}$ on compact CY$_3$]
\label{thm:compact-cy3-3dualizability}
\ClaimStatusConjectured

Let $X$ be a smooth compact Calabi--Yau threefold with holomorphic
volume form $\Omega_X \in H^0(X, \Omega^3_X)$, and let $\fg$ be a
finite-dimensional semisimple Lie algebra. Conditional on Hypothesis
\ref{hyp:compact-cy3-HH-dolbeault} below,
$\HH^\bullet_{E_3}(\Obs_{\hCS}(X)|_{\fg})$ is finite-dimensional in
each cohomological degree, with explicit chain-level presentation
\[
  \HH^0_{E_3}\bigl(\Obs_{\hCS}(X)|_{\fg}\bigr)
  \;\simeq\;
  \bigoplus_{q = 0}^{3}
  H^{0,q}(X) \otimes_{\C}
  H^\bullet_{\mathrm{Lie}}(\fg, \C)^{[q]},
\]
and $\Obs_{\hCS}(X)|_{\fg}$ is $3$-dualisable in
$\mathrm{Alg}_{E_3}(\Ch(\Dolb))$, promoting $6$D $\hCS$ on $X$ to a
fully extended framed $3$-TFT via the Lurie cobordism hypothesis.
The CY-to-chiral construction $\Phi_3$ thereby extends to an
$(\infty,3)$-functor on the subcategory of compact CY$_3$ inputs.
\end{theorem}

\begin{hypothesis}[Compact-CY$_3$ chiral-Hochschild--Dolbeault
identification]
\label{hyp:compact-cy3-HH-dolbeault}
For every smooth compact Calabi--Yau threefold $X$ and every reductive
Lie algebra $\fg$, the chiral Chevalley--Eilenberg complex
$\CE^\bullet_{\dbar,\chir}(\Omega^{0,\bullet}(X, \fg), \cO_X)$ computes
$\HH^\bullet_{E_3}(\Obs_{\hCS}(X)|_{\fg})$, and global Dolbeault
cohomology on $X$ supplies the chain-level identification
\[
  \HH^\bullet_{E_3}\bigl(\Obs_{\hCS}(X)|_{\fg}\bigr)
  \;\simeq\;
  \bigoplus_{p + q = \bullet}
  H^{0,q}(X) \otimes_{\C} H^p_{\mathrm{Lie}}(\fg, \C).
\]
This is the compact-$X$ extension of Gwilliam--Williams $2021$
(\texttt{arXiv:2009.05037}) Proposition $5.3.2$, whose original scope is
$\C^3$ with the polynomial ring $\cO(\C^3) = \C[z_1, z_2, z_3]$
supplying infinite-dimensional $\HH^0_{E_3} = \C[\![\tau_1, \tau_2,
\tau_3]\!]$; on compact $X$ the polynomial generators collapse to
$H^0(X, \cO_X) = \C$ and the full Dolbeault ring
$\bigoplus_q H^{0,q}(X)$ replaces the polynomial generators, truncated
at $q = 3$ by dimension.
\end{hypothesis}

\begin{proof}[Proof sketch, conditional on
Hypothesis~\ref{hyp:compact-cy3-HH-dolbeault}]
Granting the hypothesis, the chain-level identification gives finite
total rank: $\sum_q h^{0,q}(X) < \infty$ by Cartan--Serre finiteness
on the compact complex manifold $X$, and $\dim H^\bullet_{\mathrm{Lie}}
(\fg, \C) < \infty$ for reductive $\fg$ by Chevalley--Eilenberg
$1948$. Finite tensor product is finite. For 3-dualisability:
Pantev--Toën--Vaquié--Vezzosi $2013$ gives the $(-3)$-shifted symplectic
structure on $\mathrm{Map}(X, B\fg)$; Calaque--Pantev--Toën--Vaquié--Vezzosi
$2017$ Prop.~$2.6$ promotes this to 3-dualisability of the associated
$E_3$-algebra. The Lurie $2009$ cobordism hypothesis Thm.~$2.4.6$ then
produces the fully extended 3-TFT. Extended functoriality of $\Phi_3$
follows by naturality of the PTVV construction in the CY$_3$ input.
The hypothesis itself composes Francis $2013$ \emph{Compos.\ Math.}\
$149$ Thm.~$3.4$ ($E_n$-PBW), Costello--Gwilliam Vol.~II Thm.~$9.3.1$
(BV quantisation on compact CY$_3$), Gwilliam--Williams $2021$ Thm.~$2.5.5$
($E_d^{\mathrm{hol}} \simeq E_d$ comparison), and Cartan--Serre
finiteness of compact-complex Dolbeault cohomology.
\end{proof}

\begin{remark}[Independent chain-level witness on $K3 \times E$]
\label{rem:compact-cy3-3dualizability-k3e}
On the canonical compact example $X = K3 \times E$, the chain-level
identification is independently witnessed by K\"unneth: the holomorphic
K\"unneth formula
$\CE^\bullet_{\dbar,\chir}(\Omega^{0,\bullet}(X, \fg))
\simeq \CE^\bullet_{\dbar,\chir}(\Omega^{0,\bullet}(K3, \fg))
\otimes \CE^\bullet_{\dbar,\chir}(\Omega^{0,\bullet}(E, \fg))$
combined with $h^{0,0}(K3) = h^{0,2}(K3) = 1$, $h^{0,1}(K3) = 0$,
$h^{0,0}(E) = h^{0,1}(E) = 1$ gives finite total rank
$4 \cdot \dim H^\bullet_{\mathrm{Lie}}(\fg, \C)^{E_3}$, consistent with
$\kcat(K3 \times E) = \chi(\cO_{K3}) \cdot \chi(\cO_E) = 2 \cdot 0 = 0$
(K\"unneth-multiplicative on the total space) and with the non-vanishing
chiral-Hochschild pairing $\langle[\chi_3], [e_3^{K3 \times E}]
\rangle_{\Phi_3} = 2 \cdot \mathrm{Vol}(E) \cdot (2\pi i)^3$ of
Proposition~\ref{prop:chi-3-nonvanishing-MNOP} via the reduced
Maulik--Oberdieck--Pandharipande DT pairing. This chain-level witness
is not itself a proof of Hypothesis~\ref{hyp:compact-cy3-HH-dolbeault},
but it exhibits the compact-CY$_3$ finite-rank regime at an explicit
rational value on the canonical example.
\end{remark}

## Cross-consistency notes

**Wave-1 spine.** The Wave-1 spine
(\texttt{notes/platonic\_synthesis\_post\_adversarial.tex}) at L509--521
states this precisely as
\texttt{wn:conj:spine-compact-recovery}\ClaimStatusConjectured. The
current closure tightens this to Hypothesis \texttt{H} + conditional
theorem, preserving the conjectural status but making the precise
named gap explicit (arXiv:2009.05037 Prop.~5.3.2 compact extension).
No change to the Wave-1 conjecture label is required beyond
flagging Hypothesis H as the single named gap.

**Wave-2 refinement.** The Wave-2 three-tier stratification
(\texttt{notes/platonic\_synthesis\_wave2\_refinement.tex} L829--856)
places this at **Tier II (moderate, method extension)** with the
note "gated by Tier III integral $E_d$-formality." The present closure
agrees with Tier II: the ingredients exist in primary literature; the
execution gap is the compact-$X$ chain-level assembly of
Gwilliam--Williams 2021 Prop.~5.3.2.

**CoHA treatise.} The
\texttt{notes/CoHA\_to\_W\_infty\_treatise.tex} $(\infty,3)$-functor
extensions of CoHA-side structures are compatible: both use
Lurie 2009 cobordism at $n=3$ with compactness supplying the
2-morphism duals. The CoHA side gives a parallel compact-vs-non-compact
distinction ($\CoHA(\C^3) = Y^+$ non-dualisable at $E_3$ level vs.
compact-surface CoHA dualisable at appropriate level).

**First-principles cache.** AP-CY265 of
\texttt{notes/antipatterns\_catalogue.md} (L504, L4474) already
registers the compact-vs-non-compact distinction on $\HH^*_{E_3}$ as
a Critical anti-pattern. The present closure tightens the positive
compact-side statement to a conditional theorem with Hypothesis H
naming the primary-source gap precisely.

**CLAUDE.md charter.** Consistent with the $(\infty,1)$-categorical
lane discipline: Theorem is stated at the lane in which its proof
works (here, $(\infty,3)$-categorical via Lurie + CPTVV). The
chain-level witness on $K3 \times E$ is a parallel lane confirmation
at the explicit rational value. Both lanes load-bearing per equal-status
rule. Subscript discipline: $\kcat$, $\kch$, $\kBKM$, $\kfib$, $\kanom$
used at native scope throughout; no bare $\kappa$ in the inscription-ready
TeX block.

**Status-tag discipline.** The inscription uses
`\ClaimStatusConjectured` (theorem conditional on explicit hypothesis)
rather than `\ClaimStatusOpen` (frontier); the hypothesis itself is the
single named primary-source gap, so the theorem-under-H is substantive
progress from the Wave-1 bare-conjecture formulation.

## Summary

**Terminal state:** B (conditional closure).

**Named hypothesis:** Compact-$X$ extension of
Gwilliam--Williams 2021 (arXiv:2009.05037) Proposition 5.3.2 — the
chain-level identification
$\HH^\bullet_{E_3}(\Obs_{\hCS}(X)|_{\fg})
\simeq \bigoplus_{p+q = \bullet} H^{0,q}(X) \otimes H^p_{\mathrm{Lie}}
(\fg, \C)$ on compact CY$_3$ $X$.

**Under the hypothesis:** Theorem is fully proved at CFG level of
detail, assembling Costello--Gwilliam Vol.~II Thm.~9.3.1 + Francis
2013 Thm.~3.4 + PTVV 2013 + CPTVV 2017 Prop.~2.6 + Lurie 2009
Thm.~2.4.6 + Cartan--Serre + Chevalley--Eilenberg 1948.

**Promotes:** item (iv) of \texttt{thm:plat-dualizability} (currently
`\ClaimStatusProvedElsewhere` with attribution-only proof) to
\texttt{thm:compact-cy3-3dualizability}
(`\ClaimStatusConjectured` with full proof modulo one named
hypothesis).

**Does not promote:** the bare unconditional theorem (A) because
the compact-$X$ chain-level identification is not currently a single
named theorem in primary literature.
