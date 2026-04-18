# AGENTS.md (Vol III)

## What this repository is for

This repository is an instrument for advancing human mathematical
knowledge. Specifically, for understanding the **CY-to-chiral functor
$\Phi: \mathrm{CY}\text{-cat}_d \to \mathrm{ChirAlg}$**, and the seven
faces of $r_{\mathrm{CY}}$ that crystallise the correspondence between
BPS quantum groups (K3 Yangian, BKM / Borcherds / Monster) and their
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
- $\mathrm{CoHA}(\mathbb{C}^3) = Y^+$ (positive half), NOT $\mathcal{W}_{1+\infty}$.
- Six routes to $G(K3 \times E)$ are six DIFFERENT constructions, NOT six $\Phi$ applications.
- $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$ FAILS at every $N \in \{1,2,3,4,6\}$ (not a coincidence; at $N=1$ LHS = $5$, RHS = $0+0 = 0$). Universal formula: $\kappa_{\mathrm{BKM}} = c_N(0)/2$ (Borcherds 1998; Gritsenko 1999).
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
6. **Do not spawn 30 parallel Codex agents** — serialised + silently
   budget-cut; ~1 deliverable per session window.
7. **HZ-7 discipline**: $\kappa$ always subscripted. HZ-3-11
   Independent Verification Protocol applies to ProvedHere decorators.
8. Claim-status tags default `\ClaimStatusConjectured` when uncertain.
   CY-C is conjectural; $G(X)$ is unconstructed in general;
   Super-Yangian is conjectural.

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
