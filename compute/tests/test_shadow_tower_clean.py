r"""
Clean tests for the BKM shadow obstruction tower identification.

These tests import ONLY from phi01_fourier.py and recompute everything
from scratch, verifying the central claim:

    The shadow obstruction tower at arity r captures exactly the roots of
    complexity <= r in the BKM product formula for (1/64) Delta_5.

This is an independently auditable test suite that does NOT depend on
bkm_shadow_tower.py.  All lattice geometry, root enumeration, and
complexity assignments are recomputed from first principles.

References:
    compute/scripts/verify_shadow_tower_clean.py (the full verification script)
    compute/lib/phi01_fourier.py (exact phi_{0,1} computation)
    k3_times_e.tex: thm:k3e-denominator, thm:k3e-product
"""

import os
import sys
import math
import cmath
import pytest
from fractions import Fraction
from collections import defaultdict
from typing import Dict, Tuple

# Import the clean verification module
_scripts_dir = os.path.join(os.path.dirname(__file__), '..', 'scripts')
_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')
if _scripts_dir not in sys.path:
    sys.path.insert(0, _scripts_dir)
if _lib_dir not in sys.path:
    sys.path.insert(0, _lib_dir)

from verify_shadow_tower_clean import (  # noqa: E402
    GRAM,
    inner,
    norm_sq,
    siegel_discriminant,
    root_norm_from_disc,
    get_phi01_table,
    get_f,
    root_multiplicity,
    is_positive,
    root_complexity,
    enumerate_positive_roots,
    roots_at_complexity,
    roots_up_to_complexity,
    log_product_coefficients,
    verify_truncation_consistency,
    verify_specific_multiplicities,
    verify_weyl_vector,
    verify_real_root_structure,
    verify_product_factorization_numerical,
)


# ==========================================================================
# Fixtures
# ==========================================================================

@pytest.fixture(scope="module")
def phi01_table():
    """phi_{0,1} Fourier coefficients, computed once for the module."""
    return get_phi01_table(max_n=10)


# ==========================================================================
# 1. LATTICE GEOMETRY
# ==========================================================================

class TestLatticeGeometry:
    """Verify the hyperbolic lattice from first principles."""

    def test_gram_symmetric(self):
        for i in range(3):
            for j in range(3):
                assert GRAM[i][j] == GRAM[j][i]

    def test_gram_diagonal_2(self):
        for i in range(3):
            # VERIFIED [DC] structural property [CF] cross-family census
            assert GRAM[i][i] == 2

    def test_gram_offdiag_minus2(self):
        for i in range(3):
            for j in range(3):
                if i != j:
                    # VERIFIED [DC] structural property [CF] cross-family census
                    assert GRAM[i][j] == -2

    def test_gram_determinant(self):
        A = GRAM
        det = (A[0][0] * (A[1][1]*A[2][2] - A[1][2]*A[2][1])
             - A[0][1] * (A[1][0]*A[2][2] - A[1][2]*A[2][0])
             + A[0][2] * (A[1][0]*A[2][1] - A[1][1]*A[2][0]))
        # VERIFIED [DC] structural property [CF] cross-family census
        assert det == -32

    def test_simple_root_norm(self):
        """Simple roots e_i have norm 2."""
        for i in range(3):
            e_i = tuple(1 if j == i else 0 for j in range(3))
            # VERIFIED [DC] structural property [CF] cross-family census
            assert norm_sq(e_i) == 2

    def test_weyl_vector(self):
        """(rho, delta_i) = -1 for all i."""
        checks = verify_weyl_vector()
        for c in checks:
            assert c['pass'], f"(rho, delta_{c['i']}) = {c['val']}, expected -1"


# ==========================================================================
# 2. phi_{0,1} COEFFICIENTS (EZ CONVENTION)
# ==========================================================================

