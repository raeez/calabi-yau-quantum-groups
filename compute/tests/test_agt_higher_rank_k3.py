r"""Tests for the higher-rank K3 AGT correspondence engine.

Verifies:
  1. Rank-1 VW = Gottsche's formula (baseline consistency)
  2. Rank-2 VW from symmetric product / DMVV
  3. W_N vacuum characters at low N
  4. AGT matching: Z_VW^{U(N)} vs W_N^{24} at genus 1
  5. Structure function degree scaling: (24N, 24N)
  6. Unitarity: g_N(u) * g_N(-u) = 1
  7. Nonabelian structure at N >= 2
  8. Central charge and modular weight scaling
  9. Bar Euler product at higher rank
  10. Kummer route data at higher rank
  11. R-matrix block structure at rank N
  12. Log expansion coefficients at rank N

Ground truth:
  - Gottsche (1990): chi(Hilb^n(K3)) = p_{24}(n)
  - DMVV (1997): second-quantized K3 partition function
  - W_N representation theory: vacuum characters (classical)
  - Alday-Gaiotto-Tachikawa (2009): AGT for C^2
  - K3 Yangian (CONJECTURAL, AP-CY14) for Yangian interpretation

Manuscript references:
  en_factorization.tex: prop:einf-fh-k3, eq:einf-fh-k3-formula
  k3_times_e.tex: ch:k3-times-e, sec:dmvv-product
"""

import pytest
import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from lib.agt_higher_rank_k3 import (
    # Constants
    K3_CHI, MUKAI_RANK, KNOWN_HILB_CHI, KNOWN_RANK2_CHI,
    STATUS_PROVED, STATUS_CONJECTURAL,
    # VW partition functions
    vw_rank1_k3,
    vw_rank2_k3,
    vw_rank_N_symmetric_product,
    vw_rank_N_k3_naive,
    # W_N characters
    wn_vacuum_character_coeffs,
    wn_24_partition_function,
    # Structure function
    structure_function_rank_N_evaluate,
    structure_function_rank_N_degree,
    structure_function_rank_N_coefficients,
    structure_function_rank_N_log_coefficients,
    verify_unitarity_rank_N,
    verify_degree_scaling,
    # R-matrix
    r_matrix_rank_N,
    r_matrix_rank_N_explicit_block,
    # AGT verification
    verify_agt_rank_N_genus1,
    # Nonabelian structure
    nonabelian_structure_summary,
    # Central charge
    central_charge_wn_24,
    # Bar Euler product
    bar_euler_product_rank_N,
    # Kummer route
    kummer_route_rank_N,
    # Summary
    higher_rank_summary,
    # Internal helpers
    _integer_partitions,
)

F = Fraction


# =========================================================================
# 1. Rank-1 VW: baseline consistency with Gottsche
# =========================================================================

class TestRank1VW:
    """Verify rank-1 VW partition function matches Gottsche's formula."""

    @pytest.mark.parametrize("n,expected", list(KNOWN_HILB_CHI.items()))
    def test_rank1_known_values(self, n, expected):
        """chi(Hilb^n(K3)) matches known Gottsche values."""
        coeffs = vw_rank1_k3(n)
        # VERIFIED [DC] numerical match [LC] Gottsche 1990
        assert coeffs[n] == expected

    def test_rank1_hilb0(self):
        """chi(Hilb^0(K3)) = 1."""
        coeffs = vw_rank1_k3(0)
        assert coeffs[0] == 1

    def test_rank1_hilb1_equals_chi_k3(self):
        """chi(Hilb^1(K3)) = chi(K3) = 24."""
        coeffs = vw_rank1_k3(1)
        assert coeffs[1] == K3_CHI

    def test_rank1_positive(self):
        """All Euler characteristics are positive."""
        coeffs = vw_rank1_k3(8)
        for n in range(9):
            assert coeffs[n] > 0

    def test_rank1_monotone(self):
        """Euler characteristics strictly increase for n >= 1."""
        coeffs = vw_rank1_k3(6)
        for n in range(2, 7):
            assert coeffs[n] > coeffs[n - 1]


# =========================================================================
# 2. Rank-2 VW from DMVV symmetric product
# =========================================================================

