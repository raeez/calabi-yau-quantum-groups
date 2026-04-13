r"""Tests for the gl(1|1) factored transfer matrix T(u) = (u-phi_1)(u-phi_2).

Verifies:
  1. Monodromy matrix construction: T_a(u) = R_{a,1}(u-phi_1) R_{a,2}(u-phi_2)
  2. Factored transfer matrix: t(u) = str_a(T_a(u)) on V_1 x V_2
  3. Transfer matrix commutativity: [t(u), t(v)] = 0 (integrability)
  4. Bialgebra axiom H3 at charge (1,0) x (0,1) via RTT route
  5. Coassociativity at charge (1,0) x (0,1) via triple product
  6. Supertrace structure: str(t(u)) = 0 (super-cancellation)
  7. Spectral parameter independence of commutativity
  8. Inhomogeneity independence of structure

MATHEMATICAL CONTENT:

The gl(1|1) transfer matrix for the conifold two-site spin chain
is constructed from the Yang R-matrix R(u) = u*Id + P_graded:

  T_a(u) = R_{a,1}(u - phi_1) * R_{a,2}(u - phi_2)

where phi_1 (bosonic, charge (1,0)) and phi_2 (fermionic, charge (0,1))
are the inhomogeneity parameters corresponding to the two BPS states.

The transfer matrix t(u) = str_a(T_a(u)) acts on V_1 tensor V_2 = C^{1|1} x C^{1|1}.

Bialgebra axiom H3:
  The factored form T = R_{a1} R_{a2} encodes H3 via the interchange law
  in the graded tensor product. The RTT coproduct Delta(T) = T dot-tensor T
  is an algebra homomorphism precisely because the monodromy matrix factorizes.

Coassociativity:
  [t(u), t(v)] = 0 for all u, v is equivalent to coassociativity via the
  RTT formalism (Faddeev-Reshetikhin-Takhtajan). The triple product
  str_a(R1 R2 R3) is invariant under reordering of spectral parameters.

Multi-path verification:
    Path 1:  Transfer matrix structure (4 tests)
    Path 2:  Transfer commutativity at 5 parameter pairs (5 tests)
    Path 3:  H3 via RTT at 3 spectral parameters (3 tests)
    Path 4:  Coassociativity via triple product (2 tests)
    Path 5:  Supertrace vanishing (3 tests)
    Path 6:  Inhomogeneity variation (3 tests)
    Path 7:  Full verification integration (1 test)
    Path 8:  Cross-checks between algebraic and RTT routes (5 tests)

Manuscript references:
    Vol III, Part III: CY landscape, conifold functor chain
    Vol III, Part IV: R-matrix from Drinfeld center
    Vol I, Part I: bar complex, bialgebra structure

Mathematical references:
    [FRT]   Faddeev-Reshetikhin-Takhtajan, Leningrad Math J 1 (1990) 193-225
    [KS]    Kontsevich-Soibelman, arXiv:0811.2435
    [CR]    Creutzig-Ridout, arXiv:1207.6104 (gl(1|1) VOA)
    [BGM]   Bershtein-Gavrylenko-Marshakov, arXiv:1405.7040 (Yangian of gl(1|1))
"""

import pytest
from fractions import Fraction

from compute.lib.conifold_e1_full_chain import (
    GL11FactoredTransferMatrix,
    GL11TransferMatrix,
    ConifoldE1Bialgebra,
    YangianGL11,
    conifold_e1_bialgebra_verification,
)


# ================================================================
# 1. TRANSFER MATRIX STRUCTURE
# ================================================================

class TestTransferMatrixStructure:
    """Verify structural properties of the factored transfer matrix."""

    def test_transfer_is_4x4(self):
        """t(u) is a 4x4 matrix on V_1 x V_2 = C^{1|1} x C^{1|1}."""
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        t = ftm.transfer_matrix_factored(Fraction(2))
        # VERIFIED [DC] dimension check [LT] transfer matrix construction
        assert len(t) == 4
        assert all(len(row) == 4 for row in t)

    def test_monodromy_is_8x8(self):
        """T_a(u) is 8x8 on V_a x V_1 x V_2."""
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        T = ftm.monodromy_matrix(Fraction(2))
        # VERIFIED [DC] dimension check [LT] monodromy construction
        assert len(T) == 8
        assert all(len(row) == 8 for row in T)

    def test_transfer_diagonal_dominates(self):
        """The diagonal entries of t(u) are nonzero for generic u."""
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        t = ftm.transfer_matrix_factored(Fraction(3))
        # VERIFIED [DC] diagonal structure [LT] R-matrix regularity
        for i in range(4):
            assert t[i][i] != Fraction(0), f"Diagonal entry t[{i}][{i}] is zero"

    def test_transfer_exact_at_u2(self):
        """Verify exact entries of t(u=2) with phi_1=0, phi_2=1.

        R(u-0) = R(2) = 2*Id + P, R(u-1) = R(1) = Id + P.
        The transfer matrix is computed by taking str_a of the product
        of the embedded R-matrices. We verify the diagonal entries.
        """
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        t = ftm.transfer_matrix_factored(Fraction(2))
        # VERIFIED [DC] exact computation [LT] R-matrix product
        # t[0][0] = 4 (the (|00>,|00>) entry: both sites bosonic)
        assert t[0][0] == Fraction(4)
        # t[3][3] = 2 (the (|11>,|11>) entry: both sites fermionic)
        assert t[3][3] == Fraction(2)


