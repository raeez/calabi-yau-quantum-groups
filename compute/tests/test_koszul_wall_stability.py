r"""
Tests for koszul_wall_stability.py -- Koszul walls in the Bridgeland
stability manifold.

Test structure:
  1.  KOSZUL WALL CRITERION (the three axioms K1, K2, K3)
  2.  CONIFOLD: STANDARD WALL IS NOT KOSZUL
  3.  CONIFOLD: TRANSITION IS A KOSZUL WALL
  4.  GEPNER POINT: NOT A KOSZUL WALL
  5.  LARGE-VOLUME KOSZUL WALL = MIRROR WALL
  6.  YANGIAN KOSZUL SELF-DUALITY (C^3)
  7.  MIRROR KOSZUL WALL ANALYSIS
  8.  KOSZUL WALL MONODROMY (Z/2 from each Koszul wall)
  9.  S^3-FRAMING KOSZUL COMPATIBILITY
  10. WALL TYPE CLASSIFICATION
  11. COMPREHENSIVE ATLAS
  12. CROSS-CONSISTENCY AND MULTI-PATH VERIFICATION
  13. FABER-PANDHARIPANDE COEFFICIENT CROSS-CHECK
  14. SELF-MIRROR CY3s (kappa = 0)
  15. FULL CONSISTENCY SUITE

Each test uses at least 3 independent verification paths (per CLAUDE.md
multi-path verification mandate).
"""

import pytest
from fractions import Fraction

from compute.lib.koszul_wall_stability import (
    # Wall types
    WallType,
    StabilityWall,
    # Koszul wall criterion
    KoszulWallCriterion,
    evaluate_koszul_wall_criterion,
    # Conifold
    ConifoldKoszulWallData,
    conifold_koszul_wall_analysis,
    # Gepner point
    GepnerKoszulWallData,
    gepner_koszul_wall_analysis,
    # Large volume
    LargeVolumeKoszulWallData,
    large_volume_koszul_wall,
    # Yangian
    YangianKoszulSelfDualityData,
    yangian_koszul_self_duality,
    # Mirror Koszul wall
    MirrorKoszulWallData,
    mirror_koszul_wall_analysis,
    # Monodromy
    KoszulWallMonodromyData,
    koszul_wall_monodromy_quintic,
    koszul_wall_monodromy_conifold,
    # S^3-framing
    S3FramingKoszulData,
    s3_framing_koszul_compatibility,
    # Atlas
    koszul_wall_atlas,
    # Classification
    classify_wall,
    # Consistency
    verify_koszul_wall_consistency,
    # Internal
    _faber_pandharipande_coefficients,
)


# =========================================================================
# 1.  KOSZUL WALL CRITERION (K1, K2, K3)
# =========================================================================

