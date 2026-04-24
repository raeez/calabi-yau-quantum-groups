r"""Tests for bkm_yangian_generators.py: BKM simple roots as conjectural Yangian-deformation generators.

STATUS: ALL Yangian interpretations are CONJECTURAL (AP-CY14).
Tests verify INTERNAL CONSISTENCY of the dictionary, not existence
of the putative deformation Y(g_hat_{Delta_5}).

WHAT IS TESTED
==============

Section 1: Real simple roots and Cartan data (9 tests)
Section 2: Imaginary simple root sectors (12 tests)
Section 3: Generator census (8 tests)
Section 4: CoHA-to-Yangian dictionary (7 tests)
Section 5: Borcherds-Serre relations (6 tests)
Section 6: Framework assessment (5 tests)
Section 7: Cross-verification with existing engines (8 tests)

Total: 55 tests

CRITICAL AP COMPLIANCE
======================

AP-CY7:  CoHA is associative, NOT E_1-chiral.
AP-CY14: All Yangian results are CONJECTURAL.
AP-CY8:  Bar Euler = BKM denominator requires CY-A + Vol I anchor.
AP113:   kappa subscripts: kappa_BKM = 5, never bare kappa.

Manuscript references:
    k3_times_e.tex sec:k3e-bkm (Construction constr:k3e-roots)
    k3_times_e.tex thm:k3e-yangian (Yangian via MO R-matrix)
    k3_times_e.tex sec:k3e-mo-rmatrix (MO R-matrix)
"""

import math
import pytest

from compute.lib.bkm_yangian_generators import (
    # Constants
    STATUS,
    GRAM_MATRIX,
    NUM_REAL_SIMPLE_ROOTS,
    WEYL_GROUP_ORDER,
    WEYL_VECTOR_COORDS,
    KNOWN_MULTIPLICITIES,
    # Real simple roots
    real_simple_roots,
    cartan_matrix,
    cartan_matrix_determinant,
    weyl_group_data,
    # Imaginary simple roots
    imaginary_simple_root_sectors,
    imaginary_generator_at_discriminant,
    # Generator census
    generator_census,
    # CoHA dictionary
    coha_to_yangian_dictionary,
    # Serre relations
    borcherds_serre_relations,
    # Framework
    framework_assessment,
    # Summary
    bkm_yangian_summary,
)


# ===========================================================================
# SECTION 1: REAL SIMPLE ROOTS AND CARTAN DATA
# ===========================================================================

class TestRealSimpleRoots:
    """Real simple roots delta_1, delta_2, delta_3 of g_{Delta_5}."""

    def test_three_real_simple_roots(self):
        """g_{Delta_5} has exactly 3 real simple roots."""
        roots = real_simple_roots()
        assert len(roots) == 3

    def test_real_root_norm(self):
        """All real simple roots have norm^2 = 2 (even lattice)."""
        # VERIFIED [DC] direct computation [LT] k3_times_e.tex sec:k3e-reflections
        roots = real_simple_roots()
        for r in roots:
            assert r.norm_sq == 2

    def test_gram_matrix_symmetric(self):
        """Gram matrix is symmetric: A_{ij} = A_{ji}."""
        for i in range(3):
            for j in range(3):
                assert GRAM_MATRIX[i][j] == GRAM_MATRIX[j][i]

    def test_gram_matrix_diagonal(self):
        """Diagonal entries are 2."""
        # VERIFIED [DC] direct computation [LT] k3_times_e.tex sec:k3e-reflections
        for i in range(3):
            assert GRAM_MATRIX[i][i] == 2

    def test_gram_matrix_off_diagonal(self):
        """Off-diagonal entries are -2."""
        # VERIFIED [DC] direct computation [LT] k3_times_e.tex sec:k3e-reflections
        for i in range(3):
            for j in range(3):
                if i != j:
                    assert GRAM_MATRIX[i][j] == -2

    def test_cartan_matrix_equals_gram(self):
        """Cartan matrix a_{ij} = A_{ij} (since A_{ii} = 2 for all i)."""
        # VERIFIED [DC] a_{ij} = 2*A_{ij}/A_{ii} = A_{ij} when A_{ii}=2
        cm = cartan_matrix()
        for i in range(3):
            for j in range(3):
                assert cm[i][j] == GRAM_MATRIX[i][j]

    def test_cartan_determinant(self):
        """det(Cartan matrix) = -32 (hyperbolic)."""
        # VERIFIED [DC] direct computation
        det = cartan_matrix_determinant()
        assert det == -32

    def test_real_roots_are_cartan_generators(self):
        """Real roots correspond to Cartan triples in the Yangian."""
        roots = real_simple_roots()
        for r in roots:
            assert r.yangian_generator_type == 'Cartan triple (h, e, f)'

    def test_weyl_group_order(self):
        """Weyl group has order 6 (S_3)."""
        # VERIFIED [DC] [LT] k3_times_e.tex sec:k3e-reflections
        data = weyl_group_data()
        assert data['order'] == 6
        assert data['weyl_group'] == 'S_3'


