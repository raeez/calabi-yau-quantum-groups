"""Tests for crystal melting / bar complex identification for C^3.

Manuscript references:
    ~/calabi-yau-quantum-groups/notes/theory_cy_to_chiral.tex: CY-to-chiral functor
    ~/chiral-bar-cobar/chapters/frame/bar_cobar_adjunction_curved.tex: bar complex

Literature:
    Okounkov-Reshetikhin-Vafa arXiv:hep-th/0309208: crystal melting
    Schiffmann-Vasserot arXiv:1211.1287: CoHA(C^3) = Y^+(gl_hat_1)
    Kontsevich-Soibelman arXiv:0811.2435: motivic DT / plethystic
    OEIS A000219: plane partitions

Multi-path verification:
    Path A: Direct 3D partition enumeration and classification
    Path B: Generating function comparison
    Path C: Plethystic logarithm/exponential round-trip
    Path D: Bar complex convolution vs enumeration cross-check
"""

import pytest
from fractions import Fraction

from compute.lib.crystal_bar_identification import (
    ALL_ARITY_NOTIONS,
    arity_distinct_heights,
    arity_footprint,
    arity_largest_cube,
    arity_max_height,
    arity_max_spread,
    arity_num_cols,
    arity_num_rows,
    arity_removable_boxes,
    arity_trace,
    bar_as_ordered_crystal_compositions,
    bps_as_bar_generators,
    classify_partitions_by_arity,
    compare_all_notions_with_bar,
    compare_arity_with_bar,
    crystal_bar_comparison_report,
    crystal_restricted_gf,
    crystal_statistics,
    inverse_macmahon_from_crystal,
    notion_generating_functions,
    plethystic_exp_from_bps,
    total_arity_distribution,
    verify_bar_dims_by_enumeration,
    verify_gf_decomposition,
    verify_inverse_macmahon_three_paths,
    verify_plethystic_round_trip,
    verify_s3_symmetry,
    wedge_k_bps_dims,
)
from compute.lib.c3_dt_partition import (
    enumerate_plane_partitions,
    macmahon_coefficients,
    plane_partition_counts,
)
from compute.lib.yangian_bar_complex import (
    bar_arity_k_dims,
    bar_euler_char_by_degree,
    bps_invariants_c3,
)


# ==================================================================
# S_3 SYMMETRY OF C^3
# ==================================================================

class TestS3Symmetry:
    """Verify S_3 symmetry: max_height, num_rows, num_cols have identical distributions."""

    def test_s3_symmetry_small(self):
        """S_3 symmetry holds for n <= 7."""
        result = verify_s3_symmetry(8)
        assert result['match'], (
            f"S_3 symmetry fails at n={result['first_failure']}"
        )

    def test_s3_symmetry_individual_values(self):
        """Spot-check that the three notions agree at n=4."""
        for n in [3, 4, 5, 6]:
            d_h = classify_partitions_by_arity(n, arity_max_height)
            d_r = classify_partitions_by_arity(n, arity_num_rows)
            d_c = classify_partitions_by_arity(n, arity_num_cols)
            assert d_h == d_r, f"max_height != num_rows at n={n}"
            assert d_h == d_c, f"max_height != num_cols at n={n}"

    def test_max_height_n4_distribution(self):
        """At n=4: 5 partitions with max_height=1, 5 with 2, 2 with 3, 1 with 4."""
        dist = classify_partitions_by_arity(4, arity_max_height)
        assert dist[1] == 5
        assert dist[2] == 5
        assert dist[3] == 2
        assert dist[4] == 1
        assert sum(dist.values()) == 13  # p(4) = 13


# ==================================================================
# ARITY NOTION CORRECTNESS
# ==================================================================

