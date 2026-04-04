r"""Tests for matrix_factorization_shadow.py

Tests the LG/CY correspondence computations: ADE singularities,
Jacobian rings, residue pairings, modular characteristics (kappa),
Knorrer periodicity, Gepner models, bar complex data, and the
LG/CY correspondence for the quintic threefold.

55+ tests organized in thematic groups.
"""

import pytest
from fractions import Fraction
from sympy import Rational, Matrix, det, simplify

from compute.lib.matrix_factorization_shadow import (
    ADESingularity,
    make_A,
    make_D,
    make_E,
    all_ade_singularities,
    jacobian_ring_basis_A,
    jacobian_ring_basis_D,
    jacobian_ring_basis_E,
    milnor_number,
    residue_pairing_A,
    residue_pairing_matrix_A,
    residue_pairing_E6,
    residue_pairing_E8,
    hessian_trace_A,
    kappa_mf,
    kappa_n2_minimal,
    kappa_affine_from_mf,
    shadow_tower_rank,
    n2_central_charge,
    n2_central_charge_D,
    n2_central_charge_E,
    knorrer_stabilize,
    sebastiani_thom,
    GepnerModel,
    quintic_gepner,
    bar_complex_A,
    bar_cohomology_A,
    curved_ainfty_curvature,
    degree_to_kappa_relation,
    QuinticCYData,
    quintic_lgcy_check,
    multiplication_matrix_A,
    hessian_element_A,
    multiplication_trace_A,
    residue_trace_A,
    ade_shadow_summary,
)


# ============================================================================
# 1. ADE singularity construction and basic invariants
# ============================================================================

class TestADEConstruction:
    """Test ADE singularity data structures."""

    def test_A2_milnor(self):
        """A_2: W = x^3, mu = 2."""
        s = make_A(3)
        assert s.milnor_number == 2
        assert s.type_name == "A2"

    def test_A3_milnor(self):
        """A_3: W = x^4, mu = 3."""
        s = make_A(4)
        assert s.milnor_number == 3

    def test_A4_milnor(self):
        """A_4: W = x^5, mu = 4."""
        s = make_A(5)
        assert s.milnor_number == 4

    def test_A1_milnor(self):
        """A_1: W = x^2, mu = 1."""
        s = make_A(2)
        assert s.milnor_number == 1
        assert s.coxeter_number == 2

    def test_D4_milnor(self):
        """D_4: W = x^3 + xy^2, mu = 4."""
        s = make_D(4)
        assert s.milnor_number == 4
        assert s.coxeter_number == 6

    def test_D5_milnor(self):
        """D_5: W = x^4 + xy^2, mu = 5."""
        s = make_D(5)
        assert s.milnor_number == 5
        assert s.coxeter_number == 8

    def test_E6_milnor(self):
        """E_6: W = x^3 + y^4, mu = 6."""
        s = make_E(6)
        assert s.milnor_number == 6
        assert s.coxeter_number == 12

    def test_E7_milnor(self):
        """E_7: W = x^3 + xy^3, mu = 7."""
        s = make_E(7)
        assert s.milnor_number == 7
        assert s.coxeter_number == 18

    def test_E8_milnor(self):
        """E_8: W = x^3 + y^5, mu = 8."""
        s = make_E(8)
        assert s.milnor_number == 8
        assert s.coxeter_number == 30

    def test_A_invalid(self):
        """A-type requires n >= 2."""
        with pytest.raises(ValueError):
            make_A(1)

    def test_D_invalid(self):
        """D-type requires n >= 4."""
        with pytest.raises(ValueError):
            make_D(3)

    def test_E_invalid(self):
        """E-type requires n in {6,7,8}."""
        with pytest.raises(ValueError):
            make_E(5)

    def test_lie_dims(self):
        """Verify Lie algebra dimensions for all ADE types."""
        # sl_n: dim = n^2 - 1
        assert make_A(2).lie_dim == 3   # sl_2
        assert make_A(3).lie_dim == 8   # sl_3
        assert make_A(4).lie_dim == 15  # sl_4

        # so_{2n}: dim = n(2n-1)
        assert make_D(4).lie_dim == 28  # so_8
        assert make_D(5).lie_dim == 45  # so_10

        # Exceptional
        assert make_E(6).lie_dim == 78
        assert make_E(7).lie_dim == 133
        assert make_E(8).lie_dim == 248

    def test_all_ade_count(self):
        """Check total count of ADE singularities up to rank 8."""
        sings = all_ade_singularities(8)
        # A_1 through A_8 (n=2..9): 8
        # D_4 through D_8: 5
        # E_6, E_7, E_8: 3
        # Total: 16
        assert len(sings) == 16


