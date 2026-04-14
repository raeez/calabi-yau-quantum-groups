r"""Tests for heterotic/type II string duality and the K3 Yangian.

Tests organized by topic:
  1. Narain moduli space and Yangian parameter identification
  2. Heterotic/type II duality map
  3. Coupling-Kahler exchange
  4. Perturbative limit: tree-level Yangian
  5. D-brane states and BKM imaginary root dictionary
  6. BPS mass formula
  7. Fricke involution
  8. Self-dual point
  9. Structure function duality invariance
  10. Instanton corrections
  11. Constants consistency
  12. Full end-to-end verification

All test points satisfy AP-CY28 (avoid poles at +/- h_i).
kappa subscripts per AP113.
"""

import math
import numpy as np
import pytest
from fractions import Fraction

from compute.lib.heterotic_typeII_yangian import (
    BKM_ROOT_MULTIPLICITIES,
    HETEROTIC_GAUGE_RANK,
    HETEROTIC_LEFT_MOVERS,
    KAPPA_BKM,
    KAPPA_CAT,
    KAPPA_CH,
    KAPPA_FIBER,
    NARAIN_DIM,
    NARAIN_RANK,
    NARAIN_SIGNATURE,
    STATUS,
    DBraneChargeVector,
    bkm_d_brane_dictionary,
    bps_mass_formula,
    coupling_kahler_exchange,
    d_brane_charge_vector,
    duality_map_data,
    fricke_action_on_eta,
    fricke_involution,
    fricke_on_yangian_parameters,
    full_heterotic_typeII_verification,
    instanton_correction_structure,
    narain_moduli_data,
    narain_moduli_decomposition,
    narain_to_yangian_map,
    perturbative_expansion,
    perturbative_regime_verification,
    perturbative_yangian_data,
    self_dual_point,
    structure_function_duality_invariance,
)


# =========================================================================
# 1. Narain moduli space
# =========================================================================

class TestNarainModuli:
    """Narain moduli space N_{4,20}."""

    def test_narain_dimension(self):
        """dim N_{4,20} = 4 * 20 = 80."""
        data = narain_moduli_data()
        assert data.dimension == 80

    def test_narain_rank(self):
        """Narain lattice rank = 24 (= Mukai rank)."""
        data = narain_moduli_data()
        assert data.rank == 24

    def test_narain_signature(self):
        """Narain signature = (4, 20)."""
        data = narain_moduli_data()
        assert data.signature == (4, 20)

    def test_narain_yangian_params(self):
        """24 Yangian parameters from Narain lattice."""
        data = narain_moduli_data()
        assert data.num_yangian_params == 24

    def test_narain_effective_params(self):
        """Effective params = 24 - 1 (CY_2 constraint) = 23."""
        data = narain_moduli_data()
        assert data.effective_params == 23

    def test_narain_lattice_isomorphism(self):
        """Narain lattice = U^4 + E_8(-1)^2."""
        data = narain_moduli_data()
        assert 'U^4' in data.narain_lattice_iso
        assert 'E_8' in data.narain_lattice_iso

    def test_narain_dim_formula(self):
        """dim = sig_plus * sig_minus."""
        assert NARAIN_DIM == NARAIN_SIGNATURE[0] * NARAIN_SIGNATURE[1]

    def test_narain_to_yangian_surjective(self):
        """The map Narain -> Yangian params is surjective."""
        data = narain_to_yangian_map()
        assert data.is_surjective

    def test_narain_to_yangian_not_injective(self):
        """The map Narain -> Yangian params is NOT injective (O(4,20;Z) orbits)."""
        data = narain_to_yangian_map()
        assert not data.is_injective

    def test_narain_decomposition_het(self):
        """Heterotic decomposition sums to 80."""
        decomp = narain_moduli_decomposition()
        het = decomp['heterotic_decomposition']
        assert het['total'] == 80

    def test_narain_decomposition_iia(self):
        """Type IIA decomposition sums to 80."""
        decomp = narain_moduli_decomposition()
        iia = decomp['typeIIA_decomposition']
        assert iia['total'] == 80


# =========================================================================
# 2. Duality map
# =========================================================================

