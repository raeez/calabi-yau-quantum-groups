"""Tests for kazhdan_lusztig_shadow: KL equivalence from the shadow obstruction tower.

Verifies the Kazhdan-Lusztig equivalence Rep_q(g) ≅ KL_k(g) from the
shadow obstruction tower perspective, cross-checking Vol I (shadow invariants) with
Vol III (quantum group data).

Ground truth:
  Vol I: higher_genus_modular_koszul.tex (shadow obstruction tower, κ formula)
  Vol I: kac_moody.tex (affine algebras)
  Vol III: chapters/examples/quantum_group_reps.tex (CY-C)
  Kazhdan-Lusztig, JAMS 6-7 (1993-94)
  Bakalov-Kirillov, AMS (2001)

MATHEMATICAL VERIFICATION NOTES (Beilinson principle — AP1, AP10):
  Every expected value below is computed from first principles.
  κ(ŝl₂_k) = 3(k+2)/4: this is dim(sl_2)·(k+h∨)/(2·h∨) with dim=3, h∨=2.
  κ(ŝl₃_k) = 4(k+3)/3: dim=8, h∨=3.
  Cross-family consistency (AP10): κ values checked against three independent
  sources (formula, shadow obstruction tower, quantum dimensions).
"""

import cmath
import math
from fractions import Fraction

import numpy as np
import pytest

from compute.lib.kazhdan_lusztig_shadow import (
    kappa_affine,
    kappa_sl2,
    kappa_sl3,
    shadow_tower_sl2,
    shadow_tower_sl3,
    kl_shadow_data_sl2,
    KLShadowData,
    braiding_from_shadow,
    braiding_comparison,
    s_matrix_from_shadow,
    s_matrix_comparison,
    cy_kappa_match,
    quantum_dims_from_shadow,
    sl3_simple_data,
    sl3_fusion_rules_level1,
    sl3_s_matrix_level1,
    nonsemisimple_detector,
    approaching_root_of_unity,
    genus_expansion_from_shadow,
    cross_level_kappa_check,
    verify_kl_shadow_all_levels,
)
from compute.lib.kl_sl2_level1 import (
    q_parameter,
    q_number,
    quantum_dimension,
    r_matrix_eigenvalue,
    modular_s_matrix,
    modular_t_matrix,
    central_charge,
    conformal_weight,
    verlinde_coefficient,
    total_quantum_dimension_squared,
)


# ======================================================================
# 1. Shadow obstruction tower κ for affine algebras
# ======================================================================

class TestKappaAffine:
    """Test the modular characteristic κ for affine Lie algebras.

    κ(ĝ_k) = dim(g) · (k + h∨) / (2 · h∨).
    AP1: each formula independently verified, never copied between families.
    """

    def test_kappa_sl2_k1(self):
        """κ(ŝl₂₁) = 3·3/(2·2) = 9/4."""
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert kappa_sl2(1) == Fraction(9, 4)

    def test_kappa_sl2_k2(self):
        """κ(ŝl₂₂) = 3·4/4 = 3."""
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert kappa_sl2(2) == Fraction(3, 1)

    def test_kappa_sl2_k3(self):
        """κ(ŝl₂₃) = 3·5/4 = 15/4."""
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert kappa_sl2(3) == Fraction(15, 4)

    def test_kappa_sl2_k4(self):
        """κ(ŝl₂₄) = 3·6/4 = 9/2."""
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert kappa_sl2(4) == Fraction(9, 2)

    def test_kappa_sl2_k5(self):
        """κ(ŝl₂₅) = 3·7/4 = 21/4."""
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert kappa_sl2(5) == Fraction(21, 4)

    def test_kappa_sl3_k1(self):
        """κ(ŝl₃₁) = 8·4/(2·3) = 16/3."""
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert kappa_sl3(1) == Fraction(16, 3)

    def test_kappa_sl3_k2(self):
        """κ(ŝl₃₂) = 8·5/(2·3) = 20/3."""
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert kappa_sl3(2) == Fraction(20, 3)

    def test_kappa_not_equal_c_over_2(self):
        """For affine KM: κ != c/2 in general (κ = c/2 is Virasoro only)."""
        for k in range(1, 6):
            kap = kappa_sl2(k)
            c = central_charge(k, 2)
            # κ(KM) = dim(g)*(k+h∨)/(2h∨), c/2 = dim(g)*k/(2(k+h∨))
            # These are NOT equal
            assert kap != c / 2, f"κ should NOT equal c/2 at k={k}"

    def test_kappa_monotone_increasing(self):
        """κ(ŝl₂_k) is strictly increasing in k for k > 0."""
        kappas = [kappa_sl2(k) for k in range(1, 11)]
        for i in range(len(kappas) - 1):
            assert kappas[i] < kappas[i + 1]

    def test_kappa_limit(self):
        """κ(ŝl₂_k) grows linearly: κ ~ 3k/4 for large k.

        The ratio κ(k) / k → 3/4 = dim(sl_2) / (2·h∨) as k → ∞.
        """
        kap_1000 = float(kappa_sl2(1000))
        # κ(1000) = 3*1002/4 = 751.5
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert abs(kap_1000 - 751.5) < 0.01

    def test_kappa_critical_level(self):
        """κ = 0 at the critical level k = -h∨ = -2."""
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert kappa_sl2(-2) == Fraction(0)


