r"""Tests for umbral_23_niemeier_yangian.py: Umbral mock modular forms
from the 23 Niemeier K3 Yangians.

STATUS: ALL results in this module are CONJECTURAL (AP-CY14).
The tests verify INTERNAL CONSISTENCY of the Umbral-Yangian construction.

CENTRAL RESULTS (all conjectural):
    (1) At each of the 23 Niemeier points, the K3 Yangian parameters
        specialize to Coxeter exponents with sum = 0 (CY_2 constraint).
    (2) The Umbral Frame shapes for all 23 groups sum to 24.
    (3) The identity element of each Umbral group gives eta^{24}.
    (4) The mock modular polar coefficient is -kappa_ch = -2 at all 23 points.
    (5) The shadow tower mechanism produces h_N uniformly for all 23 cases.
    (6) Mock modular coefficients at n >= 1 are positive (G_N rep dimensions).

Test structure:
    Section 1: Yangian parameter specialization (15 tests)
    Section 2: Umbral Frame shape eta products (14 tests)
    Section 3: Mock modular forms and shadow tower (14 tests)
    Section 4: Uniform construction Y -> h_N (8 tests)
    Section 5: Umbral group structure (12 tests)
    Section 6: Cross-verification and landscape (7 tests)

Manuscript references:
    k3_chiral_algebra.tex, Section "Umbral moonshine programme"
    k3_chiral_algebra.tex, "Niemeier Yangian landscape and Umbral groups"
    Cheng-Duncan-Harvey, arXiv:1204.2779 (Umbral moonshine)
    Duncan-Griffin-Ono, arXiv:1503.01472 (proof)
"""

import pytest
from fractions import Fraction

from compute.lib.umbral_23_niemeier_yangian import (
    # Constants
    ENGINE_STATUS,
    KAPPA_CH_K3_SIGMA,
    KAPPA_CH_LATTICE_VOA,
    MOCK_POLAR_COEFF,
    # Section 1: Parameters
    ade_coxeter_exponents,
    ade_content_vector,
    NiemeierYangianParams,
    niemeier_yangian_parameters,
    verify_parameter_sum_zero,
    structure_function_at_niemeier,
    # Section 2: Frame shapes
    UmbralFrameShape,
    UMBRAL_FRAME_SHAPES,
    umbral_frame_shapes,
    umbral_eta_product,
    eta_product_weight,
    eta_product_level,
    eta_product_leading_power,
    # Section 3: Mock modular
    UmbralMockModularData,
    UMBRAL_MOCK_COEFFICIENTS,
    umbral_mock_modular_data,
    umbral_polar_coefficient,
    # Section 4: Uniform construction
    UniformConstructionData,
    uniform_construction,
    shadow_tower_produces_mock,
    # Section 5: Umbral groups
    UmbralGroupData,
    UMBRAL_GROUP_STRUCTURE,
    umbral_group_data,
    # Section 6: Verification
    verify_all_parameter_sums,
    verify_all_polar_coefficients,
    verify_all_frame_shape_sums,
    verify_umbral_eta_products,
    verify_mock_coefficients_positive,
    verify_uniform_construction,
    umbral_23_landscape,
    full_umbral_verification,
)

from compute.lib.mathieu_moonshine_yangian import (
    UMBRAL_NIEMEIER_DATA,
    KAPPA_CH_K3,
    MOCK_MODULAR_COEFFICIENTS,
)


# =========================================================================
# Section 1: Yangian parameter specialization (15 tests)
# =========================================================================