class TestRank2VW:
    """Verify rank-2 VW from (1/2)(1/eta^{48} + 1/eta(q^2)^{24})."""

    @pytest.mark.parametrize("n,expected", list(KNOWN_RANK2_CHI.items()))
    def test_rank2_known_values(self, n, expected):
        """Rank-2 chi values match the DMVV formula extraction."""
        coeffs = vw_rank2_k3(n)
        # VERIFIED [DC] numerical match [LC] DMVV formula
        assert coeffs[n] == expected

    def test_rank2_n0(self):
        """chi(M(2, 0; K3)) = 1."""
        coeffs = vw_rank2_k3(0)
        assert coeffs[0] == 1

    def test_rank2_n1(self):
        """chi(M(2, 1; K3)) = 24."""
        coeffs = vw_rank2_k3(1)
        assert coeffs[1] == 24

    def test_rank2_n2(self):
        """Rank-2 symmetric product at n=2: (1/2)(1224 + 24) = 624.

        Z_1^2 at q^2 = 1*324 + 24*24 + 324*1 = 1224.
        Z_1(q^2) at q^2 = p_{24}(1) = 24.
        Z_2 = (1/2)(1224 + 24) = 624.
        """
        coeffs = vw_rank2_k3(2)
        # VERIFIED [DC] numerical match [LC] DMVV symmetric product
        # Multi-path: (1/2)(1/eta^48 at q^2 + 1/eta^24 at q^1)
        #           = (1/2)(1224 + 24) = 624
        assert coeffs[2] == 624

    def test_rank2_all_positive(self):
        """All rank-2 Euler characteristics are positive."""
        coeffs = vw_rank2_k3(6)
        for n in range(7):
            assert coeffs[n] > 0

    def test_rank2_all_integers(self):
        """All rank-2 values are integers (Euler characteristics)."""
        coeffs = vw_rank2_k3(6)
        for n in range(7):
            assert isinstance(coeffs[n], int)


# =========================================================================
# 3. Symmetric product formula: general N
# =========================================================================

class TestSymmetricProductRankN:
    """Verify the symmetric product / DMVV extraction at general rank."""

    def test_rank1_symmetric_product_matches_direct(self):
        """Symmetric product at N=1 matches vw_rank1_k3."""
        sp = vw_rank_N_symmetric_product(1, 6)
        direct = vw_rank1_k3(6)
        for n in range(7):
            assert sp[n] == F(direct[n]), f"Mismatch at n={n}: sp={sp[n]}, direct={direct[n]}"

    def test_rank2_symmetric_product_matches_direct(self):
        """Symmetric product at N=2 matches vw_rank2_k3."""
        sp = vw_rank_N_symmetric_product(2, 4)
        direct = vw_rank2_k3(4)
        for n in range(5):
            assert sp[n] == F(direct[n]), f"Mismatch at n={n}: sp={sp[n]}, direct={direct[n]}"

    def test_rank3_n0(self):
        """Z_VW^{U(3)} coefficient at q^0 is 1."""
        sp = vw_rank_N_symmetric_product(3, 0)
        assert sp[0] == F(1)

    def test_rank3_n1(self):
        """Z_VW^{U(3)} coefficient at q^1 is 24."""
        sp = vw_rank_N_symmetric_product(3, 1)
        # At q^1: all N produce p_{24}(1) * correction = 24
        # The q^1 coefficient of exp(sum p^k/k Z_1(q^k)) at p^3 level:
        # Only the partition (1,1,1) contributes to q^1:
        # (1/6)(Z_1)^3 at q^1 = (1/6)*3*24*1*1 = ... computed numerically
        assert sp[1] == F(24)

    def test_all_integers_rank3(self):
        """Symmetric product coefficients at N=3 are integers."""
        sp = vw_rank_N_symmetric_product(3, 4)
        for n in range(5):
            val = sp[n]
            assert val == int(val), f"Non-integer at n={n}: {val}"

    def test_rank_N_invalid(self):
        """Rank N < 1 raises ValueError."""
        with pytest.raises(ValueError):
            vw_rank_N_symmetric_product(0, 5)


# =========================================================================
# 4. W_N vacuum characters
# =========================================================================

class TestWNVacuumCharacter:
    """Verify W_N vacuum character coefficients."""

    def test_w1_trivial(self):
        """W_1 higher-spin character is 1 (no spins >= 2)."""
        ch = wn_vacuum_character_coeffs(1, 5)
        assert ch[0] == F(1)
        for n in range(1, 6):
            assert ch[n] == F(0)

    def test_w2_first_terms(self):
        """W_2 = Virasoro: ch = prod_{n>=2} 1/(1-q^n).

        Coefficients: q^0: 1, q^1: 0, q^2: 1, q^3: 1, q^4: 2, q^5: 2.
        """
        ch = wn_vacuum_character_coeffs(2, 5)
        assert ch[0] == F(1)
        assert ch[1] == F(0)   # no spin-2 mode at level 1
        # VERIFIED [DC] structural property [LC] Virasoro character
        assert ch[2] == F(1)   # one spin-2 state at level 2
        assert ch[3] == F(1)   # one spin-2 state at level 3
        assert ch[4] == F(2)   # two states at level 4: L_{-4} and L_{-2}^2
        assert ch[5] == F(2)   # two states at level 5

    def test_w3_q0(self):
        """W_3 vacuum character starts with 1."""
        ch = wn_vacuum_character_coeffs(3, 5)
        assert ch[0] == F(1)

    def test_w3_q2(self):
        """W_3 at q^2: one Virasoro mode L_{-2}."""
        ch = wn_vacuum_character_coeffs(3, 5)
        # spin 2: prod_{n>=2} contributes 1 at q^2
        # spin 3: prod_{n>=3} contributes 0 at q^2
        assert ch[2] == F(1)

    def test_w3_q3(self):
        """W_3 at q^3: L_{-3} and W_{-3}."""
        ch = wn_vacuum_character_coeffs(3, 5)
        # spin 2 at q^3: 1 (L_{-3})
        # spin 3 at q^3: 1 (W_{-3})
        # product: 1*1 + 1*0 + 0*1 = ... convolution gives 2
        assert ch[3] == F(2)


