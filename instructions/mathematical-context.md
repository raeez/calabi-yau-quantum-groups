# Mathematical context and source routing

Read the relevant sections before mathematical work. These summaries are source locators, not substitutes for proof.
Verify each affected claim against its current theorem, hypotheses, and independent evidence.
The source contains unresolved status differences. In particular, compare `prop:native-en-level` with nearby broad existence summaries.
Use the exact statement and scope being proved. A summary does not settle a conflict.

## What this repository is

An instrument for advancing human mathematical knowledge: the Calabi–Yau-to-chiral functor

$$\Phi^{(\Sigma_{d-1}, C)}_d \;=\; \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \,\circ\, \Phi^{\mathrm{FA}}_d,$$

and the seven faces of $r_{\mathrm{CY}}$ that crystallise the BPS-quantum-group / chiral-algebra correspondence — K3 BKM $\mathfrak{g}_{\Delta_5}$ from Gritsenko's $\Delta_5$, the K3 Yangian on the Mukai self-mirror branch, the Borcherds Monster, the Fake Monster at $d = 5$.

Every read, grep, edit, inscription, refactor, retraction serves advancing the mathematics, one true theorem at a time. When a choice is between mathematics and accounting, do the mathematics. Use installed hooks as review aids and inspect their output.

## The mathematics

**One functor, two stages.** Stage-1 $\Phi^{\mathrm{FA}}_d : \mathrm{CY}_d\text{-cat} \to E_d\text{-HolFA}(X)$ is a canonical functor at fixed $d$, unique up to a $\mathrm{GRT}_1(\mathbb{Q})$-torsor (Kontsevich–Tamarkin $E_d$-formality + Costello–Gwilliam–Li holomorphic locality). Stage-2 $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}$ is chart-specialisation: factorisation homology over a $(d{-}1)$-cycle restricted to a reference curve. The collection $\{\Phi_d\}$ is a per-$d$ correspondence programme; the target $E_{n(d)}\text{-ChirAlg}$ depends on $d$: $n(3) = 1$ is derived (Dunn factorisation; trivial braiding from $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3)) = 0$); $n(d) = 1$ at $d \geq 4$ is the same Dunn output stated as hypothesis; $n(2) = 2$ and $n(1) = \infty$ are conditional enhancements (the $d = 2$ braided enhancement needs the chain-level $\mathbb{S}^2$-framing action; the $d = 1$ $E_\infty$ claim needs a chain-level argument — the constructed rank-2 Heisenberg output has singular OPE and is not commutative). See `prop:native-en-level`. $\{\Phi_d\}$ does not assemble into a single functor across $d$; the framing "correspondence programme, not unified functor" lives at `chapters/theory/cy_to_chiral.tex:2840-2856`.

**Four $\kappa$-invariants, never conflated.**

- $\kappa_{\mathrm{ch}}$ — chiral-side, via $\Phi$. Subscripted further by reading: $\kappa_{\mathrm{ch}}^{\mathrm{Hodge}} = \sum_q (-1)^q h^{0, q}(X)$ on compact CY$_d$; $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}$ for Heisenberg–Mukai specialisation; $\kappa_{\mathrm{ch}}^{\mathrm{Mukai}}$ for the Mukai-doubling face on K3; $\kappa_{\mathrm{ch}}^{\mathrm{cpt}}, \kappa_{\mathrm{ch}}^{\mathrm{loc}}$ for compact vs local CY$_3$ readings (cache row 1); $\kappa_{\mathrm{ch}, \mathrm{BV}}$ for one-loop BV-corrected.
- $\kappa_{\mathrm{cat}} = \chi(\mathcal{O}_X)$ — categorical Euler. Künneth-multiplicative on products: $\kappa_{\mathrm{cat}}(K3 \times E) = \chi(\mathcal{O}_{K3}) \cdot \chi(\mathcal{O}_E) = 2 \cdot 0 = 0$. Not 2 (which is the K3 fibre value).
- $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ — Borcherds 1995 *Invent. Math.* 120 / Gritsenko 1999 universal weight identity; $N$ names the Siegel input denominator.
- $\kappa_{\mathrm{fiber}}$ — fibre / lattice rank correction.

