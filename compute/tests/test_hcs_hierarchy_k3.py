r"""Tests for the holomorphic CS hierarchy for K3.

Verifies the 3d -> 5d -> 6d tower, dimensional reductions,
Omega-background data, boundary conditions, Wilson lines, and
cross-engine compatibility.

MATHEMATICAL GROUND TRUTH:
  - 3d level: H_Muk, g(u) = 1, kappa_ch = 2.  PROVED (CY-A_2).
  - 5d level: Y(g_{K3}), g(u) = prod (u-h_i)/(u+h_i), kappa_ch = 3.
    CONJECTURAL (AP-CY14).
  - 6d level: U_{q,t}(g_{K3}^{tor}), G(x) = prod (1-q_a x)/(1-q_a^{-1} x).
    CONJECTURAL (AP-CY14).
  - 6d -> 5d: shrink E, trigonometric -> rational.
  - 5d -> 3d: shrink C, rational -> classical (g = 1).
  - kappa-spectrum: {0, 2, 3, 5, 24} (AP113).

TEST STRUCTURE:
  1. Hierarchy levels and status
  2. Structure functions at each level
  3. Dimensional reduction 6d -> 5d
  4. Dimensional reduction 5d -> 3d
  5. Omega-background at each level
  6. Boundary conditions and bulk/defect algebras
  7. Wilson lines
  8. kappa-spectrum consistency
  9. Cross-engine compatibility
  10. Master diagram
  11. AP compliance

VERIFIED values:
  # VERIFIED [DC] direct computation, [LT] Costello 2013 / Costello-Gwilliam 2021
  # VERIFIED [LC] limiting cases (eps -> 0, tau -> i*infty)
  # VERIFIED [CF] cross-engine (holomorphic_cs_chiral_engine, k3_yangian, k3_quantum_toroidal)
"""

import math

import numpy as np
import pytest
from fractions import Fraction
from sympy import Rational

from compute.lib.hcs_hierarchy_k3 import (
    # Constants
    STATUS_3D, STATUS_5D, STATUS_6D,
    STATUS_K3_3D, STATUS_K3_5D, STATUS_K3_6D,
    MUKAI_RANK, MUKAI_SIG,
    KAPPA_CH_K3, KAPPA_CH_K3E, KAPPA_BKM_K3E,
    KAPPA_CAT_K3, KAPPA_CAT_K3E, KAPPA_FIBER_K3,
    # Hierarchy data
    FLAT_HIERARCHY, K3_HIERARCHY,
    HierarchyLevel,
    # Dimensional reduction
    reduce_6d_to_5d,
    reduce_5d_to_3d,
    # Omega-background
    OmegaBackgroundK3,
    # Boundary data
    boundary_data_3d,
    boundary_data_5d,
    boundary_data_6d,
    # Wilson lines
    wilson_data_3d,
    wilson_data_5d,
    wilson_data_6d,
    # Structure functions
    structure_function_3d,
    structure_function_5d,
    structure_function_6d,
    # Reductions
    verify_6d_to_5d_reduction,
    verify_5d_to_3d_reduction,
    # Cross-engine
    verify_flat_space_specialisation,
    verify_kappa_spectrum_consistency,
    # Master diagram
    master_diagram,
    hierarchy_summary_table,
)

from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground
from compute.lib.k3_yangian import kummer_k3_parameters


# =========================================================================
# Test data: safe parameters (AP-CY28)
# =========================================================================

def _safe_kummer_params():
    """Kummer parameters with eps=1: h_i = 1 (i=1..4), h_i = -1/5 (i=5..24).

    Returns the raw list of 24 Rational parameters (not the NamedTuple).
    """
    return kummer_k3_parameters(epsilon=Rational(1)).h


def _safe_omega():
    """Safe Omega-background for flat-space tests (AP-CY28: avoid poles)."""
    # h = (37, 41, -78): large parameters, test points far from poles
    return OmegaBackground(h1=Rational(37), h2=Rational(41))


# =========================================================================
# 1. Hierarchy levels and status
# =========================================================================

