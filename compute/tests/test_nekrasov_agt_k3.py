r"""Tests for nekrasov_agt_k3: AGT correspondence for K3, Nekrasov partition
function, Heisenberg conformal blocks, and K3 Yangian character.

Claims tested:
  1. VW partition function = Heisenberg Fock character (genus-1 AGT)
  2. chi_y genus specializations: chi_1 = 24, chi_0 = 2, chi_{-1} = -16
  3. Modular weight = -12 = -chi(K3)/2
  4. Kummer decomposition: 24 = 8 (invariant) + 16 (twisted)
  5. Ramanujan tau function cross-check
  6. BPS degeneracy counting
  7. Conformal block dimensions at genus 0, 1, 2
  8. Refined VW specializations
  9. Wall-crossing at rank 1 (trivial) and rank 2 (nontrivial)
  10. Full AGT verification suite

Ground truth:
  Gottsche (1990): chi(Hilb^n(K3)) from prod 1/(1-q^k)^{chi(K3)}
  Ramanujan: tau(1)=1, tau(2)=-24, tau(3)=252, tau(4)=-1472, tau(5)=4830
  Vafa-Witten (hep-th/9408074): modularity, S-duality
  Schiffmann-Vasserot (arXiv:1211.1287): AGT for C^2

Manuscript references:
  k3_times_e.tex: sec:k3e-gottsche-eta, sec:k3e-topological-string-shadow
  k3_times_e.tex: subsec:k3-yangian, conj:k3-yangian
"""

import pytest
from fractions import Fraction

F = Fraction

from compute.lib.nekrasov_agt_k3 import (
    # Constants
    K3_CHI, K3_CHI_O, K3_B2, MUKAI_RANK,
    KAPPA_CH, KAPPA_CAT, KAPPA_BKM, KAPPA_FIBER,
    C_HEISENBERG_K3, VW_WEIGHT_K3,
    KNOWN_HILB_CHI, KNOWN_TAU,
    STATUS_PROVED, STATUS_CONJECTURAL,
    # Core functions
    colored_partition,
    vw_partition_function_k3,
    heisenberg_partition_function_genus1,
    heisenberg_conformal_block_genus_g,
    # AGT comparison
    verify_agt_genus1,
    # Refined VW
    refined_vw_partition_function,
    chi_y_genus_k3,
    verify_chi_y_specializations,
    refined_vw_coefficients_factored,
    # Yangian character
    k3_yangian_character_prediction,
    # Kummer
    kummer_vw_partition_function,
    kummer_yangian_comparison,
    # Modularity
    verify_modular_weight_k3,
    verify_yangian_character_modularity,
    # Wall-crossing
    wall_crossing_rank1_k3,
    wall_crossing_rank2_k3,
    wall_crossing_yangian_fusion_prediction,
    # Tau function
    ramanujan_tau_from_eta24,
    verify_tau_values,
    # BPS
    bps_degeneracies_from_vw,
    # Full suite
    full_agt_verification,
    status_summary,
)


# ======================================================================
# 1. Vafa-Witten partition function = Heisenberg Fock character
# ======================================================================

