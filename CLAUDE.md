# CLAUDE.md (Vol III)

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
$\{2, 3, 5, 24\}$ from four **distinct constructions** (Mukai lattice,
Igusa $\Phi_{10}$ via Gritsenko $\Delta_5$, BKM Borcherds weight, K3
fibre-rank). Six routes to $G(K3 \times E)$ exist; they are six
DIFFERENT constructions, NOT six $\Phi$ applications.

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
C derived-centre complementarity, D obstruction-tower universality,
H Hochschild concentration.

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
- A falsified claim: demonstrating an asserted identity fails at a
  specific parameter point (e.g., an advertised $\Phi$-identification
  broken at a concrete K3 automorphism).
- A sharpened scope: narrowest hypothesis on which a proof actually
  holds.
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
- K3 $\times$ E spectrum $\{2, 3, 5, 24\}$ (four distinct constructions).
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
  in $\{2, 3, 5, 24\}$; check the Mukai-vanishing-bypass lemma
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

- **`notes/claude_md_legacy_20260418.md`** — full prior CLAUDE.md,
  899 lines, lossless. Contains the Vol III AP-CY catalogue (AP-CY1
  through AP-CY67), detailed theorem status, HZ-3-11 independent
  verification protocol, and the CY-specific cross-volume awareness.
  Grep by index.
- **`notes/agents_md_legacy_20260418.md`** — full prior AGENTS.md,
  1508 lines.
- **`notes/first_principles_cache_comprehensive.md`** (if present) —
  confusion-pattern registry with AP-CY triggers.
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

Claim-status tags default `\ClaimStatusConjectured` when uncertain —
CY-C is conjectural, $G(X)$ is unconstructed in general, Super-Yangian
is conjectural. Honest scope from the start.

## Ambient hooks

- **`PreToolUse(Agent)`** → cache-injection (if locally installed).
- **`PreToolUse(Bash, git commit)`** → no AI attribution reminder.
- **`PostToolUse(Edit|Write)`** → `beilinson-gate.sh` AP + cache sweep.
- **`Stop`** → session-end summary (if locally installed).

## Do not

1. Spawn 30 parallel Codex agents for an audit.
2. Propagate status-label wording when mathematics is waiting.
3. Invent formulas from memory.
4. Run `make fast` after every edit.
5. Add AI attribution anywhere.
6. `git stash` or amend commits.
7. Read `notes/claude_md_legacy_20260418.md` whole — grep by AP-CY index.
8. Confuse this file with a configuration manual. Mathematician's manifesto.
