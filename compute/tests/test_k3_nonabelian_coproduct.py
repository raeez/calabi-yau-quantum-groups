r"""Tests for K3 nonabelian coproduct engine.

STATUS: CONJECTURAL (AP-CY14). All results conditional on Y(g_{K3}).
The coproduct formulae themselves are standard Drinfeld coproducts;
the conjectural part is their realization within Y(g_{K3}).

Test organization:
  1. Lattice decomposition consistency (all ADE types)
  2. A_1 Drinfeld coproduct on evaluation rep (numerical)
  3. A_2 Drinfeld coproduct on fundamental rep (numerical)
  4. D_4 properties (Cartan null vector, triality)
  5. Cartan-Miura-Drinfeld consistency
  6. Generic point recovery
  7. Mixing vanishes at level 1
  8. Full verification suite
"""

from fractions import Fraction

import numpy as np

from compute.lib.k3_nonabelian_coproduct import (
    MUKAI_RANK,
    ADE_DATA,
    LatticeDecomposition,
    DrinfeldCoproductADE,
    MixingAnalysis,
    A1CoproductNumerical,
    A2CoproductSymbolic,
    D4CoproductSymbolic,
    FullK3Coproduct,
    verify_cartan_miura_drinfeld_consistency,
    ade_structure_function_landscape,
    k3_nonabelian_coproduct_full_verification,
)


# =========================================================================
# 1. Lattice decomposition
# =========================================================================

class TestLatticeDecomposition:
    """Lattice decomposition at ADE enhancement points."""

    def test_a1_decomposition(self):
        d = LatticeDecomposition('A1')
        assert d.rank == 1
        assert d.complement_rank == 23
        assert d.h_dual == 2
        # c(hat sl_{2,1}) = dim(sl_2)/(1 + h^v) = 3/3 = 1 = rank
        # VERIFIED: [DC] 3/3 = 1, [LT] Kac-Peterson
        r = d.verify_rank_consistency()
        assert r['ok']

    def test_a2_decomposition(self):
        d = LatticeDecomposition('A2')
        assert d.rank == 2
        assert d.complement_rank == 22
        assert d.h_dual == 3
        # c(hat sl_{3,1}) = 8/4 = 2 = rank
        # VERIFIED: [DC] 8/4 = 2, [LT] Kac-Peterson
        r = d.verify_rank_consistency()
        assert r['ok']

    def test_d4_decomposition(self):
        d = LatticeDecomposition('D4')
        assert d.rank == 4
        assert d.complement_rank == 20
        assert d.h_dual == 6
        # c(hat so_{8,1}) = 28/7 = 4 = rank
        # VERIFIED: [DC] 28/7 = 4, [LT] Kac-Peterson
        r = d.verify_rank_consistency()
        assert r['ok']

    def test_e6_decomposition(self):
        d = LatticeDecomposition('E6')
        assert d.rank == 6
        assert d.complement_rank == 18
        # c(hat E_{6,1}) = 78/13 = 6 = rank
        # VERIFIED: [DC] 78/13 = 6
        r = d.verify_rank_consistency()
        assert r['ok']

    def test_e7_decomposition(self):
        d = LatticeDecomposition('E7')
        assert d.rank == 7
        assert d.complement_rank == 17
        # c(hat E_{7,1}) = 133/19 = 7 = rank
        # VERIFIED: [DC] 133/19 = 7
        r = d.verify_rank_consistency()
        assert r['ok']

    def test_e8_decomposition(self):
        d = LatticeDecomposition('E8')
        assert d.rank == 8
        assert d.complement_rank == 16
        # c(hat E_{8,1}) = 248/31 = 8 = rank
        # VERIFIED: [DC] 248/31 = 8
        r = d.verify_rank_consistency()
        assert r['ok']

    def test_all_ade_rank_conservation(self):
        """Rank conservation: complement + ADE = 24 for all types."""
        for ade in ADE_DATA:
            d = LatticeDecomposition(ade)
            assert d.complement_rank + d.rank == MUKAI_RANK, (
                f'{ade}: {d.complement_rank} + {d.rank} != {MUKAI_RANK}'
            )

    def test_all_ade_central_charge_equals_rank(self):
        """c(hat g_1) = rank(g) for all simply-laced g at level 1."""
        for ade, data in ADE_DATA.items():
            c = Fraction(data['dim'], 1 + data['h_dual'])
            assert c == data['rank'], (
                f'{ade}: c = {data["dim"]}/{1 + data["h_dual"]} = {c} != {data["rank"]}'
            )


# =========================================================================
# 2. A_1 coproduct (numerical, evaluation rep)
# =========================================================================

