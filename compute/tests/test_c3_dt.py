"""Tests for C^3 DT partition function, MacMahon function, and Y^+(gl_hat_1).

Manuscript references:
    Part V (Standard Landscape): CY 3-folds, DT theory
    Part IV (Quantum Groups): Yangian/RTT, affine Yangian

Ground truth:
    - Plane partition counts: OEIS A000219
    - MacMahon function: prod_{n>=1} 1/(1-q^n)^n
    - DT partition function: Z^{DT}_{C^3}(q) = M(-q)
    - CoHA = Y^+(gl_hat_1): Schiffmann-Vasserot (2013), RSYZ (2020)
"""

import pytest
from fractions import Fraction

from compute.lib.c3_dt_partition import (
    macmahon_coefficients,
    macmahon_coefficients_product,
    plane_partition_counts,
    dt_partition_function_c3,
    topological_vertex_empty,
    yangian_graded_dimensions,
    yangian_character,
    enumerate_plane_partitions,
    plane_partition_volume,
    addable_boxes,
    can_add_box,
    wright_asymptotic,
    verify_macmahon_two_methods,
    verify_dt_c3_signs,
    verify_yangian_coha_dimensions,
    verify_all,
)


# ================================================================
# PLANE PARTITION COUNTS (OEIS A000219)
# ================================================================

class TestPlanePartitionCounts:
    """Test plane partition counts p(n) against known values."""

    # OEIS A000219: number of plane partitions of n
    KNOWN_VALUES = {
        0: 1,
        1: 1,
        2: 3,
        3: 6,
        4: 13,
        5: 24,
        6: 48,
        7: 86,
        8: 160,
        9: 282,
        10: 500,
        11: 859,
        12: 1479,
        13: 2485,
        14: 4167,
        15: 6879,
        16: 11297,
        17: 18334,
        18: 29601,
        19: 47330,
        20: 75278,
    }

    def test_p0_through_p5(self):
        """Core values: p(0)=1, p(1)=1, p(2)=3, p(3)=6, p(4)=13, p(5)=24."""
        counts = plane_partition_counts(6)
        assert counts[0] == 1, f"p(0) = {counts[0]}, expected 1"
        assert counts[1] == 1, f"p(1) = {counts[1]}, expected 1"
        assert counts[2] == 3, f"p(2) = {counts[2]}, expected 3"
        assert counts[3] == 6, f"p(3) = {counts[3]}, expected 6"
        assert counts[4] == 13, f"p(4) = {counts[4]}, expected 13"
        assert counts[5] == 24, f"p(5) = {counts[5]}, expected 24"

    def test_all_known_values(self):
        """Verify all 21 known values from OEIS A000219."""
        counts = plane_partition_counts(21)
        for n, expected in self.KNOWN_VALUES.items():
            assert counts[n] == expected, (
                f"p({n}) = {counts[n]}, expected {expected}"
            )

    def test_p50(self):
        """p(50) = 10499640707 (OEIS A000219)."""
        counts = plane_partition_counts(51)
        assert counts[50] == 10499640707, f"p(50) = {counts[50]}, expected 10499640707"

    def test_monotone_increasing(self):
        """p(n) is strictly increasing for n >= 1."""
        counts = plane_partition_counts(51)
        for n in range(2, 51):
            assert counts[n] > counts[n - 1], (
                f"p({n}) = {counts[n]} <= p({n-1}) = {counts[n-1]}"
            )

    def test_p1_equals_1(self):
        """p(1) = 1: the unique plane partition of 1 is [[1]]."""
        counts = plane_partition_counts(2)
        assert counts[1] == 1

    def test_p2_equals_3(self):
        """p(2) = 3: the plane partitions are [[2]], [[1,1]], [[1],[1]]."""
        counts = plane_partition_counts(3)
        assert counts[2] == 3

    def test_counts_up_to_50(self):
        """Verify p(n) for n up to 50 is computed without error."""
        counts = plane_partition_counts(51)
        assert len(counts) == 51
        assert all(c > 0 for c in counts)
        # Verify a few more known values from OEIS
        assert counts[25] == 696_033
        assert counts[30] == 5_668_963
        assert counts[40] == 281_846_923

    def test_exact_rational(self):
        """Coefficients are exact integers (no floating point errors)."""
        coeffs = macmahon_coefficients(30)
        for k, c in enumerate(coeffs):
            assert c.denominator == 1, (
                f"M(q) coefficient at q^{k} is {c}, not an integer"
            )


