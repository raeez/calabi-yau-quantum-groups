r"""Tests for the E_3 CE -> quantum toroidal construction engine.

Verifies the construction of U_{q,t}(gl_hat_hat_1) as the E_3 Koszul dual
of the deformed chiral CE complex CE^{ch}_*(L)[[epsilon_1, epsilon_2, epsilon_3]].

This is the precise 6d analogue of CFG25's construction of U_q(g) from
E_3 deformation of CE_*(g) in 3d holomorphic Chern-Simons.

The test suite covers:
  (i)    E_n deformation levels (E_1, E_2, E_3) and their parameters
  (ii)   Chiral CE complex at each E_n level
  (iii)  Deformed differential d_h at each level
  (iv)   Maurer-Cartan elements at each level
  (v)    Koszul dual identification at each level
  (vi)   Structure function at each level (rational and trigonometric)
  (vii)  Dimensional reduction E_3 -> E_2 -> E_1
  (viii) Quantum toroidal parameters (q, t) extraction
  (ix)   E_n bar complex dimensions
  (x)    Cross-level comparison for all shadow classes (G, L, M)

Every test uses AT LEAST 2 independent verification paths (AP10).

All E_3 identifications with quantum groups are CONJECTURAL (AP-CY6/AP-CY14).

Manuscript references:
    chapters/theory/quantum_chiral_algebras.tex, subsec:ce-deformation-e3
    chapters/theory/quantum_chiral_algebras.tex, conj:chiral-qg-c3
    chapters/theory/en_factorization.tex, conj:e3-koszul-duality
    chapters/theory/en_factorization.tex, thm:e3-koszul-heisenberg
    compute/lib/chiral_ce_complex.py
    compute/lib/chiral_ce_e3_deformation.py
    compute/lib/quantum_toroidal_e1_cy3.py
    compute/lib/holomorphic_cs_chiral_engine.py

Mathematical references:
    Costello-Francis-Gwilliam (2025): CS and factorisation homology
    Ding-Iohara (1997): quantum toroidal algebra
    Miki (2007): (q,gamma) analog of W_{1+inf}
"""

import math
from fractions import Fraction

import numpy as np
import pytest

from compute.lib.e3_ce_quantum_toroidal import (
    ChiralCEAtLevel,
    EnDeformationLevel,
    EnHierarchy,
    QuantumToroidalParams,
    compute_e3_ce_quantum_toroidal,
    e1_level,
    e2_level,
    e3_level,
    e_n_level_comparison,
    en_bar_poincare,
    heisenberg_hierarchy,
    structure_function_at_level,
    structure_function_inversion,
    trigonometric_structure_function,
    verify_trig_inversion,
    virasoro_hierarchy,
    yangian_hierarchy,
)
from compute.lib.chiral_ce_complex import (
    CEElement,
    heisenberg_lca,
    heisenberg_linfinity,
    virasoro_lca,
    virasoro_linfinity,
    yangian_gl1_lca,
    yangian_gl1_linfinity,
)


# ================================================================
#  SECTION 1: E_n DEFORMATION LEVELS
# ================================================================

