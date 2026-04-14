r"""Tests for k3_toroidal_verlinde_proof.py: K3 quantum toroidal no-Miki theorem,
charge-n dimensions, bar Euler PBW invariance, and root-of-unity Verlinde.

CENTRAL RESULTS:
    Part A (K3 quantum toroidal structure):
      (A1) No S_3 Miki: PROVED (4 independent legs, unconditional).
      (A2) Charge-n dim = p_{24}(n): PROVED (Gottsche 1990).
      (A3) Bar Euler product invariance from PBW flatness: PROVED (theorem).
           Application to K3 deformation family: CONJECTURAL (AP-CY14).

    Part B (chiral Verlinde at root of unity):
      (B1) K3 truncation at q = e^{2*pi*i/N}: CONJECTURAL (AP-CY5, AP-CY14).
      (B2) K3 Verlinde genus-1 = p_{24}(N): CONJECTURAL (AP-CY14).
      (B3) MTC from abelian factorisation: CONJECTURAL (AP-CY14).

Manuscript references:
    k3_times_e.tex, subsec:k3-quantum-toroidal
    k3_times_e.tex, prop:k3-qt-no-s3-miki
    en_factorization.tex, subsec:toroidal-from-k3xe
    en_factorization.tex, conj:miki-from-e3

Test structure:
    Section 1: No-Miki theorem (16 tests)
    Section 2: Charge-n representation dimensions (10 tests)
    Section 3: PBW flatness / bar Euler invariance (12 tests)
    Section 4: Root-of-unity truncation (10 tests)
    Section 5: K3 Verlinde at root of unity (10 tests)
    Section 6: MTC analysis (8 tests)
    Section 7: Cross-engine consistency (8 tests)
    Section 8: Full verification suite (4 tests)
"""

import math

import numpy as np
import pytest

from compute.lib.k3_toroidal_verlinde_proof import (
    # Part A
    NoMikiProof,
    charge_n_dimensions,
    charge_n_character_table,
    PBWFlatnessProof,
    # Part B
    k3_toroidal_truncation,
    k3_truncation_table,
    k3_chiral_verlinde_root_of_unity,
    k3_verlinde_genus1_table,
    k3_mtc_analysis,
    # Verification
    verify_no_miki,
    verify_charge_dimensions,
    verify_pbw_flatness,
    verify_truncation_table,
    verify_verlinde_genus0,
    verify_verlinde_genus1,
    verify_mtc_structure,
    full_verification,
)

from compute.lib.k3_quantum_toroidal import (
    N_MUKAI,
    K3QuantumToroidalAlgebra,
    bar_euler_product_invariance,
)

from compute.lib.k3_yangian import (
    MUKAI_RANK,
    SIG_PLUS,
    SIG_MINUS,
)

from compute.lib.chiral_verlinde_formula import (
    chiral_verlinde,
    verlinde_3d_integer,
    _partition_number,
    _coloured_partition_number,
)


# =========================================================================
# Section 1: No-Miki theorem (16 tests)
# =========================================================================

