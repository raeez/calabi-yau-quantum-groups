r"""Tests for k3_yangian_borcherds_weight_theta_refinement.

Verifies the Jacobi theta-component refinement c_N(0) = T_{H^*}(g_N) - 2 A_N
and the Borcherds weight identity kappa_BKM(Phi_N) = c_N(0)/2 on the CHL
ladder N in {1, 2, 3, 4, 6}.
"""

import pytest

from compute.lib.k3_yangian_borcherds_weight_theta_refinement import (
    CHL_LADDER,
    cross_volume_reconciliation_N1,
    kappa_BKM_table,
    verify_borcherds_weight,
    verify_frame_dim,
    verify_lefschetz_trace,
    verify_monotone_CHL,
    verify_physics_convention,
    verify_theta_refinement,
)


CHL_N_VALUES = [1, 2, 3, 4, 6]


class TestFrameDimConstraint:
    """sum_a a * m_a = 24 on the Mukai-rep lattice."""

    @pytest.mark.parametrize("N", CHL_N_VALUES)
    def test_frame_dim_equals_24(self, N):
        assert verify_frame_dim(N)


class TestLefschetzTrace:
    """T_{H^*}(g_N) = sum_a m_a (number of Mukai-rep cycles)."""

    @pytest.mark.parametrize("N,expected_T", [(1, 24), (2, 16), (3, 12), (4, 10), (6, 8)])
    def test_T_values(self, N, expected_T):
        assert CHL_LADDER[N].T_lefschetz == expected_T

    @pytest.mark.parametrize("N", CHL_N_VALUES)
    def test_T_equals_frame_cycle_count(self, N):
        assert verify_lefschetz_trace(N)


class TestThetaRefinement:
    """c_N(0) = T_{H^*}(g_N) - 2 A_N."""

    @pytest.mark.parametrize("N", CHL_N_VALUES)
    def test_refinement(self, N):
        assert verify_theta_refinement(N)

    @pytest.mark.parametrize("N,expected_c", [(1, 10), (2, 8), (3, 6), (4, 4), (6, 2)])
    def test_c_N_0_values(self, N, expected_c):
        assert CHL_LADDER[N].c_N_0 == expected_c

    @pytest.mark.parametrize("N,expected_A", [(1, 7), (2, 4), (3, 3), (4, 3), (6, 3)])
    def test_A_N_values(self, N, expected_A):
        assert CHL_LADDER[N].A_N == expected_A


class TestBorcherdsWeight:
    """kappa_BKM(Phi_N) = c_N(0) / 2."""

    @pytest.mark.parametrize("N", CHL_N_VALUES)
    def test_borcherds_weight_identity(self, N):
        assert verify_borcherds_weight(N)

    @pytest.mark.parametrize("N,expected_kb", [(1, 5), (2, 4), (3, 3), (4, 2), (6, 1)])
    def test_kappa_BKM_values(self, N, expected_kb):
        assert CHL_LADDER[N].kappa_BKM == expected_kb

    def test_CHL_monotone_decrease(self):
        """kappa_BKM strictly decreases on N = 1 -> 2 -> 3 -> 4 -> 6."""
        assert verify_monotone_CHL()


class TestPhysicsConvention:
    """Physics Igusa-square weight k^{phys} = c_N(0) = 2 * kappa_BKM."""

    @pytest.mark.parametrize("N", CHL_N_VALUES)
    def test_physics_convention(self, N):
        assert verify_physics_convention(N)

    @pytest.mark.parametrize("N,expected_k", [(1, 10), (2, 8), (3, 6), (4, 4), (6, 2)])
    def test_physics_k_values(self, N, expected_k):
        assert CHL_LADDER[N].physics_k == expected_k


class TestCrossVolumeReconciliation:
    """Vol I three-faces vs Vol III Borcherds-weight at N = 1."""

    def test_N1_reconciliation(self):
        recon = cross_volume_reconciliation_N1()
        assert recon["vol_III_Borcherds"] == 5
        assert recon["vol_I_three_faces"] == 12
        assert recon["chi_OX_K3xE"] == 0
        assert recon["reconciliation_delta"] == 7


class TestCHLLadderTable:
    """Tabulated tuple (N, T, c_N(0), A_N, kappa_BKM)."""

    def test_table_ordering(self):
        table = kappa_BKM_table()
        assert [row[0] for row in table] == [1, 2, 3, 4, 6]

    def test_table_values(self):
        table = kappa_BKM_table()
        expected = [
            (1, 24, 10, 7, 5),
            (2, 16, 8, 4, 4),
            (3, 12, 6, 3, 3),
            (4, 10, 4, 3, 2),
            (6, 8, 2, 3, 1),
        ]
        assert table == expected


class TestConsistencyWithDiagonalSiegel:
    """Cross-check against compute/lib/diagonal_siegel_cy_orbifolds.py."""

    @pytest.mark.parametrize("N", CHL_N_VALUES)
    def test_c_N_0_agrees_with_canonical_engine(self, N):
        from compute.lib.diagonal_siegel_cy_orbifolds import FRAME_SHAPE_DATA

        canonical = FRAME_SHAPE_DATA[N]
        refinement = CHL_LADDER[N]
        assert canonical.c_disc_0 == refinement.c_N_0, (
            f"c_N(0) mismatch at N={N}: canonical={canonical.c_disc_0}, "
            f"refinement={refinement.c_N_0}"
        )

    @pytest.mark.parametrize("N", CHL_N_VALUES)
    def test_weight_agrees_with_canonical_engine(self, N):
        from compute.lib.diagonal_siegel_cy_orbifolds import FRAME_SHAPE_DATA

        canonical = FRAME_SHAPE_DATA[N]
        refinement = CHL_LADDER[N]
        assert canonical.borcherds_weight == refinement.kappa_BKM, (
            f"weight mismatch at N={N}: canonical={canonical.borcherds_weight}, "
            f"refinement={refinement.kappa_BKM}"
        )

    @pytest.mark.parametrize("N", CHL_N_VALUES)
    def test_frame_shape_agrees_with_canonical_engine(self, N):
        from compute.lib.diagonal_siegel_cy_orbifolds import FRAME_SHAPE_DATA

        canonical = FRAME_SHAPE_DATA[N]
        refinement = CHL_LADDER[N]
        assert canonical.frame_shape == refinement.frame_shape, (
            f"frame shape mismatch at N={N}"
        )


class TestInvariantsUnderRegauging:
    """Identity c_N(0) = T - 2A_N is invariant under A_N <-> (T-c)/2 swap."""

    @pytest.mark.parametrize("N", CHL_N_VALUES)
    def test_A_N_derivable_from_T_c(self, N):
        d = CHL_LADDER[N]
        derived_A = (d.T_lefschetz - d.c_N_0) // 2
        assert derived_A == d.A_N

    @pytest.mark.parametrize("N", CHL_N_VALUES)
    def test_c_derivable_from_T_A(self, N):
        d = CHL_LADDER[N]
        derived_c = d.T_lefschetz - 2 * d.A_N
        assert derived_c == d.c_N_0
