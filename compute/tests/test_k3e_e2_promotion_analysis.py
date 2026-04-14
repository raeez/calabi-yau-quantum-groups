r"""Tests for k3e_e2_promotion_analysis.py: E_2 promotion obstruction for K3 x E.

CENTRAL RESULTS TESTED:
    (1) Non-locality obstruction: >92% of global Drinfeld center is non-local.
    (2) MO stable envelope bypass: unconditional E_2 braiding from geometry.
    (3) Derived center HH^*(H_Muk): dim 325 = 1 + 24 + 300 (class G).
    (4) Drinfeld center != derived center (AP-CY4), same E_2 braiding (BZFN).
    (5) Three obstructions: symmetric braiding, center-hocolim, CY-A_3.
    (6) BKM character: ch(n_+)_1 = 24, ch(g)_1 = 1248.

Manuscript references:
    drinfeld_center.tex: rem:k3e-nonlocality-quantification,
        rem:mo-bypass-k3e, prop:derived-center-h-muk,
        rem:three-obstructions-k3e, rem:imaginary-root-nonlocality
    cy_to_chiral.tex: prop:center-hocolim (>92% claim),
        thm:e1-universality-cy3 (E_1 -> E_2 mechanism)

Anti-patterns checked:
    AP-CY3: E_2 != commutative (non-symmetric braiding).
    AP-CY4: Drinfeld center != derived center.
    AP-CY6: A_{K3xE} conditional on CY-A_3.
    AP113: kappa always subscripted.
    AP-CY11: Conditionality propagates.

Multi-path verification: at least 3 independent paths per major claim.
"""

import pytest
from fractions import Fraction

from compute.lib.k3e_e2_promotion_analysis import (
    # Constants
    MUKAI_RANK,
    MUKAI_SIG_PLUS,
    MUKAI_SIG_MINUS,
    BKM_CARTAN_DIM,
    # Non-locality obstruction
    NonLocalityData,
    bkm_nplus_character,
    bkm_full_character,
    local_center_character,
    compute_nonlocality_data,
    minimum_nonlocality_ratio,
    nonlocality_interpretation,
    # MO bypass
    MOBypassData,
    mo_bypass_analysis,
    mo_vs_center_comparison,
    # Derived center
    DerivedCenterData,
    derived_center_h_muk,
    derived_vs_drinfeld_comparison,
    # Three obstructions
    E2ObstructionData,
    three_obstructions,
    # Imaginary roots
    ImaginaryRootData,
    imaginary_root_analysis,
    # Verification
    verify_nonlocality_lower_bound,
    verify_derived_center_dimensions,
    verify_mo_bypass,
    verify_three_obstructions,
    verify_bkm_character_level1,
    verify_ap_compliance,
    full_verification,
)

F = Fraction


# =========================================================================
# Section 1: Constants
# =========================================================================

class TestConstants:
    """Verify fundamental constants of the Mukai lattice and BKM algebra."""

    def test_mukai_rank(self):
        """Mukai lattice has rank 24."""
        assert MUKAI_RANK == 24

    def test_mukai_signature(self):
        """Mukai signature is (4, 20)."""
        assert MUKAI_SIG_PLUS == 4
        assert MUKAI_SIG_MINUS == 20
        assert MUKAI_SIG_PLUS + MUKAI_SIG_MINUS == MUKAI_RANK

    def test_bkm_cartan_dim(self):
        """BKM Cartan has dim 26 = 24 + 2 (Mukai + hyperbolic)."""
        assert BKM_CARTAN_DIM == 26
        assert BKM_CARTAN_DIM == MUKAI_RANK + 2


# =========================================================================
# Section 2: BKM character computation
# =========================================================================

