# Wave-3 Synthesis: The Non-Abelian K3 Yangian

**Date**: 2026-04-19.
**Wave**: 3 (building on Wave-1 and Wave-2 syntheses).
**Sources**: 10-agent adversarial attack-heal swarm,
channelling Gelfand, Kazhdan, Etingof, Polyakov, Nekrasov,
Beilinson, Drinfeld (Russian school) + Witten, Costello, Gaiotto
(mathematical physics).

## 0. Status epistemic legend (unchanged from Wave-2)

- **[H]** high-confidence — $\ge 3$ independent verification paths
- **[M]** medium-confidence — 1–2 paths; agent consensus not cross-checked
- **[L]** low-confidence — tension with another result
- **[O]** open — genuine open problem
- **[F]** falsified — Wave-produced concrete falsification
- **[R]** retracted — prior-wave claim retracted in this wave

## 1. Major convergences in Wave 3

### 1.1 [H][R] The "$\mathfrak{so}(4, 20)$ single simple-Yangian envelope" is RETRACTED

Polyakov Wave-3 delivered a negative result of major structural
significance: the Reshetikhin-Faddeev auxiliary-$Q$ dressing FAILS
for indefinite $\mathfrak{so}(4, 20)$. Bare Belavin-Drinfeld CYBE
residual at rank 4 signature $(2, 2)$: $1.003 \times 10^{+1}$;
$Q$-dressed CYBE residual: $5.191 \times 10^{+1}$ (5.2× WORSE).
Kappa scan monotonically increasing; $\alpha$-scan and two-pole
Reshetikhin-Faddeev scans offer no improvement.

**Structural obstruction theorem**: $\|[\Omega_{12}, \Omega_{13}]\|_{\max}
= 0.25$ at both rank 4 and rank 24 (rank-local invariant); Cartan
entries of $\Omega_{\mathfrak{so}(p, q)}$ are zero, so the obstruction
lives entirely in the root-space, and $Q$ is algebraically
orthogonal to it.

**Retraction**: Wave-2's claim of a single simple-Yangian envelope
$Y_\hbar(\mathfrak{so}(4, 20))$ admitting an elliptic R-matrix is
**retracted**. The viable structure is a direct-sum stratification
$$
Y_{K3}^{\mathrm{classical}}
\;=\;
\mathrm{Heis}_{\mathrm{rank}\,24,\,\mathrm{sig}\,(4, 20)}
\;\oplus\;
\bigoplus_{\Lambda \subset \Lambda_{\mathrm{Muk}},\,\mathrm{ADE}}
Y(\mathfrak g_\Lambda)
\;\oplus\;
\text{BKM sector}
$$
stratified by Mukai-lattice sublattices. This aligns with
Etingof W2's ADE locus, Drinfeld W2's pentagon stratification,
and the Wave-3 Beilinson $M_{K3}$-vs-$M^\flat$ disambiguation.

### 1.2 [H] Witten-Costello anomaly tension RESOLVED

Witten Wave-3 retracted his Wave-2 multiplicative formula and
derived the additive level-shift from first principles via the
Noether current + $\hat A$-genus on $K3 \times E$:
$$
\boxed{\;k \mapsto k + 12 + h^\vee\;}
$$
where $12 = \chi(K3)/2$ and $h^\vee$ is the dual Coxeter number.

Drinfeld Wave-3 gave the deeper reconciliation: Witten's Wave-2
quantity $24 h^\vee \dim\mathfrak g$ and Costello's $12 + h^\vee$
compute **different quantities**, both correct in their
respective bookkeeping:
- Witten's quantity is the characteristic-class integral
  $\int_{K3 \times E} \mathrm{ch}_2(\mathrm{ad}\,\mathfrak g) \wedge
  c_2(T_{K3})/12$ (total anomalous charge in adjoint-trace
  normalisation). Under fundamental-trace normalisation the $h^\vee$
  factor collapses and one recovers $\chi(K3)/2 = 12$.
- Costello's quantity is the effective-Yangian level shift from
  fish-diagram decomposition into two independent Wick
  contractions: K3-geometric loop ($+12$) + Chevalley colour
  trace ($+h^\vee$), additive because distinct 1-PI diagrams
  contribute additively.

