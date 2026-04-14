r"""Tests for the Kummer Step 5 excision decomposition.

Verifies Proposition prop:kummer-step5-excision in cy_to_chiral.tex:
  Step 5a: Local excision at each A_1 singularity (PROVED)
  Step 5b: Global Mayer-Vietoris assembly (PROVED)
  Step 5c: Pairing identification as Mukai (4, 20) (CONDITIONAL)

~70 tests covering:
  - CP^1 factorization homology rank
  - Lens space L(2,1) cohomology and Z_2-action
  - Mayer-Vietoris rank count
  - Degree-graded decomposition matching K3 Betti numbers
  - Lattice classification forcing Mukai signature
  - Euler characteristic cross-checks
  - McKay correspondence consistency
  - Character-level convolution cross-check
"""

import pytest
from fractions import Fraction as F

from compute.lib.kummer_excision_verification import (
    CP1_BETTI,
    CP1_RANK,
    S3_BETTI,
    LENS_BETTI_RATIONAL,
    T4_BETTI,
    T4_EVEN_DIM,
    NUM_FIXED_POINTS,
    K3_TOTAL_DIM,
    K3_HODGE,
    MUKAI_SIGNATURE,
    MUKAI_RANK,
    local_excision_verification,
    lens_space_analysis,
    mayer_vietoris_rank_count,
    lattice_classification,
    euler_characteristic_verification,
    degree_graded_mv,
    mckay_correspondence_check,
    character_cross_check,
    full_excision_verification,
)


# =========================================================================
# Constants
# =========================================================================

class TestTopologicalConstants:
    """Verify topological constants used in the excision analysis."""

    def test_cp1_betti_numbers(self):
        """CP^1 has Betti numbers (1, 0, 1)."""
        assert CP1_BETTI == {0: 1, 1: 0, 2: 1}

    def test_cp1_rank(self):
        """CP^1 total cohomological rank is 2."""
        assert CP1_RANK == 2

    def test_s3_betti_numbers(self):
        """S^3 has Betti numbers (1, 0, 0, 1)."""
        assert S3_BETTI == {0: 1, 1: 0, 2: 0, 3: 1}

    def test_lens_space_rational_betti(self):
        """L(2,1) has rational Betti numbers (1, 0, 0, 1)."""
        assert LENS_BETTI_RATIONAL == {0: 1, 1: 0, 2: 0, 3: 1}

    def test_lens_space_h1_torsion_killed(self):
        """H_1(L(2,1); Z) = Z/2, killed over C."""
        # Over Z: H_1 = Z/2 (torsion from Z_2 quotient)
        # Over C: H^1 = Hom(H_1, C) = 0 (Z/2 has no nonzero C-valued maps)
        assert LENS_BETTI_RATIONAL[1] == 0

    def test_lens_space_h2_vanishes(self):
        """H^2(L(2,1); C) = 0."""
        assert LENS_BETTI_RATIONAL[2] == 0

    def test_t4_even_dim(self):
        """T^4 even cohomology has dimension 8."""
        assert T4_EVEN_DIM == 8

    def test_num_fixed_points(self):
        """Z_2 acting by x -> -x on T^4 has 16 fixed points."""
        assert NUM_FIXED_POINTS == 16

    def test_k3_total_dim(self):
        """dim H^*(K3, C) = 24."""
        assert K3_TOTAL_DIM == 24

    def test_mukai_signature(self):
        """Mukai lattice has signature (4, 20)."""
        assert MUKAI_SIGNATURE == (4, 20)

    def test_mukai_rank(self):
        """Mukai lattice has rank 24."""
        assert MUKAI_RANK == 24


# =========================================================================
# Step 5a: Local excision
# =========================================================================

class TestStep5aLocalExcision:
    """Step 5a: local excision at each A_1 singularity."""

    def test_cp1_rank_is_2(self):
        """int_{CP^1} H_1 = rank-2 Heisenberg."""
        data = local_excision_verification()
        assert data.cp1_rank == 2

    def test_cp1_betti(self):
        """Generators from H^0 and H^2, none from H^1."""
        data = local_excision_verification()
        assert data.cp1_betti[0] == 1
        assert data.cp1_betti.get(1, 0) == 0
        assert data.cp1_betti[2] == 1

    def test_tstar_cp1_retraction(self):
        """T*CP^1 deformation-retracts onto CP^1."""
        data = local_excision_verification()
        assert data.t_star_cp1_retracts is True

    def test_einf_descent(self):
        """E_inf descent applies to H_1 on T*CP^1."""
        data = local_excision_verification()
        assert data.einf_descent_applies is True

    def test_status_proved(self):
        """Step 5a is PROVED."""
        data = local_excision_verification()
        assert data.status == 'PROVED'


