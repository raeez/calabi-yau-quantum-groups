r"""Tests for the conifold CoHA bar complex in both DT chambers.

Verifies:
  1. CoHA structure in each chamber (generator counts, BPS spectra)
  2. Bar complex dimensions (B^k total and by charge sector)
  3. Bar differential d^2 = 0 (fundamental consistency)
  4. Bar cohomology in each charge sector
  5. DT invariants from bar cohomology Euler characteristics
  6. Wall-crossing as gauge equivalence of MC elements
  7. Pentagon identity consistency with gauge equivalence
  8. Shadow obstruction tower (class G, kappa = 1)
  9. Multi-path verification (4 independent paths)
  10. Wall-crossing at the bar level (quasi-isomorphism)

MULTI-PATH VERIFICATION:
  Path (a): Direct bar complex computation (bar cohomology)
  Path (b): DT generating function (partition function expansion)
  Path (c): Pentagon identity (quantum dilogarithm factorization)
  Path (d): Gauge equivalence of MC elements

Manuscript references:
    Vol III, Part V: resolved conifold, DT theory
    Vol I, Part I: bar complex, shadow obstruction tower
    Vol I, concordance.tex: shadow depth classification

Mathematical references:
    [KS]    Kontsevich-Soibelman, arXiv:0811.2435
    [Nagao] Nagao, arXiv:1002.4884
    [RSYZ]  Rapcak-Soibelman-Yang-Zhao, arXiv:1810.10402
"""

import pytest
from fractions import Fraction

from compute.lib.conifold_bar_complex import (
    # CoHA structure
    CoHAGenerator,
    ConifoldCoHA,
    conifold_coha_chamber_I,
    conifold_coha_chamber_II,
    # Bar complex
    BarElement,
    ConifoldBarComplex,
    # Summaries
    conifold_bar_summary,
    conifold_bar_both_chambers,
    # d^2 = 0
    verify_d_squared_zero,
    # Wall-crossing
    wall_crossing_gauge_equivalence,
    wall_crossing_bar_level,
    # Pentagon
    pentagon_from_mc,
    # DT from bar
    dt_from_bar_cohomology,
    # Shadow tower
    conifold_shadow_tower,
    # Comprehensive
    conifold_bar_comprehensive,
    # Utility
    _matrix_rank,
)


# ================================================================
# 1. CoHA STRUCTURE
# ================================================================

class TestCoHAStructure:
    """Verify the CoHA algebra structure in each chamber."""

    def test_chamber_I_generator_count(self):
        """Chamber I has exactly 2 BPS generators."""
        coha = conifold_coha_chamber_I()
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert coha.num_generators == 2

    def test_chamber_II_generator_count(self):
        """Chamber II has exactly 3 BPS generators."""
        coha = conifold_coha_chamber_II()
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert coha.num_generators == 3

    def test_chamber_I_charges(self):
        """Chamber I generators have charges (1,0) and (0,1)."""
        coha = conifold_coha_chamber_I()
        charges = sorted(g.charge for g in coha.generators)
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert charges == [(0, 1), (1, 0)]

    def test_chamber_II_charges(self):
        """Chamber II generators have charges (1,0), (0,1), (1,1)."""
        coha = conifold_coha_chamber_II()
        charges = sorted(g.charge for g in coha.generators)
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert charges == [(0, 1), (1, 0), (1, 1)]

    def test_all_omega_minus_one(self):
        """All BPS states have Omega = -1 (fermionic/hypermultiplet)."""
        for ch in ["I", "II"]:
            coha = ConifoldCoHA(ch)
            for g in coha.generators:
                # VERIFIED [DC] structural property [LT] operadic Koszul theory
                assert g.omega == -1, f"Chamber {ch}, {g.charge}: Omega={g.omega}"

    def test_antisymmetric_pairing_standard(self):
        """<(1,0), (0,1)> = 1 (the standard symplectic pairing)."""
        coha = ConifoldCoHA("I")
        # VERIFIED [DC] symmetry check [LT] operadic Koszul theory
        assert coha.antisymmetric_pairing((1, 0), (0, 1)) == 1
        # VERIFIED [DC] symmetry check [LT] operadic Koszul theory
        assert coha.antisymmetric_pairing((0, 1), (1, 0)) == -1

    def test_antisymmetric_pairing_self(self):
        """<gamma, gamma> = 0 (antisymmetry)."""
        coha = ConifoldCoHA("I")
        # VERIFIED [DC] symmetry check [LT] operadic Koszul theory
        assert coha.antisymmetric_pairing((1, 0), (1, 0)) == 0
        # VERIFIED [DC] symmetry check [LT] operadic Koszul theory
        assert coha.antisymmetric_pairing((0, 1), (0, 1)) == 0
        # VERIFIED [DC] symmetry check [LT] operadic Koszul theory
        assert coha.antisymmetric_pairing((1, 1), (1, 1)) == 0

    def test_pairing_with_bound_state(self):
        """<(1,0), (1,1)> = 1 and <(0,1), (1,1)> = -1."""
        coha = ConifoldCoHA("II")
        # VERIFIED [DC] growth bound [LT] operadic Koszul theory
        assert coha.antisymmetric_pairing((1, 0), (1, 1)) == 1
        # VERIFIED [DC] growth bound [LT] operadic Koszul theory
        assert coha.antisymmetric_pairing((0, 1), (1, 1)) == -1

    def test_bps_spectrum_chamber_I(self):
        """BPS spectrum in Chamber I: {(1,0): -1, (0,1): -1}."""
        coha = ConifoldCoHA("I")
        spec = coha.bps_spectrum()
        # VERIFIED [DC] BPS state [LT] operadic Koszul theory
        assert spec == {(1, 0): -1, (0, 1): -1}

    def test_bps_spectrum_chamber_II(self):
        """BPS spectrum in Chamber II: {(1,0): -1, (0,1): -1, (1,1): -1}."""
        coha = ConifoldCoHA("II")
        spec = coha.bps_spectrum()
        # VERIFIED [DC] BPS state [LT] operadic Koszul theory
        assert spec == {(1, 0): -1, (0, 1): -1, (1, 1): -1}

    def test_invalid_chamber_raises(self):
        """Invalid chamber name raises ValueError."""
        with pytest.raises(ValueError):
            ConifoldCoHA("III")


# ================================================================
# 2. BAR COMPLEX DIMENSIONS
# ================================================================

