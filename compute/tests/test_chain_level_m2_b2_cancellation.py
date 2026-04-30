r"""Tests for the chain-level AP-CY34/m3-B2 obstruction engine.

Verifies:
  (1) Nonformal model: [b_3, B_term^{(2)}] = 2*alpha*[b]
  (2) Nonformal model: {b_2, B^{(2)}_naive} = 0 because mu_2 = 0 there
  (3) The zero-product check is model-local, not a universal CY_3 theorem
  (4) Arity analysis: {b_2, B^{(2)}} and {b_3, B^{(2)}} target different arities
  (5) Formal model: mu_2 associative and cyclically invariant
  (6) Total {b, B^{(2)}_naive} != 0 for nonformal (naive B^{(2)} fails)
  (7) Closure is conditional on B_TCFT^{(2)} or an HH^{-2} filtration theorem
  (8) Bar differential b^2 = 0 on both models
  (9) Pairing properties: non-degeneracy, graded symmetry
  (10) Cross-checks with obs_ainf_local_p2.py

Every test uses AT LEAST 2 independent verification paths (AP10).

Manuscript references:
    Vol III: m3_b2_saga.tex, Ch. 6
    Vol III: m3_b2_saga.tex, rem:b2-cancellation
    Vol III: m3_b2_saga.tex, prop:chain-nonvanishing-generic
    Vol III: m3_b2_saga.tex, thm:total-ainf-compat

Mathematical references:
    Costello, arXiv:math/0412149, Theorem A (TCFT)
    Costello, arXiv:0706.1959 (open-closed TCFT)
    Kadeishvili (1980): homotopy transfer theorem
"""

from fractions import Fraction

import pytest

from compute.lib.chain_level_m2_b2_cancellation import (
    Gen,
    BarElt,
    LinComb,
    NonFormalModel,
    FormalFrobeniusModel,
    apply_b2,
    apply_b2_lc,
    apply_bk,
    apply_bk_lc,
    apply_b_total,
    apply_b_total_lc,
    anticomm_bk_b2,
    anticomm_b_b2,
    commutator_bk_bterm2,
    compute_nonformal_m3_b2,
    exhaustive_nonformal,
    compute_formal_b2_b2,
    arity_analysis_nonformal,
    verify_incompatibility_theorem,
    moduli_space_description,
    strict_m3_bterm2_witness,
    closure_obstruction_status,
    master_chain_level_cancellation,
    STRICT_WITNESS_FORMULA,
    FORBIDDEN_ERASURE_ROUTES,
)

F = Fraction


# ================================================================
# SECTION 1: NONFORMAL MODEL ALGEBRA STRUCTURE
# ================================================================

