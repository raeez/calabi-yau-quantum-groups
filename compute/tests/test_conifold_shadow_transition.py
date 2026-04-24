r"""Tests for the conifold shadow transition engine.

Verifies:
    1. Hodge number arithmetic across the conifold transition
    2. Euler characteristic change: delta_chi = 4 per node
    3. BCOV-shadow candidate chi/24 in both phases
    4. Shadow tower class preservation (M -> M)
    5. GV-to-shadow dictionary (seed mechanism n^0_1 = 1)
    6. Log period corrections (alternating sign)
    7. Shadow metric and discriminant
    8. Multi-node transitions
    9. Conifold period expansion
    10. Monodromy data (rank-1 nilpotent)
    11. Comprehensive analysis consistency

Ground truth:
    Quintic: h^{1,1}=1, h^{2,1}=101, chi=-200, shadow scalar=-25/3.
    Resolved (1 node): h^{1,1}=2, h^{2,1}=100, chi=-196, shadow scalar=-49/6.
    Delta_chi = 4, delta_kappa = 1/6.
    GV seed: n^0_1 = 1 (single vanishing cycle, class G, depth 2).
    Conifold monodromy: unipotent index 2, nilpotent rank 1.

All claims CONJECTURAL (conditional on CY-A_3, AP-CY6/AP-CY14).
Degeneration type: conifold (AP-CY157).

References:
    Greene-Morrison-Strominger, hep-th/9504145
    Strominger, hep-th/9504090
    Candelas-de la Ossa-Green-Parkes, NPB 359 (1991) 21
    Gopakumar-Vafa, hep-th/9809187
    Vol I: shadow obstruction tower
    Vol III: conifold_wall_crossing.py, conifold_bar_complex.py
"""

import pytest
from fractions import Fraction

from compute.lib.conifold_shadow_transition import (
    # Transition data
    ConifoldTransitionData,
    conifold_transition_data,
    quintic_conifold_transition,
    multi_node_quintic_transition,
    CONIFOLD_TRANSITIONS,
    all_conifold_transitions,
    # Period
    conifold_period_expansion,
    conifold_monodromy_data,
    # GV invariants
    GV_CONIFOLD_SEED,
    QUINTIC_GV_GENUS0,
    gv_seed_contribution,
    # Shadow tower
    ShadowTowerData,
    shadow_tower_smooth_quintic,
    shadow_tower_conifold_point,
    shadow_tower_resolved,
    shadow_transition_comparison,
    # GV-to-shadow
    gv_to_shadow_tower,
    conifold_seed_shadow,
    quintic_gv_shadow,
    # Log corrections
    log_period_shadow_correction,
    # Shadow metric
    shadow_metric_transition,
    shadow_metric_across_transition,
    # Comprehensive
    conifold_shadow_transition_comprehensive,
)


# ================================================================
# 1. HODGE ARITHMETIC
# ================================================================

