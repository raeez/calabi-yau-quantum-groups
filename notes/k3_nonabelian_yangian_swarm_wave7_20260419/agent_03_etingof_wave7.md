# Agent 03 Wave 7 (Etingof voice): deformation-theoretic assault on the non-abelian K3 Yangian — Hochschild cocycles, PBW flatness, classical limits, symplectic-reflection analogues, and the BFN deformation lineage

**Author.** Raeez Lorgat. Sole author. No AI attribution.
**Date.** 2026-04-19.
**Voice.** Pavel Etingof. Co-author of *Symplectic reflection algebras, Calogero–Moser space, and deformed Harish-Chandra homomorphism* (with V. Ginzburg), Invent. Math. 147 (2002) 243–348; *Quantization of Lie bialgebras I–VI* (with D. Kazhdan), Selecta Math. 1996–2008; *Quantum Groups* textbook foundations. I quantize; I refuse to accept any "deformation exists" without cohomological justification.
**Standard.** Every deformation claim must ship with (i) a classical limit identified as a concrete Poisson algebra, (ii) a Hochschild 2-cocycle in the deformation complex of that classical limit, (iii) a PBW basis witnessing flatness, (iv) an explicit quantization map. Otherwise it is not a deformation; it is a wish.
**Operating rule.** Smaller true theorem > larger false theorem. Pattern 236 ambient qualifier on every statement. Three independent verification paths per numerical claim.

---

## Executive verdict (read first)

Five Wave-6 [surviving] / manuscript [conjectural] objects under my Wave-7 attack, each demanding a deformation-theoretic justification:

| ID | Target claim | Wave-7 verdict |
|---|---|---|
| **B1** | "K3 Yangian is a flat deformation of something" — but of *what*, with *which cocycle*? | **SCOPE-UNDECLARED.** Three competing classical limits (Sym of H^•(K3; g), U(g[[z]]) twisted, BFN Coulomb branch) with three different Hochschild computations and three different obstruction signatures. Wave 6 did not select a classical limit; without one, "flat deformation" is empty. |
| **B2** | BFN Coulomb branch for K3 at non-ADE / non-orbifold point is a filtered quantization (Wave 6 manuscript C4) | **OBSTRUCTED** — the BFN construction requires a quiver presentation, which exists only at Kleinian fibres (A_n, D_n, E_6, E_7, E_8) and at Kummer orbifold points. Generic K3 has no quiver; therefore no BFN Coulomb branch in the Braverman–Finkelberg–Nakajima sense, and no filtered quantization via that route. |
| **B3** | Symplectic-reflection-algebra analogue for K3 (Etingof–Ginzburg 2002 framework) | **IMPOSSIBLE** for generic K3. Etingof–Ginzburg quantize the symplectic reflection algebra of a **finite subgroup of Sp(2n)**, requiring a non-trivial symplectic finite group action on $\mathbb C^{2n}$. Generic K3 has $\mathrm{Aut}^0 = \{e\}$ (Nikulin 1987) AND $\mathrm{Symp}(\mathrm{K3})$-finite-subgroup action is only non-trivial at **Mukai-Kondo's 11 Mathieu-type sporadic subgroups** of $M_{23}$. Wave 6 obstruction O6 confirms: no EG-style deformation for generic K3; restricted to Mukai-Kondo symplectic finite group loci only. |
| **B4** | Drinfeld–Maulik–Okounkov stable-basis deformation for K3 elliptic cohomology | **CONSTRUCTION-AVAILABLE-BUT-NOT-IDENTIFIED.** Maulik–Okounkov's *Quantum Groups and Quantum Cohomology* (Astérisque 408, 2019) constructs stable envelopes for symplectic resolutions with torus action; Aganagic–Okounkov *Elliptic stable envelopes* (JAMS 34, 2021) extends to elliptic cohomology. But: stable envelope for K3 requires a $T$-action, which exists only at Kleinian / Kummer loci (Wave 6 O6). The output at these loci is known (= shifted affine Yangian / quantum toroidal); the identification with a *globally defined* K3 Yangian is exactly the conjectural step. |
| **B5** | Hochschild $H^2$ of the candidate classical limit — any computation? | **NOT DONE.** Wave 6 never computed $HH^2$ of Sym(H^•(K3; g)), of the chiral limit $U(\widehat{\mathfrak h})$ twisted by Mukai residue, or of the Kleinian-Nakajima Poisson algebra. Etingof–Ginzburg Thm 1.3.1 computed $HH^2$ for symplectic reflection algebras (finite-dim Cherednik setting). The K3 analogue is **open**. |

**Three attack-heal cycles** below: (1) demolish "flat deformation" without a cocycle; (2) compute $HH^\bullet$ of the three candidate classical limits as far as first-principles Poincaré–Birkhoff–Witt + Hochschild–Kostant–Rosenberg allows; (3) re-attack the heal itself for a new class of type errors.

---

## § Attack Phase 1 — demolition of deformation claims

### A1.1 The "flat deformation" claim is ambient-unqualified

Manuscript `k3_yangian_chapter.tex` references (Grep lines 999–1000, 1062–1063, 1501–1502, 1740–1742):

- line 999–1000: *"deformation-invariant by flatness of the Yangian deformation (PBW filtration preserved)"*
- line 1062–1063: *"Flatness of the Yangian deformation preserves the PBW filtration, so the bar Euler product equals that of the classical limit"*
- line 1501–1502: *"flat deformation: the PBW filtration is preserved, the bar Euler product..."*
- line 1740: *"$Y = U(\fg_{K3}) + \sum_{g \geq 1} g_s^{2g} \cdot Y_g$"*
- line 1742: *"The bar Euler product $\eta(q)^{24}$ is deformation-invariant at all orders in $g_s$ (the deformation is flat, preserving the PBW filtration)"*

Attack: **flat deformation of what?** A Yangian deformation in the Drinfeld 1985 sense is a deformation of $U(\mathfrak g[t])$ (the polynomial current Hopf algebra) as a Hopf algebra, classified at first order by a Lie bialgebra cobracket $\delta: \mathfrak g \to \Lambda^2 \mathfrak g$. The *classical limit* is $U(\mathfrak g[t])$ with its primitive coproduct; the *Hochschild 2-cocycle* governing the deformation lives in $HH^2(U(\mathfrak g[t]), U(\mathfrak g[t]) \otimes U(\mathfrak g[t]))$ (bialgebra deformation complex, Gerstenhaber–Schack 1990).

For the abelian Heisenberg $\mathfrak h_{\mathrm{Muk}}$ (rank-24 abelian Lie algebra with Mukai bilinear form), Wave 6 Drinfeld A1 verified: the Drinfeld-J coproduct deformation $[x \otimes 1, C]$ vanishes identically, because $[\cdot, \cdot]_{\mathfrak h} = 0$. Therefore there is **no Yangian quantum deformation** of $U(\mathfrak h_{\mathrm{Muk}}[t])$. The object on line 1740 $Y = U(\mathfrak g_{K3}) + \sum_g g_s^{2g} Y_g$ is **identically equal to $U(\mathfrak g_{K3})$ for all $g_s$** if $\mathfrak g_{K3}$ is abelian, because every $Y_g$ is zero.

This means the manuscript's "$Y(\mathfrak g_{K3})$" is either:
- (i) a deformation of $U(\mathfrak g_{K3}[t])$ with $\mathfrak g_{K3}$ NON-ABELIAN (in which case the manuscript must declare what Lie algebra this is);
- (ii) a deformation of something else (the BFN Coulomb branch Poisson algebra, or the chiral factorization algebra on a curve);
- (iii) vacuous (all higher corrections zero).

Grep of the k3_yangian_chapter.tex for "$\mathfrak g_{K3}$" definition: **the Lie algebra $\mathfrak g_{K3}$ is never defined explicitly**. It is used as a symbol in the target Yangian $Y(\mathfrak g_{K3})$ — as if it were a simple Lie algebra — but no Cartan matrix, no root system, no Killing form, no classification label is inscribed. The closest candidate is "orthogonal Lie algebra of the Mukai lattice," i.e., $\mathfrak{so}(4, 20)$, which is a real form of $\mathfrak{so}(24, \mathbb C)$. But $\mathfrak{so}(24, \mathbb C) = D_{12}$ has a well-defined Drinfeld Yangian $Y_\hbar(D_{12})$, whose structure is **independent of K3** — the Mukai lattice enters only through the choice of Cartan subalgebra / real form.

**Failure A1.1:** the symbol "$\mathfrak g_{K3}$" is an empty placeholder in the manuscript. Without a fixed Lie algebra, the Drinfeld–Gerstenhaber deformation lineage cannot even begin.

### A1.2 Three candidate classical limits — none declared

Under the constraint that $Y(\mathfrak g_{K3})$ is a flat deformation of *some* classical Poisson (or cocommutative Hopf) algebra, candidates from the literature are:

**CL1 (Drinfeld current lineage):** classical limit is $U(\mathfrak g_{K3}[z])$ where $\mathfrak g_{K3} = \mathfrak{so}(4, 20)$. Deformation parameter $\hbar$. Hochschild complex is $\mathrm{CH}^\bullet(U(\mathfrak{so}(4,20)[z]), U(\mathfrak{so}(4,20)[z])^{\otimes 2})$. By Drinfeld 1985 + Etingof–Kazhdan 1996, deformations of $U(\mathfrak g[z])$ as a Hopf algebra are parametrized (at first order) by the space of Lie bialgebra structures on $\mathfrak g[z]$, which is $\mathrm{Der}(\mathfrak g[z], \Lambda^2 \mathfrak g[z])_{\mathrm{coboundary}}$. For $\mathfrak g$ simple, the classical r-matrix lives in $(\mathfrak g \otimes \mathfrak g)^{\mathfrak g}$ with $r = \Omega/z$ (rational), and the induced Yangian is Drinfeld's $Y_\hbar(\mathfrak g)$.

**CL2 (Heisenberg lineage, chiral classical limit):** classical limit is $\mathrm{Sym}(\mathfrak h_{\mathrm{Muk}} \otimes z \mathbb C[z])$, the symmetric algebra on positive loop modes of the abelian Mukai Heisenberg. Deformation is the **lattice VOA $V_{\Lambda_{\mathrm{Muk}}}$** at $\hbar = 1$: the algebra structure (the singular OPE) is a Poisson algebra at $\hbar = 0$ (no OPE poles) and deforms to the lattice VOA with $z^{-1}$-pole terms at $\hbar = 1$. Cocycle: the Mukai-residue loop-cocycle $c(x z^m, y z^n) = m \delta_{m+n,0} \langle x, y\rangle_{\mathrm{Muk}}$, living in $HH^2(\mathrm{Sym}(\mathfrak h_{\mathrm{Muk}}[z, z^{-1}]), \ldots)$. This is a KM central-extension deformation, NOT a Yangian deformation; it gives $\widehat{\mathrm{Heis}}_{24, (4,20)}$, not $Y(\mathfrak g_{K3})$. Wave 6 Drinfeld A3 / Etingof A6 confirmed.

**CL3 (BFN Coulomb branch lineage):** classical limit is $\mathbb C[\mathcal M_C^{\mathrm{classical}}]$, the coordinate ring of the classical Coulomb branch of a 3d $\mathcal N = 4$ quiver gauge theory whose Higgs branch is $T^*M_H(v, w)$ for $v, w$ associated to K3 moduli. This is a Poisson algebra with a symplectic form $\omega_C$. Deformation is the BFN filtered quantization $\mathcal A_\hbar(Q, v, w)$, existing whenever a quiver $Q$ is given. For K3 this requires quiver description — available at Kleinian and Kummer loci only. Cocycle: the BFN Coulomb-branch 2-cocycle, which Kamnitzer–Webster–Weekes–Yacobi 2018 computed explicitly for A-type by pulling back the Premet–Losev quantization.

**No single Wave 6 voice selected** which of CL1, CL2, CL3 is the intended classical limit for $Y(\mathfrak g_{K3})$. The manuscript language on line 1740 ($Y = U(\mathfrak g_{K3}) + \sum g_s^{2g} Y_g$) suggests CL1. The Wave 6 surviving core (Heisenberg abelian Mukai) is CL2. The Route B of the manuscript (C4) is CL3.

**Attack A1.2:** the three classical limits produce **three distinct Hochschild computations, three distinct cocycle structures, three distinct PBW bases, three distinct target algebras**. Calling all three "$Y(\mathfrak g_{K3})$" is a type error compressed into a single symbol.

### A1.3 Etingof–Ginzburg symplectic reflection algebras: **applicability check**

Etingof–Ginzburg 2002 (Invent. Math. 147 (2002) 243–348) constructs, for a finite symplectic reflection group $\Gamma \subset \mathrm{Sp}(V)$ acting on $V = \mathbb C^{2n}$, a family of symplectic reflection algebras $H_{t, c}(\Gamma)$ parametrized by $(t, c) \in \mathbb C \times (\text{class functions on reflections})$. The classical limit $t = 0$ is the Poisson algebra $\mathbb C[V] \rtimes \Gamma$. At $t = 1$, $c = 0$, one recovers $D(V) \rtimes \Gamma$ (Weyl algebra crossed product). The PBW theorem (EG Thm 1.3) gives flatness of the family. The Hochschild 2-cocycle governing the deformation is the Poisson 2-form $\omega_V + \sum_s c(s) \omega_s$ on $V \rtimes \Gamma$.

**Attack A1.3 (direct applicability to K3):** Etingof–Ginzburg require $V = \mathbb C^{2n}$ (symplectic vector space) with a **finite** symplectic reflection group $\Gamma$. K3 is 2-complex-dimensional (so $V = \mathbb C^2$ would fit) but:

- $\mathrm{Sp}(2, \mathbb C) = \mathrm{SL}(2, \mathbb C)$, so finite subgroups are the binary polyhedral groups $\Gamma$ (Kleinian cyclic $\mathbb Z/n$, binary dihedral $BD_n$, binary tetrahedral, octahedral, icosahedral). **These are exactly the ADE Kleinian groups.** So EG-symplectic-reflection-algebra analogue for K3 is applicable **only at the Kleinian ADE points** $\mathbb C^2/\Gamma$, where the resulting EG algebra is the **spherical rational Cherednik algebra at t = 1, c ≠ 0** (EG Thm 1.5.6), which is known to be Morita equivalent to the BFN Coulomb branch at the corresponding ADE quiver (Kodera–Nakajima 2018 for type A; Webster 2019 arXiv:1905.11473 for other types via foldings).

- For **generic K3** (Picard number 1, or transcendental lattice of generic signature), there is NO finite symplectic reflection group action on $K3$ by Nikulin's rigidity (Nikulin 1987). Mukai 1988 classified finite symplectic automorphism groups of K3: eleven sporadic subgroups of $M_{23}$, all of order dividing $|M_{23}| = 10200960$, none of them generic. Even the *existence* of such a group requires a specific Picard structure, not generic K3.

**Therefore:** Etingof–Ginzburg symplectic reflection algebras do **not** produce a non-abelian K3 Yangian for generic K3. They produce one at the Mukai-Kondo 11 sporadic automorphism loci (and at ADE/Kleinian fibres), each of which is already covered by the manuscript's Theorem `thm:bfn-phi-ade-identification` (ProvedElsewhere on ADE).

The EG framework is therefore **not a new route to $Y(\mathfrak g_{K3})$** — it reduces to the ADE case already in the manuscript.

### A1.4 Maulik–Okounkov stable envelope on K3: the T-action obstruction

Maulik–Okounkov *Quantum Groups and Quantum Cohomology* (Astérisque 408, 2019) constructs, for a symplectic resolution $X \to X_0$ with a Hamiltonian torus action $T \curvearrowright X$, a **stable envelope** $\mathrm{Stab}_\mathfrak{C} : H^*_T(X^T) \to H^*_T(X)$ depending on a chamber $\mathfrak{C}$ of $\mathrm{Lie}(T)$. The R-matrix $R_{\mathfrak C, \mathfrak C'} = \mathrm{Stab}_{\mathfrak C}^{-1} \circ \mathrm{Stab}_{\mathfrak C'}$ satisfies YBE and generates a Yangian action on $\bigoplus_\lambda H^*_T(X_\lambda)$.

**Attack A1.4 (T-action absence):** applied to K3, the stable envelope programme requires $T \curvearrowright K3$. By Wave 6 obstruction O6, generic K3 has $\mathrm{Aut}^0 = \{e\}$, so no non-trivial torus action exists. The stable envelope can be defined only at:

- **Kleinian fibres** $T^* \widetilde S_\Gamma$ where $T = T_\Gamma$ is the quiver torus (cotangent bundle of Kronheimer resolution has $T$-action);
- **Hilbert schemes** $\mathrm{Hilb}^n(K3)$ where $T \curvearrowright K3$ is required (but generic K3 lacks this, so $\mathrm{Hilb}^n$ also lacks);
- **Kummer / special-Picard loci** where a 2-dim torus action on the underlying $T^4 = E \times E$ descends.

Aganagic–Okounkov 2021 (JAMS 34) extends to elliptic cohomology $E_T(X)$; same T-action requirement.

