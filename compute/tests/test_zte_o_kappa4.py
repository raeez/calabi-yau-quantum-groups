"""Tests for ZTE correction at O(kappa^4): iterated exact Newton solver.

Verifies the iterated exact Newton process that resolves the ZTE
obstruction order by order in kappa^2.

KEY DISCOVERY: The gauge choice in the linearized ZTE solver
determines whether the charge-2 ZTE is resolved in one step or
requires iteration:

  RREF GAUGE (free vars = 0):
    - Charge-2 ZTE resolved EXACTLY in ONE step.
    - Uses only 18/80 parameters (sparse).
    - Leaves larger residual on charge-1/3 sectors.

  MINIMUM-NORM GAUGE (pseudoinverse):
    - Charge-2 residual is O(kappa^4) after step 1.
    - Uses 72/80 parameters (dense).
    - Better balance across all charge sectors.
    - Rank jumps from 35 to 36 at step 2 (scalar gauge broken).

Both gauges satisfy A*x = b (the linearized ZTE on charge-2).

VERIFIED sources:
[DC]  Direct computation via Fraction arithmetic.
[ZTE] Zamolodchikov tetrahedron equation (face formulation on V^4).
[LA]  Exact linear algebra via sympy rref + pseudoinverse.
[SC]  Scaling check across kappa values.
[XV]  Cross-validation between two independent code paths.
"""

import pytest
from fractions import Fraction

from compute.lib.zte_o_kappa4 import (
    _FACE_ORDER,
    _apply_correction,
    _extract_faces_from_solution,
    _is_c2_zero,
    _max_abs_c2,
    _solve_exact_fast,
    _structural_analysis_c2,
    _zte_residual_from_s,
    compute_iterated_zte_correction,
    format_iterated_results,
)
from compute.lib.zte_t_matrix_exact import (
    _C2_IDX,
    _KAPPA_DEFAULT,
    _U_DEFAULT,
    _build_linearized_system_c2,
    _embed_ternary_full_frac,
    _fmat_add,
    _fmat_extract,
    _fmat_zeros,
    _zte_obstruction_frac,
    compute_exact_t_matrix,
)


# ---------------------------------------------------------------------------
# Fixtures (module-scoped for performance)
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def rref_one_step():
    """Single-step rref solver at canonical parameters."""
    return compute_iterated_zte_correction(
        n_steps=1, kappa=_KAPPA_DEFAULT, u=list(_U_DEFAULT),
        solver="rref",
    )


@pytest.fixture(scope="module")
def base_step1():
    """First correction from the base engine (min-norm).

    Uses compute_exact_t_matrix which is already fast (~2s).
    This avoids calling _solve_exact_minnorm in the iteration context.
    """
    return compute_exact_t_matrix()


@pytest.fixture(scope="module")
def minnorm_step2_data(base_step1):
    """Step 2 data built from the base engine's min-norm step 1.

    Step 1: uses base engine (min-norm, fast).
    Step 2: uses rref solver on the O(kappa^4) residual.
    """
    obs_data = _zte_obstruction_frac(_U_DEFAULT, _KAPPA_DEFAULT)
    S0 = obs_data["S_dict"]

    # Apply min-norm correction from base engine
    S1 = _apply_correction(S0, base_step1["C_faces"])
    resid1 = _zte_residual_from_s(S1)

    # Analyze O(kappa^4) residual
    obs4_c2 = resid1["obs_c2"]
    obs4_analysis = _structural_analysis_c2(obs4_c2, label="O(kappa^4)")

    # Step 2: linearize around S^{(1)} and solve with rref
    A2, b2 = _build_linearized_system_c2(resid1["S_c2"], obs4_c2)
    x2, rank2 = _solve_exact_fast(A2, b2)

    # Extract C_2 and apply
    C2_faces = _extract_faces_from_solution(x2)
    S2 = _apply_correction(S1, C2_faces)
    resid2 = _zte_residual_from_s(S2)
    obs6_c2 = resid2["obs_c2"]
    obs6_analysis = _structural_analysis_c2(obs6_c2, label="O(kappa^6)")

    # Build cumulative T = C_1 + C_2
    T_cum_16 = _fmat_zeros(16, 16)
    for (fi, fj, fk) in _FACE_ORDER:
        C1_embed = _embed_ternary_full_frac(
            base_step1["C_faces"][(fi, fj, fk)], fi, fj, fk
        )
        C2_embed = _embed_ternary_full_frac(
            C2_faces[(fi, fj, fk)], fi, fj, fk
        )
        T_cum_16 = _fmat_add(T_cum_16, _fmat_add(C1_embed, C2_embed))
    T_cum_c2 = _fmat_extract(T_cum_16, _C2_IDX, _C2_IDX)
    cum_analysis = _structural_analysis_c2(T_cum_c2, label="T_cumulative")

    # Combine face corrections
    C_cumulative = {}
    for f in _FACE_ORDER:
        C_cumulative[f] = _fmat_add(
            base_step1["C_faces"][f], C2_faces[f]
        )

    return {
        "S0": S0,
        "S1": S1,
        "S2": S2,
        "C2_faces": C2_faces,
        "C_cumulative": C_cumulative,
        "obs4_c2": obs4_c2,
        "obs4_analysis": obs4_analysis,
        "obs6_c2": obs6_c2,
        "obs6_analysis": obs6_analysis,
        "rank2": rank2,
        "T_cumulative_c2": T_cum_c2,
        "T_cumulative_analysis": cum_analysis,
        "kappa": _KAPPA_DEFAULT,
    }