Bare $\kappa$ forbidden (HZ-7 / AP-CY113). Subscript at every use, including in conversation turns.

**The chain fusion conjecture.** $A_X = \Phi^{(\Sigma_{d-1}, C)}_d(\mathcal{C}_X)$ on the curve $C$ is the boundary algebra $A_{b(X, \Sigma, C)}$ for a canonical boundary vacuum in an open factorisation dg-category on $(C, D_C, \tau_C)$, where $D_C$ encodes the CY data's special points (orbifold loci, fibration punctures, conifold singularities). The conjecture is supported by model cases: constructed local comparison models at $\mathbb{C}^3$, local $\mathbb{P}^2$, conifold (Hall-side identifications; the $\mathbb{C}^3$ hCS$\leftrightarrow$Hall comparison is Open Problem `op:cy3-hcs-hall-comparison`), and a conditional comparison target at $K3 \times E$; no end-to-end verification exists. It is the bridge from Vol III's Stage-2 output to Vol I/II's open-side primitive package $(X, D, \tau; \mathcal{C}^{\mathrm{op}}, b, A_b, Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{C}), \Theta_\mathcal{C}, \mathrm{Tr}_\mathcal{C})$. See `notes/chatgpt_critique_consequence_map_adversarial_review.md` §III.

## Three-axis scope discipline

Every theorem statement carries coordinates on three orthogonal axes. Promotion across coordinates requires the named comparison arrow under named hypotheses. No claim is permitted to be promoted by elision.

**Vertical (level).** $0$ primitive (CY$_d$-cat / open factorisation category) → $1$ canonical functorial passage (Stage-1 / chart-augmented $A_b$) → $2$ chart-specialised shadow (Stage-2 chiral / bar twisting $B(A)$) → $3$ centre / quantum vertex group ($Z^{\mathrm{der}}_{\mathrm{ch}}(A)$, $Y^+(X)$, $G(X) = D(Y^+(X))$) → $4$ scalar trace / Borcherds form. The bar $B(A)$ is the comparison arrow between levels 2 and 3 via $Z^{\mathrm{der}}_{\mathrm{ch}}(A) = \mathrm{ChirHoch}^\bullet(A, A) = \mathrm{R}\mathrm{Hom}(\Omega B(A), A)$; bar is twisting/coupling, not bulk.

**Horizontal (chart datum).** Equivariance stratum × $(\Sigma_{d-1}, C)$ × boundary vacuum $b$ × admissibility window. Four equivariance strata: toric $T^d$ (local $\mathbb{P}^2$, $\mathbb{C}^3$, conifold) / reduced $\mathbb{C}^\times +$ Aut (K3, $K3 \times E$, abelian) / orbifold inertia $I(X/G)$ (Mathieu $M_{24}$, McKay $\Gamma \subset \mathrm{SU}(d)$) / lattice-polarised period domain (Borcherds lifts, Gritsenko $\Delta_5$, Igusa $\Phi_{10}$).

**Ambient (depth).** Ordinary chain complex / weight-completed / pro / $J$-adic / HS-sewing / formal-local / global-with-descent / derived $\infty$-categorical. Class $\mathcal{M}$ chain-level holds in weight-completed, fails in ordinary (Vol II `weight_completed_topologization_class_m_platonic.tex`). $W_\infty[\lambda] \Rightarrow E_\infty$ holds in the four-condition admissible window (Prochazka triangular truncation + Creutzig–Kanade–Linshaw parafermion + Pope–Romans–Shen / Bakas + Yamada weight-window).

The deepest false ideas in this programme are **scope-omission collapses** — treating a level-$k$ object as level-$(k \pm 1)$, treating a chart-dependent statement as universal, treating a completed-ambient theorem as ordinary. The three-axis discipline catches them. See `notes/chatgpt_critique_consequence_map_adversarial_review.md` for the seventeen archetypal collapses surfaced by the May 2026 Beilinson critique and their reconstitution.

## Named status boundaries

