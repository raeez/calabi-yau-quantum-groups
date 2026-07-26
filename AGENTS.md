# AGENTS.md (Vol III)

> Inherits `~/ecosystem/INVARIANTS.md` — destructive-git list, multi-agent worktree concurrency, standalone-document discipline, Russian-school voice, every-file-into-the-repo, no-LLM-attribution-on-commits, deep-semantic-merges, intelligence propagation, mathematical-repair doctrine. Read once per session; do not paraphrase; do not weaken.
>
> Inherits `~/ecosystem/AGENTS-HARNESS.md` — Codex / GPT-5-family harness calibration: reasoning-effort per task class, agentic eagerness, tool-use discipline, tool preambles, persistence and stop conditions, verbosity, uncertainty handling, long-context outlining, self-reflection rubric (§VIII), scope discipline, error-handling, git-and-worktree restatement, frontend quality, no-LLM-commit-attribution, voice.
>
> Mirrors this repo's `CLAUDE.md` on substance. Before editing code in this repo, `read_file ./CLAUDE.md` — it carries the repo-local layout, commands, doctrine, and conventions. `AGENTS.md` and `CLAUDE.md` must not diverge in facts; they may differ in structure and voice.
>
> Writing standards binding: `MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md` (root). Every reader-facing line in `chapters/`, `frame/`, `examples/`, `theory/`, `connections/`, `bibliography/`, `appendices/` answers to it.
>
> Load order: `INVARIANTS.md` → `AGENTS-HARNESS.md` → this repo's `CLAUDE.md` → this file. The closest `AGENTS.md` in the directory tree wins per `agents.md`; explicit principal chat instructions outrank everything.
>
> Model target: deepest host-exposed GPT-5.5 / GPT-5-Codex-family model. `reasoning_effort = xhigh` for any non-trivial mathematical work, never lower than `high`. Terse declarative voice per `INVARIANTS.md §IV`. No LLM attribution on commits (`INVARIANTS.md §VI`).

---

## What this repository is

An instrument for advancing human mathematical knowledge: the Calabi–Yau-to-chiral functor

$$\Phi^{(\Sigma_{d-1}, C)}_d \;=\; \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \,\circ\, \Phi^{\mathrm{FA}}_d,$$

and the seven faces of $r_{\mathrm{CY}}$ that crystallise the BPS-quantum-group / chiral-algebra correspondence — K3 BKM $\mathfrak{g}_{\Delta_5}$ from Gritsenko's $\Delta_5$, the K3 Yangian on the Mukai self-mirror branch, the Borcherds Monster, the Fake Monster at $d = 5$.

If you are an agent here, your purpose is identical to that mission. Every read, grep, edit, inscription, refactor, retraction serves advancing the mathematics, one true theorem at a time. When a choice is between mathematics and accounting, do the mathematics. The PostToolUse hook handles accounting.

## The mathematics

**One functor, two stages.** $\Phi^{\mathrm{FA}}_d : \mathrm{CY}_d\text{-cat} \to E_d\text{-HolFA}(X)$ is a canonical functor at fixed $d$, unique up to a $\mathrm{GRT}_1(\mathbb{Q})$-torsor (Kontsevich–Tamarkin $E_d$-formality + Costello–Gwilliam–Li holomorphic locality). $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}$ is chart-specialisation: factorisation homology over a $(d{-}1)$-cycle restricted to a reference curve. The collection $\{\Phi_d\}$ is a per-$d$ correspondence programme; the target $E_{n(d)}\text{-ChirAlg}$ depends on $d$ ($n = \infty, 2, 1, 1, 1$ at $d = 1, 2, 3, 4, 5$ via the shift law $(d, \text{shift}, E_n^{\mathrm{cl}})$). $\{\Phi_d\}$ does not assemble into a single functor across $d$. The framing "correspondence programme, not unified functor" lives at `chapters/theory/cy_to_chiral.tex:2840-2856`.

**Four $\kappa$-invariants, never conflated.**

- $\kappa_{\mathrm{ch}}$ — chiral-side, via $\Phi$. Subscripted further: $\kappa_{\mathrm{ch}}^{\mathrm{Hodge}} = \sum_q (-1)^q h^{0, q}(X)$ on compact CY$_d$; $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}$ for Heisenberg–Mukai specialisation; $\kappa_{\mathrm{ch}}^{\mathrm{Mukai}}$ for the Mukai-doubling face on K3; $\kappa_{\mathrm{ch}}^{\mathrm{cpt}}, \kappa_{\mathrm{ch}}^{\mathrm{loc}}$ for compact vs local CY$_3$ (cache row 1); $\kappa_{\mathrm{ch}, \mathrm{BV}}$ for one-loop BV-corrected.
- $\kappa_{\mathrm{cat}} = \chi(\mathcal{O}_X)$ — Künneth-multiplicative on products. $\kappa_{\mathrm{cat}}(K3 \times E) = 0$ (total space); not 2 (fibre).
- $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ — Borcherds 1995 *Invent. Math.* 120 / Gritsenko 1999 universal weight identity; $N$ names the Siegel input denominator.
- $\kappa_{\mathrm{fiber}}$ — fibre / lattice rank correction.

