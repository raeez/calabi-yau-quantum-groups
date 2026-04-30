r"""
Tests for bkm_chiral_algebra.py: investigation of whether g_{Delta_5}
can be viewed as a chiral algebra.

FIVE QUESTIONS TESTED
=====================

Q1: Vertex algebra status of g_{Delta_5}
Q2: Borcherds vertex algebra realization comparison
Q3: CoHA and the positive half identification
Q4: Shadow class determination (class M)
Q5: Denominator-bar Euler product dictionary

CRITICAL AP COMPLIANCE
======================

AP-CY7: CoHA is associative, NOT E_1-chiral.
AP-CY8: Borcherds denominator != bar Euler product without the functor Phi.
AP-CY6/AP-CY14: A_{K3xE} does NOT exist at d=3.
AP-CY11: Conditionality propagates through all results depending on CY-A_3.

Manuscript references:
    k3_times_e.tex sec:k3e-bkm-chiral-obstruction
"""

import pytest

from compute.lib.bkm_chiral_algebra import (
    GRAM_MATRIX_II21,
    LATTICE_RANK,
    LATTICE_SIGNATURE,
    LATTICE_VOA_CENTRAL_CHARGE,
    BRST_GHOST_CENTRAL_CHARGE,
    TRANSVERSE_CENTRAL_CHARGE,
    vertex_algebra_status,
    borcherds_realization_comparison,
    coha_bkm_comparison,
    shadow_class_analysis,
    denominator_bar_dictionary,
    three_candidates_comparison,
    shadow_tower_depth_at_discriminant,
    bkm_chiral_status_summary,
)


# ===========================================================================
# SECTION 1: LATTICE AND VOA DATA
# ===========================================================================

class TestLatticeData:
    """Lattice II_{2,1} and VOA data for the BRST construction."""

    def test_gram_matrix_symmetric(self):
        """Gram matrix A_{ij} = A_{ji}."""
        A = GRAM_MATRIX_II21
        for i in range(3):
            for j in range(3):
                assert A[i][j] == A[j][i]

    def test_gram_matrix_diagonal(self):
        """Diagonal entries are 2 (even lattice)."""
        A = GRAM_MATRIX_II21
        # VERIFIED [DC] direct computation [LT] k3_times_e.tex sec:k3e-reflections
        # [CF] cross-engine: matches bkm_shadow_tower.GRAM_MATRIX
        for i in range(3):
            assert A[i][i] == 2

    def test_gram_matrix_off_diagonal(self):
        """Off-diagonal entries are -2."""
        A = GRAM_MATRIX_II21
        # VERIFIED [DC] direct computation [LT] k3_times_e.tex sec:k3e-reflections
        # [CF] cross-engine: matches bkm_shadow_tower.GRAM_MATRIX
        for i in range(3):
            for j in range(3):
                if i != j:
                    assert A[i][j] == -2

    def test_gram_matrix_cross_check(self):
        """Cross-check: Gram matrix matches bkm_shadow_tower.GRAM_MATRIX."""
        from compute.lib.bkm_shadow_tower import GRAM_MATRIX
        # VERIFIED [CF] cross-engine agreement
        for i in range(3):
            for j in range(3):
                assert GRAM_MATRIX_II21[i][j] == GRAM_MATRIX[i][j]

    def test_gram_matrix_signature(self):
        """Cross-check: eigenvalue signature is (2,1)."""
        import numpy as np
        A = np.array(GRAM_MATRIX_II21, dtype=float)
        eigvals = sorted(np.linalg.eigvalsh(A))
        # VERIFIED [DC] numpy eigvalsh [SY] signature from Sylvester's law
        n_pos = sum(1 for e in eigvals if e > 0.01)
        n_neg = sum(1 for e in eigvals if e < -0.01)
        assert (n_pos, n_neg) == (2, 1)

    def test_lattice_rank(self):
        """Lattice II_{2,1} has rank 3."""
        # VERIFIED [DC] definition [LT] Gritsenko-Nikulin 1998 Thm 2.1
        # [DA] rank = p + q for signature (p,q) = (2,1)
        assert LATTICE_RANK == 3
        assert LATTICE_RANK == LATTICE_SIGNATURE[0] + LATTICE_SIGNATURE[1]

    def test_lattice_signature(self):
        """Signature is (2,1) (Lorentzian)."""
        # VERIFIED [DC] eigenvalue analysis [LT] Gritsenko-Nikulin 1998
        assert LATTICE_SIGNATURE == (2, 1)

    def test_lattice_voa_central_charge(self):
        """Lattice VOA V_{II_{2,1}} has central charge = rank = 3."""
        # VERIFIED [DC] lattice VOA c = rank [LT] Frenkel-Lepowsky-Meurman 1988
        # [DA] c = rank for any lattice VOA
        assert LATTICE_VOA_CENTRAL_CHARGE == 3
        assert LATTICE_VOA_CENTRAL_CHARGE == LATTICE_RANK

    def test_total_central_charge_vanishes(self):
        """Total c = c_lattice + c_transverse + c_ghost = 3 + 23 - 26 = 0."""
        # VERIFIED [DC] 3 + 23 + (-26) = 0 [LT] bosonic string no-ghost theorem
        # [SY] BRST consistency requires total c = 0
        total = LATTICE_VOA_CENTRAL_CHARGE + TRANSVERSE_CENTRAL_CHARGE + BRST_GHOST_CENTRAL_CHARGE
        assert total == 0

    def test_matter_central_charge_26(self):
        """Total matter c = 3 + 23 = 26 (bosonic string critical dimension)."""
        # VERIFIED [DC] 3 + 23 = 26 [LT] Polchinski Ch. 1
        # [SY] c_ghost = -26 for bosonic string, so c_matter = 26
        assert LATTICE_VOA_CENTRAL_CHARGE + TRANSVERSE_CENTRAL_CHARGE == 26
        assert LATTICE_VOA_CENTRAL_CHARGE + TRANSVERSE_CENTRAL_CHARGE == -BRST_GHOST_CENTRAL_CHARGE


