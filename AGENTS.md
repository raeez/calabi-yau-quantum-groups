# AGENTS.md - Calabi-Yau Quantum Groups

## Charter

This file is the always-on Codex constitution for Volume III. It is optimized for Codex with GPT-5.4-style agentic work: persistent tool use, explicit verification, tight scope control, and sharp stopping criteria. `CLAUDE.md` may remain richer and more experimental, but `AGENTS.md` must be the stable operating system that still works after compaction, context loss, or model drift.

Use this file for:

- durable repo-wide invariants;
- task routing and operating modes;
- claim-state and definition discipline;
- cross-volume propagation rules;
- verification and convergence gates;
- the current dated risk map when live repo state materially changes behavior.

Do not use this file for temporary chatter, local TODO spam, or motivational prose that does not change execution.

## Programme Map

Volume III asks a single question:

> In what precise sense can a Calabi-Yau category produce a quantum chiral algebra whose bar data, trace, and modular characteristic match the modular Koszul duality programme from Volumes I and II?

Primary targets:

- `CY-A`: `Phi: CY_d-Cat -> E_2-ChirAlg`
- `CY-B`: `E_2`-chiral bar-cobar adjunction with CY trace as curvature datum
- `CY-C`: quantum-group realization
- `CY-D`: modular CY characteristic

Current hard status boundary:

- `CY-A` is proved in the manuscript only for `d = 2`.
- Any `d = 3` version depends on a chain-level `S^3` framing construction and is not unconditional.
- `A_X`, `G(X)`, and similar CY3 chiral-algebra objects are not constructed objects of this manuscript.
- CoHA is associative data, not automatically the `E_1` sector of a larger chiral object.
- Borcherds denominator identities are not automatically bar Euler products.
- Drinfeld center and derived/chiral center are distinct unless hypotheses are stated.

## Design Axioms for Codex/GPT-5.4

Best-practice prompt design in this repo means reducing entropy, not adding rhetoric.

1. Exact scope before reasoning.
   Name the file, theorem label, definition, convention, family, and status boundary before trying to solve the problem.
2. Verification before verbosity.
   Prefer a short instruction plus a falsifiable check over long exhortation.
3. Reasoning effort is a last-mile knob.
   Before escalating effort, tighten the task definition, output contract, and verification loop.
4. Durable rules, triggered playbooks, mechanical hooks.
   Keep always-on rules here, deep workflows in skills, deterministic enforcement in hooks or grep-based checks.
5. Local truth surfaces over inherited summaries.
   Live `.tex`, compute, tests, logs, and diffs outrank memory, prior chats, and metadata prose.
6. Self-contained state beats hidden context.
   For substantial work, externalize the plan, assumptions, blockers, and verification record in a durable note.
7. Smaller true claims beat larger false ones.
   The objective is not impressive prose; it is surviving hostile rereading.
8. Add instructions only when they change behavior.
   Remove decorative meta-rules, duplicated guidance, and vague slogans that widen the search space.

## Codex-Native Operating Stance

- Default deliverable: a verified change or a precisely named blocker, not an outline.
- Default reasoning: `medium`.
- Escalate to `high` or `xhigh` only for load-bearing proof surgery, chapter-scale architecture, or stalled frontier synthesis after the workflow itself has already been sharpened.
- No plan theater.
  If a plan exists, it must cash out into edits, checks, or a blocker.
- Tool persistence.
  The first plausible answer is not enough; stop only when the relevant falsifier passes or the blocker is real.
- Dependency-first execution.
  Read before editing. Verify prerequisites before downstream claims.
- Parallel evidence gathering.
  Batch independent greps, file reads, log checks, and targeted tests whenever they do not couple tightly.
- Skill-first specialization.
  If a task matches a repo skill, use the skill instead of reconstructing the workflow from scratch.
- `AGENTS.md`, `CLAUDE.md`, README files, and prior agent prose are operational guides, not mathematical evidence.

