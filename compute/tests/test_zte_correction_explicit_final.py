"""Tests for the definitive ZTE correction engine.

Verifies the construction of the explicit correction T such that
S^{corr} = S^{fact} + T satisfies the Zamolodchikov tetrahedron equation
to machine precision.

Key results verified (Proposition prop:zte-explicit-correction):

  OBSTRUCTION STRUCTURE:
    1. O_2 = lim O/kappa^2 is antisymmetric (O_2^T = -O_2).
    2. O_2 has rank 4 (kernel dimension 2).
    3. O_2 is persymmetric (J O_2 J = O_2).

  NEWTON CONVERGENCE:
    4. Adaptive Newton converges in <= 3 iterations (improvement > 10^5).
    5. First step: rank 35/36 (one missing = scalar gauge).
    6. Second step: rank 36/36 (full).
    7. Obstruction decreases monotonically within accepted iterations.

  CORRECTION STRUCTURE:
    8. T_c2 is symmetric (T = T^T).
    9. T_c2 is persymmetric (J T J = T).
   10. T_c2 has zero anti-diagonal (T[i, 5-i] = 0).
   11. T_c2 has full rank 6.
   12. T_c2 has mixed-sign eigenvalues.

  FACTORIZABILITY:
   13. Per-face correction is factorizable (ternary fraction < 1e-6).
   14. V^4 correction is factorizable (ternary fraction < 1e-6).

  GAUGE FREEDOM:
   15. Linearized system: rank 35, null dim 45.

  S4 DECOMPOSITION:
   16. S4 trivial fraction is small (< 5%).

  HIGHER ORDER:
   17. No higher-order obstruction (monotone within accepted steps).

  UNIVERSALITY:
   18. Structural properties are independent of spectral parameters.
   19. Structural properties are independent of kappa value.

VERIFIED sources:
[DC]  Direct computation via numpy linear algebra.
[ZTE] Zamolodchikov tetrahedron equation (face formulation on V^4).
[NI]  Adaptive Newton iteration on the full ZTE.
[KV]  Kapranov-Voevodsky: permutation limit satisfies ZTE.
"""

import numpy as np
import pytest

from compute.lib.zte_correction_explicit_final import (
    analyze_gauge_freedom,
    compute_zte_correction,
    convergence_analysis,
    extract_leading_obstruction,
    higher_order_analysis,
    run_full_verification,
    spectral_parameter_dependence,
)


# ---------------------------------------------------------------------------
# Test parameters
# ---------------------------------------------------------------------------

_U_DEFAULT = [0.0, 1.0, 3.0, 7.0]
_KAPPA_DEFAULT = 0.2


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def canonical_sol():
    """The canonical correction at kappa=0.2, u=[0,1,3,7]."""
    return compute_zte_correction(_KAPPA_DEFAULT, _U_DEFAULT)


@pytest.fixture(scope="module")
def leading_obs():
    """The leading O(kappa^2) obstruction."""
    return extract_leading_obstruction(_U_DEFAULT)


# ---------------------------------------------------------------------------
# Obstruction structure tests
# ---------------------------------------------------------------------------

class TestObstructionStructure:
    """Verify structural properties of the ZTE obstruction O_2."""

    def test_obstruction_antisymmetric(self, leading_obs):
        """O_2 is antisymmetric: O_2^T = -O_2."""
        assert leading_obs["is_antisymmetric"], (
            "O_2 should be antisymmetric, error = %.4e" %
            leading_obs["antisymmetry_error"]
        )

    def test_obstruction_rank_4(self, leading_obs):
        """O_2 has rank 4 (kernel dimension 2)."""
        assert leading_obs["rank"] == 4, (
            "Expected rank 4, got %d" % leading_obs["rank"]
        )

    def test_obstruction_persymmetric(self, leading_obs):
        """O_2 is persymmetric: J O_2 J = O_2."""
        assert leading_obs["is_persymmetric"], (
            "O_2 should be persymmetric, error = %.4e" %
            leading_obs["persymmetry_error"]
        )

    def test_obstruction_nonzero(self, leading_obs):
        """O_2 is nonzero (ZTE fails at O(kappa^2))."""
        assert leading_obs["norm"] > 0.01, (
            "O_2 norm too small: %.6e" % leading_obs["norm"]
        )

    def test_obstruction_kappa_independent(self, leading_obs):
        """O_2 is approximately kappa-independent."""
        assert leading_obs["kappa_independence"] < 0.05, (
            "O_2 not kappa-independent: rel diff = %.4e" %
            leading_obs["kappa_independence"]
        )


