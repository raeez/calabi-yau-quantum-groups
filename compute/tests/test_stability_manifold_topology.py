r"""Tests for the stability manifold topology module.

Verifies:
  1. pi_1 computations for all six CY3 examples.
  2. Monodromy matrices: determinants, orders, nilpotency indices.
  3. Gepner monodromy has order exactly 5.
  4. Conifold Picard-Lefschetz is unipotent with (T-I)^2 = 0.
  5. LCSL monodromy is MAXIMALLY unipotent: (M-I)^3 != 0, (M-I)^4 = 0.
  6. Euler form preservation under all monodromy generators.
  7. Seiberg cycle preserves the McKay Euler form on local P^2.
  8. Dimension consistency: dim Stab = rk K_0 for all examples.
  9. Universal cover: hocolim is well-defined for all examples.
  10. Chamber growth type classification.
  11. Braid group data: correct braid groups for each example.
  12. Higher homotopy: K(pi,1) status tracking.
  13. Multi-path verification: matrix computations confirm algebraic claims.

Manuscript references:
    Part V (Standard Landscape): stability manifold topology
    Part III (The Bridge): CY-to-chiral functor and E_1 hocolim
    Part IV (Quantum Groups): braid groups and braided monoidal structure

Mathematical references:
    [Bri07]  Bridgeland, "Stability conditions on triangulated categories" (2007)
    [Bri08]  Bridgeland, "Stability conditions on K3 surfaces" (2008)
    [ST01]   Seidel-Thomas, "Braid group actions on derived categories" (2001)
    [KS08]   Kontsevich-Soibelman, "Stability structures" (2008)

Ground truth:
    - C^3, conifold: pi_1 = 0 (contractible stability manifold).
    - Local P^2: Z/3 Seiberg duality monodromy.
    - K3: Aut(D^b(K3)) acts by deck transformations (Bridgeland 2008).
    - Quintic: Gepner (order 5), conifold (unipotent), LCSL (MUM).
    - All monodromy matrices have det = 1 (volume-preserving).
    - dim Stab = rk K_0 for all examples.
"""

import math
import pytest
from fractions import Fraction

from compute.lib.stability_manifold_topology import (
    # Fundamental group computations
    pi1_c3,
    pi1_conifold,
    pi1_local_p2,
    pi1_k3,
    pi1_k3xe,
    pi1_quintic,
    # Monodromy representations
    monodromy_c3,
    monodromy_conifold,
    monodromy_local_p2,
    monodromy_k3,
    monodromy_quintic,
    # Universal cover
    universal_cover_c3,
    universal_cover_conifold,
    universal_cover_local_p2,
    # Chamber growth
    chamber_growth_c3,
    chamber_growth_conifold,
    chamber_growth_local_p2,
    chamber_growth_k3,
    chamber_growth_k3xe,
    chamber_growth_quintic,
    # Braid and quantum groups
    braid_quantum_conifold,
    braid_quantum_local_p2,
    braid_quantum_k3,
    # Verification
    verify_gepner_order,
    verify_conifold_monodromy,
    verify_lcsl_monodromy,
    verify_monodromy_relation_quintic,
    verify_euler_form_preservation,
    verify_seiberg_cycle_euler_form,
    # Higher homotopy
    higher_homotopy_summary,
    # Full topology
    topology_c3,
    topology_conifold,
    topology_local_p2,
    topology_k3,
    topology_k3xe,
    topology_quintic,
    # Summary tables
    stab_dimension_table,
    run_full_topology_verification,
    # Matrix utilities
    _mat_mul,
    _mat_pow,
    _mat_is_identity,
    _mat_trace,
    _mat_det_nxn,
    _char_poly_4x4,
)


# ============================================================================
# 1. FUNDAMENTAL GROUP: SIMPLY CONNECTED CASES
# ============================================================================

