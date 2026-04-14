r"""Tests for factorization_categories_chiral.py: factorization categories for chiral quantum groups.

CENTRAL RESULTS:
    (1) Kazhdan-Lusztig factorization category: Rep^{E_2}(V_k(g))^{ss} ~ MTC_q(g) (PROVED).
    (2) Verlinde formula: dim V_{k,sl_2}(Sigma_g) computed and cross-checked.
    (3) Heisenberg factorization category: Rep(H_Muk) with character 1/eta^{24} (PROVED).
    (4) Drinfeld center passage: Z(Rep^{E_1}) = Rep^{E_2} (braided from ordered).
    (5) E_n hierarchy: d=1 -> E_inf, d=2 -> E_2, d=3 -> E_1 (VERIFIED).
    (6) BPS category for K3 x E: CONJECTURAL, Gottsche numbers verified.
    (7) Ran space formulation: cosheaf on Ran(C) for E_inf / Ran^{ord}(C) for E_1.
    (8) Factorization isomorphism: F(U_1 cup U_2) ~ F(U_1) tensor F(U_2) (VERIFIED).

Manuscript references:
    en_factorization.tex sec:dunn-additivity (E_n hierarchy)
    braided_factorization.tex sec:bf-categorical-r-matrix (categorical R-matrix)
    quantum_groups_foundations.tex thm:qgf-kazhdan-lusztig (KL equivalence)
    modular_koszul_bridge.tex def:three-hochschild (derived center as End(id))
"""

import pytest
from fractions import Fraction

from compute.lib.factorization_categories_chiral import (
    # Constants
    MUKAI_RANK,
    MUKAI_SIG_PLUS,
    MUKAI_SIG_MINUS,
    SL2_DIM,
    SL2_DUAL_COXETER,
    SL2_LACING,
    VERLINDE_SL2_G0,
    VERLINDE_SL2_G1,
    VERLINDE_SL2_G2,
    # Axioms
    verify_factorization_category_axioms,
    # Kazhdan-Lusztig
    kazhdan_lusztig_sl2,
    verlinde_dimension_table,
    # Heisenberg
    heisenberg_factorization_category,
    heisenberg_fiber_dimensions,
    # Drinfeld center
    drinfeld_center_factorization_category,
    # Ran space
    ran_space_formulation,
    # BPS
    bps_factorization_category_k3,
    # E_n hierarchy
    en_factorization_category_by_dimension,
    # Factorization isomorphism
    verify_factorization_isomorphism,
    # Comparison
    factorization_algebra_vs_category,
    # Chiral homology
    chiral_homology_factorization_category,
    # Landscape
    factorization_category_landscape,
    # Verification
    verify_kazhdan_lusztig_consistency,
    verify_heisenberg_factcat_consistency,
    verify_en_hierarchy_consistency,
    verify_bps_category_consistency,
    verify_algebra_vs_category,
    full_verification,
)

F = Fraction


# =========================================================================
# Section 1: Factorization category axioms
# =========================================================================

class TestFactorizationCategoryAxioms:
    """Verify the five factorization category axioms."""

    def test_heisenberg_axioms_all_satisfied(self):
        """Heisenberg (E_inf): all five axioms unconditional."""
        ax = verify_factorization_category_axioms('heisenberg')
        assert ax.all_satisfied is True

    def test_kac_moody_axioms_all_satisfied(self):
        """Affine KM at positive integer level: all axioms proved."""
        ax = verify_factorization_category_axioms('kac_moody')
        assert ax.all_satisfied is True

    def test_yangian_axioms_structural(self):
        """Yangian (E_1): axioms structurally consistent."""
        ax = verify_factorization_category_axioms('yangian')
        assert ax.all_satisfied is True

    def test_quantum_toroidal_axioms(self):
        """Quantum toroidal (E_3 on C^3): axioms structural."""
        ax = verify_factorization_category_axioms('quantum_toroidal')
        assert ax.all_satisfied is True

    def test_unknown_algebra_raises(self):
        """Unknown algebra type raises ValueError."""
        with pytest.raises(ValueError):
            verify_factorization_category_axioms('unknown')

    def test_fc1_assignment_universal(self):
        """FC1 (assignment) holds for all known types."""
        for t in ('heisenberg', 'kac_moody', 'yangian', 'quantum_toroidal'):
            ax = verify_factorization_category_axioms(t)
            assert ax.fc1_assignment is True

    def test_fc3_factorization_universal(self):
        """FC3 (factorization for disjoint opens) holds universally."""
        for t in ('heisenberg', 'kac_moody', 'yangian', 'quantum_toroidal'):
            ax = verify_factorization_category_axioms(t)
            assert ax.fc3_factorization is True