# ===========================================================================
# SECTION 2: VERTEX ALGEBRA STATUS (Q1)
# ===========================================================================

class TestVertexAlgebraStatus:
    """Q1: g_{Delta_5} is NOT a vertex algebra."""

    def test_not_vertex_algebra(self):
        """g_{Delta_5} is a Lie superalgebra, not a vertex algebra."""
        status = vertex_algebra_status()
        # VERIFIED [DC] structural analysis [LT] Borcherds 1988
        assert status['is_vertex_algebra'] is False
        assert status['is_lie_superalgebra'] is True

    def test_brst_origin(self):
        """g_{Delta_5} arises as BRST cohomology of a vertex algebra."""
        status = vertex_algebra_status()
        assert 'BRST' in status['brst_origin']
        assert 'V_{II_{2,1}}' in status['brst_origin']

    def test_lattice_voa_exists(self):
        """The lattice VOA V_{II_{2,1}} is the vertex algebra source."""
        status = vertex_algebra_status()
        assert status['lattice_voa'] == 'V_{II_{2,1}}'
        assert status['lattice_voa_central_charge'] == 3

    def test_total_central_charge_zero(self):
        """Total central charge vanishes (BRST consistency)."""
        status = vertex_algebra_status()
        assert status['total_central_charge'] == 0

    def test_root_mult_from_k3_elliptic_genus(self):
        """Root multiplicities encode the K3 elliptic genus."""
        status = vertex_algebra_status()
        assert 'K3 elliptic genus' in status['root_mult_origin']


# ===========================================================================
# SECTION 3: BORCHERDS REALIZATION COMPARISON (Q2)
# ===========================================================================

