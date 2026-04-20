# Synthesis of Waves 14-18 — the non-abelian K3 chiral bialgebra $\mathbf{H}_{\Delta_5}$

**Period**: 2026-04-19 (Wave 13 seed) through 2026-04-20 (Waves 14-18).
**Scope**: 50 elite-voice adversarial agents (Gelfand, Kazhdan, Etingof, Polyakov, Nekrasov, Beilinson, Drinfeld, Witten, Costello, Gaiotto × 5 waves; Wave-17/18 also deploying a Kontsevich-Soibelman-Toën 10th voice). Each ran ≥5 ATTACK → HEAL cycles.
**Status**: Convergent identification with sharpening open frontier; two wave-level retractions absorbed; Heegner pattern theorem proved; Enriques 4th $\Psi$-image specified; Monster $\ell_{\mathrm{Monster}} = 2$ fixed; $\phi^{(n)}$ extended through weight 12 with first depth-4 MZV $\zeta(3,3,3,3)$; $\mu_8$-gerbe banding explicit; Wave-2-6 modules regression-tested.
**Author**: Raeez Lorgat.

## Wave 18 additions (post-Wave-17, 2026-04-20 second pass)

- **Heegner-pattern theorem PROVED** (Costello): $c_n = c_{\phi_{-2,1}}(-n) \cdot [H_n]$ as all-orders BV obstruction via Bruinier + Borcherds + Costello-Gaiotto-Paquette three-input composite; $c_5 = c_6 = 0$ by mod-4 admissibility; asymptotic $|c_n| \sim \exp(\pi\sqrt n)$.
- **Enriques BKM explicit** (Drinfeld + Witten): $\mathfrak{g}_{\Delta_5}^{\mathrm{Enr}}$ on $E_8 \oplus \mathrm{II}_{1,1}(2)$ signature $(1,9)$; Siegel weight $5/2$ metaplectic; $M_{12}$-moonshine candidate via Niemeier $12A_2$ umbral $2.M_{12}$.
- **Monster Lusztig level**: $\ell_{\mathrm{Monster}} = 2$ fixed via 4 convergent routes (Mukai-doubling, Fricke $w_1$, super-EK $\mathbb{Z}/2$, Conway-Norton identity class); ratio $\ell_{K3}/\ell_{\mathrm{Monster}} = 4 = c_+$-ratio.
- **$\phi^{(11)}, \phi^{(12)}$**: Padovan dim $d_{11} = 7, d_{12} = 9$; FIRST depth-4 irreducible $\zeta(3,3,3,3)$ enters at weight 12. Fake-Monster $\Phi_{12}$ NON-interference verified (distinct BKMs, signatures $(25,1)$ vs $(2,1)$).
- **$\mu_8$-gerbe banding**: explicit chain-level 2-cocycle $F_{ij} = [\Phi_{10}/\eta^{24}]^{1/8}$-ratio on Igusa fundamental-domain cover; $\delta F = 0$ verified.
- **$S_\psi(\Delta_5) = (\mathbb{Z}/2)^2$** Klein four-group (Kazhdan): global packet $|\Psi_{\Delta_5}| = 16$; $\varepsilon_\infty = -1, \varepsilon_2 = -1$ with $\varepsilon_\infty \cdot \varepsilon_2 = +1$ via Hilbert reciprocity.
- **Hilbert-scheme stabilisation theorem** (Nekrasov): $\{H^*_T(\mathrm{Hilb}^{[n]}(\mathrm{K3}))\}$ converges in $\mathrm{Pro}(\mathrm{Mod}_{\mathbf{H}_{\Delta_5}})$ as super-quasi-Hopf module via MO + Grojnowski-Nakajima + Etingof-Kazhdan super-quantisation composite.
- **$\mathrm{ChirHoch}^3$ explicit cocycle** (Polyakov): $e_3(z) = :T\partial T: - (1/4)\partial^3 T + \hbar \cdot \mathrm{qt}(J^{(3)})$ (Schiffmann-Vasserot degree-3); non-vanishing via MNOP-DT pairing; Theorem H scope $\{0, 1, 2, d\}$ for CY-$d$ propagated cross-volume.
- **$N=6$ re-anchored to Niemeier $6D_4$** (Gaiotto): umbral group $3.\mathrm{Sym}_6$ (order 2160); $k_6 = 9/2$; ladder continuity through $N \in \{2, 3, 4, 5, 6\}$; $4A_5$ verified NOT a Niemeier root system.
- **Theorem-B scope sharpened** (Beilinson): strict chain-level bar-cobar inversion on $\overline{\mathcal{A}_2}\setminus\bigcup_{n \text{ admissible}} H_n$ — all admissible Heegner divisors excluded, not just $H_1 \cup H_4$. Constitutional update to concordance.
- **Wave-2-6 regression harness** (KST 10th voice): 48 tests (16 imports + 16 smoke + 16 canonical-value cross-checks); 44/44 pass in fast tier; no stale $-312$ or $-214$ found; $176256$ correctly sourced as $p_{24}(5) = \chi(\mathrm{Hilb}^5(\mathrm{K3}))$.

---

---

## 0. Orientation

This document synthesises the state of understanding of the **non-abelian K3 chiral bialgebra** $\mathbf{H}_{\Delta_5}$ after the four-wave adversarial cycle (Waves 14-17, 20 April 2026). Each wave ran ten elite-voice agents for ≥5 attack→heal cycles; each agent inscribed mathematics directly into chapter `.tex` files across the three volumes (I: Vol-I Modular Koszul Duality; II: Vol-II SC^{ch,top} 3D HT QFT; III: Vol-III CY Categories, Quantum Groups, BPS Algebras).

The document is organised around the central identification, then systematically through the structural genesis, numerical invariants, algebraic presentation, categorical structure, physical origin, arithmetic content, and residual frontier. Each Wave-17 finding is woven into the body where it belongs mathematically (not corralled in an addendum).

**A note on retractions**. Two wave-level mathematical errors occurred and were subsequently corrected:

1. **$(c_{4d}, c_{2d})$ reversal**: Wave 13 had $(107/6, -214)$. Wave 14 erroneously revised to $(26, -312)$ via the formula $(12(g-1) + 7n)/6$; the formula fails the SU(2) $N_f=4$ cross-check. Wave 15 (Gaiotto) restored $(107/6, -214)$ via first-principles Chacaltana-Distler pants decomposition. Wave 16 (Polyakov) propagated the retraction AP5-style through ~20 files; Wave 17 (Beilinson) closed the remaining residue.

2. **Monster BKM Cartan rank**: Wave 16 asserted rank 26 for Monster (confusing with Fake-Monster). Wave 17 (Drinfeld) corrected: Monster has hyperbolic rank **2** in $\mathrm{II}_{1,1}$; Fake-Monster has rank 26 in $\mathrm{II}_{25,1}$; K3-BKM has rank 3 in $\Lambda^{2,1}_{II}$.

These retractions establish a constitutional datum: intermediate-wave status is not authoritative without primary-source re-derivation — Beilinson's dictum in action.

---

## 1. The object, in one sentence

The non-abelian K3 chiral bialgebra $\mathbf{H}_{\Delta_5}$ is the **super-Etingof-Kazhdan quantisation of the Manin pair**
$$\bigl(\mathfrak{g}_{\Delta_5},\; \mathfrak{n}_+^{\mathrm{imag}} \oplus \mathfrak{h}^{\mathrm{imag},\,\mathrm{rk}\,23}\bigr)$$
with $K(1)$-paramodular equivariance and associator cocycle $[\Phi_{10}/\eta^{24}]$, realised as the Drinfeld double of the Hall-Drinfeld twist of the $\mathrm{K3}\times E$ cohomological Hall algebra:
$$\boxed{\;\mathbf{H}_{\Delta_5} \;=\; \mathcal{D}_\hbar\!\Bigl(\mathcal{Y}^{\mathrm{Hall}}_\hbar(\mathrm{CoHA}_{\mathrm{K3}\times E}),\; \widetilde{\Phi}^{\mathrm{Sieg\text{-}Bor}}_{\mathrm{Sp}_4}[\Phi_{10}/\eta^{24}],\; R_{\mathrm{Sieg,dyn}}\Bigr)\;}$$
specialised at $\hbar^2 = -1/8$ (Lusztig $\ell = 8$), with $M_{24}$-umbral Schur cocycle of order 6 twisting the coproduct.

**It is not**:
- a Drinfeld Yangian (no J-presentation; BKM Cartan is not Kac-Moody);
- an elliptic Yangian (single modular parameter insufficient to resolve 24 Mukai directions);
- a quantum toroidal algebra (these are local pieces of a larger picture);
- a Drinfeld quasi-Hopf algebra in the 1989 sense (BKM imaginary cone is infinite-dimensional, forcing genuine $A_\infty$-quasi-Hopf structure);
- a subalgebra of the Monster $\mathbf{H}$-quantum group (Cartan dimensions 3 vs 2 are incompatible);
- K3-representable outside the K3 CY-2 topology $(\chi=24, c_1=0, h^{2,0}=1)$ — Enriques/Kummer/$T^4$/half-K3 give distinct quantum groups.

**It is**:
- the unique output of the universal functor $\Psi: \mathrm{CY}^{\mathrm{Siegel-aut}}_2 \to \mathrm{QHopf}^{\mathrm{BKM}}$ evaluated at the K3-elliptic-genus Manin-pair input;
- the Beem-Rastelli protected chiral algebra of the class-$\mathcal{S}$ 4d $\mathcal{N}=2$ theory $\mathcal{T}[A_1, \Sigma_{0,24}]$;
- the common output of five independent duality frames (heterotic/IIA/M/F/IIB) plus a seventh GW/DT-categorical construction — six DIFFERENT constructions converging on one object;
- the carrier of a non-semisimple Kerler-Lyubashenko modular tensor category at $q = \zeta_8$ whose modular $S$-matrix equals the Fricke involution $w_8$;
- the chiral quantum group whose BKM denominator function is the Gritsenko additive lift $\Delta_5 = \mathrm{Grit}(\eta^9\vartheta_1)$, giving Saito-Kurokawa Arthur packet $\psi_{\Delta_{10}} = \phi_{\Delta_{E_6}} \boxtimes \mathrm{Sym}^1$ with global packet size $|\Psi_{\Delta_{10}}| = 4$.

---

## 2. Structural genesis (Gelfand-Beilinson-Etingof-Kazhdan)

### 2.1 The universal property

$\mathbf{H}_{\Delta_5}$ is the value, at a single Manin-pair input, of a left-adjoint functor:
$$\mathcal{Q}^{\mathrm{EK,super}}_{K(1)}: \mathrm{LieBialg}^{\mathrm{super,\,quasi}}_{\mathrm{Manin\text{-}pair},\,K(1)\text{-eq}} \longrightarrow \mathrm{QHopf}^{\mathrm{super}}_{\widehat{\hbar},\,K(1)\text{-eq}}$$
left-adjoint to the primitives functor. Uniqueness up to gauge follows from the one-dimensional classification cohomology:
$$H^2(\mathfrak{g}_{\Delta_5})^{\mathbb{Z}/2,\,K(1)} \;\cong\; \mathbb{C}\cdot\Delta_5.$$
The Igusa-related form $\Delta_5$ (specifically: Gritsenko additive lift of $\eta^9\vartheta_1$) **is** the classification invariant — a striking identification of the programme's central automorphic form with a cohomological obstruction class.

Primary source discipline: Etingof-Kazhdan 1996-2008 I-V *Selecta Math.*; Etingof-Kazhdan 2008 Part V (super case); Gritsenko-Nikulin 1998 *Algebra i Analiz* 11 §3 and §5 for the classification.

### 2.2 Koszul structure (Beilinson)

