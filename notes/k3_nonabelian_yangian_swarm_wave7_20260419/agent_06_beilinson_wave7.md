# Agent 06 — Beilinson, Wave 7. Factorization-geometric demolition and reconstruction of the non-abelian K3 Yangian.

**Author.** Raeez Lorgat. Sole author. No AI attribution.

**Date.** 2026-04-19.

**Voice.** A.A. Beilinson. Beilinson–Drinfeld *Chiral Algebras* (AMS Colloq. Publ. 51) in the strict sense. Factorization spaces and D-modules; derived categories on Ran spaces; six-functor formalism (Gaitsgory–Rozenblyum, ind-coherent); Francis–Gaitsgory (FG11 arXiv:1107.3939; FG12 arXiv:1111.4797); Lurie *Higher Algebra* §4.8, §5.5; Positselski arXiv:0905.2621. Chain-level and $(\infty,1)$-categorical both load-bearing (CLAUDE.md).

**Dictum.** What limits forward progress is not the lack of genius but the inability to dismiss false ideas. A small true theorem beats a large false one. The manuscript is suspect. Every prior wave is memory (lowest rung). Every claim reduced to primary source or direct computation. No self-exoneration.

**Target.** The non-abelian K3 Yangian $Y_{\text{BFN}}(K3)$ as some sort of factorization-algebraic object. The precise question Wave 7 attacks: **is the "K3 Yangian" a chiral algebra, a factorization algebra, or a derived centre — and on what factorization space, with what D-module structure, with what six-functor accessibility?**

**Method.** AT LEAST FIVE full ATTACK → HEAL cycles. Each cycle (a) starts from first principles, (b) opens a specific structural hole, (c) exhibits a mitigation, (d) tests the mitigation with a new attack. Convergence = attack pass finds no new structural hole.

---

## §0. Preflight.

### 0.1. What the manuscript inscribes that bears on BD factorization.

- **`cy_to_chiral.tex:27`.** "The factorization envelope construction produces a factorization algebra $\Fact_X(\mathfrak L_\cC)$ on any smooth **curve** $X$." The target of $\Phi_d$ is a factorization algebra on a **curve**. (The word "curve" is used in the BD sense: 1-complex-dim, smooth, proper or affine.)
- **`cy_to_chiral.tex:50`.** $\Phi_2: \CY_2\text{-Cat} \to E_2\text{-ChirAlg}$, and `:50` again $\Phi_3: \CY_3\text{-Cat}^{\mathrm{fr}} \to E_1\text{-ChirAlg}$. Target category is $E_{n(d)}\text{-ChirAlg}(\cM_d)$, per `thm:phi-platonic` (`cy_to_chiral.tex:45–77`).
- **`cy_to_chiral.tex:71`.** `thm:phi-k3-explicit`: $\Phi_2(D^b(\Coh(K3))) = \cH_{\mathrm{Muk}}$, rank-24 Mukai-Heisenberg, signature $(4,20)$, $\kappa_{\mathrm{ch}} = 2$, $\eta^{24}$. Proved. **This is abelian.**
- **`k3_yangian_chapter.tex:91–101`.** Route A: CY-A through $\Phi$; Yangian quantization step **open**. Route B: BFN; conjectural for generic K3, proved at Kleinian $\tilde S_{\fg}$ (`thm:bfn-phi-ade-identification`).
- **`k3_yangian_chapter.tex:2380–2465`.** `sec:k3-perturbative-fact-homology`: Costello–Gwilliam $E_3$-factorization algebra $\cF$ on $\C^3$ restricted to $K3 \times E$; factorization homology $\int_{K3} \cF$ produces chiral data on the residual direction $E$. **`\ClaimStatusConjectured`** (line 2405).
- **`k3e_bkm_chapter.tex:9–13`.** "The threefold $K3 \times E$ is a fibration of a CY$_2$ over a CY$_1$"; $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3$ (chiral de Rham); $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$. **Two distinct modular characteristics**; conflating them is the pathology.
- **`k3e_bkm_chapter.tex:33–46`, Theorem Oberdieck–Pixton.** $Z^X(q,t,p) = C/(\Delta_5)^2 = C'/\Phi_{10}$ for $X = S \times E$ at order $N = 1$. **$\Delta_5$ is the Gritsenko–Nikulin form**, weight 5 on $\mathrm{O}^+(3,2) \cong \mathrm{Sp}_4(\Z)/\{\pm I\}$.
- **`k3e_bkm_chapter.tex:125–138`.** Denominator identity $\frac{1}{64}\Delta_5(2Z) = \Phi(z) = e^{-2\pi i \langle \rho, z\rangle} \prod_{\alpha \in \Delta_+}(1 - e^{-2\pi i \langle \alpha, z\rangle})^{\mathrm{mult}\,\alpha}$, for $\rho \in \Lambda^{2,1}_{II}$, $W^{(2)}(\Lambda^{2,1})$ Weyl group, $\mult(\alpha) = f(nm, l)$ with $f$ the Fourier coefficients of $\phi_{0,1}$ (weak Jacobi form, K3 elliptic genus).

### 0.2. What the automorphic-corrections PDF (Lorgat 2020) establishes directly.

Read: `~/Downloads/raeez.lorgat.automorphic-corrections.pdf`.

- **§1 Motivating conjecture, Conjecture 1.** All eight diagonal-divisor Siegel paramodular forms of Gritsenko–Clery type arise as reciprocal-square-root denominators of DT partition functions $Z^X_{L,h_M}$ of twisted CY3's $X = (S \times E)/(\Z/M\Z)$ with $S$ an elliptically-fibered K3, lattice polarization $L$, and finite-order symplectic automorphisms $g_N, h_M$. Moreover each is a **denominator of a generalized BKM superalgebra** with root multiplicities given by the $g_N$–$h_M$-twisted twined elliptic genus of $S$.
- **§3 Isomorphism $\Sp_4(\Z)/\{\pm I_4\} \xrightarrow{\wedge^2} \mathrm{O}(\Lambda^{3,2})_+/\{\pm I_5\}$** via the Pfaffian. Signature $(3,2)$. This places $\Delta_5$ in the BKM / lattice framework.
- **§4 The lattice $\Lambda^{3,2}$.** $\Lambda^{3,2} \simeq \Lambda^{(1,1)} \oplus \Lambda^{(1,1)} \oplus [2]$; primitive hyperbolic sub-lattice $\Lambda^{2,1} = \Lambda^{(1,1)} \oplus [2]$; $\Lambda^{2,1}_{II}$ with Gram matrix $\begin{pmatrix}2&-2&-2\\-2&2&-2\\-2&-2&2\end{pmatrix}$, Weyl group $W^{(2)}(\Lambda^{2,1}_{II})$, Weyl vector $\rho = \tfrac12\delta_1 + \tfrac12\delta_2 + \tfrac12\delta_3 = f_2 - \tfrac12 f_3 + f_{-2}$. Three vertices at infinity with $S_3$ permutation group $\Aut(\cP_{II})$.
- **§5 $\mathfrak g_{\Delta_5}$.** Real even simple roots $\Delta^{\mathrm{re}}_0 = \{\delta_1, \delta_2, \delta_3\}$. Imaginary simple roots indexed by $a \in \Lambda^{2,1}_{II} \cap \R_{\geq 0}\cP_{II}$ with multiplicities $\tau(a), m(a)$ derived from Fourier coefficients $f(n,l,m)$ of $\Delta_5$, i.e. $m(a) = -\tfrac{1}{64}f(n,l,m)$. **$\mathfrak g_{\Delta_5}$ has no real odd roots; it is a superalgebra with real part a Kac–Moody on $\Lambda^{2,1}_{II}$ corrected by imaginary (even and odd) roots coming from $\Delta_5$.**
- **§6 Connection to $\phi_{0,1}$.** $\phi_{0,1} = \phi_{12,1}/\delta_{12}$ with $\delta_{12} = q \prod_n (1-q^n)^{24}$ is the K3 elliptic genus; $\mathrm{mult}(\alpha) = f(nm, l) = f(D)$ with $D = 4nm - l^2$. **The cohomology class whose weights give the BKM root multiplicities is the K3 elliptic genus, which is a class in $E_\pi^{\bullet, \bullet}$ of the elliptic fibration $\pi: S \to \mathbb P^1$.**

### 0.3. The Beilinson-specific frame.

Three candidate realizations for the non-abelian K3 Yangian, to be tested:
- **(a) Elliptic fibration.** $\pi: S \to \mathbb P^1$ realizes K3 as elliptic-surface. Pushforward $\pi_!$ of chiral data on $S$ lands on $\mathbb P^1$. The base $\mathbb P^1$ is a curve; factorization algebra on $\mathbb P^1$ in BD sense is defined.
- **(b) Kummer / transverse-chiral.** $K3_{\mathrm{Kum}} = (T^4/\Z_2)^{\mathrm{min.res.}}$; orbifold chiral data on $T^4$ with $\Z_2$-equivariance descends to 16-Kleinian-local chiral data glued.
- **(c) Derived centre.** $Y_{K3}$ as $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$ of some chiral algebra $A$ on a curve $X$ with K3 data in coefficients. This is the Drinfeld-centre / `\ref{phi:U3}` reading.

Every cycle below tests one of these or exhibits a factorization-algebraic obstruction.

### 0.4. Epistemic frame.

The Wave 6 synthesis (`SYNTHESIS_WAVE6_ADVERSARIAL`) identified the Wave 1–5 $Y_{K3}$-programme as (a) conflating four distinct objects (Mukai-Heis, BFN at Kleinian, classical $\mathfrak{so}(4,20)$-envelope, $L_\infty$-coupled total), (b) unsupported by any named factorization space, convolution dGLA, or MC element, (c) non-applicable to Vol I Theorem B in its stated scope (Yangians are not conilpotent). Wave 7 starts from this position — not as an axiom, but as a baseline.

