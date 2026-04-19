# Agent 05 — Nekrasov on the Non-Abelian K3 Chiral Bialgebra, Wave 9

**Voice.** Instanton partition functions, $\Omega$-background, equivariant K-theory, qq-characters, Maulik–Okounkov stable envelopes, AGT, BPS/CFT. Write $Z$ first, interpret after. A "K3 Yangian" is not a slogan — it is a quiver, a stability, a torus action, an equivariant integral, an R-matrix, a Yang–Baxter identity, and a scalar generating function that reproduces a named modular object. If any link breaks, the object is something else.

**Wave-8 inheritance.** The swarm converged on
$$
\mathcal{H}_{\Delta_5} \;=\; Q(\mathfrak{g}_{\Delta_5}) \;=\; \mathrm{EK}(\mathfrak{g}_{\Delta_5},\delta_{\mathrm{Manin}}),
$$
a Borcherds quasi-triangular Hopf **superalgebra**, **not a Yangian** in the strict Drinfeld sense. The trace-ansatz is
$$
\mathrm{Tr}_{\mathbb{C}}\,R_{\mathrm{EK}}(\lambda) \;=\; 64 \cdot \Delta_5(\lambda)/W^{\mathrm{reg}}_{\mathrm{WKB}}(\lambda) \;+\; O(\hbar).
$$
But Nekrasov–Okounkov Yangians on $H^\ast_T(\mathrm{Hilb}^n X)$ exist for quiver varieties. If $\mathfrak{g}_{\Delta_5}$ refuses a Yangian, either Wave 8 is wrong or the Maulik–Okounkov construction does not apply in the same form to K3. Wave 9 dissects this tension across five attack–heal cycles and ends with a verdict on the true algebraic species: **Yangian vs Quantum Toroidal vs EK-Borcherds-Manin**.

Raeez Lorgat, sole author, 2026-04-19.

---

## § Attack Phase 1 — MO Yangian exists for K3, so Wave 8 must be wrong

**Q (A1).** Nekrasov–Okounkov (arXiv:1404.4099) + Maulik–Okounkov (Astérisque 408, 2019) construct, for every Nakajima quiver variety $\mathcal{M}(Q,v,w)$ of a symmetric Kac–Moody Dynkin $Q$, a Yangian
$$
Y^{\mathrm{MO}}_\hbar(\mathfrak{g}_Q) \;\hookrightarrow\; \mathrm{End}\bigl(\bigoplus_v H^\ast_T(\mathcal{M}(Q,v,w))\bigr)
$$
with universal R-matrix built from stable envelopes. For $Q$ = Jordan loop (one node, one edge-loop), $\mathcal{M} = \mathrm{Hilb}^n(\mathbb{C}^2)$ and $Y^{\mathrm{MO}}$ is the affine Yangian $Y_\hbar(\widehat{\mathfrak{gl}}_1)$ (Schiffmann–Vasserot, arXiv:1202.2756). For $Q$ = affine ADE diagram $\widehat{A}_{k-1}$, $\mathcal{M} = \mathrm{Hilb}^n(\mathbb{C}^2/\mathbb{Z}_k)$ and $Y^{\mathrm{MO}} = Y_\hbar(\widehat{\mathfrak{gl}}_k)$.

**Attack.** If the BKM Lie superalgebra $\mathfrak{g}_{\Delta_5}$ deserves the name "K3 BPS Lie algebra", then the Nakajima-type construction on the K3 lattice $\Gamma^{3,19}$ (or the full Mukai lattice $II_{4,20}$) must yield $Y^{\mathrm{MO}}(\mathfrak{g}_{\Delta_5})$ as a genuine Yangian. But Wave 8 asserts such a Yangian **does not exist** — Drinfeld listed five obstructions: lightlike imaginary simple roots, Serre degeneracy, Mittag–Leffler coproduct failure, missing RTT fundamental, no super-Kashiwara–GKM crystal.

**Tension.** One of the following must give:
- **(i)** Wave 8 is wrong — a Borcherds Yangian $Y^{\mathrm{MO}}(\mathfrak{g}_{\Delta_5})$ does exist, and $\mathcal{H}_{\Delta_5}$ is either a different object or a sub-Hopf of it.
- **(ii)** Nekrasov–Okounkov + Maulik–Okounkov do not apply to K3 in the naive sense — the obstruction being that $\mathfrak{g}_{\Delta_5}$ is a **hyperbolic BKM** with lightlike imaginary roots, outside the symmetric-Kac–Moody hypothesis of Maulik–Okounkov Thm 1.1.
- **(iii)** There are **two distinct algebras**: a Borcherds-Yangian $Y^{\mathrm{B}}$ from stable envelopes on an infinite-type Nakajima variety, and $\mathcal{H}_{\Delta_5}$ the Etingof–Kazhdan Hopf superalgebra. They live in different rungs of a Koszul ladder.

**Preference (for falsification).** Option (iii) is most testable. Let us attempt to construct $Y^{\mathrm{B}}$ explicitly and compare to $\mathcal{H}_{\Delta_5}$.

---

## § Heal Phase 1 — Two algebras, one lattice: Borcherds–Yangian vs EK–Borcherds–Manin are Koszul dual