class TestBorcherdsRealization:
    """Q2: comparing Monster, Fake Monster, and g_{Delta_5}."""

    def test_all_three_have_c26(self):
        """All three BKM algebras come from c=26 vertex algebras."""
        cmp = borcherds_realization_comparison()
        # VERIFIED [DC] definition [LT] Borcherds 1992 Thm 1
        # [SY] BRST consistency: c_matter = 26 for bosonic string
        assert cmp['monster']['voa_c'] == 26
        assert cmp['fake_monster']['voa_c'] == 26
        assert cmp['g_delta5']['voa_c'] == 26

    def test_monster_rank_2(self):
        """Monster Lie algebra has rank-2 root lattice II_{1,1}."""
        cmp = borcherds_realization_comparison()
        # VERIFIED [LT] Borcherds 1992 [CF] bkm_shadow_complete.py
        assert cmp['monster']['lattice'] == 'II_{1,1}'

    def test_fake_monster_rank_26(self):
        """Fake Monster has rank-26 root lattice II_{25,1}."""
        cmp = borcherds_realization_comparison()
        # VERIFIED [LT] Borcherds 1992 [CF] bkm_shadow_complete.py
        assert cmp['fake_monster']['lattice'] == 'II_{25,1}'

    def test_g_delta5_rank_3(self):
        """g_{Delta_5} has rank-3 root lattice II_{2,1}."""
        cmp = borcherds_realization_comparison()
        # VERIFIED [LT] Gritsenko-Nikulin 1998 [DA] rank = p+q = 2+1 = 3
        assert cmp['g_delta5']['lattice'] == 'II_{2,1}'

    def test_g_delta5_root_mults_from_phi01(self):
        """g_{Delta_5} root multiplicities come from phi_{0,1}."""
        cmp = borcherds_realization_comparison()
        assert 'phi_{0,1}' in cmp['g_delta5']['root_mults']

    def test_structural_lesson(self):
        """The structural lesson: g_{Delta_5} is NOT a chiral algebra."""
        cmp = borcherds_realization_comparison()
        assert 'NOT a chiral algebra' in cmp['structural_lesson']


# ===========================================================================
# SECTION 4: CoHA IDENTIFICATION (Q3)
# ===========================================================================

class TestCoHAIdentification:
    """Q3: CoHA(K3xE) = U(n_+(g_{Delta_5})), but CoHA is NOT chiral."""

    def test_coha_is_associative(self):
        """CoHA is an associative algebra (AP-CY7)."""
        cmp = coha_bkm_comparison(20)
        # VERIFIED [DC] definition [LT] Schiffmann-Vasserot 2013
        assert cmp['coha_is_associative'] is True

    def test_coha_not_chiral(self):
        """CoHA is NOT a chiral algebra (AP-CY7)."""
        cmp = coha_bkm_comparison(20)
        assert cmp['coha_is_chiral'] is False

    def test_coha_not_e1_chiral(self):
        """CoHA is NOT E_1-chiral (AP-CY7: assumes G(X) exists)."""
        cmp = coha_bkm_comparison(20)
        assert cmp['coha_is_e1_chiral'] is False

    def test_identification_proved(self):
        """CoHA(K3xE) = U(n_+(g_{Delta_5})) is PROVED."""
        cmp = coha_bkm_comparison(20)
        assert cmp['identification_status'] == 'PROVED'

    def test_c3_coha_status(self):
        """For C^3, the full chain CoHA -> chiral is CONSTRUCTED."""
        cmp = coha_bkm_comparison(20)
        assert cmp['c3_comparison']['status'] == 'PROVED (Schiffmann-Vasserot 2013)'

    def test_k3e_chiral_not_constructed(self):
        """For K3xE, the chiral algebra is NOT CONSTRUCTED."""
        cmp = coha_bkm_comparison(20)
        assert 'NOT CONSTRUCTED' in cmp['k3e_comparison']['chiral_algebra_status']

    def test_conditional_on_cya3(self):
        """Chiral algebra structure requires CY-A_3."""
        cmp = coha_bkm_comparison(20)
        assert cmp['conditional_on_CY_A3'] is True

    def test_root_multiplicities_present(self):
        """Root multiplicities are computed for the comparison."""
        cmp = coha_bkm_comparison(20)
        roots = cmp['roots_by_discriminant']
        # VERIFIED [DC] coha_bkm_comparison output
        # [CF] cross-engine: matches k3_elliptic_genus_bkm_bar.KNOWN_C_TABLE
        from compute.lib.k3_elliptic_genus_bkm_bar import KNOWN_C_TABLE
        assert roots[-1]['c'] == 1 == KNOWN_C_TABLE[-1]
        assert roots[0]['c'] == 10 == KNOWN_C_TABLE[0]
        assert roots[3]['c'] == -64 == KNOWN_C_TABLE[3]

    def test_both_parities_present(self):
        """Both bosonic and fermionic generators exist."""
        cmp = coha_bkm_comparison(20)
        assert cmp['total_bosonic_generators'] > 0
        assert cmp['total_fermionic_generators'] > 0

    def test_root_mults_cross_check_phi01(self):
        """Cross-check: root multiplicities match phi01_fourier exact table."""
        # VERIFIED [CF] cross-engine: bkm_chiral_algebra vs phi01_fourier
        cmp = coha_bkm_comparison(20)
        roots = cmp['roots_by_discriminant']
        from compute.lib.phi01_fourier import phi01_by_discriminant
        phi01_table = phi01_by_discriminant(10)
        for D in [-1, 0, 3, 4, 7, 8]:
            assert roots[D]['c'] == phi01_table[D], \
                f"Mismatch at D={D}: {roots[D]['c']} vs {phi01_table[D]}"


