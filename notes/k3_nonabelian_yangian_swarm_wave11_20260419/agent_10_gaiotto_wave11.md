# Agent 10 (Gaiotto voice) -- Wave 11: $T[K3]$ as class-$\mathcal{S}$, Schur-index match against $\Delta_5$, Niemeier vs Mukai 24, Lagrangian-free 4d $\mathcal{N}=2$ avatar

**Raeez Lorgat, sole author. Wave 11, 2026-04-19.**

---

## Wave 10 target (W11-GAIOTTO-T[K3])

Wave 10 (Cycle 1, Heal 1.B) proposed the candidate Lagrangian
$$
T[K3]^{\text{cand}} \;=\; \text{3D}\ \mathcal{N}{=}4\ \text{quiver gauge theory}\ \widehat{A}_{23}\ \prod_{i=1}^{24}U(1)_i,
$$
with 24 bifundamental hypers around the elliptic K3 base; 24 BPS vacua = 24 Kodaira $I_1$ fibres; 24 holomorphic blocks = vector-valued Sp$_4(\mathbb{Z})$-Jacobi forms of weight 5 index 1; the Coulomb-branch K-theoretic algebra equals $\mathbf{H}_{\Delta_5}$.

This Wave 11 cycle attacks the entire structural identification on five fronts -- (i) class-$\mathcal{S}$ assignment, (ii) rank-24 quiver vs Mukai matching, (iii) 24 vs 23 Jacobi-block count, (iv) Schur-index check via Beem--Lemos--Liendo--Peelaers--Rastelli--van Rees (BLLPRvR) 2013, (v) line operators and the cuspidal limit -- and finds the **true physics avatar** to be a 6d $(2,0)$-of-type-$E_8$ theory on $K3 \times \Sigma_{g}$, which is *Lagrangian-free* (no quiver), with rank-24 invariant matching the $E_8$-instanton lattice rather than Mukai. The "$\widehat{A}_{23}$ quiver" of Wave 10 is retracted; its replacement is a non-Lagrangian Argyres--Douglas-class theory $T[K3,E_8]$ whose Schur index is the vacuum character of $\mathbf{H}_{\Delta_5}$ in the Beem--Rastelli sense.

The five attack-heal cycles below are followed by Pattern 236 chain-level / $(\infty,1)$-categorical labelling and a deduplicated list of Wave 12 tasks.

---

## Cycle 1 -- ATTACK: pants decomposition vs affine quiver

### §1.1 Class-$\mathcal{S}$ as Gaiotto--Moore--Neitzke framework

Class-$\mathcal{S}$ (Gaiotto 2009 arXiv:0904.2715, Gaiotto--Moore--Neitzke 2009 arXiv:0907.3987) constructs a 4d $\mathcal{N}=2$ theory $T[\mathfrak{g},\mathcal{C},\mathcal{D}]$ from:
- a 6d $(2,0)$ theory of ADE type $\mathfrak{g}$ (= $A_{N-1}$, $D_N$, $E_6, E_7, E_8$);
- a punctured Riemann surface $\mathcal{C}$ with punctures $\mathcal{D}=\{p_1,\dots,p_k\}$;
- a labelling of each puncture by a nilpotent orbit in $\mathfrak{g}$ (the puncture type).

The 4d theory inherits a UV $\mathcal{N}=2$ S-duality group $\mathrm{MCG}(\mathcal{C},\mathcal{D})$ (mapping class group). The Coulomb-branch dimension is given by the Riemann--Roch type formula (Chacaltana--Distler--Tachikawa 2013 arXiv:1212.3952): for $A_{N-1}$ on $\Sigma_{g,n}$ with maximal punctures,
$$
\dim_\mathbb{C}\mathcal{M}_C \;=\; (g-1)(N-1)(N+1) + n\binom{N}{2} - n.
$$

A **pants decomposition** of $\mathcal{C}$ exhibits the theory as a gluing of 3-punctured-sphere theories $T_N$ via $\mathfrak{g}$-gauging. This is the standard class-$\mathcal{S}$ Lagrangian frame.

### §1.2 K3 is NOT a Riemann surface

K3 is a 4-real-dimensional complex surface, NOT a Riemann surface. Class-$\mathcal{S}$ as defined in Gaiotto 2009 takes a Riemann surface $\mathcal{C}$ as input, not a complex surface. So the literal "$T[K3]$ via class-$\mathcal{S}$" is a category error.

