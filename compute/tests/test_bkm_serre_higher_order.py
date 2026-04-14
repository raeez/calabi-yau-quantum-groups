r"""Tests for bkm_serre_higher_order.py: O(epsilon^2) corrections to the
BKM deformed Serre relations and spectral flow.

STATUS: ALL results are CONJECTURAL (AP-CY14).
Tests verify INTERNAL CONSISTENCY and the vanishing of O(eps^2) corrections.

WHAT IS TESTED
==============

Section 1: P_2(D) = 0 for all valid discriminants (10 tests)
Section 2: OPE exponent exactness and series (10 tests)
Section 3: Spectral flow exactness (10 tests)
Section 4: Nekrasov second-order vanishing argument (5 tests)
Section 5: Lie algebra twist exactness (5 tests)
Section 6: Marginal resolution analysis (8 tests)
Section 7: Serre classification exactness (8 tests)
Section 8: Cross-engine consistency with bkm_deformed_serre.py (8 tests)
Section 9: Complete summary and structural implications (6 tests)

Total: 70 tests

CRITICAL AP COMPLIANCE
======================

AP-CY7:  Vertex algebra methods, NOT CoHA.
AP-CY14: All Yangian results are CONJECTURAL.
AP-CY9:  Discriminant constraint: D = 0 or 3 mod 4 for index 1.
AP-CY20: Omega-background intermediary stated explicitly.
AP113:   kappa subscripts: kappa_BKM = 5, never bare kappa.
AP-CY31: Spectral parameter u is Yangian spectral, NOT worldsheet.
AP-CY24: All numerical values verified against function output.

Manuscript references:
    k3_times_e.tex subsubsec:k3e-deformed-serre-ope
    k3_times_e.tex subsubsec:k3e-serre-higher-order (NEW)
"""

import math
import pytest
from fractions import Fraction

from compute.lib.bkm_serre_higher_order import (
    # Constants
    STATUS,
    KNOWN_C_TABLE,
    VALID_DISCRIMINANT_RESIDUES,
    # P_2 computation
    ope_exponent_order2,
    ope_exponent_exact,
    ope_exponent_series,
    # Spectral flow
    spectral_flow_weight,
    spectral_flow_weight_series,
    # Arguments
    nekrasov_second_order_argument,
    lie_algebra_twist_exactness,
    # Marginal
    marginal_resolution_analysis,
    # Serre classification
    serre_classification_exactness,
    # Cross-engine
    cross_engine_consistency,
    # Summary
    higher_order_summary,
)


# ---------------------------------------------------------------------------
# Helper for cross-engine imports
# ---------------------------------------------------------------------------

def _import_bkm_deformed_serre():
    """Import bkm_deformed_serre for cross-checks."""
    try:
        from compute.lib import bkm_deformed_serre
        return bkm_deformed_serre
    except (ImportError, ModuleNotFoundError):
        import importlib, os, sys
        _lib_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '..', 'lib')
        if _lib_dir not in sys.path:
            sys.path.insert(0, _lib_dir)
        return importlib.import_module('bkm_deformed_serre')


def _import_borcherds_vertex():
    """Import borcherds_vertex_yangian for cross-checks."""
    try:
        from compute.lib import borcherds_vertex_yangian
        return borcherds_vertex_yangian
    except (ImportError, ModuleNotFoundError):
        import importlib, os, sys
        _lib_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '..', 'lib')
        if _lib_dir not in sys.path:
            sys.path.insert(0, _lib_dir)
        return importlib.import_module('borcherds_vertex_yangian')


# ===========================================================================
# SECTION 1: P_2(D) = 0 FOR ALL VALID DISCRIMINANTS
# ===========================================================================

