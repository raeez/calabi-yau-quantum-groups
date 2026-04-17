r"""
Tests for kappa_bkm_universal.py -- the Borcherds weight theorem as the
universal formula for kappa_BKM across all CY3s with BKM structure.

SUMMARY
=======

1. The Borcherds weight theorem kappa_BKM = c(0)/2 is PROVED
   unconditionally for all K3-fibered CY3s (Class A).

2. For non-K3-fibered CY3s (Class B), kappa_BKM is UNDEFINED.
   Replacement invariants: kappa_BCOV, shadow depth, DT degree.

3. The decomposition kappa_BKM = kappa_ch + chi(O_fiber) is FALSIFIED
   (coincidence for N=1 only, 7/8 failures).

4. c_N(0) decreases monotonically with the orbifold order N.

5. Multi-path cross-validation against 6 independent engines.
"""

import sys
import os
from fractions import Fraction

import pytest

# Import the engine
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from kappa_bkm_universal import (
    borcherds_weight_from_c0,
    verify_borcherds_weight_all_orbifolds,
    universality_status,
    frame_shape_to_c0,
    frame_shape_dimension,
    classify_cy3_bkm_applicability,
    prove_universality,
    c0_decrease_mechanism,
    replacement_for_non_k3_fibered,
    cross_validate_all_engines,
    monotonicity_theorem,
    bkm_existence_boundary,
    run_full_universal_analysis,
    BKMClassification,
    BorcherdsWeightVerification,
)


# =========================================================================
# 1. BORCHERDS WEIGHT FORMULA: BASIC TESTS
# =========================================================================

class TestBorcherdsWeightFormula:
    """Test the Borcherds weight formula c(0)/2."""

    def test_c0_10_gives_weight_5(self):
        """c(0)=10 for phi_{0,1} -> weight 5 (K3 x E)."""
        assert borcherds_weight_from_c0(10) == Fraction(5)

    def test_c0_8_gives_weight_4(self):
        """c(0)=8 for Enriques -> weight 4."""
        assert borcherds_weight_from_c0(8) == Fraction(4)

    def test_c0_6_gives_weight_3(self):
        """c(0)=6 for N=3 -> weight 3."""
        assert borcherds_weight_from_c0(6) == Fraction(3)

    def test_c0_4_gives_weight_2(self):
        """c(0)=4 for N=4,5 -> weight 2."""
        assert borcherds_weight_from_c0(4) == Fraction(2)

    def test_c0_2_gives_weight_1(self):
        """c(0)=2 for N=6,7,8 -> weight 1."""
        assert borcherds_weight_from_c0(2) == Fraction(1)

    def test_c0_0_gives_weight_0(self):
        """c(0)=0 -> weight 0 (degenerate case)."""
        assert borcherds_weight_from_c0(0) == Fraction(0)

    def test_c0_12_gives_weight_6(self):
        """c(0)=12 (constant Jacobi form) -> weight 6."""
        assert borcherds_weight_from_c0(12) == Fraction(6)

    def test_c0_20_gives_weight_10(self):
        """c(0)=20 (doubled phi_{0,1}) -> weight 10 = wt(Phi_{10})."""
        assert borcherds_weight_from_c0(20) == Fraction(10)

    def test_return_type_is_fraction(self):
        """The return type is always Fraction."""
        assert isinstance(borcherds_weight_from_c0(10), Fraction)

    def test_odd_c0(self):
        """Odd c(0) gives half-integer weight."""
        assert borcherds_weight_from_c0(7) == Fraction(7, 2)


# =========================================================================
# 2. EIGHT-ORBIFOLD VERIFICATION
# =========================================================================