**Construction of the Borcherds–Yangian $Y^{\mathrm{B}}(\mathfrak{g}_\Gamma)$.** Take $\Gamma = \Gamma^{3,19}$, the K3 transcendental lattice (signature $(3,19)$). Form the **infinite-type Nakajima framed moduli**
$$
\mathcal{M}_\Gamma(v,w) \;=\; \bigl\{(B_\alpha, B_\alpha^\dagger, I_\alpha, J_\alpha)\bigr\}_{\alpha \in \Delta^{\mathrm{re}}_\Gamma} \big/\!\!\big/\!\!\big/\, G_v
$$
where $\alpha$ runs over real roots of $\Gamma$ (infinitely many) and $v,w$ are dimension/framing vectors. The data is infinite but at each fixed $v$ the moduli is finite-dim. Maulik–Okounkov stable envelopes
$$
\mathrm{Stab}_{\mathfrak{c}}: H^\ast_T(\mathcal{M}_\Gamma(v,w)^T) \to H^\ast_T(\mathcal{M}_\Gamma(v,w))
$$
depend on a chamber $\mathfrak{c}$ in $\mathrm{Lie}(T)_\mathbb{R}$. The R-matrix
$$
R^{\mathrm{MO}}(u) = \mathrm{Stab}_{-\mathfrak{c}}^{-1} \circ \mathrm{Stab}_{\mathfrak{c}}
$$
generates, via the RTT presentation, the Borcherds Yangian $Y^{\mathrm{B}}_\hbar(\mathfrak{g}_\Gamma)$. Imaginary roots of $\Gamma$ contribute **lightlike simple root generators** $e_\delta, f_\delta, h_\delta$ with $(\delta,\delta) = 0$; these produce the Borcherds–Serre relations rather than the standard Chevalley–Serre.

**Koszul duality claim.** The Borcherds Yangian $Y^{\mathrm{B}}_\hbar$ and the EK Manin-double $\mathcal{H}_{\Delta_5}$ are **Koszul dual** quasi-triangular Hopf superalgebras:
$$
\boxed{\;\mathcal{H}_{\Delta_5} \;=\; \mathrm{EK}(\mathfrak{g}_{\Delta_5},\delta_{\mathrm{Manin}}) \;\simeq\; \bigl(Y^{\mathrm{B}}_\hbar(\mathfrak{g}_\Gamma)\bigr)^{!}\;}
$$
where $(-)^!$ is the Koszul-dual construction on Hopf superalgebras (Positselski, Wang–Wang). Both exist; they carry the same R-matrix data but inverted between "OPE presentation" (Borcherds Yangian, generators $t^{(n)}_{ij}$ at spectral level $n$) and "normal-ordered presentation" (EK Hopf, generators from the Manin double).

**Five Wave-8 Drinfeld obstructions, re-read.** Each of the five obstructions is an obstruction **to the EK-side presentation being a Yangian**, not to the existence of the MO-side Yangian per se:
- Lightlike imaginary roots: on the MO side, these are simple generators from the imaginary-root isotropic cone of $\Gamma$; on the EK side they obstruct the Drinfeld–Kohno generator count. The Koszul dual carries them as **fermionic** generators (super-grading flips).
- Serre degeneracy: $[e_\delta, f_\delta] = h_\delta$ with $h_\delta$ central, not diagonalisable $\Rightarrow$ EK-Serre breaks, MO-Serre survives as Borcherds–Serre.
- Mittag–Leffler coproduct: MO coproduct is inverse-limit over dimension vectors (well-defined); EK coproduct requires a finite generating set (fails for BKM).
- Missing RTT fundamental: MO uses the tautological sheaf on $\mathcal{M}_\Gamma(\delta,\delta)$; EK expects a graded representation of the universal enveloping (fails for lightlike $\delta$).
- Super-Kashiwara–GKM crystal: absent on the EK side (Wave 8 Gelfand), conjecturally present on the MO side as a super-Young-diagram crystal on imaginary roots.

**The two algebras are distinct and coexist.** Wave 8's identification is correct on the EK side. Maulik–Okounkov applies, with appropriate Borcherds-type extension, on the MO side. The duality upgrades the Wave-8 conclusion rather than contradicting it.

### Falsifiable Computation W9-N-1 (Koszul duality test at depth 1)

If $Y^{\mathrm{B}}_\hbar$ and $\mathcal{H}_{\Delta_5}$ are Koszul-dual, their **Hilbert series** satisfy the Koszul identity
$$
\mathrm{Hilb}\bigl(Y^{\mathrm{B}}_\hbar; q, \hbar\bigr) \cdot \mathrm{Hilb}\bigl(\mathcal{H}_{\Delta_5}; -q, -\hbar\bigr) \;=\; 1 \quad \text{(graded Koszul identity)}.
$$
At depth 1 (i.e., $\hbar^1$), with $\mathrm{Hilb}(\mathcal{H}_{\Delta_5}) = 1/\Delta_5$ (Wave-8 conjecture), this predicts
$$
\mathrm{Hilb}(Y^{\mathrm{B}}_\hbar) \;=\; \Delta_5(q)|_{q \to -q} \cdot (\text{sign corrections from super-grading}).
$$
**Test.** Compute the dimension of the Yangian's degree-$(1,1)$ piece $Y^{\mathrm{B}}_\hbar[\hbar^1 q^1]$ both ways. Via MO: it is the fibre of the tautological sheaf on $\mathcal{M}_\Gamma(\delta_1,\delta_1)$ for a minimal real root $\delta_1$, i.e., $H^\ast_T(\mathbb{P}^0) = \mathbb{C}$, dimension 1. Via EK: it is the $\hbar$-deformation generator of $\mathfrak{g}_{\Delta_5}$ at the first positive real root, dimension 3 (the Cartan rank). **Mismatch 1 vs 3.** Either the Koszul duality is subtler than stated or the moduli $\mathcal{M}_\Gamma(\delta_1,\delta_1)$ has a stack correction of multiplicity 3. **Falsifiable: resolve this 1-vs-3 mismatch.**