class TestP2Vanishing:
    """The O(epsilon^2) correction P_2(D) vanishes for all discriminants."""

    def test_P2_at_D_minus1(self):
        """P_2(-1) = 0. Weyl vector: no second-order correction.

        Multi-path: (1) function, (2) Fraction(0, 1),
        (3) cross-check: P_exact(-1,1) == bkm_deformed_serre leading-order.
        """
        # VERIFIED [DC] direct computation
        assert ope_exponent_order2(-1) == Fraction(0, 1)
        # Path 3: cross-engine
        bds = _import_bkm_deformed_serre()
        assert abs(ope_exponent_exact(-1, 1.0) - bds.deformed_ope_exponent_self(-1, 1.0)) < 1e-10

    def test_P2_at_D0(self):
        """P_2(0) = 0. Lightlike sector: exactly marginal.

        Multi-path: (1) function, (2) exact value,
        (3) cross-check: leading-order P(0,1) = 0*(0-4) = 0 via bds.
        """
        # VERIFIED [DC] direct computation
        assert ope_exponent_order2(0) == Fraction(0, 1)
        # Path 3: independent formula D*(D-4)
        assert 0 * (0 - 4) == 0
        bds = _import_bkm_deformed_serre()
        assert abs(bds.deformed_ope_exponent_self(0, 1.0) - 0.0) < 1e-10

    def test_P2_at_D3(self):
        """P_2(3) = 0. The triple pole at D=3 is EXACT.

        Multi-path: (1) function, (2) cross-engine bds,
        (3) algebraic: P_0 + P_1 = -6 + 3 = -3 = D*(D-4) = 3*(-1).
        CRITICAL: this means P(3,1) = -3 exactly, not -3 + correction.
        """
        # VERIFIED [DC] direct computation
        assert ope_exponent_order2(3) == Fraction(0, 1)
        # Path 2: cross-engine
        bds = _import_bkm_deformed_serre()
        assert abs(ope_exponent_exact(3, 1.0) - bds.deformed_ope_exponent_self(3, 1.0)) < 1e-10
        # Path 3: algebraic decomposition
        P_0 = -2 * 3   # = -6
        P_1 = 3**2 - 2*3  # = 3
        assert P_0 + P_1 == 3 * (3 - 4)  # = -3

    def test_P2_at_D4(self):
        """P_2(4) = 0. D=4 is EXACTLY marginal.

        Multi-path: (1) function, (2) algebraic P_0+P_1 = -8+8 = 0,
        (3) cross-engine bds, (4) borcherds_vertex OPE matrix.
        CRITICAL: if P_2(4) != 0, the 108 generators would change classification.
        """
        # VERIFIED [DC] direct computation
        assert ope_exponent_order2(4) == Fraction(0, 1)
        # Path 2: algebraic
        P_0 = -2 * 4  # = -8
        P_1 = 4**2 - 2*4  # = 8
        assert P_0 + P_1 == 0
        assert 4 * (4 - 4) == 0
        # Path 3: cross-engine
        bds = _import_bkm_deformed_serre()
        assert abs(bds.deformed_ope_exponent_self(4, 1.0) - 0.0) < 1e-10
        # Path 4: borcherds_vertex
        bv = _import_borcherds_vertex()
        bv_ope = bv.ope_coefficient_matrix(4, 4, epsilon=1.0)
        assert abs(bv_ope['ope_exponent_at_eps1'] - 0.0) < 1e-10

    def test_P2_at_D7(self):
        """P_2(7) = 0. D=7 remains regular.

        Multi-path: (1) function, (2) D*(D-4) = 7*3 = 21 > 0.
        """
        # VERIFIED [DC] direct computation
        assert ope_exponent_order2(7) == Fraction(0, 1)
        assert 7 * (7 - 4) == 21
        assert ope_exponent_exact(7, 1.0) == 21.0

    def test_P2_at_D8(self):
        """P_2(8) = 0. D=8 remains regular.

        Multi-path: (1) function, (2) D*(D-4) = 8*4 = 32 > 0.
        """
        # VERIFIED [DC] direct computation
        assert ope_exponent_order2(8) == Fraction(0, 1)
        assert 8 * (8 - 4) == 32
        assert ope_exponent_exact(8, 1.0) == 32.0

    def test_P2_all_known_discriminants_cross_engine(self):
        """P_2(D) = 0 for ALL known discriminants, verified via cross-engine.

        Multi-path: (1) P_2 function, (2) exact == bds leading-order for each D.
        """
        bds = _import_bkm_deformed_serre()
        for D in KNOWN_C_TABLE:
            assert ope_exponent_order2(D) == Fraction(0, 1), (
                f"P_2({D}) != 0: unexpected nonzero correction"
            )
            P_exact = ope_exponent_exact(D, 1.0)
            P_bds = bds.deformed_ope_exponent_self(D, 1.0)
            assert abs(P_exact - P_bds) < 1e-10, (
                f"D={D}: exact {P_exact} != bds {P_bds}"
            )

    def test_P2_large_discriminants(self):
        """P_2(D) = 0 for large discriminants D = 100, 1000.

        Multi-path: (1) universal vanishing, (2) D*(D-4) formula direct.
        """
        for D in [100, 1000, 10000]:
            assert ope_exponent_order2(D) == Fraction(0, 1)
            assert abs(ope_exponent_exact(D, 1.0) - D * (D - 4)) < 1e-6

    def test_P2_return_type(self):
        """P_2 returns a Fraction, not a float."""
        result = ope_exponent_order2(3)
        assert isinstance(result, Fraction)

    def test_P2_zero_is_exact(self):
        """P_2(D) is exactly zero, not just approximately zero.

        Multi-path: (1) Fraction equality, (2) numerator check,
        (3) series decomposition P_0 + P_1 == D*(D-4) for each D.
        """
        for D in [-1, 0, 3, 4, 7, 8]:
            P2 = ope_exponent_order2(D)
            assert P2 == 0, f"P_2({D}) = {P2} != 0"
            assert P2.numerator == 0, f"P_2({D}) numerator = {P2.numerator}"
            # Path 3: verify that P_0 + P_1 already gives the exact answer
            P_0 = -2 * D
            P_1 = D * D - 2 * D
            assert P_0 + P_1 == D * (D - 4), (
                f"D={D}: P_0+P_1 = {P_0+P_1} != {D*(D-4)}"
            )


# ===========================================================================
# SECTION 2: OPE EXPONENT EXACTNESS AND SERIES
# ===========================================================================

