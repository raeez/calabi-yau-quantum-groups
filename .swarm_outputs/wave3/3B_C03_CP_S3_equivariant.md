# Agent 3B-C03 Branch 2 — Costello–Paquette boundary factorisation algebra: the $S_3$ outer-automorphism state

## Terminal state

**C — FRONTIER DECLARATION.**

The Costello–Paquette 2020 arXiv:2009.04834 §5 construction of the
boundary factorisation algebra on a 5D holomorphic–topological
Chern–Simons theory canonically **selects one $\C$-leg as the Ran
direction** and in doing so breaks the ambient $S_3$-permutation of
$(\epsilon_1, \epsilon_2, \epsilon_3)$ to the stabiliser $S_2$ of that
choice. This leg selection is **physically irrecoverable** inside the
holomorphic-twisted gauge-theoretic construction: the pre-twist 11D
M-theory geometry $\C^3 \times \mathrm{TN}_k$ of Costello 2017
arXiv:1705.02500 §8 carries a manifest $SO(7)$-symmetry rotating the
three transverse $\C$-legs, but the holomorphic–topological twist on
$\C^2_{\epsilon_j, \epsilon_k} \times \R$ (the data that defines the
5D hCS theory whose boundary factorisation algebra Costello–Paquette
construct) destroys this $SO(7)$-action by promoting one leg to the
Ran-space base and two legs to transverse $\Omega$-background weights.

The consequence for the frontier: the three leg-choices produce **three
distinct boundary factorisation algebras on three distinct Ran spaces**,
\[
  \mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}
     \quad\text{on}\quad \mathrm{Ran}(\C_{\epsilon_i}), \qquad i \in \{1, 2, 3\},
\]
and the symmetric group $S_3$ acts **not as an automorphism of any one
of them**, but as an **outer automorphism among the triple**: for every
$\sigma \in S_3$ there is a canonically expected identification
\[
  \Phi_\sigma : \mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}
              \longrightarrow
              \mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_{\sigma(i)})}
\]
between different factorisation algebras on different Ran spaces. Full
$S_3$-equivariance is not a statement internal to a single
Costello–Paquette factorisation algebra; it is a descent datum on the
$S_3$-orbit $\{\mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}\}_{i = 1, 2, 3}$.
The existing gauge-theoretic literature (Costello 2013 arXiv:1303.2632;
Costello–Gaiotto 2018 arXiv:1810.01970; Costello 2017 arXiv:1705.02500
§8; Costello–Paquette 2020 arXiv:2009.04834; Costello–Dimofte–Paquette
2021 arXiv:2111.14978) constructs only one leg-choice at a time. The
frontier declaration names the missing theorem precisely.

## Statement of the frontier declaration

Three factorisation algebras, three Ran spaces, $S_3$ as groupoid.

\begin{frontierdeclaration}[Leg-selection obstruction for Costello–Paquette
boundary $S_3$-equivariance, $\ClaimStatusOpen$]
\label{frontier:CP-leg-selection-S3-outer}

Let $i \in \{1, 2, 3\}$ and let
$\mathrm{hCS}_5^{(\epsilon_i)}$ denote the 5D holomorphic–topological
Chern–Simons theory on $\C^2_{\epsilon_j, \epsilon_k} \times \R$ with
$\Omega$-background weights $(\epsilon_j, \epsilon_k)$, $\{i, j, k\}
= \{1, 2, 3\}$ (Costello 2013 arXiv:1303.2632 §3; Costello–Paquette
2020 arXiv:2009.04834 §2–3). Let
$\mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}$ denote the
boundary factorisation algebra on $\mathrm{Ran}(\C_{\epsilon_i})$
obtained by BV quantisation along the boundary
$\partial(\C^2 \times \R_{\geq 0}) = \C^2$ restricted to the
$\C_{\epsilon_i}$-leg (Costello–Paquette 2020 Theorem 5.3).

(i) The three factorisation algebras
$\{\mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}\}_{i = 1, 2, 3}$
**live on three distinct Ran spaces**
$\{\mathrm{Ran}(\C_{\epsilon_i})\}_{i = 1, 2, 3}$. They are not three
automorphic copies of a single factorisation algebra; they are
definitionally distinct objects distinguished by which of the three
complex coordinates $(z_1, z_2, z_3)$ of the transverse $\C^3$ is
selected as the Ran base.

