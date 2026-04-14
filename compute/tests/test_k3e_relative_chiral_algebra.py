r"""
Tests for K3 x E relative chiral algebra via fiberwise Phi_2.

Verifies:
    1. Fiber data: Phi_2(D^b(Coh(K3))) = V_{tilde{Lambda}_{K3}}
    2. Base data: elliptic curve E
    3. Relative chiral algebra A_{K3xE/E}
    4. Factorization homology character (rank-0 sector)
    5. Kappa spectrum accessible from relative construction
    6. BKM positive part: root multiplicities from phi_{0,1}
    7. Total root multiplicity = 24 at each level
    8. Obstruction analysis: what the relative construction misses
    9. Relative vs absolute comparison
   10. Second-quantized elliptic genus verification
   11. BPS Lie algebra from relative construction

Ground truth:
    - CY-A_2 (PROVED): Phi_2(D^b(K3)) = V_{tilde{Lambda}_{K3}}
    - Mukai lattice: rank 24, signature (4,20)
    - kappa_ch(K3) = 2 (chi(O_{K3}))
    - kappa_ch(K3 x E) = 3 (additivity)
    - kappa_BKM = 5 (weight of Delta_5)
    - kappa_fiber = 24 (Mukai rank)
    - Total root multiplicity per level = 24 (Jacobi form identity)
    - c(-1) = 1, c(0) = 10 (EZ normalization)
    - K3 is formal (DGMS 1975)

Manuscript references:
    k3_times_e.tex: ch:k3-times-e
    toroidal_elliptic.tex: sec:k3e-relative-chiral, sec:k3e-relative-fact-hom
"""

import pytest
import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from lib.k3e_relative_chiral_algebra import (
    # Constants
    H_K3,
    MUKAI_RANK,
    MUKAI_SIGNATURE,
    HH_DIMS,
    HH_TOTAL,
    # Fiber functions
    phi2_fiber_data,
    phi2_fiber_character_coeffs,
    # Base functions
    base_elliptic_data,
    # Relative functions
    relative_chiral_algebra_data,
    # Factorization homology
    fact_hom_character_rank0,
    fact_hom_character_dmvv,
    # Kappa spectrum
    kappa_spectrum_relative,
    # BKM positive part
    bkm_positive_part_from_relative,
    total_root_mult_per_level,
    # Obstruction analysis
    obstruction_analysis,
    relative_vs_absolute_comparison,
    # Second-quantized elliptic genus
    second_quantized_elliptic_genus_check,
    # BPS Lie algebra
    bps_lie_algebra_from_relative,
)


# =========================================================================
# 1. FIBER: Phi_2(D^b(Coh(K3)))
# =========================================================================

