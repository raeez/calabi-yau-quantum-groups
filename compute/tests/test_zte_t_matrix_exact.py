"""Tests for the exact rational ZTE correction T-matrix.

Verifies the construction of T with exact Fraction entries such that
S^{corr} = S^{fact} + T resolves the O(kappa^2) ZTE obstruction.

Key results verified:

  EXACT OBSTRUCTION (charge-2 sector):
    1. O_c2 is nonzero (ZTE fails).
    2. O_c2 is exactly antisymmetric: O + O^T = 0.
    3. O_c2 is exactly persymmetric: J O J = O.
    4. O_c2 has rank 4 (kernel dim 2).
    5. Diagonal of O_c2 is exactly zero.

  LINEARIZED SYSTEM:
    6. System A*x = b has shape (36, 80).
    7. rank(A) = 35 (one missing = scalar gauge), via compute_exact.
    8. System is consistent (verified by existence of exact solution).

  EXACT T-MATRIX STRUCTURE:
    9. T_c2 is exactly symmetric: T = T^T.
   10. T_c2 is exactly persymmetric: J T J = T.
   11. T_c2 has exactly zero anti-diagonal.
   12. T_c2 has only 10 distinct rational values.
   13. T_c2 entries are exact Fraction (not float).

  CORRECTION VERIFICATION:
   14. Corrected ZTE residual is nonzero (O(kappa^4) remainder).
   15. Residual is strictly smaller than original (linearized improvement).
   16. Original obstruction is O(kappa^2).

  CROSS-VALIDATION:
   17. Exact T agrees with numerical T to ~20% (higher-order difference).
   18. Both exact and numerical T share structural properties.
   19. Exact A*x reproduces b (system solution verification).
   20. Persymmetry of T cross-checked against persymmetry of O.

  PARAMETER INDEPENDENCE:
   21. Structural properties hold at different kappa.
   22. Structural properties hold at different spectral parameters.

VERIFIED sources:
[DC]  Direct computation via Fraction arithmetic.
[ZTE] Zamolodchikov tetrahedron equation (face formulation on V^4).
[LA]  Exact linear algebra via sympy rref + pseudoinverse.
[XV]  Cross-validation against numerical Newton iteration engine.
"""

import pytest
from fractions import Fraction

