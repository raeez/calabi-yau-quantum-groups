# AGENTS.md (Vol III)

> **Inherits `~/ecosystem/INVARIANTS.md`** — canonical ecosystem rules (model-agnostic): destructive-git forbidden list, multi-agent worktree concurrency, standalone-documents discipline, Russian-school voice, every-file-into-the-repo rule, no-LLM-attribution in commits, deep-semantic-merges, intelligence propagation, open-source whitelist.
> **Inherits `~/ecosystem/AGENTS-HARNESS.md`** — canonical Codex / GPT-5-family harness calibration: reasoning-effort per task class, agentic eagerness, tool-use discipline, tool preambles, persistence and stop conditions, verbosity control, uncertainty handling, long-context outlining, self-reflection rubric, scope discipline, error-handling, git-and-worktree restatement for Codex defaults, frontend quality, no-LLM-commit-attribution, voice.
> **Mirrors this repo's `CLAUDE.md`** on substance. Before editing code in this repo, `read_file ./CLAUDE.md` — it carries the repo-local layout, commands, doctrine, and conventions. `AGENTS.md` and `CLAUDE.md` must not diverge in facts; they may differ in structure and voice.
>
> **Load order.** `INVARIANTS.md` → `AGENTS-HARNESS.md` → this repo's `CLAUDE.md` → this file's repo-local section (if any). The closest `AGENTS.md` in the directory tree wins per `agents.md`; explicit principal chat instructions outrank everything.
>
> **Model target.** gpt-5-codex family, `reasoning_effort=high` or `xhigh` for non-trivial work (Pro-class). Terse, declarative voice per `INVARIANTS.md §IV`. No LLM attribution on commits (`INVARIANTS.md §VI`).

---

## Wave-12 inscription roster (2026-04-22/23)

Wave 12 ran ~70 inscription agents across the CY-to-chiral frontier over 2026-04-22/23, keyed in `notes/wave12_*.tex`. The roster is grouped by lane; each entry lists scope and outcome. The synthesis landed in `notes/wave12_frontier_inventory.tex` (15pp, five cross-sections plus 20 single-sentence frontier targets) and in the wave-12 chapter-level inscriptions tracked by the PostToolUse hook log.

### Lane A: CY-A/B/C/D framework and $\kappa$-stratification (~25 agents)

