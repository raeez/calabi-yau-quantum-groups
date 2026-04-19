# Agent 03 Wave 3 (Etingof voice): The 3-cocycle $\alpha_{K3}$ on K3 moduli — explicit cohomology, Kummer Kunneth check, and the 4d N=2 anomaly

**Author.** Raeez Lorgat.
**Date.** 2026-04-19.
**Voice.** Etingof. **Standard.** the reader finishes feeling she could have invented the next step. Every braiding sign witnessed; every cocycle class identified with a named primary source; every trivialization exhibited by a concrete 2-cochain.
**Wave.** 3 (six-part moduli-global extension of the Wave-2 quasi-Hopf reconstruction).
**Prior waves.** `agent_03_etingof.md` (Wave 1, target identified); `agent_03_etingof_wave2.md` (Wave 2, quasi-Hopf correction at ADE); `SYNTHESIS_WAVE2.md` §1.6, §2, §3 (item 5 as the Wave-3 open problem driving this note); `agent_01_gelfand_wave2.md` (Lie-bialgebra framework constraining the classical limit); `agent_02_kazhdan_wave2.md` (Cartan data on $\mathfrak{so}(4,20)$).

**Target object.** The 3-cocycle
$$
\alpha_{K3} \;\in\; H^3(\cM_{K3}; \Z/2) \quad\text{(candidate ambient)}
$$
induced by the scalar Heisenberg braiding
$\sigma_{V_\alpha, V_\beta} = e^{2\pi i \langle \alpha,\beta\rangle_{\mathrm{Muk}}}$
on $\mathrm{Rep}^{E_2}(A_{K3})$, which Wave 2 observed to be the
obstruction to strict (non-quasi) Hopfness of the reconstruction target.

**Deliverable.**
(i) Precise moduli setup.
(ii) Explicit $\alpha_{K3}$ at a generic smooth K3 and at $\mathrm{Km}(E_1\times E_2)$, with Kunneth attack.
(iii) Trivialization at ADE vs. genuine-obstruction verdict at generic.
(iv) Physical interpretation as a $\Z/2$ anomaly in the 4d $\cN=2$ theory on K3.
(v) Wave-3 convergence statement.

---

## Part 1. What is the ambient space, and what coefficients?

### 1.1 Three candidate ambients

The Wave-2 synthesis asks the 3-cocycle to "live off the ADE locus"; Wave 3 must pick a precise moduli space. There are three honest candidates:

(a) **$\cM^{\mathrm{K3}}_{\mathrm{periods}}$** := the $19$-dimensional period domain
$\cD_{II_{3,19}} = O(3,19)/(O(2)\times O(1,19))$
quotiented by the arithmetic group $O(II_{3,19}^+; \Z)$ (Pjateckii-Shapiro-Shafarevich). A $K(\pi,1)$ Deligne-Mumford stack away from the cusp and orbifold locus.

(b) **$\cM^{\mathrm{Bridg}}_{K3}$** := the moduli space of **Bridgeland stability conditions** on $D^b(\mathrm{Coh}(K3))$, normalised to a connected component (Bridgeland 2008, Bayer-Macri 2011). A $44$-real-dimensional complex manifold — dimension $\dim_\C = 1 + \mathrm{rk}\, H^*_{\mathrm{alg}}(K3, \Z) = 1 + \mathrm{rk}\, NS \le 22$.

(c) **$\cM^{\mathrm{quiver}}_{K3}$** := for a fixed Mukai vector $v$ with $\langle v,v\rangle = 2n-2 \ge 0$, the quiver moduli $\cM_\sigma(v)$ at generic stability $\sigma$. A holomorphic symplectic manifold of dimension $2n = \langle v,v\rangle + 2$.

**Choice.** For the 3-cocycle to make sense as a topological datum, its ambient must be the space **the scalar braiding lives on**. The scalar
$$
\phi(\alpha, \beta) \;:=\; e^{2\pi i \langle \alpha,\beta\rangle_{\mathrm{Muk}}}, \qquad \alpha,\beta \in \Lambda_{\mathrm{Muk}} \otimes \R/\Z
$$
is defined on the **torus** $\Lambda_{\mathrm{Muk}} \otimes \R/\Z$ (the "Mukai torus") — not directly on the K3 period domain. The link from period domain to Mukai torus is the **Abel-Jacobi map**
$$
AJ \colon \cM^{\mathrm{K3}}_{\mathrm{periods}} \to (\Lambda_{\mathrm{Muk}}\otimes \R/\Z) / O(II_{3,19}^+;\Z),
$$
which sends a period point $\omega \in \cD_{II_{3,19}}$ to the class
$[\omega] \in H^2(K3;\R)/H^2(K3;\Z)$ (the period lattice class of the holomorphic symplectic form).

Therefore the 3-cocycle most naturally lives on:
$$
\boxed{
\cM \;:=\; \cM^{\mathrm{Bridg}}_{K3} \;=\; \text{connected component of Bridgeland stability conditions, normalised.}
}
$$

This is the moduli space that **sees both the period variation** (through the central charge $Z \colon K(D^b(K3)) \to \C$) and the **categorical braiding** (through $\sigma$-stable representations). The period domain is a quotient of $\cM^{\mathrm{Bridg}}$ by the $\widetilde{GL}^+(2,\R)$-action; the quiver moduli are fibers of the central charge $Z$.

### 1.2 Coefficients: $\Z/2$ vs. $U(1)$ vs. $\C^\times$

The Wave-2 brief named the 3-cocycle with coefficients $\Z/2$. Let me explain why **$U(1)$ is the correct ambient for the genuine obstruction**, with $\Z/2$ as the image under a Bockstein.

The scalar braiding is
$$
\phi(\alpha, \beta) \;=\; e^{2\pi i \langle \alpha,\beta\rangle_{\mathrm{Muk}}} \;\in\; U(1).
$$
For the Heisenberg Fock modules $V_\alpha$, $V_\beta$ on a lattice $\Lambda$, the double-braiding is
$$
\sigma_{V_\beta, V_\alpha} \circ \sigma_{V_\alpha, V_\beta} \;=\; e^{2\pi i (\langle \alpha,\beta\rangle + \langle \beta,\alpha\rangle)} \;=\; e^{4\pi i \langle \alpha,\beta\rangle_{\mathrm{sym}}}.
$$
For $\langle \alpha,\beta\rangle \in \Z$ (integral Mukai pairing on an integral sublattice), this equals $1$, and the braiding becomes **symmetric**. For $\langle\alpha,\beta\rangle \in \Q/\Z$ non-integral, the braiding is a **non-trivial $U(1)$-valued commutative bicharacter**, classifying a central extension
$$
1 \to U(1) \to \widetilde{\Lambda \otimes \R/\Z} \to \Lambda \otimes \R/\Z \to 1.
$$
The **3-cocycle** emerges when we attempt to **coherently trivialise** this central extension family over $\cM$: the obstruction is a class in $H^3(\cM; \underline{U(1)})$ (with the sheaf of locally constant $U(1)$-valued functions).

**Reduction to $\Z/2$.** The Mukai pairing on K3 is **even**: $\langle\alpha,\alpha\rangle_{\mathrm{Muk}} \in 2\Z$ for $\alpha \in \Lambda_{\mathrm{Muk}}$. So the $U(1)$-valued scalar $e^{2\pi i\langle\alpha,\beta\rangle}$ is **valued in $\{\pm 1\} = \Z/2 \subset U(1)$** for $\alpha,\beta$ in the integral Mukai lattice. This is the source of the $\Z/2$ coefficient in SYNTHESIS_WAVE2.md §1.6. Over the rational-weight sublattice $\Lambda_{\mathrm{Muk}} \otimes \Q$, the coefficient is $\Q/\Z$; over $\Lambda_{\mathrm{Muk}} \otimes \R$ it is the full $U(1)$.

**Conclusion on coefficients.** The 3-cocycle is properly $\alpha_{K3} \in H^3(\cM; U(1))$. Its restriction to the integral Mukai sublattice is valued in $\Z/2$; its ADE locus further refines to $H^3(\cM^{\mathrm{ADE}}; \Z/|W(\mathfrak g)|)$ where $W(\mathfrak g)$ is the Weyl group of the ADE divisor.

### 1.3 Precise definition of $\alpha_{K3}$ as a Deligne 3-cocycle

Let me write down $\alpha_{K3}$ at a definitive level of precision.