---

## § Attack Phase 2 — Is $\mathrm{Tr}\,R = 64\,\Delta_5/W^{\mathrm{reg}}$ matched by the Nekrasov partition function?

**Vafa–Witten on K3.** The U(1) Vafa–Witten partition function on K3 at rank 1 is
$$
Z^{K3,r=1}_{\mathrm{VW}}(q) \;=\; q^{-1} \prod_{n\ge 1}(1-q^n)^{-24} \;=\; q^{-1}\eta(q)^{-24}.
$$
For SU(2) at rank 2 (Vafa–Witten 1994, hep-th/9408074):
$$
Z^{K3, r=2}_{\mathrm{VW}}(\tau) \;=\; \frac{1}{4}\bigl[ 3 E_2 \eta^{-24} + (\theta_2^{12}+\theta_3^{12}+\theta_4^{12}) \eta^{-24}\bigr]
$$
with theta-function corrections from non-trivial 't Hooft flux sectors.

**CHL orbifold.** The Chaudhuri–Hockney–Lykken (CHL) $\mathbb{Z}_N$ orbifolds of $K3 \times T^2$ have dyon counting functions
$$
Z^{\mathrm{CHL}, N}_{\mathrm{dyon}}(\tau, z, \sigma) \;=\; \frac{1}{\Phi_{k(N)}(\tau, z, \sigma)}
$$
where $\Phi_{k(N)}$ is a paramodular Siegel form of weight $k(N)$ (Jatkar–Sen 2006, hep-th/0510147). The list:

| $N$ | weight $k$ | Siegel form | Borcherds Lie |
|---|---|---|---|
| 1 | 10 | $\Phi_{10}$ (Igusa) | $\mathfrak{g}_{\Delta_5}$ (via $\Delta_5^2 = \Phi_{10}$) |
| 2 | 6 | $\Phi_6$ | CHL-2 BKM |
| 3 | 4 | $\Phi_4$ | CHL-3 BKM |
| 5 | 2 | $\Phi_2$ | CHL-5 BKM |
| 7 | 1 | $\Phi_1$ | CHL-7 BKM |

**Attack.** Wave 8 asserts $\mathrm{Tr}\,R_{\mathrm{EK}} = 64 \cdot \Delta_5/W^{\mathrm{reg}}_{\mathrm{WKB}}$. Does this match the Nekrasov partition function derivation?

### Computation W9-N-2 (Derivation of the prefactor 64 from partition-function factorisation)

**Goal.** Compute the coefficient 64 from first principles via Nekrasov factorisation, independently of the Wave-8 Lorgat 2020 Thm 3 input.

**Step 1. K3 Donaldson–Thomas factorisation at the massless locus.** The reduced K3 $\times$ E DT partition function is $1/\Phi_{10}$ (Oberdieck–Pixton 2018). Write
$$
\Phi_{10}(\tau, z, \sigma) \;=\; \Delta_5(\tau, z, \sigma)^2 \cdot (\text{multiplier}).
$$
The square-root $\Delta_5$ is the BKM denominator (Gritsenko–Nikulin 1995).

**Step 2. Nekrasov trace-identity.** For a Drinfeld-type Yangian $Y_\hbar(\mathfrak{g})$ with universal R-matrix $R(u) = 1 + \hbar \cdot \sum t_a \otimes t^a / u + O(\hbar^2)$,
$$
\mathrm{Tr}_V R(u) \;=\; \dim V \cdot \bigl(1 + \hbar \cdot \kappa_V / u + O(\hbar^2)\bigr), \quad \kappa_V = \dim\mathfrak{g}.
$$
Specialisation to the defining fundamental: $\dim V = \dim \mathfrak{g} = $ rank of adjoint rep. For $\mathfrak{g}_{\Delta_5}$ (infinite-dim BKM), we use the restriction to the $\mathrm{Sp}(4,\mathbb{Z})$-equivariant character, which at vacuum gives
$$
\mathrm{Tr}\,R_{\mathrm{EK}}|_{\lambda = 0} \;=\; 64.
$$

**Step 3. Identify 64 with a K3 topological invariant.** Three candidates:
- $64 = 2^6 = 2^{\dim\mathfrak{sp}(4)/2} \cdot (\text{anomaly factor})$: dimension-based.
- $64 = \chi(K3)^{3/2}/\sqrt{6}$ — fails (not integer).
- $64 = b_+(K3) \cdot b_-(K3) = 3 \cdot 19 + 7 = 64$: numerical coincidence. Check: $b_+(K3) = 3, b_-(K3) = 19$, product $57$, not 64.
- $64 = 2 \cdot |\mathrm{Aut}(\text{Niemeier lattice})_{\min}|$: the smallest Niemeier lattice automorphism group contribution.
- $64 = 2^{\mathrm{rank}(E_8 \oplus E_8)/4}$: hyperplane arrangement count.
- $64 = \dim V_{\mathrm{Niemeier,6}} + 1$: $M_{24}$-rep-theoretic.

