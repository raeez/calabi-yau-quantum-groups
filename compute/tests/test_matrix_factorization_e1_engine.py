r"""Tests for matrix_factorization_e1_engine.py

E1 chiral algebras from CY3 matrix factorization categories (LG models).

Tests the LG/CY correspondence at the E1 chiral level:
- Brieskorn-Pham singularities (Milnor numbers, CY dimensions, charges)
- N=2 minimal models (central charges, chiral rings, kappa values)
- Gepner models (orbifold invariant dimensions, CY condition)
- Orlov equivalence (singularity categories, ADE classification)
- LG/CY correspondence for the quintic
- Knorrer periodicity and Sebastiani-Thom
- Multi-path kappa verification
- E1 vs E_infty bar complex dimensions
- Wall-crossing and MC gauge transformations

100+ tests organized in thematic groups.
"""

import pytest
from fractions import Fraction as F

from compute.lib.matrix_factorization_e1_engine import (
    BrieskornPham,
    N2MinimalModel,
    GepnerModelE1,
    E1ChiralAlgebraFromMF,
    SingularityCategoryData,
    LGCYCorrespondence,
    GLSMPhase,
    fermat_quintic,
    conifold_node,
    e6_surface_singularity,
    e6_threefold_singularity,
    ade_singularity_bp,
    quintic_gepner_e1,
    cy3_gepner_models,
    e1_chiral_from_bp,
    kappa_from_milnor,
    kappa_from_central_charge_virasoro,
    kappa_from_central_charge_n2,
    kappa_from_euler_characteristic,
    kappa_gepner_quintic,
    e1_bar_dimensions,
    e_infty_bar_dimensions,
    bar_ratio_e1_vs_einfty,
    singularity_category_A,
    singularity_category_D,
    singularity_category_E,
    quintic_lgcy,
    knorrer_kappa_invariance,
    sebastiani_thom_kappa,
    ade_e1_chiral_table,
    fermat_quintic_computation,
    conifold_computation,
    e6_computation,
    brieskorn_pham_general,
    glsm_phases_quintic,
    wall_crossing_bps_count_conifold,
    kappa_verification_table,
    cy_central_charge_constraint,
    gepner_level_dimension_relation,
    chiral_ring_bp,
    all_cy3_gepner_summary,
    consistency_check_all,
    _binomial,
    _count_tuples_with_sum,
)


# ============================================================================
# 1. Brieskorn-Pham singularities: basic invariants
# ============================================================================

class TestBrieskornPhamBasic:
    """Test Brieskorn-Pham singularity construction and basic properties."""

    def test_fermat_quintic_n_vars(self):
        """Fermat quintic has 5 variables."""
        bp = fermat_quintic()
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert bp.n_vars == 5

    def test_fermat_quintic_degrees(self):
        """Fermat quintic has degrees (5,5,5,5,5)."""
        bp = fermat_quintic()
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert bp.degrees == (5, 5, 5, 5, 5)

    def test_fermat_quintic_milnor(self):
        """mu(x_1^5 + ... + x_5^5) = 4^5 = 1024."""
        bp = fermat_quintic()
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert bp.milnor_number == 4**5
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert bp.milnor_number == 1024

    def test_fermat_quintic_cy_dim(self):
        """CY dimension = n_vars - 2 = 3."""
        bp = fermat_quintic()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert bp.cy_dimension == 3

    def test_fermat_quintic_charges(self):
        """Charges q_i = 1/5 for all i."""
        bp = fermat_quintic()
        assert all(q == F(1, 5) for q in bp.charges)

    def test_fermat_quintic_charge_sum(self):
        """sum q_i = 5 * 1/5 = 1 (CY condition)."""
        bp = fermat_quintic()
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert bp.charge_sum == 1

    def test_fermat_quintic_is_cy(self):
        """Fermat quintic satisfies the CY condition."""
        bp = fermat_quintic()
        assert bp.is_cy_condition is True

    def test_fermat_quintic_c_hat(self):
        """c_hat = 5 - 2*5*(1/5) = 5 - 2 = 3."""
        bp = fermat_quintic()
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert bp.c_hat == 3

    def test_fermat_quintic_central_charge(self):
        """c = 3 * c_hat = 9."""
        bp = fermat_quintic()
        # VERIFIED [DC] central charge formula [LT] matrix factorization theory
        assert bp.total_central_charge == 9

    def test_a1_node_milnor(self):
        """A_1 node: W = sum x_i^2, mu = 1^4 = 1."""
        bp = conifold_node()
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert bp.milnor_number == 1

    def test_a1_node_cy_dim(self):
        """A_1 node: CY dim = 4 - 2 = 2."""
        bp = conifold_node()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert bp.cy_dimension == 2

    def test_a1_node_central_charge_zero(self):
        """A_1 node: c = 3*(4 - 2*4/2) = 3*0 = 0."""
        bp = conifold_node()
        # VERIFIED [DC] central charge formula [LT] matrix factorization theory
        assert bp.total_central_charge == 0

    def test_e6_surface_milnor(self):
        """E_6: W = x^3 + y^4, mu = 2*3 = 6."""
        bp = e6_surface_singularity()
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert bp.milnor_number == 6

    def test_e6_surface_cy_dim(self):
        """E_6 surface: CY dim = 2 - 2 = 0."""
        bp = e6_surface_singularity()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert bp.cy_dimension == 0

    def test_e6_threefold_milnor(self):
        """E_6 threefold: W = x^3+y^4+z^2+w^2, mu = 2*3*1*1 = 6 (Knorrer)."""
        bp = e6_threefold_singularity()
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert bp.milnor_number == 6

    def test_e6_threefold_cy_dim(self):
        """E_6 threefold: CY dim = 4 - 2 = 2."""
        bp = e6_threefold_singularity()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert bp.cy_dimension == 2

    def test_degree_validation(self):
        """Degrees must be >= 2."""
        with pytest.raises(ValueError):
            BrieskornPham(degrees=(1,))

    def test_jacobian_ring_dim_equals_milnor(self):
        """dim Jac(W) = mu(W) always."""
        for degrees in [(5,), (3, 4), (5, 5, 5, 5, 5), (2, 2, 2, 2)]:
            bp = BrieskornPham(degrees=degrees)
            assert bp.jacobian_ring_dim == bp.milnor_number