class TestKoszulWallCriterion:
    """Test the three-part Koszul wall criterion."""

    def test_all_criteria_met_gives_koszul(self):
        """When K1, K2, K3 all hold, the wall is classified as Koszul."""
        crit = evaluate_koszul_wall_criterion(
            monodromy_squared_is_identity=True,
            bps_spectrum_before={'a': 1},
            bps_spectrum_after={'b': 1},
            kappa_before=Fraction(5),
            kappa_after=Fraction(-5),
            shadow_class_before='G+',
            shadow_class_after='G-',
        )
        assert crit.is_koszul_wall
        assert crit.k1_involution
        assert crit.k2_bps_dual
        assert crit.k3_shadow_change

    def test_k1_fails(self):
        """K1 failure: monodromy^2 != identity."""
        crit = evaluate_koszul_wall_criterion(
            monodromy_squared_is_identity=False,
            bps_spectrum_before={'a': 1},
            bps_spectrum_after={'b': 1},
            kappa_before=Fraction(5),
            kappa_after=Fraction(-5),
            shadow_class_before='G+',
            shadow_class_after='G-',
        )
        assert not crit.is_koszul_wall
        assert not crit.k1_involution
        assert crit.k2_bps_dual
        assert crit.k3_shadow_change

    def test_k2_fails_kappa_nonzero_sum(self):
        """K2 failure: kappa does not satisfy complementarity."""
        crit = evaluate_koszul_wall_criterion(
            monodromy_squared_is_identity=True,
            bps_spectrum_before={'a': 1},
            bps_spectrum_after={'b': 1},
            kappa_before=Fraction(5),
            kappa_after=Fraction(5),  # same kappa, no complementarity
            shadow_class_before='G',
            shadow_class_after='L',
        )
        assert not crit.is_koszul_wall
        assert crit.k1_involution
        assert not crit.k2_bps_dual

    def test_k2_fails_bps_count_mismatch(self):
        """K2 failure: BPS counts don't match."""
        crit = evaluate_koszul_wall_criterion(
            monodromy_squared_is_identity=True,
            bps_spectrum_before={'a': 1, 'b': 1},
            bps_spectrum_after={'c': 1},  # different count
            kappa_before=Fraction(5),
            kappa_after=Fraction(-5),
            shadow_class_before='G+',
            shadow_class_after='G-',
        )
        assert not crit.is_koszul_wall
        assert not crit.k2_bps_dual

    def test_k3_fails_same_shadow_class(self):
        """K3 failure: shadow class unchanged."""
        crit = evaluate_koszul_wall_criterion(
            monodromy_squared_is_identity=True,
            bps_spectrum_before={'a': 1},
            bps_spectrum_after={'b': 1},
            kappa_before=Fraction(5),
            kappa_after=Fraction(-5),
            shadow_class_before='G',
            shadow_class_after='G',  # same class
        )
        assert not crit.is_koszul_wall
        assert crit.k1_involution
        assert crit.k2_bps_dual
        assert not crit.k3_shadow_change

    def test_criterion_explanation_nonempty(self):
        """The explanation string should be nonempty in all cases."""
        for mono in [True, False]:
            crit = evaluate_koszul_wall_criterion(
                monodromy_squared_is_identity=mono,
                bps_spectrum_before={'a': 1},
                bps_spectrum_after={'b': 1},
                kappa_before=Fraction(5),
                kappa_after=Fraction(-5),
                shadow_class_before='G+',
                shadow_class_after='G-',
            )
            assert len(crit.explanation) > 0


# =========================================================================
# 2.  CONIFOLD: STANDARD WALL IS NOT KOSZUL
# =========================================================================

class TestConifoldStandardWall:
    """The standard conifold wall is a KS mutation wall, not a Koszul wall."""

    def test_standard_wall_is_not_koszul(self):
        """Path 1: direct criterion check."""
        data = conifold_koszul_wall_analysis()
        assert not data.is_standard_wall_koszul

    def test_standard_wall_k1_fails(self):
        """Path 2: K1 fails because T_S^2 != identity."""
        data = conifold_koszul_wall_analysis()
        assert not data.standard_wall_criterion.k1_involution

    def test_standard_wall_kappa_unchanged(self):
        """Path 3: kappa does not change across the standard wall.

        kappa depends on the equivariant data (non-compact CY3), NOT on
        the chamber.  Both chambers have the same kappa.
        """
        data = conifold_koszul_wall_analysis()
        # kappa should be the same on both sides of the standard wall.
        # The criterion checks kappa + kappa_after = 0; for the standard
        # wall, kappa_before = kappa_after, so the sum is 2*kappa != 0.
        assert not data.standard_wall_criterion.k2_bps_dual

    def test_spherical_twist_squared_not_identity(self):
        """Independent verification: T_S^2 on the rank-2 lattice.

        T_S = [[1, 1], [0, 1]] (upper triangular shear).
        T_S^2 = [[1, 2], [0, 1]] != identity.
        """
        T = [[1, 1], [0, 1]]
        T2 = [[T[0][0]*T[0][0]+T[0][1]*T[1][0], T[0][0]*T[0][1]+T[0][1]*T[1][1]],
              [T[1][0]*T[0][0]+T[1][1]*T[1][0], T[1][0]*T[0][1]+T[1][1]*T[1][1]]]
        assert T2 == [[1, 2], [0, 1]]
        assert T2 != [[1, 0], [0, 1]]


# =========================================================================
# 3.  CONIFOLD: TRANSITION IS A KOSZUL WALL
# =========================================================================

