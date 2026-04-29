# CLAUDE.md (Vol III)

> **Inherits `~/ecosystem/INVARIANTS.md`.** That file holds the canonical ecosystem rules: destructive-git forbidden-command list, multi-agent worktree concurrency, standalone-documents discipline, Russian-school voice, every-file-into-the-repo rule, commits-carry-no-LLM-attribution, deep-semantic-merges, intelligence propagation. Read it first. Repo-local rules follow.

---

## What this repository is for

This repository is an instrument for advancing human mathematical
knowledge. Specifically, for understanding the **CY-to-chiral functor
$\Phi: \mathrm{CY}\text{-cat} \to \mathrm{ChirAlg}$** that sends a
Calabi–Yau category of dimension $d$ to its chiral-algebra image, and
the seven faces of $r_{\mathrm{CY}}$ that crystallise the correspondence
between BPS quantum groups (K3 Yangian, Monster / Borcherds / BKM
algebras) and their chiral-side analogues.

Every tool call, every edit, every agent decision made here has one
purpose: to advance that understanding, one true theorem at a time.

When a choice presents itself between doing mathematics and updating
accounting, **do the mathematics.** Accounting is handled automatically
by the PostToolUse hook and can always be reconciled at session end.

## The mathematics

**One functor**: $\Phi: \mathrm{CY}\text{-cat}_d \to \mathrm{ChirAlg}$.
Its output is $d$-dependent: $E_2$-chiral at $d \leq 2$; $E_1$-chiral at
$d \geq 3$. The CY-A/B/C/D framework dimensionally stratifies the
correspondence. $\Phi$ gives ONE output per category; different
$\kappa$ values come from DIFFERENT constructions, NOT six $\Phi$
applications to one object.

**Four $\kappa$-invariants, never conflated**:
$\kappa_{\mathrm{ch}}$ (chiral-side, via $\Phi$), $\kappa_{\mathrm{cat}}$
(categorical Euler $\chi(\mathcal{O}_X)$, Künneth-**multiplicative** on
products), $\kappa_{\mathrm{BKM}}$ (Borcherds/BKM weight $c_N(0)/2$),
$\kappa_{\mathrm{fiber}}$ (fibre/lattice correction). Bare $\kappa$ is
forbidden; subscript always.

**One K3-specific crystallisation**: the K3 $\times$ E compact
Calabi–Yau threefold carries four $\kappa_\bullet$ values
$\{0, 3, 5, 24\}$ from four **distinct constructions**:
$\kappa_{\mathrm{cat}}(K3 \times E) = 0$ (Künneth-multiplicative
total space; the K3 fibre value $\kappa_{\mathrm{cat}}(K3) = 2$ is not
the total-space value), $\kappa_{\mathrm{ch}}^{\mathrm{Heis}} = 3$
(chiral Heisenberg–Mukai specialisation), $\kappa_{\mathrm{BKM}}
(\mathfrak{g}_{\Delta_5}) = 5$ (Borcherds weight via Gritsenko
$\Delta_5$), and $\kappa_{\mathrm{fiber}} = 24$ (Mukai-lattice rank of
K3). Six routes to $G(K3 \times E)$ exist; they are six DIFFERENT
constructions, NOT six $\Phi$ applications.

**Seven parts** hold the Vol III structure:

| Part | Content |
|---|---|
| I | Foundations — CY categories, factorisation, $E_n$ |
| II | CY-to-chiral functor $\Phi$ |
| III | $E_n$ hierarchy — output scope by dimension $d$ |
| IV | K3 Yangian |
| V | CY landscape — quintic, $K3\times E$, abelian, local surfaces |
| VI | Seven faces of $r_{\mathrm{CY}}$ |
| VII | Frontiers |