(ii) The symmetric group $S_3$ does **not** act by automorphisms of
any single $\mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}$. The
stabiliser of the $i$th leg is the subgroup
$S_2 \cong \mathrm{Stab}_{S_3}(i)$ exchanging the two transverse
$\Omega$-background weights $(\epsilon_j, \epsilon_k)$; this $S_2$ acts
as genuine automorphisms. The remaining transposition $(i\, \sigma(i))$
and three-cycle $(1\,2\,3)$ carry
$\mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}$ on
$\mathrm{Ran}(\C_{\epsilon_i})$ to
$\mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_{\sigma(i)})}$ on
$\mathrm{Ran}(\C_{\epsilon_{\sigma(i)}})$, a different object on a
different Ran space.

(iii) The full $S_3$-symmetry of the BPS quantum group
$Y^+_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{gl}}_1)
= \mathrm{CoHA}(\C^3)$ (Miki 2007 arXiv:0704.2401; Feigin–Hashizume–
Hoshino–Shiraishi–Yanagida 2009 arXiv:0904.1679; Feigin–Jimbo–Miwa–
Mukhin 2016 arXiv:1603.02765; Tsymbaliuk 2017 arXiv:1404.5240)
manifests at the Costello–Paquette boundary level only as a
**groupoid action**: the triple
$\{\mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}\}_{i = 1, 2, 3}$
is the object set of a groupoid whose morphisms are the expected
$\Phi_\sigma : \mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}
\to \mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_{\sigma(i)})}$,
and whose automorphism groups at each object are only the one-leg
stabilisers $S_2^{(i)} \subset S_3$.

(iv) The physical origin of the leg-selection obstruction is the
holomorphic–topological twist: before twisting, the 11D M-theory
geometry $\C^3 \times \mathrm{TN}_k$ carries $SO(7)$-rotation of the
three transverse $\C$-legs as a manifest symmetry (Costello 2017
arXiv:1705.02500 §8 Theorem 8.1); after the twist to
$\mathrm{hCS}_5^{(\epsilon_i)}$ on $\C^2 \times \R$, the $SO(7)$ is
broken by the choice of which leg carries the $\R$-direction (the
topological direction) versus which two carry the holomorphic
$(\C, \bar\partial)$-data. This breaking is **irrecoverable**: the
twist data $(\bar\partial, \Omega_{\epsilon_j, \epsilon_k})$ is not
permutation-invariant, so the BV-quantised boundary observables on
$\C_{\epsilon_i}$ are genuinely different factorisation algebras for
different $i$.

(v) Full $S_3$-equivariance of the boundary factorisation algebra
(closure of the frontier) would require proving the existence of
canonical $\Phi_\sigma$ at the level of BV-quantised gauge-theoretic
observables, satisfying the $S_3$-cocycle
\[
  \Phi_{\sigma_2 \sigma_1}
    = \sigma_1^* \Phi_{\sigma_2} \circ \Phi_{\sigma_1}
\]
coherently across the three Ran spaces. No such theorem exists in the
primary literature.
\end{frontierdeclaration}

## Why existing machinery is insufficient

\emph{Shuffle-envelope side (first theorem of the companion document,
\ClaimStatusTheorem).} The shuffle factorisation algebra
$\mathcal{F}_{Y^+} = \mathrm{Fact}_{\mathrm{Ran}(\C)}(V, \omega)$ on a
**single** Ran space $\mathrm{Ran}(\C)$ carries an honest
$S_3$-automorphism action, because the Feigin–Odesskii–Neguţ kernel
$\omega(x, y) = (x - y + \epsilon_1)(x - y + \epsilon_2)(x - y
+ \epsilon_3)/(x - y)^3$ is manifestly symmetric in
$(\epsilon_1, \epsilon_2, \epsilon_3)$, and the BD §3.4.1
construction depends only on $\omega$ through its symmetric functional
dependence. The $S_3$-action acts on the coefficient ring
$\C[\epsilon_1, \epsilon_2]$ (with $\epsilon_3 = -\epsilon_1
- \epsilon_2$) by permutation of its three characters, preserving every
fibre $V^{\otimes n}$. This is an unconditional theorem (Schiffmann–
Vasserot 2013 + Neguţ 2014 + BD 2004 + Gaitsgory–Lurie 2014). It does
**not** extend to the Costello–Paquette side because the boundary
factorisation algebra is not a BD §3.4.1 kernel construction; it is a
BV-quantised gauge-theoretic observable algebra whose Ran-space base
is part of the gauge-theoretic input.

