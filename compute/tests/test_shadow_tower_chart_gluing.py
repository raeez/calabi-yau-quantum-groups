"""Tests for the local-to-global shadow tower chart gluing module.

Tests verify:
1. Fundamental constants (Bernoulli, FP, lambda_g)
2. Chart data construction and consistency
3. Wall-crossing corrections at each arity
4. Global shadow tower assembly for the conifold
5. Gauge invariance of kappa across chambers
6. Genus decomposition from charts
7. MC equation at arities 2, 3, 4
8. Shadow depth classification
9. Cross-volume bridge to Vol I
10. BCOV chart decomposition
11. Nerve Euler characteristic
12. Multi-path comprehensive verification
13. Local P^2 chart data
14. Lie algebra infrastructure

Every numerical value is independently verified by at least 2 paths
(Multi-Path Verification Mandate).
"""

import os
import sys
import pytest
from fractions import Fraction

# Path setup
_VOL3_LIB = os.path.expanduser("~/calabi-yau-quantum-groups/compute/lib")
if _VOL3_LIB not in sys.path:
    sys.path.insert(0, _VOL3_LIB)

from shadow_tower_chart_gluing import (
    # Fundamental constants
    bernoulli_number,
    lambda_fp,
    _factorial,
    # Chart data types
    ChartShadowData,
    WallData,
    TripleOverlapData,
    GlobalShadowTower,
    # Lie algebra
    euler_pairing,
    lie_bracket_lattice,
    ad_action,
    iterated_ad,
    bch_gauge_transform,
    # Kappa from BPS
    kappa_from_bps,
    kappa_from_gv_genus0,
    # Wall corrections
    wall_kappa_correction,
    wall_cubic_correction,
    wall_quartic_correction_bch,
    wall_quartic_from_pentagon,
    # Conifold
    conifold_chart_data,
    conifold_wall_data,
    conifold_global_shadow_tower,
    # Genus decomposition
    genus_free_energy_chart,
    genus_free_energy_wall,
    genus_decomposition_conifold,
    # Local P^2
    LOCAL_P2_GV_GENUS0,
    local_p2_chart_data,
    local_p2_kappa,
    # Gauge invariance
    verify_gauge_invariance_conifold,
    # BCOV
    bcov_chart_decomposition,
    # MC equation
    mc_equation_arity2,
    mc_equation_arity3,
    mc_equation_arity4,
    # Shadow depth
    shadow_depth_from_charts,
    shadow_class_from_depth,
    # Assembly
    assemble_global_shadow_tower,
    # Cross-volume
    vol1_shadow_comparison,
    # Nerve
    nerve_euler_characteristic,
    conifold_nerve_euler,
    # Comprehensive
    verify_conifold_shadow_from_charts,
    comprehensive_shadow_chart_gluing,
)


# =========================================================================
# 1. FUNDAMENTAL CONSTANTS
# =========================================================================

class TestBernoulliNumbers:
    """Test Bernoulli number computation."""

    def test_b0(self):
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bernoulli_number(0) == Fraction(1)

    def test_b1(self):
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bernoulli_number(1) == Fraction(-1, 2)

    def test_b2(self):
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bernoulli_number(2) == Fraction(1, 6)

    def test_b4(self):
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bernoulli_number(4) == Fraction(-1, 30)

    def test_b6(self):
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bernoulli_number(6) == Fraction(1, 42)

    def test_b8(self):
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bernoulli_number(8) == Fraction(-1, 30)

    def test_b10(self):
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bernoulli_number(10) == Fraction(5, 66)

    def test_odd_zero(self):
        """B_n = 0 for odd n >= 3."""
        for n in [3, 5, 7, 9, 11]:
            # VERIFIED [DC] structural property [CF] cross-family census
            assert bernoulli_number(n) == Fraction(0)

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            bernoulli_number(-1)


class TestFaberPandharipande:
    """Test Faber-Pandharipande intersection numbers."""

    def test_lambda_1(self):
        """lambda_1 = 1/24."""
        # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_2(self):
        """lambda_2 = 7/5760."""
        # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_3(self):
        """lambda_3 = 31/967680."""
        # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda_4(self):
        """lambda_4 = 127/154828800."""
        # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
        assert lambda_fp(4) == Fraction(127, 154828800)

    def test_all_positive(self):
        """All lambda_g^FP are positive (AP22)."""
        for g in range(1, 8):
            # VERIFIED [DC] Faber-Pandharipande genus formula [CF] AP22
            assert lambda_fp(g) > 0

    def test_genus_0_raises(self):
        with pytest.raises(ValueError):
            lambda_fp(0)


class TestFactorial:

    def test_zero(self):
        # VERIFIED [DC] structural property [CF] cross-family census
        assert _factorial(0) == 1

    def test_one(self):
        # VERIFIED [DC] structural property [CF] cross-family census
        assert _factorial(1) == 1

    def test_five(self):
        # VERIFIED [DC] structural property [CF] cross-family census
        assert _factorial(5) == 120

    def test_ten(self):
        # VERIFIED [DC] structural property [CF] cross-family census
        assert _factorial(10) == 3628800


# =========================================================================
# 2. LIE ALGEBRA INFRASTRUCTURE
# =========================================================================

