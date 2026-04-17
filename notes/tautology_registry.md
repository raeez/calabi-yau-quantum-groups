# Tautology Registry — ProvedHere claims where honest `@independent_verification` decoration fails

This is the working queue for manuscript healing. Each entry lists:
- Claim label
- Why the canonical test is tautological (same source on both sides)
- Three healing options (disjoint source / scope restriction / status downgrade)
- Current recommendation

A claim leaves this registry when either (a) a disjoint verification source is found and installed, or (b) the scope is restricted or status downgraded in the .tex.

Seeded from adversarial audit 2026-04-16 (first_principles_cache.md #57-68).

---

## prop:bkm-weight-universal (kappa_BKM = c_N(0)/2)

**File:** chapters/examples/k3_chiral_algebra.tex

**Tautology:** FRAME_SHAPE_DATA[N] hardcodes `(weight, c_0, ...)` with the invariant `weight := c_0 / 2` literal. All 99 tests verify `Fraction(c_0, 2) == weight` against the same table. "6-path cross-validation" imports/reconstructs the same FRAME_SHAPE_DATA.

**Disjoint source (if pursued):** Compute the BKM central charge of g_{Δ_5} directly from imaginary-root multiplicities of the denominator product Φ_10 (Gritsenko-Nikulin 1998), and compare to c_0/2 as the weight of the Borcherds lift. These are independent derivations.

**Scope restriction:** Replace "all K3-fibered CY3s" with "the 8 diagonal Z/NZ symplectic orbifolds (Chaudhuri-Dolan-Hockney-Polchinski / Gaberdiel-Volpato list) plus K3 × E". STU in the diagonal limit only.

**Status downgrade:** For general K3-fibered, `\begin{conjecture}` until the root-multiplicity verification is installed.

**Recommendation:** scope restriction + separate `prop:bkm-weight-automorphic` (unconditional, trivially c_0/2 by Borcherds) from `conj:bkm-weight-central-charge` (identifying automorphic weight with BKM central charge; proved for N=1,2,3,4 via Gritsenko-Nikulin, conjectural otherwise).

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

## sec:k3e-six-routes (Six routes to G(K3 × E))

**File:** chapters/examples/k3_chiral_algebra.tex:716-733

**Tautology:** Not a single tautological ProvedHere claim — a structural incoherence. The six "routes" produce six different objects (BKM superalgebra, abelian Heisenberg, nonabelian Yangian, chiral algebra, heuristic BPS, Virasoro). G(K3 × E) is never independently defined. The follow-up remark `rem:bllpr-k3-connection` explicitly admits these are "different algebraizations".

**Disjoint source (if pursued):** N/A — the target object doesn't exist as stated.

**Scope restriction:** Rename "Six routes to G(K3 × E)" → "Six constructions producing algebras with shared numerical invariants". Drop the convergence claim; the convergence IS CY-C and CY-C is conjectural for simple g, not formulated for K3 × E.

**Status downgrade:** Remove "routes to G(K3 × E)" framing entirely. Present as a comparison table of six algebraizations (AP-CY59, AP-CY60).

**Recommendation:** structural rewrite. Keep the six constructions as independent content; drop the convergence claim; add a remark citing AP-CY59/AP-CY60.

---

## Entries to add (next pass)

- `thm:class-m-e3-bar-dim` (currently PROVED for g ≤ 3, stated globally): scope restrict to g ≤ 3.
- `conj:cy-kappa-identification` at d=3: already Conjectured — no action.
- `thm:k3-super-yangian-lift`: tagged Conjectured — replace "lift from Mukai signature (4,20)" with "proposed super-Yangian resolution of ω-twisted unitarity; Z/2-grading from positive/negative Mukai cones (non-canonical choice)".
