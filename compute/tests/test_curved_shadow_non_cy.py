r"""
Tests for the curved shadow obstruction tower for non-CY geometries.

VERIFICATION AXES (multi-path, per CLAUDE.md mandate):

  1. CY defect computation: delta = deg(K_C) - deg(L) for all standard surfaces
  2. CY locus: delta = 0 iff the geometry is CY (Tot(K_C -> C))
  3. Curved kappa: kappa^{crv} = kappa + delta^2 * chi(C) / 24
  4. CY limit: delta -> 0 recovers the uncurved tower at every level
  5. Genus amplitudes: F_g^{crv} = kappa^{crv} * a_hat_g
  6. Koszul duality: kappa^{crv} is invariant under delta -> -delta
  7. Base curve dependence: chi(C) = 0 (torus) kills the correction
  8. Arity structure: arity-0 = m_0 = delta, arity-1 = correction
  9. Inhomogeneous MC: integrability checks at each arity
 10. Coderived category: D^co = D^b iff CY
 11. Partition function: tree-level F_0 = delta^2 / 2
 12. Shadow metric and depth class: preserved under curvature
 13. Landscape consistency: all examples pass all checks
 14. Cross-checks: multiple independent derivations agree

Ground truth:
  Positselski, "Two kinds of derived categories" (2011)
  Lefevre-Hasegawa, thesis (2003)
  Keller, "A-infinity algebras, modules and functor categories" (2006)
  Vol I: bar_cobar_adjunction_curved.tex
  Vol I: higher_genus_modular_koszul.tex
"""

import math
import os
import sys
import importlib.util
from fractions import Fraction

import pytest

# Load module under test
_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')
_spec = importlib.util.spec_from_file_location(
    'curved_shadow_non_cy',
    os.path.join(_lib_dir, 'curved_shadow_non_cy.py')
)
csn = importlib.util.module_from_spec(_spec)
sys.modules['curved_shadow_non_cy'] = csn
_spec.loader.exec_module(csn)


# =========================================================================
# 1. CY DEFECT COMPUTATION
# =========================================================================

class TestCYDefect:
    """Verify the CY defect delta = deg(K_C) - deg(L) for all standard surfaces."""

    def test_tot_O_P1_delta(self):
        """Tot(O -> P^1): delta = (-2) - 0 = -2."""
        surf = csn.tot_O_P1()
        assert surf.delta == -2

    def test_tot_O_minus2_P1_delta(self):
        """Tot(O(-2) -> P^1) = T*P^1: delta = (-2) - (-2) = 0 (CY)."""
        surf = csn.tot_O_minus2_P1()
        assert surf.delta == 0

    def test_tot_O_minus1_P1_delta(self):
        """Tot(O(-1) -> P^1): delta = (-2) - (-1) = -1."""
        surf = csn.tot_O_minus1_P1()
        assert surf.delta == -1

    def test_tot_O_1_P1_delta(self):
        """Tot(O(1) -> P^1): delta = (-2) - 1 = -3."""
        surf = csn.tot_O_1_P1()
        assert surf.delta == -3

    def test_tot_O_E_delta(self):
        """Tot(O -> E): delta = 0 - 0 = 0 (CY)."""
        surf = csn.tot_O_E()
        assert surf.delta == 0

    def test_tot_O_1_E_delta(self):
        """Tot(O(1) -> E): delta = 0 - 1 = -1."""
        surf = csn.tot_O_1_E()
        assert surf.delta == -1

    def test_tot_K_P1_is_cy(self):
        """Tot(K_{P^1} -> P^1): delta = 0 always (by definition)."""
        surf = csn.tot_K_C(0)
        assert surf.delta == 0
        assert surf.is_cy

    def test_tot_K_genus2_is_cy(self):
        """Tot(K_C -> C_2): delta = 0 for any genus."""
        surf = csn.tot_K_C(2)
        assert surf.delta == 0
        assert surf.is_cy

    def test_tot_K_genus5_is_cy(self):
        """Tot(K_C -> C_5): delta = 0."""
        surf = csn.tot_K_C(5)
        assert surf.delta == 0
        assert surf.is_cy

    def test_delta_formula_genus0(self):
        """For P^1 (g=0): delta = -2 - deg(L)."""
        for deg in range(-5, 6):
            surf = csn.tot_O_genus_g(0, deg)
            assert surf.delta == -2 - deg, f"Failed for deg={deg}"

    def test_delta_formula_genus1(self):
        """For E (g=1): delta = 0 - deg(L) = -deg(L)."""
        for deg in range(-5, 6):
            surf = csn.tot_O_genus_g(1, deg)
            assert surf.delta == -deg, f"Failed for deg={deg}"

    def test_delta_formula_genus_g(self):
        """For C_g: delta = (2g-2) - deg(L)."""
        for g in range(0, 6):
            for deg in range(-3, 4):
                surf = csn.tot_O_genus_g(g, deg)
                assert surf.delta == (2*g - 2) - deg


# =========================================================================
# 2. CY LOCUS: delta = 0
# =========================================================================

class TestCYLocus:
    """Verify that delta = 0 iff the geometry is CY."""

    def test_cy_surfaces_have_delta_zero(self):
        """All CY surfaces have delta = 0."""
        cy_surfaces = [
            csn.tot_O_minus2_P1(),    # T*P^1
            csn.tot_O_E(),             # E x C
            csn.tot_K_C(0),            # T*P^1 (same)
            csn.tot_K_C(1),            # T*E
            csn.tot_K_C(2),            # T*C_2
            csn.tot_K_C(3),            # T*C_3
        ]
        for surf in cy_surfaces:
            assert surf.is_cy, f"{surf.name} should be CY"
            assert surf.delta == 0, f"{surf.name} should have delta=0"

    def test_non_cy_have_delta_nonzero(self):
        """Non-CY surfaces have delta != 0."""
        non_cy = [
            csn.tot_O_P1(),
            csn.tot_O_minus1_P1(),
            csn.tot_O_1_P1(),
            csn.tot_O_1_E(),
        ]
        for surf in non_cy:
            assert not surf.is_cy, f"{surf.name} should not be CY"
            assert surf.delta != 0, f"{surf.name} should have delta != 0"

    def test_cy_iff_L_equals_K(self):
        """CY iff deg(L) = deg(K_C) = 2g-2."""
        for g in range(0, 5):
            for deg in range(-5, 6):
                surf = csn.tot_O_genus_g(g, deg)
                expected_cy = (deg == 2*g - 2)
                assert surf.is_cy == expected_cy, \
                    f"g={g}, deg={deg}: expected CY={expected_cy}, got {surf.is_cy}"