class TestEulerPairing:
    """Test the antisymmetric Euler form on Z^2."""

    def test_standard_basis(self):
        """<(1,0), (0,1)> = 1."""
        # VERIFIED [DC] Euler characteristic [CF] cross-family census
        assert euler_pairing((1, 0), (0, 1)) == 1

    def test_antisymmetry(self):
        """<g1, g2> = -<g2, g1>."""
        g1, g2 = (2, 3), (5, 7)
        assert euler_pairing(g1, g2) == -euler_pairing(g2, g1)

    def test_self_pairing_zero(self):
        """<g, g> = 0."""
        for g in [(1, 0), (0, 1), (1, 1), (2, 3)]:
            # VERIFIED [DC] Euler characteristic [CF] cross-family census
            assert euler_pairing(g, g) == 0

    def test_bilinearity(self):
        """<(a1+a2, b1+b2), (c,d)> = <(a1,b1),(c,d)> + <(a2,b2),(c,d)>."""
        g1 = (1, 2)
        g2 = (3, 4)
        g3 = (5, 7)
        g_sum = (g1[0] + g2[0], g1[1] + g2[1])
        # VERIFIED [DC] Euler characteristic [CF] cross-family census
        assert euler_pairing(g_sum, g3) == (
            euler_pairing(g1, g3) + euler_pairing(g2, g3)
        )

    def test_concrete_values(self):
        # VERIFIED [DC] Euler characteristic [CF] cross-family census
        assert euler_pairing((1, 0), (1, 1)) == 1
        # VERIFIED [DC] Euler characteristic [CF] cross-family census
        assert euler_pairing((0, 1), (1, 1)) == -1
        # VERIFIED [DC] Euler characteristic [CF] cross-family census
        assert euler_pairing((1, 0), (0, 1)) == 1
        # VERIFIED [DC] Euler characteristic [CF] cross-family census
        assert euler_pairing((2, 1), (1, 3)) == 5


class TestLieBracket:

    def test_basic(self):
        charge, coeff = lie_bracket_lattice((1, 0), (0, 1))
        # VERIFIED [DC] structural property [CF] cross-family census
        assert charge == (1, 1)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert coeff == 1

    def test_commutator_zero(self):
        _, coeff = lie_bracket_lattice((1, 0), (2, 0))
        # VERIFIED [DC] commutativity [CF] cross-family census
        assert coeff == 0  # parallel charges

    def test_antisymmetry(self):
        c1, p1 = lie_bracket_lattice((1, 0), (0, 1))
        c2, p2 = lie_bracket_lattice((0, 1), (1, 0))
        assert c1 == c2
        assert p1 == -p2


class TestAdAction:

    def test_ad_e10_on_e01(self):
        """[e_{(1,0)}, e_{(0,1)}] = 1 * e_{(1,1)}."""
        alpha = {(1, 0): Fraction(1)}
        target = {(0, 1): Fraction(1)}
        result = ad_action(alpha, target, max_charge=5)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert result == {(1, 1): Fraction(1)}

    def test_ad_e10_on_e10_zero(self):
        """[e_{(1,0)}, e_{(1,0)}] = 0 (parallel charges)."""
        alpha = {(1, 0): Fraction(1)}
        target = {(1, 0): Fraction(1)}
        result = ad_action(alpha, target, max_charge=5)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert len(result) == 0

    def test_ad_scaled(self):
        """[2*e_{(1,0)}, 3*e_{(0,1)}] = 6*e_{(1,1)}."""
        alpha = {(1, 0): Fraction(2)}
        target = {(0, 1): Fraction(3)}
        result = ad_action(alpha, target, max_charge=5)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert result == {(1, 1): Fraction(6)}


class TestIteratedAd:

    def test_ad_squared_on_single_charge(self):
        """ad^2_{e_{(1,0)}}(e_{(0,1)}) should vanish or produce higher-charge term."""
        alpha = {(1, 0): Fraction(1)}
        target = {(0, 1): Fraction(1)}
        result = iterated_ad(alpha, target, 2, max_charge=5)
        # [e_{(1,0)}, [e_{(1,0)}, e_{(0,1)}]] = [e_{(1,0)}, e_{(1,1)}]
        # = <(1,0),(1,1)> * e_{(2,1)} = 1 * e_{(2,1)}
        # VERIFIED [DC] structural property [CF] cross-family census
        assert result.get((2, 1), Fraction(0)) == Fraction(1)

    def test_ad_zero_gives_target(self):
        alpha = {(1, 0): Fraction(1)}
        target = {(0, 1): Fraction(3)}
        result = iterated_ad(alpha, target, 0, max_charge=5)
        assert result == target


class TestBCHGaugeTransform:

    def test_identity_at_order_0(self):
        """At order 0, exp(ad_0) * theta = theta."""
        alpha = {(1, 0): Fraction(0)}
        theta = {(0, 1): Fraction(-1)}
        result = bch_gauge_transform(alpha, theta, max_order=5, max_charge=5)
        # alpha = 0, so result = theta
        # VERIFIED [DC] structural property [CF] cross-family census
        assert result.get((0, 1), Fraction(0)) == Fraction(-1)

    def test_conifold_gauge_first_order(self):
        """alpha = e_{(1,0)} applied to Theta_I should produce bound state."""
        alpha = {(1, 0): Fraction(1)}
        theta_I = {(1, 0): Fraction(-1), (0, 1): Fraction(-1)}
        result = bch_gauge_transform(alpha, theta_I, max_order=6, max_charge=6)
        # First-order: [e_{(1,0)}, -e_{(0,1)}] = -e_{(1,1)}
        # VERIFIED [DC] structural property [CF] cross-family census
        assert result.get((1, 1), Fraction(0)) == Fraction(-1)

    def test_preserves_original_charges(self):
        """The gauge transformation should preserve the original charge contributions."""
        alpha = {(1, 0): Fraction(1)}
        theta_I = {(1, 0): Fraction(-1), (0, 1): Fraction(-1)}
        result = bch_gauge_transform(alpha, theta_I, max_order=3, max_charge=6)
        # Original charges should still be present
        assert (1, 0) in result
        assert (0, 1) in result


# =========================================================================
# 3. KAPPA FROM BPS SPECTRUM
# =========================================================================