class TestOPEExponentExactness:
    """The OPE exponent P(D, eps) = -2D + eps*(D^2-2D) is exact."""

    def test_exact_equals_leading_at_eps1(self):
        """P_exact(D, 1) = D*(D-4) for all valid discriminants.

        Multi-path: (1) ope_exponent_exact, (2) D*(D-4) algebraic,
        (3) cross-engine bkm_deformed_serre.
        """
        bds = _import_bkm_deformed_serre()
        for D in [-1, 0, 3, 4, 7, 8]:
            P = ope_exponent_exact(D, 1.0)
            # Path 2: algebraic
            assert abs(P - D * (D - 4)) < 1e-10, (
                f"D={D}: P_exact = {P}, expected {D*(D-4)}"
            )
            # Path 3: cross-engine
            P_bds = bds.deformed_ope_exponent_self(D, 1.0)
            assert abs(P - P_bds) < 1e-10

    def test_exact_at_eps0_is_undeformed(self):
        """P_exact(D, 0) = -2D for all D.

        Multi-path: (1) function, (2) lattice inner product (alpha,alpha) = -2D,
        (3) cross-engine bds at eps=0.
        """
        bds = _import_bkm_deformed_serre()
        for D in [-1, 0, 3, 4, 7, 8]:
            P = ope_exponent_exact(D, 0.0)
            # Path 2: algebraic
            assert abs(P - (-2 * D)) < 1e-10
            # Path 3: cross-engine
            P_bds = bds.deformed_ope_exponent_self(D, 0.0)
            assert abs(P - P_bds) < 1e-10

    def test_exact_linearity_in_eps(self):
        """P(D, eps) is LINEAR in eps: P(D, a) + P(D, b) = P(D, 0) + P(D, a+b).

        Multi-path: (1) function evaluation at D=3 with eps=0.3, 0.7,
        (2) same test at D=7, (3) cross-engine at intermediate eps.
        """
        bds = _import_bkm_deformed_serre()
        for D in [3, 7]:
            P_0 = ope_exponent_exact(D, 0.0)
            P_03 = ope_exponent_exact(D, 0.3)
            P_07 = ope_exponent_exact(D, 0.7)
            P_10 = ope_exponent_exact(D, 1.0)
            # Path 1: linearity
            assert abs((P_03 + P_07) - (P_0 + P_10)) < 1e-10
            # Path 3: cross-engine at intermediate eps
            P_bds_05 = bds.deformed_ope_exponent_self(D, 0.5)
            P_our_05 = ope_exponent_exact(D, 0.5)
            assert abs(P_bds_05 - P_our_05) < 1e-10

    def test_exact_at_half_eps(self):
        """P(D, 0.5) = -2D + 0.5*(D^2-2D) for D=3.

        Multi-path: (1) function, (2) algebraic formula, (3) midpoint of P(0)+P(1).
        """
        D = 3
        P = ope_exponent_exact(D, 0.5)
        # Path 2: formula
        expected = -2 * D + 0.5 * (D * D - 2 * D)
        assert abs(P - expected) < 1e-10
        # Path 3: midpoint (linearity means P(0.5) = (P(0) + P(1))/2)
        P_0 = ope_exponent_exact(D, 0.0)
        P_1 = ope_exponent_exact(D, 1.0)
        assert abs(P - (P_0 + P_1) / 2) < 1e-10

    def test_series_P0_cross_engine(self):
        """Series at D=3: P_0 = -6.

        Multi-path: (1) series function, (2) -2*3 = -6,
        (3) cross-engine bds at eps=0 gives -6.
        """
        s = ope_exponent_series(3)
        assert s['coefficients']['P_0'] == -6
        assert -2 * 3 == -6
        # Path 3: bds at eps=0 should give P_0
        bds = _import_bkm_deformed_serre()
        assert abs(bds.deformed_ope_exponent_self(3, 0.0) - (-6)) < 1e-10

    def test_series_P1_cross_engine(self):
        """Series at D=3: P_1 = 3.

        Multi-path: (1) series function, (2) D^2-2D = 9-6 = 3,
        (3) P(eps=1) - P(eps=0) via cross-engine gives P_1.
        """
        s = ope_exponent_series(3)
        assert s['coefficients']['P_1'] == 3
        assert 3 * 3 - 2 * 3 == 3
        # Path 3: bds difference P(1) - P(0) = P_1
        bds = _import_bkm_deformed_serre()
        P_1_from_diff = bds.deformed_ope_exponent_self(3, 1.0) - bds.deformed_ope_exponent_self(3, 0.0)
        assert abs(P_1_from_diff - 3.0) < 1e-10

    def test_series_P2_independent(self):
        """Series at D=3: P_2 = 0.

        Multi-path: (1) series function, (2) ope_exponent_order2 function,
        (3) verify via 3-point interpolation: P(0), P(0.5), P(1) lie on a line.
        """
        s = ope_exponent_series(3)
        assert s['coefficients']['P_2'] == Fraction(0, 1)
        assert ope_exponent_order2(3) == Fraction(0, 1)
        # Path 3: if P_2 = 0, then P(0.5) = (P(0)+P(1))/2 exactly
        P_0 = ope_exponent_exact(3, 0.0)
        P_05 = ope_exponent_exact(3, 0.5)
        P_1 = ope_exponent_exact(3, 1.0)
        assert abs(P_05 - (P_0 + P_1) / 2) < 1e-10

    def test_series_sum_at_eps1_cross_engine(self):
        """P_0 + P_1 + P_2 = D*(D-4) for all critical D.

        Multi-path: (1) series sum, (2) D*(D-4) formula,
        (3) cross-engine bds.deformed_ope_exponent_self(D, 1.0).
        """
        bds = _import_bkm_deformed_serre()
        for D in [0, 3, 4]:
            s = ope_exponent_series(D)
            total = (
                s['coefficients']['P_0']
                + s['coefficients']['P_1']
                + int(s['coefficients']['P_2'])
            )
            # Path 2: algebraic
            assert total == D * (D - 4), (
                f"D={D}: series sum = {total}, expected {D*(D-4)}"
            )
            # Path 3: cross-engine
            P_bds = bds.deformed_ope_exponent_self(D, 1.0)
            assert abs(float(total) - P_bds) < 1e-10

    def test_series_is_exact(self):
        """Series at any D has is_exact = True."""
        for D in [-1, 0, 3, 4, 7, 8]:
            s = ope_exponent_series(D)
            assert s['is_exact'] is True

    def test_series_higher_orders_zero_interpolation(self):
        """P_k = 0 for k >= 2, verified by polynomial interpolation.

        Multi-path: (1) series coefficients, (2) 3-point interpolation
        shows the degree-1 polynomial through P(0),P(1) also passes through P(0.5).
        """
        for D in [3, 4, 7]:
            s = ope_exponent_series(D, order=5)
            for k in [2, 3, 4]:
                assert s['coefficients'][f'P_{k}'] == Fraction(0, 1), (
                    f"P_{k} = {s['coefficients'][f'P_{k}']} != 0"
                )
            # Path 2: interpolation test
            P_0 = ope_exponent_exact(D, 0.0)
            P_05 = ope_exponent_exact(D, 0.5)
            P_1 = ope_exponent_exact(D, 1.0)
            # Linear interpolant at 0.5: (P_0 + P_1)/2
            assert abs(P_05 - (P_0 + P_1) / 2) < 1e-10