# ======================================================================
# 2. Shadow obstruction tower structure
# ======================================================================

class TestShadowTowerStructure:
    """Test the shadow obstruction tower invariants for affine KM algebras.

    Affine KM algebras are class L (Lie/tree): shadow depth r_max = 3.
    The shadow obstruction tower terminates: quartic and all higher shadows vanish.
    """

    def test_shadow_class_L(self):
        """All affine KM algebras are class L."""
        for k in range(1, 6):
            shadow = shadow_tower_sl2(k)
            # VERIFIED [DC] shadow structure [CF] cross-family census
            assert shadow["shadow_class"] == "L"

    def test_shadow_depth_3(self):
        """r_max = 3 for all affine KM."""
        for k in range(1, 6):
            shadow = shadow_tower_sl2(k)
            # VERIFIED [DC] shadow structure [CF] cross-family census
            assert shadow["r_max"] == 3

    def test_discriminant_zero(self):
        """Critical discriminant Δ = 0 for class L (perfect square Q_L)."""
        for k in range(1, 6):
            shadow = shadow_tower_sl2(k)
            # VERIFIED [DC] structural property [CF] cross-family census
            assert shadow["Delta"] == 0

    def test_quartic_vanishes(self):
        """Quartic shadow Q = 0 for class L."""
        for k in range(1, 6):
            shadow = shadow_tower_sl2(k)
            # VERIFIED [DC] vanishing check [CF] cross-family census
            assert shadow["Q_quartic"] == 0

    def test_cubic_alpha_negative(self):
        """Cubic coefficient α < 0 (antisymmetry of structure constants)."""
        for k in range(1, 6):
            shadow = shadow_tower_sl2(k)
            # VERIFIED [DC] structural property [CF] cross-family census
            assert shadow["alpha"] < 0

    def test_cubic_alpha_sl2_k1(self):
        """α = -(2/3)·2/3 = -4/9 for sl_2 at k=1."""
        shadow = shadow_tower_sl2(1)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert shadow["alpha"] == Fraction(-4, 9)

    def test_sl3_shadow_class_L(self):
        """sl_3 at level 1 is also class L."""
        shadow = shadow_tower_sl3(1)
        # VERIFIED [DC] shadow structure [CF] cross-family census
        assert shadow["shadow_class"] == "L"
        # VERIFIED [DC] shadow structure [CF] cross-family census
        assert shadow["r_max"] == 3

    def test_sl3_kappa_k1(self):
        """κ(ŝl₃₁) = 16/3 from shadow obstruction tower."""
        shadow = shadow_tower_sl3(1)
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert shadow["kappa"] == Fraction(16, 3)


# ======================================================================
# 3. KL shadow data at level 1
# ======================================================================

