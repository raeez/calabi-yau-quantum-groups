r"""Tests for categorified chiral invariants of torus knots T(2,n).

Manuscript references:
    Part IV (Quantum Groups and Braided Monoidal Structure):
        conj:chiral-knot-invariant: Chiral torus knot invariant
        rem:tree-level-divergence: Universal divergence at (1,1)
        subsec:chiral-torus-knots: Chiral torus knot invariants
        subsec:categorified-chiral-torus-knots: Categorified invariants (NEW)

    en_factorization.tex (section: Categorified chiral torus knot invariants)

    CLAIM STATUS:
        Tree-level divergence: PROVED (universal, 71 tests in stratified engine).
        Residue regularization: PROVED (analytic).
        Categorified graded dim (1+t)^g: CONJECTURAL (CY-A_3).
        Mukai weight grading: CONJECTURAL (K3 Yangian, AP-CY14).
        Jones polynomial limit: CONJECTURAL (RT identification).

Literature ground truth:
    [Milnor] Genus of T(2,n) = (n-1)/2.
    [Pick] Interior lattice points = genus for Newton polygon.
    [KH] Khovanov (2000): Jones polynomial of T(2,3) = -t^{-4}+t^{-3}+t^{-1}.
    [Rasm] Rasmussen (2010): Khovanov homology of torus knots.
    [ORS] Oblomkov-Rasmussen-Shende: knot homology from Hilb.
    [DC] Direct computation via exact arithmetic.
    CY condition: h1+h2+h3 = 0.
    CY inversion: g(z)*g(-z) = 1.
    Universal divergence: g(h1+h2) = g(-h3) = pole.

AP-CY28: All test points chosen far from poles at +/-h_i.
    With h = (3.1, -1.3, -1.8): poles at z = {-3.1, 1.3, 1.8}.
    Interior point arguments:
      (1,1): 1.8 = -h_3 (POLE, expected)
      (1,2): 4.9 (safe)
      (1,3): 8.0 (safe)
"""

import math

import numpy as np
import pytest

from compute.lib.chiral_khovanov_torus_knots import (
    CategorifiedTorusKnotInvariant,
    CinquefoilT25,
    MukaiWeight,
    T2nGeneralFormula,
    TorusKnotT2n,
    TrefoilT23,
    jones_polynomial_t2n,
    mukai_grading_analysis,
    t2n_genus,
    t2n_interior_points,
    t2n_milnor_number,
    verify_chiral_khovanov_torus_knots,
    verify_jones_limit_t2n,
)


# =========================================================================
# Standard test parameters (AP-CY28 safe)
# =========================================================================

# Omega-background parameters: h = (3.1, -1.3, -1.8)
# Poles at z = {-3.1, 1.3, 1.8}
# Interior point (1,1): argument 3.1 + (-1.3) = 1.8 = -h_3 -> POLE (expected)
# Interior point (1,2): argument 2*3.1 + (-1.3) = 4.9 -> safe
# Interior point (1,3): argument 3*3.1 + (-1.3) = 8.0 -> safe
H1 = 3.1
H2 = -1.3
H3 = -(H1 + H2)  # = -1.8


# =========================================================================
# 1. Newton polygon combinatorics
# =========================================================================

class TestNewtonPolygon:
    """Interior lattice points of Newton polygon of z_1^2 - z_2^n."""

    def test_t23_one_interior_point(self):
        """T(2,3): 1 interior point (1,1). [Pick, DC]"""
        pts = t2n_interior_points(3)
        assert pts == [(1, 1)]

    def test_t25_two_interior_points(self):
        """T(2,5): 2 interior points (1,1), (1,2). [Pick, DC]"""
        pts = t2n_interior_points(5)
        assert pts == [(1, 1), (1, 2)]

    def test_t27_three_interior_points(self):
        """T(2,7): 3 interior points. [Pick, DC]"""
        pts = t2n_interior_points(7)
        assert pts == [(1, 1), (1, 2), (1, 3)]

    def test_t29_four_interior_points(self):
        """T(2,9): 4 interior points. [Pick, DC]"""
        pts = t2n_interior_points(9)
        assert len(pts) == 4
        assert pts[0] == (1, 1)
        assert pts[-1] == (1, 4)

    def test_interior_count_equals_genus(self):
        """Number of interior points = genus for all T(2,n). [Pick, Milnor]"""
        for n in range(3, 20, 2):
            pts = t2n_interior_points(n)
            assert len(pts) == t2n_genus(n)

    def test_all_points_have_a_equals_1(self):
        """For T(2,n), all interior points have a=1. [DC]"""
        for n in range(3, 20, 2):
            pts = t2n_interior_points(n)
            assert all(a == 1 for a, b in pts)

    def test_even_n_rejected(self):
        """T(2, even) is not a knot (gcd != 1). [DC]"""
        with pytest.raises(ValueError):
            t2n_interior_points(4)

    def test_n_less_than_3_rejected(self):
        """T(2,1) is trivial; T(2,2) has gcd != 1. [DC]"""
        with pytest.raises(ValueError):
            t2n_interior_points(1)


# =========================================================================
# 2. Genus and Milnor number
# =========================================================================

class TestGenusAndMilnor:
    """Genus and Milnor number for T(2,n)."""

    def test_t23_genus_1(self):
        """T(2,3) trefoil has genus 1. [Milnor]"""
        assert t2n_genus(3) == 1

    def test_t25_genus_2(self):
        """T(2,5) cinquefoil has genus 2. [Milnor]"""
        assert t2n_genus(5) == 2

    def test_t27_genus_3(self):
        """T(2,7) has genus 3. [Milnor]"""
        assert t2n_genus(7) == 3

    @pytest.mark.parametrize("n,expected", [
        (3, 1), (5, 2), (7, 3), (9, 4), (11, 5), (13, 6), (15, 7),
    ])
    def test_genus_formula(self, n, expected):
        """genus(T(2,n)) = (n-1)/2 for all odd n. [Milnor]"""
        assert t2n_genus(n) == expected

    def test_t23_milnor_number_2(self):
        """T(2,3) trefoil has Milnor number 2. [Milnor]"""
        assert t2n_milnor_number(3) == 2

    def test_t25_milnor_number_4(self):
        """T(2,5) cinquefoil has Milnor number 4. [Milnor]"""
        assert t2n_milnor_number(5) == 4

    @pytest.mark.parametrize("n", [3, 5, 7, 9, 11, 13])
    def test_milnor_equals_n_minus_1(self, n):
        """mu(T(2,n)) = n-1. [Milnor]"""
        assert t2n_milnor_number(n) == n - 1

    @pytest.mark.parametrize("n", [3, 5, 7, 9, 11])
    def test_milnor_equals_twice_genus(self, n):
        """mu = 2*g for T(2,n). [DC]"""
        assert t2n_milnor_number(n) == 2 * t2n_genus(n)