# =========================================================================
# 3. CURVED KAPPA
# =========================================================================

class TestCurvedKappa:
    """Verify kappa^{crv} = kappa + delta^2 * chi(C) / 24."""

    def test_curved_kappa_formula_P1(self):
        """For P^1: kappa^{crv} = kappa + delta^2 * 2 / 24 = kappa + delta^2/12."""
        kappa = Fraction(1)
        chi = 2
        for delta in range(-5, 6):
            k_crv = csn.compute_curved_kappa(kappa, Fraction(delta), chi)
            expected = kappa + Fraction(delta**2 * chi, 24)
            assert k_crv == expected, f"delta={delta}: got {k_crv}, expected {expected}"

    def test_curved_kappa_formula_E(self):
        """For E: kappa^{crv} = kappa (no correction, chi(E)=0)."""
        kappa = Fraction(1)
        chi = 0
        for delta in range(-5, 6):
            k_crv = csn.compute_curved_kappa(kappa, Fraction(delta), chi)
            assert k_crv == kappa, f"delta={delta}: got {k_crv}, expected {kappa}"

    def test_curved_kappa_formula_genus2(self):
        """For genus 2: kappa^{crv} = kappa - delta^2/12 (chi = -2)."""
        kappa = Fraction(1)
        chi = -2
        for delta in range(-3, 4):
            k_crv = csn.compute_curved_kappa(kappa, Fraction(delta), chi)
            expected = kappa + Fraction(delta**2 * chi, 24)
            assert k_crv == expected

    def test_curved_kappa_quadratic_in_delta(self):
        """kappa^{crv}(delta) is a quadratic function of delta."""
        kappa = Fraction(3)
        chi = 2
        # Check kappa^{crv}(-d) = kappa^{crv}(d) (even in delta)
        for d in range(1, 6):
            k_plus = csn.compute_curved_kappa(kappa, Fraction(d), chi)
            k_minus = csn.compute_curved_kappa(kappa, Fraction(-d), chi)
            assert k_plus == k_minus, f"d={d}: even symmetry failed"

    def test_curved_kappa_at_delta_0_is_uncurved(self):
        """At delta = 0: kappa^{crv} = kappa."""
        for kappa_val in [Fraction(1), Fraction(5), Fraction(-25, 3)]:
            for chi in [-2, 0, 2]:
                k_crv = csn.compute_curved_kappa(kappa_val, Fraction(0), chi)
                assert k_crv == kappa_val

    def test_curved_kappa_P1_explicit_values(self):
        """Explicit kappa^{crv} values for O(deg) -> P^1 with kappa_cy=1."""
        kappa = Fraction(1)
        # delta = -2 - deg, chi = 2
        # kappa^{crv} = 1 + (2+deg)^2 / 12
        expected = {
            -4: Fraction(1) + Fraction(4, 12),     # delta=2, (2)^2/12 = 1/3
            -3: Fraction(1) + Fraction(1, 12),     # delta=1, 1/12
            -2: Fraction(1),                        # delta=0, CY!
            -1: Fraction(1) + Fraction(1, 12),     # delta=-1, 1/12
             0: Fraction(1) + Fraction(4, 12),     # delta=-2, 4/12=1/3
             1: Fraction(1) + Fraction(9, 12),     # delta=-3, 9/12=3/4
             2: Fraction(1) + Fraction(16, 12),    # delta=-4, 16/12=4/3
        }
        for deg, exp in expected.items():
            surf = csn.tot_O_genus_g(0, deg)
            data = csn.curved_data_from_surface(surf, kappa)
            tower = csn.build_curved_shadow_tower(data)
            assert tower.kappa_curved == exp, \
                f"deg={deg}: got {tower.kappa_curved}, expected {exp}"


# =========================================================================
# 4. CY LIMIT: delta -> 0 recovers uncurved tower
# =========================================================================

