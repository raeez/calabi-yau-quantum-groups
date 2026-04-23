# Architecture of the Gluing Chapter

*Vol III new chapter design — consolidating every mode of assembling local CoHAs into global CoHAs, with K3 × E as the master test case*

Date: 2026-04-23

## 0. Organising principle

Every CoHA seen in this programme arises by assembling *local* data through a *gluing cocycle* valued in some category of compatibilities. The gluing mode is dictated by where on the *four equivariance strata* the geometry sits:

| Stratum | Local datum | Gluing cocycle | Examples |
|---|---|---|---|
| (i) Toric $T^d$ | $\mathbb{C}^3$-chart with Jordan-triple $W$ | FM kernel $\mathcal{O}_\Delta \otimes \pi_1^*\mathcal{O}(-1)^{\otimes k}$ on overlaps | $\mathbb{C}^3$, conifold, local $\mathbb{P}^2$, banana, SPP |
| (ii) Reduced $\mathbb{C}^\times \times \mathrm{Aut}(X)$ | Automorphism-equivariant local pieces | $\mathrm{Aut}(X)$-cocycle on the quotient | K3, K3 $\times$ E generic |
| (iii) Orbifold inertia $I(X/G)$ | $G$-equivariant chart | BKR / McKay cocycle | $\mathbb{C}^3/G$, Mathieu $M_{24} \curvearrowright K3$ |
| (iv) Lattice-polarised period | Lattice-polarised chart + Borcherds-lift | Gritsenko-Cléry automorphic form | K3 at Humbert divisors, K3 $\times$ E with $\Delta_5$, Igusa $\Phi_{10}$ |

These strata are **not a partition**: a geometry may carry two or more at once. Local $\mathbb{P}^2$ sits in (i)$\cap$(iii); Mathieu $K3$ in (iii)$\cap$(iv); $K3 \times E$ straddles (ii)–(iv). The gluing machinery must handle each pairwise intersection.

## 1. Chapter structure

### Part I — The gluing problem in categorical generality

#### §1.1 The abstract set-up
For $X$ a CY$_d$ variety (or CY$_d$ category), we seek a *CoHA* $\mathcal{H}(X)$ that is:
- *Local*: defined chart-wise on an open cover $\{U_\alpha\}$ of $X$
- *Gluing-covariant*: glues along the Čech nerve of the cover
- *Derived-invariant*: independent of the cover and of the choice of tilting

#### §1.2 The gluing 2-category
The target is a 2-category $\mathrm{GluedCoHA}(X)$ whose:
- objects are sheaves of CoHAs on $X$;
- 1-morphisms are local-to-global gluing maps;
- 2-morphisms are higher gluing coherences.

The global CoHA is the limit over this 2-category (when it exists).

#### §1.3 The four-stratum taxonomy
Formal statement of the four equivariance strata above. Theorem: every known CoHA-gluing in Vol III factors through exactly the 15 non-empty intersections of the four strata.

### Part II — Chart-wise gluing on toric CY$_3$ (Stratum i)

#### §2.1 Čech gluing of two charts: the conifold paradigm
- Two-chart atlas $Y = U_+ \cup U_-$, each $U_\pm \cong \mathbb{C}^3$
- Each chart carries Schiffmann–Vasserot CoHA $Y^+(\widehat{\mathfrak{gl}}_1)$
- FM transition $K_{+-} = \mathcal{O}_\Delta \otimes \pi_1^*\mathcal{O}(-1)$ on overlap $\mathbb{G}_m \times \mathbb{C}^2$
- Homotopy colimit = super-Yangian $Y^+(\widehat{\mathfrak{gl}}(1|1))$
- Super structure from Koszul sign $\sigma = -1$ of base-orientation flip

#### §2.2 Multi-chart toric fan
- Toric fan $\Sigma$ with cones indexed by lattice points
- Each top-dim cone gives a $\mathbb{C}^3$ chart
- Gluing cocycle runs along the fan's face lattice
- Galakhov–Li–Yamazaki bond factor presentation per edge
- Examples: $\mathbb{C}^3/\mathbb{Z}_n$ (linear toric), banana threefold, suspended pinch point

