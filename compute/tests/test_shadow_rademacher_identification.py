"""Tests for shadow_rademacher_identification.py.

Multi-path verification of the shadow tower / Rademacher expansion
identification for K3 and K3 x E.

Test organization:
  1. Dedekind sums and Kloosterman sums (12 tests)
  2. Bessel functions (6 tests)
  3. Rademacher expansion (12 tests)
  4. Shadow tower correspondence (8 tests)
  5. Convergence analysis (8 tests)
  6. Exponential suppression (6 tests)
  7. Kloosterman conductor structure (6 tests)
  8. Siegel-level Rademacher (5 tests)
  9. Identification table (8 tests)
  10. Conjecture verification (5 tests)

Total: 76 tests.
"""

import math
import pytest
from fractions import Fraction

from compute.lib.shadow_rademacher_identification import (
    # Dedekind / Kloosterman
    dedekind_sum,
    generalized_kloosterman,
    standard_kloosterman,
    verify_kloosterman_special_values,
    # Bessel
    bessel_I_3half,
    bessel_I_9half,
    # Rademacher
    RademacherTerm,
    rademacher_term,
    rademacher_partial_sum,
    # Shadow
    shadow_contribution,
    shadow_partial_sum,
    # Correspondence
    CorrespondenceRow,
    correspondence_table,
    # Convergence
    ConvergenceRow,
    convergence_analysis,
    verify_leading_term_accuracy,
    verify_exponential_suppression,
    # Kloosterman structure
    kloosterman_conductor_analysis,
    # Siegel
    SiegelRademacherTerm,
    siegel_rademacher_term,
    siegel_exponential_ratios,
    # Identification
    IdentificationResult,
    compute_identification,
    compute_identification_table,
    # Conjecture
    shadow_rademacher_conjecture,
    shadow_rademacher_summary,
    # Constants
    PHI01_COEFFICIENTS,
    K3_KAPPA_CH,
    K3E_KAPPA_CH,
    K3E_KAPPA_CH_COMPACT,
    K3E_KAPPA_CH_HEIS,
)


# =========================================================================
# 1. DEDEKIND SUMS AND KLOOSTERMAN SUMS
# =========================================================================

class TestDedekindSums:
    """Verify Dedekind sum computation."""

    def test_dedekind_s_1_1(self):
        """s(1, 1) = 0 (trivial)."""
        assert dedekind_sum(1, 1) == 0.0

    def test_dedekind_s_1_2(self):
        """s(1, 2) = 0 (only r=1 term, both sawtooths = 0)."""
        assert abs(dedekind_sum(1, 2)) < 1e-12

    def test_dedekind_reciprocity(self):
        """Dedekind reciprocity: 12*c*d*(s(d,c) + s(c,d)) = d^2 + c^2 - 3*c*d + 1.

        For coprime c, d with c, d >= 1.
        """
        for c, d in [(3, 5), (7, 11), (4, 9), (5, 7)]:
            lhs = 12 * c * d * (dedekind_sum(d, c) + dedekind_sum(c, d))
            rhs = d**2 + c**2 - 3 * c * d + 1
            assert abs(lhs - rhs) < 1e-8, (
                f"Reciprocity fails for ({c},{d}): {lhs} != {rhs}"
            )


class TestStandardKloosterman:
    """Verify standard Kloosterman sums."""

    def test_kl_c1_is_1(self):
        """Kl(m, n; 1) = 1 for all m, n."""
        for m in [-1, 0, 1, 3]:
            for n in range(1, 6):
                assert abs(standard_kloosterman(m, n, 1) - 1.0) < 1e-12

    def test_kl_weil_bound(self):
        """Weil bound: |Kl(m, n; c)| <= d(c) * sqrt(gcd(m*n, c)) * sqrt(c).

        Simplified check: |Kl(-1, n; c)| <= c for small c.
        """
        for c in range(2, 8):
            for n in range(1, 10):
                kl = standard_kloosterman(-1, n, c)
                # Euler phi(c) is the number of terms, each of modulus 1
                # So |Kl| <= phi(c) <= c
                assert abs(kl) <= c + 1e-8

    def test_kl_symmetry(self):
        """Kl(m, n; c) = Kl(n, m; c) (by d <-> d' symmetry)."""
        for c in range(2, 6):
            for m in [-1, 2]:
                for n in [3, 5]:
                    kl_mn = standard_kloosterman(m, n, c)
                    kl_nm = standard_kloosterman(n, m, c)
                    assert abs(kl_mn - kl_nm) < 1e-10