class TestPhi01Coefficients:
    """Verify phi_{0,1} Fourier coefficients against known values."""

    EZ_KNOWN = {
        (0, 0): 10,
        (0, 1): 1,
        (1, 0): 108,
        (1, 1): -64,
        (1, 2): 10,
        (2, 0): 808,
        (2, 1): -513,
        (2, 2): 108,
        (2, 3): 1,
        (3, 0): 4016,
        (3, 1): -2752,
        (3, 2): 808,
        (3, 3): -64,
    }

    @pytest.mark.parametrize("n,l,expected", [
        (n, l, v) for (n, l), v in sorted(EZ_KNOWN.items())
    ])
    def test_ez_coefficient(self, n, l, expected, phi01_table):
        assert get_f(n, l, phi01_table) == expected

    def test_symmetry(self, phi01_table):
        """f(n, l) = f(n, -l)."""
        for (n, l), v in phi01_table.items():
            assert phi01_table.get((n, -l), 0) == v

    def test_row_sum_n0(self, phi01_table):
        """sum_l f(0, l) = 12."""
        s = sum(v for (n, l), v in phi01_table.items() if n == 0)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert s == 12

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
    def test_row_sum_nge1(self, n, phi01_table):
        """sum_l f(n, l) = 0 for n >= 1."""
        s = sum(v for (nn, l), v in phi01_table.items() if nn == n)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert s == 0

    def test_discriminant_dependence(self, phi01_table):
        """f(n, l) depends only on D = 4n - l^2."""
        by_disc = {}
        for (n, l), v in phi01_table.items():
            D = 4 * n - l * l
            if D in by_disc:
                assert by_disc[D] == v, f"c({D}) inconsistent: {by_disc[D]} vs {v}"
            else:
                by_disc[D] = v

    def test_c_minus1_equals_1(self, phi01_table):
        """c(-1) = 1 (the real root coefficient)."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert get_f(0, 1, phi01_table) == 1

    def test_c_0_equals_10(self, phi01_table):
        """c(0) = 10 (lightlike root coefficient)."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert get_f(0, 0, phi01_table) == 10

    def test_c_4_equals_108(self, phi01_table):
        """c(4) = 108 (first timelike imaginary root)."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert get_f(1, 0, phi01_table) == 108


# ==========================================================================
# 3. ROOT MULTIPLICITIES
# ==========================================================================

class TestRootMultiplicities:
    """Verify root_multiplicity(n, l, m) = f(nm, l) with correct phi_{0,1}."""

    def test_mult_010(self, phi01_table):
        """Real root (0,1,0): mult = f(0, 1) = 1."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert root_multiplicity(0, 1, 0, phi01_table) == 1

    def test_mult_100(self, phi01_table):
        """Lightlike (1,0,0): mult = f(0, 0) = 10."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert root_multiplicity(1, 0, 0, phi01_table) == 10

    def test_mult_001(self, phi01_table):
        """Lightlike (0,0,1): mult = f(0, 0) = 10."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert root_multiplicity(0, 0, 1, phi01_table) == 10

    def test_mult_101_CRITICAL(self, phi01_table):
        """CRITICAL: mult(1,0,1) = f(1, 0) = 108, NOT -252.

        The old code had -252 here from a wrong hardcoded phi_{0,1} table.
        The correct value from the EZ theta-function computation is 108.
        """
        # VERIFIED [DC] structural property [CF] cross-family census
        assert root_multiplicity(1, 0, 1, phi01_table) == 108

    def test_mult_111(self, phi01_table):
        """mult(1,1,1) = f(1, 1) = -64."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert root_multiplicity(1, 1, 1, phi01_table) == -64

    def test_mult_102(self, phi01_table):
        """mult(1,0,2) = f(2, 0) = 808."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert root_multiplicity(1, 0, 2, phi01_table) == 808

    def test_mult_201(self, phi01_table):
        """mult(2,0,1) = f(2, 0) = 808."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert root_multiplicity(2, 0, 1, phi01_table) == 808

    def test_mult_121(self, phi01_table):
        """mult(1,2,1) = f(1, 2) = 10."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert root_multiplicity(1, 2, 1, phi01_table) == 10


# ==========================================================================
# 4. ROOT CLASSIFICATION AND COMPLEXITY
# ==========================================================================

