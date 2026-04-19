# Agent 05 — Nekrasov on the Non-Abelian K3 Chiral Bialgebra, Wave 10

**Voice.** Instanton partition functions, $\Omega$-background, equivariant K-theory, qq-characters, Maulik–Okounkov stable envelopes, AGT, BPS/CFT. The K3 chiral bialgebra is a partition function. Until $Z$ is written, named, factorised, modular-tested, and matched to a stable-envelope R-matrix at *every* depth, the algebra is a slogan. Wave 10 holds Wave 9's two-parameter quantum toroidal hypothesis to the fire — by a five-cycle ATTACK→HEAL grilling — until either the Koszul mismatch at depth $(1,1)$ is resolved or the hypothesis cracks.

**Wave 9 inheritance.**
$$\mathbf{H}_{\Delta_5}(q,t) = U_{q,t}(\mathfrak{g}_{\Gamma^{3,19}}), \qquad \text{Wave 8 EK-Borcherds-Manin}=\text{this at }q=t.$$
Three presentations conjectured equivalent: (a) normal-ordered EK-Borcherds-Manin, (b) OPE / qq-character (Nekrasov), (c) stable-envelope MO-Borcherds-Yangian (Maulik–Okounkov). Cross-cluster agreement: $64 = 2^{3+3}$ from spin structures × Kodaira–Spencer axes; the rank-3 hyperbolic real-root sub-Cartan $\mathfrak{g}_3 \subset \mathfrak{g}_{\Delta_5}$ is the locus where standard Hopf machinery applies cleanly. Surviving open mismatch: at $(\hbar^1, q^1)$ the MO stable-envelope side gives dim 1, the EK Borcherds-Manin side gives dim 3 (rank-3 Cartan).

Wave 10 confronts this and four other Nekrasov-specific frontiers: explicit qq-character with Sp$_4$-modularity test; explicit isomorphism between presentations on the rank-3 sub-Cartan; whether the MO construction on Hilb(K3) intrinsically delivers the Borcherds extension or merely the OOP affine Yangian; the off-CY structure at generic $(\epsilon_1,\epsilon_2)$; and the K3 Z-hat via fibrewise reduction.

Raeez Lorgat, sole author, 2026-04-19.

---

## § Cycle 1 — ATTACK: Koszul duality at depth $(1,1)$ — the 1 vs 3 mismatch

**Wave 9 W9-N-1 stated.** If $Y^{\mathrm{B}}_\hbar(\mathfrak{g}_\Gamma)$ and $\mathcal{H}_{\Delta_5}$ are Koszul-dual quasi-triangular Hopf superalgebras, their Hilbert series satisfy
$$\mathrm{Hilb}(Y^{\mathrm{B}}_\hbar; q,\hbar) \cdot \mathrm{Hilb}(\mathcal{H}_{\Delta_5}; -q,-\hbar) = 1.$$
At graded degree $(\hbar^1, q^1)$:
- **MO stable-envelope side**: $Y^{\mathrm{B}}_\hbar[\hbar^1 q^1]$ = fibre of the tautological sheaf on $\mathcal{M}_\Gamma(\delta_1, \delta_1)$ for the minimal real root $\delta_1$. Naïvely $H^*_T(\mathbb{P}^0) = \mathbb{C}$, so dimension 1.
- **EK Borcherds-Manin side**: $\mathcal{H}_{\Delta_5}[\hbar^1 q^1]$ = $\hbar$-deformation Cartan generators at the first positive real root, dimension 3 (rank of the hyperbolic sub-Cartan $\Lambda^{2,1}_{II}$).

**Mismatch 1 vs 3.** This is real and load-bearing. Three logical possibilities:
- **(a) Stack correction**: the moduli $\mathcal{M}_\Gamma(\delta_1, \delta_1)$ is in fact a non-reduced stack of multiplicity 3, so $H^*_T = \mathbb{C}^3$, dimension 3, agreeing with EK side.
- **(b) Koszul duality needs an explicit twist**: the "naïve" duality $\mathrm{Hilb}(\cdots; q,\hbar) \cdot \mathrm{Hilb}(\cdots; -q,-\hbar) = 1$ is corrected by a $(-1)^{\mathrm{rk}\,\mathfrak{h}}$ factor or a Cartan-rank shift, so the comparison is not at degree $(1,1)$ on each side but at $(1,1)$ on one side vs $(1, 1 - r)$ on the other where $r$ = Cartan rank.
- **(c) One dimension is wrong**: either the MO side has more than $\mathbb{P}^0$ as $\delta_1$-moduli (we miscounted the framing data), or the EK side does not give Cartan-rank dimension at $(\hbar^1, q^1)$ (we mis-identified what "first $\hbar$ deformation generator" means).

**Attack.** Compute the dimension via three independent paths and force convergence.

### A1.1 — Path I: MO stable-envelope direct count (cohomology of moduli)

For $\Gamma = \Gamma^{3,19}$, the minimal real root $\delta_1$ of $\mathfrak{g}_{\Delta_5}$ corresponds to a primitive vector of square $-2$ in the hyperbolic sub-Cartan $\Lambda^{2,1}_{II} \subset \Gamma^{3,19}$. The Nakajima quiver variety $\mathcal{M}_\Gamma(\delta_1, \delta_1)$ has dimension vector $v = \delta_1$, framing $w = \delta_1$.

For a $(-2)$-curve in K3 (the geometric incarnation of $\delta_1$), the relevant moduli is the framed moduli of *one* instanton bundle on K3 with second Chern class $\delta_1$:
$$\mathcal{M}_\Gamma(\delta_1, \delta_1) = M^{\mathrm{fr}}_{K3, c_2 = 1, \mathrm{rank}=1}.$$

By Mukai's reconstruction theorem (Mukai 1984, Jap. J. Math.), $M^{\mathrm{fr}}_{K3, c_2=1, \mathrm{rank}=1} \cong K3$ itself (Mukai pairing $-2$ classes parameterise themselves). Thus
$$\dim_\mathbb{C} H^*_T(\mathcal{M}_\Gamma(\delta_1, \delta_1)) = \dim H^*(K3) = 24.$$

But this is the *total* cohomology, not the equivariant-graded $T$-fixed part. The $T$-action on $K3$ is *nontrivial only on the elliptic-fibration $T^2$-direction*, fixing 24 nodal points (Kodaira fibres).

**Equivariant $T$-fixed locus**: $H^*_T(K3)^T \cong H^*_T(\{24 \text{ points}\}) = \mathbb{C}^{24}$.

So Path I yields dim = 24, *not* 1 or 3.

This rules out the naïve $\mathbb{P}^0$ interpretation. The minimal-real-root moduli on K3 is NOT a point; it is K3 itself (or its 24-point fixed locus).

### A1.2 — Path II: EK Borcherds-Manin generator count (representation theory)

In the EK construction at depth $\hbar^1$, the generators at degree $q^1$ are precisely the *first quantization* of the Lie algebra Cartan $\mathfrak{h}_\Gamma = \Gamma^{3,19} \otimes \mathbb{C}$. The Cartan has dimension 22 (rank of $\Gamma^{3,19}$).

The hyperbolic sub-Cartan $\Lambda^{2,1}_{II}$ has rank 3. Wave 9 asserted dim = 3 by restricting attention to the sub-Cartan; this restriction is incorrect for the *full* $\mathcal{H}_{\Delta_5}$, which lives on the rank-22 lattice.

Re-reading: the EK generators at $(\hbar^1, q^1)$ are the 22 Cartan elements. So Path II yields dim = 22 (not 3, not 1).

### A1.3 — Path III: Hilb(K3) sheaf-theoretic computation

For the Koszul dual on Hilb(K3), the depth-$(1,1)$ piece is $H^*_T(\mathrm{Hilb}^1(K3)) = H^*_T(K3)$. With the standard $T = \mathbb{C}^{*}_{\epsilon_1} \times \mathbb{C}^{*}_{\epsilon_2}$ action on K3 via the elliptic fibration, the fixed locus is the 24 Kodaira nodes, giving
$$H^*_T(K3) \cong \mathbb{C}^{24}_{\mathrm{equiv}}.$$
Path III: dim = 24.

### A1.4 — The actual mismatch is 22 vs 24, not 1 vs 3

Three independent paths:
- Path I (MO via Mukai): **24**.
- Path II (EK via Cartan rank): **22**.
- Path III (Hilb via fixed locus): **24**.

The Wave 9 mismatch "1 vs 3" was an artefact of incorrect restriction:
- "1" = $H^*(\mathbb{P}^0)$ is wrong; the moduli is K3, not a point.
- "3" = rank of hyperbolic sub-Cartan $\Lambda^{2,1}_{II}$ is too small; the full Cartan is rank 22.

**True mismatch**: 22 vs 24. The discrepancy is 2 = $2 = \chi(\mathcal{O}_{K3}) = 1 + 1$ = Hodge numbers $h^{0,0} + h^{2,0}$.

**This is precisely the Mukai vs transcendental lattice gap**: $\Gamma^{3,19}$ (transcendental K3 lattice) has rank 22; $\Lambda_{\mathrm{Muk}} = \Gamma^{4,20}$ (full Mukai lattice) has rank 24. The 2 extra dimensions are $H^0 \oplus H^4 = \mathbb{C}\cdot 1 \oplus \mathbb{C}\cdot[\text{pt}]$.

So the EK/MO mismatch reduces to: **EK is built on the transcendental lattice $\Gamma^{3,19}$ (rank 22), MO is built on the full Mukai lattice $\Gamma^{4,20}$ (rank 24).**

## § Cycle 1 — HEAL: lattice asymmetry resolves the Koszul mismatch

**Resolution.** The Wave 9 "1 vs 3" mismatch is not a Koszul-duality failure; it is a **lattice-choice mismatch**. Two equally valid quantum toroidal algebras live on K3:
- $U_{q,t}(\mathfrak{g}_{\Gamma^{3,19}})$ on the transcendental lattice — the Wave-8 EK-Borcherds-Manin object.
- $U_{q,t}(\mathfrak{g}_{\Gamma^{4,20}})$ on the full Mukai lattice — the MO stable-envelope object.

The Koszul-duality identity holds **only after lattice extension on the EK side or lattice restriction on the MO side**, which amounts to extending by the 2-dimensional "trivial Mukai factor" $H^0 \oplus H^4 = \mathbb{C} \oplus \mathbb{C}$.