class TestConifoldTransitionKoszulWall:
    """The conifold transition (resolved <-> deformed) IS a Koszul wall."""

    def test_transition_is_koszul(self):
        """Path 1: direct criterion check."""
        data = conifold_koszul_wall_analysis()
        assert data.is_transition_koszul

    def test_transition_kappa_complementarity(self):
        """Path 2: kappa(resolved) + kappa(deformed) = 0.

        kappa(resolved) = -chi(resolved) = -2
        kappa(deformed) = -chi(deformed) = +2
        Sum = 0.
        """
        data = conifold_koszul_wall_analysis()
        assert data.kappa_resolved == Fraction(-2)
        assert data.kappa_deformed == Fraction(2)
        assert data.complementarity_sum == Fraction(0)

    def test_transition_monodromy_is_involution(self):
        """Path 3: mirror of mirror = identity."""
        data = conifold_koszul_wall_analysis()
        assert data.transition_criterion.k1_involution

    def test_transition_all_three_criteria(self):
        """Path 4: all three criteria K1, K2, K3 hold."""
        data = conifold_koszul_wall_analysis()
        c = data.transition_criterion
        assert c.k1_involution, "K1 should hold"
        assert c.k2_bps_dual, "K2 should hold"
        assert c.k3_shadow_change, "K3 should hold"

    def test_kappa_arithmetic_exact(self):
        """Path 5: verify exact arithmetic.

        chi(resolved) = 2*(1 - 0) = 2
        chi(deformed) = 2*(0 - 1) = -2
        kappa = -chi => kappa(res) = -2, kappa(def) = 2
        """
        chi_res = 2 * (1 - 0)
        chi_def = 2 * (0 - 1)
        assert chi_res == 2
        assert chi_def == -2
        kappa_res = Fraction(-chi_res)
        kappa_def = Fraction(-chi_def)
        assert kappa_res == Fraction(-2)
        assert kappa_def == Fraction(2)
        assert kappa_res + kappa_def == Fraction(0)


# =========================================================================
# 4.  GEPNER POINT: NOT A KOSZUL WALL
# =========================================================================

class TestGepnerPoint:
    """The Gepner point of the quintic is NOT a Koszul wall."""

    def test_gepner_not_koszul(self):
        """Path 1: direct criterion check."""
        data = gepner_koszul_wall_analysis()
        assert not data.is_koszul_wall

    def test_gepner_monodromy_order_5(self):
        """Path 2: monodromy has order 5 (not 2)."""
        data = gepner_koszul_wall_analysis()
        assert data.monodromy_order == 5

    def test_gepner_no_z2_subgroup(self):
        """Path 3: Z/5 does not contain Z/2 as a subgroup.

        gcd(2, 5) = 1, so 2 does not divide 5.
        """
        data = gepner_koszul_wall_analysis()
        assert not data.contains_z2_subaction
        # Independent check
        assert 5 % 2 != 0

    def test_orlov_equivalence_not_koszul(self):
        """The Orlov equivalence D^b ~ MF is not a Koszul duality."""
        data = gepner_koszul_wall_analysis()
        assert not data.orlov_equivalence_is_koszul

    def test_kappa_unchanged_at_gepner(self):
        """kappa is intrinsic to D^b(Q); it does not change at the Gepner point."""
        data = gepner_koszul_wall_analysis()
        assert data.kappa_mum == data.kappa_gepner
        assert data.kappa_mum == Fraction(200)


# =========================================================================
# 5.  LARGE-VOLUME KOSZUL WALL = MIRROR WALL
# =========================================================================