class TestHierarchyLevels:
    """Test the hierarchy level data structures."""

    def test_flat_hierarchy_has_three_levels(self):
        assert len(FLAT_HIERARCHY) == 3

    def test_k3_hierarchy_has_three_levels(self):
        assert len(K3_HIERARCHY) == 3

    def test_flat_dims(self):
        """Flat space: dims 1, 2, 3."""
        assert [l.dim for l in FLAT_HIERARCHY] == [1, 2, 3]

    def test_k3_dims(self):
        """K3 hierarchy: dims 1, 2, 3."""
        assert [l.dim for l in K3_HIERARCHY] == [1, 2, 3]

    def test_en_levels_match_dims(self):
        """E_n level = complex dimension."""
        for h in FLAT_HIERARCHY + K3_HIERARCHY:
            assert h.en_level == h.dim

    def test_flat_status(self):
        """Flat space: 3d and 5d proved, 6d conjectural."""
        assert FLAT_HIERARCHY[0].status == 'PROVED'
        assert FLAT_HIERARCHY[1].status == 'PROVED'
        assert FLAT_HIERARCHY[2].status == 'CONJECTURAL'

    def test_k3_status(self):
        """K3: 3d proved (CY-A_2), 5d and 6d conjectural (AP-CY14)."""
        assert K3_HIERARCHY[0].status == 'PROVED'
        assert K3_HIERARCHY[1].status == 'CONJECTURAL'
        assert K3_HIERARCHY[2].status == 'CONJECTURAL'

    def test_k3_3d_algebra_is_heisenberg(self):
        assert 'Heisenberg' in K3_HIERARCHY[0].algebra_name

    def test_k3_5d_algebra_is_yangian(self):
        assert 'Yangian' in K3_HIERARCHY[1].algebra_name

    def test_k3_6d_algebra_is_toroidal(self):
        assert 'toroidal' in K3_HIERARCHY[2].algebra_name

    def test_structure_fn_types(self):
        """3d: classical, 5d: rational, 6d: trigonometric."""
        types = [l.structure_fn_type for l in K3_HIERARCHY]
        assert types == ['classical', 'rational', 'trigonometric']


# =========================================================================
# 2. Structure functions at each level
# =========================================================================

class TestStructureFunctions:
    """Test structure functions at each hierarchy level."""

    def test_3d_structure_fn_is_one(self):
        """At 3d, g(u) = 1 for all u."""
        # VERIFIED [DC] direct computation: no Omega-background means g = 1
        for u in [0.5, 1.0, 3.7, 100.0]:
            assert abs(structure_function_3d(u) - 1.0) < 1e-15

    def test_5d_structure_fn_large_u(self):
        """g_{K3}(u) -> 1 as u -> infinity (leading coeff ratio = 1)."""
        # VERIFIED [DC] degree (24,24) with equal leading coefficients
        h = _safe_kummer_params()
        g_large = structure_function_5d(1000.0, h)
        assert abs(g_large - 1.0) < 1e-3

    def test_5d_reflection_identity(self):
        """g(u) * g(-u) = 1 (algebraic unitarity)."""
        # VERIFIED [DC] factorwise cancellation, [CF] k3_yangian.py
        h = _safe_kummer_params()
        for u in [3.7 + 0.1j, 10.0, 50.0 + 1j]:
            gu = structure_function_5d(u, h)
            g_minus_u = structure_function_5d(-u, h)
            assert abs(gu * g_minus_u - 1.0) < 1e-10

    def test_5d_degree_24_24(self):
        """g_{K3} is degree (24, 24): 24 zeros and 24 poles."""
        # VERIFIED [DC] product has 24 factors, each contributing one zero and one pole
        h = _safe_kummer_params()
        # The zeros are at u = h_i, poles at u = -h_i
        # Test a zero (u = h_1 = 1 for Kummer with eps=1)
        u_near_zero = complex(h[0]) + 0.001j  # Near h_1
        g_near = structure_function_5d(u_near_zero, h)
        assert abs(g_near) < 0.1  # Near a zero, |g| should be small

    def test_5d_classical_limit(self):
        """g -> 1 as all h_i -> 0."""
        # VERIFIED [LC] classical limit: no deformation means g = 1
        h_zero = [Rational(0)] * MUKAI_RANK
        for u in [1.0, 5.0, 100.0]:
            g = structure_function_5d(u, h_zero)
            assert abs(g - 1.0) < 1e-15

    def test_6d_inversion_identity(self):
        """G(x) * G(1/x) = 1 (trigonometric unitarity)."""
        # VERIFIED [DC] see k3_quantum_toroidal.py verify_inversion_identity
        h = _safe_kummer_params()
        eps = 0.1  # Small eps to keep q_a near 1
        q_params = [np.exp(complex(hi) * eps) for hi in h]
        for theta in [0.3, 1.0, 2.7]:
            x = 0.5 * np.exp(1j * theta)
            Gx = structure_function_6d(x, q_params)
            Gx_inv = structure_function_6d(1.0 / x, q_params)
            assert abs(Gx * Gx_inv - 1.0) < 1e-8