class TestPhi2Fiber:
    """The CY2 fiber under the constructed functor Phi_2."""

    def test_mukai_rank(self):
        """Mukai lattice rank = 24."""
        assert MUKAI_RANK == 24

    def test_mukai_signature(self):
        """Mukai lattice signature = (4, 20)."""
        assert MUKAI_SIGNATURE == (4, 20)

    def test_hh_total(self):
        """Total Hochschild homology dim = 24 = Mukai rank."""
        assert HH_TOTAL == 24
        assert HH_TOTAL == MUKAI_RANK

    def test_hh_dims(self):
        """HH_0 = 2, HH_1 = 20, HH_2 = 2."""
        assert HH_DIMS[0] == 2
        assert HH_DIMS[1] == 20
        assert HH_DIMS[2] == 2

    def test_fiber_kappa_ch(self):
        """kappa_ch(K3) = 2 = chi(O_{K3})."""
        data = phi2_fiber_data()
        assert data['kappa_ch'] == 2

    def test_chi_O_K3(self):
        """chi(O_{K3}) = h^{0,0} - h^{1,0} + h^{2,0} = 1 - 0 + 1 = 2."""
        data = phi2_fiber_data()
        assert data['chi_O_K3'] == 2

    def test_central_charge(self):
        """Central charge = 24 (Mukai rank)."""
        data = phi2_fiber_data()
        assert data['central_charge'] == 24

    def test_e2_structure(self):
        """Fiber algebra is E_2 (from CY_2)."""
        data = phi2_fiber_data()
        assert data['E_n_level'] == 2

    def test_shadow_class_G(self):
        """Fiber shadow class is G (Gaussian)."""
        data = phi2_fiber_data()
        assert data['shadow_class'] == 'G'

    def test_construction_proved(self):
        """CY-A_2 is proved."""
        data = phi2_fiber_data()
        assert 'PROVED' in data['construction_status']

    def test_hodge_numbers(self):
        """K3 Hodge numbers: h^{0,0}=1, h^{1,1}=20, h^{2,0}=1."""
        assert H_K3[(0, 0)] == 1
        assert H_K3[(1, 1)] == 20
        assert H_K3[(2, 0)] == 1
        assert H_K3[(1, 0)] == 0

    def test_betti_numbers(self):
        """K3 Betti numbers: b_0=1, b_1=0, b_2=22, b_3=0, b_4=1."""
        b0 = H_K3[(0, 0)]
        b2 = H_K3[(2, 0)] + H_K3[(1, 1)] + H_K3[(0, 2)]
        b4 = H_K3[(2, 2)]
        assert b0 == 1
        assert b2 == 22
        assert b4 == 1
        assert b0 + b2 + b4 == 24  # = Mukai rank


class TestPhi2FiberCharacter:
    """Character coefficients of V_{tilde{Lambda}_{K3}}."""

    def test_leading_coeff(self):
        """Leading coefficient = 1."""
        coeffs = phi2_fiber_character_coeffs(0)
        assert coeffs[0] == 1

    def test_n1_coeff(self):
        """Coefficient at n=1 is 24 = chi(K3)."""
        coeffs = phi2_fiber_character_coeffs(1)
        assert coeffs[1] == 24

    def test_n2_coeff(self):
        """Coefficient at n=2 is 324 = chi(Hilb^2(K3))."""
        coeffs = phi2_fiber_character_coeffs(2)
        assert coeffs[2] == 324

    def test_growth(self):
        """Coefficients are strictly increasing for n >= 1."""
        coeffs = phi2_fiber_character_coeffs(6)
        for n in range(1, 6):
            assert coeffs[n + 1] > coeffs[n]


# =========================================================================
# 2. BASE: elliptic curve E
# =========================================================================

class TestBaseEllipticCurve:
    """Data of the base elliptic curve E."""

    def test_genus(self):
        """E has genus 1."""
        data = base_elliptic_data()
        assert data['genus'] == 1

    def test_chi_O_E(self):
        """chi(O_E) = 1 - g = 0."""
        data = base_elliptic_data()
        assert data['chi_O_E'] == 0

    def test_kappa_ch_E(self):
        """kappa_ch(E) = 1 (from Phi_1)."""
        data = base_elliptic_data()
        assert data['kappa_ch_E'] == 1

    def test_hh_dims(self):
        """HH_0(E) = 2, HH_1(E) = 2."""
        data = base_elliptic_data()
        assert data['HH_dims'][0] == 2
        assert data['HH_dims'][1] == 2


# =========================================================================
# 3. RELATIVE CHIRAL ALGEBRA A_{K3xE/E}
# =========================================================================