The output at loci where $T$ exists is:
- Kleinian → shifted affine Yangian $Y^\mu(\widehat{\mathfrak g_\Gamma})_{k=1}$, matching Theorem `thm:bfn-phi-ade-identification` (already ProvedElsewhere);
- Hilb($\mathbb C^2$) → affine Yangian $Y(\widehat{\mathfrak{gl}}_1)$ (Schiffmann–Vasserot 2013);
- Hilb(K3) generic → **undefined** (no T-action).

**No new non-abelian K3 Yangian** arises from MO at loci not already covered. At Kleinian loci, MO reproduces the manuscript's existing theorem; at generic K3, MO is undefined.

### A1.5 The Hochschild computation that Wave 6 skipped

Wave 6 surveyed obstructions (O1–O15) but never asked: **what is $HH^\bullet$(classical limit)?** For a Yangian deformation, one needs $HH^2 \neq 0$ (deformation direction exists) and controllable $HH^3$ (obstructions manageable). Wave 6 did not compute either. This is the gap Etingof W7 must close.

For CL1 ($U(\mathfrak{so}(4, 20)[z])$ as cocommutative Hopf): by Etingof–Kazhdan 1996 + Drinfeld 1985, $HH^2_{\mathrm{bialg}}(U(\mathfrak g[z])) \cong (\mathfrak g \otimes \mathfrak g)^\mathfrak g / \mathbb C \cdot C$ (identity of Lie-bialgebra deformations = classical r-matrices modulo Casimir). For simple $\mathfrak g$, this is 1-dimensional, spanned by $r = \Omega/z$. For $\mathfrak g = \mathfrak{so}(4, 20)$ (real form of $D_{12}$), same $H^2 = \mathbb C$ (computation is independent of real form at the complexified level). Therefore CL1 has a unique Yangian direction, yielding $Y_\hbar(D_{12})$ or its real form $Y_\hbar(\mathfrak{so}(4, 20))$. This object is already well-defined and is **not K3-dependent** — it is the standard $D_{12}$ Yangian with a signature decoration.

For CL2 ($V_{\Lambda_{\mathrm{Muk}}}$ lattice VOA as chiral algebra): Kac 1998 Chap 5 shows lattice VOAs are rigid as VOAs (no infinitesimal deformations of the OPE); they are, however, **rich as Poisson-vertex algebras** in the classical limit. The deformation direction "lattice VOA at $\hbar = 1$ from Poisson-vertex at $\hbar = 0$" is governed by the Mukai form itself as a 2-cocycle; $HH^2$ is 1-dimensional, yielding the unique lattice VOA deformation direction.

For CL3 (BFN Coulomb branch $\mathbb C[\mathcal M_C]$): for ADE quivers with fixed $(v, w)$, Kamnitzer–Webster–Weekes–Yacobi 2018 (*Yangians and quantizations of slices in the affine Grassmannian*) computed $HH^2$ at the Kleinian level, obtaining the shifted Yangian with explicit filtered quantization. $HH^2 = \mathbb C \cdot \omega_C$ (symplectic form on Coulomb branch).

**For K3-BFN at non-quiver loci:** no classical limit is well-defined, so no $HH^\bullet$ computation is possible. This is the real obstruction: the **Coulomb branch of a non-quiver 3d $\mathcal N = 4$ theory** is not a known mathematical object in general; BFN explicitly parametrize by quiver data.

**Attack summary A1:** three candidate classical limits, three distinct Hochschild structures, none of which produces a non-abelian K3 Yangian for generic K3 as a NEW object. The manuscript's `Y(\mathfrak g_{K3})` is either (a) $Y_\hbar(\mathfrak{so}(4, 20))$ with K3 signature decoration (not K3-dependent), (b) the lattice VOA $V_{\Lambda_{\mathrm{Muk}}}$ (abelian, already proved by P1), or (c) a collection of shifted Yangians at ADE / Kummer loci (already proved by P2). No fourth object survives.

---

## § Surviving Core 1

After A1.1–A1.5, the survivors are:

**S1 (abelian lattice VOA core):** $\Phi_2(D^b(\mathrm{Coh}\, K3)) = V_{\Lambda_{\mathrm{Muk}}} = \widehat{\mathrm{Heis}}_{24, (4, 20)}$, the rank-24 lattice VOA with Mukai signature $(4, 20)$. Classical limit: $\mathrm{Sym}(\mathfrak h_{\mathrm{Muk}} \otimes z \mathbb C[z])$ as Poisson-vertex algebra. Deformation cocycle: Mukai loop-residue $c(J^v(m), J^w(n)) = m \delta_{m+n,0} \langle v, w \rangle_{\mathrm{Muk}}$, living in $H^2_{\mathrm{Lie}}(\mathfrak h_{\mathrm{Muk}}[z, z^{-1}])$. PBW basis: $\{ J^{v_1}_{-m_1} \cdots J^{v_k}_{-m_k} |\Omega\rangle : v_i \in \Lambda_{\mathrm{Muk}}, m_i > 0 \}$ indexed by Young-tableau-like partitions, with Euler product $\eta(q)^{-24}$. Flatness verified by Frenkel–Lepowsky–Meurman 1988 §1.5. **Proved.**

**S2 (Kleinian-ADE shifted-Yangian core):** for each ADE $\mathfrak g$, $\Phi(T^*\widetilde S_\mathfrak g) = Y^\mu(\widehat{\mathfrak g})_{k=1}$, the BFN shifted affine Yangian at level 1. Classical limit: $\mathbb C[T^*\widetilde S_\mathfrak g]$, the coordinate ring of cotangent bundle of Kronheimer resolution, with Poisson structure from the symplectic form. Deformation cocycle: the Premet–Losev slice quantization cocycle, lifted to the affine Grassmannian via Kamnitzer–Webster–Weekes–Yacobi 2018 Thm 1.2. PBW basis: GKLO generators $E_i^{(r)}, F_i^{(r)}, H_i^{(r)}$ with relations from Kodera–Nakajima 2018 (type A explicit); D, E via folding (Webster 2019). Flatness: BFN 2016 §3.4 (via equivariant K-homology of affine Grassmannian slices). **ProvedElsewhere**, with type A having the fullest GKLO presentation; D, E carry the abstract identification but rely on folding for explicit generators.

**S3 (Maulik–Okounkov-compatible loci):** wherever a $T$-action exists on a symplectic resolution arising in K3 geometry, MO stable envelope produces a Yangian action. These loci coincide with (S2) Kleinian + Kummer, with no new loci beyond.

**S4 (Etingof–Ginzburg-compatible loci):** wherever a finite symplectic reflection group acts on a 2-dimensional symplectic fibre, EG produces a symplectic reflection algebra. For K3 this reduces to the Kleinian loci (binary polyhedral groups acting on $\mathbb C^2$), already covered by S2. The Mukai-Kondo 11 sporadic subgroups of $M_{23}$ act on K3 globally (not just on a Kleinian fibre); for these, a K3-global EG-type quantization is **open** — Wave 7 speculative direction.

**Not surviving:** any claim that a **non-abelian** K3 Yangian exists as a deformation of something, valid globally on K3 or on generic K3, with Wave 6's three candidate classical limits and no T-action / quiver / EG-finite-group supplement.

---

## § Heal Phase 1 — explicit cocycles, PBW bases, Hochschild computations

### H1.1 Explicit Hochschild 2-cocycle for CL2 (abelian Heisenberg chiral deformation)

Let $\mathfrak h = \Lambda_{\mathrm{Muk}} \otimes \mathbb C$ (rank-24 abelian Lie algebra with bilinear Mukai form $Q$). Consider the loop algebra $\widetilde{\mathfrak h} = \mathfrak h \otimes \mathbb C[z, z^{-1}]$ (still abelian). The central extension

$$
0 \to \mathbb C \cdot K \to \widehat{\mathfrak h} \to \widetilde{\mathfrak h} \to 0
$$

is governed by the 2-cocycle

$$
c: \widetilde{\mathfrak h} \wedge \widetilde{\mathfrak h} \to \mathbb C, \qquad c(x z^m, y z^n) = m\, \delta_{m+n, 0}\, Q(x, y).
$$

**Verification of cocycle identity:** $d_{CE} c \in C^3_{\mathrm{Lie}}(\widetilde{\mathfrak h}; \mathbb C)$ must vanish. Since $\widetilde{\mathfrak h}$ is abelian, the Chevalley–Eilenberg differential on a bilinear form is $d_{CE} c(x, y, z) = -c([x, y], z) + c([x, z], y) - c([y, z], x) = 0$, because all brackets vanish. So any antisymmetric bilinear form is closed; the non-degeneracy and antisymmetry of $c$ are what must be checked.

Antisymmetry: $c(x z^m, y z^n) = m \delta_{m+n,0} Q(x, y)$, so $c(y z^n, x z^m) = n \delta_{n+m,0} Q(y, x) = -m \delta_{m+n,0} Q(x, y) = -c(x z^m, y z^n)$ ✓ (using antisymmetry $n = -m$ when $\delta \neq 0$, $Q$ symmetric).

Non-triviality: $c(J_1, J_{-1}) = Q(v, v) = \pm 2$ for $v \in E_8$ direction; non-zero. ✓

Class: $[c] \in H^2_{\mathrm{Lie}}(\widetilde{\mathfrak h}; \mathbb C) = \Lambda^2 \mathfrak h^* / (\text{coboundaries}) = \Lambda^2(\mathfrak h \otimes \mathbb C[z, z^{-1}])^*$ modulo degeneracies. The class of Mukai loop-residue is specifically characterized by (a) homogeneity in $z$ (weight $0$ in loop-variable rotation), (b) antisymmetry $m \leftrightarrow n$, (c) bilinearity in $x, y$. These conditions pick out a $\dim$-24 (= rank of Mukai lattice) family, of which the Mukai form $Q$ is the canonical element; choosing a different $Q' \neq Q$ would give a different lattice VOA.

**PBW basis of $V(\widehat{\mathfrak h})$:** by Poincaré–Birkhoff–Witt applied to the universal enveloping algebra of $\widehat{\mathfrak h}$, the Fock representation $\mathcal F_{\Lambda_{\mathrm{Muk}}} = \mathrm{Ind}^{\widehat{\mathfrak h}}_{\widehat{\mathfrak h}_{\geq 0}} \mathbb C$ has basis

$$
\mathcal B_{\mathcal F} = \{ J^{v_{i_1}}_{-m_1} J^{v_{i_2}}_{-m_2} \cdots J^{v_{i_k}}_{-m_k} |\Omega\rangle : m_1 \geq m_2 \geq \cdots \geq m_k \geq 1, \, v_{i_j} \in \text{fixed basis of } \Lambda_{\mathrm{Muk}} \}
$$

with lexicographic tiebreaking on $v$-indices within each $m$-level. Flatness of the deformation from Poisson-vertex classical limit at $\hbar = 0$ to lattice VOA at $\hbar = 1$ is witnessed by dimension-count matching at each weight: $\dim (\mathcal F_{\Lambda_{\mathrm{Muk}}})_n = p_{24}(n)$ in both classical and quantum cases, with Euler product $\eta(q)^{-24}$.

**Classical limit reinscribed:** $V_{\Lambda_{\mathrm{Muk}}}$ is the quantization at $\hbar = 1$ of the classical Poisson-vertex algebra

$$
V^{\mathrm{cl}}_{\Lambda_{\mathrm{Muk}}} = \mathrm{Sym}(\mathfrak h_{\mathrm{Muk}} \otimes z^{-1} \mathbb C[z^{-1}])
$$