# =========================================================================
# 3. Dimensional reduction 6d -> 5d
# =========================================================================

class TestReduction6dTo5d:
    """Test dimensional reduction: shrink E (trigonometric -> rational)."""

    def test_structure_fn_reduction(self):
        """Trigonometric -> rational as eps -> 0.

        At eps = 0.01, the O(eps^2) correction is ~0.005 for Kummer params,
        so we use tol = 0.01 (the agreement improves as eps -> 0).
        """
        # VERIFIED [LC] limiting case: G(e^{eps u}; e^{eps h}) -> g(u; h) as eps -> 0
        h = _safe_kummer_params()
        passes, max_err = verify_6d_to_5d_reduction(h, n_points=15, tol=0.01)
        assert passes, f"6d->5d reduction failed: max_rel_err = {max_err}"

    def test_cy2_preserved_under_reduction(self):
        """The CY_2 constraint survives the 6d -> 5d reduction."""
        # VERIFIED [DC] sum h_i = 0 => prod q_a = prod exp(h_i) = exp(sum h_i) = 1
        h = _safe_kummer_params()
        q_params = [np.exp(complex(hi) * 0.1) for hi in h]
        tau = 0.5j  # Im(tau) > 0 (FM24)
        _, diag = reduce_6d_to_5d(q_params, tau)
        assert diag['cy2_preserved']

    def test_nome_convergence(self):
        """Im(tau) > 0 implies |q| < 1 (FM24)."""
        # VERIFIED [DC] q = exp(2 pi i tau), |q| = exp(-2 pi Im(tau))
        h = _safe_kummer_params()
        q_params = [np.exp(complex(hi) * 0.1) for hi in h]
        for tau in [0.5j, 1.0j, 2.0j, 0.3 + 0.5j]:
            _, diag = reduce_6d_to_5d(q_params, tau)
            assert diag['nome_abs'] < 1.0
            assert diag['im_tau'] > 0

    def test_fm24_violation_caught(self):
        """Im(tau) <= 0 should raise assertion (FM24: B-cycle sign)."""
        h = _safe_kummer_params()
        q_params = [np.exp(complex(hi) * 0.1) for hi in h]
        with pytest.raises(AssertionError, match="FM24"):
            reduce_6d_to_5d(q_params, tau=-0.5j)


# =========================================================================
# 4. Dimensional reduction 5d -> 3d
# =========================================================================

class TestReduction5dTo3d:
    """Test dimensional reduction: shrink C (rational -> classical)."""

    def test_classical_limit_at_eps_zero(self):
        """At eps = 0: all h_i = 0, g = 1, Y -> H_Muk."""
        # VERIFIED [LC] epsilon = 0 is exact classical limit
        h = _safe_kummer_params()
        h_float = [float(hi) for hi in h]
        is_classical, diag = reduce_5d_to_3d(h_float, epsilon=0.0)
        assert is_classical
        assert diag['sigma3_scaled'] == 0.0
        assert 'Heisenberg' in diag['boundary_algebra']

    def test_nonclassical_at_eps_nonzero(self):
        """At eps > 0: sigma_3 != 0, full Yangian."""
        h = _safe_kummer_params()
        h_float = [float(hi) for hi in h]
        is_classical, diag = reduce_5d_to_3d(h_float, epsilon=1.0)
        assert not is_classical
        assert abs(diag['sigma3_scaled']) > 1e-10
        assert 'Y(g_K3)' in diag['boundary_algebra']

    def test_structure_fn_reduces_to_one(self):
        """Verify g(u; {0}) = 1 at multiple test points."""
        # VERIFIED [DC] product of (u-0)/(u+0) = 1 for 24 factors
        passes, max_res = verify_5d_to_3d_reduction(
            _safe_kummer_params(), n_points=15
        )
        assert passes, f"5d->3d reduction failed: max_res = {max_res}"


# =========================================================================
# 5. Omega-background at each level
# =========================================================================