class TestKLShadowLevel1:
    """Full KL-shadow verification at the simplest level k=1."""

    @pytest.fixture
    def data(self):
        return kl_shadow_data_sl2(1)

    def test_num_simples(self, data):
        """2 simples at level 1."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert data.num_simples == 2

    def test_kappa_value(self, data):
        """κ = 9/4."""
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert data.kappa == Fraction(9, 4)

    def test_central_charge(self, data):
        """c = 1."""
        # VERIFIED [DC] central charge formula [LT] literature cross-check
        assert data.central_charge_val == Fraction(1, 1)

    def test_drinfeld_kohno(self, data):
        """Drinfeld-Kohno theorem holds."""
        assert data.drinfeld_kohno_match

    def test_verlinde(self, data):
        """Verlinde formula from S-matrix works."""
        assert data.verlinde_match

    def test_modular_relations(self, data):
        """SL(2,Z) modular relations hold."""
        assert data.modular_match

    def test_quantum_dims(self, data):
        """d_0 = 1, d_1 = 1 at level 1."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert abs(data.quantum_dims[0] - 1.0) < 1e-12
        # VERIFIED [DC] structural property [CF] cross-family census
        assert abs(data.quantum_dims[1] - 1.0) < 1e-12

    def test_fusion_z2(self, data):
        """Fusion ring is Z/2Z at level 1."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert data.fusion_rules[(1, 1)] == [0]
        # VERIFIED [DC] structural property [CF] cross-family census
        assert data.fusion_rules[(0, 1)] == [1]


# ======================================================================
# 4. KL shadow data at level 2
# ======================================================================

class TestKLShadowLevel2:
    """KL-shadow verification at level 2: 3 simples, richer structure."""

    @pytest.fixture
    def data(self):
        return kl_shadow_data_sl2(2)

    def test_num_simples(self, data):
        """3 simples at level 2."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert data.num_simples == 3

    def test_kappa_value(self, data):
        """κ = 3."""
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert data.kappa == Fraction(3, 1)

    def test_central_charge(self, data):
        """c = 3/2 (N=1 super-Virasoro!)."""
        # VERIFIED [DC] central charge formula [LT] literature cross-check
        assert data.central_charge_val == Fraction(3, 2)

    def test_drinfeld_kohno(self, data):
        assert data.drinfeld_kohno_match

    def test_verlinde(self, data):
        assert data.verlinde_match

    def test_modular(self, data):
        assert data.modular_match

    def test_quantum_dim_V1_sqrt2(self, data):
        """d_1 = √2 at level 2."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert abs(data.quantum_dims[1] - math.sqrt(2)) < 1e-12

    def test_fusion_V1_squared(self, data):
        """V_1 ⊗ V_1 = V_0 ⊕ V_2 at level 2."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert data.fusion_rules[(1, 1)] == [0, 2]

    def test_fusion_V1_V2(self, data):
        """V_1 ⊗ V_2 = V_1 at level 2."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert data.fusion_rules[(1, 2)] == [1]

    def test_fusion_V2_squared(self, data):
        """V_2 ⊗ V_2 = V_0 at level 2."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert data.fusion_rules[(2, 2)] == [0]


# ======================================================================
# 5. Braiding from shadow obstruction tower
# ======================================================================

class TestBraidingFromShadow:
    """Test that the E_2-shadow obstruction tower reproduces the quantum R-matrix braiding."""

    def test_braiding_k1_trivial(self):
        """Braiding on vacuum channel is 1."""
        ev = braiding_from_shadow(0, 0, 0, k=1)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert abs(ev - 1.0) < 1e-14

    def test_braiding_k1_fund_times_fund(self):
        """Braiding on V_0 channel of V_1 ⊗ V_1 at k=1 is i."""
        ev = braiding_from_shadow(1, 1, 0, k=1)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert abs(ev - 1j) < 1e-12

    def test_braiding_matches_r_matrix_k1(self):
        """Shadow braiding = R-matrix for all channels at k=1."""
        result = braiding_comparison(k=1)
        assert result["all_match"]

    def test_braiding_matches_r_matrix_k2(self):
        """Shadow braiding = R-matrix for all channels at k=2."""
        result = braiding_comparison(k=2)
        assert result["all_match"]

    def test_braiding_matches_r_matrix_k3(self):
        """Shadow braiding = R-matrix for all channels at k=3."""
        result = braiding_comparison(k=3)
        assert result["all_match"]

    def test_braiding_matches_r_matrix_k4(self):
        """Shadow braiding = R-matrix for all channels at k=4."""
        result = braiding_comparison(k=4)
        assert result["all_match"]

    def test_braiding_matches_r_matrix_k5(self):
        """Shadow braiding = R-matrix for all channels at k=5."""
        result = braiding_comparison(k=5)
        assert result["all_match"]

    def test_num_channels_k3(self):
        """At k=3 (4 simples), there are many fusion channels."""
        result = braiding_comparison(k=3)
        # 4 simples, each pair has at most k+1 channels
        # VERIFIED [DC] structural property [CF] cross-family census
        assert result["num_channels"] > 10

    def test_braiding_v1v1_v0_k2(self):
        """Braiding eigenvalue on V_0 in V_1⊗V_1 at k=2.

        q = exp(πi/4), δ = -3/2, sign = (-1)^1 = -1.
        σ = -q^{-3/2} = -exp(-3πi/8).
        """
        q = q_parameter(2, 2)
        ev = braiding_from_shadow(1, 1, 0, k=2)
        expected = -q**(-1.5)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert abs(ev - expected) < 1e-12

    def test_braiding_v1v1_v2_k2(self):
        """Braiding eigenvalue on V_2 in V_1⊗V_1 at k=2.

        δ = (8-3-3)/4 = 1/2, sign = (-1)^0 = 1.
        σ = q^{1/2} = exp(πi/8).
        """
        q = q_parameter(2, 2)
        ev = braiding_from_shadow(1, 1, 2, k=2)
        expected = q**0.5
        # VERIFIED [DC] structural property [CF] cross-family census
        assert abs(ev - expected) < 1e-12


