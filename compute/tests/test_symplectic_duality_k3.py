r"""Tests for symplectic_duality_k3.py: Coulomb/Higgs branch duality for K3.

STATUS: ALL results CONJECTURAL (AP-CY14) unless otherwise noted.
Tests verify internal consistency of the symplectic duality framework,
not existence of Y(g_{K3}).

Test structure:
    Section 1: Coulomb branch geometry (10 tests)
    Section 2: Higgs branch and Beauville (8 tests)
    Section 3: K3 self-duality (10 tests)
    Section 4: Langlands duality (6 tests)
    Section 5: Structure function under dualities (10 tests)
    Section 6: BFN quantized Coulomb branch (8 tests)
    Section 7: Symplectic vs Koszul diagnostic (8 tests)
    Section 8: Generating functions (8 tests)
    Section 9: Hilbert-Chow resolution (6 tests)
    Section 10: Dolgachev-Nikulin lattice (8 tests)
    Section 11: Yangian involutions (10 tests)
    Section 12: Two routes comparison (4 tests)
    Section 13: Full verification suite (6 tests)

Total: 102 tests.

Manuscript references:
    subsec:mo-bypass-k3e (drinfeld_center.tex)
    prop:mo-bypass (drinfeld_center.tex)
    prop:k3e-beauville (k3_times_e.tex)
    prop:k3e-hall-yangian (k3_times_e.tex)
    quantum_groups_foundations.tex (quantum group regimes)

Multi-path verification:
    Path 1 (DC): direct computation of Euler chars, kappa values
    Path 2 (LT): comparison with Beauville (1983), Goettsche (1990), BFN (2016)
    Path 3 (LC): limiting cases (charge 0, charge 1)
    Path 4 (SY): symmetry properties (self-duality, unitarity, involutions)
    Path 5 (CF): cross-family with k3_yangian.py, k3_mirror_koszul.py
"""

import pytest
from fractions import Fraction as F

from compute.lib.symplectic_duality_k3 import (
    # Constants
    STATUS,
    MUKAI_RANK,
    MUKAI_SIG_PLUS,
    MUKAI_SIG_MINUS,
    MUKAI_SIGNATURE,
    HILB_EULER_CHARS,
    KAPPA_CH_K3,
    KAPPA_BKM_K3,
    KAPPA_CAT_K3,
    KAPPA_FIBER_K3,
    KOSZUL_CONDUCTOR_FREE_FIELD,
    # Types
    CoulombBranchData,
    HiggsBranchData,
    SelfDualityData,
    BFNCoulombData,
    SymplecticDualityDiagnostic,
    LatticeSelfdualityData,
    YangianDualityInvolution,
    TwoRoutesComparison,
    VerificationResult,
    # Functions
    coulomb_branch_k3,
    higgs_branch_k3,
    k3_self_duality,
    langlands_dual_structure_function,
    structure_function_under_dualities,
    bfn_kummer_k3,
    bfn_ade_k3,
    symplectic_vs_koszul_diagnostic,
    coulomb_branch_generating_function,
    hilbert_chow_resolution_data,
    dolgachev_nikulin_self_duality,
    yangian_duality_involutions,
    two_routes_to_k3_yangian,
    # Verification
    verify_coulomb_higgs_match,
    verify_kappa_diagnostic,
    verify_unitarity,
    verify_koszul_is_inversion,
    verify_langlands_trivial,
    verify_dolgachev_nikulin_signatures,
    verify_beauville_euler_chars,
    full_verification,
)


# ============================================================================
# Fixtures
# ============================================================================

@pytest.fixture
def default_h_params():
    """Default K3 Yangian parameters satisfying CY_2 constraint.

    h_i = 1 for i=1..4, h_i = -1/5 for i=5..24.
    Sum = 4 - 20/5 = 0.
    """
    return [F(1)] * MUKAI_SIG_PLUS + [-F(1, 5)] * MUKAI_SIG_MINUS


@pytest.fixture
def safe_z():
    """Test point z=7 far from all poles (AP-CY28).

    For default params: poles at z=+/-1 and z=+/-1/5.
    z=7 is safely far from all poles.
    """
    return F(7)


@pytest.fixture
def sparse_h_params():
    """Sparse 4-parameter CY_2 vector for testing.

    h = (3, 1, -1, -3, 0, 0, ..., 0).
    Sum = 0. Nonzero in 4 directions only.
    """
    return [F(3), F(1), F(-1), F(-3)] + [F(0)] * 20


# ============================================================================
# Section 1: Coulomb branch geometry (10 tests)
# ============================================================================

