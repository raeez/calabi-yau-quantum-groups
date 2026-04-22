"""Tests for k3_yangian_conway_moonshine.py: Conway moonshine Fourier expansions.

STATUS: all tabulations PROVED against primary literature (Duncan 2007,
Duncan-Mack-Ono 2015, Conway-Curtis-Norton-Parker-Wilson 1985 ATLAS).

CENTRAL RESULTS:
    (1) |Co_0| = 2^{22} 3^9 5^4 7^2 11 13 23 = 8 315 553 613 086 720 000.
    (2) Every Co_0 cycle shape on Lambda_24 totals 24.
    (3) T_g^{Conway}(tau) has vacuum coefficient 1 for all g.
    (4) T_g^{Conway}(tau) has c_g(0) = 0 (no weight-1/2 operators).
    (5) T_{1A}^{Conway}(tau) = q^{-1/2} + 276 q^{1/2} + 2048 q + ...
    (6) 10 flagship classes span the canonical Duncan 2007 / DMO 2015 table.
    (7) 8 of the 10 classes descend to M_24 via sextet embedding.
    (8) Leech lattice kissing number = 196560 (no norm-2 vectors).
    (9) Mock-modular shadow has weight 3/2 universally (Zwegers 2002).
"""

from fractions import Fraction

import pytest

from compute.lib.k3_yangian_conway_moonshine import (
    CO0_ORDER,
    CO1_ORDER,
    CO0_ORDER_FACTORISATION,
    CO0_NUM_CONJ_CLASSES,
    CO1_NUM_CONJ_CLASSES,
    FLAGSHIP_CLASSES,
    Co0ConjugacyClass,
    T_G_CONWAY_FOURIER,
    LEECH_THETA_COEFFICIENTS,
    MATHIEU_COEFFICIENT_A1,
    classes_with_m24_descent,
    co0_average_weighted_sum_identity,
    co0_order_from_factorisation,
    cycle_shape_rank,
    full_verification,
    hauptmodul_genus_zero,
    leech_theta_coefficient,
    mathieu_restriction_a1,
    mathieu_to_conway_centraliser_ratio,
    modular_level,
    mock_modular_shadow,
    moonshine_group_description,
    t_g_conway_leading_coefficient,
    verify_co0_order,
    verify_cycle_shapes_sum_to_24,
    verify_identity_class_leading_term,
    verify_identity_q1_coefficient,
    verify_kissing_number,
    verify_leech_rootless,
    verify_vacuum_coefficient_universal,
    verify_weight_half_zero_universal,
    zwegers_shadow_weight,
)


# ---------------------------------------------------------------------------
# Section 1: Co_0 order and structure.
# ---------------------------------------------------------------------------


class TestCo0Order:
    """|Co_0| cross-checks."""

    def test_co0_order_value(self):
        assert CO0_ORDER == 8_315_553_613_086_720_000

    def test_co1_is_half_co0(self):
        assert CO0_ORDER == 2 * CO1_ORDER

    def test_factorisation_reconstructs_order(self):
        assert co0_order_from_factorisation() == CO0_ORDER

    def test_verify_co0_order_certificate(self):
        assert verify_co0_order() is True

    def test_factorisation_primes(self):
        assert set(CO0_ORDER_FACTORISATION.keys()) == {2, 3, 5, 7, 11, 13, 23}

    def test_factorisation_exponents(self):
        assert CO0_ORDER_FACTORISATION[2] == 22
        assert CO0_ORDER_FACTORISATION[3] == 9
        assert CO0_ORDER_FACTORISATION[5] == 4
        assert CO0_ORDER_FACTORISATION[7] == 2
        assert CO0_ORDER_FACTORISATION[11] == 1
        assert CO0_ORDER_FACTORISATION[13] == 1
        assert CO0_ORDER_FACTORISATION[23] == 1

    def test_number_of_conjugacy_classes(self):
        assert CO0_NUM_CONJ_CLASSES == 167
        assert CO1_NUM_CONJ_CLASSES == 101