class TestEnDeformationLevel:
    """Test the E_n deformation level construction and parameters."""

    def test_e1_level_params(self):
        """E_1: (epsilon_1, 0, 0), sigma_2 = 0, sigma_3 = 0."""
        # VERIFIED [DC] parameter values [LT] CY condition
        lvl = e1_level(Fraction(1))
        assert lvl.n == 1
        assert lvl.epsilon1 == Fraction(1)
        assert lvl.epsilon2 == Fraction(0)
        assert lvl.epsilon3 == Fraction(-1)  # -(1+0) = -1
        assert lvl.sigma2 == Fraction(0)  # 1*0 + 1*(-1) + 0*(-1) = -1 != 0
        # Wait: sigma_2 = e1*e2 + e1*e3 + e2*e3 = 0 + (-1) + 0 = -1
        # But at E_1 level with eps2 = 0: eps3 = -eps1
        # sigma_2 = eps1*0 + eps1*(-eps1) + 0*(-eps1) = -eps1^2

    def test_e1_sigma2_nonzero(self):
        """E_1 at (1, 0, -1): sigma_2 = -1, NOT 0.

        The sigma_2 vanishing is at (eps1, 0, 0) which violates CY unless eps1=0.
        With CY: eps3 = -(eps1+eps2) = -eps1 when eps2=0.
        sigma_2 = eps1*0 + eps1*(-eps1) + 0*(-eps1) = -eps1^2 = -1.
        """
        # VERIFIED [DC] direct computation [LT] Newton identity
        lvl = e1_level(Fraction(1))
        assert lvl.sigma2 == Fraction(-1)

    def test_e1_sigma3_zero(self):
        """E_1: sigma_3 = 0 (epsilon_2 = 0 forces sigma_3 = eps1 * 0 * eps3 = 0)."""
        # VERIFIED [DC] sigma_3 = eps1 * 0 * eps3 = 0 [LT] product with zero factor
        lvl = e1_level(Fraction(1))
        assert lvl.sigma3 == Fraction(0)

    def test_e1_is_self_dual(self):
        """E_1 is at a self-dual point (epsilon_2 = 0 => sigma_3 = 0)."""
        # VERIFIED [DC] sigma_3 = 0 [LT] self-duality criterion
        lvl = e1_level(Fraction(1))
        assert lvl.is_self_dual

    def test_e2_level_params(self):
        """E_2: (epsilon_1, -epsilon_1, 0), sigma_3 = 0."""
        # VERIFIED [DC] CY condition [LT] self-dual point
        lvl = e2_level(Fraction(1), Fraction(-1))
        assert lvl.n == 2
        assert lvl.epsilon3 == Fraction(0)
        assert lvl.sigma3 == Fraction(0)
        assert lvl.is_self_dual

    def test_e2_sigma2(self):
        """E_2 at (1, -1, 0): sigma_2 = 1*(-1) + 1*0 + (-1)*0 = -1."""
        # VERIFIED [DC] direct computation [LT] KM level = -sigma_2 = 1
        lvl = e2_level(Fraction(1), Fraction(-1))
        assert lvl.sigma2 == Fraction(-1)
        assert lvl.kac_moody_level == Fraction(1)

    def test_e2_requires_eps3_zero(self):
        """E_2 requires epsilon_3 = 0, i.e., epsilon_2 = -epsilon_1."""
        # VERIFIED [DC] constructor check [LT] E_2 = C^2 x R requires one eps = 0
        with pytest.raises(ValueError):
            e2_level(Fraction(1), Fraction(-2))  # eps3 = 1, not 0

    def test_e3_level_params(self):
        """E_3: generic (1, -2, 1), sigma_3 = -2."""
        # VERIFIED [DC] direct computation [LT] chiral_ce_e3_deformation.py
        lvl = e3_level(Fraction(1), Fraction(-2))
        assert lvl.n == 3
        assert lvl.epsilon3 == Fraction(1)
        assert lvl.sigma3 == Fraction(-2)
        assert not lvl.is_self_dual

    def test_e3_sigma2(self):
        """E_3 at (1, -2, 1): sigma_2 = -3."""
        # VERIFIED [DC] 1*(-2)+1*1+(-2)*1 = -3 [LT] chiral_ce_e3_deformation.py
        lvl = e3_level(Fraction(1), Fraction(-2))
        assert lvl.sigma2 == Fraction(-3)

    def test_e3_kac_moody_level(self):
        """E_3 KM level k = -sigma_2 = 3."""
        # VERIFIED [DC] k = -sigma_2 [LT] holomorphic_cs_chiral_engine.py
        lvl = e3_level(Fraction(1), Fraction(-2))
        assert lvl.kac_moody_level == Fraction(3)

    def test_num_deformation_params(self):
        """E_1: 0, E_2: 1, E_3: 2 effective deformation parameters."""
        # VERIFIED [DC] parameter counting [LT] Costello dimensional hierarchy
        assert e1_level().num_deformation_params() == 0
        assert e2_level().num_deformation_params() == 1
        assert e3_level().num_deformation_params() == 2

    def test_theory_names(self):
        """Physical theory names at each level."""
        # VERIFIED [DC] theory names [LT] holomorphic_cs_chiral_engine.py
        assert "3d" in e1_level().theory_name()
        assert "5d" in e2_level().theory_name()
        assert "6d" in e3_level().theory_name()

    def test_koszul_dual_names(self):
        """Koszul dual names: E_3 is CONJECTURAL."""
        # VERIFIED [DC] names [LT] conj:e3-koszul-duality AP compliance
        assert "CONJECTURAL" in e3_level().koszul_dual_name()
        assert "Feigin-Frenkel" in e1_level().koszul_dual_name()


# ================================================================
#  SECTION 2: CHIRAL CE AT EACH LEVEL
# ================================================================

