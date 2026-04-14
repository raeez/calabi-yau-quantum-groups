"""Tests for the ZTE correction engine.

Verifies the construction of the corrected 3-particle S-operator
S^{corr}_{ijk} = R_{ij} R_{ik} R_{jk} + C_{ijk} that solves the
Zamolodchikov tetrahedron equation at the linearized level.

Key results verified:
  1. Linearized ZTE system has rank 35 (of 36 constraints).
  2. 45-dimensional null space (gauge freedom).
  3. Pairwise R-matrix deformations are gauge-trivial (rescaling).
  4. Ternary correction C_{ijk} exists and is non-factorizable.
  5. Corrected obstruction scales as O(kappa^4).
  6. Non-factorizability: genuinely ternary component is nonzero.

VERIFIED sources:
[DC]  Direct computation via numpy linear algebra.
[ZTE] Zamolodchikov tetrahedron equation (face formulation on V^4).
[KV]  Kapranov-Voevodsky: permutation limit satisfies ZTE.
"""

import numpy as np
import pytest

from compute.lib.zte_correction_engine import (
    build_r_and_s,
    correction_scaling_analysis,
    embed_pairwise_correction,
    embed_ternary_correction,
    linearized_zte_ternary,
    nonfactorizability_analysis,
    pairwise_deformation_analysis,
    run_zte_correction_verification,
    solve_linearized_zte,
    zte_obstruction,
)
from compute.lib.zamolodchikov_tetrahedron_engine import (
    charge_sector_basis,
)


# ---------------------------------------------------------------------------
# Test parameters
# ---------------------------------------------------------------------------

_U_DEFAULT = [0.0, 1.0, 3.0, 7.0]
_KAPPA_SMALL = -0.01


# ---------------------------------------------------------------------------
# Embedding tests
# ---------------------------------------------------------------------------

class TestEmbeddings:
    """Verify that pairwise and ternary embeddings are correct."""

    def test_pairwise_preserves_charge(self):
        """Pairwise embedding preserves total charge on V^4."""
        D = np.eye(4, dtype=complex) * 0.5  # charge-preserving
        E = embed_pairwise_correction(D, 0, 1)
        # Check: for each basis vector, charge is preserved
        for src in range(16):
            bits = [(src >> (3 - k)) & 1 for k in range(4)]
            charge_src = sum(bits)
            for dst in range(16):
                if abs(E[dst, src]) < 1e-15:
                    continue
                bits_d = [(dst >> (3 - k)) & 1 for k in range(4)]
                assert sum(bits_d) == charge_src, (
                    f"Charge not preserved: src={bits}, dst={bits_d}"
                )

    def test_ternary_preserves_charge(self):
        """Ternary embedding preserves total charge on V^4."""
        C = np.eye(8, dtype=complex) * 0.3
        E = embed_ternary_correction(C, 0, 1, 2)
        for src in range(16):
            bits = [(src >> (3 - k)) & 1 for k in range(4)]
            charge_src = sum(bits)
            for dst in range(16):
                if abs(E[dst, src]) < 1e-15:
                    continue
                bits_d = [(dst >> (3 - k)) & 1 for k in range(4)]
                assert sum(bits_d) == charge_src

    def test_ternary_identity_is_identity(self):
        """Ternary embedding of Id on (0,1,2) is identity on charge sectors."""
        I8 = np.eye(8, dtype=complex)
        E = embed_ternary_correction(I8, 0, 1, 2)
        # Should be identity on V^4 (since it acts as Id on 012 and Id on 3)
        assert np.allclose(E, np.eye(16)), (
            "Ternary embedding of Id should be Id on V^4"
        )

    def test_pairwise_identity_is_identity(self):
        """Pairwise embedding of Id on (0,1) is identity."""
        I4 = np.eye(4, dtype=complex)
        E = embed_pairwise_correction(I4, 0, 1)
        assert np.allclose(E, np.eye(16))

    def test_ternary_all_faces(self):
        """Ternary embedding works for all 4 faces."""
        C = np.random.randn(8, 8) + 1j * np.random.randn(8, 8)
        # Make charge-preserving by zeroing off-charge blocks
        charges = {}
        for idx in range(8):
            c = ((idx >> 2) & 1) + ((idx >> 1) & 1) + (idx & 1)
            charges.setdefault(c, []).append(idx)
        C_cp = np.zeros((8, 8), dtype=complex)
        for c, indices in charges.items():
            for p in indices:
                for q in indices:
                    C_cp[p, q] = C[p, q]

        for (i, j, k) in [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]:
            E = embed_ternary_correction(C_cp, i, j, k)
            assert E.shape == (16, 16), f"Wrong shape for face ({i},{j},{k})"
            assert np.all(np.isfinite(E)), f"Non-finite for face ({i},{j},{k})"


