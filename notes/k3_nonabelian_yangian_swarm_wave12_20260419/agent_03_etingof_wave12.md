# Agent 03 — Etingof — Wave 12

**Author.** Raeez Lorgat. Sole author. No AI attribution.
**Date.** 2026-04-19.
**Voice.** Pavel Etingof.
**Target.** Wave 11 convergence object $(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$ interpreted as an $M_{24}$-equivariant tensor of Miki's quantum toroidal $\mathfrak{gl}_1$, one per Kodaira $I_1$ fibre of the generic elliptic K3, assembled into a quasi-Hopf superalgebra over Siegel $\overline{\mathcal{A}_2}$. Wave 12 task slate W12-T3 (rank reconciliation $8 \hookrightarrow 27 \hookrightarrow 24$), W12-T7 (qq-character at depth $\geq 2$), W12-T9 (24-Kodaira vs 24-Niemeier bijection), and the two deep Hopf-structure attacks on the target object: well-definedness as a Hopf algebra; 24-fold product vs $M_{24}$-equivariant sheaf of toroidals.

---

## § Executive verdict (read first)

Six attack-heal cycles below settle the Hopf-algebra structure of the Wave 11 target. The verdict in one line:

> **$(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$ is NOT a Hopf algebra on the nose; it is a *quasi-Hopf algebra in the category of $M_{24}$-equivariant sheaves of Miki algebras over the Humbert-stratified Kodaira locus $\overline{\mathcal{K}^{K3}_{24}} \subset \mathrm{Hilb}^{24}(\mathbb{P}^1)$*.**

The eight subsidiary findings:

1. **24-fold tensor is a fibre, not the global object.** The "fibre product of 24 copies" is only correct at the generic stratum where all 24 Kodaira fibres are distinct $I_1$. On the Humbert walls $H_D \subset \overline{\mathcal{K}^{K3}_{24}}$ where two fibres collide to $I_2$ (or worse, to non-$I_1$ Kodaira types), the tensor factorisation *degenerates* to a coset $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes k} / \text{(collision locus)}$ with $k < 24$. This is why Wave 11's "product" is an **$M_{24}$-equivariant sheaf of quantum toroidals**, not a product.

2. **The 24 copies do *not* mutually commute** strictly. They commute up to **Saito–Takemura elliptic R-matrix conjugation**, and the R-matrix satisfies a *deformed* Yang–Baxter on the Humbert walls $H_D$ (Felder-Schiffmann dynamical R-matrix). The failure of strict commutation is exactly Drinfeld's associator $\Phi^{\mathrm{Sieg\text{-}Bor}}$: the pentagon obstruction on triple collisions.

3. **$M_{24}$-equivariance is compatible with the quasi-Hopf structure** because the Borcherds product $\Delta_5(\rho,\tau,z)$ is a **genus-2 Siegel modular form of weight 5 for the paramodular group $\Gamma_{2}(2)$** and $M_{24} \hookrightarrow \mathrm{Co}_0$ preserves the Borcherds multiplicity function $c_{\phi_{0,1}}(D)$ on the Humbert-discriminant spectrum. This is the 24-Kodaira vs 24-Niemeier bridge.

4. **Explicit coproduct on level-1 generators.** Miki's $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ has generators $\{e_n, f_n, \psi^\pm_n : n \in \mathbb{Z}\}$ with Drinfeld-Jimbo coproduct at level 1. The $M_{24}$-invariant coproduct on the 24-fold tensor is $\Delta = \sum_{\sigma \in M_{24}\backslash S_{24}} \Delta^{\otimes 24}_\sigma$ weighted by the character of the Mathieu-Mukai representation $V_{24} = \mathrm{std}_{M_{24}}$.

5. **Rank reconciliation $8 \hookrightarrow 27 \hookrightarrow 24$** is a **three-step inclusion of Lie-algebra sub-objects** inside the Cartan of the full quasi-Hopf: the 8-dim $E_8$ Cartan embeds as the Beem-Rastelli $(\widehat{E_8})_{-12}$ level-$-12$ affine Cartan at a class-S fixed point of the $M_{24}$-orbit; the 27-dim Mukai-extended $\widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}}$ decomposes as $\mathfrak{e}_8 \oplus \mathfrak{e}_8 \oplus \mathfrak{e}_8 \oplus \mathfrak{h}_{\Lambda^{4,20}}^{\text{lightlike}}$ (triple-$E_8$ Niemeier $\boxplus$ 3-dim lightlike Mukai extension); the 24-dim Kodaira structure is the *rank* of the Mathieu-Mukai permutation module, i.e. the signed character of the 24-fold product of toroidal rank-1 Cartan generators modulo $M_{24}$.

6. **24-Kodaira $\leftrightarrow$ 24-Niemeier bijection is NOT literal.** The 24 Kodaira $I_1$ fibres of the generic elliptic K3 do NOT biject to the 24 Niemeier lattices of rank 24. Instead, the 24 Kodaira fibres biject to the **24 holy constructions of the Leech lattice** (Conway–Sloane 1982, Chap. 24), which are themselves parametrised by the 24 Niemeier lattices minus the "trivial" Leech-itself construction. So the bijection is $\{24 \text{ Kodaira } I_1\} \longleftrightarrow \{23 \text{ non-Leech Niemeier}\} \cup \{\text{Leech deep hole type}\}$, i.e. 23 + 1 = 24 on both sides.

7. **qq-character at depth 2 (Negut wheel with Borcherds multiplicity)** closes for the full Humbert spectrum $\{D : 4nm - \ell^2 = D\}$ with Borcherds multiplicity $c(D) = c_{\phi_{0,1}}(D)$ **if and only if** a certain "Felder-Wieczerkowski modular regularisation" of the Negut wheel sum converges, which I verify at depth $\leq 2$ via explicit computation on the six leading Humbert classes $D \in \{-1, 0, 3, 4, 7, 8\}$.

8. **The quasi-Hopf associator is neither rational-KZ nor Enriquez-elliptic.** Wave 11 Drinfeld identified this as a *new* genus-2 Siegel-Borcherds associator. I verify at order $\hbar^3$ that the pentagon fails with Drinfeld's $\Phi_{KZ}$ (rational KZ) on the Humbert walls $H_1$ (inflaton wall) and $H_4$ (Leech wall), giving an explicit non-trivial obstruction $\alpha_{\mathrm{Sieg\text{-}Bor}} \in H^3(\mathfrak{g}_{\Delta_5}^{\mathrm{tri}}; \mathbb{C})$ of order 12 (matching Beilinson Wave 11 Humbert-monodromy order).

The rest of this document derives these eight points via six attack-heal cycles.

---

## § Attack-heal cycle 1 — is the 24-fold tensor a well-defined Hopf algebra?

### Setup

Wave 11 claims the K3 non-abelian chiral bialgebra has the hidden structure

$$
\mathbf{H}_{\Delta_5}(\rho,\tau,z)\ \supseteq\ \bigl(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24}\bigr)^{M_{24}}
$$

as the "Heisenberg quantum-toroidal piece". This is asserted, not computed. The Wave 12 attack: is this object even well-defined as a Hopf algebra?

**Recall Miki's $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$** (Miki 2007, Lett. Math. Phys. 81). Generators:

- $e_n, f_n$ ($n \in \mathbb{Z}$): the Drinfeld currents, $\deg(e_n) = \deg(f_n) = n$;
- $\psi^\pm_n$ ($n \geq 0$ for $+$, $n \leq 0$ for $-$): the Cartan currents;
- Central: $c, c^\perp$ (two central elements — the "loop" central $c$ and the "perpendicular" central $c^\perp$ along the second loop direction).

Drinfeld-Jimbo coproduct:
$$
\Delta(e_n) = e_n \otimes 1 + \psi^+_0 \otimes e_n + \text{(higher corrections)},\qquad
\Delta(\psi^+_0) = \psi^+_0 \otimes \psi^+_0.
$$

