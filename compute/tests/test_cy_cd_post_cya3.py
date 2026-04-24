r"""Tests for cy_cd_post_cya3.py: CY-C and CY-D reassessment after CY-A_3.

STATUS: Mixed. CY-C remains CONJECTURED (AP-CY14); CY-D at d=2 is PROVED.
Tests verify internal consistency of the reassessment and the logical
dependencies between CY-A, CY-C, and CY-D.

Test structure:
    Section 1: CY-A status verification -- 8 tests
    Section 2: CY-C status and conjectural depth -- 10 tests
    Section 3: CY-C at d=2, abelian K3 case -- 12 tests
    Section 4: CY-D status and kappa_ch definitions -- 12 tests
    Section 5: CY-D at d=3 assessment -- 10 tests
    Section 6: BFN route to CY-C at d=3 -- 8 tests
    Section 7: kappa-spectrum post CY-A_3 -- 8 tests
    Section 8: Shadow predictions from kappa_ch -- 6 tests
    Section 9: Full reassessment summary -- 10 tests

Total: 84 tests.

Multi-path verification:
    Path 1 (DC): direct computation of kappa values, spectrum data
    Path 2 (LT): comparison with literature (BZFN, BFN, Drinfeld)
    Path 3 (LC): limiting cases (d=1 trivial, d=2 proved)
    Path 4 (SY): consistency of status labels across theorems
    Path 5 (CF): cross-family with existing engines (76+93+80 tests)

Manuscript references:
    thm:cy-to-chiral-d3 (cy_to_chiral.tex): CY-A_3, ProvedHere
    conj:qg-realization (quantum_group_reps.tex): CY-C, Conjectured
    conj:qgf-cy-c (quantum_groups_foundations.tex): CY-C, Conjectured
    thm:cy-modular-characteristic (modular_trace.tex): CY-D, ProvedHere at d=2
    thm:cy-d-d2 (cy_categories.tex): CY-D_2, ProvedHere
    thm:bzfn (drinfeld_center.tex): BZFN theorem, ProvedElsewhere
"""

import pytest
from fractions import Fraction

from compute.lib.cy_cd_post_cya3 import (
    # Status tracking
    CY_A_STATUS,
    cy_a_status,
    cy_c_status,
    cy_c_conjectural_depth,
    cy_d_status,
    cy_d_definedness_post_cya3,
    # CY-C at d=2
    MUKAI_RANK,
    DRINFELD_DOUBLE_DIM_K3,
    KUMMER_H_POS,
    KUMMER_H_NEG,
    cy_c_assessment_d2_abelian,
    drinfeld_double_as_quantum_group,
    abelian_cy_c_chain,
    # CY-D
    KAPPA_CH_VALUES,
    kappa_ch_k3_times_e_additivity,
    kappa_ch_defined_post_cya3,
    kappa_ch_cy_d_d3_assessment,
    # BFN route
    cy_c_bfn_route_d3,
    three_route_post_cya3,
    # kappa-spectrum
    kappa_spectrum_k3xe_post_cya3,
    # Shadow
    shadow_predictions_d3,
    # Full reassessment
    full_reassessment_post_cya3,
)

F = Fraction


# =========================================================================
# Section 1: CY-A status verification
# =========================================================================

class TestCYAStatus:
    """Verify CY-A status at all dimensions."""

    def test_cya1_proved(self):
        """CY-A_1 is PROVED (trivial: E -> H_1)."""
        assert cy_a_status(1).claim == 'PROVED'

    def test_cya2_proved(self):
        """CY-A_2 is PROVED (thm:cy-to-chiral)."""
        assert cy_a_status(2).claim == 'PROVED'

    def test_cya3_proved(self):
        """CY-A_3 is PROVED (thm:cy-to-chiral-d3).

        # VERIFIED [DC] manuscript check [LT] cy_to_chiral.tex L3086
        """
        assert cy_a_status(3).claim == 'PROVED'

    def test_cya3_no_dependencies(self):
        """CY-A_3 has no unresolved dependencies."""
        assert cy_a_status(3).dependencies == ()

    def test_cya_all_proved(self):
        """All CY-A theorems (d=1,2,3) are PROVED."""
        for d in [1, 2, 3]:
            assert cy_a_status(d).claim == 'PROVED'

    def test_cya_invalid_dimension(self):
        """CY-A at d=4 raises ValueError."""
        with pytest.raises(ValueError):
            cy_a_status(4)

    def test_cya3_framing_hypothesis(self):
        """CY-A_3 notes mention chain-level S^3-framing."""
        assert 'S^3-framing' in cy_a_status(3).notes

    def test_cya3_e1_output(self):
        """CY-A_3 produces E_1-chiral algebra (not E_2)."""
        assert 'E_1' in cy_a_status(3).notes


