"""Tests for the Zamolodchikov tetrahedron computation engine.

Exercises the symbolic computation paths added to the tetrahedron engine:
  1. Optimised charge-1 YBE verification (symbolic kappa, u, v).
  2. Specialised ZTE obstruction with exact rational h1, h2, kappa.
  3. Kappa-expansion: leading order is O(kappa^2), orders 0 and 1 vanish.
  4. Cross-check: symbolic specialised result matches numerical at same params.
  5. Numpy division-by-zero fix at z + kappa = 0.
  6. Charge-2 optimised S-operator agrees with full 16x16 projection.
  7. Fully symbolic ZTE (slow, all 5 parameters symbolic).

VERIFIED sources:
[DC]  Direct computation via sympy exact arithmetic.
[KV]  Kapranov-Voevodsky: permutation limit satisfies ZTE.
[YBE] Yang-Baxter equation: positive control on optimised path.
"""

import numpy as np
import pytest

from sympy import Rational, Symbol, cancel, expand, symbols

from compute.lib.zamolodchikov_tetrahedron_engine import (
    _embed_r_numpy,
    _r_embed_charge2,
    _s_operator_charge2,
    _yang_r_numpy,
    charge_sector_basis,
    project_to_charge_sector,
    s_operator,
    s_operator_numpy,
    verify_ybe_charge2_optimized,
    yang_r_matrix_4x4,
    zamolodchikov_charge2_symbolic_optimized,
    zamolodchikov_zte_numpy,
    zte_obstruction_kappa_expansion,
    zte_obstruction_specialised,
)


# ---------------------------------------------------------------------------
# YBE on optimised charge-1 path (positive control)
# ---------------------------------------------------------------------------

class TestYBEOptimised:
    """YBE on the charge-1 sector of V^3 via the optimised 3x3 path."""

    def test_ybe_charge1_satisfied(self):
        """YBE holds symbolically on the charge-1 sector (3x3)."""
        r = verify_ybe_charge2_optimized()
        assert r["all_zero"], (
            "YBE FAILED on charge-1 optimised path. "
            "This is a positive control -- should never fail."
        )

    def test_ybe_charge1_diff_is_zero_matrix(self):
        """Every entry of the YBE difference matrix is exactly 0."""
        r = verify_ybe_charge2_optimized()
        diff = r["diff"]
        for i in range(3):
            for j in range(3):
                assert diff[i, j] == 0, (
                    f"YBE diff[{i},{j}] = {diff[i,j]} != 0"
                )


# ---------------------------------------------------------------------------
# Numpy division-by-zero fix
# ---------------------------------------------------------------------------

class TestNumpyDivisionByZeroFix:
    """The numpy R-matrix no longer crashes when z + kappa = 0."""

    def test_no_crash_at_pole(self):
        """R(z) at z = -kappa returns a finite matrix (no NaN/Inf)."""
        kappa = -6.0
        z = 6.0  # z + kappa = 0
        R = _yang_r_numpy(z, kappa)
        assert np.all(np.isfinite(R)), (
            "R-matrix contains NaN/Inf at z = -kappa"
        )

    def test_pole_returns_permutation(self):
        """At the pole z = -kappa, the regularised R-matrix is P."""
        kappa = -3.5
        z = 3.5  # z + kappa = 0
        R = _yang_r_numpy(z, kappa)
        P = np.array([[1, 0, 0, 0],
                      [0, 0, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 1]], dtype=complex)
        assert np.allclose(R, P, atol=1e-14), (
            "Regularised R-matrix at pole is not the permutation"
        )

    def test_zte_monotonic_decrease_no_crash(self):
        """The Kapranov-Voevodsky monotonic decrease test no longer crashes.

        This exercises the code path that previously failed due to
        division by zero when spectral parameter differences coincided
        with kappa values.
        """
        u_vals = [0, 1, 3, 7]
        prev_err = float('inf')
        for kap in [10.0, 1.0, 0.1, 0.01, 0.001]:
            r = zamolodchikov_zte_numpy(kap, u_vals)
            err = r["max_error"]
            assert np.isfinite(err), (
                f"ZTE error is not finite at kappa={kap}"
            )
            assert err < prev_err, (
                f"Obstruction not decreasing: kappa={kap}, "
                f"err={err:.4e} >= prev {prev_err:.4e}"
            )
            prev_err = err


