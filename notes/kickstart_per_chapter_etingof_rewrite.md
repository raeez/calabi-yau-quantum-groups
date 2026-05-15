# Kickstart: per-chapter Etingof rewrite (Vol III platonic reconstitution)

Self-contained kickstart for a fresh `/clear` session. Paste the prompt block below verbatim into the new session after `/clear`. The state in this document is current as of the head commit on `main`; verify with `git log --oneline -1` before starting.

---

## What this is

A per-chapter Etingof-voice rewrite of Vol III (`/Users/raeez/calabi-yau-quantum-groups`), pursued one chapter per iteration, 3–5 specific paragraph rewrites per chapter, with build verification on every iteration. This is the **second phase** of the platonic reconstitution; the first phase (structural reorganisation: Part openers, chapter openers, cross-volume citation cleanup, the headline `cy_to_chiral` formal-locus extraction) has shipped.

The discipline is on `CLAUDE.md`. The Russian-school "Chriss–Ginzburg north star" is binding (`MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md`). Forbidden patterns: meta-narration, rhetorical Q/A, hedging, negative framing, bookkeeping/catalogue IDs in prose.

## Iteration shape (single-chapter, single-iteration)

1. Pick ONE chapter from the priority list (below) that has not yet had a deep per-chapter rewrite.
2. Read it end-to-end if ≤ 2000 lines, or its central section if larger. Skim each section for 3–5 specific paragraphs that fail one of:
   - **(a) define-before-use** — a symbol used before its definition;
   - **(b) inevitability** — a statement that does not land as inevitable in the moment;
   - **(c) elite-voice** — rhetorical buildup, descriptive prose where mathematical statement would do, hedging in a definitional context, **negative-form** scope disclaimers ("does not", "is not", "no", "neither/nor").
3. Rewrite those 3–5 specific paragraphs. **The mathematical content of every scope/type distinction is preserved entirely**; the prose changes from negative-form to positive-form.
4. Run `make fast` (build takes ~2 min; first pass shows large undef counts that resolve in pass 2; converged build is `2534pp, 0 undef citations, 0 undef references`).
5. Commit + push **only if** `make fast` produces 0 distinct undef refs/cites (verify with `grep -cE "(Reference|Citation) .* undefined" out/main.log`).
6. Each iteration MUST end with: (1) before/after diff of specific paragraphs touched, (2) build passes with 0 new undef, (3) one sentence identifying the inevitability / define-before-use / elite-voice violation repaired.

**Discipline (hard rules):**
- NO bulk regex.
- NO global pattern sweeps.
- NO `sed`/`perl` find-replace across many files.
- One chapter, one build cycle, one commit per iteration.
- Always retry on OOM (exit code 137); the second build typically passes.
- Pass 1 of `make fast` always shows large undef counts — verify on pass 2+.

## Chapters already deeply rewritten this session (skip these)

Each was 5 paragraph rewrites with build verification:

1. `chapters/theory/m3_b2_obstruction.tex` — 5 rewrites: Q/A rhetoric, counterfactual hedging, "is a category error", "Costello's theorem does not assert", "Forgetting this distinction"
2. `chapters/theory/cy3_chain_level_bridge.tex` — 5 rewrites: chapter opener (slogan negation), 4 trailing scope disclaimers ("does not construct the Hall comparison", "is not the direct target", etc.)
3. `chapters/examples/k3_yangian_chapter.tex` — 5 rewrites: opening prose envelope distinction, BKM nomenclature scope, Schiffmann–Vasserot scope, Hall–Drinfeld scope, Frenkel–Kac section opener
4. `chapters/examples/k3_chiral_algebra.tex` — 5 rewrites: bullet item κ_BKM scope, Drinfeld Yangian scope, CoHA evaluation chain, chiral de Rham parenthetical, Hall recognition gate
5. `chapters/theory/e1_chiral_algebras.tex` — 5 rewrites: chapter opener "too coarse", averaging map "lossy", Drinfeld Yangian scope, Swiss-cheese two-coloured operad, av-lossy proposition trailer
6. `chapters/theory/en_factorization.tex` — 5 rewrites: Bott periodicity prose, subsec opener "is not automatic", `rem:en-factorization-stage1-target`, prop weiss-refinement-upgrade, proof of prop dunn-lurie-sp (iv)
7. `chapters/theory/quantum_chiral_algebras.tex` — 5 rewrites: thm hcs-obs E3 CE Dolbeault, def qca-dimension-stratified item (ii), def qca-five-objects (B(A)), rem qvcg-construction-locus, prop qca-finite-rees-layer-separation (v)
8. `chapters/theory/introduction.tex` — 5 rewrites: chapter opener "does not carry a single numerical shadow", five-numbers paragraph, K–S CY datum setup ("no global NCCR is assumed"), Stage 2 theorem, six routes paragraph
9. `chapters/frame/preface.tex` — 5 rewrites: five-numbers / layer-separation paragraph, cusp form Δ_5 description, positive-geometry grammar opener, CoHA evaluation chain, five-numbers signature
10. `chapters/connections/cy_holographic_datum_master.tex` — 5 rewrites: `rem:cy-seven-face-tier-iii-siblings` opener, `rem:cy-seven-face-three-tier-opener` opener, `rem:cy-kappa-bkm-two-scopes-opener` GC catalogue, `rem:face1-two-bars` trailer, `rem:no-cobar-bulk-confusion` title + body
11. `chapters/examples/k3_chiral_bialgebra_platonic.tex` — 5 rewrites: chapter intro $E_2$ braiding, sec:k3-structural-genesis opener, proof sketch compact source, `rem:k3-gelfand-universal-property`, `rem:k3-non-yangian-adjoint` title + body
12. `chapters/theory/hochschild_calculus.tex` — 5 rewrites: sec:cy-hh-duality opener, three-dimensions remark (c), sec:categorical-hodge opener, sec:kt-formality-atiyah-cocycles opener, thm:kt-formality-d3 trailer
13. `chapters/examples/k3e_bkm_chapter.tex` — 5 rewrites: `rem:k3e-four-corner-scope` triple negation, prop:k3e-four-corner-comparison-maps (ii) and (iii), proof Yangian trailer, prop:k3e-finite-dwr-ran-positive-half-surface triple negation
14. `chapters/theory/cy_to_chiral.tex` (Künneth section, lines ~3500–3700) — 5 rewrites: `rem:phi-subscript-discipline` subscript framing + ill-typed expression, V1 Warning quotient, V4 sextic non-product, `rem:phi-4-sextic-vs-quintic`
15. `chapters/theory/cy_to_chiral.tex` (5D-hCS section, lines ~1810–1888) — 5 rewrites: `rem:costello-yagi-vs-cgy-distinction` citation discipline, `prop:super-all-orders-open` obstruction location, `rem:li-yamazaki-synthesis-vs-gaiotto-rapcak` attribution, `conj:g-delta5-is-sp-k3-general-extension` separate primitives, `rem:four-kappa-stage-assignment` Borcherds-weight identity
16. `chapters/theory/quantum_chiral_algebras.tex` (hcs-vs-sigma + three-dualities, lines ~2073–2188) — 5 rewrites: `subsec:hcs-vs-sigma-adversarial` opener, item (iv) Yangian, "all four contradictions" prose, `rem:hcs-sigma-conflations` title + body, `rem:three-dualities-k3`
17. `chapters/theory/cy_to_chiral.tex` (derived-rigour + Morse-Bott section, lines ~827–1250) — 5 rewrites: `subsec:phi-d-derived-rigour` opener ("is ambiguous unless"), `prop:phi3-arbitrary-morphism-obstruction-criterion` closing paragraph ("does not define the map"), same proposition's proof closing ("Without these choices there is no defined composite"), `cor:cya3-finite-witness-package` body ("is not an unproved consequence"), `sec:morphism-functoriality-phi-fa-3` opener (rhetorical Q/A "The question is... The answer is...")

Total: 17 iterations · 85 paragraph rewrites · all builds clean. Chapters 7 and 14 each had two iterations on different sections; cy_to_chiral.tex has had three iterations on different sections (Künneth, 5D-hCS, derived-rigour + Morse-Bott).

## Priority list for remaining iterations

In order:

(i) `chapters/theory/cy_to_chiral.tex` — sections **beyond** the Künneth section already touched. The file is ~13K lines, the central construction; pick another tractable section.
(ii) `chapters/examples/k3e_bkm_chapter.tex` — sections **beyond** the four-corner block already touched. The file is 15K lines.
(iii) `chapters/examples/k3_yangian_chapter.tex` — sections **beyond** the openers/scope remarks already touched.
(iv) `chapters/examples/k3_chiral_algebra.tex` — sections beyond first wave.
(v) `chapters/theory/quantum_chiral_algebras.tex` — sections beyond first wave.
(vi) `chapters/theory/hochschild_calculus.tex` — sections beyond first wave.
(vii) `chapters/theory/e1_chiral_algebras.tex` — sections beyond first wave.
(viii) `chapters/theory/e2_chiral_algebras.tex` — already substantively in elite voice; light pass only.
(ix) `chapters/connections/cy_holographic_datum_master.tex` — face 1–7 **bodies** (only first-wave remarks touched).
(x) `chapters/examples/k3_chiral_bialgebra_platonic.tex` — sections beyond first wave.
(xi) `chapters/examples/cy_d_kappa_stratification.tex` — canonical κ table chapter; large.
(xii) Any other chapter under `chapters/` showing forbidden patterns.

## Defect patterns to look for (catalogue from this session)

Each of these recurred multiple times; learn the shape, then sweep:

**1. Drinfeld Yangian negation.** "is not a Drinfeld Yangian: no Kac–Moody Cartan / no J-presentation / no Weyl action on imaginary simple roots". Repair: positive BKM-Hopf-superalgebra identification with Manin pair, imaginary simple roots, Borcherds denominator, in place of strict Yangian Cartan/J-presentation.

**2. "Not on $A$ itself" trailing.** "The $E_2$ braiding lives on $\cZ(\Rep^{E_1}(A))$, not on $A$ itself." Repair: "The $E_2$ braiding lives at the next level of the universal arrow on $\cZ(\Rep^{E_1}(A))$ ≃ $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$." Name where it LIVES.

**3. "Lossy" / "forgets" averaging map.** Repair: name the kernel explicitly and identify which bar carries which data ($B^{\mathrm{ord}}$ retains the $R$-matrix; $B^\Sigma$ projects onto its $S_n$-invariant scalar trace).

**4. Triple-negative scope disclaimers.** "does not identify ..., does not prove ..., and does not by themselves glue ...". Repair: positive enumeration of where each further construction lives — "the further constructions $X$, $Y$, $Z$ are the separate primitives of Theorem $T$ and Problem $P$".

**5. Section openers framed by rhetoric.** "The question is whether ...", "The passage from $X$ to $Y$ is not automatic", "Without $X$, $Y$ is only a target tuple". Repair: direct statement of what the section constructs ("On a smooth CY category, the Serre functor pairs Hochschild homology and cohomology: ..." rather than "Hochschild homology and cohomology of a general dg category are not paired").

**6. Negative-form bullet points.** "(K1) The unframed symbol $\PhiFA_3$ is not the direct target of a finite-rank hCS comparison." Repair: positive identification of the direct target.

**7. "Wrong question" / "failure is not an accident" framing.** Repair: name the layer separation positively ("each of the five numbers belongs to a distinct construction layer; the formula crosses layers; the universal identity on a single layer is $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$").

**8. "Warning:" prose.** Repair: just state the distinction positively. The warning is bookkeeping.

**9. "is *not* a single context-free map" / "is *ill-typed*".** Repair: name the type discipline positively ("the CY-to-chiral functor on a product $X_1 \times X_2$ is $\Phi_{d_1+d_2}$, with subscript equal to the total complex dimension").

**10. "Bar-cobar inversion is not the seven-face master move".** Repair: distinct-construction title and body naming what each construction IS, both on the boundary, with the bulk Drinfeld centre at the next level.

## CoHA evaluation chain (one-line invariant)

When repairing CoHA / $W_{1+\infty}$ scope, always write out the three-arrow chain explicitly:

> $\CoHA(\mathbb{C}^3) = Y^+(\widehat{\mathfrak{gl}}_1) \hookrightarrow Y(\widehat{\mathfrak{gl}}_1) \xrightarrow{\mathrm{ev}_\lambda} \mathrm{End}(\mathcal{W}_{1+\infty}[\lambda]\text{-vac})$

Three algebraic objects on three arrows; positive-half / Drinfeld double / Fock evaluation image; never "the full $\mathcal{W}_{1+\infty}$ algebra, not the CoHA itself".

## Four $\kappa$-subscript discipline (one-line reminder)

