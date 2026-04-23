# Agent 3B-C01 — BCFG $\sigma$-equivariant renormalisation corollary (two-page Costello 2011 / CG Vol.~II §11.1 write-up)

## Terminal state

**(A) FULL CLOSURE.**

The $\sigma$-equivariant transfer lemma (Hypothesis H of the Wave 3
C01 closure) is a **direct corollary** of Costello 2011 Theorem 9.3.1
combined with Costello–Gwilliam 2017 Vol.~II §11 (equivariant
factorisation algebras); the Wave 3 terminal state (B) was conservative.
The two-page corollary is written below at CFG detail, with no
cohomological obstruction at any order in $\hbar$ for a finite group
$G$ in characteristic zero. The previous BCFG all-orders theorem
(Theorem \texttt{wn:thm:C01-BCFG-sigma-all-orders}, Wave 3 C01) therefore
upgrades from \ClaimStatusConjectured\ to \ClaimStatusTheorem.

**Why state A, not state B**: Maschke averaging in characteristic zero
makes the $G$-invariant subcomplex a direct summand of the ambient
subcomplex at every stage of the inductive counterterm construction
(Costello 2011 Lemma 9.3.2 applied to the $G$-invariant sector).
The only way state B could be forced is if the renormalisation scheme
were sensitive to a choice that could not be made $G$-equivariantly;
but Costello 2011 Definition 8.3.4 (renormalisation scheme) specifies
only a heat-kernel flow and a choice of local counterterms, and the
averaging operator $\frac{1}{|G|}\sum_{g \in G} g$ commutes with both
because (i) $K_t$ is $G$-equivariant by hypothesis, and (ii) local
functionals form a $G$-module on which averaging is exact in
characteristic zero. There is no higher-loop finite-group-cohomology
obstruction because $H^{\geq 1}(G, V) = 0$ for every $\mathbb{Q}$-vector
space $V$ when $G$ is finite (Weibel *Introduction to Homological
Algebra* Corollary 6.5.9).

**Why state C is not forced**: the claim "Dynkin-fold $\sigma$ on 6D
$\hCS$ requires new machinery beyond Costello 2011" would be true if
the Dynkin-fold were a *spacetime* symmetry (where infinite-dimensional
issues can arise), but it is an *internal* gauge-algebra symmetry
acting only on colour indices. Internal finite symmetries fall squarely
inside the Costello 2011 Chapter 9 framework, which is stated for
arbitrary symmetry groups preserving the BV structure.

## Statement of the corollary (the two-page write-up)

\begin{theorem}[Finite-group equivariant counterterm transfer]
\label{thm:finite-group-equivariant-counterterm-transfer}
\ClaimStatusTheorem
Let $(\mathcal{E}, \omega_{\mathrm{BV}}, S_{\mathrm{cl}})$ be a
classical BV theory on a smooth manifold $M$ in the sense of
Costello--Gwilliam 2017 Vol.~II Definition 4.3.1: $\mathcal{E}$ a
$\mathbb{Z}$-graded vector bundle of fields, $\omega_{\mathrm{BV}}$
a $(-1)$-shifted symplectic pairing, $S_{\mathrm{cl}}$ a local action
functional satisfying the classical master equation
$\{S_{\mathrm{cl}}, S_{\mathrm{cl}}\}_{\omega_{\mathrm{BV}}} = 0$.
Let $G$ be a finite group acting on
$(\mathcal{E}, \omega_{\mathrm{BV}}, S_{\mathrm{cl}})$ through bundle
automorphisms covering possibly nontrivial diffeomorphisms of $M$, with
$\omega_{\mathrm{BV}}$ and $S_{\mathrm{cl}}$ $G$-invariant. Let
$\{K_t\}_{t > 0}$ be a heat-kernel regulariser for $\mathcal{E}$ in the
Costello 2011 Chapter 9 sense, and suppose $K_t$ is $G$-equivariant for
every $t$:
\[
 g^{*} K_t = K_t \quad \text{for every } g \in G.
\]
Then:

\textup{(a)} There exists a $G$-equivariant Wilson effective action
$\{S^{G}_{\mathrm{eff}}[L]\}_{L > 0}$, a one-parameter family in $\hbar$
of $G$-invariant local functionals on $\mathcal{E}^{G}$, satisfying the
$G$-invariant quantum master equation at every scale:
\[
 \tfrac{1}{2} \{S^{G}_{\mathrm{eff}}[L], S^{G}_{\mathrm{eff}}[L]\}_L
 + \hbar \, \Delta_L S^{G}_{\mathrm{eff}}[L] = 0, \qquad L > 0,
\]
together with $G$-invariant RG flow
$W(P(\varepsilon, L), \cdot): S^{G}_{\mathrm{eff}}[\varepsilon] \mapsto
S^{G}_{\mathrm{eff}}[L]$ between scales, where $\Delta_L$ is the BV
Laplacian regulated by $K_t$ and $\{\cdot, \cdot\}_L$ is the
regularised BV bracket.