# ============================================================================
# 2. Milnor numbers
# ============================================================================

class TestMilnorNumbers:
    """Verify Milnor numbers for all types."""

    def test_milnor_A_type(self):
        """mu(A_{n-1}) = n-1."""
        for param in range(1, 10):
            assert milnor_number('A', param) == param

    def test_milnor_D_type(self):
        """mu(D_n) = n."""
        for param in range(4, 10):
            assert milnor_number('D', param) == param

    def test_milnor_E_type(self):
        """mu(E_n) = n for n = 6, 7, 8."""
        for n in [6, 7, 8]:
            assert milnor_number('E', n) == n

    def test_shadow_rank_equals_milnor(self):
        """Shadow tower rank = Milnor number for all ADE."""
        for s in all_ade_singularities(8):
            assert shadow_tower_rank(s) == s.milnor_number


# ============================================================================
# 3. Jacobian ring bases
# ============================================================================

class TestJacobianBases:
    """Verify Jacobian ring bases have correct dimension."""

    def test_jac_A2(self):
        """Jac(x^3) has basis {1, x}, dim 2."""
        basis = jacobian_ring_basis_A(3)
        assert len(basis) == 2

    def test_jac_A3(self):
        """Jac(x^4) has basis {1, x, x^2}, dim 3."""
        basis = jacobian_ring_basis_A(4)
        assert len(basis) == 3

    def test_jac_A4(self):
        """Jac(x^5) has basis {1, x, x^2, x^3}, dim 4."""
        basis = jacobian_ring_basis_A(5)
        assert len(basis) == 4

    def test_jac_D4(self):
        """Jac(x^3 + xy^2) has dim 4."""
        basis = jacobian_ring_basis_D(4)
        assert len(basis) == 4

    def test_jac_D5(self):
        """Jac(x^4 + xy^2) has dim 5."""
        basis = jacobian_ring_basis_D(5)
        assert len(basis) == 5

    def test_jac_E6(self):
        """Jac(x^3 + y^4) has dim 6."""
        basis = jacobian_ring_basis_E(6)
        assert len(basis) == 6

    def test_jac_E7(self):
        """Jac(x^3 + xy^3) has dim 7."""
        basis = jacobian_ring_basis_E(7)
        assert len(basis) == 7

    def test_jac_E8(self):
        """Jac(x^3 + y^5) has dim 8."""
        basis = jacobian_ring_basis_E(8)
        assert len(basis) == 8

    def test_jac_dim_equals_milnor(self):
        """For all A-types, dim Jac = mu."""
        for n in range(2, 12):
            basis = jacobian_ring_basis_A(n)
            assert len(basis) == n - 1


# ============================================================================
# 4. Residue pairing
# ============================================================================

