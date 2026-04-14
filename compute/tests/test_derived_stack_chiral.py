r"""Tests for derived_stack_chiral.py: derived moduli stack of chiral algebra structures.

CENTRAL RESULTS:
    (1) ChirAlg(V) is a derived stack controlled by dgLa L_V = CHoch*(V,V)[1] (THEOREM: DAG).
    (2) T_A ChirAlg(V) = HH*_ch(A,A)[1] (THEOREM: Francis-Gaitsgory tangent complex).
    (3) HH^2_ch(H_Muk, H_Muk) = 0: the Heisenberg is UNOBSTRUCTED (THEOREM).
    (4) HH^1_ch(H_Muk, H_Muk) = Sym^2(C^{24*}) = C^{300} (THEOREM: deformation space).
    (5) phi_K3: M_{K3} -> ChirAlg(V) is injective on tangent spaces (THEOREM: local Torelli).
    (6) ADE strata: WZW(g,1) x H(C^{24-rk}) with c_total = 24 (THEOREM: Frenkel-Kac-Segal).
    (7) kappa_ch = 2 everywhere on M_{K3} (THEOREM: topological invariance).
    (8) Virtual dimension at Heisenberg = 299 (THEOREM: -1 + 300 - 0).

Test structure:
    - dgLa structure: dimensions, grading, MC equation (7 tests)
    - Tangent complex: HH^0, HH^1, HH^2, smoothness (8 tests)
    - K3 moduli map: dimensions, injectivity, local Torelli (6 tests)
    - ADE stratification: all types, codimension, central charge (9 tests)
    - Virtual dimension: Heisenberg, ADE, boundary (5 tests)
    - kappa variation: constancy across moduli (5 tests)
    - Degenerate pairings: boundary strata (4 tests)
    - Period map: Torelli theorems (4 tests)
    - Moduli comparison: A_inf vs chiral vs E_n (4 tests)
    - Numerical verification: pairing deformation, Jacobi (6 tests)
    - Full verification: integration test (2 tests)

Manuscript references:
    cy_to_chiral.tex, Section sec:chiral-deformation-stack
    k3_times_e.tex (K3 Mukai pairing and moduli)
    en_factorization.tex (Francis-Gaitsgory deformation complex)
"""

import pytest
import numpy as np
from fractions import Fraction

from compute.lib.derived_stack_chiral import (
    # Constants
    V_DIM, V_GRADED_DIMS, K3_MODULI_DIM,
    HEISENBERG_DEF_DIM, NARAIN_DIM,
    ADE_DATA, MAX_ADE_RANK_IN_K3,
    # dgLa
    chiral_deformation_dgla,
    _count_hom_graded,
    # Tangent complex
    tangent_complex_heisenberg,
    tangent_complex_wzw,
    # K3 moduli map
    k3_moduli_map,
    # ADE strata
    ade_stratum,
    all_ade_strata,
    # Virtual dimension
    virtual_dimension_at_point,
    heisenberg_locus_dimension,
    # Degenerate pairings
    degenerate_pairing_stratum,
    # Period map
    period_map_data,
    # kappa variation
    kappa_variation_heisenberg,
    kappa_variation_ade,
    # Moduli comparison
    moduli_comparison_table,
    # Numerical
    mukai_pairing_matrix,
    deformed_mukai_pairing,
    verify_nondegeneracy,
    lambda_bracket_from_pairing,
    verify_deformation_unobstructed,
    # Full
    full_verification,
)

F = Fraction


# =========================================================================
# Section 1: dgLa controlling chiral deformations
# =========================================================================

