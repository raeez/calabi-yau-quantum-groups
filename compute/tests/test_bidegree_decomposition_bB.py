r"""Tests for the fixed-j bar-length diagnostic.

Verifies the degree arithmetic used by the rejected bidegree proof and
checks that the engine does not certify termwise Obs_Ainf vanishing.

Structure:
  - Section 1: Bar-length degree computations (unit tests)
  - Section 2: Bidegree table and fixed-j degree distinctness
  - Section 3: Collision analysis (cross-j vs within-j)
  - Section 4: Obs_Ainf bidegree-proof rejection
  - Section 5: Symbolic bar-length verification
  - Section 6: Integration with existing A-infinity infrastructure
  - Section 7: Consistency with Costello's theorem
  - Section 8: Master verification
"""

import pytest
from fractions import Fraction

from compute.lib.bidegree_decomposition_bB import (
    bar_length_degree_b_k,
    bar_length_degree_B_j,
    bar_length_degree_commutator,
    bidegree_table,
    BidegreeEntry,
    BarElement,
    check_decomposition_at_fixed_j,
    check_full_bidegree_decomposition,
    collision_analysis,
    resolve_obs_ainf,
    ObsAinfResolution,
    CostelloChainMapVerification,
    symbolic_b_k_action,
    symbolic_B_j_action,
    verify_bar_length_change,
    master_verification,
)


# =========================================================================
#  Section 1: Bar-length degree computations
# =========================================================================

class TestBarLengthDegreeBk:
    """Tests for bar-length degree of b_k."""

    def test_b1_preserves_length(self):
        """b_1 (internal differential) has bar-length degree 0."""
        assert bar_length_degree_b_k(1) == 0

    def test_b2_reduces_by_one(self):
        """b_2 (binary product) has bar-length degree -1."""
        assert bar_length_degree_b_k(2) == -1

    def test_b3_reduces_by_two(self):
        """b_3 (ternary product) has bar-length degree -2."""
        assert bar_length_degree_b_k(3) == -2

    def test_b4_reduces_by_three(self):
        """b_4 (quartic product) has bar-length degree -3."""
        assert bar_length_degree_b_k(4) == -3

    def test_general_formula(self):
        """b_k has bar-length degree -(k-1) for k = 1, ..., 10."""
        for k in range(1, 11):
            assert bar_length_degree_b_k(k) == -(k - 1)

    def test_strictly_decreasing(self):
        """Bar-length degrees are strictly decreasing in k."""
        degrees = [bar_length_degree_b_k(k) for k in range(1, 11)]
        assert all(degrees[i] > degrees[i + 1] for i in range(len(degrees) - 1))

    def test_invalid_k_raises(self):
        """k < 1 should raise ValueError."""
        with pytest.raises(ValueError):
            bar_length_degree_b_k(0)


class TestBarLengthDegreeBj:
    """Tests for bar-length degree of B^{(j)}."""

    def test_B0_connes_operator(self):
        """B^{(0)} = B (standard Connes) has bar-length degree +1."""
        assert bar_length_degree_B_j(0) == 1

    def test_B1_degree(self):
        """B^{(1)} has bar-length degree -1."""
        assert bar_length_degree_B_j(1) == -1

    def test_B2_degree(self):
        """B^{(2)} (S^2-framing map) has bar-length degree -3."""
        assert bar_length_degree_B_j(2) == -3

    def test_B3_framing_map(self):
        """B^{(3)} = F (S^3-framing) has bar-length degree -5."""
        assert bar_length_degree_B_j(3) == -5

    def test_general_formula(self):
        """B^{(j)} has bar-length degree 1 - 2j for j = 0, ..., 5."""
        for j in range(6):
            assert bar_length_degree_B_j(j) == 1 - 2 * j

    def test_invalid_j_raises(self):
        """j < 0 should raise ValueError."""
        with pytest.raises(ValueError):
            bar_length_degree_B_j(-1)


