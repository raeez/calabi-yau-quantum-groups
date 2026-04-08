# AGENTS.md — Calabi-Yau Quantum Groups

## Purpose

This file is the Codex runtime constitution for Volume III. `CLAUDE.md` may contain Claude-specific orchestration, hooks, or command macros, but `AGENTS.md` must stand on its own as the always-on operating system for Codex.

Use this file for:

- durable, repo-wide invariants;
- metacognitive control loops that should survive context drift and compaction;
- claim-status discipline;
- verification discipline;
- Vol III-specific anti-pattern avoidance;
- the bridge from manuscript work to compute, tests, build hygiene, and cross-volume propagation.

Do not use this file as a dumping ground for temporary plans, local task chatter, or aspirational slogans that do not change behavior.

## Codex Design Principles

Codex is strongest in this repo when the environment supplies four things clearly:

1. **Exact scope.** Name the file, theorem, definition, formula, family, and convention before reasoning.
2. **Executable verification.** Prefer checks that can fail: targeted grep, local computation, `pytest`, `make fast`, log inspection, or line-by-line proof tracing.
3. **Sharp stopping criteria.** End only at `CONVERGED` or `BLOCKED`, not at "I looked around and found some things."
4. **Progressive disclosure.** Keep always-on rules in `AGENTS.md`; keep triggered workflows in repo skills; keep deterministic enforcement in Codex hooks where possible.

Design prompts and workflows for Codex accordingly:

- Prefer positive instructions over vague prohibitions.
- Prefer checklists and control loops over essays.
- Prefer local truth surfaces over historical summaries.
- Prefer independent recomputation over pattern completion.
- Prefer smaller true claims to larger false ones.
- Prefer reusable skills for repeated deep workflows.

## What This Is

Research monograph by Raeez Lorgat. Volume III of the modular Koszul duality programme. Volumes I (`~/chiral-bar-cobar`) and II (`~/chiral-bar-cobar-vol2`) built the bar-cobar machine for chiral algebras and its 3d holomorphic-topological QFT interpretation. This volume asks:

> In what precise sense is a Calabi-Yau category, or a more general category with the relevant CY-type structures, actually a Calabi-Yau quantum chiral algebra?

**Title**: *Calabi-Yau Quantum Groups: Chiral Algebras from Calabi-Yau Categories via E_1/E_2 Factorization*

## The Central Question

A CY category `C` of dimension `d` carries a cyclic `A_\infty` structure: a nondegenerate trace

`Tr: HH_*(C) -> k[-d]`

on Hochschild homology. The cyclic bar complex `CC_*(C)` with its `S^d` framing is the primary invariant.

A chiral algebra `A` carries a bar complex `B(A)`, a factorization coalgebra on `Ran(X)`, with the full modular structure controlled by `Theta_A` from Volume I.

The programme is to construct a precise functor

`Phi: CY_d-Cat -> E_2-ChirAlg`

that:

1. takes a CY category as input;
2. extracts the `E_2`-monoidal structure;
3. produces a chiral algebra `A_C` whose bar complex encodes CY cyclic homology;
4. realizes the CY trace as the modular characteristic `kappa(A_C)`.

## The Dual Imperative

Maximalist ambition and maximal truth-seeking are not in tension here. Precision is what lets the ambition survive contact with reality.

When claims outrun proofs:

- strengthen the proof first;
- narrow the theorem second;
- downgrade the status third;
- delete the false slogan if necessary.

Never protect narrative momentum at the expense of truth conditions.

## The Beilinson Principle

Every claim is false until independently verified. Every session should behave as if six hostile examiners are present:

- Beilinson
- Witten
- Costello
- Gaiotto
- Drinfeld
- Kontsevich

Their job is to break the argument. Yours is to help them.

### The Verification Reflex

Before asserting anything nontrivial, ask:

> How do I know this? Did I read it in the live source, compute it, verify it, or merely inherit it?

If the answer is "inherit" or "pattern-match," stop and verify.

### Epistemic Hierarchy

Trust these sources in this order:

1. direct computation and exact local verification;
2. the live `.tex` source, read with local context;
3. build logs, test output, and compiler failures;
4. primary literature with explicit convention check;
5. repo audit notes and concordance-like summaries;
6. `AGENTS.md` and `CLAUDE.md`;
7. memory, summaries, and prior chat conclusions.