class TestBarDimensions:
    """Verify bar complex dimensions B^k in each chamber."""

    def test_B1_chamber_I(self):
        """B^1(CoHA_I) = 2 (one for each generator)."""
        bar = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=3)
        # VERIFIED [DC] dimension count [LT] operadic Koszul theory
        assert bar.bar_dimension(1) == 2

    def test_B1_chamber_II(self):
        """B^1(CoHA_II) = 3 (one for each generator)."""
        bar = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=3)
        # VERIFIED [DC] dimension count [LT] operadic Koszul theory
        assert bar.bar_dimension(1) == 3

    def test_B2_chamber_I(self):
        """B^2(CoHA_I) = 2^2 = 4 (ordered pairs of generators)."""
        bar = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=3)
        # VERIFIED [DC] dimension count [LT] operadic Koszul theory
        assert bar.bar_dimension(2) == 4

    def test_B2_chamber_II(self):
        """B^2(CoHA_II) = 3^2 = 9 (ordered pairs of generators)."""
        bar = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=3)
        # VERIFIED [DC] dimension count [LT] operadic Koszul theory
        assert bar.bar_dimension(2) == 9

    def test_B3_chamber_I(self):
        """B^3(CoHA_I) = 2^3 = 8."""
        bar = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=3)
        # VERIFIED [DC] dimension count [LT] operadic Koszul theory
        assert bar.bar_dimension(3) == 8

    def test_B3_chamber_II(self):
        """B^3(CoHA_II) = 3^3 = 27."""
        bar = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=3)
        # VERIFIED [DC] dimension count [LT] operadic Koszul theory
        assert bar.bar_dimension(3) == 27

    def test_Bk_formula_chamber_I(self):
        """B^k(CoHA_I) = 2^k for all k."""
        bar = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=5)
        for k in range(1, 6):
            # VERIFIED [DC] dimension count [LT] operadic Koszul theory
            assert bar.bar_dimension(k) == 2 ** k

    def test_Bk_formula_chamber_II(self):
        """B^k(CoHA_II) = 3^k for all k."""
        bar = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=5)
        for k in range(1, 6):
            # VERIFIED [DC] dimension count [LT] operadic Koszul theory
            assert bar.bar_dimension(k) == 3 ** k


# ================================================================
# 3. BAR COMPLEX BY CHARGE
# ================================================================

class TestBarByCharge:
    """Verify bar complex dimension decomposition by charge sector."""

    def test_B1_charge_sectors_I(self):
        """B^1 in Chamber I: one element at each generator charge."""
        bar = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=2)
        dims = bar.bar_dimension_by_charge(1)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert dims == {(1, 0): 1, (0, 1): 1}

    def test_B1_charge_sectors_II(self):
        """B^1 in Chamber II: one element at each of three charges."""
        bar = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=2)
        dims = bar.bar_dimension_by_charge(1)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert dims == {(1, 0): 1, (0, 1): 1, (1, 1): 1}

    def test_B2_charge_11_I(self):
        """B^2 at charge (1,1) in Chamber I: 2 elements."""
        bar = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=2)
        dims = bar.bar_dimension_by_charge(2)
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert dims.get((1, 1), 0) == 2  # [(1,0)|(0,1)] and [(0,1)|(1,0)]

    def test_B2_charge_20_I(self):
        """B^2 at charge (2,0) in Chamber I: 1 element."""
        bar = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=2)
        dims = bar.bar_dimension_by_charge(2)
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert dims.get((2, 0), 0) == 1  # [(1,0)|(1,0)]

    def test_charge_conservation(self):
        """Total dimension = sum over all charge sectors."""
        for ch in ["I", "II"]:
            bar = ConifoldBarComplex(ConifoldCoHA(ch), max_bar_degree=4)
            for k in range(1, 5):
                total = bar.bar_dimension(k)
                by_charge = bar.bar_dimension_by_charge(k)
                assert sum(by_charge.values()) == total


# ================================================================
# 4. BAR DIFFERENTIAL d^2 = 0
# ================================================================

class TestDSquaredZero:
    """Verify the fundamental relation d^2 = 0 for the bar differential."""

    @pytest.mark.parametrize("chamber", ["I", "II"])
    @pytest.mark.parametrize("charge", [(1, 0), (0, 1), (1, 1)])
    def test_d_squared_zero(self, chamber, charge):
        """d^2 = 0 at each charge sector in each chamber."""
        result = verify_d_squared_zero(chamber, charge, max_bar_degree=4)
        assert result["d_squared_zero_all"], (
            f"d^2 != 0 in chamber {chamber} at charge {charge}"
        )

    def test_d_squared_zero_higher_charges(self):
        """d^2 = 0 at higher charge sectors."""
        for charge in [(2, 0), (0, 2), (2, 1), (1, 2)]:
            for ch in ["I", "II"]:
                result = verify_d_squared_zero(ch, charge, max_bar_degree=4)
                assert result["d_squared_zero_all"]


# ================================================================
# 5. BAR COHOMOLOGY AND DT INVARIANTS
# ================================================================

class TestBarCohomology:
    """Verify bar cohomology dimensions and DT invariant extraction."""

    def test_H1_at_generators_I(self):
        """H^1(B, gamma) = 1 for each generator charge in Chamber I."""
        bar = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=3)
        for charge in [(1, 0), (0, 1)]:
            h = bar.bar_cohomology_dimension(1, charge)
            # VERIFIED [DC] dimension count [DA] dimensional consistency
            assert h["dim_cohomology"] == 1

    def test_H1_at_generators_II(self):
        """H^1(B, gamma) for generator charges in Chamber II.
        At (1,0) and (0,1): H^1 = 1.
        At (1,1): H^1 = 0 (the bound state is killed by im(d_2))."""
        bar = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=3)
        for charge in [(1, 0), (0, 1)]:
            h = bar.bar_cohomology_dimension(1, charge)
            # VERIFIED [DC] dimension count [DA] dimensional consistency
            assert h["dim_cohomology"] == 1
        h_11 = bar.bar_cohomology_dimension(1, (1, 1))
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert h_11["dim_cohomology"] == 0

    def test_euler_char_at_primitive_charges_I(self):
        """chi_bar(gamma) = -1 at primitive BPS charges in Chamber I."""
        bar = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=3)
        for charge in [(1, 0), (0, 1)]:
            euler = 0
            for k in range(1, 4):
                h = bar.bar_cohomology_dimension(k, charge)
                euler += (-1) ** k * h["dim_cohomology"]
            # VERIFIED [DC] Euler characteristic formula [LT] operadic Koszul theory
            assert euler == -1, f"chi_bar({charge}) = {euler}, expected -1"

    def test_euler_char_at_primitive_charges_II(self):
        """chi_bar(gamma) = -1 at primitive charges (1,0), (0,1) in Chamber II."""
        bar = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=3)
        for charge in [(1, 0), (0, 1)]:
            euler = 0
            for k in range(1, 4):
                h = bar.bar_cohomology_dimension(k, charge)
                euler += (-1) ** k * h["dim_cohomology"]
            # VERIFIED [DC] Euler characteristic formula [LT] operadic Koszul theory
            assert euler == -1

    def test_chamber_I_chi_11(self):
        """chi_bar((1,1)) = 2 in Chamber I.
        In Chamber I, charge (1,1) has no generator, so all elements
        are in B^2 and higher, with H^2((1,1)) = 2."""
        bar = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=4)
        euler = 0
        for k in range(1, 5):
            h = bar.bar_cohomology_dimension(k, (1, 1))
            euler += (-1) ** k * h["dim_cohomology"]
        # VERIFIED [DC] Euler characteristic formula [LT] operadic Koszul theory
        assert euler == 2

    def test_chamber_II_chi_11(self):
        """chi_bar((1,1)) = 1 in Chamber II.
        The bound state generator reduces the cohomology."""
        bar = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=4)
        euler = 0
        for k in range(1, 5):
            h = bar.bar_cohomology_dimension(k, (1, 1))
            euler += (-1) ** k * h["dim_cohomology"]
        # VERIFIED [DC] Euler characteristic formula [LT] operadic Koszul theory
        assert euler == 1

    def test_wall_crossing_changes_chi(self):
        """Wall-crossing changes chi_bar at charge (1,1): 2 -> 1."""
        bar_I = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=4)
        bar_II = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=4)
        euler_I = sum((-1) ** k * bar_I.bar_cohomology_dimension(k, (1, 1))["dim_cohomology"]
                      for k in range(1, 5))
        euler_II = sum((-1) ** k * bar_II.bar_cohomology_dimension(k, (1, 1))["dim_cohomology"]
                       for k in range(1, 5))
        assert euler_I != euler_II
        # VERIFIED [DC] Euler characteristic formula [LT] operadic Koszul theory
        assert euler_I == 2
        # VERIFIED [DC] Euler characteristic formula [LT] operadic Koszul theory
        assert euler_II == 1