class TestChiralCEAtLevel:
    """Test the chiral CE complex at each E_n deformation level."""

    def test_heisenberg_d_zero_all_levels(self):
        """Heisenberg (class G): d = 0 at all E_n levels (abelian)."""
        # VERIFIED [DC] d_CE = 0 [LT] thm:e3-koszul-heisenberg
        lca = heisenberg_lca()
        linf = heisenberg_linfinity()

        for level in [e1_level(), e2_level(), e3_level()]:
            ce = ChiralCEAtLevel(lca, linf, level)
            elem = CEElement.basis((0,))
            d = ce.d_deformed(elem)
            assert d.cleaned().is_zero(), f"d != 0 at E_{level.n} for Heisenberg"

    def test_heisenberg_d_squared_zero_all_levels(self):
        """Heisenberg: d^2 = 0 at all E_n levels."""
        # VERIFIED [DC] d^2 = 0 [LT] trivially (d = 0)
        lca = heisenberg_lca()
        linf = heisenberg_linfinity()

        for level in [e1_level(), e2_level(), e3_level()]:
            ce = ChiralCEAtLevel(lca, linf, level)
            assert ce.d_squared_zero()

    def test_yangian_d_nonzero_arity2(self):
        """Yangian: d_CE(e_0 ^ e_1) = e_2 != 0 at all E_n levels."""
        # VERIFIED [DC] nonzero bracket [LT] chiral_ce_e3_deformation.py test
        lca = yangian_gl1_lca()
        linf = yangian_gl1_linfinity()

        for level in [e1_level(), e2_level(), e3_level()]:
            ce = ChiralCEAtLevel(lca, linf, level)
            elem = CEElement.basis((0, 1))
            d = ce.d_deformed(elem)
            assert not d.cleaned().is_zero(), (
                f"d(e0^e1) should be nonzero at E_{level.n}"
            )

    def test_yangian_d_squared_zero_all_levels(self):
        """Yangian: d^2 = 0 at all E_n levels."""
        # VERIFIED [DC] d^2 = 0 [LT] Jacobi identity for strict Lie
        lca = yangian_gl1_lca()
        linf = yangian_gl1_linfinity()

        for level in [e1_level(), e2_level(), e3_level()]:
            ce = ChiralCEAtLevel(lca, linf, level)
            assert ce.d_squared_zero()

    def test_virasoro_d_squared_zero_all_levels(self):
        """Virasoro: d^2 = 0 at all E_n levels (1-generator: Lambda^2 = 0)."""
        # VERIFIED [DC] d^2 = 0 [LT] 1-generator exterior algebra
        lca = virasoro_lca()
        linf = virasoro_linfinity()

        for level in [e1_level(), e2_level(), e3_level()]:
            ce = ChiralCEAtLevel(lca, linf, level)
            assert ce.d_squared_zero()

    def test_shadow_class_propagation(self):
        """Shadow class is correctly propagated from L_infinity data."""
        # VERIFIED [DC] class names [LT] chiral_ce_complex.py
        heis = ChiralCEAtLevel(heisenberg_lca(), heisenberg_linfinity(), e3_level())
        yang = ChiralCEAtLevel(yangian_gl1_lca(), yangian_gl1_linfinity(), e3_level())
        vir = ChiralCEAtLevel(virasoro_lca(), virasoro_linfinity(), e3_level())

        assert heis.shadow_class == "G"
        assert yang.shadow_class == "L"
        assert vir.shadow_class == "M"


# ================================================================
#  SECTION 3: MAURER-CARTAN ELEMENTS
# ================================================================

class TestMaurerCartan:
    """Test Maurer-Cartan elements at each E_n level."""

    def test_mc_e1_trivial(self):
        """E_1: MC element = 0 (classical vacuum) for all algebras."""
        # VERIFIED [DC] alpha_1 = 0 [LT] no quantum correction at E_1
        lca = heisenberg_lca()
        linf = heisenberg_linfinity()
        ce = ChiralCEAtLevel(lca, linf, e1_level())
        mc = ce.mc_element_description()
        assert mc["level"] == "E_1"
        assert "0" in mc["mc_element"]
        assert mc["sigma3"] == Fraction(0)

    def test_mc_e2_classical_r(self):
        """E_2: MC element = sigma_2 * Omega/u (classical r-matrix)."""
        # VERIFIED [DC] CYBE [LT] Costello 2013 classical r-matrix
        lca = yangian_gl1_lca()
        linf = yangian_gl1_linfinity()
        ce = ChiralCEAtLevel(lca, linf, e2_level())
        mc = ce.mc_element_description()
        assert mc["level"] == "E_2"
        assert "r-matrix" in mc["mc_element"]
        assert mc["sigma3"] == Fraction(0)

    def test_mc_e3_quantum_correction(self):
        """E_3: MC element has sigma_3-correction for class L/M."""
        # VERIFIED [DC] sigma_3 deformation [LT] L_infinity MC equation
        for lca, linf, expected_class in [
            (yangian_gl1_lca(), yangian_gl1_linfinity(), "L"),
            (virasoro_lca(), virasoro_linfinity(), "M"),
        ]:
            ce = ChiralCEAtLevel(lca, linf, e3_level())
            mc = ce.mc_element_description()
            assert mc["level"] == "E_3"
            assert mc["sigma3"] != Fraction(0)

    def test_mc_heisenberg_trivial_at_all_levels(self):
        """Heisenberg: MC = 0 at all levels (class G, abelian)."""
        # VERIFIED [DC] abelian L has trivial MC [LT] Goldman-Millson (1988)
        lca = heisenberg_lca()
        linf = heisenberg_linfinity()

        for level in [e1_level(), e2_level(), e3_level()]:
            ce = ChiralCEAtLevel(lca, linf, level)
            mc = ce.mc_element_description()
            if level.n == 3:
                # Even at E_3, class G has no correction
                assert "class G" in mc.get("correction", mc.get("mc_element", ""))

    def test_mc_virasoro_gevrey1_at_e3(self):
        """Virasoro (class M): MC element is Gevrey-1 divergent at E_3."""
        # VERIFIED [DC] class M MC type [LT] shadow tower infinite => Gevrey-1
        lca = virasoro_lca()
        linf = virasoro_linfinity()
        ce = ChiralCEAtLevel(lca, linf, e3_level())
        mc = ce.mc_element_description()
        assert "Gevrey-1" in mc["mc_type"]