class TestNoMikiTheorem:
    """Tests for the no-S_3 Miki theorem for the K3 quantum toroidal."""

    def test_leg1_geometric_k3_no_torus(self):
        """Leg 1: K3 has pi_1 = 0 and b_1 = 0, hence no torus action."""
        proof = NoMikiProof()
        leg = proof.leg1_geometric()
        assert leg['pi_1_k3'] == 0
        assert leg['b_1_k3'] == 0
        assert leg['sufficient'] is True

    def test_leg1_torus_dim_1(self):
        """Leg 1: The CY torus of K3 x E has dimension 1."""
        proof = NoMikiProof()
        leg = proof.leg1_geometric()
        assert leg['dim_torus_k3e'] == 1

    def test_leg2_weyl_order(self):
        """Leg 2: |W(T_E)| = 2 < 6 = |S_3|."""
        proof = NoMikiProof()
        leg = proof.leg2_algebraic()
        assert leg['weyl_k3e_order'] == 2
        assert leg['weyl_c3_order'] == 6
        assert leg['sufficient'] is True

    def test_leg2_s3_not_subgroup(self):
        """Leg 2: S_3 is NOT a subgroup of W(T_E) = Z/2Z."""
        proof = NoMikiProof()
        leg = proof.leg2_algebraic()
        assert leg['s3_is_subgroup_of_weyl'] is False

    def test_leg3_signature_obstruction(self):
        """Leg 3: Mukai signature (4,20) is not S_3-symmetric."""
        proof = NoMikiProof()
        leg = proof.leg3_parameter_count()
        assert leg['k3e_signature'] == (SIG_PLUS, SIG_MINUS)
        assert leg['k3e_s3_symmetric'] is False
        assert leg['sufficient'] is True

    def test_leg3_c3_is_s3_symmetric(self):
        """Leg 3: C^3 signature (3,0) IS S_3-symmetric (positive definite)."""
        proof = NoMikiProof()
        leg = proof.leg3_parameter_count()
        assert leg['c3_signature'] == (3, 0)
        assert leg['c3_s3_symmetric'] is True

    def test_leg4_rank_mismatch(self):
        """Leg 4: rank K(K3) = 24 != 2 = rank K(E)."""
        proof = NoMikiProof()
        leg = proof.leg4_representation()
        assert leg['rank_horizontal_k3'] == 24
        assert leg['rank_vertical_e'] == 2
        assert leg['ranks_match'] is False
        assert leg['sufficient'] is True

    def test_sl2z_exists(self):
        """The SL_2(Z) symmetry from MCG(E) does exist."""
        proof = NoMikiProof()
        sl2z = proof.sl2z_symmetry()
        assert sl2z['symmetry'] == 'SL_2(Z)'
        assert sl2z['acts_on_e_modulus'] is True
        assert sl2z['acts_on_mukai'] is False

    def test_all_four_legs_sufficient(self):
        """All four legs are independently sufficient."""
        proof = NoMikiProof()
        result = proof.full_proof()
        assert result['all_legs_sufficient'] is True
        assert result['n_legs'] == 4

    def test_full_proof_status(self):
        """The full proof status is PROVED."""
        proof = NoMikiProof()
        result = proof.full_proof()
        assert 'PROVED' in result['status']

    def test_ap_cy22_compliant(self):
        """The proof is AP-CY22 compliant."""
        proof = NoMikiProof()
        result = proof.full_proof()
        assert result['ap_cy22_compliant'] is True

    def test_c3_vs_k3_torus_dimensions(self):
        """C^3 has dim(T) = 2, K3 x E has dim(T) = 1."""
        proof = NoMikiProof()
        assert proof.dim_torus_c3 == 2
        assert proof.dim_torus_k3e == 1

    def test_n_mukai_is_24(self):
        """The Mukai rank is 24."""
        proof = NoMikiProof()
        assert proof.n_mukai == 24

    def test_sig_plus_minus(self):
        """Signature is (4, 20)."""
        proof = NoMikiProof()
        assert proof.sig_plus == 4
        assert proof.sig_minus == 20

    def test_weyl_labels(self):
        """Weyl group labels are correct."""
        proof = NoMikiProof()
        assert proof.weyl_c3 == 'S_3'
        assert proof.weyl_k3e == 'Z/2Z'

    def test_verify_no_miki_passes(self):
        """The verification function passes."""
        result = verify_no_miki()
        assert result['all_legs_sufficient'] is True


# =========================================================================
# Section 2: Charge-n representation dimensions (10 tests)
# =========================================================================