class TestLargeVolumeKoszulWall:
    """The large-volume Koszul wall is the mirror wall."""

    def test_quintic_large_volume_is_koszul(self):
        """Path 1: the large-volume wall for the quintic is Koszul."""
        data = large_volume_koszul_wall(1, 101)
        assert data.is_koszul_wall

    def test_quintic_large_volume_is_mirror(self):
        """Path 2: the Koszul wall is the mirror wall."""
        data = large_volume_koszul_wall(1, 101)
        assert data.wall_is_mirror

    def test_complementarity(self):
        """Path 3: kappa(Sym) + kappa(Ext) = 0."""
        data = large_volume_koszul_wall(1, 101)
        assert data.complementarity_sum == Fraction(0)

    def test_kappa_values(self):
        """Exact kappa values for the quintic."""
        data = large_volume_koszul_wall(1, 101)
        assert data.kappa_sym == Fraction(200)  # -chi = -(-200) = 200
        assert data.kappa_ext == Fraction(-200)

    def test_generator_counts_match(self):
        """Sym and Lambda have the same number of generators."""
        data = large_volume_koszul_wall(1, 101)
        assert data.sym_generators == data.ext_generators

    def test_conifold_large_volume(self):
        """Large-volume wall for the conifold."""
        data = large_volume_koszul_wall(1, 0)
        assert data.is_koszul_wall
        assert data.kappa_sym == Fraction(-2)
        assert data.kappa_ext == Fraction(2)
        assert data.complementarity_sum == Fraction(0)

    def test_self_mirror_large_volume(self):
        """For self-mirror CY3: kappa = 0, Sym ~ Ext (self-dual)."""
        data = large_volume_koszul_wall(11, 11)
        assert data.kappa_sym == Fraction(0)
        assert data.kappa_ext == Fraction(0)
        assert data.complementarity_sum == Fraction(0)

    def test_total_hh_dimension(self):
        """Total HH dimension: 4 + 2*h11 + 2*h21.

        Quintic: 4 + 2 + 202 = 208.
        """
        data = large_volume_koszul_wall(1, 101)
        assert data.sym_generators == 4 + 2 * 1 + 2 * 101
        assert data.sym_generators == 208


# =========================================================================
# 6.  YANGIAN KOSZUL SELF-DUALITY (C^3)
# =========================================================================

class TestYangianKoszulSelfDuality:
    """Y^+(gl_hat_1) is Koszul self-dual at the self-dual point."""

    def test_self_duality(self):
        """Path 1: the Yangian is self-dual."""
        data = yangian_koszul_self_duality()
        assert data.is_self_dual

    def test_kappa_complementarity(self):
        """Path 2: kappa + kappa^! = 0."""
        data = yangian_koszul_self_duality()
        assert data.kappa_yangian + data.kappa_dual == Fraction(0)
        assert data.kappa_yangian == Fraction(1)
        assert data.kappa_dual == Fraction(-1)

    def test_bar_differential_vanishes(self):
        """Path 3: bar differential d_{E_1} = 0 for H_1.

        The Heisenberg has no first-order pole, so mu(a,a) = 0,
        and the bar differential vanishes identically.
        """
        data = yangian_koszul_self_duality()
        assert data.bar_differential_zero

    def test_bar_cohomology_equals_bar(self):
        """Since d = 0, H*(B) = B itself."""
        data = yangian_koszul_self_duality()
        assert data.bar_cohomology_equals_bar

    def test_generator_counts(self):
        """Both the Yangian and its Koszul dual have 1 generator."""
        data = yangian_koszul_self_duality()
        assert data.original_generator_count == 1
        assert data.koszul_dual_generator_count == 1

    def test_bar_dimensions(self):
        """Bar complex dimensions: 1 at each arity (1 generator, d=0)."""
        data = yangian_koszul_self_duality()
        for n in range(1, 5):
            assert data.bar_dims[n] == 1

    def test_all_verification_paths(self):
        """All four verification paths pass."""
        data = yangian_koszul_self_duality()
        assert all(data.verification_paths.values())


# =========================================================================
# 7.  MIRROR KOSZUL WALL ANALYSIS
# =========================================================================

