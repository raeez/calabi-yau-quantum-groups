r"""Tests for mathieu_moonshine_yangian.py: M_24 moonshine through the K3 Yangian.

STATUS: ALL results in this module are CONJECTURAL (AP-CY14).
The tests verify INTERNAL CONSISTENCY of the construction.

CENTRAL RESULTS (all conjectural):
    (1) All 26 M_24 Frame shapes account for 24 letters.
    (2) A_n = kappa_ch * dim(rho_n) = 2 * a_n (moonshine factorization).
    (3) The polar coefficient of h(tau) is -kappa_ch = -2.
    (4) The twined eta product for 1A is eta(tau)^{24} = Delta(q)/q.
    (5) M_24 permutes the 24 Yangian parameters, preserving CY_2.
    (6) The 24-dim rep decomposes as 23_std + 1_triv.
    (7) Twined structure functions have degree (trace_g, trace_g).
    (8) The trace-of-power formula for Frame shapes is consistent.
    (9) Umbral moonshine data for 23 Niemeier root systems tabulated.

Test structure:
    Section 1: Frame shapes (9 tests)
    Section 2: Moonshine coefficients (8 tests)
    Section 3: Twined eta products (8 tests)
    Section 4: M_24 action on Yangian (7 tests)
    Section 5: Umbral moonshine (5 tests)
    Section 6: Trace of power (7 tests)
    Section 7: Cross-verification (6 tests)

Manuscript references:
    toroidal_elliptic.tex, Thm thm:mathieu-moonshine (L1973)
    toroidal_elliptic.tex, Rem rem:twining-genera (L2074)
    toroidal_elliptic.tex, Rem rem:factor-2-is-kappa (L2043)
    toroidal_elliptic.tex, Rem rem:mock-modular-k3 (L2001)
    k3_times_e.tex, Prop prop:niemeier-shadow-landscape (L2007)
"""

import pytest
from fractions import Fraction
from sympy import Rational

from compute.lib.mathieu_moonshine_yangian import (
    # Constants
    ENGINE_STATUS,
    KAPPA_CH_K3,
    MATHIEU_COEFFICIENTS_A,
    MATHIEU_HALF_MULTIPLICITIES,
    MOCK_MODULAR_COEFFICIENTS,
    # M_24 classes
    M24_CONJUGACY_CLASSES,
    M24ConjugacyClass,
    m24_conjugacy_classes,
    m24_realized_classes,
    _frame_shape_trace,
    _frame_shape_total,
    _trace_of_power,
    # Twined eta products
    twined_bar_euler_exponent,
    twined_eta_product,
    twined_eta_product_leading_power,
    # M_24 action
    m24_action_on_charge_1,
    m24_traces_on_representations,
    # Moonshine coefficients
    moonshine_coefficient,
    mock_modular_polar_coefficient,
    # Twined structure function
    twined_structure_function_degree,
    twined_structure_function_evaluate,
    # Umbral moonshine
    UMBRAL_NIEMEIER_DATA,
    umbral_moonshine_at_niemeier,
    # 24 = 23 + 1
    decomposition_24_equals_23_plus_1,
    # Verification
    verify_frame_shapes,
    verify_moonshine_factorization,
    verify_eta_product_identity,
    verify_twined_eta_product_2a,
    verify_trace_of_power,
    full_verification,
)


# =========================================================================
# Section 1: Frame shapes (9 tests)
# =========================================================================