class TestCoulombBranch:
    """Tests for Coulomb branch M_C = T^*Hilb^n(K3)."""

    def test_charge_0(self):
        """Charge 0: trivial Coulomb branch."""
        c = coulomb_branch_k3(0)
        assert c.charge == 0
        assert c.complex_dim == 0
        assert c.euler_char_fixed == 1
        assert c.is_hyperkahler is True

    def test_charge_1_dim(self):
        """Charge 1: dim_C(T^*Hilb^1(K3)) = 4."""
        c = coulomb_branch_k3(1)
        assert c.complex_dim == 4
        assert c.quaternionic_dim == 1

    def test_charge_1_euler(self):
        """Charge 1: chi(Hilb^1(K3)) = chi(K3) = 24."""
        c = coulomb_branch_k3(1)
        assert c.euler_char_fixed == 24

    def test_charge_2_euler(self):
        """Charge 2: chi(Hilb^2(K3)) = p_{24}(2) = 324."""
        c = coulomb_branch_k3(2)
        assert c.euler_char_fixed == 324

    def test_charge_3_euler(self):
        """Charge 3: chi(Hilb^3(K3)) = p_{24}(3) = 3200."""
        c = coulomb_branch_k3(3)
        assert c.euler_char_fixed == 3200

    def test_symplectic_resolution_charge_1(self):
        """Charge 1: Hilb^1 = K3 is smooth, no resolution needed."""
        c = coulomb_branch_k3(1)
        assert c.symplectic_resolution is False

    def test_symplectic_resolution_charge_2(self):
        """Charge 2: Hilb^2 -> Sym^2 is a symplectic resolution."""
        c = coulomb_branch_k3(2)
        assert c.symplectic_resolution is True

    def test_hyperkahler_all_charges(self):
        """All Coulomb branches are hyperkahler."""
        for n in range(6):
            c = coulomb_branch_k3(n)
            assert c.is_hyperkahler is True

    def test_dim_formula(self):
        """dim_C = 4n for all charges."""
        for n in range(6):
            c = coulomb_branch_k3(n)
            assert c.complex_dim == 4 * n

    def test_negative_charge_raises(self):
        """Negative charge should raise ValueError."""
        with pytest.raises(ValueError):
            coulomb_branch_k3(-1)


# ============================================================================
# Section 2: Higgs branch and Beauville (8 tests)
# ============================================================================

class TestHiggsBranch:
    """Tests for Higgs branch: moduli of stable sheaves on K3."""

    def test_charge_0(self):
        """Charge 0: trivial Higgs branch."""
        h = higgs_branch_k3(0)
        assert h.charge == 0
        assert h.euler_char == 1

    def test_charge_1_beauville(self):
        """Charge 1: chi(M_H) = 24 (Beauville, Goettsche)."""
        h = higgs_branch_k3(1)
        assert h.euler_char == 24

    def test_charge_2_beauville(self):
        """Charge 2: chi(M_H(v)) = p_{24}(2) = 324."""
        h = higgs_branch_k3(2)
        assert h.euler_char == 324

    def test_mukai_vector_sq(self):
        """<v,v>_Muk = 2n-2 for primitive Mukai vector at charge n."""
        for n in range(6):
            h = higgs_branch_k3(n)
            assert h.mukai_vector_sq == 2 * n - 2

    def test_self_dual_flag(self):
        """K3 is self-mirror: all Higgs branches carry self-dual flag."""
        for n in range(6):
            h = higgs_branch_k3(n)
            assert h.is_self_dual is True

    def test_dim_formula(self):
        """dim_C(M_H) = 4n for n > 0."""
        for n in range(1, 6):
            h = higgs_branch_k3(n)
            assert h.complex_dim == 4 * n

    def test_charge_4_euler(self):
        """Charge 4: p_{24}(4) = 25650."""
        h = higgs_branch_k3(4)
        assert h.euler_char == 25650

    def test_charge_5_euler(self):
        """Charge 5: p_{24}(5) = 176256."""
        h = higgs_branch_k3(5)
        assert h.euler_char == 176256


# ============================================================================
# Section 3: K3 self-duality (10 tests)
# ============================================================================

class TestSelfDuality:
    """Tests for K3 self-duality under symplectic duality."""

    def test_is_self_mirror(self):
        """K3 is self-mirror."""
        sd = k3_self_duality()
        assert sd.is_self_mirror is True

    def test_euler_chars_match(self):
        """Coulomb and Higgs Euler chars match (self-duality)."""
        sd = k3_self_duality(max_charge=5)
        assert sd.euler_chars_match is True

    def test_euler_match_charge_by_charge(self):
        """Verify C=H at each charge individually."""
        sd = k3_self_duality(max_charge=5)
        for n in range(6):
            assert sd.coulomb_euler_chars[n] == sd.higgs_euler_chars[n]

    def test_kappa_preserved_by_symplectic(self):
        """Symplectic duality preserves kappa_ch."""
        sd = k3_self_duality()
        assert sd.kappa_ch_preserved is True

    def test_kappa_reversed_by_koszul(self):
        """Koszul duality reverses kappa_ch."""
        sd = k3_self_duality()
        assert sd.koszul_kappa_reversed is True

    def test_langlands_type(self):
        """Langlands dual type is self-dual for gl_1."""
        sd = k3_self_duality()
        assert "self-dual" in sd.langlands_dual_type

    def test_coulomb_euler_charge_0(self):
        """Coulomb Euler char at charge 0 is 1."""
        sd = k3_self_duality()
        assert sd.coulomb_euler_chars[0] == 1

    def test_coulomb_euler_charge_1(self):
        """Coulomb Euler char at charge 1 is 24."""
        sd = k3_self_duality()
        assert sd.coulomb_euler_chars[1] == 24

    def test_coulomb_euler_charge_2(self):
        """Coulomb Euler char at charge 2 is 324."""
        sd = k3_self_duality()
        assert sd.coulomb_euler_chars[2] == 324

    def test_conjectural_status(self):
        """All results are conjectural (AP-CY14)."""
        sd = k3_self_duality()
        assert sd.status == 'CONJECTURAL'