## Claude-Codex Parity Rule

No durable Claude-side workflow is allowed to remain Claude-only.

Any always-on skill, hook, loop, routine, or metacognitive control surface that changes behavior must have a Codex-native home in one of:

- `AGENTS.md` for always-on rules;
- `.agents/skills/` for triggered workflows;
- `.codex/hooks/` for mechanical routing and guardrails.

If `CLAUDE.md` grows a durable behavior and Codex lacks an analogue, either:

1. add the Codex analogue in the same session; or
2. explicitly mark the parity gap and treat it as unresolved debt.

### Claude -> Codex parity map

- Claude `/build` -> Codex skill `vol3-build-surface`
- Claude `/audit` and `/rectify` -> Codex skill `vol3-beilinson-loop`
- Claude `/chriss-ginzburg-rectify` -> Codex skill `vol3-chriss-ginzburg-rectification`
- Claude `/verify` -> Codex skills `vol3-pre-edit-verification` plus `vol3-claim-verification`
- Claude `/propagate` -> Codex skill `vol3-cross-volume-propagation`
- Claude `/compute-engine` -> Codex skill `vol3-compute-engine`
- Claude `/research-swarm`, `/beilinson-swarm`, `/rectify-all` -> Codex skill `vol3-swarm-orchestration`

Codex-specific delegation rule:

- swarm-style decomposition is permitted only when the user explicitly authorizes sub-agents or delegation;
- absent that authorization, use the same logical workflow locally without spawning agents.

## Session Entry Protocol

For any nontrivial task:

1. Lock the exact target.
   Name the file(s), labels, formulas, conventions, and whether the task is audit, rectification, verification, compute, or frontier work.
2. Read the live target before editing.
   Never patch by pattern alone.
3. Inspect the dirty surface.
   Read the current diff in the touched repo and, when cross-volume claims are involved, inspect the relevant diffs in Volumes I and II.
4. Lock the conventions.
   Check grading, shifts, OPE versus lambda-brackets, `E_1` versus `E_2`, CY dimension versus manifold dimension, and any `kappa` subscripts in play.
5. Name the claim state.
   Decide whether the surface is proved, proved elsewhere, conditional, conjectural, heuristic, or open.
6. Name the narrowest falsifier.
   Usually a targeted `pytest`, grep, local computation, proof trace, or `make fast`.
7. Only then edit.

## Pre-Edit Verification Protocol

This is the Codex analogue of the Claude-side pre-edit templates.

Use `vol3-pre-edit-verification` before editing any surface touching:

- `r`-matrices or OPE/lambda-bracket conversions;
- `kappa` formulas or modular characteristics;
- bar/cobar/Koszul-dual/desuspension formulas;
- d=3 theorem environments, status tags, or unconstructed objects;
- shadow class or SC-formality claims;
- `MF(W)` CY-dimension claims;
- cross-volume Part references;
- hardcoded compute or test oracles.

Protocol:

1. In commentary, write a fenced `PRE-EDIT` block before invoking the edit.
2. Fill in the exact object/formula, convention, source, boundary checks, and wrong variants avoided.
3. End with `verdict: ACCEPT` or `verdict: REJECT`.
4. If any required source is blank or any boundary check fails, do not edit yet.

This protocol is not decorative. Filling the block is part of verification.

## Live Truth Surface

The order of trust in this repo is:

1. direct computation and exact local verification;
2. the live `.tex` or `.py` source, read in context;
3. build logs, test output, and compiler failures;
4. primary literature with explicit convention conversion;
5. audit notes and self-contained verification notes;
6. `AGENTS.md` and the three `CLAUDE.md` files;
7. memory, summaries, prior chat conclusions.

For nontrivial work, the live surface is:

- the target file plus local neighboring context;
- `main.tex` and the active `\input` graph;
- the current dirty diff;
- relevant build logs;
- the narrowest relevant compute/tests slice;
- cross-volume duplicate or advertised claims in `~/chiral-bar-cobar` and `~/chiral-bar-cobar-vol2`.