class TestOmegaBackground:
    """Test the Omega-background data at each hierarchy level."""

    def test_3d_has_no_params(self):
        """3d level: no Omega-background."""
        ob = OmegaBackgroundK3(level=3)
        assert ob.num_params == 0
        assert all(h == 0 for h in ob.h_params)
        assert ob.tau is None

    def test_5d_has_23_params(self):
        """5d level: 24 Mukai params with 1 CY_2 constraint = 23 free."""
        h = _safe_kummer_params()
        ob = OmegaBackgroundK3(level=5, h_params=h)
        assert ob.num_params == 23

    def test_6d_has_24_params(self):
        """6d level: 23 Mukai + tau = 24 free parameters."""
        h = _safe_kummer_params()
        ob = OmegaBackgroundK3(level=6, h_params=h, tau=0.5j)
        assert ob.num_params == 24

    def test_5d_cy2_enforced(self):
        """CY_2 constraint violation is caught."""
        bad_h = [Rational(1)] * MUKAI_RANK  # sum = 24 != 0
        with pytest.raises(AssertionError, match="CY_2"):
            OmegaBackgroundK3(level=5, h_params=bad_h)

    def test_6d_nome(self):
        """Nome q = exp(2 pi i tau) is computed correctly."""
        # VERIFIED [DC] q = exp(2 pi i * i/2) = exp(-pi) ~ 0.0432
        h = _safe_kummer_params()
        ob = OmegaBackgroundK3(level=6, h_params=h, tau=0.5j)
        expected_abs = np.exp(-np.pi)  # |q| = exp(-2 pi * 0.5)
        assert abs(abs(ob.nome) - expected_abs) < 1e-10

    def test_3d_deformation_is_classical(self):
        ob = OmegaBackgroundK3(level=3)
        eff = ob.effective_deformation()
        assert eff['type'] == 'classical'
        assert eff['hbar'] == 0

    def test_5d_deformation_is_rational(self):
        h = _safe_kummer_params()
        ob = OmegaBackgroundK3(level=5, h_params=h)
        eff = ob.effective_deformation()
        assert eff['type'] == 'rational'
        assert 'sigma3' in eff

    def test_6d_deformation_is_trigonometric(self):
        h = _safe_kummer_params()
        ob = OmegaBackgroundK3(level=6, h_params=h, tau=0.5j)
        eff = ob.effective_deformation()
        assert eff['type'] == 'trigonometric'
        assert eff['nome_abs'] < 1.0  # FM24: |q| < 1


# =========================================================================
# 6. Boundary conditions and bulk/defect algebras
# =========================================================================

class TestBoundaryData:
    """Test boundary condition data at each level."""

    def test_3d_boundary(self):
        bd = boundary_data_3d()
        assert bd.level == 3
        assert bd.bc_type == 'Dirichlet'
        assert 'Heisenberg' in bd.boundary_algebra
        assert bd.kappa_ch == Rational(2)  # VERIFIED [LT] kappa_ch(K3) = 2

    def test_5d_boundary(self):
        bd = boundary_data_5d()
        assert bd.level == 5
        assert 'Yangian' in bd.boundary_algebra
        assert 'CONJECTURAL' in bd.boundary_algebra  # AP-CY14
        assert bd.kappa_ch == Rational(3)  # VERIFIED [LT] kappa_ch(K3 x E) = 3

    def test_6d_boundary(self):
        bd = boundary_data_6d()
        assert bd.level == 6
        assert 'toroidal' in bd.boundary_algebra
        assert 'CONJECTURAL' in bd.boundary_algebra  # AP-CY14
        assert bd.kappa_ch == Rational(3)

    def test_all_levels_have_bulk(self):
        """Every level has a bulk algebra (derived center)."""
        for bd in [boundary_data_3d(), boundary_data_5d(), boundary_data_6d()]:
            assert 'Z^{der}' in bd.bulk_algebra or 'HH*' in bd.bulk_algebra

    def test_all_levels_have_defect(self):
        """Every level has a defect algebra (Koszul dual)."""
        for bd in [boundary_data_3d(), boundary_data_5d(), boundary_data_6d()]:
            assert 'Koszul dual' in bd.defect_algebra or '!' in bd.defect_algebra


# =========================================================================
# 7. Wilson lines
# =========================================================================