class TestResiduePairing:
    """Verify the Grothendieck residue pairing on Jacobian rings."""

    def test_residue_A2_unit(self):
        """<1, x> on Jac(x^3): coeff of x^1 in 1*x = 1. Res = 1/3."""
        val = residue_pairing_A(3, [Rational(1)], [Rational(0), Rational(1)])
        assert val == Rational(1, 3)

    def test_residue_A2_top(self):
        """<x, x> on Jac(x^3): coeff of x^1 in x*x = x^2. But x^2 has degree 2 > 1.
        target_deg = n-2 = 1. coeff of x^1 in x*x: i+j=1 with i=1,j=0 => a_1*b_0.
        f = [0,1] (= x), g = [0,1] (= x). i=1,j=1: i+j=2 != 1. No hit for target.
        Actually: f = x has coeffs [0, 1]. g = x has coeffs [0, 1].
        Pairs (i,j) with i+j=1: (0,1) -> a_0*b_1 = 0*1 = 0, (1,0) -> a_1*b_0 = 1*0 = 0.
        So <x,x> = 0. Correct: x*x = x^2 which has degree 2 > n-2=1, so vanishes in Jac."""
        val = residue_pairing_A(3, [Rational(0), Rational(1)], [Rational(0), Rational(1)])
        assert val == Rational(0)

    def test_residue_A3_standard(self):
        """<1, x^2> on Jac(x^4): target deg = 2. coeff of x^2 in 1*x^2 = 1. Res = 1/4."""
        val = residue_pairing_A(4, [Rational(1)], [Rational(0), Rational(0), Rational(1)])
        assert val == Rational(1, 4)

    def test_residue_A3_cross(self):
        """<x, x> on Jac(x^4): target deg = 2. f=g=[0,1]. i=1,j=1: 1*1=1. Res = 1/4."""
        val = residue_pairing_A(4, [Rational(0), Rational(1)], [Rational(0), Rational(1)])
        assert val == Rational(1, 4)

    def test_residue_matrix_A3_symmetric(self):
        """The residue pairing matrix for Jac(x^4) is symmetric."""
        M = residue_pairing_matrix_A(4)
        assert M == M.T

    def test_residue_matrix_A3_antidiag(self):
        """For Jac(x^4), the pairing matrix is anti-diagonal (up to 1/n)."""
        M = residue_pairing_matrix_A(4)
        # M should be 3x3 with M[i,j] = (1/4)*delta_{i+j,2}
        assert M[0, 2] == Rational(1, 4)
        assert M[1, 1] == Rational(1, 4)
        assert M[2, 0] == Rational(1, 4)
        assert M[0, 0] == 0
        assert M[0, 1] == 0

    def test_residue_matrix_nondegenerate(self):
        """The residue pairing is nondegenerate for all A-types."""
        for n in range(2, 8):
            M = residue_pairing_matrix_A(n)
            assert det(M) != 0

    def test_residue_E6_symmetric(self):
        """E6 residue pairing is symmetric."""
        M = residue_pairing_E6()
        assert M == M.T

    def test_residue_E6_nondegenerate(self):
        """E6 residue pairing is nondegenerate."""
        M = residue_pairing_E6()
        assert det(M) != 0

    def test_residue_E8_symmetric(self):
        """E8 residue pairing is symmetric."""
        M = residue_pairing_E8()
        assert M == M.T

    def test_residue_E8_nondegenerate(self):
        """E8 residue pairing is nondegenerate."""
        M = residue_pairing_E8()
        assert det(M) != 0


# ============================================================================
# 5. Modular characteristic kappa
# ============================================================================

