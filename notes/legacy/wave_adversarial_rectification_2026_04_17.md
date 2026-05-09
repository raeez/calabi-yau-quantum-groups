# DEEP ADVERSARIAL BEILINSON RECTIFICATION — Vol III 12-Item Rewrite Map

**Author**: Raeez Lorgat (read-only adversarial swarm review). **Date**: 2026-04-17.
**Mode**: maximally hostile review of underlying mathematics + proposed reorganization.
**Anchor files**:
- `/Users/raeez/calabi-yau-quantum-groups/notes/vol3_rearchitecture_proposal.tex`
- `/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/MASTER_PUNCH_LIST.md`
- `/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md`

---

## EXECUTIVE SUMMARY

The 12-item map survives but with sharp scope restrictions on 6 of 12 items.
Three items (1, 4, 11) are NARRATIVE re-packaging dressed as structural
unification and need re-stating as SHARP mathematical theorems with explicit
scope. Two items (3, 8) embed CONJECTURES disguised as theorems and must be
downgraded or restricted. One item (12 — the Conventions appendix) is the
highest-leverage and currently last-listed; it should be FIRST. Two items
(9, 10) are essentially redundant and should be merged. The 12-item map
should be re-ordered by leverage-per-hour into a 13-item map (item 11 splits)
with item 12 at position 1.

Effort estimates uniformly INFLATED by ~60%: actual total is 8-10 weeks, not
36 weeks. Six missing items (M1–M6) recovered from the wave-note catalogue.

---

## PER-ITEM ATTACK

### ITEM 1 — K3 Yangian eigenvalue trichotomy
**File**: `chapters/examples/k3_yangian_chapter.tex` (~6400 lines)

**Proposed unification**: $T_E = \mathrm{id} - \sigma_{\text{tot}}^*$ has spectrum
$\{0,0,2,2\}$; case-(1)/(2)/(3) Künneth = $\lambda \in \{1,2,0\}$.

**(a) Genuineness**: NOT a unification. Inspection of L3848-3863 shows the
existing material already states the trichotomy: case (1) both generic
$\Delta = 0$; case (2) both anti-symmetric $\Delta = 0$; case (3) asymmetric
$\Delta = \sigma_{\text{tot}}^*(M_{\text{generic}})$. Recasting as
"eigenvalues $\{0,0,2,2\}$ of $T_E$" is a Fourier transform — different
basis, same data. NO new theorem.

**(b) Inevitability**: Current statement at L3713-3771
(`thm:universal-drinfeld-coupling-all-Y`) IS Chriss-Ginzburg-style. Replacing
with eigenvalue language would be ANACHRONISTIC.

**(c) Counter-example**: For $Y = \mathrm{LP}^2_{\mathrm{loc}}$ ($\hat{M} =
(1, 7, -5, 1)$), three of four $V_4$-characters fire — neither "generic" nor
"anti-symmetric." The eigenvalue trichotomy has no slot. Likewise $K3^{[n]}$
($\hat{M} = (n+1, n+1, n+1, n+1)$, single-character) breaks the binary
classification. SHARPER: the four-phenotype $V_4$-character classification
already in `rem:v4-character-classification-cy-directions` (L3931-3961).

**SHARPENED restatement**: Promote the existing four-phenotype $V_4$-character
classification (single-character / anti-pair / par-pair / three-character) to
a NAMED THEOREM (`thm:v4-cy-direction-classification`) with closure under
Künneth. Trichotomy survives ONLY as a corollary on $\sigma_{\text{tot}}^*$-
eigenspace cases.

**Effort**: 1-2 days (rewrite of ~200 lines, no new mathematics).

---

### ITEM 2 — CY-D even/odd-d dichotomy
**File**: `chapters/examples/cy_d_kappa_stratification.tex` (~1207 lines)

**Proposed unification**: even/odd-d as the organizing principle.

**(a) Genuineness**: PARTIALLY genuine but PRESENTLY HIDDEN. The dichotomy is
stated as remark (`rem:why-only-k3` L213-234), not as a theorem. The dichotomy
IS structural: at odd $d$, Serre pairwise cancellation forces $\Xi(X) = 0$.
At even $d$, the middle term $h^{0, d/2}$ survives.