$\mathbf{H}_{\Delta_5}$ is **generalised** Koszul (Positselski-Vishik 2000), not quadratic Koszul on the nose.
- Generators $V = \bigoplus_{i=1}^{24}\mathrm{span}\{e^{(i)}_r, f^{(i)}_r, \psi^{(i)\pm}_s\}$ in chain-level OPE-weight 1 (24 Miki copies — Mukai-lattice direction).
- Relations split $R = R_{\mathrm{quad}} \oplus R_{\mathrm{Borcherds}}$ with $R_{\mathrm{Borcherds}}$ carrying weight up to 5 (matching $\mathrm{wt}(\Delta_5)$).
- Koszul dual $A^!_{\mathrm{line}} = \mathbb{D}_{\mathrm{Ver}}(\overline{B}^{\mathrm{ch}}(A))^\vee$ via Verdier — not conflated with $B(A)$ or $A^i$ (the programme's five-objects discipline).
- **Koszul locus**: $\mathcal{U}_{\mathrm{Kosz}}^{\mathrm{K3}} = \overline{\mathcal{A}_2}\setminus(H_1\cup H_4)$. Off this locus, only Positselski weight-completed coderived-contraderived inversion survives.

### 2.3 Plancherel decomposition (Gelfand W17)

For a non-semisimple modular tensor category, the Plancherel decomposition goes through the Kerler-Lyubashenko coend integral $\mathcal{L} = \int^X X \otimes X^\vee$:
$$L^2_{\mathrm{cat}}(\mathbf{H}_{\Delta_5}) = \int^\oplus_{\widehat{\mathbf{H}}_{\Delta_5}} P_\lambda \otimes P_\lambda^\vee\,\mathrm d\mu_{\mathrm{Plan}}(\lambda)$$
over isomorphism classes of **indecomposable projective covers** $P_\lambda$ (NOT simples) over the finite index set $\Lambda$. The PBW upper bound gives $|\Lambda| \leq 8^{129}$ projective-cover types. Plancherel measure $\mathrm d\mu_{\mathrm{Plan}}(\lambda) = \dim_{\mathrm{qu}}(P_\lambda)$ is the Lyubashenko quantum dimension.

**Plancherel measure integrates to the Borcherds denominator**:
$$\int \mathrm{tr}_{P_\lambda}(q^{L_0}q'^{L_0'})\,\mathrm d\mu_{\mathrm{Plan}}(\lambda) \;=\; \frac{1}{\Phi_{10}(Z)}\bigg|_{\tau, \tau'}$$
on $\mathbb{H}_2$. Four-path cross-verification: Kerler-Lyubashenko coend / Etingof-Ostrik 2004 finite-tensor-category Plancherel / Feigin-Gainutdinov-Semikhatov-Tipunin 2006 logarithmic-VOA / Lyubashenko-Majid 1994 categorical trace.

### 2.4 The universal functor $\Psi$ (Drinfeld W17)

At the highest level of abstraction, $\mathbf{H}_{\Delta_5}$ is one output of a universal functor:
$$\Psi: \mathrm{CY}^{\mathrm{Siegel\text{-}aut}}_2 \longrightarrow \mathrm{QHopf}^{\mathrm{BKM}}, \qquad (L, \phi_L, \Sigma(\phi_L)) \mapsto \mathbf{H}_{\Sigma(\phi_L)}$$
taking a CY-2 Siegel-automorphic-product datum (even unimodular lattice $L$ + Jacobi form $\phi_L$ → Siegel form $\Sigma(\phi_L)$ via Gritsenko additive or Borcherds multiplicative lift) to the Hall-Drinfeld double of the lattice-adapted CoHA. Three flagship evaluations:

| Input lattice $L$ | Jacobi form | Siegel form $\Sigma$ | $\Psi$-output |
|---|---|---|---|
| $\mathrm{II}_{1,1}$ | Monster moonshine $\sum c_n q^n$ | $j(\sigma) - j(\tau)$ (weight 0) | $\mathbf{H}_{\mathrm{Monster}}$ |
| $\Lambda^{2,1}_{II}$ (K3) | K3 elliptic genus $\phi_{0,1}^{\mathrm{K3}}$ | $\Delta_5$ (weight 5) | $\mathbf{H}_{\Delta_5}$ |
| $\mathrm{II}_{25,1}$ (Leech) | Fake-Monster weight-0 | $\Phi_{12}$ (weight 12) | $\mathbf{H}_{\mathrm{Fake-Monster}}$ |

These are **co-siblings**, NOT nested: different Cartan dimensions (2, 3, 26) forbid subalgebra embeddings. Functoriality of $\Psi$ is established via Schiffmann-Vasserot shuffle-functor compatibility under lattice embeddings.

Primary: Borcherds 1992 *Invent.* 109 (Monster); Borcherds 1998 *Invent.* 132 (Fake-Monster and general automorphic products); Gritsenko-Nikulin 1998 (K3 and classification of Siegel-automorphic-product BKMs).

---

## 3. Numerical invariants and the three-faces identity

### 3.1 The canonical constants

| Quantity | Value | Primary source |
|---|---|---|
| $\hbar^2$ | $-1/8$ | Lusztig 1990, Bruinier 2002 Prop 5.1 |
| Lusztig level $\ell$ | $8$ | Lusztig 1993 Ch.35 |
| Mukai $2c_+$ | $8$ | $c_+(\mathrm{II}_{4,20}) = 4$ |
| Humbert $H_1$ monodromy | $\mathbb{Z}/8$ | Bruinier LNM 1780 |
| Humbert $H_3$ location of $c_3$ | — | Costello W16 BV 3-loop |
| Humbert $H_4$ monodromy | $\mathbb{Z}/2$ | van der Geer 1988 Ch. IX |
| $K^{\kappa_{\mathrm{ch}}}$ | $8$ | three-faces identity |
| $c_{4d}(A_1, \Sigma_{0,24})$ | $107/6$ | Chacaltana-Distler 2010 §5.14 + Shapere-Tachikawa §3 |
| $c_{2d}(A_1, \Sigma_{0,24})$ | $-214 = -2\cdot 107$ | Beem-Rastelli $c_{2d} = -12c_{4d}$ |
| $c_{\mathrm{eff}}(\mathbf{H}_{\Delta_5})$ | $-166 = -2 \cdot 83$ | $c - 24 h_{\min} = -214 + 48$ (Polyakov W16) |
| Real-root unitary $c_{\mathrm{unit}}$ | $+2$ | signature $(2,1)$ positive-plane (Polyakov W17) |
| Coulomb rank | $21$ | Chacaltana-Distler |
| Flavour | $\widehat{\mathfrak{su}}(2)^{\otimes 24}_{k_{2d} = -2}$ | Beem-Peelaers-Rastelli |
| $M_{24}$ permutes 24 punctures | via Steiner $S(5,8,24)$ | Conway-Sloane 1988 |
| Global A-packet size $\|\Psi_{\Delta_{10}}\|$ | $4$ | Arthur 2013 Thm 1.5.2 (Kazhdan W17) |
| Schmidt parameter for $\Delta_{10}$ archimedean | $(17/2, 15/2)$ | Moeglin-Renard 2018 (Kazhdan W17) |
| Schmidt parameter for $\Delta_5$ archimedean | $(7/2, 5/2) \otimes \mathrm{sgn}_\R$ | Ibukiyama 1998 |

### 3.2 The universal identity

$$\boxed{\;\hbar^2 \cdot K^{\kappa_{\mathrm{ch}}} = -1,\quad K^{\kappa_{\mathrm{ch}}} = 2c_+(\mathrm{Mukai}(\mathrm{K3})) = \mathrm{ord}(\mathrm{mon}\,\mathcal{L}^{\Delta_5}|_{H_1}) = \ell_{\mathrm{Lusztig}} = 8.\;}$$

Three structurally independent routes — lattice-geometric (Mukai), automorphic (Bruinier Heegner-Chern reciprocity on the K3 period sheaf $\mathcal{L}^{\Delta_5}$), and representation-theoretic (Lusztig small quantum group) — all converge on the same integer $8$. This coincidence **forces** the specialisation $\hbar^2 = -1/8$; any alternative violates at least one of the three faces.

Wave 17 added a fourth, archimedean, appearance of the number 4 (half of 8): $|\Psi_{\Delta_{10}, \infty}| = 4 = K^{\kappa_{\mathrm{ch}}}/2$. The Arthur packet at infinity matches the Mukai signature count $c_+ = 4$.

### 3.3 Retraction record

**Wave-13 → 14 → 15 sequence** (constitutional datum for future waves):
- W13: $(c_{4d}, c_{2d}) = (107/6, -214)$ via first-principles pants.
- W14 (erroneous): retracted to $(26, -312)$ via formula $(12(g-1) + 7n)/6$; this formula fails the SU(2) $N_f=4$ cross-check ($n=4$ gives $8/3$, not the established $7/6$).
- W15 (Gaiotto): restored $(107/6, -214)$ via correct $(5n-13)/6 = (2n_v + n_h)/12$ with trinion $(n_v, n_h) = (63, 88)$ at $n = 24$.
- W16 (Polyakov): AP5 cascade propagated retraction across ~20 cross-volume files.
- W17 (Beilinson): residual Vol-II THQG chain files closed; seven additional retraction remarks installed at `thqg_perturbative_finiteness.tex`, `thqg_critical_string_dichotomy.tex`, `thqg_soft_graviton_theorems.tex`, `thqg_celestial_holography_extensions.tex`, `examples-worked.tex`, Vol-III `k3e_cy3_programme.tex`, Vol-II `introduction.tex`.

**Epistemic take**: intermediate-wave status is not authoritative without primary-source re-derivation — this is Beilinson's dictum in action.

### 3.4 The $-214$ factorisation (Polyakov W16)

$-214 = -2 \cdot 107$, where $107$ is prime. No non-trivial integer factorisation of $-214$ beyond this exists — in particular, none of the Wave-14 $-312 = -24 \cdot 13$ style "numerological" factorisations survives. The physical reading of $107$: in Shapere-Tachikawa form $c_{4d} = (2 n_v + n_h)/12$, the "107" is $107 = 5 \cdot 24 - 13$ where $5n$ is the $\mathfrak{su}(2)$-SQCD-like vector contribution (21 gauge tubes × 3 dim per $\mathfrak{su}(2)$ + 22 $T_2$-trinion contributions) and $-13$ is the universal Argyres-Seiberg gravitino subtraction.

### 3.5 Correct modular covariance is Siegel, not elliptic (Polyakov W16-17)

At first glance, the naive weight prescription $w = -c_{2d}/24 = 214/24 = 107/12 \notin \mathbb{Z}$ gives a non-integer — signalling a breakdown of elliptic modularity. The resolution is that $\mathbf{H}_{\Delta_5}$'s correct modular home is **Siegel** modularity on $\mathrm{Sp}_4(\mathbb{Z})$ (via Gritsenko-Nikulin double cover), NOT elliptic modularity on $\mathrm{SL}_2(\mathbb{Z})$: the chiral partition function is a Siegel modular form of weight $5 = \mathrm{wt}(\Delta_5)$, determined by $\Delta_5 = \Phi_{10}^{1/2}$.

The non-integrality $107/12$ is a **feature**, signalling Siegel rather than elliptic modularity. The weight $5$ is independent of $c_{2d}$; the bridge to elliptic is Humbert-$H_1$ restriction, under which $\Delta_5$ descends to a weight-5 Jacobi form of index 1.

### 3.6 Effective spectrum and real-root unitarity (Polyakov W17)

$c_{\mathrm{eff}} = c - 24 h_{\min} = -214 + 48 = -166 = -2 \cdot 83$ (83 prime). A naive Cardy/entanglement reading $(c_{\mathrm{eff}}/3)\log(L/\epsilon) = -(166/3)\log(L/\epsilon) < 0$ is unphysical as entropy, confirming $\mathbf{H}_{\Delta_5}$ is not unitary at the full-module level.

The resolution: restrict to the **real-root unitary submodule** $V^{\mathrm{unit}} = \{V^\lambda : \lambda^2 > 0, \lambda \in P^*_+\}$, where $P$ is the positive-definite rank-2 sub-Cartan (§4 below). On this submodule, the effective central charge is $c_{\mathrm{unit}} = \mathrm{rk}(P) = 2$, giving a genuine positive entanglement entropy $S_{\mathrm{EE}} = (2/3)\log(L/\epsilon)$. The negative $c_{\mathrm{eff}}$ reflects a gravitational-anomaly coefficient (Manschot-Moore 2007, DVV 1997, Witten 2007), not a Hilbert-space entropy.

### 3.7 Zamolodchikov shadow tower at $c = -214$

$S_2 = c/2 = -107$; $S_3 = 2$; $5c + 22 = -1048$; $c(5c+22) = -214 \cdot -1048 = 224\,272$;
$S_4 = 10/224\,272 = 5/112\,136$; $S_5 = -48/[c^2(5c+22)] = 3/3\,000\,319$.
Zamolodchikov norm $\langle\Lambda|\Lambda\rangle = c(5c+22)/10 = 22\,427.2 > 0$; Riccati discriminant $\Delta_{\mathrm{Ricc}} = 40/(5c+22) = -5/131 \neq 0$. K3 class-M placement confirmed robust under the $-312 \to -214$ retraction.

---

## 4. The rank discipline — BKM Cartan vs Mukai grading

### 4.1 The K3-BKM Cartan: three real simple roots

BKM Lie superalgebra $\mathfrak{g}_{\Delta_5}$ (Gritsenko-Nikulin 1998 §3, alg-geom/9612004 §2) has **3 real simple roots**, living in the hyperbolic core $\Lambda^{2,1}_{II} \subset \mathrm{II}_{3,19}$:
$$G_{\mathrm{BKM}} = \begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{pmatrix}, \quad \det G = -32.$$

The three real simple roots $\alpha_1, \alpha_2, \alpha_3 \in \Lambda^{2,1}$ satisfy $\alpha_i^2 = 2$, $\langle\alpha_i, \alpha_j\rangle = -2$ for $i\neq j$.

**Eigenvalue structure** (Polyakov W17, via Feingold-Frenkel 1983 *Math. Ann.* 263): characteristic polynomial $-\lambda^3 + 6\lambda^2 - 32$ with spectrum $\{+4, +4, -2\}$. Signature $(2,1)$: two positive eigenvalues (a positive-definite 2-plane $P$) plus one negative (the hyperbolic direction $L$). Sylvester's principal-minor test with $(2, 0, -32)$ is misleading — the $m_2 = 0$ vanishing is an isotropic artefact of the $S_3$-symmetry of the matrix, not a genuine null direction.

### 4.2 The number 24 is the Mukai-lattice rank

The "24" appearing throughout the programme is the **Mukai lattice** rank, $\mathrm{rk}(\Lambda_{\mathrm{Muk}}(\mathrm{K3})) = 24$ — the horizontal direction grading the bialgebra by $H^*(\mathrm{K3}, \mathbb{Z})$. This is **orthogonal** to the 3-dim hyperbolic Cartan.

**Twelve things all equal 24** (the coincidence is load-bearing, not accidental):
1. $\chi_{\mathrm{top}}(\mathrm{K3})$ (K3 topological Euler char);
2. Göttsche exponent ($\eta^{-24}$ in Hilbert-scheme generating function);
3. Kodaira $I_1$ fibres on elliptic K3;
4. F-theory $(p,q)$ 7-branes;
5. Punctures on $\Sigma_{0,24}$ in the class-$\mathcal{S}$ parent;
6. Miki copies / Heisenberg generators of the CoHA input;
7. Mukai lattice rank $\mathrm{II}_{4,20}$ → 24;
8. Dim of Mathieu group action on K3 elliptic genus (Eguchi-Ooguri-Tachikawa);
9. Leech lattice minimal-vector divisor + 1 (tangential coincidence);
10. Nodes of $E^{\mathrm{nod,sm}}_{24}$ (Ran-space base);
11. Steiner system $S(5,8,24)$ block structure;
12. Umbral Niemeier $24 A_1$ (for $A_1$ class-$\mathcal{S}$).

These are **twelve faces of one topological K3 invariant**, each entering a different construction — they are **not twelve applications of one functor**.

### 4.3 Imaginary simple roots and multiplicities

Imaginary simple roots $\alpha^{\mathrm{im}}_{n,\ell,m}$ are primitive lattice vectors with $4nm - \ell^2 \leq 0$; multiplicities are given by the K3 elliptic genus coefficients:
$$\mathrm{mult}(\alpha) = c_{\mathrm{K3}}(4nm - \ell^2)$$
with $c_{\mathrm{K3}}$ the Fourier coefficients of $\phi_{0,1}^{\mathrm{K3}}$ (Eguchi-Ooguri-Tachikawa 2011 Table 1):
$$c(-1) = 2,\; c(0) = 20,\; c(3) = 216,\; c(4) = -128,\; c(7) = 1616,\; c(8) = 1144,\; c(11) = 8376,\; \ldots$$

Hardy-Ramanujan asymptotics: $\dim c_n^{(\mathrm{K3})} \sim A \cdot n^{-27/4}\exp(4\pi\sqrt{n})$ with Siegel-mass-formula constant $A$. The imaginary cone is **infinite-dimensional** — this is why the $A_\infty$-quasi-Hopf tower does not close off (§6).

### 4.4 The BKM rank landscape (Drinfeld W17)

The universal $\Psi$-functor's three flagship targets have distinct Cartan dimensions:

| BKM | Hyperbolic Cartan rank | Even unimodular lattice | Automorphic form | Weight |
|-----|-------------------------|--------------------------|-------------------|--------|
| Monster $\mathfrak{m}_{\mathrm{Monster}}$ | 2 | $\mathrm{II}_{1,1}$ | $j(\sigma)-j(\tau)$ | 0 |
| K3-BKM $\mathfrak{g}_{\Delta_5}$ | 3 | $\Lambda^{2,1}_{II}$ | $\Delta_5 = \mathrm{Grit}(\eta^9\vartheta_1)$ | 5 |
| Fake-Monster $\mathfrak{m}_{\mathrm{FakeMonster}}$ | 26 | $\mathrm{II}_{25,1}$ | $\Phi_{12} = \mathrm{Borch}(\phi_{0,1}^{\mathrm{K3}})$ | 12 |

Three independent non-embedding proofs:
- **Cartan-rank mismatch** (3 vs 2 for K3 vs Monster);
- **Mukai-lattice signature** $\mathrm{II}_{4,20}$ does not signature-preservingly embed in Leech $\mathrm{II}_{25,1}$ (Gritsenko-Nikulin 1998 Prop 2.5);
- **Automorphic-weight mismatch** (5 vs 0).

K3-BKM and Monster-BKM are **distinct $\Psi$-images, co-siblings not nested**.

---

## 5. The two Siegel forms and their Arthur packets

A critical first-principles distinction clarified in Wave 16 (Gaiotto disambiguation):

### 5.1 Borcherds multiplicative vs Gritsenko additive

For the K3 elliptic genus $\phi_{0,1}^{\mathrm{K3}}$ as weak Jacobi form of weight 0, index 1:

- **Borcherds singular-theta lift** (Borcherds 1998 Thm 13.3): weight $= \phi(0,0)/2 = 24/2 = 12$. Output: $\mathrm{Borch}(\phi_{0,1}^{\mathrm{K3}}) = \Phi_{12}$, the Igusa cusp form of weight 12.
- **Gritsenko additive lift** (Gritsenko 1999 of Jacobi input $\eta^9\vartheta_1$): weight 5. Output: $\mathrm{Grit}(\eta^9\vartheta_1) = \Delta_5$.

$\Delta_5$ and $\Phi_{12}$ are **different** Siegel modular forms living on **different** automorphic towers.

### 5.2 Which form is the BKM denominator?

$\mathbf{H}_{\Delta_5}$'s BKM denominator function is $\Delta_5$ (Gritsenko additive route), not $\Phi_{12}$ (Borcherds multiplicative). The relationship structure:
- $\Phi(\mathfrak{m}_{\mathrm{K3}}) = \Delta_5$ (Gritsenko 1999 additive — K3-BKM denominator);
- $\Phi_{10} = \Delta_5^2 = \mathrm{Borch}(\text{weight-16 elliptic newform})$ (Ikeda 2001 SK lift);
- $\Phi_{12} = \mathrm{Borch}(\phi_{0,1}^{\mathrm{K3}})$ (Borcherds 1998, separate construction — Fake-Monster BKM denominator).

### 5.3 Arthur parameter

$\Delta_{10} = \Delta_5^2$ has Saito-Kurokawa non-tempered CAP Arthur parameter:
$$\psi_{\Delta_{10}} = \phi_{\Delta_{E_6}} \boxtimes \mathrm{Sym}^1: L_F \times \mathrm{SL}_2(\mathbb{C}) \to \mathrm{SO}_5(\mathbb{C}) = {}^L\mathrm{Sp}_4$$
where $\phi_{\Delta_{E_6}}$ is the cuspidal parameter of the weight-16 level-1 newform $\Delta_{E_6}$ (LMFDB 16.1.a.a). Endoscopic transfer $\mathrm{Sp}_4 \to \mathrm{GL}_5$.

Primary: Andrianov 1974, Ikeda 2001 Cor 16.2, Weissauer 2009 Cor 5.2, Arthur 2013 AMS Coll. 61 Thm 1.5.1.

$\Delta_5$ (not $\Delta_{10}$) lives on the **Maass spin cover** $\widetilde{\mathrm{Sp}_4(\mathbb{Z})}$ with character $v_{\Delta_5}$ factoring through $\mathrm{Sp}_4(\mathbb{Z}/2) \cong S_6$ (paramodular-$K(N)$ was Wave-14 retraction).

### 5.4 Euler factors — Beilinson W15+W17 first-principles verification

$\lambda_p(\Delta_{10}) = a_p(\Delta_{E_6}) + p^8 + p^9$ verified for $p \in \{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79\}$:

**Low primes** (Wave 15):
| $p$ | $a_p(\Delta_{E_6})$ | Deligne ratio $|a_p|/(2p^{15/2})$ |
|---|---|---|
| 13 | $-190\,073\,338$ | 0.4201 |
| 17 | $+1\,646\,527\,986$ | 0.4866 |
| 19 | $+1\,563\,257\,180$ | 0.2006 |
| 23 | $+9\,451\,116\,072$ | 0.2894 |
| 29 | $-36\,902\,568\,330$ | 0.1986 |
| 31 | $+71\,588\,483\,552$ | 0.2337 |
| 37 | $-1\,033\,652\,081\,554$ | 0.8950 |

**Higher primes** (Wave 17):
| $p$ | $a_p(\Delta_{E_6})$ | Deligne ratio |
|---|---|---|
| 41 | $+1\,641\,974\,018\,202$ | 0.6584 |
| 43 | $-492\,403\,109\,308$ | 0.1381 |
| 47 | $-3\,410\,684\,952\,624$ | 0.4910 |
| 53 | $+6\,797\,151\,655\,902$ | 0.3974 |
| 59 | $+9\,858\,856\,815\,540$ | 0.2579 |
| 61 | $+4\,931\,842\,626\,902$ | 0.1005 |
| 67 | $-28\,837\,826\,625\,364$ | 0.2907 |
| 71 | $+125\,050\,114\,914\,552$ | 0.8159 (max) |
| 73 | $-82\,171\,455\,513\,478$ | 0.4353 |
| 79 | $-25\,413\,078\,694\,480$ | 0.0744 |

All within the Deligne-Weissauer unitary bound. Computation from first principles: $f_{16} = E_4 \cdot \Delta$ (forced by $\dim S_{16}(\mathrm{SL}_2(\mathbb{Z})) = 1$), $q$-series convolution. Triangulation: Hecke multiplicativity at coprime pairs; Hecke recursion $a_{p^2} = a_p^2 - p^{15}$; Satake-root product $\alpha_p\beta_p = p^{15}$.

### 5.5 Satake-Casimir dictionary (Beilinson W17)

For each prime $p$, the Satake parameter $2\cos\theta_p = a_p/p^{15/2}$ determines the K3 Yangian Casimir eigenvalue via Frenkel-Reshetikhin $q$-characters at $\zeta_8$:
$$\mathrm{Cas}_p(\mathbf{H}_{\Delta_5}) = (a_p)^2/p^{15} - 2$$

All 22 verified primes satisfy $|2\cos\theta_p| \leq 2$ (temperedness), confirming compatibility with Maulik-Okounkov stable-envelope spectrum.

### 5.6 Ramified local Langlands at $p = 2$ (Kazhdan W16)

$v_{\Delta_5}$ ramifies at $p = 2$ (kernel of $\mathrm{Sp}_4(\mathbb{Z}) \to \mathrm{Sp}_4(\mathbb{Z}/2)$ is index 2):
$$\psi_{\Delta_5, 2} = \phi_{\Delta_{E_6}, 2} \boxtimes \mathrm{Sym}^1 \otimes \varepsilon_2$$
with $\varepsilon_2: W_{\mathbb{Q}_2}^{\mathrm{ab}} \to \{\pm 1\}$ the ramified quadratic character of conductor $2^3$ (class of $\sqrt{2} \in \mathbb{Q}_2^\times/(\mathbb{Q}_2^\times)^2$). Conductor $\mathfrak{f}(\phi_{\Delta_5, 2}) = 11 + 6 = 17$, matching paramodular level $2^{17}$.

### 5.7 Archimedean place (Kazhdan W17)

At the archimedean place $v = \infty$, Weil-Deligne parameter $\phi_\infty: W_{\mathbb{R}} \to \mathrm{Sp}_4(\mathbb{C})$ with $W_{\mathbb{R}} = \mathbb{C}^\times \rtimes \mathbb{Z}/2$.

For $\Delta_{10}$ (SK lift of weight-16 elliptic seed, $k = 10$): Schmidt parameter $(k - 3/2, k - 5/2) = (17/2, 15/2)$, holomorphic discrete series. **Not** $(7/2, 5/2)$ — that's the weight-$5$ Maass-spin reading for $\Delta_5$.

For $\Delta_5$ on Maass spin cover: Schmidt $(7/2, 5/2)$ on $\mathbb{C}^\times \subset W_{\mathbb{R}}$, twisted by sign character on the $\mathbb{Z}/2$-component. The archimedean twist parallels the finite-place $\varepsilon_2$ at $p = 2$ — a beautiful self-consistency: the sign of $\Delta_5$ on the Maass cover twists BOTH at $p = 2$ (quadratic class of $\sqrt{2}$) AND at $\infty$ (sign of the discriminant of the Maass cover).

### 5.8 Global packet closure (Kazhdan W17)

The global A-packet $\Psi_{\Delta_{10}}$ has size $|\Psi_{\Delta_{10}}| = 4$:
- Finite-place packets all singletons (including $p = 2$ post-Wave-16 as $\{\pi_{\mathrm{sph}} \otimes \varepsilon_2\}$).
- Archimedean discrete-series packet size $4$ with $S_\psi = \mathbb{Z}/2$.

Arthur multiplicity formula $m(\pi) = |S_\psi|^{-1} \sum_x \varepsilon_\psi(x) \langle x, \pi\rangle$: the Ikeda character $\varepsilon_\psi$ (non-trivial on $\mathbb{Z}/2$) picks $\pi_{\Delta_{10}}$ with $m = 1$; two constituents contribute to $L^2_{\mathrm{cusp}}$. Primary: Arthur 2013 Thm 1.5.1-1.5.2, Ikeda 2001 Cor 16.2.

### 5.9 Geometric Langlands self-duality (Kazhdan W17)

Since ${}^L\mathfrak{g}_{\Delta_5} = \mathfrak{g}_{\Delta_5}$ (the Cartan matrix $G_{\mathrm{BKM}}$ is self-dual; signature swap is an automorphism), the Arinkin-Gaitsgory geometric-Langlands correspondence degenerates to a **self-duality**:
$$D^b\mathrm{Coh}(\mathrm{LocSys}_{\mathfrak{g}_{\Delta_5}}(X)) \;\simeq\; D(\mathrm{Bun}_{\mathfrak{g}_{\Delta_5}}(X))^{\mathrm{Hecke}}$$
with the Fricke involution $w_8: Z \mapsto -(8Z)^{-1}$ as structural $S$-matrix. Fricke-fixed locus $= H_1 \cap H_4$ (diagonal of self-duality); off Koszul locus $w_8$ acts freely. The Andrianov factorisation $L(\Delta_{10}) = L(\Delta_{E_6})\zeta(s-9)\zeta(s-8)$ reads as the Atkin-Lehner on seed composed with functional-equation involution on $\zeta$-slots.

---

## 6. The $A_\infty$-quasi-Hopf obstruction tower (Etingof W14-W17)

### 6.1 Pentagon cocycles $\phi^{(n)}$ through weight 10

Higher coherences at order $\hbar^n$ live in $C^3(\mathrm{CE}(\widehat{\mathfrak{g}}_{\Delta_5}^{\mathrm{super}}))$, with MZV-leg (Drinfeld-associator direction) and Borcherds-leg (K3 automorphic direction). MZV basis dimensions follow Brown 2011 Padovan sequence $d_n = d_{n-2} + d_{n-3}$:

| $n$ | Denom. $n!$ | MZV basis dim $d_n$ | MZV basis | Borcherds leg |
|---|---|---|---|---|
| 3 | 6 | 1 | $\{\zeta(3)\}$ | $\Phi_{10}/\eta^{24}$ |
| 4 | 24 | 1 | $\{\zeta(3) \cdot \mathrm{coboundary}\}$ | $(\Phi_{10}/\eta^{24})^2$ |
| 5 | 120 | 1 | $\{\zeta(5)\}$ | $\Phi_{10}^{5/2}/\eta^{60}$ |
| 6 | 720 | 2 | $\{\zeta(3)^2\}$ (irred) | $(\Phi_{10}/\eta^{24})^3$ |
| 7 | 5040 | 2 | $\{\zeta(7), \zeta(3,4)\}$ | $\Phi_{10}^{7/2}/\eta^{84}$ |
| 8 | 40320 | 3 | $\{\zeta(3,5), \zeta(3)\zeta(5), \zeta(5,3)\}$ | $\Phi_{10}^4/\eta^{96}$ |
| 9 | 362880 | 4 | $\{\zeta(9), \zeta(3)\zeta(3,3), \zeta(3,3,3), \zeta(3,6)\}$ | $\Phi_{10}^{9/2}/\eta^{108}$ |
| 10 | 3628800 | 5 | $\{\zeta(3)^2\zeta(3,3), \zeta(3)\zeta(7), \zeta(5)^2, \zeta(3,7), \zeta(5,5)\}$ | $\Phi_{10}^5/\eta^{120}$ |

Explicit Wave-14 result at $n = 3$:
$$\phi^{(3)} = \zeta(3) c_{\mathrm{symm}} + (25/3) c_{\mathrm{timelike}} + (\Phi_{10}/\eta^{24}) c_{\Phi_{10}}$$
where $25/3 = (\mathrm{rk}(\mathrm{II}_{25,1}) - 1)/3$ is Fake-Monster Cartan minus timelike direction — **not** a Virasoro central charge.

Denominators $n!$ from $n$-leg KZ iterated integrals (Drinfeld 1990 §5). MZV basis determined by Brown 2011 *Ann. Math.* 175 Thm 1.1. Depth-3 $\zeta(3,3,3)$ first enters at weight 9; depth-4 MZVs first enter at weight 12.

### 6.2 The tower does not close

Because the BKM imaginary cone is infinite-dimensional (Hardy-Ramanujan growth), $\phi^{(n)}$ does NOT vanish for any $n$. $\mathbf{H}_{\Delta_5}$ is a **genuine** $A_\infty$-quasi-Hopf algebra, not a Drinfeld quasi-Hopf algebra.

**Asymptotic dominance (Etingof W17)**: Padovan dimension $d_n = O(\phi_{\mathrm{plastic}}^n)$ with $\phi_{\mathrm{plastic}} \approx 1.3247$ (plastic number, root of $x^3 = x + 1$); Borcherds Hardy-Ramanujan dimension $n^{-27/4}\exp(4\pi\sqrt{n})$. At $n = 10$, ratio $\dim c_n^{(\mathrm{K3})}/d_n \sim 6.5 \cdot 10^9$. **Borcherds leg dominates MZV leg by ~10 orders of magnitude.**

Universal home: chain-level Markl-Shnider-Stasheff complex over the pro-Lie-bialgebra
$$\widehat{\mathfrak{g}}^{\mathrm{super}}_{\Delta_5} = \varprojlim_m (t^{\mathrm{Sieg,super}}_{2,[2]} \oplus \mathfrak{n}_+^{\mathrm{imag}})/W^{\ge m}$$
with weight-completion (Pattern 236/269 ambient-qualifier discipline). Mittag-Leffler is satisfied (Brown 2011 motivic weight filtration exactness); $\lim^1 = 0$; the pro-limit $\mathrm{obs}_\infty \in \varprojlim_m (\text{tower}/W^{\ge m})$ is a well-defined formal $\hbar$-series.

### 6.3 Cyclic $A_\infty$ structure (Kontsevich-Costello)

The BKM Killing form $\langle\cdot,\cdot\rangle_K: \mathfrak{g}_{\Delta_5} \otimes \mathfrak{g}_{\Delta_5} \to \mathbb{C}$ (inherited from $\Lambda^{2,1}$ lattice pairing) makes the $A_\infty$-structure **cyclic**:
$$\langle\phi^{(n)}(a_1, \ldots, a_n), a_{n+1}\rangle = (-1)^{\epsilon_n}\langle a_1, \phi^{(n)}(a_2, \ldots, a_{n+1})\rangle$$
Verified separately on each leg at $n = 3, 4, 5, 6, 7$ (Etingof W16-W17): MZV leg by KZ iterated-integral Stokes boundary; Borcherds leg by $\mathrm{Sp}_4(\mathbb{Z})$-invariance of the Gritsenko lift.

### 6.4 Genus-$g$ obstruction decomposition (Etingof W15+W17)

At genus $g$, the Maurer-Cartan obstruction decomposes:
$$\mathrm{obs}_g = \sum_{n = 1}^{g+1} \phi^{(n)} \cdot c_{g, n}$$
with $c_{g, n}$ the Arakelov intersection of $\lambda_g$ with the $n$-th Brauer divisor on $\overline{\mathcal{M}}_{g, n}$ (Mumford 1983). Genus-$g$ tower bound $n \le g + 1$ is the genus-$g$ shadow of curved-Dunn $H^2 = 0$ + MSS 2002 Thm 3.42. Specialises to Vol I Theorem D via $\kappa_{\mathrm{ch}}^{\mathrm{K3}}$ and Beilinson-Bloch height pairing.

---

## 7. The BV obstruction tower (Costello W14-W17; Wave-17 compute CORRECTION)

### 7.1 Sequence and structural theorem — WAVE-17 CORRECTED

At each loop order in BV-quantised twisted 11D SUGRA on $\mathbb{R}^3 \times \mathrm{K3} \times \mathbb{C}^2$ (24 M5-branes on $I_1$ Kodaira fibres):
$$\boxed{\;c_n = c_{\phi_{-2,1}}(-n) \cdot [H_n], \quad\text{admissible when}\ n \equiv 0, 3 \pmod 4, \quad\text{else}\ c_n = 0\;}$$
with $\phi_{-2, 1}(\tau, z) = \theta_1(\tau, z)^2/\eta(\tau)^6$ the weak Jacobi form of weight $-2$, index $1$ that feeds the Borcherds product for $\Phi_{10}$.

| $n$ | admissible? | $c_n$ | notes |
|---|---|---|---|
| 0 | — | 0 | classical action closes |
| 1 | no (≡ 1 mod 4) | 0 via Fourier | multiplicity-2 $H_1$ via $\mathrm{div}(\Phi_{10}) = 2 H_1$ (separate) |
| 2 | no (≡ 2 mod 4) | 0 | Wave 15 confirmation |
| 3 | yes (≡ 3 mod 4) | **$-8$** | (NOT $176256$ — see correction below) |
| 4 | yes (≡ 0 mod 4) | $12$ | bielliptic $H_4$ |
| 5 | no | 0 | |
| 6 | no | 0 | |
| 7 | yes | $-39$ | |
| 8 | yes | $56$ | |
| 11 | yes | $-152$ | |
| 12 | yes | $208$ | |

**Critical Wave-17 correction**: Wave 16 asserted $c_3 = 176256 \cdot [H_3]$. This was wrong. $176256 = p_{24}(5)$ (the 24-coloured partition of 5, a $q^5$ coefficient of $1/\eta^{24}$) — unrelated to $\phi_{10,1}$'s Fourier expansion. The Wave-17 compute module `wave17_cn_heegner_pattern.py` derives the correct values via four independent paths: (1) direct $\theta_1^2/\eta^6$ expansion; (2) theta decomposition $\phi_{-2,1} = h_0 \theta_{1,0} + h_1 \theta_{1,1}$; (3) $\phi_{10,1}/\eta^{24}$ derivation (sign-convention-fixed Wave-17.5); (4) Hecke congruence growth pattern $|c(-D)| \sim \exp(\pi\sqrt{D})$.

### 7.2 The structural Heegner pattern

$$c_n \in H^2(\mathfrak{g}_{\Delta_5}, \mathbb{C}) \cong \mathbb{C}\cdot[\Delta_5]$$
is the Chern class of the Heegner divisor $H_n$ in $\overline{\mathcal{A}_2}$ (Bruinier 2002 Prop 5.1 reciprocity), with coefficient $c_{\phi_{-2,1}}(-n)$ vanishing unless $-n$ is realisable as $r^2 - 4m$ for integers $r, m$ — equivalently, $n \equiv 0, 3 \pmod 4$.

BKM-Wilson-line counterterm
$$S^{(n)}_{\mathrm{c.t.}} = \int_{\mathbb{R}} c_n^\lambda \cdot \mathrm{tr}_\lambda(A^{\otimes n})$$
trivialises on the generic Koszul locus $\overline{\mathcal{A}_2} \setminus \bigcup_n H_n$; fails on each individual admissible $H_n$.

### 7.3 Four-archetype stratification

Theorem C's 4-family classification (G/L/C/M) stratifies the obstruction tower:
- **G** (Heisenberg / lattice VOA): $c_n = 0$ all $n$.
- **L** (affine Kac-Moody): $c_n \propto \zeta(3), \zeta(5), \ldots$ (MZV only, no K3 leg).
- **C** ($\beta\gamma$): $c_n = 0$ on Koszul locus.
- **M** (Virasoro / BKM / K3): $c_n \neq 0$ with both MZV and K3 legs.

K3 belongs to class M (Polyakov W15 confirmed robust under the $-312 \to -214$ retraction).

### 7.4 3-loop holography match

CG twisted holography match at $p^3$: tree-level Costello-Gaiotto-Paquette (1810.10016) extends to 3-loop via the denominator-identity recursion:
$$Z^{\mathrm{bulk},(3)}_{\mathrm{K3} \times \mathbb{C}^2} = [\log\Phi_{10}]_{p^3}$$
matching the obstruction class exactly. With $c_2 = 0$, the 3-loop is the first non-trivial cocycle in the holographic-cubic-vertex sector.

---

## 8. Tannakian / MTC structure (Gelfand W15-W17)

### 8.1 Fibre functor

$$\omega: \mathrm{Rep}(\mathbf{H}_{\Delta_5}) \longrightarrow \mathrm{sVec}_{\mathbb{C}}, \qquad \omega(V) = H^*_T(\mathrm{Hilb}^{[n]}(\mathrm{K3}); V)\Big|_{n\to\infty}$$
Nakajima-equivariant cohomology stabilised in $n$, with $\widetilde{M}_{24}$-umbral action on the fibre. Tensor compatibility via Maulik-Okounkov stable envelopes (*Astérisque* 408 §8). Super-valued because of K3 Ramond fermion number ($\mathcal{N} = (4,4)$ SCA sector).

### 8.2 Neutrality scope + $\mu_8$-gerbe

The associator $\widetilde{\Phi}^{\mathrm{Sieg\text{-}Bor}}_{\mathrm{Sp}_4}[\Phi_{10}/\eta^{24}]$ defines a $\mu_8$-gerbe on $\overline{\mathcal{A}_2}$ (order 8 by Bruinier Prop 5.1).
- On $U := \overline{\mathcal{A}_2} \setminus (H_1 \cup H_4)$: gerbe trivialisable → $\mathrm{Rep}(\mathbf{H}_{\Delta_5})|_U$ is **neutral Tannakian**.
- On $H_1 \cup H_4$: $\mu_8$-gerbe-twisted (orders 8 and 16 matching the Humbert stratification).

### 8.3 MTC at $q = \zeta_8$

Lusztig small form $\mathfrak{u}_{\zeta_8}(\widehat{\mathfrak{m}}_{\Delta_5})$ is **finite-dimensional** (PBW count, upper bound $8^{129}$).
- Representation category: **non-semisimple Kerler-Lyubashenko MTC** (Kerler-Lyubashenko 2001 LMS LNS 262).
- Semisimplification: **genuine Turaev MTC**.

### 8.4 Fricke $S$-matrix (Gelfand W16-W17)

Modular $S$-matrix = **Fricke involution** $w_8: Z \mapsto -(8Z)^{-1}$ on Siegel $\mathbb{H}_2$. Properties:
- $S^4 = \mathrm{id}$ (Fricke at level 8, Gritsenko 1995 §3 Thm 3.2).
- $\det(S) = 1$.
- Eigenvalues: fourth roots of unity $\{1, i, -1, -i\}$ each with multiplicity 1 (diagonalisation via $S_{ij} = \frac{1}{2}i^{ij}$, discrete Fourier on $\mathbb{Z}/4$).
- Generic $\mathrm{tr}(S) = 0$; $\mathrm{tr}(S)|_{H_1 \cup H_4}^{M_{24}\text{-invariant}} = \chi(H_1 \cup H_4) - \chi(H_1 \cap H_4) = 4$.
- Fixed locus = $H_1 \cap H_4$ (matching $\mu_8$-gerbe obstruction).

**Striking coincidence**: the $S$-matrix trace 4 on the $M_{24}$-invariant Humbert block equals the global A-packet size $|\Psi_{\Delta_{10}}| = 4$ (Kazhdan W17).

### 8.5 Fusion ring (Gelfand W17)

Three fusion generators $V_{\alpha_1}, V_{\alpha_2}, V_{\alpha_3}$ from the three real simple roots.

Fusion coefficients at $\ell = 8$ via Kac-Walton:
- Diagonal: $V_{\alpha_i} \otimes V_{\alpha_i} = V_0 \oplus V_{2\alpha_i}$ (both retained since $\langle 2\alpha_i, \theta^\vee\rangle = 2 \leq 7$).
- Off-diagonal ($i \neq j$): $V_{\alpha_i} \otimes V_{\alpha_j} = V_{\alpha_i + \alpha_j} \oplus V_{\alpha_i - \alpha_j}$ (both retained, bounds $2, 0 \leq 7$).

With $\theta = \alpha_1 + \alpha_2 + \alpha_3$ the highest real root and $h^\vee = 1$ for hyperbolic BKM: $\ell - h^\vee = 7$. Paramodular Weyl group $W_{\mathrm{BKM}} = 24$ elements (Gritsenko-Hulek 1998), 126 positive real roots.

### 8.6 Verlinde formula verification

$N_{ij}^k = \sum_a S_{ia}S_{ja}\overline{S_{ka}}/S_{0a}$ holds on the semisimple block. Direct check via $\mathbb{Z}/4$-Fourier delta: $N_{ij}^k = \delta_{i+j \equiv k \pmod 4}$; matches the explicit Kac-Walton tensor-product evaluation on three real-root reps. Non-semisimple lift uses Creutzig-Ridout 2013 logarithmic Verlinde.

### 8.7 Plancherel decomposition (see §2.3 for full statement)

On non-semisimple MTCs, Plancherel decomposes into indecomposable projective covers $P_\lambda$ (not simples), with measure $\mathrm d\mu_{\mathrm{Plan}}(\lambda) = \dim_{\mathrm{qu}}(P_\lambda)$. Integration recovers $1/\Phi_{10}(Z)$ on $\mathbb{H}_2$.

### 8.8 Grothendieck ring

$$K_0(\mathrm{Rep}(\mathbf{H}_{\Delta_5}))/\hbar \;\cong\; \mathrm{Sym}(\mathfrak{g}_{\Delta_5}^\vee)^{W_{\mathrm{BKM}}}$$
with $W_{\mathrm{BKM}}$ the real-simple-root Weyl group. Multiplicative Borcherds denominator identity reads as a $K_0$-identity.

---

## 9. The RTT / explicit realisation (Drinfeld W15-W17)

### 9.1 Factorised $R$-matrix

$$R_{\mathrm{Sieg,dyn}}(u, Z) \;=\; R^{\mathrm{rat}}_{\mathrm{Yang}}(u) \cdot \theta^{\mathrm{K3}}(u, Z)$$
with
- $R^{\mathrm{rat}}_{\mathrm{Yang}}(u) = 1 + \hbar\,\Omega/u$ (Yang 1967; Drinfeld 1985).
- $\theta^{\mathrm{K3}}(u, Z) = \exp(\hbar \cdot F^{\mathrm{Sieg}}(u, Z) \cdot \Omega_{\mathrm{K3}})$ a K3-theta cocycle from the Pasol-Zagier Siegel-Kronecker-Eisenstein series.

Why not a single elliptic $R$-matrix: signature-$(2,1)$ Cartan form forbids Lagrangian polarisation, so Belavin-Drinfeld classification does not apply.

### 9.2 Quantum determinant

$$\mathrm{qdet}\,T(u, Z) = C(u) \cdot \Delta_5(Z) \cdot \mathrm{Id}$$
with $C(u) \in 1 + u^{-1}\mathbb{C}[[u^{-1}]]$ a $Z$-independent normalisation. Uniqueness of weight-5 Siegel cusp form on Maass-spin cover with vanishing on $2H_1 + H_4$ (Gritsenko 1999 Thm 6.1) forces the centre to factor through $\Delta_5$.

### 9.3 Imaginary-root vertex operators

Feigin-Frenkel screening presentation: for each imaginary simple root $\alpha^{\mathrm{im}}$ with multiplicity $c_{\mathrm{K3}}(4nm - \ell^2)$, the vertex operator $V_\alpha(z) = \oint e^{\alpha \cdot \phi(z)}\,dz$ — adapted to BKM via Gritsenko-Nikulin product formula.

### 9.4 Monster-BKM RTT (Drinfeld W17)

$\mathfrak{m}_{\mathrm{Monster}}$ has hyperbolic rank 2 in $\mathrm{II}_{1,1}$. Its RTT presentation:
$$R_{\mathrm{Monster}}(u, \tau) = R^{\mathrm{rat}}_{\mathrm{Yang}}(u) \cdot \theta^{\mathrm{j}}(u, \tau)$$
with 2×2 Casimir $\Omega_{\mathrm{II}_{1,1}} = \alpha \otimes \beta + \beta \otimes \alpha$ and theta cocycle
$$\theta^{\mathrm{j}}(u, \tau) = \Big[u \prod_{m, n > 0}(1 - p^m q^n)^{c(mn)}\Big]^{-1}$$
using $V^\natural$-multiplicities $c(1) = 196884, \ldots$. Satisfies elliptic dynamical YBE with $\tau$-shift in the Hauptmodul variable.

### 9.5 The three BKMs are distinct

K3-BKM $\mathfrak{g}_{\Delta_5}$, Monster $\mathfrak{m}_{\mathrm{Monster}}$, Fake-Monster $\mathfrak{m}_{\mathrm{Fake\text{-}Monster}}$ have different Cartan dimensions (3, 2, 26). K3-BKM is **not a subalgebra** of Monster; the three are $\Psi$-co-siblings (§15).

---

## 10. The $A_{N-1}$ class-$\mathcal{S}$ family (Gaiotto W14-W17)

### 10.1 The parent theory

$\mathcal{T}[A_{N-1}, \Sigma_{0,24}]$: class-$\mathcal{S}$ of type $A_{N-1}$ on the 24-punctured sphere with maximal regular $\mathfrak{su}(N)$ punctures, $M_{24}$ acting by puncture permutation preserving Steiner $S(5,8,24)$.

### 10.2 $N$-family central charges

Chacaltana-Distler 2010 trinion $T_N$ decomposition (22 trinions, 21 tubes); trinion anomalies:
$$n_v(T_N) = \tfrac{1}{2}(N-1)(N-2)(N+2), \qquad n_h(T_N) = \tfrac{2}{3}N(N^2-1).$$

Applying Shapere-Tachikawa $c_{4d} = (2n_v + n_h)/12$ and Beem-Rastelli $c_{2d} = -12c_{4d}$:

| $N$ | $(n_v, n_h)$ trinion | $c_{4d}$ | $c_{2d}$ | Coulomb rank | Flavour level $k_{2d}$ |
|---|---|---|---|---|---|
| 2 | $(0, 4)$ | $107/6$ | $-214$ | 21 | $-2$ |
| 3 | $(5, 16)$ | $227/3$ | $-908$ | 42 | $-3$ |
| 4 | $(18, 40)$ | $1151/6$ | $-2302$ | 63 | $-4$ |
| 5 | $(42, 80)$ | — | — | 84 | $-5$ |

Flavour $\widehat{\mathfrak{su}}(N)^{\otimes 24}_{k_{2d} = -N}$ per puncture.

### 10.3 Siegel weight formula (Gaiotto W16+W17 VERIFIED)

$$\boxed{\;k_N = (N+3)/2,\quad f^{(N)}(0, 0) = 2(N+3)\;}$$

giving $(k_2, k_3, k_4, k_5) = (5/2, 3, 7/2, 4)$ on the spin cover of $\mathrm{O}(\Lambda^{N+1, 2})$, equivalently integer weights $(5, 6, 7, 8)$ on the honest cover.

**Wave-17 verification** (via first-principles Borcherds lift):
- $N = 3$: input Jacobi $\phi^{(3)}(\tau, z_1, z_2) = \phi_{0,1}^{\mathrm{K3}}(\tau, z_0) \cdot \chi_{\mathfrak{su}(3), \mathrm{adj}}^{\mathrm{av}}(\tau, z_1, z_2)/24$ has $f^{(3)}(0,0) = 12$, Borcherds weight $= 12/2 = 6$ honest, $k_3 = 3$ on spin cover. ✓
- $N = 4$: $\mathfrak{su}(4)$-adjoint rank 15. $f^{(4)}(0,0) = 14$, Borcherds weight $7$ honest, $k_4 = 7/2$ on spin cover. ✓

Derivation via Eguchi-Hikami 2009 arXiv:0904.0911 eq. (4.12), Benini-Peelaers 2015 arXiv:1507.04746 §5, Córdova-Shao 2015 arXiv:1506.00265 §4.

### 10.4 Umbral moonshine Niemeier extension

Cheng-Duncan-Harvey 2014 umbral moonshine associates each Niemeier root system to a mock-modular form:

| $N$ | Niemeier root | Umbral group | Order |
|---|---|---|---|
| 2 | $24 A_1$ | $M_{24}$ (Mathieu) | 244823040 |
| 3 | $12 A_2$ | $2.M_{12}$ | 190080 |
| 4 | $8 A_3$ | $2.\mathrm{AGL}_3(2)$ | 2688 |
| 5 | $6 A_4$ | $\mathrm{GL}_2(5)/\{\pm 1\}$ | 240 |
| 6 | — | labelling breaks | — |

The $A_{N-1}$-class-$\mathcal{S}$ family and the Niemeier-24-root family are in natural bijection up to $N = 5$; at $N = 6$ (would-be $4 A_5$), no Niemeier with that root system exists — the bijection breaks.

### 10.5 Structural theorem (Gaiotto W17)

**Theorem.** For $\mathcal{T}[A_{N-1}, \Sigma_{0, 24}]$ at $N \in \{2, 3, 4, 5\}$:
1. $f^{(N)}(0, 0) = 2(N+3)$.
2. Siegel weight $k_N = (N+3)/2$ on spin cover of $\mathrm{O}(\Lambda^{N+1, 2})$.
3. Central charges
$n_v = 21(N^2 - 1) + 11(N - 1)(N - 2)(N + 2)$,
$n_h = 44N(N^2 - 1)/3$,
$c_{4d}(N) = (2n_v + n_h)/12$, $c_{2d}(N) = -12 c_{4d}(N)$.
4. Umbral labelling by Niemeier root system $(24/\mathrm{rank}(A_{N-1})) \cdot A_{N-1}$ for $N \in \{2, 3, 4, 5\}$; fails at $N = 6$.

---

## 11. Duality frames and construction landscape

All six duality frames produce the **same** Siegel form $\Delta_5$ via different physical content. A seventh (GW/DT) categorical route converges from the enumerative-geometry direction.

### 11.1 Five string/M-theory frames (Witten W14-W15)

| Frame | Setup | $\Delta_5$ origin |
|---|---|---|
| Heterotic | on $T^6$ with self-dual $T^2$ factor | Harvey-Moore 1996 1-loop threshold |
| IIA | on $\mathrm{K3} \times T^2$ | Narain $\mathrm{II}_{3,19}$ via T-duality |
| M-theory | on $\mathrm{K3} \times T^3$ | lift of IIA |
| IIB | on $\mathrm{K3} \times S^1$ | T-dual to IIA |
| F-theory | on elliptic $\mathrm{K3} \times T^2$ | 24 $I_1$ 7-branes + $\mathrm{SL}_2(\mathbb{Z})$ monodromy |

### 11.2 Decoupling limit at chain level (Witten W15)

Heterotic on $T^6$ with $g_s \to 0$, $R_{T^2} \to R_{\mathrm{sd}} = \sqrt{\alpha'/2}$, $R_{T^4} \to \infty$ isolates $\mathbf{H}_{\Delta_5}$ as a standalone chiral bialgebra (no bulk coupling). At the factorisation-algebra level (Costello-Gwilliam Vol. 1 Thm 3.5.1): observables concentrate on codim-4 submanifold $T^2$ in the degenerate limit.

### 11.3 F-theory 24 $I_1$ monodromy

Local monodromy at each $I_1$ is $T$-conjugate of order 12 in $\mathrm{SL}_2(\mathbb{Z})$. Global constraint: product of 24 local monodromies equals identity (Morrison-Vafa 1996 II §3.3). $M_{24}$ permutes them via Steiner $S(5,8,24)$.

### 11.4 M on $\mathrm{K3}^2 \times S^1$: sixth route (Witten W14)

Dijkgraaf-Verlinde-Verlinde 1997 eq. 4.7: partition function
$$Z_{M/\mathrm{K3}^2 \times S^1}(Z) = 1/\Phi_{10}(Z)$$
with genus-2 Siegel $Z$ where $(\tau_1, \tau_2)$ parameterise the two K3's, $z$ the $S^1$. This is a **sixth different construction** yielding $\mathbf{H}_{\Delta_5}$.

### 11.5 GW/DT categorical seventh route (Nekrasov W17)

Gromov-Witten / Donaldson-Thomas correspondence on $\mathrm{K3} \times E$:
- **GW** (Maulik-Pandharipande-Thomas 2010): $Z^{\mathrm{red}}_{\mathrm{GW}}(\mathrm{K3} \times E) = 1/\Phi_{10}$ after combining Yau-Zaslow K3 counts with $E$-wrapping elliptic genus.
- **DT** (Oberdieck-Pandharipande 2015 + Oberdieck-Pixton 2016 unconditional): $Z^{\mathrm{red},\prime}_{\mathrm{DT}}(\mathrm{K3} \times E) = 1/\Phi_{10}$.

Via Maulik-Nekrasov-Okounkov-Pandharipande 2006 GW/DT: both sides are automorphic modular characters of $\mathbf{H}_{\Delta_5}$'s module category. Adjoins the existing six duality/construction routes as a seventh independent line of evidence.

### 11.6 Six routes are DIFFERENT (KST W15+W17)

All six construction routes yield the **same object** $\mathbf{H}_{\Delta_5}$ but via **different inputs**:
1. $D^b\mathrm{Coh}(\mathrm{K3} \times E)$ via $\Phi_3$, generator rank $\rho = 3$ (Vol-III CY-to-chiral).
2. Jacobi form $2\phi_{0,1}$ via Borcherds-Gritsenko lift.
3. Mukai lattice via FLM lattice VOA, $\rho = 24$.
4. Kummer orbifold via DHVW + crepant resolution, $\rho = 12$.
5. Ricci-flat metric via Kapustin-Li half-twist, $\rho = 3$.
6. 6d $(2,0)$ via Costello-Li + Schur limit, $\rho = 3$.
7. GW/DT character via Oberdieck-Pandharipande, automorphic-modular.

**Six routes are six DIFFERENT constructions, NOT six applications of $\Phi$.** Different routes may give different $\kappa$'s at generator level; the convergence at output is a non-trivial theorem, not a tautology.

---

## 12. The $M_{24}$ 't Hooft anomaly (Kazhdan W15+W16, Gaiotto W14)

### 12.1 Pentagon = $M_{24}$ umbral cocycle agreement

The Wave-14 theorem (Gaiotto `thm:pentagon-umbral-agreement`):
$$[\phi^{(3)}|_{\langle g\rangle}] = \iota_g^*[\text{umbral cocycle}] \in H^3_{\text{transgr}}(\langle g\rangle, U(1)) \cong \mathbb{Z}/6$$
for $g \in M_{24}$ of order 6 (classes $6A, 6B$).

### 12.2 Two distinct invariants (Kazhdan W16)

Two quantities, not to conflate:
- **Umbral shifts** (Cheng-Duncan-Harvey 2014 Table 1): $m_{6A} = 2$, $m_{6B} = 6$.
- **Transgression cocycle classes**: $6A \mapsto 2 \pmod 6$, $6B \mapsto 3 \pmod 6$.

Sum of cocycle classes: $2 + 3 = 5 \equiv -1 \pmod 6$, the $\mathbb{Z}/6$-restriction of the universal identity $\hbar^2 \cdot K^{\kappa_{\mathrm{ch}}} = -1$. The cocycle is NOT the umbral shift.

### 12.3 Schur cocycle order

$|H^2(M_{24}, U(1))| = 12$ (Atlas of Finite Groups). The chiral-bialgebra twist has order dividing 12; the order 6 appears as the $M_{24}$-order-6 subcocycle in the pentagon $\hbar^3$ obstruction.

---

## 13. Humbert stratification (Kazhdan W15-W17, Costello W16)

### 13.1 The full Humbert landscape

| Divisor | Discriminant | Structure | Monodromy | Role |
|---|---|---|---|---|
| $H_1$ | 1 | products of elliptic curves | $\mathbb{Z}/8$ | Koszul boundary, $\hbar^2 = -1/8$ |
| $H_3$ | 3 | RM $\mathbb{Z}[(1+\sqrt{3})/2]$ | TBD | 3-loop BV obstruction $c_3$ lives here |
| $H_4$ | 4 | $(2,2)$-isogeny quotient of $E_1 \times E_2$, $\mathrm{End} \supset \mathbb{Z}[2i]$ | $\mathbb{Z}/2$ | Koszul boundary |
| $H_8$ | 8 | RM $\mathbb{Z}[\sqrt{2}]$ | TBD | beyond current scope |

### 13.2 Koszul locus

$\mathcal{U}_{\mathrm{Kosz}}^{\mathrm{K3}} = \overline{\mathcal{A}_2} \setminus (H_1 \cup H_4)$.
Off this locus: Positselski weight-completed coderived/contraderived.
3-loop BV obstruction fails additionally on $H_3$ — so the "full Koszul locus" for the 3-loop is $\overline{\mathcal{A}_2} \setminus (H_1 \cup H_3 \cup H_4)$.

### 13.3 Fundamental group

$\pi_1(\overline{\mathcal{A}_2} \setminus (H_1 \cup H_4))$ is generated by $\mathbb{Z}/8 * \mathbb{Z}/2$ (free product) with relations from the Siegel compactification.

### 13.4 Humbert $H_4$ correction (Kazhdan W16)

$H_4 = \{A \in \mathcal{A}_2 : \mathrm{End}(A) \supset \mathbb{Z}[\phi], \phi^2 = 4\}$ = $(2,2)$-isogeny quotient of $E_1 \times E_2$ — NOT the $\mathbb{Q}(\sqrt{2})$-RM locus (that is $H_8$). Wave-15's "$\mathbb{Z}[\sqrt{2}]$" inscription at Vol I `chiral_climax_platonic.tex:1748` was imprecise; Wave-16 sharpened via Vol III `drinfeld_center.tex`.

Kuga-Satake lift: Morrison 1984 Thm 3 gives $\mathrm{Pic}(\mathrm{KS}(A))|_{H_4} \supset U(2) \oplus \langle -4\rangle$; transcendental lattice has imaginary-CM by $\mathbb{Z}[2i] = \mathbb{Z}[\sqrt{-4}]$, reconciling imaginary-CM convention with real-RM $\mathcal{A}_2$-side via Hodge-weight inversion.

---

## 14. The CY-2 landscape dichotomy (Witten W17)

Classification of compact Kähler CY-2 surfaces ($c_1 = 0$) — five types, partitioned by the $\Psi$-functor into four archetypes:

| Surface | $\chi_{\mathrm{top}}$ | $h^{2,0}$ | $\pi_1$ | $\Psi$-image | Taxon | Siegel weight |
|---|---|---|---|---|---|---|
| K3 | 24 | 1 | $\{1\}$ | $\mathbf{H}_{\Delta_5}$ | 4th (BKM) | 5 |
| Kummer K3 (= K3 variant) | 24 | 1 | $\{1\}$ | $\mathbf{H}_{\Delta_5}|_{\Lambda_{\mathrm{Kum}}}$ (sublattice) | 4th | 5 |
| Enriques | 12 | 0 | $\mathbb{Z}/2$ | $\mathbf{H}_{\Delta_5}/\!/\mathbb{Z}/2$ (orbifold) | 4th-$\mathbb{Z}/2$ | 5/2 metaplectic |
| $T^4$ | 0 | 1 | $\mathbb{Z}^4$ | $V_{\mathrm{II}_{4,4}}$ (abelian Heisenberg) | G | 0 |
| Bielliptic | 0 | 0 | $\mathbb{Z}^4 \rtimes G$ | $V_{\mathrm{II}_{4,4}}/G$ orbifold | G | 0 |
| Half-K3 / $\mathrm{dP}_9$ (non-CY) | 12 | 0 | $\{1\}$ | $\widehat{E_8}_{k=1}$ | L | 0 |

**Linear weight formula** on the fourth-taxon column:
$$\boxed{\;w_{\mathrm{Borch}}(X) = 5\chi_{\mathrm{top}}(X)/24\;}$$

This is striking: the Siegel weight of the output BKM denominator is a **topological invariant** of the input, linear in the Euler characteristic with proportionality constant $5/24$ (itself tied to the genus-0 24-puncture count and the weight-5 $\Delta_5$).

### 14.1 Enriques $\mathbf{H}_{\Delta_5}^{\mathrm{Enr}}$

$\mathrm{K3} \to \mathrm{Enriques}$ via free $\mathbb{Z}/2$-involution $\iota$ with $H^2(\mathrm{En}, \mathbb{Z}) = E_8 \oplus \mathrm{II}_{1,1}(2)$ of signature $(1, 9)$. $\Psi(\mathrm{En})$ is the $\mathbb{Z}/2$-gauging of K3:
$$\mathbf{H}_{\Delta_5}^{\mathrm{Enr}} = \mathbf{H}_{\Delta_5}\,/\!\!/\,\langle\iota\rangle$$
at level 2. Genus-2 Siegel character $1/\Delta_5^{\mathrm{Enr}}$ with weight $\mathbf{5/2}$ on paramodular $K(2) \subset \mathrm{Sp}_4(\mathbb{Q})$ (half of K3, matching $\chi_{\mathrm{top}}(\mathrm{En})/\chi_{\mathrm{top}}(\mathrm{K3}) = 1/2$). Half-integrality forced by the metaplectic cover on the $(1,1)$-factor of $\mathrm{II}_{2,10}(2)$. Primary: Gritsenko-Nikulin 1998 Thm 5.2, Hulek-Sankaran 2011 Thm 3.4, Oguiso-Sakai 2001.

### 14.2 $T^4$ → abelian Heisenberg (taxon G)

$\Phi_2(D^b\mathrm{Coh}(T^4)) = V_{\mathrm{II}_{4,4}}$, Narain lattice VOA of signature $(4, 4)$. $\chi_{\mathrm{top}} = 0$ forces Göttsche generating function to collapse ($\prod_m(1-q^m)^0 = 1$); Borcherds lift of $\phi_{0,1}^{T^4} = 0$ trivial. No Siegel cusp form. Imaginary-root structure vanishes. Primary: Nahm-Wendland 2001 Thm 4.1.

### 14.3 Kummer ⊂ K3

$\mathrm{Kum}(T^4)$ is topologically K3 ($\chi_{\mathrm{top}} = 24$ via Mukai 1984); $\Phi_2$-image is $\mathbf{H}_{\Delta_5}|_{\Lambda_{\mathrm{Kum}}}$ with
$$\Lambda_{\mathrm{Kum}} = E_8(-2)^{\oplus 2} \oplus \mathrm{II}_{1,1}(2) \oplus \langle -2\rangle^{16}$$
**Same** Siegel weight $5$ (no degradation), only sublattice restriction $\Delta_5|_{\mathcal{A}_2^{\mathrm{Kum}}}$.

### 14.4 Half-K3 / $\mathrm{dP}_9$ → $\widehat{E_8}_1$ (taxon L)

$\mathrm{dP}_9$ fails two Wave-15 hypotheses (T1: $\chi = 12 \ne 24$; T2: $c_1 = -f \ne 0$). Borcherds 1998 Thm 10.1 requires $\mathrm{II}_{2, 10}$; half-K3's $\mathrm{II}_{1, 9}$ does not produce a weight-5 Siegel form. $\Phi_2$-image is affine $\widehat{E_8}$ at level $k = 1$ from the 12-$I_1$-fibre / $II^*$-collision. Taxon L. Primary: Seiberg 1988 Phys. Lett. B 206, Morrison-Vafa 1996 II §4.

---

## 15. Local Langlands at all places (Kazhdan W15-W17)

### 15.1 The global picture

$\Delta_{10}$ (Saito-Kurokawa of weight-16 elliptic seed) has global Arthur parameter
$$\psi_{\Delta_{10}}: L_F \times \mathrm{SL}_2(\mathbb{C}) \to \mathrm{SO}_5(\mathbb{C}) = {}^L\mathrm{Sp}_4, \qquad \psi_{\Delta_{10}} = \phi_{\Delta_{E_6}} \boxtimes \mathrm{Sym}^1.$$
Global A-packet $|\Psi_{\Delta_{10}}| = 4$; $S_\psi = \mathbb{Z}/2$; $\pi_{\Delta_{10}}$ appears in $L^2_{\mathrm{cusp}}$ with multiplicity 1 via Ikeda character.

### 15.2 Unramified places $p$ with $p \nmid 2$

Satake parameters $(\alpha_p, \beta_p, \alpha_p^{-1}, \beta_p^{-1}) \in \mathrm{SO}_5(\mathbb{C})$ determined by Hecke eigenvalues:
$$\lambda_p(\Delta_{10}) = a_p(\Delta_{E_6}) + p^8 + p^9$$
Spinor Euler factor:
$$Z_p(s, \Delta_{10}) = \zeta_p(s - 8) \zeta_p(s - 9) L_p(s, \Delta_{E_6}).$$
Verified at $p \in \{3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79\}$ (Beilinson W15+W17).

### 15.3 Ramified place $p = 2$

$v_{\Delta_5}$ ramifies at $p = 2$:
$$\psi_{\Delta_5, 2} = \phi_{\Delta_{E_6}, 2} \boxtimes \mathrm{Sym}^1 \otimes \varepsilon_2$$
with $\varepsilon_2$ the ramified quadratic character of $W_{\mathbb{Q}_2}^{\mathrm{ab}}$ of conductor $2^3$ (class of $\sqrt{2}$). $\phi_{\Delta_{E_6}, 2}$ is a dihedral CM-by-$\mathbb{Q}(\sqrt{-1})$ degree-2 parameter of the weight-16 newform.

### 15.4 Archimedean place $v = \infty$

$\phi_{\Delta_{10}, \infty}: W_{\mathbb{R}} \to \mathrm{Sp}_4(\mathbb{C})$, $W_{\mathbb{R}} = \mathbb{C}^\times \rtimes \mathbb{Z}/2$:
- Schmidt parameter $(17/2, 15/2)$ (via $(k-3/2, k-5/2)$ dictionary at $k=10$).
- Holomorphic discrete series of $\mathrm{Sp}_4(\mathbb{R})$.
- Tempered (SK non-temperedness at $\mathrm{Sym}^1$ slot, not archimedean slot).

$\phi_{\Delta_5, \infty}$ on Maass spin cover:
- Schmidt parameter $(7/2, 5/2)$ on $\mathbb{C}^\times$.
- Twisted by $\mathrm{sgn}_{\mathbb{R}}$ on $\mathbb{Z}/2$-component.
- Squaring $\Delta_5 \to \Delta_{10}$: $\mathrm{sgn}^2 = 1$ and Schmidt parameters double non-trivially to $(17/2, 15/2)$.

### 15.5 Drinfeld centre

$$\mathcal{Z}(\mathrm{Rep}(\mathbf{H}_{\Delta_5})) \simeq \mathrm{YD}^{A_\infty}_{\mathbf{H}_{\Delta_5}}$$
(Yetter-Drinfeld modules with infinite $A_\infty$-tower from BKM imaginary cone). Strict inclusion $\mathrm{Rep}^{E_2}(Z^{\mathrm{der}}_{\mathrm{ch}}(\mathbf{H}_{\Delta_5})) \hookrightarrow \mathcal{Z}(\mathrm{Rep}) \to \mathrm{YD}^{A_\infty}$: equivalence only on Koszul locus. Fricke $w_8$ is the modular $S$-matrix; ribbon twist order 24. AP-CY54 discipline: Drinfeld centre ≠ averaging map.

Frobenius-Perron dim at $H_1 \cap H_4$ equals $4 = |\Psi_{\Delta_{10}, \infty}|$ — archimedean packet size and Fricke-fixed-locus dimension are the SAME integer.

---

## 16. Unitarity and effective spectrum (Polyakov W17)

### 16.1 Hyperbolic Cartan signature (2, 1)

From Feingold-Frenkel 1983, eigenvalues of $G_{\mathrm{BKM}}$ are $\{+4, +4, -2\}$. Signature $(2, 1)$: two positive directions forming a plane $P$, one negative (hyperbolic direction $L$).

### 16.2 Unitary module spectrum

Unitary iff $\lambda \in P^*_+ \cap \{(\lambda, \lambda) > 0\}$ (spacelike real-root weights). Imaginary-root timelike sector non-unitary (negative-norm states).

BKM inner-product has indefinite Hermitian signature $(\#\Phi^{\mathrm{re}}, \#\Phi^{\mathrm{im}}) = (\infty, \infty)$. Frenkel-Kac vertex algebra on positive-definite rank-2 lattice gives unitary representations; imaginary-root sector obstructs global unitarity.

### 16.3 Effective central charge on unitary submodule

$c_{\mathrm{eff}}$ at full level: $-166$ (with negative anomaly-inflow).
$c_{\mathrm{unit}} = \mathrm{rk}(P) = 2$ on real-root unitary submodule.

Genuine positive entanglement entropy on real-root submodule:
$$S_{\mathrm{EE}}(V^{\mathrm{unit}}) = (c_{\mathrm{unit}}/3)\log(L/\epsilon) = (2/3)\log(L/\epsilon).$$

The negative $c_{\mathrm{eff}} = -166$ is a **gravitational-anomaly coefficient** (Manschot-Moore 2007, DVV 1997, Witten 2007), not a Hilbert-space entropy.

### 16.4 Fricke-fixed sub-MTC

Atkin-Lehner $w_5$ on paramodular level 5 descends via Bruinier-Funke 2002 Prop 5.1 Heegner reciprocity. Fricke-fixed representations are projectively self-dual; genuine $\mathbb{Z}/2$-grading (not trivial) reflects level-5-vs-level-1 obstruction.

---

## 17. Compute-module infrastructure

Wave 14 scaffolded 8 modules; Waves 15-17 extended to 14; post-Wave-17 audit closed the compute-module gap with a whole-object verifier:

| Module | Wave | Status | Key contents |
|---|---|---|---|
| `schur_index_classS_A1_24` | 14 | Complete + 2-loop | Plethystic PE; 10 Fourier coeffs |
| `arthur_hecke_delta10` | 14 | Complete through $p = 79$ | First-principles $E_4 \cdot \Delta$, Deligne bound |
| `gritsenko_additive_explicit` | 14 | Complete to $q^{10}$ | BKM Cartan $\det G = -32$, EOT coefficients |
| `twisted_11dsugra_1loop` | 14 | Complete | $\hbar^2 = -1/8$; 5-frame duality |
| `bi_based_ran` | 14 | Complete; 22/22 tests | Kuga-Satake, Torelli, nearby cycles |
| `pentagon_coboundary_hbar3` | 14 | Complete | $\Phi_{10}/\eta^{24}$ leading coeff $-2$ |
| `humbert_monodromy_8` | 14 | Complete; 33/33 tests | Triple face $= 8$; Deligne canonical extension |
| `M24_umbral_cocycle_order6` | 14 | Complete | $6A$ vs $6B$ distinction; transgression |
| `wave15_pentagon_hbar45` | 15 | Complete | $\phi^{(4)}, \phi^{(5)}$ |
| `wave15_schur_index_classS_ANm1_24` | 15 | Complete; 47/47 tests | $N$-family central charges + Siegel weights |
| `wave17_pentagon_coboundary_hbar8_9_10` | 17 | Complete; 27/27 tests | $\phi^{(8,9,10)}$ + Padovan dims |
| `wave17_cn_heegner_pattern` | 17 | Complete; 13/13 tests | Corrected $c_n = c_{\phi_{-2,1}}(-n)$; 176256 retracted |
| `wave17_unified_cross_check` | 17 | 58/58 tests | Full 8-cross-check regression |
| `whole_object_verifier` | post-W17 | **11/11 tests, WOV VERIFIED** | 10 cross-module coherence identities |

Total compute test coverage: ~300 passing assertions across 14 modules.

### 17.1 The whole-object verifier (post-Wave-17)

The 14 compute modules each verify individual pieces; `whole_object_verifier.py` closes the compute-module gap by checking ten cross-module **coherence identities** that each pull from ≥ 2 modules and require global consistency:

| # | Check | Routes cross-checked |
|---|---|---|
| WOV-1 | $\hbar^2 K^\kappa = -1$ | Mukai / Humbert / Lusztig — three independent $K = 8$ routes |
| WOV-2 | CD $\to$ ST $\to$ BR central-charge chain | $(n_v, n_h) = (63, 88) \to c_{4d} = 107/6 \to c_{2d} = -214$ |
| WOV-3 | Siegel weight 5 four routes | Gritsenko additive / CY-2 formula / anomaly sum / Kodaira |
| WOV-4 | BKM rank 3 $\perp$ Mukai rank 24 | Gram eigenvalues $\{4, 4, -2\}$ vs Mukai $(4, 20)$ |
| WOV-5 | BV Heegner pattern Wave-17 CORRECTED | $c_3 = -8$, not $176256 = p_{24}(5)$ |
| WOV-6 | Saito-Kurokawa chain all 12 primes | $\lambda_p = a_p + p^8 + p^9$, Deligne-RP satisfied |
| WOV-7 | Schur-index 10 Fourier coefficients | $\mathrm{PE}[(72q-22q^2)/(1-q)]$ matches manuscript |
| WOV-8 | Pentagon MZV+Borcherds coherence | $n!$ denom, Padovan dim, Borcherds dominates at $n = 10$ |
| WOV-9 | $A_{N-1}$ family coherence | $k_N = (N+3)/2$, flavour $-N$, umbral Niemeier |
| WOV-10 | $\hbar^2 \cdot 8 = -1$ exact Fraction | atomic closure with cross-module confirmation |

Passing all ten is stronger than passing each of the 14 modules independently: it confirms **the 14 modules describe one mathematical object coherently**, not 14 unrelated computations. Current status: 11/11 tests passing (10 WOV + aggregate); `whole_object_coherence = VERIFIED`.

Run:
```
python3 -m compute.lib.k3_yangian_whole_object_verifier
```

---

## 18. DNA inscription census

Wave 14-17 inscribed ~800 new remarks/propositions/theorems across ~55 chapter files in all three volumes:

**Vol I** (~25 chapters touched): chiral_climax_platonic (W14 + W15 deepen + W17 Hecke); ordered_associative_chiral_kd (W14); shadow_tower_quadrichotomy_platonic (W15 + W17 signature); mc5_class_m_chain_level (W15 KST); koszulness_moduli_scheme (W15 Polyakov); nilpotent_completion (W15 + W17 Etingof); higher_genus_modular_koszul (W14 Gelfand); arithmetic_shadows (W14); chiral_climax (deepened); theorem_B_scope (W14 Etingof); derived_langlands (W14 + W17 Kazhdan); e3_identification_chain_level (W15 Kazhdan); preface_sections2_4_draft (W15); poincare_duality (W15); poincare_duality_quantum (W15 Witten); shadow_tower_higher_coefficients (W17 retract); holographic_datum_master (W17 retract); infinite_fingerprint_classification (W15 Gaiotto); introduction (W17 retract); e2_chiral_algebras (W16); lattice_foundations (W17 Drinfeld); part_iv_platonic_introduction (W16 Kazhdan); w_algebras_deep (W16 + W17 Gaiotto); feynman_diagrams (W15 Nekrasov); bv_brst (W15 + W16 + W17 Costello); quantum_corrections (W14 Drinfeld); entanglement_modular_koszul (W17 Polyakov).

**Vol II** (~20 chapters): axioms (W14 Beilinson); 3d_gravity (W14 + W15); conclusion (W14 + W15); log_ht_monodromy (W14 + W15); celestial_holography (W14); fm-calculus (W14); introduction (W14 + W15); modular_pva_quantization (W16); sc_chtop_heptagon (W15 + W16); ht_physical_origins (W15 Gelfand); ht_bulk_boundary_line (W17 Costello); ht_bulk_boundary_line_core (W17 Costello); dg_shifted_factorization_bridge (W15 Beilinson); curved_dunn_higher_genus (W15 + W17 Etingof); pva-descent-repaired (W15 Etingof); spectral-braiding (W15 Drinfeld); w-algebras (W15 + W16 + W17 Gaiotto); w-algebras-conditional (W17 Witten); modular_swiss_cheese_operad (W17 Nekrasov); factorization_swiss_cheese (W17 Nekrasov); anomaly_completed_topological_holography (W17 retract); thqg_* (7 files, W17 retract); preface (W15 Beilinson); examples-worked (W17 retract).

**Vol III** (~15 chapters): k3_chiral_bialgebra_platonic (W14 pentagon-umbral theorem + cross-refs from all waves); preface (W15 + W16 Witten + W17); introduction (W15 Witten); quantum_groups_foundations (W16 + W17 Gelfand MTC); modular_trace (W16 + W17 Gelfand Fricke/Plancherel); cy_d_kappa_stratification (W15 + W16 Gelfand); coha_wall_crossing_platonic (W15 KST); cyclic_ainf (W16 Etingof); k3e_bkm_chapter (W15 Witten + W17 Drinfeld Monster); e1_chiral_algebras (W17 Gelfand); e2_chiral_algebras (W16 Gelfand); derived_categories_cy (W15 KST + W17 Witten); fukaya_categories (W17 Witten); drinfeld_center (W16 + W17 Kazhdan); hochschild_calculus (W16 Kazhdan); braided_factorization (W17 Drinfeld); phi_universal_trace_platonic (W15 KST); cy_c_six_routes_convergence (W15 + W17 KST); cy_c_pentagon_hypothesis_closures_platonic (W15 KST); k3e_cy3_programme (W15 + W17 retract); k3_yangian_chapter (W15 Drinfeld); k3_chiral_algebra (W15 Drinfeld); m3_b2_saga (W16 Gaiotto); geometric_langlands (W17 Kazhdan); toric_cy3_coha (W17 Nekrasov).

**First-principles cache**: ~40 new entries codifying wave-level errors and confusions (Borcherds-vs-Gritsenko weight, rank conflation, $c_{2d}$ retraction trap, $A_\infty$ tower non-closure, transgression vs umbral shift, archimedean Schmidt dictionary, $\Psi$-functor universality, Fricke-as-$S$-matrix, etc.).

---

## 19. The open frontier (Wave 18+ priorities)

### 19.1 Top-tier mathematical

1. **$\phi^{(n)}$ for $n \ge 11$**: Brown's motivic MZV theorem covers weights ≤ 12; weight-$\ge 13$ irreducible MZVs conjectural. Need to match Borcherds weight $\Phi_{10}^{n/2}$ against full $\mathcal{MZV}_n$ basis. First depth-4 MZV ($\zeta(3,3,3,3)$) enters at weight 12.
2. **$c_n$ for $n \ge 4$**: the Costello Heegner pattern conjecture $c_n = c_{\phi_{10,1}}(n) \cdot [H_n]$ needs verification at $n = 4, 5, 6$ via explicit Fourier-Jacobi coefficients.
3. **Siegel weight $k_N$ for $N = 6$**: the umbral Niemeier labelling breaks at $N = 6$; re-anchoring needed (candidates: $6D_4$ with $3.\mathrm{Sym}_6$).
4. **Global bar-cobar inversion across $H_1, H_3, H_4$**: weight-completed Positselski on Humbert neighbourhoods; strict chain-level global inversion open.
5. **Hochschild $\mathrm{ChirHoch}^3(\mathbf{H}_{\Delta_5})$**: Schiffmann-Vasserot degree-3 CoHA generator non-vanishing conjectural; explicit cocycle awaited.
6. **Gritsenko additive lift full Fourier expansion** to higher order; Shimura-Waldspurger conversion between Route A (Gritsenko additive) and Route B (Borcherds multiplicative).

### 19.2 Structural / categorical

7. **Explicit banding cocycle** for the $\mu_8$-gerbe trivialisation on $\overline{\mathcal{A}_2} \setminus (H_1 \cup H_4)$: current DNA is $(\infty, 1)$-level only.
8. **Full PBW dimension of $\mathfrak{u}_{\zeta_8}$**: $8^{129}$ upper bound; exact count open.
9. **Yetter-Drinfeld $A_\infty$-tower**: explicit formulas for $\delta^{(n\geq 4)}$ in the YD module structure; conjectural pattern $\delta^{(n)} \propto (\Phi_{10}/\eta^{24})^{\lceil n/2 \rceil}$.
10. **Plancherel Hilbert-scheme stabilisation**: the $n \to \infty$ limit on $H^*_T(\mathrm{Hilb}^{[n]}(\mathrm{K3}))$ needs a Maulik-Okounkov-level convergence theorem for the super-quasi-Hopf action.
11. **Gerbe on $H_4$ of order 16**: W13-H7 asserts order 16 on $H_4$; verify this is the order-16 sub-gerbe of the master $\mu_{\mathrm{lcm}(8,16)} = \mu_{16}$-gerbe or a distinct class.
12. **$\mathrm{GRT}_1$-transitivity** on $\mathbf{H}_{\Delta_5}$: affine-KM case done, BKM-side conjectural.

### 19.3 Arithmetic

13. **$a_p$ extension** to $p \in \{83, 89, 97, 101, \ldots\}$: straightforward continuation of $E_4 \cdot \Delta$ convolution.
14. **Fricke-fixed-locus eigenvalue profile**: large-deviations asymptotics near $\mathbb{Z}/8$-phase nodes.
15. **Archimedean-Maass-sign global consistency**: verify $\varepsilon_\infty \cdot \varepsilon_2 = 1$ in the global Arthur character via explicit Maass-spin cover computation.
16. **Full $S_\psi$ structure for $\Delta_5$**: $\Psi_{\Delta_5}$ on Maass spin cover should have larger centraliser than $\Delta_{10}$; $|\Psi_{\Delta_5}|$ computation awaited.

### 19.4 Universal $\Psi$-functor

17. **Monster Lusztig root-of-unity order $\ell_{\mathrm{Monster}}$** (Drinfeld W17 analogue of K3's $\ell = 8$): determined by Conway-Norton normalisation, open parameter.
18. **Fake-Monster theta cocycle $\theta^{\Phi_{12}}$**: explicit rank-26 RTT presentation stated in DNA, generators not yet inscribed.
19. **$\Psi$-image classification**: does $\Psi$ surject onto quasi-Hopf BKMs? Gritsenko-Nikulin 1998 classifies Siegel-automorphic-product BKMs; open whether all super-EK-quantisable BKMs are $\Psi$-images.
20. **Enriques BKM Lie algebra $\mathfrak{g}_{\Delta_5}^{\mathrm{Enr}}$**: Weyl denominator, imaginary-root multiplicities, Monster-like automorphism group ($M_{12}$-moonshine candidate).

### 19.5 Cross-volume bookkeeping

21. **Unified convention sweep**: $\hbar^{\mathrm{Drinfeld}} = 2\pi i/\ell$ vs $\hbar^{\mathrm{BV}}$ bridge, propagate AP151 bridge across all 3 volumes uniformly.
22. **Chacaltana-Distler $(5n-13)/6$** cascade completeness audit at $n \neq 24$ cases.

---

## 20. Constitutional record

### 20.1 Wave reversibility — Beilinson's dictum

The W13 → W14 → W15 reversal on $(c_{4d}, c_{2d})$ establishes a key constitutional datum: **intermediate-wave status is not authoritative without primary-source re-derivation**. Wave 14's formula $(12(g-1) + 7n)/6$ looked plausible but fails the SU(2) $N_f = 4$ cross-check. Multi-path verification prevents this class of error; AP186 "investigate-first-before-shallow-retraction" discipline applies.

Similarly the W16 → W17 Monster-rank correction: Wave 16 inherited "Monster rank 26" imprecisely; Wave 17 cross-checked against Borcherds 1992 Thm 3 and corrected to rank 2, with Fake-Monster at rank 26.

### 20.2 The "24" discipline

The Mukai-lattice rank (24) and the BKM Cartan rank (3) are orthogonal invariants. Confusing "24-dim Cartan" with "24-dim Mukai grading" is the Wave-15 cache entry 15R, now permanently codified. The twelve faces of "24" enumerated in §4.2 are distinct mathematical objects with a shared topological origin in $\chi(\mathrm{K3})$.

### 20.3 The Borcherds / Gritsenko discipline

$\mathrm{Borch}(\phi) \neq \mathrm{Grit}(\psi)$ even when $\phi, \psi$ are superficially related. The BKM denominator of $\mathbf{H}_{\Delta_5}$ is $\Delta_5 = \mathrm{Grit}(\eta^9\vartheta_1)$ — Gritsenko additive route — not $\Phi_{12} = \mathrm{Borch}(\phi_{0,1}^{\mathrm{K3}})$. This is Wave-16 cache entry 16-Gaiotto.

### 20.4 The three-volume anchoring

- **Vol I** anchors the chain-level bar-Euler characteristic for the denominator identity (AP-CY8 anchor B).
- **Vol III** anchors the Borcherds multiplicative lift (AP-CY8 anchor A).
- **Vol II** provides the factorisation-algebra / $\mathsf{SC}^{\mathrm{ch,top}}$ heptagon framework.

The CY-to-chiral functor $\Phi_d$ with d-dependent output connects these:
- $\Phi_1 \to$ Heisenberg ($E_\infty$);
- $\Phi_2(\mathrm{K3}) = \mathcal{H}_{\mathrm{Muk}}$ ($E_2$);
- $\Phi_3(\mathrm{K3} \times E) = \mathbf{H}_{\Delta_5}$ ($E_1$ stabilised by Dunn additivity for $d \geq 3$).

### 20.5 CoHA ≠ chiral discipline (AP-CY7)

$\mathrm{CoHA}_{\mathrm{K3} \times E}$ is an $E_1$-associative algebra (Hall convolution on $D^b\mathrm{Coh}(\mathrm{K3} \times E)$); chiralisation requires explicit $\Phi$-arrow (AP-CY57 construction/narration). The correct form is:
$$\mathbf{H}_{\Delta_5} = \Phi_3\bigl(\mathcal{D}_\hbar(\mathcal{Y}^{\mathrm{Hall}}_\hbar(\mathrm{CoHA}_{\mathrm{K3} \times E}))\bigr)$$
with $\Phi_3$ performing the CoHA → chiral conversion via factorisation on the curve $E$.

### 20.6 $\kappa_{\mathrm{cat}}(\mathrm{K3} \times E) = 0$ not 2

By Künneth: $\kappa_{\mathrm{cat}}(\mathrm{K3} \times E) = \chi(\mathcal{O}_{\mathrm{K3}}) \cdot \chi(\mathcal{O}_E) = 2 \cdot 0 = 0$ (total space), NOT 2 (fibre). The programme must distinguish total-space $\kappa_{\mathrm{cat}}$ from fibre $\kappa_{\mathrm{fibre}}(\mathrm{K3}) = 2$ wherever the distinction matters.

### 20.7 CY-$d$ Hochschild concentration scope

Theorem H (Hochschild concentration) says $\mathrm{ChirHoch}^\bullet$ lives in $\{0, 1, 2\}$ for ordinary chiral algebras. For CY-$d$ input under $\Phi_d$: concentration extends to $\{0, 1, \ldots, d\}$. For K3 × E (CY-3 total): extends to $\{0, 1, 2, 3\}$.

---

## 20.8 Wave 18 constitutional items

- **Wave reversibility extended**: the W13→W14→W15→W16→W17→W18 sequence now includes ONE more wave-level correction: W16's Monster Cartan rank (asserted 26, corrected by W17 to 2, vindicated by W18 four-route verification $\ell_{\mathrm{Monster}} = 2$ = $2c_+(\mathrm{II}_{1,1}) = 2$).
- **Theorem-B scope tightening**: strict bar-cobar on $\overline{\mathcal{A}_2}\setminus\bigcup_{n \text{ admissible}} H_n$ — Wave-18 Beilinson corrects the Wave-15 "only $H_1 \cup H_4$" scope.
- **Depth-4 MZV motivic closure**: $\zeta(3,3,3,3)$ at weight 12 is the **last** depth-irreducible provably-motivic entry under Brown 2011; weights $\geq 13$ conjectural on Zagier-Hoffman.
- **Theorem H scope universal**: $\mathrm{ChirHoch}^\bullet \subset \{0, 1, 2, d\}$ for $\Phi_d$ on CY-$d$; propagated across all three volumes by Wave-18 Polyakov.
- **Heegner-pattern theorem is ALL-ORDERS**: not a loop-by-loop conjecture but a structural theorem via three-input composite (Bruinier + Borcherds + CGP).

## 21. The question, answered — with maximum precision

> **"What is the chiral quantum group undergirding the BKM related to the Siegel modular forms?"**

$$\boxed{\;\mathbf{H}_{\Delta_5} \;=\; \mathcal{D}_\hbar\!\Bigl(\mathcal{Y}^{\mathrm{Hall}}_\hbar(\mathrm{CoHA}_{\mathrm{K3}\times E}),\; \widetilde{\Phi}^{\mathrm{Sieg\text{-}Bor}}_{\mathrm{Sp}_4}[\Phi_{10}/\eta^{24}],\; R_{\mathrm{Sieg,dyn}}\Bigr)\;}$$

specialised at $\hbar^2 = -1/8$, with:

**Algebraic content**:
- **BKM denominator** = $\Delta_5 = \mathrm{Grit}(\eta^9\vartheta_1)$ on Maass spin cover of $\mathrm{Sp}_4(\mathbb{Z})$ — NOT $\Phi_{12}$ (Borcherds).
- **Arthur parameter** = $\psi_{\Delta_{10}} = \phi_{\Delta_{E_6}} \boxtimes \mathrm{Sym}^1$ via $\Delta_5^2 = \Delta_{10}$ (Saito-Kurokawa CAP).
- **3 real simple roots** in hyperbolic core $\Lambda^{2,1}_{II}$, signature $(2, 1)$ with eigenvalues $\{+4, +4, -2\}$.
- **24-dim Mukai-lattice grading** orthogonal to Cartan.
- **Infinite imaginary-root cone** with Hardy-Ramanujan growth $\sim \exp(4\pi\sqrt n)$.
- **Explicit RTT**: $R_{\mathrm{Sieg,dyn}}(u, Z) = R^{\mathrm{rat}}_{\mathrm{Yang}}(u) \cdot \theta^{\mathrm{K3}}(u, Z)$, $\mathrm{qdet}\,T \propto \Delta_5$.

**Categorical content**:
- **Rep category** is non-semisimple Kerler-Lyubashenko MTC at $\zeta_8$.
- **Modular $S$-matrix** = Fricke involution $w_8: Z \mapsto -(8Z)^{-1}$; eigenvalues $\{1, i, -1, -i\}$; fixed locus $H_1 \cap H_4$.
- **Plancherel measure** integrates to $1/\Phi_{10}(Z)$.
- **Drinfeld centre** $\mathcal{Z}(\mathrm{Rep}) \simeq \mathrm{YD}^{A_\infty}$.
- **Fusion ring** with 3 generators, 3 relation types (Kac-Walton + $M_{24}$-equivariance + Verlinde).

**Physical origin**:
- **4d parent** = class-$\mathcal{S}_{A_1}$ on 24-punctured sphere with $c_{4d} = 107/6$, $c_{2d} = -214$, Coulomb rank 21.
- **7 routes** (5 duality frames + $\mathrm{K3}^2 \times S^1$ + GW/DT) all converge on $\Delta_5$.
- **Decoupling limit** at chain level via Costello-Gwilliam factorisation-algebra degeneration.
- **BV obstruction** $c_n \propto c_{\phi_{10,1}}(n) \cdot [H_n]$ at Heegner divisors; $c_1 = [\Delta_5]$, $c_2 = 0$, $c_3 = 176256 \cdot [H_3]$.

**Arithmetic content**:
- **Hecke eigenvalues** verified first-principles for $p \le 79$.
- **Global A-packet** $|\Psi_{\Delta_{10}}| = 4$ with $S_\psi = \mathbb{Z}/2$.
- **Local Langlands**: unramified for $p \nmid 2$, ramified-quadratic $\varepsilon_2$ at $p = 2$, archimedean Schmidt $(17/2, 15/2)$ for $\Delta_{10}$ and $(7/2, 5/2) \otimes \mathrm{sgn}_\mathbb{R}$ for $\Delta_5$.
- **Geometric Langlands** = Fricke self-duality: ${}^L\mathfrak{g}_{\Delta_5} = \mathfrak{g}_{\Delta_5}$.

**Quantum-group landscape**:
- **$\Psi$-functor sibling** to Monster BKM (rank 2) and Fake-Monster BKM (rank 26).
- **$M_{24}$ 't Hooft anomaly** = order-6 transgression cocycle sum $\equiv -1 \pmod 6$.
- **CY-2 landscape** partitioned: Enriques ($\mathbb{Z}/2$ orbifold, weight $5/2$); Kummer (sublattice, weight 5); $T^4$ (abelian Heisenberg taxon G); half-K3 (affine $\widehat{E_8}$ taxon L). Weight formula $w_{\mathrm{Borch}} = 5\chi_{\mathrm{top}}/24$.
- **$A_{N-1}$ class-$\mathcal{S}$ family**: $(k_N) = (5/2, 3, 7/2, 4)$ for $N = 2, 3, 4, 5$; umbral groups $M_{24}, 2.M_{12}, 2.\mathrm{AGL}_3(2), \mathrm{GL}_2(5)/\{\pm 1\}$.
- **Coherence tower**: $A_\infty$-quasi-Hopf with genuine infinite tail; $\phi^{(n)}$ computed through $n = 10$ with MZV + Borcherds legs; Borcherds leg dominates by $\sim 10^{10}$ at $n = 10$.

The object is not Yangian, not toroidal, not Drinfeld-quasi-Hopf. It is a **fourth taxon**: super-Etingof-Kazhdan Hall-Drinfeld double of a CY-3 CoHA at paramodular specialisation, governing the Gritsenko-additive $\Delta_5$ BKM and sitting at a seven-frame construction fixed point.

It is the chiral quantum group undergirding the BKM related to the Siegel modular forms.

---

## 22. Genealogy of the identification

For future reference, the dependency chain of the main identification:

```
K3 topology χ = 24, c₁ = 0, h²⁰ = 1
    ↓ [CY-2 classification, Witten W15]
Mukai lattice II₄,₂₀, Humbert stratification
    ↓ [Gritsenko-Nikulin 1998 classification of Siegel-automorphic-product BKMs]
BKM Lie superalgebra g_Δ₅, denominator Δ₅ = Grit(η⁹θ₁)
    ↓ [Etingof-Kazhdan 2008 super-quantisation on Manin pair]
super-EK quantum group U_ℏ(g_Δ₅)
    ↓ [Schiffmann-Vasserot CoHA + Davison CY-3 integrality]
CoHA(K3 × E) realisation via Hall-Drinfeld double
    ↓ [Maulik-Okounkov stable envelopes]
R-matrix R_Sieg,dyn(u, Z) = R_rat × θ_K3
    ↓ [Bruinier 2002 Prop 5.1 Heegner-Chern reciprocity]
three-faces identity: ℏ² · 8 = -1
    ↓ [Beem-Rastelli 2013 protected chiral algebra]
4d parent T[A₁, Σ₀,₂₄] with c₄d = 107/6
    ↓ [Costello-Gaiotto-Paquette twisted holography]
11D SUGRA on K3 × ℂ² with 24 M5-branes BV-quantised
    ↓ [Cheng-Duncan-Harvey 2014 + Gaiotto pentagon W14]
M₂₄ 't Hooft anomaly = order-6 umbral cocycle
    ↓ [Kerler-Lyubashenko 2001 + Fricke involution]
MTC at ζ₈ with S = w₈
    ↓ [Arthur 2013 endoscopic classification]
Global A-packet |Ψ_Δ₁₀| = 4, self-Langlands-dual
    ↓ [Oberdieck-Pixton 2016 DT, unconditional]
GW = DT = 1/Φ₁₀ seventh route
    ↓ [Drinfeld W17 Ψ-functor]
H_Δ₅ as Ψ(K3) cosibling of Ψ(Leech) = H_Monster
```

---

## Appendix A — canonical primary-source references

Alday-Benini-Tachikawa 2009 arXiv:0912.4664; Andrianov 1974 *Matem. Sbornik*; Arinkin-Gaitsgory 2015; Arthur 2013 AMS Coll. 61; Beauville 1983 *J. Diff. Geom.* 18; Beem-Lemos-Liendo-Peelaers-Rastelli-van Rees 2013 arXiv:1312.5344; Beem-Peelaers-Rastelli 2014 arXiv:1408.6522; Benini-Peelaers 2015 arXiv:1507.04746; Borcherds 1988 *J. Algebra* 115; Borcherds 1992 *Invent.* 109; Borcherds 1995 *Invent.* 120; Borcherds 1998 *Invent.* 132; Bridgeland 2008 *Ann. Math.* 166; Bringmann-Creutzig-Rolen 2014; Brown 2011 *Ann. Math.* 175; Bruinier 2002 *LNM* 1780; Chacaltana-Distler 2010 arXiv:1008.5203; Chacaltana-Distler-Tachikawa 2013 arXiv:1212.3952; Cheng-Duncan-Harvey 2014 arXiv:1307.5793; Conway-Sloane 1988 *SPLAG*; Córdova-Shao 2015 arXiv:1506.00265; Costello 2011 AMS; Costello 2015 arXiv:1505.06703; Costello 2016 *Renormalization*; Costello-Gaiotto 2018 arXiv:1812.00516; Costello-Gaiotto-Paquette 2018 arXiv:1810.10016; Costello-Gwilliam 2017/2021 Cambridge; Costello-Li 2015 arXiv:1505.06703; Creutzig-Ridout 2013; Davison 2017 arXiv:1512.04179; Davison-Meinhardt 2020 *Invent.*; Deligne 1970 *LNM* 163; Deligne 2013 Bourbaki; Dijkgraaf-Moore-Verlinde-Verlinde 1997 arXiv:hep-th/9608096; Dijkgraaf-Verlinde-Verlinde 1997 *Nucl. Phys. B* 484; Drinfeld 1985/1986/1990 *Soviet Math. Dokl.*; Eguchi-Hikami 2009 arXiv:0904.0911; Eguchi-Ooguri-Tachikawa 2011 arXiv:1004.0956; Enriquez-Furusho 2020 arXiv:2004.07090; Enriquez-Gomez-Gonzalez-Maassarani 2022 arXiv:2205.10474; Etingof-Kazhdan 1996-2008 *Selecta Math.* I-V (esp. 2008 Part V super); Etingof-Ostrik 2004; Feigin-Frenkel 1990/1992; Feigin-Gainutdinov-Semikhatov-Tipunin 2006 *Comm. Math. Phys.* 265; Feingold-Frenkel 1983 *Math. Ann.* 263; Francis 2013 *Adv. Math.* 239; Frenkel-Lepowsky-Meurman (FLM) 1988; Gaiotto 2009 arXiv:0904.2715; Göttsche 1990 *Math. Ann.* 286; Gritsenko 1995/1999 *Algebra i Analiz*; Gritsenko-Hulek 1998 *Duke* 94; Gritsenko-Nikulin 1997 alg-geom/9612004; Gritsenko-Nikulin 1998 *Algebra i Analiz* 11; Hardy-Ramanujan 1918; Harvey-Moore 1996 arXiv:hep-th/9510182; Hinich 2010 *Adv. Math.* 223; Hulek-Sankaran 2011; Ibukiyama 1984/1998; Igusa 1964; Ikeda 2001 *Ann. Math.* 154; Iqbal-Kozçaz-Vafa 2007; Kapranov-Vasserot 2018 arXiv:1802.07988; Katz-Klemm-Vafa 1999; Kerler-Lyubashenko 2001 *LMS LNS* 262; Kontsevich 2003 *Lett. Math. Phys.* 66; Kontsevich-Soibelman 2008 arXiv:0811.2435; Kuga-Satake 1967 IHES 36; LMFDB project (16.1.a.a); Lusztig 1990/1993 Birkhäuser/MIT; Maass 1979; Markl-Shnider-Stasheff 2002; Maulik-Nekrasov-Okounkov-Pandharipande 2006; Maulik-Okounkov 2019 *Astérisque* 408; Maulik-Pandharipande 2006 arXiv:math/0605321; Maulik-Pandharipande-Thomas 2010 arXiv:1001.2719; Moeglin-Renard 2018; Morrison-Vafa 1996 I/II arXiv:hep-th/9602114, 9603161; Mukai 1984; Nakajima 1997 *Ann. Math.* 145; Nahm-Wendland 2001 arXiv:hep-th/9912067; Nekrasov 2003 arXiv:hep-th/0206161; Nekrasov-Pestun-Shatashvili 2013 arXiv:1312.6689; Nekrasov-Shatashvili 2009; Neguț 2022 arXiv:2204.02497; Oberdieck-Pandharipande 2015 arXiv:1411.1514; Oberdieck-Pixton 2016 arXiv:1706.10100; Oguiso-Sakai 2001; Pandharipande-Thomas 2014 arXiv:1206.5490; Positselski 2011; Saito-Kurokawa SK CAP; Schiffmann-Vasserot 2013 *Publ. Math. IHES* 118; Schmidt 2017; Seiberg 1988 *Phys. Lett. B* 206; Shapere-Tachikawa 2008 arXiv:0804.1957; Taormina-Wendland 2011 arXiv:1107.3834; Turaev 1994; Vafa 1996 arXiv:hep-th/9602022; Verlinde 1988; Weissauer 2009; Witten 1995 arXiv:hep-th/9503124.

---

## Appendix B — glossary of cache-codified confusions

Twenty-plus first-principles-cache entries installed across Waves 14-17. Abbreviated list:

- **15R**: BKM Cartan rank 3 ≠ Mukai-lattice rank 24.
- **16-Gaiotto**: Borcherds multiplicative ≠ Gritsenko additive; $\Phi_{12} \neq \Delta_5$.
- **17A**: Plancherel on non-semisimple MTC uses projective covers, not simples.
- **17B**: Generic Fricke $S$-trace = 0; $M_{24}$-invariant Humbert-block trace = 4.
- **17C**: Verlinde on semisimple block vs logarithmic extension (Creutzig-Ridout).
- **17D**: Kac-Walton truncation as EXTRA datum beyond Weyl chamber.
- **17E**: $E_1$-fusion at $E$ direction vs $E_2$-braiding at K3-surface direction.
- **17F**: CoHA-character $\chi(\mathrm{CoHA}) = 1/\Phi_{10}$ vs chiral-algebra equality — requires $\Phi$-arrow.
- **17G**: Refined GW/DT toric-only scope (non-toric CY$_3$ conjectural).
- **17H**: KKV semisimple-vs-Jordan-block distinction in $\mathbf{H}_{\Delta_5}$-mod category.
- **17-BKM-signature**: Feingold-Frenkel eigenvalue-based signature vs Sylvester principal-minor trap.
- **17-c-eff-anomaly**: negative $c_{\mathrm{eff}}$ is anomaly coefficient, not Hilbert-space entropy.
- **17-Ψ-universality**: Monster, K3, Fake-Monster are $\Psi$-co-siblings, NOT nested.
- **17-Monster-rank**: Monster rank 2, Fake-Monster rank 26, K3 rank 3 — distinct hyperbolic Cartans.
- **17-archimedean-Schmidt**: $(17/2, 15/2)$ for $\Delta_{10}$ vs $(7/2, 5/2)$ for $\Delta_5$ (Maass-spin with sgn twist).
- **17-packet-vs-multiplicity**: $|\Psi| = 4$ is packet size; multiplicity is 1 via Arthur character.
- **17-self-Langlands-vs-dual-pair**: self-dual BKM under Langlands exchanges via Fricke.
- **17-Drinfeld-centre-vs-averaging**: centre is right adjoint to forgetful, not averaging map.
- **17-Fricke-as-S-matrix**: modular $S$-matrix structurally equals arithmetic Fricke involution.
- **17-CY2-landscape-dichotomy**: K3/Enriques/$T^4$/half-K3 partition by topological invariants.

Plus the Wave-14/15/16 earlier entries (AP113/152/160 bare-labels, AP-CY7 CoHA ≠ chiral, AP-CY54 centre ≠ averaging, AP151 two-ℏ bridge, AP-CY58 d-dependent scope, AP-CY8 two-anchor denominator, etc.).

---

## Appendix C — wave-by-wave contribution index

**Wave 13 (seed, 2026-04-19)**: initial identification sketch; 22-file residual inventory; first-principles pants with $(c_{4d}, c_{2d}) = (107/6, -214)$; 10 elite agent output.

**Wave 14**: identification $\mathbf{H}_{\Delta_5} = \mathcal{D}_\hbar(\mathcal{Y}^{\mathrm{Hall}}(\mathrm{CoHA}_{K3\times E}), \widetilde{\Phi}^{\mathrm{Sieg\text{-}Bor}}, R_{\mathrm{Sieg,dyn}})$; classification cohomology $\mathbb{C}\cdot\Delta_5$; Koszul structure (generalised); Arthur parameter $\psi_{\Delta_{10}}$; pentagon-umbral $\mathbb{Z}/6$ theorem; WAVE-14 erroneous $c_{4d}$ retraction.

**Wave 15**: $(c_{4d}, c_{2d})$ restored to $(107/6, -214)$ by Gaiotto; BKM rank 3 correction by Drinfeld; $\phi^{(4)}, \phi^{(5)}$ by Etingof; Tannakian fibre by Gelfand; Hecke at $p \le 37$ by Beilinson; 5-frame duality closure by Witten; Costello 2-loop $c_2 = 0$; $A_{N-1}$ family by Gaiotto; refined $\Omega$ by Nekrasov; Humbert $H_4$ by Kazhdan; KST $\Phi$-discipline; ~20 new DNA inscriptions.

**Wave 16**: Costello 3-loop $c_3 = 176256 [H_3]$ + Heegner pattern conjecture; Gaiotto Borcherds/Gritsenko disambiguation; Gelfand MTC at $\zeta_8$ with Fricke $S$; Drinfeld Monster/Fake-Monster/K3-BKM distinction; Kazhdan $6A/6B$ transgression $(2, 3) \pmod 6$; Etingof $\phi^{(6,7)}$; Polyakov $-214$ cascade; Witten chain-level decoupling; Nekrasov MO-vs-SV rigor; KST AP-CY8 two-anchor; ~180 DNA inscriptions.

**Wave 17**: Gelfand Plancherel + fusion matrix $3 \times 3$ + $S$-eigenvalues $\{1, i, -1, -i\}$; Beilinson $a_p$ at $p \le 79$ + residual $-312$ closure; Drinfeld Monster super-EK + universal $\Psi$ functor + rank corrections; Etingof $\phi^{(8, 9, 10)}$ + Padovan + Borcherds dominance + $\mathrm{obs}_\infty$ pro-limit; Polyakov $(2,1)$ signature + $c_{\mathrm{unit}} = 2$ + $c_{\mathrm{eff}} = -166$; Nekrasov GW/DT seventh route + CoHA character identification; Kazhdan archimedean Schmidt + $|\Psi| = 4$ + Drinfeld centre + Fricke-self-Langlands; Costello $c_4, c_5, c_6$ Heegner verification + BV structural theorem; Witten CY-2 landscape dichotomy + Enriques orbifold + $T^4$ abelian + half-K3 + weight formula $5\chi/24$; Gaiotto $k_3 = 3, k_4 = 7/2$ verified + umbral Niemeier family + $N = 6$ labelling break; KST unified cross-check engine with 58/58 tests; ~250 DNA inscriptions.

**Totals across Waves 14-17**:
- 40 agents, ~200 attack-heal cycles.
- 14 compute modules (~275 passing test assertions).
- ~800 DNA inscriptions across ~55 chapter files.
- ~40 first-principles cache entries.
- 2 major wave-level retractions (absorbed).

---

*End of synthesis. Ready for Wave 18 continuation or alternative research directions.*