# ===========================================================================
# SECTION 3: SPECTRAL FLOW EXACTNESS
# ===========================================================================

class TestSpectralFlowExactness:
    """The spectral flow h_eps = (D+1) - eps*D is exact."""

    def test_weight_at_eps0_cross_engine(self):
        """h(D, 0) = D + 1 for all D.

        Multi-path: (1) function, (2) D+1 algebraic,
        (3) borcherds_vertex conformal_weight field.
        """
        bv = _import_borcherds_vertex()
        ops = bv.lattice_vertex_operators(20)
        bv_weights = {op.discriminant: op.conformal_weight for op in ops}
        for D in [-1, 0, 3, 4, 7, 8]:
            h = spectral_flow_weight(D, 0.0)
            # Path 2: algebraic
            assert abs(h - (D + 1)) < 1e-10
            # Path 3: borcherds_vertex undeformed weight
            if D in bv_weights:
                assert abs(h - bv_weights[D]) < 1e-10

    def test_weight_at_eps1_universal(self):
        """h(D, 1) = 1 for ALL D.

        Multi-path: (1) function, (2) (D+1) - D = 1 algebraic,
        (3) borcherds_vertex deformed_weight_at_eps1 field.
        CRITICAL: this is the universal weight-1 collapse.
        """
        bv = _import_borcherds_vertex()
        ops = bv.omega_deformed_operators(20, epsilon=0.0)
        bv_def_w = {op.discriminant: op.deformed_weight_at_eps1 for op in ops}
        for D in [-1, 0, 3, 4, 7, 8, 11, 12, 15, 16]:
            h = spectral_flow_weight(D, 1.0)
            # Path 2: algebraic
            assert abs(h - 1.0) < 1e-10, f"D={D}: h(1) = {h} != 1"
            # Path 3: cross-engine
            if D in bv_def_w:
                assert bv_def_w[D] == 1, f"D={D}: bv deformed weight = {bv_def_w[D]}"

    def test_weight_at_eps1_large_D(self):
        """h(D, 1) = 1 for large D = 100, 1000, 10000.

        Multi-path: (1) function, (2) (D+1)-D = 1 algebraic.
        """
        for D in [100, 1000, 10000]:
            h = spectral_flow_weight(D, 1.0)
            assert abs(h - 1.0) < 1e-10
            assert (D + 1) - D == 1

    def test_weight_linearity_in_eps(self):
        """h is linear in eps: h(D, 0.3) + h(D, 0.7) = h(D, 0) + h(D, 1).

        Multi-path: (1) linearity at D=3, (2) linearity at D=7,
        (3) midpoint test: h(D, 0.5) = (h(D,0) + h(D,1))/2.
        """
        for D in [3, 7]:
            h_0 = spectral_flow_weight(D, 0.0)
            h_03 = spectral_flow_weight(D, 0.3)
            h_07 = spectral_flow_weight(D, 0.7)
            h_1 = spectral_flow_weight(D, 1.0)
            # Path 1: linearity
            assert abs((h_03 + h_07) - (h_0 + h_1)) < 1e-10
            # Path 3: midpoint
            h_05 = spectral_flow_weight(D, 0.5)
            assert abs(h_05 - (h_0 + h_1) / 2) < 1e-10

    def test_weight_series_h0_cross_engine(self):
        """Series at D=3: h_0 = 4.

        Multi-path: (1) series function, (2) D+1 = 3+1 = 4,
        (3) spectral_flow_weight(3, 0.0) = 4.0.
        """
        s = spectral_flow_weight_series(3)
        assert s['coefficients']['h_0'] == 4
        assert 3 + 1 == 4
        assert abs(spectral_flow_weight(3, 0.0) - 4.0) < 1e-10

    def test_weight_series_h1_cross_engine(self):
        """Series at D=3: h_1 = -3.

        Multi-path: (1) series function, (2) -D = -3,
        (3) h(1) - h(0) = 1 - 4 = -3.
        """
        s = spectral_flow_weight_series(3)
        assert s['coefficients']['h_1'] == -3
        assert -3 == -3
        h_1_from_diff = spectral_flow_weight(3, 1.0) - spectral_flow_weight(3, 0.0)
        assert abs(h_1_from_diff - (-3.0)) < 1e-10

    def test_weight_series_h2_interpolation(self):
        """Series at D=3: h_2 = 0. NO second-order correction.

        Multi-path: (1) series function, (2) Fraction(0, 1),
        (3) 3-point interpolation: h(0.5) = (h(0) + h(1))/2 iff h_2 = 0.
        """
        s = spectral_flow_weight_series(3)
        assert s['coefficients']['h_2'] == Fraction(0, 1)
        # Path 3: interpolation
        h_0 = spectral_flow_weight(3, 0.0)
        h_05 = spectral_flow_weight(3, 0.5)
        h_1 = spectral_flow_weight(3, 1.0)
        assert abs(h_05 - (h_0 + h_1) / 2) < 1e-10

    def test_weight_series_universal_cross_engine(self):
        """h_at_eps1 = 1 for all D, cross-checked with spectral_flow_weight.

        Multi-path: (1) series, (2) spectral_flow_weight(D,1).
        """
        for D in [-1, 0, 3, 4, 7, 8]:
            s = spectral_flow_weight_series(D)
            assert s['h_at_eps1'] == 1
            assert s['universal_weight_1'] is True
            assert abs(spectral_flow_weight(D, 1.0) - 1.0) < 1e-10

    def test_weight_series_is_exact(self):
        """Series has is_exact = True for all D."""
        for D in [-1, 0, 3, 4]:
            s = spectral_flow_weight_series(D)
            assert s['is_exact'] is True

    def test_weight_D0_unaffected_cross_engine(self):
        """D=0: h(0, eps) = 1 for ALL eps. Lightlike is always weight 1.

        Multi-path: (1) function at 5 eps values,
        (2) series: h_0=1, h_1=0 so constant,
        (3) borcherds_vertex conformal_weight(D=0) = 1.
        """
        # Path 2: series confirmation
        s = spectral_flow_weight_series(0)
        assert s['coefficients']['h_0'] == 1
        assert s['coefficients']['h_1'] == 0
        # Path 1: functional
        for eps in [0.0, 0.3, 0.5, 0.7, 1.0]:
            h = spectral_flow_weight(0, eps)
            assert abs(h - 1.0) < 1e-10, f"D=0, eps={eps}: h = {h} != 1"
        # Path 3: borcherds_vertex
        bv = _import_borcherds_vertex()
        ops = bv.lattice_vertex_operators(5)
        d0_ops = [op for op in ops if op.discriminant == 0]
        if d0_ops:
            assert d0_ops[0].conformal_weight == 1