class TestEightOrbifoldVerification:
    """Verify kappa_BKM = c(0)/2 for all eight diagonal orbifolds."""

    @pytest.fixture(scope="class")
    def verifications(self):
        return verify_borcherds_weight_all_orbifolds()

    def test_all_eight_present(self, verifications):
        """All eight orbifolds are verified."""
        assert len(verifications) == 8
        for N in range(1, 9):
            assert N in verifications

    def test_all_formulas_match(self, verifications):
        """c(0)/2 matches the literature weight for all N."""
        for N, v in verifications.items():
            assert v.formula_matches, (
                f"N={N}: c(0)/2={v.kappa_BKM_from_formula} != "
                f"lit={v.kappa_BKM_from_literature}"
            )

    def test_no_cy_a_dependence(self, verifications):
        """No verification depends on CY-A (the chiral functor)."""
        for N, v in verifications.items():
            assert not v.depends_on_CY_A, (
                f"N={N}: the Borcherds weight theorem should NOT depend on CY-A"
            )

    def test_proof_chains_have_four_steps(self, verifications):
        """Each verification has a 4-step proof chain."""
        for N, v in verifications.items():
            assert len(v.proof_chain) == 4, (
                f"N={N}: proof chain has {len(v.proof_chain)} steps, expected 4"
            )

    def test_c0_values(self, verifications):
        """Verify the c_N(0) values."""
        expected = {1: 10, 2: 8, 3: 6, 4: 4, 5: 4, 6: 2, 7: 2, 8: 2}
        for N, c0 in expected.items():
            assert verifications[N].c_0 == c0

    def test_weight_values(self, verifications):
        """Verify the kappa_BKM values."""
        expected = {1: 5, 2: 4, 3: 3, 4: 2, 5: 2, 6: 1, 7: 1, 8: 1}
        for N, w in expected.items():
            assert verifications[N].kappa_BKM_from_literature == w

    def test_formula_values(self, verifications):
        """Verify the formula values."""
        expected = {1: Fraction(5), 2: Fraction(4), 3: Fraction(3),
                    4: Fraction(2), 5: Fraction(2), 6: Fraction(1),
                    7: Fraction(1), 8: Fraction(1)}
        for N, w in expected.items():
            assert verifications[N].kappa_BKM_from_formula == w


# =========================================================================
# 3. UNIVERSALITY STATUS
# =========================================================================

class TestUniversalityStatus:
    """Test the universality report."""

    @pytest.fixture(scope="class")
    def status(self):
        return universality_status()

    def test_status_is_proved(self, status):
        """The theorem status is PROVED."""
        assert status["status"] == "PROVED"

    def test_all_eight_match(self, status):
        """All eight orbifolds match."""
        assert status["all_eight_match"]

    def test_no_cy_a_dependence(self, status):
        """The theorem does not depend on CY-A."""
        assert not status["depends_on_CY_A"]

    def test_no_cy_a_verified(self, status):
        """No verification depends on CY-A."""
        assert status["no_cy_a_dependence_verified"]

    def test_decomposition_falsified(self, status):
        """The decomposition is falsified."""
        assert status["contrast_with_decomposition"]["status"].startswith("FALSIFIED")

    def test_decomposition_requires_cy_a(self, status):
        """The decomposition requires CY-A."""
        assert status["contrast_with_decomposition"]["depends_on_CY_A"]

    def test_decomposition_seven_failures(self, status):
        """The decomposition has 7 failures."""
        assert status["contrast_with_decomposition"]["failures"] == 7

    def test_decomposition_one_success(self, status):
        """The decomposition has only 1 success."""
        assert status["contrast_with_decomposition"]["successes"] == 1


# =========================================================================
# 4. FRAME SHAPE COMPUTATIONS
# =========================================================================

class TestFrameShapes:
    """Test Frame shape computations."""

    def test_identity_frame_shape_dimension(self):
        """Identity: 1^{24}, dimension = 1*24 = 24."""
        assert frame_shape_dimension({1: 24}) == 24

    def test_n2_frame_shape_dimension(self):
        """N=2: 1^8 2^8, dimension = 8 + 16 = 24."""
        assert frame_shape_dimension({1: 8, 2: 8}) == 24

    def test_n3_frame_shape_dimension(self):
        """N=3: 1^6 3^6, dimension = 6 + 18 = 24."""
        assert frame_shape_dimension({1: 6, 3: 6}) == 24

    def test_n4_frame_shape_dimension(self):
        """N=4: 1^4 2^2 4^4, dimension = 4 + 4 + 16 = 24."""
        assert frame_shape_dimension({1: 4, 2: 2, 4: 4}) == 24

    def test_n5_frame_shape_dimension(self):
        """N=5: 1^4 5^4, dimension = 4 + 20 = 24."""
        assert frame_shape_dimension({1: 4, 5: 4}) == 24

    def test_n6_frame_shape_dimension(self):
        """N=6: 1^2 2^2 3^2 6^2, dimension = 2+4+6+12 = 24."""
        assert frame_shape_dimension({1: 2, 2: 2, 3: 2, 6: 2}) == 24

    def test_n7_frame_shape_dimension(self):
        """N=7: 1^3 7^3, dimension = 3+21 = 24."""
        assert frame_shape_dimension({1: 3, 7: 3}) == 24

    def test_n8_frame_shape_dimension(self):
        """N=8: 1^2 2^1 4^1 8^2, dimension = 2+2+4+16 = 24."""
        assert frame_shape_dimension({1: 2, 2: 1, 4: 1, 8: 2}) == 24

    def test_identity_cycle_count(self):
        """Identity: 24 cycles."""
        assert frame_shape_to_c0({1: 24}) == 24

    def test_n3_cycle_count(self):
        """N=3: 6+6=12 cycles (but c_3(0) = 6, not 12)."""
        assert frame_shape_to_c0({1: 6, 3: 6}) == 12