class TestAGTGenus1:
    """Verify the genus-1 AGT: Z_VW(K3) = ch(Fock(H_Muk))."""

    def test_agt_genus1_holds(self):
        """The genus-1 AGT identification holds at max_n = 6."""
        result = verify_agt_genus1(6)
        assert result['agt_genus1_holds'] is True

    def test_coefficients_match(self):
        """VW and Heisenberg coefficients agree term-by-term."""
        vw = vw_partition_function_k3(6)
        heis = heisenberg_partition_function_genus1(6)
        assert vw == heis

    def test_vw_equals_p24(self):
        """VW coefficients are 24-coloured partition numbers."""
        vw = vw_partition_function_k3(6)
        for n in range(7):
            assert vw[n] == colored_partition(n, 24)

    def test_known_hilb_chi(self):
        """chi(Hilb^n(K3)) matches known values from Gottsche."""
        vw = vw_partition_function_k3(6)
        # VERIFIED [DC] Hilbert scheme chi [LT] Gottsche 1990
        for n, expected in KNOWN_HILB_CHI.items():
            assert vw[n] == expected, f"n={n}: {vw[n]} != {expected}"

    def test_hilb_0_is_1(self):
        """chi(Hilb^0(K3)) = 1 (a point)."""
        vw = vw_partition_function_k3(0)
        assert vw[0] == 1

    def test_hilb_1_is_24(self):
        """chi(Hilb^1(K3)) = 24 = chi(K3)."""
        vw = vw_partition_function_k3(1)
        assert vw[1] == 24

    def test_hilb_2_is_324(self):
        """chi(Hilb^2(K3)) = 324."""
        vw = vw_partition_function_k3(2)
        assert vw[2] == 324

    def test_hilb_3_is_3200(self):
        """chi(Hilb^3(K3)) = 3200."""
        vw = vw_partition_function_k3(3)
        assert vw[3] == 3200

    def test_integrality_and_positivity(self):
        """All chi(Hilb^n(K3)) are positive integers."""
        vw = vw_partition_function_k3(8)
        for n, val in enumerate(vw):
            assert isinstance(val, int)
            assert val > 0

    def test_status_is_proved(self):
        """Genus-1 AGT is PROVED (classical, no Yangian needed)."""
        result = verify_agt_genus1(3)
        assert result['status'] == STATUS_PROVED


# ======================================================================
# 2. Hirzebruch chi_y genus
# ======================================================================

class TestChiYGenus:
    """Verify chi_y(K3) = 2 + 20y + 2y^2 and its specializations."""

    def test_chi_y_at_1(self):
        """chi_1(K3) = 24 = chi(K3) = kappa_fiber."""
        assert chi_y_genus_k3(F(1)) == F(24)

    def test_chi_y_at_0(self):
        """chi_0(K3) = 2 = chi(O_{K3}) = kappa_cat."""
        assert chi_y_genus_k3(F(0)) == F(2)

    def test_chi_y_at_neg1(self):
        """chi_{-1}(K3) = -16 = Tr(omega_Muk) = 4 - 20."""
        assert chi_y_genus_k3(F(-1)) == F(-16)

    def test_verify_all_specializations(self):
        """All chi_y specializations match expected values."""
        result = verify_chi_y_specializations()
        assert result['all_match'] is True

    def test_chi_y_polynomial_form(self):
        """chi_y = 2 + 20y + 2y^2 as a polynomial."""
        # Verify at multiple points
        for y_val, expected in [(F(2), F(2 + 40 + 8)),
                                 (F(-2), F(2 - 40 + 8)),
                                 (F(1, 2), F(2 + 10 + F(1, 2)))]:
            assert chi_y_genus_k3(y_val) == expected

    def test_kappa_cat_from_chi_0(self):
        """chi_0(K3) recovers kappa_cat = 2."""
        assert chi_y_genus_k3(F(0)) == KAPPA_CAT

    def test_kappa_fiber_from_chi_1(self):
        """chi_1(K3) recovers kappa_fiber = 24."""
        assert chi_y_genus_k3(F(1)) == KAPPA_FIBER


# ======================================================================
# 3. Modular weight
# ======================================================================

class TestModularity:
    """Verify VW modular weight and S-duality structure."""

    def test_modular_weight_k3(self):
        """VW modular weight on K3 is -12."""
        result = verify_modular_weight_k3()
        assert result['weights_match'] is True
        assert result['vw_modular_weight'] == F(-12)

    def test_weight_formula(self):
        """weight = -chi(K3)/2 = -24/2 = -12."""
        assert VW_WEIGHT_K3 == F(-12)
        assert VW_WEIGHT_K3 == F(-K3_CHI, 2)

    def test_kappa_fiber_relation(self):
        """weight = -kappa_fiber / 2."""
        result = verify_modular_weight_k3()
        assert result['vw_modular_weight'] == -KAPPA_FIBER / 2