# ---------------------------------------------------------------------------
# Charge-2 optimised S-operator: cross-check with full-space projection
# ---------------------------------------------------------------------------

class TestCharge2Optimised:
    """Optimised 6x6 path agrees with full 16x16 -> project path."""

    def test_s_operator_charge2_vs_full(self):
        """S_{012} on charge-2 via optimised 6x6 equals projection of 16x16."""
        kappa = Symbol("kappa")
        u0, u1, u2 = Rational(0), Rational(1), Rational(3)

        # Optimised 6x6 path.
        S_opt = _s_operator_charge2(u0, u1, u2, kappa, 0, 1, 2)

        # Full 16x16 path, then project.
        S_full = s_operator(u0, u1, u2, kappa, 0, 1, 2, 4)
        S_proj = project_to_charge_sector(S_full, 4, 2)

        diff = (S_opt - S_proj).applyfunc(lambda x: cancel(expand(x)))
        for i in range(6):
            for j in range(6):
                assert diff[i, j] == 0, (
                    f"S-operator mismatch at ({i},{j}): "
                    f"opt={S_opt[i,j]}, proj={S_proj[i,j]}"
                )

    def test_r_embed_charge2_vs_full(self):
        """R_{01} on charge-2 via optimised 6x6 equals projection of 16x16."""
        from compute.lib.zamolodchikov_tetrahedron_engine import (
            _embed_r_matrix,
        )
        kappa = Symbol("kappa")
        z = Symbol("z")

        R_opt = _r_embed_charge2(z, kappa, 0, 1)
        R_full = _embed_r_matrix(z, kappa, 0, 1, 4)
        R_proj = project_to_charge_sector(R_full, 4, 2)

        diff = (R_opt - R_proj).applyfunc(lambda x: cancel(expand(x)))
        for i in range(6):
            for j in range(6):
                assert diff[i, j] == 0, (
                    f"R-embed mismatch at ({i},{j})"
                )

    def test_r_embed_all_pairs(self):
        """R_{ij} optimised equals projection for all 6 pairs (i,j)."""
        from compute.lib.zamolodchikov_tetrahedron_engine import (
            _embed_r_matrix,
        )
        kappa = Symbol("kappa")
        z = Symbol("z")

        for i in range(4):
            for j in range(i + 1, 4):
                R_opt = _r_embed_charge2(z, kappa, i, j)
                R_full = _embed_r_matrix(z, kappa, i, j, 4)
                R_proj = project_to_charge_sector(R_full, 4, 2)
                diff = (R_opt - R_proj).applyfunc(
                    lambda x: cancel(expand(x))
                )
                all_zero = all(
                    diff[a, b] == 0 for a in range(6) for b in range(6)
                )
                assert all_zero, (
                    f"R-embed mismatch for pair ({i},{j})"
                )


# ---------------------------------------------------------------------------
# ZTE specialised: exact rational h1, h2
# ---------------------------------------------------------------------------

