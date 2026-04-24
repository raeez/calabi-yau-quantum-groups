r"""
Tests for modular_koszul_bridge_k3e.py: the modular Koszul bridge for K3 x E.

MATHEMATICAL CONTENT
====================

The modular Koszul bridge connects the bar complex B(A) to a modular form:

    B(A_{K3xE}) -> bar Euler product -> Borcherds lift -> Delta_5

Central result: the bar Euler exponents ARE the BKM root multiplicities
c(D) of phi_{0,1}, and the Borcherds lift produces Delta_5 (weight 5).

The weight puzzle: kappa_ch = 3 != wt(Delta_5) = 5. Resolution: these
are DIFFERENT invariants from DIFFERENT algebraizations (AP113).

Test structure:
    - Kappa-spectrum: {0, 3, 5, 24} verification (5 paths)
    - Weight formulas: W1-W4 for K3 x E
    - Bridge chain: Steps 1-5 consistency
    - Reconstruction: bar data -> phi_{0,1} -> Delta_5
    - Weight puzzle: kappa_ch = 3 vs wt = 5 resolution
    - d=2 vs d=3 comparison
    - Four obstructions separating shadow tower from Phi_10

Manuscript references:
    chapters/connections/modular_koszul_bridge.tex
    chapters/examples/k3_times_e.tex
    theory_denominator_bar_euler.tex (thm:denom-bar-euler)
"""

import pytest
from fractions import Fraction

from compute.lib.modular_koszul_bridge_k3e import (
    KappaSpectrum,
    kappa_spectrum_k3xe,
    kappa_spectrum_k3,
    kappa_spectrum_elliptic,
    WeightFormula,
    weight_formula_lattice_voa,
    weight_formula_borcherds_lift,
    weight_formula_chiral_obs,
    four_weight_formulas_k3xe,
    BridgeStep,
    ModularKoszulBridge,
    bridge_k3xe,
    bridge_k3_generic,
    reconstruct_delta5_from_bar_exponents,
    WeightPuzzleResolution,
    resolve_weight_puzzle_k3xe,
    DimensionComparison,
    compare_d2_d3,
    verify_kappa_spectrum_k3xe,
    verify_weight_puzzle_resolution,
    verify_bridge_chain_k3xe,
    verify_d2_vs_d3_comparison,
    verify_four_obstructions_k3xe,
)


# ===========================================================================
# SECTION 1: KAPPA-SPECTRUM VERIFICATION
# ===========================================================================