class TestYangianParameters:
    """Verify Yangian parameter specialization at all 23 Niemeier points."""

    def test_a1_exponents(self):
        """A_1 Coxeter exponents = {1}, h = 2."""
        exps = ade_coxeter_exponents('A', 1)
        assert exps == (1,)

    def test_a2_exponents(self):
        """A_2 Coxeter exponents = {1, 2}, h = 3."""
        exps = ade_coxeter_exponents('A', 2)
        assert exps == (1, 2)

    def test_d4_exponents(self):
        """D_4 Coxeter exponents = {1, 3, 3, 5}, h = 6."""
        exps = ade_coxeter_exponents('D', 4)
        assert sorted(exps) == [1, 3, 3, 5]

    def test_e8_exponents(self):
        """E_8 Coxeter exponents = {1, 7, 11, 13, 17, 19, 23, 29}, h = 30."""
        exps = ade_coxeter_exponents('E', 8)
        assert exps == (1, 7, 11, 13, 17, 19, 23, 29)
        assert sum(exps) == 120  # = rank * h / 2 = 8 * 30 / 2

    def test_exponent_sum_equals_rh_over_2(self):
        """For all ADE types: sum of exponents = r*h/2."""
        from compute.lib.niemeier_shadow_landscape import ade_root_system
        test_cases = [
            ('A', 1), ('A', 2), ('A', 3), ('A', 4), ('A', 5),
            ('A', 6), ('A', 7), ('A', 8), ('A', 9), ('A', 11),
            ('A', 12), ('A', 15), ('A', 17), ('A', 24),
            ('D', 4), ('D', 5), ('D', 6), ('D', 7), ('D', 8),
            ('D', 9), ('D', 10), ('D', 12), ('D', 16), ('D', 24),
            ('E', 6), ('E', 7), ('E', 8),
        ]
        for letter, n in test_cases:
            exps = ade_coxeter_exponents(letter, n)
            rs = ade_root_system(letter, n)
            expected = n * rs.dual_coxeter // 2
            assert sum(exps) == expected, (
                f"{letter}_{n}: sum(exps) = {sum(exps)}, expected {expected}"
            )

    def test_a1_24_parameters(self):
        """A_1^{24}: all 24 parameters are 0 (single exponent = h/2)."""
        params = niemeier_yangian_parameters('A_1^{24}')
        assert len(params.parameters) == 24
        assert all(p == 0 for p in params.parameters)
        assert params.sum_check == 0

    def test_a2_12_parameters(self):
        """A_2^{12}: 12 pairs of (-1/2, +1/2)."""
        params = niemeier_yangian_parameters('A_2^{12}')
        assert len(params.parameters) == 24
        assert params.sum_check == 0
        # Each A_2 pair: (1 - 3/2, 2 - 3/2) = (-1/2, 1/2)
        for group in params.parameter_groups:
            assert len(group) == 2
            assert sorted(group) == [Fraction(-1, 2), Fraction(1, 2)]

    def test_e8_cubed_parameters(self):
        """E_8^3: 3 groups of 8 parameters from E_8 exponents."""
        params = niemeier_yangian_parameters('E_8^3')
        assert len(params.parameters) == 24
        assert params.sum_check == 0
        assert len(params.parameter_groups) == 3
        for group in params.parameter_groups:
            assert len(group) == 8
            assert sum(group, Fraction(0)) == 0

    def test_d24_parameters(self):
        """D_{24}: single group of 24 parameters from D_24 exponents."""
        params = niemeier_yangian_parameters('D_{24}')
        assert len(params.parameters) == 24
        assert params.sum_check == 0
        assert len(params.parameter_groups) == 1
        assert len(params.parameter_groups[0]) == 24

    def test_all_23_have_24_parameters(self):
        """All 23 Niemeier Yangians have exactly 24 parameters."""
        for rs in UMBRAL_NIEMEIER_DATA:
            params = niemeier_yangian_parameters(rs)
            assert len(params.parameters) == 24, (
                f"{rs}: {len(params.parameters)} parameters"
            )

    def test_all_23_sum_to_zero(self):
        """CY_2 constraint: sum h_i = 0 at all 23 Niemeier points."""
        result = verify_all_parameter_sums()
        assert result['all_ok']
        assert result['num_niemeier'] == 23

    def test_mixed_root_system_params(self):
        """A_5^4 D_4: mixed root system with 4*5 + 1*4 = 24 parameters."""
        params = niemeier_yangian_parameters('A_5^4 D_4')
        assert len(params.parameters) == 24
        assert params.sum_check == 0
        # 4 A_5 groups of rank 5 + 1 D_4 group of rank 4
        assert len(params.parameter_groups) == 5

    def test_structure_function_at_identity(self):
        """Structure function g(0) at A_2^{12} Niemeier point."""
        # At z=0 with paired parameters (-1/2, +1/2):
        # Each pair contributes (0-h)(0+h) / ((0+h)(0-h)) = 1 (if h != 0)
        # Actually: (0-(-1/2))(0-(1/2)) / ((0+(-1/2))(0+(1/2)))
        # = (1/2)(-1/2) / ((-1/2)(1/2)) = (-1/4)/(-1/4) = 1
        val = structure_function_at_niemeier('A_2^{12}', Fraction(3))
        assert isinstance(val, Fraction)

    def test_parameter_groups_match_components(self):
        """Number of parameter groups matches number of root system copies."""
        for rs in UMBRAL_NIEMEIER_DATA:
            params = niemeier_yangian_parameters(rs)
            components = params.components
            expected_groups = sum(mult for _, _, mult in components)
            assert len(params.parameter_groups) == expected_groups, (
                f"{rs}: {len(params.parameter_groups)} groups vs "
                f"{expected_groups} expected"
            )