# =========================================================================
# Section 2: CY-C status and conjectural depth
# =========================================================================

class TestCYCStatus:
    """Verify CY-C status and conjectural depth."""

    def test_cyc_d2_conjectured(self):
        """CY-C at d=2 is CONJECTURED (AP-CY14).

        Even with Phi(C) existing, C(C,q) is not constructed in general.
        """
        assert cy_c_status(2).claim == 'CONJECTURED'

    def test_cyc_d3_conjectured(self):
        """CY-C at d=3 is CONJECTURED.

        # VERIFIED [DC] manuscript check [LT] quantum_groups_foundations.tex
        """
        assert cy_c_status(3).claim == 'CONJECTURED'

    def test_cyc_d2_depends_on_cya2(self):
        """CY-C at d=2 depends on CY-A_2."""
        assert 'CY-A_2' in cy_c_status(2).dependencies

    def test_cyc_d3_depends_on_cya3(self):
        """CY-C at d=3 depends on CY-A_3."""
        assert 'CY-A_3' in cy_c_status(3).dependencies

    def test_cyc_depth_d2_unchanged(self):
        """CY-C at d=2: conjectural depth unchanged (CY-A_2 was already proved)."""
        depth = cy_c_conjectural_depth(2)
        assert depth['depth_before_cya3'] == 1
        assert depth['depth_after_cya3'] == 1

    def test_cyc_depth_d3_reduced(self):
        """CY-C at d=3: conjectural depth reduced from 2 to 1.

        Before CY-A_3: doubly conjectural (Phi_3 + C(C,q)).
        After CY-A_3: singly conjectural (just C(C,q)).
        """
        depth = cy_c_conjectural_depth(3)
        assert depth['depth_before_cya3'] == 2
        assert depth['depth_after_cya3'] == 1

    def test_cyc_d3_resolved_conjecture(self):
        """CY-A_3 resolved the Phi_3 existence conjecture."""
        depth = cy_c_conjectural_depth(3)
        assert 'Phi_3 existence' in depth['resolved_by_cya3'][0]

    def test_cyc_d3_remaining_conjecture(self):
        """Only C(C,q) existence remains open at d=3."""
        depth = cy_c_conjectural_depth(3)
        assert depth['open_conjectures'] == ['C(C,q) existence']

    def test_cyc_invalid_dimension(self):
        """CY-C at d=1 raises ValueError (not defined)."""
        with pytest.raises(ValueError):
            cy_c_status(1)

    def test_cyc_d3_singly_conjectural(self):
        """CY-C at d=3 is now singly conjectural."""
        depth = cy_c_conjectural_depth(3)
        assert 'singly' in depth['change']


# =========================================================================
# Section 3: CY-C at d=2, abelian K3 case
# =========================================================================