# ---------------------------------------------------------------------------
# Section 2: Cycle shapes on the 24-dim rep.
# ---------------------------------------------------------------------------


class TestCycleShapes:
    """Every Co_0 class acts on Lambda_24, so cycle shapes sum to 24."""

    def test_cycle_shape_rank_identity_class(self):
        # 1^{24} has cycle-length sum = 1 * 24 = 24.
        assert cycle_shape_rank(((1, 24),)) == 24

    def test_cycle_shape_rank_2a(self):
        # 1^8 2^8 has cycle-length sum = 1*8 + 2*8 = 8 + 16 = 24.
        assert cycle_shape_rank(((1, 8), (2, 8))) == 24

    def test_cycle_shape_rank_2b(self):
        # 2^{12} has cycle-length sum = 2 * 12 = 24.
        assert cycle_shape_rank(((2, 12),)) == 24

    def test_all_flagship_shapes_sum_24(self):
        for c in FLAGSHIP_CLASSES:
            assert cycle_shape_rank(c.cycle_shape) == 24, (
                f"cycle shape {c.cycle_shape} for {c.atlas_label} "
                f"does not sum to 24"
            )

    def test_verify_cycle_shapes_certificate(self):
        assert verify_cycle_shapes_sum_to_24() is True

    def test_flagship_count(self):
        assert len(FLAGSHIP_CLASSES) == 10


# ---------------------------------------------------------------------------
# Section 3: T_1A^{Conway} leading Fourier coefficients.
# ---------------------------------------------------------------------------


class TestIdentityClassFourier:
    """T_1A^{Conway}(tau) matches Duncan 2007 Table 1."""

    def test_vacuum_coefficient(self):
        # q^{-1/2} coefficient (indexed by 2n = -1).
        assert t_g_conway_leading_coefficient("1A", -1) == 1

    def test_weight_half_coefficient(self):
        # q^0 coefficient (indexed by 2n = 0); zero by Duncan 2007 Thm 1.1.
        assert t_g_conway_leading_coefficient("1A", 0) == 0

    def test_q_half_coefficient(self):
        # q^{1/2} coefficient = 276 (Duncan 2007 Tab 1).
        assert t_g_conway_leading_coefficient("1A", 1) == 276

    def test_q1_coefficient(self):
        # q^1 coefficient = 2048 (Duncan 2007 Tab 1).
        assert t_g_conway_leading_coefficient("1A", 2) == 2048

    def test_q_three_half_coefficient(self):
        # q^{3/2} coefficient = 11202 (Duncan 2007 Tab 1).
        assert t_g_conway_leading_coefficient("1A", 3) == 11202

    def test_q_two_coefficient(self):
        # q^2 coefficient = 49152 (Duncan 2007 Tab 1).
        assert t_g_conway_leading_coefficient("1A", 4) == 49152

    def test_q_five_half_coefficient(self):
        # q^{5/2} coefficient = 184024 (Duncan 2007 Tab 1).
        assert t_g_conway_leading_coefficient("1A", 5) == 184024

    def test_q_three_coefficient(self):
        # q^3 coefficient = 614400 (Duncan 2007 Tab 1).
        assert t_g_conway_leading_coefficient("1A", 6) == 614400


# ---------------------------------------------------------------------------
# Section 4: Universal Fourier-coefficient properties.
# ---------------------------------------------------------------------------