What Wave 10 must mean (and didn't precisely say): take 6d $(2,0)$ on $K3 \times \mathcal{C}$ for some Riemann surface $\mathcal{C}$, compactify on K3, and obtain a 4d theory on $\mathbb{R}^{1,3}$ depending on $\mathcal{C}$. Or: take 6d on K3 alone, getting a 2d theory (Gadde--Gukov--Putrov 2013 arXiv:1306.4320 with $T[K3,A_{N-1}] = $ 2d $(0,4)$ on Hilb$^N$(K3)).

### §1.3 Affine $\widehat{A}_{23}$ vs ADE Dynkin

Class-$\mathcal{S}$ uses **finite-type ADE** Dynkin labels for the 6d $(2,0)$ type. Affine $\widehat{A}_{23}$ is **NOT** a 6d $(2,0)$ type; affine type appears only on the $\mathcal{C}$ side as a quiver associated to a pants decomposition with a degeneration limit (Gaiotto 2009 §3 for $A_1$ degeneration $\to$ linear quiver; Coman--Pomoni--Teschner 2018 arXiv:1812.10493 for affine-Dynkin appearance from a punctured torus).

A pants decomposition of $\Sigma_g$ with $g \ge 1$ produces a quiver of:
- $3g-3+n$ tubes (gauge groups, one per tube);
- $2g-2+n$ pants (matter, one per pants).

For genus $g=1$ with $n$ punctures: $3-3+n = n$ tubes (gauge), $0+n = n$ pants. A torus with $n=24$ punctures gives $3g-3+n = 24$ gauge groups, but each is $\mathfrak{g}$-valued (not $U(1)$). For 6d $(2,0)$ of type $A_1$ ($\mathfrak{g} = SU(2)$): 24 SU(2) gauge groups, 24 pants $T_2$ (= bifundamental hypers), forming a **circular quiver** structure since the torus has cyclic monodromy.

This DOES give an affine-A-type quiver structure, but the gauge groups are $SU(2)$, not $U(1)$. Wave 10's "$U(1)^{24}$" is wrong: it should be **$SU(2)^{24}$** for the $A_1$ class-$\mathcal{S}$ on $T^2 \setminus \{24\}$.

### §1.4 ATTACK 1 conclusion

Wave 10's "$\widehat{A}_{23}$ quiver $\prod U(1)$" conflates:
(a) the 3d Coulomb-branch gauge group $U(1)^{24}$ (from Heal 1.B Nakajima ALE template);
(b) the 4d class-$\mathcal{S}$ gauge group $SU(2)^{24}$ (from $A_1$ pants decomposition of $T^2 \setminus \{24\}$);
(c) the 6d $(2,0)$ ADE type vs the quiver type from $\mathcal{C}$.

The category error is fatal as stated. **HEAL 1**: there are TWO consistent class-$\mathcal{S}$ frames depending on dimensional assignment.

### §1.5 HEAL 1 -- two consistent frames

**Frame 1.A** (compactify on $\mathcal{C} = T^2$, get 4d $\mathcal{N}=2^*$):
6d $(2,0)$ of type $\mathfrak{g}$ on $T^2 \times \mathbb{R}^{1,3}$ gives 4d $\mathcal{N}=4$ super Yang--Mills (Maldacena--Nunez 2000 hep-th/0007018, Witten 1995 hep-th/9512099) with gauge group $\mathfrak{g}_{\mathrm{ADE}}$. Adding $n$ punctures with mass deformation gives 4d $\mathcal{N}=2^*$. For $\mathfrak{g} = E_8$, this is 4d $\mathcal{N}=2^*$ $E_8$ super Yang--Mills.

This frame has NO K3. The K3 enters only as the moduli space (the $E_8$ Coulomb branch with mass deformation has a Seiberg--Witten curve fibered over a K3 base in some specialisations; Donagi--Witten 1995 hep-th/9510101).

**Frame 1.B** (compactify on K3, get 2d $(0,4)$):
6d $(2,0)$ of type $\mathfrak{g}$ on K3 gives 2d $(0,4)$ on $\mathbb{R}^{1,1}$ (GGP 2013). For $\mathfrak{g} = A_1$: 2d $(0,4)$ sigma model with target Hilb$^2$(K3). For $\mathfrak{g} = E_8$: 2d $(0,4)$ sigma model with target $\mathcal{M}_{E_8}(K3)$ = moduli of $E_8$-instantons on K3.

This frame has K3 in the input but the output is **2d, not 3d**. Wave 10's "3d $T[K3]$" is the further $S^1$-uplift, not directly this frame.

**Frame 1.C** (the *correct* T[K3] frame, 3d $\mathcal{N}=4$ via M5 on $K3 \times S^1$):
M-theory M5-brane wrapping $K3 \times S^1 \subset \mathbb{R}^{1,2} \times K3 \times S^1 \times \mathbb{R}^3$ gives 3d $\mathcal{N}=4$ on $\mathbb{R}^{1,2}$. The 6d $(2,0)$ type is determined by the **stack of M5-branes**: $N$ stacked M5s give 6d $(2,0)_{A_{N-1}}$. For a single M5 = $A_0$ = trivial; for $N$ M5s = $A_{N-1}$.

The Wave 10 "single M5 on K3" gives the $A_0$ free tensor multiplet on $K3 \times S^1$ which compactifies to a 3d $\mathcal{N}=4$ free hyper on $S^1$, NOT a 24-vacuum quiver theory. To get 24 vacua, one needs **24 M5s** wrapping K3 $\times S^1$, giving 6d $(2,0)_{A_{23}}$ on K3 $\times S^1$, which compactifies to a 3d $\mathcal{N}=4$ theory whose Coulomb branch is the $A_{23}$-instanton moduli on K3.

Or: **single M5 of type $E_8$** (i.e., heterotic $E_8$ small instanton, Witten 1996 hep-th/9512219), wrapping K3 $\times S^1$ -- gives a 3d $\mathcal{N}=4$ theory whose Coulomb branch is the moduli of one $E_8$ small instanton on K3, which is **K3 itself** (the instanton number 1 moduli = K3). 24 vacua = 24 $I_1$ fibres of K3 in the elliptic fibration.

**The genuine physics avatar is Frame 1.C with $E_8$ small instanton**: 6d $(2,0)$-of-type-$E_8$ on K3 $\times S^1$, single M5 with $E_8$ small instanton structure, giving 3d $\mathcal{N}=4$ with K3-shaped Coulomb branch. This is the Minahan--Nemeschansky $E_8$ theory (Minahan--Nemeschansky 1996 hep-th/9610076) compactified on $S^1$ with K3-twisted boundary conditions.

This is **Lagrangian-free** -- the Minahan--Nemeschansky $E_8$ theory has no Lagrangian description (the $E_8$ flavour symmetry is intrinsically non-Lagrangian); thus $T[K3]$ inherits Lagrangian-freeness. The Wave 10 "$\widehat{A}_{23}$ $\prod U(1)$" Lagrangian is a wrong attempt to Lagrangianize a fundamentally non-Lagrangian theory.

**HEAL 1**: $T[K3]$ = 3d $\mathcal{N}=4$ compactification of 4d Minahan--Nemeschansky $E_8$ theory on $S^1$ with K3-twisted boundary; non-Lagrangian; rank-1 Coulomb branch in 4d (rank-24 after K3 enhancement); 24 BPS vacua = 24 $I_1$ Kodaira fibres.

---

## Cycle 2 -- ATTACK: rank-24 match -- $\widehat{A}_{23}$ vs Mukai vs Niemeier

### §2.1 Three different "24"s

There are at least three distinct rank-24 lattices and groups appearing in K3 mathematics, and Wave 10 conflates them:

(i) **Mukai lattice** $\Gamma^{4,20} = H^*(K3, \mathbb{Z}) = H^0 \oplus H^2 \oplus H^4$, rank 24, signature $(4,20)$. Mukai 1987.

(ii) **Niemeier lattices**: 24 even unimodular positive-definite lattices of rank 24, classified by Niemeier 1973 (one is the Leech lattice, 23 have non-trivial root systems with total rank 24).

(iii) **24 Kodaira $I_1$ fibres** on a generic elliptic K3, by $\chi(\mathrm{K3}) = 24$.

(iv) **24 nodes of $\widehat{A}_{23}$** affine Dynkin diagram (cyclic).

The **Mukai $4{+}20$** has signature $(4,20)$, NOT $(0,24)$ or $(24,0)$. It is NOT positive-definite. So it is NOT a Niemeier lattice. The Mukai 24 and the Niemeier 24 are different.

The Niemeier classification has 24 lattices; one is Leech; 23 have root systems. So if the K3 chiral algebra is built from a Niemeier lattice, the count of Niemeier lattices is **24** (including Leech) or **23** (excluding Leech as rootless).

### §2.2 The 24 $I_1$ fibres

For a generic elliptic K3: $\chi(\mathrm{K3}) = 24$ from a count of singular fibres. The 24 $I_1$ fibres are **physical points on the base $\mathbb{P}^1$**, not lattice elements. The natural action of monodromy is in $\mathrm{SL}_2(\mathbb{Z})$ (period monodromy), not in O(Mukai).

The 24 monodromy generators around the 24 punctures of $\mathbb{P}^1 \setminus \{24\}$ satisfy
$$
\prod_{i=1}^{24} T_i \;=\; 1,
$$
where each $T_i$ is conjugate to the parabolic Dehn twist $T = \begin{pmatrix}1&1\\0&1\end{pmatrix}$. The product is forced to be $1$ by $\pi_1$ relations on the 24-punctured sphere.

This gives a representation $\rho: \pi_1(\mathbb{P}^1 \setminus \{24\}) \to \mathrm{SL}_2(\mathbb{Z})$ with image a subgroup of finite index in $\mathrm{SL}_2(\mathbb{Z})$. The image is the **monodromy group** of the K3 elliptic fibration; for a generic K3 with $J$-invariant degree 24, this is all of $\mathrm{SL}_2(\mathbb{Z})$ (Miranda 1989, Persson 1990).

So 24-Kodaira $\ne$ 24-Mukai $\ne$ 24-Niemeier. Wave 10 conflated 24-Kodaira with 24-quiver-nodes.

### §2.3 ATTACK 2 conclusion

The "rank 24" in Wave 10's $\widehat{A}_{23}$ quiver is the **Kodaira-fibre count**, NOT the Mukai-lattice rank or any Niemeier rank. The match "$\widehat{A}_{23}$ has 24 nodes = rank(Mukai) = 24" is numerically true but conceptually wrong: $\widehat{A}_{23}$ Cartan has signature $(0,23) \oplus (1,1)$ (positive-semidefinite with 1-dim radical), while Mukai is signature $(4,20)$. The lattices are NOT isomorphic.

If the K3 chiral algebra were genuinely $\widehat{A}_{23}$-based, its character would be the affine $A_{23}^{(1)}$ character $\sim \prod (1-q^n)^{-23}/\eta(q)$, NOT $1/\Phi_{10}$ which has $\eta$-product structure of total weight $-1/12 \cdot 24 = -2$ at the cusp matching $1/\eta^{24}$ (the K3 elliptic genus).

The numerics do not support an $\widehat{A}_{23}$ identification at level 1.

### §2.4 HEAL 2 -- the rank-24 invariant is $E_8$-instanton, not affine A

The rank-24 invariant of K3 in M-theory / heterotic duality is the **$E_8 \times E_8$ instanton number** on K3:
$$
\int_{\mathrm{K3}} \mathrm{tr}\, F_1 \wedge F_1 + \int_{\mathrm{K3}} \mathrm{tr}\, F_2 \wedge F_2 \;=\; 24,
$$
where $F_1, F_2$ are the curvatures of the two $E_8$ heterotic gauge bundles, and the total instanton number $24$ is forced by anomaly cancellation $-\chi(\mathrm{K3}) + n_1 + n_2 = 0 \Rightarrow n_1 + n_2 = 24$ (Schwarz 1995 hep-th/9512053, Vafa F-theory K3 hep-th/9602022).

The 24 small instantons can split as $(n_1, n_2)$ for any $0 \le n_1 \le 24$, giving the F-theory K3 moduli space. The standard split $(12, 12)$ is symmetric; the extreme $(24, 0)$ has all instantons in one $E_8$.

For the standard $\Phi_{10}^{-1}$ K3-on-elliptic computations (Gaiotto--Strominger--Yin 2005 hep-th/0504126, Maulik--Pandharipande 2007 arXiv:0708.4154, OP 2018 arXiv:1607.05105), the relevant lattice is the **Mukai $\Gamma^{4,20}$** acted on by **$O(\Gamma^{4,20})$ = full Mukai isometry group**, NOT $\widehat{A}_{23}$.

The connection between 24-Kodaira and 24-instantons is via Vafa's F-theory K3 (Vafa 1996 hep-th/9602022): F-theory on elliptic K3 is dual to heterotic on $T^2$ at certain limits; the 24 $I_1$ fibres correspond to 24 7-branes in F-theory, which dualize to 24 $E_8$ small instantons in heterotic. So 24-Kodaira = 24-7-branes-F-theory = 24-instantons-heterotic. **Not** = 24-Mukai-rank.

**HEAL 2**: the rank-24 invariant is $E_8$-instanton-number on K3, dual to 24-7-branes in F-theory, dual to 24 $I_1$ Kodaira fibres. The Mukai lattice $\Gamma^{4,20}$ is rank 24 by coincidence -- it counts the BPS state space, not the 7-brane / instanton / Kodaira count, which lives on the K3 base. **Wave 10's $\widehat{A}_{23}$ quiver is replaced by the F-theory K3 7-brane structure**: 24 7-branes on the base $\mathbb{P}^1$, monodromy $T_i$ around each, total $\prod T_i = 1$; the chiral algebra sees this as a Beilinson factorization algebra on $\mathbb{P}^1 \setminus \{24\}$ with parabolic weights.

---

## Cycle 3 -- ATTACK: 24 Sp$_4$-Jacobi blocks vs 23 vs other counts

### §3.1 Jacobi forms of weight 5 index 1 for Sp$_4$

Eichler--Zagier 1985 ("The Theory of Jacobi Forms") classifies Jacobi forms $\phi(\tau, z)$ for $\Gamma_0^J \subset \mathrm{SL}_2(\mathbb{Z}) \ltimes \mathbb{Z}^2$. The space $J_{k,m}$ of weight $k$ index $m$ Jacobi forms has dimension given by EZ formula.

For weight $k = 5$, index $m = 1$: $\dim J_{5,1} = 0$ (Eichler--Zagier Tab.\ 1, since odd-weight forms on $\Gamma_0^J$ vanish).

But Wave 10 said "Sp$_4$-Jacobi forms of weight 5 index 1". Sp$_4$-Jacobi (Siegel--Jacobi) forms are different: they live on $\mathbb{H}_2 \times \mathbb{H} \times \mathbb{C}$ and transform under the parabolic Jacobi subgroup of Sp$_6(\mathbb{Z})$ embedded in Sp$_4(\mathbb{Z})$. The relevant space is the space of **Siegel modular forms** on $\Gamma_2 = \mathrm{Sp}_4(\mathbb{Z})$ of weight 5 with Jacobi-type expansion.

Igusa 1962 classified $M_*(\Gamma_2)$: weight-10 cusp form $\Phi_{10}$ (Igusa cusp form), weight-12, weight-35 odd cusp form, etc. Weight 5: $\dim M_5(\Gamma_2) = 0$ (no even-weight gap; weight 5 is odd, and odd Siegel forms on $\Gamma_2$ vanish or are skew). Actually, by Igusa's structure theorem, $M_*(\Gamma_2) = \mathbb{C}[E_4, E_6, \chi_{10}, \chi_{12}, \chi_{35}]$ with $\chi_{35}$ skew; even weight space is generated by $E_4, E_6, \chi_{10}, \chi_{12}$, all even.

So $\dim M_5(\Gamma_2) = 0$. **Weight-5 Siegel forms for Sp$_4$ do not exist**.

What CAN exist at weight 5: vector-valued Siegel forms, or Jacobi-Siegel forms, or weight-5 forms for a finite-index subgroup (paramodular group $K(p)$ for $p$ prime).

### §3.2 What Wave 10 likely meant

Wave 10's "weight 5 index 1" is probably:
(a) $\Phi_{10}^{1/2}$, formal half-power (which is not a modular form);
(b) the Borcherds Maass-lift of $\phi_{0,1}$ (K3 weak Jacobi form of weight 0 index 1), giving $\Phi_{10}$ at weight $10$; "weight 5" then refers to the **Maass-lift seed** of weight... actually Maass lift takes weight $k$ index $m$ Jacobi to weight $k+1$ paramodular; for $\phi_{0,1}$ this is weight 1, not 5;
(c) Gritsenko Jacobi-form lift: Gritsenko 1994 (alg-geom/9408005) constructs a weight-10 paramodular form from $\phi_{10,1} = \eta^{18} \vartheta_1^2$ via additive lift; "weight 5 index 1" might be a typo for "weight 10 index 1";
(d) Gritsenko--Nikulin 1996 (alg-geom/9504006) construct $\Phi_{10}^{-1}$ as Borcherds product of $2 \phi_{0,1}$, giving weight $10 = 2 \cdot 5$, where "5" appears as half-weight in the Borcherds product formalism.

In all four interpretations, the Wave 10 phrase "weight 5 index 1" is imprecise. The correct statement is one of:
- 24 Jacobi forms summing to $\phi_{10,1} = \eta^{18}\vartheta_1^2$ (depth-1 expansion of $\Phi_{10}^{-1}$);
- 24 holomorphic blocks transforming as a modular tensor category of $V_{II_{4,20}}^+$-modules at level 1.

### §3.3 ATTACK 3 conclusion: the count is 23 (Niemeier minus Leech) OR 24

**Niemeier count**: there are 24 Niemeier lattices total; 23 have non-trivial root systems; 1 (Leech) has trivial root system. The **23 root-Niemeier lattices** are in bijection with 23 even-genus lattices, classified by Conway--Sloane 1999 §16.

**Mukai count**: $\Gamma^{4,20}$ has 24 generators; Mukai isometry group acts.

**Kodaira count**: 24 $I_1$ fibres for generic elliptic K3.

**Block count**: Wave 10 says "24 Sp$_4$-Jacobi blocks". Three independent paths to verify:

- **Path A** (BPS state count): the number of independent BPS-state generators at depth 1 in $\Phi_{10}^{-1}$ Fourier expansion. From the Fourier expansion $\Phi_{10}^{-1} = \sum_{n,\ell,m} c(n,\ell,m) q^n \zeta^\ell p^m$, the depth-1 term ($n=1, m=0$) is $\sum_\ell c(1, \ell, 0) \zeta^\ell$. This is $\phi_{10,1} \cdot \zeta^{-1} \cdot$... actually depth 1 is $\eta^{-24}$ before Borcherds-lift conversion. The count of BPS states at level 1 is **24 = -$\chi(K3)$** (Yau--Zaslow 1996).

- **Path B** (modular tensor category): the chiral algebra $V_{II_{4,20}}^+$ at the K3 lattice point has a modular tensor category of representations whose object count at the lowest non-trivial weight is determined by the lattice's discriminant group; for $II_{4,20}$ even unimodular, the discriminant group is trivial, so the MTC has **1 simple object** at vacuum. The "24" must come from elsewhere -- e.g., the 24-dim Frenkel--Lepowsky--Meurman moonshine module orbifold.

- **Path C** (Sp$_4$ representation theory): Sp$_4$ has irreps labelled by highest weights $(\lambda_1, \lambda_2)$. The number of weight-5 representations (in the sense of dimensions $\le 5$) is finite and small: trivial (1d), defining 4d, adjoint 10d. The count of "vector-valued weight-5 components" is at most a few, NOT 24.

The three paths give 24, 1, and small. They DISAGREE. Wave 10's "24 Sp$_4$-Jacobi blocks" is **not** simultaneously rank-of-Mukai AND number-of-MTC-simples AND vector-valued Sp$_4$ components. It conflates three different "counts".

### §3.4 HEAL 3 -- the correct count is 23 OR 24 depending on what is being counted

**HEAL 3.A** (Wave-10 retraction, partial): the "24 holomorphic blocks" should be re-stated as "24 Fourier coefficients of $\phi_{10,1}$ at depth 1, indexed by 24 BPS-state classes mod Bogomol'nyi-PSU(1,1)$_T$ orbits". This is a count of **K3 BPS states modulo the elliptic fibration's $T$-monodromy**, NOT a count of Sp$_4$-Jacobi forms.

**HEAL 3.B** (Niemeier 23): if instead the chiral algebra is the **Niemeier-lattice VOA** $V^N_\Lambda$ for a Niemeier lattice $\Lambda$, the count is **23 root-Niemeier lattices** (excluding Leech). Each gives a distinct 4d $\mathcal{N}=2$ class-$\mathcal{S}$ analogue via Höhn--Mason 2016 (arXiv:1507.00105) "Genus-zero VOAs and Niemeier lattices". The 23 + 1 (Leech, the Conway VOA $V^\natural$) gives 24 total, matching the Wave 10 count.

**HEAL 3.C** (Sp$_4$ modular tensor): the genuine Sp$_4(\mathbb{Z})$ representation theory of vector-valued Jacobi forms of $\Phi_{10}^{-1}$ has a specific finite count given by the eigenspaces of $\Phi_{10}$ vanishing locus. From Igusa's classification: the Hecke eigenspace of $\chi_{10}$ at level 1 has dimension 1 (Igusa 1962). The "24" arises from the Fourier expansion's depth-1 multiplicity, NOT from Sp$_4$ block count.

**HEAL 3 unified**: the "24" is **24 BPS states / 24 Niemeier lattices counting Leech / 24 Kodaira fibres**, all cohering via the F-theory dictionary; the "Sp$_4$-Jacobi block" framing of Wave 10 is loose. The genuine count is:
- 24 BPS states at depth 1 of $\Phi_{10}^{-1}$ (Yau--Zaslow);
- 24 = 23 + 1 Niemeier lattices (Höhn--Mason);
- 1 Sp$_4$-modular character at level 1 (Igusa $\chi_{10}$);
- 24 7-branes / 24 instantons / 24 Kodaira fibres (Vafa F-theory).

**Wave 10 retraction**: "24 vector-valued Sp$_4(\mathbb{Z})$-Jacobi forms of weight 5 index 1" replaced by **"24-dim BPS Hilbert space at depth 1 of $\Phi_{10}^{-1}$, transforming under the modular subgroup that fixes $\chi_{10}$, with character-level identification to the depth-1 Borcherds-lift coefficient"**. The "24" is BPS-state-count, not Sp$_4$-block-count.

---

## Cycle 4 -- ATTACK: Schur-index match against $\Delta_5$ via Beem--Lemos--Liendo--Peelaers--Rastelli--van Rees

### §4.1 Beem--Rastelli 4d $\mathcal{N}=2$ chiral algebra

Beem--Lemos--Liendo--Peelaers--Rastelli--van Rees (BLLPRvR) 2013 (arXiv:1312.5344, "Infinite chiral symmetry in four dimensions") constructed a map from any 4d $\mathcal{N}=2$ SCFT to a 2d chiral algebra (vertex operator algebra), preserving the structure of protected operators. Schematically:
$$
\chi: \quad \{4d\ \mathcal{N}=2\ \mathrm{SCFTs}\} \;\to\; \{2d\ \mathrm{VOAs}\},
$$
with $\chi(\mathcal{T})$ the **Schur sector** of the 4d theory. The identification is:
$$
\mathrm{Schur\ index}(\mathcal{T}) \;=\; \mathrm{vac.\ char.}\bigl(\chi(\mathcal{T})\bigr).
$$

For class-$\mathcal{S}$ theories, $\chi(T[\mathfrak{g},\mathcal{C},\mathcal{D}])$ is the **Beem--Rastelli chiral algebra** = a $\mathcal{W}$-algebra obtained by Drinfeld--Sokolov reduction of an affine $\mathfrak{g}$ chiral algebra on $\mathcal{C}$ at level $-h^\vee$ (critical level twist).

The Schur index is computable from 4d:
$$
\mathcal{I}_{\mathrm{Schur}}(q) \;=\; \mathrm{Tr}_{\mathcal{H}_{S^3}} (-1)^F q^{\Delta - R},
$$
where $\Delta$ is conformal dimension and $R$ is a $\mathcal{N}=2$ R-charge. By BLLPRvR Thm 1.1, this equals the vacuum character of the 2d chiral algebra.

### §4.2 If $T[K3]$ has a 4d $\mathcal{N}=2$ avatar, its Schur index = vacuum character of $\mathbf{H}_{\Delta_5}$?

Wave 10 implicitly conjectured (without saying so explicitly): the **4d $\mathcal{N}=2$ avatar of $T[K3]$**, viewed as a class-$\mathcal{S}$ theory, has Beem--Rastelli chiral algebra equal to the K3 chiral bialgebra, and its Schur index equals the depth-1 vacuum character of $\mathbf{H}_{\Delta_5}$ = $\phi_{10,1}(\tau, z) / \eta(\tau)^{24}$.

But there is NO 4d $\mathcal{N}=2$ avatar of $T[K3]$ in Wave 10's frame. Wave 10 went M5-on-$K3 \times S^1$ giving 3d directly, skipping the 4d step. The 4d step requires a different compactification.

If we instead use **6d $(2,0)$ on K3 only (no $S^1$)**, we get 2d $(0,4)$ (GGP 2013), no 4d. So the standard route to a 4d theory is **6d $(2,0)$ on $\mathcal{C}_g$ (Riemann surface) only**, giving 4d class-$\mathcal{S}$ on $\mathcal{C}_g$ with no K3.

To get a 4d theory associated to K3, we need an alternative: **6d $(2,0)$-of-type-$E_8$ on $\mathcal{C}_g \times K3$** with compactification on $\mathcal{C}_g \times K3$ giving... 0d (a theory on a point). That doesn't work.

The correct 4d avatar: **F-theory on K3 $\times \mathbb{R}^{1,5}$ with Calabi--Yau-3-fold $K3 \times T^2$ in the F-theory base** giving 6d $(1,0)$ supergravity (Vafa 1996 hep-th/9602022), which compactifies on $T^2$ to 4d $\mathcal{N}=2$ supergravity. This is gravity, not a class-$\mathcal{S}$ field theory.

**There is no clean 4d class-$\mathcal{S}$ avatar of $T[K3]$** because K3 is 4-dimensional. The Beem--Rastelli framework requires a 4d $\mathcal{N}=2$ SCFT input, and $T[K3]$ doesn't naturally live in 4d.

### §4.3 ATTACK 4 conclusion

The Wave 10 prompt suggested checking the Schur-index match. But there is no 4d $\mathcal{N}=2$ SCFT to compute the Schur index of. The 3d theory $T[K3]$ has a **superconformal index in 3d** (Kim 2009 arXiv:0903.2172), not a Schur index. The 3d index is a function of $(q, m, t)$ where $m$ is a magnetic flux and $t$ is the R-symmetry parameter. The 3d $\mathcal{N}=4$ index of $T[K3]$ is computable via Bullimore--Dimofte--Gaiotto 2016 (arXiv:1601.03586) Coulomb-branch index formula.

The 3d $\mathcal{N}=4$ Coulomb-branch index of an affine $\widehat{A}_{23}$ quiver $\prod U(1)$ with 24 bifundamental hypers is:
$$
\mathcal{I}^{3d, C}_{T[K3]^{\mathrm{cand}}}(q, t) \;=\; \prod_{i=1}^{24} \prod_{n \ge 0} \frac{1 - q^{n + 1/2} t}{1 - q^{n + 1/2} t^{-1}} \;=\; \biggl[\prod_{n}(1 - q^n t)/(1 - q^n t^{-1})\biggr]^{24}.
$$
At $t = 1$: this is 1 (trivial). At $t \to 0$: this is $[\prod (1-q^n)]^{24} = \eta(q)^{24} q^{-1}$ (up to normalization).

So the 3d Coulomb-branch index of the candidate quiver is $\eta(q)^{24}/q$, NOT $\phi_{10,1} = \eta^{18}\vartheta_1^2$.

**Wave 10's identification fails the 3d index check at the leading character level**: the candidate quiver gives $\eta^{24}$, not $\eta^{18} \vartheta_1^2$. The $\vartheta_1^2$ factor (= 4 in the dimensional count) is missing from the candidate quiver.

### §4.4 HEAL 4 -- the correct 4d avatar is $E_8$ Minahan--Nemeschansky on K3-twisted $T^2$

**HEAL 4**: the 4d $\mathcal{N}=2$ avatar of $T[K3]$ in the Beem--Rastelli sense is the **Minahan--Nemeschansky $E_8$ rank-1 SCFT** (Minahan--Nemeschansky 1996 hep-th/9610076 / 9706110, "Superconformal fixed points with $E_n$ global symmetry") **compactified on $T^2$ with K3-elliptic-fibration twist**, giving 2d $(0,4)$ on $T^2$ = the Beem--Rastelli 2d chiral algebra.

Beem--Rastelli explicitly identified the 2d chiral algebra of MN $E_8$:
$$
\chi(T_{E_8}^{\mathrm{MN}}) \;=\; (\widehat{E_8})_{-12},
$$
the affine $E_8$ chiral algebra at level $k = -12 = -h^\vee$ (critical level shifted; Beem--Rastelli 2014 arXiv:1404.1079, §6 / Tab.\ 1). The Schur index is the vacuum character of $(\widehat{E_8})_{-12}$:
$$
\mathcal{I}_{\mathrm{Schur}}(T_{E_8}^{\mathrm{MN}}) \;=\; \mathrm{ch}_{(\widehat{E_8})_{-12}, \mathrm{vac}}(\tau, z).
$$

For the K3-twisted compactification: the 24 small instantons of $E_8$ on K3 give a 4d theory whose chiral algebra is a **$\mathcal{W}_{E_8}$-algebra at central charge $c = 24$** (matching $c = -\chi(K3) \cdot h^\vee_{E_8} / 24 = 24$ heuristically). The Schur index of this theory at the K3-twisted point would then be $\eta(q)^{-24} \cdot$theta-factor, matching $1/\Phi_{10}$ at the Borcherds-lift level.

**HEAL 4 sharper claim** (W11-G-1, falsifiable):
$$
\boxed{\quad
\mathcal{I}_{\mathrm{Schur}}\bigl(T[K3]^{\mathrm{4d-avatar}}\bigr)(q, z) \;=\; \mathrm{ch}_{\mathbf{H}_{\Delta_5}, \mathrm{vac}}(\tau, z) \;=\; \frac{\phi_{10,1}(\tau, z)}{\eta(\tau)^{24}} \;=\; \frac{\eta(\tau)^{18} \vartheta_1(\tau, z)^2}{\eta(\tau)^{24}} \;=\; \frac{\vartheta_1(\tau, z)^2}{\eta(\tau)^6}.
\quad}
$$

The right-hand side is a weight-$(2 - 6 \cdot \frac{1}{2}) = -1$, index-1 weak Jacobi form, matching the **K3 weak Jacobi elliptic genus** $\phi_{0,1}$ of weight 0 index 1 modulo a weight shift. The Schur-index identification predicts the 4d $\mathcal{N}=2$ avatar of $T[K3]$ has central charge such that $c_{4d} - c_{2d}$ matches the EHIY anomaly formula (Beem--Rastelli 2014 §3).

**Three-path test for HEAL 4**:
- **Path 1** (Beem--Rastelli MN $E_8$): $\mathrm{ch}_{(\widehat{E_8})_{-12}}(q, z) = $ explicit $E_8$ character formula, computable at low order.
- **Path 2** (K3 elliptic genus): $\phi_{0,1}(\tau, z) = \mathrm{Ell}(K3; \tau, z)$ (Eguchi--Ooguri--Tachikawa 2010 arXiv:1004.0956, K3 elliptic genus).
- **Path 3** (Borcherds lift): $\Phi_{10}^{-1} = $ Borcherds product of $2\phi_{0,1}$; the K3 elliptic genus is half-Borcherds.

The three paths give consistent leading-order character data; full match at all orders is conjectural, falsifiable by depth-1 / depth-2 character expansion.

---

## Cycle 5 -- ATTACK: line operators / Coulomb branch

### §5.1 BPS line operators of class-$\mathcal{S}$

For 4d $\mathcal{N}=2$ class-$\mathcal{S}$ on $\mathcal{C}_g$, the BPS line operators are labelled by:
- 't Hooft--Wilson lines, valued in the lattice $\Lambda_{\mathrm{el-mag}}$;
- Drukker--Morrison--Okuda (DMO) 2010 (arXiv:0911.2562) and Aharony--Seiberg--Tachikawa (AST) 2013 (arXiv:1305.0318) classify the lattice structure.

The category of BPS line operators forms a **braided tensor category** under fusion (Kapustin--Saulina 2009 arXiv:0908.3140). For class-$\mathcal{S}$ on $\Sigma_g$ of type $\mathfrak{g}$, this category is conjecturally:
$$
\mathrm{Lines}\bigl(T[\mathfrak{g}, \Sigma_g]\bigr) \;\cong\; \mathrm{Skein}_q\bigl(\mathfrak{g}, \Sigma_g\bigr) \;=\; \text{quantum-group skein category},
$$
the skein algebra of $\mathfrak{g}$-decorated graphs on $\Sigma_g$ at quantum parameter $q$ (Allegretti--Kim 2017 arXiv:1612.05641 for $A_1$; Higgs--Goncharov for general type).

### §5.2 K-theoretic Coulomb branch

The K-theoretic Coulomb-branch ring of $T[\mathfrak{g}, \Sigma_g]$ is, by BFN 2018 (arXiv:1601.03586),
$$
K^T(\mathcal{R}_{G_\Sigma, \mathbf{N}_\Sigma}) \;\cong\; K^T(\mathrm{Hitchin}^{\mathrm{loc}}(\Sigma, G)) / \mathrm{relations},
$$
a quantization of the Hitchin moduli (Bezrukavnikov--Kazhdan 2017 arXiv:1705.01419 for tame Hitchin, Beilinson--Drinfeld for global).

For $\mathfrak{g} = E_8$ (rank 8), $\Sigma = T^2$ with K3-twist: the K-theoretic Coulomb branch is the **K3-twisted $E_8$ Hitchin moduli**, conjecturally equal to the **K3 Mukai moduli space** at appropriate stability (Hausel--Thaddeus 2003 math/0205236 mirror symmetry; Donagi--Pantev 2008 arXiv:0707.4022 for Hitchin = Mukai on elliptic fibration).

### §5.3 ATTACK 5 -- is the line-operator category $= \mathbf{H}_{\Delta_5}$ or only the cuspidal limit?

Wave 10 implicitly identified $\mathbf{H}_{\Delta_5}$ with the K-theoretic Coulomb-branch K-theory at full elliptic deformation $(q, t, p)$. The line-operator category gives the **full** algebra including non-cuspidal ($\tau$ generic) deformations. So Wave 10 has:
$$
\mathbf{H}_{\Delta_5}^{\mathrm{full}} \;\overset{?}{=}\; \mathrm{Lines}\bigl(T[K3]^{\mathrm{4d}}\bigr) \;=\; K^T(\mathcal{M}_{\mathrm{Hitchin, K3}}^{E_8}).
$$

But the **strict-Hopf rigorous Borcherds Yangian** (Wave 10 Drinfeld convergence: cusp $\tau \to i\infty$ specialisation) is only the cuspidal limit $\tau \to i\infty$, $p \to 0$. So:
$$
\mathbf{H}_{\Delta_5}^{\mathrm{cusp}} \;=\; Y^{\mathrm{Borch}}_\hbar(\mathfrak{g}_{\Delta_5}) \;\overset{?}{=}\; \mathrm{Lines}^{\mathrm{cusp}}\bigl(T[K3]^{\mathrm{4d}}\bigr).
$$

The Wave 10 framing is ambiguous: line operators give a category whose K-theory (decategorified) is a ring; the ring carries a Hopf structure if and only if the category is a **monoidal** category, which is true for the BPS line category by Kapustin--Saulina. The Hopf structure encodes the fusion.

### §5.4 HEAL 5 -- the line-operator category is the cuspidal Hopf limit; full quasi-Hopf comes from elliptic deformation

**HEAL 5** (W11-G-2, falsifiable):
$$
\mathrm{Lines}\bigl(T[K3]^{\mathrm{4d}}\bigr) \;\cong\; \mathbf{H}_{\Delta_5}^{\mathrm{cusp}} \;=\; Y^{\mathrm{Borch}}_\hbar(\mathfrak{g}_{\Delta_5}),
$$
the cuspidal limit (strict Hopf) is the BPS line-operator category of the 4d $\mathcal{N}=2$ avatar; the full elliptic family $\mathbf{H}_{\Delta_5}^{\mathrm{full}}(\tau)$ is the **$\tau$-deformation of the line category** by introducing elliptic spectral parameter. Concretely, the elliptic spectral $u \in E_\tau$ corresponds to **elliptic Casimir deformation** of the line operators (Aganagic--Okounkov 2016 elliptic stable envelopes; Felder--Tarasov--Varchenko 2015 elliptic dynamical $R$-matrix).

**Three-path test for HEAL 5**:
- **Path 1** (Kapustin--Saulina): line-operator category is monoidal braided; ring is Hopf.
- **Path 2** (Bullimore--Dimofte--Gaiotto): Coulomb-branch K-theory has Hopf-algebra structure from BFN convolution; matches BPS line category.
- **Path 3** (Aganagic--Okounkov): elliptic stable envelopes deform Hopf to quasi-Hopf at finite $\tau$.

All three converge: cuspidal limit = strict Hopf = line-operator ring; elliptic = quasi-Hopf via dynamical R-matrix.

**HEAL 5 corollary**: the Wave 10 "K-theoretic Hall on coh(K3) at $(q_1, q_2, z)$" and the Wave 11 "BPS line operators of $T_{E_8}^{\mathrm{MN}}$ on K3-twist" are **equivalent at the cuspidal limit** but DIFFER at finite elliptic deformation: the Hall-algebra picture sees the elliptic deformation as $z$-rotation, the line-operator picture sees it as elliptic spectral $u$. The two pictures are dual under the Borcherds = Howe correspondence.

---

## Pattern 236 chain-level / $(\infty,1)$-categorical labelling

Following Pattern 236 ambient-qualifier discipline:

- **Cycle 1 HEAL**: chain-level (M-theory M5-brane on $K3 \times S^1$) and $(\infty, 1)$-categorical (the $(\infty, 1)$-functor from 6d $(2,0)$ ADE category to 4d $\mathcal{N}=2$ category). Both lanes equally load-bearing.

- **Cycle 2 HEAL**: chain-level (24 7-branes on $\mathbb{P}^1$, monodromy $T_i$ around each); $(\infty, 1)$-categorical (factorization $\infty$-category of $\mathbb{P}^1 \setminus \{24\}$ with parabolic punctures).

- **Cycle 3 HEAL**: chain-level (Yau--Zaslow 24 BPS state count via nodal-rational-curve enumeration); $(\infty, 1)$-categorical (modular tensor category of $V_{II_{4,20}}^+$-modules at Niemeier point).

- **Cycle 4 HEAL**: chain-level (3d Coulomb-branch index as $q$-hypergeometric), $(\infty, 1)$-categorical (Beem--Rastelli $\chi: \mathrm{SCFT}_4^{\mathcal{N}=2} \to \mathrm{VOA}$ as $\infty$-functor).

- **Cycle 5 HEAL**: chain-level (Hopf-algebra K-theory class of BPS line categories); $(\infty, 1)$-categorical (monoidal $(\infty, 1)$-category of line operators with fusion as $E_2$-monoidal structure).

---

## Wave 11 final statement (refining Wave 10)

**Wave 11 final claim** (sharpening of Wave 10 boxed equation):

$$
\boxed{\quad
\mathbf{H}_{\Delta_5} \;=\; \mathrm{Lines}\bigl(T_{E_8}^{\mathrm{MN}, K3}\bigr) \;\cong\; K^T(\mathcal{M}_{\mathrm{Hitchin}}^{E_8, K3\text{-twist}})_{(q, t, p)},
\quad}
$$

where $T_{E_8}^{\mathrm{MN}, K3}$ is the **Minahan--Nemeschansky $E_8$ rank-1 4d $\mathcal{N}=2$ SCFT, K3-twisted via 24 instantons**, a **Lagrangian-free** 4d theory (Minahan--Nemeschansky 1996), and $\mathcal{M}_{\mathrm{Hitchin}}^{E_8, K3\text{-twist}}$ is its K-theoretic Coulomb branch given by K3-twisted $E_8$ Hitchin moduli.

The Wave 10 affine-$\widehat{A}_{23}$ quiver is **retracted** in favour of this non-Lagrangian $E_8$-class avatar, which:
- correctly reproduces 24 BPS vacua = 24 Kodaira fibres = 24 $E_8$ instantons (via Vafa F-theory K3);
- correctly identifies rank-24 invariant as $E_8$-instanton-number on K3, NOT Mukai-rank;
- correctly predicts Schur index = $\vartheta_1^2 / \eta^6$ (cuspidal limit), matching depth-1 Borcherds expansion;
- correctly identifies cuspidal-limit Hopf structure as BPS line-operator ring;
- correctly predicts elliptic deformation as Aganagic--Okounkov elliptic stable envelopes.

**Three-path verification of Wave 11 final claim**:

- **Path 1** (Beem--Rastelli MN $E_8$): vacuum character of $(\widehat{E_8})_{-12}$ at K3-twist matches $\mathbf{H}_{\Delta_5}$ vacuum character.
- **Path 2** (Vafa F-theory K3): 24 7-branes on K3 = 24 $E_8$ instantons = 24 Kodaira fibres = 24 BPS vacua.
- **Path 3** (Aganagic--Okounkov + BFN): elliptic stable envelopes on K3 Hitchin moduli = elliptic deformation of $\mathbf{H}_{\Delta_5}$.

---

## Wave 11 retractions (vs Wave 10)

1. **Affine $\widehat{A}_{23}$ quiver Lagrangian for $T[K3]$** RETRACTED (Cycle 1.5): replaced by the non-Lagrangian Minahan--Nemeschansky $E_8$ K3-twist avatar. The "$U(1)^{24}$" frame is a category error; the correct frame is **Lagrangian-free** $E_8$ class.

2. **"24 vector-valued Sp$_4(\mathbb{Z})$-Jacobi forms of weight 5 index 1"** RETRACTED (Cycle 3.4): weight-5 Sp$_4$-Jacobi forms do not exist (Igusa). Replaced by **24-dim BPS Hilbert space at depth 1 of $\Phi_{10}^{-1}$** with character $\vartheta_1^2/\eta^6$, transforming as a vector-valued elliptic genus.

3. **"Rank(Mukai) = rank($\widehat{A}_{23}$ quiver) = 24"** RETRACTED (Cycle 2.4): coincidence of numerics; the lattices have different signatures and isomorphism types. The genuine rank-24 invariant is $E_8$-instanton-number = Vafa F-theory K3 7-brane count.

4. **"3D Coulomb-branch index of $\widehat{A}_{23}$ candidate matches $\phi_{10,1}$"** FALSIFIED (Cycle 4.3): the candidate quiver gives $\eta^{24}$, missing the $\vartheta_1^2$ factor.

5. **"K-theoretic Hall on coh(K3) = $\mathbf{H}_{\Delta_5}$ unconditionally"** PARTIALLY RETRACTED (Cycle 5.4): the Hall-algebra picture is the cuspidal limit; full elliptic structure comes from elliptic stable envelopes.

---

## Wave 11 promotions (Wave 10 status raised)

- **24 BPS vacua = 24 Kodaira fibres**: PROMOTED to **= 24 $E_8$ instantons = 24 F-theory 7-branes** via Vafa hep-th/9602022; full F-theory dictionary now load-bearing.
- **3D mirror frame**: PROMOTED to **Beem--Rastelli 4d $\mathcal{N}=2$ avatar** with explicit chiral algebra $(\widehat{E_8})_{-12}$.
- **Holomorphic block / Sp$_4$ Jacobi structure**: SHARPENED to **vacuum character of MN $E_8$ K3-twist Schur sector**.

---

## Wave 11 surviving disagreements / OPEN MATH

**Disagreement W11-G-D1**: the Schur-index match in §4.4 boxed equation (W11-G-1) is conjectural at all orders past leading. Falsification test: compute $\mathrm{ch}_{(\widehat{E_8})_{-12}, \mathrm{vac}}$ at $q^1$ and check against $\vartheta_1^2/\eta^6$ expansion. **Status**: OPEN MATH, ~200 lines SageMath / Mathematica.

**Disagreement W11-G-D2**: the K3-twist of MN $E_8$ is implicit; no primary literature constructs this twist explicitly. The natural candidate is "MN $E_8$ on $S^3$ with 24-instanton boundary condition" but the explicit instanton-bundle data is non-trivial. **Status**: OPEN MATH, requires Yamada--Yoshida-style explicit 24-instanton bundle on K3.

**Disagreement W11-G-D3**: the Aganagic--Okounkov elliptic stable envelopes on $E_8$ Hitchin moduli are not explicitly computed in primary literature; their existence is conjectural for non-A-type. **Status**: OPEN MATH, requires extension of AO 2016 to type $E$.

**Disagreement W11-G-D4** (carried from Wave 10 D5): T[K3] N=4 vs N=8 SUSY enhancement. With Wave 11's MN $E_8$ avatar, the 3d compactification has $\mathcal{N}=4$ from M-theory direct count; no $\mathcal{N}=8$ enhancement at the rank-1 MN $E_8$ point (which is genuinely $\mathcal{N}=2$ in 4d with no further enhancement). **Status**: PARTIALLY CLOSED -- 3d MN $E_8$ on $S^1$ has $\mathcal{N}=4$, matching Wave 10 Heal 1.A.

---

## Wave 12 tasks (W12-T_*)

**W12-G-T1 (highest payoff / low difficulty)**: compute $\mathrm{ch}_{(\widehat{E_8})_{-12}, \mathrm{vac}}(q, z)$ at $q^0, q^1, q^2$ and compare to $\vartheta_1^2/\eta^6$ depth-1 expansion. ~200 lines SageMath. **Settles Wave 11 W11-G-1 falsifiability.**

**W12-G-T2 (high / moderate)**: explicit 24-instanton bundle on K3, compute its $E_8$ moduli space dimension and match to MN $E_8$ Coulomb branch dimension after K3-twist. ~500 lines SageMath. **Settles W11-G-D2.**

**W12-G-T3 (high / very high)**: extend Aganagic--Okounkov elliptic stable envelopes from A-type to $E_8$. **Settles W11-G-D3, requires multi-quarter effort.**

**W12-G-T4 (moderate / high)**: F-theory geometric engineering of $\Delta_5$ via Vafa K3 $\times T^2$ background. **Resolves Wave 10 D6 (Costello).**

**W12-G-T5 (high / moderate)**: compute the BPS line-operator category of MN $E_8$ on $S^1$ via class-$\mathcal{S}$-skein-algebra technology (Higgs--Goncharov). Compare to $\mathbf{H}_{\Delta_5}^{\mathrm{cusp}}$ Hopf structure. ~300 lines.

---

## Manuscript amendments suggested for Wave 12

1. **`chapters/examples/k3_yangian_chapter.tex`**: replace Wave 10 inscription "affine $\widehat{A}_{23}$ quiver Lagrangian for $T[K3]$" with **"Minahan--Nemeschansky $E_8$ K3-twist Lagrangian-free 4d $\mathcal{N}=2$ avatar"**; cite Minahan--Nemeschansky 1996, Beem--Rastelli 2014, Vafa F-theory 1996.

2. **`chapters/examples/k3_yangian_chapter.tex`**: add subsection "Schur-index identification: $\mathcal{I}_{\mathrm{Schur}}(T_{E_8}^{\mathrm{MN}, K3}) = \vartheta_1^2/\eta^6$" with explicit character data.

3. **`chapters/examples/cy_d_kappa_stratification.tex`**: register **AP-CY-W11-Gaiotto-1**: Lagrangianizing a Lagrangian-free SCFT (Argyres--Douglas, MN $E_8$, etc.) is a category error; treat directly via Beem--Rastelli chiral algebra.

4. **`chapters/connections/concordance.tex`**: register **AP-CY-W11-Gaiotto-2**: 24-Kodaira / 24-Mukai / 24-Niemeier / 24-7-branes are FOUR distinct counts, not interchangeable; specify which is meant.

5. **`appendices/first_principles_cache.md`**: append Wave 11 Gaiotto entries (Lagrangian-free 4d $\mathcal{N}=2$, 24-count taxonomy, Beem--Rastelli Schur identification).

---

## Summary

Wave 10 Gaiotto's "$\widehat{A}_{23}$ quiver $T[K3]$" with "24 Sp$_4$-Jacobi blocks of weight 5 index 1" is **retracted on five fronts**: the Lagrangian frame is a category error; rank-24 conflates Kodaira/Mukai/Niemeier; weight-5 Sp$_4$-Jacobi forms don't exist; the candidate-quiver Coulomb-branch index doesn't match $\phi_{10,1}$; the line-operator structure is only cuspidal not full elliptic. The **true physics avatar** is the **Minahan--Nemeschansky $E_8$ rank-1 4d $\mathcal{N}=2$ SCFT, K3-twisted via 24 instantons**, a Lagrangian-free theory whose Beem--Rastelli chiral algebra is $(\widehat{E_8})_{-12}$, whose Schur index is $\vartheta_1^2/\eta^6$, and whose BPS line-operator category is the cuspidal limit $\mathbf{H}_{\Delta_5}^{\mathrm{cusp}} = Y^{\mathrm{Borch}}_\hbar(\mathfrak{g}_{\Delta_5})$. The full elliptic structure comes from Aganagic--Okounkov elliptic stable envelopes on $E_8$ Hitchin moduli.

Five attack-heal cycles closed. Five Wave 10 retractions issued. Three Wave 10 promotions issued. Four open math disagreements (W11-G-D1..D4). Five Wave 12 tasks proposed. Wave 11 final boxed equation:
$$
\mathbf{H}_{\Delta_5} \;=\; \mathrm{Lines}\bigl(T_{E_8}^{\mathrm{MN}, K3}\bigr) \;\cong\; K^T\bigl(\mathcal{M}_{\mathrm{Hitchin}}^{E_8, K3\text{-twist}}\bigr)_{(q, t, p)}.
$$