class TestCYCD2Abelian:
    """CY-C at d=2 for the abelian K3 Yangian: D(H_Muk)."""

    def test_candidate_is_drinfeld_double(self):
        """Candidate quantum group is D(H_Muk)."""
        assessment = cy_c_assessment_d2_abelian()
        assert assessment.candidate_name == 'D(H_Muk)'

    def test_candidate_is_hopf(self):
        """D(H_Muk) is a Hopf algebra."""
        assessment = cy_c_assessment_d2_abelian()
        assert assessment.is_hopf_algebra is True

    def test_rep_braided(self):
        """Rep(D(H_Muk)) is braided monoidal."""
        assessment = cy_c_assessment_d2_abelian()
        assert assessment.rep_category_braided is True

    def test_abelian_match(self):
        """Rep^{E_2} matches for the abelian case."""
        assessment = cy_c_assessment_d2_abelian()
        assert 'YES' in assessment.rep_category_matches

    def test_bzfn_proved(self):
        """BZFN theorem is PROVED."""
        assessment = cy_c_assessment_d2_abelian()
        assert 'PROVED' in assessment.evidence['bzfn_theorem']

    def test_drinfeld_double_dim_49(self):
        """Drinfeld double has dimension 49 = 24 + 24 + 1.

        # VERIFIED [DC] generator count [LT] Kassel 1995
        """
        assert DRINFELD_DOUBLE_DIM_K3 == 49
        assert DRINFELD_DOUBLE_DIM_K3 == 2 * MUKAI_RANK + 1

    def test_drinfeld_double_is_quantum_group(self):
        """D(H_Muk) is a quasitriangular Hopf algebra = quantum group."""
        dd = drinfeld_double_as_quantum_group()
        assert dd['is_hopf'] is True
        assert dd['is_quasitriangular'] is True
        assert dd['status'] == 'PROVED'

    def test_drinfeld_double_ribbon(self):
        """D(H_Muk) has ribbon structure with twist -1 at charge 1."""
        dd = drinfeld_double_as_quantum_group()
        assert dd['ribbon'] is True
        assert dd['ribbon_twist_charge_1'] == F(-1)

    def test_drinfeld_double_mukai_signature(self):
        """Mukai signature is (4, 20).

        # VERIFIED [LT] Mukai 1987
        """
        dd = drinfeld_double_as_quantum_group()
        assert dd['mukai_signature'] == (4, 20)

    def test_abelian_chain_all_proved(self):
        """All arrows in the abelian CY-C chain are PROVED."""
        chain = abelian_cy_c_chain()
        assert chain['all_arrows_proved'] is True

    def test_abelian_chain_three_arrows(self):
        """The chain has exactly 3 arrows."""
        chain = abelian_cy_c_chain()
        assert len(chain['arrows']) == 3

    def test_abelian_chain_status_proved(self):
        """Overall chain status is PROVED (abelian case).

        This is the content: CY-C at d=2, abelian, IS answered.
        D(H_Muk) is the quantum group, Rep(D(H_Muk)) = Rep^{E_2}(H_Muk).
        """
        chain = abelian_cy_c_chain()
        assert chain['status'] == 'PROVED'


# =========================================================================
# Section 4: CY-D status and kappa_ch definitions
# =========================================================================

class TestCYDStatus:
    """Verify CY-D status at all dimensions."""

    def test_cyd_d2_proved(self):
        """CY-D at d=2 is PROVED.

        # VERIFIED [DC] manuscript check [LT] modular_trace.tex L16-31
        """
        assert cy_d_status(2).claim == 'PROVED'

    def test_cyd_d3_conjectured(self):
        """CY-D at d=3 is CONJECTURED (kappa_ch defined, equality open)."""
        assert cy_d_status(3).claim == 'CONJECTURED'

    def test_cyd_d2_depends_on_cya2(self):
        """CY-D at d=2 depends on CY-A_2."""
        assert 'CY-A_2' in cy_d_status(2).dependencies

    def test_cyd_d3_depends_on_cya3(self):
        """CY-D at d=3 depends on CY-A_3."""
        assert 'CY-A_3' in cy_d_status(3).dependencies

    def test_kappa_ch_k3xe_additivity(self):
        """kappa_ch_Heis(K3 x E) = 3 by additivity: 2 + 1 = 3.

        # VERIFIED [DC] direct computation [LT] additivity
        """
        result = kappa_ch_k3_times_e_additivity()
        assert result['kappa_ch_K3xE'] == F(0)
        assert result['kappa_ch_Heis_K3xE'] == F(3)
        assert result['additivity_holds'] is True

    def test_kappa_ch_k3xe_no_cya3(self):
        """kappa_ch_Heis(K3 x E) = 3 does NOT require CY-A_3."""
        result = kappa_ch_k3_times_e_additivity()
        assert result['uses_cya3'] is False

    def test_kappa_ch_k3xe_dependencies(self):
        """kappa_ch additivity uses CY-A_2 + CY-A_1 only."""
        result = kappa_ch_k3_times_e_additivity()
        assert 'CY-A_2' in result['dependencies']
        assert 'CY-A_1' in result['dependencies']

    def test_kappa_ch_defined_d3(self):
        """kappa_ch is now defined at d=3 (CY-A_3 proved)."""
        result = cy_d_definedness_post_cya3()
        assert result['newly_defined_d3'] is True

    def test_kappa_ch_equality_d2_proved(self):
        """kappa_ch = chi^CY is proved at d=2."""
        result = cy_d_definedness_post_cya3()
        assert result['equality_proved']['d=2'] is True

    def test_kappa_ch_equality_d3_open(self):
        """kappa_ch = chi^CY is NOT proved at d=3."""
        result = cy_d_definedness_post_cya3()
        assert result['equality_proved']['d=3'] is False

    def test_kappa_ch_known_values(self):
        """Check all known kappa_ch values.

        # VERIFIED [DC] direct computation [LT] various sources
        """
        assert KAPPA_CH_VALUES['point'] == F(0)
        assert KAPPA_CH_VALUES['elliptic_curve'] == F(1)
        assert KAPPA_CH_VALUES['K3'] == F(2)
        assert KAPPA_CH_VALUES['K3_times_E'] == F(0)
        assert KAPPA_CH_VALUES['K3_times_E_Heis'] == F(3)
        assert KAPPA_CH_VALUES['C3'] == F(1)

    def test_kappa_ch_k3_is_chi_o_k3(self):
        """kappa_ch(K3) = chi(O_{K3}) = 2.

        chi(O_{K3}) = h^{0,0} - h^{0,1} + h^{0,2} = 1 - 0 + 1 = 2.
        # VERIFIED [DC] Hodge diamond [LT] K3 standard
        """
        assert KAPPA_CH_VALUES['K3'] == F(2)


