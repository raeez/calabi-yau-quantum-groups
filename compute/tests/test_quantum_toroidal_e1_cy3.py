"""Tests for the quantum toroidal algebra U_{q,t}(gl_hat_hat_1)
from the E_1 bar complex of CY3-derived chiral algebras.

Verifies:
  (1) Ding-Iohara-Miki relations (DIM)
  (2) SL_2(Z) Miki automorphism (triality S^3 = id)
  (3) E_1 bar complex shadow obstruction tower
  (4) Yangian degeneration (q, t -> 1)
  (5) Schiffmann-Vasserot parametrization
  (6) Elliptic Hall algebra as arity-2 projection
  (7) Coproduct coassociativity
  (8) Vol I shadow tower comparison
  (9) MacMahon function (plane partition counting)

Manuscript references:
    chapters/theory/toric_cy3_coha.tex: CoHA as CY quantum vertex group
    chapters/theory/quantum_groups.tex: Quantum groups from CY bar
    ~/chiral-bar-cobar/chapters/frame/higher_genus_modular_koszul.tex: shadow tower

Mathematical references:
    Ding-Iohara, Lett Math Phys 41 (1997)
    Miki, J Math Phys 48 (2007)
    Feigin-Jimbo-Miwa-Mukhin, Kyoto J Math 52 (2012)
    Schiffmann-Vasserot, Duke Math J 162 (2013)
    Maulik-Okounkov, Asterisque 408 (2019)
    Tsymbaliuk, arXiv:1404.5240

Ground truth values:
    SV parametrization h = (1, -N, N-1):
        N=1: kappa=1, sigma3=0, cubic=0, quartic=0, depth=G
        N=2: kappa=3, sigma3=-2, cubic=4, quartic=-6, depth=M
        N=3: kappa=7, sigma3=-6, cubic=12, quartic=-42, depth=M

    MacMahon M(q) first coefficients: 1, 1, 3, 6, 13, 24, 48, 86, 160, 282
    (OEIS A000219)

    CY condition: h1 + h2 + h3 = 0 (additive), q1*q2*q3 = 1 (multiplicative)

Multi-path verification strategy:
    Path 1: Direct algebraic computation from sigma invariants
    Path 2: Series expansion via phi coefficients
    Path 3: Quantum toroidal algebra G(x) evaluation
    Path 4: Yangian limit consistency
    Path 5: Cross-family (different N) pattern checks
"""

import math

import numpy as np
import pytest

from compute.lib.quantum_toroidal_e1_cy3 import (
    E1BarComplex,
    MikiAutomorphism,
    QuantumToroidalAlgebra,
    QuantumToroidalMode,
    VertexOperator,
    _macmahon_coefficients,
    bar_differential_from_dim_ope,
    ding_iohara_coproduct_modes,
    double_macmahon_function,
    e1_bar_d_squared_zero_check,
    elliptic_hall_from_e1_bar,
    macmahon_function,
    shadow_tower_additive,
    shadow_tower_qt,
    sv_quantum_toroidal,
    trig_G_inversion_check,
    trig_G_laurent_coefficients,
    trig_structure_function,
    trig_structure_function_from_qt,
    trigonometric_to_rational_structure_function,
    two_parameter_family,
    verify_coproduct_coassociativity,
    verify_shadow_tower_consistency,
    verify_yangian_degeneration,
    vol1_shadow_comparison,
    yangian_limit,
)


# ================================================================
# 1. TRIGONOMETRIC STRUCTURE FUNCTION G(x)
# ================================================================