If these surfaces disagree, investigate. Do not silently pick the most convenient layer.

## Current Empirical Risk Map (April 10, 2026)

This dated section is here because the user explicitly requested that the current failure distribution and dirty state be part of the steering surface. Refresh it when it goes stale.

### Last-100-commit archaeology

- Volume I is dominated by rectification, build-noise cleanup, formula/convention repair, compute/test synchronization, and repeated AP126/AP141, AP124/AP125, AP136, AP137, AP140, AP29, and AP128 failures.
- Volume II is dominated by rectification, convention repair, cross-volume propagation, AP40 environment/status drift, AP44 divided-power drift, AP32 uniform-weight drift, V2-AP26/V2-AP30 stale Part references, V2-AP31 proof-after-conjecture, and V2-AP32/V2-AP35 artifact/connective drift.
- Volume III is dominated by build noise, compute/test frontier corrections, AP113 `kappa`-subscript repair, AP-CY6/AP-CY11/AP-CY14 conditionality failures, AP-CY12 shadow-depth misclassification, AP-CY13 stale Part references, AP-CY17/AP-CY18/AP-CY19 geometric/computational convention drift, and README/doc scope inflation.

### Current dirty hotspots

- Volume I currently has a large compute-and-test rectification wave plus extensive PDF/log noise. The live mathematical hotspots include:
  - Heisenberg versus odd-current versus genuine `E_1` distinction in `chapters/frame/heisenberg_frame.tex`;
  - PBW / Barr-Beck-Lurie proof strengthening and Koszul-dual degree bookkeeping in `chapters/theory/chiral_koszul_pairs.tex`;
  - Bershadsky-Polyakov central charge / `K_BP = 196` corrections in `compute/lib/non_principal_w_bar_engine.py` and its tests;
  - `AGENTS.md` itself is dirty there, so treat Vol I control-surface text as live and evolving.
- Volume II currently has a focused but load-bearing dirty surface in `chapters/connections/thqg_perturbative_finiteness.tex`, where genus-2 stable graph classification is being corrected from an undercount to:
  - 7 total connected stable strata at `g = 2`, `n = 0` if the smooth no-edge stratum is included;
  - 6 edge-bearing Feynman graph types under the at-least-one-edge convention.
  This surface also adds genus-1 vertex contributions, so any citation to genus-2 graph counts or `F_2` graph formulas must be rechecked.
- Volume III currently has a compute/manuscript rectification cluster around:
  - `kappa_ch` versus `kappa_BKM` for `K3 x E`;
  - restoring the level prefix in CY `r`-matrices;
  - correcting local `P^2` from class `L` to class `M`;
  - synchronized updates across `chapters/theory/introduction.tex`, `chapters/connections/cy_holographic_datum_master.tex`, `chapters/examples/toroidal_elliptic.tex`, `compute/lib/modular_cy_characteristic.py`, `compute/lib/swiss_cheese_cy3_e1.py`, and their tests.

Treat all of these as live audit surfaces, not settled facts.

## The Resonance Loop

For any nontrivial task, run this loop until `CONVERGED` or `BLOCKED`.

### 0. Scope Lock

Identify:

- the exact surface;
- the dependent labels, formulas, and conventions;
- whether the task is audit, rectification, verification, propagation, compute rectification, or frontier synthesis.

### 1. Invariant Lock

Before trusting any local argument, lock:

- grading and shifts;
- bar / cobar / Koszul-dual object identity;
- open / closed color directionality;
- OPE modes versus lambda-brackets with divided powers;
- genus / arity / filtration / family scope;
- Volume I versus II versus III conventions.

### 2. Read the Surface

Read the live target before editing anything. Never patch by pattern alone.

### 3. RED Pass

Attack logic and mathematics:

- hidden hypotheses;
- circularity;
- sign or degree errors;
- formula drift;
- overclaimed biconditionals;
- false identifications;
- proofs that silently assume the conclusion.

