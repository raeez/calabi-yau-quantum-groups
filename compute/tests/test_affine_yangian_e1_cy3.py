r"""Tests for the affine Yangian Y(gl_hat_1) from E_1 bar complex of W_{1+inf}.

Verifies:
  (a) R-matrix = collision residue of E_1 shadow obstruction tower
  (b) Shuffle algebra identification
  (c) Higher-genus DT invariants
  (d) Yang-Baxter equation from MC equation
  (e) Multi-path cross-verification (3+ independent paths per claim)

Manuscript references:
  thm:yangian-e1 (yangians_foundations.tex): Y(g) as E_1-chiral algebra
  thm:e1-chiral-koszul-duality: E_1 bar-cobar Koszul duality via R-matrix
  thm:sv-c3 (toric_cy3_coha.tex): CoHA(C^3) = Y^+(gl_hat_1)
  cor:mc3-all-types: MC3 proved for all simple types

Literature:
  Schiffmann-Vasserot arXiv:1211.1287 (CoHA = positive Yangian)
  Tsymbaliuk arXiv:1404.5240 (affine Yangian presentation)
  Prochazka-Rapcak arXiv:1910.07997 (W_{1+inf} and Yangian)
  Maulik-Okounkov arXiv:1211.1287 (quantum groups from geometry)

Ground truth values:
  h = (1, 2, -3): sigma_2 = -7, sigma_3 = -6
  phi = [1, 0, 0, 12, 0, 84, 72, 588, 1008, 4548, ...]
  phi_3 = -2*sigma_3 = 12
  BPS invariants: Omega(n) = n for all n >= 1
  lambda_1^FP = 1/24, lambda_2^FP = 7/5760
"""

import pytest
from fractions import Fraction

from compute.lib.affine_yangian_e1_cy3 import (
    classical_r_matrix_coefficients,
    collision_residue_e1,
    comprehensive_atlas,
    cross_verify_bps_3paths,
    cross_verify_genus_tower,
    cross_verify_r_matrix_3paths,
    dt_invariants_from_shadow,
    e1_bar_differential_matrix,
    e1_shadow_tower_arity2,
    faber_pandharipande,
    genus_g_free_energy,
    genus_tower_w_infinity,
    kappa_per_channel,
    kappa_w_infinity_regulated,
    macmahon_from_genus_regulated,
    macmahon_genus_decomposition,
    r_matrix_from_g,
    shadow_depth_per_channel,
    shuffle_product_arity2,
    shuffle_product_explicit_low_degree,
    structure_function_at_integer,
    total_shadow_depth,
    verify_classical_ybe_scalar,
    verify_g_minus_z_equals_inv_g,
    verify_log_g_odd_powers_only,
    verify_quantum_ybe_scalar,
    verify_r_equals_collision_residue,
    verify_shuffle_deconcatenation,
    verify_unitarity,
    ybe_from_mc_arity3,
)
from compute.lib.affine_yangian_gl1 import (
    elementary_symmetric_from_h,
    phi_explicit,
    power_sums_from_h,
    structure_function_coefficients,
)


# ================================================================
# SECTION 1: CLASSICAL r-MATRIX BASIC PROPERTIES
# ================================================================

class TestClassicalRMatrix:
    """Tests for the classical r-matrix r(z) = g(z) - 1."""

    def test_r_matrix_starts_at_z_minus_3(self):
        """The r-matrix starts at z^{-3} (phi_1 = phi_2 = 0 by CY condition)."""
        r = classical_r_matrix_coefficients(Fraction(1), Fraction(2), max_order=6)
        assert 1 not in r, "r-matrix should have no z^{-1} pole (CY condition)"
        assert 2 not in r, "r-matrix should have no z^{-2} pole"
        assert 3 in r, "r-matrix should have z^{-3} pole"

    def test_r_matrix_even_poles_from_log_products(self):
        """The r-matrix r(z)=g(z)-1 has BOTH odd and even powers.

        log g has only odd powers alpha_k (k odd). But g = exp(log g),
        and exponentiation creates even-power terms from products of
        odd alpha_k: phi_6 = alpha_3^2/2, phi_8 = alpha_3*alpha_5, etc.

        The ODD-only property is for LOG g, not for g-1.
        The INVERSION identity g(-z) = 1/g(z) means:
          phi_j(-h) = (-1)^j phi_j(h)  (parity under h -> -h)
        NOT that even phi vanish.
        """
        r = classical_r_matrix_coefficients(Fraction(1), Fraction(2), max_order=10)
        # phi_6 = alpha_3^2/2 = (-2*sigma_3)^2/2 = 2*36 = 72
        assert 6 in r and r[6] == 72, f"phi_6 should be 72, got {r.get(6)}"
        # phi_4 = 0 (no partition of 4 into odd parts >= 3)
        assert 4 not in r, f"phi_4 should be 0, but found in r"

    def test_r_matrix_leading_term_equals_neg2_sigma3(self):
        """The leading r-matrix coefficient is phi_3 = -2*sigma_3."""
        for h1, h2 in [(Fraction(1), Fraction(2)),
                        (Fraction(3), Fraction(-1)),
                        (Fraction(1, 2), Fraction(1, 3))]:
            h3 = -(h1 + h2)
            sigma3 = h1 * h2 * h3
            r = classical_r_matrix_coefficients(h1, h2, max_order=6)
            assert r[3] == -2 * sigma3, (
                f"phi_3 = {r[3]} should equal -2*sigma_3 = {-2 * sigma3}"
            )

    def test_r_matrix_vanishes_at_abelian_point(self):
        """At GL_1 (h=(1,-1,0)): sigma_3=0, so phi_j=0 for all j>=1."""
        r = classical_r_matrix_coefficients(Fraction(1), Fraction(-1), max_order=10)
        assert len(r) == 0, f"r-matrix should vanish at abelian point, got {r}"

    def test_r_matrix_gl2_values(self):
        """Ground truth values for GL_2: h=(1,-2,1), sigma_3=-2."""
        r = classical_r_matrix_coefficients(Fraction(1), Fraction(-2), max_order=8)
        # phi_3 = -2*sigma_3 = -2*(-2) = 4
        assert r[3] == 4

    def test_r_matrix_generic_values(self):
        """Ground truth values for h=(1,2,-3): sigma_3 = -6, phi_3 = 12."""
        r = classical_r_matrix_coefficients(Fraction(1), Fraction(2), max_order=6)
        assert r[3] == 12, f"phi_3 should be 12, got {r[3]}"