class TestKappaSpectrum:
    """Verify the total-space kappa-spectrum {0, 3, 5, 24} for K3 x E."""

    def test_k3xe_kappa_cat(self):
        """kappa_cat(K3 x E) = chi(O_{K3 x E}) = 0."""
        # VERIFIED [DC] Kunneth [LT] holomorphic Euler characteristic
        spec = kappa_spectrum_k3xe()
        assert spec.kappa_cat == Fraction(0)

    def test_k3xe_kappa_ch(self):
        """compact kappa_ch(K3 x E)=0; Heisenberg shadow=3."""
        # VERIFIED [DC] chiral de Rham [LT] CY-A_2 for K3 factor
        spec = kappa_spectrum_k3xe()
        assert spec.kappa_ch == Fraction(0)
        assert spec.kappa_ch_Heis == Fraction(3)

    def test_k3xe_kappa_bkm(self):
        """kappa_BKM(K3 x E) = 5 = c(0)/2 = 10/2."""
        # VERIFIED [DC] phi_{0,1} [LT] Borcherds lift weight
        spec = kappa_spectrum_k3xe()
        assert spec.kappa_bkm == Fraction(5)

    def test_k3xe_kappa_fiber(self):
        """kappa_fiber(K3 x E) = rank(Lambda_{K3}) = 24."""
        # VERIFIED [DC] K3 lattice [LT] Mukai lattice rank
        spec = kappa_spectrum_k3xe()
        assert spec.kappa_fiber == Fraction(24)

    def test_k3xe_all_distinct(self):
        """Heisenberg, BKM, compact category, and fiber values are distinct."""
        # VERIFIED [DC] spectral structure [LT] kappa-spectrum uniqueness
        spec = kappa_spectrum_k3xe()
        values = {spec.kappa_ch_Heis, spec.kappa_bkm, spec.kappa_cat, spec.kappa_fiber}
        assert len(values) == 4

    def test_k3xe_kappa_ch_additivity(self):
        """kappa_ch_Heis(K3 x E) = 2 + 1 = 3."""
        # VERIFIED [DC] additivity [LT] Proposition kappa-non-multiplicative
        k3 = kappa_spectrum_k3()
        assert k3.kappa_ch == Fraction(2)
        e = kappa_spectrum_elliptic()
        assert e.kappa_ch == Fraction(1)
        k3xe = kappa_spectrum_k3xe()
        assert k3xe.kappa_ch == Fraction(0)
        assert k3xe.kappa_ch_Heis == k3.kappa_ch + e.kappa_ch

    def test_k3_kappa_spectrum(self):
        """K3 (CY_2) kappa-spectrum: {2, 2, 12, 24}."""
        # VERIFIED [DC] Hodge diamond [LT] CY-A_2 proved
        spec = kappa_spectrum_k3()
        assert spec.kappa_cat == Fraction(2)
        assert spec.kappa_ch == Fraction(2)
        assert spec.kappa_bkm == Fraction(12)  # weight of Delta(tau) = eta^{24}
        assert spec.kappa_fiber == Fraction(24)

    def test_k3_kappa_cat_equals_kappa_ch(self):
        """At d=2: kappa_cat = kappa_ch (Proposition kappa-cat-chi-cy)."""
        # VERIFIED [DC] CY-D [LT] proved at d=2
        spec = kappa_spectrum_k3()
        assert spec.kappa_cat == spec.kappa_ch

    def test_verify_kappa_spectrum_five_paths(self):
        """Full five-path verification of the kappa-spectrum."""
        # VERIFIED [DC] five independent paths [LT] cross-check consistency
        result = verify_kappa_spectrum_k3xe()
        assert result['all_paths_pass']
        assert result['spectrum'] == {
            'kappa_cat': 0,
            'kappa_ch': 0,
            'kappa_ch_Heis': 3,
            'kappa_bkm': 5,
            'kappa_fiber': 24,
        }


# ===========================================================================
# SECTION 2: WEIGHT FORMULAS
# ===========================================================================

class TestWeightFormulas:
    """Verify the four weight formulas W1-W4."""

    def test_W1_lattice_voa_rank24(self):
        """W1: lattice VOA rank 24 -> wt = 12."""
        # VERIFIED [DC] lattice VOA [LT] eta^{24} has weight 12
        wf = weight_formula_lattice_voa(24)
        assert wf.weight == Fraction(12)

    def test_W1_lattice_voa_rank8(self):
        """W1: lattice VOA rank 8 -> wt = 4."""
        # VERIFIED [DC] E_8 lattice VOA [LT] eta^8 has weight 4
        wf = weight_formula_lattice_voa(8)
        assert wf.weight == Fraction(4)

    def test_W1_lattice_voa_rank1(self):
        """W1: Heisenberg (rank 1) -> wt = 1/2."""
        # VERIFIED [DC] Heisenberg [LT] eta has weight 1/2
        wf = weight_formula_lattice_voa(1)
        assert wf.weight == Fraction(1, 2)

    def test_W2_borcherds_c0_10(self):
        """W2: Borcherds lift with c(0)=10 -> wt = 5."""
        # VERIFIED [DC] Borcherds theorem [LT] Delta_5 weight
        wf = weight_formula_borcherds_lift(10)
        assert wf.weight == Fraction(5)

    def test_W2_borcherds_c0_12(self):
        """W2: Borcherds lift with c(0)=12 -> wt = 6."""
        # VERIFIED [DC] Borcherds theorem [LT] Eisenstein series weight
        wf = weight_formula_borcherds_lift(12)
        assert wf.weight == Fraction(6)

    def test_W3_chiral_obs_kappa3(self):
        """W3: chiral obstruction with kappa_ch=3 -> obs_1 weight = 3."""
        # VERIFIED [DC] Vol I Theorem D [LT] genus-1 obstruction
        wf = weight_formula_chiral_obs(Fraction(3))
        assert wf.weight == Fraction(3)

    def test_four_formulas_k3xe_distinct_weights(self):
        """Four weight formulas give three distinct weights for K3 x E."""
        # VERIFIED [DC] weight formula independence [LT] polysemy
        formulas = four_weight_formulas_k3xe()
        # W1: 12, W2: 5, W3: 3, W4: 5
        assert formulas['W1'].weight == Fraction(12)
        assert formulas['W2'].weight == Fraction(5)
        assert formulas['W3'].weight == Fraction(3)
        assert formulas['W4'].weight == Fraction(5)
        # W2 and W4 agree (both = kappa_BKM = 5)
        assert formulas['W2'].weight == formulas['W4'].weight
        # W1, W2, W3 are pairwise distinct
        assert formulas['W1'].weight != formulas['W2'].weight
        assert formulas['W1'].weight != formulas['W3'].weight
        assert formulas['W2'].weight != formulas['W3'].weight


