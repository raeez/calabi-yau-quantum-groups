"""Tests for the bar complex of Y^+(gl_hat_1).

Manuscript references:
    thm:sv-c3 (toric_cy3_coha.tex): CoHA(C^3) = Y^+(gl_hat_1)
    ~/chiral-bar-cobar/chapters/frame/bar_cobar_adjunction_curved.tex: bar complex
    ~/calabi-yau-quantum-groups/notes/theory_cy_to_chiral.tex: CY-to-chiral functor

Literature:
    Schiffmann-Vasserot arXiv:1211.1287: CoHA = positive Yangian
    Kontsevich-Soibelman arXiv:0811.2435: DT from motivic Hall algebra
    MNOP arXiv:math/0312059: DT/GW correspondence
    OEIS A000219: plane partitions

Multi-path verification strategy:
    Path 1 (direct): compute bar complex dimensions by convolution
    Path 2 (combinatorial): compare with plane partition combinatorics
    Path 3 (generating function): compare with MacMahon / plethystic logarithm
    Path 4 (Euler characteristic): alternating sum = inverse MacMahon
"""

import pytest
from fractions import Fraction

from compute.lib.yangian_bar_complex import (
    augmentation_ideal_dims,
    bar_arity_k_dims,
    bar_arity_k_generating_function,
    bar_cohomology_arity1,
    bar_cohomology_arity2,
    bar_complex_summary,
    bar_complex_table,
    bar_differential_matrix_dims,
    bar_euler_char_alternating_sum,
    bar_euler_char_by_degree,
    bps_invariants_c3,
    bps_invariants_from_macmahon,
    dt_from_bar_euler_char,
    explicit_bar_elements_arity2,
    indecomposables_dim,
    plethystic_log_coefficients,
    symmetric_model_cohomology_dims,
    verify_cohomology_euler_char,
    verify_macmahon_bar_identity,
)
from compute.lib.c3_dt_partition import (
    macmahon_coefficients,
    macmahon_coefficients_product,
    plane_partition_counts,
)


# ================================================================
# BPS INVARIANTS AND PLETHYSTIC LOGARITHM
# ================================================================

class TestBPSInvariants:
    """Tests for BPS invariants Omega(n) of C^3."""

    def test_bps_c3_values(self):
        """Omega(n) = n for n >= 1 (C^3 BPS counts)."""
        bps = bps_invariants_c3(20)
        for n in range(20):
            assert bps[n] == n, f"Omega({n}) should be {n}, got {bps[n]}"

    def test_bps_from_plethystic_log(self):
        """PLog(M(q)) = sum n*q^n, computed from MacMahon function."""
        N = 15
        plog = bps_invariants_from_macmahon(N)
        for n in range(1, N):
            assert abs(float(plog[n]) - n) < 1e-10, (
                f"PLog(M(q)) coefficient at q^{n}: expected {n}, got {float(plog[n])}"
            )

    def test_bps_from_plethystic_log_exact(self):
        """PLog(M(q)) coefficients are exact integers via Fraction arithmetic."""
        N = 12
        plog = bps_invariants_from_macmahon(N)
        for n in range(1, N):
            assert plog[n] == Fraction(n), (
                f"PLog exact at q^{n}: expected {n}, got {plog[n]}"
            )

    def test_plethystic_log_round_trip(self):
        """PLog(M(q)) should give exponents that reproduce M(q) via PExp.

        M(q) = prod_{n>=1} (1-q^n)^{-Omega(n)} with Omega(n) = n.
        Verify: prod_{n>=1} (1-q^n)^{-n} = M(q).
        """
        N = 15
        mac1 = macmahon_coefficients(N)
        mac2 = macmahon_coefficients_product(N)
        for i in range(N):
            assert mac1[i] == mac2[i], (
                f"MacMahon methods disagree at q^{i}: {mac1[i]} vs {mac2[i]}"
            )


# ================================================================
# PLANE PARTITION COUNTS (OEIS A000219)
# ================================================================

class TestPlanePartitions:
    """Verify plane partition counts against OEIS A000219."""

    KNOWN_VALUES = {
        0: 1, 1: 1, 2: 3, 3: 6, 4: 13, 5: 24,
        6: 48, 7: 86, 8: 160, 9: 282, 10: 500,
        11: 859, 12: 1479, 13: 2485, 14: 4167, 15: 6879,
    }

    def test_plane_partition_counts(self):
        """Verify p(n) against OEIS values."""
        pp = plane_partition_counts(16)
        for n, expected in self.KNOWN_VALUES.items():
            assert pp[n] == expected, (
                f"p({n}): expected {expected}, got {pp[n]}"
            )

    def test_macmahon_two_methods_agree(self):
        """Two independent computations of M(q) agree (Path 2 vs Path 3)."""
        N = 20
        mac_log = macmahon_coefficients(N)
        mac_prod = macmahon_coefficients_product(N)
        for i in range(N):
            assert mac_log[i] == mac_prod[i], (
                f"MacMahon methods disagree at q^{i}"
            )