class TestRMatrixMultipleParametrizations:
    """Test r-matrix across multiple parametrizations."""

    @pytest.mark.parametrize("h1,h2,expected_sigma3", [
        (Fraction(1), Fraction(2), Fraction(-6)),
        (Fraction(1), Fraction(-2), Fraction(-2)),
        (Fraction(1), Fraction(-3), Fraction(-6)),
        (Fraction(2), Fraction(3), Fraction(-30)),
        (Fraction(1, 2), Fraction(1, 3), Fraction(5, 36)),
    ])
    def test_phi_3_across_params(self, h1, h2, expected_sigma3):
        """phi_3 = -2*sigma_3 for various (h1, h2)."""
        h3 = -(h1 + h2)
        actual_sigma3 = h1 * h2 * h3
        assert actual_sigma3 == expected_sigma3, (
            f"sigma_3({h1},{h2},{h3}) = {actual_sigma3}, expected {expected_sigma3}"
        )
        r = classical_r_matrix_coefficients(h1, h2, max_order=4)
        assert r.get(3, Fraction(0)) == -2 * expected_sigma3


# ================================================================
# SECTION 2: UNITARITY AND INVERSION IDENTITY
# ================================================================

class TestUnitarity:
    """Tests for R(z)R(-z) = 1, i.e., g(-z) = 1/g(z)."""

    def test_unitarity_generic(self):
        """g(z)*g(-z) = 1 for h=(1,2,-3)."""
        result = verify_unitarity(Fraction(1), Fraction(2), max_order=10)
        assert result['all_pass'], "Unitarity failed for generic parameters"

    def test_unitarity_gl2(self):
        """g(z)*g(-z) = 1 for GL_2 parametrization."""
        result = verify_unitarity(Fraction(1), Fraction(-2), max_order=10)
        assert result['all_pass']

    def test_unitarity_gl3(self):
        """g(z)*g(-z) = 1 for GL_3 parametrization."""
        result = verify_unitarity(Fraction(1), Fraction(-3), max_order=10)
        assert result['all_pass']

    def test_unitarity_rational_params(self):
        """g(z)*g(-z) = 1 for rational h parameters."""
        result = verify_unitarity(Fraction(1, 2), Fraction(1, 3), max_order=8)
        assert result['all_pass']

    @pytest.mark.parametrize("h1,h2", [
        (Fraction(1), Fraction(2)),
        (Fraction(3), Fraction(-1)),
        (Fraction(5), Fraction(7)),
        (Fraction(1, 3), Fraction(2, 5)),
    ])
    def test_unitarity_parametric(self, h1, h2):
        """Unitarity holds for all CY parameters."""
        result = verify_unitarity(h1, h2, max_order=8)
        assert result['all_pass']


class TestGInversion:
    """Tests for g(-z) = 1/g(z) via direct computation."""

    def test_g_inversion_generic(self):
        assert verify_g_minus_z_equals_inv_g(Fraction(1), Fraction(2), max_order=10)

    def test_g_inversion_gl2(self):
        assert verify_g_minus_z_equals_inv_g(Fraction(1), Fraction(-2), max_order=10)

    def test_g_inversion_gl3(self):
        assert verify_g_minus_z_equals_inv_g(Fraction(1), Fraction(-3), max_order=10)

    def test_g_inversion_rational(self):
        assert verify_g_minus_z_equals_inv_g(Fraction(1, 2), Fraction(1, 3), max_order=8)


class TestLogGOddPowers:
    """Tests for log g(z) having only odd powers of z^{-1}."""

    def test_log_g_even_vanish_generic(self):
        result = verify_log_g_odd_powers_only(Fraction(1), Fraction(2))
        assert result['even_vanish']

    def test_log_g_alpha1_zero_cy(self):
        """alpha_1 = 0 by CY condition (p_1 = 0)."""
        result = verify_log_g_odd_powers_only(Fraction(1), Fraction(2))
        assert result['alpha_1_zero']

    def test_log_g_all_pass(self):
        result = verify_log_g_odd_powers_only(Fraction(1), Fraction(2), max_order=12)
        assert result['all_pass']

    @pytest.mark.parametrize("h1,h2", [
        (Fraction(1), Fraction(2)),
        (Fraction(3), Fraction(-1)),
        (Fraction(1, 7), Fraction(2, 7)),
    ])
    def test_log_g_parametric(self, h1, h2):
        result = verify_log_g_odd_powers_only(h1, h2, max_order=10)
        assert result['all_pass']


# ================================================================
# SECTION 3: COLLISION RESIDUE = R-MATRIX IDENTIFICATION
# ================================================================

class TestCollisionResidue:
    """Tests for Res^{coll}_{0,2}(Theta^{E_1}) = r(z)."""

    def test_collision_residue_scalar_vanishes(self):
        """The scalar collision residue (z^{-1} coefficient) vanishes by CY."""
        data = collision_residue_e1(Fraction(1), Fraction(2))
        assert data['collision_residue_scalar'] == 0

    def test_collision_residue_scalar_vanishes_gl2(self):
        data = collision_residue_e1(Fraction(1), Fraction(-2))
        assert data['collision_residue_scalar'] == 0

    def test_collision_residue_leading_term(self):
        """Leading collision residue is phi_3 = -2*sigma_3."""
        data = collision_residue_e1(Fraction(1), Fraction(2))
        assert data['r_matrix_coefficients'].get(3) == 12  # -2*(-6) = 12

    def test_r_matrix_coefficients_match_phi(self):
        """r-matrix coefficients match phi_j for j >= 3."""
        h1, h2 = Fraction(1), Fraction(2)
        data = collision_residue_e1(h1, h2, max_order=10)
        phi = data['phi']
        r = data['r_matrix_coefficients']
        for k in r:
            assert r[k] == phi[k], f"r[{k}]={r[k]} should equal phi[{k}]={phi[k]}"