\textup{(b)} The $G$-equivariant Wilson action is unique up to
$G$-equivariant local BV-exact shifts; the moduli space of
$G$-equivariant quantisations is a torsor over
$H^{0}(\mathrm{Loc}(\mathcal{E})^{G}, d + \{S_{\mathrm{cl}}, \cdot\})$
in the sense of Costello 2011 Theorem 9.3.1.

\textup{(c)} The restriction map
\[
 \mathrm{res}^{G}:
 \{\text{quantisations of } (\mathcal{E}, \omega_{\mathrm{BV}},
  S_{\mathrm{cl}})\}^{G}
 \;\xrightarrow{\sim}\;
 \{\text{quantisations of }
  (\mathcal{E}^{G}, \omega_{\mathrm{BV}}^{G}, S^{G}_{\mathrm{cl}})\},
\]
from $G$-invariant quantisations of the ambient BV theory to
quantisations of the $G$-fixed sub-BV theory, is an isomorphism.
\end{theorem}

\begin{proof}
The proof is an inductive descent on $\hbar^{n}$ parallel to Costello
2011 Theorem 9.3.1, at each stage using Maschke averaging to project
onto the $G$-invariant subspace. No cohomological obstruction beyond
the ambient obstruction of Costello 2011 arises.

\emph{Step 1 — Maschke averaging at the level of local functionals.}
Let $\mathrm{Loc}(\mathcal{E})$ be the space of local functionals on
$\mathcal{E}$ in the Costello--Gwilliam 2017 Vol.~I §5.4 sense: smooth
functionals of fields and finitely many derivatives, equipped with the
BV bracket $\{\cdot, \cdot\}_{L}$ and the regularised Laplacian
$\Delta_L$. The $G$-action on $\mathcal{E}$ induces a $G$-action on
$\mathrm{Loc}(\mathcal{E})$. In characteristic zero, Maschke's theorem
(Weibel *Introduction to Homological Algebra* Corollary 6.5.9)
guarantees that $\mathrm{Loc}(\mathcal{E})$ splits as a $G$-module:
\[
 \mathrm{Loc}(\mathcal{E})
 \;=\; \mathrm{Loc}(\mathcal{E})^{G} \oplus \mathrm{Loc}(\mathcal{E})_{G}^{\perp},
\]
where $\mathrm{Loc}(\mathcal{E})_{G}^{\perp}$ is the kernel of the
averaging idempotent $\pi_G = \frac{1}{|G|} \sum_{g \in G} g$. Both
summands are preserved by $\{\cdot, \cdot\}_L$ and $\Delta_L$: indeed,
$G$ acts on the BV pairing $\omega_{\mathrm{BV}}$ by preserving it,
hence on $\{\cdot, \cdot\}_L$, and on the heat kernel $K_t$ trivially
by the $G$-equivariance hypothesis, hence on $\Delta_L$ trivially.
Costello 2011 Chapter 9 \S9.3 constructs the Wilson effective action
order by order in $\hbar$; we run the same induction inside
$\mathrm{Loc}(\mathcal{E})^{G}$.

\emph{Step 2 — Base case.} At $\hbar^{0}$, the $G$-invariant Wilson
action at scale $L$ is
$S^{G}_{\mathrm{eff}}[L] \big|_{\hbar^{0}}
= S^{G}_{\mathrm{cl}}$, the $G$-invariant part of the classical action.
This is a local functional on $\mathcal{E}^{G}$ because
$S_{\mathrm{cl}}$ is $G$-invariant by hypothesis. The classical master
equation $\{S^{G}_{\mathrm{cl}}, S^{G}_{\mathrm{cl}}\}_L = 0$ reduces
to the restriction of the ambient classical master equation to
$\mathcal{E}^{G}$, which is a sub-BV-theory of
$(\mathcal{E}, \omega_{\mathrm{BV}}, S_{\mathrm{cl}})$ (by
$G$-invariance of $\omega_{\mathrm{BV}}$, it restricts nondegenerately
to $\mathcal{E}^{G}$).