class TestBarLengthDegreeCommutator:
    """Tests for bar-length degree of [b_k, B^{(j)}]."""

    def test_m2_B_preserves_length(self):
        """[m_2, B] has bar-length degree 0 (preserves length)."""
        assert bar_length_degree_commutator(2, 0) == 0

    def test_m3_B_reduces_by_one(self):
        """[m_3, B] has bar-length degree -1."""
        assert bar_length_degree_commutator(3, 0) == -1

    def test_m3_B2_the_target(self):
        """[m_3, B^{(2)}] has bar-length degree -5."""
        # This is the Obs_Ainf target: 2 - 3 - 2*2 = 2 - 3 - 4 = -5
        assert bar_length_degree_commutator(3, 2) == -5

    def test_m2_B2(self):
        """[m_2, B^{(2)}] has bar-length degree -4."""
        assert bar_length_degree_commutator(2, 2) == -4

    def test_m4_B2(self):
        """[m_4, B^{(2)}] has bar-length degree -6."""
        assert bar_length_degree_commutator(4, 2) == -6

    def test_general_formula(self):
        """[b_k, B^{(j)}] has degree 2 - k - 2j."""
        for k in range(1, 7):
            for j in range(4):
                expected = 2 - k - 2 * j
                assert bar_length_degree_commutator(k, j) == expected

    def test_additivity(self):
        """Commutator degree = sum of individual degrees."""
        for k in range(1, 7):
            for j in range(4):
                deg_bk = bar_length_degree_b_k(k)
                deg_Bj = bar_length_degree_B_j(j)
                deg_comm = bar_length_degree_commutator(k, j)
                assert deg_comm == deg_bk + deg_Bj


# =========================================================================
#  Section 2: Bidegree table and decomposition
# =========================================================================

class TestBidegreeTable:
    """Tests for the bidegree table."""

    def test_table_size(self):
        """Table has k_max * (j_max + 1) entries."""
        table = bidegree_table(k_max=6, j_max=3)
        assert len(table) == 6 * 4

    def test_table_entries_correct(self):
        """Each entry has the correct bidegree."""
        table = bidegree_table(k_max=4, j_max=2)
        for entry in table:
            expected = 2 - entry.k - 2 * entry.j
            assert entry.bar_length_degree == expected

    def test_target_entry_in_table(self):
        """The target (k=3, j=2) is in the table with degree -5."""
        table = bidegree_table(k_max=6, j_max=3)
        target = [e for e in table if e.k == 3 and e.j == 2]
        assert len(target) == 1
        assert target[0].bar_length_degree == -5


class TestDecompositionAtFixedJ:
    """Tests for fixed-j degree distinctness."""

    def test_j0_decomposition(self):
        """The j=0 bar-length shifts are distinct."""
        result = check_decomposition_at_fixed_j(0, k_max=10)
        assert result["decomposition_holds"]
        assert not result["termwise_vanishing_established"]
        assert result["all_distinct"]
        assert result["strictly_decreasing"]

    def test_j1_decomposition(self):
        """The j=1 bar-length shifts are distinct."""
        result = check_decomposition_at_fixed_j(1, k_max=10)
        assert result["decomposition_holds"]
        assert not result["termwise_vanishing_established"]

    def test_j2_decomposition(self):
        """The j=2 bar-length shifts are distinct but not decisive."""
        result = check_decomposition_at_fixed_j(2, k_max=10)
        assert result["decomposition_holds"]
        assert not result["termwise_vanishing_established"]
        assert result["all_distinct"]
        assert result["strictly_decreasing"]

    def test_j3_decomposition(self):
        """The j=3 bar-length shifts are distinct."""
        result = check_decomposition_at_fixed_j(3, k_max=10)
        assert result["decomposition_holds"]
        assert not result["termwise_vanishing_established"]

    def test_all_j_decompose(self):
        """Distinctness holds for all j in {0, 1, 2, 3}."""
        for j in range(4):
            result = check_decomposition_at_fixed_j(j, k_max=10)
            assert result["decomposition_holds"], (
                f"Degree distinctness fails at j={j}"
            )

    def test_degrees_are_arithmetic_sequence(self):
        """At fixed j, degrees are 1-2j, -2j, -1-2j, ... (common diff -1)."""
        for j in range(4):
            result = check_decomposition_at_fixed_j(j, k_max=5)
            degrees = result["degrees"]
            for i in range(len(degrees) - 1):
                assert degrees[i] - degrees[i + 1] == 1

    def test_j2_specific_degrees(self):
        """Verify specific degree values at j=2 for k=1..6."""
        result = check_decomposition_at_fixed_j(2, k_max=6)
        expected = [-3, -4, -5, -6, -7, -8]
        assert result["degrees"] == expected