class TestHodgeArithmetic:
    """Verify Hodge number changes across the conifold transition."""

    def test_quintic_hodge_before(self):
        """Quintic before transition: h^{1,1}=1, h^{2,1}=101."""
        t = quintic_conifold_transition()
        # VERIFIED [DC] Candelas et al. [LT] mirror symmetry
        assert t.h11_before == 1
        assert t.h21_before == 101

    def test_quintic_hodge_after(self):
        """After 1-node resolution: h^{1,1}=2, h^{2,1}=100."""
        t = quintic_conifold_transition()
        # VERIFIED [DC] h11 increases by 1, h21 decreases by 1
        assert t.h11_after == 2
        assert t.h21_after == 100

    def test_quintic_chi_before(self):
        """chi(quintic) = 2*(1-101) = -200."""
        t = quintic_conifold_transition()
        # VERIFIED [DC] Euler characteristic formula [LT] standard
        assert t.chi_before == -200

    def test_quintic_chi_after(self):
        """chi after resolution = 2*(2-100) = -196."""
        t = quintic_conifold_transition()
        assert t.chi_after == -196

    def test_delta_chi_per_node(self):
        """Each conifold node changes chi by +4."""
        t = quintic_conifold_transition()
        # VERIFIED [DC] topological surgery [LT] Clemens-Friedman
        assert t.delta_chi == 4

    def test_delta_chi_multi_node(self):
        """k nodes change chi by 4k."""
        for k in [1, 2, 5, 10]:
            t = multi_node_quintic_transition(k)
            assert t.delta_chi == 4 * k

    def test_hodge_sum_preserved(self):
        """h^{1,1} + h^{2,1} changes by 0 (one up, one down per node)."""
        t = quintic_conifold_transition()
        sum_before = t.h11_before + t.h21_before
        sum_after = t.h11_after + t.h21_after
        assert sum_before == sum_after

    def test_chi_formula_consistency(self):
        """chi = 2*(h^{1,1} - h^{2,1}) in all phases."""
        for k in [1, 3, 10, 50]:
            t = multi_node_quintic_transition(k)
            assert t.chi_before == 2 * (t.h11_before - t.h21_before)
            assert t.chi_after == 2 * (t.h11_after - t.h21_after)

    def test_max_nodes_boundary(self):
        """Cannot resolve more than h^{2,1} nodes."""
        with pytest.raises(ValueError):
            multi_node_quintic_transition(102)


# ================================================================
# 2. KAPPA ACROSS THE TRANSITION
# ================================================================

class TestKappaTransition:
    """Verify the BCOV-shadow candidate chi/24 across phases."""

    def test_kappa_before(self):
        """Quintic BCOV-shadow candidate = -25/3."""
        t = quintic_conifold_transition()
        # VERIFIED [DC] chi/24 = -200/24 = -25/3 [LT] fractional kappa
        assert t.kappa_ch_before == Fraction(-25, 3)

    def test_kappa_after_1_node(self):
        """kappa_ch after 1 node = -196/24 = -49/6."""
        t = quintic_conifold_transition()
        assert t.kappa_ch_after == Fraction(-196, 24)
        assert t.kappa_ch_after == Fraction(-49, 6)

    def test_delta_kappa_per_node(self):
        """Each node changes kappa by 4/24 = 1/6."""
        t = quintic_conifold_transition()
        # VERIFIED [DC] delta_chi/24 = 4/24 = 1/6
        assert t.delta_kappa == Fraction(1, 6)

    def test_delta_kappa_multi_node(self):
        """k nodes change kappa by k/6."""
        for k in [1, 2, 6, 12]:
            t = multi_node_quintic_transition(k)
            assert t.delta_kappa == Fraction(k, 6)

    def test_kappa_12_nodes_integral(self):
        """12 nodes: delta_kappa = 2 (integer). New kappa = -25/3 + 2 = -19/3."""
        t = multi_node_quintic_transition(12)
        assert t.delta_kappa == Fraction(2)
        assert t.kappa_ch_after == Fraction(-25, 3) + Fraction(2)
        assert t.kappa_ch_after == Fraction(-19, 3)

    def test_kappa_consistency(self):
        """kappa = chi/24 in both phases."""
        for k in [1, 5, 10]:
            t = multi_node_quintic_transition(k)
            assert t.kappa_ch_before == Fraction(t.chi_before, 24)
            assert t.kappa_ch_after == Fraction(t.chi_after, 24)


# ================================================================
# 3. SHADOW TOWER PHASES
# ================================================================