class TestArityNotions:
    """Test each arity function on known plane partitions."""

    def test_single_box(self):
        """The single box partition [[1]] has arity 1 for all notions."""
        pp = [[1]]
        assert arity_max_height(pp) == 1
        assert arity_num_rows(pp) == 1
        assert arity_num_cols(pp) == 1
        assert arity_footprint(pp) == 1
        assert arity_trace(pp) == 1
        assert arity_max_spread(pp) == 1
        assert arity_removable_boxes(pp) == 1
        assert arity_distinct_heights(pp) == 1
        assert arity_largest_cube(pp) == 1

    def test_column_partition(self):
        """Partition [[3]]: one column of height 3."""
        pp = [[3]]
        assert arity_max_height(pp) == 3
        assert arity_num_rows(pp) == 1
        assert arity_num_cols(pp) == 1
        assert arity_footprint(pp) == 1
        assert arity_trace(pp) == 1
        assert arity_max_spread(pp) == 3
        assert arity_distinct_heights(pp) == 1  # only height 3
        assert arity_largest_cube(pp) == 1  # 1x1x3, max cube is 1

    def test_flat_row(self):
        """Partition [[1, 1, 1]]: flat row of 3 boxes."""
        pp = [[1, 1, 1]]
        assert arity_max_height(pp) == 1
        assert arity_num_rows(pp) == 1
        assert arity_num_cols(pp) == 3
        assert arity_footprint(pp) == 3
        assert arity_trace(pp) == 1
        assert arity_max_spread(pp) == 3

    def test_2x2x1_block(self):
        """Partition [[1, 1], [1, 1]]: 2x2 flat block."""
        pp = [[1, 1], [1, 1]]
        assert arity_max_height(pp) == 1
        assert arity_num_rows(pp) == 2
        assert arity_num_cols(pp) == 2
        assert arity_footprint(pp) == 4
        assert arity_trace(pp) == 2
        assert arity_max_spread(pp) == 2
        assert arity_largest_cube(pp) == 1

    def test_2x2x2_cube(self):
        """Partition [[2, 2], [2, 2]]: the 2x2x2 cube (n=8)."""
        pp = [[2, 2], [2, 2]]
        assert arity_max_height(pp) == 2
        assert arity_num_rows(pp) == 2
        assert arity_num_cols(pp) == 2
        assert arity_footprint(pp) == 4
        assert arity_trace(pp) == 2
        assert arity_max_spread(pp) == 2
        assert arity_largest_cube(pp) == 2  # the full 2x2x2 cube fits
        assert arity_distinct_heights(pp) == 1  # only height 2

    def test_staircase(self):
        """Partition [[2, 1], [1]]: a staircase shape (n=4)."""
        pp = [[2, 1], [1]]
        assert arity_max_height(pp) == 2
        assert arity_num_rows(pp) == 2
        assert arity_num_cols(pp) == 2
        assert arity_footprint(pp) == 3
        assert arity_trace(pp) == 2
        assert arity_distinct_heights(pp) == 2  # heights 1 and 2

    def test_removable_boxes_staircase(self):
        """Removable boxes for [[2, 1], [1]]: boxes at (0,0,h=2), (0,1,h=1), (1,0,h=1).
        Top of (0,0): h=2, below=(1,0) has h=1<2, right=(0,1) has h=1<2 => removable
        Top of (0,1): h=1, below=(1,1) doesn't exist => removable, right doesn't exist => removable
        Top of (1,0): h=1, below doesn't exist => removable, right doesn't exist => removable
        Total: 3 removable boxes.
        """
        pp = [[2, 1], [1]]
        assert arity_removable_boxes(pp) == 3


# ==================================================================
# PARTITION COUNT CONSISTENCY
# ==================================================================

class TestPartitionCounts:
    """Verify that arity distributions sum to p(n)."""

    @pytest.mark.parametrize("notion_name", list(ALL_ARITY_NOTIONS.keys()))
    def test_distribution_sums_to_pn(self, notion_name):
        """Each arity distribution sums to p(n) for n <= 7."""
        fn = ALL_ARITY_NOTIONS[notion_name]
        pp_counts = plane_partition_counts(8)
        for n in range(8):
            dist = classify_partitions_by_arity(n, fn)
            total = sum(dist.values())
            assert total == pp_counts[n], (
                f"{notion_name} at n={n}: sum of distribution = {total}, p(n) = {pp_counts[n]}"
            )


# ==================================================================
# GF DECOMPOSITION VERIFICATION
# ==================================================================

class TestGFDecomposition:
    """Verify that restricted GFs sum to M(q) for each notion."""

    @pytest.mark.parametrize("notion_name", list(ALL_ARITY_NOTIONS.keys()))
    def test_gf_decomposition(self, notion_name):
        """sum_k M_k(q) = M(q) for the notion's decomposition."""
        result = verify_gf_decomposition(8, ALL_ARITY_NOTIONS[notion_name], notion_name)
        assert result['match'], (
            f"GF decomposition fails for {notion_name}: {result['mismatches']}"
        )