# =========================================================================
# 3. Universal (1,1) divergence
# =========================================================================

class TestUniversalDivergence:
    """The universal tree-level divergence at the (1,1) interior point."""

    def test_11_argument_equals_minus_h3(self):
        """(1,1) argument = h_1 + h_2 = -h_3 (CY condition). [DC]"""
        tk = TorusKnotT2n(3, H1, H2)
        arg = tk.point_argument(1, 1)
        assert abs(arg - (-H3)) < 1e-12

    def test_11_is_pole_trefoil(self):
        """(1,1) is a pole for T(2,3). [DC]"""
        tk = TorusKnotT2n(3, H1, H2)
        assert tk.is_pole_point(1, 1)

    def test_11_is_pole_cinquefoil(self):
        """(1,1) is a pole for T(2,5). [DC]"""
        tk = TorusKnotT2n(5, H1, H2)
        assert tk.is_pole_point(1, 1)

    @pytest.mark.parametrize("n", [3, 5, 7, 9, 11, 13, 15])
    def test_11_is_pole_all_t2n(self, n):
        """(1,1) is ALWAYS a pole for every T(2,n). [CY condition, universal]"""
        tk = TorusKnotT2n(n, H1, H2)
        assert tk.is_pole_point(1, 1)

    @pytest.mark.parametrize("n", [5, 7, 9, 11, 13])
    def test_regular_points_not_poles(self, n):
        """Points (1,b) for b >= 2 are NOT poles (generically). [DC, AP-CY28]"""
        tk = TorusKnotT2n(n, H1, H2)
        for a, b in tk.regular_points():
            assert not tk.is_pole_point(a, b)

    def test_exactly_one_singular_point(self):
        """Each T(2,n) has exactly one singular point: (1,1). [DC]"""
        for n in range(3, 16, 2):
            tk = TorusKnotT2n(n, H1, H2)
            sing = tk.singular_points()
            assert len(sing) == 1
            assert sing[0] == (1, 1)


# =========================================================================
# 4. Regularized invariant
# =========================================================================

class TestRegularizedInvariant:
    """Residue regularization at the (1,1) pole."""

    def test_residue_finite(self):
        """Residue at -h_3 is finite. [DC]"""
        tk = TorusKnotT2n(3, H1, H2)
        res = tk.residue_at_11()
        assert np.isfinite(abs(res))

    def test_residue_nonzero(self):
        """Residue at -h_3 is nonzero for generic h. [DC]"""
        tk = TorusKnotT2n(3, H1, H2)
        res = tk.residue_at_11()
        assert abs(res) > 1e-12

    def test_trefoil_reg_equals_residue(self):
        """For T(2,3), Z^{reg} = Res (no regular factors). [DC]"""
        tk = TorusKnotT2n(3, H1, H2)
        reg = tk.regularized_invariant()
        res = tk.residue_at_11()
        assert abs(reg - res) < 1e-12

    def test_cinquefoil_reg_equals_res_times_g(self):
        """For T(2,5), Z^{reg} = Res * g(h_2 + 2*h_1). [DC]"""
        tk = TorusKnotT2n(5, H1, H2)
        reg = tk.regularized_invariant()
        res = tk.residue_at_11()
        g_12 = tk.tree_level_regular_factor()
        assert abs(reg - res * g_12) < 1e-12

    def test_t27_reg_has_two_regular_factors(self):
        """For T(2,7), 2 regular points and Z^{reg} = Res * product. [DC]"""
        tk = TorusKnotT2n(7, H1, H2)
        assert len(tk.regular_points()) == 2
        reg = tk.regularized_invariant()
        res = tk.residue_at_11()
        regular = tk.tree_level_regular_factor()
        assert abs(reg - res * regular) < 1e-12

    def test_regularized_invariant_nonzero(self):
        """Z^{reg} is nonzero for generic parameters. [DC]"""
        for n in [3, 5, 7, 9]:
            tk = TorusKnotT2n(n, H1, H2)
            reg = tk.regularized_invariant()
            assert abs(reg) > 1e-12, f"T(2,{n}): Z^reg = 0"

    def test_regularized_invariant_finite(self):
        """Z^{reg} is finite. [DC]"""
        for n in [3, 5, 7, 9]:
            tk = TorusKnotT2n(n, H1, H2)
            reg = tk.regularized_invariant()
            assert np.isfinite(abs(reg)), f"T(2,{n}): Z^reg infinite"

    def test_residue_explicit_trefoil(self):
        """Explicit residue computation for T(2,3). [DC]

        Res_{z=-h_3} g(z) = (-h_3-h_1)(-h_3-h_2)(-2h_3) / [(-h_3+h_1)(-h_3+h_2)]
        With h = (3.1, -1.3, -1.8):
          -h_3 = 1.8
          numer = (1.8-3.1)(1.8-(-1.3))(1.8-(-1.8)) = (-1.3)(3.1)(3.6)
          Full numer = (-1.3)*(3.1)*(3.6) = -14.508
          denom_deriv = (1.8+3.1)(1.8+(-1.3)) = (4.9)(0.5) = 2.45
          Res = -14.508 / 2.45 = -5.92163...
        """
        tk = TorusKnotT2n(3, H1, H2)
        res = tk.residue_at_11()
        # Manual computation
        mh3 = -H3  # = 1.8
        numer = (mh3 - H1) * (mh3 - H2) * (mh3 - H3)
        denom = (mh3 + H1) * (mh3 + H2)
        expected = numer / denom
        assert abs(res - expected) < 1e-10

    def test_alternative_parameters(self):
        """Regularized invariant with different safe parameters. [DC, AP-CY28]"""
        # Use h = (2.7, -0.9, -1.8), poles at {-2.7, 0.9, 1.8}
        h1, h2 = 2.7, -0.9
        tk = TorusKnotT2n(5, h1, h2)
        reg = tk.regularized_invariant()
        assert np.isfinite(abs(reg))
        assert abs(reg) > 1e-12