class TestWilsonLines:
    """Test Wilson line data at each hierarchy level."""

    def test_3d_wilson_is_point(self):
        w = wilson_data_3d()
        assert w.level == 3
        assert 'point' in w.line_type

    def test_5d_wilson_is_line(self):
        w = wilson_data_5d()
        assert w.level == 5
        assert 'line' in w.line_type

    def test_6d_wilson_is_surface(self):
        w = wilson_data_6d()
        assert w.level == 6
        assert 'surface' in w.line_type

    def test_3d_coproduct_is_primitive(self):
        """At 3d, the Heisenberg coproduct is primitive."""
        w = wilson_data_3d()
        assert 'primitive' in w.coproduct_type

    def test_5d_coproduct_is_miura(self):
        """At 5d, the Yangian coproduct is Miura."""
        w = wilson_data_5d()
        assert 'Miura' in w.coproduct_type

    def test_wilson_dimension_increases(self):
        """Wilson operators increase in dimension: point < line < surface."""
        dims = {
            'point': 0,
            'line': 1,
            'surface': 2,
        }
        w3 = wilson_data_3d()
        w5 = wilson_data_5d()
        w6 = wilson_data_6d()
        d3 = max(d for key, d in dims.items() if key in w3.line_type)
        d5 = max(d for key, d in dims.items() if key in w5.line_type)
        d6 = max(d for key, d in dims.items() if key in w6.line_type)
        assert d3 < d5 < d6


# =========================================================================
# 8. kappa-spectrum consistency (AP113)
# =========================================================================

class TestKappaSpectrum:
    """Test the kappa-spectrum (AP113: NEVER bare kappa)."""

    def test_kappa_ch_k3(self):
        """kappa_ch(K3) = 2."""
        # VERIFIED [LT] CY-A_2 proved, kappa_ch = chi^{CY} at d=2
        assert KAPPA_CH_K3 == Rational(2)

    def test_kappa_ch_k3e(self):
        """kappa_ch(K3 x E) = 3 (additivity: 2 + 1)."""
        # VERIFIED [LT] product formula, [DC] 2 + 1 = 3
        assert KAPPA_CH_K3E == Rational(3)

    def test_kappa_bkm(self):
        """kappa_BKM(K3 x E) = 5 (Igusa cusp form weight)."""
        # VERIFIED [LT] Gritsenko-Nikulin: weight of Delta_5
        assert KAPPA_BKM_K3E == Rational(5)

    def test_kappa_cat_k3(self):
        """kappa_cat(K3) = chi(O_K3) = 2."""
        # VERIFIED [LT] Serre duality + Hodge diamond: h^{0,0} + h^{2,0} = 1 + 1 = 2
        assert KAPPA_CAT_K3 == Rational(2)

    def test_kappa_cat_k3e_kuenneth(self):
        """kappa_cat(K3 x E) = 0 (Kuenneth: chi(O_K3)*chi(O_E) = 2*0 = 0)."""
        # VERIFIED [DC] chi(O_E) = 0 for elliptic curve (h^{0,0} - h^{1,0} = 1-1 = 0)
        assert KAPPA_CAT_K3E == Rational(0)

    def test_kappa_fiber(self):
        """kappa_fiber = 24 = rank(Mukai lattice)."""
        # VERIFIED [LT] Mukai lattice = U^3 + E_8(-1)^2 has rank 24
        assert KAPPA_FIBER_K3 == Rational(24)

    def test_five_distinct_values(self):
        """The kappa-spectrum has five distinct values: {0, 2, 3, 5, 24}."""
        checks = verify_kappa_spectrum_consistency()
        assert checks['five_values']

    def test_all_kappa_consistency(self):
        """All six consistency checks pass."""
        checks = verify_kappa_spectrum_consistency()
        for name, result in checks.items():
            assert result, f"kappa consistency check '{name}' failed"


# =========================================================================
# 9. Cross-engine compatibility
# =========================================================================