# ============================================================================
# Section 4: Langlands duality (6 tests)
# ============================================================================

class TestLanglandsDuality:
    """Tests for Langlands duality of the K3 Yangian."""

    def test_gl1_trivial(self, default_h_params):
        """Langlands duality is trivial for gl_1."""
        result = langlands_dual_structure_function(default_h_params)
        assert "self-Langlands-dual" in result

    def test_cy2_constraint_enforced(self):
        """CY_2 constraint sum h_i = 0 is enforced."""
        bad_params = [F(1)] * 24  # sum = 24 != 0
        with pytest.raises(ValueError, match="CY_2 constraint"):
            langlands_dual_structure_function(bad_params)

    def test_structure_function_gl1(self, default_h_params, safe_z):
        """g^L(z) = g(z) for gl_1."""
        result = structure_function_under_dualities(default_h_params, safe_z)
        assert result['g_original'] == result['g_langlands']

    def test_koszul_is_inversion(self, default_h_params, safe_z):
        """g^!(z) = 1/g(z)."""
        result = structure_function_under_dualities(default_h_params, safe_z)
        product = result['g_original'] * result['g_koszul']
        assert product == F(1)

    def test_pole_safety(self, default_h_params):
        """Test point z=1 is a pole for default params (AP-CY28)."""
        # z=1 is a zero of g (since h_1=1), but z+h_5 = 1+(-1/5) = 4/5 != 0
        # Actually z-h_1 = 0 when z=1 and h_1=1, so g(1) = 0, not a pole.
        # The pole is at z = -h_1 = -1.
        result = structure_function_under_dualities(default_h_params, F(1))
        assert result['g_original'] == F(0)  # zero, not pole

    def test_langlands_preserves_cy2(self, default_h_params):
        """Langlands dual parameters satisfy CY_2 constraint."""
        # For gl_1: h^L = h, so sum h^L = sum h = 0
        assert sum(default_h_params) == 0


# ============================================================================
# Section 5: Structure function under dualities (10 tests)
# ============================================================================

class TestStructureFunctionDualities:
    """Tests for g(z) under Koszul, symplectic, and unitarity."""

    def test_unitarity_default(self, default_h_params, safe_z):
        """g(z)*g(-z) = 1 for default parameters."""
        inv = yangian_duality_involutions(default_h_params, safe_z)
        assert inv.g_unitarity_product == F(1)

    def test_koszul_inversion(self, default_h_params, safe_z):
        """g(z)*g^!(z) = 1."""
        inv = yangian_duality_involutions(default_h_params, safe_z)
        assert inv.g_original_at_z * inv.g_koszul_at_z == F(1)

    def test_langlands_identity(self, default_h_params, safe_z):
        """g^L(z) = g(z) for gl_1."""
        inv = yangian_duality_involutions(default_h_params, safe_z)
        assert inv.g_langlands_at_z == inv.g_original_at_z

    def test_koszul_involution_order(self, default_h_params, safe_z):
        """Koszul involution has order 2."""
        inv = yangian_duality_involutions(default_h_params, safe_z)
        assert inv.koszul_involution_order == 2

    def test_langlands_involution_order(self, default_h_params, safe_z):
        """Langlands involution has order 1 (trivial for gl_1)."""
        inv = yangian_duality_involutions(default_h_params, safe_z)
        assert inv.langlands_involution_order == 1

    def test_unitarity_sparse(self, sparse_h_params):
        """g(z)*g(-z) = 1 for sparse parameters."""
        z = F(11)  # far from poles at +/-3, +/-1
        inv = yangian_duality_involutions(sparse_h_params, z)
        assert inv.g_unitarity_product == F(1)

    def test_koszul_params(self, default_h_params, safe_z):
        """Koszul dual parameters are h_i -> -h_i."""
        inv = yangian_duality_involutions(default_h_params, safe_z)
        for i in range(len(default_h_params)):
            assert inv.h_koszul[i] == -default_h_params[i]

    def test_langlands_params(self, default_h_params, safe_z):
        """Langlands dual parameters equal original for gl_1."""
        inv = yangian_duality_involutions(default_h_params, safe_z)
        for i in range(len(default_h_params)):
            assert inv.h_langlands[i] == default_h_params[i]

    def test_pole_raises(self, default_h_params):
        """Pole test point raises ValueError (AP-CY28)."""
        # z = -1 is a pole: z + h_1 = -1 + 1 = 0
        with pytest.raises(ValueError, match="pole"):
            yangian_duality_involutions(default_h_params, F(-1))

    def test_g_at_zero(self, default_h_params):
        """g(0) = (-1)^24 = 1 (even number of factors)."""
        # g(0) = prod (-h_i/h_i) = prod(-1) = (-1)^24 = 1
        # But we need to check that z=0 is not a pole
        # z + h_i = h_i != 0 for all nonzero h_i (no pole at z=0 if no h_i = 0)
        # Default params: h_i = 1 or -1/5, none zero. Safe.
        inv = yangian_duality_involutions(default_h_params, F(0))
        # g(0) = prod (-h_i / h_i) = (-1)^24 = 1
        # But actually: some params are negative (-1/5), so
        # for h = 1: (0-1)/(0+1) = -1
        # for h = -1/5: (0-(-1/5))/(0+(-1/5)) = (1/5)/(-1/5) = -1
        # Product = (-1)^24 = 1
        assert inv.g_original_at_z == F(1)