class TestCYLimit:
    """Verify that the curved tower reduces to the uncurved tower at delta = 0."""

    def test_cy_limit_arity_0_vanishes(self):
        """At delta = 0: arity-0 curvature vanishes."""
        for kappa in [Fraction(1), Fraction(2), Fraction(5)]:
            surf = csn.tot_O_minus2_P1()  # CY
            data = csn.curved_data_from_surface(surf, kappa)
            tower = csn.build_curved_shadow_tower(data)
            assert tower.arity_0_curvature == 0

    def test_cy_limit_arity_1_vanishes(self):
        """At delta = 0: arity-1 correction vanishes."""
        for kappa in [Fraction(1), Fraction(2), Fraction(5)]:
            surf = csn.tot_O_minus2_P1()  # CY
            data = csn.curved_data_from_surface(surf, kappa)
            tower = csn.build_curved_shadow_tower(data)
            assert tower.arity_1_correction == 0

    def test_cy_limit_kappa_matches(self):
        """At delta = 0: kappa^{crv} = kappa."""
        for kappa in [Fraction(1), Fraction(2), Fraction(5), Fraction(-25, 3)]:
            surf = csn.tot_O_minus2_P1()  # CY
            data = csn.curved_data_from_surface(surf, kappa)
            tower = csn.build_curved_shadow_tower(data)
            assert tower.kappa_curved == kappa

    def test_cy_limit_genus_amplitudes(self):
        """At delta = 0: F_g^{crv} = F_g = kappa * a_hat_g."""
        for kappa in [Fraction(1), Fraction(5)]:
            surf = csn.tot_O_minus2_P1()  # CY
            data = csn.curved_data_from_surface(surf, kappa)
            tower = csn.build_curved_shadow_tower(data)
            for g in range(1, 6):
                if g in csn.A_HAT_COEFFICIENTS:
                    expected = kappa * csn.A_HAT_COEFFICIENTS[g]
                    assert tower.genus_amplitudes[g] == expected, \
                        f"g={g}: got {tower.genus_amplitudes[g]}, expected {expected}"

    def test_cy_limit_F0_vanishes(self):
        """At delta = 0: genus-0 curvature self-energy F_0 = 0."""
        surf = csn.tot_O_minus2_P1()  # CY
        data = csn.curved_data_from_surface(surf, Fraction(1))
        tower = csn.build_curved_shadow_tower(data)
        assert tower.genus_amplitudes[0] == 0

    def test_cy_limit_check_all_pass(self):
        """All CY limit checks pass for a CY surface."""
        kappa = Fraction(5)
        surf = csn.tot_O_minus2_P1()
        data = csn.curved_data_from_surface(surf, kappa)
        tower = csn.build_curved_shadow_tower(data)
        checks = csn.cy_limit_check(tower, kappa)
        for name, ok in checks.items():
            assert ok, f"CY limit check '{name}' failed"

    def test_cy_limit_torus(self):
        """Tot(O -> E) is CY, tower matches uncurved."""
        kappa = Fraction(1)
        surf = csn.tot_O_E()
        data = csn.curved_data_from_surface(surf, kappa)
        tower = csn.build_curved_shadow_tower(data)
        checks = csn.cy_limit_check(tower, kappa)
        for name, ok in checks.items():
            assert ok, f"Torus CY limit check '{name}' failed"

    def test_cy_limit_function(self):
        """cy_limit_tower returns consistent data."""
        kappa = Fraction(2)
        result = csn.cy_limit_tower(kappa)
        assert result["delta"] == 0
        assert result["m_0"] == 0
        assert result["Theta_1"] == 0
        assert result["kappa_crv"] == kappa
        assert result["kappa_match"] is True


# =========================================================================
# 5. GENUS AMPLITUDES
# =========================================================================

class TestGenusAmplitudes:
    """Verify F_g^{crv} = kappa^{crv} * a_hat_g for g >= 1."""

    def test_genus_1_formula(self):
        """F_1^{crv} = kappa^{crv} / 24."""
        for d in range(-3, 4):
            kappa = Fraction(1)
            k_crv = csn.compute_curved_kappa(kappa, Fraction(d), 2)
            f1 = csn.compute_curved_genus_amplitude(k_crv, Fraction(d), 2, 1)
            assert f1 == k_crv / Fraction(24)

    def test_genus_2_formula(self):
        """F_2^{crv} = 7 * kappa^{crv} / 5760."""
        kappa = Fraction(1)
        k_crv = csn.compute_curved_kappa(kappa, Fraction(2), 2)
        f2 = csn.compute_curved_genus_amplitude(k_crv, Fraction(2), 2, 2)
        assert f2 == Fraction(7) * k_crv / Fraction(5760)

    def test_genus_3_formula(self):
        """F_3^{crv} = 31 * kappa^{crv} / 967680."""
        kappa = Fraction(2)
        k_crv = csn.compute_curved_kappa(kappa, Fraction(3), 2)
        f3 = csn.compute_curved_genus_amplitude(k_crv, Fraction(3), 2, 3)
        assert f3 == Fraction(31) * k_crv / Fraction(967680)

    def test_genus_0_is_curvature_self_energy(self):
        """F_0^{crv} = delta^2 / 2 (curvature self-energy at tree level)."""
        for d in range(-5, 6):
            delta = Fraction(d)
            f0 = csn.compute_curved_genus_amplitude(
                Fraction(1), delta, 2, 0
            )
            assert f0 == delta * delta / Fraction(2)

    def test_genus_0_vanishes_for_cy(self):
        """F_0 = 0 when delta = 0."""
        f0 = csn.compute_curved_genus_amplitude(
            Fraction(1), Fraction(0), 2, 0
        )
        assert f0 == 0

    def test_genus_amplitudes_linear_in_kappa_crv(self):
        """F_g is linear in kappa^{crv} for g >= 1."""
        for g in range(1, 4):
            for scale in [Fraction(1), Fraction(2), Fraction(1, 3)]:
                k1 = Fraction(1)
                k2 = scale * k1
                f1 = csn.compute_curved_genus_amplitude(k1, Fraction(0), 0, g)
                f2 = csn.compute_curved_genus_amplitude(k2, Fraction(0), 0, g)
                assert f2 == scale * f1, f"g={g}, scale={scale}: linearity failed"

    def test_genus_amplitude_invalid_genus(self):
        """Negative genus raises ValueError."""
        with pytest.raises(ValueError):
            csn.compute_curved_genus_amplitude(Fraction(1), Fraction(0), 0, -1)


# =========================================================================
# 6. KOSZUL DUALITY: kappa^{crv} invariant under delta -> -delta
# =========================================================================