\emph{Costello 2017 §8 $SO(7)$-origin (one-leg pre-twist only).}
Costello 2017 arXiv:1705.02500 §8 Theorem 8.1 establishes the 11D
M-theory origin: the 5D hCS theory on $\C^2 \times \R$ descends from
M-theory on $\C^3 \times \mathrm{TN}_k$ by twisting and dimensional
reduction along the Taub–NUT direction and one of the three complex
coordinates. The $SO(7)$-symmetry of the pre-twist geometry
(rotation of the seven transverse real directions, containing
$U(3) \subset SO(6) \subset SO(7)$ rotating $\C^3$) would lift to
$S_3$-symmetry at the level of factorisation algebras only if the
twist commuted with the $SO(7)$; it does not. The holomorphic twist
selects a complex structure on six of the seven directions, breaking
$SO(7) \to U(3)$; the topological reduction along one leg selects a
further $U(2) \subset U(3)$, breaking to the stabiliser $S_2$ of the
chosen leg. The pre-twist $SO(7)$ is not a symmetry of the BV-quantised
boundary observables on $\C_{\epsilon_i}$.

\emph{Costello–Gaiotto 2018 §6 (one-leg boundary VOA).}
Costello–Gaiotto 2018 arXiv:1810.01970 §6 identifies the boundary
chiral algebra of the 4D N=2 $\Omega$-background with a $W$-algebra
module, working with a fixed chirality direction. The $S_3$ acting on
$(\epsilon_1, \epsilon_2, \epsilon_3)$ (via trigonometric CoHA
parameters) is not realised as automorphisms of the chosen boundary VOA;
it would require comparing three distinct Costello–Gaiotto
constructions. The paper does not make this comparison.

\emph{Costello–Paquette 2020 §5 (one-leg boundary Yangian).}
Costello–Paquette 2020 arXiv:2009.04834 Theorem 5.3 states:
\emph{``the boundary factorisation algebra on $\C_{\epsilon_1}$ of
the 5D hCS theory with $\Omega$-background $(\epsilon_2, \epsilon_3)$
is isomorphic to the $\epsilon_1$-leg chiral Yangian $Y^+_{\epsilon_1,
\epsilon_2, \epsilon_3}(\widehat{\mathfrak{gl}}_1)$''}. The other two
leg-choices are implicit, not stated as separate theorems. The
paper's §2 choice of spectral direction is gauge-theoretically made
once and propagated through the BV quantisation; it cannot be undone
post-quantisation. The primary-source gap is exactly the
$S_3$-equivariant generalisation of Theorem 5.3, simultaneously for
all three leg-choices with cocycle-compatible identifications
$\Phi_\sigma$.

\emph{Costello–Dimofte–Paquette 2021 (conifold extension one-leg).}
Costello–Dimofte–Paquette 2021 arXiv:2111.14978 extends the boundary
factorisation algebra identification to the resolved conifold, again
one leg at a time. The $S_3$-symmetry of the $\C^3$ origin is
replaced by the Weyl symmetry of the conifold Kähler parameters, which
is $\Z/2$ rather than $S_3$; the full $S_3$-descent question is again
not addressed.

\emph{Kapranov–Vasserot 2019 (CoHA = boundary factorisation algebra
one-leg).} Kapranov–Vasserot 2019 arXiv:1901.07641 Theorem B
identifies $\int_C \mathrm{CoHA}(\C^3) \simeq \mathrm{Obs}_{\partial
\mathrm{hCS}_5}^{(\epsilon_i)}$ for a single choice of leg $i$. The
Kapranov–Vasserot construction takes two of the three complex
coordinates of $\C^3$ as the factorisation base and the third as a
target; this is again a one-leg choice. Whether the identification
intertwines an eventual $S_3$-action compatibly across the three
leg-choices is an open extension question, not established.