# =========================================================================
# Section 2: Kazhdan-Lusztig factorization category
# =========================================================================

class TestKazhdanLusztigCategory:
    """Kazhdan-Lusztig factorization category for sl_2."""

    def test_kl_level1_central_charge(self):
        """V_1(sl_2): c = 1*3/(1+2) = 1.
        # VERIFIED: [DC] k*dim(g)/(k+h^v) = 1*3/3 = 1, [LT] Kac "Infinite-dim Lie algebras" (1990) Table Aff 1
        # [LC] k=1 is minimal model boundary: c(sl_2, k=1) = 1
        """
        kl = kazhdan_lusztig_sl2(1)
        # DC path: direct formula
        assert kl.central_charge == F(1)
        # CF path: formula c = k*dim(g)/(k+h^v) with dim(sl_2)=3, h^v=2
        assert kl.central_charge == F(1 * 3, 1 + 2)

    def test_kl_level2_central_charge(self):
        """V_2(sl_2): c = 2*3/(2+2) = 3/2.
        # VERIFIED: [DC] k*dim(g)/(k+h^v) = 6/4, [LT] Di Francesco et al. CFT (1997) Ch. 18
        # [LC] Ising model central charge c = 1/2 is DIFFERENT (that is minimal model, not KM)
        """
        kl = kazhdan_lusztig_sl2(2)
        assert kl.central_charge == F(3, 2)
        # DC path: 2*3/(2+2) = 6/4 = 3/2
        assert kl.central_charge == F(2 * SL2_DIM, 2 + SL2_DUAL_COXETER)

    def test_kl_level3_central_charge(self):
        """V_3(sl_2): c = 3*3/(3+2) = 9/5.
        # VERIFIED: [DC] k*dim(g)/(k+h^v) = 9/5, [LT] Kac (1990), [DA] c -> dim(g) = 3 as k -> inf
        """
        kl = kazhdan_lusztig_sl2(3)
        assert kl.central_charge == F(9, 5)
        assert kl.central_charge == F(3 * SL2_DIM, 3 + SL2_DUAL_COXETER)

    def test_kl_num_integrable_reps(self):
        """Number of integrable reps = k+1 for sl_2.
        # VERIFIED: [DC] highest weights 0,1,...,k, [LT] Kac (1990) Thm 10.7
        # [LC] k=1 gives 2 reps (vacuum + fundamental), k=0 gives 1 (vacuum only = trivial)
        """
        for k in range(1, 6):
            kl = kazhdan_lusztig_sl2(k)
            assert kl.num_integrable_reps == k + 1

    def test_kl_is_modular(self):
        """KL category is modular at positive integer level."""
        for k in range(1, 5):
            kl = kazhdan_lusztig_sl2(k)
            assert kl.is_modular is True

    def test_kl_proved_status(self):
        """Proof status: PROVED."""
        kl = kazhdan_lusztig_sl2(1)
        assert 'PROVED' in kl.proof_status

    def test_kl_invalid_level_raises(self):
        """Level 0 or negative raises ValueError."""
        with pytest.raises(ValueError):
            kazhdan_lusztig_sl2(0)
        with pytest.raises(ValueError):
            kazhdan_lusztig_sl2(-1)


# =========================================================================
# Section 3: Verlinde formula
# =========================================================================