class TestRelativeChiralAlgebra:
    """The relative chiral algebra A_{K3xE/E}."""

    def test_relative_kappa_ch(self):
        """kappa_ch(K3xE) = kappa_ch(K3) + kappa_ch(E) = 2 + 1 = 3."""
        data = relative_chiral_algebra_data()
        assert data['relative_kappa_ch'] == 3

    def test_fiber_kappa_ch(self):
        """Fiber kappa_ch = 2."""
        data = relative_chiral_algebra_data()
        assert data['fiber_kappa_ch'] == 2

    def test_base_kappa_ch(self):
        """Base kappa_ch = 1."""
        data = relative_chiral_algebra_data()
        assert data['base_kappa_ch'] == 1

    def test_kappa_fiber(self):
        """kappa_fiber = 24 (Mukai rank)."""
        data = relative_chiral_algebra_data()
        assert data['kappa_fiber'] == 24

    def test_kappa_BKM(self):
        """kappa_BKM = 5 (weight of Delta_5)."""
        data = relative_chiral_algebra_data()
        assert data['kappa_BKM'] == 5

    def test_shadow_class_fiber_G(self):
        """Fiber shadow class is G."""
        data = relative_chiral_algebra_data()
        assert data['shadow_class_fiber'] == 'G'

    def test_shadow_class_relative_M(self):
        """Relative shadow class is M (from sewing)."""
        data = relative_chiral_algebra_data()
        assert data['shadow_class_relative'] == 'M'

    def test_kappa_additivity(self):
        """kappa_ch is additive: kappa_ch(K3xE) = kappa_ch(K3) + kappa_ch(E)."""
        data = relative_chiral_algebra_data()
        assert data['relative_kappa_ch'] == data['fiber_kappa_ch'] + data['base_kappa_ch']


# =========================================================================
# 4. FACTORIZATION HOMOLOGY: rank-0 sector
# =========================================================================

class TestFactHom:
    """Factorization homology of A_{K3} over E."""

    KNOWN_COEFFS = {0: 1, 1: 24, 2: 324, 3: 3200, 4: 25650}

    @pytest.mark.parametrize("n,expected", list(KNOWN_COEFFS.items()))
    def test_rank0_coefficients(self, n, expected):
        """Rank-0 character = 1/eta^{24}."""
        coeffs = fact_hom_character_rank0(n)
        assert coeffs[n] == expected

    def test_rank0_matches_hilb(self):
        """Rank-0 coefficients = chi(Hilb^n(K3))."""
        from lib.k3e_relative_shadow import KNOWN_HILB_CHI
        coeffs = fact_hom_character_rank0(max(KNOWN_HILB_CHI.keys()))
        for n, expected in KNOWN_HILB_CHI.items():
            assert coeffs[n] == expected

    def test_dmvv_has_rank0(self):
        """DMVV formula has a rank-0 sector."""
        result = fact_hom_character_dmvv(2, 3, 2)
        assert 'rank0_sector' in result
        assert result['rank0_sector'][0] == 1

    def test_dmvv_log_nonempty(self):
        """DMVV log expansion has entries."""
        result = fact_hom_character_dmvv(2, 3, 2)
        assert len(result['log_coefficients']) > 0


# =========================================================================
# 5. KAPPA SPECTRUM
# =========================================================================

class TestKappaSpectrum:
    """The kappa spectrum accessible from the relative construction."""

    def test_kappa_ch_K3(self):
        """kappa_ch(K3) = 2."""
        spec = kappa_spectrum_relative()
        assert spec['kappa_ch_K3'] == 2

    def test_kappa_ch_K3xE(self):
        """kappa_ch(K3 x E) = 3."""
        spec = kappa_spectrum_relative()
        assert spec['kappa_ch_K3xE'] == 3

    def test_kappa_cat(self):
        """kappa_cat = 2 = chi(O_{K3})."""
        spec = kappa_spectrum_relative()
        assert spec['kappa_cat'] == 2

    def test_kappa_fiber(self):
        """kappa_fiber = 24."""
        spec = kappa_spectrum_relative()
        assert spec['kappa_fiber'] == 24

    def test_kappa_BKM(self):
        """kappa_BKM = 5 = c(0)/2."""
        spec = kappa_spectrum_relative()
        assert spec['kappa_BKM'] == 5

    def test_c0_is_10(self):
        """c(0) = 10 in EZ normalization."""
        spec = kappa_spectrum_relative()
        assert spec['c0'] == 10

    def test_all_from_relative(self):
        """All kappa values accessible from relative construction."""
        spec = kappa_spectrum_relative()
        assert spec['all_from_relative'] is True

    def test_kappa_BKM_is_fraction(self):
        """kappa_BKM is exactly 5 (not approximate)."""
        spec = kappa_spectrum_relative()
        assert spec['kappa_BKM'] == Fraction(5)


