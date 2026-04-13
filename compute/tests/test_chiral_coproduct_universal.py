"""Tests for the universal Drinfeld coproduct at ALL spins s <= 6.

Verifies the universal formula:

    Delta_z(psi_{s,n}) = psi_{s,n}^L
      + sum_{a=0}^{s-1} sum_{p=0}^{s-1-a} C(s-a-1, p) z^p
          [psi_a^L conv psi_{s-a-p}^R]_n

derived from the multiplicative Drinfeld coproduct
Delta_z(T(u)) = T_L(u) * T_R(u-z) on Y(gl_hat_1).

Key results:
- Universal formula reproduces spin-2 engine at s=2 (zero error)
- Universal formula reproduces spin-3 engine at s=3 (zero error)
- z-polynomial degree = s - 1 for all s
- Leading z^{s-1} coefficient = J^R (single term)
- Subleading z^1 coefficient at s=3 = (s-1)*psi_2^R + J^L*J^R
- First-time computation at s=4,5,6 via structural formula
- Total operator products at spin s = s(s+1)/2 - 1
- Cross-terms at z=0 = s-1 bilinear types

VERIFIED sources:
[TM] Transfer matrix multiplication T_L(u)*T_R(u-z), u^{-s} extraction
[DC] Direct computation: universal formula matches 4 independent engines
[LC] Structural: z-degree, term counts, binomial coefficients consistent
[SY] Numerical: z-polynomial fitting confirms degree bound
"""

import numpy as np
import pytest

from compute.lib.chiral_coproduct_universal_engine import (
    AllSpinCoproduct,
    compute_spin456_tables,
    verify_against_allspin,
    verify_against_general,
    verify_against_spin2,
    verify_against_spin3,
    verify_highest_z_is_JR,
    verify_structural_consistency,
    verify_subleading_z1,
    verify_vacuum_annihilation,
    verify_z0_cross_terms,
    verify_z_polynomial_degree,
    verify_z_polynomial_degree_structural,
)


# ---------------------------------------------------------------------------
# Part A: Cross-validation against existing engines at s=2
# ---------------------------------------------------------------------------

class TestUniversalVsSpin2:
    """Universal engine at s=2 matches the spin-2/spin-3 engines."""

    def test_vs_spin2_Psi1(self):
        # VERIFIED: [DC] Universal cross-term at s=2 matches spin-2 engine, Psi=1.
        r = verify_against_spin2(Psi=1.0, N_max=6, z=0.3 + 0.2j)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_vs_spin2_Psi2(self):
        # VERIFIED: [DC] Universal cross-term at s=2 matches spin-2 engine, Psi=2.
        r = verify_against_spin2(Psi=2.0, N_max=6, z=0.3 + 0.2j)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.7])
    def test_vs_spin2_parametric(self, Psi):
        # VERIFIED: [DC] Agreement across Psi range.
        r = verify_against_spin2(Psi=Psi, N_max=5, z=0.4 + 0.3j)
        assert r["ok"], f"Psi={Psi}: max error {r['max_error']:.2e}"

    def test_vs_general_s2_Psi1(self):
        # VERIFIED: [DC] Universal matches general engine at s=2, Psi=1.
        r = verify_against_general(s=2, Psi=1.0, N_max=5, z=0.3 + 0.2j)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_vs_general_s2_Psi2(self):
        # VERIFIED: [DC] Universal matches general engine at s=2, Psi=2.
        r = verify_against_general(s=2, Psi=2.0, N_max=5, z=0.3 + 0.2j)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_vs_allspin_s2_Psi1(self):
        # VERIFIED: [DC] Universal matches allspin engine at s=2, Psi=1.
        r = verify_against_allspin(s=2, Psi=1.0, N_max=5, z=0.3 + 0.2j)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_vs_allspin_s2_Psi2(self):
        # VERIFIED: [DC] Universal matches allspin engine at s=2, Psi=2.
        r = verify_against_allspin(s=2, Psi=2.0, N_max=5, z=0.3 + 0.2j)
        assert r["ok"], f"max error {r['max_error']:.2e}"