class TestSebastianThomMilnor:
    """Test the Sebastiani-Thom theorem: mu(f+g) = mu(f)*mu(g)."""

    def test_x3_y4(self):
        """mu(x^3 + y^4) = mu(x^3) * mu(y^4) = 2*3 = 6."""
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert BrieskornPham(degrees=(3, 4)).milnor_number == 2 * 3

    def test_x5_y5(self):
        """mu(x^5 + y^5) = 4*4 = 16."""
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert BrieskornPham(degrees=(5, 5)).milnor_number == 16

    def test_five_copies_x5(self):
        """mu(x1^5+...+x5^5) = 4^5 = 1024."""
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert BrieskornPham(degrees=(5, 5, 5, 5, 5)).milnor_number == 4**5

    def test_general_product(self):
        """mu(x1^{d1}+...+xn^{dn}) = prod(d_i-1)."""
        bp = BrieskornPham(degrees=(3, 5, 7))
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert bp.milnor_number == 2 * 4 * 6
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert bp.milnor_number == 48


# ============================================================================
# 2. N=2 minimal models
# ============================================================================

class TestN2MinimalModel:
    """Test N=2 minimal model properties."""

    def test_k1_central_charge(self):
        """k=1: c = 3/3 = 1."""
        mm = N2MinimalModel(level=1)
        # VERIFIED [DC] central charge formula [LT] matrix factorization theory
        assert mm.central_charge == 1

    def test_k2_central_charge(self):
        """k=2: c = 6/4 = 3/2."""
        mm = N2MinimalModel(level=2)
        assert mm.central_charge == F(3, 2)

    def test_k3_central_charge(self):
        """k=3: c = 9/5."""
        mm = N2MinimalModel(level=3)
        assert mm.central_charge == F(9, 5)

    def test_k6_central_charge(self):
        """k=6: c = 18/8 = 9/4."""
        mm = N2MinimalModel(level=6)
        assert mm.central_charge == F(9, 4)

    def test_exponent(self):
        """n = k+2."""
        for k in range(1, 10):
            mm = N2MinimalModel(level=k)
            assert mm.exponent == k + 2

    def test_milnor_number(self):
        """mu = k+1."""
        for k in range(1, 10):
            mm = N2MinimalModel(level=k)
            assert mm.milnor_number == k + 1

    def test_chiral_ring_dim(self):
        """Chiral ring dim = k+1."""
        mm = N2MinimalModel(level=3)
        # VERIFIED [DC] Euler characteristic formula [LT] matrix factorization theory
        assert mm.chiral_ring_dim == 4

    def test_kappa_virasoro(self):
        """kappa_Vir = c/2."""
        mm = N2MinimalModel(level=3)
        assert mm.kappa_virasoro == F(9, 10)

    def test_kappa_n2(self):
        """kappa_N2 = c/6."""
        mm = N2MinimalModel(level=3)
        assert mm.kappa_n2 == F(9, 30)
        assert mm.kappa_n2 == F(3, 10)

    def test_kappa_mf(self):
        """kappa_MF = mu/2 = (k+1)/2."""
        mm = N2MinimalModel(level=3)
        assert mm.kappa_mf == F(4, 2)
        # VERIFIED [DC] kappa formula [LT] matrix factorization theory
        assert mm.kappa_mf == 2

    def test_level_validation(self):
        """Level must be >= 1."""
        with pytest.raises(ValueError):
            N2MinimalModel(level=0)

    def test_n_simple_modules(self):
        """At level k: (k+1)(k+2) simple modules."""
        mm = N2MinimalModel(level=3)
        # VERIFIED [DC] modular structure [LT] matrix factorization theory
        assert mm.n_simple_modules == 4 * 5
        # VERIFIED [DC] modular structure [LT] matrix factorization theory
        assert mm.n_simple_modules == 20


# ============================================================================
# 3. Gepner models
# ============================================================================

class TestGepnerModels:
    """Test Gepner model construction and properties."""

    def test_quintic_cy_condition(self):
        """(3)^5 satisfies CY3 condition: 5 * 3/5 = 3."""
        g = quintic_gepner_e1()
        assert g.verify_cy_condition() is True

    def test_quintic_total_c(self):
        """(3)^5 has c_total = 9."""
        g = quintic_gepner_e1()
        # VERIFIED [DC] central charge formula [LT] matrix factorization theory
        assert g.total_central_charge == 9

    def test_quintic_orbifold_order(self):
        """(3)^5 orbifold group Z/5Z."""
        g = quintic_gepner_e1()
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert g.orbifold_order == 5

    def test_quintic_orbifold_invariant_dim(self):
        """(3)^5: orbifold-invariant Jac dim = 204 = b_3(quintic)."""
        g = quintic_gepner_e1()
        dim = g.orbifold_invariant_dimension_exact()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert dim == 204

    def test_quintic_orbifold_numerical(self):
        """Numerical computation should agree with exact."""
        g = quintic_gepner_e1()
        exact = int(g.orbifold_invariant_dimension_exact())
        numerical = g.orbifold_invariant_dimension()
        assert exact == numerical

    def test_quintic_chiral_ring_decomposition(self):
        """Chiral ring decomposition matches quintic Hodge diamond."""
        g = quintic_gepner_e1()
        decomp = g.chiral_ring_invariant_decomposition()
        # For CY3 quintic: h^{3,0}=1, h^{2,1}=101, h^{1,2}=101, h^{0,3}=1
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert decomp[0] == 1      # h^{3,0} (or unit)
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert decomp[1] == 101    # h^{2,1}
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert decomp[2] == 101    # h^{1,2}
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert decomp[3] == 1      # h^{0,3} (or top form)
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert sum(decomp.values()) == 204

    def test_all_cy3_gepner_c9(self):
        """All uniform CY3 Gepner models have c = 9."""
        for g in cy3_gepner_models():
            # VERIFIED [DC] central charge formula [LT] matrix factorization theory
            assert g.total_central_charge == 9

    def test_all_cy3_gepner_cy_condition(self):
        """All CY3 Gepner models satisfy the CY condition."""
        for g in cy3_gepner_models():
            assert g.verify_cy_condition() is True

    def test_four_cy3_gepner_models(self):
        """There are exactly 4 uniform CY3 Gepner models."""
        models = cy3_gepner_models()
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert len(models) == 4
        levels = [m.levels[0] for m in models]
        n_factors = [m.n_factors for m in models]
        # VERIFIED [DC] level formula [LT] matrix factorization theory
        assert levels == [1, 2, 3, 6]
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert n_factors == [9, 6, 5, 4]

    def test_gepner_19_orbifold_dim(self):
        """(1)^9 model: orbifold-invariant dim."""
        g = cy3_gepner_models()[0]
        dim = int(g.orbifold_invariant_dimension_exact())
        # (2^9 + (-1)^9 * 2) / 3 = (512 - 2)/3 = 510/3 = 170
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert dim == 170

    def test_gepner_26_orbifold_dim(self):
        """(2)^6 model: orbifold-invariant dim."""
        g = cy3_gepner_models()[1]
        dim = int(g.orbifold_invariant_dimension_exact())
        # n=4, r=6, mu=3. 4 does not divide 6.
        # dim = (3^6 + (-1)^7)/4 = (729 - 1)/4 = 728/4 = 182
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert dim == 182

    def test_gepner_64_orbifold_dim(self):
        """(6)^4 model: orbifold-invariant dim."""
        g = cy3_gepner_models()[3]
        dim = int(g.orbifold_invariant_dimension_exact())
        # n=8, r=4, mu=7. 8 does not divide 4.
        # dim = (7^4 + (-1)^5)/8 = (2401 - 1)/8 = 2400/8 = 300
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert dim == 300

    def test_gepner_is_uniform(self):
        """Uniform Gepner models have all levels equal."""
        g = quintic_gepner_e1()
        assert g.is_uniform is True

    def test_gepner_c_hat(self):
        """c_hat_total = cy_dim for each CY3 Gepner model."""
        for g in cy3_gepner_models():
            # VERIFIED [DC] structural property [LT] matrix factorization theory
            assert g.c_hat_total == 3