class TestKoszulDuality:
    """Verify that kappa^{crv} is invariant under Koszul duality (delta -> -delta)."""

    def test_kappa_crv_even_in_delta(self):
        """kappa^{crv}(delta) = kappa^{crv}(-delta)."""
        for kappa in [Fraction(1), Fraction(2), Fraction(5)]:
            for chi in [-2, 0, 2, 4]:
                for d in range(1, 6):
                    k_plus = csn.compute_curved_kappa(kappa, Fraction(d), chi)
                    k_minus = csn.compute_curved_kappa(kappa, Fraction(-d), chi)
                    assert k_plus == k_minus

    def test_curved_koszul_dual_invariance(self):
        """curved_koszul_dual reports kappa invariance."""
        for surf_fn in [csn.tot_O_P1, csn.tot_O_minus1_P1,
                        csn.tot_O_1_P1, csn.tot_O_1_E]:
            surf = surf_fn()
            kd = csn.curved_koszul_dual(surf, Fraction(1))
            assert kd.kappa_invariant, f"{surf.name}: kappa not invariant"

    def test_delta_sign_flip(self):
        """Under Koszul duality: delta -> -delta."""
        surf = csn.tot_O_P1()
        kd = csn.curved_koszul_dual(surf, Fraction(1))
        assert kd.delta_A == -kd.delta_A_dual

    def test_cy_surfaces_are_self_dual(self):
        """CY surfaces have delta = 0, so delta = -delta trivially."""
        surf = csn.tot_O_minus2_P1()
        kd = csn.curved_koszul_dual(surf, Fraction(1))
        assert kd.delta_A == 0
        assert kd.delta_A_dual == 0
        assert kd.kappa_invariant

    def test_genus_1_amplitude_koszul_invariant(self):
        """F_1^{crv} is invariant under delta -> -delta."""
        kappa = Fraction(1)
        chi = 2
        for d in range(1, 6):
            k_plus = csn.compute_curved_kappa(kappa, Fraction(d), chi)
            k_minus = csn.compute_curved_kappa(kappa, Fraction(-d), chi)
            f1_plus = k_plus * csn.A_HAT_COEFFICIENTS[1]
            f1_minus = k_minus * csn.A_HAT_COEFFICIENTS[1]
            assert f1_plus == f1_minus


# =========================================================================
# 7. BASE CURVE DEPENDENCE: chi(C) = 0 (torus) kills correction
# =========================================================================

class TestBaseCurveDependence:
    """Verify the role of chi(C) in the curved correction."""

    def test_torus_no_correction(self):
        """On the torus (g=1, chi=0): kappa^{crv} = kappa for any delta."""
        kappa = Fraction(1)
        for d in range(-10, 11):
            k_crv = csn.compute_curved_kappa(kappa, Fraction(d), 0)
            assert k_crv == kappa, f"delta={d}: torus should have no correction"

    def test_P1_positive_correction(self):
        """On P^1 (chi=2): correction is positive (delta^2 * 2 / 24 > 0)."""
        kappa = Fraction(1)
        for d in range(1, 6):
            k_crv = csn.compute_curved_kappa(kappa, Fraction(d), 2)
            assert k_crv > kappa, f"delta={d}: P^1 correction should be positive"

    def test_genus2_negative_correction(self):
        """On genus-2 curve (chi=-2): correction is negative for delta != 0."""
        kappa = Fraction(1)
        for d in range(1, 6):
            k_crv = csn.compute_curved_kappa(kappa, Fraction(d), -2)
            assert k_crv < kappa, f"delta={d}: genus-2 correction should be negative"

    def test_base_curve_dependence_function(self):
        """base_curve_dependence returns correct data."""
        kappa = Fraction(1)
        delta = Fraction(2)
        result = csn.base_curve_dependence(kappa, delta)
        # g=0: chi=2, correction positive
        assert result[0]["correction"] > 0
        # g=1: chi=0, no correction
        assert result[1]["correction"] == 0
        # g=2: chi=-2, correction negative
        assert result[2]["correction"] < 0

    def test_correction_proportional_to_chi(self):
        """Correction is linear in chi(C)."""
        kappa = Fraction(1)
        delta = Fraction(3)
        c1 = csn.compute_curved_kappa(kappa, delta, 2) - kappa
        c2 = csn.compute_curved_kappa(kappa, delta, 4) - kappa
        assert c2 == 2 * c1  # chi=4 gives twice the correction of chi=2


# =========================================================================
# 8. ARITY STRUCTURE
# =========================================================================

class TestArityStructure:
    """Verify the arity structure of the curved tower."""

    def test_arity_0_equals_delta(self):
        """Arity-0 piece = m_0 = delta."""
        for d in range(-5, 6):
            surf = csn.tot_O_genus_g(0, -2 - d)  # delta = d
            data = csn.curved_data_from_surface(surf, Fraction(1))
            tower = csn.build_curved_shadow_tower(data)
            assert tower.arity_0_curvature == d

    def test_arity_1_on_P1(self):
        """Arity-1 on P^1: Theta_1 = delta * chi(P^1) / 2 = delta."""
        delta = Fraction(3)
        theta_1 = csn.compute_curved_arity_1(delta, 2)
        assert theta_1 == delta * Fraction(2, 2)
        assert theta_1 == delta

    def test_arity_1_on_torus(self):
        """Arity-1 on torus (E): Theta_1 = 0 (chi(E) = 0)."""
        delta = Fraction(5)
        theta_1 = csn.compute_curved_arity_1(delta, 0)
        assert theta_1 == 0

    def test_arity_1_on_genus2(self):
        """Arity-1 on genus-2 curve: Theta_1 = delta * (-2) / 2 = -delta."""
        delta = Fraction(3)
        theta_1 = csn.compute_curved_arity_1(delta, -2)
        assert theta_1 == -delta

    def test_arity_2_equals_kappa_crv(self):
        """Arity-2 piece = kappa^{crv}."""
        surf = csn.tot_O_P1()
        data = csn.curved_data_from_surface(surf, Fraction(1))
        tower = csn.build_curved_shadow_tower(data)
        assert tower.tower[2] == tower.kappa_curved

    def test_arity_shift_nonzero_for_curved(self):
        """The arity shift is -2 for curved algebras."""
        surf = csn.tot_O_P1()
        data = csn.curved_data_from_surface(surf, Fraction(1))
        bc = csn.build_curved_bar(data)
        assert bc.arity_shift() == -2

    def test_arity_shift_zero_for_cy(self):
        """The arity shift is 0 for CY algebras."""
        surf = csn.tot_O_minus2_P1()
        data = csn.curved_data_from_surface(surf, Fraction(1))
        bc = csn.build_curved_bar(data)
        assert bc.arity_shift() == 0