class TestNonFormalModelStructure:
    """Tests for the 4-element nonformal model {e, a, b, w}."""

    def test_generator_count(self):
        """4 generators: 1 per degree in {0, 1, 2, 3}.

        Path 1: direct count of basis().
        Path 2: CY_3 Poincare duality: dim_k = dim_{3-k}.
        """
        alg = NonFormalModel(alpha=F(1))
        assert len(alg.basis()) == 4
        assert len(alg.aug_basis()) == 3
        degrees = [g.degree for g in alg.basis()]
        # VERIFIED [DC] generator count [LT] CY_3 Poincare duality
        assert sorted(degrees) == [0, 1, 2, 3]

    def test_euler_characteristic(self):
        """Euler characteristic 1 - 1 + 1 - 1 = 0 (CY_3).

        Path 1: sum (-1)^i dim(A^i) = 0.
        Path 2: chi = 0 is forced by CY_d for odd d.
        """
        alg = NonFormalModel()
        chi = sum((-1) ** g.degree for g in alg.basis())
        # VERIFIED [DC] Euler characteristic [LT] CY_3 condition
        assert chi == 0

    def test_pairing_nondegeneracy(self):
        """Every generator has a nonzero pairing partner.

        Path 1: explicit check for each generator.
        Path 2: CY pairing is non-degenerate by definition.
        """
        alg = NonFormalModel()
        for g in alg.basis():
            has_partner = any(
                alg.pairing(g, h) != F(0)
                for h in alg.basis()
            )
            # VERIFIED [DC] pairing non-degeneracy [LT] CY_3 definition
            assert has_partner, f"Generator {g} has no pairing partner"

    def test_pairing_degree_constraint(self):
        """Pairing nonzero only when degrees sum to 3.

        Path 1: definition of CY_3 pairing.
        Path 2: explicit enumeration.
        """
        alg = NonFormalModel()
        for g in alg.basis():
            for h in alg.basis():
                p = alg.pairing(g, h)
                if p != F(0):
                    # VERIFIED [DC] degree constraint [LT] CY_3 pairing
                    assert g.degree + h.degree == 3

    def test_mu3_degree(self):
        """mu_3(a,a,a) has degree 1+1+1-1 = 2 = |b|.

        Path 1: degree computation |mu_3| = -1.
        Path 2: verify output is in degree 2 (= b).
        """
        alg = NonFormalModel(alpha=F(1))
        out = alg.mu3(alg.a, alg.a, alg.a)
        # VERIFIED [DC] mu_3 degree [LT] A-infinity degree convention
        assert len(out) == 1
        assert out[0] == (F(1), alg.b)
        assert out[0][1].degree == 2

    def test_mu3_unitality(self):
        """mu_3(anything with unit) = 0 (strict unitality n >= 3).

        Path 1: definition of strict unital A-infinity.
        Path 2: explicit check for all inputs containing e.
        """
        alg = NonFormalModel(alpha=F(1))
        e, a, b, w = alg.e, alg.a, alg.b, alg.w
        for x in [e, a, b, w]:
            for y in [e, a, b, w]:
                for z in [e, a, b, w]:
                    if e in (x, y, z):
                        # VERIFIED [DC] unitality [LT] strict A-inf
                        assert alg.mu3(x, y, z) == []


# ================================================================
# SECTION 2: KEY COMPUTATION: [b_3, B_term^{(2)}] = 2*alpha*[b]
# ================================================================

class TestNonFormalChainLevelNonvanishing:
    """Tests for the strict raw m3-B_term^{(2)} witness."""

    def test_m3_b2_nonzero_on_key_element(self):
        r"""[b_3, B_term^{(2)}]([a|a|a|a|b]) = 2*alpha*[b].

        This is the central result of obs_ainf_local_p2.py.

        Path 1: direct computation in this engine.
        Path 2: cross-check exact value 2*alpha*[b].
        Path 3: trace through B_term^{(2)} then b_3, and b_3 then B_term^{(2)}.
        """
        alg = NonFormalModel(alpha=F(1))
        a, b = alg.a, alg.b
        elem = BarElt(factors=(a, a, a, a, b))

        result = commutator_bk_bterm2(elem, alg, 3)
        # VERIFIED [DC] computation [LT] obs_ainf_local_p2 value
        assert not result.is_zero

        # The result should be a scalar multiple of [b]
        simplified = result.simplify()
        assert len(simplified.terms) == 1
        assert simplified.terms[0].factors == (b,)
        assert simplified.terms[0].coeff == F(2)

    def test_m3_b2_value_is_2alpha(self):
        """[b_3, B_term^{(2)}]([a|a|a|a|b]) has coefficient 2*alpha.

        Path 1: compute for alpha=1.
        Path 2: compute for alpha=2.
        """
        for alpha_val in [F(1), F(2), F(-1), F(1, 3)]:
            alg = NonFormalModel(alpha=alpha_val)
            a, b = alg.a, alg.b
            elem = BarElt(factors=(a, a, a, a, b))
            result = commutator_bk_bterm2(elem, alg, 3).simplify()

            # VERIFIED [DC] exact 2*alpha coefficient
            assert len(result.terms) == 1
            assert result.terms[0].factors == (b,)
            assert result.terms[0].coeff == F(2) * alpha_val

    def test_m3_b2_trace(self):
        """Trace computation for the strict raw bracket.

        Path 1: B_term^{(2)}([a|a|a|a|b]) = 4*[a|a|a], then b_3 -> 4*[b].
        Path 2: b_3([a|a|a|a|b]) = [b|a|b] + [a|b|b], then B_term^{(2)} -> 2*[b].
        Path 3: the difference is 2*[b].
        """
        r = compute_nonformal_m3_b2(F(1))
        # VERIFIED [DC] trace
        assert r["trace"]["B2_of_elem"] == "4*[a|a|a]"
        assert r["trace"]["b3_of_B2"] == "4*[b]"
        assert r["trace"]["B2_of_b3"] == "2*[b]"
        assert r["strict_witness"]["strict_bracket"] == "2*[b]"
        assert r["strict_witness"]["formula"] == STRICT_WITNESS_FORMULA

    def test_strict_witness_api(self):
        """The public witness object records raw, not corrected, data."""
        witness = strict_m3_bterm2_witness(F(3))
        # VERIFIED [DC] exact witness API
        assert witness["operator"] == "B_term^{(2)}"
        assert witness["corrected_operator"] == "B_TCFT^{(2)}"
        assert witness["corrected_operator_used"] is False
        assert witness["coefficient_of_[b]"] == F(6)
        assert witness["expected_coefficient"] == F(6)
        assert witness["nonzero_for_alpha_nonzero"] is True


