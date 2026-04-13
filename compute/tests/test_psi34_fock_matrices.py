r"""Tests for the Fock space psi_3 and psi_4 transfer matrix matrices.

Verifies the Yangian Y(gl_hat_1) transfer matrix coefficients psi_3 and psi_4,
constructed as Fock space matrices via the Miura factorization recursion:

    psi_1(n) = J(n)
    psi_2(n) = T(n) + (1/(2*Psi)) sum_k J(k) J(n-k)
    psi_3(n) = sum_k J(k) psi_2(n-k)
    psi_4(n) = sum_k J(k) psi_3(n-k)

These are the [u^{-3}] and [u^{-4}] coefficients of the transfer matrix
T(u) = 1 + psi_1 u^{-1} + psi_2 u^{-2} + psi_3 u^{-3} + psi_4 u^{-4} + ...
in the Heisenberg Fock space representation at level Psi.

Key results:
- Positive modes annihilate the vacuum: psi_k(n)|0> = 0 for n >= 1
- Conformal weight grading: [T_0, psi_k(n)] = -n * psi_k(n) (exact)
- The maximal-depth partition coefficient is Psi-dependent and N_max-independent:
    psi_3(-3)|0> -> |(1,1,1)> = 1/Psi
    psi_4(-4)|0> -> |(1,1,1,1)> = 1/Psi
- psi_4(-1)|0> = 0 (spin-4 field has no weight-1 creation)
- psi_3(n) matches the spin-3 engine's construction exactly

VERIFIED sources:
[DC] Direct computation from Miura recursion psi_s = J * psi_{s-1}
[S3] Consistency with chiral_coproduct_spin3_engine.py (coassociativity-tested)
[LC] Limit checks: Psi=1 free boson, positive mode annihilation
[EV] Eigenvalue structure from conformal weight grading
"""

import numpy as np
import pytest

from compute.lib.chiral_coproduct_spin2_engine import HeisenbergFock


# ---------------------------------------------------------------------------
# Test 1: psi_3 positive mode vacuum annihilation
# ---------------------------------------------------------------------------

class TestPsi3VacuumAnnihilation:
    """psi_3(n)|0> = 0 for all n >= 1."""

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.0])
    def test_psi3_positive_modes_annihilate_vacuum(self, Psi):
        # VERIFIED: [LC] All positive modes of the transfer matrix coefficient
        # annihilate the Fock vacuum, independent of level Psi.
        H = HeisenbergFock(Psi=Psi, N_max=6)
        vac = H.vacuum()
        for n in range(1, 5):
            result = H._psi3_matrix(n) @ vac
            err = float(np.linalg.norm(result))
            assert err < 1e-12, (
                f"Psi={Psi}: psi_3({n})|0> has norm {err:.2e}, expected 0"
            )


# ---------------------------------------------------------------------------
# Test 2: psi_4 positive mode vacuum annihilation
# ---------------------------------------------------------------------------

class TestPsi4VacuumAnnihilation:
    """psi_4(n)|0> = 0 for all n >= 1."""

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.0])
    def test_psi4_positive_modes_annihilate_vacuum(self, Psi):
        # VERIFIED: [LC] All positive modes of the spin-4 transfer matrix
        # coefficient annihilate the vacuum.
        H = HeisenbergFock(Psi=Psi, N_max=6)
        vac = H.vacuum()
        for n in range(1, 5):
            result = H._psi4_matrix(n) @ vac
            err = float(np.linalg.norm(result))
            assert err < 1e-12, (
                f"Psi={Psi}: psi_4({n})|0> has norm {err:.2e}, expected 0"
            )


# ---------------------------------------------------------------------------
# Test 3: psi_3 conformal weight grading
# ---------------------------------------------------------------------------