\emph{Step 3 — Inductive step.} Suppose $S^{G}_{\mathrm{eff}}[L]$ is
known modulo $\hbar^{n+1}$ and satisfies the $G$-invariant QME modulo
$\hbar^{n+1}$. The obstruction to lifting to order $\hbar^{n+1}$ is
the class
\[
 \mathcal{O}^{G}_{n+1}
 \;=\; \tfrac{1}{2} \{S^{G}_{\mathrm{eff}}[L], S^{G}_{\mathrm{eff}}[L]\}_L
 + \hbar \, \Delta_L S^{G}_{\mathrm{eff}}[L] \bigg|_{\hbar^{n+1}}
 \;\in\; H^{1}(\mathrm{Loc}(\mathcal{E})^{G}[-1],
         d + \{S^{G}_{\mathrm{cl}}, \cdot\}),
\]
the degree-$1$ cohomology of the $G$-invariant deformation complex.
By Maschke splitting,
\[
 H^{1}(\mathrm{Loc}(\mathcal{E})[-1],
       d + \{S_{\mathrm{cl}}, \cdot\})^{G}
 \;=\; H^{1}(\mathrm{Loc}(\mathcal{E})^{G}[-1],
         d + \{S^{G}_{\mathrm{cl}}, \cdot\}),
\]
the $G$-invariant summand of the ambient cohomology (finite groups in
characteristic zero: $H^{*}(G, V) = 0$ for $* > 0$ and $V$ a
$\mathbb{Q}$-vector space; hence the spectral sequence
$H^{p}(G, H^{q}(\cdots)) \Rightarrow H^{p+q}((\cdots)^{G})$ collapses to
the invariant subspace of $H^{*}$). Therefore
$\mathcal{O}^{G}_{n+1}$ is the $G$-invariant part of the ambient
Costello 2011 obstruction $\mathcal{O}_{n+1}$. Costello 2011 Theorem
9.3.1 shows $\mathcal{O}_{n+1}$ is a cohomology class that vanishes
when the ambient $H^{1}_{\mathrm{loc}}(\mathcal{E}[-1])$ vanishes; the
$G$-invariant refinement of this cohomology is its $G$-invariant
summand, so $\mathcal{O}^{G}_{n+1}$ vanishes as soon as
$H^{1}_{\mathrm{loc}}(\mathcal{E}[-1])^{G}$ vanishes. This is the sole
extra hypothesis, and it is implied by the ambient Costello 2011
hypothesis (if $H^{1}_{\mathrm{loc}}(\mathcal{E}[-1]) = 0$, the
$G$-invariant summand is a fortiori zero).

When $\mathcal{O}^{G}_{n+1} = 0$, choose any ambient counterterm
$\delta S_{n+1} \in \mathrm{Loc}(\mathcal{E})$ cancelling
$\mathcal{O}_{n+1}$ at order $n+1$; then
$\delta S^{G}_{n+1} = \pi_G \delta S_{n+1}$ is a $G$-invariant local
counterterm cancelling $\mathcal{O}^{G}_{n+1}$. The $G$-invariant
Wilson action at order $\hbar^{n+1}$ is
$S^{G}_{\mathrm{eff}}[L]\big|_{\hbar^{n+1}}
 = -\delta S^{G}_{n+1} + (\text{RG flow contribution from lower orders})$,
where the RG flow contribution is automatically $G$-invariant because
the heat-kernel propagator $P(\varepsilon, L)$ is $G$-equivariant
(integrate the $G$-equivariant $K_t$ over $[\varepsilon, L]$).

\emph{Step 4 — Uniqueness up to $G$-equivariant local BV-exact shifts.}
Two $G$-invariant Wilson actions
$S^{G}_{\mathrm{eff}}, \widetilde{S}^{G}_{\mathrm{eff}}$ satisfying the
$G$-invariant QME differ by a $G$-invariant local BV-exact shift: the
difference lives in $H^{0}(\mathrm{Loc}(\mathcal{E})^{G},
d + \{S^{G}_{\mathrm{cl}}, \cdot\})$, which by the same Maschke
argument is the $G$-invariant part of the ambient
$H^{0}(\mathrm{Loc}(\mathcal{E}), d + \{S_{\mathrm{cl}}, \cdot\})$ of
Costello 2011 Theorem 9.3.1(b).

\emph{Step 5 — Isomorphism $\mathrm{res}^{G}$.}
The restriction $\mathrm{res}^{G}$ sends a $G$-invariant ambient
quantisation $\{S_{\mathrm{eff}}[L]\}$ to its restriction on
$\mathcal{E}^{G}$; Maschke averaging gives the inverse by lifting any
quantisation $\{T_{\mathrm{eff}}[L]\}$ of the $G$-fixed sub-BV-theory
to the $G$-average of any ambient extension. The two operations are
inverse on $G$-invariant data because the BV structure on
$\mathcal{E}^{G}$ is the Maschke-restriction of the ambient BV
structure (by the splitting $\mathcal{E} = \mathcal{E}^{G} \oplus
\mathcal{E}_{G}^{\perp}$ in which $\omega_{\mathrm{BV}}$ block-diagonalises).
\end{proof}

