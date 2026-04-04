"""Tests for the E_2 bar complex B_{E_2}(A).

Verifies the explicit computation of the E_2 bar complex for:
  1. H_k (Heisenberg vertex algebra) -- complete
  2. V_k(sl_2) (affine sl_2) -- first few bidegrees

Manuscript references:
    notes/theory_e2_chiral_formalism.tex, Sections 2-5
    CLAUDE.md: CY-B (E_2-chiral Koszul duality)

Mathematical references:
    Getzler-Jones (1994): E_2 bar construction
    Fresse (2009): E_n operadic bar-cobar
    Tamarkin (2003): Kontsevich formality for E_2
    Frenkel-Ben-Zvi (2004): vertex algebra OPEs
    Kazhdan-Lusztig (1993-94): braided tensor categories for affine algebras
"""

import numpy as np
import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.e2_bar_complex import (
    AffineSL2OPE,
    BarElement,
    E2BarComplex,
    Generator,
    HeisenbergOPE,
    comparison_table,
    compute_e2_bar_heisenberg,
    compute_e2_bar_sl2,
    heisenberg_e2_euler_characteristic,
    heisenberg_inner_product_matrix,
    heisenberg_kt_decomposition,
    heisenberg_monodromy_computation,
    kz_r_matrix_sl2,
    sl2_dx_matrix,
    sl2_what_would_be_needed,
    verify_ce_coderivation_shuffle,
    verify_coderivation,
    verify_d_squared_zero,
    verify_d_X_d_Y_commute,
    verify_qybe_sl2,
    x_first_spectral_sequence_e1,
)


# ================================================================
#  HEISENBERG OPE BASICS
# ================================================================

class TestHeisenbergOPE:
    """Test the OPE data for the Heisenberg VOA H_k."""

    def test_ope_second_order_pole(self):
        """a(z)a(w) ~ k/(z-w)^2: the singular OPE has a second-order pole."""
        k = Symbol("k")
        ope = HeisenbergOPE(k=k)
        sing = ope.ope_singular_part(ope.gen_a, ope.gen_a)
        assert 2 in sing, "Heisenberg OPE must have a second-order pole"
        assert sing[2] == k, f"Coefficient of (z-w)^{{-2}} should be k, got {sing[2]}"

    def test_no_first_order_pole(self):
        """a(z)a(w) has NO first-order pole: this is the critical structural fact."""
        k = Symbol("k")
        ope = HeisenbergOPE(k=k)
        sing = ope.ope_singular_part(ope.gen_a, ope.gen_a)
        assert 1 not in sing, (
            "Heisenberg OPE must NOT have a first-order pole. "
            "The absence of the (z-w)^{-1} term is what makes "
            "the braiding symmetric and d_Y = 0."
        )

    def test_chiral_bracket_vanishes(self):
        """mu(a,a) = Res_{z=w} a(z)a(w) = 0: no residue means no Lie bracket."""
        k = Symbol("k")
        ope = HeisenbergOPE(k=k)
        result = ope.chiral_bracket(ope.gen_a, ope.gen_a)
        assert result is None, (
            f"Chiral bracket mu(a,a) should vanish, got {result}"
        )

    def test_gerstenhaber_bracket_vanishes(self):
        """[a,a]_Ger = 0: the Gerstenhaber bracket is zero for Heisenberg."""
        k = Symbol("k")
        ope = HeisenbergOPE(k=k)
        result = ope.gerstenhaber_bracket(ope.gen_a, ope.gen_a)
        assert result == 0, (
            "Gerstenhaber bracket [a,a] must vanish for the Heisenberg VOA. "
            "Non-vanishing would indicate non-trivial E_2 structure."
        )

    def test_r_matrix_trivial(self):
        """R = id for Heisenberg: the classical r-matrix vanishes."""
        k = Symbol("k")
        ope = HeisenbergOPE(k=k)
        assert ope.r_matrix_classical() == 0

    def test_kappa_heisenberg(self):
        """kappa(H_k) = k, from Volume I (authoritative)."""
        k = Symbol("k")
        ope = HeisenbergOPE(k=k)
        assert ope.kappa == k


# ================================================================
#  HEISENBERG E_2 BAR COMPLEX
# ================================================================