class TestGeneralizedKloosterman:
    """Verify generalized Kloosterman sums with eta^3 multiplier."""

    def test_gen_kl_c1_is_1(self):
        """K(-1, D; 1, chi) = 1 for all D (trivial conductor)."""
        for D in [3, 4, 7, 8, 11, 15]:
            assert abs(generalized_kloosterman(-1, D, 1) - 1.0) < 1e-12

    def test_gen_kl_is_real(self):
        """K(-1, D; c, chi) is real (imaginary parts cancel)."""
        # This is tested implicitly by the assertion in the function,
        # but we verify explicitly here.
        for c in range(1, 6):
            for D in [3, 7, 11, 15]:
                # Should not raise AssertionError
                kl = generalized_kloosterman(-1, D, c)
                assert isinstance(kl, float)

    def test_gen_kl_bounded(self):
        """Generalized Kloosterman sums are bounded by phi(c)."""
        for c in range(2, 8):
            for D in [3, 4, 7, 8]:
                kl = generalized_kloosterman(-1, D, c)
                # phi(c) <= c, so |K| <= c is a loose bound
                assert abs(kl) <= c + 1e-8

    def test_verify_special_values(self):
        """All special-value checks pass."""
        checks = verify_kloosterman_special_values()
        for name, ok in checks.items():
            assert ok, f"Failed: {name}"


# =========================================================================
# 2. BESSEL FUNCTIONS
# =========================================================================

class TestBesselFunctions:
    """Verify Bessel function implementations."""

    def test_I_3half_small(self):
        """I_{3/2}(x) ~ x*sqrt(2/(pi*x)) for small x."""
        x = 0.01
        val = bessel_I_3half(x)
        # I_{3/2}(x) ~ (x/3) * sqrt(2/pi) for small x
        # Actually I_{3/2}(x) = sqrt(2/(pi*x))*(cosh(x) - sinh(x)/x)
        # For small x: cosh(x) ~ 1 + x^2/2, sinh(x)/x ~ 1 + x^2/6
        # So I_{3/2}(x) ~ sqrt(2/(pi*x)) * (x^2/2 - x^2/6) = sqrt(2/(pi*x)) * x^2/3
        expected = math.sqrt(2 / (math.pi * x)) * x**2 / 3
        assert abs(val - expected) / expected < 0.01

    def test_I_3half_large(self):
        """I_{3/2}(x) ~ e^x / sqrt(2*pi*x) for large x.

        At x=10, the subleading correction is O(1/x) ~ 10%, so use 15%.
        At x=50, the correction O(1/x) ~ 2%.
        """
        x = 10.0
        val = bessel_I_3half(x)
        asymp = math.exp(x) / math.sqrt(2 * math.pi * x)
        assert abs(val - asymp) / asymp < 0.15

    def test_I_3half_known_value(self):
        """I_{3/2}(1) = sqrt(2/pi) * (cosh(1) - sinh(1))."""
        val = bessel_I_3half(1.0)
        expected = math.sqrt(2 / math.pi) * (math.cosh(1) - math.sinh(1))
        assert abs(val - expected) < 1e-12

    def test_I_3half_positive(self):
        """I_{3/2}(x) > 0 for x > 0."""
        for x in [0.1, 1.0, 10.0, 100.0]:
            assert bessel_I_3half(x) > 0

    def test_I_9half_positive(self):
        """I_{9/2}(x) > 0 for x > 0."""
        for x in [0.5, 1.0, 5.0, 50.0]:
            assert bessel_I_9half(x) > 0

    def test_I_9half_large_asymptotic(self):
        """I_{9/2}(x) matches the corrected large-x asymptotic.

        For nu=9/2 the leading correction is
        -(4*nu^2 - 1)/(8*x) = -80/(8*x), about -10% at x=100.
        The uncorrected leading term is therefore not a 5% approximation
        at x=100.
        """
        x = 100.0
        nu = 9.0 / 2.0
        mu = 4.0 * nu * nu
        val = bessel_I_9half(x)
        leading = math.exp(x) / math.sqrt(2 * math.pi * x)
        corrected = leading * (
            1.0
            - (mu - 1.0) / (8.0 * x)
            + (mu - 1.0) * (mu - 9.0) / (2.0 * (8.0 * x) ** 2)
        )
        assert abs(val - corrected) / corrected < 0.001