Bare $\kappa$ forbidden (HZ-7 / AP-CY113). Subscript at every use, including conversation turns about manuscript content.

**Chain fusion conjecture.** $A_X = \Phi^{(\Sigma_{d-1}, C)}_d(\mathcal{C}_X)$ on the curve $C$ equals the boundary algebra $A_{b(X, \Sigma, C)}$ in an open factorisation dg-category on $(C, D_C, \tau_C)$, where $D_C$ encodes the CY data's special points (orbifold loci, fibration punctures, conifold singularities). Verified at $\mathbb{C}^3$, local $\mathbb{P}^2$, conifold, $K3 \times E$. Bridges Vol III's Stage-2 to Vol I/II's open-side primitives.

## Key facts (always-on cache, primary-source-anchored)

- The K3-side BKM object is the Hall–Drinfeld double $\mathcal{D}_\hbar(\mathrm{CoHA}_{K3 \times E})$. *K3 Yangian* is shorthand for the separate Mukai self-mirror branch $Y_\hbar(\mathfrak{so}(4 \mid 20))$ when the Hodge $\mathbb{Z}/2$-super-extension is imposed; ungraded Mukai-form classical limit is $\mathfrak{so}(4, 20)$, never $\mathfrak{osp}(4 \mid 20)$ (cache row 9: Mukai is symmetric on both parts; $\mathfrak{osp}$ requires symplectic on odd part).
- $\mathrm{CoHA}(\mathbb{C}^3) = Y^+(\widehat{\mathfrak{gl}}_1)$ ($E_1$-associative positive half). $\mathcal{W}_{1+\infty}$ is the Drinfeld-double + Fock-evaluation image, not the CoHA itself. Evaluation chain: $\mathrm{CoHA} = Y^+ \hookrightarrow Y$ (Drinfeld double, Hopf) $\xrightarrow{\mathrm{ev}_\lambda} \mathrm{End}(\mathcal{W}_{1+\infty}[\lambda]\text{-vac})$. Three arrows, three associativity classes.
- Six routes to $G(K3 \times E)$ are six distinct $(\Sigma_2, C)$-specialisations of one Stage-1 datum, not six $\Phi$-applications.
- $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$ fails at every $N \in \{1, 2, 3, 4, 6\}$ (cache row 64). Universal: $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$. Vol I `lattice_foundations.tex:5866` "$N = 1$ K3 Mukai accident" remark is consistent under $\kappa_{\mathrm{ch}}^{\mathrm{Mukai}}$ subscript; bare $\kappa_{\mathrm{ch}}$ is HZ-7 violation, not contradiction.
- $\kappa_{\mathrm{BKM}}(\mathbf{H}_{\Delta_5}) = 5$ at paramodular $\Delta_5$; $= 12$ at Fake-Monster $\Phi_{12}$. Same universal identity, two conventions; name the input denominator (cache row 65, AP-CY49).
- Class $\mathcal{M}$ $E_3$ bar $= 6^g$ at cohomological level for $g \le 3$; $g \ge 4$ open pending $d_5$ computation. Chain-level infinite in ordinary complexes; finite in weight-completed (Vol II `weight_completed_topologization_class_m_platonic.tex`).
- At $d \ge 3$, $A$ is $E_1$; $E_2$-braiding lives on $Z(\mathrm{Rep}^{E_1}(A))$, not on $A$.
- 5d hCS on $\mathbb{R} \times \mathbb{C}^2$ quantises to $Y^{\mathrm{VOA}}(\mathfrak{g})$ all-orders for simply-laced $\mathfrak{g}$ (Costello–Gaiotto–Yagi); convergent (not asymptotic) by Kontsevich–Tamarkin formality. Non-simply-laced: open at all orders.
- 6d hCS on $\mathbb{C}^3$ realises $\Phi^{\mathrm{FA}}_3$ at toric loci. One-loop obstruction: cohomological piece $\int_X \mathrm{Tr}_{\mathrm{ad}}(A(F_A)^3)$ sourced by cubic symmetric Casimir $d^{abc}$; quartic in fields, not 3d-CS-cubic. Wave-function piece $A_{w.f.} = -2 h^\vee / (2\pi)^3$ scheme-dependent, absorbed into BV counter-term. $\mathfrak{sl}_2$ unobstructed; $\mathfrak{sl}_{N \ge 3}$ obstructed with $d^{abc} = 2N$.
- Maulik–Okounkov $R$-matrix is a gluing-cocycle residue: $R^{\mathrm{MO}}(u) = \mathrm{Res}_{u = u_\star} \phi^+_{\mathrm{UV}}(u)$. The MO axiom (YBE + unitarity) is the cocycle condition.
- $K3 \times E$ admits no global NCCR; five obstructions (trivial $\omega$ but $\omega$-structure not reflexive-tilting; derived McKay needs finite Aut fixing a point; HPD self-dual fails product polarisation; Mukai vanishing fails off K3 factor; no global CY$_3$ symmetric obstruction theory). Serre-equivariant quasi-NCCR substitutes.
- Dimension-stratified BKM siblings: K3-BKM $\mathfrak{g}_{\Delta_5}$ at $d = 3$ (rank 3 on $\Lambda^{2, 1}_{\mathrm{II}}$); Borcherds Monster at $d = 3$ (Cartan rank 2 on $\mathrm{II}_{1, 1}$, not 26 — cache row 24); Fake Monster at $d = 5$ on $\mathrm{II}_{25, 1}$ via $K3 \times K3 \times E + E_5 \simeq E_2 \otimes E_2 \otimes E_1$. Conway / Leech bridge $d = 4$.

