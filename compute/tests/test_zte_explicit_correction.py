"""Tests for the explicit ZTE correction engine.

Verifies the construction of the explicit correction T such that
S^{corr} = S^{fact} + T satisfies the Zamolodchikov tetrahedron equation
to machine precision.

Key results verified:
  1. Newton iteration converges in 3 steps (improvement > 10^6).
  2. T_c2 is symmetric (complementary to antisymmetric O).
  3. T_c2 is persymmetric (particle-hole duality J T J = T).
  4. T_c2 has full rank 6 on the charge-2 sector.
  5. Leading-order T is factorizable (ternary fraction < 1e-4).
  6. Obstruction O_2 is antisymmetric, rank 4, persymmetric.
  7. Gauge freedom: 45-dim at step 0, then 44-dim at steps 1,2.
  8. S4 trivial fraction of T is small (< 5%).
  9. No higher-order obstruction: iteration converges monotonically.
 10. Convergence is robust across kappa values.

VERIFIED sources:
[DC]  Direct computation via numpy linear algebra.
[ZTE] Zamolodchikov tetrahedron equation (face formulation on V^4).
[NI]  Newton iteration on the linearized ZTE.
[KV]  Kapranov-Voevodsky: permutation limit satisfies ZTE.
"""

import numpy as np
import pytest

from compute.lib.zte_explicit_correction import (
    convergence_analysis,
    gauge_freedom_analysis,
    higher_order_obstruction,
    newton_zte_correction,
    normalized_obstruction,
    run_explicit_correction_verification,
    s4_decomposition,
)


# ---------------------------------------------------------------------------
# Test parameters
# ---------------------------------------------------------------------------

_U_DEFAULT = [0.0, 1.0, 3.0, 7.0]
_KAPPA_DEFAULT = -0.1


# ---------------------------------------------------------------------------
# Obstruction structure tests
# ---------------------------------------------------------------------------

class TestObstructionStructure:
    """Verify structural properties of the ZTE obstruction O_2."""

    def test_obstruction_antisymmetric(self):
        """O_2 = lim O/kappa^2 is antisymmetric."""
        obs = normalized_obstruction(_U_DEFAULT)
        assert obs["is_antisymmetric"], "O_2 should be antisymmetric"

    def test_obstruction_rank_4(self):
        """O_2 has rank 4 (kernel dimension 2)."""
        obs = normalized_obstruction(_U_DEFAULT)
        assert obs["rank"] == 4, f"Expected rank 4, got {obs['rank']}"

    def test_obstruction_persymmetric(self):
        """O_2 is persymmetric: J O_2 J = O_2."""
        obs = normalized_obstruction(_U_DEFAULT)
        assert obs["is_persymmetric"], "O_2 should be persymmetric"

    def test_obstruction_nonzero(self):
        """O_2 is nonzero (ZTE fails at O(kappa^2))."""
        obs = normalized_obstruction(_U_DEFAULT)
        assert obs["norm"] > 0.1, f"O_2 norm too small: {obs['norm']}"

    def test_obstruction_kappa_independent(self):
        """O_2 is approximately kappa-independent."""
        obs = normalized_obstruction(_U_DEFAULT)
        assert obs["kappa_independence"] < 0.01, (
            f"O_2 not kappa-independent: rel diff = {obs['kappa_independence']}"
        )

    def test_obstruction_pure_imaginary_eigenvalues(self):
        """Antisymmetric O_2 has pure imaginary eigenvalues."""
        obs = normalized_obstruction(_U_DEFAULT)
        eigs = obs["eigenvalues"]
        for e in eigs:
            # Eigenvalues should be either ~0 or pure imaginary
            if abs(e) > 1e-6:
                assert abs(e.real) < 0.01 * abs(e.imag), (
                    f"Eigenvalue {e} not pure imaginary"
                )


# ---------------------------------------------------------------------------
# Newton iteration convergence tests
# ---------------------------------------------------------------------------