# ===========================================================================
# SECTION 2: IMAGINARY SIMPLE ROOT SECTORS
# ===========================================================================

class TestImaginarySimpleRoots:
    """Imaginary simple roots organized by discriminant D."""

    def test_d_minus1_multiplicity(self):
        """At D=-1: multiplicity 1 (unique Weyl vector root)."""
        # VERIFIED [DC] c(-1) = 1 [CF] k3_elliptic_genus_bkm_bar.py KNOWN_C_TABLE
        data = imaginary_generator_at_discriminant(-1)
        assert data['multiplicity'] == 1
        assert data['c_value'] == 1

    def test_d_minus1_is_bosonic(self):
        """D=-1 root is bosonic (c(-1) > 0)."""
        data = imaginary_generator_at_discriminant(-1)
        assert data['parity'] == 'bosonic'

    def test_d_minus1_is_timelike(self):
        """D=-1 root is timelike ((alpha,alpha) < 0)."""
        data = imaginary_generator_at_discriminant(-1)
        assert data['norm_type'] == 'timelike'

    def test_d_minus1_unique_yangian_generator(self):
        """D=-1 gives a UNIQUE Yangian generator (Weyl vector current)."""
        data = imaginary_generator_at_discriminant(-1)
        assert 'Weyl vector' in data['yangian_data']['type']
        assert 'UNIQUE' in data['yangian_data']['uniqueness']

    def test_d_zero_multiplicity(self):
        """At D=0: multiplicity 10 (lightlike sector)."""
        # VERIFIED [DC] c(0) = 10 [CF] k3_elliptic_genus_bkm_bar.py KNOWN_C_TABLE
        data = imaginary_generator_at_discriminant(0)
        assert data['multiplicity'] == 10
        assert data['c_value'] == 10

    def test_d_zero_kappa_bkm(self):
        """D=0 sector gives kappa_BKM = c(0)/2 = 5."""
        # VERIFIED [DC] [LT] k3_times_e.tex sec:k3e-fiber-to-global
        data = imaginary_generator_at_discriminant(0)
        assert data['yangian_data']['kappa_BKM'] == 5

    def test_d_zero_is_lightlike(self):
        """D=0 roots are lightlike (isotropic)."""
        data = imaginary_generator_at_discriminant(0)
        assert data['norm_type'] == 'lightlike'

    def test_d3_first_fermionic(self):
        """At D=3: c(3) = -64 (first fermionic sector)."""
        # VERIFIED [DC] c(3) = -64 [CF] k3_elliptic_genus_bkm_bar.py KNOWN_C_TABLE
        data = imaginary_generator_at_discriminant(3)
        assert data['c_value'] == -64
        assert data['multiplicity'] == 64
        assert data['parity'] == 'fermionic'

    def test_d4_first_spacelike_bosonic(self):
        """At D=4: c(4) = 108 (first spacelike bosonic)."""
        # VERIFIED [DC] c(4) = 108 [CF] k3_elliptic_genus_bkm_bar.py KNOWN_C_TABLE
        data = imaginary_generator_at_discriminant(4)
        assert data['c_value'] == 108
        assert data['multiplicity'] == 108
        assert data['parity'] == 'bosonic'

    def test_discriminant_constraint(self):
        """Only D equiv 0 or 3 mod 4 have nonzero c(D) (AP-CY9)."""
        sectors = imaginary_simple_root_sectors(D_max=30)
        for s in sectors:
            D = s.discriminant
            if D >= 0:
                assert D % 4 in (0, 3), f"Invalid discriminant D={D}"

    def test_sign_pattern(self):
        """c(D) < 0 iff D equiv 3 mod 4 (for D >= 3)."""
        sectors = imaginary_simple_root_sectors(D_max=30)
        for s in sectors:
            if s.discriminant >= 3:
                if s.discriminant % 4 == 3:
                    assert s.parity == 'fermionic', f"D={s.discriminant} should be fermionic"
                elif s.discriminant % 4 == 0:
                    assert s.parity == 'bosonic', f"D={s.discriminant} should be bosonic"

    def test_nonexistent_discriminant(self):
        """D=1 gives no generators (1 mod 4 is not valid for index 1)."""
        data = imaginary_generator_at_discriminant(1)
        assert data['multiplicity'] == 0
        assert not data['has_generators']