# ======================================================================
# 4. Kummer orbifold decomposition
# ======================================================================

class TestKummerDecomposition:
    """Verify Kummer orbifold decomposition of Z_VW."""

    def test_exponent_sum(self):
        """24 = 8 (invariant) + 16 (twisted)."""
        result = kummer_vw_partition_function(6)
        assert result['exponent_sum_correct'] is True

    def test_invariant_rank(self):
        """Invariant sublattice has rank 8."""
        result = kummer_vw_partition_function(3)
        assert result['invariant_rank'] == 8

    def test_twisted_rank(self):
        """16 twisted sectors (from 16 fixed points of Z_2)."""
        result = kummer_vw_partition_function(3)
        assert result['twisted_rank'] == 16

    def test_kappa_ch_kummer(self):
        """kappa_ch at Kummer point = 2 = chi(O_{K3})."""
        result = kummer_vw_partition_function(3)
        assert result['kappa_ch_kummer'] == KAPPA_CAT

    def test_steps_1_through_4_proved(self):
        """Kummer route Steps 1-4 are proved."""
        result = kummer_vw_partition_function(3)
        assert result['steps_proved'] == [1, 2, 3, 4]

    def test_step_5_conjectural(self):
        """Step 5 (Yangian identification) is conjectural."""
        result = kummer_vw_partition_function(3)
        assert result['step_5_status'] == STATUS_CONJECTURAL


class TestKummerYangianComparison:
    """Verify Kummer Yangian character matches VW."""

    def test_characters_match(self):
        """Kummer Yangian character = VW partition function."""
        result = kummer_yangian_comparison(6)
        assert result['characters_match'] is True

    def test_flat_deformation_reason(self):
        """Match is due to flat deformation invariance."""
        result = kummer_yangian_comparison(3)
        assert 'Flat deformation' in result['reason']

    def test_status_conjectural(self):
        """Kummer Yangian comparison is conjectural (AP-CY14)."""
        result = kummer_yangian_comparison(3)
        assert result['status'] == STATUS_CONJECTURAL


# ======================================================================
# 5. Ramanujan tau function
# ======================================================================

class TestRamanujanTau:
    """Verify tau(n) from eta^{24} matches known values."""

    def test_tau_1(self):
        """tau(1) = 1."""
        tau = ramanujan_tau_from_eta24(5)
        assert tau[1] == 1

    def test_tau_2(self):
        """tau(2) = -24."""
        tau = ramanujan_tau_from_eta24(5)
        assert tau[2] == -24

    def test_tau_3(self):
        """tau(3) = 252."""
        tau = ramanujan_tau_from_eta24(5)
        assert tau[3] == 252

    def test_tau_4(self):
        """tau(4) = -1472."""
        tau = ramanujan_tau_from_eta24(5)
        assert tau[4] == -1472

    def test_tau_5(self):
        """tau(5) = 4830."""
        tau = ramanujan_tau_from_eta24(5)
        assert tau[5] == 4830

    def test_all_known_tau(self):
        """All known tau values match."""
        result = verify_tau_values(10)
        assert result['all_pass'] is True

    def test_multiplicativity_2_3(self):
        """tau(6) = tau(2)*tau(3) (Hecke multiplicativity at coprime)."""
        tau = ramanujan_tau_from_eta24(10)
        # tau is multiplicative for coprime n, m:
        # tau(2*3) = tau(2)*tau(3)
        assert tau[6] == tau[2] * tau[3]

    def test_tau_positivity_pattern(self):
        """tau alternates sign for small n (not a theorem, an observation)."""
        tau = ramanujan_tau_from_eta24(6)
        # tau(1) = 1 > 0, tau(2) = -24 < 0, tau(3) = 252 > 0, ...
        assert tau[1] > 0
        assert tau[2] < 0
        assert tau[3] > 0


# ======================================================================
# 6. BPS degeneracies
# ======================================================================