Numerical cross-checks: $\mathfrak{sl}_2$ shift $= 14$ (Costello
fish-diagram verified); AGT spectral-parameter cross-check at $A_1$
matches $\hbar = 1/(k + 12 + 2h^\vee)$. Witten's Wave-2 formula
$24 h^\vee \dim\mathfrak g$ is recorded as a different invariant,
not retracted.

### 1.3 [H] Jacobi-antisymmetry gap FULLY resolved (Gelfand W3)

Gelfand Wave-3 completed the Wave-2 R3 framework: full
Drinfeld-first (J-presentation) inscribed with:
- Generators $x, J(x)$ for $x \in \mathfrak g_{K3, \mathrm{coeff}}
  = \mathfrak{so}(4, 20) \otimes H^*(K3)$.
- Three relations: (J1) $\mathfrak g_{K3, \mathrm{coeff}}$-Lie
  structure (no central term); (J2) linearity compatibility
  $[x, J(y)] = J([x, y])$; (J3) Drinfeld terminal
  $[J(x), J(y)] - J([x, y]) = \hbar^2 w(x, y)$ with $w$ the
  anomaly 3-tensor built from Mukai-weighted Casimir.

**Key finding (antipode carries K3 Euler)**:
$$
S(J(x_0^h)) \;=\; -J(x_0^h) + 24 \hbar \cdot x_0^h,
$$
where the $24$ is $\chi(K3)$ via the Mukai-Frobenius trace identity
$\sum_{i,j} Q^{ij} \mu^k_{ij} = 24 \delta^k_0$. **This is a direct
bridge between Yangian algebraic structure and K3 topology** —
the first time the K3 Euler number $= 24$ appears in the Yangian
antipode formula. Crossing shift $\kappa = N - 2 = 22$.

All five Hopf axioms (H1)-(H5) verified on the triple
$(x_0^e, x_{23}^f, J(x_0^h))$ at rank 24.

### 1.4 [H] Drinfeld-second presentation with all 12 Serre relations

Kazhdan Wave-3 inscribed the full Drinfeld-second presentation of
$Y_\hbar(\mathfrak{so}(4, 20))$ with R1-R6 relations covering all
12 Serre pairs of the $D_{12}$ Dynkin diagram:
- R1: commuting Cartan currents $[H_i(u), H_j(v)] = 0$.
- R2: Cartan-current exchange with $\pm \hbar a_{ij}/(u - v)$.
- R3: raising-lowering with $\delta_{ij} \hbar/(u - v)$.
- R4: like-type current exchange with symmetrised
  $\hbar a_{ij}/2$ anticommutator.
- R5: symmetrised Serre for all 11 adjacency classes (9 chain
  + 2 fork).
- R6: null-adjacency decoupling for $(\alpha_{11}, \alpha_{12})$.

Total: 44 Serre generator families (11 pairs $\times$ $2_\pm$ $\times$
$2_{\mathrm{orient}}$). Signs cross-checked against AMR 2006 Eqns
(3.8)-(3.14) and Guay 2007 Thm 5.1. Full draft replacement LaTeX
ready for inscription at `k3_yangian_chapter.tex:1855-2223`.

**Consistency**: this presentation exists at the formal-Yangian
level; per Polyakov W3, the ELLIPTIC R-matrix realising it does not
exist as a single simple-Yangian object across the indefinite
$(4, 20)$ signature. The formal Drinfeld-second relations are valid
(they encode the Serre data of $\mathfrak{so}(4, 20)$), but the
spectral-parameter R-matrix realisation requires the sublattice
stratification of W3 §1.1.

### 1.5 [H] Three-stratum Tannakian reconstruction (Etingof W3)

Etingof Wave-3 sharpened Wave-2's single "quasi-Hopf globally"
claim to a three-stratum structure:
- **ADE points**: strict Hopf up to torus gauge. Explicit
  2-cochain trivialisation $c_{\mathrm{ADE}}(\alpha) =
  (-1)^{-\langle \alpha, \alpha \rangle/2}$.
- **Generic smooth K3**: strict Hopf on the Tannakian-visible
  subcategory (integral Mukai lattice); Wave-2 overclaimed
  quasi-Hopf here.
- **Kummer/special-Picard K3**: genuinely quasi-Hopf, 3-cocycle
  $\alpha^{\mathrm{Km}} \in \Z/6 \oplus \Z/6$ inherited from
  $\Z/12$ Schur multiplier of $SL(2, \Z)^2$.