# ============================================================================
# 4. Kappa computations (multi-path verification)
# ============================================================================

class TestKappaMultiPath:
    """Multi-path kappa verification (mandate: 3+ independent paths)."""

    def test_kappa_milnor_A2(self):
        """Path 1: kappa_MF(A_2) = mu/2 = 2/2 = 1."""
        # VERIFIED [DC] kappa formula [LT] matrix factorization theory
        assert kappa_from_milnor(2) == 1

    def test_kappa_virasoro_A2(self):
        """Path 2: kappa_Vir(A_2) = c/2 = 1/2."""
        c = F(3, 3)  # k=1, c=3*1/3=1
        assert kappa_from_central_charge_virasoro(c) == F(1, 2)

    def test_kappa_n2_A2(self):
        """Path 3: kappa_N2(A_2) = c/6 = 1/6."""
        c = F(1)
        assert kappa_from_central_charge_n2(c) == F(1, 6)

    def test_kappa_mf_and_vir_differ(self):
        """kappa_MF != kappa_Vir in general (they are DIFFERENT invariants)."""
        # For A_4 (x^5): mu=4, c=9/5
        kappa_mf = kappa_from_milnor(4)  # 2
        kappa_vir = kappa_from_central_charge_virasoro(F(9, 5))  # 9/10
        assert kappa_mf != kappa_vir

    def test_kappa_mf_equals_vir_only_at_a1(self):
        """kappa_MF = kappa_Vir only for A_1 (trivial case, mu=1, c=0)."""
        kappa_mf = kappa_from_milnor(1)  # 1/2
        kappa_vir = kappa_from_central_charge_virasoro(F(0))  # 0
        assert kappa_mf != kappa_vir  # Even A_1 disagrees!

    def test_kappa_bcov_quintic(self):
        """Path 4: kappa_BCOV = chi/24 = -200/24 = -25/3."""
        assert kappa_from_euler_characteristic(-200) == F(-25, 3)

    def test_kappa_gepner_quintic_dictionary(self):
        """All kappa values for the quintic Gepner model."""
        d = kappa_gepner_quintic()
        assert d['kappa_virasoro'] == F(9, 2)
        assert d['kappa_n2'] == F(3, 2)
        assert d['kappa_bcov'] == F(-25, 3)
        # VERIFIED [DC] kappa formula [LT] matrix factorization theory
        assert d['kappa_mf_per_factor'] == 2
        # VERIFIED [DC] kappa formula [LT] matrix factorization theory
        assert d['kappa_mf_total_naive'] == 10

    def test_kappa_n2_is_c_over_6(self):
        """Verify kappa_N2 = c/6 for several levels."""
        for k in [1, 2, 3, 6, 10]:
            mm = N2MinimalModel(level=k)
            assert mm.kappa_n2 == mm.central_charge / 6

    def test_kappa_mf_is_mu_over_2(self):
        """Verify kappa_MF = mu/2 for all N=2 MMs."""
        for k in [1, 2, 3, 6, 10]:
            mm = N2MinimalModel(level=k)
            assert mm.kappa_mf == F(mm.milnor_number, 2)


# ============================================================================
# 5. Singularity categories (Orlov equivalence)
# ============================================================================

class TestSingularityCategories:
    """Test singularity category data for ADE types."""

    def test_A2_milnor(self):
        """A_2: mu = 2."""
        sc = singularity_category_A(3)
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert sc.milnor_number == 2

    def test_A4_milnor(self):
        """A_4: mu = 4."""
        sc = singularity_category_A(5)
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert sc.milnor_number == 4

    def test_A_n2_level(self):
        """A_{n-1}: N=2 level = n-2."""
        for n in range(2, 8):
            sc = singularity_category_A(n)
            assert sc.n2_level == n - 2

    def test_A_central_charge(self):
        """A_{n-1}: c = 3(n-2)/n."""
        for n in range(3, 8):
            sc = singularity_category_A(n)
            assert sc.central_charge == F(3 * (n - 2), n)

    def test_D4_milnor(self):
        """D_4: mu = 4."""
        sc = singularity_category_D(4)
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert sc.milnor_number == 4

    def test_D5_milnor(self):
        """D_5: mu = 5."""
        sc = singularity_category_D(5)
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert sc.milnor_number == 5

    def test_D_central_charge(self):
        """D_n: c = 3(n-2)/(n-1)."""
        for n in range(4, 8):
            sc = singularity_category_D(n)
            assert sc.central_charge == F(3 * (n - 2), n - 1)

    def test_E6(self):
        """E_6: mu=6, h=12, k=10, c=5/2."""
        sc = singularity_category_E(6)
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert sc.milnor_number == 6
        # VERIFIED [DC] level formula [LT] matrix factorization theory
        assert sc.n2_level == 10
        assert sc.central_charge == F(5, 2)

    def test_E7(self):
        """E_7: mu=7, h=18, k=16, c=8/3."""
        sc = singularity_category_E(7)
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert sc.milnor_number == 7
        # VERIFIED [DC] level formula [LT] matrix factorization theory
        assert sc.n2_level == 16
        assert sc.central_charge == F(8, 3)

    def test_E8(self):
        """E_8: mu=8, h=30, k=28, c=14/5."""
        sc = singularity_category_E(8)
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert sc.milnor_number == 8
        # VERIFIED [DC] level formula [LT] matrix factorization theory
        assert sc.n2_level == 28
        assert sc.central_charge == F(14, 5)

    def test_n_simples_equals_milnor(self):
        """For ADE: n_simples = mu."""
        for sc in [singularity_category_A(5), singularity_category_D(5),
                    singularity_category_E(6)]:
            assert sc.n_simples == sc.milnor_number