Always subscripted:
- $\kappa_{\mathrm{ch}}^{\mathrm{Hodge}}(X) = \sum_q (-1)^q h^{0,q}(X)$ — compact Hodge supertrace.
- $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}$ — Heisenberg–Mukai chiral pairing (rank-additive).
- $\kappa_{\mathrm{cat}} = \chi(\cO_X)$ — categorical Euler. Künneth-multiplicative.
- $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ — universal Borcherds-weight identity. Subscripted by input denominator.
- $\kappa_{\mathrm{fiber}}$ — fibre / lattice rank correction.

The $K3 \times E$ spectrum $\{0, 0, 3, 5, 24\}$ comes from five distinct constructions; bare $\kappa$ on a product CY is HZ-7 violation.

## Build verification

```bash
cd ~/calabi-yau-quantum-groups && make fast 2>&1 | tail -8
```

A clean build looks like:

```
── Pass 1 / 4 ──
   2490pp, 259 undef citations, 6770 undef references, 1 rerun requests, ...
── Pass 2 / 4 ──
   2534pp, 0 undef citations, 0 undef references, 1 rerun requests, ...
── Pass 3 / 4 ──
   2534pp, 0 undef citations, 0 undef references, 0 rerun requests, ...
✓ Converged after 3 passes.
```

If pass 2 (or later) shows 0 undef refs and 0 undef cites, the build is clean. Pass 1 always shows large undef counts. OOM failures (exit 137) are transient; just retry.

## What does NOT count as progress

- Bare $\kappa \to \kappa_{\mathrm{ch}}^{\mathrm{Hodge}}$ subscript fixes alone.
- Status rows.
- Phantom-label audits.
- Scope propagation across ten files.
- FRONTIER retractions.
- AGENTS.md / CLAUDE.md harmonisation.
- Bulk regex sweeps.
- Cross-file find-replace.

The PostToolUse hook catches the first six. Only per-paragraph Etingof rewrites with build verification count.

## What counts as progress

- 3–5 specific paragraph rewrites in a single chapter per iteration, each preserving mathematical content while moving prose from negative-form to positive-form.
- Build passes with 0 new undef refs/cites.
- Commit message names each defect with before/after context.
- Commit pushes to `origin/main`.

---

## Kickstart prompt (paste into fresh /clear session)

```
Per-chapter Etingof rewrite of Vol III, single-chapter / single-iteration discipline.

Read /Users/raeez/calabi-yau-quantum-groups/notes/kickstart_per_chapter_etingof_rewrite.md for the full discipline, defect patterns, completed chapters, and priority list.

Then:
1. Run `git log --oneline -3` to see the head of `main`.
2. Pick ONE chapter from the priority list in the kickstart document that has not yet had a deep per-chapter rewrite (the 14 already-rewritten chapters are listed there — skip them).
3. Read the chapter end-to-end (or its central section if > 2000 lines).
4. Identify 3–5 specific paragraphs that fail elite-voice / define-before-use / inevitability tests.
5. Rewrite those specific paragraphs in positive form, preserving all mathematical content (scope distinctions, type discipline, level identifications).
6. Build with `cd ~/calabi-yau-quantum-groups && make fast 2>&1 | tail -8` (background it if you have other work; retry on exit code 137 / OOM).
7. Verify the build by checking Pass 2 or later shows `0 undef citations, 0 undef references`.
8. Commit with a message naming each defect with before/after context.
9. Push to `origin/main`.
10. Repeat for the next chapter on the priority list.

Hard discipline:
- NO bulk regex.
- NO global pattern sweeps.
- NO sed/perl find-replace across many files.
- One chapter, one build cycle, one commit per iteration.
- Preserve all mathematical content; only rewrite the prose framing.

If you encounter a defect pattern not in the kickstart document's catalogue, add it to the document under "Defect patterns to look for" when you commit.
```

---

## Memory pointer

When this kickstart fires in a fresh session, also load:
- `~/calabi-yau-quantum-groups/CLAUDE.md` (Vol III manifesto)
- `~/calabi-yau-quantum-groups/MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md` (writing standards)
- `/Users/raeez/.claude/projects/-Users-raeez-calabi-yau-quantum-groups/memory/MEMORY.md` (auto-memory)

The CLAUDE.md inherits `~/ecosystem/INVARIANTS.md` (destructive-git list, multi-agent worktree concurrency, etc.) — do not paraphrase that file; read it once per session.