# ===========================================================================
# SECTION 3: GENERATOR CENSUS
# ===========================================================================

class TestGeneratorCensus:
    """Total generator counts and growth estimates."""

    def test_real_count(self):
        """3 real simple roots."""
        census = generator_census(D_max=20)
        assert census['real_simple_roots'] == 3

    def test_timelike_count(self):
        """1 timelike imaginary generator (D=-1)."""
        census = generator_census(D_max=20)
        assert census['imaginary_generators']['timelike_D_lt_0'] == 1

    def test_lightlike_count(self):
        """10 lightlike imaginary generators (D=0)."""
        census = generator_census(D_max=20)
        assert census['imaginary_generators']['lightlike_D_eq_0'] == 10

    def test_grand_total_gt_real(self):
        """Grand total > real count (imaginary generators exist)."""
        census = generator_census(D_max=20)
        assert census['grand_total'] > census['real_simple_roots']

    def test_imaginary_total_consistency(self):
        """Imaginary total = timelike + lightlike + spacelike_bos + spacelike_ferm."""
        census = generator_census(D_max=20)
        img = census['imaginary_generators']
        total = (img['timelike_D_lt_0'] + img['lightlike_D_eq_0']
                 + img['spacelike_bosonic'] + img['spacelike_fermionic'])
        assert total == img['total']

    def test_kappa_bkm(self):
        """kappa_BKM = c(0)/2 = 5 (AP113 compliant)."""
        # VERIFIED [DC] [LT] k3_times_e.tex sec:k3e-fiber-to-global
        census = generator_census(D_max=20)
        assert census['kappa_BKM'] == 5

    def test_class_m(self):
        """Shadow class is M (infinite generators)."""
        census = generator_census(D_max=20)
        assert 'M' in census['class']

    def test_growth_monotonic(self):
        """Total generators grow with D_max."""
        c10 = generator_census(D_max=10)
        c20 = generator_census(D_max=20)
        assert c20['grand_total'] > c10['grand_total']


# ===========================================================================
# SECTION 4: CoHA-TO-YANGIAN DICTIONARY (AP-CY7 CRITICAL)
# ===========================================================================

class TestCoHADictionary:
    """CoHA identification and AP-CY7 compliance."""

    def test_coha_identification_proved(self):
        """CoHA(K3xE) = U(n_+(g_{Delta_5})) is PROVED."""
        d = coha_to_yangian_dictionary()
        assert d['coha_identification']['status'] == 'PROVED'

    def test_coha_is_associative(self):
        """CoHA is an ASSOCIATIVE algebra (AP-CY7)."""
        d = coha_to_yangian_dictionary()
        assert d['coha_is_associative'] is True

    def test_coha_is_not_chiral(self):
        """CoHA is NOT a chiral algebra (AP-CY7)."""
        d = coha_to_yangian_dictionary()
        assert d['coha_is_chiral'] is False

    def test_coha_is_not_e1_chiral(self):
        """CoHA is NOT an E_1-chiral algebra (AP-CY7: requires G(X) to exist)."""
        d = coha_to_yangian_dictionary()
        assert d['coha_is_e1_chiral'] is False

    def test_yangian_double_conjectural(self):
        """The Drinfeld double Y(g_{Delta_5}) is CONJECTURAL."""
        d = coha_to_yangian_dictionary()
        assert d['yangian_double']['status'] == 'CONJECTURAL'

    def test_c3_comparison_proved(self):
        """For C^3, the Drinfeld double IS proved (Schiffmann-Vasserot)."""
        d = coha_to_yangian_dictionary()
        assert 'PROVED' in d['c3_comparison']['yangian']

    def test_coha_generators_nonempty(self):
        """CoHA has generators at multiple discriminants."""
        d = coha_to_yangian_dictionary()
        assert len(d['coha_generators']) > 5