CY-C remains conjectural. Check `conj:qgf-cy-c` in `chapters/theory/braided_factorization.tex` and the comparison hypotheses in `chapters/theory/drinfeld_center.tex`.
The legacy Super-Yangian target $Y_{\mathrm{osp}}(4 \mid 20)$ remains conjectural, not an established K3 identification.
Keep it separate from the Mukai-preserving Hodge-parity target in `chapters/theory/cy3_chain_level_bridge.tex`, which explicitly excludes Kac $Y_{\mathrm{osp}}(4|20)$.
General compact non-toric $G(X)$ requires its missing construction. Named targets and model examples do not supply that construction.

## Source-qualified mathematical facts

- The K3-side BKM object is the Hall–Drinfeld double $\mathcal{D}_\hbar(\mathrm{CoHA}_{K3 \times E})$. "K3 Yangian" is shorthand for the separate Mukai self-mirror branch $Y_\hbar(\mathfrak{so}(4 \mid 20))$ when the Hodge $\mathbb{Z}/2$-super-extension is imposed; the ungraded Mukai-form classical limit is $\mathfrak{so}(4, 20)$, never $\mathfrak{osp}(4 \mid 20)$ (cache row 9: Mukai pairing is symmetric on both parts).
- $\mathrm{CoHA}(\mathbb{C}^3) = Y^+(\widehat{\mathfrak{gl}}_1)$ (positive half, $E_1$-associative). $\mathcal{W}_{1+\infty}$ is the Drinfeld-double + Fock-evaluation image — not the CoHA itself. CoHA evaluation chain: CoHA = $Y^+$ $\hookrightarrow$ $Y$ (Drinfeld double, Hopf) $\xrightarrow{\mathrm{ev}_\lambda}$ $\mathrm{End}(\mathcal{W}_{1+\infty}[\lambda]\text{-vac})$. Three arrows, three associativity classes.
- Six routes to $G(K3 \times E)$ are six distinct $(\Sigma_2, C)$-specialisations of one Stage-1 datum $\Phi^{\mathrm{FA}}_3(D^b\mathrm{Coh}(K3 \times E))$ — not six $\Phi$-applications.
- $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$ fails at every $N \in \{1, 2, 3, 4, 6\}$ (cache row 64). Universal identity: $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$. The Vol I `lattice_foundations.tex:5866` "$N=1$ accident, K3 Mukai datum" remark is consistent with this when read with the $\kappa_{\mathrm{ch}}^{\mathrm{Mukai}}$ subscript explicit; the bare $\kappa_{\mathrm{ch}}$ is HZ-7 violation, not contradiction.
- $\kappa_{\mathrm{BKM}}(\mathbf H_{\Delta_5})$ takes value $5$ at the paramodular $\Delta_5$ input and $12$ at the Fake-Monster $\Phi_{12}$ input — same universal identity, two conventions, name the input denominator (cache row 65, AP-CY49).
- Class $\mathcal{M}$ $E_3$ bar $= 6^g$ at cohomological level for $g \le 3$; $g \ge 4$ open pending $d_5$ computation. Chain-level infinite in ordinary complexes; finite in weight-completed.
- At $d \geq 3$, $A$ is $E_1$; the $E_2$-braiding lives on $Z(\mathrm{Rep}^{E_1}(A))$, not on $A$.
- 5d hCS on $\mathbb{R} \times \mathbb{C}^2$ quantises to the Yangian VOA $Y^{\mathrm{VOA}}(\mathfrak{g})$ to all orders for simply-laced $\mathfrak{g}$ (Costello–Gaiotto–Yagi). Convergence (not asymptotic) by Kontsevich–Tamarkin formality on the holomorphic factor. Non-simply-laced: twisted Yangian; open at all orders.
- 6d hCS on $\mathbb{C}^3$ realises $\Phi^{\mathrm{FA}}_3$ at toric loci. One-loop obstruction: cohomological piece $\int_X \mathrm{Tr}_{\mathrm{ad}}(A(F_A)^3)$ sourced by cubic symmetric Casimir $d^{abc}$; quartic in fields, not 3d-CS-cubic. Wave-function piece scheme-dependent, absorbed into BV counter-term ($A_{w.f.} = -C_2 / (2\pi)^3 = -2 h^\vee / (2\pi)^3$). $\mathfrak{sl}_2$ unobstructed; $\mathfrak{sl}_{N \geq 3}$ obstructed with $d^{abc} = 2N$.
- Maulik–Okounkov $R$-matrix is a gluing-cocycle residue: $R^{\mathrm{MO}}(u) = \mathrm{Res}_{u = u_\star} \phi^+_{\mathrm{UV}}(u)$ where $\phi^+_{\mathrm{UV}}$ is the UV positive-half gluing cocycle across the equivariant chamber wall at $u_\star$. The MO axiom (YBE + unitarity) is the cocycle condition for $\phi^+_{\mathrm{UV}}$.
- $K3 \times E$ admits no global NCCR. Five obstructions (a) trivial $\omega$ but $\omega$-structure not reflexive-tilting; (b) derived McKay needs finite Aut fixing a point; (c) HPD self-dual fails product polarisation; (d) Mukai vanishing fails off the K3 factor; (e) no global CY$_3$ symmetric obstruction theory. Serre-equivariant quasi-NCCR substitutes.
- Dimension-stratified BKM siblings: K3-BKM $\mathfrak{g}_{\Delta_5}$ at $d = 3$ (rank 3 on $\Lambda^{2, 1}_{\mathrm{II}}$); Borcherds Monster $V^\natural$ at $d = 3$ (Cartan rank 2 on $\mathrm{II}_{1, 1}$, not 26 — cache row 24); Fake Monster at $d = 5$ on $\mathrm{II}_{25, 1}$ via $K3 \times K3 \times E + E_5 \simeq E_2 \otimes E_2 \otimes E_1$. Conway / Leech at $d = 4$ bridge.