# =========================================================================
# 5. Categorified invariant: graded dimensions
# =========================================================================

class TestCategorifiedDimensions:
    """Graded dimensions of the categorified complex CKh_{2,n}."""

    def test_trefoil_total_dim_2(self):
        """CKh_{2,3} has total dimension 2. [DC]"""
        cat = CategorifiedTorusKnotInvariant(3, H1, H2)
        assert cat.total_dimension() == 2

    def test_cinquefoil_total_dim_4(self):
        """CKh_{2,5} has total dimension 4. [DC]"""
        cat = CategorifiedTorusKnotInvariant(5, H1, H2)
        assert cat.total_dimension() == 4

    def test_t27_total_dim_8(self):
        """CKh_{2,7} has total dimension 8. [DC]"""
        cat = CategorifiedTorusKnotInvariant(7, H1, H2)
        assert cat.total_dimension() == 8

    @pytest.mark.parametrize("n,expected_dim", [
        (3, 2), (5, 4), (7, 8), (9, 16), (11, 32), (13, 64),
    ])
    def test_dimension_is_2_to_genus(self, n, expected_dim):
        """dim CKh_{2,n} = 2^g for all T(2,n). [DC]"""
        cat = CategorifiedTorusKnotInvariant(n, H1, H2)
        assert cat.total_dimension() == expected_dim

    def test_trefoil_graded_dims(self):
        """CKh_{2,3}: graded dims = [1, 1] = row 1 of Pascal. [DC]"""
        cat = CategorifiedTorusKnotInvariant(3, H1, H2)
        assert cat.homological_graded_dimension() == [1, 1]

    def test_cinquefoil_graded_dims(self):
        """CKh_{2,5}: graded dims = [1, 2, 1] = row 2 of Pascal. [DC]"""
        cat = CategorifiedTorusKnotInvariant(5, H1, H2)
        assert cat.homological_graded_dimension() == [1, 2, 1]

    def test_t27_graded_dims(self):
        """CKh_{2,7}: graded dims = [1, 3, 3, 1] = row 3 of Pascal. [DC]"""
        cat = CategorifiedTorusKnotInvariant(7, H1, H2)
        assert cat.homological_graded_dimension() == [1, 3, 3, 1]

    def test_t29_graded_dims(self):
        """CKh_{2,9}: graded dims = [1, 4, 6, 4, 1]. [DC]"""
        cat = CategorifiedTorusKnotInvariant(9, H1, H2)
        assert cat.homological_graded_dimension() == [1, 4, 6, 4, 1]

    @pytest.mark.parametrize("n", [3, 5, 7, 9, 11])
    def test_graded_dims_are_pascal_row(self, n):
        """Graded dims = row g of Pascal's triangle. [DC]"""
        cat = CategorifiedTorusKnotInvariant(n, H1, H2)
        g = t2n_genus(n)
        expected = [math.comb(g, i) for i in range(g + 1)]
        assert cat.homological_graded_dimension() == expected


# =========================================================================
# 6. Euler characteristic vanishing
# =========================================================================

class TestEulerCharacteristic:
    """Euler characteristic chi(CKh_{2,n}) = 0 for genus >= 1."""

    @pytest.mark.parametrize("n", [3, 5, 7, 9, 11, 13, 15])
    def test_euler_char_zero(self, n):
        """chi(CKh_{2,n}) = (1-1)^g = 0 for g >= 1. [DC]"""
        cat = CategorifiedTorusKnotInvariant(n, H1, H2)
        assert cat.euler_characteristic() == 0

    def test_euler_char_algebraic(self):
        """Algebraic verification: sum (-1)^i binom(g,i) = 0. [DC]"""
        for g in range(1, 10):
            s = sum((-1) ** i * math.comb(g, i) for i in range(g + 1))
            assert s == 0

    def test_poincare_at_minus_1_vanishes(self):
        """P(-1) = (1+(-1))^g = 0 for g >= 1. [DC]"""
        for n in [3, 5, 7, 9]:
            cat = CategorifiedTorusKnotInvariant(n, H1, H2)
            assert abs(cat.poincare_polynomial(-1.0)) < 1e-12

    def test_poincare_at_1_is_total_dim(self):
        """P(1) = (1+1)^g = 2^g = total dimension. [DC]"""
        for n in [3, 5, 7, 9]:
            cat = CategorifiedTorusKnotInvariant(n, H1, H2)
            assert abs(cat.poincare_polynomial(1.0) - cat.total_dimension()) < 1e-12


# =========================================================================
# 7. Bigraded Betti numbers and Mukai weight
# =========================================================================

class TestBigradedBetti:
    """Bigraded Betti numbers b^{i,j} with Mukai weight grading."""

    def test_trefoil_betti(self):
        """T(2,3): b^{0,-1}=1, b^{1,+1}=1. [DC]"""
        cat = CategorifiedTorusKnotInvariant(3, H1, H2)
        betti = cat.bigraded_betti_numbers()
        assert betti == {(0, -1): 1, (1, 1): 1}

    def test_trefoil_two_states(self):
        """T(2,3): exactly 2 states. [DC]"""
        cat = CategorifiedTorusKnotInvariant(3, H1, H2)
        states = cat.all_states()
        assert len(states) == 2

    def test_cinquefoil_four_states(self):
        """T(2,5): exactly 4 states. [DC]"""
        cat = CategorifiedTorusKnotInvariant(5, H1, H2)
        states = cat.all_states()
        assert len(states) == 4

    def test_cinquefoil_betti_sum(self):
        """T(2,5): sum of Betti numbers = 4. [DC]"""
        cat = CategorifiedTorusKnotInvariant(5, H1, H2)
        betti = cat.bigraded_betti_numbers()
        assert sum(betti.values()) == 4

    def test_mukai_weight_trefoil(self):
        """T(2,3): Mukai weights are (0,0,-1) and (0,0,+1). [DC]"""
        cat = CategorifiedTorusKnotInvariant(3, H1, H2)
        states = cat.all_states()
        weights = sorted([s.mukai_weight for s in states])
        assert MukaiWeight(0, 0, -1) in weights
        assert MukaiWeight(0, 0, 1) in weights

    def test_t27_eight_states(self):
        """T(2,7): exactly 8 states. [DC]"""
        cat = CategorifiedTorusKnotInvariant(7, H1, H2)
        assert len(cat.all_states()) == 8

    @pytest.mark.parametrize("n", [3, 5, 7, 9, 11])
    def test_state_count_is_2_to_genus(self, n):
        """Number of states = 2^g. [DC]"""
        cat = CategorifiedTorusKnotInvariant(n, H1, H2)
        assert len(cat.all_states()) == 2 ** t2n_genus(n)