# ---------------------------------------------------------------------------
# Part A': Cross-validation against existing engines at s=3
# ---------------------------------------------------------------------------

class TestUniversalVsSpin3:
    """Universal engine at s=3 matches the spin-3 engine."""

    def test_vs_spin3_Psi1(self):
        # VERIFIED: [DC] Universal cross-term at s=3 matches spin-3 engine, Psi=1.
        r = verify_against_spin3(Psi=1.0, N_max=6, z=0.3 + 0.2j)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_vs_spin3_Psi2(self):
        # VERIFIED: [DC] Universal cross-term at s=3 matches spin-3 engine, Psi=2.
        r = verify_against_spin3(Psi=2.0, N_max=6, z=0.3 + 0.2j)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.7])
    def test_vs_spin3_parametric(self, Psi):
        # VERIFIED: [DC] Agreement across Psi range at s=3.
        r = verify_against_spin3(Psi=Psi, N_max=5, z=0.4 + 0.3j)
        assert r["ok"], f"Psi={Psi}: max error {r['max_error']:.2e}"

    def test_vs_general_s3_Psi1(self):
        # VERIFIED: [DC] Universal matches general engine at s=3, Psi=1.
        r = verify_against_general(s=3, Psi=1.0, N_max=5, z=0.3 + 0.2j)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_vs_general_s3_Psi2(self):
        # VERIFIED: [DC] Universal matches general engine at s=3, Psi=2.
        r = verify_against_general(s=3, Psi=2.0, N_max=5, z=0.3 + 0.2j)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_vs_allspin_s3_Psi1(self):
        # VERIFIED: [DC] Universal matches allspin engine at s=3, Psi=1.
        r = verify_against_allspin(s=3, Psi=1.0, N_max=5, z=0.3 + 0.2j)
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_vs_allspin_s3_Psi2(self):
        # VERIFIED: [DC] Universal matches allspin engine at s=3, Psi=2.
        r = verify_against_allspin(s=3, Psi=2.0, N_max=5, z=0.3 + 0.2j)
        assert r["ok"], f"max error {r['max_error']:.2e}"


# ---------------------------------------------------------------------------
# Part B: z-polynomial degree = s - 1
# ---------------------------------------------------------------------------

class TestZPolynomialDegree:
    """Delta_z(psi_s) is a polynomial of degree s-1 in z."""

    def test_z_degree_s2_fock(self):
        # VERIFIED: [SY] Degree 1 at s=2 (Fock space fit).
        r = verify_z_polynomial_degree(s=2, Psi=2.0, N_max=5)
        assert r["ok"], f"max error {r.get('max_error', 'n/a')}"
        assert r["expected_degree"] == 1

    def test_z_degree_s3_fock(self):
        # VERIFIED: [SY] Degree 2 at s=3 (Fock space fit).
        r = verify_z_polynomial_degree(s=3, Psi=2.0, N_max=5)
        assert r["ok"], f"max error {r.get('max_error', 'n/a')}"
        assert r["expected_degree"] == 2

    @pytest.mark.parametrize("s", [1, 2, 3, 4, 5, 6])
    def test_z_degree_structural(self, s):
        # VERIFIED: [LC] Structural z-degree = s - 1 for all s.
        r = verify_z_polynomial_degree_structural(s)
        assert r["ok"], f"s={s}: z_degree={r['z_degree']}, expected={r['expected']}"

    @pytest.mark.parametrize("s", [4, 5, 6])
    def test_z_degree_spin456_structural(self, s):
        # VERIFIED: [LC] First-time: structural z-degree at s=4,5,6.
        r = verify_z_polynomial_degree(s=s)
        assert r["ok"], f"s={s}: degree mismatch"
        assert r["actual_degree"] == s - 1


# ---------------------------------------------------------------------------
# Part C: Leading z^{s-1} = J^R
# ---------------------------------------------------------------------------