**Five objects, never conflated.** $A$, $B(A)$, $A^i$, $A^!$, $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$. $\Omega(B(A)) = A$ is bar–cobar inversion (Quillen, Lefèvre-Hasegawa). The bulk is $Z^{\mathrm{der}}_{\mathrm{ch}} = \mathrm{R}\mathrm{Hom}(\Omega B(A), A)$ via chiral Hochschild. The bar represents twisting/coupling; bar is not centre.

**Seven parts** (current): I Foundations · II $\Phi$ functor · III $E_n$ hierarchy · IV K3 Yangian · V CY landscape · VI Seven faces of $r_{\mathrm{CY}}$ · VII Frontiers.

**Five theorems** (shared with Vol I): A bar–cobar; B chiral Positselski; C derived-centre complementarity ($\kappa + \kappa^! \in \{0, 8, 13, 250/3, 25/3\}$ on $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$ five-archetype landmark — distinct from the K3 × E spectrum); D obstruction-tower universality; H Hochschild concentration.

## Three-axis scope discipline

Every theorem statement carries coordinates on three orthogonal axes. Promotion across coordinates requires the named comparison arrow under named hypotheses. No claim is permitted to be promoted by elision.

**Vertical (level).** $0$ primitive (CY$_d$-cat / open factorisation category) → $1$ canonical functorial passage (Stage-1 / chart-augmented $A_b$) → $2$ chart-specialised shadow (Stage-2 chiral / bar twisting $B(A)$) → $3$ centre / quantum vertex group ($Z^{\mathrm{der}}_{\mathrm{ch}}(A)$, $Y^+(X)$, $G(X) = D(Y^+(X))$) → $4$ scalar trace / Borcherds form. The bar $B(A)$ is the comparison arrow between levels 2 and 3 via $Z^{\mathrm{der}}_{\mathrm{ch}}(A) = \mathrm{R}\mathrm{Hom}(\Omega B(A), A)$. Bar is not bulk.

**Horizontal (chart datum).** Equivariance stratum × $(\Sigma_{d-1}, C)$ × boundary vacuum $b$ × admissibility window. Four equivariance strata: toric $T^d$ (local $\mathbb{P}^2$, $\mathbb{C}^3$, conifold) / reduced $\mathbb{C}^\times +$ Aut (K3, $K3 \times E$, abelian) / orbifold inertia $I(X/G)$ (Mathieu $M_{24}$, McKay $\Gamma \subset \mathrm{SU}(d)$) / lattice-polarised period domain (Borcherds lifts, Gritsenko $\Delta_5$, Igusa $\Phi_{10}$).

**Ambient (depth).** Ordinary chain complex / weight-completed / pro / $J$-adic / HS-sewing / formal-local / global-with-descent / derived $\infty$-categorical. Class $\mathcal{M}$ chain-level: weight-completed yes, ordinary no. $W_\infty[\lambda] \Rightarrow E_\infty$: Prochazka triangular-truncation + Creutzig–Kanade–Linshaw parafermion + Pope–Romans–Shen / Bakas + Yamada weight-window admissible window.