# ================================================================
# BAR COMPLEX DIMENSIONS (ARITY-BY-DEGREE)
# ================================================================

class TestBarComplexDimensions:
    """Tests for dim B^k_n = dim (Y^+_{>0})^{otimes k} at total degree n."""

    def test_bar_arity0(self):
        """B^0 = Q (ground field), concentrated at degree 0."""
        dims = bar_arity_k_dims(0, 10)
        assert dims[0] == 1
        for n in range(1, 10):
            assert dims[n] == 0

    def test_bar_arity1_equals_augmentation(self):
        """B^1 = Y^+_{>0}, so dim B^1_n = p(n) for n >= 1, 0 for n = 0."""
        N = 12
        dims = bar_arity_k_dims(1, N)
        pp = plane_partition_counts(N)
        assert dims[0] == 0
        for n in range(1, N):
            assert dims[n] == pp[n], (
                f"B^1_{n}: expected p({n})={pp[n]}, got {dims[n]}"
            )

    def test_bar_arity2_at_degree2(self):
        """B^2_2 = Y^+_1 tensor Y^+_1, dim = p(1)*p(1) = 1."""
        dims = bar_arity_k_dims(2, 5)
        assert dims[2] == 1  # [e_0 | e_0]

    def test_bar_arity2_at_degree3(self):
        """B^2_3 = (Y^+_1 tensor Y^+_2) + (Y^+_2 tensor Y^+_1).
        dim = p(1)*p(2) + p(2)*p(1) = 1*3 + 3*1 = 6.
        """
        dims = bar_arity_k_dims(2, 5)
        assert dims[3] == 6

    def test_bar_arity2_at_degree4(self):
        """B^2_4 = sum_{a+b=4, a,b>=1} p(a)*p(b).
        = p(1)*p(3) + p(2)*p(2) + p(3)*p(1) = 1*6 + 3*3 + 6*1 = 21.
        """
        dims = bar_arity_k_dims(2, 5)
        assert dims[4] == 21

    def test_bar_arity3_at_degree3(self):
        """B^3_3 = Y^+_1^{tensor 3}, dim = p(1)^3 = 1."""
        dims = bar_arity_k_dims(3, 5)
        assert dims[3] == 1

    def test_bar_arity3_at_degree4(self):
        """B^3_4: three ways to split 4 = 1+1+2 = 1+2+1 = 2+1+1.
        dim = 3 * p(1)*p(1)*p(2) = 3*1*1*3 = 9.
        """
        dims = bar_arity_k_dims(3, 5)
        assert dims[4] == 9

    def test_bar_arity4_at_degree4(self):
        """B^4_4 = Y^+_1^{tensor 4}, dim = p(1)^4 = 1."""
        dims = bar_arity_k_dims(4, 5)
        assert dims[4] == 1

    def test_bar_vanishing_below_arity(self):
        """B^k_n = 0 for n < k (each factor needs degree >= 1)."""
        for k in range(1, 6):
            dims = bar_arity_k_dims(k, k + 3)
            for n in range(k):
                assert dims[n] == 0, f"B^{k}_{n} should vanish, got {dims[n]}"

    def test_bar_diagonal_is_one(self):
        """B^k_k = p(1)^k = 1 (each factor in degree 1)."""
        for k in range(1, 7):
            dims = bar_arity_k_dims(k, k + 1)
            assert dims[k] == 1, f"B^{k}_{k} should be 1, got {dims[k]}"

    def test_generating_function_matches_dims(self):
        """bar_arity_k_generating_function and bar_arity_k_dims agree."""
        N = 10
        for k in range(5):
            gf = bar_arity_k_generating_function(k, N)
            dims = bar_arity_k_dims(k, N)
            for n in range(N):
                assert int(gf[n]) == dims[n], (
                    f"GF vs dims mismatch at k={k}, n={n}: {gf[n]} vs {dims[n]}"
                )


# ================================================================
# BAR EULER CHARACTERISTIC
# ================================================================