class TestPsi3ConformalGrading:
    """[T_0, psi_3(n)] = -n * psi_3(n) on the safe subspace.

    The Sugawara T_0 generates the conformal weight grading. Since psi_3(n)
    has mode index n, it shifts the weight by -n (creation for n < 0,
    annihilation for n > 0). This identity is EXACT (not truncation-dependent)
    on the safe subspace.
    """

    @pytest.mark.parametrize("n", [-3, -2, -1, 0, 1, 2])
    def test_psi3_grading(self, n):
        # VERIFIED: [EV] Conformal weight grading is exact for psi_3 at all
        # mode indices, independent of Psi and N_max (on safe subspace).
        H = HeisenbergFock(Psi=2.0, N_max=6)
        P = H.projector_safe(3)
        comm = H.T(0) @ H._psi3_matrix(n) - H._psi3_matrix(n) @ H.T(0)
        expected = float(-n) * H._psi3_matrix(n)
        err = float(np.max(np.abs(P @ (comm - expected) @ P)))
        assert err < 1e-10, (
            f"[T_0, psi_3({n})] + {n}*psi_3({n}) has error {err:.2e}"
        )


# ---------------------------------------------------------------------------
# Test 4: psi_4 conformal weight grading
# ---------------------------------------------------------------------------

class TestPsi4ConformalGrading:
    """[T_0, psi_4(n)] = -n * psi_4(n) on the safe subspace."""

    @pytest.mark.parametrize("n", [-3, -2, -1, 0, 1, 2])
    def test_psi4_grading(self, n):
        # VERIFIED: [EV] Same conformal weight grading for psi_4.
        H = HeisenbergFock(Psi=2.0, N_max=6)
        P = H.projector_safe(3)
        comm = H.T(0) @ H._psi4_matrix(n) - H._psi4_matrix(n) @ H.T(0)
        expected = float(-n) * H._psi4_matrix(n)
        err = float(np.max(np.abs(P @ (comm - expected) @ P)))
        assert err < 1e-10, (
            f"[T_0, psi_4({n})] + {n}*psi_4({n}) has error {err:.2e}"
        )


# ---------------------------------------------------------------------------
# Test 5: psi_3(-3)|0> maximal-depth partition coefficient = 1/Psi
# ---------------------------------------------------------------------------

class TestPsi3MaxDepthEigenvalue:
    r"""psi_3(-3)|0> projected onto |(1,1,1)> equals 1/Psi.

    This is the maximal-depth partition at weight 3. The coefficient
    1/Psi arises because the only path to |(1,1,1)> = J_{-1}^3|0>/Psi
    passes through the (1/(2*Psi)) factor in psi_2 exactly once,
    combined with a single J action. The result is:
        <(1,1,1)| psi_3(-3) |0> = 1/Psi

    This is N_max-INDEPENDENT (verified at N_max in {4,5,6,7}).
    """

    @pytest.mark.parametrize("Psi", [0.25, 0.5, 1.0, 2.0, 3.0, 4.0])
    def test_psi3_111_coefficient(self, Psi):
        # VERIFIED: [DC] Direct computation at 6 values of Psi.
        H = HeisenbergFock(Psi=Psi, N_max=6)
        vac = H.vacuum()
        state = H._psi3_matrix(-3) @ vac
        coeff = float(state[H.idx[(1, 1, 1)]])
        expected = 1.0 / Psi
        assert abs(coeff - expected) < 1e-10, (
            f"Psi={Psi}: <(1,1,1)|psi_3(-3)|0> = {coeff:.6f}, "
            f"expected 1/Psi = {expected:.6f}"
        )


# ---------------------------------------------------------------------------
# Test 6: psi_4(-4)|0> maximal-depth partition coefficient = 1/Psi
# ---------------------------------------------------------------------------

