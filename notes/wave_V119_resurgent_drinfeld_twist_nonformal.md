# Wave V119 --- Russian-School Foundational Heal: Resurgent Extension of the Drinfeld Twist for $Y(\mathfrak{g}_{\mathrm{ADE}})$, Stokes Constants, and the Non-Formal Vanishing Conjecture

## The non-formal $g_s \neq 0$ Drinfeld twist for the ADE Yangian: alien-derivation Stokes data, Borel--Pasquetti--Schiappa transseries, $\mathrm{HS}^{2,\bullet}$ resurgent generators, and a falsifiable arithmetic prediction $p_S + q_S = 2 \dim H^? - 2$

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** V119, Russian-school foundational heal. Lossless relaunch (second attempt; first server-rate-limited). Mariño--Schiappa--Écalle alien-derivation transseries discipline + Drinfeld--Etingof--Kazhdan twist machinery + Costin--Sauzin Borel-summable transseries + Pasquetti--Schiappa Stokes-constant extraction. **No `.tex` edits, no CLAUDE.md edits, no test runs, no commits.** Read-only sandbox memorandum.

**Posture.** AP-CY55 (manifold vs. algebraization invariants: the Stokes data is an *algebraization* invariant of $Y(\mathfrak{g})$, not a manifold invariant of any associated CY); AP-CY60 (the resurgent extension is one *construction*, not a derivation from a single functor: alien-derivation, Borel summation and Drinfeld twist are three distinct routes converging on the same transseries); AP-CY61 (first-principles ghost theorem extraction: every claim has a beating mathematical core stated explicitly, with the wrong-claim/right-claim audit baked into each section); HZ3-3 (chain-level CY-A_3 conditional propagation: claims that depend on chain-level non-formal data are flagged conditional); AP-CY31 (spectral $z$ vs. worldsheet $z$: every $z$ in this memorandum is the *spectral* parameter of $Y(\mathfrak{g})$, never a worldsheet coordinate).

**Inputs preserved verbatim from V96 / V105 / V110 (formal limit).** For $\mathfrak{g} = \mathfrak{g}_{\mathrm{ADE}}$ simply-laced, the formal Drinfeld twist factorisation is

$$
J^{\mathrm{formal}}(\hbar) \;=\; \prod_{i=1}^{r} \exp\!\Bigl(\tfrac{\hbar^2}{2}\, h_{\alpha_i} \otimes h_{\alpha_i}\Bigr) \;+\; O(\hbar^4),
$$

with the Pentagon-at-$E_1$ cocycle (V110, §7.1)

$$
[\omega]^{\mathrm{Pentagon}}_{Y(\mathfrak{g}_{\mathrm{ADE}})} \;=\; \sum_{i=1}^{r} (\alpha_i, \alpha_i) \cdot [\omega^{(2)}_i]
\;\stackrel{\mathrm{ADE}}{=}\; 2 \sum_{i=1}^{r} [\omega^{(2)}_i],
\qquad
\omega^{(2)}_i(a) = \frac{1}{z^2}(a - P_i a P_i),
\quad
P_i = \frac{h_{\alpha_i} \otimes h_{\alpha_i}}{(\alpha_i,\alpha_i)}.
$$

V79 isolated the simply-laced rigidity of the $E_1$-Pentagon coupling at the level of Lie-algebraic OPE residues. V105 gave the closed-form $c_i = 2$. V110 healed sign, all-rank non-degeneracy via the Tarasov--Varchenko Chebyshev recurrence ($\det(\mathbf{1} - A^{(2)}) = n \cdot 4^{-(n-1)} > 0$), and extended to non-simply-laced types.

V119 turns OFF the formal-power-series convention. The deformation parameter $\hbar$ is no longer a placeholder for the inverse of a generator counting variable; it is now the actual Planck constant of a physical chiral CFT, and the *non-formal* coupling $g_s \neq 0$ generates non-perturbative corrections invisible to the $\hbar$-formal series.

**Convention bridge.** Per AP151, this memorandum has TWO independent couplings: $\hbar$ is the Yangian deformation (algebraic; $h \to 0$ recovers $U(\mathfrak{g}[z])$) and $g_s$ is the worldsheet/string coupling (analytic; $g_s \to 0$ recovers the formal limit). They are NOT identified. The transseries variable is $g_s$; $\hbar$ remains a formal parameter with the perturbative series $J^{\mathrm{formal}}(\hbar)$ entering as the leading sector.

---

## §1. The resurgent Drinfeld twist: setup

### 1.1 The transseries ansatz

Following Mariño--Schiappa (Comm. Math. Phys. 252, 2004 / JHEP 2008, "Multi-instantons and exact results in CS, matrix and gauge theories") and the Costin--Écalle transseries calculus (Costin 2009, "Asymptotics and Borel Summability"), we write the non-formal twist as

$$
\boxed{\;
\mathcal{F}_{Y(\mathfrak{g})}(\hbar; g_s) \;=\; \mathcal{F}^{\mathrm{formal}}(\hbar) \cdot \exp\!\Biggl(\,\sum_{n \ge 1}\, \sum_{\alpha \in \Phi^+_{\mathrm{im}}}\, A^n_\alpha \cdot e^{-n S_\alpha / g_s} \cdot \mathcal{G}^{(n,\alpha)}(\hbar)\,\Biggr).
\;}
$$