## The platonic architecture (target for reorganisation)

Vol III's seven-part inscription refines toward six movements + one frontier (`notes/platonic_ideal_architecture_vol3.md`):

I. **The categorical input** (level 0). CY$_d$-categories with cyclic $A_\infty$-data, PTVV $(2{-}d)$-shifted symplectic, Hochschild calculus. Tier (i) $r_{\mathrm{CY}}$-intrinsics live here.

II. **The two-stage construction** (levels 0→2). Stage-1 + Stage-2 + four physical lanes (5d hCS, 6d hCS, mixed-HT-strings local model, mathematical perturbative). $E_n$-tower via shift law as derived consequence (absorbing current Part III). CY-A theorems. Tier (ii) Stage-1 invariants ($\kappa_{\mathrm{fiber}}$).

III. **The bulk** (level 3). $Z^{\mathrm{der}}_{\mathrm{ch}}(A_X)$, $Y^+(X)$, $G(X) = D(Y^+(X))$ as three constructions of one level-3 object. CoHA evaluation chain. Compact-CoHA construction gates. K3 Yangian as principal $d = 2$ instance (absorbing current Part IV). Chain fusion conjecture.

IV. **The seven-faced R-matrix $r_{\mathrm{CY}}$** (level-2 cross-axis). Three tiers (`working_notes.tex:742-752`) × seven algebraic presentations (bar–cobar / CoHA / coisson / MO stable envelope / Yangian / Sklyanin / Gaudin). MO as gluing-cocycle residue. The bar-of-$\Phi$ shadow — the level-2 crystallisation that organises the entire output side.

V. **The CY landscape** (level-2 instances by chart class). Toric ($\mathbb{C}^3$, local $\mathbb{P}^2$, conifold), reduced + Aut ($K3 \times E$ central), orbifold inertia, lattice-polarised. Cross-stratum sibling census ($d = 1, 2, 3, 4, 5$). The K3 × E five $\kappa$-values $\{0, 0, 3, 5, 24\}$ vs the $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$ five-archetype landmark $\{0, 8, 13, 250/3, 25/3\}$ — two distinct fives, common cell $\mathsf{B}$-row.

VI. **The terminal scalar shadow** (level 4). Universal Borcherds-weight identity. CHL ladder $N \in \{1, 2, 3, 4, 6\}$. Gritsenko–Cléry 8-form catalogue. Cross-volume terminal-shadow disclaimer (`~/igusa-cusp-form/main.tex:96` cited): scalar is not Hilbert space, not Hall pairing, not orientation, not BPS operator product.