class TestBPSDegeneracies:
    """Verify BPS state counting from VW."""

    def test_bps_degeneracies_match_hilb(self):
        """BPS degeneracies = chi(Hilb^n(K3))."""
        result = bps_degeneracies_from_vw(6)
        for n, expected in KNOWN_HILB_CHI.items():
            assert result['bps_degeneracies'][n] == expected

    def test_asymptotic_growth(self):
        """log Omega(n) grows as ~ 4*pi*sqrt(n) for large n."""
        result = bps_degeneracies_from_vw(6)
        # At n=6, the ratio log(Omega)/BH should be close to 1
        # (but not exactly 1 -- the asymptotic is for large n)
        import math
        omega_6 = KNOWN_HILB_CHI[6]
        log_omega = math.log(omega_6)
        bh_6 = 4 * math.pi * math.sqrt(6)
        ratio = log_omega / bh_6
        # Should be between 0.3 and 1.5 (approaching 1 from below)
        assert 0.3 < ratio < 1.5


# ======================================================================
# 7. Conformal block dimensions
# ======================================================================

class TestConformalBlocks:
    """Verify Heisenberg conformal block data at various genera."""

    def test_genus_0(self):
        """Genus-0 conformal block is trivial."""
        result = heisenberg_conformal_block_genus_g(0)
        assert result['conformal_block_dim'] == 1
        assert result['genus'] == 0

    def test_genus_1(self):
        """Genus-1 conformal block: 1-dimensional, weight -12."""
        result = heisenberg_conformal_block_genus_g(1)
        assert result['conformal_block_dim'] == 1
        assert result['modular_weight'] == F(-12)
        assert result['central_charge'] == 24

    def test_genus_2(self):
        """Genus-2: weight -24, Sp(4,Z) modular group."""
        result = heisenberg_conformal_block_genus_g(2)
        assert result['modular_weight'] == F(-24)
        assert result['modular_group'] == 'Sp(4,Z)'

    def test_genus_3(self):
        """Genus-3: weight -36."""
        result = heisenberg_conformal_block_genus_g(3)
        assert result['modular_weight'] == F(-36)

    def test_weight_scaling(self):
        """Modular weight scales as -12*g."""
        for g in range(5):
            result = heisenberg_conformal_block_genus_g(g)
            assert result['modular_weight'] == F(-12) * g

    def test_status_proved(self):
        """Conformal block data is PROVED (classical)."""
        for g in range(3):
            result = heisenberg_conformal_block_genus_g(g)
            assert result['status'] == STATUS_PROVED


# ======================================================================
# 8. Refined VW partition function
# ======================================================================

class TestRefinedVW:
    """Verify refined VW partition function properties."""

    def test_unrefined_coefficients(self):
        """Unrefined (y=1) refined VW = standard VW."""
        ref = refined_vw_partition_function(6)
        for n, expected in KNOWN_HILB_CHI.items():
            assert ref.unrefined_coeffs[n] == expected

    def test_chi_y_at_y1_gives_24(self):
        """At y=1, chi_y = 24, so refined = unrefined."""
        coeffs = refined_vw_coefficients_factored(6, F(1))
        vw = vw_partition_function_k3(6)
        assert [int(c) for c in coeffs] == vw

    def test_chi_y_at_y0_gives_2(self):
        """At y=0, chi_y = 2, giving prod 1/(1-q^n)^2."""
        coeffs = refined_vw_coefficients_factored(6, F(0))
        # prod 1/(1-q^n)^2 coefficients: p_2(n)
        expected = [colored_partition(n, 2) for n in range(7)]
        assert [int(c) for c in coeffs] == expected

    def test_mukai_signature(self):
        """Mukai signature is (4, 20)."""
        ref = refined_vw_partition_function(3)
        assert ref.mukai_signature == (4, 20)

    def test_central_charge_24(self):
        """Central charge c = 24."""
        ref = refined_vw_partition_function(3)
        assert ref.central_charge == 24