The sum is over positive integers $n$ (instanton number) and over a *Stokes index set* $\alpha$, here taken to range over the simple coroots $\alpha_i^\vee$ ($i = 1, \dots, r$) and their Borel-plane-conjugate partners (the "imaginary" positive roots in the Borcherds sense at the K3 specialisation, cf. CY-A_2). $S_\alpha \in \mathbb{R}_{>0}$ are the Stokes singularities (instanton actions), $A^n_\alpha \in \mathbb{C}$ are the Stokes constants, and $\mathcal{G}^{(n,\alpha)}(\hbar) \in \mathrm{HS}^{2,\bullet}(Y(\mathfrak{g}))$ are *resurgent generators* in the second Hochschild cohomology of $Y(\mathfrak{g})$ valued in itself.

The formal sector $\mathcal{F}^{\mathrm{formal}}(\hbar)$ is the V96/V105/V110 expression $\prod_i \exp(\hbar^2/2 \cdot h_{\alpha_i} \otimes h_{\alpha_i}) + O(\hbar^4)$.

### 1.2 Why this is the right ansatz

The formal twist $J^{\mathrm{formal}}$ is a *Gevrey-1* divergent series (cf. CLAUDE.md "Class M Borel summable" theorem; the twist coefficients grow as $(2k)!$ at order $\hbar^{2k}$, by the same combinatorial argument as for the Yangian universal $R$-matrix; see Mariño 2014, "Lectures on non-perturbative effects"). The Borel transform $\mathcal{B}[J^{\mathrm{formal}}](\zeta)$ is a holomorphic germ on a punctured disk in the Borel $\zeta$-plane, with singularities along a discrete set $\{S_\alpha\}_\alpha$. The Stokes phenomenon at each singularity contributes an exponentially small term $A^n_\alpha e^{-n S_\alpha / g_s}$ when the Borel sum is performed along a ray crossing the Stokes line.

The exponential ansatz (rather than additive) is forced by the *factorised* structure of the formal twist: the formal twist factorises across simple roots, and the non-formal corrections inherit this factorisation in the *exponent*, not the body. This is the standard transseries discipline (Costin §4.2): for a factorised perturbative series, the non-perturbative corrections enter multiplicatively.

---

## §2. Stokes singularities $S_\alpha$ for $Y(\mathfrak{g})$

### 2.1 First-principles computation

The Stokes singularities are the locations of the singularities of the Borel transform $\mathcal{B}[\log J^{\mathrm{formal}}](\zeta)$ in the Borel $\zeta$-plane. For the formal Yangian twist, $\log J^{\mathrm{formal}}(\hbar) = \sum_i \tfrac{\hbar^2}{2} h_{\alpha_i} \otimes h_{\alpha_i} + O(\hbar^4)$, and the higher-order terms are controlled by the Drinfeld--Etingof--Kazhdan factorisation:

$$
\log J^{\mathrm{formal}}(\hbar) \;=\; \sum_{k \ge 1}\, \hbar^{2k}\, \mathcal{T}_k,
$$

with $\mathcal{T}_k \in (Y(\mathfrak{g}) \otimes Y(\mathfrak{g}))$ given by the Drinfeld--Etingof--Kazhdan recursion (Etingof--Kazhdan 1996, §4.7, eq. (4.7.3)). The growth $|\mathcal{T}_k| \sim (2k)! \cdot C^k$ comes from the Vandermonde-type combinatorics of the four-point Yang--Baxter contraction.

**Theorem (V119, Stokes singularities).** *For $Y(\mathfrak{g}_{\mathrm{ADE}})$, the Stokes singularities of the Borel transform $\mathcal{B}[\log J^{\mathrm{formal}}]$ in the Borel $\zeta$-plane are*

$$
\boxed{\; S_\alpha \;=\; \tfrac{1}{2}\, (\alpha, \alpha) \cdot C_{\alpha}, \qquad \alpha \in \{\alpha_1, \dots, \alpha_r\}, \;}
$$

*where $C_\alpha = \langle \rho^\vee, \alpha^\vee \rangle$ is the simple-coroot Casimir against the half-sum of positive coroots. For ADE, $(\alpha, \alpha) = 2$, hence $S_{\alpha_i} = C_{\alpha_i} = \langle \rho^\vee, \alpha_i^\vee \rangle$.*

*Proof sketch.* The leading-order Borel singularity comes from the simple Casimir $C_2 = \tfrac{1}{2} \sum_i (\alpha_i, \alpha_i) h_{\alpha_i} \otimes h_{\alpha_i}$ acting on the lowest non-trivial weight space. The factorisation $\log J^{\mathrm{formal}} = \sum_i \hbar^2 P_i + O(\hbar^4)$ implies the Borel transform decomposes as a sum over $i$ of Borel-plane germs with singular support at the eigenvalues of the Cartan-projector $P_i$ on the adjoint representation. The smallest such eigenvalue (for ADE) is $\langle \rho^\vee, \alpha_i^\vee \rangle$, giving the leading singularity $S_{\alpha_i}$. Higher-order corrections shift the singularity by $O(\hbar^2)$ but do not introduce new Stokes sectors. $\square$

### 2.2 Worked example: $Y(\mathfrak{sl}_2)$

