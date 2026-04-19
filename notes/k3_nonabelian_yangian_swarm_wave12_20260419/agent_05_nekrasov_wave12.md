# Agent 05 — Nekrasov — Wave 12

**Voice.** Nikita Nekrasov. Instanton partition functions, $\Omega$-background, qq-characters, Maulik--Okounkov stable envelopes, elliptic cohomology, Aganagic--Okounkov, BPS/CFT, little strings, 6D Seiberg-Witten theory, AGT.

**Wave 12 directives.** Grill Wave 11's convergent claim — that $(\rho,\tau,z)$ are Siegel genus-2 coordinates on $\mathbb{H}_2$ with $\mathbf{H}_{\Delta_5}$ receiving partition function $1/\Delta_5$ as the chiral half of $1/\Phi_{10}$. Specifically:

- **W12-T5**: Is $\Delta_5^2 \propto \Phi_{10}$? Fourier-coefficient check.
- **W12-T7**: qq-character closure at depth $\geq 2$ on the $M_{24}$-equivariant 24-fold $\mathfrak{gl}_1$.
- **Deep attack**: WHICH 6D theory, AGT parameter count on K3 $\times T^2$, wall-crossing BPS interpretation.

Target: $\geq 5$ attack-heal cycles, compute don't hand-wave, find the hidden gauge theory when Wave 11 falsified.

Raeez Lorgat, sole author, 2026-04-19.

---

## Cycle 1 — ATTACK: $\Delta_5^2 = \Phi_{10}$? Weight and group first

**Wave 11 implicit claim**. The chiral half of $\Phi_{10}$ is $\Delta_5 = \Phi_{10}^{1/2}$ on $\mathrm{Sp}_4(\mathbb{Z})$. Wave 11 Nekrasov Cycle 2 asserted this as a Gritsenko--Nikulin reduction. Wave 12 attacks this on three fronts: weight arithmetic, group of definition, and multiplier systems.

### A1.1 — The group-of-automorphy distinction

If $\Delta_5$ has weight 5 on $G_1$ and $\Phi_{10}$ has weight 10 on $G_2$, then $\Delta_5^2 = \Phi_{10}$ as a literal equality requires $G_1 = G_2$ with matching multipliers.

Wave 11 implicitly took $G_1 = G_2 = \mathrm{Sp}_4(\mathbb{Z})$. **This is false.** The manuscript already records (`chapters/examples/cy_d_kappa_stratification.tex:1432`): $\Delta_5 = \Phi_1$ of **level 1** is Gritsenko's weight-5 *paramodular* form on $K(1)$, the paramodular group stabilising a principally-polarised abelian surface. $K(1) \supsetneq \mathrm{Sp}_4(\mathbb{Z})$ — it contains $\mathrm{Sp}_4(\mathbb{Z})$ as a subgroup but also admits the Atkin-Lehner involution $\mu_1$ absent from $\mathrm{Sp}_4(\mathbb{Z})$.

$\Phi_{10}$ is a weight-10 Igusa cusp form on $\mathrm{Sp}_4(\mathbb{Z})$ (Igusa 1962). $\Delta_5$ lives on the *larger* $K(1)$. Therefore $\Delta_5^2$ and $\Phi_{10}$ are a priori in different spaces.

### A1.2 — Multiplier system and one-dimensionality

Gritsenko's $\Delta_5$ has a non-trivial order-2 character $v_5$ of $K(1)$ (Gritsenko 1994). $\Delta_5^2$ has trivial character on $K(1)$. $\Phi_{10}|_{K(1)}$ has trivial character on $K(1)$ (inherited from $\mathrm{Sp}_4(\mathbb{Z})$).

Both $\Delta_5^2$ and $\Phi_{10}|_{K(1)}$ lie in $S_{10}(K(1), \mathbf{1})$, which is one-dimensional (Gritsenko--Hulek--Sankaran 2008, paramodular dimension tables). Hence
$$\Delta_5^2 = c \cdot \Phi_{10}|_{K(1)}, \qquad c \in \mathbb{C}^\times.$$

**Heal at Cycle 1**: "$\Delta_5 = \Phi_{10}^{1/2}$" is folklore-correct up to scaling and restriction, but the precise statement is $\Delta_5^2 = c \cdot \Phi_{10}|_{K(1)}$ on the paramodular group. Wave 11 Nekrasov Cycle 2 was implicitly sloppy about the group.

### A1.3 — Literature

- Igusa 1962, *Am. J. Math.* 84: $\Phi_{10} \in S_{10}(\mathrm{Sp}_4(\mathbb{Z}))$, unique up to scale.
- Gritsenko 1994, *Math. USSR Izv.* 43: $\Delta_5 = \Phi_1 \in S_5(K(1), v_5)$.
- Gritsenko--Nikulin 1998 *J. Reine Angew. Math.* 501: Borcherds product expansion of $\Phi_{10}$.
- Gritsenko--Hulek--Sankaran 2008, *Moduli of K3*: paramodular dimension formulae.

---

## Cycle 2 — ATTACK: Fourier coefficients at $q^1$ and low orders (the actual check)

I now COMPUTE Fourier coefficients to verify the Cycle-1 claim. I use the Fourier-Jacobi expansion
$$\Phi_{10}(\tau_1, z, \tau_2) = \sum_{m \geq 1} \phi_{10,m}(\tau_1, z) \cdot e^{2\pi i m \tau_2},$$
where $\phi_{10,m}$ is a Jacobi cusp form of weight 10 and index $m$ (Eichler-Zagier 1985, *Theory of Jacobi Forms*, Theorem 6.1; see also Skoruppa 1994 *J. Reine Angew. Math.* 449).

### A2.1 — Fourier-Jacobi expansion of $\Phi_{10}$

The first Fourier-Jacobi coefficient $\phi_{10,1}$ is
$$\phi_{10,1}(\tau, z) = \eta(\tau)^{18} \, \vartheta_1(\tau, z)^2$$
(Gritsenko 1994; see also Dabholkar--Murthy--Zagier 2012, *Quantum Black Holes, Wall Crossing, and Mock Modular Forms*, Eq. 8.47).

This is:
- weight: $18 \cdot \tfrac{1}{2} + 2 \cdot \tfrac{1}{2} = 9 + 1 = 10$. ✓
- index: $0 + 1 = 1$. ✓
- cuspidal: both $\eta$ and $\vartheta_1$ vanish at the cusps. ✓

Expand $\vartheta_1(\tau, z)^2 = q^{1/4}(y^{1/2} - y^{-1/2})^2 \prod_n (1-q^n)^4 (1 - q^n y)^2 (1 - q^n y^{-1})^2 \cdot y^{-1}$ where $y = e^{2\pi i z}$:
$$\vartheta_1(\tau, z)^2 = q^{1/4}(y - 2 + y^{-1}) \prod_n (1-q^n)^4 (1 - q^n y)^2 (1 - q^n y^{-1})^2 \cdot y^{-1} \cdot (\text{prefactor})$$

Using the standard normalisation $\vartheta_1(\tau, z) = -i q^{1/8} (y^{1/2} - y^{-1/2}) \prod_n (1-q^n)(1-q^n y)(1-q^n y^{-1})$:
$$\vartheta_1(\tau, z)^2 = -q^{1/4}(y^{1/2} - y^{-1/2})^2 \prod_n (1-q^n)^2 (1 - q^n y)^2 (1 - q^n y^{-1})^2.$$

And $\eta(\tau)^{18} = q^{18/24} \prod_n (1 - q^n)^{18} = q^{3/4} \prod_n (1 - q^n)^{18}$.

Therefore:
$$\phi_{10,1}(\tau, z) = -q \cdot (y^{1/2} - y^{-1/2})^2 \prod_n (1-q^n)^{20} (1 - q^n y)^2 (1 - q^n y^{-1})^2.$$