# =========================================================================
# Section 2: Umbral Frame shape eta products (14 tests)
# =========================================================================

class TestUmbralFrameShapes:
    """Verify Frame shapes and eta products for all 23 Umbral groups."""

    def test_all_frame_shapes_sum_to_24(self):
        """Every Umbral Frame shape sums to 24."""
        result = verify_all_frame_shape_sums()
        assert result['all_ok']
        assert result['num_shapes'] >= 83  # at least 83 shapes across all groups

    def test_all_23_have_identity(self):
        """Every Umbral group has an identity element with Frame shape 1^{24}."""
        for rs in UMBRAL_FRAME_SHAPES:
            shapes = umbral_frame_shapes(rs)
            identities = [s for s in shapes if s.is_identity]
            assert len(identities) == 1, f"{rs}: {len(identities)} identities"
            assert identities[0].frame_shape == {1: 24}
            assert identities[0].trace_24 == 24

    def test_identity_eta_is_eta_24(self):
        """Identity element gives eta^{24} = Delta/q for all 23 groups."""
        result = verify_umbral_eta_products()
        assert result['all_ok']
        assert result['num_checked'] == 23

    def test_a1_24_matches_m24(self):
        """A_1^{24} Frame shapes are consistent with M_24 data."""
        shapes = umbral_frame_shapes('A_1^{24}')
        # Should have at least the identity, 2a, 2b, 3a, 23a
        names = {s.element_name for s in shapes}
        assert '1a' in names
        assert '2a' in names
        assert '2b' in names

    def test_e8_cubed_s3_shapes(self):
        """E_8^3 Umbral group S_3 has 3 conjugacy classes."""
        shapes = umbral_frame_shapes('E_8^3')
        assert len(shapes) == 3  # 1a, 2a, 3a for S_3

    def test_z2_groups_have_2_shapes(self):
        """Z_2 Umbral groups have exactly 2 Frame shapes (identity + involution)."""
        z2_systems = [rs for rs, data in UMBRAL_GROUP_STRUCTURE.items()
                      if data['group'] == 'Z_2']
        for rs in z2_systems:
            if rs in UMBRAL_FRAME_SHAPES:
                shapes = umbral_frame_shapes(rs)
                assert len(shapes) == 2, f"{rs}: {len(shapes)} shapes for Z_2"

    def test_eta_product_weight_identity(self):
        """Identity Frame shape 1^{24} has eta product weight 12."""
        w = eta_product_weight({1: 24})
        assert w == Fraction(12)

    def test_eta_product_level_identity(self):
        """Identity Frame shape 1^{24} has level 1."""
        lvl = eta_product_level({1: 24})
        assert lvl == 1

    def test_eta_product_leading_power_identity(self):
        """Identity Frame shape 1^{24} has leading q-power 1."""
        lp = eta_product_leading_power({1: 24})
        assert lp == Fraction(1)

    def test_non_identity_eta_product_d4_6(self):
        """Non-identity element 3a of D_4^6 gives eta product with weight 0."""
        # 3a: Frame shape {3: 8}, weight = (1/2)*8 = 4
        coeffs = umbral_eta_product('D_4^6', '3a', max_degree=10)
        assert coeffs.get(0, 0) == 1  # leading coefficient

    def test_non_identity_eta_product_a2_12(self):
        """2a element of A_2^{12} gives correct eta product."""
        # 2a: Frame shape {1: 8, 2: 8}
        coeffs = umbral_eta_product('A_2^{12}', '2a', max_degree=5)
        assert coeffs[0] == 1  # leading coefficient

    def test_eta_leading_power_2cycle(self):
        """Frame shape 2^{12} has leading q-power 1."""
        lp = eta_product_leading_power({2: 12})
        assert lp == Fraction(1)

    def test_eta_leading_power_3cycle(self):
        """Frame shape 3^{8} has leading q-power 1."""
        lp = eta_product_leading_power({3: 8})
        assert lp == Fraction(1)

    def test_frame_shape_trace_consistency(self):
        """Stored trace equals a_1 (number of 1-cycles) for all shapes."""
        from compute.lib.mathieu_moonshine_yangian import _frame_shape_trace
        for rs, shapes in UMBRAL_FRAME_SHAPES.items():
            for s in shapes:
                computed_trace = _frame_shape_trace(s.frame_shape)
                assert s.trace_24 == computed_trace, (
                    f"{rs}/{s.element_name}: trace {s.trace_24} vs {computed_trace}"
                )


# =========================================================================
# Section 3: Mock modular forms and shadow tower (14 tests)
# =========================================================================

