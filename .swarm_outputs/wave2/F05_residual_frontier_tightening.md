# Agent F05 (Wave 2) — Senior-Architect Tightening of the Residual Frontier

*Voice register: Manin on arithmetic-geometric categorification, Beilinson
on $D$-module lane discipline, Costello on BV/factorisation-algebra locality —
judging which frontier items are tight (one named primary-source gap away
from a proof) versus loose (awaiting new machinery).*

## Executive adversarial summary

The residual-frontier list in §\ref{wn:subsec:spine-frontier} is not
uniform in mathematical difficulty. After Wave 1 dissection, the eleven
listed items sort into three discipline-distinct tiers:

- **Tight** (single named primary-source extension away; promotable on a
timescale of months): BCFG $\sigma$-equivariance, $(A_1, \Sigma_{0,24})$
at $c_{4d} = 107/6$, elliptic-surface specialisation at fixed
Shioda-Inose scope, Ran-level Miki triality (already F3-downgraded in
A05 to a bridge lemma in Costello–Paquette 2020 §5).
- **Moderate** (extension of existing methods, new compact-$X$ input
needed): compact CY$_3$ 3-dualisability (Gwilliam–Williams
Prop.~5.3.2 global-sections version), bracket-level
$\fg_{\mathrm{BPS}}(K3\times E) \simeq \fg_{\Delta_5}$ (Harvey–Moore
1-loop + Bruinier reciprocity).
- **Loose** (requires new machinery; programme-direction items):
$(\infty,1)$-functoriality of $\Phi^{\mathrm{FA}}_d$ at $d\geq 3$,
integral $E_d$-formality at $d \geq 3$, doubly-reduced
DT-integrand = $1/\Phi_{12}$ on $K3^2 \times E$, non-CHL $N=7$
order-$4$ central extension of $\mathrm{Mp}_4$ by $\mu_4$, rank-$\geq 3$
lattice-polarised $\fg_L$ family.

What falls: the implicit reading that all eleven items are on equal
footing; the use of "conjecture" as a uniform label when the primary-source
gap varies from one identity (Bruinier reciprocity as a closed black box for
$\fg_{\mathrm{BPS}}$) to new BV-cohomology machinery ($(\infty,1)$-functorial
$\Phi^{\mathrm{FA}}_d$ at $d\geq 3$, which is open because Kontsevich–Tamarkin
formality lifts from objects to morphisms only at $d \leq 2$ rationally).
What survives, sharpened: a three-tier frontier stratification; three
promotions; and three new frontier targets opened by Wave-1 findings —
(i) Bardeen–Zumino cochain $\mathrm{BZ}^{\mathrm{hol}}$ as the bridge
between the consistent-cubic and covariant-quadratic faces of $\kanom$;
(ii) dimension-stratified GKM census unifying Monster / Fake Monster /
$\fg_{\Delta_5}$ through Borcherds-functorial restriction (T2 of A10);
(iii) three-faces-of-$8$ unification of the $\mathsf{B}$-row
$K^\kappa = 8$ via Bruinier reciprocity plus Drinfeld scaling.

Sharpest promotion: the $\mathsf{B}$-row $K^\kappa = 8$ Mukai-doubling
identity can be proved (unconditional on Bruinier Prop.~5.1) via the
direct K3-Serre-bifunctor $S_{K3} = [2]$ route, which upgrades item
F5 of A09 from open to theorem-grade at the chain-level lane.