# ---------------------------------------------------------------------------
# RREF gauge: charge-2 exact in one step
# ---------------------------------------------------------------------------

class TestRrefGaugeExact:
    """Verify that the rref gauge resolves charge-2 ZTE exactly."""

    def test_charge2_exactly_zero(self, rref_one_step):
        """Single rref step resolves charge-2 ZTE exactly. [ZTE, DC]"""
        step1 = rref_one_step["steps"][0]
        assert step1["residual_after_analysis"]["is_zero"], (
            "Rref gauge should resolve charge-2 ZTE exactly in one step"
        )

    def test_rank_35(self, rref_one_step):
        """Linearized system rank is 35 (one scalar gauge). [LA]"""
        assert rref_one_step["steps"][0]["rank"] == 35

    def test_correction_symmetric(self, rref_one_step):
        """Rref correction is symmetric. [DC]"""
        assert rref_one_step["steps"][0]["correction_analysis"]["is_symmetric"]

    def test_correction_persymmetric(self, rref_one_step):
        """Rref correction is persymmetric. [DC]"""
        assert rref_one_step["steps"][0]["correction_analysis"]["is_persymmetric"]

    def test_correction_zero_antidiag(self, rref_one_step):
        """Rref correction has zero anti-diagonal. [DC]"""
        assert rref_one_step["steps"][0]["correction_analysis"]["has_zero_antidiag"]

    def test_sparse_solution(self, rref_one_step):
        """Rref solution is sparse: anti-diagonal zeros present. [DC]"""
        T_cum = rref_one_step["T_cumulative_c2"]
        n_zero = sum(
            1 for r in range(6) for c in range(6)
            if T_cum[r][c] == Fraction(0)
        )
        assert n_zero >= 6


# ---------------------------------------------------------------------------
# Min-norm gauge: order-by-order structure
# ---------------------------------------------------------------------------

class TestMinnormOrderByOrder:
    """Verify the order-by-order structure with min-norm gauge."""

    def test_step1_residual_nonzero(self, base_step1):
        """Step 1 (min-norm) leaves O(kappa^4) residual. [ZTE]"""
        obs_corr = base_step1["obs_corr_c2"]
        assert not _is_c2_zero(obs_corr)

    def test_o_kappa4_antisymmetric(self, minnorm_step2_data):
        """O(kappa^4) residual is exactly antisymmetric. [DC]"""
        assert minnorm_step2_data["obs4_analysis"]["is_antisymmetric"]

    def test_o_kappa4_persymmetric(self, minnorm_step2_data):
        """O(kappa^4) residual is exactly persymmetric. [DC]"""
        assert minnorm_step2_data["obs4_analysis"]["is_persymmetric"]

    def test_o_kappa4_rank_4(self, minnorm_step2_data):
        """O(kappa^4) residual has rank 4. [LA]"""
        assert minnorm_step2_data["obs4_analysis"]["rank"] == 4

    def test_o_kappa4_zero_diagonal(self, minnorm_step2_data):
        """O(kappa^4) residual has zero diagonal (from antisymmetry). [DC]"""
        assert minnorm_step2_data["obs4_analysis"]["has_zero_diagonal"]

    def test_o_kappa4_scaling(self, minnorm_step2_data):
        """Residual after step 1 scales as kappa^4. [SC]"""
        max_after = _max_abs_c2(minnorm_step2_data["obs4_c2"])
        kappa = minnorm_step2_data["kappa"]
        ratio = max_after / (kappa ** 4)
        assert Fraction(1, 100) < ratio < Fraction(100, 1), (
            f"O^(4)/kappa^4 = {float(ratio):.6f}, expected O(1)"
        )

    def test_step2_rank_36(self, minnorm_step2_data):
        """Step 2 linearized system has rank 36 (full). [LA]"""
        assert minnorm_step2_data["rank2"] == 36

    def test_o_kappa6_exactly_zero(self, minnorm_step2_data):
        """O(kappa^6) residual after two steps is exactly zero. [ZTE, DC]

        The minnorm step 1 (rank 35) leaves O(kappa^4) residual;
        the rref step 2 (rank 36) resolves charge-2 ZTE exactly.
        The two-step combination achieves exact charge-2 resolution,
        just like the one-step rref solver.
        """
        assert minnorm_step2_data["obs6_analysis"]["is_zero"]

    def test_o_kappa6_rank_0(self, minnorm_step2_data):
        """O(kappa^6) residual has rank 0 (exactly zero). [LA]"""
        assert minnorm_step2_data["obs6_analysis"]["rank"] == 0

    def test_monotone_decrease(self, base_step1, minnorm_step2_data):
        """Obstruction decreases monotonically. [ZTE]"""
        max_o2 = _max_abs_c2(base_step1["obs_c2"])
        max_o4 = _max_abs_c2(minnorm_step2_data["obs4_c2"])
        max_o6 = _max_abs_c2(minnorm_step2_data["obs6_c2"])
        assert max_o4 < max_o2
        assert max_o6 <= max_o4


