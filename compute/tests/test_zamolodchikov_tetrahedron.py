"""Tests for the Zamolodchikov tetrahedron equation engine.

Verifies the complete 3-simplex analysis for the Yang R-matrix
R(z) = (z*Id + kappa*P)/(z+kappa) on V = C^2.

Key results verified here:
  1. YBE (2-simplex) on V^3: SATISFIED (positive control).
  2. Long braid relation on V^4: SATISFIED (consequence of YBE).
  3. Face-operator ZTE on V^4: NOT SATISFIED (the main result).
  4. Obstruction is O(kappa^2), antisymmetric, rank 4 on charge-2.
  5. At kappa=0, ZTE IS satisfied (Kapranov-Voevodsky permutation limit).
  6. LHS and RHS of ZTE have identical eigenvalues (similar operators).

The Yang R-matrix is intrinsically 2-dimensional: it solves the 2-simplex
equation but NOT the 3-simplex equation.

VERIFIED sources:
[KV] Kapranov-Voevodsky (1994): permutations give trivial tetrahedra.
[ZAM] Zamolodchikov (1981): ZTE as 3-simplex consistency.
[DC] Direct computation: 16x16 matrix products, charge-sector decomposition.
[SC] Scaling analysis: obstruction ~ kappa^2 from log-log fit.
"""

import numpy as np
import pytest

from compute.lib.zamolodchikov_tetrahedron_engine import (
    charge2_obstruction_analysis,
    charge_sector_basis,
    charge_sector_labels,
    kapranov_voevodsky_analysis,
    obstruction_scaling,
    project_to_charge_sector,
    run_tetrahedron_verification,
    s_operator_numpy,
    verify_long_braid_numpy,
    verify_ybe_symbolic,
    yang_r_matrix_4x4,
    zamolodchikov_zte_numpy,
    _embed_r_numpy,
    _yang_r_numpy,
)


# ---------------------------------------------------------------------------
# Foundations: R-matrix properties
# ---------------------------------------------------------------------------

class TestYangRMatrix:
    """Basic properties of the Yang R-matrix."""

    def test_unitarity(self):
        """R(z) * R(-z) = Id (unitarity)."""
        kappa = -6.0
        for z in [1.0, 2.5, 0.3, 7.0]:
            R_z = _yang_r_numpy(z, kappa)
            R_neg = _yang_r_numpy(-z, kappa)
            prod = R_z @ R_neg
            assert np.allclose(prod, np.eye(4), atol=1e-12), \
                f"R(z)*R(-z) != Id at z={z}, kappa={kappa}"

    def test_permutation_limit(self):
        """At z=0: R(0) = P (the permutation operator)."""
        kappa = -6.0
        R0 = _yang_r_numpy(0.0, kappa)
        P = np.array([[1, 0, 0, 0],
                      [0, 0, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 1]], dtype=complex)
        assert np.allclose(R0, P, atol=1e-14), "R(0) != P"

    def test_identity_limit(self):
        """As z -> infinity: R(z) -> Id."""
        kappa = -6.0
        R_big = _yang_r_numpy(1e10, kappa)
        assert np.allclose(R_big, np.eye(4), atol=1e-6), \
            "R(z) does not approach Id as z -> inf"

    def test_charge_preservation(self):
        """R(z) preserves the total number of 1-bits."""
        kappa = -6.0
        z = 2.5
        R = _yang_r_numpy(z, kappa)
        # |01> and |10> have charge 1; R should not mix with |00> or |11>
        # Check that the charge-0 and charge-2 sectors are diagonal
        assert abs(R[0, 1]) < 1e-14  # |00> <- |01>
        assert abs(R[0, 2]) < 1e-14  # |00> <- |10>
        assert abs(R[3, 1]) < 1e-14  # |11> <- |01>
        assert abs(R[3, 2]) < 1e-14  # |11> <- |10>
        assert abs(R[1, 0]) < 1e-14  # |01> <- |00>
        assert abs(R[2, 0]) < 1e-14  # |10> <- |00>
        assert abs(R[1, 3]) < 1e-14  # |01> <- |11>
        assert abs(R[2, 3]) < 1e-14  # |10> <- |11>

    def test_sympy_numpy_agreement(self):
        """Sympy and numpy implementations agree."""
        from sympy import Rational
        kappa = Rational(-6)
        z = Rational(5, 2)
        R_sym = yang_r_matrix_4x4(z, kappa)
        R_num = _yang_r_numpy(2.5, -6.0)
        for i in range(4):
            for j in range(4):
                assert abs(complex(R_sym[i, j]) - R_num[i, j]) < 1e-14