# ================================================================
# 2. TRANSFER MATRIX COMMUTATIVITY
# ================================================================

class TestTransferCommutativity:
    """Verify [t(u), t(v)] = 0 for the factored transfer matrix.

    This is the fundamental integrability condition, equivalent to
    coassociativity through the RTT formalism.
    """

    def test_commute_u1_v2(self):
        """[t(1), t(2)] = 0."""
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        # VERIFIED [DC] integrability [LT] YBE consequence
        assert ftm.transfer_commute_check(Fraction(1), Fraction(2)) is True

    def test_commute_u3_v5(self):
        """[t(3), t(5)] = 0."""
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        # VERIFIED [DC] integrability [LT] YBE consequence
        assert ftm.transfer_commute_check(Fraction(3), Fraction(5)) is True

    def test_commute_u1_v_half(self):
        """[t(1), t(1/2)] = 0."""
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        # VERIFIED [DC] integrability [LT] YBE consequence
        assert ftm.transfer_commute_check(Fraction(1), Fraction(1, 2)) is True

    def test_commute_u7_v3(self):
        """[t(7), t(3)] = 0."""
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        # VERIFIED [DC] integrability [LT] YBE consequence
        assert ftm.transfer_commute_check(Fraction(7), Fraction(3)) is True

    def test_commute_near_singularity(self):
        """[t(phi_1+epsilon), t(phi_2+epsilon)] = 0 near the poles."""
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        # Near phi_1=0 and phi_2=1: use u = 1/10 and v = 11/10
        # VERIFIED [DC] integrability near poles [LT] YBE consequence
        assert ftm.transfer_commute_check(Fraction(1, 10), Fraction(11, 10)) is True


# ================================================================
# 3. BIALGEBRA AXIOM H3 VIA RTT
# ================================================================

class TestH3ViaRTT:
    """Verify bialgebra axiom H3 at charge (1,0) x (0,1) via the
    factored transfer matrix route.

    H3: Delta(a*b) = Delta(a) * Delta(b).

    In the RTT formalism, this is encoded by the factored form
    T = R_{a1} R_{a2}, which ensures the coproduct Delta(T) = T x T
    is an algebra homomorphism via the interchange law.
    """

    def test_h3_at_u1(self):
        """H3 holds at spectral parameter u = 1."""
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        result = ftm.verify_H3_via_transfer(Fraction(1))
        # VERIFIED [DC] bialgebra axiom [LT] RTT factorisation
        assert result["H3_holds"] is True

    def test_h3_at_u2(self):
        """H3 holds at spectral parameter u = 2."""
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        result = ftm.verify_H3_via_transfer(Fraction(2))
        # VERIFIED [DC] bialgebra axiom [LT] RTT factorisation
        assert result["H3_holds"] is True

    def test_h3_at_u_third(self):
        """H3 holds at spectral parameter u = 1/3."""
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        result = ftm.verify_H3_via_transfer(Fraction(1, 3))
        # VERIFIED [DC] bialgebra axiom [LT] RTT factorisation
        assert result["H3_holds"] is True


# ================================================================
# 4. COASSOCIATIVITY VIA TRIPLE PRODUCT
# ================================================================

class TestCoassociativityTriple:
    """Verify coassociativity at charge (1,0) x (0,1) via the triple
    transfer matrix product.

    Coassociativity: (Delta x id) o Delta = (id x Delta) o Delta.

    Verified through:
    (a) Pairwise commutativity [t(u), t(v)] = 0 at three pairs
    (b) Triple supertrace invariance under permutation of (u,v,w)
    """

    def test_coassoc_triple_123(self):
        """Coassociativity at (u,v,w) = (1,2,3)."""
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        result = ftm.verify_coassociativity_transfer(
            Fraction(1), Fraction(2), Fraction(3)
        )
        # VERIFIED [DC] coassociativity [LT] RTT triple product
        assert result["coassociative"] is True
        assert result["pairwise_commute_uv"] is True
        assert result["pairwise_commute_vw"] is True
        assert result["pairwise_commute_uw"] is True
        assert result["triple_invariant"] is True

    def test_coassoc_triple_half_steps(self):
        """Coassociativity at (u,v,w) = (1/2, 3/2, 5/2)."""
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        result = ftm.verify_coassociativity_transfer(
            Fraction(1, 2), Fraction(3, 2), Fraction(5, 2)
        )
        # VERIFIED [DC] coassociativity [LT] RTT triple product
        assert result["coassociative"] is True