# =========================================================================
# Section 5: CY-D at d=3 assessment
# =========================================================================

class TestCYDD3:
    """CY-D at d=3: kappa_ch = chi^CY assessment."""

    def test_c3_proved(self):
        """kappa_ch(C^3) = 1 = chi^CY: PROVED.

        # VERIFIED [DC] five-path verification [LT] thm:kappa-c3
        """
        result = kappa_ch_cy_d_d3_assessment()
        assert result['c3']['proved'] is True
        assert result['c3']['kappa_ch'] == F(1)
        assert result['c3']['chi_cy'] == F(1)

    def test_k3xe_proved(self):
        """Compact kappa_ch(K3 x E)=0; the Heisenberg shadow equals 3."""
        result = kappa_ch_cy_d_d3_assessment()
        assert result['k3xe']['proved'] is True
        assert result['k3xe']['kappa_ch'] == F(0)
        assert result['k3xe']['kappa_ch_Heis'] == F(3)
        assert result['k3xe']['chi_cy_compact'] == F(0)

    def test_quintic_open(self):
        """Quintic has a BCOV-shadow candidate; constructed kappa_ch is open."""
        result = kappa_ch_cy_d_d3_assessment()
        assert result['quintic']['proved'] is False
        assert result['quintic']['kappa_BCOV_shadow_conjectural'] == F(-25, 3)
        assert result['quintic']['kappa_ch_constructed'] is False

    def test_c3_match(self):
        """C^3: kappa_ch matches chi^CY."""
        result = kappa_ch_cy_d_d3_assessment()
        assert result['c3']['match'] is True

    def test_k3xe_match(self):
        """K3 x E: kappa_ch matches chi^CY."""
        result = kappa_ch_cy_d_d3_assessment()
        assert result['k3xe']['match'] is True

    def test_quintic_conjectural_match(self):
        """Quintic: BCOV-shadow candidate matches chi^CY candidate conjecturally."""
        result = kappa_ch_cy_d_d3_assessment()
        assert result['quintic']['match'] is True

    def test_quintic_chi_top_24(self):
        """Quintic: BCOV-shadow candidate = chi_top/24 = -25/3.

        # VERIFIED [DC] direct computation
        """
        assert F(-200, 24) == F(-25, 3)
        result = kappa_ch_cy_d_d3_assessment()
        assert result['quintic']['kappa_BCOV_shadow_conjectural'] == F(-25, 3)

    def test_k3xe_additivity_method(self):
        """K3 x E: proved by additivity."""
        result = kappa_ch_cy_d_d3_assessment()
        assert 'additivity' in result['k3xe']['method']

    def test_c3_five_path_method(self):
        """C^3: proved by five-path verification."""
        result = kappa_ch_cy_d_d3_assessment()
        assert 'five-path' in result['c3']['method']

    def test_status_summary_present(self):
        """Status summary present and describes d=3 situation."""
        result = kappa_ch_cy_d_d3_assessment()
        assert 'constructed kappa_ch is PROVED' in result['status_summary']
        assert 'BCOV-shadow candidate' in result['status_summary']
        assert 'conjectural' in result['status_summary']


# =========================================================================
# Section 6: BFN route to CY-C at d=3
# =========================================================================