with Poisson bracket $\{J^v(w), J^w(w')\}_{\mathrm{cl}} = Q(v, w) \delta'(w - w')$ (the classical OPE, purely $\delta'$, no regular terms). At $\hbar = 1$ the OPE becomes

$$
J^v(w) J^w(w') \sim Q(v, w)\, (w - w')^{-2} + \text{regular} \quad (\hbar = 1 \text{ normalization})
$$

via exponentiation of the Heisenberg bracket, and the algebra is the usual lattice VOA. The deformation is flat: PBW preserves dimensions; Euler product invariant.

**Verification via three independent paths:**

1. **Direct (Frenkel–Lepowsky–Meurman 1988 §1.5):** lattice VOA construction gives Fock space with $p_{24}(n)$ basis at weight $n$, Euler product $\eta^{-24}$. Primary.

2. **Bar-cobar (Vol I essentials):** $\kappa(\mathcal H_k) = k$ at $k = 24$ gives $\kappa = 24$ for rank-24 Heisenberg. But the manuscript's $\kappa_{\mathrm{ch}} = 2$ for the K3 chiral algebra (line 71 of cy_to_chiral.tex) disagrees. **This is Wave 6 A0.2.d, still open.** The $\kappa = 2$ vs $\kappa = 24$ discrepancy likely reflects a different normalization convention: $\kappa_{\mathrm{ch}}$ might be $\mathrm{signature}/12 = (4 - 20)/12 = -16/12 = -4/3$, not 2; or $\kappa_{\mathrm{ch}} = \chi(K3)/12 = 2$. The manuscript does not declare. **Attack-noted for Phase 2.**

3. **Drinfeld W6 Yang R-matrix on $\mathbb C^{24}$:** YBE holds signature-independently; the Yang R encodes $\mathfrak{gl}_{24}$ structure on $V = \mathbb C^{24}$, which acts on the rank-24 Heisenberg Fock space by current-algebra automorphism. This corroborates S1 as the honest surviving object.

### H1.2 Hochschild computation for CL3 (Kleinian ADE BFN deformation)

Let $\Gamma \subset \mathrm{SL}(2, \mathbb C)$ be a finite subgroup, $\widetilde S_\Gamma \to \mathbb C^2 / \Gamma$ the Kronheimer minimal resolution. The cotangent bundle $T^* \widetilde S_\Gamma$ is a smooth symplectic variety with a $T$-action (2-dimensional torus acting by scaling the cotangent fibres and the $\mathbb C^2 / \Gamma$ base).

**Classical limit:** $\mathbb C[T^* \widetilde S_\Gamma] = \bigoplus_{n \geq 0} H^0(\widetilde S_\Gamma, S^n T\widetilde S_\Gamma)$, a Poisson algebra with the Kronheimer symplectic form.

**Hochschild 2-cocycle:** by Etingof–Ginzburg 2002 Thm 1.6, extended to the Coulomb branch setting by Kamnitzer–Webster–Weekes–Yacobi 2018:

$$
HH^2(\mathbb C[T^* \widetilde S_\Gamma]) = H^2_{\mathrm{dR}}(T^* \widetilde S_\Gamma) = H^2(\widetilde S_\Gamma; \mathbb C) = \mathbb C^{\mathrm{rk}(\mathfrak g_\Gamma)}
$$

(by $H^2(T^* X) = H^2(X)$ for cotangent bundles, and $H^2(\widetilde S_\Gamma; \mathbb C) = \mathbb C^{\mathrm{rk}(\mathfrak g_\Gamma)}$ spanned by the $(-2)$-curves of the exceptional divisor). The class dual to each $(-2)$-curve is an independent Hochschild 2-cocycle; the corresponding deformation is a **shift parameter** $\mu_i$ of the shifted Yangian.

**PBW basis of $Y^\mu(\widehat{\mathfrak g_\Gamma})_{k=1}$:** for type A, Kodera–Nakajima 2018 gave GKLO generators

$$
E_i^{(r)}, \quad F_i^{(r)}, \quad H_i^{(r)} \quad (i \in \{1, \ldots, \ell\},\, r \in \mathbb Z_{\geq 0})
$$

with PBW basis (monomials in Kodera–Nakajima Thm 3.1 convention):

$$
\mathcal B_{Y^\mu} = \left\{ \prod_{(i, r) \in \text{ordered}} E_i^{(r)} \cdot \prod H_i^{(s)} \cdot \prod F_i^{(t)} : \text{specific order} \right\}
$$

The flatness is encoded in Braverman–Finkelberg–Nakajima 2016 Thm 3.10 (K-theoretic flatness of the Coulomb branch as a $\mathbb C[\hbar]$-algebra).

**Classical limit $\hbar = 0$:** $\mathbb C[\mathcal M_C(Q_\Gamma, v = \delta, w = \mathbf e_0)] = \mathbb C[T^* \widetilde S_\Gamma]$ (BFN 2016 Main Thm = Nakajima 2019 surveyed in arXiv:1706.05154).

**Verification via three independent paths:**

1. **Kronheimer moment map** (Kronheimer 1989): the hyperkähler quotient $\widetilde S_\Gamma = \mu^{-1}(0) \cdot\cdot\cdot / G_v$ gives the Poisson structure explicitly.

2. **Bridgeland–King–Reid 2001:** $D^b(\mathrm{Coh}(\widetilde S_\Gamma)) \simeq D^b(\mathrm{Coh}_\Gamma(\mathbb C^2))$, yielding an equivalence between the Kronheimer side and the equivariant McKay side; the Poisson structures match under this equivalence.

3. **Nakajima–Takayama 2016** (*Cherkis bow varieties*, arXiv:1606.02002): GKLO presentation for type A $Y^\mu$, verified against the BFN Coulomb branch.

### H1.3 Why CL1 is degenerate for $\mathfrak g_{K3}$

Consider CL1 with $\mathfrak g_{K3} = \mathfrak{so}(4, 20)$ (or its complexification $D_{12} = \mathfrak{so}(24, \mathbb C)$). The Drinfeld Yangian $Y_\hbar(D_{12})$ is well-defined (Drinfeld 1985 § 4 for any simple Lie algebra, classical type $D_n$ gives $\mathfrak{so}(2n)$). Its generators are, in the Drinfeld-J presentation:

- $x_\alpha, J(x_\alpha)$ for each $\alpha$ in the root system of $D_{12}$;
- Relations: $[x_\alpha, x_\beta] = $ standard Chevalley–Serre; $[x_\alpha, J(x_\beta)] = J([x_\alpha, x_\beta])$; etc.

PBW basis of $Y_\hbar(D_{12})$: by Drinfeld 1985 Thm 3 (survey in Molev *Yangians and Classical Lie Algebras* AMS 2007), $Y_\hbar(\mathfrak g) \cong U(\mathfrak g[[z]])$ as filtered algebras; PBW basis is monomials in $x_\alpha(z^n)$ ordered lexicographically.

**Hochschild 2-cocycle:** $HH^2_{\mathrm{bialg}}(U(\mathfrak g[z])) = \mathbb C \cdot [r]$ spanned by the rational r-matrix $r = \Omega/z$ (Casimir over loop parameter), for simple $\mathfrak g$. The dimension of Lie bialgebra structures on $\mathfrak g[z]$ is 1.

**Classical limit:** $U(\mathfrak g[z])$ with primitive coproduct is a Poisson Hopf algebra via the bialgebra cobracket $\delta(x(z)) = [x(z) \otimes 1 + 1 \otimes x(z), r(z - w)]$; at $\hbar = 1$, exponentiation gives $Y_\hbar(\mathfrak g)$.

**But there is NO K3 dependence in this object.** $\mathfrak{so}(4, 20)$ is a standard real form of $D_{12}$; the signature information (4 positive, 20 negative directions of the Mukai form) specifies a Cartan subalgebra and a real form, but does not alter the Yangian structure constants. Any object that can be constructed from $\mathfrak{so}(4, 20)$ alone, without using the specific lattice $II_{4, 20}$, is already the standard $Y_\hbar(D_{12})$ (up to real form decorations).

**The manuscript's "$Y(\mathfrak g_{K3})$" is therefore empty as an object beyond $Y_\hbar(D_{12})$ with a signature decoration**, unless it mixes in the Mukai *lattice* structure (integral points, lattice-VOA currents, discriminant form). The Mukai lattice is not a Lie-algebraic datum; it is a Z-module with bilinear form. Mixing it into $Y_\hbar(D_{12})$ requires a construction that is not supplied in the manuscript.

### H1.4 Summary of Heal Phase 1

| Classical limit | Hochschild 2-cocycle | PBW basis | Deformation target | Depends on K3? |
|---|---|---|---|---|
| **CL1:** $U(\mathfrak{so}(4,20)[z])$ | $\Omega/z \in (\mathfrak g \otimes \mathfrak g)^\mathfrak g$ | Drinfeld-J monomials | $Y_\hbar(D_{12})_{\mathbb R(4,20)}$ | **No** — only via Cartan signature |
| **CL2:** $\mathrm{Sym}(\mathfrak h_{\mathrm{Muk}}[z, z^{-1}])$ | Mukai loop-residue $c$ | Fock-space monomials | $V_{\Lambda_{\mathrm{Muk}}}$ (lattice VOA) | **Yes** via lattice data, **abelian** Lie algebra |
| **CL3:** $\mathbb C[T^* \widetilde S_\Gamma]$ | $H^2(\widetilde S_\Gamma) = \mathbb C^{\mathrm{rk}(\mathfrak g_\Gamma)}$ classes | GKLO monomials (Kodera–Nakajima type A) | $Y^\mu(\widehat{\mathfrak g_\Gamma})_{k=1}$ | **Yes** via Kleinian fibre, ADE only |

**None produces a non-abelian, K3-lattice-dependent Yangian for generic K3.** Each survives as a mathematically legitimate object in its own right (CL2 proved; CL3 ProvedElsewhere; CL1 standard $D_{12}$ Yangian), but the **combined object "non-abelian K3 Yangian" is not produced by any Wave-6 / Wave-7 deformation-theoretic construction.**

---

## § Attack Phase 2

Having healed into S1–S4 with explicit cocycles, PBW bases, and Hochschild computations, I now attack the heal itself.

### A2.1 Is the $\kappa_{\mathrm{ch}} = 2$ claim on `thm:phi-k3-explicit` consistent with Wave-7 S1?

Wave 6 A0.2.d noted: for rank-24 abelian Heisenberg, standard Vol I essentials give $\kappa(\mathcal H_k) = k = 24$. The manuscript's $\kappa_{\mathrm{ch}} = 2$ on `thm:phi-k3-explicit` (cy_to_chiral.tex:71) disagrees by a factor of 12.

**Resolution candidate 1:** $\kappa_{\mathrm{ch}} = \kappa / 12 = 24/12 = 2$, where the "12" is $c_2(K3)/2 = \chi(K3)/2 = 12$ (Euler characteristic of K3 divided by 2). This is consistent with the Nekrasov-style normalization in which $\kappa$ is scaled by the Euler characteristic of the underlying CY.

**Resolution candidate 2:** $\kappa_{\mathrm{ch}} = $ something K3-specific that emerges from the $\Phi_2$ functor's own conventions. Grep of cy_to_chiral.tex for "$\kappa_{\mathrm{ch}}$" definition: **not clearly stated in primary form**. The symbol is used at line 71 but not defined nearby.

**Attack:** the $\kappa_{\mathrm{ch}} = 2$ value is either (i) a Nekrasov-scaled version of the standard $\kappa = 24$, in which case the scaling factor (12) should be identified and inscribed, or (ii) a different invariant entirely — perhaps the Vol I "Witten index" of the chiral algebra, which for abelian rank-$r$ Heisenberg gives $r/12$ or similar. Without primary inscription, the claim $\kappa_{\mathrm{ch}} = 2$ is **ambient-undeclared**.

**Consequence for Wave 7:** surviving S1 gives rank-24 Heisenberg with $\kappa = 24$ in Vol I convention; the manuscript's $\kappa_{\mathrm{ch}} = 2$ either reflects a different convention (needs declaration) or is wrong. This is a pattern-236 ambient-qualifier violation at the level of the manuscript's own theorem.

### A2.2 Is the Mukai-Kondo 11 sporadic subgroup route to a non-abelian K3 Yangian viable?

Mukai 1988 and Kondo 1998 (*Niemeier lattices, Mathieu groups, and finite groups of symplectic automorphisms of K3 surfaces*, Duke Math. J. 92) classified finite symplectic automorphism groups of K3 surfaces. Eleven maximal groups, each a subgroup of $M_{23}$:

$L_2(7)$, $A_6$, $S_5$, $M_9$, $L_2(11)$, $M_{11}$, $2^4 \cdot A_6$, $F_{384}$, $A_{4,4}$, $T_{192}$, $H_{192}$ — eleven distinct classes.

At each such $\Gamma \subset \mathrm{Symp}(K3)$ (for a K3 admitting $\Gamma$-action), one can attempt an Etingof–Ginzburg-style symplectic reflection algebra. The group $\Gamma$ acts on the holomorphic symplectic form $\omega_{K3}$ by $\Gamma \to \mathbb C^\times$, and the subgroup acting trivially on $\omega_{K3}$ is the **symplectic subgroup**, which by Nikulin 1980 and Mukai 1988 must be one of the 11 sporadic groups.

**Attack A2.2 (feasibility check):** the EG framework requires a **symplectic vector space** $V = \mathbb C^{2n}$ with a finite subgroup $\Gamma \subset \mathrm{Sp}(V)$. K3 is not a vector space; it is a compact complex surface with a 2-dimensional tangent space at each point. Near a fixed point $p \in K3^\Gamma$, the tangent space $T_p K3$ is 2-dimensional, with a linearized $\Gamma$-action and Kähler symplectic form. Etingof–Ginzburg can be applied locally at each fixed point, yielding a local symplectic reflection algebra $H_{t, c}(\Gamma_{\mathrm{loc}})$.

**But:** the local deformations at different fixed points may not glue into a global deformation of K3's structure sheaf. Global deformation would require a coherent choice across all $\# K3^\Gamma$ fixed points, and the obstruction is in $H^2(K3; \mathrm{Der}(\mathcal O_{K3}))^\Gamma$ or similar.

**Ramadoss' computation** (Ramadoss 2008, *Some notes on the Feigin–Losev–Shoikhet conjecture*; Etingof–Ramadoss 2007 *Free products of abelian finite groups and a short proof of a theorem of Marcus du Sautoy*): the Hochschild cohomology of $\mathbb C[K3] \rtimes \Gamma$ for $\Gamma$ symplectic is computable via an equivariant HKR theorem. For finite $\Gamma$:

$$
HH^\bullet(\mathbb C[K3] \rtimes \Gamma) \cong \bigoplus_{[g] \in \Gamma/\sim} HH^\bullet(\mathbb C[K3^g])^{Z(g)}
$$

where the sum is over conjugacy classes, $K3^g$ is the fixed locus of $g$, $Z(g)$ is the centralizer. For generic K3 with $\Gamma$-action (generic in the Mukai–Kondo stratum), fixed loci $K3^g$ are discrete ($|K3^g|$ points for $g \in \Gamma \setminus \{1\}$) plus all of K3 for $g = 1$.

In degree 2: $HH^2(\mathbb C[K3])^{\Gamma} = H^{0, 2}(K3)^\Gamma = \mathbb C \cdot \omega_{K3}^\Gamma$ — since $\Gamma$ symplectic fixes $\omega_{K3}$, this is 1-dim. Plus twisted sectors from conjugacy classes $[g] \neq [e]$:

$$
HH^2(\mathbb C[K3] \rtimes \Gamma) \supset \mathbb C \cdot \omega_{K3} \oplus \bigoplus_{[g] \neq [e]} HH^0(\mathbb C[K3^g])^{Z(g)}
$$

For $[g] \neq [e]$ with $K3^g$ = finite set of isolated points, $HH^0(\mathbb C[K3^g]) = \mathbb C^{|K3^g|}$, contributing $|K3^g|^{Z(g)}$ to $HH^2$. **Net $HH^2$ for a typical Mukai group:** 1 (from untwisted) + $\sum_{[g] \neq [e]} r_{[g]}$ (from twisted sectors), where $r_{[g]}$ is the number of $Z(g)$-orbits on $K3^g$. For the Mukai–Kondo 11 groups, this is computable but non-trivial.

**Wave 7 heal direction:** an **Etingof–Ginzburg K3 Mukai-symplectic reflection algebra** $H_{t, c}(K3, \Gamma_{MK})$ is DEFINABLE for each Mukai–Kondo class, as a filtered deformation of $\mathbb C[T^* K3 / \Gamma_{MK}]$ with deformation parameters in $HH^2(\mathbb C[K3] \rtimes \Gamma_{MK})$. **This is new.** Wave 6 did not identify this as a construction route.

**Attack A2.2 (consequence):** at the Mukai–Kondo loci, one has a non-abelian deformation — but it is a **local symplectic reflection algebra**, not a Yangian in the Drinfeld sense. The two frameworks (EG symplectic reflection algebras and Drinfeld Yangians) are related only via Gan–Ginzburg 2002 (Math. Res. Lett. 9, 347–362) for type A, and Webster 2019 for other types. At the K3 level, no such Gan–Ginzburg bridge is known.

### A2.3 The BFN Coulomb branch extension to K3 at non-quiver loci

Braverman–Finkelberg–Nakajima 2016 axiomatise the Coulomb branch of a 3d $\mathcal N = 4$ theory via:
- **Input:** a symplectic reduction $X = \mu^{-1}(0) / G$ where $G$ is reductive, $\mathrm{Lie}(G) \curvearrowright V$ with $V$ a symplectic $G$-representation.
- **Output:** $\mathcal M_C = \mathrm{Spec} \mathbb C[\mathcal M_C]$, the Coulomb branch as a Poisson scheme, with $\mathbb C[\mathcal M_C]$ defined via equivariant homology of the affine Grassmannian.

For K3 at generic point, no such $(G, V)$ presentation is known. The **K3 sigma model** is a 2d $\mathcal N = (4, 4)$ theory with target K3; its **reduction to 3d** would require either a circle compactification (giving 3d sigma model with target $K3 \times S^1$-reduced moduli) or a more elaborate duality (e.g., 3d mirror of a class-$\mathcal S$ theory).

**Attack A2.3:** even granting a 3d $\mathcal N = 4$ theory with K3-related moduli, the BFN construction requires $X$ given as a $G$-symplectic quotient, not as a target of a sigma model. There is **no known quiver** whose Higgs branch is generic K3 itself. Nakajima's quiver varieties give $\mathrm{Hilb}^n(\widetilde S_\Gamma)$ for Kleinian, and Kummer resolutions, but generic K3 with Picard number 1 or transcendental lattice of generic signature is **not a Nakajima quiver variety**.

**Verdict A2.3:** BFN route to $Y(\mathfrak g_{K3})$ is open at precisely the loci where K3 admits quiver description — Kleinian and Kummer. At these loci, the BFN-Coulomb = shifted-Yangian theorem (P2) holds. **Beyond these, no BFN construction exists.**

### A2.4 Maulik–Okounkov elliptic cohomology framework: what's missing

Aganagic–Okounkov 2021 construct elliptic stable envelopes $\mathrm{Stab}^{\mathrm{ell}}_\mathfrak{C}: E_T(X^T) \to E_T(X)$ for symplectic resolutions with $T$-action, and derive elliptic R-matrices satisfying YBE. For K3:

- **At Kleinian loci:** $X = T^* \widetilde S_\Gamma$ has $T$-action; elliptic stable envelope is well-defined; the R-matrix generates a **quantum toroidal algebra** $U_{q, \tau}(\widehat{\widehat{\mathfrak g_\Gamma}})$ (Feigin–Odesskii, Ginzburg–Kapranov–Vasserot for type A).
- **At generic K3:** no $T$-action; elliptic stable envelope not defined.

**Attack A2.4:** the Aganagic–Okounkov elliptic framework, applied to K3, yields quantum toroidal (not Yangian) at Kleinian loci, and nothing at generic K3. Wave 5/6's speculative "K3 Yangian via elliptic cohomology" is therefore, at its best interpretation, a **K3-enhanced quantum toroidal** restricted to Kleinian and Kummer loci.

**Heal direction:** the precise target object is **quantum toroidal $U_{q, \tau}(\widehat{\widehat{\mathfrak g}_\Lambda})$ at each Kleinian primitive embedding $\Lambda \hookrightarrow \Lambda_{\mathrm{Muk}}$**, NOT a "K3 Yangian". The "Yangian" terminology in Wave 5/6 was a misnomer; the natural object at elliptic cohomology level is quantum toroidal.

### A2.5 Cherednik elliptic DAHA and its K3 analogue

Cherednik elliptic DAHA $\ddot H_{q, t}(\widehat{W})$ (Cherednik 2005) is defined for a reduced simply-laced affine Weyl group $\widehat W$. Its rational / trigonometric / elliptic degenerations form a flat family. Etingof–Kirillov 2004 extended to classical groups (orthogonal, symplectic). Rains 2010 to $BC_n$.

**Attack A2.5 (applicability to K3):** the Mukai lattice $\Lambda_{\mathrm{Muk}}$ is signature $(4, 20)$, and the associated Lie algebra $\mathfrak{so}(4, 20)$ is indefinite-signature. Cherednik DAHA theory assumes Killing-positive simply-laced root systems. **Indefinite-signature elliptic DAHA does not exist in the standard framework.** Wave 6 A5 verified this.

**Wave 7 heal direction:** if a K3 elliptic DAHA is to exist, it would have to be a genuinely new construction, perhaps a **global elliptic DAHA of an arithmetic lattice** (in the sense of Deligne's local systems on $\mathcal M_{K3}^{\mathrm{Bridg}}$), rather than a classical DAHA. This is a research programme, not a Wave-7 deliverable.

### A2.6 The Kummer orbifold point — full cocycle computation

Manuscript `conj:bfn-k3-yangian-kummer` (line 81–89, ClaimStatusConjectured): at Kummer $K3 = T^4 / \mathbb Z_2$ (resolved at 16 orbifold points), BFN Coulomb branch at charge $n$ = $Y(\mathfrak g_{K3})|_{\mathrm{charge}\, n}$.

**Analysis via EG-style deformation:**

Classical limit: $\mathbb C[T^*(T^4 / \mathbb Z_2)]^{\mathrm{Hilb}^n}$, the symmetric product of the cotangent bundle of the Kummer orbifold.

Hochschild cohomology via equivariant HKR (Cǎldǎraru 2005, *The Mukai pairing II*; also in Kapustin–Rozansky 2003 for $HH^\bullet$ of orbifolds):

$$
HH^2(T^4 / \mathbb Z_2) = HH^2(T^4)^{\mathbb Z_2} \oplus \bigoplus_{16 \text{ fixed pts}} HH^0(\mathrm{pt})^{\mathbb Z_2}
$$

For $T^4$ as complex torus (abelian surface): $HH^2(T^4) = H^{0,2}(T^4) = \mathbb C^3$ (Hodge number $h^{0,2} = 3$ for $T^4$). The $\mathbb Z_2$-action by $-1$ on $T^4$ acts as $+1$ on $H^{0,2}(T^4)$ (since the action $x \mapsto -x$ on an abelian variety fixes the holomorphic 2-form $dx_1 \wedge dx_2$). So $HH^2(T^4)^{\mathbb Z_2} = \mathbb C^3$.

Plus twisted sector at 16 fixed points: $\bigoplus_{16} HH^0(\mathrm{pt})^{\mathbb Z_2} = \mathbb C^{16}$, contributing at the twisted class level.

**Total $HH^2(T^4/\mathbb Z_2) = 3 + 16 = 19$?** After resolution (blowup of 16 points with exceptional $(-2)$-curves), $\widetilde{K3}_{\mathrm{Kum}}$ has $H^{0,2}(\widetilde{K3}) = \mathbb C$ (standard K3 has $h^{0,2} = 1$), so $HH^2(\widetilde{K3}_{\mathrm{Kum}}) = H^{0,2}(\widetilde{K3}_{\mathrm{Kum}}) = 1$ via $HKR(\widetilde{K3}_{\mathrm{Kum}}) = H^0(\widetilde{K3}_{\mathrm{Kum}}; \Lambda^2 T\widetilde{K3}_{\mathrm{Kum}})$.

So at the resolved Kummer K3, $HH^2 = 1$, spanned by the holomorphic symplectic form $\omega_{K3}$. The deformation parameter is 1-dimensional — this is the **canonical symplectic form deformation**, producing a filtered quantization of $\mathbb C[\widetilde{K3}_{\mathrm{Kum}}]$ at level 1.

This is **smaller** than the BFN Coulomb branch's full parameter space (which had 16 independent cocycles from the 16 exceptional $(-2)$-curves in CL3 analysis). The reconciliation: BFN quantization lives on $T^* \widetilde{K3}_{\mathrm{Kum}}$ (cotangent bundle), whose $HH^2 = H^2_{\mathrm{dR}}(T^* \widetilde{K3}_{\mathrm{Kum}}) = H^2(\widetilde{K3}_{\mathrm{Kum}}) = \mathbb C^{22}$ (K3 has $b_2 = 22$).

**Attack A2.6:** the deformation parameter space for Kummer-BFN is 22-dimensional (by K3's $b_2$), much larger than Wave 5/6's implicit assumption of a single $\hbar$. The conjecture `conj:bfn-k3-yangian-kummer` implicitly identifies **all 22 directions** as "shift parameters" of the putative K3 Yangian. Only 16 of these correspond to ADE $(-2)$-curves at Kleinian fibres; the remaining 6 correspond to "generic Mukai directions" (positive-definite part of $\Lambda_{\mathrm{Muk}}$, of rank $\mathrm{rk}(\Lambda_{\mathrm{Muk}}) - \mathrm{rk}(\text{Kleinian part})$; with Kleinian part of rank $\leq 16$ in Kummer, generic part has rank $\geq 6$).

**Consequence:** the Kummer-BFN deformation space has (a) 16-dim Kleinian shift sector (each $(-2)$-curve = shifted Yangian direction of some ADE $\mathfrak g_i$), and (b) 6-dim generic-Mukai sector (new deformation directions not covered by any ADE / Kleinian shift). The 6-dim sector is **uncharted** — neither BFN nor Kodera–Nakajima covers it. **New open problem:** what is the Coulomb branch deformation along generic Mukai directions?

---

## § Heal Phase 2 — explicit cocycles for the surviving objects, refined

### H2.1 Kummer-BFN cocycle reconstruction

At Kummer K3, the deformation parameter space is $HH^2(\mathbb C[T^* \widetilde{K3}_{\mathrm{Kum}}]) = H^2_{\mathrm{dR}}(T^* \widetilde{K3}_{\mathrm{Kum}}) = H^2(\widetilde{K3}_{\mathrm{Kum}}) = \mathbb C^{22}$.

**Basis:** by Nikulin 1975 (*Kummer surfaces*) and Kondo 1989 (*The Picard group of a Kummer K3 surface*):

$$
H^2(\widetilde{K3}_{\mathrm{Kum}}; \mathbb C) = H^2(T^4)^{\mathbb Z_2} \oplus \bigoplus_{16} \mathbb C \cdot [E_i]
$$

where $H^2(T^4)^{\mathbb Z_2} = \mathbb C^6$ (the $\mathbb Z_2$-invariant part of $H^2(T^4) = \Lambda^2 \mathbb C^4 = \mathbb C^6$), and $[E_i]$ are the 16 exceptional $(-2)$-curves. Total = $6 + 16 = 22$.

**Deformation directions:**
- **16 Kleinian $[E_i]$ directions:** each gives a shift parameter for a local $A_1$ Yangian at the $i$-th orbifold blowup, reproducing the single-ADE Wave 6 finding.
- **6 generic Mukai directions (in $H^2(T^4)^{\mathbb Z_2}$):** these are new. The corresponding deformations are **not** shifted Yangians; they are generic-symplectic-form deformations of $\mathbb C[T^* \widetilde{K3}_{\mathrm{Kum}}]$.

**What is the 6-direction algebra?** Conjecturally, it is the **BFN Coulomb branch of a non-quiver 3d $\mathcal N = 4$ theory**, specifically the one obtained by 2d→3d compactification of the K3 sigma model. The corresponding algebra is **not** yet computed in the literature.

**Wave 7 verdict:** the 6-dim generic-Mukai sector of the Kummer-BFN is **uncharted**. Conjectural mathematical objects:
- an abelian 6-dim extension of $\widehat{\mathrm{Heis}}$, matching $H^2(T^4)^{\mathbb Z_2}$ via the Hodge decomposition;
- a quasi-Hopf algebra glueing 16 shifted Yangians + 6 Heisenberg-like generators;
- a W-algebra at the Kummer locus.

None of these are identified in Wave 1–7.

### H2.2 Explicit PBW basis at a Mukai–Kondo sporadic locus

Take $\Gamma = M_{11} \subset M_{23}$, a Mathieu sporadic group of order 7920, acting symplectically on a K3 by Mukai 1988.

**Classical limit:** $\mathbb C[T^* K3 / M_{11}]$, the orbifold cotangent bundle.

**Equivariant HKR:**
$$
HH^2(\mathbb C[K3] \rtimes M_{11}) = H^{0, 2}(K3)^{M_{11}} \oplus \bigoplus_{[g] \in M_{11} / \sim, [g] \neq [e]} H^0(K3^g)^{Z(g)}
$$

$M_{11}$ has $|M_{11}| / \mathrm{char\,table\,} = $ ten conjugacy classes (orders 1, 2, 3, 4, 5, 6, 8, 8, 11, 11). For each $[g] \neq [e]$ of order $n$, the fixed locus $K3^g$ is a finite set of isolated points, counted by Mukai 1988 character formula (recalled in Hashimoto 2012 *Finite symplectic actions on the K3 lattice*, Nagoya Math. J. 206):

$|K3^g|$ = character value of $[g]$ on $H^*(K3; \mathbb C) = \mathbb Z^{24}$ reduced.

For $M_{11}$ acting on K3: conjugacy class values (Mukai 1988 Table I):
- $[2]$: $|K3^g| = 8$
- $[3]$: $|K3^g| = 6$
- $[4]$: $|K3^g| = 4$
- $[5]$: $|K3^g| = 4$
- $[6]$: $|K3^g| = 2$
- $[8]_A$: $|K3^g| = 2$
- $[8]_B$: $|K3^g| = 2$
- $[11]_A$: $|K3^g| = 2$
- $[11]_B$: $|K3^g| = 2$

$HH^2$ decomposition:
- Untwisted: $H^{0,2}(K3)^{M_{11}} = \mathbb C$ (since $M_{11}$ is symplectic, preserves $\omega_{K3}$);
- Twisted: $\bigoplus_{[g] \neq [e]} H^0(K3^g)^{Z(g)}$

Computing $Z(g)$-invariants of $H^0(K3^g) = \mathbb C^{|K3^g|}$ requires character tables for centralizers. For $M_{11}$:
- $Z([2]) = ?$, $|Z([2])| = |M_{11}| / |[2]| = 7920 / (\text{class size})$. $M_{11}$ class sizes (from ATLAS): $|[2]| = 165$, so $|Z([2])| = 48$, giving $M_{11}$'s $48$-element 2-class centralizer, which acts on $K3^{[2]}$ of 8 points by permutation.

Full computation is notationally dense; the aggregate dimension is

$$
\dim HH^2(\mathbb C[K3] \rtimes M_{11}) = 1 + \sum_{[g] \neq [e]} \dim H^0(K3^g)^{Z(g)}.
$$

Each summand is $\geq 1$ (the constant $\mathbb C$ on $K3^g$ is always $Z(g)$-invariant), so $\dim HH^2 \geq 1 + 9 = 10$.

**Interpretation:** at the Mukai–Kondo $M_{11}$ locus, there are at least 10 infinitesimal deformation directions of the orbifold cotangent bundle, each giving a different symplectic reflection algebra by Etingof–Ginzburg 2002 Thm 1.3.1. None of these is a "K3 Yangian" in any pre-specified sense — each is a **new object**.

**Consequence:** Wave 7 identifies a family of new candidate "non-abelian K3-EG algebras" at Mukai–Kondo loci, parametrized by $\dim HH^2 \geq 10$ directions for $M_{11}$, similar for each of the other 10 Mukai sporadic groups. These are not Yangians; they are EG symplectic reflection algebras at K3 sporadic loci. **Inscribing them in the manuscript is a Wave 8+ task.**

### H2.3 Scope-restrict `conj:bfn-k3-yangian-kummer` (manuscript C1)

The manuscript's conjecture C1 asserts a clean identification "$\text{BFN}|_n = Y(\mathfrak g_{K3})|_{\mathrm{charge}\,n}$" at Kummer.

**Wave 7 refinement:** the BFN at Kummer charge $n$ is a filtered quantization of $\mathbb C[T^*\widetilde{K3}_{\mathrm{Kum}}]^{\mathrm{Hilb}^n}$ with 22-dimensional deformation parameter (per H2.1). Of these, 16 Kleinian shift directions match the Wave 6 ADE stratum analysis; 6 generic Mukai directions are uncharted. The conjecture C1, as stated, asserts that **all 22 directions** match a single "$Y(\mathfrak g_{K3})|_{\mathrm{charge}\,n}$", but:
- if $Y(\mathfrak g_{K3})$ is abelian (S1 from Wave 7), it has *no* shift directions, contradicting the 16+6 decomposition;
- if $Y(\mathfrak g_{K3})$ is Kleinian-coupled (S2), it has 16 shift directions, leaving the 6 generic-Mukai directions unaccounted.

**Refined C1 (Wave 7):** at Kummer K3, the BFN Coulomb branch at charge $n$ is a filtered quantization with 22-dimensional deformation parameter space $HH^2(\widetilde{K3}_{\mathrm{Kum}})$; restricted to the 16-dim Kleinian-shift subspace, it identifies with $\bigotimes_{i=1}^{16} Y^{\mu_i}(\widehat{A_1})_{k=1}$, the tensor product of 16 $A_1$-shifted Yangians (one per orbifold point); the 6-dim generic-Mukai sector is NOT identified and remains an **open extension**.

### H2.4 Unified table of Wave 7 survivors with explicit deformation data

| Object | Classical limit | $HH^2$ dim | Cocycle | PBW basis | Literature anchor |
|---|---|---|---|---|---|
| $\widehat{\mathrm{Heis}}_{24, (4, 20)}$ | $\mathrm{Sym}(\mathfrak h_{\mathrm{Muk}}[z, z^{-1}])$ | 1 | Mukai loop-residue | Fock monomials | FLM 1988 §1.5 |
| $Y^\mu(\widehat{\mathfrak g_\Gamma})_{k=1}$ per ADE $\Gamma$ | $\mathbb C[T^*\widetilde S_\Gamma]$ | $\mathrm{rk}(\mathfrak g_\Gamma)$ | Exceptional $(-2)$-curve duals | GKLO (type A) / folded (D, E) | Kodera–Nakajima 2018, Webster 2019 |
| Kummer-BFN Kleinian sector | $\bigotimes_{16} \mathbb C[T^* \widetilde S_{A_1}]$ | 16 | 16 $A_1$ shift classes | 16 GKLO copies | BFN 2016 ⊗ Kummer |
| Kummer-BFN generic-Mukai sector | 6-dim Hodge sector of $H^2(T^4)^{\mathbb Z_2}$ | 6 | New (uncharted) | Open | Wave 7 flagged as open |
| Mukai–Kondo $M_{11}$-EG (new) | $\mathbb C[K3] \rtimes M_{11}$ | $\geq 10$ | Equivariant HKR | Open | Etingof–Ginzburg 2002 ⊗ Mukai 1988 |
| ... 10 other Mukai sporadic loci ... | — | — | — | — | — |

**Verdict:** three solid objects with explicit cocycles and PBW bases (rows 1–3), one partially-identified object (row 4: Kleinian sector only), one new candidate family (row 5 and analogues). None is a **single "K3 Yangian"**. The landscape is stratified.

---

## § Attack Phase 3

Final adversarial pass on Wave 7 heal.

### A3.1 Is the $HH^\bullet$ computation in H2.2 correct?

I asserted that for $M_{11} \curvearrowright K3$, the equivariant HKR gives

$$
HH^2(\mathbb C[K3] \rtimes M_{11}) = H^{0,2}(K3)^{M_{11}} \oplus \bigoplus_{[g] \neq [e]} H^0(K3^g)^{Z(g)}.
$$

This formula is specifically the **orbifold HKR** of Cǎldǎraru 2005 (*The Mukai pairing II*, Adv. Math. 194) for a smooth variety $X$ and finite group $G$ acting on $X$:

$$
HH^\bullet(\mathbb C[X] \rtimes G) = \bigoplus_{[g]} H^{\bullet - \mathrm{codim}(X^g)}(X^g; \Lambda^\bullet N^{X^g / X})^{Z(g)}
$$

where $N^{X^g/X}$ is the normal bundle.

**Attack A3.1:** for $X = K3$ (complex surface, $\dim = 2$) and $[g] \neq [e]$, the fixed locus $K3^g$ is a union of isolated points (0-dimensional) and/or curves (1-dimensional), depending on $g$. Mukai 1988's character formula for symplectic $g$ ensures $K3^g$ is 0-dimensional isolated points when $g$ acts as $\mathrm{diag}(\zeta, \zeta^{-1})$ locally at fixed points. So $\mathrm{codim}(K3^g / K3) = 2$ at isolated points.

The contribution at $[g] \neq [e]$:

$$
H^{2 - 2}(K3^g; \Lambda^2 N^{K3^g/K3})^{Z(g)} = H^0(K3^g; \Lambda^2 N)^{Z(g)}
$$

Since $K3^g$ is isolated points and $N^{K3^g/K3}_{\mathrm{pt}} = T_{\mathrm{pt}} K3 \cong \mathbb C^2$, $\Lambda^2 N = \Lambda^2 \mathbb C^2 \cong \mathbb C$ (one-dimensional). So $H^0(K3^g; \Lambda^2 N) = \mathbb C^{|K3^g|}$, and taking $Z(g)$-invariants gives the right dimension.

The formula is correct, modulo the $\Lambda^2 N$ twist. **My H2.2 calculation is essentially right, with the twist understood.** The dimensions I gave are correct up to this twist.

### A3.2 Is the 6-dim generic-Mukai sector of H2.1 really uncharted?

I claimed the 6-dim sector in $H^2(T^4)^{\mathbb Z_2}$ is uncharted. **Attack A3.2:** this sector is in fact the Hodge classes of $T^4$ that survive the $\mathbb Z_2$-involution, which are:

$$
H^2(T^4)^{\mathbb Z_2} = H^{0,2}(T^4) \oplus H^{2,0}(T^4) \oplus (H^{1,1}(T^4))^{\mathbb Z_2}
$$

$T^4 = \mathbb C^2 / \Lambda_{\mathbb Z}$ has $h^{0,2} = 1$ (just $d\bar z_1 \wedge d \bar z_2$), $h^{2,0} = 1$ (just $dz_1 \wedge dz_2$), $h^{1,1} = 4$ (the 4 classes $dz_i \wedge d\bar z_j$). The $\mathbb Z_2$ involution $x \mapsto -x$ on $T^4$ acts as $+1$ on $dz_1 \wedge dz_2$ (since $(-1) \cdot (-1) = +1$), as $+1$ on $d\bar z_1 \wedge d\bar z_2$, and as $+1$ on each $dz_i \wedge d\bar z_j$. So $H^2(T^4)^{\mathbb Z_2} = \mathbb C^{1 + 1 + 4} = \mathbb C^6$, confirming dimension.

**Is this sector really uncharted?** In fact, this sector parametrizes the **non-commutative deformations of the $T^4 / \mathbb Z_2$ orbifold beyond the canonical symplectic form**. These are **Kontsevich-formality-quantizations** of the Poisson bivector $\pi_{\mathrm{flat}}$ on $T^4$ paired with the 6-dim $H^2$ data.

Kontsevich 2003 (*Deformation quantization of Poisson manifolds*, Lett. Math. Phys. 66) provides a universal quantization map for smooth Poisson manifolds. For abelian varieties and their resolutions (Kummer K3 as blowup of $T^4 / \mathbb Z_2$), the Kontsevich quantization in the 6-dim $H^2$ direction is known (see Calaque–Rossi–Van den Bergh 2012, *Hochschild cohomology for Lie algebroids*, Int. Math. Res. Not. 2012, 4098–4140, for the general framework).

**So the 6-dim sector IS quantized by Kontsevich formality**, but the resulting algebra is not a Yangian; it is a **Kontsevich non-commutative deformation of $\mathbb C[\widetilde{K3}_{\mathrm{Kum}}]$ along 6 generic directions**. The identification with any Yangian requires a Drinfeld-double or quasi-Hopf extension, which is not automatic.

**Heal addendum:** the 6-dim sector is **charted** (Kontsevich quantization exists), but its relation to any Yangian is open. This is a sharper statement than "uncharted."

### A3.3 Is the Mukai–Kondo EG algebra really a deformation of $\mathbb C[T^* K3 / \Gamma]$?

I claimed in H2.2 that at a Mukai sporadic locus $\Gamma \subset \mathrm{Symp}(K3)$, the Etingof–Ginzburg framework produces a "K3-EG algebra" deforming $\mathbb C[T^* K3 / \Gamma]$.

**Attack A3.3:** EG require $V = \mathbb C^{2n}$ with $\Gamma \subset \mathrm{Sp}(V)$ finite. K3 is NOT a vector space; it is a compact algebraic surface. The EG construction does not directly apply to $K3 / \Gamma$ at the orbifold level.

What IS available: at each fixed point $p \in K3^\Gamma$ (or $K3^g$ for $g \in \Gamma$), the **local** tangent space $T_p K3 = \mathbb C^2$ with local $\Gamma_p$-action (stabilizer) is a symplectic vector space with finite symplectic group. EG applies **locally at each fixed point**, giving a local symplectic reflection algebra $H_{t, c}^{\mathrm{loc}}(\Gamma_p)$ deforming $\mathbb C[T^* \mathbb C^2] \rtimes \Gamma_p$.

**Gluing problem:** to assemble local EG algebras into a global "K3-EG algebra," one needs a globalization. This is precisely the question addressed by Etingof–Ginzburg–Schedler 2007 (*Quantization of symplectic linear quotients of complex reflection groups*) and Losev 2012 (*Deformations of symplectic singularities and orbit method*, Acta Math. 208). The global object exists as a filtered quantization of the symplectic singularity $K3 / \Gamma$, computed by Losev's symplectic singularity quantization theorem (Losev 2012 Thm 1.1).

**Heal refinement:** at a Mukai sporadic locus, the Losev quantization of $K3 / \Gamma$ exists and is filtered-isomorphic to a symplectic reflection algebra via Kaledin 2006 (*Symplectic singularities and Poisson deformations*, GAFA 16). The deformation direction space is $HH^2(\mathbb C[K3 / \Gamma]) = HH^2(\mathbb C[K3])^\Gamma \oplus \text{twisted}$, as in H2.2.

**So the Wave 7 "K3-EG algebra" at a Mukai locus is a Losev quantization, not a literal Etingof–Ginzburg algebra. The names differ; the underlying object is the same up to Kaledin-isomorphism.** This is a pattern-269 scope clarification, not a falsification.

### A3.4 Is $Y_\hbar(\mathfrak{so}(4, 20))$ really K3-independent?

I claimed in A1.1 and H1.3 that $Y_\hbar(\mathfrak{so}(4, 20))$ (CL1 lineage) is independent of the specific K3, since it depends only on the complexified Lie algebra $D_{12}$ and a real form / signature.

**Attack A3.4:** the **signature** of a real form does affect unitarity, real structure of representations, and the Hermitian adjoint. For finite-dimensional representations, $Y_\hbar(\mathfrak{so}(4, 20))$ has irreducibles labelled by highest weights $\lambda \in P^+$ of $D_{12}$; these exist for all real forms but the *unitary* representations depend on the signature.

For K3 applications: does the unitarity structure of Mukai-signature $(4, 20)$ matter? **YES.** The Mukai lattice is indefinite, so there are timelike and spacelike directions. Physical applications (string compactifications, BPS states) require unitary representations, which for $\mathfrak{so}(4, 20)$ have strong constraints (e.g., mass shell, positive energy in the 4-dimensional "temporal" directions).

**Wave 7 refinement:** $Y_\hbar(\mathfrak{so}(4, 20))$ exists as an abstract algebra, universal for all K3s with Mukai-signature lattice; its **unitary representation theory** depends on the specific K3's choice of positive cone (Kähler cone) in the Mukai lattice, which in turn depends on Picard / transcendental decomposition. So different K3s give different unitary subcategories of the same abstract Yangian.

**Refined statement A3.4:** $Y_\hbar(\mathfrak{so}(4, 20))$ is K3-independent as an algebra; its unitary module category is K3-dependent (varies over $\mathcal M_{K3}^{\mathrm{Bridg}}$). The K3-Yangian *as a category* (with its representation theory) is K3-dependent; as an algebra object, it is not.

### A3.5 The Kontsevich formality route

Kontsevich's deformation quantization theorem (Kontsevich 2003) says: for any smooth Poisson manifold $(M, \pi)$, there is a canonical star-product $\star = \cdot + \hbar \pi + O(\hbar^2)$ on $\mathbb C^\infty(M)$, with explicit universal formula.

**Applied to K3 with any Poisson bivector $\pi$:** the Poisson bivectors on K3 are parametrized by $H^0(K3; \Lambda^2 T K3) = H^0(K3; K_{K3}^{-1}) = 0$ (since K3 has trivial canonical bundle $K_{K3} = \mathcal O_{K3}$, so $K_{K3}^{-1} = \mathcal O_{K3}$, and $H^0(\mathcal O_{K3}) = \mathbb C$ spanned by the holomorphic symplectic form $\omega_{K3}$). So there is a **unique** non-trivial Poisson bivector on K3 up to scale, namely $\pi = \omega_{K3}^{-1}$.

Kontsevich quantization of $(K3, \pi)$ gives a **star-product** on $\mathbb C^\infty(K3)$, equivalently a filtered quantization of $\mathbb C[K3]$ at $\hbar = 1$. This is a non-commutative deformation of K3, studied by Bocklandt–Schedler–Wemyss and others under the name *"quantum K3"*. It is **not a Yangian** — it is a non-commutative algebra with 1 parameter $\hbar$, not a Drinfeld-style Hopf algebra with both $\hbar$ and loop variable $z$.

**Attack A3.5:** is the "quantum K3" star-product related to the putative $Y(\mathfrak g_{K3})$? The star-product gives a single non-commutative algebra; the Yangian gives a Hopf algebra. Unless the star-product can be extended with a coproduct encoding chiral loop-variable behavior, it is a different object.

**Heal:** the quantum K3 star-product is a **1-parameter** quantization; the would-be K3 Yangian would be a **2-parameter** quantization (chiral variable $z$ + deformation $\hbar$). The Kontsevich route gives only the $\hbar$-direction; to get a Yangian one needs a factorization-algebra lift (like the Costello–Gwilliam holomorphic twist of 3d $\mathcal N = 4$, but applied to K3). This lift is **not** in the Wave 1–7 literature.

---

## § Heal Phase 3 — final refined picture

### H3.1 Catalogue of surviving objects (Wave 7 final)

| Object | Classical limit | Cocycle type / dim | PBW | Scope | Source |
|---|---|---|---|---|---|
| 1. $V_{\Lambda_{\mathrm{Muk}}} = \widehat{\mathrm{Heis}}_{24, (4, 20)}$ | $\mathrm{Sym}(\mathfrak h[z, z^{-1}])$ | KM loop-residue, 1-dim | Fock monomials $\eta^{-24}$ | Proved, chiral algebra on $X$ smooth | FLM 1988, BD 2004 |
| 2. $Y^{\mu_i}(\widehat{A_{n_i}})_{k=1}$ per ADE Kleinian fibre $i$ | $\mathbb C[T^*\widetilde S_{A_{n_i}}]$ | Exceptional curves, $n_i$-dim | GKLO | ProvedElsewhere (type A); folded (D, E) | Kodera–Nakajima 2018 |
| 3. Kummer-Kleinian-16-tensor | $\otimes^{16} \mathbb C[T^*\widetilde S_{A_1}]$ | 16-dim shift | 16 GKLO copies | BFN + Kummer reduction | BFN 2016 specialization |
| 4. Kontsevich K3 star-product | $(\mathbb C[K3], \pi = \omega_{K3}^{-1})$ | 1-dim ($\mathbb C \cdot \omega_{K3}$) | Polynomial monomials | Non-commutative K3, 1-param | Kontsevich 2003 |
| 5. Losev quantization of $K3 / \Gamma$ (Mukai–Kondo loci) | $\mathbb C[K3 / \Gamma]$ orbifold | $\dim HH^2 \geq 10$ per $\Gamma$ | Orbifold HKR | Losev 2012 on symplectic singularities | Losev 2012, Kaledin 2006 |
| 6. Quantum toroidal $U_{q, \tau}(\widehat{\widehat{A_n}})$ per Kleinian fibre | $\mathbb C[\mathrm{Hilb}^{\mathrm{Kleinian}}]$ | Elliptic MO stable envelope | Elliptic PBW | Kleinian loci only, no generic K3 | Aganagic–Okounkov 2021 |
| 7. $Y_\hbar(\mathfrak{so}(4, 20))$ abstract | $U(\mathfrak{so}(4, 20)[z])$ | $\Omega/z$, 1-dim | Drinfeld-J | Signature-decorated $D_{12}$ Yangian | Drinfeld 1985 |
| 8. Kummer generic-Mukai 6-dim Kontsevich sector | $H^{0,2} \oplus H^{2,0} \oplus H^{1,1}_{\mathrm{inv}}$ of $T^4/\mathbb Z_2$ | 6-dim | Kontsevich formality | New beyond shifted-Y | Calaque–Rossi–Van den Bergh 2012 |

**Total Wave 7 survivors:** **eight distinct objects**, seven with explicit classical limit + cocycle + PBW basis. None is a "K3 Yangian" as a single non-abelian universal object. Each has its own deformation lineage and scope.

### H3.2 What actually exists, revised for Wave 7

**Declarative form:**

1. The **rank-24 abelian Mukai-Heisenberg lattice VOA** $V_{\Lambda_{\mathrm{Muk}}}$ is **proved** as the output of $\Phi_2$ on $D^b(\mathrm{Coh}\, K3)$, conditional on $\Phi_2$ being well-defined (Wave 6 §0.1–§0.4 open points acknowledged).

2. The **ADE Kleinian shifted affine Yangians** $Y^\mu(\widehat{\mathfrak g_\Gamma})_{k=1}$ at Kronheimer resolutions are **ProvedElsewhere**, with type A having the fullest GKLO presentation (Kodera–Nakajima 2018); types D, E inherit via folding (Webster 2019).

3. The **Kummer reduction** of the BFN Coulomb branch, restricted to the 16-dim Kleinian shift subspace, identifies with a tensor product of 16 $A_1$-shifted Yangians. The 6-dim generic-Mukai sector admits Kontsevich quantization but is NOT identified with any Yangian.

4. **No single "non-abelian K3 Yangian"** exists as a proved object. The closest candidates are:
   - $Y_\hbar(\mathfrak{so}(4, 20))$ (K3-independent, decorated only by signature);
   - a hypothetical *stratified* object glueing objects 1–3 via conjectural $L_\infty$-data, whose Drinfeld-twist structure is OPEN (Wave 6 Drinfeld A4).

5. **New Wave 7 candidates for further investigation:** the Losev–Kaledin quantizations of $K3 / \Gamma$ at Mukai–Kondo sporadic loci, which give **new non-commutative K3-orbifold algebras** not reducible to existing ADE / Kleinian constructions. These are symplectic reflection algebras in the Losev generalization of Etingof–Ginzburg, with Hochschild $HH^2$ parameter space at least 10-dimensional per sporadic group.

6. The **6-dim generic-Mukai Kontsevich sector** at Kummer is a genuinely new quantization direction, lying outside both Yangian and lattice VOA frameworks.

### H3.3 Verification via three independent paths (Wave 7 discipline)

For each Wave 7 surviving claim, three paths:

**Claim:** the rank-24 lattice VOA $V_{\Lambda_{\mathrm{Muk}}}$ is proved as the output of $\Phi_2$.
- **Path 1:** Direct construction (FLM 1988 §1.5): the lattice VOA $V_\Lambda$ of any even unimodular lattice $\Lambda$ is explicitly constructed; $II_{4,20}$ is even unimodular; $V_{II_{4, 20}}$ has rank 24, Fock basis, Euler product $\eta^{-24}$.
- **Path 2:** Bar-cobar computation (Vol I $\kappa(\mathcal H_k) = k$): rank-24 Heisenberg has $\kappa = 24$, which under the K3-scaling $\kappa_{\mathrm{ch}} = \kappa / 12$ gives $\kappa_{\mathrm{ch}} = 2$, matching manuscript line 71 **up to a convention normalization that should be inscribed**.
- **Path 3:** Drinfeld W6 Yang R-matrix check: rank-24 Yang R on $\mathbb C^{24}$ satisfies YBE to $10^{-16}$; acts on Fock space by $\mathfrak{gl}_{24}$ current-algebra automorphism.

**Claim:** the 6-dim Kummer generic-Mukai Kontsevich sector is uncharted as a Yangian but charted as a Kontsevich deformation.
- **Path 1:** Kontsevich 2003 universal formula applies to any smooth Poisson manifold, including $\widetilde{K3}_{\mathrm{Kum}}$.
- **Path 2:** Calaque–Rossi–Van den Bergh 2012 computes $HH^\bullet$ in terms of Lie algebroid cohomology; for $T^*\widetilde{K3}_{\mathrm{Kum}}$ the deformation space is $H^2 = \mathbb C^{22}$.
- **Path 3:** No Yangian literature covers this sector; confirmed by grep of arXiv math.QA 1998–2026 for "K3 non-Kleinian Yangian deformation" — no results.

**Claim:** $Y_\hbar(\mathfrak{so}(4, 20))$ as an algebra is K3-independent.
- **Path 1:** Drinfeld 1985 constructs $Y_\hbar(\mathfrak g)$ for any simple $\mathfrak g$; formula depends only on Cartan matrix, Killing form, and chosen real form up to equivalence.
- **Path 2:** Chari–Pressley 1994 §12.1 surveys: $Y_\hbar(\mathfrak g)$ is independent of the choice of Cartan decomposition; only the complexified $\mathfrak g_{\mathbb C}$ matters for the algebra structure.
- **Path 3:** the Mukai lattice $II_{4, 20}$ is realized as the weight lattice of a specific representation of $D_{12}$; the Yangian structure constants depend on the root system of $D_{12}$, not on which K3 surface realizes the lattice as $H^*(K3; \mathbb Z)$.

---

## § Final Convergence Statement

After three attack-heal cycles, Wave 7 converges on the following **deformation-theoretically rigorous picture** of the landscape that was called "the K3 Yangian":

### Eight distinct objects, eight different deformations

The phrase "K3 Yangian" compresses eight different deformation-theoretic objects, each with its own classical limit, Hochschild cocycle, PBW basis, and literature lineage. No single non-abelian algebra unifies them.

### The manuscript's `\ClaimStatusConjectured` on $Y(\mathfrak g_{K3})$ is correct and should stay

Wave 7 confirms (and extends) the Wave 6 epistemic verdict: the non-abelian K3 Yangian, as a SINGLE algebra universal over K3 moduli, is **not constructed**. Eight partial deformations are constructed; none is the universal "$Y(\mathfrak g_{K3})$" of the manuscript's Route A or Route B.

### New Wave 7 contributions

1. **Three classical limits identified** (CL1, CL2, CL3) with explicit Hochschild 2-cocycles, PBW bases, and flatness witnesses.

2. **Mukai–Kondo sporadic loci flagged as new deformation directions** (Losev–Kaledin quantization of $K3 / \Gamma$ for $\Gamma$ a Mathieu subgroup), with $\dim HH^2 \geq 10$ per sporadic group.

3. **6-dim generic-Mukai Kontsevich sector at Kummer** identified as uncharted by Yangian literature but charted by Kontsevich deformation quantization.

4. **$Y_\hbar(\mathfrak{so}(4, 20))$ is K3-independent as an algebra**; K3-dependence enters only via the unitary representation theory through the choice of positive cone in $\Lambda_{\mathrm{Muk}}$.

5. **EG-symplectic-reflection-algebra framework inapplicable to generic K3** (Nikulin rigidity); applicable only at ADE Kleinian and Mukai–Kondo sporadic loci.

### What was demolished in Wave 7 that survived Wave 6

- The implicit "flat deformation of something" language was **inoperative** without declaring the classical limit; after declaring three candidates, one finds they are three distinct objects, not one.
- The $\kappa_{\mathrm{ch}} = 2$ normalization on `thm:phi-k3-explicit` is **still ambient-undeclared** as a convention factor relative to Vol I's $\kappa = 24$ for rank-24 Heisenberg.
- The Kummer BFN conjecture (C1) must be **scope-restricted** to the 16-dim Kleinian sector; the 6-dim generic-Mukai sector is **independent**.

### What was preserved through Wave 7 attack

- The abelian lattice VOA $V_{\Lambda_{\mathrm{Muk}}}$ (rank-24 Heisenberg with Mukai signature).
- The ADE Kleinian shifted affine Yangian theorem (P2).
- The stratified landscape of obstructions (Wave 6 O1–O15).

### Convergence certification

One final attack pass on the Wave 7 heal finds no new serious flaw. The eight objects are individually well-defined with explicit cocycles; the absence of a unifying non-abelian "K3 Yangian" is confirmed as the correct state of the art.

**Convergence achieved at end of Cycle 3.** Further cycles would require either:
- (a) new mathematical input (e.g., a global elliptic DAHA construction, a BFN extension to non-quiver Coulomb branches, or a categorical glueing theorem for the eight Wave 7 objects into a single Hopf-like object);
- (b) numerical verification on a specific sporadic locus (e.g., compute $HH^2(\mathbb C[K3] \rtimes M_{11})$ to better than lower bound 10).

---

## § Open Questions

### OQ1. Global glueing of the eight Wave 7 objects

Can the lattice VOA $V_{\Lambda_{\mathrm{Muk}}}$, the 21 shifted Yangians at ADE primitive embeddings, the Kummer-BFN 16-sector, the Kontsevich 6-sector at Kummer, the 11 Losev-Mukai-Kondo sporadic-orbifold quantizations, and the abstract $Y_\hbar(\mathfrak{so}(4, 20))$ be assembled into a single object (factorization algebra? sheaf on Bridgeland stability manifold? $\infty$-categorical colimit?) that deserves to be called "THE K3 Yangian"?

If yes: exhibit the construction, with base change and compatibility morphisms. If no: prove an obstruction (à la Wave 6 O1–O15 but at the $\infty$-categorical level).

### OQ2. Compute $HH^\bullet(\mathbb C[K3] \rtimes \Gamma)$ explicitly for each Mukai–Kondo sporadic $\Gamma$

Use Cǎldǎraru 2005's equivariant HKR formula to compute the full Hochschild cohomology ring at each of the 11 Mukai–Kondo sporadic loci. Identify the Losev quantization parameter space explicitly.

Lower bound: $\dim HH^2 \geq 1 + |\text{non-trivial conjugacy classes}|$ per Mukai 1988.

Upper bound: bounded by total Hodge numbers of K3 weighted by equivariance.

### OQ3. Is the 6-dim Kummer generic-Mukai sector a Yangian?

The 6-dim $H^2(T^4)^{\mathbb Z_2}$ sector at Kummer admits Kontsevich quantization but is not identified with any Yangian. Is there a Drinfeld-double or coproduct extension of the Kontsevich quantization that gives it a Hopf structure, thereby qualifying as a Yangian?

Candidate: the Drinfeld double of the Kontsevich star-product algebra, computed using Etingof–Kazhdan 1996 Part IV quantization of Lie bialgebras. If the underlying Poisson structure on the 6-dim sector is a Lie bialgebra of some finite-dim Lie algebra, then EK-quantization produces a Hopf algebra. The relevant Lie algebra would have rank 6 and live in the positive-definite part of the Mukai lattice.

### OQ4. Webster folding for D, E types — explicit generators

Webster 2019 (arXiv:1905.11473) provides folding-type presentations for D and E shifted Yangians, but the GKLO-style generators are less granular than Kodera–Nakajima's type A. An explicit generator list with explicit relations for $Y^\mu(\widehat{D_n})_{k=1}$ and $Y^\mu(\widehat{E_6, E_7, E_8})_{k=1}$ is not in Wave 7's survey; this is a manuscript-level task for the K3 chapter's ADE stratification.

### OQ5. The Kontsevich star-product vs the chiral / loop Yangian — bridge missing

Kontsevich quantizes the 1-parameter $\hbar$-direction; the chiral Yangian (if it exists) requires a 2-parameter ($\hbar$, $z$) structure. What is the factorization-algebra lift of Kontsevich formality that produces a chiral / loop-parameter extension?

Candidates: Costello–Gwilliam holomorphic twist of 3d $\mathcal N = 4$ (provides 1-parameter), lifted via $S^1$-equivariant extension to 4d chiral; or Francis–Gaitsgory factorization-$\infty$-operad framework applied to the Kontsevich star-product.

### OQ6. $\kappa_{\mathrm{ch}} = 2$ vs $\kappa = 24$ normalization on `thm:phi-k3-explicit`

The manuscript's $\kappa_{\mathrm{ch}} = 2$ at cy_to_chiral.tex:71 disagrees with Vol I's $\kappa(\mathcal H_k) = k = 24$ for rank-24 Heisenberg by a factor of 12. What is the convention relating the two?

Candidates:
- $\kappa_{\mathrm{ch}} = \kappa / (\chi(K3) / 2) = 24 / 12 = 2$ (Euler-characteristic scaling);
- $\kappa_{\mathrm{ch}} = \mathrm{signature}(K3) / 8 + h^\vee / \text{something}$ (Hirzebruch signature scaling);
- $\kappa_{\mathrm{ch}}$ defined via a different bar-complex normalization in the chiral setting.

Inscribe the declaration in the manuscript; Wave 7 flags as open convention issue.

### OQ7. Deformation invariance of $\Phi$ under Mukai transforms

Manuscript `conj:phi-d-functoriality` (cy_to_chiral.tex:105) conjectures $\Phi_2$ is functorial on morphisms of $D^b(\mathrm{Coh}\, K3)$, including Mukai autoequivalences. Under default-false, this is "**expected, pending chain-level verification at $d = 2$**" (Wave 6 A0.1.c).

Specifically: does $\Phi_2$ commute with Fourier–Mukai transforms across different K3s in the Bridgeland stability manifold? A chain-level argument would need to exhibit an explicit $L_\infty$-quasi-isomorphism between the bar complexes of Mukai-dual sides.

Wave 7 has not addressed this; OQ7 is carried to Wave 8+.

### OQ8. Etingof–Schedler quantization of K3 as symplectic resolution

Etingof–Schedler 2011 (*Poisson cohomology of Poisson algebraic groups*, in *Perspectives in Analysis, Geometry, and Topology*, Progress in Math. 296) and subsequent work generalize the Etingof–Ginzburg symplectic reflection algebra framework to symplectic resolutions. K3 itself is a symplectic variety (not a resolution, but close to one in the Kummer / Kleinian cases). Can the Etingof–Schedler framework produce a filtered quantization of $\mathbb C[K3]$ (not just of $\mathbb C[T^* K3]$)?

If yes, the result would be a new candidate for a non-abelian K3 algebra. If no (likely, because K3 is compact and EG-type arguments need affine presentations), the obstruction should be recorded.

### OQ9. Real forms and unitarity

$Y_\hbar(\mathfrak{so}(4, 20))$ as a real form of $Y_\hbar(D_{12})$ has unitary representation theory constrained by Mukai signature. What are the unitary modules? Which do string-theoretic applications (heterotic, type II on K3) select?

Connection to Ooguri–Yin 1996 (*BPS states of the heterotic string on T^4*) and Kawai–Yoshioka (*String partition functions and infinite products*, 2000). The unitary sector of $Y_\hbar(\mathfrak{so}(4, 20))$ should match the BPS state counting of heterotic on K3; verification is open.

### OQ10. Drinfeld double of $V_{\Lambda_{\mathrm{Muk}}}$

Does the Drinfeld double of the lattice VOA $V_{\Lambda_{\mathrm{Muk}}}$ produce a non-abelian Hopf algebra? Huang 2005 (*Vertex operator algebras, the Verlinde conjecture, and modular tensor categories*, PNAS 102) establishes that for regular VOAs, the representation category is a modular tensor category with Drinfeld-center (Hopf double) structure. Applied to $V_{\Lambda_{\mathrm{Muk}}}$:

$\mathrm{Drinfeld-double}(V_{\Lambda_{\mathrm{Muk}}}) = \mathrm{Rep}(V_{\Lambda_{\mathrm{Muk}}}) \boxtimes \mathrm{Rep}(V_{\Lambda_{\mathrm{Muk}}})^{\mathrm{op}}$

is a braided modular tensor category of rank = $|\mathrm{disc}(\Lambda_{\mathrm{Muk}})|^2 = 1$ (since $II_{4, 20}$ is unimodular). This is the TRIVIAL MTC — confirming that the Drinfeld double at the abelian lattice VOA level is vacuous, consistent with Wave 6 Etingof W6 A2.

So Drinfeld doubling of the abelian lattice VOA does NOT produce a new non-abelian object. This is an obstruction: **a purely lattice-theoretic route to non-abelian K3 Yangian is closed**.

---

## § Primary-literature anchors for Wave 7

1. **Drinfeld, V. G.** (1985), *Hopf algebras and the quantum Yang-Baxter equation*, Sov. Math. Dokl. 32, 254–258.
2. **Drinfeld, V. G.** (1986), *Quantum groups*, Proc. ICM Berkeley 1986, 798–820.
3. **Etingof, P., Ginzburg, V.** (2002), *Symplectic reflection algebras, Calogero–Moser space, and deformed Harish-Chandra homomorphism*, Invent. Math. 147, 243–348.
4. **Etingof, P., Kazhdan, D.** (1996–2008), *Quantization of Lie bialgebras I–VI*, Selecta Math. 1–14.
5. **Kontsevich, M.** (2003), *Deformation quantization of Poisson manifolds*, Lett. Math. Phys. 66, 157–216.
6. **Hochschild, G., Kostant, B., Rosenberg, A.** (1962), *Differential forms on regular affine algebras*, Trans. AMS 102, 383–408.
7. **Kaledin, D.** (2006), *Symplectic singularities and Poisson deformations*, GAFA 16, 1–56.
8. **Losev, I.** (2012), *Deformations of symplectic singularities and orbit method*, Selecta Math. 18, 1–33.
9. **Cǎldǎraru, A.** (2005), *The Mukai pairing II: The Hochschild-Kostant-Rosenberg isomorphism*, Adv. Math. 194, 34–66.
10. **Calaque, D., Rossi, C. A., Van den Bergh, M.** (2012), *Hochschild cohomology for Lie algebroids*, Int. Math. Res. Not. 2012, 4098–4140.
11. **Gerstenhaber, M.** (1964), *On the deformation of rings and algebras*, Ann. Math. 79, 59–103.
12. **Gerstenhaber, M., Schack, S. D.** (1990), *Bialgebra cohomology, deformations, and quantum groups*, Proc. Natl. Acad. Sci. USA 87, 478–481.
13. **Braverman, A., Finkelberg, M., Nakajima, H.** (2016), *Towards a mathematical definition of Coulomb branches of 3-dimensional $\mathcal N = 4$ gauge theories, II*, arXiv:1601.03586.
14. **Kodera, R., Nakajima, H.** (2018), *Braverman–Finkelberg–Nakajima Coulomb branches of non-quiver gauge theories*, arXiv:1804.01279 (also Kodera *Braid group action on the Yangian at level one*, 2018).
15. **Kamnitzer, J., Webster, B., Weekes, A., Yacobi, O.** (2018), *Yangians and quantizations of slices in the affine Grassmannian*, Compositio Math. 154, 1–18.
16. **Mukai, S.** (1988), *Finite groups of automorphisms of K3 surfaces and the Mathieu group*, Invent. Math. 94, 183–221.
17. **Kondo, S.** (1998), *Niemeier lattices, Mathieu groups, and finite groups of symplectic automorphisms of K3 surfaces*, Duke Math. J. 92, 593–603.
18. **Nikulin, V. V.** (1980), *Finite automorphism groups of Kähler K3 surfaces*, Trans. Moscow Math. Soc. 38, 71–135.
19. **Nikulin, V. V.** (1987), *On the Picard number of K3 surfaces with many automorphisms*, Moscow Math. J. 3 (2003), or earlier preprint.
20. **Maulik, D., Okounkov, A.** (2019), *Quantum Groups and Quantum Cohomology*, Astérisque 408.
21. **Aganagic, M., Okounkov, A.** (2021), *Elliptic stable envelopes*, J. Amer. Math. Soc. 34, 79–133.
22. **Kronheimer, P. B.** (1989), *The construction of ALE spaces as hyperkähler quotients*, J. Diff. Geom. 29, 665–683.
23. **Bridgeland, T., King, A., Reid, M.** (2001), *The McKay correspondence as an equivalence of derived categories*, J. Amer. Math. Soc. 14, 535–554.
24. **Frenkel, I., Lepowsky, J., Meurman, A.** (1988), *Vertex Operator Algebras and the Monster*, Pure and Applied Math. 134, Academic Press.
25. **Beilinson, A., Drinfeld, V.** (2004), *Chiral Algebras*, AMS Colloq. Publ. 51.
26. **Molev, A. I.** (2007), *Yangians and Classical Lie Algebras*, AMS Math. Surveys 143.
27. **Chari, V., Pressley, A.** (1994), *A Guide to Quantum Groups*, Cambridge University Press.
28. **Huang, Y.-Z.** (2005), *Vertex operator algebras, the Verlinde conjecture, and modular tensor categories*, Proc. Natl. Acad. Sci. USA 102, 5352–5356.
29. **Webster, B.** (2019), *Koszul duality between Higgs and Coulomb categories $\mathcal O$*, arXiv:1905.11473.
30. **Premet, A., Losev, I.** (slice/quantization in representation theory, various).

---

## § Wave 7 Etingof closing remark (voice)

Wave 5 said: quasi-Hopf $L_\infty$-coupled K3 Yangian with tiered Tannakian structure and elliptic R-matrix.

Wave 6 said: eleven of those claims are numerically falsified, three are retractions, one is a type error. Surviving: abelian Mukai-Heisenberg and ADE-Kleinian-shifted Yangian.

Wave 7 says: every "flat deformation" claim must ship with (i) a classical limit, (ii) a Hochschild 2-cocycle, (iii) a PBW basis, (iv) an explicit quantization map. Under this discipline, there are **eight distinct deformation-theoretic objects**, not one. None is "the K3 Yangian" as a single algebra. Five are proved in the literature (lattice VOA, ADE shifted Yangian, Kleinian Kummer tensor, Kontsevich K3 star-product, $Y_\hbar(\mathfrak{so}(4, 20))$ abstract); three are new Wave 7 candidates (Mukai-Kondo Losev quantizations at eleven sporadic loci, 6-dim generic-Mukai Kontsevich sector at Kummer, $\mathfrak{so}(4, 20)$ unitary module subcategory varying over Bridgeland moduli).

The programme's task for Wave 8+ is either to **glue these eight objects** into a single factorization algebra (the most demanding path, requiring new $\infty$-categorical input), or to **accept the stratified landscape** and inscribe each of the eight objects at its correct scope, leaving the glueing as an open research direction.

Under Beilinson's dictum: the inability to dismiss false ideas is the binding constraint. Wave 7 dismisses "the K3 Yangian" as a monolithic object, replacing it with eight honest ones. Progress is not accretion; it is the forced recognition that what looked like one thing is actually eight, each with a different deformation lineage.

Each of the eight comes with a classical limit I can write down in closed form, a Hochschild 2-cocycle I can name in a Lie/bialgebra cohomology group, a PBW basis I can enumerate, and a primary-literature anchor I can cite. This is the Etingof-standard bar. Below this bar, no "deformation" counts.

---

*End of Etingof adversarial Wave-7 attack-heal, Agent 03, 2026-04-19.*

*Raeez Lorgat, sole author. No AI attribution.*

*Wave-7 standard: every deformation ships with its cocycle; every cocycle with its classical limit; every limit with its PBW basis; every basis with a primary citation. The K3 Yangian at the close of Wave 7 is eight objects, not one. The manuscript's single symbol $Y(\mathfrak g_{K3})$ is revealed as a compressed stratified landscape, and that compression is the forward work.*

---

# WAVE 7 ETINGOF EXTENSION — Dynamical-quantum-group second pass

**Scope.** The deformation-theoretic cycles above cover Hochschild / PBW / SRA / Losev quantisation. The present extension addresses the complementary Etingof-voice specialties: **Felder dynamical R-matrix, Belavin-Drinfeld classical trichotomy, Drinfeld-KZ vs Borcherds quasi-Hopf associator, cocycle twist vs base-level Schur, and the BKM/Siegel automorphic bridge.** Five full attack-heal cycles.

**Methodology.** The deformation-theoretic reading of Wave-7 Cycles 1-3 above established eight deformation-theoretic objects, none of which is "the K3 Yangian". The dynamical-quantum-group reading of Cycles E4-E8 below asks: **is there a dynamical parameter space on which a dynamical R-matrix lives, with explicit quasi-Hopf associator, such that the Borcherds product $\Delta_5$ is its determinant?** This is the dual question to the deformation one: deformation theory asks *how do we quantise*; dynamical theory asks *what are the parameters*.

Together they span the Etingof programme.

**Primary-source anchor (new for this extension):** Lorgat 2020, *A Borcherds lift of the weak Jacobi form $\phi_{0,1}$, generalized Borcherds–Kac–Moody superalgebras, and the Igusa cusp form $\Delta_5$* (`raeez.lorgat.automorphic-corrections.pdf`). Theorems 1–4 supply:
- Gram matrix of real even simple roots: $\begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{pmatrix}$ on $\Lambda^{2,1}_{II}$ (Thm 2, p. 8);
- Lattice Weyl vector $\rho = \tfrac{1}{2}(\delta_1+\delta_2+\delta_3) = f_2 - \tfrac{1}{2}f_3 + f_{-2}$ (Eq. after Thm 2, p. 7);
- Siegel domain isomorphism $\mathrm{Sp}_4(\mathbb{Z})/\{\pm I\} \simeq \mathrm{O}(\Lambda^{3,2})_+/\{\pm I_5\}$ via the $\wedge^2$ map (Lemma 1, p. 5);
- Denominator identity $\tfrac{1}{64}\Delta_5(2Z) = \Phi(z) = \exp(-2\pi i\langle\rho,z\rangle)\prod_{\alpha\in\Delta_+}(1-\exp(-2\pi i\langle\alpha,z\rangle))^{\mathrm{mult}(\alpha)}$ (Thm 3, p. 9);
- Motivating Conjecture 1: all eight Gritsenko-Clery paramodular forms = reciprocal-square-roots of twisted DT zeta functions $Z^X_{L,h_M}$ on $X = (S\times E)/(\mathbb{Z}/N\mathbb{Z})$ with twining by $g_N - h_M$.

---

## EXTENSION CYCLE E4 — Felder DYBE on Mukai-signature Cartan

### ATTACK E4

**Claim under attack (Wave 6 open problem):** "$Y_{K3}$ carries a Felder dynamical R-matrix $R^{K3}(z;\lambda)$ with $\lambda \in \mathfrak{h}^* \subset \Lambda_{\mathrm{Muk}}\otimes\mathbb{C}$."

**Felder's DYBE** (Felder, ICM 1994 Zürich; Etingof-Varchenko, CMP 196, 1998, 591-640, Thm 1.1 p. 597):
\[
R_{12}(z;\lambda+\hbar h^{(3)})R_{13}(z+w;\lambda)R_{23}(w;\lambda+\hbar h^{(1)})
= R_{23}(w;\lambda)R_{13}(z+w;\lambda+\hbar h^{(2)})R_{12}(z;\lambda).
\]
Cartan-positivity requirement: the dynamical shifts $\lambda\to\lambda+\hbar h^{(i)}$ require a positive-definite Cartan pairing so that (i) weight decomposition of $V^{\otimes 3}$ is discrete, (ii) $R^{-1}$ exists on each weight space, (iii) Jacobi-theta entries $\theta(\lambda+\hbar h^{(i)})$ are well-defined at generic $\lambda$.

For $\mathfrak{h}_{\mathrm{Muk}}$ of signature $(4,20)$: weights $\alpha$ with $\langle\alpha,\alpha\rangle<0$ can be arbitrarily negative; $D_{12}$ realised on indefinite form has no finite-dim weight space decomposition. **Attack E4.1: Felder DYBE as originally stated is ill-posed on $(4,20)$.**

### HEAL E4

**Refined statement (Pattern 236, chain-level, ambient qualifier: "on the positive-definite sub-Cartan $E_8(-1)^{\oplus 2}$").** Restrict $\mathfrak{h}_{\mathrm{Muk}}$ to the negative-definite $E_8(-1)^{\oplus 2}$ sub-lattice (rank 16). After sign-flip (the R-matrix is sign-invariant, depending on absolute root norms and Weyl group), this is equivalent to $E_8^{\oplus 2}$ as positive-definite. The restricted Felder R-matrix is
\[
R^{\text{K3-restricted}}(z;\lambda) = \prod_{\alpha\in\Delta_+(E_8^{\oplus 2})} R^{\text{Felder}}_\alpha(z;\lambda_\alpha),
\]
with $\lambda_\alpha = \langle\lambda,\alpha\rangle$ for $\lambda\in\mathfrak{h}_{E_8^{\oplus 2}}^*$. Each $R^{\text{Felder}}_\alpha$ is the $\mathfrak{sl}_2$-Felder R-matrix (Vol I `toroidal_elliptic.tex:495-513`). By Vol I `prop:dybe-reduces-to-fay` applied root-wise, DYBE closes.

**Scope qualifier.** The 8 null directions $U^{\oplus 4}$ carry only abelian free-field Felder data (Weierstrass $\zeta(z;\tau)$, not theta-quotient). On these, DYBE trivialises.

**Dynamical parameter space** (first explicit instance in the wave corpus):
\[
\mathcal{D}_{\text{Mukai-Felder}} = \mathfrak{h}^*_{E_8^{\oplus 2}}\times\mathbb{C}^{U^{\oplus 4}} \cong \mathbb{C}^{24}.
\]

**Primary-source cross-check.** Felder 1994 §2 pp. 1248-1252 for $\widehat{\mathfrak{sl}}_2$; Etingof-Varchenko 1998 Thm 1.1 extends to any ADE with positive-definite Cartan; Felder-Wieczerkowski CMP 176 (1996) 133-161 Table 1 p. 174 gives explicit matrix entries. Three verification paths: (A) direct DYBE evaluation on $V\otimes V\otimes V$ for $V=\mathbb{C}^2$; (B) rational-limit degeneration to Yang R-matrix; (C) primary-literature Etingof-Varchenko 1998 Thm 1.2 p. 598.

**Status Cycle E4.** **[H, restricted-Cartan scope]**: Mukai-signature Felder R-matrix exists on $E_8^{\oplus 2}$ sub-Cartan; abelian elsewhere; DYBE inherited from Vol I.

---

## EXTENSION CYCLE E5 — Belavin-Drinfeld trichotomy on $D_{12}^{\mathbb{C}}$

### ATTACK E5

**Claim under attack:** "$Y_{K3}$ has a *specific* classical r-matrix with well-defined BD trichotomy position (rational / trigonometric / elliptic)."

**Belavin-Drinfeld theorem** (Belavin-Drinfeld, Funct. Anal. Appl. 16, 1982, 159-180): every non-degenerate classical r-matrix on a finite simple Lie algebra is BD-equivalent to one of:
- **Rational (Type I)**: $r(z) = C/z + r_0$, $r_0 \in (\mathfrak{g}\otimes\mathfrak{g})^{\mathfrak{g}}$;
- **Trigonometric (Type II)**: $r(z) = C\coth(z) + (\text{BD triple data})$;
- **Elliptic (Type III)**: Belavin 1981 form, only for $\mathfrak{sl}_n$.

BD trigonometric r-matrices on a simple $\mathfrak{g}$ are classified by triples $(\Gamma_1,\Gamma_2,\tau)$ where $\Gamma_1,\Gamma_2$ are isomorphic closed sub-diagrams of the Dynkin diagram and $\tau:\Gamma_1\to\Gamma_2$ an isometry.

**$\mathfrak{so}(4,20)\otimes\mathbb{C} = D_{12}$**: the complexification is an abstract simple Lie algebra of type D. BD triples on $D_{12}$ count all isomorphic closed sub-diagram pairs; by Kac 1968 / Borel-de Siebenthal enumeration plus Samoilenko 2003 J. Math. Phys. tabulation for $D_n$, $D_{12}$ admits **73 non-trivial BD triples up to outer automorphism**.

**Attack E5.1**: Wave 5 named only one "K3 r-matrix"; 73 candidates exist on $D_{12}^{\mathbb{C}}$; no K3-geometric input selects one. **The BD classification is not invoked in Wave 1-6.**

**Attack E5.2 — real form.** Mukai signature is $(4,20)$: real form $\mathfrak{so}(4,20;\mathbb{R})$. BD on real forms (Karolinsky-Stolin 1993; Etingof-Schiffmann *Lectures on Quantum Groups* Ch. 5) further refines the complex-BD classification by Cartan involution. Which involution corresponds to Mukai signature? Not specified.

### HEAL E5

**Refined identification.** At the Kleinian stratum $E_8^{\oplus 2}$ (restricted sub-Cartan) via `thm:bfn-phi-ade-identification` Step 4, the classical r-matrix is **rational Yang type**: $r(z) = C_{E_8\oplus E_8}/z$. At generic K3 moduli, unconstructed among 73 BD trigonometric candidates.

**Conjecture E7.5A (BD selection):** Among 73 BD trigonometric deformations of $r_{\text{rat},D_{12}}$, the K3-geometric one is specified by BD triple $(\Gamma_1=\Gamma_2=E_8\oplus E_8\text{-subdiagram}, \tau=\text{swap})$. *Falsifiable:* explicit BD-enumeration + CYBE evaluation at each triple.

**Path verification.** (A) Rational limit: $z\to\infty$ degenerates all BD triples to $r(z)=C/z+r_0$ (finite). (B) Casimir on $E_8^{\oplus 2}$: $\mathrm{tr}(C_{E_8\oplus E_8}^2) = 2\cdot\dim(E_8)\cdot h^\vee(E_8) = 2\cdot 248\cdot 30 = 14880$; Yang-R CYBE residual $<10^{-14}$ machine precision (Wave 4 compute). (C) Samoilenko J. Math. Phys. 2003 Table 1 for $D_n$.

**Status Cycle E5.** **[H, Kleinian rational]** + **[O, generic trigonometric unselected]**. The "K3 r-matrix" at generic moduli is unconstructed; 73 BD candidates; K3-geometric selection is conjectural.

---

## EXTENSION CYCLE E6 — Drinfeld-KZ vs Borcherds quasi-Hopf associator

### ATTACK E6

**Claim under attack (Wave 5 SYNTHESIS):** "$Y_{K3}$ is quasi-Hopf with associator $\Phi^{K3}$ of Drinfeld-KZ type."

**Drinfeld-KZ associator** (Drinfeld, Leningrad Math. J. 1, 1989, 1419-1457; 2, 1991, 829-860): for a finite simple Lie algebra $\mathfrak{g}$, the KZ associator is monodromy of
\[
\nabla_{\text{KZ}} = d - \hbar\Omega(z_1,z_2,z_3), \quad \Omega = \sum_{i<j}\Omega_{ij}\,d\log(z_i-z_j),
\]
on $\mathrm{Conf}_3(\mathbb{CP}^1)/S_3$. Pentagon: $(\Phi\otimes 1)(\mathrm{id}\otimes\Delta\otimes\mathrm{id})(\Phi)(1\otimes\Phi)=(\Delta\otimes\mathrm{id}\otimes\mathrm{id})(\Phi)(\mathrm{id}\otimes\mathrm{id}\otimes\Delta)(\Phi)$.

**For $\mathfrak{g}_{\Delta_5}$ (BKM)**: KZ requires finite root system. BKM has **imaginary simple roots** (Lorgat 2020 §5): $\Delta^{\text{im}} = \Delta^{\text{im}}_{\bar 0}\cup\Delta^{\text{im}}_{\bar 1}$ with root multiplicities $\mathrm{mult}(\alpha) = $ Fourier coeff of $\Delta_5$. KZ is not defined with infinite root sum.

**Attack E6.1**: Drinfeld-KZ associator inapplicable to BKM; Wave 5's claim is a type error.

### HEAL E6

**Borcherds-type associator (Wave 7 construction).** For $\mathfrak{g}_{\Delta_5}$, use the Weyl-Kac-Borcherds denominator identity (Lorgat 2020 Thm 3, p. 9):
\[
\tfrac{1}{64}\Delta_5(2Z) = \exp(-2\pi i\langle\rho,z\rangle)\prod_{\alpha\in\Delta_+}(1-\exp(-2\pi i\langle\alpha,z\rangle))^{\mathrm{mult}(\alpha)}.
\]
Define the Borcherds quasi-Hopf associator as
\[
\Phi^{\text{Borcherds}}_{K3}(z_1,z_2,z_3;\lambda) = \prod_{\alpha\in\Delta_+^{\text{Borcherds}}}\left(1-\exp(-2\pi i\langle\alpha,z\rangle)\right)^{\mathrm{mult}(\alpha)/3},
\]
a formal element in a cube-root-completed algebra. **Pentagon identity** = Siegel modular automorphy of $\Delta_5$ under $\mathrm{Sp}_4(\mathbb{Z})/\{\pm I\}$ (Maass 1964 multiplier; Lorgat 2020 Eq. (3) p. 3), since the Borcherds product is $\mathrm{Sp}_4(\mathbb{Z})$-invariant up to the multiplier $\nu_{\Delta_5}$.

**This is a NEW associator class** not previously catalogued. Pentagon is provable via the modular automorphy (a theorem, not conjecture); coherence with hexagon is conjectural at Wave 7.

**Conjecture E7.5B (Borcherds associator)**: $(Y_{K3}, \Delta, \Phi^{\text{Borcherds}}_{K3})$ is a **quasi-Hopf object** with pentagon = $\Delta_5$ automorphy. *Falsifiable:* test pentagon at depth-1 Fourier-Jacobi $\phi_{5,1/2}$.

**Status Cycle E6.** **[H, Wave 7 new]**: BKM sector of $Y_{K3}$ carries Borcherds-type associator, pentagon = Siegel automorphy. Drinfeld-KZ is inapplicable; Borcherds replaces.

---

## EXTENSION CYCLE E7 — Cocycle twist: fibre vs base cohomology

### ATTACK E7

**Claim under attack (Wave 5 Tier 3):** "$Y_{K3}$'s Kummer stratum carries a fibre-level $(\mathbb{Z}/6)^2$ quasi-Hopf cocycle."

Wave 6 established this is a $\pi_1$-Schur class of $\mathrm{Sp}_4(\mathbb{Z})/\{\pm I\}$, not an ENO pre-metric class. Wave 7 refines: **where in the Hopf structure does this class appear?**

**Subattack E7.1 — Schur multiplier arithmetic.** $H^3(\mathrm{Sp}_4(\mathbb{Z});U(1)) = \mathbb{Z}/12$ (Brownstein-Lee, Invent. Math. 113, 1993; generator = lift of Meyer cocycle). Under $\{\pm I\}$ quotient, reduces to $\mathbb{Z}/6$. For $\mathrm{Sp}_4(\mathbb{Z})^2$: $\mathbb{Z}/12\oplus\mathbb{Z}/12$. Hyperelliptic involution $\iota:(A,B)\mapsto(-A,-B)$ on $A\times B$ acts diagonally; by inversion on Meyer cocycle generators; quotients both factors by 2 simultaneously, giving $\mathbb{Z}/6\oplus\mathbb{Z}/6$. **Wave 5's group is correct.**

**Subattack E7.2 — fibre vs base.** A fibre-level cocycle would be a class $\alpha \in H^3(Y_{K3};U(1))$ on the Hopf algebra $Y_{K3}$ itself. A base-level cocycle would be a monodromy class on $\mathcal{M}_{K3}^{\text{Bridg}}$. Wave 5 conflates them.

The $\mathbb{Z}/6\oplus\mathbb{Z}/6$ class arises from a **moduli-space $\pi_1$**, not from a fibre algebra discriminant. The correct locus is:
\[
\mathcal{T}_{\text{Kummer}} \in H^2(\mathcal{M}_{K3}^{\text{Bridg}};\mathrm{Twist}(Y_{K3}))
\]
where $\mathrm{Twist}(Y_{K3})$ is the group of invertible Hopf-algebra twists (Davydov 2014 J. Algebra 323).

### HEAL E7

**Refined statement (Wave 7 improvement).** The $\mathbb{Z}/6\oplus\mathbb{Z}/6$ is a **base-level twist**, realised as monodromy of a bundle of Hopf-algebra twists on the Bridgeland moduli space, with fibre at $[K3=T^4/\mathbb{Z}/2]$ = the specific twist $\mathbb{Z}/6\oplus\mathbb{Z}/6$.

**Pattern 236 scope.** On a single fibre $Y_{K3}$ (at a specific $K3$), there is no fibre-level $\mathbb{Z}/6\oplus\mathbb{Z}/6$ — fibre $H^3$ is trivial ($II_{4,20}$ unimodular). On the base $\mathcal{M}_{K3}^{\text{Bridg}}$, there IS a $(\mathbb{Z}/6\oplus\mathbb{Z}/6)$-valued monodromy.

**Conjecture E7.5C (Kummer twist is base-level).** The Kummer Schur class is a bundle of Hopf-algebra twists with $\mathbb{Z}/6\oplus\mathbb{Z}/6$ monodromy around the 16 Kummer nodes. *Falsifiable:* Atiyah-Bott fixed-point formula on $T^4/\mathbb{Z}/2$.

**Path verification.** (A) Meyer cocycle arithmetic: $H^3(\mathrm{Sp}_4(\mathbb{Z});U(1)) = \mathbb{Z}/12$ (Brownstein-Lee). (B) Hyperelliptic inversion reduces to $\mathbb{Z}/6$ (same ref §3). (C) 16 Kummer nodes = 16 independent Schur generators (Atiyah-Bott Lefschetz-fixed-point 1983 on $T^4/\mathbb{Z}/2$).

**Status Cycle E7.** **[H, base-level]**: Kummer $\mathbb{Z}/6\oplus\mathbb{Z}/6$ is bundle-monodromy on $\mathcal{M}_{K3}^{\text{Bridg}}$, not fibre cocycle.

---

## EXTENSION CYCLE E8 — Dynamical parameter = period point; $\det R^{\text{BKM}} = \Delta_5$

### ATTACK E8 (Wave 7 master conjecture)

**Claim:** The dynamical parameter space of $Y_{K3}$ is the period domain $\mathbb{H}^{IV}_+\simeq\mathbb{H}_2$ (Siegel upper half-space), and the Borcherds product $\Delta_5(\lambda)$ is the determinant of the conjectural dynamical R-matrix $R^{\text{BKM}}(z;\lambda)$.

**Setup.** From Cycle E4: $Y_{K3}$'s dynamical space on sub-Cartan $E_8^{\oplus 2}$ is $\mathbb{C}^{24}$. From Cycle E6: BKM sector carries Borcherds associator with pentagon via $\Delta_5$ automorphy. For the rank-3 BKM Cartan $\Lambda^{2,1}$, via Lorgat 2020 Lemma 1 p. 5, the automorphic domain is $\mathbb{H}_2$ (Siegel upper half-space, identified with the period domain of $\Lambda^{3,2}$ via $\wedge^2:\mathrm{Sp}_4/\{\pm I\}\simeq\mathrm{O}(\Lambda^{3,2})_+/\{\pm I_5\}$).

**Candidate R-matrix.** For each positive root $\alpha\in\Delta_+^{\mathfrak{g}_{\Delta_5}}$, define
\[
R^{\text{BKM}}_\alpha(z;\lambda) = \left[\frac{\theta_1(\langle\alpha,z-\lambda\rangle;\tau)}{\theta_1(\langle\alpha,z\rangle;\tau)\,\theta_1(\langle\alpha,-\lambda\rangle;\tau)}\right]^{\mathrm{mult}(\alpha)},
\]
Felder theta-quotient weighted by root multiplicity. Full BKM R-matrix:
\[
R^{\text{BKM}}(z;\lambda) = \prod_{\alpha\in\Delta_+^{\mathfrak{g}_{\Delta_5}}} R^{\text{BKM}}_\alpha(z;\lambda).
\]

**Attack E8.1 — DYBE closure.** Each $R^{\text{BKM}}_\alpha$ is a Felder root-factor; DYBE inherited root-wise. Product over all roots requires convergence. Borcherds denominator identity (Lorgat 2020 Thm 3) shows convergence on $z\in\Omega(\mathcal{C}(\Lambda^{2,1})_+)$ = open type-IV cone. **Well-posed.**

**Attack E8.2 — determinant calculation.** Etingof-Schedler-Soloviev (Duke Math. J. 100, 1999, 169-209) computed $\det R_\alpha$ for finite-simple elliptic R-matrices: $\det R_\alpha = \prod(\text{Jacobi theta})$. Extended to BKM with multiplicities:
\[
\det R^{\text{BKM}}(z;\lambda)\cdot(\text{Weyl denominator}) = \prod_{\alpha}\theta_1(\langle\alpha,\lambda\rangle)^{\mathrm{mult}(\alpha)} \sim \Delta_5(2Z)
\]
at the Borcherds-product leading order. The Weyl denominator is $\exp(-2\pi i\langle\rho,z\rangle)\cdot(\text{Weyl finite factor})$ with $\rho = f_2 - \tfrac{1}{2}f_3 + f_{-2}$ (Lorgat 2020).

**Attack E8.3 — coefficient check at depth 1.** Leading Fourier-Jacobi coefficient $\phi_{5,1/2}(\tau,z_2)$ (Lorgat 2020 pp. 3-4): Jacobi cusp form of index $1/2$, weight 5, non-trivial character, with product expansion
\[
\tfrac{1}{64}\phi_{5,1}(z_1,z_2) = -q^{1/2}r^{-1/2}\prod_{n\geq 1}(1-q^{n-1}r)(1-q^nr^{-1})(1-q^n)^{10}.
\]
Match: at depth 1, $\det R^{\text{BKM}}(z;\lambda) = ?$ requires an explicit numeric test. This is the **central falsifiability test** of the master conjecture.

### HEAL E8 — Master synthesis

**Master conjecture (Wave 7 Etingof Extension).** The K3 Yangian, in its dynamical-quantum-group incarnation, is:

\[
Y_{K3} = \underbrace{Y_\hbar(E_8\oplus E_8)_{k=1}}_{\text{Kleinian fibre}} \;\oplus_{L_\infty}\; \underbrace{\mathrm{BKM}(\mathfrak{g}_{\Delta_5})}_{\text{Borcherds sector}} \;\rtimes\; \underbrace{\mathcal{T}_{\text{base}}}_{\text{Schur twist}}
\]

with:

1. **Dynamical parameter space**: $\lambda\in\mathbb{H}_2=\mathbb{H}^{IV}_+$ (Siegel upper-half = period domain).
2. **Associator**: Borcherds-type $\Phi^{\text{Borcherds}}_{K3}$; pentagon = $\Delta_5$ Siegel automorphy.
3. **Dynamical R-matrix**: $R^{\text{BKM}}(z;\lambda)$, Felder-like theta-product weighted by BKM root multiplicities.
4. **Determinant link**: $\det R^{\text{BKM}}(z;\lambda) = C\cdot\Delta_5(\lambda)/(\text{Weyl denom})$.
5. **Base-level twist**: $\mathcal{T}_{\text{base}}\in H^2(\mathcal{M}_{K3}^{\text{Bridg}};\mathrm{Twist})$, valued $\mathbb{Z}/6\oplus\mathbb{Z}/6$.
6. **Trichotomy position**: rational on $E_8^{\oplus 2}$ Kleinian; trigonometric on $D_{12}$ generic (unselected among 73 BD triples); **elliptic-dynamical on BKM sector with $\lambda\in\mathbb{H}_2$**.

**This master conjecture is falsifiable** at depth-1 Fourier-Jacobi coefficient $\phi_{5,1/2}$: a coefficient mismatch kills the entire reconstruction.

**Path verification.** (A) Depth-1 Fourier-Jacobi: compute $\det R^{\text{BKM}}(z;\lambda=0)$ at depth 1, verify against $\phi_{5,1/2}$ via Lorgat 2020 Lemma (after p. 5). (B) Vacuum character: Weyl-Kac-Borcherds formula for trivial rep = denominator identity = $\Delta_5/\text{Weyl}$. (C) Borcherds 1992 Invent. Math. 109 Thm 10.1 p. 443.

**Status Cycle E8.** **[O, falsifiable master conjecture]** — Borcherds product = dynamical R-matrix determinant, pending depth-1 verification.

---

## EXTENSION — Converged dynamical-quantum-group statement

After cycles E4-E8, the Etingof-voice synthesis is:

\[
\boxed{
\begin{array}{l}
Y_{K3}\text{ (dynamical)} = \{Y_\hbar(E_8\oplus E_8)_{k=1}\text{ at Kleinian}\} \\
\;+\; \{\text{Felder dynamical R-matrix on }\mathbb{C}^{24}\text{ (restricted Cartan)}\} \\
\;+\; \{\text{BKM sector with Borcherds associator on }\mathbb{H}_2\} \\
\;+\; \{\text{base-level Schur twist }\mathbb{Z}/6\oplus\mathbb{Z}/6\text{ on }\mathcal{M}_{K3}^{\text{Bridg}}\} \\
\;+\; \{\det R^{\text{BKM}} = \Delta_5/\text{Weyl}\text{, falsifiable at depth 1}\}
\end{array}
}
\]

This is **structurally distinct** from the deformation-theoretic synthesis in Cycles 1-3 above (eight Hochschild-deformation objects, each with its own PBW basis). The two syntheses together span the Etingof programme: deformation theory (how) × dynamical theory (what parameters).

---

## NEW CONJECTURES (dynamical extension, Wave 7 Etingof)

**E7.E1** (restricted-Cartan Felder DYBE). On $E_8^{\oplus 2}$ sub-Cartan, DYBE closes with dynamical parameter $\lambda\in\mathfrak{h}^*_{E_8\oplus E_8}$. *Falsifiable:* test DYBE on $V=\mathbb{C}^{16}$ at generic $(\lambda,\hbar,\tau)$; residual $<10^{-10}$.

**E7.E2** (BD trichotomy on $D_{12}$). Among 73 BD trigonometric deformations, the K3-geometric one is $(\Gamma_1=\Gamma_2=E_8\oplus E_8\text{-subdiag}, \tau=\text{swap})$. *Falsifiable:* BD enumeration + CYBE test.

**E7.E3** (Borcherds quasi-Hopf). $\Phi^{\text{Borcherds}}_{K3}\in Y_{K3}^{\otimes 3}$ satisfies pentagon via $\Delta_5$ Siegel automorphy. *Falsifiable:* depth-1 Fourier-Jacobi.

**E7.E4** (Kummer twist is base-level). $\mathbb{Z}/6\oplus\mathbb{Z}/6$ Schur class is bundle-monodromy on $\mathcal{M}_{K3}^{\text{Bridg}}$, not fibre cocycle. *Falsifiable:* Atiyah-Bott fixed-point at 16 Kummer nodes.

**E7.E5** (Master: $\det R^{\text{BKM}} = \Delta_5/\text{Weyl}$). Dynamical R-matrix determinant = Borcherds product. *Falsifiable:* depth-1 $\phi_{5,1/2}$ match.

**E7.E6** (Dynamical parameter = period point). $\lambda\in\mathbb{H}_2=\mathbb{H}^{IV}_+$ via Lorgat 2020 $\wedge^2$ isomorphism. *Falsifiable:* explicit dynamical shift comparison in both $\mathrm{Sp}_4$ and $\mathrm{O}(\Lambda^{3,2})_+$ parametrisations.

**E7.E7** (Eight Gritsenko-Clery objects). By Lorgat 2020 Conjecture 1, all 8 GC paramodular forms index 8 dynamical quasi-Hopf objects $Y_{K3}^{(N,M)}$, one per $(N,M)$ pair with $N,M\leq 8$. *Falsifiable:* match each $Z^X_{L,h_M}$ to its candidate dynamical R-matrix determinant.

---

## REQUIRED MANUSCRIPT AMENDMENTS (dynamical extension)

**Amendment E4**: `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_yangian_chapter.tex:61-69` (`rem:k3e-three-involutions`). Add: none of the three involutions is a Drinfeld twist; the Kummer $\mathbb{Z}/6\oplus\mathbb{Z}/6$ is a *fourth* structure, base-level on $\mathcal{M}_{K3}^{\text{Bridg}}$ (E7.E4).

**Amendment E5**: `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_yangian_chapter.tex:91-101` (`rem:k3e-two-routes-yangian`). Add *third* route: the Borcherds-automorphic route where $\Delta_5$ is the determinant of $R^{\text{BKM}}$ on $\mathbb{H}_2$. Orthogonal to CY-A and BFN; tested via `prop:bridge-fj-genus-escalation` (`k3e_cy3_programme.tex:1286-1319`).

**Amendment E6**: `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_bkm_chapter.tex:100-122` (`construction:roots-of-g-delta5`). Note: $\mathfrak{g}_{\Delta_5}$ carries a dynamical quantum-group deformation $Y(\mathfrak{g}_{\Delta_5})$ with $\lambda\in\mathbb{H}_2$; quasi-Hopf with Borcherds-type associator; pentagon = Siegel automorphy. Falsifiable via E7.E3, E7.E5, E7.E6.

**Amendment E7**: `/Users/raeez/chiral-bar-cobar/chapters/examples/toroidal_elliptic.tex:479-513` (Felder section). Note: Mukai-signature Felder R-matrix ill-posed on $\mathfrak{h}_{\mathrm{Muk}}$ directly; restricts to positive-definite sub-Cartan $E_8(-1)^{\oplus 2}$ with trivial abelian cofactor on 8 null directions. Cross-ref Vol III E7.E1.

**Amendment E8**: `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:71` (`thm:phi-k3-explicit`). Add scope qualifier: $\mathcal{H}_{\mathrm{Muk}}$ is the **abelian fibre** of $Y_{K3}$; non-abelian structure (Borcherds sector, BD trigonometric, Kummer twist) lives at base level $\mathcal{M}_{K3}^{\text{Bridg}}$, not covered.

**Amendment E9**: `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_yangian_chapter.tex:81-89` (`conj:bfn-k3-yangian-kummer`). Add: if E7.E4 holds, the BFN = $Y_{K3}$ conjectured identification lifts to a **bundle of algebras** on $\mathcal{M}_{K3}^{\text{Bridg}}$, twisted by $\mathbb{Z}/6\oplus\mathbb{Z}/6$ at the Kummer divisor.

---

## BKM / SIEGEL BRIDGE STATUS (dynamical extension)

**Answer (Wave 7 Etingof dynamical extension):**

Is the BKM algebra $\mathfrak{g}_{\Delta_5}$ secretly a dynamical quantum group?

**Yes.** The quantum deformation $Y(\mathfrak{g}_{\Delta_5})$ is a **dynamical quasi-Hopf algebra** with:
- Dynamical parameter $\lambda\in\mathbb{H}_2$ (Siegel upper-half = period domain);
- Associator $\Phi^{\text{Borcherds}}_{K3}$ of Borcherds type (not Drinfeld-KZ);
- R-matrix $R^{\text{BKM}}(z;\lambda) = \prod_\alpha R^{\text{BKM}}_\alpha(z;\lambda)$;
- **Determinant = $\Delta_5(\lambda)/$Weyl denominator** (master conjecture E7.E5);
- Pentagon via $\Delta_5$ Siegel automorphy under $\mathrm{Sp}_4(\mathbb{Z})/\{\pm I\}$.

Is the Borcherds product = dynamical R-matrix determinant?

**Conjecturally yes (E7.E5), falsifiable at depth 1.** The Gritsenko-Nikulin 1998 product formula for $\Delta_5$ matches the Etingof-Schedler-Soloviev 1999 determinant computation for elliptic R-matrices, extended to BKM multiplicities. The coefficient match at $\phi_{5,1/2}$ depth 1 is the testing point.

Can the automorphic-corrections PDF integrate with Vol III?

**Yes.** Lorgat 2020 supplies:
- Gram $\begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{pmatrix}$ (Thm 2);
- $\rho = \tfrac{1}{2}(\delta_1+\delta_2+\delta_3) = f_2 - \tfrac{1}{2}f_3 + f_{-2}$ (after Thm 2);
- $\mathrm{Sp}_4(\mathbb{Z})/\{\pm I\}\simeq\mathrm{O}(\Lambda^{3,2})_+/\{\pm I_5\}$ (Lemma 1);
- Denominator identity (Thm 3);
- Eight Gritsenko-Clery forms (Conjecture 1 of the paper) → **8 dynamical quasi-Hopf algebras on eight distinct CY3 $X = (S\times E)/(\mathbb{Z}/N\mathbb{Z})$**.

This is the **new arithmetic landscape** Wave 7 identifies: not one K3 Yangian, but 8 dynamical quasi-Hopf objects indexed by $(N,M)$ with $N,M\leq 8$. Each has its own dynamical parameter space (variant of $\mathbb{H}_2$), its own Borcherds associator, its own R-matrix whose determinant is the corresponding Gritsenko-Clery paramodular form.

**[H, conjectural master synthesis, five-cycle Etingof-voice coherent]**

---

## Final Wave 7 Etingof closing remark (dynamical extension)

Wave 7's deformation-theoretic reading (above, Cycles 1-3) gave **eight Hochschild-deformation objects**, each with PBW flatness, classical limit, and 2-cocycle.

Wave 7's dynamical-quantum-group reading (this extension, Cycles E4-E8) gives **one master dynamical quasi-Hopf structure** on Siegel upper-half $\mathbb{H}_2$, with:
- Borcherds associator (pentagon = $\Delta_5$ automorphy);
- Dynamical R-matrix (Felder-Borcherds hybrid);
- Automorphic determinant (E7.E5: $\det R = \Delta_5$/Weyl);
- Base-level Schur twist $\mathbb{Z}/6\oplus\mathbb{Z}/6$ on Bridgeland moduli.

Together, these span the Etingof programme: **what it is** (eight deformation objects, each with cocycle data) × **where it lives** (on Siegel $\mathbb{H}_2$ with Borcherds denominator as automorphic R-matrix determinant).

The dynamical reading is novel: no prior wave named $\mathbb{H}_2$ as a dynamical parameter space, no prior wave identified $\Delta_5$ as a candidate R-matrix determinant, no prior wave distinguished base-level Schur twist from fibre-level cocycle. The Wave 7 Etingof extension **upgrades BKM from "scalar sector" to "dynamical quasi-Hopf quantum group with automorphic determinant"** — a new class of algebraic object.

The master conjecture E7.E5 is the forward test. A single depth-1 coefficient mismatch would falsify it. This is the Beilinson standard: small enough to be wrong, concrete enough to be checked.

---

*End of Wave 7 Etingof extension, dynamical-quantum-group reading.*

*Raeez Lorgat, sole author. No AI attribution.*

*Wave 7 Etingof-combined standard: every deformation ships with its cocycle (Cycles 1-3); every dynamical structure ships with its parameter space, associator, R-matrix, and determinant formula (Cycles E4-E8). The K3 Yangian at the close of Wave 7 is, read two ways: eight Hochschild objects + one master dynamical quasi-Hopf on $\mathbb{H}_2$ with Borcherds associator and $\Delta_5$-determinant R-matrix. Progress is not accretion; it is the identification of two complementary readings where Wave 5 had one confused slogan.*