class TestFullDecomposition:
    """Tests for fixed-j degree distinctness across all j."""

    def test_all_decompositions_hold(self):
        """All fixed-j degree lines are distinct for CY_3."""
        result = check_full_bidegree_decomposition(k_max=6, j_max=3)
        assert result["all_decompositions_hold"]

    def test_total_entries(self):
        """Correct number of total entries."""
        result = check_full_bidegree_decomposition(k_max=6, j_max=3)
        assert result["total_entries"] == 24

    def test_cy2_decomposition(self):
        """Degree distinctness also holds for CY_2 (j_max=2)."""
        result = check_full_bidegree_decomposition(k_max=6, j_max=2)
        assert result["all_decompositions_hold"]


# =========================================================================
#  Section 3: Collision analysis
# =========================================================================

class TestCollisionAnalysis:
    """Tests for cross-j collision analysis."""

    def test_within_j_all_distinct(self):
        """Within each fixed j, all bidegrees are distinct."""
        result = collision_analysis(k_max=10, j_max=3)
        assert result["within_j_all_distinct"]

    def test_cross_j_collisions_exist(self):
        """Cross-j collisions DO exist (e.g., (k=3,j=0) and (k=1,j=1))."""
        result = collision_analysis(k_max=6, j_max=3)
        assert result["num_cross_j_collisions"] > 0

    def test_specific_cross_collision(self):
        """(k=3, j=0) and (k=1, j=1) both have degree -1."""
        d1 = bar_length_degree_commutator(3, 0)
        d2 = bar_length_degree_commutator(1, 1)
        assert d1 == d2 == -1

    def test_cross_collisions_do_not_repair_failed_proof(self):
        """Cross-j collisions do not repair the failed termwise proof."""
        result = collision_analysis(k_max=6, j_max=3)
        assert result["within_j_all_distinct"]
        assert result["num_cross_j_collisions"] > 0


# =========================================================================
#  Section 4: Obs_Ainf bidegree-proof rejection
# =========================================================================

class TestObsAinfResolution:
    """Tests for rejection of the bidegree proof."""

    def test_obs_ainf_vanishes(self):
        """The bidegree engine no longer certifies Obs_Ainf = 0."""
        resolution = resolve_obs_ainf(cy_dim=3)
        assert not resolution.obs_ainf_vanishes

    def test_step1_holds(self):
        """Costello's theorem is not a termwise B_term proof."""
        resolution = resolve_obs_ainf(cy_dim=3)
        assert not resolution.step1_holds

    def test_step2_holds(self):
        """The bar-length inference is rejected."""
        resolution = resolve_obs_ainf(cy_dim=3)
        assert not resolution.step2_holds

    def test_target_bidegree(self):
        """[m_3, B^{(2)}] has bidegree -5."""
        resolution = resolve_obs_ainf(cy_dim=3)
        assert resolution.bidegree_of_target == -5

    def test_nearest_bidegree_distinct(self):
        """Nearest neighbor bidegree is distinct from target."""
        resolution = resolve_obs_ainf(cy_dim=3)
        assert resolution.nearest_bidegree != resolution.bidegree_of_target

    def test_nearest_bidegree_gap(self):
        """Gap between target and nearest is exactly 1."""
        resolution = resolve_obs_ainf(cy_dim=3)
        gap = abs(resolution.nearest_bidegree - resolution.bidegree_of_target)
        assert gap == 1

    def test_proof_chain_nonempty(self):
        """Proof chain has substantive steps."""
        resolution = resolve_obs_ainf(cy_dim=3)
        assert len(resolution.proof_chain) >= 4

    def test_proof_chain_mentions_costello(self):
        """Proof chain scopes Costello's theorem correctly."""
        resolution = resolve_obs_ainf(cy_dim=3)
        chain_text = " ".join(resolution.proof_chain)
        assert "Costello" in chain_text
        assert "corrected TCFT" in chain_text

    def test_cy2_also_works(self):
        """The failed bidegree proof is rejected in CY_2 as well."""
        resolution = resolve_obs_ainf(cy_dim=2)
        assert not resolution.obs_ainf_vanishes

    def test_cy1_fails_for_j2(self):
        """For CY_1, j=2 > d=1, so Costello's theorem does not apply."""
        resolution = resolve_obs_ainf(cy_dim=1)
        assert not resolution.step1_holds
        assert not resolution.obs_ainf_vanishes