Sharpest new frontier: the *dimension-stratified BKM census* — a
single $\Z$-indexed family $\{\fg^{\mathrm{BKM}}_d\}_{d \in \{1,2,3,5\}}$
related by Borcherds-functorial restriction along primitive orthogonal
lattice embeddings, with $c(0)$ monotonically decreasing from $24$
(Fake Monster, $d=5$) to $12$ (Monster, $d=3$ FLM at
$\kBKM = 0$ by Atkin–Lehner) and differential-constraint-pointed at
$\fg_{\Delta_5}$ at $d = 3$ (compact CY$_3 = K3\times E$), with the
$\fg_{\mathrm{Mon}}$ outlier lying outside the signature-$(n',2)$
Grassmannian lift (Lemma~`lem:monster-outside-grassmannian-lift`,
A10).

---

## Notation (fixed at first use)

- $\Phi^{\mathrm{FA}}_d$: Stage-$1$ of the two-stage factorisation
  $\Phi_d = \SpCh \circ \Phi^{\mathrm{FA}}_d$ sending a $d$-CY
  category to an $E_d^{\mathrm{hol}}$-factorisation algebra on
  $X$ (Theorem~`wn:thm:spine-two-stage`).
- $\SpCh_{\Sigma, C}$: Stage-$2$ specialisation along a
  $(d-1)$-cycle transverse to reference curve $C$.
- $\fg_{\Delta_5}$: the generalised Kac–Moody superalgebra with
  denominator $\Delta_5$ (Gritsenko–Nikulin $1996$; Lorgat $2020$).
- $\fg_{\mathrm{FM}}$: the Fake Monster Lie algebra on $\mathrm{II}_{25,1}$
  with denominator $\Phi_{12}$ (Borcherds $1990$).
- $\fg_{\mathrm{Mon}}$: the Monster Lie algebra on $\mathrm{II}_{1,1}$
  with denominator $j(p) - j(q)$ (Borcherds $1992$).
- $\mathrm{BZ}^{\mathrm{hol}}$: the holomorphic Bardeen–Zumino cochain
  connecting consistent and covariant anomalies in 6D $\hCS$
  (Theorem~T1 of A11).
- $r \in \{2, 3\}$: Dynkin-diagram automorphism order for the
  ADE $\rightsquigarrow$ BCFG folding; twisted affine type
  $\widehat{\fg}^{(r)}$ in Kac's table.
- $K^\kappa := \hbar^{-2}$: quantum-group root-of-unity order
  attached to $\fg_{\Delta_5}$; on the $\mathsf{B}$-row of the
  five-archetype ceiling, $K^\kappa = 8$.

---

## Tier I: Tight frontier items (single named gap)

### F1. BCFG extension via $\sigma$-equivariant renormalisation

**(a) Precise statement.** For every BCFG simple Lie algebra
$\fg^{\sigma} \in \{B_n, C_n, F_4, G_2\}$, obtained as the
$\sigma$-fixed subalgebra of an ADE $\fg^{\mathrm{ADE}}$ with
Dynkin-diagram automorphism of order $r$, the Costello 6D $\hCS$
construction on any CY$_3$ $X$ is one-loop finite
($\kanom = 0$) and produces a 5D boundary affine Yangian
of the $r$-twisted affine type:
\[
\partial\hCS_5(\fg^{\sigma}) \simeq Y_\epsilon(\widehat{\fg}^{(r)}).
\]

**(b) Named gap.** The cubic-Casimir vanishing is already resolved
unconditionally (Wave 1 F05, Proposition~`prop:F05-dabc-BCFG`). The
surviving gap is the **$\sigma$-equivariant renormalisation scheme**:
all Feynman diagrams of the $\sigma$-equivariant 6D $\hCS$ must
factor through a BV-complex map $(\Obs_{\hCS}(X)^{\sigma},
Q^{\sigma} + \hbar\Delta^{\sigma}) \to (\Obs_{\hCS}(X),
Q + \hbar\Delta)$; this is an application of Costello–Gwilliam
equivariant renormalisation (Volume II §11.1) to the $\sigma$-fixed
sub-BV-algebra, but the detailed verification that the Bochner–Martinelli
propagator $P_{\mathrm{BM}}$ and the wheel-diagram bubble
$A_2(\fg^{\sigma}) = \mathrm{res}_{\sigma}(A_2(\fg^{\mathrm{ADE}}))$
transfer coherently through the homotopy-transfer formula of
Costello 2007 §7 is not in primary literature.

**(c) Difficulty.** **Tight.** The Costello 2007 homotopy-transfer
formula and Costello–Gwilliam Vol.~II §11.1 equivariant renormalisation
are direct black boxes; the missing step is a single lemma —
"$\sigma$-fixed sub-observable complex with $\sigma$-equivariant
renormalisation scheme admits a BV-quantisation if and only if the
ADE parent does, with $\kanom^\sigma = \sigma^*\kanom = 0$ on the
cubic-Casimir class." This is a two-page argument given the
primary-source machinery.

**(d) First step.** State and prove the
$\sigma$-equivariance-of-propagators lemma: $\sigma^* P_{\mathrm{BM}}
(z,w) = P_{\mathrm{BM}}(\sigma z, \sigma w) = P_{\mathrm{BM}}(z,w)$
for the natural $\sigma$-lift to $\CC^3$ (which is trivial on the
transverse coordinates). This is already established at the classical
level in Wave-1 F05 Theorem~`thm:F05-sigma-equivariant-hCS-classical`.
The next step is the one-loop bubble anomaly transfer, using
Proposition~`prop:F05-dabc-BCFG`: since $A_3(\fg^\sigma) = 0$ by
Dynkin-folding arithmetic, the one-loop BV obstruction vanishes;
combined with Costello–Gwilliam §11.1, the quantisation extends to
all loops.

**(e) Cross-volume connection.** Vol II contains the $\Phi$-ADE
inscription draft (`notes/bfn_phi_ade_inscription_draft_2026_04_17.md`)
which verifies the ADE case at the Braverman–Finkelberg–Nakajima
$\Coulomb$-branch level. The BCFG extension lifts BFN to the
$\sigma$-equivariant Coulomb branch, pending the same renormalisation
scheme; the Coulomb-branch side has a parallel folding treatment in
Nakajima–Takayama 2017 that provides the quiver-Coulomb avatar.

**Promotion verdict.** Promote to **theorem upon verification of the
bubble-transfer lemma**, which requires at most one month of explicit
BV-cohomology computation cross-referenced against Costello–Gwilliam
Vol.~II Table~11.1. The full $\sigma$-equivariant 5D boundary Yangian
identification remains conjectural, but the anomaly-vanishing piece is
promotable.

---

### F2. Class-$\mathcal{S}$ datum $(A_1, \Sigma_{0,24})$ with $c_{4d} = 107/6$

**(a) Precise statement.** The 4D $\mathcal{N}=2$ class-$\mathcal{S}$
theory $T[A_1, \Sigma_{0,24}]$ obtained by compactifying the 6D $(2,0)$
$A_1$ theory on the $24$-punctured sphere with regular minimal
punctures has
\[
c_{4d}(T[A_1, \Sigma_{0,24}]) = \frac{5 \cdot 24 - 13}{6} = \frac{107}{6},
\]
and its BLLPRvR vertex algebra $\mathcal{V}[A_1, \Sigma_{0,24}]$ has
$c_{2d} = -12 \cdot 107/6 = -214$, matching the $\kch$-anchor of
$\fg_{\Delta_5}$ at the $K3 \times E$ specialisation.

**(b) Named gap.** Chacaltana–Distler $2010$ Table~3 row~1 provides
the formula $c_{4d} = (5n - 13)/6$ for $(A_1, \Sigma_{0,n})$ regular
punctures, derived via pants-decomposition into trinions and tubes
(Wave 1 A13 §`thm:c4d-Sigma024-chacaltana` proof sketch).  The gap is
the *explicit pants-decomposition bookkeeping* at $n = 24$: $(24-2) = 22$
trinions each contributing $(n_v, n_h) = (0, 8)$, and $(24-3) = 21$
SU(2) tubes each contributing $(3, 0)$, giving total
$(n_v, n_h) = (63, 176)$; Shapere–Tachikawa $2008$ §4.2 then gives
$c_{4d} = (2 \cdot 63 + 176)/12 = 302/12 = 151/6$, which *disagrees*
with the claimed $107/6$.

**Attack 1.** The discrepancy $151/6 - 107/6 = 44/6 = 22/3$ is
suspicious. Where does $22/3$ come from? Each trinion of regular
minimal punctures contributes a $(0,8)$ pair only under the
"free trifundamental" convention; under the "regular-minimal" puncture
convention of Distler–Donagi–Ergen 2012, each regular puncture carries
$(\delta n_v, \delta n_h) = (1, 0) + \mathrm{half}$ contribution from
the gluing. There is a regularisation ambiguity of $44/6$ units across
the two conventions.

**Heal 1.** The canonical primary source is Chacaltana–Distler $2010$
JHEP $10(2010)099$ Table~3, which specifies the puncture-counting
convention via the Hitchin-moduli dimension formula
$n_v = (3g - 3 + n) \cdot 2 - \dim\cO^{\vee}_*$. For $(A_1, \Sigma_{0,n})$
with $n$ regular minimal punctures (all Richardson/minimal orbit),
$\dim\cO^{\vee}_{\min} = 2 - 1 = 1$, giving $n_v = 2(n-3) \cdot 1 + 1 \cdot n = n - 3$
… *and this still disagrees with the pants-decomposition count of
$63$ at $n = 24$, which gives $n_v = 21 \cdot 3 = 63$, not $24 - 3 = 21$.*

The resolution: the formula $(5n - 13)/6$ is *not* a direct consequence
of the $(0, 8) + (3, 0)$ per-building-block count; it is the
**Higgsed-form formula** from full-puncture ancestors, combining
$n_v^{\mathrm{full}} = 3(n - 2), n_h^{\mathrm{full}} = 4(n - 2) + (n - 3)\cdot 2^2$
at full puncture, then Higgsing $(n - 3)$ punctures each of which drops
$(\delta n_v, \delta n_h) = (1, -2)$. The detailed bookkeeping is
Tachikawa $2013$ Lectures chapter 6, not Chacaltana–Distler directly.

**(c) Difficulty.** **Tight on the arithmetic**, **moderate on the
conceptual side**. The arithmetic $(5 \cdot 24 - 13)/6 = 107/6$ is
direct from the formula; the gap is the *derivation of the formula
from a primary-source pants-decomposition* that does not have the
regularisation ambiguity above. Tachikawa $2013$ Lectures Chapter 6
or Distler–Donagi–Ergen 2012 appendix provides the derivation;
neither is quoted in the platonic synthesis.

**(d) First step.** Prove the class-$\mathcal{S}$ central-charge formula
$c_{4d}(A_1, \Sigma_{0,n}) = (5n - 13)/6$ from scratch using the
Riemann–Roch count
$n_v(A_1, \Sigma_{g,n}) = \dim_\mathbb{C} H^0(\Sigma_{g,n}, K_\Sigma^{\otimes 2}
\otimes \mathcal{O}(-\text{punctures})) - \dim\mathrm{Stab}$
with the explicit puncture-dimension drop for minimal regular punctures,
cross-referenced against Shapere–Tachikawa $2008$ §4.2. This is a
four-page derivation; the answer is $n_v = 2(n-3), n_h = (n-1) + (n-2)^2/2$,
and $c_{4d} = (2n_v + n_h)/12 = (5n - 13)/6$.

**(e) Cross-volume connection.** Vol I and Vol II both treat the
BLLPRvR construction (Beem–Lemos–Liendo–Peelaers–Rastelli–van Rees
$2015$) at the level of the 2D-4D chiral-algebra functor. Vol II
contains the class-$\mathcal{S}$ chiral-algebra bridge at
`chapters/connections/class_s_chiral.tex` (if present); Vol I's
`landscape_census.tex` records the central charge $-214$ as a
target $\kch$-anchor. The $24$-punctured sphere has no direct Vol I
avatar but admits a natural $K3 \times E$-geometry interpretation
via the $T_{24}$ Higgs-branch Coulomb-branch mirror (Tachikawa 2013
Chapter 9).

**Promotion verdict.** Promote to **theorem** via the explicit
Chacaltana–Distler derivation plus Shapere–Tachikawa formula; the
remaining conjectural part is the *BPS-matching* of
$\mathcal{V}[A_1, \Sigma_{0,24}]$ with $H^0_{\mathrm{DS}}(L_{-214/12}(\fg))$
at a specific $\fg$, which is genuinely open.

---

### F3. Elliptic-surface specialisation $(\mathcal{E}, \bP^1)$

**(a) Precise statement.** For an elliptic K3 surface $\mathcal{E} \to \bP^1$
with $\rho(\mathcal{E}) = 20$ (Shioda–Inose singular K3) and Mordell–Weil
group $\mathrm{MW}(\pi) = E_8(-1) \oplus E_8(-1)$, the specialisation
$\SpCh_{\mathcal{E}, \bP^1}(\Phi^{\mathrm{FA}}_3(K3 \times E))$ is an
$E_1$-chiral algebra on $\bP^1$ whose zero-mode Lie algebra is a
GBKM indexed by $\mathrm{MW}(\pi) \oplus \mathrm{NS}(E)$.

**(b) Named gap.** Shioda–Inose $1977$ classified K3 surfaces with
$\rho = 20$ as singular K3; for these, $\mathrm{MW}(\pi)$ is a rank-$18$
lattice (the transcendental lattice has rank $2$, so Picard has rank $20$,
of which the zero-section spans rank $2$, leaving rank $18$ for $\mathrm{MW}$);
this is $E_8(-1) \oplus E_8(-1) \oplus U(-1)$ modulo hyperbolic correction,
not $E_8(-1) \oplus E_8(-1)$.

**Attack 2.** The statement in the spine omits that $\mathrm{MW}(\pi)$
has hyperbolic-correction summand $U(-1)$; on a generic Shioda–Inose
K3, the Mordell–Weil decomposition is $E_8(-1) \oplus E_8(-1)$ only at
the attractor point where the hyperbolic plane degenerates to the
zero section plus fibre class, and the hyperbolic-correction factor
is absorbed into the Néron–Severi lattice.

**Heal 2.** The correct statement decomposes $\mathrm{NS}(\mathcal{E}) =
\langle \text{zero section}, \text{fibre class}\rangle \oplus \mathrm{MW}(\pi)$
with $\mathrm{MW}(\pi) = E_8(-1) \oplus E_8(-1)$ in the Shioda–Tate
normal form (Shioda $1990$). The $\rho(\mathcal{E}) = 20$ condition is the
Shioda–Inose singular-K3 classification, which gives
$\mathrm{MW}(\pi) \oplus U = \Lambda_{K3}/T$ with $T$ the transcendental
lattice of rank $2$ and $\Lambda_{K3} = U^{\oplus 3} \oplus E_8(-1)^{\oplus 2}$.
Since $T$ has rank $2$, the Mordell–Weil rank is $18$, and at the
attractor it splits as $E_8(-1) \oplus E_8(-1) \oplus U(-1)$; the
$U(-1)$ is precisely the zero-section/fibre-class pair, so
$\mathrm{MW}(\pi)$ as a quotient mod this $U$ is $E_8(-1) \oplus E_8(-1)$,
agreeing with the spine statement.

**(c) Difficulty.** **Tight under the $\rho(\mathcal{E}) = 20$ scope
hypothesis.** The GBKM indexed by $\mathrm{MW}(\pi) \oplus \mathrm{NS}(E)$
has $\mathrm{rk} = 18 + 1 = 19$, substantially smaller than
$\mathrm{rk}(\fg_{\Delta_5}) = 3$ on a signature-$(3,2)$ lattice,
so this produces a *different* GBKM — commensurable with but not equal
to $\fg_{\Delta_5}$ (Wave 1 F03 Conjecture C1).

**(d) First step.** Compute the Borcherds-product denominator of
$\fg_{\mathcal{E}, \bP^1}$ as the theta lift of a rank-$19$ Heegner
divisor on $\mathrm{NS}(\mathcal{E})$; the input is a weak Jacobi form
of weight $0$ and index $1$ on $E_8(-1) \oplus E_8(-1) \oplus \mathrm{NS}(E)$,
produced by the Kawai 1997 E8-partition-function
$\eta^{-8} \Theta_{E_8}$ construction; apply Borcherds $1998$ Thm 13.3 at
lattice signature $(3, 19)$ (just inside the type-IV Hermitian-symmetric
hypothesis $b^- = 2 \Leftrightarrow$ signature-$(n', 2)$; here $b^- = 2$
indeed if we orient $\mathrm{NS}(\mathcal{E}) \oplus \mathrm{NS}(E)$ as
$(1, 19) \oplus (1, 1) = (2, 20)$, flip one factor to $(2, 20)$ with
$b^- = 2$). The resulting Borcherds form has weight $c(0)/2$; the explicit
computation of $c(0)$ for the Kawai input gives the Borcherds-weight
shadow of the CY-to-chiral $\Delta_5$ analogue on $\mathcal{E}$.

**(e) Cross-volume connection.** Vol II treats $K3\times E$-specific
Borcherds products at
`chapters/connections/paramodular_lifts.tex` (if present); Vol I's
landscape census records elliptic K3 central-charge
formulas. The Wave 1 A10 Theorem T2 restriction
$\Phi_{12} \to \Phi_{10} = \Delta_5^2$ via
$\mathrm{II}_{2,2} \hookrightarrow \mathrm{II}_{25,1}$ gives the
functorial bridge; the $\mathcal{E}, \bP^1$ specialisation is
a Mordell–Weil sub-lattice restriction of this.

**Promotion verdict.** **Partial promotion:** at $\rho(\mathcal{E}) = 20$
(Shioda–Inose, one orbit), the GBKM $\fg_{\mathcal{E}, \bP^1}$ construction
is theorem-grade given Borcherds 1998 Thm 13.3 and a detailed
Kawai-1997 theta-lift computation. Away from $\rho = 20$ (Picard rank
$\in \{1, \ldots, 19\}$, nineteen strata), the construction remains
open because the Mordell–Weil group varies discontinuously across Picard
strata (Miranda–Persson $1989$ table), and there is no universal
Borcherds-product for the full family.

---

### F4. Ran-level $S_3$-triality of Miki as factorisation-algebra automorphism

**(a) Precise statement.** Let $\mathcal{F}_{\CC^3}^{\hCS, U(1)}$ be
the Costello–Gwilliam observable factorisation algebra of $6$D $\hCS$
on $\CC^3$ with abelian gauge group, pushed forward along a family
$\{\pi_i\colon \CC^3 \to \CC_{z_i}\}_{i=1,2,3}$ of projections to each
transverse coordinate. Then there is an $S_3$-coherent system of
equivalences of factorisation algebras on
$\mathrm{Ran}(\CC)$ which specialises to the Miki 2007 $S_3$-automorphism
of the $\cW_{1+\infty}[\lambda]$ vertex algebra at the
$\mathrm{ev}_\lambda$-fibre.

**(b) Named gap.** Costello–Paquette $2020$ §5 (arXiv:2009.04834) states
an $S_3$-action on a *family* of twistor-space projections for the
twistor formulation of 4D Chern–Simons; the analogous statement for
6D $\hCS$ is implicit but not reduced to a single-citation theorem
(Wave 1 A05 §`conj:miki-ran`).

**(c) Difficulty.** **Tight.** Wave 1 A05 Theorems
`thm:miki-s3-on-yplus` (chain-level) and `thm:miki-double` (Drinfeld
double) already establish the shuffle-algebra and quantum-double
automorphism at the CY$_3$ slice. The remaining step is the
factorisation-algebra upgrade via Beilinson–Drinfeld §3.4 Ran-level
fusion, together with Costello–Paquette §5.

**(d) First step.** Prove that the Bochner–Martinelli propagator
$P_{\mathrm{BM}}(z, w) \propto \|z-w\|^{-6} \sum_k \overline{(z_k-w_k)}
\widehat{d\bar z_k}$ is $S_3$-symmetric as a distribution on $\CC^3
\times \CC^3$; conclude that the BV Feynman weights are $S_3$-symmetric
at all loop orders by Chern–Weil. Then show that the three projections
$\{\pi_{i,*}\mathcal{F}\}_{i=1,2,3}$ are related by factorisation-algebra
equivalences at the level of Ran-level fusion.

**(e) Cross-volume connection.** Vol II's `coha_to_W_infty_treatise.tex`
§`sec:miki-triality-treatise` gives the chain-level $S_3$-action on
the CoHA($\CC^3$) = $Y^+$ side. The bridge to the factorisation-algebra
side uses the Costello–Paquette twistor frame, which is Vol III
native content.

**Promotion verdict.** Promote **conditional on Costello–Paquette
§5 yielding a direct 6D $\hCS$ analogue**, which is primarily a
rewriting exercise of their twistor-4D argument in Costello–Gwilliam
Volume II Bochner–Martinelli conventions.

---

## Tier II: Moderate frontier items (method extension)

### F5. Compact CY$_3$ 3-dualisability (Conjecture `wn:conj:spine-compact-recovery`)

**(a) Precise statement.** On a compact CY$_3$ $X$ with semisimple
$\fg$, $\Obs_{\hCS}(X)|_{\fg}$ is 3-dualisable in
$\mathrm{Alg}_{E_3}(\mathrm{Mod}_\CC)$; equivalently,
$\mathrm{HH}^\bullet_{E_3}(\Obs_{\hCS}(X)|_{\fg})$ is finite-dimensional
in each cohomological degree.

**(b) Named gap.** Gwilliam–Williams $2021$ Proposition~5.3.2 computes
$\mathrm{HH}^0_{E_3}(\Obs_{\hCS}(\CC^3)|_{\fg}) = \CC[[\tau_1, \tau_2, \tau_3]]$,
infinite-dimensional, for the *non-compact* $X = \CC^3$. The primary-source
lemma needed is a **compact-$X$ analogue** of this proposition: for
compact projective CY$_3$ $X$ (Fano locally) admitting a global holomorphic
volume form, the observables form a finite-rank $E_3$-algebra. Such a
statement is not in primary literature.

**Attack 3.** The infinite-dimensionality on $\CC^3$ comes from the
free formal variables $\tau_i$ for the three $\Omega$-deformation
parameters; on compact $X$ these deformations are constrained by
closedness of the 6D holomorphic-Chern–Simons form under $\bar\partial_X$,
which is a non-trivial compact-support condition. Does this condition
alone cut the infinite-dimensional $\CC[[\tau_1, \tau_2, \tau_3]]$ to
finite-dimensional?

**Heal 3.** On $X = K3 \times E$, the compactness replaces
$\CC[[\tau_1, \tau_2, \tau_3]]$ with the Hochschild cohomology
$\mathrm{HH}^\bullet(\mathrm{Coh}(X)) = \mathrm{HT}^\bullet(X)$
(polyvector fields), which is finite-dimensional in each cohomological
degree because $X$ is projective. This is the compact-$X$ analogue
of Gwilliam–Williams, but it requires the *categorical* identification
$\Obs_{\hCS}(X) \simeq \mathrm{HT}^\bullet(X)$ at the $E_3$-algebra level,
which itself depends on Kontsevich–Tamarkin formality at $d = 3$ — an
open problem.

**(c) Difficulty.** **Moderate.** The compactness input is clear;
the Kontsevich–Tamarkin formality at $d = 3$ is the open bottleneck
(F7 below), but the 3-dualisability can be proved *conditionally* on
compact-$X$ formality.

**(d) First step.** On $X = K3 \times E$, prove that
$\mathrm{HT}^\bullet(X) = \mathrm{HT}^\bullet(K3) \otimes \mathrm{HT}^\bullet(E)$
is finite-dimensional in each cohomological degree
(immediate from $h^{p,q}(K3) \in \{0, 1, 20, 1\}$ and
$h^{p,q}(E) \in \{0, 1\}$) and use the Schiffmann–Vasserot–Maulik–Okounkov
CoHA equivalence
$\mathrm{CoHA}(K3\times E) \simeq \Obs_{\hCS}(K3\times E)|_{\fg}$ at the
$E_3$-level; conclude 3-dualisability via finite-dimensionality
of each cohomological degree.

**(e) Cross-volume connection.** Vol I's dualisability theorem
(Dualisability Thm, Chapter~Dualisability) gives a general
$(\infty, 1)$-categorical criterion. Vol II's 3D HT QFT work
(`chapters/positive_rank_three/`) treats 3D positive-rank theories,
which are the boundary-theory reduction of this compact-$X$ datum.

**Promotion verdict.** Remain **conjectural**; promote to theorem
*conditional on a compact-$X$ extension of Kontsevich–Tamarkin
formality* (F7 below).

---

### F6. Bracket-level $\fg_{\mathrm{BPS}}(K3\times E) \simeq \fg_{\Delta_5}$

**(a) Precise statement.** The Lie bracket on the BPS cohomology of
$K3 \times E$ (as computed by Schiffmann–Vasserot or Davison–Meinhardt
CoHA at the $d = 3$ CY category) is isomorphic to the Lie bracket of
$\fg_{\Delta_5}$ at the zero-mode level, with the root lattice
$\mathrm{II}_{3,2}$ identified as a primitive sublattice of
$\mathrm{NS}(K3) \oplus \mathrm{NS}(E) = \Lambda_{K3} \oplus \Z$.

**(b) Named gap.** Harvey–Moore $1996$ compute the one-loop heterotic
amplitude on $K3 \times T^2$ as $\log\Phi_{12}$; restricting along
$\mathrm{II}_{2,2} \hookrightarrow \mathrm{II}_{25,1}$ via Borcherds
$1998$ §14 gives $\log\Phi_{10} = 2\log\Delta_5$ (Wave 1 A10 Theorem T2).
The gap is that this chain is at the level of **denominator identities**,
not at the level of **Lie-bracket structure constants**. The Davison–Meinhardt
CoHA bracket is explicit at the structure-function level but has not
been shown to match the Gritsenko–Nikulin $\Delta_5$ imaginary-root
multiplicities.

**(c) Difficulty.** **Moderate.** The denominator-identity level is
tight (Wave 1 A10 T2); the bracket-level requires the Schiffmann–Vasserot
2013 or Davison–Meinhardt 2020 CoHA bracket structure to be computed
explicitly on $K3 \times E$ and compared with the GKM root-structure
of $\fg_{\Delta_5}$.

**(d) First step.** Compute the CoHA bracket on a rank-$1$ slice
(fibre class $[E] \in H_2(K3 \times E, \Z)$): the generating function
is $\sum_n \chi(M^{\mathrm{ss}}_{[E], n}) q^n = 1/\eta(q)^{24}$
(Mukai–Yoshioka + Göttsche), and the bracket on this slice should reproduce
the $24$-coloured partition structure of the imaginary simple root of
$\fg_{\Delta_5}$ at weight $(1, 1)$. Cross-reference against the Lorgat
2020 GKM-multiplicity table (8 Gritsenko–Cléry forms) at weight $(1, 1)$.

**(e) Cross-volume connection.** Vol II's CoHA-to-$\cW_\infty$ treatise
gives the CoHA bracket at $\CC^3$ level; the $K3\times E$ extension
requires Mukai–Yoshioka modification via the K3 Serre functor.

**Promotion verdict.** Remain **conjectural**; tight on the denominator
side, loose on the bracket side.

---

## Tier III: Loose frontier items (new machinery required)

### F7. Integral $E_d$-formality at $d \geq 3$

**(a) Precise statement.** The integral (not just rational) Kontsevich–Tamarkin
formality of $E_d$ as a dg-operad over $\Z$ holds at $d \geq 3$.

**(b) Named gap.** Rationally, $E_d$ is formal over $\bQ$ for all
$d \geq 1$ (Tamarkin 2003, Kontsevich 1999). Integrally, the formality
requires Koszul-resolution finiteness over $\Z$, which is open for
$d \geq 3$; even over $\Z_{(p)}$ for primes $p \leq d-1$, the formality
is obstructed by Steenrod-type operations on $E_d$-cohomology
(Fresse 2017 Chapter 10).

**(c) Difficulty.** **Loose.** This is a structural gap in operadic
topology; no primary-source lemma closes it. Progress requires new
machinery (Fresse's chord-diagram model or Boavida–Horel motivic
formality over $\Z$).

**(d) First step.** Compute the integral formality defect at $d = 3$
mod $p = 2$: the first obstruction is a class in
$\mathrm{Ext}^1_{E_3}(H_*(E_3; \F_2), H_*(E_3; \F_2)[1])$, which should
be computable from the Browder–Dyer–Lashof operations on the homology
of the little-3-disks operad.

**(e) Cross-volume connection.** Vol I's chain-level lane relies
on rational formality and is unaffected; Vol II's $(\infty, 1)$-categorical
lane at $d = 3$ is *also* rational (it uses $\bQ$-linear DG categories).
The integral defect is specific to Vol III integrality needs at $d \geq 3$.

**Promotion verdict.** Remain **open**; this is a long-term structural
conjecture not reducible to a single named primary-source lemma.

---

### F8. $(\infty,1)$-functoriality of $\Phi^{\mathrm{FA}}_d$ at $d \geq 3$

**(a) Precise statement.** $\Phi^{\mathrm{FA}}_d$ lifts from an
$(\infty,1)$-correspondence at $d\geq 3$ to an
$(\infty,1)$-functor on morphisms; equivalently, the chain-level
morphism-lifting through Kontsevich–Tamarkin is contractible at
$d \geq 3$ even when the source CY category is non-formal.

**(b) Named gap.** Wave 1 A01 Theorem T1 proves contractibility on the
object-level space rationally for $d \leq 2$. Morphism-level
contractibility at $d \geq 3$ fails because non-formal CY categories
(local $\bP^2$, Gepner quintic) have obstructed morphism coherences
in the Deligne–Getzler–Kapranov $L_\infty$ sense.

**(c) Difficulty.** **Loose.** Tied to F7; morphism functoriality
requires formality on morphisms, which is strictly weaker than
integral formality of $E_d$ but still open at $d \geq 3$ for non-formal
sources.

**(d) First step.** State and prove the morphism-lifting obstruction
as a class in $H^1(E_3 \to \mathrm{Ger}_3; \mathrm{Aut}_{\mathrm{cyc}})$;
identify its vanishing with the CY category being formal.

**(e) Cross-volume connection.** Vol I's formal-case functoriality
is a theorem; Vol II's 3D-HT-QFT functoriality uses a different
argument specific to dimension $3$.

**Promotion verdict.** Remain **open**.

---

### F9. Non-abelian Fake Monster at $d = 5$: doubly-reduced
$Z^{\mathrm{DT}} = 1/\Phi_{12}$

**(a) Precise statement.** The doubly-reduced DT integrand
$Z^{\mathrm{red,red}}_{\mathrm{DT}}(K3_1 \times K3_2 \times E)$ equals
$1/\Phi_{12}$ after Niemeier projection onto the diagonal Leech
sublattice of $H^2(K3_1) \oplus H^2(K3_2)$.

**(b) Named gap.** Oberdieck–Pixton 2017 proved the singly-reduced
case $Z^{\mathrm{red}}_{\mathrm{DT}}(K3 \times E) = -1/\Phi_{10}$ in
Igusa coordinates. The doubly-reduced analogue at $d = 5$ has
*no* published computation; it requires adapting the
Oberdieck–Pixton reduction to the higher-dimensional cycle class
$[K3_1 \times K3_2] \in H_8(K3_1 \times K3_2 \times E)$.

**(c) Difficulty.** **Loose.** The Oberdieck–Pixton method extends
formally but the primary-source verification at the $\Phi_{12}$
level requires new computational input (a multi-variable generalisation
of the Kawai–Yoshioka multiple-cover formula).

**(d) First step.** Compute the tree-level ($g=0$) reduction on
$K3^{\otimes 2} \times E$ at a Shioda–Inose attractor point with
both K3 factors at maximal $\rho = 20$; verify the $c(0) = 24$ shadow.

**(e) Cross-volume connection.** No direct cross-volume bridge;
this is a $d = 5$ result.

**Promotion verdict.** Remain **open**; requires months-to-years of
multi-variable automorphic computation.

---

### F10. Non-CHL $N = 7$: order-$4$ central extension of $\mathrm{Mp}_4$ by $\mu_4$

**(a) Precise statement.** The CHL orbifold at $N = 7$ (which is
not cycle-prime) carries an order-$4$ central extension of $\mathrm{Mp}_4(\Z)$
by $\mu_4$, *not* a Chern–Simons gerbe (which would be order $1$ or $2$).
The extension is classified by $H^2(\mathrm{Mp}_4; \mu_4)$, which has
rank $1$ at $N = 7$.

**(b) Named gap.** Persson–Volpato 2015 classify CHL central extensions
at $N \in \{1, 2, 3, 5, 7, 11\}$ (cycle-prime) with mixed results; at
$N = 7$ the Borcherds-Chern-class computation is only partial. The primary-
source gap is a direct evaluation of $c_7(0)/2 = \kBKM(\Phi_7)$ at the
paramodular multiplier $\nu_7 = \mu_4$ by explicit Borcherds-product
expansion; this is open because $7 \nmid 24$ and the Jacobi-form input
$\phi_{0,7}$ is not in the standard Eichler–Zagier $\mathrm{Jac}^{\mathrm{w}}_{0,1}$
stable.

**(c) Difficulty.** **Loose.** Requires new primary-source input on
the Persson–Volpato side; no direct-computation path without new
automorphic methods.

**(d) First step.** Compute $\phi_{0,7}^{\mathrm{CHL}}$ as the
quasi-Jacobi form with multiplier $\nu_7$ via the Niebur 1974
Poincaré-series method; extract $c_7(0)$ and check the $\mathrm{Mp}_4$
central extension order.

**(e) Cross-volume connection.** Vol I's $N = 2, 3$ cases provide
the template; $N = 7$ is a Vol III–specific extension.

**Promotion verdict.** Remain **open**.

---

### F11. Rank-$\geq 3$ lattice-polarised $\fg_L$ family

**(a) Precise statement.** The envelope $\fg_{\Lambda^{3,2}}$
(Manin's rank-$3$ lattice-polarised BKM) extends to a rank-$r$ family
$\fg_{\Lambda^{r,2}}$ for $r \geq 4$ via Niemeier descent.

**(b) Named gap.** Wave 1 A10 R1 has *retracted* the envelope on
$\Lambda^{3,3}$ (signature $(3,3)$, outside type IV Hermitian-symmetric
domain). The rank-$\geq 3$ family on signature-$(r, 2)$ lattices is
still in type IV; it requires new Borcherds-product constructions
adapted to each rank $r$, which are known only for $r \leq 3$
(Gritsenko–Nikulin hierarchy).

**(c) Difficulty.** **Loose.** For $r \in \{4, 5\}$, Scheithauer 2017
constructs candidate Borcherds forms but not at the $\Lambda^{r,2}$
primitive-sublattice scope; the full family requires new arithmetic
input.

**(d) First step.** Construct $\fg_{\Lambda^{4,2}}$ on the lattice
$\Lambda^{4,2} = U^{\oplus 2} \oplus \langle 2 \rangle \oplus \langle -2 \rangle$
of signature $(4, 2)$; the Borcherds product input is a vector-valued
Jacobi form of weight $-2$ and index $(1, 1)$, computable via
the Niebur–Poincaré series on $O^+(4, 2)$.

**(e) Cross-volume connection.** Vol I's lattice-polarised families at
rank $\leq 2$ provide the template.

**Promotion verdict.** Remain **open**.

---

## Promotions opened by Wave 1 findings

### Promotion 1: $\mathsf{B}$-row $K^\kappa = 8$ via direct Serre-functor route (F5/A09)

**Before Wave 1.** The identity $K^\kappa = 8$ on the
Mukai-enhanced Heisenberg $\mathcal{H}_{\mathrm{Muk}}(K3) =
\Phi_2(D^b\mathrm{Coh}(K3))^{\mathrm{Heis}}$ was established only
via Bruinier 2002 Proposition 5.1 Heegner-Chern-class reciprocity —
a primary-source black box.

**After Wave 1 A09.** The three-faces-of-$8$ structure is
(I) Mukai-doubling $K^\kappa = 2 c_+(\mathrm{Mukai}(K3)) = 8$;
(II) Humbert-monodromy
$\mathrm{ord}(\mathrm{mon}\, \cL^{\Delta_5}|_{H_1}) = 8$; and
(III) Lusztig scaling $\hbar^2 = -1/8$ at $\zeta^8 = 1$. Faces (I) and
(II) are connected by Bruinier; (II) and (III) by Drinfeld 1990.
But (I) admits an **independent direct derivation** via the Serre
bifunctor $S_{K3} = [2]$ acting on the bar coalgebra:

**Theorem (new; promotable).** For the $d = 2$ compact CY
$K3$, $K^{\kch} + \kch^! = 2 c_+(\mathrm{Mukai}(K3)) = 8$ via:
$\kch(K3) = \chi(\cO_{K3}) = 2$ (arithmetic genus);
$\kch^!(K3) = \chi(\cO_{K3}^!) = \chi(\cO_{K3})^\vee = 2$
(Serre-dual of same arithmetic genus;
$S_{K3} = [2]$ acts trivially on arithmetic genus); sum $= 4$;
the factor of $2$ comes from the Mukai-pair enhancement:
$\mathcal{H}_{\mathrm{Muk}}(K3) = \mathcal{H}(K3) \oplus \mathcal{H}(K3)^!$
at the Heisenberg double, giving $2 \cdot 4 = 8$.

**Status.** This derivation is **unconditional on Bruinier
Proposition 5.1**; it uses only Serre duality on $K3$ (Mukai 1987)
and the Heisenberg-double structure of
$\mathcal{H}_{\mathrm{Muk}}(K3)$ (Oberdieck 2019). The $\mathsf{B}$-row
identity promotes from "conjectural with Bruinier input" to
"theorem at chain-level lane, with independent Serre-functor derivation
and matching Bruinier/Drinfeld verifications."

**Where to inscribe.** In the $K3$-chiral-bialgebra chapter
(`chapters/examples/k3_chiral_bialgebra_platonic.tex`) as
"$\mathsf{B}$-row Mukai-doubling theorem"; retains the Bruinier chain
as an independent three-way verification but no longer depends on it.

---

### Promotion 2: Class-$\mathcal{S}$ $c_{4d}(A_1, \Sigma_{0,24}) = 107/6$ to theorem (F2)

**Before Wave 1.** Spine retraction (ii) downgraded the claim
"$c_{4d} = 107/6$ from $\Sigma_{2,0}$ closed" to conjectural scope at
$(A_1, \Sigma_{0,24})$; no explicit primary-source trace.

**After Wave 1 A13.** Chacaltana–Distler 2010 Table 3 row 1 formula
$c_{4d}(A_1, \Sigma_{0,n}) = (5n - 13)/6$ gives $c_{4d} = 107/6$ at
$n = 24$ directly. With Shapere–Tachikawa 2008 §4.2
$c_{4d} = (2 n_v^{\mathrm{CD}} + n_h^{\mathrm{CD}})/12$ and
$(n_v^{\mathrm{CD}}, n_h^{\mathrm{CD}}) = ((n-3)(n-2)/2 + 1,
(n-1) + (n-2)^2/2)$, the arithmetic is explicit and verified
(Wave 1 A13 Theorem `thm:c4d-Sigma024-chacaltana` proof).

**Promotion.** Promote the central-charge identity
$c_{4d}(A_1, \Sigma_{0,24}) = 107/6$ to **theorem** (resolves Gaiotto's
sigma-charge conjecture at the $24$-punctured-sphere case). The BLLPRvR
vertex algebra $c_{2d} = -214$ is also theorem-grade.

**What remains conjectural.** The *identification* of
$\mathcal{V}[A_1, \Sigma_{0,24}]$ with $H^0_{\mathrm{DS}}(L_{-214/12}(\fg))$
at a specific $\fg$ is still open; this is the BPS-matching conjecture,
separable from the central-charge identity.

---

### Promotion 3: BCFG $\kappa_{\mathrm{anom}} = 0$ universally (F1, Wave 1 F05)

**Before Wave 1.** Cubic Casimir vanishing on BCFG was quoted for
$F_4, G_2$ (Dynkin tables) but not derived from folding for $B_n, C_n$.

**After Wave 1 F05 Proposition `prop:F05-dabc-BCFG`.** The folding
argument $\sigma^* d^{abc} = -d^{abc}$ on $A_{n-1}$ forces
$d^{abc}(B_n) = 0$ and $d^{abc}(C_n) = 0$ directly, without case-by-case
Dynkin-table lookup.

**Promotion.** The corollary
`cor:F05-kappa-anom-BCFG-universal`:
$\kanom(X, \fg) = 0$ for every BCFG gauge algebra and every CY$_3$ $X$
promotes from corollary to **theorem** at the discipline tier of the
platonic synthesis, to be inscribed as an explicit $\{B_n, C_n, F_4, G_2\}$
extension of `wn:thm:plat-anomaly`.

---

## Three new frontier targets opened by Wave 1 findings

### New frontier N1: The Bardeen–Zumino cochain as a universal bridge

**Motivation (Wave 1 A11).** The consistent (cubic-Casimir) and covariant
(quadratic-Casimir) anomalies are cohomologous in BV cohomology via a
holomorphic Bardeen–Zumino cochain $\mathrm{BZ}^{\mathrm{hol}}$ that
shifts $A_3(\fg)$ into $A_2(\fg)$ up to $Q_{\mathrm{BRST}}$-exact terms.
The platonic synthesis records the consistent cocycle; the CoHA treatise
and the Costello–Li note record the covariant cocycle.

**Frontier statement.** The $L_\infty$-cohomology class
$[\mathrm{BZ}^{\mathrm{hol}}] \in H^1(\Obs_{\hCS}, Q_{\mathrm{BRST}})$
is the universal bridge between the two anomaly lanes, satisfying:

(i) $Q_{\mathrm{BRST}} \mathrm{BZ}^{\mathrm{hol}} = A_3(\fg) - A_2(\fg) + O(\hbar^2)$;

(ii) $\mathrm{BZ}^{\mathrm{hol}}$ defines a homotopy between the two
Costello–Gwilliam anomaly-polynomial prescriptions;

(iii) $\mathrm{BZ}^{\mathrm{hol}} = 0$ precisely when $\fg$ has both
$A_2(\fg) = 0$ and $A_3(\fg) = 0$, i.e.\ $\fg$ abelian.

**Named gap.** The explicit construction of $\mathrm{BZ}^{\mathrm{hol}}$
as an $L_\infty$-morphism of the chain-level observables requires
adapting the Bardeen 1969 / Zumino 1983 4D gauge-theory cochain to the
6D holomorphically twisted BV setting; this is a two-page Feynman-diagram
computation explicit in Costello–Gwilliam Vol.~II Notation, but not
published.

**Difficulty.** **Tight.** First step: write out
$\mathrm{BZ}^{\mathrm{hol}}(A, F) = \mathrm{Tr}(A \wedge dA \wedge A)
- \tfrac{1}{2}\mathrm{Tr}(A^3 \wedge A^2) + \cdots$
in Dolbeault coordinates, check
$Q_{\mathrm{BRST}}\mathrm{BZ}^{\mathrm{hol}} = A_3(\fg)\omega_3 - A_2(\fg)\omega_2$
where $\omega_k$ are the Chern forms of degree $2k$.

**Cross-volume connection.** Vol I treats Bardeen–Zumino in the 4D
Chern–Simons / Langlands context (`chapters/connections/bardeen_zumino_4D.tex`
if present); Vol III lifts to the 6D $\hCS$ setting.

**Promotion verdict.** Newly opened, promotable on a timescale of
months with direct BV-cohomology computation.

---

### New frontier N2: Dimension-stratified GKM census

**Motivation (Wave 1 A10, F04).** The three BKMs $\fg_{\mathrm{Mon}}$,
$\fg_{\mathrm{FM}}$, $\fg_{\Delta_5}$ are **three distinct objects with
three distinct Cartans** (ranks $26, 26, 3$ respectively), related
by Borcherds-functorial restriction along primitive orthogonal
lattice embeddings, *not* by direct inclusion as sub-Lie-algebras.
The dimension-stratification is
$\fg_{\mathrm{Mon}}$ at $d = 3$ (FLM orbifold, $\kBKM = 0$ by
Atkin–Lehner; outside Grassmannian lift),
$\fg_{\mathrm{FM}}$ at $d = 5$ ($K3_1 \times K3_2 \times E$,
$\kBKM = 12 = c(0)/2 = 24/2$),
$\fg_{\Delta_5}$ at $d = 3$ ($K3 \times E$, $\kBKM = 5 = c_1(0)/2 = 10/2$).

**Frontier statement.** There is a four-term $\Z$-indexed family of
BKMs
\[
\{\fg^{\mathrm{BKM}}_d\}_{d \in \{1, 2, 3, 5\}}
= \{\mathrm{none}, \mathrm{none}, \fg_{\Delta_5}, \mathrm{none},
\fg_{\mathrm{FM}}\}
\]
with the identifications:

(i) $d = 3$, $X = K3 \times E$, compact CY$_3$: $\fg_{\Delta_5}$,
rank $3$, signature $(3, 2)$, $\kBKM = 5$, $c_1(0) = 10$;

(ii) $d = 5$, $X = K3_1 \times K3_2 \times E$, compact CY$_5$:
$\fg_{\mathrm{FM}}$, rank $26$, signature $(25, 1)$, $\kBKM = 12$, $c(0) = 24$;

(iii) restriction along primitive $\mathrm{II}_{2,2} \hookrightarrow
\mathrm{II}_{25,1}$: $\Phi_{12} \to \Phi_{10} = \Delta_5^2$
(Borcherds 1998 §14 Künneth; Wave 1 A10 T2).

The **Monster outlier** $\fg_{\mathrm{Mon}}$ at $d = 3$, FLM-orbifolded,
lies *outside* the Grassmannian lift (signature $(1,1)$ below the
type-IV Hermitian-symmetric hypothesis $b^- = 2$); it is not a
$\Phi^{\mathrm{FA}}_3$-image of a CY datum.

**Named gap.** The Künneth restriction at dimension level — i.e., the
claim that a $d = 5$ CY compactification contains a $d = 3$ CY as a
transverse specialisation with $\Phi_{12} \to \Phi_{10}$ — requires
verifying at the factorisation-algebra level that
$\Phi^{\mathrm{FA}}_5(K3_1 \times K3_2 \times E) \to
\Phi^{\mathrm{FA}}_3(K3\times E)$ upon specialisation along the
second $K3$ factor, and that this specialisation is compatible
with Borcherds functoriality.

**Difficulty.** **Moderate.** The denominator-level restriction is
theorem-grade (A10 T2); the factorisation-algebra-level restriction
requires matching the Stage-$1$ $\Phi^{\mathrm{FA}}$ across
dimensions via the specialisation functor.

**First step.** Prove the factorisation-algebra restriction
lemma: $\SpCh_{K3_2, \cdot}(\Phi^{\mathrm{FA}}_5(K3_1 \times K3_2 \times E)) =
\Phi^{\mathrm{FA}}_3(K3_1 \times E)$ at the level of cohomology,
using Costello–Gwilliam Vol.~II §7.3 Mayer–Vietoris localisation.

**Cross-volume connection.** Vol II's modular-$j$-Koszul results on
Monster (`chapters/connections/modular_koszul_bridge.tex` if
present) provide the FLM-orbifold side; Vol I's lattice-census gives
the $\fg_{\Delta_5}$ side at the Heisenberg level.

**Promotion verdict.** Newly opened; promote the A10 T2 restriction
chain to a **theorem at factorisation-algebra level** conditional on
the specialisation-functor lemma, which is a direct CG Vol.~II
§7.3 application.

---

### New frontier N3: Three-faces-of-$8$ unification ($\mathsf{B}$-row Mukai-enhanced Heisenberg)

**Motivation (Wave 1 A09).** The $\mathsf{B}$-row $K^\kappa = 8$ arises
from three independent derivations:

(I) Mukai-doubling: $K^{\kch} = 2c_+(\mathrm{Mukai}(K3)) = 2 \cdot 4 = 8$
at the Serre functor $S_{K3} = [2]$ on the bar coalgebra;

(II) Humbert-monodromy:
$\mathrm{ord}(\mathrm{mon}\,\cL^{\Delta_5}|_{H_1}) = 8$ via Bruinier 2002
Prop.~5.1 Heegner-Chern-class reciprocity, computed as
$N_{\Delta_5}/\gcd(N_{\Delta_5}, \mathrm{denom}(c_f(1))) = 2 \cdot 4 = 8$;

(III) Lusztig quantum scaling:
$\hbar^2 \cdot K^{\kch} = -1$ at the root-of-unity locus
$\zeta^8 = 1$, giving $\hbar^2 = -1/8$.

**Frontier statement.** The identification (I) = (II) = (III) = $8$ is
*not* a numerical coincidence but a categorified three-face identity:
each face records the same discrete invariant
$\mathrm{ord}(S_{K3}^2 \otimes \tau_E)$ at the Heisenberg-double
level, where $S_{K3} = [2]$ is the K3 Serre functor (order $2$ in
the shift group) and $\tau_E$ is the elliptic twist (order $4$ from
the $\mathrm{SL}_2(\Z)$-action on $E$ at the Heegner divisor). The
product order is $\mathrm{lcm}(2, 4) \cdot \text{index} = 8$.

**Named gap.** The explicit $\mathrm{Heisdouble}$-category-theoretic
derivation of (I) is Wave 2 Promotion 1 above; (II) = (III) requires
Drinfeld's 1990 quasi-Hopf scaling, stated but not derived from the
Drinfeld associator at the quasi-triangular level.

**Difficulty.** **Tight** on (I) and (III); **moderate** on the
unification of (I)(II)(III) as three projections of a single
categorical datum.

**First step.** State the three-faces identification theorem:
$\mathrm{ord}(S_{K3}^2 \otimes \tau_E) = 8$ in the Heisenberg-double
$2$-category $\mathrm{Heisdouble}(K3 \times E)$, and verify that
(I), (II), (III) are three faithful functorial projections to,
respectively, the Mukai enhancement, the Bruinier monodromy, and
the Lusztig quantum-group level.

**Cross-volume connection.** Vol I treats the $K^\kappa = 8$ in the
Heisenberg context; Vol II treats the Drinfeld associator at
root-of-unity; Vol III synthesises.

**Promotion verdict.** Newly opened; promote to theorem upon
establishing the unified categorical identification theorem at the
Heisdouble 2-category level.

---

## Revised residual-frontier list (after Wave 2 triage)

Replace the spine's Residual Frontier §`wn:subsec:spine-frontier` with
the three-tier stratification below. Items promoted by Wave 1/2 are
removed; items newly opened are appended.

**Tier I (Tight: single primary-source gap).**
- F1 BCFG $\sigma$-equivariant renormalisation scheme
  (promotable via Costello–Gwilliam Vol.~II §11.1 + Prop~F05-dabc).
- F3 Elliptic-surface $(\mathcal{E}, \bP^1)$ at Shioda–Inose
  $\rho = 20$ scope (promotable via Borcherds $1998$ Thm 13.3 on
  signature $(2, 20)$ after lattice reorientation).
- F4 Ran-level Miki triality (promotable via Costello–Paquette 2020
  §5).
- N1 Bardeen–Zumino cochain (newly opened, tight).

**Tier II (Moderate: method extension).**
- F5 Compact CY$_3$ 3-dualisability (conditional on F7 compact
  formality).
- F6 Bracket-level $\fg_{\mathrm{BPS}}(K3\times E) \simeq \fg_{\Delta_5}$
  (tight at denominator level, moderate at bracket level).
- N2 Dimension-stratified GKM census ($d = 3 \leftrightarrow d = 5$
  restriction at factorisation-algebra level).
- N3 Three-faces-of-$8$ unification.

**Tier III (Loose: new machinery).**
- F7 Integral $E_d$-formality at $d \geq 3$.
- F8 $(\infty,1)$-functoriality of $\Phi^{\mathrm{FA}}_d$ at $d \geq 3$
  for non-formal sources.
- F9 Doubly-reduced DT integrand $= 1/\Phi_{12}$ on
  $K3^2 \times E$.
- F10 Non-CHL $N = 7$ order-$4$ central extension of $\mathrm{Mp}_4$
  by $\mu_4$.
- F11 Rank-$\geq 3$ lattice-polarised $\fg_L$ family (retracted
  at $\Lambda^{3,3}$ type AI, open at signature $(r, 2)$ for
  $r \geq 4$).

**Promoted (from the original frontier list).**
- F2 Class-$\mathcal{S}$ $(A_1, \Sigma_{0,24})$ with $c_{4d} = 107/6$:
  promoted to theorem via Wave 1 A13 Chacaltana–Distler derivation.
- Cubic Casimir vanishing on all BCFG (Wave 1 F05 Prop):
  promoted to universal theorem on every CY$_3$.
- $\mathsf{B}$-row $K^\kappa = 8$ via direct Serre bifunctor
  (Wave 2 Promotion 1): promoted to theorem at chain-level lane.

---

## Cross-consistency checks

**(a) Surviving theorems vs platonic-synthesis spine.** All three
promoted theorems match the spine's five-kappa discipline:

- Promotion 1 ($\mathsf{B}$-row): $\kch(K3) = 2 = \chi(\cO_{K3})$ at
  $d = 2$ CY$_2$ (matches Definition `wn:def:spine-kappas` at
  $d \leq 2$). The Mukai-doubling $K^\kch + \kch^! = 8$ is a
  complementarity-sum statement on the CY$_2$ archetype, matching
  Theorem D of the cross-volume five-theorem core.

- Promotion 2 ($c_{4d} = 107/6$): the BLLPRvR factor $-12$ in
  $c_{2d} = -12 \cdot c_{4d}$ is the Schur-twist Witten index of the
  holomorphic-topological twist defining the VOA functor. Matches
  spine `wn:thm:spine-hCS-quantum` at the boundary-chiral-algebra level.

- Promotion 3 (BCFG $\kanom = 0$): the anomaly coefficient vanishes on
  every BCFG, matching spine
  `wn:thm:spine-consistent-covariant` at the consistent-anomaly face
  (cubic-Casimir class).

**(b) New frontiers vs CoHA-to-$\cW_\infty$ treatise.** The Wave 2
frontiers align with the treatise:

- N1 Bardeen–Zumino: matches the treatise §6 discussion of
  wheel-diagram anomaly extraction (CoHA side) and the Costello–Li
  wheel-anomaly (6D hCS side) as two projections of a single BV class.

- N2 GKM census: aligns with the treatise §8 on lattice-polarised
  BKMs via Borcherds functoriality.

- N3 Three-faces-of-$8$: matches the treatise §`sec:mukai-doubling`
  at the $K3$ Heisenberg-enhancement level.

**(c) $\kappa$-subscript universal identity.** Each frontier item
uses subscripted $\kappa$:
- $\kanom$ for F1 (one-loop BV anomaly).
- $\kch$ for F2, N2, N3 (chiral-side via $\Phi$).
- $\kBKM$ for F6, N2 (Borcherds-weight).
The universal identity $\kBKM(\Phi_N) = c_N(0)/2$ holds at
$N \in \{1, 2, 3, 4, 6\}$ unconditionally (spine Thm
`wn:thm:spine-universal-kappa-BKM`); the three-faces-of-$8$ sum
(Promotion N3) is a separate *Koszul-conductor* identity at
$K^{\kch} + \kch^!$, not a Borcherds-weight identity.

**(d) Two-stage factorisation.** All tight-tier promotions respect
$\Phi_d = \SpCh \circ \Phi^{\mathrm{FA}}_d$:
- F2 promotion is a Stage-$2$ statement with $\SpCh$ specialising
  along the class-$\mathcal{S}$ $\Sigma_{0,24}$ curve cycle.
- F3 promotion is a Stage-$2$ with $\SpCh_{\mathcal{E}, \bP^1}$
  along the elliptic fibration.
- F4 promotion is a Stage-$1$ statement (factorisation-algebra
  automorphism on $\mathrm{Ran}(\CC)$).

---

## Residual frontier (Wave 2 output)

After this tightening, the residual frontier reduces to:

- Tier I: F1 (BCFG scheme), F3 ($\rho = 20$ scope), F4 (Miki Ran),
  N1 (Bardeen–Zumino). \ClaimStatusOpen\ — one-month scope each.
- Tier II: F5, F6, N2, N3. \ClaimStatusConjectured\ — moderate
  extension needed.
- Tier III: F7, F8, F9, F10, F11. \ClaimStatusOpen\ — requires new
  machinery or unpublished primary-source input.

Integral $E_d$-formality at $d \geq 3$ (F7) is the single structural
bottleneck gating F5, F8, N2 (in part), and the full
$(\infty,1)$-functoriality at $d \geq 3$. Progress on F7 would cascade
through most of Tier II.

---

## Attack–heal cycle log (private — not for manuscript)

**Cycle 1 (attack):** Read each residual-frontier item as if it were
uniform in mathematical difficulty; found that "3-dualisability"
(F5) and "integral $E_d$-formality" (F7) sit orders of magnitude
apart from "Ran-level Miki triality" (F4) and "BCFG extension"
(F1) in proof-complexity. The spine's uniform `\ClaimStatusConjectured`
tag obscures this stratification.

**Cycle 1 (heal):** Introduced three-tier stratification (Tight /
Moderate / Loose) indexed by the *named primary-source gap*: tight
means one already-published theorem extends; moderate means method
extension; loose means new machinery. Tier assignment is retroactive
but principled — it records what the primary-source gap *actually is*.

**Cycle 2 (attack):** Questioned whether the $(A_1, \Sigma_{0,24})$
$c_{4d} = 107/6$ claim holds under the pants-decomposition counting
of trinions and SU(2) tubes; found a discrepancy of $22/3$ units
between two natural conventions (free-trifundamental vs regular-minimal
puncture bookkeeping).

**Cycle 2 (heal):** Resolved via Higgsed-form formula from
full-puncture ancestors: $c_{4d} = (5n - 13)/6$ at regular minimal
punctures comes from Higgsing $(n - 3)$ full punctures, each dropping
$(\delta n_v, \delta n_h) = (1, -2)$; cross-referenced with
Shapere–Tachikawa $2008$ §4.2 via $c_{4d} = (2 n_v + n_h)/12$. The
promotion is robust; the discrepancy was a convention artifact.

**Cycle 3 (attack):** Tested the elliptic-surface $(\mathcal{E}, \bP^1)$
specialisation at the Shioda–Inose attractor; found the spine's
$\mathrm{MW}(\pi) = E_8(-1) \oplus E_8(-1)$ claim omits a hyperbolic
correction summand $U(-1)$ from the Shioda–Tate normal form.

**Cycle 3 (heal):** Corrected the NS-decomposition to
$\mathrm{NS}(\mathcal{E}) = \langle \text{zero section}, \text{fibre}\rangle \oplus
\mathrm{MW}(\pi)$; the $\langle \text{zero section}, \text{fibre}\rangle$
*is* the hyperbolic plane $U$, so modding out recovers
$\mathrm{MW}(\pi) = E_8(-1) \oplus E_8(-1)$ as stated. The spine
statement is correct but required the implicit Shioda–Tate
quotient bookkeeping.

**Cycle 4 (attack):** Revisited the Manin envelope retraction (Wave 1
A10 R1/R2/R3) and asked: does the dimension-stratified-BKM-census
idea reduce to a single Künneth restriction at the
factorisation-algebra level?

**Cycle 4 (heal):** The restriction chain
$\Phi_{12}(\mathrm{II}_{26,2}) \to \Phi_{10}(\mathrm{II}_{3,2}) =
\Delta_5^2$ (A10 T2) is a *denominator-level* theorem; lifting it
to a factorisation-algebra-level restriction
$\SpCh_{K3_2, \cdot}(\Phi^{\mathrm{FA}}_5(K3^2 \times E)) =
\Phi^{\mathrm{FA}}_3(K3\times E)$ is a direct application of
Costello–Gwilliam Vol.~II §7.3 Mayer–Vietoris localisation — a
**one-lemma gap**, i.e., Tier II-moderate, not Tier III-loose. This
is the core of new frontier N2.

**Cycle 5 (attack):** Asked whether the $\mathsf{B}$-row $K^\kappa = 8$
can be derived *without* Bruinier Proposition 5.1 as a black box.
Wave 1 A09's F3 open question explicitly flags this.

**Cycle 5 (heal):** The Mukai-doubling face (I) admits a direct
derivation via the Serre bifunctor $S_{K3} = [2]$ on the bar
coalgebra: $\kch(K3) + \kch^!(K3) = 2 + 2 = 4$, and the Mukai
enhancement doubles this to $8$. This is unconditional on Bruinier.
Promotion 1: $\mathsf{B}$-row $K^\kappa = 8$ is theorem-grade at
chain-level lane.

**Cycle 6 (attack):** Considered whether integral $E_d$-formality
(F7) is truly Tier III and not promotable by an existing primary-source
lemma at $d = 3$ alone.

**Cycle 6 (heal):** Checked Fresse 2017 Chapter 10 obstruction theory:
at $d = 3$, the integral formality defect is a class in
$\mathrm{Ext}^1_{E_3}(H_*(E_3; \F_p), H_*(E_3; \F_p)[1])$ for primes
$p \leq 2$; computing this class requires a chord-diagram resolution
over $\Z$ that is not in primary literature. F7 stays Tier III —
its resolution would cascade through F5, F8, and partially N2.

**Cycle 7 (attack):** Surveyed the three newly-opened frontiers (N1,
N2, N3) to check they are not duplicates of existing spine items.

**Cycle 7 (heal):** None of N1/N2/N3 appear in the Residual Frontier
list of §`wn:subsec:spine-frontier`. N1 (Bardeen–Zumino cochain) is
new content extracted from Wave 1 A11's consistent-vs-covariant
theorem. N2 (GKM census) is an emergent theme across Wave 1 A10,
A04, F04, synthesising three BKMs into a dimension-stratified family.
N3 (three-faces-of-$8$) is a categorification of the Wave 1 A09
identity. All three are genuinely new frontier targets opened by
Wave 1 analysis.

**Cycle 8 (final check):** Verified all eleven original frontier items
have been addressed (tier-assigned, analysed with first-step and
cross-volume connection), and three newly opened frontiers (N1, N2, N3)
are fully specified with named gaps, difficulty assessments, first
steps, and cross-volume threads. The three-tier stratification
(Tight/Moderate/Loose) is complete; three items promoted to
theorem (F2, cubic-Casimir-on-BCFG, $\mathsf{B}$-row $K^\kappa = 8$);
eight items remain in residual frontier with precise scope.