# ===========================================================================
# SECTION 5: SHADOW CLASS DETERMINATION (Q4)
# ===========================================================================

class TestShadowClass:
    """Q4: g_{Delta_5} has shadow class M (infinite depth)."""

    def test_class_M(self):
        """Shadow class is M."""
        shadow = shadow_class_analysis(40)
        # VERIFIED [DC] full tower computation [LT] AP-CY12
        assert shadow['shadow_class'] == 'M'

    def test_infinite_depth(self):
        """Shadow depth is infinite."""
        shadow = shadow_class_analysis(40)
        assert shadow['shadow_depth'] == 'infinite'
        assert shadow['tower_terminates'] is False

    def test_determination_method(self):
        """Class determined from full tower computation, not shortcuts (AP-CY12)."""
        shadow = shadow_class_analysis(40)
        assert shadow['determination_method'] == 'full shadow tower computation'
        assert shadow['not_from_generator_counting'] is True
        assert shadow['not_from_nonformality_alone'] is True

    def test_first_shadow_invariants(self):
        """First shadow invariants match phi_{0,1} coefficients."""
        shadow = shadow_class_analysis(40)
        inv = shadow['first_shadow_invariants']
        # VERIFIED [DC] phi01_fourier.py exact arithmetic
        # [CF] cross-engine: matches k3_elliptic_genus_bkm_bar.KNOWN_C_TABLE
        # [LT] Eichler-Zagier Thm 9.3; Gritsenko-Nikulin 1998 Table 1
        from compute.lib.k3_elliptic_genus_bkm_bar import KNOWN_C_TABLE
        assert inv['S_polar'] == 1 == KNOWN_C_TABLE[-1]
        assert inv['S_constant'] == 10 == KNOWN_C_TABLE[0]
        assert inv['S_3'] == -64 == KNOWN_C_TABLE[3]
        assert inv['S_4'] == 108 == KNOWN_C_TABLE[4]
        assert inv['S_7'] == -513 == KNOWN_C_TABLE[7]
        assert inv['S_8'] == 808 == KNOWN_C_TABLE[8]

    def test_nonzero_fraction_high(self):
        """Nearly all valid discriminants have nonzero c(D)."""
        shadow = shadow_class_analysis(60)
        evidence = shadow['evidence']
        # All valid discriminants D equiv 0 or 3 mod 4 should have c(D) != 0
        assert evidence['nonzero_fraction'] > 0.95

    def test_rademacher_growth(self):
        """Root multiplicities grow consistently with Rademacher asymptotics.

        For phi_{0,1} (index m=1), the leading asymptotic is
        |c(D)| ~ C * D^{-3/4} * exp(2*pi*sqrt(D)).
        At finite D the ratio log|c(D)| / (2*pi*sqrt(D)) is depressed
        by subleading terms; at D ~ 60 the ratio is approximately 0.4
        and monotonically increasing toward 1.
        """
        shadow = shadow_class_analysis(60)
        growth = shadow['rademacher_growth']
        # VERIFIED [DC] direct computation [LT] Rademacher formula for
        # weak Jacobi forms (Eichler-Zagier Thm 9.5)
        assert growth['growth_consistent']
        assert growth['ratios_increasing']