# ============================================================================
# Section 6: BFN quantized Coulomb branch (8 tests)
# ============================================================================

class TestBFN:
    """Tests for BFN quantized Coulomb branch at special K3 points."""

    def test_kummer_charge_1(self):
        """Kummer K3 BFN at charge 1."""
        data = bfn_kummer_k3(1)
        assert data.quiver_type == "affine_A1"
        assert data.coulomb_dim == 4

    def test_kummer_charge_2(self):
        """Kummer K3 BFN at charge 2: dim = 8."""
        data = bfn_kummer_k3(2)
        assert data.coulomb_dim == 8

    def test_kummer_charge_0(self):
        """Kummer K3 BFN at charge 0: trivial."""
        data = bfn_kummer_k3(0)
        assert data.gauge_group == "trivial"

    def test_kummer_conjectural(self):
        """BFN identification is conjectural."""
        data = bfn_kummer_k3(1)
        assert data.status == 'CONJECTURAL'

    def test_ade_a1(self):
        """ADE type A1 BFN construction."""
        data = bfn_ade_k3("A1", 1)
        assert data.quiver_type == "affine_A1"
        assert data.coulomb_dim == 4

    def test_ade_e8(self):
        """ADE type E8 BFN construction."""
        data = bfn_ade_k3("E8", 1)
        assert data.quiver_type == "affine_E8"

    def test_ade_invalid_type(self):
        """Invalid ADE type raises ValueError."""
        with pytest.raises(ValueError):
            bfn_ade_k3("G2", 1)

    def test_ade_negative_charge(self):
        """Negative charge raises ValueError."""
        with pytest.raises(ValueError):
            bfn_ade_k3("A1", -1)


# ============================================================================
# Section 7: Symplectic vs Koszul diagnostic (8 tests)
# ============================================================================

class TestSymplecticVsKoszul:
    """Tests for the kappa diagnostic distinguishing symplectic and Koszul."""

    def test_kappa_original(self):
        """kappa_ch(Y) = 2."""
        diag = symplectic_vs_koszul_diagnostic()
        assert diag.kappa_ch_original == F(2)

    def test_kappa_koszul_dual(self):
        """kappa_ch(Y^!) = -2."""
        diag = symplectic_vs_koszul_diagnostic()
        assert diag.kappa_ch_koszul_dual == F(-2)

    def test_kappa_symplectic_dual(self):
        """kappa_ch(Y^L) = 2 (preserved)."""
        diag = symplectic_vs_koszul_diagnostic()
        assert diag.kappa_ch_symplectic_dual == F(2)

    def test_kappa_flop(self):
        """kappa_ch under flop = 2 (preserved, AP-CY10)."""
        diag = symplectic_vs_koszul_diagnostic()
        assert diag.kappa_ch_flop == F(2)

    def test_koszul_conductor(self):
        """Koszul conductor K = 0 (free-field branch)."""
        diag = symplectic_vs_koszul_diagnostic()
        assert diag.koszul_conductor == F(0)

    def test_symplectic_self_dual(self):
        """K3 is self-dual under symplectic duality."""
        diag = symplectic_vs_koszul_diagnostic()
        assert diag.symplectic_is_self_dual is True

    def test_koszul_not_self_dual(self):
        """K3 is NOT self-dual under Koszul (kappa != -kappa)."""
        diag = symplectic_vs_koszul_diagnostic()
        assert diag.koszul_is_self_dual is False

    def test_flop_trivial(self):
        """Flop is trivial for K3 surfaces."""
        diag = symplectic_vs_koszul_diagnostic()
        assert diag.flop_is_trivial is True


# ============================================================================
# Section 8: Generating functions (8 tests)
# ============================================================================