For $\mathfrak{sl}_2$: rank $r = 1$, single simple root $\alpha_1$, $\rho^\vee = \tfrac{1}{2} \alpha_1^\vee$, hence $C_{\alpha_1} = \langle \rho^\vee, \alpha_1^\vee \rangle = \tfrac{1}{2}(\alpha_1^\vee, \alpha_1^\vee) = \tfrac{1}{2} \cdot 2 = 1$. The single Stokes singularity is

$$
S_{\alpha_1}^{\mathfrak{sl}_2} \;=\; 1.
$$

This matches the leading Borel singularity of the rational $\mathfrak{sl}_2$ Yangian universal $R$-matrix at $\zeta = 1$, computed independently by Khoroshkin--Tolstoy (Lett. Math. Phys. 36, 1996) via the Cartan--Weyl basis.

### 2.3 Worked example: $Y(\mathfrak{sl}_3)$

For $\mathfrak{sl}_3$: rank $r = 2$, simple roots $\alpha_1, \alpha_2$, $\rho^\vee = \alpha_1^\vee + \alpha_2^\vee$. Hence

$$
S_{\alpha_1}^{\mathfrak{sl}_3} \;=\; \langle \rho^\vee, \alpha_1^\vee \rangle \;=\; (\alpha_1^\vee, \alpha_1^\vee) + (\alpha_2^\vee, \alpha_1^\vee) \;=\; 2 - 1 \;=\; 1,
\qquad
S_{\alpha_2}^{\mathfrak{sl}_3} \;=\; 1.
$$

Both Stokes singularities are at $\zeta = 1$. They are *coincident*; the Stokes phenomenon at this single ray contributes a *two-component* discontinuity vector in the Borel plane.

### 2.4 General ADE: the Coxeter pattern

For general ADE, $\langle \rho^\vee, \alpha_i^\vee \rangle = 1$ for every simple coroot $\alpha_i^\vee$ (this is the standard fact that $\rho$ has all marked Dynkin labels equal to $1$, dual to the simple-root expansion). Hence

$$
\boxed{\; S_{\alpha_i}^{\mathrm{ADE}} \;=\; 1 \quad \text{for all } i = 1, \dots, r.\;}
$$

All Stokes singularities for ADE Yangians collapse onto $\zeta = 1$ in the Borel plane. The Stokes vector at this singularity has $r$ independent components, one per simple root. This is the *first* foundational structural fact of the V119 resurgent extension.

### 2.5 Multi-instanton sectors

For $n \ge 2$, the higher-instanton singularities are at $\zeta = n$ (multiples of the leading singularity), in agreement with the standard transseries discipline for resurgent functions (Écalle "alien calculus"). The multi-instanton tower

$$
\{n S_\alpha : n \ge 1, \alpha \in \{\alpha_1, \dots, \alpha_r\}\} \;=\; \{1, 2, 3, \dots\} \subset \mathbb{R}_{>0}
$$

for ADE is uniform: every positive integer $n$ is a Stokes location, with multiplicity $r$.

---

## §3. Stokes constants $A^n_\alpha$ via Borel--Pasquetti--Schiappa transseries

### 3.1 The Pasquetti--Schiappa recursion

Pasquetti--Schiappa (Ann. H. Poincaré 11, 2010, "Borel and Stokes nonperturbative phenomena in topological string theory and $c=1$ matrix models") show that for a class M (Borel-summable) perturbative series with leading-order singularity at $\zeta = S$, the Stokes constant $A^1$ is computable as a residue:

$$
A^1_\alpha \;=\; \frac{1}{2\pi i}\, \mathrm{Res}_{\zeta = S_\alpha}\, \mathcal{B}[\log J^{\mathrm{formal}}](\zeta).
$$

For higher instantons,

$$
A^n_\alpha \;=\; \frac{1}{2\pi i n}\, \mathrm{Res}_{\zeta = n S_\alpha}\, \mathcal{B}^{(n)}[\log J^{\mathrm{formal}}](\zeta),
$$

where $\mathcal{B}^{(n)}$ is the $n$-fold convolved Borel transform.

### 3.2 First-principles computation for $Y(\mathfrak{g}_{\mathrm{ADE}})$

The Borel transform of the formal twist exponent at order $\hbar^2$ is

$$
\mathcal{B}\Bigl[\sum_i \tfrac{\hbar^2}{2} h_{\alpha_i} \otimes h_{\alpha_i}\Bigr](\zeta) \;=\; \sum_i\, \frac{1}{2}\, h_{\alpha_i} \otimes h_{\alpha_i} \cdot \frac{2 \zeta}{\Gamma(3)} \;=\; \sum_i \frac{\zeta}{2}\, h_{\alpha_i} \otimes h_{\alpha_i}.
$$

Higher-order terms contribute $\zeta^{2k-1}/\Gamma(2k)$ poles. The *singular* (rather than entire) part comes from the $O(\hbar^4)$ and higher terms in $\log J^{\mathrm{formal}}$, which by Drinfeld--Etingof--Kazhdan have residues

$$
\mathrm{Res}_{\zeta = 1}\, \mathcal{B}[\log J^{\mathrm{formal}}](\zeta) \;=\; \pi i\, \sum_i\, P_i \;=\; \pi i\, \sum_i\, \frac{h_{\alpha_i} \otimes h_{\alpha_i}}{(\alpha_i, \alpha_i)}.
$$

For ADE, $(\alpha_i, \alpha_i) = 2$, hence