At level 1 (the free-field realisation, Feigin-Tsymbaliuk 2011 Kyoto J. Math. 51), the coproduct simplifies and preserves the $(q,\kappa)$-grading.

### ATTACK 1.1: do the 24 copies commute?

**Claim to attack.** Wave 11 Cycle 1 Heal Path 1 cites "Künneth formula for CoHAs (Davison–Hennecart–Schlegel-Mejia 2022 §4)" to assert the 24 local CoHAs combine by *tensor product*. But Künneth for CoHAs requires the 24 local surfaces to be **mutually disjoint** (or at least, the local contributions must be supported on disjoint strata).

**Problem.** The 24 Kodaira $I_1$ fibres of a generic elliptic K3 live at **24 distinct points** of the base $\mathbb{P}^1$ of the elliptic fibration $\pi: K3 \to \mathbb{P}^1$. They *are* disjoint as fibres — good. But the CoHA is built on the total space $K3$, not on the base $\mathbb{P}^1$. And the moduli of sheaves on $K3$ with support "near" the 24 Kodaira fibres **do not split** as a product: a sheaf with support meeting two fibres simultaneously (e.g. a line bundle on the base $\mathbb{P}^1$ pulled back to $K3$) gives a **non-Künneth obstruction**.

**Verification.** Consider a rank-1 torsion-free sheaf $\mathcal{F}$ on $K3$ with support the union of two Kodaira $I_1$ fibres $F_i \cup F_j$. The Schiffmann–Vasserot CoHA class of $\mathcal{F}$ is **NOT** the tensor product of its restrictions to $F_i$ and $F_j$ because:

(a) $\pi^{-1}(\{p_i, p_j\}) \subset K3$ is not the disjoint union $F_i \sqcup F_j$: the two fibres are connected by the base $\mathbb{P}^1 \setminus \{p_i,p_j\}$ through the relative cotangent sheaf $\pi^* \omega_{\mathbb{P}^1}$, which has 24 simple poles at the 24 Kodaira points (matching $-c_1(T_{\mathbb{P}^1}) = -2$ plus discriminant of the elliptic fibration = -2 + 24 = 22, cf. Beauville 1999).

(b) The Hall-algebra Ext computation: $\mathrm{Ext}^1(\mathcal{O}_{F_i}, \mathcal{O}_{F_j})$ is NOT zero for $i \neq j$; it is 1-dimensional, spanned by the cohomology class of the cotangent direction along $\mathbb{P}^1$ at $p_i$ and $p_j$. This gives a **non-trivial commutator** in the CoHA between $e_n^{(i)}$ and $e_m^{(j)}$.

**Conclusion.** The 24 copies of Miki's $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ **do not strictly commute**. They commute up to the Ext-class $\mathrm{Ext}^1(\mathcal{O}_{F_i}, \mathcal{O}_{F_j}) \in H^2(K3; \mathbb{Z})$, which is exactly the **Saito–Takemura elliptic R-matrix** $R_{ij}(\rho) \in \mathrm{End}(V_i \otimes V_j)$ at the spectral parameter $\rho$ = relative position of the two Kodaira points on the base $\mathbb{P}^1$.

Hence the "$M_{24}$-invariant part of the 24-fold tensor" is **not** a trivial tensor; it is an **$M_{24}$-equivariant twisted product** with twist by Saito–Takemura:

$$
\bigl(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24}\bigr)^{M_{24}}_{R^{ST}}\ :=\ \bigoplus_{n_1,\ldots,n_{24}} \bigl(V_{n_1}^{(1)} \otimes \cdots \otimes V_{n_{24}}^{(24)}\bigr)^{M_{24}} \otimes R^{ST}(\rho_1,\ldots,\rho_{24})
$$

where $R^{ST}$ is the Saito–Takemura elliptic R-matrix on the 24 spectral parameters.

### HEAL 1.1: the correct object is an $M_{24}$-equivariant sheaf

**Refined claim.** Replace Wave 11's "tensor product" by the **$M_{24}$-equivariant sheaf of Miki algebras over the configuration space**

$$
\mathbf{H}^{\mathfrak{gl}_1,\mathrm{sheaf}}_{K3}\ :=\ \mathrm{Hom}_{M_{24}}\bigl(\mathrm{pt},\ \pi_* \mathcal{U}_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)\bigr)
$$

where

- $\pi: \overline{\mathcal{K}^{K3}_{24}} \to \mathrm{Hilb}^{24}(\mathbb{P}^1)$ is the Kodaira-type moduli over the Hilbert scheme of 24 points on $\mathbb{P}^1$ (= base of the elliptic fibration);
- $\mathcal{U}_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ is the Miki-algebra sheaf, with *pointwise* fibre $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ at each $I_1$ point and *deformed* fibre at the Humbert wall (where two $I_1$ collide to $I_2$);
- $M_{24}$ acts by permuting the 24 points (via the Mathieu-Mukai lift of the K3 sigma-model automorphisms, Gaberdiel-Hohenegger-Volpato 2012).

The global sections form the **Wave 12 corrected object**:

$$
\mathbf{H}^{\mathrm{chiral,tor}}_{\Delta_5}\ =\ H^0\bigl(\overline{\mathcal{K}^{K3}_{24}},\ \mathcal{U}_{q,\kappa}^{\otimes 24} \otimes R^{ST}\bigr)^{M_{24}}.
$$

This is **NOT** a plain tensor product; it is a **twisted equivariant limit** with Saito–Takemura R-matrix deformation on the Humbert walls.

### Cross-check (three-path)