**Five theorems** (shared with Vol I): A bar–cobar, B chiral Positselski,
C derived-centre complementarity ($\kappa + \kappa^! \in
\{0, 8, 13, 250/3, 98/3\}$ on the canonical five-archetype
$\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$ landmark
ceiling; the $\mathsf{B}$-row $K^\kappa = 8$ is the Vol III Mukai-enhanced
K3 Heisenberg witness via Bruinier Heegner Chern-class reciprocity),
D obstruction-tower universality, H Hochschild concentration.

Vol III-specific contributions: the CY-A_3 equivalence, the K3
abelian-Yangian presentation, the ZTE $T$ computation, the CY-D
dimensional stratification ($\kappa_{\mathrm{ch}} = \chi(\mathcal{O})$
supertrace identification on compact CY_d), and the universal Borcherds
weight identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ across
$N \in \{1, 2, 3, 4, 6\}$.

## What counts as progress

- A new theorem precisely stated, rigorously proved, inscribed with a
  proof body verifiable against primary literature (Gritsenko–Nikulin,
  Borcherds, Schiffmann–Vasserot, Maulik–Okounkov, Nakajima,
  Costello–Gaiotto for physics input).
- A new example: compute $\kappa_{\mathrm{ch}}, \kappa_{\mathrm{cat}},
  \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}$ for a CY not yet
  tabulated in `cy_d_kappa_stratification.tex`.
- A falsified claim repaired by a corrected statement, construction, or
  proof obligation (e.g., an advertised $\Phi$-identification broken at a
  concrete K3 automorphism).
- A healed statement: the natural hypothesis and proof on which the
  intended theorem actually holds.
- A first-principles computation replacing a citation-only black box.

**Progress is *not*** updating a status-table row, renaming a label
(bare $\kappa$ → $\kappa_{\mathrm{ch}}$ is bookkeeping, not
mathematics), counting six routes to $G(K3 \times E)$ in a
meta-theorem, propagating AP-CY scope across ten files, editing
FRONTIER to match CLAUDE.md, or editing AGENTS.md. The hook catches
these. You do not have to.

## Beilinson's dictum

> What limits forward progress is not the lack of genius but the
> inability to dismiss false ideas.

Every claim is false until independently verified from primary source.
Prefer a smaller true theorem to a larger false one. 3+ independent
verification paths for numerics.

**Epistemic hierarchy** (higher wins):
1. Direct computation.
2. `.tex` source ±100 lines.
3. Build system / tests.
4. Published literature (primary).
5. Concordance (shared with Vol I / Vol II).
6. This file.
7. Memory.

## The manuscript is self-complete, self-coherent, self-consistent

The current version stands for itself and only itself. All LaTeX
mathematical writing is standalone, up-to-date, consistent, coherent.
The manuscript does not reference its own previous versions. There is
no place in this research programme for references to previous
versions, intermediate ansätze, earlier drafts, retracted values,
superseded formulas, or any other drafting-history commentary. If a
formula used to be $X$ and now it is $Y$, the manuscript says $Y$;
it does not say "$Y$ (previously $X$, now retracted)", does not say
"$Y$ supersedes the earlier $X$", does not explain how the author
arrived at $Y$.  The mathematical argument proves $Y$; the drafting
trajectory is not part of the mathematics.

When a mathematical retraction is genuinely informative --- a proof
that was attempted and failed, whose failure illuminates why the
successful proof is forced --- state the failed argument and its
flaw as mathematics: "the identity $[m_k, B^{(2)}] = 0$ fails
per-$k$ because cyclic invariance controls adjacent contractions
but not non-adjacent terms (Proposition~X)". Do not frame it as
"the author initially attempted $X$ but retracted in favour of $Y$".
The mathematics is the Gap/Flaw, not the drafting record.

## Writing standard: Chriss–Ginzburg north star