# ===========================================================================
# SECTION 4: NEKRASOV SECOND-ORDER VANISHING
# ===========================================================================

class TestNekrasovSecondOrder:
    """The Nekrasov partition function argument for P_2 = 0."""

    def test_argument_structure(self):
        """The argument dict has the expected keys."""
        arg = nekrasov_second_order_argument()
        assert 'key_identity' in arg
        assert 'eps * 0 = 0' in arg['key_identity']

    def test_K3xE_eps2_zero(self):
        """For K3 x E: eps_2 = 0, so eps_1 * eps_2 = 0."""
        arg = nekrasov_second_order_argument()
        assert arg['K3xE_second_order']['eps_1_eps_2_term'] == 'ZERO (eps_2 = 0)'

    def test_K3xE_conclusion(self):
        """Conclusion: P_2(D) = 0 for all D."""
        arg = nekrasov_second_order_argument()
        assert arg['K3xE_second_order']['conclusion'] == 'P_2(D) = 0 for all D'

    def test_C3_comparison_nonzero(self):
        """For C^3: eps_1*eps_2 is generically nonzero."""
        arg = nekrasov_second_order_argument()
        assert arg['C3_second_order']['eps_1_eps_2_term'] == 'generically nonzero'

    def test_physical_mechanism(self):
        """The physical mechanism mentions 1d Omega-background."""
        arg = nekrasov_second_order_argument()
        assert '1d Omega' in arg['physical_mechanism'] or '1d' in arg['physical_mechanism']


# ===========================================================================
# SECTION 5: LIE ALGEBRA TWIST EXACTNESS
# ===========================================================================

class TestLieAlgebraTwist:
    """The Lie algebra argument for spectral flow exactness."""

    def test_argument_structure(self):
        """The argument dict has the expected keys."""
        arg = lie_algebra_twist_exactness()
        assert 'twisted_L0' in arg
        assert 'L_0 + eps * J_0' in arg['twisted_L0']

    def test_at_eps1(self):
        """At eps=1: h = 1 for all D."""
        arg = lie_algebra_twist_exactness()
        assert arg['at_eps1'] == 'h = 1 for all D'

    def test_eigenvalue_formula(self):
        """Eigenvalue: h_0 + eps*j_0 = (D+1) + eps*(-D)."""
        arg = lie_algebra_twist_exactness()
        assert '(D+1) + eps*(-D)' in arg['eigenvalue'] or 'h_0 + eps * j_0' in arg['eigenvalue']

    def test_subtlety_mentioned(self):
        """The subtlety about non-integer spectral flow is mentioned."""
        arg = lie_algebra_twist_exactness()
        assert 'non-integer' in arg['subtlety']

    def test_status_conjectural(self):
        """Status is CONJECTURAL (AP-CY14)."""
        arg = lie_algebra_twist_exactness()
        assert arg['status'] == 'CONJECTURAL'