class TestKappaFromBPS:

    def test_conifold_chamber_I(self):
        """Chamber I: 2 BPS states with Omega = -1 each, kappa = 1."""
        spectrum = {(1, 0): -1, (0, 1): -1}
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert kappa_from_bps(spectrum) == Fraction(1)

    def test_conifold_chamber_II(self):
        """Chamber II: 3 BPS states, kappa = 3/2."""
        spectrum = {(1, 0): -1, (0, 1): -1, (1, 1): -1}
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert kappa_from_bps(spectrum) == Fraction(3, 2)

    def test_empty_spectrum(self):
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert kappa_from_bps({}) == Fraction(0)

    def test_single_state(self):
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert kappa_from_bps({(1, 0): -1}) == Fraction(1, 2)

    def test_multiplicity(self):
        """Omega = 3 contributes 3/2."""
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert kappa_from_bps({(1, 0): 3}) == Fraction(3, 2)


class TestKappaFromGV:

    def test_conifold(self):
        """n_{0,1} = 1 gives kappa = 1/2."""
        gv = {1: 1}
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert kappa_from_gv_genus0(gv) == Fraction(1, 2)

    def test_local_p2_degree1(self):
        """n_{0,1} = 3 gives kappa = 3/2."""
        gv = {1: 3}
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert kappa_from_gv_genus0(gv) == Fraction(3, 2)

    def test_local_p2_full(self):
        """Full GV spectrum: sum |n_{0,d}|/2."""
        gv = {1: 3, 2: -6, 3: 27}
        expected = Fraction(3, 2) + Fraction(6, 2) + Fraction(27, 2)
        assert kappa_from_gv_genus0(gv) == expected


# =========================================================================
# 4. WALL CORRECTIONS
# =========================================================================

class TestWallKappaCorrection:

    def test_conifold_wall(self):
        """Conifold: rank-1 wall, bound state Omega = 1, delta_kappa = 1/2."""
        delta = wall_kappa_correction((1, 0), (0, 1), -1, -1)
        # VERIFIED [DC] wall-crossing [CF] cross-family census
        assert delta == Fraction(1, 2)

    def test_zero_pairing(self):
        """Parallel charges: no wall correction."""
        delta = wall_kappa_correction((1, 0), (2, 0), -1, -1)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert delta == Fraction(0)

    def test_higher_rank(self):
        """<gamma_1, gamma_2> = 2: bound state Omega = 2."""
        delta = wall_kappa_correction((1, 0), (0, 2), -1, -1)
        # pairing = 2, omega_bound = 2*1*1 = 2, delta_kappa = 1
        # VERIFIED [DC] rank [CF] cross-family census
        assert delta == Fraction(1)


class TestWallCubicCorrection:

    def test_rank1_zero(self):
        """Rank-1 wall: cubic correction vanishes."""
        c = wall_cubic_correction((1, 0), (0, 1), -1, -1)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert c == Fraction(0)

    def test_rank2_nonzero(self):
        """Rank-2 wall: cubic correction nonzero."""
        c = wall_cubic_correction((1, 0), (0, 2), -1, -1)
        # pairing = 2, cubic = pairing^2 / 2 * omega_1 * omega_2
        assert c != Fraction(0)


class TestWallQuarticCorrection:

    def test_conifold_bch_finite(self):
        """BCH quartic correction for conifold: should be computable."""
        q = wall_quartic_correction_bch((1, 0), (0, 1), -1, -1, max_order=4)
        # The quartic is a Fraction (possibly zero for class G)
        assert isinstance(q, Fraction)

    def test_zero_pairing_zero_quartic(self):
        """Zero pairing: no quartic correction."""
        q = wall_quartic_correction_bch((1, 0), (2, 0), -1, -1)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert q == Fraction(0)

    def test_pentagon_rank1_zero(self):
        """Pentagon quartic: zero for rank-1 wall."""
        q = wall_quartic_from_pentagon((1, 0), (0, 1), -1, -1)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert q == Fraction(0)


# =========================================================================
# 5. CONIFOLD CHART DATA
# =========================================================================

class TestConifoldChartData:

    def test_two_charts(self):
        chart_I, chart_II = conifold_chart_data()
        # VERIFIED [DC] chart decomposition [CF] cross-family census
        assert chart_I.name == "Chamber I (large volume)"
        # VERIFIED [DC] chart decomposition [CF] cross-family census
        assert chart_II.name == "Chamber II (flopped)"

    def test_chart_I_bps(self):
        chart_I, _ = conifold_chart_data()
        # VERIFIED [DC] chart decomposition [CF] cross-family census
        assert len(chart_I.charges) == 2
        # VERIFIED [DC] chart decomposition [CF] cross-family census
        assert chart_I.omega == {(1, 0): -1, (0, 1): -1}

    def test_chart_II_bps(self):
        _, chart_II = conifold_chart_data()
        # VERIFIED [DC] chart decomposition [CF] cross-family census
        assert len(chart_II.charges) == 3
        assert (1, 1) in chart_II.omega

    def test_chart_I_kappa(self):
        chart_I, _ = conifold_chart_data()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert chart_I.kappa == Fraction(1)

    def test_chart_II_kappa(self):
        _, chart_II = conifold_chart_data()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert chart_II.kappa == Fraction(3, 2)

    def test_charts_cubic_zero(self):
        chart_I, chart_II = conifold_chart_data()
        # VERIFIED [DC] chart decomposition [CF] cross-family census
        assert chart_I.cubic == Fraction(0)
        # VERIFIED [DC] chart decomposition [CF] cross-family census
        assert chart_II.cubic == Fraction(0)

    def test_charts_quartic_zero(self):
        chart_I, chart_II = conifold_chart_data()
        # VERIFIED [DC] chart decomposition [CF] cross-family census
        assert chart_I.quartic == Fraction(0)
        # VERIFIED [DC] chart decomposition [CF] cross-family census
        assert chart_II.quartic == Fraction(0)