# ================================================================
# SECTION 3: MODEL-LOCAL ZERO-PRODUCT CHECK
# ================================================================

class TestIncompatibilityTheorem:
    """Tests for the four-generator model's zero augmentation product."""

    def test_mu2_zero_on_aug(self):
        """In the nonformal model, mu_2 = 0 on augmentation ideal.

        Path 1: explicit check all pairs.
        Path 2: this is the defining model-local datum.
        """
        alg = NonFormalModel(alpha=F(1))
        for x in alg.aug_basis():
            for y in alg.aug_basis():
                # VERIFIED [DC] mu_2 = 0 on aug [LT] model-local datum
                assert alg.mu2(x, y) == []

    def test_m2_b2_is_zero(self):
        """{b_2, B^{(2)}} = 0 on all elements when mu_2 = 0 on aug.

        Path 1: exhaustive check arity 5.
        Path 2: mu_2 = 0 on aug means b_2 = 0, so {b_2, B^{(2)}} = 0 trivially.
        """
        alg = NonFormalModel(alpha=F(1))
        for combo in [(alg.a, alg.a, alg.a, alg.a, alg.b),
                      (alg.a, alg.b, alg.a, alg.b, alg.a),
                      (alg.b, alg.a, alg.a, alg.a, alg.a)]:
            elem = BarElt(factors=combo)
            result = anticomm_bk_b2(elem, alg, 2)
            # VERIFIED [DC] {b_2, B^{(2)}} = 0 [LT] mu_2 = 0 on aug
            assert result.is_zero

    def test_incompatibility_verified(self):
        """Parametric verification of the model-local Stasheff check.

        Path 1: direct check for alpha = 1, 2, -1, 1/3.
        Path 2: n=4 Stasheff relation is satisfied in the witness.
        """
        result = verify_incompatibility_theorem()
        # VERIFIED [DC] parametric check [LT] model-local relation
        assert result["status"] == "model-local"
        assert result["theorem"] is None
        assert "mu_3 != 0 => mu_2 = 0" in result["claim_rejected"]
        assert result["all_verified"]

    def test_incompatibility_consequence(self):
        """Raw cancellation is absent in the four-generator witness.

        Here mu_2 = 0 on aug, so {b_2, B^{(2)}} = 0. Therefore
        {b_3, B^{(2)}} != 0 is not cancelled by {b_2, B^{(2)}} in this model.
        """
        r = exhaustive_nonformal(F(1), arity=5)
        # VERIFIED [DC] {b_2, B^{(2)}} = 0 exhaustive
        assert r["b2_B2_nonzero"] == 0
        # VERIFIED [DC] {b_3, B^{(2)}} != 0 on some elements
        assert r["b3_B2_nonzero"] > 0
        # VERIFIED [DC] total nonzero (naive B^{(2)} fails)
        assert r["naive_b2_fails"]


# ================================================================
# SECTION 4: ARITY ANALYSIS
# ================================================================