# =========================================================================
# Lens space analysis
# =========================================================================

class TestLensSpaceAnalysis:
    """Z_2 action on S^3 and lens space L(2,1) = S^3/Z_2."""

    def test_z2_free_on_s3(self):
        """Z_2 acts freely on S^3 (no fixed points)."""
        data = lens_space_analysis()
        assert data.z2_action_is_free is True

    def test_antipodal_preserves_orientation(self):
        """v -> -v on S^3 subset R^4 has degree +1 (orientation-preserving)."""
        data = lens_space_analysis()
        assert data.z2_action_on_s3[3] == +1

    def test_z2_trivial_on_h0(self):
        """Z_2 acts trivially on H^0(S^3)."""
        data = lens_space_analysis()
        assert data.z2_action_on_s3[0] == +1

    def test_invariant_rank_is_2(self):
        """(H^*(S^3))^{Z_2} has rank 2."""
        data = lens_space_analysis()
        assert data.invariant_rank == 2

    def test_degree_0_relations(self):
        """One degree-0 gluing relation per lens space."""
        data = lens_space_analysis()
        assert data.degree_0_relations == 1

    def test_degree_2_no_relations(self):
        """No degree-2 relations (H^2(L(2,1); C) = 0)."""
        data = lens_space_analysis()
        assert data.degree_2_relations == 0

    def test_degree_3_no_net_relations(self):
        """Degree-3 orientation matching: isomorphism, not net relation."""
        data = lens_space_analysis()
        assert data.degree_3_net_relations == 0

    def test_total_relations_per_point(self):
        """Total: 1 relation per lens space."""
        data = lens_space_analysis()
        assert data.total_relations_per_point == 1


# =========================================================================
# Step 5b: Mayer-Vietoris rank count
# =========================================================================

class TestStep5bMayerVietoris:
    """Step 5b: global Mayer-Vietoris assembly."""

    def test_complement_rank_8(self):
        """Complement has rank 8 (Z_2-even Heisenberg)."""
        data = mayer_vietoris_rank_count()
        assert data.complement_rank == 8

    def test_resolution_rank_per_pt(self):
        """Each resolution patch contributes rank 2."""
        data = mayer_vietoris_rank_count()
        assert data.resolution_rank_per_pt == 2

    def test_resolution_rank_total(self):
        """Total resolution rank: 16 * 2 = 32."""
        data = mayer_vietoris_rank_count()
        assert data.resolution_rank_total == 32

    def test_boundary_rank_per_pt(self):
        """Each boundary contributes 1 relation."""
        data = mayer_vietoris_rank_count()
        assert data.boundary_rank_per_pt == 1

    def test_boundary_rank_total(self):
        """Total boundary relations: 16."""
        data = mayer_vietoris_rank_count()
        assert data.boundary_rank_total == 16

    def test_resolved_rank_24(self):
        """Resolved rank: 8 + 32 - 16 = 24."""
        data = mayer_vietoris_rank_count()
        assert data.resolved_rank == 24

    def test_rank_arithmetic_explicit(self):
        """Cross-check the rank arithmetic."""
        data = mayer_vietoris_rank_count()
        assert (data.complement_rank + data.resolution_rank_total
                - data.boundary_rank_total) == 24

    def test_matches_k3(self):
        """Resolved rank matches K3 total dim."""
        data = mayer_vietoris_rank_count()
        assert data.matches_k3 is True

    def test_status_proved(self):
        """Step 5b is PROVED."""
        data = mayer_vietoris_rank_count()
        assert data.status == 'PROVED'


# =========================================================================
# Degree-graded Mayer-Vietoris
# =========================================================================