# ===========================================================================
# SECTION 3: BRIDGE CHAIN
# ===========================================================================

class TestBridgeChain:
    """Verify the modular Koszul bridge chain for K3 x E."""

    def test_bridge_k3xe_steps(self):
        """Bridge has 5 steps: bar -> exponents -> phi01 -> lift -> chi10."""
        # VERIFIED [DC] chain structure [LT] bridge completeness
        bridge = bridge_k3xe()
        assert len(bridge.steps) == 5
        assert bridge.steps[0].step_number == 1
        assert bridge.steps[4].step_number == 5

    def test_bridge_k3xe_output_weight(self):
        """Bridge output weight = 5 (Delta_5)."""
        # VERIFIED [DC] Borcherds theorem [LT] Siegel form weight
        bridge = bridge_k3xe()
        assert bridge.output_weight == Fraction(5)

    def test_bridge_k3xe_conditional(self):
        """Steps 1-2 conditional on CY-A_3; steps 3-5 proved."""
        # VERIFIED [DC] conditionality [LT] AP-CY6 / AP-CY11
        bridge = bridge_k3xe()
        assert "CONDITIONAL" in bridge.steps[0].status
        assert "CONDITIONAL" in bridge.steps[1].status
        assert "PROVED" in bridge.steps[2].status
        assert "PROVED" in bridge.steps[3].status
        assert "PROVED" in bridge.steps[4].status

    def test_bridge_k3_generic_proved(self):
        """Generic K3 (d=2) bridge is fully proved."""
        # VERIFIED [DC] CY-A_2 [LT] unconditional at d=2
        bridge = bridge_k3_generic()
        assert bridge.output_weight == Fraction(12)
        assert "PROVED" in bridge.overall_status
        for step in bridge.steps:
            assert "PROVED" in step.status

    def test_bridge_k3_generic_3_steps(self):
        """Generic K3 bridge has 3 steps (simpler than K3 x E)."""
        # VERIFIED [DC] chain structure [LT] d=2 simplification
        bridge = bridge_k3_generic()
        assert len(bridge.steps) == 3

    def test_verify_bridge_chain(self):
        """Full bridge chain verification passes."""
        # VERIFIED [DC] chain consistency [LT] reconstruction success
        result = verify_bridge_chain_k3xe()
        assert result['output_weight'] == 5
        assert result['reconstruction']['phi01_match']
        assert result['reconstruction']['borcherds_weight'] == 5
        assert result['reconstruction']['disc_constraint']
        assert result['verification_passed']


# ===========================================================================
# SECTION 4: RECONSTRUCTION FROM BAR DATA
# ===========================================================================