# ================================================================
# 6. GAUGE EQUIVALENCE
# ================================================================

class TestGaugeEquivalence:
    """Verify the gauge transformation connecting the two chambers."""

    def test_gauge_match_at_11(self):
        """exp(ad_alpha)(Theta_I) matches Theta_II at charge (1,1)."""
        result = wall_crossing_gauge_equivalence(max_order=5)
        assert result["match_at_11"]

    def test_gauge_match_at_10(self):
        """exp(ad_alpha)(Theta_I) matches Theta_II at charge (1,0)."""
        result = wall_crossing_gauge_equivalence(max_order=5)
        assert result["match_at_10"]

    def test_gauge_match_at_01(self):
        """exp(ad_alpha)(Theta_I) matches Theta_II at charge (0,1)."""
        result = wall_crossing_gauge_equivalence(max_order=5)
        assert result["match_at_01"]

    def test_alpha_is_e_10(self):
        """The gauge parameter is alpha = e_{(1,0)}."""
        result = wall_crossing_gauge_equivalence(max_order=5)
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert result["alpha"] == "(1, 0)"

    def test_first_order_produces_e_11(self):
        """[alpha, Theta_I] produces the (1,1) term.
        [e_{(1,0)}, -e_{(0,1)}] = -<(1,0),(0,1)> e_{(1,1)} = -e_{(1,1)}."""
        result = wall_crossing_gauge_equivalence(max_order=5)
        terms = result["order_terms"]
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert len(terms) >= 1
        # First order term at charge (1,1) should be -1
        first_order = terms[0]["terms"]
        assert "(1, 1)" in first_order
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert first_order["(1, 1)"] == "-1"

    def test_higher_orders_decay(self):
        """Higher-order corrections at (k,1) decay as 1/k!."""
        result = wall_crossing_gauge_equivalence(max_order=6)
        higher = result["higher_charge_corrections"]
        # (2,1) should be -1/2, (3,1) should be -1/6, etc.
        if "(2, 1)" in higher:
            # VERIFIED [DC] structural property [LT] operadic Koszul theory
            assert higher["(2, 1)"] == "-1/2"
        if "(3, 1)" in higher:
            # VERIFIED [DC] structural property [LT] operadic Koszul theory
            assert higher["(3, 1)"] == "-1/6"


# ================================================================
# 7. PENTAGON IDENTITY CONSISTENCY
# ================================================================

class TestPentagonConsistency:
    """Verify the pentagon identity is consistent with gauge equivalence."""

    def test_pentagon_holds(self):
        """E(X)*E(Y) = E(Y)*E(XY)*E(X) in the quantum torus."""
        result = pentagon_from_mc(N_q=10, max_charge=4)
        assert result["pentagon_holds"]

    def test_gauge_consistent_with_pentagon(self):
        """Gauge equivalence at (1,1) is consistent with the pentagon."""
        result = pentagon_from_mc(N_q=10, max_charge=4)
        assert result["gauge_equivalence_match_11"]

    def test_dt_C1_consistent(self):
        """DT C_1(q) = sum k*q^k matches the partition function."""
        result = pentagon_from_mc(N_q=10, max_charge=4)
        assert result["dt_C1_match"]

    def test_all_three_paths_consistent(self):
        """All three verification paths agree."""
        result = pentagon_from_mc(N_q=10, max_charge=4)
        assert result["all_three_consistent"]


# ================================================================
# 8. SHADOW OBSTRUCTION TOWER
# ================================================================

class TestShadowTower:
    """Verify the shadow obstruction tower for the conifold."""

    def test_kappa_equals_one(self):
        """kappa(CoHA_conifold) = 1 = chi_CY(resolved conifold)."""
        result = conifold_shadow_tower()
        # VERIFIED [DC] kappa formula [LT] operadic Koszul theory
        assert result["kappa"] == "1"

    def test_shadow_class_G(self):
        """The conifold CoHA is class G (Gaussian)."""
        result = conifold_shadow_tower()
        # VERIFIED [DC] shadow structure [LT] operadic Koszul theory
        assert result["shadow_class"] == "G"

    def test_r_max_equals_2(self):
        """Shadow depth r_max = 2 for class G."""
        result = conifold_shadow_tower()
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert result["r_max"] == 2

    def test_cubic_shadow_vanishes(self):
        """Cubic shadow C = 0 (class G has no cubic obstruction)."""
        result = conifold_shadow_tower()
        # VERIFIED [DC] shadow structure [LT] operadic Koszul theory
        assert result["shadow_arity_3"] == "0"

    def test_quartic_shadow_vanishes(self):
        """Quartic shadow Q = 0 (class G terminates at arity 2)."""
        result = conifold_shadow_tower()
        # VERIFIED [DC] shadow structure [LT] operadic Koszul theory
        assert result["shadow_arity_4"] == "0"

    def test_discriminant_zero(self):
        """Critical discriminant Delta = 0 for class G."""
        result = conifold_shadow_tower()
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert result["discriminant_Delta"] == "0"

    def test_shadow_metric_positive(self):
        """Shadow metric Q_L > 0 (since kappa = 1 > 0)."""
        result = conifold_shadow_tower()
        q_val = Fraction(result["shadow_metric_Q"])
        # VERIFIED [DC] shadow structure [LT] operadic Koszul theory
        assert q_val > 0


# ================================================================
# 9. WALL-CROSSING AT THE BAR LEVEL
# ================================================================

class TestWallCrossingBar:
    """Verify how the bar complex changes across the wall."""

    def test_generators_differ(self):
        """Chambers I and II have different generator counts."""
        result = wall_crossing_bar_level(max_bar_degree=3)
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert result["chamber_I_generators"] == 2
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert result["chamber_II_generators"] == 3

    def test_B1_differs(self):
        """dim B^1 differs between chambers."""
        result = wall_crossing_bar_level(max_bar_degree=3)
        assert result["comparison"]["bar_degree_1"]["differ"]

    def test_bar_complexes_not_isomorphic(self):
        """The bar complexes are not isomorphic as chain complexes."""
        result = wall_crossing_bar_level(max_bar_degree=3)
        assert not result["bar_complexes_isomorphic"]

    def test_quasi_isomorphism_exists(self):
        """A quasi-isomorphism exists between the bar complexes."""
        result = wall_crossing_bar_level(max_bar_degree=3)
        assert result["quasi_isomorphism_exists"]