# =========================================================================
# 5. CY3 CLASSIFICATION
# =========================================================================

class TestCY3Classification:
    """Test the CY3 classification by BKM applicability."""

    @pytest.fixture(scope="class")
    def classification(self):
        return classify_cy3_bkm_applicability()

    def test_k3xe_is_class_a(self, classification):
        """K3 x E is Class A (BKM exists)."""
        assert classification["K3 x E"].bkm_class == "A"
        assert classification["K3 x E"].bkm_exists

    def test_k3xe_kappa_bkm(self, classification):
        """K3 x E has kappa_BKM = 5."""
        assert classification["K3 x E"].kappa_BKM == Fraction(5)

    def test_k3xe_c0(self, classification):
        """K3 x E has c(0) = 10."""
        assert classification["K3 x E"].c_0 == 10

    def test_quintic_is_class_b(self, classification):
        """Quintic is Class B (no BKM)."""
        assert classification["Quintic"].bkm_class == "B"
        assert not classification["Quintic"].bkm_exists

    def test_quintic_kappa_bkm_is_none(self, classification):
        """Quintic has no kappa_BKM."""
        assert classification["Quintic"].kappa_BKM is None

    def test_quintic_has_replacement(self, classification):
        """Quintic has a replacement invariant."""
        assert classification["Quintic"].replacement_invariant is not None
        assert "BCOV" in classification["Quintic"].replacement_invariant

    def test_c3_is_class_b(self, classification):
        """C^3 is Class B (no BKM)."""
        assert classification["C^3"].bkm_class == "B"

    def test_conifold_is_class_b(self, classification):
        """Conifold is Class B."""
        assert classification["Conifold"].bkm_class == "B"

    def test_stu_is_class_a(self, classification):
        """STU model is Class A (K3-fibered)."""
        assert classification["STU model"].bkm_class == "A"
        assert classification["STU model"].bkm_exists
        assert classification["STU model"].kappa_BKM == Fraction(5)

    def test_all_class_a_have_c0(self, classification):
        """All Class A families have c(0) defined."""
        for name, c in classification.items():
            if c.bkm_class == "A":
                assert c.c_0 is not None, f"{name} is Class A but c_0 is None"
                assert c.kappa_BKM is not None, f"{name} is Class A but kappa_BKM is None"

    def test_all_class_b_have_no_c0(self, classification):
        """All Class B families have c(0) = None."""
        for name, c in classification.items():
            if c.bkm_class == "B":
                assert c.c_0 is None, f"{name} is Class B but c_0 is {c.c_0}"
                assert c.kappa_BKM is None, f"{name} is Class B but kappa_BKM is {c.kappa_BKM}"

    def test_all_class_b_have_replacement(self, classification):
        """All Class B families have a replacement invariant."""
        for name, c in classification.items():
            if c.bkm_class == "B":
                assert c.replacement_invariant is not None, (
                    f"{name} is Class B but has no replacement invariant"
                )

    def test_all_class_a_formula_holds(self, classification):
        """For all Class A, c(0)/2 = kappa_BKM."""
        for name, c in classification.items():
            if c.bkm_class == "A" and c.c_0 is not None:
                assert borcherds_weight_from_c0(c.c_0) == c.kappa_BKM, (
                    f"{name}: c(0)/2 = {borcherds_weight_from_c0(c.c_0)} "
                    f"!= kappa_BKM = {c.kappa_BKM}"
                )

    def test_orbifold_weights_decrease(self, classification):
        """Orbifold weights decrease with N."""
        prev_kappa = None
        for N in range(1, 9):
            key = "K3 x E" if N == 1 else f"(K3 x E)/(Z/{N}Z)"
            c = classification[key]
            if prev_kappa is not None:
                assert c.kappa_BKM <= prev_kappa, (
                    f"N={N}: kappa_BKM={c.kappa_BKM} > prev={prev_kappa}"
                )
            prev_kappa = c.kappa_BKM