class TestNewtonConvergence:
    """Verify convergence of the Newton iteration."""

    def test_three_iterations_suffice(self):
        """Three Newton iterations reduce obstruction by > 10^6."""
        sol = newton_zte_correction(_KAPPA_DEFAULT, _U_DEFAULT, n_iters=3)
        assert sol["improvement"] > 1e6, (
            f"Improvement {sol['improvement']:.2e} < 10^6"
        )

    def test_obstruction_decreases_monotonically(self):
        """Obstruction decreases at each Newton step."""
        sol = newton_zte_correction(_KAPPA_DEFAULT, _U_DEFAULT, n_iters=3)
        obs_vals = [sol["obs_orig"]] + [
            d["obs_after"] for d in sol["per_iteration"]
        ]
        for i in range(len(obs_vals) - 1):
            assert obs_vals[i + 1] < obs_vals[i], (
                f"Obstruction increased at step {i}: "
                f"{obs_vals[i]:.4e} -> {obs_vals[i+1]:.4e}"
            )

    def test_first_step_rank_35(self):
        """First Newton step has rank 35 (one missing = scalar gauge)."""
        sol = newton_zte_correction(_KAPPA_DEFAULT, _U_DEFAULT, n_iters=1)
        assert sol["per_iteration"][0]["rank"] == 35, (
            f"Expected rank 35, got {sol['per_iteration'][0]['rank']}"
        )

    def test_second_step_rank_36(self):
        """Second Newton step has full rank 36."""
        sol = newton_zte_correction(_KAPPA_DEFAULT, _U_DEFAULT, n_iters=2)
        assert sol["per_iteration"][1]["rank"] == 36, (
            f"Expected rank 36, got {sol['per_iteration'][1]['rank']}"
        )

    def test_convergence_at_small_kappa(self):
        """Newton iteration converges at small kappa."""
        sol = newton_zte_correction(-0.01, _U_DEFAULT, n_iters=3)
        assert sol["improvement"] > 1e6, (
            f"Improvement at kappa=-0.01: {sol['improvement']:.2e}"
        )

    def test_convergence_at_moderate_kappa(self):
        """Newton iteration converges at moderate kappa."""
        sol = newton_zte_correction(-0.2, _U_DEFAULT, n_iters=3)
        assert sol["improvement"] > 1e6, (
            f"Improvement at kappa=-0.2: {sol['improvement']:.2e}"
        )

    def test_final_obstruction_below_threshold(self):
        """Final obstruction is < 1e-8 * original."""
        sol = newton_zte_correction(_KAPPA_DEFAULT, _U_DEFAULT, n_iters=3)
        assert sol["obs_final"] < 1e-8 * sol["obs_orig"], (
            f"Final obstruction too large: {sol['obs_final']:.4e} vs "
            f"threshold {1e-8 * sol['obs_orig']:.4e}"
        )


# ---------------------------------------------------------------------------
# Structural properties of T
# ---------------------------------------------------------------------------