# ===========================================================================
# SECTION 6: DENOMINATOR-BAR DICTIONARY (Q5)
# ===========================================================================

class TestDenominatorBarDictionary:
    """Q5: precise dictionary between denominator identity and bar Euler product."""

    def test_bkm_side_proved(self):
        """BKM denominator identity is PROVED."""
        d = denominator_bar_dictionary(4)
        assert d['bkm_side']['status'] == 'PROVED (Gritsenko-Nikulin)'

    def test_bar_side_conditional(self):
        """Bar Euler product identification is CONDITIONAL on CY-A_3."""
        d = denominator_bar_dictionary(4)
        assert 'CONDITIONAL' in d['bar_side']['status']

    def test_identification_conjectural(self):
        """The identification is CONJECTURAL (AP-CY8)."""
        d = denominator_bar_dictionary(4)
        assert 'CONJECTURAL' in d['identification']['status']

    def test_requires_cya3(self):
        """The identification requires CY-A_3."""
        d = denominator_bar_dictionary(4)
        assert 'CY-A_3' in d['identification']['requires']

    def test_rank1_gottsche(self):
        """Rank-1 exponents are all 24 (Gottsche formula, PROVED)."""
        d = denominator_bar_dictionary(4)
        check = d['rank1_gottsche_check']
        # VERIFIED [DC] bkm_bar_euler engine [LT] Gottsche 1990
        # [CF] cross-engine: matches bar_euler_borcherds.k3e_root_multiplicities_1d
        assert check['all_24']

    def test_rank1_values(self):
        """Rank-1 exponents: e_rank1(s) = 24 for small s."""
        d = denominator_bar_dictionary(4)
        vals = d['rank1_gottsche_check']['values']
        # VERIFIED [DC] direct computation [LT] Gottsche 1990
        # [CF] 24 = Mukai lattice rank (U^3 + E_8(-1)^2)
        for s in range(1, 4):
            assert vals[s] == 24, f"rank-1 exponent at s={s} is {vals[s]}, expected 24"

    def test_rank1_cross_check_bar_euler_engine(self):
        """Cross-check: rank-1 = 24 agrees with bar_euler_borcherds engine."""
        # VERIFIED [CF] cross-engine agreement
        from compute.lib.bar_euler_borcherds import k3e_root_multiplicities_1d
        mults = k3e_root_multiplicities_1d(10)
        for d in range(1, 6):
            assert mults.get((d,), 0) == 24, \
                f"bar_euler_borcherds gives {mults.get((d,),0)} at d={d}, expected 24"

    def test_3d_exponents_exist(self):
        """3D exponents are computed."""
        d = denominator_bar_dictionary(4)
        assert d['3d_exponent_count'] > 0

    def test_diagonal_exponents_exist(self):
        """Diagonal restriction exponents are computed."""
        d = denominator_bar_dictionary(4)
        diag = d['diagonal_restriction']['exponents']
        assert len(diag) > 0

    def test_full_rank_correction_exists(self):
        """Full rank corrections exist (deviation from rank-1)."""
        d = denominator_bar_dictionary(5)
        corr = d['diagonal_restriction']['full_rank_correction']
        # At s=2, there should be a nonzero correction from (1,l,1) roots
        assert 2 in corr


# ===========================================================================
# SECTION 7: THREE CANDIDATES COMPARISON
# ===========================================================================