class TestDualityMap:
    """Heterotic/type IIA duality map."""

    def test_duality_theories(self):
        """E_8 x E_8 heterotic <-> Type IIA."""
        data = duality_map_data()
        assert 'E_8' in data.heterotic_theory
        assert 'IIA' in data.typeII_theory

    def test_compactification_k3(self):
        """Compactification on K3."""
        data = duality_map_data()
        assert data.compactification == 'K3'

    def test_spacetime_dim(self):
        """Spacetime dimension = 6 (10 - 4)."""
        data = duality_map_data()
        assert data.spacetime_dim == 6

    def test_requires_cy_a2(self):
        """Duality identification requires CY-A_2."""
        data = duality_map_data()
        assert data.requires_cy_a2

    def test_cy_a2_proved(self):
        """CY-A_2 is PROVED at d=2."""
        data = duality_map_data()
        assert data.cy_a2_status == 'PROVED'

    def test_does_not_require_cy_a3(self):
        """Does NOT require CY-A_3 (AP-CY6 compliant)."""
        data = duality_map_data()
        assert not data.requires_cy_a3


# =========================================================================
# 3. Coupling-Kahler exchange
# =========================================================================

class TestCouplingKahlerExchange:
    """The fundamental relation g_s^{het} <-> t^{IIA}."""

    def test_weak_coupling(self):
        """g_s = 0.01 -> t_IIA = 100 (large volume)."""
        result = coupling_kahler_exchange(0.01)
        assert abs(result['t_IIA'] - 100.0) < 1e-10

    def test_strong_coupling(self):
        """g_s = 100 -> t_IIA = 0.01 (small volume)."""
        result = coupling_kahler_exchange(100.0)
        assert abs(result['t_IIA'] - 0.01) < 1e-10

    def test_self_dual_coupling(self):
        """g_s = 1 is the self-dual coupling."""
        result = coupling_kahler_exchange(1.0)
        assert result['self_dual_coupling']

    def test_coupling_relation(self):
        """phi^{het} + log(t^{IIA}) = 0."""
        for g_s in [0.01, 0.1, 1.0, 5.0, 100.0]:
            result = coupling_kahler_exchange(g_s)
            assert result['relation_check'], f"Failed at g_s = {g_s}"

    def test_inverse_relation(self):
        """g_s * t = 1."""
        for g_s in [0.01, 0.5, 1.0, 2.0, 100.0]:
            result = coupling_kahler_exchange(g_s)
            assert abs(g_s * result['t_IIA'] - 1.0) < 1e-12

    def test_hbar_equals_g_s(self):
        """Yangian deformation parameter hbar = g_s at leading order."""
        result = coupling_kahler_exchange(0.1)
        assert abs(result['hbar_yangian'] - 0.1) < 1e-15

    def test_invalid_coupling_raises(self):
        """Negative coupling raises ValueError."""
        with pytest.raises(ValueError):
            coupling_kahler_exchange(-0.1)

    def test_zero_coupling_raises(self):
        """Zero coupling raises ValueError."""
        with pytest.raises(ValueError):
            coupling_kahler_exchange(0.0)


# =========================================================================
# 4. Perturbative limit
# =========================================================================

class TestPerturbativeLimit:
    """Tree-level K3 Yangian in the weak coupling limit."""

    def test_tree_level_is_UEA(self):
        """Tree-level Yangian = U(g_{K3})."""
        data = perturbative_yangian_data()
        assert data.tree_level == 'U(g_{K3})'

    def test_bar_euler_invariant(self):
        """Bar Euler product eta^{24} is deformation-invariant."""
        data = perturbative_yangian_data()
        assert data.bar_euler_invariant

    def test_preserves_unitarity(self):
        """Unitarity g(z)*g(-z)=1 preserved at all orders."""
        data = perturbative_yangian_data()
        assert data.preserves_unitarity

    def test_corrections_vanish_class_G(self):
        """For class G (Heisenberg), all perturbative corrections vanish."""
        result = perturbative_expansion(0.01, 37.0)
        assert result['corrections_vanish_class_G']

    def test_structure_fn_independent_of_g_s(self):
        """For class G, g(z) is independent of g_s."""
        result = perturbative_regime_verification()
        assert result['all_couplings_give_same_g']

    def test_class_G_confirmed(self):
        """Class G confirmed by perturbative regime scan."""
        result = perturbative_regime_verification()
        assert result['class_G_confirmed']

    def test_shadow_class_G(self):
        """Perturbative expansion confirms shadow class G."""
        result = perturbative_expansion(0.1, 37.0)
        assert result['shadow_class'] == 'G'

    def test_multiple_z_values(self):
        """Corrections vanish at multiple z values."""
        for z in [37.0, 41.0, 53.0]:
            result = perturbative_expansion(0.1, z)
            assert result['corrections_vanish_class_G'], f"Failed at z={z}"


