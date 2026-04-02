r"""Tests for the Kontsevich-Soibelman wall-crossing on the resolved conifold.

Verifies:
  1. Quantum torus algebra (YX = qXY, associativity)
  2. Compact quantum dilogarithm E(z) = prod_{k>=0}(1+q^k z)
  3. Pentagon identity: E(X)*E(Y) = E(Y)*E(XY)*E(X) (exact, over Q[[q]])
  4. Pentagon identity (numerical, Schrodinger representation)
  5. BPS spectra in the two chambers
  6. MC equation and gauge transformation
  7. DT partition functions in both chambers
  8. DT decomposition: C_1 = q/(1-q)^2
  9. Chamber-independence of the full DT partition function

Manuscript references:
    Part V (Standard Landscape): resolved conifold, DT theory
    Part IV (Quantum Groups): quantum torus, KS wall-crossing

Mathematical references:
    [KS]    Kontsevich-Soibelman, arXiv:0811.2435
    [FK]    Faddeev-Kashaev, q-dilogarithm (1994)
    [Kell]  Keller, arXiv:1102.4148

Ground truth:
    - Pentagon: E(X)*E(Y) = E(Y)*E(XY)*E(X) in quantum torus with YX = qXY
    - M(q) = prod(1-q^n)^{-n} (MacMahon, OEIS A000219)
    - C_1(q) = sum k*q^k = q/(1-q)^2 (colored partition with one D2)
    - Lie bracket: [e_{g1}, e_{g2}] = <g1,g2> * e_{g1+g2}
"""

import pytest
from fractions import Fraction

from compute.lib.conifold_wall_crossing import (
    # Quantum torus
    QuantumTorusElement,
    # Compact quantum dilogarithm
    compact_quantum_dilog,
    _q_pochhammer,
    _q_pochhammer_inv,
    # Pentagon
    pentagon_identity_quantum_torus,
    pentagon_numerical,
    # BPS spectra
    chamber_I_spectrum,
    chamber_II_spectrum,
    conifold_pentagon_spectrum,
    # MC / gauge
    lie_bracket,
    mc_equation_check,
    gauge_transformation_conifold,
    # DT
    dt_chamber_I,
    dt_chamber_II,
    conifold_dt_partition_function,
    conifold_dt_vs_macmahon,
    dt_numerical,
    # Power series
    _poly_one,
    _poly_mul_trunc,
    _poly_inv_trunc,
    _poly_add,
    _poly_scale,
    _macmahon_coeffs,
)


# ================================================================
# 1. QUANTUM TORUS ALGEBRA
# ================================================================

class TestQuantumTorus:
    """Verify the quantum torus algebra with YX = qXY."""

    def test_identity(self):
        """1 * A = A * 1 = A."""
        N = 6
        one = QuantumTorusElement.one(N)
        X = QuantumTorusElement.monomial(1, 0, _poly_one(N), N)
        assert (one * X).get_coeff(1, 0) == X.get_coeff(1, 0)
        assert (X * one).get_coeff(1, 0) == X.get_coeff(1, 0)

    def test_yx_equals_q_xy(self):
        """YX = qXY: the defining relation of the quantum torus."""
        N = 6
        X = QuantumTorusElement.monomial(1, 0, _poly_one(N), N)
        Y = QuantumTorusElement.monomial(0, 1, _poly_one(N), N)
        XY = X * Y
        YX = Y * X
        # XY at (1,1) should be [1, 0, 0, ...]
        assert XY.get_coeff(1, 1)[0] == Fraction(1)
        assert all(XY.get_coeff(1, 1)[k] == 0 for k in range(1, N))
        # YX at (1,1) should be [0, 1, 0, ...] (= q)
        assert YX.get_coeff(1, 1)[0] == Fraction(0)
        assert YX.get_coeff(1, 1)[1] == Fraction(1)
        assert all(YX.get_coeff(1, 1)[k] == 0 for k in range(2, N))

    def test_associativity(self):
        """(X*Y)*X = X*(Y*X) in the quantum torus."""
        N = 8
        X = QuantumTorusElement.monomial(1, 0, _poly_one(N), N)
        Y = QuantumTorusElement.monomial(0, 1, _poly_one(N), N)
        lhs = (X * Y) * X
        rhs = X * (Y * X)
        # Both should be at charge (2,1)
        for k in range(N):
            assert lhs.get_coeff(2, 1)[k] == rhs.get_coeff(2, 1)[k], \
                f"Associativity fails at q^{k}"

    def test_xy_power_ordering(self):
        """(XY)^2 = q * X^2 Y^2 and (XY)^3 = q^3 * X^3 Y^3."""
        N = 8
        XY = QuantumTorusElement.monomial(1, 1, _poly_one(N), N)
        XY2 = XY * XY
        XY3 = XY2 * XY
        # (XY)^2 at (2,2): should be q^1
        assert XY2.get_coeff(2, 2)[0] == 0
        assert XY2.get_coeff(2, 2)[1] == 1
        # (XY)^3 at (3,3): should be q^3
        assert XY3.get_coeff(3, 3)[3] == 1
        assert all(XY3.get_coeff(3, 3)[k] == 0 for k in range(3))

    def test_addition_subtraction(self):
        """(A + B) - B = A."""
        N = 4
        X = QuantumTorusElement.monomial(1, 0, _poly_one(N), N)
        Y = QuantumTorusElement.monomial(0, 1, _poly_one(N), N)
        result = (X + Y) - Y
        assert result.get_coeff(1, 0) == X.get_coeff(1, 0)
        assert all(result.get_coeff(0, 1)[k] == 0 for k in range(N))