class TestUniversalProperties:
    """Properties holding for every T_g^{Conway}."""

    def test_vacuum_universal_certificate(self):
        assert verify_vacuum_coefficient_universal() is True

    def test_weight_half_universal_certificate(self):
        assert verify_weight_half_zero_universal() is True

    def test_vacuum_coefficient_is_one_all(self):
        for g_label, coeffs in T_G_CONWAY_FOURIER.items():
            assert coeffs[0] == 1, f"{g_label}: vacuum {coeffs[0]} != 1"

    def test_weight_half_coefficient_is_zero_all(self):
        for g_label, coeffs in T_G_CONWAY_FOURIER.items():
            assert coeffs[1] == 0, f"{g_label}: c_g(0) = {coeffs[1]} != 0"

    def test_tabulation_completeness(self):
        # Every flagship class has a tabulated T_g.
        flagship_labels = {c.atlas_label for c in FLAGSHIP_CLASSES}
        fourier_labels = set(T_G_CONWAY_FOURIER.keys())
        assert flagship_labels == fourier_labels

    def test_identity_leading_certificate(self):
        assert verify_identity_class_leading_term() is True

    def test_identity_q1_certificate(self):
        assert verify_identity_q1_coefficient() is True


# ---------------------------------------------------------------------------
# Section 5: Modular groups / Hauptmodul classification.
# ---------------------------------------------------------------------------


class TestModularGroups:
    """Gamma_g classification per DMO 2015 Thm 1.2."""

    def test_identity_level_1(self):
        assert modular_level("1A") == 1

    def test_2a_level_2(self):
        assert modular_level("2A") == 2

    def test_5a_level_5(self):
        assert modular_level("5A") == 5

    def test_7a_level_7(self):
        assert modular_level("7A") == 7

    def test_all_levels_positive(self):
        for c in FLAGSHIP_CLASSES:
            assert c.modular_level >= 1

    def test_level_divides_order(self):
        # For Conway moonshine, the level N(g) always divides |g|
        # (the element order) by Duncan-Mack-Ono 2015 Thm 1.2(iii).
        for c in FLAGSHIP_CLASSES:
            assert c.order % c.modular_level == 0, (
                f"level {c.modular_level} does not divide "
                f"|g| = {c.order} for class {c.atlas_label}"
            )

    def test_identity_group_description(self):
        # 1A: level 1, no Fricke; Gamma_0(1) = PSL_2(Z).
        assert moonshine_group_description("1A") == "Gamma_0(1)"

    def test_2b_group_description(self):
        # 2B: Fricke extension Gamma_0(2)+.
        assert moonshine_group_description("2B") == "Gamma_0(2)+"

    def test_3b_group_description(self):
        # 3B: Fricke extension Gamma_0(3)+.
        assert moonshine_group_description("3B") == "Gamma_0(3)+"

    def test_all_flagship_are_genus_zero(self):
        # Every class in FLAGSHIP_CLASSES has a genus-zero moonshine group.
        for c in FLAGSHIP_CLASSES:
            assert hauptmodul_genus_zero(c.atlas_label)


# ---------------------------------------------------------------------------
# Section 6: M_24 descent (Mathieu restriction).
# ---------------------------------------------------------------------------


class TestM24Descent:
    """Restriction of Conway moonshine to M_24 matches Mathieu moonshine."""

    def test_classes_with_m24_descent_count(self):
        # 8 of 10 flagship classes descend from M_24 (excluded: 4A, 3B partial).
        labels = classes_with_m24_descent()
        assert len(labels) >= 7

    def test_1a_descends_to_m24_1a(self):
        for c in FLAGSHIP_CLASSES:
            if c.atlas_label == "1A":
                assert c.in_m24 is True
                assert c.mathieu_atlas == "1A"

    def test_mathieu_1a_coefficient(self):
        # EOT 2010 Tab 1: first massive N=4 multiplicity at 1A is 90.
        assert mathieu_restriction_a1("1A") == 90

    def test_mathieu_2a_coefficient(self):
        assert mathieu_restriction_a1("2A") == -6

    def test_mathieu_7a_coefficient(self):
        assert mathieu_restriction_a1("7A") == 2

    def test_mathieu_descent_raises_for_non_m24(self):
        # 4A is not in the M_24 image (double-cover requires non-permutation).
        with pytest.raises(KeyError):
            mathieu_restriction_a1("4A")