class TestKappa:
    """Verify kappa computations from matrix factorizations."""

    def test_kappa_mf_A2(self):
        """kappa_{MF}(A_2) = mu/2 = 2/2 = 1."""
        s = make_A(3)
        assert kappa_mf(s) == Rational(1)

    def test_kappa_mf_A3(self):
        """kappa_{MF}(A_3) = mu/2 = 3/2."""
        s = make_A(4)
        assert kappa_mf(s) == Rational(3, 2)

    def test_kappa_mf_A4(self):
        """kappa_{MF}(A_4) = mu/2 = 4/2 = 2."""
        s = make_A(5)
        assert kappa_mf(s) == Rational(2)

    def test_kappa_mf_D4(self):
        """kappa_{MF}(D_4) = mu/2 = 4/2 = 2."""
        s = make_D(4)
        assert kappa_mf(s) == Rational(2)

    def test_kappa_mf_E6(self):
        """kappa_{MF}(E_6) = mu/2 = 6/2 = 3."""
        s = make_E(6)
        assert kappa_mf(s) == Rational(3)

    def test_kappa_mf_E7(self):
        """kappa_{MF}(E_7) = mu/2 = 7/2."""
        s = make_E(7)
        assert kappa_mf(s) == Rational(7, 2)

    def test_kappa_mf_E8(self):
        """kappa_{MF}(E_8) = mu/2 = 8/2 = 4."""
        s = make_E(8)
        assert kappa_mf(s) == Rational(4)

    def test_kappa_vir_A2(self):
        """For A_2 (n=3): c = 3*1/3 = 1, kappa_Vir = 1/2."""
        assert kappa_n2_minimal(3) == Rational(1, 2)

    def test_kappa_vir_A3(self):
        """For A_3 (n=4): c = 3*2/4 = 3/2, kappa_Vir = 3/4."""
        assert kappa_n2_minimal(4) == Rational(3, 4)

    def test_kappa_vir_A4(self):
        """For A_4 (n=5): c = 3*3/5 = 9/5, kappa_Vir = 9/10."""
        assert kappa_n2_minimal(5) == Rational(9, 10)

    def test_kappa_mf_vs_vir_distinct(self):
        """kappa_{MF} != kappa_{Vir} in general (they are different invariants).

        kappa_{MF} = mu/2 (categorical).
        kappa_{Vir} = c/2 = 3(n-2)/(2n) (Virasoro sub-algebra).
        These differ because kappa_{MF} counts ALL fields in the CY category,
        while kappa_{Vir} only counts the Virasoro part.
        """
        for n in range(3, 10):
            s = make_A(n)
            k_mf = kappa_mf(s)
            k_vir = kappa_n2_minimal(n)
            # They should be different (except possibly at n=infinity)
            assert k_mf != k_vir, f"Unexpected equality at n={n}"

    def test_hessian_trace_A2(self):
        """Tr(Hess(x^3)) = 2 = mu."""
        assert hessian_trace_A(3) == Rational(2)

    def test_hessian_trace_A3(self):
        """Tr(Hess(x^4)) = 3 = mu."""
        assert hessian_trace_A(4) == Rational(3)

    def test_hessian_trace_equals_milnor(self):
        """Tr(Hess(x^n)) = n-1 = mu for all n."""
        for n in range(2, 15):
            assert hessian_trace_A(n) == Rational(n - 1)

    def test_kappa_affine_sl2_level1(self):
        """kappa(V_1(sl_2)) = (1+2)*3/(2*2) = 9/4.

        sl_2: dim = 3, h = h^v = 2.
        """
        s = make_A(2)  # A_1 <-> sl_2
        k = kappa_affine_from_mf(s, level=1)
        assert k == Rational(9, 4)

    def test_kappa_affine_sl3_level1(self):
        """kappa(V_1(sl_3)) = (1+3)*8/(2*3) = 16/3.

        sl_3: dim = 8, h = h^v = 3.
        """
        s = make_A(3)  # A_2 <-> sl_3
        k = kappa_affine_from_mf(s, level=1)
        assert k == Rational(16, 3)


# ============================================================================
# 6. N=2 central charges
# ============================================================================

class TestCentralCharge:
    """Verify central charges of N=2 minimal models from ADE singularities."""

    def test_c_A2(self):
        """A_2 (n=3): c = 3*1/3 = 1."""
        assert n2_central_charge(3) == Rational(1)

    def test_c_A3(self):
        """A_3 (n=4): c = 3*2/4 = 3/2."""
        assert n2_central_charge(4) == Rational(3, 2)

    def test_c_A4(self):
        """A_4 (n=5): c = 9/5."""
        assert n2_central_charge(5) == Rational(9, 5)

    def test_c_D4(self):
        """D_4 (h=6): c = 3*4/6 = 2."""
        assert n2_central_charge_D(4) == Rational(2)

    def test_c_D5(self):
        """D_5 (h=8): c = 3*6/8 = 9/4."""
        assert n2_central_charge_D(5) == Rational(9, 4)

    def test_c_E6(self):
        """E_6 (h=12): c = 3*10/12 = 5/2."""
        assert n2_central_charge_E(6) == Rational(5, 2)

    def test_c_E7(self):
        """E_7 (h=18): c = 3*16/18 = 8/3."""
        assert n2_central_charge_E(7) == Rational(8, 3)

    def test_c_E8(self):
        """E_8 (h=30): c = 3*28/30 = 14/5."""
        assert n2_central_charge_E(8) == Rational(14, 5)

    def test_c_unitarity_bound(self):
        """All N=2 MM central charges satisfy 0 < c < 3."""
        for n in range(3, 20):
            c = n2_central_charge(n)
            assert c > 0
            assert c < 3

    def test_c_monotone(self):
        """c = 3(n-2)/n is monotonically increasing in n."""
        for n in range(3, 20):
            c_n = n2_central_charge(n)
            c_n1 = n2_central_charge(n + 1)
            assert c_n1 > c_n

    def test_c_from_singularity_object_A(self):
        """Cross-check: c from ADESingularity matches standalone function."""
        for n in range(2, 10):
            s = make_A(n)
            assert s.n2_central_charge == n2_central_charge(n)

    def test_c_from_singularity_object_D(self):
        """D-type c from object vs function."""
        for n in range(4, 9):
            s = make_D(n)
            assert s.n2_central_charge == n2_central_charge_D(n)

    def test_c_from_singularity_object_E(self):
        """E-type c from object vs function."""
        for n in [6, 7, 8]:
            s = make_E(n)
            assert s.n2_central_charge == n2_central_charge_E(n)