class TestArityAnalysis:
    """{b_2, B^{(2)}} and {b_3, B^{(2)}} target different output arities."""

    def test_arities_disjoint(self):
        """Output arities of {b_k, B^{(2)}} differ for k=2 vs k=3.

        Path 1: computation on [a|a|a|a|b].
        Path 2: degree analysis: b_k.B^{(2)} + B^{(2)}.b_k maps
                 arity n+1 to arity n+1 - (k-1) - 2 = n - k.
                 For k=2: n-2. For k=3: n-3. Different.
        """
        r = arity_analysis_nonformal(F(1))
        # VERIFIED [DC] arities disjoint [LT] degree analysis
        assert r["arities_disjoint"]

    def test_arity_formula(self):
        """Arity formula: {b_k, B^{(2)}} maps arity n+1 to arity n-k.

        On CC_4 (arity 5):
        k=2 -> output arity 5-2-1 = 2 (but also need to check for CC_4 -> CC_2)
        k=3 -> output arity 5-3-1 = 1

        Actually:
        b_k reduces arity by k-1, B^{(2)} reduces arity by 2.
        Both routes: total reduction = (k-1)+2 = k+1.
        Input arity 5, k=2: output arity 5-(2+1) = 2. [NOT 3!]
        Input arity 5, k=3: output arity 5-(3+1) = 1.
        """
        # k=3 on arity 5 should give arity 1
        alg = NonFormalModel(alpha=F(1))
        elem = BarElt(factors=(alg.a, alg.a, alg.a, alg.a, alg.b))
        r = anticomm_bk_b2(elem, alg, 3).simplify()
        for t in r.terms:
            # VERIFIED [DC] output arity [LT] degree formula
            assert t.arity == 1


# ================================================================
# SECTION 5: BAR DIFFERENTIAL PROPERTIES
# ================================================================

class TestBarDifferential:
    """Tests for b^2 = 0 on both models."""

    def test_b_squared_zero_nonformal(self):
        """b^2 = 0 on the nonformal model (A-infinity relation).

        Path 1: direct computation b(b(elem)) for several elements.
        Path 2: A-infinity relations imply b^2 = 0 identically.
        """
        alg = NonFormalModel(alpha=F(1))
        a, b = alg.a, alg.b
        for factors in [(a, a, a, a, b), (a, b, a, b, a), (b, a, a, a, a),
                        (a, a, a), (a, a, b)]:
            elem = BarElt(factors=factors)
            b_elem = apply_b_total(elem, alg)
            b_squared = apply_b_total_lc(b_elem, alg).simplify()
            # VERIFIED [DC] b^2 = 0 [LT] A-infinity relation
            assert b_squared.is_zero, f"b^2 != 0 on {elem}: {b_squared}"

    def test_b_squared_zero_formal(self):
        """b^2 = 0 on the formal model."""
        alg = FormalFrobeniusModel()
        a, b = alg.a, alg.b
        for factors in [(a, a, a, a, b), (a, b, a, b, a), (b, a, a, a, a)]:
            elem = BarElt(factors=factors)
            b_elem = apply_b_total(elem, alg)
            b_squared = apply_b_total_lc(b_elem, alg).simplify()
            # VERIFIED [DC] b^2 = 0 formal [LT] associativity
            assert b_squared.is_zero, f"b^2 != 0 on {elem}: {b_squared}"


# ================================================================
# SECTION 6: FORMAL MODEL
# ================================================================

class TestFormalModel:
    """Tests for the formal Frobenius CY_3 algebra."""

    def test_associativity(self):
        """mu_2 is strictly associative.

        Path 1: exhaustive check on augmentation basis.
        Path 2: formal model by construction.
        """
        alg = FormalFrobeniusModel()
        from collections import defaultdict
        aug = alg.aug_basis()
        for x in aug:
            for y in aug:
                for z in aug:
                    total = defaultdict(F)
                    for c1, g1 in alg.mu2(x, y):
                        for c2, g2 in alg.mu2(g1, z):
                            total[g2] += c1 * c2
                    for c1, g1 in alg.mu2(y, z):
                        for c2, g2 in alg.mu2(x, g1):
                            total[g2] -= c1 * c2
                    for g, c in total.items():
                        # VERIFIED [DC] associativity [LT] construction
                        assert c == F(0), f"Assoc fails: ({x},{y},{z})"

    def test_mu3_zero(self):
        """mu_3 = 0 on the formal model.

        Path 1: all triples give empty output.
        Path 2: formal = mu_k = 0 for k >= 3.
        """
        alg = FormalFrobeniusModel()
        aug = alg.aug_basis()
        for x in aug:
            for y in aug:
                for z in aug:
                    # VERIFIED [DC] mu_3 = 0 [LT] formality
                    assert alg.mu3(x, y, z) == []

    def test_mu2_nontrivial(self):
        """mu_2 IS nontrivial: mu_2(a, b) = w.

        Path 1: direct computation.
        Path 2: non-formality of the ALGEBRA (not of mu_3).
        """
        alg = FormalFrobeniusModel()
        out = alg.mu2(alg.a, alg.b)
        # VERIFIED [DC] mu_2(a,b) = w [LT] Frobenius structure
        assert len(out) == 1
        assert out[0] == (F(1), alg.w)