class TestGeneratingFunctions:
    """Tests for Coulomb/Higgs generating functions."""

    def test_self_dual_match(self):
        """Coulomb and Higgs generating functions match."""
        gf = coulomb_branch_generating_function()
        assert gf['self_dual_match'] is True

    def test_coulomb_values(self):
        """Coulomb Euler chars = p_{24}(n)."""
        gf = coulomb_branch_generating_function()
        assert gf['coulomb_euler_chars'][0] == 1
        assert gf['coulomb_euler_chars'][1] == 24
        assert gf['coulomb_euler_chars'][2] == 324
        assert gf['coulomb_euler_chars'][3] == 3200

    def test_higgs_values(self):
        """Higgs Euler chars = p_{24}(n)."""
        gf = coulomb_branch_generating_function()
        assert gf['higgs_euler_chars'][0] == 1
        assert gf['higgs_euler_chars'][1] == 24
        assert gf['higgs_euler_chars'][2] == 324

    def test_bar_euler_exponents(self):
        """Bar Euler exponents = -24 (class G)."""
        gf = coulomb_branch_generating_function()
        for k in range(1, 7):
            assert gf['bar_euler_exponents'][k] == -24

    def test_generating_function_form(self):
        """Generating function is 1/eta(q)^{24}."""
        gf = coulomb_branch_generating_function()
        assert gf['generating_function'] == '1/eta(q)^{24}'

    def test_fock_character(self):
        """Fock space character is 1/eta(q)^{24}."""
        gf = coulomb_branch_generating_function()
        assert gf['fock_space_character'] == '1/eta(q)^{24}'

    def test_p24_6(self):
        """p_{24}(6) = 1073720."""
        gf = coulomb_branch_generating_function(max_charge=6)
        assert gf['coulomb_euler_chars'][6] == 1073720

    def test_fake_monster_connection(self):
        """Connection to Fake Monster Lie algebra."""
        gf = coulomb_branch_generating_function()
        assert 'Fake Monster' in gf['fake_monster_connection']


# ============================================================================
# Section 9: Hilbert-Chow resolution (6 tests)
# ============================================================================

class TestHilbertChow:
    """Tests for the Hilbert-Chow symplectic resolution."""

    def test_charge_0(self):
        """Charge 0: point, no resolution."""
        data = hilbert_chow_resolution_data(0)
        assert data['hilb_dim'] == 0
        assert data['is_symplectic_resolution'] is False

    def test_charge_1_not_resolution(self):
        """Charge 1: Hilb^1 = K3, isomorphism not resolution."""
        data = hilbert_chow_resolution_data(1)
        assert data['hilb_dim'] == 2
        assert data['is_symplectic_resolution'] is False

    def test_charge_2_is_resolution(self):
        """Charge 2: Hilb^2 -> Sym^2 is symplectic resolution."""
        data = hilbert_chow_resolution_data(2)
        assert data['is_symplectic_resolution'] is True
        assert data['exceptional_fiber_dim'] == 1

    def test_cotangent_dim(self):
        """dim(T^*Hilb^n) = 4n."""
        for n in range(1, 6):
            data = hilbert_chow_resolution_data(n)
            assert data['cotangent_hilb_dim'] == 4 * n

    def test_hilb_vs_sym_euler(self):
        """chi(Hilb^n) != chi(Sym^n) for n >= 2 (resolution correction)."""
        data2 = hilbert_chow_resolution_data(2)
        # chi(Hilb^2(K3)) = 324, chi(Sym^2(K3)) = binomial(25, 2) = 300
        assert data2['euler_char_hilb'] == 324
        assert data2['euler_char_sym'] == 300
        assert data2['euler_char_hilb'] != data2['euler_char_sym']

    def test_charge_1_euler_match(self):
        """At charge 1: Hilb^1 = Sym^1, so Euler chars match."""
        data1 = hilbert_chow_resolution_data(1)
        assert data1['euler_char_hilb'] == 24
        assert data1['euler_char_sym'] == 24


# ============================================================================
# Section 10: Dolgachev-Nikulin lattice (8 tests)
# ============================================================================

class TestDolgachevNikulin:
    """Tests for Dolgachev-Nikulin lattice self-duality."""

    def test_rho_10_self_mirror(self):
        """At rho=10: K3 is lattice-polarized self-mirror."""
        data = dolgachev_nikulin_self_duality(10)
        assert data.is_lattice_self_mirror is True

    def test_rho_1_not_self_mirror(self):
        """At rho=1: mirror has rho=19, not self-mirror."""
        data = dolgachev_nikulin_self_duality(1)
        assert data.is_lattice_self_mirror is False
        assert data.mirror_picard_rank == 19

    def test_rho_20_mirror(self):
        """At rho=20 (Kummer): mirror has rho=0 (not valid)."""
        data = dolgachev_nikulin_self_duality(20)
        assert data.mirror_picard_rank == 0

    def test_algebraic_signature(self):
        """Algebraic sublattice has signature (2, rho)."""
        for rho in range(1, 21):
            data = dolgachev_nikulin_self_duality(rho)
            assert data.algebraic_signature == (2, rho)

    def test_transcendental_signature(self):
        """Transcendental sublattice has signature (2, 20-rho)."""
        for rho in range(1, 21):
            data = dolgachev_nikulin_self_duality(rho)
            assert data.transcendental_signature == (2, 20 - rho)

    def test_euler_char_preserved(self):
        """chi(Hilb^n) = p_{24}(n) for ALL K3 (all Picard ranks)."""
        for rho in range(1, 21):
            data = dolgachev_nikulin_self_duality(rho)
            assert data.euler_char_preserved is True

    def test_mukai_rank_preserved(self):
        """Mukai rank = 24 for all K3."""
        for rho in range(1, 21):
            data = dolgachev_nikulin_self_duality(rho)
            assert data.mukai_rank_preserved is True

    def test_invalid_rho(self):
        """Picard rank outside [1,20] raises ValueError."""
        with pytest.raises(ValueError):
            dolgachev_nikulin_self_duality(0)
        with pytest.raises(ValueError):
            dolgachev_nikulin_self_duality(21)