class TestChiralDeformationDgLa:
    """Tests for the dgLa L_V = CHoch*(V, V)[1]."""

    def test_v_dim(self):
        """V = H^*(K3, C) has dimension 24."""
        assert V_DIM == 24

    def test_graded_dims(self):
        """V has grading {0: 1, 2: 22, 4: 1}."""
        assert V_GRADED_DIMS == {0: 1, 2: 22, 4: 1}
        assert sum(V_GRADED_DIMS.values()) == 24

    def test_dgla_l0_positive(self):
        """L^0 = End(V) (grading-preserving) has positive dimension."""
        dgla = chiral_deformation_dgla()
        assert dgla.dgla_dims[0] > 0

    def test_dgla_l0_equals_graded_end(self):
        """L^0 = sum dim(V_d)^2 = 1 + 484 + 1 = 486."""
        dgla = chiral_deformation_dgla()
        expected = 1**2 + 22**2 + 1**2  # = 486
        assert dgla.dgla_dims[0] == expected

    def test_dgla_l1_positive(self):
        """L^1 = Hom(V tensor V, V) (degree-additive) is nonzero."""
        dgla = chiral_deformation_dgla()
        assert dgla.dgla_dims[1] > 0

    def test_dgla_l1_lambda_bracket_space(self):
        """L^1 contains all degree-additive bilinear maps V x V -> V.

        Degree constraint: deg(a) + deg(b) = deg(output).
        Triples (d1, d2, d_out) with d1+d2=d_out and all in {0,2,4}:
          (0,0,0): 1*1*1 = 1
          (0,2,2): 1*22*22 = 484
          (0,4,4): 1*1*1 = 1
          (2,0,2): 22*1*22 = 484
          (2,2,4): 22*22*1 = 484
          (4,0,4): 1*1*1 = 1
        Total: 1 + 484 + 1 + 484 + 484 + 1 = 1455
        """
        dgla = chiral_deformation_dgla()
        assert dgla.dgla_dims[1] == 1455

    def test_mc_equation_dim(self):
        """MC equation space = dim L^1."""
        dgla = chiral_deformation_dgla()
        assert dgla.mc_equation_dim == dgla.dgla_dims[1]


# =========================================================================
# Section 2: Tangent complex at Heisenberg point
# =========================================================================

class TestTangentComplexHeisenberg:
    """Tests for T_A ChirAlg(V) = HH*_ch(A,A)[1] at A = H_Muk."""

    def test_hh0_dim(self):
        """HH^0_ch(H_Muk, H_Muk) = C (identity automorphism)."""
        tc = tangent_complex_heisenberg()
        assert tc.hh0_dim == 1

    def test_hh1_dim(self):
        """HH^1_ch(H_Muk, H_Muk) = Sym^2(C^{24*}) has dim 300."""
        tc = tangent_complex_heisenberg()
        assert tc.hh1_dim == 300

    def test_hh1_equals_sym2(self):
        """dim Sym^2(V*) = n(n+1)/2 = 24*25/2 = 300."""
        assert HEISENBERG_DEF_DIM == 300

    def test_hh2_vanishes(self):
        """HH^2_ch(H_Muk, H_Muk) = 0 (UNOBSTRUCTED)."""
        tc = tangent_complex_heisenberg()
        assert tc.hh2_dim == 0

    def test_is_smooth(self):
        """ChirAlg(V) is smooth at the Heisenberg point."""
        tc = tangent_complex_heisenberg()
        assert tc.is_smooth is True

    def test_higher_obs_vanish(self):
        """All higher obstructions vanish (class G, free field)."""
        tc = tangent_complex_heisenberg()
        assert tc.higher_obs_vanish is True

    def test_virtual_dim(self):
        """vdim = -1 + 300 - 0 = 299."""
        tc = tangent_complex_heisenberg()
        assert tc.virtual_dim == 299

    def test_formal_neighborhood(self):
        """Formal neighborhood has dim 300 (= HH^1 since smooth)."""
        tc = tangent_complex_heisenberg()
        assert tc.formal_neighborhood_dim == 300


# =========================================================================
# Section 3: K3 moduli map
# =========================================================================

