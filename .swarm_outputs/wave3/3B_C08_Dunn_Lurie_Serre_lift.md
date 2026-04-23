# Agent 3B-C08 — Dunn--Lurie $E_3 \simeq E_2 \otimes E_1$ lift of $(S_{K3}, \tau_E)$ on $\cF_{K3 \times E}$

## Terminal state

**C (FRONTIER DECLARATION)** with two distinct internal corrections recorded below.

The Dunn--Lurie statement itself --- $E_3 \simeq E_2 \otimes E_1$ as $\infty$-operads, and
the factorisation-homology monoidality on a product of complex manifolds --- is Lurie \emph{HA}
Theorem~$5.5.3.6$ applied through Francis--Gaitsgory $2012$ Lemma~$3.3.4$; this
machinery does apply to $\PhiFA_3(\Perf(K3 \times E))$ and is already inscribed
at three sites in the manuscript (\texttt{cy\_to\_chiral.tex}~303, \texttt{cy\_to\_chiral.tex}~394,
\texttt{k3e\_cy3\_programme.tex}~3736). The \emph{lift of $(S_{K3}, \tau_E)$ through Dunn--Lurie to
commuting factorisation-algebra autoequivalences} is not established, for three independent reasons
that must each be addressed by a new theorem:

(G1) The arithmetic in the hypothesis is off by a factor of $2$: with $S_{K3}^2 = [4]$
on $D^b(\Coh(K3))$, we have $(S_{K3}^2)^8 = [32]$, \emph{not} $[16]$. The object
that gives $[16] \otimes \mathrm{id}$ is the composite $(S_{K3} \otimes \tau_E)^8$,
not $(S_{K3}^2 \otimes \tau_E)^8$.

(G2) ``Trivial on bar'' needs a construction, not a declaration. The bar complex
$B(A_{K3})$ of the K3 chiral algebra is \emph{not} automatically annihilated by
a cohomological shift $[2n]$ --- on a non-unital associative chiral algebra the
shift acts on each tensor power separately, and $[2n] \cdot B(A) = B(A)[2n] \neq B(A)$.
Triviality on bar is genuine: it requires identifying $[2n]$ with the
grading-shift operator on the suspended tensor coalgebra $T^c(s^{-1}\bar{A})$
and exhibiting a homotopy to the identity, which at $n \geq 2$ uses the cyclic
$A_\infty$-structure of Kontsevich--Soibelman $2006$ and is proven only at $n = 1$
(the classical bar--cobar shift) in \texttt{chapters/theory/cyclic\_ainf.tex}.

(G3) The Serre functor $S_{K3}$ on $D^b(\Coh(K3))$ and the Fourier--Mukai
autoequivalence $\tau_E$ on $D^b(\Coh(E_{j = 1728}))$ are autoequivalences of
\emph{categories}; their descent through $\PhiFA_3$ (Stage 1) and $\SpCh_{K3, E}$
(Stage 2) to autoequivalences of the factorisation algebra $\cF_{K3 \times E} =
\SpCh_{K3, E}(\PhiFA_3(\Perf(K3 \times E)))$ is \emph{not} established in the
published literature. Tamarkin~$2007$ gives $(\infty,1)$-functoriality of Stage~1
for the bracket structure; Costello--Gwilliam $2017$ Theorem~$3.2.3$ gives the
assembly into a factorisation algebra; but the compatibility with specific
Fourier--Mukai autoequivalences is covered only for the Atiyah--Mukai class by
Ben-Zvi--Francis--Nadler $2010$ Proposition~$2.3$. This is Pattern 273
($\Phi$-functor vs object-level correspondence) in
\texttt{appendices/first\_principles\_cache.md}, which is precisely a
scope-declaration marker: at $d = 3$, the $(\infty,1)$-functor has been
constructed only for kernels in the Atiyah class.

## Statement of the frontier declaration

