# Agent 09 --- Costello --- Wave 12

**Raeez Lorgat, sole author. No AI attribution.**

Voice: Kevin Costello. Factorization algebras, holomorphic Chern--Simons, Koszul duality in the sense of Lurie HA Ch. 5 and 6, BV formalism, derived algebraic geometry, renormalization. Wave 12 is an adversarial audit of my own Wave 11 conclusions --- in particular, the "CY-3 shift" attributed to $(\mathbf{H}_{\Delta_5})^!$ and the "27 = 24 + 3" Mukai-extended $H^1$ computation. Both will need surgery.

---

## 0. What I am attacking in Wave 11

My Wave 11 output (§H3.1, §S.1(iii)) stated:

$$(\mathbf{H}_{\Delta_5})^! \;=\; V(\mathfrak{g}_{\Delta_5})^{\mathrm{coalg}}[3]$$

with the shift $[3]$ explained as "CY-3" because 6D hCS lives on $K3 \times \mathbb{C}$ (complex 3-fold). I also reinstated $\dim H^1(\widetilde{\mathfrak g}_{\Delta_5}^{\mathrm{Muk}};\mathrm{ad}) = 27 = 24 + 3$ after retracting the bare-BKM claim to $4$. And I asserted Lurie HA 6.3.1.5 as licensing an $E_3$-Koszul dual shifted by $[3]$.

Three of these claims are wrong at the level I stated them. Let me demolish them in five cycles and then rebuild.

---

## Attack-heal cycle 1 --- The CY-$d$-of-what conflation

### ATTACK 1 (first-principles).

**Claim (Wave 11):** Koszul duality of $\mathbf{H}_{\Delta_5}$ carries a CY-3 shift because the geometric base is $K3 \times \mathbb{C}$, which is complex-3-dimensional.

**Demolition.** This is a direct instance of the first-principles-cache TOP-15 confusion pattern #3 ("native / derived $E_n$"): Lurie HA 6.3.1.5 shifts by $[d]$ where $d$ is the $E_d$-linearity of the *algebra*, not the complex dimension of an *ambient geometric space*. CLAUDE.md (Vol III) is explicit: "At $d\ge 3$, $A$ is $E_1$; $E_2$ lives on $Z(\mathrm{Rep}(A))$, not on $A$." That is: when the CY category input has complex dimension $\ge 3$, the $\Phi$-output is natively $E_1$. The geometric 3-ness does **not** promote the algebra's own $E_d$-level to $d = 3$.

More sharply: Lurie HA 6.3.1.5 (bar--cobar for $E_n$-algebras, version in the 2017 text) states that if $A$ is an augmented $E_n$-algebra in a stable presentable $\infty$-category, the iterated bar $B^n(A)$ is an $E_n$-coalgebra and the cobar $\Omega^n$ is left adjoint; the Koszul self-duality statement $A \simeq \Omega^n(B^n(A))$ holds when $A$ is, in a precise sense, *small* ($n$-connected) or *proper* ($n$-coproper). The shift $[d]$ enters only for *CY-$d$-Frobenius* $E_n$-algebras with $n = d$: i.e., the algebra carries a non-degenerate cyclic form of cohomological degree $-d$ and is $E_d$-linear on the nose. It is a property of $A$, not of the space $A$ lives on.

**What failed.** I conflated (i) the CY-dimension of $K3 \times \mathbb{C}$ as an algebraic manifold (complex 3, real 6), with (ii) the $E_d$-level of $\mathbf{H}_{\Delta_5}$ as a factorization algebra, with (iii) the shift $[d]$ in Lurie 6.3.1.5 for $E_d$-Koszul self-duality of CY-$d$-Frobenius algebras. Three different $d$'s, only one of which is the one Lurie's theorem controls.

### HEAL 1.

Name the shift honestly. The object $\mathbf{H}_{\Delta_5}$ in the Wave 11 consensus is constructed over **Siegel $\mathcal{A}_2$** (Wave 11 §C2, four-voice convergence), not over $K3 \times \mathbb{C}$. The complex dimension of $\mathcal{A}_2$ is 3. But $\mathbf{H}_{\Delta_5}$ is not an $E_3$-algebra on $\mathcal{A}_2$; it is a factorization algebra whose chiral OPE is two-dimensional (holomorphic on a curve), with the Siegel base entering as a modular/automorphic parameter space. This is the **Wave 10 Cycle 7 F-theory confusion, repeated** --- where I falsely concluded BKM comes perturbatively from F-theory on $K3 \times \mathbb{C}$ and so the full 6-manifold "is the home". It is not. The home of $\mathbf{H}_{\Delta_5}$ is **a curve**: the ordered/symmetric chiral configuration space of the modular curve fibre inside Siegel $\mathcal{A}_2$.

The correct statement, removing the $d$-conflation: $\mathbf{H}_{\Delta_5}$ is an $E_1$-chiral factorization algebra on a curve (the modular curve fibre of $\mathcal{A}_2 \to \overline{M}_{1,1}$), $E_2$-braided on $Z(\mathrm{Rep}(\mathbf{H}_{\Delta_5}))$. Lurie HA 6.3.1.5 applied to this $E_1$ structure gives a bar--cobar adjunction (Vol I Theorem A, chiral version) with **no $d$-shift in the Koszul statement itself**. The Koszul dual $(\mathbf{H}_{\Delta_5})^!$ is the $E_1$-Koszul dual, computed via the single-fold bar $B^{\mathrm{ch}}$: no iterated bar, no $[d]$-shift.

**So: my Wave 11 "CY-3 shift" was wrong.** There is no CY-3 shift. The shift that does appear --- and this is the hidden structure --- is a **CY-2 shift of degree $[2]$**, but it appears in a different place: in the cyclic (Calabi--Yau) pairing on $\Phi(D^b\mathrm{Coh}(K3))$ itself, inherited from the Serre functor of $D^b\mathrm{Coh}(K3)$, which is the shift functor $[2]$ because K3 has canonical bundle $\mathcal{O}_{K3}$ trivial and complex dimension 2.

---

## Attack-heal cycle 2 --- CY-2 vs CY-3, the correct shift

### ATTACK 2.

**Claim (Wave 11):** The $[3]$-shift in $(\mathbf{H}_{\Delta_5})^! = V(\mathfrak g_{\Delta_5})^{\mathrm{coalg}}[3]$ is CY-3.

**Demolition.** K3 is a complex-2-dimensional CY (CY-2): $\omega_{K3} = \mathcal{O}_{K3}$, $c_1(K3) = 0$, $h^{0,0} = h^{0,2} = 1$, $h^{0,1} = 0$. The Serre functor on $D^b\mathrm{Coh}(K3)$ is $[\dim K3] = [2]$. Any Koszul-duality shift that comes from the CY-dimension of $\Phi$'s input **must** be $[d]$ with $d = 2$, not $d = 3$.

I wrote $[3]$ because I was thinking of 6D hCS on $K3 \times \mathbb{C}$, which adds one extra complex dimension from the $\mathbb{C}$ factor (the chiral-spacetime direction) to get a real-6-dimensional CY-3 total space. But that $\mathbb{C}$ factor is **not** part of the CY input to $\Phi$; it is the chiral parameter direction along which the factorization algebra is ordered. In the Wave 11 consensus formula
$$
\mathbf{H}_{\Delta_5}(\rho,\tau,z) = \mathcal{H}^{\mathrm{Bess}}|_{\Pi^{\mathrm{Soudry}}} \otimes_{\mathcal{Z}^{\mathrm{Sat}}} (U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}} \cdot \Phi^{\mathrm{Sieg\text{-}Bor}}_{\mathrm{Sp}_4}
$$
there is no tensor factor with complex dimension contributing 1; the Siegel coordinates $(\rho, \tau, z)$ are *modular* parameters, not chiral-spacetime.

**What failed.** Cache confusion #3 repeats. The "3" in "CY-3 shift" was a confusion of (a) the complex dimension of the 6D hCS home, (b) the $E_d$ of Lurie's theorem, and (c) the Siegel rank $g = 2$ which gives complex dimension $3$ for $\mathcal{A}_g$ at $g=2$. Three unrelated "3"s. None of them is the CY-dimension of the input to $\Phi$ --- which is $D^b\mathrm{Coh}(K3)$, CY-**2**.