VII. **Frontiers + scope discipline.** Three-axis discipline as operating gate. Open frontiers: chain fusion proof in general $d$, $G(X)$ for compact non-toric, $W_\infty[\lambda] \Rightarrow E_\infty$ beyond admissible window, modularity under fusion, $d \geq 4$ stratum, higher-$n$ bar-twisting.

Reorganisation is iterative refinement: current Part III ($E_n$ hierarchy) absorbs into Part II; current Part IV (K3 Yangian) absorbs into platonic Part III; new platonic Part VI (scalar terminus) hosts the level-4 universal identity; current Part VI (seven faces) promotes earlier as platonic Part IV. Content survives entirely; the form makes the inner symmetry visible.

## Five theorems (shared with Vol I)

A bar–cobar; B chiral Positselski; C derived-centre complementarity ($\kappa + \kappa^! \in \{0, 8, 13, 250/3, 25/3\}$ on the canonical $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$ landmark, with $\mathsf{B}$-row $K^\kappa = 8$ the Vol III Mukai-enhanced K3 Heisenberg witness via Bruinier Heegner Chern-class reciprocity); D obstruction-tower universality; H Hochschild concentration.

Vol III-specific contributions: the CY-A$_3$ object-level + $E_1$-rigidity theorem (`working_notes.tex:762-768`), the K3 abelian-Yangian presentation, the ZTE $T$-matrix exact rational, the CY-D dimensional stratification ($\kappa_{\mathrm{ch}}^{\mathrm{Hodge}} = \chi(\mathcal{O})$ Hodge supertrace on compact CY$_d$), the universal Borcherds-weight identity across $N \in \{1, 2, 3, 4, 6\}$.

## Five objects, never conflated

$A$, $B(A)$, $A^i$, $A^!$, $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$. $\Omega(B(A)) = A$ is bar–cobar inversion (Quillen, Lefèvre-Hasegawa, Loday–Vallette). $A^!$ via Verdier when applicable. $A^i$ via Connes' $B$-operator periodicity. The bulk is $Z^{\mathrm{der}}_{\mathrm{ch}}$ via chiral Hochschild. The bar represents twisting/coupling; the bar is not a centre.

## Chain-level and $(\infty, 1)$-categorical: equal status

Both lanes load-bearing in Vol III; neither replaces or subsumes the other. Chain-level: explicit denominators, $L_\infty$-twistings, witnessed homotopies, ambient-qualified Mittag–Leffler towers, explicit Borcherds product expansions, explicit Hodge-supertrace summands, explicit Mukai-vanishing inputs. $(\infty, 1)$-categorical: CY $\infty$-categories of Kontsevich–Soibelman, derived $\infty$-stable categories of coherent sheaves, CoHA as stable $\infty$-category construction, Maulik–Okounkov stable envelopes in derived geometry.

State each theorem in the lane in which its proof actually works. Ambient-qualify when both lanes are used (Pattern 236). Pattern 273 ($\Phi$-functor vs object-level correspondence) is a scope declaration, not a hierarchy: chain-level and $(\infty, 1)$-categorical are two different statements about two different categorical structures, both load-bearing. Never write *this is the chain-level shadow of the real theorem*: both shadows are the theorem, viewed through different lenses.

## Essential constants (Vol III-specific)

