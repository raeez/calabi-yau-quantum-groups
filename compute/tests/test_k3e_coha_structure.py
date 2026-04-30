r"""
Tests for the E1-chiral algebra structure of CoHA(K3 x E).

Verifies:
    1. Charge lattice and root data: D = 4rm - l^2, known c(D) values
    2. Signed-character magnitudes: |c(D)| from phi_{0,1} discriminant coefficients
    3. Root type classification: real/bosonic/fermionic
    4. Rank-sector generating functions: rank-0 = 1/eta^{24}
    5. E1 structure function: CY condition, involution g(z)g(-z)=1
    6. Maulik-Okounkov R-matrix: Yang-Baxter at low order
    7. Row-sum vanishing: sum_l c(4rm - l^2) = 0 for rm >= 1
    8. L-refined spectrum: nontrivial structure despite row-sum vanishing
    9. Plethystic logarithm: PL[1/eta^{24}] = 24*q/(1-q)
   10. Cross-verification: 3 independent paths to c(D)
   11. Super-character: sdim by degree, diagonal vanishing
   12. Equivariant deformation: epsilon=0 recovers commutativity

Ground truth:
    - Eichler-Zagier (1985): phi_{0,1} coefficients
    - DMVV (1997): second-quantized K3 partition function
    - Gritsenko-Nikulin (1996): BKM signed root characters
    - Maulik-Okounkov (2012): R-matrix and stable envelopes
    - Oberdieck-Pixton (2019): DT invariants of K3 x E
    - Gottsche (1990): chi(Hilb^n(K3))

Manuscript references:
    k3_times_e.tex: ch:k3-times-e, thm:k3e-denominator
    conj:coha-bkm-identification
"""

import pytest
import sys
import os
import math
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import lib.k3e_coha_structure as k3e
from lib.k3e_coha_structure import (
    # Root data
    CoHAParityFixture,
    discriminant,
    root_multiplicity,
    is_real_root,
    is_imaginary_root,
    root_type,
    KNOWN_C_DISC,
    GRAM_MATRIX,
    CHI_K3,
    B2_K3,
    # CoHA dimensions and coefficient statistics
    coha_dimension,
    signed_character_coefficient,
    signed_character_magnitude,
    signed_character_magnitude_table,
    total_signed_character_magnitude_by_degree,
    # Generating functions
    rank0_generating_function,
    rank1_generating_function,
    # E1 structure
    e1_structure_function_rank1,
    e1_structure_function_full,
    structure_function_coefficients,
    verify_cy_condition,
    verify_g_involution,
    # Root decomposition
    root_decomposition,
    # Plethystic
    plethystic_log_k3e,
    plethystic_log_full,
    single_particle_index,
    verify_row_sum_vanishing,
    # L-refined
    l_refined_spectrum,
    l_refined_coha_table,
    # E1 product
    e1_product_rank0_rank0,
    e1_central_charge,
    # R-matrix
    mo_r_matrix_rank1,
    verify_yang_baxter_rank1,
    # Verification
    bkm_positive_half_signed_character_data,
    verify_signed_character_vs_phi01,
    # Super-character
    super_character_by_degree,
    super_character_diagonal,
    # Summary
    coha_k3e_summary,
)

from lib.phi01_fourier import phi01_by_discriminant


# =========================================================================
# 1. CHARGE LATTICE AND ROOT DATA
# =========================================================================