class TestReconstruction:
    """Verify reconstruction of Delta_5 from bar complex exponents."""

    def test_phi01_coefficients_match(self):
        """Bar exponents reconstruct phi_{0,1} coefficients correctly."""
        # VERIFIED [DC] phi_{0,1} table [LT] EZ convention (AP-CY9)
        recon = reconstruct_delta5_from_bar_exponents(max_degree=8)
        assert recon['phi01_match']

    def test_c_minus1_equals_1(self):
        """c(-1) = 1 for normalized phi_{0,1}; Z_K3 = 2*phi_{0,1} has 2*c(-1) = 2."""
        # VERIFIED [DC] phi01_fourier [LT] polar coefficient
        recon = reconstruct_delta5_from_bar_exponents(max_degree=5)
        assert recon['c_table'][-1] == 1

    def test_c0_equals_10(self):
        """c(0) = 10 -> Borcherds weight = 5."""
        # VERIFIED [DC] phi_{0,1} [LT] BKM weight determination
        recon = reconstruct_delta5_from_bar_exponents(max_degree=5)
        assert recon['c_table'][0] == 10
        assert recon['borcherds_weight'] == Fraction(5)
        assert recon['borcherds_weight_int'] == 5

    def test_c3_equals_minus64(self):
        """c(3) = -64 (fermionic/odd roots, negative multiplicity)."""
        # VERIFIED [DC] phi_{0,1} [LT] BKM superalgebra odd roots
        recon = reconstruct_delta5_from_bar_exponents(max_degree=5)
        assert recon['c_table'][3] == -64

    def test_c4_equals_108(self):
        """c(4) = 108."""
        # VERIFIED [DC] phi_{0,1} [LT] discriminant D=4 coefficient
        recon = reconstruct_delta5_from_bar_exponents(max_degree=5)
        assert recon['c_table'][4] == 108

    def test_discriminant_constraint(self):
        """Discriminant constraint: c(D)!=0 only if D=0 or 3 mod 4 (AP-CY9)."""
        # VERIFIED [DC] index-1 constraint [LT] AP-CY9
        recon = reconstruct_delta5_from_bar_exponents(max_degree=8)
        assert recon['disc_constraint_ok']

    def test_reconstruction_successful(self):
        """Full reconstruction from bar data to Delta_5 succeeds."""
        # VERIFIED [DC] reconstruction chain [LT] bar-to-Siegel map
        recon = reconstruct_delta5_from_bar_exponents(max_degree=8)
        assert recon['reconstruction_successful']


# ===========================================================================
# SECTION 5: WEIGHT PUZZLE RESOLUTION
# ===========================================================================

class TestWeightPuzzle:
    """Verify the resolution of kappa_ch_Heis=3 vs wt(Delta_5)=5."""

    def test_kappa_ch_heis_equals_3(self):
        """kappa_ch_Heis(K3 x E) = 3; compact kappa_ch=0."""
        # VERIFIED [DC] chiral de Rham [LT] additivity
        res = resolve_weight_puzzle_k3xe()
        assert res.kappa_ch == Fraction(0)
        assert res.kappa_ch_Heis == Fraction(3)

    def test_borcherds_weight_equals_5(self):
        """wt(Delta_5) = 5 (Borcherds)."""
        # VERIFIED [DC] Borcherds theorem [LT] c(0)/2
        res = resolve_weight_puzzle_k3xe()
        assert res.borcherds_weight == Fraction(5)

    def test_mismatch_acknowledged(self):
        """kappa_ch_Heis != wt(Delta_5) is a feature, not a bug."""
        # VERIFIED [DC] polysemy [LT] AP113 kappa-spectrum
        res = resolve_weight_puzzle_k3xe()
        assert res.mismatch
        assert res.kappa_ch_Heis != res.borcherds_weight

    def test_genus1_obstruction_weight(self):
        """Genus-1 obstruction weight = kappa_ch_Heis = 3 (not 5)."""
        # VERIFIED [DC] Vol I Theorem D [LT] genus-1 shadow
        res = resolve_weight_puzzle_k3xe()
        assert res.genus1_obstruction_weight == Fraction(3)

    def test_siegel_form_weight(self):
        """Siegel form weight = 5 (from Borcherds, not from kappa_ch)."""
        # VERIFIED [DC] Borcherds theorem [LT] Siegel weight
        res = resolve_weight_puzzle_k3xe()
        assert res.siegel_form_weight == Fraction(5)

    def test_verify_weight_puzzle(self):
        """Full weight puzzle verification passes."""
        # VERIFIED [DC] resolution validity [LT] five-check consistency
        result = verify_weight_puzzle_resolution()
        assert result['resolution_valid']
        assert result['kappa_ch'] == 0
        assert result['kappa_ch_Heis'] == 3
        assert result['borcherds_weight'] == 5
        assert result['c0_value'] == 10
        assert result['c0_over_2'] == 5