# =========================================================================
# 5. D-brane states and BKM dictionary
# =========================================================================

class TestDBraneBKM:
    """D-brane / BKM imaginary root dictionary."""

    def test_d_brane_charge_vector(self):
        """Construct a D-brane charge vector."""
        v = d_brane_charge_vector(1, 0, 0)
        assert v.r == 1
        assert v.C_sq == 0
        assert v.n == 0

    def test_mukai_norm(self):
        """Mukai norm: <v,v> = C^2 - 2rn."""
        v = d_brane_charge_vector(1, -4, 1)
        assert v.mukai_norm_sq == -4 - 2  # = -6

    def test_bkm_discriminant(self):
        """BKM discriminant D = rn - C^2/2."""
        v = d_brane_charge_vector(1, 0, 0)
        assert v.bkm_discriminant == 0  # D = 1*0 - 0 = 0

    def test_bkm_discriminant_minus_one(self):
        """D = -1 for v = (1, 0, -1)."""
        v = d_brane_charge_vector(1, 0, -1)
        assert v.bkm_discriminant == -1  # D = 1*(-1) - 0 = -1

    def test_bkm_discriminant_three(self):
        """D = 3 for v = (1, -4, 1)."""
        v = d_brane_charge_vector(1, -4, 1)
        assert v.bkm_discriminant == 3  # D = 1*1 - (-4)/2 = 1 + 2 = 3

    def test_bkm_multiplicity_lookup(self):
        """BKM multiplicity from phi_{0,1} coefficients."""
        v = d_brane_charge_vector(1, 0, 0)
        assert v.bkm_multiplicity == 10  # c(0) = 10

    def test_weyl_vector_multiplicity(self):
        """c(-1) = 2 (EZ convention, AP-CY9)."""
        assert BKM_ROOT_MULTIPLICITIES[-1] == 2

    def test_lightlike_multiplicity(self):
        """c(0) = 10 determines kappa_BKM = 5."""
        assert BKM_ROOT_MULTIPLICITIES[0] == 10
        assert KAPPA_BKM == BKM_ROOT_MULTIPLICITIES[0] // 2

    def test_fermionic_root(self):
        """c(3) = -2 (fermionic, D = 3 mod 4)."""
        assert BKM_ROOT_MULTIPLICITIES[3] == -2

    def test_odd_C_sq_raises(self):
        """Odd C^2 raises ValueError (K3 intersection form is even)."""
        with pytest.raises(ValueError, match="even"):
            d_brane_charge_vector(1, 3, 0)

    def test_dictionary_completeness(self):
        """Dictionary has entries for D = -1, 0, 3, 4."""
        result = bkm_d_brane_dictionary()
        discriminants = [entry['discriminant'] for entry in result['dictionary']]
        assert -1 in discriminants
        assert 0 in discriminants
        assert 3 in discriminants
        assert 4 in discriminants

    def test_dictionary_multiplicities(self):
        """Dictionary multiplicities match BKM_ROOT_MULTIPLICITIES."""
        result = bkm_d_brane_dictionary()
        for entry in result['dictionary']:
            D = entry['discriminant']
            assert entry['bkm_multiplicity'] == BKM_ROOT_MULTIPLICITIES[D]


# =========================================================================
# 6. BPS mass formula
# =========================================================================

class TestBPSMass:
    """BPS mass formula for D-brane states."""

    def test_bps_mass_positive(self):
        """BPS mass is positive for nontrivial charges."""
        result = bps_mass_formula(1, 0, 0, t_IIA=10.0)
        assert result['bps_mass'] > 0

    def test_bps_mass_scales_with_volume(self):
        """D4-brane mass scales with Kahler modulus t."""
        m1 = bps_mass_formula(1, 0, 0, t_IIA=10.0)['bps_mass']
        m2 = bps_mass_formula(1, 0, 0, t_IIA=100.0)['bps_mass']
        # D4 mass ~ r * t, so m2/m1 ~ 10
        assert m2 / m1 > 5  # Should be ~10

    def test_d0_mass_scales_inversely(self):
        """D0-brane mass scales inversely with t."""
        m1 = bps_mass_formula(0, 0, 1, t_IIA=10.0)['bps_mass']
        m2 = bps_mass_formula(0, 0, 1, t_IIA=100.0)['bps_mass']
        # D0 mass ~ n/t, so m2/m1 ~ 0.1
        assert m2 / m1 < 0.2

    def test_perturbative_state(self):
        """State with r=0, n=0 is perturbative."""
        result = bps_mass_formula(0, -2, 0, t_IIA=10.0)
        assert result['is_perturbative']

    def test_nonperturbative_suppression(self):
        """D4-brane has exponential suppression at large t."""
        result = bps_mass_formula(1, 0, 0, t_IIA=10.0)
        assert result['suppression_factor'] < 1e-4  # exp(-10)

    def test_degeneration_type_specified(self):
        """AP157: degeneration type is always specified."""
        result = bps_mass_formula(1, 0, 0)
        assert 'degeneration_type' in result
        assert result['degeneration_type'] == 'large Kahler volume'


