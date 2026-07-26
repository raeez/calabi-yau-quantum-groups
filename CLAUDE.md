# CLAUDE.md (Vol III)

> Inherits `~/ecosystem/INVARIANTS.md` — destructive-git list, multi-agent worktree concurrency, standalone-document discipline, Russian-school voice, every-file-into-the-repo, no-LLM-attribution-on-commits, deep-semantic-merges, intelligence propagation, mathematical-repair doctrine, shared LaTeX template. Read it once per session; do not re-read; do not paraphrase. Repo-local rules follow.
>
> Writing standards binding: `MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md` (root). Every reader-facing line in `chapters/`, `frame/`, `examples/`, `theory/`, `connections/`, `bibliography/`, `appendices/` answers to it.

---

## What this repository is

An instrument for advancing human mathematical knowledge: the Calabi–Yau-to-chiral functor

$$\Phi^{(\Sigma_{d-1}, C)}_d \;=\; \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \,\circ\, \Phi^{\mathrm{FA}}_d,$$

and the seven faces of $r_{\mathrm{CY}}$ that crystallise the BPS-quantum-group / chiral-algebra correspondence — K3 BKM $\mathfrak{g}_{\Delta_5}$ from Gritsenko's $\Delta_5$, the K3 Yangian on the Mukai self-mirror branch, the Borcherds Monster, the Fake Monster at $d = 5$.

Every read, grep, edit, inscription, refactor, retraction serves advancing the mathematics, one true theorem at a time. When a choice is between mathematics and accounting, do the mathematics. The PostToolUse hook handles accounting.

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

## Key facts (always-on cache)

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

## Beilinson's dictum

> What limits forward progress is not the lack of genius but the inability to dismiss false ideas.

3+ independent verification paths for any load-bearing numeric (cache row 75, AP-CY446: paths must be genuinely independent — a restatement, copied table, or verifier consuming path 1 is not a third path). When a heal is proposed, attack-heal: strongest counterexample, sign / convention check, ambient-category check, missing hypothesis, false functoriality, unproved equivalence, numerical constant. Heal and attack again until the theorem closes or the exact obstruction is named for the next repair cycle.

**Epistemic hierarchy** (higher wins on conflict): direct computation > `.tex` source ±100 lines > tests > primary literature > concordance > this file > memory.

**Refined Beilinson cut.** Every theorem in the programme declares its (level, chart, ambient) coordinates. Promotion across coordinates requires the named comparison arrow, constructed under the named hypotheses. No claim is permitted to be promoted from one coordinate to another by elision.

## What counts as progress

A new theorem precisely stated, rigorously proved, inscribed with proof body verifiable against primary literature (Borcherds, Gritsenko–Nikulin, Schiffmann–Vasserot, Maulik–Okounkov, Nakajima, Costello–Gaiotto, Beilinson–Drinfeld). A new CY example: compute the four $\kappa_\bullet$ for $X$ not yet in `cy_d_kappa_stratification.tex`. A falsified claim repaired by corrected statement, construction, or proof obligation; not deletion, not status-row demotion. A first-principles computation replacing a citation black box. A scope coordinate made explicit on a theorem that previously elided one — bar level / chart / ambient.

**What does NOT count as progress.** Bare $\kappa \to \kappa_{\mathrm{ch}}^{\mathrm{Hodge}}$ subscript fixes. Status rows. Phantom-label audits. Scope propagation across ten files. FRONTIER retractions. AGENTS.md / CLAUDE.md harmonisation. The PostToolUse hook catches these; you do not have to.

## Hard rules