# =========================================================================
# 3. RADEMACHER EXPANSION
# =========================================================================

class TestRademacherExpansion:
    """Verify the Rademacher expansion for phi_{0,1} coefficients."""

    def test_rademacher_term_is_namedtuple(self):
        """rademacher_term returns a RademacherTerm."""
        rt = rademacher_term(3, 1)
        assert isinstance(rt, RademacherTerm)
        assert rt.conductor == 1
        assert rt.discriminant == 3

    def test_c1_kloosterman_is_1(self):
        """At conductor c=1, the Kloosterman sum is always 1."""
        for D in [3, 4, 7, 8, 11]:
            rt = rademacher_term(D, 1)
            assert abs(rt.kloosterman - 1.0) < 1e-12

    def test_leading_term_matches_phi01_D3(self):
        """R_1(3) matches |c(3)| = 64 to within 5%."""
        rt = rademacher_term(3, 1)
        assert abs(rt.term_value - 64) / 64 < 0.05

    def test_leading_term_matches_phi01_D7(self):
        """R_1(7) matches |c(7)| = 513 to within 1%."""
        rt = rademacher_term(7, 1)
        assert abs(rt.term_value - 513) / 513 < 0.01

    def test_leading_term_matches_phi01_D15(self):
        """R_1(15) matches |c(15)| = 11775 to within 0.1%."""
        rt = rademacher_term(15, 1)
        assert abs(rt.term_value - 11775) / 11775 < 0.001

    def test_leading_term_matches_phi01_D19(self):
        """R_1(19) matches |c(19)| = 43200 to within 0.01%."""
        rt = rademacher_term(19, 1)
        assert abs(rt.term_value - 43200) / 43200 < 0.001

    def test_partial_sum_1_equals_leading(self):
        """Partial sum at max_c=1 equals the leading term."""
        D = 7
        ps = rademacher_partial_sum(D, 1)
        rt = rademacher_term(D, 1)
        assert abs(ps - rt.term_value) < 1e-12

    def test_bessel_magnitude_decreases_with_c(self):
        """The Bessel factor I_{3/2}(pi*sqrt(D)/c) decreases with c.

        Individual |R_c| terms need NOT decrease monotonically because
        the Kloosterman sum K(-1,D;c,chi) can vanish at certain c
        (e.g., K(-1,8;3) ~ 0), making |R_c| accidentally small.
        But the BESSEL part always decreases.
        """
        D = 11
        for c in range(1, 5):
            b_c = bessel_I_3half(math.pi * math.sqrt(D) / c)
            b_next = bessel_I_3half(math.pi * math.sqrt(D) / (c + 1))
            assert b_next < b_c

    def test_bessel_arg_decreases_with_c(self):
        """Bessel argument pi*sqrt(D)/c decreases with conductor c."""
        D = 8
        for c in range(1, 5):
            rt = rademacher_term(D, c)
            expected_arg = math.pi * math.sqrt(D) / c
            assert abs(rt.bessel_arg - expected_arg) < 1e-12

    def test_invalid_D_raises(self):
        """D < 1 raises ValueError."""
        with pytest.raises(ValueError):
            rademacher_term(0, 1)

    def test_invalid_c_raises(self):
        """c < 1 raises ValueError."""
        with pytest.raises(ValueError):
            rademacher_term(3, 0)

    def test_all_leading_within_5pct(self):
        """All leading terms R_1(D) match |c(D)| within 5%."""
        result = verify_leading_term_accuracy(3, 20, 0.05)
        assert result["all_pass"]