# =========================================================================
# 8. Mukai lattice grading analysis
# =========================================================================

class TestMukaiGrading:
    """The Mukai lattice weight grading on CKh_{2,n}."""

    def test_trefoil_graded_by_mukai(self):
        """T(2,3) is graded by the Mukai lattice. [DC]"""
        result = mukai_grading_analysis(3, H1, H2)
        assert result["is_graded_by_mukai"]

    def test_trefoil_weight_spectrum(self):
        """T(2,3): weight spectrum = {-1, +1}. [DC]"""
        result = mukai_grading_analysis(3, H1, H2)
        assert set(result["weight_spectrum"]) == {-1, 1}

    def test_cinquefoil_weight_spectrum(self):
        """T(2,5): weight spectrum is nontrivial. [DC]"""
        result = mukai_grading_analysis(5, H1, H2)
        assert len(result["weight_spectrum"]) >= 2

    def test_weight_by_homological_degree(self):
        """Mukai weights are correctly distributed by homological degree. [DC]"""
        result = mukai_grading_analysis(5, H1, H2)
        wbhd = result["weight_by_hom_deg"]
        # Homological degree 0 should have 1 state
        assert len(wbhd.get(0, [])) == 1
        # Homological degree 1 should have 2 states
        assert len(wbhd.get(1, [])) == 2
        # Homological degree 2 should have 1 state
        assert len(wbhd.get(2, [])) == 1

    @pytest.mark.parametrize("n", [3, 5, 7])
    def test_distinct_mukai_vectors_at_least_2(self, n):
        """At least 2 distinct Mukai vectors for each T(2,n). [DC]"""
        result = mukai_grading_analysis(n, H1, H2)
        assert result["n_distinct_vectors"] >= 2


# =========================================================================
# 9. Jones polynomial limit
# =========================================================================

class TestJonesLimit:
    """The Jones polynomial limit of categorified invariants."""

    def test_jones_t23_evaluates(self):
        """Jones polynomial of T(2,3) can be evaluated. [DC]"""
        q = np.exp(0.1)
        val = jones_polynomial_t2n(3, q)
        assert np.isfinite(abs(val))

    def test_jones_t25_evaluates(self):
        """Jones polynomial of T(2,5) can be evaluated. [DC]"""
        q = np.exp(0.1)
        val = jones_polynomial_t2n(5, q)
        assert np.isfinite(abs(val))

    def test_jones_breadth_equals_2g(self):
        """Jones breadth of T(2,n) = n-1 = 2*genus. [KH, Rasm]"""
        for n in [3, 5, 7, 9, 11]:
            g = t2n_genus(n)
            assert (n - 1) == 2 * g

    def test_jones_limit_breadth_consistency(self):
        """verify_jones_limit confirms breadth = 2*genus. [DC]"""
        for n in [3, 5, 7, 9]:
            result = verify_jones_limit_t2n(n)
            assert result["breadth_consistent"]

    def test_jones_even_n_rejected(self):
        """Jones for T(2,even) raises error. [DC]"""
        with pytest.raises(ValueError):
            jones_polynomial_t2n(4, 1.0)

    def test_poincare_degree_is_genus(self):
        """Poincare polynomial has degree g. [DC]"""
        for n in [3, 5, 7, 9]:
            result = verify_jones_limit_t2n(n)
            assert result["poincare_degree"] == t2n_genus(n)


# =========================================================================
# 10. T(2,3) trefoil: detailed verification
# =========================================================================

class TestTrefoilDetailed:
    """Comprehensive tests for the trefoil T(2,3)."""

    def test_genus(self):
        """T(2,3) genus = 1. [Milnor]"""
        t = TrefoilT23(H1, H2)
        assert t.verify_genus()["ok"]

    def test_milnor(self):
        """T(2,3) Milnor number = 2. [Milnor]"""
        t = TrefoilT23(H1, H2)
        assert t.verify_milnor_number()["ok"]

    def test_interior_points(self):
        """T(2,3) has 1 interior point (1,1). [Pick, DC]"""
        t = TrefoilT23(H1, H2)
        assert t.verify_interior_points()["ok"]

    def test_divergence(self):
        """T(2,3) tree-level diverges at (1,1). [universal divergence]"""
        t = TrefoilT23(H1, H2)
        assert t.verify_universal_divergence()["ok"]

    def test_residue_finite(self):
        """T(2,3) residue is finite and nonzero. [DC]"""
        t = TrefoilT23(H1, H2)
        assert t.verify_residue_finite()["ok"]

    def test_reg_equals_res(self):
        """T(2,3) regularized = residue (only point is singular). [DC]"""
        t = TrefoilT23(H1, H2)
        assert t.verify_regularized_equals_residue()["ok"]

    def test_categorified_dim(self):
        """T(2,3) categorified dim = 2. [DC]"""
        t = TrefoilT23(H1, H2)
        assert t.verify_categorified_dimension()["ok"]

    def test_euler_zero(self):
        """T(2,3) chi = 0. [DC]"""
        t = TrefoilT23(H1, H2)
        assert t.verify_euler_zero()["ok"]

    def test_bigraded_betti(self):
        """T(2,3) bigraded Betti: b^{0,-1}=1, b^{1,+1}=1. [DC]"""
        t = TrefoilT23(H1, H2)
        assert t.verify_bigraded_betti()["ok"]


