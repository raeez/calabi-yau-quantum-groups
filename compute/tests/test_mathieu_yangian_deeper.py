r"""Tests for mathieu_yangian_deeper.py: deeper Mathieu-Yangian connection.

STATUS: ALL results in this module are CONJECTURAL (AP-CY14).
The tests verify INTERNAL CONSISTENCY of the deeper construction.

CENTRAL RESULTS (all conjectural):
    (1) M_24 permutes the 24 Mukai generators at the A_1^{24} Niemeier point.
    (2) The twined bar Euler product equals the Frame shape eta product
        for all 26 M_24 conjugacy classes (cyclotomic identity).
    (3) The 23 Niemeier Yangians form a landscape with universal bar Euler
        product eta^{24} and varying Umbral groups.
    (4) The Yangian deformation preserves the GHV symmetry surfing group.

Test structure:
    Section 1: Generator permutation (10 tests)
    Section 2: Frame shape bar Euler products (12 tests)
    Section 3: Niemeier Yangians and Umbral groups (11 tests)
    Section 4: Surfing group preservation (10 tests)
    Section 5: Cross-verification (7 tests)

Manuscript references:
    k3_chiral_algebra.tex, Conjecture conj:mathieu-yangian (L1000)
    k3e_cy3_programme.tex, Thm thm:mathieu-moonshine (L487)
    k3e_cy3_programme.tex, Rem rem:twining-genera (L588)
"""

import pytest
from fractions import Fraction

from compute.lib.mathieu_yangian_deeper import (
    # Constants
    DEEPER_ENGINE_STATUS,
    DIM_H0, DIM_H2, DIM_H4, DIM_TOTAL,
    MUKAI_SIG_PLUS, MUKAI_SIG_MINUS,
    # Section 1: Generator permutation
    GeneratorPermutationData,
    generator_permutation_analysis,
    m24_action_on_mukai_lattice,
    generator_fixed_point_structure,
    _count_orbits,
    # Section 2: Frame shape bar Euler products
    CyclotomicBarIdentity,
    verify_cyclotomic_identity,
    twined_bar_euler_product,
    verify_all_twined_bar_euler_products,
    frame_shape_to_modular_data,
    # Section 3: Niemeier Yangians
    NiemeierYangianData,
    niemeier_yangian_at_point,
    niemeier_yangian_landscape,
    umbral_group_order,
    umbral_landscape_summary,
    # Section 4: Surfing
    SurfingData,
    K3_SIGMA_MODEL_POINTS,
    surfing_analysis,
    surfing_union_generates_m24,
    yangian_deformation_preserves_symmetry,
    # Section 5: Verification
    verify_generator_permutation,
    verify_cyclotomic_identities,
    verify_niemeier_landscape,
    verify_surfing_preservation,
    full_deeper_verification,
)

from compute.lib.mathieu_moonshine_yangian import (
    M24_CONJUGACY_CLASSES,
    UMBRAL_NIEMEIER_DATA,
    KAPPA_CH_K3,
    twined_eta_product,
)


# =========================================================================
# Section 1: Generator permutation (10 tests)
# =========================================================================

class TestGeneratorPermutation:
    """Verify M_24 action on the 24 Mukai generators."""

    def test_cohomology_dimensions(self):
        """H*(K3, C) = H^0 + H^2 + H^4, dims 1 + 22 + 1 = 24."""
        assert DIM_H0 == 1
        assert DIM_H2 == 22
        assert DIM_H4 == 1
        assert DIM_TOTAL == 24

    def test_mukai_signature(self):
        """Mukai lattice has signature (4, 20)."""
        assert MUKAI_SIG_PLUS == 4
        assert MUKAI_SIG_MINUS == 20
        assert MUKAI_SIG_PLUS + MUKAI_SIG_MINUS == 24

    def test_identity_permutation(self):
        """1A fixes all 24 generators."""
        data = generator_permutation_analysis('1A')
        assert data.trace_on_generators == 24
        assert data.preserves_sum_constraint is True
        assert data.preserves_mukai_pairing is True

    def test_2B_no_fixed_generators(self):
        """2B (free involution) fixes 0 generators."""
        data = generator_permutation_analysis('2B')
        assert data.trace_on_generators == 0
        assert data.preserves_sum_constraint is True

    def test_all_preserve_sum_constraint(self):
        """All M_24 elements preserve sum h_i = 0."""
        for name in M24_CONJUGACY_CLASSES:
            data = generator_permutation_analysis(name)
            assert data.preserves_sum_constraint is True, (
                f"{name}: does not preserve sum constraint"
            )

    def test_mukai_lattice_data(self):
        """Mukai lattice analysis returns correct structural data."""
        data = m24_action_on_mukai_lattice()
        assert data['mukai_rank'] == 24
        assert data['mukai_signature'] == (4, 20)
        assert data['m24_order'] == 244823040

    def test_fixed_point_structure_identity(self):
        """Identity fixes all 24 generators, has 24 orbits (each trivial)."""
        fps = generator_fixed_point_structure()
        assert fps['1A']['fixed_generators'] == 24
        assert fps['1A']['yangian_parameter_orbits'] == 24

    def test_fixed_point_structure_2B(self):
        """2B fixes 0, has 12 orbits (each a 2-cycle)."""
        fps = generator_fixed_point_structure()
        assert fps['2B']['fixed_generators'] == 0
        assert fps['2B']['yangian_parameter_orbits'] == 12

    def test_orbit_count_formula(self):
        """Number of orbits = sum of Frame shape multiplicities."""
        for name, cc in M24_CONJUGACY_CLASSES.items():
            expected = sum(cc.frame_shape.values())
            assert _count_orbits(cc.frame_shape) == expected, (
                f"{name}: orbit count mismatch"
            )

    def test_verification_suite(self):
        """The generator permutation verification suite passes."""
        result = verify_generator_permutation()
        assert result['all_ok']
        assert result['num_classes'] == 26