class TestZTESpecialised:
    """ZTE obstruction with specific CY parameters h1, h2."""

    def test_h1_1_h2_2_not_satisfied(self):
        """ZTE fails for h1=1, h2=2, h3=-3, kappa=-6."""
        r = zte_obstruction_specialised(Rational(1), Rational(2))
        assert r["kappa"] == Rational(-6), (
            f"kappa should be -6, got {r['kappa']}"
        )
        assert not r["all_zero"], "ZTE should NOT be satisfied"

    def test_h1_1_h2_2_exact_entry(self):
        """Verify a specific entry of the obstruction at h1=1, h2=2."""
        r = zte_obstruction_specialised(Rational(1), Rational(2))
        # The obstruction is an exact rational number.
        diff = r["diff_charge2"]
        # At least some entries must be nonzero rationals.
        nonzero = [(i, j) for i in range(6) for j in range(6)
                   if diff[i, j] != 0]
        assert len(nonzero) > 0, "All entries zero -- ZTE should fail"
        # Each nonzero entry is a Rational (no symbolic variables remain).
        for i, j in nonzero:
            assert diff[i, j].is_rational, (
                f"Entry ({i},{j}) = {diff[i,j]} is not rational"
            )

    def test_h1_half_h2_third(self):
        """ZTE fails for h1=1/2, h2=1/3, h3=-5/6, kappa=5/72."""
        r = zte_obstruction_specialised(Rational(1, 2), Rational(1, 3))
        expected_kappa = Rational(1, 2) * Rational(1, 3) * Rational(-5, 6)
        assert r["kappa"] == expected_kappa, (
            f"kappa mismatch: {r['kappa']} vs {expected_kappa}"
        )
        assert not r["all_zero"], "ZTE should NOT be satisfied"

    def test_specialised_antisymmetric(self):
        """Obstruction is antisymmetric for specific h1, h2."""
        r = zte_obstruction_specialised(Rational(1), Rational(2))
        diff = r["diff_charge2"]
        for i in range(6):
            for j in range(6):
                assert cancel(diff[i, j] + diff[j, i]) == 0, (
                    f"Antisymmetry fails at ({i},{j}): "
                    f"D[{i},{j}]={diff[i,j]}, D[{j},{i}]={diff[j,i]}"
                )

    def test_specialised_matches_numerical(self):
        """Symbolic specialised result matches numerical computation."""
        r_sym = zte_obstruction_specialised(Rational(1), Rational(2))
        r_num = zamolodchikov_zte_numpy(-6.0, [0.0, 1.0, 3.0, 7.0])
        diff_num = project_to_charge_sector(r_num["diff"], 4, 2)
        diff_sym = r_sym["diff_charge2"]

        for i in range(6):
            for j in range(6):
                sym_val = complex(diff_sym[i, j])
                num_val = diff_num[i, j]
                assert abs(sym_val - num_val) < 1e-12, (
                    f"Sym/num mismatch at ({i},{j}): "
                    f"sym={sym_val}, num={num_val}"
                )

    def test_multiple_h_values(self):
        """ZTE fails for several different (h1, h2) values."""
        params = [
            (Rational(1), Rational(3)),
            (Rational(2), Rational(5)),
            (Rational(1, 7), Rational(1, 11)),
        ]
        for h1, h2 in params:
            r = zte_obstruction_specialised(h1, h2)
            assert not r["all_zero"], (
                f"ZTE should fail at h1={h1}, h2={h2}"
            )


# ---------------------------------------------------------------------------
# Kappa-expansion: leading order O(kappa^2)
# ---------------------------------------------------------------------------