# =========================================================================
# 7. Fricke involution
# =========================================================================

class TestFrickeInvolution:
    """Fricke involution W_N: tau -> -1/(N*tau)."""

    def test_fricke_n1_is_s_duality(self):
        """W_1 = S-duality: tau -> -1/tau."""
        data = fricke_involution(1)
        assert data.N == 1
        assert data.matrix == ((0, -1), (1, 0))

    def test_fricke_order_2(self):
        """Fricke involution has projective order 2."""
        for N in [1, 2, 3, 5]:
            data = fricke_involution(N)
            assert data.order == 2

    def test_fricke_preserves_uhp(self):
        """Fricke preserves the upper half-plane."""
        for N in [1, 2, 3]:
            data = fricke_involution(N)
            assert data.preserves_uhp

    def test_fricke_fixed_point_n1(self):
        """Fixed point of W_1: tau_* = i."""
        data = fricke_involution(1)
        assert abs(data.fixed_point - 1j) < 1e-12

    def test_fricke_fixed_point_n2(self):
        """Fixed point of W_2: tau_* = i/sqrt(2)."""
        data = fricke_involution(2)
        assert abs(data.fixed_point - 1j / math.sqrt(2)) < 1e-12

    def test_fricke_exchanges_cusps(self):
        """Fricke exchanges cusps of X_0(N)."""
        data = fricke_involution(1)
        assert data.exchanges_cusps

    def test_fricke_invalid_N_raises(self):
        """N < 1 raises ValueError."""
        with pytest.raises(ValueError):
            fricke_involution(0)

    def test_fricke_eta_convergence(self):
        """Both q-expansions converge (FM24)."""
        result = fricke_action_on_eta(1, 0.3 + 1.5j)
        assert result['q_tau_convergent']
        assert result['q_fricke_convergent']

    def test_fricke_eta_invalid_tau(self):
        """Im(tau) <= 0 raises ValueError."""
        with pytest.raises(ValueError, match="Im"):
            fricke_action_on_eta(1, 1.0 + 0j)

    def test_fricke_kappa_ch_preserved(self):
        """kappa_ch = 2 is preserved under Fricke (AP113)."""
        result = fricke_action_on_eta(1, 0.5 + 1.0j)
        assert result['kappa_ch_preserved']


# =========================================================================
# 8. Fricke on Yangian parameters
# =========================================================================

class TestFrickeOnYangian:
    """Fricke involution action on K3 Yangian parameters."""

    def test_class_G_trivial_action(self):
        """For class G (abelian), Fricke acts trivially on parameters."""
        from compute.lib.k3_yangian import kummer_k3_parameters
        params = kummer_k3_parameters()
        h_list = [float(h) for h in params.h]
        result = fricke_on_yangian_parameters(h_list, 1, 0.5 + 2.0j)
        assert result['class_G_trivial_action']

    def test_structure_fn_preserved(self):
        """Structure function preserved for class G."""
        from compute.lib.k3_yangian import kummer_k3_parameters
        params = kummer_k3_parameters()
        h_list = [float(h) for h in params.h]
        result = fricke_on_yangian_parameters(h_list, 1, 0.5 + 2.0j)
        assert result['structure_fn_preserved']


# =========================================================================
# 9. Self-dual point
# =========================================================================