- **a1_bar_cobar_gelfand** — bar--cobar duality in Gelfand-elite voice on CY$_d$ categories; 48KB expansion of Theorem A on CY$_3$ chain level. Outcome: clean bar--cobar identification $\Omega B(A) = A$ on CY$_3$; feeds into V3-F18 chain-level closure path.
- **a1_phi_functor_foundations** — Pillar-$\alpha$ two-stage factorisation $\Phi_d = \mathrm{Sp}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$ in first-principles prose; 52KB foundational inscription. Outcome: scope-declared $\Phi$ as functor on $(\infty, 1)$-categories plus object-level chain-level reading (Pattern 273 discipline).
- **a1_shuffle_first_principles** — shuffle-algebra first-principles derivation on toric $\mathbb{C}^3$; input to V3-F24 algebra-half reducible closure.
- **a2_drinfeld_currents_audit** — Drinfeld-currents audit on K3 abelian Yangian against Feigin--Odesskii elliptic. Outcome: current-style presentation confirmed abelian-at-Lie; twist reinstated at vertex level.
- **a2_k3_abelian_yangian_kazhdan** — Kazhdan-voice inscription of K3 abelian Yangian presentation; matches `thm:k3-yangian-abelian`.
- **a2_k3xE_BKM_kazhdan** — Kazhdan-voice BKM on K3 $\times$ E including Hall--Drinfeld double frame; consistent with Wave 13 R2.
- **a2_kappa_invariants_universal_borcherds** — four $\kappa_\bullet$-invariants on the Gritsenko--Cléry 8-row catalogue with cover-group stratification; closes Pillar $\beta'$ accounting.
- **a3_cy_a3_equivalence** — CY-A$_3$ inscription with infinity-categorical resolution; OPEN questions logged on explicit $S^3$-framing $A_\infty$-twisting datum on $\mathrm{Perf}(Q^5)$.
- **a3_MO_E2_etingof** — Etingof-voice Maulik--Okounkov $E_2$-structure audit; verifies $R^{\mathrm{MO}}(u) = \mathrm{Res}_{u = u_\star} \phi^+_{\mathrm{UV}}(u)$ Pillar-$\delta$ cocycle-residue reading.
- **a3_quantum_toroidal_etingof** — Etingof-voice $U_{q, t}(\widehat{\widehat{\mathfrak{g}_{K3}}})$ inscription; V3-F27 sub-split (F27a, F27b, F27c) reinstated.
- **a3_W_infty_lambda_verification** — $\mathcal{W}_\infty[\lambda]$ family verification at $\lambda \to 1$ collapse; feeds Gaberdiel--Gopakumar holographic target.
- **a4_costello_2013_audit** — Costello 2013 factorisation-algebra audit; prop:costello-5-routes-6d-hCS in the line of wave12_a13.
- **a4_k3_yangian_abelian** — Chariot-Pressley-voice K3 abelian Yangian presentation; PDF-inscribed standalone.
- **a4_modular_char_polyakov** — Polyakov-voice modular character of $\Phi(K3 \times E)$; Mukai lattice at $\mathrm{Mp}_4$ cover.
- **a4_zte_T_nekrasov** — Nekrasov-voice ZTE $T$-matrix exact rational; cross-matches Vol II compute engine `zte_tensor_engine.py`.
- **a5_C3_rosetta_nekrasov** — Nekrasov-Rosetta compute on $\mathbb{C}^3$: CoHA$(\mathbb{C}^3) = Y^+$ confirmed; not $\mathcal{W}_{1 + \infty}$ (which lives on the Drinfeld double, not on $A$).
- **a5_cy_d_stratification** — CY-D $\kappa_{\mathrm{ch}}$-stratification across $d \in \{1, 2, 3, 4, 5\}$ with open question on the odd-$d$ formula correction.
- **a5_hCS_BV_BRST_explicit** — explicit 6d hCS BV--BRST Feynman expansion on $\mathbb{C}^3$; V3-F27a ingredient.
- **a5_mock_modular_polyakov** — Polyakov-voice K3 mock-modular theorem at $d = 2$; cross-validates thm:k3-mock-modular-proof.
- **a6_derived_center_beilinson** — Beilinson-voice derived-centre Pillar-$\delta$ reading; Maulik--Okounkov stable envelopes as global $K$-theoretic bypass of hocolim obstruction.
- **a6_hochschild_coderived_beilinson** — Beilinson-voice Hochschild coderived audit; Positselski $D^{\mathrm{co}}$ route to Theorem B.
- **a6_universal_borcherds_verification** — universal Borcherds identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ verified across the 8-row catalogue with explicit Fourier constants.
- **a7_coha_w_infty_drinfeld** — Drinfeld-voice CoHA-to-$\mathcal{W}_{1+\infty}$ identification via the Drinfeld double (not on $A$ directly).
- **a7_zte_t_matrix** — ZTE $T$-matrix exact rational inscription; 35 tests.

### Lane B: Shadow tower, class $\mathbf{M}$, and six routes (~15 agents)

- **a8_en_hierarchy_kapranov** — Kapranov-voice $E_n$-hierarchy on CY$_d$ with $E_d$-chiral vs $E_1$-chiral stratification.
- **a8_shadow_tower** — shadow tower inscription through $m_8, S_8$.
- **a9_class_m_bezrukavnikov** — Bezrukavnikov-voice class-$\mathbf{M}$ logarithmic Drinfeld-centre identification.
- **a9_langlands_higgs_bezrukavnikov** — Bezrukavnikov-voice Langlands--Higgs correspondence at class $\mathbf{M}$; cascades into V3-F28b.
- **a9_mock_modular_k3** — K3 mock-modular inscription; thm:k3-mock-modular-proof cross-verified.
- **a10_class_m_e3_bar** — class-$\mathbf{M}$ $E_3$ bar $= 6^g$ at $g \leq 3$; $g \geq 4$ open pending $d_5$ computation.
- **a10_cy_c_three_routes_soibelman** — Soibelman-voice CY-C three-routes-to-$G(K3 \times E)$: CoHA, Koszul, stable envelope.
- **a10_wall_crossing_soibelman** — Soibelman-voice Kontsevich--Soibelman wall-crossing; 42KB deep audit.
- **a11_coha_y_plus_vs_w_infty** — CoHA $= Y^+$ (positive half), NOT $\mathcal{W}_{1+\infty}$ (which is the Drinfeld double at the dual side); cache-discipline reinscription.
- **a11_shadow_macmahon_kontsevich** — shadow tower vs MacMahon partition asymptotics; 45KB Kontsevich-voice.
- **a11_shadow_tower_kontsevich** — shadow-tower $\{S_k\}$ through $S_8$ in Kontsevich-voice.
- **a12_gravitational_witten** — Witten-voice gravitational-side interpretation; AdS$_3 \times S^3 \times K3$ microstate reading of $\kappa_{\mathrm{BKM}}(\Phi_1) = 5$.
- **a12_six_routes_k3_e** — six-distinct-constructions inscription for $G(K3 \times E)$; cache discipline ("NOT six $\Phi$ applications").
- **a13_bkm_serre_root_unity** — BKM Serre $P_2 = 0$ exact, extended to root-of-unity $N = 2$ module count (324).
- **a13_costello_5_routes_6d_hCS** — Costello-voice five-routes-to-6d-hCS; V3-F27a.
- **a14_chiral_volume** — chiral volume conjecture $\lim_N (1/N) \log |Z_N(X, C)| = (1/2\pi) |\mathrm{AJ}_X(C)|$; conditional on CY-A$_3$.
- **a14_quiver_chart_gaiotto** — Gaiotto-voice quiver-chart inscription on $\Sigma_{0, 24}$.
- **a15_e8xe8_super_yangian** — $E_8 \times E_8$ Super-Yangian $Y_{osp}(4|20)$ structure function degree $(24, 24)$; V3-F26.
- **a15_moonshine_segal** — Segal-voice Mathieu-moonshine inscription for all 25 $M_{24}$ conjugacy classes; 47KB.