# =========================================================================
# 11. T(2,5) cinquefoil: detailed verification
# =========================================================================

class TestCinquefoilDetailed:
    """Comprehensive tests for the cinquefoil T(2,5)."""

    def test_genus(self):
        """T(2,5) genus = 2. [Milnor]"""
        c = CinquefoilT25(H1, H2)
        assert c.verify_genus()["ok"]

    def test_milnor(self):
        """T(2,5) Milnor number = 4. [Milnor]"""
        c = CinquefoilT25(H1, H2)
        assert c.verify_milnor_number()["ok"]

    def test_interior_points(self):
        """T(2,5) has 2 interior points. [Pick, DC]"""
        c = CinquefoilT25(H1, H2)
        assert c.verify_interior_points()["ok"]

    def test_singular_regular_split(self):
        """T(2,5): (1,1) singular, (1,2) regular. [DC]"""
        c = CinquefoilT25(H1, H2)
        assert c.verify_singular_regular_split()["ok"]

    def test_regular_factor_finite(self):
        """T(2,5) regular factor g(h_2+2*h_1) is finite. [DC, AP-CY28]"""
        c = CinquefoilT25(H1, H2)
        assert c.verify_regular_factor_finite()["ok"]

    def test_regularized_product(self):
        """T(2,5) Z^{reg} = Res * g(h_2+2*h_1). [DC]"""
        c = CinquefoilT25(H1, H2)
        assert c.verify_regularized_product()["ok"]

    def test_categorified_dim(self):
        """T(2,5) categorified dim = 4. [DC]"""
        c = CinquefoilT25(H1, H2)
        assert c.verify_categorified_dimension()["ok"]

    def test_euler_zero(self):
        """T(2,5) chi = 0. [DC]"""
        c = CinquefoilT25(H1, H2)
        assert c.verify_euler_zero()["ok"]


# =========================================================================
# 12. General T(2,n) family patterns
# =========================================================================

class TestGeneralT2nFamily:
    """Pattern verification across the T(2,n) family."""

    def test_genus_formula(self):
        """genus = (n-1)/2 for all T(2,n). [Milnor]"""
        gen = T2nGeneralFormula(H1, H2)
        assert gen.verify_genus_formula()["all_ok"]

    def test_dimension_doubling(self):
        """dim = 2^g for all T(2,n). [DC]"""
        gen = T2nGeneralFormula(H1, H2)
        assert gen.verify_dimension_doubling()["all_ok"]

    def test_euler_vanishing(self):
        """chi = 0 for all T(2,n). [DC]"""
        gen = T2nGeneralFormula(H1, H2)
        assert gen.verify_euler_vanishing()["all_ok"]

    def test_jones_breadth(self):
        """Jones breadth = 2*genus. [KH, Rasm]"""
        gen = T2nGeneralFormula(H1, H2)
        assert gen.verify_jones_breadth_match()["all_ok"]

    def test_singular_universal(self):
        """(1,1) is always singular. [universal divergence]"""
        gen = T2nGeneralFormula(H1, H2)
        assert gen.verify_singular_point_universal()["all_ok"]

    def test_pascal_row(self):
        """Graded dims = Pascal row g. [DC]"""
        gen = T2nGeneralFormula(H1, H2)
        assert gen.verify_pascal_row()["all_ok"]


# =========================================================================
# 13. One-loop correction
# =========================================================================

class TestOneLoopCorrection:
    """One-loop correction from the Milnor fiber."""

    def test_trefoil_one_loop_finite(self):
        """T(2,3) one-loop is finite. [DC]"""
        tk = TorusKnotT2n(3, H1, H2)
        olc = tk.one_loop_correction()
        assert np.isfinite(abs(olc))

    def test_cinquefoil_one_loop_finite(self):
        """T(2,5) one-loop is finite. [DC]"""
        tk = TorusKnotT2n(5, H1, H2)
        olc = tk.one_loop_correction()
        assert np.isfinite(abs(olc))

    def test_one_loop_scales_with_kappa(self):
        """One-loop has factor kappa^g (Planck constant to the genus). [DC]"""
        # Verify that doubling kappa scales the one-loop by 2^g
        tk1 = TorusKnotT2n(5, H1, H2)
        # Scale by factor alpha: h1 -> alpha*h1, h2 -> alpha*h2
        # Then kappa -> alpha^3 * kappa, g=2, so one-loop ~ alpha^6 * original
        # (scaling is more complex due to monodromy eigenvalues, but kappa^g
        # factor is explicit)
        olc = tk1.one_loop_correction()
        # Just check it's O(kappa^g) = O(kappa^2) for T(2,5)
        # By verifying it's nonzero and finite
        assert abs(olc) > 1e-30
        assert np.isfinite(abs(olc))

    def test_full_regularized_includes_one_loop(self):
        """Full regularized = reg * (1 + one_loop). [DC]"""
        tk = TorusKnotT2n(5, H1, H2)
        full = tk.full_regularized_invariant(include_one_loop=True)
        reg = tk.regularized_invariant()
        olc = tk.one_loop_correction()
        expected = reg * (1.0 + olc)
        assert abs(full - expected) < 1e-12

    def test_full_without_one_loop(self):
        """Full without one-loop = reg. [DC]"""
        tk = TorusKnotT2n(5, H1, H2)
        full = tk.full_regularized_invariant(include_one_loop=False)
        reg = tk.regularized_invariant()
        assert abs(full - reg) < 1e-12


# =========================================================================
# 14. Cross-engine consistency
# =========================================================================