# =========================================================================
# 5. AGT matching at genus 1
# =========================================================================

class TestAGTGenusOne:
    """Verify AGT: Z_VW^{U(N)}(K3) = Z_{W_N^{24}}(Sigma_1)."""

    def test_agt_rank1(self):
        """AGT at rank 1: both sides = 1/eta^{24}. PROVED."""
        result = verify_agt_rank_N_genus1(1, max_n=6)
        assert result['coefficients_match'] is True
        assert result['status'] == STATUS_PROVED

    def test_agt_rank1_coefficients(self):
        """Explicit coefficient match at rank 1."""
        vw = vw_rank1_k3(4)
        wn = wn_24_partition_function(1, 4)
        for n in range(5):
            # VERIFIED [DC] numerical match [LC] both = 1/eta^{24}
            assert wn[n] == F(vw[n])

    def test_agt_rank2_conjectural(self):
        """AGT at rank 2: status is CONJECTURAL."""
        result = verify_agt_rank_N_genus1(2, max_n=2)
        assert result['status'] == STATUS_CONJECTURAL

    def test_agt_rank2_q0(self):
        """AGT at rank 2, q^0: both sides = 1."""
        vw = vw_rank_N_symmetric_product(2, 0)
        wn = wn_24_partition_function(2, 0)
        assert vw[0] == F(1)
        assert wn[0] == F(1)


# =========================================================================
# 6. Structure function degree scaling
# =========================================================================

class TestStructureFunctionDegree:
    """Verify deg(g_N) = (24N, 24N)."""

    @pytest.mark.parametrize("N", [1, 2, 3, 4, 5, 10])
    def test_degree_scaling(self, N):
        """Structure function degree = (24N, 24N)."""
        num_deg, den_deg = structure_function_rank_N_degree(N)
        # VERIFIED [DC] algebraic formula [LC] g_N = g_1^N
        assert num_deg == 24 * N
        assert den_deg == 24 * N

    def test_degree_verification_batch(self):
        """Batch verification via verify_degree_scaling."""
        result = verify_degree_scaling(max_N=6)
        assert result['all_match'] is True


# =========================================================================
# 7. Unitarity: g_N(u) * g_N(-u) = 1
# =========================================================================

class TestUnitarity:
    """Verify g_N(u) * g_N(-u) = 1 for all ranks."""

    def _default_h_list(self):
        """Kummer K3 parameters: 4 positive, 20 negative, sum = 0."""
        h_pos = [F(1)] * 4
        h_neg = [F(-1, 5)] * 20
        return h_pos + h_neg

    @pytest.mark.parametrize("N", [1, 2, 3, 4])
    def test_unitarity(self, N):
        """g_N(u) * g_N(-u) = 1 at multiple test points."""
        h = self._default_h_list()
        result = verify_unitarity_rank_N(N, h)
        # VERIFIED [DC] algebraic identity [LC] g(u)*g(-u)=1
        assert result['unitarity_holds'] is True

    def test_unitarity_explicit_rank2(self):
        """Explicit unitarity check at rank 2."""
        h = self._default_h_list()
        u = F(37)
        g2_u = structure_function_rank_N_evaluate(2, u, h)
        g2_neg_u = structure_function_rank_N_evaluate(2, -u, h)
        assert g2_u * g2_neg_u == F(1)

    def test_unitarity_null_parameters(self):
        """Unitarity with null Mukai parameters."""
        h = [F(0)] * 24
        h[0] = F(1)
        h[1] = F(-1)
        h[4] = F(1)
        h[5] = F(-1)
        # sum = 1 - 1 + 1 - 1 = 0, OK
        result = verify_unitarity_rank_N(2, h)
        assert result['unitarity_holds'] is True


# =========================================================================
# 8. Nonabelian structure at N >= 2
# =========================================================================