class TestBarEulerCharacteristic:
    """Tests for chi_n = sum_k (-1)^k dim B^k_n = [q^n] 1/M(q)."""

    KNOWN_INVERSE_MACMAHON = [
        1, -1, -2, -1, 0, 4, 4, 7, 3, -2, -9, -17,
    ]

    def test_euler_char_values(self):
        """Verify chi_n against known 1/M(q) coefficients."""
        euler = bar_euler_char_by_degree(12)
        for n, expected in enumerate(self.KNOWN_INVERSE_MACMAHON):
            assert int(euler[n]) == expected, (
                f"chi_{n}: expected {expected}, got {euler[n]}"
            )

    def test_euler_char_alternating_sum_low_degree(self):
        """Alternating sum matches exact for low degrees (where max_arity is enough)."""
        N = 8  # at degree n, need arity up to n
        euler_exact = bar_euler_char_by_degree(N)
        euler_alt = bar_euler_char_alternating_sum(N, N)
        for n in range(N):
            assert int(round(float(euler_alt[n]))) == int(euler_exact[n]), (
                f"chi_{n}: exact={euler_exact[n]}, alt_sum={euler_alt[n]}"
            )

    def test_macmahon_times_inverse_is_one(self):
        """M(q) * (1/M(q)) = 1 mod q^N."""
        result = verify_macmahon_bar_identity(20)
        assert result['product_is_identity'], "M(q) * (1/M(q)) should be 1"

    def test_chi_0_is_one(self):
        """chi_0 = 1 (from B^0_0 = 1, all other B^k_0 = 0)."""
        euler = bar_euler_char_by_degree(5)
        assert euler[0] == Fraction(1)

    def test_chi_1_is_minus_one(self):
        """chi_1 = -p(1) = -1 (only B^1_1 = 1 contributes)."""
        euler = bar_euler_char_by_degree(5)
        assert euler[1] == Fraction(-1)


# ================================================================
# DT INVARIANTS FROM BAR COMPLEX
# ================================================================

class TestDTFromBar:
    """Test extraction of DT invariants from bar complex data."""

    def test_bps_product_matches_inverse_macmahon(self):
        """prod_{n>=1} (1-q^n)^n = 1/M(q) (DT = MacMahon)."""
        result = dt_from_bar_euler_char(15)
        assert result['match'], "BPS product should match 1/M(q)"

    def test_dt_partition_function_signs(self):
        """Z^DT(q) = M(-q): sign pattern matches."""
        from compute.lib.c3_dt_partition import dt_partition_function_c3
        N = 10
        mac = macmahon_coefficients(N)
        dt = dt_partition_function_c3(N)
        for n in range(N):
            expected = mac[n] * (Fraction(-1) ** n)
            assert dt[n] == expected, (
                f"Z^DT at q^{n}: expected {expected}, got {dt[n]}"
            )


# ================================================================
# BAR COHOMOLOGY (SYMMETRIC MODEL)
# ================================================================