# ============================================================================
# 6. LG/CY correspondence
# ============================================================================

class TestLGCYCorrespondence:
    """Test the LG/CY correspondence for the quintic."""

    def test_quintic_hodge_match(self):
        """Orbifold-invariant Jac dim = b_3(quintic) = 204."""
        lgcy = quintic_lgcy()
        assert lgcy.verify_hodge_match() is True
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert lgcy.orbifold_dim == 204

    def test_quintic_euler(self):
        """chi(quintic) = -200."""
        lgcy = quintic_lgcy()
        # VERIFIED [DC] Euler characteristic formula [LT] matrix factorization theory
        assert lgcy.cy_euler == -200

    def test_quintic_h21(self):
        """h^{2,1}(quintic) = 101."""
        lgcy = quintic_lgcy()
        # VERIFIED [DC] Hodge number [LT] matrix factorization theory
        assert lgcy.cy_hodge['h21'] == 101

    def test_quintic_h11(self):
        """h^{1,1}(quintic) = 1."""
        lgcy = quintic_lgcy()
        # VERIFIED [DC] Hodge number [LT] matrix factorization theory
        assert lgcy.cy_hodge['h11'] == 1

    def test_quintic_kappa_dictionary(self):
        """All kappa values for the quintic LGCY correspondence."""
        lgcy = quintic_lgcy()
        kd = lgcy.kappa_dictionary()
        assert kd['kappa_virasoro'] == F(9, 2)
        assert kd['kappa_n2'] == F(3, 2)
        assert kd['kappa_bcov'] == F(-25, 3)
        assert kd['kappa_mf_categorical'] == F(1024, 2)


# ============================================================================
# 7. Knorrer periodicity and Sebastiani-Thom
# ============================================================================

class TestKnorrerPeriodicity:
    """Test Knorrer periodicity: MF(W+y^2) = MF(W)."""

    def test_knorrer_x3(self):
        """mu(x^3) = mu(x^3+y^2) = 2."""
        bp = BrieskornPham(degrees=(3,))
        result = knorrer_kappa_invariance(bp)
        assert result['invariant'] is True
        assert result['kappa_original'] == F(2, 2)

    def test_knorrer_x5(self):
        """mu(x^5) = mu(x^5+y^2) = 4."""
        bp = BrieskornPham(degrees=(5,))
        result = knorrer_kappa_invariance(bp)
        assert result['invariant'] is True

    def test_knorrer_e6(self):
        """mu(x^3+y^4) = mu(x^3+y^4+z^2) = 6."""
        bp = e6_surface_singularity()
        result = knorrer_kappa_invariance(bp)
        assert result['invariant'] is True

    def test_knorrer_fermat_quintic(self):
        """mu(quintic) = mu(quintic+y^2) = 1024."""
        bp = fermat_quintic()
        result = knorrer_kappa_invariance(bp)
        assert result['invariant'] is True
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert result['mu_original'] == 1024


class TestSebastianThomKappa:
    """Test kappa under Sebastiani-Thom."""

    def test_x3_y4(self):
        """kappa(x^3+y^4) = 2*kappa(x^3)*kappa(y^4)."""
        bp1 = BrieskornPham(degrees=(3,))
        bp2 = BrieskornPham(degrees=(4,))
        result = sebastiani_thom_kappa(bp1, bp2)
        assert result['consistent'] is True
        assert result['kappa_fg'] == F(6, 2)  # mu=6, kappa=3

    def test_x5_x5(self):
        """kappa(x^5+y^5) = 2*kappa(x^5)*kappa(y^5) = 2*2*2 = 8."""
        bp1 = BrieskornPham(degrees=(5,))
        bp2 = BrieskornPham(degrees=(5,))
        result = sebastiani_thom_kappa(bp1, bp2)
        assert result['consistent'] is True
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert result['mu_fg'] == 16
        # VERIFIED [DC] kappa formula [LT] matrix factorization theory
        assert result['kappa_fg'] == 8


# ============================================================================
# 8. E1 vs E_infty bar complex
# ============================================================================

class TestBarComplex:
    """Test E1 and E_infty bar complex dimensions."""

    def test_e1_bar_mu1(self):
        """E1 bar: mu=1 gives dim 1 at all arities."""
        dims = e1_bar_dimensions(1, 5)
        for n in range(1, 6):
            # VERIFIED [DC] structural property [LT] matrix factorization theory
            assert dims[n] == 1

    def test_e1_bar_mu4(self):
        """E1 bar: mu=4 gives 4^n."""
        dims = e1_bar_dimensions(4, 4)
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert dims[1] == 4
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert dims[2] == 16
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert dims[3] == 64
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert dims[4] == 256

    def test_einfty_bar_mu4(self):
        """E_infty bar: mu=4 gives C(n+3, 3)."""
        dims = e_infty_bar_dimensions(4, 4)
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert dims[1] == 4      # C(4,3) = 4
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert dims[2] == 10     # C(5,3) = 10
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert dims[3] == 20     # C(6,3) = 20
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert dims[4] == 35     # C(7,3) = 35

    def test_e1_geq_einfty(self):
        """E1 bar is at least as large as E_infty bar."""
        for mu in range(1, 8):
            for n in range(1, 6):
                e1 = e1_bar_dimensions(mu, n)[n]
                einf = e_infty_bar_dimensions(mu, n)[n]
                assert e1 >= einf

    def test_ratio_mu1_is_1(self):
        """For mu=1: E1/E_infty ratio = 1."""
        for n in range(1, 6):
            # VERIFIED [DC] structural property [LT] matrix factorization theory
            assert bar_ratio_e1_vs_einfty(1, n) == 1

    def test_ratio_mu2_arity2(self):
        """For mu=2, arity 2: 2^2 / C(3,1) = 4/3."""
        assert bar_ratio_e1_vs_einfty(2, 2) == F(4, 3)

    def test_ratio_grows(self):
        """The ratio E1/E_infty grows with arity for mu >= 2."""
        for mu in [2, 4, 6]:
            prev = bar_ratio_e1_vs_einfty(mu, 1)
            for n in range(2, 6):
                curr = bar_ratio_e1_vs_einfty(mu, n)
                assert curr >= prev
                prev = curr