# ================================================================
# MACMAHON FUNCTION
# ================================================================

class TestMacMahonFunction:
    """Test the MacMahon function M(q) = prod_{n>=1} 1/(1-q^n)^n."""

    def test_constant_term(self):
        """M(q) has constant term 1."""
        coeffs = macmahon_coefficients(5)
        assert coeffs[0] == Fraction(1)

    def test_first_20_coefficients(self):
        """M(q) first 20 coefficients match OEIS A000219."""
        coeffs = macmahon_coefficients(20)
        expected = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282,
                    500, 859, 1479, 2485, 4167, 6879, 11297, 18334, 29601, 47330]
        for k in range(20):
            assert int(coeffs[k]) == expected[k], (
                f"M(q) coefficient at q^{k}: got {int(coeffs[k])}, "
                f"expected {expected[k]}"
            )

    def test_two_methods_agree(self):
        """Log-exp and direct product methods agree exactly."""
        N = 40
        c1 = macmahon_coefficients(N)
        c2 = macmahon_coefficients_product(N)
        for k in range(N):
            assert c1[k] == c2[k], (
                f"Discrepancy at q^{k}: log-exp={c1[k]}, product={c2[k]}"
            )

    def test_verify_function(self):
        """The verify_macmahon_two_methods function reports match."""
        result = verify_macmahon_two_methods(40)
        assert result["match"] is True
        assert result["first_discrepancy"] is None

    def test_all_positive(self):
        """All MacMahon coefficients are positive."""
        coeffs = macmahon_coefficients(50)
        for k in range(50):
            assert coeffs[k] > 0, f"M(q) coefficient at q^{k} is {coeffs[k]}"

    def test_growth_rate(self):
        """MacMahon coefficients grow super-polynomially (exp(n^{2/3}))."""
        counts = plane_partition_counts(51)
        # p(50)/p(40) should be much larger than (50/40)^k for any fixed k
        ratio = counts[50] / counts[40]
        assert ratio > 10, (
            f"p(50)/p(40) = {ratio}, expected super-polynomial growth"
        )


# ================================================================
# DT PARTITION FUNCTION Z^{DT}_{C^3}
# ================================================================