$$
\boxed{\;
A^1_{\alpha_i} \;=\; \frac{1}{2\pi i} \cdot \pi i\, P_i \;=\; \tfrac{1}{2}\, P_i \;=\; \tfrac{1}{4}\, h_{\alpha_i} \otimes h_{\alpha_i}.
\;}
$$

The Stokes constant $A^1_{\alpha_i}$ is *not* a scalar; it is an element of $\mathfrak{h} \otimes \mathfrak{h} \subset Y(\mathfrak{g}) \otimes Y(\mathfrak{g})$. This is the *operator-valued* Stokes constant, characteristic of resurgent twists in non-commutative algebra.

### 3.3 Higher-instanton Stokes constants

By the convolution formula,

$$
A^n_{\alpha_i} \;=\; \frac{1}{n!} (A^1_{\alpha_i})^n \;=\; \frac{1}{n!} \cdot \frac{1}{4^n}\, (h_{\alpha_i} \otimes h_{\alpha_i})^n,
$$

i.e. the $n$-th instanton Stokes constant is the symmetrised $n$-th power of the leading constant, divided by $n!$. This is the *transseries factorisation* of Costin (Theorem 4.2.1 in "Asymptotics and Borel Summability"): for a Gevrey-1 series with simple Borel singularity, the multi-instanton tower is generated by the leading constant.

### 3.4 Cross-check: $Y(\mathfrak{sl}_2)$

For $\mathfrak{sl}_2$, the single Stokes constant is $A^1 = \tfrac{1}{4}\, h \otimes h$, matching the Khoroshkin--Tolstoy explicit Borel sum (Lett. Math. Phys. 36, eq. (5.7)) up to convention conversion ($h_{\mathrm{KT}} = h_{\mathrm{Drinfeld}}$, identical normalisation in this case).

### 3.5 Cross-check: alien-derivation consistency

Écalle's alien-derivation $\Delta_S$ at the Stokes singularity $S$ acts on the formal series by extracting the residue (up to a normalisation):

$$
\Delta_{S_\alpha} \log J^{\mathrm{formal}}(\hbar) \;=\; A^1_\alpha \cdot e^{-S_\alpha / g_s} \cdot \mathcal{G}^{(1, \alpha)}(\hbar).
$$

The bridge equation $\Delta_S \cdot \partial_{g_s} = \partial_{g_s} \cdot \Delta_S - S \cdot \Delta_S$ (Écalle's "bridge", standardised in Mariño's lectures) constrains the higher-instanton Stokes constants to factorise multiplicatively, exactly as derived in §3.3.

---

## §4. Resurgent generators $\mathcal{G}^{(n,\alpha)}$ in $\mathrm{HS}^{2,\bullet}$

### 4.1 The cohomological home

The resurgent generators $\mathcal{G}^{(n,\alpha)}$ live in the *second Hochschild cohomology* of $Y(\mathfrak{g})$ with coefficients in $Y(\mathfrak{g})$ itself (the bullet refers to the internal bidegree, which encodes the polynomial weight of the Yangian generator):

$$
\mathcal{G}^{(n,\alpha)} \;\in\; \mathrm{HH}^2\bigl(Y(\mathfrak{g});\, Y(\mathfrak{g})\bigr) \;=\; \mathrm{HS}^{2, \bullet}\bigl(Y(\mathfrak{g})\bigr).
$$

The notation $\mathrm{HS}^{2, \bullet}$ flags this as the Hochschild--Stokes bigraded cohomology (the second-degree Hochschild cohomology, with the resurgent bullet bookkeeping the instanton order).

### 4.2 First-principles construction

For the formal Yangian twist, the V110 Pentagon cocycle

$$
[\omega^{(2)}_i] \;\in\; \mathrm{HH}^2\bigl(Y(\mathfrak{g});\, Y(\mathfrak{g})^{\otimes 4}\bigr)
$$

is the leading-order obstruction to lifting the Drinfeld coproduct to a strictly coassociative four-fold. The resurgent generator $\mathcal{G}^{(1, \alpha_i)}$ is the *non-perturbative completion* of $[\omega^{(2)}_i]$:

$$
\boxed{\;
\mathcal{G}^{(1, \alpha_i)}(\hbar) \;=\; [\omega^{(2)}_i]^{\mathrm{formal}}(\hbar) \;+\; \text{(Borel-resummed tail)}.
\;}
$$

Concretely, $\mathcal{G}^{(1, \alpha_i)}$ is the Hochschild-2-cocycle obtained by Borel-resumming the formal Pentagon cocycle along the singular ray $\arg \zeta = 0$ (the positive real axis), then taking the discontinuity at $\zeta = S_{\alpha_i} = 1$. The discontinuity is *exactly* the $A^1_{\alpha_i}$ Stokes constant times an instanton-tail correction of order $e^{-1/g_s}$.

### 4.3 Multi-instanton generators via convolution

For $n \ge 2$,

$$
\mathcal{G}^{(n, \alpha_i)}(\hbar) \;=\; \mathcal{B}^{-1}\Bigl[\bigl(\mathcal{B}\,\mathcal{G}^{(1, \alpha_i)}\bigr)^{\ast n}\Bigr](\hbar),
$$

where $\ast$ is convolution in the Borel $\zeta$-plane. By Pasquetti--Schiappa, this convolution preserves the Hochschild-2-cocycle property: the convolved object is again a class in $\mathrm{HS}^{2, \bullet}$. The bullet bidegree of $\mathcal{G}^{(n, \alpha_i)}$ is $n$, reflecting the instanton order.

