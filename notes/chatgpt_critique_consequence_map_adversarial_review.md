# Deep Adversarial Review of the Consequence Map

**Date:** 2026-05-09
**Subject:** First-principles review of `notes/chatgpt_chiral_duality_critique_consequence_map.md`
**Operating discipline:** Beilinson — dismiss false ideas before they take root, including the false ideas in this very review's predecessor.
**Target form:** the strongest possible reconstitution map and plan, with the inner symmetries of the subject revealed.

---

## I. What was wrong in the original map

A first-principles re-reading of the original consequence map exposes four errors of varying severity. Each is named, attacked, and replaced.

### I.1 The "single hard cross-volume contradiction" was not a contradiction

The original map identified Vol I `chapters/examples/lattice_foundations.tex:5866` as positively asserting `$\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fibre}})$` and called this the AP5-pending cross-volume contradiction.

Reading lines 5862-5871 in context exposes this as wrong. The line lives inside Remark `rem:latfnd-w18-witten-LCM-vs-ell` ("LCM of Conway-Norton spectrum ≠ ℓ_Monster: scope discipline"), and the surrounding text reads:

> "Propagating the K3 CY-3-fibre coincidence $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fibre}})$ (which is an $N = 1$-specific identity for the K3 Mukai datum...) to the Monster case is a separate scope violation"

Vol I asserts the formula as **an $N=1$ accident under the Mukai-datum convention** that does not propagate. Vol III `chapters/examples/k3e_bkm_chapter.tex:14340` says "no additive shift relates 5 and 12" — i.e., does not propagate from $N=1$ to the Fake-Monster $\Phi_{12}$ row. Cache row 64 even uses the wording "$N = 1$ accident only".

These three statements are **consistent**. There is no contradiction. The original map's Phase 2 (priority repair of this line) was misdirected.

What is the **real** issue at line 5866? It is HZ-7 subscript overload. Vol I uses bare `$\kappa_{\mathrm{ch}}$` without naming whether it means $\kappa_{\mathrm{ch}}^{\mathrm{Mukai}}$, $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}$, $\kappa_{\mathrm{ch}}^{\mathrm{Hodge}}$, or another reading. The numerical truth of the $N=1$ accident depends on the choice. Under the K3-Mukai-datum convention, $\kappa_{\mathrm{ch}}^{\mathrm{Mukai}}(K3) = 5$ and the formula holds at $N=1$ with $\chi(\mathcal{O}_E) = 0$ on the elliptic fibre. Under the Heisenberg-Mukai convention, $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3$ and the formula fails. Both readings are correct in their own scope; bare $\kappa_{\mathrm{ch}}$ is the violation.

**Correction.** The Vol I repair is a subscript fix (bare $\kappa_{\mathrm{ch}} \to \kappa_{\mathrm{ch}}^{\mathrm{Mukai}}$ at line 5866), not a formula replacement. The formula is correct under the named convention.