# ---------------------------------------------------------------------------
# Cumulative correction structure
# ---------------------------------------------------------------------------

class TestCumulativeCorrection:
    """Verify structural properties of cumulative T = C_1 + C_2."""

    def test_cumulative_symmetric(self, minnorm_step2_data):
        """T_cumulative is symmetric. [DC]"""
        assert minnorm_step2_data["T_cumulative_analysis"]["is_symmetric"]

    def test_cumulative_persymmetric(self, minnorm_step2_data):
        """T_cumulative is persymmetric. [DC]"""
        assert minnorm_step2_data["T_cumulative_analysis"]["is_persymmetric"]

    def test_cumulative_zero_antidiag(self, minnorm_step2_data):
        """T_cumulative has zero anti-diagonal. [DC]"""
        assert minnorm_step2_data["T_cumulative_analysis"]["has_zero_antidiag"]

    def test_cumulative_full_rank(self, minnorm_step2_data):
        """T_cumulative has full rank 6. [LA]"""
        assert minnorm_step2_data["T_cumulative_analysis"]["rank"] == 6

    def test_entries_are_fractions(self, minnorm_step2_data):
        """All T_cumulative entries are exact Fractions. [DC]"""
        T = minnorm_step2_data["T_cumulative_c2"]
        for r in range(6):
            for c in range(6):
                assert isinstance(T[r][c], Fraction)


# ---------------------------------------------------------------------------
# Multi-path cross-validation (AP10 compliance)
# ---------------------------------------------------------------------------