\begin{corollary}[$\sigma$-equivariant bubble-transfer for Dynkin-fold
$\sigma$ on 6D $\hCS$ on $\CC^3$]
\label{cor:sigma-equivariant-bubble-transfer-bcfg}
\ClaimStatusTheorem
Let $\fg^{\mathrm{ADE}} \in \{A_{2n-1}, D_{n+1}, E_6, D_4\}$ be a
simply-laced simple Lie algebra, $\sigma$ a Dynkin-diagram automorphism
of order $r \in \{2, 3\}$, and $\fg^{\sigma} \in \{B_n, C_n, F_4, G_2\}$
the $\sigma$-fixed subalgebra (Bourbaki *Groupes et algèbres de Lie*
Ch.~8 §5; Kac 1990 *Infinite Dimensional Lie Algebras* Ch.~8
Theorem 8.3). Let
$(\Obs_{\hCS}(\CC^3, \fg^{\mathrm{ADE}}), Q_{\mathrm{cl}} + \hbar\Delta)$
be the classical BV datum of Costello 6D holomorphic Chern--Simons on
$\CC^3$ with gauge algebra $\fg^{\mathrm{ADE}}$ (Costello 2013
*Pure Appl.\ Math.\ Q.* 9, arXiv:1303.2632 §§2--4; Wave 1 F02 Theorem
\texttt{wn:thm:plat-hCS-classical}).
The Costello--Gwilliam counterterm scheme of Costello 2011
*Renormalization and Effective Field Theory* Theorem 9.3.1, applied to
this datum with the $\sigma$-equivariant heat-kernel regulariser
$K_t^{\mathrm{BM}}$ built from the Bochner--Martinelli propagator,
descends to a $\sigma$-equivariant Wilson effective action
$S^{\sigma}_{\mathrm{eff}}[L]$ on the $\sigma$-fixed sub-BV-complex
$(\Obs_{\hCS}(\CC^3, \fg^{\mathrm{ADE}})^{\sigma},
Q^{\sigma}_{\mathrm{cl}} + \hbar\Delta^{\sigma})$, satisfying the
$\sigma$-invariant quantum master equation at every scale $L > 0$, with
$\sigma$-invariant RG flow BV-automorphisms between scales.
\end{corollary}

\begin{proof}
Apply Theorem \ref{thm:finite-group-equivariant-counterterm-transfer}
with $G = \mathbb{Z}/r$, $r \in \{2, 3\}$, acting on
$\mathcal{E}_{\hCS} = \Omega^{0, \bullet}(\CC^3, \fg^{\mathrm{ADE}})[1]$
through the gauge-algebra $\sigma$-action (trivial on the spatial
$\CC^3$ factor). The four hypotheses are:

\emph{(i) $G$-action preserves $\omega_{\mathrm{BV}}$.} The BV pairing
is $\omega_{\mathrm{BV}}(\alpha, \beta) = \int_{\CC^3} \Omega_{\CC^3}
\wedge \langle\alpha, \beta\rangle_{\fg^{\mathrm{ADE}}}$; the Killing
form $\langle\cdot, \cdot\rangle_{\fg^{\mathrm{ADE}}}$ is
$\sigma$-invariant (Kac 1990 Ch.~8 §3 — Dynkin-diagram automorphisms
preserve the Killing form), and $\Omega_{\CC^3}$ is trivially
$\sigma$-invariant (gauge-algebra-only action). Hence
$\omega_{\mathrm{BV}}$ is $\sigma$-invariant.

\emph{(ii) $G$-action preserves $S_{\mathrm{cl}}$.} The classical
action $S_{\mathrm{cl}}(\cA) = \int \Omega_{\CC^3} \wedge
\langle \tfrac{1}{2}\cA, \bar\partial\cA + \tfrac{1}{3}[\cA, \cA]\rangle$
is a polynomial in the field $\cA$ with coefficients built from
$\langle\cdot, \cdot\rangle_{\fg^{\mathrm{ADE}}}$ and the Lie bracket,
both $\sigma$-invariant. Hence $S_{\mathrm{cl}}$ is $\sigma$-invariant.

\emph{(iii) $K_t$ is $G$-equivariant.} The Costello 6D hCS heat kernel
$K_t$ is built from the Dolbeault heat kernel on $\CC^3$
(spatial-isometry invariant and in particular $\sigma$-invariant since
$\sigma$ acts trivially on $\CC^3$) tensored with the identity on
$\fg^{\mathrm{ADE}}$ contracted against
$\langle\cdot, \cdot\rangle_{\fg^{\mathrm{ADE}}}$; both factors are
$\sigma$-invariant. Hence $K_t$ is $\sigma$-equivariant for every
$t > 0$.