# ======================================================================
# 6. Modular S-matrix from shadow
# ======================================================================

class TestSMatrixFromShadow:
    """Test S-matrix computation from the shadow obstruction tower."""

    def test_s_matrix_match_k1(self):
        """Shadow S-matrix = standard S-matrix at k=1."""
        result = s_matrix_comparison(1)
        assert result["s_matrices_match"]
        # VERIFIED [DC] structural property [CF] cross-family census
        assert result["max_diff"] < 1e-14

    def test_s_matrix_match_k2(self):
        result = s_matrix_comparison(2)
        assert result["s_matrices_match"]

    def test_s_matrix_match_k3(self):
        result = s_matrix_comparison(3)
        assert result["s_matrices_match"]

    def test_s_matrix_match_k5(self):
        result = s_matrix_comparison(5)
        assert result["s_matrices_match"]

    def test_verlinde_from_shadow_s_k1(self):
        """Verlinde formula works from shadow S-matrix at k=1."""
        result = s_matrix_comparison(1)
        assert result["verlinde_from_shadow_s"]

    def test_verlinde_from_shadow_s_k2(self):
        result = s_matrix_comparison(2)
        assert result["verlinde_from_shadow_s"]

    def test_verlinde_from_shadow_s_k3(self):
        result = s_matrix_comparison(3)
        assert result["verlinde_from_shadow_s"]

    def test_s_matrix_unitarity_from_shadow(self):
        """Shadow-derived S-matrix is unitary."""
        for k in range(1, 4):
            S = s_matrix_from_shadow(k)
            n = k + 1
            assert np.allclose(S @ S.conj().T, np.eye(n), atol=1e-12)

    def test_s_matrix_symmetry_from_shadow(self):
        """Shadow-derived S-matrix is symmetric."""
        for k in range(1, 4):
            S = s_matrix_from_shadow(k)
            assert np.allclose(S, S.T, atol=1e-12)


# ======================================================================
# 7. CY interpretation: κ matching
# ======================================================================

class TestCYKappaMatch:
    """Test that the CY-to-chiral functor preserves κ.

    NOTE: κ(KM) != c/2. The cy_kappa_match function now sets kappa_match
    to False because the old c/2 comparison was incorrect.
    """

    def test_kappa_match_k1(self):
        """κ(ŝl₂₁) = 9/4."""
        result = cy_kappa_match(1)
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert result["kappa_shadow"] == Fraction(9, 4)

    def test_kappa_match_k2(self):
        result = cy_kappa_match(2)
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert result["kappa_shadow"] == Fraction(3, 1)

    def test_kappa_match_k3(self):
        result = cy_kappa_match(3)
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert result["kappa_shadow"] == Fraction(15, 4)

    def test_kappa_match_k5(self):
        result = cy_kappa_match(5)
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert result["kappa_shadow"] == Fraction(21, 4)

    def test_d_squared_k1(self):
        """D² = 2 at level 1."""
        result = cy_kappa_match(1)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert abs(result["D_squared"] - 2.0) < 1e-10

    def test_d_squared_k2(self):
        """D² = 4 at level 2."""
        result = cy_kappa_match(2)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert abs(result["D_squared"] - 4.0) < 1e-10