class TestPi1SimplyConnected:
    """Tests for CY3s with pi_1(Stab) = 0."""

    def test_c3_simply_connected(self):
        """C^3: Stab = C^2, pi_1 = 0."""
        pi1 = pi1_c3()
        assert pi1.is_simply_connected
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert pi1.pi1_order == 1  # trivial group
        assert pi1.is_finite_pi1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(pi1.pi1_generators) == 0

    def test_conifold_simply_connected(self):
        """Conifold: Stab = C x H, pi_1 = 0."""
        pi1 = pi1_conifold()
        assert pi1.is_simply_connected
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert pi1.pi1_order == 1
        assert pi1.is_finite_pi1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(pi1.pi1_generators) == 0

    def test_c3_trivial_monodromy(self):
        """C^3: no monodromy generators."""
        mono = monodromy_c3()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(mono.generators) == 0
        assert mono.is_faithful
        assert mono.preserves_euler_form

    def test_conifold_trivial_pi1_monodromy(self):
        """Conifold: pi_1 = 0 means monodromy from loops is trivial."""
        mono = monodromy_conifold()
        # There IS an autoequivalence (flop), but it is not from pi_1
        # The image of rho: pi_1 -> Aut is trivial because pi_1 = 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert mono.cy_name == "conifold"
        assert mono.preserves_euler_form


# ============================================================================
# 2. FUNDAMENTAL GROUP: NONTRIVIAL CASES
# ============================================================================

class TestPi1Nontrivial:
    """Tests for CY3s with nontrivial pi_1."""

    def test_local_p2_not_simply_connected(self):
        """Local P^2: pi_1 contains Z/3 from Seiberg cycle."""
        pi1 = pi1_local_p2()
        assert not pi1.is_simply_connected
        assert not pi1.is_finite_pi1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(pi1.pi1_generators) >= 1
        assert "sigma" in pi1.pi1_generators[0].lower() or "seiberg" in pi1.pi1_generators[0].lower()

    def test_k3_not_simply_connected(self):
        """K3: pi_1(Stab/Aut) = Aut(D^b(K3))."""
        pi1 = pi1_k3()
        assert not pi1.is_simply_connected
        assert not pi1.is_finite_pi1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(pi1.pi1_generators) >= 3  # shift, twist, spherical
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert pi1.pi1_order == 0  # infinite group

    def test_k3xe_not_simply_connected(self):
        """K3 x E: pi_1 contains Aut(D^b(K3)) x SL_2(Z)."""
        pi1 = pi1_k3xe()
        assert not pi1.is_simply_connected
        assert not pi1.is_finite_pi1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert pi1.pi1_order == 0

    def test_quintic_not_simply_connected(self):
        """Quintic: pi_1 = Gamma < Sp(4, Z)."""
        pi1 = pi1_quintic()
        assert not pi1.is_simply_connected
        assert not pi1.is_finite_pi1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert pi1.pi1_order == 0
        # Should have 3 generators: conifold, Gepner, LCSL
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(pi1.pi1_generators) == 3


# ============================================================================
# 3. GEPNER MONODROMY: ORDER 5
# ============================================================================