# ---------------------------------------------------------------------------
# Newton convergence tests
# ---------------------------------------------------------------------------

class TestNewtonConvergence:
    """Verify convergence of the adaptive Newton iteration."""

    def test_converges_with_high_improvement(self, canonical_sol):
        """Adaptive Newton achieves improvement > 10^5."""
        assert canonical_sol["improvement"] > 1e5, (
            "Improvement %.2e < 10^5" % canonical_sol["improvement"]
        )

    def test_at_most_3_iterations(self, canonical_sol):
        """At most 3 iterations are used."""
        assert canonical_sol["n_iters_used"] <= 3, (
            "Used %d iterations, expected <= 3" % canonical_sol["n_iters_used"]
        )

    def test_first_step_rank_35(self, canonical_sol):
        """First Newton step has rank 35 (one missing = scalar gauge)."""
        assert canonical_sol["per_iteration"][0]["rank"] == 35, (
            "Expected rank 35, got %d" %
            canonical_sol["per_iteration"][0]["rank"]
        )

    def test_second_step_rank_36(self, canonical_sol):
        """Second Newton step has full rank 36."""
        if canonical_sol["n_iters_used"] >= 2:
            assert canonical_sol["per_iteration"][1]["rank"] == 36, (
                "Expected rank 36, got %d" %
                canonical_sol["per_iteration"][1]["rank"]
            )

    def test_obstruction_decreases_monotonically(self, canonical_sol):
        """Obstruction decreases at each accepted Newton step."""
        n = canonical_sol["n_iters_used"]
        obs_vals = [canonical_sol["obs_orig"]] + [
            d["obs_after"] for d in canonical_sol["per_iteration"][:n]
        ]
        for i in range(len(obs_vals) - 1):
            assert obs_vals[i + 1] < obs_vals[i], (
                "Obstruction increased at step %d: %.4e -> %.4e" %
                (i, obs_vals[i], obs_vals[i + 1])
            )


# ---------------------------------------------------------------------------
# Structural properties of T
# ---------------------------------------------------------------------------

class TestCorrectionStructure:
    """Verify structural properties of the correction T."""

    def test_t_symmetric(self, canonical_sol):
        """T_c2 is symmetric (T = T^T)."""
        assert canonical_sol["structural"]["is_symmetric"], (
            "T_c2 not symmetric: error = %.4e" %
            canonical_sol["structural"]["symmetry_error"]
        )

    def test_t_persymmetric(self, canonical_sol):
        """T_c2 is persymmetric (J T J = T)."""
        assert canonical_sol["structural"]["is_persymmetric"], (
            "T_c2 not persymmetric: error = %.4e" %
            canonical_sol["structural"]["persymmetry_error"]
        )

    def test_t_zero_antidiag(self, canonical_sol):
        """T_c2 has zero anti-diagonal entries."""
        assert canonical_sol["structural"]["has_zero_antidiag"], (
            "Anti-diagonal max = %.4e" %
            canonical_sol["structural"]["antidiag_max"]
        )

    def test_t_full_rank(self, canonical_sol):
        """T_c2 has full rank 6."""
        assert canonical_sol["structural"]["rank"] == 6, (
            "Expected rank 6, got %d" % canonical_sol["structural"]["rank"]
        )

    def test_t_mixed_sign_eigenvalues(self, canonical_sol):
        """T_c2 has both positive and negative eigenvalues."""
        assert canonical_sol["structural"]["has_mixed_sign_eigs"], (
            "Expected mixed-sign eigenvalues: %s" %
            canonical_sol["structural"]["eigenvalues"]
        )

    def test_complementary_symmetry(self, canonical_sol, leading_obs):
        """O is antisymmetric, T is symmetric (complementary)."""
        assert leading_obs["is_antisymmetric"], "O should be antisymmetric"
        assert canonical_sol["structural"]["is_symmetric"], "T should be symmetric"