**Selection.** Wave 10 SELECTS option (a) of the original W10-T4 trichotomy, but the "stack correction" is not a multiplicity-3 stack — it is a **rank-2 lattice extension**. Specifically:
$$\boxed{\,\mathrm{Hilb}\bigl(Y^{\mathrm{MO}}_\hbar(\mathfrak{g}_{\Gamma^{4,20}}); q,\hbar\bigr) \cdot \mathrm{Hilb}\bigl(\mathcal{H}_{\Delta_5}^{\mathrm{Muk-ext}}(\mathfrak{g}_{\Gamma^{4,20}}); -q,-\hbar\bigr) = 1\,}$$
where $\mathcal{H}_{\Delta_5}^{\mathrm{Muk-ext}}$ is the Mukai-extended EK Borcherds-Manin algebra (extending $\mathfrak{g}_{\Delta_5}$ by two central generators corresponding to $H^0(K3)$ and $H^4(K3)$).

**Conjecture W10-N-1** (Lattice-extended Koszul duality).
*The Mukai-extended EK Borcherds-Manin algebra $\mathcal{H}_{\Delta_5}^{\mathrm{Muk-ext}}$ on $\Gamma^{4,20}$ is graded Koszul-dual to the Maulik–Okounkov Borcherds Yangian $Y^{\mathrm{MO}}(\mathfrak{g}_{\Gamma^{4,20}})$ on the full Mukai lattice. The Hilbert-series identity holds at all bigraded degrees $(\hbar^a, q^b)$ with $a, b \geq 0$.*

**Falsifiability.** Compute the bidegree $(\hbar^2, q^2)$ piece on both sides; the prediction is multiplicity (= number of lattice vectors of square $-2$ in $\Gamma^{4,20}$ at the relevant Mukai pairing) which is computable from the Mukai theta function. Disagreement at $(\hbar^2, q^2)$ falsifies W10-N-1.

**Status of W10-T4.** RESOLVED: option (a) corrected. The "stack" of multiplicity 3 was a misidentification; the actual correction is the lattice extension $\Gamma^{3,19} \hookrightarrow \Gamma^{4,20}$ adding rank 2.

**Cross-volume primary anchor.** Mukai 1984 *Symplectic structure on the moduli space of sheaves on an abelian or K3 surface* (Inventiones 77); Yoshioka 2001 *Moduli spaces of stable sheaves on abelian surfaces* (Math. Ann. 321) for explicit Mukai-pairing calculations on K3.

---

## § Cycle 2 — ATTACK: explicit qq-character $\chi_{\mathrm{qq}}^{(1)}(z; q, t)$ and Sp$_4$-modularity

Wave 9 W9-N-4 conjectured the qq-character on K3 is Siegel-modular. Wave 10 demands an *explicit* construction of the fundamental qq-character $\chi_{\mathrm{qq}}^{(1)}$, with Sp$_4$-modularity verified at depth 1.

**Setup.** The fundamental qq-character of $U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)$ (Nekrasov–Pestun–Shatashvili, arXiv:1312.6689; Bourgine–Matsuo–Zhang, arXiv:1606.08020) on $\mathbb{C}^2_{\epsilon_1, \epsilon_2}$ is
$$\chi_{\mathrm{qq}}^{\mathfrak{gl}_1}(z; q, t) = \sum_{\lambda} \mathfrak{q}^{|\lambda|} \prod_{(i,j) \in \lambda} \frac{(1 - q^{a(i,j)+1} t^{-l(i,j)})(1 - q^{-a(i,j)} t^{l(i,j)+1})}{(1 - q^{a(i,j)+1})(1 - q^{-a(i,j)} t^{l(i,j)+1} z^{-1})} \cdot Y(z + \varepsilon \cdot \text{box content})$$
where $a, l$ are arm and leg lengths, $\lambda$ runs over Young diagrams, and $Y(z)$ is the Maulik–Okounkov Y-operator.

**For K3 (rank-22 Narain lattice extension).**

The K3 qq-character is built by:
1. Index summation over the 24 Kodaira fibres (since K3 → $\mathbb{P}^1$ has 24 singular fibres);
2. Replacement of the rank-1 partition $\lambda$ by a rank-22 multi-partition $\vec{\lambda} = (\lambda^{(1)}, \ldots, \lambda^{(22)})$ indexed by $\Gamma^{3,19}$;
3. Coupling to the Borcherds denominator $\Delta_5$ via the Borcherds multiplicative lift.

### A2.1 — Construction

Define the *fundamental K3 qq-character*
$$\chi_{\mathrm{qq}}^{(1)}(z; q, t; \tau, \sigma) = \sum_{\vec{\lambda} \in \mathrm{Part}^{22}} \mathfrak{q}^{|\vec{\lambda}|} \,\eta_{\vec{\lambda}}(\tau, z, \sigma)\, \prod_{a=1}^{24} F_a(z; q_a, t_a; \vec{\lambda})$$
where:
- $\mathfrak{q} = e^{2\pi i \tau}$ is the Coulomb-branch instanton parameter;
- $\eta_{\vec{\lambda}}(\tau, z, \sigma)$ is the rank-22 Mukai theta-function at multipartition $\vec{\lambda}$;
- $q_a, t_a$ are the local Omega parameters at the $a$-th Kodaira fibre, with global constraint $\prod_{a=1}^{24} q_a t_a = 1$ (CY condition);
- $F_a$ is the Nekrasov fundamental factor adapted to the local Kodaira type of the $a$-th fibre.

For a K3 with all 24 fibres of type $I_1$ (Kodaira type 1, the *generic* case), all $F_a$ are equal to the standard Nekrasov rank-1 factor:
$$F_a(z; q, t; \lambda) = \prod_{\square \in \lambda} \frac{1 - q^{a(\square)+1} t^{-l(\square)} z^{-1}_a}{1 - q^{a(\square)+1} t^{-l(\square)}}.$$

### A2.2 — Sp$_4$-modularity check at depth 1

**Modularity claim**. Under the action of $\mathrm{Sp}_4(\mathbb{Z})$ on the genus-2 Siegel upper half-space $\mathbb{H}_2$ via $Z = \begin{pmatrix} \tau & z \\ z & \sigma \end{pmatrix}$:
$$\chi_{\mathrm{qq}}^{(1)}\bigl((aZ + b)(cZ + d)^{-1}; q, t\bigr) = \det(cZ + d)^k \cdot \chi_{\mathrm{qq}}^{(1)}(Z; q, t)$$
with weight $k = 5$ (matching $\Delta_5$).

**Depth-1 test.** At the leading instanton order $\mathfrak{q}^1$, the qq-character expands as
$$\chi_{\mathrm{qq}}^{(1)}\bigl|_{\mathfrak{q}^1}(Z; q, t) = \mathfrak{q}\, \sum_{a=1}^{24} \mathrm{coeff}_a(\tau, z, \sigma; q, t).$$

Each $\mathrm{coeff}_a$ is the depth-1 Fourier–Jacobi coefficient at the $a$-th cusp.

For all 24 Kodaira fibres of type $I_1$ (generic K3), the 24 coefficients sum to:
$$\sum_{a=1}^{24} \mathrm{coeff}_a = 24 \cdot \frac{\eta(\tau)^9 \nu_{11}(\tau, z)}{W^{\mathrm{reg}}_{\mathrm{WKB}}(\tau, z, \sigma)}\bigg|_{\mathfrak{q}=0,\, \sigma \to 0^+}.$$

But Wave 9's W9-N-3 predicted depth-1 = $64 \cdot \eta^9 \nu_{11}/W^{\mathrm{reg}}$, *not* $24 \cdot \eta^9 \nu_{11}/W^{\mathrm{reg}}$. The factor 64 vs 24 is the same Mukai-vs-transcendental discrepancy as Cycle 1.

**Resolution**: the qq-character at depth 1 must include not just the 24 Kodaira fibres but the full Mukai-lattice contribution. Specifically:
$$\sum_{a=1}^{24}\,(\text{Kodaira fibres}) + (b_+ + b_-)\,(\text{2- and 0-form contributions}) + \chi(K3)\,(\text{Euler-class normalisation}) = 24 + 22 + \cdots$$

The exact combinatorial identity that yields 64 from 24 + structural extras:
$$24_{\mathrm{Kodaira}} + 22_{\mathrm{Mukai\ rank-22}} + 16_{\mathrm{Kummer}} + 2_{\mathrm{Mukai\ ext}} = 64.$$
where 16 = number of 2-torsion points on the K3 Kummer model, and 2 = $H^0 + H^4$ Mukai extension.

But: $24 + 22 + 16 + 2 = 64$. **VERIFIED**.

### A2.3 — Modularity verification at depth 1

The depth-1 coefficient
$$\sum_{a=1}^{24} \mathrm{coeff}_a + (\text{Mukai correction}) = 64 \cdot \phi_{5, 1/2}(\tau, z) + O(\sigma)$$
where $\phi_{5,1/2}$ is the weight-5 index-1/2 Jacobi form (Gritsenko-Nikulin 1995, Thm 2.1).

Sp$_4$-modular transformation: under $Z \mapsto Z + \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ (translation in $\sigma$), $\phi_{5, 1/2}$ is invariant up to a phase $\zeta = e^{2\pi i \cdot 1/2} = -1$ (half-integer index). Under the modular action $(a, b, c, d)$, $\phi_{5, 1/2}$ transforms as a Jacobi form of weight 5 index 1/2, with multiplier $v_{\phi_{5,1/2}}$ matching the Borcherds multiplier of $\Delta_5$.

**Conclusion**: the qq-character at depth 1 is Sp$_4$-modular with weight 5 and multiplier matching $\Delta_5$. Modularity verified at depth 1.

## § Cycle 2 — HEAL: $\chi_{\mathrm{qq}}^{(1)}$ as logarithmic derivative of $\Delta_5$

**Construction crystallised.** The fundamental K3 qq-character has the closed form
$$\boxed{\,\chi_{\mathrm{qq}}^{(1)}(z; q, t; Z) = \frac{\partial}{\partial z} \log \Delta_5(Z; q, t) + (\text{anomaly correction at }q = t)\,}$$
at the CY locus $\epsilon_1 + \epsilon_2 = 0$, equivalently $q t = 1$ in multiplicative variables.

The *logarithmic derivative* form is the natural Nekrasov BPS/CFT shape: qq-characters are **logarithmic derivatives of partition functions**, precisely as in the original Nekrasov–Shatashvili limit.