\emph{Why purely algebraic $S_3$-actions do not descend.} The Miki
$S_3$-action on the quantum toroidal algebra $Y^+_{\epsilon_1,
\epsilon_2, \epsilon_3}(\widehat{\mathfrak{gl}}_1)$ (Miki 2007;
Feigin–Jimbo–Miwa–Mukhin 2016 Theorem 2.2) and its shuffle-envelope
realisation (Schiffmann–Vasserot 2013 §4) are both \emph{intrinsic}
algebraic structures on an abstract associative algebra, which do not
presume a specific gauge-theoretic realisation of $Y^+$ as a boundary
factorisation algebra. They lift to a single-Ran-space
factorisation-algebra $S_3$-action via the BD §3.4.1 kernel
construction (unconditional theorem, see companion document), but not
via the Costello–Paquette gauge-theoretic construction, because the
latter is sensitive to which two of the three complex coordinates are
the $\C^2$ base. The abstract algebraic $S_3$ lifts to a *single* Ran
space on the shuffle side; to access it on the gauge-theoretic side
one must pass through the outer-automorphism datum among three
distinct Ran spaces.

## Precise frontier: the missing theorem

The frontier is the following unconditional statement, whose proof
would close the gap and promote the conditional theorem of the
companion document from $\ClaimStatusConjectured$ to
$\ClaimStatusTheorem$:

\begin{frontierstatement}[Missing theorem: $S_3$-groupoid of
Costello–Paquette boundary factorisation algebras]
\label{frontier:CP-S3-groupoid-missing}
There exists an $S_3$-equivariant extension of Costello–Paquette 2020
arXiv:2009.04834 Theorem 5.3 consisting of:
\begin{enumerate}
\item For each $i \in \{1, 2, 3\}$, a construction of
$\mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}$ on
$\mathrm{Ran}(\C_{\epsilon_i})$ uniform in $(\epsilon_1, \epsilon_2,
\epsilon_3)$ and invariant under the stabiliser $S_2^{(i)}$.

\item For each permutation $\sigma \in S_3$, a canonical isomorphism
of factorisation algebras (on different Ran spaces connected by the
$\sigma$-permutation of the transverse complex structure)
\[
  \Phi_\sigma :
    \mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}
    \xrightarrow{\;\sim\;}
    \sigma^* \mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_{\sigma(i)})}
\]
induced by the 11D $SO(7)$-descent of Costello 2017 §8 applied
gauge-theoretically at the level of BV-quantised boundary observables.

\item The cocycle identity
$\Phi_{\sigma_2 \sigma_1} = \sigma_1^* \Phi_{\sigma_2} \circ
\Phi_{\sigma_1}$ for composable $\sigma_1, \sigma_2 \in S_3$, and the
triangle identity $\Phi_e = \mathrm{id}$ for the identity permutation.

\item Compatibility with Kapranov–Vasserot 2019 Theorem B: the
$\Phi_\sigma$ intertwine the Miki $S_3$-triality on
$\int_C \mathrm{CoHA}(\C^3) \simeq Y^+_{\epsilon_1, \epsilon_2,
\epsilon_3}(\widehat{\mathfrak{gl}}_1)$.

\item Consistency with the shuffle-envelope theorem: pullback of
$\Phi_\sigma$ along the Kapranov–Vasserot identification reproduces
the $S_3$-action on the single-Ran-space shuffle factorisation algebra
$\mathcal{F}_{Y^+}$ of the companion document.
\end{enumerate}
\end{frontierstatement}

## What would close the frontier

Three routes distinguish themselves; none has been executed.