class TestHeisenbergE2Bar:
    """Test the E_2 bar complex B_{E_2}(H_k).

    THE MAIN RESULT: for the Heisenberg, both differentials vanish
    and the braiding is symmetric. The E_2 bar complex is maximally
    degenerate -- it is an E_infty bar complex, not just E_2.
    """

    @pytest.fixture
    def hk_result(self):
        """Compute B_{E_2}(H_k)."""
        return compute_e2_bar_heisenberg(k=Symbol("k"), max_x=4, max_y=4)

    def test_d_X_vanishes(self, hk_result):
        """d_X = 0 for H_k: the chiral bracket mu(a,a) = 0 means the
        bar differential has nothing to insert between adjacent factors.

        This is because:
          a(z)a(w) ~ k/(z-w)^2  (no first-order pole)
        so the residue Res_{z=w} a(z)a(w) = 0, and d_X = sum mu_X = 0.
        """
        assert hk_result["d_X_vanishes"], (
            "d_X must vanish for H_k. The Heisenberg OPE has no "
            "first-order pole, so the bar differential is zero."
        )

    def test_d_Y_vanishes(self, hk_result):
        """d_Y = 0 for H_k: the braiding is symmetric, so the
        Y-direction chiral bracket (Gerstenhaber bracket) vanishes.

        The physical reason: H_k is a free field. Free fields have
        symmetric statistics. The KZ monodromy is trivial.
        """
        assert hk_result["d_Y_vanishes"], (
            "d_Y must vanish for H_k. The braiding is symmetric "
            "(E_infty), so the Y-direction differential is zero."
        )

    def test_braiding_symmetric(self, hk_result):
        """The E_2 braiding for H_k is symmetric: E_2 = E_infty.

        This is the key structural consequence: the Heisenberg VOA,
        being a free field, has no quantum group structure.
        """
        assert hk_result["braiding_symmetric"], (
            "Heisenberg braiding must be symmetric. "
            "Non-symmetric braiding would imply a quantum group, "
            "but free fields don't produce quantum groups."
        )

    def test_dimensions_by_bidegree(self, hk_result):
        """Check dimensions of the bar complex at each bidegree.

        Since H_k has one generator a, each bidegree (p, q) has
        dimension 1 (the unique element [a|...|a]_X repeated q times).
        """
        dims = hk_result["dimensions_by_bidegree"]
        for p in range(1, 5):
            for q in range(1, 5):
                assert dims[(p, q)] == 1, (
                    f"dim B_{{E_2}}(H_k)^{{({p},{q})}} should be 1 "
                    f"(one generator), got {dims[(p, q)]}"
                )

    def test_bar_element_structure(self, hk_result):
        """Check the bar elements have correct bidegree."""
        gens = hk_result["generators_by_bidegree"]
        for (p, q), elems in gens.items():
            for elem in elems:
                assert elem.y_degree == q, (
                    f"Y-degree should be {q}, got {elem.y_degree}"
                )
                assert all(len(b) == p for b in elem.bars), (
                    f"Each X-bar should have length {p}"
                )

    def test_coproduct_Delta_X(self, hk_result):
        """Delta_X is deconcatenation in the X-direction."""
        a = hk_result["ope"].gen_a
        cx = hk_result["complex"]

        # Test on [a|a|a]_X (bidegree (3, 1))
        elem = BarElement(bars=((a, a, a),))
        delta = cx.Delta_X(elem)

        # Should have 2 terms:
        # [a]_X tensor [a|a]_X  and  [a|a]_X tensor [a]_X
        assert len(delta) == 2, (
            f"Delta_X([a|a|a]) should have 2 terms, got {len(delta)}"
        )

    def test_coproduct_Delta_Y(self, hk_result):
        """Delta_Y is deconcatenation in the Y-direction."""
        a = hk_result["ope"].gen_a
        cx = hk_result["complex"]

        # Test on [[a]_X | [a]_X | [a]_X]_Y (bidegree (1, 3))
        elem = BarElement(bars=((a,), (a,), (a,)))
        delta = cx.Delta_Y(elem)

        # Should have 2 terms:
        # [[a]_X]_Y tensor [[a]_X | [a]_X]_Y  and
        # [[a]_X | [a]_X]_Y tensor [[a]_X]_Y
        assert len(delta) == 2, (
            f"Delta_Y on 3-fold Y-bar should have 2 terms, got {len(delta)}"
        )

    def test_spectral_sequence_collapses(self, hk_result):
        """For H_k, the spectral sequence collapses at E_1.

        Since d_X = d_Y = 0, both spectral sequences (X-first and Y-first)
        degenerate immediately: E_1 = E_infty = the raw bigraded space.
        """
        cx = hk_result["complex"]
        gens = hk_result["generators_by_bidegree"]
        e1 = x_first_spectral_sequence_e1(cx, gens)
        for (p, q), dim in e1.items():
            assert dim == 1, (
                f"E_1^{{{p},{q}}} should be 1-dimensional, got {dim}"
            )

    def test_e2_structure_is_e_infty(self, hk_result):
        """The E_2 structure on H_k is actually E_infty.

        Since the braiding is symmetric and the Gerstenhaber bracket
        vanishes, the E_2-algebra structure extends uniquely to an
        E_infty structure. This is a theorem: for E_2-algebras with
        trivial bracket, the E_2 -> E_infty lift is unobstructed.
        """
        assert hk_result["braiding_symmetric"]
        assert hk_result["d_Y_vanishes"]
        # These two conditions together imply E_infty.

    def test_koszul_self_duality(self, hk_result):
        """For H_k with d = 0, the Koszul dual is H_k itself.

        B_{E_2}(H_k) has zero differential, so the Koszul dual
        (cobar of the dual) recovers H_k. The E_2 Koszul dual
        of a free field is the same free field: Sym^ch(V*) is
        self-dual under Koszul duality.
        """
        # The key check: both differentials vanish and the coalgebra
        # structure is the free (cofree) one.
        assert hk_result["d_X_vanishes"]
        assert hk_result["d_Y_vanishes"]
        # Self-duality follows formally.


# ================================================================
#  AFFINE sl_2 OPE BASICS
# ================================================================