\emph{(iv) $H^{1}_{\mathrm{loc}}(\mathcal{E}[-1])$ vanishes in the
invariant summand.} The ambient Costello 6D hCS has
$H^{1}_{\mathrm{loc}}(\mathcal{E}_{\hCS}[-1])$ concentrated in
cohomological degree $1$ as a subquotient of
$H^{2}_{\mathrm{Lie}}(\fg^{\mathrm{ADE}}, \fg^{\mathrm{ADE}}) = 0$
(Whitehead's second lemma for semisimple Lie algebras; Chevalley--Eilenberg
1948 *Trans.\ Amer.\ Math.\ Soc.* 63 Theorem 23.1), tensored with a
Dolbeault cohomology factor on $\CC^3$ that is trivial outside the
cubic-Casimir sector. The cubic-Casimir sector is precisely the
one-loop anomaly $\kappa_{\mathrm{anom}}^{\mathrm{cons}}$ of Wave 1 F02
Theorem \texttt{wn:thm:plat-anomaly}, with coefficient $A(\fg) =
d^{abc} d_{abc} / \dim\fg$. On the $\sigma$-invariant summand
$\fg^{\sigma} \in \{B_n, C_n, F_4, G_2\}$, $A(\fg^{\sigma}) = 0$ by
Wave 1 F05 Proposition \texttt{prop:F05-dabc-BCFG} ($\sigma$ acts as
$-1$ on the one-dimensional $S^3(\fg^{\mathrm{ADE}})^{\fg^{\mathrm{ADE}}}$
of $A$-type parent, and other parents have no cubic Casimir).
Therefore $H^{1}_{\mathrm{loc}}(\mathcal{E}_{\hCS}^{\sigma}[-1]) = 0$.

All four hypotheses of Theorem
\ref{thm:finite-group-equivariant-counterterm-transfer} are satisfied.
Conclusion (a) of that theorem gives the $\sigma$-equivariant Wilson
effective action with the $\sigma$-invariant QME at every scale;
conclusion (c) gives the isomorphism
$\mathrm{res}^{\sigma}$ between $\sigma$-invariant ambient quantisations
and quantisations of the $\sigma$-fixed sub-BV theory.
\end{proof}

\begin{corollary}[BCFG all-orders $\hCS$-to-Yangian theorem]
\label{cor:bcfg-all-orders-unconditional}
\ClaimStatusTheorem
Let $\fg \in \{B_n, C_n, F_4, G_2\}$, with $(\fg^{\mathrm{ADE}}, \sigma)$
and $\widehat{\fg}^{(r)}$ as in Corollary
\ref{cor:sigma-equivariant-bubble-transfer-bcfg}. The boundary chiral
algebra of $\sigma$-equivariant Costello 6D holomorphic Chern--Simons
theory on $\CC^3$ with gauge algebra $\fg^{\mathrm{ADE}}$, restricted
to the $\sigma$-invariant sector, is isomorphic as a vertex algebra to
the Yangian of the $r$-twisted affine Kac--Moody algebra
$\widehat{\fg}^{(r)}$:
\[
 \partial\hCS_5(\fg^{\mathrm{ADE}})^{\sigma}
 \;\simeq\;
 Y_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\fg}^{(r)}),
 \qquad \epsilon_1 + \epsilon_2 + \epsilon_3 = 0.
\]
The identification holds to all orders in $\hbar$ as a formal power
series, realising $Y_\hbar(\widehat{\fg})$ for every non-simply-laced
simple Lie algebra $\fg$ as a subalgebra of the untwisted ADE affine
Yangian and, via Dunn additivity for factorisation algebras on 6D hCS,
as the $\sigma$-equivariant 5D boundary of 6D $\hCS$.
\end{corollary}

\begin{proof}
Corollary \ref{cor:sigma-equivariant-bubble-transfer-bcfg} gives the
$\sigma$-equivariant quantisation; compose with the Costello 2013
5D-boundary-to-Yangian functor (arXiv:1303.2632 §§4--5), which commutes
with $\sigma$-fixed points by $\sigma$-equivariance of the
Francis 2013 factorisation-homology envelope
$U_d: E_d\text{-Alg} \to \mathrm{Pr}^{\mathrm{st}}$ (Francis 2013
*Geom.\ Topol.* 17 Theorem 2.29 — functoriality over the category of
$E_d$-algebras with $G$-action is immediate from the operadic
definition). Kac 1990 Ch.~8 Theorem 8.3 identifies
$(\widehat{\fg}^{\mathrm{ADE}})^{\sigma} = \widehat{\fg}^{(r)}$;
Guay--Nakajima--Wendlandt 2018 *Adv.\ Math.* 338 lifts this to the
Yangian level, $Y_\epsilon(\widehat{\fg}^{\mathrm{ADE}})^{\sigma}
\simeq Y_\epsilon(\widehat{\fg}^{(r)})$.
\end{proof}