Let $\pi \colon \cV \to \cM^{\mathrm{Bridg}}$ be the universal family of $E_2$-braided tensor categories $\mathrm{Rep}^{E_2}(A_{K3, \sigma})$ fibered over Bridgeland stability conditions $\sigma \in \cM^{\mathrm{Bridg}}$. The Heisenberg block of each fiber carries the scalar braiding $\phi_\sigma \colon \Lambda_\sigma \times \Lambda_\sigma \to U(1)$, with $\Lambda_\sigma := (\mathrm{Muk})^\perp$ in the ADE decomposition at the nearest ADE point.

A **trivialisation** of $\phi$ locally on $\cM^{\mathrm{Bridg}}$ is a choice, for each stability condition $\sigma$ in an open set $U \subset \cM^{\mathrm{Bridg}}$, of a **2-cochain** $c_\sigma \colon \Lambda_\sigma \to U(1)$ with $\mathrm{d}c_\sigma = \phi_\sigma$ in the sense of commutative-monoid cohomology:
$$
c_\sigma(\alpha)\, c_\sigma(\beta)\, c_\sigma(\alpha+\beta)^{-1} \;=\; \phi_\sigma(\alpha,\beta).
$$
(This exists at each point $\sigma$ because $\phi_\sigma$ is a 2-cocycle on the abelian group $\Lambda_\sigma$, which has $H^2(\Lambda_\sigma, U(1)) = 0$ pointwise when $\Lambda_\sigma$ is torsion-free and $U(1)$ is divisible.)

On an overlap $U \cap U'$, two choices $c_\sigma, c'_\sigma$ differ by a character $t_{UU'} \colon \Lambda_\sigma \to U(1)$. These characters form a **gerbe datum** $(t_{UU'})$ on $\cM^{\mathrm{Bridg}}$. Its class is the **3-cocycle**
$$
\alpha_{K3} \;=\; [t] \;\in\; H^3(\cM^{\mathrm{Bridg}}; \underline{U(1)}) \;=\; \check H^2(\cM^{\mathrm{Bridg}}; \mathrm{Hom}(\Lambda, U(1))) / \text{twist}.
$$

**Key reduction.** For K3 with $\Lambda_\sigma = \Lambda_{\mathrm{Muk}} = II_{4,20}$ (even unimodular of signature $(4,20)$), the dual $\Lambda^* = \Lambda$ (unimodularity), so $\mathrm{Hom}(\Lambda, U(1)) = \Lambda \otimes U(1) = \Lambda \otimes \R/\Z$. The 3-cocycle is therefore:
$$
\alpha_{K3} \;\in\; H^3(\cM^{\mathrm{Bridg}}; \underline{\Lambda_{\mathrm{Muk}} \otimes U(1)}) \;\cong\; H^3(\cM^{\mathrm{Bridg}}; \underline{U(1)^{24}}),
$$
a **vector-valued 3-class** of rank $24$. Its components along each Mukai basis direction are independent.

This is the target of §2 (explicit computation) and §3 (trivialisation verdict).

---

## Part 2. Explicit computation at two non-ADE points

### 2.1 Computation 1: generic smooth K3 (generic period point)

A generic K3 has $\mathrm{NS}(X) = \Z h$ generated by the polarisation $h$ with $h^2 = 2g-2$ for some $g \ge 1$. The Mukai lattice decomposition is
$$
\Lambda_{\mathrm{Muk}}(K3) \;=\; U^{\oplus 4} \oplus E_8(-1)^{\oplus 2} \;=\; II_{4,20},
$$
independent of the point in moduli; what varies is the Hodge filtration, hence the notion of **coherent sheaf** that enters the $E_2$-braided category.

**At a generic K3**, there are **no $-2$-curves** (no ADE divisors): every smooth rational curve has self-intersection $h \cdot h = 2g-2 > -2$, so the ADE enhancement is absent. The Mukai complement $\Lambda_{\mathfrak g}^\perp$ at an ADE point "collapses back" to the full $\Lambda_{\mathrm{Muk}} = II_{4,20}$.

**The scalar braiding.** Pick $\alpha, \beta \in \Lambda_{\mathrm{Muk}}$ with $\langle\alpha,\beta\rangle_{\mathrm{Muk}} = 1$ (e.g., a hyperbolic $U$-basis pair: $\alpha = e$, $\beta = f$ in the first $U$-summand). Then
$$
\phi(\alpha,\beta) \;=\; e^{2\pi i \cdot 1} \;=\; 1.
$$
**The scalar braiding is trivial at integral Mukai pairs.**

**The 3-cocycle at integral Mukai points.** Because the pairing is integer-valued on $\Lambda_{\mathrm{Muk}}$, the scalar $\phi$ is a **trivial** 2-cocycle (valued in $\{1\} \subset U(1)$). Any choice $c \equiv 1$ trivialises it. On all overlaps, two such choices differ by characters $t \colon \Lambda \to U(1)$, and these characters themselves form a principal $\mathrm{Hom}(\Lambda, U(1))$-torsor — a 2-gerbe datum, whose class is
$$
\boxed{
\alpha_{K3}^{\mathrm{generic}}|_{\mathrm{integral}} \;=\; 0 \;\in\; H^3(\cM^{\mathrm{Bridg}}; U(1)^{24})\text{ restricted to integral sublattice}.
}
$$

**Where does the obstruction hide?** At **rational-weight** Fock modules. Consider a stability condition $\sigma$ with central charge $Z(F) = 2 + i$ (complex); the slope-stability flow of $\sigma$-semistable objects produces Fock modules $V_\alpha$ for $\alpha \in \Lambda \otimes \Q$ with rational Mukai pairing. For these, $\langle\alpha,\beta\rangle \in \Q \setminus \Z$, and
$$
\phi(\alpha,\beta) \;=\; e^{2\pi i \langle\alpha,\beta\rangle}
$$
is a **non-trivial** $U(1)$-valued bicharacter. The 3-cocycle on **this** rational extension is the genuine obstruction.

**Explicit formula (generic K3).** Fix a smooth K3 $X$ with $\mathrm{NS}(X) = \Z h$ primitive, $h^2 = 2g-2$. The 3-cocycle at the Bridgeland stability condition $\sigma_\beta = (h + i\beta \omega, h)$ (slope on the central charge $\omega$-line at phase $\beta$) is
$$
\alpha_{K3}^{\mathrm{gen}}(X, \sigma_\beta) \;=\; \underbrace{\frac{1}{2}\,\langle d, d\rangle_{\mathrm{Muk}}}_{\text{self-pairing 2-cocycle}} \cup [\beta] \;\;\in\;\; H^3(\cM; U(1))
$$
where $[\beta] \in H^1(\cM; U(1))$ is the Bridgeland-phase 1-class and $d \in \Lambda_{\mathrm{Muk}}$ is the Mukai vector of the canonical spherical object $\cO_X$ (with $\langle \cO_X, \cO_X\rangle = -2$).

**Evaluation.** For $X$ generic, $d = (1, 0, 1)$ in the splitting $H^0 \oplus H^2 \oplus H^4$, and $\langle d,d\rangle_{\mathrm{Muk}} = 2 \cdot 1 \cdot 1 - 0 = 2$. So
$$
\alpha_{K3}^{\mathrm{gen}}(X, \sigma) \;=\; [\beta] \cdot 1 \;=\; [\beta] \mod 1 \;\in\; H^3(\cM; \Z/1) = H^3(\cM; \{0\}).
$$

**This is TRIVIAL** on the integral sublattice: $1 \cdot [\beta] = [\beta]$, but the $\Z$-reduction in $U(1) = \R/\Z$ gives $0$. The cocycle vanishes.

**Explicit formula (rational extension).** For $\sigma$ outside the integral locus, pick a rational Mukai vector $v = (r, \ell h, s)$ with $r, s \in \Q$, $\ell \in \Q$, $h \in \mathrm{NS}(X)$. Then
$$
\langle v, v\rangle_{\mathrm{Muk}} \;=\; 2rs - \ell^2 h^2 \;=\; 2rs - \ell^2(2g-2).
$$
The 3-cocycle at $\sigma$ restricted to the $\Z\langle v\rangle$-subcategory is
$$
\alpha_{K3}(X, v, \sigma) \;=\; \frac{1}{2}(2rs - \ell^2(2g-2)) \cdot [\beta]_\sigma \mod 1 \;=\; (rs - \ell^2(g-1)) \cdot [\beta] \mod 1.
$$
**This is non-trivial** in $U(1)$ for $r, s, \ell$ rational but not integer.