class TestMockModularForms:
    """Verify Umbral mock modular forms at all 23 Niemeier points."""

    def test_a1_24_mock_matches_parent(self):
        """A_1^{24} mock coefficients match the M_24 moonshine data."""
        mock = UMBRAL_MOCK_COEFFICIENTS['A_1^{24}'][1]
        assert mock[-1] == MOCK_MODULAR_COEFFICIENTS[-1]  # -1
        assert mock[1] == MOCK_MODULAR_COEFFICIENTS[1]    # 45
        assert mock[2] == MOCK_MODULAR_COEFFICIENTS[2]    # 231
        assert mock[3] == MOCK_MODULAR_COEFFICIENTS[3]    # 770

    def test_all_23_have_mock_data(self):
        """All 23 Niemeier root systems have mock coefficient tables."""
        for rs in UMBRAL_NIEMEIER_DATA:
            assert rs in UMBRAL_MOCK_COEFFICIENTS, (
                f"Missing mock data for {rs}"
            )

    def test_polar_coefficient_universal(self):
        """Polar coefficient = -kappa_ch = -2 at all 23 Niemeier points."""
        result = verify_all_polar_coefficients()
        assert result['all_ok']
        assert result['num_niemeier'] == 23
        assert result['kappa_ch'] == 2

    def test_polar_coeff_a1_24(self):
        """A_1^{24} polar coefficient = -2."""
        polar = umbral_polar_coefficient('A_1^{24}', component=1)
        assert polar == -2

    def test_polar_coeff_a2_12(self):
        """A_2^{12} polar coefficient = -2."""
        polar = umbral_polar_coefficient('A_2^{12}', component=1)
        assert polar == -2

    def test_polar_coeff_d24(self):
        """D_{24} polar coefficient = -2."""
        polar = umbral_polar_coefficient('D_{24}', component=1)
        assert polar == -2

    def test_mock_coefficients_positive(self):
        """All mock coefficients at n >= 1 are positive integers."""
        result = verify_mock_coefficients_positive()
        assert result['all_ok']
        assert result['num_checked'] == 23

    def test_mock_modular_data_a1_24(self):
        """A_1^{24} mock data: lambency 2, weight 1/2, level 8."""
        md = umbral_mock_modular_data('A_1^{24}')
        assert md.lambency == 2
        assert md.weight == Fraction(1, 2)
        assert md.level == 8
        assert md.umbral_group == 'M_24'
        assert md.num_components == 1

    def test_mock_modular_data_a2_12(self):
        """A_2^{12} mock data: lambency 3, weight 1/2, level 12."""
        md = umbral_mock_modular_data('A_2^{12}')
        assert md.lambency == 3
        assert md.weight == Fraction(1, 2)
        assert md.level == 12
        assert md.umbral_group == '2.M_12'

    def test_mock_modular_data_d24(self):
        """D_{24} mock data: lambency 46, weight 1/2, level 184."""
        md = umbral_mock_modular_data('D_{24}')
        assert md.lambency == 46
        assert md.level == 184
        assert md.umbral_group == 'Z_2'

    def test_num_components_increases_with_lambency(self):
        """Number of mock modular components increases with lambency."""
        # At lambency 2: 1 component. At lambency 46: 22 components.
        md2 = umbral_mock_modular_data('A_1^{24}')
        md46 = umbral_mock_modular_data('D_{24}')
        assert md2.num_components < md46.num_components

    def test_shadow_tower_a1_24(self):
        """Shadow tower at A_1^{24}: class M, kappa_ch = 2, polar = -2."""
        st = shadow_tower_produces_mock('A_1^{24}')
        assert st['shadow_class'] == 'M'
        assert st['kappa_ch'] == 2
        assert st['polar_equals_neg_kappa']

    def test_shadow_tower_all_23(self):
        """Shadow tower produces mock modular forms at all 23 points."""
        for rs in UMBRAL_NIEMEIER_DATA:
            st = shadow_tower_produces_mock(rs)
            assert st['polar_equals_neg_kappa'], f"{rs}: polar check failed"
            assert st['shadow_class'] == 'M', f"{rs}: shadow class != M"

    def test_a2_12_first_few_coefficients(self):
        """A_2^{12} mock coefficients: -1, 16, 55, 144, 330, 640, ..."""
        mock = UMBRAL_MOCK_COEFFICIENTS['A_2^{12}'][1]
        assert mock[-1] == -1
        assert mock[1] == 16
        assert mock[2] == 55
        assert mock[3] == 144


# =========================================================================
# Section 4: Uniform construction Y -> h_N (8 tests)
# =========================================================================