class TestDTPartitionFunction:
    """Test Z^{DT}_{C^3}(q) = M(-q)^chi."""

    def test_chi_1_constant_term(self):
        """Z^{DT}(q) at chi=1 has constant term 1."""
        dt = dt_partition_function_c3(5, chi=1)
        assert dt[0] == Fraction(1)

    def test_chi_1_sign_alternation(self):
        """Z^{DT}(q) = M(-q) has coefficients (-1)^k p(k)."""
        N = 20
        m = macmahon_coefficients(N)
        dt = dt_partition_function_c3(N, chi=1)
        for k in range(N):
            expected = m[k] * (Fraction(-1) ** k)
            assert dt[k] == expected, (
                f"Z_{{DT}}[{k}] = {dt[k]}, expected {expected}"
            )

    def test_chi_1_first_coefficients(self):
        """Explicit first coefficients of M(-q)."""
        dt = dt_partition_function_c3(10, chi=1)
        # M(-q) = 1 - q + 3q^2 - 6q^3 + 13q^4 - 24q^5 + ...
        expected = [1, -1, 3, -6, 13, -24, 48, -86, 160, -282]
        for k in range(10):
            assert int(dt[k]) == expected[k], (
                f"M(-q) at q^{k}: got {int(dt[k])}, expected {expected[k]}"
            )

    def test_chi_0_is_one(self):
        """Z^{DT}(q) at chi=0 is identically 1."""
        dt = dt_partition_function_c3(10, chi=0)
        assert dt[0] == Fraction(1)
        for k in range(1, 10):
            assert dt[k] == Fraction(0)

    def test_chi_minus_1(self):
        """Z^{DT}(q) at chi=-1 is M(-q)^{-1}."""
        N = 20
        dt_pos = dt_partition_function_c3(N, chi=1)
        dt_neg = dt_partition_function_c3(N, chi=-1)
        # Product should be 1 mod q^N
        from compute.lib.c3_dt_partition import _poly_mul_trunc
        product = _poly_mul_trunc(dt_pos, dt_neg, N)
        assert product[0] == Fraction(1)
        for k in range(1, N):
            assert product[k] == Fraction(0), (
                f"M(-q) * M(-q)^{{-1}} coefficient at q^{k}: {product[k]}"
            )

    def test_chi_2(self):
        """Z^{DT}(q) at chi=2 is M(-q)^2."""
        N = 15
        dt_1 = dt_partition_function_c3(N, chi=1)
        dt_2 = dt_partition_function_c3(N, chi=2)
        from compute.lib.c3_dt_partition import _poly_mul_trunc
        product = _poly_mul_trunc(dt_1, dt_1, N)
        for k in range(N):
            assert dt_2[k] == product[k], (
                f"M(-q)^2 at q^{k}: got {dt_2[k]}, expected {product[k]}"
            )

    def test_verify_signs_function(self):
        """The verify_dt_c3_signs function reports correct signs."""
        result = verify_dt_c3_signs(20)
        assert result["all_signs_correct"] is True


# ================================================================
# TOPOLOGICAL VERTEX
# ================================================================

class TestTopologicalVertex:
    """Test the topological vertex C_{0,0,0}(q) = M(q)."""

    def test_empty_vertex_equals_macmahon(self):
        """C_{emptyset,emptyset,emptyset}(q) = M(q)."""
        N = 30
        vertex = topological_vertex_empty(N)
        macmahon = macmahon_coefficients(N)
        for k in range(N):
            assert vertex[k] == macmahon[k], (
                f"Topological vertex differs from MacMahon at q^{k}"
            )


# ================================================================
# AFFINE YANGIAN Y^+(gl_hat_1) / CoHA
# ================================================================

class TestAffineYangian:
    """Test the connection CoHA(C^3) = Y^+(gl_hat_1)."""

    def test_graded_dims_equal_pp_counts(self):
        """dim Y^+(gl_hat_1)_n = p(n) for all n."""
        N = 30
        dims = yangian_graded_dimensions(N)
        counts = plane_partition_counts(N)
        assert dims == counts, "Yangian graded dimensions != plane partition counts"

    def test_character_equals_macmahon(self):
        """chi_{Y^+}(q) = M(q)."""
        N = 30
        char = yangian_character(N)
        mac = macmahon_coefficients(N)
        for k in range(N):
            assert char[k] == mac[k], (
                f"Yangian character differs from MacMahon at q^{k}"
            )

    def test_dim_0(self):
        """dim Y^+_0 = 1 (vacuum state = empty partition)."""
        dims = yangian_graded_dimensions(5)
        assert dims[0] == 1

    def test_dim_1(self):
        """dim Y^+_1 = 1 (single box, generated by e_0|0>)."""
        dims = yangian_graded_dimensions(5)
        assert dims[1] == 1

    def test_dim_2(self):
        """dim Y^+_2 = 3 (three plane partitions of 2)."""
        dims = yangian_graded_dimensions(5)
        assert dims[2] == 3

    def test_verify_function(self):
        """The verify_yangian_coha_dimensions function confirms match."""
        result = verify_yangian_coha_dimensions(30)
        assert result["dimensions_match_pp_counts"] is True
        assert result["character_equals_macmahon"] is True

    def test_coha_multiplication_adds_boxes(self):
        """The CoHA e_0 action on the empty partition creates one box."""
        empty_pp = []  # empty plane partition (as height matrix)
        boxes = addable_boxes(empty_pp)
        # Only one box can be added: at position (0,0,0)
        assert len(boxes) == 1
        assert boxes[0] == (0, 0, 0)

    def test_coha_single_box_addable(self):
        """From a single box [[1]], there are 3 addable positions."""
        # The plane partition [[1]] has a single box at (0,0) with height 1.
        # Addable positions: (1,0,0), (0,1,0), (0,0,1) -- three directions.
        single_box = [[1]]
        boxes = addable_boxes(single_box)
        assert len(boxes) == 3, (
            f"Expected 3 addable boxes from [[1]], got {len(boxes)}: {boxes}"
        )