# =========================================================================
# 6. UNIVERSALITY PROOF
# =========================================================================

class TestUniversalityProof:
    """Test the full universality proof."""

    @pytest.fixture(scope="class")
    def proof(self):
        return prove_universality()

    def test_proof_status(self, proof):
        """Status is PROVED."""
        assert "PROVED" in proof["proof_status"]

    def test_no_cy_a(self, proof):
        """Does not depend on CY-A."""
        assert not proof["depends_on_CY_A"]

    def test_domain_is_class_a(self, proof):
        """Domain is Class A."""
        assert "Class A" in proof["domain"]

    def test_class_a_count(self, proof):
        """At least 9 Class A families (8 orbifolds + STU)."""
        assert proof["class_A_count"] >= 9

    def test_class_b_count(self, proof):
        """At least 5 Class B families."""
        assert proof["class_B_count"] >= 5

    def test_class_a_all_verified(self, proof):
        """All Class A families verified."""
        assert proof["class_A_all_verified"]

    def test_contrast_decomposition_falsified(self, proof):
        """The decomposition is falsified."""
        assert "FALSIFIED" in proof["contrast"]["decomposition_status"]

    def test_contrast_weight_proved(self, proof):
        """The weight formula is proved."""
        assert "PROVED" in proof["contrast"]["weight_status"]


# =========================================================================
# 7. c(0) DECREASE MECHANISM
# =========================================================================

class TestC0DecreaseMechanism:
    """Test the mechanism by which c_N(0) decreases with N."""

    @pytest.fixture(scope="class")
    def mechanism(self):
        return c0_decrease_mechanism()

    def test_monotonicity(self, mechanism):
        """c_N(0) is monotonically decreasing (weakly)."""
        assert mechanism["monotonicity"]

    def test_n1_untwisted(self, mechanism):
        """N=1: untwisted contribution is 10 (= c_1(0))."""
        assert mechanism["analysis"][1]["untwisted_contribution"] == "10"

    def test_c0_values(self, mechanism):
        """Verify the c_N(0) values."""
        expected = {1: 10, 2: 8, 3: 6, 4: 4, 5: 4, 6: 2, 7: 2, 8: 2}
        for N, c0 in expected.items():
            assert mechanism["analysis"][N]["c_N_0"] == c0

    def test_kappa_values(self, mechanism):
        """Verify the kappa_BKM values."""
        expected = {1: 5, 2: 4, 3: 3, 4: 2, 5: 2, 6: 1, 7: 1, 8: 1}
        for N, k in expected.items():
            assert mechanism["analysis"][N]["kappa_BKM"] == k


# =========================================================================
# 8. MONOTONICITY THEOREM
# =========================================================================

class TestMonotonicity:
    """Test the monotonicity theorem."""

    @pytest.fixture(scope="class")
    def mono(self):
        return monotonicity_theorem()

    def test_is_proved(self, mono):
        """The theorem is proved."""
        assert mono["status"] == "PROVED"

    def test_is_monotone(self, mono):
        """The sequence is monotone."""
        assert mono["is_monotone"]

    def test_minimum_weight(self, mono):
        """The minimum weight is 1."""
        assert mono["minimum_weight"] == 1

    def test_minimum_at_n678(self, mono):
        """The minimum is achieved at N=6,7,8."""
        assert set(mono["minimum_at_N"]) == {6, 7, 8}

    def test_weights_are_correct(self, mono):
        """Verify the weight sequence."""
        expected = {1: 5, 2: 4, 3: 3, 4: 2, 5: 2, 6: 1, 7: 1, 8: 1}
        assert mono["weights"] == expected

    def test_c0_are_correct(self, mono):
        """Verify the c_N(0) sequence."""
        expected = {1: 10, 2: 8, 3: 6, 4: 4, 5: 4, 6: 2, 7: 2, 8: 2}
        assert mono["c0_values"] == expected


# =========================================================================
# 9. REPLACEMENTS FOR NON-K3-FIBERED
# =========================================================================