class TestShadowTowerPhases:
    """Verify shadow tower data in each phase of the transition."""

    def test_smooth_phase_class_M(self):
        """Smooth quintic is class M (infinite depth)."""
        s = shadow_tower_smooth_quintic()
        # VERIFIED [DC] infinite GV invariants -> class M [LT] AP-CY12
        assert s.shadow_class == "M"
        assert s.shadow_depth == -1  # infinite

    def test_smooth_phase_kappa(self):
        """Smooth quintic BCOV-shadow candidate = -25/3."""
        s = shadow_tower_smooth_quintic()
        assert s.kappa_ch == Fraction(-25, 3)

    def test_smooth_phase_S2(self):
        """S_2 equals the smooth quintic BCOV-shadow scalar."""
        s = shadow_tower_smooth_quintic()
        assert s.S_2 == s.kappa_ch

    def test_smooth_phase_no_log(self):
        """No log correction in smooth phase."""
        s = shadow_tower_smooth_quintic()
        assert s.log_correction is False

    def test_conifold_point_class_M(self):
        """Conifold point is still class M."""
        c = shadow_tower_conifold_point()
        assert c.shadow_class == "M"

    def test_conifold_point_log_correction(self):
        """Conifold point has log period correction."""
        c = shadow_tower_conifold_point()
        # VERIFIED [DC] Pi ~ t*log(t) singularity [LT] Candelas+91
        assert c.log_correction is True

    def test_conifold_point_S2_shifted(self):
        """At conifold point, S_2 gets a +1 shift from massless BPS state."""
        smooth = shadow_tower_smooth_quintic()
        conifold = shadow_tower_conifold_point()
        # The massless hypermultiplet adds 1 to S_2
        assert conifold.S_2 == smooth.S_2 + Fraction(1)

    def test_resolved_phase_class_M(self):
        """Resolved quintic (1 node) is still class M."""
        r = shadow_tower_resolved(1)
        # Class M persists: surviving tower from smooth phase is infinite
        assert r.shadow_class == "M"
        assert r.shadow_depth == -1

    def test_resolved_phase_kappa(self):
        """Resolved kappa_ch = -49/6."""
        r = shadow_tower_resolved(1)
        assert r.kappa_ch == Fraction(-49, 6)

    def test_resolved_no_log(self):
        """Resolved phase: no log correction (smooth again)."""
        r = shadow_tower_resolved(1)
        assert r.log_correction is False


# ================================================================
# 4. GV-TO-SHADOW DICTIONARY
# ================================================================

class TestGVToShadow:
    """Verify the GV invariant to shadow tower conversion."""

    def test_seed_gv(self):
        """n^0_1 = 1 is the conifold seed."""
        # VERIFIED [DC] single vanishing cycle [LT] Greene-Morrison-Strominger
        assert GV_CONIFOLD_SEED == {(0, 1): 1}

    def test_seed_contributes_to_S2(self):
        """Genus-0 BPS state contributes to S_2 (arity 2)."""
        shadow = gv_to_shadow_tower(GV_CONIFOLD_SEED, max_arity=8)
        assert shadow[2] == Fraction(1)

    def test_seed_no_higher_arity(self):
        """Genus-0 seed contributes nothing above arity 2."""
        shadow = gv_to_shadow_tower(GV_CONIFOLD_SEED, max_arity=8)
        for k in range(4, 9, 2):
            assert shadow[k] == Fraction(0)

    def test_seed_class_G(self):
        """The conifold seed is class G (Gaussian, depth 2)."""
        seed = conifold_seed_shadow()
        assert seed["shadow_class"] == "G"
        assert seed["shadow_depth"] == 2

    def test_genus_0_coefficient(self):
        """Genus-0 BPS-to-shadow coefficient is 1."""
        result = gv_seed_contribution(1, 0)
        assert result["coefficient"] == "1"
        assert result["target_arity"] == 2

    def test_genus_1_coefficient(self):
        """Genus-1 BPS-to-shadow coefficient is 1/12."""
        result = gv_seed_contribution(1, 1)
        # VERIFIED [DC] lambda_1 integral on M_{1,1} = 1/24 [LT] Faber-Pandharipande
        assert result["coefficient"] == "1/12"
        assert result["target_arity"] == 4

    def test_genus_2_coefficient(self):
        """Genus-2 BPS-to-shadow coefficient is |B_4|/(4*2!) = 1/(30*8) = 1/240."""
        result = gv_seed_contribution(1, 2)
        # |B_4| = 1/30, genus 2: 1/30 / (4 * 2) = 1/240
        assert result["coefficient"] == "1/240"
        assert result["target_arity"] == 6

    def test_gv_additivity(self):
        """GV contributions to shadow are additive."""
        gv1 = {(0, 1): 3}
        gv2 = {(0, 2): 5}
        gv_both = {(0, 1): 3, (0, 2): 5}

        s1 = gv_to_shadow_tower(gv1, max_arity=4)
        s2 = gv_to_shadow_tower(gv2, max_arity=4)
        s_both = gv_to_shadow_tower(gv_both, max_arity=4)

        assert s_both[2] == s1[2] + s2[2]

    def test_quintic_gv_S2_degree_1(self):
        """Quintic n^0_1 = 2875 contributes S_2 = 2875 at degree 1."""
        gv = {(0, 1): 2875}
        shadow = gv_to_shadow_tower(gv, max_arity=4)
        assert shadow[2] == Fraction(2875)

    def test_quintic_gv_shadow_growth(self):
        """Quintic GV S_2 grows rapidly with degree (class M signature)."""
        s3 = quintic_gv_shadow(3)
        s5 = quintic_gv_shadow(5)
        # More degrees -> larger S_2
        s3_val = Fraction(s3["shadow_S2_from_gv"])
        s5_val = Fraction(s5["shadow_S2_from_gv"])
        assert s5_val > s3_val