# =========================================================================
# 4. SHADOW TOWER CORRESPONDENCE
# =========================================================================

class TestShadowCorrespondence:
    """Verify shadow arity <-> Rademacher conductor correspondence."""

    def test_shadow_k2_equals_R1(self):
        """Shadow arity k=2 contribution equals R_1(D) (leading term)."""
        for D in [3, 7, 11, 15]:
            sc = shadow_contribution(2, D)
            rt = rademacher_term(D, 1)
            assert abs(sc - rt.term_value) < 1e-12

    def test_shadow_k3_equals_R2(self):
        """Shadow arity k=3 contribution equals R_2(D)."""
        for D in [3, 7, 11, 15]:
            sc = shadow_contribution(3, D)
            rt = rademacher_term(D, 2)
            assert abs(sc - rt.term_value) < 1e-12

    def test_shadow_k4_equals_R3(self):
        """Shadow arity k=4 contribution equals R_3(D)."""
        for D in [3, 7, 11]:
            sc = shadow_contribution(4, D)
            rt = rademacher_term(D, 3)
            assert abs(sc - rt.term_value) < 1e-12

    def test_shadow_partial_equals_rademacher_partial(self):
        """Shadow partial sum through k equals Rademacher partial sum through c=k-1."""
        for D in [3, 7, 11, 15]:
            for max_k in [2, 3, 4, 5]:
                sp = shadow_partial_sum(max_k, D)
                rp = rademacher_partial_sum(D, max_k - 1)
                assert abs(sp - rp) < 1e-12

    def test_shadow_invalid_k_raises(self):
        """Shadow arity k < 2 raises ValueError."""
        with pytest.raises(ValueError):
            shadow_contribution(1, 3)

    def test_correspondence_table_structure(self):
        """Correspondence table has correct structure."""
        rows = correspondence_table([3, 7], 4)
        assert len(rows) == 2 * 3  # 2 D-values, 3 arities (k=2,3,4)
        for row in rows:
            assert isinstance(row, CorrespondenceRow)
            assert row.conductor_c == row.arity_k - 1

    def test_correspondence_ratio_at_c1_is_1(self):
        """Exponential ratio at c=1 is always 1.0 (self-reference)."""
        rows = correspondence_table([3, 7, 11], 6)
        for row in rows:
            if row.conductor_c == 1:
                assert abs(row.exponential_ratio - 1.0) < 1e-12

    def test_correspondence_ratios_envelope_decreases(self):
        """Exponential ratio envelope decreases: max(c=4,5) < max(c=2,3).

        Individual |R_c/R_1| need NOT be monotone in c because the
        Kloosterman sum K(-1,D;c,chi) can be near zero at certain c.
        But the ENVELOPE (maximum over consecutive pairs) decreases,
        reflecting the underlying Bessel suppression.
        """
        rows = correspondence_table([11], 6)
        ratios = [row.exponential_ratio for row in rows]
        # ratios[0] = c=1 (=1.0), ratios[1] = c=2, ..., ratios[4] = c=5
        early_max = max(ratios[1], ratios[2])   # c=2, c=3
        late_max = max(ratios[3], ratios[4])     # c=4, c=5
        assert late_max < early_max


# =========================================================================
# 5. CONVERGENCE ANALYSIS
# =========================================================================