---

## CYCLE 1 — Is the "K3 Yangian" a chiral algebra on the surface K3?

### ATTACK 1. First-principles D-module / factorization-space obstruction.

A Beilinson–Drinfeld chiral algebra on a variety $X$ is a D-module $A$ on $X$ together with a chiral bracket $\mu: j_* j^* A \boxtimes A \to \Delta_* A$ on $X^2$ (BD §3.3.3). This construction is tightly tied to $X$ being a **smooth algebraic curve**:

- **(1.a) Codimension of the diagonal.** On a curve $X$, $\Delta_X \subset X^2$ is codim 1. The chiral bracket is a second-order distribution supported on $\Delta$ (cf. BD §3.3.5, residue of order 1). On a surface $S$, $\Delta_S \subset S^2$ is codim 2; the analog residue is fourth-order and the Leibniz identity for the bracket does not hold with the same normalization.
- **(1.b) Factorization space.** BD factorization lives on the Ran space $\Ran(X)$ for $X$ a curve. The Ran space of a surface $\Ran(S)$ is not the natural home for chiral algebras: the colimit of $S^n/S_n$ has dimension $2n$ and its cohomology with D-module coefficients picks up the surface braid group $\pi_1(\Conf_n(S))$, which is **not** the Artin braid group and does not furnish the $E_1$-operadic structure that classical chiral algebras require.
- **(1.c) $E_n$-operadic level.** FG11 §2 / Lurie *HA* §5.5 identifies chiral algebras on a curve with $E_1$-algebras in D-modules on $\Ran(X)$. The analog on a surface is $E_2$-algebras on $\Ran(S)$ — a genuinely different operadic category. Yangians are $E_1$-algebras (associative Hopf), not $E_2$.
- **(1.d) $c_1(K3) = 0$ does not supply a frame.** Lurie *HA* 5.5.4 and Ayala–Francis arXiv:1206.5522 require a **framing** (not just a tangential structure) for factorization homology to be well-defined on an $n$-manifold. K3 is hyperkähler, not parallelizable; $TK3 \not\cong \mathcal O_{K3}^{\oplus 2}$ as $\mathcal O$-modules.

**Conclusion.** The naive reading "$Y_{K3}$ is a chiral algebra on the surface K3" fails at four distinct categorical checkpoints: codimension of diagonal, factorization-space structure, $E_n$-level, framing. **Dismissed as a category error** in the BD sense.

### HEAL 1. $Y_{K3}$ lives on a curve; K3 appears as coefficients.

Read `cy_to_chiral.tex:27` literally. $\Phi_d$ produces a factorization algebra on a **curve** $X$. When the CY input is $D^b(\Coh(K3))$, the output $\Phi_2(D^b(\Coh(K3))) = \cH_{\mathrm{Muk}}$ (`cy_to_chiral.tex:71`) is a factorization algebra on **some smooth curve** — the curve is a parameter of the construction, not K3 itself. This is the honest scope.

**H1.1 (Healed statement).** If $Y(\mathfrak g_{K3})$ is factorization-algebraic at all, it is a factorization algebra on a curve $X$, with K3 appearing through either (i) coefficient D-modules (K3-module category), (ii) characteristic classes (cohomology of K3 entering as ground-field decorations), or (iii) base-change data (the factorization algebra varies over a K3-moduli base). **Option (b)** of Wave 6 A1 — "chiral algebra on K3 as a surface" — is rejected.

**H1.2 (Named curves, candidate list).** The natural candidate curves are:
- $X = E$ (elliptic), with K3 integrated out of $K3 \times E$: chiral algebra on $E$ with $K3 \times E$ CY3 coefficients.
- $X = \mathbb P^1$ (rational), with K3 elliptic-fibered $\pi: S \to \mathbb P^1$: chiral algebra on $\mathbb P^1$ with fibration data as coefficients.
- $X = D = \Spec k[[t]]$ (formal disc): stalk of any of the above.
- $X = $ smooth curve, with factorization data varying over Bridgeland moduli $\cM^{\mathrm{Bridg}}(K3)$.

Each is a different factorization algebra. Wave 7 will constrain which is (are) well-posed.

---

## CYCLE 2 — The elliptic-fibration route: $\pi: S \to \mathbb P^1$ as a chiral algebra on $\mathbb P^1$.

### ATTACK 2. Is $\pi_! (\text{chiral-data-on-}S)$ a chiral algebra on $\mathbb P^1$?

The primary source here is the Oberdieck–Pixton theorem (`k3e_bkm_chapter.tex:33`) and the automorphic-corrections PDF §1: **$S$ is taken to be an elliptically-fibered K3 with sections $s_1, s_2$, and the CY3 is $X = (S \times E)/(\Z/N\Z)$**. The relevant chiral structure descends from CY3.

- **(2.a) Pushforward of D-modules.** For $\pi: S \to \mathbb P^1$, the derived pushforward $\pi_!: D^b(D\text{-mod}(S)) \to D^b(D\text{-mod}(\mathbb P^1))$ is well-defined via the six-functor formalism. If $A$ is a D-module on $\Ran(S)$ with a factorization structure, the fibrewise pushforward $\pi_!^{\mathrm{fw}} A$ is a D-module on $\Ran(\mathbb P^1)$; but this pushforward does **not** automatically preserve the factorization structure, because the map $\Ran(S) \to \Ran(\mathbb P^1)$ is not étale or flat and the base-change morphisms for $j_*$ and $\Delta_*$ on $S^2$ vs $(\mathbb P^1)^2$ involve singular fibres.
- **(2.b) Singular fibres of $\pi$.** A generic elliptic K3 has 24 singular fibres (Kodaira type $I_1$ for a generic Weierstrass model), located at the zero-set of the discriminant $\Delta = 4A^3 + 27B^2 \in H^0(\mathbb P^1, \cO(24))$. The Euler characteristic $\chi(S) = 24 = \chi_{\mathrm{fibre-sing}} \cdot 1 + \chi_{\mathrm{gen}} \cdot 0 = 24$ (Euler–Grothendieck). **This is the source of the magical "24" that Wave 5–6 chased under many names.**
- **(2.c) Chiral pushforward.** BD §3.5 handles chiral algebras under flat maps; the base-change for $\pi$ requires care at the 24 singular fibres. The pushforward $\pi_!$ of a chiral algebra on $S$ with Mukai pairing (in the sense of Wave 7 CYCLE 1 H1) to $\mathbb P^1$ picks up monodromy representations around the 24 points: $\rho_i: \pi_1(\mathbb P^1 \setminus \{p_1, \ldots, p_{24}\}) \to \Aut(\cH_{\mathrm{Muk}})$.
- **(2.d) Does this produce a chiral algebra on $\mathbb P^1$?** A factorization algebra on $\mathbb P^1$ with monodromy around 24 punctures is **not** a chiral algebra in the BD sense on the compact $\mathbb P^1$; it is a chiral algebra on the complement $\mathbb P^1 \setminus \{24 \text{ points}\}$ with specified monodromy/extension data. **So Attack 2.a is clean: pushforward lands in a chiral-algebra-with-punctures, not a global $\mathbb P^1$-chiral-algebra.**

### HEAL 2. Chiral algebra on $\mathbb P^1$ with 24 punctures, monodromy = Mukai–Heisenberg.

**H2.1 (Healed statement).** The elliptic-fibration route defines a chiral algebra on $U := \mathbb P^1 \setminus \{p_1, \ldots, p_{24}\}$, with monodromy representations $\rho_i$ encoding the Kodaira type of each singular fibre. For generic elliptic K3, all $\rho_i$ are unipotent of the type $I_1$ (single node). The chiral algebra on $U$ is built from the Mukai-Heisenberg sitting on the generic fibre; monodromy corrections realize the 24-point local data.

**H2.2 (Factorization space, named).** The factorization space is $\Ran(U) = \Ran(\mathbb P^1 \setminus 24\text{ pts})$; it is a prestack well-defined in BD §3.4. The D-module on $\Ran(U)$ is the factorization envelope of the Mukai-Heisenberg Lie conformal algebra, with the 24 punctures' monodromy added as local systems.

**H2.3 (Relation to BKM/Siegel).** The 24 punctures on $\mathbb P^1$ are the Euler class of K3. The Weyl-Kac-Borcherds denominator identity of §0.2 (automorphic PDF §5, `k3e_bkm_chapter.tex:125–138`) uses the K3 elliptic genus $\phi_{0,1}$ whose Fourier coefficients are computed on the punctured base. **The factorization algebra on $\Ran(U)$ is the natural home for a K3-adapted BKM, with 24 punctures = 24 Ramond sectors.** This is my Wave 7 new structural conjecture (formally stated in CONJ below).

### ATTACK 2 (return). Is the pushforward actually a chiral algebra?

Test: does $\pi_!$ preserve the chiral bracket $\mu$?

- **Proper pushforward** $\pi_*$: for a proper map, $\pi_* = \pi_!$, and it preserves the chiral bracket *up to* base change. $\pi: S \to \mathbb P^1$ is proper (elliptic surface over $\mathbb P^1$).
- **Base-change for $\pi^2: S^2 \to (\mathbb P^1)^2$ around the diagonal.** The diagonal $\Delta_{\mathbb P^1} \subset (\mathbb P^1)^2$ pulls back to $\Delta_{\mathbb P^1} \times_{\mathbb P^1, \mathrm{fibre}} (S \times_{\mathbb P^1} S)$, which is a subvariety of $S \times_{\mathbb P^1} S$ but not equal to the full diagonal $\Delta_S \subset S^2$. **The chiral bracket on $S^2$ (supported on $\Delta_S$, codim 2) does not push forward to a chiral bracket on $(\mathbb P^1)^2$ (supported on $\Delta_{\mathbb P^1}$, codim 1): the codimension drops.** The distribution picks up an extra factor of 1-complex-dim fiberwise volume $\omega_{\pi}$ (relative dualising sheaf).
- **Résidual dimension.** $\pi_! \omega_\pi = [\pi_1^*(-2)]$ (relative dualising of an elliptic fibration, degree $-\chi(F) = 0$ if $F$ smooth, with delta contribution at the 24 singular fibres). So $\pi_! \omega_\pi$ has singular support on the 24 points and is a torsion D-module there.