class TestBarCohomologySym:
    """Tests for H^k(B(Sym(V_BPS))) = Wedge^k(V_BPS).

    This is the commutative model (associated graded of the CoHA).
    The exterior powers encode the BPS state space and its multilinear
    algebra. The dimensions test the bar complex cohomology in the
    symmetric approximation.
    """

    def test_h0_is_ground_field(self):
        """H^0 = Q, concentrated at degree 0."""
        cohom = symmetric_model_cohomology_dims(10, 1)
        assert cohom[0][0] == 1
        for n in range(1, 10):
            assert cohom[0][n] == 0

    def test_h1_equals_bps(self):
        """H^1_n = Omega(n) = n (BPS generators)."""
        N = 12
        cohom = symmetric_model_cohomology_dims(N, 1)
        for n in range(1, N):
            assert cohom[1][n] == n, (
                f"H^1_{n}: expected {n}, got {cohom[1][n]}"
            )

    def test_h1_from_indecomposables(self):
        """H^1 from bar_cohomology_arity1 matches symmetric model."""
        N = 10
        h1_bar = bar_cohomology_arity1(N)
        cohom = symmetric_model_cohomology_dims(N, 1)
        for n in range(N):
            assert h1_bar[n] == cohom[1][n], (
                f"H^1_{n}: bar={h1_bar[n]}, sym={cohom[1][n]}"
            )

    def test_h2_values(self):
        """H^2 = Wedge^2(V_BPS), specific values.

        H^2_3: Wedge^2 of (V_1 + V_2) at degree 3 = dim(V_1) * dim(V_2) = 1*2 = 2.
        H^2_4: V_1 tensor V_3 (dim=3) + Wedge^2(V_2) (dim=C(2,2)=1) = 3+1 = 4.
        H^2_5: V_1 tensor V_4 + V_2 tensor V_3 = 1*4 + 2*3 = 4+6 = 10.
        """
        cohom = symmetric_model_cohomology_dims(10, 2)
        assert cohom[2][3] == 2, f"H^2_3: expected 2, got {cohom[2][3]}"
        assert cohom[2][4] == 4, f"H^2_4: expected 4, got {cohom[2][4]}"
        assert cohom[2][5] == 10, f"H^2_5: expected 10, got {cohom[2][5]}"

    def test_h2_vanishes_below_degree3(self):
        """Wedge^2 requires two distinct BPS states, minimum degree 1+2 = 3."""
        cohom = symmetric_model_cohomology_dims(5, 2)
        assert cohom[2][0] == 0
        assert cohom[2][1] == 0
        assert cohom[2][2] == 0

    def test_h3_first_nonzero(self):
        """H^3_5 = Wedge^3: need degrees 1+2+... >= 1+2+... .
        Minimum degree for Wedge^3 is when we pick from V_1, V_1, V_2
        but Wedge requires distinct SPACES... Actually:
        Wedge^3(V) at degree 5: using graded pieces V_1 (dim 1), V_2 (dim 2).
        We need 3 basis vectors with total degree 5, using wedge product.
        Possible: one from V_1, two from V_2: dim = 1 * C(2,2) = 1.
        So H^3_5 = 1.
        """
        cohom = symmetric_model_cohomology_dims(8, 3)
        assert cohom[3][5] == 1, f"H^3_5: expected 1, got {cohom[3][5]}"

    def test_h3_vanishes_below_degree5(self):
        """Wedge^3(V_BPS): minimum degree is 1 + ... but since dim(V_1)=1,
        we need at least one element from V_2, giving min degree >= 5.
        Actually: from V_1 (dim 1), V_2 (dim 2), V_3 (dim 3), ...
        We need 3 vectors. From V_1 alone: only 1 vector (dim 1), not enough.
        Min is: 1 vector from V_1, 2 from V_2: degree = 1+2+2 = 5.
        Or: 1 from V_1, 1 from V_2, 1 from... but V_1 has dim 1, V_2 has dim 2.
        3 vectors with degrees summing to n: (1,1,...) needs 3 copies from V_1
        but dim V_1 = 1 so Wedge = 0. (1,2,...) needs 1+2+rest: (1,2,2) sum=5.
        Wedge^2(V_2) * V_1 = C(2,2)*1 = 1. So H^3_5 = 1, and H^3_n = 0 for n < 5.
        """
        cohom = symmetric_model_cohomology_dims(6, 3)
        for n in range(5):
            assert cohom[3][n] == 0, f"H^3_{n} should vanish, got {cohom[3][n]}"

    def test_h4_first_nonzero_at_degree8(self):
        """H^4: minimum degree for Wedge^4(V_BPS) with dim V_n = n.
        Need 4 vectors. From V_1 (1), V_2 (2), V_3 (3):
        (1,2,2,3): sum=8. Needs 1 from V_1, Wedge^2(V_2)=1, 1 from V_3.
        So H^4_8 = 1*C(2,2)*3 = 3.
        """
        cohom = symmetric_model_cohomology_dims(10, 4)
        assert cohom[4][8] == 3, f"H^4_8: expected 3, got {cohom[4][8]}"
        for n in range(8):
            assert cohom[4][n] == 0, f"H^4_{n} should vanish, got {cohom[4][n]}"

    def test_cohomology_euler_char_matches_bar(self):
        """sum_k (-1)^k char(H^k) = 1/M(q) (bar Euler char identity)."""
        result = verify_cohomology_euler_char(10, 6)
        assert result['match'], (
            f"Cohomology Euler char should match bar Euler char. "
            f"Mismatches: {result['mismatches']}"
        )


# ================================================================
# BAR COMPLEX ARITY-2 EXPLICIT
# ================================================================