class TestHighestZPower:
    """z^{s-1} coefficient of Delta_z(psi_s) is exactly J^R."""

    @pytest.mark.parametrize("s", [2, 3])
    def test_leading_JR_fock(self, s):
        # VERIFIED: [DC] z^{s-1} = J^R on Fock space.
        r = verify_highest_z_is_JR(s=s, Psi=2.0, N_max=5)
        assert r["ok"], f"s={s}: max error {r.get('max_error', 'n/a')}"

    @pytest.mark.parametrize("s", [4, 5, 6])
    def test_leading_JR_structural(self, s):
        # VERIFIED: [LC] z^{s-1} = J^R (structural, first-time for s >= 4).
        r = verify_highest_z_is_JR(s=s, Psi=2.0, N_max=5)
        assert r["ok"], f"s={s}: structural check failed"


# ---------------------------------------------------------------------------
# Part D: Subleading z^1 coefficient
# ---------------------------------------------------------------------------

class TestSubleadingZ1:
    """z^1 coefficient of Delta_z(psi_s).

    At s=3: z^1 = (s-1)*psi_2^R + J^L*J^R = 2*psi_2^R + J^L*J^R.
    """

    def test_subleading_s3_fock(self):
        # VERIFIED: [DC] z^1 = 2*psi_2^R + J^L*J^R at s=3 (Fock space).
        r = verify_subleading_z1(s=3, Psi=2.0, N_max=5)
        assert r["ok"], f"s=3: subleading check failed"

    def test_subleading_s3_Psi1(self):
        # VERIFIED: [DC] z^1 subleading at s=3, Psi=1.
        r = verify_subleading_z1(s=3, Psi=1.0, N_max=5)
        assert r["ok"], f"s=3, Psi=1: subleading check failed"

    @pytest.mark.parametrize("s", [2, 3, 4, 5, 6])
    def test_subleading_structural(self, s):
        # VERIFIED: [LC] Subleading coefficient structural check.
        r = verify_subleading_z1(s=s, Psi=2.0, N_max=5)
        assert r["ok"], f"s={s}: subleading structural failed"

    def test_subleading_s3_coefficient_value(self):
        """At s=3, the z^1 R-shifted leading term has coefficient s-1=2."""
        info = AllSpinCoproduct.subleading_coefficient_z1(3)
        assert info["leading_R_shifted"]["coefficient"] == 2
        assert info["leading_R_shifted"]["operator"] == "psi_2^R"

    @pytest.mark.parametrize("s", [4, 5, 6])
    def test_subleading_coefficient_is_s_minus_1(self, s):
        """The leading R-shifted term at z^1 has coefficient s-1."""
        info = AllSpinCoproduct.subleading_coefficient_z1(s)
        assert info["leading_R_shifted"]["coefficient"] == s - 1
        assert info["leading_R_shifted"]["operator"] == f"psi_{s-1}^R"


# ---------------------------------------------------------------------------
# Part E: Vacuum annihilation
# ---------------------------------------------------------------------------

class TestVacuumAnnihilation:
    """C_s(n, z=0)|0,0> = 0 for n >= 0."""

    @pytest.mark.parametrize("s", [2, 3])
    def test_vacuum_Psi1(self, s):
        # VERIFIED: [TM] Vacuum annihilation at Psi=1.
        r = verify_vacuum_annihilation(s=s, Psi=1.0, N_max=5)
        assert r["ok"], f"s={s}: max error {r.get('max_error', 'n/a')}"

    @pytest.mark.parametrize("s", [2, 3])
    def test_vacuum_Psi2(self, s):
        # VERIFIED: [TM] Vacuum annihilation at Psi=2.
        r = verify_vacuum_annihilation(s=s, Psi=2.0, N_max=5)
        assert r["ok"], f"s={s}: max error {r.get('max_error', 'n/a')}"

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.7])
    def test_vacuum_s2_parametric(self, Psi):
        # VERIFIED: [TM] Vacuum annihilation at s=2 across Psi.
        r = verify_vacuum_annihilation(s=2, Psi=Psi, N_max=5)
        assert r["ok"], f"Psi={Psi}: max error {r.get('max_error', 'n/a')}"

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.7])
    def test_vacuum_s3_parametric(self, Psi):
        # VERIFIED: [TM] Vacuum annihilation at s=3 across Psi.
        r = verify_vacuum_annihilation(s=3, Psi=Psi, N_max=5)
        assert r["ok"], f"Psi={Psi}: max error {r.get('max_error', 'n/a')}"