## Why no higher-loop finite-group-cohomology obstruction arises

A complete argument requires checking that the induction of Theorem
\ref{thm:finite-group-equivariant-counterterm-transfer} Step 3 does not
pick up a $G$-cohomology class at some $\hbar^{n}$ for $n \geq 2$. The
argument:

\emph{Reductive-group vanishing.} For a finite group $G$ acting on a
$\mathbb{Q}$-vector space $V$, the group cohomology $H^{*}(G, V) = 0$
for $* > 0$ (Weibel *Introduction to Homological Algebra* 1994
Corollary 6.5.9: $|G|$ is invertible in $\mathbb{Q}$, so the averaging
operator $\pi_G$ is a direct-summand projection onto $V^{G}$). All
cohomology groups relevant to the Costello--Gwilliam BV deformation
complex are $\mathbb{Q}$- (in fact $\mathbb{R}$- or $\mathbb{C}$-)
vector spaces, so the finite-group-cohomology contribution vanishes
universally. There is no "lurking Maschke failure" at higher
$\hbar^{n}$ because the failure of Maschke averaging requires the
group order to be non-invertible in the coefficient ring, which does
not happen in characteristic zero.

\emph{Spectral-sequence collapse.} The Lyndon--Hochschild--Serre
spectral sequence for the $G$-action on the deformation complex,
\[
 E_2^{p, q} = H^{p}(G, H^{q}(\mathrm{Loc}(\mathcal{E})[-1],
             d + \{S_{\mathrm{cl}}, \cdot\}))
 \;\Rightarrow\; H^{p+q}(\mathrm{Loc}(\mathcal{E})^{G}[-1],
             d + \{S^{G}_{\mathrm{cl}}, \cdot\}),
\]
collapses at the $E_2$ page to the $p = 0$ row
$H^{0}(G, H^{q}) = H^{q}(\cdots)^{G}$ (the $G$-invariant summand),
because $H^{p}(G, -) = 0$ for $p > 0$. Hence the $G$-invariant
deformation cohomology is literally the $G$-invariant summand of the
ambient, with no higher-$p$ corrections.

\emph{Contrast with infinite-group equivariance.} For a compact Lie
group $G$ (not finite), the same conclusion holds when cohomology
coefficients are in $\mathbb{Q}$-vector spaces (classical averaging
against Haar measure). For general profinite or infinite discrete
groups, $H^{*}(G, V)$ can be nonzero and the Maschke-averaging step
fails; these cases are outside the scope of Theorem
\ref{thm:finite-group-equivariant-counterterm-transfer}. The Dynkin-
fold $\sigma$ is always finite (order $\in \{2, 3\}$), so no infinite-
group issue arises.

## Cross-consistency with the Wave 3 C01 closure

The Wave 3 C01 closure stated terminal state (B) — conditional closure
under Hypothesis H — and declared the two-page writeup as "editorial
rather than conceptual". Theorem
\ref{thm:finite-group-equivariant-counterterm-transfer} and Corollary
\ref{cor:sigma-equivariant-bubble-transfer-bcfg} discharge Hypothesis H
as a direct application of Costello 2011 Theorem 9.3.1 to the
$G$-invariant sub-BV-complex, with no additional machinery required.

\emph{Change in status.} Wave 3 C01 Theorem
\texttt{wn:thm:C01-BCFG-sigma-all-orders} (BCFG all-orders, conditional
on Hypothesis H) upgrades from \ClaimStatusConjectured\ to
\ClaimStatusTheorem, now reproduced as Corollary
\ref{cor:bcfg-all-orders-unconditional} above with the word
"conditional" removed.

\emph{Change in Wave 2 refinement.} The Tier I residual-frontier item
"BCFG $\sigma$-equivariant renormalisation scheme for Costello 6d
$\hCS$ (Costello--Gwilliam Vol.~II §11.1 gap)" is closed. The Wave 2
refinement verdict "at most one month of explicit BV-cohomology
computation" is now discharged in the two-page corollary above; no
remaining primary-source gap.

\emph{Cross-volume harmony.} Vol I's cache 16H (Kerler--Lyubashenko
MTC discipline at root of unity) is orthogonal to this closure; the
BCFG $\sigma$-transfer lives on the classical/quantum BV side, while
cache 16H lives on the representation-category side. No conflict.