class TestAffineSL2OPE:
    """Test the OPE data for V_k(sl_2)."""

    def test_ef_ope(self):
        """e(z)f(w) ~ k/(z-w)^2 + h(w)/(z-w): has BOTH first and second order poles."""
        k = Symbol("k")
        ope = AffineSL2OPE(k=k)
        sing = ope.ope_singular_part(ope.gen_e, ope.gen_f)
        assert 2 in sing and sing[2] == k
        assert 1 in sing

    def test_hh_ope(self):
        """h(z)h(w) ~ 2k/(z-w)^2: second-order pole only."""
        k = Symbol("k")
        ope = AffineSL2OPE(k=k)
        sing = ope.ope_singular_part(ope.gen_h, ope.gen_h)
        assert 2 in sing and sing[2] == 2 * k
        # No first-order pole for h with h
        assert 1 not in sing

    def test_ee_regular(self):
        """e(z)e(w) ~ regular: no singular terms."""
        k = Symbol("k")
        ope = AffineSL2OPE(k=k)
        sing = ope.ope_singular_part(ope.gen_e, ope.gen_e)
        assert len(sing) == 0, "e(z)e(w) should be regular"

    def test_chiral_bracket_sl2(self):
        """The chiral bracket gives the sl_2 Lie algebra."""
        k = Symbol("k")
        ope = AffineSL2OPE(k=k)

        # [e, f] = h
        ef = ope.chiral_bracket(ope.gen_e, ope.gen_f)
        assert ef is not None
        coeff, gen = ef
        assert coeff == 1 and gen.name == "h"

        # [h, e] = 2e
        he = ope.chiral_bracket(ope.gen_h, ope.gen_e)
        assert he is not None
        coeff, gen = he
        assert coeff == 2 and gen.name == "e"

        # [h, f] = -2f
        hf = ope.chiral_bracket(ope.gen_h, ope.gen_f)
        assert hf is not None
        coeff, gen = hf
        assert coeff == -2 and gen.name == "f"

    def test_jacobi_identity(self):
        """The sl_2 structure constants satisfy the Jacobi identity.

        [[e,f],h] + [[f,h],e] + [[h,e],f] = 0

        [e,f] = h, so [[e,f],h] = [h,h] = 0.
        [f,h] = 2f, so [[f,h],e] = 2[f,e] = -2h.
        [h,e] = 2e, so [[h,e],f] = 2[e,f] = 2h.
        Total: 0 + (-2h) + 2h = 0. Checks out.
        """
        k = Symbol("k")
        ope = AffineSL2OPE(k=k)

        ef = ope.chiral_bracket(ope.gen_e, ope.gen_f)  # (1, h)
        fh = ope.chiral_bracket(ope.gen_f, ope.gen_h)  # (2, f)
        he = ope.chiral_bracket(ope.gen_h, ope.gen_e)  # (2, e)

        # [[e,f],h] = [h,h] = 0 (hh has no first-order pole)
        hh = ope.chiral_bracket(ope.gen_h, ope.gen_h)
        assert hh is None  # [h,h] = 0

        # [[f,h],e] = 2*[f,e] = 2*(-1)*h = -2h
        fe = ope.chiral_bracket(ope.gen_f, ope.gen_e)  # (-1, h)
        assert fe is not None
        coeff_fe, gen_fe = fe
        term_fhe = 2 * coeff_fe  # = -2, for generator h

        # [[h,e],f] = 2*[e,f] = 2*1*h = 2h
        coeff_ef, gen_ef = ef
        term_hef = 2 * coeff_ef  # = 2, for generator h

        assert term_fhe + term_hef == 0, (
            f"Jacobi identity violated: {term_fhe} + {term_hef} != 0"
        )

    def test_gerstenhaber_bracket_nonzero(self):
        """The Gerstenhaber bracket is NON-ZERO for V_k(sl_2).

        This is the critical difference from Heisenberg: the non-trivial
        braiding (from KZ monodromy) gives a non-zero degree -1 bracket.
        """
        k = Symbol("k")
        ope = AffineSL2OPE(k=k)
        gb = ope.gerstenhaber_bracket(ope.gen_e, ope.gen_f)
        assert gb != 0, (
            "Gerstenhaber bracket [e,f]_Ger must be non-zero for V_k(sl_2)"
        )

    def test_kappa_sl2(self):
        """kappa(V_k(sl_2)) = 3(k+2)/4."""
        k = Symbol("k")
        ope = AffineSL2OPE(k=k)
        expected = Rational(3, 4) * (k + 2)
        assert simplify(ope.kappa - expected) == 0, (
            f"kappa should be 3(k+2)/4, got {ope.kappa}"
        )


# ================================================================
#  AFFINE sl_2 E_2 BAR COMPLEX
# ================================================================