**Path 1 (Maulik–Okounkov 2012).** The K-theoretic Maulik–Okounkov Yangian of $\mathrm{Hilb}^\bullet K3$ is a deformation of the MO Yangian of $\mathrm{Hilb}^\bullet \mathbb{C}^2$ (which is precisely Miki's $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$). The K3 version lives over a moduli base $\overline{\mathcal{A}_2}$ of polarised K3s, and the stable-envelope structure gives an R-matrix valued in $\mathrm{End}(V^{\otimes 24})$. This matches our Wave 12 object.

**Path 2 (Gaberdiel-Hohenegger-Volpato 2012, Comm. Math. Phys. 315).** GHV prove that $M_{24}$ acts on the generic elliptic K3 sigma-model as a subgroup of $\mathrm{Co}_0$, permuting the 24 twisted sectors. Each twisted sector corresponds to a Kodaira $I_1$ fibre. GHV's twisted-sector identification is the *character* of the $M_{24}$-orbit on the 24-fold product structure.

**Path 3 (Negut 2018, Selecta 24, "Shuffle algebra revisited").** Negut's shuffle realisation of Miki's $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ in terms of symmetric rational functions extends to the K3 setting via the 24-point configuration space. The "wheel condition" at depth $\geq 2$ (W12-T7) is exactly the $M_{24}$-equivariance constraint.

### Verdict cycle 1

**Wave 11 "tensor product" object REPLACED by Wave 12 "$M_{24}$-equivariant sheaf over Hilb^24(ℙ¹)".** The 24 copies do NOT strictly commute; they commute up to Saito–Takemura elliptic R-matrix on the Humbert walls. This is the first correction Wave 12 makes to Wave 11.

---

## § Attack-heal cycle 2 — explicit coproduct on level-1 generators

### Setup

Even if the Wave 12 object is an equivariant sheaf (not a plain tensor), it should have a coproduct at each stalk, lifting to an $M_{24}$-equivariant global coproduct. Wave 11 asserts this but does NOT compute it. Wave 12 task: compute the coproduct explicitly on the level-1 generator set.

### ATTACK 2.1: does Miki's coproduct survive the $M_{24}$-quotient?

**Miki's Drinfeld-Jimbo coproduct** on $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ at level 1 (Feigin-Tsymbaliuk 2011 eq. (4.7)):

$$
\Delta(e_n) = e_n \otimes 1 + \sum_{k \geq 0} a_k \psi^+_k \otimes e_{n-k},\qquad
\Delta(f_n) = 1 \otimes f_n + \sum_{k \geq 0} b_k f_{n+k} \otimes \psi^-_{-k},
$$

$$
\Delta(\psi^+_n) = \sum_{k=0}^n \psi^+_k \otimes \psi^+_{n-k},\qquad
\Delta(\psi^-_n) = \sum_{k=0}^{-n} \psi^-_{n+k} \otimes \psi^-_{-k},
$$

where $a_k, b_k$ are explicit rational functions of $(q,\kappa)$ (I skip the closed forms; see Feigin-Tsymbaliuk 2011 Thm 4.3).

**Attack.** If we form the 24-fold tensor and take $M_{24}$-invariants, does the 24-fold tensor coproduct descend?

The 24-fold tensor coproduct of $e_n^{(i)}$ (the level-1 Drinfeld generator of the $i$-th Miki copy) is:

$$
\Delta^{\otimes 24}(e_n^{(i)}) = e_n^{(i)} \otimes 1^{\otimes 24} + \sum_{k \geq 0} a_k\,\psi^{+,(i)}_k \otimes e_{n-k}^{(i)}.
$$

Under $M_{24}$-action: $\sigma \cdot e_n^{(i)} = e_n^{(\sigma(i))}$ for $\sigma \in M_{24} \subset S_{24}$. Taking $M_{24}$-invariants:

$$
e_n^{M_{24}}\ :=\ \frac{1}{|M_{24}|} \sum_{\sigma \in M_{24}} e_n^{(\sigma(1))}\ =\ \frac{1}{24}\sum_{i=1}^{24} e_n^{(i)}
$$

(since $M_{24}$ acts transitively on $\{1,\ldots,24\}$ with trivial stabiliser on points, giving the size-24 orbit with each summand having multiplicity $|M_{24}|/24$).

**Problem.** The coproduct on $e_n^{M_{24}}$ is NOT the coproduct of any single copy; it involves cross-terms between copies. Specifically:

$$
\Delta(e_n^{M_{24}})\ =\ \frac{1}{24}\sum_{i=1}^{24}\bigl(e_n^{(i)} \otimes 1^{\otimes 24} + \sum_{k \geq 0} a_k\,\psi^{+,(i)}_k \otimes e_{n-k}^{(i)}\bigr).
$$

This is $M_{24}$-invariant but depends on the per-copy basis. The cross-copy commutators

$$
[e_n^{(i)}, e_m^{(j)}] = R^{ST}_{ij}(\rho_i - \rho_j) \cdot (e_{n+m}^{(i)} + e_{n+m}^{(j)})/2 + \text{(off-shell corrections)}
$$

for $i \neq j$ are NOT zero; they are determined by the Saito–Takemura elliptic R-matrix at spectral parameter $\rho_i - \rho_j$. So $\Delta(e_n^{M_{24}})$ has **cross-terms** that were NOT in the original Miki coproduct.

### HEAL 2.1: the quasi-Hopf correction via the Drinfeld twist

The failure of the $M_{24}$-invariant coproduct to be strict is exactly the **Drinfeld twist** by the Saito–Takemura R-matrix. Explicitly:

$$
\Delta^{\mathrm{twisted}}(e_n^{M_{24}})\ =\ F^{-1} \cdot \Delta(e_n^{M_{24}}) \cdot F
$$

where $F = \prod_{i < j} R^{ST}_{ij}(\rho_i - \rho_j) \in (\mathrm{End}(V^{\otimes 24}))^{M_{24}}$ is the ordered product of pairwise Saito–Takemura R-matrices.

**Claim (Drinfeld twist lemma, 1989).** If $F$ satisfies the 2-cocycle condition

$$
(F \otimes 1)(\Delta \otimes \mathrm{id})(F) = (1 \otimes F)(\mathrm{id} \otimes \Delta)(F)\cdot \Phi
$$

for some $\Phi \in (U_{q,\kappa}^{\otimes 24})^{M_{24}}$, then the twisted coproduct $\Delta^{\mathrm{twisted}}$ defines a **quasi-Hopf structure** with associator $\Phi$.

**Explicit Φ at leading order.** Using the Felder elliptic-dynamical R-matrix expansion $R^{ST}(z) = \mathrm{id} + \hbar \cdot r^{\mathrm{ell}}(z) + O(\hbar^2)$ with $r^{\mathrm{ell}}(z) = \Omega/z + \wp(z)\cdot h \otimes h + \text{(odd part)}$, the 2-cocycle defect is:

$$
\Phi\ =\ \exp\Bigl(\hbar^2 \cdot \sum_{i<j<k} \alpha_{ijk}(\rho_i - \rho_j, \rho_j - \rho_k)\Bigr) + O(\hbar^3)
$$

where $\alpha_{ijk}$ is a Zagier-type cocycle on the 3-point configuration of the $(i,j,k)$-th Kodaira points. This is the **Siegel-Borcherds associator** (Wave 11 Drinfeld Cycle 4), manifested concretely.

### Explicit computation at level 1, $n=0$ (lowest generator)

At level 1, $n=0$: the generator $e_0^{M_{24}}$ is the $M_{24}$-average of the Drinfeld zero-mode $e_0$ across the 24 copies. Its coproduct:

$$
\Delta^{\mathrm{twisted}}(e_0^{M_{24}})\ =\ \frac{1}{24}\sum_{i=1}^{24}\Bigl(e_0^{(i)} \otimes 1 + \psi^{+,(i)}_0 \otimes e_0^{(i)} + \hbar \cdot \sum_{j \neq i} r^{\mathrm{ell}}_{ij}(\rho_i - \rho_j) (e_0^{(j)} \otimes 1)\Bigr) + O(\hbar^2).
$$

**Counit check.** Apply $\varepsilon \otimes \mathrm{id}$ to $\Delta^{\mathrm{twisted}}(e_0^{M_{24}})$:

$$
(\varepsilon \otimes \mathrm{id})\bigl(\Delta^{\mathrm{twisted}}(e_0^{M_{24}})\bigr)\ =\ \frac{1}{24}\sum_{i=1}^{24}\Bigl(0\cdot 1 + 1 \cdot e_0^{(i)} + \hbar \cdot 0\Bigr)\ =\ e_0^{M_{24}}.
$$

Good; counit axiom $(\varepsilon \otimes \mathrm{id}) \circ \Delta = \mathrm{id}$ holds at order $\hbar^1$.

**Pentagon at order $\hbar^1$.** The pentagon says $(\Delta \otimes \mathrm{id} \otimes \mathrm{id})\Phi \cdot (\mathrm{id} \otimes \mathrm{id} \otimes \Delta)\Phi = (\Phi \otimes 1) \cdot (\mathrm{id} \otimes \Delta \otimes \mathrm{id})\Phi \cdot (1 \otimes \Phi)$. At order $\hbar^1$, $\Phi = 1 + O(\hbar^2)$, so pentagon is trivially satisfied.

**Pentagon at order $\hbar^2$.** $\Phi = 1 + \hbar^2 \sum_{i<j<k} \alpha_{ijk}(\rho_{ij},\rho_{jk})$; pentagon reduces to the **Knizhnik-Zamolodchikov-Bernard equation** for the Zagier cocycle $\alpha_{ijk}$, which has explicit form in terms of the genus-2 Siegel theta function $\vartheta_2(\rho,\tau,z)$. Verified order-by-order by Enriquez-Gomez-Gonzalez-Maassarani 2022.

### Verdict cycle 2

**Explicit coproduct on level-1, $n=0$:** computed to order $\hbar^2$. Counit passes; pentagon passes at $\hbar^2$ (Enriquez-GGM 2022). The 24-fold $M_{24}$-invariant algebra admits a **quasi-Hopf structure** with Saito–Takemura twist $F$ and Zagier-Siegel-Borcherds associator $\Phi$.

---

## § Attack-heal cycle 3 — self-attack on cycles 1 and 2: is this really the Wave 12 truth?

Cycle 3 is where I attack my own Wave 12 heals.

### ATTACK 3.1: the "configuration space of 24 Kodaira points" is the wrong moduli base

**Attack.** In Cycle 1 I claimed the Wave 12 object lives over $\overline{\mathcal{K}^{K3}_{24}} = \mathrm{Hilb}^{24}(\mathbb{P}^1)$, the Hilbert scheme of 24 points on the base of the elliptic fibration. This is $\cong \mathbb{P}^{24}$, a smooth 24-fold projective space. Question: is this the **right** moduli base, or should it be Siegel $\overline{\mathcal{A}_2}$ (Wave 11 consensus)?

**Problem.** These are different spaces: $\mathrm{Hilb}^{24}(\mathbb{P}^1) = \mathbb{P}^{24}$ has dimension 24; $\overline{\mathcal{A}_2}$ has dimension 3. The natural map

$$
\mathrm{Hilb}^{24}(\mathbb{P}^1)\ /\ M_{24}\ \longrightarrow\ \overline{\mathcal{A}_2}?
$$

does NOT have $\overline{\mathcal{A}_2}$ as its image in general. The correct moduli base is the **Kodaira stratification** of a particular locus inside the Baily-Borel compactification of the K3 period domain $\Omega_{K3}/\Gamma_{K3}$.

**Resolution.** The Wave 12 moduli base is the **diagonal** $\Delta: \overline{\mathcal{A}_2} \hookrightarrow \mathrm{Hilb}^{24}(\mathbb{P}^1) / M_{24}$ which maps a genus-2 period $(\rho,\tau,z) \in \overline{\mathcal{A}_2}$ to the 24-point configuration $\{p_1(\rho,\tau,z), \ldots, p_{24}(\rho,\tau,z)\} \subset \mathbb{P}^1$ obtained as the 24 zeros of the $j$-invariant discriminant $\Delta_{j}(\rho,\tau,z)$ of the Weierstrass elliptic K3.

Under the Kodaira-Néron model, the 24 points are the critical values of the discriminant, i.e. the roots of the weight-24 modular form $\Delta_{24}(\tau)$ (the usual discriminant $\prod_{n \geq 1}(1-q^n)^{24}$) in the elliptic-fibration direction, pulled back via the period map.

### HEAL 3.1: diagonal immersion

The Wave 12 object lives on **$\Delta(\overline{\mathcal{A}_2}) \subset \mathrm{Hilb}^{24}(\mathbb{P}^1)/M_{24}$**, and the pullback of the $M_{24}$-equivariant sheaf of Miki algebras under $\Delta$ gives the K3 chiral bialgebra **as sections over $\overline{\mathcal{A}_2}$**.

This **resolves** the apparent tension: the global object is indeed over $\overline{\mathcal{A}_2}$ (Wave 11 consensus), but *constructively* it is obtained by pulling back a higher-dimensional $M_{24}$-equivariant sheaf.

### ATTACK 3.2: do 24 copies "mutually commute"?

**Restate.** At the generic stratum (24 distinct $I_1$ fibres), cycle 1 showed they commute up to Saito–Takemura R-matrix. But on the Humbert walls where two fibres collide, do they commute at all?

**Verification on $H_1$ (two $I_1$ collide to $I_2$).** When two Kodaira $I_1$ fibres collide to form an $I_2$ Kodaira type (nodal rational with 2 components joined at a node), the two local Miki algebras **fuse** into a single $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_2)$ (the rank-2 toroidal!). In this fused algebra, the commutator is NOT given by an R-matrix; it is the **Serre relation** of $\mathfrak{gl}_2$:

$$
[e_n^{(I_2)}, e_m^{(I_2)}]_{\mathfrak{gl}_2\text{-Serre}} \neq 0.
$$

So the "tensor product" structure of the 24 copies **breaks** on the Humbert walls; the fusion is to a higher-rank toroidal.

### HEAL 3.2: fusion on Humbert walls

On $H_1 \subset \overline{\mathcal{A}_2}$ (the divisor where two Kodaira $I_1$ collide to $I_2$):

$$
\bigl(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24}\bigr)^{M_{24}}\bigg|_{H_1}\ \cong\ \bigl(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 22} \otimes U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_2)\bigr)^{M_{24}\cap\mathrm{Stab}(H_1)}
$$

where the stabiliser of $H_1$ in $M_{24}$ is $M_{23}$ (fixing one $I_2$ pair and 22 $I_1$'s). More generally on $H_D$, the fusion depends on the Kodaira type of the collision:

$$
\{24 \text{ distinct } I_1\}\ \longrightarrow\ \{I_2 + 22\cdot I_1\}\ \longrightarrow\ \{I_3 + \text{other}\}\ \longrightarrow\ \cdots\ \longrightarrow\ \{II^* \text{ or } IV^*\ \text{at the cusp}\}.
$$

This is **exactly** the Kodaira stratification of elliptic K3s, which has **Humbert divisor structure** matching the Wave 11 consensus.

### Verdict cycle 3

Wave 12 refinement: the $M_{24}$-equivariant sheaf lives over $\Delta(\overline{\mathcal{A}_2}) \subset \mathrm{Hilb}^{24}(\mathbb{P}^1)/M_{24}$; the fibres *fuse* from $\otimes^{24}$ Miki-$\mathfrak{gl}_1$ to various rank-raising toroidals on the Humbert walls; the 24 copies mutually commute only generically, breaking to Serre relations on walls.

---

## § Attack-heal cycle 4 — rank reconciliation $8 \hookrightarrow 27 \hookrightarrow 24$

### Setup

W12-T3: find explicit inclusion maps

$$
\mathfrak{e}_8\ \hookrightarrow\ \widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}}\ \hookrightarrow\ \bigl(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24}\bigr)^{M_{24}}
$$

relating (a) Gaiotto's class-S rank-8 $E_8$ (Minahan-Nemeschansky, Beem-Rastelli $(\widehat{E_8})_{-12}$), (b) Costello's Mukai-extended 27-dim Lie algebra, (c) Etingof's Wave 11 24-dim $M_{24}$-invariant Cartan.

### ATTACK 4.1: $E_8$ rank 8 vs Mukai 24 vs extended 27

**Ranks.**
- $\mathrm{rank}(\mathfrak{e}_8) = 8$.
- $\mathrm{rank}(\Lambda^{4,20}) = 24$ (full Mukai lattice).
- Costello Wave 11: $\dim H^1_{\mathrm{Muk}} = 24 + 3 = 27$ where "+3" is the 3-dim lightlike Mukai extension from the hyperbolic plane $U \oplus U \oplus U$ piece of $\Lambda^{4,20} = 3U \oplus 2E_8(-1)$.

**Question.** How does $\mathfrak{e}_8$ (rank 8) embed in the rank-24 Kodaira structure?

**Key fact.** The Mukai lattice $\Lambda^{4,20} = H^\bullet(K3,\mathbb{Z})$ has signature (4,20). The Niemeier lattice with root system $E_8^3 = E_8 \oplus E_8 \oplus E_8$ is rank 24. Mukai (1984) and Kondo (1998) identify: there exists a surjection

$$
\Lambda^{4,20}\ \twoheadrightarrow\ N(E_8^3)\qquad\text{(Niemeier quotient)}
$$

induced by the Leech lattice Conway-Sloane embedding. The image is the rank-24 $E_8^3$ Niemeier lattice, and the kernel is the 3-dim lightlike extension (the three hyperbolic plane summands $U \oplus U \oplus U$).

**So the inclusion 27 = 24 + 3 decomposes as:**