class TestChargeNDimensions:
    """Tests for charge-n representation dimensions = p_{24}(n)."""

    def test_p24_0_is_1(self):
        """p_{24}(0) = 1 (vacuum)."""
        result = charge_n_dimensions(max_n=0)
        assert result['dimensions'][0] == 1

    def test_p24_1_is_24(self):
        """p_{24}(1) = 24 (Mukai rank)."""
        # VERIFIED: [DC] computation, [LT] Gottsche (1990), OEIS A006922
        result = charge_n_dimensions(max_n=1)
        assert result['dimensions'][1] == 24

    def test_p24_2_is_324(self):
        """p_{24}(2) = 324."""
        result = charge_n_dimensions(max_n=2)
        assert result['dimensions'][2] == 324

    def test_p24_3_is_3200(self):
        """p_{24}(3) = 3200."""
        result = charge_n_dimensions(max_n=3)
        assert result['dimensions'][3] == 3200

    def test_p24_4_is_25650(self):
        """p_{24}(4) = 25650."""
        result = charge_n_dimensions(max_n=4)
        assert result['dimensions'][4] == 25650

    def test_p24_5_is_176256(self):
        """p_{24}(5) = 176256."""
        result = charge_n_dimensions(max_n=5)
        assert result['dimensions'][5] == 176256

    def test_p24_6_is_1073720(self):
        """p_{24}(6) = 1073720."""
        # VERIFIED: [LT] Gottsche (1990) Table 1
        result = charge_n_dimensions(max_n=6)
        assert result['dimensions'][6] == 1073720

    def test_gottsche_all_match(self):
        """All computed values match Gottsche's table."""
        result = charge_n_dimensions(max_n=6)
        assert result['all_match'] is True

    def test_character_table_structure(self):
        """Character table has correct structure."""
        table = charge_n_character_table(max_n=3)
        assert len(table) == 4  # n = 0, 1, 2, 3
        assert table[0]['dim'] == 1
        assert table[1]['dim'] == 24
        assert table[2]['dim'] == 324
        assert table[3]['dim'] == 3200

    def test_growth_rate_increasing(self):
        """p_{24}(n) is strictly increasing for n >= 1."""
        result = charge_n_dimensions(max_n=6)
        dims = result['dimensions']
        for i in range(2, len(dims)):
            assert dims[i] > dims[i - 1], f"p_24({i}) = {dims[i]} <= p_24({i-1}) = {dims[i-1]}"


# =========================================================================
# Section 3: PBW flatness / bar Euler invariance (12 tests)
# =========================================================================

class TestPBWFlatness:
    """Tests for the PBW flatness -> bar Euler invariance proof."""

    def test_step1_proved(self):
        """Step 1 (flatness) has PROVED status."""
        proof = PBWFlatnessProof()
        step = proof.step1_flatness()
        assert 'PROVED' in step['status']

    def test_step2_proved(self):
        """Step 2 (bar filtration) has PROVED status."""
        proof = PBWFlatnessProof()
        step = proof.step2_bar_filtration()
        assert 'PROVED' in step['status']

    def test_step3_proved(self):
        """Step 3 (spectral sequence) has PROVED status."""
        proof = PBWFlatnessProof()
        step = proof.step3_spectral_sequence()
        assert 'PROVED' in step['status']

    def test_step4_proved(self):
        """Step 4 (graded dimension) has PROVED status."""
        proof = PBWFlatnessProof()
        step = proof.step4_graded_dimension()
        assert 'PROVED' in step['status']

    def test_all_steps_proved(self):
        """All four steps have PROVED status."""
        proof = PBWFlatnessProof()
        result = proof.full_proof()
        assert result['all_steps_proved'] is True

    def test_rank_24(self):
        """The rank is 24 for K3."""
        proof = PBWFlatnessProof(rank=24)
        assert proof.rank == 24

    def test_eta24_coefficient_0(self):
        """eta^{24} coefficient c_0 = 1."""
        proof = PBWFlatnessProof()
        result = proof.numerical_verification()
        assert result['eta24_coefficients'][0] == 1

    def test_eta24_coefficient_1(self):
        """eta^{24} coefficient c_1 = -24."""
        # VERIFIED: [DC] direct expansion, [LT] Ramanujan tau function
        proof = PBWFlatnessProof()
        result = proof.numerical_verification()
        assert result['eta24_coefficients'][1] == -24

    def test_eta24_coefficient_2(self):
        """eta^{24} coefficient c_2 = 252."""
        proof = PBWFlatnessProof()
        result = proof.numerical_verification()
        assert result['eta24_coefficients'][2] == 252

    def test_eta24_coefficient_3(self):
        """eta^{24} coefficient c_3 = -1472."""
        proof = PBWFlatnessProof()
        result = proof.numerical_verification()
        assert result['eta24_coefficients'][3] == -1472

    def test_ramanujan_tau_match(self):
        """eta^{24} coefficients match Ramanujan tau function."""
        proof = PBWFlatnessProof()
        result = proof.numerical_verification()
        assert result['all_match'] is True

    def test_deformation_family_has_4_members(self):
        """The K3 deformation family has 4 members."""
        proof = PBWFlatnessProof()
        app = proof.application_k3()
        assert len(app['family']) == 4