# =========================================================================
# 9. INHOMOGENEOUS MC EQUATION
# =========================================================================

class TestInhomogeneousMC:
    """Verify the integrability of the inhomogeneous MC equation."""

    def test_imc_all_consistent_P1(self):
        """iMC is consistent at all arities for Tot(O -> P^1)."""
        result = csn.imc_integrability_check(
            Fraction(-2), Fraction(1), 2
        )
        assert result["all_consistent"]

    def test_imc_all_consistent_E(self):
        """iMC is consistent for E-based surfaces."""
        result = csn.imc_integrability_check(
            Fraction(-1), Fraction(1), 0
        )
        assert result["all_consistent"]

    def test_imc_source_is_central(self):
        """m_0 is central in the deformation complex."""
        result = csn.imc_integrability_check(
            Fraction(3), Fraction(2), 2
        )
        assert result["m_0_central"]

    def test_imc_source_is_closed(self):
        """D * m_0 = 0 (the source is closed)."""
        result = csn.imc_integrability_check(
            Fraction(3), Fraction(2), 2
        )
        assert result["source_closed"]

    def test_imc_residual_vanishes(self):
        """MC residual vanishes at every arity."""
        for d in range(-3, 4):
            result = csn.imc_integrability_check(
                Fraction(d), Fraction(1), 2, max_arity=6
            )
            for r in range(7):
                assert result["residuals"][r] == 0, f"delta={d}, arity={r}"

    def test_imc_homogeneous_at_cy(self):
        """At delta = 0, the iMC reduces to the standard MC equation."""
        result = csn.imc_integrability_check(
            Fraction(0), Fraction(1), 2
        )
        assert result["all_consistent"]
        assert result["arity_0"]["Theta_0"] == 0


# =========================================================================
# 10. CODERIVED CATEGORY
# =========================================================================

class TestCoderivedCategory:
    """Verify coderived category properties."""

    def test_coderived_trivial_for_cy(self):
        """D^co = D^b for uncurved (CY) algebras."""
        surf = csn.tot_O_minus2_P1()
        data = csn.curved_data_from_surface(surf, Fraction(1))
        info = csn.coderived_info(data)
        assert info.is_trivial

    def test_coderived_nontrivial_for_non_cy(self):
        """D^co strictly larger than D^b for curved algebras."""
        surf = csn.tot_O_P1()
        data = csn.curved_data_from_surface(surf, Fraction(1))
        info = csn.coderived_info(data)
        assert not info.is_trivial

    def test_coderived_curvature_matches(self):
        """Coderived info reports correct curvature."""
        surf = csn.tot_O_P1()
        data = csn.curved_data_from_surface(surf, Fraction(1))
        info = csn.coderived_info(data)
        assert info.curvature == Fraction(-2)

    def test_bar_cobar_extends(self):
        """Bar-cobar adjunction extends to D^co."""
        surf = csn.tot_O_P1()
        data = csn.curved_data_from_surface(surf, Fraction(1))
        info = csn.coderived_info(data)
        assert "extends" in info.bar_cobar_status or "Positselski" in info.bar_cobar_status


# =========================================================================
# 11. PARTITION FUNCTION
# =========================================================================

class TestPartitionFunction:
    """Verify the curved shadow partition function."""

    def test_tree_level_F0(self):
        """F_0^{crv} = delta^2 / 2 (tree-level curvature self-energy)."""
        for d in range(-5, 6):
            delta = Fraction(d)
            kappa_crv = csn.compute_curved_kappa(Fraction(1), delta, 2)
            pf = csn.curved_shadow_partition_function(kappa_crv, delta)
            assert pf["F_0"] == delta * delta / Fraction(2)

    def test_tree_level_vanishes_for_cy(self):
        """F_0 = 0 for CY (delta = 0)."""
        pf = csn.curved_shadow_partition_function(Fraction(1), Fraction(0))
        assert pf["F_0"] == 0
        assert not pf["has_tree_level"]

    def test_tree_level_exists_for_non_cy(self):
        """F_0 != 0 for non-CY (delta != 0)."""
        pf = csn.curved_shadow_partition_function(Fraction(1), Fraction(2))
        assert pf["F_0"] != 0
        assert pf["has_tree_level"]

    def test_higher_genus_present(self):
        """Higher genus amplitudes are present in the PF."""
        kappa_crv = Fraction(4, 3)
        delta = Fraction(-2)
        pf = csn.curved_shadow_partition_function(kappa_crv, delta)
        for g in range(1, 6):
            assert f"F_{g}" in pf
            assert pf[f"F_{g}"] == kappa_crv * csn.A_HAT_COEFFICIENTS[g]


# =========================================================================
# 12. SHADOW METRIC AND DEPTH CLASS
# =========================================================================

class TestShadowMetricAndDepth:
    """Verify shadow metric and depth classification for curved algebras."""

    def test_shadow_metric_at_origin(self):
        """Q_L^{crv}(0) = (2 * kappa^{crv})^2."""
        kappa_crv = Fraction(4, 3)
        q = csn.curved_shadow_metric(kappa_crv, t=Fraction(0))
        assert q == (2 * kappa_crv) ** 2

    def test_shadow_metric_positive_definite(self):
        """Q_L^{crv}(t) > 0 for t near 0 (when kappa^{crv} > 0)."""
        kappa_crv = Fraction(4, 3)
        for t_val in [Fraction(0), Fraction(1, 10), Fraction(-1, 10)]:
            q = csn.curved_shadow_metric(kappa_crv, t=t_val)
            assert q > 0

    def test_shadow_connection_residue(self):
        """Shadow connection residue = 1/2 (universal, curvature-independent)."""
        kappa_crv = Fraction(4, 3)
        res = csn.curved_shadow_connection_residue(kappa_crv)
        assert res == Fraction(1, 2)

    def test_depth_class_G(self):
        """Gaussian class (alpha=0, S4=0)."""
        cls = csn.curved_shadow_depth_class(Fraction(2), Fraction(1))
        assert cls == "G"

    def test_depth_class_L(self):
        """Lie class (alpha!=0, S4=0)."""
        cls = csn.curved_shadow_depth_class(
            Fraction(2), Fraction(1),
            alpha_crv=Fraction(1), S4_crv=Fraction(0)
        )
        assert cls == "L"

    def test_depth_class_M(self):
        """Mixed class (Delta != 0)."""
        cls = csn.curved_shadow_depth_class(
            Fraction(2), Fraction(1),
            alpha_crv=Fraction(1), S4_crv=Fraction(1)
        )
        assert cls == "M"