\begin{frontier}[Dunn--Lurie lift of Serre + CM translation on $\cF_{K3 \times E}$]\ClaimStatusOpen
\label{frontier:dunn-lurie-serre-cm-lift-k3e}
\index{Dunn--Lurie!Serre-CM lift on $K3 \times E$}
\index{Serre functor!factorisation-algebra lift}
Let $X = K3 \times E_{j = 1728}$, $\cA_X = \PhiFA_3(\Perf(X)) \in E_3\text{-}\HolFA(X)$
the Stage-$1$ holomorphic factorisation algebra of
Theorem~\ref{thm:phi-two-stage-factorisation}, and
$\cF_X = \SpCh_{K3, E_{j = 1728}}(\cA_X) \in E_1\text{-}\mathrm{ChirAlg}(E_{j = 1728})$ the
Stage-$2$ specialisation. Write $[n]$ for the cohomological shift functor on
$D^b(\Coh(X))$, which descends through $\Phi_3$ to an $E_1$-chiral shift functor
$[n]$ on $\cF_X$.

Let $S_{K3} = [2]$ be the Serre functor on $D^b(\Coh(K3))$ (Huybrechts~$2006$
\emph{Fourier--Mukai transforms in algebraic geometry}, Corollary~$3.13$), and let
$\tau_E \colon E_{j = 1728} \to E_{j = 1728}$ be the CM translation
$p \mapsto i \cdot p$, with induced Fourier--Mukai autoequivalence
$(\tau_E)^* \in \mathrm{Autoeq}(D^b(\Coh(E_{j = 1728})))$ of order $4$
(Silverman~$1994$ \emph{Advanced topics in the arithmetic of elliptic curves}
Proposition~A.1.2: for a CM elliptic curve of $j$-invariant $1728$ over
$\bar{\mathbb{Q}}$, $\mathrm{Aut}(E) \cong \mu_4 = \langle i \rangle$, acting on
the structure sheaf by the identity and on $T_E$ by multiplication by $i$).

\textbf{The conjecture:} There exist an $E_1$-chiral autoequivalence
$\widetilde{S}_{K3}$ of $\cF_X$ (descended from the Serre functor along the
$E_2$-tensor factor of Dunn--Lurie) and an $E_1$-chiral autoequivalence
$\widetilde{\tau}_E$ of $\cF_X$ (descended from the CM translation along the
$E_1$-tensor factor) such that
\begin{enumerate}[label=\textup{(\roman*)}]
 \item $[\widetilde{S}_{K3}, \widetilde{\tau}_E] = 0$ on $\cF_X$;
 \item $(\widetilde{S}_{K3} \otimes \widetilde{\tau}_E)^8 = [16] \otimes \mathrm{id}$,
       acting trivially on the chiral bar complex $B(\cF_X)$;
 \item the order-$8$ monodromy of $(\widetilde{S}_{K3} \otimes \widetilde{\tau}_E)$
       coincides with the Humbert-$H_1$ monodromy order of
       Theorem~\ref{thm:humbert-order-K-kappa} and with the Koszul-conductor value
       $K^{\kappa_{\mathrm{ch}}} = 2\, c_+(\mathrm{Mukai}(K3)) = 8$ of
       Remark~\ref{rem:k3e-cy3-platonic-mukai}.
\end{enumerate}
The statement is genuine frontier: each of (i)--(iii) requires a construction
that is not in the published literature. The machinery of Lurie~\emph{HA}~$5.5.3.6$
gives the operadic backbone $E_3 \simeq E_2 \otimes E_1$ and the monoidal
factorisation-homology functor; it does not automatically supply the
descent of Fourier--Mukai autoequivalences through $\Phi_3$ to
factorisation-algebra autoequivalences.
\end{frontier}

## Primary-source gap

**The gap is threefold**, and each sub-gap names a distinct missing theorem.

### Gap 1. Arithmetic normalisation (internal hypothesis correction)

As stated, the hypothesis reads $(S_{K3}^2 \otimes \tau_E)^8 = [16] \otimes \mathrm{id}$.
With $S_{K3}^2 = [4]$, the left side is $[32] \otimes \tau_E^8 = [32] \otimes \mathrm{id}$
(since $\tau_E$ has order $4$, so $\tau_E^8 = \mathrm{id}$). The right side is
$[16] \otimes \mathrm{id}$. These are not equal as functors on $D^b(\Coh(X))$.