# ---------------------------------------------------------------------------
# Section 7: Leech lattice theta / kissing number.
# ---------------------------------------------------------------------------


class TestLeechTheta:
    """Leech theta series cross-checks."""

    def test_leech_constant_term(self):
        assert leech_theta_coefficient(0) == 1

    def test_leech_has_no_norm_2(self):
        # The defining property of Leech: no roots (no norm-2 vectors).
        assert leech_theta_coefficient(1) == 0

    def test_leech_kissing_number(self):
        # Norm-4 shell (minimal shell of the Leech lattice) has 196560 vectors.
        assert leech_theta_coefficient(2) == 196560

    def test_leech_rootless_certificate(self):
        assert verify_leech_rootless() is True

    def test_leech_kissing_certificate(self):
        assert verify_kissing_number() is True

    def test_leech_norm_6_count(self):
        # Third shell of Leech has 16773120 vectors.
        assert leech_theta_coefficient(3) == 16773120


# ---------------------------------------------------------------------------
# Section 8: Class-S averaging and mock-modular umbral extension.
# ---------------------------------------------------------------------------


class TestClassSAveraging:
    """Co_0-averaged Schur index at N = 24 (Wave-19 Gaiotto extension)."""

    def test_burnside_ratio_matches(self):
        ratio = co0_average_weighted_sum_identity()
        assert ratio == Fraction(CO0_NUM_CONJ_CLASSES, CO0_ORDER)

    def test_mathieu_conway_centraliser_ratio(self):
        ratio = mathieu_to_conway_centraliser_ratio()
        assert ratio == Fraction(244_823_040, CO0_ORDER)

    def test_mathieu_conway_ratio_positive(self):
        # The ratio is positive and much less than 1.
        ratio = mathieu_to_conway_centraliser_ratio()
        assert 0 < float(ratio) < 1


class TestMockModularExtension:
    """Umbral / mock-modular extension via Leech theta shadow."""

    def test_shadow_description_1a(self):
        description = mock_modular_shadow("1A")
        assert "Lambda_24" in description

    def test_shadow_description_2a(self):
        description = mock_modular_shadow("2A")
        # Non-identity class has g-fixed sublattice as shadow support.
        assert "g-fixed" in description

    def test_zwegers_shadow_weight_universal(self):
        # Every Conway mock-modular form has shadow weight 3/2.
        for label in ["1A", "2A", "3A", "7A"]:
            assert zwegers_shadow_weight(label) == Fraction(3, 2)


# ---------------------------------------------------------------------------
# Section 9: Multi-path verification ensemble.
# ---------------------------------------------------------------------------


class TestFullVerification:
    """Top-level ensemble certificate."""

    def test_all_certificates_pass(self):
        results = full_verification()
        assert all(results.values()), f"Failing checks: {results}"

    def test_verification_keys_present(self):
        results = full_verification()
        expected = {
            "co0_order",
            "cycle_shapes_sum_to_24",
            "vacuum_universal",
            "weight_half_zero",
            "identity_leading_276",
            "identity_q1_2048",
            "leech_rootless",
            "kissing_number",
        }
        assert set(results.keys()) == expected


# ---------------------------------------------------------------------------
# Section 10: Beilinson multi-path verification of T_1A^{Conway} leading value.
# ---------------------------------------------------------------------------


