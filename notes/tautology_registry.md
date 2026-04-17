# Tautology Registry — ProvedHere claims where honest `@independent_verification` decoration fails

This is the working queue for manuscript healing. Each entry lists:
- Claim label
- Why the canonical test is tautological (same source on both sides)
- Three healing options (disjoint source / scope restriction / status downgrade)
- Current recommendation

A claim leaves this registry when either (a) a disjoint verification source is found and installed, or (b) the scope is restricted or status downgraded in the .tex.

Seeded from adversarial audit 2026-04-16 (first_principles_cache.md #57-68).

---

## prop:bkm-weight-universal (kappa_BKM = c_N(0)/2) — HEALED at N=1 2026-04-17

**Status:** Manuscript clean. Engine N=1 case has genuine disjoint-source verification installed. Engine N=2..8 (orbifold cases) still pending Mathieu-twined verification — future compute-side work.

**File:** chapters/examples/k3_chiral_algebra.tex (manuscript), compute/tests/test_kappa_bkm_universal.py::TestIndependentVerificationN1 (engine).

**What was done at manuscript level (commit 5e758f0):**
- Added `rem:bkm-weight-universal-iv-status` (k3_chiral_algebra.tex L590-624) documenting the manuscript proposition is genuinely proved via disjoint sources (Borcherds 1998 + GHV 2010); no manuscript-level tautology.

**What was done at engine level (commit fd18c0c):**
- New TestIndependentVerificationN1 class in test_kappa_bkm_universal.py with @independent_verification decorated test:
  - DERIVATION: FRAME_SHAPE_DATA[1].c_disc_0 = 10 (GHV 2010 Frame-shape from M_24 character theory)
  - VERIFICATION: phi01_by_discriminant(D=0) = 10 (exact theta-ratio formula in phi01_fourier.py, EZ 1985 Jacobi-form theory)
  - DISJOINT: M_24 character theory ⊥ theta-function ratios (no common mathematical input)
  - 2 tests pass; verify-independence audit registers entry as non-tautological.
- Also installed test_c_minus_1_via_theta_ratio_polar_term documenting the half-normalization convention.

**What remains:**
- Extend to N=2..8 orbifold cases: install independent verification of c_g(0) values via Mathieu-twined elliptic genus formula α(g) φ_{0,1} + β(g) φ_{-2,1} (Eguchi-Hikami-Ooguri 2010, Cheng 2010, GHV 2010). The α(g), β(g) coefficients can be computed from Frame shape data, but require an independent computational path (not the FRAME_SHAPE_DATA table).
- Future tick.

**Lossless reframe:** the proposition stays `\ClaimStatusProvedHere`; engine N=1 case has genuine disjoint-source verification; remaining N=2..8 cases tracked as future compute work without affecting manuscript status.

---

## thm:derived-framing-obstruction (CY-A_3 inf-cat) — PARTIALLY HEALED 2026-04-17

**Status:** Theorem hypothesis explicitly tightened; compact non-formal CY_3 case correctly tagged as conditional. Engine-side connectivity verification still pending.

**File:** chapters/theory/cy_to_chiral.tex L1975-2050

**What was done:**
- Theorem hypothesis modified to require BOTH "connective ($\HH_n(\cC) = 0$ for $n < 0$)" AND "unit-connected ($\HH^0(\cC) = k$)" explicitly, no longer concealing the connectivity assumption inside "unit-connectedness" prose.
- Step 2 in the proof updated: "by the bar-resolution argument: connectivity gives $\bar{A} = A_{\geq 1}$ concentrated in strictly positive degrees" (no longer the misleading "by unit-connectedness").
- New rem:derived-framing-scope-restriction inserted after the theorem documenting:
  (a) The connectivity hypothesis HOLDS for toric CY_3 (C^3, conifold, local P^2, local P^1 × P^1) and smooth quasi-projective CY_3 with formal Kapranov-Manin-Tate model.
  (b) For compact CY_3 with Serre duality (quintic, K3 × E, complete-intersection threefolds), Serre self-duality gives HH_{-3}(C) ≅ HH_0(C)^* ≅ k* ≠ 0, so A is NON-CONNECTIVE at the chain level. The theorem applies in this regime only after passage to a formal model OR Goodwillie convergence in the non-connective category.
  (c) The status table of rem:hopf-reduction reflects this distinction: "formal" entries use formality directly; "TCFT" entries use Costello's operadic resolution.
  (d) The compact non-formal CY_3 case is conditional on (1) chain-level formality OR (2) Goodwillie convergence in non-connective category.

**Lossless reframe:** The theorem retains \ClaimStatusProvedHere because the proof IS sound under the (now explicit) connective + unit-connected hypothesis. Previously the connectivity was hidden inside "unit-connectedness" prose; the rectification surfaces it explicitly. The compact non-formal case is properly tagged as conditional, not proved.

**What remains:**
- Engine-side independent verification of the Goodwillie tower convergence for compact non-connective A (or formality verification for specific compact CY_3 A_∞ models).
- This is the chain-level rectification work. Several existing engines verify the formal cases; the compact non-formal case requires either (a) explicit chain-level rectification of [m_3, B^(2)] for specific non-formal CY_3 A_∞ algebras (e.g., quintic), or (b) a direct construction of the E_3-lift on a concrete family.

---

## prop:cy-a-three-saga-resolution-costello (total {b, B^(2)} = 0) — PARTIALLY HEALED 2026-04-17

**Status:** Theorem reframed via TCFT-vs-naive disambiguation; chain-level identification gap surfaced explicitly. Engine refutation incorporated as documented evidence.

**File:** chapters/theory/m3_b2_saga.tex L531-545 (theorem) + new rem:tcft-vs-naive-b2 L596-654

**What was done:**
- Added rem:tcft-vs-naive-b2 immediately after rem:tcft-vs-mixed documenting:
  (a) The B^(2) in thm:total-ainf-compat is the TCFT-derived operator on C_•(A), defined by Costello's open-closed identification with the genus-change operation on the moduli operad. The TCFT identity {b, B^(2)_TCFT} = 0 holds at the moduli-operad chain complex level by ∂² = 0.
  (b) The naive chain-level B^(2)_naive (defined directly as a Connes-hierarchy contraction on the bar complex) does NOT satisfy cross-arity cancellation: chain_level_m2_b2_cancellation.py engine VERIFIES that {b_2, B^(2)_naive} maps arity 5 → arity 2 while {b_3, B^(2)_naive} maps arity 5 → arity 1; their sum lives in different graded pieces and cannot vanish by direct cancellation.
  (c) The chain-level identification B^(2)_TCFT ≃ B^(2)_naive on the bar complex is the CONJECTURAL chain-level frontier of CY-A_3: lifting the operadic-TCFT identity to a strict chain-level identity requires either (1) chain-level rectification of the cyclic A_∞-structure, or (2) an explicit chain homotopy h with B^(2)_TCFT - B^(2)_naive = [d_tot, h]. The latter is Tradler's strictification (math/0108027) for formal algebras; for non-formal A_∞-algebras the strictification is conjectural.
  (d) The status discipline: thm:total-ainf-compat is correctly stated for B^(2)_TCFT; the chain-level identification with B^(2)_naive on the bar complex is conjectural for non-formal A_∞-algebras.
  (e) Cross-references AP-CY62 (geometric vs algebraic Hochschild model) — this is the same family of disambiguations.

**Lossless reframe:** The theorem retains \ClaimStatusProvedHere because it IS proved for the TCFT-derived operator at the moduli-operad level. The chain-level open frontier is correctly surfaced in the new remark as conjectural for non-formal algebras. No claim was demoted; the interpretive ambiguity (TCFT vs naive operator) was the silent gap, now made explicit.

**What remains:**
- Engine work: install an explicit chain homotopy h with B^(2)_TCFT - B^(2)_naive = [d_tot, h] for at least one non-formal CY_3 model (e.g., local P^2). This converts the conjectural identification into a proved chain-level identity.
- This is the chain-level rectification work that several existing engines partially address but do not yet complete.

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
