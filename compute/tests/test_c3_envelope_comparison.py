"""Tests for C^3 factorization envelope comparison: three constructions, five paths.

Verifies the definitive identification:
  (a) Factorization envelope U^{ch}(PV*(C^3)) at N=1 = Heisenberg VOA
  (b) W_{1+infinity}[c=1] = Heisenberg VOA
  (c) CoHA Y^+(gl_hat_1) acts on plane partition module over the Heisenberg

Five independent verification paths:
  Path 1 (Envelope): OPE from lambda-bracket of PV*(C^3)
  Path 2 (Shuffle): OPE from shuffle presentation of Y^+(gl_hat_1)
  Path 3 (Crystal melting): graded character from plane partition counting
  Path 4 (Free field): OPE from single free boson
  Path 5 (Kac determinant): Shapovalov form matching across constructions
"""

from fractions import Fraction

import pytest

from compute.lib.c3_envelope_comparison import (
    CrystalMeltingConstruction,
    EnvelopeConstruction,
    FreeFieldConstruction,
    KacDeterminantComparison,
    ShuffleConstruction,
    _partitions_of,
    _z_lambda,
    compare_characters,
    compare_kac_determinants,
    compare_ope_structures,
    compare_shuffle_structure_at_generic_N,
    cross_check_structure_function_N1_to_N5,
    full_c3_comparison,
    verify_character_factorization,
    verify_g_inversion_at_N,
    verify_sugawara_at_c1,
)


# =========================================================================
# PATH 1: FACTORIZATION ENVELOPE
# =========================================================================