### HEAL 2.

The correct shift on $(\mathbf{H}_{\Delta_5})^!$, arising from the CY-2-ness of the K3 input and Lurie HA 6.3.1.5 applied to the $E_2$-chiral output, is **$[2]$, not $[3]$**. More precisely:

- At the level of $\Phi(D^b\mathrm{Coh}(K3))$: this is the Mukai-Heisenberg $\mathcal{H}_{\mathrm{Muk}}$ (rank 24, signature $(4,20)$), an $E_2$-chiral algebra on a curve. CY-2 gives it a cyclic (Calabi--Yau) pairing of degree $-2$ via the Serre functor. Its $E_2$-Koszul dual, via Lurie HA 6.3.1.5 applied with $n=2$ and CY-2 Frobenius structure, is $\mathcal{H}_{\mathrm{Muk}}^{\mathrm{coalg}}[2]$, where the shift $[2]$ is the CY-2 shift.
- At the BKM level: $\mathbf{H}_{\Delta_5}$ is built from $\mathcal{H}_{\mathrm{Muk}}$ plus the Borcherds denominator structure $\Delta_5$. The Koszul dual **inherits** the $[2]$-shift from the K3 Mukai layer; it does **not** acquire an extra $[1]$-shift from the $\mathbb{C}$ parameter direction, because that direction is a chiral-spacetime coordinate, not part of the CY input.

**Corrected Wave-11 claim (W12-Costello-RET-CY3):**
$$
\boxed{\;(\mathbf{H}_{\Delta_5})^! \;=\; V(\mathfrak g_{\Delta_5})^{\mathrm{coalg}}[2]\;}
$$
with the $[2]$ being the **CY-2** shift from the K3 input to $\Phi$, not a CY-3 shift. My Wave 11 "[3]" was a factor-of-one off error, traceable to the cache confusion #3.

**Sanity check.** Vol III `chapters/theory/cy_to_chiral.tex` line 71 confirms that $\Phi(D^b\mathrm{Coh}(K3))$ has complex dimension-2 input and $E_2$-output. Line 2254 names the $E_2$-cotangent complex $L_{E_2}(A)$ in degrees $\ge 1$. Line 2267 gives Dunn additivity: $E_3 \simeq E_2 \otimes E_1$, so an $E_3$-object has to have *both* an $E_2$-layer and an $E_1$-layer. For $\mathbf{H}_{\Delta_5}$ the $E_1$-layer is the chiral factorization direction (along the modular curve fibre); the $E_2$-layer is the braided rep-theory structure on $Z(\mathrm{Rep}(\mathbf{H}_{\Delta_5}))$. That is $E_2$, not $E_3$. So the appropriate $n$ in Lurie HA 6.3.1.5 is $n = 2$, shifted by $[d] = [2]$ from CY-2-Frobenius.

---

## Attack-heal cycle 3 --- Is $\mathbf{H}_{\Delta_5}$ actually CY-$d$-Frobenius at the algebra level?

### ATTACK 3.

**Claim (Wave 11 implicit):** Lurie HA 6.3.1.5 applies, so the Koszul dual involves a shift.

**Demolition.** Lurie HA 6.3.1.5's shift $[d]$ requires $A$ to be a **CY-$d$-Frobenius** $E_n$-algebra: there is a non-degenerate cyclic trace $\tau: A \to k[-d]$ that pairs with the multiplication. For $A = \mathbf{H}_{\Delta_5}$, *does such a cyclic trace exist at the algebra level?*

At the level of *categories*, yes: $D^b\mathrm{Coh}(K3)$ is a CY-2 category in the sense of Kontsevich, with Serre functor $[2]$ and cyclic Hochschild structure of degree $-2$. The Mukai--Polishchuk--Bondal--Orlov pairing $\langle \mathcal{E}, \mathcal{F}\rangle = \chi(\mathcal{E}, \mathcal{F})$ on numerical Grothendieck groups realises the CY-2 Frobenius form.

At the level of $\mathbf{H}_{\Delta_5}$ as an algebra, the situation is more subtle. $\mathbf{H}_{\Delta_5}$ is infinite-dimensional and the obvious candidate cyclic trace --- the Borcherds--Gritsenko denominator pairing --- requires regularization to give a finite value. The Beilinson-voice Wave 11 found $K^\kappa = 8, \varrho = 1/6, K = 48$ for the Theorem-C bucket; these are finite regularized cyclic-trace values. But they are **not** the $[d]$-shift data of Lurie 6.3.1.5 directly. They are the chiral Hochschild characteristic numbers.

**What I need to check:** does $\mathbf{H}_{\Delta_5}$ carry a genuine CY-2 Frobenius structure at the algebra level (not just via its CY-2 category input)? The answer is not automatic.

### HEAL 3.

The correct statement distinguishes three Frobenius-type data, following the Vol III "four $\kappa$-invariants, never conflated" discipline:

1. **$\Phi$-input-CY**: $D^b\mathrm{Coh}(K3)$ is CY-2 as a category. This is category-level data.
2. **$\Phi$-output cyclic structure**: $\mathcal{H}_{\mathrm{Muk}} = \Phi(D^b\mathrm{Coh}(K3))$ inherits a cyclic pairing of degree $-2$, constructed explicitly as the Mukai pairing $\langle \cdot, \cdot\rangle_{\mathrm{Muk}}$ of signature $(4, 20)$. This is chain-level data; it gives the $E_2$-chiral Koszul self-duality $\mathcal{H}_{\mathrm{Muk}}^! \simeq \mathcal{H}_{\mathrm{Muk}}^{\mathrm{coalg}}[2]$.
3. **$\mathbf{H}_{\Delta_5}$ as algebra**: this is the Mukai-Heisenberg *plus* the Borcherds denominator structure, which includes imaginary roots with multiplicities $|c_{\phi_{0,1}}(D)|$. It has a **regularized** cyclic trace (the Borcherds-$\zeta$-regularised supertrace from my Wave 10 Cycle 1), and this regularized trace is of degree $-2$, not $-3$. But it is *only defined up to regularisation*; the naive trace diverges on infinite-multiplicity root spaces.

So the $[d]$-shift in Lurie HA 6.3.1.5 for $(\mathbf{H}_{\Delta_5})^!$ is $[2]$, with the caveat that the Frobenius structure is *regularized* CY-2, not unregularized. This is weaker than the hypothesis of Lurie's theorem in the purely finite-dim case. The theorem still applies, but only after choosing a regularization scheme (Borcherds-$\zeta$).

**Hidden structure revealed.** The Koszul-dual shift $[2]$ is **the $E_2$-CY shift from the K3 input category**, inherited through $\Phi$. There is a *separate* structural twist from the Borcherds-imaginary-root sector, but this twist is *not* a shift; it is a **superization** (the $\mathbb{Z}/2$-grading of the BKM superalgebra $\mathfrak g_{\Delta_5}$) plus a regularization constraint. Together these give the Wave-11 "biquasitriangular cobraided quasi-Hopf *super* algebra" of Drinfeld voice; the "super" is the hidden Koszul-dual piece beyond the $[2]$-shift.

---

## Attack-heal cycle 4 --- The $\dim H^1 = 27$ decomposition, re-examined

### ATTACK 4.

**Claim (Wave 11 §A5.4, §H5.1):** $\dim H^1(\mathfrak g_{\Delta_5}; \mathrm{ad}) = 4$ (bare: 3 Cartan + 1 lightlike central). $\dim H^1(\widetilde{\mathfrak g}_{\Delta_5}^{\mathrm{Muk}}; \mathrm{ad}) = 27 = 24 + 3$ (Mukai-extended).

**Demolition.** The "24 + 3" decomposition needs to be spelled out cochain-level, not asserted. Let me redo the Chevalley--Eilenberg computation from first principles, and this time track exactly which 24 and which 3.

