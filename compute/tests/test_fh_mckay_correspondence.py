r"""Tests for the factorization-homology McKay correspondence.

Verifies the FH McKay correspondence conjecture at the level of:
  - Ranks (graded dimensions)
  - Lattice structure (intersection forms, Cartan matrices)
  - Link cohomology (vanishing of H^2 for all ADE types)
  - K-theory comparison
  - Characters (convolution identity)
  - Application to Kummer Step 5

for ALL ADE types: A_1, A_2, A_3, A_4, D_4, D_5, D_6, E_6, E_7, E_8.

~100 tests covering 8 verification paths.
"""

import pytest
from fractions import Fraction as F

from compute.lib.fh_mckay_correspondence import (
    ADE_TYPES,
    ADEData,
    ade_data,
    orbifold_fh,
    resolution_fh,
    fh_mckay_comparison,
    a1_detailed_comparison,
    degree_graded_ade,
    character_comparison_a1,
    kummer_fh_mckay,
    cartan_matrix_properties,
    link_cohomology,
    full_fh_mckay_verification,
)


# =========================================================================
# 1. ADE data verification
# =========================================================================

class TestADEData:
    """Verify ADE singularity data is correct."""

    def test_a1_group_order(self):
        """A_1 = Z/2, order 2."""
        assert ade_data('A1').group_order == 2

    def test_a2_group_order(self):
        """A_2 = Z/3, order 3."""
        assert ade_data('A2').group_order == 3

    def test_a3_group_order(self):
        """A_3 = Z/4, order 4."""
        assert ade_data('A3').group_order == 4

    def test_a4_group_order(self):
        """A_4 = Z/5, order 5."""
        assert ade_data('A4').group_order == 5

    def test_d4_group_order(self):
        """D_4 = BD_8 (binary dihedral), order 8."""
        assert ade_data('D4').group_order == 8

    def test_d5_group_order(self):
        """D_5 = BD_12, order 12."""
        assert ade_data('D5').group_order == 12

    def test_d6_group_order(self):
        """D_6 = BD_16, order 16."""
        assert ade_data('D6').group_order == 16

    def test_e6_group_order(self):
        """E_6 = binary tetrahedral, order 24."""
        assert ade_data('E6').group_order == 24

    def test_e7_group_order(self):
        """E_7 = binary octahedral, order 48."""
        assert ade_data('E7').group_order == 48

    def test_e8_group_order(self):
        """E_8 = binary icosahedral, order 120."""
        assert ade_data('E8').group_order == 120

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_mckay_theorem(self, type_name):
        """McKay's theorem: |Conj(G)| = rank + 1 for all ADE types."""
        ade = ade_data(type_name)
        assert ade.num_conjugacy_classes == ade.root_system_rank + 1

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_exceptional_curves_equals_rank(self, type_name):
        """Number of exceptional CP^1's equals root system rank."""
        ade = ade_data(type_name)
        assert ade.exceptional_curves == ade.root_system_rank


# =========================================================================
# 2. McKay rank match (the core theorem)
# =========================================================================

class TestFHMcKayRankMatch:
    """The FH McKay correspondence: rank match for all ADE types."""

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_rank_match(self, type_name):
        """Orbifold rank = resolution rank for all ADE types."""
        ade = ade_data(type_name)
        result = fh_mckay_comparison(ade)
        assert result.ranks_match, (
            f"{type_name}: orbifold rank {result.orbifold_rank} != "
            f"resolution rank {result.resolution_rank}"
        )

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_orbifold_rank_is_r_plus_1(self, type_name):
        """Orbifold rank = r + 1 = |Conj(G)|."""
        ade = ade_data(type_name)
        orb = orbifold_fh(ade)
        assert orb.total_rank == ade.root_system_rank + 1

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_resolution_rank_is_r_plus_1(self, type_name):
        """Resolution rank = 1 + 2r - r = r + 1."""
        ade = ade_data(type_name)
        res = resolution_fh(ade)
        assert res.total_rank == ade.root_system_rank + 1

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_orbifold_untwisted_rank_1(self, type_name):
        """Untwisted sector has rank 1 for all types."""
        ade = ade_data(type_name)
        orb = orbifold_fh(ade)
        assert orb.untwisted_rank == 1

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_orbifold_twisted_sectors_count(self, type_name):
        """Number of twisted sectors = |Conj(G)| - 1 = r."""
        ade = ade_data(type_name)
        orb = orbifold_fh(ade)
        assert orb.num_twisted_sectors == ade.root_system_rank


# =========================================================================
# 3. Resolution excision data
# =========================================================================