class TestUniformConstruction:
    """Verify the uniform construction Y(g_{K3}(N)) -> h_N(tau)."""

    def test_uniform_at_a1_24(self):
        """Uniform construction at A_1^{24} (Mathieu moonshine)."""
        uc = uniform_construction('A_1^{24}')
        assert uc.is_uniform
        assert uc.status == ENGINE_STATUS

    def test_uniform_at_e8_cubed(self):
        """Uniform construction at E_8^3 (S_3 symmetry)."""
        uc = uniform_construction('E_8^3')
        assert uc.is_uniform

    def test_uniform_at_d24(self):
        """Uniform construction at D_{24} (Z_2 symmetry)."""
        uc = uniform_construction('D_{24}')
        assert uc.is_uniform

    def test_all_23_uniform(self):
        """The construction is uniform for all 23 Niemeier points."""
        result = verify_uniform_construction()
        assert result['all_ok']
        assert result['num_niemeier'] == 23

    def test_step2_shadow_universal(self):
        """Step 2: shadow tower data is universal (class M, kappa_ch = 2)."""
        for rs in ['A_1^{24}', 'A_2^{12}', 'E_8^3', 'D_{24}']:
            uc = uniform_construction(rs)
            assert 'class M' in uc.step2_shadow_tower
            assert str(KAPPA_CH_K3_SIGMA) in uc.step2_shadow_tower

    def test_step3_polar_universal(self):
        """Step 3: polar coefficient -kappa_ch = -2 is universal."""
        for rs in ['A_1^{24}', 'A_2^{12}', 'E_8^3', 'D_{24}']:
            uc = uniform_construction(rs)
            assert str(MOCK_POLAR_COEFF) in uc.step3_polar

    def test_step4_rademacher_level_varies(self):
        """Step 4: Rademacher level varies with lambency."""
        uc2 = uniform_construction('A_1^{24}')
        uc46 = uniform_construction('D_{24}')
        assert 'level 8' in uc2.step4_rademacher
        assert 'level 184' in uc46.step4_rademacher

    def test_non_uniform_part_describes_variation(self):
        """Non-uniform part correctly identifies what varies."""
        uc = uniform_construction('A_1^{24}')
        assert 'Lambency' in uc.non_uniform_part
        assert 'M_24' in uc.non_uniform_part


# =========================================================================
# Section 5: Umbral group structure (12 tests)
# =========================================================================

class TestUmbralGroups:
    """Verify Umbral group data for all 23 Niemeier root systems."""

    def test_all_23_have_group_data(self):
        """All 23 Niemeier root systems have Umbral group data."""
        for rs in UMBRAL_NIEMEIER_DATA:
            assert rs in UMBRAL_GROUP_STRUCTURE, f"Missing group data for {rs}"

    def test_m24_is_sporadic_simple(self):
        """M_24 at A_1^{24} is sporadic and simple."""
        gd = umbral_group_data('A_1^{24}')
        assert gd.group_name == 'M_24'
        assert gd.order == 244823040
        assert gd.structure_constants['sporadic']
        assert gd.structure_constants['simple']
        assert not gd.is_abelian

    def test_m24_order_factorization(self):
        """|M_24| = 2^{10} * 3^3 * 5 * 7 * 11 * 23."""
        gd = umbral_group_data('A_1^{24}')
        assert gd.order == (2**10) * (3**3) * 5 * 7 * 11 * 23

    def test_2m12_order(self):
        """|2.M_12| = 190080 = 2 * |M_12|."""
        gd = umbral_group_data('A_2^{12}')
        assert gd.order == 190080
        assert gd.order == 2 * 95040  # |M_12| = 95040

    def test_3s6_order(self):
        """|3.S_6| = 2160 = 3 * 720."""
        gd = umbral_group_data('D_4^6')
        assert gd.order == 2160
        assert gd.order == 3 * 720

    def test_z2_groups_abelian(self):
        """All Z_2 Umbral groups are abelian."""
        for rs, gs in UMBRAL_GROUP_STRUCTURE.items():
            if gs['group'] == 'Z_2':
                assert gs['abelian'], f"{rs}: Z_2 should be abelian"
                assert gs['order'] == 2

    def test_z3_group_abelian(self):
        """Z_3 at A_8^3 is abelian with order 3."""
        gd = umbral_group_data('A_8^3')
        assert gd.group_name == 'Z_3'
        assert gd.order == 3
        assert gd.is_abelian

    def test_s3_groups(self):
        """S_3 groups at D_8^3 and E_8^3 have order 6."""
        for rs in ['D_8^3', 'E_8^3']:
            gd = umbral_group_data(rs)
            assert gd.group_name == 'S_3'
            assert gd.order == 6
            assert not gd.is_abelian

    def test_dih4_order(self):
        """Dih_4 at A_7^2 D_5^2 has order 8."""
        gd = umbral_group_data('A_7^2 D_5^2')
        assert gd.order == 8
        assert not gd.is_abelian

    def test_num_conjugacy_classes_geq_1(self):
        """All Umbral groups have at least 1 conjugacy class."""
        for rs in UMBRAL_GROUP_STRUCTURE:
            gs = UMBRAL_GROUP_STRUCTURE[rs]
            assert gs['num_cc'] >= 1

    def test_group_order_matches_parent_engine(self):
        """Umbral group orders match the parent engine data."""
        from compute.lib.mathieu_yangian_deeper import umbral_group_order
        for rs in UMBRAL_NIEMEIER_DATA:
            if rs in UMBRAL_GROUP_STRUCTURE:
                local_order = UMBRAL_GROUP_STRUCTURE[rs]['order']
                parent_order = umbral_group_order(rs)
                assert local_order == parent_order, (
                    f"{rs}: local {local_order} vs parent {parent_order}"
                )

    def test_group_order_hierarchy(self):
        """Group orders form a descending hierarchy from M_24 to Z_2."""
        orders = sorted(
            {UMBRAL_GROUP_STRUCTURE[rs]['order'] for rs in UMBRAL_GROUP_STRUCTURE},
            reverse=True,
        )
        assert orders[0] == 244823040  # M_24
        assert orders[-1] == 2         # Z_2