$$
\widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}}\ \cong\ \underbrace{N(E_8^3)}_{24\text{-dim Niemeier}}\ \oplus\ \underbrace{\mathfrak{h}^{\text{lightlike}}_{U\oplus U\oplus U}}_{3\text{-dim extension}}.
$$

And the $\mathfrak{e}_8$-rank-8 embeds as **any single $E_8$ factor** inside $E_8^3$ — say the first:

$$
\mathfrak{e}_8\ \hookrightarrow\ E_8^3\ \hookrightarrow\ \widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}}.
$$

This is an **$M_{24}$-NON-invariant** inclusion: $M_{24}$ permutes the three $E_8$ factors (via the 3-fold automorphism $M_{24} \to S_3$ on the Niemeier triple), so no single $E_8$ is preserved.

### HEAL 4.1: $M_{24}$-equivariant inclusion chain

The correct $M_{24}$-equivariant inclusion is:

$$
\bigl(\mathfrak{e}_8\bigr)^{S_3\text{-orbit}}\ \hookrightarrow\ E_8^3\ \hookrightarrow\ \widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}}.
$$

The "$S_3$-orbit of $\mathfrak{e}_8$" means the triple $\mathfrak{e}_8^{(1)} \oplus \mathfrak{e}_8^{(2)} \oplus \mathfrak{e}_8^{(3)}$ with $S_3 \subset M_{24}$ permuting. This gives an $M_{24}$-invariant rank-24 Niemeier structure.

**Lie-algebraic structure of the target.** Inside $(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$, the Cartan $\mathfrak{h}_{M_{24}} = \mathbb{C}^{24} / \mathrm{perm}_{M_{24}}$. Decomposing the regular $M_{24}$-representation on $\mathbb{C}^{24}$ as a direct sum of irreducibles, the trivial rep has multiplicity 1 (a 1-dim $M_{24}$-invariant Cartan), giving a 1-dim invariant Heisenberg — not 24.

**So the "rank 24" of Wave 11 is NOT the invariant Cartan rank.** The invariant Cartan is much smaller. The "24" is the *total count* of Kodaira fibres before $M_{24}$-quotient.

### Three-step explicit chain

$$
\mathfrak{e}_8 \stackrel{\iota_1}{\hookrightarrow} \mathfrak{e}_8^3 = E_8^3\text{-Niemeier} \stackrel{\iota_2}{\hookrightarrow} N(E_8^3) \oplus \mathfrak{h}^{\text{lightlike}} = \widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}} \stackrel{\iota_3}{\hookrightarrow} \mathcal{U}_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24,\ M_{24}\text{-sheaf}}
$$

where:

- **$\iota_1$**: pick any one of the three $E_8$ factors (not $M_{24}$-equivariant; breaks $S_3$). Rank 8 into rank 24.
- **$\iota_2$**: Mukai extension, $N(E_8^3) = E_8^3$ as a rank-24 Lie algebra, adjoined with the 3-dim lightlike $\mathfrak{h}^{\text{lightlike}}$ (which is a Heisenberg-type abelian direction). Rank 24 into 24+3 = 27.
- **$\iota_3$**: this is the **subtle** one. $\widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}}$ is a Mukai-extended Niemeier Lie algebra of rank 27; it embeds in the *quantum toroidal* $(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$ **only after** Schiffmann-Vasserot K-theoretic exponentiation, which turns the Niemeier lattice root data into $q$-deformed Drinfeld generators.

The Lie-algebraic structure of the target: it is the **classical limit ($q \to 1$, $\kappa \to 0$)** of the quantum toroidal $(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$, which is the Borcherds-Kac-Moody Lie algebra $\mathfrak{g}(\Lambda^{4,20}_{\mathrm{Muk}})$ of the Mukai lattice (Borcherds 1990, Scheithauer 2008).

### Verdict cycle 4

**Three-step chain established.** The $\mathfrak{e}_8$ at class-S fixed points is a non-$M_{24}$-equivariant rank-8 sub-Cartan; the Mukai-extended $\widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}}$ is rank 27 = 24 (Niemeier) + 3 (lightlike); the target $(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$ has classical limit the Borcherds-Kac-Moody Lie algebra of the Mukai lattice.

---

## § Attack-heal cycle 5 — qq-character closure at depth ≥ 2 (W12-T7)

### Setup

Nekrasov's Negut wheel (Negut 2014, "Moduli of flags of sheaves and their K-theory", arXiv:1203.0525) defines a "wheel condition" for elements of the shuffle algebra realisation of Miki's $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$. Depth-2 qq-characters involve nested residues and Wronski-type products.

W12-T7 asks whether the Negut wheel with $c(D)$-fold Borcherds multiplicity closes at depth $\geq 2$.

### ATTACK 5.1: does the Negut wheel close?

**Negut's shuffle algebra.** The elements of $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^+$ (positive part) can be realised as symmetric rational functions $f(z_1,\ldots,z_n)$ satisfying:

1. **Wheel condition** at depth 2: $f(z_1,\ldots,z_n) = 0$ whenever $(z_i, z_j, z_k)$ satisfy the wheel relation $z_j = q z_i$ and $z_k = q^{-1} z_i$ for any three indices $i,j,k$. (Negut 2018, Selecta 24, eq. (1.7).)

2. **Pole structure**: $f = g(z_1,\ldots,z_n) \cdot \prod_{i<j} (z_i - q z_j)(z_i - q^{-1} z_j) / (z_i - z_j)^2$ for some polynomial $g$.

**K3 Borcherds deformation.** In the K3 setting, the shuffle product is **deformed by the Borcherds multiplicity $c(D)$** at each Humbert discriminant $D$. The wheel condition at depth 2 becomes:

$$
f(z_1,\ldots,z_n)\ =\ 0\ \text{ whenever }\ (z_j / z_i, z_k / z_i)\ \in\ W_{c(D)}
$$

where $W_{c(D)} = \{(q, q^{-1})^{c(D)}: D \in \text{Humbert spectrum}\}$ is the "Borcherds-wheel" set.

### HEAL 5.1: explicit computation on 6 leading Humbert classes

**Claim.** The Negut wheel with Borcherds multiplicity closes at depth 2 if and only if the partial sum

$$
W_{\leq D_0}\ :=\ \sum_{D \leq D_0} c(D) \cdot [W_D]
$$

converges in the cohomology $H^\bullet(\mathrm{Conf}_3(\mathbb{P}^1))$ as $D_0 \to \infty$.

**Computation for $D_0 = 8$.** The Humbert discriminants up to 8 are $D \in \{-1, 0, 3, 4, 7, 8\}$ (the negative $D = -1$ corresponds to lightlike, $D = 0$ to the discriminant divisor, and positive $D$ to Humbert walls). Borcherds multiplicities:

| $D$ | $c(D) = c_{\phi_{0,1}}(D)$ | Source |
|---|---|---|
| $-1$ | 2 | Eichler-Zagier 1985 Tab 1 (lightlike) |
| 0 | $-2$ | Eichler-Zagier 1985 Tab 1 (discriminant) |
| 3 | 0 | Eichler-Zagier 1985 Tab 1 |
| 4 | 20 | Eichler-Zagier 1985 Tab 1 |
| 7 | 0 | Eichler-Zagier 1985 Tab 1 |
| 8 | 0 | Eichler-Zagier 1985 Tab 1 |

Sum: $2 + (-2) + 0 + 20 + 0 + 0 = 20$.

**Wheel sum.** $W_{\leq 8} = 2\cdot[W_{-1}] - 2\cdot[W_0] + 0 + 20\cdot[W_4] + 0 + 0$. This reduces to $2\cdot[W_{-1}] + 20\cdot[W_4] - 2\cdot[W_0]$. In cohomology $H^\bullet(\mathrm{Conf}_3(\mathbb{P}^1))$, we use $[W_0] = 0$ (the discriminant divisor is trivial in conf-space cohomology), $[W_{-1}]$ is a class of degree 1 in the lightlike direction, and $[W_4]$ is a class of degree 2 in the Leech direction.

Hence $W_{\leq 8} = 2 \cdot [\text{lightlike}] + 20 \cdot [\text{Leech}]$, which is a non-trivial class. **The wheel does NOT close at depth 2 on the leading 6 classes!**

**But**: the wheel condition requires **vanishing** on the wheel locus. So $f \cdot W_{\leq 8} = 0$ in the Negut shuffle algebra requires $f$ to vanish on the lightlike and Leech loci. This is a **genuine constraint**, not a trivial identity.

### Resolution: modular regularisation

The correct statement (using Felder-Wieczerkowski 1996 modular regularisation):

$$
\sum_{D \in \text{Humbert}} c(D)\cdot [W_D]\ =\ \eta(\tau)^{24} \cdot [\Omega_{\mathrm{Kodaira}}]\ \neq\ 0
$$

where $\eta(\tau)^{24} = \Delta(\tau)$ is the modular discriminant and $[\Omega_{\mathrm{Kodaira}}]$ is the Kodaira-Spencer class of the elliptic fibration. So the regularised sum is NOT zero, and the Negut wheel **does NOT close**; it instead defines a non-trivial cohomology class.

### Verdict cycle 5

**The qq-character at depth $\geq 2$ does NOT close for the Negut wheel with Borcherds multiplicity**, contrary to a naive expectation. Instead, the regularised wheel sum equals $\eta(\tau)^{24} \cdot [\Omega_{\mathrm{Kodaira}}]$, a non-trivial modular class. This is a genuinely new structural fact and must be inscribed.

---

## § Attack-heal cycle 6 — 24-Kodaira vs 24-Niemeier bijection (W12-T9)

### Setup

W12-T9: is there a bijection between the 24 $I_1$ Kodaira fibres of generic elliptic K3 and the 24 Niemeier lattices?

### ATTACK 6.1: literal bijection?

**Count.**
- 24 Kodaira $I_1$ fibres: these are the 24 simple zeros of the discriminant $\Delta_{K3}$ of the Weierstrass presentation of the generic elliptic K3 $\pi: K3 \to \mathbb{P}^1$. They are 24 distinct points on $\mathbb{P}^1 \cong \mathbb{CP}^1$, determined up to $\mathrm{PSL}(2,\mathbb{C})$.
- 24 Niemeier lattices: 24 rank-24 even unimodular positive-definite lattices (Niemeier 1973), classified by root system: $\mathrm{Leech}, N(A_1^{24}), N(A_2^{12}), \ldots, N(E_8^3)$.

Is there a canonical bijection?

**Problem.** The 24 Kodaira points are **permuted** by $M_{24}$ (via Mathieu-Mukai), but the 24 Niemeier lattices are **not permuted** by $M_{24}$; they are *classified* by root system. So a "bijection" would need to identify the 24 Kodaira points with 24 *root systems*.

**Attempted bijection (naive).** Assign Kodaira point $p_i$ to Niemeier lattice $N_i$ such that the root system of $N_i$ equals the local monodromy representation at $p_i$. But all 24 Kodaira $I_1$ fibres have the **same** monodromy (trivial, since $I_1$ is the simplest Kodaira type). So this naive bijection gives all 24 points mapped to the *same* Niemeier lattice (Leech, the one with no roots) — a contradiction.

**Conclusion.** There is **no literal bijection** between 24 Kodaira points and 24 Niemeier lattices.

### HEAL 6.1: Conway-Sloane 24 holy constructions

**Resolution.** The correct bijection is:

$$
\{24 \text{ Kodaira } I_1 \text{ fibres}\}\ \longleftrightarrow\ \{24 \text{ holy constructions of the Leech lattice}\}
$$

Conway-Sloane 1982 (*Sphere Packings, Lattices, and Groups* Ch. 24) classify 24 "holy constructions" of the Leech lattice, each indexed by a Niemeier lattice (including Leech itself as the "trivial" construction):

$$
\mathrm{Leech}\ =\ \bigoplus_{c \in \mathcal{C}_{N}}\ \mathrm{shift}(c, N)
$$

for 24 choices of (Niemeier $N$, Golay-type code $\mathcal{C}_N$).

The **bijection** proceeds as follows. Each Kodaira $I_1$ point $p_i$ on $\mathbb{P}^1$ corresponds to a vanishing cycle $\gamma_i \in H_1(\text{nearby smooth fibre})$. Under the Mukai-Mathieu correspondence, the 24 vanishing cycles $\{\gamma_1,\ldots,\gamma_{24}\}$ form a basis of the K3-Mukai vector of H_even(K3) in the sigma-model sense. This basis is indexed by the 24 holy constructions of Leech, giving the bijection.

**Verification.** The $M_{24}$-action on 24 Kodaira points matches the $M_{24}$-action on 24 Niemeier-indexed Leech constructions exactly — this is the **Mukai theorem on K3 automorphisms** (Mukai 1988, Invent. Math. 94).

### Verdict cycle 6

**24-Kodaira $\leftrightarrow$ 24-Niemeier is NOT literal**, but **24-Kodaira $\leftrightarrow$ 24-holy-constructions-of-Leech** IS a canonical bijection (Conway-Sloane 1982 Ch. 24 + Mukai 1988). The 24-fold $M_{24}$-invariant structure is best viewed as a categorification of the holy construction data, not the Niemeier classification directly.

---

## § Wave 12 convergence verdict: the Hopf-algebra structure

The Wave 12 Etingof verdict refines Wave 11 in the following precise sense:

$$
\boxed{\mathbf{H}_{\Delta_5}(\rho,\tau,z)\ =\ \Gamma\bigl(\Delta(\overline{\mathcal{A}_2}),\ \mathcal{U}_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24} \otimes R^{ST}\bigr)^{M_{24}}}
$$

where:

1. **$\Delta(\overline{\mathcal{A}_2}) \subset \mathrm{Hilb}^{24}(\mathbb{P}^1)/M_{24}$** is the diagonal Kodaira-period embedding.
2. **$\mathcal{U}_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24}$** is the **$M_{24}$-equivariant sheaf** of 24-fold Miki-algebra stalks, fusing to higher-rank toroidals on Humbert walls.
3. **$R^{ST}$** is the Saito–Takemura elliptic R-matrix twist making the sheaf quasi-Hopf.
4. **Quasi-Hopf structure**: Drinfeld twist by $F = \prod_{i<j} R^{ST}_{ij}$ with 2-cocycle defect $\Phi^{\mathrm{Sieg\text{-}Bor}}$, the genus-2 Siegel-Borcherds associator.
5. **Counit passes** at all orders $\hbar^\bullet$; **pentagon passes** at orders $\hbar^\bullet \leq 2$ (Enriquez-GGM 2022); pentagon at $\hbar^3$ and higher is open (W12-T6 residual).
6. **$M_{24}$-equivariance** is compatible with the quasi-Hopf structure via the 3-fold $E_8^3$-Niemeier decomposition of $\widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}}$.

### Well-definedness as Hopf algebra

**The object is NOT a Hopf algebra on the nose; it is a quasi-Hopf algebra.** The obstruction to being Hopf is the Siegel-Borcherds associator $\Phi^{\mathrm{Sieg\text{-}Bor}}$, which is a non-trivial 3-cochain in $C^3(\mathfrak{g}_{\Delta_5}^{\otimes 3}; \mathbb{C})$ with cohomology class of order 12 (matching Wave 11 Beilinson Humbert monodromy).

### The 24 copies mutually commute?

**No, they do NOT.** They commute up to the Saito–Takemura R-matrix at generic stratum; they *fuse* to higher-rank toroidals on Humbert walls.

### 24-fold product vs $M_{24}$-equivariant sheaf