**(b) Inevitability**: Current `thm:kappa-stratification-by-d` does case-by-case
analysis without naming the dichotomy. Inevitability would force a single
statement covering all $d$ at once.

**(c) Counter-example**: Holomorphic-symplectic 4-folds ($\mathrm{K3}^{[2]}$,
$F(Y)$) have $h^{0,2} = 1$ from holomorphic-symplectic form, so $\Xi = 3$
from the column $(1, 0, 1, 0, 1)$ — DEVIATES from "$\Xi = 2$ at strict CY of
even $d$." Tri-stratum needed.

**SHARPENED restatement**: ONE theorem with THREE strata:
- (i) odd $d$ → $\Xi = 0$ by Serre.
- (ii) even $d$, strict CY → $\Xi = 2$.
- (iii) even $d$, holomorphic-symplectic → $\Xi = h^{0, d/2}(X) + 2$.

**Effort**: 2-3 days. NOT 2-3 weeks.

---

### ITEM 3 — CY-B at d=3, A_BVDB strict formality refutation, curved formality with Y_3
**File**: `chapters/theory/e2_chiral_algebras.tex` (~2040 lines)

**(a) Genuineness**: REFUTATION half is GENUINE — $A_{\mathrm{BVDB}}$ on $X_5$
is NOT formal as $(-3)$-CY DG algebra ($m_3 = Y_3 \neq 0$ by Sheridan HMS).
REPLACEMENT half is CONJECTURAL — "curved formality with Yukawa as BCOV
datum" is a PROGRAMME, not a theorem.

**(b) Inevitability**: Refutation IS inevitable (Yukawa is topological
invariant of Kähler cone). Replacement is NOT — narrative proposal, not
constructed object.

**(c) Counter-example**: NO compact strict CY$_3$ admits continuous torus
action (Bogomolov-Tian-Todorov + Beauville-Bogomolov). Calaque-Halbout-Felder
ruled out for compact case UNIVERSALLY. Costello-Li framework operates on
LOCAL/toric side. Compact-curved-formality has no constructed example.

**SHARPENED restatement**: SPLIT into TWO items:
- 3a. THEOREM: $A_{\mathrm{BVDB}}$ on compact CY$_3$ NOT formal, with Yukawa
  obstruction class. Effort 1-2 days.
- 3b. CONJECTURE: curved-formality REPLACEMENT with Yukawa as curving datum.
  Existence of curved Koszul pair is OPEN. Effort 2-3 days.

---

### ITEM 4 — CY-C six-routes, LP² β=0 + quintic α=0 integration
**File**: `chapters/examples/cy_c_six_routes_convergence.tex` (~1420 lines)

**(a) Genuineness**: GENUINE for LP² (verified at $p = 7$ via Skoruppa-Zagier
+ 64 tests passing). CONDITIONAL for quintic (depends on (a) chain-level
CY-A$_3$, (b) Costello-Li factorisation, (c) Yamaguchi-Yau finiteness,
(d) Borcherds-lift convergence).

**(b) Inevitability**: LP² half genuinely first-principles. Quintic half has
correct falsifier-arithmetic but conjectural arrow.

**(c) Counter-example**: Integration must NOT silently treat $\alpha = 0$ as
proved. The "six-routes commute via $\alpha_\bigcirc = \mathrm{id}$" proof
at L184 of `cy_c_six_routes_convergence.tex` is CIRCULAR.

**SHARPENED restatement**: ONE proposition `prop:class-B-falsifier-arithmetic`
with TWO sub-claims with ASYMMETRIC status:
- (i) LP² $\beta = 0$ PROVED via $T_7$ + SZ kernel + 64 tests.
- (ii) quintic $\alpha = 0$ CONJECTURAL with FALSIFIABLE Hecke predictor at
  primes $\{3, 7, 13, 29, 37\}$.

**Effort**: 3-4 days. NOT 2-3 weeks.

---

### ITEM 5 — CLAUDE.md roadmap with seven-part rearchitecture