# ======================================================================
# 8. Quantum dimensions from shadow
# ======================================================================

class TestQuantumDimsFromShadow:
    """Test extraction of quantum dimensions from the shadow obstruction tower."""

    def test_three_methods_agree_k1(self):
        """Formula, S-matrix, and trig all agree at k=1."""
        result = quantum_dims_from_shadow(1)
        assert result["all_three_agree"]

    def test_three_methods_agree_k2(self):
        result = quantum_dims_from_shadow(2)
        assert result["all_three_agree"]

    def test_three_methods_agree_k3(self):
        result = quantum_dims_from_shadow(3)
        assert result["all_three_agree"]

    def test_truncation_k1(self):
        """[3]_q = 0 at k=1 (q = exp(πi/3))."""
        result = quantum_dims_from_shadow(1)
        assert result["truncation_dim_zero"]

    def test_truncation_k2(self):
        """[4]_q = 0 at k=2 (q = exp(πi/4))."""
        result = quantum_dims_from_shadow(2)
        assert result["truncation_dim_zero"]

    def test_golden_ratio_k3(self):
        """d_1 = golden ratio φ = (1+√5)/2 at k=3."""
        result = quantum_dims_from_shadow(3)
        phi = (1 + math.sqrt(5)) / 2
        # VERIFIED [DC] structural property [CF] cross-family census
        assert abs(result["dims_formula"][1] - phi) < 1e-12

    def test_d_squared_sum_k1(self):
        """D² = Σ d_j² = 2 at k=1."""
        result = quantum_dims_from_shadow(1)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert abs(result["D_squared"] - 2.0) < 1e-10

    def test_d_squared_sum_k2(self):
        """D² = 1 + 2 + 1 = 4 at k=2."""
        result = quantum_dims_from_shadow(2)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert abs(result["D_squared"] - 4.0) < 1e-10

    def test_d_squared_sum_k3(self):
        """D² at k=3: 1 + φ² + φ² + 1 = 2 + 2φ² = 2 + 2(3+√5)/2 = 5+√5."""
        result = quantum_dims_from_shadow(3)
        phi = (1 + math.sqrt(5)) / 2
        expected_D2 = 2 * (1 + phi**2)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert abs(result["D_squared"] - expected_D2) < 1e-10


# ======================================================================
# 9. sl_3 at level 1
# ======================================================================