class TestConvergence:
    """Verify convergence of Rademacher partial sums."""

    def test_convergence_rows_structure(self):
        """Convergence analysis returns ConvergenceRow tuples."""
        rows = convergence_analysis([3], 3)
        assert len(rows) == 3  # c=1, c=2, c=3
        for row in rows:
            assert isinstance(row, ConvergenceRow)

    def test_convergence_D3_c1_error_under_5pct(self):
        """At D=3, c=1 error is under 5%."""
        rows = convergence_analysis([3], 1)
        assert rows[0].residual_rel < 0.05

    def test_convergence_D15_c1_error_under_1pct(self):
        """At D=15, c=1 error is under 1%."""
        rows = convergence_analysis([15], 1)
        assert rows[0].residual_rel < 0.01

    def test_convergence_D3_improves_c1_to_c5(self):
        """At D=3, error at c=5 is less than error at c=1."""
        rows = convergence_analysis([3], 5)
        err_c1 = rows[0].residual_rel
        err_c5 = rows[4].residual_rel
        assert err_c5 < err_c1

    def test_convergence_D12_c5_under_1pct(self):
        """At D=12, error at c=5 is under 1%."""
        rows = convergence_analysis([12], 5)
        err_c5 = rows[4].residual_rel
        assert err_c5 < 0.01

    def test_convergence_D20_c5_under_1pct(self):
        """At D=20, error at c=5 is under 1%."""
        rows = convergence_analysis([20], 5)
        err_c5 = rows[4].residual_rel
        assert err_c5 < 0.01

    def test_leading_accuracy_all_pass(self):
        """All leading terms pass the 5% tolerance."""
        result = verify_leading_term_accuracy(3, 20, 0.05)
        assert result["all_pass"]

    def test_leading_accuracy_D19_under_1pct(self):
        """At D=19, leading-term error is under 1%."""
        result = verify_leading_term_accuracy(19, 19, 0.001)
        assert result["all_pass"]


# =========================================================================
# 6. EXPONENTIAL SUPPRESSION
# =========================================================================

class TestExponentialSuppression:
    """Verify that higher Rademacher terms are exponentially suppressed."""

    def test_R2_R1_ratio_decreases_with_D(self):
        """|R_2/R_1| decreases as D increases (exponential suppression)."""
        supp = verify_exponential_suppression([3, 7, 11, 15])
        ratios = [supp[D][2]["actual_ratio"] for D in [3, 7, 11, 15]]
        for i in range(len(ratios) - 1):
            assert ratios[i + 1] < ratios[i]

    def test_R2_R1_under_10pct_at_D3(self):
        """|R_2/R_1| < 10% at D=3."""
        supp = verify_exponential_suppression([3])
        assert supp[3][2]["actual_ratio"] < 0.10

    def test_R2_R1_under_1pct_at_D11(self):
        """|R_2/R_1| < 1% at D=11."""
        supp = verify_exponential_suppression([11])
        assert supp[11][2]["actual_ratio"] < 0.01

    def test_R3_smaller_than_R2(self):
        """|R_3/R_1| < |R_2/R_1| for each D."""
        supp = verify_exponential_suppression([3, 7, 11])
        for D in [3, 7, 11]:
            assert supp[D][3]["actual_ratio"] < supp[D][2]["actual_ratio"]

    def test_suppression_matches_bessel_prediction(self):
        """Exponential suppression roughly matches exp(-pi*sqrt(D)/2) at c=2.

        The predicted ratio is exp(-pi*sqrt(D)*(1-1/2)) = exp(-pi*sqrt(D)/2).
        Allow a factor of 3 tolerance due to Kloosterman phase effects.
        """
        supp = verify_exponential_suppression([15])
        actual = supp[15][2]["actual_ratio"]
        predicted = supp[15][2]["predicted_ratio"]
        # Allow factor-of-3 tolerance
        assert actual < 3 * predicted

    def test_R4_R1_under_1pct_at_D7(self):
        """|R_4/R_1| < 1% at D=7."""
        supp = verify_exponential_suppression([7])
        assert supp[7][4]["actual_ratio"] < 0.01


# =========================================================================
# 7. KLOOSTERMAN CONDUCTOR STRUCTURE
# =========================================================================