class TestCorrectionStructure:
    """Verify structural properties of the correction T."""

    @pytest.fixture(scope="class")
    def sol(self):
        return newton_zte_correction(_KAPPA_DEFAULT, _U_DEFAULT, n_iters=3)

    def test_t_symmetric(self, sol):
        """T_c2 is symmetric (T = T^T)."""
        assert sol["structural"]["is_symmetric"], (
            f"T_c2 not symmetric: asym_norm={sol['structural']['asym_norm']:.4e}"
        )

    def test_t_persymmetric(self, sol):
        """T_c2 is persymmetric (J T J = T)."""
        assert sol["structural"]["is_persymmetric"], (
            f"T_c2 not persymmetric: error={sol['structural']['persymmetry_error']:.4e}"
        )

    def test_t_full_rank(self, sol):
        """T_c2 has full rank 6."""
        assert sol["structural"]["rank"] == 6, (
            f"Expected rank 6, got {sol['structural']['rank']}"
        )

    def test_t_factorizable_leading(self, sol):
        """Leading-order T is factorizable on V^4."""
        assert sol["structural"]["is_factorizable"], (
            f"T not factorizable: ternary fraction = "
            f"{sol['structural']['v4_ternary_fraction']:.6f}"
        )

    def test_t_nonzero_eigenvalues(self, sol):
        """T_c2 has 6 nonzero eigenvalues (both positive and negative)."""
        eigs = sol["structural"]["eigenvalues"]
        assert len(eigs) == 6
        n_pos = sum(1 for e in eigs if e > 1e-10)
        n_neg = sum(1 for e in eigs if e < -1e-10)
        assert n_pos >= 1 and n_neg >= 1, (
            f"Expected mixed-sign eigenvalues, got {eigs}"
        )

    def test_t_nonzero_determinant(self, sol):
        """T_c2 has nonzero determinant (full rank confirmation)."""
        assert abs(sol["structural"]["determinant"]) > 1e-10, (
            f"Determinant too small: {sol['structural']['determinant']}"
        )

    def test_complementary_symmetry(self, sol):
        """O is antisymmetric, T is symmetric (complementary)."""
        obs = normalized_obstruction(_U_DEFAULT)
        assert obs["is_antisymmetric"], "O should be antisymmetric"
        assert sol["structural"]["is_symmetric"], "T should be symmetric"


# ---------------------------------------------------------------------------
# Non-factorizability tests
# ---------------------------------------------------------------------------

class TestNonFactorizability:
    """Verify factorizability properties of T."""

    def test_leading_factorizable(self):
        """First Newton increment is completely factorizable."""
        sol = newton_zte_correction(_KAPPA_DEFAULT, _U_DEFAULT, n_iters=1)
        nf = sol["per_iteration"][0]["nf_avg"]
        assert nf < 1e-6, (
            f"First increment should be factorizable: nf = {nf:.6e}"
        )

    def test_second_increment_factorizable(self):
        """Second Newton increment is also factorizable."""
        sol = newton_zte_correction(_KAPPA_DEFAULT, _U_DEFAULT, n_iters=2)
        nf = sol["per_iteration"][1]["nf_avg"]
        assert nf < 1e-4, (
            f"Second increment should be near-factorizable: nf = {nf:.6e}"
        )

    def test_v4_total_factorizable(self):
        """Cumulative T on V^4 is factorizable at leading order."""
        sol = newton_zte_correction(_KAPPA_DEFAULT, _U_DEFAULT, n_iters=3)
        assert sol["structural"]["v4_ternary_fraction"] < 1e-3, (
            f"V4 ternary fraction = {sol['structural']['v4_ternary_fraction']}"
        )


# ---------------------------------------------------------------------------
# Gauge freedom tests
# ---------------------------------------------------------------------------

class TestGaugeFreedom:
    """Verify gauge freedom analysis."""

    def test_null_dim_45(self):
        """First Newton step has 45-dimensional null space."""
        gf = gauge_freedom_analysis(_KAPPA_DEFAULT, _U_DEFAULT)
        assert gf["null_dim"] == 45, (
            f"Expected null dim 45, got {gf['null_dim']}"
        )

    def test_rank_35(self):
        """First Newton step has rank 35."""
        gf = gauge_freedom_analysis(_KAPPA_DEFAULT, _U_DEFAULT)
        assert gf["rank"] == 35, (
            f"Expected rank 35, got {gf['rank']}"
        )

    def test_null_space_has_mixed_ternary(self):
        """Null space contains both factorizable and ternary directions."""
        gf = gauge_freedom_analysis(_KAPPA_DEFAULT, _U_DEFAULT)
        fracs = gf["null_ternary_fractions"]
        has_low = any(f < 0.1 for f in fracs)
        has_high = any(f > 0.3 for f in fracs)
        assert has_low and has_high, (
            f"Null space should have mixed ternary content: "
            f"min={min(fracs):.4f}, max={max(fracs):.4f}"
        )


# ---------------------------------------------------------------------------
# S4 decomposition tests
# ---------------------------------------------------------------------------