**Wider lesson.** Before declaring any cross-volume contradiction, read the contradiction candidate **with surrounding context**. Cross-volume mismatches are usually convention overloads or compatible dual readings (the cache's Compatible-dual-readings table, line 103+ of `appendices/first_principles_cache.md`, exists exactly to catch this).

### I.2 Phase 1 preface paragraph insertion is wrong architecture

The original map's Phase 1 was: "insert level-discipline preface paragraphs into all 5 manuscripts." This is the wrong move.

CLAUDE.md's Chriss-Ginzburg discipline forbids meta-narration in manuscript prose: "no 'we now turn to', 'having established', 'let us now'". A "level discipline preface paragraph" is exactly the kind of meta-narration that does not belong in a Russian-school manuscript.

The level discipline is a **meta-rule** for *checking* whether a theorem statement is well-scoped. It does not appear in the manuscript; the **level-aware mathematical statements** appear in the manuscript. The meta-rule lives in `notes/`, `CLAUDE.md`, or the architecture document.

**Correction.** Phase 1 becomes: rewrite **theorem statements** (and definitions) so each one declares its (level, chart, ambient) scope. The change is in the math, not in a preface paragraph. A theorem that previously read

> "Theorem (CY-to-chiral). $\Phi_3$ produces an $E_1$-chiral algebra."

becomes

> "Theorem (CY-to-chiral, $d=3$, chart $(\Sigma_2, C)$). $\Phi_3^{(\Sigma_2, C)} = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_2, C} \circ \Phi^{\mathrm{FA}}_3$ produces an $E_1$-chiral algebra on $C$ in the verified-locus ambient, unique up to a contractible space of $E_1$-lifts (Theorem CY-A$_3$)."

The scope coordinates ($d$, chart, ambient) are declared in the theorem name itself.

### I.3 AP-CY-Crit numbering scheme is wrong

The original map drafted "AP-CY-Crit-1 through AP-CY-Crit-17", labelling entries by the critique's own enumeration. This is a critique-specific numbering scheme that scars the catalogue with one author's enumeration.

The catalogue is type-organized: "primitive/chart", "scope/convention", "ambient qualifier", etc. (see column 6 of the existing rows in `notes/antipatterns_catalogue.md`). New entries should be appended to existing types, not given a new numbering convention.

**Correction.** Each of the 17 dismissals maps to one of the existing AP-CY types. Append to the type-organized catalogue with the next sequential AP-CY-N number, citing the critique as evidence. The 17-entry block becomes invisible to the catalogue's organising principle.

### I.4 "Shadow = object" master pattern is too narrow

The original map named "shadow = object" as the master pattern. This covers many dismissals (1, 2, 6, 7, 8, 11, 12) but fails to cover others naturally. Dismissal 9 (6d hCS ≠ 3d CS) is theory-misimport, not shadow-as-object. Dismissal 10 (formal Darboux ≠ global) is local-as-global, not shadow-as-object. Dismissal 14 (W_∞[λ] ⇒ E_∞ requires hypotheses) is endpoint-admissibility, not shadow-as-object. Dismissal 15 (class M chain-level) is ambient-mismatch, not shadow-as-object.

The deeper master pattern is **scope omission**. Every dismissal is a place where some scope coordinate (level, chart datum, ambient, hypothesis, theory-context) is omitted from a claim, allowing a level-N statement to masquerade as level-M, or a chart-A claim to masquerade as universal, or a completed-ambient theorem to masquerade as ordinary.

The healed form **always** explicates the missing coordinate. This unifies all 17 dismissals.

---

## II. The hidden inner form: three-axis scope architecture

Once "scope omission" is recognized as the master pattern, the natural question is: **what scope coordinates are there?** First-principles enumeration gives three orthogonal axes.

### II.1 The three axes

**Axis 1: Vertical level (the universal arrow).**
$$
\underbrace{\text{primitive}}_{0} \;\rightsquigarrow\; \underbrace{\text{functorial passage 1 (canonical)}}_{1} \;\rightsquigarrow\; \underbrace{\text{functorial passage 2 (chart)}}_{2} \;\rightsquigarrow\; \underbrace{\text{centre / quantum double}}_{3} \;\rightsquigarrow\; \underbrace{\text{scalar trace}}_{4}
$$
The vertical axis is intrinsic to the programme — it tracks how categorical input is reduced to scalar output through stages of structural extraction.

**Axis 2: Horizontal chart datum.**
At each level, multiple chart choices give different concrete realisations. At level 1: equivariance stratum (toric / reduced + Aut / orbifold inertia / lattice-polarised period domain). At level 2: $(\Sigma_{d-1}, C)$ datum + boundary vacuum $b$ + endpoint admissibility window. At level 3: chosen Drinfeld double / chosen Fock evaluation $\lambda$. At level 4: chosen Siegel input denominator $\Phi_N$.

**Axis 3: Ambient discipline.**
Each theorem holds in a named ambient: ordinary chain complexes, weight-completed, pro-, $J$-adic, HS-sewing, formal-local, global-with-descent, completed-perfect, derived $\infty$-categorical. Some statements are true in one ambient and false in another (class M chain-level: false in ordinary, true in weight-completed).

### II.2 The 17 dismissals as scope-omission errors classified by axis

Every dismissal omits one or more axes:

| # | Dismissal | Vertical | Horizontal | Ambient |
|---|---|:-:|:-:|:-:|
| 1 | $A$ = primitive open object | ✗ | ✗ | |
| 2 | Bar = bulk | ✗ | | |
| 3 | $E_1$-bar explains $2d→3d$ | | ✗ | |
| 4 | Open sector on bare $X$ | | ✗ | ✗ |
| 5 | Closed algebra is modular | ✗ | | |
| 6 | Five $\kappa$-numbers are one | | ✗ | |
| 7 | $\Phi$ direct one-stage | | ✗ | |
| 8 | $Y^+ = G$; $\mathrm{CoHA}(\mathbb{C}^3) = \mathcal{W}_{1+\infty}$ | ✗ | | |
| 9 | 6d hCS = 3d CS | | ✗ | |
| 10 | Formal Darboux ⇒ global | | | ✗ |
| 11 | $\Delta_5$ = compact BPS Hilbert space | ✗ | | |
| 12 | $Z_{\mathrm{BPS}}$ = operator algebra | ✗ | | |
| 13 | Universal Holography = quantum gravity | ✗ | | ✗ |
| 14 | $W_\infty[\lambda] ⇒ E_\infty$ | | | ✗ |
| 15 | Class M chain-level in ordinary complexes | | | ✗ |
| 16 | PVA Jacobi ⇒ all-loop quantum | ✗ | | ✗ |
| 17 | Quadratic chiral dual ⇒ Koszulness | ✗ | | ✗ |

The classification reveals **structure**: 8 dismissals are pure vertical-axis omissions (level confusion), 6 are horizontal-axis omissions (chart/datum confusion), 5 are ambient-axis omissions (often co-occurring with vertical). No dismissal is pure ambient — ambient-only confusions don't generate the kind of false equality the critique attacks; they generate "this theorem is missing its ambient qualifier" failures, which are recoverable.

This taxonomy is what the original map should have organized around.

### II.3 The universal arrow with its sub-structure

Within each level, there is **internal structure**. The bar/twisting and the centre/double live at adjacent levels with a comparison arrow between them.

**Open/closed instantiation:**
- Level 0: open factorisation dg-category on $(X, D, \tau)$ with closed-colour input $(\mathcal{C}^{\mathrm{op}}, \Theta_{\mathcal{C}}, \mathrm{Tr}_{\mathcal{C}})$
- Level 1: chart-augmented data $(b, A_b = \mathrm{End}_{\mathcal{C}}(b))$
- Level 2: bar/twisting shadow $B(A_b)$, the universal twisting coalgebra
- Level 3: derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(A_b) \simeq \mathrm{ChirHoch}^\bullet(A_b, A_b) = \RHom(\Omega B(A_b), A_b)$, the bulk
- Level 4: trace / closed-shadow modular form

**CY/chiral instantiation:**
- Level 0: $\mathrm{CY}_d$-category $\mathcal{C}$ with PTVV $(2-d)$-shifted symplectic structure
- Level 1: Stage-1 native FA $\Phi^{\mathrm{FA}}_d(\mathcal{C}) \in E_d\text{-HolFA}(X)$, canonical up to GRT$_1(\mathbb{Q})$-torsor (Kontsevich–Tamarkin formality + Costello–Gwilliam–Li locality)
- Level 2: Stage-2 chiral algebra $A_X = \Phi^{(\Sigma_{d-1}, C)}_d(\mathcal{C}) \in \text{ChirAlg}^{E_{n(d)}}(C)$, chart-dependent
- Level 3: positive half $Y^+(X) = H^\bullet_{\mathrm{eq}}(\mathcal{M}^+_{\mathrm{eff}}(X), \phi_W)$ → quantum vertex group $G(X) = D(Y^+(X))$ → derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(A_X)$ — three names for one bulk-level object
- Level 4: scalar trace / Borcherds form / partition function $Z_{\mathrm{BPS}}^X$

The bar $B(A_X)$ in the CY chain is at level 2, computing the centre at level 3 via the Quillen equivalence $Z^{\mathrm{der}}_{\mathrm{ch}}(A_X) \simeq \RHom(\Omega B(A_X), A_X)$. The bar IS the comparison arrow between levels 2 and 3; that is the deepest content of the critique's Dismissal 2.

---

## III. Chain fusion: the five manuscripts tell one story

The original map presented two arrow chains as parallel structures. In fact they fuse, and the fusion is the inner form of the entire programme.

### III.1 Fusion at level 2

The CY/chiral chain's level-2 output (Stage-2 chiral algebra $A_X$ on a curve $C$) **is** the open/closed chain's level-1 chart algebra (boundary algebra $A_b$ on the same curve $C$, with appropriate boundary vacuum $b$ and tangential log structure $(C, D_C, \tau_C)$).

Concretely:
$$
A_X = \Phi^{(\Sigma_{d-1}, C)}_d(\mathcal{C}_X) = A_{b(X)}, \qquad b(X) = \text{boundary vacuum induced by } (\mathcal{C}_X, \Sigma_{d-1}, C)
$$

Once this identification is made, levels 2-4 of the two chains coincide. The Vol III "the chiral algebra of $X$" and the Vol I/II "boundary algebra of an open factorisation category" are the **same object**, viewed from two sides. The CY-side gives an existence theorem (Stage-1 + Stage-2 produces $A_X$); the open-side gives the structure (Swiss-cheese pair, modular trace + clutching, derived centre).

### III.2 Five manuscripts as five faces

With chain fusion in place, the five manuscripts read as five faces of one structure:

- **Vol III (calabi-yau-quantum-groups)** — The CY-input face. Constructs levels 0-1 of the universal arrow on CY data: how does a CY$_d$-category produce its native factorisation algebra and its chart-dependent chiral specialisations?
- **Vol I (chiral-bar-cobar)** — The bar/twisting face. Constructs the level-2 shadow and its Koszul comparison data: what is the bar, what is the modular open-closed convolution, how does the trace + clutching structure on the open side produce modular consequences for the closed shadow?
- **Vol II (Ainfinity-chiral / chiral-bar-cobar-vol2)** — The centre face. Constructs level 3 of the universal arrow: the Hochschild centre, the universal holography pair (boundary $A$, bulk $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$), the algebraic holographic HT sector.
- **igusa-cusp-form** — The terminal scalar face. Constructs level 4: the protected Borcherds denominator $\Delta_5$, the virtual $K_0$-determinant, the Borcherds weight $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ at chosen Siegel input. **Disclaims** the level-3 promotion (compact BPS Hilbert space, operator algebra, Hall pairing) as a research target.
- **mixed-holomorphic-topological-strings** — The physical realisation face of level 1. Constructs the concrete $\mathbb{R}^2_{\mathrm{top}} \times \mathbb{C}^2_{\mathrm{hol}}$ formal model with Hamiltonian BF sector, completing at a brane, and **names** the global obstruction (holomorphic de Rham class) for level-1 data on non-formal targets.

The five manuscripts are not five chains; they are five **slices of one chain**, each manuscript developing its own slice in depth.

### III.3 The "shadow ⇒ object" arrow is the comparison map between adjacent levels

In this picture, "shadow" and "object" are not arbitrary — shadow is always level $k$ and object is always level $k+1$ or $k-1$. The seventeen dismissals are seventeen places where a level-$k$ data is asserted as level-$(k+1)$ or level-$(k-1)$ data without the comparison map being constructed.

Concretely:
- Dismissal 11 ($\Delta_5$ = Hilbert space) collapses level 4 to level 3 (scalar to operator).
- Dismissal 12 ($Z_{\mathrm{BPS}}$ = operator algebra) collapses level 4 to level 3.
- Dismissal 8 ($Y^+ = G$) collapses level 3-positive-half to level 3-full (within level 3).
- Dismissal 2 (bar = bulk) collapses level 2 to level 3.
- Dismissal 7 ($\Phi$ direct one-stage) collapses level 1 to level 2 (skipping the chart).

The healed form always supplies the comparison arrow: scalar = trace of operator (level 3 → level 4), operator algebra = Drinfeld double of positive half (level 3 → level 3), bulk = derived centre of bar's $\Omega$ (level 3 = $\RHom(\Omega B, A)$), $\Phi^{(\Sigma, C)}_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma, C} \circ \Phi^{\mathrm{FA}}_d$ (level 2 = level-1 + chart-specialisation).

---

## IV. Inner symmetries unexpressed in the original map

Five symmetries the original map missed.

### IV.1 The three tiers of $r_{\mathrm{CY}}$ ARE the level-axis projection of the seven-face programme

Vol III `working_notes.tex:742-752` already inscribes the three-tier structure of $r_{\mathrm{CY}}$ faces:
- **Tier (i), CY-datum intrinsics.** Mukai lattice pairing; Hodge supertrace $\kappa_{\mathrm{ch}}$. **Lives at level 0** (intrinsic to $\mathcal{C}_X$).
- **Tier (ii), Stage-1 invariants.** K3-fibre rank $\kappa_{\mathrm{fiber}} = 24$. **Lives at level 1** (invariant of $\Phi^{\mathrm{FA}}_d(\mathcal{C}_X) = \mathcal{F}_X$, before specialisation).
- **Tier (iii), $(\Sigma_{d-1}, C)$-specialisations.** BKM face $(K3, E) \mapsto \mathfrak{g}_{\Delta_5}$ with $\kappa_{\mathrm{BKM}} = 5$; Niemeier 23-twist family; Humbert boundary-monodromy; CHL $\mathbb{Z}/N$ family. **Lives at level 2** (Stage-2 chart-dependent shadows).

The "algebraic seven-presentation" (bar–cobar, CoHA, coisson, MO stable envelope, Yangian, Sklyanin, Gaudin) is an **orthogonal slicing** of the same factorisation-algebra data — i.e., a horizontal-axis enumeration AT level 2.

So the seven faces decompose along TWO axes:
- Vertical: three tiers (level 0, level 1, level 2)
- Horizontal: seven algebraic presentations (mostly at level 2)

The original map mentioned the seven faces only in passing. The structural insight — that the seven faces are level-2 chart-shadows in the $r_{\mathrm{CY}}$ sub-architecture — is invisible in the original map.

### IV.2 K3 × E five $\kappa$-values vs $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$ five archetypes — two distinct fives

The critique's Dismissal 6 talks about "the five $\kappa$-numbers" on $K3 \times E$: $\{0, 0, 3, 5, 24\} = (\kappa_{\mathrm{cat}}, \kappa_{\mathrm{ch}}^{\mathrm{Hodge}}, \kappa_{\mathrm{ch}}^{\mathrm{Heis}}, \kappa_{\mathrm{BKM}}(\Delta_5), \kappa_{\mathrm{fiber}})$.

Vol I `chapters/theory/chiral_center_theorem.tex:2885+` has a different "five-element bucket" $\{0, 8, 13, 250/3, 98/3\}$ on $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$ — these are the values of $K^\kappa = \kappa + \kappa^!$ for five archetype VOA classes (Heisenberg / affine Kac–Moody / Virasoro / principal $\mathcal{W}_N$ / K3 BKM-Mukai).

These are **two completely different fives**:
- The K3 × E five is **five constructions at one chart point** ($d = 3$, $X = K3 \times E$). It is a horizontal enumeration WITHIN one chart slot.
- The $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$ five is **five archetype classes across the entire chiral landscape**. It is a horizontal enumeration ACROSS chart slots.

Conflating them would be a higher-order scope error (collapsing two different stratifications). The original map and the critique both refer to "the five $\kappa$" without disambiguating, and risk this conflation. The reconstitution must keep them distinct: the K3 × E five is the chart-internal enumeration of constructions; the archetype five is the cross-landscape enumeration of types.

A subtlety: the $\mathsf{B}$-row in the archetype five (K3 BKM-Mukai, $K^\kappa = 8$) **is** related to the K3 × E five — specifically to the Mukai-doubling face of $K3$ as it sits in $K3 \times E$. So the two fives have one common cell. But they are not the same enumeration.

### IV.3 The chart datum has internal product structure

At level 2 (Stage-2 chiral specialisation), the chart datum is $(\Sigma_{d-1}, C, b)$. But this triple has further structure:

The four equivariance strata named in CLAUDE.md (toric $T^d$ / reduced $\mathbb{C}^\times +$ Aut / orbifold inertia $I(X/G)$ / lattice-polarised period domain) are **strata of the chart space**. Within each stratum, the chart has additional fine structure: for toric $T^d$, the equivariant cohomology + GIT stability chamber + framing class; for reduced $\mathbb{C}^\times +$ Aut, the Aut-action data; for orbifold inertia, the conjugacy class data; for lattice-polarised, the period datum.

So the chart space is fibered:
$$
\text{Chart} \;=\; \text{equivariance stratum} \times_{\text{stratum}} (\Sigma_{d-1}, C) \times_{\text{stratum}} (\text{boundary vacuum } b) \times_{\text{stratum}} (\text{endpoint admissibility window})
$$

A theorem at level 2 must declare **all four** chart coordinates, not just $(\Sigma_{d-1}, C)$. The original map collapsed this fibered structure into a single "chart datum".

### IV.4 Stage-1 functor + Stage-2 chart-specialisation: resolving the Vol III "correspondence programme, not functor" tension

Vol III `chapters/theory/cy_to_chiral.tex:2840-2856` says:

> "The collection $\{\Phi_d\}_{d \geq 1}$ is a correspondence programme, not a single functor: the target category $E_{n(d)}\text{-}\mathrm{ChirAlg}(\mathcal{M}_d)$ depends on $d$."

The critique's "two-stage functor" framing risks tension with this. The resolution:

- $\Phi^{\mathrm{FA}}_d : \mathrm{CY}_d\text{-cat} \to E_d\text{-HolFA}(X)$ is a **functor** (canonical up to GRT$_1(\mathbb{Q})$-torsor) at fixed $d$. The functoriality is the Kontsevich–Tamarkin formality + Costello–Gwilliam–Li locality content. This is Stage-1.
- $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} : E_d\text{-HolFA}(X) \to \text{ChirAlg}^{E_{n(d)}}(C)$ is a **chart-dependent specialisation** at fixed $(\Sigma_{d-1}, C)$. Functoriality on CY morphisms reduces to (per-$d$ conjecture) $R$-matrix-gauge transport. This is Stage-2.
- The composition $\Phi^{(\Sigma_{d-1}, C)}_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$ inherits Stage-1 functoriality and Stage-2 chart-dependence. At fixed $(\Sigma_{d-1}, C)$, this is an object-level construction with morphism-level conjecture.
- The collection $\{\Phi^{(\Sigma_{d-1}, C)}_d\}_{d \ge 1, (\Sigma, C)}$ is a **two-parameter correspondence programme** (parameters: $d$ and chart datum), not a single functor.