class TestAffineSL2E2Bar:
    """Test the E_2 bar complex B_{E_2}(V_k(sl_2))."""

    @pytest.fixture
    def sl2_result(self):
        """Compute first few terms of B_{E_2}(V_k(sl_2))."""
        return compute_e2_bar_sl2(k=Symbol("k"), max_x=3, max_y=3)

    def test_braiding_not_symmetric(self, sl2_result):
        """The braiding for V_k(sl_2) is NOT symmetric.

        This is the key non-degeneracy: the KZ monodromy gives a
        genuine E_2 (but not E_infty) structure, which is the source
        of the quantum group.
        """
        assert not sl2_result["braiding_symmetric"], (
            "V_k(sl_2) braiding must NOT be symmetric. "
            "A symmetric braiding would kill the quantum group structure."
        )

    def test_dimensions_bidegree_11(self, sl2_result):
        """dim B_{E_2}(V_k(sl_2))^{(1,1)} = 3 (generators e, f, h)."""
        assert sl2_result["dimensions_by_bidegree"][(1, 1)] == 3

    def test_dimensions_bidegree_21(self, sl2_result):
        """dim B_{E_2}(V_k(sl_2))^{(2,1)} = 9 = 3^2."""
        assert sl2_result["dimensions_by_bidegree"][(2, 1)] == 9

    def test_dimensions_bidegree_12(self, sl2_result):
        """dim B_{E_2}(V_k(sl_2))^{(1,2)} = 9 = 3^2."""
        assert sl2_result["dimensions_by_bidegree"][(1, 2)] == 9

    def test_dimensions_bidegree_22(self, sl2_result):
        """dim B_{E_2}(V_k(sl_2))^{(2,2)} = 81 = 3^4."""
        assert sl2_result["dimensions_by_bidegree"][(2, 2)] == 81

    def test_d_X_on_ef_bar(self, sl2_result):
        """d_X([e|f]_X) = -[h]_X (from mu(e,f) = h, with bar sign)."""
        cx = sl2_result["complex"]
        ope = sl2_result["ope"]
        e, f, h = ope.gen_e, ope.gen_f, ope.gen_h

        elem = BarElement(bars=((e, f),))
        result = cx.d_X(elem)

        assert len(result) == 1, (
            f"d_X([e|f]) should give 1 term, got {len(result)}"
        )
        term = result[0]
        # The result should be [h]_X (possibly with a sign)
        assert len(term.bars) == 1
        assert len(term.bars[0]) == 1
        assert term.bars[0][0].name == "h", (
            f"d_X([e|f]) should give [h], got [{term.bars[0][0]}]"
        )

    def test_d_X_on_he_bar(self, sl2_result):
        """d_X([h|e]_X) should give [2e]_X = 2*[e]_X."""
        cx = sl2_result["complex"]
        ope = sl2_result["ope"]
        e, f, h = ope.gen_e, ope.gen_f, ope.gen_h

        elem = BarElement(bars=((h, e),))
        result = cx.d_X(elem)

        assert len(result) == 1
        term = result[0]
        assert term.bars[0][0].name == "e", (
            f"d_X([h|e]) should give a multiple of [e], got [{term.bars[0][0]}]"
        )

    def test_d_X_on_ee_bar(self, sl2_result):
        """d_X([e|e]_X) = 0 (mu(e,e) = 0)."""
        cx = sl2_result["complex"]
        ope = sl2_result["ope"]
        e = ope.gen_e

        elem = BarElement(bars=((e, e),))
        result = cx.d_X(elem)
        assert len(result) == 0, "d_X([e|e]) should vanish"

    def test_d_X_on_hh_bar(self, sl2_result):
        """d_X([h|h]_X) = 0 (mu(h,h) = 0)."""
        cx = sl2_result["complex"]
        ope = sl2_result["ope"]
        h = ope.gen_h

        elem = BarElement(bars=((h, h),))
        result = cx.d_X(elem)
        assert len(result) == 0, "d_X([h|h]) should vanish"

    def test_d_X_squared_zero(self, sl2_result):
        """d_X^2 = 0 on [e|f|h]_X.

        This follows from the Jacobi identity of sl_2 but is a good
        numerical check of the implementation.
        """
        cx = sl2_result["complex"]
        ope = sl2_result["ope"]
        e, f, h = ope.gen_e, ope.gen_f, ope.gen_h

        elem = BarElement(bars=((e, f, h),))
        assert verify_d_squared_zero(cx, elem), (
            "d_X^2 != 0 on [e|f|h]. This would mean the Jacobi identity fails."
        )

    def test_d_Y_nontrivial_on_sl2(self, sl2_result):
        """d_Y != 0 for V_k(sl_2): check on [[e]_X | [f]_X]_Y.

        d_Y should give a nonzero result proportional to [[h]_X]_Y / (k+2).
        """
        cx = sl2_result["complex"]
        ope = sl2_result["ope"]
        e, f = ope.gen_e, ope.gen_f

        elem = BarElement(bars=((e,), (f,)))
        result = cx.d_Y(elem)

        # d_Y should produce a term involving h
        assert len(result) > 0, (
            "d_Y([[e]|[f]]_Y) must be non-zero for V_k(sl_2). "
            "A zero result would imply symmetric braiding."
        )

    def test_r_matrix_nontrivial(self, sl2_result):
        """The classical r-matrix for V_k(sl_2) is Omega/z * 1/(k+2)."""
        r = sl2_result["r_matrix"]
        assert r != 0, "R-matrix for V_k(sl_2) must be non-trivial"


# ================================================================
#  KZ R-MATRIX NUMERICAL TESTS
# ================================================================