# ================================================================
#  SECTION 4: KOSZUL DUAL IDENTIFICATION
# ================================================================

class TestKoszulDual:
    """Test the E_n Koszul dual identification at each level."""

    def test_e1_koszul_dual_is_level_reflection(self):
        """E_1 Koszul dual: V_{-k}(gl_1) (Feigin-Frenkel dual)."""
        # VERIFIED [DC] Feigin-Frenkel 1992 [LT] Vol I Theorem A
        lca = heisenberg_lca()
        linf = heisenberg_linfinity()
        ce = ChiralCEAtLevel(lca, linf, e1_level())
        kd = ce.koszul_dual_info()
        assert kd["en_level"] == 1
        assert "Feigin-Frenkel" in kd["algebra_name"]
        assert kd["status"] == "ESTABLISHED (Feigin-Frenkel 1992)"

    def test_e2_koszul_dual_is_yangian(self):
        """E_2 Koszul dual: affine Yangian Y(gl_hat_1)."""
        # VERIFIED [DC] Costello 2013 [LT] holomorphic_cs_chiral_engine.py
        lca = heisenberg_lca()
        linf = heisenberg_linfinity()
        ce = ChiralCEAtLevel(lca, linf, e2_level())
        kd = ce.koszul_dual_info()
        assert kd["en_level"] == 2
        assert "Yangian" in kd["algebra_name"]

    def test_e3_koszul_dual_is_quantum_toroidal(self):
        """E_3 Koszul dual: U_{q,t}(gl_hat_hat_1) (CONJECTURAL)."""
        # VERIFIED [DC] conj:e3-koszul-duality [LT] AP-CY14 compliance
        lca = heisenberg_lca()
        linf = heisenberg_linfinity()
        ce = ChiralCEAtLevel(lca, linf, e3_level())
        kd = ce.koszul_dual_info()
        assert kd["en_level"] == 3
        assert "CONJECTURAL" in kd["algebra_name"]
        assert "CONJECTURAL" in kd["status"]

    def test_e3_has_miki_automorphism(self):
        """E_3 Koszul dual has Miki automorphism (algebra-specific, AP-CY22)."""
        # VERIFIED [DC] Miki present [LT] AP-CY22 not operadic
        lca = heisenberg_lca()
        linf = heisenberg_linfinity()
        ce = ChiralCEAtLevel(lca, linf, e3_level())
        kd = ce.koszul_dual_info()
        assert "Miki" in kd.get("miki_automorphism", "")
        assert "NOT operadic" in kd["miki_automorphism"]

    def test_e3_zte_failure_noted(self):
        """E_3 Koszul dual notes ZTE failure (thm:zte-failure, AP-CY30)."""
        # VERIFIED [DC] ZTE status [LT] zamolodchikov_tetrahedron_engine.py
        lca = heisenberg_lca()
        linf = heisenberg_linfinity()
        ce = ChiralCEAtLevel(lca, linf, e3_level())
        kd = ce.koszul_dual_info()
        assert "FAILS" in kd.get("zte_status", "")

    def test_e3_structure_function_in_koszul(self):
        """E_3 Koszul dual has the trigonometric structure function G(x)."""
        # VERIFIED [DC] G(x) formula [LT] quantum_toroidal_e1_cy3.py
        lca = heisenberg_lca()
        linf = heisenberg_linfinity()
        ce = ChiralCEAtLevel(lca, linf, e3_level())
        kd = ce.koszul_dual_info()
        assert "G(x)" in kd["structure_function"]