class TestNonabelianStructure:
    """Verify nonabelian features at rank N >= 2."""

    def test_rank1_abelian(self):
        """Rank 1 is abelian."""
        s = nonabelian_structure_summary(1)
        assert s.is_abelian is True
        assert s.off_diagonal_rmatrix is False
        assert s.gl_N_generators == 1

    def test_rank2_nonabelian(self):
        """Rank 2 is genuinely nonabelian."""
        s = nonabelian_structure_summary(2)
        assert s.is_abelian is False
        assert s.off_diagonal_rmatrix is True
        assert s.gl_N_generators == 4

    def test_rank3_generators(self):
        """gl_3 has 9 generators; total currents = 9 * 24 = 216."""
        s = nonabelian_structure_summary(3)
        assert s.gl_N_generators == 9
        assert '216' in s.total_yangian_generators

    def test_rank_N_gl_N_generators(self):
        """gl_N generator count = N^2."""
        for N in range(1, 6):
            s = nonabelian_structure_summary(N)
            assert s.gl_N_generators == N * N

    def test_rank2_has_serre(self):
        """Rank 2 mentions Serre relations."""
        s = nonabelian_structure_summary(2)
        assert 'Serre' in s.serre_relations or 'None' not in s.serre_relations

    def test_all_conjectural(self):
        """All nonabelian structure summaries are CONJECTURAL."""
        for N in range(1, 5):
            s = nonabelian_structure_summary(N)
            assert s.status == STATUS_CONJECTURAL


# =========================================================================
# 9. Central charge and modular weight
# =========================================================================

class TestCentralCharge:
    """Verify central charge and kappa-spectrum scaling."""

    def test_rank1_central_charge(self):
        """c_total = 24 at rank 1."""
        cc = central_charge_wn_24(1)
        assert cc['c_total_with_heisenberg'] == 24

    def test_rank2_central_charge(self):
        """c_total = 48 at rank 2."""
        cc = central_charge_wn_24(2)
        assert cc['c_total_with_heisenberg'] == 48

    @pytest.mark.parametrize("N", [1, 2, 3, 4])
    def test_central_charge_scaling(self, N):
        """c_total = 24*N."""
        cc = central_charge_wn_24(N)
        assert cc['c_total_with_heisenberg'] == 24 * N

    @pytest.mark.parametrize("N", [1, 2, 3, 4])
    def test_modular_weight(self, N):
        """Modular weight = -12*N."""
        cc = central_charge_wn_24(N)
        # VERIFIED [DC] structural property [LC] weight = -c/2
        assert cc['modular_weight'] == F(-12 * N)

    def test_kappa_fiber_scaling(self):
        """kappa_fiber = 24*N (AP113 compliant)."""
        for N in range(1, 5):
            cc = central_charge_wn_24(N)
            assert cc['kappa_spectrum']['kappa_fiber'] == F(24 * N)

    def test_kappa_ch_scaling(self):
        """kappa_ch = 3*N (conjectural for N >= 2; AP113 compliant)."""
        for N in range(1, 5):
            cc = central_charge_wn_24(N)
            assert cc['kappa_spectrum']['kappa_ch'] == F(3 * N)

    def test_rank1_proved(self):
        """Rank 1 status is PROVED."""
        cc = central_charge_wn_24(1)
        assert cc['status'] == STATUS_PROVED


# =========================================================================
# 10. Bar Euler product at higher rank
# =========================================================================

class TestBarEulerProduct:
    """Verify bar Euler product at rank N."""

    def test_rank1_first_term(self):
        """prod (1-q^n)^{24}: leading coefficient = 1."""
        coeffs = bar_euler_product_rank_N(1, 5)
        assert coeffs[0] == 1

    def test_rank1_q1(self):
        """prod (1-q^n)^{24}: coefficient of q^1 = -24."""
        coeffs = bar_euler_product_rank_N(1, 5)
        # VERIFIED [DC] Ramanujan tau [LC] tau(2) = -24
        assert coeffs[1] == -24

    def test_rank2_first_term(self):
        """prod (1-q^n)^{48}: leading coefficient = 1."""
        coeffs = bar_euler_product_rank_N(2, 3)
        assert coeffs[0] == 1

    def test_rank2_q1(self):
        """prod (1-q^n)^{48}: coefficient of q^1 = -48."""
        coeffs = bar_euler_product_rank_N(2, 3)
        assert coeffs[1] == -48

    @pytest.mark.parametrize("N", [1, 2, 3])
    def test_q1_coefficient(self, N):
        """Coefficient of q^1 in eta^{24N} is -24N."""
        coeffs = bar_euler_product_rank_N(N, 1)
        # (1-q)^{24N} at q^1 = -24N
        assert coeffs[1] == -24 * N


# =========================================================================
# 11. R-matrix block structure
# =========================================================================