class TestKZRMatrix:
    """Numerical tests for the KZ R-matrix of V_k(sl_2)."""

    @pytest.mark.parametrize("k_val", [1, 2, 3, 4, 5, 10])
    def test_r_matrix_invertible(self, k_val):
        """The R-matrix should be invertible."""
        R = kz_r_matrix_sl2(k_val)
        det = np.linalg.det(R)
        assert abs(det) > 1e-10, (
            f"R-matrix at k={k_val} is singular (det={det})"
        )

    @pytest.mark.parametrize("k_val", [1, 2, 3, 4, 5])
    def test_braid_relation(self, k_val):
        """The R-matrix satisfies the braid relation R_12 R_23 R_12 = R_23 R_12 R_23.

        This is the Yang-Baxter equation for constant R-matrices.
        The braid relation is the operadic coherence of the E_2 structure:
        it comes from pi_1(FM_3(C)) being the pure braid group.
        """
        err = verify_qybe_sl2(k_val)
        assert err < 1e-10, (
            f"Braid relation violated at k={k_val}: ||LHS - RHS|| = {err}"
        )

    def test_rcheck_not_identity(self):
        """Rcheck != P (permutation) for V_k(sl_2): the braiding is not symmetric.

        If Rcheck were the permutation P, then the braiding would be trivial
        (symmetric) and there would be no quantum group structure. The
        deviation Rcheck - P measures the "quantum-ness".
        """
        k_val = 2
        Rcheck = kz_r_matrix_sl2(k_val)

        # The permutation (swap) matrix P on C^2 tensor C^2
        P = np.array([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
        ], dtype=complex)

        diff = np.linalg.norm(Rcheck - P)
        assert diff > 1e-10, (
            f"Rcheck = P at k={k_val}: this would mean no "
            f"quantum group structure. Diff = {diff}"
        )

    def test_rcheck_eigenvalues(self):
        """Eigenvalues of the Jimbo Rcheck for sl_2 fundamental rep.

        The checked R-matrix (braiding) on V tensor V = Sym^2(V) + Lambda^2(V)
        has eigenvalues:
            q  (with multiplicity 3, on Sym^2)
           -1/q  (with multiplicity 1, on Lambda^2)

        This is the standard result from Jimbo (1986): the minimal polynomial
        of Rcheck is (Rcheck - q)(Rcheck + q^{-1}) = 0, giving the
        Hecke relation Rcheck^2 = (q - q^{-1}) Rcheck + 1.
        """
        k_val = 2
        q = np.exp(1j * np.pi / (k_val + 2))
        Rcheck = kz_r_matrix_sl2(k_val)

        evals = np.linalg.eigvals(Rcheck)

        ev_sym = q           # eigenvalue on Sym^2
        ev_alt = -1.0 / q    # eigenvalue on Lambda^2

        close_to_q = sum(1 for ev in evals if abs(ev - ev_sym) < 1e-8)
        close_to_mqi = sum(1 for ev in evals if abs(ev - ev_alt) < 1e-8)

        assert close_to_q == 3, (
            f"Expected 3 eigenvalues q={ev_sym}, found {close_to_q}. "
            f"Eigenvalues: {evals}"
        )
        assert close_to_mqi == 1, (
            f"Expected 1 eigenvalue -1/q={ev_alt}, found {close_to_mqi}. "
            f"Eigenvalues: {evals}"
        )

    @pytest.mark.parametrize("k_val", [1, 2, 3, 5])
    def test_hecke_relation(self, k_val):
        """Rcheck satisfies the Hecke relation: Rcheck^2 = (q - q^{-1}) Rcheck + I.

        This is the defining relation of the Hecke algebra H_n(q), and
        is equivalent to the minimal polynomial (Rcheck - q)(Rcheck + q^{-1}) = 0.
        The Hecke relation is the fundamental algebraic identity underlying
        the Jones polynomial and quantum group representation theory.
        """
        q = np.exp(1j * np.pi / (k_val + 2))
        Rcheck = kz_r_matrix_sl2(k_val)
        I4 = np.eye(4, dtype=complex)

        lhs = Rcheck @ Rcheck
        rhs = (q - 1.0 / q) * Rcheck + I4

        err = np.linalg.norm(lhs - rhs)
        assert err < 1e-10, (
            f"Hecke relation violated at k={k_val}: "
            f"||Rcheck^2 - (q-q^{{-1}})Rcheck - I|| = {err}"
        )


# ================================================================
#  STRUCTURAL IDENTITIES
# ================================================================

class TestStructuralIdentities:
    """Test structural identities of the E_2 bar complex."""

    def test_heisenberg_d_commutator_vanishes(self):
        """[d_X, d_Y] = 0 for H_k: trivially, since both are zero."""
        k = Symbol("k")
        ope = HeisenbergOPE(k=k)
        cx = E2BarComplex(ope=ope)
        a = ope.gen_a

        elem = BarElement(bars=((a, a), (a, a)))
        assert verify_d_X_d_Y_commute(cx, elem), (
            "[d_X, d_Y] != 0 on a Heisenberg element -- impossible"
        )

    def test_sl2_d_commutator_genus_zero(self):
        """[d_X, d_Y] = 0 at genus 0 for V_k(sl_2).

        At genus 0 (on fixed curves), the two differentials commute.
        At genus >= 1, [d_X, d_Y] = kappa * omega_g.
        """
        k = Symbol("k")
        ope = AffineSL2OPE(k=k)
        cx = E2BarComplex(ope=ope)
        e, f = ope.gen_e, ope.gen_f

        # Test on [[e]|[f]]_Y -- simplest non-trivial case
        elem = BarElement(bars=((e,), (f,)))
        assert verify_d_X_d_Y_commute(cx, elem), (
            "[d_X, d_Y] != 0 at genus 0. This is a serious bug: "
            "the two differentials MUST commute at genus 0."
        )

    def test_heisenberg_coderivation(self):
        """d_X is a coderivation w.r.t. Delta_X for Heisenberg.

        Trivially true since d_X = 0, but the structural identity
        still must hold.
        """
        k = Symbol("k")
        ope = HeisenbergOPE(k=k)
        cx = E2BarComplex(ope=ope)
        a = ope.gen_a

        elem = BarElement(bars=((a, a, a),))
        assert verify_coderivation(cx, elem)

    def test_sl2_coderivation_note(self):
        """Document: d_X is a coderivation on Lambda^*(g), not on T(g).

        IMPORTANT SUBTLETY: The CE differential d_CE is a coderivation
        with respect to the wedge coproduct on the EXTERIOR algebra
        Lambda^*(g). Our implementation works on the TENSOR algebra T(g)
        (ordered bar elements [a|b|c], not antisymmetrized).

        On T(g), d_CE is NOT a coderivation with respect to EITHER:
          - The deconcatenation coproduct (which pairs with the bar
            differential of associative algebras, not Lie algebras)
          - The shuffle coproduct (which is the T(g) lift of the wedge
            coproduct, but the identity holds only after antisymmetrization)

        The coderivation property Delta . d = (d x id + id x d) . Delta
        holds on Lambda^*(g) with the wedge coproduct. Verifying this
        numerically would require implementing an explicit antisymmetrization
        map T(g) -> Lambda^*(g) and working on the quotient.

        For the Heisenberg (where d_X = 0), the identity is trivially satisfied.
        """
        # Document the mathematical fact but don't assert a false identity.
        # The Heisenberg case is trivially true:
        k = Symbol("k")
        ope = HeisenbergOPE(k=k)
        cx = E2BarComplex(ope=ope)
        a = ope.gen_a
        elem = BarElement(bars=((a, a, a),))
        assert verify_ce_coderivation_shuffle(cx, elem), (
            "Heisenberg shuffle coderivation should hold trivially (d=0)"
        )