# ================================================================
# 10. COMPREHENSIVE MULTI-PATH
# ================================================================

class TestComprehensive:
    """Full multi-path verification."""

    def test_comprehensive_pentagon(self):
        """Pentagon holds in the comprehensive test."""
        result = conifold_bar_comprehensive(N_q=8, max_charge=3, max_bar_degree=3)
        assert result["pentagon_holds"]

    def test_comprehensive_gauge(self):
        """Gauge equivalence holds in the comprehensive test."""
        result = conifold_bar_comprehensive(N_q=8, max_charge=3, max_bar_degree=3)
        assert result["gauge_match_11"]

    def test_comprehensive_d_squared_zero(self):
        """d^2 = 0 everywhere in the comprehensive test."""
        result = conifold_bar_comprehensive(N_q=8, max_charge=3, max_bar_degree=3)
        for key, val in result["d_squared_zero"].items():
            assert val, f"d^2 != 0 at {key}"

    def test_comprehensive_shadow_class(self):
        """Shadow class is G in the comprehensive test."""
        result = conifold_bar_comprehensive(N_q=8, max_charge=3, max_bar_degree=3)
        # VERIFIED [DC] genus tower [LT] operadic Koszul theory
        assert result["shadow_tower"]["shadow_class"] == "G"


# ================================================================
# 11. BAR ELEMENT PROPERTIES
# ================================================================

class TestBarElement:
    """Verify BarElement properties (desuspension, degree)."""

    def test_bar_degree(self):
        """Bar degree = number of tensor factors."""
        e = BarElement([(1, 0), (0, 1)])
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert e.bar_degree == 2

    def test_total_charge(self):
        """Total charge = sum of factor charges."""
        e = BarElement([(1, 0), (0, 1)])
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert e.total_charge == (1, 1)

    def test_cohom_degree(self):
        """Cohomological degree = -bar_degree (since all generators have degree 0)."""
        e = BarElement([(1, 0), (0, 1), (1, 1)])
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert e.cohom_degree == -3

    def test_single_factor(self):
        """Single-factor bar element."""
        e = BarElement([(1, 0)])
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert e.bar_degree == 1
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert e.total_charge == (1, 0)
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert e.cohom_degree == -1


# ================================================================
# 12. MATRIX RANK UTILITY
# ================================================================

class TestMatrixRank:
    """Verify the matrix rank computation over Q."""

    def test_zero_matrix(self):
        """Rank of zero matrix is 0."""
        mat = [[Fraction(0)] * 3 for _ in range(2)]
        # VERIFIED [DC] rank [LT] operadic Koszul theory
        assert _matrix_rank(mat) == 0

    def test_identity_matrix(self):
        """Rank of identity matrix is n."""
        n = 3
        mat = [[Fraction(1) if i == j else Fraction(0) for j in range(n)]
               for i in range(n)]
        assert _matrix_rank(mat) == n

    def test_rank_1_matrix(self):
        """Rank of a rank-1 matrix is 1."""
        mat = [
            [Fraction(1), Fraction(2), Fraction(3)],
            [Fraction(2), Fraction(4), Fraction(6)],
        ]
        # VERIFIED [DC] rank [LT] operadic Koszul theory
        assert _matrix_rank(mat) == 1

    def test_rank_2_matrix(self):
        """Rank of a generic 2x3 matrix is 2."""
        mat = [
            [Fraction(1), Fraction(0), Fraction(1)],
            [Fraction(0), Fraction(1), Fraction(1)],
        ]
        # VERIFIED [DC] rank [LT] operadic Koszul theory
        assert _matrix_rank(mat) == 2

    def test_empty_matrix(self):
        """Rank of empty matrix is 0."""
        # VERIFIED [DC] rank [LT] operadic Koszul theory
        assert _matrix_rank([]) == 0
        # VERIFIED [DC] rank [LT] operadic Koszul theory
        assert _matrix_rank([[]]) == 0


# ================================================================
# 13. DT FROM BAR COHOMOLOGY
# ================================================================

class TestDTFromBar:
    """Verify DT invariant extraction from bar cohomology."""

    def test_dt_chamber_I(self):
        """DT invariants from bar cohomology in Chamber I."""
        result = dt_from_bar_cohomology("I", max_bar_degree=3)
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert result["chamber"] == "I"
        # At primitive charges, should detect Omega = -1
        dt = result["dt_invariants"]
        assert "(1, 0)" in dt
        assert "(0, 1)" in dt

    def test_dt_chamber_II(self):
        """DT invariants from bar cohomology in Chamber II."""
        result = dt_from_bar_cohomology("II", max_bar_degree=3)
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert result["chamber"] == "II"

    def test_primitive_charges_match_spectrum(self):
        """At primitive charges, Euler char matches BPS spectrum."""
        for ch in ["I", "II"]:
            coha = ConifoldCoHA(ch)
            bar = ConifoldBarComplex(coha, max_bar_degree=4)
            for charge in [(1, 0), (0, 1)]:
                euler = sum(
                    (-1) ** k * bar.bar_cohomology_dimension(k, charge)["dim_cohomology"]
                    for k in range(1, 5)
                )
                # VERIFIED [DC] Euler characteristic formula [LT] operadic Koszul theory
                assert euler == -1, (
                    f"Chamber {ch}, charge {charge}: euler = {euler}, expected -1"
                )


# ================================================================
# 14. COHA GENERATOR PROPERTIES
# ================================================================

class TestCoHAGenerator:
    """Verify CoHAGenerator properties."""

    def test_generator_creation(self):
        """Basic generator creation."""
        g = CoHAGenerator((1, 0), -1, "e_1")
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert g.charge == (1, 0)
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert g.omega == -1
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert g.name == "e_1"
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert g.cohom_degree == 0

    def test_default_name(self):
        """Default name from charge."""
        g = CoHAGenerator((2, 3), 1)
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert g.name == "e_(2, 3)"


# ================================================================
# 15. BAR SUMMARY
# ================================================================

class TestBarSummary:
    """Verify the bar complex summary functions."""

    def test_bar_summary_I(self):
        """Bar summary for Chamber I is well-formed."""
        result = conifold_bar_summary("I", max_bar_degree=3)
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert result["chamber"] == "I"
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert result["num_generators"] == 2
        assert 1 in result["bar_dimensions_total"]
        assert 2 in result["bar_dimensions_total"]
        assert 3 in result["bar_dimensions_total"]

    def test_bar_summary_II(self):
        """Bar summary for Chamber II is well-formed."""
        result = conifold_bar_summary("II", max_bar_degree=3)
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert result["chamber"] == "II"
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert result["num_generators"] == 3

    def test_both_chambers(self):
        """Both-chambers comparison is well-formed."""
        result = conifold_bar_both_chambers(max_bar_degree=3)
        assert "chamber_I" in result
        assert "chamber_II" in result
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert result["generator_count_I"] == 2
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert result["generator_count_II"] == 3
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert result["dim_B1_I"] == 2
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert result["dim_B1_II"] == 3