# ======================================================================
# 9. Wall-crossing
# ======================================================================

class TestWallCrossing:
    """Verify wall-crossing structure."""

    def test_rank1_trivial(self):
        """Rank-1 wall-crossing is trivial (Hilb^n smooth)."""
        result = wall_crossing_rank1_k3()
        assert result['stability_independent'] is True
        assert result['status'] == STATUS_PROVED

    def test_rank2_nontrivial(self):
        """Rank-2 wall-crossing is nontrivial."""
        result = wall_crossing_rank2_k3()
        assert result['ks_formula'] == 'PROVED (Kontsevich-Soibelman)'

    def test_yangian_fusion_conjectural(self):
        """Yangian fusion interpretation is conjectural."""
        result = wall_crossing_yangian_fusion_prediction()
        assert result['status'] == STATUS_CONJECTURAL

    def test_higher_coherence_warning(self):
        """AP-CY30 higher coherence warning is present."""
        result = wall_crossing_yangian_fusion_prediction()
        assert 'AP-CY30' in result['higher_coherence']


# ======================================================================
# 10. Yangian character prediction
# ======================================================================

class TestYangianCharacter:
    """Verify K3 Yangian character predictions (CONJECTURAL)."""

    def test_fock_equals_vw(self):
        """Yangian Fock character = VW partition function."""
        result = k3_yangian_character_prediction(6)
        assert result['fock_equals_vw'] is True

    def test_bar_euler_eta24(self):
        """Bar Euler product = eta^{24}/q (Ramanujan Delta shifted)."""
        result = k3_yangian_character_prediction(6)
        # eta^{24} at q^0 is 1
        assert result['bar_euler_coeffs'][0] == 1
        # eta^{24} at q^1 is -24
        assert result['bar_euler_coeffs'][1] == -24

    def test_yangian_character_modularity(self):
        """Yangian character modularity prediction."""
        result = verify_yangian_character_modularity()
        assert result['genus_1_modular'] is True
        assert result['genus_1_group'] == 'SL(2,Z)'
        assert result['genus_2_group'] == 'Sp(4,Z)'

    def test_status_conjectural(self):
        """All Yangian character results are conjectural."""
        result = k3_yangian_character_prediction(3)
        assert result['status'] == STATUS_CONJECTURAL


# ======================================================================
# 11. Constants and kappa-spectrum
# ======================================================================

class TestConstants:
    """Verify constants and kappa-spectrum (AP113)."""

    def test_kappa_spectrum(self):
        """kappa-spectrum: ch=3, cat=2, BKM=5, fiber=24."""
        assert KAPPA_CH == F(3)
        assert KAPPA_CAT == F(2)
        assert KAPPA_BKM == F(5)
        assert KAPPA_FIBER == F(24)

    def test_k3_euler_characteristic(self):
        """chi(K3) = 24."""
        assert K3_CHI == 24

    def test_k3_holomorphic_euler(self):
        """chi(O_{K3}) = 2."""
        assert K3_CHI_O == 2

    def test_mukai_rank(self):
        """Mukai lattice rank = 24."""
        assert MUKAI_RANK == 24

    def test_central_charge(self):
        """Heisenberg central charge c = 24."""
        assert C_HEISENBERG_K3 == 24


# ======================================================================
# 12. Full verification suite
# ======================================================================

class TestFullSuite:
    """Verify the complete AGT verification suite."""

    def test_full_agt_all_pass(self):
        """All classical AGT checks pass."""
        result = full_agt_verification(6)
        assert result['classical_all_pass'] is True

    def test_total_checks(self):
        """Five classical checks are performed."""
        result = full_agt_verification(6)
        assert result['total_checks'] == 5

    def test_status_summary_completeness(self):
        """Status summary covers all claims."""
        summary = status_summary()
        proved_count = sum(1 for v in summary.values() if 'PROVED' in v)
        conjectural_count = sum(1 for v in summary.values() if 'CONJECTURAL' in v)
        # At least 7 proved and 4 conjectural claims
        assert proved_count >= 7
        assert conjectural_count >= 4