### 4. BLUE Pass

Attack consistency:

- theorem / proof / status mismatch;
- label drift;
- stale Part references;
- duplicated formulations;
- compute/manuscript disagreement;
- README or metadata advertising a stronger claim than the `.tex` supports;
- cross-volume inconsistencies.

### 5. GREEN Pass

Attack structural gaps:

- missing definitions;
- objects used before axiomatization;
- missing lemmas;
- dangling references;
- places where the true statement is weaker than the advertised one.

### 6. Patch in Dependency Order

Fix `CRITICAL` and `SERIOUS` findings first, then `MODERATE`.
For each fix:

1. re-read the local context;
2. recompute or re-derive independently;
3. make the smallest truthful edit;
4. immediately search for downstream advertisements of the old claim.

### 7. Propagate

After any mathematical change:

- grep Volume III;
- grep Volume II;
- grep Volume I;
- verify sameness of object and convention before editing a verbal match;
- update genuine duplicates in the same session or leave an explicit pending note.

### 8. Verify

Run the narrowest check that can actually falsify the change:

- targeted `pytest`;
- targeted grep or label check;
- proof trace;
- log inspection;
- `make fast` for load-bearing manuscript rewrites;
- broader build only when the local slice passes and scope demands it.

### 9. Re-Audit

Hostilely reread your own rewrite. Try to break it.

### 10. Convergence

- `CONVERGED`: no known actionable `MODERATE+` finding remains on the modified surface, and the narrowest relevant verification passes.
- `BLOCKED`: exact blocker named precisely.

Do not stop in between.

## Convergent Writing Loop

For introductions, prefaces, chapter openings, architectural rewrites, and other load-bearing prose:

1. write a first truthful draft;
2. reimagine the structure under hostile and compression-minded rereading;
3. rewrite from scratch rather than line-polishing a bad skeleton;
4. run a Beilinson audit on the rewritten surface;
5. repeat until no actionable `MODERATE+` finding remains.

Minimum standard:

- preface/introduction scale work: three or more iterations;
- chapter openings and major transitions: two or more iterations.

Structural moves worth preferring when they genuinely fit:

- deficiency opening;
- unique-survivor framing;
- instant computation;
- forced transition;
- decomposition table;
- true dichotomy;
- sentence-as-theorem compression.

## Operating Modes

### Mode 1 - Default Research Mode

Use for ordinary manuscript, notation, compute, and proof maintenance.

Loop:

1. identify the exact target;
2. read the local source;
3. inspect the nearby diff and dependencies;
4. make the smallest defensible correction;
5. run the narrowest falsifier;
6. propagate shared formula/status changes;
7. stop only when the surface is coherent.

### Mode 2 - Deep Beilinson Audit

Trigger when asked to audit, review, red-team, challenge, falsify, or pressure-test a theorem, chapter, formula family, or region.

Audit the live surface:

- `main.tex`;
- current `\input` graph;
- dirty diff;
- relevant logs;
- narrow compute/tests slice.

Mandatory passes:

- `RED`: logic, formulas, signs, hypotheses, scope, hidden conditionality;
- `BLUE`: collisions across intro/chapter/examples/appendices/compute/tests/README/other volumes;
- `GREEN`: missing definitions, dangling references, absent lemmas, frontier gaps, overstated claims.

Findings are mathematical bugs, not editorial trivia.

### Mode 3 - Beilinson Rectification Loop

Trigger when asked to fix, rectify, converge, tighten, or repair a mathematical surface.

Rectification loop:

1. identify claims and dependencies;
2. classify findings by severity and order;
3. fix `CRITICAL` and `SERIOUS` first;
4. after each fix, rerun the narrowest falsifier;
5. re-audit the modified surface;
6. repeat until no actionable `MODERATE+` finding remains.

### Mode 4 - Multi-Path Claim Verification

Trigger when asked whether a formula, invariant, theorem statement, example, or comparison is correct.