The manuscript prose is written in the Chriss–Ginzburg voice,
channelling simultaneously the Russian elite mathematical school ---
Gelfand, Manin, Drinfeld, Arnold, Beilinson, Bernstein, Kapranov,
Etingof, Kazhdan, Kontsevich, Soibelman, Bezrukavnikov --- and the
mathematical physics elite --- Polyakov, Nekrasov, Witten, Costello,
Gaiotto, Moore, Segal. **Show don't tell.** Do not narrate. Construct
the mathematics directly and let the synthesis of disparate technical
domains (algebra + geometry, physics + mathematics, operads +
representation theory, Hodge theory + automorphic forms) bring out
the inner music of the subject.

**Forbidden in manuscript prose** (reader-facing `.tex` in `chapters/`,
`frame/`, `examples/`, `theory/`, `connections/`, `bibliography/`):

- Bookkeeping vocabulary of any kind. No "Wave N", no "round M",
  no "batch K", no "DNA strand S$x$", no "AP-CY$n$", no
  "antipattern $n$", no "Pattern $n$", no "cache entry $n$",
  no "CG-rectify pass $k$", no "$\mathsf{HZ}$-$n$ inscription".
  These belong in `notes/`, `FRONTIER.md`, commit messages, and
  the local `memory/` --- never in the manuscript.
- Meta-narration of the author's intent: "we now turn to",
  "having established", "let us now", "this brings us to",
  "it is worth noting", "notably", "crucially", "remarkably",
  "furthermore", "moreover", "in the present work", "this preface's
  role is to". Delete every instance; replace with direct mathematical
  statements.
- Hedging the mathematics does not earn. If the identification
  $X = Y$ is proved, write "$X = Y$"; do not write "$X$ is closely
  related to $Y$". Courage, after Drinfeld and Polyakov and Nekrasov:
  the equals sign is a theorem, not a suggestion.

**Required** (the CG standard):

- Every section and subsection title names a mathematical object,
  construction, theorem, or question --- never a process, wave,
  round, or meta-organising device.
- Every definition is preceded within ten lines by the question
  or obstruction it answers. The reader feels "of course" before
  the definition arrives.
- Every symbol is defined at or before first use, with a
  parenthetical first-principles definition for standard concepts
  (D-module, Ran space, FM compactification, Hodge bundle,
  $L_\infty$-algebra, Kuga--Satake, Humbert divisor).
- Every physical claim is labelled: theorem, heuristic, or
  metaphor. When a physical identification can be stated as a
  theorem, state it as a theorem; do not hide the content as an
  "analogy".
- **Economy.** Every word carries weight. A paragraph that can be
  one sentence is one sentence.
- At every section boundary, three sentences: (1) what was just
  established; (2) the question or obstruction the next section
  resolves; (3) the construction or theorem that resolves it.
  These sentences are *mathematics*, not signposts.

The reader is an equal who sees the force of the argument when it
is stated with sufficient precision. The prose does not explain
mathematics; it *is* mathematics, carrying the same logical force
as the displayed equations.

This rule is retroactive and forward-looking. Existing manuscript
prose containing bookkeeping vocabulary is to be rectified chapter
by chapter through the `chriss-ginzburg-rectify` skill; new prose
is to be written in the CG voice from the first keystroke.

## How to work

**$\kappa$ values come from the subscripted source.** Bare $\kappa$ is
forbidden (HZ-7, AP113). For $\kappa_{\mathrm{ch}}$, compute via $\Phi$
or cite `chapters/examples/cy_d_kappa_stratification.tex`. For
$\kappa_{\mathrm{cat}} = \chi(\mathcal{O}_X)$, Künneth on total space
(e.g. $\kappa_{\mathrm{cat}}(K3 \times E) = 0$, **not** 2 which is the
K3 fibre). For $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$, primary
source Borcherds 1995 / Gritsenko series.

**Key facts** (from the cache — check every claim against these):

- $\kappa_{\mathrm{cat}}(K3 \times E) = 0$ (total space,
  Künneth-multiplicative), NOT 2 (fibre).
- $\mathrm{CoHA}(\mathbb{C}^3) = Y^+$ (positive half), NOT
  $\mathcal{W}_{1+\infty}$ (full).