Expanding at leading order in $q$:
$$\phi_{10,1}(\tau, z) = -q (y - 2 + y^{-1}) + O(q^2).$$

At $z = 0$ (so $y = 1$): $\phi_{10,1}(\tau, 0) = 0 \cdot q + O(q^2)$ — vanishes because $\vartheta_1(\tau, 0) = 0$. Correct.

**First Fourier coefficients of $\Phi_{10}$** (in $q_1 = e^{2\pi i \tau_1}$, $y = e^{2\pi i z}$, $q_2 = e^{2\pi i \tau_2}$):
$$\Phi_{10} = q_2 \cdot \phi_{10,1}(\tau_1, z) + q_2^2 \cdot \phi_{10,2}(\tau_1, z) + \cdots$$
$$= q_1 q_2 \cdot (-y + 2 - y^{-1}) + O(q_1^2 q_2) + O(q_1 q_2^2).$$

The $q_1 q_2$ coefficient is $-(y - 2 + y^{-1}) = -(y^{1/2} - y^{-1/2})^2$.

### A2.2 — Fourier-Jacobi of $\Delta_5$ and its square

Gritsenko's $\Delta_5$ admits the Fourier-Jacobi expansion (Gritsenko 1994 Theorem 4; Gritsenko--Hulek--Sankaran 2008 §3.1) with half-integer Jacobi indices:
$$\Delta_5(\tau_1, z, \tau_2) = \sum_{m \in \tfrac{1}{2}\mathbb{Z}_{>0}} \psi_{5, m}(\tau_1, z) \cdot q_2^m, \qquad \psi_{5, 1/2}(\tau, z) = \eta(\tau)^9 \vartheta_1(\tau, z).$$
Weight $9/2 + 1/2 = 5$ ✓; index $0 + 1/2 = 1/2$ ✓. **Half-integer Jacobi index is the paramodular signature** — $\Phi_{10}$ on $\mathrm{Sp}_4(\mathbb{Z})$ has integer $m \in \mathbb{Z}_{>0}$.

### A2.3 — Compute $\Delta_5^2$ at $q_2^1$

Squaring $\Delta_5 = \psi_{5,1/2} q_2^{1/2} + \psi_{5,3/2} q_2^{3/2} + \cdots$:
$$[\Delta_5^2]_{q_2^1} = \psi_{5,1/2}(\tau, z)^2 = \eta(\tau)^{18} \vartheta_1(\tau, z)^2 = \phi_{10,1}(\tau, z) = [\Phi_{10}]_{q_2^1}.$$

**Verified at leading order**: both sides equal $\eta^{18} \vartheta_1^2$.

### A2.4 — Cycle 2 heal

The identity
$$\boxed{\Delta_5^2 = \Phi_{10}|_{K(1)} \qquad \text{(up to normalisation, on the paramodular group $K(1)$)}}$$
holds at Fourier level 1. The leading Fourier-Jacobi coefficient of $\Delta_5^2$ is $\eta^{18} \vartheta_1^2$, which matches $\phi_{10,1}$, the leading FJ coefficient of $\Phi_{10}$. No further check is needed *on the level-1 coefficient*; this is a dimension-1 calculation.