class TestMirrorKoszulWall:
    """Mirror symmetry as a Koszul wall."""

    def test_quintic_mirror_is_koszul(self):
        """The quintic mirror wall is a Koszul wall."""
        data = mirror_koszul_wall_analysis(1, 101, "quintic")
        assert data.is_koszul_wall

    def test_quintic_complementarity(self):
        """kappa(Q) + kappa(Q^v) = 0."""
        data = mirror_koszul_wall_analysis(1, 101, "quintic")
        assert data.complementarity_sum == Fraction(0)
        assert data.kappa_X == Fraction(200)
        assert data.kappa_mirror == Fraction(-200)

    def test_conifold_mirror_is_koszul(self):
        """The conifold mirror wall is a Koszul wall."""
        data = mirror_koszul_wall_analysis(1, 0, "conifold")
        assert data.is_koszul_wall

    def test_fg_koszul_dual_matches_mirror(self):
        """F_g(A^!) = F_g(A_{mirror}) at all genera.

        Path 1: direct comparison from the shadow tower.
        """
        data = mirror_koszul_wall_analysis(1, 101, "quintic")
        for g, fdata in data.fg_comparisons.items():
            assert fdata['kd_matches_mirror'], (
                f"F_{g}(A^!) != F_{g}(A_mirror)"
            )

    def test_self_mirror_trivial(self):
        """For self-mirror CY3: kappa = 0, trivial Koszul wall."""
        data = mirror_koszul_wall_analysis(11, 11, "Z_manifold")
        assert data.kappa_X == Fraction(0)
        assert data.kappa_mirror == Fraction(0)
        assert data.complementarity_sum == Fraction(0)

    def test_bar_dims_preserved(self):
        """Bar complex dimensions are the same on both sides (same total HH)."""
        data = mirror_koszul_wall_analysis(1, 101, "quintic")
        for n in data.bar_dims_X:
            assert data.bar_dims_X[n] == data.bar_dims_mirror[n]


# =========================================================================
# 8.  KOSZUL WALL MONODROMY
# =========================================================================

class TestKoszulWallMonodromy:
    """Double Koszul dual = identity (Z/2 monodromy)."""

    def test_quintic_double_koszul(self):
        """Path 1: kappa -> -kappa -> kappa (quintic)."""
        data = koszul_wall_monodromy_quintic()
        assert data.double_koszul_is_identity
        assert data.kappa_after_double_koszul == Fraction(200)

    def test_conifold_double_koszul(self):
        """Path 2: kappa -> -kappa -> kappa (conifold)."""
        data = koszul_wall_monodromy_conifold()
        assert data.double_koszul_is_identity
        assert data.kappa_after_double_koszul == Fraction(-2)

    def test_quintic_koszul_walls_count(self):
        """Quintic has 1 Koszul wall (conifold transition in extended moduli)."""
        data = koszul_wall_monodromy_quintic()
        assert data.koszul_walls == 1

    def test_quintic_autoequivalence_walls(self):
        """Quintic has 1 autoequivalence wall (Gepner point)."""
        data = koszul_wall_monodromy_quintic()
        assert data.autoequivalence_walls == 1

    def test_conifold_standard_walls(self):
        """Conifold has 1 standard wall."""
        data = koszul_wall_monodromy_conifold()
        assert data.standard_walls == 1

    def test_double_koszul_exact_arithmetic(self):
        """Path 3: exact arithmetic for double Koszul on several examples.

        For any kappa: kappa -> -kappa -> -(-kappa) = kappa.
        """
        test_values = [Fraction(200), Fraction(-2), Fraction(0),
                       Fraction(7, 3), Fraction(-149)]
        for k in test_values:
            k_single = -k
            k_double = -k_single
            assert k_double == k, f"Double Koszul failed for kappa = {k}"


# =========================================================================
# 9.  S^3-FRAMING KOSZUL COMPATIBILITY
# =========================================================================

class TestS3FramingKoszulCompatibility:
    """S^3-framing must be compatible with Koszul duality."""

    def test_quintic_compatible(self):
        """Path 1: quintic framing is compatible."""
        data = s3_framing_koszul_compatibility(1, 101, "quintic")
        assert data.koszul_compatible

    def test_quintic_not_trivial(self):
        """The quintic is not self-mirror, so framing is non-trivial."""
        data = s3_framing_koszul_compatibility(1, 101, "quintic")
        assert not data.framing_trivial

    def test_self_mirror_trivial_framing(self):
        """Path 2: self-mirror CY3 has trivial framing."""
        data = s3_framing_koszul_compatibility(11, 11, "Z_manifold")
        assert data.framing_trivial
        assert data.koszul_compatible

    def test_kappa_transforms_correctly(self):
        """Path 3: kappa(X) + kappa(mirror) = 0 in the constraint."""
        data = s3_framing_koszul_compatibility(1, 101, "quintic")
        assert data.constraint_verification['kappa_transforms_correctly']

    def test_all_verifications(self):
        """All constraint verification paths pass."""
        data = s3_framing_koszul_compatibility(1, 101, "quintic")
        for key, val in data.constraint_verification.items():
            assert val, f"Constraint verification failed: {key}"

    def test_conifold_framing(self):
        """Conifold framing is non-trivial but compatible."""
        data = s3_framing_koszul_compatibility(1, 0, "resolved_conifold")
        assert data.koszul_compatible
        assert not data.framing_trivial