- $\kappa_{\mathrm{ch}}^{\mathrm{Hodge}}(A_X) = \sum_q (-1)^q h^{0, q}(X)$ on compact CY$_d$.
- $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ across $N \in \{1, 2, 3, 4, 6\}$. $N = 1$: Gritsenko $\Delta_5$ weight $5$, $c_1(0) = 10$, $\kappa_{\mathrm{BKM}} = 5$. Fake Monster $\Phi_{12}$: weight $12$, $c_\Lambda(0) = 24$, $\kappa_{\mathrm{BKM}} = 12$. Always name the input denominator (cache row 65, AP-CY49).
- $K3 \times E$ spectrum: $\{0, 0, 3, 5, 24\}$ from five distinct constructions: $\kappa_{\mathrm{cat}} = 0$ (Künneth multiplicative), $\kappa_{\mathrm{ch}}^{\mathrm{Hodge}} = 0$, $\kappa_{\mathrm{ch}}^{\mathrm{Heis}} = 3$, $\kappa_{\mathrm{BKM}}(\Delta_5) = 5$, $\kappa_{\mathrm{fiber}} = 24$. Distinct from the $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$ five-archetype landmark $\{0, 8, 13, 250/3, 25/3\}$.
- Theorem-C $\mathsf{B}$-row Mukai-doubling face: $K^{\kappa_{\mathrm{ch}}} = 8 = \mathrm{ord}(H_1)$; $\hbar^2 K^{\kappa_{\mathrm{ch}}} = -1$.
- Local $\mathbb{P}^2$: $\kappa_{\mathrm{ch}}^{\mathrm{loc}} = 3/2$ via direct McKay shadow at $d = 3$.
- Conifold: not a local surface; $\kappa_{\mathrm{ch}} = 1$ via direct McKay.
- 8-form Gritsenko–Clery catalogue: weights $(5, 2, 3, 1, 2, 1/2, 3/2, 1)$ indexed by triples $(t, N; k)$, with Fourier coefficients $c_N(0) \in \{10, 4, 6, 2, 4, 1, 3, 2\}$ giving $\kappa_{\mathrm{BKM}} = c_N(0)/2$ row-by-row. Half-integer weights via multiplier systems $(v_\eta^3 \times v_H)$, not metaplectic. No weight-$0$ row, no weight-$1/4$ row.

## Where the bookkeeping lives

- `notes/chatgpt_chiral_duality_critique_consequence_map.md` + `notes/chatgpt_critique_consequence_map_adversarial_review.md` — May 2026 ChatGPT Beilinson critique reconstitution. The deep adversarial review supersedes Phase 1-2 of the original; installs three-axis scope discipline + chain fusion conjecture as inner form.
- `notes/platonic_ideal_architecture_vol3.md` — six-movement platonic architecture target.
- `notes/antipatterns_catalogue.md` — Vol III AP-CY catalogue (AP-CY1–454; type-organised).
- `appendices/first_principles_cache.md` — confusion-pattern cache with Wave-N append blocks; canonical-values registry; compatible-dual-readings table (line 103+) for non-contradictions.
- `chapters/examples/cy_d_kappa_stratification.tex` — canonical Vol III $\kappa$ table; Theorem `thm:borcherds-weight-kappa-BKM-universal`.
- `chapters/theory/cy_to_chiral.tex:2840-2856` — correspondence-programme remark.
- `working_notes.tex` — sec:two-stage-factorisation, sec:three-tiers-rcy, sec:cy-a3-existence-rigidity, central-identification table.
- `~/chiral-bar-cobar/CLAUDE.md` (Vol I), `~/chiral-bar-cobar-vol2/CLAUDE.md` (Vol II), `~/chiral-bar-cobar-vol4/CLAUDE.md` (Vol IV — verification capstone) — main-volume manifestos (shared five-theorem core; Vol IV exhibits independent verification paths for ProvedHere inscriptions across Vols I–III).
- `~/chiral-bar-cobar/chapters/examples/landscape_census.tex` — canonical $\kappa$ / $r(z)$ per family.
- `~/chiral-bar-cobar/chapters/theory/configuration_spaces.tex:2062-2544` — tangential log curve $(X, D, \tau)$ definition (referenced from chain fusion).
- `~/igusa-cusp-form/main.tex:96` — terminal-shadow disclaimer.
- `~/mixed-holomorphic-topological-strings/main.tex:3207-3266` — holomorphic de Rham obstruction discipline.
- `scripts/hooks/beilinson-gate.sh` — version-controlled PostToolUse AP + cache sweep; install via `cp scripts/hooks/beilinson-gate.sh .claude/hooks/`.

## Reference corpus

Read to re-calibrate; cite by author + year + theorem / equation number when load-bearing.