# ================================================================
#  HEISENBERG VS sl_2 COMPARISON
# ================================================================

class TestComparison:
    """Compare H_k and V_k(sl_2) to highlight the key structural differences."""

    def test_heisenberg_is_e_infty_sl2_is_not(self):
        """H_k is E_infty, V_k(sl_2) is genuinely E_2 (not E_infty).

        This is the central dichotomy:
        - Free fields (Heisenberg) => symmetric braiding => E_infty => no quantum group
        - Interacting fields (affine sl_2) => non-symmetric braiding => E_2 => quantum group
        """
        k = Symbol("k")

        hk = HeisenbergOPE(k=k)
        cx_hk = E2BarComplex(ope=hk)
        assert cx_hk.braiding_is_symmetric(), "H_k must be E_infty"

        sl2 = AffineSL2OPE(k=k)
        cx_sl2 = E2BarComplex(ope=sl2)
        assert not cx_sl2.braiding_is_symmetric(), "V_k(sl_2) must NOT be E_infty"

    def test_d_Y_discriminates(self):
        """d_Y = 0 for H_k but d_Y != 0 for V_k(sl_2).

        The Y-differential is the litmus test for genuine E_2 structure.
        """
        k = Symbol("k")

        # Heisenberg: d_Y = 0
        hk = HeisenbergOPE(k=k)
        cx_hk = E2BarComplex(ope=hk)
        a = hk.gen_a
        elem_hk = BarElement(bars=((a,), (a,)))
        assert len(cx_hk.d_Y(elem_hk)) == 0

        # sl_2: d_Y != 0
        sl2 = AffineSL2OPE(k=k)
        cx_sl2 = E2BarComplex(ope=sl2)
        e, f = sl2.gen_e, sl2.gen_f
        elem_sl2 = BarElement(bars=((e,), (f,)))
        assert len(cx_sl2.d_Y(elem_sl2)) > 0

    def test_comparison_table_renders(self):
        """The comparison table should render without errors."""
        table = comparison_table()
        assert "H_k" in table
        assert "V_k(sl_2)" in table
        assert "E_infty" in table
        assert "q^{Omega/2}" in table


# ================================================================
#  EDGE CASES AND VALIDATION
# ================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_single_generator_bar(self):
        """A bar element with a single generator has d_X = 0 trivially."""
        k = Symbol("k")
        ope = AffineSL2OPE(k=k)
        cx = E2BarComplex(ope=ope)
        e = ope.gen_e

        elem = BarElement(bars=((e,),))
        result = cx.d_X(elem)
        assert len(result) == 0, "d_X on a length-1 bar must vanish"

    def test_single_y_factor_delta_y(self):
        """Delta_Y on a single Y-factor is zero (no way to split)."""
        k = Symbol("k")
        ope = HeisenbergOPE(k=k)
        cx = E2BarComplex(ope=ope)
        a = ope.gen_a

        elem = BarElement(bars=((a, a),))  # y_degree = 1
        delta = cx.Delta_Y(elem)
        assert len(delta) == 0, "Delta_Y on y_degree=1 must be empty"

    def test_generator_repr(self):
        """Generator repr is the name."""
        g = Generator("e", weight=1)
        assert repr(g) == "e"

    def test_bar_element_bidegree(self):
        """Check bidegree computation."""
        e = Generator("e")
        f = Generator("f")
        h = Generator("h")

        # [[e|f]_X | [h]_X]_Y has total X-degree 3, Y-degree 2
        elem = BarElement(bars=((e, f), (h,)))
        assert elem.bidegree == (3, 2)
        assert elem.y_degree == 2
        assert elem.x_degrees == (2, 1)

    def test_heisenberg_numeric_k(self):
        """Computation works with numeric k."""
        result = compute_e2_bar_heisenberg(k=Rational(1), max_x=3, max_y=3)
        assert result["d_X_vanishes"]
        assert result["d_Y_vanishes"]
        assert result["kappa"] == Rational(1)  # kappa(H_k) = k, not k/2

    def test_sl2_numeric_k(self):
        """Computation works with numeric k for sl_2."""
        result = compute_e2_bar_sl2(k=Rational(1), max_x=2, max_y=2)
        assert not result["braiding_symmetric"]
        expected_kappa = Rational(3, 4) * 3  # 3(1+2)/4 = 9/4
        assert simplify(result["kappa"] - expected_kappa) == 0


# ================================================================
#  KONTSEVICH-TAMARKIN DECOMPOSITION FOR H_k
# ================================================================