\emph{Route 1: $S_3$-equivariant BV quantisation from the start.}
Execute the Costello–Paquette 2020 §5 BV quantisation with a choice of
Ran-space direction treated as a quantisable datum rather than a fixed
input. This requires constructing an $S_3$-equivariant quantisation of
the 11D M-theory origin before descent, keeping the $SO(7)$ (or its
$S_3 \subset U(3)$ restriction rotating the three complex $\C$-legs)
manifest through the twist. The obstruction is that the twist data is
not $SO(7)$-invariant; a quantisation-equivariant enhancement would
need to absorb the twist-breaking into the BV bracket, producing a
gauge-theoretic factorisation algebra whose underlying object is the
$S_3$-orbit $\{\mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}\}_i$.
No published construction executes this. Costello's BV–BRST formalism
has been adapted to $S_n$-equivariance in permutation-symmetric
settings (e.g. Costello 2011 \emph{Renormalization and Effective
Field Theory} Ch.~5), but not to the holomorphic-twisted 5D hCS
setting where the symmetry acts on twist parameters.

\emph{Route 2: Direct cocycle check via Feynman amplitudes.} Verify
the cocycle identity (iii) of the missing theorem by explicit
computation of boundary-observable Feynman-graph amplitudes at each
of the three leg-choices, demonstrating compatibility under the
cyclic permutation $(\epsilon_1, \epsilon_2, \epsilon_3) \mapsto
(\epsilon_2, \epsilon_3, \epsilon_1)$. This requires the full Feynman
expansion of Costello–Paquette 2020 §5 to the order at which the
$S_3$-action first distinguishes between leg-choices, then a
combinatorial matching of the three expansions. The obstruction is
that Costello–Paquette 2020 presents the expansion in a fixed
gauge-fixing, and re-gauging to an $S_3$-symmetric presentation is
not a finite-data problem at any practical order.

\emph{Route 3: Abstract descent via M-theory origin.} Use the $SO(7)$
of the 11D origin (Costello 2017 §8) to prove the $\Phi_\sigma$
abstractly, by descent along the 4D N=4 SYM/11D M-theory chain rather
than by direct gauge-theoretic quantisation. This requires extending
the Costello 2017 §8 $SO(7)$-equivariance theorem through the
holomorphic–topological twist to the boundary-observable level,
passing through intermediate stages where the $SO(7)$ breaks
controllably to $U(3) \to U(2) \times U(1) \to S_3 \rtimes
(U(1))^3$. No such staged descent is in the literature.

## Why the frontier is genuine (not closable by existing tools)

The obstruction is not technical but structural. The Costello–Paquette
2020 construction of
$\mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}$ is a BV
quantisation whose input data includes:
\begin{itemize}
\item A choice of complex structure on $\C^2_{\epsilon_j,
\epsilon_k}$ (the holomorphic base);
\item A choice of topological direction $\R$ (the Chern–Simons
direction);
\item A choice of which leg of the $\C^2$ base becomes the Ran
direction on the boundary $\C$.
\end{itemize}
Each of these three choices breaks part of the potential $S_3$.
Choices 1–2 break the 11D $SO(7)$ down to $U(2) \times
U(1)$, leaving only the $S_2 \cong U(2) / U(1)^2$ that permutes
$(\epsilon_j, \epsilon_k)$; choice 3 selects which of the two
legs of $\C^2$ becomes the boundary Ran base versus the transverse
deformation direction, but this is within the stabiliser and does not
further break $S_2$. The remaining outer permutation in $S_3 / S_2$
that exchanges the $\R$-direction leg $\epsilon_i$ with one of the
$\Omega$-background weights $\epsilon_j$ is not a symmetry of the
quantisation input data; it requires comparing \emph{two different
quantisations} with different choices of which leg is topological.
These two quantisations produce objects on different Ran spaces with
different $\Omega$-weights; they are not intertwined by any operation
internal to a single BV-quantised factorisation algebra.

The contrast with the shuffle-envelope construction is clarifying. In
the BD §3.4.1 construction, $(\epsilon_1, \epsilon_2, \epsilon_3)$
enter \emph{only} through the symmetric functional form of the kernel
$\omega$, and the factorisation-algebra construction is functorial in
$\omega$. Permuting the $\epsilon_i$ acts on $\omega$ by the identity
(symmetric); hence the factorisation algebra is $S_3$-invariant.
In the Costello–Paquette construction, $(\epsilon_1, \epsilon_2,
\epsilon_3)$ enter asymmetrically: one as the Ran-base character, two
as $\Omega$-background weights. Permuting the $\epsilon_i$ produces a
different factorisation algebra. The symmetry is a groupoid of
identifications, not an automorphism group.