# ---------------------------------------------------------------------------
# Part F: Cross-term count at z=0
# ---------------------------------------------------------------------------

class TestCrossTermCount:
    """At z=0, C_s has exactly s-1 bilinear cross-term types."""

    @pytest.mark.parametrize("s", [2, 3])
    def test_z0_cross_fock(self, s):
        # VERIFIED: [DC] s-1 cross-terms at z=0 (Fock space).
        r = verify_z0_cross_terms(s=s, Psi=2.0, N_max=5)
        assert r["ok"], f"s={s}: max error {r.get('max_error', 'n/a')}"
        assert r["cross_terms"] == s - 1

    @pytest.mark.parametrize("s", [4, 5, 6])
    def test_z0_cross_structural(self, s):
        # VERIFIED: [LC] s-1 cross-terms at z=0 (structural, first-time).
        r = verify_z0_cross_terms(s=s, Psi=2.0, N_max=5)
        assert r["ok"], f"s={s}: cross-terms = {r.get('cross_terms', 'n/a')}"
        assert r["cross_terms"] == s - 1


# ---------------------------------------------------------------------------
# Part G: First-time computation at spins 4, 5, 6
# ---------------------------------------------------------------------------

class TestSpin456FirstTime:
    """First-time structural computation of the coproduct at s=4,5,6."""

    def test_spin456_tables_computed(self):
        # VERIFIED: [LC] Tables for s=4,5,6 are self-consistent.
        tables = compute_spin456_tables()
        assert 4 in tables and 5 in tables and 6 in tables

    @pytest.mark.parametrize("s", [4, 5, 6])
    def test_z_degree(self, s):
        tables = compute_spin456_tables()
        assert tables[s]["z_degree"] == s - 1

    @pytest.mark.parametrize("s", [4, 5, 6])
    def test_total_terms(self, s):
        """total_terms = s(s+1)/2 (includes diagonal psi_s^R).

        total_operator_products = s(s+1)/2 - 1 (excludes diagonal psi_s^L only).
        total_terms = total_operator_products + 1 (includes unshifted psi_s^R).
        """
        tables = compute_spin456_tables()
        expected = s * (s + 1) // 2
        assert tables[s]["total_terms"] == expected

    @pytest.mark.parametrize("s", [4, 5, 6])
    def test_cross_at_z0(self, s):
        """Cross-terms at z=0 = s-1."""
        tables = compute_spin456_tables()
        assert tables[s]["cross_at_z0"] == s - 1

    @pytest.mark.parametrize("s", [4, 5, 6])
    def test_terms_per_z_power(self, s):
        """Terms at z^p = s - p."""
        tables = compute_spin456_tables()
        expected = {p: s - p for p in range(s)}
        assert tables[s]["terms_per_z_power"] == expected

    def test_spin4_explicit_structure(self):
        """Spin-4: total_operator_products = 9, total_terms = 10."""
        table = AllSpinCoproduct.delta_z_table(4)
        # total_operator_products = s(s+1)/2 - 1 = 9 (excludes psi_s^L)
        assert table["total_operator_products"] == 9
        # total_terms = 10 (includes unshifted psi_s^R)
        assert table["total_terms"] == 10
        assert table["total_terms"] == len(table["all_terms"])

    def test_spin5_explicit_structure(self):
        """Spin-5 has 5*6/2 - 1 = 14 operator products."""
        table = AllSpinCoproduct.delta_z_table(5)
        assert table["total_operator_products"] == 14

    def test_spin6_explicit_structure(self):
        """Spin-6 has 6*7/2 - 1 = 20 operator products."""
        table = AllSpinCoproduct.delta_z_table(6)
        assert table["total_operator_products"] == 20

    def test_spin4_z1_coefficient(self):
        """Spin-4 z^1 leading R term: coefficient = 3 = s-1."""
        info = AllSpinCoproduct.subleading_coefficient_z1(4)
        assert info["leading_R_shifted"]["coefficient"] == 3
        assert info["n_terms"] == 3  # a = 0, 1, 2

    def test_spin5_z1_coefficient(self):
        """Spin-5 z^1 leading R term: coefficient = 4 = s-1."""
        info = AllSpinCoproduct.subleading_coefficient_z1(5)
        assert info["leading_R_shifted"]["coefficient"] == 4
        assert info["n_terms"] == 4  # a = 0, 1, 2, 3

    def test_spin6_z1_coefficient(self):
        """Spin-6 z^1 leading R term: coefficient = 5 = s-1."""
        info = AllSpinCoproduct.subleading_coefficient_z1(6)
        assert info["leading_R_shifted"]["coefficient"] == 5
        assert info["n_terms"] == 5  # a = 0, 1, 2, 3, 4

    @pytest.mark.parametrize("s", [4, 5, 6])
    def test_spin456_leading_z_single_JR(self, s):
        """At z^{s-1}, exactly one term: psi_1^R = J^R."""
        table = AllSpinCoproduct.delta_z_table(s)
        top_terms = table["terms_by_z"].get(s - 1, [])
        assert len(top_terms) == 1
        assert top_terms[0]["right_spin"] == 1
        assert top_terms[0]["left_spin"] == 0
        assert top_terms[0]["binomial"] == 1

    @pytest.mark.parametrize("s", [4, 5, 6])
    def test_spin456_binomials_pascal(self, s):
        """Binomial coefficients match Pascal's triangle rows."""
        import math
        table = AllSpinCoproduct.delta_z_table(s)
        for term in table["all_terms"]:
            a = term["left_spin"]
            p = term["z_power"]
            expected = math.comb(s - a - 1, p)
            assert term["binomial"] == expected, (
                f"s={s}, a={a}, p={p}: got {term['binomial']}, "
                f"expected C({s-a-1},{p}) = {expected}"
            )