# ================================================================
# 5. LOG PERIOD CORRECTIONS
# ================================================================

class TestLogPeriodCorrections:
    """Verify logarithmic corrections to shadow coefficients."""

    def test_correction_alternating_sign(self):
        """Log corrections alternate in sign: (-1)^k / k."""
        lc = log_period_shadow_correction(8)
        corrections = lc["corrections"]
        # k=2: (-1)^2/2 = 1/2
        assert corrections["2"] == "1/2"
        # k=3: (-1)^3/3 = -1/3
        assert corrections["3"] == "-1/3"
        # k=4: (-1)^4/4 = 1/4
        assert corrections["4"] == "1/4"

    def test_correction_arity_2(self):
        """delta_S_2 = 1/2 (positive, from log expansion)."""
        lc = log_period_shadow_correction(4)
        assert Fraction(lc["corrections"]["2"]) == Fraction(1, 2)

    def test_correction_arity_3(self):
        """delta_S_3 = -1/3."""
        lc = log_period_shadow_correction(4)
        assert Fraction(lc["corrections"]["3"]) == Fraction(-1, 3)

    def test_corrections_sum_log2(self):
        """Sum of corrections: sum (-1)^k/k for k=2..inf = 1 - log(2)."""
        # Partial sum through k=8
        lc = log_period_shadow_correction(8)
        partial = sum(Fraction(v) for v in lc["corrections"].values())
        # 1/2 - 1/3 + 1/4 - 1/5 + 1/6 - 1/7 + 1/8 = ...
        expected = sum(Fraction((-1) ** k, k) for k in range(2, 9))
        assert partial == expected

    def test_degeneration_type_conifold(self):
        """Degeneration type is 'conifold' (AP-CY157)."""
        lc = log_period_shadow_correction(4)
        assert lc["degeneration_type"] == "conifold"


# ================================================================
# 6. CONIFOLD PERIOD
# ================================================================

class TestConifoldPeriod:
    """Verify the conifold period expansion."""

    def test_period_leading_coefficient(self):
        """Leading coefficient b_0 = 1 (normalization)."""
        coeffs = conifold_period_expansion(Fraction(1), 5)
        assert coeffs[0] == Fraction(1)

    def test_period_b1(self):
        """b_1 = -H_1/1! = -1."""
        coeffs = conifold_period_expansion(Fraction(1), 5)
        assert coeffs[1] == Fraction(-1)

    def test_period_b2(self):
        """b_2 = H_2/2! = (1+1/2)/2 = 3/4."""
        coeffs = conifold_period_expansion(Fraction(1), 5)
        assert coeffs[2] == Fraction(3, 4)

    def test_monodromy_unipotent(self):
        """Conifold monodromy is unipotent of index 2."""
        m = conifold_monodromy_data()
        # VERIFIED [DC] single vanishing S^3 [LT] Picard-Lefschetz
        assert m["monodromy_type"] == "unipotent_index_2"
        assert m["nilpotent_rank"] == 1
        assert m["nilpotent_index"] == 2

    def test_monodromy_degeneration_type(self):
        """Monodromy degeneration type is conifold (AP-CY157)."""
        m = conifold_monodromy_data()
        assert m["degeneration_type"] == "conifold"

    def test_vanishing_cycle_self_intersection(self):
        """Vanishing S^3 has self-intersection 0 in H_3."""
        m = conifold_monodromy_data()
        assert m["vanishing_cycle_self_intersection"] == 0