Minimum standard:

- at least three genuinely independent verification paths for any load-bearing numerical or computational claim;
- at least two independent paths for test oracles when three are not practical.

Allowed path families:

1. direct computation;
2. structurally different equivalent formula;
3. limiting or degenerate case;
4. symmetry or duality;
5. cross-family consistency;
6. literature comparison with convention check;
7. degree / weight / sign / units analysis;
8. numerical evaluation;
9. operadic or factorization consistency;
10. descent to a classical/PVA/shadow.

Mandatory Vol III overlays when relevant:

- `AP-CY1`: CY dimension is not real dimension;
- `AP-CY2`: CY trace lives in negative cyclic, not merely Hochschild;
- `AP-CY5`: quantum-group claims must specify the `q` regime;
- `AP-CY6` / `AP-CY11` / `AP-CY14`: d=3 conditionality propagates;
- `AP-CY7`: CoHA is not automatically an `E_1`-chiral algebra;
- `AP-CY8`: denominator identity is not automatically a bar Euler product;
- `AP-CY12`: shadow class comes from the full tower, not a leading approximation;
- `AP49`: cross-volume convention conversion.

### Mode 5 - Cross-Volume Propagation Sweep

Trigger whenever you change a:

- formula;
- theorem status;
- definition;
- notation;
- convention;
- summary sentence advertising a result;
- claim touching `kappa`, `Theta`, bar/cobar, CoHA, `E_1`/`E_2`, Borcherds products, quantum groups, centers, or shadow towers.

Propagation protocol:

1. grep Volume III;
2. grep Volume II;
3. grep Volume I;
4. verify sameness of object and convention before editing;
5. update all genuine duplicates or explicitly mark what remains pending and why.

Never paste formulas between volumes without explicit convention conversion.

### Mode 6 - Compute Rectification Mode

Trigger whenever a `.py` engine, test oracle, table value, hardcoded coefficient, or numerical claim is edited.

Rules:

- Every new or changed hardcoded value must record source and normalization.
- Engine and test must not derive from the same mental model.
- Prefer exact arithmetic when the claim is exact.
- When a formula changes, audit neighboring comments, docstrings, and tests for stale reasoning.
- If a compute result is important enough for the prose, it is important enough for an independent executable check.
- Build artifacts are never evidence.

This mode exists to prevent AP10, AP38, AP80, AP122, AP123, AP128, AP140, and the recurring "engine and test agree on the same wrong number" failure.

### Mode 7 - Frontier Research Mode

Trigger for new theorems, new definitions, new constructions, and CY3 frontier architecture.

Frontier rule set:

1. define the object before naming the programme around it;
2. test toy models before general prose;
3. search for counterexamples early;
4. separate construction, evidence, conditional result, conjecture, heuristic, and slogan explicitly;
5. never upgrade a frontier claim to theorem status in the same pass that first drafts its proof;
6. default new Vol III formal frontier statements to `conjecture` unless the proof is complete and unconditional.

This mode exists to prevent AP36, AP40, AP42, AP43, AP-CY6, AP-CY11, and AP-CY14.

## Claim-State Governance

Every serious statement must belong to exactly one of:

- `\ClaimStatusProvedHere`
- `\ClaimStatusProvedElsewhere`
- `\ClaimStatusConditional`
- `\ClaimStatusConjectured`
- `\ClaimStatusHeuristic`
- `\ClaimStatusOpen`

Rules:

- status is part of the mathematics, not decoration;
- theorem/proposition/lemma/corollary environments are for proof-bearing or genuinely cited results only;
- conjectural or heuristic material does not belong in theorem-like environments;
- if the proof chain passes through an unconstructed d=3 object, the result is at least `Conditional`, and often `Conjectured`;
- if the proof proves less than the sentence claims, weaken the sentence;
- do not strengthen both statement and status in the same unchecked pass;
- when status changes, update the environment, label prefix, surrounding prose, downstream advertisements, and any compute/docs surface selling the claim.