### Lane B: Conifold and Szendrői bridge (~6 agents)

- **b1_coha_w_infty_cross_consistency** — CoHA / $\mathcal{W}_{1+\infty}$ cross-consistency against Vol I landscape census.
- **b1_szendroi_morita** — Szendrői-voice Morita-equivalence on conifold CoHA.
- **b2_cross_volume_consistency** — cross-volume consistency of $\kappa_{\mathrm{ch}}$-values across Vol I / Vol II / Vol III.
- **b2_davison_conifold_coha** — Davison-voice conifold CoHA audit.
- **b3_6d_hCS_E3_gen_rel** — 6d hCS $E_3$-algebra generators and relations.
- **b3_negut_conifold_kernel** — Neguţ-voice conifold kernel: $\kappa_{\mathrm{ch}}(\mathrm{conifold}) = 1$ via direct McKay; NOT a local surface.
- **b4_6d_hCS_BV_BRST_Feynman** — BV--BRST Feynman coefficients for 6d hCS; input to V3-F27a.
- **b4_quantum_toroidal** — quantum-toroidal presentation audit.
- **b5_conifold_chiral_yangian** — conifold chiral Yangian inscription.

### Lane C: K3 $\times$ E bridge and defect-curve (~6 agents)

- **c1_davison_K3E_primer** — Davison-voice K3 $\times$ E primer; CoHA$(K3 \times E)$ frame.
- **c2_oberdieck_2017_audit** — Oberdieck 2017 DT-invariants audit on primitive K3-classes at $N = 1$.
- **c3_lie_bracket_compatibility** — Lie-bracket compatibility across BKM / Hall--Drinfeld / Yangian presentations.
- **c4_K3xE_localisation** — Atiyah--Bott localisation on $K3 \times E$ for the $\mathbb{C}^\times + \mathrm{Aut}(X)$ reduced equivariance stratum.
- **c5_chiral_BKM_defect_curve** — chiral-BKM defect curve on 6d hCS.

### Lane D: Slides, adversarial, holographic (~5 agents)

- **d1_slides_last_pages** — slides-last-pages wrap; programme state as of wave-12 close.
- **d2_conj1_adversarial** — adversarial audit of Lorgat 2020 Conjecture 1; five adversarial holes enumerated.
- **d3_gauge_theory_K3xE_class_S** — gauge-theory class-$\mathcal{S}$ $\mathcal{T}[A_1, \Sigma_{0, 24}]$ on $K3 \times E$.
- **d4_holographic_AdS3** — holographic AdS$_3 \times S^3 \times K3$ microstate-counting reading.
- **d5_quantum_gravity_BH** — quantum-gravity black-hole reading of $\kappa_{\mathrm{BKM}}(\Phi_N)$.

### Lane F: Feynman, $E_3$ generators, meta-audit (~5 agents)

- **f1_6d_hcs_e3_generators** — 6d hCS $E_3$-generators inscription; V3-F27a grounding.
- **f2_bv_brst_to_chiral_ce** — BV--BRST-to-chiral-CE bridge; V3-F18 chain-level closure ingredient.
- **f3_feynman_coefficients_costello** — Costello-voice Feynman coefficients at 6d hCS one-loop.
- **f4_coha_w_infty_consistency** — CoHA / $\mathcal{W}_{1+\infty}$ consistency against $A = $ positive half cache.
- **f5_programme_meta_audit** — programme meta-audit across Vol I / II / III; Pillar-reading-crosscheck against 2026-04-22 spine.