# ---------------------------------------------------------------------------
# Build and obstruction tests
# ---------------------------------------------------------------------------

class TestBuildAndObstruction:
    """Verify S-operator construction and ZTE obstruction."""

    def test_zte_fails(self):
        """ZTE is not satisfied for the Yang R-matrix."""
        _, S_dict = build_r_and_s(_KAPPA_SMALL, _U_DEFAULT)
        obs = zte_obstruction(S_dict)
        assert obs["frobenius_c2"] > 1e-10, "ZTE should fail"

    def test_zte_trivial_at_zero(self):
        """ZTE is trivially satisfied at kappa=0 (Kapranov-Voevodsky)."""
        _, S_dict = build_r_and_s(0.0, _U_DEFAULT)
        obs = zte_obstruction(S_dict)
        assert obs["frobenius_c2"] < 1e-14, (
            "ZTE should be satisfied at kappa=0"
        )

    def test_obstruction_scales_as_kappa_squared(self):
        """ZTE obstruction scales as O(kappa^2)."""
        norms = []
        kappas = [0.001, 0.01]
        for k in kappas:
            _, S = build_r_and_s(-k, _U_DEFAULT)
            obs = zte_obstruction(S)
            norms.append(obs["frobenius_c2"])
        # Ratio of norms should be ~ (kappas[1]/kappas[0])^2 = 100
        ratio = norms[1] / norms[0]
        assert 90 < ratio < 110, (
            f"Scaling ratio {ratio:.1f}, expected ~100 for O(kappa^2)"
        )

    def test_obstruction_antisymmetric(self):
        """ZTE obstruction is antisymmetric on charge-2 sector."""
        _, S = build_r_and_s(_KAPPA_SMALL, _U_DEFAULT)
        obs = zte_obstruction(S)
        O = obs["charge2"]
        assert np.allclose(O + O.T, 0, atol=1e-14), (
            "Obstruction should be antisymmetric"
        )


# ---------------------------------------------------------------------------
# Linearized system tests
# ---------------------------------------------------------------------------

class TestLinearizedSystem:
    """Verify properties of the linearized ZTE system."""

    def test_system_dimensions(self):
        """Linear system has correct dimensions: 36 constraints, 80 params."""
        sys = linearized_zte_ternary(_KAPPA_SMALL, _U_DEFAULT)
        assert sys["n_constraints"] == 36, (
            f"Expected 36 constraints, got {sys['n_constraints']}"
        )
        assert sys["n_params"] == 80, (
            f"Expected 80 parameters, got {sys['n_params']}"
        )

    def test_rank_is_35(self):
        """Linearized system has rank 35."""
        sys = linearized_zte_ternary(_KAPPA_SMALL, _U_DEFAULT)
        assert sys["rank"] == 35, (
            f"Expected rank 35, got {sys['rank']}"
        )

    def test_null_space_dim_45(self):
        """Null space has dimension 45."""
        sys = linearized_zte_ternary(_KAPPA_SMALL, _U_DEFAULT)
        assert sys["null_dim"] == 45, (
            f"Expected null dim 45, got {sys['null_dim']}"
        )

    def test_target_in_image(self):
        """The ZTE obstruction lies in the image of the linearized operator."""
        sys = linearized_zte_ternary(_KAPPA_SMALL, _U_DEFAULT)
        A = sys["A"]
        b = sys["b"]
        U, s, _ = np.linalg.svd(A, full_matrices=True)
        rank = sys["rank"]
        b_proj = sum(np.dot(U[:, i].conj(), b) * U[:, i] for i in range(rank))
        residual = np.linalg.norm(b - b_proj)
        rel = residual / np.linalg.norm(b)
        assert rel < 1e-10, (
            f"Target not in image: relative residual = {rel:.2e}"
        )


# ---------------------------------------------------------------------------
# Pairwise gauge triviality
# ---------------------------------------------------------------------------