class TestBarArity2:
    """Tests for the arity-2 bar complex B^2(Y^+)."""

    def test_arity2_dims(self):
        """Explicit dimensions of B^2_n for small n."""
        dims = explicit_bar_elements_arity2(8)
        # B^2_2: [pp_1 | pp_1] -> 1*1 = 1
        assert dims[2] == 1
        # B^2_3: [pp_1|pp_2] + [pp_2|pp_1] -> 1*3 + 3*1 = 6
        assert dims[3] == 6
        # B^2_4: [pp_1|pp_3] + [pp_2|pp_2] + [pp_3|pp_1] -> 6 + 9 + 6 = 21
        assert dims[4] == 21

    def test_arity2_from_bar_differential_target(self):
        """The bar differential d: B^2 -> B^1 has:
        source = B^2_n, target = B^1_n = Y^+_n.
        Check dimensions are consistent.
        """
        for n in range(2, 8):
            src, tgt = bar_differential_matrix_dims(2, n)
            b2 = bar_arity_k_dims(2, n + 1)
            b1 = bar_arity_k_dims(1, n + 1)
            assert src == b2[n], f"Source dim at n={n}"
            assert tgt == b1[n], f"Target dim at n={n}"


# ================================================================
# AUGMENTATION IDEAL
# ================================================================

class TestAugmentationIdeal:
    """Tests for the augmentation ideal Y^+_{>0}."""

    def test_augmentation_degree0(self):
        """Augmentation ideal has dim 0 at degree 0."""
        aug = augmentation_ideal_dims(5)
        assert aug[0] == 0

    def test_augmentation_equals_pp_shifted(self):
        """dim(Y^+_{>0})_n = p(n) for n >= 1."""
        N = 10
        aug = augmentation_ideal_dims(N)
        pp = plane_partition_counts(N)
        for n in range(1, N):
            assert aug[n] == pp[n]


# ================================================================
# MACMAHON IDENTITY TESTS
# ================================================================

class TestMacMahonIdentity:
    """Comprehensive tests of the bar complex = MacMahon function identity."""

    def test_identity_N15(self):
        """M(q) * (1/M(q)) = 1 mod q^15."""
        result = verify_macmahon_bar_identity(15)
        assert result['product_is_identity']

    def test_identity_N25(self):
        """M(q) * (1/M(q)) = 1 mod q^25."""
        result = verify_macmahon_bar_identity(25)
        assert result['product_is_identity']

    def test_inverse_macmahon_first_few(self):
        """Check specific coefficients of 1/M(q) = prod (1-q^n)^n."""
        inv = bar_euler_char_by_degree(8)
        # [q^0] = 1
        assert inv[0] == Fraction(1)
        # [q^1] = -1 (from (1-q)^1)
        assert inv[1] == Fraction(-1)
        # [q^2] = -2 (from (1-q)^1*(1-q^2)^2: -1 from q^2 term of (1-q),
        #              -2 from (1-q^2)^2 leading term)
        assert inv[2] == Fraction(-2)
        # [q^3] = -1
        assert inv[3] == Fraction(-1)
        # [q^4] = 0
        assert inv[4] == Fraction(0)
        # [q^5] = 4
        assert inv[5] == Fraction(4)


# ================================================================
# MULTI-PATH VERIFICATION
# ================================================================

class TestMultiPathVerification:
    """Cross-verification tests using multiple independent paths."""

    def test_path1_vs_path2_arity_dims(self):
        """Path 1 (convolution) vs Path 2 (generating function) for B^k dims."""
        N = 10
        for k in range(5):
            dims_conv = bar_arity_k_dims(k, N)
            gf = bar_arity_k_generating_function(k, N)
            dims_gf = [int(c) for c in gf]
            for n in range(N):
                assert dims_conv[n] == dims_gf[n], (
                    f"Path 1 vs 2 at k={k}, n={n}: {dims_conv[n]} vs {dims_gf[n]}"
                )

    def test_path3_plethystic_log(self):
        """Path 3: PLog(M(q)) gives BPS = [0, 1, 2, 3, ...]."""
        bps_direct = bps_invariants_c3(15)
        bps_plog = bps_invariants_from_macmahon(15)
        for n in range(15):
            assert abs(float(bps_plog[n]) - bps_direct[n]) < 1e-10, (
                f"PLog at n={n}: direct={bps_direct[n]}, plog={float(bps_plog[n])}"
            )

    def test_path4_euler_char_two_methods(self):
        """Path 4: Euler char from product vs from alternating sum (low degree)."""
        N = 7
        euler_product = bar_euler_char_by_degree(N)
        euler_alt = bar_euler_char_alternating_sum(N, N)
        for n in range(N):
            assert int(round(float(euler_alt[n]))) == int(euler_product[n]), (
                f"Euler char at n={n}: product={euler_product[n]}, "
                f"alt_sum={euler_alt[n]}"
            )

    def test_macmahon_two_independent_computations(self):
        """M(q) from log-exp vs from direct product (independent computations)."""
        N = 20
        mac1 = macmahon_coefficients(N)  # log-exp method
        mac2 = macmahon_coefficients_product(N)  # direct product
        for i in range(N):
            assert mac1[i] == mac2[i], (
                f"MacMahon at q^{i}: log-exp={mac1[i]}, product={mac2[i]}"
            )

    def test_h1_three_paths(self):
        """H^1 from (a) indecomposables, (b) symmetric model, (c) direct BPS.

        All three should give dim H^1_n = n.
        """
        N = 12
        h1_indecomp = indecomposables_dim(N)
        cohom = symmetric_model_cohomology_dims(N, 1)
        h1_sym = cohom[1]
        bps = bps_invariants_c3(N)
        for n in range(1, N):
            assert h1_indecomp[n] == n, f"Indecomposables at n={n}: {h1_indecomp[n]}"
            assert h1_sym[n] == n, f"Symmetric model at n={n}: {h1_sym[n]}"
            assert bps[n] == n, f"BPS at n={n}: {bps[n]}"