class TestFrameShapes:
    """Verify all 26 M_24 conjugacy classes have valid Frame shapes."""

    def test_all_frame_shapes_sum_to_24(self):
        """Every Frame shape must account for exactly 24 letters."""
        for name, cc in M24_CONJUGACY_CLASSES.items():
            total = _frame_shape_total(cc.frame_shape)
            assert total == 24, f"{name}: sum = {total}, expected 24"

    def test_trace_equals_fixed_points(self):
        """The trace on V_24 must equal the number of 1-cycles."""
        for name, cc in M24_CONJUGACY_CLASSES.items():
            computed_trace = _frame_shape_trace(cc.frame_shape)
            assert cc.trace_24 == computed_trace, (
                f"{name}: stored trace {cc.trace_24} != "
                f"computed {computed_trace}"
            )

    def test_num_conjugacy_classes(self):
        """M_24 has exactly 26 conjugacy classes (ATLAS)."""
        assert len(M24_CONJUGACY_CLASSES) == 26

    def test_identity_class(self):
        """1A is the identity: Frame shape 1^{24}, trace 24."""
        cc = M24_CONJUGACY_CLASSES['1A']
        assert cc.order == 1
        assert cc.frame_shape == {1: 24}
        assert cc.trace_24 == 24
        assert cc.realized_on_k3 is True

    def test_cycle_lengths_divide_order(self):
        """Every cycle length in a Frame shape must divide the element order."""
        for name, cc in M24_CONJUGACY_CLASSES.items():
            for cycle_len in cc.frame_shape:
                assert cc.order % cycle_len == 0, (
                    f"{name}: cycle length {cycle_len} does not "
                    f"divide order {cc.order}"
                )

    def test_realized_count(self):
        """At least 21 classes are realized as K3 sigma model symmetries."""
        realized = m24_realized_classes()
        # The manuscript lists 21 in its table (some with caveats)
        assert len(realized) >= 21

    def test_unrealized_classes(self):
        """7A, 7B, 15A, 15B are NOT realized on K3."""
        for name in ['7A', '7B', '15A', '15B']:
            assert not M24_CONJUGACY_CLASSES[name].realized_on_k3, (
                f"{name} should not be realized on K3"
            )

    def test_frame_shape_verification_suite(self):
        """The full Frame shape verification suite passes."""
        result = verify_frame_shapes()
        assert result['all_ok']
        assert result['num_classes'] == 26

    def test_involutions_are_order_2(self):
        """2A and 2B have order 2."""
        assert M24_CONJUGACY_CLASSES['2A'].order == 2
        assert M24_CONJUGACY_CLASSES['2B'].order == 2
        # 2A has 8 fixed points (non-free involution)
        assert M24_CONJUGACY_CLASSES['2A'].trace_24 == 8
        # 2B has 0 fixed points (free involution)
        assert M24_CONJUGACY_CLASSES['2B'].trace_24 == 0


# =========================================================================
# Section 2: Moonshine coefficients (8 tests)
# =========================================================================