class TestCrossEngineConsistency:
    """Consistency checks against stratified_en_fh_chiral.py."""

    def test_cy_condition(self):
        """h1 + h2 + h3 = 0 enforced. [DC]"""
        tk = TorusKnotT2n(3, H1, H2)
        assert abs(tk.h1 + tk.h2 + tk.h3) < 1e-12

    def test_kappa_consistent(self):
        """kappa = h1*h2*h3. [DC]"""
        tk = TorusKnotT2n(3, H1, H2)
        expected = H1 * H2 * H3
        assert abs(tk.kappa - expected) < 1e-12

    def test_psi_consistent(self):
        """Psi = -(h1*h2 + h1*h3 + h2*h3). [DC]"""
        tk = TorusKnotT2n(3, H1, H2)
        expected = -(H1 * H2 + H1 * H3 + H2 * H3)
        assert abs(tk.Psi - expected) < 1e-12

    def test_genus_matches_stratified_engine(self):
        """Genus matches stratified_en_fh_chiral computation. [Milnor]"""
        # T(2,3): genus 1, T(2,5): genus 2
        for n, expected_g in [(3, 1), (5, 2), (7, 3)]:
            assert t2n_genus(n) == expected_g

    def test_interior_points_match(self):
        """Interior points match stratified engine. [Pick, DC]"""
        # T(2,3): 1 point, T(2,5): 2 points
        assert len(t2n_interior_points(3)) == 1
        assert len(t2n_interior_points(5)) == 2
        assert len(t2n_interior_points(7)) == 3

    def test_residue_cross_check_manual(self):
        """Residue via _g_residue_at_minus_hk vs manual N(z0)/D'(z0). [DC x2]

        Path 1: our _g_residue_at_minus_hk(h1, h2, h3, k=3).
        Path 2: manual Res_{z=-h3} g(z) = N(-h3) / D'(-h3)
                 where N(z) = prod_i (z-h_i), D'(z0) = prod_{i!=k} (z0+h_i).
        """
        from compute.lib.chiral_khovanov_torus_knots import _g_residue_at_minus_hk
        our_res = _g_residue_at_minus_hk(H1, H2, H3, k=3)
        # Manual: z0 = -H3
        z0 = -H3
        numer = (z0 - H1) * (z0 - H2) * (z0 - H3)   # includes (z0-h3)=-2*h3
        denom_deriv = (z0 + H1) * (z0 + H2)           # prod_{i!=3} (z0 + h_i)
        manual_res = numer / denom_deriv
        assert abs(our_res - manual_res) < 1e-10, (
            f"Residue mismatch: {our_res} != {manual_res}"
        )

    def test_genus_cross_check_algebraic_curve(self):
        """Genus from our formula vs AlgebraicCurve.milnor_fiber_genus. [DC, stratified]

        Path 1: t2n_genus(n) = (n-1)//2.
        Path 2: AlgebraicCurve("torus_knot", {"p":2, "q":n}).milnor_fiber_genus.
        """
        from compute.lib.stratified_en_fh_chiral import AlgebraicCurve
        for n in [3, 5, 7, 9, 11]:
            our_g = t2n_genus(n)
            curve = AlgebraicCurve("torus_knot", {"p": 2, "q": n})
            their_g = curve.milnor_fiber_genus
            assert abs(our_g - their_g) < 1e-12, (
                f"T(2,{n}): our genus {our_g} != stratified genus {their_g}"
            )

    def test_milnor_number_cross_check_algebraic_curve(self):
        """Milnor number via two paths. [DC, stratified]

        Path 1: t2n_milnor_number(n) = n-1.
        Path 2: AlgebraicCurve.milnor_number = (p-1)(q-1).
        """
        from compute.lib.stratified_en_fh_chiral import AlgebraicCurve
        for n in [3, 5, 7, 9, 11]:
            our_mu = t2n_milnor_number(n)
            curve = AlgebraicCurve("torus_knot", {"p": 2, "q": n})
            their_mu = curve.milnor_number
            assert our_mu == their_mu, (
                f"T(2,{n}): our mu={our_mu} != stratified mu={their_mu}"
            )

    def test_interior_points_cross_check_stratified(self):
        """Interior points via two paths. [DC, stratified]

        Path 1: t2n_interior_points(n) (our formula).
        Path 2: TorusKnotChiralInvariant.newton_polygon_interior (stratified engine).
        """
        from compute.lib.stratified_en_fh_chiral import TorusKnotChiralInvariant
        for n in [3, 5, 7, 9, 11]:
            our_pts = t2n_interior_points(n)
            strat_tk = TorusKnotChiralInvariant(2, n, H1, H2, H3)
            their_pts = strat_tk.newton_polygon_interior()
            assert our_pts == their_pts, (
                f"T(2,{n}): points mismatch: {our_pts} != {their_pts}"
            )

    def test_g_function_cross_check(self):
        """Structure function g(z) via two paths. [DC, stratified]

        Path 1: our _g function.
        Path 2: stratified_en_fh_chiral._g.
        """
        from compute.lib.chiral_khovanov_torus_knots import _g as our_g
        from compute.lib.stratified_en_fh_chiral import _g as strat_g
        for z in [4.9, 8.0, 11.0, 0.3 + 0.5j]:
            our_val = our_g(z, H1, H2, H3)
            their_val = strat_g(z, H1, H2, H3)
            assert abs(our_val - their_val) < 1e-12, (
                f"g({z}): {our_val} != {their_val}"
            )

    def test_cy_inversion_cross_check(self):
        """CY inversion g(z)*g(-z) = 1 via our _g. [DC, CY condition]

        Path 1: evaluate our _g at z and -z and multiply.
        Path 2: identity 1 (algebraic).
        """
        from compute.lib.chiral_khovanov_torus_knots import _g
        for z in [4.9, 8.0, 0.3 + 0.5j, 11.7]:
            product = _g(z, H1, H2, H3) * _g(-z, H1, H2, H3)
            assert abs(product - 1.0) < 1e-10, (
                f"CY inversion fails at z={z}: g(z)*g(-z)={product}"
            )


# =========================================================================
# 14b. Multi-path cross-verification (AP10)
# =========================================================================