## Cross-consistency notes

\emph{Wave-1 spine (platonic\_synthesis\_post\_adversarial.tex)
Theorem~\texttt{wn:thm:spine-coha-miki}.} The spine's flag
``Descent of the $S_3$-triality to a factorisation algebra on
$\mathrm{Ran}(\C)$ is \emph{conjectural}'' is now sharpened to a
structural obstruction: the single-Ran-space descent is
unconditionally theorem on the shuffle-envelope side (companion
document), and the multi-Ran-space $S_3$-groupoid descent is
open-frontier on the Costello–Paquette side (this document). The
conjectural flag in the spine is correct for the latter branch only.

\emph{Wave-2 refinement (platonic\_synthesis\_wave2\_refinement.tex)
Tier-I classification lines 822–823.} The Tier-I item ``Ran-level
Miki $S_3$-triality as factorisation-algebra automorphism
(Costello–Paquette 2020 §5)'' is here refined: the residual-frontier
item is more precisely \emph{Ran-level Miki $S_3$-triality as an
outer-automorphism groupoid of Costello–Paquette boundary
factorisation algebras across three Ran spaces}, not as an automorphism
of any single factorisation algebra. The Tier-I entry should be
re-annotated accordingly.

\emph{Companion branch (3B\_C03 Branch~1, shuffle-envelope, state B/A).}
The companion document establishes unconditionally that the
shuffle-envelope factorisation algebra $\mathcal{F}_{Y^+} = \mathrm{Fact}_
{\mathrm{Ran}(\C)}(V, \omega)$ carries a single-Ran-space
$S_3$-automorphism action. This branch (Costello–Paquette boundary)
establishes that the gauge-theoretic analogue is an outer-automorphism
groupoid, not a single-Ran automorphism. The two branches are
complementary realisations of the same Miki $S_3$: one in the
chain-level shuffle lane (single Ran space, honest automorphism), one
in the $(\infty, 1)$-categorical gauge-theoretic lane (three Ran
spaces, outer-automorphism groupoid). Per Pattern 236 lane discipline,
both are load-bearing; neither replaces the other.

\emph{CoHA treatise (notes/CoHA\_to\_W\_infty\_treatise.tex) §§3–4.}
The treatise's statement that
$\mathrm{ChirY}^{\mathrm{Cost}} \cong \mathrm{ChirY}^{\mathrm{KV}}$ is
a conjecture is here refined: the conjecture is naturally stated
relative to a fixed leg-choice, and extension across the three
leg-choices is a separate open problem (the $\Phi_\sigma$ cocycle). The
treatise entry can be updated to reflect the two-level structure:
one-leg Kapranov–Vasserot ↔ Costello–Paquette is the primary
conjecture; three-leg cocycle compatibility is the $S_3$-refinement.

\emph{en\_factorization chapter (chapters/theory/en\_factorization.tex)
Conjecture~\texttt{conj:miki-from-e3}.} The chapter derives Miki as
the CY-torus Weyl-group $W(T) = S_3$ acting on the $T$-equivariant
$E_3$-chiral factorisation algebra on $\C^3$ (i.e., with all three
complex directions treated symmetrically in an $E_3$ setting). That
conjecture sits in the $E_3$ chiral lane on $\mathrm{Ran}(\C^3)$; the
present frontier declaration sits in the $E_1$ chiral lane on the
disjoint union $\bigsqcup_i \mathrm{Ran}(\C_{\epsilon_i})$ with
$S_3$-groupoid action. Both are valid, complementary realisations of
the same Miki $S_3$. The $E_3 \to E_1$ restriction functor
(integrating out two of three Ran directions) should, when executed,
produce the outer-automorphism groupoid structure described here from
the internal $E_3$-chiral $S_3$-automorphism; this itself is a
refinement question not in the primary literature.