The deepest false ideas are scope-omission collapses — treating level-$k$ as level-$(k \pm 1)$, treating chart-dependent as universal, treating completed-ambient as ordinary. The three-axis discipline catches them. See `notes/chatgpt_critique_consequence_map_adversarial_review.md` for the seventeen archetypal collapses surfaced by the May 2026 Beilinson critique and their reconstitution.

**Refined Beilinson cut.** Every theorem in the programme declares its (level, chart, ambient) coordinates. Promotion across coordinates requires the named comparison arrow, constructed under the named hypotheses. No claim is permitted to be promoted from one coordinate to another by elision.

## The platonic architecture (target for reorganisation)

Vol III's seven-part inscription refines toward six movements + one frontier (`notes/platonic_ideal_architecture_vol3.md`):

I. **Categorical input** (level 0). CY$_d$-categories, cyclic $A_\infty$, PTVV $(2{-}d)$-shifted symplectic, Hochschild calculus. Tier (i) $r_{\mathrm{CY}}$-intrinsics live here.

II. **Two-stage construction** (levels 0→2). Stage-1 + Stage-2 + four physical lanes (5d hCS / 6d hCS / mixed-HT-strings local model / mathematical perturbative). $E_n$ tower via shift law as derived consequence (absorbing current Part III). CY-A theorems. Tier (ii) Stage-1 invariants.

III. **The bulk** (level 3). $Z^{\mathrm{der}}_{\mathrm{ch}}(A_X)$, $Y^+(X)$, $G(X) = D(Y^+(X))$ as three constructions of one level-3 object. CoHA evaluation chain. Compact-CoHA construction gates. K3 Yangian as principal $d = 2$ instance (absorbing current Part IV). Chain fusion conjecture.

IV. **Seven-faced $r_{\mathrm{CY}}$** (level-2 cross-axis). Three tiers (`working_notes.tex:742-752`) × seven algebraic presentations (bar–cobar / CoHA / coisson / MO stable envelope / Yangian / Sklyanin / Gaudin). MO as gluing-cocycle residue. Promotes earlier as Part IV.

V. **CY landscape** (level-2 instances by chart class). Toric / reduced + Aut / orbifold inertia / lattice-polarised. Cross-stratum sibling census ($d = 1, 2, 3, 4, 5$). $K3 \times E$ five $\kappa$-values $\{0, 0, 3, 5, 24\}$ vs $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$ five-archetype $\{0, 8, 13, 250/3, 25/3\}$ — two distinct fives.

VI. **Terminal scalar shadow** (level 4). Universal Borcherds identity. CHL ladder $N \in \{1, 2, 3, 4, 6\}$. Gritsenko–Cléry 8-form catalogue. Cross-volume terminal-shadow disclaimer (`~/igusa-cusp-form/main.tex:96`).

VII. **Frontiers + scope discipline.** Three-axis discipline as operating gate. Open frontiers: chain fusion proof in general $d$, $G(X)$ for compact non-toric, $W_\infty[\lambda] \Rightarrow E_\infty$ beyond admissible window, modularity under fusion, $d \geq 4$ stratum, higher-$n$ bar-twisting.

Reorganisation is iterative refinement: current Part III ($E_n$ hierarchy) absorbs into Part II; current Part IV (K3 Yangian) absorbs into platonic Part III; new platonic Part VI hosts the level-4 universal identity; current Part VI promotes earlier as platonic Part IV. Content survives entirely.

## Harness — maximum always

| Parameter | Setting | Rationale |
|---|---|---|
| `reasoning_effort` | **`xhigh`** for any non-trivial work; never lower than `high` | CY frontier / Yangian / BKM / mock-modular / MO $E_2$. No downgrade permitted. |
| `model` | **Deepest host-exposed**: GPT-5.5 Pro / Heavy in ChatGPT when available; GPT-5.5 or latest GPT-5-Codex-family in Codex; API fallback latest GPT-5.4 / GPT-5-Codex with `xhigh` where supported | Pro-class coding + mathematics harness. |
| `verbosity` | As the proof requires | No abridgment of load-bearing calculations. Terse where terse is honest. |
| Token budget | Unbounded for research tasks | If context fills, compact side work. Never elide load-bearing equations, Fourier constants, named lemmas, or proof obligations. |
| Tool use | Parallel reads | Batch `read_file` over every cited chapter, compute file, primary source before writing the first line of math. |
| Persistence | Absolute | Do not yield on a partial proof. Either close the argument or name the open obligation precisely. |
| Self-reflection rubric | Required before any inscription | See `~/ecosystem/AGENTS-HARNESS.md §VIII`; research-grade instantiation below. |