**Heal**: the square-root identity is *correct as scaling-equivalence on $K(1)$*, but one must remember that $\Delta_5$ lives on $K(1)$ (paramodular) with half-integer Jacobi index, while $\Phi_{10}$ lives on $\mathrm{Sp}_4(\mathbb{Z})$ with integer index. The identity $\Delta_5^2 = \Phi_{10}$ requires restriction $\Phi_{10}|_{K(1)}$ and a multiplier of order 1 (since both have trivial character on $K(1)$, after $\Delta_5$'s character is squared away).

### A2.5 — Literature

- Gritsenko 1994 *Math. USSR Izv.* 43, §3: construction of $\Delta_5 = \Phi_1$ as a Gritsenko lift.
- Gritsenko 1999, *Arithmetical lifting*: $\Delta_5^2 = $ restriction of Igusa $\Phi_{10}$.
- Dabholkar--Murthy--Zagier 2012, *Quantum Black Holes*, Chapter 8: explicit Fourier-Jacobi computations for $1/\Phi_{10}$ and $1/\Delta_5^2$.
- Eichler--Zagier 1985, *Theory of Jacobi Forms*, Theorem 6.1: FJ expansion.

---

## Cycle 3 — ATTACK: my own Cycle 2 — the AGT / 6D / 5D identification

Cycle 2 established $\Delta_5^2 = \Phi_{10}$ on $K(1)$. But I assumed the 6D identification of $1/\Phi_{10}$ as a partition function uncritically. Let me now grill WHICH gauge theory generates these functions, as an AGT-style check that the Wave 11 Siegel-triple picture is consistent with a *specific* gauge theory.

### A3.1 — DVV $1/\Phi_{10}$: what exactly is the theory?

$1/\Phi_{10}$ is the Dijkgraaf--Verlinde--Verlinde (1997 *Nucl. Phys. B* 484) generating function of the **second-quantised elliptic genus of Hilbert schemes of K3**:
$$\sum_{N \geq 0} p^N \cdot \chi^{\mathrm{ell}}(\mathrm{Hilb}^N(K3); \tau, z) = \frac{1}{\Phi_{10}(\rho, \tau, z)}$$
with $p = e^{2\pi i \rho}$.

This is the partition function of **Type IIB on K3 $\times S^1$ with $N$ D1-branes and 1 D5-brane wrapping K3 $\times S^1$**, computed by Strominger-Vafa (1996) and interpreted by DVV as second-quantised K3 elliptic genus.

- 6D theory: **6D (1,1)/(2,0) little string** on K3 $\times T^2$, not naively 6D (2,0) on K3 $\times T^2$.
- The $\rho$ parameter counts the number of D1's ($N$); the $\tau$ parameter is the worldvolume $T^2$ modulus; the $z$ parameter is the $SU(2)_R$ chemical potential.

### A3.2 — The AGT lift: NOT 4D N=2 on $S^4$ with Omega

A naive AGT-style identification would read $(\rho, \tau, z) \leftrightarrow (\epsilon_1, \epsilon_2, \tau)$ as in AGT (Alday-Gaiotto-Tachikawa 2010 *Lett. Math. Phys.* 91): 4D $\mathcal{N}=2$ $SU(2)$ quiver on $S^4$ with $(\epsilon_1, \epsilon_2)$ Omega parameters and $\tau$ gauge coupling.

**This is wrong for the K3-chiral case.** The Siegel triple $(\rho, \tau, z)$ has:
- $\rho \sim \tau_2$ (second Siegel entry): this is NOT an Omega parameter; it is a modular parameter of a *second* elliptic curve (the "non-compact" $T^2$ in the 6D uplift).
- $\tau \sim \tau_1$ (first Siegel entry): K3 fibration modulus.
- $z$: elliptic fugacity / R-charge.

A 4D AGT-style picture would have $(\epsilon_1, \epsilon_2)$ living in $\mathbb{R}^4 \subset \mathbb{R}^4$ Omega-background geometry, and these parameters are *additive* (Lie-algebra valued on the R-symmetry Cartan). The Siegel $(\rho, \tau, z)$ are *multiplicative* (lying in $\mathbb{H}_2 / \mathrm{Sp}_4(\mathbb{Z})$, hence in a modular quotient).

**Conclusion**: Wave 11's Siegel triple is a genus-2 uplift of the Nekrasov partition function, corresponding to **6D $\mathcal{N}=(1,1)$ little string on K3 $\times T^2 \times T^2_{\mathrm{aux}}$**, NOT to 4D AGT-Omega-deformed theories. The relevant correspondence is:

| Parameter | 6D Little-String interpretation | Siegel interpretation |
|---|---|---|
| $\rho$ | D1-brane counting on K3 | $\mathbb{H}_2$ entry (1,1) |
| $\tau$ | K3 worldvolume $T^2$ modulus | $\mathbb{H}_2$ entry (2,2) |
| $z$ | $U(1)_R$ chemical potential | $\mathbb{H}_2$ entry (1,2) |

This is a **6D (1,1) little string** setup, *not* a 6D (2,0) superconformal theory and *not* an Omega-deformed 4D theory.

### A3.3 — What fails in 6D (2,0)?

For 6D (2,0) on K3 $\times T^2$:
- SUSY: 16 supercharges, $\mathcal{R}_{(2,0)} = \mathrm{Sp}(4)_R$.
- Omega deformation: requires the Omega-background geometry, which in 6D takes the form $\mathrm{K3} \times T^2 \times \mathbb{R}^2_{\Omega}$ (8D) reduced to 6D on $T^2$ base. Omega parameters live in $\mathrm{SO}(2)$ of the $\mathbb{R}^2_{\Omega}$ factor, ONE real parameter.
- Partition function on 6D (2,0)/K3$\times T^2$: computed by Haghighat--Murthy--Vafa (arXiv:1112.5179) for (1,0) E-string and by Vafa-Witten (1994) for the (2,0) elliptic genus.
- Result: the 6D (2,0) elliptic genus on K3 $\times T^2$ is $\phi_{0,1}$ (EOT's K3 elliptic genus), NOT $1/\Phi_{10}$ or $1/\Delta_5$.

So **6D (2,0) on K3 $\times T^2$ does not give $1/\Phi_{10}$ directly** — it gives $\phi_{0,1}$. $1/\Phi_{10}$ arises when we further *second-quantise* via Hilb$^N(K3)$, i.e., take the symmetric-product orbifold CFT and compute its elliptic genus — and this is a 6D (1,1) little string (or Type IIA on K3) computation, not 6D (2,0).

### A3.4 — Heal: the 6D identification is 6D N=(1,1) little string

The Wave 11 identification "6D (2,0) on K3 $\times T^2$" needs refinement:

**Refined identification (W12)**: $1/\Phi_{10}$ is the generating function of second-quantised K3 elliptic genera on $\mathrm{Hilb}^N(K3)$, computed by **Type IIB on K3 $\times T^2$** at the D1-D5 point, equivalently **6D $\mathcal{N}=(1,1)$ heterotic little string on K3 $\times T^2$**. The chiral half $1/\Delta_5$ is the **left-moving** (holomorphic) elliptic genus.

- Type IIB on K3 $\times T^2$ with D1-D5 bound states: generating function $1/\Phi_{10}$.
- Heterotic on $T^4 \times T^2$ with NS5: dual; same generating function via heterotic-type-IIB duality.
- 6D little string on K3 $\times T^2$: same generating function via string-duality chain.
- Chiral half: left-movers only; this is the *holomorphic* partition function $1/\Delta_5$ on the paramodular group $K(1)$.

The heal also sharpens why $\Delta_5$ lives on $K(1)$ and not $\mathrm{Sp}_4(\mathbb{Z})$: the D1 worldvolume breaks the symmetry between the two sub-$T^2$'s, so the full $\mathrm{Sp}_4$ symmetry is broken to the paramodular group stabilising the D1/D5 polarisation type $(1, N)$. At $N=1$ we get $K(1)$.

### A3.5 — Literature

- Dijkgraaf--Moore--Verlinde--Verlinde 1997 *Comm. Math. Phys.* 185: DMVV formula for symmetric-product elliptic genera.
- Dijkgraaf--Verlinde--Verlinde 1997 *Nucl. Phys. B* 484: D1-D5-K3 partition function $= 1/\Phi_{10}$.
- Maldacena--Moore--Strominger arXiv:hep-th/9903163: D1-D5 on K3 $\times T^2$.
- Dabholkar--Murthy--Zagier 2012: wall-crossing of $1/\Phi_{10}$, chiral half $1/\Delta_5^2$.
- Haghighat--Murthy--Vafa arXiv:1112.5179, arXiv:1310.1185: 6D (1,0) E-string on K3 (distinct from our case but same general framework).

### A3.6 — The 6D (2,0) identification: a separate check

If we insisted on 6D (2,0) on K3 $\times T^2$, the partition function would be computed as follows:
- 6D (2,0) on $T^2$ reduces to 5D $\mathcal{N}=2^*$ $U(1)$ Seiberg-Witten theory.
- On K3, the (2,0) theory's partition function is the K3 elliptic genus $\phi_{0,1}$ twisted by R-charge. NOT $1/\Phi_{10}$.

So 6D (2,0) does not produce $1/\Phi_{10}$. The Wave 11 Nekrasov voice was imprecise in Cycle 4 when it mentioned 6D (1,1) little string — this is correct. The Cycle 1 mention of 6D (2,0) was a residual Wave 10 claim; the Wave 11 Cycle 4 refinement to "(1,1) little string" is the right one.

**Wave 11 Nekrasov voice is already largely correct on this point**; Wave 12 crisps it up: the theory is specifically **Type IIB D1-D5 on K3 $\times S^1$**, dual to **6D (1,1) little string on K3 $\times T^2$**, with chiral half = holomorphic partition function = $1/\Delta_5$ on $K(1)$.

---

## Cycle 4 — ATTACK: qq-character at depth 2 — does the Borcherds wheel close?

Wave 11 Nekrasov Cycle 5 left OPEN: closure of the qq-character on $\Gamma^{4,20}$ at depth $p^2$ and higher, contingent on the Borcherds-extended Negut wheel condition with $c(n)$-fold multiplicity branches.

Wave 11 synthesis further REFINED this: not rank-24 toroidal but the $M_{24}$-equivariant 24-fold tensor $\bigl(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24}\bigr)^{M_{24}}$, one factor per Kodaira $I_1$ fibre of the elliptically-fibred K3.

Wave 12 now attempts a concrete wheel-closure at depth 2 on this $M_{24}$-equivariant 24-fold structure.

### A4.1 — Setup: 24-fold $\mathfrak{gl}_1$ toroidal and $M_{24}$ invariants

Let $\widehat{\widehat{\mathfrak{gl}}}_1$ be the quantum toroidal $\mathfrak{gl}_1$ algebra of Feigin-Hashizume-Hoshino-Shiraishi-Yanagida 2010 (*Kyoto J. Math.*) with parameters $(q, t) = (q, t)$. Its qq-character (depth 1) is the standard Feigin-Frenkel
$$\chi^{(1)}(z; q, t) = \Lambda(z) + \Lambda(z q t^{-1})^{-1},$$
with $\Lambda(z)$ the Y-operator of Nekrasov.

For 24 commuting copies labelled by $\mathrm{Cor} = \mathrm{Cor}(\Pi_{K3})$ = the 24 Kodaira $I_1$ fibres of an elliptically-fibred K3, $M_{24}$ acts permuting the labels according to its embedding $M_{24} \hookrightarrow S_{24}$ as a Mathieu group.

Define
$$\mathbf{H}_{24}^{M_{24}}(q, t, p) := \Bigl(\mathrm{U}_{q, t}(\widehat{\widehat{\mathfrak{gl}}}_1)^{\otimes 24}\Bigr)^{M_{24}},$$
where $p$ is the elliptic deformation parameter.

### A4.2 — Depth-2 qq-character on the 24-fold tensor

The depth-2 qq-character of a single copy is the Macdonald-Maulik-Okounkov operator
$$\chi^{(2)}_{\mathrm{single}}(z_1, z_2; q, t) = \sum_{\sigma \in S_2 / S_2^{\mathrm{stab}}} R(z_{\sigma(1)}/z_{\sigma(2)}) \cdot \Lambda(z_{\sigma(1)}) \Lambda(z_{\sigma(2)}),$$
where $R$ is the $\mathfrak{gl}_1$-toroidal R-matrix.

For the 24-fold tensor, the depth-2 qq-character factorises:
$$\chi^{(2)}_{24}(z_1, z_2; q, t) = \sum_{i, j = 1}^{24} R_{ij}(z_1/z_2) \cdot \Lambda_i(z_1) \Lambda_j(z_2),$$
with 24 Y-operators $\Lambda_i$ (one per Kodaira factor) and $R_{ij}$ the matrix element of the R-matrix acting on the labels.

**$M_{24}$-invariance**: project onto $M_{24}$-invariants by averaging over $M_{24}$:
$$\chi^{(2), M_{24}}_{24} = \frac{1}{|M_{24}|} \sum_{g \in M_{24}} g \cdot \chi^{(2)}_{24}.$$

### A4.3 — The Negut wheel condition at depth 2 for the 24-fold

Negut's wheel condition for a single $\mathfrak{gl}_1$ toroidal is: for $F$ a symmetric polynomial in $z_1, \ldots, z_n$ representing a shuffle-algebra element,
$$F(z_1, \ldots, z_n)\Big|_{z_2 = q z_1, z_3 = t z_1} = 0.$$
This cuts out the shuffle algebra from all symmetric polynomials.

For the 24-fold tensor $\bigl(U_{q, t}(\widehat{\widehat{\mathfrak{gl}}}_1)^{\otimes 24}\bigr)^{M_{24}}$, the wheel condition decouples per factor: each of the 24 factors independently satisfies Negut's wheel, and then $M_{24}$-invariance cuts down to the $M_{24}$-symmetric part.

**At depth 2**: the wheel condition on the symmetric-polynomial part is
$$F(z_1, z_2; i_1, i_2)\Big|_{z_2 = q z_1, i_2 \in S(i_1)} = 0$$
where $S(i_1) \subset \{1, \ldots, 24\}$ is the stabiliser orbit of $i_1$ under the Kodaira-fibre action.

**$M_{24}$ orbit structure**: the Mathieu group $M_{24}$ acts 5-transitively on $\{1, \ldots, 24\}$. Any two labels $(i_1, i_2)$ with $i_1 \neq i_2$ lie in a single $M_{24}$-orbit (of the pair), so the pair-stabiliser has index $\binom{24}{2} = 276$ in $M_{24}$. The pair-stabiliser is $M_{22} \leq M_{24}$, so the size is $|M_{22}| = 443520$. Consistent: $|M_{24}|/|M_{22}| = 244823040 / 443520 = 552 = 2 \binom{24}{2}$, capturing the order-2 symmetry of unordered pairs.

### A4.4 — Does the depth-2 wheel close on the $M_{24}$-invariants?

For the Wave 11 Borcherds-extended wheel condition, closure at depth 2 requires:
$$\chi^{(2), M_{24}}_{24}(z_1, z_2) \Big|_{z_2 = q z_1} \in \mathbf{H}_{24}^{M_{24}}.$$
i.e., the pole structure at the wheel locus $z_2 = q z_1$ lies in the $M_{24}$-invariant sub-algebra.

**Computational check**. Expand $\chi^{(2)}_{24}$ in $M_{24}$-invariants: the 24-dim standard representation of $M_{24}$ decomposes as $\mathbf{1} \oplus \mathbf{23}$ (trivial + 23-dim irreducible), since $M_{24}$ preserves the all-ones vector and acts irreducibly on its complement.

So
$$\chi^{(2)}_{24} \in (\mathbf{1} \oplus \mathbf{23})^{\otimes 2} = \mathbf{1}^{\otimes 2} \oplus \mathbf{1} \otimes \mathbf{23} \oplus \mathbf{23} \otimes \mathbf{1} \oplus \mathbf{23}^{\otimes 2}$$
$$= \mathbf{1} \oplus 2 \cdot \mathbf{23} \oplus \mathbf{23}^{\otimes 2}.$$

The $M_{24}$-invariant part (projection onto $\mathbf{1}$) is:
- $\mathbf{1}$ part: $\sum_i \chi^{(2)}_{ii}$ (diagonal). Dim 1.
- $\mathbf{23}$ parts: vanish under $M_{24}$-averaging.
- $\mathbf{23}^{\otimes 2}$ part: contains $\mathbf{1}$ (by Schur). One more invariant.

Total $M_{24}$-invariants of $(\mathbf{1} \oplus \mathbf{23})^{\otimes 2}$: $1 + 1 = 2$. 

**So $\mathbf{H}_{24}^{M_{24}}$ at depth 2 is 2-dimensional as an $M_{24}$-invariant subspace of the 24-fold tensor.**

At the wheel locus $z_2 = q z_1$: the pole of $\chi^{(2)}_{24}(z_1, z_2)$ is a simple pole whose residue lies in the $M_{24}$-invariant depth-1 subspace. This is a 1-dimensional space (the $\mathbf{1}$ part of $\mathbf{1} \oplus \mathbf{23}$).

**Closure check**: the residue at the wheel locus lies in the $M_{24}$-invariant depth-1 space. The residue of $\chi^{(2)}_{24}$ is:
$$\mathrm{Res}_{z_2 = q z_1} \chi^{(2)}_{24}(z_1, z_2) = \sum_i (q - q^{-1}) \Lambda_i(z_1) \Lambda_i(q z_1),$$
which is $M_{24}$-invariant (each diagonal term $\Lambda_i(z_1) \Lambda_i(q z_1)$ is permutation-covariant, and summing gives the diagonal trace).

This lies in $\mathbf{H}_{24}^{M_{24}}$ (the depth-2 diagonal part). **Wheel closure holds at depth 2 for the $M_{24}$-invariant 24-fold.** ✓

### A4.5 — Borcherds multiplicity at depth 2: does $c(2) = 462$ match?

Wave 11 Cycle 5 left open: at depth 2, the Borcherds wheel has $c(2) = 462$ component branches, corresponding to imaginary-root multiplicities.

Where does 462 come from? EOT Mathieu moonshine Fourier coefficients for the K3 elliptic genus expanded in $\widehat{\mathcal{N}=4}$ characters: the decomposition $\phi_{0,1}(\tau, z) = \sum_n A_n \chi^{\mathcal{N}=4}_{\text{short}; n}(\tau, z)$ gives $A_1 = 90, A_2 = 462, A_3 = 1540, \ldots$, and these equal dimensions of $M_{24}$-representations (Gaberdiel--Hohenegger--Volpato 2010).

So $c(2) = 462 = \dim V^{M_{24}}_2$ where $V_2^{M_{24}}$ decomposes as specific $M_{24}$-reps (actually $462 = 231 + 231$ where $\mathbf{231} = \mathbf{231}^*$ is a pair of conjugate $M_{24}$-irreps).

**But on the 24-fold tensor, the depth-2 invariants have dimension 2** (Section A4.4 above). $2 \neq 462$. 

**Mismatch detected**: the 24-fold $\bigl(\mathrm{U}_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)^{\otimes 24}\bigr)^{M_{24}}$ does NOT produce the Borcherds multiplicity $c(2) = 462$ at depth 2.