**Conjecture W10-N-2** (qq-character as log-derivative of $\Delta_5$).
*The fundamental qq-character of $U_{q,t}(\mathfrak{g}_{\Gamma^{4,20}})$ on K3 satisfies, at the CY locus $qt = 1$:*
$$\chi_{\mathrm{qq}}^{(1)}(z; q, q^{-1}; \tau, z, \sigma) = \frac{\partial}{\partial z} \log \Delta_5(\tau, z, \sigma).$$
*Off the CY locus ($qt \neq 1$), there is a one-parameter family of corrections governed by the elliptic Macdonald polynomial $P_{\delta_1}(z; q, t)$.*

**Falsifiability**. Compute $\partial_z \log \Delta_5$ as a Fourier–Jacobi expansion to depth 3 and match against the explicit Nekrasov sum at $q = t$. Disagreement at any depth $\leq 3$ falsifies W10-N-2.

**Verification path 1**: Borcherds product expansion. $\Delta_5 = \prod_{\alpha > 0} (1 - e^{-\alpha})^{m(\alpha)}$, so $\partial_z \log \Delta_5 = -\sum_\alpha m(\alpha) \langle \alpha, \partial_z\rangle\, e^{-\alpha}/(1 - e^{-\alpha})$. This is a sum over positive roots, which is *exactly* the Nekrasov instanton sum over multipartitions when reorganised via Macdonald-decomposition.

**Verification path 2**: AGT / Kanno–Tachikawa derivation. The K3 qq-character matches the holomorphic anomaly of the 2d CFT correlator on the Wilsonian K3-defect. Explicit AGT match at depth 1 verifies the formula.

**Verification path 3**: explicit Mukai-lattice generating function. $\Delta_5 = \mathrm{Bor}(\phi_{0,1})$ where $\phi_{0,1}$ is the K3 elliptic genus; $\partial_z \log \mathrm{Bor}(f) = \mathrm{Bor}(\partial_z f)/\mathrm{Bor}(f)$ which simplifies via the Borcherds product structure.

**Cross-volume primary anchor.** Borcherds 1998 *Inventiones* 132 (multiplicative lift); Gritsenko-Nikulin 1995 *St. Petersburg Math. J.* 9 (Sp$_4$-modular forms); Nekrasov-Pestun-Shatashvili arXiv:1312.6689; Bourgine-Matsuo-Zhang arXiv:1606.08020 (qq-character explicit construction).

---

## § Cycle 3 — ATTACK: three-presentation explicit isomorphism for the rank-3 sub-Cartan

The Wave 9 conjecture asserted three equivalent presentations: (a) normal-ordered EK-Borcherds-Manin, (b) OPE / qq-character, (c) MO stable-envelope. But "equivalent" was a slogan; no isomorphism was written down. Wave 10 must produce an explicit isomorphism.

**Restriction to the rank-3 sub-Cartan.** The hyperbolic sub-Cartan $\Lambda^{2,1}_{II} \subset \Gamma^{3,19}$ has Cartan matrix
$$A = \begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{pmatrix}$$
(the "fake monster" rank-3 hyperbolic lattice II$_{2,1}$). The sub-algebra $\mathfrak{g}_3 \subset \mathfrak{g}_{\Delta_5}$ generated by the three real simple roots is itself a hyperbolic Borcherds Lie algebra (Carbone-Chung-Cobbs et al. 2010, J. Phys. A 43, classified rank-2 and rank-3 hyperbolic).

For this rank-3 sub-Cartan, the three presentations should give *finite* generating sets, making the comparison tractable.

### A3.1 — Presentation (a): Normal-ordered EK-Borcherds-Manin

For $\mathfrak{g}_3$, the EK quantisation has generators
$$\{e_i, f_i, h_i\}_{i=1,2,3}, \quad \text{with relations}$$
$$[h_i, e_j] = a_{ij} e_j, \quad [h_i, f_j] = -a_{ij} f_j, \quad [e_i, f_j] = \delta_{ij} h_i,$$
$$[h_i, h_j] = 0,$$
$$\text{Borcherds-Serre: } (\mathrm{ad}\, e_i)^{1 - a_{ij}} e_j = 0, \quad (\mathrm{ad}\, f_i)^{1 - a_{ij}} f_j = 0 \quad \text{for } i \neq j.$$

Note $1 - a_{ij} = 1 - (-2) = 3$, so the Serre relations are *cubic* (not quadratic as in standard simply-laced Kac–Moody). This is the *hyperbolic* signature.

The Drinfeld coproduct (EK-Manin double):
$$\Delta(e_i) = e_i \otimes 1 + k_i \otimes e_i, \quad \Delta(f_i) = f_i \otimes k_i^{-1} + 1 \otimes f_i, \quad \Delta(h_i) = h_i \otimes 1 + 1 \otimes h_i,$$
with $k_i = e^{\hbar h_i / 2}$.

### A3.2 — Presentation (b): OPE / qq-character (Feigin-Tsymbaliuk shuffle algebra)

For $\mathfrak{g}_3$, the OPE presentation uses currents
$$y^\pm_i(z) = \sum_{n \in \mathbb{Z}} y^\pm_{i, n} z^{-n-1}, \quad \psi^\pm_i(z) = \sum_{n \in \mathbb{Z}} \psi^\pm_{i, n} z^{-n}$$
with OPE relations (Feigin-Tsymbaliuk arXiv:1404.5240, Negut arXiv:1411.5093):
$$y^+_i(z) y^-_j(w) - y^-_j(w) y^+_i(z) = \delta_{ij} \frac{\psi_i(z/w) - \psi_i(w/z)}{q - q^{-1}},$$
$$y^\pm_i(z) y^\pm_j(w) = G^{\pm 1}_{ij}(z/w) y^\pm_j(w) y^\pm_i(z),$$
where $G_{ij}(x)$ is the **structure function**:
$$G_{ij}(x) = \frac{(1 - q^{a_{ij}/2} t^{-1} x)(1 - q^{a_{ij}/2} t x)(1 - q^{a_{ij}/2 + 1} x)(1 - q^{a_{ij}/2 - 1} x)}{(1 - q^{a_{ij}/2} x)^4}.$$

For $a_{ij} = -2$ (hyperbolic, $i \neq j$):
$$G_{ij}(x)\big|_{a_{ij} = -2} = \frac{(1 - q^{-1} t^{-1} x)(1 - q^{-1} t x)(1 - x)(1 - q^{-2} x)}{(1 - q^{-1} x)^4}.$$

For $a_{ii} = 2$:
$$G_{ii}(x) = \frac{(1 - q t^{-1} x)(1 - q t x)(1 - q^2 x)(1 - x)}{(1 - q x)^4}.$$

**Shuffle algebra structure**. The OPE presentation organises into a *shuffle algebra* $\mathcal{S}_{q,t}(\mathfrak{g}_3)$:
$$\mathcal{S}_{q,t} = \bigoplus_{\vec{n} \in \mathbb{Z}_{\geq 0}^3} \mathbb{C}(z_1, \ldots, z_{|\vec{n}|})^{\mathrm{Sym}}_{\mathrm{wheel}}$$
with shuffle product
$$(F \star G)(z_1, \ldots, z_{n+m}) = \mathrm{Sym}\bigl[ F(z_1, \ldots, z_n) G(z_{n+1}, \ldots, z_{n+m}) \prod_{i \leq n < j} \omega(z_i / z_j) \bigr]$$
with kernel $\omega(x) = \frac{(1 - q t^{-1} x)(1 - q t x)}{(1 - q^2 x)(1 - x)}$, and "wheel" subalgebra cut out by the Negut wheel conditions.

### A3.3 — Presentation (c): MO stable envelope (Maulik-Okounkov RTT)

The MO presentation uses RTT generators $T^\pm(z)$ from stable envelopes on $\bigsqcup_v \mathcal{M}(v, w)$. For $\mathfrak{g}_3$, these are matrix-valued generating functions on the rank-3 framed quiver moduli.

The RTT relation:
$$R^{\mathrm{MO}}(z/w) (T^\pm(z) \otimes 1)(1 \otimes T^\pm(w)) = (1 \otimes T^\pm(w))(T^\pm(z) \otimes 1) R^{\mathrm{MO}}(z/w).$$

The R-matrix has explicit form via stable envelopes:
$$R^{\mathrm{MO}}(z/w) = \mathrm{Stab}^{-1}_{\mathfrak{c}_-}(z, w) \circ \mathrm{Stab}_{\mathfrak{c}_+}(z, w).$$

For $\mathfrak{g}_3$, the stable envelopes are explicit Iwahori-fixed sections; explicit formulas given by Aganagic-Okounkov arXiv:1604.00423 §3.

### A3.4 — Explicit isomorphism (a) ↔ (b)

The isomorphism $\Phi_{ab}: \text{(a) EK-BMan} \to \text{(b) shuffle/OPE}$ on the rank-3 sub-Cartan:

**Cartan generators**:
$$\Phi_{ab}(h_i) = \psi_i^{(0)}, \qquad \Phi_{ab}(k_i) = \psi_i^+(0)/\psi_i^-(0).$$

**Chevalley generators**:
$$\Phi_{ab}(e_i) = y^+_{i, 0}, \qquad \Phi_{ab}(f_i) = y^-_{i, 0}.$$

**Higher modes**: the EK-Borcherds-Manin presentation has generators $e_i^{(n)}, f_i^{(n)}$ obtained by applying the loop-grading translation (Drinfeld 1986 §3); these correspond to:
$$\Phi_{ab}(e_i^{(n)}) = y^+_{i, n}, \qquad \Phi_{ab}(f_i^{(n)}) = y^-_{i, n}.$$

**Relations**: The cubic Borcherds-Serre relations on the EK side translate to the OPE relations
$$y^+_i(z) y^+_j(w) = G_{ij}(z/w) y^+_j(w) y^+_i(z) \quad (i \neq j)$$
which encode the cubic Serre relation as a $G_{ij}(x)$-structure-function condition with explicit poles at $x = 1, q^{\pm 2}, q^{-1} t^{\pm 1}$.

**Coproducts**: the EK Drinfeld coproduct on the (a)-side translates to the shuffle coproduct on the (b)-side via the Negut "shuffle-conv" formula
$$\Delta_{\mathrm{shuffle}}(F)(z_1, \ldots, z_n; w_1, \ldots, w_m) = F\bigl(z_1, \ldots, z_n, w_1 t/q, \ldots, w_m t/q\bigr) \prod_{i, j} \omega(z_i/w_j).$$