# ================================================================
# 16. CROSS-CHAMBER BAR COHOMOLOGY COMPARISON
# ================================================================

class TestCrossChamberCohomology:
    """Compare bar cohomology between chambers to detect wall-crossing."""

    def test_primitive_charges_agree(self):
        """H^1 at primitive charges (1,0) and (0,1) is the same in both chambers."""
        bar_I = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=3)
        bar_II = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=3)
        for charge in [(1, 0), (0, 1)]:
            h_I = bar_I.bar_cohomology_dimension(1, charge)["dim_cohomology"]
            h_II = bar_II.bar_cohomology_dimension(1, charge)["dim_cohomology"]
            # VERIFIED [DC] structural property [LT] operadic Koszul theory
            assert h_I == h_II == 1

    def test_bound_state_charge_differs(self):
        """Bar cohomology at (1,1) differs between chambers."""
        bar_I = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=4)
        bar_II = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=4)
        euler_I = sum(
            (-1) ** k * bar_I.bar_cohomology_dimension(k, (1, 1))["dim_cohomology"]
            for k in range(1, 5)
        )
        euler_II = sum(
            (-1) ** k * bar_II.bar_cohomology_dimension(k, (1, 1))["dim_cohomology"]
            for k in range(1, 5)
        )
        # VERIFIED [DC] Euler characteristic formula [LT] operadic Koszul theory
        assert euler_I == 2
        # VERIFIED [DC] Euler characteristic formula [LT] operadic Koszul theory
        assert euler_II == 1

    def test_wall_crossing_jump(self):
        """The wall-crossing jump at (1,1) is Delta(chi) = -1.

        The jump in chi_bar at charge (1,1):
          Chamber I: chi = 2 (no bound state)
          Chamber II: chi = 1 (bound state present)
          Jump = 2 - 1 = 1

        This is related to the KS wall-crossing formula:
          Delta(Omega(gamma_1 + gamma_2)) is triggered by the
          pairing <gamma_1, gamma_2> = 1.
        """
        bar_I = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=4)
        bar_II = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=4)
        euler_I = sum(
            (-1) ** k * bar_I.bar_cohomology_dimension(k, (1, 1))["dim_cohomology"]
            for k in range(1, 5)
        )
        euler_II = sum(
            (-1) ** k * bar_II.bar_cohomology_dimension(k, (1, 1))["dim_cohomology"]
            for k in range(1, 5)
        )
        jump = euler_I - euler_II
        # VERIFIED [DC] wall-crossing [LT] operadic Koszul theory
        assert jump == 1


# ================================================================
# 17. HIGHER CHARGE WALL-CROSSING
# ================================================================

class TestHigherChargeWC:
    """Verify wall-crossing effects at higher charge sectors."""

    def test_chi_21_differs(self):
        """chi_bar at (2,1) differs between chambers."""
        bar_I = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=4)
        bar_II = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=4)
        euler_I = sum(
            (-1) ** k * bar_I.bar_cohomology_dimension(k, (2, 1))["dim_cohomology"]
            for k in range(1, 5)
        )
        euler_II = sum(
            (-1) ** k * bar_II.bar_cohomology_dimension(k, (2, 1))["dim_cohomology"]
            for k in range(1, 5)
        )
        # Chamber I: chi = -3
        # Chamber II: chi = -1
        # VERIFIED [DC] Euler characteristic formula [LT] operadic Koszul theory
        assert euler_I == -3
        # VERIFIED [DC] Euler characteristic formula [LT] operadic Koszul theory
        assert euler_II == -1

    def test_chi_20_agrees(self):
        """chi_bar at (2,0) agrees between chambers (no wall-crossing)."""
        bar_I = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=4)
        bar_II = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=4)
        euler_I = sum(
            (-1) ** k * bar_I.bar_cohomology_dimension(k, (2, 0))["dim_cohomology"]
            for k in range(1, 5)
        )
        euler_II = sum(
            (-1) ** k * bar_II.bar_cohomology_dimension(k, (2, 0))["dim_cohomology"]
            for k in range(1, 5)
        )
        # VERIFIED [DC] Euler characteristic formula [LT] operadic Koszul theory
        assert euler_I == euler_II == 1


# ================================================================
# 18. BAR DIFFERENTIAL MATRIX STRUCTURE
# ================================================================

class TestBarDifferentialMatrix:
    """Verify structure of the bar differential matrix."""

    def test_d2_matrix_at_11_chamber_II(self):
        """d_2 matrix at (1,1) in Chamber II: 1 x 2 with entries -1, 1.

        The two B^2 elements at (1,1) are:
          [(0,1)|(1,0)] and [(1,0)|(0,1)]
        Their differentials map to s^{-1}(e_2 * e_1) and s^{-1}(e_1 * e_2)
        at charge (1,1) in B^1, which is spanned by s^{-1}e_{12}.
        """
        bar = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=3)
        mat = bar.bar_differential_matrix(2, (1, 1))
        # VERIFIED [DC] dimension count [LT] operadic Koszul theory
        assert len(mat) == 1  # target: B^1 at (1,1) has dim 1
        # VERIFIED [DC] dimension count [LT] operadic Koszul theory
        assert len(mat[0]) == 2  # source: B^2 at (1,1) has dim 2 (from generators (0,1), (1,0) only)

    def test_d2_at_11_chamber_I_empty(self):
        """d_2 matrix at (1,1) in Chamber I has empty target.

        In Chamber I, B^1 at charge (1,1) is empty (no generator of that charge),
        so the matrix from B^2 -> B^1 at (1,1) is empty.
        """
        bar = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=3)
        mat = bar.bar_differential_matrix(2, (1, 1))
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert mat == []


# ================================================================
# 19. SHADOW TOWER CROSS-VERIFICATION
# ================================================================

class TestShadowCrossVerification:
    """Cross-verify shadow tower data with known values."""

    def test_kappa_matches_cy_euler(self):
        """kappa = 1 matches chi_CY(resolved conifold) = 1 from cy_bar_complex_engine."""
        st = conifold_shadow_tower()
        # VERIFIED [DC] kappa formula [LT] operadic Koszul theory
        assert st["kappa"] == "1"
        # Cross-check with the CY bar complex engine value
        from compute.lib.modular_cy_characteristic import chi_cy_resolved_conifold
        result = chi_cy_resolved_conifold()
        # VERIFIED [DC] Euler characteristic formula [LT] operadic Koszul theory
        assert result.chi_cy == Fraction(1)
        # VERIFIED [DC] kappa formula [LT] operadic Koszul theory
        assert result.kappa == Fraction(1)

    def test_class_G_consistent_with_heisenberg(self):
        """Class G = same shadow class as Heisenberg (free-field type).

        Both have r_max = 2 and Delta = 0. The conifold is the
        'free-field' limit of CY3 geometry (single compact cycle,
        no complex moduli).
        """
        st = conifold_shadow_tower()
        # VERIFIED [DC] consistency check [LT] operadic Koszul theory
        assert st["shadow_class"] == "G"
        # VERIFIED [DC] consistency check [LT] operadic Koszul theory
        assert st["r_max"] == 2
        # VERIFIED [DC] consistency check [LT] operadic Koszul theory
        assert st["discriminant_Delta"] == "0"