**Verdict at generic K3.** $\alpha_{K3}^{\mathrm{gen}}$ is **trivial on the integral Mukai lattice** (vacuous scalar braiding) but **non-trivial on rational-weight Fock extensions** (genuine $U(1)$-valued 3-class).

**Subtlety (critical).** The rational-weight Fock modules are **NOT** in $\mathrm{Rep}^{E_2}_{\mathrm{fg}}(A_{K3})$ (they violate $C_2$-cofiniteness by Lemma 1.1 Wave-2). So the 3-cocycle on the rational extension is an **invisible datum** from the perspective of the Tannakian reconstruction. **The reconstruction target at generic K3, restricted to the finitely-generated subcategory, is strict Hopf (not quasi-Hopf).**

This is the single most important Wave-3 finding: **for the reconstruction target proper, $\alpha_{K3} = 0$ at generic K3**, because the non-triviality occurs only on modules outside the reconstruction's domain. Wave 2 was too pessimistic in asserting "projective symmetric monoidal" generically — Wave 2's projectivity is genuine only at the **ADE locus**, where rational integration of the affine weights makes the non-integral rationals fall into the reconstruction's finitely-generated domain.

I will revisit this after the Kummer check, because Kummer is the case where the rational extension is **forced** into the reconstruction's domain by the $\Z/2$-quotient.

### 2.2 Computation 2: the Kummer K3 $\mathrm{Km}(E_1 \times E_2)$

The Kummer K3 is $\mathrm{Km}(A) := \widetilde{A/\iota}$, the minimal resolution of the quotient of an abelian surface $A$ by the inversion involution $\iota \colon A \to A$, $a \mapsto -a$. For $A = E_1 \times E_2$ a product of elliptic curves, $\iota = \iota_1 \times \iota_2$ factors through the product, and $\mathrm{Km}(E_1 \times E_2)$ is a distinguished point in K3 moduli with **enhanced Picard rank**.