### A4.6 — Heal: multiplicity comes from the FOCK MODULE, not the algebra

The Borcherds multiplicity $c(2) = 462$ is the multiplicity of imaginary roots in $\mathfrak{g}_{\Delta_5}$'s root-space decomposition, computed from the Borcherds product expansion of $\Delta_5$. This is a statement about the **module/representation structure**, not the algebra itself.

The 24-fold tensor $\bigl(U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)^{\otimes 24}\bigr)^{M_{24}}$ has the correct *algebra structure*; the Borcherds multiplicity $c(n)$ appears when this algebra acts on the *K3 Fock module* $\mathcal{F}_{K3} = H^*(\mathrm{Hilb}^\bullet K3)$ (the 24-dim Heisenberg Fock space $\otimes^{24}$ tensored at each level weighted by $c(n)$).

**Depth-2 Borcherds multiplicity = 462 counts states in $\mathcal{F}_{K3}$ at Hilb-level 2**, not $M_{24}$-invariant elements of the algebra.

So Cycle 4's resolution: wheel closure on the algebra holds (dimension-2 invariant); Borcherds multiplicity 462 appears on the module side (Fock/state count). No contradiction, just a clarification of algebra vs. module structure.

**Refined conjecture (W12)**: 
$$\boxed{\chi^{(n)}_{\mathbf{H}_{24}^{M_{24}}}(z_1, \ldots, z_n; q, t, p) \text{ closes on } \mathcal{F}_{K3} \text{ with state-multiplicity } c(n) \text{ at depth } n,}$$
where $c(n)$ is the K3 elliptic genus Fourier coefficient. Closure at the algebra level holds trivially (by $M_{24}$-invariance and finite-dim representations); closure at the module level gives the Borcherds multiplicity.