class TestResolutionExcision:
    """Resolution FH via Mayer-Vietoris excision."""

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_base_rank_1(self, type_name):
        """Base (complement) contributes rank 1."""
        ade = ade_data(type_name)
        res = resolution_fh(ade)
        assert res.base_rank == 1

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_cp1_rank_2(self, type_name):
        """Each exceptional CP^1 contributes rank 2."""
        ade = ade_data(type_name)
        res = resolution_fh(ade)
        assert res.cp1_rank_per_curve == 2

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_exceptional_total(self, type_name):
        """Total exceptional rank = 2 * r."""
        ade = ade_data(type_name)
        res = resolution_fh(ade)
        assert res.exceptional_rank_total == 2 * ade.root_system_rank

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_boundary_relations(self, type_name):
        """Boundary relations = r (one per curve)."""
        ade = ade_data(type_name)
        res = resolution_fh(ade)
        assert res.boundary_relations == ade.root_system_rank

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_mv_arithmetic(self, type_name):
        """MV arithmetic: 1 + 2r - r = 1 + r."""
        ade = ade_data(type_name)
        res = resolution_fh(ade)
        r = ade.root_system_rank
        assert res.total_rank == 1 + 2 * r - r == 1 + r


# =========================================================================
# 4. Cartan matrix properties
# =========================================================================

class TestCartanMatrix:
    """Properties of ADE Cartan matrices."""

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_symmetric(self, type_name):
        """ADE Cartan matrices are symmetric (simply-laced)."""
        ade = ade_data(type_name)
        props = cartan_matrix_properties(ade)
        assert props['symmetric']

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_diagonal_is_2(self, type_name):
        """All diagonal entries are 2."""
        ade = ade_data(type_name)
        props = cartan_matrix_properties(ade)
        assert props['diagonal_is_2']

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_simply_laced(self, type_name):
        """Off-diagonal entries are 0 or -1."""
        ade = ade_data(type_name)
        props = cartan_matrix_properties(ade)
        assert props['simply_laced']

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_determinant(self, type_name):
        """Determinant matches known values."""
        ade = ade_data(type_name)
        props = cartan_matrix_properties(ade)
        assert props['determinant_correct'], (
            f"{type_name}: det = {props['determinant']}, "
            f"expected {props['expected_determinant']}"
        )

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_positive_definite(self, type_name):
        """Cartan matrix is positive definite."""
        ade = ade_data(type_name)
        props = cartan_matrix_properties(ade)
        assert props['positive_definite']

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_is_tree(self, type_name):
        """Dynkin diagram is a tree (r-1 edges for r nodes)."""
        ade = ade_data(type_name)
        props = cartan_matrix_properties(ade)
        assert props['is_tree']

    def test_a1_det_is_2(self):
        """det(C_{A_1}) = 2."""
        props = cartan_matrix_properties(ade_data('A1'))
        assert props['determinant'] == 2

    def test_d4_det_is_4(self):
        """det(C_{D_4}) = 4."""
        props = cartan_matrix_properties(ade_data('D4'))
        assert props['determinant'] == 4

    def test_e6_det_is_3(self):
        """det(C_{E_6}) = 3."""
        props = cartan_matrix_properties(ade_data('E6'))
        assert props['determinant'] == 3

    def test_e7_det_is_2(self):
        """det(C_{E_7}) = 2."""
        props = cartan_matrix_properties(ade_data('E7'))
        assert props['determinant'] == 2

    def test_e8_det_is_1(self):
        """det(C_{E_8}) = 1 (E_8 is unimodular)."""
        props = cartan_matrix_properties(ade_data('E8'))
        assert props['determinant'] == 1


# =========================================================================
# 5. Intersection form on exceptional locus
# =========================================================================

class TestIntersectionForm:
    """Intersection form on exceptional curves = negative Cartan."""

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_negative_definite(self, type_name):
        """Intersection form is negative definite for all ADE types."""
        ade = ade_data(type_name)
        result = fh_mckay_comparison(ade)
        assert result.is_negative_definite

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_self_intersection_minus_2(self, type_name):
        """All exceptional curves have self-intersection -2."""
        ade = ade_data(type_name)
        res = resolution_fh(ade)
        for i in range(ade.root_system_rank):
            assert res.exceptional_intersection[i][i] == -2


# =========================================================================
# 6. Link cohomology
# =========================================================================