class TestBKMCharacter:
    """Verify the BKM character ch(n_+) and ch(g)."""

    def test_nplus_level0(self):
        """ch(n_+)_0 = 1 (vacuum)."""
        ch = bkm_nplus_character(5)
        assert int(ch[0]) == 1

    def test_nplus_level1(self):
        """ch(n_+)_1 = 24 (one real root per Mukai direction)."""
        ch = bkm_nplus_character(5)
        assert int(ch[1]) == 24

    def test_nplus_level2(self):
        """ch(n_+)_2 = 324 = C(25,2) + 24 = 300 + 24.

        Decomposition: 24 roots at level 1 can pair (C(25,2) = 300 multisets
        of size 2 from 24 items = Sym^2(C^{24})), plus 24 roots at level 2.
        Total: C(24+1, 2) + 24 = 300 + 24 = 324.
        """
        ch = bkm_nplus_character(5)
        assert int(ch[2]) == 324

    def test_full_bkm_level0(self):
        """ch(g)_0 = 26 (BKM Cartan dimension)."""
        ch = bkm_full_character(5)
        assert int(ch[0]) == BKM_CARTAN_DIM

    def test_full_bkm_level1(self):
        """ch(g)_1 = 1248.

        Derivation: ch(n_+)^2 at q^1 = 2 * 1 * 24 = 48.
        ch(g)_1 = 26 * 48 = 1248.
        """
        ch = bkm_full_character(5)
        assert int(ch[1]) == 1248

    def test_full_bkm_level1_decomposition(self):
        """Verify ch(g)_1 = BKM_CARTAN_DIM * 2 * ch(n_+)_1."""
        ch_n = bkm_nplus_character(5)
        expected = BKM_CARTAN_DIM * 2 * int(ch_n[1])
        ch_g = bkm_full_character(5)
        assert int(ch_g[1]) == expected

    def test_bkm_character_verification(self):
        """Full character verification via verify_bkm_character_level1."""
        result = verify_bkm_character_level1()
        assert result["all_pass"]


# =========================================================================
# Section 3: Non-locality obstruction
# =========================================================================

class TestNonLocalityObstruction:
    """Verify the >92% non-locality claim."""

    def test_nonlocality_data_structure(self):
        """compute_nonlocality_data returns correct structure."""
        data = compute_nonlocality_data(4)
        assert len(data) == 4
        assert all(isinstance(d, NonLocalityData) for d in data)

    def test_level0_z_hocolim(self):
        """Z(hocolim)_0 = 26 (BKM Cartan)."""
        data = compute_nonlocality_data(4)
        assert data[0].z_hocolim == BKM_CARTAN_DIM

    def test_level1_z_hocolim(self):
        """Z(hocolim)_1 = 1248."""
        data = compute_nonlocality_data(4)
        assert data[1].z_hocolim == 1248

    def test_level0_hocolim_z(self):
        """hocolim(Z)_0 = 1 (vacuum only from local charts)."""
        data = compute_nonlocality_data(4)
        assert data[0].hocolim_z == 1

    def test_obstruction_nonnegative(self):
        """Obstruction is non-negative at all levels."""
        data = compute_nonlocality_data(6)
        for d in data:
            assert d.obstruction >= 0, f"Negative obstruction at level {d.level}"

    def test_level0_obstruction(self):
        """Level 0 obstruction: 26 - 1 = 25."""
        data = compute_nonlocality_data(4)
        assert data[0].obstruction == 25

    def test_level0_ratio(self):
        """Level 0 ratio: 25/26."""
        data = compute_nonlocality_data(4)
        assert data[0].ratio == F(25, 26)

    def test_minimum_ratio_above_92_pct(self):
        """Minimum non-locality ratio across levels 1..5 exceeds 92%."""
        ratio = minimum_nonlocality_ratio(6)
        assert ratio > F(92, 100), (
            f"Non-locality ratio {float(ratio)*100:.1f}% is below 92%"
        )

    def test_nonlocality_verification(self):
        """Full non-locality verification path."""
        result = verify_nonlocality_lower_bound(6)
        assert result["all_above_92_pct"]
        assert result["minimum_ratio"] > 92.0

    def test_interpretation_fields(self):
        """Non-locality interpretation has required fields."""
        interp = nonlocality_interpretation()
        assert "center_exists" in interp
        assert "local_computation_fails" in interp
        assert "physical_meaning" in interp
        assert "ap_cy6_status" in interp

    def test_center_exists(self):
        """The center EXISTS (BKM algebra is well-defined)."""
        interp = nonlocality_interpretation()
        assert "YES" in interp["center_exists"]

    def test_local_computation_fails(self):
        """Local computation captures less than 8%."""
        interp = nonlocality_interpretation()
        assert "92%" in interp["local_computation_fails"]


# =========================================================================
# Section 4: MO stable envelope bypass
# =========================================================================