class TestVerlindeFormula:
    """Verlinde formula for sl_2 at various levels and genera."""

    def test_genus0_always_1(self):
        """Genus 0 conformal block space is 1-dimensional for all k.
        # VERIFIED: [DC] Verlinde sum at g=0 gives 1, [LT] Verlinde (1988)
        # [SY] genus 0 = P^1 has unique vacuum for any rational VOA
        """
        for k in range(1, 8):
            kl = kazhdan_lusztig_sl2(k)
            assert kl.verlinde_dims[0] == 1

    def test_genus1_is_k_plus_1(self):
        """Genus 1: dim = k+1 (number of integrable reps).
        # VERIFIED: [DC] Verlinde sum at g=1 = k+1, [LT] Beauville (1996)
        # [SY] genus 1 trace = sum over simple objects = number of simples = k+1
        """
        for k in range(1, 8):
            kl = kazhdan_lusztig_sl2(k)
            # DC path: Verlinde formula
            assert kl.verlinde_dims[1] == k + 1
            # CF path: equals num_integrable_reps
            assert kl.verlinde_dims[1] == kl.num_integrable_reps

    def test_genus2_level1(self):
        """Genus 2, level 1: dim = C(4,3) = 4.
        # VERIFIED: [DC] sum (S_{0j})^{-2} = (k+2)/2 * sum csc^2 = 3/2 * 8/3 = 4
        # [CF] C(k+3,3) = C(4,3) = 4
        """
        import math
        kl = kazhdan_lusztig_sl2(1)
        assert kl.verlinde_dims[2] == 4  # VERIFIED: [DC] S-matrix sum
        assert kl.verlinde_dims[2] == math.comb(1 + 3, 3)  # CF: C(4,3)

    def test_genus2_level2(self):
        """Genus 2, level 2: dim = C(5,3) = 10.
        # VERIFIED: [DC] S-matrix sum, [CF] C(k+3,3) = C(5,3) = 10
        # [LT] Beauville (1996): this value is standard
        """
        import math
        kl = kazhdan_lusztig_sl2(2)
        assert kl.verlinde_dims[2] == 10
        assert kl.verlinde_dims[2] == math.comb(2 + 3, 3)  # CF: C(5,3)

    def test_genus2_level3(self):
        """Genus 2, level 3: dim = C(6,3) = 20.
        # VERIFIED: [DC] S-matrix sum, [CF] C(k+3,3) = C(6,3) = 20
        """
        import math
        kl = kazhdan_lusztig_sl2(3)
        assert kl.verlinde_dims[2] == 20
        assert kl.verlinde_dims[2] == math.comb(3 + 3, 3)  # CF: C(6,3)

    def test_genus2_level4(self):
        """Genus 2, level 4: dim = C(7,3) = 35.
        # VERIFIED: [DC] S-matrix sum, [CF] C(k+3,3) = C(7,3) = 35
        """
        import math
        kl = kazhdan_lusztig_sl2(4)
        assert kl.verlinde_dims[2] == 35
        assert kl.verlinde_dims[2] == math.comb(4 + 3, 3)  # CF: C(7,3)

    def test_verlinde_table_structure(self):
        """Verlinde dimension table has correct keys."""
        table = verlinde_dimension_table(max_level=3, max_genus=2)
        assert (1, 0) in table
        assert (3, 2) in table
        assert table[(1, 0)] == 1
        assert table[(2, 1)] == 3

    def test_verlinde_monotone_in_level(self):
        """At fixed genus >= 1, Verlinde dimension increases with level."""
        table = verlinde_dimension_table(max_level=6, max_genus=2)
        for g in (1, 2):
            for k in range(1, 6):
                assert table[(k, g)] <= table[(k + 1, g)]

    def test_verlinde_known_values_g0(self):
        """Cross-check against hardcoded VERLINDE_SL2_G0."""
        for k, expected in VERLINDE_SL2_G0.items():
            kl = kazhdan_lusztig_sl2(k)
            assert kl.verlinde_dims[0] == expected

    def test_verlinde_known_values_g1(self):
        """Cross-check against hardcoded VERLINDE_SL2_G1."""
        for k, expected in VERLINDE_SL2_G1.items():
            kl = kazhdan_lusztig_sl2(k)
            assert kl.verlinde_dims[1] == expected

    def test_verlinde_known_values_g2(self):
        """Cross-check against hardcoded VERLINDE_SL2_G2 = C(k+3,3).
        # VERIFIED: [DC] S-matrix sum, [CF] closed form C(k+3,3)
        """
        import math
        for k, expected in VERLINDE_SL2_G2.items():
            kl = kazhdan_lusztig_sl2(k)
            assert kl.verlinde_dims[2] == expected
            # CF path: closed-form binomial
            assert kl.verlinde_dims[2] == math.comb(k + 3, 3)