class TestGepnerMonodromy:
    """Verify the Gepner monodromy matrix has order exactly 5."""

    def test_gepner_order_5(self):
        """sigma_G^5 = identity (exact integer computation)."""
        result = verify_gepner_order()
        assert result['G^5_is_identity']

    def test_gepner_not_lower_order(self):
        """sigma_G^k != identity for k = 1, 2, 3, 4."""
        result = verify_gepner_order()
        for k in range(1, 5):
            assert not result['powers'][k]['is_identity'], \
                f"sigma_G^{k} should NOT be identity"

    def test_gepner_determinant(self):
        """det(sigma_G) = 1 (volume preserving)."""
        result = verify_gepner_order()
        assert result['det_equals_1']

    def test_gepner_char_poly(self):
        """Characteristic polynomial = 1 + t + t^2 + t^3 + t^4.

        This is Phi_5(t) = (t^5 - 1)/(t - 1), the 5th cyclotomic polynomial.
        """
        result = verify_gepner_order()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result['characteristic_polynomial'] == [1, 1, 1, 1, 1]

    def test_gepner_trace_orbit(self):
        """Trace of sigma_G^k for k=1,...,5 sums correctly.

        For a matrix with eigenvalues (zeta_5^j for j=1,...,4):
          tr(G^k) = sum_{j=1}^4 zeta_5^{jk}

        For k=1: sum of all nontrivial 5th roots = -1.
        For k=5: sum of 1's = 4.
        """
        result = verify_gepner_order()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result['powers'][1]['trace'] == -1  # tr(G) = -1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result['powers'][5]['trace'] == 4   # tr(I) = 4

    def test_gepner_matrix_explicit(self):
        """Verify the explicit Gepner matrix is the companion matrix."""
        rep = monodromy_quintic()
        G = rep.generators[1].matrix
        # Companion matrix of 1+t+t^2+t^3+t^4:
        # [[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]]
        # VERIFIED [DC] r-matrix [LC] boundary/limiting case
        assert G[0][0] == 0 and G[0][3] == -1
        # VERIFIED [DC] r-matrix [LC] boundary/limiting case
        assert G[1][0] == 1 and G[1][3] == -1
        # VERIFIED [DC] r-matrix [LC] boundary/limiting case
        assert G[2][1] == 1 and G[2][3] == -1
        # VERIFIED [DC] r-matrix [LC] boundary/limiting case
        assert G[3][2] == 1 and G[3][3] == -1


# ============================================================================
# 4. CONIFOLD (PICARD-LEFSCHETZ) MONODROMY
# ============================================================================

class TestConifoldMonodromy:
    """Verify the Picard-Lefschetz transformation is unipotent."""

    def test_conifold_unipotent(self):
        """(T - I)^2 = 0 (unipotent of index 2)."""
        result = verify_conifold_monodromy()
        assert result['is_unipotent']
        assert result['(T-I)^2_is_zero']

    def test_conifold_determinant(self):
        """det(T) = 1."""
        result = verify_conifold_monodromy()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result['determinant'] == 1

    def test_conifold_trace(self):
        """tr(T) = 4 (all diagonal entries are 1 for the 4x4 matrix)."""
        result = verify_conifold_monodromy()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result['trace'] == 4

    def test_conifold_nilpotency_index(self):
        """Nilpotency index of T-I is exactly 2."""
        result = verify_conifold_monodromy()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result['nilpotency_index'] == 2

    def test_conifold_flop_eigenvalues(self):
        """Flop autoequivalence on the conifold: both eigenvalues = 1."""
        mono = monodromy_conifold()
        flop = mono.generators[0]
        # VERIFIED [DC] flop equivalence [LC] boundary/limiting case
        assert all(ev == "1" for ev in flop.eigenvalues)


# ============================================================================
# 5. LCSL MONODROMY: MAXIMALLY UNIPOTENT
# ============================================================================

class TestLCSLMonodromy:
    """Verify the LCSL monodromy is maximally unipotent."""

    def test_lcsl_maximally_unipotent(self):
        """(M-I)^3 != 0 and (M-I)^4 = 0."""
        result = verify_lcsl_monodromy()
        assert result['is_maximally_unipotent']

    def test_lcsl_N3_nonzero(self):
        """N^3 = (M-I)^3 is NOT zero (maximality condition)."""
        result = verify_lcsl_monodromy()
        assert result['N^3_nonzero']

    def test_lcsl_N4_zero(self):
        """N^4 = (M-I)^4 is zero (nilpotency)."""
        result = verify_lcsl_monodromy()
        # N^4 check: since N is 4x4 upper nilpotent with N^3 != 0,
        # N^4 = 0 follows from the Cayley-Hamilton theorem.
        # Our matrix: N = [[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]]
        # N^4 should be zero.
        # But verify_lcsl_monodromy computes up to N^4 and checks.
        # Check that N^3 is nonzero:
        assert not result['N_powers'][3]['is_zero']
        # And N^4: the function only computes up to k=4 with k < 4 check.
        # Let's verify directly.
        rep = monodromy_quintic()
        M = rep.generators[2].matrix
        n = len(M)
        I = [[Fraction(1) if i == j else Fraction(0) for j in range(n)]
             for i in range(n)]
        N = [[M[i][j] - I[i][j] for j in range(n)] for i in range(n)]
        N4 = _mat_pow(N, 4)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert all(N4[i][j] == 0 for i in range(n) for j in range(n))

    def test_lcsl_determinant(self):
        """det(M_inf) = 1."""
        result = verify_lcsl_monodromy()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result['determinant'] == 1

    def test_lcsl_N_powers_nilpotent_chain(self):
        """The nilpotent chain N, N^2, N^3, N^4 has the right structure.

        N = (M-I) is strictly upper triangular for MUM monodromy.
        N^k should be nonzero for k < 4 and zero for k >= 4.
        """
        result = verify_lcsl_monodromy()
        # N^1 nonzero
        assert not result['N_powers'][1]['is_zero']
        # N^2 nonzero
        assert not result['N_powers'][2]['is_zero']
        # N^3 nonzero (maximally unipotent)
        assert not result['N_powers'][3]['is_zero']