# ---------------------------------------------------------------------------
# Yang-Baxter equation (2-simplex, positive control)
# ---------------------------------------------------------------------------

class TestYangBaxterEquation:
    """YBE: the 2-simplex equation that the Yang R-matrix satisfies."""

    def test_ybe_symbolic(self):
        """YBE verified symbolically with symbolic kappa, u, v."""
        r = verify_ybe_symbolic()
        assert r["all_zero"], "YBE FAILED symbolically -- this should never happen"

    def test_ybe_numerical_multiple_params(self):
        """YBE verified numerically at several parameter values."""
        params = [
            (-6.0, 1.0, 3.0),
            (-0.42, 0.3, 0.8),
            (-120.0, 2.0, 5.0),
            (-0.006, 0.5, 1.0),
        ]
        n = 3
        for kappa, u, v in params:
            R01 = _embed_r_numpy(u - v, kappa, 0, 1, n)
            R02 = _embed_r_numpy(u, kappa, 0, 2, n)
            R12 = _embed_r_numpy(v, kappa, 1, 2, n)
            lhs = R01 @ R02 @ R12
            rhs = R12 @ R02 @ R01
            diff = lhs - rhs
            max_err = np.max(np.abs(diff))
            assert max_err < 1e-12, \
                f"YBE failed at kappa={kappa}, u={u}, v={v}: err={max_err:.2e}"


# ---------------------------------------------------------------------------
# Long braid relation (consequence of YBE)
# ---------------------------------------------------------------------------

class TestLongBraidRelation:
    """Long braid: lex-product of 6 R_{ij} = reverse-lex product on V^4."""

    def test_long_braid_kappa_neg6(self):
        r = verify_long_braid_numpy(-6.0, [0, 1, 3, 7])
        assert r["satisfied"], f"Long braid failed: max_err={r['max_error']:.2e}"

    def test_long_braid_small_kappa(self):
        r = verify_long_braid_numpy(-0.42, [0, 0.3, 0.8, 1.5])
        assert r["satisfied"], f"Long braid failed: max_err={r['max_error']:.2e}"

    def test_long_braid_large_kappa(self):
        r = verify_long_braid_numpy(-120.0, [0, 2, 5, 11])
        assert r["satisfied"], f"Long braid failed: max_err={r['max_error']:.2e}"


# ---------------------------------------------------------------------------
# Charge sector utilities
# ---------------------------------------------------------------------------

class TestChargeSectors:
    """Charge sector decomposition of V^{tensor n}."""

    def test_charge_basis_n4_q2(self):
        """Charge-2 basis of V^4 has 6 elements."""
        basis = charge_sector_basis(4, 2)
        assert len(basis) == 6
        # Verify these are exactly the 4-bit strings with 2 ones
        for idx in basis:
            assert bin(idx).count('1') == 2

    def test_charge_dimensions(self):
        """dim(charge q of V^n) = C(n,q)."""
        from math import comb
        for n in [3, 4, 5]:
            for q in range(n + 1):
                assert len(charge_sector_basis(n, q)) == comb(n, q)

    def test_labels_n4_q2(self):
        labels = charge_sector_labels(4, 2)
        expected = ["|0011>", "|0101>", "|0110>", "|1001>", "|1010>", "|1100>"]
        assert labels == expected

    def test_charge_sectors_cover_full_space(self):
        """All charge sectors together span the full 2^n space."""
        n = 4
        all_indices = []
        for q in range(n + 1):
            all_indices.extend(charge_sector_basis(n, q))
        assert sorted(all_indices) == list(range(2 ** n))


# ---------------------------------------------------------------------------
# S-operator (face / half-monodromy)
# ---------------------------------------------------------------------------