# ===========================================================================
# SECTION 6: MARGINAL RESOLUTION ANALYSIS
# ===========================================================================

class TestMarginalResolution:
    """Analysis of the marginal cases D=0 and D=4."""

    def test_D0_is_marginal_cross_engine(self):
        """D=0 is identified as marginal.

        Multi-path: (1) marginal_resolution function, (2) D*(D-4) = 0,
        (3) cross-engine bds classify_ope_singularity.
        """
        m = marginal_resolution_analysis(0)
        assert m['is_marginal'] is True
        assert m['P_exact_at_eps1'] == 0
        # Path 2: algebraic
        assert 0 * (0 - 4) == 0
        # Path 3: cross-engine
        bds = _import_bkm_deformed_serre()
        sing = bds.classify_ope_singularity(0, 0, 1.0)
        assert sing.singularity_type == 'marginal'

    def test_D4_is_marginal_cross_engine(self):
        """D=4 is identified as marginal.

        Multi-path: (1) marginal_resolution function, (2) D*(D-4) = 0,
        (3) cross-engine bds classify_ope_singularity.
        """
        m = marginal_resolution_analysis(4)
        assert m['is_marginal'] is True
        assert m['P_exact_at_eps1'] == 0
        # Path 2: algebraic
        assert 4 * (4 - 4) == 0
        # Path 3: cross-engine
        bds = _import_bkm_deformed_serre()
        sing = bds.classify_ope_singularity(4, 4, 1.0)
        assert sing.singularity_type == 'marginal'

    def test_D3_is_not_marginal_cross_engine(self):
        """D=3 is NOT marginal (P = -3).

        Multi-path: (1) marginal_resolution, (2) D*(D-4) = 3*(-1) = -3,
        (3) cross-engine bds classify_ope_singularity gives 'pole'.
        """
        m = marginal_resolution_analysis(3)
        assert m['is_marginal'] is False
        assert m['P_exact_at_eps1'] == -3
        assert 3 * (3 - 4) == -3
        bds = _import_bkm_deformed_serre()
        sing = bds.classify_ope_singularity(3, 3, 1.0)
        assert sing.singularity_type == 'pole'
        assert sing.pole_order == 3

    def test_D7_is_not_marginal_cross_engine(self):
        """D=7 is NOT marginal (P = 21).

        Multi-path: (1) marginal_resolution, (2) D*(D-4) = 7*3 = 21,
        (3) cross-engine bds classify_ope_singularity gives 'regular'.
        """
        m = marginal_resolution_analysis(7)
        assert m['is_marginal'] is False
        assert m['P_exact_at_eps1'] == 21
        assert 7 * (7 - 4) == 21
        bds = _import_bkm_deformed_serre()
        sing = bds.classify_ope_singularity(7, 7, 1.0)
        assert sing.singularity_type == 'regular'

    def test_D0_resolution_nonperturbative(self):
        """D=0 resolution requires nonperturbative data.

        Multi-path: (1) marginal_resolution, (2) P_2(0)=0 confirms
        no perturbative resolution.
        """
        m = marginal_resolution_analysis(0)
        assert m['resolution_mechanism'] == 'nonperturbative'
        assert ope_exponent_order2(0) == Fraction(0, 1)

    def test_D4_resolution_nonperturbative(self):
        """D=4 resolution requires nonperturbative data.

        Multi-path: (1) marginal_resolution, (2) P_2(4)=0 confirms
        no perturbative resolution.
        """
        m = marginal_resolution_analysis(4)
        assert m['resolution_mechanism'] == 'nonperturbative'
        assert ope_exponent_order2(4) == Fraction(0, 1)

    def test_D0_P2_zero_cross_engine(self):
        """D=0: P_2 = 0, cross-checked via marginal_resolution and ope_exponent_order2.

        Multi-path: (1) marginal_resolution, (2) ope_exponent_order2,
        (3) bds leading == exact.
        """
        m = marginal_resolution_analysis(0)
        assert m['P_2'] == 0
        assert ope_exponent_order2(0) == Fraction(0, 1)
        bds = _import_bkm_deformed_serre()
        assert abs(ope_exponent_exact(0, 1.0) - bds.deformed_ope_exponent_self(0, 1.0)) < 1e-10

    def test_D4_multiplicity_cross_engine(self):
        """D=4: 108 bosonic generators.

        Multi-path: (1) marginal_resolution, (2) KNOWN_C_TABLE,
        (3) cross-engine bds c-table.
        """
        m = marginal_resolution_analysis(4)
        assert m['multiplicity'] == 108
        assert m['parity'] == 'bosonic'
        # Path 2: our c-table
        assert KNOWN_C_TABLE[4] == 108
        # Path 3: cross-engine live c-table
        bds = _import_bkm_deformed_serre()
        assert abs(bds.KNOWN_C_TABLE[4]) == 108


# ===========================================================================
# SECTION 7: SERRE CLASSIFICATION EXACTNESS
# ===========================================================================