class TestMoonshineCoefficients:
    """Verify the moonshine decomposition A_n = kappa_ch * dim(rho_n)."""

    def test_kappa_ch_equals_2(self):
        """kappa_ch(A_{K3}) = 2."""
        # VERIFIED: thm:k3-kappa in k3_times_e.tex (5 independent paths).
        assert KAPPA_CH_K3 == 2

    def test_A1_equals_90(self):
        """A_1 = 90 (first massive coefficient).
        # VERIFIED: [LT] EOT 2010, [DC] N=4 character decomposition.
        """
        assert MATHIEU_COEFFICIENTS_A[1] == 90

    def test_half_multiplicities(self):
        """a_n = A_n / 2 for all tabulated n.
        # VERIFIED: [DC] A_n/2, [LT] Gannon 2012.
        """
        for n, A_n in MATHIEU_COEFFICIENTS_A.items():
            assert MATHIEU_HALF_MULTIPLICITIES[n] == A_n // KAPPA_CH_K3

    def test_moonshine_factorization_all(self):
        """A_n = kappa_ch * a_n for all tabulated n."""
        result = verify_moonshine_factorization()
        assert result['all_ok']
        assert result['kappa_ch'] == 2

    def test_moonshine_coefficient_function(self):
        """The moonshine_coefficient function returns correct data."""
        mc = moonshine_coefficient(1)
        assert mc['A_n'] == 90
        assert mc['a_n'] == 45
        assert mc['kappa_ch'] == 2

    def test_mock_modular_polar_is_neg_kappa(self):
        """The polar coefficient of h(tau) is -kappa_ch = -2.
        # VERIFIED: [LT] EOT 2010, [DC] mock modular decomposition.
        """
        result = mock_modular_polar_coefficient()
        assert result['polar_equals_neg_kappa']
        assert result['A_0_full'] == -2
        assert result['a_0'] == -1

    def test_mock_modular_first_coefficients(self):
        """h(tau) = 2*q^{-1/8}(-1 + 45q + 231q^2 + 770q^3 + ...)."""
        assert MOCK_MODULAR_COEFFICIENTS[-1] == -1
        assert MOCK_MODULAR_COEFFICIENTS[1] == 45
        assert MOCK_MODULAR_COEFFICIENTS[2] == 231
        assert MOCK_MODULAR_COEFFICIENTS[3] == 770

    def test_first_nine_A_values(self):
        """A_1,...,A_9 match Eguchi-Ooguri-Tachikawa Table 1.
        # VERIFIED: [LT] arXiv:1004.0956, [DC] N=4 decomposition.
        """
        expected = {1: 90, 2: 462, 3: 1540, 4: 4554, 5: 11592,
                    6: 27830, 7: 60996, 8: 126270, 9: 246520}
        for n, val in expected.items():
            assert MATHIEU_COEFFICIENTS_A[n] == val, (
                f"A_{n}: expected {val}, got {MATHIEU_COEFFICIENTS_A[n]}"
            )


# =========================================================================
# Section 3: Twined eta products (8 tests)
# =========================================================================

class TestTwinedEtaProducts:
    """Verify the twined eta products associated to Frame shapes."""

    def test_identity_eta_product_is_eta24(self):
        """For 1A (identity), eta_g = eta^{24} = Delta/q.
        # VERIFIED: [DC] direct expansion, [LT] Ramanujan tau.
        """
        result = verify_eta_product_identity()
        assert result['all_ok']

    def test_identity_leading_power(self):
        """The leading q-power for 1A is 24/24 = 1."""
        lp = twined_eta_product_leading_power('1A')
        assert lp == Fraction(1)

    def test_2A_eta_product(self):
        """For 2A, eta_g = eta(tau)^8 * eta(2*tau)^8."""
        result = verify_twined_eta_product_2a()
        assert result['coeff_q0_is_1']

    def test_2B_eta_product_leading(self):
        """For 2B (Frame shape 2^{12}), leading power = 12*2/24 = 1."""
        lp = twined_eta_product_leading_power('2B')
        assert lp == Fraction(1)

    def test_3A_eta_product(self):
        """For 3A (1^6 3^6), eta_g = eta(tau)^6 * eta(3*tau)^6."""
        coeffs = twined_eta_product('3A', max_degree=4)
        assert coeffs.get(0, 0) == 1

    def test_twined_bar_euler_exponent_identity(self):
        """For 1A, twined bar Euler exponent is 24."""
        assert twined_bar_euler_exponent('1A') == 24

    def test_twined_bar_euler_exponent_2B(self):
        """For 2B (no fixed points), twined bar Euler exponent is 0."""
        assert twined_bar_euler_exponent('2B') == 0

    def test_all_leading_powers_positive(self):
        """All leading q-powers are positive rationals."""
        for name in M24_CONJUGACY_CLASSES:
            lp = twined_eta_product_leading_power(name)
            assert lp > 0, f"{name}: leading power {lp} <= 0"


# =========================================================================
# Section 4: M_24 action on Yangian (7 tests)
# =========================================================================