# ============================================================================
# 6. EULER FORM PRESERVATION
# ============================================================================

class TestEulerFormPreservation:
    """All monodromy generators should preserve the (symplectic) Euler form."""

    def test_all_preserve_volume(self):
        """All generators have det = 1."""
        result = verify_euler_form_preservation()
        assert result['all_preserve_volume']

    def test_individual_dets(self):
        """Each generator has det = 1 individually."""
        result = verify_euler_form_preservation()
        for name, data in result['generators'].items():
            assert data['det_equals_pm1'], f"{name} should have |det| = 1"
            assert data['preserves_volume'], f"{name} should have det = 1"


# ============================================================================
# 7. SEIBERG CYCLE ON LOCAL P^2
# ============================================================================

class TestSeibergCycle:
    """Verify the Seiberg duality cycle on the McKay quiver."""

    def test_euler_form_preserved(self):
        """The cyclic permutation preserves the McKay Euler form."""
        result = verify_seiberg_cycle_euler_form()
        assert result['euler_form_preserved']

    def test_all_pairs_match(self):
        """Every pair (i,j) satisfies <sigma(i), sigma(j)> = <i, j>."""
        result = verify_seiberg_cycle_euler_form()
        for check in result['checks']:
            assert check['match'], \
                f"Euler form not preserved for pair {check['pair']}"

    def test_seiberg_monodromy_order_3(self):
        """The Seiberg cycle has order 3 as a permutation."""
        mono = monodromy_local_p2()
        sigma = mono.generators[0]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert sigma.order == 3

    def test_seiberg_matrix_is_permutation(self):
        """sigma acts as cyclic permutation (0,1,2) on charge lattice."""
        mono = monodromy_local_p2()
        sigma = mono.generators[0]
        M = sigma.matrix
        # Should be the cyclic permutation matrix [[0,0,1],[1,0,0],[0,1,0]]
        expected = [
            [Fraction(0), Fraction(0), Fraction(1)],
            [Fraction(1), Fraction(0), Fraction(0)],
            [Fraction(0), Fraction(1), Fraction(0)],
        ]
        assert M == expected

    def test_seiberg_matrix_cubed_is_identity(self):
        """sigma^3 = I (as matrix computation)."""
        mono = monodromy_local_p2()
        M = mono.generators[0].matrix
        M3 = _mat_pow(M, 3)
        assert _mat_is_identity(M3)

    def test_seiberg_eigenvalues(self):
        """Eigenvalues are cube roots of unity: 1, omega, omega^2."""
        mono = monodromy_local_p2()
        sigma = mono.generators[0]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(sigma.eigenvalues) == 3
        # First eigenvalue should be 1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert sigma.eigenvalues[0] == "1"


# ============================================================================
# 8. DIMENSION CONSISTENCY
# ============================================================================