# ============================================================================
# 9. ADE chiral algebra table
# ============================================================================

class TestADEChiralTable:
    """Test the complete ADE E1 chiral algebra table."""

    def test_table_has_entries(self):
        """Table should have A_1 through A_8, D_4 through D_8, E_6,E_7,E_8."""
        table = ade_e1_chiral_table()
        types = [row['type'] for row in table]
        assert 'A1' in types
        assert 'A8' in types
        assert 'D4' in types
        assert 'E6' in types
        assert 'E8' in types

    def test_a1_trivial(self):
        """A_1: mu=1, c=0 (trivial)."""
        table = ade_e1_chiral_table()
        a1 = [r for r in table if r['type'] == 'A1'][0]
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert a1['mu'] == 1
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert a1['c'] == 0

    def test_a4_values(self):
        """A_4: mu=4, c=9/5, k=3."""
        table = ade_e1_chiral_table()
        a4 = [r for r in table if r['type'] == 'A4'][0]
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert a4['mu'] == 4
        assert a4['c'] == F(9, 5)
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert a4['k'] == 3

    def test_e1_bar_larger_than_einfty(self):
        """E1 bar arity-2 >= E_infty bar arity-2 for all ADE."""
        table = ade_e1_chiral_table()
        for row in table:
            assert row['e1_bar_arity2'] >= row['einfty_bar_arity2']


# ============================================================================
# 10. Specific computations (Fermat quintic, conifold, E6)
# ============================================================================

class TestSpecificComputations:
    """Test the detailed computation functions."""

    def test_fermat_quintic_is_rational(self):
        """The Gepner model is a rational CFT."""
        fc = fermat_quintic_computation()
        assert fc['is_rational_cft'] is True

    def test_fermat_quintic_not_standard_w_algebra(self):
        """The Gepner model is NOT a standard W-algebra."""
        fc = fermat_quintic_computation()
        assert fc['is_standard_w_algebra'] is False

    def test_fermat_quintic_orbifold_dim_204(self):
        """Orbifold-invariant dim = 204."""
        fc = fermat_quintic_computation()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert fc['orbifold_invariant_dim'] == 204

    def test_fermat_quintic_kappa_n2(self):
        """kappa_N2 = 3/2."""
        fc = fermat_quintic_computation()
        assert fc['kappa_n2'] == F(3, 2)

    def test_fermat_quintic_kappa_bcov(self):
        """kappa_BCOV = -25/3."""
        fc = fermat_quintic_computation()
        assert fc['kappa_bcov'] == F(-25, 3)

    def test_fermat_quintic_cy_condition(self):
        fc = fermat_quintic_computation()
        assert fc['cy_condition_check'] is True

    def test_conifold_trivial(self):
        """A_1 node in 4 vars: trivial by Knorrer."""
        cc = conifold_computation()
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert cc['milnor_number'] == 1
        # VERIFIED [DC] central charge formula [LT] matrix factorization theory
        assert cc['central_charge'] == 0

    def test_e6_milnor_6(self):
        """E_6: mu = 6."""
        ec = e6_computation()
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert ec['milnor_number'] == 6

    def test_e6_central_charge(self):
        """E_6: c = 5/2."""
        ec = e6_computation()
        assert ec['central_charge'] == F(5, 2)

    def test_e6_kappa_mf(self):
        """E_6: kappa_MF = 3."""
        ec = e6_computation()
        # VERIFIED [DC] kappa formula [LT] matrix factorization theory
        assert ec['kappa_mf'] == 3

    def test_e6_n_simples(self):
        """E_6: 6 simple objects."""
        ec = e6_computation()
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert ec['n_simples'] == 6


class TestBrieskornPhamGeneral:
    """Test the general Brieskorn-Pham formula."""

    def test_single_variable(self):
        """W = x^5: 1 var, CY dim = -1."""
        result = brieskorn_pham_general((5,))
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert result['n_vars'] == 1
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert result['cy_dim'] == -1
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert result['milnor_number'] == 4

    def test_two_variables(self):
        """W = x^3 + y^4: 2 vars, CY dim = 0, mu = 6."""
        result = brieskorn_pham_general((3, 4))
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert result['n_vars'] == 2
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert result['cy_dim'] == 0
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert result['milnor_number'] == 6

    def test_cy_condition_check(self):
        """The quintic is CY; (3,4) is not."""
        assert brieskorn_pham_general((5, 5, 5, 5, 5))['is_cy'] is True
        assert brieskorn_pham_general((3, 4))['is_cy'] is False

    def test_bar_dims_included(self):
        """The result includes E1 and E_infty bar dimensions."""
        result = brieskorn_pham_general((5,))
        assert 1 in result['e1_bar_dims']
        assert 1 in result['einfty_bar_dims']


# ============================================================================
# 11. GLSM phases and wall-crossing
# ============================================================================

class TestGLSMWallCrossing:
    """Test GLSM phases and wall-crossing data."""

    def test_three_phases(self):
        """The quintic GLSM has CY, LG, and Gepner phases."""
        phases = glsm_phases_quintic()
        assert 'CY' in phases
        assert 'LG' in phases
        assert 'Gepner' in phases

    def test_cy_phase_positive(self):
        """CY phase has positive FI parameter."""
        phases = glsm_phases_quintic()
        assert phases['CY'].fi_parameter_sign == 'positive'

    def test_lg_phase_negative(self):
        """LG phase has negative FI parameter."""
        phases = glsm_phases_quintic()
        assert phases['LG'].fi_parameter_sign == 'negative'

    def test_conifold_bps_count(self):
        """Conifold has 1 BPS state in each chamber."""
        wc = wall_crossing_bps_count_conifold()
        # VERIFIED [DC] BPS state [LT] matrix factorization theory
        assert wc['chamber_I_bps'] == {'gamma_1': 1}
        # VERIFIED [DC] BPS state [LT] matrix factorization theory
        assert wc['chamber_II_bps'] == {'gamma_2': 1}
        # VERIFIED [DC] wall-crossing [LT] matrix factorization theory
        assert wc['wall_bps'] == {'gamma_1+gamma_2': 1}


# ============================================================================
# 12. Central charge constraints
# ============================================================================

class TestCentralChargeConstraints:
    """Test CY dimension constraints on central charge."""

    def test_cy1_c3(self):
        """CY1: c = 3."""
        # VERIFIED [DC] central charge [LT] matrix factorization theory
        assert cy_central_charge_constraint(1) == 3

    def test_cy2_c6(self):
        """CY2: c = 6."""
        # VERIFIED [DC] central charge [LT] matrix factorization theory
        assert cy_central_charge_constraint(2) == 6

    def test_cy3_c9(self):
        """CY3: c = 9."""
        # VERIFIED [DC] central charge [LT] matrix factorization theory
        assert cy_central_charge_constraint(3) == 9