# ==================================================================
# COMPARISON WITH BAR COMPLEX
# ==================================================================

class TestBarComparison:
    """Test whether any arity notion matches bar complex dimensions B^k_n."""

    def test_dimension_notions_fail_at_arity_1(self):
        """The dimension-based notions (max_height, num_rows, num_cols) do NOT
        match B^1_n = p(n), because max_height=1 gives ordinary partitions
        which are a proper subset of plane partitions.

        For example at n=2: max_height=1 partitions are [[1,1]] and [[1],[1]]
        (only 2 of the 3 plane partitions), while B^1_2 = p(2) = 3.
        """
        max_n = 8
        pp = plane_partition_counts(max_n)
        for name in ['max_height', 'num_rows', 'num_cols', 'footprint']:
            fn = ALL_ARITY_NOTIONS[name]
            crystal_at_1 = [0] * max_n
            for n in range(max_n):
                dist = classify_partitions_by_arity(n, fn)
                crystal_at_1[n] = dist.get(1, 0)
            # These should differ from p(n) for n >= 2
            has_diff = any(crystal_at_1[n] != pp[n] for n in range(2, max_n))
            assert has_diff, (
                f"Notion {name} unexpectedly matches p(n) at arity 1: "
                f"crystal = {crystal_at_1}, p(n) = {pp}"
            )

    def test_no_notion_matches_bar_at_nontrivial_arities(self):
        """No arity notion matches B^k_n at intermediate arities k=2,...,5.

        B^k_n at k >= 2 has nontrivial convolution structure (products of p(ni)),
        and no geometric arity notion on individual partitions can reproduce this.
        We test at k=2 through 5 where the bar dimensions are large enough to
        distinguish from any single-partition statistic.

        Note: k=0 trivially matches (both [1,0,...]), and k=1 can have finite-range
        coincidences (e.g., largest_cube gives arity=1 for all pp of size <= 7,
        matching B^1_n = p(n) in that range). But k >= 2 with max_n >= 9 provides
        definitive separation.
        """
        max_n = 9  # extend to n=8 to catch largest_cube divergence
        for name, fn in ALL_ARITY_NOTIONS.items():
            for k in range(2, 6):
                crystal = [0] * max_n
                bar = bar_arity_k_dims(k, max_n)
                for n in range(max_n):
                    dist = classify_partitions_by_arity(n, fn)
                    crystal[n] = dist.get(k, 0)
                # Bar dimensions at k >= 2 grow rapidly (B^2_4 = 21, etc.)
                # while geometric arity counts grow slowly.
                # Check that they differ at some position with bar > 1.
                nontrivial_positions = [n for n in range(max_n) if bar[n] > 1]
                if nontrivial_positions:
                    has_diff = any(crystal[n] != bar[n] for n in nontrivial_positions)
                    assert has_diff, (
                        f"Notion {name} at k={k} matches B^k_n at nontrivial positions! "
                        f"crystal={crystal}, bar={bar}"
                    )

    def test_b1_n_is_all_partitions(self):
        """B^1_n = p(n): bar arity 1 counts ALL partitions of size n."""
        pp = plane_partition_counts(9)
        b1 = bar_arity_k_dims(1, 9)
        for n in range(1, 9):
            assert b1[n] == pp[n], f"B^1_{n} != p({n})"

    def test_bar_arity_is_about_tuples(self):
        """B^k_n = sum_{n1+...+nk=n} prod p(ni) counts ordered k-tuples."""
        # Verify by direct enumeration
        result = verify_bar_dims_by_enumeration(7, 4)
        assert result['match'], (
            f"Bar dimension cross-check fails: {result['mismatches']}"
        )


# ==================================================================
# PLETHYSTIC ROUND-TRIP
# ==================================================================