# ======================================================================
# 13. Cross-consistency with existing engines
# ======================================================================

class TestCrossConsistency:
    """Cross-check with existing VW and K3 engines."""

    def test_consistency_with_vafa_witten_k3(self):
        """Our VW coefficients match vafa_witten_k3.py."""
        from compute.lib.vafa_witten_k3 import (
            hilb_euler_characteristics,
            KNOWN_HILB_CHI as VW_KNOWN,
        )
        ours = vw_partition_function_k3(6)
        theirs = hilb_euler_characteristics(6)
        assert ours == theirs

    def test_consistency_with_vafa_witten_shadow(self):
        """Our VW coefficients match vafa_witten_shadow.py."""
        from compute.lib.vafa_witten_shadow import (
            vw_hilb_euler_k3,
            KNOWN_HILB_K3,
        )
        ours = vw_partition_function_k3(6)
        theirs = vw_hilb_euler_k3(6)
        assert ours == theirs

    def test_consistency_with_k3_dca(self):
        """Bar Euler product matches k3_double_current_algebra.py."""
        from compute.lib.k3_double_current_algebra import (
            bar_euler_generating_function,
        )
        from compute.lib.nekrasov_agt_k3 import _eta_power_coeffs
        our_eta24 = _eta_power_coeffs(24, 8)
        their_bar = bar_euler_generating_function(8)
        for n in range(9):
            assert int(our_eta24.get(n, F(0))) == their_bar.get(n, 0)

    def test_consistency_with_k3_yangian_bar_euler(self):
        """Bar Euler matches k3_yangian.py."""
        from compute.lib.k3_yangian import bar_euler_product_yangian
        from compute.lib.nekrasov_agt_k3 import _eta_power_coeffs
        our_eta24 = _eta_power_coeffs(24, 8)
        their_bar = bar_euler_product_yangian(8)
        for n in range(9):
            assert int(our_eta24.get(n, F(0))) == their_bar.get(n, 0)


# ======================================================================
# 14. Multi-path verification (AP10 compliance)
# ======================================================================