# ================================================================
# 7. SHADOW METRIC
# ================================================================

class TestShadowMetric:
    """Verify shadow metric and discriminant computations."""

    def test_class_G_metric(self):
        """Class G (alpha=0, S_4=0): discriminant = 0, depth 2."""
        m = shadow_metric_transition(Fraction(1))
        assert m["shadow_class"] == "G"
        assert m["shadow_depth"] == 2
        assert m["discriminant"] == "0"

    def test_class_G_Q_at_0(self):
        """Q_L(0) = 4*kappa^2."""
        m = shadow_metric_transition(Fraction(-25, 3))
        expected = 4 * Fraction(-25, 3) ** 2
        assert Fraction(m["Q_at_0"]) == expected

    def test_quintic_metric_positive(self):
        """Q_L(0) > 0 for any nonzero kappa (well-defined metric)."""
        m = shadow_metric_transition(Fraction(-25, 3))
        assert Fraction(m["Q_at_0"]) > 0

    def test_discriminant_formula(self):
        """Delta = -256 * kappa^3 * S_4."""
        kappa = Fraction(3, 2)
        S_4 = Fraction(10, 27)
        m = shadow_metric_transition(kappa, S_4=S_4)
        expected = Fraction(-256) * kappa ** 3 * S_4
        assert Fraction(m["discriminant"]) == expected

    def test_class_L_alpha_nonzero_S4_zero(self):
        """Class L: alpha != 0, Delta = 0 (S_4 = 0)."""
        m = shadow_metric_transition(Fraction(1), alpha=Fraction(2))
        assert m["shadow_class"] == "L"
        assert m["shadow_depth"] == 3

    def test_class_M_nonzero_discriminant(self):
        """Class M: Delta != 0 (infinite depth)."""
        m = shadow_metric_transition(Fraction(1), S_4=Fraction(1))
        assert m["shadow_class"] == "M"
        assert m["shadow_depth"] == -1

    def test_metric_across_transition(self):
        """Shadow metric changes across the transition."""
        result = shadow_metric_across_transition(1)
        k_before = Fraction(result["before_transition"]["kappa_ch"])
        k_after = Fraction(result["after_transition"]["kappa_ch"])
        assert k_before == Fraction(-25, 3)
        assert k_after == Fraction(-49, 6)


# ================================================================
# 8. TRANSITION COMPARISON
# ================================================================

class TestTransitionComparison:
    """Verify consistency of the full transition comparison."""

    def test_comparison_three_phases(self):
        """Comparison returns data for all three phases."""
        comp = shadow_transition_comparison(1)
        assert "smooth_phase" in comp
        assert "conifold_point" in comp
        assert "resolved_phase" in comp

    def test_comparison_class_preserved(self):
        """Shadow class is M in all three phases."""
        comp = shadow_transition_comparison(1)
        assert comp["smooth_phase"]["shadow_class"] == "M"
        assert comp["conifold_point"]["shadow_class"] == "M"
        assert comp["resolved_phase"]["shadow_class"] == "M"

    def test_comparison_seed_class_G(self):
        """The seed channel is class G."""
        comp = shadow_transition_comparison(1)
        assert comp["seed_data"]["seed_class"] == "G (Gaussian, depth 2)"

    def test_comparison_seed_kappa(self):
        """Seed kappa = 1/6 (= delta_kappa per node)."""
        comp = shadow_transition_comparison(1)
        assert comp["seed_data"]["seed_kappa"] == "1/6"