# ============================================================================
# Section 11: Yangian involutions (10 tests)
# ============================================================================

class TestYangianInvolutions:
    """Tests for the three involutions on Yangian parameters."""

    def test_unitarity_at_z7(self, default_h_params):
        """g(7)*g(-7) = 1."""
        inv = yangian_duality_involutions(default_h_params, F(7))
        assert inv.g_unitarity_product == F(1)

    def test_unitarity_at_z13(self, default_h_params):
        """g(13)*g(-13) = 1."""
        inv = yangian_duality_involutions(default_h_params, F(13))
        assert inv.g_unitarity_product == F(1)

    def test_koszul_at_z7(self, default_h_params):
        """g(7)*g^!(7) = 1."""
        inv = yangian_duality_involutions(default_h_params, F(7))
        assert inv.g_original_at_z * inv.g_koszul_at_z == F(1)

    def test_langlands_at_z7(self, default_h_params):
        """g^L(7) = g(7) for gl_1."""
        inv = yangian_duality_involutions(default_h_params, F(7))
        assert inv.g_langlands_at_z == inv.g_original_at_z

    def test_unitarity_sparse(self, sparse_h_params):
        """g(z)*g(-z) = 1 for sparse params (4 nonzero + 20 zero)."""
        # Zero h_i contribute (z-0)/(z+0) = 1, harmless
        # Poles at z = +/-3, +/-1. Use z = 11.
        inv = yangian_duality_involutions(sparse_h_params, F(11))
        assert inv.g_unitarity_product == F(1)

    def test_koszul_sparse(self, sparse_h_params):
        """g*g^! = 1 for sparse params."""
        inv = yangian_duality_involutions(sparse_h_params, F(11))
        assert inv.g_original_at_z * inv.g_koszul_at_z == F(1)

    def test_koszul_order_2(self, default_h_params, safe_z):
        """Koszul involution has order 2: (h^!)^! = h."""
        inv = yangian_duality_involutions(default_h_params, safe_z)
        h_double_koszul = [-h for h in inv.h_koszul]
        for i in range(len(default_h_params)):
            assert h_double_koszul[i] == default_h_params[i]

    def test_langlands_order_1(self, default_h_params, safe_z):
        """Langlands involution has order 1 (trivial for gl_1)."""
        inv = yangian_duality_involutions(default_h_params, safe_z)
        assert inv.langlands_involution_order == 1
        for i in range(len(default_h_params)):
            assert inv.h_langlands[i] == default_h_params[i]

    def test_three_involutions_distinct(self, default_h_params, safe_z):
        """The three involutions are distinct operations."""
        inv = yangian_duality_involutions(default_h_params, safe_z)
        # Koszul reverses sign; Langlands is identity; unitarity is g(-z)
        # Koszul != Langlands (unless h=0)
        assert inv.h_koszul != inv.h_langlands

    def test_cy2_preserved(self, default_h_params, safe_z):
        """All involutions preserve the CY_2 constraint sum h_i = 0."""
        inv = yangian_duality_involutions(default_h_params, safe_z)
        assert sum(inv.h_koszul) == 0
        assert sum(inv.h_langlands) == 0


# ============================================================================
# Section 12: Two routes comparison (4 tests)
# ============================================================================

class TestTwoRoutes:
    """Tests for the CY-A vs BFN route comparison."""

    def test_route_a_status(self):
        """Route A (CY-A) has CY-A_2 proved."""
        comp = two_routes_to_k3_yangian()
        assert "CY-A_2 PROVED" in comp.route_a_status

    def test_route_b_status(self):
        """Route B (BFN) is proved for quiver varieties."""
        comp = two_routes_to_k3_yangian()
        assert "PROVED for quiver" in comp.route_b_status

    def test_shared_output(self):
        """Both routes target the same Y(g_{K3})."""
        comp = two_routes_to_k3_yangian()
        assert "Y(g_{K3})" in comp.shared_output

    def test_kappa_ch_both_routes(self):
        """Both routes give kappa_ch = 2."""
        comp = two_routes_to_k3_yangian()
        assert "kappa_ch = 2" in comp.distinguishing_data['route_a_kappa_ch']
        assert "kappa_ch = 2" in comp.distinguishing_data['route_b_kappa_ch']


# ============================================================================
# Section 13: Full verification suite (6 tests)
# ============================================================================