# ================================================================
# 5. SUPERTRACE VANISHING
# ================================================================

class TestSupertraceVanishing:
    """Verify str(t(u)) = 0 for the factored transfer matrix.

    The supertrace over V_1 x V_2 of the transfer matrix vanishes
    because sdim(gl(1|1)) = 0 (boson-fermion cancellation).
    """

    def test_supertrace_at_u1(self):
        """str(t(1)) = 0."""
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        # VERIFIED [DC] super-cancellation [LT] sdim(gl(1|1)) = 0
        assert ftm.supertrace_transfer(Fraction(1)) == Fraction(0)

    def test_supertrace_at_u5(self):
        """str(t(5)) = 0."""
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        # VERIFIED [DC] super-cancellation [LT] sdim(gl(1|1)) = 0
        assert ftm.supertrace_transfer(Fraction(5)) == Fraction(0)

    def test_supertrace_at_u_half(self):
        """str(t(1/2)) = 0."""
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        # VERIFIED [DC] super-cancellation [LT] sdim(gl(1|1)) = 0
        assert ftm.supertrace_transfer(Fraction(1, 2)) == Fraction(0)


# ================================================================
# 6. INHOMOGENEITY VARIATION
# ================================================================

class TestInhomogeneityVariation:
    """Verify that the bialgebra structure holds for different values
    of the inhomogeneity parameters phi_1, phi_2.

    The integrability and bialgebra axioms are structural properties
    of the gl(1|1) R-matrix, independent of the specific values of
    phi_1 (bosonic) and phi_2 (fermionic).
    """

    def test_shifted_inhomogeneities(self):
        """H3 and commutativity hold for phi_1=1/3, phi_2=7/5."""
        ftm = GL11FactoredTransferMatrix(Fraction(1, 3), Fraction(7, 5))
        # VERIFIED [DC] parameter independence [LT] YBE universality
        assert ftm.transfer_commute_check(Fraction(1), Fraction(2)) is True
        h3 = ftm.verify_H3_via_transfer(Fraction(2))
        assert h3["H3_holds"] is True

    def test_coincident_inhomogeneities(self):
        """Structure persists at phi_1 = phi_2 = 0 (degenerate case)."""
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(0))
        # VERIFIED [DC] degenerate case [LT] R-matrix regularity
        assert ftm.transfer_commute_check(Fraction(1), Fraction(3)) is True

    def test_negative_inhomogeneities(self):
        """Structure persists for phi_1=-2, phi_2=-3."""
        ftm = GL11FactoredTransferMatrix(Fraction(-2), Fraction(-3))
        # VERIFIED [DC] parameter sign independence [LT] YBE universality
        assert ftm.transfer_commute_check(Fraction(1), Fraction(5)) is True
        result = ftm.verify_coassociativity_transfer(
            Fraction(1), Fraction(2), Fraction(3)
        )
        assert result["coassociative"] is True


# ================================================================
# 7. FULL VERIFICATION INTEGRATION
# ================================================================

class TestFullVerification:
    """Verify the complete bialgebra suite via the factored transfer matrix."""

    def test_full_verification_passes(self):
        """The full_verification() method reports all checks passing."""
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        result = ftm.full_verification()
        # VERIFIED [DC] integration test [LT] full bialgebra suite
        assert result["all_H3_pass"] is True
        assert result["all_commute_pass"] is True
        assert result["all_coassoc_pass"] is True
        assert result["all_pass"] is True


# ================================================================
# 8. CROSS-CHECKS: ALGEBRAIC vs RTT ROUTES
# ================================================================