# ================================================================
# 9. MULTI-NODE EXAMPLES
# ================================================================

class TestMultiNode:
    """Verify multi-node conifold transitions."""

    def test_all_standard_transitions(self):
        """All standard conifold transitions have valid data."""
        for t in all_conifold_transitions():
            assert t.chi_before == 2 * (t.h11_before - t.h21_before)
            assert t.chi_after == 2 * (t.h11_after - t.h21_after)
            assert t.delta_chi == 4 * t.num_nodes

    def test_schoen_transition(self):
        """Schoen manifold (h11=19, h21=19): chi=0, self-mirror."""
        t = conifold_transition_data("Schoen", 19, 19, 1)
        assert t.chi_before == 0
        assert t.chi_after == 4
        assert t.kappa_ch_before == Fraction(0)
        assert t.kappa_ch_after == Fraction(1, 6)

    def test_quintic_16_nodes(self):
        """Quintic with 16 nodes: (1,101) -> (17,85)."""
        t = multi_node_quintic_transition(16)
        assert t.h11_after == 17
        assert t.h21_after == 85
        assert t.delta_chi == 64


# ================================================================
# 10. COMPREHENSIVE ANALYSIS
# ================================================================

class TestComprehensive:
    """Verify the comprehensive shadow transition analysis."""

    def test_comprehensive_returns_all_sections(self):
        """Comprehensive analysis includes all required sections."""
        result = conifold_shadow_transition_comprehensive(
            num_nodes=1, max_gv_degree=3, max_arity=6)
        assert "transition_data" in result
        assert "shadow_phases" in result
        assert "gv_analysis" in result
        assert "log_period_corrections" in result
        assert "shadow_metrics" in result
        assert "monodromy" in result
        assert "period_regular_coeffs" in result

    def test_comprehensive_claim_status(self):
        """All claims are conjectural (conditional on CY-A_3)."""
        result = conifold_shadow_transition_comprehensive()
        assert "CONJECTURAL" in result["claim_status"]
        assert "CY-A_3" in result["claim_status"]

    def test_comprehensive_degeneration_type(self):
        """Degeneration type is conifold (AP-CY157)."""
        result = conifold_shadow_transition_comprehensive()
        assert "conifold" in result["degeneration_type"]

    def test_comprehensive_transition_data(self):
        """Transition data is consistent."""
        result = conifold_shadow_transition_comprehensive(num_nodes=1)
        td = result["transition_data"]
        assert td["chi_before"] == -200
        assert td["chi_after"] == -196
        assert td["delta_chi"] == 4

    def test_comprehensive_shadow_phases(self):
        """All three shadow phases are present and class M."""
        result = conifold_shadow_transition_comprehensive()
        sp = result["shadow_phases"]
        for phase in ["smooth", "conifold_point", "resolved"]:
            assert phase in sp
            assert sp[phase]["class"] == "M"

    def test_comprehensive_seed(self):
        """Seed mechanism is present in GV analysis."""
        result = conifold_shadow_transition_comprehensive()
        seed = result["gv_analysis"]["seed"]
        assert seed["shadow_class"] == "G"
        assert seed["shadow_depth"] == 2

    def test_comprehensive_period_coefficients(self):
        """Period expansion has correct number of coefficients."""
        result = conifold_shadow_transition_comprehensive()
        coeffs = result["period_regular_coeffs"]
        assert len(coeffs) == 6  # default num_terms=6
        assert Fraction(coeffs[0]) == Fraction(1)  # b_0 = 1


# ================================================================
# 11. MULTI-PATH CROSS-VERIFICATION (AP10)
# ================================================================