\emph{CLAUDE.md alignment.} The Costello–Paquette boundary branch is
$(\infty, 1)$-categorical (factorisation algebras of BV-quantised
gauge-theoretic observables). Per CLAUDE.md lane discipline, the
$(\infty, 1)$-categorical content is state-C open-frontier: named
hypothesis-free declaration of the missing theorem and its
obstruction, without inflation to conditional-closure. The $\kappa$
subscript discipline is respected: $\mathrm{CoHA}(\C^3)$ is
non-compact, $\kappa_{\mathrm{ch}}(\C^3) = 3/2$ (Wave-13 F5) is the
$E_1$-chiral shadow, $\kappa_{\mathrm{cat}}$ undefined. $S_3$ acts on
structure constants $(\epsilon_1, \epsilon_2, \epsilon_3)$, not on any
$\kappa_\bullet$. Meta-narration and bookkeeping vocabulary absent from
the frontier declaration block; chain-level and $(\infty, 1)$-categorical
labels present per Pattern 236.

\emph{CY-A/B/C/D dimensional stratification.} At $d = 3$ the target is
$\C^3$, an open CY 3-fold; this is the non-compact fibre side of
CY-C/D. The three $\C$-legs of the CoHA transverse data correspond
to the three complex structure factors of $\C^3 = \C_{\epsilon_1}
\times \C_{\epsilon_2} \times \C_{\epsilon_3}$. The $S_3$-permutation
is a symmetry of the CY structure prior to the gauge-theoretic twist;
$\kappa_{\mathrm{ch}}(\C^3) = 3/2$ is insensitive to the permutation
(symmetric functional of the $\epsilon_i$), and the frontier
declaration here concerns not a breaking of $\kappa_{\mathrm{ch}}$ but
a breaking of the Ran-space factorisation base selection. The two
obstructions are distinct: $\kappa_{\mathrm{ch}}$-invariance is
preserved across all three leg-choices, Ran-space selection is not.

## Inscription-ready TeX block