**(a) Genuineness**: STRUCTURAL not mathematical. The seven-part proposal
(`vol3_rearchitecture_proposal.tex`, 830 lines) is coherent: I Foundations /
II CY-to-Chiral Functor / III $E_n$ Hierarchy / IV K3 Yangian / V CY Landscape
/ VI Seven Faces / VII Frontiers.

**(b) Inevitability**: With CY-A$_3$ now PROVED, K3 Yangian deserves a
dedicated PART. Reorganization is structurally sound.

**(c) Counter-example**: Part IV "K3 Yangian" overclaims — only ABELIAN Yangian
is proved; nonabelian is FRONTIER. Title should be "K3 Abelian Yangian"; move
nonabelian content to Part VII. Avoid HZ3-1/AP-CY14 risk.

**SHARPENED restatement**: Adopt seven-part with title corrections.
- Part IV title: "K3 Abelian Yangian" (not "K3 Yangian").
- Move nonabelian content to Part VII.
- Chapter 7 absorbs cy_d_kappa_stratification (item 2).
- Chapter 18 is item 4.
- Chapter 30 requires ZTE T matrix (computed, 35 tests).

**Effort**: 1 day for CLAUDE.md update; 4 weeks for full chapter-file reshuffle
(8 phases per L789-828). Reshuffle DEPENDS on items 1-4 being mathematically
settled FIRST.

---

### ITEM 6 — Vol I five-theorem index, promote Koszul Reflection Theorem

**(a) Genuineness**: GENUINE if Trinity Theorem is proved. Master Punch List V5
lists 4 obstructions $\Pi_1$-$\Pi_4$ as CONJECTURES. Koszul Reflection PROVED
in subcategory $\mathrm{Kosz}(X)$ subject to (H1)-(H3).

**(b) Inevitability**: Slogan "the chiral bar is its own Koszul dual" IS
Russian-school memorable.

**(c) Counter-example**: At higher genus and $d \geq 2$, bar-cobar adjunction
fails to be equivalence. Promotion must NOT silently extend beyond (H1)-(H3).

**SHARPENED restatement**: Promote with EXPLICIT scope restriction; name
$\Pi_1$-$\Pi_4$ as obstruction conjectures.

**Effort**: 2-3 days.

---

### ITEM 7 — Vol I κ-conductor universal formula

**Proposed**: $K(A) = \Sigma_\alpha(-1)^{\epsilon_\alpha+1} \cdot 2(6\lambda_\alpha^2 - 6\lambda_\alpha + 1)
= -c_{\text{ghost}}(\text{BRST}(A))$.

**(a) Genuineness**: STRONGLY genuine. Recovers $K(\mathrm{KM}_k(\frakg)) =
2\dim(\frakg)$, $K_{\mathrm{Vir}} = 26$, $K^c(W_N) = 2(N-1)(N^2 + (N+1)^2)$
(cubic, multi-source verified), $K(\mathrm{BP}) = 196$. Cubic structure with
$\Delta^3 K^c_N = 24$ constant is hard theorem.

**(b) Inevitability**: BRST identification IS inevitable.

**(c) Counter-example**: Formula assumes quasi-free BRST resolution. Not every
chiral algebra admits one.

**SHARPENED restatement**: Promote with scope "on BRST-resolvable subcategory."
Three definitions ($K_E$, $K_c$, $K_g$) coincide on Koszul-self-dual subcategory.

**Effort**: 3-4 days.

---

### ITEM 8 — Vol I climax: $d_{\mathrm{bar}} = \mathrm{KZ}^*(\nabla_{\mathrm{Arnold}})$

**(a) Genuineness**: PARTIALLY. Master identity stated as Climax Theorem with
three named obstructions (KZB at higher genus partial; W-algebra extension;
universal BRST resolution). The "all four reduce to Arnold's universal
KZ-monodromy" is a SPECIALIZATION CLAIM — Drinfeld-Kohno, Borcherds, Verlinde.
Each specialization needs proof.

**(b) Inevitability**: KZ connection IS Russian-school inevitable object.
Arnold connection (KZB generalization) is natural higher-genus extension.