#### §2.3 The compact-4-cycle obstruction
Local $\mathbb{P}^2 = \mathrm{Tot}(K_{\mathbb{P}^2}) = [\mathbb{C}^3/\mathbb{Z}_3]^{\mathrm{res}}$ has a compact $\mathbb{P}^2$-divisor — a compact 4-cycle. The chart-wise $\mathbb{C}^3$ atlas formally covers but the factorisation-homology assembly picks up *internal lattice-point contributions* (Neguț wheel-condition corrections). Chart-wise CoHA without modification misses these; the correct local-global reconstruction uses either:
- (a) the McKay/orbifold route (Stratum iii) on $[\mathbb{C}^3/\mathbb{Z}_3]$ with BKR equivalence;
- (b) explicit treatment of internal lattice points via higher-rank shuffle-algebra relations.

#### §2.4 The local-to-global theorem
Theorem: for a local toric CY$_3$ $X$ with toric diagram having zero interior lattice points, the Čech-glued CoHA is well-defined and matches the direct Davison–Meinhardt critical CoHA on $X$.

### Part III — McKay/orbifold gluing (Stratum iii)

#### §3.1 Orbifold inertia and BKR
- $[\mathbb{C}^3/G]$ for $G \subset SU(3)$ finite
- Inertia stack $I([\mathbb{C}^3/G])$ decomposes by conjugacy class of $G$
- Bridgeland–King–Reid equivalence $D^b([\mathbb{C}^3/G]) \simeq D^b_G(\mathbb{C}^3)$

#### §3.2 Local $\mathbb{P}^2 = [\mathbb{C}^3/\mathbb{Z}_3]$
- The nine-arrow Beilinson quiver via skew-group Morita
- CoHA via Schiffmann–Vasserot on $[\mathbb{C}^3/\mathbb{Z}_3]$ equivariantised
- Alternative: chart-wise cover of the crepant resolution

#### §3.3 Mathieu $M_{24}$ on K3
- Twined elliptic genera of Eguchi–Ooguri–Tachikawa
- Mathieu moonshine weight-$1/2$ mock modular forms
- CoHA twisted by $M_{24}$-conjugacy class
- This is Stratum (iii)$\cap$(iv): orbifold *and* lattice-polarised

### Part IV — Derived Morita gluing (Stratum i–iii overlap)

#### §4.1 Van den Bergh tilting bundles
- Tilting object $T \in D^b(\mathrm{Coh}\,X)$ with $\mathrm{End}(T)$ finite
- Derived Morita $R\mathrm{Hom}(T, -) : D^b(\mathrm{Coh}\,X) \xrightarrow{\sim} D^b(A\text{-mod})$
- Transport of Hall product along derived Morita (Davison–Hennecart–Schlegel Mejia)

#### §4.2 Tilting as gluing presentation
- Tilting object = universal local presentation
- $T = \bigoplus_i T_i$ with $T_i$ local pieces
- End $T$ = Jacobi algebra of gluing quiver
- Examples: VdB on conifold; Bridgeland on local $\mathbb{P}^2$; Craw on $(-3)$-curves

#### §4.3 The gluing-preservation theorem
If $T, T'$ are tilting objects related by a derived equivalence (e.g., mutation), the CoHAs constructed via $\mathrm{End}(T)$ and $\mathrm{End}(T')$ are canonically isomorphic.

### Part V — Factorisation-algebra gluing (Costello–Gwilliam framework)

#### §5.1 Weiss covers
- Weiss cover: open cover closed under finite disjoint unions
- Factorisation prefactorisation algebras (CG Vol II Def 3.1.1)
- Locality axiom via Weiss cover (Def 6.1.6)

#### §5.2 Ran space / Beilinson–Drinfeld
- $\mathrm{Ran}(C)$ for curve $C$; colim of $C^n/S_n$
- Chiral algebras on $\mathrm{Ran}(C)$
- Francis–Gaitsgory chiral Koszul duality

#### §5.3 The two-stage factorisation $\Phi_3 = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_2, C} \circ \Phi^{FA}_3$
- Stage-1: $E_3$-factorisation algebra on $X$ via Kontsevich–Tamarkin formality + Costello–Li
- Stage-2: specialisation to curve $C$ via Dunn–Lurie $E_3 = E_1 \otimes E_2$
- Each stage is itself a gluing: Stage-1 from hCS Feynman rules, Stage-2 from transverse-fibre integration

#### §5.4 Holomorphic vs topological factors
- 5D hCS: 1D topological × 4D holomorphic
- Factorisation on each factor separately
- Gluing along stratified manifold structure (CG Vol II §8)

### Part VI — Wall-crossing gluing (Stratum-independent)

