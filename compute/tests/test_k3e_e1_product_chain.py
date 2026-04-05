"""Tests for the K3 x E  E_1-chiral functor chain.

90+ tests covering:
  - Hodge numbers (Kuenneth + direct + symmetry checks)
  - Hochschild homology (two independent computations)
  - Kappa values (four paths + cross-verification)
  - E_n structure analysis
  - E_1 bar complex generators
  - BKM identification
  - CY involution constraints
  - Cross-module consistency
  - The kappa = 13 question
"""

import pytest
from fractions import Fraction

import sys
from pathlib import Path

# Ensure repo root on path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from compute.lib.k3e_e1_product_chain import (
    # Hodge data
    k3_hodge, e_hodge, k3e_hodge, k3e_hodge_diamond,
    k3e_euler_characteristic, k3e_betti_numbers,
    K3_HODGE, E_HODGE,

    # Hochschild homology
    hh_k3, hh_e, hh_k3e_kuenneth, hh_k3e_direct,
    hh_k3e_verify_consistency,

    # Kappa
    kappa_bcov, kappa_bkm, kappa_tensor_product, kappa_rank1_fiber,
    kappa_comparison, kappa_13_analysis,

    # E_n structure
    en_elliptic_curve, en_k3, en_k3e_naive_product, en_k3e_cy3,
    en_rank1_sector, en_rank2_sector,
    e1_obstruction_class,

    # Lie conformal algebra
    lie_conformal_k3e,

    # Chiral algebra
    chiral_algebra_k3e,

    # Bar complex
    e1_bar_generators, e1_bar_euler_char,

    # BKM identification
    bkm_bar_identification,

    # CY involution
    cy_involution_constraints,

    # Product vs twist
    product_vs_e1_twist,

    # Full functor chain
    full_functor_chain,

    # Cross-verification
    cross_verify_with_coha,
    cross_verify_with_shadow,
    cross_verify_hodge_with_functor,

    # Summary
    summary_statistics,
)


# =========================================================================
# SECTION 1: HODGE NUMBERS (18 tests)
# =========================================================================

class TestK3Hodge:
    """K3 surface Hodge numbers."""

    def test_h00(self):
        assert k3_hodge(0, 0) == 1

    def test_h10(self):
        assert k3_hodge(1, 0) == 0

    def test_h01(self):
        assert k3_hodge(0, 1) == 0

    def test_h20(self):
        assert k3_hodge(2, 0) == 1

    def test_h11(self):
        assert k3_hodge(1, 1) == 20

    def test_h02(self):
        assert k3_hodge(0, 2) == 1

    def test_h22(self):
        assert k3_hodge(2, 2) == 1

    def test_euler_char(self):
        """chi(K3) = 24."""
        chi = sum((-1)**(p+q) * k3_hodge(p, q) for p in range(3) for q in range(3))
        assert chi == 24

    def test_hodge_symmetry(self):
        """h^{p,q} = h^{q,p} for Kahler manifold."""
        for p in range(3):
            for q in range(3):
                assert k3_hodge(p, q) == k3_hodge(q, p)


class TestEllipticCurveHodge:
    """Elliptic curve Hodge numbers."""

    def test_h00(self):
        assert e_hodge(0, 0) == 1

    def test_h10(self):
        assert e_hodge(1, 0) == 1

    def test_h01(self):
        assert e_hodge(0, 1) == 1

    def test_h11(self):
        assert e_hodge(1, 1) == 1

    def test_euler_char_zero(self):
        """chi(E) = 0."""
        chi = sum((-1)**(p+q) * e_hodge(p, q) for p in range(2) for q in range(2))
        assert chi == 0