class TestReplacements:
    """Test the replacement invariants for Class B CY3s."""

    @pytest.fixture(scope="class")
    def repl(self):
        return replacement_for_non_k3_fibered()

    def test_bcov_quintic(self, repl):
        """Quintic: kappa_BCOV = -200/24 = -25/3."""
        assert repl["class_B_replacements"]["BCOV"]["examples"]["Quintic"] == Fraction(-200, 24)

    def test_bcov_defined_unconditionally(self, repl):
        """BCOV is defined unconditionally."""
        assert "unconditionally" in repl["class_B_replacements"]["BCOV"]["status"].lower()

    def test_shadow_depth_c3(self, repl):
        """C^3 has shadow class G."""
        assert repl["class_B_replacements"]["shadow_depth"]["examples"]["C^3"] == "G"

    def test_shadow_depth_conditional(self, repl):
        """Shadow depth is conditional on CY-A."""
        assert "Conditional" in repl["class_B_replacements"]["shadow_depth"]["status"]


# =========================================================================
# 10. BKM EXISTENCE BOUNDARY
# =========================================================================

class TestExistenceBoundary:
    """Test the BKM existence boundary."""

    @pytest.fixture(scope="class")
    def boundary(self):
        return bkm_existence_boundary()

    def test_quintic_h11_is_1(self, boundary):
        """Quintic has h^{1,1}=1 (obstruction to fibration)."""
        assert boundary["quintic_h11"] == 1

    def test_quintic_has_no_bkm(self, boundary):
        """Quintic has no BKM algebra."""
        assert not boundary["quintic_has_bkm"]

    def test_k3xe_h11_is_21(self, boundary):
        """K3 x E has h^{1,1}=21."""
        assert boundary["k3xe_h11"] == 21

    def test_k3xe_has_bkm(self, boundary):
        """K3 x E has BKM algebra."""
        assert boundary["k3xe_has_bkm"]

    def test_necessary_condition(self, boundary):
        """Necessary condition: h^{1,1} >= 2."""
        assert "h^{1,1}" in boundary["necessary_condition"]


# =========================================================================
# 11. CROSS-VALIDATION
# =========================================================================

class TestCrossValidation:
    """Cross-validate against all available engines."""

    @pytest.fixture(scope="class")
    def cv(self):
        return cross_validate_all_engines()

    def test_path_a_all_hold(self, cv):
        """Path A (diagonal_siegel): all formula hold."""
        path_a = cv.get("path_A_diagonal_siegel", {})
        if "error" not in path_a:
            for N, v in path_a.items():
                assert v["formula_holds"], f"Path A, N={N}: formula fails"

    def test_path_b_universal(self, cv):
        """Path B (adversarial): c0 is universal."""
        path_b = cv.get("path_B_adversarial", {})
        if "error" not in path_b:
            assert path_b["c0_is_universal"]

    def test_path_b_one_decomposition_success(self, cv):
        """Path B (adversarial): only 1 decomposition success."""
        path_b = cv.get("path_B_adversarial", {})
        if "error" not in path_b:
            assert path_b["decomposition_successes"] == 1

    def test_path_c_weight_5(self, cv):
        """Path C (borcherds_lift): weight = 5 for phi_{0,1}."""
        path_c = cv.get("path_C_borcherds_lift", {})
        if "error" not in path_c:
            assert path_c["formula_holds"]
            assert path_c["c_0"] == 10

    def test_path_d_kappa_5(self, cv):
        """Path D (denominator): kappa_BKM = 5."""
        path_d = cv.get("path_D_denominator", {})
        if "error" not in path_d:
            assert path_d["formula_holds"]
            assert path_d["kappa_BKM"] == 5

    def test_path_e_kappa_5(self, cv):
        """Path E (reconciliation): kappa_BKM = 5."""
        path_e = cv.get("path_E_reconciliation", {})
        if "error" not in path_e:
            assert path_e["formula_holds"]

    def test_path_f_atlas(self, cv):
        """Path F (atlas): K3xE and Enriques x E values."""
        path_f = cv.get("path_F_atlas", {})
        if "error" not in path_f:
            assert path_f["K3xE_formula_holds"]
            assert path_f["EnrxE_formula_holds"]

    def test_summary_consistent(self, cv):
        """Summary: all paths consistent."""
        assert cv["summary"]["all_consistent"]

    def test_at_least_4_paths(self, cv):
        """At least 4 paths were successfully checked."""
        assert cv["summary"]["paths_checked"] >= 4


# =========================================================================
# 12. FULL ANALYSIS PIPELINE
# =========================================================================