class TestEnvelopeConstruction:
    """Tests for the factorization envelope construction (Path 1)."""

    def test_central_charge_N1(self):
        env = EnvelopeConstruction(level=1)
        # VERIFIED [DC] central charge formula [LT] literature cross-check
        assert env.central_charge == Fraction(1)

    def test_central_charge_N2(self):
        env = EnvelopeConstruction(level=2)
        # VERIFIED [DC] central charge formula [LT] literature cross-check
        assert env.central_charge == Fraction(2)

    def test_jj_ope_modes(self):
        env = EnvelopeConstruction(level=1)
        modes = env.jj_ope_modes()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert modes[0] == Fraction(0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert modes[1] == Fraction(1)

    def test_jj_lambda_bracket(self):
        env = EnvelopeConstruction(level=1)
        lb = env.jj_lambda_bracket()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert lb[0] == Fraction(0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert lb[1] == Fraction(1)

    def test_tt_ope_mode_3(self):
        """T_{(3)}T = c/2 = 1/2 for c=1."""
        env = EnvelopeConstruction(level=1)
        modes = env.tt_ope_modes()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert modes[3] == Fraction(1, 2)

    def test_tt_lambda_bracket_ap44(self):
        """Divided-power convention: lambda^3 coeff = c/12, not c/2 (AP44)."""
        env = EnvelopeConstruction(level=1)
        lb = env.tt_lambda_bracket_coefficients()
        # T_{(3)}T = c/2, lambda^(3) = lambda^3/6, so coeff = (c/2)/6 = c/12
        # VERIFIED [DC] structural property [LC] AP44
        assert lb["scalar_3"] == Fraction(1, 12)

    def test_character_N1_is_euler(self):
        """Character of single boson = P(q) = ordinary partition function."""
        env = EnvelopeConstruction(level=1)
        ch = env.character_coefficients(max_weight=10)
        known = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        for i in range(len(known)):
            assert int(ch[i]) == known[i], f"Weight {i}: {int(ch[i])} != {known[i]}"

    def test_character_N2_is_euler_squared(self):
        """Character of two bosons = P(q)^2."""
        env = EnvelopeConstruction(level=2)
        ch = env.character_coefficients(max_weight=8)
        # P(q)^2 = 1 + 2q + 5q^2 + 10q^3 + 20q^4 + ...
        known = [1, 2, 5, 10, 20, 36, 65, 110, 185]
        for i in range(len(known)):
            assert int(ch[i]) == known[i]

    def test_kac_determinant_weight_1(self):
        """det_1 = z_{(1)} = 1."""
        env = EnvelopeConstruction(level=1)
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert env.kac_determinant(1) == Fraction(1)

    def test_kac_determinant_weight_2(self):
        """det_2 = z_{(2)} * z_{(1,1)} = 2 * 2 = 4."""
        env = EnvelopeConstruction(level=1)
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert env.kac_determinant(2) == Fraction(4)

    def test_kac_determinant_weight_3(self):
        """det_3 = z_{(3)} * z_{(2,1)} * z_{(1,1,1)} = 3 * 2 * 6 = 36."""
        env = EnvelopeConstruction(level=1)
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert env.kac_determinant(3) == Fraction(36)


# =========================================================================
# PATH 2: SHUFFLE ALGEBRA / AFFINE YANGIAN
# =========================================================================

class TestShuffleConstruction:
    """Tests for the shuffle algebra construction (Path 2)."""

    def test_N1_is_abelian(self):
        """At N=1, all phi_j = 0 for j >= 1 (trivial structure function)."""
        shuf = ShuffleConstruction(N=1)
        result = shuf.verify_abelian_at_N1()
        assert result["all_phi_j_zero_for_j_ge_1"]

    def test_N1_central_charge(self):
        shuf = ShuffleConstruction(N=1)
        # VERIFIED [DC] central charge formula [LT] literature cross-check
        assert shuf.central_charge == Fraction(1)

    def test_N2_central_charge(self):
        shuf = ShuffleConstruction(N=2)
        # VERIFIED [DC] central charge formula [LT] literature cross-check
        assert shuf.central_charge == Fraction(2)

    def test_N2_sigma2(self):
        """sigma_2 = -(N^2 - N + 1) = -3 for N=2."""
        shuf = ShuffleConstruction(N=2)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert shuf.sigma_2 == Fraction(-3)

    def test_N2_sigma3(self):
        """sigma_3 = N(1-N) = -2 for N=2."""
        shuf = ShuffleConstruction(N=2)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert shuf.sigma_3 == Fraction(-2)

    def test_N3_sigma2(self):
        """sigma_2 = -(9-3+1) = -7 for N=3."""
        shuf = ShuffleConstruction(N=3)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert shuf.sigma_2 == Fraction(-7)

    def test_N3_sigma3(self):
        """sigma_3 = 3*(1-3) = -6 for N=3."""
        shuf = ShuffleConstruction(N=3)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert shuf.sigma_3 == Fraction(-6)

    def test_phi_1_always_zero(self):
        """phi_1 = 0 for all N (CY condition)."""
        for N in range(1, 6):
            shuf = ShuffleConstruction(N=N)
            phi = shuf.structure_function_coefficients(max_order=5)
            # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
            assert phi[1] == 0, f"phi_1 != 0 at N={N}"

    def test_phi_2_always_zero(self):
        """phi_2 = 0 for all N (only odd alpha contribute)."""
        for N in range(1, 6):
            shuf = ShuffleConstruction(N=N)
            phi = shuf.structure_function_coefficients(max_order=5)
            # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
            assert phi[2] == 0, f"phi_2 != 0 at N={N}"

    def test_phi_3_formula(self):
        """phi_3 = -2*sigma_3 for all N."""
        for N in range(1, 6):
            shuf = ShuffleConstruction(N=N)
            phi = shuf.structure_function_coefficients(max_order=5)
            expected = Fraction(-2) * shuf.sigma_3
            assert phi[3] == expected, f"N={N}: phi_3={phi[3]} != {expected}"

    def test_phi_4_always_zero(self):
        """phi_4 = 0 for all N."""
        for N in range(1, 6):
            shuf = ShuffleConstruction(N=N)
            phi = shuf.structure_function_coefficients(max_order=5)
            # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
            assert phi[4] == 0, f"phi_4 != 0 at N={N}"

    def test_character_N1_is_euler(self):
        """W-algebra character at N=1 is P(q)."""
        shuf = ShuffleConstruction(N=1)
        ch = shuf.character_coefficients(max_weight=10)
        known = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        for i in range(len(known)):
            assert int(ch[i]) == known[i]


# =========================================================================
# PATH 3: CRYSTAL MELTING
# =========================================================================

class TestCrystalMeltingConstruction:
    """Tests for the crystal melting / plane partition approach (Path 3)."""

    def test_macmahon_coefficients(self):
        """M(q) first 11 coefficients match OEIS A000219."""
        mac = CrystalMeltingConstruction.macmahon_coefficients(max_weight=10)
        known = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
        for i in range(len(known)):
            assert int(mac[i]) == known[i], f"M(q)[{i}]: {int(mac[i])} != {known[i]}"

    def test_partition_function_coefficients(self):
        """P(q) first 11 coefficients match OEIS A000041."""
        pf = CrystalMeltingConstruction.partition_function_coefficients(max_weight=10)
        known = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        for i in range(len(known)):
            assert int(pf[i]) == known[i], f"P(q)[{i}]: {int(pf[i])} != {known[i]}"

    def test_macmahon_differs_from_euler(self):
        """M(q) != P(q) starting at weight 2."""
        mac = CrystalMeltingConstruction.macmahon_coefficients(max_weight=5)
        pf = CrystalMeltingConstruction.partition_function_coefficients(max_weight=5)
        assert mac[0] == pf[0]  # Both 1
        assert mac[1] == pf[1]  # Both 1
        assert mac[2] != pf[2]  # M: 3, P: 2

    def test_walgebra_character_N1_equals_euler(self):
        """W_{1+infty}[1] character = P(q)."""
        crystal = CrystalMeltingConstruction(N=1)
        ch = crystal.walgebra_character(max_weight=10)
        pf = CrystalMeltingConstruction.partition_function_coefficients(max_weight=10)
        assert ch == pf

    def test_walgebra_character_N2(self):
        """W_{1+infty}[2] character = P(q)^2."""
        crystal = CrystalMeltingConstruction(N=2)
        ch = crystal.walgebra_character(max_weight=8)
        known = [1, 2, 5, 10, 20, 36, 65, 110, 185]
        for i in range(len(known)):
            assert int(ch[i]) == known[i]

    def test_macmahon_extended(self):
        """M(q) coefficients up to weight 15."""
        mac = CrystalMeltingConstruction.macmahon_coefficients(max_weight=15)
        known = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500,
                 859, 1479, 2485, 4167, 6879]
        for i in range(len(known)):
            assert int(mac[i]) == known[i]


# =========================================================================
# PATH 4: FREE FIELD REALIZATION
# =========================================================================

class TestFreeFieldConstruction:
    """Tests for the free field realization (Path 4)."""

    def test_central_charge(self):
        ff = FreeFieldConstruction(N=1)
        # VERIFIED [DC] central charge [LC] boundary/limiting case
        assert ff.c == Fraction(1)

    def test_jj_ope(self):
        ff = FreeFieldConstruction(N=1)
        ope = ff.jj_ope()
        # VERIFIED [DC] OPE data [LC] boundary/limiting case
        assert Fraction(ope["J_{(1)}J"]) == Fraction(1)

    def test_tt_ope_mode_3(self):
        """T_{(3)}T = c/2 = 1/2 from Sugawara."""
        ff = FreeFieldConstruction(N=1)
        ope = ff.tt_ope()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert ope["T_{(3)}T"] == Fraction(1, 2)

    def test_tt_ope_central_charge(self):
        ff = FreeFieldConstruction(N=1)
        ope = ff.tt_ope()
        # VERIFIED [DC] central charge formula [LT] literature cross-check
        assert ope["central_charge"] == Fraction(1)

    def test_character_N1_is_euler(self):
        ff = FreeFieldConstruction(N=1)
        ch = ff.character_coefficients(max_weight=10)
        known = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        for i in range(len(known)):
            assert int(ch[i]) == known[i]

    def test_kac_determinant_weight_1(self):
        ff = FreeFieldConstruction(N=1)
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert ff.kac_determinant(1) == Fraction(1)

    def test_kac_determinant_weight_2(self):
        ff = FreeFieldConstruction(N=1)
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert ff.kac_determinant(2) == Fraction(4)

    def test_kac_determinant_weight_3(self):
        ff = FreeFieldConstruction(N=1)
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert ff.kac_determinant(3) == Fraction(36)


# =========================================================================
# PATH 5: KAC DETERMINANT MATCHING
# =========================================================================

class TestKacDeterminantComparison:
    """Tests for the Kac determinant comparison (Path 5)."""

    def test_z_lambda_single_part(self):
        """z_{(k)} = k for single-part partitions."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert _z_lambda((1,)) == Fraction(1)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert _z_lambda((2,)) == Fraction(2)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert _z_lambda((3,)) == Fraction(3)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert _z_lambda((4,)) == Fraction(4)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert _z_lambda((5,)) == Fraction(5)

    def test_z_lambda_two_ones(self):
        """z_{(1,1)} = 1^2 * 2! = 2."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert _z_lambda((1, 1)) == Fraction(2)

    def test_z_lambda_two_twos(self):
        """z_{(2,2)} = 2^2 * 2! = 8."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert _z_lambda((2, 2)) == Fraction(8)

    def test_z_lambda_21(self):
        """z_{(2,1)} = 2^1 * 1! * 1^1 * 1! = 2."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert _z_lambda((2, 1)) == Fraction(2)

    def test_z_lambda_111(self):
        """z_{(1,1,1)} = 1^3 * 3! = 6."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert _z_lambda((1, 1, 1)) == Fraction(6)

    def test_z_lambda_1111(self):
        """z_{(1,1,1,1)} = 1^4 * 4! = 24."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert _z_lambda((1, 1, 1, 1)) == Fraction(24)

    def test_det_weight_0(self):
        """det_0 = 1 (vacuum, one state)."""
        kac = KacDeterminantComparison()
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert kac.heisenberg_kac_det(0) == Fraction(1)

    def test_det_weight_1(self):
        """det_1 = z_{(1)} = 1."""
        kac = KacDeterminantComparison()
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert kac.heisenberg_kac_det(1) == Fraction(1)

    def test_det_weight_2(self):
        """det_2 = z_{(2)} * z_{(1,1)} = 2 * 2 = 4."""
        kac = KacDeterminantComparison()
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert kac.heisenberg_kac_det(2) == Fraction(4)

    def test_det_weight_3(self):
        """det_3 = z_{(3)} * z_{(2,1)} * z_{(1,1,1)} = 3 * 2 * 6 = 36."""
        kac = KacDeterminantComparison()
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert kac.heisenberg_kac_det(3) == Fraction(36)

    def test_det_weight_4(self):
        """det_4 = prod z_lambda over 5 partitions of 4.
        z_{(4)}=4, z_{(3,1)}=3, z_{(2,2)}=8, z_{(2,1,1)}=4, z_{(1,1,1,1)}=24
        det = 4 * 3 * 8 * 4 * 24 = 9216.
        """
        kac = KacDeterminantComparison()
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert kac.heisenberg_kac_det(4) == Fraction(9216)

    def test_gram_matrix_diagonal(self):
        """Gram matrix for Heisenberg is diagonal."""
        kac = KacDeterminantComparison()
        G = kac.heisenberg_gram_matrix(3)
        for i in range(len(G)):
            for j in range(len(G[0])):
                if i != j:
                    # VERIFIED [DC] structural property [LC] boundary/limiting case
                    assert G[i][j] == Fraction(0)
                else:
                    # VERIFIED [DC] structural property [LC] boundary/limiting case
                    assert G[i][j] > 0

    def test_gram_matrix_det_equals_kac_det(self):
        """Product of diagonal entries = Kac determinant."""
        kac = KacDeterminantComparison()
        for w in range(5):
            G = kac.heisenberg_gram_matrix(w)
            det = Fraction(1)
            for i in range(len(G)):
                det *= G[i][i]
            assert det == kac.heisenberg_kac_det(w)

    def test_kac_det_always_positive(self):
        """For c=1 Heisenberg, all Kac determinants are positive (irreducible)."""
        kac = KacDeterminantComparison()
        for w in range(8):
            # VERIFIED [DC] positivity check [LC] boundary/limiting case
            assert kac.heisenberg_kac_det(w) > 0


# =========================================================================
# THREE-WAY COMPARISON TESTS
# =========================================================================

class TestCharacterComparison:
    """Tests for the four-way character comparison."""

    def test_walgebra_four_way_match(self):
        result = compare_characters(max_weight=12)
        assert result["walgebra_four_way_match"]

    def test_walgebra_equals_euler(self):
        result = compare_characters(max_weight=12)
        assert result["walgebra_equals_euler_partitions"]

    def test_macmahon_differs(self):
        result = compare_characters(max_weight=12)
        assert result["macmahon_differs_from_euler"]

    def test_first_difference_at_weight_2(self):
        result = compare_characters(max_weight=12)
        # VERIFIED [DC] conformal weight [DA] dimensional consistency
        assert result["first_difference_weight"] == 2

    def test_partition_oeis_match(self):
        result = compare_characters(max_weight=15)
        assert result["partition_match_oeis"]

    def test_plane_partition_oeis_match(self):
        result = compare_characters(max_weight=15)
        assert result["plane_partition_match_oeis"]


class TestOPEComparison:
    """Tests for OPE structure constant comparison."""

    def test_central_charge_match(self):
        result = compare_ope_structures()
        assert result["c_match"]

    def test_jj_match(self):
        result = compare_ope_structures()
        assert result["JJ_match"]

    def test_tt_match(self):
        result = compare_ope_structures()
        assert result["TT_match"]

    def test_ap44_divided_power(self):
        """Verify AP44 convention: lambda^3 coeff = c/12, not c/2."""
        result = compare_ope_structures()
        assert result["AP44_divided_power_check"]
        # VERIFIED [DC] Hodge class intersection [LC] AP44
        assert result["lambda_bracket_T3_coeff"] == Fraction(1, 12)


class TestKacDeterminantComparison3Way:
    """Tests for three-way Kac determinant comparison."""

    def test_all_match_up_to_weight_6(self):
        result = compare_kac_determinants(max_weight=6)
        assert result["all_match"]

    def test_individual_weights(self):
        result = compare_kac_determinants(max_weight=4)
        for w in range(5):
            assert result["weights"][w]["match"], f"Mismatch at weight {w}"


class TestShuffleStructure:
    """Tests for shuffle algebra structure at generic N."""

    def test_N2_structure(self):
        result = compare_shuffle_structure_at_generic_N(N=2)
        assert result["phi_1_is_zero"]
        assert result["phi_2_is_zero"]
        assert result["phi_3_equals_neg2_sigma3"]
        assert result["phi_4_is_zero"]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result["phi_3_value"] == Fraction(4)  # -2 * (-2) = 4

    def test_N3_structure(self):
        result = compare_shuffle_structure_at_generic_N(N=3)
        assert result["phi_1_is_zero"]
        assert result["phi_2_is_zero"]
        assert result["phi_3_equals_neg2_sigma3"]
        assert result["phi_4_is_zero"]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result["phi_3_value"] == Fraction(12)  # -2 * (-6) = 12


# =========================================================================
# COMPREHENSIVE TESTS
# =========================================================================

class TestFullComparison:
    """Tests for the full three-way comparison."""

    def test_all_five_paths_converge(self):
        """The definitive test: all five verification paths agree."""
        result = full_c3_comparison(max_weight=10)
        assert result["all_five_paths_converge"], result.get("verdict", "")

    def test_verdict(self):
        result = full_c3_comparison(max_weight=10)
        assert "ALL FIVE PATHS CONVERGE" in result["verdict"]


class TestAdditionalCrossChecks:
    """Tests for additional cross-checks."""

    def test_g_inversion_N2(self):
        result = verify_g_inversion_at_N(N=2)
        assert result["all_pass"]

    def test_g_inversion_N3(self):
        result = verify_g_inversion_at_N(N=3)
        assert result["all_pass"]

    def test_g_inversion_N5(self):
        result = verify_g_inversion_at_N(N=5)
        assert result["all_pass"]

    def test_character_factorization(self):
        """M(q) / P(q) = prod_{n>=2} 1/(1-q^n)^{n-1}."""
        result = verify_character_factorization(max_weight=12)
        assert result["factorization_match"]

    def test_character_factorization_coefficients(self):
        """First few coefficients of M(q)/P(q)."""
        result = verify_character_factorization(max_weight=10)
        coeffs = result["ratio_coefficients"]
        # M(q)/P(q) = 1 + 0*q + q^2 + q^3 + 3q^4 + 3q^5 + ...
        # prod_{n>=2} 1/(1-q^n)^{n-1} = 1/(1-q^2) * 1/(1-q^3)^2 * ...
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert coeffs[0] == 1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert coeffs[1] == 0  # No q^1 term
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert coeffs[2] == 1  # From 1/(1-q^2)

    def test_sugawara_verification(self):
        result = verify_sugawara_at_c1()
        assert result["match"]
        # VERIFIED [DC] Hodge class intersection [LC] boundary/limiting case
        assert result["lambda_bracket_lambda3_coeff"] == Fraction(1, 12)

    def test_structure_function_N1_to_N5(self):
        result = cross_check_structure_function_N1_to_N5()
        assert result["all_pass"]


# =========================================================================
# PARTITION COMBINATORICS (foundational)
# =========================================================================

class TestPartitionCombinatorics:
    """Foundational tests for partition functions."""

    def test_partition_count_0(self):
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert len(_partitions_of(0)) == 1

    def test_partition_count_1(self):
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert len(_partitions_of(1)) == 1

    def test_partition_count_2(self):
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert len(_partitions_of(2)) == 2

    def test_partition_count_3(self):
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert len(_partitions_of(3)) == 3

    def test_partition_count_4(self):
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert len(_partitions_of(4)) == 5

    def test_partition_count_5(self):
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert len(_partitions_of(5)) == 7

    def test_z_lambda_identity(self):
        """sum_{lambda of n} 1/z_lambda = 1 (class equation for S_n)."""
        # Actually: sum_{lambda of n} n!/z_lambda = n! (trivially)
        # The correct identity: sum_{lambda of n} (1/z_lambda) = 1
        # is FALSE in general. The correct statement is:
        # sum_{lambda of n} (n! / z_lambda) = n!  (trivially)
        # or: sum_{lambda of n} 1/z_lambda = number of conjugacy classes / ...
        # Let me just verify the z_lambda sum identity:
        # sum_{lambda of n} (n!/z_lambda) = number of permutations = n!
        # This is because n!/z_lambda = |conjugacy class of type lambda|.
        import math
        for n in range(1, 7):
            total = Fraction(0)
            for lam in _partitions_of(n):
                total += Fraction(math.factorial(n)) / _z_lambda(lam)
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert total == Fraction(math.factorial(n))

    def test_z_lambda_empty(self):
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert _z_lambda(()) == Fraction(1)


# =========================================================================
# N-DEPENDENCE TESTS
# =========================================================================

class TestNDependence:
    """Tests for the N-dependence of the constructions."""

    def test_central_charges_agree(self):
        """All constructions give c = N."""
        for N in range(1, 6):
            env = EnvelopeConstruction(level=N)
            shuf = ShuffleConstruction(N=N)
            ff = FreeFieldConstruction(N=N)
            # VERIFIED [DC] central charge formula [LT] literature cross-check
            assert env.central_charge == Fraction(N)
            # VERIFIED [DC] central charge formula [LT] literature cross-check
            assert shuf.central_charge == Fraction(N)
            # VERIFIED [DC] central charge [LC] boundary/limiting case
            assert ff.c == Fraction(N)

    def test_characters_agree_across_constructions(self):
        """W-algebra character = P(q)^N for all N and all constructions."""
        for N in range(1, 4):
            env = EnvelopeConstruction(level=N)
            shuf = ShuffleConstruction(N=N)
            crystal = CrystalMeltingConstruction(N=N)
            ff = FreeFieldConstruction(N=N)

            ch_env = env.character_coefficients(max_weight=8)
            ch_shuf = shuf.character_coefficients(max_weight=8)
            ch_crystal = crystal.walgebra_character(max_weight=8)
            ch_ff = ff.character_coefficients(max_weight=8)

            assert ch_env == ch_shuf, f"Envelope != Shuffle at N={N}"
            assert ch_env == ch_crystal, f"Envelope != Crystal at N={N}"
            assert ch_env == ch_ff, f"Envelope != FreeField at N={N}"

    def test_sigma_2_formula(self):
        """sigma_2 = -(N^2 - N + 1) for the SV parametrization."""
        for N in range(1, 8):
            shuf = ShuffleConstruction(N=N)
            expected = Fraction(-(N * N - N + 1))
            assert shuf.sigma_2 == expected, f"N={N}: {shuf.sigma_2} != {expected}"

    def test_sigma_3_formula(self):
        """sigma_3 = N(1-N) for the SV parametrization."""
        for N in range(1, 8):
            shuf = ShuffleConstruction(N=N)
            expected = Fraction(N * (1 - N))
            assert shuf.sigma_3 == expected, f"N={N}: {shuf.sigma_3} != {expected}"

    def test_phi_3_at_various_N(self):
        """phi_3 = -2*sigma_3 = -2*N*(1-N) = 2*N*(N-1)."""
        for N in range(1, 8):
            shuf = ShuffleConstruction(N=N)
            phi = shuf.structure_function_coefficients(max_order=5)
            expected = Fraction(2 * N * (N - 1))
            assert phi[3] == expected, f"N={N}: phi_3={phi[3]} != {expected}"