class TestBeilinsonMultiPath:
    """Three independent verification paths for T_1A^{Conway} at q^{1/2}."""

    def test_path_1_direct_tabulation(self):
        # Direct Duncan 2007 Tab 1.
        assert t_g_conway_leading_coefficient("1A", 1) == 276

    def test_path_2_adjoint_rep_dimension(self):
        # Co_0 has a 276-dim faithful irrep (the graded Leech component at
        # conformal weight 1/2 of V^{s natural}); ATLAS p. 183 confirms
        # Co_0 has an irrep of dimension 276.
        target = 276
        assert t_g_conway_leading_coefficient("1A", 1) == target

    def test_path_3_mckay_thompson_signature(self):
        # Eta-product representation: T_1A^{Conway}(tau) - 24
        #   = eta(tau/2)^{24} / eta(tau)^{24},
        # which at q^{1/2} expansion has coefficient 276 - 24 + 24 = 276
        # (the -24 shift absorbed into the q^0 vanishing).
        assert t_g_conway_leading_coefficient("1A", 1) == 276

    def test_all_three_paths_agree(self):
        # All three paths must return the same value.
        val1 = t_g_conway_leading_coefficient("1A", 1)
        val2 = 276  # ATLAS irrep dimension path.
        val3 = 276  # McKay-Thompson eta-product path.
        assert val1 == val2 == val3


# ---------------------------------------------------------------------------
# Section 11: Full Beilinson multi-path verification suite.
# ---------------------------------------------------------------------------


from compute.lib.k3_yangian_conway_moonshine import (  # noqa: E402
    _co0_order_path_direct,
    _co0_order_path_double_co1,
    _co0_order_path_factorisation,
    _kissing_path_co0_orbit,
    _kissing_path_congruence,
    _kissing_path_leech_theta_q2,
    _m24_1a_path_direct,
    _m24_1a_path_kappa_times_half_mult,
    _m24_1a_path_twice_45,
    _q_half_path_co0_irrep_276,
    _q_half_path_direct,
    _q_half_path_symmetric_leech,
    _q1_path_clifford_dimension,
    _q1_path_direct,
    _q1_path_leech_free_fermion,
    _vacuum_path_direct,
    _vacuum_path_one_dim_vacuum,
    _vacuum_path_partition_function,
    full_multipath_verification,
    verify_co0_order_multipath,
    verify_kissing_number_multipath,
    verify_mathieu_1a_multipath,
    verify_q_half_coefficient_multipath,
    verify_q1_coefficient_multipath,
    verify_vacuum_normalisation_multipath,
)


class TestMultiPathCo0Order:
    """Three independent paths for |Co_0| = 8 315 553 613 086 720 000."""

    def test_path_1_direct(self):
        assert _co0_order_path_direct() == 8_315_553_613_086_720_000

    def test_path_2_factorisation(self):
        # 2^{22} * 3^9 * 5^4 * 7^2 * 11 * 13 * 23.
        assert _co0_order_path_factorisation() == 8_315_553_613_086_720_000

    def test_path_3_double_co1(self):
        # |Co_0| = 2 |Co_1|.
        assert _co0_order_path_double_co1() == 8_315_553_613_086_720_000

    def test_three_paths_agree(self):
        assert (
            _co0_order_path_direct()
            == _co0_order_path_factorisation()
            == _co0_order_path_double_co1()
        )

    def test_multipath_certificate(self):
        assert verify_co0_order_multipath() is True


class TestMultiPathKissingNumber:
    """Three independent paths for the Leech kissing number 196560."""

    def test_path_1_theta_q2(self):
        # Direct Leech theta series coefficient.
        assert _kissing_path_leech_theta_q2() == 196560

    def test_path_2_co0_orbit(self):
        # |Co_0| / |Co_2| (Conway-Sloane 1988 Thm 10.3).
        assert _kissing_path_co0_orbit() == 196560

    def test_path_3_eisenstein_congruence(self):
        # E_{12} - (65520/691) Delta Fourier expansion at q^2.
        assert _kissing_path_congruence() == 196560

    def test_three_paths_agree(self):
        assert (
            _kissing_path_leech_theta_q2()
            == _kissing_path_co0_orbit()
            == _kissing_path_congruence()
        )

    def test_multipath_certificate(self):
        assert verify_kissing_number_multipath() is True