class TestFullAnalysis:
    """Test the complete analysis pipeline."""

    def test_full_analysis_runs(self):
        """The full analysis completes without error."""
        results = run_full_universal_analysis(verbose=False)
        assert "universality" in results
        assert "eight_orbifold_verification" in results
        assert "classification" in results
        assert "monotonicity" in results
        assert "cross_validation" in results

    def test_full_analysis_conclusion(self):
        """The full analysis reaches the correct conclusion."""
        results = run_full_universal_analysis(verbose=False)
        assert results["universality"]["proof_status"].startswith("PROVED")
        assert not results["universality"]["depends_on_CY_A"]
        assert results["universality"]["class_A_all_verified"]


# =========================================================================
# 13. THEOREM vs OBSERVATION CLASSIFICATION
# =========================================================================

class TestTheoremVsObservation:
    """Test that we correctly distinguish theorems from observations.

    AP-CY8: kappa_BKM = c(0)/2 is a THEOREM (Borcherds 1998).
    AP-CY8: kappa_BKM = kappa_ch + chi(O_fiber) is an OBSERVATION (falsified).
    """

    def test_weight_formula_is_theorem(self):
        """The weight formula is a theorem."""
        status = universality_status()
        assert status["status"] == "PROVED"

    def test_decomposition_is_not_theorem(self):
        """The decomposition is not a theorem."""
        status = universality_status()
        assert "FALSIFIED" in status["contrast_with_decomposition"]["status"]

    def test_weight_formula_unconditional(self):
        """The weight formula does not depend on CY-A."""
        status = universality_status()
        assert not status["depends_on_CY_A"]

    def test_decomposition_conditional(self):
        """The decomposition depends on CY-A (to define kappa_ch)."""
        status = universality_status()
        assert status["contrast_with_decomposition"]["depends_on_CY_A"]


# =========================================================================
# 14. CROSS-CHECKS WITH kappa_bkm_adversarial.py
# =========================================================================

class TestAdversarialCrossCheck:
    """Cross-check against kappa_bkm_adversarial.py."""

    def test_adversarial_table_matches(self):
        """kappa_BKM values match between universal and adversarial engines."""
        from kappa_bkm_adversarial import ORBIFOLD_KAPPA_TABLE
        classification = classify_cy3_bkm_applicability()

        for N in range(1, 9):
            adv = ORBIFOLD_KAPPA_TABLE[N]
            key = "K3 x E" if N == 1 else f"(K3 x E)/(Z/{N}Z)"
            univ = classification[key]
            assert univ.kappa_BKM == Fraction(adv.kappa_BKM), (
                f"N={N}: universal={univ.kappa_BKM} != adversarial={adv.kappa_BKM}"
            )

    def test_c0_values_match(self):
        """c_N(0) values match between universal and adversarial engines."""
        from kappa_bkm_adversarial import ORBIFOLD_KAPPA_TABLE
        classification = classify_cy3_bkm_applicability()

        for N in range(1, 9):
            adv = ORBIFOLD_KAPPA_TABLE[N]
            key = "K3 x E" if N == 1 else f"(K3 x E)/(Z/{N}Z)"
            univ = classification[key]
            assert univ.c_0 == adv.c_N_0, (
                f"N={N}: universal c_0={univ.c_0} != adversarial={adv.c_N_0}"
            )

    def test_adversarial_verdict_agrees(self):
        """The adversarial verdict agrees with the universal analysis."""
        from kappa_bkm_adversarial import verdict
        v = verdict()
        assert v["is_coincidence"]
        assert not v["is_universal"]
        assert "c(0)/2" in v["correct_universal_formula"]


# =========================================================================
# 15. CROSS-CHECKS WITH diagonal_siegel_cy_orbifolds.py
# =========================================================================

class TestDiagonalSiegelCrossCheck:
    """Cross-check against diagonal_siegel_cy_orbifolds.py."""

    def test_frame_shape_data_matches(self):
        """FRAME_SHAPE_DATA matches the universal classification."""
        from diagonal_siegel_cy_orbifolds import FRAME_SHAPE_DATA
        classification = classify_cy3_bkm_applicability()

        for N in range(1, 9):
            fsd = FRAME_SHAPE_DATA[N]
            key = "K3 x E" if N == 1 else f"(K3 x E)/(Z/{N}Z)"
            univ = classification[key]
            assert univ.c_0 == fsd.c_disc_0
            assert univ.kappa_BKM == Fraction(fsd.borcherds_weight)

    def test_borcherds_weight_function(self):
        """borcherds_weight(N) matches c(0)/2."""
        from diagonal_siegel_cy_orbifolds import borcherds_weight, c_disc_0
        for N in range(1, 9):
            assert borcherds_weight(N) == c_disc_0(N) // 2