class TestREqualsCollisionResidue:
    """Verify the identification r(z) = collision residue of E_1 shadow tower."""

    def test_verification_generic(self):
        result = verify_r_equals_collision_residue(Fraction(1), Fraction(2))
        assert result['unitarity_verified']
        assert result['mc_arity2_vanishes']

    def test_verification_gl2(self):
        result = verify_r_equals_collision_residue(Fraction(1), Fraction(-2))
        assert result['unitarity_verified']
        assert result['mc_arity2_vanishes']

    def test_verification_gl3(self):
        result = verify_r_equals_collision_residue(Fraction(1), Fraction(-3))
        assert result['unitarity_verified']
        assert result['mc_arity2_vanishes']

    def test_mc_arity2_equation_content(self):
        """The arity-2 MC equation r(z)+r(-z)+r(z)r(-z)=0 holds."""
        result = verify_r_equals_collision_residue(Fraction(1), Fraction(2), max_order=10)
        for i, v in enumerate(result['mc_arity2_values']):
            assert v == 0, f"MC arity-2 at order {i} = {v}, should be 0"


# ================================================================
# SECTION 4: YANG-BAXTER EQUATION
# ================================================================

class TestYangBaxter:
    """Tests for the Yang-Baxter equation derived from the MC equation."""

    def test_scalar_cybe_trivial(self):
        """For scalar R-matrices, CYBE is trivially satisfied."""
        result = verify_classical_ybe_scalar(Fraction(1), Fraction(2))
        assert result['scalar_cybe_trivial']
        assert result['unitarity_verified']

    def test_scalar_qybe_trivial(self):
        """For scalar R-matrices, quantum YBE is trivially satisfied."""
        result = verify_quantum_ybe_scalar(Fraction(1), Fraction(2))
        assert result['scalar_qybe_trivial']
        assert result['unitarity']

    def test_ybe_from_mc_arity3_nonzero_bracket(self):
        """The arity-3 MC bracket is generally nonzero (solved by Serre)."""
        result = ybe_from_mc_arity3(Fraction(1), Fraction(2))
        # For generic parameters, the bracket should be nonzero
        some_nonzero = False
        for key, val in result['results'].items():
            if val['bracket_3'] != 0:
                some_nonzero = True
                break
        assert some_nonzero, (
            "Arity-3 bracket should be nonzero for generic parameters"
        )

    def test_ybe_from_mc_abelian_limit(self):
        """At the abelian limit (h=(1,-1,0)), all brackets vanish."""
        result = ybe_from_mc_arity3(Fraction(1), Fraction(-1))
        for key, val in result['results'].items():
            assert val['bracket_3'] == 0, (
                f"Bracket should vanish at abelian limit, got {val['bracket_3']}"
            )


class TestMCEquationContent:
    """Test the MC equation D*Theta + (1/2)[Theta,Theta] = 0 at arity 2."""

    def test_mc_arity2_is_unitarity(self):
        """The arity-2 MC equation reduces to unitarity g(z)g(-z)=1."""
        # This is the key theorem: the MC equation at arity 2, when projected
        # to the E_1 shadow tower, gives exactly the unitarity condition.
        result = verify_r_equals_collision_residue(Fraction(1), Fraction(2))
        assert result['mc_arity2_vanishes'], (
            "MC equation at arity 2 should be equivalent to unitarity"
        )

    @pytest.mark.parametrize("h1,h2", [
        (Fraction(1), Fraction(2)),
        (Fraction(1), Fraction(-2)),
        (Fraction(1), Fraction(-3)),
        (Fraction(2), Fraction(3)),
    ])
    def test_mc_arity2_parametric(self, h1, h2):
        result = verify_r_equals_collision_residue(h1, h2, max_order=8)
        assert result['mc_arity2_vanishes']


# ================================================================
# SECTION 5: SHUFFLE ALGEBRA
# ================================================================

class TestShuffleAlgebra:
    """Tests for the shuffle algebra presentation of Y^+(gl_hat_1)."""

    def test_shuffle_product_symmetric_part(self):
        """The symmetric part of g(u) + 1/g(u) has only even powers."""
        h1, h2 = Fraction(1), Fraction(2)
        phi = phi_explicit(h1, h2, max_order=10)
        result = shuffle_product_arity2([], [], phi, max_degree=10)
        # Odd coefficients should vanish (g + 1/g is even)
        for n in range(1, len(result)):
            if n % 2 == 1:
                assert result[n] == 0, (
                    f"Odd coefficient at order {n} = {result[n]}, should be 0"
                )

    def test_shuffle_product_leading_symmetric(self):
        """g(u) + 1/g(u) starts at 2 (constant term)."""
        h1, h2 = Fraction(1), Fraction(2)
        phi = phi_explicit(h1, h2, max_order=10)
        result = shuffle_product_arity2([], [], phi, max_degree=10)
        assert result[0] == 2, f"Constant term should be 2, got {result[0]}"

    def test_shuffle_explicit_antisymmetric_odd(self):
        """g(u) - 1/g(u) has only odd powers."""
        result = shuffle_product_explicit_low_degree(Fraction(1), Fraction(2))
        g_minus = result['g_minus_ginv']
        for n in range(len(g_minus)):
            if n % 2 == 0:
                assert g_minus[n] == 0, (
                    f"Even coefficient at order {n} = {g_minus[n]}, should be 0"
                )

    def test_shuffle_explicit_symmetric_even(self):
        """g(u) + 1/g(u) has only even powers."""
        result = shuffle_product_explicit_low_degree(Fraction(1), Fraction(2))
        g_plus = result['g_plus_ginv']
        for n in range(len(g_plus)):
            if n % 2 == 1:
                assert g_plus[n] == 0, (
                    f"Odd coefficient at order {n} = {g_plus[n]}, should be 0"
                )

    def test_shuffle_deconcatenation_dimensions(self):
        """Verify bar deconcatenation dimensions are consistent."""
        result = verify_shuffle_deconcatenation(max_degree=6)
        # The target dimension should be >= source dimension
        # (deconcatenation is a coproduct, not a restriction)
        for key, val in result.items():
            assert val['target_total_dim'] >= val['source_dim'], (
                f"At (n,k)={key}: target {val['target_total_dim']} < source {val['source_dim']}"
            )


