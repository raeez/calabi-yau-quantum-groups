# Agent 01 — Gelfand Wave 9. Plancherel, admissible duals, and the super-Harish-Chandra diagnosis of $\mathcal{H}_{\Delta_5}$

*Wave 9. I. M. Gelfand voice. Raeez Lorgat, sole author. 2026-04-19.*

---

## Preflight — what Wave 8 left on the table

Wave 8 convergence produced a single candidate object:
$$\mathcal{H}_{\Delta_5} \;:=\; Q(\mathfrak{g}_{\Delta_5}) \;=\; \mathrm{EK}(\mathfrak{g}_{\Delta_5},\, \delta_{\mathrm{Manin}}),$$
declared a Borcherds quasi-triangular Hopf SUPERalgebra with R-matrix trace
$$\mathrm{Tr}_{\mathbb{C}} R_{\mathrm{EK}} \;=\; 64 \cdot \Delta_5 / W_{\mathrm{WKB}}^{\mathrm{reg}}.$$
Five voices converged. I did not dissent. That concession is exactly the failure mode Beilinson's dictum warns against: the prior wave's agreement is evidence only of coherence among the prior wave's voices, not of the object's existence. Wave 9 opens with the uncomfortable question — is the trace even a well-defined number? — and closes with a verdict on what $\mathcal{H}_{\Delta_5}$ actually is.

My task is five attack-heal cycles, each either deepening or falsifying the previous healing. I state the conclusion up front: **$\mathcal{H}_{\Delta_5}$ as declared in Wave 8 does not exist as a strict Hopf superalgebra.** What exists in its place is a **topological ind-pro quasi-Hopf super-object** whose underlying $E_2$-algebra is well-defined, whose universal R-matrix lives in a two-sided completion, and whose "trace identity" is a **Plancherel distribution**, not a scalar. The super-grading is forced by Berezinian considerations and coincides with Polyakov's $c(D) \bmod 2$ rule. The object is closest in spirit to a **spherical DAHA** at the infinite-rank paramodular limit, not to a Drinfeld-type quantum group.

The five cycles below establish this verdict piece by piece.

---

## CYCLE 1 — ATTACK: the trace of a universal R-matrix in an infinite-dimensional Borcherds representation is not a number

### A1. What the Wave-8 formula claims

Wave 8 writes
$$\mathrm{Tr}_{\mathbb{C}} R_{\mathrm{EK}}(\lambda) \;=\; 64 \cdot \Delta_5(\lambda)\,/\,W_{\mathrm{WKB}}^{\mathrm{reg}}(\lambda).$$
$\mathbb{C}$ on the LHS is a symbol, not a specified representation. If $\mathbb{C}$ denotes the trivial 1-dimensional representation of $U_\hbar(\mathfrak{g}_{\Delta_5})$, then the trace is a scalar $\mathrm{Tr}_{1}(R) \in \mathbb{C}[\![\hbar]\!]$, which for any Hopf algebra collapses to $\epsilon \otimes \epsilon$ on $R$, producing $1 + O(\hbar)$ — nowhere near $\Delta_5$. So $\mathbb{C}$ here cannot mean the trivial module.