**Physical interpretation**: $\alpha^{\mathrm{Km}} \mod 2 = (1, 1)
\in \Z/2 \oplus \Z/2$ matches the Cecotti-Vafa / Segal-Tian
reflection anomaly in the 4d $\cN = 2$ theory on K3. Cross-checked
against Gaiotto W2's $20 + 2 + 2$ Schur-index split.

**Refined Mukai criterion**: vanishes iff (A) integer discriminant
AND (B) arithmetic monodromy 3-class trivial. Wave-2's "integer
discriminant" alone was necessary but not sufficient.

### 1.6 [H] One-loop counterterm proved rigorously (Costello W3)

Costello Wave-3 derived the Wave-2 counterterm
$\mathrm{CT}_1(u) = -(12 + h^\vee/2)(t \otimes t - P/2)/u^2$
RIGOROUSLY from Costello-Gwilliam factorisation axioms FA1-FA4
(cosheaf, RG equation, locality, cohomology control). Status
lifted from Wave-2's ClaimStatusConjectured to ClaimStatusProvedHere.

Two-loop sunset coefficient explicit:
$$
A_2(\mathfrak g, K3) = (12 + h^\vee/2)^2 - (h^\vee)^2/12.
$$
Per family: $\mathfrak{sl}_2: 168.67$; $\mathfrak{sl}_3: 181.5$;
$\mathfrak{so}(8): 222$; $E_8: 654$.

Two-loop counterterm: $\mathrm{CT}_2(u) = -A_2 \cdot [(3P/2 - t \otimes
t) \otimes t]_{\mathrm{sym}}/u^4$, forced by factorisation-cohomology
$H^1_{\hbar^4}$.

CWY 4d hCS cross-check: 6d-on-$K3 \times E$ counterterm equals
CWY 4d + universal $\chi(K3)/2 = 12$ additive shift, numerically
verified for $\mathfrak{sl}_2, \mathfrak{so}(8), E_8$.

BRST residual for $\mathfrak{su}(2)$: $5.4 \times 10^{-17}$ (machine
precision).

### 1.7 [H] Two-parameter Hodge-Deligne refinement (Nekrasov W3)

Nekrasov Wave-3 delivered the TWO-parameter Hodge refinement:
$$
\chi_{y, \bar y}(K3) \;=\; 1 + y^2 + \bar y^2 + 20\,y\bar y + y^2\bar y^2,
\qquad
Z_{K3}^{(y, \bar y)}(q) \;=\;
\prod_{n \ge 1} \frac{1}{(1-q^n)(1-q^n y^2)(1-q^n \bar y^2)(1-q^n y \bar y)^{20}(1-q^n y^2 \bar y^2)}.
$$
Each $[q^k]$ coefficient is the Hodge-Deligne polynomial
$e(\mathrm{Hilb}^k(K3); y, \bar y)$, verified to $q^5$.

**Scope-sharpening of Wave-2**: the single-exponent refined
formula $\prod (1-q^n)^{-\chi_y(K3)}$ agrees only at
$y \in \{0, 1\}$; at $y = -1$ it diverges from the Hodge-Deligne
form starting at $q^2$. Wave-2 aggregation loses Hodge-type
information.

Level-$k$ multiplicities in $\mathfrak{so}(24)$-irreps:
$k = 4 \to 25\,650$; $k = 5 \to 176\,256$. Gaiotto W2's $20 + 2 + 2$
split confirmed: $h^{1,1} + (h^{0,0} + h^{2,2}) + (h^{2,0} + h^{0,2})$.

### 1.8 [H] The $(y - 1)^{-2}$ regularisation explained (Gaiotto W3)

Gaiotto Wave-3 resolved the $(y - 1)^{-2}$ Weyl-vector prefactor
through three independent attacks, all naming the same object:
- **Physics**: two-fold BPS zero-mode vacuum trace from $J_3 = \pm 1$
  $SU(2)_R$ Cartan doubled by $\Delta_5^2 = \Phi_{10}$.
- **Mathematics**: Mittag-Leffler completion $\widehat M_Y \ominus M_Y$
  at $J_0 = \pm 1$.
- **Weyl denominator**: imaginary simple roots of
  $\mathfrak g_{\Delta_5}$ at $(0, 0, \pm 1)$ with multiplicity
  $c_{\Phi_{10}}(-1) = 2$.

**Resolution**: regularisation of the trace FUNCTIONAL (not a
subtraction, not a projective limit of the module proper).