This is the precise statement. The original map said "two-stage Φ" without articulating where the functoriality lives at each stage. The corrected statement says: Stage-1 IS a functor; Stage-2 is chart-specialisation; the composition is the per-chart construction; the collection across charts is a correspondence programme.

This is a strictly stronger claim than either "Φ is a functor" or "Φ is just a correspondence programme". It honours the critique's two-stage framing AND Vol III's correspondence-programme remark, by locating the functoriality precisely.

### IV.5 mixed-HT-strings is the level-1 physical face, not a separate chain

The original map listed mixed-HT-strings as one of the parallel chains. With chain fusion, the right placement is:

**mixed-HT-strings is the *physical realisation* of Stage-1 ($\Phi^{\mathrm{FA}}_d$) at toric loci.**

The local model $\mathbb{R}^2_{\mathrm{top}} \times \mathbb{C}^2_{\mathrm{hol}}$ with Hamiltonian BF sector is ONE concrete realisation of the canonical Stage-1 datum. Other realisations:
- 5d hCS (Costello–Gaiotto–Yagi) → Yangian VOA at $d = 2$.
- 6d hCS on $\mathbb{C}^3$ → CY$_3$ chiral algebra Stage-1 at $d = 3$.
- Costello–Gwilliam–Li perturbative quantisation (mathematical formality side).
- Kontsevich–Tamarkin $E_d$-formality (algebraic side).