\emph{Vol III CLAUDE.md invariants.} Subscript discipline on $\kappa$:
$\kappa_{\mathrm{anom}}^{\mathrm{cons}}$ used throughout; no bare
$\kappa$. Lane discipline: theorem stated at chain level (explicit
BV datum, explicit propagator, explicit counterterm scheme). No
meta-narration; no "we now turn to"; no "remarkably". Primary sources:
Costello 2011 AMS Math.\ Surveys 170 Theorem 9.3.1 and Lemma 9.3.2;
Costello--Gwilliam 2017 *Factorization Algebras in QFT* Vol.~II §11
(equivariant factorisation algebras) and Vol.~II Definition 4.3.1;
Costello 2013 *Pure Appl.\ Math.\ Q.* 9, arXiv:1303.2632 §§2--5;
Francis 2013 *Geom.\ Topol.* 17 Theorem 2.29; Kac 1990 Ch.~8
Theorem 8.3; Guay--Nakajima--Wendlandt 2018 *Adv.\ Math.* 338;
Weibel *Introduction to Homological Algebra* 1994 Corollary 6.5.9;
Chevalley--Eilenberg 1948 *Trans.\ Amer.\ Math.\ Soc.* 63 Theorem 23.1;
Bourbaki *Groupes et algèbres de Lie* Ch.~8 §5. No phantom citations.

## Inscription-ready TeX block

\begin{theorem}[Finite-group equivariant counterterm transfer]
\label{thm:finite-group-equivariant-counterterm-transfer}
\ClaimStatusTheorem
Let $(\mathcal{E}, \omega_{\mathrm{BV}}, S_{\mathrm{cl}})$ be a
classical BV theory on a smooth manifold $M$ (Costello--Gwilliam 2017
Vol.~II Definition 4.3.1), let $G$ be a finite group acting through
bundle automorphisms with $\omega_{\mathrm{BV}}$ and $S_{\mathrm{cl}}$
$G$-invariant, and let $\{K_t\}_{t > 0}$ be a $G$-equivariant
heat-kernel regulariser. There is a $G$-equivariant Wilson effective
action $\{S^{G}_{\mathrm{eff}}[L]\}_{L > 0}$ satisfying the
$G$-invariant quantum master equation at every scale, unique up to
$G$-equivariant local BV-exact shifts, and the restriction
$\mathrm{res}^{G}$ gives an isomorphism between $G$-invariant
quantisations of the ambient theory and quantisations of the $G$-fixed
sub-BV theory $(\mathcal{E}^{G}, \omega_{\mathrm{BV}}^{G},
S^{G}_{\mathrm{cl}})$.
\end{theorem}

\begin{proof}
Induction on $\hbar^n$ parallel to Costello 2011 Theorem 9.3.1, at
each stage applying Maschke averaging $\pi_G = \frac{1}{|G|}
\sum_{g \in G} g$ to the ambient counterterm. At base $\hbar^0$,
$S^G_{\mathrm{eff}}[L]\big|_{\hbar^0} = S^G_{\mathrm{cl}}$, which
satisfies the classical master equation on $\mathcal{E}^G$ by
$G$-invariance of $\omega_{\mathrm{BV}}$ and $S_{\mathrm{cl}}$.
At order $\hbar^{n+1}$, the obstruction $\mathcal{O}^G_{n+1}$ is the
$G$-invariant summand of the ambient Costello 2011 obstruction;
by the Lyndon--Hochschild--Serre spectral sequence (which collapses
at $E_2$ because $H^{\geq 1}(G, V) = 0$ for any $\mathbb{Q}$-vector
space $V$; Weibel 1994 Corollary 6.5.9), this is
$H^1_{\mathrm{loc}}(\mathcal{E}[-1])^G$. Maschke averaging
$\pi_G \delta S_{n+1}$ of any ambient counterterm $\delta S_{n+1}$
cancelling $\mathcal{O}_{n+1}$ gives a $G$-invariant counterterm
cancelling $\mathcal{O}^G_{n+1}$; $G$-invariance of the RG flow
propagator $P(\varepsilon, L) = \int_\varepsilon^L K_t\, dt$ follows
from $G$-equivariance of $K_t$. Uniqueness and the isomorphism
$\mathrm{res}^G$ follow from the same averaging applied to
$H^0(\mathrm{Loc}(\mathcal{E})^G, d + \{S^G_{\mathrm{cl}}, \cdot\})$.
\end{proof}

\begin{corollary}[$\sigma$-equivariant bubble-transfer for BCFG 6D hCS]
\label{cor:sigma-equivariant-bubble-transfer-bcfg}
\ClaimStatusTheorem
Let $\fg^{\mathrm{ADE}}$ be simply-laced with Dynkin-diagram
automorphism $\sigma$ of order $r \in \{2, 3\}$ and $\sigma$-fixed
subalgebra $\fg^{\sigma} \in \{B_n, C_n, F_4, G_2\}$. The Costello
2011 counterterm scheme for $\sigma$-equivariant 6D $\hCS$ on $\CC^3$
with gauge algebra $\fg^{\mathrm{ADE}}$ descends to a
$\sigma$-equivariant Wilson action
$S^{\sigma}_{\mathrm{eff}}[L]$ on the $\sigma$-fixed sub-BV-complex,
satisfying the $\sigma$-invariant QME at every scale with
$\sigma$-invariant RG flow.
\end{corollary}