### Lane U: Supervisory two-stage-functor rearchitecture (1 agent)

- **u1_two_stage_functor** — two-stage-functor supervisory note; locks Pillar-$\alpha$ presentation across the wave-12 inscription lane.

### Wave-12 outcome summary

- 20 single-sentence frontier targets logged in `notes/wave12_frontier_inventory.tex`, five of which are lifted into FRONTIER.md Wave-12 section.
- $\kappa$-subscript discipline maintained across all 70+ wave-12 notes (HZ-7 compliance).
- Cache-discipline corrections reinscribed: CoHA $= Y^+$ (not $\mathcal{W}_{1+\infty}$); K3 $\times$ E spectrum $\{2, 3, 5, 24\}$ from four distinct constructions; six routes to $G(K3 \times E)$ are six different constructions, not six $\Phi$ applications; $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$ fails at every $N \in \{1, 2, 3, 4, 6\}$.
- Chapter-level rectifications tracked in `chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex`, `chapters/examples/cy_d_kappa_stratification.tex`, `chapters/examples/k3_chiral_algebra.tex`, `chapters/examples/k3_chiral_bialgebra_platonic.tex`, `chapters/examples/k3_quantum_toroidal_chapter.tex`, `chapters/examples/k3_yangian_chapter.tex`, `chapters/examples/k3e_bkm_chapter.tex`, `chapters/examples/k3e_cy3_programme.tex`, `chapters/theory/hochschild_calculus.tex`, `chapters/theory/quantum_groups_foundations.tex`.
- CY-C remains conjectural; $Y_{osp}(4|20)$ Super-Yangian remains conjectural; CY-A$_3$ chain-level explicit on non-formal CY$_3$ remains the gating frontier.

## What this repository is for

This repository is an instrument for advancing human mathematical
knowledge. Specifically, for understanding the **CY-to-chiral functor
$\Phi: \mathrm{CY}\text{-cat}_d \to \mathrm{ChirAlg}$**, and the seven
faces of $r_{\mathrm{CY}}$ that crystallise the correspondence between
BPS quantum groups (K3 Hall--Drinfeld double / self-mirror K3 Yangian
branch, BKM / Borcherds / Monster) and their
chiral-side analogues.

If you are an agent here, your purpose is identical to that mission.
Every action — read, grep, edit, inscription, refactor, retraction —
serves advancing the mathematics, one true theorem at a time.

When a choice is between doing mathematics and updating accounting,
**do the mathematics.** Accounting is automated by the PostToolUse
hook.

## The mathematics you are working on

**One functor** $\Phi: \mathrm{CY}\text{-cat}_d \to \mathrm{ChirAlg}$,
$d$-dependent output: $E_2$-chiral at $d \leq 2$, $E_1$-chiral at
$d \geq 3$.

**Four $\kappa$-invariants, never conflated**: $\kappa_{\mathrm{ch}}$,
$\kappa_{\mathrm{cat}} = \chi(\mathcal{O}_X)$ (Künneth-**multiplicative**
on products), $\kappa_{\mathrm{BKM}} = c_N(0)/2$, $\kappa_{\mathrm{fiber}}$.
Bare $\kappa$ forbidden (HZ-7 / AP113).

**Key facts** (always-on cache):
- $\kappa_{\mathrm{cat}}(K3 \times E) = 0$ (total space), NOT 2 (fibre).
- The BKM-side K3 object is the Hall--Drinfeld double $\mathcal{D}_\hbar(\mathrm{CoHA}_{K3\times E})$, NOT a Drinfeld Yangian. "K3 Yangian" is historical shorthand for the separate Mukai self-mirror branch.
- $\mathrm{CoHA}(\mathbb{C}^3) = Y^+$ (positive half), NOT $\mathcal{W}_{1+\infty}$.
- Six routes to $G(K3 \times E)$ are six DIFFERENT constructions, NOT six $\Phi$ applications.
- $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$ FAILS at every $N \in \{1,2,3,4,6\}$ (not a coincidence; at $N=1$ LHS = $5$, RHS = $0+0 = 0$). Universal formula: $\kappa_{\mathrm{BKM}} = c_N(0)/2$ (Borcherds 1998; Gritsenko 1999).
- Wave 13 crown: bi-based Ran/$\overline{\mathcal{A}_2}$ architecture, CY-2 $[2]$ shift, class-$\mathcal{S}$ $A_1$ parent on $\Sigma_{0,24}$, $H^2(\mathfrak{g}_{\Delta_5})^{\mathbb{Z}/2,K(1)} = \mathbb{C}\cdot\Delta_5$, and $\Delta_5$ as 1-loop-forced output.
- On the $\mathcal{B}$-family, $K^{\kappa_{\mathrm{ch}}}=8=\mathrm{ord}(H_1)$ and $\hbar^2 \cdot K^{\kappa_{\mathrm{ch}}}=-1$.
- Wave 13 installs 59 AP-CY-W13-* anti-patterns; highest-recurrence confusions are Ikeda↔Gritsenko, BKM-as-Yangian, $\Delta_5$ input-vs-output, Lie-level abelianity versus vertex-level non-abelianity, and CY-3 versus CY-2 shift.
- Class M $E_3$ bar $= 6^g$ at cohomology, NOT infinite.
- At $d \geq 3$, $A$ is $E_1$; $E_2$ lives on $Z(\mathrm{Rep}(A))$, not on $A$.