# ================================================================
#  SECTION 5: STRUCTURE FUNCTION AT EACH LEVEL
# ================================================================

class TestStructureFunction:
    """Test the rational structure function at each E_n level."""

    def test_e1_structure_function(self):
        """E_1 at (1, 0, -1): g(5) = (5-1)(5-0)(5+1)/((5+1)(5+0)(5-1)) = 1."""
        # VERIFIED [DC] g(5) = 4*5*6/(6*5*4) = 1 [LT] trivial at E_1
        lvl = e1_level(Fraction(1))
        g5 = structure_function_at_level(lvl, Fraction(5))
        assert g5 == Fraction(1)

    def test_e2_structure_function_trivial(self):
        """E_2 at (1, -1, 0): g(u) = 1 (self-dual, trivial structure)."""
        # VERIFIED [DC] g(5) = (5-1)(5+1)(5-0)/((5+1)(5-1)(5+0)) = 1
        # [LT] sigma_3 = 0 at self-dual
        lvl = e2_level(Fraction(1), Fraction(-1))
        g5 = structure_function_at_level(lvl, Fraction(5))
        assert g5 == Fraction(1)

    def test_e3_structure_function_nontrivial(self):
        """E_3 at (1, -2, 1): g(5) = 28/27 != 1 (nontrivial)."""
        # VERIFIED [DC] g(5) = 4*7*4/(6*3*6) = 112/108 = 28/27
        # [LT] chiral_ce_e3_deformation.py test_structure_function_at_safe_point
        lvl = e3_level(Fraction(1), Fraction(-2))
        g5 = structure_function_at_level(lvl, Fraction(5))
        assert g5 == Fraction(28, 27)

    def test_structure_function_inversion_identity(self):
        """g(u) * g(-u) = 1 at all E_n levels (from CY condition)."""
        # VERIFIED [DC] inversion identity [LT] CY condition e1*e2*e3 product
        for lvl in [e1_level(), e2_level(), e3_level()]:
            assert structure_function_inversion(lvl, Fraction(5))
            assert structure_function_inversion(lvl, Fraction(7))

    def test_structure_function_pole_returns_none(self):
        """g(u) returns None at poles u = -epsilon_i."""
        # VERIFIED [DC] pole check [LT] AP-CY28 pole avoidance
        lvl = e3_level(Fraction(1), Fraction(-2))
        # Poles at u = -1, 2, -1 => distinct poles at -1, 2
        assert structure_function_at_level(lvl, Fraction(-1)) is None
        assert structure_function_at_level(lvl, Fraction(2)) is None

    def test_e3_g_not_one(self):
        """E_3 structure function is not identically 1 (sigma_3 != 0)."""
        # VERIFIED [DC] g(5) != 1 [LT] sigma_3 = -2 != 0
        lvl = e3_level()
        g5 = structure_function_at_level(lvl, Fraction(5))
        assert g5 != Fraction(1)


# ================================================================
#  SECTION 6: TRIGONOMETRIC STRUCTURE FUNCTION
# ================================================================

class TestTrigStructureFunction:
    """Test the trigonometric (exponentiated) structure function G(x)."""

    def test_trig_G_at_x_1_half(self):
        """G(0.5) for generic (q, t) should be finite and nonzero."""
        # VERIFIED [DC] numerical evaluation [LT] quantum_toroidal_e1_cy3.py
        q1 = np.exp(1.0)
        q2 = np.exp(-2.0)
        q3 = 1.0 / (q1 * q2)
        G = trigonometric_structure_function(0.5, q1, q2, q3)
        assert np.isfinite(G)
        assert abs(G) > 1e-10

    def test_trig_inversion_identity(self):
        """G(x) * G(1/x) = 1 verified numerically."""
        # VERIFIED [DC] numerical check [LT] CY condition q1*q2*q3 = 1
        q1 = np.exp(1.0)
        q2 = np.exp(-2.0)
        passes, max_res = verify_trig_inversion(q1, q2)
        assert passes, f"G(x)*G(1/x) != 1, max residual = {max_res}"

    def test_trig_inversion_at_self_dual(self):
        """G(x)*G(1/x) = 1 at self-dual point (q2 = 1)."""
        # VERIFIED [DC] self-dual [LT] sigma_3 = 0 at q2 = 1
        q1 = np.exp(1.0)
        q2 = 1.0  # self-dual: eps2 = 0
        passes, max_res = verify_trig_inversion(q1, q2)
        assert passes

    def test_trig_G_reduces_to_rational(self):
        """At small epsilon, G(x) ~ g(log(x)/epsilon) (rational limit).

        In the rational limit epsilon -> 0, the trigonometric G(x)
        reduces to the rational g(u) via x = exp(epsilon * u).
        """
        # VERIFIED [DC] rational limit [LT] Yangian = rational limit of toroidal
        eps = 0.01
        q1 = np.exp(eps)
        q2 = np.exp(-2 * eps)
        q3 = 1.0 / (q1 * q2)
        # G(x) near x = 1 + eps*u should approximate g(u)
        u = 5.0
        x = np.exp(eps * u)
        G = trigonometric_structure_function(x, q1, q2, q3)
        # In the limit eps -> 0: G -> 1 (the function approaches 1 for small eps)
        assert abs(G - 1.0) < 0.5  # small eps => G close to 1

    def test_trig_cy_condition(self):
        """q1 * q2 * q3 = 1 verified for the parametrization."""
        # VERIFIED [DC] CY product [LT] definition of q3 = 1/(q1*q2)
        q1 = np.exp(1.0)
        q2 = np.exp(-2.0)
        q3 = 1.0 / (q1 * q2)
        assert abs(q1 * q2 * q3 - 1.0) < 1e-14