# ===========================================================================
# SECTION 6: d=2 vs d=3 COMPARISON
# ===========================================================================

class TestD2vsD3:
    """Compare the bridge at d=2 (K3) and d=3 (K3 x E)."""

    def test_weights_differ(self):
        """d=2 weight (12) != d=3 weight (5)."""
        # VERIFIED [DC] dimension comparison [LT] weight formula difference
        comp = compare_d2_d3()
        assert comp.weight_d2 == Fraction(12)
        assert comp.weight_d3 == Fraction(5)
        assert comp.weight_d2 != comp.weight_d3

    def test_kappas_differ(self):
        """d=2 kappa_ch (2) differs from compact d=3 kappa_ch (0) and Heis (3)."""
        # VERIFIED [DC] dimension comparison [LT] kappa additivity
        comp = compare_d2_d3()
        assert comp.kappa_ch_d2 == Fraction(2)
        assert comp.kappa_ch_d3 == Fraction(0)
        assert comp.kappa_ch_Heis_d3 == Fraction(3)
        assert comp.kappa_ch_d2 != comp.kappa_ch_d3
        assert comp.kappa_ch_d2 != comp.kappa_ch_Heis_d3

    def test_d2_proved(self):
        """d=2 bridge is PROVED."""
        # VERIFIED [DC] CY-A_2 [LT] unconditional
        comp = compare_d2_d3()
        assert "PROVED" in comp.status_d2

    def test_d3_conditional(self):
        """d=3 bridge is CONDITIONAL on CY-A_3."""
        # VERIFIED [DC] AP-CY6 [LT] conditionality
        comp = compare_d2_d3()
        assert "CONDITIONAL" in comp.status_d3

    def test_d2_weight_formula_W1(self):
        """d=2 uses weight formula W1: wt = rank/2."""
        # VERIFIED [DC] lattice VOA [LT] 1D bar Euler suffices at d=2
        comp = compare_d2_d3()
        assert "rank" in comp.weight_formula_d2 or "24/2" in comp.weight_formula_d2

    def test_d3_weight_formula_W2(self):
        """d=3 uses weight formula W2: wt = c(0)/2."""
        # VERIFIED [DC] Borcherds [LT] 3D root data needed at d=3
        comp = compare_d2_d3()
        assert "c(0)" in comp.weight_formula_d3 or "10/2" in comp.weight_formula_d3

    def test_verify_d2_vs_d3(self):
        """Full d=2 vs d=3 comparison passes."""
        # VERIFIED [DC] comparison consistency [LT] eta^{24} and Ramanujan tau
        result = verify_d2_vs_d3_comparison()
        assert result['d2']['eta24_verified']
        assert result['d2']['ramanujan_tau_verified']
        assert result['weights_differ']
        assert result['kappas_differ']


# ===========================================================================
# SECTION 7: FOUR OBSTRUCTIONS
# ===========================================================================