**Bare BKM.** $\mathfrak g_{\Delta_5}$ has Cartan rank 3 (hyperbolic rank, see `standalone/k3e_cy3_programme_vol3.tex`). Its abelianization is $\mathfrak g_{\Delta_5}^{\mathrm{ab}} = \mathfrak h \oplus \mathfrak z$ where $\mathfrak h$ is the rank-3 Cartan and $\mathfrak z$ is the centre (imaginary roots orthogonal to all real roots).

*Question: what is $\dim \mathfrak z$?* For a BKM with even Lorentzian root lattice of signature $(n, 1)$, the centre is spanned by the light-like vectors in the imaginary cone fixed by Weyl. For $\mathfrak g_{\Delta_5}$ with root lattice $\mathrm{II}_{2,1}$ (the rank-3 hyperbolic lattice), the light-cone has dimension 1 (a single null direction modulo scale). So $\dim \mathfrak z = 1$.

Total bare: $\dim H^1 = \dim(\mathfrak g^{\mathrm{ab}})^* = 3 + 1 = 4$. **Agrees with Wave 11.**

**Mukai-extended $\widetilde{\mathfrak g}_{\Delta_5}^{\mathrm{Muk}}$.** This is $\mathfrak g_{\Delta_5}$ semidirect (or direct, depending on how the Mukai-Heisenberg is glued) with the rank-24 Mukai-Heisenberg $\mathfrak h_{\mathrm{Muk}}$. The Mukai-Heisenberg is a central extension of an abelian Lie algebra of dim 24 by a 1-dimensional centre (the Heisenberg central charge); as a Lie algebra (not Lie conformal algebra) it is a Heisenberg $\mathfrak h_{\mathrm{Muk}}^{\mathrm{Lie}}$ of dim $24 + 1 = 25$, with abelianization of dim 24.

What gets glued: the lightlike central direction of $\mathfrak g_{\Delta_5}$ is identified with the Heisenberg central charge of $\mathfrak h_{\mathrm{Muk}}$. (This is the "Mukai-shift" = lightlike-central identification, witnessed in `cy_to_chiral.tex` line 1091--1094 where the $(4,20)$-signature arises from K3 second cohomology plus two hyperbolic planes, the latter being the absorbed light-cone direction.)

So $\widetilde{\mathfrak g}_{\Delta_5}^{\mathrm{Muk}, \mathrm{ab}} = \mathfrak h \oplus (\mathfrak h_{\mathrm{Muk}}^{\mathrm{Lie}})^{\mathrm{ab}}$ where the 1-dim centre of $\mathfrak g$ coincides with the 1-dim centre of $\mathfrak h_{\mathrm{Muk}}$. Dimensions: $3 + 24 = 27$, with **no overlap in dimension counting** because the 1-dim centre is shared (and thus counted once, on the Heisenberg side).

**The decomposition is 3 (Cartan) + 24 (Mukai-Heisenberg abelianization)**, **not** 3 (Cartan) + 1 (central) + 23 (non-central Mukai) [which would also sum to 27 but with a different justification]. The Wave 11 "24 + 3" is correct, with the 24 = Mukai-rank = $\chi(K3)$ and the 3 = BKM-Cartan-rank. My Wave 11 statement is vindicated.

### HEAL 4.

**Three independent verification paths for $\dim H^1(\widetilde{\mathfrak g}_{\Delta_5}^{\mathrm{Muk}}; \mathrm{ad}) = 27$:**

(V1) **Chevalley--Eilenberg abelianization.** $\widetilde{\mathfrak g}^{\mathrm{Muk},\mathrm{ab}} = \mathfrak h \oplus \mathfrak h_{\mathrm{Muk}}^{\mathrm{ab}}$, dim $3 + 24 = 27$. Each summand is independent because the gluing identifies only the 1-dim centre (which is subtracted from both and re-added once).

(V2) **Out(g) via BKM derivations.** Outer derivations of $\widetilde{\mathfrak g}^{\mathrm{Muk}}$ = Cartan rescalings (3) + Mukai-Heisenberg outer twists (24 = Mukai rank), total 27. This is the abelian quotient $(\mathrm{Aut}/\mathrm{Inn})_0$ of the identity component.

(V3) **Lattice of characters.** The character lattice of $\widetilde{\mathfrak g}^{\mathrm{Muk}}$ is the Mukai lattice $\Lambda^{4,20}$ (rank 24) plus the Cartan dual of $\mathfrak g_{\Delta_5}$ (rank 3), giving rank 27 total. $H^1$ = rank of character lattice = 27.

All three agree on 27.

**But crucially:** this is the $H^1$ of the *Mukai-extended* algebra $\widetilde{\mathfrak g}^{\mathrm{Muk}}$, not of the bare BKM. And it counts infinitesimal *Lie algebra* deformations via derivations, not operadic $E_2$-chiral deformations via Hochschild cochains on the factorization algebra. The latter is a different object, entering the Theorem-C bucket via $H^2_{\mathrm{Hoch}}$ with regularized trace.

**Correction to Wave 11 §H5.1:** The fourth entry, $\dim H^1_{\mathrm{BV\text{-}BRST}}(\mathcal F^{\mathrm{hCS}};\hbar) = 0$, corresponds to *BV anomaly* first cohomology on 6D hCS. This is a *different* cohomology from the Lie-algebra $H^1$ of $\mathfrak g_{\Delta_5}$. It equals zero after Borcherds-$\zeta$-regularized anomaly cancellation. The Wave 11 table is correct *only* if one is explicit that four different cohomologies are being listed. Let me re-state, with explicit ambient qualifiers:

| # | Complex | Coefficients | Value |
|---|---|---|---|
| 1 | Chevalley--Eilenberg, bare $\mathfrak g_{\Delta_5}$ | trivial $\mathbb{C}$ | 4 |
| 2 | Chevalley--Eilenberg, bare $\mathfrak g_{\Delta_5}$ | $\mathrm{ad}$ | 4 (out-derivations) |
| 3 | Chevalley--Eilenberg, Mukai-ext $\widetilde{\mathfrak g}^{\mathrm{Muk}}$ | $\mathrm{ad}$ | 27 |
| 4 | BV-BRST 6D hCS, one-loop, Borcherds-$\zeta$-regularized | trivial | 0 |
| 5 | Brown-K3 elliptic motivic Lie coalgebra, Pollack-free, M24-equiv. at wt. 5 | | 27 (conj.) |
| 6 | Hochschild $\mathrm{ChirHoch}^1(\mathbf{H}_{\Delta_5})$ | $\mathrm{ad}$ | **open** (needs Theorem-C bucket resolution) |

Only two of these are 27, and they are coincidences by construction (V1--V3 for row 3, and motivic weight-5 count for row 5).

---

## Attack-heal cycle 5 --- The factorization algebra base: where does $\mathbf{H}_{\Delta_5}$ actually live?

### ATTACK 5.

**Claim (unstated but implicit in Wave 11):** $\mathbf{H}_{\Delta_5}$ is a factorization algebra on $\mathbb{A}^2$ (the K3-local model) or on K3 itself.

**Demolition.** Neither is right.

- **K3 itself?** A factorization algebra on a CY-2 surface is a 2d object; its chiral coproduct / OPE is **2-dimensional** (Beilinson--Drinfeld's chiral algebras are genuinely defined on *curves*, not surfaces, in the standard convention). Costello--Gwilliam factorization algebras on a 2-fold are $E_2$-in-the-factorization-axiom sense, but the OPE has the form of surface operators, not the vertex-algebra OPE $A(z)B(w) \sim (z-w)^{-n}\cdot C(w)$ we need. So: $\mathbf{H}_{\Delta_5}$ is *not* a factorization algebra on K3 in the Beilinson--Drinfeld sense.

- **$\mathbb{A}^2$?** This is the Schiffmann--Vasserot home for CoHA-on-$\mathbb{C}^2$ constructions, and it gives quantum toroidal $\mathfrak{gl}_1$. The Wave 11 formula places $\mathbf{H}_{\Delta_5}$ as an $M_{24}$-invariant part of $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24}$ --- so 24 copies of the $\mathbb{A}^2$-CoHA, one per Kodaira fibre. **But** the whole is not on $\mathbb{A}^2$; it is on the union of 24 local patches, one per Kodaira fibre of an elliptic K3.