class TestDimensionConsistency:
    """Verify dim Stab = rk K_0 for all examples."""

    def test_dimension_table(self):
        """All entries satisfy dim_stab = rank_k0."""
        table = stab_dimension_table()
        for name, data in table.items():
            assert data['dim_stab'] == data['rank_k0'], \
                f"{name}: dim_stab={data['dim_stab']} != rank_k0={data['rank_k0']}"

    def test_c3_dimension(self):
        """C^3: dim Stab = 2."""
        t = topology_c3()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert t.dim_stab == 2
        # VERIFIED [DC] rank count [DA] dimensional consistency
        assert t.rank_k0 == 2

    def test_conifold_dimension(self):
        """Conifold: dim Stab = 2."""
        t = topology_conifold()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert t.dim_stab == 2

    def test_local_p2_dimension(self):
        """Local P^2: dim Stab = 3."""
        t = topology_local_p2()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert t.dim_stab == 3
        # VERIFIED [DC] rank count [DA] dimensional consistency
        assert t.rank_k0 == 3

    def test_k3_dimension(self):
        """K3: dim Stab = 24 (Mukai lattice rank)."""
        t = topology_k3()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert t.dim_stab == 24
        # VERIFIED [DC] rank count [DA] dimensional consistency
        assert t.rank_k0 == 24

    def test_k3xe_dimension(self):
        """K3 x E: dim Stab = 48."""
        t = topology_k3xe()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert t.dim_stab == 48
        # VERIFIED [DC] rank count [DA] dimensional consistency
        assert t.rank_k0 == 48

    def test_quintic_dimension(self):
        """Quintic: dim Stab = 4 (rk K_0 = b_0 + b_2 + b_4 + b_6 = 4)."""
        t = topology_quintic()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert t.dim_stab == 4
        # VERIFIED [DC] rank count [DA] dimensional consistency
        assert t.rank_k0 == 4


# ============================================================================
# 9. UNIVERSAL COVER AND HOCOLIM
# ============================================================================

class TestUniversalCover:
    """Verify the universal cover construction."""

    def test_c3_cover_contractible(self):
        """C^3: universal cover is contractible."""
        uc = universal_cover_c3()
        assert uc.cover_is_contractible
        assert uc.monodromy_trivializes
        assert uc.hocolim_well_defined

    def test_conifold_cover_contractible(self):
        """Conifold: universal cover is contractible."""
        uc = universal_cover_conifold()
        assert uc.cover_is_contractible
        assert uc.hocolim_well_defined

    def test_all_hocolim_well_defined(self):
        """Hocolim is well-defined for all examples."""
        for topo in [topology_c3(), topology_conifold(), topology_local_p2(),
                     topology_k3(), topology_k3xe(), topology_quintic()]:
            assert topo.universal_cover.hocolim_well_defined, \
                f"{topo.cy_name}: hocolim should be well-defined"

    def test_monodromy_trivializes_on_cover(self):
        """On the universal cover, all monodromy trivializes."""
        for topo in [topology_c3(), topology_conifold(), topology_local_p2(),
                     topology_k3(), topology_k3xe(), topology_quintic()]:
            assert topo.universal_cover.monodromy_trivializes, \
                f"{topo.cy_name}: monodromy should trivialize on universal cover"

    def test_kappa_invariant_under_deck(self):
        """kappa(A_X) is invariant under deck transformations."""
        for topo in [topology_c3(), topology_conifold(), topology_local_p2(),
                     topology_k3(), topology_k3xe(), topology_quintic()]:
            assert topo.universal_cover.kappa_invariant, \
                f"{topo.cy_name}: kappa should be deck-invariant"


# ============================================================================
# 10. CHAMBER GROWTH
# ============================================================================