class TestBFNRoute:
    """BFN Coulomb branch route to CY-C at d=3."""

    def test_comparison_well_defined(self):
        """Comparison between Phi_3(C) and A_hbar is well-defined.

        This is the key change from CY-A_3: both sides now exist.
        """
        result = cy_c_bfn_route_d3()
        assert result['comparison_well_defined'] is True

    def test_identification_conjectural(self):
        """The identification Phi_3(C) = A_hbar is still CONJECTURAL."""
        result = cy_c_bfn_route_d3()
        assert result['identification_status'] == 'CONJECTURAL'

    def test_three_routes_exist(self):
        """All three routes (CY-A, CoHA, BFN) are described."""
        result = cy_c_bfn_route_d3()
        assert 'a' in result['routes']
        assert 'b' in result['routes']
        assert 'c' in result['routes']

    def test_route_a_constructive(self):
        """Route (a) is now CONSTRUCTIVE (Phi_3 exists)."""
        result = cy_c_bfn_route_d3()
        assert 'CONSTRUCTIVE' in result['routes']['a']['status']

    def test_evidence_all_match(self):
        """All evidence categories match between routes."""
        result = cy_c_bfn_route_d3()
        assert result['evidence']['structure_function_match'] is True
        assert result['evidence']['fock_dimensions_match'] is True
        assert result['evidence']['unitarity'] is True
        assert result['evidence']['classical_limit_agree'] is True

    def test_three_route_comparison_constructive(self):
        """After CY-A_3, route (a) is constructive."""
        result = three_route_post_cya3()
        assert result['route_a_constructive'] is True

    def test_three_routes_all_agree(self):
        """All three routes agree on classical limit, Fock, structure fn."""
        result = three_route_post_cya3()
        assert result['all_classical_limits_agree'] is True
        assert result['all_fock_characters_agree'] is True
        assert result['all_structure_functions_agree'] is True

    def test_three_routes_kappa_ch_agree(self):
        """All three routes give kappa_ch = 2 for K3."""
        result = three_route_post_cya3()
        assert result['all_kappa_ch_agree'] is True
        assert result['kappa_ch_value'] == F(2)


# =========================================================================
# Section 7: kappa-spectrum post CY-A_3
# =========================================================================

class TestKappaSpectrum:
    """The four-kappa spectrum for K3 x E after CY-A_3."""

    def test_kappa_ch_slots(self):
        """compact kappa_ch(K3 x E)=0 and kappa_ch_Heis(K3 x E)=3 (AP113).

        # VERIFIED [DC] additivity [LT] kappa_spectrum_reconciliation.py
        """
        result = kappa_spectrum_k3xe_post_cya3()
        assert result['kappa_ch'] == F(0)
        assert result['kappa_ch_Heis'] == F(3)

    def test_kappa_bkm_5(self):
        """kappa_BKM(K3 x E) = 5 (Borcherds weight)."""
        result = kappa_spectrum_k3xe_post_cya3()
        assert result['kappa_BKM'] == F(5)

    def test_kappa_cat_total_0(self):
        """kappa_cat(K3 x E) = chi(O_{K3 x E}) = 0."""
        result = kappa_spectrum_k3xe_post_cya3()
        assert result['kappa_cat'] == F(0)

    def test_kappa_cat_fiber_2(self):
        """kappa_cat(K3 fiber) = chi(O_{K3}) = 2."""
        result = kappa_spectrum_k3xe_post_cya3()
        assert result['kappa_cat_fiber'] == F(2)

    def test_kappa_fiber_24(self):
        """kappa_fiber(K3 x E) = 24 (Mukai lattice rank)."""
        result = kappa_spectrum_k3xe_post_cya3()
        assert result['kappa_fiber'] == F(24)

    def test_resolved_distinct_values(self):
        """The public K3xE values are {0, 3, 5, 24}; 2 is auxiliary fiber data."""
        result = kappa_spectrum_k3xe_post_cya3()
        spectrum = result['spectrum']
        assert len(spectrum) == 4
        assert spectrum == {F(0), F(3), F(5), F(24)}
        assert result['auxiliary_fiber_values'] == {F(2)}

    def test_kappa_ch_proved(self):
        """compact kappa_ch = 0 and kappa_ch_Heis = 3 are both typed."""
        result = kappa_spectrum_k3xe_post_cya3()
        assert 'PROVED' in result['kappa_ch_status']
        assert 'PROVED' in result['kappa_ch_Heis_status']

    def test_kappa_bkm_conjectural(self):
        """kappa_BKM = 5 is CONJECTURAL."""
        result = kappa_spectrum_k3xe_post_cya3()
        assert 'CONJECTURAL' in result['kappa_BKM_status']

    def test_kappa_ch_independent_of_cya3(self):
        """The K3xE slot separation is independent of CY-A_3."""
        result = kappa_spectrum_k3xe_post_cya3()
        assert result['kappa_ch_cya3_independent'] is True