## Long-form proof harness — GPT-5.5 Pro / Heavy analogue

Public OpenAI material describes GPT-5.5 Pro as the ChatGPT research-grade option for the hardest long-running workflows and GPT-5.5 in Codex as a 400K-context agentic coding model. The private ChatGPT Pro harness is not public. This repo encodes the open analogue: deepest model, maximum reasoning effort, large context, tool-grounded verification, repeated attack-heal cycles.

1. **Deliberation budget.** For theorem repair, cross-volume synthesis, adversarial review, primary-source reconstruction, a 30–60 minute agent run is normal. Do not stop because the first plan is plausible. Stop when the proof closes, a computation decides the point, or the exact open obligation is named.
2. **Private scratch, public proof trace.** Use private reasoning for search and synthesis. Never expose raw scratchpad as an answer. The deliverable is the checked proof path: definitions, reductions, cited theorems, computations, and the remaining obstruction if any.
3. **Context before invention.** Load `CLAUDE.md`, this file, the target chapter, its local dependencies, cited bibliography entries, compute files, cross-volume anchors before the first mathematical edit. Build an internal outline; do not write from memory.
4. **Multiple routes.** For any load-bearing identity, seek independent derivations: worked example, formal argument, primary literature, local computation, cross-volume consistency. Agreement is evidence; disagreement is the deliverable. Three paths must be genuinely independent: a restatement, copied table, or verifier consuming path 1 is not a third path (cache row 75, AP-CY446).
5. **Adversarial loop.** After a proposed repair, attack the strongest failure mode: convention / sign, ambient category, missing hypothesis, false functoriality, unproved equivalence, numerical constant, scope coordinate elision. Heal, attack again, until no fatal objection survives.
6. **Agent topology.** Large swarms partitioned by disjoint proof obligations or files. Subagents provide evidence, not authority. The main thread integrates by deep semantic merge; heals the proof, statement, or construction; does not vote truth into existence; does not degrade the manuscript.
7. **Progress reports.** Long runs emit compact `commentary` checkpoints: what has been read, what has been ruled out, what proof obligation remains. The final answer is short unless the proof itself is the requested artifact.

## Research-grade discipline — `INVARIANTS.md §IV` and §XI made actionable

1. **Every load-bearing claim carries an epistemic status.** *Proved / conjectured / expected / heuristic / computed / folklore.* Conditional theorems carry the conditions inline, not in a footnote.
2. **Worked case before general statement.** CY$_3$ before CY$_d$. Abelian Yangian on K3 before elliptic on $K3 \times E$. The 8-row Gritsenko–Cléry catalogue before the universal $\kappa_{\mathrm{BKM}}$ identity.
3. **Named attribution beats passive voice.** *By Maulik–Okounkov (2012)*, *by Nekrasov–Okounkov (2003)*, *by Costello (2013)*. Year + page where the claim is load-bearing.
4. **No "obviously".** $E_d$-chiral vs $E_1$-chiral distinctions, Drinfeld-centre identifications, explicit framings are load-bearing — never hand-wave.
5. **Physical intuition and formal rigor coexist.** 6d hCS / M-theory pictures and their formal counterparts are both first-class.
6. **Honest subtlety.** *This is subtle* + dissection beats *somewhat delicate*. Pattern 273 discipline ($\Phi$-as-functor vs object-level correspondence) is a recurring subtlety — spell it out.
7. **Healing over downgrade.** When an attack finds a broken proof: fix the proof, statement, or construction. Sharpen definitions, add the missing lemma, supply the worked example, mechanize the step, or state the exact obstruction and its repair route. Do not delete the theorem. Do not demote to motivation. Do not move to an appendix and call the manuscript repaired. Do not change a status label without healing the underlying proof. Conjecture / expected / heuristic labels are temporary honest-status markers, not closures (`INVARIANTS.md §XI`).
8. **Three-axis scope check.** Before inscribing any theorem, scope-check: what level, what chart, what ambient. A statement underscoped on any axis is a defect.

## Self-reflection rubric — before any inscription, chapter revision, or merge