# =========================================================================
# Section 2: Frame shape bar Euler products (12 tests)
# =========================================================================

class TestFrameShapeBarEuler:
    """Verify that twined bar Euler product = eta product of Frame shape."""

    def test_cyclotomic_identity_k1(self):
        """Cyclotomic identity for k=1: trivial (1-cycle)."""
        result = verify_cyclotomic_identity(1)
        assert result.identity_holds

    def test_cyclotomic_identity_k2(self):
        """Cyclotomic identity for k=2: (1-x)(1+x) = 1-x^2."""
        result = verify_cyclotomic_identity(2)
        assert result.identity_holds

    def test_cyclotomic_identity_k3(self):
        """Cyclotomic identity for k=3: (1-x)(1-omega x)(1-omega^2 x) = 1-x^3."""
        result = verify_cyclotomic_identity(3)
        assert result.identity_holds

    def test_cyclotomic_identity_all_cycle_lengths(self):
        """Cyclotomic identity holds for all cycle lengths in M_24 Frame shapes."""
        result = verify_cyclotomic_identities()
        assert result['all_ok']
        # M_24 Frame shapes use cycle lengths 1,2,3,4,5,6,7,8,10,11,12,14,15,21,23
        assert result['num_lengths'] >= 15

    def test_bar_euler_identity_1A(self):
        """For 1A: twined bar Euler = eta^{24} = Delta/q."""
        result = twined_bar_euler_product('1A')
        assert result['bar_equals_eta']

    def test_bar_euler_identity_2A(self):
        """For 2A: twined bar Euler = eta(tau)^8 * eta(2*tau)^8."""
        result = twined_bar_euler_product('2A')
        assert result['bar_equals_eta']

    def test_bar_euler_identity_2B(self):
        """For 2B: twined bar Euler = eta(2*tau)^{12}."""
        result = twined_bar_euler_product('2B')
        assert result['bar_equals_eta']

    def test_bar_euler_identity_3A(self):
        """For 3A: twined bar Euler = eta(tau)^6 * eta(3*tau)^6."""
        result = twined_bar_euler_product('3A')
        assert result['bar_equals_eta']

    def test_bar_euler_all_26_classes(self):
        """Twined bar Euler = eta product for all 26 M_24 classes."""
        result = verify_all_twined_bar_euler_products(max_degree=12)
        assert result['all_ok']
        assert result['num_classes'] == 26

    def test_modular_data_1A(self):
        """For 1A: eta product has weight 12, level 1."""
        data = frame_shape_to_modular_data('1A')
        assert data['eta_weight'] == '12'  # (1/2)*24 = 12
        assert data['eta_level'] == 1
        assert data['total_exponent'] == 24

    def test_modular_data_2A(self):
        """For 2A: eta product has weight 8, level 2."""
        data = frame_shape_to_modular_data('2A')
        assert data['eta_weight'] == '8'  # (1/2)*(8+8) = 8
        assert data['eta_level'] == 2
        assert data['total_exponent'] == 16  # a_1 + a_2 = 8 + 8 = 16

    def test_modular_data_23A(self):
        """For 23A: eta product has weight 1, level 23."""
        data = frame_shape_to_modular_data('23A')
        assert data['eta_weight'] == '1'  # (1/2)*(1+1) = 1
        assert data['eta_level'] == 23
        assert data['order'] == 23