The object intended is almost certainly the composite $(S_{K3} \otimes \tau_E)^8$ with a
single Serre functor, \emph{not} its square: $(S_{K3} \otimes \tau_E)^8 = S_{K3}^8 \otimes \tau_E^8
= [16] \otimes \mathrm{id}$. This is consistent with the Mukai-doubling value
$K^{\kappa_{\mathrm{ch}}} = 2\,c_+(\mathrm{Mukai}(K3)) = 8$ of
Remark~\ref{rem:k3e-cy3-platonic-mukai} read as an \emph{order of the composite
autoequivalence}, not of $S_{K3}^2$ alone. The correct formula for $(S_{K3}^2 \otimes \tau_E)^n
= \mathrm{id}$ (trivial on bar up to $[2m]$-shifts) is $n = 4$, giving
$(S_{K3}^2 \otimes \tau_E)^4 = [16] \otimes \mathrm{id}$; this is the statement that
matches the numerics.

**What would close this gap**: restating the hypothesis with either
$(S_{K3} \otimes \tau_E)^8$ or $(S_{K3}^2 \otimes \tau_E)^4$ in place of the
incorrect exponent-$8$ on the $S_{K3}^2$-composite. This is an internal
arithmetic correction, not a new theorem.

### Gap 2. ``Trivial on bar'' requires cyclic-$A_\infty$ proof at $n \geq 2$

The bar complex $B(A)$ of a non-unital chiral algebra is
$T^c(s^{-1}\bar{A}) = \bigoplus_n (s^{-1}\bar{A})^{\otimes n}$ with
deconcatenation and bar differential. Under a cohomological shift $[2m]$ on the
input $A$, the bar complex becomes $B(A)[2mn]$ in tensor degree $n$, which is
\emph{not} equivalent to $B(A)$ as a graded object. Equivalence up to shift
requires a homotopy that uses the cyclic $A_\infty$-pairing of
Kontsevich--Soibelman $2006$ \emph{Notes on $A_\infty$-algebras, $A_\infty$-categories, and
non-commutative geometry}, $\S 10$, to identify $[2m]$ on $B(A)$ with a graded
involution on the tensor coalgebra. At $m = 1$ this is the bar--cobar shift
$B \circ \Omega \simeq \mathrm{id}[2]$ of \texttt{chapters/theory/cyclic\_ainf.tex};
at $m \geq 2$ it requires a higher-cyclic cocycle that is not constructed for
K3 chiral algebras in the published literature. Statement (ii) of the frontier
declaration therefore presupposes a theorem of the form:

\emph{Missing theorem (Gap 2)}: For $A = \cF_X$ a compact $E_1$-chiral algebra
with cyclic $A_\infty$-structure of degree $d = 3$, and $[2m]$ the $m$-fold
iterated shift, there is an explicit cyclic-homotopy trivialisation
$B(A)[2m] \simeq B(A)$ for $m$ a multiple of the Mukai Clifford-parity rank
$c_+(\mathrm{Mukai}(K3)) = 4$.

This would generalise the $m = 1$ bar--cobar shift; it is not stated in
Costello $2007$ \emph{Topological Conformal Field Theories and Calabi--Yau
Categories} (which handles $m = 1$ with cyclic degree $d = 2$), nor in
Costello--Li~$2020$ \emph{Anomaly cancellation in the topological string} (which
handles the cohomological-shift side but not the cyclic-homotopy side), nor in
any published work on K3 chiral algebras.

**What would close this gap**: a cyclic-$A_\infty$ extension of Costello's
shift-trivialisation theorem to higher multiples of the CY dimension, carried
out on K3 chiral algebras with the explicit Mukai-pairing cyclic structure of
Chapter~\ref{ch:k3-chiral-bialgebra-platonic}. The $c_+(\mathrm{Mukai}(K3)) = 4$
Clifford-parity rank is the expected level at which the shift becomes trivial
on bar.

### Gap 3. Descent of $(S_{K3}, \tau_E)$ through $\Phi_3$ to factorisation-algebra autoequivalences