class TestS4Decomposition:
    """Verify S4 representation-theoretic decomposition."""

    def test_trivial_fraction_small(self):
        """S4 trivial component is small (< 5% of total)."""
        sol = newton_zte_correction(_KAPPA_DEFAULT, _U_DEFAULT, n_iters=3)
        s4 = s4_decomposition(sol["T_c2"])
        assert s4["trivial_fraction"] < 0.05, (
            f"S4 trivial fraction {s4['trivial_fraction']:.4f} > 5%"
        )

    def test_nontrivial_dominates(self):
        """S4 non-trivial component dominates T."""
        sol = newton_zte_correction(_KAPPA_DEFAULT, _U_DEFAULT, n_iters=3)
        s4 = s4_decomposition(sol["T_c2"])
        assert s4["nontrivial_fraction"] > 0.95, (
            f"S4 non-trivial fraction {s4['nontrivial_fraction']:.4f} < 95%"
        )


# ---------------------------------------------------------------------------
# Higher-order obstruction tests
# ---------------------------------------------------------------------------

class TestHigherOrder:
    """Verify no higher-order cohomological obstruction."""

    def test_no_obstruction_at_any_order(self):
        """Newton iteration converges monotonically (no obstruction)."""
        ho = higher_order_obstruction(_KAPPA_DEFAULT, _U_DEFAULT)
        assert ho["no_higher_obstruction"], (
            "Higher-order obstruction detected"
        )

    def test_each_step_improves(self):
        """Each Newton step reduces the obstruction."""
        ho = higher_order_obstruction(_KAPPA_DEFAULT, _U_DEFAULT)
        for d in ho["orders"]:
            assert d["obs_after"] < d["obs_before"], (
                f"Step {d['iteration']}: obs increased "
                f"{d['obs_before']:.4e} -> {d['obs_after']:.4e}"
            )


# ---------------------------------------------------------------------------
# Cross-kappa consistency tests
# ---------------------------------------------------------------------------

class TestCrossKappaConsistency:
    """Verify consistency across different kappa values."""

    @pytest.mark.parametrize("kappa", [-0.01, -0.05, -0.1, -0.2])
    def test_convergence_at_kappa(self, kappa):
        """Newton iteration converges at this kappa value."""
        sol = newton_zte_correction(kappa, _U_DEFAULT, n_iters=3)
        assert sol["improvement"] > 1e5, (
            f"Improvement at kappa={kappa}: {sol['improvement']:.2e}"
        )

    @pytest.mark.parametrize("kappa", [-0.01, -0.05, -0.1])
    def test_symmetry_preserved(self, kappa):
        """T is symmetric at all kappa values."""
        sol = newton_zte_correction(kappa, _U_DEFAULT, n_iters=3)
        assert sol["structural"]["is_symmetric"], (
            f"T not symmetric at kappa={kappa}"
        )

    @pytest.mark.parametrize("kappa", [-0.01, -0.05, -0.1])
    def test_persymmetry_preserved(self, kappa):
        """T is persymmetric at all kappa values."""
        sol = newton_zte_correction(kappa, _U_DEFAULT, n_iters=3)
        assert sol["structural"]["is_persymmetric"], (
            f"T not persymmetric at kappa={kappa}"
        )


# ---------------------------------------------------------------------------
# Master verification test
# ---------------------------------------------------------------------------

class TestMasterVerification:
    """Run the complete verification suite."""

    def test_master_suite(self):
        """Master verification passes all checks."""
        results = run_explicit_correction_verification(
            kappa=-0.1, u_vals=_U_DEFAULT
        )
        assert results["summary"]["T_exists"], "T should exist"
        assert results["summary"]["T_is_symmetric"], "T should be symmetric"
        assert results["summary"]["T_is_persymmetric"], "T should be persymmetric"
        assert results["summary"]["obstruction_antisymmetric"], (
            "O should be antisymmetric"
        )
        assert results["summary"]["obstruction_rank"] == 4, (
            "O should have rank 4"
        )
        assert results["summary"]["no_higher_obstruction"], (
            "No higher obstruction"
        )