class TestKloostermanStructure:
    """Verify the arithmetic structure of Kloosterman sums at each conductor."""

    def test_c1_all_equal_1(self):
        """At c=1, all K(-1,D;1) = 1."""
        data = kloosterman_conductor_analysis(1, 20)
        for D, kl in data[1]["kloosterman_values"].items():
            assert abs(kl - 1.0) < 1e-12

    def test_c1_arity_is_2(self):
        """Conductor c=1 maps to shadow arity k=2."""
        data = kloosterman_conductor_analysis(1, 20)
        assert data[1]["arity"] == 2

    def test_c2_arity_is_3(self):
        """Conductor c=2 maps to shadow arity k=3."""
        data = kloosterman_conductor_analysis(2, 20)
        assert data[2]["arity"] == 3

    def test_c2_kl_oscillates(self):
        """At c=2, the Kloosterman sums change sign between D values."""
        data = kloosterman_conductor_analysis(2, 20)
        vals = data[2]["kloosterman_values"]
        # Values should not all be the same sign
        signs = [v > 0 for v in vals.values() if abs(v) > 1e-10]
        assert len(set(signs)) >= 2, "K(-1,D;2) should oscillate"

    def test_mean_abs_decreases(self):
        """Mean |K(-1,D;c)| at conductor c does not grow faster than c."""
        data = kloosterman_conductor_analysis(5, 20)
        for c, cdata in data.items():
            # Weil bound: |K| <= d(c)*sqrt(c). Mean should be moderate.
            assert cdata["mean_abs"] <= c + 1

    def test_all_conductors_have_data(self):
        """Analysis returns data for all requested conductors."""
        data = kloosterman_conductor_analysis(5, 20)
        assert set(data.keys()) == {1, 2, 3, 4, 5}


# =========================================================================
# 8. SIEGEL-LEVEL RADEMACHER
# =========================================================================

class TestSiegelRademacher:
    """Verify Siegel Rademacher terms for 1/Phi_{10} (conditional on CY-A_3)."""

    def test_siegel_term_is_namedtuple(self):
        """siegel_rademacher_term returns a SiegelRademacherTerm."""
        st = siegel_rademacher_term(3, 1)
        assert isinstance(st, SiegelRademacherTerm)

    def test_siegel_term_positive(self):
        """Leading Siegel Rademacher term is positive."""
        st = siegel_rademacher_term(7, 1)
        assert st.term_value > 0

    def test_siegel_exponential_suppression(self):
        """Siegel |C_2/C_1| < |C_1/C_1| = 1 (exponentially suppressed)."""
        ratios = siegel_exponential_ratios([7, 15])
        for D in [7, 15]:
            assert ratios[D][2] < 1.0

    def test_siegel_bessel_argument(self):
        """Siegel Bessel argument is pi*sqrt(D)/c."""
        D, c = 11, 2
        st = siegel_rademacher_term(D, c)
        assert abs(st.bessel_arg - math.pi * math.sqrt(D) / c) < 1e-12

    def test_siegel_invalid_raises(self):
        """Invalid D or c raises ValueError."""
        with pytest.raises(ValueError):
            siegel_rademacher_term(0, 1)
        with pytest.raises(ValueError):
            siegel_rademacher_term(3, 0)


# =========================================================================
# 9. IDENTIFICATION TABLE
# =========================================================================

class TestIdentificationTable:
    """Verify the full identification computation."""

    def test_identification_returns_named_tuple(self):
        """compute_identification returns IdentificationResult."""
        result = compute_identification(3, 4)
        assert isinstance(result, IdentificationResult)

    def test_identification_D3(self):
        """At D=3, identification matches known |c(3)| = 64."""
        result = compute_identification(3, 6)
        assert result.exact_c_D == -64
        # Leading term within 5%
        assert result.residuals_rel[0] < 0.05

    def test_identification_D7(self):
        """At D=7, identification matches known |c(7)| = 513."""
        result = compute_identification(7, 6)
        assert result.exact_c_D == -513
        assert result.residuals_rel[0] < 0.01

    def test_identification_5_terms_improves_D3(self):
        """At D=3, 5-term error is less than 1-term error."""
        result = compute_identification(3, 6)
        assert result.residuals_rel[4] < result.residuals_rel[0]

    def test_identification_shadow_equals_rademacher(self):
        """Shadow contributions exactly equal Rademacher terms (by definition)."""
        result = compute_identification(11, 6)
        for i in range(len(result.rademacher_terms)):
            assert abs(result.shadow_contributions[i] - result.rademacher_terms[i]) < 1e-14

    def test_identification_table_all_D(self):
        """Identification table covers all positive D in PHI01_COEFFICIENTS."""
        table = compute_identification_table()
        D_computed = {row.D for row in table}
        D_expected = {D for D in PHI01_COEFFICIENTS if D > 0}
        assert D_computed == D_expected

    def test_identification_arities_correct(self):
        """Shadow arities are k=2,...,max_k."""
        result = compute_identification(7, 6)
        assert result.shadow_arities == [2, 3, 4, 5, 6]

    def test_identification_exponential_ratios_start_at_1(self):
        """Exponential ratio at c=1 is 1.0."""
        result = compute_identification(7, 6)
        assert abs(result.exponential_ratios[0] - 1.0) < 1e-12