class TestK3ModuliMap:
    """Tests for phi_K3: M_{K3} -> ChirAlg(V)."""

    def test_source_dim(self):
        """M_{K3} has dimension 20."""
        km = k3_moduli_map()
        assert km.source_dim == 20

    def test_target_dim(self):
        """Narain moduli has dimension 80."""
        km = k3_moduli_map()
        assert km.target_dim == 80

    def test_narain_dim_formula(self):
        """dim Narain = p*q = 4*20 = 80."""
        assert NARAIN_DIM == 4 * 20

    def test_differential_injective(self):
        """Local Torelli: d(phi_K3) is injective."""
        km = k3_moduli_map()
        assert km.is_injective is True

    def test_differential_rank(self):
        """Rank of d(phi_K3) = 20 (full rank of source)."""
        km = k3_moduli_map()
        assert km.differential_rank == 20

    def test_not_surjective(self):
        """phi_K3 is not surjective: 20 < 80."""
        km = k3_moduli_map()
        assert km.is_surjective is False


# =========================================================================
# Section 4: ADE stratification
# =========================================================================

class TestADEStratification:
    """Tests for ADE strata of ChirAlg(V)."""

    def test_a1_stratum(self):
        """A1 stratum: rank 1, codim 1, residual 23."""
        s = ade_stratum('A1')
        assert s.rank == 1
        assert s.codimension_in_k3_moduli == 1
        assert s.residual_heisenberg_rank == 23

    def test_e8_stratum(self):
        """E8 stratum: rank 8, codim 8, residual 16."""
        s = ade_stratum('E8')
        assert s.rank == 8
        assert s.codimension_in_k3_moduli == 8
        assert s.residual_heisenberg_rank == 16

    def test_total_central_charge_all_types(self):
        """Total central charge = 24 for all ADE types."""
        for lt in ADE_DATA:
            s = ade_stratum(lt)
            assert s.total_central_charge == 24, f"Failed for {lt}"

    def test_wzw_central_charge(self):
        """c(WZW(g, k=1)) = rank(g) for simply-laced g."""
        for lt in ADE_DATA:
            s = ade_stratum(lt)
            assert s.wzw_central_charge == s.rank, f"Failed for {lt}"

    def test_central_charge_additivity(self):
        """c(WZW) + c(residual Heis) = 24."""
        for lt in ADE_DATA:
            s = ade_stratum(lt)
            assert s.wzw_central_charge + s.residual_heisenberg_rank == 24

    def test_all_are_lattice_voa(self):
        """Simply-laced at level 1 -> lattice VOA (Frenkel-Kac-Segal)."""
        for lt in ADE_DATA:
            s = ade_stratum(lt)
            assert s.is_lattice_voa is True

    def test_all_strata_count(self):
        """We have 7 ADE types: A1, A2, D4, D5, E6, E7, E8."""
        strata = all_ade_strata()
        assert len(strata) == 7

    def test_max_ade_rank(self):
        """All ADE ranks <= 20 (Picard bound for K3)."""
        for lt in ADE_DATA:
            assert ADE_DATA[lt]['rank'] <= MAX_ADE_RANK_IN_K3

    def test_codimension_equals_rank(self):
        """Codimension of ADE stratum in M_{K3} = rank(G)."""
        for lt in ADE_DATA:
            s = ade_stratum(lt)
            assert s.codimension_in_k3_moduli == s.rank


# =========================================================================
# Section 5: Virtual dimension
# =========================================================================

class TestVirtualDimension:
    """Tests for virtual dimension of ChirAlg(V)."""

    def test_heisenberg_vdim(self):
        """vdim at Heisenberg = 299."""
        tc = tangent_complex_heisenberg()
        vd = virtual_dimension_at_point(tc)
        assert vd.vdim == 299

    def test_heisenberg_unobstructed(self):
        """Heisenberg point is unobstructed."""
        tc = tangent_complex_heisenberg()
        vd = virtual_dimension_at_point(tc)
        assert vd.is_unobstructed is True

    def test_heisenberg_actual_dim(self):
        """Actual dimension = HH^1 = 300 (since unobstructed)."""
        tc = tangent_complex_heisenberg()
        vd = virtual_dimension_at_point(tc)
        assert vd.actual_dim == 300

    def test_ade_vdim_smaller(self):
        """ADE strata have smaller vdim (fewer residual deformations)."""
        tc_heis = tangent_complex_heisenberg()
        tc_a1 = tangent_complex_wzw('A1')
        assert tc_a1.virtual_dim < tc_heis.virtual_dim

    def test_heisenberg_locus_dim(self):
        """Heisenberg locus Heis(V) has real dimension 80."""
        hl = heisenberg_locus_dimension()
        assert hl['real_dim'] == 80
        assert hl['is_smooth'] is True