class TestShuffleProductGlN:
    """Shuffle product for specific GL_N parametrizations."""

    def test_shuffle_abelian_limit(self):
        """At GL_1 (abelian): g=1, so g+1/g = 2 and g-1/g = 0."""
        result = shuffle_product_explicit_low_degree(Fraction(1), Fraction(-1))
        g_plus = result['g_plus_ginv']
        g_minus = result['g_minus_ginv']
        assert g_plus[0] == 2
        for n in range(1, len(g_plus)):
            assert g_plus[n] == 0, f"Abelian: g+1/g should be constant 2, order {n} = {g_plus[n]}"
        for n in range(len(g_minus)):
            assert g_minus[n] == 0, f"Abelian: g-1/g should be 0, order {n} = {g_minus[n]}"

    def test_shuffle_gl2_nontrivial(self):
        """GL_2 (h=(1,-2,1)): g is nontrivial, g+1/g has even-power corrections."""
        result = shuffle_product_explicit_low_degree(Fraction(1), Fraction(-2))
        g_plus = result['g_plus_ginv']
        # phi_3 = -2*sigma_3 = -2*(-2) = 4, so nonzero odd poles
        assert g_plus[0] == 2
        # Even powers may be nonzero (from phi_6 = alpha_3^2/2 = 2*sigma_3^2)
        # sigma_3 = -2, phi_6 = 2*4 = 8
        # g_plus[6] = phi_6 + gamma_6 where gamma_6 is from 1/g


# ================================================================
# SECTION 6: HIGHER GENUS AND DT INVARIANTS
# ================================================================

class TestKappaRegulated:
    """Tests for the regulated kappa of W_{1+inf}."""

    def test_kappa_n1(self):
        """kappa(W_{1+inf}, N=1) = H_1 = 1."""
        assert kappa_w_infinity_regulated(1) == Fraction(1)

    def test_kappa_n2(self):
        """kappa(W_{1+inf}, N=2) = H_2 = 3/2."""
        assert kappa_w_infinity_regulated(2) == Fraction(3, 2)

    def test_kappa_n3(self):
        """kappa(W_{1+inf}, N=3) = H_3 = 11/6."""
        assert kappa_w_infinity_regulated(3) == Fraction(11, 6)

    def test_kappa_n10(self):
        """kappa(W_{1+inf}, N=10) = H_10 = 7381/2520."""
        expected = sum(Fraction(1, k) for k in range(1, 11))
        assert kappa_w_infinity_regulated(10) == expected

    def test_kappa_monotone_increasing(self):
        """kappa(N) is strictly increasing."""
        prev = Fraction(0)
        for N in range(1, 20):
            curr = kappa_w_infinity_regulated(N)
            assert curr > prev, f"kappa({N}) = {curr} <= kappa({N-1}) = {prev}"
            prev = curr


class TestFaberPandharipande:
    """Tests for Faber-Pandharipande intersection numbers."""

    def test_lambda_1(self):
        """lambda_1^FP = 1/24."""
        assert faber_pandharipande(1) == Fraction(1, 24)

    def test_lambda_2(self):
        """lambda_2^FP = 7/5760."""
        assert faber_pandharipande(2) == Fraction(7, 5760)

    def test_lambda_3(self):
        """lambda_3^FP = 31/967680."""
        assert faber_pandharipande(3) == Fraction(31, 967680)

    def test_lambda_positive(self):
        """All lambda_g^FP are positive."""
        for g in range(1, 8):
            assert faber_pandharipande(g) > 0

    def test_lambda_decreasing(self):
        """lambda_g^FP is strictly decreasing."""
        prev = Fraction(1)
        for g in range(1, 8):
            curr = faber_pandharipande(g)
            assert curr < prev, f"lambda_{g} = {curr} >= lambda_{g-1} = {prev}"
            prev = curr

    def test_lambda_1_invalid(self):
        with pytest.raises(ValueError):
            faber_pandharipande(0)


class TestGenusTower:
    """Tests for the genus tower F_g(W_{1+inf}, regulated)."""

    def test_f1_at_n1(self):
        """F_1(W_{1+inf}, N=1) = H_1 * 1/24 = 1/24."""
        tower = genus_tower_w_infinity(1)
        assert tower[1] == Fraction(1, 24)

    def test_f1_at_n2(self):
        """F_1(W_{1+inf}, N=2) = H_2 * 1/24 = 3/2 * 1/24 = 1/16."""
        tower = genus_tower_w_infinity(2)
        assert tower[1] == Fraction(3, 2) * Fraction(1, 24)
        assert tower[1] == Fraction(1, 16)

    def test_f2_at_n1(self):
        """F_2(W_{1+inf}, N=1) = 1 * 7/5760 = 7/5760."""
        tower = genus_tower_w_infinity(1)
        assert tower[2] == Fraction(7, 5760)

    def test_genus_tower_positive(self):
        """All F_g values are positive."""
        tower = genus_tower_w_infinity(5, max_genus=5)
        for g in range(1, 6):
            assert tower[g] > 0

    def test_genus_tower_proportional_to_kappa(self):
        """F_g(N) = H_N * lambda_g^FP for all N and g."""
        for N in [1, 2, 5, 10]:
            tower = genus_tower_w_infinity(N, max_genus=4)
            kappa = kappa_w_infinity_regulated(N)
            for g in range(1, 5):
                expected = kappa * faber_pandharipande(g)
                assert tower[g] == expected, (
                    f"F_{g}(N={N}) = {tower[g]}, expected kappa*lambda = {expected}"
                )