class TestM24YangianAction:
    """Verify the M_24 action on Y(g_{K3}) representations."""

    def test_identity_action(self):
        """The identity acts trivially on V_24."""
        action = m24_action_on_charge_1('1A')
        assert action.trace_on_V24 == 24
        assert action.preserves_structure_fn is True
        assert action.preserves_cy2 is True

    def test_all_preserve_structure_function(self):
        """All M_24 elements preserve the structure function g_{K3}(z)."""
        for name in M24_CONJUGACY_CLASSES:
            action = m24_action_on_charge_1(name)
            assert action.preserves_structure_fn is True

    def test_all_preserve_cy2(self):
        """All M_24 elements preserve the CY_2 constraint sum h_i = 0."""
        for name in M24_CONJUGACY_CLASSES:
            action = m24_action_on_charge_1(name)
            assert action.preserves_cy2 is True

    def test_24_decomposition(self):
        """V_24 = 23_std + 1_triv under M_24."""
        result = decomposition_24_equals_23_plus_1()
        assert result['dim_std'] == 23
        assert result['dim_triv'] == 1
        assert result['mukai_rank'] == 24

    def test_traces_consistency(self):
        """Trace on V_24 = trace on V_23 + 1."""
        traces = m24_traces_on_representations()
        for name, data in traces.items():
            assert data['trace_V23'] == data['trace_V24'] - 1

    def test_sym2_dim_for_identity(self):
        """Sym^2(V_24) has dimension 24*25/2 = 300 at identity."""
        traces = m24_traces_on_representations()
        # Trace of identity on Sym^2(V_24) = dim(Sym^2(V_24)) = 24*25/2 = 300
        assert traces['1A']['trace_Sym2_V24'] == 300

    def test_alt2_dim_for_identity(self):
        """Alt^2(V_24) has dimension 24*23/2 = 276 at identity."""
        traces = m24_traces_on_representations()
        assert traces['1A']['trace_Alt2_V24'] == 276


# =========================================================================
# Section 5: Umbral moonshine (5 tests)
# =========================================================================

class TestUmbralMoonshine:
    """Verify Umbral moonshine data for Niemeier lattices."""

    def test_23_niemeier_root_systems(self):
        """There are 23 Niemeier lattices with nonempty root system."""
        assert len(UMBRAL_NIEMEIER_DATA) == 23

    def test_a1_24_is_mathieu(self):
        """The A_1^{24} Niemeier lattice gives M_24 moonshine."""
        result = umbral_moonshine_at_niemeier('A_1^{24}')
        assert result['is_mathieu_case'] is True
        assert result['umbral_group'] == 'M_24'
        assert result['lambency'] == 2

    def test_all_rank_24(self):
        """All Niemeier lattices have rank 24."""
        for rs, data in UMBRAL_NIEMEIER_DATA.items():
            assert data['rank'] == 24, f"{rs}: rank = {data['rank']}"

    def test_shadow_data_consistent(self):
        """Shadow data at Niemeier points: lattice VOA kappa_ch = 24."""
        for rs in ['A_1^{24}', 'E_8^3', 'D_{24}']:
            result = umbral_moonshine_at_niemeier(rs)
            assert result['shadow_data']['kappa_ch_lattice_voa'] == 24
            assert result['shadow_data']['kappa_ch_k3_sigma'] == 2
            assert result['shadow_data']['shadow_class_lattice'] == 'G'

    def test_unknown_root_system(self):
        """Querying an unknown root system returns an error."""
        result = umbral_moonshine_at_niemeier('Z_99')
        assert 'error' in result


# =========================================================================
# Section 6: Trace of power (7 tests)
# =========================================================================