# =========================================================================
# Section 6: kappa variation
# =========================================================================

class TestKappaVariation:
    """Tests for constancy of kappa_ch across the moduli."""

    def test_kappa_ch_generic_k3(self):
        """kappa_ch = 2 at generic K3."""
        kv = kappa_variation_heisenberg()
        assert kv.kappa_ch == F(2)

    def test_kappa_ch_a1(self):
        """kappa_ch = 2 at A1 enhancement."""
        kv = kappa_variation_ade('A1')
        assert kv.kappa_ch == F(2)

    def test_kappa_ch_e8(self):
        """kappa_ch = 2 at E8 enhancement."""
        kv = kappa_variation_ade('E8')
        assert kv.kappa_ch == F(2)

    def test_kappa_ch_all_ade(self):
        """kappa_ch = 2 at ALL ADE enhancement points."""
        for lt in ADE_DATA:
            kv = kappa_variation_ade(lt)
            assert kv.kappa_ch == F(2), f"Failed for {lt}"

    def test_kappa_is_topological(self):
        """kappa_ch is a topological invariant (constant on M_{K3})."""
        kv = kappa_variation_heisenberg()
        assert kv.is_topological_invariant is True


# =========================================================================
# Section 7: Degenerate pairings (boundary strata)
# =========================================================================

class TestDegeneratePairings:
    """Tests for boundary strata of the Heisenberg locus."""

    def test_corank_0(self):
        """Corank 0: nondegenerate, full Heisenberg, stratum dim = 0."""
        dp = degenerate_pairing_stratum(0)
        assert dp.residual_heisenberg_rank == 24
        assert dp.num_central_generators == 0
        assert dp.stratum_dim == 0

    def test_corank_1(self):
        """Corank 1: one central generator, stratum dim = 23."""
        dp = degenerate_pairing_stratum(1)
        assert dp.residual_heisenberg_rank == 23
        assert dp.num_central_generators == 1
        assert dp.stratum_dim == 23  # Gr(1, 24) = P^{23}

    def test_corank_12(self):
        """Corank 12: half degenerate, stratum dim = 144."""
        dp = degenerate_pairing_stratum(12)
        assert dp.residual_heisenberg_rank == 12
        assert dp.stratum_dim == 12 * 12  # = 144

    def test_corank_24(self):
        """Corank 24: fully degenerate (abelian), stratum dim = 0."""
        dp = degenerate_pairing_stratum(24)
        assert dp.residual_heisenberg_rank == 0
        assert dp.num_central_generators == 24
        assert dp.stratum_dim == 0  # Gr(24, 24) = point


# =========================================================================
# Section 8: Period map and Torelli
# =========================================================================

class TestPeriodMap:
    """Tests for the period map and Torelli theorems."""

    def test_local_torelli(self):
        """Local Torelli holds for K3."""
        pm = period_map_data()
        assert pm.local_torelli_holds is True

    def test_global_torelli(self):
        """Global Torelli holds for K3."""
        pm = period_map_data()
        assert pm.global_torelli_holds is True

    def test_chiral_torelli(self):
        """Chiral Torelli holds: S recoverable from Phi(D^b(Coh(S)))."""
        pm = period_map_data()
        assert pm.chiral_torelli_holds is True

    def test_period_map_degree(self):
        """Period map has degree 1 (birational to period domain)."""
        pm = period_map_data()
        assert pm.period_map_degree == 1


# =========================================================================
# Section 9: Moduli comparison (A_inf vs chiral vs E_n)
# =========================================================================