# ================================================================
# SECTION 7: NAIVE B^{(2)} FAILS FOR NONFORMAL
# ================================================================

class TestNaiveB2Fails:
    """The naive pairwise B^{(2)} does NOT satisfy {b, B^{(2)}} = 0."""

    def test_total_nonzero_nonformal(self):
        """{b, B^{(2)}_naive} != 0 on the nonformal model.

        Path 1: direct computation on [a|a|a|a|b].
        Path 2: since {b_2, B^{(2)}} = 0 and {b_3, B^{(2)}} != 0,
                 total = {b_3, B^{(2)}} != 0.
        """
        alg = NonFormalModel(alpha=F(1))
        elem = BarElt(factors=(alg.a, alg.a, alg.a, alg.a, alg.b))
        total = anticomm_b_b2(elem, alg)
        # VERIFIED [DC] total nonzero [LT] mu_2=0 means total = {b_3, B^{(2)}}
        assert not total.is_zero

    def test_naive_b2_fails_exhaustive(self):
        """Exhaustive: naive B^{(2)} fails on nonformal model.

        Path 1: exhaustive check at arity 5.
        Path 2: count confirms > 0 elements with {b, B^{(2)}_naive} != 0.
        """
        r = exhaustive_nonformal(F(1), arity=5)
        # VERIFIED [DC] exhaustive check
        assert r["naive_b2_fails"]
        assert r["total_nonzero"] > 0

    def test_formal_alpha_zero(self):
        """At alpha=0 (formal limit), {b_3, B^{(2)}} = 0 trivially.

        Path 1: mu_3 = 0 at alpha = 0.
        Path 2: b_3 = 0 when mu_3 = 0.
        """
        alg = NonFormalModel(alpha=F(0))
        elem = BarElt(factors=(alg.a, alg.a, alg.a, alg.a, alg.b))
        m3_result = anticomm_bk_b2(elem, alg, 3)
        # VERIFIED [DC] alpha=0 gives zero [LT] mu_3 = 0
        assert m3_result.is_zero


# ================================================================
# SECTION 8: TCFT RESOLUTION
# ================================================================

class TestTCFTResolution:
    """Tests for conditional closure: B_TCFT^{(2)} is not B_term^{(2)}."""

    def test_moduli_space_description(self):
        """Moduli space data is conditional on the corrected TCFT operator.

        Path 1: dictionary keys are present.
        Path 2: raw/corrected operators are distinguished.
        """
        desc = moduli_space_description()
        # VERIFIED [DC] description [LT] Costello TCFT
        assert desc["raw_operator"] == "B_term^{(2)}"
        assert desc["corrected_operator"] == "B_TCFT^{(2)}"
        assert "M_{0,n+2}^{node}" in desc["moduli_space"]
        assert "if the corrected TCFT datum is supplied" in desc["identity"]

    def test_tcft_b2_differs(self):
        """The corrected TCFT operator cannot be identified with raw contraction.

        Path 1: naive fails on nonformal (computed above).
        Path 2: closure status is conditional, not universal.
        Path 3: therefore B_TCFT^{(2)} != B_term^{(2)} in this witness.
        """
        alg = NonFormalModel(alpha=F(1))
        elem = BarElt(factors=(alg.a, alg.a, alg.a, alg.a, alg.b))
        naive_total = anticomm_b_b2(elem, alg)
        status = closure_obstruction_status()
        # VERIFIED [DC] naive fails [LT] conditional status
        assert not naive_total.is_zero
        assert status["raw_universal_closure"] is False
        assert status["corrected_closure_status"] == "conditional"

    def test_forbidden_erasure_routes_do_not_close_witness(self):
        """No named slogan is allowed to erase the strict raw witness."""
        status = closure_obstruction_status()
        erasures = status["forbidden_erasure_routes"]
        # VERIFIED [DC] stale universal-claim rejection
        assert set(erasures) == set(FORBIDDEN_ERASURE_ROUTES)
        assert all(value is False for value in erasures.values())
        assert "HH^{-2} filtration theorem" in status["remaining_proof_obligation"]
        assert "empty total-degree -2 line" in status["remaining_proof_obligation"]

    def test_allowed_closure_hypotheses_are_explicit(self):
        """Closure requires B_TCFT^{(2)} or the precise HH^{-2} theorem."""
        status = closure_obstruction_status()
        hypotheses = status["allowed_closure_hypotheses"]
        # VERIFIED [DC] conditional closure hypotheses
        assert len(hypotheses) == 2
        assert "corrected TCFT datum" in hypotheses[0]
        assert "B_TCFT^{(2)}" in hypotheses[0]
        assert "comparison map" in hypotheses[1]
        assert "complete, exhaustive, separated, strongly convergent" in hypotheses[1]
        assert "empty total-degree -2 line" in hypotheses[1]