- Six routes to $G(K3 \times E)$ are six DIFFERENT constructions, NOT
  six $\Phi$ applications.
- $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$
  is FALSE at every $N \in \{1, 2, 3, 4, 6\}$ (numerically: at $N=1$,
  left = $5$, right = $\kappa_{\mathrm{ch}}(K3 \times E) + \chi(\cO_E)
  = 0 + 0 = 0$; at $N=2$, left = $4$, right = $1$). The universal
  formula is $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ (Borcherds
  weight theorem; Gritsenko 1999). See
  \texttt{chapters/examples/cy\_d\_kappa\_stratification.tex}
  Theorem~\texttt{thm:borcherds-weight-kappa-BKM-universal}.
- Class M $E_3$ bar $= 6^g$ at cohomology, NOT infinite.
- At $d \geq 3$, $A$ is $E_1$; $E_2$ lives on $Z(\mathrm{Rep}(A))$, not on $A$.
- Two-stage factorisation: $\Phi_d = \mathrm{Sp}_{\Sigma_{d-1}, C} \circ
  \Phi^{FA}_d$. Stage~1 $\Phi^{FA}_d$ is canonical (Kontsevich–Tamarkin
  $E_d$-formality + Costello–Gwilliam–Li locality); Stage~2
  $\mathrm{Sp}_{\Sigma_{d-1}, C}$ is specialisation, not inversion. A
  single CY$_d$ category admits a family of $E_1$-chiral shadows
  parametrised by $(\Sigma_{d-1}, C)$.
- Universal positive-geometry grammar: $Y^+(X) = H^\bullet_{\mathrm{eq}}(
  \mathcal{M}^+_{\mathrm{eff}}(X), \phi_W)$, with $G(X) = D(Y^+(X))$
  (Drinfeld double of the positive half). CoHA, Nakajima stable-envelope,
  orbifold inertia, lattice-polarised period half-spaces all factor
  through this grammar.
- Four equivariance strata: (i) toric $T^d$ (local $\mathbb{P}^2$,
  $\mathbb{C}^3$, resolved conifold); (ii) reduced $\mathbb{C}^\times$ +
  $\mathrm{Aut}(X)$ (K3, K3 $\times$ E, abelian surface); (iii) orbifold
  inertia $I(X/G)$ (Mathieu $M_{24}$, McKay $\Gamma \subset \mathrm{SU}(d)$);
  (iv) lattice-polarised period domain (Borcherds lifts, Gritsenko
  $\Delta_5$, Igusa $\Phi_{10}$). The stratum fixes the precise
  equivariant cohomology in $Y^+(X)$.
- 8-form Gritsenko–Clery catalogue: weights $(5, 2, 3, 1, 2, 1/2, 3/2, 1)$
  with Fourier coefficients $c_N(0) \in \{10, 4, 6, 2, 4, 1, 3, 2\}$
  so that $\kappa_{\mathrm{BKM}} = c_N(0)/2$ row-by-row. Cover group
  stratification is by the actual multiplier systems of the eight
  diagonal-divisor rows; the catalogue contains no weight-$0$ row and no
  quarter-weight row. The comparison tuple
  $(5,2,1,1,1/2,1,1/4,0)$ is not the Gritsenko--Clery catalogue and cannot
  be identified with it without an explicit row-map datum.
- Maulik–Okounkov $R$-matrix is a gluing-cocycle residue:
  $R^{MO}(u) = \mathrm{Res}_{u = u_\star} \phi^+_{\mathrm{UV}}(u)$
  where $\phi^+_{\mathrm{UV}}$ is the UV positive half's gluing cocycle
  across the equivariant chamber wall at $u_\star$. The MO axiom
  (Yang–Baxter + unitarity) is the cocycle condition for
  $\phi^+_{\mathrm{UV}}$.