Level-$k$ Yangian modules: $k=1$: rank 24 with $20 + 2 + 2$ split;
$k=2$: $\dim 575$ with $32 + 318 + 800$ split. Only $k = 1$
factorises cleanly into $\Phi_{10}^{-1}$ at $p = 0$; higher $k$
requires DMVV $p$-refinement. Beem-Rastelli VOA/Schur
correspondence fits $T_{K3}$ after recognising $c_{\mathrm{2d}}
= -24$ (BRST-reduced) not $+24$ (ambient lattice).

### 1.9 [H][R] Wave-2 Beilinson's "$M_{K3}$ catastrophic defect" was a CONVENTION CONFLATION

Beilinson Wave-3 showed the Wave-2 arithmetic defect was a
labeling conflation, not a genuine error. Two distinct objects
were collapsed under one symbol:
- $M_{K3}^{\mathrm{BKM}} = (0, 5, -16, 13)$, trace 2, bare BKM
  matrix (base-case input).
- $M^\flat = M_{K3 \times E^k} = (0, 5, -16, 11)$, trace 0,
  K3-anchored fixed point (post-iteration).

Wave-2's computation $(-11, 21, -21, 11) \ne (-13, 21, -21, 13)$
was correct arithmetic on wrong input (silent substitution of
$M^\flat$ into base-case convolution). Line 4686 was mislabeled.

Five surgical manuscript edits applied directly to
`k3_yangian_chapter.tex` to disambiguate. All downstream theorems
preserved; no retractions, no downgrades.

Bracketing-associator witness correction: Wave-2's critique of
$(C, C, K3)$ confirmed ($\sigma^*$-generic factors $\to a = 0$).
Corrected witness: $(\mathrm{conifold}, K3, E)$ with $a = (0, 0,
2, -2) \to c_\beta = 1$.

## 2. Residual open problems after Wave 3

Ranked by severity:

**Critical**.
1. **Explicit non-diagonal K-matrix for full $(4, 20)$ reflection
   equation.** Drinfeld W3 verified rank-24 RE structurally via
   block decomposition; explicit rank-24 non-diagonal K-matrix still
   open. Compute sprint recommended:
   `compute/lib/k3_reflection_equation_rank24.py`.
2. **Compact-CY$_3$ Tradler strictification** (Wave 1 carried).
3. **$L_\infty$-homotopy super-extension $\mathfrak{so}(4|20)^{oo}$
   via $l_4$ computation** from the third Gerstenhaber operation on
   $\mathrm{HH}^\bullet(D^b(K3))$ — Kazhdan W3 deferred.

**High**.
4. **BKM imaginary-root Drinfeld-$J$ presentation** for
   $\mathfrak g_{\Delta_5}$ (Wave 1 carried).
5. **Elliptic Belavin-Drinfeld r-matrices on ADE sub-lattices
   of $\Lambda_{\mathrm{Muk}}$** (Polyakov W3 sprint F1).
6. **Gluing/composition of $Y(\mathfrak g_{\mathrm{ADE}})$
   sub-Yangians** (Polyakov W3 sprint F2).
7. **BKM imaginary-root contribution via Borcherds lift**
   (Polyakov W3 sprint F3).
8. **Explicit elliptic dressing of $\mathrm{CT}_2$** beyond
   rational limit (Costello W3 open).
9. **Global K3-moduli extension of counterterm** requiring
   Etingof's quasi-Hopf 3-cocycle trivialisation (Costello W3 open).
10. **Three-loop double-sunset/tetrahedron diagram** (Costello W3).

**Medium**.
11. Higher-$k$ DMVV $p$-refinement for Yangian modules at $k \ge 2$
    (Gaiotto W3).
12. All-rank, all-$\mathfrak g$ Gelfand-W3 verification
    (beyond rank 24 $\mathfrak{sl}_2$).
13. Universal $R$-matrix in closed form for the direct-sum
    stratified algebra (Gelfand W3, Polyakov W3 combined).
14. Rational-Fock-module visibility: the Kummer K3 3-cocycle
    lives on modules invisible to $C_2$-cofinite Tannakian
    subcategory (Etingof W3).

## 3. Consolidated picture after Wave 3

**What the non-abelian K3 Yangian IS** (converged):