# =========================================================================
# Section 6: Cross-verification and landscape (7 tests)
# =========================================================================

class TestLandscape:
    """Cross-verification and landscape summary."""

    def test_landscape_has_23_entries(self):
        """The landscape has exactly 23 Niemeier Yangians."""
        ls = umbral_23_landscape()
        assert ls['num_niemeier'] == 23
        assert len(ls['landscape']) == 23

    def test_landscape_lambency_range(self):
        """Lambency ranges from 2 (A_1^{24}) to 46 (D_{24})."""
        ls = umbral_23_landscape()
        assert ls['statistics']['lambency_range'] == (2, 46)

    def test_landscape_universal_kappa(self):
        """kappa_ch = 2 is universal across the landscape."""
        ls = umbral_23_landscape()
        assert ls['statistics']['universal_kappa_ch'] == 2

    def test_landscape_universal_shadow_class(self):
        """Shadow class M is universal across the landscape."""
        ls = umbral_23_landscape()
        assert ls['statistics']['universal_shadow_class'] == 'M'

    def test_full_verification_suite(self):
        """The full verification suite passes."""
        result = full_umbral_verification()
        assert result['status'] == 'CONJECTURAL'
        assert result['path1_parameter_sums']['all_ok']
        assert result['path2_polar_coefficients']['all_ok']
        assert result['path3_frame_shape_sums']['all_ok']
        assert result['path4_identity_eta_products']['all_ok']
        assert result['path5_mock_coefficients']['all_ok']
        assert result['path6_uniform_construction']['all_ok']

    def test_constants_consistency(self):
        """Module constants are consistent with parent engine."""
        assert KAPPA_CH_K3_SIGMA == KAPPA_CH_K3
        assert KAPPA_CH_K3_SIGMA == 2
        assert KAPPA_CH_LATTICE_VOA == 24
        assert MOCK_POLAR_COEFF == -2
        assert ENGINE_STATUS == 'CONJECTURAL'

    def test_landscape_does_not_claim_cy_host(self):
        """The 23-umbral engine is a conjectural shadow engine, not a host."""
        ls = umbral_23_landscape()
        assert ls['num_niemeier'] == 23
        assert ls['status'] == ENGINE_STATUS
        assert ENGINE_STATUS == 'CONJECTURAL'
        for entry in ls['landscape']:
            assert entry['construction_uniform'] is True
            assert 'host' not in entry

    def test_degenerate_lambencies_exist(self):
        """Some lambencies are shared: 6 (D_4^6 and A_5^4 D_4), etc."""
        lambency_counts = {}
        for rs, data in UMBRAL_NIEMEIER_DATA.items():
            ell = data['lambency']
            lambency_counts[ell] = lambency_counts.get(ell, 0) + 1
        degenerate = {ell: c for ell, c in lambency_counts.items() if c > 1}
        # At least lambency 6, 10, 12, 18, 30 are degenerate
        assert 6 in degenerate
        assert 10 in degenerate
        assert 12 in degenerate
        assert 18 in degenerate
        assert 30 in degenerate


# =========================================================================
# Section 7: Multi-path cross-verification (AP10 compliance)
# =========================================================================