| Category | Top-marks test |
|---|---|
| Correctness | Every step verified. No gap. No unsignalled assumption. |
| Rigor | Every load-bearing claim carries *proved / conjectured / expected / heuristic / computed / folklore*. |
| Attribution | Every prior result cited by author + year + theorem / equation number. |
| Concrete-before-abstract | Worked case precedes general statement. |
| Voice | Russian school + mathematical-physics frontier (`INVARIANTS.md §IV`; `MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md`). |
| Standalone | No version labels. No phase labels. No prior-draft references. No catalogue IDs in reader-facing prose. (`INVARIANTS.md §III`) |
| Three-axis scope | Theorem declares (level, chart, ambient) coordinates. Promotion across coordinates names the comparison arrow. |
| Deep-semantic merge | Every cross-volume / cross-chapter cross-reference re-checked (`INVARIANTS.md §VII`). |
| Compute agreement | `compute/` output agrees with prose. If not, the compute is usually right — stop and reconcile. |

If any category falls short — restart that category. Do not patch.

## Proof-obligation discipline

- **Proved** → complete argument in this tree or cited reference (page + theorem + year).
- **Conjecture / expected** → named evidence: worked case, cohomological computation, physical heuristic.
- **Heuristic** → physics argument named (BCOV, bootstrap, SUSY localization, anomaly matching) and rigor level called out.
- **Computed** → `compute/` or `notes/` entry; cite file + line. Pattern 273: functorial-level vs chain-level reading is always labeled.

## Long-context handling

Frontier inventories, swarm logs, and chapter TeX easily exceed 10K tokens.

1. Outline internally before writing.
2. Parallel-`read_file` every cited chapter, compute file, cross-volume reference.
3. Hold the whole chapter or inventory in context; compact side lanes, never load-bearing math.
4. When consulting `notes/wave*_*.tex` or `notes/adversarial_*/`, the synthesis (`notes/wave*_frontier_inventory.tex` or `SYNTHESIS.md` of the swarm) is the canonical entry point — not every individual agent file.

## User-authorised max-effort swarm protocol

When the user explicitly asks for a large adversarial, rescue, review, or cross-volume swarm, treat that as authorisation to use the largest useful swarm the runtime can support. Do not downshift because of old 3-agent / 5-agent / 30-agent cautionary language. Request the strongest available model and the highest available reasoning budget for research agents when the host exposes those controls. When it does not, encode the same requirement in the agent prompt: proof-grade, first-principles, max-effort mathematical reasoning.

Swarm design must be explicit before launch:

- Partition agents by disjoint mathematical axes, files, or proof obligations; no two agents own the same theorem.
- Name the integration owner; subagents provide evidence, not authority.
- Forbid agents from reverting work they did not make.
- Require deep semantic merge across `~/chiral-bar-cobar`, `~/chiral-bar-cobar-vol2`, `~/calabi-yau-quantum-groups`, `~/igusa-cusp-form`, `~/mixed-holomorphic-topological-strings` whenever claims cross repositories.

Every attack-heal agent must return a compact, checkable report: claim attacked, failure mode or proof, local file anchors, primary source anchors where needed, exact formulas / constants, claim-status recommendation, files changed, tests or computations run, remaining open questions. For theorem-level work, require repeated attack / heal cycles until convergence: no new fatal attack survives, and at least one real mathematical improvement is inscribed.

The main thread integrates; agents do not vote truth into existence. Preserve all mathematically substantive content; resolve conflicts by reading both sides in context; verify with targeted `rg`, local computations, and session-end builds only when appropriate.

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

Any claim about $\kappa_{\mathrm{BKM}}$, $\Phi(K3 \times E)$, K3 abelian Yangian, MO $E_2$-structure, or six-routes chiral audit must be consistent across the corpus. Disagreement is the deliverable; report, do not silently reconcile.

## Codex load order

1. `~/ecosystem/INVARIANTS.md` (Sections I, III, IV, VI, VII, IX, XI binding for this repo).
2. `~/ecosystem/AGENTS-HARNESS.md` §VIII (self-reflection rubric).
3. `./CLAUDE.md`.
4. This file.
5. Repo master PDF (`calabi_yau_quantum_groups.pdf`); `FRONTIER.md` if extant.
6. `notes/chatgpt_critique_consequence_map_adversarial_review.md` (three-axis discipline, chain fusion).
7. `notes/platonic_ideal_architecture_vol3.md` (target architecture).
8. `appendices/first_principles_cache.md` (canonical-values registry; compatible-dual-readings table).
9. `notes/antipatterns_catalogue.md` (AP-CY catalogue, type-organised).
10. The chapter TeX directly relevant to the task; relevant compute file (e.g. `compute/zte_tensor_engine.py`); Coq / Lean sources for the target claim.
11. Latest `notes/wave*_frontier_inventory.tex` and any in-flight `adversarial_swarm_*/SYNTHESIS.md` only as needed.

## What counts as progress