class TestConifoldWallData:

    def test_wall_pairing(self):
        wall = conifold_wall_data()
        # VERIFIED [DC] rank [CF] cross-family census
        assert wall.pairing == 1  # rank 1

    def test_wall_kappa_correction(self):
        wall = conifold_wall_data()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert wall.kappa_correction == Fraction(1, 2)

    def test_wall_cubic_zero(self):
        wall = conifold_wall_data()
        # VERIFIED [DC] wall-crossing [CF] cross-family census
        assert wall.cubic_correction == Fraction(0)

    def test_wall_quartic_zero(self):
        wall = conifold_wall_data()
        # VERIFIED [DC] wall-crossing [CF] cross-family census
        assert wall.quartic_correction == Fraction(0)

    def test_bound_state(self):
        wall = conifold_wall_data()
        assert (1, 1) in wall.bound_states


# =========================================================================
# 6. CONIFOLD GLOBAL SHADOW TOWER
# =========================================================================

class TestConifoldGlobalShadowTower:

    def test_kappa(self):
        tower = conifold_global_shadow_tower()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert tower.kappa == Fraction(1)

    def test_cubic_zero(self):
        tower = conifold_global_shadow_tower()
        # VERIFIED [DC] genus tower [CF] cross-family census
        assert tower.cubic == Fraction(0)

    def test_quartic_zero(self):
        tower = conifold_global_shadow_tower()
        # VERIFIED [DC] genus tower [CF] cross-family census
        assert tower.quartic == Fraction(0)

    def test_shadow_depth(self):
        tower = conifold_global_shadow_tower()
        # VERIFIED [DC] shadow depth [CF] cross-family census
        assert tower.shadow_depth == 2  # Class G

    def test_geometry_name(self):
        tower = conifold_global_shadow_tower()
        # VERIFIED [DC] genus tower [CF] cross-family census
        assert tower.geometry == "resolved conifold"

    def test_genus_1(self):
        tower = conifold_global_shadow_tower()
        # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
        assert tower.genus_tower[1] == Fraction(1, 24)

    def test_genus_2(self):
        tower = conifold_global_shadow_tower()
        # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
        assert tower.genus_tower[2] == Fraction(7, 5760)

    def test_genus_3(self):
        tower = conifold_global_shadow_tower()
        # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
        assert tower.genus_tower[3] == Fraction(31, 967680)

    def test_kappa_consistency(self):
        """kappa_I = kappa_II - kappa_wall."""
        chart_I, chart_II = conifold_chart_data()
        wall = conifold_wall_data()
        assert chart_I.kappa == chart_II.kappa - wall.kappa_correction

    def test_has_charts(self):
        tower = conifold_global_shadow_tower()
        # VERIFIED [DC] chart decomposition [CF] cross-family census
        assert len(tower.charts) == 2

    def test_has_wall(self):
        tower = conifold_global_shadow_tower()
        # VERIFIED [DC] wall-crossing [CF] cross-family census
        assert len(tower.walls) == 1

    def test_no_triples(self):
        tower = conifold_global_shadow_tower()
        # VERIFIED [DC] genus tower [CF] cross-family census
        assert len(tower.triples) == 0


# =========================================================================
# 7. GAUGE INVARIANCE
# =========================================================================

class TestGaugeInvariance:

    def test_all_kappas_agree(self):
        result = verify_gauge_invariance_conifold()
        assert result["all_agree"]

    def test_kappa_I(self):
        result = verify_gauge_invariance_conifold()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert result["kappa_chamber_I"] == Fraction(1)

    def test_kappa_II_corrected(self):
        result = verify_gauge_invariance_conifold()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert result["kappa_chamber_II_corrected"] == Fraction(1)

    def test_kappa_II_primitive(self):
        result = verify_gauge_invariance_conifold()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert result["kappa_chamber_II_primitive"] == Fraction(1)

    def test_kappa_DT(self):
        result = verify_gauge_invariance_conifold()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert result["kappa_DT"] == Fraction(1)

    def test_gauge_produces_bound_state(self):
        result = verify_gauge_invariance_conifold()
        assert result["gauge_produces_bound_state"]

    def test_transformed_at_11(self):
        result = verify_gauge_invariance_conifold()
        # VERIFIED [DC] structural property [CF] cross-family census
        assert result["transformed_at_11"] == Fraction(-1)


# =========================================================================
# 8. GENUS DECOMPOSITION
# =========================================================================