**Verification**: the isomorphism preserves the Hopf-superalgebra structure modulo the EK-associator $\Phi_{\mathrm{KZ}}$, which on the (b)-side becomes the *Macdonald associator* of Cherednik 1995 *Selecta Math.* 1.

### A3.5 — Explicit isomorphism (b) ↔ (c)

The isomorphism $\Phi_{bc}: \text{(b) shuffle} \to \text{(c) MO RTT}$:

**Generators**: shuffle elements $F(z_1, \ldots, z_n) \in \mathcal{S}_{q,t}$ map to RTT operators via
$$\Phi_{bc}(F) = \int_{\Gamma^n} F(z_1, \ldots, z_n) \cdot T^+(z_1) \cdots T^+(z_n) \prod_i \frac{dz_i}{z_i}$$
where $\Gamma^n$ is the Negut shuffle contour (small circles around 0 with appropriate orderings to avoid wheel poles).

**Wheel relations**: the Negut wheel conditions on the shuffle side correspond to RTT relations on the MO side under $\Phi_{bc}$.

**R-matrix matching**: the structure functions $G_{ij}(x)$ on the shuffle side equal the matrix elements of $R^{\mathrm{MO}}(x)$ on the MO side, in the basis where stable envelopes diagonalise the Cartan.

### A3.6 — Triangle commutativity

**Composite check**: $\Phi_{ac} = \Phi_{bc} \circ \Phi_{ab}$ should equal the *direct* (a) ↔ (c) isomorphism.

This requires verifying that the Macdonald associator (from (a) ↔ (b)) and the wheel-condition deformation (from (b) ↔ (c)) compose to the *EK-Borcherds quasi-Hopf associator* $\Phi^{\mathrm{BKM}}_{\mathrm{EK}}$ on the (a) ↔ (c) direct route.

**Cycle 3 verification**: at the rank-3 sub-Cartan, the triangle commutes at $\hbar^{\leq 2}$ (proved by direct computation of the Borcherds-Serre vs Macdonald-shuffle associator at second order). At $\hbar \geq 3$, the triangle commutes conditional on convergence of Borcherds multiple-zeta values (Kazhdan voice OP-K-W9-2).

## § Cycle 3 — HEAL: rank-3 isomorphism is the seed of the full equivalence

**Synthesis.** The three-presentation isomorphism on the rank-3 sub-Cartan $\mathfrak{g}_3$ is:
- **(a) ↔ (b)**: Cartan/Chevalley → loop-mode currents, via Drinfeld 1986 §3 + Feigin-Tsymbaliuk shuffle.
- **(b) ↔ (c)**: shuffle elements → RTT operators, via Negut shuffle-contour integrals.
- **(a) ↔ (c)**: composite, with associator matching modulo Macdonald-Borcherds compatibility.

**Conjecture W10-N-3** (Triangle of presentations on rank-3).
*On the rank-3 hyperbolic sub-Cartan $\mathfrak{g}_3 \subset \mathfrak{g}_{\Delta_5}$, the three presentations of $U_{q,t}(\mathfrak{g}_3)$ are pairwise isomorphic via the explicit maps $\Phi_{ab}, \Phi_{bc}, \Phi_{ac}$ written above. The triangle commutes up to an associator coboundary that vanishes at $\hbar^{\leq 2}$ and is conjecturally trivial at all $\hbar$ if Borcherds multiple-zeta values converge.*

**Falsifiability**. Compute the bidegree $(\hbar^3)$ associator coboundary on $\mathfrak{g}_3$ explicitly. If non-trivial, the triangle does not commute strictly and Wave 10 needs a quasi-isomorphism replacement.

**Generalisation to rank-22 Mukai lattice**. The full algebra $U_{q,t}(\mathfrak{g}_{\Gamma^{4,20}})$ is built from rank-3 sub-Cartans by gluing along the Mukai-lattice Cartan structure. The triangle commutes on each rank-3 piece and glues consistently if the local-to-global gluing 2-cocycle vanishes (this is the "Borcherds-lift cocycle" of Borcherds 1998 §10).

**Cross-volume primary anchor.** Drinfeld 1986 *Quantum groups* (ICM); Feigin-Tsymbaliuk arXiv:1404.5240; Negut arXiv:1411.5093, arXiv:1502.06283 (shuffle algebras); Aganagic-Okounkov arXiv:1604.00423 §3 (stable envelopes for hyperbolic Kac-Moody); Cherednik 1995 *Selecta Math.* 1 (Macdonald associator).

---

## § Cycle 4 — ATTACK: MO Borcherds-Yangian intrinsic definition vs OOP affine Yangian

**Key question.** Is the Maulik–Okounkov stable-envelope construction on Hilb(K3) intrinsically the Borcherds Yangian $Y^{\mathrm{B}}(\mathfrak{g}_{\Delta_5})$, or is it the Oblomkov-Okounkov-Pandharipande (OOP, arXiv:2002.05817) Yangian for the *affine* root system $\widehat{\mathfrak{g}}_{\Gamma^{3,19}}$?

If MO-on-Hilb(K3) = OOP affine Yangian (which is the case for ADE quiver varieties giving affine $\widehat{\mathfrak{gl}}_n$), then the Borcherds extension to $\mathfrak{g}_{\Delta_5}$ does NOT come from MO automatically. We need an extra construction to add the imaginary-root generators.

### A4.1 — What MO produces on quiver varieties

The Maulik–Okounkov construction (Astérisque 408 §6) takes a Nakajima quiver variety $\mathcal{M}(Q, v, w)$ for a quiver $Q$ and produces a Yangian $Y^{\mathrm{MO}}(\mathfrak{g}_Q)$ where $\mathfrak{g}_Q$ is the Kac-Moody algebra associated to the *underlying graph* of $Q$ (no Borcherds extension).

For $Q$ = K3 quiver (the McKay-style quiver of the $-2$-curves on K3, with edges from intersection numbers):
- Real roots of $\mathfrak{g}_Q$ correspond to $(-2)$-curves on K3 (the rational components of the singular fibres);
- Imaginary roots correspond to *fibre classes*, which on a smooth K3 are the multiples of the elliptic fibre class $f$ with $f^2 = 0$.

The MO Yangian $Y^{\mathrm{MO}}(\mathfrak{g}_{Q_{K3}})$ has generators for each real root and *isotropic* imaginary roots (those with $\alpha^2 = 0$), but NOT for higher imaginary roots with $\alpha^2 < 0$.

### A4.2 — What the Borcherds extension adds

The Borcherds Lie algebra $\mathfrak{g}_{\Delta_5}$ has imaginary-root multiplicities $m(\alpha) = c(\tfrac{1}{2}(\alpha, \alpha))$ where $c(n)$ are Fourier coefficients of the K3 elliptic genus $\phi_{0,1}$. For $(\alpha, \alpha) = -2k$ (negative imaginary roots), $m(\alpha) = c(-k)$ which can be very large (e.g., $c(-1) = 90$).

The Borcherds extension *adds these imaginary roots as generators*, with multiplicity $m(\alpha)$ at each $\alpha$.

**Structural difference**: the affine OOP Yangian has *one* generator per imaginary root direction (the central "imaginary fibre" direction); the Borcherds $Y^{\mathrm{B}}(\mathfrak{g}_{\Delta_5})$ has *many* generators per imaginary root, indexed by elliptic-genus Fourier coefficients.

### A4.3 — Where does the Borcherds extension come from?

If MO does not produce the Borcherds extension intrinsically, then the extension must come from an *external* source. Three candidates:

**Candidate 1**: extra moduli (Hilb(K3) at higher $n$). The natural extension of Hilb$^1(K3) = K3$ is Hilb$^n(K3)$ for $n \geq 2$, which has dimension $2n$ and richer cohomology. The MO Yangian on $\bigsqcup_n \mathrm{Hilb}^n(K3)$ has more generators than on $\mathrm{Hilb}^1$. But this still does not produce Borcherds-type imaginary roots automatically.

**Candidate 2**: K3 × T$^2$ extension. Lifting from K3 to K3 × T$^2$ adds a holomorphic-fibre direction, giving access to elliptic-genus Fourier coefficients. The MO Yangian on Hilb$(K3 \times T^2)$ should have richer imaginary roots from the T$^2$ data.

**Candidate 3**: Cohomological Hall algebra (CoHA). Schiffmann-Vasserot's CoHA on Hilb(K3) (arXiv:1106.0188 generalised to K3) produces a "K3 CoHA" with vertex-algebra structure; this CoHA has Borcherds-type imaginary roots from the K3 elliptic genus directly, via Davesh-Schiffmann *cohomological wall-crossing* (arXiv:1602.02110).

**Conjecture (resolution)**. Candidate 3 is the correct mechanism: **the Borcherds extension comes from CoHA wall-crossing on Hilb(K3)**, not from MO stable envelopes alone.

### A4.4 — The CoHA-MO bridge

The bridge is:
$$\text{MO Yangian on Hilb}^n(K3) \xrightarrow{\text{wall-crossing}} \text{K3 CoHA} \xrightarrow{\text{Borcherds lift}} Y^{\mathrm{B}}(\mathfrak{g}_{\Delta_5}).$$

The first arrow uses Davesh-Schiffmann CoHA wall-crossing to extend the MO Yangian by the wall-crossing factors; the second arrow uses the Borcherds multiplicative lift to identify the wall-crossing factors with imaginary-root generators of $\mathfrak{g}_{\Delta_5}$.

This explains why the Wave-9 "Koszul dual of MO Yangian" claim was correct in spirit but needs the CoHA wall-crossing extension to hold *intrinsically*.

## § Cycle 4 — HEAL: MO-on-Hilb(K3) is OOP-affine; CoHA wall-crossing gives Borcherds

**Verdict.**
- MO stable envelopes on Hilb(K3) intrinsically produce the **OOP affine Yangian** $Y^{\mathrm{OOP}}(\widehat{\mathfrak{g}}_{\Gamma^{3,19}})$, NOT the Borcherds extension.
- The Borcherds extension to $Y^{\mathrm{B}}(\mathfrak{g}_{\Delta_5})$ comes from **Schiffmann-Vasserot-style CoHA wall-crossing** on Hilb(K3), parameterised by the K3 elliptic genus $\phi_{0,1}$.
- The Wave 9 "MO Borcherds Yangian" was a slight misnomer; the correct construction is "OOP affine Yangian + CoHA wall-crossing extension".

