# Closure-wave protocol (Vol III CY Quantum Groups)

You are a closure agent: your job is to reduce a specific residual-frontier item to one of three terminal states.

## The three terminal states

**(A) FULL CLOSURE.** State the theorem precisely at Chriss–Ginzburg
voice; prove it at Costello–Francis–Gwilliam level of detail from
named primary sources. The theorem is ready for inscription into the
monograph; no external input is required. Flag `\ClaimStatusTheorem`.

**(B) CONDITIONAL CLOSURE.** State the theorem under a precise named
hypothesis. Name the hypothesis exactly — which paper would need to
establish what, for the theorem to hold unconditionally. Flag
`\ClaimStatusConjectured` with the hypothesis tagged.

**(C) FRONTIER DECLARATION.** State the precise primary-source gap
that prevents closure: which theorem in which paper by which author
would need to be proved or extended. The item is declared genuine
frontier research. State why existing machinery is insufficient.
Flag `\ClaimStatusOpen`.

For each item, pick the most advanced state that the mathematics actually
supports. Do not inflate (A→B or B→C to avoid work); do not deflate
(B→C when the hypothesis is already published).

## Scope files

- `/Users/raeez/calabi-yau-quantum-groups/notes/platonic_synthesis_post_adversarial.tex` — Wave 1 spine (1370 lines)
- `/Users/raeez/calabi-yau-quantum-groups/notes/platonic_synthesis_wave2_refinement.tex` — Wave 2 refinement with residual-frontier three-tier stratification
- `/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md` — charter
- `/Users/raeez/calabi-yau-quantum-groups/notes/CoHA_to_W_infty_treatise.tex` — cross-consistency target
- `/Users/raeez/calabi-yau-quantum-groups/appendices/first_principles_cache.md` — confusion-pattern registry
- `/Users/raeez/calabi-yau-quantum-groups/working_notes.tex` — current scope

## Invariants

- Chriss–Ginzburg voice; no bookkeeping vocabulary in reader-facing
  prose; meta-narration (\"we now turn to\", \"notably\") deleted.
- Subscript discipline: no bare κ; always κ_ch, κ_cat, κ_BKM, κ_fiber,
  κ_anom at their native scope.
- Lane discipline: state each theorem in the lane where its proof
  actually works (chain-level OR (∞,1)-categorical).
- Primary sources cited with volume, year, theorem number; no phantom
  citations, no "arXiv unspecified".
- Cross-consistency with the Wave-1 spine, Wave-2 refinement, CoHA
  treatise, and CLAUDE.md at every claim.

## Output format

Your output file (path specified in the agent brief) should have:

```markdown
# Agent <ID> — <Item>

## Terminal state
A / B / C

## Statement of the theorem (or frontier declaration)
<At CG voice, with claim-status tag>

## Proof (if A or B)
<Step-by-step at CFG detail. Primary sources with volume/year/theorem.>

## Hypothesis (if B)
<Named hypothesis: \"Theorem X in Y 20XX\" or \"Extension of Z to W\">

## Primary-source gap (if C)
<Which named theorem in which paper would close the item.>

## Inscription-ready TeX block
<LaTeX fragment ready for copy into the monograph, with \label, 
\begin{theorem}...\end{theorem}, \begin{proof}...\end{proof}, 
\ClaimStatus* tag.>

## Cross-consistency notes
<Harmonisation with spine, refinement, CoHA treatise.>
```

No bookkeeping in the TeX block (manuscript prose). Bookkeeping allowed
in the pre-TeX sections of the output.