class TestLinkCohomology:
    """Cohomology of the link S^3/G."""

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_h0_is_1(self, type_name):
        """H^0(S^3/G; C) = C."""
        link = link_cohomology(ade_data(type_name))
        assert link.h0 == 1

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_h1_is_0(self, type_name):
        """H^1(S^3/G; C) = 0 (finite torsion killed over C)."""
        link = link_cohomology(ade_data(type_name))
        assert link.h1 == 0

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_h2_is_0(self, type_name):
        """H^2(S^3/G; C) = 0 (Poincare duality + H^1 = 0).

        This is the KEY FACT: it ensures no degree-2 boundary relations
        in the Mayer-Vietoris sequence, so all exceptional H^2(CP^1)
        generators survive.
        """
        link = link_cohomology(ade_data(type_name))
        assert link.h2 == 0

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_h3_is_1(self, type_name):
        """H^3(S^3/G; C) = C (fundamental class)."""
        link = link_cohomology(ade_data(type_name))
        assert link.h3 == 1

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_total_rank_2(self, type_name):
        """Total rational cohomological rank of S^3/G is 2."""
        link = link_cohomology(ade_data(type_name))
        assert link.total_rank == 2

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_orientation_preserved(self, type_name):
        """All elements of SL_2(C) preserve orientation on S^3."""
        link = link_cohomology(ade_data(type_name))
        assert link.orientation_preserved

    def test_a1_h1_torsion(self):
        """H_1(S^3/Z_2; Z) = Z/2."""
        link = link_cohomology(ade_data('A1'))
        assert link.h1_integral_torsion == "Z/2"

    def test_e8_h1_trivial(self):
        """H_1(S^3/BI; Z) = trivial (binary icosahedral is perfect)."""
        link = link_cohomology(ade_data('E8'))
        assert "trivial" in link.h1_integral_torsion


# =========================================================================
# 7. Degree-graded decomposition
# =========================================================================

class TestDegreeGraded:
    """Degree-graded Mayer-Vietoris for ADE resolutions."""

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_degree_0_total_is_1(self, type_name):
        """Degree 0: 1 + r - r = 1 (unique vacuum)."""
        ade = ade_data(type_name)
        deg = degree_graded_ade(ade)
        assert deg.degree_0_total == 1

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_degree_2_total_is_r(self, type_name):
        """Degree 2: r (one surviving generator per exceptional CP^1)."""
        ade = ade_data(type_name)
        deg = degree_graded_ade(ade)
        assert deg.degree_2_total == ade.root_system_rank

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_total_is_r_plus_1(self, type_name):
        """Total = 1 + r = r + 1."""
        ade = ade_data(type_name)
        deg = degree_graded_ade(ade)
        assert deg.total == ade.root_system_rank + 1

    @pytest.mark.parametrize("type_name", ADE_TYPES)
    def test_no_degree_2_boundary_relations(self, type_name):
        """No degree-2 boundary relations (H^2(S^3/G; C) = 0)."""
        ade = ade_data(type_name)
        deg = degree_graded_ade(ade)
        assert deg.degree_2_boundary_relations == 0


# =========================================================================
# 8. A_1 detailed comparison (Kummer building block)
# =========================================================================

class TestA1Detailed:
    """Detailed comparison for A_1 = C^2/Z_2 -> T*CP^1."""

    def test_orbifold_total_rank_2(self):
        """A_1 orbifold has total rank 2."""
        a1 = a1_detailed_comparison()
        assert a1.orb_total_rank == 2

    def test_resolution_total_rank_2(self):
        """A_1 resolution has total rank 2."""
        a1 = a1_detailed_comparison()
        assert a1.res_total_rank == 2

    def test_ranks_match(self):
        """A_1 orbifold and resolution ranks match."""
        a1 = a1_detailed_comparison()
        assert a1.ranks_match

    def test_twisted_weight_half(self):
        """Twisted sector conformal weight h = 1/2."""
        a1 = a1_detailed_comparison()
        assert a1.orb_twisted_weight == F(1, 2)

    def test_mckay_quiver_2_nodes(self):
        """McKay quiver has 2 nodes (trivial + sign rep)."""
        a1 = a1_detailed_comparison()
        assert a1.mckay_quiver_nodes == 2

    def test_k0_match(self):
        """K_0(T*CP^1) = K_0^{Z_2}(C^2) = Z^2."""
        a1 = a1_detailed_comparison()
        assert a1.k0_match

    def test_boundary_relation_1(self):
        """One boundary relation from lens space L(2,1)."""
        a1 = a1_detailed_comparison()
        assert a1.res_boundary_relations == 1

    def test_cp1_rank_2(self):
        """int_{CP^1} H_1 has rank 2."""
        a1 = a1_detailed_comparison()
        assert a1.res_cp1_rank == 2


# =========================================================================
# 9. Conformal weights for A-type twisted sectors
# =========================================================================

