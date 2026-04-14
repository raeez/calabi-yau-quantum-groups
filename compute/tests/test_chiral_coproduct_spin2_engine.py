import numpy as np
from fractions import Fraction

from compute.lib.chiral_coproduct_spin2_engine import (
    HeisenbergFock,
    TensorHeisenberg,
    compute_delta3_T0,
    extract_c_eff,
    verify_heisenberg,
    verify_virasoro,
)
from compute.lib.a_infinity_bar_w1inf import (
    AInfBarComplex,
    AInfShadowTower,
    T,
    W1InfOPE,
)


def test_spin2_heisenberg_and_virasoro_checks():
    virasoro = verify_virasoro()

    assert verify_heisenberg()["ok"]
    assert virasoro["ok"]
    assert virasoro["c"] == 1.0


def test_spin2_effective_central_charge_formula():
    result = extract_c_eff(2.0)

    assert result["c_eff_correct"]
    assert result["c_eff"] == 4.0


# ================================================================
#  A_inf coproduct correction delta^{(3)}(T_0)
# ================================================================


class TestDelta3CoproductCorrection:
    r"""Test the first A_inf coproduct correction delta^{(3)}(T_0).

    The A_inf coproduct deforms the Drinfeld coproduct:
        Delta^{A_inf} = Delta^{Yan} + hbar^2 * delta^{(3)} + ...

    The obstruction to Delta^{Yan} being an A_inf morphism at m_3:
        O_3 = m_3^{tensor}(Delta(T)^3) - Delta(m_3(T^3))
            = 2 * alpha_cop * X_0   (at leading order)
    where alpha_cop = (Psi-1)/Psi, X_0 = sum_k J_k^L J_{-k}^R.

    The normalized weight-1 transfer matrix element of O_3
    gives delta^{(3)} = 2*(Psi - 1) = -m_3_coeff * (Psi - 1).

    At Psi=2 (self-dual point): delta^{(3)} = 2 = S_3 (spin-2 shadow),
    confirming S_k = delta^{(k)} at this level.

    Manuscript references:
        Vol III: a_infinity_bar_w1inf.py (m_3(T,T,T) = -2T)
        Vol III: c3_shadow_tower.py (S_3 = 2 for spin-2 at c=1)
        Vol III: chiral_coproduct_spin2_engine.py (Drinfeld coproduct)
    """

    def test_delta3_at_psi2_equals_S3(self):
        """delta^{(3)}(T_0) = 2 = S_3 at Psi=2 (self-dual point).

        The NUMBER: 2. This is the spin-2 cubic shadow from the
        A_inf bar complex, confirming S_k = delta^{(k)}.
        """
        # VERIFIED [DC] Fock matrix element [CT] S_3 from shadow tower
        result = compute_delta3_T0(Psi=2.0, N_max=8)
        assert result["delta3_value"] == 2.0
        assert result["match_S3_at_Psi2"] is True

    def test_delta3_equals_minus_m3_coeff_times_psi_minus_1(self):
        r"""delta^{(3)}(T_0; Psi) = -m_3_coeff * (Psi - 1) = 2*(Psi - 1).

        The exact formula at all Psi values. Derived from:
        O_3 = 2*alpha_cop*X_0, physical me(X_0) = Psi^2,
        normalized: 2*alpha_cop*Psi = 2*(Psi-1).
        """
        # VERIFIED [DC] exact formula [DA] alpha_cop dependence
        for Psi in [1.0, 1.5, 2.0, 3.0, 5.0]:
            result = compute_delta3_T0(Psi=Psi, N_max=8)
            assert result["match_exact"], f"Failed at Psi={Psi}"
            expected = 2.0 * (Psi - 1.0)
            assert abs(result["delta3_value"] - expected) < 1e-10

    def test_delta3_vanishes_at_psi1(self):
        """At Psi=1 (free boson): delta^{(3)} = 0.

        The Heisenberg at Psi=1 is a vertex bialgebra with primitive
        coproduct Delta(J) = J^L + J^R. No cross-term, no correction.
        """
        # VERIFIED [DC] free boson limit [LT] primitive coproduct
        result = compute_delta3_T0(Psi=1.0, N_max=8)
        assert result["delta3_value"] == 0.0

    def test_delta3_is_minus2_times_kappa_ch_at_psi2(self):
        r"""The obstruction coefficient: O_3 matrix element = -2 * kappa_ch * (-2).

        At Psi=2, the normalized matrix element of the cross-term X_0 = Psi = 2.
        The obstruction O_3 = X_0 (since 2*alpha_cop = 1 at Psi=2).
        So delta^{(3)} = 2 = -2 * kappa_ch * m_3_coeff
                            = -2 * (1/2) * (-2) = 2.
        """
        # VERIFIED [DC] kappa decomposition [CT] shadow tower kappa_ch = 1/2
        result = compute_delta3_T0(Psi=2.0, N_max=8)
        kappa_ch = result["kappa_ch"]
        m3_coeff = result["m3_coeff"]
        assert kappa_ch == 0.5
        assert m3_coeff == -2
        assert abs(result["delta3_value"] - (-2.0 * kappa_ch * m3_coeff)) < 1e-10

    # ---- Cross-checks (AP10: multi-path verification) ----

    def test_delta3_cross_check_shadow_tower_S3(self):
        """Cross-check: delta^{(3)} at Psi=2 matches S_3 from shadow tower module.

        Path 1: compute_delta3_T0 (Fock space matrix element).
        Path 2: AInfShadowTower.shadow_tower_channel (convolution recursion).
        Both must give 2.
        """
        # Path 1: Fock space
        result = compute_delta3_T0(Psi=2.0, N_max=8)
        delta3 = result["delta3_value"]

        # Path 2: shadow tower recursion from a_infinity_bar_w1inf
        ope = W1InfOPE(c=Fraction(1))
        bar_cx = AInfBarComplex(ope=ope)
        shadow = AInfShadowTower(bar_cx, max_spin=3)
        tower = shadow.shadow_tower_channel(2, max_r=4)
        S3_from_tower = float(tower[3])

        assert abs(delta3 - S3_from_tower) < 1e-10

    def test_delta3_cross_check_m3_coefficient(self):
        """Cross-check: m_3(T,T,T) coefficient from bar complex matches engine.

        Path 1: compute_delta3_T0 returns m3_coeff = -2.
        Path 2: AInfBarComplex.m3(T,T,T) directly.
        """
        # Path 1
        result = compute_delta3_T0(Psi=2.0, N_max=8)
        m3_from_engine = result["m3_coeff"]

        # Path 2
        bar_cx = AInfBarComplex()
        m3_result = bar_cx.m3(T, T, T).simplify()
        m3_from_bar = int(m3_result.terms[0].coeff)

        assert m3_from_engine == m3_from_bar == -2

    def test_delta3_cross_check_direct_operator(self):
        """Cross-check: direct operator construction matches compute_delta3_T0.

        Path 1: compute_delta3_T0 (the engine function).
        Path 2: build O_3 = 2*alpha_cop*X_0 directly and extract matrix element.
        """
        Psi = 2.0
        N_max = 8

        # Path 1
        result = compute_delta3_T0(Psi=Psi, N_max=N_max)
        delta3_engine = result["delta3_value"]

        # Path 2: direct construction
        H = HeisenbergFock(Psi, N_max)
        d = H.dim
        alpha_cop = (Psi - 1.0) / Psi

        M = N_max + 2
        X0 = np.zeros((d * d, d * d))
        for k in range(-M, M + 1):
            X0 += np.kron(H.J(k), H.J(-k))
        O3 = 2.0 * alpha_cop * X0

        # Build physical Gram matrix
        from collections import Counter
        G_diag = np.zeros(d)
        for i, lam in enumerate(H.partitions):
            if not lam:
                G_diag[i] = 1.0
            else:
                cnt = Counter(lam)
                val = 1.0
                for part, ni in cnt.items():
                    val *= (Psi * part) ** ni
                    f = 1
                    for kk in range(2, ni + 1):
                        f *= kk
                    val *= f
                G_diag[i] = val
        G_tensor = np.kron(np.diag(G_diag), np.diag(G_diag))

        vac_idx = H.idx[()]
        j1_idx = H.idx[(1,)]

        ket = np.zeros(d * d)
        ket[j1_idx * d + vac_idx] = 1.0
        bra = np.zeros(d * d)
        bra[vac_idx * d + j1_idx] = 1.0

        me_phys = float(bra @ G_tensor @ O3 @ ket)
        delta3_direct = me_phys / Psi  # normalize by physical norm of |(1,)>

        assert abs(delta3_engine - delta3_direct) < 1e-10