class TestHeisenbergKTDecomposition:
    """Test the Kontsevich-Tamarkin decomposition B_{E_2}(H_k) ~ B_comm x C_CE."""

    def test_harrison_dims(self):
        """Harrison complex of Sym(V), dim V = 1: each degree is 1-dimensional."""
        result = heisenberg_kt_decomposition()
        for p in range(1, 7):
            assert result["harrison_dims"][p] == 1, (
                f"Harrison dim at degree {p} should be 1"
            )

    def test_ce_dims_one_generator(self):
        """CE of a 1-dim vector space with zero bracket: Lambda^0 = Lambda^1 = k."""
        result = heisenberg_kt_decomposition()
        assert result["ce_dims"][0] == 1
        assert result["ce_dims"][1] == 1
        for q in range(2, 7):
            assert result["ce_dims"][q] == 0, (
                f"Lambda^{q}(k) = 0 for q >= 2"
            )

    def test_kt_product_dims(self):
        """Product dimensions: B_comm^p tensor CE^q."""
        result = heisenberg_kt_decomposition()
        for p in range(1, 7):
            assert result["kt_dims"][(p, 0)] == 1
            assert result["kt_dims"][(p, 1)] == 1
            for q in range(2, 7):
                assert result["kt_dims"][(p, q)] == 0

    def test_euler_characteristic_vanishes(self):
        """Euler characteristic is 0 for the E_2 bar complex of H_k.

        Since d = 0, chi = sum (-1)^{p+q} * dim B^{p,q}.
        For one generator with dim 1 at each (p,q) with p,q >= 1:
        chi = (sum_{p>=1} (-1)^p)^2 which is formally 1/4 (regularized)
        but the truncated version alternates.
        """
        result_val = heisenberg_kt_decomposition()
        assert result_val["euler_char"] == Rational(0)

    def test_inner_product_level_k(self):
        """Inner product on B_X^p(H_k) is k^p * p!."""
        from sympy import factorial
        k = Symbol("k")
        result = heisenberg_kt_decomposition(k=k)
        ip = result["inner_product"]
        for p in range(1, 7):
            expected = k**p * factorial(p)
            assert simplify(ip[p] - expected) == 0, (
                f"Inner product at degree {p}: expected {expected}, got {ip[p]}"
            )


# ================================================================
#  HEISENBERG INNER PRODUCT
# ================================================================

class TestHeisenbergInnerProduct:
    """Test the inner product on B_X(H_k) from the level-k pairing."""

    def test_degree_1(self):
        """<[a], [a]> = k."""
        k = Symbol("k")
        ip = heisenberg_inner_product_matrix(k=k)
        assert ip[1] == k

    def test_degree_2(self):
        """<[a|a], [a|a]> = k^2 * 2! = 2k^2."""
        k = Symbol("k")
        ip = heisenberg_inner_product_matrix(k=k)
        assert simplify(ip[2] - 2 * k**2) == 0

    def test_degree_3(self):
        """<[a|a|a], [a|a|a]> = k^3 * 3! = 6k^3."""
        k = Symbol("k")
        ip = heisenberg_inner_product_matrix(k=k)
        assert simplify(ip[3] - 6 * k**3) == 0

    def test_numeric_k1(self):
        """At k=1: inner product at degree p is p!."""
        from sympy import factorial
        ip = heisenberg_inner_product_matrix(k=Rational(1))
        for p in range(1, 6):
            assert ip[p] == factorial(p)

    def test_non_degeneracy(self):
        """Inner product is non-degenerate for k != 0."""
        k = Symbol("k", nonzero=True)
        ip = heisenberg_inner_product_matrix(k=k)
        for p in range(1, 6):
            assert simplify(ip[p]) != 0, (
                f"Inner product at degree {p} is degenerate"
            )


# ================================================================
#  HEISENBERG EULER CHARACTERISTIC
# ================================================================

class TestHeisenbergEulerChar:
    """Test Euler characteristic of B_{E_2}(H_k)."""

    def test_even_truncation(self):
        """For even max_total, the truncated chi = 0."""
        assert heisenberg_e2_euler_characteristic(max_total=4) == 0
        assert heisenberg_e2_euler_characteristic(max_total=10) == 0

    def test_odd_truncation(self):
        """For odd max_total, the truncated chi = 1."""
        assert heisenberg_e2_euler_characteristic(max_total=3) == 1
        assert heisenberg_e2_euler_characteristic(max_total=5) == 1


# ================================================================
#  HEISENBERG MONODROMY
# ================================================================

class TestHeisenbergMonodromy:
    """Test the explicit monodromy computation for R = id."""

    def test_monodromy_trivial(self):
        """Total monodromy is 1 (R = id)."""
        result = heisenberg_monodromy_computation()
        assert result["total_monodromy"] == 1

    def test_r_matrix_identity(self):
        """R-matrix is the identity."""
        result = heisenberg_monodromy_computation()
        assert result["r_matrix"] == "id"

    def test_singular_exponents(self):
        """Only exponent is -2 (second-order pole)."""
        result = heisenberg_monodromy_computation()
        assert result["ope_singular_exponents"] == [-2]

    def test_physical_reason_documented(self):
        """Physical reason is documented."""
        result = heisenberg_monodromy_computation()
        assert "second-order pole" in result["physical_reason"]
        assert "no first-order pole" in result["physical_reason"].lower() or \
               "No first-order pole" in result["physical_reason"]


# ================================================================
#  sl_2 CE COHOMOLOGY VIA d_X MATRICES
# ================================================================