## Definition-First and Object Discipline

Before using a central object in a theorem, ensure the manuscript already contains a formal definition with hypotheses and ambient category.

This is non-negotiable for:

- `G(X)` or any "quantum vertex chiral group";
- any `A_X` or `A_{K3 x E}` at `d = 3`;
- any `C(g,q)` or quantum-group object whose existence is part of the programme;
- any center construction where "center" might mean Drinfeld center, derived center, or factorization object;
- any "bulk algebra" language that could mean different constructions;
- any claim that sells CoHA as if it were already the chiral object itself.

Never conflate:

- `A` (algebra);
- `B(A)` (bar coalgebra);
- `A^i = H^*(B(A))` (dual coalgebra);
- `A^! = (A^i)^vee` (dual algebra);
- `Z^{der}_{ch}(A)` (derived/chiral center = bulk);
- `Z(Rep^{E_1}(A))` (Drinfeld center of a monoidal category).

## Volume III Invariant Lock

### E_1 / E_2 hierarchy

- `E_1`-chiral algebras: associative factorization on `C x R`; representation categories are monoidal.
- `E_2`-chiral algebras: braided factorization on `C x C`; representation categories are braided monoidal.
- `E_2` is braided, not symmetric in general.
- `E_1 -> E_2` via Dunn additivity is structural, not automatic at the level of every candidate example.
- The Drinfeld center is not the same object as the derived/chiral center unless explicit hypotheses are stated.

### Kappa discipline

Bare `kappa` is forbidden in Volume III unless the local section explicitly binds it to one approved invariant.

Approved subscripts:

- `kappa_ch`: chiral modular characteristic;
- `kappa_cat`: categorical / Euler-like invariant when precisely defined;
- `kappa_BKM`: Borcherds-Kac-Moody / automorphic-weight invariant;
- `kappa_fiber`: fiber/lattice invariant when precisely defined.

Immediate sanity rule:

- `K3 x E` has multiple `kappa`-type numbers.
- Current active rectification distinguishes `kappa_ch(K3 x E) = 3` from `kappa_BKM(K3 x E) = 5`.
- Never write `kappa(K3 x E) = 5` unqualified.
- If `kappa_cat` or `kappa_fiber` enter, re-check the live source instead of inheriting a remembered value.

### Load-bearing d=3 boundaries

- `CY-A` is unconditional only for `d = 2`.
- Any d=3 theorem depending on chain-level `S^3` framing, chart gluing, or unconstructed `A_X` is not `ProvedHere`.
- CoHA is associative and may be evidence for an `E_1` sector, but it is not identical to the `E_1`-chiral algebra.
- Local `P^2` must be classified from the full shadow tower, not a leading Lie-type approximation.
- `MF(W)` has CY dimension `n - 2` for `W: A^n -> A^1`, not `n - 1`.

## Canonical Checks

Verify against these before trusting a sentence or test:

```text
kappa(H_k) = k
kappa(Vir_c) = c/2
kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)
kappa(W_N) = c*(H_N - 1),  H_N = sum_{j=1}^N 1/j

r^KM(z) = k*Omega/z
r^Heis(z) = k/z
r^Vir(z) = (c/2)/z^3 + 2T/z

c_bc(lambda) = 1 - 3(2*lambda-1)^2
c_bg(lambda) = 2*(6*lambda^2 - 6*lambda + 1)
c_bc + c_bg = 0

B(A) = T^c(s^{-1} A-bar),   A-bar = ker(epsilon)
|s^{-1}v| = |v| - 1
d_bar^2 = 0
MC: d*Theta + (1/2)[Theta,Theta] = 0
QME: hbar*Delta*S + (1/2){S,S} = 0
F_1 = kappa/24
F_2 = 7*kappa/5760
eta(tau) = q^(1/24) * prod_{n>=1}(1-q^n)
Cauchy normalization = 1/(2*pi*i)

K_BP = 196
genus-2 stable graph count:
  7 total connected stable strata at g=2, n=0
  6 edge-bearing Feynman types under the at-least-one-edge convention

kappa_ch(K3 x E) = 3
kappa_BKM(K3 x E) = 5
local P^2 = class M, not class L
```