class TestMOBypass:
    """Verify the MO stable envelope bypass."""

    def test_structure_function_degree(self):
        """Structure function is degree (3,3) for CY_3."""
        mo = mo_bypass_analysis()
        assert mo.structure_function_degree == (3, 3)

    def test_self_dual_trivial(self):
        """In the self-dual limit h1 = -h2, g(u) = 1."""
        mo = mo_bypass_analysis()
        assert mo.self_dual_trivial

    def test_bypasses_center_hocolim(self):
        """MO bypasses the center-hocolim obstruction."""
        mo = mo_bypass_analysis()
        assert mo.bypasses_center_hocolim

    def test_hk_breaking(self):
        """Generic parameters break hyper-Kahler symmetry."""
        mo = mo_bypass_analysis(F(1), F(2))
        assert mo.breaks_hyper_kahler

    def test_self_dual_preserves_hk(self):
        """Self-dual parameters preserve hyper-Kahler."""
        mo = mo_bypass_analysis(F(1), F(-1))
        assert not mo.breaks_hyper_kahler

    def test_comparison_routes(self):
        """MO vs center comparison has both routes."""
        comp = mo_vs_center_comparison()
        assert "route_a_drinfeld_center" in comp
        assert "route_b_mo_stable_envelope" in comp
        assert "relationship" in comp
        assert "drinfeld_uniqueness" in comp

    def test_route_b_unconditional(self):
        """Route B (MO) is unconditional."""
        comp = mo_vs_center_comparison()
        assert "UNCONDITIONAL" in comp["route_b_mo_stable_envelope"]["status"]

    def test_route_a_conditional(self):
        """Route A (Drinfeld center) is conditional on CY-A_3."""
        comp = mo_vs_center_comparison()
        assert "CONDITIONAL" in comp["route_a_drinfeld_center"]["status"]

    def test_mo_verification(self):
        """Full MO verification path."""
        result = verify_mo_bypass()
        assert result["all_pass"]


# =========================================================================
# Section 5: Derived center HH^*(H_Muk)
# =========================================================================

class TestDerivedCenter:
    """Verify the derived center Z^{der}_{ch}(H_Muk) = HH^*(H_Muk, H_Muk)."""

    def test_hh0_dimension(self):
        """HH^0(H_Muk) = C, dim = 1 (unit)."""
        dc = derived_center_h_muk()
        assert dc.hh0_dim == 1

    def test_hh1_dimension(self):
        """HH^1(H_Muk) = C^{24}, dim = 24 (derivations)."""
        dc = derived_center_h_muk()
        assert dc.hh1_dim == 24

    def test_hh2_dimension(self):
        """HH^2(H_Muk) = Sym^2(C^{24}), dim = C(25,2) = 300."""
        dc = derived_center_h_muk()
        assert dc.hh2_dim == 300
        # Verify: Sym^2(C^r) = C(r+1, 2) = r(r+1)/2
        r = MUKAI_RANK
        assert dc.hh2_dim == r * (r + 1) // 2

    def test_total_dimension(self):
        """Total dim = 1 + 24 + 300 = 325."""
        dc = derived_center_h_muk()
        assert dc.total_dim == 325
        assert dc.total_dim == dc.hh0_dim + dc.hh1_dim + dc.hh2_dim

    def test_euler_characteristic(self):
        """chi(HH^*) = 1 - 24 + 300 = 277."""
        dc = derived_center_h_muk()
        assert dc.euler_characteristic == 277
        assert dc.euler_characteristic == dc.hh0_dim - dc.hh1_dim + dc.hh2_dim

    def test_shadow_class_g(self):
        """Heisenberg is class G (shadow depth 2)."""
        dc = derived_center_h_muk()
        assert dc.shadow_class == "G"
        assert dc.shadow_depth == 2

    def test_poincare_polynomial(self):
        """Poincare polynomial is 1 + 24t + 300t^2."""
        dc = derived_center_h_muk()
        assert "1 + 24t + 300t^2" in dc.poincare_polynomial

    def test_gerstenhaber_bracket(self):
        """Gerstenhaber bracket uses inverse Mukai pairing."""
        dc = derived_center_h_muk()
        assert "omega^{ij}" in dc.gerstenhaber_bracket

    def test_derived_center_verification(self):
        """Full derived center verification path."""
        result = verify_derived_center_dimensions()
        assert result["all_pass"]