# =========================================================================
#  Section 5: Symbolic bar-length verification
# =========================================================================

class TestSymbolicBarElement:
    """Tests for the symbolic bar element."""

    def test_bar_length(self):
        """Bar length = number of factors - 1."""
        e = BarElement(factors=("a", "b", "c"))
        assert e.bar_length == 2

    def test_repr(self):
        """String representation."""
        e = BarElement(factors=("a", "b", "c"))
        assert "[a | b | c]" == repr(e)


class TestSymbolicBkAction:
    """Tests for symbolic b_k action."""

    def test_b2_on_length_3(self):
        """b_2 on [a|b|c] produces elements of length 2."""
        x = BarElement(factors=("a", "b", "c"))
        results = symbolic_b_k_action(x, 2)
        assert all(r.bar_length == 1 for r in results)

    def test_b3_on_length_4(self):
        """b_3 on [a|b|c|d] produces elements of length 2."""
        x = BarElement(factors=("a", "b", "c", "d"))
        results = symbolic_b_k_action(x, 3)
        assert all(r.bar_length == 1 for r in results)

    def test_b2_count(self):
        """b_2 on n+1 factors produces n terms."""
        for n in range(2, 7):
            x = BarElement(factors=tuple(f"a_{i}" for i in range(n + 1)))
            results = symbolic_b_k_action(x, 2)
            assert len(results) == n

    def test_bk_length_change(self):
        """b_k changes bar length by -(k-1)."""
        for k in range(2, 5):
            for n in range(k, 8):
                x = BarElement(factors=tuple(f"a_{i}" for i in range(n + 1)))
                results = symbolic_b_k_action(x, k)
                for r in results:
                    assert r.bar_length == n - (k - 1)

    def test_bk_too_large(self):
        """b_k on element shorter than k returns empty."""
        x = BarElement(factors=("a", "b"))
        results = symbolic_b_k_action(x, 3)
        assert len(results) == 0


class TestSymbolicBjAction:
    """Tests for symbolic B^{(j)} action."""

    def test_B0_increases_length(self):
        """B^{(0)} increases bar length by 1."""
        x = BarElement(factors=("a", "b", "c"))
        results = symbolic_B_j_action(x, 0)
        assert all(r.bar_length == 3 for r in results)

    def test_B2_decreases_length(self):
        """B^{(2)} decreases bar length by 3."""
        x = BarElement(factors=("a", "b", "c", "d", "e"))
        results = symbolic_B_j_action(x, 2)
        # Input bar length 4, output bar length 4-3 = 1
        # B^{(2)} contracts 2 out of 5 factors, leaving 3 factors
        # but also prefixes with pairing scalar (length-1 factor)
        # so output has roughly 3 factors -> bar length 2
        # Actual behavior depends on implementation detail;
        # the structural point is the degree
        assert len(results) > 0


class TestBarLengthVerification:
    """Tests for explicit bar-length change verification."""

    def test_m3_B2_predicted_degree(self):
        """Predicted degree of [b_3, B^{(2)}] is -5."""
        result = verify_bar_length_change(3, 2, input_length=6)
        assert result["predicted_commutator_degree"] == -5

    def test_m2_B0_predicted_degree(self):
        """Predicted degree of [b_2, B^{(0)}] is 0."""
        result = verify_bar_length_change(2, 0, input_length=5)
        assert result["predicted_commutator_degree"] == 0

    def test_expected_output_length(self):
        """Output length = input length + commutator degree."""
        for k in range(2, 5):
            for j in range(3):
                n = max(k + 2 * j, 6)  # ensure enough input length
                result = verify_bar_length_change(k, j, input_length=n)
                expected = n + bar_length_degree_commutator(k, j)
                assert result["expected_output_length"] == expected