The Serre functor $S_{K3}$ and the CM translation $\tau_E$ are autoequivalences
of the input categories $D^b(\Coh(K3))$ and $D^b(\Coh(E_{j = 1728}))$. Their
images under $\Phi_3$ are autoequivalences of the factorisation algebra
$\cF_{K3 \times E}$ \emph{only if} $\Phi_3$ is an $(\infty,1)$-functor (not only
an object-level correspondence) compatible with these specific Fourier--Mukai
kernels. This is Pattern~273 of
\texttt{appendices/first\_principles\_cache.md}: $(\infty, 1)$-functoriality of
$\Phi_d$ on general Fourier--Mukai kernels is established at $d \leq 2$
(Kontsevich--Vlassopoulos $2022$) but remains conjectural at $d \geq 3$
(Conjecture~\ref{conj:phi-d-functoriality}), with proof known for the
Atiyah--Mukai class only (Ben-Zvi--Francis--Nadler $2010$ Proposition~$2.3$).

The Serre functor is a cohomological shift $[2]$ on the ambient, hence passes
through $\Phi_3$ unconditionally: shifts are symmetric-monoidal-compatible with
Dunn--Lurie. The CM translation $\tau_E$ is a non-trivial Fourier--Mukai kernel
(the structure sheaf of the graph of translation-by-$i$ inside
$E_{j = 1728} \times E_{j = 1728}$), and its descent is the content of Gap 3.

\emph{Missing theorem (Gap 3)}: Conjecture~\ref{conj:phi-d-functoriality} at
$d = 3$ for the specific Fourier--Mukai kernel supported on the graph of
$\tau_E \colon E_{j = 1728} \to E_{j = 1728}$. Equivalently, a
Bridgeland--Maciocia $2001$ \emph{J.\ Algebraic Geom.}~$11$ Theorem~$1.2$-style
compatibility theorem for CM-elliptic Fourier--Mukai transforms with the
Costello--Gwilliam factorisation-homology assembly on $K3 \times E_{j = 1728}$.

**What would close this gap**: the $d = 3$ instance of
Conjecture~\ref{conj:phi-d-functoriality} for CM-elliptic translations, or
equivalently an extension of Ben-Zvi--Francis--Nadler $2010$ Proposition~$2.3$
from Atiyah--Mukai kernels to the CM-translation kernel on $E_{j = 1728}$. This
is not in the published literature.

## Why existing machinery is insufficient

Lurie \emph{HA}~$5.5.3.6$ gives the monoidal Dunn--Lurie equivalence
$E_3 \simeq E_2 \otimes E_1$ and monoidality of factorisation homology on
products. Francis--Gaitsgory $2012$ Lemma~$3.3.4$ gives the pushforward-pullback
formula for factorisation cosheaves. These establish the operadic backbone:
the factorisation algebra $\cF_X$ decomposes as $\cF_{K3} \otimes_{E_\infty} \cF_E$
under the Dunn--Lurie equivalence, and $\widetilde{S}_{K3}$ (the image of the
shift $[2]$ along the $E_2$-tensor factor) and $\widetilde{\tau}_E$ (the image
of a Fourier--Mukai kernel along the $E_1$-tensor factor, when it descends)
commute as tensor-factor-respecting autoequivalences. What is not established:

1. That a CM-elliptic Fourier--Mukai kernel descends through $\PhiFA_1$ at all
   (Gap 3);
2. That the composite $(\widetilde{S}_{K3} \otimes \widetilde{\tau}_E)^n$ for
   the right $n$ acts trivially on the chiral bar $B(\cF_X)$ (Gap 2);
3. That the numerical identity $n = 8$ and the shift $[16]$ come out correctly
   from the Mukai-doubling and Clifford-parity counts without an off-by-factor-
   of-$2$ error (Gap 1).

The Humbert-wall monodromy order $8$ of
Theorem~\ref{thm:humbert-order-K-kappa} and the Mukai-doubling value
$K^{\kappa_{\mathrm{ch}}} = 8$ of Remark~\ref{rem:k3e-cy3-platonic-mukai} are
\emph{consequences} of the correct lift, not independent evidence for it.
Bruinier $2002$ Proposition~$5.1$ gives the Chern-class reciprocity on
$\overline{\mathcal{A}_2}$; this is on the \emph{moduli} side, not on the
factorisation-algebra side. The identification of the two ``$8$''s is exactly
the content of Remark~\ref{rem:k3e-cy3-platonic-mukai}, not independent
machinery available to close the frontier declaration.