# =========================================================================
# Section 6: AP-CY4 compliance: Drinfeld != derived center
# =========================================================================

class TestCenterDistinction:
    """Verify AP-CY4: Drinfeld center != derived center."""

    def test_dimensions_differ(self):
        """Drinfeld double has dim 49; derived center has dim 325."""
        comp = derived_vs_drinfeld_comparison()
        assert comp["derived_center_dim"] == 325
        assert comp["drinfeld_double_dim"] == 49
        assert comp["dimensions_differ"]

    def test_same_braided_category(self):
        """BZFN theorem: same E_2 braided category."""
        comp = derived_vs_drinfeld_comparison()
        assert comp["same_braided_category"]

    def test_matching_r_matrix(self):
        """R-matrix data matches across both centers."""
        comp = derived_vs_drinfeld_comparison()
        invariants = comp["matching_invariants"]
        assert "omega" in invariants["r_matrix_exponent"].lower()

    def test_matching_shadow_class(self):
        """Shadow class G matches."""
        comp = derived_vs_drinfeld_comparison()
        assert comp["matching_invariants"]["shadow_class"] == "G"

    def test_ap_cy4_compliant(self):
        """The comparison is AP-CY4 compliant."""
        comp = derived_vs_drinfeld_comparison()
        assert comp["ap_cy4_compliant"]


# =========================================================================
# Section 7: Three obstructions classification
# =========================================================================

class TestThreeObstructions:
    """Verify the three-obstruction classification."""

    def test_three_obstructions_count(self):
        """Exactly three obstructions classified."""
        obs = three_obstructions()
        assert len(obs) == 3

    def test_obstruction_types(self):
        """All three are E2ObstructionData."""
        obs = three_obstructions()
        assert all(isinstance(o, E2ObstructionData) for o in obs)

    def test_symmetric_braiding_obstruction(self):
        """First obstruction: E_3 gives symmetric braiding."""
        obs = three_obstructions()
        assert "symmetric" in obs[0].name.lower() or "symmetric" in obs[0].description.lower()
        assert obs[0].bypass_available

    def test_center_hocolim_obstruction(self):
        """Second obstruction: center-hocolim gap."""
        obs = three_obstructions()
        assert "hocolim" in obs[1].name.lower() or "hocolim" in obs[1].description.lower()
        assert obs[1].bypass_available
        assert "MO" in obs[1].bypass_method or "stable" in obs[1].bypass_method

    def test_cya3_obstruction(self):
        """Third obstruction: CY-A_3 dependence."""
        obs = three_obstructions()
        assert "CY-A" in obs[2].name or "CY-A" in obs[2].description
        assert not obs[2].bypass_available
        assert obs[2].severity == "HIGH"

    def test_three_obstructions_verification(self):
        """Full verification path."""
        result = verify_three_obstructions()
        assert result["all_pass"]


# =========================================================================
# Section 8: Imaginary root analysis
# =========================================================================

class TestImaginaryRoots:
    """Verify imaginary root analysis."""

    def test_real_root_multiplicity(self):
        """Real roots have mult 1 (c(-1) = 1 in EZ convention)."""
        ir = imaginary_root_analysis()
        assert ir.real_root_mult == 1

    def test_imaginary_root_multiplicity(self):
        """Imaginary roots have mult 10 (c(0) = 10 in EZ convention)."""
        ir = imaginary_root_analysis()
        assert ir.imaginary_root_mult == 10

    def test_real_roots_local(self):
        """Real roots are local."""
        ir = imaginary_root_analysis()
        assert "LOCAL" in ir.real_root_locality

    def test_imaginary_roots_nonlocal(self):
        """Imaginary roots are non-local."""
        ir = imaginary_root_analysis()
        assert "NON-LOCAL" in ir.imaginary_root_locality

    def test_level1_all_real(self):
        """At level 1, all roots are real (imaginary fraction = 0)."""
        ir = imaginary_root_analysis()
        assert ir.fraction_imaginary_level1 == F(0)


# =========================================================================
# Section 9: AP compliance
# =========================================================================