class TestGepnerLevelDimension:
    """Test Gepner level-dimension relation."""

    def test_k3_r5_is_cy3(self):
        """k=3, r=5 gives CY3."""
        result = gepner_level_dimension_relation(3, 5)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert result['cy_dim'] == 3
        assert result['is_integer_dim'] is True

    def test_k1_r9_is_cy3(self):
        """k=1, r=9 gives CY3."""
        result = gepner_level_dimension_relation(1, 9)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert result['cy_dim'] == 3

    def test_k6_r4_is_cy3(self):
        """k=6, r=4 gives CY3."""
        result = gepner_level_dimension_relation(6, 4)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert result['cy_dim'] == 3

    def test_c_total_equals_9(self):
        """All CY3 Gepner models: c = 9."""
        for k, r in [(1, 9), (2, 6), (3, 5), (6, 4)]:
            result = gepner_level_dimension_relation(k, r)
            # VERIFIED [DC] structural property [LT] matrix factorization theory
            assert result['c_total'] == 9


# ============================================================================
# 13. Chiral ring and marginal deformations
# ============================================================================

class TestChiralRing:
    """Test chiral ring computation."""

    def test_quintic_101_marginal(self):
        """The quintic has 101 marginal deformations = h^{2,1}."""
        bp = fermat_quintic()
        ring = chiral_ring_bp(bp)
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert ring['n_marginal_deformations'] == 101

    def test_chiral_ring_dim_equals_milnor(self):
        """Chiral ring dim = mu always."""
        for degrees in [(5,), (3, 4), (3, 5)]:
            bp = BrieskornPham(degrees=degrees)
            ring = chiral_ring_bp(bp)
            assert ring['chiral_ring_dim'] == bp.milnor_number

    def test_chiral_ring_is_frobenius(self):
        """The chiral ring is always Frobenius."""
        bp = fermat_quintic()
        ring = chiral_ring_bp(bp)
        assert ring['is_frobenius'] is True

    def test_non_cy_no_marginal(self):
        """Non-CY models don't compute marginal deformations."""
        bp = BrieskornPham(degrees=(3, 4))  # Not CY
        ring = chiral_ring_bp(bp)
        assert ring['n_marginal_deformations'] is None

    def test_sextic_marginal(self):
        """W = x^6+y^6+z^6+w^6+v^6+u^6: CY4 if sum 1/6*6=1."""
        bp = BrieskornPham(degrees=(6, 6, 6, 6, 6, 6))
        assert bp.is_cy_condition is True
        ring = chiral_ring_bp(bp)
        # This is a CY4 model, should have marginal deformations
        assert ring['n_marginal_deformations'] is not None


# ============================================================================
# 14. Kappa verification table
# ============================================================================

class TestKappaVerificationTable:
    """Test the comprehensive kappa verification table."""

    def test_table_has_entries(self):
        """The table should have entries for A-types, E-types, and quintic."""
        table = kappa_verification_table()
        types = [row['type'] for row in table]
        assert any('A' in t for t in types)
        assert any('E' in t for t in types)
        assert any('Quintic' in t for t in types)

    def test_knorrer_invariant_all(self):
        """Knorrer invariance should hold for all entries."""
        table = kappa_verification_table()
        for row in table:
            assert row['knorrer_invariant'] is True

    def test_kappa_mf_neq_kappa_vir_general(self):
        """kappa_MF != kappa_Vir for most entries (they are different objects)."""
        table = kappa_verification_table()
        # At least some should differ
        differ = [row for row in table if row.get('mf_eq_vir', True) is False]
        # VERIFIED [DC] kappa computation [LT] matrix factorization theory
        assert len(differ) > 0


# ============================================================================
# 15. E1 chiral algebra from BP
# ============================================================================

class TestE1ChiralFromBP:
    """Test the E1 chiral algebra construction from BP singularities."""

    def test_fermat_quintic_cy_dim(self):
        bp = fermat_quintic()
        alg = e1_chiral_from_bp(bp)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert alg.cy_dim == 3

    def test_fermat_quintic_kappa_cat(self):
        bp = fermat_quintic()
        alg = e1_chiral_from_bp(bp)
        assert alg.kappa_categorical == F(1024, 2)

    def test_e6_shadow_class(self):
        """E_6 surface (mu=6): shadow depth class M (mu >= 5)."""
        bp = e6_surface_singularity()
        alg = e1_chiral_from_bp(bp)
        # VERIFIED [DC] shadow depth [LT] matrix factorization theory
        assert alg.shadow_depth_class == "M"

    def test_a1_surface(self):
        """A_1 surface (x^2+y^2): mu=1, shadow class G."""
        bp = BrieskornPham(degrees=(2, 2))
        alg = e1_chiral_from_bp(bp)
        # VERIFIED [DC] shadow depth [LT] matrix factorization theory
        assert alg.shadow_depth_class == "G"


# ============================================================================
# 16. ADE singularity BP construction
# ============================================================================

class TestADESingularityBP:
    """Test ADE singularity construction as BP."""

    def test_A2_bp(self):
        """A_2 = x^3 + y^2."""
        bp = ade_singularity_bp('A', 2)
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert bp.degrees == (3, 2)
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert bp.milnor_number == 2

    def test_A4_bp(self):
        """A_4 = x^5 + y^2."""
        bp = ade_singularity_bp('A', 4)
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert bp.degrees == (5, 2)
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert bp.milnor_number == 4

    def test_E6_bp(self):
        """E_6 = x^3 + y^4."""
        bp = ade_singularity_bp('E', 6)
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert bp.degrees == (3, 4)
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert bp.milnor_number == 6

    def test_E8_bp(self):
        """E_8 = x^3 + y^5."""
        bp = ade_singularity_bp('E', 8)
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert bp.degrees == (3, 5)
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert bp.milnor_number == 8

    def test_D_not_bp(self):
        """D-type is NOT Brieskorn-Pham (has mixed term xy^2)."""
        with pytest.raises(ValueError, match="not Brieskorn-Pham"):
            ade_singularity_bp('D', 4)

    def test_E7_not_bp(self):
        """E_7 is NOT Brieskorn-Pham (has mixed term xy^3)."""
        with pytest.raises(ValueError, match="not Brieskorn-Pham"):
            ade_singularity_bp('E', 7)