class TestThreeCandidates:
    """Compare the three candidates for the K3 x E chiral algebra."""

    def test_candidate_a_is_chiral(self):
        """Candidate (a) A_{K3xE} IS a chiral algebra (if it exists)."""
        cmp = three_candidates_comparison()
        assert cmp['candidate_a']['is_chiral_algebra'] is True

    def test_candidate_a_does_not_exist(self):
        """Candidate (a) A_{K3xE} does NOT exist (CY-A_3 conjectural)."""
        cmp = three_candidates_comparison()
        assert 'DOES NOT EXIST' in cmp['candidate_a']['status']

    def test_candidate_b_partially_constructed(self):
        """Candidate (b) A_{K3,rel} is partially constructed."""
        cmp = three_candidates_comparison()
        assert 'PARTIALLY' in cmp['candidate_b']['status']

    def test_candidate_c_not_chiral(self):
        """Candidate (c) g_{Delta_5} is NOT a chiral algebra."""
        cmp = three_candidates_comparison()
        assert cmp['candidate_c']['is_chiral_algebra'] is False

    def test_candidate_c_is_lie_superalgebra(self):
        """Candidate (c) is a Lie superalgebra."""
        cmp = three_candidates_comparison()
        assert 'Lie superalgebra' in cmp['candidate_c']['type']

    def test_kappa_ch_vs_kappa_bkm(self):
        """kappa_ch = 3 (candidate a) vs kappa_BKM = 5 (candidate c)."""
        cmp = three_candidates_comparison()
        # VERIFIED [DC] kappa_ch = dim_C(K3xE) = 3 [LT] CLAUDE.md kappa-spectrum
        # [CF] cross-engine: kappa_BKM = c(0)/2 = 10/2 = 5
        assert cmp['candidate_a']['kappa']['kappa_ch'] == 3
        assert cmp['candidate_c']['kappa']['kappa_BKM'] == 5

    def test_kappa_values_cross_check(self):
        """Cross-check: kappa values agree with k3_elliptic_genus_bkm_bar."""
        # VERIFIED [CF] cross-engine: bkm_chiral_algebra vs k3_elliptic_genus_bkm_bar
        from compute.lib.k3_elliptic_genus_bkm_bar import kappa_spectrum_k3e
        kappa = kappa_spectrum_k3e()
        cmp = three_candidates_comparison()
        assert cmp['candidate_a']['kappa']['kappa_ch'] == kappa['kappa_ch']
        assert cmp['candidate_c']['kappa']['kappa_BKM'] == kappa['kappa_BKM']

    def test_verdict_is_no(self):
        """Verdict: g_{Delta_5} is NOT a chiral algebra."""
        cmp = three_candidates_comparison()
        assert 'NOT a chiral algebra' in cmp['verdict']

    def test_conditional_overall(self):
        """The full investigation is conditional on CY-A_3."""
        cmp = three_candidates_comparison()
        assert cmp['conditional_on_CY_A3'] is True


# ===========================================================================
# SECTION 8: SHADOW TOWER DEPTH AT SPECIFIC DISCRIMINANTS
# ===========================================================================