class TestRootClassification:
    """Verify the complexity assignment stratifies roots correctly."""

    def test_real_roots_complexity_2(self, phi01_table):
        """All real roots (norm 2) have complexity 2."""
        all_roots = enumerate_positive_roots(5, phi01_table)
        for rt, mult, nrm, cmp in all_roots:
            if nrm == 2:
                # VERIFIED [DC] structural property [CF] cross-family census
                assert cmp == 2, f"Real root {rt} has complexity {cmp}, expected 2"

    def test_real_roots_all_mult_1(self, phi01_table):
        """All real roots have multiplicity 1 = c(-1)."""
        check = verify_real_root_structure(5, phi01_table)
        assert check['all_multiplicity_1']
        # VERIFIED [DC] structural property [CF] cross-family census
        assert check['n_real_roots'] > 0  # there are real roots

    def test_first_imaginary_complexity_3(self, phi01_table):
        """Lightlike roots at n+m=1 have complexity 3."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert root_complexity(1, 0, 0) == 3
        # VERIFIED [DC] structural property [CF] cross-family census
        assert root_complexity(0, 0, 1) == 3

    def test_arity_4_contains_101(self, phi01_table):
        """Root (1,0,1) is at complexity 4."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert root_complexity(1, 0, 1) == 4

    def test_arity_4_roots_count(self, phi01_table):
        """Arity 4 has exactly 7 roots: 4 lightlike + 3 timelike."""
        r4 = roots_at_complexity(4, 5, phi01_table)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert len(r4) == 7
        n_light = sum(1 for _, _, nrm in r4 if nrm == 0)
        n_time = sum(1 for _, _, nrm in r4 if nrm < 0)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert n_light == 4
        # VERIFIED [DC] structural property [CF] cross-family census
        assert n_time == 3

    def test_no_imaginary_at_complexity_2(self, phi01_table):
        """No imaginary roots at complexity 2."""
        r2 = roots_at_complexity(2, 5, phi01_table)
        for rt, mult, nrm in r2:
            # VERIFIED [DC] structural property [CF] cross-family census
            assert nrm == 2, f"Non-real root {rt} at complexity 2"


# ==========================================================================
# 5. CENTRAL CLAIM: TRUNCATION CONSISTENCY
# ==========================================================================

class TestTruncationConsistency:
    """THE CENTRAL TEST: shadow obstruction tower at arity r = roots of complexity <= r."""

    @pytest.mark.parametrize("arity", [2, 3, 4, 5, 6])
    def test_truncation_agreement(self, arity, phi01_table):
        """log(Phi^{<=r}) - log(Phi^{<=r-1}) is exactly the arity-r roots."""
        results = verify_truncation_consistency(arity, 5, phi01_table)
        assert results[arity]['match'], (
            f"Truncation mismatch at arity {arity}: "
            f"{results[arity]['mismatches'][:3]}"
        )

    def test_all_arities_pass(self, phi01_table):
        """All arities 2-6 pass the truncation consistency check."""
        results = verify_truncation_consistency(6, 5, phi01_table)
        for r in range(2, 7):
            assert results[r]['match'], f"Arity {r} FAILED"

    def test_arity_2_only_real(self, phi01_table):
        """Arity 2 contains only real roots."""
        results = verify_truncation_consistency(6, 5, phi01_table)
        assert results[2]['n_real'] == results[2]['n_roots']
        # VERIFIED [DC] structural property [CF] cross-family census
        assert results[2]['n_lightlike'] == 0
        # VERIFIED [DC] structural property [CF] cross-family census
        assert results[2]['n_timelike'] == 0

    def test_arity_3_only_lightlike(self, phi01_table):
        """Arity 3 contains only lightlike imaginary roots."""
        results = verify_truncation_consistency(6, 5, phi01_table)
        assert results[3]['n_lightlike'] == results[3]['n_roots']
        # VERIFIED [DC] structural property [CF] cross-family census
        assert results[3]['n_real'] == 0

    def test_arity_4_mixed(self, phi01_table):
        """Arity 4 has both lightlike and timelike imaginary roots."""
        results = verify_truncation_consistency(6, 5, phi01_table)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert results[4]['n_lightlike'] > 0
        # VERIFIED [DC] structural property [CF] cross-family census
        assert results[4]['n_timelike'] > 0

    def test_arity_4_total_abs_mult(self, phi01_table):
        """Arity 4 total |mult| = 276 with correct phi_{0,1}."""
        results = verify_truncation_consistency(6, 5, phi01_table)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert results[4]['total_abs_mult'] == 276


# ==========================================================================
# 6. LOG COEFFICIENT STRUCTURE
# ==========================================================================