# =========================================================================
# 13. LANDSCAPE: all standard examples
# =========================================================================

class TestLandscape:
    """Verify all standard examples in the landscape."""

    def test_landscape_builds(self):
        """The full landscape builds without errors."""
        landscape = csn.standard_landscape()
        assert len(landscape) > 0

    def test_landscape_contains_cy(self):
        """Landscape includes CY examples."""
        landscape = csn.standard_landscape()
        cy_count = sum(1 for t in landscape.values() if t.delta == 0)
        assert cy_count > 0

    def test_landscape_contains_non_cy(self):
        """Landscape includes non-CY examples."""
        landscape = csn.standard_landscape()
        non_cy_count = sum(1 for t in landscape.values() if t.delta != 0)
        assert non_cy_count > 0

    def test_landscape_summary(self):
        """Summary table is nonempty."""
        summary = csn.landscape_summary()
        assert len(summary) > 0

    def test_all_cy_in_landscape_have_zero_delta(self):
        """Every CY example in the landscape has delta = 0."""
        landscape = csn.standard_landscape()
        for name, tower in landscape.items():
            if tower.data.is_uncurved:
                assert tower.delta == 0, f"{name}: CY but delta != 0"

    def test_all_non_cy_have_nonzero_m0(self):
        """Every non-CY example has m_0 != 0."""
        landscape = csn.standard_landscape()
        for name, tower in landscape.items():
            if not tower.data.is_uncurved:
                assert tower.arity_0_curvature != 0


# =========================================================================
# 14. CROSS-CHECKS: multiple derivations agree
# =========================================================================

class TestCrossChecks:
    """Cross-check computations via independent paths."""

    def test_kappa_crv_two_paths(self):
        """Compute kappa^{crv} via tower and via direct formula."""
        kappa = Fraction(1)
        surf = csn.tot_O_P1()
        # Path 1: via tower
        data = csn.curved_data_from_surface(surf, kappa)
        tower = csn.build_curved_shadow_tower(data)
        kappa_tower = tower.kappa_curved
        # Path 2: direct formula
        kappa_direct = csn.compute_curved_kappa(kappa, Fraction(surf.delta), surf.euler_char_base)
        assert kappa_tower == kappa_direct

    def test_F1_two_paths(self):
        """Compute F_1 via tower and via kappa^{crv}/24."""
        kappa = Fraction(1)
        surf = csn.tot_O_P1()
        data = csn.curved_data_from_surface(surf, kappa)
        tower = csn.build_curved_shadow_tower(data)
        # Path 1: from tower
        f1_tower = tower.genus_amplitudes[1]
        # Path 2: direct
        f1_direct = tower.kappa_curved / Fraction(24)
        assert f1_tower == f1_direct

    def test_comparison_matches_tower(self):
        """CurvedUncurvedComparison matches the tower computation."""
        kappa = Fraction(1)
        surf = csn.tot_O_P1()
        comp = csn.compare_curved_uncurved(surf, kappa)
        data = csn.curved_data_from_surface(surf, kappa)
        tower = csn.build_curved_shadow_tower(data)
        assert comp.kappa_curved == tower.kappa_curved
        assert comp.genus_1_curved == tower.genus_amplitudes[1]

    def test_obstruction_class_matches_tower(self):
        """Obstruction classes match tower values."""
        kappa = Fraction(1)
        delta = Fraction(-2)
        chi = 2
        o0 = csn.curved_obstruction_class(0, delta, kappa, chi)
        o1 = csn.curved_obstruction_class(1, delta, kappa, chi)
        o2 = csn.curved_obstruction_class(2, delta, kappa, chi)
        assert o0 == delta
        assert o1 == csn.compute_curved_arity_1(delta, chi)
        assert o2 == csn.compute_curved_kappa(kappa, delta, chi)

    def test_delta_family_matches_individual(self):
        """delta_family_kappas matches individual computations."""
        kappa = Fraction(1)
        chi = 2
        family = csn.delta_family_kappas(kappa, chi, range(-3, 4))
        for d in range(-3, 4):
            individual = csn.compute_curved_kappa(kappa, Fraction(d), chi)
            assert family[d] == individual, f"d={d}: family vs individual mismatch"

    def test_delta_family_genus_1_matches(self):
        """delta_family_genus_1 matches individual F_1 computations."""
        kappa = Fraction(1)
        chi = 2
        family = csn.delta_family_genus_1(kappa, chi, range(-3, 4))
        for d in range(-3, 4):
            k_crv = csn.compute_curved_kappa(kappa, Fraction(d), chi)
            f1_individual = k_crv * csn.A_HAT_COEFFICIENTS[1]
            assert family[d] == f1_individual

    def test_P1_family_symmetry(self):
        """O(d) and O(-4-d) on P^1 give the same kappa^{crv} (symmetry around d=-2)."""
        kappa = Fraction(1)
        # delta(d) = -2 - d.  delta(-4-d) = -2 - (-4-d) = 2 + d.
        # These have |delta| equal iff d and -4-d have delta^2 equal.
        # delta(d)^2 = (2+d)^2, delta(-4-d)^2 = (2+d)^2.  YES!
        for d in range(-6, 3):
            t1 = csn.compute_general_P1(d, kappa)
            t2 = csn.compute_general_P1(-4 - d, kappa)
            assert t1.kappa_curved == t2.kappa_curved, \
                f"d={d} vs d={-4-d}: kappa^crv should be equal by symmetry"