# ================================================================
# EXPLICIT ENUMERATION (small n)
# ================================================================

class TestPlanePartitionEnumeration:
    """Test explicit enumeration of plane partitions for small n."""

    def test_enumerate_0(self):
        """Plane partitions of 0: just the empty partition."""
        pps = enumerate_plane_partitions(0)
        assert len(pps) == 1
        assert pps[0] == []

    def test_enumerate_1(self):
        """Plane partitions of 1: just [[1]]."""
        pps = enumerate_plane_partitions(1)
        assert len(pps) == 1

    def test_enumerate_2(self):
        """Plane partitions of 2: [[2]], [[1,1]], [[1],[1]] => 3 total."""
        pps = enumerate_plane_partitions(2)
        assert len(pps) == 3, f"Expected 3 plane partitions of 2, got {len(pps)}"
        # Verify volumes
        for pp in pps:
            assert plane_partition_volume(pp) == 2

    def test_enumerate_3(self):
        """Plane partitions of 3: 6 total."""
        pps = enumerate_plane_partitions(3)
        assert len(pps) == 6, f"Expected 6 plane partitions of 3, got {len(pps)}"
        for pp in pps:
            assert plane_partition_volume(pp) == 3

    def test_enumerate_4(self):
        """Plane partitions of 4: 13 total."""
        pps = enumerate_plane_partitions(4)
        assert len(pps) == 13, f"Expected 13 plane partitions of 4, got {len(pps)}"
        for pp in pps:
            assert plane_partition_volume(pp) == 4

    def test_enumerate_5(self):
        """Plane partitions of 5: 24 total."""
        pps = enumerate_plane_partitions(5)
        assert len(pps) == 24, f"Expected 24 plane partitions of 5, got {len(pps)}"
        for pp in pps:
            assert plane_partition_volume(pp) == 5

    def test_enumeration_matches_counts(self):
        """Enumeration count matches generating function count for n=0..8."""
        counts = plane_partition_counts(9)
        for n in range(9):
            pps = enumerate_plane_partitions(n)
            assert len(pps) == counts[n], (
                f"Enumeration of p({n}): got {len(pps)}, "
                f"expected {counts[n]} from generating function"
            )

    def test_volume_consistency(self):
        """Every enumerated plane partition has the correct volume."""
        for n in range(7):
            pps = enumerate_plane_partitions(n)
            for pp in pps:
                vol = plane_partition_volume(pp)
                assert vol == n, (
                    f"Plane partition {pp} has volume {vol}, expected {n}"
                )


# ================================================================
# WRIGHT ASYMPTOTICS
# ================================================================