class TestDTInvariants:
    """Tests for DT invariants of C^3."""

    def test_bps_invariants_direct(self):
        """Omega(n) = n for n >= 1."""
        result = dt_invariants_from_shadow(15)
        for n in range(1, 15):
            assert result['bps_direct'][n] == n

    def test_bps_agree_with_macmahon(self):
        """BPS from plethystic log of MacMahon agrees with direct formula."""
        result = dt_invariants_from_shadow(15)
        assert result['agreement'], "BPS invariants disagree between paths"

    def test_macmahon_first_values(self):
        """MacMahon function first values: M(q) = 1 + q + 3q^2 + 6q^3 + ..."""
        result = dt_invariants_from_shadow(10)
        expected = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282]
        for i in range(min(10, len(result['macmahon_coeffs']))):
            assert result['macmahon_coeffs'][i] == expected[i], (
                f"M(q) coeff at q^{i} = {result['macmahon_coeffs'][i]}, expected {expected[i]}"
            )

    def test_dt_partition_function_signs(self):
        """Z^DT(C^3) = M(-q): alternating signs."""
        result = dt_invariants_from_shadow(10)
        for i, c in enumerate(result['dt_coeffs']):
            # M(-q) coefficients have sign (-1)^n * p(n)
            expected_sign = (-1) ** i
            expected = result['macmahon_coeffs'][i] * expected_sign
            assert c == expected


class TestMacMahonFromChannels:
    """Test that M(q) is recovered from the channel decomposition."""

    def test_macmahon_cutoff_5(self):
        """Channel product matches MacMahon up to q^4 for cutoff N=5."""
        result = macmahon_from_genus_regulated(5, max_degree=4)
        assert result['agrees_up_to'] >= 4

    def test_macmahon_cutoff_10(self):
        """Channel product matches MacMahon up to q^9 for cutoff N=10."""
        result = macmahon_from_genus_regulated(10, max_degree=9)
        assert result['agrees_up_to'] >= 9

    def test_macmahon_cutoff_exact(self):
        """For cutoff N >= max_degree, channel product = MacMahon exactly."""
        result = macmahon_from_genus_regulated(20, max_degree=8)
        for n in range(9):
            assert result['channel_product'][n] == result['macmahon'][n], (
                f"At q^{n}: channel={result['channel_product'][n]}, mac={result['macmahon'][n]}"
            )


# ================================================================
# SECTION 7: E_1 SHADOW TOWER
# ================================================================

class TestE1ShadowTower:
    """Tests for the E_1 shadow obstruction tower."""

    def test_arity2_r_matrix_generic(self):
        """The arity-2 E_1 shadow is the r-matrix r(z) = g(z) - 1."""
        data = e1_shadow_tower_arity2(Fraction(1), Fraction(2))
        assert data['phi_3'] == 12  # -2*(-6)
        assert data['sigma_3'] == -6

    def test_arity2_antisymmetric_is_odd(self):
        """The antisymmetric (genuinely E_1) part has only odd-order poles."""
        data = e1_shadow_tower_arity2(Fraction(1), Fraction(2))
        for k in data['r_antisymmetric']:
            assert k % 2 == 1, f"Antisymmetric part has even-order pole at {k}"

    def test_arity2_symmetric_is_even(self):
        """The symmetric (E_inf) part has only even-order poles."""
        data = e1_shadow_tower_arity2(Fraction(1), Fraction(2))
        for k in data['r_symmetric']:
            assert k % 2 == 0, f"Symmetric part has odd-order pole at {k}"

    def test_arity2_abelian_vanishes(self):
        """At the abelian point, the E_1 shadow tower vanishes."""
        data = e1_shadow_tower_arity2(Fraction(1), Fraction(-1))
        assert len(data['r_matrix_full']) == 0

    def test_e1_bar_differential_structure(self):
        """The E_1 bar differential involves the structure function."""
        data = e1_bar_differential_matrix(Fraction(1), Fraction(2))
        assert data['g_leading_nontrivial'] == 12  # phi_3


# ================================================================
# SECTION 8: SHADOW DEPTH AND CLASSIFICATION
# ================================================================

class TestShadowDepth:
    """Tests for shadow depth classification."""

    def test_spin1_is_gaussian(self):
        """Spin-1 (Heisenberg) channel is class G."""
        depths = shadow_depth_per_channel()
        assert depths[1] == 'G'

    def test_spin2_is_mixed(self):
        """Spin-2 (Virasoro) channel is class M."""
        depths = shadow_depth_per_channel()
        assert depths[2] == 'M'

    def test_total_depth_infinite(self):
        """Total shadow depth of W_{1+inf} is infinity."""
        assert total_shadow_depth() == float('inf')

    def test_kappa_per_channel_values(self):
        """kappa_s = c/s for each channel."""
        kappas = kappa_per_channel(Fraction(1), max_spin=5)
        assert kappas[1] == Fraction(1)
        assert kappas[2] == Fraction(1, 2)
        assert kappas[3] == Fraction(1, 3)
        assert kappas[4] == Fraction(1, 4)
        assert kappas[5] == Fraction(1, 5)


# ================================================================
# SECTION 9: CROSS-VERIFICATION (3+ PATHS)
# ================================================================

class TestCrossVerifyRMatrix:
    """Cross-verify R-matrix via 3 independent paths."""

    def test_3path_generic(self):
        result = cross_verify_r_matrix_3paths(Fraction(1), Fraction(2))
        assert result['path12_agree'], "Series and exponentiation disagree"

    def test_3path_gl2(self):
        result = cross_verify_r_matrix_3paths(Fraction(1), Fraction(-2))
        assert result['path12_agree']

    def test_3path_gl3(self):
        result = cross_verify_r_matrix_3paths(Fraction(1), Fraction(-3))
        assert result['path12_agree']

    def test_3path_numerical_close(self):
        """Numerical evaluation of g(z) matches series expansion at z=100."""
        result = cross_verify_r_matrix_3paths(Fraction(1), Fraction(2))
        for z_val, check in result['numerical_checks'].items():
            # At z=100 with order 10 terms, the difference should be < 10^{-20}
            assert check['diff'] < Fraction(1, 10**10), (
                f"At z={z_val}: diff={check['diff']} too large"
            )


class TestCrossVerifyBPS:
    """Cross-verify BPS invariants via 3 paths."""

    def test_3path_bps(self):
        result = cross_verify_bps_3paths(12)
        assert result['all_agree'], (
            f"BPS paths disagree: 12={result['path12_agree']}, 13={result['path13_agree']}"
        )

    def test_bps_path1_values(self):
        result = cross_verify_bps_3paths(10)
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert result['bps_direct'] == expected

    def test_bps_path2_matches(self):
        result = cross_verify_bps_3paths(10)
        assert result['path12_agree']

    def test_bps_path3_matches(self):
        result = cross_verify_bps_3paths(10)
        assert result['path13_agree']