# =========================================================================
# 6. BKM POSITIVE PART
# =========================================================================

class TestBKMPositivePart:
    """Root multiplicities from the relative bar complex."""

    def test_level1_has_roots(self):
        """Level 1 has positive roots."""
        data = bkm_positive_part_from_relative(3)
        assert data[1]['num_roots'] > 0

    def test_level1_total_mult_24(self):
        """Total root multiplicity at level 1 is 24."""
        data = bkm_positive_part_from_relative(3)
        assert data[1]['total_mult'] == 24

    def test_root_types(self):
        """Roots are correctly classified as real/lightlike/imaginary."""
        data = bkm_positive_part_from_relative(3)
        for h in range(1, 4):
            for root_info in data[h]['roots']:
                D = root_info['D']
                if D == -1:
                    assert root_info['type'] == 'real'
                elif D == 0:
                    assert root_info['type'] == 'lightlike'
                else:
                    assert root_info['type'] == 'imaginary'


# =========================================================================
# 7. TOTAL ROOT MULTIPLICITY = 24
# =========================================================================

class TestTotalMultiplicity:
    """Total root multiplicity at each level = 24 = chi(K3)."""

    @pytest.mark.parametrize("h", range(1, 11))
    def test_level_h_mult_24(self, h):
        """Total multiplicity at level h is 24."""
        mult = total_root_mult_per_level(h)
        assert mult[h] == 24, f"Total mult at level {h}: {mult[h]}, expected 24"

    def test_levels_1_to_20(self):
        """All levels 1-20 have total multiplicity 24."""
        mult = total_root_mult_per_level(20)
        for h in range(1, 21):
            assert mult[h] == 24, f"Level {h}: {mult[h]}"


# =========================================================================
# 8. OBSTRUCTION ANALYSIS
# =========================================================================

class TestObstructionAnalysis:
    """What the relative construction misses."""

    def test_cohomological_obstruction_vanishes(self):
        """K3 x E is formal, so cohomological obstruction vanishes."""
        obs = obstruction_analysis()
        assert obs['cohomological_obstruction'] == 'VANISHES (K3 x E is formal)'

    def test_chain_level_obstruction_nonvanishing(self):
        """Chain-level obstruction is non-vanishing."""
        obs = obstruction_analysis()
        assert 'NON-VANISHING' in obs['chain_level_obstruction']

    def test_formality(self):
        """K3 is formal, E is formal, K3 x E is formal."""
        obs = obstruction_analysis()
        assert obs['formality_of_K3'] is True
        assert obs['formality_of_E'] is True
        assert obs['formality_of_product'] is True

    def test_massey_products_zero(self):
        """Massey products vanish on cohomology (formality)."""
        obs = obstruction_analysis()
        assert 'zero' in obs['massey_products'].lower()


# =========================================================================
# 9. RELATIVE VS ABSOLUTE COMPARISON
# =========================================================================

class TestRelativeVsAbsolute:
    """Comparison of relative and absolute constructions."""

    def test_agreement_list_nonempty(self):
        """Relative and absolute agree on many features."""
        comp = relative_vs_absolute_comparison()
        assert len(comp['agree_on']) >= 8

    def test_disagreement_list_nonempty(self):
        """Relative and absolute differ on some features."""
        comp = relative_vs_absolute_comparison()
        assert len(comp['differ_on']) >= 2

    def test_e_n_differs(self):
        """E_n level differs: E_2 (relative) vs E_1 (absolute)."""
        comp = relative_vs_absolute_comparison()
        en_diff = [d for d in comp['differ_on'] if 'E_n' in d or 'E_2' in d]
        assert len(en_diff) > 0

    def test_formality_explains_agreement(self):
        """Formality of K3 explains the agreement."""
        comp = relative_vs_absolute_comparison()
        assert 'formal' in comp['reason_for_agreement'].lower()