# ============================================================================
# 7. Knorrer periodicity
# ============================================================================

class TestKnorrer:
    """Verify Knorrer periodicity: MF(W + y^2) ~ MF(W)."""

    def test_knorrer_preserves_milnor(self):
        """Knorrer stabilization preserves Milnor number."""
        for s in all_ade_singularities(8):
            s_stab = knorrer_stabilize(s)
            assert s_stab.milnor_number == s.milnor_number

    def test_knorrer_preserves_kappa(self):
        """Knorrer stabilization preserves kappa_{MF}."""
        for s in all_ade_singularities(8):
            s_stab = knorrer_stabilize(s)
            assert s_stab.kappa_mf == s.kappa_mf

    def test_knorrer_preserves_coxeter(self):
        """Knorrer stabilization preserves Coxeter number."""
        s = make_A(3)
        s_stab = knorrer_stabilize(s)
        assert s_stab.coxeter_number == s.coxeter_number

    def test_knorrer_adds_variable(self):
        """Knorrer adds one variable."""
        s = make_A(3)
        s_stab = knorrer_stabilize(s)
        assert s_stab.n_vars == s.n_vars + 1

    def test_knorrer_A2_D4_shadow_match(self):
        """The D_4 singularity x^3 + xy^2 vs stabilized A_2 (x^3 + y^2).

        These are NOT the same: x^3 + xy^2 (D_4, mu=4) vs x^3 + y^2 (A_2 stab, mu=2).
        Knorrer says MF(x^3 + y^2) ~ MF(x^3), but x^3 + xy^2 is NOT x^3 + y^2.
        The cross-term xy^2 is crucial for D-type.

        So kappa_{MF}(A_2 stab) = 1 != kappa_{MF}(D_4) = 2.
        This is correct: Knorrer only applies to W + y^2, not W + xy^2.
        """
        a2_stab = knorrer_stabilize(make_A(3))
        d4 = make_D(4)
        assert a2_stab.kappa_mf == Rational(1)
        assert d4.kappa_mf == Rational(2)
        assert a2_stab.kappa_mf != d4.kappa_mf


# ============================================================================
# 8. Sebastiani-Thom
# ============================================================================

class TestSebastianiThom:
    """Test multiplicativity of Milnor numbers for disjoint sums."""

    def test_product_A2_A2(self):
        """mu(x^3 + y^3) = mu(x^3) * mu(y^3) = 2 * 2 = 4."""
        s1 = make_A(3)
        s2 = make_A(3)
        assert sebastiani_thom(s1, s2) == 4

    def test_product_A2_A3(self):
        """mu(x^3 + y^4) = 2 * 3 = 6.

        Note: this IS the E_6 singularity! x^3 + y^4 has mu=6.
        Cross-check: make_E(6).milnor_number = 6. Consistent.
        """
        s1 = make_A(3)
        s2 = make_A(4)
        mu_product = sebastiani_thom(s1, s2)
        assert mu_product == 6
        assert mu_product == make_E(6).milnor_number

    def test_product_A2_A4(self):
        """mu(x^3 + y^5) = 2 * 4 = 8.

        This IS the E_8 singularity! x^3 + y^5 has mu=8.
        """
        s1 = make_A(3)
        s2 = make_A(5)
        mu_product = sebastiani_thom(s1, s2)
        assert mu_product == 8
        assert mu_product == make_E(8).milnor_number

    def test_stabilization_by_quadratic(self):
        """mu(W + y^2) = mu(W) * mu(y^2) = mu(W) * 1 = mu(W).

        This is the algebraic basis for Knorrer periodicity.
        """
        quad = make_A(2)  # A_1: W = y^2, mu = 1
        assert quad.milnor_number == 1

        for s in all_ade_singularities(8):
            assert sebastiani_thom(s, quad) == s.milnor_number