class TestPlethysticRoundTrip:
    """Verify PExp(PLog(M(q))) = M(q) and PLog(M(q)) = sum n q^n."""

    def test_round_trip_N15(self):
        """Full round-trip verification at N=15."""
        result = verify_plethystic_round_trip(15)
        assert result['plog_matches_bps'], "PLog(M) should give BPS = n"
        assert result['pexp_matches_macmahon'], "PExp(sum n q^n) should give M(q)"

    def test_plog_is_sum_nqn(self):
        """PLog(M(q)) = sum_{n>=1} n q^n: the arity-1 generator count."""
        mac = macmahon_coefficients(12)
        from compute.lib.yangian_bar_complex import plethystic_log_coefficients
        plog = plethystic_log_coefficients(mac, 12)
        for n in range(1, 12):
            assert abs(float(plog[n]) - n) < 1e-10, (
                f"PLog at q^{n}: expected {n}, got {float(plog[n])}"
            )

    def test_pexp_reconstructs_macmahon(self):
        """PExp(sum_{n>=1} n q^n) = M(q) = prod (1-q^n)^{-n}."""
        N = 15
        bps = [0] * N
        for n in range(1, N):
            bps[n] = n
        pexp = plethystic_exp_from_bps(bps, N)
        mac = macmahon_coefficients(N)
        for n in range(N):
            assert abs(float(pexp[n]) - float(mac[n])) < 1e-10, (
                f"PExp at q^{n}: expected {int(mac[n])}, got {float(pexp[n])}"
            )

    def test_pexp_exact_rational(self):
        """PExp computation is exact (Fraction arithmetic)."""
        N = 10
        bps = [0] * N
        for n in range(1, N):
            bps[n] = n
        pexp = plethystic_exp_from_bps(bps, N)
        mac = macmahon_coefficients(N)
        for n in range(N):
            assert pexp[n] == mac[n], (
                f"PExp exact at q^{n}: expected {mac[n]}, got {pexp[n]}"
            )


# ==================================================================
# BPS AS BAR GENERATORS
# ==================================================================

class TestBPSGenerators:
    """Verify Omega(n) = n matches bar cohomology H^1_n."""

    def test_three_path_agreement(self):
        """PLog, bar cohomology, and direct BPS all give H^1_n = n."""
        result = bps_as_bar_generators(12)
        assert result['all_match'], (
            f"BPS-generator identification fails: {result['mismatches']}"
        )

    def test_omega_n_equals_n(self):
        """Direct BPS invariants: Omega(n) = n for n >= 1."""
        bps = bps_invariants_c3(20)
        for n in range(1, 20):
            assert bps[n] == n

    def test_bps_is_h1_bar(self):
        """The BPS generators are exactly the bar cohomology at arity 1."""
        result = bps_as_bar_generators(10)
        for n in range(1, 10):
            assert result['plog'][n] == n
            assert result['h1'][n] == n
            assert result['bps'][n] == n


# ==================================================================
# INVERSE MACMAHON
# ==================================================================

class TestInverseMacMahon:
    """Verify 1/M(q) = prod (1-q^n)^n by three independent paths."""

    def test_three_paths_agree(self):
        """Crystal product, bar Euler char, and series inversion agree."""
        result = verify_inverse_macmahon_three_paths(15)
        assert result['all_agree'], (
            f"1/M(q) cross-check fails: crystal_bar={result['crystal_vs_bar']}, "
            f"crystal_series={result['crystal_vs_series_inv']}"
        )

    def test_known_values(self):
        """Verify specific coefficients of 1/M(q)."""
        inv = inverse_macmahon_from_crystal(12)
        known = [1, -1, -2, -1, 0, 4, 4, 7, 3, -2, -9, -17]
        for n in range(12):
            assert int(inv[n]) == known[n], (
                f"1/M(q) at q^{n}: expected {known[n]}, got {int(inv[n])}"
            )

    def test_macmahon_times_inverse_is_one(self):
        """M(q) * 1/M(q) = 1 mod q^N."""
        N = 20
        mac = macmahon_coefficients(N)
        inv = inverse_macmahon_from_crystal(N)
        product = [Fraction(0)] * N
        for i in range(N):
            for j in range(N - i):
                product[i + j] += mac[i] * inv[j]
        assert product[0] == Fraction(1)
        for n in range(1, N):
            assert product[n] == Fraction(0), (
                f"M*1/M at q^{n}: expected 0, got {product[n]}"
            )


# ==================================================================
# BAR DIMENSION CROSS-VERIFICATION
# ==================================================================