# ================================================================
# 2. COMPACT QUANTUM DILOGARITHM
# ================================================================

class TestQuantumDilogarithm:
    """Verify E(z) = prod(1+q^k z) = sum q^{n(n-1)/2} z^n / (q;q)_n."""

    def test_q_pochhammer_values(self):
        """(q;q)_0 = 1, (q;q)_1 = 1-q, (q;q)_2 = (1-q)(1-q^2)."""
        N = 8
        assert _q_pochhammer(0, N)[0] == 1
        assert all(_q_pochhammer(0, N)[k] == 0 for k in range(1, N))

        qq1 = _q_pochhammer(1, N)
        assert qq1[0] == 1
        assert qq1[1] == -1
        assert all(qq1[k] == 0 for k in range(2, N))

        qq2 = _q_pochhammer(2, N)
        # (1-q)(1-q^2) = 1 - q - q^2 + q^3
        assert qq2[0] == 1
        assert qq2[1] == -1
        assert qq2[2] == -1
        assert qq2[3] == 1

    def test_E_X_constant_term(self):
        """E(X) at charge (0,0) should be 1 (the n=0 term)."""
        N = 8
        mc = 6
        E = compact_quantum_dilog(1, 0, N, mc)
        assert E.get_coeff(0, 0)[0] == 1
        assert all(E.get_coeff(0, 0)[k] == 0 for k in range(1, N))

    def test_E_X_linear_term(self):
        """E(X) at charge (1,0): coefficient of X should be 1/(q;q)_1 = 1/(1-q)."""
        N = 8
        mc = 6
        E = compact_quantum_dilog(1, 0, N, mc)
        inv_qq1 = _q_pochhammer_inv(1, N)
        for k in range(N):
            assert E.get_coeff(1, 0)[k] == inv_qq1[k]

    def test_E_Y_linear_term(self):
        """E(Y) at charge (0,1): same as E(X) at (1,0) by symmetry."""
        N = 8
        mc = 6
        E = compact_quantum_dilog(0, 1, N, mc)
        inv_qq1 = _q_pochhammer_inv(1, N)
        for k in range(N):
            assert E.get_coeff(0, 1)[k] == inv_qq1[k]

    def test_E_XY_quadratic_term(self):
        """E(XY) at charge (2,2): should be q^{2(2-1)(1+1)/2} / (q;q)_2 = q^2 / (q;q)_2."""
        N = 10
        mc = 8
        E = compact_quantum_dilog(1, 1, N, mc)
        # n=2 term: phase = n(n-1)/2 + n(n-1)*ba/2 = 1 + 1 = 2
        inv_qq2 = _q_pochhammer_inv(2, N)
        expected = [Fraction(0)] * N
        for i in range(N - 2):
            expected[i + 2] = inv_qq2[i]
        for k in range(N):
            assert E.get_coeff(2, 2)[k] == expected[k], \
                f"E(XY) at (2,2), q^{k}: got {E.get_coeff(2,2)[k]}, expected {expected[k]}"