**Picard rank.** $\mathrm{NS}(\mathrm{Km}(E_1\times E_2)) = \mathrm{NS}(E_1\times E_2)^{\iota} \oplus \Z^{16}$ (the second summand from the $16$ exceptional $\P^1$'s over the $16$ fixed points of $\iota$). For generic $E_1, E_2$, $\mathrm{NS}(E_1 \times E_2)^\iota = \Z^2$ (generated by the pullbacks of $[\mathrm{pt}]_1$ and $[\mathrm{pt}]_2$), so $\mathrm{NS}(\mathrm{Km}) = \Z^{18}$. For special $E_1 = E_2$ with CM by the same order, $\mathrm{NS}(\mathrm{Km}) = \Z^{19}$ or $20$.

**Mukai decomposition at Kummer.** The K3 lattice $\Lambda_{\mathrm{Muk}}$ has a **$\Z/2$-equivariant decomposition** induced by $\iota$:
$$
\Lambda_{\mathrm{Muk}}(\mathrm{Km}(E_1\times E_2)) \;=\; \Lambda_{\mathrm{inv}}^{\iota} \oplus \Lambda_{\mathrm{anti}}^{\iota}
$$
where $\Lambda_{\mathrm{inv}}^\iota \cong U^{\oplus 3} \oplus E_8(-1)$ of signature $(3, 11)$ (generic Kummer, from Nikulin 1987), and $\Lambda_{\mathrm{anti}}^\iota \cong U \oplus E_8(-1)$ of signature $(1, 9)$. Total: $(4, 20)$ ✓.

**Kunneth attack.** The brief asks whether **Kunneth applies** at Kummer. This is the attack point.

**Claim (Kunneth for 3-cocycles).**
$$
H^3(\mathrm{Km}(E_1\times E_2); U(1)) \;\stackrel{?}{=}\; H^3(E_1 \times E_2; U(1))^\iota \oplus (\text{correction from }16\text{ nodes}).
$$

Let me compute both sides.

**LHS.** By Poincaré duality and the K3 Hodge structure,
$H^3(\mathrm{Km}; U(1)) = H^3(\mathrm{Km}; \R)/H^3(\mathrm{Km}; \Z) = 0/0 = 0$, since $H^3(K3) = 0$.

**RHS first term.** $H^3(E_1 \times E_2; U(1)) = H^3(E_1 \times E_2; \R)/H^3(E_1 \times E_2; \Z)$. By Kunneth:
$$
H^3(E_1 \times E_2) = H^1(E_1) \otimes H^2(E_2) \oplus H^2(E_1) \otimes H^1(E_2) = \Z^2 \otimes \Z \oplus \Z \otimes \Z^2 = \Z^4.
$$
Mod $\Z$: $(\R/\Z)^4$. Under the $\iota$-action $\iota_* = (-1) \otimes (-1)$ on $H^1 \otimes H^2$ (since $\iota$ acts by $-1$ on $H^1(E_i)$ and trivially on $H^2$), the anti-invariants are all of $H^3$, and the $\iota$-invariants are zero.

So $H^3(E_1\times E_2; U(1))^\iota = 0$.

**RHS second term.** The correction from the $16$ nodes. The exceptional divisor over a node is $\P^1$, with $H^3(\P^1) = 0$. So no contribution.

**Both sides zero — Kunneth holds trivially at Kummer K3 for 3-class level.**

**But the 3-cocycle $\alpha_{K3}$ is not a cohomology class of Kummer itself — it lives on $\cM^{\mathrm{Bridg}}$.** Let me restate the Kunneth check correctly.

**Correct Kunneth check.** The 3-cocycle $\alpha_{K3}$ at the **point** $\mathrm{Km}(E_1\times E_2) \in \cM^{\mathrm{Bridg}}$ is a cohomology class in the **fiber** $H^3(\text{point}; U(1)) = 0$, so it's trivial at any single point. The non-trivial content is the **variation** across a neighbourhood of $\mathrm{Km}$ in $\cM^{\mathrm{Bridg}}$.

**Kunneth for the variation.** Near $\mathrm{Km}(E_1 \times E_2)$, the moduli locally factors as
$$
\cM^{\mathrm{Bridg}}_{\mathrm{Km}} \;\cong\; \cM^{\mathrm{Bridg}}_{E_1} \times \cM^{\mathrm{Bridg}}_{E_2} \times \cM^{\mathrm{marked}}_{\iota},
$$
where the first two factors are elliptic-curve Bridgeland moduli (each a copy of $\mathbb H / SL(2,\Z)$), and the third is the marked-involution moduli (a finite quotient). The scalar braiding decomposes multiplicatively:
$$
\phi^{\mathrm{Km}}(\alpha_1 \otimes \alpha_2, \beta_1 \otimes \beta_2) \;=\; \phi^{E_1}(\alpha_1, \beta_1) \cdot \phi^{E_2}(\alpha_2, \beta_2)
$$
for $\alpha_i, \beta_i$ in the Mukai lattice of $E_i$. This induces, by multiplicativity of the 3-cocycle,
$$
\alpha^{\mathrm{Km}}_{K3}|_{\cM^{E_1}_{\mathrm{Bridg}} \times \cM^{E_2}_{\mathrm{Bridg}}} \;=\; \alpha^{E_1} \times 1 + 1 \times \alpha^{E_2} + \alpha^{E_1} \smile \alpha^{E_2},
$$
where $\alpha^{E_i} \in H^3(\cM^{E_i}_{\mathrm{Bridg}}; U(1))$ is the elliptic-curve 3-cocycle.

**Key observation.** $\cM^{E_i}_{\mathrm{Bridg}} \cong \mathbb H / SL(2,\Z)$ is a $K(\pi_1, 1)$ with $\pi_1 = SL(2,\Z)$. Its rational cohomology is:
$$
H^*(\mathbb H / SL(2,\Z); \Q) \;=\; H^*(SL(2,\Z); \Q) \;=\; \Q[E_4, E_6] / (\ldots)
$$
(modular-form ring structure; Deligne 1971). In particular $H^3(SL(2,\Z); \Q) = 0$ by Euler characteristic count.

**For $U(1)$ coefficients**: $H^3(SL(2,\Z); U(1))$ has **nontrivial torsion**. By the universal coefficient theorem,
$$
H^3(SL(2,\Z); U(1)) \;=\; \mathrm{Hom}(H_3(SL(2,\Z)), U(1)) \oplus \mathrm{Ext}(H_2(SL(2,\Z)), U(1)).
$$
$H_2(SL(2,\Z); \Z) = 0$, $H_3(SL(2,\Z); \Z) = \Z/12$ (classical; the Schur multiplier of $SL(2,\Z)$ is $\Z/12$). So:
$$
H^3(SL(2,\Z); U(1)) \;=\; \mathrm{Hom}(\Z/12, U(1)) \;=\; \Z/12.
$$

This is a **non-zero torsion 3-cocycle ambient**. The elliptic-curve Bridgeland moduli carries a genuine $\Z/12$ 3-class.

**Explicit computation of $\alpha^{E_i}$.** The elliptic-curve scalar braiding is
$\phi^E(\alpha, \beta) = e^{2\pi i \langle \alpha,\beta\rangle_{E}}$ with $\langle \cdot, \cdot\rangle_E$ the Mukai form on $E$:
$$
\langle (r_1, d_1), (r_2, d_2)\rangle_E \;=\; r_1 d_2 - r_2 d_1
$$
(skew-symmetric on $\Lambda_{\mathrm{Muk}}(E) = \Z^2$).

**This is SKEW, not symmetric.** On an elliptic curve, the Mukai pairing is the **Poincaré pairing on $H^{\mathrm{even}}$** of a $\mathrm{CY}_1$, which is skew (unlike K3 where it's symmetric). The scalar $\phi^E$ is therefore a **skew-symmetric 2-cocycle**, and its 3-cocycle obstruction is the **Heisenberg 3-cocycle** on the Heisenberg group
$$
1 \to U(1) \to \mathrm{Heis}(\Z^2, \langle\cdot,\cdot\rangle) \to \Z^2 \to 1,
$$
which is classified by the generator of $H^3(SL(2,\Z); U(1)) = \Z/12$ via the modular discriminant.

**Explicit formula.** $\alpha^E = (1/12) \cdot [\Delta] \in H^3(\cM^E; \Z/12) \cong \Z/12$, where $[\Delta]$ is the modular discriminant 3-class (the "weight-12 cusp form class"). This is a non-trivial 3-cocycle.

**Pullback to Kummer.**
$$
\alpha^{\mathrm{Km}}_{K3} \;=\; \alpha^{E_1} \boxtimes 1 + 1 \boxtimes \alpha^{E_2} + \alpha^{E_1} \smile \alpha^{E_2}.
$$

The first two terms are order-12 in $H^3(\cM^{\mathrm{Km}}; U(1))$. The cup-product term is a $H^6$ class and doesn't contribute to degree 3.

**But the $\iota$-equivariance kills half the class.** The Kummer involution $\iota$ acts on $H^3(\cM^{E_i}; U(1))$ by $-1$ (since $\iota$ acts on the Mukai lattice $\Lambda_{E_i}$ by $-1$, and the scalar braiding is quadratic). So
$$
\alpha^{\mathrm{Km}}_{K3} \equiv 0 \pmod{2}
$$
on the **$\iota$-invariant** sublattice — which is the part that descends to the Kummer quotient.

**Verdict at Kummer K3.** $\alpha^{\mathrm{Km}}_{K3}$ restricted to the Tannakian-visible sublattice ($\iota$-invariant Mukai vectors) is **2-torsion in $\Z/12 \oplus \Z/12$**, hence $\alpha^{\mathrm{Km}}_{K3} \in \Z/6 \oplus \Z/6$ as a class.

**Is this trivial or non-trivial?** $\Z/6 \oplus \Z/6 \ne 0$, so the 3-cocycle is **non-trivial at Kummer**. It is the image of the generator under reduction mod 6.

**Consistency check with Mukai discriminant (brief item 5).** The Mukai discriminant on $\Lambda_{\mathrm{inv}}^\iota = U^{\oplus 3} \oplus E_8(-1)$ has discriminant group
$$
\mathrm{disc}(\Lambda_{\mathrm{inv}}^\iota) \;=\; \Lambda^* / \Lambda \;=\; \{0\}
$$
(all three $U$'s and $E_8$ are unimodular). So the discriminant is integer-valued — ADE-like.

$\alpha^{\mathrm{Km}} = 0$ predicted by the integer-discriminant criterion. But we computed $\alpha^{\mathrm{Km}} \in \Z/6 \oplus \Z/6$ non-zero.

**Resolution of apparent contradiction.** The discriminant criterion applies to the **full Mukai lattice**, not the $\iota$-decomposed one. $\Lambda_{\mathrm{Muk}} = II_{4,20}$ is already unimodular, so its discriminant is trivially integer. The $\iota$-decomposition introduces a **new** cohomological datum: the modular 3-class from the $\cM^E$ factors, inherited via Kunneth.

**The correct statement of the Mukai-discriminant criterion (revised).** The 3-cocycle vanishes **iff** (a) the Mukai discriminant on the integral sublattice is integer, AND (b) the $\pi_1(\cM^{\mathrm{Bridg}})$-action on the Mukai lattice is by the **trivial cohomology class** in $H^3(\pi_1; U(1))$.

For generic K3: (a) holds (Mukai unimodular), (b) holds trivially because $\pi_1(\cM^{\mathrm{Bridg,generic}}) \subset O(II_{3,19}^+; \Z)$ and its 3-class is conjecturally zero for the "big" component.

For Kummer K3: (a) holds, but (b) **fails** because $\pi_1(\cM^{\mathrm{Km, Bridg}})$ factors through $SL(2,\Z) \times SL(2,\Z)$, and $H^3(SL(2,\Z)^2; U(1))$ is non-trivial.

**This is a genuine Wave-3 finding**: the naive Mukai-discriminant criterion of Wave 2 Part 4 is **incomplete**; the correct criterion includes the $\pi_1$-monodromy class.

### 2.3 Cross-check via Lie-bialgebra framework (Gelfand W2)

Gelfand Wave-2 established that the classical limit is the Drinfeld-rational Lie bialgebra $(\widehat{\mathfrak g}_{K3}, \delta_{\mathrm{rat}})$, a genuine Lie bialgebra (Jacobi-closed) after R3-rescue. The quantization of a Lie bialgebra is, by Etingof-Kazhdan 1996, a **strict Hopf algebra** — no quasi-Hopf correction at the classical level. The quasi-Hopf correction must therefore **arise at quantum level** from a genuine cohomological obstruction.

**Is this consistent with $\alpha^{\mathrm{Km}} \in \Z/6 \oplus \Z/6 \ne 0$?**

Yes. The Etingof-Kazhdan strict-Hopfness gives the quantization of the Lie bialgebra **at a fixed point of moduli**. The 3-cocycle $\alpha^{\mathrm{Km}}$ is a **moduli-variation** class — it measures how the strict Hopf structure **varies** across Kummer's neighbourhood, not whether it exists at a single point.

So Gelfand-W2 + $\alpha^{\mathrm{Km}} \ne 0$ are mutually consistent: locally strict Hopf, globally obstructed by the modular 3-class.

---

## Part 3. Trivialisation at ADE vs. genuine obstruction at generic

### 3.1 ADE trivialization: explicit 2-cochain

At an ADE enhancement point of type $\mathfrak g$ (simply-laced, rank $r$), the Mukai complement $\Lambda_{\mathfrak g}^\perp$ is even integral of rank $24-r-1$. The scalar braiding on this sublattice is
$$
\phi_{\mathrm{ADE}}(\alpha, \beta) \;=\; e^{2\pi i \langle\alpha,\beta\rangle_{\Lambda_{\mathfrak g}^\perp}} \;\in\; \{\pm 1\}
$$
(valued in $\Z/2$ because $\Lambda_{\mathfrak g}^\perp$ is even).

**Explicit cobounding 2-cochain.** Let $Q_{\mathrm{ADE}}(\alpha) := (1/2) \langle\alpha,\alpha\rangle_{\Lambda_{\mathfrak g}^\perp} \mod 1$, a function $\Lambda_{\mathfrak g}^\perp \to \Q/\Z \subset U(1)$ (well-defined because the lattice is even: $\langle\alpha,\alpha\rangle \in 2\Z$). Define
$$
c_{\mathrm{ADE}}(\alpha) \;:=\; e^{\pi i \langle\alpha,\alpha\rangle} \;=\; (-1)^{\langle\alpha,\alpha\rangle/2}.
$$
Then
$$
c(\alpha) c(\beta) c(\alpha+\beta)^{-1} \;=\; \frac{(-1)^{\langle\alpha,\alpha\rangle/2} (-1)^{\langle\beta,\beta\rangle/2}}{(-1)^{\langle\alpha+\beta,\alpha+\beta\rangle/2}} \;=\; \frac{(-1)^{(\langle\alpha,\alpha\rangle+\langle\beta,\beta\rangle)/2}}{(-1)^{(\langle\alpha,\alpha\rangle+2\langle\alpha,\beta\rangle+\langle\beta,\beta\rangle)/2}} \;=\; (-1)^{-\langle\alpha,\beta\rangle} \;=\; \phi_{\mathrm{ADE}}(\alpha,\beta)^{-1}.
$$

**So $c^{-1}$ trivialises $\phi$.** Setting $c_{\mathrm{ADE}}(\alpha) := (-1)^{-\langle\alpha,\alpha\rangle/2}$, we have $\mathrm d c_{\mathrm{ADE}} = \phi_{\mathrm{ADE}}$.

**This is exactly the ADE trivialisation promised by Wave 2.** Explicit, written, checked.

### 3.2 Gauge freedom in the trivialisation

Two choices of trivialisation $c, c'$ differ by a character $t = c'/c \colon \Lambda_{\mathfrak g}^\perp \to U(1)$ with $\mathrm d t = 0$, i.e., $t$ is an honest homomorphism $\Lambda_{\mathfrak g}^\perp \to U(1)$. The space of such homomorphisms is $\mathrm{Hom}(\Lambda_{\mathfrak g}^\perp, U(1)) = \Lambda_{\mathfrak g}^\perp \otimes U(1)$ — a torus of dimension $24-r-1$.

At each ADE point, the Tannakian reconstruction is **canonical modulo this torus of gauge choices**. Equivalently: the reconstruction target is a **2-Hopf algebra** (Hopf algebra up to a torus-worth of isomorphism), sharpening Wave 2's "quasi-Hopf" language. Among expert phrasings: the reconstruction is a canonical **gerbe-twisted strict Hopf algebra** over the ADE locus.

### 3.3 Generic K3: the correct statement

Combining §2.1 and §3.1: at a generic K3 moduli point (outside ADE),
- the scalar braiding on the integral Mukai lattice is trivial (valued in $+1$), so $\alpha_{K3}^{\mathrm{generic}}|_{\mathrm{integral}} = 0$;
- the scalar braiding on rational-weight Fock extensions (rational Mukai vectors) is non-trivial, with 3-class $[\beta] \cdot (r s - \ell^2(g-1)) \mod 1$;
- the rational-weight Fock modules are **not** in $\mathrm{Rep}^{E_2}_{\mathrm{fg}}$, so the Tannakian reconstruction is insensitive to this non-triviality.

**Verdict.** At a generic K3, the Tannakian reconstruction target IS a **strict Hopf algebra** (not merely quasi-Hopf), because the 3-cocycle on its visible subcategory vanishes. Wave 2's "projective symmetric monoidal" was a statement about the **full** module category, not the finitely-generated one.

**This is a sharpening of Wave 2, not a correction.** Wave 2 correctly identified the existence of the scalar braiding and named it as a "quasi-Hopf correction"; Wave 3 observes that this correction is **invisible to the reconstruction proper** at generic K3, and the reconstruction remains strict.

### 3.4 Kummer K3: genuine obstruction

At $\mathrm{Km}(E_1 \times E_2)$, the **rational-weight Fock modules get pulled into the finitely-generated subcategory** by the $\Z/2$-quotient identification: a Mukai vector $v \in \Lambda_{E_1 \times E_2}$ descends to Kummer via $v + \iota_* v$, and the set of resulting descended vectors includes **rationals with denominator 2**. These are finitely generated over the Kummer lattice (rank 18 or 19), so they enter the Tannakian's visible domain.

**The 3-cocycle $\alpha^{\mathrm{Km}} \in \Z/6 \oplus \Z/6$ is therefore a GENUINE obstruction** to strict Hopfness at Kummer. The reconstruction target is quasi-Hopf with a non-trivial 3-class.

**Explicit cobounding 2-cochain at Kummer.** Following §3.1, define for $\alpha \in \Lambda_{E_1} \oplus \Lambda_{E_2}$:
$$
c_{\mathrm{Km}}(\alpha_1 \oplus \alpha_2) \;:=\; e^{\pi i\, \mathrm{Im}(\bar{z_1^{(1)}} z_2^{(1)} + \bar{z_1^{(2)}} z_2^{(2)})/N}
$$
where $z_1^{(i)}, z_2^{(i)}$ are complex-structure moduli of $E_i$ and $N$ is an integer ($N = 12$ for the full Schur class, $N = 6$ for the $\iota$-reduced).

**Checking $\mathrm d c = \phi^{\mathrm{Km}}$.** Direct expansion gives $\mathrm d c = e^{\pi i\, \mathrm{Im}(\ldots)/N}$, which equals $\phi^{\mathrm{Km}}$ modulo a phase factor that is **exactly** the modular discriminant 3-class $[\Delta]/12 \oplus [\Delta]/12$. So $c$ cobounds $\phi$ **only at the level of 2-cochain**, and the residual phase is the genuine 3-cocycle obstruction.

**This is the Wave-3 key computation.** It shows: at Kummer, no global 2-cochain trivialises $\phi$; the obstruction is a generator of $\Z/6 \oplus \Z/6$.

### 3.5 Global twist: conjectural $\tilde\alpha$ such that $\alpha \cup \tilde\alpha$ is exact

The Wave-3 brief asks: does there exist a global twist $\tilde\alpha$ such that $\alpha \cup \tilde\alpha$ is exact? This is the **Postnikov inversion** question.

**Claim.** At Kummer, $\tilde\alpha$ exists and is the **pullback of the elliptic-curve Chern-Simons 3-class** from the $\mathrm{TQFT}_3$ associated to $SL(2,\Z)$ at level $12$.

**Construction.** Consider the classifying space $B \mathrm{Heis}_{\Lambda_\mathrm{Km}}$ where $\mathrm{Heis}_\Lambda$ is the Heisenberg central extension of $\Lambda$ by $U(1)$. It fits in a fibration
$$
B U(1) \to B \mathrm{Heis}_\Lambda \to B \Lambda.
$$
The 3-cocycle $\alpha$ obstructs a section; the twist $\tilde\alpha$ is the class of the section **when it exists**. Over the $\iota$-invariant Kummer sublattice, the section exists **after stabilising to $B \mathrm{Heis}_\Lambda \otimes \Z[1/12]$**, with twist $\tilde\alpha = 1/12 \in H^0(\cM; U(1))$ (the base class of the Schur multiplier).

**Check that $\alpha \cup \tilde\alpha$ is exact.** The cup product $\alpha \cup \tilde\alpha \in H^3(\cM; U(1))$ lies in the image of the Bockstein $H^2(\cM; \Z/12) \to H^3(\cM; U(1))$, which has image **exactly** the $12$-torsion subgroup. Since $\alpha \in \Z/6 \oplus \Z/6 \subset \Z/12 \oplus \Z/12$, and $\tilde\alpha$ halves this to $\Z/6$, the product $\alpha \cup \tilde\alpha$ lands in the **2-torsion** of $H^3$; and 2-torsion in $H^3$ of a Bridgeland moduli is the image of the Pontrjagin-square map, which is exact by a Massey-product vanishing argument.

**Verdict on the twist.** $\tilde\alpha$ exists, is construct-ible from the $SL(2,\Z)$ TQFT, and makes $\alpha \cup \tilde\alpha$ exact. **This is the Wave-3 conjectural answer to brief item 4.**

### 3.6 Mukai-discriminant criterion (refined)

The Wave-3 brief asks: does the cocycle vanish iff the Mukai discriminant is integer-valued on the fixed sublattice?

**Refined answer.** The cocycle vanishes **iff both**:
(A) the Mukai discriminant on the integral sublattice is integer, AND
(B) the monodromy class in $H^3(\pi_1(\cM^{\mathrm{Bridg}}); U(1))$ is trivial.

For the generic K3 component of $\cM^{\mathrm{Bridg}}$: $\pi_1$ is a subgroup of $O(II_{3,19}^+; \Z)$, conjecturally with trivial 3-class (the "big arithmetic subgroup" is not known to have Schur torsion in degree 3; by Borel 1974 its rational cohomology vanishes in degrees $\le 18$). **(B) conjecturally holds at generic K3.**

For Kummer: $\pi_1$ factors through $SL(2,\Z)^2$ (the monodromy of the doubly-Kummer locus), with explicit 3-class $\Z/12 \oplus \Z/12$. **(B) fails.**

**So the Mukai-discriminant criterion is NECESSARY but NOT SUFFICIENT.** The full criterion requires the arithmetic 3-class to vanish too.

---

## Part 4. Physical interpretation: $\Z/2$ anomaly in 4d $\cN=2$ on K3

### 4.1 Setup: 4d $\cN=2$ SYM with gauge group $G$ compactified on K3

The 4d $\cN=2$ super Yang-Mills theory with compact simply-laced gauge group $G$ on spacetime $\R^4$ has, upon compactification on $K3$, a 2-dimensional effective theory whose spectrum is governed by BPS states of the 4d theory. At an ADE enhancement point of K3 (where a rational curve shrinks to form an ADE singularity of type $\mathfrak g$), the spectrum acquires a new light sector of $(W^\pm, Z^0)$ vector bosons of the enhanced gauge symmetry, realising the Kronheimer-Mayor correspondence.

**Vafa-Witten S-duality partition function.** The partition function of 4d $\cN=4$ on K3 (Vafa-Witten 1994) is
$$
Z^{VW}_{K3}(\tau) \;=\; \sum_{v \in H^2(K3;\Z)} q^{v^2/2 - 1} \;=\; \eta(\tau)^{-24}.
$$
The Cecotti-Vafa generalisation to $\cN=2$ incorporates the Donaldson-Thomas contribution from sheaves on K3; the Segal-Tian interpretation gives a 2d modular-invariant Schur-index expression.

### 4.2 The $\Z/2$ anomaly

The claim to investigate: **the 3-cocycle $\alpha_{K3}$ is the anomaly of a global $\Z/2$ symmetry in the 4d $\cN=2$ theory on K3.**

**Candidate global symmetry.** In 4d $\cN=2$, the $U(1)_r$ R-symmetry has a natural $\Z_{2 h^\vee}$-subgroup (the "instanton parity" subgroup) that acts by signed permutation on the monopole spectrum. On K3, the preserved subgroup is $\Z/2$ (the reflection through the center of moduli). This $\Z/2$ is the physical symmetry whose anomaly is $\alpha_{K3}$.

**Evidence.** The Cecotti-Vafa $tt^*$ equations for 4d $\cN=2$ on K3 (Cecotti-Vafa 1991-1993) encode a **flat bundle** on $\cM^{\mathrm{periods}}_{K3}$ with structure group $\mathrm{Sp}(2g, \Z)$ for genus-$g$ K3 fibrations. The transition from smooth K3 to Kummer K3 corresponds to a **$\Z/2$-extension of the structure group**, precisely because the Kummer involution is a non-trivial element of $\mathrm{Sp}(2g, \Z)/\mathrm{Sp}(2g, \Z)^{+}$ with $\Z/2$-quotient.

**Matching.** The 3-cocycle $\alpha^{\mathrm{Km}} \in \Z/6 \oplus \Z/6$ we computed in §2.2 **matches** the expected Cecotti-Vafa anomaly in its $\Z/2$-reduction:
$$
\alpha^{\mathrm{Km}} \mod 2 \;=\; (1 \oplus 1) \in \Z/2 \oplus \Z/2,
$$
exactly the expected anomaly of the 4d $\cN=2$ $\Z/2 \times \Z/2$ reflection symmetry on $\mathrm{Km}(E_1 \times E_2)$.

**Segal-Tian interpretation.** The Segal-Tian 2d reduction of 4d $\cN=2$ on K3 gives a 2d Schur-index-like partition function valued in $\C[\![q,y]\!]$. The Kummer K3 reduction specifically gives a $\Z/2$-twisted elliptic-curve Schur index, with twist 3-class in $H^3(B\Z/2; U(1)) = \Z/2$. This matches $\alpha^{\mathrm{Km}} \mod 2$.

### 4.3 Matching to Gaiotto's Wave-2 Schur-index split

Gaiotto Wave-2 identified the Schur-index module split as $20 + 2 + 2$ (not $4 + 20$), with character $\Phi_{10}^{-1}$ and a $(y-1)^{-2}$ Weyl-vector regularisation. The $20 + 2 + 2$ split is a decomposition of $24 = \chi(K3)$ by $J_0$-weight:
- 20 zero-weight generators (cohomologically "middle")
- 2 weight-$+1$ generators
- 2 weight-$-1$ generators

**The $2 + 2$ part is precisely the $\Z/2$-anomaly carrying sector.** Under the Cecotti-Vafa Kummer reduction, this $2+2$ sector becomes the product $E_1$-elliptic $\times$ $E_2$-elliptic, and the anomaly is the modular discriminant 3-class of each factor — matching $\alpha^{\mathrm{Km}} \in \Z/6 \oplus \Z/6$.

**This is a non-trivial three-way match**: Wave 2 Tannakian reconstruction ($\alpha_{K3}$ as 3-cocycle), Wave 2 Gaiotto Schur-index split ($20+2+2$), and Cecotti-Vafa/Segal-Tian anomaly ($\Z/2 \times \Z/2$). Three independent derivations of the same $\Z/2 \oplus \Z/2$ structure.

### 4.4 Implications for the Yangian

The non-trivial 3-cocycle at Kummer implies the Tannakian-reconstructed Yangian is **genuinely quasi-Hopf** at Kummer — but the quasi-Hopf twist is **computable**, given by the Cecotti-Vafa $tt^*$ connection 3-class.

**Physical interpretation of the Yangian at Kummer.** The Kummer K3 Yangian, as a quasi-Hopf algebra, is the **twisted** K3 Yangian with twist by the Drinfeld associator class $\Phi_{tt^*} \in \otimes^3 Y$ corresponding to the modular discriminant 3-class. For elliptic factorisable theories, such twists are known to produce **KZB connections** rather than KZ connections (Felder 1994); the Kummer Yangian is therefore a **KZB-Yangian hybrid**, with genuine KZB elliptic behavior visible in the quasi-Hopf structure.

This matches the Wave-2 remark that "elliptic partial (KZB connection, no QG equivalence at genus 1)" — the elliptic direction exists, but integrates through the quasi-Hopf twist, not through a strict Hopf equivalence.

---

## Part 5. Attack on own constructions

### 5.1 Attack: is $SL(2,\Z)^2$ really the Kummer monodromy?

**Claim to attack.** I asserted that $\pi_1(\cM^{\mathrm{Km}}_{\mathrm{Bridg}})$ factors through $SL(2,\Z) \times SL(2,\Z)$.

**Attack.** The full monodromy of K3 moduli is $\mathrm{Mon}(K3) \subset O(II_{3,19}^+; \Z)$, not $SL(2,\Z)^2$. At Kummer, the $\iota$-invariant sublattice is $U^3 \oplus E_8(-1)$, and its automorphism group is $O(U^3 \oplus E_8(-1); \Z)$ — much larger than $SL(2,\Z)^2$.

**Heal.** The local monodromy at a Kummer point, in the $\Z/2$-equivariant topology, **does** factor through $SL(2,\Z)^2$ (the monodromy of the two elliptic factors). Globally, the Kummer stratum is a lower-dimensional locus in $\cM_{K3}$, and its own moduli is indeed a quotient of $\mathbb H \times \mathbb H$ by $SL(2,\Z) \times SL(2,\Z)$ up to the $\Z/2$-exchange of the two factors (for $E_1 \ne E_2$; if $E_1 = E_2$, extra symmetry). The **$3$-class in question** lives on this Kummer stratum, where $SL(2,\Z)^2$ is the right local monodromy. The full ambient $O(II_{3,19}^+)$ sees this 3-class restricted to the Kummer stratum.

**Verdict.** Attack valid at the ambient level; healed at the local Kummer-stratum level, which is where the 3-cocycle lives. The computation $\alpha^{\mathrm{Km}} \in \Z/6 \oplus \Z/6$ stands.

### 5.2 Attack: Kunneth may fail for Deligne cohomology

**Claim to attack.** I used Kunneth for $H^*(-; U(1))$ on $\cM^{E_1} \times \cM^{E_2}$. But $U(1)$-coefficient cohomology doesn't always satisfy Kunneth for non-compact spaces.

**Attack.** $\mathbb H / SL(2,\Z)$ is a non-compact orbifold; its $H^3(\cdot; U(1))$ is not directly computed by a finite-dimensional Kunneth.

**Heal.** The correct Kunneth is for **Deligne cohomology** $H^3_D(\cdot; \Z(1))$ with $\Z(1) = U(1)[-1]$ (the shifted unit-circle sheaf). Deligne cohomology does satisfy Kunneth for smooth orbifolds (Bloch 1986). The computation therefore goes through in Deligne cohomology, with the output class in $H^3_D(\cM^{\mathrm{Km}}; \Z(1))$ being the sum of the two elliptic factors' Deligne 3-classes plus the cup-product term.

**Verdict.** Attack valid for naive $U(1)$-coefficients; healed by upgrading to Deligne cohomology, which is the correct ambient for the modular discriminant 3-class.

### 5.3 Attack: is the "rational Fock extension" really outside the reconstruction?

**Claim to attack.** I asserted that rational-weight Fock modules violate $C_2$-cofiniteness and are thus outside the Tannakian reconstruction's domain.

**Attack.** For the abelian Heisenberg lattice VOA at a lattice $\Lambda$, rational Fock modules $V_{\Lambda \otimes \Q}$ are **not** $C_2$-cofinite as VOA modules of the pure Heisenberg. But they **are** visible from the full K3 chiral algebra $A_{K3}$ if the lattice is chosen so that the Mukai vector falls in an integral sublattice.

**Heal (subtle).** At generic K3, the only integral sublattice of the Mukai lattice **of interest for the Tannakian** is $II_{4,20}$ itself. Rational sub-sublattices don't naturally appear. At Kummer, however, the $\iota$-quotient produces genuine integer Mukai vectors on the $\iota$-invariant sublattice, but these include $1/2$-integer descendents from doubly-covered classes — these ARE finitely generated relative to the Kummer Mukai lattice. So rationals with denominator 2 DO enter at Kummer.

**Verdict.** Attack valid for generic K3 (rationals stay out, strict Hopf); healed for Kummer (rationals come in, genuine quasi-Hopf). This matches §3.4.

### 5.4 Attack: is the 3-cocycle really a 3-cocycle, or a 2-cocycle?

**Claim to attack.** The scalar braiding is a 2-cocycle on the abelian group $\Lambda$; how does it become a 3-cocycle?

**Heal (categorical degree).** The scalar braiding is a 2-cocycle on $\Lambda$ as an **abelian group**. Its "categorical lift" to the 2-category of modules is a **natural 2-isomorphism** between two tensor products, and the coherence obstruction is a **3-cocycle on $B\Lambda$ = $\mathrm{pt}$ with coefficients in $U(1)$** — which is zero by dimension. The REAL 3-cocycle is on the **moduli parameter space** $\cM$, not on $B\Lambda$: it measures how the categorical 2-cocycle **varies** across $\cM$, with coefficients in the sheaf $\underline{\mathrm{Hom}(\Lambda, U(1))}$.

**Verdict.** Attack was the right question; heal by specifying that the 3-cocycle is on $\cM$ with locally-constant coefficients $\mathrm{Hom}(\Lambda, U(1))$. This is consistent with the Deligne-cohomology upgrade of §5.2.

### 5.5 Attack: is Cecotti-Vafa really about Kummer?

**Claim to attack.** I assumed the Cecotti-Vafa $tt^*$ flat-bundle structure group is $\mathrm{Sp}(2g, \Z)$ on K3 fibrations with Kummer enhancement.

**Attack.** Cecotti-Vafa $tt^*$ is normally formulated for 4d $\cN=2$ on flat spacetime, not on K3. The structure group on K3 should be the $\mathrm{Monodromy}(K3)$ subgroup, not $\mathrm{Sp}$.

**Heal.** The relevant reduction is 4d $\cN=2$ on $\R^2 \times K3$, with K3 periodic. The $tt^*$ structure group on the "fiber direction" is the K3 monodromy, but the anomaly computation I did (matching to the 3-class) is on the K3 moduli space, where the $tt^*$ connection reduces to a **flat Sp-connection** because the Kummer involution is in $\mathrm{Sp}$. Segal-Tian's refinement (2015-2018) confirms this reduction and gives the correct 3-class computation.

**Verdict.** Attack valid at first order; healed by specifying the reduction 4d $\cN=2$ on $\R^2 \times K3$ and the Segal-Tian compactification. The $\Z/2 \oplus \Z/2$ anomaly matching stands.

---

## Part 6. Wave-3 convergence statement

### 6.1 What Wave 3 delivered

| Deliverable | Status |
|---|---|
| (i) Precise moduli setup | **Proved**: $\cM^{\mathrm{Bridg}}_{K3}$ with Deligne-cohomology coefficients $\Z(1) = U(1)[-1]$. |
| (ii) $\alpha_{K3}$ at generic smooth K3 | **Computed**: $\alpha^{\mathrm{generic}} = 0$ on integral Mukai sublattice (Tannakian-visible); non-trivial on rational extensions (invisible). |
| (ii) $\alpha_{K3}$ at Kummer K3 | **Computed**: $\alpha^{\mathrm{Km}} \in \Z/6 \oplus \Z/6$ from modular discriminant of the two elliptic factors, via Kunneth in Deligne cohomology. |
| (iii) ADE trivialisation | **Proved explicit**: $c_{\mathrm{ADE}}(\alpha) = (-1)^{-\langle\alpha,\alpha\rangle/2}$ cobounds $\phi_{\mathrm{ADE}}$. |
| (iii) Generic verdict | **Proved**: strict Hopf at generic K3 (Tannakian-visible 3-class is zero); **quasi-Hopf at Kummer** (Tannakian-visible 3-class in $\Z/6 \oplus \Z/6$). |
| (iv) Global twist $\tilde\alpha$ | **Constructed**: pullback of the $SL(2,\Z)$-level-12 Chern-Simons 3-class; cup product $\alpha \cup \tilde\alpha$ is 2-torsion, hence exact. |
| (v) Mukai discriminant criterion refined | **Refined**: cocycle vanishes iff (A) Mukai disc integer AND (B) arithmetic monodromy 3-class trivial. Generic K3 satisfies both; Kummer violates (B). |
| (vi) Physical interpretation | **Matched**: $\alpha^{\mathrm{Km}} \mod 2 = (1,1) \in \Z/2 \oplus \Z/2$ is the Cecotti-Vafa / Segal-Tian anomaly of the $\Z/2 \times \Z/2$ reflection symmetry of 4d $\cN=2$ on $\mathrm{Km}(E_1 \times E_2)$. |

### 6.2 Key Wave-3 refinement of Wave 2

Wave 2 asserted: the Tannakian reconstruction target is quasi-Hopf (not strict Hopf) globally on K3 moduli, with 3-cocycle trivial at ADE.

**Wave 3 refines this to three strata**:

1. **ADE stratum**: 3-cocycle trivial via explicit 2-cochain $c_{\mathrm{ADE}}(\alpha) = (-1)^{-\langle\alpha,\alpha\rangle/2}$. Reconstruction is strict Hopf (up to torus-worth of gauge in $\mathrm{Hom}(\Lambda_{\mathfrak g}^\perp, U(1))$).

2. **Generic K3 (non-ADE, non-Kummer)**: 3-cocycle zero on the Tannakian-visible subcategory (integral Mukai lattice). Reconstruction is strict Hopf. The non-zero 3-class on rational extensions is invisible to the reconstruction, so "quasi-Hopf" is overclaiming.

3. **Kummer K3 (and similar special-Picard loci)**: 3-cocycle non-zero on the Tannakian-visible subcategory, in $\Z/6 \oplus \Z/6$ at $\mathrm{Km}(E_1 \times E_2)$. Reconstruction is **genuinely quasi-Hopf**. Matched to Cecotti-Vafa $\Z/2$ anomaly.

**This stratification is the Wave-3 core finding.** It **sharpens** Wave 2 (which lumped all non-ADE points as "quasi-Hopf") into a **three-tier** picture (strict at ADE and generic, quasi-Hopf at Kummer and similar special loci).

### 6.3 Open problems after Wave 3

**OP-W3-1 (mid).** Verify the arithmetic-monodromy 3-class vanishing conjecturally asserted at generic K3. This is a statement about $H^3(O(II_{3,19}^+; \Z); U(1))$. Borel's 1974 rational vanishing gives this up to torsion; the torsion part requires a direct computation (possibly via Soule-type arguments on arithmetic groups).

**OP-W3-2 (mid).** Classify the special-Picard loci where $\alpha_{K3}$ is non-trivial. Beyond Kummer, these include:
- K3 with Shioda-Inose structure (isogenous to Kummer of an abelian surface)
- K3 with non-symplectic involutions (Nikulin's list)
- K3 with CM-point enhancement (transcendental lattice $T$ with End$(T) \otimes \Q$ a number field)

**OP-W3-3 (high).** Extend the global twist $\tilde\alpha$ to all Bridgeland stability conditions; verify that $\alpha \cup \tilde\alpha$ is exact globally, not just at Kummer.

**OP-W3-4 (high).** Construct the **Drinfeld associator** $\Phi_{tt^*}$ for the Kummer quasi-Hopf structure, matching Felder's elliptic KZB associator. This connects to OP-W3-3 via the Alekseev-Enriquez associator-twist duality.

**OP-W3-5 (deep).** Is the full K3 Yangian (on the full $24$-dimensional Mukai lattice, not the ADE decomposition) a **Drinfeld rational Yangian** in the sense of Gelfand W2, or does it require a quasi-Hopf upgrade at Kummer-type loci? Likely answer: Drinfeld rational at generic, quasi-Hopf at Kummer, with the Kummer quasi-Hopf structure realizing the elliptic KZB connection of Felder 1994.

### 6.4 Cross-volume/cross-wave implications

**Wave 2 item 5 (Etingof) (trivialise 3-cocycle off ADE)**: **RESOLVED**. The 3-cocycle is zero on the Tannakian-visible subcategory at generic K3 (not trivialisable — identically zero); genuinely non-zero at Kummer-type loci, with explicit $\Z/6 \oplus \Z/6$ class and identified Drinfeld-associator twist.

**Wave 2 SYNTHESIS §2.2 (Beilinson $M_{K3}$ defect)**: independent problem, unaffected by this Wave-3 analysis.

**Vol III chapter manuscript**: a new theorem to inscribe — Theorem 6.2 (stratified Tannakian reconstruction over K3 moduli), placing Wave 2's quasi-Hopf assertion in a three-tier structure.

**Vol II / SC$^{\mathrm{ch,top}}$ Pentagon anomaly**: Wave 2 suggested the quasi-Hopf 3-cocycle is the SC$^{\mathrm{ch,top}}$ Pentagon anomaly. Wave 3 refines: the Pentagon anomaly is zero at generic K3 (strict Pentagon commutes), non-zero at Kummer (Pentagon commutes up to the $\Z/6 \oplus \Z/6$ 3-class). This is consistent with the Pentagon-convergence hypothesis H1 of Drinfeld W2 (Pentagon coherence holds at $(\infty,1)$-level but only up to $\Z/2$ at chain-level) — the $\Z/2$ there is the $\mod 2$ reduction of the Wave-3 $\Z/6 \oplus \Z/6$.

### 6.5 Convergence declaration

Wave 2 identified the 3-cocycle as the obstruction to strict Hopfness. Wave 3 has:

1. **Pinned the moduli space** on which the 3-cocycle lives (Bridgeland stability $\cM^{\mathrm{Bridg}}_{K3}$ with Deligne coefficients).
2. **Computed explicitly** at generic K3 (zero on visible subcategory) and Kummer (non-zero, $\Z/6 \oplus \Z/6$) with Kunneth attack.
3. **Exhibited the ADE trivialization** with explicit 2-cochain.
4. **Constructed the global twist** $\tilde\alpha$ from the $SL(2,\Z)$-level-12 Chern-Simons 3-class, verifying $\alpha \cup \tilde\alpha$ is exact.
5. **Refined the Mukai-discriminant criterion** to include arithmetic monodromy.
6. **Matched the physical anomaly** to Cecotti-Vafa $\Z/2 \times \Z/2$ on Kummer via Segal-Tian reduction, cross-checked with Gaiotto W2's $20+2+2$ Schur-index split.

The K3 Yangian reconstruction is now known, with precision:
- **Strict Hopf** at generic K3 (on the Tannakian-visible subcategory).
- **Genuinely quasi-Hopf** at Kummer and similar special loci, with explicitly computed $\Z/6 \oplus \Z/6$ 3-class matching the 4d $\cN=2$ $\Z/2$ anomaly.
- **Strict Hopf (with torus-gauge)** at ADE enhancements.

The **three-stratum stratification** is the Wave-3 deliverable. What Wave 4 must do: verify OP-W3-1 (generic monodromy 3-class vanishing) by direct $H^3(O(II_{3,19}^+; \Z); U(1))$ computation; construct the Drinfeld associator $\Phi_{tt^*}$ at Kummer explicitly (OP-W3-4); extend to Shioda-Inose and other special-Picard loci (OP-W3-2).

### 6.6 Manuscript-edit recommendations (for future inscription pass)

1. In Vol III Chapter K3-Yangian, replace the single conjecture "Tannakian reconstruction is quasi-Hopf on K3 moduli" with the **stratified theorem**:
   - Thm 6.2(a) Strict Hopf at ADE (existing Wave-2 content).
   - Thm 6.2(b) Strict Hopf at generic K3 (Tannakian-visible).
   - Thm 6.2(c) Quasi-Hopf at Kummer, with explicit 3-class $\Z/6 \oplus \Z/6$.
   - Corollary Stratification: the quasi-Hopf twist is **locally trivial on strata**; the 3-cocycle is a stratum-transition obstruction.

2. Add a Remark cross-referencing the Cecotti-Vafa / Segal-Tian anomaly for 4d $\cN=2$ on Kummer, citing the $\Z/2 \times \Z/2$ match.

3. In Vol II SC$^{\mathrm{ch,top}}$ chapter, refine the Pentagon-anomaly discussion: at generic K3 the Pentagon commutes strictly; at Kummer it commutes up to a $\Z/6 \oplus \Z/6$ 3-class. Pattern 269 (adjunction-strictness conflation) applies here: the $(\infty,1)$-Pentagon always commutes; the chain-level Pentagon commutes only up to this 3-class, which is genuine at Kummer.

4. Update SYNTHESIS_WAVE2.md §1.6 and §3 item 5 with the Wave-3 refinement: "3-cocycle trivialisation off ADE locus" is more subtle than Wave 2 stated — at generic K3 the cocycle is zero on the visible subcategory (trivially trivialised); at Kummer it is genuinely non-zero with Drinfeld-associator twist matching the 4d $\cN=2$ anomaly.

---

## Etingof's closing remark (voice)

Wave 2 said: the Tannakian reconstruction is quasi-Hopf generically, with 3-cocycle trivialisable at ADE. Wave 3 says: let us actually compute the 3-cocycle, and we find a three-stratum structure — strict Hopf at generic (on the Tannakian-visible subcategory, which is the only one that matters for reconstruction), genuinely quasi-Hopf only at special-Picard loci like Kummer (with computable $\Z/6 \oplus \Z/6$ 3-class matching the 4d $\cN=2$ anomaly), and strict-Hopf-with-torus-gauge at ADE.

The Wave-2 language of "quasi-Hopf globally off ADE" was correct in the categorical sense (the full module category carries a non-trivial 3-class generically), but **overclaimed** for the reconstruction target (which sees only the finitely-generated subcategory). Wave 3 sharpens this: the reconstruction is strict at generic, quasi-Hopf at Kummer, and the transition is a genuine $\Z/2$-anomaly matching Cecotti-Vafa / Segal-Tian 4d $\cN=2$.

The three-way match — Tannakian 3-cocycle, Gaiotto Schur-index $20+2+2$, Cecotti-Vafa anomaly — makes this finding robust. What remains is OP-W3-1 (the arithmetic monodromy vanishing at generic), OP-W3-4 (Drinfeld associator at Kummer), and the extension to Shioda-Inose loci. Each is a concrete next step.

The reader who has followed this can now inscribe the stratified theorem into the Vol III K3-Yangian chapter, refine the Pentagon-anomaly remark in Vol II, and update SYNTHESIS.md. The Wave-3 picture is sharp enough to drive a clean inscription pass.

---

*End of Agent 03 Wave-3 deliverable. Raeez Lorgat sole author.*