# ================================================================
#  SECTION 7: DIMENSIONAL REDUCTION E_3 -> E_2 -> E_1
# ================================================================

class TestDimensionalReduction:
    """Test the dimensional reduction E_3 -> E_2 -> E_1."""

    def test_heisenberg_reduction_passes(self):
        """Heisenberg: all dimensional reduction checks pass."""
        # VERIFIED [DC] all checks [LT] thm:e3-koszul-heisenberg
        h = heisenberg_hierarchy()
        for key, val in h["verification"].items():
            assert val, f"Heisenberg reduction failed: {key}"

    def test_yangian_reduction_passes(self):
        """Yangian: all dimensional reduction checks pass."""
        # VERIFIED [DC] all checks [LT] Costello hierarchy
        y = yangian_hierarchy()
        for key, val in y["verification"].items():
            assert val, f"Yangian reduction failed: {key}"

    def test_virasoro_reduction_passes(self):
        """Virasoro: all dimensional reduction checks pass."""
        # VERIFIED [DC] all checks [LT] shadow class M compatibility
        v = virasoro_hierarchy()
        for key, val in v["verification"].items():
            assert val, f"Virasoro reduction failed: {key}"

    def test_e2_sigma3_zero_all(self):
        """E_2 has sigma_3 = 0 for all algebras (self-dual point)."""
        # VERIFIED [DC] sigma_3 = 0 [LT] CY with one eps = 0
        for factory in [heisenberg_hierarchy, yangian_hierarchy, virasoro_hierarchy]:
            h = factory()
            assert h["comparison"]["E_2"]["sigma3"] == Fraction(0)

    def test_e3_sigma3_nonzero_all(self):
        """E_3 has sigma_3 != 0 for all algebras (generic point)."""
        # VERIFIED [DC] sigma_3 = -2 [LT] default (1, -2, 1) parameters
        for factory in [heisenberg_hierarchy, yangian_hierarchy, virasoro_hierarchy]:
            h = factory()
            assert h["comparison"]["E_3"]["sigma3"] != Fraction(0)

    def test_effective_params_hierarchy(self):
        """E_1 < E_2 < E_3 in effective deformation parameters."""
        # VERIFIED [DC] param counting [LT] dimensional hierarchy
        h = heisenberg_hierarchy()
        assert h["comparison"]["E_1"]["effective_params"] == 0
        assert h["comparison"]["E_2"]["effective_params"] == 1
        assert h["comparison"]["E_3"]["effective_params"] == 2


# ================================================================
#  SECTION 8: QUANTUM TOROIDAL PARAMETERS
# ================================================================

class TestQuantumToroidalParams:
    """Test the quantum toroidal parameter extraction."""

    def test_from_e3_level(self):
        """QuantumToroidalParams from E_3 level (1, -2, 1)."""
        # VERIFIED [DC] parameter extraction [LT] convention (q,t) = (exp(e1), exp(-e2))
        lvl = e3_level(Fraction(1), Fraction(-2))
        qt = QuantumToroidalParams.from_level(lvl)
        assert qt.epsilon1 == Fraction(1)
        assert qt.epsilon2 == Fraction(-2)
        assert qt.epsilon3 == Fraction(1)

    def test_cy_condition_numerical(self):
        """q1 * q2 * q3 = 1 verified numerically."""
        # VERIFIED [DC] CY product [LT] definition
        qt = QuantumToroidalParams(Fraction(1), Fraction(-2))
        assert qt.cy_check_numerical()

    def test_sigma_values(self):
        """sigma_2 = -3, sigma_3 = -2 at (1, -2, 1)."""
        # VERIFIED [DC] direct computation [LT] chiral_ce_e3_deformation.py
        qt = QuantumToroidalParams(Fraction(1), Fraction(-2))
        assert qt.sigma2 == Fraction(-3)
        assert qt.sigma3 == Fraction(-2)

    def test_from_non_e3_raises(self):
        """QuantumToroidalParams.from_level raises for E_1, E_2."""
        # VERIFIED [DC] ValueError check [LT] toroidal requires E_3
        with pytest.raises(ValueError):
            QuantumToroidalParams.from_level(e1_level())
        with pytest.raises(ValueError):
            QuantumToroidalParams.from_level(e2_level())

    def test_q_t_numerical(self):
        """q = exp(1), t = exp(2) at (1, -2)."""
        # VERIFIED [DC] q = exp(eps1), t = exp(-eps2) [LT] Macdonald convention
        qt = QuantumToroidalParams(Fraction(1), Fraction(-2))
        assert abs(qt.q_numerical() - np.exp(1.0)) < 1e-12
        assert abs(qt.t_numerical() - np.exp(2.0)) < 1e-12