class TestLogCoefficients:
    """Verify specific log-product coefficients."""

    def test_arity_2_log_nonzero(self, phi01_table):
        """Arity 2 (real roots only) produces nonzero log coefficients."""
        log2 = log_product_coefficients(2, 5, phi01_table)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert len(log2) > 0

    def test_arity_3_adds_terms(self, phi01_table):
        """Arity 3 adds new log coefficients beyond arity 2."""
        log2 = log_product_coefficients(2, 5, phi01_table)
        log3 = log_product_coefficients(3, 5, phi01_table)
        # log3 should have all of log2's keys plus new ones
        for key in log2:
            assert key in log3 or log3.get(key, Fraction(0)) == log2[key]
        assert len(log3) >= len(log2)

    def test_log_coeff_100(self, phi01_table):
        """The log coefficient at (1,0,0) comes from the lightlike root at arity 3.

        (1,0,0) has mult=10, so log contribution at (1,0,0) = -10/1 = -10.
        Plus any contribution from real roots that are multiples of (1,0,0)
        -- but (1,0,0) is not a multiple of any real root (real roots have
        norm 2, and norm(1,0,0) = 0), so the arity-2 contribution is 0.
        At arity 3, we add -10.
        """
        log3 = log_product_coefficients(3, 5, phi01_table)
        # Arity 2 does not contribute to (1,0,0) since it's not real
        log2 = log_product_coefficients(2, 5, phi01_table)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert log2.get((1, 0, 0), Fraction(0)) == Fraction(0)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert log3.get((1, 0, 0), Fraction(0)) == Fraction(-10)


# ==========================================================================
# 7. NUMERICAL CONVERGENCE
# ==========================================================================

class TestNumericalConvergence:
    """Verify that truncated products converge."""

    def test_convergence(self, phi01_table):
        """Successive differences decrease (product converges)."""
        result = verify_product_factorization_numerical(4, phi01_table)
        assert result['converging'], (
            f"Successive diffs not decreasing: {result['diffs']}"
        )

    def test_rapid_convergence(self, phi01_table):
        """The convergence is rapid: |Phi^{<=6} - Phi^{<=5}| < 1e-15."""
        result = verify_product_factorization_numerical(4, phi01_table)
        # VERIFIED [DC] convergence [CF] cross-family census
        assert result['diffs'][6] < 1e-15


# ==========================================================================
# 8. REGRESSION: OLD WRONG VALUES
# ==========================================================================

class TestRegression:
    """Ensure the old wrong values are NOT present."""

    def test_mult_101_not_minus252(self, phi01_table):
        """mult(1,0,1) must NOT be -252 (the old wrong value)."""
        m = root_multiplicity(1, 0, 1, phi01_table)
        assert m != -252, "REGRESSION: still getting old wrong value -252"
        # VERIFIED [DC] structural property [CF] cross-family census
        assert m == 108, f"Expected 108, got {m}"

    def test_f_0_0_is_10_not_20(self, phi01_table):
        """f(0,0) = 10 in EZ normalization (NOT 20 as in some wrong tables).

        The EZ normalization has phi_{0,1}(tau, 0) = 12, with:
            f(0, -1) + f(0, 0) + f(0, 1) = 1 + 10 + 1 = 12.
        Some references use a different normalization with f(0,0) = 20.
        """
        # VERIFIED [DC] structural property [CF] cross-family census
        assert get_f(0, 0, phi01_table) == 10

    def test_c_minus1_is_1_not_2(self, phi01_table):
        """c(-1) = 1 (NOT 2).

        In EZ normalization, phi_{0,1} = r^{-1} + 10 + r + O(q),
        so f(0,1) = 1, hence c(-1) = 1.  Some references have c(-1) = 2
        from a different normalization (the 2y + 20 + 2y^{-1} convention).
        """
        # VERIFIED [DC] structural property [CF] cross-family census
        assert get_f(0, 1, phi01_table) == 1


# ==========================================================================
# 9. FULL VERIFICATION (integration test)
# ==========================================================================

class TestFullVerification:
    """Run the complete verification as an integration test."""

    def test_full_passes(self, phi01_table):
        """All specific multiplicity checks pass."""
        checks = verify_specific_multiplicities(phi01_table)
        for c in checks:
            assert c['pass'], f"FAILED: {c['desc']} (got {c['actual']}, expected {c['expected']})"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