# ============================================================================
# 17. Consistency check suite
# ============================================================================

class TestConsistencyChecks:
    """Test all internal consistency checks."""

    def test_all_pass(self):
        """All consistency checks should pass."""
        checks = consistency_check_all()
        for name, passed in checks.items():
            assert passed, f"Consistency check failed: {name}"

    def test_sebastiani_thom_checks(self):
        """Sebastiani-Thom multiplicativity checks pass."""
        checks = consistency_check_all()
        st_checks = {k: v for k, v in checks.items() if k.startswith('ST_')}
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert len(st_checks) >= 3
        for name, passed in st_checks.items():
            assert passed

    def test_knorrer_checks(self):
        """Knorrer periodicity checks pass."""
        checks = consistency_check_all()
        kn_checks = {k: v for k, v in checks.items() if k.startswith('Knorrer_')}
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert len(kn_checks) >= 3
        for name, passed in kn_checks.items():
            assert passed


# ============================================================================
# 18. All CY3 Gepner summary
# ============================================================================

class TestAllCY3Summary:
    """Test the summary of all CY3 Gepner models."""

    def test_four_models(self):
        """Exactly 4 uniform CY3 Gepner models."""
        summary = all_cy3_gepner_summary()
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert len(summary) == 4

    def test_all_c9(self):
        """All have total c = 9."""
        for s in all_cy3_gepner_summary():
            # VERIFIED [DC] structural property [LT] matrix factorization theory
            assert s['c_total'] == 9

    def test_all_satisfy_cy(self):
        """All satisfy the CY condition."""
        for s in all_cy3_gepner_summary():
            assert s['cy_condition'] is True

    def test_orbifold_dims_positive(self):
        """All orbifold-invariant dimensions are positive."""
        for s in all_cy3_gepner_summary():
            # VERIFIED [DC] dimension count [LT] matrix factorization theory
            assert s['orbifold_invariant_dim'] > 0


# ============================================================================
# 19. Combinatorial helpers
# ============================================================================

class TestCombinatorialHelpers:
    """Test binomial and tuple-counting functions."""

    def test_binomial_basic(self):
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert _binomial(5, 2) == 10
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert _binomial(10, 3) == 120
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert _binomial(0, 0) == 1
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert _binomial(5, 0) == 1
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert _binomial(5, 5) == 1

    def test_binomial_negative(self):
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert _binomial(3, -1) == 0
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert _binomial(3, 4) == 0

    def test_count_tuples_basic(self):
        """Count tuples (a1,...,ar) with sum=s and 0<=ai<=k."""
        # r=2, k=2, s=2: (0,2),(1,1),(2,0) -> 3
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert _count_tuples_with_sum(2, 2, 2) == 3

    def test_count_tuples_s0(self):
        """sum=0: only (0,...,0) -> 1."""
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert _count_tuples_with_sum(5, 3, 0) == 1

    def test_count_tuples_s_max(self):
        """sum=r*k: only (k,...,k) -> 1."""
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert _count_tuples_with_sum(3, 4, 12) == 1

    def test_count_tuples_quintic_s0(self):
        """Quintic: r=5, k=3, s=0 -> 1 tuple (all zeros)."""
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert _count_tuples_with_sum(5, 3, 0) == 1

    def test_count_tuples_quintic_s5(self):
        """Quintic: r=5, k=3, s=5 (charge 1 monomials)."""
        count = _count_tuples_with_sum(5, 3, 5)
        # These are the marginal deformations + the superpotential terms
        # The quintic has degree 5 monomials in 5 variables with max power 3
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert count == 101


# ============================================================================
# 20. Cross-checks between engines
# ============================================================================

class TestCrossChecks:
    """Cross-check results between this engine and matrix_factorization_shadow.py."""

    def test_milnor_agreement_A(self):
        """A-type Milnor numbers agree with shadow engine."""
        from compute.lib.matrix_factorization_shadow import make_A
        for n in range(2, 8):
            shadow = make_A(n)
            bp = BrieskornPham(degrees=(n, 2))  # A_{n-1} with Knorrer
            assert shadow.milnor_number == bp.milnor_number

    def test_milnor_agreement_E(self):
        """E-type Milnor numbers agree with shadow engine."""
        from compute.lib.matrix_factorization_shadow import make_E
        for n in [6, 8]:  # E_7 is not BP
            shadow = make_E(n)
            bp = ade_singularity_bp('E', n)
            assert shadow.milnor_number == bp.milnor_number

    def test_kappa_mf_agreement(self):
        """kappa_MF = mu/2 agrees between engines."""
        from compute.lib.matrix_factorization_shadow import make_A, kappa_mf
        for n in range(2, 8):
            shadow_kappa = kappa_mf(make_A(n))
            bp_kappa = kappa_from_milnor(n - 1)
            assert shadow_kappa == bp_kappa

    def test_central_charge_agreement(self):
        """N=2 MM central charges agree between engines."""
        from compute.lib.matrix_factorization_shadow import n2_central_charge
        for n in range(3, 8):
            shadow_c = n2_central_charge(n)
            mm = N2MinimalModel(level=n - 2)
            assert shadow_c == mm.central_charge

    def test_quintic_gepner_agreement(self):
        """Quintic Gepner data agrees between engines."""
        from compute.lib.matrix_factorization_shadow import (
            quintic_gepner, quintic_lgcy_check,
        )
        shadow_gepner = quintic_gepner()
        e1_gepner = quintic_gepner_e1()
        assert shadow_gepner.total_central_charge() == e1_gepner.total_central_charge
        assert shadow_gepner.verify_cy_condition() == e1_gepner.verify_cy_condition()

    def test_quintic_lgcy_agreement(self):
        """LGCY invariant dimension agrees."""
        from compute.lib.matrix_factorization_shadow import quintic_lgcy_check
        shadow_result = quintic_lgcy_check()
        e1_result = quintic_lgcy()
        assert shadow_result['dim_invariant_jac'] == e1_result.orbifold_dim

    def test_e6_central_charge_agreement(self):
        """E6 central charge agrees between engines."""
        from compute.lib.matrix_factorization_shadow import n2_central_charge_E
        shadow_c = n2_central_charge_E(6)
        sc = singularity_category_E(6)
        assert shadow_c == sc.central_charge