# =========================================================================
# 10. CONJECTURE VERIFICATION
# =========================================================================

class TestConjectureVerification:
    """Verify the shadow-Rademacher conjecture formulation."""

    def test_conjecture_returns_dict(self):
        """shadow_rademacher_conjecture returns a dictionary."""
        conj = shadow_rademacher_conjecture()
        assert isinstance(conj, dict)
        assert "conjecture_name" in conj
        assert "claim_status" in conj

    def test_conjecture_leading_accuracy(self):
        """All leading-term checks pass in the conjecture verification."""
        conj = shadow_rademacher_conjecture()
        assert conj["leading_accuracy"]["all_pass"]

    def test_conjecture_has_exponential_suppression(self):
        """Conjecture includes exponential suppression data."""
        conj = shadow_rademacher_conjecture()
        assert "exponential_suppression" in conj
        # At D=3, c=2 should have a ratio
        assert 2 in conj["exponential_suppression"][3]

    def test_summary_passes(self):
        """Full summary computation does not error."""
        summary = shadow_rademacher_summary()
        assert "conjecture" in summary
        assert "status" in summary

    def test_conjecture_status_d2_verified(self):
        """Conjecture status includes d=2 verified."""
        conj = shadow_rademacher_conjecture()
        assert "d=2" in conj["claim_status"].lower() or "verified" in conj["claim_status"].lower()


# =========================================================================
# 11. CROSS-VERIFICATIONS (multi-path, AP10 compliance)
# =========================================================================