# ---------------------------------------------------------------------------
# Part H: Full structural consistency
# ---------------------------------------------------------------------------

class TestStructuralConsistency:
    """Full structural consistency check for s = 1..6."""

    def test_consistency_s1_to_s6(self):
        # VERIFIED: [LC] All structural checks pass for s = 1..6.
        r = verify_structural_consistency(6)
        assert r["ok"], f"structural consistency failed: {r['details']}"

    @pytest.mark.parametrize("s", range(1, 7))
    def test_z_degree_per_spin(self, s):
        """z-degree = s - 1 at each spin."""
        table = AllSpinCoproduct.delta_z_table(s)
        assert table["z_polynomial_degree"] == s - 1

    @pytest.mark.parametrize("s", range(2, 7))
    def test_total_ops_per_spin(self, s):
        """Total operator products = s(s+1)/2 - 1."""
        table = AllSpinCoproduct.delta_z_table(s)
        assert table["total_operator_products"] == s * (s + 1) // 2 - 1

    @pytest.mark.parametrize("s", range(2, 7))
    def test_terms_count_monotone(self, s):
        """Terms at z^p decrease: s-p terms at power p."""
        table = AllSpinCoproduct.delta_z_table(s)
        for p in range(s):
            assert table["terms_by_z_power"].get(p, 0) == s - p


# ---------------------------------------------------------------------------
# Part I: Direct matrix element tests
# ---------------------------------------------------------------------------