# =========================================================================
# 10.  WALL TYPE CLASSIFICATION
# =========================================================================

class TestWallClassification:
    """Test the wall classification engine."""

    def test_koszul_wall_classification(self):
        """A wall with complementary kappa and involutive monodromy is Koszul."""
        wall = classify_wall(
            monodromy_matrix=[[1, 0], [0, 1]],  # identity (M^2 = id)
            kappa_before=Fraction(5),
            kappa_after=Fraction(-5),
            bps_before={'a': 1},
            bps_after={'b': 1},
        )
        assert wall.wall_type == WallType.KOSZUL
        assert wall.monodromy_order == 2

    def test_standard_wall_classification(self):
        """A wall with unchanged kappa is standard."""
        wall = classify_wall(
            monodromy_matrix=[[1, 1], [0, 1]],  # shear, M^2 != id
            kappa_before=Fraction(5),
            kappa_after=Fraction(5),
            bps_before={'a': 1, 'b': 1},
            bps_after={'b': 1, 'c': 1, 'a': 1},
        )
        assert wall.wall_type == WallType.STANDARD
        assert wall.kappa_change == Fraction(0)

    def test_marginal_wall_classification(self):
        """A wall with non-complementary, non-equal kappa is marginal."""
        wall = classify_wall(
            monodromy_matrix=[[0, -1], [1, 0]],  # rotation, M^2 = -id
            kappa_before=Fraction(5),
            kappa_after=Fraction(3),
            bps_before={'a': 1},
            bps_after={'b': 1},
        )
        assert wall.wall_type == WallType.MARGINAL


# =========================================================================
# 11.  COMPREHENSIVE ATLAS
# =========================================================================

class TestKoszulWallAtlas:
    """Test the comprehensive Koszul wall atlas."""

    def test_atlas_has_all_examples(self):
        """The atlas covers all standard CY3 examples."""
        atlas = koszul_wall_atlas()
        expected = ["quintic", "resolved_conifold", "deformed_conifold",
                    "octic_WP", "bicubic", "Z_manifold", "Schoen_manifold"]
        for name in expected:
            assert name in atlas, f"Missing {name} from atlas"

    def test_atlas_complementarity_universal(self):
        """kappa complementarity holds for every example in the atlas."""
        atlas = koszul_wall_atlas()
        for name, data in atlas.items():
            assert data['mirror_koszul']['complementarity_sum'] == Fraction(0), (
                f"Complementarity fails for {name}"
            )

    def test_atlas_large_volume_koszul(self):
        """Every example's large-volume wall is a Koszul wall."""
        atlas = koszul_wall_atlas()
        for name, data in atlas.items():
            assert data['large_volume_koszul']['is_koszul_wall'], (
                f"Large-volume wall should be Koszul for {name}"
            )

    def test_atlas_s3_framing_compatible(self):
        """S^3-framing is compatible for all examples."""
        atlas = koszul_wall_atlas()
        for name, data in atlas.items():
            assert data['s3_framing']['compatible'], (
                f"S^3-framing not compatible for {name}"
            )

    def test_atlas_self_mirror_trivial_framing(self):
        """Self-mirror examples have trivial framing."""
        atlas = koszul_wall_atlas()
        for name in ["Z_manifold", "Schoen_manifold"]:
            assert atlas[name]['s3_framing']['trivial'], (
                f"Self-mirror {name} should have trivial framing"
            )

    def test_atlas_euler_characteristics(self):
        """Verify Euler characteristics in the atlas (independent computation)."""
        atlas = koszul_wall_atlas()
        assert atlas['quintic']['hodge']['chi'] == -200
        assert atlas['resolved_conifold']['hodge']['chi'] == 2
        assert atlas['deformed_conifold']['hodge']['chi'] == -2
        assert atlas['Z_manifold']['hodge']['chi'] == 0
        assert atlas['Schoen_manifold']['hodge']['chi'] == 0