class TestMultiPathCrossVerification:
    """Cross-check assertions via independent computation paths.

    Each test verifies the SAME quantity via two or more independent
    methods, ensuring no single-path confabulation (AP10).

    Five independent paths:
        Path A: direct Hodge arithmetic (chi = 2*(h11-h21))
        Path B: transition formula (delta_chi = 4*k, kappa = chi/24)
        Path C: GV-to-shadow dictionary (BPS -> shadow arity)
        Path D: shadow metric (Q_L(t) formula)
        Path E: comprehensive analysis (all-in-one)
    """

    def test_cross_chi_two_paths(self):
        """Cross-check chi via direct Hodge arithmetic (A) and transition (B).

        Path A: chi = 2*(h11 - h21) computed directly.
        Path B: chi_after = chi_before + 4*k from transition formula.
        """
        # Path A: direct
        h11_a, h21_a = 2, 100
        chi_A = 2 * (h11_a - h21_a)

        # Path B: from transition
        t = quintic_conifold_transition()
        chi_B = t.chi_before + t.delta_chi

        assert chi_A == chi_B == -196

    def test_cross_kappa_two_paths(self):
        """Cross-check kappa via chi/24 (A) and transition delta (B).

        Path A: kappa = chi_after / 24 directly.
        Path B: kappa = kappa_before + delta_kappa.
        """
        t = quintic_conifold_transition()

        # Path A: direct from chi_after
        kappa_A = Fraction(t.chi_after, 24)

        # Path B: from transition
        kappa_B = t.kappa_ch_before + t.delta_kappa

        assert kappa_A == kappa_B

    def test_cross_delta_kappa_two_paths(self):
        """Cross-check delta_kappa via two formulas.

        Path A: delta_kappa = kappa_after - kappa_before (subtraction).
        Path B: delta_kappa = delta_chi / 24 = 4k/24 = k/6 (formula).
        """
        for k in [1, 3, 6, 12]:
            t = multi_node_quintic_transition(k)

            # Path A: subtraction
            delta_A = t.kappa_ch_after - t.kappa_ch_before

            # Path B: formula
            delta_B = Fraction(k, 6)

            assert delta_A == delta_B == t.delta_kappa

    def test_cross_seed_shadow_two_paths(self):
        """Cross-check seed shadow via GV dictionary (C) and direct (D).

        Path C: gv_to_shadow_tower({(0,1): 1}) at arity 2.
        Path D: gv_seed_contribution(1, 0) coefficient * multiplicity.
        """
        # Path C: dictionary
        shadow_C = gv_to_shadow_tower(GV_CONIFOLD_SEED, max_arity=8)

        # Path D: direct computation
        result_D = gv_seed_contribution(1, 0)
        shadow_D = Fraction(result_D["contribution_to_shadow"])

        assert shadow_C[2] == shadow_D == Fraction(1)

    def test_cross_gv_additivity_three_paths(self):
        """Cross-check GV additivity via three paths.

        Path C1: compute shadow of combined GV data.
        Path C2: compute shadow of each part and sum.
        Path C3: manual arithmetic check.
        """
        gv_part1 = {(0, 1): 2875}
        gv_part2 = {(0, 2): 609250}
        gv_combined = {(0, 1): 2875, (0, 2): 609250}

        # Path C1: combined
        s_combined = gv_to_shadow_tower(gv_combined, max_arity=4)

        # Path C2: sum of parts
        s1 = gv_to_shadow_tower(gv_part1, max_arity=4)
        s2 = gv_to_shadow_tower(gv_part2, max_arity=4)
        s_sum = s1[2] + s2[2]

        # Path C3: manual
        s_manual = Fraction(2875 + 609250)

        assert s_combined[2] == s_sum == s_manual

    def test_cross_shadow_metric_Q0_two_paths(self):
        """Cross-check Q_L(0) via shadow_metric_transition (D) and direct (A).

        Path D: shadow_metric_transition returns Q_at_0.
        Path A: direct computation 4 * kappa^2.
        """
        kappa = Fraction(-25, 3)

        # Path D
        metric = shadow_metric_transition(kappa)
        Q_D = Fraction(metric["Q_at_0"])

        # Path A: direct
        Q_A = 4 * kappa ** 2

        assert Q_D == Q_A == Fraction(2500, 9)

    def test_cross_discriminant_two_paths(self):
        """Cross-check discriminant via shadow_metric_transition (D) and direct (A).

        Path D: shadow_metric_transition returns discriminant.
        Path A: direct computation -256 * kappa^3 * S_4.
        """
        kappa = Fraction(3, 2)
        S_4 = Fraction(10, 27)

        # Path D
        metric = shadow_metric_transition(kappa, S_4=S_4)
        disc_D = Fraction(metric["discriminant"])

        # Path A: direct
        disc_A = Fraction(-256) * kappa ** 3 * S_4

        assert disc_D == disc_A

    def test_cross_comprehensive_vs_components(self):
        """Cross-check comprehensive output against individual component calls.

        Path E: comprehensive analysis.
        Paths A+B: direct Hodge + transition.
        Path C: GV seed.
        """
        # Path E: comprehensive
        comp = conifold_shadow_transition_comprehensive(num_nodes=1)

        # Path A: direct
        t = quintic_conifold_transition()
        assert comp["transition_data"]["chi_before"] == t.chi_before
        assert comp["transition_data"]["chi_after"] == t.chi_after
        assert comp["transition_data"]["delta_chi"] == t.delta_chi

        # Path C: GV seed
        seed_direct = conifold_seed_shadow()
        seed_comp = comp["gv_analysis"]["seed"]
        assert seed_comp["shadow_class"] == seed_direct["shadow_class"]
        assert seed_comp["shadow_depth"] == seed_direct["shadow_depth"]

    def test_cross_log_correction_sum_vs_direct(self):
        """Cross-check log correction partial sums.

        Path 1: sum individual corrections from log_period_shadow_correction.
        Path 2: direct computation of sum_{k=2}^{N} (-1)^k / k.
        """
        lc = log_period_shadow_correction(8)
        corrections = lc["corrections"]

        # Path 1: from the engine
        sum_engine = sum(Fraction(v) for v in corrections.values())

        # Path 2: direct
        sum_direct = sum(Fraction((-1) ** k, k) for k in range(2, 9))

        assert sum_engine == sum_direct

    def test_cross_period_coefficients_recurrence(self):
        """Cross-check period coefficients via the harmonic number recurrence.

        Path 1: conifold_period_expansion output.
        Path 2: direct computation b_k = (-1)^k * H_k / k!.
        """
        coeffs = conifold_period_expansion(Fraction(1), 6)

        # Path 2: independent computation
        H = Fraction(0)
        fact_inv = Fraction(1)
        for k in range(6):
            if k == 0:
                assert coeffs[k] == Fraction(1)
            else:
                H += Fraction(1, k)
                fact_inv /= Fraction(k)
                expected = Fraction((-1) ** k) * H * fact_inv
                assert coeffs[k] == expected

    def test_cross_hodge_sum_two_paths(self):
        """Cross-check h11+h21 preservation two ways.

        Path A: direct comparison of sums.
        Path B: from transition data: delta_h11 + delta_h21 = k + (-k) = 0.
        """
        for k in [1, 5, 20]:
            t = multi_node_quintic_transition(k)
            # Path A
            assert t.h11_before + t.h21_before == t.h11_after + t.h21_after
            # Path B
            delta_h11 = t.h11_after - t.h11_before
            delta_h21 = t.h21_after - t.h21_before
            assert delta_h11 == k
            assert delta_h21 == -k
            assert delta_h11 + delta_h21 == 0

    def test_cross_class_M_all_phases_two_paths(self):
        """Cross-check class M across phases via comparison (E) and individual (A).

        Path E: shadow_transition_comparison output.
        Path A: individual shadow_tower_* calls.
        """
        # Path E
        comp = shadow_transition_comparison(1)

        # Path A
        smooth = shadow_tower_smooth_quintic()
        conifold = shadow_tower_conifold_point()
        resolved = shadow_tower_resolved(1)

        assert comp["smooth_phase"]["shadow_class"] == smooth.shadow_class == "M"
        assert comp["conifold_point"]["shadow_class"] == conifold.shadow_class == "M"
        assert comp["resolved_phase"]["shadow_class"] == resolved.shadow_class == "M"