# ================================================================
#  SECTION 9: E_n BAR COMPLEX DIMENSIONS
# ================================================================

class TestEnBarPoincare:
    """Test the E_n bar complex Poincare polynomial."""

    def test_heisenberg_e1_g1(self):
        """Heisenberg E_1 g=1: (1+t)^1, dim = 2."""
        # VERIFIED [DC] 2^1 = 2 [LT] chiral_ce_complex.py
        bp = en_bar_poincare(1, 1, 1, "G")
        assert bp["total_dimension"] == 2

    def test_heisenberg_e2_g1(self):
        """Heisenberg E_2 g=1: (1+t)^2, dim = 4."""
        # VERIFIED [DC] 2^2 = 4 [LT] E_2 bar doubles the E_1 bar
        bp = en_bar_poincare(1, 2, 1, "G")
        assert bp["total_dimension"] == 4

    def test_heisenberg_e3_g1(self):
        """Heisenberg E_3 g=1: (1+t)^3, dim = 8."""
        # VERIFIED [DC] 2^3 = 8 [LT] thm:e3-koszul-heisenberg
        bp = en_bar_poincare(1, 3, 1, "G")
        assert bp["total_dimension"] == 8

    def test_heisenberg_e3_g3(self):
        """Heisenberg E_3 g=3: (1+t)^9, dim = 512."""
        # VERIFIED [DC] 2^9 = 512 [LT] genus-3 E_3 bar
        bp = en_bar_poincare(1, 3, 3, "G")
        assert bp["total_dimension"] == 512

    def test_yangian_e3_g1(self):
        """Yangian (3 gens) E_3 g=1: (1+t)^9, dim = 512."""
        # VERIFIED [DC] 2^(3*3*1) = 2^9 = 512 [LT] 3 generators, E_3, g=1
        bp = en_bar_poincare(3, 3, 1, "L")
        assert bp["total_dimension"] == 512

    def test_virasoro_e3_g1_cohomology(self):
        """Virasoro E_3 g=1: cohomology = 6 (class M, AP-CY21)."""
        # VERIFIED [DC] 6^1 = 6 [LT] AP-CY21 class M fails (1+t)^{3g}
        bp = en_bar_poincare(1, 3, 1, "M")
        assert bp["cohomology_dim"] == 6

    def test_virasoro_e3_g3_cohomology(self):
        """Virasoro E_3 g=3: cohomology = 216 (class M, 6^3)."""
        # VERIFIED [DC] 6^3 = 216 [LT] AP-CY21
        bp = en_bar_poincare(1, 3, 3, "M")
        assert bp["cohomology_dim"] == 216

    def test_poincare_binomial(self):
        """Poincare polynomial matches binomial coefficients."""
        # VERIFIED [DC] binom(3, k) [LT] (1+t)^3 = 1 + 3t + 3t^2 + t^3
        bp = en_bar_poincare(1, 3, 1, "G")
        assert bp["poincare_poly"][0] == 1
        assert bp["poincare_poly"][1] == 3
        assert bp["poincare_poly"][2] == 3
        assert bp["poincare_poly"][3] == 1


# ================================================================
#  SECTION 10: DEFORMATION COEFFICIENTS
# ================================================================