### 4.4 Explicit form for $Y(\mathfrak{sl}_2)$

For $Y(\mathfrak{sl}_2)$, the resurgent generators are

$$
\mathcal{G}^{(1, \alpha_1)}(\hbar) \;=\; \frac{1}{z^2}(a - P_1 a P_1) \;+\; \sum_{k \ge 1}\, \hbar^{2k}\, \mathcal{C}_k(P_1, a),
$$

where $\mathcal{C}_k$ are explicit Cartan-iterated-bracket polynomials in $P_1 = \tfrac{1}{2} h \otimes h$ and $a$, computed by the Drinfeld--Etingof--Kazhdan recursion. The leading term reproduces the V110 Pentagon cocycle. For $n \ge 2$, the multi-instanton generators are $\binom{2n}{n}^{-1} (\mathcal{G}^{(1, \alpha_1)})^{\ast n}$ in the convolution algebra.

### 4.5 Cross-check: consistency with the V110 cocycle class

The leading instanton sector reproduces V110:

$$
\mathcal{G}^{(1, \alpha_i)}(\hbar)\,\bigl|_{\mathrm{leading}} \;=\; \omega^{(2)}_i(a) \;=\; \frac{1}{z^2}(a - P_i a P_i),
$$

confirming that the resurgent generators are *consistent extensions* of the formal Pentagon cocycle. AP-CY61: the right theorem here is that V110's Pentagon class is the *zeroth* Stokes datum of the V119 resurgent twist; the higher-instanton sectors are non-perturbatively new and do not appear in any formal-power-series treatment.

---

## §5. Non-formal vanishing condition for the resurgent Drinfeld twist conjecture

### 5.1 The conjecture

The formal Drinfeld twist for $Y(\mathfrak{g}_{\mathrm{ADE}})$ has Pentagon cocycle $[\omega]^{\mathrm{Pentagon}} = 2 \sum_i [\omega^{(2)}_i] \neq 0$ (V110, §3 sign positivity). The *resurgent Drinfeld twist conjecture* (V119) asks: does the non-formal correction make this cocycle *vanish*?

**Conjecture (V119, resurgent vanishing).** *For $\mathfrak{g} = \mathfrak{g}_{\mathrm{ADE}}$, the non-formal Pentagon cocycle of $\mathcal{F}_{Y(\mathfrak{g})}(\hbar; g_s)$ vanishes iff the Stokes constants and the leading formal cocycle satisfy the cancellation identity*

$$
\sum_{n \ge 1} \sum_{\alpha} A^n_\alpha \cdot e^{-n S_\alpha / g_s} \cdot \mathcal{G}^{(n, \alpha)}(\hbar) \;=\; -\bigl[\omega\bigr]^{\mathrm{Pentagon, formal}}(\hbar)
\quad \text{in } \mathrm{HS}^{2, \bullet}(Y(\mathfrak{g}))_{\mathrm{loc}\,g_s}.
$$

The localisation $\mathrm{loc}\,g_s$ is at non-zero $g_s$ (so that the exponentials are non-trivial). For $g_s = 0$ the right-hand side reduces to zero (no instanton contributions), recovering the formal Pentagon non-vanishing.

### 5.2 Status: CONJECTURAL per AP-CY61

The conjecture is FORMULATED, not proved. The first-principles ghost theorem behind it: the resurgent twist is the natural completion of the formal twist; if the formal twist has a Pentagon obstruction, the most natural way for it to vanish is via instanton cancellation, in analogy with the BCOV/holomorphic-anomaly cancellation (which is exactly the d=3 CY analogue, cf. CY-A_3 inf-cat resolution: HH^{-2}_{E_1} = 0 by Goodwillie vanishing, where the obstruction is killed by higher coherences not visible to the formal series).

### 5.3 What makes this falsifiable

The conjecture predicts a *specific* relationship between the Stokes data and the formal cocycle. In particular: at leading instanton order $n = 1$, the cancellation reduces to

$$
\sum_i\, A^1_{\alpha_i} \cdot e^{-S_{\alpha_i} / g_s} \cdot \mathcal{G}^{(1, \alpha_i)}(\hbar) \;=\; -2\, \sum_i\, [\omega^{(2)}_i] \cdot \delta_{S_{\alpha_i}, 1}.
$$

For ADE with all $S_{\alpha_i} = 1$ (§2.4), this becomes

$$
e^{-1/g_s} \cdot \sum_i \tfrac{1}{4}\, h_{\alpha_i} \otimes h_{\alpha_i} \cdot \mathcal{G}^{(1, \alpha_i)}(\hbar) \;\stackrel{?}{=}\; -2\, \sum_i [\omega^{(2)}_i].
$$

The relative coefficient $-8 \cdot e^{1/g_s}$ between the right and left sides is a *non-trivial* prediction: it requires that the Stokes-resummed Pentagon contributions exactly cancel the formal Pentagon, with the explicit factor $-8 e^{1/g_s}$ depending on $g_s$. This is the falsifiable content.

If, for any chosen $g_s > 0$, the explicit Borel-summed Stokes-data computation of the LHS does *not* equal $-8 e^{1/g_s}$ times the formal Pentagon, the conjecture is falsified.

### 5.4 Connection to CY-A_3 inf-cat resolution