These are FOUR FACES of one Stage-1 datum, related by the Beilinson "two lanes equally load-bearing" rule (CLAUDE.md). The mixed-HT-strings programme is the physical lane at $d = 2$ (and partly $d = 3$). It is not parallel to Vol III; it is INSIDE Vol III's level 1.

This repositioning has consequences:
- The "global obstruction" of mixed-HT (holomorphic de Rham class) is the level-1 → level-1 obstruction at non-formal targets within Stage-1. This is a Stage-1-internal global obstruction, not a separate global theory issue.
- mixed-HT theorems at level 1 inherit the level discipline: every local Hamiltonian BF assertion at level 1 must declare its descent / QME / anomaly / locality package.

---

## V. Low-hanging fruit unexpressed in the original map

Five concrete strengthening moves the original map missed.

### V.1 Subscript-overload sweep on $\kappa_{\mathrm{ch}}$

Bare $\kappa_{\mathrm{ch}}$ is forbidden (CLAUDE.md "Essential constants"; cache row 1; AP-CY68/AP234). The subscript variants in active use:
- $\kappa_{\mathrm{ch}}^{\mathrm{Hodge}}$ — Hodge supertrace $\sum_q (-1)^q h^{0,q}(X)$ on compact CY$_d$
- $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}$ — Heisenberg–Mukai specialisation (e.g. $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3$)
- $\kappa_{\mathrm{ch}}^{\mathrm{Mukai}}$ — Mukai-datum convention on K3 (e.g. $\kappa_{\mathrm{ch}}^{\mathrm{Mukai}}(K3) = 5$ in the $N=1$ accident reading)
- $\kappa_{\mathrm{ch}}^{\mathrm{cpt}}, \kappa_{\mathrm{ch}}^{\mathrm{loc}}$ — cache row 1 BCOV / surface-reduced split for compact vs local CY$_3$
- $\kappa_{\mathrm{ch}, \mathrm{BV}}$ — one-loop BV-corrected (memory `project_kappa_ch_bv_five_invariant_extension.md`)