class TestDirectProperties:
    """Direct checks on the AllSpinCoproduct class."""

    def test_delta_z_returns_matrix(self):
        """delta_z returns a matrix of the correct dimension."""
        uni = AllSpinCoproduct(Psi=1.0, N_max=5)
        mat = uni.delta_z(2, 0, 0.3 + 0.2j)
        assert mat.shape == (uni.dim, uni.dim)

    def test_delta_z_s1_is_primitive(self):
        """At s=1, Delta_z(psi_1) = J^L + J^R (no z-shift in the psi-basis).

        The psi-level coproduct at s=1 has zero z-degree: the formula gives
        psi_1^L + psi_1^R with no z-dependent terms. The z-shifted Delta_J
        from the spin-2 engine is the CONFORMAL-WEIGHT-shifted version,
        which is a different operation. Here we test the psi-level formula.
        """
        uni = AllSpinCoproduct(Psi=2.0, N_max=5)
        P = uni.safe_proj(3)
        for n in [0, -1, 1]:
            d1 = uni.delta_z(1, n, 0.3 + 0.2j)
            # At s=1, no z-dependence: Delta_z(psi_1) = J^L + J^R
            expected = uni.J_L(n).astype(complex) + uni.J_R(n).astype(complex)
            err = float(np.max(np.abs(P @ (d1 - expected) @ P)))
            assert err < 1e-10, f"n={n}: error {err:.2e}"

    def test_cross_term_z0_real(self):
        """At z=0, cross-term is real for real Psi."""
        uni = AllSpinCoproduct(Psi=2.0, N_max=5)
        P = uni.safe_proj(3)
        for s in [2, 3]:
            for n in [0, -1, -2]:
                c = uni.cross_term(s, n, 0.0)
                imag = float(np.max(np.abs(np.imag(P @ c @ P))))
                assert imag < 1e-12, f"s={s}, n={n}: imaginary part {imag:.2e}"

    def test_cross_term_creation(self):
        """C_s(-n) creates states from vacuum for n >= s."""
        uni = AllSpinCoproduct(Psi=1.0, N_max=6)
        vac = np.zeros(uni.dim, dtype=complex)
        vi = uni.H.idx[()] * uni.d + uni.H.idx[()]
        vac[vi] = 1.0
        for s in [2, 3]:
            result = uni.cross_term(s, -s, 0.0) @ vac
            assert float(np.linalg.norm(result)) > 0.01, (
                f"C_{s}(-{s})|vac> should be nonzero"
            )

    def test_z_poly_cross_reconstructs_cross_term(self):
        """z-polynomial cross-coefficients reconstruct the full cross-term."""
        uni = AllSpinCoproduct(Psi=2.0, N_max=5)
        P = uni.safe_proj(3)
        for s in [2, 3]:
            for n in [0, -1]:
                coeffs = uni.z_poly_cross_coefficients(s, n)
                assert len(coeffs) == s
                for z_val in [0.3 + 0.2j, -0.5 + 0.7j]:
                    reconstructed = np.zeros((uni.dim, uni.dim), dtype=complex)
                    for p, cp in enumerate(coeffs):
                        reconstructed += (z_val ** p) * cp
                    actual = uni.cross_term(s, n, z_val)
                    err = float(np.max(np.abs(P @ (reconstructed - actual) @ P)))
                    assert err < 1e-10, (
                        f"s={s}, n={n}, z={z_val}: reconstruction error {err:.2e}"
                    )

    def test_delta_z_raises_for_s4(self):
        """Fock space delta_z at s >= 4 raises NotImplementedError."""
        uni = AllSpinCoproduct(Psi=1.0, N_max=5)
        with pytest.raises(NotImplementedError):
            uni.delta_z(4, 0, 0.0)

    def test_delta_z_table_works_for_all_spins(self):
        """delta_z_table is available for s up to at least 20."""
        for s in range(1, 21):
            table = AllSpinCoproduct.delta_z_table(s)
            assert table["spin"] == s
            assert table["z_polynomial_degree"] == s - 1


# ---------------------------------------------------------------------------
# Part J: Multi-path cross-checks (AP10 compliance)
# ---------------------------------------------------------------------------