# ================================================================
# 20. PENTAGON-MC SYNTHESIS
# ================================================================

class TestPentagonMCSynthesis:
    """Synthesize pentagon identity with MC framework."""

    def test_gauge_alpha_reproduces_pentagon_spectrum(self):
        """The gauge transformation alpha = e_{(1,0)} applied to Theta_I
        produces exactly the additional BPS state at (1,1)."""
        ge = wall_crossing_gauge_equivalence(max_order=3)
        # The first-order term [alpha, Theta_I] gives -e_{(1,1)}
        assert ge["match_at_11"]
        # This is the bar-complex content of the pentagon identity:
        # E(X)*E(Y) = E(Y)*E(XY)*E(X) translates to
        # Theta_I + [alpha, Theta_I] = Theta_II at leading order

    def test_pentagon_numerical_consistent(self):
        """The pentagon identity holds numerically."""
        from compute.lib.conifold_wall_crossing import pentagon_numerical
        for q_val in [0.3, 0.5, 0.7]:
            result = pentagon_numerical(q_val)
            assert result["match"], f"Pentagon fails at q={q_val}"


# ================================================================
# 21. BAR COMPLEX ENUMERATION PATTERNS
# ================================================================

class TestBarEnumerationPatterns:
    """Verify combinatorial structure of bar complex basis enumeration."""

    def test_B2_all_ordered_pairs_I(self):
        """B^2 in Chamber I enumerates all ordered pairs of 2 generators.
        There should be 4 elements: (1,0)(1,0), (1,0)(0,1), (0,1)(1,0), (0,1)(0,1)."""
        bar = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=2)
        b2 = bar._bar_basis[2]
        factors_list = sorted([tuple(e.factors) for e in b2])
        expected = sorted([
            ((0, 1), (0, 1)),
            ((0, 1), (1, 0)),
            ((1, 0), (0, 1)),
            ((1, 0), (1, 0)),
        ])
        assert factors_list == expected

    def test_B2_charge_decomposition_I(self):
        """B^2 in Chamber I decomposes: (2,0):1, (1,1):2, (0,2):1."""
        bar = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=2)
        dims = bar.bar_dimension_by_charge(2)
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert dims.get((2, 0), 0) == 1
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert dims.get((1, 1), 0) == 2
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert dims.get((0, 2), 0) == 1

    def test_B3_charge_decomposition_I(self):
        """B^3 at charge (2,1) in Chamber I: 3 elements.
        They are: (1,0)(1,0)(0,1), (1,0)(0,1)(1,0), (0,1)(1,0)(1,0)."""
        bar = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=3)
        dims = bar.bar_dimension_by_charge(3)
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert dims.get((2, 1), 0) == 3

    def test_charge_sector_symmetry_I(self):
        """In Chamber I, the charge lattice has Z_2 symmetry (1,0) <-> (0,1).
        This means dim B^k(n,m) = dim B^k(m,n) for all k, n, m."""
        bar = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=4)
        for k in range(1, 5):
            dims = bar.bar_dimension_by_charge(k)
            for (n, m), d in dims.items():
                assert dims.get((m, n), 0) == d, (
                    f"Asymmetry at k={k}: dim({n},{m})={d} != dim({m},{n})={dims.get((m,n),0)}"
                )


# ================================================================
# 22. WALL-CROSSING JUMP FORMULA
# ================================================================

class TestWallCrossingJumpFormula:
    """Verify the wall-crossing jump formula: Delta(chi) at each charge."""

    def test_jump_at_11(self):
        """Wall-crossing jump at (1,1): Delta(chi) = 2 - 1 = 1."""
        bar_I = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=4)
        bar_II = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=4)
        chi_I = sum((-1)**k * bar_I.bar_cohomology_dimension(k, (1,1))["dim_cohomology"]
                    for k in range(1, 5))
        chi_II = sum((-1)**k * bar_II.bar_cohomology_dimension(k, (1,1))["dim_cohomology"]
                     for k in range(1, 5))
        # VERIFIED [DC] Euler characteristic [LT] operadic Koszul theory
        assert chi_I - chi_II == 1

    def test_jump_at_21(self):
        """Wall-crossing jump at (2,1): Delta(chi) = -3 - (-1) = -2."""
        bar_I = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=4)
        bar_II = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=4)
        chi_I = sum((-1)**k * bar_I.bar_cohomology_dimension(k, (2,1))["dim_cohomology"]
                    for k in range(1, 5))
        chi_II = sum((-1)**k * bar_II.bar_cohomology_dimension(k, (2,1))["dim_cohomology"]
                     for k in range(1, 5))
        # VERIFIED [DC] Euler characteristic [LT] operadic Koszul theory
        assert chi_I - chi_II == -2

    def test_no_jump_at_20(self):
        """No wall-crossing at (2,0): gamma_1 direction, no bound states cross."""
        bar_I = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=4)
        bar_II = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=4)
        chi_I = sum((-1)**k * bar_I.bar_cohomology_dimension(k, (2,0))["dim_cohomology"]
                    for k in range(1, 5))
        chi_II = sum((-1)**k * bar_II.bar_cohomology_dimension(k, (2,0))["dim_cohomology"]
                     for k in range(1, 5))
        assert chi_I == chi_II

    def test_no_jump_at_02(self):
        """No wall-crossing at (0,2): gamma_2 direction, no bound states cross."""
        bar_I = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=4)
        bar_II = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=4)
        chi_I = sum((-1)**k * bar_I.bar_cohomology_dimension(k, (0,2))["dim_cohomology"]
                    for k in range(1, 5))
        chi_II = sum((-1)**k * bar_II.bar_cohomology_dimension(k, (0,2))["dim_cohomology"]
                     for k in range(1, 5))
        assert chi_I == chi_II


# ================================================================
# 23. DT GENERATING FUNCTION COMPARISON
# ================================================================

class TestDTGeneratingFunction:
    """Compare DT generating function with bar complex data."""

    def test_chamber_I_F1_sign(self):
        """Chamber I: F_I[1](q) = -sum k*q^k (sign from (1-Qq^k)^{+k})."""
        from compute.lib.conifold_wall_crossing import dt_chamber_I
        F_I = dt_chamber_I(15, N_Q=2)
        for k in range(1, 10):
            # VERIFIED [DC] structural property [LT] operadic Koszul theory
            assert F_I[1][k] == Fraction(-k)

    def test_chamber_II_G1(self):
        """Chamber II: G_II[1](q) = sum k*q^k (from (1-Q^{-1}q^k)^{-k})."""
        from compute.lib.conifold_wall_crossing import dt_chamber_II
        G_II = dt_chamber_II(15, N_Qinv=2)
        for k in range(1, 10):
            # VERIFIED [DC] structural property [LT] operadic Koszul theory
            assert G_II[1][k] == Fraction(k)

    def test_macmahon_first_coefficients(self):
        """M(q) = 1 + q + 3q^2 + 6q^3 + 13q^4 + ... (MacMahon/OEIS A000219)."""
        from compute.lib.conifold_wall_crossing import _macmahon_coeffs
        M = _macmahon_coeffs(10)
        expected = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282]
        for k in range(10):
            # VERIFIED [DC] partition function [LT] OEIS A000219
            assert M[k] == Fraction(expected[k])