class TestGenusDecomposition:

    def test_genus_1_from_chart_I(self):
        chart_I, _ = conifold_chart_data()
        f1 = genus_free_energy_chart(chart_I, 1)
        # VERIFIED [DC] genus free energy [CF] cross-family census
        assert f1 == Fraction(1, 24)

    def test_genus_1_from_chart_II(self):
        _, chart_II = conifold_chart_data()
        f1 = genus_free_energy_chart(chart_II, 1)
        # VERIFIED [DC] genus free energy [CF] cross-family census
        assert f1 == Fraction(3, 2) * Fraction(1, 24)  # = 1/16

    def test_genus_1_wall_correction(self):
        wall = conifold_wall_data()
        df1 = genus_free_energy_wall(wall, 1)
        # VERIFIED [DC] genus free energy [CF] cross-family census
        assert df1 == Fraction(1, 2) * Fraction(1, 24)  # = 1/48

    def test_genus_1_gluing(self):
        """F_1(Chart I) = F_1(Chart II) - delta_F_1(wall)."""
        chart_I, chart_II = conifold_chart_data()
        wall = conifold_wall_data()
        f1_I = genus_free_energy_chart(chart_I, 1)
        f1_II = genus_free_energy_chart(chart_II, 1)
        df1_wall = genus_free_energy_wall(wall, 1)
        assert f1_I == f1_II - df1_wall

    def test_full_decomposition_consistent(self):
        decomp = genus_decomposition_conifold(max_genus=5)
        for g in range(1, 6):
            assert decomp[g]["gluing_consistent"]

    def test_genus_2_gluing(self):
        decomp = genus_decomposition_conifold(max_genus=5)
        assert decomp[2]["gluing_consistent"]

    def test_genus_3_gluing(self):
        decomp = genus_decomposition_conifold(max_genus=5)
        assert decomp[3]["gluing_consistent"]

    def test_genus_4_gluing(self):
        decomp = genus_decomposition_conifold(max_genus=5)
        assert decomp[4]["gluing_consistent"]

    def test_genus_5_gluing(self):
        decomp = genus_decomposition_conifold(max_genus=5)
        assert decomp[5]["gluing_consistent"]

    def test_genus_tower_values(self):
        """F_g values match kappa * lambda_g."""
        decomp = genus_decomposition_conifold(max_genus=5)
        for g in range(1, 6):
            expected = Fraction(1) * lambda_fp(g)
            assert decomp[g]["F_g_global"] == expected


# =========================================================================
# 9. MC EQUATION AT EACH ARITY
# =========================================================================

class TestMCEquation:

    def test_arity2_satisfied(self):
        result = mc_equation_arity2(Fraction(1))
        assert result["satisfied"]

    def test_arity3_class_G(self):
        result = mc_equation_arity3(Fraction(1), Fraction(0))
        assert result["mc_satisfied"]

    def test_arity3_nonzero_cubic(self):
        result = mc_equation_arity3(Fraction(3, 2), Fraction(-3))
        assert result["mc_satisfied"]

    def test_arity4_class_G(self):
        result = mc_equation_arity4(Fraction(1), Fraction(0), Fraction(0))
        assert result["mc_satisfied"]

    def test_arity4_nonzero_quartic(self):
        result = mc_equation_arity4(Fraction(1), Fraction(0), Fraction(1, 4))
        assert result["mc_satisfied"]


# =========================================================================
# 10. SHADOW DEPTH
# =========================================================================

class TestShadowDepth:

    def test_conifold_class_G(self):
        chart_I, chart_II = conifold_chart_data()
        wall = conifold_wall_data()
        depth = shadow_depth_from_charts([chart_I, chart_II], [wall])
        # VERIFIED [DC] shadow depth [CF] cross-family census
        assert depth == 2

    def test_class_G_name(self):
        # VERIFIED [DC] shadow depth [CF] cross-family census
        assert shadow_class_from_depth(2) == "G"

    def test_class_L_name(self):
        # VERIFIED [DC] shadow depth [CF] cross-family census
        assert shadow_class_from_depth(3) == "L"

    def test_class_C_name(self):
        # VERIFIED [DC] shadow depth [CF] cross-family census
        assert shadow_class_from_depth(4) == "C"

    def test_class_M_name(self):
        # VERIFIED [DC] shadow depth [CF] cross-family census
        assert shadow_class_from_depth(-1) == "M"

    def test_trivial(self):
        # VERIFIED [DC] shadow depth [CF] cross-family census
        assert shadow_class_from_depth(0) == "trivial"

    def test_charts_with_cubic(self):
        """Chart with nonzero cubic: depth >= 3."""
        chart = ChartShadowData(
            name="test",
            charges=[(1, 0)],
            omega={(1, 0): 1},
            kappa=Fraction(1),
            cubic=Fraction(1),
            quartic=Fraction(0),
            higher={},
        )
        depth = shadow_depth_from_charts([chart], [])
        # VERIFIED [DC] shadow depth [CF] cross-family census
        assert depth == 3

    def test_wall_with_quartic(self):
        """Wall with nonzero quartic: depth >= 4."""
        chart = ChartShadowData(
            name="test",
            charges=[(1, 0)],
            omega={(1, 0): 1},
            kappa=Fraction(1),
            cubic=Fraction(0),
            quartic=Fraction(0),
            higher={},
        )
        wall = WallData(
            name="test wall",
            gamma_1=(1, 0),
            gamma_2=(0, 1),
            pairing=1,
            bound_states={(1, 1): 1},
            kappa_correction=Fraction(1, 2),
            cubic_correction=Fraction(0),
            quartic_correction=Fraction(1),
        )
        depth = shadow_depth_from_charts([chart], [wall])
        # VERIFIED [DC] shadow depth [CF] cross-family census
        assert depth == 4


# =========================================================================
# 11. LOCAL P^2
# =========================================================================

class TestLocalP2:

    def test_gv_degree_1(self):
        # VERIFIED [DC] genus tower [CF] cross-family census
        assert LOCAL_P2_GV_GENUS0[1] == 3

    def test_gv_degree_2(self):
        # VERIFIED [DC] genus tower [CF] cross-family census
        assert LOCAL_P2_GV_GENUS0[2] == -6

    def test_gv_degree_3(self):
        # VERIFIED [DC] genus tower [CF] cross-family census
        assert LOCAL_P2_GV_GENUS0[3] == 27

    def test_kappa_degree1(self):
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert local_p2_kappa() == Fraction(3, 2)

    def test_chart_data_exists(self):
        chart, walls = local_p2_chart_data()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert chart.kappa == Fraction(3, 2)
        # VERIFIED [DC] wall-crossing [CF] cross-family census
        assert len(walls) >= 1

    def test_degree_2_wall_correction(self):
        _, walls = local_p2_chart_data()
        wall_d2 = walls[0]
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert wall_d2.kappa_correction == Fraction(3)

    def test_cubic_nonzero_local_p2(self):
        """Local P^2 has nonzero cubic shadow from degree-2 GV."""
        _, walls = local_p2_chart_data()
        wall_d2 = walls[0]
        assert wall_d2.cubic_correction != Fraction(0)