class TestPairwiseGauge:
    """Verify that pairwise R-matrix corrections are gauge-trivial."""

    def test_all_id_plus_p(self):
        """All pairwise solutions have form a*Id + b*P."""
        pw = pairwise_deformation_analysis(_KAPPA_SMALL, _U_DEFAULT)
        assert pw["all_id_plus_p"], (
            "Pairwise solution should be of the form a*Id + b*P"
        )

    def test_rescale_prediction(self):
        """Predicted rescaling ratio matches actual ratio."""
        pw = pairwise_deformation_analysis(_KAPPA_SMALL, _U_DEFAULT)
        # The predicted (1+c)^12 should match actual obs_corr/obs_orig
        assert abs(pw["predicted_ratio"] - pw["actual_ratio"]) < 0.01, (
            f"Predicted {pw['predicted_ratio']:.4f} vs "
            f"actual {pw['actual_ratio']:.4f}"
        )

    def test_pairwise_does_not_solve(self):
        """Pairwise correction does not eliminate the obstruction."""
        pw = pairwise_deformation_analysis(_KAPPA_SMALL, _U_DEFAULT)
        # The ratio should be significantly above 0 (not solving ZTE)
        assert pw["actual_ratio"] > 0.1, (
            f"Pairwise ratio too small: {pw['actual_ratio']:.4f}"
        )


# ---------------------------------------------------------------------------
# Ternary correction existence
# ---------------------------------------------------------------------------

class TestTernaryCorrection:
    """Verify that the ternary correction exists and works."""

    def test_solvable(self):
        """The linearized ZTE admits a ternary correction."""
        sol = solve_linearized_zte(_KAPPA_SMALL, _U_DEFAULT)
        assert sol["solvable"], "Linearized ZTE should be solvable"

    def test_improvement(self):
        """Ternary correction improves the ZTE residual."""
        sol = solve_linearized_zte(_KAPPA_SMALL, _U_DEFAULT)
        assert sol["improvement_ratio"] > 5, (
            f"Improvement ratio {sol['improvement_ratio']:.1f} too small"
        )

    def test_all_faces_nonzero(self):
        """All four face corrections are nonzero."""
        sol = solve_linearized_zte(_KAPPA_SMALL, _U_DEFAULT)
        for face, C in sol["C_faces"].items():
            assert np.linalg.norm(C, "fro") > 1e-10, (
                f"Face {face} correction is zero"
            )

    def test_correction_charge_preserving(self):
        """Each face correction C preserves charge on V^3."""
        sol = solve_linearized_zte(_KAPPA_SMALL, _U_DEFAULT)
        charges = {}
        for idx in range(8):
            c = ((idx >> 2) & 1) + ((idx >> 1) & 1) + (idx & 1)
            charges.setdefault(c, []).append(idx)

        for face, C in sol["C_faces"].items():
            for c1 in charges:
                for c2 in charges:
                    if c1 == c2:
                        continue
                    for p in charges[c1]:
                        for q in charges[c2]:
                            assert abs(C[p, q]) < 1e-12, (
                                f"Face {face}: C[{p},{q}] = {C[p,q]} "
                                f"violates charge ({c1} -> {c2})"
                            )

    def test_multiple_kappa_values(self):
        """Ternary correction exists at multiple kappa values."""
        for kap in [-0.001, -0.01, -0.05, -0.1]:
            sol = solve_linearized_zte(kap, _U_DEFAULT)
            assert sol["solvable"], f"Not solvable at kappa={kap}"

    def test_different_spectral_params(self):
        """Ternary correction exists for different spectral parameters."""
        u_alt = [0.0, 2.0, 5.0, 11.0]
        sol = solve_linearized_zte(_KAPPA_SMALL, u_alt)
        assert sol["solvable"], "Not solvable at u=(0,2,5,11)"


# ---------------------------------------------------------------------------
# Non-factorizability
# ---------------------------------------------------------------------------

class TestNonFactorizability:
    """Verify that the correction is genuinely ternary."""

    def test_is_nonfactorizable(self):
        """The correction has a nonzero genuinely ternary component."""
        nf = nonfactorizability_analysis(_KAPPA_SMALL, _U_DEFAULT)
        assert nf["is_nonfactorizable"], (
            "Correction should be non-factorizable"
        )

    def test_ternary_fraction_significant(self):
        """The ternary fraction is significant (not just rounding)."""
        nf = nonfactorizability_analysis(_KAPPA_SMALL, _U_DEFAULT)
        assert nf["overall_ternary_fraction"] > 0.01, (
            f"Ternary fraction {nf['overall_ternary_fraction']:.4f} too small"
        )

    def test_all_faces_nonfactorizable(self):
        """Each face correction has a nonzero ternary component."""
        nf = nonfactorizability_analysis(_KAPPA_SMALL, _U_DEFAULT)
        for face, data in nf["per_face"].items():
            assert data["ternary_fraction"] > 0.001, (
                f"Face {face}: ternary fraction too small"
            )