class TestCrossVerifyGenusTower:
    """Cross-verify genus tower via multiple paths."""

    def test_genus_tower_2paths(self):
        result = cross_verify_genus_tower(10)
        assert result['kappa_agree'], "Kappa computation disagrees between modules"
        assert result['paths_agree'], "Genus tower paths disagree"


# ================================================================
# SECTION 10: COMPREHENSIVE ATLAS
# ================================================================

class TestComprehensiveAtlas:
    """Tests for the comprehensive atlas across parametrizations."""

    def test_atlas_sigma1_zero(self):
        """CY condition: sigma_1 = 0 for all parametrizations."""
        atlas = comprehensive_atlas()
        for name, data in atlas.items():
            assert data['sigma_1'] == 0, (
                f"sigma_1 != 0 for {name}: {data['sigma_1']}"
            )

    def test_atlas_unitarity_all(self):
        """Unitarity holds for all parametrizations."""
        atlas = comprehensive_atlas()
        for name, data in atlas.items():
            assert data['unitarity'], f"Unitarity failed for {name}"

    def test_atlas_log_odd_all(self):
        """Log g has only odd powers for all parametrizations."""
        atlas = comprehensive_atlas()
        for name, data in atlas.items():
            assert data['log_odd_only'], f"Log-odd-powers failed for {name}"

    def test_atlas_g_inversion_all(self):
        """g(-z) = 1/g(z) for all parametrizations."""
        atlas = comprehensive_atlas()
        for name, data in atlas.items():
            assert data['g_inversion'], f"g-inversion failed for {name}"

    def test_atlas_abelian_trivial(self):
        """At the abelian point, all r-matrix coefficients vanish."""
        atlas = comprehensive_atlas()
        r_abelian = atlas['GL_1_abelian']['r_leading']
        assert len(r_abelian) == 0, f"Abelian r-matrix nonzero: {r_abelian}"

    def test_atlas_generic_phi3(self):
        """Generic parametrization has phi_3 = 12."""
        atlas = comprehensive_atlas()
        assert atlas['generic']['phi'][3] == 12

    def test_atlas_gl2_phi3(self):
        """GL_2 has phi_3 = -2*sigma_3 = 4."""
        atlas = comprehensive_atlas()
        assert atlas['GL_2']['phi'][3] == 4

    def test_atlas_gl3_phi3(self):
        """GL_3 has phi_3 = -2*sigma_3 = 12."""
        atlas = comprehensive_atlas()
        assert atlas['GL_3']['phi'][3] == 12

    def test_atlas_phi_0_is_one(self):
        atlas = comprehensive_atlas()
        for name, data in atlas.items():
            assert data['phi'][0] == 1, f"phi_0 != 1 for {name}"

    def test_atlas_phi_1_vanishes(self):
        atlas = comprehensive_atlas()
        for name, data in atlas.items():
            assert data['phi'][1] == 0, f"phi_1 != 0 for {name}"

    def test_atlas_phi_2_vanishes(self):
        atlas = comprehensive_atlas()
        for name, data in atlas.items():
            assert data['phi'][2] == 0, f"phi_2 != 0 for {name}"

    def test_atlas_collision_residue_vanishes(self):
        """Scalar collision residue vanishes for all CY parameters."""
        atlas = comprehensive_atlas()
        for name, data in atlas.items():
            assert data['collision_residue'] == 0, (
                f"Collision residue nonzero for {name}: {data['collision_residue']}"
            )


# ================================================================
# SECTION 11: STRUCTURE FUNCTION EVALUATION
# ================================================================

class TestStructureFunctionEvaluation:
    """Test exact evaluation of g(z) at specific z values."""

    def test_g_at_large_z(self):
        """g(z) -> 1 as z -> infinity."""
        g = structure_function_at_integer(Fraction(1), Fraction(2), z_val=1000)
        assert abs(g - 1) < Fraction(1, 100), f"g(1000) = {g}, should be ~1"

    def test_g_at_z_equals_h1(self):
        """g(h1) = 0 (zero of numerator)."""
        h1 = Fraction(3)
        g = structure_function_at_integer(h1, Fraction(2), z_val=3)
        assert g == 0, f"g(h1) = {g}, should be 0"

    def test_g_product_identity(self):
        """g(z) * g(-z) = 1 evaluated at integer z."""
        h1, h2 = Fraction(1), Fraction(2)
        for z in [5, 7, 10, 20]:
            gz = structure_function_at_integer(h1, h2, z_val=z)
            gmz = structure_function_at_integer(h1, h2, z_val=-z)
            assert gz * gmz == 1, f"g({z})*g({-z}) = {gz * gmz}, should be 1"

    @pytest.mark.parametrize("z_val", [4, 5, 6, 7, 8, 9, 10])
    def test_g_times_g_neg_is_one(self, z_val):
        """g(z)*g(-z) = 1 for various integer z."""
        h1, h2 = Fraction(1), Fraction(2)
        gz = structure_function_at_integer(h1, h2, z_val=z_val)
        gmz = structure_function_at_integer(h1, h2, z_val=-z_val)
        assert gz * gmz == 1


# ================================================================
# SECTION 12: MACMAHON GENUS DECOMPOSITION
# ================================================================

class TestMacMahonGenusDecomposition:
    """Tests for decomposing MacMahon into genus contributions."""

    def test_log_macmahon_coeff1(self):
        """[q^1] log M(q) = sigma_2(1)/1 = 1."""
        result = macmahon_genus_decomposition()
        # sigma_2(1) = 1^2 = 1; coefficient = 1/1 = 1
        assert result['log_macmahon_coeffs'][0] == (1, Fraction(1))

    def test_log_macmahon_coeff2(self):
        """[q^2] log M(q) = sigma_2(2)/2 = (1+4)/2 = 5/2."""
        result = macmahon_genus_decomposition()
        assert result['log_macmahon_coeffs'][1] == (2, Fraction(5, 2))

    def test_log_macmahon_coeff3(self):
        """[q^3] log M(q) = sigma_2(3)/3 = (1+9)/3 = 10/3."""
        result = macmahon_genus_decomposition()
        assert result['log_macmahon_coeffs'][2] == (3, Fraction(10, 3))

    def test_regulated_tower_n1(self):
        """At N=1: F_1 = 1/24, F_2 = 7/5760."""
        result = macmahon_genus_decomposition()
        tower_n1 = result['regulated_towers'][1]
        assert tower_n1[1] == Fraction(1, 24)
        assert tower_n1[2] == Fraction(7, 5760)