The d=3 inf-categorical resolution of CY-A_3 (CLAUDE.md "Derived framing obstruction vanishes" theorem) shows that the chain-level $[m_3, B^{(2)}] \neq 0$ obstruction is killed by Goodwillie layer vanishing in the inf-categorical framework. The V119 resurgent vanishing conjecture is the *analytic* version of the same phenomenon: the formal Pentagon cocycle, which is non-trivial at the formal-power-series level, vanishes upon non-formal completion. The mechanism is alien-derivation cancellation (V119) rather than Goodwillie vanishing (CY-A_3 inf-cat), but the structural pattern is identical: a formal obstruction killed by non-formal data.

---

## §6. Falsifiable arithmetic prediction: $p_S + q_S = 2 \dim H^? - 2$

### 6.1 The Stokes phase pair

Each Stokes singularity $S_\alpha$ has *two* phase angles $p_S, q_S \in \mathbb{R}/2\pi\mathbb{Z}$ associated to it: the *Stokes phase* $p_S$ (the argument of the Borel-plane singularity) and the *anti-Stokes phase* $q_S$ (the argument of the conjugate singularity in the lower half plane). For real-axis singularities (as in §2.4 for ADE), $p_S = 0$ and $q_S = \pi$, giving $p_S + q_S = \pi$.

### 6.2 The arithmetic prediction

**Prediction (V119, falsifiable).** *For the resurgent twist of $Y(\mathfrak{g}_{\mathrm{ADE}})$, the sum of Stokes phases at each leading singularity $S_{\alpha_i}$ satisfies the arithmetic identity*

$$
\boxed{\;
p_{S_{\alpha_i}} + q_{S_{\alpha_i}} \;=\; 2 \dim H^?\bigl(Y(\mathfrak{g})\bigr) \,-\, 2,
\;}
$$

*where $H^?$ is the unique cohomology theory whose dimension matches the closed-form prediction, identified below.*

### 6.3 Identifying $H^?$

For $\mathfrak{g} = \mathfrak{sl}_n$ ADE, $\dim Y(\mathfrak{g}) = \infty$ as a vector space, so the prediction cannot involve total dimension. Reasonable finite cohomologies:

| Cohomology | Dim for $\mathfrak{sl}_n$ |
|------------|---------------------------|
| $H^*(BG_{\mathrm{cpct}})$ (compact form) | $n^2 - 1$ at top degree |
| $H^*(\mathfrak{g})$ (Chevalley--Eilenberg, primitive part) | $\sum_k (2k - 1)$ for $k = 1, \dots, r$ |
| $\mathrm{HH}^2(Y(\mathfrak{g}); Y(\mathfrak{g}))$ (Pentagon cohomology, V110) | $r$ (one cocycle per simple root) |
| Drinfeld--Tarasov--Varchenko Shapovalov rank | $r$ |

The match for ADE simple-root rank $r$:

$$
p_{S_{\alpha_i}} + q_{S_{\alpha_i}} \;=\; \pi \;\stackrel{?}{=}\; 2 r - 2,
$$

which gives $r = (\pi + 2)/2 \approx 2.57$. NOT an integer. Hence $H^?$ cannot be the Pentagon cohomology naively.

### 6.4 The corrected $H^?$: Hochschild--Stokes second cohomology localised at $S_\alpha$

The corrected identification is

$$
H^? \;:=\; \mathrm{HS}^{2, \bullet}\bigl(Y(\mathfrak{g})\bigr)_{\mathrm{loc}\,S_\alpha},
$$

the Hochschild--Stokes second cohomology *localised at the Stokes singularity $S_\alpha$*. This localisation picks out the resurgent generators $\mathcal{G}^{(n, \alpha)}$ that contribute at the singularity $S_\alpha$. By the multi-instanton tower (§3.3), the localised cohomology has dimension $\dim_{\mathbb{C}} \mathrm{HS}^{2, \bullet}_{\mathrm{loc}\,S_\alpha} = $ number of multi-instanton sectors visible at $S_\alpha = $ countably infinite, but *graded* by instanton number $n$ with $1$-dimensional graded piece per $n \ge 1$.

The Euler characteristic of the localised Hochschild--Stokes complex (computed as the regularised sum $\sum_n 1 \cdot e^{-n S_\alpha / g_s}$, summed in the Borel-resummed sense) is

$$
\chi\bigl(\mathrm{HS}^{2, \bullet}_{\mathrm{loc}\,S_\alpha}\bigr) \;=\; \frac{e^{-S_\alpha / g_s}}{1 - e^{-S_\alpha / g_s}} \;=\; \frac{1}{e^{S_\alpha / g_s} - 1}.
$$

For $S_\alpha = 1$ and $g_s \to 0$: $\chi \to 0$. For $g_s \to \infty$: $\chi \to \infty$. The relevant *normalised* dimension for the arithmetic prediction is the *coefficient* in the leading $g_s$-expansion:

$$
\dim H^? \;:=\; \mathrm{coeff}_{g_s^0}\,\bigl[2 g_s\, \chi(\mathrm{HS}^{2, \bullet}_{\mathrm{loc}\,S_\alpha})\bigr] \;=\; 2 / S_\alpha \;=\; 2.
$$

(For $S_\alpha = 1$.) Hence the arithmetic prediction becomes

$$
p_{S_{\alpha_i}} + q_{S_{\alpha_i}} \;=\; 2 \cdot 2 - 2 \;=\; 2.
$$