**Seven parts**: I Foundations · II $\Phi$ functor · III $E_n$ hierarchy
· IV K3 Yangian · V CY landscape · VI Seven faces of $r_{\mathrm{CY}}$ · VII Frontiers.

**Five theorems** (shared with Vol I): A, B, C, D, H.

## What counts as progress

- A new theorem precisely stated, rigorously proved, inscribed with a
  proof body verifiable against primary literature
  (Gritsenko–Nikulin, Borcherds, Schiffmann–Vasserot, Maulik–Okounkov,
  Nakajima, Costello–Gaiotto).
- A new CY example: $\kappa_{\mathrm{ch}}, \kappa_{\mathrm{cat}},
  \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}$ for a CY not yet
  tabulated in `cy_d_kappa_stratification.tex`.
- A falsified claim at a specific parameter point.
- A sharpened scope: narrowest hypothesis on which a proof holds.
- A first-principles computation replacing a citation black box.

## What does NOT count as progress

Bare $\kappa$ → $\kappa_{\mathrm{ch}}$ subscript (bookkeeping). Status
rows. Phantom-label audits. Scope propagation across ten files. FRONTIER
retractions. AGENTS.md ↔ CLAUDE.md harmonisation. The hook catches
these. You do not have to.

## Beilinson's dictum

> What limits forward progress is not the lack of genius but the
> inability to dismiss false ideas.

3+ independent verification paths for numerics. Epistemic hierarchy:
direct computation > `.tex` source > tests > primary literature >
concordance > CLAUDE.md > memory.

## Agent rules (hard)

1. **No AI attribution anywhere.** Commits by Raeez Lorgat only.
2. **No `git stash`.**
3. **Do not amend commits.**
4. **Do not build after every edit.**
5. **Never guess a formula.** Vol III `cy_d_kappa_stratification.tex`,
   `cy_to_chiral.tex`, or primary paper.
6. **User-authorized large swarms are permitted.** When the user
   explicitly asks for a large adversarial or cross-volume swarm,
   launch it with disjoint scopes, explicit integration ownership, and
   deep semantic merge discipline across Vol I/II/III. Runtime limits
   are operational constraints to manage, not repo-level prohibitions.
7. **HZ-7 discipline**: $\kappa$ always subscripted. HZ-3-11
   Independent Verification Protocol applies to ProvedHere decorators.
8. Claim-status tags default `\ClaimStatusConjectured` when uncertain.
   CY-C is conjectural; $G(X)$ is unconstructed in general;
   Super-Yangian is conjectural.

## User-authorized max-effort swarm protocol

When the user explicitly asks for a large adversarial, rescue, review,
or cross-volume swarm, treat that as authorization to use the largest
useful swarm the runtime can support. Do not downshift because of old
3-agent, 5-agent, or 30-agent cautionary language. Request the strongest
available model and the highest available reasoning budget for research
agents when the host exposes those controls; when it does not, encode
the same requirement in the agent prompt: proof-grade, first-principles,
max-effort mathematical reasoning.

Swarm design must be explicit before launch: partition agents by
disjoint mathematical axes, files, or proof obligations; name the
integration owner; forbid agents from reverting work they did not make;
and require deep semantic merge across
`~/chiral-bar-cobar`, `~/chiral-bar-cobar-vol2`,
`~/calabi-yau-quantum-groups`, `~/igusa-cusp-form`, and
`~/topological-strings` whenever claims cross those repositories.

Every attack-heal agent must return a compact, checkable report:
claim attacked, failure mode or proof, local file anchors, primary
source anchors where needed, exact formulas/constants, claim-status
recommendation, files changed, tests or computations run, and remaining
open questions. For theorem-level work, require repeated attack/heal
cycles until convergence: no new fatal attack survives, and at least
one real mathematical improvement is inscribed.