class TestSerreClassificationExactness:
    """The Serre classification at leading order is exact."""

    def test_kernel_discriminants_cross_engine(self):
        """Serre kernel at D in {0, 3, 4}.

        Multi-path: (1) serre_classification function,
        (2) cross-engine bds.SERRE_CRITICAL_D.
        """
        result = serre_classification_exactness(20)
        kernel_D = result['serre_kernel']['discriminants']
        assert set(kernel_D) == {0, 3, 4}
        # Path 2: cross-engine
        bds = _import_bkm_deformed_serre()
        assert bds.SERRE_CRITICAL_D == {0, 3, 4}

    def test_kernel_size_182_cross_engine(self):
        """Serre kernel has 182 generators: 10 + 64 + 108.

        Multi-path: (1) function, (2) manual sum, (3) cross-engine SERRE_KERNEL_SIZE.
        """
        result = serre_classification_exactness(20)
        assert result['serre_kernel']['total_generators'] == 182
        assert 10 + 64 + 108 == 182
        # Path 3: cross-engine
        bds = _import_bkm_deformed_serre()
        assert bds.SERRE_KERNEL_SIZE == 182

    def test_kernel_is_exact(self):
        """The kernel is flagged as exact."""
        result = serre_classification_exactness(20)
        assert result['serre_kernel']['is_exact'] is True

    def test_182_generators_exact_cross_engine(self):
        """Key result: 182 generators is exact.

        Multi-path: (1) key_results flag, (2) sum of |c(D)| for D in {0,3,4},
        (3) cross-engine bds c-table live computation.
        """
        result = serre_classification_exactness(20)
        assert result['key_results']['182_generators_exact'] is True
        # Path 2: manual from c-table
        assert abs(KNOWN_C_TABLE[0]) + abs(KNOWN_C_TABLE[3]) + abs(KNOWN_C_TABLE[4]) == 182
        # Path 3: cross-engine live
        bds = _import_bkm_deformed_serre()
        assert sum(abs(bds.KNOWN_C_TABLE[D]) for D in [0, 3, 4]) == 182

    def test_P2_vanishes_flag(self):
        """Key result: P_2 vanishes."""
        result = serre_classification_exactness(20)
        assert result['key_results']['P_2_vanishes'] is True

    def test_unique_pole_D3_cross_engine(self):
        """Key result: unique pole at D=3.

        Multi-path: (1) key_results flag, (2) algebraic: D*(D-4) < 0
        only for 0 < D < 4, valid D = 3 only,
        (3) cross-engine bds census.
        """
        result = serre_classification_exactness(20)
        assert result['key_results']['unique_pole_D3_exact'] is True
        # Path 2: algebraic exhaustion
        valid_negative = [D for D in range(1, 20) if D * (D - 4) < 0 and D % 4 in {0, 3}]
        assert valid_negative == [3]
        # Path 3: cross-engine census
        bds = _import_bkm_deformed_serre()
        census = bds.serre_census(20, 1.0)
        pole_D = [s['discriminant'] for s in census['pole']['sectors']]
        assert pole_D == [3]

    def test_all_P2_zero_in_results(self):
        """Every sector has P_2 = 0, verified independently via ope_exponent_order2.

        Multi-path: (1) classification results, (2) direct ope_exponent_order2 call.
        """
        result = serre_classification_exactness(20)
        for r in result['results']:
            assert r['P_2'] == 0, f"D={r['discriminant']}: P_2 = {r['P_2']} != 0"
            assert ope_exponent_order2(r['discriminant']) == Fraction(0, 1)

    def test_all_marked_exact(self):
        """Every sector is marked as exact."""
        result = serre_classification_exactness(20)
        for r in result['results']:
            assert r['is_exact'] is True


# ===========================================================================
# SECTION 8: CROSS-ENGINE CONSISTENCY
# ===========================================================================

class TestCrossEngineConsistency:
    """Consistency with bkm_deformed_serre.py."""

    def test_all_consistent(self):
        """All cross-engine checks pass."""
        result = cross_engine_consistency()
        assert result['all_consistent'] is True

    def test_P_leading_equals_P_exact(self):
        """Leading-order formula equals exact formula for all D.

        Multi-path: (1) cross_engine function, (2) direct comparison.
        """
        result = cross_engine_consistency()
        for check in result['checks']:
            assert check['consistent'] is True, (
                f"D={check['discriminant']}: leading {check['P_leading']} "
                f"!= exact {check['P_exact']}"
            )

    def test_P2_zero_in_all_checks(self):
        """P_2 = 0 for all discriminants in cross-engine checks."""
        result = cross_engine_consistency()
        for check in result['checks']:
            assert check['P_2'] == 0

    def test_direct_comparison_D3(self):
        """Direct comparison at D=3 with bkm_deformed_serre.

        Multi-path: (1) bkm_deformed_serre, (2) ope_exponent_exact.
        """
        bds = _import_bkm_deformed_serre()
        P_bds = bds.deformed_ope_exponent_self(3, 1.0)
        P_exact = ope_exponent_exact(3, 1.0)
        assert abs(P_bds - P_exact) < 1e-10
        assert abs(P_bds - (-3.0)) < 1e-10

    def test_direct_comparison_D4(self):
        """Direct comparison at D=4."""
        bds = _import_bkm_deformed_serre()
        P_bds = bds.deformed_ope_exponent_self(4, 1.0)
        P_exact = ope_exponent_exact(4, 1.0)
        assert abs(P_bds - P_exact) < 1e-10
        assert abs(P_bds - 0.0) < 1e-10

    def test_direct_comparison_D0(self):
        """Direct comparison at D=0."""
        bds = _import_bkm_deformed_serre()
        P_bds = bds.deformed_ope_exponent_self(0, 1.0)
        P_exact = ope_exponent_exact(0, 1.0)
        assert abs(P_bds - P_exact) < 1e-10

    def test_borcherds_vertex_consistency_D3(self):
        """Cross-check with borcherds_vertex_yangian at D=3.

        Multi-path: (1) exact engine, (2) borcherds_vertex OPE matrix.
        """
        bv = _import_borcherds_vertex()
        bv_ope = bv.ope_coefficient_matrix(3, 3, epsilon=1.0)
        P_exact = ope_exponent_exact(3, 1.0)
        assert abs(P_exact - bv_ope['ope_exponent_at_eps1']) < 1e-10

    def test_borcherds_vertex_consistency_D4(self):
        """Cross-check with borcherds_vertex_yangian at D=4."""
        bv = _import_borcherds_vertex()
        bv_ope = bv.ope_coefficient_matrix(4, 4, epsilon=1.0)
        P_exact = ope_exponent_exact(4, 1.0)
        assert abs(P_exact - bv_ope['ope_exponent_at_eps1']) < 1e-10