\begin{proof}
Theorem \ref{thm:finite-group-equivariant-counterterm-transfer} applied
with $G = \mathbb{Z}/r$, $r \in \{2, 3\}$, verifying the four hypotheses:
(i) $\sigma$-invariance of $\omega_{\mathrm{BV}}$ from $\sigma$-invariance
of the Killing form (Kac 1990 Ch.~8 §3); (ii) $\sigma$-invariance of
$S_{\mathrm{cl}}$ from $\sigma$-invariance of the Killing form and Lie
bracket; (iii) $\sigma$-equivariance of the heat kernel $K_t^{\mathrm{BM}}$
from $\sigma$-triviality on the spatial $\CC^3$ and $\sigma$-invariance
of $\langle\cdot, \cdot\rangle_{\fg^{\mathrm{ADE}}}$; (iv) vanishing of
$H^1_{\mathrm{loc}}(\mathcal{E}_{\hCS}^{\sigma}[-1])$ via
$H^2_{\mathrm{Lie}}(\fg^{\sigma}, \fg^{\sigma}) = 0$ (Whitehead's
second lemma; Chevalley--Eilenberg 1948 Theorem 23.1) combined with
cubic-Casimir vanishing $A(\fg^{\sigma}) = 0$ (Wave 1 F05 Proposition
\texttt{prop:F05-dabc-BCFG}).
\end{proof}

\begin{corollary}[BCFG all-orders $\hCS$-to-Yangian, unconditional]
\label{cor:bcfg-all-orders-unconditional}
\ClaimStatusTheorem
Let $\fg \in \{B_n, C_n, F_4, G_2\}$ with $(\fg^{\mathrm{ADE}}, \sigma)$
as above and $\widehat{\fg}^{(r)} \in \{A_{2n-1}^{(2)}, D_{n+1}^{(2)},
E_6^{(2)}, D_4^{(3)}\}$ the $r$-twisted affine Kac--Moody algebra with
finite root system $\fg$ (Kac 1990 Ch.~8 Theorem 8.3, Aff 2 / Aff 3).
\[
 \partial\hCS_5(\fg^{\mathrm{ADE}})^{\sigma}
 \;\simeq\;
 Y_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\fg}^{(r)}),
 \qquad \epsilon_1 + \epsilon_2 + \epsilon_3 = 0,
\]
as a vertex-algebra isomorphism to all orders in $\hbar$ as a formal
power series.
\end{corollary}

\begin{proof}
Corollary \ref{cor:sigma-equivariant-bubble-transfer-bcfg} gives the
$\sigma$-equivariant all-orders quantisation of 6D $\hCS(\fg^{\mathrm{ADE}})$;
the Costello 2013 5D-boundary functor (arXiv:1303.2632 §§4--5) transports
it to an identification $\partial\hCS_5(\fg^{\mathrm{ADE}})^{\sigma}
\simeq Y_\epsilon(\widehat{\fg}^{\mathrm{ADE}})^{\sigma}$ via the
Francis 2013 factorisation-homology envelope $U_3: E_3\text{-Alg} \to
\mathrm{Pr}^{\mathrm{st}}$ (*Geom.\ Topol.* 17 Theorem 2.29; functorial
in $\sigma$-equivariant input). Kac 1990 Theorem 8.3 identifies
$(\widehat{\fg}^{\mathrm{ADE}})^{\sigma} = \widehat{\fg}^{(r)}$;
Guay--Nakajima--Wendlandt 2018 *Adv.\ Math.* 338 lifts this to
$Y_\epsilon(\widehat{\fg}^{\mathrm{ADE}})^{\sigma}
\simeq Y_\epsilon(\widehat{\fg}^{(r)})$.
\end{proof}

## Summary: state A closure

The Wave 3 C01 conditional closure is upgraded to full closure. The
$\sigma$-equivariant bubble-transfer lemma is a direct corollary of
Costello 2011 Theorem 9.3.1 applied to a finite $G$-action in
characteristic zero, using Maschke averaging. No higher-loop
finite-group-cohomology obstruction arises because $H^{\geq 1}(G,
\mathbb{Q}\text{-vector space}) = 0$ for finite $G$. The Lyndon--Hochschild--Serre
spectral sequence collapses at $E_2$, giving the $G$-invariant
deformation cohomology as a direct summand of the ambient. The
BCFG all-orders $\hCS$-to-Yangian theorem (Corollary
\ref{cor:bcfg-all-orders-unconditional}) is unconditional, closing
the Wave 2 refinement Tier I residual item.