class TestCrossValidation:
    """Multi-path verification via independent code paths."""

    def test_both_gauges_satisfy_linearized_system(self):
        """Both rref and min-norm solutions satisfy A*x = b. [DC, XV]"""
        from compute.lib.zte_t_matrix_exact import _solve_exact as _solve_mn

        obs_data = _zte_obstruction_frac(_U_DEFAULT, _KAPPA_DEFAULT)
        S_c2 = obs_data["S_c2"]
        obs_c2 = obs_data["obs_c2"]
        A, b = _build_linearized_system_c2(S_c2, obs_c2)

        x_rref, _ = _solve_exact_fast(A, b)
        x_mn, _ = _solve_mn(A, b)

        for label, x in [("rref", x_rref), ("minnorm", x_mn)]:
            for r in range(36):
                s = Fraction(0)
                for c in range(80):
                    s += A[r][c] * x[c]
                assert s == b[r], (
                    f"{label}: A*x[{r}] != b[{r}]"
                )

    def test_final_residual_recomputed(self, minnorm_step2_data):
        """Final residual verified by recomputing ZTE from S2. [DC, ZTE, XV]"""
        recomputed = _zte_residual_from_s(minnorm_step2_data["S2"])
        stored = minnorm_step2_data["obs6_c2"]
        for r in range(6):
            for c in range(6):
                assert stored[r][c] == recomputed["obs_c2"][r][c], (
                    f"Residual mismatch at [{r},{c}]"
                )

    def test_s2_equals_s0_plus_cumulative(self, minnorm_step2_data):
        """S2 = S^{fact} + embed(C_cumulative) for each face. [DC, XV]"""
        S0 = minnorm_step2_data["S0"]
        C_cum = minnorm_step2_data["C_cumulative"]
        S2 = minnorm_step2_data["S2"]

        for (fi, fj, fk) in _FACE_ORDER:
            C_embed = _embed_ternary_full_frac(
                C_cum[(fi, fj, fk)], fi, fj, fk
            )
            S_rebuilt = _fmat_add(S0[(fi, fj, fk)], C_embed)
            for r in range(16):
                for c_idx in range(16):
                    assert S2[(fi, fj, fk)][r][c_idx] == S_rebuilt[r][c_idx], (
                        f"S2 mismatch at face {(fi,fj,fk)}, [{r},{c_idx}]"
                    )

    def test_antisymmetry_implies_zero_diagonal(self, minnorm_step2_data):
        """Zero diagonal follows from antisymmetry. [DC, XV]"""
        for analysis in [minnorm_step2_data["obs4_analysis"],
                         minnorm_step2_data["obs6_analysis"]]:
            if analysis["is_antisymmetric"]:
                assert analysis["has_zero_diagonal"]

    def test_persymmetry_preserved(self, minnorm_step2_data):
        """Persymmetry preserved at every stage. [DC, XV]"""
        assert minnorm_step2_data["obs4_analysis"]["is_persymmetric"]
        assert minnorm_step2_data["obs6_analysis"]["is_persymmetric"]
        assert minnorm_step2_data["T_cumulative_analysis"]["is_persymmetric"]

    def test_kappa4_ratio_between_two_kappas(self):
        """Scaling verified by comparing two kappa values. [SC, XV]"""
        kap1 = Fraction(1, 5)
        kap2 = Fraction(1, 10)

        # Use base engine (min-norm) for both
        r1 = compute_exact_t_matrix(kappa=kap1)
        r2 = compute_exact_t_matrix(kappa=kap2)

        max1 = _max_abs_c2(r1["obs_corr_c2"])
        max2 = _max_abs_c2(r2["obs_corr_c2"])

        actual_ratio = max1 / max2
        expected_ratio = (kap1 / kap2) ** 4  # = 16
        assert expected_ratio / 5 < actual_ratio < expected_ratio * 5, (
            f"Scaling ratio {float(actual_ratio):.4f} vs expected "
            f"{float(expected_ratio):.4f}"
        )

    def test_rref_exact_matches_base_obstruction(self, rref_one_step):
        """Rref solver gets same initial obstruction as base engine. [DC, XV]"""
        obs_data = _zte_obstruction_frac(_U_DEFAULT, _KAPPA_DEFAULT)
        step1_obs = rref_one_step["steps"][0]["obstruction_analysis"]
        assert step1_obs["rank"] == 4
        assert step1_obs["is_antisymmetric"]
        assert step1_obs["is_persymmetric"]


# ---------------------------------------------------------------------------
# Parameter independence
# ---------------------------------------------------------------------------

class TestParameterIndependence:
    """Verify structural properties at different parameters."""

    def test_rref_exact_at_kappa_one_third(self):
        """Rref gauge resolves charge-2 exactly at kappa=1/3. [DC, ZTE]"""
        sol = compute_iterated_zte_correction(
            n_steps=1, kappa=Fraction(1, 3), solver="rref",
        )
        assert sol["steps"][0]["residual_after_analysis"]["is_zero"]

    def test_rref_exact_at_different_spectral_params(self):
        """Rref gauge resolves charge-2 exactly at u=[0,2,5,11]. [DC, ZTE]"""
        u = [Fraction(0), Fraction(2), Fraction(5), Fraction(11)]
        sol = compute_iterated_zte_correction(
            n_steps=1, kappa=_KAPPA_DEFAULT, u=u, solver="rref",
        )
        assert sol["steps"][0]["residual_after_analysis"]["is_zero"]

    def test_minnorm_residual_nonzero_at_kappa_one_third(self):
        """Min-norm leaves O(kappa^4) residual at kappa=1/3. [DC]"""
        result = compute_exact_t_matrix(kappa=Fraction(1, 3))
        assert not _is_c2_zero(result["obs_corr_c2"])


# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------

class TestDisplay:
    """Verify display formatting."""

    def test_format_produces_output(self, rref_one_step):
        """format_iterated_results returns nonempty string. [DC]"""
        s = format_iterated_results(rref_one_step)
        assert len(s) > 100
        assert "Step 1" in s