**Sweep target:** `grep -rn "\\\\kappa_{\\\\mathrm{ch}}[^a-zA-Z_]" *.tex chapters/`. Every bare-$\kappa_{\mathrm{ch}}$ occurrence is a latent AP violation. Vol I `lattice_foundations.tex:5866` is one example; there are likely dozens more.

This sweep alone resolves several "apparent contradictions" across volumes that are actually subscript-overload artefacts.

### V.2 Single canonical architecture document

Instead of inserting preface paragraphs into 5 manuscripts, write **one** master architecture document that all 5 cite. Candidate location: `/Users/raeez/ecosystem/UNIVERSAL_ARROW.md` (or `LEVEL_DISCIPLINE.md`), inheriting the same status as `~/ecosystem/INVARIANTS.md` (referenced by all five CLAUDE.md files).

Contents:
- The universal arrow (5 levels)
- The three axes (level, chart, ambient)
- The chain fusion (CY/chiral and open/closed share levels 2-3)
- The level-discipline gate (a theorem must declare its scope coordinates)
- The Beilinson cut: primitive objects first, shadows second, scalar modular forms last

Every CLAUDE.md gains one line: "Inherits `~/ecosystem/UNIVERSAL_ARROW.md`." Every preface gains zero new prose.

This is dramatically cleaner architecturally than 5 preface paragraphs.

### V.3 Three-axis discipline as theorem-statement check

A theorem statement is **scope-checked** by a three-line inspection:
1. **Level check:** what level does the statement live at? (0 / 1 / 2 / 3 / 4)
2. **Chart check:** which chart datum is named? (equivariance stratum / $(\Sigma_{d-1}, C)$ / boundary $b$ / Drinfeld double / $\Phi_N$ denominator)
3. **Ambient check:** which ambient is named? (ordinary / completed / pro / $J$-adic / HS-sewing / formal-local / global-with-descent)

A theorem is **well-scoped** iff its (level, chart, ambient) coordinates are explicit (or the relevant axis is genuinely scope-independent, e.g., a level-0-and-up universal statement).

The 17 dismissals are 17 archetypal failures of this check. The check is a finite, repeatable discipline that any agent (or human reader) can apply.

This becomes the new gate at the end of every theorem rectification: scope-check the statement before declaring convergence.

### V.4 "Bar = twisting" as the central organising insight

The critique's Dismissal 2 (bar ≠ bulk) is the deepest structural insight. Once internalised, it organises a large fraction of the programme:
- The bar of an $E_1$-algebra is a single-colour $E_1$-chiral coalgebra (the universal twisting/coupling data).
- The cobar $\Omega B(A)$ recovers $A$ when Koszul.
- The centre $Z^{\mathrm{der}}_{\mathrm{ch}}(A) = \RHom(\Omega B(A), A)$ is the bulk.
- The Swiss-cheese pair (boundary $A$, bulk $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$) governs open/closed dynamics.
- The seven faces of $r_{\mathrm{CY}}$ are seven manifestations of $\text{bar of } \Phi(\mathcal{C}_X)$ at different chart specialisations.
- Modular trace + clutching on the open category is the closed-shadow modular consequence — it is ALSO a level-2 (bar/twisting) structure, not a level-3 (bulk) property.

The Vol I/II prose should anchor every Koszul-duality / Swiss-cheese / chiral-centre construction to "bar = twisting; centre = bulk". This is a single rectification sweep target across both volumes.

### V.5 Cardinal-quantifier hygiene

Cache row 7: "Abstract enumeration-lead opens with a cardinal that does not match the actual enumeration count." The original consequence map is itself susceptible — I wrote "five $\kappa$-numbers" without distinguishing the K3 × E five from the $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$ five.

Every cardinal-quantifier in the manuscripts ("seven faces", "five archetypes", "four equivariance strata", "five $\kappa$ values") must be reconciled to a specific stratification with named items. The reconstitution provides an opportunity to install this discipline globally.

---

## VI. Revised plan

The original five-phase plan is restructured around the inner form. Six phases now:

### Phase 0: Master architecture document (new)

Write `/Users/raeez/ecosystem/UNIVERSAL_ARROW.md` (single canonical reference, ~3-5 pages):