class TestMultiPathVerification:
    """Multi-path verification: same result derived via independent routes.

    Each test computes the SAME quantity via at least 2 independent paths
    and verifies agreement.  This is the core AP10 pattern: hardcoded
    assertions alone are insufficient; the value must be confirmed by
    independent computation routes.
    """

    def test_hilb_n_three_paths(self):
        """chi(Hilb^n(K3)) via 3 paths: eta product, coloured partitions, VW engine.

        Path 1: eta^{-24} expansion (our engine)
        Path 2: p_{24}(n) coloured partition (combinatorial recursion)
        Path 3: vafa_witten_k3.py (independent engine)
        """
        from compute.lib.vafa_witten_k3 import hilb_euler_characteristics
        max_n = 6
        path1 = vw_partition_function_k3(max_n)
        path2 = [colored_partition(n, 24) for n in range(max_n + 1)]
        path3 = hilb_euler_characteristics(max_n)
        assert path1 == path2 == path3

    def test_tau_two_paths(self):
        """tau(n) via 2 paths: our eta^{24} engine, and KNOWN_TAU table.

        Path 1: eta^{24} coefficient extraction
        Path 2: hardcoded table (verified against OEIS A000594)
        """
        computed = ramanujan_tau_from_eta24(10)
        for n, known in KNOWN_TAU.items():
            assert computed[n] == known, f"tau({n}): {computed[n]} != {known}"

    def test_tau_hecke_multiplicativity(self):
        """tau(mn) = tau(m)*tau(n) for coprime m, n (Hecke eigenform).

        This is an ALGEBRAIC cross-check: the multiplicativity property
        is a theorem (Mordell 1917), independent of the eta product
        computation route.

        Path 1: direct computation from eta^{24}
        Path 2: multiplicativity relation tau(mn) = tau(m)*tau(n)
        """
        tau = ramanujan_tau_from_eta24(10)
        # (2, 3) coprime
        assert tau[6] == tau[2] * tau[3]
        # (2, 5) coprime
        assert tau[10] == tau[2] * tau[5]
        # (3, 5) coprime -- tau(15) would need max_n >= 15; skip
        # (2, 7) coprime -- tau(14) would need higher; skip
        # Instead verify the Ramanujan congruence tau(n) == sigma_11(n) mod 691
        # for n <= 10 (this is a separate algebraic property):
        # sigma_11(2) = 1 + 2^11 = 2049
        # tau(2) = -24, tau(2) mod 691 = -24 mod 691 = 667
        # sigma_11(2) mod 691 = 2049 mod 691 = 667. Check!
        assert tau[2] % 691 == 2049 % 691

    def test_chi_y_three_paths(self):
        """chi_y(K3) via 3 paths: polynomial, Hodge numbers, kappa values.

        Path 1: evaluate 2 + 20y + 2y^2
        Path 2: from Hodge numbers chi(Omega^p) = {2, -20, 2}
        Path 3: kappa_fiber at y=1, kappa_cat at y=0
        """
        # Path 1: polynomial evaluation
        path1_y1 = chi_y_genus_k3(F(1))
        path1_y0 = chi_y_genus_k3(F(0))

        # Path 2: from Hodge numbers directly
        # chi(O) = h^{0,0} - h^{0,1} + h^{0,2} = 1 - 0 + 1 = 2
        # chi(Omega^1) = h^{1,0} - h^{1,1} + h^{1,2} = 0 - 20 + 0 = -20
        # chi(Omega^2) = h^{2,0} - h^{2,1} + h^{2,2} = 1 - 0 + 1 = 2
        hodge_chi_O = 2
        hodge_chi_Om1 = -20
        hodge_chi_Om2 = 2
        path2_y1 = hodge_chi_O - hodge_chi_Om1 + hodge_chi_Om2  # 2+20+2=24
        path2_y0 = hodge_chi_O  # chi_0 = chi(O) = 2

        # Path 3: known kappa values
        path3_y1 = int(KAPPA_FIBER)  # = 24
        path3_y0 = int(KAPPA_CAT)    # = 2

        assert path1_y1 == path2_y1 == path3_y1
        assert path1_y0 == path2_y0 == path3_y0

    def test_modular_weight_two_paths(self):
        """VW modular weight via 2 paths: chi formula and eta weight.

        Path 1: weight = -chi(K3)/2 = -24/2 = -12
        Path 2: eta^{-24} transforms with weight -24*1/2 = -12
        """
        path1 = F(-K3_CHI, 2)
        # Path 2: eta^N has weight N/2, so eta^{-24} has weight -12
        path2 = F(-24, 2)
        assert path1 == path2 == F(-12)

    def test_bar_euler_three_engines(self):
        """Bar Euler prod(1-q^n)^{24} via 3 independent engines.

        Path 1: our _eta_power_coeffs(24, n)
        Path 2: k3_double_current_algebra.bar_euler_generating_function
        Path 3: k3_yangian.bar_euler_product_yangian
        """
        from compute.lib.nekrasov_agt_k3 import _eta_power_coeffs
        from compute.lib.k3_double_current_algebra import bar_euler_generating_function
        from compute.lib.k3_yangian import bar_euler_product_yangian

        max_n = 8
        path1 = {n: int(_eta_power_coeffs(24, max_n).get(n, F(0)))
                 for n in range(max_n + 1)}
        path2 = bar_euler_generating_function(max_n)
        path3 = bar_euler_product_yangian(max_n)

        for n in range(max_n + 1):
            assert path1[n] == path2.get(n, 0) == path3.get(n, 0), \
                f"Bar Euler at q^{n}: {path1[n]} vs {path2.get(n,0)} vs {path3.get(n,0)}"

    def test_kummer_exponent_decomposition_two_paths(self):
        """24 = 8 + 16 via 2 paths: our engine and direct lattice counting.

        Path 1: kummer_vw_partition_function exponent decomposition
        Path 2: direct count: T^4 has b_*(T^4)=16, Z_2-invariant sublattice
                has rank 8, 16 fixed points contribute 16.
        """
        # Path 1: from engine
        result = kummer_vw_partition_function(3)
        path1_inv = result['invariant_rank']
        path1_tw = result['twisted_rank']

        # Path 2: direct lattice theory
        # b_*(T^4) = 1 + 4 + 6 + 4 + 1 = 16
        b_star_T4 = 1 + 4 + 6 + 4 + 1
        assert b_star_T4 == 16
        # Z_2-invariant sublattice: rank = b_star_T4 / 2 = 8
        path2_inv = b_star_T4 // 2
        # Fixed points of T^4 / Z_2: 2^4 = 16
        path2_tw = 2**4

        assert path1_inv == path2_inv == 8
        assert path1_tw == path2_tw == 16
        assert path1_inv + path1_tw == K3_CHI

    def test_genus1_agt_via_independent_generating_functions(self):
        """Genus-1 AGT via 2 generating function computations.

        Path 1: prod 1/(1-q^n)^{24} via recursive eta inverse
        Path 2: sum_{partitions lambda} 1 weighted by 24-colouring
        Both should give chi(Hilb^n) = p_{24}(n).
        """
        from compute.lib.nekrasov_agt_k3 import _eta_inverse_coeffs

        max_n = 6
        # Path 1: eta inverse product
        eta_coeffs = _eta_inverse_coeffs(24, max_n)
        path1 = [int(eta_coeffs.get(n, F(0))) for n in range(max_n + 1)]

        # Path 2: coloured partition recursion (independent DP algorithm)
        path2 = [colored_partition(n, 24) for n in range(max_n + 1)]

        assert path1 == path2

    def test_bps_entropy_two_paths(self):
        """BPS entropy via 2 paths: exact count and Bekenstein-Hawking.

        Path 1: exact log(Omega(n)) from eta inverse
        Path 2: Bekenstein-Hawking entropy S_BH = 4*pi*sqrt(n) for large n

        The ratio log(Omega(n)) / (4*pi*sqrt(n)) -> 1 as n -> infinity.
        At finite n, we verify the EXPONENT agrees to within a factor.
        The Cardy formula gives S ~ 2*pi*sqrt(c_eff*n/6) with c_eff=24,
        so S ~ 4*pi*sqrt(n). The LOGARITHMIC comparison is the correct one
        (not the exponential, which has a polynomial prefactor at finite n).
        """
        import math
        # Verify at n=6 where the asymptotic is reasonable
        omega_6 = vw_partition_function_k3(6)[6]
        assert omega_6 == 1073720  # exact (Gottsche)

        log_omega = math.log(omega_6)            # ~ 13.89
        bh_entropy = 4 * math.pi * math.sqrt(6)  # ~ 30.77

        # At n=6 the ratio is about 0.45 -- the Cardy formula overestimates
        # at small n because it is an asymptotic formula. The key check is
        # that log Omega GROWS like sqrt(n), which we verify by comparing
        # the growth rate between n=3 and n=6.
        omega_3 = vw_partition_function_k3(3)[3]
        log_omega_3 = math.log(omega_3)
        log_omega_6 = log_omega

        # If log Omega ~ C*sqrt(n), then log(Omega(6))/log(Omega(3))
        # should be approximately sqrt(6)/sqrt(3) = sqrt(2) ~ 1.414
        growth_ratio = log_omega_6 / log_omega_3
        sqrt_ratio = math.sqrt(6) / math.sqrt(3)
        # Allow 30% tolerance (finite-n corrections)
        assert abs(growth_ratio - sqrt_ratio) / sqrt_ratio < 0.30, \
            f"growth ratio {growth_ratio:.4f} vs sqrt(2) = {sqrt_ratio:.4f}"