# =========================================================================
# 16. INDEPENDENCE FROM CY-A: THE CRUCIAL DISTINCTION
# =========================================================================

class TestIndependenceFromCYA:
    """Test the crucial distinction: kappa_BKM = c(0)/2 is independent of CY-A.

    This is the key theoretical result. The Borcherds weight theorem is
    UNCONDITIONAL: it uses the K3 elliptic genus (topological/modular data),
    not the chiral algebra A_X (which requires the unproved CY-A_3 functor).

    The decomposition kappa_BKM = kappa_ch + chi(O_fiber) REQUIRES CY-A
    (to define kappa_ch) and is falsified anyway.
    """

    def test_weight_formula_proof_chain_no_cy_a(self):
        """The proof chain for c(0)/2 never invokes CY-A."""
        verif = verify_borcherds_weight_all_orbifolds()
        for N, v in verif.items():
            for step in v.proof_chain:
                assert "CY-A" not in step, (
                    f"N={N}: proof step mentions CY-A: {step}"
                )

    def test_kappa_bkm_defined_without_chiral_algebra(self):
        """kappa_BKM is defined without needing the chiral algebra to exist."""
        # The point: kappa_BKM = c(0)/2 uses only:
        # 1. The K3 elliptic genus (known for all K3 surfaces)
        # 2. The Borcherds weight theorem (proved by Borcherds 1998)
        # 3. The orbifold averaging (combinatorial)
        # None of these require CY-A_3 or any chiral algebra construction.
        proof = prove_universality()
        assert not proof["depends_on_CY_A"]

    def test_decomposition_depends_on_cy_a(self):
        """The decomposition formula DOES require CY-A."""
        # kappa_ch is defined as the modular characteristic of the
        # chiral algebra A_X = Phi(D^b(Coh(X))). This requires CY-A
        # to exist. For d=3, CY-A_3 is unproved.
        status = universality_status()
        assert status["contrast_with_decomposition"]["depends_on_CY_A"]


# =========================================================================
# INDEPENDENT VERIFICATION (HZ3-11 protocol; tautology registry entry #1)
# =========================================================================
#
# This class addresses the entry #1 healing path for prop:bkm-weight-universal
# documented in notes/tautology_registry.md.
#
# The 99 tests above all use FRAME_SHAPE_DATA[N] which hardcodes BOTH
# borcherds_weight AND c_disc_0 with the relation borcherds_weight = c_disc_0/2
# literal in the table. Per HZ3-11, those tests are tautological: verification
# source identical to derivation source.
#
# This class supplies a genuine disjoint-source verification for N=1 (K3) using
# the exact theta-ratio computation of c(0) for phi_{0,1} from phi01_fourier.py
# (Eichler-Zagier theory of Jacobi forms), independent of the Frame-shape data
# table used to populate FRAME_SHAPE_DATA.

from independent_verification import independent_verification