class TestDegreeGradedMV:
    """Mayer-Vietoris graded by cohomological degree."""

    def test_degree_0_resolved(self):
        """Degree 0: 1 + 16 - 16 = 1 = b_0(K3)."""
        data = degree_graded_mv()
        assert data.resolved_by_degree[0] == 1

    def test_degree_2_resolved(self):
        """Degree 2: 6 + 16 - 0 = 22 = b_2(K3)."""
        data = degree_graded_mv()
        assert data.resolved_by_degree[2] == 22

    def test_degree_4_resolved(self):
        """Degree 4: 1 + 0 - 0 = 1 = b_4(K3)."""
        data = degree_graded_mv()
        assert data.resolved_by_degree[4] == 1

    def test_total_resolved_24(self):
        """Total resolved rank is 24."""
        data = degree_graded_mv()
        assert data.total_resolved == 24

    def test_matches_k3_betti(self):
        """Resolved degrees match K3 Betti numbers."""
        data = degree_graded_mv()
        assert data.matches_k3_betti is True

    def test_no_odd_degree_generators(self):
        """No generators in odd degrees (K3 has b_1 = b_3 = 0)."""
        data = degree_graded_mv()
        for d in [1, 3]:
            assert data.resolved_by_degree.get(d, 0) == 0

    def test_degree_2_decomposition(self):
        """Degree-2 generators: 6 from torus + 16 from blow-ups."""
        data = degree_graded_mv()
        assert data.complement_by_degree[2] == 6
        assert data.resolution_by_degree[2] == 16
        assert data.boundary_by_degree.get(2, 0) == 0

    def test_degree_0_boundary_kills_redundancy(self):
        """16 degree-0 boundary relations kill 16 redundant constants."""
        data = degree_graded_mv()
        assert data.complement_by_degree[0] == 1
        assert data.resolution_by_degree[0] == 16
        assert data.boundary_by_degree[0] == 16
        # 1 + 16 - 16 = 1 (unique vacuum)
        assert data.resolved_by_degree[0] == 1


# =========================================================================
# Step 5c: Lattice classification
# =========================================================================

class TestStep5cLatticeClassification:
    """Step 5c: lattice classification forces Mukai (4, 20)."""

    def test_rank_24(self):
        """Lattice has rank 24."""
        data = lattice_classification()
        assert data.rank == 24

    def test_even(self):
        """Lattice is even (K3 is spin)."""
        data = lattice_classification()
        assert data.is_even is True

    def test_unimodular(self):
        """Lattice is unimodular (Poincare duality)."""
        data = lattice_classification()
        assert data.is_unimodular is True

    def test_signature_mod_8(self):
        """Signature is 0 mod 8."""
        data = lattice_classification()
        assert data.sig_mod_8 == 0

    def test_h2_signature_3_19(self):
        """H^2(K3) intersection form has signature (3, 19)."""
        data = lattice_classification()
        assert data.h2_signature == (3, 19)

    def test_hyperbolic_plane_contribution(self):
        """H^0 + H^4 contribute one hyperbolic plane (1, 1)."""
        data = lattice_classification()
        assert data.hyperbolic_contribution == (1, 1)

    def test_total_signature_4_20(self):
        """Total signature is (4, 20)."""
        data = lattice_classification()
        assert data.total_signature == (4, 20)

    def test_milnor_uniqueness(self):
        """Milnor's theorem: indefinite even unimodular with sig 0 mod 8 is unique."""
        data = lattice_classification()
        assert data.is_unique is True

    def test_status_conditional(self):
        """Step 5c is CONDITIONAL."""
        data = lattice_classification()
        assert 'CONDITIONAL' in data.status

    def test_hodge_excludes_12_12(self):
        """Signature (12, 12) is excluded by H^2(K3) having signature (3, 19)."""
        data = lattice_classification()
        # H^2 contributes (3, 19), H^0 + H^4 adds (1, 1) -> (4, 20)
        # There is no room for (12, 12) because 3 + 1 = 4 != 12
        assert data.h2_signature[0] + data.hyperbolic_contribution[0] == 4
        assert 4 != 12


# =========================================================================
# Euler characteristic cross-checks
# =========================================================================