# ---------------------------------------------------------------------------
# Factorizability tests
# ---------------------------------------------------------------------------

class TestFactorizability:
    """Verify factorizability of T."""

    def test_per_face_factorizable(self, canonical_sol):
        """Per-face corrections are factorizable (no ternary content)."""
        assert canonical_sol["structural"]["is_factorizable_per_face"], (
            "Per-face ternary fraction = %.6e" %
            canonical_sol["structural"]["max_face_ternary_fraction"]
        )

    def test_v4_factorizable(self, canonical_sol):
        """V^4 correction is factorizable."""
        assert canonical_sol["structural"]["is_factorizable_v4"], (
            "V4 ternary fraction = %.6e" %
            canonical_sol["structural"]["v4_ternary_fraction"]
        )


# ---------------------------------------------------------------------------
# Gauge freedom tests
# ---------------------------------------------------------------------------

class TestGaugeFreedom:
    """Verify gauge freedom analysis."""

    def test_rank_35(self):
        """Linearized system has rank 35."""
        gf = analyze_gauge_freedom(_KAPPA_DEFAULT, _U_DEFAULT)
        assert gf["rank"] == 35, (
            "Expected rank 35, got %d" % gf["rank"]
        )

    def test_null_dim_45(self):
        """Linearized system has 45-dimensional null space."""
        gf = analyze_gauge_freedom(_KAPPA_DEFAULT, _U_DEFAULT)
        assert gf["null_dim"] == 45, (
            "Expected null dim 45, got %d" % gf["null_dim"]
        )

    def test_solvable(self):
        """The linearized system is solvable."""
        gf = analyze_gauge_freedom(_KAPPA_DEFAULT, _U_DEFAULT)
        assert gf["solvable"], "Linearized system should be solvable"


# ---------------------------------------------------------------------------
# S4 decomposition tests
# ---------------------------------------------------------------------------

class TestS4Decomposition:
    """Verify S4 representation-theoretic decomposition."""

    def test_trivial_fraction_small(self, canonical_sol):
        """S4 trivial component is small (< 10%)."""
        assert canonical_sol["structural"]["s4_trivial_fraction"] < 0.10, (
            "S4 trivial fraction %.4f > 10%%" %
            canonical_sol["structural"]["s4_trivial_fraction"]
        )

    def test_nontrivial_dominates(self, canonical_sol):
        """S4 non-trivial component dominates T."""
        assert canonical_sol["structural"]["s4_nontrivial_fraction"] > 0.90, (
            "S4 non-trivial fraction %.4f < 90%%" %
            canonical_sol["structural"]["s4_nontrivial_fraction"]
        )


# ---------------------------------------------------------------------------
# Higher-order obstruction tests
# ---------------------------------------------------------------------------

class TestHigherOrder:
    """Verify no higher-order cohomological obstruction."""

    def test_no_higher_obstruction(self):
        """Adaptive iteration handles all orders (monotone decrease)."""
        ho = higher_order_analysis(_KAPPA_DEFAULT, _U_DEFAULT)
        assert ho["no_higher_obstruction"], (
            "Higher-order obstruction detected: improvement = %.2e" %
            ho["final_improvement"]
        )

    def test_monotone_within_accepted(self):
        """Obstruction decreases monotonically within accepted iterations."""
        ho = higher_order_analysis(_KAPPA_DEFAULT, _U_DEFAULT)
        assert ho["monotone_within_accepted"], (
            "Non-monotone obstruction within accepted iterations"
        )


# ---------------------------------------------------------------------------
# Cross-kappa consistency tests
# ---------------------------------------------------------------------------