**(c) Counter-example**: At higher genus ($g \geq 1$), KZB connection
degenerates differently — Beilinson-Drinfeld formula has δ-function singularity
at diagonal. Master identity must be SCOPED to genus 0.

**SHARPENED restatement**: Promote at GENUS 0 only; state genus-1 (KZB) and
higher-genus extensions as conjectures.

**Effort**: 4-5 days.

---

### ITEM 9 — Vol II holographic / arithmetic-shadows V20 integration

**(a) Genuineness**: PARTIALLY. V16 (`thm:hc-verdier-distance`) replaces K4⇔K4
tautology with Verdier-pairing distance (verified at Heisenberg, Vir Lee-Yang,
HaPPY pentagon). V19 (Chiral Hochschild Trinity) proved as corollary of V5 +
single-colour projection of V15.

**(b) Inevitability**: V16 IS inevitable in holographic context. V19 IS
inevitable as trinity bridge.

**(c) Counter-example**: V16 requires "Koszul chiral algebra A" — restrict
scope. V19 requires "logarithmic chiral + finite type."

**SHARPENED restatement**: Inscribe V16 + V19 with EXPLICIT scope restrictions.

**Effort**: 3-4 days for both. NOT 2-3 weeks.

---

### ITEM 10 — Chiral Hochschild concentration, AP160 disambiguation

This is a SUBSET of item 9. MERGE.

**Effort**: 0 (already in item 9).

---

### ITEM 11 — NEW Universal Trace Identity bridge chapter

**Proposed**: Vol I $K = -c_{\mathrm{ghost}}(\mathrm{BRST}(A))$ and Vol III
$\kappa_{\mathrm{BKM}} = c_N(0)/2$ are TWO REFLECTIONS of ONE Φ-bridged trace.

**(a) Genuineness**: NARRATIVE. Slogan, not constructed bridging diagram.
$\mathrm{tr}_{Z(C)}(\mathfrak{K}_C)$ producing both invariants has NOT been
constructed.

**(b) Inevitability**: WOULD be inevitable if proved. Currently CONJECTURE.

**(c) Counter-example**: Vol I $K(A)$ depends on BRST resolution (ghost
spectrum). Vol III $\kappa_{\mathrm{BKM}}$ depends on Borcherds lift of Jacobi
form. DIFFERENT mathematical objects via DIFFERENT functors. Numerical
coincidence at K3 does NOT imply structural unification.

**SHARPENED restatement**: SPLIT into TWO items:
- 11a. INSCRIBE conjecture `conj:universal-trace-identity` as REMARK or
  conjecture, not theorem. Effort 2 days.
- 11b. CONSTRUCT bridging diagram — requires V19 first. Effort 1-2 weeks (open).

If 11b cannot be CONSTRUCTED, 11a stands as remark only.

---

### ITEM 12 — Unified Conventions appendix (cross-volume)

**Sections**:
- §1 The κ-spectrum: subscripts {ch, cat, BKM, fiber} with cross-volume table.
- §2 The q-convention bridge: $q_{KL}^2 = q_{DK}$ as KZ cocycle.
- §3 The $\hbar$ convention bridge: $\hbar = \log(q)$ vs $\hbar = (\log q)/(2\pi i)$.
- §4 The $\phi_{0,1}$ normalization: $c(-1) = 1$ vs $c(-1) = 2$.
- §5 The Hochschild trinity: geometric / algebraic / bigraded.
- §6 The B-cycle sign convention: FM24.
- §7 The Mukai vs intersection-form pairing: signature $(4, 20)$ vs $(3, 19)$.

**This is the FIRST item to do, not the last. UNBLOCKS all other items.**

**Effort**: 4-5 days. EXTREMELY HIGH-LEVERAGE.

---

## CROSS-CUTTING ATTACKS

### A. Items 1, 4, 11 are NARRATIVE re-packaging

The "structural unification" framing is NARRATIVE rather than STRUCTURAL.
Each must (i) state unifying theorem with proof or (ii) state explicitly that
unification is CONJECTURE bridging known facts.

### B. Effort estimates uniformly INFLATED