# ============================================================================
# 9. Gepner model
# ============================================================================

class TestGepner:
    """Test Gepner model computations."""

    def test_quintic_cy_condition(self):
        """The quintic Gepner model satisfies the CY3 condition."""
        g = quintic_gepner()
        assert g.verify_cy_condition()

    def test_quintic_total_c(self):
        """Total c = 5 * 9/5 = 9 = 3*3."""
        g = quintic_gepner()
        assert g.total_central_charge() == Rational(9)

    def test_quintic_milnor_per_factor(self):
        """Each factor of the quintic Gepner has mu = 4."""
        g = quintic_gepner()
        assert g.milnor_per_factor == 4

    def test_quintic_milnor_total(self):
        """Total unorbifolded Milnor = 4^5 = 1024."""
        g = quintic_gepner()
        assert g.milnor_total_unorbifolded == 1024

    def test_quintic_orbifold_order(self):
        """Orbifold group is Z/5Z."""
        g = quintic_gepner()
        assert g.orbifold_order == 5

    def test_quintic_kappa_per_factor(self):
        """kappa_{MF} per factor = 4/2 = 2."""
        g = quintic_gepner()
        assert g.kappa_per_factor == Rational(2)

    def test_quintic_c_per_factor(self):
        """c per factor = 9/5."""
        g = quintic_gepner()
        assert g.central_charge_per_factor() == Rational(9, 5)

    def test_other_gepner_models(self):
        """Verify CY condition for other Gepner models.

        CY3 solutions: r*k = 3(k+2).
        k=1, r=9: 1*9 = 9 = 3*3. Yes.
        k=2, r=6: 2*6 = 12 = 3*4. Yes.
        k=3, r=5: 3*5 = 15 = 3*5. Yes.
        k=6, r=4: 6*4 = 24 = 3*8. Yes.
        """
        models = [
            GepnerModel(level=1, n_factors=9, cy_dim=3),
            GepnerModel(level=2, n_factors=6, cy_dim=3),
            GepnerModel(level=3, n_factors=5, cy_dim=3),
            GepnerModel(level=6, n_factors=4, cy_dim=3),
        ]
        for m in models:
            assert m.verify_cy_condition(), f"CY condition failed for k={m.level}, r={m.n_factors}"

    def test_gepner_total_c_equals_3d(self):
        """For all valid Gepner models, total c = 3d."""
        for (k, r, d) in [(1, 9, 3), (2, 6, 3), (3, 5, 3), (6, 4, 3)]:
            g = GepnerModel(level=k, n_factors=r, cy_dim=d)
            assert g.total_central_charge() == 3 * d


# ============================================================================
# 10. LG/CY correspondence for quintic
# ============================================================================

class TestLGCY:
    """Test the LG/CY correspondence numerical checks."""

    def test_quintic_hodge_data(self):
        """Quintic threefold: h^{1,1}=1, h^{2,1}=101, chi=-200."""
        q = QuinticCYData()
        assert q.h11 == 1
        assert q.h21 == 101
        assert q.euler_char == -200

    def test_quintic_betti(self):
        """Quintic Betti numbers."""
        q = QuinticCYData()
        b = q.betti
        assert b[0] == 1
        assert b[1] == 0
        assert b[2] == 1
        assert b[3] == 204
        assert b[4] == 1
        assert b[5] == 0
        assert b[6] == 1
        # Euler char = sum (-1)^i b_i = 1 - 0 + 1 - 204 + 1 - 0 + 1 = -200
        assert sum((-1)**i * b[i] for i in range(7)) == -200

    def test_lgcy_invariant_jac_dimension(self):
        """LG/CY: dim(Jac_total^{Z/5Z}) = 204 = b_3(quintic)."""
        result = quintic_lgcy_check()
        assert result['dim_invariant_jac'] == 204
        assert result['b3_quintic'] == 204
        assert result['match'] is True

    def test_lgcy_trace_identity(self):
        """Trace of identity (j=0) on Jac_total = 4^5 = 1024."""
        result = quintic_lgcy_check()
        assert abs(result['traces_per_twist'][0] - 1024.0) < 1e-10

    def test_lgcy_trace_generator(self):
        """Trace of omega (j=1) on Jac_total = (-1)^5 = -1."""
        result = quintic_lgcy_check()
        assert abs(result['traces_per_twist'][1] - (-1.0)) < 1e-10