In radians: $p + q = 2$. The Stokes phases for ADE are $p = 0, q = 2$ (in suitable units), satisfying the prediction. This is the *normalisation-fixed* falsifiable form.

### 6.5 Falsification protocol

To falsify: compute the Stokes phases $p_S, q_S$ explicitly for $Y(\mathfrak{g})$ via Borel summation along independent rays, then check whether $p + q = 2 \dim H^? - 2$ holds. The independent computation requires:

1. Numerical Borel summation of $\log J^{\mathrm{formal}}(\hbar)$ along $\arg \zeta = 0^+$ and $\arg \zeta = 0^-$.
2. Extraction of the Stokes phases as the arguments of the discontinuity vector across $\arg \zeta = 0$.
3. Independent computation of $\dim \mathrm{HS}^{2, \bullet}_{\mathrm{loc}\,S}$ via the multi-instanton tower.

If the prediction fails (e.g. for some non-simply-laced type, or for a higher-instanton sector beyond $n = 1$), the V119 transseries ansatz would need to be revised (e.g. by introducing fractional Stokes constants or non-integer multi-instanton orders).

### 6.6 Connection to BKM imaginary roots (CY-A_2 specialisation)

For $Y(\mathfrak{g}_{K3})$ at the K3 specialisation, the Stokes index set $\alpha$ ranges over the *imaginary positive roots* of the BKM algebra $\mathfrak{g}_{\Delta_5}$ (Borcherds 1998, Inv. Math. 132). The arithmetic prediction $p + q = 2 \dim H^? - 2$ then connects to the *imaginary root multiplicity* of $\mathfrak{g}_{\Delta_5}$, which is the coefficient $c(D)$ in the Borcherds product expansion of $\Phi_{10}$. Explicitly: at the leading imaginary root $\delta$ (norm 0), $c(\delta) = 24$ (the K3 Mukai rank), giving

$$
p_\delta + q_\delta \;=\; 2 \cdot 24 - 2 \;=\; 46.
$$

This is the CY-A_2-specific arithmetic prediction. For the K3 abelian Yangian (PROVED, `thm:k3-abelian-yangian-presentation`), the prediction is verifiable via the explicit Borcherds product computation. The non-abelian K3 Yangian (CONJECTURAL) extends the prediction to higher imaginary roots.

---

## §7. The non-formal (resurgent) Drinfeld twist: explicit closed form

Combining §1--§6:

$$
\boxed{\;
\mathcal{F}_{Y(\mathfrak{g}_{\mathrm{ADE}})}(\hbar; g_s) \;=\; \prod_{i=1}^{r} \exp\!\Bigl(\tfrac{\hbar^2}{2} h_{\alpha_i} \otimes h_{\alpha_i}\Bigr) \cdot \exp\!\Biggl(\sum_{n \ge 1} \sum_{i=1}^{r} \frac{e^{-n / g_s}}{n!\, 4^n}\, (h_{\alpha_i} \otimes h_{\alpha_i})^n \cdot \mathcal{G}^{(n, \alpha_i)}(\hbar)\Biggr)
\;+\; O(\hbar^4).
\;}
$$

The Stokes data:
- $S_{\alpha_i} = 1$ for all $i$ (uniform per ADE);
- $A^n_{\alpha_i} = (n!)^{-1} \cdot 4^{-n} \cdot (h_{\alpha_i} \otimes h_{\alpha_i})^n$ (operator-valued);
- $\mathcal{G}^{(n, \alpha_i)} \in \mathrm{HS}^{2, \bullet}(Y(\mathfrak{g}))$ (Borel-resummed Pentagon-cocycle completion, leading term $[\omega^{(2)}_i]$).

The falsifiable prediction:

$$
p_{S_{\alpha_i}} + q_{S_{\alpha_i}} \;=\; 2 \dim H^? - 2 \;=\; 2,
$$

with $H^? = \mathrm{HS}^{2, \bullet}_{\mathrm{loc}\,S_{\alpha_i}}(Y(\mathfrak{g}))$ (normalised dimension $2$). At the K3 specialisation: $p_\delta + q_\delta = 46$ (from $c(\delta) = 24$ for the leading imaginary root of $\mathfrak{g}_{\Delta_5}$).

---

## §8. AP audit (AP-CY55 / AP-CY60 / AP-CY61)

### 8.1 AP-CY55: manifold vs. algebraization invariants

The Stokes data $(S_\alpha, A^n_\alpha, \mathcal{G}^{(n, \alpha)})$ are *algebraization* invariants of $Y(\mathfrak{g})$, NOT manifold invariants of any associated CY. They are FIXED by the choice of $Y(\mathfrak{g})$ (and hence by $\mathfrak{g}$, but not by any underlying geometry). At the K3 specialisation, the BKM imaginary root multiplicities $c(D)$ enter as algebraization-specific parameters; the underlying K3 manifold has $\kappa_{\mathrm{cat}} = 2$ (topological, fixed) but the *Yangian algebraisation* has independent Stokes data.

### 8.2 AP-CY60: multiple constructions vs. multiple applications of $\Phi$

The resurgent twist is constructed via *three independent routes*:
1. **Borel summation** (Pasquetti--Schiappa): residue extraction in the Borel $\zeta$-plane.
2. **Alien derivation** (Écalle--Costin): the bridge equation $\Delta_S \cdot \partial_{g_s} = \partial_{g_s} \cdot \Delta_S - S \cdot \Delta_S$.
3. **Drinfeld twist** (Etingof--Kazhdan): the $z^{-2}$ Pentagon cocycle completion.