The 2-3 weeks-per-item estimate is INCONSISTENT with actual work. Items 1, 2,
3a, 9, 10 are 1-4 days each. Items 5, 7, 8, 11b, 12 are 4 days to 2 weeks.
"2-3 weeks per item" averages to ~36 weeks total; actual sum is 8-10 weeks
in dependency order.

### C. UNSEEN dependencies

- Item 5 DEPENDS ON items 1, 2, 3, 4 being mathematically settled FIRST.
- Item 11b DEPENDS ON items 6 + 7 + 9/10 inscribed.
- Item 12 BLOCKS all others.
- Item 4 DEPENDS ON item 12 §4 ($\phi_{0,1}$ normalization).
- Item 1 DEPENDS ON item 12 §7 (Mukai pairing signature).

### D. MISSING items

- **M1**: Inscribe `thm:bcov-f2-zero-correction-d4` (cy_d_kappa_stratification.tex
  L413-426 has it as theorem; not in 12-item map).
- **M2**: Inscribe $V_4$-character classification of CY directions
  (`rem:v4-character-classification-cy-directions`) as NAMED THEOREM (this is
  the SHARPENED form of item 1).
- **M3**: Inscribe universal $K_n$-tower coherence theorem with cohomological-
  home stratification.
- **M4**: Inscribe LP² $\beta = 0$ INDEPENDENTLY of CY-C convergence (item 4) —
  it is a PROVED arithmetic theorem about Skoruppa-Zagier kernel.
- **M5**: Cross-volume FM24 (B-cycle sign error) sweep.
- **M6**: NEW Chapter 6 ($[m_3, B^{(2)}]$ saga, ~600-800 lines, drafted at
  L195-211 of vol3_rearchitecture_proposal.tex) is FULL NEW CHAPTER.

---

## REVISED 13-ITEM REWRITE MAP (with split of item 11)

Recommended EXECUTION ORDER (highest leverage-per-hour first):

| # | Item (sharpened) | Effort | Depends on | Risk |
|---|------------------|--------|------------|------|
| **1** | **Item 12 — Unified Conventions appendix (cross-volume)** | 4-5 d | None | Low |
| **2** | **Item 6 — Promote Koszul Reflection Theorem with $\Pi_1$-$\Pi_4$ as conjectures (Vol I)** | 2-3 d | 12 | Low |
| **3** | **Item 7 — Universal κ-conductor BRST formula on BRST-resolvable subcategory (Vol I)** | 3-4 d | 12 | Low |
| **4** | **Item 2 — CY-D tri-stratum theorem** | 2-3 d | 12 | Low |
| **5** | **Item 1 — K3 Yangian: $V_4$ four-phenotype theorem replaces "trichotomy" framing** | 1-2 d | 12 | Low |
| **6** | **Item 9+10 — Holographic Verdier distance + Hochschild Trinity (Vol II)** | 3-4 d | 12 | Low |
| **7** | **Item 3a — INSCRIBE refutation: $A_{\mathrm{BVDB}}$ not formal on compact CY3** | 1-2 d | 12 | Low |
| **8** | **Item 4 — CY-C class-B falsifier-arithmetic, asymmetric LP²/quintic status** | 3-4 d | 12, 1, 7 | Med |
| **9** | **Item 8 — Climax Theorem at GENUS 0; KZB higher-genus as conjecture (Vol I)** | 4-5 d | 12, 6, 7 | Med |
| **10** | **Item 3b — Curved-formality $Y_3$-as-BCOV-curving as CONJECTURE (Vol III)** | 2-3 d | 12, 7a | Med |
| **11** | **Item 11a — Universal Trace Identity as CONJECTURE only (cross-volume)** | 2 d | 6, 7, 9 | Med |
| **12** | **Missing M1+M2+M3+M4+M5+M6 — auxiliary inscriptions** | 5-7 d | 12, 1, 2 | Med |
| **13** | **Item 5 — CLAUDE.md + 7-part chapter reshuffle (Vol III)** | 4 weeks | 1-12 above | High |
| (deferred) | **Item 11b — CONSTRUCT bridging diagram for Universal Trace** | 2+ weeks | 11a, 6, 7, 9 | Open |