1. The universal arrow (5 levels) with both instantiations (CY/chiral and open/closed) and the chain fusion at levels 2-3.
2. The three axes (level, chart, ambient).
3. The level-discipline gate (theorem-statement scope check).
4. The Beilinson cut: primitive objects first, shadows second, scalar modular forms last.

Each manuscript's CLAUDE.md gains one line: "Inherits `~/ecosystem/UNIVERSAL_ARROW.md`."

**Time:** 1 session. **Leverage:** maximal (all subsequent phases inherit this).

### Phase 1 (revised): Theorem-statement scope rewrite

For each manuscript, identify the central theorems and rewrite the **theorem name and statement** to declare (level, chart, ambient). No preface paragraphs. The level-aware theorem text replaces the previously underscoped text.

Examples:
- Vol III `chapters/theory/hochschild_calculus.tex:1570` "$\Phi_3 : \mathrm{CY}\text{-cat}_3 \to \mathrm{ChirAlg}^{E_1}$" $\to$ "$\Phi^{(\Sigma_2, C)}_3 = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_2, C} \circ \Phi^{\mathrm{FA}}_3 : \mathrm{CY}\text{-cat}_3 \to \mathrm{ChirAlg}^{E_1}(C)$, on the verified-locus ambient" (level 2, chart $(\Sigma_2, C)$, ambient verified-locus).
- Vol II `modular_swiss_cheese_operad.tex:4177` "master theorem realizes 3D quantum gravity" $\to$ "master theorem identifies the algebraic holographic HT sector for $A = \mathrm{Vir}_c$" (level 3, chart $A = \mathrm{Vir}_c$, ambient algebraic-without-saddle-dominance).
- Vol I `frontier_modular_holography_platonic.tex:5244` "$\cA_{\mathrm{M5}}(N) = W_{1+\infty}[\lambda = N]$" $\to$ "$\cA_{\mathrm{M5}}(N) \simeq \mathrm{ev}_{\lambda = N}(D(Y^+(\widehat{\mathfrak{gl}}_1)))$, the Fock-evaluation image at $\lambda = N$ of the Drinfeld double of the affine-Yangian positive half" (level 3-after-doubling-and-evaluation, chart $\lambda = N$).

This is a **finite punch list**: identify the ~20-50 high-impact theorem statements per manuscript, rewrite them. Bulk prose follows.

**Time:** 3-5 sessions. **Leverage:** high.

### Phase 2 (revised): Subscript-overload sweep

Run `grep -rn "\\\\kappa_{\\\\mathrm{ch}}[^a-zA-Z_]" *.tex chapters/` across all 5 manuscripts. For each occurrence, determine the intended subtype ($\mathrm{Hodge}$ / $\mathrm{Heis}$ / $\mathrm{Mukai}$ / $\mathrm{cpt}$ / $\mathrm{loc}$ / $\mathrm{BV}$) and add the subscript.

**Expected count:** dozens to hundreds across the 5 volumes (mostly Vol I and Vol III).

Same sweep applies to bare $\Phi$ (must be $\Phi^{\mathrm{FA}}_d$ or $\Phi^{(\Sigma, C)}_d$), bare $\kappa$ (must be subscripted), bare "the bulk" (must be "$Z^{\mathrm{der}}_{\mathrm{ch}}$" or "the derived chiral centre").

**Time:** 2-3 sessions. **Leverage:** very high (catches latent contradictions across volumes).

### Phase 3 (revised): Per-dismissal three-axis sweep

For each of the 17 dismissals, run a targeted sweep using the three-axis discipline:
- Vertical-axis dismissals (1, 2, 5, 8, 11, 12, 13, 16, 17): find theorem statements that confuse adjacent levels; install the comparison arrow.
- Horizontal-axis dismissals (3, 4, 6, 7, 9): find statements that omit the chart datum; declare it.
- Ambient-axis dismissals (10, 14, 15): find statements that omit the ambient; declare it.

Order by (severity × cross-volume reach × number of hits). The original map's ranking is approximately correct here.

**Time:** 5-10 sessions across the 5 volumes. **Leverage:** medium-high.

### Phase 4: Cross-volume citation graph with chain-fusion backbone

Once theorems are scope-aware, install the citation graph:
- Vol III's universal Borcherds-weight identity → Vol I + Vol II κ_BKM references.
- Vol III's Stage-1/Stage-2 → Vol I + Vol II Φ-references.
- Vol I's tangential log curve $(X, D, \tau)$ → Vol II + Vol III open-sector references.
- Vol II's HS-sewing / weight-completed class M → Vol I + Vol III ambient references.
- igusa-cusp-form's `main.tex:96` disclaimer → Vol II + Vol III Δ_5 references.
- mixed-HT-strings's `main.tex:3207-3266` obstruction → Vol II + Vol III local-Hamiltonian-BF references.
- The chain fusion (level 2 = boundary algebra) → cross-cited from Vol III Stage-2 outputs and Vol I/II open-side primitives.

**Time:** 1-2 sessions. **Leverage:** medium (mostly notational; structural value comes from Phase 1-3).

### Phase 5: Bookkeeping integrated into existing AP catalogue

Append the 17 new entries to `notes/antipatterns_catalogue.md` integrated into the existing type classification (not as "AP-CY-Crit-N"). Mirror to Vol I and Vol II catalogues. Append cache rows to `appendices/first_principles_cache.md` integrated into the existing Wave-N append blocks (under a new "ChatGPT critique 2026-05-09" heading).

Memory entries: add `feedback_three_axis_scope_discipline.md`, `project_chain_fusion_level_2.md`, `feedback_subscript_overload_sweep.md`. Keep the existing `project_chatgpt_critique_consequence_map_20260509.md` as the master pointer.

**Time:** 1 session. **Leverage:** low-medium (institutional memory).

### Phase 6: Publication strategy (new)

The reconstitution naturally supports a sharper publication architecture:

**Option A: Five separate publications (status quo).**
- Vol III (CY input + Stage-1/Stage-2)
- Vol I (bar/twisting / open / modular Koszul)
- Vol II (Hochschild centre / universal holography)
- igusa-cusp-form (terminal scalar / Borcherds denominator)
- mixed-HT-strings (physical realisation of Stage-1)