#### §6.1 Kontsevich–Soibelman quantum torus
- $\mathcal{T}_\Gamma$: formal power series in $\hat{x}_\gamma$ with $\hat{x}_\gamma\hat{x}_{\gamma'} = \mathbb{L}^{\langle\gamma,\gamma'\rangle/2}\hat{x}_{\gamma+\gamma'}$
- Skew-Euler form $\langle\cdot,\cdot\rangle$ vanishes on CY$_3$ — so the torus is commutative
- Non-commutativity lives in the Hall product, not the torus

#### §6.2 Chambers as gluing cells
- Stability space stratified into chambers
- KS wall-crossing formula = chamber-to-chamber automorphism
- The *quantum-dilogarithm cocycle* $\prod \Psi(x_\gamma)^{\Omega(\gamma)}$ is the gluing datum
- Joyce–Song integration map $I$ is chamber-equivariant

#### §6.3 Seiberg-duality mutation as gluing
- Mutation at a vertex = quiver gluing automorphism
- Weyl group $W(Q)$ acts on the chamber lattice
- The CoHA algebra is chamber-independent; representations are chamber-parametrised
- Shifted quiver Yangian (GLY) indexes the chamber-by-chamber story

### Part VII — Lattice-polarised / automorphic gluing (Stratum iv)

#### §7.1 Mukai lattice of K3
- $H^\bullet_{\mathrm{even}}(K3, \mathbb{Z}) \cong \mathrm{II}_{4,20}$
- Mukai pairing: $\langle v, w\rangle = v_0 w_2 + v_2 w_0 - v_1 \cdot w_1$
- Kuga–Satake / period map to $\mathcal{D}_{4,20}$

#### §7.2 Borcherds lifts
- Weak Jacobi form $\phi \in J_{k, m}$ on K3 lattice
- Borcherds lift $\Psi: J \to \mathrm{MFs}(\mathcal{D})$ produces automorphic form
- CoHA-multiplication coefficients = Fourier coefficients of $\Psi$

#### §7.3 Gritsenko–Cléry eight-form family
Eight automorphic forms on $\mathcal{A}_2$ with Fourier coefficients $c_N(0) \in \{10, 4, 2, 2, 1, 2, 1/2, 0\}$ producing $\kappa_{\mathrm{BKM}} = c_N(0)/2$ on $N \in \{1,2,3,4,6\}$. Each form is a gluing datum for a specific BKM-CY$_3$ correspondence.

#### §7.4 The $\Delta_5$ / K3 × E gluing
- $\Delta_5 = \mathrm{Grit}(\phi_{0,1})$ is the Gritsenko lift of the weak Jacobi form of K3
- $\kappa_{\mathrm{BKM}}(\mathfrak{g}_{\Delta_5}) = 5$
- Automorphic cocycle assembling local Hall-Drinfeld double pieces into global

### Part VIII — The K3 × E master example

#### §8.1 Elliptic K3 as fibration
- $\pi: K3 \to \mathbb{P}^1$ with 24 singular fibres of type $I_1$
- $\chi(K3) = 24 = \sum_{I_1} \chi(I_1)$
- Nodal elliptic curves at each $I_1$

#### §8.2 K3 × E as local-global assembly
The insight: on $K3 \times E$, the 24 $I_1$-fibres become 24 curve-supported loci $I_1 \times E$, each a nodal-elliptic × E configuration. Locally at each node, the geometry looks like
$$\{xy = 0\} \times E \quad \subset \quad \mathrm{smooth\ threefold}.$$
These are **not smooth $\mathbb{C}^3$ points**, but *curve-stalks* supported on the $E$-factor. At each such stalk, the local CoHA is a Davison critical CoHA of a quiver-with-potential (the Jordan-triple $W = \mathrm{tr}(x[y,z])$ tensored with $E$-coefficients).

#### §8.3 The four-stratum decomposition of K3 × E
K3 × E sits in strata (ii), (iii), (iv):
- (ii) via reduced Aut(K3) × Aut(E) action
- (iii) via Mathieu $M_{24}$ twisted by K3
- (iv) via Borcherds-lift $\Delta_5$ on Kuga–Satake period domain

Four separate gluing cocycles, each encoding a different piece of CoHA structure.

#### §8.4 The Serre-equivariant quasi-NCCR
Per CLAUDE.md key-facts: K3 × E admits **no global NCCR** due to five obstructions (dualising sheaf not reflexive-tilting, derived McKay requires finite Aut fixing a point, HPD self-dual not product-compatible, Mukai vanishing fails off K3 factor, no global CY-3 symmetric obstruction theory). The *Serre-equivariant quasi-NCCR* substitutes: a *locally-defined* tilting object equivariant under the Serre twist, gluing via the factorisation pushforward.

#### §8.5 The Hall–Drinfeld double assembly
- 24 $\mathbb{C}^3$-stalks $\to$ 24 $Y^+(\widehat{\mathfrak{gl}}_1)$ via Schiffmann–Vasserot
- Mukai-lattice cocycle $\to$ Manin pair of signature (4, 20) or (2, 21) (TBD after the active adversarial thread completes)
- Borcherds cocycle $\to$ $\Delta_5$-associator for the quasi-Hopf structure
- Mathieu cocycle $\to$ $M_{24}$-twining generating function

#### §8.6 The imaginary rank-23 Cartan
Assembled imaginary-root Cartan:
$$\mathfrak{h}^{\mathrm{imag}} \cong H^\bullet_{\mathrm{even}}(K3, \mathbb{Q}) / \langle [\mathrm{fibre}]\rangle \oplus \langle [E]\rangle$$
giving $(24 - 1) + 1 - 1 = 23$ (or similar; exact count depends on the fibre-line reduction and the Humbert-monodromy factor).

#### §8.7 The Humbert monodromy
- Humbert surface $\mathcal{H}_1 \subset \mathcal{A}_2$ of discriminant 1
- Order-8 monodromy acting on middle cohomology of K3 × E fibration
- This is a *stratum-(iv)* invariant: not visible to Čech or derived-Morita gluing
- Contributes the factor $|{\rm Humbert}| = 8$ to the derived-centre complementarity $\kappa + \kappa^! = 8$

### Part IX — When gluing fails

#### §9.1 The four obstructions (recap from conifold synthesis)
- (O1) No toric atlas
- (O2) BCOV anomaly $\alpha_{\mathrm{BCOV}}$ non-zero
- (O3) No equivariant localisation on simples
- (O4) No finite quiver with potential

#### §9.2 Compact CY$_3$ without K3 × E structure
For the quintic, bicubic in $\mathbb{P}^2 \times \mathbb{P}^2$, etc. — no fibration structure giving the 24-stalk assembly. Here even the Stratum-(iv) automorphic gluing is subtler: only the categorical CoHA via MNOP + Davison integrality is available, with no explicit chart-wise formulas.

#### §9.3 Partial transfer on compact CY$_3$
- Davison–Meinhardt critical CoHA is stratum-free
- Kontsevich–Soibelman motivic wall-crossing is stratum-free
- Two-stage factorisation is stratum-free in principle, but Stage-1 explicit formula needs a local presentation that compact CY$_3$ generally lacks

### Part X — Unifying framework

#### §10.1 The gluing classification theorem
Theorem (aspirational): every CoHA assembled in Vol III fits into the 15 non-empty intersections of the four strata, with gluing cocycle valued in an explicitly-named group:
- (i) alone: FM-kernel cocycle in $H^1(X, \underline{\mathrm{Pic}})$
- (ii) alone: $\mathrm{Aut}(X)$-cocycle in $H^1(X/\mathrm{Aut}, \underline{\mathrm{Aut}})$
- (iii) alone: orbifold inertia, $H^1(I(X/G), \underline{G})$
- (iv) alone: Borcherds-lift automorphic, $H^1(\mathcal{A}_g, \underline{\mathrm{Sp}_{2g}(\mathbb{Z})})$
- Pairwise intersections: fibre-product cocycles
- Triple/quadruple: nested fibre-product cocycles culminating in $K3 \times E$ data

#### §10.2 The sheaf-of-CoHAs perspective
A global CoHA is equivalently a *sheaf of CoHAs* on the (2,1)-stack of equivariance strata. The assembly is local-to-global along this stack. The K3 × E CoHA lives at the "deepest" stratum (all four stacks meet), making it the *master test case* for the entire gluing machinery.

#### §10.3 Cross-volume relevance
- Vol I: the categorical bar–cobar adjunction is a CoHA-gluing at the chiral-algebra level
- Vol II: the 3D HT QFT partition function assembles via factorisation-homology gluing
- Vol III: everything above

#### §10.4 Open frontiers (post-chapter)
- Making precise the (2,1)-stack of equivariance strata
- Computing the gluing cocycle cohomology in each of the 15 cells
- Verifying the 24-stalk assembly of K3 × E at explicit chain level
- Extending to CY$_5$ Fake Monster / rank-25 case

## 2. Section-level chronology

| § | Title | Status target | Primary citations |
|---|---|---|---|
| 1.1–1.3 | Abstract framework | Proposition-level | CG Vol II; Davison 2017 |
| 2.1 | Two-chart conifold | Theorem (current synthesis) | Costello-Li 1605.09656; VdB math/0211064; Szendrői 0705.3419 |
| 2.2 | Multi-chart toric fan | Proposition | GLY 2106.01230; Neguț arXiv:1505.01528 |
| 2.3 | Compact 4-cycle obstruction | Theorem (obstruction) | This chapter |
| 2.4 | Local-to-global | Proposition | Davison-Meinhardt 1601.02479 |
| 3.1–3.3 | McKay / orbifold | Theorem-level | BKR math/9908027; EOT 1005.5415 |
| 4.1–4.3 | VdB tilting | Theorem | VdB math/0211064; DHSM 2303.12592 |
| 5.1–5.4 | Factorisation algebras | Theorem-level (CG Vol II) | BD 2004; CG Vol II; Francis 1104.0181 |
| 6.1–6.3 | Wall-crossing | Theorem | KS 0811.2435; Joyce-Song 0810.5645 |
| 7.1–7.4 | Lattice-polarised | Theorem | Borcherds; Gritsenko-Nikulin |
| 8.1–8.7 | K3 × E master example | Theorem / Conjecture mixture | K3 × E chapter of Vol III (existing) |
| 9.1–9.3 | Obstructions | Proposition / Theorem | Costello-Li; this programme |
| 10.1–10.4 | Unifying framework | Conjecture | This chapter |

## 3. CG-voice discipline

Per CLAUDE.md: every section title names a mathematical object/construction/theorem; no process language. Every definition preceded by the obstruction it resolves. Every symbol defined at first use. Physical claims labelled theorem/heuristic/metaphor. Hedges-the-mathematics-does-not-earn forbidden.

## 4. Open questions the chapter must settle

1. **Is the "24 smooth-$\mathbb{C}^3$ stalks" count correct, or is it 24 curve-stalks on $I_1 \times E$?** (Wave 4 Agent 8 flagged this as a geometric error in the master synthesis.)

2. **What is the exact rank of the imaginary Cartan on K3 × E?** Commonly stated as 23 ("$H^\bullet_{\mathrm{even}}(K3)$ rank 24 minus one fibre-line"), but the exact count depends on conventions.

3. **Does the Serre-equivariant quasi-NCCR admit an explicit presentation?** Per CLAUDE.md this is a standing open item.

4. **Do the four obstructions to compact CY$_3$ gluing admit partial resolutions via MNOP categorified machinery?** Davison integrality is stratum-free; the chart-wise formulas are not.

5. **What is the appropriate 2-categorical home for the $(2,1)$-stack of equivariance strata?** Possibly Derived stacks (Toën-Vezzosi) or Lurie's $(\infty, 2)$-category of stacks.

## 5. Relationship to the existing manuscript

This chapter would:
- **Subsume** the current `chapters/examples/toric_cy3_coha.tex` §conifold two-chart construction as §2.1
- **Subsume** the current `rem:tcy3-coha-mcKay` (K3 × E as 24 smooth-ℂ³ stalks) as §8.5, now properly corrected with Wave 4 Agent 8's curve-stalk rectification
- **Subsume** the current local ℙ² construction as §3.2
- **Subsume** the current Part VI of Vol III (seven faces of $r_{\mathrm{CY}}$) as a *consequence* of the gluing taxonomy — the seven faces are seven different gluing cocycle classes
- **Provide** a unifying narrative tying Parts I–VII of Vol III together

## 6. Suggested chapter name

**"The Gluing Atlas of CoHA: Local Charts, Global Assembly, Automorphic Cocycles"**

Alternatives:
- "Assembling Cohomological Hall Algebras: Chart-Wise Charts and Their Gluings"
- "From Local CoHA to Global CoHA: The Four-Stratum Taxonomy"

Preferred: the first, for its Chriss–Ginzburg-voiced direct naming of mathematical content (Atlas, Charts, Cocycles).

## 7. Execution plan

1. **Immediate**: this architecture document (done, this file)
2. **Next**: delegate 10 inscription agents, one per Part, each producing a polished section draft
3. **Then**: master editorial pass aligning cross-references, notation, CG voice
4. **Finally**: integrate into Vol III main manuscript as Part IX (new) between current Part VIII (K3 × E) and Part IX (Frontiers) — or restructure into its own chapter inside Part V (CY landscape)