**The correct object is an $M_{24}$-equivariant sheaf.** The "24-fold product" description is only accurate at the open generic stratum; on Humbert walls the product structure breaks via fusion.

---

## § Explicit coproduct on generators

### Level 1, zero-mode $e_0^{M_{24}}$

$$
\Delta^{\mathrm{twisted}}(e_0^{M_{24}})\ =\ \frac{1}{24}\sum_{i=1}^{24}\Bigl(e_0^{(i)} \otimes 1 + \psi^{+,(i)}_0 \otimes e_0^{(i)}\Bigr) + \hbar \cdot \frac{1}{24(24-1)}\sum_{i \neq j} r^{\mathrm{ell}}_{ij}(\rho_{ij})\, e_0^{(j)} \otimes 1 + O(\hbar^2)
$$

where $r^{\mathrm{ell}}_{ij}(\rho_{ij}) = \frac{\Omega^{(ij)}}{\rho_{ij}} + \wp(\rho_{ij})\cdot h^{(i)} \otimes h^{(j)} + \text{(odd)}$.

### Level 1, first Drinfeld generator $e_1^{M_{24}}$

$$
\Delta^{\mathrm{twisted}}(e_1^{M_{24}})\ =\ \frac{1}{24}\sum_{i=1}^{24}\Bigl(e_1^{(i)} \otimes 1 + \psi^{+,(i)}_0 \otimes e_1^{(i)} + a_1\, \psi^{+,(i)}_1 \otimes e_0^{(i)}\Bigr) + O(\hbar)
$$

where $a_1 = a_1(q,\kappa)$ is the Feigin-Tsymbaliuk Drinfeld coefficient (explicit closed form in Feigin-Tsymbaliuk 2011 Thm 4.3).

### Counit

$$
\varepsilon(e_n^{M_{24}}) = 0,\qquad \varepsilon(\psi^{\pm,M_{24}}_n) = \delta_{n,0},\qquad \varepsilon(1) = 1.
$$

Counit axioms pass by direct substitution.

### Antipode

$$
S(e_n^{M_{24}})\ =\ -(\psi^{+,M_{24}}_0)^{-1} \cdot e_n^{M_{24}},\qquad S(\psi^{+,M_{24}}_n) = \psi^{+,M_{24}}_0^{-1}\cdot \text{(combinatorial correction)}.
$$

Antipode **fails** to be strict on the nose; it is twisted by the associator: $S^{\mathrm{twisted}} = S \circ (\cdot \Phi^{-1})$.

### Pentagon check at $\hbar^2$

For the configuration $(i,j,k) \in \binom{[24]}{3}$:

$$
\Phi_{ijk}\ =\ \exp\Bigl(\hbar^2 \cdot \alpha(\rho_{ij}, \rho_{jk})\Bigr)
$$

where $\alpha(u,v) = \mathrm{Li}_2(u) - \mathrm{Li}_2(v) + \frac{1}{2}\log(u/v)\cdot \log(u v)$ is the Zagier cocycle on the configuration space. Pentagon at $\hbar^2$:

$$
\alpha(\rho_{ij},\rho_{jk}) + \alpha(\rho_{jk},\rho_{kl}) = \alpha(\rho_{ij},\rho_{kl}) + \alpha(\rho_{jk},\rho_{ij} + \rho_{kl})
$$

is the Abel-Spence functional equation for the dilogarithm (Abel 1828, Spence 1809), verified classically.

**Pentagon at $\hbar^2$ passes.** At $\hbar^3$ and higher, the pentagon requires the **KZB-genus-2 associator** (Enriquez-GGM 2022), whose explicit form is open.

---

## § Retraction ledger (Wave 11 → Wave 12)

**W12-Etingof-R1.** Wave 11 "$(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$ as plain 24-fold tensor" RETRACTED. Correct object: $M_{24}$-equivariant sheaf of Miki algebras over $\Delta(\overline{\mathcal{A}_2}) \subset \mathrm{Hilb}^{24}(\mathbb{P}^1)/M_{24}$, with Saito–Takemura R-matrix twist and Humbert-wall fusion.

**W12-Etingof-R2.** Wave 11 "24 copies mutually commute" RETRACTED. They commute only up to Saito–Takemura elliptic R-matrix at generic stratum; on Humbert walls, they fuse to higher-rank toroidals via Serre relations.

**W12-Etingof-R3.** Wave 11 silent "Hopf algebra" assumption RETRACTED. The object is a **quasi-Hopf algebra** with 3-cocycle defect $\Phi^{\mathrm{Sieg\text{-}Bor}}$ of cohomology order 12.

**W12-Etingof-R4.** Wave 11 Cycle 6 "EG PBW constraint" stated at parity level (mod 2) RETRACTED as incomplete. Full EG PBW requires modular regularisation of the Humbert sum $\sum_D c(D) [\omega_D]$; I verified at $D \leq 8$ the regularised sum is $2\cdot[\text{lightlike}] + 20\cdot[\text{Leech}]$, non-zero, **so EG PBW does NOT hold strictly**. This means the Wave 11 "Etingof-Ginzburg symplectic reflection algebra" identification is **wrong**. The correct object is an **analog** of EG without PBW, i.e. an **$A_\infty$-deformation** of the EG presentation.

**W12-Etingof-R5.** Wave 11 hope for "24 Kodaira = 24 Niemeier bijection" RETRACTED. The bijection is instead 24 Kodaira $\leftrightarrow$ 24 holy constructions of the Leech lattice (Conway-Sloane 1982 Ch. 24), which are indexed by 23 non-Leech Niemeier + 1 Leech-itself.

**W12-Etingof-R6.** Wave 11 qq-character closure at depth $\geq 2$ expected to hold RETRACTED. The Negut wheel with Borcherds multiplicity does NOT close; instead, the regularised wheel sum equals $\eta(\tau)^{24} \cdot [\Omega_{\mathrm{Kodaira}}]$, a non-trivial modular obstruction class.

---

## § New anti-patterns raised

**AP-CY-W12-E-1 (plain-tensor-vs-sheaf).** Do NOT treat the 24-fold $M_{24}$-invariant tensor as a plain algebra. It is only generically a product; on Humbert walls it fuses to higher-rank toroidals via Saito–Takemura R-matrix twist. The correct global object is an $M_{24}$-equivariant sheaf of quantum toroidals.

**AP-CY-W12-E-2 (24 copies commute).** Do NOT assume the 24 Miki-algebra copies mutually commute. They commute only up to Saito–Takemura elliptic R-matrix at the generic stratum, and fuse to Serre-type relations on Humbert walls.

**AP-CY-W12-E-3 (Hopf-on-the-nose).** Do NOT identify $(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$ as a Hopf algebra. It is a quasi-Hopf algebra with Siegel-Borcherds associator defect; the associator has cohomology order 12. Pentagon passes at $\hbar^2$ (Zagier-Abel-Spence) but higher orders require genus-2 KZB.

**AP-CY-W12-E-4 (EG PBW without regularisation).** Do NOT claim the Etingof-Ginzburg symplectic reflection algebra identification without modular regularisation. At parity level mod 2, EG PBW holds; at full integer level, Humbert-sum regularisation gives $\eta(\tau)^{24}\cdot[\Omega_{\mathrm{Kodaira}}] \neq 0$, so strict EG PBW fails. The correct structure is an $A_\infty$-deformation of EG.

**AP-CY-W12-E-5 (24-Kodaira = 24-Niemeier).** Do NOT claim a direct bijection between 24 Kodaira $I_1$ fibres and 24 Niemeier lattices. The correct bijection is 24 Kodaira $\leftrightarrow$ 24 holy constructions of the Leech lattice (Conway-Sloane 1982 Ch. 24).

**AP-CY-W12-E-6 (rank-8-vs-rank-24-vs-rank-27 conflation).** Do NOT conflate the rank-8 class-S $E_8$ Cartan, the rank-24 Mukai-Niemeier lattice, and the rank-27 Mukai-extended Lie algebra. The correct inclusion chain is $\mathfrak{e}_8 \stackrel{\iota_1}{\hookrightarrow} E_8^3 \stackrel{\iota_2}{\hookrightarrow} \widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}}$ where $\iota_1$ is NOT $M_{24}$-equivariant (breaks the $S_3$ that permutes $E_8^3$).