If these layers disagree, investigate. Do not silently choose the most convenient one.

## Codex Operating Modes

The always-on layer is small. The deep workflows are triggered.

### Mode 1 — Default Research Mode

Use for ordinary manuscript, proof, notation, and compute tasks.

Loop:

1. identify the exact target;
2. read the local source before editing;
3. inspect the live diff and nearby dependencies;
4. make the smallest correction that can be defended;
5. run the narrowest verification that can falsify the change;
6. propagate any shared formula or status correction;
7. stop only after the modified surface is coherent.

### Mode 2 — Deep Beilinson Audit

Trigger when the user asks to audit, review, red-team, challenge, falsify, or pressure-test a theorem, chapter, formula family, or manuscript region.

Audit the **live manuscript surface**:

- `main.tex`;
- currently `\input`-ed files;
- the dirty git diff;
- relevant build logs;
- the narrowest relevant compute/tests slice.

Run three local passes:

- `RED`: logic, formulas, signs, hypotheses, scope, status tags, hidden conditionality;
- `BLUE`: collisions across intro/chapter/examples/appendices/compute/tests/README/other volumes;
- `GREEN`: missing definitions, dangling references, absent lemmas, frontier gaps, and places where the text overstates what has actually been built.

Findings are mathematical bugs, not editorial trivia.

### Mode 3 — Beilinson Rectification Loop

Trigger when the user asks to fix, rectify, converge, clean up, tighten, or repair a mathematical surface.

Rectification loop:

1. identify the exact claims and dependencies;
2. classify findings by severity and dependency order;
3. fix `CRITICAL` and `SERIOUS` items first;
4. after each fix, rerun the narrowest falsifying check;
5. re-audit the modified surface hostilely;
6. repeat until no actionable `MODERATE` or higher findings remain.

**Convergence condition**:

- `CONVERGED` means the modified surface has no known actionable `MODERATE+` findings and the narrowest relevant verification passes.
- `BLOCKED` means a real missing input, unresolved contradiction, or external dependency is named precisely.

Do not end a rectification session anywhere in between.

### Mode 4 — Multi-Path Claim Verification

Trigger when the user asks whether a formula, invariant, theorem statement, or comparison is correct.

Minimum standard: **three genuinely independent verification paths** for any numerical or computational claim.

Use the Vol I verification taxonomy:

1. direct computation;
2. alternative formula;
3. limiting case;
4. symmetry or duality;
5. cross-family consistency;
6. literature comparison with convention check;
7. dimensional or degree analysis;
8. numerical evaluation.

For Vol III, add these mandatory checks when relevant:

- `AP-CY1`: CY dimension `d` is not complex dimension `n` versus real dimension `2n`;
- `AP-CY2`: CY trace lives in `HC^-_d(C)`, not merely `HH_d -> k`;
- `AP-CY5`: quantum-group claims must specify the `q` regime;
- `AP-CY6`: any CY3 chiral algebra claim may be conditional on an `S^3` framing construction;
- `AP-CY7`: CoHA is associative; it is not automatically the `E_1` sector of anything;
- `AP-CY8`: denominator identity is not automatically a bar Euler product;
- `AP49`: convention conversion across Volumes I, II, and III.

### Mode 5 — Cross-Volume Propagation Sweep

Trigger whenever you change a:

- formula;
- theorem status;
- definition;
- notation;
- convention;
- summary sentence that advertises a result;
- claim touching `kappa`, `Theta`, bar/cobar, CoHA, `E_1`/`E_2`, Borcherds products, quantum groups, or center constructions.

Propagation protocol:

1. grep Volume III;
2. grep Volume II;
3. grep Volume I;
4. verify that similarly worded statements are actually in the same convention;
5. update all genuine duplicates in the same session or explicitly mark the remaining ones as pending.

Never paste a formula between volumes without explicit convention conversion.

### Mode 6 — Frontier Research Mode

Trigger for new theorems, new definitions, conjectural architecture, and the CY3 frontier.

Frontier rule set:

1. define the object before naming the programme around it;
2. test toy models before general prose;
3. search for counterexamples early;
4. separate construction, evidence, conjecture, and slogan explicitly;
5. do not upgrade a frontier claim to theorem status in the same pass that first drafts its proof.