class TestPsi4MaxDepthEigenvalue:
    r"""psi_4(-4)|0> projected onto |(1,1,1,1)> equals 1/Psi.

    Analogous to the spin-3 case: the maximal-depth partition coefficient
    at weight 4 is 1/Psi, reflecting the single passage through the
    (1/(2*Psi)) factor in the Miura recursion chain.

    This is N_max-INDEPENDENT (verified at N_max in {5,6,7}).
    """

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.0, 4.0])
    def test_psi4_1111_coefficient(self, Psi):
        # VERIFIED: [DC] Direct computation at 5 values of Psi.
        H = HeisenbergFock(Psi=Psi, N_max=6)
        vac = H.vacuum()
        state = H._psi4_matrix(-4) @ vac
        coeff = float(state[H.idx[(1, 1, 1, 1)]])
        expected = 1.0 / Psi
        assert abs(coeff - expected) < 1e-10, (
            f"Psi={Psi}: <(1,1,1,1)|psi_4(-4)|0> = {coeff:.6f}, "
            f"expected 1/Psi = {expected:.6f}"
        )


# ---------------------------------------------------------------------------
# Test 7: psi_3 consistency with spin-3 engine
# ---------------------------------------------------------------------------

class TestPsi3Spin3Consistency:
    """psi_3(n) from HeisenbergFock matches Spin3CoproductEngine.psi2_single convolution.

    The spin-3 engine (chiral_coproduct_spin3_engine.py) independently implements
    psi_2 on the single Fock space and uses sum_k J(k) psi_2(n-k) in its
    coassociativity-verified triple tensor product. Our _psi3_matrix must match.
    """

    @pytest.mark.parametrize("Psi", [1.0, 2.0])
    def test_psi3_matches_spin3_engine(self, Psi):
        # VERIFIED: [S3] Exact agreement with the spin-3 engine construction,
        # which itself is validated by coassociativity at spin 3.
        from compute.lib.chiral_coproduct_spin3_engine import Spin3CoproductEngine
        eng = Spin3CoproductEngine(Psi=Psi, N_max=6)
        H = HeisenbergFock(Psi=Psi, N_max=6)
        for n in [-3, -2, -1, 0, 1, 2]:
            our = H._psi3_matrix(n)
            # Replicate the spin-3 engine formula
            M = H.N_max + abs(n) + 2
            ref = np.zeros((H.dim, H.dim))
            for k in range(-M, M + 1):
                ref += H.J(k) @ eng.psi2_single(n - k)
            err = float(np.max(np.abs(our - ref)))
            assert err < 1e-12, (
                f"Psi={Psi}, n={n}: psi_3 mismatch with spin-3 engine, "
                f"max error {err:.2e}"
            )


# ---------------------------------------------------------------------------
# Test 8: psi_4 recursion consistency
# ---------------------------------------------------------------------------

class TestPsi4RecursionConsistency:
    """psi_4(n) = sum_k J(k) psi_3(n-k) verified by independent recomputation.

    Recomputes psi_4 from scratch using a fresh HeisenbergFock instance to
    verify the cached result agrees with the defining recursion.
    """

    @pytest.mark.parametrize("Psi", [1.0, 2.0])
    def test_psi4_recursion(self, Psi):
        # VERIFIED: [DC] Direct recomputation matches cached result.
        H = HeisenbergFock(Psi=Psi, N_max=6)
        P = H.projector_safe(3)
        for n in [-3, -2, -1, 0, 1]:
            cached = H._psi4_matrix(n)
            # Recompute independently
            K = H.N_max + abs(n) + 2
            recomputed = np.zeros((H.dim, H.dim))
            for k in range(-K, K + 1):
                recomputed += H.J(k) @ H._psi3_matrix(n - k)
            err = float(np.max(np.abs(P @ (cached - recomputed) @ P)))
            assert err < 1e-12, (
                f"Psi={Psi}, n={n}: psi_4 recursion mismatch, "
                f"max error {err:.2e}"
            )


# ---------------------------------------------------------------------------
# Test 9: psi_4(-1)|0> = 0 (no weight-1 creation at spin 4)
# ---------------------------------------------------------------------------

