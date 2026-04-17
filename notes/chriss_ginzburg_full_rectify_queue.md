# Chriss-Ginzburg full-rectify queue (Vol III, 2026-04-17)

Loop directive: run `/chriss-ginzburg-rectify` (skill tool) on every Vol III
chapter EXCEPT abstract, preface, introduction. Then every standalone paper.
Cron: `trig_01EwyA6My2f9sdmBdMYCcMZD` (hourly, claude-opus-4-7, Momentum env,
created 2026-04-17). Dashboard: https://claude.ai/code/scheduled/trig_01EwyA6My2f9sdmBdMYCcMZD

One chapter per tick (the skill is heavy). On each tick: pick first pending
`[ ]` entry, rectify through all 5 phases, mark completed (or `[~]` partial
for files >3000 lines), commit with author "Raeez Lorgat", push to main.

## Vol III chapters (manuscript body, 34 files)

Excluded: `chapters/frame/preface.tex`, `chapters/theory/introduction.tex`
(abstract lives in main.tex frontmatter).

### theory/ (12 files after exclusions)

- [x] `chapters/theory/cy_categories.tex` — 2026-04-17 rectified (Kontsevich HKR K3 example corrected: 1+0+22+0+1=24 split; Mukai row-grading kept as secondary collapse; 2 typos; dangling-verb remark fixed)
- [x] `chapters/theory/cyclic_ainf.tex` — 2026-04-17 CG-rectified (merged two sl_2 examples; K3 HKR → Kontsevich convention; quintic HKR regraded to HH^2=101, HH^3=4 with Λ^r T ≅ Ω^{3-r} stated; Killing form → trace form on defining rep; AP-CY70 metadata scrub (HZ3-2/AP113/AP160/wave-14 tags removed); Drinfeld center as right-adjoint-to-forgetful, not averaging; dangling sentences fixed; 3-agent re-audit: RED+BLUE+GREEN all CONVERGED after fixes. AP5 propagated to derived_categories_cy.tex (quintic HKR grading).)
- [x] `chapters/theory/hochschild_calculus.tex` — 2026-04-17 CG-rectified (opening re-arrangement: org question first; AP-CY70 scrub (AP160/HZ3-2/AP113/"NEVER conflate"/"forbidden"/"%: always subscript" directive); added motivating openers to §1-§5, §7; (2-d)-shifted Poisson bracket degree stated as $d-2$ (PTVV); BV generator formula inlined; CY class convention unified to $\HC^-_d$; SBI triangle reordered to Loday standard; Hodge-dR SS target corrected to $\HC^-_q$; cyclic homology $\otimes_{k[B]} \to \otimes_{k[u]}$; 3d HT/BRST marked heuristic dictionary; $\cC_\Delta$ diagonal bimodule introduced explicitly; closing bridge sentence added. 3-agent re-audit: BLUE CONVERGED, RED+GREEN converged after fixes.)
- [~] `chapters/theory/cy_to_chiral.tex` — 2026-04-17 PARTIAL CG-rectify (5166 lines, central climax chapter). Phase 2 complete: AP-CY70 scrub (empty `\textup{()}`, HZ3-1 / HZ3-11 tags at 7 sites, "adversarial audit" label, "healed framework" → "framework"). Phase 3 chunk 1 only (L1-50 converged, 1 MINOR fix: `\CY_3\text{-}\Cat^{\mathrm{fr}}` parenthetical). Phase 4 RED+BLUE+GREEN all reported NOT CONVERGED with mathematical findings. Fixed: 4 CRITICAL build-blockers (`$\begin{construction/conjecture/theorem}$` literals inside math dollars at L4963/4964/5163/5165 → `\texttt{\textbackslash begin\{...\}}`), 5 healing-language instances ("now in hand"/"now proved"/"now constructed"). **Deferred to targeted future pass**: RED#1 L2782 CoHA = U^ch conflation (AP-CY7); RED#2 L504 Kummer Step 4 Route-3 scope (AP-CY60); RED#3 thm:cy-to-chiral-d3 chain-level status tag overclaim; RED#6 def:critical-coha undefined ref; BLUE#5 def:shadow-tower-recursion Vol I cross-ref; GREEN closing crystallization; AP-CY52 file >3000 lines (split recommended but would fragment CY-A theorem chain). Build gate: skipped (pdflatex unavailable).
- [x] `chapters/theory/m3_b2_saga.tex` — 2026-04-17 CG-rectified (B^(2) arity corrected C_n → C_{n-2}; opening rewritten to lead with core identification; B^(2)_TCFT vs B^(2)_naive discipline established at first statement; AP-CY70 metadata scrubbed (pedagogical-value preface, "new content of this chapter", "this is the content of the saga", "records that shift"); S^3-framing / unit-connected / Goodwillie tower / Čech-HTT / SC-formal / chirally Koszul parenthetical glosses added; thm:single-object-incompatibility proof reordered to eliminate circularity (Step 1: μ_2(a,a)=0 cyclic; Step 2: Stasheff kills mixed; Step 3: μ_2(b,b)=0 degree); Francis-Gaitsgory cited for connective E_1 bounded-below HH; closing crystallization added. 3-agent re-audit: RED 1 CRITICAL (circular proof) fixed, RED arithmetic findings false positive (engine confirms 4,2,6); BLUE 3 HARD FAIL + 4 MEDIUM all fixed; GREEN 4 findings all fixed. Critical build-blocker `\end{remark>` typo fixed. Engine `chain_level_m2_b2_cancellation.py` values (4, 2, 6) re-verified against manuscript. Build gate: pdflatex unavailable; static checks PASS.
- [x] `chapters/theory/quantum_chiral_algebras.tex` — 2026-04-17 CG-rectified (2716-line chapter, Phase 2 AP-CY70 metadata scrub: stripped AP-tag parenthetical citations from prose, remark titles, and table "AP compliance" rows across lines 248, 252, 266, 358, 455, 466, 489–494, 605, 695, 868, 892, 971, 975, 979, 1008, 1265, 1434, 1579, 1634, 1722, 1832, 1852, 1897, 1904, 2010, 2114, 2160, 2219, 2337, 2393, 2446, 2712; replaced "adversarial" reader-facing wording with "consistency tests" / "route comparison" / "lift-rate assessment" / "final-verdict integration" / "consistency vectors"; removed healing-language ("now proved", "now constructed", "Dependency (b) is resolved") at L38/L371; repaired truncated remark title at L1634; "AP compliance" table-row labels replaced by mathematical-content descriptors ("Convention checks", "Conjectural status flag", etc.); begin/end balanced 300/300; zero bare kappa confirmed. Labels `subsec:cfg25-adversarial` / `conj:cfg25-adversarial` and engine filenames retained (non-rendered). Build/test gates: pdflatex + numpy + pytest unavailable in sandbox; structural grep checks PASS. Phase 4/5 single-pass audit; deeper 3-agent re-audit deferred.)
- [ ] `chapters/theory/e1_chiral_algebras.tex`
- [ ] `chapters/theory/e2_chiral_algebras.tex`
- [ ] `chapters/theory/en_factorization.tex`
- [x] `chapters/theory/quantum_groups_foundations.tex` — 2026-04-17 CG-rectified (AP-CY70 scrub: 2 healing-language + 1 AP-tag-in-label leaks removed; §1 motivating opener added; classical r-matrix r=Ω corrected to r+r^{21}=Ω with skew-symmetric decomposition; level-stripped r(z) remark restructured to separate level prefix from κ_ch formula; κ_BKM scope clarified as K3xE-specific; "is forbidden" directive replaced by mathematical statement on invariant distinctness with N=1 coincidence noted; fermionic ribbon twist labeled as heuristic (Costello-Gaiotto); closing bridge to braided_factorization added; ∑h_i=0 clarified as normalization convention; sentence-case typo fixed. 3-agent re-audit: BLUE CONVERGED; RED 3 false-positive HIGH findings (conflating κ with c_Sug, abelian vs non-abelian Yangian Cartan, conductor K=0 with individual values); GREEN 2 HIGH + 2 MED all fixed.)
- [ ] `chapters/theory/braided_factorization.tex`
- [ ] `chapters/theory/drinfeld_center.tex`
- [x] `chapters/theory/modular_trace.tex` — 2026-04-17 CG-rectified (AP-CY70 scrub: 3 healing-language + outdated-CY-A_3-not-constructed comment; CY-D scope restricted to (d=2,h^{1,0}=0) with Serre parity; Φ(D^b(K3))=H_Muk (not N=4 SCA) per AP-CY59; Δ_5 paramodular group via O^+(2,3)≃PGSp_4; opening triple sharpened (χ(O_X) third limb); λ_g parenthetical; closing pivot to Part VI seven faces. 3-agent re-audit: BLUE CONVERGED; RED+GREEN converged after RECTIFICATION-FLAG strip.)

### examples/ (17 files)

- [x] `chapters/examples/derived_categories_cy.tex` — 2026-04-17 CG-rectified (header metadata block stripped (wave-14/AP-CY55/AP184/HMS-Koszul tags); K3 HKR aligned to Kontsevich (1+0+22+0+1=24) per rectified cy_categories; Phi(D^b(K3))=H_Muk clarification (AP-CY75 — N=4 SCA is a separate algebra); "is now proved/constructed" healing language → plain theorem citation; L330 broken sentence "distinguishes..." repaired with subject; L363 truncated "confirming..." completed with \ref{conj:wallcrossing-dictionary}; prop→conj:wallcrossing-dictionary ref-type fixed at 3 sites; platonic_ideal_2026_04_17.md timestamped filename leak stripped at 2 sites; \ref{ch:fukaya-categories}→\ref{ch:fukaya} (BLUE); ch:universal-conductor/thm:koszul-reflection → texttt Vol I cross-volume form; engine cite L235 supplementary-verification stripped (GREEN); χ(O) vs χ_top conflation at L210 corrected per AP-CY34a (χ(O)=0 identically for odd-d CY); closing pivot to Fukaya. 3-agent re-audit: RED 3 HIGH + MED, BLUE 6 issues, GREEN 3 HIGH + MED — all fixed.)
- [ ] `chapters/examples/fukaya_categories.tex`
- [x] `chapters/examples/matrix_factorizations.tex` — 2026-04-17 CG-rectified (AP-CY70 scrub: stripped header metadata comments ("wave-14 anchors", "AP-CY17/AP-CY18" / "FM-LIE-NUMERICS" tags); healing language "is now proved"/"is established" → theorem cite; L183 dangling sentence "in line with." completed; A_1 Virasoro@c=2 vs Ising@c=1/2 conflation corrected (AP-CY79 new); Gepner Hodge indices h^{p,d-p} anti-diagonal (AP-CY80 new); Knörrer stabilization count k=2 uv-pairs not 4 (AP-CY81 new); Cl_4 graded-Morita via complex super-Bott 2-periodicity (AP-CY82 new); \ref{ch:fukaya-categories}→\ref{ch:fukaya} (BLUE broken ref); ch:universal-conductor→\texttt{} cross-volume form (BLUE broken ref); closing pivot to Fukaya chapter added (GREEN). 3-agent re-audit: BLUE 2 broken refs fixed; RED 1 HIGH + 4 MEDIUM all fixed; GREEN 1 MEDIUM + LOW all fixed. 4 new AP-CY entries 79-82 added to CLAUDE.md + cache.)
- [ ] `chapters/examples/quantum_group_reps.tex`
- [ ] `chapters/examples/toric_cy3_coha.tex`
- [ ] `chapters/examples/coha_wall_crossing_platonic.tex`
- [ ] `chapters/examples/k3_chiral_algebra.tex`
- [ ] `chapters/examples/k3_yangian_chapter.tex`
- [ ] `chapters/examples/k3_quantum_toroidal_chapter.tex`
- [ ] `chapters/examples/toroidal_elliptic.tex`
- [ ] `chapters/examples/k3e_bkm_chapter.tex`
- [ ] `chapters/examples/k3e_cy3_programme.tex`
- [ ] `chapters/examples/cy_c_six_routes_convergence.tex`
- [ ] `chapters/examples/cy_c_six_routes_generator_level_platonic.tex`
- [ ] `chapters/examples/cy_c_pentagon_hypothesis_closures_platonic.tex`
- [ ] `chapters/examples/cy_d_kappa_stratification.tex`
- [ ] `chapters/examples/super_riccati_shadow_tower_platonic.tex`

### connections/ (4 files)

- [ ] `chapters/connections/modular_koszul_bridge.tex`
- [ ] `chapters/connections/bar_cobar_bridge.tex`
- [ ] `chapters/connections/cy_holographic_datum_master.tex`
- [ ] `chapters/connections/geometric_langlands.tex`

## Standalone papers (Vol I folder, Vol III topics)

To be enumerated when manuscript body is complete. Candidates:
`cy_to_chiral_functor.tex`, `cy_quantum_groups_6d_hcs.tex`,
`drinfeld_kohno_bridge.tex`, `chiral_chern_weil.tex`, `classification.tex`,
`classification_trichotomy.tex`, and more.

## Completion log

Each entry: `YYYY-MM-DD HH:MM  <file>  commit=<sha>  notes`

- 2026-04-17  `chapters/theory/cy_categories.tex`  commit=uncommitted  CG rectify: fixed
  chain-level grading inconsistency in `ex:hh-k3` — the stated decomposition
  $\HH^0=k^2,\HH^1=k^{20},\HH^2=k^2$ is the Mukai row-grading ($p=q$) but was
  attached to the Kontsevich HKR theorem ($p=q+r$). Rewrote as
  $\HH^0=k$, $\HH^1=0$, $\HH^2=k^{22}$, $\HH^3=0$, $\HH^4=k$ with the row-graded
  collapse `(1+1)+20+(1+1)=2+20+2` kept as a secondary identification.
  Also cleared `H^2(T_X)=k` (false for K3) and fixed 2 `;.` typos +
  one dangling sentence in `rem:cy-cat-drinfeld-center-not-averaging`.