# =========================================================================
# 10. SECOND-QUANTIZED ELLIPTIC GENUS
# =========================================================================

class TestSecondQuantizedEllipticGenus:
    """Verification of the second-quantized elliptic genus."""

    def test_all_checks_pass(self):
        """All verification checks pass."""
        result = second_quantized_elliptic_genus_check(6)
        assert result['all_checks_pass'] is True

    def test_rank0_correct(self):
        """Rank-0 character is correct."""
        result = second_quantized_elliptic_genus_check(3)
        assert result['rank0_correct'] is True

    def test_borcherds_weight(self):
        """Borcherds weight = 5."""
        result = second_quantized_elliptic_genus_check(3)
        assert result['weight_correct'] is True
        assert result['borcherds_weight'] == 5

    def test_c_neg1(self):
        """c(-1) = 1 in EZ normalization."""
        result = second_quantized_elliptic_genus_check(3)
        assert result['c_neg1_correct'] is True
        assert result['c_neg1'] == 1

    def test_mult_all_24(self):
        """Total root multiplicity at each level is 24."""
        result = second_quantized_elliptic_genus_check(6)
        assert result['mult_all_24'] is True


# =========================================================================
# 11. BPS LIE ALGEBRA
# =========================================================================

class TestBPSLieAlgebra:
    """The positive part g^+ of g_{Delta_5}."""

    def test_has_real_roots(self):
        """g^+ has real roots."""
        result = bps_lie_algebra_from_relative(3)
        assert result['total_real_mult'] > 0

    def test_has_imaginary_roots(self):
        """g^+ has imaginary roots."""
        result = bps_lie_algebra_from_relative(3)
        assert result['total_imaginary_mult'] > 0

    def test_has_lightlike_roots(self):
        """g^+ has lightlike roots."""
        result = bps_lie_algebra_from_relative(3)
        assert result['total_lightlike_mult'] > 0

    def test_coha_identification(self):
        """CoHA identification is stated correctly (AP-CY7)."""
        result = bps_lie_algebra_from_relative(3)
        # AP-CY7: CoHA != chiral algebra
        assert 'CoHA' in result['coha_identification']
        assert 'ASSOCIATIVE' in result['coha_identification']


# =========================================================================
# 12. CROSS-MODULE CONSISTENCY
# =========================================================================

class TestCrossModuleConsistency:
    """Consistency with other compute modules."""

    def test_fiber_kappa_consistent_with_relative_shadow(self):
        """fiber_kappa() from k3e_relative_shadow = 24."""
        from lib.k3e_relative_shadow import fiber_kappa as shadow_fiber_kappa
        assert shadow_fiber_kappa() == 24

    def test_mukai_rank_consistent(self):
        """Mukai rank = HH_total = 24."""
        assert MUKAI_RANK == HH_TOTAL == 24

    def test_chi_K3_consistent(self):
        """chi(K3) = 24 from both modules."""
        from lib.k3e_relative_shadow import CHI_K3 as shadow_chi
        assert shadow_chi == 24
        # chi(K3) = sum (-1)^i b_i = 1 - 0 + 22 - 0 + 1 = 24
        betti_sum = (H_K3[(0, 0)]
                     - 2 * H_K3[(1, 0)]
                     + H_K3[(2, 0)] + H_K3[(1, 1)] + H_K3[(0, 2)]
                     - 2 * H_K3[(2, 1)]
                     + H_K3[(2, 2)])
        assert betti_sum == 24

    def test_kappa_ch_consistent_with_phi01(self):
        """kappa_BKM = c(0)/2 = 5, consistent with phi01_fourier."""
        from lib.phi01_fourier import phi01_by_discriminant
        c_disc = phi01_by_discriminant(5)
        assert Fraction(c_disc[0], 2) == 5