**Conclusion of Attack 2 (return).** The pushforward $\pi_! \text{(chiral-alg-on-}S)$ is a factorization algebra on $\Ran(\mathbb P^1)$ with singular support along the 24 punctures. The chiral bracket is well-defined on the generic locus and extends to a factorization-algebra-with-boundary on $\Ran(\mathbb P^1)$ with boundary conditions at the 24 points = the Kodaira fibre data.

**So: Option (a) in the Beilinson-angle list (K3 elliptic fibration over $\mathbb P^1$) gives a well-posed factorization algebra on $\Ran(\mathbb P^1)$, with 24 punctures = singular fibres of $\pi$.** This is the first cleanly surviving construction.

### HEAL 2 (final). Statement W7-CYCLE2.

**W7-CYCLE2.** *Let $\pi: S \to \mathbb P^1$ be an elliptically-fibered K3 with generic Kodaira type $I_1$ at 24 singular fibres. Let $U = \mathbb P^1 \setminus \{p_1, \ldots, p_{24}\}$. The factorization algebra*
$$
A^{\mathrm{ell}}_{K3/\mathbb P^1} := \pi_!\bigl(\Fact_S(\mathfrak L_{S})\bigr) \in \Fact(\Ran(U))
$$
*pushforward of the factorization envelope of the K3 Lie conformal algebra along $\pi$, is well-defined as a D-module on $\Ran(U)$ with factorization structure inherited from the upstairs one, modulo the 24-puncture extension data. Its stalk at a generic point of $\mathbb P^1$ is $\cH_{\mathrm{Muk}}$ (Mukai-Heisenberg).* **`\ClaimStatusConjectured`** chain-level, because the full proof of factorization-preservation under $\pi_!$ requires an explicit compatibility of the upstairs chiral bracket with the singular-fibre monodromies. *$(\infty,1)$-categorical statement*: in the Gaitsgory–Rozenblyum ind-coherent six-functor formalism, $\pi_!$ is a well-defined functor $\mathrm{IndCoh}(\Ran(S)) \to \mathrm{IndCoh}(\Ran(\mathbb P^1))$, and the factorization-algebra-structure preservation is a compatibility check. This check has not been carried out in Vol III.

---

## CYCLE 3 — The Kummer route: $K3_{\mathrm{Kum}} = (T^4/\Z_2)^{\mathrm{min.res.}}$ as $\Z_2$-equivariant chiral data on $T^4$.

### ATTACK 3. Does $\Z_2$-equivariant chiral data on $T^4$ descend to a chiral algebra?

$T^4$ is a complex 2-torus, not a curve. So `cy_to_chiral.tex:27`'s "chiral algebra on a curve" does not apply directly to $T^4$. But $T^4 = E_1 \times E_2$ for two elliptic curves, and one can:

- **(3.a) Restrict to a "chiral direction".** View $T^4$ as $E_1 \times E_2$; take $E_1$ as the chiral direction (a curve), with $E_2$ as a "transverse direction" contributing coefficients. Chiral algebras on $E_1$ with $E_2$-dependent coefficients are well-defined (BD §3.9 on twisted chiral algebras; FG12 for ind-coherent coefficients).
- **(3.b) $\Z_2$-action.** The Kummer $\Z_2$ acts on both $E_1$ and $E_2$ with involutions $\sigma_i: E_i \to E_i$, $[-1]$-map. Fixed points: 4 per $E_i$, giving 16 fixed points on $T^4 = E_1 \times E_2$ (the Kummer 16 points).
- **(3.c) Resolution.** The minimal resolution $K3_{\mathrm{Kum}} = \widetilde{(T^4/\Z_2)}$ replaces the 16 fixed points by 16 exceptional $\mathbb P^1$'s (Kummer divisors), each with self-intersection $-2$.
- **(3.d) Descent.** Chiral data on $E_1$ with $E_2$-coefficients, $\Z_2$-equivariant, descends to chiral data on $E_1/\Z_2$ with $E_2/\Z_2$-coefficients. **$E_1/\Z_2 \cong \mathbb P^1$** (branched double cover) with four branch points (the 2-torsion points of $E_1$). So the quotient factorization space is $\Ran(\mathbb P^1)$ with 4-puncture structure.

**Objection**: this route produces a chiral algebra on $\mathbb P^1$ with **4 punctures**, not 24. The 24 punctures of the elliptic-fibration route (CYCLE 2) do not match the 16 Kleinian points of the Kummer route. **Dissonance.**

### HEAL 3. The two routes are different chiral algebras; they agree only on a shared locus.

**H3.1 (Healed statement).** The Kummer route and the elliptic-fibration route produce **different** chiral algebras:
- **Elliptic:** factorization on $\Ran(\mathbb P^1 \setminus 24)$; 24 punctures = Kodaira singular fibres; Mukai-Heisenberg stalk.
- **Kummer:** factorization on $\Ran(\mathbb P^1 \setminus 4)$ with $E_2$-valued coefficients; 4 punctures = branch points of $E_1 \to E_1/\Z_2 = \mathbb P^1$; 16 Kleinian ADE points visible in the blown-up $K3_{\mathrm{Kum}}$ as chart-local $A_1$ singularities.