# ===========================================================================
# SECTION 5: BORCHERDS-SERRE RELATIONS
# ===========================================================================

class TestBorcherdsSerre:
    """Borcherds-Serre relations and Yangian deformation status."""

    def test_real_real_serre_known(self):
        """Real-real Serre relations: Yangian deformation is KNOWN."""
        serre = borcherds_serre_relations()
        assert serre['real_real_serre']['yangian_deformation_status'] == 'KNOWN'

    def test_real_imaginary_partial(self):
        """Real-imaginary Serre: partially known."""
        serre = borcherds_serre_relations()
        assert 'PARTIAL' in serre['real_imaginary_serre']['yangian_deformation_status']

    def test_imaginary_imaginary_unknown(self):
        """Imaginary-imaginary Serre: COMPLETELY UNKNOWN for BKM."""
        serre = borcherds_serre_relations()
        assert 'UNKNOWN' in serre['imaginary_imaginary_serre']['yangian_deformation_status']

    def test_serre_power_off_diagonal(self):
        """Serre power for i!=j: 1 - a_{ij} = 1 - (-2) = 3."""
        # VERIFIED [DC] Serre relation (ad e_i)^3 e_j = 0
        serre = borcherds_serre_relations()
        for (i, j), data in serre['real_real_serre']['relations'].items():
            if i != j:
                assert data['serre_power'] == 3

    def test_cartan_entries_off_diagonal(self):
        """Off-diagonal Cartan entries are -2."""
        serre = borcherds_serre_relations()
        for (i, j), data in serre['real_real_serre']['relations'].items():
            if i != j:
                assert data['cartan_entry'] == -2

    def test_overall_status_conjectural(self):
        """Overall status is CONJECTURAL."""
        serre = borcherds_serre_relations()
        assert serre['status'] == STATUS


# ===========================================================================
# SECTION 6: FRAMEWORK ASSESSMENT
# ===========================================================================

class TestFramework:
    """Framework assessment for conjectural Yangian-deformation generators."""

    def test_real_roots_proved(self):
        """Real root Yangian realization is standard (proved)."""
        fw = framework_assessment()
        assert 'PROVED' in fw['real_roots']['status']
        assert fw['real_roots']['new_math_required'] is False

    def test_d_minus1_plausible(self):
        """D=-1 root: plausible by affine analogy."""
        fw = framework_assessment()
        assert 'PLAUSIBLE' in fw['d_minus1']['status']

    def test_d_zero_conjectural(self):
        """D=0 roots: conjectural (no direct analogue)."""
        fw = framework_assessment()
        assert fw['d_zero']['status'] == 'CONJECTURAL'
        assert fw['d_zero']['new_math_required'] is True

    def test_d_positive_unknown(self):
        """D>0 roots: UNKNOWN (fundamental obstruction)."""
        fw = framework_assessment()
        assert 'UNKNOWN' in fw['d_positive']['status']
        assert fw['d_positive']['new_math_required'] is True

    def test_verdict_mentions_new_math(self):
        """Verdict identifies the need for new mathematics."""
        fw = framework_assessment()
        assert 'NEW MATHEMATICS' in fw['verdict']


# ===========================================================================
# SECTION 7: CROSS-VERIFICATION WITH EXISTING ENGINES
# ===========================================================================