class TestCrossChecks:
    """Cross-verify the bialgebra structure through independent paths.

    Each test below verifies the SAME mathematical fact through two
    independent computational routes. A mismatch between paths
    indicates a bug in one of the routes.

    Cross-checks:
      XC-F1: Algebraic H3 (ConifoldE1Bialgebra) vs RTT H3 (factored transfer)
      XC-F2: Algebraic coassociativity vs transfer commutativity
      XC-F3: Single-site transfer = Id vs factored structure
      XC-F4: YBE on R-matrix vs transfer commutativity
      XC-F5: Full bialgebra verification includes factored data
    """

    def test_xcf1_algebraic_h3_vs_rtt_h3(self):
        """XC-F1: H3 at (1,0)x(0,1) via two independent routes.

        Path A: ConifoldE1Bialgebra.verify_H3_charge_sector("e1", "e2")
                (algebraic: Delta(e1*e2) == Delta(e1)*Delta(e2) term by term).
        Path B: GL11FactoredTransferMatrix.verify_H3_via_transfer(u)
                (RTT: factored monodromy encodes H3 via interchange law).
        """
        # Path A: algebraic
        bialg = ConifoldE1Bialgebra()
        h3_alg = bialg.verify_H3_charge_sector("e1", "e2")
        path_A = h3_alg["H3_holds"]

        # Path B: RTT factored
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        h3_rtt = ftm.verify_H3_via_transfer(Fraction(2))
        path_B = h3_rtt["H3_holds"]

        # CROSS-CHECK [XC-F1] algebraic H3 = RTT H3
        assert path_A is True
        assert path_B is True

    def test_xcf2_algebraic_coassoc_vs_transfer_commute(self):
        """XC-F2: Coassociativity via two independent routes.

        Path A: ConifoldE1Bialgebra.verify_coassociativity (algebraic coproduct).
        Path B: GL11FactoredTransferMatrix.transfer_commute_check (RTT).
        Path C: GL11TransferMatrix.transfer_commute_check (single-site RTT).

        All three are consequences of the same Yangian coproduct structure.
        """
        # Path A: algebraic
        bialg = ConifoldE1Bialgebra()
        for gen in ["e1", "e2", "e12"]:
            result = bialg.verify_coassociativity(gen)
            assert result["coassociative"] is True, f"Path A fails on {gen}"

        # Path B: factored transfer commutativity
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        assert ftm.transfer_commute_check(Fraction(1), Fraction(2)) is True

        # Path C: single-site transfer commutativity
        tm = GL11TransferMatrix()
        assert tm.transfer_commute_check(Fraction(1), Fraction(2)) is True

        # CROSS-CHECK [XC-F2] all three routes confirm coassociativity

    def test_xcf3_single_site_transfer_vs_factored(self):
        """XC-F3: Single-site transfer matrix = Id cross-checked against
        the factored transfer matrix structure.

        Path A: GL11TransferMatrix.transfer_matrix(u) = Id for all u.
        Path B: GL11FactoredTransferMatrix: each single-site t(u-phi_i) = Id,
                verified via the H3 check.
        """
        # Path A: single-site
        tm = GL11TransferMatrix()
        for u_val in [Fraction(1), Fraction(2), Fraction(1, 2)]:
            t = tm.transfer_matrix(u_val)
            for i in range(2):
                for j in range(2):
                    expected = Fraction(1) if i == j else Fraction(0)
                    assert t[i][j] == expected, (
                        f"Single-site t({u_val})[{i}][{j}] = {t[i][j]}, expected {expected}"
                    )

        # Path B: factored check confirms single-site = Id
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))
        h3 = ftm.verify_H3_via_transfer(Fraction(2))
        assert h3["single_site_t1_is_id"] is True
        assert h3["single_site_t2_is_id"] is True

        # CROSS-CHECK [XC-F3] single-site = Id from both routes

    def test_xcf4_ybe_vs_transfer_commute(self):
        """XC-F4: Yang-Baxter equation implies transfer commutativity.

        Path A: YangianGL11.yang_baxter_check (R-matrix level).
        Path B: GL11FactoredTransferMatrix.transfer_commute_check (transfer level).

        YBE is the microscopic identity; transfer commutativity is the
        macroscopic consequence. Both must hold simultaneously.
        """
        yangian = YangianGL11()
        ftm = GL11FactoredTransferMatrix(Fraction(0), Fraction(1))

        for u_val, v_val in [
            (Fraction(1), Fraction(2)),
            (Fraction(3), Fraction(5)),
        ]:
            # Path A: YBE
            ybe_ok = yangian.yang_baxter_check(u_val, v_val)
            # Path B: transfer commutativity
            comm_ok = ftm.transfer_commute_check(u_val, v_val)

            # CROSS-CHECK [XC-F4] YBE => [t(u), t(v)] = 0
            assert ybe_ok is True, f"YBE fails at u={u_val}, v={v_val}"
            assert comm_ok is True, f"Transfer fails at u={u_val}, v={v_val}"

    def test_xcf5_full_bialgebra_includes_factored(self):
        """XC-F5: The conifold_e1_bialgebra_verification() includes
        factored transfer matrix data and all checks pass.
        """
        result = conifold_e1_bialgebra_verification()

        # Standard checks
        assert result["all_H3_pass"] is True
        assert result["all_coassoc_pass"] is True
        assert result["all_counit_pass"] is True
        assert result["all_transfer_commute"] is True

        # Factored transfer checks
        # CROSS-CHECK [XC-F5] factored data integrated into full verification
        assert "factored_transfer" in result
        ft = result["factored_transfer"]
        assert ft["all_H3_pass"] is True
        assert ft["all_commute_pass"] is True
        assert ft["all_coassoc_pass"] is True
        assert ft["all_pass"] is True