The main thread integrates; agents do not vote truth into existence.
Preserve all mathematically substantive content, resolve conflicts by
reading both sides in context, and verify with targeted `rg`, local
computations, and session-end builds only when appropriate.

## How to work

Formulas come from the Vol III subscripted source. Proofs live in
`chapters/**.tex` with `\label{thm:...}` and
`\begin{proof}...\end{proof}`. After every inscription the
PostToolUse hook (`.claude/hooks/beilinson-gate.sh`) sweeps for
AP-CY + cache violations. Builds at session end on user opt-in.

## Essential constants (Vol III-specific)

- $\kappa_{\mathrm{ch}}(A_X) = \sum_q (-1)^q h^{0, q}(X)$ on compact CY_d.
- $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ across
  $N \in \{1, 2, 3, 4, 6\}$. $N = 1$: Gritsenko $\Delta_5$ weight 5,
  $\kappa_{\mathrm{BKM}} = 5$.
- K3 $\times$ E spectrum: $\{2, 3, 5, 24\}$ from four distinct
  constructions.
- Theorem-C $\mathcal{B}$-family face: $K^{\kappa_{\mathrm{ch}}}=8$,
  Humbert-$H_1$ monodromy order $8$, and $\hbar^2 \cdot
  K^{\kappa_{\mathrm{ch}}}=-1$.
- Local $\mathbb{P}^2$: $\kappa_{\mathrm{ch}} = 3/2$.
- Conifold is NOT a local surface; $\kappa_{\mathrm{ch}} = 1$ via
  direct McKay.

**Five objects never conflated**: $A$, $B(A)$, $A^i$, $A^!$,
$Z^{\mathrm{der}}_{\mathrm{ch}}(A)$. $\Omega(B(A))=A$ is inversion;
$A^!$ via Verdier; bulk via Hochschild.

## Chain-level and $(\infty,1)$-categorical: equal status

Both **chain-level** (explicit complexes, $L_\infty$-twistings,
witnessed homotopies, ambient-qualified Mittag–Leffler towers,
explicit Borcherds-product expansions, explicit
$\kappa_{\mathrm{ch}} = \sum_q (-1)^q h^{0,q}$ Hodge supertraces,
explicit Mukai-vanishing inputs) and **$(\infty,1)$-categorical**
(CY $\infty$-categories of Kontsevich–Soibelman, derived $\infty$-
stable categories of coherent sheaves, the cohomological-Hall algebra
as a stable $\infty$-category construction, Maulik–Okounkov stable
envelopes in derived geometry) mathematics are **equally load-bearing**
in this volume. Neither is "the better lane"; neither "replaces" or
"subsumes" the other.

State each Vol III theorem in the lane in which its proof actually
works. Chain-level: name the explicit denominator formula / Borcherds
product / Hodge-supertrace summand / Mukai vanishing input.
$(\infty,1)$-categorical: name the $(\infty,1)$-functor / cofibre
sequence / dualisable object / fully extended TFT. If both lanes are
needed: state both, ambient-qualified (Pattern 236).

Pattern 273 ($\Phi$ as functor vs object-level correspondence) is a
*scope declaration*, not a hierarchy. **Never** write "this is just
the chain-level / $(\infty,1)$-shadow of the real theorem".

## Where the bookkeeping lives

- `notes/claude_md_legacy_20260418.md` — 899-line Vol III CLAUDE.md,
  lossless. Grep for AP-CY indices + detailed status.
- `notes/agents_md_legacy_20260418.md` — 1508-line Vol III AGENTS.md,
  lossless.
- `notes/first_principles_cache_comprehensive.md` (if local) —
  confusion-pattern registry.
- `~/chiral-bar-cobar/CLAUDE.md` — Vol I manifesto (shared five-theorem
  core, canonical formulas).
- `~/chiral-bar-cobar/chapters/examples/landscape_census.tex` — canonical
  $\kappa$/$r(z)$ per family.
- `~/chiral-bar-cobar-vol2/CLAUDE.md` — Vol II manifesto.
- `chapters/examples/cy_d_kappa_stratification.tex` — Vol III canonical
  $\kappa$ table.
- `chapters/theory/cy_to_chiral.tex` — the $\Phi$ functor construction.
- `scripts/hooks/beilinson-gate.sh` — version-controlled hook.

## Build (session-end only)

```bash
cd ~/calabi-yau-quantum-groups && make fast
```

## Do not

1. Propagate status-label wording when mathematics is waiting.
2. Invent formulas from memory.
3. Run `make fast` after every edit.
4. Add AI attribution anywhere.
5. `git stash` or amend.
6. Read legacy files whole — grep by AP-CY index.
7. Confuse this file with a configuration manual. Mathematician's
   manifesto.