# ---------------------------------------------------------------------------
# Scaling analysis
# ---------------------------------------------------------------------------

class TestScalingAnalysis:
    """Verify perturbative scaling of the correction."""

    def test_original_scales_quadratically(self):
        """Original obstruction scales as O(kappa^2)."""
        scaling = correction_scaling_analysis(_U_DEFAULT)
        assert abs(scaling["scaling_orig"] - 2.0) < 0.15, (
            f"Original scaling exponent {scaling['scaling_orig']:.2f}, "
            f"expected ~2.0"
        )

    def test_corrected_scales_quartically(self):
        """Corrected residual scales as O(kappa^4)."""
        scaling = correction_scaling_analysis(_U_DEFAULT)
        assert abs(scaling["scaling_corr"] - 4.0) < 0.3, (
            f"Corrected scaling exponent {scaling['scaling_corr']:.2f}, "
            f"expected ~4.0"
        )

    def test_improvement_increases_at_small_kappa(self):
        """Improvement ratio increases as kappa -> 0."""
        ratios = []
        for kap in [0.05, 0.01, 0.001]:
            sol = solve_linearized_zte(-kap, _U_DEFAULT)
            ratios.append(sol["improvement_ratio"])
        # Improvement should increase as kappa decreases
        for i in range(len(ratios) - 1):
            assert ratios[i + 1] > ratios[i], (
                f"Improvement not increasing: {ratios}"
            )


# ---------------------------------------------------------------------------
# Master verification
# ---------------------------------------------------------------------------

class TestMasterVerification:
    """Integration test: run the full verification suite."""

    @pytest.mark.slow
    def test_full_suite(self):
        """Run complete verification and check all assertions."""
        results = run_zte_correction_verification()

        assert results["summary"]["ternary_correction_exists"]
        assert results["summary"]["pairwise_is_gauge"]
        assert results["summary"]["is_nonfactorizable"]
        assert results["summary"]["linearized_rank"] == 35
        assert results["summary"]["gauge_dim"] == 45

    @pytest.mark.slow
    def test_full_suite_alt_params(self):
        """Full verification with alternative spectral parameters."""
        u_alt = [0.0, 2.0, 5.0, 11.0]
        results = run_zte_correction_verification(u_alt)
        assert results["summary"]["ternary_correction_exists"]


# ---------------------------------------------------------------------------
# Cross-checks with zamolodchikov_tetrahedron_engine
# ---------------------------------------------------------------------------

class TestCrossChecks:
    """Cross-validate against the original tetrahedron engine."""

    def test_obstruction_matches_original(self):
        """Our obstruction matches the original engine's computation."""
        from compute.lib.zamolodchikov_tetrahedron_engine import (
            zamolodchikov_zte_numpy,
            project_to_charge_sector,
        )
        kap = -0.01
        r_orig = zamolodchikov_zte_numpy(kap, _U_DEFAULT)
        diff_orig = project_to_charge_sector(r_orig["diff"], 4, 2)

        _, S = build_r_and_s(kap, _U_DEFAULT)
        obs = zte_obstruction(S)
        diff_new = obs["charge2"]

        assert np.allclose(diff_orig, diff_new, atol=1e-12), (
            "Obstruction mismatch between engines"
        )

    def test_r_matrix_matches(self):
        """Our R-matrix construction matches the original."""
        from compute.lib.zamolodchikov_tetrahedron_engine import (
            _embed_r_numpy as orig_embed,
        )
        kap = -0.5
        for a in range(4):
            for b in range(a + 1, 4):
                z = _U_DEFAULT[a] - _U_DEFAULT[b]
                R_orig = orig_embed(z, kap, a, b, 4)
                R_new = _embed_r_numpy(z, kap, a, b, 4)
                assert np.allclose(R_orig, R_new, atol=1e-14), (
                    f"R-matrix mismatch at ({a},{b})"
                )