class TestCrossVerification:
    """Cross-verify with k3_elliptic_genus_bkm_bar and bkm_chiral_algebra."""

    def test_gram_matrix_matches_bkm_chiral(self):
        """Gram matrix matches bkm_chiral_algebra.GRAM_MATRIX_II21."""
        # VERIFIED [CF] cross-engine consistency
        from compute.lib.bkm_chiral_algebra import GRAM_MATRIX_II21
        for i in range(3):
            for j in range(3):
                assert GRAM_MATRIX[i][j] == GRAM_MATRIX_II21[i][j]

    def test_multiplicities_match_bkm_bar(self):
        """Known multiplicities match k3_elliptic_genus_bkm_bar.KNOWN_C_TABLE."""
        # VERIFIED [CF] cross-engine consistency
        from compute.lib.k3_elliptic_genus_bkm_bar import KNOWN_C_TABLE
        for D, expected in KNOWN_MULTIPLICITIES.items():
            assert KNOWN_C_TABLE[D] == expected, f"Mismatch at D={D}"

    def test_kappa_bkm_matches_lift_weight(self):
        """kappa_BKM = 5 matches borcherds_lift_weight()."""
        # VERIFIED [CF] cross-engine consistency
        from compute.lib.k3_elliptic_genus_bkm_bar import borcherds_lift_weight
        assert borcherds_lift_weight() == 5

    def test_shadow_class_matches_bkm_chiral(self):
        """Shadow class M matches bkm_chiral_algebra analysis."""
        from compute.lib.bkm_chiral_algebra import shadow_class_analysis
        shadow = shadow_class_analysis(30)
        assert shadow['shadow_class'] == 'M'

    def test_coha_status_matches_bkm_chiral(self):
        """CoHA identification status matches bkm_chiral_algebra."""
        from compute.lib.bkm_chiral_algebra import coha_bkm_comparison
        coha = coha_bkm_comparison(20)
        assert coha['identification_status'] == 'PROVED'
        assert coha['coha_is_associative'] is True
        assert coha['coha_is_chiral'] is False

    def test_lattice_rank_consistency(self):
        """Lattice rank = 3 matches bkm_chiral_algebra.LATTICE_RANK."""
        from compute.lib.bkm_chiral_algebra import LATTICE_RANK
        assert NUM_REAL_SIMPLE_ROOTS == LATTICE_RANK

    def test_summary_consistency(self):
        """Summary function runs without error and returns expected keys."""
        summary = bkm_yangian_summary(D_max=16)
        assert 'real_simple_roots' in summary
        assert 'imaginary_simple_roots' in summary
        assert 'generator_census' in summary
        assert 'coha_status' in summary
        assert 'serre_relations' in summary
        assert summary['status'] == STATUS

    def test_sectors_cover_known_discriminants(self):
        """Imaginary sectors cover all known discriminants."""
        sectors = imaginary_simple_root_sectors(D_max=16)
        covered_D = {s.discriminant for s in sectors}
        for D in KNOWN_MULTIPLICITIES:
            assert D in covered_D, f"D={D} not covered by sectors"


# ===========================================================================
# SECTION 8: MULTI-PATH VERIFICATION (AP10 compliance)
# ===========================================================================