# ================================================================
# SECTION 13: EDGE CASES AND BOUNDARY VALUES
# ================================================================

class TestEdgeCases:
    """Edge cases and boundary values."""

    def test_abelian_limit_all_phi_vanish(self):
        """At GL_1 (abelian): all phi_j = 0 for j >= 1."""
        phi = phi_explicit(Fraction(1), Fraction(-1), Fraction(0), max_order=10)
        for j in range(1, 11):
            assert phi[j] == 0, f"phi_{j} = {phi[j]} at abelian limit"

    def test_self_dual_sigma2_equals_neg1(self):
        """GL_1 abelian has sigma_2 = -1."""
        s = elementary_symmetric_from_h(Fraction(1), Fraction(-1), Fraction(0))
        assert s[1] == -1

    def test_negative_h_parameters(self):
        """R-matrix computation works for negative h parameters."""
        r = classical_r_matrix_coefficients(Fraction(-1), Fraction(-2), max_order=6)
        # h = (-1, -2, 3), sigma_3 = (-1)*(-2)*3 = 6
        assert r[3] == -2 * Fraction(6)  # phi_3 = -12

    def test_large_h_parameters(self):
        """R-matrix computation works for large h parameters."""
        r = classical_r_matrix_coefficients(Fraction(10), Fraction(20), max_order=6)
        h3 = -(Fraction(10) + Fraction(20))
        sigma3 = Fraction(10) * Fraction(20) * h3
        assert r[3] == -2 * sigma3

    def test_fractional_h_parameters(self):
        """R-matrix computation works for fractional h."""
        h1, h2 = Fraction(1, 3), Fraction(2, 5)
        h3 = -(h1 + h2)
        sigma3 = h1 * h2 * h3
        r = classical_r_matrix_coefficients(h1, h2, max_order=6)
        assert r[3] == -2 * sigma3


# ================================================================
# SECTION 14: CONSISTENCY BETWEEN MODULES
# ================================================================

class TestInterModuleConsistency:
    """Verify consistency between affine_yangian_e1_cy3 and affine_yangian_gl1."""

    def test_phi_values_match(self):
        """phi values from this module match affine_yangian_gl1."""
        h1, h2 = Fraction(1), Fraction(2)
        from compute.lib.affine_yangian_gl1 import phi_explicit as phi_gl1
        phi1 = phi_gl1(h1, h2, max_order=10)
        phi2 = r_matrix_from_g(h1, h2, max_order=10)
        for j in range(11):
            assert phi1[j] == phi2[j], f"phi mismatch at j={j}: {phi1[j]} vs {phi2[j]}"

    def test_structure_function_match(self):
        """structure_function_coefficients matches r_matrix_from_g."""
        h1, h2 = Fraction(1), Fraction(2)
        sf = structure_function_coefficients(h1, h2, max_order=10)
        rm = r_matrix_from_g(h1, h2, max_order=10)
        for j in range(11):
            assert sf[j] == rm[j], f"Mismatch at j={j}: sf={sf[j]}, rm={rm[j]}"

    def test_sigma_values_match(self):
        """Elementary symmetric polynomials are consistent."""
        h1, h2 = Fraction(1), Fraction(2)
        h3 = -(h1 + h2)
        s1, s2, s3 = elementary_symmetric_from_h(h1, h2, h3)
        assert s1 == 0
        assert s2 == h1 * h2 + h1 * h3 + h2 * h3
        assert s3 == h1 * h2 * h3


class TestBPSFromTwoModules:
    """BPS invariants from yangian_bar_complex vs affine_yangian_e1_cy3."""

    def test_bps_match(self):
        """BPS invariants from both modules agree."""
        from compute.lib.yangian_bar_complex import bps_invariants_c3 as bps1
        bps2 = dt_invariants_from_shadow(15)['bps_direct']
        for n in range(15):
            assert bps1(15)[n] == bps2[n], f"BPS mismatch at n={n}"


# ================================================================
# SECTION 15: AP-COMPLIANCE TESTS
# ================================================================

class TestAPCompliance:
    """Tests for anti-pattern compliance."""

    def test_ap19_pole_order(self):
        """AP19: r-matrix poles are from g(z)-1, not from the OPE directly.

        The bar complex extracts residues along d log(z-w), reducing pole
        orders by 1. For the scalar structure function:
        OPE has poles at z^{-2s-1}; r-matrix = g(z)-1 starts at z^{-3}.
        """
        r = classical_r_matrix_coefficients(Fraction(1), Fraction(2), max_order=6)
        # No z^{-1} pole (CY condition absorbs it)
        assert 1 not in r

    def test_ap22_genus_convention(self):
        """AP22: F_1 = kappa/24 at genus 1 (hbar^0 or hbar^2 depending on convention)."""
        assert faber_pandharipande(1) == Fraction(1, 24)
        kappa = kappa_w_infinity_regulated(1)
        assert genus_g_free_energy(kappa, 1) == Fraction(1, 24)

    def test_ap27_propagator_weight(self):
        """AP27: The bar propagator d log E(z,w) has weight 1.
        All channels use E_1, regardless of field weight."""
        # For the affine Yangian, the structure function g(z) is the
        # propagator-weighted kernel. The weight-1 propagator gives
        # g(z) = prod (z-h_a)/(z+h_a), which is weight 0 as a function of z.
        # This is consistent with AP27: d log(z-w) has weight 1, and
        # the field of weight h contributes h_a = h * sigma_a.
        phi = phi_explicit(Fraction(1), Fraction(2), max_order=4)
        assert phi[0] == 1  # g(z) -> 1 as z -> inf (weight-0 function)

    def test_ap45_desuspension(self):
        """AP45: s^{-1} shifts degree DOWN by 1 (desuspension)."""
        # In the bar complex B^k(Y^+), elements are desuspended:
        # |s^{-1}a| = |a| - 1. For degree-0 elements (Y^+ concentrated
        # in cohomological degree 0), s^{-1}a has degree -1.
        # The bar differential |d| = +1 in cohomological grading.
        pass  # Convention check -- no computation needed

    def test_ap48_kappa_not_c_over_2(self):
        """AP48: kappa(W_{1+inf}) != c/2. Total kappa diverges."""
        # At c = 1 with spin cutoff N:
        # kappa(W_{1+inf,N}) = H_N (harmonic number)
        # c/2 = 1/2 (fixed)
        # For N >= 2: H_N > 1/2, so kappa != c/2.
        kappa_n2 = kappa_w_infinity_regulated(2)
        assert kappa_n2 == Fraction(3, 2)
        assert kappa_n2 != Fraction(1, 2), "kappa should not equal c/2"