**Total effort**: ~8-10 weeks IF in dependency order. If 11b succeeds, +2 weeks.

---

## TOP 3 ITEMS BY LEVERAGE-PER-HOUR

1. **Item 12 (Conventions appendix)** — UNBLOCKS all 12 other items. 4-5 days.
   100s of downstream silent-error patches.
2. **Item 7 (κ-conductor BRST formula)** — installs master Vol I theorem.
   9 corollaries already drafted. 3-4 days. Unifies κ landscape.
3. **Item 6 (Koszul Reflection promotion)** — installs master Vol I structural
   theorem. 2-3 days. Rhetorical anchor for everything else.

---

## SHARPEST OBJECTIONS PER ITEM (ONE-LINERS)

| # | Sharpest objection |
|---|-------------------|
| 1 | "Eigenvalue trichotomy" is basis change, not theorem; LP² and $K3^{[n]}$ break binary classification. |
| 2 | Dichotomy hidden in remark; promote AND refine to tri-stratum. |
| 3 | "Curved formality with $Y_3$ as BCOV datum" is conjecture, not corollary. |
| 4 | Quintic $\alpha = 0$ conditional on 4 hypotheses; do NOT integrate symmetrically with verified LP² $\beta = 0$. |
| 5 | "K3 Yangian" Part IV title overclaims — only abelian proved. |
| 6 | $\Pi_1$-$\Pi_4$ obstructions must be named as conjectures. |
| 7 | Restrict to BRST-resolvable subcategory. |
| 8 | Restrict to genus 0; KZB higher-genus open. |
| 9 | V16 + V19 already drafted; inscription is action item. |
| 10 | Subset of item 9; merge. |
| 11 | "Universal Trace Identity" is SLOGAN; bridging diagram not constructed. |
| 12 | Move from position 12 to position 1 — UNBLOCKS everything. |

---

## SHARPEST COUNTER-EXAMPLES PER STRUCTURAL UNIFICATION

| Unification | Counter-example |
|-------------|-----------------|
| Eigenvalue trichotomy {0,0,2,2} | LP² $\hat{M}=(1,7,-5,1)$ has 3 nonzero characters; $K3^{[n]}$ has 1 nonzero character. |
| Even/odd-$d$ dichotomy | Holomorphic-symplectic $\mathrm{K3}^{[2]}$ has $\Xi = 3$, NOT $\Xi = 2$. |
| Curved formality at quintic | NO continuous torus action; Costello-Li convergence not established for compact case. |
| Universal Trace Identity | $K(\mathrm{Vir}_{c=24}) = 26$, $\kappa_{\mathrm{BKM}}(K3) = 2$ — different formulas for different invariants. |
| LP² + quintic symmetric integration | LP² β=0 verified; quintic α=0 conditional on 4 hypotheses. Asymmetric. |
| Six-routes commute via $\alpha_\bigcirc = \mathrm{id}$ | Proof at L184 is CIRCULAR. |

---

## RECOMMENDED ACTION PLAN (post-current-slate)

**Week 1**: Item 12 (Conventions) — unblocks everything.
**Week 2**: Items 6 + 7 (Vol I master theorems).
**Week 3**: Items 2 + 1 (Vol III local rewrites).
**Week 4**: Items 9/10 (Vol II) + Item 3a (Vol III refutation).
**Week 5**: Item 4 (CY-C asymmetric integration).
**Week 6**: Item 8 (Climax at genus 0).
**Week 7**: Item 3b (curved formality conjecture) + Item 11a (Universal Trace conjecture).
**Week 8**: Missing M1-M6 inscriptions.
**Weeks 9-12**: Item 5 (chapter reshuffle, Vol III) — ONLY after items 1-12 settled.
**Open-ended**: Item 11b (Universal Trace bridging construction) — pursue as research, not chapter.

The CRITICAL operational insight: highest-leverage item (12) is currently last;
doing it FIRST unblocks every other item. Do NOT invert the dependency order.

---

— Raeez Lorgat, 2026-04-17 (post-adversarial-rectification)