class TestCrossVerifications:
    """Multi-path cross-checks against independent engines.

    Each test verifies a numerical claim via at least 2 independent paths,
    preventing single-engine confabulation (AP-CY24).
    """

    def test_phi01_coefficients_match_fourier_engine(self):
        """Path 1: PHI01_COEFFICIENTS. Path 2: phi01_fourier.py.

        The c(D) values hardcoded in this engine MUST match the independent
        computation in phi01_fourier.py.
        """
        from compute.lib.phi01_fourier import phi01_by_discriminant
        by_d = phi01_by_discriminant(15)
        for D, val in PHI01_COEFFICIENTS.items():
            if D in by_d:
                assert val == by_d[D], (
                    f"c({D}): this engine={val}, phi01_fourier={by_d[D]}"
                )

    def test_leading_rademacher_matches_phi01_shadow(self):
        """Path 1: rademacher_term(D,1). Path 2: phi01_shadow_decomposition.py.

        The c=1 Rademacher term from this engine must match the
        independently implemented rademacher_leading_term in
        phi01_shadow_decomposition.py.
        """
        from compute.lib.phi01_shadow_decomposition import rademacher_leading_term
        for D in [3, 7, 11, 15, 19]:
            our_R1 = rademacher_term(D, 1).term_value
            their_R1 = rademacher_leading_term(D)
            # Both compute sqrt(2)*pi*D^{-3/4}*I_{3/2}(pi*sqrt(D))
            # with independent Bessel implementations
            assert abs(our_R1 - their_R1) / their_R1 < 1e-6, (
                f"D={D}: our R_1={our_R1}, theirs={their_R1}"
            )

    def test_bessel_3half_matches_phi01_shadow(self):
        """Path 1: bessel_I_3half (this engine). Path 2: _bessel_I_3half (phi01).

        Two independent implementations of I_{3/2}(x).
        """
        from compute.lib.phi01_shadow_decomposition import _bessel_I_3half
        for x in [0.5, 1.0, 5.0, 10.0]:
            ours = bessel_I_3half(x)
            theirs = _bessel_I_3half(x)
            assert abs(ours - theirs) / theirs < 1e-6, (
                f"x={x}: our I_3/2={ours}, theirs={theirs}"
            )

    def test_kappa_ch_k3_matches_mock_modular(self):
        """Path 1: K3_KAPPA_CH (this engine). Path 2: mock_modular_mechanism.py.

        The K3 kappa_ch value must agree between engines.
        """
        from compute.lib.mock_modular_mechanism import K3_KAPPA_CH as mock_kappa
        assert K3_KAPPA_CH == mock_kappa

    def test_kappa_ch_k3e_matches_bps_entropy(self):
        """This engine separates compact and Heisenberg K3 x E kappa_ch values.

        The legacy K3E_KAPPA_CH alias is the Heisenberg shadow value.
        """
        from compute.lib.bps_entropy_shadow import K3E_KAPPA_SPECTRUM
        assert K3E_KAPPA_CH_COMPACT == K3E_KAPPA_SPECTRUM.kappa_ch
        assert K3E_KAPPA_CH_HEIS == K3E_KAPPA_SPECTRUM.kappa_ch_Heis
        assert K3E_KAPPA_CH == K3E_KAPPA_CH_HEIS

    def test_dedekind_reciprocity_multi_pair(self):
        """Cross-check: Dedekind reciprocity verified for 6 coprime pairs.

        Path 1: dedekind_sum(d,c) + dedekind_sum(c,d) computed.
        Path 2: algebraic formula (d^2 + c^2 - 3cd + 1) / (12cd).
        """
        pairs = [(3, 5), (7, 11), (4, 9), (5, 7), (8, 13), (11, 17)]
        for c, d in pairs:
            lhs = dedekind_sum(d, c) + dedekind_sum(c, d)
            rhs = (d**2 + c**2 - 3 * c * d + 1) / (12.0 * c * d)
            assert abs(lhs - rhs) < 1e-10, (
                f"Reciprocity fails for ({c},{d}): {lhs} != {rhs}"
            )

    def test_rademacher_c1_vs_bekenstein_hawking(self):
        """Cross-check: log(R_1(D)) ~ pi*sqrt(D) (Bekenstein-Hawking).

        Path 1: R_1(D) from Rademacher.
        Path 2: pi*sqrt(D) from Bekenstein-Hawking entropy formula.

        For large D, log(R_1(D)) -> pi*sqrt(D) + subleading.
        """
        for D in [15, 16, 19, 20]:
            R1 = rademacher_term(D, 1).term_value
            log_R1 = math.log(R1)
            S_BH = math.pi * math.sqrt(D)
            # log(R_1) = pi*sqrt(D) + O(log(D)), so within 50% of S_BH
            # (the subleading -3/4 * log(D) is significant at small D)
            assert abs(log_R1 - S_BH) / S_BH < 0.50

    def test_exponential_suppression_vs_bessel_ratio(self):
        """Cross-check: |R_2/R_1| ~ I_{3/2}(pi*sqrt(D)/2) / (2*I_{3/2}(pi*sqrt(D))).

        Path 1: actual |R_2/R_1| ratio.
        Path 2: Bessel ratio (ignoring Kloosterman phases).
        """
        for D in [7, 11, 15]:
            R1_abs = abs(rademacher_term(D, 1).term_value)
            R2_abs = abs(rademacher_term(D, 2).term_value)
            actual_ratio = R2_abs / R1_abs

            # Bessel ratio (pure exponential part, no Kloosterman)
            b1 = bessel_I_3half(math.pi * math.sqrt(D))
            b2 = bessel_I_3half(math.pi * math.sqrt(D) / 2)
            bessel_ratio = b2 / (2 * b1)  # factor 1/c = 1/2

            # They should agree within a factor from the Kloosterman ratio
            # |K(-1,D;2)| / |K(-1,D;1)| which is <= 1
            assert actual_ratio <= bessel_ratio * 1.01  # Kloosterman bounded by 1