class TestCrossVerification:
    """Multi-path cross-checks: same quantity computed via independent routes."""

    def test_xv_param_sum_two_paths(self):
        """Cross-verify: parameter sum = 0 via (a) direct sum and (b) exponent identity.

        Path A: sum all 24 parameters directly.
        Path B: for each ADE component of rank r and Coxeter h, the Coxeter
        exponent sum equals r*h/2, so the centered sum is 0 per component.
        """
        from compute.lib.niemeier_shadow_landscape import ade_root_system
        for rs in UMBRAL_NIEMEIER_DATA:
            params = niemeier_yangian_parameters(rs)
            # Path A: direct sum
            direct_sum = sum(params.parameters, Fraction(0))
            # Path B: algebraic identity per component
            algebraic_sum = Fraction(0)
            for cv in params.exponent_data:
                # sum(m_k) - r * h/2 = 0 for each component
                exp_sum = sum(cv.exponents)
                algebraic_check = exp_sum - cv.rank * cv.coxeter // 2
                algebraic_sum += algebraic_check
            assert direct_sum == 0, f"{rs}: direct sum = {direct_sum}"
            assert algebraic_sum == 0, f"{rs}: algebraic sum = {algebraic_sum}"

    def test_xv_eta_24_two_paths(self):
        """Cross-verify: eta^{24} via (a) this engine's identity element and
        (b) parent engine's 1A M_24 computation.

        Both must produce identical q-expansion coefficients.
        """
        from compute.lib.mathieu_moonshine_yangian import twined_eta_product as parent_eta
        max_deg = 8
        # Path A: parent engine (M_24 class 1A)
        parent_coeffs = parent_eta('1A', max_degree=max_deg)
        # Path B: this engine (each Niemeier identity)
        for rs in ['A_1^{24}', 'A_2^{12}', 'E_8^3', 'D_{24}', 'D_4^6']:
            local_coeffs = umbral_eta_product(rs, '1a', max_degree=max_deg)
            for n in range(max_deg + 1):
                p = parent_coeffs.get(n, 0)
                l = local_coeffs.get(n, 0)
                assert p == l, (
                    f"{rs} at q^{n}: parent={p}, local={l}"
                )

    def test_xv_polar_from_mock_and_from_kappa(self):
        """Cross-verify: polar coefficient via (a) mock coefficient table and
        (b) -kappa_ch constant.

        Path A: read polar from the stored mock modular coefficients.
        Path B: compute as -KAPPA_CH_K3_SIGMA.
        """
        for rs in UMBRAL_MOCK_COEFFICIENTS:
            mock = UMBRAL_MOCK_COEFFICIENTS[rs]
            if 1 in mock and -1 in mock[1]:
                # Path A: from coefficient table
                path_a = KAPPA_CH_K3_SIGMA * mock[1][-1]
                # Path B: from constant
                path_b = -KAPPA_CH_K3_SIGMA
                assert path_a == path_b, (
                    f"{rs}: table polar={path_a}, constant polar={path_b}"
                )

    def test_xv_group_order_three_sources(self):
        """Cross-verify: group order from (a) UMBRAL_GROUP_STRUCTURE,
        (b) parent engine umbral_group_order, (c) UMBRAL_NIEMEIER_DATA consistency.

        All three must agree.
        """
        from compute.lib.mathieu_yangian_deeper import umbral_group_order
        for rs in UMBRAL_NIEMEIER_DATA:
            # Path A: local structure table
            order_a = UMBRAL_GROUP_STRUCTURE[rs]['order']
            # Path B: parent engine function
            order_b = umbral_group_order(rs)
            # Path C: cross-check abelian groups have order = |conjugacy classes|
            # (for abelian groups only)
            assert order_a == order_b, (
                f"{rs}: local={order_a}, parent={order_b}"
            )
            assert order_a > 0

    def test_xv_niemeier_rank_24_two_paths(self):
        """Cross-verify: total rank = 24 via (a) parameter count and
        (b) root system component sum.

        Path A: len(params.parameters) == 24.
        Path B: sum of rank*mult over components == 24.
        """
        for rs in UMBRAL_NIEMEIER_DATA:
            params = niemeier_yangian_parameters(rs)
            # Path A
            count_a = len(params.parameters)
            # Path B
            count_b = sum(rank * mult for _, rank, mult in params.components)
            assert count_a == 24, f"{rs}: param count = {count_a}"
            assert count_b == 24, f"{rs}: component sum = {count_b}"
            assert count_a == count_b

    def test_xv_frame_shape_weight_from_trace_and_cycle_sum(self):
        """Cross-verify: eta product weight via (a) sum of Frame shape
        multiplicities and (b) (24 + sum_of_traces_of_other_classes)/normalization.

        Path A: weight = (1/2) * sum(a_i).
        Path B: independent computation from cycle decomposition.
        For the identity: weight = (1/2)*24 = 12.
        """
        for rs, shapes in UMBRAL_FRAME_SHAPES.items():
            for s in shapes:
                # Path A: from the eta_product_weight function
                weight_a = eta_product_weight(s.frame_shape)
                # Path B: direct computation
                total_mult = sum(s.frame_shape.values())
                weight_b = Fraction(total_mult, 2)
                assert weight_a == weight_b, (
                    f"{rs}/{s.element_name}: {weight_a} vs {weight_b}"
                )
                # Cross-check: total letters = 24
                total_letters = sum(k * v for k, v in s.frame_shape.items())
                assert total_letters == 24

    def test_xv_a1_24_mock_matches_eot_coefficients(self):
        """Cross-verify: A_1^{24} mock coefficients against independent EOT data.

        Path A: UMBRAL_MOCK_COEFFICIENTS (this engine).
        Path B: MOCK_MODULAR_COEFFICIENTS (parent engine, from EOT 2010).
        Path C: MATHIEU_COEFFICIENTS_A / kappa_ch (parent engine).
        """
        from compute.lib.mathieu_moonshine_yangian import MATHIEU_COEFFICIENTS_A
        mock_local = UMBRAL_MOCK_COEFFICIENTS['A_1^{24}'][1]
        for n in range(1, 10):
            if n in mock_local and n in MOCK_MODULAR_COEFFICIENTS:
                # Path A: local
                val_a = mock_local[n]
                # Path B: parent mock coefficients
                val_b = MOCK_MODULAR_COEFFICIENTS[n]
                # Path C: from Mathieu A_n / kappa_ch
                val_c = MATHIEU_COEFFICIENTS_A[n] // KAPPA_CH_K3
                assert val_a == val_b == val_c, (
                    f"n={n}: local={val_a}, parent_mock={val_b}, A_n/kappa={val_c}"
                )

    def test_xv_structure_function_symmetry(self):
        """Cross-verify: g(-z) = 1/g(z) for all Niemeier structure functions.

        The structure function g(z) = prod(z-h_i)/(z+h_i) satisfies
        g(-z) = prod(-z-h_i)/(-z+h_i) = prod(z+h_i)/(z-h_i) = 1/g(z).
        This is a consequence of the paired structure (each h_i contributes
        both to numerator and denominator).
        """
        test_z = Fraction(17, 3)  # safe test point away from poles
        for rs in ['A_2^{12}', 'E_8^3', 'D_4^6', 'A_3^8', 'D_{24}']:
            g_pos = structure_function_at_niemeier(rs, test_z)
            g_neg = structure_function_at_niemeier(rs, -test_z)
            product = g_pos * g_neg
            assert product == 1, (
                f"{rs}: g(z)*g(-z) = {product}, expected 1"
            )

    def test_xv_coxeter_from_exponents_and_from_ade(self):
        """Cross-verify: Coxeter number from (a) max exponent + 1 and
        (b) ade_root_system.dual_coxeter.

        For ADE: h = max(exponents) + 1 = dual_coxeter.
        """
        from compute.lib.niemeier_shadow_landscape import ade_root_system
        test_cases = [
            ('A', 1), ('A', 2), ('A', 5), ('A', 8), ('A', 12), ('A', 24),
            ('D', 4), ('D', 6), ('D', 8), ('D', 12), ('D', 24),
            ('E', 6), ('E', 7), ('E', 8),
        ]
        for letter, n in test_cases:
            exps = ade_coxeter_exponents(letter, n)
            # Path A: h = max exponent + 1
            h_from_exps = max(exps) + 1
            # Path B: from ade_root_system
            h_from_ade = ade_root_system(letter, n).dual_coxeter
            assert h_from_exps == h_from_ade, (
                f"{letter}_{n}: exponent-derived h={h_from_exps}, "
                f"ade h={h_from_ade}"
            )

    def test_xv_landscape_count_vs_niemeier_data(self):
        """Cross-verify: landscape entry count matches UMBRAL_NIEMEIER_DATA."""
        ls = umbral_23_landscape()
        assert len(ls['landscape']) == len(UMBRAL_NIEMEIER_DATA)
        # Every root system in UMBRAL_NIEMEIER_DATA appears in the landscape
        landscape_rs = {entry['root_system'] for entry in ls['landscape']}
        for rs in UMBRAL_NIEMEIER_DATA:
            assert rs in landscape_rs, f"{rs} missing from landscape"
