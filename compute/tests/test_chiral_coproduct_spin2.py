"""Tests for the spin-2 Yangian coproduct on W_{1+infinity} / Y(gl_hat_1).

Verifies the formula:
    Delta_z(T_n) = T_n^L + tilde{T}_n^R(z) + (1/Psi) sum_k J_k^L tilde{J}_{n-k}^R(z)

derived from the multiplicative Yangian coproduct Delta_z(psi(u)) = psi_L(u)*psi_R(u-z).

Key results:
- c_eff = 4 on the vacuum (= c_L + c_R + c_cross = 1 + 1 + 2)
- [Delta(T_n), Delta(J_m)] = -2m * Delta(J_{n+m}) (factor 2 from cross term)
- c_eff = 4 independent of level Psi and spectral parameter z

VERIFIED sources:
[DC] Direct computation from Sugawara formula + mode commutators
[LT] Drinfeld coproduct multiplicative formula (Drinfeld 1987, Tsymbaliuk 2014)
[LC] c_eff at Psi = 0.5, 1.0, 2.0, 3.7 all give 4 (level independence)
[SY] c_eff at z = 0, 0.3, 0.5+0.3j, 1.0 all give 4 (spectral independence)
"""

import pytest

from compute.lib.chiral_coproduct_spin2_engine import (
    HeisenbergFock,
    TensorHeisenberg,
    extract_c_eff,
    verify_c_eff_independence,
    verify_delta_J,
    verify_heisenberg,
    verify_T_J_intertwining,
    verify_T0_eigenvalues,
    verify_virasoro,
    verify_z0_consistency,
)


# ---------------------------------------------------------------------------
# Foundation: single-copy algebra
# ---------------------------------------------------------------------------

class TestHeisenberg:
    """Heisenberg commutation relations on safe subspace."""

    def test_commutators_Psi1(self):
        r = verify_heisenberg(Psi=1.0, N_max=6)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_commutators_Psi2(self):
        r = verify_heisenberg(Psi=2.0, N_max=6)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_vacuum_annihilation(self):
        H = HeisenbergFock(Psi=1.0, N_max=6)
        vac = H.vacuum()
        for n in range(1, 4):
            assert float(max(abs(H.J(n) @ vac))) < 1e-15, f"J_{n}|0> != 0"


class TestVirasoro:
    """Sugawara Virasoro at c = 1."""

    def test_virasoro_Psi1(self):
        r = verify_virasoro(Psi=1.0, N_max=6)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_virasoro_Psi_half(self):
        r = verify_virasoro(Psi=0.5, N_max=6)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_T0_vacuum(self):
        # VERIFIED: T_0|0> = 0 [DC] direct, [LC] consistent with c=1.
        H = HeisenbergFock(Psi=1.0, N_max=6)
        vac = H.vacuum()
        T0_vac = H.T(0) @ vac
        assert float(max(abs(T0_vac))) < 1e-12

    def test_T0_J_eigenvalue(self):
        # VERIFIED: T_0 J_{-1}|0> = 1 * J_{-1}|0> [DC] Sugawara eigenvalue.
        H = HeisenbergFock(Psi=1.0, N_max=6)
        J_state = H.J(-1) @ H.vacuum()
        T0_J = H.T(0) @ J_state
        diff = float(max(abs(T0_J - J_state)))
        assert diff < 1e-10


# ---------------------------------------------------------------------------
# Spin-1 coproduct
# ---------------------------------------------------------------------------

class TestDeltaJ:
    """Primitive coproduct Delta_z(J) = J^L + J^R(shifted)."""

    def test_preserves_commutators(self):
        # VERIFIED: [DC] Delta(J) satisfies [Delta(J_m), Delta(J_n)] = 2*Psi*m*delta.
        r = verify_delta_J(Psi=1.0, N_max=6, z=0.5 + 0.3j)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_z0_primitive(self):
        r = verify_delta_J(Psi=1.0, N_max=6, z=0.0)
        assert r["ok"], f"max error {r['max_error']:.2e}"


# ---------------------------------------------------------------------------
# Spin-2 coproduct: the main result
# ---------------------------------------------------------------------------

class TestDeltaT:
    """Spin-2 Yangian coproduct Delta_z(T_n)."""

    def test_z0_consistency(self):
        r = verify_z0_consistency(Psi=1.0, N_max=6)
        assert r["ok"], f"error {r['error']:.2e}"

    def test_vacuum_eigenvalue_zero(self):
        # VERIFIED: Delta(T_0)|0,0> = 0 [DC] conformal weight of vacuum.
        r = verify_T0_eigenvalues(Psi=1.0, N_max=6)
        assert r["vac_zero"]

    def test_J_eigenvalue_one(self):
        # VERIFIED: Delta(T_0)|J_{-1}|0>,|0>> = 1 [DC] conformal weight of J.
        r = verify_T0_eigenvalues(Psi=1.0, N_max=6)
        assert r["J-1_vac_correct"]


class TestCeff:
    """Effective central charge c_eff = 4 in the image."""

    def test_c_eff_4_z0(self):
        # VERIFIED: c_eff = 4 [DC] from [Delta(T_2), Delta(T_{-2})] vacuum element.
        r = extract_c_eff(Psi=1.0, N_max=6, z=0.0)
        assert r["c_eff_correct"], f"c_eff = {r['c_eff']}"

    def test_c_eff_4_z_complex(self):
        # VERIFIED: c_eff = 4 [SY] spectral parameter independence.
        r = extract_c_eff(Psi=1.0, N_max=6, z=0.5 + 0.3j)
        assert r["c_eff_correct"], f"c_eff = {r['c_eff']}"

    def test_c_eff_4_z1(self):
        r = extract_c_eff(Psi=1.0, N_max=6, z=1.0)
        assert r["c_eff_correct"], f"c_eff = {r['c_eff']}"

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.7])
    def test_c_eff_level_independence(self, Psi):
        # VERIFIED: c_eff = 4 for all Psi [LC] level independence.
        r = extract_c_eff(Psi=Psi, N_max=6, z=0.5 + 0.3j)
        assert r["c_eff_correct"], f"Psi={Psi}: c_eff = {r['c_eff']}"

    def test_full_independence(self):
        # VERIFIED: 12/12 (Psi, z) pairs give c_eff = 4 [LC]+[SY].
        r = verify_c_eff_independence(N_max=6)
        assert r["ok"]


class TestIntertwining:
    """[Delta(T_n), Delta(J_m)] = -2m * Delta(J_{n+m})."""

    def test_intertwining_z0(self):
        # VERIFIED: factor 2 from cross-term action on both J^L and J^R [DC].
        r = verify_T_J_intertwining(Psi=1.0, N_max=6, z=0.0)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_intertwining_z_complex(self):
        # VERIFIED: holds at z = 0.5 + 0.3j [DC]+[SY].
        r = verify_T_J_intertwining(Psi=1.0, N_max=6, z=0.5 + 0.3j)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_intertwining_Psi2(self):
        r = verify_T_J_intertwining(Psi=2.0, N_max=6, z=0.0)
        assert r["ok"], f"max error {r['max_error']:.2e}"