# ================================================================
# BAR COMPLEX TABLE
# ================================================================

class TestBarComplexTable:
    """Tests for the comprehensive bar complex table."""

    def test_table_has_all_keys(self):
        """Table contains all required keys."""
        table = bar_complex_table(8, 4)
        assert 'dims' in table
        assert 'euler_exact' in table
        assert 'euler_alternating' in table
        assert 'cohomology_sym' in table
        assert 'bps' in table
        assert 'plane_partitions' in table

    def test_table_dims_consistent(self):
        """Dims from table match individual computations."""
        N = 8
        table = bar_complex_table(N, 4)
        for k in range(5):
            individual = bar_arity_k_dims(k, N)
            for n in range(N):
                assert table['dims'][k][n] == individual[n]


# ================================================================
# SUMMARY REPORT
# ================================================================

class TestSummaryReport:
    """Test the human-readable summary output."""

    def test_summary_runs(self):
        """Summary generates without errors."""
        summary = bar_complex_summary(8, 4)
        assert "BAR COMPLEX" in summary
        assert "MacMahon identity" in summary
        assert "True" in summary

    def test_summary_contains_bps(self):
        """Summary contains BPS invariants."""
        summary = bar_complex_summary(8, 4)
        assert "BPS invariants" in summary


# ================================================================
# STRUCTURAL PROPERTIES
# ================================================================

class TestStructuralProperties:
    """Tests for structural properties of the bar complex."""

    def test_b1_n_equals_p_n(self):
        """B^1_n = p(n) for all n >= 1 (arity 1 = augmentation ideal)."""
        N = 15
        dims = bar_arity_k_dims(1, N)
        pp = plane_partition_counts(N)
        for n in range(1, N):
            assert dims[n] == pp[n]

    def test_b2_n_convolution(self):
        """B^2_n = sum_{a+b=n, a,b>=1} p(a)*p(b) (explicit convolution)."""
        N = 10
        pp = plane_partition_counts(N)
        dims = bar_arity_k_dims(2, N)
        for n in range(2, N):
            expected = sum(pp[a] * pp[n - a] for a in range(1, n))
            assert dims[n] == expected, (
                f"B^2_{n}: expected {expected}, got {dims[n]}"
            )

    def test_growth_rate_b_k_n(self):
        """B^k_n grows: B^k_n >= B^k_{n-1} for n >= k+1."""
        N = 12
        for k in range(1, 5):
            dims = bar_arity_k_dims(k, N)
            for n in range(k + 2, N):
                assert dims[n] >= dims[n - 1], (
                    f"B^{k}: non-monotone at n={n}: {dims[n]} < {dims[n-1]}"
                )

    def test_inverse_macmahon_changes_sign(self):
        """1/M(q) coefficients oscillate (from prod (1-q^n)^n cancellation)."""
        inv = bar_euler_char_by_degree(12)
        # Verify it has both positive and negative terms
        has_pos = any(inv[n] > 0 for n in range(1, 12))
        has_neg = any(inv[n] < 0 for n in range(1, 12))
        assert has_pos and has_neg, "1/M(q) should have both signs"

    def test_macmahon_is_positive(self):
        """M(q) has all positive coefficients (plane partition counts >= 0)."""
        mac = macmahon_coefficients(20)
        for n in range(20):
            assert mac[n] > 0, f"M(q) at q^{n} should be positive"