class TestEulerCharacteristic:
    """Euler characteristic cross-checks for the Kummer surface."""

    def test_chi_t4_is_0(self):
        """chi(T^4) = 0."""
        result = euler_characteristic_verification()
        assert result['chi_t4'] == 0

    def test_chi_orb_is_8(self):
        """chi_orb(T^4/Z_2) = 8."""
        result = euler_characteristic_verification()
        assert result['chi_orb'] == 8

    def test_chi_tcp1_is_2(self):
        """chi(T*CP^1) = chi(CP^1) = 2."""
        result = euler_characteristic_verification()
        assert result['chi_tcp1'] == 2

    def test_chi_km_is_24(self):
        """chi(Km(T^4)) = 24."""
        result = euler_characteristic_verification()
        assert result['chi_km_path_A'] == 24

    def test_chi_O_k3_is_2(self):
        """chi(O_{K3}) = 2 = kappa_ch."""
        result = euler_characteristic_verification()
        assert result['chi_O_k3'] == 2

    def test_all_paths_agree(self):
        """All Euler characteristic paths give 24."""
        result = euler_characteristic_verification()
        assert result['all_agree'] is True


# =========================================================================
# McKay correspondence
# =========================================================================

class TestMcKayCorrespondence:
    """McKay correspondence consistency for A_1 singularities."""

    def test_k0_ranks_match(self):
        """K_0(T*CP^1) = K_0^{Z_2}(C^2) = Z^2."""
        result = mckay_correspondence_check()
        assert result['mckay_k0_match'] is True

    def test_a1_self_intersection(self):
        """Exceptional curve in A_1 resolution has self-intersection -2."""
        result = mckay_correspondence_check()
        assert result['a1_self_intersection'] == -2

    def test_e8_embedding(self):
        """16 exceptional classes embed into E_8(-1)^2 (rank 16)."""
        result = mckay_correspondence_check()
        assert result['embedding_consistent'] is True

    def test_fh_mckay_conditional(self):
        """FH McKay correspondence is conditional."""
        result = mckay_correspondence_check()
        assert 'CONDITIONAL' in result['fh_mckay_status']


# =========================================================================
# Character cross-check
# =========================================================================

class TestCharacterCrossCheck:
    """Character-level verification: p_8 * p_16 = p_24."""

    def test_convolution_matches_through_q10(self):
        """p_8 * p_16 = p_24 through q^10."""
        result = character_cross_check(max_deg=10)
        assert result['matches_through_max'] is True

    def test_p16_q1_is_16(self):
        """p_16(1) = 16 = number of blow-ups."""
        result = character_cross_check(max_deg=10)
        assert result['p16_q1_is_16'] is True

    def test_p24_known_coefficients(self):
        """p_24 first coefficients match known values (OEIS A006922)."""
        result = character_cross_check(max_deg=5)
        expected = {0: 1, 1: 24, 2: 324, 3: 3200, 4: 25650, 5: 176256}
        for n, val in expected.items():
            assert result['p24_first'][n] == val

    def test_p8_known_coefficients(self):
        """p_8 first coefficients."""
        result = character_cross_check(max_deg=5)
        expected = {0: 1, 1: 8, 2: 44, 3: 192, 4: 726, 5: 2464}
        for n, val in expected.items():
            assert result['p8_first'][n] == val


# =========================================================================
# Full verification
# =========================================================================

class TestFullExcisionVerification:
    """Full multi-path verification of the excision decomposition."""

    def test_step_5a_passed(self):
        """Step 5a passes."""
        result = full_excision_verification()
        assert result['step_5a_local_excision']['passed'] is True

    def test_step_5b_passed(self):
        """Step 5b passes."""
        result = full_excision_verification()
        assert result['step_5b_mayer_vietoris']['passed'] is True

    def test_step_5c_conditional(self):
        """Step 5c is conditional but passes classification."""
        result = full_excision_verification()
        assert result['step_5c_lattice_classification']['passed'] is True

    def test_rank_24_unconditional(self):
        """Rank 24 is unconditional (proved from 5a + 5b)."""
        result = full_excision_verification()
        assert result['summary']['rank_24_unconditional'] is True

    def test_pairing_conditional(self):
        """Pairing identification is conditional."""
        result = full_excision_verification()
        assert result['summary']['pairing_conditional'] is True

    def test_summary_statuses(self):
        """Summary statuses are correct."""
        result = full_excision_verification()
        assert result['summary']['step_5a'] == 'PROVED'
        assert result['summary']['step_5b'] == 'PROVED'
        assert 'CONDITIONAL' in result['summary']['step_5c']