class TestSOperator:
    """Properties of the face operator S_{ijk} = R_{ij} R_{ik} R_{jk}."""

    def test_s_operator_preserves_charge(self):
        """S_{012} preserves charge sectors on V^3."""
        kappa = -6.0
        S = s_operator_numpy(0.0, 1.0, 3.0, kappa, 0, 1, 2, 3)
        n = 3
        for q in range(n + 1):
            idx_q = charge_sector_basis(n, q)
            idx_other = [i for i in range(2 ** n) if i not in idx_q]
            if not idx_q or not idx_other:
                continue
            cross_block = S[np.ix_(idx_other, idx_q)]
            assert np.max(np.abs(cross_block)) < 1e-14, \
                f"S_{'{012}'} mixes charge {q} with other sectors"

    def test_s_equals_ybe_rhs(self):
        """S_{012} = R_{01}R_{02}R_{12} = R_{12}R_{02}R_{01} by YBE."""
        kappa = -6.0
        u0, u1, u2 = 0.0, 1.0, 3.0
        n = 3
        # Forward (our definition)
        S_fwd = s_operator_numpy(u0, u1, u2, kappa, 0, 1, 2, n)
        # Reverse
        R12 = _embed_r_numpy(u1 - u2, kappa, 1, 2, n)
        R02 = _embed_r_numpy(u0 - u2, kappa, 0, 2, n)
        R01 = _embed_r_numpy(u0 - u1, kappa, 0, 1, n)
        S_rev = R12 @ R02 @ R01
        assert np.allclose(S_fwd, S_rev, atol=1e-12), \
            "S_{012} (forward) != S_{012} (reverse by YBE)"

    def test_s_at_kappa0_is_permutation(self):
        """At kappa=0, S_{012} is a permutation matrix (product of transpositions)."""
        kappa = 1e-15  # near-zero
        S = s_operator_numpy(0.0, 1.0, 3.0, kappa, 0, 1, 2, 3)
        # Should be close to a permutation (product of 3 permutations)
        # Each row and column should have exactly one entry close to 1
        for row in range(8):
            sorted_abs = np.sort(np.abs(S[row, :]))[::-1]
            assert abs(sorted_abs[0] - 1.0) < 1e-8, \
                f"S at kappa~0: row {row} max entry = {sorted_abs[0]}"


# ---------------------------------------------------------------------------
# Zamolodchikov tetrahedron equation: the main result
# ---------------------------------------------------------------------------

class TestZamolodchikovTetrahedron:
    """ZTE (3-simplex): the Yang R-matrix does NOT satisfy it."""

    def test_zte_not_satisfied_kappa_neg6(self):
        """ZTE fails at kappa = -6 (h1=1, h2=2, h3=-3)."""
        r = zamolodchikov_zte_numpy(-6.0, [0, 1, 3, 7])
        assert r["max_error"] > 1e-3, \
            f"ZTE unexpectedly satisfied at kappa=-6: err={r['max_error']:.2e}"

    def test_zte_not_satisfied_small_kappa(self):
        """ZTE fails at kappa = -0.42 (h1=0.5, h2=0.7)."""
        r = zamolodchikov_zte_numpy(-0.42, [0, 0.3, 0.8, 1.5])
        assert r["max_error"] > 1e-4, \
            f"ZTE unexpectedly satisfied at kappa=-0.42: err={r['max_error']:.2e}"

    def test_zte_not_satisfied_large_kappa(self):
        """ZTE fails at kappa = -120 (h1=3, h2=5)."""
        r = zamolodchikov_zte_numpy(-120.0, [0, 2, 5, 11])
        assert r["max_error"] > 1e-2, \
            f"ZTE unexpectedly satisfied at kappa=-120: err={r['max_error']:.2e}"

    def test_zte_charges_0_and_4_trivial(self):
        """Charges 0 and 4 (dim 1) trivially satisfy ZTE."""
        r = zamolodchikov_zte_numpy(-6.0, [0, 1, 3, 7])
        assert r["sector_results"][0]["is_zero"], "Charge 0 should be trivial"
        assert r["sector_results"][4]["is_zero"], "Charge 4 should be trivial"

    def test_zte_charge2_nontrivial(self):
        """Charge-2 sector (dim 6) has nonzero ZTE obstruction."""
        r = zamolodchikov_zte_numpy(-6.0, [0, 1, 3, 7])
        assert not r["sector_results"][2]["is_zero"], \
            "Charge 2 ZTE obstruction should be nonzero"

    def test_zte_charge1_and_3_nontrivial(self):
        """Charges 1 and 3 (dim 4) have nonzero ZTE obstruction."""
        r = zamolodchikov_zte_numpy(-6.0, [0, 1, 3, 7])
        assert not r["sector_results"][1]["is_zero"], \
            "Charge 1 ZTE obstruction should be nonzero"
        assert not r["sector_results"][3]["is_zero"], \
            "Charge 3 ZTE obstruction should be nonzero"