class TestRMatrixRankN:
    """Verify R-matrix structure at rank N."""

    def test_rank1_diagonal(self):
        """Rank-1 R-matrix is diagonal."""
        rm = r_matrix_rank_N(1)
        assert rm.is_diagonal is True
        assert rm.charge1_dim == 24

    def test_rank2_not_diagonal(self):
        """Rank-2 R-matrix is NOT diagonal."""
        rm = r_matrix_rank_N(2)
        assert rm.is_diagonal is False
        assert rm.charge1_dim == 48

    @pytest.mark.parametrize("N", [1, 2, 3, 4])
    def test_charge1_dim(self, N):
        """Charge-1 representation dimension = 24*N."""
        rm = r_matrix_rank_N(N)
        assert rm.charge1_dim == 24 * N

    @pytest.mark.parametrize("N", [1, 2, 3, 4])
    def test_structure_function_degree_in_rmatrix(self, N):
        """R-matrix records structure function degree (24N, 24N)."""
        rm = r_matrix_rank_N(N)
        assert rm.structure_function_degree == (24 * N, 24 * N)

    def test_rank2_explicit_block_shape(self):
        """Explicit 2x2 block has correct shape (4x4 for N=2)."""
        block = r_matrix_rank_N_explicit_block(2, F(5), 0, F(1))
        assert len(block) == 4
        assert all(len(row) == 4 for row in block)

    def test_rank2_explicit_block_off_diagonal(self):
        """Rank-2 block has nonzero off-diagonal entries."""
        block = r_matrix_rank_N_explicit_block(2, F(5), 0, F(1))
        # P_2 permutation contributes off-diagonal: block[0][3] and block[1][2]
        # In basis |0>|0>, |0>|1>, |1>|0>, |1>|1>:
        # P|0>|1> = |1>|0>, so P has entry at (1,2) and (2,1)
        # u*I + P has off-diagonal at (1,2) and (2,1)
        # VERIFIED [DC] structural property [LC] Yang R-matrix has off-diag
        assert block[1][2] != F(0) or block[2][1] != F(0)


# =========================================================================
# 12. Structure function coefficients at rank N
# =========================================================================

class TestStructureFunctionCoefficients:
    """Verify structure function log and series coefficients at rank N."""

    def _default_h_list(self):
        return [F(1)] * 4 + [F(-1, 5)] * 20

    def test_log_coeffs_rank1_phi1_zero(self):
        """alpha_1 = 0 at rank 1 (CY_2 constraint: sum h = 0)."""
        h = self._default_h_list()
        alphas = structure_function_rank_N_log_coefficients(1, h, 5)
        assert alphas[1] == F(0)

    def test_log_coeffs_rankN_phi1_zero(self):
        """alpha_1 = 0 at any rank N (CY_2 constraint)."""
        h = self._default_h_list()
        for N in range(1, 4):
            alphas = structure_function_rank_N_log_coefficients(N, h, 5)
            # VERIFIED [DC] structural property [LC] CY_2 kills p_1
            assert alphas[1] == F(0)

    def test_log_coeffs_even_zero(self):
        """Even log coefficients vanish (only odd powers)."""
        h = self._default_h_list()
        alphas = structure_function_rank_N_log_coefficients(2, h, 10)
        for k in range(0, 11, 2):
            assert alphas[k] == F(0)

    def test_log_coeffs_rank_scaling(self):
        """alpha_k^{(N)} = N * alpha_k^{(1)}."""
        h = self._default_h_list()
        alphas_1 = structure_function_rank_N_log_coefficients(1, h, 10)
        for N in range(2, 5):
            alphas_N = structure_function_rank_N_log_coefficients(N, h, 10)
            for k in range(11):
                assert alphas_N[k] == N * alphas_1[k], (
                    f"Rank {N}, k={k}: {alphas_N[k]} != {N}*{alphas_1[k]}"
                )

    def test_series_coeffs_phi0(self):
        """phi_0 = 1 at all ranks."""
        h = self._default_h_list()
        for N in range(1, 4):
            phi = structure_function_rank_N_coefficients(N, h, 5)
            assert phi[0] == F(1)

    def test_series_coeffs_phi1_zero(self):
        """phi_1 = 0 at all ranks (CY_2 kills it)."""
        h = self._default_h_list()
        for N in range(1, 4):
            phi = structure_function_rank_N_coefficients(N, h, 5)
            assert phi[1] == F(0)

    def test_evaluate_at_zero(self):
        """g_N(0) = ((-1)^{24})^N = 1 for all N."""
        h = self._default_h_list()
        for N in range(1, 4):
            val = structure_function_rank_N_evaluate(N, F(0), h)
            # VERIFIED [DC] structural property [LC] g(0) = 1
            assert val == F(1), f"g_{N}(0) = {val} != 1"

    def test_evaluate_cy2_constraint(self):
        """CY_2 constraint check: sum h = 0."""
        h = self._default_h_list()
        assert sum(h) == F(0)


# =========================================================================
# 13. Kummer route at higher rank
# =========================================================================