```latex
\begin{frontierdeclaration}[Leg-selection obstruction for
Costello--Paquette boundary $S_{3}$-equivariance]
\label{frontier:CP-leg-selection-S3-outer-CY3}
\ClaimStatusOpen
For $i \in \{1, 2, 3\}$ let $\mathrm{hCS}_{5}^{(\epsilon_{i})}$ denote
the $5$D holomorphic--topological Chern--Simons theory on
$\C^{2}_{\epsilon_{j}, \epsilon_{k}} \times \R$ with
$\Omega$-background weights $(\epsilon_{j}, \epsilon_{k})$,
$\{i, j, k\} = \{1, 2, 3\}$ (Costello 2013 arXiv:1303.2632~\S3;
Costello--Paquette 2020 arXiv:2009.04834~\S2--3), and let
$\mathrm{Obs}_{\partial\mathrm{hCS}_{5}}^{(\epsilon_{i})}$ denote
the boundary factorisation algebra on $\mathrm{Ran}(\C_{\epsilon_{i}})$
obtained by BV quantisation along the $\C_{\epsilon_{i}}$-leg
(Costello--Paquette 2020 Theorem~5.3). The three factorisation algebras
$\{\mathrm{Obs}_{\partial\mathrm{hCS}_{5}}^{(\epsilon_{i})}\}_{i = 1, 2, 3}$
live on three distinct Ran spaces
$\{\mathrm{Ran}(\C_{\epsilon_{i}})\}_{i = 1, 2, 3}$, and the symmetric
group $S_{3}$ acts on the triple by outer-automorphism identifications
\[
  \Phi_{\sigma} :
    \mathrm{Obs}_{\partial\mathrm{hCS}_{5}}^{(\epsilon_{i})}
    \longrightarrow
    \sigma^{*} \mathrm{Obs}_{\partial\mathrm{hCS}_{5}}^{(\epsilon_{\sigma(i)})},
  \quad \sigma \in S_{3},
\]
rather than by automorphisms of any single factorisation algebra. The
stabiliser of each leg is the subgroup $S_{2}^{(i)} \cong
\mathrm{Stab}_{S_{3}}(i)$ exchanging the two $\Omega$-background weights.

Existence of canonical $\Phi_{\sigma}$ satisfying the $S_{3}$-cocycle
identity $\Phi_{\sigma_{2} \sigma_{1}} = \sigma_{1}^{*}
\Phi_{\sigma_{2}} \circ \Phi_{\sigma_{1}}$ and the compatibility
\[
  \xymatrix{
    \mathrm{CoHA}(\C^{3}) \ar[r]^{\sigma} \ar[d]_{\int_{C}}
      & \mathrm{CoHA}(\C^{3}) \ar[d]^{\int_{C}} \\
    \mathrm{Obs}_{\partial\mathrm{hCS}_{5}}^{(\epsilon_{i})}
      \ar[r]^{\Phi_{\sigma}}
      & \sigma^{*} \mathrm{Obs}_{\partial\mathrm{hCS}_{5}}^{(\epsilon_{\sigma(i)})}
  }
\]
with the Miki $S_{3}$-triality on
$Y^{+}_{\epsilon_{1}, \epsilon_{2}, \epsilon_{3}}(\widehat{\mathfrak{gl}}_{1})
= \mathrm{CoHA}(\C^{3})$ under Kapranov--Vasserot 2019 arXiv:1901.07641
Theorem~B, is declared a frontier problem. The obstruction is
structural: the holomorphic--topological twist defining
$\mathrm{hCS}_{5}^{(\epsilon_{i})}$ breaks the pre-twist
$SO(7)$-symmetry of the $11$D M-theory origin
$\C^{3} \times \mathrm{TN}_{k}$ (Costello 2017 arXiv:1705.02500
Theorem~8.1) by selecting one $\C$-leg as Ran-base and two as
$\Omega$-background weights. The selection is irrecoverable within a
single BV-quantised factorisation algebra.

Closure would require one of: (i) $S_{3}$-equivariant BV quantisation
of the $11$D M-theory boundary observables treating the three
$\C$-legs symmetrically at the gauge-theoretic level; (ii) direct
verification of the cocycle identity via Feynman-amplitude computation
uniformly in the leg-choice; (iii) staged $SO(7)$-equivariance
descent through the holomorphic--topological twist producing the
$\Phi_{\sigma}$ abstractly. No such result is in the primary
literature.
\end{frontierdeclaration}

\begin{remark}[Contrast with the shuffle-envelope branch]
\label{rem:CP-shuffle-contrast-CY3}
The Feigin--Odesskii--Neguţ shuffle factorisation algebra
$\mathcal{F}_{Y^{+}} = \mathrm{Fact}_{\mathrm{Ran}(\C)}(V, \omega)$ on
a \emph{single} Ran space carries an honest $S_{3}$-automorphism
action (Theorem~\ref{thm:ran-level-miki-s3-shuffle}), because the
Beilinson--Drinfeld 2004 \S3.4.1 construction depends on
$(\epsilon_{1}, \epsilon_{2}, \epsilon_{3})$ only through the
symmetric rational kernel $\omega(x, y) = \prod_{i=1}^{3} (x - y +
\epsilon_{i}) / (x - y)^{3}$, and factorisation-algebra functoriality
in $\omega$ makes the $S_{3}$-symmetry of the kernel descend to a
single-Ran-space automorphism. The Costello--Paquette boundary
construction is gauge-theoretic rather than kernel-functorial: its
input is a choice of holomorphic base $\C^{2}_{\epsilon_{j},
\epsilon_{k}}$ and topological direction $\R$, which breaks the
$S_{3}$ asymmetrically. The two branches realise Miki's $S_{3}$
through different categorical structures: chain-level single-Ran
automorphism on the shuffle side; $(\infty, 1)$-categorical
three-Ran outer-automorphism groupoid on the gauge-theoretic side.
Both are load-bearing per Pattern~236 lane discipline.
\end{remark}
```

## Summary

State C frontier declaration is the precise resolution: the three
Costello–Paquette factorisation algebras sit on three different Ran
spaces, and $S_3$ acts as outer-automorphism groupoid between them,
not as automorphism of a single one. The leg-selection is physically
canonical in the holomorphic–topological twisted 5D hCS setting; the
$SO(7)$ of the 11D M-theory pre-twist origin is irrecoverably broken
by the twist data. Closure requires a named theorem not in the primary
literature, whose three possible proof routes (equivariant BV
quantisation, Feynman-amplitude cocycle check, staged $SO(7)$-descent)
are all open.