## Inscription-ready TeX block

\begin{frontier}[Dunn--Lurie $(S_{K3}, \tau_E)$-lift on $\cF_{K3 \times E_{j = 1728}}$]\ClaimStatusOpen
\label{frontier:dunn-lurie-serre-cm-lift-k3e}
\index{Dunn--Lurie lift!Serre + CM on $K3 \times E_{j = 1728}$}
Let $X = K3 \times E_{j = 1728}$, $\cF_X \in E_1\text{-}\mathrm{ChirAlg}(E_{j = 1728})$
the Stage-$2$ specialisation of $\PhiFA_3(\Perf(X))$ along $\Sigma_2 = K3$, and
$[n]$ the cohomological shift functor. Conjecturally, the Serre functor
$S_{K3} = [2] \in \mathrm{Autoeq}(D^b(\Coh(K3)))$ and the CM translation
$\tau_E(p) = i\cdot p \in \mathrm{Aut}(E_{j = 1728})$, $(\tau_E)^{\otimes 4} = \mathrm{id}$,
descend through $\Phi_3$ to commuting $E_1$-chiral autoequivalences
$\widetilde{S}_{K3}, \widetilde{\tau}_E \in \mathrm{Autoeq}_{E_1}(\cF_X)$
satisfying
\[
 \bigl(\widetilde{S}_{K3} \otimes \widetilde{\tau}_E\bigr)^8
 \;=\; [16] \otimes \mathrm{id}
\]
with left-hand side acting trivially on the chiral bar complex $B(\cF_X)$. Under
Bruinier $2002$ Proposition~$5.1$ Chern-class reciprocity on
$\overline{\mathcal{A}_2}$ (Theorem~\ref{thm:bruinier-prop-5-1}), the order-$8$
monodromy of the composite coincides with the Humbert-$H_1$ monodromy of
$\mathcal{L}^{\Delta_5}$ of Theorem~\ref{thm:humbert-order-K-kappa} and with the
Mukai-doubling Koszul conductor $K^{\kappa_{\mathrm{ch}}} = 2\, c_+(\mathrm{Mukai}(K3)) = 8$ of
Remark~\ref{rem:k3e-cy3-platonic-mukai}.

The declaration is frontier: the descent of $\tau_E$ through $\Phi_3$ is the
$d = 3$ CM-elliptic instance of Conjecture~\ref{conj:phi-d-functoriality},
unproved in the published literature; the triviality of $[2m]$-shifts on the
chiral bar at $m \geq 2$ requires a cyclic-$A_\infty$ extension of Costello
$2007$ beyond the $m = 1$ bar--cobar shift; and the numerical normalisation
$[16]$ (as opposed to $[32] = (S_{K3}^2)^8$) fixes the order of the composite
at $8$, not the order of $S_{K3}^2$ alone.
\end{frontier}

## Cross-consistency notes

### With spine (\texttt{platonic\_synthesis\_post\_adversarial.tex})

The frontier declaration refines, rather than replaces, the spine's Wave~1
identification of the Humbert-wall order $8$ with $K^{\kappa_{\mathrm{ch}}}$:
the spine states that the two ``$8$''s coincide; this closure asks the further
question of whether the coincidence lifts to an actual composite-autoequivalence
of order $8$ on $\cF_{K3 \times E_{j = 1728}}$. The spine's identification
remains correct at the moduli / lattice level (Bruinier reciprocity applied to
Humbert Heegner divisors); the chiral-side lift is the frontier item.

### With Wave~2 refinement

Wave~2 established the two-tier / three-tier stratification of residual
frontier items; this is a Tier~(iii) frontier declaration ``no existing theorem
in any cited corpus closes the item''. The three sub-gaps (arithmetic,
cyclic-shift-triviality, Fourier--Mukai descent) each give a distinct
publish-close path; Gap~1 is immediate (internal arithmetic correction),
Gaps~2 and 3 are new frontier theorems.