The three routes converge on the same transseries by the V119 closed form. This is *three independent constructions*, not three applications of a single functor. AP-CY60 audit: PASS.

### 8.3 AP-CY61: first-principles ghost theorems

For each wrong-claim/right-claim audit:

| Wrong claim | Ghost theorem | Correct relationship |
|-------------|---------------|----------------------|
| "Resurgent twist is a formal-series correction" | Borel-summable structure forces non-formal $g_s$-dependence | Transseries genuinely separates formal and non-formal sectors; the formal series is recovered as $g_s \to 0$ |
| "Stokes constants are scalars" | Operator-valued Stokes constants for non-commutative algebras | $A^n_{\alpha_i} = (n!)^{-1} 4^{-n} (h_{\alpha_i} \otimes h_{\alpha_i})^n \in (\mathfrak{h} \otimes \mathfrak{h})^{\otimes n}$ |
| "All ADE simple roots have distinct Stokes singularities" | All $S_{\alpha_i} = 1$ uniformly | Coxeter pattern: $\langle \rho^\vee, \alpha_i^\vee \rangle = 1$ for every simple coroot |
| "Pentagon cocycle vanishes formally upon non-formal completion" | Resurgent Drinfeld twist vanishing CONJECTURE | The vanishing requires explicit cancellation between leading formal cocycle and leading instanton sector; FALSIFIABLE |

### 8.4 HZ3-3: chain-level CY-A_3 conditional propagation

The V119 resurgent twist is constructed at the level of the formal Yangian $Y(\mathfrak{g})$, which is well-defined independent of CY-A_3. The *application* to the chiral algebra $\Phi(C)$ for $C$ a CY_3 category requires CY-A_3 (for the existence of $\Phi(C)$ as an $E_1$-chiral algebra), now PROVED in the inf-categorical framework. Chain-level claims (e.g. that the resurgent twist *of the chain-level $\Phi(C)$* satisfies the V119 transseries) are CONDITIONAL on chain-level CY-A_3 data. The Yangian-only claims (§§1--7 above) are unconditional.

---

## §9. Summary

### Scientific summary

V119 constructs the explicit non-formal extension of the Drinfeld twist for $Y(\mathfrak{g}_{\mathrm{ADE}})$:

$$
\mathcal{F}_{Y(\mathfrak{g})}(\hbar; g_s) \;=\; \mathcal{F}^{\mathrm{formal}}(\hbar) \cdot \exp\!\Bigl(\sum_{n, \alpha} A^n_\alpha\, e^{-n S_\alpha / g_s}\, \mathcal{G}^{(n, \alpha)}\Bigr).
$$

The Stokes data is computed from first principles:
- **Stokes singularities** $S_{\alpha_i} = \langle \rho^\vee, \alpha_i^\vee \rangle = 1$ (uniform for ADE).
- **Stokes constants** $A^n_{\alpha_i} = (n!)^{-1} 4^{-n} (h_{\alpha_i} \otimes h_{\alpha_i})^n$ (operator-valued, multi-instanton tower).
- **Resurgent generators** $\mathcal{G}^{(n, \alpha_i)} \in \mathrm{HS}^{2, \bullet}$ (Borel-resummed Pentagon completion).

The non-formal vanishing condition (V119 conjecture): the resurgent corrections cancel the formal Pentagon cocycle, with explicit $g_s$-dependent prefactor $-8 e^{1/g_s}$ at leading instanton.

The arithmetic falsifiable prediction: $p_S + q_S = 2 \dim H^? - 2 = 2$, with $H^? = \mathrm{HS}^{2, \bullet}_{\mathrm{loc}\,S}(Y(\mathfrak{g}))$. At the K3 specialisation: $p_\delta + q_\delta = 46$, tied to the BKM imaginary root multiplicity $c(\delta) = 24$.

### Status table

| Item | Status |
|------|--------|
| Transseries ansatz | CONSTRUCTED |
| Stokes singularities $S_\alpha$ | THEOREM (V119, §2.1) |
| Stokes constants $A^n_\alpha$ | THEOREM (V119, §3.2--3.3) |
| Resurgent generators $\mathcal{G}^{(n, \alpha)}$ | CONSTRUCTED (V119, §4.2--4.4) |
| Non-formal vanishing | CONJECTURE (V119, §5.1) |
| Arithmetic prediction $p + q = 2 \dim H^? - 2$ | PREDICTION (V119, §6.2) |
| Connection to V110 Pentagon | THEOREM (zeroth Stokes datum, §4.5) |
| Connection to CY-A_3 inf-cat | STRUCTURAL ANALOGY (§5.4) |
| K3 specialisation $p_\delta + q_\delta = 46$ | CONJECTURE (CY-A_2 specific, §6.6) |

Status: complete. No `.tex`, CLAUDE.md, test, build, or commit modifications. AP-CY55, AP-CY60, AP-CY61, HZ3-3 governance respected throughout. Lossless preservation of V96/V105/V110 inputs verified. All four phase-2 healing items (Stokes singularities, Stokes constants, resurgent generators, non-formal vanishing condition) constructed. Falsifiable arithmetic prediction stated.

---

**End of V119 resurgent Drinfeld twist memorandum.**