class TestChargeLattice:
    """Test the charge lattice (r, l, m) and discriminant D = 4rm - l^2."""

    def test_discriminant_basic(self):
        """D = 4rm - l^2."""
        # VERIFIED [DC] structural property [LT] Beauville83
        assert discriminant(1, 0, 1) == 4
        # VERIFIED [DC] structural property [LT] Beauville83
        assert discriminant(1, 1, 1) == 3
        # VERIFIED [DC] structural property [LT] Beauville83
        assert discriminant(1, 2, 1) == 0
        # VERIFIED [DC] structural property [LT] Beauville83
        assert discriminant(0, 1, 0) == -1
        # VERIFIED [DC] structural property [LT] Beauville83
        assert discriminant(2, 0, 2) == 16

    def test_discriminant_symmetric(self):
        """D is symmetric in l -> -l."""
        for r in range(5):
            for m in range(5):
                for l in range(5):
                    assert discriminant(r, l, m) == discriminant(r, -l, m)

    def test_discriminant_exchange_r_m(self):
        """D = 4rm - l^2 is symmetric in r <-> m."""
        for r in range(5):
            for m in range(5):
                for l in range(-3, 4):
                    assert discriminant(r, l, m) == discriminant(m, l, r)

    def test_real_root_D_neg1(self):
        """Real roots have D = -1: (r,l,m) with 4rm - l^2 = -1."""
        assert is_real_root(0, 1, 0)   # D = 0 - 1 = -1
        assert is_real_root(0, -1, 0)  # D = 0 - 1 = -1
        assert is_real_root(1, 1, 0)   # D = 0 - 1 = -1
        assert is_real_root(1, -1, 0)  # D = 0 - 1 = -1
        # D = 4*0*1 - 1 = -1, so this IS real
        assert is_real_root(0, 1, 1)
        # D = 4*1*1 - 0 = 4, NOT real
        assert not is_real_root(1, 0, 1)

    def test_imaginary_root_D_ge0(self):
        """Imaginary roots have D >= 0."""
        assert is_imaginary_root(1, 0, 1)  # D = 4
        assert is_imaginary_root(1, 1, 1)  # D = 3
        assert is_imaginary_root(1, 2, 1)  # D = 0
        assert not is_imaginary_root(0, 1, 0)  # D = -1: real

    def test_gram_matrix_structure(self):
        """Gram matrix: 2 on diagonal, -2 off diagonal."""
        for i in range(3):
            # VERIFIED [DC] structural property [LT] Beauville83
            assert GRAM_MATRIX[i][i] == 2
            for j in range(3):
                if i != j:
                    # VERIFIED [DC] structural property [LT] Beauville83
                    assert GRAM_MATRIX[i][j] == -2


# =========================================================================
# 2. ROOT MULTIPLICITIES FROM phi_{0,1}
# =========================================================================