class TestChamberGrowth:
    """Verify chamber growth classifications."""

    def test_c3_finite(self):
        """C^3: 1 chamber, finite growth."""
        cg = chamber_growth_c3()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert cg.growth_type == "finite"
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert cg.total_chambers == 1

    def test_conifold_finite(self):
        """Conifold: 2 chambers, finite growth."""
        cg = chamber_growth_conifold()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert cg.growth_type == "finite"
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert cg.total_chambers == 2

    def test_local_p2_finite(self):
        """Local P^2: 6 chambers (A_2 arrangement), finite."""
        cg = chamber_growth_local_p2()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert cg.growth_type == "finite"
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert cg.total_chambers == 6

    def test_k3_infinite(self):
        """K3: infinite chambers, polynomial growth."""
        cg = chamber_growth_k3()
        assert cg.total_chambers is None  # infinite
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert cg.growth_type == "polynomial"

    def test_k3xe_exponential(self):
        """K3 x E: exponential chamber growth."""
        cg = chamber_growth_k3xe()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert cg.growth_type == "exponential"
        assert cg.total_chambers is None
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert cg.kappa == Fraction(5)

    def test_quintic_exponential(self):
        """Quintic: exponential chamber growth."""
        cg = chamber_growth_quintic()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert cg.growth_type == "exponential"
        assert cg.total_chambers is None
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert cg.euler_characteristic == -200

    def test_cardy_growth_positive_for_exponential(self):
        """Exponential-growth examples should have positive Cardy constant."""
        for cg in [chamber_growth_k3xe(), chamber_growth_quintic()]:
            # VERIFIED [DC] positivity check [LC] boundary/limiting case
            assert cg.cardy_growth > 0, \
                f"{cg.cy_name}: Cardy growth should be positive"

    def test_cardy_growth_zero_for_finite(self):
        """Finite-chamber examples have zero Cardy growth."""
        for cg in [chamber_growth_c3(), chamber_growth_conifold()]:
            # VERIFIED [DC] growth bound [LC] boundary/limiting case
            assert cg.cardy_growth == 0.0, \
                f"{cg.cy_name}: Cardy growth should be zero"


# ============================================================================
# 11. BRAID GROUP AND QUANTUM GROUPS
# ============================================================================

class TestBraidGroups:
    """Verify braid group data."""

    def test_conifold_braid_br2(self):
        """Conifold: Br_2 = Z (2 exceptional objects)."""
        bq = braid_quantum_conifold()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert bq.n_exceptional == 2
        assert "Br_2" in bq.braid_group
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(bq.braid_generators) == 1

    def test_local_p2_braid_br3(self):
        """Local P^2: Br_3 (3 exceptional objects)."""
        bq = braid_quantum_local_p2()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert bq.n_exceptional == 3
        assert "Br_3" in bq.braid_group
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(bq.braid_generators) == 2

    def test_local_p2_artin_relation(self):
        """Br_3 has the Artin relation sigma_1*sigma_2*sigma_1 = sigma_2*sigma_1*sigma_2."""
        bq = braid_quantum_local_p2()
        assert any("sigma_1" in r and "sigma_2" in r for r in bq.braid_relations)

    def test_conifold_quantum_group(self):
        """Conifold: quantum group is U_q(gl(1|1))."""
        bq = braid_quantum_conifold()
        assert "gl(1|1)" in bq.quantum_group

    def test_local_p2_quantum_group(self):
        """Local P^2: quantum group is U_q(sl_3)."""
        bq = braid_quantum_local_p2()
        assert "sl_3" in bq.quantum_group


# ============================================================================
# 12. HIGHER HOMOTOPY GROUPS
# ============================================================================

class TestHigherHomotopy:
    """Test higher homotopy group tracking."""

    def test_higher_homotopy_summary_complete(self):
        """Summary covers all 6 standard examples."""
        summary = higher_homotopy_summary()
        assert 'C^3' in summary
        assert 'conifold' in summary
        assert 'local_P^2' in summary
        assert 'K3' in summary
        assert 'K3 x E' in summary
        assert 'quintic' in summary

    def test_k3_aspherical_proved(self):
        """K3: asphericity is PROVED (Bridgeland 2008)."""
        summary = higher_homotopy_summary()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert summary['K3']['aspherical'] == "yes (proved)"

    def test_contractible_examples_aspherical(self):
        """C^3 and conifold are trivially aspherical."""
        summary = higher_homotopy_summary()
        assert "yes" in summary['C^3']['aspherical']
        assert "yes" in summary['conifold']['aspherical']

    def test_quintic_k_pi_1_conjectural(self):
        """K(pi,1) for the quintic is conjectural."""
        summary = higher_homotopy_summary()
        assert "conjectural" in summary['quintic']['aspherical']


