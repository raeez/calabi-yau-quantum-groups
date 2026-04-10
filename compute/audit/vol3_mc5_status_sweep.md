# Vol III MC5 Status Sweep

## Canonical truth (Vol I `chapters/connections/editorial_constitution.tex:179`)

MC5 is not fully proved. What IS proved at all genera is the analytic HS-sewing package. The remaining genuswise BV/BRST/bar identification is still conjectural; at genus 0 the algebraic BRST/bar comparison is proved; tree-level amplitude pairing is conditional on `cor:string-amplitude-genus0`.

## Scope of sweep

Vol III only (`/Users/raeez/calabi-yau-quantum-groups`). Vol I and Vol II untouched by this agent.

## Summary

Vol III contains NO "MC5 PROVED" assertion anywhere. Every MC5 mention is a forward reference into Vol I for the sewing-mechanism content (analytic HS-sewing lane), which IS the proved lane per canonical truth. No Vol III theorem, proposition, remark, or status table claims MC5 as a whole is proved. The Vol III frontier line at `working_notes.tex:3328-3330` was already in canonical form prior to this sweep:

> "The modular Koszul duality engine is now proved (Theorems A--D+H, MC1 through MC4, the analytic HS-sewing lane of MC5, and the 12-fold Koszulness characterization; the genuswise BV/BRST/bar identification of MC5 remains conjectural)."

The sweep added the explicit qualifier "MC5 analytic HS-sewing lane" (or equivalent) at every Vol III citation site where a bare "(Vol I, MC5)" reference could be misread as citing MC5 as a whole. Two sites were already explicitly scoped to "analytic completion programme" and needed no edit.

## Files touched (6 edits across 4 files)

1. `/Users/raeez/calabi-yau-quantum-groups/working_notes.tex`
   - Line 2253: "sewing envelope A^sew (MC5)" to "sewing envelope A^sew (MC5 analytic HS-sewing lane)"
   - Line 2630: "Sewing parameter space (Vol I, MC5)" to "Sewing parameter space (Vol I, MC5 analytic HS-sewing lane)"
   - Line 2641: "sewing mechanism of MC5" to "analytic HS-sewing lane of MC5 (the proved lane of Vol I; the genuswise BV/BRST/bar identification of MC5 remains conjectural)"

2. `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex`
   - Line 319: "sewing envelope of Volume I, MC5" to "sewing envelope of Volume I, MC5 analytic HS-sewing lane"

3. `/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex`
   - Line 196: "Sewing parameter (Vol I, MC5)" to "Sewing parameter (Vol I, MC5 analytic HS-sewing lane)"

4. `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex`
   - Line 526: "E_1 sewing rules (Vol I, MC5)" to "E_1 sewing rules (Vol I, MC5 analytic HS-sewing lane)"

## Files NOT touched (already scoped correctly)

1. `working_notes.tex:3328-3330` - already in full canonical form with genuswise BV/BRST/bar caveat.
2. `chapters/theory/introduction.tex:120` - already "the analytic completion programme of Volume I (MC5, section analytic-sewing)".
3. `chapters/theory/cy_to_chiral.tex:303` - already "the analytic completion programme (MC5, section analytic-sewing of Vol I)".

## Preservations verified

- Wave 13-1 FIX 2 (H_2 parametrization) and FIX 3 (HC^-_d) in Vol III preface: untouched (lines 37-38, 43-45 of preface unchanged).
- Wave 15-3 three-volume thesis interweaving: untouched (preface lines 266-279, e1_chiral_algebras remark `rem:three-volume-thesis` unchanged).
- AP113 compliance: all edits are outside kappa formulas; no bare kappa introduced. Existing kappa_ch, kappa_BKM, kappa_cat, kappa_fiber subscripts unchanged.
- Vol III lambda-bracket convention: no formulas altered.
- No em dashes introduced. No AI slop. No passive voice hedging.

## Pre-existing hook warnings (out of scope)

Hook flagged AP24 (bare kappa+kappa'=0), AP25/AP34 (bar-cobar), AP113 (bare kappa), AP7/AP32 (scope), AP14 (Koszulness), AP106 (narration block), V2-AP26 (hardcoded Part numbers) at lines NOT touched by this sweep (working_notes.tex lines 179, 213, 274, 798, 1167, 1785, 1878, 2399, 2494, 2522, 3492, 3527; cy_to_chiral.tex lines 202, 596, 1039, 1261; preface.tex lines 196 context, 284-291; fukaya_categories.tex lines 196, 558). These are pre-existing content violations unrelated to MC5 status and outside task scope.

## Verification grep

```
grep -rn "MC5\|MC\.5" /Users/raeez/calabi-yau-quantum-groups --include="*.tex"
```

Output (post-sweep, all 9 Vol III citations):

- `chapters/examples/fukaya_categories.tex:319`: "MC5 analytic HS-sewing lane"
- `working_notes.tex:2253`: "(MC5 analytic HS-sewing lane)"
- `working_notes.tex:2630`: "(Vol I, MC5 analytic HS-sewing lane)"
- `working_notes.tex:2641`: "analytic HS-sewing lane of MC5 (the proved lane of Vol I; the genuswise BV/BRST/bar identification of MC5 remains conjectural)"
- `working_notes.tex:3328`: "the analytic HS-sewing lane of MC5" (pre-existing canonical)
- `working_notes.tex:3330`: "of MC5 remains conjectural" (pre-existing canonical)
- `chapters/theory/introduction.tex:120`: "the analytic completion programme of Volume I (MC5, section analytic-sewing)" (pre-existing canonical)
- `chapters/theory/cy_to_chiral.tex:303`: "the analytic completion programme (MC5, section analytic-sewing of Vol I)" (pre-existing canonical)
- `chapters/theory/cy_to_chiral.tex:526`: "E_1 sewing rules (Vol I, MC5 analytic HS-sewing lane)"
- `chapters/frame/preface.tex:196`: "(Vol I, MC5 analytic HS-sewing lane)"

Every Vol III MC5 citation is now either explicitly scoped to the analytic HS-sewing lane, explicitly scoped to the analytic completion programme, or carries the full canonical caveat about the conjectural genuswise BV/BRST/bar identification. No Vol III location claims MC5 proved as a whole.