A new theorem precisely stated, rigorously proved, inscribed with proof body verifiable against primary literature. A new CY example: compute the four $\kappa_\bullet$ for $X$ not yet in `cy_d_kappa_stratification.tex`. A falsified claim repaired by corrected statement, construction, or proof obligation; not deletion, not status-row demotion. A first-principles computation replacing a citation black box. A scope coordinate made explicit on a theorem that previously elided one. A cross-repo disagreement reported and triangulated by primary source.

## What does NOT count as progress

Bare $\kappa \to \kappa_{\mathrm{ch}}^{\mathrm{Hodge}}$ subscript fixes. Status rows. Phantom-label audits. Scope propagation across ten files. FRONTIER retractions. AGENTS.md / CLAUDE.md harmonisation. The PostToolUse hook catches these; do not propagate them as work.

## Hard rules (Vol III specific; INVARIANTS dominate)

1. No AI attribution anywhere. All commits by Raeez Lorgat (`INVARIANTS.md §VI`).
2. No `git stash`. No `git commit --amend`. Deep semantic merges only (`INVARIANTS.md §I, §VII`).
3. Do not build after every edit. Builds at session end on user opt-in: `cd ~/calabi-yau-quantum-groups && make fast`.
4. Never invent a formula. Source: `chapters/examples/cy_d_kappa_stratification.tex`, `chapters/theory/cy_to_chiral.tex`, `working_notes.tex`, primary paper, or direct computation.
5. HZ-7: $\kappa$ always subscripted at every use. HZ-3-11 independent verification protocol applies to any `\ProvedHere` decorator.
6. Claim-status tags are temporary bookkeeping, not repairs. Heal the proof, statement, or construction; do not downgrade the manuscript to close (`INVARIANTS.md §XI`). CY-C is conjectural; $G(X)$ unconstructed for compact non-toric in general; Super-Yangian $Y_{\mathrm{osp}}(4 \mid 20)$ remains conjectural.
7. Standalone documents only (`INVARIANTS.md §III`). No version labels, phase labels, prior-draft references, "Wave $N$ / round / strand / DNA / cache-entry / AP-CY$n$" vocabulary in `chapters/`, `frame/`, `examples/`, `theory/`, `connections/`, `bibliography/`, `appendices/`. Bookkeeping vocabulary lives in `notes/`, commits, and memory only.
8. When a mathematical retraction is genuinely informative — a proof attempted and failed, whose failure forces the successful proof — state the failed argument and its flaw as mathematics, not as a drafting record.
9. The PostToolUse hook (`scripts/hooks/beilinson-gate.sh`, install via `cp scripts/hooks/beilinson-gate.sh .claude/hooks/`) sweeps for AP-CY + cache violations after every Edit / Write. Do not bypass.

## Beilinson's dictum

> What limits forward progress is not the lack of genius but the inability to dismiss false ideas.

3+ independent verification paths for any load-bearing numeric. Paths must be genuinely independent.

**Epistemic hierarchy** (higher wins on conflict): direct computation > `.tex` source ±100 lines > tests > primary literature > concordance > this file > memory.

## Chain-level and $(\infty, 1)$-categorical: equal status

Both lanes load-bearing in Vol III; neither replaces or subsumes the other. State each theorem in the lane in which its proof actually works. Ambient-qualify when both lanes used (Pattern 236). Pattern 273 ($\Phi$-functor vs object-level correspondence) is a scope declaration, not a hierarchy. Never write *this is the chain-level shadow of the real theorem*: both shadows are the theorem, viewed through different lenses.

## Where the bookkeeping lives

- `notes/chatgpt_chiral_duality_critique_consequence_map.md` + `notes/chatgpt_critique_consequence_map_adversarial_review.md` — May 2026 ChatGPT Beilinson critique reconstitution. The deep adversarial review supersedes parts of the original; installs three-axis scope discipline + chain fusion conjecture as inner form.
- `notes/platonic_ideal_architecture_vol3.md` — six-movement platonic architecture target.
- `notes/antipatterns_catalogue.md` — Vol III AP-CY catalogue (AP-CY1–454; type-organised). Append to existing types; do not introduce parallel numbering.
- `appendices/first_principles_cache.md` — confusion-pattern cache; canonical-values registry (every quantity has canonical value + rejected alternatives + source); compatible-dual-readings table (line 103+) for non-contradictions.
- `chapters/examples/cy_d_kappa_stratification.tex` — canonical Vol III $\kappa$ table; Theorem `thm:borcherds-weight-kappa-BKM-universal`.
- `chapters/theory/cy_to_chiral.tex:2840-2856` — correspondence-programme remark.
- `chapters/theory/quantum_chiral_algebras.tex:1247` — bulk = $Z^{\mathrm{der}}_{\mathrm{ch}}$ canonical assertion.
- `working_notes.tex` — sec:two-stage-factorisation, sec:three-tiers-rcy, sec:cy-a3-existence-rigidity, central-identification table.
- `~/chiral-bar-cobar/CLAUDE.md`, `~/chiral-bar-cobar-vol2/CLAUDE.md` — Vol I, Vol II manifestos.
- `~/chiral-bar-cobar/chapters/examples/landscape_census.tex` — canonical $\kappa$ / $r(z)$ per family.
- `~/chiral-bar-cobar/chapters/theory/configuration_spaces.tex:2062-2544` — tangential log curve definition.
- `~/igusa-cusp-form/main.tex:96` — terminal-shadow disclaimer.
- `~/mixed-holomorphic-topological-strings/main.tex:3207-3266` — holomorphic de Rham obstruction discipline.
- `scripts/hooks/beilinson-gate.sh` — version-controlled PostToolUse hook.