class TestK3EHodge:
    """K3 x E Hodge numbers via Kuenneth."""

    def test_h00(self):
        assert k3e_hodge(0, 0) == 1

    def test_h10(self):
        """h^{1,0}(K3xE) = h^{1,0}(K3)*h^{0,0}(E) + h^{0,0}(K3)*h^{1,0}(E) = 0+1 = 1."""
        assert k3e_hodge(1, 0) == 1

    def test_h01(self):
        assert k3e_hodge(0, 1) == 1

    def test_h11(self):
        """h^{1,1}(K3xE) = 20 + 0 + 0 + 1 = 21."""
        assert k3e_hodge(1, 1) == 21

    def test_h20(self):
        """h^{2,0}(K3xE) = h^{2,0}(K3) + h^{1,0}(K3)*h^{1,0}(E) = 1 + 0 = 1."""
        assert k3e_hodge(2, 0) == 1

    def test_h21(self):
        """h^{2,1}(K3xE) = h^{2,1}(K3) + h^{1,1}(K3)*h^{1,0}(E) + h^{2,0}(K3)*h^{0,1}(E) = 0 + 20 + 1 = 21."""
        assert k3e_hodge(2, 1) == 21

    def test_h30(self):
        """h^{3,0}(K3xE) = h^{2,0}(K3)*h^{1,0}(E) = 1."""
        assert k3e_hodge(3, 0) == 1

    def test_h33(self):
        """h^{3,3}(K3xE) = h^{2,2}(K3)*h^{1,1}(E) = 1."""
        assert k3e_hodge(3, 3) == 1

    def test_euler_characteristic_zero(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
        assert k3e_euler_characteristic() == 0

    def test_euler_from_hodge_diamond(self):
        """chi = sum (-1)^{p+q} h^{p,q}."""
        diamond = k3e_hodge_diamond()
        chi = sum((-1)**(p+q) * v for (p, q), v in diamond.items())
        assert chi == 0

    def test_hodge_symmetry_k3e(self):
        """h^{p,q}(K3xE) = h^{q,p}(K3xE) (Kahler)."""
        for p in range(4):
            for q in range(4):
                assert k3e_hodge(p, q) == k3e_hodge(q, p), \
                    f"h^{{{p},{q}}} = {k3e_hodge(p,q)} != h^{{{q},{p}}} = {k3e_hodge(q,p)}"

    def test_serre_duality_k3e(self):
        """h^{p,q}(K3xE) = h^{3-p,3-q}(K3xE) (Serre duality for compact Kahler 3-fold)."""
        for p in range(4):
            for q in range(4):
                assert k3e_hodge(p, q) == k3e_hodge(3 - p, 3 - q), \
                    f"Serre: h^{{{p},{q}}} = {k3e_hodge(p,q)} != h^{{{3-p},{3-q}}} = {k3e_hodge(3-p,3-q)}"

    def test_h11_equals_h21(self):
        """For K3 x E: h^{1,1} = h^{2,1} = 21 (mirror-symmetric CY3)."""
        assert k3e_hodge(1, 1) == k3e_hodge(2, 1) == 21

    def test_betti_b0(self):
        assert k3e_betti_numbers()[0] == 1

    def test_betti_b1(self):
        """b_1(K3xE) = h^{1,0} + h^{0,1} = 2."""
        assert k3e_betti_numbers()[1] == 2

    def test_betti_b2(self):
        """b_2 = h^{2,0} + h^{1,1} + h^{0,2} = 1 + 21 + 1 = 23."""
        assert k3e_betti_numbers()[2] == 23

    def test_betti_b3(self):
        """b_3 = h^{3,0} + h^{2,1} + h^{1,2} + h^{0,3} = 1+21+21+1 = 44."""
        assert k3e_betti_numbers()[3] == 44

    def test_total_betti(self):
        """sum b_k = 2*(1 + 2 + 23 + 44) = ... actually b_k satisfy Poincare duality."""
        betti = k3e_betti_numbers()
        # For a compact orientable 6-manifold: b_0=b_6, b_1=b_5, b_2=b_4
        assert betti[0] == betti[6]
        assert betti[1] == betti[5]
        assert betti[2] == betti[4]


# =========================================================================
# SECTION 2: HOCHSCHILD HOMOLOGY (12 tests)
# =========================================================================

class TestHHK3:
    """Hochschild homology of D^b(K3)."""

    def test_hh0(self):
        assert hh_k3()[0] == 2

    def test_hh1(self):
        assert hh_k3()[1] == 20

    def test_hh2(self):
        assert hh_k3()[2] == 2

    def test_total(self):
        assert sum(hh_k3().values()) == 24


class TestHHE:
    """Hochschild homology of D^b(E)."""

    def test_hh0(self):
        assert hh_e()[0] == 2

    def test_hh1(self):
        assert hh_e()[1] == 2

    def test_total(self):
        assert sum(hh_e().values()) == 4


class TestHHK3E:
    """Hochschild homology of D^b(K3 x E)."""

    def test_kuenneth_hh0(self):
        assert hh_k3e_kuenneth()[0] == 4

    def test_kuenneth_hh1(self):
        assert hh_k3e_kuenneth()[1] == 44

    def test_kuenneth_hh2(self):
        assert hh_k3e_kuenneth()[2] == 44

    def test_kuenneth_hh3(self):
        assert hh_k3e_kuenneth()[3] == 4

    def test_kuenneth_total(self):
        assert sum(hh_k3e_kuenneth().values()) == 96

    def test_direct_equals_kuenneth(self):
        """Two independent HH computations must agree."""
        assert hh_k3e_kuenneth() == hh_k3e_direct()

    def test_consistency_three_paths(self):
        """Three-path verification of HH dimensions."""
        result = hh_k3e_verify_consistency()
        assert result['all_consistent']

    def test_kuenneth_palindromic(self):
        """HH dimensions are palindromic: HH_p = HH_{d-p} for CY d-fold."""
        hh = hh_k3e_kuenneth()
        assert hh[0] == hh[3]
        assert hh[1] == hh[2]


# =========================================================================
# SECTION 3: KAPPA VALUES (14 tests)
# =========================================================================

class TestKappa:
    """Kappa computation via multiple paths."""

    def test_bcov_zero(self):
        """kappa_BCOV = chi/24 = 0/24 = 0."""
        assert kappa_bcov() == Fraction(0)

    def test_bkm_five(self):
        """kappa_BKM = c(0)/2 = 10/2 = 5."""
        assert kappa_bkm() == Fraction(5)

    def test_tensor_twentyfive(self):
        """kappa_tensor = 24 + 1 = 25."""
        assert kappa_tensor_product() == Fraction(25)

    def test_fiber_twentyfour(self):
        """kappa_fiber = chi(K3) = 24."""
        assert kappa_rank1_fiber() == Fraction(24)

    def test_all_four_distinct(self):
        """The four kappa values are all different."""
        vals = [kappa_bcov(), kappa_bkm(), kappa_tensor_product(), kappa_rank1_fiber()]
        assert len(set(vals)) == 4

    def test_bcov_from_chi(self):
        """kappa_BCOV = chi(K3xE)/24 from the Euler characteristic."""
        assert kappa_bcov() == Fraction(k3e_euler_characteristic(), 24)

    def test_bkm_weight_igusa(self):
        """kappa_BKM = weight(Delta_5) = 5."""
        comp = kappa_comparison()
        assert comp['bkm_equals_weight']

    def test_kappa_comparison_consistency(self):
        """All cross-checks in kappa_comparison pass."""
        comp = kappa_comparison()
        assert comp['bcov_from_chi']
        assert comp['bkm_from_c0']
        assert comp['bkm_equals_weight']
        assert comp['tensor_not_bkm']
        assert comp['fiber_not_bkm']

    def test_kappa_bkm_from_phi01(self):
        """kappa_BKM = c(0)/2 where c(0) is the disc-0 coefficient of phi_{0,1}."""
        comp = kappa_comparison()
        assert comp['c0_phi01'] == 10
        assert comp['kappa_BKM'] == Fraction(10, 2)

    def test_kappa_13_cy_sum(self):
        """CY-category kappa sum: kappa_{CY2}(K3) + kappa_{CY1}(E) = 12 + 1 = 13."""
        analysis = kappa_13_analysis()
        assert analysis['naive_sum_CY'] == Fraction(13)

    def test_kappa_13_voa_sum(self):
        """VOA kappa sum: kappa(V_Lambda) + kappa(H_1) = 24 + 1 = 25."""
        analysis = kappa_13_analysis()
        assert analysis['naive_sum_VOA'] == Fraction(25)

    def test_kappa_13_not_equal_bkm(self):
        """Neither 13 nor 25 equals the BKM kappa = 5."""
        analysis = kappa_13_analysis()
        assert analysis['naive_sum_CY'] != kappa_bkm()
        assert analysis['naive_sum_VOA'] != kappa_bkm()

    def test_self_dual_virasoro_kappa(self):
        """kappa(Vir_{13}) = 13/2 (NOT 13)."""
        analysis = kappa_13_analysis()
        assert analysis['self_dual_virasoro_kappa'] == Fraction(13, 2)

    def test_critical_virasoro_kappa(self):
        """kappa(Vir_{26}) = 26/2 = 13."""
        analysis = kappa_13_analysis()
        assert analysis['critical_virasoro_kappa'] == Fraction(13)


# =========================================================================
# SECTION 4: E_n STRUCTURE (12 tests)
# =========================================================================

class TestEnStructure:
    """E_n operadic level analysis."""

    def test_elliptic_curve_e_infty(self):
        """D^b(E) gives E_infty (symmetric braiding)."""
        en = en_elliptic_curve()
        assert en.n >= 100  # effectively infinity

    def test_k3_e2(self):
        """D^b(K3) gives E_2 (holomorphic symplectic braiding)."""
        en = en_k3()
        assert en.n == 2

    def test_naive_product_e2(self):
        """Naive tensor product has E_2 (from Dunn additivity)."""
        en = en_k3e_naive_product()
        assert en.n == 2

    def test_cy3_e1(self):
        """CY3 chiral algebra is E_1 (not E_2)."""
        en = en_k3e_cy3()
        assert en.n == 1

    def test_rank1_sector_e_infty(self):
        """Rank-1 sector is E_infty (abelian theory)."""
        en = en_rank1_sector()
        assert en.n >= 100

    def test_rank2_sector_e1(self):
        """Rank-2 sector is E_1 (non-commutative BKM bracket)."""
        en = en_rank2_sector()
        assert en.n == 1

    def test_e1_less_than_naive_product(self):
        """CY3 E_1 < naive product E_2."""
        assert en_k3e_cy3().n < en_k3e_naive_product().n

    def test_obstruction_exists(self):
        """E_2 obstruction is nontrivial."""
        obs = e1_obstruction_class()
        assert obs['e2_obstruction_exists']

    def test_bkm_non_abelian(self):
        """BKM algebra is non-abelian (source of E_2 obstruction)."""
        obs = e1_obstruction_class()
        assert not obs['is_abelian']

    def test_gram_matrix_indefinite(self):
        """BKM real root Gram matrix is indefinite (det < 0)."""
        obs = e1_obstruction_class()
        assert obs['gram_det'] < 0

    def test_three_real_roots(self):
        """BKM has exactly 3 real simple roots."""
        obs = e1_obstruction_class()
        assert obs['real_roots'] == 3

    def test_gram_trace(self):
        """Gram matrix trace = 2 + 2 + 2 = 6."""
        obs = e1_obstruction_class()
        assert obs['gram_trace'] == 6


# =========================================================================
# SECTION 5: LIE CONFORMAL ALGEBRA (5 tests)
# =========================================================================

class TestLieConformal:
    """Lie conformal algebra L_{K3 x E}."""

    def test_total_rank(self):
        """Total rank = dim HH_1 = 44."""
        lca = lie_conformal_k3e()
        assert lca.total_rank == 44

    def test_heisenberg_sector(self):
        """Heisenberg sector: HH_0(K3) * HH_1(E) = 2*2 = 4."""
        lca = lie_conformal_k3e()
        assert lca.generators['heisenberg'] == 4

    def test_k3_deformation_sector(self):
        """K3 deformation sector: HH_1(K3) * HH_0(E) = 20*2 = 40."""
        lca = lie_conformal_k3e()
        assert lca.generators['k3_deformation'] == 40

    def test_sector_sum(self):
        """Sector sum: 4 + 40 = 44 = total rank."""
        lca = lie_conformal_k3e()
        assert lca.generators['heisenberg'] + lca.generators['k3_deformation'] == lca.total_rank

    def test_non_abelian_bracket(self):
        """Bracket type is non-abelian (KS bracket from CY3 trace)."""
        lca = lie_conformal_k3e()
        assert 'non-abelian' in lca.bracket_type


# =========================================================================
# SECTION 6: CHIRAL ALGEBRA (8 tests)
# =========================================================================

class TestChiralAlgebra:
    """E_1-chiral algebra A_{K3 x E}."""

    def test_en_level(self):
        assert chiral_algebra_k3e().en_level == 1

    def test_kappa_bkm(self):
        assert chiral_algebra_k3e().kappa_bkm == Fraction(5)

    def test_kappa_bcov(self):
        assert chiral_algebra_k3e().kappa_bcov == Fraction(0)

    def test_kappa_tensor(self):
        assert chiral_algebra_k3e().kappa_tensor == Fraction(25)

    def test_kappa_fiber(self):
        assert chiral_algebra_k3e().kappa_fiber == Fraction(24)

    def test_total_hh(self):
        assert chiral_algebra_k3e().total_hh_dim == 96

    def test_shadow_depth_M(self):
        assert 'M' in chiral_algebra_k3e().shadow_depth

    def test_bkm_algebra(self):
        assert 'Delta_5' in chiral_algebra_k3e().bkm_algebra


# =========================================================================
# SECTION 7: BAR COMPLEX GENERATORS (8 tests)
# =========================================================================

class TestBarGenerators:
    """E_1 bar complex generators."""

    def test_real_root_disc_neg1(self):
        """Discriminant D=-1: real root, mult = 1."""
        bar = e1_bar_generators()
        gen = bar['generators_by_disc'][-1]
        assert gen['multiplicity'] == 1
        assert gen['type'] == 'real'

    def test_first_imaginary_disc_0(self):
        """Discriminant D=0: first imaginary, mult = 10."""
        bar = e1_bar_generators()
        gen = bar['generators_by_disc'][0]
        assert gen['multiplicity'] == 10
        assert gen['type'] == 'imaginary_bosonic'

    def test_disc_1_mult(self):
        """Discriminant D=1: c(1) = 108."""
        bar = e1_bar_generators()
        if 1 in bar['generators_by_disc']:
            assert bar['generators_by_disc'][1]['multiplicity'] == 108

    def test_first_fermionic_disc_3(self):
        """Discriminant D=3: first fermionic root, c(3) = -64."""
        bar = e1_bar_generators()
        if 3 in bar['generators_by_disc']:
            gen = bar['generators_by_disc'][3]
            assert gen['multiplicity'] == -64
            assert gen['type'] == 'imaginary_fermionic'

    def test_total_positive(self):
        """Total generator dimension is positive."""
        bar = e1_bar_generators()
        assert bar['total_dim_through_D'] > 0

    def test_bosonic_exceeds_fermionic_low_disc(self):
        """At low discriminant, bosonic generators outnumber fermionic."""
        bar = e1_bar_generators(max_disc=4)
        assert bar['total_bosonic'] > bar['total_fermionic']

    def test_bar_degree_one(self):
        """All generators have bar degree 1 (desuspended)."""
        bar = e1_bar_generators()
        for D, gen in bar['generators_by_disc'].items():
            assert gen['bar_degree'] == 1

    def test_abs_mult_positive(self):
        """Absolute multiplicity is always positive."""
        bar = e1_bar_generators()
        for D, gen in bar['generators_by_disc'].items():
            assert gen['abs_multiplicity'] > 0


# =========================================================================
# SECTION 8: BKM IDENTIFICATION (3 tests)
# =========================================================================

class TestBKMIdentification:
    """BKM bar complex identification."""

    def test_conjectural_for_d3(self):
        bkm = bkm_bar_identification()
        assert bkm['conjectural_for_d3']

    def test_proved_for_d2(self):
        bkm = bkm_bar_identification()
        assert bkm['proved_for_d2']

    def test_has_evidence(self):
        bkm = bkm_bar_identification()
        assert len(bkm['evidence']) >= 3


# =========================================================================
# SECTION 9: CY INVOLUTION (6 tests)
# =========================================================================

class TestCYInvolution:
    """CY involution g(z)g(-z) = 1 constraints."""

    def test_halves_generators(self):
        """CY involution halves the number of generators."""
        inv = cy_involution_constraints()
        assert inv['reduction_factor'] == Fraction(1, 2)

    def test_independent_are_odd(self):
        """Independent generators have odd indices."""
        inv = cy_involution_constraints()
        for n in inv['independent_generators']:
            assert n % 2 == 1

    def test_dependent_are_even(self):
        """Dependent generators have even indices."""
        inv = cy_involution_constraints()
        for n in inv['dependent_generators']:
            assert n % 2 == 0

    def test_g2_relation(self):
        """g_2 = g_1^2 / 2."""
        inv = cy_involution_constraints()
        assert 2 in inv['relations']
        assert 'g_1' in inv['relations'][2]

    def test_equal_counts(self):
        """Equal number of independent and dependent generators."""
        inv = cy_involution_constraints(max_order=10)
        assert inv['num_independent'] == inv['num_dependent']

    def test_g4_relation_has_g3(self):
        """g_4 depends on g_3 (not just g_1)."""
        inv = cy_involution_constraints()
        assert 'g_3' in inv['relations'][4]


# =========================================================================
# SECTION 10: PRODUCT vs E_1 TWIST (4 tests)
# =========================================================================

class TestProductVsTwist:
    """Comparison of naive product and E_1-twisted algebra."""

    def test_hh_match(self):
        """HH dimensions match (same vector space, different algebra structure)."""
        result = product_vs_e1_twist()
        assert result['hh_match']

    def test_en_product_higher(self):
        """Naive product E_n > CY3 E_n."""
        result = product_vs_e1_twist()
        assert result['en_product'] > result['en_cy3']

    def test_rank1_einfty(self):
        """Rank 1 sector is E_infty."""
        result = product_vs_e1_twist()
        assert 'infty' in result['rank_filtration'][1]['en']

    def test_rank_ge2_e1(self):
        """Rank >= 2 sector is E_1."""
        result = product_vs_e1_twist()
        assert 'E_1' in result['rank_filtration']['>=2']['en']


# =========================================================================
# SECTION 11: CROSS-VERIFICATION (6 tests)
# =========================================================================

class TestCrossVerification:
    """Cross-module consistency checks."""

    def test_hodge_matches_functor(self):
        """Our Hodge numbers match cy_to_chiral_functor module."""
        result = cross_verify_hodge_with_functor()
        assert result['match'], f"Mismatches: {result['mismatches']}"

    def test_shadow_kappa_fiber_match(self):
        """kappa_fiber matches k3e_relative_shadow module."""
        result = cross_verify_with_shadow()
        assert result['match_fiber']

    def test_shadow_kappa_bkm_match(self):
        """kappa_BKM matches k3e_relative_shadow module."""
        result = cross_verify_with_shadow()
        assert result['match_bkm']

    def test_coha_bar_consistency(self):
        """CoHA dimensions match bar generator multiplicities."""
        result = cross_verify_with_coha()
        assert result['all_match']

    def test_hh_total_matches_product(self):
        """Total HH(K3xE) = total HH(K3) * total HH(E) = 24 * 4 = 96."""
        hh_k = sum(hh_k3().values())
        hh_ec = sum(hh_e().values())
        hh_product_total = hh_k * hh_ec
        hh_k3e_total = sum(hh_k3e_kuenneth().values())
        assert hh_product_total == hh_k3e_total == 96

    def test_euler_multiplicative(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
        chi_k3 = sum((-1)**(p+q) * k3_hodge(p,q) for p in range(3) for q in range(3))
        chi_e = sum((-1)**(p+q) * e_hodge(p,q) for p in range(2) for q in range(2))
        assert chi_k3 * chi_e == k3e_euler_characteristic()


# =========================================================================
# SECTION 12: FULL FUNCTOR CHAIN (5 tests)
# =========================================================================

class TestFullFunctorChain:
    """Full functor chain integration."""

    def test_chain_runs(self):
        """Full functor chain completes without error."""
        result = full_functor_chain()
        assert result is not None

    def test_chain_euler_zero(self):
        result = full_functor_chain()
        assert result.euler_characteristic == 0

    def test_chain_total_hh_96(self):
        result = full_functor_chain()
        assert result.total_hh == 96

    def test_chain_en_1(self):
        result = full_functor_chain()
        assert result.en_structure.n == 1

    def test_chain_kappa_bkm_5(self):
        result = full_functor_chain()
        assert result.kappa_comparison['kappa_BKM'] == Fraction(5)


# =========================================================================
# SECTION 13: SUMMARY STATISTICS (4 tests)
# =========================================================================

class TestSummary:
    """Summary statistics."""

    def test_cy_dimension(self):
        assert summary_statistics()['cy_dimension'] == 3

    def test_h11_21(self):
        assert summary_statistics()['hodge_h11'] == 21

    def test_h21_21(self):
        assert summary_statistics()['hodge_h21'] == 21

    def test_igusa_weight_5(self):
        assert summary_statistics()['igusa_weight'] == 5