class TestConformalWeights:
    """Conformal weights of twisted sectors for A-type singularities."""

    def test_a1_weight(self):
        """A_1: h = 1/2 (matching Kummer Step 3)."""
        orb = orbifold_fh(ade_data('A1'))
        assert orb.conformal_weight_twisted == F(1, 2)

    def test_a2_weight(self):
        """A_2: h = 4/9 (theta_1 = 1/3, theta_2 = 2/3, complex boson convention)."""
        orb = orbifold_fh(ade_data('A2'))
        # h = (1/3)(2/3) + (2/3)(1/3) = 2/9 + 2/9 = 4/9
        assert orb.conformal_weight_twisted == F(4, 9)

    def test_a3_weight(self):
        """A_3: h = 3/8 (theta_1 = 1/4, theta_2 = 3/4, complex boson convention)."""
        orb = orbifold_fh(ade_data('A3'))
        # h = (1/4)(3/4) + (3/4)(1/4) = 3/16 + 3/16 = 3/8
        assert orb.conformal_weight_twisted == F(3, 8)


# =========================================================================
# 10. Character comparison for A_1
# =========================================================================

class TestCharacterA1:
    """Character-level comparison for A_1."""

    def test_convolution_p1_p1_equals_p2(self):
        """p_1 * p_1 = p_2 through q^10 (rank-2 Heisenberg = two rank-1)."""
        result = character_comparison_a1(max_deg=10)
        assert result['convolution_p1_x_p1_matches_p2']

    def test_rank_match(self):
        """Character rank match at the level of generators."""
        result = character_comparison_a1(max_deg=5)
        assert result['rank_match']

    def test_p2_first_coefficients(self):
        """Resolution character p_2: first coefficients 1, 2, 5, 10, 20, 36."""
        result = character_comparison_a1(max_deg=5)
        expected = {0: 1, 1: 2, 2: 5, 3: 10, 4: 20, 5: 36}
        for n, val in expected.items():
            assert result['resolution_character_p2'][n] == val


# =========================================================================
# 11. Kummer global assembly
# =========================================================================

class TestKummerFHMcKay:
    """Application of FH McKay to the Kummer surface."""

    def test_local_match(self):
        """Local A_1 match at each singularity."""
        kummer = kummer_fh_mckay()
        assert kummer.local_match

    def test_global_match(self):
        """Global rank match: both sides give 24."""
        kummer = kummer_fh_mckay()
        assert kummer.global_match

    def test_global_orbifold_rank_24(self):
        """Global orbifold rank = 8 + 16 = 24."""
        kummer = kummer_fh_mckay()
        assert kummer.global_orbifold_rank == 24

    def test_global_resolution_rank_24(self):
        """Global resolution rank = 8 + 32 - 16 = 24."""
        kummer = kummer_fh_mckay()
        assert kummer.global_resolution_rank == 24

    def test_16_singularities(self):
        """Kummer surface has 16 A_1 singularities."""
        kummer = kummer_fh_mckay()
        assert kummer.num_singularities == 16

    def test_complement_rank_8(self):
        """Torus complement contributes rank 8."""
        kummer = kummer_fh_mckay()
        assert kummer.torus_complement_rank == 8

    def test_does_not_bypass_cya3(self):
        """FH McKay does NOT bypass CY-A_3 for d=3.

        Per AP-CY32: reorganisation != bypass. The FH McKay correspondence
        closes Kummer Step 5 at d=2 (where CY-A_2 is proved) but does NOT
        provide an independent route to CY-A_3 at d=3.
        """
        kummer = kummer_fh_mckay()
        assert kummer.bypass_cya3 is False

    def test_step5_rank_proved(self):
        """Step 5 rank is PROVED."""
        kummer = kummer_fh_mckay()
        assert 'PROVED' in kummer.step5_rank_status

    def test_step5_pairing_conditional(self):
        """Step 5 pairing is CONDITIONAL."""
        kummer = kummer_fh_mckay()
        assert 'CONDITIONAL' in kummer.step5_pairing_status


# =========================================================================
# 12. Full verification
# =========================================================================

class TestFullVerification:
    """Full FH McKay verification across all ADE types."""

    def test_all_ranks_match(self):
        """Ranks match for ALL ADE types."""
        result = full_fh_mckay_verification()
        assert result['all_ranks_match']

    def test_all_negative_definite(self):
        """Intersection forms are negative definite for all types."""
        result = full_fh_mckay_verification()
        assert result['all_negative_definite']

    def test_all_determinants_correct(self):
        """Cartan matrix determinants are correct for all types."""
        result = full_fh_mckay_verification()
        assert result['all_determinants_correct']

    def test_all_link_h2_zero(self):
        """H^2(S^3/G; C) = 0 for all ADE types."""
        result = full_fh_mckay_verification()
        assert result['all_link_h2_zero']

    def test_all_pass(self):
        """All verification paths pass."""
        result = full_fh_mckay_verification()
        assert result['summary']['all_pass']

    def test_kummer_global_match(self):
        """Kummer global match passes."""
        result = full_fh_mckay_verification()
        assert result['kummer']['global_match']

    def test_character_convolution(self):
        """Character convolution matches for A_1."""
        result = full_fh_mckay_verification()
        assert result['character_a1']['convolution_match']