# =========================================================================
# 15. EXPLICIT COMPUTATIONS FOR NAMED EXAMPLES
# =========================================================================

class TestExplicitExamples:
    """Verify explicit computations for named examples."""

    def test_tot_O_P1_kappa_crv(self):
        """Tot(O -> P^1): kappa^{crv} = 1 + 4/12 = 4/3."""
        tower = csn.compute_tot_O_P1()
        assert tower.kappa_curved == Fraction(4, 3)

    def test_tot_O_minus2_P1_is_cy(self):
        """T*P^1 is CY: kappa^{crv} = kappa = 1."""
        tower = csn.compute_tot_O_minus2_P1()
        assert tower.kappa_curved == Fraction(1)
        assert tower.delta == 0

    def test_tot_O_minus1_P1_kappa_crv(self):
        """Tot(O(-1) -> P^1): kappa^{crv} = 1 + 1/12 = 13/12."""
        tower = csn.compute_tot_O_minus1_P1()
        assert tower.kappa_curved == Fraction(13, 12)

    def test_tot_O_1_P1_kappa_crv(self):
        """Tot(O(1) -> P^1): kappa^{crv} = 1 + 9/12 = 7/4."""
        tower = csn.compute_tot_O_1_P1()
        assert tower.kappa_curved == Fraction(7, 4)

    def test_tot_O_E_is_cy(self):
        """Tot(O -> E) is CY: kappa^{crv} = kappa = 1."""
        tower = csn.compute_tot_O_E()
        assert tower.kappa_curved == Fraction(1)
        assert tower.delta == 0

    def test_tot_O_1_E_kappa_crv(self):
        """Tot(O(1) -> E): delta = -1, chi(E) = 0, so kappa^{crv} = kappa = 1."""
        tower = csn.compute_tot_O_1_E()
        assert tower.kappa_curved == Fraction(1)
        # Note: delta != 0 but correction = 0 because chi(E) = 0
        assert tower.delta == Fraction(-1)

    def test_tot_O_P1_genus_0(self):
        """Tot(O -> P^1): F_0 = delta^2/2 = 4/2 = 2."""
        tower = csn.compute_tot_O_P1()
        assert tower.genus_amplitudes[0] == Fraction(2)

    def test_tot_O_P1_genus_1(self):
        """Tot(O -> P^1): F_1 = kappa^{crv}/24 = (4/3)/24 = 1/18."""
        tower = csn.compute_tot_O_P1()
        assert tower.genus_amplitudes[1] == Fraction(4, 3) / Fraction(24)
        assert tower.genus_amplitudes[1] == Fraction(1, 18)

    def test_tot_O_P1_arity_1(self):
        """Tot(O -> P^1): Theta_1 = delta * chi/2 = (-2)*1 = -2."""
        tower = csn.compute_tot_O_P1()
        assert tower.arity_1_correction == Fraction(-2)


# =========================================================================
# 16. CURVED BAR COMPLEX PROPERTIES
# =========================================================================

class TestCurvedBarComplex:
    """Verify properties of the curved bar complex."""

    def test_d_squared_equals_m0(self):
        """d_B^2 = m_0 for all arities."""
        surf = csn.tot_O_P1()
        data = csn.curved_data_from_surface(surf, Fraction(1))
        bc = csn.build_curved_bar(data)
        for n in range(1, 6):
            assert bc.d_squared_on_arity_n(n) == Fraction(-2)

    def test_d_squared_zero_for_cy(self):
        """d_B^2 = 0 for CY algebras."""
        surf = csn.tot_O_minus2_P1()
        data = csn.curved_data_from_surface(surf, Fraction(1))
        bc = csn.build_curved_bar(data)
        assert bc.curvature_defect == 0
        assert bc.is_dg

    def test_not_dg_for_curved(self):
        """B(A) is NOT a dg coalgebra when curved."""
        surf = csn.tot_O_P1()
        data = csn.curved_data_from_surface(surf, Fraction(1))
        bc = csn.build_curved_bar(data)
        assert not bc.is_dg

    def test_curvature_defect(self):
        """Curvature defect equals m_0."""
        for d in range(-3, 4):
            surf = csn.tot_O_genus_g(0, -2 - d)  # delta = d
            data = csn.curved_data_from_surface(surf, Fraction(1))
            bc = csn.build_curved_bar(data)
            assert bc.curvature_defect == d


# =========================================================================
# 17. MF CONNECTION
# =========================================================================

class TestMFConnection:
    """Verify the matrix factorization connection."""

    def test_mf_curvature_degree(self):
        """MF curvature = superpotential degree."""
        assert csn.mf_curvature(5) == 5
        assert csn.mf_curvature(3) == 3

    def test_mf_curvature_zero(self):
        """W = 0 gives zero curvature."""
        assert csn.mf_curvature(0) == 0


# =========================================================================
# 18. ADDITIONAL VERIFICATION: A-HAT COEFFICIENTS
# =========================================================================

class TestAHatCoefficients:
    """Verify the A-hat coefficients match the Vol I values."""

    def test_a_hat_1(self):
        """a_hat_1 = 1/24."""
        assert csn.A_HAT_COEFFICIENTS[1] == Fraction(1, 24)

    def test_a_hat_2(self):
        """a_hat_2 = 7/5760."""
        assert csn.A_HAT_COEFFICIENTS[2] == Fraction(7, 5760)

    def test_a_hat_3(self):
        """a_hat_3 = 31/967680."""
        assert csn.A_HAT_COEFFICIENTS[3] == Fraction(31, 967680)

    def test_a_hat_4(self):
        """a_hat_4 = 127/154828800."""
        assert csn.A_HAT_COEFFICIENTS[4] == Fraction(127, 154828800)

    def test_a_hat_5(self):
        """a_hat_5 = 73/3503554560."""
        assert csn.A_HAT_COEFFICIENTS[5] == Fraction(73, 3503554560)

    def test_a_hat_all_positive(self):
        """All A-hat coefficients are positive (Bernoulli signs after i-rotation)."""
        for g, a in csn.A_HAT_COEFFICIENTS.items():
            assert a > 0, f"a_hat_{g} = {a} is not positive"