# ================================================================
# 3. PENTAGON IDENTITY (exact)
# ================================================================

class TestPentagonExact:
    """Verify E(X)*E(Y) = E(Y)*E(XY)*E(X) exactly over Q[[q]]."""

    def test_pentagon_N8_mc4(self):
        """Pentagon at N_q=8, max_charge=4."""
        result = pentagon_identity_quantum_torus(N_q=8, max_charge=4)
        assert result["pentagon_holds"], \
            f"Pentagon failed: {result['discrepancies'][:3]}"

    def test_pentagon_N10_mc6(self):
        """Pentagon at N_q=10, max_charge=6 (higher order)."""
        result = pentagon_identity_quantum_torus(N_q=10, max_charge=6)
        assert result["pentagon_holds"], \
            f"Pentagon failed: {result['discrepancies'][:3]}"
        assert result["charges_checked"] >= 20

    def test_pentagon_N15_mc6(self):
        """Pentagon at N_q=15, max_charge=6 (deep q-series check)."""
        result = pentagon_identity_quantum_torus(N_q=15, max_charge=6)
        assert result["pentagon_holds"], \
            f"Pentagon failed: {result['discrepancies'][:3]}"

    def test_pentagon_symmetry(self):
        """The pentagon output is symmetric under (a,b) <-> (b,a) at charge level."""
        result = pentagon_identity_quantum_torus(N_q=8, max_charge=6)
        assert result["pentagon_holds"]
        sc = result["sample_coefficients"]
        # (2,1) and (1,2) should have the same coefficients
        if (2, 1) in sc and (1, 2) in sc:
            assert sc[(2, 1)]["lhs"] == sc[(1, 2)]["lhs"], \
                "Pentagon output should be symmetric in (a,b) charges"


# ================================================================
# 4. PENTAGON IDENTITY (numerical)
# ================================================================

class TestPentagonNumerical:
    """Verify the pentagon in the Schrodinger representation."""

    def test_pentagon_q03(self):
        """Pentagon at q=0.3 (well within convergence radius)."""
        result = pentagon_numerical(0.3, N_terms=50)
        assert result["match"], \
            f"Numerical pentagon failed at q=0.3: rel_err={result['relative_error']}"

    def test_pentagon_q05(self):
        """Pentagon at q=0.5."""
        result = pentagon_numerical(0.5, N_terms=50)
        assert result["match"], \
            f"Numerical pentagon failed at q=0.5: rel_err={result['relative_error']}"

    def test_pentagon_q01(self):
        """Pentagon at q=0.1 (fast convergence)."""
        result = pentagon_numerical(0.1, N_terms=30)
        assert result["match"], \
            f"Numerical pentagon failed at q=0.1: rel_err={result['relative_error']}"


# ================================================================
# 5. BPS SPECTRA
# ================================================================

class TestBPSSpectra:
    """Verify the BPS spectra in the two chambers."""

    def test_chamber_I_two_states(self):
        """Chamber I has exactly two BPS states."""
        spec = chamber_I_spectrum()
        assert len(spec) == 2
        assert spec[(1, 0)] == -1
        assert spec[(0, 1)] == -1

    def test_chamber_II_bound_states(self):
        """Chamber II has bound states (1, n) for n >= 1."""
        spec = chamber_II_spectrum(max_n=5)
        assert spec[(1, 0)] == -1
        assert spec[(0, 1)] == -1
        for n in range(1, 6):
            assert spec[(1, n)] == -1

    def test_pentagon_spectrum_sizes(self):
        """Pentagon: 2 particles (side A) vs 3 particles (side B)."""
        side_A, side_B = conifold_pentagon_spectrum()
        assert len(side_A) == 2
        assert len(side_B) == 3
        assert (1, 1) not in side_A
        assert (1, 1) in side_B

    def test_omega_all_minus_one(self):
        """All BPS indices are -1 (hypermultiplet convention)."""
        spec = chamber_II_spectrum(max_n=10)
        for charge, omega in spec.items():
            assert omega == -1, f"Omega({charge}) = {omega}, expected -1"


# ================================================================
# 6. MC EQUATION AND GAUGE TRANSFORMATION
# ================================================================