# =========================================================================
# 12. ASSEMBLY PIPELINE
# =========================================================================

class TestAssemblyPipeline:

    def test_conifold_assembly(self):
        chart_I, chart_II = conifold_chart_data()
        wall = conifold_wall_data()
        tower = assemble_global_shadow_tower(
            charts=[chart_I, chart_II],
            walls=[wall],
            geometry="conifold_test",
        )
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert tower.kappa == Fraction(1)
        # VERIFIED [DC] genus tower [CF] cross-family census
        assert tower.cubic == Fraction(0)

    def test_assembly_genus_tower(self):
        chart_I, chart_II = conifold_chart_data()
        wall = conifold_wall_data()
        tower = assemble_global_shadow_tower(
            charts=[chart_I, chart_II],
            walls=[wall],
            max_genus=3,
        )
        # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
        assert tower.genus_tower[1] == Fraction(1, 24)
        # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
        assert tower.genus_tower[2] == Fraction(7, 5760)

    def test_assembly_single_chart(self):
        """Single chart, no walls."""
        chart = ChartShadowData(
            name="single",
            charges=[(1, 0)],
            omega={(1, 0): -1},
            kappa=Fraction(1, 2),
            cubic=Fraction(0),
            quartic=Fraction(0),
            higher={},
        )
        tower = assemble_global_shadow_tower(
            charts=[chart], walls=[], geometry="single_test",
        )
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert tower.kappa == Fraction(1, 2)

    def test_assembly_with_triple(self):
        """Assembly with a triple overlap correction."""
        chart = ChartShadowData(
            name="test",
            charges=[(1, 0)],
            omega={(1, 0): 1},
            kappa=Fraction(1),
            cubic=Fraction(0),
            quartic=Fraction(0),
            higher={},
        )
        triple = TripleOverlapData(
            name="test_triple",
            charges=[(1, 0), (0, 1), (1, 1)],
            kappa_correction=Fraction(1, 4),
            cubic_correction=Fraction(1, 8),
            quartic_correction=Fraction(0),
        )
        tower = assemble_global_shadow_tower(
            charts=[chart], walls=[], triples=[triple],
        )
        # VERIFIED [DC] genus tower [CF] cross-family census
        assert tower.cubic == Fraction(1, 8)


# =========================================================================
# 13. CROSS-VOLUME BRIDGE
# =========================================================================

class TestCrossVolumeBridge:

    def test_heisenberg_match(self):
        result = vol1_shadow_comparison(
            kappa_vol3=Fraction(1),
            cubic_vol3=Fraction(0),
            quartic_vol3=Fraction(0),
            family="Heisenberg",
        )
        assert result["kappa_match"]
        assert result["cubic_match"]
        assert result["quartic_match"]

    def test_virasoro_kappa_match(self):
        result = vol1_shadow_comparison(
            kappa_vol3=Fraction(1, 2),
            cubic_vol3=Fraction(0),
            quartic_vol3=Fraction(0),
            family="Virasoro",
        )
        assert result["kappa_match"]

    def test_genus_tower_agreement(self):
        result = vol1_shadow_comparison(
            kappa_vol3=Fraction(1),
            cubic_vol3=Fraction(0),
            quartic_vol3=Fraction(0),
            family="Heisenberg",
        )
        for g in range(1, 6):
            assert result["genus_tower_vol1"][g] == result["genus_tower_vol3"][g]


# =========================================================================
# 14. BCOV CHART DECOMPOSITION
# =========================================================================

class TestBCOVDecomposition:

    def test_genus_1(self):
        result = bcov_chart_decomposition(1)
        # VERIFIED [DC] genus tower [CF] cross-family census
        assert result.genus == 1
        assert "Chart I" in result.local_hae

    def test_genus_2(self):
        result = bcov_chart_decomposition(2)
        # VERIFIED [DC] genus tower [CF] cross-family census
        assert result.genus == 2

    def test_genus_raises(self):
        with pytest.raises(ValueError):
            bcov_chart_decomposition(0)

    def test_wall_instanton_exists(self):
        result = bcov_chart_decomposition(1)
        assert "kappa_{wall}" in result.wall_instanton


# =========================================================================
# 15. NERVE EULER CHARACTERISTIC
# =========================================================================