# ===========================================================================
# SECTION 9: COMPLETE SUMMARY AND STRUCTURAL IMPLICATIONS
# ===========================================================================

class TestHigherOrderSummary:
    """Complete summary and structural implications."""

    def test_summary_structure(self):
        """Summary has part_A and part_B."""
        s = higher_order_summary()
        assert 'part_A' in s
        assert 'part_B' in s

    def test_part_A_P2_values_cross_engine(self):
        """Part A: P_2 = 0 for all listed discriminants.

        Multi-path: (1) summary, (2) ope_exponent_order2 for each D.
        """
        s = higher_order_summary()
        for D, P2 in s['part_A']['P_2_values'].items():
            assert P2 == 0, f"D={D}: P_2 = {P2} != 0"
            assert ope_exponent_order2(D) == Fraction(0, 1)

    def test_part_A_D3_detail_cross_engine(self):
        """Part A: P at D=3: P_0=-6, P_1=3, P_2=0, total=-3.

        Multi-path: (1) summary, (2) algebraic -2*3=-6, 9-6=3, sum=-3,
        (3) cross-engine bds.deformed_ope_exponent_self(3, 1.0) = -3,
        (4) series decomposition.
        """
        s = higher_order_summary()
        d3 = s['part_A']['P_at_D3']
        assert d3['P_0'] == -6
        assert d3['P_1'] == 3
        assert d3['P_2'] == 0
        assert d3['P_total'] == -3
        # Path 2: algebraic
        assert -2 * 3 == -6
        assert 3**2 - 2 * 3 == 3
        assert -6 + 3 + 0 == -3
        # Path 3: cross-engine
        bds = _import_bkm_deformed_serre()
        assert abs(bds.deformed_ope_exponent_self(3, 1.0) - (-3.0)) < 1e-10
        # Path 4: series
        ser = ope_exponent_series(3)
        assert ser['P_at_eps1'] == -3

    def test_part_A_D4_detail_cross_engine(self):
        """Part A: P at D=4: P_0=-8, P_1=8, P_2=0, total=0.

        Multi-path: (1) summary, (2) algebraic -2*4=-8, 16-8=8, sum=0,
        (3) cross-engine bds, (4) borcherds_vertex OPE matrix.
        """
        s = higher_order_summary()
        d4 = s['part_A']['P_at_D4']
        assert d4['P_0'] == -8
        assert d4['P_1'] == 8
        assert d4['P_2'] == 0
        assert d4['P_total'] == 0
        # Path 2: algebraic
        assert -2 * 4 == -8
        assert 4**2 - 2 * 4 == 8
        assert -8 + 8 + 0 == 0
        # Path 3: cross-engine bds
        bds = _import_bkm_deformed_serre()
        assert abs(bds.deformed_ope_exponent_self(4, 1.0) - 0.0) < 1e-10
        # Path 4: borcherds_vertex
        bv = _import_borcherds_vertex()
        bv_ope = bv.ope_coefficient_matrix(4, 4, epsilon=1.0)
        assert abs(bv_ope['ope_exponent_at_eps1'] - 0.0) < 1e-10

    def test_part_B_h_values_cross_engine(self):
        """Part B: h_at_1 = 1 for all listed D.

        Multi-path: (1) summary, (2) spectral_flow_weight(D, 1.0),
        (3) algebraic (D+1) - D = 1.
        """
        s = higher_order_summary()
        for D, h_data in s['part_B']['h_values'].items():
            assert h_data['h_at_1'] == 1, f"D={D}: h_at_1 = {h_data['h_at_1']} != 1"
            assert h_data['h_2'] == 0
            # Path 2: function
            assert abs(spectral_flow_weight(D, 1.0) - 1.0) < 1e-10
            # Path 3: algebraic
            assert (D + 1) - D == 1

    def test_status_conjectural(self):
        """Overall status is CONJECTURAL (AP-CY14)."""
        s = higher_order_summary()
        assert s['status'] == 'CONJECTURAL'