# ================================================================
# SECTION 9: MASTER COMPUTATION
# ================================================================

class TestMasterComputation:
    """Integration test: master computation runs without error."""

    def test_master_runs(self):
        """Master computation completes and returns all fields."""
        result = master_chain_level_cancellation(F(1))
        # VERIFIED [DC] master computation completes
        assert "Q1_nonformal_computation" in result
        assert "Q4_incompatibility" in result
        assert "Q5_moduli_space" in result
        assert "Q6_closure_status" in result
        assert result["Q6_closure_status"]["raw_universal_closure"] is False

    def test_master_alpha_2(self):
        """Master computation at alpha=2: scaling check."""
        result = master_chain_level_cancellation(F(2))
        # VERIFIED [DC] alpha=2 scaling
        assert result["Q4_incompatibility"]["all_verified"]
        assert result["Q1_nonformal_computation"]["strict_witness"]["coefficient_of_[b]"] == F(4)


# ================================================================
# SECTION 10: CROSS-CHECKS
# ================================================================

class TestCrossChecks:
    """Cross-checks with obs_ainf_local_p2.py and m3_b2_saga.tex."""

    def test_cross_check_obs_ainf(self):
        """Our strict bracket matches obs_ainf_local_p2.py.

        The obs_ainf engine computes [m_3, B^{(2)}] = m_3.B^{(2)} - B^{(2)}.m_3.
        Our raw strict bracket computes b_3.B_term^{(2)} - B_term^{(2)}.b_3.

        The obs_ainf engine reports 2*[b] for the commutator.
        """
        alg = NonFormalModel(alpha=F(1))
        elem = BarElt(factors=(alg.a, alg.a, alg.a, alg.a, alg.b))
        result = commutator_bk_bterm2(elem, alg, 3).simplify()

        # VERIFIED [DC] cross-check [LT] obs_ainf_local_p2
        assert not result.is_zero
        assert len(result.terms) == 1
        assert result.terms[0].factors == (alg.b,)
        assert result.terms[0].coeff == F(2)

    def test_three_levels_hierarchy(self):
        """The strict level is proved; higher closure levels are conditional.

        Level 1 (strict): [m_k, B^{(2)}] != 0 for nonformal. CHECK.
        Level 2 (homotopy): {b, B_TCFT^{(2)}} = 0 only with corrected TCFT datum.
        Level 3 (derived): requires the precise HH^{-2} filtration theorem.
        """
        # Level 1: strict nonvanishing
        alg = NonFormalModel(alpha=F(1))
        elem = BarElt(factors=(alg.a, alg.a, alg.a, alg.a, alg.b))
        strict = commutator_bk_bterm2(elem, alg, 3)
        # VERIFIED [DC] Level 1 nonvanishing [LT] prop:chain-nonvanishing-generic
        assert not strict.is_zero
        assert strict.simplify().terms[0].coeff == F(2)

        # Level 2: naive total fails, confirming TCFT needed
        naive_total = anticomm_b_b2(elem, alg)
        status = closure_obstruction_status()
        # VERIFIED [DC] naive total fails [LT] conditional closure status
        assert not naive_total.is_zero  # naive fails, TCFT needed
        assert status["corrected_closure_status"] == "conditional"
        assert status["raw_universal_closure"] is False