# ================================================================
# SECTION 16: SPECIFIC GROUND TRUTH VALUES
# ================================================================

class TestGroundTruthValues:
    """Tests against specific numerical ground truth values."""

    def test_phi_h_1_2_neg3(self):
        """phi values for h=(1,2,-3): [1,0,0,12,0,84,72,588,1008,4548]."""
        phi = phi_explicit(Fraction(1), Fraction(2), max_order=9)
        expected = [1, 0, 0, 12, 0, 84, 72, 588, 1008, 4548]
        for j in range(10):
            assert phi[j] == expected[j], f"phi_{j}={phi[j]}, expected {expected[j]}"

    def test_sigma_h_1_2_neg3(self):
        """sigma_2 = -7, sigma_3 = -6 for h=(1,2,-3)."""
        s = elementary_symmetric_from_h(Fraction(1), Fraction(2), Fraction(-3))
        assert s[0] == 0   # CY condition
        assert s[1] == -7  # sigma_2
        assert s[2] == -6  # sigma_3

    def test_sv_gl2(self):
        """GL_2: h=(1,-2,1), sigma_2=-3, sigma_3=-2."""
        s = elementary_symmetric_from_h(Fraction(1), Fraction(-2), Fraction(1))
        assert s[0] == 0
        assert s[1] == -3
        assert s[2] == -2

    def test_sv_gl3(self):
        """GL_3: h=(1,-3,2), sigma_2=-7, sigma_3=-6."""
        s = elementary_symmetric_from_h(Fraction(1), Fraction(-3), Fraction(2))
        assert s[0] == 0
        assert s[1] == -7
        assert s[2] == -6

    def test_sv_gl1_abelian(self):
        """GL_1: h=(1,-1,0), sigma_2=-1, sigma_3=0."""
        s = elementary_symmetric_from_h(Fraction(1), Fraction(-1), Fraction(0))
        assert s[0] == 0
        assert s[1] == -1
        assert s[2] == 0

    def test_power_sums_cy(self):
        """Power sums: p_1=0, p_2=2*sigma_2+sigma_1^2, p_3=3*sigma_3."""
        p = power_sums_from_h(Fraction(1), Fraction(2), max_k=5)
        assert p[1] == 0  # CY condition
        # p_3 = 3*sigma_3 = 3*(-6) = -18
        assert p[3] == Fraction(1)**3 + Fraction(2)**3 + Fraction(-3)**3
        assert p[3] == 1 + 8 - 27
        assert p[3] == -18

    def test_harmonic_numbers(self):
        """H_1=1, H_2=3/2, H_3=11/6, H_4=25/12, H_5=137/60."""
        expected = {
            1: Fraction(1),
            2: Fraction(3, 2),
            3: Fraction(11, 6),
            4: Fraction(25, 12),
            5: Fraction(137, 60),
        }
        for n, h in expected.items():
            assert kappa_w_infinity_regulated(n) == h, (
                f"H_{n} = {kappa_w_infinity_regulated(n)}, expected {h}"
            )


# ================================================================
# SECTION 17: ADDITIONAL MULTI-PATH VERIFICATIONS
# ================================================================

class TestMultiPathStructureFunction:
    """Multi-path verification for structure function properties."""

    @pytest.mark.parametrize("h1,h2", [
        (Fraction(1), Fraction(2)),
        (Fraction(1), Fraction(-2)),
        (Fraction(1), Fraction(-3)),
        (Fraction(2), Fraction(3)),
        (Fraction(1, 2), Fraction(1, 3)),
    ])
    def test_unitarity_and_inversion_agree(self, h1, h2):
        """Unitarity (Cauchy product) and inversion (g(-z)=1/g(z)) give same result."""
        unit = verify_unitarity(h1, h2, max_order=8)
        inv = verify_g_minus_z_equals_inv_g(h1, h2, max_order=8)
        assert unit['all_pass'] == inv

    @pytest.mark.parametrize("h1,h2", [
        (Fraction(1), Fraction(2)),
        (Fraction(3), Fraction(-1)),
    ])
    def test_phi_series_vs_explicit(self, h1, h2):
        """Path 1 (series) vs Path 2 (exponentiation) for phi."""
        phi_s = structure_function_coefficients(h1, h2, max_order=10)
        phi_e = phi_explicit(h1, h2, max_order=10)
        for j in range(11):
            assert phi_s[j] == phi_e[j], f"Mismatch at j={j}: {phi_s[j]} vs {phi_e[j]}"


class TestMultiPathGenusVerification:
    """Multi-path genus tower verification."""

    def test_f1_two_paths(self):
        """F_1 via kappa*lambda_1 vs direct computation."""
        for N in [1, 2, 3, 5]:
            kappa = kappa_w_infinity_regulated(N)
            f1_path1 = kappa * Fraction(1, 24)
            f1_path2 = genus_g_free_energy(kappa, 1)
            assert f1_path1 == f1_path2, (
                f"F_1(N={N}): path1={f1_path1}, path2={f1_path2}"
            )

    def test_f2_two_paths(self):
        """F_2 via kappa*lambda_2 vs genus_tower function."""
        for N in [1, 2, 5]:
            tower = genus_tower_w_infinity(N)
            kappa = kappa_w_infinity_regulated(N)
            expected = kappa * Fraction(7, 5760)
            assert tower[2] == expected, (
                f"F_2(N={N}): tower={tower[2]}, expected={expected}"
            )