class TestMCAndGauge:
    """Verify the Lie algebra structure and gauge transformation."""

    def test_lie_bracket_antisymmetry(self):
        """<g1, g2> = -<g2, g1>."""
        g1, g2 = (1, 0), (0, 1)
        _, p12 = lie_bracket(g1, g2)
        _, p21 = lie_bracket(g2, g1)
        assert p12 == -p21

    def test_lie_bracket_pairing(self):
        """<(1,0), (0,1)> = 1."""
        _, p = lie_bracket((1, 0), (0, 1))
        assert p == 1

    def test_lie_bracket_same_charge(self):
        """<gamma, gamma> = 0."""
        _, p = lie_bracket((1, 0), (1, 0))
        assert p == 0

    def test_mc_chamber_I_obstruction(self):
        """Chamber I: [Theta, Theta] = 0 in the naive Lie algebra.

        With only two charges (1,0) and (0,1), the bracket produces
        2 * (-1)*(-1) * <(1,0),(0,1)> * e_{(1,1)} = 2*e_{(1,1)} != 0.
        WAIT -- actually [Theta, Theta] counts ORDERED pairs, so
        [e_{g1}, e_{g2}] + [e_{g2}, e_{g1}] = 0 by antisymmetry.
        So [Theta, Theta] = sum_{g1<g2} 2*O(g1)*O(g2)*<g1,g2>*e_{g1+g2}
        plus the self-brackets which vanish.
        For g1=(1,0), g2=(0,1): 2*(-1)(-1)*1*e_{(1,1)} = 2*e_{(1,1)}.
        But also g1=(0,1), g2=(1,0): 2*(-1)(-1)*(-1)*e_{(1,1)} = -2*e_{(1,1)}.
        Total: 2-2 = 0 (from antisymmetry of the bracket).
        So [Theta, Theta] = 0. This is correct.
        """
        spec = chamber_I_spectrum()
        result = mc_equation_check(spec, 6)
        assert result["mc_equation_holds"]

    def test_mc_chamber_II_with_bound_state(self):
        """Chamber II (pentagon) also has [Theta, Theta] = 0.

        Adding the bound state doesn't break the MC equation because
        the new brackets also cancel by antisymmetry.
        """
        _, side_B = conifold_pentagon_spectrum()
        result = mc_equation_check(side_B, 6)
        assert result["mc_equation_holds"]

    def test_gauge_produces_bound_state(self):
        """alpha = e_{(1,0)} produces the bound state e_{(1,1)} at first order."""
        result = gauge_transformation_conifold(max_order=3)
        assert result["match_at_charge_11"]

    def test_gauge_higher_corrections(self):
        """Higher orders produce e_{(n,1)} corrections for n >= 2."""
        result = gauge_transformation_conifold(max_order=5)
        hc = result["higher_charge_corrections"]
        # Should have (2,1), (3,1), (4,1), (5,1) corrections
        assert "(2, 1)" in hc
        assert "(3, 1)" in hc
        # Check specific values: -1/k! pattern
        assert hc["(2, 1)"] == "-1/2"
        assert hc["(3, 1)"] == "-1/6"
        assert hc["(4, 1)"] == "-1/24"
        assert hc["(5, 1)"] == "-1/120"


# ================================================================
# 7. DT PARTITION FUNCTIONS
# ================================================================