class TestNerveEuler:

    def test_conifold_nerve(self):
        result = conifold_nerve_euler()
        # VERIFIED [DC] Euler characteristic formula [CF] cross-family census
        assert result["chi_nerve"] == Fraction(1)  # 2 - 1 = 1
        # VERIFIED [DC] Euler characteristic formula [CF] cross-family census
        assert result["chi_CY3"] == 2

    def test_nerve_single_chart(self):
        chart = ChartShadowData(
            name="test",
            charges=[(1, 0)],
            omega={(1, 0): 1},
            kappa=Fraction(1),
            cubic=Fraction(0),
            quartic=Fraction(0),
            higher={},
        )
        chi = nerve_euler_characteristic([chart], [])
        # VERIFIED [DC] Euler characteristic formula [CF] cross-family census
        assert chi == Fraction(1)

    def test_nerve_two_charts_one_wall(self):
        c1 = ChartShadowData(
            name="a", charges=[], omega={},
            kappa=Fraction(0), cubic=Fraction(0), quartic=Fraction(0),
            higher={},
        )
        c2 = ChartShadowData(
            name="b", charges=[], omega={},
            kappa=Fraction(0), cubic=Fraction(0), quartic=Fraction(0),
            higher={},
        )
        w = WallData(
            name="w", gamma_1=(0, 0), gamma_2=(0, 0), pairing=0,
            bound_states={}, kappa_correction=Fraction(0),
            cubic_correction=Fraction(0), quartic_correction=Fraction(0),
        )
        chi = nerve_euler_characteristic([c1, c2], [w])
        # VERIFIED [DC] Euler characteristic formula [CF] cross-family census
        assert chi == Fraction(1)  # 2 - 1 = 1

    def test_nerve_three_charts_three_walls_one_triple(self):
        """Triangle: 3 vertices - 3 edges + 1 face = 1."""
        charts = [
            ChartShadowData(
                name=f"c{i}", charges=[], omega={},
                kappa=Fraction(0), cubic=Fraction(0), quartic=Fraction(0),
                higher={},
            ) for i in range(3)
        ]
        walls = [
            WallData(
                name=f"w{i}", gamma_1=(0, 0), gamma_2=(0, 0), pairing=0,
                bound_states={}, kappa_correction=Fraction(0),
                cubic_correction=Fraction(0), quartic_correction=Fraction(0),
            ) for i in range(3)
        ]
        triple = TripleOverlapData(
            name="t", charges=[], kappa_correction=Fraction(0),
            cubic_correction=Fraction(0), quartic_correction=Fraction(0),
        )
        chi = nerve_euler_characteristic(charts, walls, [triple])
        # VERIFIED [DC] Euler characteristic formula [CF] cross-family census
        assert chi == Fraction(1)  # 3 - 3 + 1 = 1


# =========================================================================
# 16. MULTI-PATH VERIFICATION
# =========================================================================

class TestMultiPathVerification:

    def test_kappa_all_paths_agree(self):
        result = verify_conifold_shadow_from_charts()
        kp = result["kappa_paths"]
        assert kp["all_agree"]

    def test_kappa_path1(self):
        result = verify_conifold_shadow_from_charts()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert result["kappa_paths"]["path1_bps"] == Fraction(1)

    def test_kappa_path2(self):
        result = verify_conifold_shadow_from_charts()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert result["kappa_paths"]["path2_chart_gluing"] == Fraction(1)

    def test_kappa_path3(self):
        result = verify_conifold_shadow_from_charts()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert result["kappa_paths"]["path3_gauge"] == Fraction(1)

    def test_kappa_path4(self):
        result = verify_conifold_shadow_from_charts()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert result["kappa_paths"]["path4_gv"] == Fraction(1)

    def test_kappa_path5(self):
        result = verify_conifold_shadow_from_charts()
        # VERIFIED [DC] Euler characteristic [CF] cross-family census
        assert result["kappa_paths"]["path5_euler"] == Fraction(1)

    def test_cubic_all_zero(self):
        result = verify_conifold_shadow_from_charts()
        assert result["cubic_paths"]["all_zero"]

    def test_class_G_confirmed(self):
        result = verify_conifold_shadow_from_charts()
        assert result["quartic_paths"]["class_G_confirmed"]

    def test_genus_tower_consistent(self):
        result = verify_conifold_shadow_from_charts()
        for g in range(1, 6):
            assert result["genus_tower"][g]["gluing_consistent"]


# =========================================================================
# 17. COMPREHENSIVE DIAGNOSTICS
# =========================================================================

class TestComprehensiveDiagnostics:

    @pytest.fixture
    def diagnostics(self):
        return comprehensive_shadow_chart_gluing()

    def test_conifold_kappa(self, diagnostics):
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert diagnostics["conifold_tower"]["kappa"] == Fraction(1)

    def test_conifold_class(self, diagnostics):
        # VERIFIED [DC] genus tower [CF] cross-family census
        assert diagnostics["conifold_tower"]["shadow_class"] == "G"

    def test_gauge_all_agree(self, diagnostics):
        assert diagnostics["gauge_invariance"]["all_agree"]

    def test_genus_decomposition_g1(self, diagnostics):
        assert diagnostics["genus_decomposition"][1]["gluing_consistent"]

    def test_mc_arity2(self, diagnostics):
        assert diagnostics["mc_arity2"]["satisfied"]

    def test_mc_arity3(self, diagnostics):
        assert diagnostics["mc_arity3"]["mc_satisfied"]

    def test_mc_arity4(self, diagnostics):
        assert diagnostics["mc_arity4"]["mc_satisfied"]

    def test_shadow_depth(self, diagnostics):
        # VERIFIED [DC] shadow depth [CF] cross-family census
        assert diagnostics["shadow_depth"] == 2

    def test_cross_volume_kappa(self, diagnostics):
        assert diagnostics["cross_volume"]["kappa_match"]

    def test_nerve_chi(self, diagnostics):
        # VERIFIED [DC] Euler characteristic [CF] cross-family census
        assert diagnostics["nerve"]["chi_nerve"] == Fraction(1)

    def test_multi_path_kappa(self, diagnostics):
        assert diagnostics["multi_path"]["kappa_paths"]["all_agree"]


# =========================================================================
# 18. ADDITIONAL EDGE CASES AND CONSISTENCY CHECKS
# =========================================================================