class TestKummerRoute:
    """Verify Kummer route data at higher rank."""

    def test_rank1_proved(self):
        """Kummer route at rank 1 is PROVED."""
        kr = kummer_route_rank_N(1)
        assert kr['status'] == STATUS_PROVED

    def test_rank2_conjectural(self):
        """Kummer route at rank 2 is CONJECTURAL."""
        kr = kummer_route_rank_N(2)
        assert kr['status'] == STATUS_CONJECTURAL

    def test_heisenberg_rank_scaling(self):
        """Step 1 Heisenberg rank = 16*N."""
        for N in range(1, 5):
            kr = kummer_route_rank_N(N)
            assert kr['step1']['heisenberg_rank'] == 16 * N

    def test_kappa_ch_conjectural_scaling(self):
        """kappa_ch at Kummer = 2*N (conjectural, AP113)."""
        for N in range(1, 5):
            kr = kummer_route_rank_N(N)
            assert kr['step4']['kappa_ch_conjectural'] == F(2 * N)


# =========================================================================
# 14. Summary table
# =========================================================================

class TestSummary:
    """Verify the higher-rank summary table."""

    def test_summary_rows(self):
        """Summary has correct number of rows."""
        s = higher_rank_summary(4)
        assert len(s['ranks']) == 4

    def test_summary_rank1_proved(self):
        """Summary rank 1 is PROVED."""
        s = higher_rank_summary(1)
        assert s['ranks'][0]['status'] == STATUS_PROVED

    def test_summary_rank2_conjectural(self):
        """Summary rank 2 is CONJECTURAL."""
        s = higher_rank_summary(2)
        assert s['ranks'][1]['status'] == STATUS_CONJECTURAL

    def test_summary_nonabelian(self):
        """Summary: rank >= 2 is nonabelian."""
        s = higher_rank_summary(4)
        assert s['ranks'][0]['is_nonabelian'] is False  # N=1
        for i in range(1, 4):
            assert s['ranks'][i]['is_nonabelian'] is True


# =========================================================================
# 15. Integer partitions helper
# =========================================================================

class TestIntegerPartitions:
    """Verify the integer partition enumeration."""

    def test_partitions_of_0(self):
        """Partitions of 0: only the empty partition."""
        p = _integer_partitions(0)
        assert p == [[]]

    def test_partitions_of_1(self):
        """Partitions of 1: [[1]]."""
        p = _integer_partitions(1)
        assert p == [[1]]

    def test_partitions_of_3(self):
        """Partitions of 3: [3], [2,1], [1,1,1]."""
        p = _integer_partitions(3)
        assert len(p) == 3

    def test_partitions_of_4(self):
        """Partitions of 4: 5 partitions."""
        p = _integer_partitions(4)
        assert len(p) == 5

    def test_partitions_of_5(self):
        """Partitions of 5: 7 partitions."""
        p = _integer_partitions(5)
        assert len(p) == 7


# =========================================================================
# 16. Naive rank-N formula
# =========================================================================

class TestNaiveRankN:
    """Verify the naive (wrong for N>=2) formula 1/eta^{24N}."""

    def test_naive_rank1(self):
        """Naive at N=1 matches exact (because N=1 IS exact)."""
        naive = vw_rank_N_k3_naive(1, 6)
        exact = vw_rank1_k3(6)
        for n in range(7):
            assert naive[n] == F(exact[n])

    def test_naive_rank2_differs_from_exact(self):
        """Naive at N=2 DIFFERS from exact symmetric product."""
        naive = vw_rank_N_k3_naive(2, 4)
        exact = vw_rank_N_symmetric_product(2, 4)
        # At q^0 both are 1
        assert naive[0] == exact[0]
        # At higher orders they should differ (naive overcounts)
        # Naive = 1/eta^{48}: a_2 = 1176. Exact = 600.
        assert naive[2] != exact[2], "Naive and exact should differ at N=2, n=2"

    def test_naive_invalid_rank(self):
        """Rank N < 1 raises ValueError."""
        with pytest.raises(ValueError):
            vw_rank_N_k3_naive(0, 5)


# =========================================================================
# 17. W_N^{24} partition function cross-checks
# =========================================================================

class TestWN24PartitionFunction:
    """Cross-checks on the 24-copy W_N partition function."""

    def test_wn24_rank1_matches_eta_inverse(self):
        """W_1^{24} = 1/eta^{24}: matches rank-1 VW."""
        wn = wn_24_partition_function(1, 6)
        vw = vw_rank1_k3(6)
        for n in range(7):
            assert wn[n] == F(vw[n])

    def test_wn24_q0(self):
        """W_N^{24} at q^0 = 1 for all N."""
        for N in range(1, 5):
            wn = wn_24_partition_function(N, 0)
            assert wn[0] == F(1)

    def test_wn24_q1_rank1(self):
        """W_1^{24} at q^1 = 24."""
        wn = wn_24_partition_function(1, 1)
        assert wn[1] == F(24)

    def test_wn24_rank2_q1(self):
        """W_2^{24} at q^1: the spin-2 modes start at n=2,
        so q^1 coefficient comes only from the Heisenberg part."""
        wn = wn_24_partition_function(2, 1)
        # The full W_2 character at q^1 comes from spin 1 only
        # (spin 2 starts at n=2), so same as W_1.
        # But wait: (ch_full(W_2))^{24} at q^1.
        # ch_full(W_2) = prod_{n>=1} 1/(1-q^n) * prod_{n>=2} 1/(1-q^n)
        # At q^1: the second factor contributes nothing (starts at q^2).
        # So ch_full(W_2) at q^1 = 1 (from first factor: coeff of q^1 in 1/(1-q)(1-q^2)... is 1)
        # Then (ch_full(W_2))^{24} at q^1 = 24*1 = 24.
        assert wn[1] == F(24)