# =========================================================================
# Section 4: Root-of-unity truncation (10 tests)
# =========================================================================

class TestRootOfUnityTruncation:
    """Tests for root-of-unity truncation of the K3 quantum toroidal."""

    def test_truncation_N2(self):
        """N=2: p_{24}(2) = 324 modules."""
        data = k3_toroidal_truncation(2)
        assert data['k3_verlinde_genus1'] == 324

    def test_truncation_N3(self):
        """N=3: p_{24}(3) = 3200 modules."""
        data = k3_toroidal_truncation(3)
        assert data['k3_verlinde_genus1'] == 3200

    def test_truncation_N4(self):
        """N=4: p_{24}(4) = 25650 modules."""
        data = k3_toroidal_truncation(4)
        assert data['k3_verlinde_genus1'] == 25650

    def test_yangian_modules_N2(self):
        """N=2: Yangian has p(2) = 2 modules per direction."""
        data = k3_toroidal_truncation(2)
        assert data['yangian_modules_per_direction'] == 2

    def test_yangian_modules_N3(self):
        """N=3: Yangian has p(3) = 3 modules per direction."""
        data = k3_toroidal_truncation(3)
        assert data['yangian_modules_per_direction'] == 3

    def test_yangian_modules_N4(self):
        """N=4: Yangian has p(4) = 5 modules per direction."""
        data = k3_toroidal_truncation(4)
        assert data['yangian_modules_per_direction'] == 5

    def test_truncation_table_increasing(self):
        """Module counts increase with N."""
        result = verify_truncation_table()
        assert result['increasing'] is True
        assert result['all_positive'] is True

    def test_truncation_table_has_5_entries(self):
        """Truncation table has entries for N = 2, ..., 6."""
        table = k3_truncation_table(max_N=6)
        assert len(table) == 5

    def test_truncation_conjectural(self):
        """All truncation results are CONJECTURAL."""
        data = k3_toroidal_truncation(3)
        assert 'CONJECTURAL' in data['proof_status']

    def test_invalid_N_raises(self):
        """N < 1 raises ValueError."""
        with pytest.raises(ValueError):
            k3_toroidal_truncation(0)


# =========================================================================
# Section 5: K3 Verlinde at root of unity (10 tests)
# =========================================================================