This mode exists to prevent AP36, AP40, AP42, and AP43.

## Claim-State Governance

Every serious statement belongs to exactly one of:

- `\ClaimStatusProvedHere`
- `\ClaimStatusProvedElsewhere`
- `\ClaimStatusConjectured`
- `\ClaimStatusHeuristic`
- `\ClaimStatusOpen`

Rules:

- status is part of the mathematics, not decoration;
- theorem/proposition/lemma/corollary environments are for proof-bearing claims only;
- conjectural material belongs in conjecture/observation/remark environments, not theorem environments;
- define load-bearing objects before using them in theorems;
- do not strengthen both statement and status in the same unchecked pass;
- if the proof proves less than the sentence claims, weaken the sentence.

## Definition-First Discipline

Vol III is vulnerable to aspirational objects. Resist that.

Before using a central object in a theorem, ensure the manuscript already contains a formal definition with hypotheses and ambient category.

This is especially non-negotiable for:

- `G(X)` or any "quantum vertex chiral group";
- any putative `A_X` attached to a CY3;
- any center construction where "center" might mean different things;
- any "bulk algebra" language that could mean derived center, Drinfeld center, or factorization object.

## Context and Memory Hygiene

Codex handles long-horizon work better when intermediate state is made explicit.

For substantial tasks:

- keep a short explicit plan;
- after each major phase, restate the target, current best status, open risks, and next falsification step;
- anchor conclusions to exact file paths, theorem labels, and test names;
- prefer stable note files under `compute/audit/` or `notes/audit_*.md` for substantial audit artifacts;
- do not let summaries harden into truth without rereading the source.

## The Codex Analog of Claude Hooks

Claude Code can enforce some workflows automatically via hooks. Codex can do part of this through repo hooks, but not all of it. Therefore the hook logic must exist at two layers:

1. **mechanically**, in repo-local Codex hooks where supported;
2. **cognitively**, as mandatory self-checks in this file.

### Beilinson Gate — Post-Edit Mental Hook

After editing any `.tex` or `.py` file, explicitly check:

- did the edit change the truth conditions or only the prose;
- is the claim status still honest;
- does the surrounding environment match the status macro;
- did a definition become load-bearing and, if so, is it actually present;
- did a shared formula require propagation;
- did a cross-volume convention bridge need conversion;
- does the compute layer still support the formula;
- are there hidden CY3 existence assumptions;
- did any proof silently assume the conclusion.

For `.tex`, re-check at least:

- `AP40` environment/status mismatch;
- `AP43` undefined aspirational object;
- `AP-CY6` nonexistent CY3 chiral algebra;
- `AP-CY7` CoHA versus `E_1` conflation;
- `AP-CY8` denominator/bar-Euler overclaim;
- `AP49` cross-volume convention paste.

For `.py`, re-check:

- hardcoded expected values versus independent verification;
- source and normalization conventions in literals;
- exact arithmetic versus floating approximations where the claim demands exactness;
- existence of at least three meaningful verification paths for any new numerical claim.

### Convergence Gate — Stop-Time Mental Hook

If the session is an audit or rectification session, do not stop until you can honestly say one of:

- `CONVERGED`: modified surface is coherent and verified;
- `BLOCKED`: exact blocker named.

Do not exit with vague half-completion.

### Pre-Commit Gate

Before any commit:

1. run the narrowest build/test verification that matches the change, usually `make fast` and/or targeted `pytest`;
2. inspect the diff for build artifacts and accidental noise;
3. ensure there is no AI attribution in commit message or metadata;
4. ensure all commits remain authored by Raeez Lorgat only.

## Repo-Local Codex Skills and Hooks

This repo may include Codex-native skills under `.agents/skills/` and Codex hook configuration under `.codex/`.

Treat them as the Codex analog of Claude slash commands and hook scripts:

- skills are for triggered deep workflows;
- hooks are for deterministic guardrails;
- `AGENTS.md` remains the always-on constitution.

Current high-value Codex-side analogs include:

- `vol3-beilinson-loop` for deep audit and rectification;
- `vol3-chriss-ginzburg-rectification` for chapter-scale architectural fortification;
- `vol3-claim-verification` for multi-path formula and theorem checking;
- `vol3-cross-volume-propagation` for AP5/AP49-style propagation sweeps.

If a workflow repeats and is too large for always-on context, move it to a skill rather than bloating this file.

## The E_1/E_2 Chiral Hierarchy

The key structural ingredient, extending the `E_1` theory from Volume II:

- **`E_1`-chiral algebras**: associative factorization on `C x R`; representation categories are monoidal.
- **`E_2`-chiral algebras**: braided factorization on `C x C`; representation categories are braided monoidal.
- **`E_1 -> E_2` passage** via Dunn additivity: `E_2 ~ E_1 tensor E_1`.
- **CY connection**: for `d = 2`, the `S^2` framing of `HH_*(C)` provides an `E_2` structure on cyclic homology.

The Drinfeld center

`Z(Rep^{E_1}(A)) ~ Rep^{E_2}(Z^der_ch(A))`

is the categorical incarnation of the bulk-boundary correspondence only under explicit hypotheses. Never treat "center" as unqualified shorthand.

## Main Theorem Targets

- **CY-A**: CY-to-chiral functor `Phi: CY_d-Cat -> E_2-ChirAlg`
- **CY-B**: `E_2`-chiral bar-cobar adjunction, CY trace as curvature
- **CY-C**: quantum group realization
- **CY-D**: modular CY characteristic

These are targets, not automatic statuses. Before writing "Theorem," verify what is proved in this manuscript and in what dimension.

## Current Load-Bearing Gaps and Status Boundaries

These are the places where overclaiming is easiest and most damaging:

- `CY-A` is proved in the manuscript only in the `d = 2` case. Any `d = 3` version is conditional on a chain-level `S^3` framing construction.
- `A_X` for a genuine CY3 is not currently a defined constructed object in the manuscript.
- CoHA is not itself an `E_1`-chiral algebra; at best it is a target candidate for what an `E_1` sector should recover if the larger object exists.
- The bar Euler interpretation of Borcherds-type products in `d = 3` is an observation or analogy unless the relevant CY-to-chiral functor actually exists in that dimension.
- Drinfeld center and derived/chiral center are distinct constructions unless hypotheses are stated.

## Architecture of the Monograph

**Part I — CY Categories and Cyclic Structures**

- CY categories: smoothness, properness, CY condition, trace
- cyclic `A_\infty` structures: cyclic bar complex, `S^d` framing
- Hochschild calculus: duality and categorical Hodge theory

**Part II — E_1 and E_2 Chiral Theories**

- `E_1`-chiral review from Volume II
- `E_2`-chiral algebras as the central innovation
- higher `E_n` factorization structures

**Part III — The Bridge**

- CY-to-chiral functor
- quantum chiral algebras
- modular trace and obstruction tower

**Part IV — Quantum Groups and Braided Structure**

- quantum group foundations
- braided factorization and `E_2` bar-cobar
- Drinfeld center and bulk algebras

**Part V — The Standard Landscape**

- Fukaya categories
- derived categories of CY manifolds
- matrix factorizations
- quantum group representation categories

**Part VI — Connections and Frontier**

- bridge back to Volume I
- modular Koszul duality and CY geometry
- geometric Langlands and CY quantum groups

## Dependencies on Volumes I and II

| Volume | Provides | Used here |
|--------|----------|-----------|
| I | bar-cobar machine, `Theta_A`, `kappa(A)`, five theorems | CY bar complex, modular trace, shadow obstruction tower |
| II | `SC^{ch,top}`, PVA descent, DK bridge, `E_1` sector | `E_1` chiral theory, braided structure, bulk-boundary |

## The Multi-Path Verification Mandate

Every computational result must be supported by multiple independent computations that converge to the same result. Minimum: **three genuinely independent verification paths per numerical claim**.

The compute layer is the verification engine:

- every nontrivial computational formula should have corresponding tests;
- every new compute engine should come with a meaningful test surface;
- hardcoded values must record their source and normalization;
- tests that merely re-encode a single derivation are not enough.

Cross-volume propagation is part of verification, not aftercare.

## Anti-Patterns

All anti-patterns `AP1` through `AP49` from Volumes I and II apply here. The ones that most often kill Vol III are below.