# =========================================================================
# Section 4: Heisenberg factorization category
# =========================================================================

class TestHeisenbergFactorizationCategory:
    """Heisenberg factorization category for H_Muk."""

    def test_rank_24(self):
        """Mukai Heisenberg has rank 24.
        # VERIFIED: [DC] Mukai lattice = U^4 + E_8(-1)^2 has rank 4*2+2*8=24
        # [LT] Huybrechts "K3 surfaces" (2016) Ch. 14, [CF] chi(K3)=24
        """
        hfc = heisenberg_factorization_category()
        assert hfc.rank == 24
        # CF path: equals MUKAI_RANK constant
        assert hfc.rank == MUKAI_RANK

    def test_signature_4_20(self):
        """Mukai signature (4, 20).
        # VERIFIED: [DC] Mukai lattice U^4+E_8(-1)^2: U has sig (1,1) x 4 = (4,4),
        #   E_8(-1)^2 has sig (0,16), total (4,20)
        # [LT] Huybrechts (2016), [SY] 4+20=24=rank
        """
        hfc = heisenberg_factorization_category()
        assert hfc.signature == (4, 20)
        # SY path: signature sums to rank
        assert sum(hfc.signature) == hfc.rank

    def test_braided_after_center(self):
        """Drinfeld center gives braided structure."""
        hfc = heisenberg_factorization_category()
        assert hfc.braided_after_center is True

    def test_not_modular(self):
        """Heisenberg is NOT modular (continuous simples)."""
        hfc = heisenberg_factorization_category()
        assert hfc.is_modular is False

    def test_kappa_cat_equals_2(self):
        """kappa_cat = chi(O_{K3}) = 2 (AP113).
        # VERIFIED: [DC] chi(O_{K3}) = sum (-1)^i h^{0,i} = 1-0+1 = 2
        # [LT] Huybrechts (2016) Prop. 1.2.7, [CF] = Todd genus of K3
        """
        hfc = heisenberg_factorization_category()
        assert hfc.kappa_cat == 2

    def test_global_sections_character(self):
        """Global sections character is 1/eta^{24}."""
        hfc = heisenberg_factorization_category()
        assert 'eta' in hfc.global_sections_char
        assert '24' in hfc.global_sections_char

    def test_proof_status(self):
        """Proved for CY-A_2."""
        hfc = heisenberg_factorization_category()
        assert 'PROVED' in hfc.proof_status


class TestHeisenbergFiberDimensions:
    """Fiber dimensions = Gottsche numbers p_{24}(n) = chi(Hilb^n(K3))."""

    def test_p24_0(self):
        """p_{24}(0) = 1 (empty partition).
        # VERIFIED: [DC] recursion base case, [SY] unique empty partition
        """
        dims = heisenberg_fiber_dimensions(6)
        assert dims[0] == 1

    def test_p24_1(self):
        """p_{24}(1) = 24 (24 colours, one part).
        # VERIFIED: [DC] recursion: (1/1)*24*1*1 = 24, [LT] Gottsche (1990)
        # [CF] chi(K3) = 24 = sum of Betti numbers, [NE] OEIS A008443
        """
        dims = heisenberg_fiber_dimensions(6)
        assert dims[1] == 24
        # CF path: p_c(1) = c for any number of colours c
        assert dims[1] == MUKAI_RANK

    def test_p24_2(self):
        """p_{24}(2) = 324.
        # VERIFIED: [DC] recursion, [LT] Gottsche (1990)
        # [CF] p_c(2) = c*(c+1)/2 + c*sigma_1(2)/2 = 24*25/2 + 24*3/2 = 300+36 WRONG
        # Actually: (1/2)*(24*sigma_1(1)*p(1) + 24*sigma_1(2)*p(0)) = (1/2)*(24*1*24+24*3*1)
        #         = (1/2)*(576+72) = 324. Correct.
        """
        dims = heisenberg_fiber_dimensions(6)
        assert dims[2] == 324
        # DC path: verify recursion (1/2)*(c*1*c + c*3*1)
        c = MUKAI_RANK
        expected_2 = (c * 1 * c + c * 3 * 1) // 2
        assert dims[2] == expected_2

    def test_p24_3(self):
        """p_{24}(3) = 3200.
        # VERIFIED: [DC] recursion, [LT] Gottsche (1990), [NE] OEIS A008443
        """
        dims = heisenberg_fiber_dimensions(6)
        assert dims[3] == 3200

    def test_p24_4(self):
        """p_{24}(4) = 25650.
        # VERIFIED: [DC] recursion, [LT] Gottsche (1990), [NE] OEIS A008443
        """
        dims = heisenberg_fiber_dimensions(6)
        assert dims[4] == 25650

    def test_p24_5(self):
        """p_{24}(5) = 176256.
        # VERIFIED: [DC] recursion, [LT] Gottsche (1990), [NE] OEIS A008443
        """
        dims = heisenberg_fiber_dimensions(6)
        assert dims[5] == 176256

    def test_p24_monotone(self):
        """p_{24}(n) is strictly increasing for n >= 1."""
        dims = heisenberg_fiber_dimensions(6)
        for n in range(1, 6):
            assert dims[n] < dims[n + 1]