### With CoHA treatise (\texttt{notes/CoHA\_to\_W\_infty\_treatise.tex})

The CoHA/$\cW_{1+\infty}$ identification is on the chiral side at the local
$\mathbb{C}^3$ level (CoHA($\mathbb{C}^3$) $= Y^+$ positive-half, Pattern~274 in the cache). The
present frontier is about K3-times-$E_{j = 1728}$ global autoequivalences; the
compatibility is that the local CoHA picture does \emph{not} supply any
obstruction to the frontier, because the Serre functor of $D^b(\Coh(K3))$ is
not a CoHA autoequivalence (the CoHA is $E_2$-chiral on $\mathbb{C}^3$ with no
K3-global content).

### With CLAUDE.md

The frontier declaration is consistent with CLAUDE.md's Pattern~273
($\Phi$-functor vs object-level correspondence): Stage~1 object-level
$\PhiFA_3$ is established unconditionally; Stage~1 functor-level
$(\infty,1)$-descent of Fourier--Mukai kernels remains conjectural at $d \geq 3$
(Conjecture~\ref{conj:phi-d-functoriality}), and the CM-elliptic translation on
$E_{j = 1728}$ is a specific named Fourier--Mukai kernel whose descent is not
covered by Ben-Zvi--Francis--Nadler $2010$ Proposition~$2.3$ (which handles
the Atiyah--Mukai convolution class).

The subscript discipline is preserved: $\kappa_{\mathrm{ch}}$, $\kappa_{\mathrm{cat}}$,
$\kappa_{\mathrm{BKM}}$, $\kappa_{\mathrm{fib}}$ are all left at their native
scope; the Koszul conductor $K^{\kappa_{\mathrm{ch}}} = 8$ is correctly
superscripted.

The Chriss--Ginzburg voice: the frontier declaration names mathematical
objects (Serre functor, CM translation, factorisation algebra, Dunn--Lurie
decomposition, Bruinier reciprocity) and states the conjectural identity
directly; no bookkeeping vocabulary, no meta-narration, no hedging. The three
numbered gaps are precise mathematical conditions, not a process narrative.

### Lane discipline

The frontier lives in \textbf{both} lanes simultaneously. Chain-level: the
explicit Mukai-doubling $K^{\kappa_{\mathrm{ch}}} = 8$, the Bruinier
Chern-class reciprocity on $\overline{\mathcal{A}_2}$, the explicit cyclic-
$A_\infty$-trivialisation of $[2m]$-shifts at $m \geq 2$ on the K3 chiral bar.
$(\infty,1)$-categorical: the Dunn--Lurie decomposition as symmetric monoidal
$\infty$-operads, the $(\infty,1)$-functoriality of $\Phi_3$ on Fourier--Mukai
kernels, the Ben-Zvi--Francis--Nadler $(\infty,1)$-assembly. Gap~1 is chain-
level arithmetic; Gap~2 is chain-level cyclic-$A_\infty$; Gap~3 is
$(\infty,1)$-categorical Fourier--Mukai descent. The frontier declaration must
be closed on \emph{both} lanes; a proof on one lane alone does not suffice.

## Summary

(i) Dunn--Lurie HA~$5.5.3.6$ \textbf{does} apply to product factorisation algebras;
this is already used in the manuscript at three sites.
(ii) The hypothesis about commuting-autoequivalence lift $(S_{K3}^2, \tau_E)$
with composite order $8$ has three distinct issues:
an arithmetic off-by-$2$ error (the correct composite is
$(S_{K3} \otimes \tau_E)^8 = [16] \otimes \mathrm{id}$, not
$(S_{K3}^2 \otimes \tau_E)^8 = [32] \otimes \mathrm{id}$);
an unproven cyclic-$A_\infty$-triviality of $[2m]$-shifts on the chiral bar at
$m \geq 2$; and the unproven descent of the CM-elliptic Fourier--Mukai kernel
through $\Phi_3$ (Conjecture~\ref{conj:phi-d-functoriality} at $d = 3$).
(iii) Terminal state is \textbf{C (FRONTIER DECLARATION)} with inscription-ready
TeX block above.