class TestSL2DXMatrix:
    """Test the explicit d_X matrices for V_k(sl_2)."""

    @pytest.fixture
    def sl2_dx(self):
        """Compute d_X matrices."""
        k = Symbol("k")
        ope = AffineSL2OPE(k=k)
        return sl2_dx_matrix(ope)

    def test_d_2_to_1_shape(self, sl2_dx):
        """d_X: degree 2 -> degree 1 is a 3 x 9 matrix."""
        d = sl2_dx["d_2_to_1"]
        assert d.shape == (3, 9), f"Expected (3, 9), got {d.shape}"

    def test_d_3_to_2_shape(self, sl2_dx):
        """d_X: degree 3 -> degree 2 is a 9 x 27 matrix."""
        d = sl2_dx["d_3_to_2"]
        assert d.shape == (9, 27), f"Expected (9, 27), got {d.shape}"

    def test_d_2_to_1_rank(self, sl2_dx):
        """rank(d_2_to_1) = 3 (sl_2 has trivial center, so d is surjective).

        The CE differential at degree 2->1 maps 9 basis elements to 3.
        Since sl_2 is simple (has no center), every generator is in the
        image of the bracket, so rank = 3 and H^1 = 3 - 3 = 0.
        """
        assert sl2_dx["rank_d21"] == 3, (
            f"rank(d_2_to_1) should be 3, got {sl2_dx['rank_d21']}"
        )

    def test_h1_vanishes(self, sl2_dx):
        """H^1(sl_2, k) = 0 (Whitehead's first lemma for semisimple Lie algebras)."""
        assert sl2_dx["h1_dim"] == 0, (
            f"H^1(sl_2) should be 0, got {sl2_dx['h1_dim']}"
        )

    def test_d_ef_gives_h(self, sl2_dx):
        """d_X([e|f]) should give [h] (with a sign).

        In the basis ordering e=0, f=1, h=2 and (e,f) = index 1 in the
        9-element basis, the column for (e,f) in d_2_to_1 should have
        a nonzero entry in the h row.
        """
        d = sl2_dx["d_2_to_1"]
        # basis_2 ordering: (e,e)=0, (e,f)=1, (e,h)=2, (f,e)=3, ...
        # h is at index 2 in basis_1
        # d_2_to_1[2, 1] should be nonzero (h coefficient of d([e|f]))
        assert d[2, 1] != 0, (
            "d_X([e|f]) should have a nonzero h-component"
        )

    def test_d_ee_vanishes(self, sl2_dx):
        """d_X([e|e]) = 0 since [e,e] = 0."""
        d = sl2_dx["d_2_to_1"]
        # (e,e) is at index 0 in basis_2
        col = d[:, 0]
        assert col == col * 0, "d_X([e|e]) should be zero"

    def test_d_squared_zero_via_matrices(self, sl2_dx):
        """d_2_to_1 . d_3_to_2 = 0 (d^2 = 0).

        This is the matrix-level verification that the CE differential
        squares to zero, which follows from the Jacobi identity.
        """
        product = sl2_dx["d_2_to_1"] * sl2_dx["d_3_to_2"]
        assert product == product * 0, (
            "d^2 != 0: the product d_2_to_1 * d_3_to_2 is nonzero. "
            "This would mean the Jacobi identity fails for sl_2."
        )


# ================================================================
#  SHUFFLE COPRODUCT TESTS
# ================================================================

class TestShuffleCoproduct:
    """Test the shuffle (exterior) coproduct Delta_X_shuffle."""

    def test_shuffle_on_two_elements(self):
        """Delta_shuffle([a|b]) = [a] tensor [b] - [b] tensor [a].

        The shuffle coproduct of [e|f] has two terms from choosing
        subsets S={0}, T={1} (sign +1) and S={1}, T={0} (sign -1).
        """
        e = Generator("e")
        f = Generator("f")
        k = Symbol("k")
        ope = AffineSL2OPE(k=k)
        cx = E2BarComplex(ope=ope)

        elem = BarElement(bars=((e, f),))
        result = cx.Delta_X_shuffle(elem)

        # Should have 2 terms
        assert len(result) == 2, (
            f"Delta_shuffle on 2-element bar should have 2 terms, got {len(result)}"
        )

        # Collect (left_x_bar, right_x_bar) -> coefficient.
        # BarElement.bars for a single Y-factor: bars = ((gens...),),
        # so bars[0] is the X-bar tuple of generators.
        coeffs = {}
        for left, right in result:
            left_gens = left.bars[0]   # tuple of generators in left X-bar
            right_gens = right.bars[0]  # tuple of generators in right X-bar
            coeffs[(left_gens, right_gens)] = left.coeff

        # S={0}->e, T={1}->f: unshuffle (0,1) has sign +1
        assert coeffs[((e,), (f,))] == 1, (
            f"Expected coeff +1 for (e) tensor (f), got {coeffs.get(((e,), (f,)))}"
        )
        # S={1}->f, T={0}->e: unshuffle (1,0) has sign -1
        assert coeffs[((f,), (e,))] == -1, (
            f"Expected coeff -1 for (f) tensor (e), got {coeffs.get(((f,), (e,)))}"
        )

    def test_shuffle_on_three_elements(self):
        """Delta_shuffle on [e|f|h] has 6 terms (2-choose from 3, both ways)."""
        e = Generator("e")
        f = Generator("f")
        h = Generator("h")
        k = Symbol("k")
        ope = AffineSL2OPE(k=k)
        cx = E2BarComplex(ope=ope)

        elem = BarElement(bars=((e, f, h),))
        result = cx.Delta_X_shuffle(elem)

        # C(3,1) + C(3,2) = 3 + 3 = 6 terms
        assert len(result) == 6, (
            f"Delta_shuffle on 3-element bar should have 6 terms, got {len(result)}"
        )

    def test_heisenberg_shuffle_coderivation(self):
        """CE coderivation w.r.t. shuffle is trivially true for H_k (d_X = 0)."""
        k = Symbol("k")
        ope = HeisenbergOPE(k=k)
        cx = E2BarComplex(ope=ope)
        a = ope.gen_a

        elem = BarElement(bars=((a, a, a),))
        assert verify_ce_coderivation_shuffle(cx, elem)


# ================================================================
#  DOCUMENTATION / WHAT IS NEEDED FOR sl_2
# ================================================================

class TestDocumentation:
    """Test that documentation functions produce output."""

    def test_sl2_what_needed(self):
        """The sl_2 roadmap document renders."""
        doc = sl2_what_would_be_needed()
        assert "KZ" in doc
        assert "Omega" in doc
        assert "Koszul dual" in doc.lower() or "KOSZUL DUAL" in doc

    def test_comparison_table_structure(self):
        """Comparison table has all expected rows."""
        table = comparison_table()
        assert "kappa" in table
        assert "k" in table  # kappa(H_k) = k (corrected from k/2)
        assert "3(k+2)/4" in table
        assert "deconcatenation" in table