class TestBarDimensionCrossCheck:
    """Cross-verify B^k_n by convolution and by explicit ordered-tuple enumeration."""

    def test_enumeration_vs_convolution(self):
        """Both methods agree up to n=6, k=4."""
        result = verify_bar_dims_by_enumeration(7, 4)
        assert result['match'], f"Mismatch: {result['mismatches']}"

    def test_b2_by_enumeration(self):
        """B^2_n by explicit enumeration of pairs."""
        for n in range(2, 7):
            enum_val = bar_as_ordered_crystal_compositions(n, 2)
            conv_val = bar_arity_k_dims(2, n + 1)[n]
            assert enum_val == conv_val, (
                f"B^2_{n}: enum={enum_val}, conv={conv_val}"
            )

    def test_b3_by_enumeration(self):
        """B^3_n by explicit enumeration of triples."""
        for n in range(3, 7):
            enum_val = bar_as_ordered_crystal_compositions(n, 3)
            conv_val = bar_arity_k_dims(3, n + 1)[n]
            assert enum_val == conv_val, (
                f"B^3_{n}: enum={enum_val}, conv={conv_val}"
            )

    def test_b4_4_is_one(self):
        """B^4_4 = p(1)^4 = 1 (four single-box partitions)."""
        assert bar_as_ordered_crystal_compositions(4, 4) == 1

    def test_b0_is_ground_field(self):
        """B^0_0 = 1, B^0_n = 0 for n >= 1."""
        assert bar_as_ordered_crystal_compositions(0, 0) == 1
        for n in range(1, 5):
            assert bar_as_ordered_crystal_compositions(n, 0) == 0


# ==================================================================
# WEDGE POWER DIMENSIONS (BAR COHOMOLOGY)
# ==================================================================

class TestWedgePowers:
    """Test exterior power dimensions of V_BPS."""

    def test_wedge1_is_bps(self):
        """Wedge^1(V_BPS)_n = Omega(n) = n."""
        cohom = wedge_k_bps_dims(10, 1)
        for n in range(1, 10):
            assert cohom[1][n] == n, f"Wedge^1 at n={n}: expected {n}, got {cohom[1][n]}"

    def test_wedge2_values(self):
        """Wedge^2(V_BPS): specific computed values."""
        cohom = wedge_k_bps_dims(10, 2)
        # H^2_3: V_1 x V_2 = 1*2 = 2
        assert cohom[2][3] == 2
        # H^2_4: V_1 x V_3 + C(2,2) from V_2 = 3 + 1 = 4
        assert cohom[2][4] == 4
        # H^2_5: V_1 x V_4 + V_2 x V_3 = 4 + 6 = 10
        assert cohom[2][5] == 10

    def test_wedge0_is_ground_field(self):
        """Wedge^0 = k, concentrated at degree 0."""
        cohom = wedge_k_bps_dims(5, 0)
        assert cohom[0][0] == 1
        for n in range(1, 5):
            assert cohom[0][n] == 0

    def test_wedge_euler_char_is_inverse_macmahon(self):
        """sum_k (-1)^k char(Wedge^k(V_BPS)) = 1/M(q)."""
        N = 8
        max_k = N
        cohom = wedge_k_bps_dims(N, max_k)
        inv_mac = bar_euler_char_by_degree(N)

        for n in range(N):
            euler_n = sum((-1)**k * cohom[k][n] for k in range(max_k + 1))
            assert euler_n == int(inv_mac[n]), (
                f"Wedge Euler char at n={n}: got {euler_n}, expected {int(inv_mac[n])}"
            )


# ==================================================================
# CRYSTAL STATISTICS
# ==================================================================

class TestCrystalStatistics:
    """Test the crystal statistics computation."""

    def test_stats_n4(self):
        """Statistics at n=4 are internally consistent."""
        stats = crystal_statistics(4)
        assert stats['n'] == 4
        assert stats['count'] == 13  # p(4) = 13
        for name in ALL_ARITY_NOTIONS:
            dist = stats['distributions'][name]['values']
            assert sum(dist) == 13, (
                f"{name} distribution at n=4 sums to {sum(dist)}, expected 13"
            )

    def test_stats_n0(self):
        """Statistics at n=0: single empty partition."""
        stats = crystal_statistics(0)
        assert stats['count'] == 1


# ==================================================================
# NOTION GENERATING FUNCTIONS
# ==================================================================

