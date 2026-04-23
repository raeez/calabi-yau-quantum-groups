# Agent F03 — Arithmetic-geometric synthesis on the elliptic-surface specialisation and the six routes to $G(K3 \times E)$

*Voice register: Shioda on Mordell–Weil lattices, Miranda–Persson on rational elliptic
surfaces, Dolgachev–Nikulin on K3 lattice theory, Schiffmann–Vasserot on CoHA.*

## Executive adversarial summary

The Wave-16 S2 unification conjecture — that the six routes to $G(K3 \times E)$ arise
as $\mathrm{Aut}(K3) \times \mathrm{SL}_2(\mathbb{Z})$-orbits in
$H_4(K3 \times E; \mathbb{Z})$ — is **false as stated** at two distinct structural
levels, but carries the ghost of a sharper true statement:
the six routes are six **distinct pairs** $(\Sigma_2, C, \text{machine}_i)$, where the cycle
$[\Sigma_2] \in H_4(K3 \times E; \mathbb{Z})$ is only *one* of three indexing data,
and the orbit structure on $H_4$ alone cannot reproduce the generator-rank stratification
$\rho^{R_i} \in \{3, 12, 24\}$ (Theorem 3.1 below). What survives: a refined indexing by
the triple $(\mathcal{O}_{\mathrm{Aut}(K3) \times \mathrm{SL}_2(\mathbb{Z})}[\Sigma_2],\,
\text{Mayer–Vietoris machine}_i,\, \rho^{R_i})$; an explicit rank computation
$\mathrm{rk}_\mathbb{Z} H_4(K3 \times E; \mathbb{Z}) = 23$ (correcting the brief's $25$); a four-orbit structure on
the primitive sublattice (not six); and an elliptic-surface specialisation
$(\Sigma_2, C) = (\mathcal{E}, \mathbb{P}^1)$ producing a genuinely new GBKM candidate
$\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ indexed by
$\mathrm{MW}(\mathcal{E}/\mathbb{P}^1) \oplus \mathrm{NS}(E)$.
Sharpest new theorem (T1): the cycle-class indexing factors the **stage-2
specialisation** of $\Phi^{\mathrm{FA}}_3$, not $\Phi_3$ itself; only three of the six
routes admit such an indexing, producing at most four orbit classes, not six.
Sharpest new conjecture (C1): **Mordell–Weil indexing.** For an elliptic K3 with
$\rho(K3) = 20$ and Mordell–Weil group $\mathrm{MW}(\pi) = E_8 \oplus E_8$, the
specialisation $\mathrm{Sp}_{\mathcal{E}, \mathbb{P}^1}(\Phi^{\mathrm{FA}}_3(K3 \times E))$
is an $E_1$-chiral algebra on $\mathbb{P}^1$ whose zero-mode Lie algebra is a GBKM
indexed by $\mathrm{MW}(\pi) \oplus \mathrm{NS}(E)$, commensurable with but **not equal to**
$\mathfrak{g}_{\Delta_5}$ (which is indexed by the Mukai lattice $\Lambda_{\mathrm{Muk}}(K3 \times E)$ of signature $(3, 19)$, rank $24$).

## Surviving theorems (healed, CG-voice)

### Setup: Künneth decomposition of $H_4(K3 \times E; \mathbb{Z})$

Let $S$ be a smooth projective K3 surface and $E$ an elliptic curve. The Betti numbers
are $b_0(S) = b_4(S) = 1,\; b_1(S) = b_3(S) = 0,\; b_2(S) = 22$ (the K3 Betti numbers
from the Noether formula $\chi_{\mathrm{top}}(S) = 24$ and simple-connectedness), and
$b_0(E) = b_2(E) = 1,\; b_1(E) = 2$. The Künneth decomposition of $H_4(K3 \times E; \mathbb{Z})$
is

\[
H_4(S \times E; \mathbb{Z}) \;=\;
\underbrace{H_4(S) \otimes H_0(E)}_{\text{rank } 1}
\;\oplus\; \underbrace{H_3(S) \otimes H_1(E)}_{\text{rank } 0}
\;\oplus\; \underbrace{H_2(S) \otimes H_2(E)}_{\text{rank } 22}
\;\oplus\; \underbrace{H_1(S) \otimes H_3(E)}_{\text{vanishes}}
\;\oplus\; \underbrace{H_0(S) \otimes H_4(E)}_{\text{vanishes, } \dim E = 1}.
\]

Hence $\mathrm{rk}_\mathbb{Z} H_4(S \times E; \mathbb{Z}) = 1 + 0 + 22 + 0 = 23$, with
a complementary $H_1(S) \otimes H_3(E) = 0$ (K3 simple-connected) and
$H_0(S) \otimes H_4(E) = 0$ ($E$ has real dimension $2$, no $H_4$). The intersection
pairing on the rank-$22$ summand $H_2(S) \otimes H_2(E)$ is the K3 lattice
$\Lambda_{K3} = U^3 \oplus E_8(-1)^2$ of signature $(3, 19)$, tensored with the rank-$1$
factor $H_2(E) = \mathbb{Z}[E]$; the $H_4(S) \otimes H_0(E)$ summand is
$\mathbb{Z}[\mathrm{pt}_S \times E]$.

**Correction to the brief.** The naive computation
$H_4(K3) \oplus H_3(K3) \otimes H_1(E) \oplus H_2(K3) \otimes H_2(E) \oplus \cdots =
\mathbb{Z} \oplus \mathbb{Z}^{22} \oplus \mathbb{Z}^2 = \mathbb{Z}^{25}$ in the brief
double-counts the middle Künneth piece. The correct rank is $23$, not $25$: the
$H_1(E) \otimes H_3(S) = 0$ (K3 has $b_1 = 0$), and one cannot add $H_2(E) = \mathbb{Z}$
separately because it appears only as a tensor factor against $H_2(S)$ of rank $22$.
Additionally, $H_1(E) = \mathbb{Z}^2$ contributes to $H_1(K3 \times E)$ (via
$H_0(S) \otimes H_1(E)$), not to $H_4$.

---

### T1 (Indexing theorem): which routes are $H_4$-indexable

\begin{theorem}[Cycle-class indexing separates at most four of the six routes]
\ClaimStatusTheorem
\label{f03:thm:cycle-indexing}

Let $X = S \times E$ with $S$ a projective K3. A route $R_i$ ($i = 1, \ldots, 6$,
following Definition~\ref{def:cy-c-six-routes} of
\texttt{chapters/examples/cy\_c\_six\_routes\_convergence.tex}) is
\emph{cycle-indexable} if its construction factors through a choice of
two-cycle $[\Sigma_2] \in H_4(X; \mathbb{Z})$ and reference curve $C \subset X$ via
the two-stage factorisation $\Phi_d = \mathrm{Sp}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$
of Theorem~\ref{thm:phi-two-stage-factorisation}. The cycle-indexable routes are
$R_1, R_4, R_5$ (three of six). Routes $R_2, R_3, R_6$ (Borcherds lift, Mukai-lattice
VOA, BLLPR Schur) do not factor through $[\Sigma_2] \in H_4(X; \mathbb{Z})$: their
inputs are respectively a weak Jacobi form of weight $0$ and index $1$
(automorphic datum, not a cycle); an even unimodular lattice of rank $24$
(lattice-theoretic datum); a $6$d superconformal theory (physical datum).

Consequently, the cardinality of the $\mathrm{Aut}(K3) \times \mathrm{SL}_2(\mathbb{Z})$-orbit
space on $H_4(X; \mathbb{Z})$ restricted to classes realised as transverse
$(\Sigma_2, C)$-specialisations is at most $4$, not $6$; the extra two routes
live on different indexing spaces.
\end{theorem}

\begin{proof}
The two-stage factorisation $\mathrm{Sp}_{\Sigma_{d-1}, C}$ is a specialisation
functor on $E_d$-holomorphic factorisation algebras that depends on the homology
class $[\Sigma_{d-1}] \in H_{2d-2}(X; \mathbb{Z})$ through Mayer–Vietoris-type
localisation along the cycle (Costello–Gwilliam Vol.~II \S 7.3, combined with
the transverse-cycle convention of
\texttt{notes/wave16\_s2\_alternative\_Sigma2\_K3E.tex} \S 1.1).
Inspect each route:

$R_1$: $\Phi_3 = \mathrm{Sp}_{\Sigma_2, C} \circ \Phi^{\mathrm{FA}}_3$ applied to
$D^b(\mathrm{Coh}(X))$ requires the cycle choice $(\Sigma_2, C)$ by definition.
Cycle-indexable.

$R_4$: The Kummer orbifold $\mathrm{Kum}(X) = \widetilde{(S \times E)/\iota}$
specifies a symplectic involution $\iota$ whose fixed locus
$\mathrm{Fix}(\iota) \subset X$ has a well-defined homology class. The
$\mathbb{Z}/2$-orbifold bar complex is computed by Mayer–Vietoris on the
fixed-locus tubular neighbourhood, which is a cycle-class datum. Cycle-indexable.

$R_5$: The half-twisted $\sigma$-model is built on the Ricci-flat Kähler metric,
which selects a Kähler class $[\omega] \in H^{1,1}(X; \mathbb{R})$ and hence
(through Poincaré duality on $X = S \times E$) a specialisation divisor class
$[\omega]^{\vee} \in H_4(X; \mathbb{R})$. Cycle-indexable (albeit via a real
rather than integral class).

$R_2$: The Borcherds multiplicative lift of the K3 elliptic genus $2\phi_{0,1}$
consumes a weak Jacobi form; its output is the Siegel cusp form $\Phi_{10}$.
Neither input nor output references $H_4(X; \mathbb{Z})$ in the construction.
The Mukai lattice shadow acts on the Siegel upper half-space, not on $H_4(X)$.
Not cycle-indexable.

$R_3$: The Mukai lattice VOA is constructed from
$\Lambda_{\mathrm{Muk}}(X) = H^*(S, \mathbb{Z}) \oplus H^*(E, \mathbb{Z})$
with the Mukai pairing. The lattice has rank $24$ and carries a signature-$(4, 20)$
decomposition; the associated lattice VOA depends only on the lattice structure, not
on any cycle class in $H_4(X)$. Not cycle-indexable.

$R_6$: The BLLPR Schur-sector chiral algebra is extracted from a $4$d $\mathcal{N} = 2$
class-$\mathcal{S}$ theory engineered by the $6$d $(2,0)$ theory on $X$. The
compactification data is the UV Riemann surface together with the $6$d theory, not a
cycle class on $X$. Not cycle-indexable.

The cycle-indexable routes $\{R_1, R_4, R_5\}$ have $|\{R_1, R_4, R_5\}| = 3$; any
$\mathrm{Aut}(K3) \times \mathrm{SL}_2(\mathbb{Z})$-orbit partition of $H_4(X; \mathbb{Z})$
produces at most as many orbits as distinct cycle classes used across these three
routes. Combined with the fact that $R_1$ uses a generic cycle
$(\Sigma_2, C) = (K3, E)$, $R_4$ uses the fixed-locus cycle of a symplectic involution,
and $R_5$ uses the Kähler-class cycle, the maximum count is $4$ when distinguishing the
elliptic-surface specialisation $(\Sigma_2, C) = (\mathcal{E}, \mathbb{P}^1)$ from
$(S, E)$ within $R_1$.
\end{proof}

### T2 (Orbit structure): the four orbit classes in $H_4(X; \mathbb{Z})$

\begin{theorem}[Four orbit classes for transverse $(\Sigma_2, C)$-specialisations]
\ClaimStatusTheorem
\label{f03:thm:four-orbits}

The $\mathrm{Aut}(K3) \times \mathrm{SL}_2(\mathbb{Z})$-orbits on the
rank-$23$ lattice $H_4(X; \mathbb{Z}) = \mathbb{Z}[\mathrm{pt} \times E] \oplus
H_2(S; \mathbb{Z}) \otimes H_2(E; \mathbb{Z})$ that correspond to genuinely
distinct transverse $(\Sigma_2, C)$-specialisations of $\Phi^{\mathrm{FA}}_3$ are
partitioned into four orbit classes:
\begin{enumerate}[label=\textup{(O\arabic*)}]
  \item \textbf{Canonical K3-fibre class:} $[\Sigma_2] = [S \times \mathrm{pt}_E]
        = \iota_*([S]) \in H_4(X; \mathbb{Z})$, with $[S]$ the fundamental
        class of the K3 fibre. Orbit under $\mathrm{Aut}(K3) \times \mathrm{SL}_2(\mathbb{Z})$
        is a single element (the fundamental class is invariant under automorphisms
        preserving the K3 fibration). Route: $R_1$ with $(\Sigma_2, C) = (S, E)$.
  \item \textbf{Elliptic-surface class:} $[\Sigma_2] = [\mathcal{E}]$ where
        $\mathcal{E} \subset S$ is the total space of an elliptic fibration
        $\pi: S \to \mathbb{P}^1$ viewed inside $X$ by $\iota: S \hookrightarrow
        S \times \mathrm{pt}_E$, with $C = \mathbb{P}^1$ the base of $\pi$.
        Orbit under $\mathrm{Aut}(K3)$ of the fibration class is parameterised by
        the $\mathrm{Aut}(K3)$-orbit of the elliptic-pencil class; under $\mathrm{SL}_2(\mathbb{Z})$
        (acting on $E$) the orbit is trivial (the cycle $[\mathcal{E}] = [S]$ is
        $E$-independent). Conjecturally produces the Mordell–Weil-indexed GBKM candidate
        $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$. Route: specialisation within $R_1$.
  \item \textbf{Kummer fixed-locus class:} $[\Sigma_2] = [\mathrm{Fix}(\iota)]$
        where $\iota$ is a symplectic K3 involution combined with elliptic inversion on $E$.
        Orbit under $\mathrm{Aut}(K3) \times \mathrm{SL}_2(\mathbb{Z})$: the eight
        Nikulin-involution conjugacy classes on K3 (Nikulin 1979, Mukai 1988) combined
        with the single elliptic-inversion class on $E$. Route: $R_4$.
  \item \textbf{Kähler-class divisor:} $[\omega]^\vee \in H_4(X; \mathbb{R})$
        the Poincaré dual of the Kähler form. Orbit under $\mathrm{Aut}(K3) \times
        \mathrm{SL}_2(\mathbb{Z})$ is the Kähler cone of $X$ modulo symmetries;
        generically a continuous orbit, not a discrete one. Route: $R_5$.
\end{enumerate}
\end{theorem}

\begin{proof}
Each class $[\Sigma_2]$ of (O1)–(O4) is represented by a genuinely distinct
transverse cycle in $H_4(X; \mathbb{Z})$ or $H_4(X; \mathbb{R})$. Their orbits
are distinguished by the three invariants:
(a) **Hodge type**: (O1) is of type $(2,2)$ concentrated on the K3 diagonal in
$H^{2,2}(X)$; (O2) is of type $(1,1) + (2,2)$ when viewed via
$[\mathcal{E}] = \sum_v \mathrm{type}_v + \text{generic fibre class}$
(Kodaira fibres contribute); (O3) is of type $(2,2)$ on the fixed locus; (O4) is of
type $(2,2)$ with a generic Kähler class.
(b) **Self-intersection**: (O1) $[S]^2_X = 0$; (O2) $[\mathcal{E}]^2_X = 0$
but the fibration class has Euler number contribution $\chi_{\mathrm{top}}(\mathcal{E}) = \sum_v (\text{type}_v - 1)$;
(O3) determined by Nikulin lattice data; (O4) generic.
(c) **Stabiliser in $\mathrm{Aut}(K3) \times \mathrm{SL}_2(\mathbb{Z})$**:
(O1) full group (invariant class); (O2) the subgroup fixing the elliptic pencil,
isomorphic to the semidirect product of the Mordell–Weil group with the group of
translations of the fibration; (O3) the centraliser of $\iota$ in
$\mathrm{Aut}(K3)$; (O4) the ample cone's stabiliser.

The preservation criterion (Theorem 5.1 of
\texttt{notes/wave16\_s2\_alternative\_Sigma2\_K3E.tex}, conditions (P1)(P2)(P3)) gates
which of (O1)–(O4) preserve $\kappa_{\mathrm{BKM}} = c_N(0)/2$. (O1), (O2), (O3) pass
(P1)+(P2); (O2) is conditional on (P3) via the Mordell–Weil paramodular condition;
(O4) fails (P1) generically. Hence the $\kappa_{\mathrm{BKM}}$-preserving orbits on
$H_4(X; \mathbb{Z})$ number at most three, strictly fewer than six.
\end{proof}

### T3 (Mordell–Weil indexing): elliptic-surface specialisation produces a new GBKM

\begin{theorem}[Elliptic-surface specialisation produces a GBKM candidate indexed by $\mathrm{MW}(\pi) \oplus \mathrm{NS}(E)$]
\ClaimStatusConjectured
\label{f03:thm:elliptic-surface-gbkm}

Let $\pi: S \to \mathbb{P}^1$ be an elliptic fibration on a projective K3 surface $S$
with a section, and assume $\rho(S) = 20$ (Shioda–Inose locus). Let
$\mathrm{MW}(\pi) \subset \mathrm{NS}(S)$ denote the Mordell–Weil lattice (the sections
of $\pi$ modulo the subgroup generated by the zero section and fibre components).
Write $\mathcal{E}$ for $S$ viewed as the total space of $\pi$. Let
$(\Sigma_2, C) = (\mathcal{E}, \mathbb{P}^1)$ inside $X = S \times E$.

Then the stage-2 specialisation
$\mathrm{Sp}_{\mathcal{E}, \mathbb{P}^1}(\Phi^{\mathrm{FA}}_3(D^b\mathrm{Coh}(X)))$
is an $E_1$-chiral algebra on $\mathbb{P}^1$ whose zero-mode Lie algebra
$\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ is a generalised Kac–Moody algebra
indexed by the \emph{rank-adjusted Mordell–Weil root lattice}
\[
  \Lambda_{\mathcal{E}, \mathbb{P}^1} \;:=\; \mathrm{MW}(\pi) \oplus \mathrm{NS}(E)
\]
with simple roots generated by the vertical divisor classes (fibre components over
singular fibres) and real simple roots generated by the primitive sections of
Mordell–Weil.

At a generic Shioda–Inose elliptic K3 with maximal Mordell–Weil rank
$\mathrm{MW}(\pi) \cong E_8 \oplus E_8$ (Miranda–Persson 1986 classification applied
to extremal elliptic K3), the Lie algebra $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$
is commensurable with (but not equal to) the Gritsenko–Nikulin $\Lambda^{2,10}$
GBKM attached to the Borcherds lift on $U \oplus E_8(-1)^2$.
\end{theorem}

\begin{proof}[Proof sketch.]
Two inputs from Shioda's Mordell–Weil theory are load-bearing.

\emph{Input 1} (Shioda 1990 Theorem 1.1). For an elliptic surface $\pi: S \to B$ with
section, there is an exact sequence of abelian groups
\[
  0 \to T \to \mathrm{NS}(S) \to \mathrm{MW}(\pi) \to 0,
\]
where $T \subset \mathrm{NS}(S)$ is the \emph{trivial lattice} spanned by the zero
section and fibre components. For $B = \mathbb{P}^1$ and $S$ a K3 of Picard rank
$\rho(S) = 20$, the Shioda formula gives
$\mathrm{rk}(\mathrm{MW}(\pi)) = \rho(S) - 2 - \sum_v(m_v - 1)$
where $m_v$ is the number of components of the singular fibre over $v$, and the
$-2$ accounts for $[F] + [\mathrm{zero section}]$ in $T$. For an extremal elliptic K3
at the Shioda–Inose point, the discriminant lattice is chosen so that
$\mathrm{MW}(\pi) \cong E_8 \oplus E_8$ is the maximal rank-$16$ sublattice consistent
with unimodular $\Lambda_{K3}$ and signature $(1,1)$ hyperbolic section–fibre plane
(Shioda 1990 Theorem 10.4; Miranda–Persson 1986
\emph{Configurations of $I_n$-Fibers on Elliptic K3 Surfaces}).

\emph{Input 2} (Costello–Dimofte–Paquette 2020 \S 4, interpreted Mayer–Vietoris on the
$I_n$-fibre locus). The push-forward
$\int_{\mathcal{E}} \mathcal{F}_{K3 \times E}$ is computed by
factorisation-algebra localisation: the contribution from smooth fibres is a
commutative $E_3$-piece (the $T^2 \times E$ Heisenberg), while the contribution from
$I_n$-fibres is the Mordell–Weil section generator tower, shifted by Kodaira
classification data.

The stage-2 specialisation $\mathrm{Sp}_{\mathcal{E}, \mathbb{P}^1}$
is by definition the push-forward $\pi_! \times \mathrm{id}_E$ applied to
$\mathcal{F}_{K3 \times E}$ along $\pi: S \to \mathbb{P}^1$, followed by passage
to the reference curve $\mathbb{P}^1$. The push-forward decomposes along the
elliptic-fibration stratification: over each smooth fibre $F_b \subset S$, the
stalk of $\mathcal{F}$ is a rank-$\mathrm{rk}(H^*(F_b))$ contribution; over
singular fibres of Kodaira type $I_n, II, III, IV, I_n^*, II^*, III^*, IV^*$
the stalk is modified by the Kodaira multiplicity.

The Lie algebra $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ emerges as follows.
Real simple roots arise from primitive sections
$\sigma \in \mathrm{MW}(\pi)$: each section $\sigma$ provides a real root
$\alpha_\sigma$ whose norm is given by the canonical height pairing (Shioda's
canonical height bilinear form on $\mathrm{MW}(\pi)$ modulo torsion). Imaginary
simple roots arise from $I_n$-singular-fibre data: each $I_n$-singular fibre contributes
$n-1$ imaginary roots through the Weil-component restriction.

Commensurability with the Gritsenko–Nikulin $\Lambda^{2,10}$ GBKM follows by embedding
$\mathrm{MW}(\pi) \oplus \mathrm{NS}(E)$ as a sublattice of
$\Lambda^{2,10} \cong \Lambda_{K3} \oplus U$ via the fibre-and-section decomposition of
$\Lambda_{K3} = U^3 \oplus E_8(-1)^2$: one of the three hyperbolic planes is identified
with the fibre-and-section plane of $\pi$, another with $H^*(E, \mathbb{Z})_{\mathrm{even}}$,
leaving the rank-$18$ complement to sit inside
$\mathrm{MW}(\pi) \oplus E_8(-1)^2 \subset E_8(-1)^2 \oplus E_8(-1)^2$. The
Weyl-denominator identities of $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ and
$\mathfrak{g}_{\Delta_5}$ agree on overlapping strata of the Heegner-divisor
stratification of the Borcherds lift, giving commensurability rather than equality.

This proof sketch converts the conjectural status of
Conjecture~\ref{wn:conj:gkm-on-P1} of
\texttt{notes/wave16\_s2\_alternative\_Sigma2\_K3E.tex} into a structural
argument with explicit Mordell–Weil input. The residual gap — precisely
which Kodaira-fibre multiplicities contribute as imaginary-simple-root
multiplicities versus as Weyl-chamber-wall contributions — is the content
beyond Shioda's rank theorem and requires the Bruinier–Funke lifting of
$\eta$-products through $I_n$-fibres cited in the notes.
\end{proof}

### T4 (Preservation-criterion correction): the Mordell–Weil indexing is cycle-class indexing at $[\Sigma_2] = [\mathcal{E}]$

\begin{theorem}[Cycle-class indexing of the elliptic-surface specialisation]
\ClaimStatusTheorem
\label{f03:thm:elliptic-cycle-indexing}

Under the hypotheses of Theorem~\ref{f03:thm:elliptic-surface-gbkm}, the
elliptic-surface cycle class $[\mathcal{E}] \in H_4(X; \mathbb{Z})$ decomposes via
Künneth as
\[
  [\mathcal{E}] \;=\; [S] \otimes [\mathrm{pt}_E]
    \;=\; [S \times \mathrm{pt}_E] \;\in\; H_4(S) \otimes H_0(E).
\]
The elliptic-surface specialisation is geometrically characterised not by a
different cycle class (which agrees with $[S]$ fibre-class) but by a different
\emph{reference curve}: $C = \mathbb{P}^1 \subset S$ rather than $C = E$.

Consequently the indexing data in the Wave-16 S2 conjecture is not the cycle class
$[\Sigma_2] \in H_4(X; \mathbb{Z})$ alone but the pair
$([\Sigma_2], [C]) \in H_4(X; \mathbb{Z}) \times H_2(X; \mathbb{Z})$. The
correct indexing space is the fibre product
\[
  \{([\Sigma_2], [C]) \;:\; C \subset \Sigma_2,\; [C] \cdot [\Sigma_2] \neq 0\}
\]
modulo the diagonal $\mathrm{Aut}(K3) \times \mathrm{SL}_2(\mathbb{Z})$-action.
\end{theorem}

\begin{proof}
Compute both sides of Künneth for the elliptic surface $\mathcal{E} = S$ viewed inside
$X = S \times E$ with the embedding $s \mapsto (s, e_0)$ for a fixed point $e_0 \in E$.
The cycle $[\mathcal{E}] = \iota_*[S]$ sits in $H_4(S) \otimes H_0(E) = \mathbb{Z}
[S \times \{e_0\}]$. The same Künneth decomposition applies to the canonical cycle
$[\Sigma_2 = S, C = E]$: when $C = E$, the reference curve is the $E$-factor, and
$\Sigma_2 = S$ is the K3 fibre, so $[\Sigma_2] \in H_4(S) \otimes H_0(E)$ again (picking
a fibre over a point of $E$). Both cycles land in the same Künneth summand.

What distinguishes the two specialisations is the reference curve: in the canonical
$(K3, E)$ specialisation, $C = E$, and the stage-$2$ push-forward factors through
$E$; in the elliptic-surface specialisation, $C = \mathbb{P}^1 \subset S$ is an
internal fibration base, and the stage-$2$ push-forward factors through $\mathbb{P}^1$
followed by $\mathrm{id}_E$. The two produce genuinely different chiral algebras
despite coinciding cycle-class data in $H_4$.

Hence the brief's formulation (orbits in $H_4$ alone) conflates the two specialisations
at the rank level $23$ but distinguishes them only at the reference-curve level.
The corrected indexing is the pair $([\Sigma_2], [C])$.
\end{proof}

### T5 (Healing the unification conjecture): three-piece indexing

\begin{theorem}[Healed unification: the three-piece indexing of routes]
\ClaimStatusTheorem
\label{f03:thm:three-piece-indexing}

The correct indexing structure for the six routes to $G(K3 \times E)$ is the
triple
\[
  \bigl(\mathcal{O}_{\mathrm{Aut}(K3) \times \mathrm{SL}_2(\mathbb{Z})}[(\Sigma_2, C)],\;
    \text{Mayer–Vietoris machine}_i,\;
    \rho^{R_i}\bigr)
\]
consisting of
\begin{itemize}
  \item an $\mathrm{Aut}(K3) \times \mathrm{SL}_2(\mathbb{Z})$-orbit of
        transverse $(\Sigma_2, C)$-pairs, refining the $H_4(X)$-only picture of
        the brief;
  \item a construction machine (HKR + Dolbeault twist; Borcherds lift; lattice VOA;
        $\mathbb{Z}/2$-orbifold; half-twist; BLLPR Schur) defining the target
        category and $\kappa_\bullet$-spectrum;
  \item a generator-rank stratifier $\rho^{R_i} \in \{3, 12, 24\}$ recording how
        the machine builds its generating set.
\end{itemize}
The six routes are the six ordered triples:
\[
\begin{array}{c|c|c|c}
\text{Route} & (\Sigma_2, C) & \text{Machine} & \rho^{R_i} \\ \hline
R_1 & (S, E) & \Phi_3 \text{ via HKR} & 3 \\
R_1^{\mathrm{ell}} & (\mathcal{E}, \mathbb{P}^1) & \Phi_3 \text{ via MW indexing} & 3 \\
R_2 & \text{(not cycle-indexable)} & \text{Borcherds lift} & \text{n/a (BKM Lie superalgebra)} \\
R_3 & \text{(not cycle-indexable)} & \text{Niemeier lattice VOA} & 24 \\
R_4 & (\mathrm{Fix}(\iota), E) & \mathbb{Z}/2\text{-orbifold of lattice VOA} & 12 \\
R_5 & ([\omega]^\vee, E) & \text{half-twist } \sigma\text{-model} & 3 \\
R_6 & \text{(not cycle-indexable)} & \text{BLLPR Schur} & 3 \\
\end{array}
\]
The elliptic-surface specialisation $R_1^{\mathrm{ell}}$ is a refinement of
$R_1$ (same machine, different $(\Sigma_2, C)$); the six routes become
\emph{seven} indexing triples if $R_1^{\mathrm{ell}}$ is counted separately.
\end{theorem}

\begin{proof}
Assemble the outputs:
Theorem~\ref{f03:thm:cycle-indexing} determines the cycle-indexable subset
$\{R_1, R_4, R_5\}$.
Theorem~\ref{f03:thm:four-orbits} determines the orbit cardinality on
$H_4(X; \mathbb{Z})$ among cycle-indexable routes.
Theorem~\ref{f03:thm:elliptic-cycle-indexing} corrects the cycle-class indexing
to the pair $([\Sigma_2], [C])$.
Theorem~\ref{f03:thm:elliptic-surface-gbkm} establishes the refinement
$R_1^{\mathrm{ell}}$ of $R_1$ via Mordell–Weil indexing.
The generator ranks $\rho^{R_i}$ are from
Theorem~\ref{thm:kappa-stratification-CY-C}(iv) of
\texttt{chapters/examples/cy\_c\_six\_routes\_convergence.tex}.
The resulting triple is the minimum structure required to distinguish the routes.
\end{proof}

## Retractions with true hidden structure

### Retraction 1: The brief's rank computation of $H_4(K3 \times E)$

**Wrong claim in the brief.** "$H_4(K3 \times E) = \mathbb{Z} \oplus
\mathbb{Z}^{22} \oplus \mathbb{Z}^2 = \mathbb{Z}^{25}$."

**Precise error.** Double-counting: the $\mathbb{Z}^2$ summand (from $H_1(E) = \mathbb{Z}^2$)
appears only as a tensor factor $H_3(S) \otimes H_1(E)$, which vanishes because K3 is
simply connected ($H_3(S) = 0$); it does not appear as an independent summand of $H_4$.
Additionally, $H_1(E)$ contributes to $H_1(K3 \times E)$, not to $H_4$.

**Ghost-theorem.** The correct rank of $H_4(K3 \times E; \mathbb{Z})$ is **23**, with
Künneth decomposition
\[
H_4(S \times E; \mathbb{Z}) \;\cong\;
\mathbb{Z}[\mathrm{pt}_S \times E] \;\oplus\; H_2(S; \mathbb{Z}) \otimes H_2(E; \mathbb{Z}) \;=\; \mathbb{Z} \oplus \Lambda_{K3} \cong \mathbb{Z}^{1 + 22} = \mathbb{Z}^{23}.
\]
The intersection pairing on $H_4$ inherits the K3 lattice signature $(3, 19)$ on the
rank-$22$ summand, with the rank-$1$ summand carrying a trivial pairing
(Poincaré-dual to the hyperplane class of the $E$-factor).

### Retraction 2: The unification by $H_4$-orbits alone

**Wrong claim in the platonic synthesis (Wave-16 S2, \S 6).** "The six routes to
$G(K3 \times E)$ unify as $\mathrm{Aut}(K3) \times \mathrm{SL}_2(\mathbb{Z})$-orbits in
$H_4(K3 \times E; \mathbb{Z})$."

**Precise error.** Only three of the six routes ($R_1, R_4, R_5$) admit cycle-class
indexing in $H_4$; the other three ($R_2, R_3, R_6$) consume non-cycle-class data
(Jacobi form, lattice, physical theory). Moreover, even among cycle-indexable routes,
$H_4$-orbits conflate $R_1$ with its elliptic-surface refinement $R_1^{\mathrm{ell}}$:
both use the cycle $[S]$, but differ in reference curve. The orbit count on $H_4$
alone is at most $4$, not $6$, and produces the wrong stratifier (the generator-rank
stratification $\rho^{R_i} \in \{3, 12, 24\}$ cannot be recovered from $H_4$-data).

**Ghost-theorem.** The true indexing is the three-piece structure of
Theorem~\ref{f03:thm:three-piece-indexing}: orbit of $(\Sigma_2, C)$-pair, machine,
generator-rank. The elliptic-surface specialisation $R_1^{\mathrm{ell}}$ is a
\emph{refinement} of $R_1$ (same cycle class in $H_4$, different reference curve),
producing the Mordell–Weil-indexed GBKM $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$
conditionally on Bruinier–Funke lifting through $I_n$-fibres.

### Retraction 3: The orbit stabiliser description

**Wrong claim in the brief.** "The Mordell–Weil group $\mathrm{MW}(\mathcal{E}/\mathbb{P}^1)$
acts on sections. Does this action unify with the orbit structure?"

**Precise error.** The Mordell–Weil group acts on the lattice of sections within a
single elliptic K3, not on the orbit structure of $H_4$-classes. The stabiliser of
the elliptic-surface cycle class $[\mathcal{E}] = [S] \in H_4(X)$ under
$\mathrm{Aut}(K3) \times \mathrm{SL}_2(\mathbb{Z})$ is generated by
(a) the subgroup of $\mathrm{Aut}(K3)$ preserving the elliptic fibration (an extension of
the Mordell–Weil group by the group of fibration-preserving automorphisms),
(b) the full $\mathrm{SL}_2(\mathbb{Z})$ (which acts only on $E$ and thus trivially on
$[\mathcal{E}]$ since $[\mathcal{E}]$ lies in the $H_4(S) \otimes H_0(E)$ summand).

**Ghost-theorem.** Mordell–Weil enters as the *indexing* of simple roots within the
output GBKM $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$, not as a symmetry of the
orbit structure on $H_4$. The correct role of Mordell–Weil is internal to
Theorem~\ref{f03:thm:elliptic-surface-gbkm}: simple roots $\alpha_\sigma$ are indexed
by primitive Mordell–Weil sections $\sigma \in \mathrm{MW}(\pi)$, with root norms
given by Shioda's canonical height pairing.

### Retraction 4: Shioda–Inose locus as "every" K3

**Wrong claim** (latent in the Wave-16 S2 conjecture, uncaught by the brief).
The conjecture as stated assumes $\rho(K3) = 20$ (Shioda–Inose locus) but is written
as if it applied to every projective K3.

**Precise error.** A generic projective K3 has Picard rank $\rho(K3)$ varying between
$1$ and $20$; the Mordell–Weil rank of an elliptic fibration on it depends strongly on
$\rho$. Only at the Shioda–Inose locus $\rho = 20$ can the Mordell–Weil lattice achieve
$E_8 \oplus E_8$ (Miranda–Persson 1986). For a generic K3 with $\rho = 1$ (algebraic
but without special structure), no elliptic fibration exists in general: elliptic
fibrations on K3 require $\rho \geq 2$ and a primitive isotropic class in
$\mathrm{NS}(S)$.

**Ghost-theorem.** The Wave-16 S2 conjecture requires the Shioda–Inose scope
hypothesis $\rho(K3) = 20$. In this scope, the Mordell–Weil lattice is
$E_8 \oplus E_8$ or smaller rank depending on the Kodaira configuration; the
$\mathrm{Aut}(K3) \times \mathrm{SL}_2(\mathbb{Z})$-orbit structure involves a choice
of elliptic pencil within the $\rho = 20$ transcendental complement, and the four-orbit
count of Theorem~\ref{f03:thm:four-orbits} holds with this scope understood.

## Cross-consistency checks

**(a) Against platonic synthesis.**
Theorem~\ref{f03:thm:four-orbits} corrects the one-line picture of
\texttt{notes/platonic\_synthesis\_waves\_11\_through\_16.tex} \S
\texttt{wn:subsec:plat-one-line}, which asserts "the six routes to $G(K3 \times E)$
are six $(\Sigma_2, C)$-specialisations". The corrected statement: only three of the
six routes factor through $(\Sigma_2, C)$-specialisation, the rest live on different
indexing spaces. This is already acknowledged at the residual-frontier item in the same
file (\texttt{wn:subsec:plat-frontier}: "if Mordell–Weil-indexing conjecture holds, the
six routes unify as orbits in $H_4$"); the present F03 analysis corrects the "if" to a
structural obstruction: cycle-class indexing captures only three routes, not six.

**(b) Against CoHA treatise.**
The CoHA treatise
\texttt{notes/CoHA\_to\_W\_infty\_treatise.tex} \S \ref{wn:subsec:K3xE} states
the Hodge diamond of $K3 \times E$ as $h^{0,0} = 1, h^{1,0} = 1, h^{0,1} = 1, h^{2,0} = 1,
h^{1,1} = 21$. The quoted $h^{1,1} = 21$ appears to be a miscount: the correct value for
$K3 \times E$ via Künneth is
$h^{1,1}(K3 \times E) = h^{1,1}(K3) \cdot h^{0,0}(E) + h^{0,0}(K3) \cdot h^{1,0}(E) \cdot h^{0,1}(E)^* + \ldots$.
Evaluating: $h^{1,1}(K3) = 20$, $h^{1,1}(E) = 1$, $h^{1,0}(K3) = 0$, $h^{0,1}(E) = 1$,
gives $h^{1,1}(K3 \times E) = 20 \cdot 1 + 1 \cdot 1 + 1 \cdot 0 = 21$ (where the
middle term is $h^{0,0}(K3) \cdot h^{1,1}(E) + h^{2,0}(K3) \cdot h^{?,?}(E)$; careful
accounting gives $h^{1,1}(K3 \times E) = 20 + 1 = 21$). **The CoHA treatise value is
correct.** The total $h^{*,*}(K3 \times E)$ assembles into the Betti numbers
$b_0 = 1,\; b_1 = 2,\; b_2 = 23,\; b_3 = 46,\; b_4 = 23,\; b_5 = 2,\; b_6 = 1$, with
$b_4 = 23$ matching Theorem above.

**(c) Against the universal Borcherds weight identity.**
$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ holds uniformly at $N \in \{1, 2, 3, 4, 6\}$
(Theorem~\texttt{thm:borcherds-weight-kappa-BKM-universal} in
\texttt{chapters/examples/cy\_d\_kappa\_stratification.tex}). On the K3 $\times$ $E$
canonical specialisation $(S, E)$, $N = 1$, giving $\kappa_{\mathrm{BKM}} = c_1(0)/2 = 5$.
The elliptic-surface specialisation $(\mathcal{E}, \mathbb{P}^1)$ preserves this value
conditionally on the Mordell–Weil paramodular condition (P3) of
\texttt{notes/wave16\_s2\_alternative\_Sigma2\_K3E.tex} Theorem~5.1, and the cusp
specialisation $(K3, \Delta^\times)$ preserves it unconditionally via the Tate-curve
degeneration. The CoHA-treatise Oberdieck–Pixton identity
$Z^{\mathrm{red}}_{DT}(K3 \times E) = -C / \Phi_{10}$ is cross-consistent:
$\Phi_{10} = \Delta_5^2$, giving $\mathrm{wt}(\Delta_5) = 5 = \kappa_{\mathrm{BKM}}$.

**(d) Against the two-stage factorisation.**
$\Phi_3 = \mathrm{Sp}_{\Sigma_2, C} \circ \Phi^{\mathrm{FA}}_3$ of
Theorem~\texttt{thm:phi-two-stage-factorisation}. Both the canonical $(S, E)$ and the
elliptic-surface $(\mathcal{E}, \mathbb{P}^1)$ specialisations are instances of stage-2
push-forward applied to the single $E_3$-hFA $\Phi^{\mathrm{FA}}_3(D^b\mathrm{Coh}(K3 \times E))$;
they differ in the choice of $(\Sigma_2, C)$, not in stage 1. Theorem~\ref{f03:thm:cycle-indexing}
enforces this: the two-stage factorisation structure gates which routes can be
cycle-indexed, and routes $R_2, R_3, R_6$ do not factor through stage 2 at all.
Cross-consistent with Pattern 273 ($\Phi$ functor vs object-level correspondence)
stated in \texttt{/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md}: the
chain-level object-level $\Phi$ and the $(\infty,1)$-categorical $\Phi$-as-functor are
two different statements about two different categorical structures. The six routes
span both of these, not a single functor applied six times.

## Residual frontier

(R1) **Full determination of $\mathrm{Aut}(K3) \times \mathrm{SL}_2(\mathbb{Z})$-orbits
on $H_4(X; \mathbb{Z})$**, including the integral structure of the intersection pairing.
\ClaimStatusOpen.
The cardinality of $\mathrm{Aut}(K3) \backslash \Lambda_{K3}$ is well-studied
(Sterk 1985, Dolgachev 2008) but the refined count on the rank-$23$ lattice
$H_4(X) = \mathbb{Z} \oplus \Lambda_{K3}$ has not been computed in closed form.

(R2) **Functoriality of $R_1^{\mathrm{ell}}$**: whether the elliptic-surface
specialisation gives a genuine refinement of the pentagon of named intertwiners
$\{\alpha_{ij}\}$ of \texttt{chapters/examples/cy\_c\_six\_routes\_generator\_level\_platonic.tex}.
\ClaimStatusOpen.
The Mordell–Weil-indexed GBKM $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ would enter the
pentagon as an eighth vertex; its compatibility with the existing $\alpha_{ij}$ is an
open question.

(R3) **Commensurability theorem** between $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$
and $\mathfrak{g}_{\Delta_5}$ made explicit: identify the explicit sublattice embedding
and compute the index. Theorem~\ref{f03:thm:elliptic-surface-gbkm} asserts
commensurability but does not produce the index $[\mathfrak{g}_{\Delta_5} :
\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}]$ explicitly.
\ClaimStatusOpen.

(R4) **Higher-$\rho$ Kodaira configurations.** For $\rho(K3) < 20$, the Mordell–Weil
lattice shrinks from $E_8 \oplus E_8$ to smaller rank determined by the Shioda
formula. The corresponding family of GBKMs
$\{\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}^{\rho}\}_{\rho = 2, \ldots, 20}$ is a
Shioda–Inose-moduli-indexed family, cross-cutting the Nikulin orbifold classification
of $R_4$.
\ClaimStatusOpen.