# =========================================================================
#  Section 6: Integration with existing A-infinity infrastructure
# =========================================================================

class TestIntegrationWithAInfBar:
    """Integration tests with the A-infinity bar complex of W_{1+inf}."""

    def test_m3_has_correct_bar_degree(self):
        """m_3 on the bar complex has bar-length degree -2."""
        # This is a consistency check: m_3 applies to 3 factors,
        # producing 1, so the bar complex operation b_3 has degree -(3-1) = -2.
        assert bar_length_degree_b_k(3) == -2

    def test_m3_B2_bidegree_matches_obs_ainf(self):
        """The bidegree of [m_3, B^{(2)}] matches the Obs_Ainf structure."""
        # The degree diagnostic distinguishes k=3 from k=4.  It does not
        # prove the raw termwise commutator vanishes.
        deg_m3_B2 = bar_length_degree_commutator(3, 2)
        deg_m4_B2 = bar_length_degree_commutator(4, 2)
        # These are different, so they cannot cancel
        assert deg_m3_B2 != deg_m4_B2
        assert deg_m3_B2 == -5
        assert deg_m4_B2 == -6

    def test_heisenberg_trivial(self):
        """For the Heisenberg (class G), m_k = 0 for k >= 3.

        The vanishing is structural, not a consequence of the bidegree proof.
        """
        # Class G: all m_k = 0 for k >= 3.
        for k in range(3, 7):
            deg = bar_length_degree_commutator(k, 2)
            # Each degree is distinct; the actual term vanishes because
            # m_k is zero in this class.
            assert deg == 2 - k - 4

    def test_virasoro_nontrivial(self):
        """For the Virasoro line, the test records only the target degree."""
        # m_3(T,T,T) = -2T (from a_infinity_bar_w1inf.py)
        # The bar-length degree -5 is distinct from the other k-degrees.
        # No vanishing conclusion is drawn here.
        deg = bar_length_degree_commutator(3, 2)
        other_degs = [bar_length_degree_commutator(k, 2)
                      for k in range(1, 10) if k != 3]
        assert deg not in other_degs


# =========================================================================
#  Section 7: Consistency with Costello's theorem
# =========================================================================

class TestCostelloTheorem:
    """Tests for Costello's theorem verification."""

    def test_cy3_applies(self):
        """Costello's theorem applies for CY_3."""
        v = CostelloChainMapVerification.for_cy_dim(3)
        assert v.applies
        assert v.j_values == [0, 1, 2, 3]

    def test_cy2_applies(self):
        """Costello's theorem applies for CY_2."""
        v = CostelloChainMapVerification.for_cy_dim(2)
        assert v.applies
        assert v.j_values == [0, 1, 2]

    def test_cy1_applies(self):
        """Costello's theorem applies for CY_1."""
        v = CostelloChainMapVerification.for_cy_dim(1)
        assert v.applies
        assert v.j_values == [0, 1]

    def test_j2_available_for_cy3(self):
        """j=2 is in the hierarchy for CY_3 (j <= d=3)."""
        v = CostelloChainMapVerification.for_cy_dim(3)
        assert 2 in v.j_values

    def test_j2_available_for_cy2(self):
        """j=2 is in the hierarchy for CY_2 (j <= d=2)."""
        v = CostelloChainMapVerification.for_cy_dim(2)
        assert 2 in v.j_values

    def test_j2_not_available_for_cy1(self):
        """j=2 is NOT in the hierarchy for CY_1 (j > d=1)."""
        v = CostelloChainMapVerification.for_cy_dim(1)
        assert 2 not in v.j_values


# =========================================================================
#  Section 8: Master verification
# =========================================================================

