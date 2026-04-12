"""Tests for the spin-2 Drinfeld coproduct on W_{1+infinity} / Y(gl_hat_1).

Verifies the formula:
    Delta_z(T_n) = T_n^L + tilde{T}_n^R(z)
                 + ((Psi-1)/Psi) sum_k J_k^L tilde{J}_{n-k}^R(z)

derived from the Drinfeld coproduct Delta_z(T(u)) = T_L(u)*T_R(u-z)
composed with the Miura inversion T = psi_2 - J^2/(2*Psi).

Key results:
- c_eff = 2 + 2*(Psi-1)^2 (Psi-dependent, NOT constant)
- [Delta(T_n), Delta(J_m)] = -Psi*m * Delta(J_{n+m}) (factor Psi, not 2)
- At Psi=1 (free boson): c_eff=2, factor=1, cross-term vanishes entirely

VERIFIED sources:
[DC] Direct computation from Miura inversion, coefficient (Psi-1)/Psi
[LT] Drinfeld coproduct multiplicative formula (Drinfeld 1987, Tsymbaliuk 2014)
[LC] c_eff at Psi=1 -> 2 (two decoupled copies); Psi=2 -> 4; Psi=3 -> 10
[SY] c_eff at z = 0, 0.3, 0.5+0.3j, 1.0 all agree with formula (z-independence)
"""

import pytest

from compute.lib.chiral_coproduct_spin2_engine import (
    HeisenbergFock,
    TensorHeisenberg,
    c_eff_expected,
    derive_antipode_J,
    derive_antipode_T,
    extract_c_eff,
    verify_antipode_consistency,
    verify_c_eff_level_dependence,
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
    """Spin-2 Drinfeld coproduct Delta_z(T_n)."""

    def test_z0_consistency(self):
        r = verify_z0_consistency(Psi=1.0, N_max=6)
        assert r["ok"], f"error {r['error']:.2e}"

    def test_z0_consistency_Psi2(self):
        r = verify_z0_consistency(Psi=2.0, N_max=6)
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
    """Effective central charge c_eff = 2 + 2*(Psi-1)^2 in the image."""

    def test_c_eff_2_Psi1_z0(self):
        # VERIFIED: c_eff = 2 at Psi=1 [DC] cross-term vanishes, two decoupled copies.
        # [LC] At Psi=1, (Psi-1)/Psi = 0 so Delta(T) = T^L + T^R.
        r = extract_c_eff(Psi=1.0, N_max=6, z=0.0)
        assert r["c_eff_correct"], f"c_eff = {r['c_eff']} (expected 2.0)"

    def test_c_eff_4_Psi2_z0(self):
        # VERIFIED: c_eff = 4 at Psi=2 [DC] coefficient (Psi-1)/Psi = 1/2.
        r = extract_c_eff(Psi=2.0, N_max=6, z=0.0)
        assert r["c_eff_correct"], f"c_eff = {r['c_eff']} (expected 4.0)"

    def test_c_eff_25_Psi_half(self):
        # VERIFIED: c_eff = 2.5 at Psi=0.5 [DC] coefficient (Psi-1)/Psi = -1.
        # [LC] 2 + 2*(0.5-1)^2 = 2 + 0.5 = 2.5.
        r = extract_c_eff(Psi=0.5, N_max=6, z=0.0)
        assert r["c_eff_correct"], f"c_eff = {r['c_eff']} (expected 2.5)"

    def test_c_eff_z_independence(self):
        # VERIFIED: c_eff does not depend on z [SY] spectral parameter independence.
        for z_val in [0.0, 0.5 + 0.3j, 1.0]:
            r = extract_c_eff(Psi=2.0, N_max=6, z=complex(z_val))
            assert r["c_eff_correct"], f"z={z_val}: c_eff = {r['c_eff']}"

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.7])
    def test_c_eff_formula(self, Psi):
        # VERIFIED: c_eff = 2 + 2*(Psi-1)^2 for all Psi [DC]+[LC].
        r = extract_c_eff(Psi=Psi, N_max=6, z=0.5 + 0.3j)
        assert r["c_eff_correct"], (
            f"Psi={Psi}: c_eff = {r['c_eff']:.4f} "
            f"(expected {c_eff_expected(Psi):.4f})"
        )

    def test_full_level_dependence(self):
        # VERIFIED: all (Psi, z) pairs match formula [LC]+[SY].
        r = verify_c_eff_level_dependence(N_max=6)
        assert r["ok"]


class TestIntertwining:
    """[Delta(T_n), Delta(J_m)] = -Psi*m * Delta(J_{n+m})."""

    def test_intertwining_z0_Psi1(self):
        # VERIFIED: factor = Psi = 1 at Psi=1, cross-term vanishes [DC].
        r = verify_T_J_intertwining(Psi=1.0, N_max=6, z=0.0)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_intertwining_z0_Psi2(self):
        # VERIFIED: factor = Psi = 2 at Psi=2 [DC].
        r = verify_T_J_intertwining(Psi=2.0, N_max=6, z=0.0)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_intertwining_z_complex(self):
        # VERIFIED: holds at z = 0.5 + 0.3j [DC]+[SY].
        r = verify_T_J_intertwining(Psi=1.0, N_max=6, z=0.5 + 0.3j)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_intertwining_Psi_half(self):
        # VERIFIED: factor = Psi = 0.5 at Psi=0.5 [DC].
        r = verify_T_J_intertwining(Psi=0.5, N_max=6, z=0.0)
        assert r["ok"], f"max error {r['max_error']:.2e}"