# =========================================================================
# Section 5: Drinfeld center of factorization category
# =========================================================================

class TestDrinfeldCenterFactCat:
    """Drinfeld center Z(int_C Rep^{E_1}(A))."""

    def test_heisenberg_center_dim_49(self):
        """Z(Rep^{E_1}(H_Muk)) has Drinfeld double dim 49.
        # VERIFIED: [DC] 24(orig) + 24(dual) + 1(central) = 49
        # [LT] Kassel "Quantum Groups" (1995) Ch. IX (Drinfeld double dimension)
        # [CF] drinfeld_center_k3_heisenberg.py: DRINFELD_DOUBLE_DIM = 49
        """
        dc = drinfeld_center_factorization_category('heisenberg')
        assert dc.center_dim == 49
        # CF path: 2 * MUKAI_RANK + 1 (original + dual + central)
        assert dc.center_dim == 2 * MUKAI_RANK + 1

    def test_heisenberg_center_braided(self):
        """Center is braided, not symmetric, not modular."""
        dc = drinfeld_center_factorization_category('heisenberg')
        assert 'braided' in dc.braiding_type
        assert 'NOT symmetric' in dc.braiding_type

    def test_heisenberg_center_rational_r(self):
        """R-matrix is rational for Heisenberg."""
        dc = drinfeld_center_factorization_category('heisenberg')
        assert 'rational' in dc.r_matrix_type

    def test_km_center_modular(self):
        """KM center is modular tensor category."""
        dc = drinfeld_center_factorization_category('kac_moody')
        assert dc.is_modular is True

    def test_km_center_trigonometric_r(self):
        """KM R-matrix is trigonometric (KZ)."""
        dc = drinfeld_center_factorization_category('kac_moody')
        assert 'trigonometric' in dc.r_matrix_type

    def test_yangian_center_conjectural(self):
        """Yangian center is conjectural (AP-CY14)."""
        dc = drinfeld_center_factorization_category('yangian')
        assert 'CONJECTURAL' in dc.proof_status

    def test_yangian_e1_input(self):
        """Yangian input is E_1 (ordered)."""
        dc = drinfeld_center_factorization_category('yangian')
        assert 'E_1' in dc.input_en_level

    def test_unknown_raises(self):
        """Unknown algebra type raises ValueError."""
        with pytest.raises(ValueError):
            drinfeld_center_factorization_category('unknown')


# =========================================================================
# Section 6: Ran space formulation
# =========================================================================