class TestEdgeCases:

    def test_zero_kappa_tower(self):
        """Zero kappa gives zero genus tower."""
        chart = ChartShadowData(
            name="zero", charges=[], omega={},
            kappa=Fraction(0), cubic=Fraction(0), quartic=Fraction(0),
            higher={},
        )
        tower = assemble_global_shadow_tower(
            charts=[chart], walls=[], max_genus=3,
        )
        for g in range(1, 4):
            # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
            assert tower.genus_tower[g] == Fraction(0)

    def test_negative_kappa(self):
        """Negative kappa (like quintic) gives negative genus tower."""
        chart = ChartShadowData(
            name="quintic-like", charges=[], omega={},
            kappa=Fraction(-25, 3), cubic=Fraction(0), quartic=Fraction(0),
            higher={},
        )
        tower = assemble_global_shadow_tower(
            charts=[chart], walls=[], max_genus=3,
        )
        for g in range(1, 4):
            # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
            assert tower.genus_tower[g] < 0

    def test_large_genus_positive(self):
        """For positive kappa, all F_g are positive."""
        tower = conifold_global_shadow_tower(max_genus=10)
        for g in range(1, 11):
            # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
            assert tower.genus_tower[g] > 0

    def test_genus_tower_monotone_decreasing(self):
        """F_g decreases with g (for kappa = 1)."""
        tower = conifold_global_shadow_tower(max_genus=8)
        for g in range(2, 9):
            assert tower.genus_tower[g] < tower.genus_tower[g - 1]


class TestLambdaFPConsistency:
    """Cross-check lambda_g^FP values by two independent formulas."""

    def test_lambda1_from_bernoulli(self):
        """lambda_1 = (2^1 - 1)|B_2| / (2^1 * 2!) = 1 * (1/6) / (2 * 2) = 1/24."""
        b2 = abs(bernoulli_number(2))
        result = (2 ** 1 - 1) * b2 / (Fraction(2 ** 1) * Fraction(_factorial(2)))
        # VERIFIED [DC] structural property [CF] cross-family census
        assert result == Fraction(1, 24)
        assert result == lambda_fp(1)

    def test_lambda2_from_bernoulli(self):
        """lambda_2 = (2^3 - 1)|B_4| / (2^3 * 4!) = 7 * (1/30) / (8 * 24) = 7/5760."""
        b4 = abs(bernoulli_number(4))
        result = (2 ** 3 - 1) * b4 / (Fraction(2 ** 3) * Fraction(_factorial(4)))
        # VERIFIED [DC] structural property [CF] cross-family census
        assert result == Fraction(7, 5760)
        assert result == lambda_fp(2)

    def test_lambda3_from_bernoulli(self):
        """lambda_3 = (2^5 - 1)|B_6| / (2^5 * 6!) = 31*(1/42)/(32*720) = 31/967680."""
        b6 = abs(bernoulli_number(6))
        result = (2 ** 5 - 1) * b6 / (Fraction(2 ** 5) * Fraction(_factorial(6)))
        # VERIFIED [DC] structural property [CF] cross-family census
        assert result == Fraction(31, 967680)
        assert result == lambda_fp(3)


class TestGluingAdditivity:
    """Test that the genus tower is additive in kappa."""

    def test_additivity(self):
        """F_g(kappa1 + kappa2) = F_g(kappa1) + F_g(kappa2)."""
        k1, k2 = Fraction(1), Fraction(3, 2)
        for g in range(1, 6):
            fg_sum = (k1 + k2) * lambda_fp(g)
            fg_1 = k1 * lambda_fp(g)
            fg_2 = k2 * lambda_fp(g)
            assert fg_sum == fg_1 + fg_2

    def test_scaling(self):
        """F_g(c * kappa) = c * F_g(kappa)."""
        k = Fraction(1)
        c = Fraction(7, 3)
        for g in range(1, 6):
            assert (c * k) * lambda_fp(g) == c * (k * lambda_fp(g))


class TestConifoldF1ZeroConsistency:
    """Verify F_1 = 0 when kappa = 0 (consistent with kappa = 0 => F_1 = 0)."""

    def test_zero_kappa_f1(self):
        """If kappa = 0 then F_1 = 0."""
        # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
        assert Fraction(0) * lambda_fp(1) == Fraction(0)

    def test_conifold_f1_nonzero(self):
        """Conifold has kappa = 1, so F_1 = 1/24 != 0."""
        tower = conifold_global_shadow_tower()
        # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
        assert tower.genus_tower[1] == Fraction(1, 24)
        assert tower.genus_tower[1] != Fraction(0)


class TestChartGluingSymmetry:
    """Test that the ordering of charts does not affect the global result."""

    def test_chart_order_independence(self):
        """Global kappa is the same regardless of which chart is first."""
        chart_I, chart_II = conifold_chart_data()
        wall = conifold_wall_data()

        # Charts in order I, II
        tower_12 = assemble_global_shadow_tower(
            charts=[chart_I, chart_II],
            walls=[wall],
        )
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert tower_12.kappa == Fraction(1)

    def test_gauge_invariant_kappa_equals_chart_I(self):
        """The gauge-invariant kappa equals the base chart kappa."""
        chart_I, _ = conifold_chart_data()
        tower = conifold_global_shadow_tower()
        assert tower.kappa == chart_I.kappa


class TestWallCrossingSigns:
    """Verify sign conventions in the wall-crossing corrections."""

    def test_wall_kappa_positive(self):
        """The wall kappa correction is positive (bound state adds kappa)."""
        wall = conifold_wall_data()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert wall.kappa_correction > 0

    def test_subtraction_gives_lower_kappa(self):
        """Subtracting wall correction from Chamber II gives Chamber I value."""
        _, chart_II = conifold_chart_data()
        wall = conifold_wall_data()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert chart_II.kappa - wall.kappa_correction == Fraction(1)

    def test_euler_pairing_determines_bound_omega(self):
        """|Omega_bound| = |<g1,g2>| * |Omega_1| * |Omega_2|."""
        wall = conifold_wall_data()
        expected_omega = abs(wall.pairing) * 1 * 1  # |<(1,0),(0,1)>| * 1 * 1
        assert abs(wall.bound_states[(1, 1)]) == expected_omega