# ---------------------------------------------------------------------------
# Antipode: S(J_n) = -J_n, S(T_n) = (2*Psi - 3)*T_n
# ---------------------------------------------------------------------------

class TestAntipodeJ:
    """Spin-1 antipode S(J_n) = -J_n (sign flip for primitive elements)."""

    def test_hopf_axiom_Psi1(self):
        # VERIFIED: S(J_n) = -J_n, m(S x id)Delta(J_n) = 0 [DC].
        H = HeisenbergFock(Psi=1.0, N_max=6)
        r = derive_antipode_J(H)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_hopf_axiom_Psi2(self):
        # VERIFIED: same formula at Psi=2 [DC].
        H = HeisenbergFock(Psi=2.0, N_max=6)
        r = derive_antipode_J(H)
        assert r["ok"], f"max error {r['max_error']:.2e}"


class TestAntipodeT:
    """Spin-2 antipode S(T_n) = (2*Psi - 3)*T_n.

    Derived from the Hopf axiom m(S tensor id)Delta_0(T_n) = 0 using:
    - Delta_0(T_n) = T_n^L + T_n^R + ((Psi-1)/Psi) sum_k J_k^L J_{n-k}^R
    - S(J_k) = -J_k
    - sum_k J_k J_{n-k} = 2*Psi*T_n  for n != 0

    The coefficient (2*Psi-3) arises from:
      S(T_n) = -T_n + ((Psi-1)/Psi) * 2*Psi * T_n = (2*Psi - 3)*T_n
    """

    def test_hopf_axiom_Psi1(self):
        # VERIFIED: S(T_n) = -T_n at Psi=1 (primitive, cross-term vanishes) [DC].
        r = derive_antipode_T(Psi=1.0, N_max=6)
        assert r["ok"]
        assert abs(r["S_T_coefficient"] - (-1.0)) < 1e-12

    def test_hopf_axiom_Psi2(self):
        # VERIFIED: S(T_n) = T_n at Psi=2 (involutive, S^2 = id) [DC].
        r = derive_antipode_T(Psi=2.0, N_max=6)
        assert r["ok"]
        assert abs(r["S_T_coefficient"] - 1.0) < 1e-12

    def test_hopf_axiom_Psi_half(self):
        # VERIFIED: S(T_n) = -2*T_n at Psi=0.5 [DC].
        r = derive_antipode_T(Psi=0.5, N_max=6)
        assert r["ok"]
        assert abs(r["S_T_coefficient"] - (-2.0)) < 1e-12

    def test_hopf_axiom_Psi3(self):
        # VERIFIED: S(T_n) = 3*T_n at Psi=3 [DC].
        r = derive_antipode_T(Psi=3.0, N_max=6)
        assert r["ok"]
        assert abs(r["S_T_coefficient"] - 3.0) < 1e-12

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.0, 3.7])
    def test_S_coefficient_formula(self, Psi):
        # VERIFIED: S(T_n) = (2*Psi-3)*T_n for all Psi [DC].
        r = derive_antipode_T(Psi=Psi, N_max=6)
        assert r["ok"]
        expected = 2.0 * Psi - 3.0
        assert abs(r["S_T_coefficient"] - expected) < 1e-10, (
            f"Psi={Psi}: S_coeff={r['S_T_coefficient']} (expected {expected})"
        )

    def test_S_squared_involutive_Psi1(self):
        # VERIFIED: S^2(T_n) = T_n at Psi=1 (cocommutative case) [DC].
        r = derive_antipode_T(Psi=1.0, N_max=6)
        assert r["S_squared_is_id"]

    def test_S_squared_involutive_Psi2(self):
        # VERIFIED: S^2(T_n) = T_n at Psi=2 (special value) [DC].
        r = derive_antipode_T(Psi=2.0, N_max=6)
        assert r["S_squared_is_id"]

    def test_S_squared_non_involutive_Psi3(self):
        # VERIFIED: S^2 != id at Psi=3 (non-cocommutative, S^2=Ad(u)) [DC].
        r = derive_antipode_T(Psi=3.0, N_max=6)
        assert not r["S_squared_is_id"]

    def test_not_quasi_hopf(self):
        # VERIFIED: genuine Hopf algebra, not quasi-Hopf [DC].
        r = derive_antipode_T(Psi=2.0, N_max=6)
        assert not r["quasi_hopf"]


class TestAntipodeConsistency:
    """Full antipode consistency across multiple Psi values."""

    def test_full_consistency(self):
        # VERIFIED: Hopf axiom holds at Psi in {0.5, 1.0, 2.0, 3.0} [DC].
        r = verify_antipode_consistency(N_max=6)
        assert r["ok"]