# ============================================================================
# 11. Bar complex
# ============================================================================

class TestBarComplex:
    """Test bar complex dimensions and cohomology."""

    def test_bar_A2_degree0(self):
        """B^0(MF(x^3)) = Jac = C^2."""
        dims = bar_complex_A(3)
        assert dims[0] == 2

    def test_bar_A2_degree1(self):
        """B^1(MF(x^3)) = Jac^{otimes 2} = C^4."""
        dims = bar_complex_A(3)
        assert dims[1] == 4

    def test_bar_A3_degree0(self):
        """B^0(MF(x^4)) = Jac = C^3."""
        dims = bar_complex_A(4)
        assert dims[0] == 3

    def test_bar_cohomology_1dim(self):
        """Bar cohomology of C[x]/(x^m) is 1-dim in each degree."""
        for n in range(2, 8):
            h = bar_cohomology_A(n)
            for p in range(5):
                assert h[p] == 1


# ============================================================================
# 12. Curved A-infinity and degree-kappa relation
# ============================================================================

class TestCurvedAinfty:
    """Test curved A-infinity structure from MF."""

    def test_curvature_string(self):
        """Curvature m_0 = W for MF(W)."""
        result = curved_ainfty_curvature(3)
        assert "x^3" in result

    def test_degree_kappa_A2(self):
        """For W = x^3: deg=3, mu=2, kappa_MF=1, kappa_Vir=1/2."""
        data = degree_to_kappa_relation(3)
        assert data['deg_W'] == 3
        assert data['mu'] == 2
        assert data['kappa_mf'] == Rational(1)
        assert data['kappa_vir'] == Rational(1, 2)

    def test_degree_kappa_A4(self):
        """For W = x^5: deg=5, mu=4, kappa_MF=2, kappa_Vir=9/10."""
        data = degree_to_kappa_relation(5)
        assert data['deg_W'] == 5
        assert data['mu'] == 4
        assert data['kappa_mf'] == Rational(2)
        assert data['kappa_vir'] == Rational(9, 10)

    def test_kappa_not_proportional_to_degree(self):
        """kappa_{MF} = (deg-1)/2, NOT deg/2."""
        for n in range(2, 10):
            data = degree_to_kappa_relation(n)
            assert data['kappa_mf'] == Rational(n - 1, 2)
            assert data['kappa_mf'] != Rational(n, 2)  # NOT deg/2


# ============================================================================
# 13. Hessian and multiplication operators
# ============================================================================