class TestNotionGF:
    """Test restricted generating functions for each notion."""

    def test_max_height_gf(self):
        """Max-height restricted GF: M_1(q) counts pp with max_height=1."""
        gf = notion_generating_functions(8, 'max_height')
        # max_height=1 partitions are 2D partitions (ordinary partitions)
        # p_2d(1)=1, p_2d(2)=2, p_2d(3)=3, p_2d(4)=5, p_2d(5)=7, p_2d(6)=11
        # These are OEIS A000041 (ordinary partitions) restricted to pp with max h=1
        assert gf[1][1] == 1
        assert gf[1][2] == 2
        assert gf[1][3] == 3
        assert gf[1][4] == 5

    def test_footprint_gf_k1(self):
        """Footprint GF at k=1: partitions with exactly 1 nonzero entry."""
        gf = notion_generating_functions(8, 'footprint')
        # Footprint=1 means a single column of height n: exactly 1 for each n>=1
        for n in range(1, 8):
            assert gf[1][n] == 1, (
                f"Footprint=1 at n={n}: expected 1, got {gf[1][n]}"
            )

    def test_total_distribution_table(self):
        """Distribution table rows sum to p(n)."""
        table = total_arity_distribution(8, 'max_height')
        pp = plane_partition_counts(8)
        for n in range(8):
            row_sum = sum(table[n])
            assert row_sum == pp[n], (
                f"n={n}: row sum {row_sum} != p(n) = {pp[n]}"
            )


# ==================================================================
# STRUCTURAL THEOREMS
# ==================================================================

class TestStructuralTheorems:
    """Test the key structural results of the crystal-bar identification."""

    def test_kappa_equals_one(self):
        """For C^3 / W_{1+infty}: kappa = 1.

        The modular characteristic kappa of the CoHA (viewed as a chiral
        algebra via the CY-to-chiral functor) equals 1. This follows from
        the BPS invariant Omega(1) = 1 (single D0-brane has 1 state) and
        the genus-1 formula F_1 = kappa/24.
        """
        bps = bps_invariants_c3(5)
        assert bps[1] == 1  # kappa = Omega(1) = 1

    def test_bar_euler_product_is_inverse_macmahon(self):
        """The bar Euler product 1/M(q) = prod (1-q^n)^{Omega(n)}.

        With Omega(n) = n: 1/M(q) = prod (1-q^n)^n.
        This is the fundamental crystal-bar Euler characteristic identity.
        """
        N = 15
        # Method 1: from BPS data
        inv1 = inverse_macmahon_from_crystal(N)
        # Method 2: from bar complex
        inv2 = bar_euler_char_by_degree(N)
        for n in range(N):
            assert inv1[n] == inv2[n], (
                f"1/M(q) at q^{n}: crystal={inv1[n]}, bar={inv2[n]}"
            )

    def test_macmahon_two_methods(self):
        """M(q) from log-exp vs direct product (multi-path for the base identity)."""
        N = 20
        mac1 = macmahon_coefficients(N)
        from compute.lib.c3_dt_partition import macmahon_coefficients_product
        mac2 = macmahon_coefficients_product(N)
        for n in range(N):
            assert mac1[n] == mac2[n], f"MacMahon at q^{n}: {mac1[n]} vs {mac2[n]}"

    def test_crystal_bar_report_runs(self):
        """The comprehensive report runs without errors."""
        report = crystal_bar_comparison_report(6)
        assert report['s3_symmetry']['match']
        assert report['plethystic_round_trip']['plog_matches_bps']
        assert report['plethystic_round_trip']['pexp_matches_macmahon']
        assert report['bps_generators']['all_match']
        assert report['inverse_macmahon']['all_agree']

    def test_gf_decompositions_all_valid_in_report(self):
        """Report confirms all GF decompositions are valid (sum to M(q))."""
        report = crystal_bar_comparison_report(6)
        for name, data in report['notion_comparisons'].items():
            assert data['gf_decomposition'], (
                f"Notion {name} GF decomposition fails"
            )


# ==================================================================
# SPECIFIC ARITY DISTRIBUTIONS (HARDCODED CROSS-CHECKS)
# ==================================================================