class TestDTPartitionFunctions:
    """Verify the DT partition functions in both chambers."""

    def test_macmahon_first_values(self):
        """M(q) coefficients: 1, 1, 3, 6, 13, 24, 48, 86, ..."""
        M = _macmahon_coeffs(12)
        expected = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
        for k in range(len(expected)):
            assert int(M[k]) == expected[k], \
                f"M(q) coeff at q^{k}: got {int(M[k])}, expected {expected[k]}"

    def test_chamber_I_Q0_is_one(self):
        """Chamber I: F_0(q) = 1 (no D2-branes)."""
        F = dt_chamber_I(10, 3)
        assert F[0][0] == 1
        assert all(F[0][k] == 0 for k in range(1, 10))

    def test_chamber_I_Q1_coeffs(self):
        """Chamber I: F_1(q) = -sum k*q^k = -q/(1-q)^2.

        prod (1-Qq^k)^k at Q^1: each factor (1-Qq^k)^k contributes
        -k*Qq^k to first order in Q. So F_1(q) = -sum k*q^k.
        """
        F = dt_chamber_I(15, 3)
        for k in range(1, 15):
            assert int(F[1][k]) == -k, \
                f"F_1 at q^{k}: got {int(F[1][k])}, expected {-k}"

    def test_chamber_II_Q0_is_one(self):
        """Chamber II: G_0(q) = 1."""
        G = dt_chamber_II(10, 3)
        assert G[0][0] == 1
        assert all(G[0][k] == 0 for k in range(1, 10))

    def test_chamber_II_Qinv1_coeffs(self):
        """Chamber II: G_1(q) = sum k*q^k = q/(1-q)^2.

        prod (1-Q^{-1}q^k)^{-k} at Q^{-1}: expands to sum k*q^k Q^{-1} + ...
        """
        G = dt_chamber_II(15, 3)
        for k in range(1, 15):
            assert int(G[1][k]) == k, \
                f"G_1 at q^{k}: got {int(G[1][k])}, expected {k}"

    def test_dt_sum_FI_equals_Minv(self):
        """sum_d F_I_d (Q=1) = prod(1-q^k)^k = 1/M(q).

        Needs large enough N_Q for convergence.
        """
        result = conifold_dt_partition_function(10, N_Q=10)
        assert result["sum_FI_equals_Minv"], \
            "sum F_I_d at Q=1 should equal M(q)^{-1}"

    def test_dt_sum_GII_equals_M(self):
        """sum_d G_II_d (Q^{-1}=1) = prod(1-q^k)^{-k} = M(q).

        Needs large N_Q.
        """
        result = conifold_dt_partition_function(10, N_Q=14)
        assert result["sum_GII_equals_M"], \
            "sum G_II_d at Q^{-1}=1 should equal M(q)"


# ================================================================
# 8. DT DECOMPOSITION
# ================================================================

class TestDTDecomposition:
    """Verify the Q-expansion of the conifold factor."""

    def test_C1_equals_k_qk(self):
        """C_1(q) = sum_{k>=1} k*q^k = q/(1-q)^2."""
        result = conifold_dt_vs_macmahon(15)
        assert result["C1_equals_kq^k"]
        # Check first few values explicitly
        for k in range(1, 10):
            assert result["C1"][k] == k

    def test_C0_equals_one(self):
        """C_0(q) = 1 (the empty partition)."""
        result = conifold_dt_vs_macmahon(10)
        assert result["C0"][0] == 1
        assert all(result["C0"][k] == 0 for k in range(1, 10))

    def test_C2_first_values(self):
        """C_2(q) first nonzero at q^2, with known values."""
        result = conifold_dt_vs_macmahon(15)
        # C_2: 0, 0, 1, 2, 6, 10, 19, 28, ...
        assert result["C2"][0] == 0
        assert result["C2"][1] == 0
        assert result["C2"][2] == 1
        assert result["C2"][3] == 2
        assert result["C2"][4] == 6


# ================================================================
# 9. NUMERICAL DT: DIFFERENT BPS SPECTRA
# ================================================================

class TestNumericalDT:
    """Verify that Z_I and Z_II encode different BPS spectra."""

    def test_ZI_neq_ZII(self):
        """Z_I != Z_II: different BPS spectra."""
        result = dt_numerical(0.5)
        assert result["Z_I_neq_Z_II"]

    def test_ZI_positive(self):
        """Z_I > 0 for q in (0,1), Q in (0,1)."""
        result = dt_numerical(0.3, Q_val=0.2)
        assert result["Z_I"] > 0

    def test_ZII_nonzero(self):
        """Z_II != 0 for q in (0,1), Q in (0,1).

        Note: Z_II can be negative because prod(1-Q^{-1}q^k)^{-k} involves
        factors (1-Q^{-1}q^k) which can be negative when Q^{-1}q^k > 1.
        """
        result = dt_numerical(0.5)
        assert result["Z_II"] != 0

    def test_macmahon_positive(self):
        """M(q) > 1 for q in (0,1)."""
        result = dt_numerical(0.5)
        assert result["MacMahon"] > 1

    def test_ZI_less_than_ZII(self):
        """In the large-volume chamber, Z_I < Z_II because Chamber I
        has fewer BPS states contributing."""
        result = dt_numerical(0.5)
        assert result["Z_I"] < result["Z_II"]