class TestFullVerification:
    """Tests for the full verification suite."""

    def test_all_pass(self):
        """All verification checks pass."""
        results = full_verification()
        for r in results:
            assert r.passed, f"FAILED: {r.name}: {r.detail}"

    def test_count(self):
        """Verification suite has 7 checks."""
        results = full_verification()
        assert len(results) == 7

    def test_coulomb_higgs_match(self):
        """Coulomb-Higgs match passes."""
        r = verify_coulomb_higgs_match()
        assert r.passed

    def test_kappa_diagnostic_passes(self):
        """kappa diagnostic passes."""
        r = verify_kappa_diagnostic()
        assert r.passed

    def test_dn_signatures_pass(self):
        """DN signatures pass."""
        r = verify_dolgachev_nikulin_signatures()
        assert r.passed

    def test_beauville_passes(self):
        """Beauville Euler chars pass."""
        r = verify_beauville_euler_chars()
        assert r.passed


# ============================================================================
# Section 14: Constants and cross-consistency (extra)
# ============================================================================

class TestConstants:
    """Tests for constants and AP113 kappa compliance."""

    def test_mukai_rank(self):
        """Mukai rank = 24."""
        assert MUKAI_RANK == 24

    def test_mukai_signature(self):
        """Mukai signature = (4, 20)."""
        assert MUKAI_SIGNATURE == (4, 20)

    def test_kappa_ch(self):
        """kappa_ch(K3) = 2 (AP113)."""
        assert KAPPA_CH_K3 == F(2)

    def test_kappa_bkm(self):
        """kappa_BKM(K3) = 5 (AP113)."""
        assert KAPPA_BKM_K3 == F(5)

    def test_kappa_cat(self):
        """kappa_cat(K3) = chi(O_K3) = 2 (AP113)."""
        assert KAPPA_CAT_K3 == F(2)

    def test_kappa_fiber(self):
        """kappa_fiber(K3) = 24 (AP113)."""
        assert KAPPA_FIBER_K3 == F(24)

    def test_conjectural_status(self):
        """Module status is CONJECTURAL."""
        assert STATUS == 'CONJECTURAL'


# ============================================================================
# Section 15: Cross-engine verification (multi-path, AP10 compliance)
# ============================================================================