## Branch and worktree reconciliation -- DEEP SEMANTIC MERGES ONLY

When branches or worktrees differ, ALWAYS perform a **deep semantic
merge** to reconcile them. **NO EXCEPTIONS.**

- Never discard one side of a divergence without reading it.
- Never `git reset --hard`, `git checkout --`, or `git restore` to
  clobber work as a shortcut to resolve conflict.
- Never force-push to obliterate upstream divergence.
- Read both sides in full, understand what each side uniquely
  contributes, and construct a merged result that preserves the
  mathematical content, prose improvements, and structural refinements
  from **both** sides. When a line-level conflict is semantic
  (e.g., a theorem statement reworded), merge at the semantic level --
  pick the stronger statement, the tighter citation, the more rigorous
  proof -- not at the diff-hunk level.
- When unclear which side is stronger on a given hunk, read both in
  context. Do not guess.

Applies to: `git pull`, `git merge`, worktree reconciliation, cherry-picks
across branches, rebase conflicts, and any divergence between local and
upstream (including push rejections where upstream has new commits).

**Rationale:** work loss in this programme is irrecoverable -- chapters
represent weeks of adversarial-swarm output, elite-voice synthesis, and
primary-literature audit. A shallow "accept theirs" / "accept ours" is
never the right answer. Deep semantic merges take longer but are the
only operation consistent with Beilinson's dictum and the golden rule
"NEVER CUT CONTENT".

---

## Research-grade Codex / GPT-5 scaffolding (maximum settings)

Vol III of the chiral bar–cobar series: **Calabi–Yau-to-chiral frontier, Yangians, BKM superalgebras, $\kappa$-stratification.** Mathematics-advancement instrument, not a product. Every output here is proof-grade or paper-grade. The harness runs at its ceiling.

### Harness — maximum always

| Parameter | Setting | Rationale |
|---|---|---|
| `reasoning_effort` | **`xhigh`** (always; never lower than `high`) | CY frontier / Yangian / BKM / mock-modular / MO $E_2$ — frontier proof engineering across eight lanes. No downgrade permitted. |
| `model` | **gpt-5-codex family, latest** (current preferred: gpt-5.3-codex; fallback: gpt-5.2-codex) | Pro-class coding + mathematics harness. |
| `verbosity` | As the proof requires | No abridgment of load-bearing calculations. Terse where terse is honest. |
| Token budget | **Unbounded** for research tasks | If context fills, compact side work. Never elide load-bearing equations, Fourier constants, or named lemmas. |
| Tool use | **Parallel reads** for TeX / compute / Coq / Lean sources | Batch `read_file` over every citation before writing. |
| Persistence | **Absolute** | Do not yield on a partial proof. Either close the argument or name the open obligation precisely. |
| Self-reflection rubric | **Required** before any inscription | See `~/ecosystem/AGENTS-HARNESS.md §VIII`; research-grade instantiation below. |

### Research-grade discipline — `INVARIANTS.md §IV` made actionable

1. **Every load-bearing claim carries an epistemic status.** *Proved / conjectured / expected / heuristic / computed / folklore.*
2. **Worked case before general statement.** CY$_3$ before CY$_d$; abelian Yangian on K3 before elliptic on $K3 \times E$; the 8-row Borcherds catalogue before universal $\kappa_{\mathrm{BKM}}$.
3. **Named attribution beats passive voice.** *By Maulik–Okounkov (2012)*, *by Nekrasov–Okounkov (2003)*, *by Costello (2013)*. Year + page where the claim is load-bearing.
4. **No "obviously."** $E_d$-chiral vs $E_1$-chiral distinctions, Drinfeld-centre identifications, and explicit framings are load-bearing — never hand-wave.
5. **Physical intuition and formal rigor coexist.** 6d hCS / M-theory pictures and their formal counterparts are both first-class.
6. **Honest subtlety.** *This is subtle* + dissection beats *somewhat delicate*. Pattern 273 discipline on functorial vs chain-level readings is a recurring subtlety — spell it out.

### Self-reflection rubric (before any inscription, chapter revision, or merge)

| Category | Top-marks test |
|---|---|
| Correctness | Every step verified; no gap; no unsignalled assumption. |
| Rigor | Every load-bearing claim carries *proved / conjectured / expected / heuristic / computed / folklore*. |
| Attribution | Every prior result cited by author + year + theorem / equation number. |
| Concrete-before-abstract | Worked case precedes general statement. |
| Voice | Russian school + mathematical-physics frontier (`INVARIANTS.md §IV`). |
| Standalone | No version labels, no phase labels, no prior-draft references (`INVARIANTS.md §III`). |
| Deep-semantic merge | Every cross-volume / cross-chapter cross-reference re-checked (`INVARIANTS.md §VII`). |
| Compute agreement | `compute/` output agrees with prose. If not, the compute is usually right — stop and reconcile. |

