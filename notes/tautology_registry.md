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

## prop:p2-vanishes-exact (BKM Serre P_2(D) = 0)

**File:** working_notes.tex (called theorem there), bkm_serre_higher_order.py (status CONJECTURAL in engine)

**Tautology:** Engine self-declares `STATUS = 'CONJECTURAL'`. Argument "ε_1·ε_2 = ε·0 = 0 in 1d Ω-background" is circular (a 1d background has one parameter by definition). 70 tests compare to the linear extrapolation, not an independent source.

**Disjoint source (if pursued):** Perturbative computation of P_2 from BKM imaginary-root denominator at order ε² — checking vanishing not by parameter count but by explicit cancellation of ε² terms in the Fourier expansion of the deformed denominator.

**Scope restriction:** "P_2 = 0 to leading order in the linear approximation" is trivial; the "exact" qualifier is what's unsupported.

**Status downgrade:** Tag `\begin{conjecture}` — matches the engine's own `STATUS`.

**Recommendation:** status downgrade. AP40 violation: engine says CONJECTURAL, manuscript says THEOREM.

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