### Frequently Triggered Cross-Volume and Vol III Failures

- **AP35 — Accidentally correct theorem.**
  The statement may be right while the proof only proves a smaller case.

- **AP36 — Biconditional overclaim.**
  A target theorem gets written as proved when the construction only exists conditionally or partially.

- **AP38 — Literature normalization baked into code.**
  Hardcoded values without source and convention labels silently poison the compute layer.

- **AP40 — LaTeX environment contradicts claim status.**
  Conjectural or heuristic material appears in theorem-like environments.

- **AP42 — Correct at sophisticated level, false at naive level.**
  A high-level analogy gets flattened into a false literal identity.

- **AP43 — Central object defined by aspiration, not by axioms.**
  The text names a grand object before defining it.

- **AP44 — OPE mode is not lambda-bracket coefficient.**
  Do not forget the divided-power factor.

- **AP45 — Desuspension lowers degree.**

- **AP46 — `eta(q)` includes `q^{1/24}`.**

- **AP47 — Evaluation-generated core is not full category.**

- **AP48 — `kappa` depends on the full algebra, not just the Virasoro subalgebra.**

- **AP49 — Cross-volume paste without convention conversion.**
  Volume I uses OPE modes; Volume II uses lambda-brackets; Volume III uses motivic/categorical conventions.

### Vol III-Specific Pitfalls

- **AP-CY1**: CY dimension `d` is not complex dimension `n` versus real dimension `2n`.
- **AP-CY2**: the CY trace is a class in `HC^-_d(C)`, not merely a map `HH_d -> k`.
- **AP-CY3**: `E_2` is braided, not symmetric in general.
- **AP-CY4**: Drinfeld center is not derived/chiral center in general.
- **AP-CY5**: Kazhdan-Lusztig equivalence requires the correct `q` regime.
- **AP-CY6**: `A_X` for CY3 does not exist as a constructed object in this manuscript.
- **AP-CY7**: CoHA is not the `E_1`-chiral algebra.
- **AP-CY8**: Borcherds denominator identity is not automatically a bar Euler product.

## Agent Workflow Anti-Patterns

These are failures at the workflow layer rather than the mathematics layer:

- **AAP1**: tool markup leaked into manuscript files;
- **AAP2**: fragmented renames that leave mixed terminology;
- **AAP3**: the same formula reimplemented repeatedly in compute;
- **AAP4**: proof text appears under conjectural status;
- **AAP5**: build artifacts and noise pollute diffs and commits;
- **AAP6**: status oscillates across sessions;
- **AAP7**: intra-file inconsistency after partial edits;
- **AAP8**: README and metadata drift away from the manuscript.

Treat them as first-class failures. They create mathematical bugs indirectly.

## Build

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
make fast
```

Same engine as Volumes I and II: `memoir`, EB Garamond, `newtxmath`, `thmtools`, `microtype`.

## LaTeX Rules

- All macros live in the `main.tex` preamble. Never introduce `\newcommand` in chapter files; use `\providecommand` only when appropriate.
- Label everything: `\label{def:...}`, `\label{thm:...}`, and so on.
- Cross-reference with `\ref`.
- Do not add packages without checking preamble compatibility.
- Do not create a new `.tex` file when the content belongs in an existing chapter.
- Keep theorem environments and claim-status macros aligned.
- When changing theorem status, search for every place the claim is advertised.

## Compute Rules

- New computational claims need tests.
- New engines should live under `compute/` and come with a targeted `compute/tests/` surface.
- For any literature constant or coefficient, record the source and normalization in code comments or docstrings.
- Prefer exact arithmetic when the claim is exact.
- If a formula is important enough for prose, it is important enough for an independent compute check.

## Git — Hard Rule

All commits are authored by Raeez Lorgat.

Never include:

- `Co-authored-by`
- "Generated by"
- any AI attribution

Never commit build artifacts or noise unless explicitly requested.

## Final Meta-Rule

The central failure mode of this project is not lack of sophistication. It is confusing two objects, two conventions, two statuses, or two levels of validity that happen to look similar in a special case.

So:

- name the object;
- name the convention;
- name the status;
- name the verification path;
- then write the sentence.

If you cannot do all five, you are not ready to trust the sentence.