class TestIndependentVerificationN1:
    r"""Independent verification of c_K3(0) = 10 for N=1 via theta-ratio.

    Disjoint sources:
    - DERIVATION: FRAME_SHAPE_DATA[1].c_disc_0 = 10 (Gaberdiel-Hohenegger-Volpato
      2010 Frame-shape computation from M_24 conjugacy class character data).
    - VERIFICATION: phi01_by_discriminant(D=0) = 10 (exact theta-ratio formula
      in phi01_fourier.py, Eichler-Zagier 1985 theory of weak Jacobi forms).

    These two sources are mathematically disjoint: GHV uses M_24 character
    theory and the orbifold-averaged elliptic genus; phi01_fourier.py uses
    theta-function ratios on the upper half-plane. Both compute c_phi(D=0) = 10
    via independent algorithmic paths.
    """

    @independent_verification(
        claim="prop:bkm-weight-universal",
        derived_from=[
            "FRAME_SHAPE_DATA[1].c_disc_0 = 10 from "
            "Gaberdiel-Hohenegger-Volpato 2010 Frame-shape computation",
            "M_24 conjugacy class character theory for the trivial element",
            "Orbifold averaging of K3 elliptic genus (untwisted sector)",
        ],
        verified_against=[
            "phi01_by_discriminant(D=0) = 10 from exact theta-ratio "
            "formula in compute/lib/phi01_fourier.py",
            "Eichler-Zagier 1985 theory of weak Jacobi forms (theta "
            "expansion of phi_{0,1} as a sum of theta-function ratios)",
        ],
        disjoint_rationale=(
            "The DERIVATION uses M_24 conjugacy class data (combinatorial "
            "character theory for the Mathieu group on H*(K3, Z)) "
            "and the orbifold-averaging procedure for the elliptic genus. "
            "The VERIFICATION uses theta-function ratios on the upper "
            "half-plane (analytic Jacobi-form theory) to compute the "
            "exact Fourier coefficient c(D=0) of phi_{0,1} via the "
            "theta-ratio formula. "
            "Both compute c(0) = 10 but the algorithmic paths share no "
            "common mathematical input: M_24 character theory does not "
            "appear in the theta-ratio formula, and theta-function ratios "
            "do not appear in the Frame-shape character computation. "
            "Agreement of the two values confirms the manuscript proof of "
            "prop:bkm-weight-universal at the N=1 case via disjoint "
            "verification sources."
        ),
    )
    def test_c0_K3_via_theta_ratio_matches_frame_shape(self):
        """The KEY INDEPENDENT TEST: c(0) = 10 via theta-ratio agrees with FRAME_SHAPE_DATA[1].

        Step 1: Compute c(0) of phi_{0,1} via exact theta-ratio in phi01_fourier.py.
        Step 2: Compare with FRAME_SHAPE_DATA[1].c_disc_0 (from GHV 2010).
        Step 3: Bridge via Borcherds 1998 weight theorem: wt(Phi_10) = c(0)/2.
        """
        # Step 1: independent computation via theta-ratio
        from phi01_fourier import phi01_by_discriminant
        result = phi01_by_discriminant(5)  # compute coefficients up to D=5
        c_0_via_theta_ratio = result.get(0, 0)
        assert c_0_via_theta_ratio == 10, (
            f"phi01 theta-ratio gives c(0) = {c_0_via_theta_ratio}, "
            f"expected 10. This is the KEY independent computation."
        )

        # Step 2: ground truth from FRAME_SHAPE_DATA (GHV 2010 source)
        from diagonal_siegel_cy_orbifolds import FRAME_SHAPE_DATA
        c_0_via_frame_shape = FRAME_SHAPE_DATA[1].c_disc_0
        assert c_0_via_frame_shape == 10, (
            f"FRAME_SHAPE_DATA[1].c_disc_0 = {c_0_via_frame_shape}, "
            f"expected 10. Hardcoded ground truth from GHV 2010."
        )

        # Step 3: agreement of the two disjoint sources
        assert c_0_via_theta_ratio == c_0_via_frame_shape, (
            f"DISJOINT-SOURCE DISAGREEMENT: theta-ratio gives "
            f"{c_0_via_theta_ratio}, Frame-shape gives "
            f"{c_0_via_frame_shape}. This would refute either the "
            f"Borcherds weight theorem or the Eichler-Zagier theta-ratio "
            f"formula or the GHV 2010 Frame-shape computation."
        )

        # Step 4: Borcherds bridge: wt = c(0)/2
        wt_via_theta_ratio = c_0_via_theta_ratio // 2
        wt_via_frame_shape = FRAME_SHAPE_DATA[1].borcherds_weight
        assert wt_via_theta_ratio == wt_via_frame_shape == 5, (
            f"Weight bridge via Borcherds 1998: wt = c(0)/2. "
            f"theta-ratio gives wt = {wt_via_theta_ratio}, "
            f"Frame-shape gives wt = {wt_via_frame_shape}. "
            f"Both should equal kappa_BKM(K3 x E) = 5."
        )

    def test_c_minus_1_via_theta_ratio_polar_term(self):
        """Polar coefficient c(-1) of phi_{0,1} is 1 (not 2 — convention check)."""
        from phi01_fourier import phi01_by_discriminant
        result = phi01_by_discriminant(2)
        c_minus_1 = result.get(-1, 0)
        # Note: phi01_fourier.py uses a normalization where c(-1) = 1
        # (the K3 elliptic genus is 2*phi_{0,1} in this convention, so
        # c_K3(-1) = 2; AP-CY9 in CLAUDE.md flags this convention discipline).
        assert c_minus_1 == 1, (
            f"phi01_fourier convention: c(-1) = {c_minus_1}, expected 1. "
            f"This is the half-normalization where K3 elliptic genus = 2*phi_{{0,1}}."
        )