class TestFourObstructions:
    """Verify the four obstructions separating shadow tower from Phi_10."""

    def test_O2_kappa_mismatch(self):
        """O2: kappa_ch_Heis = 3 != kappa_BKM = 5."""
        # VERIFIED [DC] kappa-spectrum [LT] AP113 polysemy
        result = verify_four_obstructions_k3xe()
        assert result['O2_kappa_mismatch']['mismatch']
        assert result['O2_kappa_mismatch']['kappa_ch'] == 0
        assert result['O2_kappa_mismatch']['kappa_ch_Heis'] == 3
        assert result['O2_kappa_mismatch']['kappa_bkm'] == 5

    def test_O4_schottky_codimension(self):
        """O4: Schottky obstruction codim = (g-2)(g-3)/2."""
        # VERIFIED [DC] Schottky [LT] moduli space codimension
        result = verify_four_obstructions_k3xe()
        assert result['O4_schottky']['g4_codim'] == 1
        assert result['O4_schottky']['g5_codim'] == 3
        assert result['O4_schottky']['g6_codim'] == 6

    def test_borcherds_bridges_all(self):
        """Borcherds lift bridges all four obstructions."""
        # VERIFIED [DC] bridge theorem [LT] thm:k3xe-shadow-cohft-igusa
        result = verify_four_obstructions_k3xe()
        assert result['borcherds_lift_bridges_all']


# ===========================================================================
# SECTION 8: CROSS-CHECKS WITH EXISTING ENGINES
# ===========================================================================

class TestCrossChecks:
    """Cross-checks against existing compute/lib infrastructure."""

    def test_kappa_ch_matches_modular_cy(self):
        """kappa_ch_Heis = 3 matches legacy modular_cy_characteristic.py."""
        # VERIFIED [DC] cross-engine [LT] consistency
        from compute.lib.modular_cy_characteristic import kappa_ch_k3_times_e
        assert kappa_ch_k3_times_e() == Fraction(3)
        spec = kappa_spectrum_k3xe()
        assert spec.kappa_ch == Fraction(0)
        assert spec.kappa_ch_Heis == kappa_ch_k3_times_e()

    def test_kappa_bkm_matches_modular_cy(self):
        """kappa_BKM = 5 matches modular_cy_characteristic.py."""
        # VERIFIED [DC] cross-engine [LT] consistency
        from compute.lib.modular_cy_characteristic import kappa_bkm_k3_times_e
        assert kappa_bkm_k3_times_e() == Fraction(5)
        spec = kappa_spectrum_k3xe()
        assert spec.kappa_bkm == kappa_bkm_k3_times_e()

    def test_eta24_matches_bar_euler(self):
        """eta^{24} from bar_euler_borcherds.py matches weight formula W1."""
        # VERIFIED [DC] cross-engine [LT] Ramanujan Delta consistency
        from compute.lib.bar_euler_borcherds import eta_power_coefficients
        eta24 = eta_power_coefficients(24, 5)
        # eta^{24} starts: 1, -24, 252, -1472, 4830, ...
        assert eta24[0] == 1
        assert eta24[1] == -24
        assert eta24[2] == 252

    def test_phi01_c0_matches_reconstruction(self):
        """c(0) = 10 from phi01_fourier.py matches reconstruction."""
        # VERIFIED [DC] cross-engine [LT] phi_{0,1} coefficient
        from compute.lib.phi01_fourier import phi01_by_discriminant
        c_table = phi01_by_discriminant(5)
        assert c_table[0] == 10
        recon = reconstruct_delta5_from_bar_exponents(max_degree=5)
        assert recon['c_table'][0] == 10

    def test_ramanujan_tau_matches_bar_euler(self):
        """Ramanujan tau(n) from bar_euler_borcherds.py is correct."""
        # VERIFIED [DC] cross-engine [LT] tau(2) = -24
        from compute.lib.bar_euler_borcherds import ramanujan_tau
        tau = ramanujan_tau(5)
        assert tau[1] == 1
        assert tau[2] == -24
        assert tau[3] == 252