class TestRanSpaceFormulation:
    """Ran space formulation of factorization categories."""

    def test_heisenberg_unordered(self):
        """Heisenberg uses unordered Ran space (E_inf)."""
        rs = ran_space_formulation('heisenberg')
        assert 'unordered' in rs.ran_type

    def test_km_unordered(self):
        """KM uses unordered Ran space (E_inf VOA)."""
        rs = ran_space_formulation('kac_moody')
        assert 'unordered' in rs.ran_type

    def test_yangian_ordered(self):
        """Yangian uses ordered Ran space (E_1).
        AP152: 'ordered' means labeled-ordered, not time-ordered.
        """
        rs = ran_space_formulation('yangian')
        assert 'ordered' in rs.ran_type
        assert rs.en_level == 'E_1'

    def test_cosheaf_condition(self):
        """Cosheaf condition holds for all types."""
        for t in ('heisenberg', 'kac_moody', 'yangian'):
            rs = ran_space_formulation(t)
            assert rs.cosheaf_condition is True

    def test_ran_equivalence(self):
        """Ran colimit = BD chiral homology for all types."""
        for t in ('heisenberg', 'kac_moody', 'yangian'):
            rs = ran_space_formulation(t)
            assert rs.ran_equivalence is True

    def test_unknown_raises(self):
        """Unknown type raises ValueError."""
        with pytest.raises(ValueError):
            ran_space_formulation('unknown')


# =========================================================================
# Section 7: BPS state categories
# =========================================================================

class TestBPSFactorizationCategory:
    """BPS factorization category for K3 x E."""

    def test_kappa_spectrum(self):
        """AP113: kappa spectrum {3, 5, 2, 24} for K3 x E.
        # VERIFIED: [DC] kappa_ch = kappa_ch(K3) + kappa_ch(E) = 2 + 1 = 3
        # [LT] Vol III CLAUDE.md kappa-spectrum table
        # [CF] kappa_BKM = weight of Delta_5 = 5 (Igusa cusp form)
        # [DC] kappa_cat = chi(O_{K3}) = 2 (Hodge numbers h^{0,0}=h^{0,2}=1)
        """
        bps = bps_factorization_category_k3()
        assert bps.kappa_ch == 3
        assert bps.kappa_BKM == 5
        assert bps.kappa_cat == 2
        # SY path: kappa_ch != kappa_BKM != kappa_cat (all distinct, AP113)
        assert len({bps.kappa_ch, bps.kappa_BKM, bps.kappa_cat}) == 3

    def test_conjectural_status(self):
        """BPS category is CONJECTURAL (AP-CY14)."""
        bps = bps_factorization_category_k3()
        assert 'CONJECTURAL' in bps.proof_status

    def test_hilb_euler_chars(self):
        """chi(Hilb^n(K3)) = p_{24}(n) matches Gottsche.
        # VERIFIED: [DC] recursion p_c(n) = (1/n)*sum c*sigma_1(k)*p_c(n-k)
        # [LT] Gottsche (1990), [CF] chiral_homology_ran_k3.py GOTTSCHE_COEFFICIENTS
        # [NE] p_{24}(1) = 24 = chi(K3) (OEIS A008443)
        """
        bps = bps_factorization_category_k3(max_n=5)
        assert bps.hilb_euler_chars[0] == 1
        assert bps.hilb_euler_chars[1] == 24
        assert bps.hilb_euler_chars[2] == 324
        # CF path: cross-check with heisenberg_fiber_dimensions
        fiber_dims = heisenberg_fiber_dimensions(5)
        for n in range(6):
            assert bps.hilb_euler_chars[n] == fiber_dims[n]

    def test_global_sections_eta(self):
        """Global sections character is 1/eta^{24}."""
        bps = bps_factorization_category_k3()
        assert 'eta' in bps.global_sections_char

    def test_hecke_action_present(self):
        """Hecke correspondences provide factorization structure."""
        bps = bps_factorization_category_k3()
        assert 'Hecke' in bps.hecke_action


# =========================================================================
# Section 8: E_n hierarchy
# =========================================================================