class TestHessianMultiplication:
    """Test Hessian elements and multiplication operators in Jac."""

    def test_hessian_A3_top(self):
        """Hessian of x^4 is 12x^2, represented as [0,0,12] in Jac."""
        h = hessian_element_A(4)
        assert h == [Rational(0), Rational(0), Rational(12)]

    def test_hessian_A2_top(self):
        """Hessian of x^3 is 6x, represented as [0,6] in Jac."""
        h = hessian_element_A(3)
        assert h == [Rational(0), Rational(6)]

    def test_residue_trace_hessian_A3(self):
        """Residue trace of Hessian of x^4: Tr_res(12x^2) = 12/4 = 3 = mu."""
        h = hessian_element_A(4)
        tr = residue_trace_A(4, h)
        assert tr == Rational(3)

    def test_residue_trace_hessian_equals_milnor(self):
        """Tr_res(Hess(x^n)) = n-1 = mu for all n."""
        for n in range(2, 12):
            h = hessian_element_A(n)
            tr = residue_trace_A(n, h)
            assert tr == Rational(n - 1), f"Failed at n={n}"

    def test_multiplication_by_x_A3(self):
        """Multiplication by x in Jac(x^4) = C[x]/(x^3).

        Basis {1, x, x^2}. x*1 = x, x*x = x^2, x*x^2 = x^3 = 0.
        Matrix: [[0,0,0],[1,0,0],[0,1,0]].
        """
        M = multiplication_matrix_A(4, [Rational(0), Rational(1)])
        expected = Matrix([
            [0, 0, 0],
            [1, 0, 0],
            [0, 1, 0],
        ])
        assert M == expected

    def test_multiplication_by_1_A3(self):
        """Multiplication by 1 in Jac(x^4) is the identity."""
        M = multiplication_matrix_A(4, [Rational(1)])
        expected = Matrix([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ])
        assert M == expected

    def test_algebra_trace_constant(self):
        """Algebra trace of constant a_0: Tr(M_{a_0}) = mu * a_0."""
        for n in range(2, 8):
            mu = n - 1
            tr = multiplication_trace_A(n, [Rational(5)])
            assert tr == Rational(5 * mu)


# ============================================================================
# 14. Summary table and cross-checks
# ============================================================================

class TestSummary:
    """Cross-consistency checks on the full ADE shadow summary."""

    def test_summary_has_all_types(self):
        """Summary table includes all 16 ADE types up to rank 8."""
        rows = ade_shadow_summary()
        assert len(rows) == 16

    def test_summary_kappa_mf_positive(self):
        """All kappa_{MF} values are positive."""
        for r in ade_shadow_summary():
            assert r['kappa_MF'] > 0

    def test_summary_c_in_range(self):
        """All N=2 central charges satisfy 0 <= c < 3.

        A_1 (n=2) has c = 0 (the trivial N=2 theory). All others have c > 0.
        """
        for r in ade_shadow_summary():
            assert r['c_N2'] >= 0
            assert r['c_N2'] < 3

    def test_E6_is_A2_tensor_A3(self):
        """E_6 = x^3 + y^4: mu(E_6) = mu(A_2)*mu(A_3) by Sebastiani-Thom.

        mu(x^3) = 2, mu(y^4) = 3. Product = 6 = mu(E_6). Consistent.
        """
        a2 = make_A(3)  # A_2
        a3 = make_A(4)  # A_3
        e6 = make_E(6)
        assert sebastiani_thom(a2, a3) == e6.milnor_number

    def test_E8_is_A2_tensor_A4(self):
        """E_8 = x^3 + y^5: mu(E_8) = mu(A_2)*mu(A_4)."""
        a2 = make_A(3)
        a4 = make_A(5)
        e8 = make_E(8)
        assert sebastiani_thom(a2, a4) == e8.milnor_number

    def test_kappa_mf_additive_under_product(self):
        """For product singularity f+g:
        kappa_{MF}(f+g) = mu(f)*mu(g)/2 = kappa_{MF}(f)*mu(g) + ...

        Actually kappa_{MF} = mu/2, and mu is MULTIPLICATIVE (Sebastiani-Thom),
        so kappa_{MF}(f+g) = mu(f)*mu(g)/2.
        This is NOT additive in general: mu(f)*mu(g)/2 != mu(f)/2 + mu(g)/2.
        It IS multiplicative up to a factor: kappa(f+g) = 2*kappa(f)*kappa(g).
        """
        a2 = make_A(3)  # mu=2, kappa=1
        a3 = make_A(4)  # mu=3, kappa=3/2
        mu_prod = sebastiani_thom(a2, a3)
        kappa_prod = Rational(mu_prod, 2)
        assert kappa_prod == Rational(3)
        # Cross-check: 2 * kappa(A2) * kappa(A3) = 2 * 1 * 3/2 = 3. Yes.
        assert kappa_prod == 2 * a2.kappa_mf * a3.kappa_mf

    def test_dual_coxeter_equals_coxeter_simply_laced(self):
        """For all ADE (simply-laced), h^v = h."""
        for s in all_ade_singularities(8):
            assert s.dual_coxeter == s.coxeter_number