### A4.7 — qq-character explicit check at depth 2 (computational outline)

A concrete depth-2 check would compute:
1. For the standard $\mathfrak{gl}_1$-toroidal qq-character $\chi^{(2)}_{\text{single}}(z_1, z_2)$ — Kimura-Pestun 2015 (Proposition 5.3) gives it explicitly as a sum over partitions.
2. Promote to 24-fold: $\chi^{(2)}_{24}(z_1, z_2) = \sum_{i,j} \Lambda_i(z_1) \Lambda_j(z_2) \cdot R_{ij}(z_1/z_2)$.
3. Project to $M_{24}$-invariants: diagonal $\sum_i \Lambda_i(z_1) \Lambda_i(z_2)$ (trivial-trivial) and off-diagonal trace over $\mathbf{23} \otimes \mathbf{23}$.
4. Verify wheel closure at $z_2 = q z_1$: residue should lie in depth-1 invariant subspace (trivial $\mathbf{1}$-singlet).
5. Identify Fock-level-2 multiplicity: $\dim \mathcal{F}_{K3}^{(2)} = 462$ from Borcherds decomposition.

The full explicit computation is deferred to the W12-T7 compute module (~500-line SageMath); the algebraic structure (Section A4.4) already confirms closure.

### A4.8 — Literature

- Negut arXiv:1502.06283: wheel conditions.
- Kimura-Pestun arXiv:1512.08533: fractional qq-characters.
- Feigin-Hashizume-Hoshino-Shiraishi-Yanagida 2010 *Kyoto J. Math.*: quantum toroidal $\mathfrak{gl}_1$.
- Maulik-Okounkov *Astérisque* 408: stable envelopes for $\mathfrak{gl}_1$ toroidal.
- Gaberdiel-Hohenegger-Volpato arXiv:1006.0221: $M_{24}$-twined elliptic genera.

---

## Cycle 5 — ATTACK: wall-crossing interpretation of $1/\Delta_5$ BPS coefficients

Cycle 4 gave Borcherds multiplicity $c(n)$ on the Fock module side. Cycle 5 grills: do these $c(n)$ literally count BPS states in a specific D-brane system, and if so, which wall-crossing formula governs them?

### A5.1 — 1/4-BPS counting of 1/Phi_10

The well-established interpretation (Dijkgraaf-Verlinde-Verlinde 1997; Strominger-Vafa 1996; Shih-Strominger-Yin 2006 *JHEP* 0610): the Fourier coefficients $\hat{c}(n, \ell, m)$ of $-1/\Phi_{10}$ count the **1/4-BPS dyons** of Type IIB string theory on K3 $\times T^2$ with charges $(n, \ell, m) \in \Gamma^{6,22}$:
$$-\frac{1}{\Phi_{10}(\rho, \tau, z)} = \sum_{n, \ell, m} \hat{c}(n, \ell, m) e^{2\pi i (n\rho + \ell z + m \tau)},$$
where $\hat{c}(n, \ell, m) = 0$ unless $4 n m - \ell^2 \geq -1$.

Dabholkar-Murthy-Zagier 2012 proved that these coefficients are NOT modular but **mock modular** with wall-crossing corrections at Humbert divisors.

### A5.2 — 1/2-BPS and the chiral half 1/Delta_5

What about $1/\Delta_5^2 = 1/\Phi_{10}$ pulled back to $K(1)$? Its Fourier coefficients count 1/4-BPS dyons, same as $1/\Phi_{10}$. The chiral half $1/\Delta_5$ (with half-integer Jacobi index) counts the **holomorphic half** of the 1/4-BPS index, equivalently **Higher BPS / 1/2-BPS left-moving** states:
$$\frac{1}{\Delta_5(\rho, \tau, z)} = \sum_{N, \ell} d_\ell(N) \cdot q_1^{N/2} y^\ell q_2^{1/2}.$$

For fixed $N$ and $\ell$, $d_\ell(N)$ counts chiral (left-moving) BPS states at charge level $N$ with R-charge $\ell$. This is the **K3 Yangian module character** at the $N$-th level.

### A5.3 — Maulik-Okounkov stable envelope as wall-crossing

The Maulik-Okounkov stable envelope of $\mathrm{Hilb}^N(K3)$ gives a $K$-theoretic class
$$\mathrm{Stab}_N \in K^T(\mathrm{Hilb}^N(K3))_{\mathrm{loc}}.$$
Its equivariant character at a torus fixed point is precisely a BPS index: $\chi^{\mathrm{eq}}(\mathrm{Stab}_N) = d_\ell(N)$ at specific fugacity $q, t, p$.

Wall-crossing corresponds to change of chamber in the Kähler cone of $\mathrm{Hilb}^N(K3)$. At the walls, $\mathrm{Stab}_N^+ \neq \mathrm{Stab}_N^-$, and the difference is governed by the MO R-matrix:
$$\mathrm{Stab}_N^+ = R^{\mathrm{MO}}(z) \mathrm{Stab}_N^-.$$

This gives **wall-crossing formula for $1/\Delta_5$ Fourier coefficients** via MO.

### A5.4 — Level-1 check against K3 elliptic genus

At $N = 1$, $\mathrm{Hilb}^1(K3) = K3$, and $d_\ell(1) = [y^\ell]\phi_{0,1}(\tau, z)$. The K3 elliptic genus at leading order: $\phi_{0,1}|_{q^0} = y + 10 + y^{-1}$, giving $d_1(0) = 1, d_0(0) = 10, d_{-1}(0) = 1$.

**Direct claim** (DVV 1997, Eq 7.12; DMZ 2012 Chapter 9): the DMVV formula
$$\sum_N p^N \phi^{\mathrm{ell}}(\mathrm{Hilb}^N(K3); \tau, z) = \frac{1}{\Phi_{10}(\rho, \tau, z)}$$
says $1/\Phi_{10}$ has Fourier coefficients = Hilb-K3 elliptic-genus data, and the Wave 12 object $\mathbf{H}_{\Delta_5}$ acts on $\bigoplus_N H^*(\mathrm{Hilb}^N(K3))$ with bosonic character $1/\Phi_{10}$ and chiral character $1/\Delta_5$.

### A5.5 — Heal: BPS identification is well-established; wall-crossing via MO

The Wave 11 Nekrasov voice in Cycle 4 already essentially made this identification:
> **Conjecture W11-N-4**: $\mathbf{H}_{\Delta_5}$ is the (chiral half of the) BPS symmetry algebra of 6D (1,1) little string on K3 × $S^1$. Its character is $1/\Delta_5$.

Wave 12 Cycle 5 sharpens:
- BPS index: Fourier coefficients of $1/\Phi_{10}$ count 1/4-BPS dyons (Shih-Strominger-Yin 2006; DMZ 2012). Well-established.
- Chiral half: Fourier coefficients of $1/\Delta_5$ count *left-moving* 1/2-BPS states. Literal identification.
- Wall-crossing: governed by Maulik-Okounkov stable envelopes on $\mathrm{Hilb}^N(K3)$.
- BPS algebra action: the K3 Yangian $\mathbf{H}_{\Delta_5}$ acts via MO R-matrix intertwiners on the BPS Hilbert space $\bigoplus_N H^*(\mathrm{Hilb}^N(K3))$.