- K3 $\times$ E admits no global NCCR: five obstructions — (a) dualising
  sheaf $\omega_{K3 \times E} = \mathcal{O}$ but $\omega$-structure not
  reflexive-tilting; (b) derived McKay requires finite $\mathrm{Aut}$
  fixing a point; (c) HPD self-dual not compatible with product polarisation;
  (d) Mukai vanishing fails off the $K3$ factor; (e) no global CY-$3$
  symmetric obstruction theory. The Serre-equivariant quasi-NCCR
  substitutes: a locally-defined tilting object equivariant under the
  Serre twist, gluing via the factorisation pushforward.
- Dimension-stratified siblings of the Monster: at $d = 3$, the Monster
  $\mathbb{M}$ from $V^\natural$ aligns with Igusa $\Phi_{10}$
  (Gritsenko–Nikulin); at $d = 5$, the Fake Monster Lie algebra (Borcherds
  1990) from the $\mathrm{II}_{25,1}$ lattice is the $d = 5$ sibling of
  the same universal construction. Intermediate $d = 4$ (Conway /
  Leech lattice) bridges both.
- Non-abelian 5D hCS $\to$ Yangian VOA all-orders theorem for simply-laced
  $\mathfrak{g}$: Costello–Gaiotto–Yagi 5D holomorphic Chern–Simons on
  $\R \times \C^2$ quantises to the Yangian VOA $Y^{\mathrm{VOA}}(\mathfrak{g})$
  to all orders in $\hbar$ for $\mathfrak{g}$ simply-laced; the
  perturbative expansion converges (not merely asymptotic) by
  Kontsevich–Tamarkin formality on the holomorphic factor. Non-simply-laced
  requires twisted Yangian; open at all orders.

**Proofs live in `chapters/**.tex`** with `\label{thm:...}` and
`\begin{proof}...\end{proof}`. After every inscription the PostToolUse
hook sweeps the file for Vol III-specific AP-CY violations (bare
$\kappa$, $\Phi$-output-scope confusion, CoHA-vs-vertex-algebra,
Drinfeld-centre-vs-averaging, Künneth multiplicative on products) plus
the general cache patterns.

**Builds at session end only, by user opt-in**:

```bash
cd ~/calabi-yau-quantum-groups && make fast
```

## Essential constants (Vol III-specific)

- $\kappa_{\mathrm{ch}}(A_X) = \sum_q (-1)^q h^{0, q}(X)$ (Hodge
  supertrace identification on compact CY_d).
- $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ for $N \in \{1,2,3,4,6\}$.
  $N=1$: Gritsenko $\Delta_5$ weight 5, $c_1(0) = 10$, $\kappa_{\mathrm{BKM}} = 5$.
- K3 $\times$ E spectrum $\{0, 3, 5, 24\}$ (four distinct constructions):
  $\kappa_{\mathrm{cat}} = 0$ (Künneth total space), $\kappa_{\mathrm{ch}}^{\mathrm{Heis}} = 3$,
  $\kappa_{\mathrm{BKM}}(\mathfrak{g}_{\Delta_5}) = 5$, $\kappa_{\mathrm{fiber}} = 24$.
- Local $\mathbb{P}^2$: $\kappa_{\mathrm{ch}} = 3/2$ (via McKay /
  direct shadow at $d = 3$).
- Conifold is NOT a local surface at $d = 3$; $\kappa_{\mathrm{ch}} = 1$
  via direct McKay.

**Five objects, never conflate** (shared): $A$, $B(A)$, $A^i$, $A^!$,
$Z^{\mathrm{der}}_{\mathrm{ch}}(A)$. $\Omega(B(A))=A$ is inversion;
$A^!$ via Verdier; bulk via Hochschild.

## Chain-level and $(\infty,1)$-categorical: equal status