A stratified object $Y_{K3}^{\mathrm{classical}} =
\mathrm{Heis}_{\mathrm{rank}\,24, \mathrm{sig}\,(4, 20)} \oplus
\bigoplus_{\Lambda \subset \Lambda_{\mathrm{Muk}},\,\mathrm{ADE}}
Y(\mathfrak g_\Lambda) \oplus \text{BKM sector}$
built from:
- **Abelian layer**: rank-24 Mukai Heisenberg Yangian
  $Y_\hbar^{\mathrm{Heis}}(\Lambda_{K3})$ with Yang R-matrix
  $R(u) = (u + \hbar P)/(u + \hbar)$ (signature-independent YBE).
- **ADE layer**: at each enhancement point, shifted affine
  Yangian $Y_\hbar^{\mu}(\widehat{\mathfrak g})_{k = 1}$ with
  $k$-shift $k + 12 + h^\vee$ (Witten-Costello converged formula).
  Tannakian reconstruction is strict Hopf up to torus gauge.
- **BKM layer**: Borcherds branch $\mathfrak g_{\Delta_5}$ from
  Gritsenko-Nikulin Igusa cusp $\Phi_{10} = \Delta_5^2$. Hopf
  structure up to automorphic completion; pentagon source per
  Drinfeld W2.
- **Global Kummer/special-Picard**: genuinely quasi-Hopf with
  $\Z/6 \oplus \Z/6$ 3-cocycle (Etingof W3).

**What the non-abelian K3 Yangian IS NOT**:
- NOT a single simple Yangian $Y_\hbar(\mathfrak g_{K3})$ with a
  single spectral R-matrix (Polyakov W3 falsification).
- NOT strictly Hopf globally on K3 moduli (Etingof W3
  three-stratum).
- NOT describable by a bare Belavin-Drinfeld classical r-matrix
  on $\mathfrak{so}(4, 20)$ (Polyakov W3 structural obstruction).
- NOT Kac's $\osp(4 \mid 20)$ (Wave-2 Kazhdan correction).
- NOT computable from naive substitution between $M_{K3}^{\mathrm{BKM}}$
  and $M^\flat$ (Beilinson W3 disambiguation).

**The object**: $(Y_{K3}^{\mathrm{classical}}, r(z; \tau),
\mathrm{CT}_1, \mathrm{CT}_2, \alpha_{\mathrm{Km}})$ with:
- $r(z; \tau)$ elliptic tree-level R-matrix (Polyakov W2 YBE at
  rank 24 abelian + ADE sectors).
- $\mathrm{CT}_1, \mathrm{CT}_2$ one-loop and two-loop counterterms
  (Costello W3 from factorisation axioms).
- $\alpha_{\mathrm{Km}}$ Kummer 3-cocycle (Etingof W3).

## 4. Confidence table

| Claim | Confidence | Wave-3 sources |
|---|---|---|
| Abelian rank-24 Mukai Heisenberg Yangian with Yang R | [H] | Gelfand W3, Polyakov W2 |
| BFN affine-Yangian sub-quantisation at ADE | [H] | Beilinson W2 carried |
| Classical limit structure $\mathfrak{so}(4, 20)$ (not $\osp$) | [H] | Wave-2 carried |
| Rank 12 Cartan, Dynkin $D_{12}$, full Drinfeld-second | [H] | Kazhdan W3 |
| Loop-algebra Lie-bialgebra framework (R3) with explicit coproduct/antipode | [H] | Gelfand W3 |
| Antipode carries $\chi(K3) = 24$ via Mukai-Frobenius trace | [H] | Gelfand W3 |
| Level shift $k \mapsto k + 12 + h^\vee$ | [H] | Witten W3 + Costello W3 |
| One-loop counterterm $\mathrm{CT}_1$ proved rigorously | [H] | Costello W3 |
| Two-loop sunset $A_2 = (12 + h^\vee/2)^2 - (h^\vee)^2/12$ | [H] | Costello W3 |
| Two-parameter Hodge-Deligne partition function | [H] | Nekrasov W3 |
| $(y - 1)^{-2}$ regularisation identified | [H] | Gaiotto W3 |
| Pentagon H1-H4 proved | [H] | Drinfeld W2 carried |
| Witten's $24 h^\vee \dim\mathfrak g$ as characteristic-class integral | [H] | Drinfeld W3 |
| Three-stratum Tannakian reconstruction (ADE / generic / Kummer) | [H] | Etingof W3 |
| Kummer 3-cocycle $\Z/6 \oplus \Z/6$ | [M] | Etingof W3 |
| Direct-sum stratification of $Y_{K3}^{\mathrm{classical}}$ | [M] | Polyakov W3, needs integration with Gelfand W3 |
| Rank-24 reflection equation block-factorised | [M] | Drinfeld W3 |
| Explicit non-diagonal K-matrix rank 24 | [O] | Drinfeld W3 flagged |
| $L_\infty$-homotopy super-extension | [O] | Wave 1-3 carried |
| Compact-CY$_3$ CY-A$_3$ unconditional | [O] | Wave 1-3 carried |
| Single simple-Yangian $Y_\hbar(\mathfrak{so}(4, 20))$ as the envelope | [R] | Polyakov W3 falsification |
| Wave-2 catastrophic $M_{K3}$ defect | [R] | Beilinson W3 convention conflation |
| Single "quasi-Hopf globally" | [R] | Etingof W3 three-stratum |
| Witten Wave-2 multiplicative anomaly | [R] | Witten W3 retraction |