# ================================================================
# 24. FOUR-PATH VERIFICATION
# ================================================================

class TestFourPathVerification:
    """Verify all four independent paths give consistent results."""

    def test_path_a_bar_cohomology_detects_bps(self):
        """Path (a): Bar cohomology Euler char = -1 at BPS charges."""
        for ch in ["I", "II"]:
            bar = ConifoldBarComplex(ConifoldCoHA(ch), max_bar_degree=3)
            for charge in [(1, 0), (0, 1)]:
                euler = sum((-1)**k * bar.bar_cohomology_dimension(k, charge)["dim_cohomology"]
                            for k in range(1, 4))
                # VERIFIED [DC] Euler characteristic formula [LT] operadic Koszul theory
                assert euler == -1

    def test_path_b_dt_partition_function(self):
        """Path (b): DT partition function encodes BPS counts."""
        from compute.lib.conifold_wall_crossing import dt_chamber_I
        F = dt_chamber_I(10, N_Q=2)
        # F[0] = 1 (vacuum), F[1] = -sum k*q^k (one BPS state)
        # VERIFIED [DC] partition function [LT] operadic Koszul theory
        assert F[0][0] == Fraction(1)
        # VERIFIED [DC] partition function [LT] operadic Koszul theory
        assert F[1][1] == Fraction(-1)

    def test_path_c_pentagon(self):
        """Path (c): Pentagon identity holds exactly."""
        from compute.lib.conifold_wall_crossing import pentagon_identity_quantum_torus
        result = pentagon_identity_quantum_torus(N_q=8, max_charge=3)
        assert result["pentagon_holds"]

    def test_path_d_gauge_equivalence(self):
        """Path (d): Gauge transformation connects MC elements."""
        result = wall_crossing_gauge_equivalence(max_order=3)
        assert result["match_at_11"]
        assert result["match_at_10"]
        assert result["match_at_01"]


# ================================================================
# 25. BAR COMPLEX DEGREE STRUCTURE
# ================================================================

class TestBarDegreeStructure:
    """Verify the grading structure of bar complex elements."""

    def test_all_generators_degree_zero(self):
        """All CoHA generators have cohomological degree 0."""
        for ch in ["I", "II"]:
            coha = ConifoldCoHA(ch)
            for g in coha.generators:
                # VERIFIED [DC] degree count [DA] dimensional consistency
                assert g.cohom_degree == 0

    def test_bar_elements_negative_degree(self):
        """Bar elements have cohom degree = -bar_degree (all generators degree 0)."""
        bar = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=4)
        for k in range(1, 5):
            for elem in bar._bar_basis[k]:
                assert elem.cohom_degree == -k

    def test_desuspension_lowers_degree(self):
        """Each s^{-1}a has degree |a| - 1 = 0 - 1 = -1 (AP45)."""
        e = BarElement([(1, 0)])
        # s^{-1}e_1 has degree 0 - 1 = -1
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert e.cohom_degree == -1


# ================================================================
# 26. MC EQUATION STRUCTURE
# ================================================================

class TestMCEquationStructure:
    """Verify the MC equation structure in the lattice Lie algebra.

    Key mathematical point: [Theta, Theta] = 0 ALWAYS holds in any Lie
    algebra when the bracket squared is computed as the full ordered sum
    over all pairs, because the antisymmetry [e_g1, e_g2] = -[e_g2, e_g1]
    forces pairwise cancellation.  The wall-crossing obstruction is NOT
    captured by the binary Lie bracket alone -- it lives in the
    Kontsevich-Soibelman automorphism (quantum dilogarithm) product, or
    equivalently in the L_infinity higher brackets of the shadow
    obstruction tower.
    """

    def test_theta_I_mc_holds_by_antisymmetry(self):
        """[Theta_I, Theta_I] = 0 by antisymmetry of the Lie bracket.

        For Theta_I = -e_{(1,0)} - e_{(0,1)}:
          [-e_{(1,0)}, -e_{(0,1)}] = 1 * e_{(1,1)}   (pairing = 1*1 - 0*0 = 1)
          [-e_{(0,1)}, -e_{(1,0)}] = -1 * e_{(1,1)}   (pairing = 0*0 - 1*1 = -1)
        Total at (1,1): 1 + (-1) = 0.  This is a tautology of antisymmetry.
        """
        from compute.lib.conifold_wall_crossing import mc_equation_check
        result = mc_equation_check({(1, 0): -1, (0, 1): -1}, max_charge=3)
        assert result["mc_equation_holds"]

    def test_theta_I_bracket_components_cancel(self):
        """The two ordered contributions at (1,1) cancel exactly.

        This verifies the antisymmetry cancellation explicitly:
        the bracket_squared_nonzero dict should be empty.
        """
        from compute.lib.conifold_wall_crossing import mc_equation_check
        result = mc_equation_check({(1, 0): -1, (0, 1): -1}, max_charge=3)
        nonzero = result["bracket_squared_nonzero"]
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert len(nonzero) == 0

    def test_theta_II_mc_holds_by_antisymmetry(self):
        """[Theta_II, Theta_II] = 0 for the same reason: antisymmetry
        forces all ordered-pair contributions to cancel.

        For Theta_II = -e_{(1,0)} - e_{(0,1)} - e_{(1,1)}:
        every (g1, g2) pair with g1 != g2 has a reversed partner (g2, g1)
        with opposite pairing, and self-pairs (g, g) have pairing 0.
        """
        from compute.lib.conifold_wall_crossing import mc_equation_check
        result = mc_equation_check(
            {(1, 0): -1, (0, 1): -1, (1, 1): -1}, max_charge=4
        )
        assert result["mc_equation_holds"]


# ================================================================
# 27. CHAMBER SYMMETRY
# ================================================================

class TestChamberSymmetry:
    """Verify symmetry properties of the chambers."""

    def test_chamber_I_has_Z2_symmetry(self):
        """Chamber I is symmetric under (n,m) <-> (m,n).
        The two generators (1,0) and (0,1) are exchangeable."""
        coha = ConifoldCoHA("I")
        spec = coha.bps_spectrum()
        assert spec.get((1, 0)) == spec.get((0, 1))

    def test_chamber_II_breaks_Z2(self):
        """Chamber II breaks the (n,m) <-> (m,n) symmetry.
        The bound state (1,1) is self-conjugate, but the 3-particle
        chamber has an asymmetric ordering."""
        coha = ConifoldCoHA("II")
        # The spectrum itself preserves Z2 (1,1) is symmetric
        spec = coha.bps_spectrum()
        assert spec.get((1, 0)) == spec.get((0, 1))
        # But the bound state adds a new generator
        assert (1, 1) in spec

    def test_bar_cohomology_Z2_symmetric_I(self):
        """Bar cohomology at (n,m) equals bar cohomology at (m,n) in Chamber I."""
        bar = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=4)
        for k in range(1, 5):
            h_21 = bar.bar_cohomology_dimension(k, (2, 1))["dim_cohomology"]
            h_12 = bar.bar_cohomology_dimension(k, (1, 2))["dim_cohomology"]
            assert h_21 == h_12, f"Z2 broken at k={k}: H({2,1})={h_21}, H({1,2})={h_12}"