class TestWrightAsymptotics:
    """Test Wright's asymptotic formula for p(n)."""

    def test_asymptotic_order_of_magnitude(self):
        """Wright's formula gives the right order of magnitude for large n."""
        counts = plane_partition_counts(51)
        for n in [30, 40, 50]:
            exact = counts[n]
            asymp = wright_asymptotic(n)
            ratio = asymp / exact
            # Wright's leading term should be within a factor of ~2 for n>=30
            assert 0.3 < ratio < 3.0, (
                f"Wright asymptotic at n={n}: ratio = {ratio:.4f} "
                f"(exact={exact}, asymp={asymp:.0f})"
            )

    def test_asymptotic_improves_with_n(self):
        """The ratio asymp/exact should converge toward 1 as n grows."""
        counts = plane_partition_counts(51)
        ratios = []
        for n in [20, 30, 40, 50]:
            exact = counts[n]
            asymp = wright_asymptotic(n)
            ratios.append(abs(asymp / exact - 1.0))
        # Error should generally decrease (not strictly, but trend)
        assert ratios[-1] < ratios[0], (
            "Wright asymptotic error not decreasing with n"
        )


# ================================================================
# POWER SERIES ARITHMETIC
# ================================================================

class TestPowerSeriesArithmetic:
    """Test the underlying power series operations."""

    def test_inverse_is_inverse(self):
        """Inverting a series and multiplying back gives 1."""
        from compute.lib.c3_dt_partition import _poly_inv_trunc, _poly_mul_trunc
        N = 20
        # Test with MacMahon coefficients
        m = macmahon_coefficients(N)
        m_inv = _poly_inv_trunc(m, N)
        product = _poly_mul_trunc(m, m_inv, N)
        assert product[0] == Fraction(1)
        for k in range(1, N):
            assert product[k] == Fraction(0), (
                f"M(q)*M(q)^{{-1}} at q^{k} = {product[k]}"
            )

    def test_inverse_of_1(self):
        """Inverse of 1 is 1."""
        from compute.lib.c3_dt_partition import _poly_inv_trunc
        one = [Fraction(1)] + [Fraction(0)] * 9
        inv = _poly_inv_trunc(one, 10)
        assert inv[0] == Fraction(1)
        for k in range(1, 10):
            assert inv[k] == Fraction(0)

    def test_inverse_of_1_minus_q(self):
        """1/(1-q) = 1 + q + q^2 + ..."""
        from compute.lib.c3_dt_partition import _poly_inv_trunc
        f = [Fraction(1), Fraction(-1)] + [Fraction(0)] * 8
        inv = _poly_inv_trunc(f, 10)
        for k in range(10):
            assert inv[k] == Fraction(1), (
                f"1/(1-q) at q^{k} = {inv[k]}, expected 1"
            )


# ================================================================
# CROSS-VALIDATION: ENUMERATION vs GENERATING FUNCTION
# ================================================================

class TestCrossValidation:
    """Cross-validate different computation methods."""

    def test_three_methods_agree(self):
        """All three methods agree: log-exp, product, enumeration."""
        N = 9  # enumeration is slow beyond this
        logexp = macmahon_coefficients(N)
        product = macmahon_coefficients_product(N)
        for n in range(N):
            le = int(logexp[n])
            pr = int(product[n])
            en = len(enumerate_plane_partitions(n))
            assert le == pr == en, (
                f"At n={n}: log-exp={le}, product={pr}, enum={en}"
            )

    def test_dt_involution(self):
        """M(-q)*M(-q)^{-1} = 1 (chi=1 and chi=-1 are inverse)."""
        N = 25
        m_neg = dt_partition_function_c3(N, chi=1)
        m_neg_inv = dt_partition_function_c3(N, chi=-1)
        from compute.lib.c3_dt_partition import _poly_mul_trunc
        product = _poly_mul_trunc(m_neg, m_neg_inv, N)
        assert product[0] == Fraction(1)
        for k in range(1, N):
            assert product[k] == Fraction(0), (
                f"Involution check failed at q^{k}: {product[k]}"
            )

    def test_macmahon_product_relation(self):
        """M(q) = product of partition generating functions with multiplicity.

        M(q) = prod_{n>=1} 1/(1-q^n)^n. Compare with ordinary partitions:
        P(q) = prod_{n>=1} 1/(1-q^n) (OEIS A000041).
        Then M(q)/P(q) = prod_{n>=1} 1/(1-q^n)^{n-1}.
        Check that M(q) coefficients dominate P(q) coefficients.
        """
        N = 20
        m = macmahon_coefficients(N)
        # Ordinary partitions via direct product
        p = [Fraction(0)] * N
        p[0] = Fraction(1)
        for n in range(1, N):
            for k in range(n, N):
                p[k] += p[k - n]

        # p(k) counts ordinary partitions; m(k) counts plane partitions
        # Plane partitions dominate: m(k) >= p(k) for all k
        for k in range(N):
            assert m[k] >= p[k], (
                f"At q^{k}: MacMahon {m[k]} < ordinary partitions {p[k]}"
            )