# =========================================================================
# Section 3: Niemeier Yangians and Umbral groups (11 tests)
# =========================================================================

class TestNiemeierYangians:
    """Verify the landscape of 23 Niemeier Yangians."""

    def test_23_niemeier_yangians(self):
        """There are 23 Niemeier Yangians (excluding Leech)."""
        landscape = niemeier_yangian_landscape()
        assert landscape['num_niemeier'] == 23

    def test_a1_24_is_mathieu(self):
        """The A_1^{24} Yangian gives Mathieu moonshine (M_24, lambency 2)."""
        data = niemeier_yangian_at_point('A_1^{24}')
        assert data.umbral_group == 'M_24'
        assert data.lambency == 2
        assert data.coxeter_number == 2

    def test_e8_cubed_triality(self):
        """The E_8^3 Yangian has S_3 symmetry (triality)."""
        data = niemeier_yangian_at_point('E_8^3')
        assert data.umbral_group == 'S_3'
        assert data.lambency == 30
        assert data.coxeter_number == 30

    def test_d24_outer_automorphism(self):
        """The D_{24} Yangian has Z_2 symmetry (outer automorphism)."""
        data = niemeier_yangian_at_point('D_{24}')
        assert data.umbral_group == 'Z_2'
        assert data.lambency == 46

    def test_m24_is_largest_umbral_group(self):
        """M_24 has the largest order among Umbral groups."""
        summary = umbral_landscape_summary()
        assert summary['max_order'] == 244823040  # |M_24|
        assert summary['max_group'] == 'M_24 at A_1^{24}'

    def test_z2_is_smallest_umbral_group(self):
        """Z_2 is the smallest Umbral group (and most common)."""
        summary = umbral_landscape_summary()
        assert summary['min_order'] == 2
        assert summary['num_with_Z2'] >= 10  # many lattices have Z_2

    def test_umbral_group_orders_positive(self):
        """All Umbral group orders are positive."""
        for rs in UMBRAL_NIEMEIER_DATA:
            order = umbral_group_order(rs)
            assert order > 0, f"{rs}: order = {order}"

    def test_m24_order(self):
        """|M_24| = 244,823,040 = 2^10 * 3^3 * 5 * 7 * 11 * 23."""
        assert umbral_group_order('A_1^{24}') == 244823040
        # Verify prime factorization
        n = 244823040
        assert n == (2**10) * (3**3) * 5 * 7 * 11 * 23

    def test_universal_bar_euler(self):
        """All 23 Niemeier Yangians have the same bar Euler product eta^{24}."""
        landscape = niemeier_yangian_landscape()
        assert landscape['universal_properties']['bar_euler_product'] == 'eta(tau)^{24} (identical for all 23)'
        assert landscape['universal_properties']['kappa_ch_lattice'] == 24
        assert landscape['universal_properties']['kappa_ch_sigma'] == 2

    def test_niemeier_landscape_verification(self):
        """The Niemeier landscape verification suite passes."""
        result = verify_niemeier_landscape()
        assert result['all_ok']
        assert result['num_niemeier'] == 23

    def test_degenerate_lambencies(self):
        """Some lambencies are shared by multiple root systems."""
        landscape = niemeier_yangian_landscape()
        degen = landscape['degenerate_lambencies']
        # lambency 6 is shared by D_4^6 and A_5^4 D_4
        assert 6 in degen
        assert len(degen[6]) == 2


# =========================================================================
# Section 4: Surfing group preservation (10 tests)
# =========================================================================