class TestMultiPathVerification:
    """Multi-path verification: every hardcoded value checked via independent computation."""

    def test_det_gram_by_cofactor_vs_direct(self):
        """det(Gram) = -32 via cofactor expansion AND direct formula.

        Path 1: cofactor expansion (cartan_matrix_determinant)
        Path 2: direct numpy-free 3x3 determinant
        """
        # Path 1
        det1 = cartan_matrix_determinant()
        # Path 2: Sarrus rule
        A = GRAM_MATRIX
        det2 = (A[0][0]*A[1][1]*A[2][2] + A[0][1]*A[1][2]*A[2][0]
                + A[0][2]*A[1][0]*A[2][1] - A[0][2]*A[1][1]*A[2][0]
                - A[0][1]*A[1][0]*A[2][2] - A[0][0]*A[1][2]*A[2][1])
        assert det1 == det2 == -32

    def test_kappa_bkm_three_paths(self):
        """kappa_BKM = 5 via three independent paths.

        Path 1: c(0)/2 from KNOWN_MULTIPLICITIES
        Path 2: borcherds_lift_weight() from bkm_bar engine
        Path 3: census kappa_BKM from generator_census
        """
        # Path 1
        v1 = KNOWN_MULTIPLICITIES[0] // 2
        # Path 2
        from compute.lib.k3_elliptic_genus_bkm_bar import borcherds_lift_weight
        v2 = borcherds_lift_weight()
        # Path 3
        v3 = generator_census(D_max=10)['kappa_BKM']
        assert v1 == v2 == v3 == 5

    def test_c_values_engine_vs_hardcoded(self):
        """c(D) hardcoded values match exact phi01_fourier computation.

        Path 1: KNOWN_MULTIPLICITIES (hardcoded)
        Path 2: phi01_fourier.py exact theta-ratio arithmetic
        """
        from compute.lib.k3_elliptic_genus_bkm_bar import c_table_from_phi01
        computed = c_table_from_phi01(D_max=30)
        for D, hardcoded in KNOWN_MULTIPLICITIES.items():
            assert computed.get(D, 0) == hardcoded, (
                f"c({D}): hardcoded={hardcoded}, computed={computed.get(D, 0)}"
            )

    def test_d_minus1_mult_two_paths(self):
        """c(-1) = 1 via hardcoded AND imaginary_generator_at_discriminant.

        Path 1: KNOWN_MULTIPLICITIES[-1]
        Path 2: imaginary_generator_at_discriminant(-1)
        """
        v1 = KNOWN_MULTIPLICITIES[-1]
        v2 = imaginary_generator_at_discriminant(-1)['multiplicity']
        assert v1 == v2 == 1

    def test_d_zero_mult_two_paths(self):
        """c(0) = 10 via hardcoded AND sector analysis.

        Path 1: KNOWN_MULTIPLICITIES[0]
        Path 2: sector list filtered by D=0
        """
        v1 = KNOWN_MULTIPLICITIES[0]
        sectors = imaginary_simple_root_sectors(D_max=10)
        d0_sectors = [s for s in sectors if s.discriminant == 0]
        assert len(d0_sectors) == 1
        v2 = d0_sectors[0].multiplicity
        assert v1 == v2 == 10

    def test_census_total_is_sum_of_parts(self):
        """Grand total = real + imaginary, computed two ways.

        Path 1: census grand_total
        Path 2: manual sum of census sub-fields
        """
        census = generator_census(D_max=20)
        # Path 1
        gt = census['grand_total']
        # Path 2
        manual = census['real_simple_roots'] + census['imaginary_generators']['total']
        assert gt == manual

    def test_imaginary_total_matches_sector_sum(self):
        """Imaginary total from census matches sum over sector multiplicities.

        Path 1: generator_census imaginary total
        Path 2: sum of multiplicities from imaginary_simple_root_sectors
        """
        census = generator_census(D_max=20)
        v1 = census['imaginary_generators']['total']
        sectors = imaginary_simple_root_sectors(D_max=20)
        v2 = sum(s.multiplicity for s in sectors)
        assert v1 == v2

    def test_serre_power_from_gram(self):
        """Serre power 1 - a_{ij} = 3 verified from Gram matrix directly.

        Path 1: borcherds_serre_relations() output
        Path 2: direct computation from GRAM_MATRIX
        """
        serre = borcherds_serre_relations()
        for (i, j), data in serre['real_real_serre']['relations'].items():
            if i != j:
                # Path 1
                v1 = data['serre_power']
                # Path 2: a_{ij} = 2 * A_{ij} / A_{ii} = A_{ij} (since A_{ii}=2)
                a_ij = GRAM_MATRIX[i-1][j-1]
                v2 = 1 - a_ij
                assert v1 == v2 == 3

    def test_weyl_vector_inner_products(self):
        """Weyl vector rho satisfies (rho, delta_i) = -1 for all i.

        Path 1: known from manuscript (def:k3e-weyl-vector)
        Path 2: direct computation rho = (1/2)(d1+d2+d3), (rho, d_i) = (1/2)*sum_j A_{ji}
        """
        from fractions import Fraction
        for i in range(3):
            # (rho, delta_i) = sum_j (1/2) * (delta_j, delta_i) = (1/2) * sum_j A_{ji}
            inner = sum(Fraction(1, 2) * GRAM_MATRIX[j][i] for j in range(3))
            assert inner == -1, f"(rho, delta_{i+1}) = {inner}, expected -1"

    def test_discriminant_constraint_independent(self):
        """AP-CY9 discriminant constraint verified from first principles.

        Path 1: imaginary_simple_root_sectors checks
        Path 2: k3_elliptic_genus_bkm_bar.verify_discriminant_constraint
        """
        # Path 1
        sectors = imaginary_simple_root_sectors(D_max=30)
        for s in sectors:
            if s.discriminant >= 0:
                assert s.discriminant % 4 in (0, 3)
        # Path 2
        from compute.lib.k3_elliptic_genus_bkm_bar import verify_discriminant_constraint
        result = verify_discriminant_constraint(D_max=30)
        assert result['constraint_satisfied'] is True