class TestModuliComparison:
    """Tests for comparison of moduli stacks."""

    def test_three_moduli(self):
        """Three moduli stacks: A_inf, E_2, chiral."""
        mc = moduli_comparison_table()
        assert len(mc) == 3

    def test_e2_and_chiral_agree(self):
        """Mod_{E_2}(V) and Mod_{chiral}(V) have same def dim for Heisenberg."""
        mc = moduli_comparison_table()
        e2 = [m for m in mc if "E_2" in m.name][0]
        chiral = [m for m in mc if "chiral" in m.name][0]
        assert e2.deformation_dim == chiral.deformation_dim == 300

    def test_e1_larger_deformation_space(self):
        """Mod_{A_inf}(V) has larger deformation space (fewer constraints)."""
        mc = moduli_comparison_table()
        e1 = [m for m in mc if "A_inf" in m.name][0]
        chiral = [m for m in mc if "chiral" in m.name][0]
        assert e1.deformation_dim >= chiral.deformation_dim

    def test_all_unobstructed(self):
        """All three moduli are unobstructed at the Heisenberg point."""
        mc = moduli_comparison_table()
        assert all(m.is_smooth for m in mc)


# =========================================================================
# Section 10: Numerical verification
# =========================================================================

class TestNumericalVerification:
    """Numerical tests for Mukai pairing deformations."""

    def test_mukai_pairing_signature(self):
        """Mukai pairing has signature (4, 20)."""
        omega = mukai_pairing_matrix()
        nd = verify_nondegeneracy(omega)
        assert nd['signature'] == (4, 20)
        assert nd['is_nondegenerate'] is True

    def test_mukai_pairing_determinant(self):
        """Mukai pairing is unimodular: |det| = 1."""
        omega = mukai_pairing_matrix()
        nd = verify_nondegeneracy(omega)
        assert abs(nd['determinant']) == pytest.approx(1.0)

    def test_lambda_bracket_well_defined(self):
        """Lambda bracket from Mukai pairing is a valid chiral algebra."""
        omega = mukai_pairing_matrix()
        lb = lambda_bracket_from_pairing(omega)
        assert lb['is_well_defined_chiral_algebra'] is True
        assert lb['jacobi_automatic'] is True
        assert lb['is_symmetric'] is True

    def test_lambda_bracket_ope_count(self):
        """Number of independent OPE coefficients = 24*25/2 = 300."""
        omega = mukai_pairing_matrix()
        lb = lambda_bracket_from_pairing(omega)
        assert lb['num_ope_coefficients'] == 300

    def test_small_deformation_preserves_nondegeneracy(self):
        """Small deformations of omega preserve nondegeneracy."""
        omega = mukai_pairing_matrix()
        n = omega.shape[0]
        rng = np.random.RandomState(137)
        M = rng.randn(n, n)
        direction = (M + M.T) / 2.0
        omega_def = deformed_mukai_pairing(0.001, direction, omega)
        nd = verify_nondegeneracy(omega_def)
        assert nd['is_nondegenerate'] is True

    def test_deformation_unobstructed_numerical(self):
        """Numerical verification: all deformations satisfy Jacobi."""
        result = verify_deformation_unobstructed(num_directions=20)
        assert result['all_jacobi_hold'] is True
        assert result['all_nondegenerate'] is True


# =========================================================================
# Section 11: Full verification (integration)
# =========================================================================

class TestFullVerification:
    """Integration tests: full verification pipeline."""

    def test_full_verification_passes(self):
        """All component verifications pass."""
        v = full_verification()
        assert v.all_ok is True

    def test_full_verification_components(self):
        """Each individual component passes."""
        v = full_verification()
        assert v.dgla_ok is True
        assert v.tangent_ok is True
        assert v.unobstructed_ok is True
        assert v.k3_map_ok is True
        assert v.ade_ok is True
        assert v.vdim_ok is True
        assert v.kappa_ok is True
        assert v.numerical_ok is True