# =========================================================================
# 19. EDGE CASES
# =========================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_large_delta(self):
        """kappa^{crv} with large delta."""
        kappa = Fraction(1)
        delta = Fraction(100)
        k_crv = csn.compute_curved_kappa(kappa, delta, 2)
        assert k_crv == Fraction(1) + Fraction(10000 * 2, 24)
        assert k_crv > 0

    def test_negative_kappa_cy(self):
        """Negative kappa_cy (e.g., quintic: kappa = -25/3)."""
        kappa = Fraction(-25, 3)
        delta = Fraction(0)
        k_crv = csn.compute_curved_kappa(kappa, delta, 2)
        assert k_crv == kappa  # CY: no correction

    def test_negative_kappa_with_delta(self):
        """Curvature correction can make kappa^{crv} positive even for negative kappa."""
        kappa = Fraction(-1)
        delta = Fraction(10)
        k_crv = csn.compute_curved_kappa(kappa, delta, 2)
        # correction = 100 * 2 / 24 = 25/3 > 1, so kappa^{crv} > 0
        assert k_crv > 0

    def test_zero_kappa_cy(self):
        """kappa_cy = 0: the entire kappa^{crv} comes from curvature."""
        kappa = Fraction(0)
        delta = Fraction(3)
        k_crv = csn.compute_curved_kappa(kappa, delta, 2)
        assert k_crv == Fraction(9 * 2, 24)
        assert k_crv == Fraction(3, 4)

    def test_format_tower(self):
        """format_tower produces a nonempty string."""
        tower = csn.compute_tot_O_P1()
        s = csn.format_tower(tower)
        assert len(s) > 0
        assert "delta" in s.lower() or "CY defect" in s

    def test_inhomogeneous_mc_data(self):
        """InhomogeneousMCData computes correctly."""
        surf = csn.tot_O_P1()
        data = csn.curved_data_from_surface(surf, Fraction(1))
        bc = csn.build_curved_bar(data)
        mc = csn.InhomogeneousMCData(
            bar_complex=bc,
            source_term=data.curvature,
            theta_uncurved={2: Fraction(1)},
            theta_corrections={2: Fraction(1, 3)},
        )
        assert not mc.is_homogeneous
        assert mc.total_theta_at_arity(2) == Fraction(4, 3)

    def test_inhomogeneous_mc_homogeneous_case(self):
        """At CY: mc.is_homogeneous = True."""
        surf = csn.tot_O_minus2_P1()
        data = csn.curved_data_from_surface(surf, Fraction(1))
        bc = csn.build_curved_bar(data)
        mc = csn.InhomogeneousMCData(
            bar_complex=bc,
            source_term=data.curvature,
            theta_uncurved={2: Fraction(1)},
            theta_corrections={},
        )
        assert mc.is_homogeneous


# =========================================================================
# 20. PARAMETRIC SWEEP: CONSISTENCY ACROSS FAMILIES
# =========================================================================

class TestParametricSweep:
    """Sweep across parameter ranges for systematic consistency."""

    def test_P1_degree_sweep(self):
        """Sweep O(d) -> P^1 for d = -10, ..., 10: all towers build."""
        kappa = Fraction(1)
        for d in range(-10, 11):
            tower = csn.compute_general_P1(d, kappa)
            assert tower.kappa_curved is not None
            # kappa^{crv} = 1 + (2+d)^2 / 12
            expected = Fraction(1) + Fraction((2 + d)**2, 12)
            assert tower.kappa_curved == expected, f"d={d}"

    def test_genus_sweep(self):
        """Sweep genus 0, ..., 10 at fixed delta=2: chi dependence correct."""
        kappa = Fraction(1)
        delta = Fraction(2)
        for g in range(0, 11):
            chi = 2 - 2 * g
            k_crv = csn.compute_curved_kappa(kappa, delta, chi)
            expected = kappa + Fraction(4 * chi, 24)
            assert k_crv == expected, f"g={g}: got {k_crv}, expected {expected}"

    def test_kappa_sweep(self):
        """Sweep kappa_cy = 1, 2, ..., 10 at fixed delta and chi."""
        delta = Fraction(3)
        chi = 2
        for k in range(1, 11):
            kappa = Fraction(k)
            k_crv = csn.compute_curved_kappa(kappa, delta, chi)
            expected = Fraction(k) + Fraction(9 * 2, 24)
            assert k_crv == expected, f"kappa={k}: linearity check"

    def test_additivity_of_correction(self):
        """The correction delta^2 * chi / 24 is additive in chi."""
        kappa = Fraction(1)
        delta = Fraction(2)
        k1 = csn.compute_curved_kappa(kappa, delta, 2)
        k2 = csn.compute_curved_kappa(kappa, delta, 4)
        k3 = csn.compute_curved_kappa(kappa, delta, 6)
        # Corrections: 4*2/24 = 1/3, 4*4/24 = 2/3, 4*6/24 = 1
        c1 = k1 - kappa
        c2 = k2 - kappa
        c3 = k3 - kappa
        assert c2 == 2 * c1
        assert c3 == 3 * c1

    def test_quadratic_in_delta_universal(self):
        """kappa^{crv} - kappa is quadratic in delta for all base curves."""
        kappa = Fraction(1)
        for chi in [-4, -2, 0, 2, 4]:
            corrections = {}
            for d in range(0, 6):
                k_crv = csn.compute_curved_kappa(kappa, Fraction(d), chi)
                corrections[d] = k_crv - kappa
            # Check c(d) = d^2 * chi / 24
            for d in range(0, 6):
                expected = Fraction(d * d * chi, 24)
                assert corrections[d] == expected, \
                    f"chi={chi}, d={d}: correction {corrections[d]} != {expected}"