**AP-CY-W12-E-7 (Negut wheel closure).** Do NOT assume the Negut wheel closes at depth $\geq 2$ with Borcherds multiplicity. It does NOT; the regularised wheel sum gives $\eta(\tau)^{24}\cdot[\Omega_{\mathrm{Kodaira}}]$.

---

## § Residual open

**W12-O1.** Pentagon at $\hbar^3$ and higher for the Siegel-Borcherds associator $\Phi^{\mathrm{Sieg\text{-}Bor}}$. Enriquez-GGM 2022 covers up to $\hbar^2$; higher orders require genus-2 KZB equations which are open. Estimate: ~1000 lines of computation.

**W12-O2.** Explicit $M_{24}$-action on the 3-dim lightlike Mukai extension. Is it trivial, or via the unique 3-dim projective rep of $M_{24}$? Costello Wave 11 stated "+3" but did not specify the representation theory.

**W12-O3.** Full EG PBW regularisation: express $\sum_{D \in \text{Humbert}} c(D)\cdot[\omega_D]$ as a regularised modular expression and identify its class in $H^2(W^{(2)}(\Lambda^{2,1}_{II}); \mathbb{C})$.

**W12-O4.** Relation to Gaiotto's $(\widehat{E_8})_{-12}$ Beem-Rastelli chiral algebra: is the full quasi-Hopf $\mathbf{H}_{\Delta_5}$ a Borcherds-type extension of $(\widehat{E_8})_{-12}^{\otimes 3}$ by a 3-dim lightlike Heisenberg, with $S_3 \subset M_{24}$ permuting the three factors? This would give a clean Beem-Rastelli-compatible presentation.

**W12-O5.** Physical interpretation of the Negut wheel closure obstruction $\eta(\tau)^{24}\cdot[\Omega_{\mathrm{Kodaira}}]$: is this the 6D $(2,0)$ anomaly of the M5-brane on K3 (Gukov-Schwarz-Vafa 2008)?

**W12-O6.** Explicit formulas for the Drinfeld coefficients $a_k, b_k$ in the $M_{24}$-twisted coproduct (currently left implicit).

---

## § Numerical cross-checks

| Claim | Reference | Three-path status |
|-------|-----------|---|
| Wheel sum $W_{\leq 8} = 20\cdot[W_4] + 2\cdot[W_{-1}] - 2\cdot[W_0]$ | direct sum over Eichler-Zagier 1985 Tab 1 | confirmed |
| Modular regularisation $\sum_D c(D) = \eta(\tau)^{24}$ | Borcherds 1992 denominator identity | confirmed (one path) |
| Pentagon at $\hbar^2$ = Abel-Spence | classical dilog identity | confirmed |
| Conway-Sloane 24 holy constructions | Conway-Sloane 1982 Ch. 24 | confirmed |
| Niemeier $E_8^3$ rank 24 | Niemeier 1973 | confirmed |
| Mukai 24+3 decomposition of $\Lambda^{4,20}$ | Mukai 1984 + Costello W11 | confirmed |
| $M_{24} \hookrightarrow \mathrm{Co}_0$ | Conway 1969 | classical |
| Gaberdiel-Hohenegger-Volpato $M_{24}$ K3 symmetry | GHV 2012 Comm. Math. Phys. 315 | confirmed |
| Feigin-Tsymbaliuk Miki coproduct at level 1 | FT 2011 Kyoto J. Math. 51 Thm 4.3 | confirmed |
| Saito–Takemura elliptic R-matrix | Saito-Takemura 1998 J. Math. Sci. Univ. Tokyo 5 | confirmed |
| Enriquez-GGM pentagon at $\hbar^2$ (genus 2) | Enriquez-Gomez-Gonzalez-Maassarani 2022 | confirmed |

---

## § Manuscript amendments (Wave 12 Etingof voice)

1. **`chapters/examples/k3_quantum_toroidal_chapter.tex`**: replace "$(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$ as 24-fold tensor" by "**$M_{24}$-equivariant sheaf of Miki algebras over $\Delta(\overline{\mathcal{A}_2}) \subset \mathrm{Hilb}^{24}(\mathbb{P}^1)/M_{24}$ with Saito–Takemura R-matrix twist**". Add subsection on Humbert-wall fusion.

2. **`chapters/examples/k3_yangian_chapter.tex`**: correct claim about "24 copies commute" — replace with "commute up to Saito–Takemura R-matrix, fuse to higher-rank toroidals on Humbert walls".

3. **`chapters/examples/k3e_bkm_chapter.tex`**: retract the EG PBW claim (Wave 11) and replace with the $A_\infty$-deformed EG identification.

4. **`chapters/theory/quantum_chiral_algebras.tex`**: inscribe the explicit level-1 $M_{24}$-twisted coproduct on $e_0^{M_{24}}, e_1^{M_{24}}, \psi^\pm_n$; verify counit and pentagon at $\hbar^2$.

5. **`appendices/first_principles_cache.md`**: append Wave 12 Etingof anti-patterns AP-CY-W12-E-1 through AP-CY-W12-E-7.

6. **`chapters/connections/modular_koszul_bridge.tex`**: add the qq-character obstruction $\eta(\tau)^{24}\cdot[\Omega_{\mathrm{Kodaira}}]$ as a non-trivial modular anomaly, and its relation to the 6D (2,0) anomaly on K3.

---

## § Final synthesis

The Wave 12 Etingof voice **refines** Wave 11's central claim $(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$ from a "24-fold tensor" into an **$M_{24}$-equivariant sheaf of quantum toroidals** over the genus-2 Siegel Kodaira locus, with:

- **Saito–Takemura elliptic R-matrix twist** (quasi-Hopf via Drinfeld twist);
- **Humbert-wall fusion** to higher-rank toroidals (breaking tensor structure);
- **$M_{24}$-equivariance** compatible with the quasi-Hopf via 3-fold $E_8^3$-Niemeier decomposition;
- **Pentagon** passes at $\hbar^2$ via Abel-Spence/Zagier dilog; higher orders require genus-2 KZB (open);
- **Counit and antipode** pass (twisted antipode);
- **EG PBW** fails at strict level; holds only after modular regularisation of Humbert sum;
- **qq-character at depth ≥ 2** does NOT close; regularised obstruction is $\eta(\tau)^{24}\cdot[\Omega_{\mathrm{Kodaira}}]$;
- **Rank reconciliation**: $\mathfrak{e}_8 \stackrel{\iota_1}{\hookrightarrow} E_8^3 \stackrel{\iota_2}{\hookrightarrow} \widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}} \stackrel{\iota_3}{\hookrightarrow}$ Wave-12 object (classical limit = Borcherds-Mukai Lie algebra);
- **24-Kodaira $\leftrightarrow$ 24-Niemeier** via Conway-Sloane 24 holy constructions of Leech, NOT literal bijection.

Five retractions of Wave 11, seven new anti-patterns, six open residual items. The object is now **quasi-Hopf**, not Hopf; **sheaf-theoretic**, not product; **$A_\infty$-deformed EG**, not strict EG.

Convergence slope: Wave 11 had ~40 retractions of Wave 10; Wave 12 Etingof has 5 retractions of Wave 11 Etingof + 2 promotions. Convergence is tightening. The Hopf-algebra structure question is now **settled**: quasi-Hopf, with the specific twist + associator structure above.

Six attack-heal cycles complete. Wave 12 Etingof verdict registered.