class TestAPCompliance:
    """Verify anti-pattern compliance."""

    def test_ap_cy3_e2_not_symmetric(self):
        """AP-CY3: E_2 braiding is NOT symmetric."""
        result = verify_ap_compliance()
        assert result["ap_cy3_e2_not_symmetric"]

    def test_ap_cy4_centers_differ(self):
        """AP-CY4: Drinfeld center != derived center."""
        result = verify_ap_compliance()
        assert result["ap_cy4_centers_differ"]

    def test_ap_cy4_same_braiding(self):
        """AP-CY4: same E_2 braided category despite different centers."""
        result = verify_ap_compliance()
        assert result["ap_cy4_same_e2_braiding"]

    def test_ap_cy6_conditional(self):
        """AP-CY6: A_{K3xE} is conditional."""
        result = verify_ap_compliance()
        assert result["ap_cy6_conditional_stated"]

    def test_ap113_kappa_subscripted(self):
        """AP113: kappa is always subscripted."""
        result = verify_ap_compliance()
        assert result["ap113_kappa_subscripted"]


# =========================================================================
# Section 10: Full verification suite
# =========================================================================

class TestFullVerification:
    """Run the comprehensive verification suite."""

    def test_full_verification_all_paths(self):
        """All six verification paths pass."""
        result = full_verification()
        for path_name, path_result in result.items():
            if "all_pass" in path_result:
                assert path_result["all_pass"], (
                    f"Verification path {path_name} failed: {path_result}"
                )

    def test_full_verification_has_six_paths(self):
        """Six independent verification paths."""
        result = full_verification()
        assert len(result) == 6


# =========================================================================
# Section 11: Cross-checks with existing engines
# =========================================================================

class TestCrossChecks:
    """Cross-check with drinfeld_center_k3_heisenberg.py and
    drinfeld_center_hocolim.py."""

    def test_mukai_rank_consistency(self):
        """MUKAI_RANK consistent with drinfeld_center_k3_heisenberg."""
        from compute.lib.drinfeld_center_k3_heisenberg import (
            MUKAI_RANK as MUKAI_RANK_K3H,
        )
        assert MUKAI_RANK == MUKAI_RANK_K3H

    def test_drinfeld_double_dim_49(self):
        """Drinfeld double dim 49 consistent with k3_heisenberg engine."""
        from compute.lib.drinfeld_center_k3_heisenberg import DRINFELD_DOUBLE_DIM
        assert DRINFELD_DOUBLE_DIM == 49
        # Our derived center has dim 325 (different, per AP-CY4)
        dc = derived_center_h_muk()
        assert dc.total_dim == 325
        assert dc.total_dim != DRINFELD_DOUBLE_DIM

    def test_bkm_character_consistency(self):
        """BKM ch(n_+) consistent with hocolim engine."""
        from compute.lib.drinfeld_center_hocolim import DrinfeldCenterK3EHocolim
        k3e = DrinfeldCenterK3EHocolim()
        ch_hocolim = k3e.bkm_character(5)
        ch_ours = bkm_nplus_character(5)
        for n in range(5):
            assert int(ch_hocolim[n]) == int(ch_ours[n]), (
                f"ch(n_+) mismatch at level {n}: "
                f"hocolim={int(ch_hocolim[n])}, ours={int(ch_ours[n])}"
            )

    def test_full_bkm_consistency(self):
        """Full BKM character consistent with hocolim engine."""
        from compute.lib.drinfeld_center_hocolim import DrinfeldCenterK3EHocolim
        k3e = DrinfeldCenterK3EHocolim()
        ch_hocolim = k3e.full_bkm_character(5)
        ch_ours = bkm_full_character(5)
        for n in range(5):
            assert int(ch_hocolim[n]) == int(ch_ours[n]), (
                f"ch(g) mismatch at level {n}: "
                f"hocolim={int(ch_hocolim[n])}, ours={int(ch_ours[n])}"
            )

    def test_mukai_signature_consistency(self):
        """Mukai signature (4,20) consistent with k3_heisenberg."""
        from compute.lib.drinfeld_center_k3_heisenberg import (
            MUKAI_SIG_PLUS as MSP,
            MUKAI_SIG_MINUS as MSM,
        )
        assert MUKAI_SIG_PLUS == MSP
        assert MUKAI_SIG_MINUS == MSM