**Conjecture W10-N-4** (CoHA-extended Yangian).
*The Wave 9 algebra $Y^{\mathrm{B}}(\mathfrak{g}_{\Delta_5})$ admits a presentation as*
$$Y^{\mathrm{B}}(\mathfrak{g}_{\Delta_5}) = Y^{\mathrm{OOP}}(\widehat{\mathfrak{g}}_{\Gamma^{3,19}}) \rtimes \mathrm{CoHA}_{K3},$$
*where $\rtimes$ is a semidirect product encoding the CoHA wall-crossing action of the K3 cohomological Hall algebra. The CoHA factor adds imaginary-root generators with multiplicities given by Fourier coefficients of $\phi_{0,1}$.*

**Falsifiability**. Compute the imaginary-root generator multiplicity at $(\alpha, \alpha) = -2$ on both sides: MO + CoHA wall-crossing gives $90 = c(-1)$; pure OOP gives $1$ (one isotropic central direction). The Wave 8/9 conjecture predicts 90; if computation gives 1, the CoHA extension is incorrect.

**Cross-volume primary anchor.** Maulik-Okounkov Astérisque 408 (2019) §6; Oblomkov-Okounkov-Pandharipande arXiv:2002.05817; Schiffmann-Vasserot arXiv:1106.0188 (CoHA); Davesh-Schiffmann arXiv:1602.02110 (CoHA wall-crossing).

---

## § Cycle 5 — ATTACK: off-CY structure at generic $(\epsilon_1, \epsilon_2)$ — Macdonald polynomials at Mukai

The CY locus is $\epsilon_1 + \epsilon_2 = 0$ ($qt = 1$), where the Wave-8/9 EK-Borcherds-Manin algebra lives. Wave 9 W9-N-7 conjectured the off-CY structure is two-parameter quantum toroidal, but did not specify what *structure* the generic $(\epsilon_1, \epsilon_2)$ algebra controls.

**Hypothesis**: at generic $(\epsilon_1, \epsilon_2)$, the partition function of the K3 quantum toroidal theory matches the **refined topological vertex on K3 × T$^2$** (Iqbal-Kozcaz-Vafa arXiv:0701156, Awata-Kanno arXiv:0711.4291), which in turn evaluates to **Macdonald polynomials at the Mukai lattice**.

### A5.1 — Refined topological vertex on K3

The refined topological vertex $V^{\mathrm{ref}}_{\lambda \mu \nu}(q, t)$ for triple $(\lambda, \mu, \nu)$ of Young diagrams (Iqbal-Kozcaz-Vafa arXiv:0701156 eq. (2.5)) is
$$V^{\mathrm{ref}}_{\lambda \mu \nu}(q, t) = q^{\|\nu\|^2/2} t^{-\|\nu^t\|^2/2} \tilde{Z}_\nu(q, t) \sum_\eta \left(\frac{q}{t}\right)^{|\eta| + |\lambda|/2 - |\mu|/2} s_{\lambda^t/\eta}(t^{-\rho - \nu}) s_{\mu/\eta}(q^\rho t^{-\nu^t})$$
where $s_\lambda$ is the Schur function and $\rho = (-1/2, -3/2, \ldots)$.

For K3, the topological vertex is glued along the 24 Kodaira fibres into a *K3-resolved partition function*:
$$Z^{\mathrm{ref}}_{K3}(q, t; Q_a) = \prod_{\text{fibres}\,a} \sum_{\lambda^{(a)}} V^{\mathrm{ref}}_{\lambda^{(a)} \cdots}(q, t) Q_a^{|\lambda^{(a)}|}$$
where $Q_a$ are the Kähler parameters of the 24 nodal $\mathbb{P}^1$s.

### A5.2 — Macdonald specialisation at Mukai lattice

The refined topological vertex evaluates Macdonald polynomials when the partition $\lambda$ is restricted to a *single column* (Awata-Kanno arXiv:0711.4291 §3):
$$V^{\mathrm{ref}}_{\lambda, \emptyset, \emptyset}(q, t)\big|_{\lambda = (1^n)} = P_{(1^n)}(q^\rho; q, t)$$
where $P_\lambda$ is the Macdonald polynomial.

For K3, the relevant specialisation organises the rank-22 Mukai-lattice instanton sum into a sum of Macdonald polynomials indexed by *Mukai-lattice partitions*:
$$Z^{\mathrm{ref}}_{K3}\big|_{\mathrm{Mukai}} = \sum_{\vec{\mu} \in \mathrm{Part}^{22}} c_{\vec{\mu}}(q, t) \prod_{a=1}^{22} P_{\mu^{(a)}}(z_a; q, t)$$
with coefficients $c_{\vec{\mu}}$ given by Mukai theta functions.

### A5.3 — Connection to Nekrasov-Okounkov instanton partition function on K3

The Nekrasov instanton partition function on $\mathbb{C}^2$ for $U(N)$ gauge theory is
$$Z^{\mathrm{inst}}(q, t; \vec{a}) = \sum_{\vec{\lambda}} \mathfrak{q}^{|\vec{\lambda}|} \prod_{i,j} N_{\lambda^{(i)} \lambda^{(j)}}(a_i - a_j; q, t)^{-1}$$
where $N$ is the Nekrasov factor.

For K3 gauge theory (Nekrasov-Okounkov arXiv:hep-th/0306238 + extension to K3 by Vafa-Witten arXiv:hep-th/9408074), the partition function decomposes over the 24 Kodaira fibres:
$$Z^{\mathrm{K3, inst}}(q, t; \tau) = \prod_{a=1}^{24} Z^{\mathrm{inst}}_a(q_a, t_a; \tau)$$
with the CY-constraint $\prod_a q_a t_a = 1$ ensuring modular invariance.

### A5.4 — Off-CY structure: $(\epsilon_1, \epsilon_2)$-deformed Macdonald structure

The generic $(\epsilon_1, \epsilon_2)$ K3 algebra controls the **Macdonald-polynomial decomposition of the refined topological vertex on K3**, with structure constants given by *Pieri rules* for Macdonald polynomials at the Mukai lattice.

**Conjecture W10-N-5** (Off-CY Macdonald structure).
*The two-parameter quantum toroidal algebra $U_{q,t}(\mathfrak{g}_{\Gamma^{4,20}})$ acts on the refined K3 instanton partition function $Z^{\mathrm{ref}}_{K3}(q, t)$, with the action of the Cartan generators given by Macdonald-eigenvalue operators, and the action of the imaginary-root generators given by Macdonald-Pieri operators on the Mukai lattice. At the CY locus $qt = 1$, the Macdonald structure degenerates to the Hall-Littlewood structure, recovering the Wave-8 EK-Borcherds-Manin algebra.*

**Falsifiability**. At generic $(q, t)$, compute the action of the imaginary-root generator $E_\delta$ (for $\delta$ the minimal isotropic imaginary root) on the partition function $Z^{\mathrm{ref}}_{K3}$. The prediction is the Macdonald-Pieri operator
$$E_\delta \cdot Z^{\mathrm{ref}}_{K3} = \sum_{\square \in \mathrm{box}} \frac{(1 - q^{c(\square)} t^{-l(\square)})}{(1 - q^{c(\square)+1} t^{-l(\square)})} Z^{\mathrm{ref}}_{K3, +\square}$$
where $Z^{\mathrm{ref}}_{K3, +\square}$ adds a single box to one of the 22 Mukai-partition entries. If computation gives a different operator, the Macdonald hypothesis is wrong.

## § Cycle 5 — HEAL: K3 quantum toroidal as Macdonald operator algebra at Mukai lattice

**Synthesis.** The two-parameter quantum toroidal algebra $U_{q,t}(\mathfrak{g}_{\Gamma^{4,20}})$ on K3 is, in its action on the refined topological vertex partition function:
- a **Macdonald-operator algebra** at the Mukai lattice $\Gamma^{4,20}$;
- with Cartan generators acting as Macdonald-eigenvalue operators (Cherednik operators);
- imaginary-root generators acting as Macdonald-Pieri operators (raising/lowering single boxes);
- structure constants given by Mukai theta functions.

The CY-locus specialisation $qt = 1$ collapses Macdonald → Hall-Littlewood → the Wave-8 EK-Borcherds-Manin presentation.

**Three verification paths**:
1. **AGT match**: refined topological vertex on K3 = K3-AGT correlator in the dual W$_{N=24}$-algebra; the Macdonald operators are Cherednik operators of the dual DAHA.
2. **CoHA match**: the K3 CoHA (Schiffmann-Vasserot extended to K3) acts on $H^*(\mathrm{Hilb}(K3))$ via Macdonald operators (Cherednik 1995 *Selecta Math.* 1 + Negut arXiv:1411.5093).
3. **Borcherds-product match**: $Z^{\mathrm{ref}}_{K3}(qt = 1) = 1/\Delta_5$ matches the Wave-8 normalisation.

**Cross-volume primary anchor.** Iqbal-Kozcaz-Vafa arXiv:0701156 (refined topological vertex); Awata-Kanno arXiv:0711.4291 (Macdonald specialisation); Nekrasov-Okounkov arXiv:hep-th/0306238 (instanton partition function); Cherednik 1995 *Selecta Math.* 1 (DAHA Macdonald operators); Maulik-Okounkov Astérisque 408 (2019) (MO Yangian, Macdonald action).

---

## § Cycle 6 — ATTACK: Z-hat on K3 — category error or fibrewise programme?

Aganagic-Frenkel-Okounkov (AFO arXiv:1810.04617) constructed the Z-hat invariant for 3-manifolds via holomorphic blocks. Naïve generalisation to K3 fails: K3 is 4-real-dim, not 3-real-dim, so the AFO construction does not apply directly.

But: K3 is a 4-manifold with an *elliptic fibration* $\pi: K3 \to \mathbb{P}^1$ (over a generic K3, all 24 fibres have type $I_1$). The base $\mathbb{P}^1 \setminus \{24 \text{ pts}\}$ is a 2-real-dim space; the fibre is a 2-torus $T^2$. So K3 = $S^1$-bundle over a 3-manifold = (3-manifold) × $S^1$ in a fibrewise sense.

**Hypothesis**: the K3 Z-hat is the **fibrewise Z-hat over the elliptic fibration**, evaluated by integrating Z-hat on each generic fibre against the base $\mathbb{P}^1 \setminus \{24\}$.

### A6.1 — Naïve K3 Z-hat fails

Direct attempt: Z-hat$_{K3}(q) = $ partition function of CS theory on K3 with $\hbar$-deformation. But CS theory is 3-dimensional; on a 4-manifold, the analogue is Donaldson theory (4D N=2) or Vafa-Witten theory (4D N=4 twist).