# =========================================================================
# Section 8: Shadow predictions from kappa_ch
# =========================================================================

class TestShadowPredictions:
    """Shadow amplitudes from kappa_ch at d=3."""

    def test_k3xe_f1(self):
        """F_1(K3 x E) = kappa_ch / 24 = 3/24 = 1/8.

        # VERIFIED [DC] direct computation
        """
        result = shadow_predictions_d3(F(3))
        assert result['F_1'] == F(1, 8)

    def test_c3_f1(self):
        """F_1(C^3) = kappa_ch / 24 = 1/24.

        # VERIFIED [DC] direct computation [LT] MacMahon function
        """
        result = shadow_predictions_d3(F(1))
        assert result['F_1'] == F(1, 24)

    def test_quintic_f1(self):
        """F_1(quintic) from the BCOV-shadow candidate is -25/72.

        # VERIFIED [DC] direct computation [LT] BCOV
        """
        result = shadow_predictions_d3(F(-25, 3))
        assert result['F_1'] == F(-25, 72)

    def test_shadow_defined(self):
        """Shadow amplitudes are DEFINED (CY-A_3 proved)."""
        result = shadow_predictions_d3(F(3))
        assert result['shadow_defined'] is True

    def test_dt_match_conjectural(self):
        """DT matching is CONJECTURAL."""
        result = shadow_predictions_d3(F(3))
        assert 'CONJECTURAL' in result['dt_match_status']

    def test_k3xe_f2(self):
        """F_2(K3 x E) = 7 * 3 / 5760 = 21/5760 = 7/1920.

        # VERIFIED [DC] direct computation
        """
        result = shadow_predictions_d3(F(3))
        assert result['F_2'] == F(7, 1920)


# =========================================================================
# Section 9: Full reassessment summary
# =========================================================================

class TestFullReassessment:
    """Full reassessment of CY-C and CY-D after CY-A_3."""

    def test_cya3_proved(self):
        """Summary reports CY-A_3 as PROVED."""
        result = full_reassessment_post_cya3()
        assert result['cy_a3_status'] == 'PROVED'

    def test_cyc_change(self):
        """CY-C change: d=3 doubly -> singly conjectural."""
        result = full_reassessment_post_cya3()
        assert 'doubly' in result['cy_c_change']
        assert 'singly' in result['cy_c_change']

    def test_cyd_change(self):
        """CY-D change: proved lanes are separated from candidate lanes."""
        result = full_reassessment_post_cya3()
        assert 'proved lanes separated' in result['cy_d_change']
        assert 'BCOV-shadow candidate' in result['cy_d_change']

    def test_kappa_ch_k3xe_proved(self):
        """Compact kappa_ch(K3 x E)=0; the Heisenberg shadow equals 3."""
        result = full_reassessment_post_cya3()
        assert result['kappa_ch_k3xe'] == F(0)
        assert result['kappa_ch_heis_k3xe'] == F(3)
        assert result['kappa_ch_k3xe_proved'] is True

    def test_kappa_ch_k3xe_no_cya3(self):
        """The K3 x E compact and Heisenberg scalars do not use CY-A_3."""
        result = full_reassessment_post_cya3()
        assert result['kappa_ch_k3xe_uses_cya3'] is False

    def test_abelian_cyc_proved(self):
        """Abelian CY-C (D(H_Muk)) is PROVED."""
        result = full_reassessment_post_cya3()
        assert result['cy_c_abelian_proved'] is True

    def test_full_cyc_open(self):
        """Full (non-abelian) CY-C is still OPEN."""
        result = full_reassessment_post_cya3()
        assert result['cy_c_full_open'] is True

    def test_new_capabilities(self):
        """CY-A_3 enables new capabilities."""
        result = full_reassessment_post_cya3()
        assert len(result['new_capabilities']) >= 3

    def test_still_open(self):
        """There are still open problems."""
        result = full_reassessment_post_cya3()
        assert len(result['still_open']) >= 3

    def test_supporting_tests(self):
        """Supporting test counts from existing engines are documented."""
        result = full_reassessment_post_cya3()
        assert result['supporting_tests']['chiral_qg_rep_category'] == 76
        assert result['supporting_tests']['bfn_coulomb_k3_yangian'] == 93