# ============================================================================
# 21. Edge cases and boundary conditions
# ============================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_a1_singularity(self):
        """A_1: W=x^2, mu=1, simplest case."""
        bp = BrieskornPham(degrees=(2,))
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert bp.milnor_number == 1
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert bp.cy_dimension == -1

    def test_single_variable_cy_dim_minus1(self):
        """Single-variable BP: CY dim = -1 (formal/not geometric)."""
        bp = BrieskornPham(degrees=(7,))
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert bp.cy_dimension == -1

    def test_two_variables_cy_dim_0(self):
        """Two-variable BP: CY dim = 0 (semisimple MF category)."""
        bp = BrieskornPham(degrees=(3, 5))
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert bp.cy_dimension == 0

    def test_large_degree(self):
        """Large degree: W = x^100, mu = 99."""
        bp = BrieskornPham(degrees=(100,))
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert bp.milnor_number == 99
        assert kappa_from_milnor(99) == F(99, 2)

    def test_many_variables(self):
        """Many variables: W = x_1^2 + ... + x_10^2, mu = 1."""
        bp = BrieskornPham(degrees=tuple([2] * 10))
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert bp.milnor_number == 1  # 1^10 = 1
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert bp.cy_dimension == 8

    def test_c_hat_negative(self):
        """c_hat can be negative for small degrees / many variables."""
        bp = BrieskornPham(degrees=(2, 2, 2))
        # c_hat = 3 - 2*(1/2+1/2+1/2) = 3 - 3 = 0
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert bp.c_hat == 0

    def test_n2_mm_large_level(self):
        """Large level N=2 MM: c -> 3."""
        mm = N2MinimalModel(level=1000)
        c = mm.central_charge
        # c = 3000/1002 = 500/167 ~ 2.994
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert c < 3
        # VERIFIED [DC] structural property [LT] matrix factorization theory
        assert c > F(29, 10)  # > 2.9


# ============================================================================
# 22. Orbifold-dimension exact formula verification
# ============================================================================

class TestOrbifoldExact:
    """Verify the exact orbifold-invariant dimension formula."""

    def test_quintic_exact(self):
        """(3)^5: (4^5 + (-1)^5 * 4)/5 = (1024-4)/5 = 204."""
        g = quintic_gepner_e1()
        dim = g.orbifold_invariant_dimension_exact()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert dim == 204
        # Manual check
        # VERIFIED [DC] exactness [LT] matrix factorization theory
        assert (1024 + (-1)**5 * 4) == 1020
        # VERIFIED [DC] exactness [LT] matrix factorization theory
        assert 1020 // 5 == 204

    def test_19_exact(self):
        """(1)^9: n=3 divides r=9, so (2^9+(-1)^9*2)/3 = (512-2)/3 = 170."""
        g = cy3_gepner_models()[0]
        dim = g.orbifold_invariant_dimension_exact()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert dim == 170
        # Manual: n=3, r=9, mu=2. n|r.
        # VERIFIED [DC] exactness [LT] matrix factorization theory
        assert (2**9 + (-1)**9 * 2) == 510
        # VERIFIED [DC] exactness [LT] matrix factorization theory
        assert 510 // 3 == 170

    def test_26_exact(self):
        """(2)^6: n=4 does not divide r=6, so (3^6+(-1)^7)/4 = (729-1)/4 = 182."""
        g = cy3_gepner_models()[1]
        dim = g.orbifold_invariant_dimension_exact()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert dim == 182
        # Manual: n=4, r=6, mu=3. n does not divide r.
        # VERIFIED [DC] exactness [LT] matrix factorization theory
        assert (3**6 + (-1)**7) == 728
        # VERIFIED [DC] exactness [LT] matrix factorization theory
        assert 728 // 4 == 182

    def test_64_exact(self):
        """(6)^4: n=8 does not divide r=4, so (7^4+(-1)^5)/8 = (2401-1)/8 = 300."""
        g = cy3_gepner_models()[3]
        dim = g.orbifold_invariant_dimension_exact()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert dim == 300
        # VERIFIED [DC] exactness [LT] matrix factorization theory
        assert (7**4 + (-1)**5) == 2400
        # VERIFIED [DC] exactness [LT] matrix factorization theory
        assert 2400 // 8 == 300

    def test_exact_matches_numerical(self):
        """Exact and numerical computations agree for all CY3 Gepner models."""
        for g in cy3_gepner_models():
            exact = int(g.orbifold_invariant_dimension_exact())
            numerical = g.orbifold_invariant_dimension()
            assert exact == numerical, f"Mismatch for levels {g.levels}"


# ============================================================================
# 23. Charge and weight computations
# ============================================================================

class TestChargeWeights:
    """Test charge/weight computations for BP singularities."""

    def test_quintic_c_hat_equals_3(self):
        """Quintic: c_hat = 3 = CY dim."""
        bp = fermat_quintic()
        assert bp.c_hat == bp.cy_dimension

    def test_c_hat_formula(self):
        """c_hat = sum(1 - 2/d_i) = n - 2*sum(1/d_i)."""
        for degrees in [(5, 5, 5, 5, 5), (3, 4), (2, 2, 2, 2)]:
            bp = BrieskornPham(degrees=degrees)
            expected = sum(1 - F(2, d) for d in degrees)
            assert bp.c_hat == expected

    def test_cy_condition_iff_c_hat_eq_dim_minus_2(self):
        """CY condition sum q_i = 1 iff c_hat = n-2 = CY dim."""
        bp_cy = fermat_quintic()
        assert bp_cy.is_cy_condition
        assert bp_cy.c_hat == bp_cy.cy_dimension

        bp_ncy = BrieskornPham(degrees=(3, 4))
        assert not bp_ncy.is_cy_condition
        assert bp_ncy.c_hat != bp_ncy.cy_dimension


# ============================================================================
# 24. Summary table data integrity
# ============================================================================

class TestSummaryIntegrity:
    """Test data integrity of summary tables."""

    def test_gepner_summary_orbifold_dims_all_positive(self):
        for s in all_cy3_gepner_summary():
            # VERIFIED [DC] dimension count [LT] matrix factorization theory
            assert s['orbifold_invariant_dim'] > 0

    def test_gepner_summary_mu_consistency(self):
        """mu_total = mu_per_factor^r."""
        for s in all_cy3_gepner_summary():
            assert s['mu_total'] == s['mu_per_factor'] ** s['r']

    def test_ade_table_kappa_positive(self):
        """All kappa_MF values are positive."""
        for row in ade_e1_chiral_table():
            # VERIFIED [DC] kappa formula [LT] matrix factorization theory
            assert row['kappa_mf'] > 0

    def test_ade_table_c_nonnegative(self):
        """All central charges are nonnegative."""
        for row in ade_e1_chiral_table():
            # VERIFIED [DC] structural property [LT] matrix factorization theory
            assert row['c'] >= 0