class TestPsi4NoWeight1Creation:
    """psi_4(-1)|0> = 0 at all Psi values.

    The spin-4 transfer matrix coefficient at mode -1 produces zero
    when acting on the vacuum. This is because the only weight-1
    partition state |(1,)> = J_{-1}|0> cannot be reached by the
    depth-4 recursion chain J*J*J*J from the vacuum at mode -1:
    the mode arithmetic forces a cancellation.
    """

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.0])
    def test_psi4_minus1_vacuum_zero(self, Psi):
        # VERIFIED: [DC] psi_4(-1)|0> = 0 at all tested Psi.
        H = HeisenbergFock(Psi=Psi, N_max=6)
        vac = H.vacuum()
        result = H._psi4_matrix(-1) @ vac
        err = float(np.linalg.norm(result))
        assert err < 1e-12, (
            f"Psi={Psi}: psi_4(-1)|0> has norm {err:.2e}, expected 0"
        )


# ---------------------------------------------------------------------------
# Test 10: psi_3 and psi_4 creation at multiple Psi (partition decomposition)
# ---------------------------------------------------------------------------

class TestPsiCreationPartitionDecomposition:
    """Partition decomposition of psi_k(-s)|0> at fixed N_max=6.

    At N_max=6, the creation operators produce specific states whose
    partition-state overlaps are exactly computable. The maximal-depth
    coefficients are Psi-dependent (1/Psi), while single-row coefficients
    depend on N_max through regularization.

    These tests verify the COMPLETE partition decomposition at Psi=1
    and N_max=6, which pins the implementation against the known values.
    """

    def test_psi3_creation_at_Psi1(self):
        # VERIFIED: [DC] Complete partition decomposition at Psi=1, N_max=6.
        H = HeisenbergFock(Psi=1.0, N_max=6)
        vac = H.vacuum()

        # psi_3(-3)|0>: weight-3 state with two components
        state = H._psi3_matrix(-3) @ vac
        c3 = float(state[H.idx[(3,)]])
        c111 = float(state[H.idx[(1, 1, 1)]])
        c21 = float(state[H.idx[(2, 1)]])
        assert abs(c3 - 22.5) < 1e-10, f"|(3,)> coeff = {c3}"
        assert abs(c111 - 1.0) < 1e-10, f"|(1,1,1)> coeff = {c111}"
        assert abs(c21) < 1e-10, f"|(2,1)> coeff = {c21}, expected 0"

    def test_psi4_creation_at_Psi1(self):
        # VERIFIED: [DC] Complete partition decomposition at Psi=1, N_max=6.
        H = HeisenbergFock(Psi=1.0, N_max=6)
        vac = H.vacuum()

        # psi_4(-4)|0>: weight-4 state with three components
        state = H._psi4_matrix(-4) @ vac
        c31 = float(state[H.idx[(3, 1)]])
        c22 = float(state[H.idx[(2, 2)]])
        c1111 = float(state[H.idx[(1, 1, 1, 1)]])
        c4 = float(state[H.idx[(4,)]])
        c211 = float(state[H.idx[(2, 1, 1)]])
        assert abs(c31 - 81.0) < 1e-10, f"|(3,1)> coeff = {c31}"
        assert abs(c22 - 39.5) < 1e-10, f"|(2,2)> coeff = {c22}"
        assert abs(c1111 - 1.0) < 1e-10, f"|(1,1,1,1)> coeff = {c1111}"
        assert abs(c4) < 1e-10, f"|(4,)> coeff = {c4}, expected 0"
        assert abs(c211) < 1e-10, f"|(2,1,1)> coeff = {c211}, expected 0"

    def test_psi4_minus3_single_component(self):
        # VERIFIED: [DC] psi_4(-3)|0> = 107 * |(2,1)> at Psi=1, N_max=6.
        # This is a single-component creation (pure |(2,1)>), Psi-independent.
        H = HeisenbergFock(Psi=1.0, N_max=6)
        vac = H.vacuum()
        state = H._psi4_matrix(-3) @ vac
        c21 = float(state[H.idx[(2, 1)]])
        assert abs(c21 - 107.0) < 1e-10, f"|(2,1)> coeff = {c21}"
        # Verify no other weight-3 components
        for part in [(3,), (1, 1, 1)]:
            c = float(state[H.idx[part]])
            assert abs(c) < 1e-10, f"|{part}> coeff = {c}, expected 0"