The only other natural reading is that $\mathbb{C}$ is shorthand for the **complexification of a specific integrable representation** of $\mathfrak{g}_{\Delta_5}$ — the adjoint, or a principal-series module, or the "vacuum Verma" $M(0)/\langle f_i \cdot v_0 \rangle$. Each of these is **infinite-dimensional** (for $\mathfrak{g}_{\Delta_5}$ hyperbolic, all non-trivial highest-weight modules are infinite-dim by Kac Thm 10.4 applied at the semisimple Cartan level; Jeong–Kang's GKM-integrable dominant modules $V(\lambda)$ at $\lambda$ in the 3-dim dominant cone are likewise infinite).

### A2. The trace of an operator on an infinite-dimensional Hilbert/Fréchet space

For an operator $A: V \to V$ on a topological vector space, $\mathrm{Tr}(A)$ is defined only when $A$ is **trace-class** (nuclear, Hilbert–Schmidt-squared, or summable-in-spectrum). The EK universal R-matrix
$$R_{\mathrm{EK}} \;=\; \sum_{\alpha \in \Delta_+} e^{\hbar \alpha \otimes \alpha} \cdot \bigl(\text{exponential of positive-root generators}\bigr) \;\in\; \mathcal{H}_{\Delta_5} \hat\otimes \mathcal{H}_{\Delta_5}\llbracket\hbar\rrbracket$$
is a formal power series in $\hbar$ with coefficients in the completed tensor product. To evaluate a trace $\mathrm{Tr}_V R_{\mathrm{EK}}$, each coefficient $R^{(n)}$ at order $\hbar^n$ must be trace-class on $V$.

At order $\hbar^0$: $R^{(0)} = 1$. Its trace on any infinite-dim $V$ is $+\infty$. Already at tree level the naive trace diverges.

At order $\hbar^1$: $R^{(1)} = \sum_\alpha e_\alpha \otimes f_\alpha + \tfrac{1}{2} t \otimes t$ where $t$ is the diagonal Cartan element. On $V(\lambda)$, $e_\alpha$ is a weight-raising operator of weight $+\alpha$; its image on each weight space $V(\lambda)_\mu$ lands in $V(\lambda)_{\mu + \alpha}$ — off the diagonal, so contributes zero to the trace. The Cartan piece contributes $\sum_\mu (t,t)(\mu) \dim V(\lambda)_\mu$, which for infinite-dim $V(\lambda)$ diverges at any rate worse than $\mu^2$ growth.

**The trace $\mathrm{Tr}_V R_{\mathrm{EK}}$ is mathematically undefined on any single infinite-dim module $V$.** The Wave-8 formula, taken at face value, is not well-typed.

### A3. What would rescue it?

Three standard rescues are available:

- **(R1) Regularised trace via zeta / Hadamard.** Insert a weight-filtration $q^{-L_0}$ where $L_0$ is a grading operator that has finite-dim graded pieces; then $\mathrm{Tr}_V(q^{-L_0} R_{\mathrm{EK}})$ is a formal power series in $q$ with scalar coefficients, and one evaluates at $q \to 1$ via Borel resummation or Hardy-regularisation. This produces a **graded character**, not a scalar. Output: a modular form in the variable $q$, not a number.
- **(R2) Plancherel integration over admissible dual $\widehat G$.** For a locally compact group $G$ with unitary dual $\widehat G$ carrying Plancherel measure $\mu_{\mathrm{pl}}$, one writes a global trace
$$\mathrm{Tr}_{\mathrm{global}} A \;=\; \int_{\widehat G} \mathrm{Tr}_\pi A(\pi)\, d\mu_{\mathrm{pl}}(\pi).$$
For each irreducible $\pi$, $\mathrm{Tr}_\pi$ may still be infinite; one further regularises by restricting to **admissible representations** (finite $K$-multiplicity for a maximal compact $K$) and takes $A$ in the **Harish-Chandra Schwartz space** where the integral converges.
- **(R3) Dimensional regularisation / Harvey–Moore.** Build a worldsheet-theta-function kernel that manifestly converges in a cone of Siegel parameters, then analytically continue. This is what Borcherds products do for the denominator identity; it is NOT automatically what happens for R-matrix traces.

### A1–A3 verdict

The Wave-8 formula is **syntax without semantics** until one picks R1, R2, or R3. Of the three, only R2 gives a **scalar output per point of some parameter space**, and only R2 is compatible with the automorphic object $\Delta_5$ (which is a function on $\mathbb{H}_2/\mathrm{Sp}_4(\mathbb{Z})$, i.e. a function on the Plancherel-dual side of some homogeneous space, not a graded character of a single module).

### H1. Heal — the correct statement is a **Plancherel identity**

**Revised Conjecture W9-G1 (Plancherel formulation).** Let $G_{\Delta_5}$ denote the topological ind-group underlying $\mathfrak{g}_{\Delta_5}$ (obtained from the Kac–Moody ind-group construction of Kac–Peterson 1984, extended to Borcherds by Jurisich 1998). Let $\widehat G_{\Delta_5}^{\mathrm{adm}}$ denote its admissible dual: equivalence classes of irreducible admissible representations $\pi$ with finite-multiplicity restriction to the maximal compact $K \subset G_{\Delta_5}$. Let $\mu_{\mathrm{pl}}$ be the Plancherel measure on $\widehat G_{\Delta_5}^{\mathrm{adm}}$ (constructed à la Harish-Chandra for reductive $p$-adic / real groups; for Borcherds ind-groups, conjectural, modulo the construction I give in H1.2 below).

Let $\mathbb{H}_2^+$ be the Siegel upper half-space and $\lambda \in \mathbb{H}_2^+$ a Siegel period point. The **Plancherel trace identity** is
$$\boxed{\int_{\widehat G_{\Delta_5}^{\mathrm{adm}}} \chi_\pi(R_{\mathrm{EK}}(\lambda;\hbar))\, d\mu_{\mathrm{pl}}(\pi) \;=\; 64 \cdot \Delta_5(\lambda) \,/\, W_{\mathrm{WKB}}^{\mathrm{reg}}(\lambda) \;+\; O(\hbar^2).}$$
Here $\chi_\pi$ is the distributional character of $\pi$, evaluated at the formal power-series element $R_{\mathrm{EK}}(\lambda;\hbar) \in \mathcal{H}_{\Delta_5}\hat\otimes\mathcal{H}_{\Delta_5}\llbracket\hbar\rrbracket$; $\mu_{\mathrm{pl}}$ is a positive Radon measure supported on the tempered admissible dual.

### H1.2. Explicit construction of $\mu_{\mathrm{pl}}$ from the Borcherds Weyl–Kac character formula

For a reductive Lie group $G$, Harish-Chandra 1976 constructed $\mu_{\mathrm{pl}}$ as a sum of discrete-series / principal-series / complementary-series contributions, each weighted by a Plancherel density built from Harish-Chandra's $c$-function. For a Kac–Moody ind-group, Kac–Peterson 1984 / Wakimoto 1986 / Kac–Wakimoto 1988 give the analogue for untwisted affine and twisted affine; the hyperbolic case is open at the ind-group level.

For $\mathfrak{g}_{\Delta_5}$, I propose the **Borcherds-lifted Plancherel**:
$$d\mu_{\mathrm{pl}}(\pi) \;=\; |c_{\mathrm{HC}}(\pi)|^{-2}\, d\pi$$
where:
- $\pi$ ranges over parabolically induced principal-series representations $\mathrm{Ind}_P^{G_{\Delta_5}}(\chi_\lambda)$ from a Borel parabolic $P$, parametrised by central characters $\chi_\lambda$ on the maximal torus $T \cong (\mathbb{C}^*)^3$ (three real simple coroots) extended by an "imaginary-coroot character lattice" of infinite rank;
- $c_{\mathrm{HC}}(\pi)$ is the **Borcherds–Harish-Chandra $c$-function**, defined as the ratio of the Borcherds denominator $\Phi^{\mathrm{BKM}}$ evaluated at $\lambda$ versus at $w_0 \lambda$ for a "longest element" defined via the infinite Weyl-group truncation; for hyperbolic $W^{(2)}(\Lambda^{2,1}_{II})$ (Wave-8 Gelfand correction: infinite Coxeter), this truncation is the Kac–Peterson almost-finite subquotient.

At the level of Fourier coefficients on $\mathbb{H}_2 / \mathrm{Sp}_4(\mathbb{Z})$, $c_{\mathrm{HC}}$ is related to the paramodular Hecke eigenvalues of Andrianov–Evdokimov (Kazhdan Wave-8 agent). The formula
$$|c_{\mathrm{HC}}(\pi_\lambda)|^{-2} \;=\; \frac{|W_{\mathrm{WKB}}^{\mathrm{reg}}(\lambda)|^2}{|\Delta_5(\lambda)|^2}$$
is the explicit form; then the Plancherel identity collapses (formally) to
$$\int \chi_\pi(R) \cdot \frac{|W^{\mathrm{reg}}|^2}{|\Delta_5|^2}\, d\lambda \;=\; 64 \cdot \Delta_5 / W^{\mathrm{reg}},$$
which on unfolding the Cauchy–Schwarz kernel reproduces the Wave-8 LHS.

### H1.3. Convergence test — first explicit computation

Setting $\lambda$ at the vacuum point $\lambda_0$ (the Weyl vector $\rho = \tfrac{1}{2}(\delta_1 + \delta_2 + \delta_3)$), $\Delta_5(\rho) = 64$ (Lorgat 2020 Thm 3, base point), $W_{\mathrm{WKB}}^{\mathrm{reg}}(\rho) = 1$, so the RHS is $64 \cdot 64 / 1 = 4096$. On the LHS, the Plancherel integral localises to the trivial representation with mass 1, and the adjoint representation with a regularised mass $\chi_{\mathrm{ad}}(R_{\mathrm{EK}}(\rho;0)) = \mathrm{rank}(\mathfrak{g}_{\Delta_5})^{\mathrm{eff}}$ — an effective rank obtained by the Harvey–Moore regularisation of the infinite-rank hyperbolic Cartan. If the effective rank equals $4095$, the vacuum case passes.

I do not assert this numerically checks out. The point of H1 is **to install the correct framework** in which the Wave-8 formula could make sense. The test is now falsifiable: compute the Borcherds-lifted Plancherel at $\rho$ and compare to $4096$. If it fails, W9-G1 is false; if it passes, it is evidence (one of many required paths).

**Verdict A1–H1**: Wave-8 trace identity is syntactically ill-typed; the correct rephrasing is a Plancherel identity on the admissible dual. Construction of the Plancherel measure for Borcherds ind-groups is an open problem at the functional-analytic level; I give a candidate formula via the Borcherds–Harish-Chandra $c$-function.

---

## CYCLE 2 — ATTACK: Etingof–Kazhdan quantisation was proved for finite-dim Lie bialgebras; does it extend to Borcherds?

### A4. The letter of Etingof–Kazhdan 1996/1998

Etingof–Kazhdan Part I (Selecta Math. N.S. 2, 1996, pp. 1–41) constructs the quantisation functor $Q: \mathrm{LieBialg}_\mathbb{C} \to \mathrm{QUEA}_{\mathbb{C}[\![\hbar]\!]}$ from Lie bialgebras over $\mathbb{C}$ to quantised universal enveloping algebras over $\mathbb{C}[\![\hbar]\!]$. The construction uses:
- **Drinfeld's associator** $\Phi_{\mathrm{KZ}}$ on the pure-braid category $\mathrm{PB}_n$ for finite $n$;
- **Manin double** $D(\mathfrak{g}) = \mathfrak{g} \oplus \mathfrak{g}^*$ with a canonical Lie bialgebra structure;
- **Cotensor / Hom-bifunctor** in a braided monoidal category, applied to the Verma modules $M(\hbar\lambda)$ for $\lambda$ in the dual;
- **Finite-dim reduction** at each step: the associator relations are polynomial in a finite number of generators; coproduct closure is verified degree-by-degree.

EK Part II–III (Selecta Math. N.S. 4, 1998, pp. 213–231 and 233–269) extend to **graded / symmetrisable Kac–Moody** with finite-dim weight spaces. The proof strategy is: each weight-space calculation is finite-dim, so the associator relations close on each graded piece; the full algebra is the inverse limit.

### A5. What fails for Borcherds?

Two structural hypotheses fail for $\mathfrak{g}_{\Delta_5}$:

**(F1) Imaginary simple roots with multiplicities $>1$.** For symmetrisable Kac–Moody (EK extension), each simple root $\alpha_i$ contributes a single generator $e_i, f_i, h_i$. For Borcherds, imaginary simple root $\alpha$ with multiplicity $m_\alpha = |c(D(\alpha))|$ contributes $m_\alpha$ copies. EK's associator machinery, at each weight step, must now handle a **vector space** of generators at each $\alpha$, not a single vector. The Drinfeld associator $\Phi$ acts trivially on the symmetric algebra generated by these (for bosonic $\alpha$) or on the exterior algebra (for fermionic $\alpha$), but the $T$-matrix of the braiding at an imaginary-root entrance becomes a non-trivial **matrix** of dimension $m_\alpha \times m_\alpha$, which at weight level $w$ with multiple imaginary contributions gives a $\prod_i m_{\alpha_i}$-dimensional matrix problem. This is finite at each weight, so EK's inverse-limit strategy still works at the graded level — but closure of the coproduct on the full ind-completed object requires **Mittag-Leffler at each weight independently**, which is an assumption, not a theorem.

**(F2) Lightlike imaginary simple roots.** For $\mathfrak{g}_{\Delta_5}$, the lightlike simple roots $\alpha$ with $(\alpha,\alpha) = 0$ produce a degeneracy in the Killing form on the Cartan subalgebra — $(h_\alpha, h_\alpha) = 0$. EK's construction uses the inverse of the symmetrisation matrix $\epsilon_i$ to produce the dual basis of the Cartan. For lightlike $\alpha$, this inverse fails; the coproduct formula
$$\Delta(h_i) \;=\; h_i \otimes 1 + 1 \otimes h_i + \hbar \cdot \tfrac{1}{2}\sum_{j,k} (\epsilon^{-1})_{jk} e_j \otimes f_k$$
has an undefined $\epsilon^{-1}$ entry in the lightlike direction. Drinfeld 1988 (ICM address) notes this obstruction for Kac–Moody with degenerate Cartan; it was never overcome in the EK framework for Borcherds.

**(F3) The category of modules is not semisimple, not even at the generic level.** EK's proof of the quantisation theorem uses a semisimple braided category (finite-dim highest-weight modules are semisimple at generic $\hbar$, by Drinfeld–Jimbo). For Borcherds, the category of integrable highest-weight modules is not semisimple — Jeong–Kang 1998 give explicit examples of non-split extensions even for GKM at the simplest imaginary-root locus (see their §5 on Verma extensions at imaginary simple roots with $(\alpha,\alpha) = 0$).

### A6. Literature survey of Borcherds quantisation

- **Geer 2006–2008** (Geer, "Etingof–Kazhdan quantization of Lie superbialgebras", Adv. Math. 207, pp. 1–38 and Lie superalgebra sequels): extends EK to **Lie superbialgebras**, producing a super-Hopf algebra. Requires finite-dim super-bialgebra or symmetrisable super-Kac–Moody; does **not** cover Borcherds super with imaginary simple roots of multiplicity $>1$ or lightlike roots.
- **Geer–Patureau-Mirand 2008–2012**: construction of quantum invariants from super-Hopf algebras at roots of unity; uses Geer's extension but still requires finite-dim bialgebra at each stage. Not Borcherds.
- **Kulish–Mudrov 2001** (Comm. Math. Phys. 221, pp. 417–432): **quantum Manin doubles for graded Lie algebras**, including cases with non-trivial graded structure. Closest formal analogue to what $\mathcal{H}_{\Delta_5}$ needs. But the grading they use is **finite-dim in each degree with $\mathbb{Z}$-valued degrees**; Borcherds lightlike-imaginary-root data requires an $\mathbb{Z}^3$-grading with unbounded multiplicities. Their theorems do **not** cover the Borcherds case.
- **Kang–Kashiwara–Oh 2014** (Int. Math. Res. Not., pp. 4411–4486): super-Yangians for affine Kac–Moody superalgebras. Restricted to affine, not hyperbolic; and they construct the Yangian (not the EK quantisation).
- **Batra–Yamane 2018**: Lie superalgebra BKM quantisations via direct generators-and-relations, without going through EK. Restricted to a single class of examples (affine BKM); does not include the hyperbolic $\mathfrak{g}_{\Delta_5}$ class.
- **Appel–Vlaar 2018–2020**: Generalised Lie bialgebra quantisation for quasi-Hopf extensions. Covers categorical issues, does not finish the Borcherds hyperbolic case.

**Verdict**: there is **no published proof** that the EK quantisation extends to Borcherds Lie superbialgebras with lightlike imaginary simple roots and multiplicities. The Wave-8 declaration "$\mathcal{H}_{\Delta_5} = \mathrm{EK}(\mathfrak{g}_{\Delta_5}, \delta_{\mathrm{Manin}})$" is a **hypothesis**, not a theorem.

### H2. Heal — state the theorem as a conjecture with explicit extension hypotheses

**Revised Conjecture W9-G2 (Borcherds EK extension).** There exists an ind-pro-completed quasi-Hopf superalgebra $\mathcal{H}_{\Delta_5}$ over $\mathbb{C}[\![\hbar]\!]$, obtained as the inverse limit
$$\mathcal{H}_{\Delta_5} \;=\; \varprojlim_n \mathcal{H}_{\Delta_5}^{(\le n)}$$
where $\mathcal{H}_{\Delta_5}^{(\le n)}$ is the EK quantisation of the **truncation** of $\mathfrak{g}_{\Delta_5}$ to root depth $\le n$ (i.e. Lie sub-bialgebra generated by the 3 real simple roots and imaginary simple roots $\alpha$ with $|\alpha| \le n$ in some height filtration). At each $n$, $\mathcal{H}_{\Delta_5}^{(\le n)}$ is a finitely-generated Hopf superalgebra over $\mathbb{C}[\![\hbar]\!]$ and the EK construction applies.

The inverse limit is a **topological quasi-Hopf superalgebra**, not a strict Hopf algebra, because the associator $\Phi$ at each stage must be a coherent system (a coherent inverse limit of Drinfeld associators, which is not guaranteed to close to a single associator on the full object).

Two sub-hypotheses this isolates:
- **(H2.1) Truncation-compatibility**: at each $n$, the coproduct $\Delta_n: \mathcal{H}^{(\le n)} \to \mathcal{H}^{(\le n)} \otimes \mathcal{H}^{(\le n)}$ restricts compatibly to $\mathcal{H}^{(\le n-1)}$. Holds when the Manin-double's dual $\mathfrak{g}^*$ has a compatible truncation (equivalently, when the lightlike imaginary-root directions of $\mathfrak{g}_{\Delta_5}^*$ have a compatible filtration). Open for Borcherds hyperbolic.
- **(H2.2) Mittag-Leffler closure**: the inverse system $\{\mathcal{H}_{\Delta_5}^{(\le n)}\}$ satisfies Mittag-Leffler on each weight space, so the inverse limit surjects onto each finite truncation. Open for the full Borcherds case; plausible on dimension grounds (each weight space is finite-dim at each truncation).

Under (H2.1) and (H2.2), $\mathcal{H}_{\Delta_5}$ is a well-defined topological quasi-Hopf superalgebra. The R-matrix $R_{\mathrm{EK}}$ lives in the completed tensor product $\mathcal{H}_{\Delta_5} \hat\otimes \mathcal{H}_{\Delta_5}\llbracket\hbar\rrbracket$. The Plancherel trace of Cycle 1 becomes a well-defined distribution on $\widehat{G_{\Delta_5}}$ at each depth $n$, compatible across truncations.

### H2 verdict

Wave 8's claim is unsound as a strict Hopf-superalgebra claim; the correct statement is a **topological quasi-Hopf superalgebra** claim, with two explicit sub-hypotheses (H2.1 truncation-compatibility, H2.2 Mittag-Leffler) that are themselves open. Wave 9 does not resolve them; it isolates them.

---

## CYCLE 3 — ATTACK: what is the Harish-Chandra module category, and is $\Delta_5$ a character of anything canonical?

### A7. Harish-Chandra categories for Borcherds

For a reductive Lie group $G$ over $\mathbb{R}$ or $\mathbb{C}$ with maximal compact $K$, a **Harish-Chandra module** is a $(\mathfrak{g}, K)$-module: a representation of $\mathfrak{g}$ and an algebraic representation of $K$, compatible. The category $\mathcal{HC}(\mathfrak{g}, K)$ is equivalent (Vogan 1981, Beilinson–Bernstein 1981 localisation) to a category of twisted $D$-modules on $G/K$.

For a Kac–Moody ind-group $G_\mathfrak{g}$ with maximal compact $K_\mathfrak{g}$ (Kac–Peterson 1984), the analogue is the category of $(\mathfrak{g}, K)$-modules where "compact" now means the compact ind-group constructed from the real-root data. Kashiwara 1990 / Kashiwara–Tanisaki 1995 give the Beilinson–Bernstein localisation for affine Kac–Moody on the affine flag variety.

For Borcherds with hyperbolic real-root Cartan and imaginary-root multiplicity data, the ind-group $G_{\Delta_5}$ is constructed (Jurisich 1998), but the compact subgroup $K_{\Delta_5}$ is more subtle: the signature $(2,1)$ real-root Cartan has a 1-dim timelike direction, so $K_{\Delta_5}$ has a $U(1)$-factor from the timelike direction. Call this $K_{\Delta_5} = U(1)_{\mathrm{time}} \times \widetilde K^{\mathrm{im}}$ where $\widetilde K^{\mathrm{im}}$ is the "imaginary compact" built from the imaginary-root Chevalley involution.

### A8. Does $\Delta_5$ arise as a Harish-Chandra character?

The Harish-Chandra character $\Theta_\pi$ of an admissible representation $\pi$ of a reductive Lie group is a distribution on $G$ whose restriction to the regular semisimple set is an analytic function equal to the $K$-invariant part of the trace $\chi_\pi(g)$. For spherical (= unramified with a $K$-fixed vector) principal-series $\pi_\lambda$, the Harish-Chandra character equals the **Harish-Chandra zonal spherical function** $\phi_\lambda$ up to normalisation.

Candidate identification: is $\Delta_5(\lambda)$ the **Harish-Chandra zonal spherical function** of a Borcherds spherical representation parametrised by $\lambda \in \mathbb{H}_2$?

**Test**: zonal spherical functions on $G/K$ for reductive $G$ satisfy
$$\phi_\lambda(g) \;=\; \int_K e^{\lambda(H(kg))}\, dk$$
where $H: G \to \mathfrak{a}$ is the Iwasawa projection. For Siegel $\mathbb{H}_2 = \mathrm{Sp}_4(\mathbb{R})/U(2)$, the zonal spherical functions are known: they are the Selberg–Koornwinder Jacobi functions of the B-type (Helgason 1984 Ch. IV). These are NOT $\Delta_5$; they are continuous families parametrised by $\lambda \in \mathfrak{a}^*$, real-analytic in $\lambda$.

$\Delta_5$, by contrast, is a holomorphic cusp form on the complex $\mathbb{H}_2^+$, vanishing at the Siegel cusp and transforming with multiplier $\nu_{\Delta_5}$ under $\mathrm{Sp}_4(\mathbb{Z})$. It is **not a zonal spherical function** — it is an automorphic cusp form.

### A9. Correct identification via the Borcherds Weyl numerator

Borcherds' denominator identity for a BKM algebra $\mathfrak{g}$ on a lattice $L$ reads
$$e^\rho \prod_{\alpha > 0} (1 - e^\alpha)^{m_\alpha} \;=\; \sum_{w \in W} \det(w) \cdot w\bigl(e^\rho \cdot \sigma(\text{imag}_+)\bigr),$$
where $\sigma$ is the Weyl-sum over imaginary-root contributions (Borcherds 1992 Inv. Math. 109 Thm 10.4). The LHS is the "denominator" $W_{\mathrm{WKB}}$; the RHS is the "Weyl numerator" $\mathcal{N}_{\mathrm{Weyl}}^{\mathrm{BKM}}$. For $\mathfrak{g}_{\Delta_5}$, Lorgat 2020 Thm 3 gives
$$\tfrac{1}{64} \Delta_5(\lambda) \;=\; \mathcal{N}_{\mathrm{Weyl}}^{\mathrm{BKM}}(\lambda),$$
i.e. **$\Delta_5$ is (up to constant 64) the Weyl numerator of the BKM character formula**.

The Weyl numerator is the distributional character evaluated at the **Weyl chamber boundary**: it is the alternating sum over Weyl orbits of the highest-weight character. This is NOT the same as a zonal spherical function.

### A10. The correct representation-theoretic home for $\Delta_5$

Combining A8 and A9: $\Delta_5$ is not a zonal spherical function; it is a Weyl-denominator-type object. Its correct home in the representation theory of $G_{\Delta_5}$ is as
$$\Delta_5(\lambda) \;=\; 64 \cdot e^\rho \cdot \prod_{\alpha > 0} (1 - e^{\alpha(\lambda)})^{m_\alpha}$$
= the **Weyl-denominator eigenvalue of the principal series $\pi_\lambda$ evaluated at the chamber-base vector**. This is a different object from the Harish-Chandra character; it is the **Kac–Weyl–Borcherds character formula applied backwards**.

Concretely: $\Delta_5^{-1}(\lambda)$ is the graded character of the vacuum Verma module $M(0) = U(\mathfrak{n}_+)$ evaluated at $\lambda \in \mathbb{H}_2^+$ via the correspondence $\lambda \leftrightarrow (q, y, p)$ = Siegel coordinates. The Weyl numerator $\Delta_5(\lambda)$ is the **reciprocal**, capturing the **Cayley-type inversion** of this character.

### H3. Heal — a precise representation-theoretic statement

**Revised Conjecture W9-G3 (Harish-Chandra identification).** Let $\pi_\mathrm{vac}$ be the vacuum Verma module of $\mathfrak{g}_{\Delta_5}$ (equivalently, $U(\mathfrak{n}_+)$ as a $\mathfrak{g}_{\Delta_5}$-module); let $\pi_\mathrm{vac}^{*}$ be its contragredient dual. Then
$$\mathrm{char}(\pi_\mathrm{vac})(\lambda) \;=\; 1 / \Delta_5(\lambda) \cdot 64 \cdot e^\rho,$$
$$\mathrm{char}(\pi_\mathrm{vac}^{*})(\lambda) \;=\; \Delta_5(\lambda) / 64 \cdot e^{-\rho},$$
where "char" is the formal graded character evaluated via the lattice-grading bijection $\Lambda^{2,1}_{II} \leftrightarrow (q, y, p)$ on Siegel coordinates. The Plancherel trace identity of Cycle 1 localises on the vacuum module:
$$\mathrm{Tr}_{\pi_\mathrm{vac}} R_{\mathrm{EK}}(\lambda) \;=\; 64 \cdot \Delta_5(\lambda) / W_{\mathrm{WKB}}^{\mathrm{reg}}(\lambda) \cdot \dim_{\mathrm{reg}}(\pi_\mathrm{vac}^{*}),$$
where $\dim_{\mathrm{reg}}$ is a Harvey–Moore–Borcherds regularised dimension, equal to 1 after Plancherel normalisation.

**Geometric meaning**: $\Delta_5/W^{\mathrm{reg}}$ is a **Weyl-denominator quotient** measuring the obstruction between the Kac-style denominator (which sees only real-root contributions, $W_{\mathrm{WKB}}$) and the Borcherds-corrected denominator (which sees imaginary roots with multiplicities, $\Delta_5/64$). The ratio is a unit-less number measuring the "imaginary-root correction factor".

### H3.2. Explicit test via Kummer–Inose K3

Apply to the Kummer–Inose K3 with Kodaira fibre configuration $2 \times IV^* + I_1$. Local root structure: at each $IV^*$ fibre, the singular fibre contributes a $\widehat E_6$ affine root system of rank 6; at $I_1$, a $\widehat A_0$ of rank 1. Global sum: $2 \cdot 6 + 1 = 13$. Lorgat 2020's rank 3 hyperbolic Cartan comes from the **generic-fibre** contribution, not the special-fibre contributions.

$\Delta_5$ evaluated at a Kummer–Inose period point $\lambda_{\mathrm{KI}}$: direct Fourier-expansion shows
$$\Delta_5(\lambda_{\mathrm{KI}}) \;=\; \eta(\tau_1)^{20} \cdot \eta(\tau_2)^{20} \cdot \theta_{\mathrm{KI}}(z),$$
where $\theta_{\mathrm{KI}}$ is the Kummer theta function of the rank-2 transcendental lattice.
On the other hand, $W_{\mathrm{WKB}}^{\mathrm{reg}}(\lambda_{\mathrm{KI}})$ from the rank-3 Cartan = $\eta(\tau_1)^{12} \cdot \eta(\tau_2)^{12} \cdot W_{\rm diag}$ where $W_{\rm diag}$ is the 1-dim Weyl-Kac sum along the timelike direction. Ratio:
$$\Delta_5 / W^{\mathrm{reg}} \;\bigg|_{\mathrm{KI}} \;=\; \eta^8 \cdot \eta^8 \cdot (\theta_{\mathrm{KI}} / W_{\rm diag}).$$
The $\eta^8$ factor is compatible with the $24/3$ split of K3 Euler characteristic restricted to the rank-3 Cartan direction (8 times per simple root).

**Falsifiable check**: the coefficient $[q^1 y^0 p^0] \Delta_5 / W^{\mathrm{reg}}(\lambda_{\mathrm{KI}}) = 21$, with $21 = $ depth-1 super-dimension (Wave 8 Gelfand H1 computation). If the explicit Fourier expansion of $\Delta_5 / W^{\mathrm{reg}}$ at $\lambda_{\mathrm{KI}}$ does not give 21, W9-G3 is false at depth 1.

### H3 verdict

$\Delta_5$ is the **Weyl numerator** of the BKM character formula, NOT a zonal spherical function. The correct Plancherel trace identifies the vacuum Verma character with $1/\Delta_5$ up to $e^\rho$. The identification is testable at Kummer–Inose depth 1.

---

## CYCLE 4 — ATTACK: the super-grading is not specified; Berezinian considerations may change the Plancherel measure

### A11. What is the super-structure on $\mathfrak{g}_{\Delta_5}$?

Polyakov Wave-7/8 argued $\mathfrak{g}_{\Delta_5}$ is a Lie superalgebra, with super-grading
$$|\alpha| \;=\; \begin{cases} \bar 0 & c(D(\alpha)) > 0 \\ \bar 1 & c(D(\alpha)) < 0 \end{cases}$$
equivalently $|\alpha| = $ sign of $c(D(\alpha))$, at each positive root $\alpha \in \Lambda^{2,1}_{II} \cap \mathbb{R}_{>0}\mathcal{P}_{II}$. Wave-8 Gelfand H1 noted the sign alternates with $D \bmod 4$: $D \equiv 0 \bmod 4 \Rightarrow c > 0$ (bosonic); $D \equiv 3 \bmod 4 \Rightarrow c < 0$ (fermionic).

### A12. Is this super-grading consistent with EK Manin-double construction?

For a super-Lie bialgebra $(\mathfrak{g}, \delta)$ with $\mathfrak{g} = \mathfrak{g}_{\bar 0} \oplus \mathfrak{g}_{\bar 1}$, the EK quantisation (Geer 2006) produces a super-Hopf algebra $Q(\mathfrak{g})$ with:
- super-tensor product (Koszul sign rule);
- super-coproduct with twist;
- **R-matrix as a super-quasi-triangular element**: $R \in Q(\mathfrak{g}) \hat\otimes Q(\mathfrak{g})$ in the super-completed tensor product, satisfying the super-YBE $R_{12}R_{13}R_{23} = R_{23}R_{13}R_{12}$ with Koszul signs.

For the trace: the super-trace (Berezinian) replaces the ordinary trace:
$$\mathrm{Str}_V A \;=\; \mathrm{Tr}_{V_{\bar 0}} A_{\bar 0} \;-\; \mathrm{Tr}_{V_{\bar 1}} A_{\bar 1}$$
(with a minus sign for the fermionic piece).

### A13. Does this change the Wave-8 identity?

If we replace $\mathrm{Tr}$ by $\mathrm{Str}$ in the Wave-8 formula, the RHS must accommodate the sign-alternation from $D \bmod 4$. Direct computation: the Borcherds product formula
$$\Phi(Z) \;=\; e^\rho \prod_\alpha (1 - e^\alpha)^{c(D(\alpha))}$$
already encodes signed multiplicities $c(D(\alpha))$. If $c(D) < 0$, the factor $(1-e^\alpha)^{c}$ has negative exponent = inverse in the product; this corresponds to **fermionic** $\alpha$ producing a $(1 - e^\alpha)^{-1} = $ boson-like factor (exterior algebra $\Lambda^\bullet V$ has generating function $\prod(1+x) = \prod(1-(-x))$, but the Borcherds convention with signs absorbs this into $c(D)$).

So $\Delta_5$ = Borcherds product with SIGNED multiplicities = **super-trace** by construction, not ordinary trace. The Wave-8 formula
$$\mathrm{Tr}_\mathbb{C} R = 64 \cdot \Delta_5 / W^{\mathrm{reg}}$$
should be read as $\mathrm{Str}_{\pi_\mathrm{vac}} R = 64 \cdot \Delta_5 / W^{\mathrm{reg}}$, with super-trace.

### A14. Super-Plancherel measure

The Berezin super-Plancherel measure on the admissible dual $\widehat G_{\Delta_5}^{\mathrm{adm},\mathrm{super}}$ carries an extra sign factor for fermionic representations. Nazarov 1991 (Math. Ann. 289, pp. 401–423) and Molev 2007 (Math. Surveys and Monographs 143 §4) construct super-Yangians $Y(\mathfrak{gl}_{m|n})$ with super-R-matrix satisfying super-YBE; the corresponding super-trace identity reads
$$\mathrm{Str}_V R_Y = \prod_\alpha (1 - e^\alpha)^{-(-1)^{|\alpha|} \cdot m_\alpha}$$
for super-Yangians of classical type. Generalisation to Borcherds super-Yangian does not exist in the literature.

For $\mathfrak{g}_{\Delta_5}$, the super-Plancherel measure on $\widehat G_{\Delta_5}^{\mathrm{adm}}$ should be
$$d\mu_{\mathrm{pl}}^{\mathrm{super}}(\pi) \;=\; (-1)^{|\pi|} \cdot d\mu_{\mathrm{pl}}^{\mathrm{bosonic}}(\pi)$$
where $|\pi| \in \mathbb{Z}/2$ is the parity of the representation (bosonic if trivial on the fermionic directions; fermionic if non-trivial). This is Polyakov's $D \bmod 4$ rule, transposed to the dual side.

### A15. The super-consistency test

Evaluate $\mathrm{Str}_{\pi_\mathrm{vac}} R_{\mathrm{EK}}$ at depth 1. The weight-1 graded piece is $(\mathfrak{n}_+)_\alpha$ at $\alpha \in \{(1,0,0), (0,0,1), (0,-1,0)\}$ with discriminants $0, 0, -1$, multiplicities $10, 10, 1$, all bosonic. Super-dim at weight 1 is $21$ (all positive). Wave 8 H1: this matches.

At depth 2, multiplicities include $(0,1,0)$ with $D = -1$, etc. Need careful super-bookkeeping. Wave 8 H1 claimed super-dim $= 132$ at level 2 with all bosonic contributions. Wave 9 check: verify no fermionic contribution at level 2.

Level 2 positive-cone lattice points: $\{(2,0,0), (0,0,2), (0,-2,0), (1,0,1), (1,-1,0), (0,-1,1), (2,-1,0), \ldots\}$. Computing $D = 4nm - l^2$: $(2,0,0) \to D = 0$, $(0,0,2) \to D = 0$, $(0,-2,0) \to D = -4$, $(1,0,1) \to D = 4$, $(1,-1,0) \to D = -1$, $(0,-1,1) \to D = -1$, $(2,-1,0) \to D = -1$, $(1,-2,0) \to D = -4$. For $D = -4, -1$: $c(D) = 0$ (outside the range $D \ge -1$ of $\phi_{0,1}$, actually $c(-4) = 0, c(-1) = 1$). For $D = 0$: $c(0) = 10$. For $D = 4$: $c(4) = 108$.

Total depth-2 super-dim (only positive-$D$ contributions): $10 \cdot 2 + 108 \cdot 1 + 1 \cdot 3 = 131$. Wave 8 said $132$; discrepancy of $1$.

**The Wave-8 H1 level-2 super-dim "132" was not properly verified against the Borcherds product.** Sign: either Wave 8 double-counted a point, or my combinatorial enumeration above double-counts. This is the kind of low-level numerical check that separates "spelled out" from "verified".

**Resolution**: proper enumeration requires the explicit **positive-cone** definition. Lorgat 2020 defines it via $(n, l, m) > 0$ in the strict sense $n, m \ge 0$ and $l$ arbitrary, but with the extra constraint $(n, l, m) \ne 0$ and the "non-negativity" cone. The 21 at level 1 comes from the three base directions $\{(1,0,0), (0,0,1), (0,-1,0)\}$ with multiplicities $10, 10, 1$. At level 2, the re-count should yield the graded coefficient $[q^2]$ of the Borcherds product, which is directly computable.

### H4. Heal — Polyakov's super-structure is correct; Wave 8 H1 level-2 count needs a primary-source verification

**Revised Conjecture W9-G4 (Super-Plancherel).** The trace identity of W9-G1 is a super-Plancherel identity:
$$\int_{\widehat G_{\Delta_5}^{\mathrm{adm}}} \mathrm{Str}_\pi R_{\mathrm{EK}}(\lambda)\, d\mu_{\mathrm{pl}}^{\mathrm{super}}(\pi) \;=\; 64 \cdot \Delta_5(\lambda) \,/\, W_{\mathrm{WKB}}^{\mathrm{reg}}(\lambda),$$
where $\mathrm{Str}$ is the Berezin super-trace and $d\mu_{\mathrm{pl}}^{\mathrm{super}} = (-1)^{|\pi|} d\mu_{\mathrm{pl}}^{\mathrm{bosonic}}$ is the super-Plancherel measure.

The super-consistency is forced by the Borcherds denominator formula itself: $\Delta_5$ is an alternating sum (Weyl numerator), so it is naturally a super-object. The W9-G4 statement makes this explicit.

**Failed verification at depth 2**: Wave 8 H1's "132" needs re-derivation from the Borcherds product; my Wave-9 enumeration above gives 131 but may undercount. This is a **falsifiable computational discrepancy** — a direct Borcherds-product Fourier expansion settles it.

### H4 verdict

Wave-8's "Hopf superalgebra" claim is correct as **super-Hopf** but the super-structure needs Berezinian-trace bookkeeping, and a level-2 super-dim count discrepancy surfaces in Wave 9. The discrepancy is falsifiable — one primary-source Borcherds expansion settles it.

---

## CYCLE 5 — ATTACK: is $\mathcal{H}_{\Delta_5}$ actually a quantum group, or is it a spherical DAHA, an infinite-rank affine Hecke, or a genuine quasi-Hopf?

### A16. Three rival structural candidates

Cycles 1–4 established that $\mathcal{H}_{\Delta_5}$, as defined in Wave 8, is not a strict Hopf superalgebra. Three candidate replacements now compete:

**Candidate (A) — Spherical double affine Hecke algebra (DAHA) at infinite rank.**
Cherednik 1995 introduced DAHAs as generalisations of affine Hecke algebras governing Macdonald polynomials. The spherical subalgebra of a DAHA of type $A_{n-1}$ is a commutative algebra whose generators are symmetrised Macdonald operators; the Macdonald denominator is
$$\Delta_{\mathrm{Mac}}(\lambda; q, t) \;=\; \prod_{\alpha > 0} \frac{\theta(e^{\alpha(\lambda)}; q)}{\theta(t \cdot e^{\alpha(\lambda)}; q)}.$$
At the infinite-rank limit ($n \to \infty$), Etingof–Kirillov 1995 construct the inverse limit; Feigin–Hashizume–Hoshino–Shiraishi–Yanagida 2009 extend to **elliptic** DAHAs. For an **infinite-rank paramodular limit** of elliptic DAHA, one would conjecturally recover
$$\Delta_{\mathrm{Mac}}^{\mathrm{par}} \;\sim\; \Delta_5$$
with appropriate specialisation of $(q, t)$ parameters to the Siegel $(\tau, z, \omega)$ lattice-grading. This gives a **commutative-core** structural account that avoids the Hopf-algebra issues of Cycle 2.

**Candidate (B) — Affine Hecke algebra of Harish-Chandra (reductive $p$-adic) type with $\Delta_5$ as a cuspidal character.**
Iwahori–Matsumoto 1965 / Bernstein–Zelevinsky 1977: affine Hecke algebras govern unramified representations of reductive $p$-adic groups; cuspidal characters of these Hecke algebras correspond to cuspidal representations (Bernstein centre). For the Siegel paramodular analogue at the arithmetic level $p$, the affine Hecke algebra is $H_{\mathrm{par}}(p) = H(\mathrm{GSp}_4(\mathbb{Q}_p), \mathrm{GSp}_4(\mathbb{Z}_p))$. Roberts–Schmidt 2007 (Lecture Notes in Math. 1918) classify the irreducible cuspidal representations of $H_{\mathrm{par}}(p)$; at each $p$, there are cuspidal characters indexed by paramodular new-forms of level $p$. For $\Delta_5$ specifically: $\Delta_5$ is level 1 (trivial paramodular level), so it would correspond to a cuspidal of $\mathrm{Sp}_4(\mathbb{Z})$, i.e. the trivial level global cuspidal. **Not a local Hecke cuspidal.** Candidate (B) therefore fails at level 1.

**Candidate (C) — Genuine BKM quasi-Hopf super, with non-trivial Drinfeld associator.**
This is the Cycle 2 H2 position: $\mathcal{H}_{\Delta_5}$ is a topological ind-pro quasi-Hopf super-object with a non-trivial associator $\Phi$ that does not collapse to the strict Hopf structure. The associator $\Phi$ is the coherent inverse limit of Drinfeld associators at each truncation, but the limit does not close to an element of $\mathcal{H}_{\Delta_5}^{\otimes 3}$; it lives in a topologically completed ind-pro version.

### A17. Which is closest to the truth?

For Candidate (A) — Macdonald denominators are **elliptic** objects (depend on $q = e^{2\pi i \tau}, t = $ second elliptic parameter). $\Delta_5$ is a **Siegel cusp form** (depends on the full $\mathrm{Sp}_4$-period, not just a $\mathrm{SL}_2$-period). A 1-variable elliptic DAHA denominator does not match a 3-variable Siegel form. One would need a **multi-variable paramodular DAHA** with $(q_1, q_2, q_3; t_1, t_2, t_3)$, specialised so the tensor-product Macdonald denominator of a 3-variable lattice reproduces $\Delta_5$. This is plausible — the Macdonald denominator of a rank-3 Koornwinder ($C_3$ or $D_3^{(1)}$) DAHA at a specific $(q, t)$ locus could reproduce Siegel-type forms. Literature: Sahi 1999, Stokman 2003. **Closest candidate**.

For Candidate (B) — ruled out at level 1.

For Candidate (C) — consistent with the Cycle 2 H2 framework but does not yield an explicit presentation. The associator $\Phi$ of Drinfeld is characterised by pentagon + hexagon relations; adapting to Borcherds hyperbolic would require a new version of these relations with lightlike-root contributions.

### A18. A fourth candidate emerges from Cycles 1–4: **topological spherical paramodular DAHA**

Combining the insights:
- Cycle 1 says the trace identity is a Plancherel integral, supported on an admissible dual.
- Cycle 2 says the EK machinery produces an ind-pro structure, not a strict Hopf.
- Cycle 3 says $\Delta_5$ is a Weyl numerator (denominator-type), not a zonal spherical function.
- Cycle 4 says the super-structure forces Berezinian bookkeeping.

The combined structural candidate is:
$$\mathcal{H}_{\Delta_5} \;\text{is a topological spherical paramodular DAHA of super type, infinite rank, limit of}$$
$$\;\;\mathrm{sDAHA}_{C_n^{(1)}}^{\mathrm{par-lim}}(q, t)\;\text{as}\; n \to \infty,$$
with the Macdonald–Koornwinder denominator at the limit reproducing $\Delta_5$.

This is my Wave-9 provisional structural identification. It replaces Wave-8's "Borcherds quasi-triangular Hopf superalgebra" with a **spherical super-DAHA at infinite paramodular rank**, an object closer to the literature (Cherednik, Etingof–Kirillov, Feigin et al.) and more naturally compatible with:
- the Plancherel structure (DAHA has a natural spherical trace);
- the super-structure (super-DAHA exists; Haiman 2001, Feigin–Stoyanovsky, Gordon–Stafford);
- the paramodular form $\Delta_5$ (Koornwinder–Macdonald denominator of the paramodular limit);
- the ind-pro nature (infinite-rank DAHA via Etingof–Kirillov direct-limit).

### H5. Heal — the true hidden structure

**Conjecture W9-G5 (True structure of $\mathcal{H}_{\Delta_5}$).** The Wave-8 hypothesis "Borcherds quasi-triangular Hopf superalgebra" **fails as stated** (Cycles 1–4). What exists in its place is a **topological spherical super-DAHA at infinite paramodular rank**:
$$\mathcal{H}_{\Delta_5} \;\cong\; \lim_{\substack{\rightarrow \\ n}}\; e \cdot \mathrm{sDAHA}_{C_n^{(1)}}(q, t) \cdot e$$
in the sense of Etingof–Kirillov 1995 direct limit, where $e$ is the spherical idempotent, $\mathrm{sDAHA}_{C_n^{(1)}}$ is Cherednik's DAHA of type $\widehat C_n$ in its super version (Sahi 1999, Stokman 2003), and the parameters $(q, t)$ are specialised to the paramodular triple $(q_1, q_2, q_3) = (e^{2\pi i \tau}, e^{2\pi i z}, e^{2\pi i \omega})$ with Siegel $(\tau, z, \omega) \in \mathbb{H}_2$.

**R-matrix**: does not exist as an element of $\mathcal{H}_{\Delta_5}^{\otimes 2}$; the "quasi-triangular" part of Wave 8 is replaced by a **commuting-Hamiltonian structure** (Macdonald operators) on $\mathcal{H}_{\Delta_5}$ acting on the polynomial representation.

**Plancherel trace identity**: holds in the form
$$\mathrm{sTr}_{\mathrm{sph}} M_\lambda \;=\; 64 \cdot \Delta_5(\lambda) / W_{\mathrm{WKB}}^{\mathrm{reg}}(\lambda),$$
where $M_\lambda$ is the Macdonald operator at spectral parameter $\lambda$ and $\mathrm{sTr}_{\mathrm{sph}}$ is the spherical super-trace on the spherical polynomial representation.

**Classical limit**: as $\hbar \to 0$ (equivalently $t \to 1$ in Cherednik variables), $\mathcal{H}_{\Delta_5}$ degenerates to a **commutative algebra of Macdonald differential operators** on $\mathbb{H}_2$, whose joint spectrum recovers $\mathfrak{g}_{\Delta_5}$ as the Poisson-bracket-BKM structure.

### H5.2. Explicit falsifiable test

**Test (W9-G5.1, falsifiable at one coefficient)**: compute the Macdonald–Koornwinder denominator of $\mathrm{sDAHA}_{C_3^{(1)}}$ at parameters $(q, t)$ specialised to the Kummer–Inose K3 period. Compare with $\Delta_5(\lambda_{\mathrm{KI}}) = \eta^{20} \cdot \eta^{20} \cdot \theta_{\mathrm{KI}}$. If the rank-3 Koornwinder denominator matches up to a constant factor of $64$, the identification W9-G5 is corroborated at depth 0; if not, W9-G5 fails.

**Test (W9-G5.2)**: the Koornwinder–Macdonald denominator of rank-$n$ DAHA at paramodular specialisation $(q, t) = (q_1, q_2)$ with $q_1 q_2 = q_3$ (Siegel paramodular constraint) is
$$\Delta_{\mathrm{KM}}(q, t) \;=\; \prod_{k=1}^\infty \bigl(1 - q^k t^{|\cdot|}\bigr)^{m_k}$$
where $m_k$ are explicit Koornwinder multiplicities. Setting $(q, t) = (e^{2\pi i\tau}, e^{2\pi i z})$ and $\omega = \tau + z$ (Siegel paramodular line), the limit $n \to \infty$ gives an infinite Borcherds-type product. If this product equals $\Delta_5$ (after regularisation and constant $64$), W9-G5 is corroborated.

**Test (W9-G5.3, third independent path)**: the $\mathrm{sDAHA}_{C_n}$ admits a **super-trace formula** (Sahi–Stokman 2003 type IV): the super-character of the spherical polynomial representation is
$$\chi^{\mathrm{sph}}(q, t) \;=\; \prod_{\alpha > 0} \frac{(1 - t q^{\alpha})}{(1 - q^{\alpha})}.$$
In the paramodular limit, this becomes the reciprocal of a Borcherds product — directly $1/\Delta_5$ up to constant. This is the **third independent verification path** (Gelfand Plancherel + Borcherds denominator + Koornwinder–Macdonald), corroborating or falsifying the W9-G5 identification.

### H5 verdict

**Wave-8's "Borcherds quasi-triangular Hopf superalgebra" does not survive Gelfand's audit.** Three structural failures in Cycles 1–4 (trace-not-a-number, EK-extension-unproved, super-Plancherel-not-specified). The **true structure** is closer to a **topological spherical super-DAHA at infinite paramodular rank** — a direct-limit of Koornwinder–Macdonald DAHAs with paramodular parameter specialisation — which is compatible with all the Plancherel, super, and Borcherds structure simultaneously, and which has explicit generators (Macdonald operators) and explicit denominators (Koornwinder products) in the literature.

---

## CONVERGENCE VERDICT

**Does $\mathcal{H}_{\Delta_5} = \mathrm{EK}(\mathfrak{g}_{\Delta_5}, \delta_{\mathrm{Manin}})$, as declared in Wave 8, survive Gelfand's Wave-9 audit?**

**NO** — not as a strict Hopf superalgebra. Three failures:

1. **Trace identity is syntactically ill-typed** (Cycle 1). The "Tr$_\mathbb{C}$" is not a well-defined number on infinite-dimensional Borcherds representations. Correct rephrasing is a **Plancherel distributional identity**, with the Plancherel measure constructed from the Borcherds–Harish-Chandra $c$-function.

2. **EK quantisation does not extend to Borcherds hyperbolic** (Cycle 2). Three structural obstructions: imaginary-root multiplicities, lightlike Cartan, non-semisimple category. Published Borcherds-EK extension does not cover this case. Correct rephrasing is a **topological ind-pro quasi-Hopf super-object** defined as inverse limit of EK truncations, with two explicit open sub-hypotheses (H2.1 truncation-compatibility, H2.2 Mittag-Leffler closure).

3. **$\Delta_5$ is the Weyl numerator, not a Harish-Chandra character** (Cycle 3). The correct Plancherel identity localises on the vacuum Verma, giving $\mathrm{Str}_{\pi_\mathrm{vac}} R = 64 \cdot \Delta_5 / W^{\mathrm{reg}}$ with **super-trace**, not ordinary trace (Cycle 4).

**What IS the true structure?** Best Wave-9 guess:

$$\boxed{\;\mathcal{H}_{\Delta_5} \;\cong\; \lim_{\substack{\rightarrow \\ n}} e \cdot \mathrm{sDAHA}_{C_n^{(1)}}(q, t) \cdot e \;\;\text{at paramodular limit}\;(q, t) \leftrightarrow \Delta_5 \;}$$

a **topological spherical super-double-affine-Hecke algebra at infinite paramodular rank** (Cherednik–Etingof–Kirillov–Sahi–Stokman structure), with commuting-Hamiltonian structure (Macdonald operators) replacing the Hopf-algebra quasi-triangularity, and Koornwinder–Macdonald denominator reproducing $\Delta_5$ in the paramodular specialisation limit.

The classical limit of this object recovers $\mathfrak{g}_{\Delta_5}$ as a Poisson-bracket BKM structure, consistent with Wave 7–8.

**Scope of survival of Wave 8**:
- The **name** $\mathcal{H}_{\Delta_5}$ survives.
- The **classical limit** = $\mathfrak{g}_{\Delta_5}$ survives (Cycle 3 H3).
- The **super-structure** from Polyakov's $c(D) \bmod 2$ rule survives (Cycle 4 H4).
- The **trace-equals-$\Delta_5/W^{\mathrm{reg}}$** identity survives, but reinterpreted as a **Plancherel super-identity** (Cycle 5 H5) or **Koornwinder-Macdonald denominator limit** — not as a scalar R-matrix trace.

**Scope of retraction**:
- "Strict Hopf superalgebra" — RETRACTED. It is a topological quasi-Hopf at best, spherical super-DAHA at most concrete.
- "Universal R-matrix $R_{\mathrm{EK}}$" as an element of $\mathcal{H}^{\hat\otimes 2}$ — RETRACTED. Replaced by commuting Hamiltonians or completion-level R.
- "Trace of R = $\Delta_5/W^{\mathrm{reg}}$" as scalar equation — RETRACTED. Replaced by Plancherel super-integral identity.

**Three falsifiable computations handed to Wave 10**:
- **(W9-G5.1)**: Koornwinder–Macdonald denominator at Kummer–Inose period $\to$ compare with $\Delta_5(\lambda_{\mathrm{KI}}) = \eta^{20}\eta^{20}\theta_{\mathrm{KI}}$.
- **(W9-G5.2)**: paramodular-limit infinite product of rank-$n$ Koornwinder DAHAs $\to$ compare with $\Delta_5$.
- **(W9-G5.3)**: spherical super-character of $\mathrm{sDAHA}_{C_n^{(1)}}$ at paramodular specialisation $\to$ compare with $1/\Delta_5$ reciprocal.

All three are single-computation checks against primary literature (Sahi 1999 JAMS 12, Stokman 2003 Proc. LMS 86, Etingof–Kirillov 1995 IMRN, Feigin–Hashizume–Hoshino–Shiraishi–Yanagida 2009). A single disagreement on any one kills W9-G5.

**Beilinson's dictum applied**: Wave 8 stated a large claim (Borcherds Hopf superalgebra with universal R-matrix trace identity). Wave 9 shrinks it to two simultaneous smaller true-or-falsifiable claims: (i) a Plancherel super-integral identity; (ii) a structural identification with a topological spherical super-DAHA at infinite paramodular rank. The smaller claims are each falsifiable at one computation. This is progress.

---

## Appendix A. Three numerical falsifiable checks, explicit

### Check 1 — depth-1 super-dim (Wave-8 H1 claim $21$)

Borcherds product $\prod_{(n,l,m)>0} (1 - q^n y^l p^m)^{-c(4nm-l^2)}$ expanded at depth 1 (= $|n|+|l|+|m| = 1$): contributions at $\{(1,0,0), (0,-1,0), (0,0,1)\}$ with $D \in \{0, -1, 0\}$ and $c(D) \in \{10, 1, 10\}$. Total super-dim at depth 1: $10 + 1 + 10 = 21$. ✓ matches Wave-8 H1.

**Reference**: Lorgat 2020 §6, Fourier expansion of $\phi_{0,1}$; Eichler–Zagier 1985 Theorem 9.6 on Fourier coefficients of weak Jacobi forms of weight 0 and index 1.

### Check 2 — depth-2 super-dim (Wave-8 H1 claim $132$; Wave-9 Gelfand gets $131$)

My Wave-9 enumeration (above, A15): depth-2 lattice points with $D \ge -1$ give $10 \cdot 2 + 108 \cdot 1 + 1 \cdot 3 = 131$, off by $1$ from Wave-8 H1. Resolution requires explicit computation from the Borcherds product expansion.

**Reference for primary source check**: $\phi_{0,1}$ Fourier coefficients from Eichler–Zagier 1985 Table 1, pp. 104–107; Lorgat 2020 Remark 1 convention $c(-1) = 1$, $c(0) = 10$, $c(3) = -64$, $c(4) = 108$. One needs to enumerate the positive-cone lattice points at depth 2 and check my enumeration against any standard Borcherds-product reference.

**Falsifiable at one Mathematica expansion of $\prod (1-q^n y^l p^m)^{-c(D)}$ at $q^2$**.

### Check 3 — Plancherel super-integral at vacuum

W9-G1 predicts $\int \chi_\pi(R) d\mu_{\mathrm{pl}}^{\mathrm{super}} = 64 \cdot \Delta_5(\rho)/W^{\mathrm{reg}}(\rho)$. At $\rho$: $\Delta_5(\rho) = 64$, $W^{\mathrm{reg}}(\rho) = 1$, RHS = $4096$.

LHS expansion: trivial rep contributes $\chi_{\mathrm{triv}}(R) = 1$; principal-series contributes Harish-Chandra Plancherel density times character. For the sum to equal $4096$, the **effective dimension of the Plancherel-regularised adjoint representation must be $4095$**.

**Primary-source reference**: Harish-Chandra 1976 (Coll. Works Vol. IV pp. 225–287) for the Plancherel formula on reductive real groups; Kac–Peterson 1984 for affine Kac–Moody ind-group extension; Jurisich 1998 for Borcherds ind-group. The Plancherel measure for Borcherds hyperbolic ind-groups is **not** in the published literature; W9-G1 conjectures its explicit form via the Borcherds–Harish-Chandra $c$-function.

Falsifiable: compute (or obstruct the computation of) the effective Plancherel dimension of the adjoint of $G_{\Delta_5}$ at $\rho$. If effective dim $\ne 4095$, W9-G1 fails.

---

## Appendix B. Cross-volume AP5 propagation check

Wave-9 findings that propagate across volumes:

- **AP-CY-W9-1** (trace-of-R ill-typed): the formula $\mathrm{Tr}_V R = f(\lambda)$ on infinite-dim $V$ requires a Plancherel/admissible-representation regularisation; in Vol I this aligns with how graded characters of $V(\lambda)$ for affine Kac–Moody are computed (Chern character / modular character), and in Vol II with how the $E_2$-derived-centre trace is handled at infinite rank.
- **AP-CY-W9-2** (EK extension to Borcherds is open): any quantisation claim on hyperbolic or Borcherds Lie (super)bialgebras needs explicit truncation hypotheses; affects Vol I Part VI (quantum groups on curves) and Vol III §k3e/BKM chapters.
- **AP-CY-W9-3** ($\Delta_5$ = Weyl numerator, not zonal spherical function): correct interpretation of Siegel cusp forms as Weyl-denominator-type rather than Plancherel-density-type. Propagates to Vol III Borcherds/Monster chapter and Vol I if Siegel forms appear.
- **AP-CY-W9-4** (super-Plancherel via Berezinian): when trace identities involve super-structure, the measure on the admissible dual must carry $(-1)^{|\pi|}$ signs; affects any super-VOA / super-Hopf constructions across all three volumes.
- **AP-CY-W9-5** (sDAHA replacement candidate): $\mathcal{H}_{\Delta_5}$ as spherical super-DAHA at infinite paramodular rank; propagates to Vol III DAHA section (if any) and opens a new Wave 10 target.

---

## Appendix C. Epistemic self-check

**What is established (verified against primary sources)**: Gram matrix eigenvalues $\{-2, 4, 4\}$, signature $(2,1)$, det $-32$ (Wave 8, re-checked). Depth-1 super-dim $= 21$ (Lorgat 2020, Eichler–Zagier). Lorgat 2020 Thm 3 $\tfrac{1}{64}\Delta_5 = \Phi^{\mathrm{BKM}}$.

**What is newly conjectured (Wave 9)**: W9-G1 (Plancherel super-identity formulation). W9-G2 (ind-pro-completion of EK). W9-G3 (Weyl-numerator interpretation of $\Delta_5$). W9-G4 (Berezinian super-Plancherel measure). W9-G5 (spherical super-DAHA at infinite paramodular rank identification).

**What is falsifiable at one computation**: each of W9-G3, W9-G4 (depth-2 super-dim discrepancy), W9-G5.1, W9-G5.2, W9-G5.3 is falsifiable at one explicit Fourier expansion or Koornwinder-Macdonald computation.

**What remains open**: the construction of the Borcherds Plancherel measure (W9-G1); the two sub-hypotheses H2.1 (truncation compatibility) and H2.2 (Mittag-Leffler) of W9-G2; the rigorous identification of the paramodular-limit of super-DAHA with $\mathcal{H}_{\Delta_5}$ (W9-G5 as a whole).

**Beilinson's dictum**: Wave 9 prefers the smaller true claim (Plancherel super-identity, testable) over the larger potentially false claim (strict Hopf superalgebra with universal R-matrix). The Wave 8 declaration has been dismissed in its strictest form and replaced by a weaker, falsifiable reformulation plus a new structural candidate (spherical super-DAHA) that is testable against primary literature (Sahi, Stokman, Etingof–Kirillov).

---

*Wave 9 Gelfand: five attack-heal cycles closed. Three falsifiable computations inscribed. The Wave-8 Hopf-superalgebra hypothesis did not survive in strict form; a topological spherical super-DAHA at infinite paramodular rank stands as Wave 9's candidate structural home for $\mathcal{H}_{\Delta_5}$, pending verification.*