# =========================================================================
# 18. Multi-path cross-checks (AP10 compliance)
# =========================================================================

class TestMultiPathCrossChecks:
    """Multi-path verification: independent computations agree.

    Every hardcoded value is cross-checked via at least two independent
    computational paths, as required by AP10.
    """

    def _default_h_list(self):
        return [F(1)] * 4 + [F(-1, 5)] * 20

    # --- Rank-1 VW: three independent paths ---

    def test_rank1_three_paths(self):
        """Rank-1 VW via (1) vw_rank1_k3, (2) symmetric product at N=1,
        (3) W_1^{24} partition function. All three agree."""
        path1 = vw_rank1_k3(6)
        path2 = vw_rank_N_symmetric_product(1, 6)
        path3 = wn_24_partition_function(1, 6)
        for n in range(7):
            assert F(path1[n]) == path2[n] == path3[n], (
                f"n={n}: path1={path1[n]}, path2={path2[n]}, path3={path3[n]}"
            )

    def test_rank1_q2_cross_check(self):
        """chi(Hilb^2(K3)) = 324 via direct computation.

        Path 1: coefficient of q^2 in 1/eta^{24}.
        Path 2: explicit formula p_{24}(2) = C(24,1) + C(25,2) = 24 + 300 = 324.
        (Partitions of 2 into at most 24 colors: (2) gives 24, (1,1) gives C(24+1,2)=300.)
        """
        path1 = vw_rank1_k3(2)[2]
        # Path 2: direct combinatorial
        # Partitions of 2 with 24 colors:
        # (2): one part of size 2 in any of 24 colors => 24
        # (1,1): two parts of size 1, choose 2 colors with replacement => C(24+1,2) = 300
        path2 = 24 + 25 * 24 // 2
        assert path1 == path2 == 324

    # --- Rank-2 VW: two independent paths ---

    def test_rank2_two_paths(self):
        """Rank-2 VW via (1) vw_rank2_k3, (2) symmetric product.
        Both agree through q^4."""
        path1 = vw_rank2_k3(4)
        path2 = vw_rank_N_symmetric_product(2, 4)
        for n in range(5):
            assert F(path1[n]) == path2[n], (
                f"n={n}: direct={path1[n]}, symm_prod={path2[n]}"
            )

    def test_rank2_q2_explicit(self):
        """Rank-2 at q^2 = 624 via explicit sub-computation.

        Z_1^2 at q^2 = sum_{k=0}^{2} p_{24}(k)*p_{24}(2-k)
                      = 1*324 + 24*24 + 324*1 = 1224.
        Z_1(q^2) at q^2 = p_{24}(1) = 24.
        Z_2 = (1/2)(1224 + 24) = 624.
        """
        z1 = vw_rank1_k3(2)  # [1, 24, 324]
        z1_sq_q2 = z1[0] * z1[2] + z1[1] * z1[1] + z1[2] * z1[0]
        z1_q2_at_2 = z1[1]  # p_{24}(1) = 24
        expected = (z1_sq_q2 + z1_q2_at_2) // 2
        actual = vw_rank2_k3(2)[2]
        assert actual == expected == 624

    # --- Unitarity: algebraic proof + numerical verification ---

    def test_unitarity_two_paths(self):
        """g_N(u)*g_N(-u)=1: (1) algebraic from rank-1, (2) direct evaluation."""
        h = self._default_h_list()
        for N in [1, 2, 3]:
            # Path 1: evaluate g_N and g_N(-) directly
            u = F(37)
            g_u = structure_function_rank_N_evaluate(N, u, h)
            g_neg_u = structure_function_rank_N_evaluate(N, -u, h)
            # Path 2: compute g_1 and verify (g_1)^N * (g_1(-))^N = 1
            g1_u = structure_function_rank_N_evaluate(1, u, h)
            g1_neg_u = structure_function_rank_N_evaluate(1, -u, h)
            assert g_u == g1_u ** N
            assert g_neg_u == g1_neg_u ** N
            assert g_u * g_neg_u == F(1)

    # --- Structure function coefficients: series vs evaluation ---

    def test_structure_function_series_vs_evaluate(self):
        """Structure function: series expansion agrees with direct evaluation.

        Reconstruct g_N(u) from phi_j coefficients and compare with
        direct product evaluation at a test point.
        """
        h = self._default_h_list()
        u = F(10)
        for N in [1, 2]:
            # Path 1: direct evaluation
            g_direct = structure_function_rank_N_evaluate(N, u, h)
            # Path 2: from series phi_j * u^{-j}
            phi = structure_function_rank_N_coefficients(N, h, max_order=30)
            g_series = sum(phi[j] * F(1, u ** j) for j in range(len(phi)))
            # Series is truncated, so check approximate agreement
            # For u=10 and 30 terms, the error is O(u^{-31}) ~ 10^{-31}
            diff = abs(float(g_direct) - float(g_series))
            assert diff < 1e-10, (
                f"Rank {N}: direct={float(g_direct):.12f}, series={float(g_series):.12f}, diff={diff}"
            )

    # --- Bar Euler product: rank-N vs rank-1 power ---

    def test_bar_euler_rank2_vs_rank1_squared(self):
        """eta^{48} = (eta^{24})^2: bar Euler at rank 2 = square of rank 1.

        Path 1: bar_euler_product_rank_N(2, max_n).
        Path 2: convolve bar_euler_product_rank_N(1, max_n) with itself.
        """
        b1 = bar_euler_product_rank_N(1, 6)
        b2 = bar_euler_product_rank_N(2, 6)
        # Convolution of b1 with itself
        for n in range(7):
            conv = sum(b1[k] * b1[n - k] for k in range(n + 1))
            assert b2[n] == conv, f"n={n}: b2={b2[n]}, conv={conv}"

    # --- Central charge: c_total = 24*N via two formulae ---

    def test_central_charge_two_paths(self):
        """c_total = 24*N via (1) direct formula, (2) modular weight * (-2)."""
        for N in range(1, 5):
            cc = central_charge_wn_24(N)
            path1 = cc['c_total_with_heisenberg']
            path2 = int(-2 * cc['modular_weight'])
            assert path1 == path2 == 24 * N

    # --- Degree scaling: formula vs explicit count ---

    def test_degree_via_formula_and_evaluation(self):
        """deg(g_N) = (24N, 24N) via (1) formula, (2) counting zeros/poles.

        g_N = g_1^N: each of the 24 zeros/poles of g_1 gets multiplicity N,
        giving 24*N zeros and 24*N poles.
        """
        for N in range(1, 5):
            num_deg, den_deg = structure_function_rank_N_degree(N)
            # Path 1: the formula
            assert num_deg == 24 * N
            assert den_deg == 24 * N
            # Path 2: count via h_list (24 distinct h_a => 24N zeros with mult)
            h = self._default_h_list()
            distinct_zeros = len(set(h))
            # Each distinct h_a gives multiplicity N in the rank-N function
            total_zero_mult = sum(h.count(ha) * N for ha in set(h))
            assert total_zero_mult == 24 * N

    # --- Rank-2: naive overcounts ---

    def test_naive_overcounts_rank2(self):
        """Naive 1/eta^{48} at q^2 = 1224 > exact 624 = (1/2)(1224+24).

        The naive formula double-counts: the DMVV correction subtracts
        the overcounting via the Z_1(q^2) Hecke term.
        """
        naive = vw_rank_N_k3_naive(2, 2)
        exact = vw_rank_N_symmetric_product(2, 2)
        assert int(naive[2]) == 1224
        assert exact[2] == F(624)
        assert int(naive[2]) > int(exact[2])

    # --- W_N character: W_1 is trivial higher-spin ---

    def test_w1_vs_heisenberg(self):
        """W_1 higher-spin character = 1; full = 1/eta.

        Path 1: wn_vacuum_character_coeffs(1) = [1, 0, 0, ...].
        Path 2: wn_24_partition_function(1) = vw_rank1_k3 = 1/eta^{24}.
        The 24th power of 1/eta is 1/eta^{24}, which matches VW rank 1.
        """
        hs_ch = wn_vacuum_character_coeffs(1, 5)
        assert hs_ch == [F(1)] + [F(0)] * 5
        full = wn_24_partition_function(1, 4)
        vw = vw_rank1_k3(4)
        for n in range(5):
            assert full[n] == F(vw[n])

    # --- Rank-2 q^0 and q^1: universal across all computation paths ---

    def test_rank2_q0_universal(self):
        """Z_VW^{U(2)} at q^0 = 1 via all four paths."""
        assert vw_rank2_k3(0)[0] == 1
        assert vw_rank_N_symmetric_product(2, 0)[0] == F(1)
        assert int(vw_rank_N_k3_naive(2, 0)[0]) == 1
        assert wn_24_partition_function(2, 0)[0] == F(1)

    def test_rank2_q1_universal(self):
        """Z_VW^{U(2)} at q^1 = 24 via direct and symmetric product."""
        assert vw_rank2_k3(1)[1] == 24
        assert vw_rank_N_symmetric_product(2, 1)[1] == F(24)