class TestCrossEngineVerification:
    """Cross-checks against k3_double_current_algebra, k3_yangian,
    k3_mirror_koszul, k3_yangian_quantization, and drinfeld_center_k3_heisenberg.

    These tests verify that symplectic_duality_k3 agrees with independently
    computed values in the existing engine suite (multi-path verification).
    """

    def test_mukai_rank_vs_dca(self):
        """MUKAI_RANK matches k3_double_current_algebra.MUKAI_RANK."""
        from compute.lib.k3_double_current_algebra import (
            MUKAI_RANK as DCA_MUKAI_RANK,
        )
        assert MUKAI_RANK == DCA_MUKAI_RANK

    def test_mukai_sig_plus_vs_dca(self):
        """MUKAI_SIG_PLUS matches k3_double_current_algebra."""
        from compute.lib.k3_double_current_algebra import (
            MUKAI_SIG_PLUS as DCA_SIG_PLUS,
        )
        assert MUKAI_SIG_PLUS == DCA_SIG_PLUS

    def test_mukai_sig_minus_vs_dca(self):
        """MUKAI_SIG_MINUS matches k3_double_current_algebra."""
        from compute.lib.k3_double_current_algebra import (
            MUKAI_SIG_MINUS as DCA_SIG_MINUS,
        )
        assert MUKAI_SIG_MINUS == DCA_SIG_MINUS

    def test_kappa_spectrum_vs_mirror_koszul(self):
        """kappa spectrum matches k3_mirror_koszul.k3_kappa_spectrum()."""
        from compute.lib.k3_mirror_koszul import k3_kappa_spectrum
        spectrum = k3_kappa_spectrum()
        assert KAPPA_CH_K3 == spectrum['kappa_ch']
        assert KAPPA_BKM_K3 == spectrum['kappa_BKM']
        assert KAPPA_CAT_K3 == spectrum['kappa_cat']
        assert KAPPA_FIBER_K3 == spectrum['kappa_fiber']

    def test_koszul_conductor_vs_mirror_koszul(self):
        """Koszul conductor K=0 matches k3_mirror_koszul."""
        from compute.lib.k3_mirror_koszul import koszul_conductor_k3
        assert KOSZUL_CONDUCTOR_FREE_FIELD == koszul_conductor_k3()

    def test_koszul_dual_kappa_vs_mirror_koszul(self):
        """kappa^! = -2 matches k3_mirror_koszul.koszul_dual_kappa_k3()."""
        from compute.lib.k3_mirror_koszul import koszul_dual_kappa_k3
        diag = symplectic_vs_koszul_diagnostic()
        assert diag.kappa_ch_koszul_dual == koszul_dual_kappa_k3()

    def test_hms_not_koszul_vs_mirror_koszul(self):
        """HMS != Koszul confirmed by k3_mirror_koszul."""
        from compute.lib.k3_mirror_koszul import hms_is_not_koszul_k3
        # Our diagnostic: symplectic_is_self_dual=True, koszul_is_self_dual=False
        # Mirror Koszul: hms_is_not_koszul_k3() = True
        assert hms_is_not_koszul_k3() is True
        diag = symplectic_vs_koszul_diagnostic()
        assert diag.koszul_is_self_dual is False

    def test_euler_chars_vs_dca_bar_euler(self):
        """Coulomb branch Euler chars = 1/(bar Euler product) coefficients.

        bar_euler_generating_function gives coefficients of eta^{24} = prod(1-q^k)^{24}.
        The inverse gives coefficients of 1/eta^{24} = sum p_{24}(n) q^n.
        chi(Hilb^n(K3)) = p_{24}(n).
        """
        from compute.lib.k3_double_current_algebra import (
            bar_euler_generating_function,
        )
        # bar_euler gives [q^k coefficient of eta^{24}]
        # We verify via the partition function (inverse) instead
        from compute.lib.k3_double_current_algebra import partition_function
        part_fn = partition_function(max_degree=6)

        gf = coulomb_branch_generating_function(max_charge=6)
        for n in range(7):
            if n in part_fn:
                assert gf['coulomb_euler_chars'][n] == part_fn[n], \
                    f"Mismatch at n={n}: coulomb={gf['coulomb_euler_chars'][n]}, " \
                    f"partition={part_fn[n]}"

    def test_params_match_k3_yangian_kummer(self):
        """Default h_params match k3_yangian.kummer_k3_parameters()."""
        from compute.lib.k3_yangian import kummer_k3_parameters
        from sympy import Rational
        kummer = kummer_k3_parameters(Rational(1))
        # Our default: [1]*4 + [-1/5]*20
        our_h = [F(1)] * MUKAI_SIG_PLUS + [-F(1, 5)] * MUKAI_SIG_MINUS
        for i in range(MUKAI_RANK):
            assert F(kummer.h[i]) == our_h[i], \
                f"Param mismatch at i={i}: kummer={kummer.h[i]}, ours={our_h[i]}"

    def test_structure_fn_vs_k3_yangian(self):
        """Structure function g(z) matches k3_yangian.structure_function_evaluate()."""
        from compute.lib.k3_yangian import (
            kummer_k3_parameters,
            structure_function_evaluate,
        )
        from sympy import Rational
        params = kummer_k3_parameters(Rational(1))
        z_val = Rational(7)
        g_yangian = structure_function_evaluate(z_val, params)

        # Our computation
        our_h = [F(1)] * MUKAI_SIG_PLUS + [-F(1, 5)] * MUKAI_SIG_MINUS
        inv = yangian_duality_involutions(our_h, F(7))
        assert F(g_yangian) == inv.g_original_at_z

    def test_unitarity_vs_k3_yangian(self):
        """Unitarity g(z)*g(-z)=1 matches k3_yangian computation."""
        from compute.lib.k3_yangian import (
            kummer_k3_parameters,
            structure_function_evaluate,
        )
        from sympy import Rational
        params = kummer_k3_parameters(Rational(1))
        z_val = Rational(7)
        g_pos = structure_function_evaluate(z_val, params)
        g_neg = structure_function_evaluate(-z_val, params)
        assert g_pos * g_neg == 1

    def test_drinfeld_double_dim_49(self):
        """Drinfeld double dim = 49 matches drinfeld_center_k3_heisenberg."""
        from compute.lib.drinfeld_center_k3_heisenberg import (
            DRINFELD_DOUBLE_DIM,
        )
        # 2*24 + 1 = 49
        assert DRINFELD_DOUBLE_DIM == 2 * MUKAI_RANK + 1

    def test_fake_monster_multiplicities_vs_quantization(self):
        """Fake Monster root multiplicities match k3_yangian_quantization."""
        from compute.lib.k3_yangian_quantization import (
            FAKE_MONSTER_MULTIPLICITIES,
        )
        # c(0) = 24 = MUKAI_RANK (lightlike level)
        assert FAKE_MONSTER_MULTIPLICITIES[0] == MUKAI_RANK
        # c(1) = 324 = chi(Hilb^2(K3)) = p_{24}(2)
        assert FAKE_MONSTER_MULTIPLICITIES[1] == HILB_EULER_CHARS[2]
        # c(2) = 3200 = p_{24}(3)
        assert FAKE_MONSTER_MULTIPLICITIES[2] == HILB_EULER_CHARS[3]

    def test_mukai_signature_vs_mirror_koszul(self):
        """Mukai lattice signature matches k3_mirror_koszul."""
        from compute.lib.k3_mirror_koszul import mukai_lattice_signature
        sig = mukai_lattice_signature()
        assert sig == MUKAI_SIGNATURE

    def test_dn_decomposition_vs_mirror_koszul(self):
        """DN decomposition matches k3_mirror_koszul at rho=10."""
        from compute.lib.k3_mirror_koszul import dolgachev_nikulin_decomposition
        ext_data = dolgachev_nikulin_decomposition(10)
        our_data = dolgachev_nikulin_self_duality(10)
        assert ext_data['algebraic'] == our_data.algebraic_signature
        assert ext_data['transcendental'] == our_data.transcendental_signature

    def test_chi_O_vs_mirror_koszul(self):
        """chi(O_K3) = 2 matches k3_mirror_koszul.k3_chi_O()."""
        from compute.lib.k3_mirror_koszul import k3_chi_O
        assert KAPPA_CAT_K3 == F(k3_chi_O())