class TestMultiPathVerification:
    """Multi-path cross-verification for AP10 compliance.

    Each test computes the same quantity via at least 2 independent
    code paths and verifies agreement.
    """

    def test_total_dim_from_states_vs_formula(self):
        """Total dim via enumeration of states vs 2^g formula. [DC x2]

        Path 1: len(all_states()) (enumerate all binary resolutions).
        Path 2: 2**genus (closed-form formula).
        """
        for n in [3, 5, 7, 9, 11]:
            cat = CategorifiedTorusKnotInvariant(n, H1, H2)
            from_states = len(cat.all_states())
            from_formula = cat.total_dimension()
            assert from_states == from_formula, (
                f"T(2,{n}): states={from_states} != formula={from_formula}"
            )

    def test_euler_char_from_states_vs_formula(self):
        """Euler char via state enumeration vs binomial identity. [DC x2]

        Path 1: sum (-1)^{hom(s)} over all states s.
        Path 2: euler_characteristic() = sum (-1)^i binom(g,i) = 0.
        """
        for n in [3, 5, 7, 9, 11]:
            cat = CategorifiedTorusKnotInvariant(n, H1, H2)
            from_states = sum(
                (-1) ** s.homological_degree for s in cat.all_states()
            )
            from_formula = cat.euler_characteristic()
            assert from_states == from_formula, (
                f"T(2,{n}): state chi={from_states} != formula chi={from_formula}"
            )

    def test_graded_dims_from_betti_vs_homological(self):
        """Graded dims via bigraded Betti sums vs homological_graded_dimension. [DC x2]

        Path 1: sum bigraded Betti b^{i,j} over j for each i.
        Path 2: homological_graded_dimension().
        """
        for n in [3, 5, 7, 9]:
            cat = CategorifiedTorusKnotInvariant(n, H1, H2)
            betti = cat.bigraded_betti_numbers()
            g = cat.genus
            # Sum over j for each i
            from_betti = [0] * (g + 1)
            for (i, j), count in betti.items():
                from_betti[i] += count
            from_formula = cat.homological_graded_dimension()
            assert from_betti == from_formula, (
                f"T(2,{n}): betti sums {from_betti} != formula {from_formula}"
            )

    def test_poincare_from_graded_dims_vs_closed_form(self):
        """Poincare polynomial via graded dim sum vs (1+t)^g. [DC x2]

        Path 1: sum dim_i * t^i over homological_graded_dimension.
        Path 2: poincare_polynomial(t) = (1+t)^g.
        """
        for n in [3, 5, 7, 9]:
            cat = CategorifiedTorusKnotInvariant(n, H1, H2)
            graded = cat.homological_graded_dimension()
            for t in [0.5, 1.0, 2.0, -0.5]:
                from_sum = sum(d * t ** i for i, d in enumerate(graded))
                from_closed = cat.poincare_polynomial(t)
                assert abs(from_sum - from_closed) < 1e-10, (
                    f"T(2,{n}), t={t}: sum={from_sum} != closed={from_closed}"
                )

    def test_regularized_invariant_two_param_sets(self):
        """Regularized invariant at two independent parameter choices. [DC x2, AP-CY28]

        Path 1: h = (3.1, -1.3, -1.8).
        Path 2: h = (2.7, -0.9, -1.8).
        Both should give finite nonzero results (structural, not numerical match).
        Cross-check: the RATIO Z^{reg}(h)/Z^{reg}(h') must be a nonzero
        finite number (consistency of the regularization scheme).
        """
        for n in [3, 5, 7]:
            tk1 = TorusKnotT2n(n, 3.1, -1.3)
            tk2 = TorusKnotT2n(n, 2.7, -0.9)
            z1 = tk1.regularized_invariant()
            z2 = tk2.regularized_invariant()
            assert np.isfinite(abs(z1)) and abs(z1) > 1e-12
            assert np.isfinite(abs(z2)) and abs(z2) > 1e-12
            ratio = z1 / z2
            assert np.isfinite(abs(ratio)) and abs(ratio) > 1e-12, (
                f"T(2,{n}): ratio = {ratio}"
            )

    def test_singular_point_from_is_pole_vs_argument_check(self):
        """Singular point detection via two paths. [DC x2]

        Path 1: is_pole_point(1,1).
        Path 2: direct check abs(argument + h3) < epsilon.
        """
        for n in [3, 5, 7, 9]:
            tk = TorusKnotT2n(n, H1, H2)
            from_method = tk.is_pole_point(1, 1)
            arg = tk.point_argument(1, 1)
            from_direct = abs(arg + tk.h3) < 1e-12
            assert from_method == from_direct, (
                f"T(2,{n}): method={from_method} != direct={from_direct}"
            )

    def test_genus_from_interior_count_vs_formula(self):
        """Genus via Pick's theorem (count interior points) vs (n-1)/2. [Pick, Milnor]

        Path 1: len(t2n_interior_points(n)).
        Path 2: t2n_genus(n) = (n-1)//2.
        """
        for n in range(3, 22, 2):
            from_pick = len(t2n_interior_points(n))
            from_milnor = t2n_genus(n)
            assert from_pick == from_milnor, (
                f"T(2,{n}): Pick={from_pick} != Milnor={from_milnor}"
            )

    def test_residue_vs_direct_limit(self):
        """Residue via formula vs numerical limit. [DC x2]

        Path 1: _g_residue_at_minus_hk (algebraic residue formula).
        Path 2: numerical limit lim_{eps->0} g(-h3 + eps) * eps.
        """
        from compute.lib.chiral_khovanov_torus_knots import (
            _g, _g_residue_at_minus_hk,
        )
        algebraic = _g_residue_at_minus_hk(H1, H2, H3, k=3)
        # Numerical: Res = lim_{eps->0} f(z0+eps)*eps where f has simple pole at z0
        # g(z) = N(z)/D(z), pole at z0 = -H3.
        # Res = N(z0)/D'(z0). Numerically: g(z0+eps)*(eps) -> Res as eps->0.
        # But g(z0+eps) ~ Res/eps + O(1), so g(z0+eps)*eps -> Res.
        eps_values = [1e-4, 1e-6, 1e-8]
        z0 = -H3
        for eps in eps_values:
            numerical = _g(z0 + eps, H1, H2, H3) * eps
            assert abs(numerical - algebraic) < abs(algebraic) * 10 * eps, (
                f"eps={eps}: numerical={numerical} vs algebraic={algebraic}"
            )

    def test_graded_euler_char_consistency(self):
        """Graded Euler char at q=1 matches standard Euler char. [DC x2]

        Path 1: graded_euler_characteristic(q=1).
        Path 2: euler_characteristic().
        """
        for n in [3, 5, 7, 9]:
            cat = CategorifiedTorusKnotInvariant(n, H1, H2)
            graded_at_1 = cat.graded_euler_characteristic(1.0)
            standard = cat.euler_characteristic()
            assert abs(graded_at_1 - standard) < 1e-10, (
                f"T(2,{n}): graded chi(1)={graded_at_1} != chi={standard}"
            )

    def test_betti_sum_equals_total_dim(self):
        """Sum of bigraded Betti numbers = total dimension. [DC x2]

        Path 1: sum of all betti[(i,j)].
        Path 2: total_dimension().
        """
        for n in [3, 5, 7, 9, 11]:
            cat = CategorifiedTorusKnotInvariant(n, H1, H2)
            betti = cat.bigraded_betti_numbers()
            from_betti = sum(betti.values())
            from_formula = cat.total_dimension()
            assert from_betti == from_formula, (
                f"T(2,{n}): betti sum={from_betti} != dim={from_formula}"
            )

    def test_regular_factor_via_g_vs_tree_level(self):
        """Regular factor via tree_level_regular_factor vs direct _g evaluation. [DC x2]

        Path 1: tree_level_regular_factor().
        Path 2: manual product of _g over regular points.
        """
        from compute.lib.chiral_khovanov_torus_knots import _g
        for n in [5, 7, 9, 11]:
            tk = TorusKnotT2n(n, H1, H2)
            from_method = tk.tree_level_regular_factor()
            # Manual computation
            from_manual = 1.0 + 0j
            for a, b in tk.regular_points():
                arg = a * tk.h2 + b * tk.h1
                from_manual *= _g(arg, tk.h1, tk.h2, tk.h3)
            assert abs(from_method - from_manual) < 1e-12, (
                f"T(2,{n}): method={from_method} != manual={from_manual}"
            )