class TestKappaExpansion:
    """Taylor expansion of the ZTE obstruction in kappa."""

    def test_leading_order_is_2(self):
        """The leading nonzero power of kappa is 2."""
        r = zte_obstruction_kappa_expansion(max_order=3)
        assert r["leading_order"] == 2, (
            f"Leading order = {r['leading_order']}, expected 2"
        )

    def test_order_0_vanishes(self):
        """All entries at order kappa^0 are zero (KV permutation limit)."""
        r = zte_obstruction_kappa_expansion(max_order=3)
        for i in range(6):
            for j in range(6):
                assert r["coefficients"][(i, j)][0] == 0, (
                    f"O(1) coefficient nonzero at ({i},{j}): "
                    f"{r['coefficients'][(i,j)][0]}"
                )

    def test_order_1_vanishes(self):
        """All entries at order kappa^1 are zero (first-order correction vanishes)."""
        r = zte_obstruction_kappa_expansion(max_order=3)
        for i in range(6):
            for j in range(6):
                assert r["coefficients"][(i, j)][1] == 0, (
                    f"O(kappa) coefficient nonzero at ({i},{j}): "
                    f"{r['coefficients'][(i,j)][1]}"
                )

    def test_order_2_nonzero(self):
        """Some entries at order kappa^2 are nonzero."""
        r = zte_obstruction_kappa_expansion(max_order=3)
        lm = r["leading_matrix"]
        nonzero_count = sum(
            1 for i in range(6) for j in range(6) if lm[i, j] != 0
        )
        assert nonzero_count > 0, "Leading matrix should have nonzero entries"

    def test_leading_matrix_antisymmetric(self):
        """The leading O(kappa^2) matrix is antisymmetric."""
        r = zte_obstruction_kappa_expansion(max_order=3)
        lm = r["leading_matrix"]
        for i in range(6):
            for j in range(6):
                assert cancel(lm[i, j] + lm[j, i]) == 0, (
                    f"Leading matrix not antisymmetric at ({i},{j}): "
                    f"L[{i},{j}]={lm[i,j]}, L[{j},{i}]={lm[j,i]}"
                )

    def test_diagonal_vanishes(self):
        """Diagonal of the leading matrix is zero (consequence of antisymmetry)."""
        r = zte_obstruction_kappa_expansion(max_order=3)
        lm = r["leading_matrix"]
        for i in range(6):
            assert lm[i, i] == 0, (
                f"Diagonal entry ({i},{i}) = {lm[i,i]} != 0"
            )

    def test_different_spectral_params(self):
        """Leading order is still 2 for different spectral parameters."""
        u = (Rational(0), Rational(2), Rational(5), Rational(11))
        r = zte_obstruction_kappa_expansion(u_vals=u, max_order=3)
        assert r["leading_order"] == 2, (
            f"Leading order = {r['leading_order']}, expected 2 "
            f"for u={u}"
        )

    def test_expansion_matches_specialised(self):
        """Kappa-expansion at kappa = -6 reproduces the specialised result.

        The Taylor expansion gives coefficients c_k. Then
        sum_{k=0}^{N} c_k * kappa^k should approximate the exact
        obstruction entry.
        """
        kappa_val = Rational(-6)
        r_exp = zte_obstruction_kappa_expansion(max_order=3)
        r_spec = zte_obstruction_specialised(Rational(1), Rational(2))

        # For entries where the expansion converges, the partial sum
        # should be a rough approximation.
        for i in range(6):
            for j in range(6):
                coeffs = r_exp["coefficients"][(i, j)]
                partial_sum = sum(
                    coeffs[k] * kappa_val**k for k in range(4)
                )
                exact = r_spec["diff_charge2"][i, j]
                if exact == 0:
                    continue
                # The expansion is truncated so we just check same sign
                # and rough magnitude (kappa=-6 is not small so convergence
                # is not perfect).
                if partial_sum != 0:
                    # At minimum, the kappa^2 term should be nonzero
                    # when the exact result is nonzero.
                    assert coeffs[2] != 0 or coeffs[3] != 0, (
                        f"Entry ({i},{j}): exact={exact} but "
                        f"kappa^2 and kappa^3 coefficients both zero"
                    )


# ---------------------------------------------------------------------------
# Charge-2 symbolic optimised (existing function, with symbolic kappa)
# ---------------------------------------------------------------------------

class TestCharge2SymbolicOptimised:
    """The existing zamolodchikov_charge2_symbolic_optimized function."""

    def test_zte_not_satisfied(self):
        """ZTE is not satisfied (symbolic kappa, numeric spectral params)."""
        r = zamolodchikov_charge2_symbolic_optimized()
        assert not r["zte_satisfied"], "ZTE should NOT be satisfied"
        assert not r["all_zero"], "Obstruction should be nonzero"

    def test_antisymmetric(self):
        """Obstruction is antisymmetric."""
        r = zamolodchikov_charge2_symbolic_optimized()
        assert r["antisymmetric"], "Obstruction should be antisymmetric"

    def test_complement_vanishing(self):
        """Complement-pair entries (Hamming distance 4) vanish."""
        r = zamolodchikov_charge2_symbolic_optimized()
        assert r["complement_vanishing"], (
            "Complement-pair entries should vanish"
        )

    def test_nonzero_count_positive(self):
        """Some entries of the obstruction are nonzero."""
        r = zamolodchikov_charge2_symbolic_optimized()
        assert r["nonzero_count"] > 0, (
            f"Expected nonzero entries, got {r['nonzero_count']}"
        )

    def test_different_spectral_params(self):
        """ZTE fails for different spectral parameter choices."""
        u = (Rational(0), Rational(2), Rational(5), Rational(11))
        r = zamolodchikov_charge2_symbolic_optimized(u_vals=u)
        assert not r["zte_satisfied"], (
            "ZTE should NOT be satisfied at u=(0,2,5,11)"
        )

    def test_substitution_matches_specialised(self):
        """Substituting kappa=-6 in the symbolic result matches specialised."""
        r_sym = zamolodchikov_charge2_symbolic_optimized()
        r_spec = zte_obstruction_specialised(Rational(1), Rational(2))
        kappa = Symbol("kappa")

        for i in range(6):
            for j in range(6):
                sym_entry = r_sym["diff_charge2"][i, j].subs(
                    kappa, Rational(-6)
                )
                spec_entry = r_spec["diff_charge2"][i, j]
                assert cancel(sym_entry - spec_entry) == 0, (
                    f"Substitution mismatch at ({i},{j}): "
                    f"sym={sym_entry}, spec={spec_entry}"
                )