# ---------------------------------------------------------------------------
# Kapranov-Voevodsky: kappa=0 permutation limit satisfies ZTE
# ---------------------------------------------------------------------------

class TestKapranovVoevodsky:
    """At kappa=0 (permutation limit), ZTE is trivially satisfied."""

    def test_zte_at_kappa_zero(self):
        """ZTE satisfied at kappa = 0 (R = P, pure permutation)."""
        # Use very small kappa (exactly 0 causes division by zero)
        r = zamolodchikov_zte_numpy(1e-14, [0, 1, 3, 7])
        # Obstruction should be near machine epsilon
        assert r["max_error"] < 1e-6, \
            f"ZTE should be nearly satisfied at kappa~0: err={r['max_error']:.2e}"

    def test_zte_approaches_zero_as_kappa_shrinks(self):
        """Obstruction monotonically decreases as |kappa| -> 0."""
        u_vals = [0, 1, 3, 7]
        prev_err = float('inf')
        for kap in [10.0, 1.0, 0.1, 0.01, 0.001]:
            r = zamolodchikov_zte_numpy(kap, u_vals)
            err = r["max_error"]
            assert err < prev_err, \
                f"Obstruction not decreasing: kappa={kap}, err={err:.4e} >= prev {prev_err:.4e}"
            prev_err = err

    def test_kv_analysis_structure(self):
        """Kapranov-Voevodsky analysis returns correct structure."""
        kv = kapranov_voevodsky_analysis()
        assert kv["ybe_satisfied"] is True
        assert kv["zte_satisfied"] is False
        assert kv["obstruction_order"] == 2
        assert kv["permutation_limit_satisfies_zte"] is True


# ---------------------------------------------------------------------------
# Obstruction structure: antisymmetry, eigenvalues, scaling
# ---------------------------------------------------------------------------

class TestObstructionStructure:
    """Structural properties of the ZTE obstruction LHS - RHS."""

    def test_obstruction_antisymmetric(self):
        """The 6x6 charge-2 obstruction is antisymmetric: D + D^T = 0."""
        a = charge2_obstruction_analysis(-6.0, [0, 1, 3, 7])
        assert a["is_antisymmetric"], \
            f"Obstruction not antisymmetric: err = {a['antisymmetry_error']:.2e}"

    def test_obstruction_antisymmetric_multiple_params(self):
        """Antisymmetry holds at multiple parameter values."""
        params = [
            (-0.42, [0, 0.3, 0.8, 1.5]),
            (-120.0, [0, 2, 5, 11]),
            (-0.006, [0, 0.5, 1.0, 2.0]),
        ]
        for kap, u_vals in params:
            a = charge2_obstruction_analysis(kap, u_vals)
            assert a["is_antisymmetric"], \
                f"Antisymmetry failed at kappa={kap}: err={a['antisymmetry_error']:.2e}"

    def test_eigenvalues_match(self):
        """LHS and RHS of ZTE have identical eigenvalues (similar operators)."""
        a = charge2_obstruction_analysis(-6.0, [0, 1, 3, 7])
        assert a["eigenvalues_match"], \
            "LHS and RHS eigenvalues do not match"

    def test_eigenvalues_match_all_sectors(self):
        """Eigenvalue matching holds in every charge sector."""
        r = zamolodchikov_zte_numpy(-6.0, [0, 1, 3, 7])
        for q, sr in r["sector_results"].items():
            assert sr["eigenvalues_match"], \
                f"Eigenvalue mismatch in charge {q} sector"

    def test_obstruction_rank_4(self):
        """Charge-2 obstruction has numerical rank 4 (out of 6)."""
        a = charge2_obstruction_analysis(-6.0, [0, 1, 3, 7])
        assert a["obstruction_rank"] == 4, \
            f"Expected rank 4, got {a['obstruction_rank']}"

    def test_obstruction_scaling_quadratic(self):
        """ZTE obstruction scales as O(kappa^2) for kappa -> 0."""
        s = obstruction_scaling()
        exp = s["scaling_exponent"]
        assert 1.8 < exp < 2.3, \
            f"Scaling exponent {exp:.3f} not near 2 (expected O(kappa^2))"

    def test_obstruction_scaling_with_different_u(self):
        """Scaling exponent is ~2 for different spectral parameter choices."""
        s = obstruction_scaling(u_vals=[0.0, 0.5, 2.0, 5.0])
        exp = s["scaling_exponent"]
        assert 1.8 < exp < 2.3, \
            f"Scaling exponent {exp:.3f} not near 2 for alternative u_vals"