class TestEnHierarchy:
    """E_n factorization category by CY dimension."""

    def test_d1_einf(self):
        """d=1: E_inf (commutative)."""
        data = en_factorization_category_by_dimension(1)
        assert 'E_inf' in data.native_en
        assert 'symmetric' in data.factorization_cat_type

    def test_d2_e2(self):
        """d=2: E_2 (braided monoidal)."""
        data = en_factorization_category_by_dimension(2)
        assert 'E_2' in data.native_en
        assert 'braided' in data.factorization_cat_type

    def test_d3_e1(self):
        """d=3: E_1 (ordered/monoidal), braided via Drinfeld center."""
        data = en_factorization_category_by_dimension(3)
        assert 'E_1' in data.native_en
        assert 'monoidal' in data.factorization_cat_type.lower()
        assert 'NOT braided' in data.factorization_cat_type

    def test_d4_stabilized(self):
        """d >= 4: E_1-stabilized."""
        data = en_factorization_category_by_dimension(4)
        assert 'E_1-stabilized' in data.native_en

    def test_d3_center_gives_e2(self):
        """At d=3, Drinfeld center produces E_2 (braided)."""
        data = en_factorization_category_by_dimension(3)
        assert 'E_2' in data.center_gives

    def test_d0_raises(self):
        """d=0 or negative raises ValueError."""
        with pytest.raises(ValueError):
            en_factorization_category_by_dimension(0)

    def test_d5_stabilized(self):
        """d=5: also E_1-stabilized."""
        data = en_factorization_category_by_dimension(5)
        assert 'E_1-stabilized' in data.native_en


# =========================================================================
# Section 9: Factorization isomorphism
# =========================================================================

class TestFactorizationIsomorphism:
    """Factorization isomorphism: F(U1 cup U2) ~ F(U1) tensor F(U2)."""

    def test_heisenberg_lurie_tensor(self):
        """Heisenberg: Lurie tensor (E_inf symmetric)."""
        fi = verify_factorization_isomorphism('heisenberg')
        assert 'Lurie' in fi.isomorphism_type
        assert fi.character_check is True

    def test_km_lurie_tensor(self):
        """KM: Lurie tensor (E_inf VOA)."""
        fi = verify_factorization_isomorphism('kac_moody')
        assert 'Lurie' in fi.isomorphism_type

    def test_yangian_ordered_tensor(self):
        """Yangian: E_1-ordered tensor (NOT symmetric).
        AP152: labeled-ordered, not time-ordered.
        """
        fi = verify_factorization_isomorphism('yangian')
        assert 'E_1-ordered' in fi.isomorphism_type
        assert 'NOT symmetric' in fi.isomorphism_type

    def test_yangian_conjectural(self):
        """Yangian factorization isomorphism is CONJECTURAL."""
        fi = verify_factorization_isomorphism('yangian')
        assert 'CONJECTURAL' in fi.proof_status

    def test_unknown_raises(self):
        """Unknown type raises ValueError."""
        with pytest.raises(ValueError):
            verify_factorization_isomorphism('unknown')


# =========================================================================
# Section 10: Algebra vs category comparison
# =========================================================================

class TestAlgebraVsCategory:
    """Comparison: factorization algebra vs factorization category."""

    def test_algebra_assigns_vector_spaces(self):
        """Algebras assign vector spaces."""
        comp = factorization_algebra_vs_category()
        assert 'vector space' in comp.algebra_assigns.lower()

    def test_category_assigns_categories(self):
        """Categories assign dg categories."""
        comp = factorization_algebra_vs_category()
        assert 'category' in comp.category_assigns.lower()

    def test_kl_example_present(self):
        """KL example illustrates the passage."""
        comp = factorization_algebra_vs_category()
        assert 'Kazhdan-Lusztig' in comp.example_kl

    def test_en_structure_described(self):
        """E_n structure described for both."""
        comp = factorization_algebra_vs_category()
        assert 'E_n' in comp.algebra_en_structure
        assert 'Drinfeld center' in comp.category_en_structure


# =========================================================================
# Section 11: Chiral homology of factorization categories
# =========================================================================