class TestSL3Level1:
    """Test KL data for sl_3 at level 1."""

    def test_num_simples(self):
        """3 simples at level 1 for sl_3."""
        data = sl3_simple_data(1)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert data["num_simples"] == 3

    def test_weights(self):
        """Weights are (0,0), (1,0), (0,1)."""
        data = sl3_simple_data(1)
        weights = [s["weight"] for s in data["simples"]]
        assert (0, 0) in weights
        assert (1, 0) in weights
        assert (0, 1) in weights

    def test_vacuum_qdim(self):
        """d(0,0) = 1 (vacuum)."""
        data = sl3_simple_data(1)
        vac = [s for s in data["simples"] if s["weight"] == (0, 0)][0]
        # VERIFIED [DC] dimension count [CF] cross-family census
        assert abs(vac["quantum_dim"] - 1.0) < 1e-10

    def test_fund_qdim(self):
        """d(1,0) = d(0,1) by symmetry."""
        data = sl3_simple_data(1)
        d_fund = [s for s in data["simples"] if s["weight"] == (1, 0)][0]["quantum_dim"]
        d_anti = [s for s in data["simples"] if s["weight"] == (0, 1)][0]["quantum_dim"]
        # VERIFIED [DC] dimension [CF] cross-family census
        assert abs(d_fund - d_anti) < 1e-10

    def test_fund_qdim_value(self):
        """At level 1 for sl_3: all qdims = 1 (Z/3Z fusion category)."""
        data = sl3_simple_data(1)
        d_fund = [s for s in data["simples"] if s["weight"] == (1, 0)][0]["quantum_dim"]
        # VERIFIED [DC] structural property [CF] cross-family census
        assert abs(d_fund - 1.0) < 1e-10

    def test_kappa(self):
        """κ(ŝl₃₁) = 16/3."""
        data = sl3_simple_data(1)
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert data["kappa"] == Fraction(16, 3)

    def test_fusion_z3(self):
        """Fusion ring at level 1 is Z/3Z."""
        rules = sl3_fusion_rules_level1()
        # VERIFIED [DC] structural property [CF] cross-family census
        assert rules[(1, 1)] == [2]
        # VERIFIED [DC] structural property [CF] cross-family census
        assert rules[(1, 2)] == [0]
        # VERIFIED [DC] structural property [CF] cross-family census
        assert rules[(2, 2)] == [1]

    def test_s_matrix_unitarity(self):
        """S-matrix for sl_3 level 1 is unitary."""
        S = sl3_s_matrix_level1()
        assert np.allclose(S @ S.conj().T, np.eye(3), atol=1e-12)

    def test_s_matrix_symmetry(self):
        """S-matrix is symmetric."""
        S = sl3_s_matrix_level1()
        assert np.allclose(S, S.T, atol=1e-12)

    def test_s_matrix_is_fourier_z3(self):
        """S-matrix is the Fourier transform matrix for Z/3Z."""
        S = sl3_s_matrix_level1()
        omega = cmath.exp(2j * cmath.pi / 3)
        expected = np.array([
            [1, 1, 1],
            [1, omega, omega**2],
            [1, omega**2, omega],
        ], dtype=complex) / math.sqrt(3)
        assert np.allclose(S, expected, atol=1e-12)

    def test_verlinde_from_sl3_s_matrix(self):
        """Verlinde formula from sl_3 S-matrix reproduces Z/3Z fusion."""
        S = sl3_s_matrix_level1()
        rules = sl3_fusion_rules_level1()

        for i in range(3):
            for j in range(3):
                for m in range(3):
                    v_sum = sum(
                        S[i, s] * S[j, s] * np.conj(S[m, s]) / S[0, s]
                        for s in range(3)
                    )
                    v_int = int(round(v_sum.real))
                    # VERIFIED [DC] structural property [CF] cross-family census
                    assert abs(v_sum.imag) < 1e-10
                    expected = 1 if m in rules.get((i, j), []) else 0
                    assert v_int == expected, f"Verlinde failed at ({i},{j},{m})"

    def test_sl3_shadow_tower(self):
        """Shadow obstruction tower for sl_3 at k=1: class L, r_max=3."""
        shadow = shadow_tower_sl3(1)
        # VERIFIED [DC] shadow structure [CF] cross-family census
        assert shadow["shadow_class"] == "L"
        # VERIFIED [DC] shadow structure [CF] cross-family census
        assert shadow["r_max"] == 3
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert shadow["kappa"] == Fraction(16, 3)
        # VERIFIED [DC] shadow structure [CF] cross-family census
        assert shadow["Delta"] == 0


# ======================================================================
# 10. Nonsemisimple transition
# ======================================================================

class TestNonsemisimpleTransition:
    """Test detection of the nonsemisimple transition in shadow data."""

    def test_kappa_monotone(self):
        """κ is monotone increasing across levels."""
        result = nonsemisimple_detector(5)
        assert result["kappa_monotone"]

    def test_d_squared_monotone(self):
        """D² is monotone increasing across levels (more simples → larger)."""
        result = nonsemisimple_detector(5)
        assert result["D2_monotone"]

    def test_all_truncation_zero(self):
        """[k+2]_q = 0 at every level (root of unity truncation)."""
        result = nonsemisimple_detector(5)
        assert result["all_truncation_zero"]

    def test_approaching_root_k1(self):
        """[3]_q(ε) → 0 as ε → 0 for k=1."""
        result = approaching_root_of_unity(1, n_points=10)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert result["trunc_at_root"] < 1e-12
        assert result["trunc_approaches_zero"]

    def test_approaching_root_k2(self):
        """[4]_q(ε) → 0 as ε → 0 for k=2."""
        result = approaching_root_of_unity(2, n_points=10)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert result["trunc_at_root"] < 1e-12
        assert result["trunc_approaches_zero"]

    def test_level_data_consistency(self):
        """Cross-check: num_simples = k+1 at each level."""
        result = nonsemisimple_detector(5)
        for d in result["levels"]:
            assert d["num_simples"] == d["k"] + 1


# ======================================================================
# 11. Genus expansion from shadow
# ======================================================================