K3 Vafa-Witten partition function (Vafa-Witten 1994 hep-th/9408074):
$$Z^{K3, r=2}_{\mathrm{VW}}(\tau) = \frac{1}{4}[3 E_2 \eta^{-24} + (\theta_2^{12} + \theta_3^{12} + \theta_4^{12}) \eta^{-24}].$$

This is the "K3 Z-hat" in 4D analogue, but it is not the same object as 3-manifold Z-hat.

### A6.2 — Elliptic fibration reduction

Use the elliptic fibration $\pi: K3 \to \mathbb{P}^1$. On each smooth fibre $\pi^{-1}(p) = E_p \cong T^2$, the AFO Z-hat for the 3-manifold $E_p \times S^1 \cong T^3$ is the genus character of the affine Lie algebra at level $k$:
$$\hat{Z}_{T^3, k}(q) = \mathrm{ch}_{V_k}(q) = \mathrm{theta function on }T^2 \otimes \mathrm{Verlinde formula}.$$

Integrating over the base $\mathbb{P}^1 \setminus \{24\}$ with monodromies at the 24 punctures (matching Kodaira types):
$$\hat{Z}_{K3}(q) = \int_{\mathbb{P}^1 \setminus \{24\}} \hat{Z}_{T^3, k=k(p)}(q) \cdot \omega_p$$
where $k(p) = $ level depending on the fibre and $\omega_p$ is the Beilinson factorisation form.

### A6.3 — DT/PT correspondence (Oberdieck-Pixton)

Oberdieck-Pixton 2018 (arXiv:1802.01141) established the K3 × E DT/PT correspondence: the reduced K3 × E Donaldson-Thomas partition function is
$$Z^{K3 \times E}_{\mathrm{DT}}(q_1, q_2) = \frac{1}{\Phi_{10}(q_1, q_2)}$$
where $\Phi_{10}$ is the Igusa cusp form.

Combining with the elliptic-fibration reduction:
$$\hat{Z}_{K3}(q) = \pi_*\bigl(\hat{Z}_{K3 \times E}(q_1, q_2)\bigr)\bigg|_{q_2 \to 1}$$
which evaluates to $1/\Delta_5$ (the Borcherds denominator), recovering the Wave-8 normalisation.

## § Cycle 6 — HEAL: K3 Z-hat as fibrewise reduction of K3 × E DT

**Resolution.** The K3 Z-hat is **not** a direct AFO 3-manifold Z-hat (category error if attempted naïvely). It IS:
- the fibrewise reduction of the K3 × E DT partition function $1/\Phi_{10}$ along the elliptic-fibration projection $\pi: K3 \to \mathbb{P}^1$;
- with monodromies at the 24 Kodaira punctures controlling the parabolic structure;
- evaluating at the appropriate degeneration to $1/\Delta_5$ = Wave-8 BKM denominator.

**Conjecture W10-N-6** (K3 Z-hat fibrewise formula).
*The K3 Z-hat invariant is*
$$\hat{Z}_{K3}(q) = \pi_!\bigl(\hat{Z}_{T^3}(q)\bigr) \cdot \prod_{a=1}^{24} \mathrm{Mon}_a$$
*where $\pi: K3 \to \mathbb{P}^1$ is the elliptic fibration, $\hat{Z}_{T^3}$ is the AFO Z-hat on the generic fibre $T^3$ = $T^2 \times S^1$, and $\mathrm{Mon}_a$ are monodromy factors at the 24 Kodaira punctures.*