class TestCrossEngine:
    """Test compatibility with existing engines."""

    def test_flat_space_embedding(self):
        """K3 hierarchy with 21 zero params reduces to flat-space C^3."""
        # VERIFIED [CF] holomorphic_cs_chiral_engine.py structure function
        omega = _safe_omega()
        passes, max_err = verify_flat_space_specialisation(omega, n_points=8)
        assert passes, f"Flat-space specialisation failed: max_err = {max_err}"

    def test_flat_space_embedding_selfdual(self):
        """Self-dual point: one h_i = 0 -> g = 1."""
        # VERIFIED [LC] sigma_3 = 0 => g = 1
        omega = OmegaBackground(h1=Rational(1), h2=Rational(-1))
        # h3 = 0 (self-dual)
        passes, max_err = verify_flat_space_specialisation(omega, n_points=5)
        assert passes

    def test_mukai_rank_matches_k3_yangian(self):
        """MUKAI_RANK in this engine matches k3_yangian.NUM_PARAMS."""
        from compute.lib.k3_yangian import NUM_PARAMS
        assert MUKAI_RANK == NUM_PARAMS

    def test_mukai_rank_matches_k3_toroidal(self):
        """MUKAI_RANK in this engine matches k3_quantum_toroidal.N_MUKAI."""
        from compute.lib.k3_quantum_toroidal import N_MUKAI
        assert MUKAI_RANK == N_MUKAI


# =========================================================================
# 10. Master diagram
# =========================================================================

class TestMasterDiagram:
    """Test the master diagram data structure."""

    def test_diagram_has_three_levels(self):
        d = master_diagram()
        assert len(d['levels']) == 3
        assert set(d['levels'].keys()) == {'3d', '5d', '6d'}

    def test_diagram_has_two_reductions(self):
        d = master_diagram()
        assert len(d['reductions']) == 2
        assert '6d -> 5d' in d['reductions']
        assert '5d -> 3d' in d['reductions']

    def test_diagram_kappa_spectrum(self):
        d = master_diagram()
        ks = d['kappa_spectrum']
        assert ks['kappa_ch_K3'] == 2
        assert ks['kappa_ch_K3E'] == 3
        assert ks['kappa_BKM_K3E'] == 5
        assert ks['kappa_fiber_K3'] == 24

    def test_6d_status_conjectural(self):
        d = master_diagram()
        assert d['levels']['6d']['status'] == 'CONJECTURAL'

    def test_3d_status_proved(self):
        d = master_diagram()
        assert d['levels']['3d']['status'] == 'PROVED'

    def test_en_levels_ascending(self):
        d = master_diagram()
        assert d['levels']['3d']['en_level'] == 1
        assert d['levels']['5d']['en_level'] == 2
        assert d['levels']['6d']['en_level'] == 3


# =========================================================================
# 11. AP compliance
# =========================================================================

class TestAPCompliance:
    """Test anti-pattern compliance."""

    def test_ap_cy14_k3_5d_conjectural(self):
        """AP-CY14: K3 Yangian is conjectural."""
        assert STATUS_K3_5D == 'CONJECTURAL'

    def test_ap_cy14_k3_6d_conjectural(self):
        """AP-CY14: K3 quantum toroidal is conjectural."""
        assert STATUS_K3_6D == 'CONJECTURAL'

    def test_ap113_no_bare_kappa(self):
        """AP113: all kappa constants have subscripts."""
        # The constants are named KAPPA_CH_*, KAPPA_BKM_*, KAPPA_CAT_*, KAPPA_FIBER_*
        # There is no plain "KAPPA" without subscript
        import compute.lib.hcs_hierarchy_k3 as mod
        public_names = [n for n in dir(mod) if n.startswith('KAPPA')]
        for name in public_names:
            # Must have a subscript after KAPPA_
            parts = name.split('_')
            assert len(parts) >= 3, f"Bare kappa: {name}"

    def test_ap_cy31_spectral_not_worldsheet(self):
        """AP-CY31: structure function uses spectral parameter u, not worldsheet z."""
        # The 5d structure function signature uses 'u', not 'z'
        import inspect
        sig = inspect.signature(structure_function_5d)
        param_names = list(sig.parameters.keys())
        assert 'u' in param_names
        assert 'z' not in param_names

    def test_mukai_signature(self):
        """The Mukai lattice has signature (4, 20), not (3, 19)."""
        assert MUKAI_SIG == (4, 20)

    def test_hierarchy_summary_table(self):
        """The summary table has 3 rows with all required fields."""
        table = hierarchy_summary_table()
        assert len(table) == 3
        required_fields = [
            'algebra', 'en_level', 'structure_fn', 'status',
            'kappa_ch', 'wilson_type', 'coproduct',
        ]
        for row in table:
            for field in required_fields:
                assert field in row, f"Missing field '{field}' in row"