class TestK3Verlinde:
    """Tests for K3 chiral Verlinde numbers at root of unity."""

    def test_genus0_always_1(self):
        """V^{K3}_N(g=0) = 1 for all N (vacuum uniqueness)."""
        result = verify_verlinde_genus0()
        assert result['all_ok'] is True

    def test_genus1_N1(self):
        """V^{K3}_1(g=1) = p_{24}(1) = 24."""
        v = k3_chiral_verlinde_root_of_unity(1, g=1)
        assert v['verlinde_dim'] == 24

    def test_genus1_N2(self):
        """V^{K3}_2(g=1) = p_{24}(2) = 324."""
        v = k3_chiral_verlinde_root_of_unity(2, g=1)
        assert v['verlinde_dim'] == 324

    def test_genus1_N3(self):
        """V^{K3}_3(g=1) = p_{24}(3) = 3200."""
        v = k3_chiral_verlinde_root_of_unity(3, g=1)
        assert v['verlinde_dim'] == 3200

    def test_genus1_N4(self):
        """V^{K3}_4(g=1) = p_{24}(4) = 25650."""
        v = k3_chiral_verlinde_root_of_unity(4, g=1)
        assert v['verlinde_dim'] == 25650

    def test_genus1_table(self):
        """Genus-1 Verlinde table matches p_{24}."""
        table = k3_verlinde_genus1_table(max_N=5)
        assert table[1] == 24
        assert table[2] == 324
        assert table[3] == 3200
        assert table[4] == 25650
        assert table[5] == 176256

    def test_genus2_needs_s_matrix(self):
        """At genus >= 2, the S-matrix is needed (not computed)."""
        v = k3_chiral_verlinde_root_of_unity(3, g=2)
        assert v['verlinde_dim'] is None
        assert v['s_matrix_needed'] is True

    def test_s_matrix_factorises(self):
        """The S-matrix factorises over 24 Mukai directions (abelian)."""
        v = k3_chiral_verlinde_root_of_unity(3, g=1)
        assert v['abelian_factorisation'] is True
        assert v['s_matrix_factorises'] is True

    def test_verlinde_conjectural(self):
        """All root-of-unity Verlinde results are CONJECTURAL."""
        v = k3_chiral_verlinde_root_of_unity(3, g=1)
        assert 'CONJECTURAL' in v['proof_status']

    def test_invalid_g_raises(self):
        """Negative genus raises ValueError."""
        with pytest.raises(ValueError):
            k3_chiral_verlinde_root_of_unity(3, g=-1)


# =========================================================================
# Section 6: MTC analysis (8 tests)
# =========================================================================

class TestMTCAnalysis:
    """Tests for modular tensor category analysis at root of unity."""

    def test_mtc_N2_simples(self):
        """N=2: p_{24}(2) = 324 simple objects."""
        mtc = k3_mtc_analysis(2)
        assert mtc['n_simples'] == 324

    def test_mtc_N3_simples(self):
        """N=3: p_{24}(3) = 3200 simple objects."""
        mtc = k3_mtc_analysis(3)
        assert mtc['n_simples'] == 3200

    def test_mtc_N4_simples(self):
        """N=4: p_{24}(4) = 25650 simple objects."""
        mtc = k3_mtc_analysis(4)
        assert mtc['n_simples'] == 25650

    def test_mtc_semisimple(self):
        """K3 Heisenberg is class G -> semisimple truncation."""
        mtc = k3_mtc_analysis(3)
        assert mtc['semisimple'] is True
        assert mtc['shadow_class'] == 'G (free field)'

    def test_mtc_is_mtc(self):
        """Truncated category is an MTC (conjectural)."""
        mtc = k3_mtc_analysis(3)
        assert mtc['is_mtc'] is True

    def test_mtc_abelian_factorisation(self):
        """MTC factorises over 24 Mukai directions."""
        mtc = k3_mtc_analysis(3)
        assert mtc['abelian_factorisation'] is True

    def test_mtc_N1_trivial(self):
        """N < 2: trivial truncation (no MTC)."""
        mtc = k3_mtc_analysis(1)
        assert mtc['mtc_exists'] is False

    def test_verify_mtc_structure(self):
        """The MTC verification passes for N = 2, 3, 4."""
        result = verify_mtc_structure()
        assert result['all_ok'] is True