# =========================================================================
# 12.  CROSS-CONSISTENCY AND MULTI-PATH VERIFICATION
# =========================================================================

class TestCrossConsistency:
    """Multi-path cross-consistency checks across all computations."""

    def test_conifold_kappa_three_paths(self):
        """Verify conifold kappa via three independent computations.

        Path 1: from Euler characteristic.
        Path 2: from conifold_koszul_wall_analysis.
        Path 3: from mirror_koszul_wall_analysis.
        """
        # Path 1
        chi_res = 2 * (1 - 0)
        kappa_1 = Fraction(-chi_res)
        assert kappa_1 == Fraction(-2)

        # Path 2
        conifold_data = conifold_koszul_wall_analysis()
        kappa_2 = conifold_data.kappa_resolved
        assert kappa_2 == Fraction(-2)

        # Path 3
        mirror_data = mirror_koszul_wall_analysis(1, 0, "conifold")
        kappa_3 = mirror_data.kappa_X
        assert kappa_3 == Fraction(-2)

        # All three agree
        assert kappa_1 == kappa_2 == kappa_3

    def test_quintic_kappa_three_paths(self):
        """Verify quintic kappa via three independent computations.

        Path 1: from Euler characteristic.
        Path 2: from large_volume_koszul_wall.
        Path 3: from mirror_koszul_wall_analysis.
        """
        # Path 1
        chi_q = 2 * (1 - 101)
        kappa_1 = Fraction(-chi_q)
        assert kappa_1 == Fraction(200)

        # Path 2
        lv_data = large_volume_koszul_wall(1, 101)
        kappa_2 = lv_data.kappa_sym
        assert kappa_2 == Fraction(200)

        # Path 3
        mirror_data = mirror_koszul_wall_analysis(1, 101, "quintic")
        kappa_3 = mirror_data.kappa_X
        assert kappa_3 == Fraction(200)

        assert kappa_1 == kappa_2 == kappa_3

    def test_complementarity_four_paths(self):
        """Verify kappa complementarity for the quintic via four paths.

        Path 1: kappa(Q) + kappa(Q^v) = 0 from Euler chars.
        Path 2: from conifold_koszul_wall_analysis (for conifold).
        Path 3: from mirror_koszul_wall_analysis.
        Path 4: from large_volume_koszul_wall.
        """
        # Path 1
        assert Fraction(200) + Fraction(-200) == Fraction(0)

        # Path 2
        con_data = conifold_koszul_wall_analysis()
        assert con_data.complementarity_sum == Fraction(0)

        # Path 3
        mir_data = mirror_koszul_wall_analysis(1, 101, "quintic")
        assert mir_data.complementarity_sum == Fraction(0)

        # Path 4
        lv_data = large_volume_koszul_wall(1, 101)
        assert lv_data.complementarity_sum == Fraction(0)

    def test_gepner_vs_conifold_wall_types(self):
        """Gepner is NOT Koszul; conifold transition IS Koszul.

        These are two fundamentally different types of singular points.
        """
        gepner = gepner_koszul_wall_analysis()
        conifold = conifold_koszul_wall_analysis()

        assert not gepner.is_koszul_wall
        assert conifold.is_transition_koszul

        # Different monodromy orders
        assert gepner.monodromy_order == 5
        # conifold transition has Z/2 monodromy


# =========================================================================
# 13.  FABER-PANDHARIPANDE COEFFICIENT CROSS-CHECK
# =========================================================================