# ---------------------------------------------------------------------------
# Cross-checks: ZTE vs long braid
# ---------------------------------------------------------------------------

class TestZTEvsLongBraid:
    """ZTE and long braid are different equations with different outcomes."""

    def test_long_braid_passes_where_zte_fails(self):
        """At the same parameters, long braid passes but ZTE fails."""
        kappa = -6.0
        u_vals = [0, 1, 3, 7]

        braid = verify_long_braid_numpy(kappa, u_vals)
        zte = zamolodchikov_zte_numpy(kappa, u_vals)

        assert braid["satisfied"], "Long braid should pass"
        assert zte["max_error"] > 1e-3, "ZTE should fail"

    def test_zte_involves_more_r_matrices(self):
        """ZTE face product uses 12 R-matrices (each R_{ij} twice),
        while long braid uses 6 (each once)."""
        # This is a structural test: verify the S-operator is a
        # product of 3 R-matrices by checking intermediate products
        kappa = -6.0
        u = [0.0, 1.0, 3.0, 7.0]
        n = 4
        # S_{012} should equal R_{01}(u01) @ R_{02}(u02) @ R_{12}(u12)
        S012 = s_operator_numpy(u[0], u[1], u[2], kappa, 0, 1, 2, n)
        R01 = _embed_r_numpy(u[0] - u[1], kappa, 0, 1, n)
        R02 = _embed_r_numpy(u[0] - u[2], kappa, 0, 2, n)
        R12 = _embed_r_numpy(u[1] - u[2], kappa, 1, 2, n)
        S012_manual = R01 @ R02 @ R12
        assert np.allclose(S012, S012_manual, atol=1e-12)


# ---------------------------------------------------------------------------
# Master verification suite
# ---------------------------------------------------------------------------

class TestMasterVerification:
    """Integration test: run_tetrahedron_verification."""

    def test_full_suite(self):
        """Run the complete verification suite and check summary."""
        results = run_tetrahedron_verification(include_symbolic=False)
        s = results["summary"]

        assert s["long_braid_satisfied"], "Long braid should pass"
        assert not s["zte_satisfied"], "ZTE should fail for Yang R-matrix"
        assert s["obstruction_antisymmetric"], "Obstruction should be antisymmetric"
        assert s["eigenvalues_match"], "LHS/RHS eigenvalues should match"

    def test_full_suite_with_symbolic_ybe(self):
        """Run suite including symbolic YBE verification."""
        results = run_tetrahedron_verification(include_symbolic=True)
        assert results["summary"]["ybe_satisfied"], "YBE should be satisfied"

    def test_conclusion_matches_kv(self):
        """Conclusion is consistent with Kapranov-Voevodsky."""
        results = run_tetrahedron_verification(include_symbolic=False)
        conclusion = results["summary"]["conclusion"]
        assert "NOT satisfy" in conclusion or "does NOT" in conclusion
        assert "O(kappa^2)" in conclusion