Both **chain-level** mathematics (explicit complexes, $L_\infty$
twistings, witnessed homotopies, Mittag–Leffler towers, ambient-
qualified statements, explicit $K3 \times E$ Borcherds product
denominator-formula computations) and **$(\infty,1)$-categorical**
mathematics (CY $\infty$-categories of Kontsevich–Soibelman, derived
$\infty$-stable categories of coherent sheaves, the cohomological-Hall
algebra as a stable $\infty$-category construction, Maulik–Okounkov
stable envelopes in derived geometry) are **equally load-bearing** in
Vol III. Neither is "the better lane"; neither "replaces" or "subsumes"
the other.

Vol III in particular owes its content to *both* lanes simultaneously:

- The chain-level lane is what lets you compute $\kappa_{\mathrm{ch}}$
  for K3, K3 $\times$ E, local $\mathbb{P}^2$, the conifold; verify
  $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ for $N \in \{1, 2, 3, 4, 6\}$
  by direct Borcherds-product expansion; track the four constructions
  in $\{0, 3, 5, 24\}$; check the Mukai-vanishing-bypass lemma
  `lem:mo-bypass-local-to-global` against the actual product-Aut
  decomposition.
- The $(\infty,1)$-categorical lane is what lets you state $\Phi$ as a
  functor on $(\infty,1)$-categories of CY data (when morphism
  preservation is established), invoke Maulik–Okounkov $R$-matrices in
  derived geometry, write the Schiffmann–Vasserot K3 cohomological-Hall
  algebra as a stable $\infty$-category construction, and identify the
  Borcherds–Monster BKM as the image of a fully-extended CY datum.

**Operating rule**: state every theorem in the lane in which its proof
actually works. If chain-level: name the explicit denominator formula,
the explicit Borcherds product, the explicit Hodge-supertrace summand,
the explicit Mukai vanishing input. If $(\infty,1)$-categorical: name
the $(\infty,1)$-functor / cofibre sequence / dualisable object / fully
extended TFT. If both: state both, label which lane each status applies
to (Pattern 236 ambient-qualifier discipline). **Never** write "this
is just the chain-level / $(\infty,1)$-categorical shadow of the real
theorem": both shadows are real, both are the theorem, viewed through
different lenses.

Pattern 273 ($\Phi$ functor vs object-level correspondence) is a
*scope declaration*, not a hierarchy: the chain-level object-level
$\Phi$ and the $(\infty,1)$-categorical $\Phi$-as-functor (when
morphism preservation is proved) are **two different statements** about
two different categorical structures, both load-bearing, both
documented at their precise scope.

## Where the bookkeeping lives

- **`notes/antipatterns_catalogue.md`** — the sole Vol III AP-CY
  catalogue (AP-CY1 through AP-CY49 plus cross-programme AP150--AP164
  and formula-mechanical FM24--FM27). Every `/chriss-ginzburg-rectify`
  and `/investigate` invocation consults this at Gate 0 alongside the
  cache. Append new AP-CYs here. AP-CY vocabulary does not appear in
  any reader-facing `.tex` under `chapters/`, `frame/`, `examples/`,
  `theory/`, `connections/`, `bibliography/`, or `appendices/`.
- **`appendices/first_principles_cache.md`** — confusion-pattern
  registry with AP-CY triggers. Every `/chriss-ginzburg-rectify` and
  `/investigate` consults this alongside the catalogue. Append new
  patterns here with columns Wrong Claim / Ghost Theorem / Precise
  Error / Correct Relationship / Type.
- **`notes/claude_md_legacy_20260418.md`** — full prior CLAUDE.md,
  899 lines, lossless. Historical snapshot; the AP-CY catalogue has
  moved to `notes/antipatterns_catalogue.md`. Still contains the
  detailed theorem status, HZ-3-11 independent verification protocol,
  and the CY-specific cross-volume awareness. Grep by index for
  historical context.
- **`notes/agents_md_legacy_20260418.md`** — full prior AGENTS.md,
  1508 lines.
- **`~/chiral-bar-cobar/CLAUDE.md`** — Vol I manifesto (shared
  five-theorem core).