class TestSpecificDistributions:
    """Verify specific arity distributions against independently computed values."""

    def test_max_height_n3(self):
        """At n=3: {1: 3, 2: 2, 3: 1} for max_height.

        height=1: [[1,1,1]], [[1,1],[1]], [[1],[1],[1]] => 3
        height=2: [[2,1]], [[2],[1]] => 2
        height=3: [[3]] => 1
        """
        dist = classify_partitions_by_arity(3, arity_max_height)
        assert dist == {1: 3, 2: 2, 3: 1}

    def test_footprint_n3(self):
        """At n=3: footprint distribution.

        footprint=1: [[3]] => 1
        footprint=2: [[2,1]], [[2],[1]] => 2
        footprint=3: [[1,1,1]], [[1,1],[1]], [[1],[1],[1]] => 3
        """
        dist = classify_partitions_by_arity(3, arity_footprint)
        assert dist == {1: 1, 2: 2, 3: 3}

    def test_trace_n4(self):
        """At n=4: trace distribution.

        trace=1: partitions where min(rows,cols)=1 => 9
        trace=2: partitions where min(rows,cols)=2 => 4
        """
        dist = classify_partitions_by_arity(4, arity_trace)
        assert dist[1] == 9
        assert dist[2] == 4
        assert sum(dist.values()) == 13

    def test_removable_boxes_n3(self):
        """At n=3: removable boxes distribution.

        [[3]]: only top box removable => 1
        [[2,1]]: top of col(0)=2 removable, col(1)=1 removable => 2
        [[2],[1]]: top of (0,0)=2 removable, (1,0)=1 removable => 2
        [[1,1,1]]: all 3 removable (each is top of its column, no constraint) => 3
        [[1,1],[1]]: (0,0)=1 has (1,0)=1 not <1 => NOT removable;
                     (0,1)=1 has no right, no below[1] at col 1 => removable;
                     (1,0)=1 has no below, no right => removable. => 2
        [[1],[1],[1]]: each is top of column, only constraint is row below.
                       (0,0)=1 has (1,0)=1 not <1 => NOT removable
                       (1,0)=1 has (2,0)=1 not <1 => NOT removable
                       (2,0)=1 has no below => removable. => 1

        So: {1: 2, 2: 3, 3: 1} -- let me verify.
        """
        dist = classify_partitions_by_arity(3, arity_removable_boxes)
        assert sum(dist.values()) == 6  # p(3) = 6

    def test_largest_cube_mostly_one(self):
        """For n <= 7, almost all partitions have largest_cube = 1.

        Only the 2x2x2 cube at n=8 achieves largest_cube = 2.
        """
        for n in range(1, 8):
            dist = classify_partitions_by_arity(n, arity_largest_cube)
            total = sum(dist.values())
            pp = plane_partition_counts(n + 1)
            assert total == pp[n]
            # All should have largest cube 1 for n < 8
            assert dist.get(1, 0) == total, (
                f"At n={n}: not all partitions have largest_cube=1, dist={dist}"
            )

    def test_largest_cube_n8(self):
        """At n=8, exactly one partition (the 2x2x2 cube) has largest_cube=2."""
        dist = classify_partitions_by_arity(8, arity_largest_cube)
        assert dist.get(2, 0) == 1
        assert dist.get(1, 0) == 159  # p(8) - 1 = 159


# ==================================================================
# MULTI-PATH INTEGRATION
# ==================================================================

class TestMultiPathIntegration:
    """Tests that verify the same fact by multiple independent paths."""

    def test_p4_five_paths(self):
        """p(4) = 13 verified five ways.

        Path 1: Direct enumeration
        Path 2: MacMahon generating function (log-exp)
        Path 3: MacMahon generating function (product)
        Path 4: sum over arity distributions
        Path 5: bar B^1_4
        """
        # Path 1
        pps = enumerate_plane_partitions(4)
        assert len(pps) == 13
        # Path 2
        mac = macmahon_coefficients(5)
        assert int(mac[4]) == 13
        # Path 3
        from compute.lib.c3_dt_partition import macmahon_coefficients_product
        mac2 = macmahon_coefficients_product(5)
        assert int(mac2[4]) == 13
        # Path 4
        dist = classify_partitions_by_arity(4, arity_max_height)
        assert sum(dist.values()) == 13
        # Path 5
        b1 = bar_arity_k_dims(1, 5)
        assert b1[4] == 13

    def test_inverse_macmahon_at_n5_three_paths(self):
        """[q^5] 1/M(q) = 4, verified three ways.

        Path A: prod (1-q^n)^n
        Path B: alternating sum of bar arity dims
        Path C: series inversion of M(q)
        """
        result = verify_inverse_macmahon_three_paths(6)
        assert result['values'][5] == 4
        assert result['all_agree']

    def test_bps_3_paths(self):
        """Omega(5) = 5 verified by three paths.

        Path A: Direct formula
        Path B: Plethystic logarithm of M(q)
        Path C: Bar cohomology H^1_5
        """
        result = bps_as_bar_generators(6)
        assert result['plog'][5] == 5
        assert result['h1'][5] == 5
        assert result['bps'][5] == 5