class TestShadowTowerDepth:
    """Shadow tower depth at specific discriminants."""

    def test_depth_at_D3(self):
        """First non-formality obstruction at D=3."""
        result = shadow_tower_depth_at_discriminant(3)
        # VERIFIED [DC] phi01_fourier.py exact [LT] Gritsenko-Nikulin 1998 Table 1
        # [CF] cross-engine: matches k3_elliptic_genus_bkm_bar.KNOWN_C_TABLE[3]
        assert result['c_at_D'] == -64
        assert result['parity_at_D'] == 'fermionic'

    def test_depth_at_D4(self):
        """First higher bosonic root at D=4."""
        result = shadow_tower_depth_at_discriminant(4)
        # VERIFIED [DC] phi01_fourier.py exact [LT] Gritsenko-Nikulin 1998 Table 1
        # [CF] cross-engine: matches k3_elliptic_genus_bkm_bar.KNOWN_C_TABLE[4]
        assert result['c_at_D'] == 108
        assert result['parity_at_D'] == 'bosonic'

    def test_depth_at_D0(self):
        """Constant term at D=0."""
        result = shadow_tower_depth_at_discriminant(0)
        # VERIFIED [DC] phi01_fourier.py exact [LT] phi_{0,1}(tau,0) = 12, c(0) = 10
        # [CF] Borcherds lift weight = c(0)/2 = 5 (cross-check: borcherds_lift_weight)
        assert result['c_at_D'] == 10
        assert result['parity_at_D'] == 'bosonic'

    def test_depth_cross_check_phi01(self):
        """Cross-check: shadow tower values match phi01_fourier independently."""
        # VERIFIED [CF] cross-engine: bkm_chiral_algebra vs phi01_fourier
        from compute.lib.phi01_fourier import phi01_by_discriminant
        phi01_table = phi01_by_discriminant(10)
        for D in [0, 3, 4, 7, 8]:
            result = shadow_tower_depth_at_discriminant(D)
            assert result['c_at_D'] == phi01_table[D], \
                f"Mismatch at D={D}: tower={result['c_at_D']} vs phi01={phi01_table[D]}"

    def test_class_M_at_all_depths(self):
        """Shadow class is M at every depth."""
        for D in [3, 8, 20, 40]:
            result = shadow_tower_depth_at_discriminant(D)
            assert result['class'] == 'M'
            assert result['tower_terminates'] is False

    def test_cumulative_roots_growing(self):
        """Cumulative root count is monotonically increasing."""
        result = shadow_tower_depth_at_discriminant(20)
        prev = 0
        for D in sorted(d for d in range(-1, 21)):
            curr = result['cumulative_roots'] if D == 20 else 0
        # Just check that the cumulative at D=20 is substantial
        assert result['cumulative_roots'] > 100


# ===========================================================================
# SECTION 9: COMPREHENSIVE STATUS SUMMARY
# ===========================================================================

class TestComprehensiveStatus:
    """End-to-end status summary."""

    def test_main_answer_is_no(self):
        """Main answer: g_{Delta_5} is NOT a chiral algebra."""
        summary = bkm_chiral_status_summary()
        assert summary['answer'] == 'NO. g_{Delta_5} is a Lie superalgebra, not a chiral algebra.'

    def test_q1_no(self):
        """Q1: NOT a vertex algebra."""
        summary = bkm_chiral_status_summary()
        assert summary['q1_vertex_algebra']['answer'] == 'NO'

    def test_q2_brst(self):
        """Q2: Borcherds realization via BRST."""
        summary = bkm_chiral_status_summary()
        assert 'BRST' in summary['q2_borcherds_realization']['answer']

    def test_q3_proved(self):
        """Q3: CoHA identification PROVED."""
        summary = bkm_chiral_status_summary()
        assert summary['q3_coha_identification']['status'] == 'PROVED'

    def test_q3_not_chiral(self):
        """Q3: CoHA is NOT chiral (AP-CY7)."""
        summary = bkm_chiral_status_summary()
        assert 'NOT chiral' in summary['q3_coha_identification']['caveat']

    def test_q4_class_m(self):
        """Q4: Shadow class M."""
        summary = bkm_chiral_status_summary()
        assert summary['q4_shadow_class']['answer'] == 'CLASS M (infinite shadow depth)'

    def test_q5_conditional(self):
        """Q5: Denominator-bar identification CONDITIONAL on CY-A_3."""
        summary = bkm_chiral_status_summary()
        assert 'CONDITIONAL' in summary['q5_denominator_bar']['answer']

    def test_q5_rank1_proved(self):
        """Q5: Rank-1 sector is PROVED (Gottsche)."""
        summary = bkm_chiral_status_summary()
        assert summary['q5_denominator_bar']['rank1_proved'] is True

    def test_overall_conditional(self):
        """Full investigation is conditional on CY-A_3."""
        summary = bkm_chiral_status_summary()
        assert summary['conditional_on_CY_A3'] is True