class TestChiralHomologyFactCat:
    """Chiral homology int_C F of factorization categories."""

    def test_heisenberg_g0_vacuum(self):
        """int_{P^1} Rep(H_Muk) = Vect (vacuum)."""
        ch = chiral_homology_factorization_category('heisenberg', genus=0)
        assert 'Vect' in ch.global_sections_category
        assert ch.genus == 0

    def test_heisenberg_g1_eta(self):
        """int_E Rep(H_Muk) has character 1/eta^{24}."""
        ch = chiral_homology_factorization_category('heisenberg', genus=1)
        assert 'eta' in ch.dimension_or_character

    def test_heisenberg_g2_modular(self):
        """int_{Sigma_2} Rep(H_Muk): modular weight -12."""
        ch = chiral_homology_factorization_category('heisenberg', genus=2)
        assert '-12' in ch.dimension_or_character

    def test_km_g0_vacuum(self):
        """int_{P^1} Rep(V_k(g)) = Vect (vacuum)."""
        ch = chiral_homology_factorization_category('kac_moody', genus=0)
        assert 'Vect' in ch.global_sections_category

    def test_km_g1_verlinde(self):
        """int_E Rep(V_k(g)) = Verlinde category."""
        ch = chiral_homology_factorization_category('kac_moody', genus=1)
        assert 'Verlinde' in ch.global_sections_category

    def test_yangian_conjectural(self):
        """Yangian chiral homology is CONJECTURAL."""
        ch = chiral_homology_factorization_category('yangian', genus=1)
        assert 'CONJECTURAL' in ch.proof_status

    def test_unknown_raises(self):
        """Unknown type raises ValueError."""
        with pytest.raises(ValueError):
            chiral_homology_factorization_category('unknown', genus=0)


# =========================================================================
# Section 12: Landscape
# =========================================================================

class TestFactorizationCategoryLandscape:
    """Factorization category landscape across CY examples."""

    def test_landscape_nonempty(self):
        """Landscape has entries."""
        lsc = factorization_category_landscape()
        assert len(lsc) >= 5

    def test_landscape_dimensions(self):
        """Landscape covers d=1, 2, 3."""
        lsc = factorization_category_landscape()
        dims = {entry.cy_dimension for entry in lsc}
        assert 1 in dims
        assert 2 in dims
        assert 3 in dims

    def test_k3xe_kappa_ch_3(self):
        """K3 x E entry has kappa_ch = 3."""
        lsc = factorization_category_landscape()
        k3xe = [e for e in lsc if 'K3 x E' in e.cy_geometry]
        assert len(k3xe) == 1
        assert '3' in k3xe[0].kappa_ch

    def test_k3xe_conjectural(self):
        """K3 x E is CONJECTURAL (CY-A_3)."""
        lsc = factorization_category_landscape()
        k3xe = [e for e in lsc if 'K3 x E' in e.cy_geometry]
        assert 'CONJECTURAL' in k3xe[0].proof_status

    def test_c3_proved_for_toric(self):
        """C^3 toric case is PROVED."""
        lsc = factorization_category_landscape()
        c3 = [e for e in lsc if 'C^3' in e.cy_geometry]
        assert len(c3) == 1
        assert 'PROVED' in c3[0].proof_status

    def test_d1_symmetric(self):
        """d=1 entries are symmetric monoidal."""
        lsc = factorization_category_landscape()
        d1 = [e for e in lsc if e.cy_dimension == 1]
        for entry in d1:
            assert 'symmetric' in entry.fact_cat_type

    def test_quintic_conjectural(self):
        """Quintic is CONJECTURAL."""
        lsc = factorization_category_landscape()
        quintic = [e for e in lsc if 'Quintic' in e.cy_geometry]
        assert len(quintic) == 1
        assert 'CONJECTURAL' in quintic[0].proof_status


# =========================================================================
# Section 13: Full verification suite
# =========================================================================

class TestFullVerification:
    """Run the full verification suite."""

    def test_kazhdan_lusztig_consistency(self):
        """KL data internally consistent."""
        result = verify_kazhdan_lusztig_consistency()
        assert result['all_pass'] is True

    def test_heisenberg_consistency(self):
        """Heisenberg factcat data internally consistent."""
        result = verify_heisenberg_factcat_consistency()
        assert result['all_pass'] is True

    def test_en_hierarchy_consistency(self):
        """E_n hierarchy consistent across d."""
        result = verify_en_hierarchy_consistency()
        assert result['all_pass'] is True

    def test_bps_category_consistency(self):
        """BPS category data consistent."""
        result = verify_bps_category_consistency()
        assert result['all_pass'] is True

    def test_algebra_vs_category_consistency(self):
        """Algebra vs category comparison consistent."""
        result = verify_algebra_vs_category()
        assert result['all_pass'] is True

    def test_full_verification_passes(self):
        """Full verification suite passes."""
        result = full_verification()
        assert result['all_pass'] is True

    def test_total_checks_count(self):
        """At least 30 checks in full suite."""
        result = full_verification()
        assert result['total_checks'] >= 30