## Build (session-end only)

```bash
cd ~/calabi-yau-quantum-groups && make fast
```

## Branch and worktree reconciliation: deep semantic merges only

When branches or worktrees differ, perform a deep semantic merge — no exceptions. Never `git reset --hard`, `git checkout --`, `git restore`, or force-push to clobber work. Read both sides in full; merge at the semantic level (theorem statement, proof structure, prose), not the diff-hunk level. When line-level conflict is semantic — a theorem reworded — pick the stronger statement, the tighter citation, the more rigorous proof. When unclear which side is stronger, read both in context. Do not guess.

Work loss in this programme is irrecoverable. Chapters represent weeks of adversarial-swarm output, elite-voice synthesis, primary-literature audit. Deep semantic merges take longer; they are the only operation consistent with Beilinson's dictum and the golden rule "never cut content".

## Escalation — research-grade triggers

- Proof obligation cannot be discharged with honest rigor → the open obligation, named precisely, **is** the deliverable.
- Cross-volume disagreement across the corpus (Vols I–IV, igusa-cusp-form, mixed-HT-strings) → stop, report.
- Compute-vs-prose disagreement → stop, report; the computation is usually right.
- 8-row Gritsenko–Cléry / 10-row catalogue inconsistency (cover-group stratification) → stop, report; do not silently reassign a row.
- A theorem whose (level, chart, ambient) scope cannot be declared → the obligation is to determine the scope before inscribing.
- Apparent cross-volume contradiction → check the compatible-dual-readings table (`appendices/first_principles_cache.md` line 103+) before editing either side.

## Do not

1. Block large user-authorised swarms. Partition by disjoint files or mathematical axes; require short verifiable reports; merge by deep semantic review.
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
5. **Use the model only for judgment calls.** Cross-references, theorem-numbering, bibliography are deterministic. Codex drafts proofs and worked examples; it does not invent new strata or canonical-values registry rows.
6. **Token budgets are not advisory.** Monograph; checkpoint between axes and between chapters. Long-form proof harness: load context first, build internal outline.
7. **Surface conflicts, don't average them.** Cross-volume vertical equivalences with Vol I are canonical at the Vol I side; if Vol III disagrees, repair Vol III. The 8-row Gritsenko–Cléry / 10-row catalogue inconsistency triggers stop-and-report. Check `appendices/first_principles_cache.md:103+` compatible-dual-readings table before editing either side of an apparent contradiction.
8. **Read before you write.** Read the affected axis chapter and its hypothesis package. Read the canonical $\kappa$-table; never overwrite a canonical value from memory. Cross-reference with `~/chiral-bar-cobar/chapters/examples/landscape_census.tex`.
9. **Tests verify intent.** Claim-status macros, four-part term-coining test, voice-scan, AP-CY catalogue compliance. A theorem whose (level, chart, ambient) scope cannot be declared is broken — determine scope before inscribing.
10. **Checkpoint after every significant step.** Between axes, summarize hypothesis-package delta and cross-volume impact (Vols I/II/IV). Subagents return evidence; main thread integrates via deep semantic merge.
11. **Match the codebase's conventions, even if you disagree.** raeez-math-template per `INVARIANTS.md §XII`. AP-CY catalogue numbering (do not parallel-number). Canonical-values registry pattern.
12. **Fail loud.** Surface every cross-ref break, dangling theorem, unhealed conjecture (`INVARIANTS.md §XI`). 8-row/10-row catalogue inconsistency stops and reports — do not silently reassign a row. Compute-vs-prose disagreements stop and report; computation usually wins.