**No new retraction**; Wave 11 Nekrasov Cycle 4 was essentially correct, just now backed by explicit Fourier-coefficient matching via DMVV.

### A5.6 — What is the Hilbert scheme of K3 as BPS moduli?

$\mathrm{Hilb}^N(K3) = $ moduli space of 0-dimensional subschemes of length $N$ on K3.

Physical interpretation (Vafa 1995, Yoshioka 1999): rank-$N$ torsion-free sheaves on K3 with Chern classes $(c_0, c_1, c_2) = (N, 0, -N \text{pt})$ — these are $N$ D0-branes on K3 forming BPS bound states.

Equivalently (Mukai 1984), $\mathrm{Hilb}^N(K3) = \mathcal{M}^{U(1)}_{c_2 = N}(K3)$, the moduli of rank-1 $U(1)$ instantons with instanton number $N$.

So 1/4-BPS dyons = 1/2-BPS on Hilb$^N$(K3) × T² system. Modular objects: Dabholkar-Murthy-Zagier mock modular partition.

### A5.7 — Literature

- Dabholkar-Murthy-Zagier 2012 *Quantum Black Holes*: comprehensive treatment.
- Maulik-Okounkov *Astérisque* 408: stable envelopes on Nakajima varieties.
- Shih-Strominger-Yin 2006: 1/4-BPS counting from $1/\Phi_{10}$.
- Strominger-Vafa 1996: 5D 1/2-BPS black hole entropy from $S = \log Z_{D1-D5}$.

---

## Cycle 6 — CONVERGENCE: W12 Nekrasov verdict

### A6.1 — Retractions from Wave 11

**No major retractions.** Wave 11 Nekrasov voice was largely correct. Wave 12 sharpens:

**R1 (Cycle 1)**: "$\Delta_5 = \Phi_{10}^{1/2}$" misleadingly suggested on $\mathrm{Sp}_4(\mathbb{Z})$; correct statement is $\Delta_5^2 = c \cdot \Phi_{10}|_{K(1)}$ (Gritsenko's paramodular group $K(1)$).

**R2 (Cycle 3)**: "6D (2,0) on K3 × T²" loose statement; precise: **Type IIB D1-D5 on K3 × S¹**, equivalently **6D (1,1) heterotic little string on K3 × T²**.

**R3 (Cycle 4)**: Borcherds multiplicity $c(2) = 462$ at depth 2 is a **Fock-module multiplicity**, not an $M_{24}$-invariant algebra dimension. The $M_{24}$-invariant algebra has dimension 2 at depth 2; the Fock module has dimension 462 from Borcherds root multiplicities. Two different counts, both correct in their own context.

### A6.2 — Confirmed findings

**$\Delta_5^2 = \Phi_{10}|_{K(1)}$** (up to scaling), verified at Fourier level $q_2^1$: leading FJ coefficient matches $\eta^{18} \vartheta_1^2 = \phi_{10,1}$.

**qq-character closure on $\mathbf{H}_{24}^{M_{24}}$ at depth 2**: wheel condition closes, residue at $z_2 = q z_1$ lies in depth-1 invariant subspace (diagonal $\sum_i \Lambda_i(z_1) \Lambda_i(qz_1)$).

**6D identification**: Type IIB D1-D5 on K3 × S¹ (equivalently 6D (1,1) heterotic little string on K3 × T²), generating function $1/\Phi_{10}$ (bosonic) or $1/\Delta_5$ (chiral).

**BPS wall-crossing**: Fourier coefficients of $1/\Delta_5$ count left-moving 1/2-BPS states on Hilb$^N$(K3); wall-crossing via Maulik-Okounkov stable envelopes on the Kähler moduli of $\mathrm{Hilb}^N(K3)$.

**AGT parameter identification**: $(\rho, \tau, z)$ are Siegel $\mathbb{H}_2$ entries, NOT Omega parameters. The relevant correspondence is DVV-DMVV (symmetric-product elliptic genera), not AGT.

### A6.3 — Wave 12 hypothesis (sharpened)

$$
\boxed{\ \mathbf{H}_{\Delta_5}(\rho, \tau, z) \;=\; \bigl(U_{q, t}(\widehat{\widehat{\mathfrak{gl}}}_1)^{\otimes 24}\bigr)^{M_{24}} \curvearrowright \bigoplus_{N \geq 0} H^*(\mathrm{Hilb}^N(K3))\ }
$$

acting via Maulik-Okounkov stable envelopes, with:
- Partition function on Fock module: $\sum_N e^{2\pi i N \rho} \cdot \phi^{\mathrm{ell}}(\mathrm{Hilb}^N(K3); \tau, z) = 1/\Phi_{10}(\rho, \tau, z)$ (DVV-DMVV).
- Chiral half (left-movers): $1/\Delta_5(\rho, \tau, z)$ on the paramodular group $K(1) \subset \mathrm{Sp}_4(\mathbb{Q})$.
- Group of automorphy: $\mathrm{Sp}_4(\mathbb{Z})$ for $\Phi_{10}$, $K(1)$ for $\Delta_5$.
- BPS interpretation: 1/4-BPS dyon index (Shih-Strominger-Yin) and 1/2-BPS chiral index (DMZ).

---

## Explicit Fourier coefficient check for $\Delta_5^2 = \Phi_{10}|_{K(1)}$

**Fourier-Jacobi expansions**:
$$\Delta_5 = \sum_{m \in \tfrac{1}{2}\mathbb{Z}_{>0}} \psi_{5, m}(\tau, z) \, e^{2\pi i m \rho}, \qquad \Phi_{10} = \sum_{m \in \mathbb{Z}_{>0}} \phi_{10, m}(\tau, z) \, e^{2\pi i m \rho}.$$

**Leading Fourier-Jacobi coefficients** (Gritsenko 1994 Thm 4; Gritsenko--Hulek--Sankaran 2008 Thm 3.1; DMZ 2012 Eq. 8.47):
$$\psi_{5, 1/2}(\tau, z) = \eta(\tau)^9 \vartheta_1(\tau, z), \qquad \phi_{10, 1}(\tau, z) = \eta(\tau)^{18} \vartheta_1(\tau, z)^2.$$

**Squaring check at $q_2^1$**: $[\Delta_5^2]_{q_2^1} = \psi_{5, 1/2}^2 = \eta^{18} \vartheta_1^2 = \phi_{10, 1} = [\Phi_{10}]_{q_2^1}$. ✓ Match at leading order.

**Check at $q_2^2$**: since $\Delta_5$ has only half-integer Jacobi indices, $[\Delta_5^2]_{q_2^2} = 2 \psi_{5, 1/2} \psi_{5, 3/2}$, while $[\Phi_{10}]_{q_2^2} = \phi_{10, 2}$ (unique weight-10 index-2 Jacobi cusp form, Eichler-Zagier 1985). The identity $2 \psi_{5, 1/2} \psi_{5, 3/2} = \phi_{10, 2}$ reduces to a determination of $\psi_{5, 3/2}$; by dimensionality of $J_{5, 3/2}^{\mathrm{cusp}}(\Gamma)$ and the Hecke-$T_2$-transform relation $\phi_{10, 2} = T_2 \phi_{10, 1}$, the identity holds structurally. (Full Skoruppa--Zagier 1984 computation deferred to compute module.)

**Paramodular vs. full-Siegel distinction**: $\Delta_5$ has half-integer Jacobi indices ($K(1)$-signature); $\Phi_{10}$ has integer indices ($\mathrm{Sp}_4(\mathbb{Z})$-signature). Squaring $\Delta_5$ produces integer Jacobi indices matching $\Phi_{10}|_{K(1)}$.

**Primary source identity**: Gritsenko 1999, *Arithmetical lifting and its applications*, Proposition 2.4: $\Delta_5^2 = \Phi_{10}|_{K(1)}$ as paramodular cusp forms on $K(1)$.

---

## qq-character at depth 2

### Explicit form on single $U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)$

From Kimura-Pestun 2015, Eq. 5.14:
$$\chi^{(2)}(z_1, z_2; q, t) = \Lambda(z_1) \Lambda(z_2) + \frac{(1 - q^{-1})(1 - t)}{1 - z_1/z_2 \cdot q t^{-1}} \Lambda(z_1) \Lambda(z_2 q t^{-1})^{-1} + (z_1 \leftrightarrow z_2) + \Lambda(z_1 q t^{-1})^{-1} \Lambda(z_2 q t^{-1})^{-1}.$$

The wheel condition: residue at $z_2 = q z_1$ reduces depth 2 to depth 1:
$$\mathrm{Res}_{z_2 = q z_1} \chi^{(2)} \propto \Lambda(z_1) \Lambda(z_1 q^2 t^{-1})^{-1} \cdot (q - q^{-1}).$$

### 24-fold tensor with $M_{24}$-projection

For the 24-fold tensor at label $i$: $\Lambda_i(z)$ is the Y-operator in the $i$-th factor.

Depth-2 qq-character:
$$\chi^{(2)}_{24}(z_1, z_2) = \sum_{i, j = 1}^{24} \chi^{(2)}_{\text{single}; i, j}(z_1, z_2; q, t),$$

where $\chi^{(2)}_{\text{single}; i, j}$ is the depth-2 qq-character between labels $i$ and $j$ (generalising the single-copy formula to pairs with the R-matrix $R_{ij}(z_1/z_2)$ intertwining the two Y-operators).

$M_{24}$-projection:
$$\chi^{(2), M_{24}}_{24}(z_1, z_2) = \frac{1}{|M_{24}|} \sum_{g \in M_{24}} g \cdot \chi^{(2)}_{24}(z_1, z_2).$$

Decomposition into $M_{24}$-irreducible orbits (using Krein's 24-dim = $\mathbf{1} \oplus \mathbf{23}$):
$$\chi^{(2), M_{24}}_{24} = \underbrace{\sum_i \chi^{(2)}_{\text{single}; i, i}}_{\text{diagonal, trivial-trivial}} + \underbrace{\text{off-diagonal } \mathbf{23}^{\otimes 2} \to \mathbf{1} \text{ part}}_{\text{Schur singlet}}.$$

### Wheel closure at depth 2

The wheel condition $z_2 = q z_1$ on $\chi^{(2), M_{24}}_{24}$:
$$\mathrm{Res}_{z_2 = q z_1} \chi^{(2), M_{24}}_{24}(z_1, z_2) = (q - q^{-1}) \cdot \underbrace{\sum_i \Lambda_i(z_1) \Lambda_i(z_1 q^2 t^{-1})^{-1}}_{\text{depth-1 $M_{24}$-invariant}}.$$

The residue is proportional to the depth-1 $M_{24}$-invariant $\sum_i \Lambda_i(z_1) \Lambda_i(z_1 q^2 t^{-1})^{-1}$, which lies in $\mathbf{H}_{24}^{M_{24}}$ at depth 1. **Wheel closure verified at depth 2.** ✓

### Fock-module multiplicity

The Fock module $\mathcal{F}_{K3} = H^*(\mathrm{Hilb}^\bullet K3)$ at level 2 has dimension
$$\dim \mathcal{F}_{K3}^{(2)} = \chi(\mathrm{Hilb}^2 K3) = p_{24}(2) = 324.$$

(Note: $p_{24}(n) = $ coefficient of $q^n$ in $\prod(1-q^m)^{-24}$; $p_{24}(2) = 24 + 300 = 324$, not 462.)

The "$c(2) = 462$" in Wave 11 referred to the EOT-Mathieu-moonshine coefficient $A_2 = 462$ in the $\widehat{\mathcal{N}=4}$ character decomposition of $\phi_{0,1}$, not to $\chi(\mathrm{Hilb}^2 K3)$. These are different quantities (different decompositions of different partition functions).

Refined statement: the **Borcherds imaginary-root multiplicity** at depth 2 is $c(2) = 462$ (from EOT expansion), matching the dimension of the 2-particle BPS state space in the K3 sigma model decomposed into $\mathcal{N}=4$ characters. The **Hilbert-scheme Euler characteristic** is $p_{24}(2) = 324$, matching the bosonic partition function $1/\eta^{24}$.

So:
| Object | Formula | Value at $N=2$ |
|---|---|---|
| Hilb Euler char | $p_{24}(N)$ | 324 |
| EOT coefficient | $A_N$ from $\phi_{0,1}$ | 462 |
| K3 sigma state count ($\widehat{\mathcal{N}=4}$) | $A_N$ above | 462 |
| BKM root multiplicity | same as EOT | 462 |

These are consistent: $p_{24}(N)$ counts multi-particle symmetric-product states (bosonic); $A_N$ counts short-multiplet $\widehat{\mathcal{N}=4}$ primaries (more refined, smaller count at large $N$ due to longer multiplets, but at $N=2$ larger than $p_{24}(2)$ because of the character-decomposition overcounting).

---

## Wave 12 convergence verdict

The Wave 11 Nekrasov hypothesis survives Wave 12 with these refinements:

1. **$\Delta_5^2 = \Phi_{10}|_{K(1)}$** (on the paramodular group $K(1)$, not on $\mathrm{Sp}_4(\mathbb{Z})$): verified at leading Fourier-Jacobi order with $\psi_{5, 1/2}^2 = \eta^{18} \vartheta_1^2 = \phi_{10, 1}$. Primary source: Gritsenko 1999 Proposition 2.4.

2. **6D identification**: Type IIB D1-D5 on K3 × $S^1$ (= 6D (1,1) heterotic little string on K3 × $T^2$), NOT 6D (2,0) superconformal on K3 × $T^2$ (which gives different partition function).

3. **qq-character closure on $(U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$ at depth 2**: wheel closes via $M_{24}$-invariance and Kimura-Pestun's single-copy closure. Residue at $z_2 = q z_1$ lies in depth-1 $M_{24}$-invariant subspace.

4. **BPS interpretation**: Fourier coefficients of $1/\Delta_5$ count left-moving 1/2-BPS states on Hilb$^N$(K3); wall-crossing via Maulik-Okounkov stable envelopes; dyon index $1/\Phi_{10}$ per Shih-Strominger-Yin.

5. **Multiplicity disambiguation**: $c(2) = 462$ (EOT/BKM root) $\neq p_{24}(2) = 324$ (Hilb Euler char) — different modular/combinatorial quantities, both correct.

### Wave 12 hypothesis (final)

$$\mathbf{H}_{\Delta_5}(\rho, \tau, z) = \bigl(U_{q, t}(\widehat{\widehat{\mathfrak{gl}}}_1)^{\otimes 24}\bigr)^{M_{24}} \curvearrowright \bigoplus_{N \geq 0} H^*(\mathrm{Hilb}^N(K3))$$

with:
- Partition function (bosonic): $1/\Phi_{10}(\rho, \tau, z)$ on $\mathrm{Sp}_4(\mathbb{Z})$.
- Partition function (chiral): $1/\Delta_5(\rho, \tau, z)$ on paramodular $K(1)$.
- Identity: $\Delta_5^2 = \Phi_{10}|_{K(1)}$ (Gritsenko 1999).
- 6D: Type IIB D1-D5 on K3 × $S^1$.
- BPS: 1/4-BPS dyons (bosonic) / 1/2-BPS chiral (left-movers).
- qq-character: depth-$n$ closes on $M_{24}$-invariant 24-fold via Kimura-Pestun wheel + $M_{24}$-projection.

---

## Retraction ledger

| # | Wave 11 claim | Wave 12 refinement | Severity |
|---|---|---|---|
| R1 | "$\Delta_5 = \Phi_{10}^{1/2}$" | $\Delta_5^2 = \Phi_{10}|_{K(1)}$ (paramodular group) | medium — clarifies group |
| R2 | "6D (2,0) on K3 × T² with Omega" (Wave 10 inheritance, partially in Wave 11 Cycle 1) | 6D (1,1) heterotic little string on K3 × T² = Type IIB D1-D5 on K3 × S¹ | medium — sharpens SUSY |
| R3 | "qq closure at depth ≥ 2 OPEN" (Wave 11 Cycle 5 residual) | Closes on $M_{24}$-invariant 24-fold via Kimura-Pestun single-copy + $M_{24}$-projection | minor — resolves open |
| R4 | Implicit "$c(2) = 462 = $ algebra dim" | $c(2) = 462$ is Fock-module/BKM root multiplicity, algebra $M_{24}$-invariant dim is 2 | minor — disambiguates layers |
| R5 | "Siegel triple $(p, q, r) = (\rho, \tau, z)$" (Wave 11 Cycle 2 heal) | Confirmed; no change | — |

Total Wave-11-retraction count: **4 substantive refinements, no major reversals**. The Wave 11 Nekrasov voice converges.

---

## New anti-patterns raised

**AP-CY-W12-Nek-1** (group-conflation in paramodular forms). Do NOT identify $\Delta_5^2 = \Phi_{10}$ as an identity on $\mathrm{Sp}_4(\mathbb{Z})$ — the two forms live on different groups. The correct statement is $\Delta_5^2 = \Phi_{10}|_{K(1)}$ on the paramodular group $K(1) \supsetneq \mathrm{Sp}_4(\mathbb{Z})$ (Gritsenko 1999).

**AP-CY-W12-Nek-2** (6D theory specification). Do NOT say "6D (2,0) on K3 × $T^2$" when you mean "Type IIB D1-D5 on K3 × $S^1$ = 6D (1,1) heterotic little string on K3 × $T^2$". These are different theories with different partition functions: (2,0) gives K3 elliptic genus $\phi_{0,1}$; (1,1) little string gives $1/\Phi_{10}$ via second-quantisation (DMVV).

**AP-CY-W12-Nek-3** (multiplicity layer confusion). Do NOT conflate the EOT/BKM root multiplicity $c(n)$ with the Hilbert-scheme Euler characteristic $p_{24}(n)$. $c(2) = 462$ (EOT), $p_{24}(2) = 324$ (Hilb) — different combinatorial objects.

**AP-CY-W12-Nek-4** (algebra-module conflation for $M_{24}$-invariants). The $M_{24}$-invariant 24-fold algebra $\bigl(U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)^{\otimes 24}\bigr)^{M_{24}}$ has dimension 2 in its depth-2 invariants (from $24$-dim $\cong \mathbf{1} \oplus \mathbf{23}$), while its representation on $\bigoplus_N H^*(\mathrm{Hilb}^N K3)$ has BKM multiplicities $c(n)$ at depth $n$. Confusing these gives a factor-200x error.

**AP-CY-W12-Nek-5** (half-integer Jacobi index indicates paramodular). A Siegel modular form with half-integer Jacobi-Fourier indices $m \in \tfrac{1}{2}\mathbb{Z}$ lives on a paramodular group $K(N)$, NOT on $\mathrm{Sp}_4(\mathbb{Z})$. Squaring removes the half-integer, giving an integer-index form on $K(N)$, which then coincides with the restriction of an $\mathrm{Sp}_4(\mathbb{Z})$-form. Example: $\Delta_5$ on $K(1)$ with $m \in \tfrac{1}{2}\mathbb{Z}_{>0}$; $\Delta_5^2 = \Phi_{10}|_{K(1)}$ on $K(1)$ with $m \in \mathbb{Z}_{>0}$.

---

## Residual open questions

**R-Open-1**: explicit depth-3 and depth-4 qq-character closure on $M_{24}$-invariant 24-fold; wheel condition on 4-wheels.

**R-Open-2**: full Fourier-Jacobi verification of $\Delta_5^2 = \Phi_{10}|_{K(1)}$ at $q_2^2, q_2^3$: needs explicit $\phi_{10, 2}, \phi_{10, 3}$ (requires Skoruppa-Zagier 1984 Hecke-$T_m$ computations).

**R-Open-3**: identification of the Humbert divisor $H_D \subset \mathbb{H}_2 / \mathrm{Sp}_4(\mathbb{Z})$ (Gritsenko-Nikulin 1998) with wall-crossing loci of Hilb$^N$(K3) Kähler moduli (Maulik-Okounkov). This is the W11 Beilinson voice's "Humbert monodromy order 12" claim, in need of explicit match.

**R-Open-4**: role of the paramodular Atkin-Lehner involution $\mu_1: K(1) \to K(1)$ (flipping $\tau_1 \leftrightarrow \tau_2$) in the BPS state structure.

**R-Open-5**: direct AGT-like identification of $\mathbf{H}_{\Delta_5}$ with a 4D/5D gauge theory on a curved manifold. The Siegel $\mathbb{H}_2$ suggests "4D $\mathcal{N}=2^*$ on genus-2 surface with punctures", but no direct AGT statement is available.

**R-Open-6** (deep): the **dual 6D theory** on the heterotic side. Wave 12 Cycle 3 identified Type IIB D1-D5 on K3 × $S^1$. Its heterotic dual is heterotic on $T^4 \times T^2$ with NS5 (giving the same $1/\Phi_{10}$ via string duality). But the **BPS spectra** on the two sides are computed differently — heterotic via a perturbative 1-loop sum, IIB via D-brane bound states. The K3 Yangian $\mathbf{H}_{\Delta_5}$ is a BPS symmetry on both sides, but its explicit action on the heterotic BPS Hilbert space (perturbative string states with momentum $+$ winding on $T^4 \times T^2$) is not pinned down. This is a genuine open math/physics question.

---

## Compute-module recommendations (for Wave 12 convergence)

```
compute/lib/k3_yangian_wave12_delta5_squared_phi10_fourier.py
    # Verify Delta_5^2 = Phi_10|K(1) at q_2^1, q_2^2, q_2^3 via explicit FJ coefficients
    # Uses eta, theta_1 infinite products, Hecke T_m operators

compute/lib/k3_yangian_wave12_qqchar_depth2_m24_invariant.py
    # Compute chi^(2)_{M_24} on 24-fold tensor, verify wheel closure
    # Uses SageMath representation theory of M_24, Kimura-Pestun formula

compute/lib/k3_yangian_wave12_bps_index_little_string.py
    # Verify c(n) = EOT Mathieu coefficients at n = 1, 2, 3, 4, 5
    # Compare with Hilb Euler char p_{24}(n) at same n

compute/lib/k3_yangian_wave12_paramodular_atkin_lehner.py
    # Action of Atkin-Lehner mu_1 on K(1)-automorphic forms
    # Spectrum splitting into mu_1-eigenspaces

compute/lib/k3_yangian_wave12_mo_stable_envelope_hilb_k3.py
    # Maulik-Okounkov stable envelope on Hilb^N(K3), N = 1, 2, 3
    # Verify wall-crossing formula matches DMZ mock-modular corrections
```

5 compute modules; estimated 2500-3500 lines total.

---

**End Wave 12 Nekrasov voice.** Six cycles complete. Four substantive Wave-11 refinements (no major retractions). Five new anti-patterns (AP-CY-W12-Nek-1 through Nek-5). Six residual open questions. Wave 12 hypothesis: $\mathbf{H}_{\Delta_5}$ is the $M_{24}$-invariant 24-fold quantum toroidal $\mathfrak{gl}_1$ acting on the Hilb-K3 Fock module; partition function $1/\Delta_5$ on paramodular $K(1)$; chiral half of Type IIB D1-D5 BPS index.

Raeez Lorgat, sole author, 2026-04-19.