- **`~/chiral-bar-cobar/chapters/examples/landscape_census.tex`** —
  shared canonical formulas for $\kappa$, $r(z)$, central charges.
- **`~/chiral-bar-cobar-vol2/CLAUDE.md`** — Vol II manifesto
  ($\mathsf{SC}^{\mathrm{ch,top}}$, 3D HT QFT).
- **`chapters/examples/cy_d_kappa_stratification.tex`** — the Vol III
  canonical $\kappa$ table across CY dimensions.
- **`chapters/theory/cy_to_chiral.tex`** — the $\Phi$ functor
  construction.
- **`scripts/hooks/beilinson-gate.sh`** — version-controlled hook;
  install via `cp scripts/hooks/beilinson-gate.sh .claude/hooks/`.

## Git and authorship

All commits by **Raeez Lorgat** only. Never any AI attribution anywhere:
no `Claude`, no `Anthropic`, no `Co-Authored-By`, no `Generated with`,
no 🤖, in commits, comments, docstrings, or manuscripts. Pre-commit
hook nudges; remove offending content.

`git stash` forbidden. Do not amend commits.

## LaTeX

Macros in `main.tex` preamble. Inside chapters, `\providecommand`, not
`\newcommand`. Memoir + EB Garamond.

HZ-7 subscript discipline on $\kappa$ is **reader-facing** disambiguation,
not cognitive load — default to the closest mathematically-correct
subscript; do not spend cycles tuning.

Claim-status tags are temporary bookkeeping, not repairs. When uncertain,
name the exact proof obligation and heal the proof, statement, or
construction; do not downgrade the manuscript to close. CY-C is
conjectural, $G(X)$ is unconstructed in general, Super-Yangian is
conjectural. Honest scope from the start.

## Ambient hooks

- **`PreToolUse(Agent)`** → cache-injection (if locally installed).
- **`PreToolUse(Bash, git commit)`** → no AI attribution reminder.
- **`PostToolUse(Edit|Write)`** → `beilinson-gate.sh` AP + cache sweep.
- **`Stop`** → session-end summary (if locally installed).

## Long-form proof harness

For Claude Code, Codex CLI, and any GPT-5.5 / GPT-5-Codex-class agent,
frontier mathematics runs in maximum-effort mode. Use the deepest
host-exposed model and reasoning budget. If the host offers a
GPT-5.5 Pro / Heavy or `xhigh` setting, use it for theorem repair,
cross-volume synthesis, adversarial review, and primary-source
reconstruction. The private ChatGPT Pro harness is not public; this is
the open local analogue.

Long runs are normal. A 30-60 minute agent run is acceptable when a
proof obligation requires it. The agent first loads the relevant
context (`CLAUDE.md`, `AGENTS.md`, target chapter, dependencies,
bibliography, compute files, cross-volume anchors), builds an internal
outline, then works through independent proof routes: worked example,
formal argument, primary source, computation, and cross-volume
consistency. Private scratch stays private; the deliverable is the
checked proof trace and the exact remaining obstruction.

After every proposed repair, run an attack-heal loop: strongest
counterexample, sign/convention check, ambient-category check, missing
hypothesis, false functoriality, unproved equivalence, numerical
constant. Heal and attack again until the theorem closes or the exact
obstruction is named for the next repair cycle. Do not downgrade the
manuscript to close the loop. Subagents provide evidence, not authority;
the main thread integrates by deep semantic merge.

## Do not

1. Do not block large user-authorized swarms.
   Partition work by disjoint files or mathematical axes, require short
   verifiable reports, and merge by deep semantic review across Vol
   I/II/III.
2. Propagate status-label wording when mathematics is waiting.
3. Invent formulas from memory.
4. Run `make fast` after every edit.
5. Add AI attribution anywhere.
6. `git stash` or amend commits.
7. Read `notes/claude_md_legacy_20260418.md` whole — grep by AP-CY index.
8. Confuse this file with a configuration manual. Mathematician's manifesto.

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