class TestA1CoproductNumerical:
    """Numerical tests of Y(sl_2) Drinfeld coproduct on evaluation rep."""

    def test_cartan_primitive(self):
        """h is primitive (z-independent)."""
        a1 = A1CoproductNumerical()
        r = a1.verify_cartan_primitive()
        assert r['all_z_independent']

    def test_e_nonprimitive(self):
        """e is NOT primitive at z != 0."""
        a1 = A1CoproductNumerical()
        r = a1.verify_e_nonprimitive()
        assert r['delta_e_z1_differs']

    def test_commutation_at_z0(self):
        """[Delta_0(e), Delta_0(f)] = Delta_0(h) exactly at z=0."""
        a1 = A1CoproductNumerical()
        r = a1.verify_sl2_commutation_preserved(0.0)
        assert r['commutator_minus_dh_norm'] < 1e-12

    def test_commutation_leading_order(self):
        """[Delta_z(e), Delta_z(f)] = Delta_z(h) + O(z) from psi truncation."""
        a1 = A1CoproductNumerical()
        for z_val in [0.1, 0.2, 0.05]:
            r = a1.verify_sl2_commutation_preserved(z_val)
            # The error is O(z) from truncating psi to first order
            assert r['error_is_O_z'], f'Failed at z={z_val}'

    def test_abelian_limit(self):
        """With e=f=0, the coproduct reduces to abelian Miura."""
        a1 = A1CoproductNumerical()
        r = a1.verify_abelian_decomposition()
        assert r['abelian_limit_matches_miura']

    def test_yang_r_unitarity(self):
        """R(u) R_{21}(-u) = Id."""
        # AP-CY28: test point u=3+1j avoids poles
        a1 = A1CoproductNumerical()
        r = a1.verify_yang_r_unitarity(3.0 + 1.0j)
        assert r['ok']

    def test_yang_r_ybe(self):
        """YBE for 2x2 Yang R-matrix."""
        # AP-CY28: test points avoid poles
        a1 = A1CoproductNumerical()
        r = a1.verify_yang_r_ybe(2.0 + 0.5j, 3.0 + 0.7j)
        assert r['ok']

    def test_delta_e_z1_correction_structure(self):
        """The z^1 correction to Delta_z(e) is h^L/2 * e^R."""
        a1 = A1CoproductNumerical()
        de_0 = a1.delta_e_leading(0.0)
        de_z = a1.delta_e_leading(1.0)
        diff = de_z - de_0
        # Expected: z * h^L/2 * e^R = h^L/2 * e^R (at z=1)
        hL = np.kron(a1.h, a1.Id)
        eR = np.kron(a1.Id, a1.e)
        expected = 0.5 * (hL @ eR)
        err = float(np.max(np.abs(diff - expected)))
        assert err < 1e-12

    def test_delta_f_z1_correction_structure(self):
        """The z^1 correction to Delta_z(f) is -f^R * h^R/2."""
        a1 = A1CoproductNumerical()
        df_0 = a1.delta_f_leading(0.0)
        df_z = a1.delta_f_leading(1.0)
        diff = df_z - df_0
        # Expected: -z * f^R * h^R/2 = -f^R * h^R/2 (at z=1)
        hR = np.kron(a1.Id, a1.h)
        fR = np.kron(a1.Id, a1.f)
        expected = -0.5 * (fR @ hR)
        err = float(np.max(np.abs(diff - expected)))
        assert err < 1e-12

    def test_ef_asymmetry(self):
        """e and f coproducts are ASYMMETRIC (different z^1 corrections)."""
        a1 = A1CoproductNumerical()
        de_z = a1.delta_e_leading(1.0)
        df_z = a1.delta_f_leading(1.0)
        de_0 = a1.delta_e_leading(0.0)
        df_0 = a1.delta_f_leading(0.0)
        e_corr = de_z - de_0  # z * h^L/2 * e^R
        f_corr = df_z - df_0  # -z * f^R * h^R/2
        # These should NOT be related by simple transposition
        # (they act on different tensor factors)
        assert np.max(np.abs(e_corr - f_corr)) > 0.1


# =========================================================================
# 3. A_2 coproduct (numerical, fundamental rep)
# =========================================================================