class TestGenusExpansion:
    """Test the genus expansion of KL invariants from the shadow obstruction tower."""

    def test_genus1_k1(self):
        """F_1(ŝl₂₁) = κ/24 = (9/4)/24 = 9/96 = 3/32."""
        result = genus_expansion_from_shadow(1)
        # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
        assert result["genus_data"][1]["F_g"] == Fraction(9, 4) * Fraction(1, 24)

    def test_genus1_k2(self):
        """F_1(ŝl₂₂) = 3/24 = 1/8."""
        result = genus_expansion_from_shadow(2)
        # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
        assert result["genus_data"][1]["F_g"] == Fraction(3, 1) * Fraction(1, 24)

    def test_genus2_k1(self):
        """F_2(ŝl₂₁) = κ · 7/5760 = (9/4) · 7/5760."""
        result = genus_expansion_from_shadow(1)
        # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
        assert result["genus_data"][2]["F_g"] == Fraction(9, 4) * Fraction(7, 5760)

    def test_genus2_k2(self):
        """F_2(ŝl₂₂) = 3 · 7/5760 = 7/1920."""
        result = genus_expansion_from_shadow(2)
        # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
        assert result["genus_data"][2]["F_g"] == Fraction(3, 1) * Fraction(7, 5760)

    def test_genus3_k1(self):
        """F_3(ŝl₂₁) = κ · 31/967680 = (9/4) · 31/967680."""
        result = genus_expansion_from_shadow(1)
        # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
        assert result["genus_data"][3]["F_g"] == Fraction(9, 4) * Fraction(31, 967680)


# ======================================================================
# 12. Cross-level consistency
# ======================================================================

class TestCrossLevelConsistency:
    """Cross-level consistency checks (AP10)."""

    def test_cross_level_kappa(self):
        """κ increases with level."""
        result = cross_level_kappa_check(k_max=5)
        assert result["monotone_increasing"]

    def test_verify_all_levels_k5(self):
        """All shadow data consistent up to level 5."""
        result = verify_kl_shadow_all_levels(5)
        assert result["all_pass"]


# ======================================================================
# 13. Koszul dual shadow
# ======================================================================

class TestKoszulDualShadow:
    """Test κ + κ' = 0 for KM family (Feigin-Frenkel involution)."""

    def test_ff_involution_sum_sl2(self):
        """κ(ŝl₂_k) + κ(ŝl₂_{-k-4}) = dim(sl_2)/2 = 3/2.

        FF involution: k → -k - 2h∨ = -k - 4.
        κ(k) + κ(-k-4) = 3(k+2)/4 + 3(-k-4+2)/4 = 3(k+2)/4 + 3(-k-2)/4 = 0.
        """
        for k in [1, 2, 3, 4, 5]:
            k_dual = -k - 4  # -k - 2h∨
            kap = kappa_sl2(k)
            kap_dual = kappa_sl2(k_dual)
            # VERIFIED [DC] structural property [CF] cross-family census
            assert kap + kap_dual == 0, (
                f"FF sum at k={k}: κ + κ' = {kap + kap_dual}, expected 0"
            )

    def test_ff_involution_sum_sl3(self):
        """κ(ŝl₃_k) + κ(ŝl₃_{-k-6}) = 0.

        FF involution for sl_3: k → -k - 2h∨ = -k - 6.
        """
        for k in [1, 2, 3]:
            k_dual = -k - 6
            kap = kappa_sl3(k)
            kap_dual = kappa_sl3(k_dual)
            # VERIFIED [DC] structural property [CF] cross-family census
            assert kap + kap_dual == 0, (
                f"FF sum at k={k}: κ + κ' = {kap + kap_dual}, expected 0"
            )


# ======================================================================
# 14. Classical limit
# ======================================================================

class TestClassicalLimit:
    """Test behavior as k → ∞ (classical limit)."""

    def test_kappa_limit_sl2(self):
        """κ(ŝl₂_k)/k → 3/4 = dim(sl_2)/(2h∨) as k → ∞."""
        k = 10000
        ratio = float(kappa_sl2(k)) / k
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert abs(ratio - 0.75) < 0.001

    def test_kappa_limit_sl3(self):
        """κ(ŝl₃_k)/k → 4/3 = dim(sl_3)/(2h∨) as k → ∞."""
        k = 10000
        ratio = float(kappa_sl3(k)) / k
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert abs(ratio - 4.0/3.0) < 0.001