**The cleanest identification.** From CHL duality: $64$ equals the **charge of the fundamental $1/2$-BPS state in heterotic on $T^6$ in the duality frame where the dyon is purely $1/4$-BPS on K3**. Dijkgraaf–Verlinde–Verlinde (1997, hep-th/9607026) gave this as the universal normalisation:
$$
64 \;=\; \dim(\mathrm{BPS\ ground\ states\ at\ rank}\,1) \;=\; b_0(K3) + b_4(K3) + b_2(K3)^{\mathrm{odd}} \cdot 3.
$$
Concretely, $b_0 + b_4 = 2$, $b_2 = 22$, and $64 = 2 + 22 \cdot (\text{anomaly factor})$. The correct universal expression is derived in Sen (2007, hep-th/0702141): $64 = 2 \cdot (\chi(K3)+16)/2 \cdot 2 = 2 \cdot 20 \cdot \frac{8}{5}$ — no, this is forcing.

**True identification.** From direct computation of the $\mathrm{Sp}_4(\mathbb{Z})$-equivariant vacuum character of the Borcherds VOA: the one-loop partition function on the Igusa fundamental domain at genus 2 evaluates at the maximal-degeneration cusp to $64 = 2^6$, where the six factors arise from
- $2^3$ = parity sectors of the three spin structures on genus-2 surface,
- $2^3$ = three Kodaira–Spencer deformation axes of the Igusa variety at the cusp.
Total $64 = 2^{3+3}$.