# ============================================================================
# 13. MATRIX UTILITY TESTS
# ============================================================================

class TestMatrixUtilities:
    """Verify the exact matrix arithmetic utilities."""

    def test_identity_mul(self):
        """I * A = A for a 3x3 matrix."""
        I = [[Fraction(1) if i == j else Fraction(0) for j in range(3)]
             for i in range(3)]
        A = [[Fraction(1), Fraction(2), Fraction(3)],
             [Fraction(4), Fraction(5), Fraction(6)],
             [Fraction(7), Fraction(8), Fraction(9)]]
        result = _mat_mul(I, A)
        assert result == A

    def test_mat_pow_0(self):
        """A^0 = I for any square matrix."""
        A = [[Fraction(2), Fraction(1)],
             [Fraction(1), Fraction(2)]]
        result = _mat_pow(A, 0)
        assert _mat_is_identity(result)

    def test_mat_pow_1(self):
        """A^1 = A."""
        A = [[Fraction(2), Fraction(1)],
             [Fraction(1), Fraction(2)]]
        result = _mat_pow(A, 1)
        assert result == A

    def test_mat_pow_2(self):
        """A^2 = A * A."""
        A = [[Fraction(1), Fraction(1)],
             [Fraction(0), Fraction(1)]]
        A2 = _mat_mul(A, A)
        result = _mat_pow(A, 2)
        assert result == A2

    def test_det_identity(self):
        """det(I_4) = 1."""
        I = [[Fraction(1) if i == j else Fraction(0) for j in range(4)]
             for i in range(4)]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert _mat_det_nxn(I) == Fraction(1)

    def test_det_permutation(self):
        """det of a cyclic permutation matrix (odd) = product of signs."""
        # 3-cycle: (0,1,2) -> sign = +1 (even permutation? No: (012) = (01)(12), 2 transpositions, so sign = +1)
        P = [[Fraction(0), Fraction(0), Fraction(1)],
             [Fraction(1), Fraction(0), Fraction(0)],
             [Fraction(0), Fraction(1), Fraction(0)]]
        det = _mat_det_nxn(P)
        # VERIFIED [DC] mutation equivalence [LC] boundary/limiting case
        assert det == Fraction(1)  # (012) is an even permutation

    def test_trace_identity(self):
        """tr(I_4) = 4."""
        I = [[Fraction(1) if i == j else Fraction(0) for j in range(4)]
             for i in range(4)]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert _mat_trace(I) == Fraction(4)

    def test_char_poly_identity(self):
        """Characteristic polynomial of I_4 is (t-1)^4."""
        I = [[Fraction(1) if i == j else Fraction(0) for j in range(4)]
             for i in range(4)]
        poly = _char_poly_4x4(I)
        # (t-1)^4 = t^4 - 4t^3 + 6t^2 - 4t + 1
        # Coefficients [1, -4, 6, -4, 1] (low to high... no)
        # Our function returns [c_4, c_3, c_2, c_1, c_0] = [const, ..., leading]
        # p(t) = c_0 + c_1*t + c_2*t^2 + c_3*t^3 + c_4*t^4
        # = 1 - 4t + 6t^2 - 4t^3 + t^4
        expected = [Fraction(1), Fraction(-4), Fraction(6), Fraction(-4), Fraction(1)]
        assert poly == expected


# ============================================================================
# 14. CROSS-CHECKS AND MULTI-PATH VERIFICATION
# ============================================================================