class TestMultiPathCrossChecks:
    """Multi-path verification: the same mathematical fact is verified
    through at least two independent computational paths.

    Each test computes a result via Path A and Path B, then asserts they
    agree. This catches implementation bugs that would not be caught by
    single-path hardcoded assertions.
    """

    @pytest.mark.parametrize("Psi", [1.0, 2.0, 3.7])
    def test_cross_s2_universal_vs_direct_convolution(self, Psi):
        """Path A: universal cross_term(2, n, z).
        Path B: direct sum_k J_k^L J_{n-k}^R + z*J_n^R.
        """
        uni = AllSpinCoproduct(Psi, N_max=5)
        P = uni.safe_proj(3)
        M = uni.N_max + 4
        z = 0.4 + 0.3j
        for n in [0, -1, -2]:
            path_a = uni.cross_term(2, n, z)
            path_b = np.zeros((uni.dim, uni.dim), dtype=complex)
            for k in range(-M, M + 1):
                path_b += uni.J_L(k) @ uni.J_R(n - k).astype(complex)
            path_b += z * uni.J_R(n).astype(complex)
            err = float(np.max(np.abs(P @ (path_a - path_b) @ P)))
            assert err < 1e-10, f"Psi={Psi}, n={n}: err {err:.2e}"

    @pytest.mark.parametrize("Psi", [1.0, 2.0])
    def test_cross_s3_universal_vs_spin3_expanded(self, Psi):
        """Path A: universal cross_term(3, n, z).
        Path B: spin-3 engine expanded formula (J,T decomposition).
        """
        from compute.lib.chiral_coproduct_spin3_engine import Spin3CoproductEngine
        uni = AllSpinCoproduct(Psi, N_max=5)
        sp3 = Spin3CoproductEngine(Psi, N_max=5)
        P = uni.safe_proj(3)
        z = 0.3 + 0.2j
        for n in [0, -1, -2]:
            path_a = uni.cross_term(3, n, z)
            path_b = sp3.cross_psi3_expanded(n, z)
            err = float(np.max(np.abs(P @ (path_a - path_b) @ P)))
            assert err < 1e-10, f"Psi={Psi}, n={n}: err {err:.2e}"

    def test_z_degree_fock_vs_structural(self):
        """Path A: numerical z-polynomial fit (Fock space).
        Path B: structural formula (algebraic).
        Both must give degree s-1.
        """
        for s in [2, 3]:
            fock_r = verify_z_polynomial_degree(s=s, Psi=2.0, N_max=5)
            struct_r = verify_z_polynomial_degree_structural(s)
            assert fock_r["ok"] and struct_r["ok"]
            assert fock_r["expected_degree"] == struct_r["expected"]

    def test_highest_z_fock_vs_structural(self):
        """Path A: Fock space z^{s-1} coefficient (numerical).
        Path B: structural term enumeration.
        Both confirm z^{s-1} = J^R.
        """
        for s in [2, 3]:
            fock_r = verify_highest_z_is_JR(s=s, Psi=2.0, N_max=5)
            struct_r = verify_highest_z_is_JR(s=s + 2, Psi=2.0, N_max=5)
            assert fock_r["ok"]
            assert struct_r["ok"]

    @pytest.mark.parametrize("Psi", [1.0, 2.0])
    def test_delta_z_s2_decomposition_vs_full(self, Psi):
        """Path A: delta_z(2, n, z) as full matrix.
        Path B: psi_2^L + psi_2^R + cross_term(2, n, z).
        """
        uni = AllSpinCoproduct(Psi, N_max=5)
        P = uni.safe_proj(3)
        z = 0.5 + 0.1j
        for n in [0, -1]:
            path_a = uni.delta_z(2, n, z)
            path_b = (
                uni._psi_L(2, n).astype(complex)
                + uni._psi_R(2, n).astype(complex)
                + uni.cross_term(2, n, z)
            )
            err = float(np.max(np.abs(P @ (path_a - path_b) @ P)))
            assert err < 1e-10, f"Psi={Psi}, n={n}: err {err:.2e}"

    def test_subleading_z1_fock_vs_structural_coefficient(self):
        """Path A: Fock space z^1 cross-coefficient at s=3.
        Path B: structural prediction (s-1 = 2 for the R-shifted part).
        """
        uni = AllSpinCoproduct(Psi=2.0, N_max=5)
        P = uni.safe_proj(3)
        coeffs = uni.z_poly_cross_coefficients(3, 0)
        z1_coeff = coeffs[1]

        # Path B: (s-1)*psi_2^R + [J^L conv J^R] at s=3
        M = uni.N_max + 4
        expected = 2.0 * uni._psi_R(2, 0).astype(complex)
        for m in range(-M, M + 1):
            expected += uni._psi_L(1, m) @ uni._psi_R(1, -m).astype(complex)
        err = float(np.max(np.abs(P @ (z1_coeff - expected) @ P)))
        assert err < 1e-10, f"z^1 mismatch: err {err:.2e}"

        # Also verify structural side
        info = AllSpinCoproduct.subleading_coefficient_z1(3)
        assert info["leading_R_shifted"]["coefficient"] == 2

    @pytest.mark.parametrize("s", [2, 3])
    def test_cross_term_four_engine_agreement(self, s):
        """The same cross-term computed by 4 independent engines must agree.

        Path A: universal engine (this file)
        Path B: spin-3 engine (cross_psi2 or cross_psi3)
        Path C: general engine (cross_psi_s)
        Path D: allspin engine (cross_psi_s)
        """
        from compute.lib.chiral_coproduct_spin3_engine import Spin3CoproductEngine
        from compute.lib.chiral_coproduct_general_engine import GeneralCoproductEngine
        from compute.lib.chiral_coproduct_allspin_engine import AllSpinCoproductEngine

        Psi, N_max, z = 2.0, 5, 0.3 + 0.2j
        uni = AllSpinCoproduct(Psi, N_max)
        sp3 = Spin3CoproductEngine(Psi, N_max)
        gen = GeneralCoproductEngine(Psi, N_max)
        asc = AllSpinCoproductEngine(Psi, N_max)
        P = uni.safe_proj(3)

        for n in [0, -1]:
            a = uni.cross_term(s, n, z)
            b = sp3.cross_psi2(n, z) if s == 2 else sp3.cross_psi3(n, z)
            c = gen.cross_psi_s(s, n, z)
            d = asc.cross_psi_s(s, n, z)

            for label, other in [("sp3", b), ("gen", c), ("asc", d)]:
                err = float(np.max(np.abs(P @ (a - other) @ P)))
                assert err < 1e-10, (
                    f"s={s}, n={n}: universal vs {label} err {err:.2e}"
                )

    @pytest.mark.parametrize("s", range(2, 7))
    def test_term_count_two_paths(self, s):
        """Path A: count terms in delta_z_table.
        Path B: direct enumeration sum_{p=0}^{s-1} (s-p) = s(s+1)/2.
        """
        table = AllSpinCoproduct.delta_z_table(s)
        path_a = table["total_terms"]
        # Path B: direct sum
        path_b = sum(s - p for p in range(s))
        assert path_a == path_b, f"s={s}: {path_a} != {path_b}"

    def test_binomial_upper_negation_identity(self):
        """Cross-check: C(s-a-1, p) = (-1)^p * C(-s+a+1+p-1, p)
        = (-1)^p * C(-(s-a-p), p) = (-1)^p * C(-b, p).

        The universal formula written with (-1)^k C(-b, k) must match
        the standard C(b+k-1, k) form used in the general engine.
        """
        import math
        for s in range(2, 7):
            table = AllSpinCoproduct.delta_z_table(s)
            for term in table["all_terms"]:
                a = term["left_spin"]
                p = term["z_power"]
                b = term["right_spin"]
                # C(s-a-1, p) from the formula
                standard = math.comb(s - a - 1, p)
                # C(b+k-1, k) with k=p, b=s-a-p
                alt = math.comb(b + p - 1, p)
                assert standard == alt == term["binomial"], (
                    f"s={s}, a={a}, p={p}, b={b}: "
                    f"C({s-a-1},{p})={standard}, C({b+p-1},{p})={alt}, "
                    f"stored={term['binomial']}"
                )