## Forbidden Forms

Grep and fix immediately if any of these appear in the relevant convention:

```text
Omega/z                               # bare level-stripped r-matrix
(c/2)/z^4                             # Virasoro quartic r-matrix term
c*H_{N-1}                             # wrong W_N harmonic-number form
T^c(s^{-1} A)                         # bar complex forgot augmentation ideal
|s^{-1}v| = |v|+1                     # desuspension wrong direction
eta(tau) = prod(1-q^n)                # missing q^(1/24)
K_BP = 2                              # wrong Bershadsky-Polyakov conductor
kappa(K3 x E) = 5                     # unqualified Vol III kappa
local P^2: class L                    # AP-CY12 misclassification
MF(W) is CY_{n-1}                     # wrong matrix-factorization dimension
Part~IV / Chapter~12 hardcoded refs   # stale architecture references waiting to happen
```

## Cross-Volume Anti-Pattern Import

All of the following are in force here:

- the shared Vol I anti-pattern system `AP1` through `AP141` in `~/chiral-bar-cobar/CLAUDE.md`;
- the Vol II system `V2-AP1` through `V2-AP35` in `~/chiral-bar-cobar-vol2/CLAUDE.md`;
- the Vol III system `AP-CY1` through `AP-CY19` in `CLAUDE.md`;
- the workflow anti-patterns `AAP1` through `AAP8`.

### Trigger map

If editing status, theorem environments, or proof blocks, check:

- `AP40`, `AP4`, `AP125`, `AP124`, `V2-AP31`, `AP-CY11`, `AP-CY14`.

If editing `kappa`, modular characteristics, or automorphic weights, check:

- `AP1`, `AP39`, `AP48`, `AP113`, `AP-CY2`, `AP-CY10`, `AP-CY15`.

If editing `r`-matrices, OPEs, or lambda-brackets, check:

- `AP19`, `AP44`, `V2-AP34`, `AP117`, `AP126`, `AP141`.

If editing bar/cobar/Koszul-dual/bulk material, check:

- `AP14`, `AP25`, `AP34`, `AP50`, `AP132`.

If editing shadow depth, class, or SC-formality claims, check:

- `AP14`, `AP131`, `AP-CY12`.

If editing chapter migration, Part references, or duplicated statements, check:

- `AP5`, `AP12`, `AP49`, `AP124`, `AP127`, `V2-AP26`, `V2-AP27`, `V2-AP30`, `AP-CY13`.

If editing compute engines or tests, check:

- `AP10`, `AP38`, `AP80`, `AP122`, `AP123`, `AP128`, `AP140`.

If editing prose, notes, README, or metadata, check:

- `AP29`, `AP121`, `V2-AP29`, `V2-AP32`, `AP115`, `AP-CY15`, `AAP8`.

## Context and Memory Hygiene

For substantial tasks:

- keep a short explicit plan or self-contained audit note;
- after each major phase, restate the target, current status, open risks, and next falsification step;
- anchor conclusions to exact file paths, theorem labels, and test names;
- prefer durable notes under `compute/audit/` or `notes/audit_*.md` for major audits;
- write notes so a newcomer with only the current working tree can continue without hidden chat context;
- do not let summaries harden into truth without rereading the source.

## Beilinson Gate - Post-Edit Mental Hook

After editing any `.tex` or `.py` file, explicitly check:

- did the edit change truth conditions or only presentation;
- is the claim status still honest;
- does the surrounding environment match the status macro;
- did a definition become load-bearing, and if so, is it present;
- did a shared formula require propagation;
- did a cross-volume convention bridge require conversion;
- does the compute layer still support the formula;
- are there hidden CY3 existence assumptions;
- did any proof silently assume the conclusion;
- did the dirty-diff hotspot nearby require a fresh reread rather than a local patch.