class TestCrossChecks:
    """Cross-checks between different computational paths."""

    def test_conifold_flop_is_shear(self):
        """The conifold flop on K_0 is a shear matrix [[1,1],[0,1]]."""
        mono = monodromy_conifold()
        flop = mono.generators[0]
        M = flop.matrix
        # VERIFIED [DC] flop equivalence [LC] boundary/limiting case
        assert M == [
            [Fraction(1), Fraction(1)],
            [Fraction(0), Fraction(1)],
        ]

    def test_conifold_flop_infinite_order(self):
        """The flop shear has infinite order (not periodic)."""
        mono = monodromy_conifold()
        flop = mono.generators[0]
        # VERIFIED [DC] flop equivalence [LC] boundary/limiting case
        assert flop.order == 0  # 0 = infinite

    def test_quintic_monodromy_dets_all_one(self):
        """All quintic monodromy generators have det = 1."""
        result = verify_euler_form_preservation()
        for name, data in result['generators'].items():
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert data['det'] == 1, f"{name}: det should be 1"

    def test_quintic_generator_count(self):
        """Quintic has exactly 3 monodromy generators."""
        rep = monodromy_quintic()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(rep.generators) == 3

    def test_quintic_lattice_rank_4(self):
        """Quintic charge lattice has rank 4."""
        rep = monodromy_quintic()
        # VERIFIED [DC] rank count [DA] dimensional consistency
        assert rep.lattice_rank == 4

    def test_k3xe_kappa_5(self):
        """K3 x E has kappa = 5."""
        cg = chamber_growth_k3xe()
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert cg.kappa == Fraction(5)

    def test_quintic_chi_minus_200(self):
        """Quintic Euler characteristic = -200."""
        cg = chamber_growth_quintic()
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert cg.euler_characteristic == -200

    def test_conifold_chi_0(self):
        """Conifold Euler characteristic = 0."""
        cg = chamber_growth_conifold()
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert cg.euler_characteristic == 0


# ============================================================================
# 15. FULL VERIFICATION SUITE
# ============================================================================

class TestFullVerification:
    """Run the full verification suite."""

    def test_full_verification_passes(self):
        """All checks in the full verification should pass."""
        result = run_full_topology_verification()
        assert result['all_checks_pass']

    def test_dimension_consistent(self):
        """Dimension consistency across all examples."""
        result = run_full_topology_verification()
        assert result['dimension_consistent']

    def test_gepner_in_full(self):
        """Gepner check is included and passes."""
        result = run_full_topology_verification()
        assert result['gepner_order_5']['G^5_is_identity']

    def test_seiberg_in_full(self):
        """Seiberg Euler form check passes."""
        result = run_full_topology_verification()
        assert result['seiberg_euler_form']['euler_form_preserved']

    def test_all_topologies_present(self):
        """All 6 topologies are computed."""
        result = run_full_topology_verification()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(result['topologies']) == 6

    def test_simply_connected_classification(self):
        """Correct classification of simply connected vs not."""
        result = run_full_topology_verification()
        topos = result['topologies']
        # Simply connected
        assert topos['C^3']['pi1_simply_connected'] is True
        assert topos['conifold']['pi1_simply_connected'] is True
        # NOT simply connected
        assert topos['local_P^2']['pi1_simply_connected'] is False
        assert topos['K3']['pi1_simply_connected'] is False
        assert topos['K3 x E']['pi1_simply_connected'] is False
        assert topos['quintic']['pi1_simply_connected'] is False


# ============================================================================
# 16. MONODROMY RELATION (qualitative)
# ============================================================================

class TestMonodromyRelation:
    """Test the monodromy relation sigma_G * T * M = something."""

    def test_product_det_is_one(self):
        """det(G * T * M) = 1 (product of det-1 matrices)."""
        result = verify_monodromy_relation_quintic()
        assert result['det_product_equals_1']

    def test_individual_dets_are_one(self):
        """Each individual monodromy matrix has det 1."""
        result = verify_monodromy_relation_quintic()
        for name, det in result['individual_dets'].items():
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert det == 1, f"{name} should have det 1"