**Option B: One foundational paper + four specialisations (recommended after reconstitution).**
- Foundational paper: the universal arrow + three-axis discipline + chain fusion. Defines vocabulary; states master theorems at maximum scope.
- Four specialisations: each manuscript instantiates the foundational paper at its slice of the chain. Cross-citations via the foundational paper.

**Option C: One monograph encompassing all five (long horizon).**

The reconstitution doesn't force a choice, but it makes Option B feasible by giving the foundational paper its conceptual core (the universal arrow + level discipline). This is a strategic consequence that the original map missed.

**Time:** 1-2 sessions for the foundational paper draft. **Leverage:** strategic (changes the publication unit).

---

## VII. Adversarial counter-attacks on the reconstituted map

The reconstituted map is not above first-principles attack. Six lines of attack and their resolutions.

### VII.1 "The chain fusion at level 2 is unproved"

**Attack.** The claim that Stage-2 chiral output $A_X$ on a curve $C$ **is** the boundary algebra $A_{b(X)}$ for a specific boundary vacuum $b(X)$ is a structural identification that is asserted but not proved. There may be obstructions (the boundary vacuum $b$ may not exist for general $X$; the open-side modular trace may not match the CY-side $r$-matrix data).

**Defense.** This identification is **conjectural** at the level of "for every CY$_3$ datum, there exists a boundary vacuum $b$ such that $A_X = A_{b(X)}$." The conjecture is consistent with all known examples ($\mathbb{C}^3$ / Local $\mathbb{P}^2$ / conifold / $K3 \times E$ at $d=3$), and it is the natural common frame for the CY/chiral and open/closed lanes. The reconstitution map should **state the chain fusion as a programme-level conjecture**, not a theorem.

**Updated map:** the chain fusion entry in §III.1 is upgraded to:
> **Conjecture (chain fusion).** For every CY$_d$-category $\mathcal{C}_X$ and every chart datum $(\Sigma_{d-1}, C)$, the Stage-2 chiral algebra $A_X = \Phi^{(\Sigma_{d-1}, C)}_d(\mathcal{C}_X)$ is the boundary algebra $A_{b(X, \Sigma, C)}$ for a canonical boundary vacuum $b(X, \Sigma, C)$ in an open factorisation dg-category on $(C, D_C, \tau_C)$, where $D_C$ encodes the CY data's special points (orbifold loci, fibration punctures, etc.).

This is a non-trivial conjecture; the partial cases (Costello–Gaiotto–Yagi 5d hCS at $d=2$; Costello–Li 6d hCS at $d=3$) are evidence.

### VII.2 "The three-axis architecture is forced and unnatural"

**Attack.** Three orthogonal axes (level, chart, ambient) feel like an over-engineered taxonomy. Maybe there are really only two axes (level and ambient, with chart subsumed into level), or four (level, chart, ambient, $d$-stratum), or the axes are not orthogonal.

**Defense.** The orthogonality test: can a theorem have a non-trivial scope on one axis without affecting the others?
- A theorem can be at level 3 (centre) at any chart and any ambient → level is orthogonal.
- A theorem can be at chart $(\Sigma_2, C)$ at level 2 in any ambient → chart is orthogonal.
- A theorem can be in HS-sewing ambient at any level and any chart → ambient is orthogonal.

The $d$-stratum candidate fourth axis: $d$ is part of the CY data, so it is part of "primitive at level 0". It is not a separate axis; it is a coordinate on the level-0 input space. So no fourth axis.