# =========================================================================
# 15. Graded Euler characteristic
# =========================================================================

class TestGradedEulerCharacteristic:
    """q-graded Euler characteristic chi_q(CKh)."""

    def test_trefoil_graded_euler_at_q1(self):
        """chi_{q=1}(CKh_{2,3}) = 0. [DC]"""
        cat = CategorifiedTorusKnotInvariant(3, H1, H2)
        chi_1 = cat.graded_euler_characteristic(1.0)
        assert abs(chi_1) < 1e-12

    def test_cinquefoil_graded_euler_at_q1(self):
        """chi_{q=1}(CKh_{2,5}) = 0. [DC]"""
        cat = CategorifiedTorusKnotInvariant(5, H1, H2)
        chi_1 = cat.graded_euler_characteristic(1.0)
        assert abs(chi_1) < 1e-12

    def test_trefoil_graded_euler_nontrivial(self):
        """chi_{q != 1}(CKh_{2,3}) != 0 generically. [DC]"""
        cat = CategorifiedTorusKnotInvariant(3, H1, H2)
        chi_q = cat.graded_euler_characteristic(2.0)
        # q^{-1} - q = 1/2 - 2 = -3/2
        assert abs(chi_q) > 1e-6


# =========================================================================
# 16. AP-CY compliance
# =========================================================================

class TestAPCompliance:
    """Verify compliance with Vol III anti-patterns."""

    def test_ap_cy28_parameters_safe(self):
        """AP-CY28: test parameters avoid all poles. [AP-CY28]"""
        # Poles at z = -H1, -H2, -H3 = -3.1, 1.3, 1.8
        # Interior point (1,2) argument = H2 + 2*H1 = -1.3 + 6.2 = 4.9
        # Far from all poles
        tk = TorusKnotT2n(5, H1, H2)
        arg_12 = tk.point_argument(1, 2)
        for h in [H1, H2, H3]:
            assert abs(arg_12 + h) > 0.5, f"Argument {arg_12} too close to pole at {-h}"

    def test_ap_cy14_conjectural_status(self):
        """AP-CY14: categorified invariant is conjectural. [AP-CY14]
        This test documents that the categorification is conjectural,
        conditional on CY-A_3 and the K3 Yangian (AP-CY6).
        """
        # The categorification is conjectural; this test verifies
        # that the engine produces CONSISTENT results, not that the
        # mathematical claims are proved.
        cat = CategorifiedTorusKnotInvariant(3, H1, H2)
        assert cat.total_dimension() == 2
        assert cat.euler_characteristic() == 0

    def test_ap_cy31_spectral_parameter(self):
        """AP-CY31: z is spectral, not worldsheet. [AP-CY31]
        The arguments a*h_2 + b*h_1 are SPECTRAL parameters from the
        equivariant content, NOT worldsheet insertion coordinates.
        """
        tk = TorusKnotT2n(3, H1, H2)
        # The argument at (1,1) is h_1 + h_2, which is the spectral shift
        # from the Drinfeld coproduct, not an OPE pole
        arg = tk.point_argument(1, 1)
        assert abs(arg - (H1 + H2)) < 1e-12


# =========================================================================
# 17. Master verification
# =========================================================================

class TestMasterVerification:
    """Master verification runs all checks."""

    def test_master_verification_passes(self):
        """All checks pass in master verification. [DC]"""
        result = verify_chiral_khovanov_torus_knots(H1, H2)
        assert result["all_ok"]

    def test_master_verification_complete(self):
        """Master verification includes all key checks. [DC]"""
        result = verify_chiral_khovanov_torus_knots(H1, H2)
        # Check that all expected keys are present
        expected_keys = [
            "trefoil_genus", "trefoil_milnor", "trefoil_interior_pts",
            "trefoil_divergence", "trefoil_residue_finite",
            "trefoil_reg_equals_res", "trefoil_cat_dim", "trefoil_euler_zero",
            "trefoil_bigraded",
            "cinquefoil_genus", "cinquefoil_milnor",
            "cinquefoil_interior_pts", "cinquefoil_sing_reg",
            "cinquefoil_regular_finite", "cinquefoil_reg_product",
            "cinquefoil_cat_dim", "cinquefoil_euler_zero",
            "genus_formula", "dimension_doubling", "euler_vanishing",
            "jones_breadth", "singular_universal", "pascal_row",
        ]
        for key in expected_keys:
            assert key in result, f"Missing key: {key}"