class TestTraceOfPower:
    """Verify the trace-of-power formula for Frame shapes."""

    def test_identity_power_p(self):
        """trace(1A^p) = 24 for all p."""
        fs = M24_CONJUGACY_CLASSES['1A'].frame_shape
        for p in [1, 2, 3, 5, 7, 12]:
            assert _trace_of_power(fs, p) == 24

    def test_2A_squared_is_identity(self):
        """2A^2 = 1A, so trace(2A^2) = 24."""
        fs = M24_CONJUGACY_CLASSES['2A'].frame_shape
        assert _trace_of_power(fs, 2) == 24

    def test_2B_squared_is_identity(self):
        """2B^2 = 1A, so trace(2B^2) = 24."""
        fs = M24_CONJUGACY_CLASSES['2B'].frame_shape
        assert _trace_of_power(fs, 2) == 24

    def test_3A_cubed_is_identity(self):
        """3A^3 = 1A, so trace(3A^3) = 24."""
        fs = M24_CONJUGACY_CLASSES['3A'].frame_shape
        assert _trace_of_power(fs, 3) == 24

    def test_4A_squared_trace(self):
        """4A^2 fixes the entries in the four 2-cycles of 4A."""
        fs = M24_CONJUGACY_CLASSES['4A'].frame_shape
        assert _trace_of_power(fs, 2) == 8

    def test_verification_suite(self):
        """The full trace-of-power verification suite passes."""
        result = verify_trace_of_power()
        assert result['all_ok']

    def test_trace_of_power_divides_24(self):
        """trace(g^p) is always a non-negative integer <= 24."""
        for name, cc in M24_CONJUGACY_CLASSES.items():
            for p in range(1, cc.order + 1):
                tr = _trace_of_power(cc.frame_shape, p)
                assert 0 <= tr <= 24, (
                    f"{name}^{p}: trace = {tr}, out of range"
                )


# =========================================================================
# Section 7: Cross-verification (6 tests)
# =========================================================================

class TestCrossVerification:
    """Cross-verify moonshine data against K3 Yangian infrastructure."""

    def test_twined_structure_function_identity_degree(self):
        """Twined structure function for 1A has full degree (24, 24)."""
        result = twined_structure_function_degree('1A')
        assert result['twined_degree'] == (24, 24)
        assert not result['twined_trivial']

    def test_twined_structure_function_2B_trivial(self):
        """Twined structure function for 2B is trivial (no fixed points)."""
        result = twined_structure_function_degree('2B')
        assert result['twined_degree'] == (0, 0)
        assert result['twined_trivial']

    def test_twined_structure_function_evaluate_identity(self):
        """Twined structure function for 1A at z=3 is the full g_{K3}(3)."""
        from compute.lib.k3_yangian import structure_function_evaluate
        full_g = structure_function_evaluate(Rational(3))
        twined_g = twined_structure_function_evaluate('1A', Rational(3))
        assert twined_g['g_twined'] == full_g

    def test_twined_structure_function_evaluate_2B_is_1(self):
        """Twined structure function for 2B at any z is 1."""
        result = twined_structure_function_evaluate('2B', Rational(3))
        assert result['g_twined'] == 1
        assert result['trivial']

    def test_full_verification_suite(self):
        """The complete verification suite passes."""
        result = full_verification()
        assert result['status'] == 'CONJECTURAL'
        assert result['path1_frame_shapes']['all_ok']
        assert result['path2_moonshine_factorization']['all_ok']
        assert result['path3_mock_modular_polar']['polar_equals_neg_kappa']
        assert result['path4_eta_product_1A']['all_ok']
        assert result['path6_trace_of_power']['all_ok']

    def test_kappa_ch_consistency_with_k3_yangian(self):
        """kappa_ch = 2 is consistent across moonshine and K3 Yangian."""
        # kappa_ch = 2 from the K3 sigma model (5 independent paths)
        assert KAPPA_CH_K3 == 2
        # A_n / a_n = 2 for all n
        for n in MATHIEU_COEFFICIENTS_A:
            assert MATHIEU_COEFFICIENTS_A[n] == 2 * MATHIEU_HALF_MULTIPLICITIES[n]
        # The polar coefficient -2 = -kappa_ch
        assert MOCK_MODULAR_COEFFICIENTS[-1] * KAPPA_CH_K3 == -KAPPA_CH_K3