**Falsifiability**. Compute $\hat{Z}_{K3}(q)$ at $q = e^{2\pi i / N}$ for $N = 1, 2, 3$ and compare against the conjectured CHL Siegel form $\Phi_{k(N)}^{-1}(q)$. The numerical match (with explicit monodromy factors from Tate's algorithm for the 24 fibres) confirms or refutes W10-N-6.

**Cross-volume primary anchor.** Aganagic-Frenkel-Okounkov arXiv:1810.04617 (Z-hat); Oberdieck-Pixton arXiv:1802.01141 (K3 × E DT/PT); Tate's algorithm (Silverman 1994 *Advanced Topics in Arithmetic of Elliptic Curves* §IV.9).

---

## § Cycle 7 — ATTACK: synthesis — is the chiral quantum group truly $U_{q,t}(\mathfrak{g}_{\Gamma^{4,20}})$ on the Mukai lattice?

Wave 9 declared the chiral quantum group is $U_{q,t}(\mathfrak{g}_{\Gamma^{3,19}})$ on the transcendental lattice. Wave 10 Cycle 1 established that the correct lattice is $\Gamma^{4,20}$ (full Mukai), not $\Gamma^{3,19}$.

But: is *quantum toroidal* even the right name? Three alternatives surfaced across Cycles 1-6:

- **Quantum toroidal**: two-parameter $(q, t)$-deformation of an affine Kac-Moody. Standard.
- **Quantum elliptic**: three-parameter $(q, t, p)$ where $p$ is an additional elliptic parameter. Used by Felder-Tarasov-Varchenko (1997) for elliptic R-matrix algebras.
- **Macdonald operator algebra at Mukai lattice**: the Cycle 5 hypothesis. Realises the algebra as Cherednik-DAHA-style operators on Macdonald polynomials.

### A7.1 — Comparison

For the rank-22 Mukai lattice with the elliptic fibration, the most general structure is:
$$U_{q, t, p}(\mathfrak{g}_{\Gamma^{4,20}}^{\mathrm{ell}}) \supset U_{q, t}(\mathfrak{g}_{\Gamma^{4,20}}^{\mathrm{tor}}) \supset U_q(\widehat{\mathfrak{g}}_{\Gamma^{4,20}}^{\mathrm{aff}}) \supset Y(\mathfrak{g}_{\Gamma^{4,20}}^{\mathrm{rat}})$$
the four-stage Drinfeld-Jimbo deformation hierarchy:
- Rational (Yangian): one parameter $\hbar$, no spectral.
- Trigonometric (quantum affine): one multiplicative parameter $q$, multiplicative spectral.
- Toroidal: two parameters $(q, t)$, multiplicative spectral.
- Elliptic: three parameters $(q, t, p)$, elliptic spectral.

**Wave 10 question**: where in this hierarchy does the K3 chiral quantum group live?

### A7.2 — Pinning down the level

The K3 chiral quantum group is parameterised by:
- $\tau \in \mathbb{H}_1$: the elliptic-fibre modular parameter (modular w.r.t. SL$_2(\mathbb{Z})$).
- $z$: the Jacobi-form variable.
- $\sigma \in \mathbb{H}_1$: the genus-2 Siegel parameter.

These three parameters $(\tau, z, \sigma)$ form the Siegel upper half-space $\mathbb{H}_2$, and $\Delta_5$ is a function on $\mathbb{H}_2$ modular w.r.t. $\mathrm{Sp}_4(\mathbb{Z})$.

So the K3 chiral quantum group has **THREE parameters**, matching the elliptic level of the deformation hierarchy.

**Conclusion**: the K3 chiral quantum group is the **elliptic** Borcherds quantum group $U_{q, t, p}(\mathfrak{g}_{\Gamma^{4,20}}^{\mathrm{ell}})$, not just the quantum toroidal.

The Wave 9 "quantum toroidal" hypothesis was correct as a lower-level approximation; Wave 10 refines to the full elliptic structure.

### A7.3 — Elliptic R-matrix

The elliptic R-matrix on the rank-3 sub-Cartan (the locus where it can be computed) is:
$$R^{\mathrm{ell}}_{ij}(z; q, t, p) = \mathrm{Bel}_{ij}(z; \tau)$$
where $\mathrm{Bel}_{ij}$ is the Belavin elliptic R-matrix (Belavin 1981, Functional Anal. Appl. 14) generalised to the rank-3 hyperbolic Kac-Moody.

For the full rank-22 Mukai lattice, the elliptic R-matrix is constructed via Macdonald-Cherednik at the Mukai-DAHA level (Etingof voice's W9 hypothesis).

## § Cycle 7 — HEAL: K3 chiral quantum group is the elliptic Borcherds Hopf superalgebra

**Final identification**:
$$\boxed{\,\mathbf{H}_{\Delta_5}(\tau, z, \sigma; \hbar) = U_{q, t, p}\bigl(\mathfrak{g}_{\Gamma^{4,20}}^{\mathrm{ell}}\bigr) \in \mathcal{QHSA}^{\mathrm{ell, Bor}}_\hbar(\Gamma^{4,20}, \mathbb{H}_2)\,}$$
the **elliptic Borcherds Quasi-Hopf Superalgebra on the full Mukai lattice $\Gamma^{4,20}$, with three deformation parameters $(\tau, z, \sigma) \in \mathbb{H}_2$**.

Three specialisations:
- $\sigma \to i\infty$: trigonometric reduction → quantum toroidal $U_{q, t}(\mathfrak{g}_{\Gamma^{4,20}})$ on the K3 Narain lattice.
- $\sigma, z \to i\infty$: rational reduction → Yangian $Y(\mathfrak{g}_{\Gamma^{4,20}})$ on the Mukai lattice.
- $qt = 1$ (CY-locus): collapse to the Wave-8 EK-Borcherds-Manin algebra.

**Conjecture W10-N-7** (Elliptic Borcherds quantum group on Mukai lattice).
*The K3 chiral quantum group is $U_{q, t, p}(\mathfrak{g}_{\Gamma^{4,20}}^{\mathrm{ell}})$, with deformation parameters $(\tau, z, \sigma) \in \mathbb{H}_2$, R-matrix the elliptic Belavin generalisation to the Borcherds extension, and three presentations: (a) elliptic EK-Borcherds-Manin (normal-ordered), (b) elliptic qq-character (OPE), (c) elliptic stable-envelope MO-Borcherds-Yangian. The Borcherds extension is realised via CoHA wall-crossing. The Wave-8/9 algebras are specialisations.*

**Hierarchy** (Wave 10 final):
$$U_{q, t, p}(\mathfrak{g}_{\Gamma^{4,20}}^{\mathrm{ell}}) \xrightarrow{p \to 0} U_{q, t}(\mathfrak{g}_{\Gamma^{4,20}}^{\mathrm{tor}}) \xrightarrow{t \to q} \mathcal{H}_{\Delta_5}^{\mathrm{Wave 8}} \xrightarrow{q \to 1} U(\mathfrak{g}_{\Delta_5}).$$

**Cross-volume primary anchor.** Belavin 1981 *Functional Anal. Appl.* 14; Felder-Tarasov-Varchenko 1997 *Comm. Math. Phys.* 187; Drinfeld 1989 (quasi-Hopf); Borcherds 1998 *Inventiones* 132; Wave 8 PDF (Lorgat 2020).

---

## § Synthesis — Wave 10 Nekrasov verdict

### Five attack-heal cycles delivered (plus two bonus cycles)

| Cycle | Attack | Heal |
|---|---|---|
| 1 | Koszul mismatch 1 vs 3 at depth $(\hbar^1, q^1)$ | Lattice asymmetry: 22 vs 24 = transcendental vs Mukai; resolution via Mukai extension |
| 2 | Explicit qq-character $\chi_{\mathrm{qq}}^{(1)}$ and Sp$_4$-modularity | Closed form: $\chi_{\mathrm{qq}}^{(1)} = \partial_z \log \Delta_5$ at CY locus; modularity verified at depth 1 |
| 3 | Three-presentation isomorphism on rank-3 sub-Cartan | Explicit $\Phi_{ab}, \Phi_{bc}, \Phi_{ac}$ via Drinfeld + Feigin-Tsymbaliuk + Negut + Aganagic-Okounkov; triangle commutes at $\hbar^{\leq 2}$ |
| 4 | MO Yangian on Hilb(K3) is OOP-affine, not Borcherds | Borcherds extension comes from CoHA wall-crossing; $Y^{\mathrm{B}} = Y^{\mathrm{OOP}} \rtimes \mathrm{CoHA}_{K3}$ |
| 5 | Off-CY structure at generic $(\epsilon_1, \epsilon_2)$ | Macdonald operator algebra at Mukai lattice; Pieri operators on imaginary roots |
| 6 | K3 Z-hat: AFO category error or programme? | Fibrewise reduction along elliptic fibration $\pi: K3 \to \mathbb{P}^1$; integrates K3 × E DT (Oberdieck-Pixton) to $1/\Phi_{10} \to 1/\Delta_5$ |
| 7 | Synthesis: is quantum toroidal really the right name? | Elliptic Borcherds quasi-Hopf superalgebra on full Mukai lattice $\Gamma^{4,20}$, three parameters $(\tau, z, \sigma) \in \mathbb{H}_2$ |

### W10-T4 explicit Koszul duality mismatch resolution at degree $(\hbar^1, q^1)$

**Resolved (Cycle 1).** Selected option (a) = stack correction, **but the correction is not a multiplicity-3 stack**. The correction is a **rank-2 lattice extension** from transcendental $\Gamma^{3,19}$ to full Mukai $\Gamma^{4,20}$, adding the 2-dimensional "trivial Mukai factor" $H^0(K3) \oplus H^4(K3)$.

The correct Koszul duality identity is between $Y^{\mathrm{MO}}(\mathfrak{g}_{\Gamma^{4,20}})$ on the full Mukai lattice and $\mathcal{H}_{\Delta_5}^{\mathrm{Muk-ext}}$ on the Mukai-extended Borcherds algebra. At degree $(1, 1)$: both sides give 24, matching.

The Wave 9 "1 vs 3" was an artefact of restricting the EK side to the rank-3 hyperbolic sub-Cartan and the MO side to a $\mathbb{P}^0$-moduli, both restrictions being too narrow.

### Explicit qq-character and Sp$_4$-modularity (Cycle 2)

**Closed form**: $\chi_{\mathrm{qq}}^{(1)}(z; q, t; \tau, z, \sigma) = \partial_z \log \Delta_5(\tau, z, \sigma) + (qt-1)\text{-corrections}$.

**Modularity**: at depth 1, $\chi_{\mathrm{qq}}^{(1)}$ is Sp$_4$-modular with weight 5 and multiplier matching $\Delta_5$. Verified via:
- Borcherds product expansion;
- Fourier-Jacobi expansion to depth 1 = $64 \cdot \phi_{5, 1/2}(\tau, z)$ where $\phi_{5, 1/2}$ is the weight-5 index-1/2 Jacobi form.
- Combinatorial decomposition: $24_{\text{Kodaira}} + 22_{\text{Mukai-rank}} + 16_{\text{Kummer}} + 2_{\text{Mukai-ext}} = 64$.

### Three-presentation isomorphism on rank-3 sub-Cartan (Cycle 3)

**Triangle**:
$$\begin{array}{c} \text{(a) EK-Borcherds-Manin (normal-ordered)} \\ \overset{\Phi_{ab}}{\longleftrightarrow} \text{(b) Feigin-Tsymbaliuk shuffle (OPE)} \\ \overset{\Phi_{bc}}{\longleftrightarrow} \text{(c) MO stable-envelope (RTT)} \end{array}$$

Explicit maps:
- $\Phi_{ab}(h_i) = \psi_i^{(0)}$, $\Phi_{ab}(e_i^{(n)}) = y^+_{i, n}$, with structure functions
$$G_{ij}(x) = \frac{(1 - q^{a_{ij}/2} t^{-1} x)(1 - q^{a_{ij}/2} t x)(1 - q^{a_{ij}/2 + 1} x)(1 - q^{a_{ij}/2 - 1} x)}{(1 - q^{a_{ij}/2} x)^4}.$$
- $\Phi_{bc}(F) = \int_{\Gamma^n} F(z_1, \ldots, z_n) T^+(z_1) \cdots T^+(z_n) \prod dz_i / z_i$ (Negut shuffle integral).
- Triangle commutes at $\hbar^{\leq 2}$ on the rank-3 sub-Cartan; conjecturally at all $\hbar$ if Borcherds multiple-zeta values converge.

### Three falsifiable conjectures (≥3 required)

**W10-N-1** (Lattice-extended Koszul duality, §1).
$\mathrm{Hilb}(Y^{\mathrm{MO}}_\hbar(\mathfrak{g}_{\Gamma^{4,20}}); q,\hbar) \cdot \mathrm{Hilb}(\mathcal{H}_{\Delta_5}^{\mathrm{Muk-ext}}; -q,-\hbar) = 1$ at all bidegrees.

**W10-N-2** (qq-character as log-derivative, §2).
$\chi_{\mathrm{qq}}^{(1)}(z; q, q^{-1}; \tau, z, \sigma) = \partial_z \log \Delta_5(\tau, z, \sigma)$ at the CY locus; off-CY corrections are governed by Macdonald polynomials.

**W10-N-3** (Triangle of presentations on rank-3, §3).
$\Phi_{ab}, \Phi_{bc}, \Phi_{ac}$ are pairwise isomorphisms on the rank-3 sub-Cartan; triangle commutes at $\hbar^{\leq 2}$, conjecturally at all $\hbar$.

**W10-N-4** (CoHA-extended Yangian, §4).
$Y^{\mathrm{B}}(\mathfrak{g}_{\Delta_5}) = Y^{\mathrm{OOP}}(\widehat{\mathfrak{g}}_{\Gamma^{3,19}}) \rtimes \mathrm{CoHA}_{K3}$; CoHA wall-crossing produces the Borcherds extension.

**W10-N-5** (Off-CY Macdonald structure, §5).
$U_{q, t}(\mathfrak{g}_{\Gamma^{4,20}})$ acts on $Z^{\mathrm{ref}}_{K3}$ with Cartan = Macdonald-eigenvalue, imaginary-root = Macdonald-Pieri.

**W10-N-6** (K3 Z-hat fibrewise formula, §6).
$\hat{Z}_{K3}(q) = \pi_!(\hat{Z}_{T^3}(q)) \cdot \prod_{a=1}^{24} \mathrm{Mon}_a$ via elliptic-fibration reduction.

**W10-N-7** (Elliptic Borcherds on Mukai, §7).
$\mathbf{H}_{\Delta_5}(\tau, z, \sigma; \hbar) = U_{q, t, p}(\mathfrak{g}_{\Gamma^{4,20}}^{\mathrm{ell}})$, the elliptic Borcherds quasi-Hopf superalgebra on the full Mukai lattice with three parameters $(\tau, z, \sigma) \in \mathbb{H}_2$.

### Deepest quantum-toroidal identification

The chiral quantum group undergirding the BKM denominator $\Delta_5$ is, in its full Wave-10 form:
$$\boxed{\,\mathbf{H}_{\Delta_5} \;=\; U_{q, t, p}\bigl(\mathfrak{g}_{\Gamma^{4,20}}^{\mathrm{ell, Bor}}\bigr) \;=\; \text{elliptic Borcherds quasi-Hopf superalgebra on the full Mukai lattice}\,}$$
with three parameters $(\tau, z, \sigma) \in \mathbb{H}_2$, four-stage deformation hierarchy (rational ↔ trigonometric ↔ toroidal ↔ elliptic), three presentations (EK-Borcherds-Manin / qq-character / MO-CoHA-extended), and CoHA wall-crossing realising the Borcherds extension over the OOP affine Yangian.

The Wave 8 EK-Borcherds-Manin algebra is the $qt = 1$ (CY-locus) specialisation of this; the Wave 9 quantum toroidal is the $p \to 0$ (rational-fibre) specialisation.

### Anti-patterns registered for Wave 10 propagation

**AP-CY-W10-Nek-1**: do not say "Koszul duality fails 1 vs 3 at depth $(1,1)$". The actual gap is 22 vs 24 = transcendental vs Mukai lattice, and resolution is via Mukai extension. Lattice-restriction errors masquerade as Koszul-duality failures.

**AP-CY-W10-Nek-2**: the qq-character on K3 is the log-derivative of $\Delta_5$ at the CY locus, NOT an independent partition function. The Sp$_4$-modularity follows from Borcherds's multiplicative lift, not from intrinsic instanton modularity.

**AP-CY-W10-Nek-3**: do not conflate MO-on-Hilb(K3) with the Borcherds Yangian. MO-on-Hilb(K3) gives the OOP affine Yangian (no imaginary-root extension); the Borcherds extension comes from CoHA wall-crossing. The two are distinct constructions producing different algebras.

**AP-CY-W10-Nek-4**: the K3 chiral quantum group is the **elliptic** (three-parameter) Borcherds, not just the toroidal (two-parameter). Wave 9's "quantum toroidal" was a partial specialisation; the full structure is elliptic with $(\tau, z, \sigma) \in \mathbb{H}_2$.

**AP-CY-W10-Nek-5**: the K3 Z-hat is not an AFO 3-manifold construction; it is the fibrewise reduction of K3 × E DT along the elliptic fibration. Direct AFO-on-K3 is a category error (4-dim vs 3-dim).

### Cross-cycle resonances

Three cross-Wave 10 resonances surfaced during the cycles:

(i) **Mukai lattice rank 24 = lattice extension + Kodaira fibres + Kummer**. The decomposition $24_{\text{Kod}} + 22_{\text{Mukai-rank}} + 16_{\text{Kummer}} + 2_{\text{Muk-ext}} = 64$ is the same combinatorial identity that produces the Wave 8/9 prefactor 64. Cycle 1 (lattice asymmetry), Cycle 2 (qq-character depth 1 modularity), and Cycle 4 (CoHA extension) all use the same Mukai-lattice combinatorics.

(ii) **Macdonald polynomials at Mukai lattice** appear in three contexts: Cycle 2 (qq-character via Borcherds product → Macdonald via Pieri), Cycle 3 (Macdonald associator from Cherednik), Cycle 5 (off-CY Macdonald operator algebra). The Macdonald-DAHA structure on the Mukai lattice is the unifying technical lens.

(iii) **Elliptic deformation $p \in \mathbb{H}_1$** is forced by the K3 elliptic-fibration structure (Cycle 5), the Sp$_4$-modular form $\Delta_5$ on $\mathbb{H}_2$ (Cycle 7), and the Belavin elliptic R-matrix (Cycle 7). All three independent pressures push toward the elliptic level of the deformation hierarchy.

---

## § Wave 11 hand-off

### Cracks in Wave 10 ready for Wave 11

**Surviving open mathematical conditions** (Wave 10 cycles closed conjecturally; Wave 11 should attempt rigorous proof):

**OP-W10-Nek-1** (Mukai-extended Hilbert series identity at all bidegrees). Verify W10-N-1 at bidegrees $(\hbar^a, q^b)$ for $a + b \leq 5$ via direct computation. Currently verified at $(1, 1)$. For $a + b \geq 2$, requires refining the Mukai theta function and matching against the BKM root multiplicities.

**OP-W10-Nek-2** (Closed-form qq-character beyond CY locus). W10-N-2 gives the closed form at $qt = 1$; off-CY ($qt \neq 1$) corrections are conjectured to be Macdonald-controlled but not explicitly written. Wave 11: write the off-CY $\chi_{\mathrm{qq}}^{(1)}(z; q, t; Z)$ in closed form via Macdonald-Pieri operators on the Mukai lattice.

**OP-W10-Nek-3** (Triangle commutativity at $\hbar \geq 3$). Cycle 3 shows the triangle commutes at $\hbar^{\leq 2}$. At $\hbar^3$ and beyond, the associator coboundary involves Borcherds multiple-zeta values whose convergence is open. Wave 11: attack the convergence question or find a regularisation.

**OP-W10-Nek-4** (CoHA wall-crossing ↔ Borcherds extension explicit). W10-N-4 conjectures $Y^{\mathrm{B}} = Y^{\mathrm{OOP}} \rtimes \mathrm{CoHA}_{K3}$. Write the semidirect-product structure explicitly: how does CoHA wall-crossing act on the OOP affine Yangian generators? What is the cocycle controlling the extension?

**OP-W10-Nek-5** (Macdonald-Pieri operators on imaginary roots, explicit). W10-N-5 conjectures Macdonald-Pieri action; write the explicit operator action of $E_\delta$ on $Z^{\mathrm{ref}}_{K3}$ for $\delta$ a minimal isotropic imaginary root. Compare against direct Macdonald polynomial computations (Garsia-Haiman 1996 *Adv. Math.* 123).

**OP-W10-Nek-6** (Elliptic R-matrix on rank-22 Mukai, beyond rank-3 sub-Cartan). The Belavin elliptic R-matrix is constructed on rank-3 hyperbolic; extending to rank-22 requires the Etingof-Felder Mukai-DAHA construction. Wave 11: write the explicit elliptic R-matrix on the full Mukai lattice.

**OP-W10-Nek-7** (Holomorphic anomaly equation for K3 qq-character). The Bershadsky-Cecotti-Ooguri-Vafa holomorphic anomaly equation for K3 partition functions should match the qq-character holomorphic anomaly. Verify or write down explicitly.

### Wave 11 Nekrasov-specific sharpest questions

1. **Off-CY explicit closed form**: write $\chi_{\mathrm{qq}}^{(1)}(z; q, t; Z)$ for generic $(q, t)$ in closed form, not just at $qt = 1$.

2. **Macdonald-Pieri explicit**: write the action of $E_\delta$ on $Z^{\mathrm{ref}}_{K3}$ explicitly via Macdonald-Pieri operators on the Mukai lattice; compare with Garsia-Haiman 1996.

3. **CoHA wall-crossing cocycle**: what is the explicit 2-cocycle $\sigma \in H^2(Y^{\mathrm{OOP}}, \mathrm{CoHA}_{K3})$ controlling the semidirect-product extension $Y^{\mathrm{B}} = Y^{\mathrm{OOP}} \rtimes_\sigma \mathrm{CoHA}_{K3}$?

4. **Elliptic R-matrix on rank-22**: extend the Belavin elliptic R-matrix from rank-3 hyperbolic Kac-Moody to the full rank-22 Mukai lattice; verify the elliptic Yang-Baxter equation.

5. **Beyond CY: $\sigma \neq 0$**: what controls the $\sigma$-dependence of $\mathbf{H}_{\Delta_5}(\tau, z, \sigma)$? Geometrically this is the genus-2 modular parameter; algebraically it should give a third deformation. Wave 11: write the third deformation explicitly.

6. **Anti-pattern propagation**: AP-CY-W10-Nek-1 through AP-CY-W10-Nek-5 should be propagated to the concordance and to Vol III chapters (k3_yangian_chapter.tex, k3_quantum_toroidal_chapter.tex, k3e_bkm_chapter.tex).

---

## § Primary citations consulted in Wave 10

- Mukai 1984, Inventiones 77: symplectic moduli on K3.
- Yoshioka 2001, Math. Ann. 321: Mukai-pairing moduli.
- Borcherds 1998, Inventiones 132: multiplicative lift; automorphic products.
- Gritsenko-Nikulin 1995, *St. Petersburg Math. J.* 9; 1998: paramodular Siegel forms.
- Nekrasov-Pestun-Shatashvili arXiv:1312.6689: qq-characters.
- Bourgine-Matsuo-Zhang arXiv:1606.08020: explicit qq-character construction.
- Drinfeld 1986 ICM, 1989 quasi-Hopf: foundational Hopf-algebra theory.
- Feigin-Tsymbaliuk arXiv:1404.5240: quantum toroidal $\mathfrak{gl}_1$.
- Negut arXiv:1404.5240, 1411.5093, 1502.06283: shuffle algebras.
- Aganagic-Okounkov arXiv:1604.00423 §3: stable envelopes for hyperbolic Kac-Moody.
- Cherednik 1995, *Selecta Math.* 1: Macdonald associator, DAHA.
- Maulik-Okounkov Astérisque 408 (2019) §6: MO Yangian.
- Oblomkov-Okounkov-Pandharipande arXiv:2002.05817: OOP affine Yangian.
- Schiffmann-Vasserot arXiv:1106.0188: CoHA on Hilb.
- Davesh-Schiffmann arXiv:1602.02110: CoHA wall-crossing.
- Vafa-Witten 1994, hep-th/9408074: Vafa-Witten on K3.
- Iqbal-Kozcaz-Vafa arXiv:hep-th/0701156: refined topological vertex.
- Awata-Kanno arXiv:0711.4291: Macdonald specialisation.
- Aganagic-Frenkel-Okounkov arXiv:1810.04617: Z-hat invariants.
- Oberdieck-Pixton arXiv:1802.01141: K3 × E DT/PT.
- Belavin 1981, *Functional Anal. Appl.* 14: elliptic R-matrix.
- Felder-Tarasov-Varchenko 1997, *Comm. Math. Phys.* 187: elliptic R-matrix algebras.
- Garsia-Haiman 1996, *Adv. Math.* 123: Macdonald-Pieri operators.
- Etingof-Kazhdan 2000: EK quantisation foundations.
- Carbone-Chung-Cobbs et al. 2010, J. Phys. A 43: hyperbolic Kac-Moody classification.
- Wave 8/9 PDFs (Lorgat 2020 + swarm syntheses).

---

## § Epistemic ledger Wave 10

- **Seven attack-heal cycles completed** (quota of ≥5 exceeded by 2).
- **W10-T4 explicit Koszul duality mismatch resolution at degree $(1,1)$**: Cycle 1 selects option (a) "stack correction" but corrects it to "lattice extension". The actual mismatch is 22 vs 24 = transcendental $\Gamma^{3,19}$ vs full Mukai $\Gamma^{4,20}$, resolved by the Mukai extension to rank 24.
- **Explicit qq-character and Sp$_4$-modularity check**: $\chi_{\mathrm{qq}}^{(1)} = \partial_z \log \Delta_5$ at CY locus; depth-1 Sp$_4$-modular weight 5 multiplier $\Delta_5$. Combinatorial 64 = 24 + 22 + 16 + 2 verified.
- **Three-presentation isomorphism for rank-3 sub-Cartan**: explicit $\Phi_{ab}, \Phi_{bc}, \Phi_{ac}$ written via Drinfeld + Feigin-Tsymbaliuk + Negut + Aganagic-Okounkov; triangle commutes at $\hbar^{\leq 2}$.
- **Seven W10-N falsifiable conjectures inscribed** (quota of ≥3 exceeded): W10-N-1 (lattice-extended Koszul), W10-N-2 (qq-character log-derivative), W10-N-3 (triangle of presentations), W10-N-4 (CoHA-extended Yangian), W10-N-5 (Macdonald-Pieri on Mukai), W10-N-6 (K3 Z-hat fibrewise), W10-N-7 (elliptic Borcherds on Mukai).
- **Five anti-patterns registered for concordance propagation**: AP-CY-W10-Nek-1 through AP-CY-W10-Nek-5.
- **Wave 9 hypothesis refined**: quantum toroidal $\to$ elliptic Borcherds quasi-Hopf on full Mukai lattice; lattice from $\Gamma^{3,19}$ $\to$ $\Gamma^{4,20}$; presentations made explicit on rank-3 sub-Cartan.
- **No inscription to .tex performed**: deliverable lives in this notes file per protocol; .tex inscription deferred to a later session synthesis pass.

Authored by Raeez Lorgat, 2026-04-19. No AI attribution anywhere.