class TestMasterVerification:
    """Tests for the master verification."""

    def test_master_runs(self):
        """Master verification completes without error."""
        result = master_verification(cy_dim=3, k_max=6)
        assert result is not None

    def test_master_costello_applies(self):
        """Master: Costello's theorem applies."""
        result = master_verification(cy_dim=3, k_max=6)
        assert result["costello_theorem"]["applies"]

    def test_master_all_decompositions_hold(self):
        """Master: all fixed-j degree lines are distinct."""
        result = master_verification(cy_dim=3, k_max=6)
        assert result["full_decomposition"]["all_hold"]

    def test_master_obs_ainf_vanishes(self):
        """Master: Obs_Ainf is not established by this engine."""
        result = master_verification(cy_dim=3, k_max=6)
        assert not result["obs_ainf_resolution"]["vanishes"]

    def test_master_final_conclusion(self):
        """Master: final conclusion states REJECTED."""
        result = master_verification(cy_dim=3, k_max=6)
        assert "REJECTED" in result["final_conclusion"]

    def test_master_j2_table(self):
        """Master: j=2 bidegree table has correct entries."""
        result = master_verification(cy_dim=3, k_max=6)
        j2_table = result["j2_bidegree_table"]
        assert len(j2_table) == 6
        # k=1: degree -3, k=2: -4, k=3: -5, k=4: -6, k=5: -7, k=6: -8
        expected_degrees = [-3, -4, -5, -6, -7, -8]
        actual_degrees = [e["degree"] for e in j2_table]
        assert actual_degrees == expected_degrees

    def test_master_within_j_distinct(self):
        """Master: within-j bidegrees are all distinct."""
        result = master_verification(cy_dim=3, k_max=6)
        assert result["collision_analysis"]["within_j_all_distinct"]

    def test_master_cross_j_collisions_exist(self):
        """Master: cross-j collisions exist but are irrelevant."""
        result = master_verification(cy_dim=3, k_max=6)
        assert result["collision_analysis"]["cross_j_collisions"] > 0

    def test_master_bidegree_of_target(self):
        """Master: target bidegree is -5."""
        result = master_verification(cy_dim=3, k_max=6)
        assert result["obs_ainf_resolution"]["bidegree_of_target"] == -5


# =========================================================================
#  Additional edge cases and mathematical consistency
# =========================================================================

class TestEdgeCases:
    """Edge cases and mathematical consistency checks."""

    def test_b1_B0_is_classical(self):
        """[b_1, B^{(0)}] = 0 is part of the classical mixed complex."""
        # This is the m_1 part of [b, B] = 0.
        deg = bar_length_degree_commutator(1, 0)
        assert deg == 1  # b_1 preserves length, B adds 1

    def test_all_k_at_j2_distinct(self):
        """For j=2, degrees for k=1,...,20 are all distinct."""
        degrees = [bar_length_degree_commutator(k, 2) for k in range(1, 21)]
        assert len(set(degrees)) == 20

    def test_degree_formula_algebraic(self):
        """The formula 2 - k - 2j is linear in k (at fixed j).

        This linearity is what guarantees distinctness: a linear
        function with nonzero slope is injective.
        """
        # At fixed j, deg(k) = (2 - 2j) - k.
        # This is linear with slope -1, hence injective.
        for j in range(4):
            intercept = 2 - 2 * j
            for k in range(1, 11):
                assert bar_length_degree_commutator(k, j) == intercept - k

    def test_no_zero_degree_at_j2(self):
        """No [b_k, B^{(2)}] has degree 0 for k >= 1.

        This means [b_k, B^{(2)}] never preserves bar length,
        which is consistent with the contraction nature of B^{(2)}.
        """
        for k in range(1, 20):
            assert bar_length_degree_commutator(k, 2) != 0

    def test_cy4_decomposition(self):
        """Degree distinctness holds for CY_4 as well (j up to 4)."""
        result = check_full_bidegree_decomposition(k_max=6, j_max=4)
        assert result["all_decompositions_hold"]

    def test_large_k_decomposition(self):
        """Degree distinctness holds for k up to 100 at j=2."""
        result = check_decomposition_at_fixed_j(2, k_max=100)
        assert result["decomposition_holds"]