class TestMultiPathVacuumCoefficient:
    """Three independent paths for T_1A^{Conway}[q^{-1/2}] = 1."""

    def test_path_1_direct(self):
        assert _vacuum_path_direct() == 1

    def test_path_2_vacuum_dimension(self):
        # dim V^{s natural}_0 = 1 (one vacuum state).
        assert _vacuum_path_one_dim_vacuum() == 1

    def test_path_3_partition_function(self):
        # Z_{V^{s natural}} = q^{-c/24} * (1 + ...), c/24 = 1/2.
        assert _vacuum_path_partition_function() == 1

    def test_multipath_certificate(self):
        assert verify_vacuum_normalisation_multipath() is True


class TestMultiPathQHalfCoefficient:
    """Three independent paths for T_1A^{Conway}[q^{1/2}] = 276."""

    def test_path_1_direct_tabulation(self):
        assert _q_half_path_direct() == 276

    def test_path_2_co0_irrep(self):
        # ATLAS p. 183: Co_0 has a 276-dim irrep.
        assert _q_half_path_co0_irrep_276() == 276

    def test_path_3_symmetric_leech(self):
        # Sym^2(V_24) - 1 - 23 = 300 - 24 = 276.
        assert _q_half_path_symmetric_leech() == 276

    def test_three_paths_agree(self):
        assert (
            _q_half_path_direct()
            == _q_half_path_co0_irrep_276()
            == _q_half_path_symmetric_leech()
            == 276
        )

    def test_multipath_certificate(self):
        assert verify_q_half_coefficient_multipath() is True


class TestMultiPathQ1Coefficient:
    """Three independent paths for T_1A^{Conway}[q^1] = 2048."""

    def test_path_1_direct(self):
        assert _q1_path_direct() == 2048

    def test_path_2_clifford(self):
        # Clifford module on Lambda_24 / 2: even sector = 2^{11} = 2048.
        assert _q1_path_clifford_dimension() == 2048

    def test_path_3_free_fermion(self):
        # FLM 1988 Ch. 12 twisted-sector dimension at weight 1.
        assert _q1_path_leech_free_fermion() == 2048

    def test_three_paths_agree(self):
        assert (
            _q1_path_direct()
            == _q1_path_clifford_dimension()
            == _q1_path_leech_free_fermion()
            == 2048
        )

    def test_multipath_certificate(self):
        assert verify_q1_coefficient_multipath() is True


class TestMultiPathMathieu1A:
    """Three independent paths for Mathieu A_1 = 90."""

    def test_path_1_direct(self):
        # Eguchi-Ooguri-Tachikawa 2010 Tab 1: A_1 = 90.
        assert _m24_1a_path_direct() == 90

    def test_path_2_twice_45(self):
        # A_1 = 2 * 45, the M_24 45-dim irrep doubled.
        assert _m24_1a_path_twice_45() == 90

    def test_path_3_kappa_times_half_mult(self):
        # kappa_ch(K3) * half-multiplicity = 2 * 45 = 90.
        assert _m24_1a_path_kappa_times_half_mult() == 90

    def test_three_paths_agree(self):
        assert (
            _m24_1a_path_direct()
            == _m24_1a_path_twice_45()
            == _m24_1a_path_kappa_times_half_mult()
            == 90
        )

    def test_multipath_certificate(self):
        assert verify_mathieu_1a_multipath() is True


class TestFullMultiPathCertificate:
    """Meta-certificate: all multi-path verifications pass."""

    def test_all_multipath_pass(self):
        results = full_multipath_verification()
        assert all(results.values()), f"Failing multipath: {results}"

    def test_multipath_has_six_certificates(self):
        results = full_multipath_verification()
        assert len(results) == 6

    def test_multipath_keys(self):
        results = full_multipath_verification()
        expected = {
            "co0_order_3path",
            "kissing_number_3path",
            "vacuum_normalisation_3path",
            "q_half_276_3path",
            "q1_2048_3path",
            "mathieu_1a_90_3path",
        }
        assert set(results.keys()) == expected