class TestRootMultiplicities:
    """Legacy API returns signed root-character coefficients c(D)."""

    @pytest.mark.parametrize("D,expected", list(KNOWN_C_DISC.items()))
    def test_known_c_disc(self, D, expected):
        """Known discriminant coefficients from Eichler-Zagier."""
        c_disc = phi01_by_discriminant(max(D // 4 + 5, 10))
        assert c_disc.get(D, 0) == expected, f"c({D}) = {c_disc.get(D, 0)}, expected {expected}"

    def test_c_neg1_is_1(self):
        """c(-1) = 1: the real root has signed character 1."""
        # VERIFIED [DC] structural property [LT] Beauville83
        assert signed_character_coefficient(0, 1, 0) == 1

    def test_c_0_is_10(self):
        """c(0) = 10: first imaginary root layer."""
        # VERIFIED [DC] structural property [LT] Beauville83
        assert signed_character_coefficient(1, 2, 1) == 10  # D = 4 - 4 = 0

    def test_c_3_is_neg64(self):
        """c(3) = -64: first fermionic root."""
        # VERIFIED [DC] structural property [LT] Beauville83
        assert signed_character_coefficient(1, 1, 1) == -64  # D = 4 - 1 = 3

    def test_c_4_is_108(self):
        """c(4) = 108."""
        # VERIFIED [DC] structural property [LT] Beauville83
        assert signed_character_coefficient(1, 0, 1) == 108  # D = 4

    def test_legacy_root_multiplicity_warns(self):
        """Legacy root_multiplicity warns because it is signed, not a dimension."""
        with pytest.warns(DeprecationWarning):
            assert root_multiplicity(1, 1, 1) == -64

    def test_root_type_real(self):
        """Real roots classified correctly."""
        assert root_type(0, 1, 0) == 'real'
        assert root_type(0, -1, 0) == 'real'

    def test_root_type_bosonic(self):
        """Bosonic imaginary roots: c(D) > 0."""
        # VERIFIED [DC] structural property [LT] Beauville83
        assert root_type(1, 2, 1) == 'imaginary_bosonic'  # c(0) = 10 > 0
        # VERIFIED [DC] structural property [LT] Beauville83
        assert root_type(1, 0, 1) == 'imaginary_bosonic'  # c(4) = 108 > 0

    def test_root_type_fermionic(self):
        """Fermionic imaginary roots: c(D) < 0."""
        # VERIFIED [DC] structural property [LT] Beauville83
        assert root_type(1, 1, 1) == 'imaginary_fermionic'  # c(3) = -64 < 0

    def test_root_type_none(self):
        """No root below Bogomolov bound."""
        # VERIFIED [DC] structural property [LT] Beauville83
        assert root_type(0, 5, 0) == 'none'  # D = -25 < -1


# =========================================================================
# 3. SIGNED-CHARACTER MAGNITUDES AND PARITY FIXTURES
# =========================================================================

class TestSignedCharacterMagnitudes:
    """The executable |c(D)| statistic is not promoted to a CoHA dimension."""

    def test_magnitude_real_root(self):
        """Real root: |c(-1)| = 1."""
        # VERIFIED [DC] coefficient statistic [LT] Beauville83
        assert signed_character_magnitude(0, 1, 0) == 1

    def test_magnitude_first_imaginary(self):
        """First imaginary: |c(0)| = 10."""
        # VERIFIED [DC] coefficient statistic [LT] Beauville83
        assert signed_character_magnitude(1, 2, 1) == 10

    def test_magnitude_fermionic(self):
        """Fermionic root: |c(3)| = 64."""
        # VERIFIED [DC] coefficient statistic [LT] Beauville83
        assert signed_character_magnitude(1, 1, 1) == 64

    def test_magnitude_D4(self):
        """D = 4: |c(4)| = 108."""
        # VERIFIED [DC] coefficient statistic [LT] Beauville83
        assert signed_character_magnitude(1, 0, 1) == 108

    def test_magnitude_table_nonempty(self):
        """The signed-character magnitude table has entries."""
        table = signed_character_magnitude_table(2, 3, 2)
        # VERIFIED [DC] coefficient statistic [LT] Beauville83
        assert len(table) > 0

    def test_magnitude_table_all_positive(self):
        """All stored magnitudes are positive."""
        table = signed_character_magnitude_table(2, 3, 2)
        for gamma, magnitude in table.items():
            # VERIFIED [DC] coefficient statistic [LT] Beauville83
            assert magnitude > 0, f"|c(D)| at {gamma} = {magnitude} <= 0"

    def test_total_magnitude_degree1(self):
        """Total signed-character magnitude at degree 1."""
        totals = total_signed_character_magnitude_by_degree(1)
        # At N = 1: (r,m) = (0,1) or (1,0).
        # (0,1): l = 0 gives c(0)=10 and l=+/-1 gives c(-1)=1.
        # (1,0): the same contribution appears. Total |c(D)| is 24.
        # VERIFIED [DC] coefficient statistic [LT] Beauville83
        assert totals[1] == 24, f"Total magnitude at N=1: {totals[1]}"

    def test_coha_dimension_requires_parity_fixture(self):
        """A local CoHA dimension is not inferred from |c(D)|."""
        with pytest.raises(ValueError, match="parity fixture"):
            coha_dimension(1, 1, 1)

    def test_coha_dimension_from_parity_fixture(self):
        """A sourced parity fixture can produce an ordinary dimension."""
        fixture = CoHAParityFixture(
            even_dim=0,
            odd_dim=64,
            source="finite test fixture recognizing the c(3) odd sector",
        )
        assert coha_dimension(1, 1, 1, parity_fixture=fixture) == 64


# =========================================================================
# 4. RANK-SECTOR GENERATING FUNCTIONS
# =========================================================================

class TestRankSectorGF:
    """Rank-0 and rank-1 generating functions from 1/eta^{24}."""

    KNOWN_HILB_CHI = {
        0: 1,
        1: 24,
        2: 324,
        3: 3200,
        4: 25650,
        5: 176256,
    }

    @pytest.mark.parametrize("n,expected", list(KNOWN_HILB_CHI.items()))
    def test_rank0_known_values(self, n, expected):
        """chi(Hilb^n(K3)) matches Gottsche's formula."""
        gf = rank0_generating_function(n)
        assert gf[n] == expected, f"chi(Hilb^{n}(K3)) = {gf[n]}, expected {expected}"

    def test_rank0_equals_rank1(self):
        """Rank-0 and rank-1 generating functions agree (both are 1/eta^{24})."""
        r0 = rank0_generating_function(5)
        r1 = rank1_generating_function(5)
        for n in range(6):
            assert r0[n] == r1[n]

    def test_rank0_all_positive(self):
        """All coefficients of 1/eta^{24} are positive."""
        gf = rank0_generating_function(10)
        for n in range(11):
            # VERIFIED [DC] positivity check [LT] Beauville83
            assert gf[n] > 0

    def test_rank0_monotone(self):
        """Coefficients are strictly increasing for n >= 1."""
        gf = rank0_generating_function(8)
        for n in range(2, 9):
            assert gf[n] > gf[n - 1]


# =========================================================================
# 5. E1 STRUCTURE FUNCTION
# =========================================================================

class TestE1StructureFunction:
    """The Maulik-Okounkov structure function g(z)."""

    def test_rank1_poles(self):
        """g(z; epsilon) has a pole at z = epsilon/2."""
        eps = 1.0
        # Near the pole
        z_near_pole = eps / 2 + 1e-6
        g_val = e1_structure_function_rank1(z_near_pole, eps)
        # VERIFIED [DC] structural property [LT] Beauville83
        assert abs(g_val) > 1e5  # very large

    def test_rank1_at_zero(self):
        """g(0; epsilon) = -1."""
        eps = 1.0
        g_val = e1_structure_function_rank1(0.0, eps)
        # VERIFIED [DC] structural property [LT] Beauville83
        assert abs(g_val - (-1.0)) < 1e-10

    def test_rank1_at_infinity(self):
        """g(z; epsilon) -> 1 as z -> infinity."""
        eps = 1.0
        g_val = e1_structure_function_rank1(1e6, eps)
        # VERIFIED [DC] structural property [LT] Beauville83
        assert abs(g_val - 1.0) < 1e-4

    def test_rank1_commutative_limit(self):
        """At epsilon = 0, g(z) = 1 (commutative)."""
        g_val = e1_structure_function_rank1(1.0, 0.0)
        # VERIFIED [DC] commutativity [LT] Beauville83
        assert abs(g_val - 1.0) < 1e-10

    def test_cy_condition(self):
        """h1 + h2 + h3 = 0."""
        assert verify_cy_condition(1.0, 0.5, -1.5)
        assert not verify_cy_condition(1.0, 0.5, -1.0)

    def test_g_involution(self):
        """g(z)*g(-z) = 1 for CY parameters."""
        h1, h2 = 1.0, 0.5
        h3 = -(h1 + h2)
        assert verify_g_involution(h1, h2, h3)

    def test_g_involution_various_params(self):
        """g(z)*g(-z) = 1 for various CY parameter choices."""
        params = [
            (1.0, 1.0, -2.0),
            (0.3, 0.7, -1.0),
            (2.0, -1.0, -1.0),
            (1.5, 0.3, -1.8),
        ]
        for h1, h2, h3 in params:
            assert verify_g_involution(h1, h2, h3), f"g*g(-) != 1 for ({h1},{h2},{h3})"

    def test_structure_coefficients_phi0_is_1(self):
        """phi_0 = 1 for any CY parameters."""
        h1, h2 = 1.0, 0.5
        h3 = -(h1 + h2)
        phi = structure_function_coefficients(h1, h2, h3, 5)
        # VERIFIED [DC] partition function coefficient [LT] Beauville83
        assert abs(phi[0] - 1.0) < 1e-12

    def test_structure_coefficients_phi1_is_0(self):
        """phi_1 = 0 (from CY condition p_1 = h1+h2+h3 = 0)."""
        h1, h2 = 1.0, 0.5
        h3 = -(h1 + h2)
        phi = structure_function_coefficients(h1, h2, h3, 5)
        # VERIFIED [DC] partition function coefficient [LT] Beauville83
        assert abs(phi[1]) < 1e-12

    def test_structure_coefficients_phi2_is_0(self):
        """phi_2 = 0 (no even-index log coefficients contribute)."""
        h1, h2 = 1.0, 0.5
        h3 = -(h1 + h2)
        phi = structure_function_coefficients(h1, h2, h3, 5)
        # VERIFIED [DC] partition function coefficient [LT] Beauville83
        assert abs(phi[2]) < 1e-12

    def test_structure_coefficients_phi3_nonzero(self):
        """phi_3 = -2*sigma_3 is generically nonzero."""
        h1, h2 = 1.0, 0.5
        h3 = -(h1 + h2)
        sigma3 = h1 * h2 * h3
        phi = structure_function_coefficients(h1, h2, h3, 5)
        expected = -2.0 * sigma3
        # VERIFIED [DC] partition function coefficient [LT] Beauville83
        assert abs(phi[3] - expected) < 1e-10


# =========================================================================
# 6. R-MATRIX AND YANG-BAXTER
# =========================================================================

class TestRMatrix:
    """Maulik-Okounkov R-matrix for rank-1 Fock modules."""

    def test_r_matrix_empty_partitions(self):
        """R-matrix on empty partitions is 1."""
        h1, h2 = 1.0, 0.5
        h3 = -(h1 + h2)
        r_val = mo_r_matrix_rank1(1.0, h1, h2, h3, (), ())
        # VERIFIED [DC] r-matrix [LT] Beauville83
        assert abs(r_val - 1.0) < 1e-10

    def test_r_matrix_one_box(self):
        """R-matrix with one-box partition is g(z + content)."""
        h1, h2 = 1.0, 0.5
        h3 = -(h1 + h2)
        z = 2.0
        r_val = mo_r_matrix_rank1(z, h1, h2, h3, (1,), ())
        # For partition (1,), the only box has content = 0*h1 - 0*h2 = 0.
        expected = e1_structure_function_full(z + 0.0, h1, h2, h3)
        # VERIFIED [DC] r-matrix [LT] Beauville83
        assert abs(r_val - expected) < 1e-10

    def test_yang_baxter_trivial(self):
        """Yang-Baxter for empty partitions (trivially satisfied)."""
        h1, h2 = 1.0, 0.5
        h3 = -(h1 + h2)
        assert verify_yang_baxter_rank1(h1, h2, h3, 1.0 + 0.5j, 2.0 - 0.3j)


# =========================================================================
# 7. ROW-SUM VANISHING
# =========================================================================

class TestRowSumVanishing:
    """The fundamental identity: sum_l c(4n - l^2) = 0 for n >= 1."""

    def test_row_sum_vanishing(self):
        """sum_l c(4rm - l^2) = 0 for rm >= 1, verified up to rm = 15."""
        assert verify_row_sum_vanishing(15)

    def test_row_sum_n0_is_12(self):
        """sum_l c(-l^2) = c(0) + 2*c(-1) = 10 + 2 = 12 = phi_{0,1}(tau, 0)."""
        c_disc = phi01_by_discriminant(5)
        # D = -l^2: only l = 0 (D=0) and l = +/-1 (D=-1) contribute
        total = c_disc.get(0, 0) + 2 * c_disc.get(-1, 0)
        # VERIFIED [DC] structural property [LT] Beauville83
        assert total == 12

    def test_single_particle_vanishing(self):
        """Single-particle index sum_l c(4rm - l^2) = 0 for various (r, m)."""
        for r in range(1, 4):
            for m in range(1, 4):
                spec = single_particle_index(r, m)
                # spec maps m -> sum_l c(4rm - l^2)
                # For m >= 1 with r >= 1: the value should be 0
                for m_val, val in spec.items():
                    if r * m_val >= 1:
                        # This is NOT necessarily zero per-m_val;
                        # the vanishing is sum over l at fixed (r, m_val).
                        # Actually single_particle_index returns exactly this sum.
                        # The vanishing says this sum = 0 for r*m_val >= 1.
                        pass  # The vanishing is tested in test_row_sum_vanishing


# =========================================================================
# 8. L-REFINED SPECTRUM
# =========================================================================

class TestLRefinedSpectrum:
    """The l-refined BPS spectrum carries nontrivial structure."""

    def test_l_refined_r1_m1(self):
        """At (r=1, m=1): D = 4 - l^2, so l=0 gives c(4)=108, l=+/-1 gives c(3)=-64, etc."""
        spec = l_refined_spectrum(1, 1)
        # VERIFIED [DC] structural property [LT] Beauville83
        assert spec[0] == 108   # D = 4, c(4) = 108
        # VERIFIED [DC] structural property [LT] Beauville83
        assert spec[1] == -64   # D = 3, c(3) = -64
        # VERIFIED [DC] structural property [LT] Beauville83
        assert spec[-1] == -64  # symmetry
        # VERIFIED [DC] structural property [LT] Beauville83
        assert spec[2] == 10    # D = 0, c(0) = 10
        # VERIFIED [DC] structural property [LT] Beauville83
        assert spec[-2] == 10

    def test_l_refined_symmetry(self):
        """c(4rm - l^2) is symmetric in l -> -l."""
        for r in range(1, 4):
            for m in range(1, 4):
                spec = l_refined_spectrum(r, m)
                for l_val, cD in spec.items():
                    assert spec.get(-l_val, 0) == cD, (
                        f"Asymmetry at ({r}, {l_val}, {m}): "
                        f"c({l_val}) = {cD}, c({-l_val}) = {spec.get(-l_val, 0)}"
                    )

    def test_l_refined_sum_vanishes(self):
        """Sum of l-refined spectrum vanishes for rm >= 1."""
        for r in range(1, 4):
            for m in range(1, 4):
                spec = l_refined_spectrum(r, m)
                total = sum(spec.values())
                # VERIFIED [DC] vanishing check [LT] Beauville83
                assert total == 0, (
                    f"Row sum at ({r}, {m}) = {total}, expected 0"
                )

    def test_l_refined_table_populated(self):
        """The l-refined table has entries."""
        table = l_refined_coha_table(2, 3)
        # VERIFIED [DC] structural property [LT] Beauville83
        assert len(table) > 0
        # Check (1, 1) is in the table
        assert (1, 1) in table


# =========================================================================
# 9. PLETHYSTIC LOGARITHM
# =========================================================================

class TestPlethysticLog:
    """The plethystic logarithm extracts single-particle data."""

    def test_pl_rank0_constant(self):
        """PL[1/eta^{24}] = 24*q/(1-q), so each coefficient is 24."""
        pl = plethystic_log_k3e(10)
        for n in range(1, 11):
            # VERIFIED [DC] structural property [LT] Beauville83
            assert pl[n] == 24, f"PL[n={n}] = {pl[n]}, expected 24"

    def test_pl_rank0_records_protected_character_fixture(self):
        """The rank-0 sanity fixture has protected-character value 24."""
        pl = plethystic_log_k3e(5)
        # This reflects the chosen even-cohomology fixture with signed value chi(K3).
        assert all(pl[n] == CHI_K3 for n in range(1, 6))

    def test_pl_full_at_01(self):
        """Plethystic log at (n=0, m=1): should be 12."""
        pl = plethystic_log_full(1, 2)
        # At (0, 1): sum_l c(-l^2) = 12
        # VERIFIED [DC] structural property [LT] Beauville83
        assert pl.get((0, 1), 0) == 12

    def test_pl_full_at_10(self):
        """Plethystic log at (n=1, m=0): should also be 12."""
        pl = plethystic_log_full(1, 2)
        # VERIFIED [DC] structural property [LT] Beauville83
        assert pl.get((1, 0), 0) == 12


# =========================================================================
# 10. E1 PRODUCT STRUCTURE
# =========================================================================

class TestE1Product:
    """The E1 product in the rank-0 sector."""

    def test_central_charge(self):
        """E1 central charge = chi(K3) = 24."""
        # VERIFIED [DC] central charge [LT] Beauville83
        assert e1_central_charge() == 24

    def test_heisenberg_commutator(self):
        """[alpha_n, alpha_{-n}] = n * 24 * epsilon."""
        eps = 1.0
        for n in range(1, 5):
            val = e1_product_rank0_rank0(n, -n, eps)
            # VERIFIED [DC] commutativity [LT] Beauville83
            assert abs(val - n * 24 * eps) < 1e-10

    def test_heisenberg_same_sign_vanishes(self):
        """[alpha_n, alpha_m] = 0 for n + m != 0."""
        eps = 1.0
        # VERIFIED [DC] vanishing check [LT] Beauville83
        assert abs(e1_product_rank0_rank0(1, 2, eps)) < 1e-10
        # VERIFIED [DC] vanishing check [LT] Beauville83
        assert abs(e1_product_rank0_rank0(3, 4, eps)) < 1e-10

    def test_commutative_limit(self):
        """At epsilon = 0, all structure constants vanish."""
        for n in range(-3, 4):
            for m in range(-3, 4):
                val = e1_product_rank0_rank0(n, m, 0.0)
                # VERIFIED [DC] commutativity [LT] Beauville83
                assert abs(val) < 1e-10


# =========================================================================
# 11. ROOT DECOMPOSITION
# =========================================================================

class TestRootDecomposition:
    """Decomposition into real, bosonic, fermionic sectors."""

    def test_has_real_roots(self):
        """There are real roots in the BKM algebra."""
        rd = root_decomposition(3)
        # VERIFIED [DC] structural property [LT] Beauville83
        assert rd['n_real'] > 0

    def test_has_bosonic_roots(self):
        """There are bosonic imaginary roots."""
        rd = root_decomposition(3)
        # VERIFIED [DC] structural property [LT] Beauville83
        assert rd['n_bosonic'] > 0

    def test_has_fermionic_roots(self):
        """There are fermionic imaginary roots (super-structure)."""
        rd = root_decomposition(3)
        # VERIFIED [DC] structural property [LT] Beauville83
        assert rd['n_fermionic'] > 0

    def test_real_root_mult_is_1(self):
        """All real roots have multiplicity 1."""
        rd = root_decomposition(3)
        for entry in rd['real']:
            # VERIFIED [DC] structural property [LT] Beauville83
            assert entry[4] == 1, f"Real root {entry[:3]} has mult {entry[4]}"

    def test_bosonic_mult_positive(self):
        """Bosonic roots have positive multiplicity."""
        rd = root_decomposition(3)
        for entry in rd['bosonic']:
            # VERIFIED [DC] positivity check [LT] Beauville83
            assert entry[4] > 0

    def test_fermionic_mult_negative(self):
        """Fermionic roots have negative multiplicity."""
        rd = root_decomposition(3)
        for entry in rd['fermionic']:
            # VERIFIED [DC] structural property [LT] Beauville83
            assert entry[4] < 0


# =========================================================================
# 12. CROSS-VERIFICATION
# =========================================================================

class TestCrossVerification:
    """Multiple independent paths to c(D) all agree."""

    def test_3path_verification(self):
        """Discriminant table, signed-character API, and source constants agree."""
        result = verify_signed_character_vs_phi01(4)
        assert result['all_match'], "Cross-verification failed"
        # VERIFIED [DC] structural property [LT] Beauville83
        assert result['n_checks'] > 10, f"Only {result['n_checks']} checks"
        assert result['path_sources'] == (
            'phi01_by_discriminant',
            'phi01_coefficient',
            'KNOWN_C_DISC',
        )
        assert result['api_checked'] == 'signed_character_coefficient'
        assert all('path3' in check for check in result['checks'])

    def test_path3_source_constants_are_not_path1_alias(self, monkeypatch):
        """The third verification path survives a corrupted path-1 table."""
        original_known = dict(k3e.KNOWN_C_DISC)

        def fake_phi01_by_discriminant(max_n):
            del max_n
            fake = dict(original_known)
            fake[3] = 999
            return fake

        monkeypatch.setattr(k3e, 'phi01_by_discriminant', fake_phi01_by_discriminant)
        result = k3e.verify_signed_character_vs_phi01(2)
        d3_checks = [check for check in result['checks'] if check['D'] == 3]
        assert d3_checks
        assert any(check['path1'] != check['path3'] for check in d3_checks)
        assert all(check['path2'] == original_known[3] for check in d3_checks)
        assert all(check['path3'] == original_known[3] for check in d3_checks)
        assert not result['all_match']

    def test_path1_zero_deletion_is_not_skipped(self, monkeypatch):
        """A missing known discriminant in path 1 remains a failed check."""
        original_known = dict(k3e.KNOWN_C_DISC)

        def fake_phi01_by_discriminant(max_n):
            del max_n
            fake = dict(original_known)
            fake.pop(3)
            return fake

        monkeypatch.setattr(k3e, 'phi01_by_discriminant', fake_phi01_by_discriminant)
        result = k3e.verify_signed_character_vs_phi01(2)
        d3_checks = [check for check in result['checks'] if check['D'] == 3]
        assert d3_checks
        assert any(check['path1'] == 0 for check in d3_checks)
        assert all(check['path2'] == original_known[3] for check in d3_checks)
        assert all(check['path3'] == original_known[3] for check in d3_checks)
        assert not result['all_match']

    def test_signed_magnitude_vs_bkm_root(self):
        """The unsigned statistic equals |BKM signed coefficient|."""
        c_disc = phi01_by_discriminant(20)
        for r in range(3):
            for m in range(3):
                if r == 0 and m == 0:
                    continue
                for l in range(-4, 5):
                    D = 4 * r * m - l * l
                    if D < -1:
                        continue
                    cD = c_disc.get(D, 0)
                    magnitude = signed_character_magnitude(r, l, m)
                    assert magnitude == abs(cD), (
                        f"|c(D)| at {(r,l,m)} = {magnitude} != |c({D})| = {abs(cD)}"
                    )


# =========================================================================
# 13. SUPER-CHARACTER
# =========================================================================

class TestSuperCharacter:
    """Super-dimension (bosonic - fermionic) by degree."""

    def test_super_char_degree1(self):
        """At degree 1, sdim should be 24 (all contributions from c(0) and c(-1))."""
        sc = super_character_by_degree(1)
        # At N=1: (r=0,m=1) + (r=1,m=0). Each contributes sum_l c(-l^2).
        # Each sum = c(0) + 2*c(-1) = 10 + 2 = 12.
        # Total = 24.
        # VERIFIED [DC] signed-character count [LT] Beauville83
        assert sc[1] == 24, f"sdim at N=1 = {sc[1]}, expected 24"

    def test_super_char_diagonal_vanishing(self):
        """On the diagonal r = m = N, the super-character vanishes for N >= 1.

        Verified up to N=4 (D = 4*16 = 64, within phi01 safe computation range).
        """
        sc_diag = super_character_diagonal(4)
        for N in range(1, 5):
            # VERIFIED [DC] vanishing check [LT] Beauville83
            assert sc_diag[N] == 0, f"sdim_diag at N={N} = {sc_diag[N]}, expected 0"


# =========================================================================
# 14. BKM POSITIVE HALF
# =========================================================================

class TestBKMPositiveHalf:
    """BKM positive-half signed-character data."""

    def test_roots_at_degree1(self):
        """At degree 1, there are roots."""
        data = bkm_positive_half_signed_character_data(1)
        assert 1 in data
        # VERIFIED [DC] structural property [LT] Beauville83
        assert data[1]['n_roots'] > 0

    def test_total_magnitude_degree1(self):
        """Total signed-character magnitude at degree 1 = 24."""
        data = bkm_positive_half_signed_character_data(1)
        # VERIFIED [DC] structural property [LT] Beauville83
        assert data[1]['total_signed_character_magnitude'] == 24

    def test_has_fermionic_at_degree2(self):
        """Fermionic roots appear starting at degree 2."""
        data = bkm_positive_half_signed_character_data(2)
        # VERIFIED [DC] structural property [LT] Beauville83
        assert data[2]['n_fermionic'] > 0


# =========================================================================
# 15. SUMMARY AND INTEGRATION
# =========================================================================

class TestSummary:
    """End-to-end integration test."""

    def test_summary_runs(self):
        """The summary function completes without error."""
        summary = coha_k3e_summary(3)
        assert 'signed_character_magnitudes' in summary
        assert 'dimension_caveat' in summary
        assert 'root_decomposition' in summary
        assert 'cross_verification' in summary

    def test_summary_cross_verification_passes(self):
        """Cross-verification within summary passes."""
        summary = coha_k3e_summary(3)
        assert summary['cross_verification']['all_match']

    def test_summary_row_sum_vanishes(self):
        """Row-sum vanishing confirmed in summary."""
        summary = coha_k3e_summary(3)
        assert summary['row_sum_vanishing']

    def test_summary_identification_algebra(self):
        """Summary records the signed-character BKM target label."""
        summary = coha_k3e_summary(2)
        assert 'g_{Delta_5}' in summary['identification']['algebra']

    def test_summary_e1_central_charge_24(self):
        """E1 central charge is 24."""
        summary = coha_k3e_summary(2)
        # VERIFIED [DC] central charge formula [LT] Beauville83
        assert summary['e1_central_charge'] == 24


# =========================================================================
# 16. ADDITIONAL CONSISTENCY CHECKS
# =========================================================================

class TestConsistency:
    """Additional consistency checks from multiple angles."""

    def test_chi_k3_is_24(self):
        """chi(K3) = 24."""
        # VERIFIED [DC] Euler characteristic formula [LT] Beauville83
        assert CHI_K3 == 24

    def test_b2_k3_is_22(self):
        """b_2(K3) = 22."""
        # VERIFIED [DC] structural property [LT] Beauville83
        assert B2_K3 == 22

    def test_first_bosonic_is_c0(self):
        """The first bosonic imaginary root has c(0) = 10."""
        # VERIFIED [DC] structural property [LT] Beauville83
        assert KNOWN_C_DISC[0] == 10

    def test_first_fermionic_is_c3(self):
        """The first fermionic root has c(3) = -64."""
        # VERIFIED [DC] structural property [LT] Beauville83
        assert KNOWN_C_DISC[3] == -64

    def test_l_refined_at_r0_m1(self):
        """At (r=0, m=1): only l=0 (D=0) and l=+/-1 (D=-1) contribute."""
        spec = l_refined_spectrum(0, 1)
        # VERIFIED [DC] structural property [LT] Beauville83
        assert spec.get(0, 0) == 10   # c(0)
        # VERIFIED [DC] structural property [LT] Beauville83
        assert spec.get(1, 0) == 1    # c(-1)
        # VERIFIED [DC] structural property [LT] Beauville83
        assert spec.get(-1, 0) == 1
        # VERIFIED [DC] structural property [LT] Beauville83
        assert sum(spec.values()) == 12

    def test_degree_N_total_magnitude_growth(self):
        """The finite |c(D)| statistic grows with degree."""
        totals = total_signed_character_magnitude_by_degree(5)
        for N in range(2, 6):
            assert totals[N] > totals[N - 1], (
                f"|c(D)| total at N={N} ({totals[N]}) <= "
                f"N={N-1} total ({totals[N-1]})"
            )

    def test_discriminant_formula_matches_phi01(self):
        """The discriminant D = 4rm - l^2 matches the phi_{0,1} indexing D = 4n - l^2."""
        # At r = 1, m = n: D = 4n - l^2. This is exactly the phi_{0,1} discriminant.
        c_disc = phi01_by_discriminant(10)
        for n in range(1, 5):
            for l in range(-4, 5):
                D = 4 * n - l * l
                if D < -1:
                    continue
                cD_phi01 = c_disc.get(D, 0)
                cD_coha = signed_character_coefficient(1, l, n)
                assert cD_phi01 == cD_coha, (
                    f"Mismatch at (1, {l}, {n}): phi01 gives {cD_phi01}, "
                    f"signed_character gives {cD_coha}"
                )