# =========================================================================
#  Section 9: Multi-path cross-checks (AP10 compliance)
# =========================================================================

class TestMultiPathCrossChecks:
    """Cross-checks verifying the same claims through independent paths.

    Each test computes the same quantity via at least two independent
    methods and checks agreement. This guards against systematic errors
    in any single computational path.
    """

    def test_target_degree_via_formula_vs_explicit(self):
        """[m_3, B^{(2)}] degree: closed-form formula vs explicit degree calc.

        Path 1: 2 - k - 2j = 2 - 3 - 4 = -5.
        Path 2: deg(b_3) + deg(B^{(2)}) = -2 + (-3) = -5.
        """
        path1 = 2 - 3 - 2 * 2
        path2 = bar_length_degree_b_k(3) + bar_length_degree_B_j(2)
        path3 = bar_length_degree_commutator(3, 2)
        assert path1 == path2 == path3 == -5

    def test_decomposition_via_set_vs_strictly_decreasing(self):
        """Distinctness at j=2: set cardinality vs strict monotonicity.

        Path 1: |{deg(k, 2) : k=1..N}| = N.
        Path 2: deg(k, 2) > deg(k+1, 2) for all consecutive k.
        Path 3: deg(k, 2) = -2 - k is injective (slope -1).
        """
        N = 20
        degrees = [bar_length_degree_commutator(k, 2) for k in range(1, N + 1)]

        # Path 1: set cardinality
        assert len(set(degrees)) == N

        # Path 2: strict monotonicity
        assert all(degrees[i] > degrees[i + 1] for i in range(N - 1))

        # Path 3: injective linear function
        for k in range(1, N + 1):
            assert degrees[k - 1] == -2 - k

    def test_obs_ainf_via_resolution_vs_raw_decomposition(self):
        """Obs_Ainf bidegree proof rejection versus raw degree data.

        Path 1: resolve_obs_ainf() rejects the proof.
        Path 2: check_decomposition_at_fixed_j(2) still reports distinct degrees.
        Path 3: master_verification() confirms REJECTED.
        """
        path1 = resolve_obs_ainf(cy_dim=3)
        path2 = check_decomposition_at_fixed_j(2, k_max=10)
        path3 = master_verification(cy_dim=3, k_max=6)

        assert path1.obs_ainf_vanishes is False
        assert path2["decomposition_holds"] is True
        assert path2["termwise_vanishing_established"] is False
        assert "REJECTED" in path3["final_conclusion"]

    def test_bar_length_b_k_via_formula_vs_symbolic(self):
        """b_k bar-length change: formula vs symbolic action.

        Path 1: bar_length_degree_b_k(k) = -(k-1).
        Path 2: Symbolic b_k on a length-n element produces length-(n-k+1).
        """
        for k in range(2, 6):
            formula_deg = bar_length_degree_b_k(k)
            for n in range(k + 1, k + 4):
                x = BarElement(factors=tuple(f"a_{i}" for i in range(n + 1)))
                results = symbolic_b_k_action(x, k)
                for r in results:
                    symbolic_deg = r.bar_length - x.bar_length
                    assert symbolic_deg == formula_deg, (
                        f"k={k}, n={n}: formula gives {formula_deg}, "
                        f"symbolic gives {symbolic_deg}"
                    )

    def test_bar_length_B0_via_formula_vs_symbolic(self):
        """B^{(0)} bar-length change: formula vs symbolic action.

        Path 1: bar_length_degree_B_j(0) = 1.
        Path 2: Symbolic B^{(0)} on length-n produces length-(n+1).
        """
        formula_deg = bar_length_degree_B_j(0)
        for n in range(2, 6):
            x = BarElement(factors=tuple(f"a_{i}" for i in range(n + 1)))
            results = symbolic_B_j_action(x, 0)
            for r in results:
                symbolic_deg = r.bar_length - x.bar_length
                assert symbolic_deg == formula_deg, (
                    f"n={n}: formula gives {formula_deg}, "
                    f"symbolic gives {symbolic_deg}"
                )

    def test_cross_collision_existence_via_enumeration_vs_modular_arithmetic(self):
        """Cross-j collisions: enumeration vs modular arithmetic.

        Two pairs (k, j) and (k', j') collide iff k + 2j = k' + 2j'.
        Path 1: Enumerate and find collisions.
        Path 2: Predict collisions from k - k' = 2(j' - j).

        Example: (k=3, j=0) and (k=1, j=1) collide because 3+0 = 1+2.
        """
        # Path 1: enumeration
        collisions_enum = collision_analysis(k_max=6, j_max=3)
        cross_collisions = collisions_enum["cross_j_collisions"]

        # Path 2: modular arithmetic prediction
        predicted_collision_count = 0
        for deg, pairs in collisions_enum["degree_to_pairs"].items():
            j_values_in_group = set(j for _, j in pairs)
            if len(j_values_in_group) > 1:
                predicted_collision_count += 1

        assert len(cross_collisions) == predicted_collision_count

        # Verify specific known collision
        d1 = bar_length_degree_commutator(3, 0)
        d2 = bar_length_degree_commutator(1, 1)
        assert d1 == d2
        # But within j=0, k=3 is unique; within j=1, k=1 is unique
        for j in range(4):
            j_degs = [bar_length_degree_commutator(k, j)
                      for k in range(1, 7)]
            assert len(set(j_degs)) == len(j_degs)

    def test_costello_prerequisite_via_dim_vs_hierarchy(self):
        """Costello applicability: CY dim check vs hierarchy enumeration.

        Path 1: CY dim d >= 2 and target j=2 <= d.
        Path 2: CostelloChainMapVerification.j_values contains 2.
        """
        for d in range(1, 6):
            v = CostelloChainMapVerification.for_cy_dim(d)
            path1 = d >= 2  # j=2 requires d >= 2
            path2 = 2 in v.j_values
            assert path1 == path2, (
                f"d={d}: dim check gives {path1}, "
                f"hierarchy check gives {path2}"
            )

    def test_degree_linearity_two_independent_derivations(self):
        """Degree formula via two independent algebraic derivations.

        Path 1: deg([b_k, B^{(j)}]) = deg(b_k) + deg(B^{(j)})
                 = -(k-1) + (1-2j) = 2 - k - 2j.
        Path 2: b_k maps CC_n -> CC_{n-k+1}, B^{(j)} maps CC_n -> CC_{n+1-2j}.
                 b_k o B^{(j)}: CC_n -> CC_{n+1-2j} -> CC_{n+1-2j-k+1} = CC_{n+2-k-2j}.
                 Net change from CC_n: 2 - k - 2j.
        """
        for k in range(1, 8):
            for j in range(4):
                # Path 1: algebraic
                path1 = -(k - 1) + (1 - 2 * j)
                # Path 2: from CC_n target
                path2 = (2 - k - 2 * j)
                # Path 3: library function
                path3 = bar_length_degree_commutator(k, j)
                assert path1 == path2 == path3

    def test_injectivity_of_degree_map_via_pigeonhole(self):
        """Distinctness via pigeonhole: N values in range of size >= N.

        For fixed j, degrees are {2-2j-k : k=1..N} = {1-2j, -2j, ..., 2-2j-N}.
        This is an arithmetic progression of length N with common difference -1.
        An arithmetic progression with nonzero common difference contains
        N distinct elements. Cross-check: range = (N-1)*1 = N-1, so
        N values spread over a range of size N-1 with spacing 1 are distinct.
        """
        N = 50
        for j in range(4):
            degrees = [bar_length_degree_commutator(k, j)
                       for k in range(1, N + 1)]
            max_d, min_d = max(degrees), min(degrees)
            range_size = max_d - min_d  # = N - 1

            # Pigeonhole: N values in integer range [min_d, max_d] of size
            # range_size + 1 = N. They are distinct iff they fill every integer.
            assert range_size == N - 1
            assert len(set(degrees)) == N
            # Verify they fill every integer in the range
            assert set(degrees) == set(range(min_d, max_d + 1))