class TestA2CoproductNumerical:
    """Numerical tests of Y(sl_3) Drinfeld coproduct on fundamental rep."""

    def test_cartan_primitive(self):
        """Both h_1 and h_2 are primitive."""
        a2 = A2CoproductSymbolic()
        r = a2.verify_cartan_primitive()
        assert r['all_primitive']

    def test_serre_relation(self):
        """[e_1, [e_1, e_2]] = 0 (A_2 Serre)."""
        a2 = A2CoproductSymbolic()
        r = a2.verify_serre_a2()
        assert r['ok']

    def test_commutation_e1_f1(self):
        """[Delta_0(e_1), Delta_0(f_1)] = Delta_0(h_1) at z=0."""
        a2 = A2CoproductSymbolic()
        r = a2.verify_commutation_preserved(1, 0.0)
        assert r['ok_leading_order']

    def test_commutation_e2_f2(self):
        """[Delta_0(e_2), Delta_0(f_2)] = Delta_0(h_2) at z=0."""
        a2 = A2CoproductSymbolic()
        r = a2.verify_commutation_preserved(2, 0.0)
        assert r['ok_leading_order']

    def test_cross_commutation_e1_f2(self):
        """[e_1, f_2] = 0 (different simple roots)."""
        a2 = A2CoproductSymbolic()
        comm = a2.e1 @ a2.f2 - a2.f2 @ a2.e1
        assert np.max(np.abs(comm)) < 1e-14

    def test_yang_r_ybe_3(self):
        """YBE for 3x3 Yang R-matrix."""
        a2 = A2CoproductSymbolic()
        r = a2.verify_yang_r_ybe_3()
        assert r['ok']

    def test_cartan_matrix_entries(self):
        """A_2 Cartan matrix is ((2,-1),(-1,2))."""
        a2 = A2CoproductSymbolic()
        assert a2.cartan == ((2, -1), (-1, 2))
        assert a2.rank == 2


# =========================================================================
# 4. D_4 properties
# =========================================================================

class TestD4Properties:
    """D_4 Cartan matrix, null vector, and triality."""

    def test_cartan_null_vector(self):
        """The null vector (1,1,2,1,1) of affine D_4^{(1)} (5x5 Cartan)."""
        d4 = D4CoproductSymbolic()
        r = d4.cartan_matrix_properties()
        # The null vector is for the AFFINE D_4^{(1)} Cartan (5x5),
        # not the finite D_4 Cartan (4x4, det=4, no kernel).
        assert r['null_is_kernel_affine']
        assert r['null_vector_affine'] == [1, 1, 2, 1, 1]

    def test_cartan_determinant(self):
        """det(C_{D_4}) = 4."""
        # VERIFIED: [DC] det of D_4 finite Cartan = 4, [LT] Bourbaki
        d4 = D4CoproductSymbolic()
        r = d4.cartan_matrix_properties()
        assert r['determinant_finite'] == 4

    def test_triality_orbits(self):
        """Triality permutes nodes {1, 3, 4}, fixes node 2."""
        d4 = D4CoproductSymbolic()
        r = d4.triality_orbits()
        assert r['fixed_node'] == 2
        assert sorted(r['permuted_nodes']) == [1, 3, 4]
        assert r['triality_order'] == 6

    def test_d4_complement_rank(self):
        """D_4 complement has rank 20."""
        d4 = D4CoproductSymbolic()
        assert d4.complement_rank == 20

    def test_d4_coproduct_table(self):
        """D_4 has 12 generators: 4 Cartan + 4 positive + 4 negative."""
        d4 = D4CoproductSymbolic()
        table = d4.coproduct_table_symbolic()
        assert table['total_generators'] == 12
        assert table['primitive'] == 4
        assert table['nonprimitive'] == 8


# =========================================================================
# 5. Cartan-Miura-Drinfeld consistency
# =========================================================================

class TestCartanConsistency:
    """Cartan sector of Drinfeld agrees with abelian Miura."""

    def test_cartan_miura_drinfeld(self):
        r = verify_cartan_miura_drinfeld_consistency()
        assert r['cartan_primitive_at_spin_1']
        assert r['abelian_decomposition_matches']
        assert r['consistency']


# =========================================================================
# 6. Generic point recovery
# =========================================================================

class TestGenericPoint:
    """At generic point, all 24 generators are abelian."""

    def test_generic_recovery(self):
        k3 = FullK3Coproduct('A1')
        r = k3.verify_generic_point_recovery()
        assert r['generic_point']
        assert r['matches_prop_universal_coproduct']
        assert r['no_root_vectors']

    def test_generic_no_cross_node(self):
        k3 = FullK3Coproduct('A1')
        r = k3.verify_generic_point_recovery()
        assert r['no_cross_node_structure_functions']


# =========================================================================
# 7. Mixing vanishes at level 1
# =========================================================================