class TestSelfDualPoint:
    """Self-dual point of the Fricke involution."""

    def test_fixed_point_n1(self):
        """tau_* = i is a fixed point of W_1."""
        result = self_dual_point(1)
        assert result['is_fixed_point']

    def test_fixed_point_n2(self):
        """tau_* = i/sqrt(2) is a fixed point of W_2."""
        result = self_dual_point(2)
        assert result['is_fixed_point']

    def test_q_convergent(self):
        """q-expansion converges at self-dual point (FM24)."""
        for N in [1, 2, 3]:
            result = self_dual_point(N)
            assert result['q_convergent'], f"Failed at N={N}"

    def test_yangian_self_dual(self):
        """Yangian is self-dual at the fixed point."""
        result = self_dual_point(1)
        assert result['yangian_self_dual']

    def test_kappa_ch_preserved(self):
        """kappa_ch = 2 at self-dual point (AP113)."""
        result = self_dual_point(1)
        assert result['kappa_ch'] == 2
        assert result['kappa_ch_preserved']

    def test_g_s_at_self_dual_n1(self):
        """g_s = 1 at the N=1 self-dual point (strong = weak)."""
        result = self_dual_point(1)
        assert abs(result['g_s_het_self_dual'] - 1.0) < 1e-10


# =========================================================================
# 10. Structure function duality invariance
# =========================================================================

class TestStructureFnDuality:
    """Structure function is duality-invariant."""

    def test_frame_independent(self):
        """g_{K3}(z) is independent of the duality frame."""
        result = structure_function_duality_invariance()
        assert result['frame_independent']

    def test_unitarity(self):
        """g(z) * g(-z) = 1 in both frames."""
        result = structure_function_duality_invariance()
        assert result['unitarity_holds']

    def test_both_give_same_g(self):
        """Heterotic and IIA interpretations give the same g(z)."""
        result = structure_function_duality_invariance()
        assert result['both_give_same_g']

    def test_kappa_ch_consistent(self):
        """kappa_ch = 2 (AP113)."""
        result = structure_function_duality_invariance()
        assert result['kappa_ch'] == 2


# =========================================================================
# 11. Instanton corrections
# =========================================================================

class TestInstantonCorrections:
    """Instanton correction structure."""

    def test_class_G_pert_vanish(self):
        """For class G, all perturbative corrections vanish."""
        result = instanton_correction_structure()
        assert result['perturbative_het']['for_class_G'] == \
            'all corrections vanish (Heisenberg is exact)'

    def test_ns5_doubly_nonpert(self):
        """NS5-brane instantons are doubly non-perturbative."""
        result = instanton_correction_structure()
        assert result['nonperturbative_het']['doubly_nonperturbative']


# =========================================================================
# 12. Constants consistency
# =========================================================================

class TestConstants:
    """Physical and mathematical constants."""

    def test_narain_dim(self):
        """Narain dim = 80."""
        assert NARAIN_DIM == 80

    def test_narain_rank(self):
        """Narain rank = 24."""
        assert NARAIN_RANK == 24

    def test_narain_signature(self):
        """Narain signature = (4, 20)."""
        assert NARAIN_SIGNATURE == (4, 20)

    def test_heterotic_gauge_rank(self):
        """Heterotic gauge rank = 16."""
        assert HETEROTIC_GAUGE_RANK == 16

    def test_heterotic_left_movers(self):
        """16 left-moving compact bosons."""
        assert HETEROTIC_LEFT_MOVERS == 16

    def test_kappa_ch(self):
        """kappa_ch = 2 (AP113)."""
        assert KAPPA_CH == 2

    def test_kappa_bkm(self):
        """kappa_BKM = 5 (weight of Delta_5, AP113)."""
        assert KAPPA_BKM == 5

    def test_kappa_cat(self):
        """kappa_cat = 2 = chi(O_K3) (AP113)."""
        assert KAPPA_CAT == 2

    def test_kappa_fiber(self):
        """kappa_fiber = 24 (lattice rank, AP113)."""
        assert KAPPA_FIBER == 24

    def test_status_conjectural(self):
        """Status is CONJECTURAL (AP-CY14)."""
        assert STATUS == 'CONJECTURAL'

    def test_bkm_c0_gives_kappa_bkm(self):
        """c(0) / 2 = kappa_BKM = 5."""
        assert BKM_ROOT_MULTIPLICITIES[0] // 2 == KAPPA_BKM


# =========================================================================
# 13. Full end-to-end verification
# =========================================================================

class TestFullVerification:
    """End-to-end verification."""

    def test_full_verification_passes(self):
        """All sub-verifications pass."""
        result = full_heterotic_typeII_verification()
        assert result['all_ok'], "Full verification failed"

    def test_full_verification_status(self):
        """Status is CONJECTURAL."""
        result = full_heterotic_typeII_verification()
        assert result['status'] == 'CONJECTURAL'

    def test_full_verification_kappa_ch(self):
        """kappa_ch = 2 in full verification (AP113)."""
        result = full_heterotic_typeII_verification()
        assert result['kappa_ch'] == 2