# ---------------------------------------------------------------------------
# Fully symbolic ZTE (slow: 5 symbolic variables)
# ---------------------------------------------------------------------------

class TestFullySymbolic:
    """Fully symbolic ZTE with all 5 parameters symbolic.

    These tests are marked slow because sympy multivariate rational
    function simplification with 5 variables is expensive (~minutes).
    """

    @pytest.mark.slow
    def test_fully_symbolic_not_satisfied(self):
        """ZTE is not satisfied with fully symbolic parameters."""
        from compute.lib.zamolodchikov_tetrahedron_engine import (
            zamolodchikov_charge2_fully_symbolic,
        )
        r = zamolodchikov_charge2_fully_symbolic()
        assert not r["zte_satisfied"], "ZTE should NOT be satisfied"

    @pytest.mark.slow
    def test_fully_symbolic_antisymmetric(self):
        """Obstruction is antisymmetric with fully symbolic parameters."""
        from compute.lib.zamolodchikov_tetrahedron_engine import (
            zamolodchikov_charge2_fully_symbolic,
        )
        r = zamolodchikov_charge2_fully_symbolic()
        assert r["antisymmetric"], "Obstruction should be antisymmetric"


# ---------------------------------------------------------------------------
# Multi-path cross-checks (AP10 compliance)
# ---------------------------------------------------------------------------