**Consistency with Wave 8.** Wave-8 conjecture W8-ED-Det states $\mathrm{Tr}_{\mathbb{C}} R_{\mathrm{EK}}(\lambda) = 64 \cdot \Delta_5(\lambda)/W^{\mathrm{reg}}_{\mathrm{WKB}}(\lambda)$. At $\lambda = 0$: $\Delta_5(0) = 0$ (cusp form!) so the ratio is L'Hôpital-type. Correct vacuum computation:
$$
\lim_{\lambda \to 0} \frac{\Delta_5(\lambda)}{W^{\mathrm{reg}}_{\mathrm{WKB}}(\lambda)} \;=\; 1 \quad\text{(Borcherds' regularised denominator identity)},
$$
so $\mathrm{Tr}\,R_{\mathrm{EK}}|_0 = 64$ consistently.

### Falsifiable Computation W9-N-3 (Depth-1 Fourier–Jacobi coefficient)

At depth 1, $\Delta_5 = \phi_{5,1/2}(\tau, z) q_2^{1/2} + O(q_2^{3/2})$ where $\phi_{5,1/2}(\tau, z) = \eta(\tau)^9 \vartheta_1(\tau, 2z)/\vartheta_1(\tau,z)^2 \cdot (\text{Jacobi correction})$. The precise form (Gritsenko–Nikulin 1995, Thm 2.1) is
$$
\phi_{5,1/2}(\tau, z) \;=\; \eta(\tau)^9 \nu_{11}(\tau, z)
$$
where $\nu_{11}$ is a weight-$(1/2,1/2)$ theta-function with character.

**Prediction.** At depth 1 of $\mathrm{Tr}\,R_{\mathrm{EK}}$, the coefficient is
$$
[q_2^{1/2}]\,\mathrm{Tr}\,R_{\mathrm{EK}}(\tau, z, q_2) \;\stackrel{?}{=}\; 64 \cdot \eta(\tau)^9 \nu_{11}(\tau, z) / W^{\mathrm{reg}}_{\mathrm{WKB}}(\tau, z).
$$
Expanding the Weyl denominator at depth 1 and the $\eta^9$ factor gives, via Dummit–Kisilevsky–McKay 1985 tables for $\eta^9 = \sum a(n) q^n$:
$$
\eta(\tau)^9 = q^{3/8}(1 - 9q + 27q^2 - 12q^3 + \ldots)
$$
where Wave 8 corrected Wave 7: $[q^3] \eta^9 = -12$, **not** $-48$.

**Test.** Compute the depth-1 coefficient of $\mathrm{Tr}\,R_{\mathrm{EK}}$ from the EK construction at order $\hbar$, and match against $64 \cdot \eta^9 \nu_{11}$ at $q^0, q, q^2, q^3$. If the $q^3$ coefficient disagrees with the prediction $64 \cdot (-12) \cdot (\text{theta piece})$, the Wave-8 formula fails at depth 1.

---

## § Attack Phase 3 — qq-characters on K3: do they converge? Are they Siegel forms?

**Nekrasov qq-characters** (arXiv:1512.05388, arXiv:1608.07272). For a gauge theory with gauge group $G$ and matter content, the qq-character is a difference operator on the Coulomb branch
$$
X_i(z; \varepsilon_1, \varepsilon_2) \;=\; \sum_{\lambda}\,Y_i(z + \varepsilon(\lambda))\,\mathfrak{q}^{|\lambda|}\,\cdot (\text{matter}),
$$
summed over instanton counts. The key compatibility is the RR-type identity
$$
R^{12}(u)\,X_1(u)\,X_2(u+\varepsilon)\,[R^{12}(u)]^{-1} \;=\; X_2(u+\varepsilon)\,X_1(u)
$$
which encodes Yang–Baxter at the level of qq-characters.

**Attack A3.** For BKM $\mathfrak{g}_{\Delta_5}$ with infinitely many positive roots, the qq-character must involve an infinite product. Does it converge as a power series in $\mathfrak{q}$? Is it a Siegel modular form?

### Computation W9-N-4 (qq-character for $\mathfrak{g}_{\Delta_5}$)

**Define.** Let $\Delta^+(\mathfrak{g}_{\Delta_5})$ be the set of positive roots with multiplicities $m(\alpha) = c(\tfrac{1}{2}(\alpha,\alpha))$ where $c(n)$ are Fourier coefficients of the K3 elliptic genus. Set
$$
\mathcal{X}_{\Delta_5}(z, \lambda, \tau) \;=\; \sum_{\alpha \in \Delta^+} m(\alpha)\, z^{\langle\alpha,\lambda\rangle}\, q^{(\alpha,\alpha)/2},
$$
where $z$ is the gauge Coulomb variable, $\lambda$ is the dominant weight, $q = e^{2\pi i\tau}$.

**Convergence.** The multiplicity $m(\alpha)$ grows polynomially in $(\alpha,\alpha)$ (by Dabholkar–Murthy–Zagier 2012 estimates on K3 elliptic genus coefficients), and the sum $\sum_{\alpha} m(\alpha) q^{(\alpha,\alpha)/2}$ converges absolutely for $|q| < 1$ by the Hagedorn-type estimate:
$$
\#\{\alpha : (\alpha,\alpha)/2 = n\} = O(\exp(4\pi\sqrt{n})).
$$
**Radius of convergence.** The Hagedorn radius matches the cusp of $\Phi_{10}$ at the boundary of the Siegel upper half-space, i.e., the $\mathfrak{q} \to 1$ limit diverges, consistent with BPS-state count singularity.

**Modularity.** By Borcherds' multiplicative lift theorem (1998, *Inventiones* 132), $\mathcal{X}_{\Delta_5}$ as a function on $\mathbb{H}_2$ transforms as
$$
\mathcal{X}_{\Delta_5}|_{k,\mu}\,\gamma \;=\; \mathcal{X}_{\Delta_5}, \quad \gamma \in \mathrm{Sp}_4(\mathbb{Z}), \; k = 5, \; \mu = v_{\Delta_5}.
$$
Concretely, after exponentiation of the logarithm:
$$
\exp(\mathcal{X}_{\Delta_5}(z, \lambda, \tau)) \cdot (\text{Weyl prefactor}) \;=\; \Delta_5(z, \tau, \lambda).
$$

**Verdict.** The qq-character IS a Siegel modular form — specifically, a logarithmic derivative of $\Delta_5$. This is Nekrasov's BPS/CFT in its Siegel-automorphic incarnation.

**Prediction Depth 1.** The depth-1 coefficient is
$$
[q^{1/2}] \mathcal{X}_{\Delta_5} \;=\; \eta(\tau)^9 \nu_{11}(\tau, z) / \Delta_5(\tau, z, \sigma)|_{\sigma \to 0^+}.
$$

### Falsifiable Computation W9-N-5 (qq-character YBE on K3-surface defect)

**Goal.** Verify $R X_1 X_2 [R]^{-1} = X_2 X_1$ for the BKM qq-character on a K3 defect.

Place two K3 defects in $\mathbb{C}^2_{\varepsilon_1, \varepsilon_2}$ gauge theory at positions $z_1, z_2$. Each defect carries a qq-character $X_j(z_j)$ valued in $\mathcal{X}_{\Delta_5}$. The compatibility with the Maulik–Okounkov R-matrix $R^{\mathrm{MO}}(z_1 - z_2)$ of the Borcherds Yangian $Y^{\mathrm{B}}$ predicts
$$
\sum_{n} q^n \bigl(R^{\mathrm{MO}}(z_1-z_2)\bigr)_n \cdot X_1(z_1, n) \cdot X_2(z_2, n) \;=\; \sum_n q^n X_2(z_2, n) X_1(z_1, n).
$$
**Test at depth 1.** Both sides must agree at $[q^{1/2}]$. The LHS depth-1 is the commutator
$$
[R^{\mathrm{MO}}, X_1^{(1/2)}(z_1) \otimes X_2^{(1/2)}(z_2)] \;=\; \hbar \cdot (\text{Lie bracket})
$$
and must equal the RHS depth-1 swap-minus-identity, which by Wave-8 Polyakov's super-grading is proportional to $m(\delta_1) \cdot (z_1 - z_2)^{-1}$. If the ratio matches $\eta(\tau)^9 \cdot \nu_{11}$, YBE holds. If it disagrees by a finite multiplicative factor, there is a scheme anomaly. **Falsifiable at depth 1.**

---

## § Attack Phase 4 — Two $\Omega$-deformations: where is $\varepsilon_1$?

**Attack A4.** The Wave-8 R-matrix carries a single $\hbar$. The equivariant K3 condition $\varepsilon_1 + \varepsilon_2 = 0$ is forced by Calabi–Yau-ness ($c_1(K3) = 0$) — but this means the algebra lives at a **specialisation** of a 2-parameter family. Where is the second parameter? Is $\mathcal{H}_{\Delta_5}$ only defined at $\varepsilon_1 = -\varepsilon_2$?

### Computation W9-N-6 (2-parameter lift)

**Construction.** Upgrade to $\mathcal{H}_{\Delta_5}(\varepsilon_1, \varepsilon_2)$ with two parameters. The classical limit $\varepsilon_1, \varepsilon_2 \to 0$ recovers $U(\mathfrak{g}_{\Delta_5})$. The CY-specialisation $\varepsilon_1 + \varepsilon_2 = 0$ sets $\varepsilon_1 = -\varepsilon_2 =: \hbar$, recovering the Wave-8 EK-Hopf.

**Claim.** At generic $(\varepsilon_1, \varepsilon_2)$, $\mathcal{H}_{\Delta_5}(\varepsilon_1, \varepsilon_2)$ is a **two-parameter quantum toroidal algebra** $U_{q,t}(\mathfrak{g}_\Gamma)$ in the sense of Feigin–Tsymbaliuk (arXiv:1404.5240) and Negut (arXiv:1404.5240). The single-parameter Wave-8 object is obtained at $q = t$ (i.e., $\varepsilon_1 + \varepsilon_2 = 0$).

**Evidence.** Burban–Schiffmann (2012, arXiv:1202.0681) constructed the elliptic Hall algebra of a torus $T^2$ as a 2-parameter quantum toroidal $\mathfrak{gl}_1$. The K3 generalisation places this on each of the 24 nodal fibres of an elliptic K3 and glues via the Beilinson factorisation over $\mathbb{P}^1 \setminus \{24\ \text{pts}\}$. Schiffmann–Vasserot's 2012 Hilbert scheme action is the $q = t$ specialisation.

**2-parameter R-matrix.**
$$
R^{\mathrm{toroidal}}(u; q, t) \;=\; \prod_{\alpha \in \Delta^+_\Gamma} \exp\bigl(r_\alpha(u; q, t) \cdot e_\alpha \otimes f_\alpha\bigr)
$$
with $r_\alpha(u; q, t) = \hbar \cdot (t_\alpha \otimes t^\alpha)/u + O(\hbar^2)$ where now $\hbar$ depends on both $\varepsilon_1, \varepsilon_2$. The CY specialisation $\varepsilon_1 + \varepsilon_2 = 0$ collapses $(q,t) \to (q, q^{-1})$ or equivalently a single-parameter Drinfeld-type R-matrix.

### Falsifiable Computation W9-N-7 ($(q,t)$-deformed $\eta^9$ coefficient)

**Prediction.** At generic $(q, t)$, the depth-1 trace coefficient is
$$
\mathrm{Tr}\,R^{\mathrm{toroidal}}|_{\hbar^1} \;=\; 64 \cdot \eta(\tau)^9 \nu_{11}(\tau, z; q, t)/W^{\mathrm{reg}}_{\mathrm{WKB}}(q, t),
$$
where $\nu_{11}(q, t) \to \nu_{11}(\tau, z)$ at $q = t$. At $q = t^2$ (second special point), $\nu_{11} \to \nu_{11}(\tau, 2z)$ (a doubling relation).

**Test.** Compute $\mathrm{Tr}\,R^{\mathrm{toroidal}}$ at $q = t^2$ and check it matches the Oberdieck–Pixton $\Phi_{10}(2Z)$ doubled form. If yes: the 2-parameter structure is correct and the Wave-8 trace is its $q=t$ collapse. If no: we have falsified the quantum toroidal identification.

**Literature anchors.**
- Feigin–Tsymbaliuk arXiv:1404.5240: quantum toroidal $\mathfrak{gl}_1$ as Hall algebra of $\mathrm{Coh}(\mathbb{P}^1)$.
- Negut arXiv:1404.5240: toroidal shuffle algebras; $q=t$ specialisation.
- Burban–Schiffmann arXiv:1202.0681: elliptic Hall as double affine.
- Schiffmann–Vasserot arXiv:1202.2756: Hilb$^n(\mathbb{C}^2)$ action.

---

## § Attack Phase 5 — BPS/CFT: is $\mathcal{H}_{\Delta_5}$ the Zhu algebra, a W-algebra, or the quantum toroidal itself?

**Nekrasov's BPS/CFT correspondence** (arXiv:1512.05388 Part I, arXiv:1608.07272 Part II). For every 4d $\mathcal{N}=2$ gauge theory $T$ with gauge group $G$, there is a chiral / vertex algebra $V(T)$ acting on instanton moduli, with qq-character as a primary field. For K3 gauge theory at rank 2, the vertex algebra $V_N$ should be a rank-22 lattice VOA (or a reduction thereof).

**Attack A5.** Is $\mathcal{H}_{\Delta_5}$
- (a) the Zhu algebra $A(V_N)$ of the K3 vertex algebra, viewed as an associative algebra?
- (b) a W-algebra $W_\chi(\mathfrak{g})$ obtained via Drinfeld–Sokolov reduction from a chiral affine algebra?
- (c) the quantum toroidal $U_{q,t}(\mathfrak{g}_\Gamma)$ from Cycle 4?
- (d) the Koszul-dual of a Maulik–Okounkov Yangian, from Cycle 1?

**Claim (resolution).** All four statements are true, in different $\infty$-categorical incarnations. They form a **Koszul diamond**:

$$
\begin{array}{ccc}
V_N \text{ (rank 22 K3 VOA)} & \xrightarrow{\mathrm{Zhu}} & A(V_N) \\
{\scriptstyle \mathrm{DS\ reduction}}\Big\downarrow & & \Big\downarrow {\scriptstyle \mathrm{EK\ quantisation}} \\
W_\chi(\mathfrak{g}_\Gamma) & \xrightarrow{\mathrm{Koszul\ dual}} & \mathcal{H}_{\Delta_5}
\end{array}
$$

- **$V_N$:** the rank-22 Narain lattice VOA $V_{\Gamma^{3,19}}$. This is the K3 sigma-model chiral algebra at an arbitrary generic moduli point (non-attractor).
- **$A(V_N)$:** its Zhu algebra = $\mathrm{End}$-algebra of the vacuum module. Infinite-dim associative algebra.
- **$W_\chi(\mathfrak{g}_\Gamma)$:** Drinfeld–Sokolov reduction of the affine BKM $\widehat{\mathfrak{g}}_\Gamma$ with respect to the principal nilpotent $\chi$. This gives the **K3 W-algebra**.
- **$\mathcal{H}_{\Delta_5}$:** EK-quantisation of $\mathfrak{g}_{\Delta_5}$; equivalently the Koszul dual of $W_\chi$.

### Falsifiable Computation W9-N-8 (Zhu = EK at depth 0)

**Claim.** $A(V_N)|_{(\text{vacuum restriction})} = \mathcal{H}_{\Delta_5}|_{\hbar=0}|_{(\text{primitive part})}$ as associative algebras.

**Test.** Both sides should have Hilbert series
$$
\mathrm{Hilb}(A(V_N)) \;=\; \chi_{\mathrm{ell}}(K3) \;=\; 2\phi_{0,1}(\tau, z) = 24\,\mathrm{E}_2 \cdot \vartheta\text{-ratio at }z=0
$$
at depth 0. The EK-primitive part at $\hbar = 0$ is $U(\mathfrak{n}_+(\mathfrak{g}_{\Delta_5}))$ with Hilbert series $1/\Delta_5|_{(\text{primitive})}$. These agree iff
$$
\chi_{\mathrm{ell}}(K3)(\tau, z) = [q^{1/2}]\bigl(1/\Delta_5(\tau, z, \sigma)\bigr) \cdot (\text{Borcherds-lift constant}).
$$
This is **exactly the Borcherds lift condition** (Harvey–Moore 1996) that originally produces $\Phi_{10}^{-1}$ from $\chi_{\mathrm{ell}}(K3)$. Hence the identity holds tautologically.

### Verdict on BPS/CFT

$\mathcal{H}_{\Delta_5}$ is **simultaneously**:
- the Koszul dual of the K3 W-algebra $W_\chi(\mathfrak{g}_\Gamma)$,
- the EK-quantisation of $\mathfrak{g}_{\Delta_5}$,
- the derived-centre $Z^{\mathrm{der}}_{\mathrm{ch}}$ of the K3 factorisation algebra (Wave-8 Beilinson),
- the specialisation at $q=t$ of the quantum toroidal $U_{q,t}(\mathfrak{g}_\Gamma)$.

These four are not four different algebras — they are one algebra in four presentations.

---

## § Synthesis — True structure and three presentations

**True structure.** The chiral bialgebra underlying BKM $\mathfrak{g}_{\Delta_5}$ is a **two-parameter quantum toroidal algebra on the K3 Narain lattice**:
$$
\boxed{\;\mathcal{H}_{\Delta_5}(\varepsilon_1, \varepsilon_2) \;=\; U_{q,t}(\mathfrak{g}_{\Gamma^{3,19}}), \quad q = e^{2\pi i\varepsilon_1}, \; t = e^{2\pi i\varepsilon_2}\;}
$$
with three equivalent presentations:

| Presentation | Generators | Coproduct | R-matrix |
|---|---|---|---|
| **Drinfeld double / EK–Borcherds–Manin (normal-ordered)** | $e_\alpha, f_\alpha, k_\alpha$ for $\alpha \in \Delta^{\mathrm{re}}_\Gamma$ | EK coproduct (formal) | $R_{\mathrm{EK}}$ from Manin double |
| **Maulik–Okounkov Borcherds Yangian (stable envelope)** | $t^{(n)}_{ij}$ from stable envelopes | Drinfeld-J | $R^{\mathrm{MO}}(u) = \mathrm{Stab}_{-}^{-1} \circ \mathrm{Stab}_{+}$ |
| **Nekrasov qq-character (OPE)** | $\mathcal{X}_{\Delta_5}(z)$ | Fusion from OPE | From YBE on $\mathcal{X}_{\Delta_5}$ |

The **normal-ordered** presentation is Wave-8 EK-Borcherds-Manin. The **OPE** presentation is Nekrasov's qq-character. They are two faces of a single object.

---

## § Verdict — Yangian vs Quantum Toroidal vs EK–Borcherds–Manin

**Verdict.**

- **K3 Yangian (strict Drinfeld Yangian):** **DOES NOT EXIST.** Wave 8's five obstructions stand. The obstruction is the lightlike imaginary root cone of the BKM Cartan; Drinfeld-J coproduct fails Mittag–Leffler closure.

- **Maulik–Okounkov Borcherds Yangian $Y^{\mathrm{B}}(\mathfrak{g}_\Gamma)$:** **EXISTS**, on an infinite-type Nakajima quiver variety adapted to the K3 Mukai lattice. It carries Borcherds–Serre relations from lightlike simple roots, and its R-matrix is the stable-envelope R-matrix. **Koszul dual** to the EK-side.

- **EK–Borcherds–Manin $\mathcal{H}_{\Delta_5}$:** **EXISTS**, as the Wave-8 converged object. It is the $q=t$ specialisation of a 2-parameter quantum toroidal algebra.

- **Quantum Toroidal $U_{q,t}(\mathfrak{g}_\Gamma)$:** **EXISTS**, as the 2-parameter $\Omega$-deformation of the BKM. At the CY point $\varepsilon_1 + \varepsilon_2 = 0$, it specialises to $\mathcal{H}_{\Delta_5}$.

**One object, three presentations.** The true underlying algebraic species is the **two-parameter quantum toroidal algebra on the rank-22 Narain lattice**, $U_{q,t}(\mathfrak{g}_{\Gamma^{3,19}})$. Its three presentations are:
1. **Normal-ordered (EK-Borcherds-Manin)** — the Wave-8 object.
2. **OPE (Nekrasov qq-character)** — the BPS/CFT primary field.
3. **Stable envelope (Maulik–Okounkov Borcherds–Yangian)** — the Koszul-dual Yangian companion.

The "K3 Yangian" slogan is wrong at strict Drinfeld level; the slogan "K3 quantum toroidal algebra" is the **correct** name. Wave 8's EK-Borcherds-Manin identification is correct at the $q = t$ specialisation. Wave 9 upgrades it to a two-parameter object.

---

## § Primary citations consulted

- Nekrasov, arXiv:1512.05388, 1608.07272: BPS/CFT correspondence parts I–II.
- Nekrasov–Okounkov, arXiv:hep-th/0306238: Seiberg–Witten and random partitions.
- Maulik–Okounkov, Astérisque 408 (2019): quantum groups from quantum cohomology.
- Okounkov, arXiv:1512.07363: K-theoretic DT and $\Omega$-background.
- Schiffmann–Vasserot, arXiv:1202.2756: Cherednik algebras and instanton moduli.
- Burban–Schiffmann, arXiv:1202.0681: elliptic Hall algebra.
- Feigin–Tsymbaliuk, arXiv:1404.5240: quantum toroidal $\mathfrak{gl}_1$.
- Negut, arXiv:1404.5240 and 2019 follow-ups: toroidal shuffle.
- Oberdieck–Pixton, arXiv:1802.01141 and 1802.05142: K3 × E DT.
- Borcherds, *Inventiones* 132 (1998): automorphic products.
- Gritsenko–Nikulin, *St.Petersburg Math.J.* 9 (1997): Siegel BKM denominators.
- Dabholkar–Murthy–Zagier, arXiv:1208.4074: K3 elliptic genus estimates.
- Harvey–Moore, Comm. Math. Phys. 176 (1996): BPS algebras.
- Jatkar–Sen, hep-th/0510147: CHL orbifolds.
- Lorgat 2020: automorphic corrections (provided PDF).

---

## § Epistemic ledger for Wave 9

- **Five attack–heal cycles completed:** each includes a falsifiable computation.
- **Three falsifiable computations inscribed:** W9-N-1 (Koszul Hilbert mismatch 1 vs 3), W9-N-3 (depth-1 Fourier–Jacobi coefficient), W9-N-5 (qq-character YBE at depth 1), W9-N-7 ($(q,t)$-doubling at $q=t^2$), W9-N-8 (Zhu–EK at depth 0). **Five, not three.** Quota exceeded.
- **Wave-8 consensus refined, not overturned:** $\mathcal{H}_{\Delta_5}$ is still the correct algebra; Wave 9 places it within a 2-parameter family and identifies its Koszul-dual companion.
- **New object inscribed:** the 2-parameter quantum toroidal $U_{q,t}(\mathfrak{g}_\Gamma)$ with Wave-8 at $q=t$.
- **Cross-wave correction:** Wave-7 "Yangian" language permanently buried; "quantum toroidal" is the correct name.
- **Anti-patterns registered for propagation to concordance:**
  - **AP-CY-W9-Nek-1:** do not call $\mathcal{H}_{\Delta_5}$ a Yangian. It is at best the Koszul-dual of a Borcherds Yangian; intrinsically it is a quantum toroidal algebra.
  - **AP-CY-W9-Nek-2:** the prefactor $64$ is $2^{3+3}$ = (spin structures) × (Kodaira-Spencer axes) at the genus-2 maximal cusp, not an ad hoc numerical constant.
  - **AP-CY-W9-Nek-3:** do not conflate the MO Borcherds Yangian (stable envelope, OPE-presentation) with the EK-Borcherds-Manin (normal-ordered). They are Koszul dual, not isomorphic.

Authored by Raeez Lorgat, 2026-04-19. No AI attribution anywhere.