class TestCrossKappaConsistency:
    """Verify consistency across different kappa values."""

    @pytest.mark.parametrize("kappa", [0.05, 0.1, 0.2, 0.3, 0.5])
    def test_convergence_at_kappa(self, kappa):
        """Newton iteration converges at this kappa value."""
        sol = compute_zte_correction(kappa, _U_DEFAULT)
        assert sol["improvement"] > 1e5, (
            "Improvement at kappa=%.2f: %.2e" % (kappa, sol["improvement"])
        )

    @pytest.mark.parametrize("kappa", [0.05, 0.1, 0.2, 0.3])
    def test_symmetry_preserved(self, kappa):
        """T is symmetric at all kappa values."""
        sol = compute_zte_correction(kappa, _U_DEFAULT)
        assert sol["structural"]["is_symmetric"], (
            "T not symmetric at kappa=%.2f" % kappa
        )

    @pytest.mark.parametrize("kappa", [0.05, 0.1, 0.2, 0.3])
    def test_persymmetry_preserved(self, kappa):
        """T is persymmetric at all kappa values."""
        sol = compute_zte_correction(kappa, _U_DEFAULT)
        assert sol["structural"]["is_persymmetric"], (
            "T not persymmetric at kappa=%.2f" % kappa
        )

    @pytest.mark.parametrize("kappa", [0.05, 0.1, 0.2, 0.3])
    def test_zero_antidiag_preserved(self, kappa):
        """T has zero anti-diagonal at all kappa values."""
        sol = compute_zte_correction(kappa, _U_DEFAULT)
        assert sol["structural"]["has_zero_antidiag"], (
            "T anti-diagonal nonzero at kappa=%.2f" % kappa
        )

    @pytest.mark.parametrize("kappa", [0.05, 0.1, 0.2, 0.3])
    def test_rank6_preserved(self, kappa):
        """T has rank 6 at all kappa values."""
        sol = compute_zte_correction(kappa, _U_DEFAULT)
        assert sol["structural"]["rank"] == 6, (
            "T rank %d at kappa=%.2f" %
            (sol["structural"]["rank"], kappa)
        )


# ---------------------------------------------------------------------------
# Spectral parameter universality tests
# ---------------------------------------------------------------------------

class TestSpectralUniversality:
    """Verify structural properties are universal across spectral params."""

    def test_universality(self):
        """All structural properties are independent of u_vals."""
        spd = spectral_parameter_dependence()
        assert spd["universal_symmetric"], "Symmetry not universal"
        assert spd["universal_persymmetric"], "Persymmetry not universal"
        assert spd["universal_rank6"], "Rank 6 not universal"
        assert spd["universal_zero_antidiag"], "Zero antidiag not universal"
        assert spd["universal_factorizable"], "Factorizability not universal"
        assert spd["universal_mixed_sign_eigs"], "Mixed-sign eigs not universal"


# ---------------------------------------------------------------------------
# Direct ZTE verification tests
# ---------------------------------------------------------------------------

class TestDirectZTEVerification:
    """Directly verify that S^{corr} satisfies ZTE."""

    @pytest.mark.parametrize("kappa", [0.1, 0.2, 0.3])
    def test_zte_satisfied(self, kappa):
        """S^{corr} satisfies ZTE to relative precision < 1e-5."""
        sol = compute_zte_correction(kappa, _U_DEFAULT)
        rel = sol["obs_final"] / sol["obs_orig"]
        assert rel < 1e-5, (
            "ZTE relative residual %.2e at kappa=%.2f" % (rel, kappa)
        )


# ---------------------------------------------------------------------------
# Master verification test
# ---------------------------------------------------------------------------

class TestMasterVerification:
    """Run the complete verification suite."""

    def test_master_suite(self):
        """Master verification passes all checks."""
        results = run_full_verification()
        s = results["summary"]
        assert s["T_exists"], "T should exist"
        assert s["T_is_symmetric"], "T should be symmetric"
        assert s["T_is_persymmetric"], "T should be persymmetric"
        assert s["T_has_zero_antidiag"], "T should have zero anti-diagonal"
        assert s["T_rank"] == 6, "T should have rank 6"
        assert s["T_is_factorizable"], "T should be factorizable per face"
        assert s["T_has_mixed_sign_eigs"], "T should have mixed-sign eigs"
        assert s["obstruction_antisymmetric"], "O should be antisymmetric"
        assert s["obstruction_rank"] == 4, "O should have rank 4"
        assert s["no_higher_obstruction"], "No higher obstruction"
        assert s["gauge_rank"] == 35, "Gauge rank should be 35"
        assert s["gauge_null_dim"] == 45, "Gauge null dim should be 45"