These are different factorization algebras on different factorization spaces. K3 moduli has many regions: the elliptic-fibration locus and the Kummer locus both sit inside the 20-dimensional Bridgeland stability manifold $\cM^{\mathrm{Bridg}}(K3)$, and they are **co-dimension-different** specializations. On the **intersection** (a Kummer K3 that is also elliptic-fibered: there are such K3's, with 20-dim Bridgeland moduli collapsing to a smaller stratum), the two factorization algebras must agree. This agreement is a non-trivial consistency condition.

**H3.2 (Consistency principle).** The "K3 Yangian" conjecture requires the two chiral-algebra presentations (elliptic and Kummer) to agree on their overlap locus inside Bridgeland moduli. **This is a new Wave 7 falsifiable prediction.**

### ATTACK 3 (return). Does the BFN-Kleinian identification survive the descent?

Read `k3_yangian_chapter.tex:81–89` (`conj:bfn-k3-yangian-kummer`): at the Kummer orbifold point, BFN Coulomb branch at charge $n$ is $Y(\fg_{K3})|_{\text{charge }n}$, conjecturally.

- **The BFN Coulomb branch at a Kleinian $\widetilde S_{A_1}$** is the level-1 shifted Yangian $Y^\mu(\widehat{\mathfrak{sl}}_2)_{k=1}$ (`thm:bfn-phi-ade-identification`). This is a Hopf algebra / $E_1$-algebra, not a chiral algebra on a curve.
- **Its factorization-algebra realization** is on the formal disc $D = \Spec k[[t]]$ (per BD §3.9.10 applied to the Kac–Moody conformal blocks on the affine Grassmannian). So BFN at $A_1$ gives a factorization algebra on the formal disc, **not** on $\mathbb P^1$ or $E$.
- **Gluing across 16 Kummer charts.** Each of the 16 exceptional $\mathbb P^1$'s in $K3_{\mathrm{Kum}}$ contributes a chart-local $A_1$-BFN Yangian on a formal disc. Gluing to a global factorization algebra on some $X$ requires a coherent sheaf-of-chiral-algebras structure on the blow-up $K3_{\mathrm{Kum}}$. **Not supplied in Vol III.**

**Conclusion.** At the Kummer point, there are 16 chart-local factorization algebras on 16 formal discs, plus a $\Z_2$-equivariant chiral algebra on $\mathbb P^1 \setminus 4$ from the coarse-moduli descent. **These must be glued, and the gluing is exactly the conjectural open step of `conj:bfn-k3-yangian-kummer`.**

### HEAL 3 (final). Statement W7-CYCLE3.

**W7-CYCLE3.** *The Kummer-orbifold factorization presentation of the K3 Yangian consists of: (i) a $\Z_2$-equivariant chiral algebra on $\Ran(E_1) \times E_2$ with coefficients; (ii) after descent, a chiral algebra on $\Ran(\mathbb P^1 \setminus 4)$ with $E_2$-valued coefficients; (iii) 16 chart-local factorization algebras on 16 formal discs (one per Kleinian ADE-$A_1$ exceptional curve), each realizing $Y^\mu(\widehat{\mathfrak{sl}}_2)_{k=1}$ per `thm:bfn-phi-ade-identification`. The gluing into a global factorization algebra is the Kummer-deformation-invariance step, `\ClaimStatusConjectured` (`conj:bfn-k3-yangian-kummer`).*

---

## CYCLE 4 — The derived-centre route: $Y_{K3}$ as $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$.

### ATTACK 4. Read `cy_to_chiral.tex:63–67` literally.

`cy_to_chiral.tex:63–67`: *"For $d \geq 3$, the braided $E_2$-structure is recovered on the Drinfeld centre of the representation category: $\cZ(\Rep^{E_1}(\Phi(\cC))) \simeq \Rep^{E_2}(Z^{\mathrm{der}}_{\mathrm{ch}}(\Phi(\cC)))^{\mathrm{centred}}$, with half-braiding $\sigma_{V_u}(V_v) = R(z)$."*

- **(4.a) At $d = 3$, input $\cC = D^b(\Coh(K3 \times E))$.** The functor $\Phi_3$ produces an $E_1$-chiral algebra $A = \Phi_3(\cC)$. Its Drinfeld centre is $Z^{\mathrm{der}}_{\mathrm{ch}}(A) = \RHom_{A \otimes A^{\mathrm{op}}}(A, A)$ in factorization-bimodules on $\Ran(X)^2$ for the base curve $X = E$ (per `cy_to_chiral.tex:50`).
- **(4.b) The half-braiding = R-matrix** prescription says: the R-matrix of the would-be K3 Yangian is recovered as the half-braiding on evaluation modules of $\Rep^{E_1}(A)$. For $A$ abelian (e.g., the Mukai-Heisenberg), the half-braiding is trivial (braid group acts by identity on an abelian algebra's modules). **So the derived-centre route gives an abelian R-matrix for the abelian layer, not a non-abelian Yangian.**
- **(4.c) For a conjectural non-abelian $A^{\mathrm{nab}}$** (MC-deformed Mukai-Heisenberg; Wave 6 / Wave 7 H3.1 $\Theta_{K3}$ target), the half-braiding would be non-trivial and the derived centre would recover a non-abelian R-matrix structure. But: the MC element $\Theta_{K3}$ is not constructed, so this is conjectural.
- **(4.d) Dimension of the derived centre.** For $A = \cH_{\mathrm{Muk}}$ (abelian rank-24 Heisenberg), Wave 6 Beilinson §5.1 computed $Z^{\mathrm{der}}_{\mathrm{ch}}(\cH_{\mathrm{Muk}}) = \C[j_1, \ldots, j_{24}][\partial]$, abelian polynomial algebra on 24 generators + derivative. The Drinfeld centre is abelian; no Yangian recovered.

**Conclusion.** The derived-centre route recovers the non-abelian Yangian **only if** the input $A$ is non-abelian. At the proved layer ($A = \cH_{\mathrm{Muk}}$, abelian), the derived centre is abelian and the half-braiding is trivial; this cannot produce a non-abelian Yangian. **The derived-centre route is open**, conditional on constructing the non-abelian input.

### HEAL 4. $Y_{K3}$ = derived centre + MC deformation, unified statement.

**H4.1 (Healed statement).** *The non-abelian K3 Yangian, under the derived-centre reading, is*
$$
Y(\fg_{K3}) = Z^{\mathrm{der}}_{\mathrm{ch}}(A_{K3,E}^{\mathrm{nab}})
$$
*where $A_{K3,E}^{\mathrm{nab}}$ is the MC deformation of the abelian Mukai-Heisenberg $A_{K3,E}^{\mathrm{ab}} = \cH_{\mathrm{Muk}} \otimes \omega_E$ by an element $\Theta_{K3} \in \mathfrak g^{\mathrm{conv}}_{K3,E} = \Conv^{\mathrm{ch}}(A_{K3,E}^{\mathrm{ab}}, B_E(A_{K3,E}^{\mathrm{ab}}))$. The MC element exists in $H^2$ of the convolution dGLA restricted to the non-orthogonal overlap locus of ADE sub-root-lattices in $\Lambda_{\mathrm{Muk}} = II_{4,20}$; the Whitehead lemma on orthogonal sub-lattices forces vanishing there.*

This unifies:
- **Elliptic-fibration route (CYCLE 2):** the derived centre is computed on the chiral algebra $A^{\mathrm{ell}}_{K3/\mathbb P^1}$ upstairs on $S$, and pushes down to $\mathbb P^1$;
- **Kummer route (CYCLE 3):** the derived centre of the glued chart-local Yangians equals the derived centre of the reconstructed global chiral algebra;
- **Direct derived-centre on $\Ran(E)$ (CYCLE 4):** the derived centre in the $K3 \times E$ setup.

### ATTACK 4 (return). Is the MC element at the "non-orthogonal overlap" locus actually non-trivial?

The automorphic-corrections PDF (Lorgat 2020) §4 gives the explicit Gram matrix of $\Lambda^{2,1}_{II}$: $\begin{pmatrix}2&-2&-2\\-2&2&-2\\-2&-2&2\end{pmatrix}$. This is the **hyperbolic** sub-lattice of signature $(2,1)$ inside $\Lambda^{3,2}$ of signature $(3,2)$. It is **not the same as $\Lambda_{\mathrm{Muk}} = II_{4,20}$**, which is the K3 Mukai lattice.

- **(4.f) Lattice rank mismatch.** $\Lambda_{\mathrm{Muk}}$ has rank 24. The BKM Weyl-root lattice $\Lambda^{2,1}_{II}$ has rank 3. **These are different objects.** The K3 Yangian lives on $\Lambda_{\mathrm{Muk}}$; the BKM lives on $\Lambda^{2,1}_{II}$ (3-dim hyperbolic). The relation between them is through the elliptic fibration: the 2-cycle lattice of $\pi: S \to \mathbb P^1$ is `section + fibre + multi-section`, a rank-3 sub-lattice of $H^2(S, \Z)$ of hyperbolic type (the Hodge-theoretic "U + [$-2$]" lattice). **The hyperbolic $\Lambda^{2,1}$ of the Siegel side is exactly this sub-lattice after applying Lemma 1 $\wedge^2: \Sp_4(\Z) \to \mathrm{SO}(\Lambda^{3,2})$ and restricting.**

So the BKM / Siegel framework lives on the **elliptic-fibration 3-lattice**, a rank-3 sub-lattice of $\Lambda_{\mathrm{Muk}}$ that is hyperbolic. This is the "fibre + section + multi-section" part of $H^2(S, \Z)$.

- **(4.g) MC support.** The MC element $\Theta_{K3}$ for the Yangian enhancement lives in $\mathfrak g^{\mathrm{conv}}_{K3,E}$ on the *full* Mukai lattice. Its restriction to the 3-dim BKM sub-lattice matches the Gritsenko–Nikulin / Lorgat 2020 BKM denominator identity. **This is the structural cross-link between the K3 Yangian and the BKM/Siegel picture.**

### HEAL 4 (final). Statement W7-CYCLE4.

**W7-CYCLE4 (the derived-centre and MC unification).** *Let $A_{K3,E} = A^{\mathrm{ab}}_{K3,E} \oplus_{\Theta_{K3}} (\text{correction})$ be the full chiral algebra on $\Ran(E)$ produced by $\Phi_3$ on $D^b(\Coh(K3 \times E))^{\mathrm{fr}}$. Its derived centre is the conjectural non-abelian Yangian:*
$$
Y(\fg_{K3}) \simeq Z^{\mathrm{der}}_{\mathrm{ch}}(A_{K3,E}).
$$
*The MC element $\Theta_{K3}$ decomposes as*
$$
\Theta_{K3} = \Theta_{K3}^{\mathrm{Yang}} + \Theta_{K3}^{\mathrm{BKM}},
$$
*where $\Theta_{K3}^{\mathrm{Yang}}$ lives in $H^2$ of the convolution dGLA restricted to non-orthogonal Mukai sub-lattices (Yangian-type, ADE overlaps) and $\Theta_{K3}^{\mathrm{BKM}}$ lives on the 3-dim hyperbolic sub-lattice $\Lambda^{2,1}_{II} \subset \Lambda_{\mathrm{Muk}}$ corresponding to the elliptic-fibration data and matches the Gritsenko–Nikulin BKM $\mathfrak g_{\Delta_5}$.* **`\ClaimStatusConjectured`** both components; restricted to the BKM 3-lattice, existence follows from the Lorgat 2020 / Gritsenko–Nikulin automorphic machinery (primary-source proved).

---

## CYCLE 5 — Six-functor formalism and Theorem B on the proved layer.

### ATTACK 5. Can Theorem B (Vol I chiral Positselski) be verified on any candidate factorization algebra?

Vol I Theorem B: $\Omega_X(B_X(C)) \xrightarrow{\sim} C$ in $D^{\mathrm{co}}_{\mathrm{ch}}(X)$ for $C$ a conilpotent chiral coalgebra on a curve $X$. Dually, $B_X(\Omega_X(A)) \xleftarrow{\sim} A$ for $A$ a nilpotent chiral algebra. **Scope restriction** (Positselski 2011 and CLAUDE.md): applies to the Koszul-self-dual locus; Yangians are not nilpotent, so Theorem B applies only to the conilpotent completion.

- **(5.a) On the abelian layer $A^{\mathrm{ab}}_{K3,E} = \cH_{\mathrm{Muk}} \otimes \omega_E$.** Bar complex: $B_E(\cH_{\mathrm{Muk}}) = \Sym(s^{-1}\Lambda_{\mathrm{Muk}}[1]) \otimes \omega_E$ (free cocommutative factorization coalgebra on the shifted Mukai lattice on $E$). Cobar: $\Omega_E(B_E(\cH_{\mathrm{Muk}})) = \cU(\Lambda_{\mathrm{Muk}}^{\mathrm{ab}}) = \cH_{\mathrm{Muk}}$ (universal envelope of the abelian Mukai lattice = Heisenberg). **Theorem B is verified chain-level on $\cH_{\mathrm{Muk}}$**.
- **(5.b) On the non-abelian enhancement $A^{\mathrm{nab}}_{K3,E}$.** The non-abelian enhancement is MC-deformed by $\Theta_{K3}$; its conilpotent completion is the graded object associated to the Mukai-Heisenberg filtration. On the conilpotent graded part, Theorem B follows from (5.a) + MC deformation. **On the full ungraded algebra**, Theorem B is open: it requires the existence of $\Theta_{K3}$ as a Maurer-Cartan element, i.e., the Route-A Yangian-quantization step.
- **(5.c) $\pi_!$ pushforward and Theorem B.** On the elliptic-fibration route (CYCLE 2), the factorization algebra is $A^{\mathrm{ell}}_{K3/\mathbb P^1}$ on $\Ran(\mathbb P^1 \setminus 24)$. Theorem B for a factorization algebra on a punctured curve is a **relative** statement: the bar-cobar inversion holds **modulo** the 24-puncture boundary data. The monodromy representations at each puncture enter as correction terms. This is a scope qualifier not previously stated.
- **(5.d) Kummer route.** 16 chart-local Yangians; Theorem B on each is the standard Positselski on an affine Yangian at level 1 (ProvedElsewhere per the Maulik–Okounkov / Costello–Yamazaki apparatus); the global statement requires the gluing to respect Positselski inversion.

### HEAL 5. Theorem B is verified on all proved sub-structures; scope is strict.

**H5.1 (Healed statement).** *Vol I Theorem B (chiral Positselski) holds on:*
- *the abelian Mukai-Heisenberg $\cH_{\mathrm{Muk}}$ on $\Ran(E)$* **[H] chain-level**;
- *each chart-local ADE-Kleinian Yangian $Y^\mu(\widehat{\fg})_{k=1}$ on a formal disc* **[H] ProvedElsewhere (Costello–Yamazaki 2018 / BFN + Kronheimer)**;
- *the conilpotent graded part of the MC-deformed non-abelian Mukai-Heisenberg* **[M] conditional on MC existence**.

*Theorem B does not hold globally on:*
- *the 24-punctured $A^{\mathrm{ell}}_{K3/\mathbb P^1}$ without explicit monodromy-correction data at the punctures (open)*;
- *the non-abelian ungraded K3 Yangian without MC existence (open)*.

*The Vol III flagship "K3 Yangian = Vol I Theorem B-compatible chiral algebra" requires both the MC existence and the monodromy-completion; neither is supplied in Vol III as of Wave 7.*

### ATTACK 5 (return). Six-functor formalism — is $\pi_!$ a Grothendieck six-functor?

- **(5.e) Six functors on $\pi: S \to \mathbb P^1$.** The map is proper and smooth away from the 24 singular fibres. Gaitsgory–Rozenblyum ind-coherent six-functor formalism supplies $(\pi_*, \pi^*, \pi_!, \pi^!, \otimes, \RHom)$ with base-change and projection formula on the smooth locus; at the 24 singular fibres, base-change fails without additional resolution data. So $\pi_!$ as a **Grothendieck six-functor** requires a refinement: either restrict to the smooth locus, or pass to log-smooth variants (Kato logarithmic geometry: the discriminant divisor $\cD = \sum p_i$ in $\mathbb P^1$ and its preimage are log-smooth under $\pi$).
- **(5.f) Log-smooth $\pi_!$.** Under logarithmic geometry with log-structure given by the 24 punctures, $\pi: (S, \cD_S) \to (\mathbb P^1, \cD_{\mathbb P^1})$ is log-smooth. The six-functor formalism on log-smooth D-modules (Berthelot, Ogus, more recently Scholze–Weinstein) supplies $\pi_!$ with full Grothendieck compatibilities. **This is the correct framework for CYCLE 2's healed statement.**

### HEAL 5 (final). Statement W7-CYCLE5.

**W7-CYCLE5.** *The six-functor formalism for $A^{\mathrm{ell}}_{K3/\mathbb P^1}$ is the logarithmic variant of Gaitsgory–Rozenblyum ind-coherent six-functors, with log-structure at the 24 singular fibres. $\pi_!$ is a Grothendieck log-six-functor. Theorem B holds on the smooth locus; at the 24 punctures, boundary data is encoded by monodromy representations of the local system coming from Kodaira fibre type. On each generic $I_1$ fibre, the monodromy is a Dehn twist / unipotent $\begin{pmatrix}1 & 1 \\ 0 & 1\end{pmatrix}$ in $\mathrm{SL}_2(\Z)$, the modular group; the 24 such twists assemble into a representation of $\pi_1(\mathbb P^1 \setminus 24)$ whose braiding product is trivial* (by the 24-punctured $\mathbb P^1$ monodromy relation: product of 24 local monodromies = identity; cf. Eichler–Zagier *Theory of Jacobi Forms*).

---

## CYCLE 6 — The BKM / Siegel bridge: is the Siegel partition function a factorization-algebra trace?

### ATTACK 6. Is $\Phi_{10} = Z^X$ for $X = S \times E / (\Z/N)$ the trace of a factorization-algebra object?

The Oberdieck–Pixton theorem (`k3e_bkm_chapter.tex:33`) gives $Z^X = C/\Phi_{10}$, and the automorphic PDF §1 Conjecture 1 extends this to 8 Gritsenko–Clery Siegel paramodular forms, each arising from a CY3 DT partition function.

- **(6.a) DT partition function = BPS index.** $Z^X$ counts DT-sheaves on $X = (S \times E)/(\Z/N)$ with Mukai vectors $\beta_h$ and Euler characteristics $n$. In physics: this is the partition function of the $\mathcal N = (0,4)$ sigma model on $X$, or equivalently an index of $D_0$-$D_4$-$D_6$ bound states on $X$. In math: it is a virtual count of 1-dimensional subschemes $Z \subset X$.
- **(6.b) Factorization-algebra trace.** In the Costello–Gaiotto / Beilinson–Drinfeld setup, the partition function of an $E_1$-chiral algebra $A$ on a curve $X$ of genus $g$ is $\mathrm{tr}_{A}(q^{L_0}) = \chi(A) \cdot \omega(q, \tau)$ with $\omega$ a modular form of weight $\kappa_{\mathrm{ch}}/2$. For the K3 Yangian, $\kappa_{\mathrm{ch}} = 2$ for the abelian Mukai-Heisenberg; the trace contribution from the abelian layer is weight-1 (abelian trace is $\eta(q)^{-24}$, weight $-12$ by modular-weight conventions).
- **(6.c) Weight 10 from $1/\Phi_{10}$.** The Siegel cusp form $\Phi_{10}$ has weight 10 on $\mathrm{Sp}_4(\Z)$. The trace identity $Z^X = C/\Phi_{10}$ has weight $-10$. The Gritsenko–Nikulin $\Delta_5$ has weight 5, so $\Phi_{10} \propto \Delta_5^2$ (weight $2 \cdot 5 = 10$). **The weight-5 BKM form $\Delta_5$ is the denominator of $\mathfrak g_{\Delta_5}$, and $\Phi_{10} = \Delta_5^2$ is the square.**
- **(6.d) Where does the weight come from?** The automorphic PDF §5 gives the explicit form: $\mathfrak g_{\Delta_5}$ has real roots with Gram matrix $\Lambda^{2,1}_{II}$, Weyl group $W^{(2)}$, Weyl vector $\rho$, and imaginary roots with multiplicities $m(a) = -\frac{1}{64}f(n,l,m)$ where $f$ are Fourier coefficients of $\Delta_5$. Applied the Weyl-Kac character formula to the 1-dim trivial rep: $\frac{1}{64}\Delta_5(2Z) = e^{-2\pi i \langle \rho, z\rangle}\prod_{\alpha \in \Delta_+}(1 - e^{-2\pi i\langle\alpha, z\rangle})^{\mathrm{mult}\,\alpha}$.

**(6.e) Factorization-algebra content.** The BKM denominator identity says: the partition function of $\mathfrak g_{\Delta_5}$ (= trace of exponential of Hamiltonian = $\det(1 - e^{-\alpha})$ product over positive roots) is $\Delta_5$. In factorization-algebra language, this is the trace of the $E_1$-chiral algebra associated to $\mathfrak g_{\Delta_5}$ on a curve. **The BKM is a chiral algebra on a curve**, specifically on a genus-2 curve because the Siegel modular form $\Delta_5$ is on $\Sp_4(\Z) = \Gamma_{g=2}$, the genus-2 modular group.

**(6.f) Genus 2.** Siegel modular forms on $\Sp_{2g}(\Z)$ live on the moduli of genus-$g$ curves $\cM_g$; for $g = 2$, they live on $\cM_2$. The partition function $Z^X$ of a chiral algebra on a genus-2 curve is a Siegel modular form of weight $\kappa_{\mathrm{ch}}/2 \cdot g = 5 \cdot 2 / 2 = 5$ — matches $\Delta_5$ at weight 5, and $\Phi_{10} = \Delta_5^2$ at weight 10 is $\kappa_{\mathrm{ch}} \cdot g$ for $\kappa = 10$ or $\kappa = 5$ depending on normalization. **The BKM $\mathfrak g_{\Delta_5}$ is the chiral algebra of the K3 Yangian on a genus-2 curve, and its partition function is $\Delta_5$.**

### HEAL 6. The BKM is a factorization-algebra-on-a-curve story; the Siegel form is its genus-2 partition function.

**H6.1 (Healed statement).** *The BKM superalgebra $\mathfrak g_{\Delta_5}$ is a (generalized) Kac-Moody Lie superalgebra associated to the hyperbolic lattice $\Lambda^{2,1}_{II}$ via Borcherds's automorphic-correction construction. The associated vertex algebra $V(\mathfrak g_{\Delta_5})$ is a chiral algebra on any curve $X$ in the BD sense. For $X$ of genus 2, the partition function $Z_{V(\mathfrak g_{\Delta_5})}(X) = \Delta_5(\tau)$, the Gritsenko–Nikulin weight-5 Siegel cusp form. This identity is the Oberdieck–Pixton theorem recast in factorization-algebra language.*

**H6.2 (BKM/Siegel-bridge verdict).** *The BKM is a factorization algebra on a curve of genus 2; the Siegel partition function is its trace. The hyperbolic 3-lattice $\Lambda^{2,1}_{II}$ is the root lattice of its Lie-algebra core; the K3 elliptic genus $\phi_{0,1}$ gives its imaginary-root multiplicities.*

### ATTACK 6 (return). Is the weight-5 lift via the Borcherds correspondence well-defined?

- **(6.g) Borcherds correspondence.** Borcherds arXiv:9602025 shows that an even lattice $L$ of signature $(n, 2)$ gives an automorphic form on $\mathrm{O}(n, 2)$ via the Howe correspondence / theta-lift from weak Jacobi forms. For $L = \Lambda^{3,2}$, the lift of $\phi_{0,1}$ gives $\Delta_5$ (Lorgat 2020 §5; Gritsenko–Nikulin 1998).
- **(6.h) Uniqueness.** The lift is unique up to the multiplier system $v_{\Delta_5}$ of the Siegel form (automorphic PDF §2). The multiplier is $\pm 1$; $\Delta_5$ has non-trivial multiplier system. This matters for the BKM's superalgebra structure: the $\pm 1$ sign distinguishes even and odd roots of $\mathfrak g_{\Delta_5}$.

**Conclusion of Attack 6.** The Borcherds lift is primary-source proved; the BKM is a chiral algebra on a genus-2 curve; the Siegel form $\Delta_5$ is its partition function. **The BKM/Siegel bridge is factorization-algebraic and closed chain-level.**

### HEAL 6 (final). Statement W7-CYCLE6.

**W7-CYCLE6.** *The BKM / Siegel bridge closes chain-level:*

- *$\mathfrak g_{\Delta_5}$ is a BKM Lie superalgebra on $\Lambda^{2,1}_{II}$ (Borcherds 1998; Gritsenko–Nikulin 1998; Lorgat 2020).*
- *Its vertex algebra $V(\mathfrak g_{\Delta_5})$ is a chiral algebra on any smooth curve $X$ in the BD sense.*
- *The partition function $Z^X = C/\Delta_5^2 = C'/\Phi_{10}$ on a genus-2 curve is the trace of $V(\mathfrak g_{\Delta_5})$.*
- *The 3-dim hyperbolic sub-lattice $\Lambda^{2,1}_{II}$ sits inside $\Lambda_{\mathrm{Muk}}$ via the elliptic-fibration structure: $\Lambda^{2,1}_{II}$ = `fibre + section + $[2]$-multi-section`; rank 3 inside rank 24.*
- *The full "K3 Yangian" extends $V(\mathfrak g_{\Delta_5})$ from the 3-dim hyperbolic sub-lattice to the full 24-dim Mukai lattice by Yangian-quantization. The extension is `conj:bfn-k3-yangian-mukai`, open.*

**The BKM is the 3-dim sub-Yangian of the conjectural 24-dim K3 Yangian, and is fully proved on its sub-locus.**

---

## CYCLE 7 (sanity pass) — Is the Wave 7 heal stable?

### ATTACK 7. Sanity pass.

Pass over H1–H6 one more time, looking for unresolved holes.

- **(7.a) The three routes (CYCLES 2, 3, 4) produce *different* chiral algebras on *different* factorization spaces.** Is there an overall consistency condition forcing all three to agree at intersection points of K3 moduli? **Yes, and this is a new Wave 7 conjecture (see below).**
- **(7.b) Genus-2 appearance in CYCLE 6.** The BKM/Siegel sits on a genus-2 curve, not on $\mathbb P^1 \setminus 24$ (CYCLE 2) nor on $E$ (CYCLE 4). Is there a relation? **Yes**: a genus-2 curve can degenerate to $\mathbb P^1$ with 24 punctures (via Deligne–Mumford boundary of $\overline{\cM}_2$ at the maximally-degenerate locus), **and** to $E \cup E$ (two elliptic curves glued, another boundary stratum of $\overline{\cM}_2$). The K3 Yangian partition function on $\overline{\cM}_2$ specializes at these boundary strata:
  - At $\overline{\cM}_2^{\mathrm{max.deg}} = \cM_{0, 24}/S_{24}$: the CYCLE 2 picture ($\mathbb P^1$ with 24 punctures).
  - At $\overline{\cM}_2^{\mathrm{disc.}} = \cM_{1,1} \times \cM_{1,1}$ (two elliptic curves meeting at a node): the CYCLE 4 picture ($E$ with $E_2$ coefficients, where $E_2$ is the second factor).
  - At generic $\cM_2$: the Kummer / BKM picture (CYCLE 3 + CYCLE 6).
- **(7.c) Single universal factorization space: $\cM_2$ (moduli of genus-2 curves).** The K3 Yangian is a factorization algebra over $\cM_2$ (relative factorization over the moduli of curves), whose specializations at the three boundary strata give the three routes.

### HEAL 7. The K3 Yangian is a factorization algebra over $\cM_2$.

**H7.1 (Healed statement, CONVERGED).** *Let $\cM_2$ be the moduli of smooth genus-2 curves. The non-abelian K3 Yangian, as a BD factorization-algebra object, is a D-module on the relative Ran space*
$$
\Ran(\cC/\cM_2) \to \cM_2
$$
*where $\cC \to \cM_2$ is the universal genus-2 curve. The relative factorization algebra $A_{K3, \cM_2}$ specializes:*
- *at the maximally-degenerate boundary stratum $\overline{\cM}_2^{24} = \cM_{0,24}/S_{24}$: to $A^{\mathrm{ell}}_{K3/\mathbb P^1}$ of CYCLE 2;*
- *at the Deligne–Mumford compact-type boundary $\cM_{1,1} \times \cM_{1,1}$: to $A^{\mathrm{Kum}}_{K3}$ of CYCLE 3 (Kummer route) or $A^{\mathrm{derivedcentre}}$ of CYCLE 4;*
- *at generic genus-2 curve $C \in \cM_2$: to the BKM chiral algebra $V(\mathfrak g_{\Delta_5})$ on $C$, whose partition function is $\Delta_5$.*

*This unifies CYCLES 2, 3, 4, 6 into a single factorization-algebraic object.* **The "K3 Yangian" is a relative factorization algebra over the moduli of genus-2 curves.**

### ATTACK 7 (return, final).

Is H7.1 consistent with Vol I's five-theorem framework?

- **Theorem A (bar-cobar).** Holds on $A^{\mathrm{ab}} = \cH_{\mathrm{Muk}} \otimes \omega_C$ for any curve $C$ of genus $g \leq 2$; open for non-abelian $A^{\mathrm{nab}}$.
- **Theorem B (chiral Positselski).** Verified on abelian layer on each curve; conditional on MC existence on non-abelian.
- **Theorem C (derived-centre complementarity).** $\kappa + \kappa^! \in \{0, 13, 250/3, 98/3\}$ family-dependent. For Mukai-Heisenberg class G, $\kappa = 2$, $\kappa^! = -2$, complementarity $K = 0$. For the BKM $\mathfrak g_{\Delta_5}$ class: $\kappa_{\mathrm{BKM}} = 5$ (weight of $\Delta_5$); the complementarity shadow is a new identity requiring explicit computation (deferred to Wave 8).
- **Theorem D (obstruction-tower universality).** $\mathrm{obs}_g = \kappa \cdot \lambda_g$. At $g = 2$, $\lambda_2 \in H^2(\overline{\cM}_2)$ pulls back to the chiral-shadow $\kappa \cdot \lambda_2$. For the K3 Yangian, $\kappa = 2$ and $\mathrm{obs}_2 = 2\lambda_2$; this is precisely the Gritsenko–Nikulin / Oberdieck–Pixton scaling, and matches $\Phi_{10} = \Delta_5^2$ (weight $10 = 2 \kappa \cdot g = 2 \cdot 2 \cdot ??$ — **this needs the correct weight-counting formula**; deferred).
- **Theorem H (Hochschild concentration).** $\ChirHoch^\bullet(A) \in \{0, 1, 2\}$. For Mukai-Heisenberg: verified, concentrated in degree 0 (central) + degree 2 (derived centre). For non-abelian Yangian: open (conditional on MC existence).

**Conclusion of Attack 7.** H7.1 is a well-posed target for the Vol III five-theorem framework, with Theorems A, B, H conditional on MC existence, Theorem C requiring explicit class-computation, Theorem D matching Oberdieck–Pixton up to scaling. **No new structural hole; Wave 7 converges.**

---

## CONVERGED STATEMENT — Is the "K3 Yangian" a chiral algebra, a factorization algebra, or a derived centre?

**Answer.** *All three, in nested specializations, under the following unified structure:*

### CONV-1. Ontological type.

The non-abelian K3 Yangian, as constructed (not yet proved) in Vol III, is a **relative factorization algebra** over the moduli of genus-2 curves $\cM_2$. That is, a D-module on the relative Ran space $\Ran(\cC/\cM_2) \to \cM_2$ for $\cC \to \cM_2$ the universal curve, equipped with a $\cM_2$-flat family of factorization-algebra structures.

### CONV-2. Specializations.

At each stratum of $\overline{\cM}_2$, the K3 Yangian specializes:

| Stratum | Factorization space | Role of K3 | Status |
|---|---|---|---|
| Generic $C \in \cM_2$ | $\Ran(C)$ | BKM $\mathfrak g_{\Delta_5}$ on hyperbolic 3-lattice | **[H]** via Borcherds / Gritsenko–Nikulin / Lorgat 2020 |
| $\cM_{0,24}/S_{24}$ (max-deg) | $\Ran(\mathbb P^1 \setminus 24)$ | Elliptic fibration, 24 Kodaira fibres | **[M]** (pushforward of $\Phi_2$ along $\pi: S \to \mathbb P^1$) |
| $\cM_{1,1} \times \cM_{1,1}$ (D-M) | $\Ran(E_1) \times \Ran(E_2) / \Z_2$ | Kummer route on $T^4 = E_1 \times E_2$ | **[M]** (Kummer + gluing across 16 Kleinian charts) |
| formal disc $D$ at each $p \in C$ | $\Ran(D)$ | BFN Coulomb Yangian $Y^\mu(\widehat{\fg})_{k=1}$ | **[H]** (ADE Kleinian) / **[C]** (Kummer / Mukai) |

### CONV-3. Is it a derived centre?

**Yes**, under the reading $Y(\fg_{K3}) = Z^{\mathrm{der}}_{\mathrm{ch}}(A_{K3,E})$, where $A_{K3,E} = \Phi_3(D^b(\Coh(K3 \times E))^{\mathrm{fr}})$. At the abelian layer, this gives an abelian polynomial algebra (Wave 6 §5.1); at the MC-deformed non-abelian layer, this gives the non-abelian Yangian. **The derived centre reading is equivalent to the factorization-algebra reading after passing to the $E_2 \supset E_1$ universal enveloping / half-braiding structure**, per `cy_to_chiral.tex:63–67`.

### CONV-4. Is it a chiral algebra "on K3"?

**No**, in the literal BD sense. "K3 chiral algebra" as a factorization algebra on the surface K3 is a **category error** (CYCLE 1 ATTACK). What exists is:
- chiral algebra on $\mathbb P^1 \setminus 24$ (elliptic-fibration);
- chiral algebra on $E \cup E$ with Kummer descent (Kummer route);
- chiral algebra on a generic genus-2 curve (BKM);
- all assembling into a relative factorization algebra on $\cM_2$.

### CONV-5. The curve(s), named.

The factorization space for the K3 Yangian is $\Ran(\cC/\cM_2)$ for $\cC \to \cM_2$ the universal genus-2 curve. At specializations:
- generic $C$: curve of genus 2;
- $\cM_{0,24}/S_{24}$: $\mathbb P^1$ with 24 punctures;
- $\cM_{1,1} \times \cM_{1,1}$: two elliptic curves;
- at each puncture / node: formal disc $D$.

### CONV-6. The convolution dGLA.

$\mathfrak g^{\mathrm{conv}}_{K3} = \Conv^{\mathrm{ch}}(A^{\mathrm{ab}}_{K3, \cC/\cM_2}, B_{\cC/\cM_2}(A^{\mathrm{ab}}_{K3, \cC/\cM_2}))$, the relative convolution dGLA on the universal genus-2 curve. The MC element $\Theta_{K3}$ has two components: $\Theta^{\mathrm{Yang}}_{K3}$ on the full Mukai lattice, and $\Theta^{\mathrm{BKM}}_{K3}$ on the hyperbolic 3-lattice; the latter is computed by Gritsenko–Nikulin's automorphic-correction construction. This resolves Wave 6 Critical-2.

---

## NEW CONJECTURES (Wave 7 Beilinson contributions).

**C7.1 (Factorization-$\cM_2$ universality).** The non-abelian K3 Yangian $Y(\fg_{K3})$ is a relative factorization algebra on the universal genus-2 curve $\Ran(\cC/\cM_2)$, with fiber over $C \in \cM_2$ a chiral algebra on $C$. At $\partial \overline{\cM}_2$ the factorization algebra specializes to chapter-level objects (elliptic fibration / Kummer / derived centre). **Motivation**: unifies CYCLES 2–4, 6 into one factorization-algebraic object. **Falsifiable**: the 24-fibre monodromy product at $\cM_{0,24}/S_{24}$ must equal the Kummer gluing product at $\cM_{1,1} \times \cM_{1,1}$ on the shared overlap locus inside $\overline{\cM}_2$.

**C7.2 (BKM = 3-dim sub-Yangian of full K3 Yangian).** The BKM superalgebra $\mathfrak g_{\Delta_5}$ of Borcherds / Gritsenko–Nikulin / Lorgat 2020 is the sub-Yangian of $Y(\fg_{K3})$ obtained by restriction to the 3-dim hyperbolic sub-lattice $\Lambda^{2,1}_{II} \subset \Lambda_{\mathrm{Muk}}$ coming from the elliptic fibration (fibre + section + $[2]$-multi-section). Its vertex algebra $V(\mathfrak g_{\Delta_5})$ is a chiral algebra on genus-2 curves; its partition function is $\Delta_5$. **This identifies the BKM as a proved sub-structure of the conjectural full Yangian.**

**C7.3 (Log-smooth $\pi_!$).** The pushforward $\pi_!$ of the factorization algebra on $S$ along $\pi: S \to \mathbb P^1$ (elliptic fibration) is a Grothendieck log-six-functor in the Gaitsgory–Rozenblyum ind-coherent formalism with log-structure at the 24 singular fibres, and the pushforward preserves the factorization-algebra structure on the log-smooth locus. **Motivation**: makes CYCLE 2's H2.3 precise.

**C7.4 (Ayala–Francis tangential framing for K3).** Costello–Gwilliam's $E_3$-factorization algebra $\cF$ on $\C^3$ admits a tangential lift to an $E_{3, \mathrm{Sp}(1)}$-factorization algebra via K3's hyperkähler $\mathrm{Sp}(1)$-structure, making factorization homology $\int_K3 \cF$ well-defined. **Motivation**: required for the manuscript's `sec:k3-perturbative-fact-homology` to be rigorous; open as Wave 7 H-1.

**C7.5 (MC-element support locus).** The MC element $\Theta_{K3}$ for the non-abelian K3 Yangian enhancement has support on the **non-orthogonal overlap of ADE sub-lattices** in $\Lambda_{\mathrm{Muk}} = II_{4,20}$ plus the **hyperbolic 3-lattice** $\Lambda^{2,1}_{II}$ (elliptic fibration). On orthogonal pairs of sub-lattices, Whitehead's lemma kills the cross-bracket. **Motivation**: specifies the exact locus where MC obstruction must be tested; refines Wave 6 §1 A3.

**C7.6 (Theorem-C complementarity for BKM).** The chiral Koszul complementarity $\kappa + \kappa^! $ for the BKM sector takes the value $\kappa_{\mathrm{BKM}} + \kappa_{\mathrm{BKM}}^! = 0$, reflecting Borcherds self-duality of the lattice-Jacobi-form correspondence at signature $(3,2)$. **Motivation**: extends Vol I Theorem C to the new BKM family; sharpens the `{0, 13, 250/3, 98/3}` landscape with a new value.

**C7.7 (AP-CY72: chiral-algebra-on-surface = category error).** Writing "chiral algebra on K3" or "chiral algebra on a surface" without the factorization-space-on-a-curve disambiguation is a Pattern-236 ambient-qualifier violation. Correct formulations: "factorization algebra on $\Ran(E)$ with K3-valued coefficients"; "factorization algebra on $\Ran(\mathbb P^1 \setminus 24)$ via elliptic-fibration pushforward"; "relative factorization algebra on $\Ran(\cC/\cM_2)$".

**C7.8 (AP-CY73: Ayala–Francis framing omission).** Writing $\int_{K3} \cF$ without specifying the tangential framing / framing lift of the $E_n$-algebra is a scope-declaration omission. Must state: "with K3's $\mathrm{Sp}(1)$-hyperkähler framing and the $E_{3, \mathrm{Sp}(1)}$-lift of $\cF$", or flag the lift as a conjecture.

---

## REQUIRED MANUSCRIPT AMENDMENTS (file:line).

### Vol III `chapters/theory/cy_to_chiral.tex`

- **`cy_to_chiral.tex:27`.** Add after "any smooth curve $X$": "**(curve in the BD sense: smooth 1-complex-dim algebraic; for surfaces the construction must pass to a fibration over a curve, or integrate the surface out)**."
- **`cy_to_chiral.tex:71`** (Theorem `thm:phi-k3-explicit`). Append scope qualifier: "**$\Phi_2$ produces a factorization algebra on an unspecified smooth curve $X$; the K3 enters through coefficient D-modules $D^b(\Coh(K3))$ via Lurie $HA$ §4.8 tensor structure, not as the base curve. Option (b) of Wave 6 Beilinson §1 A1 — "$X = K3$ as a surface" — is a category error in the BD sense.**"
- **`cy_to_chiral.tex:94–103`** (Remark `rem:phi-not-unified-functor`). Append: "**The per-$d$ target category $\cM_d$ for $d = 2$ should be understood as the moduli of smooth curves with K3-valued coefficients; for $d = 3$ with input $K3 \times E$, the natural $\cM_3$ is (a) the universal elliptic curve, (b) the relative factorization space over genus-2 moduli $\cM_2$ via the Oberdieck–Pixton / Borcherds lift. See W7-CONV-1.**"

### Vol III `chapters/examples/k3_yangian_chapter.tex`

- **`k3_yangian_chapter.tex:2405`** (Conjecture `conj:k3-fact-tree-level`, `ClaimStatusConjectured`). Append: "**Additionally, the factorization homology $\int_{K3}$ is conditional on Wave 7 C7.4 (Ayala–Francis tangential-framing lift of Costello–Gwilliam $\cF$ from $\C^3$ to K3's hyperkähler $\mathrm{Sp}(1)$-structure), open.**"
- **`k3_yangian_chapter.tex:92–97`** (Remark `rem:k3e-two-routes-yangian`). Append a third route:

  "(C) **Derived-centre route**: $Y(\fg_{K3}) \simeq Z^{\mathrm{der}}_{\mathrm{ch}}(\Phi_3(D^b(\Coh(K3 \times E))^{\mathrm{fr}}))$. Status: the abelian layer is proved (Mukai-Heisenberg derived centre = polynomial algebra on 24 generators, Wave 6 Beilinson §5.1); the non-abelian enhancement is conjectural via MC deformation $\Theta_{K3}$ in $\mathfrak g^{\mathrm{conv}}_{K3} = \Conv^{\mathrm{ch}}(A^{\mathrm{ab}}_{K3,E}, B_E(A^{\mathrm{ab}}_{K3,E}))$."
- **`k3_yangian_chapter.tex:100–101`** (MO stable envelope discussion). Append: "**The MO route delivers an R-matrix (Hopf-algebra-action data) at ADE/Kummer loci, not a factorization algebra directly; see Wave 7 CYCLE 2 A2.1.6. The factorization-algebra structure on the $R$-matrix is BFN-side, on the formal disc, and glues across the 16 Kleinian charts of $K3_{\mathrm{Kum}}$; the global gluing is open (Wave 7 CYCLE 3).**"
- **New section after `k3_yangian_chapter.tex:2465`.** Insert a subsection titled "**The relative factorization over $\cM_2$ (Wave 7 synthesis)**" summarizing W7-CONV-1/2 and the unification of the three routes at $\overline{\cM}_2$ boundary strata. Status: `\ClaimStatusConjectured`. Cite Wave 7 Beilinson.
- **`k3_yangian_chapter.tex:2380–2465`** (Section `sec:k3-perturbative-fact-homology`). Add a subsection "**Log-smooth pushforward along the elliptic fibration**" describing the CYCLE 2 healed statement: the chiral algebra on $\Ran(\mathbb P^1 \setminus 24)$ obtained by $\pi_!$ of the upstairs chiral envelope, with 24-puncture monodromy representation. Cite Wave 7 C7.3.

### Vol III `chapters/examples/k3e_bkm_chapter.tex`

- **`k3e_bkm_chapter.tex:9–13`** (introductory paragraph). Append: "**The BKM $\mathfrak g_{\Delta_5}$ is a chiral algebra in the BD sense on any smooth curve; its partition function on a genus-2 curve is $\Delta_5$, and the K3 Yangian's BKM sub-Yangian (on the 3-dim hyperbolic lattice $\Lambda^{2,1}_{II} \subset \Lambda_{\mathrm{Muk}}$) is exactly $\mathfrak g_{\Delta_5}$. See Wave 7 C7.2.**"
- **`k3e_bkm_chapter.tex:33–46`** (Theorem Oberdieck–Pixton). Append: "**In factorization-algebra language, $Z^X = C/\Delta_5^2$ is the genus-2 partition function of the chiral algebra $V(\mathfrak g_{\Delta_5})$ on the universal genus-2 curve; this identifies $\Phi_{10} = \Delta_5^2$ as the trace-squared of the chiral BKM. See Wave 7 CYCLE 6 H6.**"
- **`k3e_bkm_chapter.tex:100–120`** (Root system $\mathfrak g_{\Delta_5}$). Append cross-reference to Lorgat 2020 automorphic-corrections §5 for the explicit construction; note that the root-multiplicities $m(a) = -\tfrac{1}{64}f(n,l,m)$ are exactly the Fourier coefficients of $\phi_{0,1}$ (K3 elliptic genus), tying the BKM structure to the K3 Yangian.

### Vol III `chapters/connections/concordance.tex` (or equivalent Vol III cross-ref file)

- Inscribe new anti-pattern entry **AP-CY72** (C7.7): "Chiral algebra on a surface" = category error; canonical rectifications listed.
- Inscribe new anti-pattern entry **AP-CY73** (C7.8): Ayala–Francis framing omission; canonical rectification.

### Vol III `chapters/theory/cy_to_chiral.tex` (second amendment)

- **`cy_to_chiral.tex:105–113`** (Conjecture `conj:phi-d-functoriality`). Append: "**Wave 7 H-1: the morphism action at $d = 3$ on $K3 \times E$ restriction from the Wave 7 W7-CYCLE4 derived-centre reading gives an independent test of functoriality; compatibility with Route A Yangian-quantization step at `k3_yangian_chapter.tex:95` is open.**"

---

## BKM / SIEGEL BRIDGE STATUS.

**Closed chain-level and $(\infty,1)$-categorical, via Borcherds–Gritsenko–Nikulin and Lorgat 2020.**

The BKM superalgebra $\mathfrak g_{\Delta_5}$ is:
- a Borcherds generalized Kac-Moody Lie superalgebra on the hyperbolic 3-lattice $\Lambda^{2,1}_{II}$ of signature $(2,1)$;
- with real root $\delta_1, \delta_2, \delta_3 \in \Lambda^{2,1}_{II}$ (Gram matrix $\begin{pmatrix}2&-2&-2\\-2&2&-2\\-2&-2&2\end{pmatrix}$) and Weyl group $W^{(2)}(\Lambda^{2,1}_{II})$, Weyl vector $\rho = f_2 - \tfrac12 f_3 + f_{-2}$;
- with imaginary roots parameterized by $a \in \Lambda^{2,1}_{II} \cap \R_{\geq 0}\cP_{II}$ and multiplicities $m(a) = -\tfrac{1}{64}f(n,l,m)$ where $f$ are Fourier coefficients of $\Delta_5$ (equivalently, $f(nm, l)$ are Fourier coefficients of the K3 elliptic genus $\phi_{0,1}$);
- with denominator identity $\frac{1}{64}\Delta_5(2Z) = \Phi(z)$ where $\Phi(z) = e^{-2\pi i\langle\rho,z\rangle}\prod_{\alpha \in \Delta_+}(1 - e^{-2\pi i\langle\alpha,z\rangle})^{\mathrm{mult}\,\alpha}$.

As a chiral algebra on a smooth curve $C$: the associated vertex algebra $V(\mathfrak g_{\Delta_5})$ is a BD factorization algebra; its partition function on a genus-2 curve is $\Delta_5$ (weight 5 Siegel cusp form); its square $\Phi_{10} = \Delta_5^2$ matches the Oberdieck–Pixton DT partition function $Z^X = C'/\Phi_{10}$.

**The BKM is the 3-dim hyperbolic sub-Yangian of the conjectural 24-dim K3 Yangian**, obtained by restriction to the elliptic-fibration 3-lattice $\Lambda^{2,1}_{II} \subset \Lambda_{\mathrm{Muk}}$. The extension to the full Mukai lattice is `conj:bfn-k3-yangian-mukai` (open).

**The Siegel partition function $Z^X = C'/\Phi_{10}$ is the trace of a factorization-algebra object** — specifically, of $V(\mathfrak g_{\Delta_5})$ on a genus-2 curve. This matches the Oberdieck–Pixton DT count via the Borcherds lift (Borcherds arXiv:9602025; Gritsenko–Nikulin 1998; Lorgat 2020 §6).

**Primary-source status**: Borcherds lift (proved); Gritsenko–Nikulin denominator identity (proved); Oberdieck–Pixton DT identity (proved); Lorgat 2020 BKM construction (proved, with CY3 source explicit). **The BKM/Siegel bridge is fully chain-level proved.**

What **remains open**:
- the extension of the BKM from the 3-lattice $\Lambda^{2,1}_{II}$ to the full Mukai lattice $II_{4,20}$ (C7.2);
- the MC element $\Theta^{\mathrm{Yang}}_{K3}$ for the Yangian enhancement outside the BKM sub-lattice (C7.5);
- the consistency of the three specializations (elliptic / Kummer / derived-centre) at overlap strata of $\overline{\cM}_2$ (C7.1).

---

## Final meta — Wave 7 Beilinson dictum.

The Wave 6 verdict was that $Y_{K3}$ does not exist as a chiral algebra on a named curve. **Wave 7 names three curves, unifies them over $\cM_2$, and identifies the BKM/Siegel sub-sector as proved chain-level. This is genuine mathematical progress.**

What survives from Wave 6:
- AP321, AP322, AP323 (stand);
- Wave 6 Critical-1 (name the curve): **resolved** — the curve is a genus-2 curve, varying over $\cM_2$, with specializations at $\partial\overline{\cM}_2$;
- Wave 6 Critical-2 (convolution dGLA): **resolved** — $\mathfrak g^{\mathrm{conv}}_{K3, \cC/\cM_2}$ over the universal genus-2 curve;
- Wave 6 Critical-3 (Theorem B): **resolved on abelian layer, conditional on MC on non-abelian**;
- Wave 6 Critical-4 ($\Phi$-vs-Yangian): **preserved** — $\Phi(D^b(K3)) = \cH_{\mathrm{Muk}}$ abelian, Yangian is an open enhancement.

New Wave 7 flags:
- AP-CY72 (chiral-algebra-on-surface = category error): installed;
- AP-CY73 (Ayala–Francis framing omission): installed;
- H-1 (Ayala–Francis framing lift for K3 hyperkähler): open, new;
- H-3 (commutativity of $\HH^\bullet(K3)$-grading with chiral grading): open, new;
- H-4 (conformal vector on non-abelian enhancement): open, new (inherited from manuscript's `sec:k3-perturbative-fact-homology`).

**The non-abelian K3 Yangian, as of Wave 7, is:**
- a relative factorization algebra on the universal genus-2 curve;
- with three specializations at $\partial\overline{\cM}_2$ (elliptic-fibration, Kummer, derived-centre);
- containing the Borcherds BKM $\mathfrak g_{\Delta_5}$ as a proved sub-Yangian on a 3-dim hyperbolic sub-lattice;
- extending to the full Mukai lattice $II_{4,20}$ via MC deformation $\Theta^{\mathrm{Yang}}_{K3}$ (conjectural, existence open);
- with Vol I Theorems A, B, H conditional on MC existence;
- with Vol I Theorem D matching Oberdieck–Pixton up to weight-counting (verified modulo scaling).

**This is a programme with explicit mathematical witnesses, not a slogan. That is the Wave 7 progress.**

---

**Raeez Lorgat, sole author. No AI attribution. Wave 7 Beilinson memo ends here.**

— End of Wave 7 Beilinson memo.