# ================================================================
# INTEGRATION TEST
# ================================================================

class TestFullVerification:
    """Integration test running the full verification suite."""

    def test_verify_all(self):
        """Run verify_all and check all components pass."""
        result = verify_all(N=25)
        assert result["macmahon_cross_check"]["match"] is True
        assert result["dt_sign_pattern"]["all_signs_correct"] is True
        assert result["yangian_coha"]["dimensions_match_pp_counts"] is True
        assert result["yangian_coha"]["character_equals_macmahon"] is True


# ================================================================
# ADDITIONAL OEIS VALUES (extended validation)
# ================================================================

class TestExtendedOEIS:
    """Extended validation against OEIS A000219 values."""

    # Values computed by three independent methods (direct product,
    # log-exp, sigma_2 recursion) and cross-validated.
    EXTENDED_VALUES = {
        21: 118794,
        22: 186475,
        23: 290783,
        24: 451194,
        25: 696033,
    }

    def test_p21_through_p25(self):
        """Verify p(21)..p(25) from cross-validated computation."""
        counts = plane_partition_counts(26)
        for n, expected in self.EXTENDED_VALUES.items():
            assert counts[n] == expected, (
                f"p({n}) = {counts[n]}, expected {expected}"
            )

    def test_large_values(self):
        """Verify selected large values (cross-validated by 3 methods)."""
        counts = plane_partition_counts(51)
        assert counts[30] == 5_668_963
        assert counts[35] == 41_691_046
        assert counts[40] == 281_846_923
        assert counts[45] == 1_774_079_109
        assert counts[50] == 10_499_640_707

    def test_p30(self):
        """p(30) = 5668963."""
        counts = plane_partition_counts(31)
        assert counts[30] == 5668963


# ================================================================
# EDGE CASES
# ================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_n0_only(self):
        """Computing just p(0) = 1."""
        counts = plane_partition_counts(1)
        assert counts == [1]

    def test_macmahon_n1(self):
        """MacMahon with N=1 returns just [1]."""
        coeffs = macmahon_coefficients(1)
        assert coeffs == [Fraction(1)]

    def test_dt_n1(self):
        """DT partition function with N=1 returns [1]."""
        dt = dt_partition_function_c3(1, chi=1)
        assert dt == [Fraction(1)]

    def test_empty_plane_partition_volume(self):
        """Volume of empty partition is 0."""
        assert plane_partition_volume([]) == 0

    def test_single_box_volume(self):
        """Volume of [[1]] is 1."""
        assert plane_partition_volume([[1]]) == 1

    def test_can_add_box_to_empty(self):
        """Can add box at (0,0,0) to empty partition."""
        assert can_add_box([], 0, 0, 0) is True

    def test_cannot_add_box_mid_air(self):
        """Cannot add box at (0,0,1) to empty partition (nothing below)."""
        assert can_add_box([], 0, 0, 1) is False