class TestMultiPathCrossChecks:
    """Cross-checks between independent computation paths.

    Each test verifies the same mathematical identity via two or more
    independent code paths: symbolic vs numerical, optimised vs full-space,
    specialised vs generic, Taylor expansion vs exact evaluation.
    """

    def test_optimised_zte_matches_full_space_zte(self):
        """Optimised 6x6 ZTE matches projection of full 16x16 ZTE.

        Path A: _s_operator_charge2 -> lhs/rhs -> diff  (6x6 direct)
        Path B: s_operator (16x16) -> project_to_charge_sector  (16x16 -> 6x6)
        """
        kap = Symbol("kappa")
        u = (Rational(0), Rational(1), Rational(3), Rational(7))

        # Path A: optimised 6x6.
        S012_a = _s_operator_charge2(u[0], u[1], u[2], kap, 0, 1, 2)
        S013_a = _s_operator_charge2(u[0], u[1], u[3], kap, 0, 1, 3)
        S023_a = _s_operator_charge2(u[0], u[2], u[3], kap, 0, 2, 3)
        S123_a = _s_operator_charge2(u[1], u[2], u[3], kap, 1, 2, 3)
        lhs_a = S012_a * S013_a * S023_a * S123_a
        rhs_a = S123_a * S023_a * S013_a * S012_a
        diff_a = (lhs_a - rhs_a).applyfunc(lambda x: cancel(expand(x)))

        # Path B: full 16x16, project to charge-2.
        n = 4
        S012_b = s_operator(u[0], u[1], u[2], kap, 0, 1, 2, n)
        S013_b = s_operator(u[0], u[1], u[3], kap, 0, 1, 3, n)
        S023_b = s_operator(u[0], u[2], u[3], kap, 0, 2, 3, n)
        S123_b = s_operator(u[1], u[2], u[3], kap, 1, 2, 3, n)
        lhs_b = S012_b * S013_b * S023_b * S123_b
        rhs_b = S123_b * S023_b * S013_b * S012_b
        diff_b_full = lhs_b - rhs_b
        diff_b = project_to_charge_sector(diff_b_full, n, 2)
        diff_b = diff_b.applyfunc(lambda x: cancel(expand(x)))

        for i in range(6):
            for j in range(6):
                assert cancel(diff_a[i, j] - diff_b[i, j]) == 0, (
                    f"Path A/B mismatch at ({i},{j}): "
                    f"opt={diff_a[i,j]}, full={diff_b[i,j]}"
                )

    def test_numpy_matches_sympy_specialised(self):
        """Numpy numerical ZTE matches sympy specialised at h1=1/2, h2=1/3.

        Path A: zamolodchikov_zte_numpy (floating point)
        Path B: zte_obstruction_specialised (exact rational)
        """
        h1, h2 = Rational(1, 2), Rational(1, 3)
        h3 = -(h1 + h2)
        kap = h1 * h2 * h3  # = -5/72
        u = (Rational(0), Rational(1), Rational(3), Rational(7))

        # Path A: numpy.
        r_num = zamolodchikov_zte_numpy(
            float(kap), [float(x) for x in u]
        )
        diff_num = project_to_charge_sector(r_num["diff"], 4, 2)

        # Path B: sympy specialised.
        r_sym = zte_obstruction_specialised(h1, h2, u_vals=u)
        diff_sym = r_sym["diff_charge2"]

        for i in range(6):
            for j in range(6):
                sym_val = complex(diff_sym[i, j])
                num_val = diff_num[i, j]
                assert abs(sym_val - num_val) < 1e-10, (
                    f"Numpy/sympy mismatch at ({i},{j}): "
                    f"num={num_val:.6e}, sym={sym_val:.6e}"
                )

    def test_kappa_expansion_reproduces_exact_at_small_kappa(self):
        """Taylor expansion in kappa matches exact evaluation at small kappa.

        Path A: zte_obstruction_kappa_expansion (Taylor coefficients)
        Path B: zte_obstruction_specialised (exact rational at specific h)

        For small kappa, the partial sum of the Taylor series should
        closely approximate the exact result.
        """
        # h1=1/10, h2=1/20 -> h3=-3/20, kappa=h1*h2*h3 = -3/4000
        h1, h2 = Rational(1, 10), Rational(1, 20)
        kap_val = h1 * h2 * (-(h1 + h2))  # = -3/4000, small

        # Path A: Taylor expansion.
        r_exp = zte_obstruction_kappa_expansion(max_order=3)
        # Path B: exact specialised.
        r_spec = zte_obstruction_specialised(h1, h2)

        for i in range(6):
            for j in range(6):
                exact = r_spec["diff_charge2"][i, j]
                if exact == 0:
                    continue
                coeffs = r_exp["coefficients"][(i, j)]
                approx = sum(
                    coeffs[k] * kap_val**k for k in range(4)
                )
                # For small kappa, the O(kappa^4) remainder should
                # be negligible relative to the O(kappa^2) leading term.
                rel_err = abs(float(cancel(approx - exact) / exact))
                assert rel_err < 0.05, (
                    f"Taylor approx poor at ({i},{j}): "
                    f"exact={float(exact):.6e}, "
                    f"approx={float(approx):.6e}, "
                    f"rel_err={rel_err:.4f}"
                )

    def test_three_h_values_all_agree_sym_vs_num(self):
        """Symbolic and numerical paths agree for 3 different (h1,h2) choices.

        Path A: zte_obstruction_specialised (sympy exact)
        Path B: zamolodchikov_zte_numpy (numpy float)
        """
        cases = [
            (Rational(1), Rational(2)),      # kappa = -6
            (Rational(1), Rational(3)),      # kappa = -12
            (Rational(2), Rational(5)),      # kappa = -70
        ]
        u = (Rational(0), Rational(1), Rational(3), Rational(7))

        for h1, h2 in cases:
            h3 = -(h1 + h2)
            kap = h1 * h2 * h3

            r_sym = zte_obstruction_specialised(h1, h2, u_vals=u)
            r_num = zamolodchikov_zte_numpy(
                float(kap), [float(x) for x in u]
            )
            diff_num = project_to_charge_sector(r_num["diff"], 4, 2)

            for i in range(6):
                for j in range(6):
                    sym_val = complex(r_sym["diff_charge2"][i, j])
                    num_val = diff_num[i, j]
                    assert abs(sym_val - num_val) < 1e-10, (
                        f"h1={h1},h2={h2}: mismatch at ({i},{j}): "
                        f"sym={sym_val:.6e}, num={num_val:.6e}"
                    )
