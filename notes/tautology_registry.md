# Tautology Registry — ProvedHere claims where honest `@independent_verification` decoration fails

This is the working queue for manuscript healing. Each entry lists:
- Claim label
- Why the canonical test is tautological (same source on both sides)
- Three healing options (disjoint source / scope restriction / status downgrade)
- Current recommendation

A claim leaves this registry when either (a) a disjoint verification source is found and installed, or (b) the scope is restricted or status downgraded in the .tex.

Seeded from adversarial audit 2026-04-16 (first_principles_cache.md #57-68).

---

## prop:bkm-weight-universal (kappa_BKM = c_N(0)/2) — PARTIALLY HEALED 2026-04-17

**Status:** Manuscript clean (proposition correctly cites disjoint sources). Engine test still tautological. Healing of test pending.

**File:** chapters/examples/k3_chiral_algebra.tex (proposition + new rem:bkm-weight-universal-iv-status)

**What was done:**
- Added `rem:bkm-weight-universal-iv-status` (k3_chiral_algebra.tex L590-624) documenting:
  (a) the manuscript proposition is genuinely proved via disjoint sources (Borcherds 1998 + Gaberdiel-Hohenegger-Volpato 2010); no manuscript-level tautology.
  (b) the engine `kappa_bkm_universal.py` `FRAME_SHAPE_DATA[N]` table hardcodes BOTH `borcherds_weight` AND `c_disc_0` with the relation `weight = c_0/2` literal, making the 99 tests `Fraction(c_0, 2) == weight` tautological per HZ3-11.
  (c) the genuine independent-verification path: compute c_N(0) independently from the Mathieu-twined elliptic genus formula α(g) φ_{0,1} + β(g) φ_{-2,1} (Eguchi-Hikami-Ooguri 2010) AND compute wt(Φ_N) independently from Igusa's Sp_4(Z) modular-form classification. Both sources disjoint from FRAME_SHAPE_DATA.

**What remains (compute work):**
Install `@independent_verification` decorated test that:
1. Computes c_N(0) from Mathieu-twined elliptic genus formula (Frame shape -> α(g), β(g) -> twined Jacobi form -> q^0 z^0 coefficient) — independent of `FRAME_SHAPE_DATA[N].c_disc_0` hardcoded value.
2. Verifies wt(Φ_N) from Borcherds product order — independent of `FRAME_SHAPE_DATA[N].borcherds_weight` hardcoded value.
3. Bridges them via Borcherds 1998 weight theorem.

This breaks the tautology by sourcing c_N(0) and wt(Φ_N) from disjoint physical/modular sources.

**Lossless reframe:** the proposition stays `\ClaimStatusProvedHere` because the manuscript proof is correct (disjoint citations to Borcherds + GHV). Engine-level test rectification is a compute-side healing, not a manuscript-side downgrade.

---

## thm:derived-framing-obstruction (CY-A_3 inf-cat)

**File:** chapters/theory/cy_to_chiral.tex:1938

**Tautology:** "HH^{-2}_{E_1}(A,A) = 0 by unit-connectedness" uses connectivity of A. For smooth proper CY_3 categories, A = HH_*(C) is Serre self-dual, so HH_{-3} ≅ HH_0* ≠ 0; A is NOT connective. The bar-filtration degree count at L1980 silently assumes A_{<0} = 0. No test supplies an independent source for vanishing — the "verification" is the same connectivity argument restated.

**Disjoint source (if pursued):** None known. The Goodwillie/Francis-Gaitsgory machinery is the only route. An independent route would require either (a) explicit chain-level rectification of [m_3, B^(2)] for a specific non-formal CY_3 A_∞ algebra, or (b) a direct construction of the E_3-lift on a concrete family.

**Scope restriction:** Replace the universal quantifier "for all smooth proper CY_3 categories" with "for A connective and unit-connected". This excludes compact CY_3 but covers the formal/local cases where the proof actually works.

**Status downgrade:** `\begin{conjecture}` for compact CY_3; `\begin{theorem}` retained for connective A.

**Recommendation:** scope restriction. The theorem as currently stated claims too much; restated under the actual hypothesis it is genuine.

---

## prop:cy-a-three-saga-resolution-costello (total {b, B^(2)} = 0)

**File:** chapters/theory/m3_b2_saga.tex

**Tautology:** The Costello-TCFT engine (`operadic_tcft_mk_b2_engine.py`, 525 lines) contains no numerical computation; tests check that specific strings appear in prose dataclasses. The cross-arity cancellation asserted in rem:b2-cancellation is REFUTED by the author's own `chain_level_m2_b2_cancellation.py`: {b_2,B^(2)} and {b_3,B^(2)} map to disjoint graded components CC_{n-k+1} and cannot cancel. The retreat to an undefined `B^(2)_TCFT` is vapor.

**Disjoint source (if pursued):** A genuine verification would require (a) defining `B^(2)_TCFT` as an explicit moduli-space operation and (b) independently computing {b_k, B^(2)_TCFT} on a concrete non-formal CY_3 algebra (local P^2 would do) and checking the total sums to zero with explicit matching terms.

**Scope restriction:** None is adequate. The claim as stated is either true with a missing proof or false at the chain level.

**Status downgrade:** Downgrade from `\begin{theorem}` to `\begin{conjecture}`; retract the Costello/Stasheff cross-arity "proof" and list it with the other three retracted proofs (cyclic invariance, bidegree, Tsygan). The chain-level route is dead; only the ∞-cat route remains (and it has its own gap — see previous entry).

**Recommendation:** status downgrade + retraction entry. Four wrong proofs, four retractions.

---

## prop:p2-vanishes-exact (BKM Serre P_2(D) = 0) — HEALED 2026-04-17

**Status:** HEALED via status downgrade. AP40 violation closed.

**File:** working_notes.tex (relabeled `conj:bkm-serre-exact`), bkm_serre_higher_order.py (engine STATUS unchanged)

**Resolution:** Status downgraded from `\begin{theorem}` (`thm:bkm-serre-exact`) to `\begin{conjecture}` (`conj:bkm-serre-exact`) with `\ClaimStatusConjectured` tag, matching the engine's self-declared `STATUS = 'CONJECTURAL'`. The two heuristic arguments (ε₁·ε₂ = 0 parameter-count and L_0 + εJ_0 spectral-flow linearity) are preserved as non-conclusive evidence in `rem:p2-status-correction`. The leading-order P_1(D) = -2D claim survives as proved (it is the verified linear-order computation). Higher-order vanishing requires perturbative ε²-cancellation in the BKM imaginary-root denominator Fourier expansion as the genuine independent source; this remains the open frontier for promotion back to theorem.

**Cross-volume sweep:** CLAUDE.md "Main Theorems" table updated (BKM Serre P_2 row tagged CONJECTURAL with healing date and AP40 reference); CLAUDE.md "Five load-bearing open problems" Item 2 updated (sl_2 Serre constraints split into proved leading-order and conjectural higher-order); CLAUDE.md Session-Entry rule 25 updated. The cy_c_six_routes_convergence.tex bullet (line 814 region) updated to reflect leading-order PROVED, higher-order CONJECTURAL split. No theorem-level claim survives as a tautology.

**Lossless reframe:** the 182-generator Serre kernel is the leading-order kernel; whether it is the full kernel depends on the conjecture. Previous lower-bound rank claims stand.

---

## sec:k3e-six-routes (Six routes to G(K3 × E)) — HEALED 2026-04-17

**Status:** HEALED via structural rewrite. AP-CY60 properly cited; convergence claim correctly tagged as content of CY-C.

**File:** chapters/examples/k3_chiral_algebra.tex L757-799

**What was done:**
- Section opener (L760) explicitly states: "approached by six independent mathematical constructions (AP-CY60). Only Route~4 uses the CY-to-chiral functor Φ; the remaining five are independent constructions. That all six converge on the same target is the *content* of Conjecture~CY-C, not a consequence of functoriality."
- Each Route 1-6 carries explicit Status tag (proved / proved at level / heuristic / conjectural).
- rem:k3e-route-comparison (L776-779) clarifies what each route captures (combinatorial skeleton vs abelian fiber vs nonabelian fiber vs full chiral algebra vs physical interpretation vs Schur sector).
- rem:bllpr-k3-connection (L781-797) explicitly distinguishes the BLLPR algebra and the K3 Yangian as DIFFERENT algebraizations, with five structural invariants (central charge, E_n level, Ω-dependence, character growth, modular group). The connection is conjectural and explicitly labelled.
- The section title "Six routes to G(K3 × E)" is preserved as proper structural narrative; the target G(K3 × E) is correctly flagged as conjectural via CY-A_3 + CY-C dependency throughout.

**Lossless reframe:** No claim was demoted; the section was already structurally rewritten in earlier work to (a) flag the conjectural CY-C target, (b) preserve the structural narrative of "approaching" the same target via independent paths, (c) cite AP-CY60 explicitly. The registry concern about "structural incoherence" is resolved: each of the six routes is presented as an independent construction with its own status, and the convergence is the explicit content of CY-C (named conjecture, not assumed equality).

---

## Entries to add (next pass)

- `thm:class-m-e3-bar-dim` (currently PROVED for g ≤ 3, stated globally): scope restrict to g ≤ 3.
- `conj:cy-kappa-identification` at d=3: already Conjectured — no action.
- `thm:k3-super-yangian-lift`: tagged Conjectured — replace "lift from Mukai signature (4,20)" with "proposed super-Yangian resolution of ω-twisted unitarity; Z/2-grading from positive/negative Mukai cones (non-canonical choice)".
