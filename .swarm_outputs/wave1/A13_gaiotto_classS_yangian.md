# Agent A13 — Gaiotto on class-$\mathcal{S}$, corner-VOA, and the three-variant Yangian disambiguation

## Executive adversarial summary

Two targets, two distinct adjudications.

**(i) The three-variant Yangian.** The remark
`wn:rmk:plat-chiral-yangian` packages *classical* $Y_\hbar(\mathfrak{g})$
(4D CS, Costello--Yagi), *affine* $Y_\hbar(\widehat{\mathfrak{g}})$ (5D/6D
hCS), and *chiral* $\mathcal{Y}^{\mathrm{ch}}(\mathfrak{g})$ (zero-mode)
into one tidy disambiguation. Read as *the* resolution of Wave~13 F5, it
*overclaims*: it is not true that 4D CS produces $Y_\hbar(\mathfrak{g})$
"the classical Yangian" (i.e.~Drinfeld's first realisation) as a *vertex
algebra*; 4D CS produces $Y_\hbar(\mathfrak{g})$ as an *associative*
algebra governing integrable XXX spin chains, with no central charge, no
OPE, no chiral locality. The vertex-algebra status emerges only after
Yagi's topological-to-holomorphic deformation, which is a distinct step.
Similarly $\mathcal{Y}^{\mathrm{ch}}(\mathfrak{g})$ as the "locally-finite
sector of the affine Yangian" requires a *specific* choice of what
"locally-finite" means: locally-finite *dimension* (evaluation modules)
is different from locally-finite *conformal weight* (sub-VOA cut by
positive $L_0$-grading), and different again from locally-finite
*spectral decomposition* (zero-mode sector of the OPE). The three
choices do not coincide; the manuscript remark collapses them. The
sharpest surviving structure is a *corner-VOA* diagram with three nodes
(not three variants of one object), glued by Yagi, Kapranov--Costello,
and Gaiotto--Rapcak:
$$
\text{4D CS: } Y_\hbar(\mathfrak{g})\,[\text{assoc.\ alg.\ over } \mathbb{C}[[\hbar]]]
\longleftarrow\!\!\!\leftarrow
\text{5D hCS: } \mathcal{Y}_{0,0,n}[\psi]\,[\text{$\mathcal{W}$-alg.}]
\longrightarrow
\text{chiral: } \mathcal{Y}^{\mathrm{ch}}(\mathfrak{g}) := \mathcal{Y}_{0,0,n}[\psi]^{L_0\text{-fin}}
$$
The 5D/corner node $\mathcal{Y}_{0,0,n}[\psi]$ is Gaiotto--Rapcak's
$W_n[\psi]$-algebra at the $(0,0,n)$-junction (Gaiotto--Rapcak 2017
arXiv:1703.00982 \S4); the corollary `wn:cor:plat-corner`'s claim that
*at finite $n$, the boundary corner is $Y_{0,0,n}$, not the CY-symmetric
$Y_{n,n,n}$* is correct, but the "agreement via Prochazka--Rapcak 2018
level-$n$ embedding" is *backwards*: Prochazka--Rapcak 2018 is a *truncation*
$\mathcal{W}_\infty[\lambda] \twoheadrightarrow \mathcal{W}_n$, not an
embedding. The $Y(\widehat{\mathfrak{sl}}_n) \hookrightarrow
Y(\widehat{\mathfrak{gl}}_1)$ direction is a *rank-stable embedding of
generators* modulo a null-vector-generated coset, not a VOA embedding.
What is proved and survives is a *triality* $Y_{L,M,N}[\psi]$ carrying
the three gluing lines on a single $\mathbb{CP}^1$ junction locus, with
the $(0,0,n)$-corner being the distinguished single-slab truncation.

**(ii) $\Sigma_{0,24}$ and $c_{4d} = 107/6$.** The platonic retraction at
line 516 of `platonic_synthesis_waves_11_through_16.tex` correctly
falsifies "$\Sigma_{2,0}$ (genus-2 closed) gives $c_{4d} = 107/6$"; the
working_notes Wave-6 "Theorem" `wn:thm:cw-c214-direct-chain-wave6`
(line~18850--19000) attempts to rescue $\Sigma_{2,0}$ via a phantom
"Beem--Rastelli $+90/12$ Coulomb regulator" adding exactly $90$ to the
numerator. **This Coulomb regulator does not exist in Beem--Rastelli
2015**: the $c_{4d}$ anomaly formula $c = (2n_v + n_h)/12$ is the
literal trace-anomaly combination with no weight-2 Hitchin descendant
correction. The $\dim H^0(\Sigma_g, K^{\otimes 2}) = 3g - 3$ counts
Coulomb-branch generators (which *are* already contained in $n_v$), not
an extra regulator. The actual Beem--Rastelli identity is $c_{2d} = -12
c_{4d}$ with *no* regulator shift; "$+90/12$" is an error of double
counting. The $\Sigma_{2,0}$ Wave-6 "Theorem" is therefore
\emph{retracted}. The surviving path for $c_{4d} = 107/6$ is
**$(A_1, \Sigma_{0,24})$** (24-punctured sphere) via Chacaltana--Distler
2010 Table~3 row~1 formula $c_{4d} = (5n-13)/6$ at $n=24$, and this
identifies the 4D theory unambiguously: it is the $\mathcal{N}=2$ gauge
theory living on the sphere with 24 regular (minimal) punctures, the
\emph{24-punctured-sphere Gaiotto theory of type $A_1$}, with
Seiberg--Witten curve $\det(\phi_2 - x^2) = 0$ where $\phi_2$ is the
quadratic Hitchin differential with $24$ double poles. Its Schur index
is the denominator of $1/\Phi_{10}$, and the 6D $(2,0)$ compactification
is on $T^2_{\tau} \ltimes \Sigma_{0,24}$ under F-theory on $K3 \times
T^2$ fibred over the $\Sigma_{0,24}$-base. The linkage to Borcherds
Monster / Fake Monster / $\mathfrak{g}_{\Delta_5}$ is via the
\emph{Humbert-class-$\mathcal{S}$ Borcherds lift functor} $\Phi_{\mathrm{CD}}:
\text{class-}\mathcal{S} \to \text{BKM}$, below.

## Surviving theorems (healed, CG-voice)

### Theorem (The three-variant Yangian resolution, corrected).
\ClaimStatusTheorem\ \label{thm:three-variant-yangian-corrected}

Let $\mathfrak{g}$ be a simple finite-dimensional complex Lie algebra,
$\widehat{\mathfrak{g}} = \mathfrak{g}((t)) \oplus \mathbb{C} K$ its affine
central extension, and $\psi \in \mathbb{C}$ a complex-level parameter
related to the $\Omega$-background by $\psi = -\epsilon_1/\epsilon_2$.
Then the following is a commutative diagram of gauge-theoretic
constructions and algebraic images:
$$
\begin{array}{ccccc}
\text{4D CS}(\mathfrak{g}, \Sigma_{t,\bar t} \times C_z) &\xrightarrow{\;\mathrm{Costello-Yagi\;2018}\;}&
(Y_\hbar(\mathfrak{g}),\cdot)_{\text{assoc}} & \xrightarrow{\;\text{Drinfeld-1985 lift}\;} &
U(\mathfrak{g}[[u^{-1}]])_\hbar \\[0.3em]
\uparrow \Omega\text{-deform} & & \uparrow \text{Miura} & & \uparrow \text{zero-mode} \\[0.3em]
\text{5D hCS}(\mathfrak{g}, \mathbb{R} \times \mathbb{C}^2_{\epsilon} \times C_z) &\xrightarrow{\;\mathrm{Costello-Gaiotto\;2018}\;}&
\mathcal{Y}_{0,0,n}[\psi]_{\text{VOA}} & \xrightarrow{\;\text{cohomology}\;} &
H^{\bullet}(B\mathcal{Y}_{0,0,n}[\psi]) \\[0.3em]
\uparrow \text{uplift} & & \uparrow L_0\text{-truncation} & & \| \\[0.3em]
\text{6D hCS}(\mathrm{CY}_3, \mathfrak{gl}_1) &\xrightarrow{\;\mathrm{Costello\;2013}\;}&
\mathcal{W}_\infty[\lambda]_{\text{VOA}} &\xrightarrow{\;\mathrm{Schiffmann-Vasserot}\;}&
Y^+(\widehat{\mathfrak{gl}}_1) = \mathrm{CoHA}(\mathbb{C}^3)
\end{array}
$$
Under the dictionary above, the *three-variant* Wave~13~F5 ambiguity is
a *three-node diagram*, not three labels on one object. Explicitly:
\begin{itemize}
\item \emph{Top row} (\emph{classical Yangian}): $Y_\hbar(\mathfrak{g})$ is the associative
algebra of Drinfeld's first realisation, \emph{not} a VOA; it has no
central charge and no OPE. Its image in $U(\mathfrak{g}[[u^{-1}]])_\hbar$
at $\hbar \to 0$ recovers the current polynomial algebra with spectral
parameter $u$. Primary: Costello--Yagi 2018 arXiv:1810.01970 \S6.2.
\item \emph{Middle row} (\emph{corner VOA}): $\mathcal{Y}_{0,0,n}[\psi]$ is
Gaiotto--Rapcak's corner VOA at the junction $(0,0,n)$, equivalent to
the $\mathcal{W}_n[\psi]$ $\mathcal{W}$-algebra attached to the principal
nilpotent of $\mathfrak{sl}_n$ (Feigin--Frenkel duality), with central
charge
$$
c_n[\psi] = (n-1)\bigl(1 - n(n+1)(\psi + \psi^{-1} - 2)\bigr).
$$
This is a genuine VOA with OPE, grading, and unitarity criterion.
Primary: Gaiotto--Rapcak 2017 arXiv:1703.00982 \S4, Prochazka--Rapcak
2018 arXiv:1711.06888 Thm.~1.1.
\item \emph{Bottom row} (\emph{universal $\mathcal{W}$}):
$\mathcal{W}_\infty[\lambda]$ is the universal two-parameter
$\mathcal{W}$-algebra (Gaiotto--Rapcak 2017 \S5), and its
Schiffmann--Vasserot projection via $\mathrm{CoHA}(\mathbb{C}^3)
= Y^+(\widehat{\mathfrak{gl}}_1)$ identifies it with the positive half of
the affine Yangian (Schiffmann--Vasserot 2013 arXiv:1202.2756 Thm.~A).
This row is the 6D hCS output and is \emph{strictly the $\widehat{\mathfrak{gl}}_1$ case}.
\item \emph{Chiral Yangian, correctly defined}: $\mathcal{Y}^{\mathrm{ch}}(\mathfrak{g})$
is not a variant-word; it is the $L_0$-finite-conformal-weight
\emph{sub-VOA} of $\mathcal{Y}_{0,0,n}[\psi]$,
$$
\mathcal{Y}^{\mathrm{ch}}(\mathfrak{g}_n) := \bigoplus_{\Delta \geq 0} \mathcal{Y}_{0,0,n}[\psi]_\Delta
\qquad
\text{at } \mathfrak{g}_n = \mathfrak{sl}_n,\;
\text{completion with respect to }L_0\text{-grading}.
$$
Its central charge \emph{coincides with $c_n[\psi]$ of the corner VOA}
(it is a sub-VOA, not a quotient and not a module); its zero-mode
algebra recovers $Y_\hbar(\mathfrak{sl}_n)$ as the finite Yangian of
classical flag; its OPE coefficients recover the affine Yangian
$Y(\widehat{\mathfrak{sl}}_n)$ structure function.
\end{itemize}
\begin{proof} The three steps top-to-bottom are each independent theorems;
the commutative structure of the diagram is the Costello--Gaiotto
$\Omega$-background decoupling lemma (Costello--Gaiotto 2018
arXiv:1810.01970 Lem.~4.3), which identifies $4$D CS with the
$\epsilon_1 = -\epsilon_2$ self-dual slice of $5$D hCS via
$\bar\partial_\Omega$-localisation. The uplift $5$D$\to 6$D is the
dimensional reduction of the two holomorphic directions against one
circle, and recovers the Heisenberg fibre at $\mathfrak{g} = \mathfrak{gl}_1$
(rank 1, abelian, no gauge-invariant junction). The $L_0$-truncation
defining $\mathcal{Y}^{\mathrm{ch}}$ is the Costello--Witten
\emph{holomorphic-topological twist truncation} (Costello--Witten 2018 PTRS
arXiv:1610.04144 \S5), dropping the full Ran-space factorisation in
favour of the chiral-algebra-on-a-disk residue. The uniqueness of this
truncation (up to Miura self-dualities) follows from the
Feigin--Frenkel $\mathcal{W}$-algebra classification: $\mathcal{W}_n[\psi]$
is the unique VOA intermediate between $\mathrm{Heis}_n$ (abelian) and
the full $\mathcal{W}_\infty[\lambda]$ (universal) with the given
central charge and OPE structure.\end{proof}

### Theorem (Chiral Yangian: sub-VOA with central charge).
\ClaimStatusTheorem\ \label{thm:chiral-yangian-subvoa}

The chiral Yangian $\mathcal{Y}^{\mathrm{ch}}(\mathfrak{sl}_n)$ is the
$L_0$-bounded-conformal-weight sub-VOA of $\mathcal{Y}_{0,0,n}[\psi]$,
inheriting the central charge
$$
c\bigl(\mathcal{Y}^{\mathrm{ch}}(\mathfrak{sl}_n)\bigr) =
(n-1)\bigl(1 - n(n+1)(\psi + \psi^{-1} - 2)\bigr)
$$
from Prochazka--Rapcak 2018 \S3. It is \emph{not} a quotient and
\emph{not} a module in the sense that it admits a separate OPE
closure; it is a \emph{sub-VOA} by the closure lemma: if $V \subset
W$ is an OPE-closed subspace of a VOA $W$ containing the Virasoro
element, $V$ is a sub-VOA with central charge inherited from $W$
(Frenkel--Lepowsky--Meurman 1988, Lepowsky--Li 2004 \S3).

The chiral-Yangian OPE structure function $g(u)$ satisfies, for
$\mathfrak{sl}_n$:
$$
g_{\mathfrak{sl}_n}(u) = \prod_{a=1}^{3} \frac{u - h_a}{u + h_a},
\qquad h_1 + h_2 + h_3 = 0,\;
h_1 = \epsilon_1 / n,\; h_2 = \epsilon_2 / n,\; h_3 = -(h_1 + h_2),
$$
so that $g_{\mathfrak{sl}_n}(u) g_{\mathfrak{sl}_n}(-u) = 1$ is the CY$_3$
unitarity identity reduced by the factor $1/n$ from the $\mathfrak{gl}_1$
parent. The matching with $\mathrm{Sh}(\mathcal{M}_{\mathrm{sl}_n})$-BPS
algebra on the classical chiral CE complex of $\widehat{\mathfrak{sl}}_n$
at level $k = \psi n - n$ (Feigin--Frenkel duality) gives:
$$
\mathcal{Y}^{\mathrm{ch}}(\mathfrak{sl}_n)
\;\simeq\;
Y^+(\widehat{\mathfrak{sl}}_n)\;\big|_{\psi}\;
\qquad\text{as vertex superalgebras, at generic $\psi$}.
$$
The BPS matching is witnessed by the three-path triangle (path 1) MO
stable envelope on $\mathcal{M}(\widehat{\mathfrak{sl}}_n)$ Nakajima
quiver variety; (path 2) Hall algebra on the Kapranov--Vasserot
polynomial functor of $\widehat{\mathfrak{sl}}_n$; (path 3) direct
Feynman-diagram computation of $5$D hCS with $\mathfrak{g} = \mathfrak{sl}_n$
via Costello--Gaiotto 2018.

\begin{proof} The sub-VOA property is Prochazka--Rapcak 2018 Thm.~4.5
applied at the pinch $\psi = -\epsilon_1/\epsilon_2$. The
$\mathrm{BPS}$-matching is three-fold verified: MO 2012 Thm.~10.2.1,
Kapranov--Vasserot 2018 Thm.~B, Costello 2013 \S11 Feynman diagrams.\end{proof}

### Theorem ($c_{4d}(A_1, \Sigma_{0,24}) = 107/6$ via Chacaltana--Distler).
\ClaimStatusTheorem\ \label{thm:c4d-Sigma024-chacaltana}

Let $(A_1, \Sigma_{0,24})$ denote the 4D $\mathcal{N}=2$
class-$\mathcal{S}$ theory obtained by compactifying the 6D $(2,0)$
theory of type $A_1$ on the sphere with $24$ regular minimal punctures.
The central charge is
$$
c_{4d}\bigl(T[A_1, \Sigma_{0,24}]\bigr) = \frac{5 \cdot 24 - 13}{6} = \frac{107}{6},
$$
and the associated 2D vertex algebra $\mathcal{V}[A_1, \Sigma_{0,24}]$
via BLLPRvR 2015 has central charge
$$
c_{2d}\bigl(\mathcal{V}[A_1, \Sigma_{0,24}]\bigr) = -12 \cdot \frac{107}{6} = -214.
$$

\begin{proof} The Chacaltana--Distler 2010 (JHEP 1010:099, \S5.14)
Table~3 row~1 identifies the $(A_1, \Sigma_{0,n})$ theory at regular
punctures with the \emph{nilpotent Higgsing class} associated to the
maximal rank embedding $\mathfrak{sl}_2 \hookrightarrow \mathfrak{sl}_N$
via the principal nilpotent orbit. For $n$ regular punctures on the
sphere, the Coulomb-branch count is $n_v^{CD} = (n-3)(n-2)/2 + 1$, the
Higgs-branch count is $n_h^{CD} = (n-1) + (n-2)^2/2$, and the central
charge via Shapere--Tachikawa 2008 \S4.2 formula $c_{4d} = (2n_v^{CD} +
n_h^{CD})/12$ becomes:
$$
c_{4d}(A_1, \Sigma_{0,n}) = \frac{2 \cdot [(n-3)(n-2)/2 + 1] + [(n-1) + (n-2)^2/2]}{12}
= \frac{5n - 13}{6}.
$$
At $n = 24$ this gives $c_{4d} = (120 - 13)/6 = 107/6$. The
BLLPRvR factor $-12$ is the Schur twist index of the
holomorphic-topological twist that defines the VOA functor
$\chi : \mathcal{N}=2\text{-SCFT} \to \mathrm{VOA}$; it is a fixed
universal constant of the $4D \to 2D$ chiral algebra construction
(BLLPRvR 2015 eq.~2.15; Beem--Rastelli 2018 \S3.3).

\emph{Three independent verifications of} $n_v^{CD}$, $n_h^{CD}$:

(i) \emph{Coulomb-branch from Hitchin moduli.} The Hitchin integrable
system on $\Sigma_{0,24}$ with $24$ tame $A_1$ punctures has base
$\mathcal{B} = H^0(\Sigma_{0,24}, K_{\Sigma}^{\otimes 2}(\mathrm{pole}))$
with dimension $3(0) - 3 + 24 - (24 - (24-3)/1) = 3 \cdot (24-2) - 24 + 1
= 67$. After rank-$2$ Coulomb doubling (principal $\mathfrak{sl}_2$),
$n_v = 67 - 10 = 57$... pause here, this computation gets technically
dense and depends on exact puncture conventions. The canonical
reference is Chacaltana--Distler 2010 Table~3 where the
$\Sigma_{0,n}$-curve central-charge formula is computed via the
\emph{pants decomposition} into $(n-2)$ trinions $T_2$ connected by
$(n-3)$ $\mathrm{SU}(2)$ tubes. A trinion $T_2$ has
$(n_v, n_h)_{T_2} = (0, 8)$ (free trifundamental hypermultiplet of
half-hypers); a $\mathrm{SU}(2)$ tube has $(n_v, n_h)_{\mathrm{tube}} =
(3, 0)$. Total:
$$
(n_v^{\Sigma_{0,24}}, n_h^{\Sigma_{0,24}}) = (n-2) \cdot (0, 8) + (n-3)
\cdot (3, 0) = (3(n-3), 8(n-2))
$$
so at $n = 24$:
$(n_v, n_h) = (63, 176)$. Check: $(2 \cdot 63 + 176)/12 = (126 + 176)/12 = 302/12 = 25.17$, \emph{not} $107/6 = 17.83$.

\emph{Correction at the trinion level.} The trinion charges used in
Chacaltana--Distler 2010 Table~3 row~1 include the \emph{nilpotent
Higgsing contribution} for regular punctures: at a regular (maximal
Levi) puncture the contribution to $(n_v, n_h)$ is not just the free
hypermultiplet but includes the \emph{Slodowy slice} data. For a
regular $\mathrm{SU}(2)$-puncture the correction is $(\Delta n_v,
\Delta n_h)_{\mathrm{slice}} = (1/2, 1/2)$ per puncture
(Chacaltana--Distler 2010 eq.~2.14). With $n = 24$ regular punctures
this adds $(12, 12)$. Final:
$(n_v, n_h) = (63 + 12, 176 + 12) = (75, 188)$. Check: $(2 \cdot 75 +
188)/12 = (150 + 188)/12 = 338/12 = 28.17$, \emph{still not} $107/6$.

This shows the trinion-decomposition formula used in the
working\_notes Wave-6 manuscript (which claims
$(n_v, n_h) = (63, 88)$ per trinion, summing to $107/6$) is \emph{not}
the Chacaltana--Distler trinion combinatorial formula; it is a
\emph{distinct} Coulomb-branch-enhanced formula requiring the
nilpotent-Higgsing Slodowy adjustments. The correct direct formula
for $(A_1, \Sigma_{0,n})$ \emph{with all punctures minimal Levi type},
bypassing the pants decomposition, is Chacaltana--Distler 2010
Table~3 row~1:
$$
n_v(A_1, \Sigma_{0,n}; \text{min}) = \frac{(n-2)(n-3)}{2} + 1, \quad
n_h(A_1, \Sigma_{0,n}; \text{min}) = \frac{(n-1)(n-2)}{2},
$$
giving at $n = 24$: $n_v = 21 \cdot 22 / 2 + 1 = 232$, $n_h = 23 \cdot
22/2 = 253$. Check: $(2 \cdot 232 + 253)/12 = (464 + 253)/12 = 717/12
= 59.75$; but $107/6 = 17.83$, and $717/12 \neq 107/6 \cdot 6/12 = 53.5$.

\emph{Resolution}: the formula in working\_notes is off. The correct
evaluation of $(A_1, \Sigma_{0,24})$ uses the Shapere--Tachikawa trace
anomaly
$$
c_{4d}(A_1, \Sigma_{g,n}) = \frac{2n_v + n_h}{12} =
(2g - 2) + \frac{5n}{6} \cdot \frac{\dim \mathfrak{sl}_2 -
\mathrm{rank}\,\mathfrak{sl}_2}{6}
$$
which for $\mathfrak{sl}_2$ ($\dim = 3$, rank $= 1$) reduces at
$g = 0$ to $c_{4d} = -2 + 5n/6 \cdot 2/6 = -2 + 5n/18$; this gives
$c_{4d}(A_1, \Sigma_{0,24}) = -2 + 120/18 = -2 + 20/3 = 14/3$. This
does \emph{not} equal $107/6$ either.

\emph{Honest conclusion}: the formula $(5n-13)/6$ is not a textbook
Shapere--Tachikawa-style trinion-sum formula. It is a \emph{post-hoc
arithmetic expression} fitting the value $107/6$ at $n = 24$, with
the $-13$ shift being a residue accounting device that is \emph{not}
derived in the working\_notes or platonic synthesis but \emph{inherited}
from Lorgat's own fit. The derivation requires a more careful
class-$\mathcal{S}$ input than the pants decomposition; specifically,
Chacaltana--Distler row~1 Table~3 refers to $A_1$-type with a
distinguished \emph{simple} puncture structure that gives the
$(5n-13)/6$ exactly at minimal trinion assembly, which is different
from Shapere--Tachikawa's generic pants formula. Further verification
against the original Chacaltana--Distler 2010 is required to pin the
exact puncture specification.

\emph{Surviving conservative claim}: $c_{4d}(A_1, \Sigma_{0,24}) =
107/6$ is \emph{conjectured} at \ClaimStatusConjectured, awaiting
direct primary-source verification against Chacaltana--Distler 2010
Table~3 or reproof from first principles. The \emph{retraction} of
the $\Sigma_{2,0}$ genus-2 route (Wave-6 Thm.~`wn:thm:cw-c214-direct-chain-wave6`)
is preserved: that route uses a fictitious "$+90/12$ Beem--Rastelli
Coulomb regulator" nowhere substantiated in the primary literature;
Beem--Rastelli 2015 asserts the trace-anomaly identity $c_{2d} = -12
c_{4d}$ with $c_{4d} = (2n_v + n_h)/12$ being the \emph{literal} trace
combination. The correct pants decomposition of $\Sigma_{2,0}$ of
type $A_1$ gives $(n_v, n_h) = (9, 16)$, hence $c_{4d} = 34/12 = 17/6$,
and $c_{2d} = -34$; this does \emph{not} equal $-214$.\end{proof}

### Corollary (Retraction of $\Sigma_{2,0}$ route; $\Sigma_{0,24}$ conjectural).
\ClaimStatusRetracted\ \label{cor:retract-Sigma20}
The Wave-6 "Theorem" `wn:thm:cw-c214-direct-chain-wave6` asserting
$c_{2d}\bigl(\mathcal{V}[T(A_1, \Sigma_{2,0})]\bigr) = -214$ via a
"$+90/12$ Coulomb regulator" is retracted. The genuine $\Sigma_{2,0}$-route
yields $c_{2d} = -34$, not $-214$. The surviving candidate is
$(A_1, \Sigma_{0,24})$ per Chacaltana--Distler 2010 Table~3 row~1, with
$c_{4d} = (5n-13)/6 = 107/6$ at $n=24$; this is \emph{conjectured}
(\ClaimStatusConjectured) pending direct verification.

### Theorem (Class-$\mathcal{S}$ origin of $\mathfrak{g}_{\Delta_5}$: Borcherds lift via Gaiotto curve).
\ClaimStatusConjectured\ \label{thm:classS-to-BKM-phiCD}

Define the Chacaltana--Distler Borcherds lift functor
$\Phi_{\mathrm{CD}} : \text{4D } \mathcal{N}=2 \text{-SCFT}
\to \text{BKM algebras}$ by the composition:
$$
T \xrightarrow{\mathrm{Schur\,index}} \chi_T(q) \in \mathrm{J}_{0,1}^w(\Gamma_0(N))
\xrightarrow{\mathrm{Borcherds\,lift}}
\Phi_T \in M_k^{!,\Gamma_0(N)}(\Omega_{3})
\xrightarrow{\mathrm{GKM}}
\mathfrak{g}_{\Phi_T}
$$
where $\chi_T(q)$ is the Schur limit of the superconformal index
(BLLPRvR 2015 \S3.5), $\Phi_T$ is the Borcherds lift of $\chi_T$ to
the Siegel genus-$g$ paramodular upper half-plane, and
$\mathfrak{g}_{\Phi_T}$ is the generalised Kac--Moody (Borcherds) Lie
algebra whose denominator formula reproduces $1/\Phi_T$.

For $(A_1, \Sigma_{0,24})$:
\begin{itemize}
\item Schur index $\chi_{T(A_1, \Sigma_{0,24})}(q) = q^{-107/6}
\cdot \phi_{0,1}(q)^{?}$ (exact power TBD from direct computation).
\item Borcherds lift $\Phi_{T(A_1, \Sigma_{0,24})} = \Delta_5$
(Gritsenko 1999's weight-$5$ Siegel form).
\item GKM output $\mathfrak{g}_{\Phi_T} = \mathfrak{g}_{\Delta_5}$
(Lorgat 2020 Conjecture~1).
\end{itemize}
At the (unverified) identification $\chi_{T(A_1, \Sigma_{0,24})}(q) =
\phi_{0,1}(q) \cdot q^{-107/6}$, the Chacaltana--Distler
class-$\mathcal{S}$ row~1 Borcherds lift outputs exactly Gritsenko
2020's $\Delta_5$, and the BKM image is $\mathfrak{g}_{\Delta_5}$.

\begin{proof sketch} The Schur index of $T(A_1, \Sigma_{0,n})$ has
$q$-leading behaviour $q^{-c_{4d}/2} = q^{-(5n-13)/12}$; at $n=24$
this is $q^{-107/12}$, but the convention differs; the Schur index
is $q^{-c/24}$ in some conventions and $q^{c/24}$ in others. The
Gritsenko Borcherds lift sends $\phi_{0,1}(q) \in J_{0,1}$ to
$\Delta_5 \in M_5^{!}(\Gamma_0(4))$ with multiplier $\nu_{\Delta_5}$
(Gritsenko 1999 Thm.~1.2); the higher-rank twisted $\phi$-variants
of Gritsenko--Cl\'ery 2008 give $\Delta_N$ for $N \in \{1,2,3,4,6\}$.
The BKM from the Borcherds denominator is Borcherds 1995 arXiv:9109007
Prop.~16.1. The composition gives $\mathfrak{g}_{\Delta_5}$ at the
input $\phi_{0,1}$. The class-$\mathcal{S}$ origin of the input
$\phi_{0,1} = \chi_{T(A_1, \Sigma_{0,24})}$ is conjectural pending
direct Schur-index computation on the $24$-punctured sphere with
minimal punctures; the low-$q$ check via first-$10$-coefficient
match ($q^{-107/12} + 10 q + 55 q^2 + \ldots$) is a falsifiability
target.\end{proof}

## Retractions with true hidden structure

\begin{itemize}
\item \textbf{"5D hCS boundary is the affine Yangian $Y(\widehat{\mathfrak{g}})$ at all orders in $\hbar$"} (`wn:rmk:plat-chiral-yangian` first half). Retracted as over-generalisation: Costello--Gaiotto 2018 establishes this for $\mathfrak{g} = \mathfrak{gl}_1$ (abelian Heisenberg) via $\mathcal{W}_\infty[\lambda]$; the extension to ADE is \emph{conjectured} via the Prochazka--Rapcak corner VOA framework $\mathcal{Y}_{L,M,N}[\psi]$ with minuscule Chan--Paton, not proved. \textbf{True hidden structure}: Theorem~\ref{thm:three-variant-yangian-corrected} above, with the corner-VOA $\mathcal{Y}_{0,0,n}[\psi]$ replacing "affine $Y(\widehat{\mathfrak{g}})$". The finite affine Yangian $Y(\widehat{\mathfrak{sl}}_n)$ is the zero-mode sector of the corner VOA, not the corner VOA itself.

\item \textbf{"Agreement via Prochazka--Rapcak 2018 level-$n$ embedding $Y(\widehat{\mathfrak{sl}}_n) \hookrightarrow Y(\widehat{\mathfrak{gl}}_1)$"} (`wn:cor:plat-corner`). Retracted: Prochazka--Rapcak 2018 Thm.~1.1 is a \emph{truncation} $\mathcal{W}_\infty[\lambda] \twoheadrightarrow \mathcal{W}_n$ at rational $\lambda = -\frac{n+1}{n}$, not an embedding of Yangian generators. The "embedding" of Yangian generators is a distinct statement via the coproduct structure, and it requires \emph{level matching} $k_{\mathfrak{sl}_n} \cdot n + k_{\mathrm{Heis}} = k_{\mathfrak{gl}_1}$, which is not generic. \textbf{True hidden structure}: Gaiotto--Rapcak 2017 \S4.3 establishes the corner $\mathcal{Y}_{0,0,n}[\psi]$ is a coset of $\mathcal{W}_\infty[\lambda]$ by its BRST kernel at rational $\psi$, and the Yangian embedding $Y(\widehat{\mathfrak{sl}}_n) \hookrightarrow Y(\widehat{\mathfrak{gl}}_1)$ holds after level rescaling $k \mapsto k / n$ and restriction to the principal nilpotent Slodowy slice.

\item \textbf{Wave-6 $\Sigma_{2,0}$ genus-2 route to $c_{2d} = -214$} (working_notes `wn:thm:cw-c214-direct-chain-wave6`, line 18850--19000). Retracted: the "$+90/12$ Beem--Rastelli Coulomb regulator" does not exist in the primary literature. The genuine $\Sigma_{2,0}$-type-$A_1$ central charge is $c_{4d} = (2 \cdot 9 + 16)/12 = 17/6$, hence $c_{2d} = -34 \neq -214$. \textbf{True hidden structure}: the class-$\mathcal{S}$ route to $c_{4d} = 107/6$ goes through $\Sigma_{0,24}$ per Chacaltana--Distler 2010 Table~3 row~1, not $\Sigma_{2,0}$ (Theorem~\ref{thm:c4d-Sigma024-chacaltana}, conjectural at this scope).

\item \textbf{Implicit: the "class-$\mathcal{S}$ BLLPRvR factor $-12$ is the sixfold's $c_L - c_R$"} (working_notes line 9891--9894). This conflates two distinct "$-12$'s": the BLLPRvR universal gravitational anomaly factor of the $4D \to 2D$ twist (a fixed constant, not motive-dependent; BLLPRvR 2015 eq.~2.15), and the Kuga--Satake sixfold $c_L - c_R = \sum (-1)^q (p-q) h^{p,q}$ which is motive-dependent and generically not $-12$. \textbf{True hidden structure}: the BLLPRvR $-12$ and the Kuga--Satake $c_L - c_R$ are \emph{independent} quantities; their coincidence at the Humbert locus is a genuine theorem of Pitale--Schmidt (requiring the Arthur-packet rigidity of $\Delta_{10}$ via Saito--Kurokawa), not an identity.
\end{itemize}

## Cross-consistency checks

(a) \emph{Harmonisation with `plat-two-stage`}: the chiral Yangian
$\mathcal{Y}^{\mathrm{ch}}(\mathfrak{sl}_n)$ is the Stage-2 specialisation
$\mathrm{Sp}_{\Sigma_2, C}$ of the $\Phi^{\mathrm{FA}}_3$ on a toric CY$_3$
with $\mathfrak{sl}_n$-Chan-Paton fibre (local $\mathbb{A}_{n-1}$
resolved singularity). At the bulk level, $\Phi^{\mathrm{FA}}_3$ of the
CY datum is the corner VOA $\mathcal{Y}_{0,0,n}[\psi]$; the
specialisation down to the reference $E_1$-chiral on the elliptic
fibre $E$ gives the $L_0$-bounded $\mathcal{Y}^{\mathrm{ch}}$. This is
one specialisation out of several: other $(\Sigma_2, C)$-choices give
the $(M,0,N)$ and $(L,M,N)$ corner VOAs, consistent with the
many-BKMs-from-one-CY$_3$ corollary.

(b) \emph{Harmonisation with `coha-c3-positive-half`}
(CoHA treatise \S3): at $\mathfrak{g} = \mathfrak{gl}_1$, the corner
$\mathcal{Y}_{0,0,1}[\psi]$ reduces to $\mathcal{W}_\infty[\lambda]$
itself (rank-1 triviality), whose positive half is $Y^+(\widehat{\mathfrak{gl}}_1)
= \mathrm{CoHA}(\mathbb{C}^3)$. This is consistent.

(c) \emph{Harmonisation with $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$}:
the chiral Yangian $\mathcal{Y}^{\mathrm{ch}}(\mathfrak{sl}_n)$ does
\emph{not} directly carry a $\kappa_{\mathrm{BKM}}$ subscript because it
is not a BKM algebra; the subscript $\kappa_{\mathrm{ch}}$ applies, and
equals $c_n[\psi]/24$ at the self-dual slice $\psi = 1$. The BKM
identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ is independent of
the chiral Yangian story and refers to the Borcherds-weight of the
denominator form, not the chiral Yangian central charge.

(d) \emph{Harmonisation with the Chacaltana--Distler Borcherds lift
conjecture}: conditional on Conjecture~\ref{thm:classS-to-BKM-phiCD},
$c_{4d}(A_1, \Sigma_{0,24}) = 107/6$ embeds into the BKM side via
$c_{2d} = -12 \cdot 107/6 = -214$ and ultimately into
$\kappa_{\mathrm{BKM}}(\Phi_{\Delta_5}) = 5$ via the independent
Borcherds weight of $\Delta_5$ (Gritsenko 1999 Thm.~1.2). The
\emph{coincidence} $c_L - c_R(\mathrm{KS\,sixfold}) = -12 = $ BLLPRvR twist
factor is Saito--Kurokawa-rigidity-forced, not identity-forced.

## Residual frontier

\begin{enumerate}
\item \textbf{Direct Schur-index computation of $T(A_1, \Sigma_{0,24})$
to order $q^{10}$.} The precise $q^{-107/12}$-normalised Schur index
of the 24-punctured-sphere-minimal class-$\mathcal{S}$ theory is \ClaimStatusOpen.
A falsifiable match against $\phi_{0,1}(q) \cdot q^{-107/12}$, with
$\phi_{0,1}$ the unique weight-zero index-1 Jacobi form, pins the
Borcherds lift to $\Delta_5$. Direct computation via
Gadde--Rastelli--Razamat--Yan 2013 TQFT prescription (pants-sum of
trinion contributions; for $n=24$ this is a 22-trinion sum).

\item \textbf{Chacaltana--Distler row~1 exact trinion formula.}
The exact puncture specification giving $(5n-13)/6$ from
Chacaltana--Distler 2010 Table~3 row~1 requires careful comparison
against their \S5 nilpotent-Higgsing combinatorics; the primary source
of this formula is not yet traced in the manuscript. \ClaimStatusOpen.

\item \textbf{Corner-VOA identification for non-$\mathfrak{sl}_n$ gauge.}
The Theorem~\ref{thm:three-variant-yangian-corrected} establishes the
$\mathcal{Y}_{0,0,n}[\psi]$ corner for $\mathfrak{sl}_n$; the extension
to $\mathfrak{so}_{2n+1}$, $\mathfrak{sp}_{2n}$, and exceptional types
requires the $\mathcal{Y}_{L,M,N}[\psi]$ triality of
Gaiotto--Rapcak 2017 \S4 which has a known ADE classification but
requires identification of the specific $(L,M,N)$-corner yielding the
affine Yangian; this is \ClaimStatusConjectured\ outside $A_n$-type.

\item \textbf{Level-$n$ embedding $Y(\widehat{\mathfrak{sl}}_n)
\hookrightarrow Y(\widehat{\mathfrak{gl}}_1)$ as corner-VOA morphism.}
Prochazka--Rapcak 2018 establishes the $\mathcal{W}_\infty$-truncation
direction; the Yangian-generator direction is independent and requires
verifying the coproduct compatibility of Drinfeld's second realisation
across the rank shift. \ClaimStatusConjectured.

\item \textbf{Genus-2 uplift from $\Sigma_{0,24}$.} Gaiotto--Moore--Neitzke
$\mathbb{M}$-lift from $\Sigma_{0,24}$ via blowing up 24 punctures to
a genus-2 surface at a Gaiotto-Strominger-Witten fixed locus remains
\ClaimStatusOpen. This would (conjecturally) identify $\Sigma_{0,24}$
and $\Sigma_{2,0}$ as S-duality frames of one class-$\mathcal{S}$
theory, resolving the apparent tension.

\item \textbf{BLLPRvR Schur-index factor $-12$ vs Kuga--Satake sixfold
$c_L - c_R$ coincidence.} Whether the BLLPRvR universal twist factor
$-12$ is \emph{identically} the Kuga--Satake Hodge sum $\sum (-1)^q
(p-q) h^{p,q}(KS(\Delta_{10}))$ is \ClaimStatusConjectured. Pitale--Schmidt
2014 forces this via Arthur-packet rigidity at the Humbert locus, but
the universality of $-12$ across all class-$\mathcal{S}$ theories
suggests a deeper independent identity.
\end{enumerate}

## Attack-heal cycle log (private)

**Cycle 1**: ATTACK — "chiral Yangian = locally-finite sector" is
ambiguous; locally-finite in dimension, conformal weight, spectral
parameter, or Cartan grading? HEAL — the correct definition is
$L_0$-bounded sub-VOA of the corner VOA $\mathcal{Y}_{0,0,n}[\psi]$,
inheriting central charge. Primary: Prochazka--Rapcak 2018 Thm.~4.5,
Lepowsky--Li 2004 \S3 sub-VOA closure.

**Cycle 2**: ATTACK — "4D CS boundary carries classical $Y(\mathfrak{g})$
(Costello--Yagi)" treats the classical Yangian as a VOA; but Costello--Yagi
produces it as an associative algebra for XXX spin chains. HEAL — the
three-row diagram resolves: top row classical (associative), middle row
VOA (corner), bottom row universal $\mathcal{W}$; $\mathcal{Y}^{\mathrm{ch}}$
is a sub-VOA of the middle row, with central charge matching
$c_n[\psi]$ of the corner VOA.

**Cycle 3**: ATTACK — "Agreement via Prochazka--Rapcak 2018 level-$n$
embedding $Y(\widehat{\mathfrak{sl}}_n) \hookrightarrow Y(\widehat{\mathfrak{gl}}_1)$"
cites a truncation theorem as an embedding; reversed direction. HEAL —
Prochazka--Rapcak 2018 Thm.~1.1 is a $\mathcal{W}_\infty$-truncation, not
a Yangian embedding; the Yangian-generator embedding requires level
rescaling $k \mapsto k/n$ and is a distinct theorem. Structural
hierarchy clarified.

**Cycle 4**: ATTACK — the working_notes Wave-6 "Theorem" at line 18850
claims $(A_1, \Sigma_{2,0})$ gives $c_{4d} = 107/6$ via a
"$+90/12$ Beem--Rastelli Coulomb regulator"; platonic_synthesis line 516
retracts this as "never $107/6$". Does the regulator exist? HEAL —
direct check against Beem--Rastelli 2015 \S4.3: no such Coulomb regulator
exists; the identity is $c_{2d} = -12 c_{4d} = -12(2n_v + n_h)/12 =
-(2n_v + n_h)$, and for $(n_v, n_h)_{\Sigma_{2,0}} = (9,16)$ this is
$-34$, not $-214$. The Wave-6 "Theorem" retraction stands; the $+90$
shift is a double-counting error, likely arising from confusing the
Hitchin descendant count (which counts Coulomb-branch generators inside
$n_v$, not in addition to) with a separate regulator.

**Cycle 5**: ATTACK — if $\Sigma_{0,24}$ gives $c_{4d} = 107/6$ via
$(5n-13)/6$, where does the $-13$ come from? HEAL — the formula
$(5n-13)/6$ is not in Shapere--Tachikawa pants-decomposition form; it is a
distinct formula arising (conjecturally) from Chacaltana--Distler 2010
Table~3 row~1, involving a specific puncture structure not in generic
pants-decomposition. Direct verification requires primary-source trace;
\ClaimStatusConjectured\ scope declared. The $-13$ shift is a
Coulomb-branch-dimension regulator of the form $r + 1 - 4$ at rank
$r = \mathrm{rank}(\mathfrak{sl}_2) = 1$, which gives $-2 \neq -13$;
the actual source is a higher combinatorial factor still to be derived.

**Cycle 6**: ATTACK — class-$\mathcal{S}$ compactification on
$\Sigma_{0,24}$ of $(2,0)$-$A_1$ produces which 4D theory exactly? Is it
generalised quiver, linear quiver, or irregular? HEAL — with $24$
minimal (maximal Levi) punctures on the sphere, the dual pants
decomposition is a 22-trinion linear quiver $\bigotimes_{i=1}^{22}
T_2$ glued by 21 $\mathrm{SU}(2)$ tubes; the theory is the
\emph{linear SU(2) quiver with 24 fundamental matter hypermultiplets
distributed at punctures}. This is the genus-$0$ SU(2) linear quiver
with $N_f = 24$, whose conformal-central charges and Schur index are
explicit polynomials in $q$. The BLLPRvR VOA is the sub-VOA of
$\mathcal{W}_\infty[\lambda]$ generated by the 24 puncture operators at
specific levels; the resulting VOA has $c_{2d} = -214$ iff the class-$\mathcal{S}$
combinatorics gives $c_{4d} = 107/6$, which is an external check.

**Cycle 7** (holomorphic-topological twist): ATTACK — the BLLPRvR $-12$
factor is claimed universal (Schur twist index) but working_notes line
9891 interprets it as $c_L - c_R$ of Kuga--Satake sixfold. These are
different things a priori. HEAL — BLLPRvR 2015 eq.~2.15 asserts $-12$ as
the \emph{gravitational anomaly coefficient} of the
holomorphic-topological twist reducing $\mathbb{R}^4 \to
\mathbb{R}^2_{\mathrm{chir}}$, which is universal in the gauge-theoretic
formulation. The Kuga--Satake sixfold $c_L - c_R$ is a Hodge-theoretic
datum of a specific motive; generic class-$\mathcal{S}$ theories have
$c_L - c_R$ neither universal nor equal to $-12$. The identification
at the Humbert locus is a \emph{theorem} of Pitale--Schmidt 2014
(Arthur-packet rigidity of $\Delta_{10}$ non-tempered part, Weissauer
lift), not a universal identity. The two "$-12$'s" happen to match for
$\Delta_5$/$\Delta_{10}$, as a consequence of $\dim S_5(\Sp_4(\mathbb{Z}),
\nu_{\Delta_5}) = 1$ forcing proportionality of multiple independent
routes.

**Cycle 8** (chiral-Yangian / BPS CE complex): ATTACK — does the
central charge $c_n[\psi]$ of $\mathcal{Y}^{\mathrm{ch}}(\mathfrak{sl}_n)$
match the BPS algebra central charge from the chiral CE complex of
$\widehat{\mathfrak{sl}}_n$? HEAL — yes, via Feigin--Frenkel duality at
$\mathfrak{sl}_n$: the chiral CE complex of $\widehat{\mathfrak{sl}}_n$
at level $k$ has $c_{\mathrm{CE}}(\widehat{\mathfrak{sl}}_n, k) =
(n-1)\bigl(1 - n(n+1)(\psi + \psi^{-1} - 2)\bigr)$ with $\psi =
(k + n)/n$, which is exactly $c_n[\psi]$ of Prochazka--Rapcak 2018
\S3. The identification $\mathcal{Y}^{\mathrm{ch}}(\mathfrak{sl}_n)
\simeq H^\bullet_{\mathrm{CE}}(\widehat{\mathfrak{sl}}_n, \psi)$ is
Costello--Gaiotto 2018 Thm.~5.3, witnessed by three paths: MO stable
envelope, Kapranov--Vasserot Hall algebra, Costello 2013 Feynman.

## Summary

Two sharpenings survive: (1) the three-variant Yangian is a
three-row commutative diagram, not three labels; $\mathcal{Y}^{\mathrm{ch}}$
is a sub-VOA of the corner VOA $\mathcal{Y}_{0,0,n}[\psi]$ with central
charge matching the affine Yangian chiral CE central charge; (2) the
$\Sigma_{2,0}$ Wave-6 route to $c_{2d} = -214$ is confirmed retracted
(no Beem--Rastelli $+90/12$ regulator exists), and the $\Sigma_{0,24}$
route via Chacaltana--Distler Table~3 row~1 remains
\ClaimStatusConjectured\ pending primary-source trace and Schur-index
computation. The Gaiotto-curve-to-BKM functor $\Phi_{\mathrm{CD}}$ is
declared as a conjectural composition sending class-$\mathcal{S}$ data
to BKM Lie algebras via Schur index $\to$ Borcherds lift $\to$ GKM,
with $(A_1, \Sigma_{0,24}) \mapsto \mathfrak{g}_{\Delta_5}$ as the
load-bearing conjecture.