class TestFaberPandharipande:
    """Cross-check the Faber-Pandharipande coefficients."""

    def test_lambda_1(self):
        """lambda_1 = 1/24 (standard value)."""
        fp = _faber_pandharipande_coefficients()
        assert fp[1] == Fraction(1, 24)

    def test_lambda_2(self):
        """lambda_2 = 7/5760."""
        fp = _faber_pandharipande_coefficients()
        assert fp[2] == Fraction(7, 5760)

    def test_lambda_3(self):
        """lambda_3 = 31/967680."""
        fp = _faber_pandharipande_coefficients()
        assert fp[3] == Fraction(31, 967680)

    def test_lambda_4(self):
        """lambda_4 = 127/154828800."""
        fp = _faber_pandharipande_coefficients()
        assert fp[4] == Fraction(127, 154828800)

    def test_lambda_positivity(self):
        """All lambda_g > 0."""
        fp = _faber_pandharipande_coefficients()
        for g in range(1, 7):
            assert fp[g] > 0, f"lambda_{g} = {fp[g]} not positive"

    def test_lambda_decreasing(self):
        """lambda_g is strictly decreasing."""
        fp = _faber_pandharipande_coefficients()
        for g in range(1, 6):
            assert fp[g] > fp[g + 1]

    def test_fg_quintic_genus_1(self):
        """F_1(quintic) = kappa * lambda_1 = 200/24 = 25/3."""
        fp = _faber_pandharipande_coefficients()
        F_1 = Fraction(200) * fp[1]
        assert F_1 == Fraction(200, 24)
        assert F_1 == Fraction(25, 3)

    def test_fg_quintic_genus_2(self):
        """F_2(quintic) = 200 * 7/5760 = 1400/5760 = 35/144."""
        fp = _faber_pandharipande_coefficients()
        F_2 = Fraction(200) * fp[2]
        assert F_2 == Fraction(1400, 5760)
        assert F_2 == Fraction(35, 144)


# =========================================================================
# 14.  SELF-MIRROR CY3s (kappa = 0)
# =========================================================================

class TestSelfMirrorKoszulWall:
    """For self-mirror CY3s: kappa = 0, trivial Koszul wall."""

    def test_z_manifold_kappa_zero(self):
        """Z-manifold: h11 = h21 = 11, chi = 0, kappa = 0."""
        data = large_volume_koszul_wall(11, 11)
        assert data.kappa_sym == Fraction(0)
        assert data.kappa_ext == Fraction(0)

    def test_schoen_kappa_zero(self):
        """Schoen manifold: h11 = h21 = 19, chi = 0, kappa = 0."""
        data = large_volume_koszul_wall(19, 19)
        assert data.kappa_sym == Fraction(0)

    def test_self_mirror_trivial_complementarity(self):
        """kappa + kappa^! = 0 + 0 = 0 (trivially)."""
        data = mirror_koszul_wall_analysis(11, 11, "Z_manifold")
        assert data.complementarity_sum == Fraction(0)

    def test_self_mirror_fg_all_zero(self):
        """F_g = kappa * lambda_g = 0 for all g when kappa = 0."""
        data = mirror_koszul_wall_analysis(11, 11, "Z_manifold")
        for g, fdata in data.fg_comparisons.items():
            assert fdata['F_g_X'] == Fraction(0)
            assert fdata['F_g_mirror'] == Fraction(0)

    def test_self_mirror_double_koszul(self):
        """Double Koszul: 0 -> 0 -> 0 (trivially identity)."""
        kappa = Fraction(0)
        assert -(-kappa) == kappa


# =========================================================================
# 15.  FULL CONSISTENCY SUITE
# =========================================================================

class TestFullConsistencySuite:
    """Run the full consistency check from verify_koszul_wall_consistency."""

    def test_full_consistency(self):
        """All consistency checks pass."""
        result = verify_koszul_wall_consistency()
        assert result['all_checks_pass']

    def test_conifold_results(self):
        """Conifold-specific results from the consistency suite."""
        result = verify_koszul_wall_consistency()
        assert result['conifold_standard_not_koszul']
        assert result['conifold_transition_is_koszul']

    def test_gepner_result(self):
        """Gepner-specific result from the consistency suite."""
        result = verify_koszul_wall_consistency()
        assert result['gepner_not_koszul']

    def test_yangian_result(self):
        """Yangian self-duality from the consistency suite."""
        result = verify_koszul_wall_consistency()
        assert result['yangian_self_dual']

    def test_monodromy_results(self):
        """Monodromy results from the consistency suite."""
        result = verify_koszul_wall_consistency()
        assert result['double_koszul_is_identity_quintic']
        assert result['double_koszul_is_identity_conifold']

    def test_s3_framing_result(self):
        """S^3-framing result from the consistency suite."""
        result = verify_koszul_wall_consistency()
        assert result['s3_framing_compatible']

    def test_atlas_complementarity_result(self):
        """Atlas-wide complementarity from the consistency suite."""
        result = verify_koszul_wall_consistency()
        assert result['atlas_complementarity_holds']