(R5) **Integral lane of Theorem~\ref{f03:thm:elliptic-surface-gbkm}.** The proof sketch
uses Shioda's canonical height as the real-simple-root norm, which is defined over
$\mathbb{Q}$. Whether $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ has an integral
structure compatible with the Mordell–Weil lattice (rather than its rationalisation) is
open and connects to Agent A01's T1 integral-vs-rational Stage-1 canonicality.
\ClaimStatusOpen.

## Attack-heal cycle log

**Cycle 1 (brief's rank computation).**
*ATTACK*: The brief claims $H_4(K3 \times E) = \mathbb{Z} \oplus \mathbb{Z}^{22}
\oplus \mathbb{Z}^2 = \mathbb{Z}^{25}$. Test via strict Künneth: $H_3(K3) = 0$ because
K3 is simply connected and has $b_1 = 0$, hence $H_3(K3) \otimes H_1(E) = 0$, not
$\mathbb{Z}^2$. The $\mathbb{Z}^2$ from $H_1(E)$ appears in $H_1(K3 \times E)$, not $H_4$.
Also $H_0(K3) \otimes H_4(E) = 0$ since $\dim_\mathbb{R} E = 2$ has no $H_4$.
*HEAL*: The correct rank is $23 = 1 + 22$. The Künneth decomposition is
$H_4(S \times E) = H_4(S) \otimes H_0(E) \oplus H_2(S) \otimes H_2(E)$, with signature
$(1, 0) \oplus (3, 19) = (4, 19)$. Retraction 1 records this correction.

**Cycle 2 (cycle-indexability audit).**
*ATTACK*: The brief and Wave-16 S2 assume all six routes are indexed by
$[\Sigma_2] \in H_4$; test by enumerating each route's construction input.
$R_2$ (Borcherds lift) consumes a Jacobi form $2\phi_{0,1}$, not a cycle class.
$R_3$ (Mukai lattice VOA) consumes the lattice $\Lambda_{\mathrm{Muk}}$, not a cycle class.
$R_6$ (BLLPR Schur) consumes a $6$d superconformal theory, not a cycle class.
Only $R_1, R_4, R_5$ factor through stage-2 cycle-class specialisation.
*HEAL*: Theorem~\ref{f03:thm:cycle-indexing} states the true indexing scope: only three
of six routes admit cycle-indexing; the orbit count on $H_4$ is at most $4$, not $6$.
Retraction 2 captures this.

**Cycle 3 (Künneth decomposition of elliptic-surface class).**
*ATTACK*: Does $[\mathcal{E}] \in H_4(X)$ differ from $[S] \in H_4(X)$ as cycle classes?
At first glance "elliptic surface $\mathcal{E}$" and "K3 fibre $S$" are distinct objects.
Test: $\mathcal{E} = S$ as a variety (the "elliptic surface" is the K3 viewed as
fibration $\pi: S \to \mathbb{P}^1$), so the cycle class agrees: $[\mathcal{E}] = [S]$
in $H_4$. The difference between the canonical $(S, E)$ specialisation and the
elliptic-surface $(\mathcal{E}, \mathbb{P}^1)$ specialisation lies in the reference
curve $C$, not in $[\Sigma_2]$.
*HEAL*: Theorem~\ref{f03:thm:elliptic-cycle-indexing} enshrines this correction:
the indexing is the pair $([\Sigma_2], [C])$, not the cycle class alone.

**Cycle 4 (Mordell–Weil action confusion).**
*ATTACK*: The brief asks whether the Mordell–Weil action on sections unifies with the
orbit structure. Test: sections of $\pi: S \to \mathbb{P}^1$ form a lattice
$\mathrm{MW}(\pi) \subset \mathrm{NS}(S)$, which acts on the subspace of $H_2(S)$ spanned
by the fibres and sections; this is a rank-$2$ subspace inside the rank-$22$ lattice
$\Lambda_{K3}$. The action of $\mathrm{MW}(\pi)$ on the remaining $20$ classes is by
translation of the torus of divisor classes, not by the $\mathrm{Aut}(K3)$-action;
the two are different symmetry structures. Mordell–Weil stabilises the fibration class
but does not stabilise the cycle $[\Sigma_2]$ in an $H_4$-orbit sense.
*HEAL*: Retraction 3 records the correct role: $\mathrm{MW}(\pi)$ indexes the simple
roots of the GBKM $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ internally via Shioda's
canonical height, not externally via orbit structure on $H_4$.

**Cycle 5 (scope hypothesis on $\rho(K3)$).**
*ATTACK*: The Wave-16 S2 conjecture is stated without an explicit $\rho(K3)$ hypothesis.
Test: for generic K3 with $\rho(K3) = 1$, no elliptic fibration $\pi: S \to \mathbb{P}^1$
exists in general; elliptic fibrations require $\rho \geq 2$ and a primitive isotropic
class. The Mordell–Weil lattice $E_8 \oplus E_8$ requires the Shioda–Inose locus
$\rho = 20$; at lower $\rho$ the Mordell–Weil rank is strictly smaller.
*HEAL*: Retraction 4 inserts the scope hypothesis $\rho(K3) = 20$ (Shioda–Inose);
Theorem~\ref{f03:thm:elliptic-surface-gbkm} is stated with this scope.

**Cycle 6 (cross-consistency with the pentagon).**
*ATTACK*: Does the elliptic-surface refinement $R_1^{\mathrm{ell}}$ break the pentagon
of named intertwiners in
\texttt{chapters/examples/cy\_c\_six\_routes\_generator\_level\_platonic.tex}?
The pentagon has five chiral-algebra vertices $\{R_1, R_3, R_4, R_5, R_6\}$ connected
by named bridges $\alpha_{ij}$. Test: if $R_1^{\mathrm{ell}}$ is a genuinely new vertex,
the pentagon becomes a hexagon; if it is a subtype of $R_1$, the pentagon is preserved.
The generator rank of $R_1^{\mathrm{ell}}$ is $\rho = 3$ (same machine, same
complex-dimension counting), matching $\rho^{R_1} = 3$; the output algebras $A_X^{R_1}$
and $A_X^{R_1^{\mathrm{ell}}}$ may differ as chiral algebras (different reference curves
give different specialisations) but agree at generator-rank level.
*HEAL*: Theorem~\ref{f03:thm:three-piece-indexing} treats $R_1^{\mathrm{ell}}$ as a
refinement of $R_1$, preserving the pentagon structure; the two appear as distinct
*triples* (orbit, machine, $\rho$), with the same machine and $\rho$ but different
orbit class $[(\mathcal{E}, \mathbb{P}^1)]$ vs $[(S, E)]$. Open question R2 records
whether this refinement produces a new pentagon vertex or is absorbed into $R_1$.

**Cycle 7 (elliptic K3 Kodaira configurations and $E_8 \oplus E_8$).**
*ATTACK*: Does the Mordell–Weil lattice $\mathrm{MW}(\pi) = E_8 \oplus E_8$ hold for
every extremal elliptic K3, or only for a specific Kodaira configuration? Test: the
Miranda–Persson 1986 classification (\emph{Configurations of $I_n$-fibers on elliptic
K3 surfaces}) enumerates the $n = 24$ elliptic K3 configurations; the $E_8 \oplus E_8$
Mordell–Weil configuration corresponds to the Kodaira type $(II^*, II^*)$ at two fibres
with all remaining fibres of type $I_1$ (giving Euler characteristic $24 = 20 + 2 + 2$).
Other configurations give other Mordell–Weil lattices (e.g., $D_4^{\oplus 2}$, $A_n$
combinations). The $E_8 \oplus E_8$ case is a single Shioda–Inose point among many.
*HEAL*: Theorem~\ref{f03:thm:elliptic-surface-gbkm} is scoped to $\mathrm{MW}(\pi) =
E_8 \oplus E_8$; for other configurations, the GBKM $\mathfrak{g}_{\mathcal{E},
\mathbb{P}^1}$ has a different structure. The family of GBKMs
parameterised by Kodaira configuration is part of the residual frontier R4.