class TestSurfingPreservation:
    """Verify the symmetry surfing group is preserved by the Yangian deformation."""

    def test_kummer_surfing(self):
        """Kummer K3 has symmetry group Z_2^4 rtimes A_4, preserved by Yangian."""
        data = surfing_analysis('Kummer_T4_Z2')
        assert data.group_order == 192
        assert data.deformation_preserves is True

    def test_fermat_surfing(self):
        """Fermat quartic has large discrete symmetry, preserved by Yangian."""
        data = surfing_analysis('Fermat_quartic')
        assert data.group_order == 6144
        assert data.deformation_preserves is True

    def test_d4_hexacode_surfing(self):
        """D_4^6 Niemeier point has 3.S_6 symmetry, preserved by Yangian."""
        data = surfing_analysis('D4_hexacode')
        assert data.group_order == 2160
        assert data.deformation_preserves is True

    def test_e8_cubed_surfing(self):
        """E_8^3 Niemeier point has S_3 symmetry, preserved by Yangian."""
        data = surfing_analysis('E8_cubed')
        assert data.group_order == 6
        assert data.deformation_preserves is True

    def test_all_explicit_points_preserved(self):
        """All explicit K3 sigma model points have symmetry preserved."""
        result = verify_surfing_preservation()
        assert result['all_ok']
        assert result['num_points'] == 4

    def test_union_generates_m24(self):
        """The union of symmetry groups generates M_24 (GHV theorem)."""
        result = surfing_union_generates_m24()
        assert result['union_generates_m24'] is True
        assert result['num_ghv_realized'] >= 21

    def test_deformation_preserves_analysis(self):
        """The deformation preservation analysis has correct structure."""
        result = yangian_deformation_preserves_symmetry()
        assert result['theorem_status'] == 'CONJECTURAL (AP-CY14)'
        assert len(result['proof_steps']) == 6
        assert len(result['conditions']) == 4

    def test_unknown_point_returns_error(self):
        """Querying an unknown K3 sigma model point returns an error."""
        data = surfing_analysis('nonexistent_point')
        assert data.status == 'ERROR'
        assert data.deformation_preserves is False

    def test_explicit_classes_subset_of_m24(self):
        """All Frame shapes realized at explicit points are valid M_24 classes."""
        for point_name, point_data in K3_SIGMA_MODEL_POINTS.items():
            for cls in point_data['frame_shapes_realized']:
                assert cls in M24_CONJUGACY_CLASSES, (
                    f"{point_name}: class {cls} not in M_24"
                )

    def test_surfing_classes_are_realized(self):
        """Frame shapes at explicit K3 points are all realized on K3."""
        for point_name, point_data in K3_SIGMA_MODEL_POINTS.items():
            for cls in point_data['frame_shapes_realized']:
                cc = M24_CONJUGACY_CLASSES[cls]
                assert cc.realized_on_k3, (
                    f"{point_name}: class {cls} is not realized on K3"
                )


# =========================================================================
# Section 5: Cross-verification (7 tests)
# =========================================================================

class TestCrossVerification:
    """Cross-verify deeper results against parent engine and manuscript."""

    def test_full_deeper_verification(self):
        """The complete deeper verification suite passes."""
        result = full_deeper_verification()
        assert result['status'] == 'CONJECTURAL'
        assert result['path1_generator_permutation']['all_ok']
        assert result['path2_cyclotomic_identities']['all_ok']
        assert result['path3_twined_bar_euler']['all_ok']
        assert result['path4_niemeier_landscape']['all_ok']
        assert result['path5_surfing_preservation']['all_ok']

    def test_kappa_ch_consistent(self):
        """kappa_ch = 2 is consistent across all deeper analysis."""
        # From parent engine
        assert KAPPA_CH_K3 == 2
        # From Niemeier landscape
        landscape = niemeier_yangian_landscape()
        assert landscape['universal_properties']['kappa_ch_sigma'] == 2

    def test_eta_product_consistency(self):
        """Twined eta products from parent engine match bar Euler computation."""
        for name in ['1A', '2A', '3A', '5A', '11A']:
            parent = twined_eta_product(name, max_degree=10)
            deeper = twined_bar_euler_product(name, max_degree=10)
            for i in range(11):
                assert parent.get(i, 0) == deeper['eta_product_coeffs'].get(i, 0), (
                    f"{name}, q^{i}: parent={parent.get(i,0)}, "
                    f"deeper={deeper['eta_product_coeffs'].get(i,0)}"
                )

    def test_niemeier_data_consistent(self):
        """Niemeier data in deeper engine matches parent engine."""
        for rs in UMBRAL_NIEMEIER_DATA:
            parent_data = UMBRAL_NIEMEIER_DATA[rs]
            deeper_data = niemeier_yangian_at_point(rs)
            assert parent_data['lambency'] == deeper_data.lambency
            assert parent_data['umbral_group'] == deeper_data.umbral_group

    def test_24_orbits_for_identity(self):
        """Identity has 24 orbits (each generator is its own orbit)."""
        fps = generator_fixed_point_structure()
        assert fps['1A']['yangian_parameter_orbits'] == 24

    def test_generator_count_equals_mukai_rank(self):
        """The total number of generators equals the Mukai lattice rank."""
        assert DIM_TOTAL == 24
        data = m24_action_on_mukai_lattice()
        assert data['mukai_rank'] == DIM_TOTAL

    def test_2a_12_is_double_mathieu(self):
        """The A_2^{12} Niemeier Yangian has group 2.M_12 (double cover of M_12)."""
        data = niemeier_yangian_at_point('A_2^{12}')
        assert data.umbral_group == '2.M_12'
        assert data.lambency == 3
        # |2.M_12| = 2 * 95040 = 190080
        assert umbral_group_order('A_2^{12}') == 190080