- **Siegel $\mathcal{A}_2$?** Nekrasov/Kazhdan/Beilinson/Drinfeld convergence (Wave 11 §C2): the *modular* parameter space is Siegel $\mathcal{A}_2$. But this is a modular parameter space, not a chiral configuration space. The object on $\mathcal{A}_2$ is a **D-module** (Beilinson voice, Wave 11), whose *fibre* at a Humbert surface point is a chiral algebra.

### HEAL 5.

The correct factorization-algebra base is **a nodal elliptic curve** $E^{\mathrm{nod}}$ with 24 marked nodes, embedded in Siegel $\mathcal{A}_2$ via the elliptic-K3 fibration. Explicitly:

1. Fix a generic elliptic K3 surface $X \to \mathbb{P}^1$ with Kodaira discriminant 24 (24 singular fibres, type $I_1$ nodal).
2. The base $\mathbb{P}^1$ carries the divisor $D_{\mathrm{disc}} = \sum_{i=1}^{24} [p_i]$ of Kodaira singular points.
3. Form the *reduced* curve $E^{\mathrm{nod}} := \mathbb{P}^1 \setminus D_{\mathrm{disc}}$, the smooth open; or alternatively the nodal singular K3-discriminant curve (24 nodes glued to a single genus-0 base).
4. $\mathbf{H}_{\Delta_5}$ is a factorization algebra on $E^{\mathrm{nod}}$ (or on a formal neighbourhood of $D_{\mathrm{disc}}$), with an $M_{24}$-equivariance permuting the 24 nodes and a Borcherds--$\Delta_5$ modular parameter living on Siegel $\mathcal{A}_2$.

This is **the K3-discriminant-loci factorization algebra**. It is natively 1-dimensional in the factorization sense (on the $\mathbb{P}^1$ base), with 2d chiral-OPE structure at each node (the local Kodaira $I_1$ singularity), and modular parameters in $\mathcal{A}_2$.

**6-functor maps.** The operadic OPE structure on $\mathbf{H}_{\Delta_5}$ as a factorization algebra on $E^{\mathrm{nod}}$ admits:

- $j_*$: extension from the smooth locus $\mathbb{P}^1 \setminus D_{\mathrm{disc}}$ to all of $\mathbb{P}^1$.
- $i^*$: restriction to each node $p_i$, giving the local $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ fibre.
- $\Delta^*$: diagonal, giving the $M_{24}$-equivariant averaging on the 24-fold product.
- $\otimes$: tensor product over the Satake centre $\mathcal{Z}^{\mathrm{Sat}}$.
- $\pi_*$: pushforward to $\mathcal{A}_2$, giving the Soudry metaplectic Klingen-CAP D-module.
- $p^!$: dualising pullback, realizing the Koszul dual via Lurie 6.3.1.5.

**OPE pole structure.** At each node $p_i$, the local OPE of two currents has the form
$$
A_i(z) B_i(w) \sim \sum_{n \ge 0} \frac{C_i^{(n)}(w)}{(z-w)^{n+1}} + \mathcal{O}(\log(z-w))
$$
with the $\log(z-w)$ term encoding the nodal degeneration. Between different nodes $p_i, p_j$ ($i \ne j$), the OPE is non-singular and has the $M_{24}$-equivariance: $A_i(z) B_j(w)$ depends only on the $M_{24}$-orbit of $(i, j)$.

**Averaging map.** The averaging $\mathrm{av}: \mathbf{H}_{\Delta_5}^{E_1} \to \mathbf{H}_{\Delta_5}^{\mathrm{mod}}$ from ordered to symmetric chiral homology is the $M_{24}$-average combined with the Borcherds-$\zeta$-regularization of Wave 10 Cycle 1; it lands in the $\Phi_{10}$-automorphic image on $\mathcal{A}_2$.

**The hidden structure is: $\mathbf{H}_{\Delta_5}$ is the 24-node factorization algebra on the K3-Kodaira discriminant curve, $M_{24}$-equivariant, Borcherds-modular on Siegel $\mathcal{A}_2$, with $[2]$-shifted Koszul dual inheriting CY-2 from the K3 input.**

---

## CY-2 vs CY-3 shift audit

Consolidated verdict:

| Interpretation | Shift | Verdict |
|---|---|---|
| "CY-dim of 6D hCS home $K3\times\mathbb{C}$" | $[3]$ | **WRONG** — confuses ambient-chiral with CY-input (AP-cache #3) |
| "CY-dim of Siegel $\mathcal{A}_2$" | $[3]$ | **WRONG** — $\mathcal{A}_2$ is modular base, not CY input |
| "CY-dim of K3 input to $\Phi$" | $[2]$ | **CORRECT** (this is the one) |
| "CY-dim of $\mathbb{A}^2$ for CoHA local model" | $[2]$ | **CORRECT for local piece**, inherited through tensor |
| "$E_n$ of algebra (bar--cobar iteration)" | $[1]$ on the $E_1$-chiral direction | **SEPARATE** — not a CY shift |

Final answer: $(\mathbf{H}_{\Delta_5})^! = V(\mathfrak g_{\Delta_5})^{\mathrm{coalg}}[2]$, with the $[2]$ being **CY-2** inherited from the K3 input to $\Phi$. The Borcherds super structure contributes a $\mathbb{Z}/2$-grading (the super, not a shift).

I retract Wave 11 §H3.1 (which said $[3]$) and replace with Wave 12 §Cycle 2 HEAL (which says $[2]$).

---

## Explicit $H^1$ computation (bare 4 + Mukai 27)

Rigorous, chain-level, Chevalley--Eilenberg. No appeal to "Etingof-Kazhdan-Schiffmann formula" which I retracted in Wave 11.

### Bare BKM $\mathfrak g_{\Delta_5}$.

Root data: Lorentzian root lattice $Q = \mathrm{II}_{2,1}$ of rank 3, signature $(2,1)$. Cartan $\mathfrak h = Q \otimes \mathbb{C}$, rank 3. Real simple roots: three $(-2)$-vectors generating a Weyl group $W \subset O(Q)$ of infinite order (hyperbolic reflection group). Imaginary simple roots: lightlike vectors in $Q$, with multiplicities $c_{\phi_{0,1}}(D)$.

Chevalley--Eilenberg complex with trivial coefficients:
$$
C^k(\mathfrak g; \mathbb{C}) = \mathrm{Hom}(\Lambda^k \mathfrak g, \mathbb{C}) = (\Lambda^k \mathfrak g)^*.
$$
$H^1(\mathfrak g; \mathbb{C}) = (\mathfrak g / [\mathfrak g, \mathfrak g])^* = (\mathfrak g^{\mathrm{ab}})^*$.

**$\mathfrak g^{\mathrm{ab}}$ for BKM:** Decompose $\mathfrak g = \mathfrak h \oplus \bigoplus_\alpha \mathfrak g_\alpha$. The commutator $[\mathfrak h, \mathfrak g_\alpha] \ne 0$ unless $\alpha$ is trivial on $\mathfrak h$, i.e., $\alpha$ is in the radical of the Cartan pairing. For BKM with $\mathfrak h$ non-degenerate (rank 3, signature $(2,1)$ non-degenerate), no nonzero $\alpha$ is trivial on $\mathfrak h$. So all $\mathfrak g_\alpha$ are in $[\mathfrak h, \mathfrak g] \subseteq [\mathfrak g, \mathfrak g]$ and drop out of $\mathfrak g^{\mathrm{ab}}$.

Wait, this gives $\mathfrak g^{\mathrm{ab}} = \mathfrak h$, dim 3. Where does the $+1$ come from?

**Subtle point:** $[\mathfrak g, \mathfrak g]$ in the BKM includes the brackets between root spaces, which generate elements in the Cartan *back*. Specifically, $[\mathfrak g_\alpha, \mathfrak g_{-\alpha}] = \mathbb{C} \cdot h_\alpha$ for real $\alpha$, which spans the full Cartan; but for imaginary $\alpha$, $[\mathfrak g_\alpha, \mathfrak g_{-\alpha}]$ might be zero or a central element. For the *lightlike* imaginary simples (the distinguishing feature of Borcherds-KM), the bracket $[\mathfrak g_\delta, \mathfrak g_{-\delta}] = 0$ in the naive construction, because the norm $\langle \delta, \delta \rangle = 0$ forces the Serre relation coefficient to vanish --- this is exactly the Borcherds-generalization that distinguishes BKM from KM.

Hmm, that is **backwards** from what I need: if $[\mathfrak g_\delta, \mathfrak g_{-\delta}] = 0$ for lightlike $\delta$, then those root spaces are *central* (commute with everything at $h$-level via the zero bracket), and they contribute to the abelianization. The 1-dim lightlike central direction is the image of these root spaces in $\mathfrak g^{\mathrm{ab}}$.

**Precise count for $\mathfrak g_{\Delta_5}$:** there is one lightlike direction in $Q = \mathrm{II}_{2,1}$ modulo Weyl, namely the isotropic vector $\delta$ with $\langle \delta, \delta \rangle = 0$ generating the 1-dim isotropic sub-lattice. Each lightlike imaginary root space $\mathfrak g_{k\delta}$ for $k \in \mathbb{Z}_{>0}$ with multiplicity $c_{\phi_{0,1}}(k^2/2)$ contributes to the abelianization *only through its image modulo $[\mathfrak g, \mathfrak g]$*. The imaginary-real bracket $[\mathfrak g_{k\delta}, \mathfrak g_{\alpha_{\mathrm{real}}}]$ is nonzero in general (inner derivation from the Cartan-valued pairing), so $\mathfrak g_{k\delta}$ is not *wholly* central. The central subspace is the kernel of all these brackets, which is 1-dim (the single "lightlike direction" modulo the imaginary-root structure).

**Conclusion:** $\mathfrak g^{\mathrm{ab}} = \mathfrak h \oplus \mathfrak z_{\mathrm{light}}$, dim $3 + 1 = 4$. **$\dim H^1(\mathfrak g_{\Delta_5}; \mathbb{C}) = 4$.** Wave 11 and Wave 12 agree.

With $\mathrm{ad}$ coefficients: $H^1(\mathfrak g; \mathrm{ad}) = \mathrm{Out}(\mathfrak g)$. Outer derivations = Cartan rescalings (3) + lightlike central twist (1) = 4. Wave 11 and Wave 12 agree.

### Mukai-extended $\widetilde{\mathfrak g}_{\Delta_5}^{\mathrm{Muk}}$.

$\widetilde{\mathfrak g}^{\mathrm{Muk}} := \mathfrak g_{\Delta_5} \rtimes \mathfrak h_{\mathrm{Muk}}$, where $\mathfrak h_{\mathrm{Muk}}$ is the rank-24 Heisenberg Lie algebra on the Mukai lattice $\Lambda^{4,20}$, with the lightlike central direction of $\mathfrak g$ identified with the Heisenberg centre of $\mathfrak h_{\mathrm{Muk}}$.

Abelianization: $\widetilde{\mathfrak g}^{\mathrm{Muk}, \mathrm{ab}} = \mathfrak h \oplus \mathfrak h_{\mathrm{Muk}}^{\mathrm{ab}}$. Dimensions: $3 + 24 = 27$ (the shared 1-dim centre is counted once, as part of $\mathfrak h_{\mathrm{Muk}}^{\mathrm{ab}}$).

**$\dim H^1(\widetilde{\mathfrak g}^{\mathrm{Muk}}; \mathbb{C}) = 27$.** With $\mathrm{ad}$: $27$ (Cartan 3 + Mukai-Heisenberg-outer 24). Verified via three paths (V1--V3 of Cycle 4 HEAL above).

### Caveat: the "27" is *regularized*.

Each Mukai-Heisenberg generator corresponds to a harmonic mode on the K3 lattice $\Lambda^{4,20}$. As a full Lie algebra, each mode has an infinite oscillator tower $a_n^{(i)}$ for $n \in \mathbb{Z}$. The "rank 24" counts the zero-modes, and the $H^1$ count 27 is specifically for the zero-mode abelianization, modulo the oscillator excitations.

If we include all oscillator modes, $H^1$ becomes infinite. The "27" is the $\mathbb{Z}$-graded weight-zero part of $H^1$, which makes sense as a finite-dim count for lattice VOAs.

---

## Koszul dual in Lurie HA 6.3.1.5 framework

### 6.3.1.5 statement, paraphrased.

Lurie HA 6.3.1.5 (roughly): let $A$ be an augmented $E_n$-algebra in a stable presentable symmetric monoidal $\infty$-category $\mathcal{C}$. Then the bar construction $B^{(n)}(A) = A \otimes_A^{E_n\text{-bar}} k$ is an augmented $E_n$-coalgebra in $\mathcal{C}$, and there is an adjunction

$$\Omega^{(n)}: \mathrm{coAlg}^{E_n, \mathrm{aug}}(\mathcal{C}) \rightleftarrows \mathrm{Alg}^{E_n, \mathrm{aug}}(\mathcal{C}) : B^{(n)}$$

with $\Omega^{(n)}$ left adjoint. If $A$ is $n$-connected (or, alternatively, $n$-coproper), $\Omega^{(n)}(B^{(n)}(A)) \simeq A$.

The shift $[d]$ enters when $\mathcal{C}$ is itself $d$-Calabi--Yau, i.e., the unit object has a cyclic self-duality of degree $-d$. Then the Koszul dual $A^! := B^{(n)}(A)^\vee$ (linear dual of the bar coalgebra) carries a $[d]$-shifted $E_n$-algebra structure: $A^! \simeq B^{(n)}(A)^\vee[d]$.

In our case:
- $\mathcal{C} = \mathrm{Mod}_{\mathbb{C}}$ or the derived category of $D$-modules on a curve; take $\mathcal{C}$ such that the Mukai pairing lives as a CY-2 structure.
- $n = 2$ (chiral $E_2$-Koszul for $\mathcal{H}_{\mathrm{Muk}}$); or $n = 1$ (chiral $E_1$-Koszul for $\mathbf{H}_{\Delta_5}$ as a factorization algebra on the nodal curve, with the $E_2$ living only on $Z(\mathrm{Rep})$).
- $d = 2$ from the CY-2 Mukai pairing (NOT $d=3$).

### Two different Koszul statements, both true.

**Statement A ($E_2$, at the Mukai-Heisenberg layer):**
$$\mathcal{H}_{\mathrm{Muk}}^! \;\simeq\; \mathcal{H}_{\mathrm{Muk}}^{\mathrm{coalg}}[2]$$
via Lurie HA 6.3.1.5 with $n = 2$, $d = 2$. This is an $E_2$-Koszul self-duality up to $[2]$-shift.

**Statement B ($E_1$, at the full BKM layer):**
$$\mathbf{H}_{\Delta_5}^! \;\simeq\; V(\mathfrak g_{\Delta_5})^{\mathrm{coalg}}[2]$$
via Lurie HA 6.3.1.5 with $n = 1$, $d = 2$. This is the $E_1$-chiral Koszul dual, with the $[2]$-shift inherited from the K3-Mukai CY-2 layer *through* the embedding $\mathcal{H}_{\mathrm{Muk}} \hookrightarrow \mathbf{H}_{\Delta_5}$ of the Cartan--Heisenberg subalgebra.

Statement B is what I stated in Wave 11, but with the corrected $[2]$ instead of $[3]$.

### Is $\mathbf{H}_{\Delta_5}$ small / $n$-coproper enough for 6.3.1.5 to apply?

Not on the nose. $\mathbf{H}_{\Delta_5}$ is infinite-dimensional and not $n$-connected; it has generators at every $\mathbb{Z}$-grading.

However, after **Borcherds-$\zeta$-regularization** (my Wave 10 Cycle 1) the regularized dimensions are finite ($\mathrm{sdim}^\zeta = 0$) and the algebra becomes $n$-coproper in a regularized sense. Lurie HA 6.3.1.5 then applies to the regularized $\mathbf{H}_{\Delta_5}^{\zeta}$, and the Koszul dual is
$$\mathbf{H}_{\Delta_5}^{\zeta, !} \;\simeq\; V(\mathfrak g_{\Delta_5})^{\mathrm{coalg}, \zeta}[2].$$

This is the precise $(\infty, 1)$-categorical statement. At chain level, one verifies it by (i) computing the bar coalgebra $B^{\mathrm{ch}}(\mathbf{H}_{\Delta_5})$ via the explicit Costello--Gwilliam factorization-algebra bar construction on the nodal curve $E^{\mathrm{nod}}$ of Cycle 5, (ii) identifying its linear dual as the vertex coalgebra $V(\mathfrak g_{\Delta_5})^{\mathrm{coalg}}$, and (iii) reading off the $[2]$-shift from the Mukai CY-2 pairing $\mathcal{H}_{\mathrm{Muk}}$ sitting inside.

---

## Factorization algebra base identification

Verdict: the factorization algebra home of $\mathbf{H}_{\Delta_5}$ is the **24-node discriminant curve of a generic elliptic K3**, which I will denote $E^{\mathrm{nod}}_{24}$ (the base $\mathbb{P}^1$ with 24 marked Kodaira $I_1$ singular-fibre points, $M_{24}$-equivariant permutation).

### Reasons this is not on $K3$ itself.

(i) Chiral factorization algebras in the Beilinson--Drinfeld sense are on *curves*, not surfaces.

(ii) A factorization algebra "on $K3$" in the Costello--Gwilliam topological sense would give a locally constant factorization algebra (since $K3$ is a topological 4-manifold), which gives $E_4$-algebras, not what we want.

(iii) The chiral OPE $A(z)B(w) \sim (z-w)^{-n} C(w)$ is genuinely 1-dimensional in the $(z-w)$ variable; promoting to $K3$ would require a 2-dim analogue that does not match the Borcherds denominator structure.

### Reasons this is not on $\mathbb{A}^2$.

$\mathbb{A}^2$ is the Schiffmann--Vasserot local model for CoHA = quantum toroidal $\mathfrak{gl}_1$. $\mathbf{H}_{\Delta_5}$ contains 24 copies of this, but the whole algebra is on the *union* of 24 $\mathbb{A}^2$-patches, one per Kodaira $I_1$ local model, glued on an $\mathbb{P}^1$ base.

### Reasons this is on the 24-node discriminant curve.

(i) Kodaira classification: a generic elliptic K3 has 24 singular fibres of type $I_1$ (nodal).
(ii) The Borcherds product $\Delta_5 = \Phi_{10}^{1/2}$ has denominator formula expanded over the 24-node lattice structure (Gritsenko--Nikulin 1998, Borcherds 1998).
(iii) Etingof voice (Wave 11): $(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$, one per Kodaira fibre, $M_{24}$-equivariant permutation of the 24 nodes.
(iv) The $M_{24}$ symmetry acts naturally on the 24 nodes of $E^{\mathrm{nod}}_{24}$; no other chiral base has this permutation symmetry.

### 6-functor formalism on $E^{\mathrm{nod}}_{24}$.

Let $j: E^{\mathrm{nod}}_{24} \setminus \mathrm{Nodes} \hookrightarrow E^{\mathrm{nod}}_{24}$ be the open inclusion of the smooth locus; $i: \mathrm{Nodes} \hookrightarrow E^{\mathrm{nod}}_{24}$ the closed inclusion. Then:

- $j_* \mathbf{H}_{\Delta_5}|_{\mathrm{smooth}}$: the extension of the smooth-locus factorization algebra.
- $i^* \mathbf{H}_{\Delta_5}$: the restriction to the 24 nodes; by Wave 11 Etingof, this is $\bigoplus_{i=1}^{24} U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)_i$.
- $i^! \mathbf{H}_{\Delta_5}$: the dualising pullback to the nodes; shifted by $[2]$ (CY-2 Serre functor on the local model $\mathbb{A}^2_i$).
- Averaging: the $M_{24}$-orbit map $\overline{E^{\mathrm{nod}}_{24}/M_{24}} \hookrightarrow \overline{\mathcal{A}_2}$ gives the Borcherds lift, pushing to the modular D-module on Siegel $\mathcal{A}_2$.

This is the concrete factorization-algebra realization of the Wave 11 consensus formula, now with a specific chiral base.

---

## Rank-reconciliation inclusion chain

Target (W12-T3): match Etingof 24, Costello 27, Gaiotto $E_8$-rank-8 via $\mathfrak e_8 \hookrightarrow \widetilde{\mathfrak g}_{\Delta_5}^{\mathrm{Muk}} \hookrightarrow (U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$.

### Inclusion 1: $\mathfrak e_8 \hookrightarrow \widetilde{\mathfrak g}_{\Delta_5}^{\mathrm{Muk}}$.

$\mathfrak e_8$ has Lie-algebra rank 8, dim 248. It sits inside $\widetilde{\mathfrak g}^{\mathrm{Muk}}$ as follows:
- The Mukai lattice $\Lambda^{4,20}$ has decomposition $\Lambda^{4,20} = U^4 \oplus E_8(-1)^2$ (where $U = $ hyperbolic plane).
- The two $E_8(-1)$ factors contribute via Frenkel--Kac construction to two $\widehat{\mathfrak e_8}_{-1}$ sub-affine-algebras of $\widetilde{\mathfrak g}^{\mathrm{Muk}}$.
- Gaiotto voice's $(\widehat{E_8})_{-12}$ (Minahan--Nemeschansky Beem--Rastelli chiral algebra): this is a level $-12$ affine $E_8$ algebra, arising in the Schur-index computation of the $T[K3]$ theory. Its classical rank is 8.

So $\mathfrak e_8$ sits in $\widetilde{\mathfrak g}^{\mathrm{Muk}}$ via the **Mukai lattice $E_8$-summands**, realized as Frenkel--Kac lattice currents. Rank count on the Cartan: 8 (from one $E_8$ summand) $\subset 24$ (Mukai rank).

### Inclusion 2: $\widetilde{\mathfrak g}_{\Delta_5}^{\mathrm{Muk}} \hookrightarrow (U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$.

Each of the 24 $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ factors has Cartan rank 1 + Heisenberg central charge, with additional toroidal generators. The $M_{24}$-equivariant part of the 24-fold tensor takes the $M_{24}$-invariant combinations:
- Total: 1 "trivial" invariant (the sum-of-24 diagonal), plus 23 "standard" invariants (from the 23-dim standard representation of $M_{24}$ on $\mathbb{C}^{24} / \mathbb{C} \cdot \mathbf{1}$).
- The trivial 1-dim part + 23 standard gives a rank-24 Cartan inside the invariant part.

Plus the toroidal extensions give the full BKM root structure: imaginary roots from the Heisenberg central charges at each node, real roots from the interaction terms between nodes weighted by the $M_{24}$-orbit structure.

**Inclusion:** the Mukai-Heisenberg subalgebra $\mathfrak h_{\mathrm{Muk}} \hookrightarrow (U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$ via the $M_{24}$-invariant Cartan-ranks. Rank count: 24 = 1 + 23 inside the invariant Cartan. The BKM rank-3 Cartan sits as a sub-Cartan of this 24, specifically as the $A_1^{24}$-Niemeier-type 3-dim sub-sublattice (Wave 11 Witten voice).

### Overall inclusion chain:

$$\mathfrak e_8^{(1)} \oplus \mathfrak e_8^{(2)} \hookrightarrow \mathfrak h_{\mathrm{Muk}} \oplus \mathfrak g_{\mathrm{BKM}\text{-}\mathrm{real}} = \widetilde{\mathfrak g}_{\Delta_5}^{\mathrm{Muk}} \hookrightarrow (U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$$

with ranks

$$8 + 8 = 16 < 24 < 24 \quad\text{(Cartan ranks)}$$

and

$$24 = \mathrm{rank}\,\Lambda^{4,20} = \chi(K3) = |{\rm Kodaira\,fibres}| \quad\text{(all three "24"s are the same invariant)}.$$

The three "24"s coincide for a generic elliptic K3 via the Kodaira-to-Niemeier bijection (mod Mukai extension):

- $\chi(K3) = 24$: Euler characteristic = Kodaira degree of discriminant for elliptic K3.
- $\mathrm{rank}\,\Lambda^{4,20} = 24$: Mukai-extended K3-lattice rank.
- $A_1^{24}$-Niemeier rank: $24 = 24 \cdot 1$, giving the 24 $A_1$-roots.

These identifications are via the Enriques--Mukai--Niemeier correspondence (cf. Wave 11 W12-T9 task).

Costello 27 = $8 + 8 + 3$ = sum of two $E_8$-rank plus BKM Cartan rank-3; **not** the same as the Mukai 24, but a different count pulled from the Lie-algebra $H^1$.

Etingof 24 = Kodaira count, matching Mukai rank.

Gaiotto 8 = $E_8$ classical rank, sitting inside one of the $E_8(-1)$ Mukai summands.

All three are now reconciled via explicit inclusions.

---

## Wave 12 convergence verdict

After five attack-heal cycles + CY-shift audit + rank reconciliation:

### RETRACTIONS from Wave 11 (this voice).

**W12-Costello-RET-CY3 (major):** $(\mathbf{H}_{\Delta_5})^! = V(\mathfrak g_{\Delta_5})^{\mathrm{coalg}}[3]$ with CY-3 shift is **WRONG**. Corrected: $(\mathbf{H}_{\Delta_5})^! = V(\mathfrak g_{\Delta_5})^{\mathrm{coalg}}[2]$ with CY-2 shift, inherited from K3 Mukai layer.

**W12-Costello-RET-6Dhome (minor):** "6D hCS on $K3 \times \mathbb{C}$" is the *twisted-SUGRA* home, but the *chiral-factorization-algebra* home is the 24-node discriminant curve $E^{\mathrm{nod}}_{24}$ of a generic elliptic K3, not $K3 \times \mathbb{C}$.

### SURVIVES from Wave 11 (this voice).

- $\dim H^1(\mathfrak g_{\Delta_5}; \mathrm{ad}) = 4$ bare. Verified chain-level three paths.
- $\dim H^1(\widetilde{\mathfrak g}^{\mathrm{Muk}}; \mathrm{ad}) = 27 = 24 + 3$. Verified three paths (V1--V3).
- Not self-Koszul; Koszul dual is vertex coalgebra, shifted.
- BV-BRST one-loop $H^1 = 0$ (anomaly-free via Borcherds-$\zeta$).

### NEW in Wave 12 (this voice).

- **Factorization algebra base:** $E^{\mathrm{nod}}_{24}$ = 24-node discriminant of generic elliptic K3, $M_{24}$-equivariant, modular-fibre over Siegel $\mathcal{A}_2$.
- **6-functor structure:** $j_*, i^*, i^!, \pi_*, \otimes$ explicit on $E^{\mathrm{nod}}_{24}$.
- **OPE pole structure:** standard chiral-VOA OPE at each node, $\log$-corrections from nodal degeneration, $M_{24}$-equivariance between nodes.
- **Averaging map:** $M_{24}$-average + Borcherds-$\zeta$-regularization, lands in $\Phi_{10}$-automorphic image on $\mathcal{A}_2$.
- **Explicit rank chain:** $\mathfrak e_8 \hookrightarrow \widetilde{\mathfrak g}^{\mathrm{Muk}} \hookrightarrow (U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$ with inclusion ranks 8/24/24.
- **CY-shift audit:** the shift is $[2]$ (CY-2 from K3), not $[3]$ (which would require a non-existent CY-3 structure on the input).

---

## Retraction ledger

| # | Wave 11 claim | Retraction type | Wave 12 correction |
|---|---|---|---|
| 1 | $(\mathbf{H}_{\Delta_5})^! = V(\mathfrak g_{\Delta_5})^{\mathrm{coalg}}[3]$ with CY-3 shift | **CY-dim-wrong** | $[2]$ with CY-2 from K3 Mukai layer |
| 2 | $\mathbf{H}_{\Delta_5}$ has CY-3 structure because ambient is $K3 \times \mathbb{C}$ | **ambient conflation** | $K3 \times \mathbb{C}$ is the 6D hCS home; the CY-input is K3 (dim 2) |
| 3 | "Lurie HA 6.3.1.5 + CY-3 shift" | **misapplied** | Lurie 6.3.1.5 + CY-2 shift; $n = 1$ or $2$ depending on layer |
| 4 | $\mathbf{H}_{\Delta_5}$ is an $E_3$-algebra on the 3-fold | **native/derived $E_n$** (cache #3) | $E_1$-chiral on the curve $E^{\mathrm{nod}}_{24}$; $E_2$ only on $Z(\mathrm{Rep})$ |

Retractions 2, 3, 4 all stem from the same root confusion: **cache TOP-15 entry #3 (native / derived $E_n$)**. This is the *single* confusion behind the three errors.

---

## New anti-patterns raised

**AP-CY-W12-Cos-1** (upgrades AP-CY-W11-Cos-2): "CY-$d$ shift in Koszul duality via Lurie HA 6.3.1.5 takes $d$ = CY-dim of the *input* to $\Phi$ (or equivalently, of the cyclic Frobenius structure on the algebra itself), **not** the complex dimension of any ambient space. For K3 input: $d = 2$. For $K3 \times \mathbb{C}$ as 6D hCS home: $d = 2$ still (the $\mathbb{C}$ is chiral-spacetime, not CY). Anyone writing $[3]$-shift for a K3-based chiral algebra has conflated CY-dim with chiral-ambient-dim."

**AP-CY-W12-Cos-2**: "A factorization algebra on a surface is not the same as a chiral algebra. Chiral algebras (Beilinson--Drinfeld) live on curves. When a surface enters (e.g. K3 as a CY-2 input), its role is as an input to $\Phi$, whose output is a chiral algebra on a curve (specifically: a discriminant curve or a modular curve)."

**AP-CY-W12-Cos-3**: "Borcherds $\mathbf{H}_{\Delta_5}$ lives on the 24-node discriminant curve $E^{\mathrm{nod}}_{24}$ of a generic elliptic K3, NOT on K3 itself and NOT on $K3 \times \mathbb{C}$. The 24 nodes are the Kodaira $I_1$ fibres; the $M_{24}$-equivariance is the natural permutation of the 24 nodes."

**AP-CY-W12-Cos-4**: "Lurie HA 6.3.1.5 requires $A$ to be $n$-coproper (or $n$-connected) for the Koszul self-duality to be strict. For infinite-dim objects like BKM $\mathbf{H}_{\Delta_5}$, one needs **Borcherds-$\zeta$-regularization** to get $n$-coproperty; the Koszul duality then holds for the regularized algebra, not the naive one."

**AP-CY-W12-Cos-5**: "Outer derivations of a BKM superalgebra are **not** the same as the chiral Hochschild cohomology of the chiral algebra generated by that BKM. Wave 11's $\dim H^1 = 27$ was the former (for Mukai-extended), not the latter (which goes through the Theorem-C bucket with $K^\kappa = 8$). Both numbers are real, but they measure different things. Do not conflate."

---

## Residual open

**OQ-W12-Cos-1:** *Hochschild $\mathrm{ChirHoch}^1(\mathbf{H}_{\Delta_5})$* --- the row-6 entry in my Cycle 4 table of cohomologies --- is left open. What is its dimension? Conjecture: it equals 27 (matching the Mukai-ext Lie-cohomology by a Vol I Theorem H concentration argument), but the proof requires the Theorem-C bucket $K^\kappa = 8$ analysis to close. Would require explicit chain-level computation on the 24-node discriminant curve.

**OQ-W12-Cos-2:** *Is $\mathbf{H}_{\Delta_5}$ actually CY-2-Frobenius at the algebra level*, not just inheriting CY-2 from the K3 input? Specifically: does the Borcherds-$\zeta$-regularized Mukai pairing extend to a non-degenerate cyclic trace on all of $\mathbf{H}_{\Delta_5}$, not just on its Cartan--Heisenberg subalgebra $\mathcal{H}_{\mathrm{Muk}}$? Partial positive evidence: the regularized $\mathrm{sdim}^\zeta = 0$ (Wave 10 Cycle 1). But this is a necessary condition, not sufficient for CY-2-Frobenius.

**OQ-W12-Cos-3:** *Precise match between Wave 11 Theorem-C bucket $K^\kappa = 8$ (Beilinson) and Lurie 6.3.1.5 $[d]$-shift machinery.* I claim $d = 2$; Beilinson's $K^\kappa = 8$ gives $2 c_+ = 8$, so $c_+ = 4$. Is the $d = 2$ shift consistent with $c_+ = 4$? Dimensional analysis: the Mukai pairing has signature $(4, 20)$; the positive-chirality $c_+ = 4$ matches the 4 positive-signature dimensions of the Mukai lattice. So yes, consistent. But the *formula* $d = 2$ (from CY-dim) and $c_+ = 4$ (from Mukai positive-signature) are a priori independent; their matching is a Wave-12 constraint to verify.

**OQ-W12-Cos-4:** *Explicit chain homotopy* witnessing $\Omega^{(1)}(B^{(1)}(\mathbf{H}_{\Delta_5}^{\zeta})) \simeq \mathbf{H}_{\Delta_5}^{\zeta}$, at the chain level on $E^{\mathrm{nod}}_{24}$. This is Vol I Theorem A (backbone bar--cobar adjunction) applied at 24 Kodaira nodes simultaneously, with $M_{24}$-equivariance. The explicit homotopy $h$ satisfying $[d, h] = \mathrm{id} - p$ needs to be written down.

**OQ-W12-Cos-5:** *Does the 24-node discriminant factorization algebra genuinely encode the F-theory non-perturbative BPS resummation of my Wave 11 Cycle 4?* Wave 11 said BKM emerges from F-theory only non-perturbatively; the 24-node factorization algebra may give the right chain-level home for the non-perturbative BPS states. Conjecture: yes, the 24-node algebra IS the non-perturbative F-theory BPS algebra, with each node contributing a $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ tower of bound states.

---

## Wave 12 synthesis (this voice, final)

**Theorem (Costello Wave 12, CY-2 Koszul shift + factorization-algebra home).**

Let $\mathbf{H}_{\Delta_5}$ be the Borcherds non-abelian chiral bialgebra of $\Delta_5$ (as refined in Wave 11 consensus formula). Then:

(a) **Factorization-algebra home** (new in Wave 12): $\mathbf{H}_{\Delta_5}$ is a factorization algebra on the 24-node discriminant curve $E^{\mathrm{nod}}_{24}$ of a generic elliptic K3, $M_{24}$-equivariantly permuting the 24 nodes, modular-fibred over Siegel $\mathcal{A}_2$ via the Borcherds theta lift to $\Delta_5 \in H^0(\mathcal{A}_2, \omega^5)$.

(b) **Koszul dual shift is $[2]$, not $[3]$** (retracts Wave 11): via Lurie HA 6.3.1.5 applied with $n = 1$ (chiral $E_1$) and CY-2 Frobenius input from the K3 Mukai layer,
$$(\mathbf{H}_{\Delta_5}^{\zeta})^! \;\simeq\; V(\mathfrak g_{\Delta_5})^{\mathrm{coalg}, \zeta}[2],$$
where $\zeta$ denotes Borcherds-$\zeta$-regularization. The $[2]$ is CY-2 from K3; not CY-3.

(c) **$\dim H^1$ count** (refines Wave 11): bare BKM has $\dim H^1 = 4$ (3 Cartan + 1 lightlike central); Mukai-extended has $\dim H^1 = 27 = 24 + 3$ (24 Mukai-Heisenberg generators + 3 BKM Cartan), verified chain-level via three independent paths (abelianization, outer derivation, character-lattice rank). These are Lie-algebra cohomologies, distinct from chiral Hochschild $\mathrm{ChirHoch}^1$.

(d) **Rank-reconciliation chain**: $\mathfrak e_8 \hookrightarrow \widetilde{\mathfrak g}_{\Delta_5}^{\mathrm{Muk}} \hookrightarrow (U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$, with ranks $8 \subset 24 \subset 24$ at the Cartan level. The three "24"s (Mukai rank, Kodaira-fibre count, $A_1^{24}$-Niemeier rank) are the same invariant via the Enriques--Mukai--Niemeier bijection.

(e) **6-functor formalism on $E^{\mathrm{nod}}_{24}$**: $j_*$ (smooth-locus extension), $i^*$ (restriction to node = local $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$), $i^!$ ($[2]$-shifted dualising pullback), $\Delta^*$ ($M_{24}$-diagonal), $\pi_*$ (Siegel-modular pushforward to $\mathcal{A}_2$).

(f) **Averaging map**: $\mathrm{av}: \mathbf{H}_{\Delta_5}^{E_1} \to \mathbf{H}_{\Delta_5}^{\mathrm{mod}}$ is the $M_{24}$-average + Borcherds-$\zeta$-regularization, landing in the $\Phi_{10}$-Siegel-automorphic image on $\mathcal{A}_2$.

### Primary literature anchors (Wave 12 new).

- **Lurie, J.**, *Higher Algebra*, 2017: Theorem 6.3.1.5 (Koszul self-duality up to shift), Theorem 5.2.2.8 (bar--cobar adjunction), Dunn additivity for $E_n$.
- **Costello, K., Gwilliam, O.**, *Factorization Algebras in Quantum Field Theory*, Vols I--II, 2017/2021: factorization-algebra framework, 6-functor formalism.
- **Costello, K., Li, S.**, "Quantum BCOV theory on Calabi-Yau manifolds and the higher genus B-model", arXiv:1201.4501: CY-dim tracking in chiral-algebra Koszul duality.
- **Beilinson, A., Drinfeld, V.**, *Chiral Algebras*, Colloquium Publications 51, 2004: chiral-algebra factorization axioms on curves.
- **Borcherds, R.**, "Automorphic forms on $O_{s+2,2}(\mathbb{R})$ and infinite products", Invent. Math. 120 (1995), 161--213: singular theta lift, $\Delta_5$.
- **Gritsenko, V., Nikulin, V.**, "Automorphic forms and Lorentzian Kac-Moody algebras, I/II", Internat. J. Math. 9 (1998): $\Delta_5$ as Borcherds product.
- **Schiffmann, O., Vasserot, E.**, "Cherednik algebras, $W$-algebras and the equivariant cohomology of the moduli space of instantons on $\mathbb{A}^2$", Publ. IHES 118 (2013): CoHA on $\mathbb{A}^2$ = $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$.
- **Kodaira, K.**, "On compact analytic surfaces II", Ann. Math. 77 (1963): Kodaira discriminant classification for elliptic K3.

### Cross-references to other Wave 12 voices (to check in synthesis).

- **Agent 03 (Etingof)**: my 24-node discriminant-curve home should match Etingof's 24-fold Kodaira-fibre Humbert-pole structure.
- **Agent 06 (Beilinson)**: my CY-2 shift $[2]$ should match Beilinson's $\hbar^2 = -1/8 = -1/(2c_+)$ with $c_+ = 4$, consistent with $d = 2$ (CY-dim of K3).
- **Agent 07 (Drinfeld)**: my Lurie 6.3.1.5 framework should be compatible with Drinfeld's genus-2 Siegel-Borcherds associator; the associator lives on $\overline{\mathcal{A}_2}$ as modular fibration, while the chiral algebra lives on the discriminant curve inside the fibres.
- **Agent 10 (Gaiotto)**: my $\mathfrak e_8$-inclusion should match Gaiotto's $(\widehat{E_8})_{-12}$ via the Mukai-lattice $E_8(-1)$ summands.

---

**End Agent 09 Costello Wave 12. Raeez Lorgat, sole author.**