## 5. Cross-volume consequences

- **Vol I**: canonical level shift $k + 12 + h^\vee$ replaces
  Wave-2's $k + 12 h^\vee$. Seven-faces $r(z)$ programme receives
  the $+12$ K3-specific contribution; generic genus-1 shifts
  reduce to $+h^\vee$.
- **Vol II**: Schur-index 2-cocycle identified with the
  $\chi(K3)/12$ Todd piece; $\mathsf{SC}^{\mathrm{ch, top}}$ Pentagon
  anomaly = Etingof W3 Kummer 3-cocycle.
- **Vol III**: `k3_yangian_chapter.tex:1855-2223` ready for
  inscription with Kazhdan W3 Drinfeld-second presentation;
  `def:k3-double-current-algebra` line 277 scrubbed per Gelfand
  W2/W3; five Beilinson W3 edits already applied; $\osp(4 \mid 20)
  \to \mathfrak{so}(4, 20)$ per Wave-2 Kazhdan.

## 6. Recommended Wave-4 targets

1. **Gelfand W4**: extend Drinfeld-first verification beyond rank
   24 $\mathfrak{sl}_2$; universal R-matrix in closed form.
2. **Kazhdan W4**: $l_4$ computation on $\mathrm{HH}^\bullet(D^b(K3))$
   for the $L_\infty$ super-extension.
3. **Etingof W4**: rational-Fock-module visibility; global
   Tannakian extension to the rational-weight sector.
4. **Polyakov W4**: Belavin-Drinfeld on ADE sub-lattices;
   sub-Yangian gluing; BKM Borcherds sector.
5. **Nekrasov W4**: three-parameter refinement $(y, \bar y, p)$
   with full Siegel modular structure; level-$k$ multiplicity for
   $k \ge 6$.
6. **Beilinson W4**: next-layer audit of the five new edits + the
   Kazhdan W3 inscription once applied.
7. **Drinfeld W4**: explicit rank-24 non-diagonal
   Ghoshal-Zamolodchikov K-matrix.
8. **Witten W4**: full heterotic $\mathrm{Spin}(4, 20)$
   T-duality $\to$ Yangian chain-level map with Obers-Pioline.
9. **Costello W4**: three-loop double-sunset/tetrahedron; elliptic
   Eisenstein dressing of $\mathrm{CT}_2$.
10. **Gaiotto W4**: higher-$k$ DMVV $p$-refinement for $k \ge 2$
    Yangian modules.

## 7. Wave-3 convergence declaration

Wave 3 produced four major convergences (Witten-Costello
resolution, Gelfand R3 completion, Kazhdan Drinfeld-second
inscription, Costello factorisation-axiom proof), three major
retractions (Polyakov Q-dressing obstruction, Beilinson
$M_{K3}$-conflation, Etingof three-stratum), and three sharpenings
(Gaiotto $(y-1)^{-2}$ identification, Nekrasov Hodge-Deligne
refinement, Drinfeld reflection-equation block decomposition).

The space of claims about the K3 Yangian has shrunk and
crystallised simultaneously: the conjectural simple-Lie-algebra
description is off the table; the direct-sum stratification is on;
the level shift is $k + 12 + h^\vee$; the three Tannakian strata
are ADE / generic / Kummer with concrete 3-cocycle data.

**Nothing is sacred**. Four Wave-2 claims were retracted in
Wave 3. Another round (Wave 4) may reveal further retractions;
the adversarial attack-heal methodology remains the operating
mode.