For `.tex`, re-check at least:

- `AP40` environment/status mismatch;
- `AP113` unqualified `kappa`;
- `AP-CY6` / `AP-CY11` / `AP-CY14` d=3 existence and conditionality;
- `AP-CY12` shadow depth from incomplete evidence;
- `AP-CY13` stale Part references;
- `AP-CY15` README or summary overclaim if the text advertises the result elsewhere;
- `V2-AP26` / `V2-AP35` stale structural references or broken connectives.

For `.py`, re-check:

- hardcoded expected values versus independent verification;
- source and normalization conventions in literals and docstrings;
- exact arithmetic versus floating approximation where exactness is claimed;
- engine/test independence;
- `AP113` subscripted invariants;
- `AP140` family-specific conductors and duality constants;
- whether adjacent tests, comments, or README surfaces still describe the old result.

## Convergence Gate - Stop-Time Mental Hook

If the session is an audit or rectification session, do not stop until you can honestly say one of:

- `CONVERGED`: modified surface is coherent and verified.
- `BLOCKED`: exact blocker named.

Do not end with a vague half-fix.

## Pre-Commit Gate

Before any commit:

1. run the narrowest build/test verification matching the change;
2. inspect the diff for build artifacts, logs, PDFs, and accidental noise;
3. grep touched surfaces for the highest-risk anti-patterns that match the change;
4. if `RECTIFICATION-FLAG` entered the diff, resolve it or record a precise tracked follow-up before committing;
5. ensure there is no AI attribution in commit message or metadata;
6. ensure all commits remain authored by Raeez Lorgat only.

## Verification Commands

Use the narrowest relevant slice first.

Volume III build:

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
make fast
```

When cross-volume propagation is involved:

```bash
cd ~/chiral-bar-cobar && make fast
cd ~/chiral-bar-cobar-vol2 && make
```

For compute work:

- run targeted `pytest` first;
- expand to a broader suite only if the local slice passes and the scope warrants it.

## Repo-Local Skills and Hooks

This repo may include Codex-native skills under `.agents/skills/` and hook configuration under `.codex/`.

Use:

- `vol3-beilinson-loop` for hostile audit and rectification;
- `vol3-chriss-ginzburg-rectification` for chapter-scale structural fortification;
- `vol3-claim-verification` for formula, theorem, and comparison checks;
- `vol3-cross-volume-propagation` for AP5/AP49-style sweeps.
- `vol3-build-surface` for build/test/log triage and stable verification surfaces;
- `vol3-frontier-research` for new theorem architecture, conjectural synthesis, and truthful frontier packaging;
- `vol3-compute-engine` for executable witnesses, engine scaffolding, and test-surface design;
- `vol3-pre-edit-verification` for mandatory pre-edit check blocks on high-risk surfaces;
- `vol3-swarm-orchestration` for Codex analogues of Claude swarm routines when the user explicitly authorizes delegation.

Current high-value hook surfaces include:

- `session_start_context.py` for startup context loading;
- `user_prompt_router.py` for skill routing and rectification-mode hints;
- `pre_tool_use_policy.py` for destructive-command and pre-commit guardrails;
- `post_tool_use_review.py` for build/test failure blocking;
- `stop_continue.py` for convergence enforcement.

Architectural rule:

- keep this file compressive and always-on;
- move repeated deep workflows into skills;
- move deterministic enforcement into hooks or grep-based checks;
- do not bloat the constitutional layer with playbook detail that belongs elsewhere.

## Final Meta-Rule

The dominant failure mode of this programme is not lack of sophistication. It is confusing two objects, two conventions, two statuses, or two levels of validity that happen to look similar in a special case.

So before trusting any sentence, name all five:

- the object;
- the convention;
- the status;
- the verification path;
- the scope.

If you cannot name all five, the sentence is not ready.