1. No AI attribution anywhere. No `Claude`, no `Anthropic`, no `Co-Authored-By`, no `Generated with`, no 🤖, in commits, comments, docstrings, or manuscripts. Pre-commit hook nudges; remove offending content if hook fires.
2. No `git stash`. No `git commit --amend`. Deep semantic merges only (`INVARIANTS.md §I, §VII`).
3. Do not build after every edit. Builds at session end on user opt-in: `cd ~/calabi-yau-quantum-groups && make fast`.
4. Never invent a formula. Source: `chapters/examples/cy_d_kappa_stratification.tex`, `chapters/theory/cy_to_chiral.tex`, `working_notes.tex` (sec:two-stage-factorisation, sec:three-tiers-rcy, sec:cy-a3-existence-rigidity), primary paper, or direct computation.
5. HZ-7: $\kappa$ always subscripted. HZ-3-11 independent verification protocol applies to any `\ProvedHere` decorator.
6. Claim-status tags are temporary bookkeeping, not repairs. When uncertain, name the exact proof obligation and heal the proof, statement, or construction; do not downgrade the manuscript to close (`INVARIANTS.md §XI`). CY-C is conjectural; $G(X)$ is unconstructed for compact non-toric in general; Super-Yangian $Y_{\mathrm{osp}}(4 \mid 20)$ remains conjectural.
7. User-authorised large swarms permitted with disjoint scopes, named integration owner, deep semantic merge across `~/chiral-bar-cobar`, `~/chiral-bar-cobar-vol2`, `~/calabi-yau-quantum-groups`, `~/igusa-cusp-form`, `~/mixed-holomorphic-topological-strings`. Do not downshift swarm size in response to old 3-agent / 5-agent cautionary language.
8. Standalone documents only (`INVARIANTS.md §III`). No version labels, phase labels, prior-draft references, "Wave $N$ / round / strand / cache-entry" vocabulary in `chapters/`, `frame/`, `examples/`, `theory/`, `connections/`, `bibliography/`, `appendices/`. Bookkeeping vocabulary lives in `notes/`, commits, and memory only.
9. When a mathematical retraction is genuinely informative — a proof attempted and failed, whose failure forces the successful proof — state the failed argument and its flaw as mathematics, not as a drafting record. *The identity $[m_k, B^{(2)}] = 0$ fails per-$k$ because cyclic invariance controls adjacent contractions but not non-adjacent terms (Proposition X)*; not *initially the author attempted X but retracted in favour of Y*. The mathematics is the gap; the drafting trajectory is not.

## Writing standard: Chriss–Ginzburg north star

Manuscript prose IS mathematics, not a description of mathematics. Seven combined voices: Witten, Etingof, Polyakov, Dirac, Feynman, Costello, Gaiotto. Russian elite school. Every statement inevitable.

`MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md` is binding. Forbidden patterns to scan-and-cut after every draft: meta-narration (*we now turn to*, *having established*, *in what follows*); bookkeeping (*Theorem A* labels embedded in body; status tables in theorem bodies); catalogue IDs (*Wave $N$*, *AP-CY$n$*, *HZ-$n$*, *DNA strand*, *MP$n$*); branding (*magic identity*, *inner music*, *X spine*, *matrix microscope*, *platonic ideal* in prose); hedging (*perhaps*, *notably*, *crucially*, *remarkably*, *clearly* used to skip a proof step); negative framing (*must not*, *would conflate*, *is wrong*, *fails to*); approximation language for exact identifications (*is closely related to*, *corresponds to*, *is the analogue of* — use $=$ or $\simeq$ when the identification is proved); CS jargon (*certificate*, *pipeline*, *API*, *spec*); passive avoidance (*it can be shown*, *it is decided*); evocative metaphor.

Define before use. Motivate before introduce. Concrete example before abstract machine. The reader is serious and adult.

The mathematics earns the equals sign. Two objects that are the same: $X = Y$ with the morphism implementing the identification stated. Not *$X$ is closely related to $Y$*. Courage, after Drinfeld and Polyakov and Nekrasov.

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

## Long-form proof harness

Frontier mathematics runs at maximum effort. For Claude Code: deepest host-exposed model + maximum reasoning. For Codex / GPT-5-Codex-class agents: see `AGENTS.md` and `~/ecosystem/AGENTS-HARNESS.md` for harness calibration; never lower than `reasoning_effort=high`, `xhigh` for theorem repair / cross-volume synthesis / adversarial review / primary-source reconstruction.

A 30–60 minute agent run is normal when a proof obligation requires it. Load the relevant context first (this file, `AGENTS.md`, target chapter, dependencies, bibliography, compute files, cross-volume anchors), build an internal outline, then work through independent proof routes: worked example, formal argument, primary source, computation, cross-volume consistency. Private scratch stays private; the deliverable is the checked proof trace and the exact remaining obstruction.

After every proposed repair, attack-heal: counterexample / sign-convention / ambient-category / missing hypothesis / false functoriality / unproved equivalence / numerical constant. Heal and attack again until the theorem closes or the obstruction is named precisely for the next cycle. Do not downgrade the manuscript to close the loop. Subagents provide evidence, not authority; the main thread integrates by deep semantic merge.

## Branch and worktree reconciliation: deep semantic merges only