Subsumption test: can chart be merged into level? Two theorems at level 2 can have different charts $(\Sigma_2, C)$ vs $(\Sigma_2, C')$ — these are genuinely distinct theorems. Chart cannot be subsumed.

The three-axis architecture is **minimal**: fewer axes lose distinguishing power; more axes over-stratify. Three is the right count.

### VII.3 "Phase 0 master architecture document creates a single point of failure"

**Attack.** Putting the universal arrow into one document at `~/ecosystem/UNIVERSAL_ARROW.md` makes the entire programme depend on this one document. If it's wrong, everything is wrong.

**Defense.** This is the **same risk profile** as `~/ecosystem/INVARIANTS.md`, which already plays this role. The risk is acceptable because the document is **small** (3-5 pages), **simple** (5 levels + 3 axes + Beilinson cut), and **versioned** (changes are propagated via the same mechanism as INVARIANTS.md).

The alternative — distributing the architecture across 5 preface paragraphs — has WORSE failure modes (drift across the 5 copies, no canonical version, conflicts).

### VII.4 "Some 'preserve' items in the original risk register need refinement"

**Attack.** The original map's "preserve" list includes items that are still partially conditional:
- $G(X) = D(Y^+(X))$ is preserved as the definition; but $Y^+(X)$ for compact non-toric CY$_3$ is itself a research target (cache rows 70, 80; AP-CY351-353, 452-453). So $G(X)$ is at level 3 with a CONDITIONAL existence on compact non-toric.
- The class M chain-level theorem in weight-completed ambient is preserved; but the equivalence between the weight-completed and HS-sewing ambients is not always made explicit.
- The two-stage Φ is preserved; but the chart datum's internal product structure (equivariance × $(\Sigma, C)$ × $b$ × admissibility) is not always declared.

**Defense.** "Preserve" is not "preserve unconditionally". The preserve list should be annotated with the conditions under which preservation holds. The reconstituted risk register has an additional column: **conditions**. With conditions named, every "preserve" is upgraded to "preserve at level $L$ in ambient $A$ at chart $C$".

### VII.5 "The 17-dismissal taxonomy may not be exhaustive"

**Attack.** The critique identified 17 false ideas. Are there OTHER false ideas not in this list that the reconstitution will miss? In particular, the critique's input was a reading of one author's work-in-progress; a different reader might identify different dismissals.

**Defense.** The 17 are not claimed to be exhaustive of all possible false ideas in the programme. They are **sufficient to expose the master pattern** (scope omission), which once installed catches an open-ended class of similar errors. The three-axis discipline applied to **every theorem statement** is the actual exhaustive instrument; the 17 dismissals are training examples that calibrate the discipline.

The reconstituted plan does NOT claim to have closed all errors; it claims to have installed the **discipline** that catches errors of the type the critique identifies.

### VII.6 "The Beilinson cut may apply too broadly and discard mathematical content"

**Attack.** "Primitive objects first, shadows second, scalar modular forms last" — applied too aggressively, this might force shadow-level theorems (e.g., scalar Borcherds identities, partition function calculations) into a subordinate position even when they are genuinely independent results.

**Defense.** The Beilinson cut is about **load-bearing assertions**, not about which mathematics is interesting. A scalar Borcherds identity is interesting AS a scalar identity at level 4; it should not be load-bearingly identified with an operator algebra at level 3. But the level-4 result is preserved and developed in its own right.

The cut forbids **promotion** ("$\Delta_5$ IS the Hilbert space"), not **work** at level 4. Igusa-cusp-form is a sophisticated level-4 development; the reconstitution preserves all of it; it just disclaims the level-3 promotion.

---

## VIII. The Beilinson cut, refined

The original map's concluding cut was:

> "Primitive objects first, shadows second, scalar modular forms last."

The reconstituted cut is finer:

> **Every theorem in the programme declares its (level, chart, ambient) coordinates. Promotion across coordinates requires the named comparison arrow, constructed under the named hypotheses. No claim is permitted to be promoted from one coordinate to another by elision.**

This is the strongest possible reconstitution discipline. It subsumes the seventeen dismissals, the three-axis architecture, the chain fusion conjecture, the level-discipline gate, and the publication strategy implications.

It also subsumes the original Beilinson cut, because:
- "Primitive first" = level-0 statements come before level-≥1 statements.
- "Shadows second" = level-2 (bar/twisting) and the chart-dependent specialisations come second.
- "Scalar modular forms last" = level-4 statements terminate the chain.

But the reconstituted cut is **stronger** because it forbids the promotion across coordinates, not just the priority ordering. Two theorems at the same level but different charts cannot be conflated. Two theorems at the same level and chart but different ambients cannot be conflated. The discipline is uniform across all dimensions.

---

## IX. The strongest possible map and plan

Drawing everything together, the strongest reconstitution map and plan has six elements:

1. **The universal arrow** (5 levels: primitive 0 / canonical-functor 1 / chart-functor 2 / centre 3 / scalar 4) with two instantiations (CY/chiral, open/closed) that fuse at levels 2-3.
2. **The three-axis scope architecture** (level / chart / ambient), with each theorem statement declaring its coordinates.
3. **The chain fusion conjecture** explicitly stated as a programme-level conjecture, with partial cases noted.
4. **The five manuscripts as five faces** of one story, with $\sim$/-ecosystem/UNIVERSAL_ARROW.md as the single canonical architecture document.
5. **The six-phase plan** (master document → theorem-rewrite → subscript-sweep → per-dismissal sweep → citation-graph → bookkeeping → publication-strategy), with priority rankings and time estimates.
6. **The refined Beilinson cut**: every theorem declares its (level, chart, ambient) coordinates; promotion requires named comparison arrows under named hypotheses; no elision.

The seventeen dismissals are **subsumed** by axis discipline + Beilinson cut. The original map's punch list is preserved but reorganised. The Vol I lattice κ "contradiction" is correctly diagnosed as subscript overload, not formula error. The seven faces of $r_{\mathrm{CY}}$ stratify across levels 0/1/2 (three tiers) AND seven algebraic presentations (orthogonal slicing). The five-archetype $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$ landmark is distinguished from the five $\kappa$-values on $K3 \times E$ (different fives). mixed-HT-strings is repositioned as the physical lane of Stage-1 within the CY chain. The publication strategy gains a new option (foundational paper + four specialisations) made feasible by the reconstitution.

The map's leverage is now properly identified: Phase 0 (master architecture document) is the highest-leverage move, not Phase 2 (which was misdirected at a non-contradiction). Phase 1 (theorem-statement scope rewrite) replaces the original Phase 1 (preface paragraphs) as the right architectural move. Phase 6 (publication strategy) is added; it was absent from the original.

---

## X. Adversarial residue: the deepest open questions

The reconstitution does NOT close everything. The deepest open questions surface clearly under the discipline:

**Q1.** Is the chain fusion conjecture (§III.1) provable in general? The cases $\mathbb{C}^3$, local $\mathbb{P}^2$, conifold, $K3 \times E$ are evidence; the general $X$ is open. The $b(X, \Sigma, C)$ canonical-boundary-vacuum construction is not in the literature.

**Q2.** Is $G(X) = D(Y^+(X))$ constructed for compact non-toric CY$_3$? Cache rows 70, 80 list the gates (compact critical CoHA, Hall–Drinfeld doubling, radical descent, PBW, no-extra-relations, parity, completion, inverse-limit, Heegner comparison). The construction is not done.

**Q3.** Is the $W_\infty[\lambda] \Rightarrow E_\infty$ endpoint open beyond the four-condition admissible window? Spin-$\le 8$ is verified; full-spin is conjectural.

**Q4.** Does the chain fusion respect modularity? I.e., does the open-side trace + clutching at level 4 match the CY-side scalar Borcherds form $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$?

**Q5.** Is the universal Borcherds-weight identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ a consequence of the chain fusion, or an independent identity? The reconstitution suggests it is a CONSEQUENCE of "level-4 scalar = trace of level-3 operator at chart $\Phi_N$", but proving this requires the chain fusion at level 3-4.

**Q6.** Does the three-axis discipline scale to higher dimensions ($d = 4, 5$)? The Fake Monster lives at $d = 5$; the discipline needs to extend.

**Q7.** Is the bar = twisting principle compatible with the $E_n$-cooperad / cobar duality at $n \ge 2$? At $n = 1$ the bar/cobar adjunction is classical. At higher $n$ the picture is more involved.

These are the genuine frontiers. The reconstitution exposes them sharply, instead of hiding them under shadow=object collapses.

---

*End of deep adversarial review. The reconstituted map (Phase 0 + revised Phases 1-6, plus this review) supersedes the original consequence map. Specific edits flow from the same per-dismissal punch list, but interpreted through the three-axis discipline and ranked by Phase 0-driven priorities.*