If any category falls short — restart that category. Do not patch.

### Proof-obligation discipline

- **Proved** → complete argument in this tree or cited reference (page + theorem + year).
- **Conjecture / expected** → named evidence (worked case, cohomological computation, physical heuristic).
- **Heuristic** → physics argument named (BCOV, bootstrap, SUSY localization, anomaly matching) and rigor level called out.
- **Computed** → `compute/` or `notes/` entry; cite file + line. Pattern 273: functorial-level vs chain-level reading is always labeled.

### Long-context handling

Frontier inventories (15pp typical), swarm logs (hundreds of inscriptions), and chapter TeX easily exceed 10K tokens:

1. Outline internally before writing.
2. Parallel-`read_file` every cited chapter, compute file, and cross-volume reference.
3. Hold the whole chapter or inventory in context; compact side lanes, never load-bearing math.
4. When consulting `notes/wave*_*.tex`, the synthesis (`notes/wave*_frontier_inventory.tex`) is the canonical entry point.

### Research constellation (cross-repo awareness)

Vol III of the chiral bar–cobar series.

- `~/chiral-bar-cobar` — Vol I: $E_1$–$E_1$ operadic Koszul duality; Theorems A, B, C, D, H; averaging map $\mathrm{av}: \mathfrak{g}^{E_1} \to \mathfrak{g}^{\mathrm{mod}}$.
- `~/chiral-bar-cobar-vol2` — Vol II: $A_\infty$ chiral algebras + 3D HT QFT via $\mathsf{SC}^{\mathrm{ch,top}}$; topologisation ladder.

Adjacent:
- `~/igusa-cusp-form` — Borcherds lift of $\phi_{0,1}$, generalized BKM superalgebras, Igusa cusp form $\Delta_5$. The $\kappa$-stratification here generalizes the Borcherds-product / BKM structure there; the 8-row catalogue here includes the Gritsenko–Cléry rows that sit in the Igusa paper's frame.
- `~/topological-strings` — Kodaira–Spencer gravity, BCOV quantum string amplitudes. Physics dual to the chiral homology of a CY threefold; conventions ($d = \dim_{\mathbb{C}} X$, framing datum on $S^3$) must agree when stated in both.

Any claim about $\kappa_{\mathrm{BKM}}$, $\Phi(K3 \times E)$, K3 abelian Yangian, MO $E_2$-structure, or the six-routes chiral audit must be consistent with the cross-repos. Disagreement is the deliverable; report, do not silently reconcile.

### Reference corpus

- Beilinson–Drinfeld, *Chiral Algebras* (2004).
- Maulik–Okounkov, *Quantum groups and quantum cohomology* (2012).
- Nekrasov, *Seiberg–Witten Prepotential from Instanton Counting* (2003).
- Costello, Costello–Gwilliam on factorization algebras in QFT.
- Gaiotto–Witten on class $S$, VOAs, generalized symmetries.
- Feigin–Odesskii on elliptic algebras.
- Etingof–Gelaki–Nikshych–Ostrik, *Tensor Categories* (2015).
- Gritsenko–Nikulin on lattice Borcherds products; Gritsenko–Cléry on the 8-row catalogue.
- Gaberdiel–Gopakumar on higher-spin holography and $\mathcal{W}_\infty[\lambda]$.
- Bershadsky–Cecotti–Ooguri–Vafa (BCOV, 1993).

### Codex load order

1. `./CLAUDE.md`.
2. `~/ecosystem/INVARIANTS.md §IV` + `~/ecosystem/AGENTS-HARNESS.md §VIII`.
3. Repo master PDF + `FRONTIER.md` + this file's wave-12 roster and lane summaries.
4. Latest `notes/wave*_frontier_inventory.tex` and any in-flight `adversarial_swarm_*/SYNTHESIS.md`.
5. Relevant chapter TeX + `compute/zte_tensor_engine.py` + Coq / Lean sources for the target claim.

### Escalation — research-grade triggers

- Proof obligation cannot be discharged with honest rigor → the open obligation, named precisely, **is** the deliverable.
- Cross-volume disagreement → stop, report.
- Compute-vs-prose disagreement → stop, report; the computation is usually right.
- 8-row / 10-row / Gritsenko–Cléry inconsistency (cover-group stratification) → stop, report; do not silently reassign a row.