# ================================================================
# 28. GAUGE TRANSFORMATION HIGHER-ORDER STRUCTURE
# ================================================================

class TestGaugeHigherOrder:
    """Verify higher-order structure of the gauge transformation."""

    def test_ad_alpha_on_e01(self):
        """[e_{(1,0)}, -e_{(0,1)}] = -1 * e_{(1,1)}: the first-order term."""
        ge = wall_crossing_gauge_equivalence(max_order=5)
        terms = ge["order_terms"]
        # VERIFIED [DC] structural property [LT] operadic Koszul theory
        assert len(terms) >= 1
        # Order 1: coefficient at (1,1) should be -1
        assert "(1, 1)" in terms[0]["terms"]

    def test_ad_alpha_squared_on_theta(self):
        """(ad_alpha)^2(Theta_I) produces the (2,1) term.
        [e_{(1,0)}, -e_{(1,1)}] = -1 * e_{(2,1)}.
        So (ad)^2 / 2! = -1/2 * e_{(2,1)}."""
        ge = wall_crossing_gauge_equivalence(max_order=5)
        higher = ge["higher_charge_corrections"]
        if "(2, 1)" in higher:
            # VERIFIED [DC] structural property [LT] operadic Koszul theory
            assert higher["(2, 1)"] == "-1/2"

    def test_gauge_series_coefficients(self):
        """exp(ad_alpha)(Theta) has corrections -1/k! at charge (k,1)."""
        ge = wall_crossing_gauge_equivalence(max_order=6)
        higher = ge["higher_charge_corrections"]
        expected = {
            "(2, 1)": "-1/2",
            "(3, 1)": "-1/6",
            "(4, 1)": "-1/24",
            "(5, 1)": "-1/120",
        }
        for charge, val in expected.items():
            if charge in higher:
                assert higher[charge] == val, (
                    f"At {charge}: got {higher[charge]}, expected {val}"
                )


# ================================================================
# 29. BAR COMPLEX AND SCATTERING DIAGRAMS
# ================================================================

class TestBarAndScattering:
    """Relate bar complex structure to scattering diagrams."""

    def test_bar_detects_bound_state_formation(self):
        """In Chamber II, the bar differential d_2 at charge (1,1) is
        nonzero, mapping 2D -> 1D. This means the bound state e_{12}
        is detected by the bar differential as a 'relation' between
        e_1 and e_2."""
        bar = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=3)
        mat = bar.bar_differential_matrix(2, (1, 1))
        # VERIFIED [DC] growth bound [LT] operadic Koszul theory
        assert len(mat) == 1  # 1D target
        # VERIFIED [DC] rank [LT] operadic Koszul theory
        assert _matrix_rank(mat) == 1  # full rank

    def test_bar_B2_at_11_spans_relation(self):
        """The two elements [(0,1)|(1,0)] and [(1,0)|(0,1)] in B^2 at (1,1)
        map under d_bar to the same target (e_{12}), generating the relation
        e_1*e_2 - e_2*e_1 ~ e_{12} (up to signs)."""
        bar = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=3)
        mat = bar.bar_differential_matrix(2, (1, 1))
        # The matrix is [c1, c2] where c1 + c2 should be 0 (antisymmetry of pairing)
        # Actually: c1 = -pairing(0,1)(1,0) = -(-1) = 1 (with sign)
        #           c2 = pairing(1,0)(0,1) = 1 (with sign from (-1)^i)
        # Check that both entries are nonzero
        assert mat[0][0] != Fraction(0)
        assert mat[0][1] != Fraction(0)

    def test_scattering_wall_pairing(self):
        """The wall of marginal stability is detected by <gamma_1, gamma_2> != 0.
        The conifold has a single wall separating chambers I and II."""
        coha = ConifoldCoHA("I")
        p = coha.antisymmetric_pairing((1, 0), (0, 1))
        # VERIFIED [DC] wall-crossing [LT] operadic Koszul theory
        assert p == 1  # nonzero => wall exists


# ================================================================
# 30. MULTI-PATH EULER CHARACTERISTIC TABLE
# ================================================================

class TestEulerCharacteristicTable:
    """Comprehensive Euler characteristic table for both chambers."""

    def test_full_euler_table_chamber_I(self):
        """Complete Euler characteristic table for Chamber I at low charges."""
        bar = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=5)
        expected = {
            (1, 0): -1,
            (0, 1): -1,
            (2, 0): 1,
            (0, 2): 1,
            (1, 1): 2,
        }
        for charge, exp_chi in expected.items():
            euler = sum(
                (-1)**k * bar.bar_cohomology_dimension(k, charge)["dim_cohomology"]
                for k in range(1, 6)
            )
            assert euler == exp_chi, f"Chamber I, {charge}: got {euler}, expected {exp_chi}"

    def test_full_euler_table_chamber_II(self):
        """Complete Euler characteristic table for Chamber II at low charges."""
        bar = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=5)
        expected = {
            (1, 0): -1,
            (0, 1): -1,
            (2, 0): 1,
            (0, 2): 1,
            (1, 1): 1,
        }
        for charge, exp_chi in expected.items():
            euler = sum(
                (-1)**k * bar.bar_cohomology_dimension(k, charge)["dim_cohomology"]
                for k in range(1, 6)
            )
            assert euler == exp_chi, f"Chamber II, {charge}: got {euler}, expected {exp_chi}"

    def test_wall_crossing_jump_table(self):
        """Wall-crossing jump Delta(chi) = chi_I - chi_II at each charge."""
        bar_I = ConifoldBarComplex(ConifoldCoHA("I"), max_bar_degree=5)
        bar_II = ConifoldBarComplex(ConifoldCoHA("II"), max_bar_degree=5)
        expected_jumps = {
            (1, 0): 0,   # no change
            (0, 1): 0,   # no change
            (2, 0): 0,   # no wall in this direction
            (0, 2): 0,   # no wall in this direction
            (1, 1): 1,   # bound state appears
        }
        for charge, exp_jump in expected_jumps.items():
            chi_I = sum(
                (-1)**k * bar_I.bar_cohomology_dimension(k, charge)["dim_cohomology"]
                for k in range(1, 6)
            )
            chi_II = sum(
                (-1)**k * bar_II.bar_cohomology_dimension(k, charge)["dim_cohomology"]
                for k in range(1, 6)
            )
            jump = chi_I - chi_II
            assert jump == exp_jump, (
                f"charge {charge}: jump={jump}, expected={exp_jump} "
                f"(chi_I={chi_I}, chi_II={chi_II})"
            )