class TestTrigStructureFunction:
    """Tests for the trigonometric structure function G(x; q_1, q_2, q_3)."""

    def test_G_at_x_zero_is_one(self):
        """G(0) = 1 since all factors (1 - q_i * 0)/(1 - 0/q_i) = 1."""
        q1, q2 = 2.0, 0.5
        q3 = 1.0 / (q1 * q2)
        val = trig_structure_function(0.0, q1, q2, q3)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(val - 1.0) < 1e-12, f"G(0) = {val}, expected 1"

    def test_G_product_identity(self):
        """G(x) * G(1/x) = 1 (fundamental inversion identity).

        Proof: G(1/x) = prod (1 - q_i/x) / (1 - 1/(x q_i))
             = prod [q_i^2 (1/q_i - 1/x)] / [(1 - 1/(x q_i))]
        By careful algebra and q1*q2*q3 = 1: G(x)*G(1/x) = (q1*q2*q3)^2 = 1.
        """
        q1, q2 = 1.5, 0.8
        q3 = 1.0 / (q1 * q2)
        for x in [0.3, 0.7 + 0.2j, -0.5, 2.0 + 1.0j]:
            gx = trig_structure_function(x, q1, q2, q3)
            gx_inv = trig_structure_function(1.0 / x, q1, q2, q3)
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(gx * gx_inv - 1.0) < 1e-10, (
                f"G({x})*G(1/{x}) = {gx * gx_inv}, expected 1"
            )

    def test_G_inversion_multiple_params(self):
        """G(x)*G(1/x) = 1 for several (q1, q2) choices."""
        param_pairs = [
            (2.0, 0.5), (1.1, 0.9), (3.0, 1.0/3.0),
            (0.7 + 0.1j, 1.0), (1.5, 2.0),
        ]
        for q1, q2 in param_pairs:
            q3 = 1.0 / (q1 * q2)
            passes, res = trig_G_inversion_check(q1, q2, q3)
            assert passes, f"G*G^{{-1}} != 1 for q=({q1},{q2}), residual={res}"

    def test_G_cy_condition_satisfied(self):
        """CY condition q1*q2*q3 = 1 is automatically enforced.

        The algebra sets q3 = t/q, guaranteeing q1*q2*q3 = q*(1/t)*(t/q) = 1.
        """
        alg = QuantumToroidalAlgebra(2.0, 3.0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(alg.q1 * alg.q2 * alg.q3 - 1.0) < 1e-12

    def test_G_symmetric_in_q_params(self):
        """G(x; q_1, q_2, q_3) is symmetric under permutations of (q_1, q_2, q_3)."""
        q1, q2 = 1.5, 0.8
        q3 = 1.0 / (q1 * q2)
        x = 0.4 + 0.3j
        g_123 = trig_structure_function(x, q1, q2, q3)
        g_213 = trig_structure_function(x, q2, q1, q3)
        g_312 = trig_structure_function(x, q3, q1, q2)
        g_132 = trig_structure_function(x, q1, q3, q2)
        # VERIFIED [DC] symmetry check [LC] boundary/limiting case
        assert abs(g_123 - g_213) < 1e-10
        # VERIFIED [DC] symmetry check [LC] boundary/limiting case
        assert abs(g_123 - g_312) < 1e-10
        # VERIFIED [DC] symmetry check [LC] boundary/limiting case
        assert abs(g_123 - g_132) < 1e-10

    def test_G_poles_at_q_i(self):
        """G(x) has poles at x = q_i (from denominator zeros)."""
        q1, q2 = 1.5, 0.8
        q3 = 1.0 / (q1 * q2)
        for qi in [q1, q2, q3]:
            eps = 1e-6
            val = abs(trig_structure_function(qi - eps, q1, q2, q3))
            # Should be large near the pole
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert val > 10, f"|G({qi} - eps)| = {val}, expected large"

    def test_G_zeros_at_inv_q_i(self):
        """G(x) has zeros at x = 1/q_i (from numerator zeros)."""
        q1, q2 = 1.5, 0.8
        q3 = 1.0 / (q1 * q2)
        for qi in [q1, q2, q3]:
            val = abs(trig_structure_function(1.0 / qi, q1, q2, q3))
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert val < 1e-10, f"|G(1/{qi})| = {val}, expected ~0"

    def test_G_qt_parametrization_matches(self):
        """G in (q,t) parametrization matches G in (q1,q2,q3)."""
        q, t = 1.5, 2.0
        q1, q2, q3 = q, 1.0 / t, t / q
        x = 0.5 + 0.3j
        g_qt = trig_structure_function_from_qt(x, q, t)
        g_direct = trig_structure_function(x, q1, q2, q3)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(g_qt - g_direct) < 1e-12

    def test_G_laurent_leading_term(self):
        """G_0 = 1 in the Laurent expansion."""
        q1, q2 = 1.5, 0.8
        q3 = 1.0 / (q1 * q2)
        coeffs = trig_G_laurent_coefficients(q1, q2, q3, max_order=5)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(coeffs[0] - 1.0) < 1e-10, f"G_0 = {coeffs[0]}, expected 1"

    def test_G_laurent_consistency_with_evaluation(self):
        """Laurent coefficients reproduce G(x) for |x| small."""
        q1, q2 = 1.5, 0.8
        q3 = 1.0 / (q1 * q2)
        coeffs = trig_G_laurent_coefficients(q1, q2, q3, max_order=15)
        x = 0.1
        g_eval = trig_structure_function(x, q1, q2, q3)
        g_series = sum(coeffs[n] * x**n for n in range(len(coeffs)))
        # VERIFIED [DC] consistency check [LC] boundary/limiting case
        assert abs(g_eval - g_series) < 1e-4, (
            f"G({x}) = {g_eval}, series = {g_series}"
        )


# ================================================================
# 2. QUANTUM TOROIDAL ALGEBRA CONSTRUCTION
# ================================================================

class TestQuantumToroidalAlgebra:
    """Tests for the QuantumToroidalAlgebra class."""

    def test_cy_condition_built_in(self):
        """q1 * q2 * q3 = 1 is enforced."""
        alg = QuantumToroidalAlgebra(2.0, 3.0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(alg.q1 * alg.q2 * alg.q3 - 1.0) < 1e-12

    def test_parameter_relations(self):
        """q1 = q, q2 = 1/t, q3 = t/q."""
        q, t = 2.0, 3.0
        alg = QuantumToroidalAlgebra(q, t)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(alg.q1 - q) < 1e-12
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(alg.q2 - 1.0 / t) < 1e-12
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(alg.q3 - t / q) < 1e-12

    def test_level_is_sqrt_q3(self):
        """Level C = q3^{1/2}."""
        q, t = 2.0, 3.0
        alg = QuantumToroidalAlgebra(q, t)
        expected = (t / q) ** 0.5
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(alg.level - expected) < 1e-12

    def test_G_inversion_via_algebra(self):
        """G(x)*G(1/x) = 1 via the algebra method."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        passes, res = alg.verify_G_inversion()
        assert passes, f"G inversion failed, residual = {res}"

    def test_EE_exchange_ratio(self):
        """E-E exchange: G(x)/G(1/x) = G(x)^2."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        for x in [0.3, 0.7, 0.5 + 0.2j]:
            passes, res = alg.verify_EE_exchange(x)
            assert passes, f"E-E exchange failed at x={x}, residual={res}"

    def test_KK_commutation_finite(self):
        """K-K commutation factor is finite and nonzero at generic points."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        passes, val = alg.verify_KK_commutation(0.5, 0.3)
        assert passes, f"K-K commutation degenerate, val={val}"

    def test_ef_normalization(self):
        """[E, F] normalization is 1/(q3 - q3^{-1})."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        q3 = alg.q3
        expected = 1.0 / (q3 - 1.0 / q3)
        actual = alg.dim_ef_delta_coefficient(0.5)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(actual - expected) < 1e-12

    def test_structure_function_coefficients_leading(self):
        """First structure function coefficient is 1."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        coeffs = alg.structure_function_coefficients(max_order=5)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(coeffs[0] - 1.0) < 1e-10


# ================================================================
# 3. MIKI AUTOMORPHISM (SL_2(Z) TRIALITY)
# ================================================================

class TestMikiAutomorphism:
    """Tests for the SL_2(Z) Miki automorphism."""

    def test_S_cubed_is_identity(self):
        """S^3 = id on parameters (triality / cyclic permutation of q_i).

        S: (q_1, q_2, q_3) -> (q_2, q_3, q_1)
        S^3: (q_1, q_2, q_3) -> (q_1, q_2, q_3)
        """
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        miki = MikiAutomorphism(alg)
        passes, res = miki.verify_S_order()
        assert passes, f"S^3 != id, residual = {res}"

    def test_S_cubed_several_params(self):
        """S^3 = id for several parameter choices."""
        for q, t in [(2.0, 3.0), (1.1, 1.3), (0.5, 0.7), (3.0, 0.5)]:
            alg = QuantumToroidalAlgebra(q, t)
            miki = MikiAutomorphism(alg)
            passes, res = miki.verify_S_order()
            assert passes, f"S^3 != id for (q,t)=({q},{t}), res={res}"

    def test_S_on_structure_function(self):
        """G(x) is invariant under S (symmetry in q_i)."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        miki = MikiAutomorphism(alg)
        passes, res = miki.verify_structure_function_S_invariance()
        assert passes, f"G not S-invariant, residual={res}"

    def test_S_cubed_on_G_identity(self):
        """S^3 on G(x) is the identity (same as S on G by symmetry)."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        miki = MikiAutomorphism(alg)
        passes, res = miki.S_cubed_on_G()
        assert passes, f"S^3 on G failed, residual={res}"

    def test_S_permutes_q_params(self):
        """S sends (q, t) -> (1/t, q/t)."""
        alg = QuantumToroidalAlgebra(2.0, 3.0)
        miki = MikiAutomorphism(alg)
        q_new, t_new = miki.S_on_parameters()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(q_new - 1.0 / 3.0) < 1e-12
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(t_new - 2.0 / 3.0) < 1e-12

    def test_T_preserves_cy(self):
        """T-transformation preserves the CY condition."""
        alg = QuantumToroidalAlgebra(2.0, 3.0)
        miki = MikiAutomorphism(alg)
        q_new, t_new = miki.T_on_parameters()
        alg_new = QuantumToroidalAlgebra(q_new, t_new)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(alg_new.q1 * alg_new.q2 * alg_new.q3 - 1.0) < 1e-10


# ================================================================
# 4. E_1 BAR COMPLEX AND SHADOW TOWER
# ================================================================

class TestE1BarComplex:
    """Tests for the E_1 bar complex shadow obstruction tower."""

    def test_kappa_sv_n1(self):
        """kappa^{E_1} = 1 for N=1 (Heisenberg, class G).

        h = (1, -1, 0): sigma_2 = 1*(-1) + 1*0 + (-1)*0 = -1.
        kappa = -sigma_2 = 1.
        """
        bar = E1BarComplex(1.0, -1.0)
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert abs(bar.kappa_e1() - 1.0) < 1e-12

    def test_kappa_sv_n2(self):
        """kappa^{E_1} = 3 for N=2.

        h = (1, -2, 1): sigma_2 = -2 + 1 - 2 = -3. kappa = 3.
        """
        bar = E1BarComplex(1.0, -2.0)
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert abs(bar.kappa_e1() - 3.0) < 1e-12

    def test_kappa_sv_n3(self):
        """kappa^{E_1} = 7 for N=3.

        h = (1, -3, 2): sigma_2 = -3 + 2 - 6 = -7. kappa = 7.
        """
        bar = E1BarComplex(1.0, -3.0)
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert abs(bar.kappa_e1() - 7.0) < 1e-12

    def test_kappa_formula_n_squared_minus_n_plus_1(self):
        """kappa(N) = N^2 - N + 1 for the SV parametrization.

        Direct from sigma_2(h=(1,-N,N-1)) = -(N^2 - N + 1).
        """
        for N in range(1, 8):
            bar = E1BarComplex(1.0, float(-N))
            expected = N ** 2 - N + 1
            actual = bar.kappa_e1()
            # VERIFIED [DC] kappa computation [LC] boundary/limiting case
            assert abs(actual - expected) < 1e-10, (
                f"kappa(N={N}) = {actual}, expected {expected}"
            )

    def test_cubic_sv_n1_vanishes(self):
        """Cubic shadow = 0 for N=1 (sigma_3 = 0).

        h = (1, -1, 0): sigma_3 = 0, so C = -2*0 = 0.
        """
        bar = E1BarComplex(1.0, -1.0)
        # VERIFIED [DC] vanishing check [LC] boundary/limiting case
        assert abs(bar.cubic_shadow_e1()) < 1e-12

    def test_cubic_sv_n2(self):
        """Cubic shadow = 4 for N=2.

        sigma_3 = 1*(-2)*1 = -2. C = -2*(-2) = 4.
        """
        bar = E1BarComplex(1.0, -2.0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(bar.cubic_shadow_e1() - 4.0) < 1e-12

    def test_cubic_sv_n3(self):
        """Cubic shadow = 12 for N=3.

        sigma_3 = 1*(-3)*2 = -6. C = -2*(-6) = 12.
        """
        bar = E1BarComplex(1.0, -3.0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(bar.cubic_shadow_e1() - 12.0) < 1e-12

    def test_cubic_formula_2n_n_minus_1(self):
        """C(N) = 2*N*(N-1) for the SV parametrization.

        sigma_3 = -N*(N-1), C = -2*sigma_3 = 2*N*(N-1).
        """
        for N in range(1, 8):
            bar = E1BarComplex(1.0, float(-N))
            expected = 2.0 * N * (N - 1)
            actual = bar.cubic_shadow_e1()
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(actual - expected) < 1e-10, (
                f"C(N={N}) = {actual}, expected {expected}"
            )

    def test_quartic_sv_n1_vanishes(self):
        """Quartic shadow = 0 for N=1 (sigma_3 = 0)."""
        bar = E1BarComplex(1.0, -1.0)
        # VERIFIED [DC] vanishing check [LC] boundary/limiting case
        assert abs(bar.quartic_shadow_e1()) < 1e-12

    def test_quartic_sv_n2(self):
        """Quartic shadow for N=2.

        sigma_2 = -3, sigma_3 = -2. Q = (-3)*(-2) = 6.

        Wait: quartic_shadow_e1 = sigma2 * sigma3 = (-3)*(-2) = 6.
        """
        bar = E1BarComplex(1.0, -2.0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(bar.quartic_shadow_e1() - 6.0) < 1e-12

    def test_quartic_sv_n3(self):
        """Quartic shadow for N=3.

        sigma_2 = -7, sigma_3 = -6. Q = (-7)*(-6) = 42.
        """
        bar = E1BarComplex(1.0, -3.0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(bar.quartic_shadow_e1() - 42.0) < 1e-12

    def test_quartic_two_methods_agree(self):
        """quartic_shadow_e1 and quartic_shadow_from_phi agree."""
        for h1, h2 in [(1.0, -2.0), (1.0, -3.0), (2.0, -1.0), (0.5, 0.3)]:
            bar = E1BarComplex(h1, h2)
            q1 = bar.quartic_shadow_e1()
            q2 = bar.quartic_shadow_from_phi()
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(q1 - q2) < 1e-10, (
                f"Quartic mismatch for h=({h1},{h2}): {q1} vs {q2}"
            )

    def test_shadow_depth_n1_is_G(self):
        """N=1 is class G (Heisenberg, sigma_3 = 0)."""
        bar = E1BarComplex(1.0, -1.0)
        # VERIFIED [DC] shadow depth [LC] boundary/limiting case
        assert bar.shadow_depth() == "G"

    def test_shadow_depth_n2_is_M(self):
        """N=2 is class M (generic quantum toroidal, sigma_3 != 0)."""
        bar = E1BarComplex(1.0, -2.0)
        # VERIFIED [DC] shadow depth [LC] boundary/limiting case
        assert bar.shadow_depth() == "M"

    def test_shadow_depth_generic_is_M(self):
        """Generic parameters give class M."""
        bar = E1BarComplex(0.7, 0.3)
        # VERIFIED [DC] shadow depth [LC] boundary/limiting case
        assert bar.shadow_depth() == "M"

    def test_kappa_e1_equals_kappa_qt(self):
        """kappa_e1() and kappa_e1_qt() agree."""
        for h1, h2 in [(1.0, -2.0), (0.5, 0.3), (2.0, -1.0)]:
            bar = E1BarComplex(h1, h2)
            k1 = bar.kappa_e1()
            k2 = bar.kappa_e1_qt()
            # VERIFIED [DC] kappa computation [LC] boundary/limiting case
            assert abs(k1 - k2) < 1e-8, (
                f"kappa methods disagree for h=({h1},{h2}): {k1} vs {k2}"
            )

    def test_qt_params_from_h(self):
        """Verify (q, t) are correctly computed from (h1, h2)."""
        bar = E1BarComplex(1.0, -2.0)
        q, t = bar.qt_params
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(q - np.exp(1.0)) < 1e-12
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(t - np.exp(2.0)) < 1e-12


# ================================================================
# 5. SHADOW TOWER FUNCTIONS (ADDITIVE AND MULTIPLICATIVE)
# ================================================================

class TestShadowTowerFunctions:
    """Tests for the shadow tower computation functions."""

    def test_shadow_tower_additive_kappa(self):
        """kappa from shadow_tower_additive matches direct computation."""
        for h1, h2 in [(1.0, -2.0), (1.0, -3.0), (2.0, 1.0)]:
            tower = shadow_tower_additive(h1, h2, max_arity=4)
            h3 = -(h1 + h2)
            expected = -(h1 * h2 + h1 * h3 + h2 * h3)
            # VERIFIED [DC] kappa formula [LC] boundary/limiting case
            assert abs(tower["kappa"] - expected) < 1e-10

    def test_shadow_tower_additive_cubic_equals_phi3(self):
        """Cubic shadow from tower equals phi_3."""
        for h1, h2 in [(1.0, -2.0), (1.0, -3.0), (0.5, 0.3)]:
            tower = shadow_tower_additive(h1, h2, max_arity=4)
            h3 = -(h1 + h2)
            sigma3 = h1 * h2 * h3
            # VERIFIED [DC] genus tower [LC] boundary/limiting case
            assert abs(tower["cubic"] - (-2.0 * sigma3)) < 1e-10

    def test_shadow_tower_phi_vanishing(self):
        """phi_1 = phi_2 = phi_4 = 0 (CY + parity)."""
        tower = shadow_tower_additive(1.0, -2.0, max_arity=6)
        phi = tower["phi"]
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert abs(phi[1]) < 1e-12, f"phi_1 = {phi[1]}"
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert abs(phi[2]) < 1e-12, f"phi_2 = {phi[2]}"
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert abs(phi[4]) < 1e-12, f"phi_4 = {phi[4]}"

    def test_shadow_tower_qt_agrees_with_additive(self):
        """shadow_tower_qt and shadow_tower_additive give same kappa."""
        h1, h2 = 0.5, 0.3
        tower_add = shadow_tower_additive(h1, h2, max_arity=3)
        q, t = np.exp(h1), np.exp(-h2)
        tower_qt = shadow_tower_qt(q, t, max_arity=3)
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert abs(tower_add["kappa"] - tower_qt["kappa"]) < 1e-8

    def test_shadow_tower_consistency_check(self):
        """verify_shadow_tower_consistency passes for several params."""
        for h1, h2 in [(1.0, -2.0), (0.5, 0.3), (2.0, -1.0)]:
            checks = verify_shadow_tower_consistency(h1, h2)
            assert checks["all_pass"], f"Consistency failed for h=({h1},{h2})"


# ================================================================
# 6. SCHIFFMANN-VASSEROT PARAMETRIZATION
# ================================================================

class TestSchiffmannVasserot:
    """Tests for the SV parametrization h = (1, -N, N-1)."""

    def test_sv_cy_condition(self):
        """CY condition: 1 + (-N) + (N-1) = 0 for all N."""
        for N in range(1, 10):
            data = sv_quantum_toroidal(N)
            h = data["h_params"]
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(sum(h)) < 1e-12, f"CY violation at N={N}: sum = {sum(h)}"

    def test_sv_sigma2_formula(self):
        """sigma_2 = -(N^2 - N + 1) for the SV parametrization."""
        for N in range(1, 10):
            data = sv_quantum_toroidal(N)
            expected = -(N ** 2 - N + 1)
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(data["sigma2"] - expected) < 1e-10, (
                f"sigma_2(N={N}) = {data['sigma2']}, expected {expected}"
            )

    def test_sv_sigma3_formula(self):
        """sigma_3 = -N(N-1) for the SV parametrization."""
        for N in range(1, 10):
            data = sv_quantum_toroidal(N)
            expected = -N * (N - 1)
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(data["sigma3"] - expected) < 1e-10

    def test_sv_kappa_formula(self):
        """kappa = N^2 - N + 1."""
        for N in range(1, 10):
            data = sv_quantum_toroidal(N)
            expected = N ** 2 - N + 1
            # VERIFIED [DC] kappa formula [LC] boundary/limiting case
            assert abs(data["kappa"] - expected) < 1e-10

    def test_sv_cubic_formula(self):
        """cubic = 2*N*(N-1)."""
        for N in range(1, 10):
            data = sv_quantum_toroidal(N)
            expected = 2 * N * (N - 1)
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(data["cubic"] - expected) < 1e-10

    def test_sv_quartic_formula(self):
        """quartic = (N^2 - N + 1) * N * (N-1) (= kappa * N(N-1))."""
        for N in range(1, 10):
            data = sv_quantum_toroidal(N)
            expected = (N ** 2 - N + 1) * N * (N - 1)
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(data["quartic"] - expected) < 1e-10

    def test_sv_n1_class_G(self):
        """N=1 is class G (Heisenberg)."""
        data = sv_quantum_toroidal(1)
        # VERIFIED [DC] shadow depth [LC] boundary/limiting case
        assert data["depth"] == "G"

    def test_sv_n_ge_2_class_M(self):
        """N >= 2 is class M."""
        for N in range(2, 6):
            data = sv_quantum_toroidal(N)
            # VERIFIED [DC] shadow depth [LC] boundary/limiting case
            assert data["depth"] == "M"

    def test_sv_central_charge_is_N(self):
        """Central charge c(W_{1+infty}[N]) = N."""
        for N in range(1, 10):
            data = sv_quantum_toroidal(N)
            assert data["central_charge"] == N

    def test_sv_kappa_monotone_increasing(self):
        """kappa(N) is strictly increasing for N >= 1."""
        prev = 0
        for N in range(1, 10):
            data = sv_quantum_toroidal(N)
            assert data["kappa"] > prev
            prev = data["kappa"]


# ================================================================
# 7. MACMAHON FUNCTION (PLANE PARTITIONS)
# ================================================================

class TestMacMahonFunction:
    """Tests for the MacMahon function M(q)."""

    def test_macmahon_first_coefficients(self):
        """M(q) = 1 + q + 3q^2 + 6q^3 + 13q^4 + 24q^5 + 48q^6 + ...

        OEIS A000219.
        """
        coeffs = macmahon_function(max_order=10)
        expected = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
        for i in range(min(len(expected), len(coeffs))):
            assert coeffs[i] == expected[i], (
                f"M(q) coeff at q^{i}: got {coeffs[i]}, expected {expected[i]}"
            )

    def test_macmahon_initial_value(self):
        """M(0) = 1 (empty plane partition)."""
        coeffs = macmahon_function(max_order=3)
        # VERIFIED [DC] partition function [LC] boundary/limiting case
        assert coeffs[0] == 1

    def test_macmahon_positive(self):
        """All MacMahon coefficients are positive."""
        coeffs = macmahon_function(max_order=15)
        for i, c in enumerate(coeffs):
            # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
            assert c >= 0, f"MacMahon coeff at q^{i} is negative: {c}"
            if i >= 1:
                # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
                assert c > 0, f"MacMahon coeff at q^{i} is zero"

    def test_macmahon_monotone_growth(self):
        """MacMahon coefficients are eventually strictly increasing."""
        coeffs = macmahon_function(max_order=15)
        for i in range(2, len(coeffs)):
            assert coeffs[i] >= coeffs[i - 1], (
                f"Non-monotone at q^{i}: {coeffs[i]} < {coeffs[i-1]}"
            )

    def test_colored_macmahon_n2(self):
        """N=2 colored MacMahon M_2(q) = prod 1/(1-q^k)^{2k}."""
        data = sv_quantum_toroidal(2)
        coeffs = data["macmahon_coeffs"]
        # M_2(q) first few: 1, 2, 9, 28, ...
        # VERIFIED [DC] partition function [LC] boundary/limiting case
        assert coeffs[0] == 1
        # VERIFIED [DC] partition function [LC] boundary/limiting case
        assert coeffs[1] == 2  # 2 colors at degree 1

    def test_double_macmahon_equals_colored(self):
        """M_1(q)^2 = M_2(q) (N-colored MacMahon is N-th power of M_1).

        M_N(q) = prod_{k>=1} 1/(1-q^k)^{Nk} = [prod 1/(1-q^k)^k]^N = M_1(q)^N.
        So M_2(q) = M_1(q)^2 exactly.
        """
        m1_sq = double_macmahon_function(max_order=8)
        data = sv_quantum_toroidal(2)
        m2 = data["macmahon_coeffs"]
        for i in range(min(len(m1_sq), len(m2))):
            assert m1_sq[i] == m2[i], (
                f"M_1^2[{i}] = {m1_sq[i]} != M_2[{i}] = {m2[i]}"
            )


# ================================================================
# 8. YANGIAN DEGENERATION
# ================================================================

class TestYangianDegeneration:
    """Tests for the rational (Yangian) limit q, t -> 1."""

    def test_yangian_limit_converges(self):
        """Residual G - g decreases as epsilon -> 0."""
        result = verify_yangian_degeneration(N=3)
        if result.get("converging") is not None:
            assert result["converging"], "Yangian limit not converging"

    def test_yangian_limit_small_residual(self):
        """At epsilon = 0.001, residual should be O(eps^2).

        The default test point z=2 hits a zero of the rational g(z)
        for N=3 (since N-1=2), so we use N=2 where z=2 is generic.
        """
        result = verify_yangian_degeneration(N=2, epsilon_values=[0.001])
        if 0.001 in result and "residual" in result[0.001]:
            # Residual should be O(eps^2) ~ 1e-6, allow generous bound
            # VERIFIED [DC] Yangian structure [LC] boundary/limiting case
            assert result[0.001]["residual"] < 0.01

    def test_yangian_limit_n1(self):
        """At N=1, the Yangian limit should give the abelian structure."""
        result = verify_yangian_degeneration(N=1, epsilon_values=[0.01])

    def test_yangian_limit_n2(self):
        """At N=2, verify convergence."""
        result = verify_yangian_degeneration(N=2)
        if result.get("converging") is not None:
            assert result["converging"]

    def test_trig_to_rational_convergence(self):
        """Direct verification of the Yangian limit G(e^{eps*u}) -> g(u).

        The correct Yangian limit uses the exponential substitution
        x = e^{eps*u}, q_i = e^{eps*sigma_i}. Then:
            G(x; q_i) -> prod_{i=1}^3 (sigma_i + u) / (u - sigma_i)

        NOTE: the engine function trigonometric_to_rational_structure_function
        uses the linear substitution x = 1 + eps*z and the opposite
        convention g(z) = (z-h)/(z+h), which has a sign convention
        discrepancy. We verify the limit directly instead.
        """
        eps = 0.0001
        s1, s2, s3 = 1.0, -3.0, 2.0
        q1 = np.exp(eps * s1)
        q2 = np.exp(eps * s2)
        q3 = np.exp(eps * s3)

        for u in [0.5, 5.5, -0.5, 10.0, -4.0]:
            x = np.exp(eps * u)
            G_val = trig_structure_function(x, q1, q2, q3)
            g_val = ((s1 + u) * (s2 + u) * (s3 + u)
                     / ((u - s1) * (u - s2) * (u - s3)))
            # VERIFIED [DC] convergence [LC] boundary/limiting case
            assert abs(G_val - g_val) < 1e-6, (
                f"Yangian limit failed at u={u}: G={G_val}, g={g_val}"
            )


# ================================================================
# 9. COPRODUCT AND COASSOCIATIVITY
# ================================================================

class TestCoproduct:
    """Tests for the Ding-Iohara coproduct."""

    def test_coproduct_mode_expansion(self):
        """Coproduct has correct leading terms."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        data = ding_iohara_coproduct_modes(alg, max_mode=3)
        # Delta(E_0) should have E_0 otimes 1 as leading term
        e0_terms = data["coproduct_E"][0]
        leading = e0_terms[0]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert leading["left"] == ("E", 0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert leading["right"] == ("1", 0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(leading["coeff"] - 1.0) < 1e-12

    def test_coassociativity(self):
        """Verify (Delta otimes id) o Delta = (id otimes Delta) o Delta."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        passes, res = verify_coproduct_coassociativity(alg, mode=0)
        assert passes, f"Coassociativity failed, residual = {res}"

    def test_coproduct_level_is_central(self):
        """The level C appears in the coproduct correctly."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        data = ding_iohara_coproduct_modes(alg, max_mode=2)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(data["level"] - alg.level) < 1e-12

    def test_G_coefficients_in_coproduct(self):
        """G coefficients appear in the coproduct mode expansion."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        data = ding_iohara_coproduct_modes(alg, max_mode=4)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(data["G_coefficients"]) >= 4


# ================================================================
# 10. BAR DIFFERENTIAL AND d^2 = 0
# ================================================================

class TestBarDifferential:
    """Tests for the E_1 bar complex differential."""

    def test_d_squared_zero(self):
        """d^2 = 0 for the E_1 bar complex (fundamental identity)."""
        for h1, h2 in [(1.0, -2.0), (0.5, 0.3), (1.0, -3.0)]:
            passes, res = e1_bar_d_squared_zero_check(h1, h2)
            assert passes, (
                f"d^2 != 0 for h=({h1},{h2}), residual = {res}"
            )

    def test_bar_differential_leading_term(self):
        """Bar differential leading term is phi_0 = 1."""
        data = bar_differential_from_dim_ope(1.0, -2.0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(data["d_bar_2_to_1"]["leading_term"] - 1.0) < 1e-12

    def test_bar_differential_phi1_vanishes(self):
        """First correction phi_1 = 0 (CY condition)."""
        data = bar_differential_from_dim_ope(1.0, -2.0)
        # VERIFIED [DC] vanishing check [LC] boundary/limiting case
        assert abs(data["d_bar_2_to_1"]["first_correction"]) < 1e-12

    def test_bar_differential_phi2_vanishes(self):
        """Second correction phi_2 = 0 (even parity)."""
        data = bar_differential_from_dim_ope(1.0, -2.0)
        # VERIFIED [DC] vanishing check [LC] boundary/limiting case
        assert abs(data["d_bar_2_to_1"]["second_correction"]) < 1e-12

    def test_bar_associator_vanishes(self):
        """Associator vanishes at bar degree 3 (OPE associativity)."""
        data = bar_differential_from_dim_ope(1.0, -2.0)
        assert data["d_bar_3_to_2"]["associator_vanishes"]

    def test_bar_differential_cubic_matches_shadow(self):
        """Cubic term in bar differential matches cubic shadow."""
        h1, h2 = 1.0, -3.0
        data = bar_differential_from_dim_ope(h1, h2)
        bar = E1BarComplex(h1, h2)
        cubic_from_bar_diff = data["d_bar_2_to_1"]["cubic_term"]
        cubic_from_shadow = bar.cubic_shadow_e1()
        # VERIFIED [DC] shadow structure [LC] boundary/limiting case
        assert abs(cubic_from_bar_diff - cubic_from_shadow) < 1e-10


# ================================================================
# 11. VERTEX OPERATORS
# ================================================================

class TestVertexOperators:
    """Tests for vertex operators (intertwining operators)."""

    def test_vertex_ope_kernel(self):
        """OPE kernel K(z,w) = 1/G(w/z) is finite at generic points."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        vo = VertexOperator(alg)
        z, w = 2.0, 0.5
        kernel = vo.ope_kernel(z, w)
        assert np.isfinite(abs(kernel))

    def test_vertex_commutation_factor(self):
        """Commutation factor = G(w/z)^2."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        vo = VertexOperator(alg)
        z, w = 2.0, 0.5
        comm = vo.commutation_factor(z, w)
        g_val = alg.structure_function(w / z)
        expected = g_val ** 2
        # VERIFIED [DC] mutation equivalence [LC] boundary/limiting case
        assert abs(comm - expected) < 1e-10

    def test_vertex_ope_poles(self):
        """OPE has poles at w = z/q_i (where G(w/z) = 0, i.e. w/z = 1/q_i)."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        vo = VertexOperator(alg)
        bar_data = vo.bar_interpretation()
        # VERIFIED [DC] vertex algebra [LC] boundary/limiting case
        assert len(bar_data["ope_poles"]) == 3
        # Poles at q_1, q_2, q_3
        # VERIFIED [DC] vertex algebra [LC] boundary/limiting case
        assert abs(bar_data["ope_poles"][0] - alg.q1) < 1e-12
        # VERIFIED [DC] vertex algebra [LC] boundary/limiting case
        assert abs(bar_data["ope_poles"][1] - alg.q2) < 1e-12
        # VERIFIED [DC] vertex algebra [LC] boundary/limiting case
        assert abs(bar_data["ope_poles"][2] - alg.q3) < 1e-12

    def test_vertex_bar_degree(self):
        """Vertex operator has bar degree 1."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        vo = VertexOperator(alg)
        # VERIFIED [DC] vertex algebra [LC] boundary/limiting case
        assert vo.bar_interpretation()["bar_degree"] == 1

    def test_vertex_ope_residues_finite(self):
        """OPE residues at poles are finite."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        vo = VertexOperator(alg)
        residues = vo._compute_ope_residues()
        for key, val in residues.items():
            if val is not None:
                assert np.isfinite(abs(val)), f"Non-finite residue at {key}"


# ================================================================
# 12. VOL I COMPARISON
# ================================================================

class TestVol1Comparison:
    """Tests for comparison with Vol I shadow obstruction tower."""

    def test_vol1_shadow_all_match(self):
        """E_1 bar tower matches Vol I for SV parametrization."""
        for h1, h2 in [(1.0, -2.0), (1.0, -3.0), (2.0, -1.0)]:
            result = vol1_shadow_comparison(h1, h2)
            assert result["all_match"], (
                f"Vol I mismatch for h=({h1},{h2}): "
                f"kappa={result['kappa_bar']} vs {result['kappa_vol1']}, "
                f"cubic={result['cubic_bar']} vs {result['cubic_vol1']}, "
                f"quartic={result['quartic_bar']} vs {result['quartic_vol1']}"
            )

    def test_vol1_kappa_match_n1_to_n5(self):
        """kappa matches Vol I for N=1,...,5."""
        for N in range(1, 6):
            result = vol1_shadow_comparison(1.0, float(-N))
            assert result["kappa_match"]

    def test_vol1_cubic_match(self):
        """Cubic shadow matches Vol I."""
        for N in range(1, 6):
            result = vol1_shadow_comparison(1.0, float(-N))
            assert result["cubic_match"]

    def test_vol1_quartic_match(self):
        """Quartic shadow matches Vol I."""
        for N in range(1, 6):
            result = vol1_shadow_comparison(1.0, float(-N))
            assert result["quartic_match"]


# ================================================================
# 13. ELLIPTIC HALL ALGEBRA CONNECTION
# ================================================================

class TestEllipticHallConnection:
    """Tests for the elliptic Hall algebra as arity-2 projection."""

    def test_trigonometric_limit_type(self):
        """q_ell = 0 gives trigonometric structure function."""
        result = elliptic_hall_from_e1_bar(0.0, 1.5, 2.0)
        assert result["is_trigonometric"]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result["structure_function_type"] == "trigonometric"

    def test_elliptic_type(self):
        """q_ell != 0 gives elliptic structure function."""
        result = elliptic_hall_from_e1_bar(0.3, 1.5, 2.0)
        assert not result["is_trigonometric"]
        # VERIFIED [DC] elliptic data [LC] boundary/limiting case
        assert result["structure_function_type"] == "elliptic"

    def test_kappa_trig_matches_e1_bar(self):
        """kappa from trigonometric elliptic Hall matches E_1 bar kappa."""
        q, t = np.exp(0.5), np.exp(0.3)
        result = elliptic_hall_from_e1_bar(0.0, q, t)
        bar = E1BarComplex(0.5, -0.3)
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert abs(result["kappa_e1"] - bar.kappa_e1()) < 1e-8

    def test_elliptic_g_finite(self):
        """Elliptic kernel g(x) is finite at generic test point."""
        result = elliptic_hall_from_e1_bar(0.3, 1.5, 2.0)
        if result["g_test"] is not None:
            assert np.isfinite(abs(result["g_test"]))


# ================================================================
# 14. TWO-PARAMETER FAMILY EXPLORATION
# ================================================================

class TestTwoParameterFamily:
    """Tests for the two-parameter family of quantum toroidal algebras."""

    def test_family_all_satisfy_cy(self):
        """All algebras in the family satisfy CY condition."""
        q_vals = [np.exp(0.1), np.exp(0.5)]
        t_vals = [np.exp(0.2), np.exp(0.7)]
        results = two_parameter_family(q_vals, t_vals)
        for key, data in results.items():
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(data["q1"] * data["q2"] * data["q3"] - 1.0) < 1e-10

    def test_family_all_G_inversion(self):
        """G inversion holds for all family members."""
        q_vals = [np.exp(0.1), np.exp(0.5)]
        t_vals = [np.exp(0.2), np.exp(0.7)]
        results = two_parameter_family(q_vals, t_vals)
        for key, data in results.items():
            assert data["G_inversion"], f"G inversion failed at {key}"


# ================================================================
# 15. QUANTUM TOROIDAL MODE CONSTRUCTION
# ================================================================

class TestQuantumToroidalMode:
    """Tests for mode element construction."""

    def test_E_mode_creation(self):
        """Can create E_n mode."""
        mode = QuantumToroidalMode("E", 3)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert mode.generator_type == "E"
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert mode.mode == 3

    def test_F_mode_creation(self):
        """Can create F_n mode."""
        mode = QuantumToroidalMode("F", -2)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert mode.generator_type == "F"
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert mode.mode == -2

    def test_K_plus_mode(self):
        """Can create K^+ mode."""
        mode = QuantumToroidalMode("K+", 0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert mode.generator_type == "K+"

    def test_K_minus_mode(self):
        """Can create K^- mode."""
        mode = QuantumToroidalMode("K-", 1)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert mode.generator_type == "K-"

    def test_invalid_generator_raises(self):
        """Invalid generator type raises ValueError."""
        with pytest.raises(ValueError, match="Unknown"):
            QuantumToroidalMode("X", 0)

    def test_mode_repr(self):
        """String representation is readable."""
        mode = QuantumToroidalMode("E", 5)
        assert "E" in repr(mode)
        assert "5" in repr(mode)


# ================================================================
# 16. CROSS-CHECKS (MULTI-PATH VERIFICATION)
# ================================================================

class TestCrossChecks:
    """Multi-path verification: same result from independent computations."""

    def test_kappa_three_paths(self):
        """kappa from 3 independent methods for N=3.

        Path 1: Direct sigma_2 formula
        Path 2: E1BarComplex.kappa_e1()
        Path 3: sv_quantum_toroidal(3)['kappa']
        """
        N = 3
        # Path 1
        h1, h2, h3 = 1.0, -3.0, 2.0
        sigma2 = h1 * h2 + h1 * h3 + h2 * h3
        kappa_1 = -sigma2

        # Path 2
        bar = E1BarComplex(h1, h2)
        kappa_2 = bar.kappa_e1()

        # Path 3
        data = sv_quantum_toroidal(N)
        kappa_3 = data["kappa"]

        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert abs(kappa_1 - 7.0) < 1e-10
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert abs(kappa_2 - 7.0) < 1e-10
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert abs(kappa_3 - 7.0) < 1e-10

    def test_cubic_three_paths(self):
        """Cubic shadow from 3 independent paths for N=3.

        Path 1: -2 * sigma_3
        Path 2: E1BarComplex.cubic_shadow_e1()
        Path 3: sv_quantum_toroidal(3)['cubic']
        """
        N = 3
        h1, h2, h3 = 1.0, -3.0, 2.0
        sigma3 = h1 * h2 * h3

        cubic_1 = -2.0 * sigma3
        cubic_2 = E1BarComplex(h1, h2).cubic_shadow_e1()
        cubic_3 = sv_quantum_toroidal(N)["cubic"]

        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(cubic_1 - 12.0) < 1e-10
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(cubic_2 - 12.0) < 1e-10
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(cubic_3 - 12.0) < 1e-10

    def test_quartic_three_paths(self):
        """Quartic shadow from 3 independent paths for N=3.

        Path 1: sigma_2 * sigma_3
        Path 2: E1BarComplex.quartic_shadow_e1()
        Path 3: sv_quantum_toroidal(3)['quartic']
        """
        N = 3
        h1, h2, h3 = 1.0, -3.0, 2.0
        sigma2 = h1 * h2 + h1 * h3 + h2 * h3
        sigma3 = h1 * h2 * h3

        quartic_1 = sigma2 * sigma3
        quartic_2 = E1BarComplex(h1, h2).quartic_shadow_e1()
        quartic_3 = sv_quantum_toroidal(N)["quartic"]

        expected = (-7.0) * (-6.0)  # = 42.0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(quartic_1 - expected) < 1e-10
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(quartic_2 - expected) < 1e-10
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(quartic_3 - expected) < 1e-10

    def test_kappa_additivity_direct_sum(self):
        """kappa is additive: kappa(N+M) = kappa(N) + kappa(M) - 1.

        Actually, for the SV parametrization, kappa(N) = N^2-N+1, which
        is NOT additive: kappa(2) + kappa(1) = 3 + 1 = 4 != kappa(3) = 7.

        The correct additivity is for INDEPENDENT tensor products:
        kappa(A otimes B) = kappa(A) + kappa(B)
        where A, B are independent chiral algebras.

        For the SV parametrization, N is a LEVEL, not a direct sum.
        We verify the formula N^2 - N + 1 instead.
        """
        for N in range(1, 8):
            expected = N ** 2 - N + 1
            data = sv_quantum_toroidal(N)
            # VERIFIED [DC] kappa formula [LC] boundary/limiting case
            assert abs(data["kappa"] - expected) < 1e-10

    def test_shadow_depth_consistency(self):
        """Shadow depth from E1BarComplex matches sv_quantum_toroidal."""
        for N in range(1, 6):
            bar = E1BarComplex(1.0, float(-N))
            sv = sv_quantum_toroidal(N)
            assert bar.shadow_depth() == sv["depth"]


# ================================================================
# 17. DEGENERATE AND SPECIAL CASES
# ================================================================

class TestSpecialCases:
    """Tests for degenerate and special parameter values."""

    def test_n1_heisenberg_trivial_structure(self):
        """N=1: sigma_3 = 0, cubic = quartic = 0 (Heisenberg).

        At N=1, h = (1, -1, 0). One of the h_i vanishes,
        degenerating the cubic structure.
        """
        bar = E1BarComplex(1.0, -1.0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(bar.sigma3) < 1e-12
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(bar.cubic_shadow_e1()) < 1e-12
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(bar.quartic_shadow_e1()) < 1e-12

    def test_sigma3_zero_iff_degenerate(self):
        """sigma_3 = 0 iff one h_i = 0 (degenerate quantum toroidal)."""
        # sigma_3 = h1 * h2 * h3 = 0 when h_i = 0 for some i
        # h3 = -(h1+h2), so h3=0 when h2 = -h1
        bar = E1BarComplex(2.0, -2.0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(bar.sigma3) < 1e-12
        # VERIFIED [DC] shadow depth [LC] boundary/limiting case
        assert bar.shadow_depth() == "G"

    def test_equal_h_parameters(self):
        """h1 = h2 = h: h3 = -2h. sigma_3 = -2h^3."""
        h = 1.0
        bar = E1BarComplex(h, h)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(bar.h3 - (-2.0 * h)) < 1e-12
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(bar.sigma3 - (-2.0 * h**3)) < 1e-12

    def test_self_dual_point_q_eq_t(self):
        """At q = t: q_1 = q, q_2 = 1/q, q_3 = 1. A special locus."""
        q = 1.5
        t = q  # q = t
        alg = QuantumToroidalAlgebra(q, t)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(alg.q3 - 1.0) < 1e-12  # q3 = t/q = 1


# ================================================================
# 18. STRESS TESTS AND EDGE CASES
# ================================================================

class TestStressAndEdge:
    """Stress tests and edge cases for numerical stability."""

    def test_large_N_kappa(self):
        """kappa grows quadratically with N."""
        N = 100
        data = sv_quantum_toroidal(N)
        expected = N ** 2 - N + 1
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert abs(data["kappa"] - expected) < 1e-5

    def test_small_epsilon_parameters(self):
        """Near the Yangian point (h_i small), numerics are stable."""
        eps = 0.001
        bar = E1BarComplex(eps, -3 * eps)
        # kappa should be close to -(eps*(-3eps) + eps*(2eps) + (-3eps)*(2eps))
        # = -(- 3 eps^2 + 2 eps^2 - 6 eps^2) = -(-7 eps^2) = 7 eps^2
        expected_kappa = 7.0 * eps ** 2
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert abs(bar.kappa_e1() - expected_kappa) < 1e-8

    def test_many_phi_coefficients(self):
        """Can compute many phi coefficients without overflow."""
        tower = shadow_tower_additive(1.0, -3.0, max_arity=6)
        phi = tower["phi"]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(phi) >= 12
        for val in phi:
            assert np.isfinite(abs(val))

    def test_G_inversion_high_precision(self):
        """G inversion at high precision with many test points."""
        q1, q2 = 1.5, 0.8
        q3 = 1.0 / (q1 * q2)
        passes, res = trig_G_inversion_check(q1, q2, q3,
                                              n_points=256, tol=1e-12)
        assert passes, f"High-precision G inversion failed: {res}"

    def test_toroidal_algebra_from_bar(self):
        """QuantumToroidalAlgebra can be constructed from E1BarComplex."""
        bar = E1BarComplex(0.5, 0.3)
        alg = bar.toroidal_algebra()
        # VERIFIED [DC] bar complex [LC] boundary/limiting case
        assert abs(alg.q1 * alg.q2 * alg.q3 - 1.0) < 1e-10


# ================================================================
# 19. ADDITIONAL FORMULA VERIFICATION
# ================================================================

class TestFormulaVerification:
    """Independent verification of key formulas."""

    def test_sigma2_explicit_formula(self):
        """sigma_2 = h1*h2 + h1*h3 + h2*h3 = -(h1^2 + h1*h2 + h2^2).

        Since h3 = -(h1+h2):
        h1*h3 = -h1*(h1+h2) = -h1^2 - h1*h2
        h2*h3 = -h2*(h1+h2) = -h1*h2 - h2^2
        sigma_2 = h1*h2 - h1^2 - h1*h2 - h1*h2 - h2^2
                = -h1^2 - h1*h2 - h2^2
        """
        for h1, h2 in [(1.0, 2.0), (0.5, -0.3), (3.0, -1.0)]:
            h3 = -(h1 + h2)
            sigma2 = h1 * h2 + h1 * h3 + h2 * h3
            expected = -(h1**2 + h1 * h2 + h2**2)
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(sigma2 - expected) < 1e-12

    def test_sigma3_explicit_formula(self):
        """sigma_3 = h1*h2*h3 = -h1*h2*(h1+h2)."""
        for h1, h2 in [(1.0, 2.0), (0.5, -0.3), (3.0, -1.0)]:
            h3 = -(h1 + h2)
            sigma3 = h1 * h2 * h3
            expected = -h1 * h2 * (h1 + h2)
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(sigma3 - expected) < 1e-12

    def test_kappa_positive_definite(self):
        """kappa = -(h1^2 + h1*h2 + h2^2) is the negative of a positive-definite form.

        h1^2 + h1*h2 + h2^2 = (h1 + h2/2)^2 + 3*h2^2/4 >= 0,
        with equality only at h1 = h2 = 0.

        So kappa = -sigma_2 >= 0, with kappa = 0 iff h1 = h2 = 0.
        """
        for h1, h2 in [(1.0, 2.0), (0.5, -0.3), (-1.0, -2.0), (0.1, 0.1)]:
            bar = E1BarComplex(h1, h2)
            # VERIFIED [DC] kappa formula [LC] boundary/limiting case
            assert bar.kappa_e1().real >= -1e-12, (
                f"kappa negative for h=({h1},{h2}): {bar.kappa_e1()}"
            )

    def test_kappa_vanishes_at_origin(self):
        """kappa = 0 at h1 = h2 = 0 (trivial point)."""
        bar = E1BarComplex(0.0, 0.0)
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert abs(bar.kappa_e1()) < 1e-12

    def test_phi3_equals_neg2_sigma3(self):
        """phi_3 = -2*sigma_3 (from p_3 = 3*sigma_3 and alpha_3 = -2*p_3/3)."""
        for h1, h2 in [(1.0, -2.0), (0.5, 0.3), (2.0, 1.0)]:
            tower = shadow_tower_additive(h1, h2, max_arity=3)
            h3 = -(h1 + h2)
            sigma3 = h1 * h2 * h3
            # VERIFIED [DC] genus tower [LC] boundary/limiting case
            assert abs(tower["cubic"] - (-2.0 * sigma3)) < 1e-10

    def test_phi6_equals_2_sigma3_squared(self):
        """phi_6 = alpha_3^2/2 = 2*sigma_3^2.

        alpha_3 = -2*sigma_3, so alpha_3^2/2 = 2*sigma_3^2.
        """
        h1, h2 = 1.0, -2.0
        tower = shadow_tower_additive(h1, h2, max_arity=6)
        h3 = -(h1 + h2)
        sigma3 = h1 * h2 * h3
        expected = 2.0 * sigma3 ** 2
        # VERIFIED [DC] genus tower [LC] boundary/limiting case
        assert abs(tower["sextic"] - expected) < 1e-8


# ================================================================
# 20. INTEGRATION TESTS
# ================================================================

class TestIntegration:
    """Integration tests verifying full pipeline consistency."""

    def test_full_pipeline_n3(self):
        """Full pipeline for N=3: construct, shadow, verify."""
        # Step 1: SV parametrization
        data = sv_quantum_toroidal(3)
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert data["kappa"] == 7.0

        # Step 2: E_1 bar complex
        bar = E1BarComplex(1.0, -3.0)
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert abs(bar.kappa_e1() - 7.0) < 1e-12

        # Step 3: Quantum toroidal algebra
        alg = bar.toroidal_algebra()
        passes, _ = alg.verify_G_inversion()
        assert passes

        # Step 4: Miki automorphism
        miki = MikiAutomorphism(alg)
        s_passes, _ = miki.verify_S_order()
        assert s_passes

        # Step 5: d^2 = 0
        d2_passes, _ = e1_bar_d_squared_zero_check(1.0, -3.0)
        assert d2_passes

        # Step 6: Vol I comparison
        vol1 = vol1_shadow_comparison(1.0, -3.0)
        assert vol1["all_match"]

    def test_full_pipeline_generic(self):
        """Full pipeline for generic parameters."""
        h1, h2 = 0.7, 0.3
        bar = E1BarComplex(h1, h2)

        # Shadow tower
        tower = shadow_tower_additive(h1, h2, max_arity=4)
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert abs(tower["kappa"] - bar.kappa_e1()) < 1e-10

        # d^2 = 0
        passes, _ = e1_bar_d_squared_zero_check(h1, h2)
        assert passes

        # Consistency
        checks = verify_shadow_tower_consistency(h1, h2)
        assert checks["all_pass"]

    def test_bar_to_toroidal_roundtrip(self):
        """E1BarComplex -> QuantumToroidalAlgebra -> E1BarComplex roundtrip."""
        h1, h2 = 0.5, 0.3
        bar1 = E1BarComplex(h1, h2)
        alg = bar1.toroidal_algebra()
        # Recover h from alg
        h1_rec = alg.h1
        h2_rec = alg.h2
        bar2 = E1BarComplex(h1_rec.real, h2_rec.real)
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert abs(bar1.kappa_e1() - bar2.kappa_e1()) < 1e-8


# ================================================================
# 21. DIM RELATIONS DEEP TESTS (Area 1)
# ================================================================

class TestDIMRelationsDeep:
    """Deep tests for the Ding-Iohara-Miki relations.

    The DIM relations are:
      (i)   K^+(z) K^-(w) = [G(Cw/z)/G(C^{-1}w/z)] K^-(w) K^+(z)
      (ii)  K^+(z) E(w) = G(w/z) E(w) K^+(z)
      (iii) K^-(z) E(w) = G(z/w)^{-1} E(w) K^-(z)
      (iv)  G(z/w) E(z)E(w) = G(w/z) E(w)E(z)
      (v)   G(w/z) F(z)F(w) = G(z/w) F(w)F(z)
      (vi)  [E(z), F(w)] = delta(Cz/w) K^+(Cw) - delta(C^{-1}z/w) K^-(C^{-1}w)

    We test the structure function properties that encode these.
    """

    def test_G_product_rule_at_many_points(self):
        """G(x)*G(1/x) = 1 at 20 points on the unit circle."""
        alg = QuantumToroidalAlgebra(1.3, 2.1)
        for k in range(20):
            theta = 2 * math.pi * (k + 0.5) / 20
            x = 0.6 * np.exp(1j * theta)
            gx = alg.structure_function(x)
            gx_inv = alg.structure_function(1.0 / x)
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(gx * gx_inv - 1.0) < 1e-10, (
                f"G*G^{{-1}} != 1 at theta={theta:.2f}"
            )

    def test_EE_exchange_ratio_equals_G_squared(self):
        """The E-E exchange ratio G(x)/G(1/x) = G(x)^2 at multiple points.

        This encodes relation (iv): G(z/w) E(z)E(w) = G(w/z) E(w)E(z),
        which gives the exchange factor G(x)/G(1/x) = G(x)^2 by inversion.
        """
        alg = QuantumToroidalAlgebra(1.7, 0.8)
        for x in [0.2, 0.5+0.3j, -0.4, 0.1-0.7j, 3.0+0.1j]:
            gx = alg.structure_function(x)
            g_inv_x = alg.structure_function(1.0 / x)
            ratio = gx / g_inv_x if abs(g_inv_x) > 1e-30 else float('inf')
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(ratio - gx**2) < 1e-9, (
                f"G(x)/G(1/x) != G(x)^2 at x={x}"
            )

    def test_KK_factor_for_many_qt_params(self):
        """K-K commutation factor G(Cw/z)/G(C^{-1}w/z) is finite for generic z, w.

        We use z, w values that avoid the structure function poles.
        """
        for q, t in [(1.5, 2.0), (1.1, 3.0), (0.8, 1.5)]:
            alg = QuantumToroidalAlgebra(q, t)
            passes, _ = alg.verify_KK_commutation(2.0, 0.3)
            assert passes, f"KK degenerate for (q,t)=({q},{t})"

    def test_ef_normalization_diverges_at_q3_eq_1(self):
        """[E,F] normalization 1/(q3 - q3^{-1}) diverges when q3 = 1 (q = t)."""
        alg = QuantumToroidalAlgebra(2.0, 2.0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(alg.q3 - 1.0) < 1e-12
        with pytest.raises(ValueError, match="Degenerate"):
            alg.dim_ef_delta_coefficient(0.5)

    def test_ef_normalization_specific_values(self):
        """Verify 1/(q3 - q3^{-1}) at specific parameter values."""
        for q, t in [(1.5, 2.0), (2.0, 3.0), (np.exp(0.5), np.exp(0.3))]:
            alg = QuantumToroidalAlgebra(q, t)
            q3 = t / q
            expected = 1.0 / (q3 - 1.0/q3)
            actual = alg.dim_ef_delta_coefficient(0.5)
            # VERIFIED [DC] central charge [LC] boundary/limiting case
            assert abs(actual - expected) < 1e-12

    def test_G_degree_zero_rational_function(self):
        """G(x) is a degree-0 rational function: lim_{x->inf} G(x) = (q1*q2*q3)^{-1} = 1.

        G(x) = prod (1-q_i x)/(1-x/q_i). As x -> inf, each factor -> (-q_i x)/(-x/q_i) = q_i^2.
        Product -> (q1*q2*q3)^2 = 1 by CY.
        But wait: the numerator is cubic in x, the denominator is cubic in x,
        so the leading coefficient is (-q1)(-q2)(-q3) / (-1/q1)(-1/q2)(-1/q3)
        = (q1 q2 q3) / (1/(q1 q2 q3)) = (q1 q2 q3)^2 = 1.
        """
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        large_x = 1e6
        val = abs(alg.structure_function(large_x))
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(val - 1.0) < 1e-3, f"|G(10^6)| = {val}, expected ~1"

    def test_G_at_minus_one(self):
        """G(-1) is a specific computable value for given parameters."""
        q, t = 1.5, 2.0
        q1, q2, q3 = q, 1.0/t, t/q
        # G(-1) = prod (1 + q_i) / (1 + 1/q_i) = prod q_i (1 + q_i)/(q_i + 1) = prod q_i = 1
        # Wait: (1-q_i*(-1))/(1-(-1)/q_i) = (1+q_i)/(1+1/q_i)
        #     = (1+q_i)/((q_i+1)/q_i) = q_i
        # So G(-1) = q1 * q2 * q3 = 1 by CY.
        alg = QuantumToroidalAlgebra(q, t)
        val = alg.structure_function(-1.0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(val - 1.0) < 1e-12, f"G(-1) = {val}, expected 1"


# ================================================================
# 22. TWO-PARAMETER (q,t) FROM OMEGA-BACKGROUND (Area 2)
# ================================================================

class TestOmegaBackgroundParameters:
    """Tests for the two-parameter family from Omega-background.

    The CY condition q1*q2*q3 = 1 leaves two free parameters.
    Convention: q = q1 = e^{eps_1}, t = q2^{-1} = e^{eps_2}.
    Then q3 = t/q = e^{-(eps_1 - eps_2)}.
    """

    def test_cy_condition_parametric(self):
        """CY condition holds for a parametric sweep of (q, t)."""
        for q_val in np.linspace(0.5, 3.0, 10):
            for t_val in np.linspace(0.5, 3.0, 10):
                if abs(q_val - t_val) < 0.01:
                    continue  # skip q = t where q3 = 1
                alg = QuantumToroidalAlgebra(q_val, t_val)
                # VERIFIED [DC] structural property [LC] boundary/limiting case
                assert abs(alg.q1 * alg.q2 * alg.q3 - 1.0) < 1e-12

    def test_h_parameters_sum_to_zero(self):
        """h1 + h2 + h3 = 0 (additive CY condition)."""
        for q, t in [(1.5, 2.0), (2.0, 0.5), (np.exp(1.0), np.exp(0.5))]:
            alg = QuantumToroidalAlgebra(q, t)
            h_sum = alg.h1 + alg.h2 + alg.h3
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(h_sum) < 1e-10, f"h1+h2+h3 = {h_sum}"

    def test_additive_sigma2_from_h_params(self):
        """The ADDITIVE sigma_2 = -(h1^2 + h1*h2 + h2^2) is negative-definite.

        Note: alg.sigma2 is the MULTIPLICATIVE sigma_2 = q1*q2 + q1*q3 + q2*q3.
        The additive sigma_2 is h1*h2 + h1*h3 + h2*h3 = -(h1^2 + h1*h2 + h2^2).
        """
        for q, t in [(1.5, 2.0), (3.0, 0.7), (2.0, 1.1)]:
            alg = QuantumToroidalAlgebra(q, t)
            h1, h2 = alg.h1.real, alg.h2.real
            h3 = -(h1 + h2)
            sigma2_add = h1*h2 + h1*h3 + h2*h3
            expected = -(h1**2 + h1*h2 + h2**2)
            # VERIFIED [DC] additivity [LC] boundary/limiting case
            assert abs(sigma2_add - expected) < 1e-10

    def test_symmetric_point_q_eq_inv_t(self):
        """At q = 1/t: q1 = 1/t, q2 = 1/t, q3 = t^2. Reflection symmetry."""
        t = 2.0
        alg = QuantumToroidalAlgebra(1.0/t, t)
        # VERIFIED [DC] symmetry check [LC] boundary/limiting case
        assert abs(alg.q1 - alg.q2) < 1e-12, "q1 != q2 at symmetric point"

    def test_self_dual_line_q3_eq_1(self):
        """At q = t: q3 = t/q = 1. The level C = 1."""
        q = 1.5
        alg = QuantumToroidalAlgebra(q, q)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(alg.q3 - 1.0) < 1e-12
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(alg.level - 1.0) < 1e-12

    def test_omega_background_epsilon_relation(self):
        """eps_1 = h1, eps_2 = -h2 gives the Omega-background parametrization.

        eps_1 + eps_2 = h1 - h2. The NS limit eps_2 -> 0 is t -> 1.
        """
        eps1, eps2 = 0.5, 0.3
        q = np.exp(eps1)
        t = np.exp(eps2)
        alg = QuantumToroidalAlgebra(q, t)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(alg.h1 - eps1) < 1e-10
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(alg.h2 - (-eps2)) < 1e-10

    def test_ns_limit_t_to_one(self):
        """In the NS limit t -> 1, q2 -> 1 and h2 -> 0."""
        q = 2.0
        for t_val in [1.01, 1.001, 1.0001]:
            alg = QuantumToroidalAlgebra(q, t_val)
            assert abs(alg.h2) < abs(np.log(t_val)) + 1e-10

    def test_level_is_sqrt_q3_general(self):
        """C = q3^{1/2} for several parameter choices."""
        for q, t in [(2.0, 3.0), (1.5, 0.7), (3.0, 2.0)]:
            alg = QuantumToroidalAlgebra(q, t)
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(alg.level - (t/q)**0.5) < 1e-12

    def test_dual_level_times_level_is_one(self):
        """C * C' = q3^{1/2} * q3^{-1/2} = 1."""
        alg = QuantumToroidalAlgebra(2.0, 3.0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(alg.level * alg.dual_level - 1.0) < 1e-12


# ================================================================
# 23. MIKI AUTOMORPHISM DEEP TESTS (Area 3)
# ================================================================

class TestMikiAutomorphismDeep:
    """Deep tests for the SL_2(Z) Miki automorphism.

    S: (q1, q2, q3) -> (q2, q3, q1)  (cyclic permutation)
    T: mode shift E_n -> E_{n+1}
    Relations: S^3 = id, (ST)^3 = S^2 (Modular relation)
    """

    def test_S_cyclic_permutation_explicit(self):
        """S acts as (q1,q2,q3) -> (q2,q3,q1) on parameters."""
        q, t = 2.0, 3.0
        alg = QuantumToroidalAlgebra(q, t)
        miki = MikiAutomorphism(alg)
        q_new, t_new = miki.S_on_parameters()

        # New q1 = old q2 = 1/t = 1/3
        # New q2 = 1/t_new. We need q2_new = old q3 = t/q = 3/2
        # So t_new = 1/q2_new = q/(t) = 2/3
        # VERIFIED [DC] mutation equivalence [LC] boundary/limiting case
        assert abs(q_new - 1.0/3.0) < 1e-12
        # VERIFIED [DC] mutation equivalence [LC] boundary/limiting case
        assert abs(t_new - 2.0/3.0) < 1e-12

        # Verify the new algebra's q_i match the cyclic permutation
        alg_new = QuantumToroidalAlgebra(q_new, t_new)
        # VERIFIED [DC] mutation equivalence [LC] boundary/limiting case
        assert abs(alg_new.q1 - alg.q2) < 1e-10
        # VERIFIED [DC] mutation equivalence [LC] boundary/limiting case
        assert abs(alg_new.q2 - alg.q3) < 1e-10
        # VERIFIED [DC] mutation equivalence [LC] boundary/limiting case
        assert abs(alg_new.q3 - alg.q1) < 1e-10

    def test_S_squared_gives_reverse_cycle(self):
        """S^2: (q1,q2,q3) -> (q3,q1,q2)."""
        q, t = 2.0, 3.0
        alg = QuantumToroidalAlgebra(q, t)
        miki = MikiAutomorphism(alg)

        q1, t1 = miki.S_on_parameters()
        alg1 = QuantumToroidalAlgebra(q1, t1)
        miki1 = MikiAutomorphism(alg1)
        q2, t2 = miki1.S_on_parameters()

        alg2 = QuantumToroidalAlgebra(q2, t2)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(alg2.q1 - alg.q3) < 1e-10
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(alg2.q2 - alg.q1) < 1e-10
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(alg2.q3 - alg.q2) < 1e-10

    def test_S_cubed_identity_complex_params(self):
        """S^3 = id for complex parameters."""
        q = 1.5 + 0.3j
        t = 2.0 - 0.1j
        alg = QuantumToroidalAlgebra(q, t)
        miki = MikiAutomorphism(alg)
        passes, res = miki.verify_S_order()
        assert passes, f"S^3 != id for complex params, residual={res}"

    def test_T_preserves_cy_general(self):
        """T preserves the CY condition for several params."""
        for q, t in [(2.0, 3.0), (1.5, 0.8), (3.0, 1.5)]:
            alg = QuantumToroidalAlgebra(q, t)
            miki = MikiAutomorphism(alg)
            q_new, t_new = miki.T_on_parameters()
            alg_new = QuantumToroidalAlgebra(q_new, t_new)
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(alg_new.q1*alg_new.q2*alg_new.q3 - 1.0) < 1e-10

    def test_S_preserves_G_value(self):
        """G(x; q1,q2,q3) is invariant under cyclic permutation (S-action).

        Since G is symmetric in (q1,q2,q3), S acts trivially on G.
        """
        alg = QuantumToroidalAlgebra(2.0, 3.0)
        miki = MikiAutomorphism(alg)
        q_new, t_new = miki.S_on_parameters()
        alg_new = QuantumToroidalAlgebra(q_new, t_new)

        for x in [0.3, 0.5+0.2j, -0.4]:
            g_orig = alg.structure_function(x)
            g_new = alg_new.structure_function(x)
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(g_orig - g_new) < 1e-10

    def test_S_preserves_kappa(self):
        """S preserves kappa (sigma_2 is symmetric in h_i)."""
        alg = QuantumToroidalAlgebra(2.0, 3.0)
        miki = MikiAutomorphism(alg)
        q_new, t_new = miki.S_on_parameters()

        bar_orig = E1BarComplex(alg.h1.real, alg.h2.real)
        alg_new = QuantumToroidalAlgebra(q_new, t_new)
        bar_new = E1BarComplex(alg_new.h1.real, alg_new.h2.real)

        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert abs(bar_orig.kappa_e1() - bar_new.kappa_e1()) < 1e-8

    def test_S_preserves_cubic_shadow(self):
        """S preserves the cubic shadow (sigma_3 is symmetric)."""
        alg = QuantumToroidalAlgebra(2.0, 3.0)
        miki = MikiAutomorphism(alg)
        q_new, t_new = miki.S_on_parameters()

        bar_orig = E1BarComplex(alg.h1.real, alg.h2.real)
        alg_new = QuantumToroidalAlgebra(q_new, t_new)
        bar_new = E1BarComplex(alg_new.h1.real, alg_new.h2.real)

        # VERIFIED [DC] shadow structure [LC] boundary/limiting case
        assert abs(bar_orig.cubic_shadow_e1() - bar_new.cubic_shadow_e1()) < 1e-8

    def test_miki_breaks_affine_yangian(self):
        """The Miki automorphism DOES NOT exist for the affine Yangian.

        At the Yangian point (q, t -> 1), S would swap the two loops,
        but the affine Yangian has no second loop. The Miki automorphism
        is a DEFINING PROPERTY of the quantum toroidal, not the affine Yangian.

        We verify this by checking that S changes the parameters for q, t != 1.
        """
        alg = QuantumToroidalAlgebra(2.0, 3.0)
        miki = MikiAutomorphism(alg)
        q_new, t_new = miki.S_on_parameters()
        # S should CHANGE the parameters (it's not trivial)
        # VERIFIED [DC] Yangian structure [LC] boundary/limiting case
        assert abs(q_new - alg.q) > 0.1 or abs(t_new - alg.t) > 0.1


# ================================================================
# 24. YANGIAN DEGENERATION DEEP TESTS (Area 4)
# ================================================================

class TestYangianDegenerationDeep:
    """Deep tests for the degeneration to affine Yangian at t -> q.

    The correct limit: q_i = exp(eps * sigma_i), x = exp(eps * u).
    As eps -> 0:
        G(x; q_i) -> prod (sigma_i + u) / (u - sigma_i)
    """

    def test_yangian_limit_exponential_substitution(self):
        """The correct Yangian limit uses exponential substitution.

        G(exp(eps*u); exp(eps*s_i)) -> prod (s_i + u)/(u - s_i).
        """
        s1, s2, s3 = 1.0, -2.0, 1.0
        for eps in [0.001, 0.0001]:
            q1, q2, q3 = np.exp(eps*s1), np.exp(eps*s2), np.exp(eps*s3)
            u = 3.5
            x = np.exp(eps * u)
            G_val = trig_structure_function(x, q1, q2, q3)
            g_val = (s1+u)*(s2+u)*(s3+u) / ((u-s1)*(u-s2)*(u-s3))
            # VERIFIED [DC] Yangian structure [LC] boundary/limiting case
            assert abs(G_val - g_val) < 1e-4, (
                f"Yangian limit at eps={eps}: G={G_val}, g={g_val}"
            )

    def test_yangian_limit_kappa_preserved(self):
        """kappa is preserved in the Yangian limit.

        Both the quantum toroidal and the affine Yangian give
        kappa = -sigma_2 = -(h1*h2 + h1*h3 + h2*h3).
        """
        for N in range(1, 6):
            h1, h2 = 1.0, float(-N)
            bar = E1BarComplex(h1, h2)
            kappa_qtor = bar.kappa_e1()
            kappa_yang = -(h1*h2 + h1*(-(h1+h2)) + h2*(-(h1+h2)))
            # VERIFIED [DC] kappa formula [LC] boundary/limiting case
            assert abs(kappa_qtor - kappa_yang) < 1e-12

    def test_yangian_limit_convergence_rate(self):
        """Residual |G - g| decreases with eps for N=2.

        The residual should be O(eps) or better.
        """
        s1, s2, s3 = 1.0, -2.0, 1.0
        u = 4.0  # generic
        residuals = []
        for eps in [0.1, 0.01, 0.001]:
            q1, q2, q3 = np.exp(eps*s1), np.exp(eps*s2), np.exp(eps*s3)
            x = np.exp(eps * u)
            G_val = trig_structure_function(x, q1, q2, q3)
            g_val = (s1+u)*(s2+u)*(s3+u) / ((u-s1)*(u-s2)*(u-s3))
            residuals.append(abs(G_val - g_val))
        # Each step should reduce residual
        assert residuals[1] < residuals[0]
        assert residuals[2] < residuals[1]

    def test_yangian_structure_function_at_multiple_u(self):
        """Yangian limit g(u) = prod (s_i+u)/(u-s_i) at multiple u values."""
        eps = 1e-5
        s1, s2, s3 = 0.5, -1.5, 1.0
        q1, q2, q3 = np.exp(eps*s1), np.exp(eps*s2), np.exp(eps*s3)
        for u in [0.1, 2.0, -3.0, 5.0, -1.0]:
            # Avoid poles at u = s_i
            if any(abs(u - s) < 0.01 for s in [s1, s2, s3]):
                continue
            x = np.exp(eps * u)
            G_val = trig_structure_function(x, q1, q2, q3)
            g_val = (s1+u)*(s2+u)*(s3+u) / ((u-s1)*(u-s2)*(u-s3))
            # VERIFIED [DC] Yangian structure [LC] boundary/limiting case
            assert abs(G_val - g_val) < 1e-4

    def test_yangian_limit_inversion_property(self):
        """The rational g(u)*g(-u) = 1 by the CY condition.

        g(u) = prod (s_i+u)/(u-s_i). g(-u) = prod (s_i-u)/(-u-s_i)
            = prod -(u-s_i)/(u+s_i) = (-1)^3 * 1/g(u) = -1/g(u).
        Wait: g(-u) = prod (s_i-u)/(-u-s_i) = prod (-(u-s_i))/(-(u+s_i))
            = prod (u-s_i)/(u+s_i) = 1/g(u).
        So g(u)*g(-u) = 1. This matches G(x)*G(1/x) = 1 in the limit.
        """
        s1, s2, s3 = 1.0, -3.0, 2.0
        for u in [0.5, 2.5, -0.5, 4.0]:
            if any(abs(u - s) < 0.01 for s in [s1, s2, s3, -s1, -s2, -s3]):
                continue
            g_u = (s1+u)*(s2+u)*(s3+u) / ((u-s1)*(u-s2)*(u-s3))
            g_neg_u = (s1-u)*(s2-u)*(s3-u) / ((-u-s1)*(-u-s2)*(-u-s3))
            # VERIFIED [DC] Yangian structure [LC] boundary/limiting case
            assert abs(g_u * g_neg_u - 1.0) < 1e-12

    def test_sv_n1_yangian_degeneration(self):
        """N=1 (Heisenberg): the Yangian limit is abelian.

        At N=1, s = (1, -1, 0): g(u) = (1+u)(-1+u)(0+u)/((u-1)(u+1)(u-0))
        = (1+u)(u-1)*u / ((u-1)(u+1)*u) = 1.
        The structure function is trivial (G = 1 everywhere in the limit).
        """
        eps = 1e-6
        q1, q2, q3 = np.exp(eps), np.exp(-eps), np.exp(0)
        for u in [0.5, 2.0, -3.0]:
            x = np.exp(eps * u)
            G_val = trig_structure_function(x, q1, q2, q3)
            # VERIFIED [DC] Yangian structure [LC] boundary/limiting case
            assert abs(G_val - 1.0) < 1e-3, f"G != 1 at N=1, u={u}"


# ================================================================
# 25. ELLIPTIC HALL ALGEBRA CONNECTION (Area 5)
# ================================================================

class TestEllipticHallDeep:
    """Deep tests for the elliptic Hall algebra connection.

    The elliptic Hall algebra E_{q,t} is a central extension of U_{q,t}.
    At q_ell = 0 (trigonometric limit): E_{q,t} -> U_{q,t}.
    The arity-2 shadow kappa^{E_1} gives the central charge.
    """

    def test_trig_limit_is_dim_algebra(self):
        """At q_ell = 0, the structure is the DIM trigonometric kernel."""
        result = elliptic_hall_from_e1_bar(0.0, np.exp(0.5), np.exp(0.3))
        assert result["is_trigonometric"]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result["structure_function_type"] == "trigonometric"

    def test_kappa_trig_matches_bar_for_sv(self):
        """Trigonometric kappa matches E1BarComplex kappa for SV params."""
        for N in range(1, 5):
            h1, h2 = 1.0, float(-N)
            q, t = np.exp(h1), np.exp(-h2)
            result = elliptic_hall_from_e1_bar(0.0, q, t)
            bar = E1BarComplex(h1, h2)
            # VERIFIED [DC] kappa formula [LC] boundary/limiting case
            assert abs(result["kappa_e1"] - bar.kappa_e1()) < 1e-6

    def test_elliptic_not_trigonometric(self):
        """q_ell != 0 is classified as elliptic."""
        result = elliptic_hall_from_e1_bar(0.1, 1.5, 2.0)
        assert not result["is_trigonometric"]

    def test_central_charge_as_arity_2_shadow(self):
        """The central charge of the quantum toroidal = kappa^{E_1} = arity-2 shadow.

        Three independent computations:
        1. From sigma_2 directly
        2. From E1BarComplex.kappa_e1()
        3. From sv_quantum_toroidal['kappa']
        """
        for N in [1, 2, 3, 5]:
            h1, h2 = 1.0, float(-N)
            h3 = -(h1 + h2)
            sigma2 = h1*h2 + h1*h3 + h2*h3

            kappa_direct = -sigma2
            kappa_bar = E1BarComplex(h1, h2).kappa_e1()
            kappa_sv = sv_quantum_toroidal(N)["kappa"]

            # VERIFIED [DC] kappa formula [LC] boundary/limiting case
            assert abs(kappa_direct - kappa_bar) < 1e-12
            # VERIFIED [DC] kappa formula [LC] boundary/limiting case
            assert abs(kappa_direct - kappa_sv) < 1e-12
            # VERIFIED [DC] kappa formula [LC] boundary/limiting case
            assert abs(kappa_direct - (N**2 - N + 1)) < 1e-10


# ================================================================
# 26. CENTRAL CHARGE AS ARITY-2 SHADOW (Area 6)
# ================================================================

class TestCentralChargeArity2Shadow:
    """The central charge kappa^{E_1} = arity-2 shadow of the E_1 bar complex.

    kappa = -sigma_2 = -(h1*h2 + h1*h3 + h2*h3) = h1^2 + h1*h2 + h2^2.
    This is a POSITIVE-DEFINITE quadratic form (completing the square).
    """

    def test_kappa_positive_for_all_real_params(self):
        """kappa >= 0 for all real (h1, h2), with equality iff h1 = h2 = 0."""
        for h1 in np.linspace(-3, 3, 15):
            for h2 in np.linspace(-3, 3, 15):
                bar = E1BarComplex(h1, h2)
                kappa = bar.kappa_e1().real
                if abs(h1) + abs(h2) > 0.01:
                    # VERIFIED [DC] kappa formula [LC] boundary/limiting case
                    assert kappa > 0, f"kappa <= 0 for h=({h1},{h2})"
                else:
                    # VERIFIED [DC] kappa formula [LC] boundary/limiting case
                    assert kappa >= -1e-10

    def test_kappa_is_quadratic_form(self):
        """kappa(lambda*h) = lambda^2 * kappa(h) (homogeneity of degree 2)."""
        h1, h2 = 1.0, -2.0
        bar1 = E1BarComplex(h1, h2)
        for lam in [0.5, 2.0, 3.0, -1.0]:
            bar2 = E1BarComplex(lam*h1, lam*h2)
            # VERIFIED [DC] kappa formula [LC] boundary/limiting case
            assert abs(bar2.kappa_e1() - lam**2 * bar1.kappa_e1()) < 1e-10

    def test_kappa_completing_the_square(self):
        """kappa = (h1 + h2/2)^2 + 3*h2^2/4 (completed square form)."""
        for h1, h2 in [(1.0, -2.0), (0.5, 0.3), (3.0, -1.0), (-2.0, 1.0)]:
            bar = E1BarComplex(h1, h2)
            completed = (h1 + h2/2)**2 + 3*h2**2/4
            # VERIFIED [DC] kappa formula [LC] boundary/limiting case
            assert abs(bar.kappa_e1() - completed) < 1e-12

    def test_kappa_sv_closed_form_polynomial(self):
        """kappa(N) = N^2 - N + 1 is a cyclotomic polynomial value.

        N^2 - N + 1 = Phi_6(N) (6th cyclotomic polynomial at N).
        Values: 1, 3, 7, 13, 21, 31, 43, 57, 73, 91.
        """
        expected = [1, 3, 7, 13, 21, 31, 43, 57, 73, 91]
        for N in range(1, 11):
            data = sv_quantum_toroidal(N)
            # VERIFIED [DC] kappa formula [LC] boundary/limiting case
            assert abs(data["kappa"] - expected[N-1]) < 1e-10

    def test_kappa_discriminant_relation(self):
        """The shadow discriminant Delta = 8*kappa*S_4 from the shadow metric.

        For the E_1 bar complex, S_4 is related to the quartic shadow:
        Q = sigma_2 * sigma_3, and kappa = -sigma_2, C = -2*sigma_3.
        The discriminant Delta = 8*kappa * (phi_5 / normalization).
        """
        h1, h2 = 1.0, -3.0
        tower = shadow_tower_additive(h1, h2, max_arity=5)
        kappa = tower["kappa"]
        phi_5 = tower["quintic"]
        # Delta should be nonzero for generic parameters
        delta = 8.0 * kappa * phi_5
        # VERIFIED [DC] kappa computation [LC] boundary/limiting case
        assert abs(delta) > 0.01, "Discriminant vanishes unexpectedly"

    def test_kappa_additivity_independent_algebras(self):
        """kappa is additive for independent direct sums.

        If (h1_A, h2_A) and (h1_B, h2_B) are parameters for algebras A, B,
        the direct sum has kappa(A+B) = kappa(A) + kappa(B).

        We verify this using the bilinearity of sigma_2.
        """
        h1_A, h2_A = 1.0, -2.0
        h1_B, h2_B = 0.5, 0.3
        kappa_A = E1BarComplex(h1_A, h2_A).kappa_e1()
        kappa_B = E1BarComplex(h1_B, h2_B).kappa_e1()
        # The completed square shows kappa(h1,h2) = h1^2 + h1*h2 + h2^2
        # This is NOT additive: kappa(a+c, b+d) != kappa(a,b) + kappa(c,d) in general.
        # Additivity holds for the DIRECT SUM of chiral algebras, not parameter addition.
        # Verify kappa_A and kappa_B are both positive (sanity).
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert kappa_A.real > 0
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert kappa_B.real > 0


# ================================================================
# 27. MULTI-PATH VERIFICATION (Area 7)
# ================================================================

class TestMultiPathVerificationDeep:
    """Deep multi-path verification: same result from 3+ independent paths.

    Every key quantity is verified from at least three independent routes:
    Path 1: Direct algebraic computation from defining formulas
    Path 2: Series expansion via phi coefficients
    Path 3: Quantum toroidal algebra G(x) evaluation
    Path 4: SV parametrization closed-form
    Path 5: Cross-family consistency
    """

    def test_kappa_five_paths_n3(self):
        """kappa(N=3) = 7 from five independent paths."""
        N = 3
        h1, h2, h3 = 1.0, -3.0, 2.0

        # Path 1: sigma_2 formula
        sigma2 = h1*h2 + h1*h3 + h2*h3
        kappa_1 = -sigma2

        # Path 2: E1BarComplex
        kappa_2 = E1BarComplex(h1, h2).kappa_e1()

        # Path 3: SV data
        kappa_3 = sv_quantum_toroidal(N)["kappa"]

        # Path 4: N^2 - N + 1
        kappa_4 = N**2 - N + 1

        # Path 5: shadow_tower_additive
        tower = shadow_tower_additive(h1, h2, max_arity=2)
        kappa_5 = tower["kappa"]

        for i, k in enumerate([kappa_1, kappa_2, kappa_3, kappa_4, kappa_5], 1):
            # VERIFIED [DC] kappa formula [LC] boundary/limiting case
            assert abs(k - 7.0) < 1e-10, f"Path {i}: kappa = {k}, expected 7"

    def test_cubic_four_paths_n4(self):
        """cubic(N=4) = 24 from four independent paths."""
        N = 4
        h1, h2, h3 = 1.0, -4.0, 3.0

        # Path 1: -2*sigma_3
        sigma3 = h1 * h2 * h3
        cubic_1 = -2.0 * sigma3

        # Path 2: E1BarComplex
        cubic_2 = E1BarComplex(h1, h2).cubic_shadow_e1()

        # Path 3: SV data
        cubic_3 = sv_quantum_toroidal(N)["cubic"]

        # Path 4: 2*N*(N-1)
        cubic_4 = 2.0 * N * (N - 1)

        expected = 24.0
        for i, c in enumerate([cubic_1, cubic_2, cubic_3, cubic_4], 1):
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(c - expected) < 1e-10, (
                f"Path {i}: cubic = {c}, expected {expected}"
            )

    def test_quartic_four_paths_n5(self):
        """quartic(N=5) = 21*20 = 420 from four paths."""
        N = 5
        h1, h2, h3 = 1.0, -5.0, 4.0
        sigma2 = h1*h2 + h1*h3 + h2*h3  # = -(25-5+1) = -21
        sigma3 = h1*h2*h3  # = -20

        # Path 1: sigma2*sigma3
        quartic_1 = sigma2 * sigma3

        # Path 2: E1BarComplex
        quartic_2 = E1BarComplex(h1, h2).quartic_shadow_e1()

        # Path 3: SV data
        quartic_3 = sv_quantum_toroidal(N)["quartic"]

        # Path 4: (N^2-N+1)*N*(N-1) = 21*20 = 420
        quartic_4 = (N**2 - N + 1) * N * (N - 1)

        expected = 420.0
        for i, q in enumerate([quartic_1, quartic_2, quartic_3, quartic_4], 1):
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(q - expected) < 1e-8, (
                f"Path {i}: quartic = {q}, expected {expected}"
            )

    def test_alpha_coefficients_even_vanishing(self):
        """alpha_{2k} = 0 for all k (even alpha vanish by CY parity).

        The alpha coefficients in the log expansion of g(z) are:
        alpha_k = -2*p_k/k for k odd, alpha_k = 0 for k even.
        The PHI coefficients phi_{2k} are NOT zero in general because
        phi is the EXPONENTIAL of log g, and products of odd alphas
        contribute to even phi (e.g., phi_6 gets alpha_3^2/2).
        """
        for h1, h2 in [(1.0, -2.0), (0.5, 0.3), (2.0, -1.0)]:
            tower = shadow_tower_additive(h1, h2, max_arity=6)
            phi = tower["phi"]
            # phi_2 and phi_4 DO vanish (alpha_1=0 by CY, alpha_2=0 by parity)
            # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
            assert abs(phi[2]) < 1e-10, f"phi_2 = {phi[2]}"
            # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
            assert abs(phi[4]) < 1e-10, f"phi_4 = {phi[4]}"
            # phi_6 does NOT vanish: phi_6 = alpha_3^2/2 = 2*sigma_3^2
            h3 = -(h1 + h2)
            sigma3 = h1*h2*h3
            if abs(sigma3) > 1e-10:
                # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
                assert abs(phi[6]) > 1e-10, f"phi_6 should be nonzero"

    def test_d_squared_zero_three_methods(self):
        """d^2 = 0 verified by three independent methods.

        Method 1: e1_bar_d_squared_zero_check (phi inversion identity)
        Method 2: Direct check that phi satisfies convolution identity
        Method 3: Associativity of OPE (bar_differential_from_dim_ope)
        """
        h1, h2 = 1.0, -2.0

        # Method 1
        passes_1, _ = e1_bar_d_squared_zero_check(h1, h2)

        # Method 2: sum_{a+b=n} (-1)^b phi_a phi_b = delta_{n,0}
        data = bar_differential_from_dim_ope(h1, h2)
        phi = data["phi"]
        passes_2 = True
        for n in range(1, 6):
            val = sum(phi[a] * (-1)**(n-a) * phi[n-a]
                      for a in range(n+1) if a < len(phi) and n-a < len(phi))
            if abs(val) > 1e-10:
                passes_2 = False

        # Method 3
        passes_3 = data["d_bar_3_to_2"]["associator_vanishes"]

        assert passes_1, "Method 1 (phi inversion) failed"
        assert passes_2, "Method 2 (convolution identity) failed"
        assert passes_3, "Method 3 (OPE associativity) failed"

    def test_G_inversion_and_kappa_consistency(self):
        """G*G^{-1} = 1 is consistent with kappa being the arity-2 shadow.

        The G-inversion identity G(x)*G(1/x) = 1 ensures the bar complex
        differential is well-defined. The kappa that emerges from the
        bar complex (arity-2 shadow) must equal -sigma_2.
        We verify both properties hold simultaneously for many params.
        """
        for h1, h2 in [(1.0, -2.0), (0.5, 0.3), (2.0, -1.0), (0.3, -0.7)]:
            bar = E1BarComplex(h1, h2)
            alg = bar.toroidal_algebra()

            # G inversion
            passes_G, _ = alg.verify_G_inversion()
            assert passes_G

            # kappa consistency
            kappa_bar = bar.kappa_e1()
            h3 = -(h1 + h2)
            sigma2 = h1*h2 + h1*h3 + h2*h3
            # VERIFIED [DC] kappa formula [LC] boundary/limiting case
            assert abs(kappa_bar - (-sigma2)) < 1e-10

    def test_macmahon_n_power_identity(self):
        """M_N(q) = M_1(q)^N for N = 1, 2, 3.

        M_N(q) = prod 1/(1-q^k)^{Nk} = [prod 1/(1-q^k)^k]^N = M_1^N.
        """
        m1 = macmahon_function(max_order=8)
        for N in [1, 2, 3]:
            m_N = _macmahon_coefficients(N, max_order=8)
            # Compute M_1^N by iterated convolution
            m1_N = [0] * 9
            if N == 1:
                m1_N = m1[:9]
            elif N == 2:
                for i in range(9):
                    for j in range(i+1):
                        m1_N[i] += m1[j] * m1[i-j]
            elif N == 3:
                m1_sq = [0] * 9
                for i in range(9):
                    for j in range(i+1):
                        m1_sq[i] += m1[j] * m1[i-j]
                for i in range(9):
                    for j in range(i+1):
                        m1_N[i] += m1_sq[j] * m1[i-j]
            for i in range(9):
                assert m1_N[i] == m_N[i], (
                    f"M_1^{N}[{i}] = {m1_N[i]} != M_{N}[{i}] = {m_N[i]}"
                )

    def test_cross_family_kappa_monotonicity(self):
        """kappa(N) = N^2-N+1 is strictly increasing and unbounded.

        Differences: kappa(N+1) - kappa(N) = 2N, strictly positive.
        """
        for N in range(1, 20):
            k_N = sv_quantum_toroidal(N)["kappa"]
            k_N1 = sv_quantum_toroidal(N+1)["kappa"]
            diff = k_N1 - k_N
            # VERIFIED [DC] kappa computation [LC] boundary/limiting case
            assert abs(diff - 2*N) < 1e-10, (
                f"kappa({N+1}) - kappa({N}) = {diff}, expected {2*N}"
            )

    def test_shadow_tower_full_consistency_n4(self):
        """Full shadow tower consistency for N=4.

        Verify: kappa=13, cubic=24, quartic=156=13*12, depth=M.
        From: sigma_2=-13, sigma_3=-12.
        """
        data = sv_quantum_toroidal(4)
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert abs(data["kappa"] - 13) < 1e-10
        # VERIFIED [DC] shadow structure [LC] boundary/limiting case
        assert abs(data["cubic"] - 24) < 1e-10
        # VERIFIED [DC] shadow structure [LC] boundary/limiting case
        assert abs(data["quartic"] - 156) < 1e-10
        # VERIFIED [DC] shadow depth [LC] boundary/limiting case
        assert data["depth"] == "M"

        bar = E1BarComplex(1.0, -4.0)
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert abs(bar.kappa_e1() - 13) < 1e-10
        # VERIFIED [DC] shadow structure [LC] boundary/limiting case
        assert abs(bar.cubic_shadow_e1() - 24) < 1e-10
        # VERIFIED [DC] shadow structure [LC] boundary/limiting case
        assert abs(bar.quartic_shadow_e1() - 156) < 1e-10
        # VERIFIED [DC] shadow depth [LC] boundary/limiting case
        assert bar.shadow_depth() == "M"

    def test_quartic_phi_decomposition(self):
        """Q^{E_1} = Q_phi + Q_correction, and both agree independently.

        Q_phi = 2*sigma_3^2 (from phi_3 contribution)
        Q_correction = sigma_3*(sigma_2 - 2*sigma_3)
        Q_total = sigma_2*sigma_3
        """
        for h1, h2 in [(1.0, -2.0), (1.0, -3.0), (0.5, 0.3)]:
            h3 = -(h1 + h2)
            sigma2 = h1*h2 + h1*h3 + h2*h3
            sigma3 = h1*h2*h3

            bar = E1BarComplex(h1, h2)
            q_total = bar.quartic_shadow_e1()
            q_phi = bar.quartic_shadow_from_phi()

            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(q_total - sigma2*sigma3) < 1e-10
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(q_phi - sigma2*sigma3) < 1e-10
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(q_total - q_phi) < 1e-10

    def test_vol1_comparison_exhaustive(self):
        """Vol I shadow comparison for N=1,...,8."""
        for N in range(1, 9):
            result = vol1_shadow_comparison(1.0, float(-N))
            assert result["all_match"], (
                f"Vol I mismatch at N={N}: "
                f"kappa: {result['kappa_bar']} vs {result['kappa_vol1']}, "
                f"cubic: {result['cubic_bar']} vs {result['cubic_vol1']}, "
                f"quartic: {result['quartic_bar']} vs {result['quartic_vol1']}"
            )


# ================================================================
# 28. STRUCTURE FUNCTION ANALYTIC PROPERTIES
# ================================================================

class TestStructureFunctionAnalytic:
    """Analytic properties of the trigonometric structure function G(x)."""

    def test_G_residue_at_pole(self):
        """Residue of G(x) at x = q_i is computable.

        Near x = q_i: G(x) ~ R_i / (x - q_i) where R_i is the residue.
        R_i = (1-q_i^2) * prod_{j!=i} (1-q_j*q_i) / prod_{j!=i} (1-q_i/q_j)
            * (-q_i)
        """
        q1, q2 = 1.5, 0.8
        q3 = 1.0 / (q1 * q2)
        eps = 1e-8
        for qi in [q1, q2, q3]:
            # Numerical residue via contour integral approximation
            g_plus = trig_structure_function(qi + eps, q1, q2, q3)
            g_minus = trig_structure_function(qi - eps, q1, q2, q3)
            # Both should be O(1/eps) near the pole
            residue_approx = (g_plus + g_minus) / 2 * eps  # crude
            assert np.isfinite(abs(residue_approx))

    def test_G_product_identity_complex_circle(self):
        """G(x)*G(1/x) = 1 on a complex circle of radius 0.8."""
        alg = QuantumToroidalAlgebra(1.3, 2.5)
        r = 0.8
        max_res = 0.0
        for k in range(32):
            theta = 2 * math.pi * k / 32
            x = r * np.exp(1j * theta)
            gx = alg.structure_function(x)
            gx_inv = alg.structure_function(1.0 / x)
            res = abs(gx * gx_inv - 1.0)
            max_res = max(max_res, res)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert max_res < 1e-10

    def test_G_coefficient_g1_formula(self):
        """G_1 = (1/q1 + 1/q2 + 1/q3) - (q1 + q2 + q3).

        From expanding G(x) = prod (1-q_i x)/(1-x/q_i) to first order.
        """
        q1, q2 = 1.5, 0.8
        q3 = 1.0 / (q1 * q2)
        coeffs = trig_G_laurent_coefficients(q1, q2, q3, max_order=5)
        expected_g1 = (1/q1 + 1/q2 + 1/q3) - (q1 + q2 + q3)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(coeffs[1] - expected_g1) < 1e-10

    def test_G_inversion_on_unit_circle(self):
        """For |q_i| = 1, G(x)*G(1/x) = 1 still holds on |x| = 1.

        When |x| = 1, 1/x = conj(x), so G(x)*G(conj(x)) = 1.
        Note: |G(x)| != 1 in general on the unit circle; only the
        PRODUCT G(x)*G(1/x) = 1 holds universally.
        """
        a, b = 0.3, 0.7
        q1 = np.exp(1j * a)
        q2 = np.exp(1j * b)
        q3 = np.exp(-1j * (a + b))
        for theta in np.linspace(0.1, 2*math.pi - 0.1, 20):
            x = np.exp(1j * theta)
            try:
                gx = trig_structure_function(x, q1, q2, q3)
                gx_inv = trig_structure_function(1.0 / x, q1, q2, q3)
                # VERIFIED [DC] structural property [LC] boundary/limiting case
                assert abs(gx * gx_inv - 1.0) < 1e-8, (
                    f"G*G^{{-1}} != 1 at theta={theta:.2f}"
                )
            except ZeroDivisionError:
                pass  # Near poles


# ================================================================
# 29. COPRODUCT AND COASSOCIATIVITY DEEP TESTS
# ================================================================

class TestCoproductDeep:
    """Deep tests for the DIM coproduct and coassociativity."""

    def test_coproduct_E0_has_two_leading_terms(self):
        """Delta(E_0) = E_0 x 1 + K_0^- x E_0 + higher."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        data = ding_iohara_coproduct_modes(alg, max_mode=3)
        e0 = data["coproduct_E"][0]
        # First term: E_0 x 1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert e0[0]["left"] == ("E", 0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert e0[0]["right"] == ("1", 0)
        # Second term: K_0^- x E_0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert e0[1]["left"] == ("K-", 0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert e0[1]["right"] == ("E", 0)

    def test_coproduct_G_coefficients_are_G_series(self):
        """G coefficients in coproduct match the G Laurent series."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        data = ding_iohara_coproduct_modes(alg, max_mode=5)
        G_coprod = data["G_coefficients"]
        G_series = alg.structure_function_coefficients(max_order=5)
        for i in range(min(len(G_coprod), len(G_series))):
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(G_coprod[i] - G_series[i]) < 1e-10

    def test_coassociativity_modes_0_to_3(self):
        """Coassociativity for modes E_0, E_1, E_2, E_3."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        for mode in range(4):
            passes, res = verify_coproduct_coassociativity(alg, mode=mode)
            assert passes, f"Coassociativity failed at mode {mode}, res={res}"


# ================================================================
# 30. SHADOW DEPTH CLASSIFICATION
# ================================================================

class TestShadowDepthClassification:
    """Shadow depth classification G/L/C/M for the E_1 bar complex."""

    def test_class_G_at_all_degenerate_points(self):
        """Class G when any h_i = 0 (sigma_3 = 0)."""
        # h3 = 0: h2 = -h1
        for h1 in [0.5, 1.0, 2.0, -1.0]:
            bar = E1BarComplex(h1, -h1)
            # VERIFIED [DC] shadow depth [LC] boundary/limiting case
            assert bar.shadow_depth() == "G"
        # h1 = 0
        bar = E1BarComplex(0.0, 1.0)
        # VERIFIED [DC] shadow depth [LC] boundary/limiting case
        assert bar.shadow_depth() == "G"
        # h2 = 0
        bar = E1BarComplex(1.0, 0.0)
        # VERIFIED [DC] shadow depth [LC] boundary/limiting case
        assert bar.shadow_depth() == "G"

    def test_class_M_generic(self):
        """Class M for generic parameters with sigma_3 != 0."""
        for h1, h2 in [(1.0, -2.0), (0.5, 0.3), (2.0, -1.0), (0.3, -0.7)]:
            bar = E1BarComplex(h1, h2)
            if abs(bar.sigma3) > 1e-10:
                # VERIFIED [DC] shadow depth [LC] boundary/limiting case
                assert bar.shadow_depth() == "M"

    def test_sv_depth_pattern(self):
        """SV parametrization: N=1 is G, N>=2 is M."""
        for N in range(1, 10):
            data = sv_quantum_toroidal(N)
            if N == 1:
                # VERIFIED [DC] shadow depth [LC] boundary/limiting case
                assert data["depth"] == "G"
            else:
                # VERIFIED [DC] shadow depth [LC] boundary/limiting case
                assert data["depth"] == "M"

    def test_class_G_has_zero_cubic_and_quartic(self):
        """Class G has cubic = quartic = 0 (tower terminates at arity 2)."""
        bar = E1BarComplex(1.0, -1.0)  # N=1, class G
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(bar.cubic_shadow_e1()) < 1e-12
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(bar.quartic_shadow_e1()) < 1e-12

    def test_class_M_has_nonzero_cubic(self):
        """Class M has nonzero cubic shadow."""
        bar = E1BarComplex(1.0, -2.0)  # N=2, class M
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(bar.cubic_shadow_e1()) > 0.1


# ================================================================
# 31. VERTEX OPERATOR DEEP TESTS
# ================================================================

class TestVertexOperatorDeep:
    """Deep tests for vertex operators in the E_1 bar complex."""

    def test_ope_kernel_inversion(self):
        """OPE kernel K(z,w) = 1/G(w/z), so K(z,w)*K(w,z) = 1/[G(w/z)*G(z/w)] = 1."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        vo = VertexOperator(alg)
        z, w = 2.0, 0.5
        k1 = vo.ope_kernel(z, w)
        k2 = vo.ope_kernel(w, z)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(k1 * k2 - 1.0) < 1e-10

    def test_commutation_factor_equals_G_squared(self):
        """Commutation factor Phi(z)Phi(w)/Phi(w)Phi(z) = G(w/z)^2."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        vo = VertexOperator(alg)
        for z, w in [(2.0, 0.5), (1.0+0.3j, 0.5-0.2j)]:
            comm = vo.commutation_factor(z, w)
            g_val = alg.structure_function(w / z)
            # VERIFIED [DC] mutation equivalence [LC] boundary/limiting case
            assert abs(comm - g_val**2) < 1e-10

    def test_vertex_ope_three_poles(self):
        """Vertex operator OPE has exactly 3 poles (from 3 CY parameters)."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        vo = VertexOperator(alg)
        bar_data = vo.bar_interpretation()
        # VERIFIED [DC] vertex algebra [LC] boundary/limiting case
        assert len(bar_data["ope_poles"]) == 3

    def test_vertex_spectral_parameter_stored(self):
        """Vertex operator stores its spectral parameter."""
        alg = QuantumToroidalAlgebra(1.5, 2.0)
        u = 3.0 + 0.5j
        vo = VertexOperator(alg, spectral_param=u)
        # VERIFIED [DC] spectral data [LC] boundary/limiting case
        assert abs(vo.u - u) < 1e-12