class TestMixingVanishes:
    """Mixing between complement and ADE subalgebra vanishes at level 1."""

    def test_mixing_a1(self):
        m = MixingAnalysis(LatticeDecomposition('A1'))
        r = m.mixing_vanishes_at_level_1()
        assert r['mixing_vanishes']
        assert r['level'] == 1

    def test_mixing_a2(self):
        m = MixingAnalysis(LatticeDecomposition('A2'))
        r = m.mixing_vanishes_at_level_1()
        assert r['mixing_vanishes']

    def test_mixing_d4(self):
        m = MixingAnalysis(LatticeDecomposition('D4'))
        r = m.mixing_vanishes_at_level_1()
        assert r['mixing_vanishes']

    def test_factorization_a1(self):
        m = MixingAnalysis(LatticeDecomposition('A1'))
        r = m.coproduct_factorization_symbolic()
        assert r['cartan_overlap']['consistency']
        assert r['cartan_overlap']['rank'] == 1

    def test_factorization_d4(self):
        m = MixingAnalysis(LatticeDecomposition('D4'))
        r = m.coproduct_factorization_symbolic()
        assert r['cartan_overlap']['rank'] == 4


# =========================================================================
# 8. Full verification
# =========================================================================

class TestFullVerification:
    """Run full verification suite."""

    def test_full_suite(self):
        r = k3_nonabelian_coproduct_full_verification()
        assert r['summary']['all_checks_pass']

    def test_all_lattice_decompositions_pass(self):
        r = k3_nonabelian_coproduct_full_verification()
        for ade in ADE_DATA:
            assert r[f'lattice_{ade}']['ok'], f'{ade} lattice decomposition failed'


# =========================================================================
# 9. Coproduct table structure
# =========================================================================

class TestCoproductTable:
    """Structural tests of the coproduct tables."""

    def test_a1_table_size(self):
        d = DrinfeldCoproductADE(LatticeDecomposition('A1'))
        t = d.coproduct_table()
        assert t['total_generators'] == 3  # h, e, f for rank 1
        assert t['primitive_generators'] == 1

    def test_a2_table_size(self):
        d = DrinfeldCoproductADE(LatticeDecomposition('A2'))
        t = d.coproduct_table()
        assert t['total_generators'] == 6  # 2*(h,e,f)
        assert t['primitive_generators'] == 2

    def test_d4_table_size(self):
        d = DrinfeldCoproductADE(LatticeDecomposition('D4'))
        t = d.coproduct_table()
        assert t['total_generators'] == 12
        assert t['primitive_generators'] == 4
        assert t['nonprimitive_generators'] == 8

    def test_h_matches_abelian_miura(self):
        """All Cartan coproducts agree with abelian Miura."""
        for ade in ['A1', 'A2', 'D4']:
            d = DrinfeldCoproductADE(LatticeDecomposition(ade))
            decomp = LatticeDecomposition(ade)
            for i in range(decomp.rank):
                h_cop = d.coproduct_h_symbolic(i)
                assert h_cop['matches_abelian_miura']

    def test_e_is_nonprimitive(self):
        """All positive root coproducts are Cartan-weighted (nonprimitive)."""
        for ade in ['A1', 'A2', 'D4']:
            d = DrinfeldCoproductADE(LatticeDecomposition(ade))
            decomp = LatticeDecomposition(ade)
            for i in range(decomp.rank):
                e_cop = d.coproduct_e_symbolic(i)
                assert 'nonabelian' in e_cop['type'].lower()


# =========================================================================
# 10. Structure function landscape
# =========================================================================

class TestStructureFunctionLandscape:
    """Cross-ADE structure function comparison."""

    def test_landscape_has_all_types(self):
        r = ade_structure_function_landscape()
        assert 'A1' in r
        assert 'A2' in r
        assert 'D4' in r
        assert 'generic' in r

    def test_a1_inversion(self):
        """For A_1: g_{01} = 1/g_{00} (full inversion)."""
        r = ade_structure_function_landscape()
        g00 = Fraction(r['A1']['g_00_at_z3'])
        g01 = Fraction(r['A1']['g_01_at_z3'])
        assert g00 * g01 == 1


# =========================================================================
# 11. Full K3 coproduct synthesis
# =========================================================================

class TestFullK3Coproduct:
    """Tests of the full K3 coproduct at ADE enhancement points."""

    def test_a1_structure(self):
        k3 = FullK3Coproduct('A1')
        s = k3.full_coproduct_structure()
        assert s['ade_type'] == 'A1'
        assert s['mukai_rank'] == 24
        assert s['coproduct']['complement']['rank'] == 23
        assert s['coproduct']['mixing']['mixing_vanishes']

    def test_d4_structure(self):
        k3 = FullK3Coproduct('D4')
        s = k3.full_coproduct_structure()
        assert s['ade_type'] == 'D4'
        assert s['coproduct']['complement']['rank'] == 20

    def test_consistency_checks(self):
        for ade in ['A1', 'A2', 'D4']:
            k3 = FullK3Coproduct(ade)
            s = k3.full_coproduct_structure()
            assert s['consistency_checks']['rank_conservation']['ok']