When branches or worktrees differ, perform a deep semantic merge — no exceptions. Never `git reset --hard`, `git checkout --`, `git restore`, or force-push to clobber work. Read both sides in full; merge at the semantic level (theorem statement, proof structure, prose), not the diff-hunk level. When line-level conflict is semantic — a theorem reworded — pick the stronger statement, the tighter citation, the more rigorous proof. When unclear which side is stronger, read both in context. Do not guess.

Work loss in this programme is irrecoverable. Chapters represent weeks of adversarial-swarm output, elite-voice synthesis, primary-literature audit. Deep semantic merges take longer; they are the only operation consistent with Beilinson's dictum and "never cut content".

## Hooks (ambient)

- `PreToolUse(Agent)` → cache-injection (if locally installed).
- `PreToolUse(Bash, git commit)` → no-AI-attribution reminder.
- `PostToolUse(Edit | Write)` → `beilinson-gate.sh` AP-CY + cache sweep.
- `Stop` → session-end summary (if locally installed).

## Do not

1. Block large user-authorised swarms. Partition by disjoint files or mathematical axes; require short verifiable reports; merge by deep semantic review across Vol I/II/III.
2. Propagate status-label wording when mathematics is waiting.
3. Invent formulas from memory.
4. Run `make fast` after every edit.
5. Add AI attribution anywhere.
6. `git stash` or amend commits.
7. Confuse this file with a configuration manual. Mathematician's manifesto.

## Code-writing discipline — repo application

Per `~/ecosystem/INVARIANTS.md §XIII`. Twelve rules instantiated for calabi-yau-quantum-groups Vol III (Calabi-Yau-to-chiral frontier; Yangians; BKM superalgebras; $\kappa$-stratification; AP-CY catalogue):

1. **Think Before Coding.** Every Yangian / BKM / quantum-group edit names the chiral target structure, the affected hypothesis package, and the claim-status. Every $\kappa$-stratification edit names the affected stratum and consults the canonical $\kappa$-table (`chapters/examples/cy_d_kappa_stratification.tex`).
2. **Simplicity First.** Three-axis scope discipline: Open-vs-CY, Categorical-vs-Chain, BKM-Yangian. No speculative axes; no abstractions ahead of the three. Append to existing AP-CY types — do not introduce parallel numbering.
3. **Surgical Changes.** An edit on the Yangian axis does not touch the BKM-superalgebra axis. A $\kappa$-stratification chapter edit does not opportunistically refactor the CY-to-chiral functor.
4. **Goal-Driven Execution.** Success = `pdflatex main.tex` clean, theorem ledger consistent, voice-scan + term-coining test pass, claim-status macros honest, raeez-math-template intact. Build session-end only with `make fast`.
5. **Use the model only for judgment calls.** Cross-references, theorem-numbering, bibliography are deterministic. The model drafts proofs and worked examples; it does not invent new strata or canonical-values registry rows.
6. **Token budgets are not advisory.** Monograph; checkpoint between axes and between chapters. Long-form proof harness: load context first, build internal outline.
7. **Surface conflicts, don't average them.** Cross-volume vertical equivalences with Vol I are canonical at the Vol I side; if Vol III disagrees, repair Vol III. The 8-row Gritsenko–Cléry / 10-row catalogue inconsistency triggers stop-and-report. Check `appendices/first_principles_cache.md:103+` compatible-dual-readings table before editing either side of an apparent contradiction.
8. **Read before you write.** Read the affected axis chapter and its hypothesis package. Read the canonical $\kappa$-table; never overwrite a canonical value from memory. Cross-reference with `~/chiral-bar-cobar/chapters/examples/landscape_census.tex`.
9. **Tests verify intent.** Claim-status macros, four-part term-coining test, voice-scan, AP-CY catalogue compliance. A theorem whose (level, chart, ambient) scope cannot be declared is broken — determine scope before inscribing.
10. **Checkpoint after every significant step.** Between axes, summarize hypothesis-package delta and cross-volume impact (Vols I/II/IV). Subagents return evidence; main thread integrates via deep semantic merge.
11. **Match the codebase's conventions, even if you disagree.** raeez-math-template per `INVARIANTS.md §XII`. AP-CY catalogue numbering (do not parallel-number). Canonical-values registry pattern.
12. **Fail loud.** Surface every cross-ref break, dangling theorem, unhealed conjecture (`INVARIANTS.md §XI`). 8-row/10-row catalogue inconsistency stops and reports — do not silently reassign a row. Compute-vs-prose disagreements stop and report; computation usually wins.