- Beilinson–Drinfeld, *Chiral Algebras* (2004).
- Maulik–Okounkov, *Quantum groups and quantum cohomology* (2012).
- Nekrasov, *Seiberg–Witten Prepotential from Instanton Counting* (2003).
- Costello, *Renormalization and Effective Field Theory* (2011); Costello–Gwilliam, *Factorization Algebras in Quantum Field Theory*.
- Gaiotto–Witten on class $\mathcal{S}$, VOAs, generalized symmetries.
- Feigin–Odesskii on elliptic algebras.
- Etingof–Gelaki–Nikshych–Ostrik, *Tensor Categories* (2015).
- Gritsenko–Nikulin on lattice Borcherds products; Gritsenko–Cléry on the 8-row catalogue (arXiv:0812.3962).
- Borcherds 1995 *Invent. Math.* 120 (singular-theta lift, denominator formulas); Borcherds 1992 *Invent. Math.* 109 (Monster Lie algebra).
- Schiffmann–Vasserot on cohomological Hall algebras.
- Gaberdiel–Gopakumar on higher-spin holography and $\mathcal{W}_\infty[\lambda]$.
- Bershadsky–Cecotti–Ooguri–Vafa (BCOV, 1993–94) for the holomorphic anomaly equation.
- Costello–Gaiotto–Yagi on 5d hCS quantising to Yangian VOA.
- Costello–Li (BCOV-quantization) for 6d holomorphic Chern–Simons on $\mathbb{C}^3$.
- Pope–Romans–Shen 1990 (PRS) on $\mathcal{W}_\infty$ family; Bakas; Yamada weight-window; Prochazka triangular-truncation; Creutzig–Kanade–Linshaw parafermion compatibility (the four endpoint admissibility conditions).

## Cross-repo awareness — research constellation

Vol III of the chiral bar–cobar programme. The corpus has four main volumes plus two satellites; the chain fusion conjecture connects them (`notes/chatgpt_critique_consequence_map_adversarial_review.md` §III):

- `~/chiral-bar-cobar` (Vol I) — bar / twisting face. $E_1$–$E_1$ operadic Koszul duality; Theorems A, B, C, D, H; averaging map $\mathrm{av}: \mathfrak{g}^{E_1} \to \mathfrak{g}^{\mathrm{mod}}$; modular open-closed convolution; tangential log curves $(X, D, \tau)$ at `chapters/theory/configuration_spaces.tex:2062-2544`. Open-side primitive of the chain fusion.
- `~/chiral-bar-cobar-vol2` (Vol II) — centre / universal-holography face. $A_\infty$ chiral algebras + 3D HT QFT via $\mathsf{SC}^{\mathrm{ch}, \mathrm{top}}$; topologisation ladder; weight-completed class $\mathcal{M}$. Master theorem identifies the algebraic holographic HT sector (boundary $A$, bulk $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$, interaction $\mathsf{SC}^{\mathrm{ch}, \mathrm{top}}$-brace), not the dynamical-metric path integral.
- `~/chiral-bar-cobar-vol4` (Vol IV) — verification capstone. Independent verification paths for theorems inscribed in Vols I–III; pairs every `\ClaimStatusProvedHere` with an external witness (mechanization / cross-volume re-derivation / numerical decisive check / primary-literature anchor). When a Vol III theorem is referenced as load-bearing across volumes, the Vol IV witness is the audit target.
- `~/igusa-cusp-form` — terminal scalar face. Borcherds lift of $\phi_{0,1}$, generalized BKM superalgebras, Igusa $\Phi_{10}$, Gritsenko $\Delta_5$. Disclaimer at `main.tex:96`: does not supply compact BPS Hilbert space, compact Hall correspondences, orientation, BPS operator product. Source / target firewall (`~/igusa-cusp-form/notes/swarm_20260430/reports/A270_cross_repo_source_target_firewall.md`).
- `~/mixed-holomorphic-topological-strings` — physical realisation face of Stage-1. Local model $\mathbb{R}^2_{\mathrm{top}} \times \mathbb{C}^2_{\mathrm{hol}}$ with Hamiltonian BF sector; holomorphic de Rham obstruction (`main.tex:3207-3266`). Inside Vol III's level 1, alongside Costello–Gwilliam–Li perturbative, Kontsevich–Tamarkin formality, 5d/6d hCS lanes — the four-lane Beilinson "two lanes equally load-bearing" structure.

Any claim about $\kappa_{\mathrm{BKM}}$, $\Phi(K3 \times E)$, K3 abelian Yangian, MO $E_2$-structure, or six-routes chiral audit must be consistent across the corpus. Investigate disagreements in the assigned scope. Record the exact unresolved claim and source evidence when comparison cannot settle it.