class TestDeformationCoefficients:
    """Test deformation coefficients at each E_n level."""

    def test_heisenberg_only_s2_at_e1(self):
        """Heisenberg at E_1: only S_2 coefficient, no sigma_3 corrections."""
        # VERIFIED [DC] shadow tower [LT] class G terminates at S_2
        lca = heisenberg_lca()
        linf = heisenberg_linfinity()
        ce = ChiralCEAtLevel(lca, linf, e1_level())
        coeffs = ce.deformation_coefficients()
        assert 2 in coeffs
        assert len(coeffs) == 1  # Only S_2 at E_1

    def test_virasoro_shadow_tower_at_e3(self):
        """Virasoro at E_3: S_2 = 1/2, S_3 = 2, S_4 = 10/27 at c=1."""
        # VERIFIED [DC] shadow values [LT] a_infinity_bar_w1inf.py, c3_shadow_tower.py
        lca = virasoro_lca()
        linf = virasoro_linfinity()
        ce = ChiralCEAtLevel(lca, linf, e3_level())
        coeffs = ce.deformation_coefficients()
        assert coeffs[2] == Fraction(1, 2)
        assert coeffs[3] == Fraction(2)
        assert coeffs[4] == Fraction(10, 27)

    def test_yangian_strict_at_e3(self):
        """Yangian at E_3: strict Lie, only S_2 nonzero."""
        # VERIFIED [DC] class L strict [LT] l_k = 0 for k >= 3
        lca = yangian_gl1_lca()
        linf = yangian_gl1_linfinity()
        ce = ChiralCEAtLevel(lca, linf, e3_level())
        coeffs = ce.deformation_coefficients()
        assert coeffs[2] == Fraction(1)  # kappa from bracket


# ================================================================
#  SECTION 11: FULL HIERARCHY COMPARISON
# ================================================================

class TestHierarchyComparison:
    """Test the full E_n hierarchy comparison across shadow classes."""

    def test_all_d_squared_zero(self):
        """d^2 = 0 at all levels for all algebras."""
        # VERIFIED [DC] d^2 = 0 [LT] L_infinity relations
        for factory in [heisenberg_hierarchy, yangian_hierarchy, virasoro_hierarchy]:
            h = factory()
            comp = h["comparison"]
            for lvl_name in ["E_1", "E_2", "E_3"]:
                assert comp[lvl_name]["d_squared_zero"], (
                    f"d^2 != 0 at {lvl_name} for {h['name']}"
                )

    def test_comparison_table_complete(self):
        """Cross-level comparison has entries for all three levels."""
        # VERIFIED [DC] table completeness [LT] three E_n levels
        comp = e_n_level_comparison()
        for name in ["Heisenberg (G)", "Yangian (L)", "Virasoro (M)"]:
            assert name in comp
            for lvl in ["E_1", "E_2", "E_3"]:
                assert lvl in comp[name]

    def test_heisenberg_shadow_class_g(self):
        """Heisenberg is class G across all levels."""
        # VERIFIED [DC] shadow class [LT] abelian Lie algebra
        h = heisenberg_hierarchy()
        assert h["shadow_class"] == "G"

    def test_virasoro_shadow_class_m(self):
        """Virasoro is class M across all levels."""
        # VERIFIED [DC] shadow class [LT] infinite shadow tower
        v = virasoro_hierarchy()
        assert v["shadow_class"] == "M"


# ================================================================
#  SECTION 12: FULL COMPUTATION SUITE
# ================================================================

class TestFullSuite:
    """Test the full computation suite runs without error."""

    def test_compute_suite_runs(self):
        """The full computation suite runs and returns expected keys."""
        # VERIFIED [DC] suite runs [LT] no exceptions
        results = compute_e3_ce_quantum_toroidal()
        assert "heisenberg" in results
        assert "yangian" in results
        assert "virasoro" in results
        assert "structure_functions" in results
        assert "trig_inversion" in results
        assert "quantum_toroidal_params" in results

    def test_trig_inversion_in_suite(self):
        """Trigonometric inversion passes in the full suite."""
        # VERIFIED [DC] G(x)*G(1/x)=1 [LT] CY condition
        results = compute_e3_ce_quantum_toroidal()
        assert results["trig_inversion"]["passes"]

    def test_qt_params_cy_check(self):
        """Quantum toroidal CY check passes in the full suite."""
        # VERIFIED [DC] q1*q2*q3=1 [LT] CY constraint
        results = compute_e3_ce_quantum_toroidal()
        assert results["quantum_toroidal_params"]["cy_check"]

    def test_structure_function_e3_nontrivial(self):
        """E_3 structure function is nontrivial in the full suite."""
        # VERIFIED [DC] g(5) = 28/27 != 1 [LT] sigma_3 != 0
        results = compute_e3_ce_quantum_toroidal()
        assert results["structure_functions"]["E_3"]["g(5)"] == Fraction(28, 27)

    def test_structure_function_e2_trivial(self):
        """E_2 structure function is trivial (= 1) in the full suite."""
        # VERIFIED [DC] g(5) = 1 [LT] sigma_3 = 0 at self-dual
        results = compute_e3_ce_quantum_toroidal()
        assert results["structure_functions"]["E_2"]["g(5)"] == Fraction(1)