from compute.lib.zte_t_matrix_exact import (
    _KAPPA_DEFAULT,
    _U_DEFAULT,
    _build_linearized_system_c2,
    _fmat_mul,
    _fmat_sub,
    _zte_obstruction_frac,
    analyze_exact_structure,
    compute_exact_t_matrix,
    format_t_matrix,
    verify_correction,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def canonical():
    """Canonical exact T at kappa=1/5, u=[0,1,3,7]."""
    return compute_exact_t_matrix()


@pytest.fixture(scope="module")
def obstruction():
    """Exact obstruction at canonical parameters."""
    return _zte_obstruction_frac(_U_DEFAULT, _KAPPA_DEFAULT)


@pytest.fixture(scope="module")
def lin_system(obstruction):
    """Linearized system at canonical parameters."""
    A, b = _build_linearized_system_c2(obstruction["S_c2"],
                                        obstruction["obs_c2"])
    return {"A": A, "b": b}


# ---------------------------------------------------------------------------
# Exact obstruction tests
# ---------------------------------------------------------------------------

class TestExactObstruction:
    """Verify structural properties of the exact ZTE obstruction."""

    def test_obstruction_nonzero(self, obstruction):
        """O_c2 is nonzero: ZTE fails at O(kappa^2). [DC]"""
        obs = obstruction["obs_c2"]
        assert any(obs[r][c] != Fraction(0)
                    for r in range(6) for c in range(6))

    def test_obstruction_exactly_antisymmetric(self, obstruction):
        """O_c2 + O_c2^T = 0 exactly (not just approximately). [DC]"""
        obs = obstruction["obs_c2"]
        for i in range(6):
            for j in range(6):
                assert obs[i][j] == -obs[j][i], (
                    f"O[{i},{j}] = {obs[i][j]} but -O[{j},{i}] = "
                    f"{-obs[j][i]}"
                )

    def test_obstruction_exactly_persymmetric(self, obstruction):
        """J O J = O exactly: O[i,j] = O[5-i, 5-j]. [DC]"""
        obs = obstruction["obs_c2"]
        for i in range(6):
            for j in range(6):
                assert obs[i][j] == obs[5 - i][5 - j], (
                    f"O[{i},{j}] = {obs[i][j]} != "
                    f"O[{5-i},{5-j}] = {obs[5-i][5-j]}"
                )

    def test_obstruction_zero_diagonal(self, obstruction):
        """Diagonal of O_c2 is exactly zero (from antisymmetry). [DC]"""
        obs = obstruction["obs_c2"]
        for i in range(6):
            assert obs[i][i] == Fraction(0), (
                f"O[{i},{i}] = {obs[i][i]} != 0"
            )

    def test_obstruction_rank_4(self, obstruction):
        """O_c2 has rank 4 (kernel dimension 2). [LA]"""
        from sympy import Matrix, Rational
        obs = obstruction["obs_c2"]
        M = Matrix(6, 6,
                   lambda r, c: Rational(obs[r][c].numerator,
                                         obs[r][c].denominator))
        assert M.rank() == 4

    def test_obstruction_24_nonzero_entries(self, obstruction):
        """O_c2 has exactly 24 nonzero entries (antisym + zero diag). [DC]"""
        obs = obstruction["obs_c2"]
        nz = sum(1 for i in range(6) for j in range(6)
                 if obs[i][j] != Fraction(0))
        assert nz == 24


# ---------------------------------------------------------------------------
# Linearized system tests
# ---------------------------------------------------------------------------

class TestLinearizedSystem:
    """Verify the linearized ZTE system structure."""

    def test_system_shape(self, lin_system):
        """A has shape (36, 80), b has length 36. [DC]"""
        A = lin_system["A"]
        b = lin_system["b"]
        assert len(A) == 36
        assert len(A[0]) == 80
        assert len(b) == 36

    def test_system_rank_35_via_solver(self, canonical):
        """rank(A) = 35 (from the exact solver). [LA]"""
        assert canonical["rank"] == 35

    def test_system_consistent_via_solution(self, canonical, lin_system):
        """System is consistent: A*x = b verified directly. [DC+LA]

        Multi-path verification: compute A*x_solution and compare to b,
        rather than computing rank of the augmented matrix.
        """
        A = lin_system["A"]
        b = lin_system["b"]
        x = canonical["x_solution"]

        # Compute A*x
        Ax = [Fraction(0)] * 36
        for r in range(36):
            s = Fraction(0)
            for c in range(80):
                s += A[r][c] * x[c]
            Ax[r] = s

        # Compare to b
        for r in range(36):
            assert Ax[r] == b[r], (
                f"A*x[{r}] = {Ax[r]} != b[{r}] = {b[r]}"
            )


# ---------------------------------------------------------------------------
# Exact T-matrix structure tests
# ---------------------------------------------------------------------------

class TestExactTStructure:
    """Verify structural properties of the exact rational T_c2."""

    def test_exactly_symmetric(self, canonical):
        """T_c2 = T_c2^T exactly. [DC]"""
        T = canonical["T_c2"]
        for i in range(6):
            for j in range(6):
                assert T[i][j] == T[j][i], (
                    f"T[{i},{j}] = {T[i][j]} != T[{j},{i}] = {T[j][i]}"
                )

    def test_exactly_persymmetric(self, canonical):
        """J T J = T exactly: T[i,j] = T[5-i, 5-j]. [DC]"""
        T = canonical["T_c2"]
        for i in range(6):
            for j in range(6):
                assert T[i][j] == T[5 - i][5 - j], (
                    f"T[{i},{j}] = {T[i][j]} != "
                    f"T[{5-i},{5-j}] = {T[5-i][5-j]}"
                )

    def test_exactly_zero_antidiagonal(self, canonical):
        """T[i, 5-i] = 0 exactly for all i. [DC]"""
        T = canonical["T_c2"]
        for i in range(6):
            assert T[i][5 - i] == Fraction(0), (
                f"T[{i},{5-i}] = {T[i][5-i]} != 0"
            )

    def test_entries_are_fractions(self, canonical):
        """All T_c2 entries are exact Fraction objects. [DC]"""
        T = canonical["T_c2"]
        for i in range(6):
            for j in range(6):
                assert isinstance(T[i][j], Fraction), (
                    f"T[{i},{j}] is {type(T[i][j])}, not Fraction"
                )

    def test_ten_distinct_values(self, canonical):
        """T_c2 has exactly 10 distinct rational values. [DC]"""
        T = canonical["T_c2"]
        vals = set()
        for i in range(6):
            for j in range(6):
                vals.add(T[i][j])
        # Symmetry + persymmetry + zero antidiag constrains to 10
        assert len(vals) == 10, (
            f"Expected 10 distinct values, got {len(vals)}"
        )

    def test_nonzero_entries(self, canonical):
        """T_c2 has exactly 30 nonzero entries (36 - 6 antidiag). [DC]"""
        T = canonical["T_c2"]
        nz = sum(1 for i in range(6) for j in range(6)
                 if T[i][j] != Fraction(0))
        assert nz == 30

    def test_mixed_sign_diagonal(self, canonical):
        """T_c2 diagonal has both positive and negative entries. [DC]"""
        T = canonical["T_c2"]
        diag = [T[i][i] for i in range(6)]
        has_pos = any(d > 0 for d in diag)
        has_neg = any(d < 0 for d in diag)
        assert has_pos and has_neg, (
            f"Diagonal signs: "
            f"{['+' if d > 0 else '-' if d < 0 else '0' for d in diag]}"
        )

    def test_trace_nonzero(self, canonical):
        """T_c2 trace is nonzero. [DC]"""
        T = canonical["T_c2"]
        trace = sum(T[i][i] for i in range(6))
        assert trace != Fraction(0)

    def test_persymmetry_matches_obstruction(self, canonical, obstruction):
        """T persymmetry is consistent with O persymmetry. [DC, XV]

        Cross-check: both T_c2 and O_c2 satisfy the same JMJ = M
        persymmetry. For T (symmetric) this gives T[i,j]=T[5-i,5-j].
        For O (antisymmetric) this gives O[i,j]=O[5-i,5-j].
        """
        T = canonical["T_c2"]
        obs = obstruction["obs_c2"]
        # Both share the persymmetry
        for i in range(6):
            for j in range(6):
                assert T[i][j] == T[5 - i][5 - j]
                assert obs[i][j] == obs[5 - i][5 - j]


# ---------------------------------------------------------------------------
# Correction verification tests
# ---------------------------------------------------------------------------

class TestCorrectionVerification:
    """Verify the exact correction resolves the O(kappa^2) obstruction."""

    def test_residual_nonzero(self, canonical):
        """Corrected residual is nonzero (O(kappa^4) remains). [ZTE]"""
        obs_corr = canonical["obs_corr_c2"]
        assert any(obs_corr[r][c] != Fraction(0)
                    for r in range(6) for c in range(6))

    def test_residual_smaller_than_original(self, canonical):
        """Corrected residual is strictly smaller than original. [ZTE]"""
        obs = canonical["obs_c2"]
        obs_corr = canonical["obs_corr_c2"]
        max_obs = max(abs(obs[r][c])
                      for r in range(6) for c in range(6))
        max_corr = max(abs(obs_corr[r][c])
                       for r in range(6) for c in range(6))
        assert max_corr < max_obs

    def test_original_is_o_kappa2(self, canonical):
        """Original obstruction entries scale as kappa^2. [ZTE]"""
        obs = canonical["obs_c2"]
        max_obs = max(abs(obs[r][c])
                      for r in range(6) for c in range(6))
        kappa = canonical["kappa"]
        # O / kappa^2 should be O(1)
        ratio = max_obs / (kappa * kappa)
        assert Fraction(1, 100) < ratio < Fraction(100, 1), (
            f"O/kappa^2 = {float(ratio):.4f}, expected O(1)"
        )

    def test_corrected_s_built_correctly(self, canonical, obstruction):
        """S^{corr} = S + C verified by recomputing ZTE from parts. [DC+ZTE]

        Multi-path: independently rebuild corrected S from S_dict + C_faces,
        compute ZTE, and compare to stored obs_corr_c2.
        """
        from compute.lib.zte_t_matrix_exact import (
            _FACE_ORDER, _embed_ternary_full_frac, _fmat_add,
            _fmat_extract, _C2_IDX,
        )

        S_dict = obstruction["S_dict"]
        C_faces = canonical["C_faces"]

        # Rebuild corrected S operators
        S_corr = {}
        for (fi, fj, fk) in _FACE_ORDER:
            C_embed = _embed_ternary_full_frac(C_faces[(fi, fj, fk)],
                                                fi, fj, fk)
            S_corr[(fi, fj, fk)] = _fmat_add(S_dict[(fi, fj, fk)], C_embed)

        # Recompute ZTE
        lhs = _fmat_mul(
            _fmat_mul(
                _fmat_mul(S_corr[(0, 1, 2)], S_corr[(0, 1, 3)]),
                S_corr[(0, 2, 3)]
            ),
            S_corr[(1, 2, 3)]
        )
        rhs = _fmat_mul(
            _fmat_mul(
                _fmat_mul(S_corr[(1, 2, 3)], S_corr[(0, 2, 3)]),
                S_corr[(0, 1, 3)]
            ),
            S_corr[(0, 1, 2)]
        )
        recomputed_obs = _fmat_sub(lhs, rhs)
        recomputed_c2 = _fmat_extract(recomputed_obs, _C2_IDX, _C2_IDX)

        stored_c2 = canonical["obs_corr_c2"]
        for r in range(6):
            for c in range(6):
                assert recomputed_c2[r][c] == stored_c2[r][c], (
                    f"Recomputed[{r},{c}] = {recomputed_c2[r][c]} != "
                    f"stored[{r},{c}] = {stored_c2[r][c]}"
                )


# ---------------------------------------------------------------------------
# Cross-validation with numerical engine
# ---------------------------------------------------------------------------

class TestCrossValidation:
    """Cross-validate exact T against numerical engine."""

    def test_agrees_with_numerical(self, canonical):
        """Exact T agrees with numerical T to ~20%. [XV]

        The numerical engine does 3 Newton iterations, accumulating
        higher-order O(kappa^4) corrections.  The exact engine does 1
        linearized step.  They should agree at O(kappa^2) but differ
        at O(kappa^4), giving ~10-20% relative difference at kappa=0.2.
        """
        import numpy as np
        from compute.lib.zte_correction_explicit_final import (
            compute_zte_correction,
        )

        T_exact = canonical["T_c2"]
        numerical = compute_zte_correction(0.2, [0.0, 1.0, 3.0, 7.0])
        T_num = numerical["T_c2_clean"]

        for r in range(6):
            for c in range(6):
                e = float(T_exact[r][c])
                n = float(T_num[r, c].real)
                if abs(e) < 1e-10 and abs(n) < 1e-10:
                    continue
                rel = abs(e - n) / max(abs(e), abs(n))
                assert rel < 0.20, (
                    f"T[{r},{c}]: exact={e:.6e} num={n:.6e} rel={rel:.4f}"
                )

    def test_numerical_also_symmetric(self):
        """Numerical T is also (approximately) symmetric. [XV]"""
        import numpy as np
        from compute.lib.zte_correction_explicit_final import (
            compute_zte_correction,
        )
        numerical = compute_zte_correction(0.2, [0.0, 1.0, 3.0, 7.0])
        T_num = numerical["T_c2_clean"]
        sym_err = float(np.linalg.norm(T_num - T_num.T, "fro"))
        total = float(np.linalg.norm(T_num, "fro"))
        assert sym_err / total < 1e-8

    def test_exact_and_numerical_same_sign_pattern(self, canonical):
        """Exact and numerical T have identical sign patterns. [XV]

        Cross-check: even though magnitudes differ by O(kappa^4),
        the sign of each entry should be the same.
        """
        import numpy as np
        from compute.lib.zte_correction_explicit_final import (
            compute_zte_correction,
        )

        T_exact = canonical["T_c2"]
        numerical = compute_zte_correction(0.2, [0.0, 1.0, 3.0, 7.0])
        T_num = numerical["T_c2_clean"]

        for r in range(6):
            for c in range(6):
                e = float(T_exact[r][c])
                n = float(T_num[r, c].real)
                if abs(e) < 1e-10 and abs(n) < 1e-10:
                    continue
                # Same sign (or both near zero)
                if abs(e) > 1e-10 and abs(n) > 1e-10:
                    assert (e > 0) == (n > 0), (
                        f"Sign mismatch at [{r},{c}]: "
                        f"exact={e:.6e} num={n:.6e}"
                    )


# ---------------------------------------------------------------------------
# Parameter independence tests
# ---------------------------------------------------------------------------

class TestParameterIndependence:
    """Verify structural properties at different parameters."""

    def test_structure_at_kappa_one_third(self):
        """Structural properties hold at kappa = 1/3. [DC]"""
        result = compute_exact_t_matrix(kappa=Fraction(1, 3))
        T = result["T_c2"]

        # Symmetric
        for i in range(6):
            for j in range(6):
                assert T[i][j] == T[j][i]

        # Persymmetric
        for i in range(6):
            for j in range(6):
                assert T[i][j] == T[5 - i][5 - j]

        # Zero antidiag
        for i in range(6):
            assert T[i][5 - i] == Fraction(0)

    def test_structure_at_different_spectral_params(self):
        """Structural properties hold at u = [0, 2, 5, 11]. [DC]"""
        u = [Fraction(0), Fraction(2), Fraction(5), Fraction(11)]
        result = compute_exact_t_matrix(u=u)
        T = result["T_c2"]

        for i in range(6):
            for j in range(6):
                assert T[i][j] == T[j][i]
                assert T[i][j] == T[5 - i][5 - j]
        for i in range(6):
            assert T[i][5 - i] == Fraction(0)

    def test_rank_35_at_different_params(self):
        """Linearized system rank is 35 at kappa=1/3, u=[0,2,5,11]. [LA]"""
        u = [Fraction(0), Fraction(2), Fraction(5), Fraction(11)]
        result = compute_exact_t_matrix(kappa=Fraction(1, 3), u=u)
        assert result["rank"] == 35


# ---------------------------------------------------------------------------
# Format and display tests
# ---------------------------------------------------------------------------

class TestDisplay:
    """Verify display formatting."""

    def test_format_produces_output(self, canonical):
        """format_t_matrix returns a nonempty string. [DC]"""
        s = format_t_matrix(canonical["T_c2"])
        assert len(s) > 100
        assert "|0011>" in s

    def test_verify_correction_returns_dict(self, canonical):
        """verify_correction returns expected keys. [DC]"""
        v = verify_correction(canonical)
        assert "original_nonzero" in v
        assert "residual_is_zero" in v
        assert "improvement" in v


# ---------------------------------------------------------------------------
# Structural analysis tests
# ---------------------------------------------------------------------------

class TestStructuralAnalysis:
    """Verify the analyze_exact_structure function."""

    def test_analysis_symmetric(self, canonical):
        """Analysis correctly reports symmetry. [DC]"""
        s = analyze_exact_structure(canonical["T_c2"])
        assert s["is_symmetric"] is True

    def test_analysis_persymmetric(self, canonical):
        """Analysis correctly reports persymmetry. [DC]"""
        s = analyze_exact_structure(canonical["T_c2"])
        assert s["is_persymmetric"] is True

    def test_analysis_zero_antidiag(self, canonical):
        """Analysis correctly reports zero anti-diagonal. [DC]"""
        s = analyze_exact_structure(canonical["T_c2"])
        assert s["has_zero_antidiag"] is True

    def test_analysis_rank(self, canonical):
        """Analysis reports correct rank. [LA]"""
        s = analyze_exact_structure(canonical["T_c2"])
        assert s["rank"] == 6

    def test_analysis_nonzero_determinant(self, canonical):
        """Analysis reports nonzero determinant (full rank). [LA]"""
        s = analyze_exact_structure(canonical["T_c2"])
        assert s["determinant"] != 0