# =========================================================================
# Section 7: Cross-engine consistency (8 tests)
# =========================================================================

class TestCrossEngineConsistency:
    """Cross-checks between this engine and k3_quantum_toroidal.py / chiral_verlinde_formula.py."""

    def test_mukai_rank_consistent(self):
        """N_MUKAI = MUKAI_RANK = 24 across engines."""
        assert N_MUKAI == MUKAI_RANK == 24

    def test_bar_euler_consistent(self):
        """Bar Euler product from k3_quantum_toroidal.py matches PBW proof."""
        bar_euler = bar_euler_product_invariance()
        assert bar_euler['deformation_invariant'] is True
        assert bar_euler['equals_eta24'] is True

    def test_p24_consistent_with_qt_engine(self):
        """p_{24}(n) from this engine matches k3_quantum_toroidal.py Fock character."""
        alg = K3QuantumToroidalAlgebra(q_nome=0.1)
        fock = alg.fock_character_generating_function(max_n=5)

        dims = charge_n_dimensions(max_n=5)['dimensions']
        for n in range(6):
            assert fock[n] == dims[n], f"Mismatch at n={n}: {fock[n]} vs {dims[n]}"

    def test_partition_numbers_consistent(self):
        """Partition numbers match between engines."""
        # p(N) from chiral_verlinde_formula
        known = {1: 1, 2: 2, 3: 3, 4: 5, 5: 7}
        for N, expected in known.items():
            assert _partition_number(N) == expected

    def test_coloured_partitions_consistent(self):
        """2-coloured partition numbers are consistent."""
        # p_2(N) = coefficients of 1/prod(1-q^k)^2
        assert _coloured_partition_number(2, 1) == 2
        assert _coloured_partition_number(2, 2) == 5
        assert _coloured_partition_number(2, 3) == 10

    def test_verlinde_class_G_dim_1(self):
        """Class G Verlinde = 1 (from chiral_verlinde_formula.py)."""
        for g in range(5):
            v = chiral_verlinde('G', g)
            assert v['verlinde_dim'] == 1

    def test_3d_verlinde_k1_g1_is_2(self):
        """3d Verlinde at k=1, g=1 is 2 (from chiral_verlinde_formula.py)."""
        assert verlinde_3d_integer(1, 1) == 2

    def test_k3_dims_exceed_sl2_verlinde(self):
        """K3 Verlinde numbers vastly exceed sl_2 Verlinde numbers."""
        for N in range(2, 6):
            k3_v = k3_chiral_verlinde_root_of_unity(N, g=1)['verlinde_dim']
            sl2_v = verlinde_3d_integer(max(N - 2, 1), 1)
            assert k3_v > sl2_v, (
                f"N={N}: K3 Verlinde {k3_v} should exceed sl_2 Verlinde {sl2_v}"
            )


# =========================================================================
# Section 8: Full verification suite (4 tests)
# =========================================================================

class TestFullVerification:
    """Tests for the full verification suite."""

    def test_full_verification_runs(self):
        """full_verification() runs without error."""
        result = full_verification()
        assert 'part_a1_no_miki' in result
        assert 'part_a2_charge_dims' in result
        assert 'part_a3_pbw_flatness' in result
        assert 'part_b1_truncation' in result
        assert 'part_b2_genus0' in result
        assert 'part_b2_genus1' in result
        assert 'part_b3_mtc' in result

    def test_no_miki_passes(self):
        """Part A1 passes."""
        result = full_verification()
        assert result['part_a1_no_miki']['all_legs_sufficient'] is True

    def test_charge_dims_pass(self):
        """Part A2 passes."""
        result = full_verification()
        assert result['part_a2_charge_dims']['all_match'] is True

    def test_verlinde_genus1_passes(self):
        """Part B2 genus-1 passes."""
        result = full_verification()
        assert result['part_b2_genus1']['all_ok'] is True
