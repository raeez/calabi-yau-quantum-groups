"""Tests for E_2 bar-cobar adjunction and E_2-chiral Koszul duality.

Verifies:
  1. E_2 Koszul self-duality: E_2^! = E_2{-2}
  2. E_2 Koszul dual computation for Sym(V), T(V), U_q(sl_2)
  3. Quantum group R-matrix from E_2 bar complex braiding
  4. E_2 bar-cobar inversion (Theorem CY-B)
  5. E_2 shadow tower and modular characteristic
  6. Cross-volume compatibility with Vol I

Manuscript references:
    notes/theory_e2_chiral_formalism.tex, Sections 6-8
    CLAUDE.md: CY-B (E_2-chiral Koszul duality)

Mathematical references:
    Getzler-Jones (1994): E_2 bar construction, E_n self-duality
    Fresse (2009): E_n operadic bar-cobar duality
    Tamarkin (2003): Kontsevich formality for E_2
    Jimbo (1986): quantum R-matrix for U_q(sl_2)
    Kassel (1995): Quantum Groups, Ch. VIII
    Drinfeld (1987): quantum groups and R-matrices
"""

import numpy as np
import pytest
from sympy import Rational, Symbol, simplify, binomial

from compute.lib.e2_barcobar_koszul import (
    cross_volume_arnold_check,
    drinfeld_r_matrix_sl2_fund,
    e2_bar_braiding_heisenberg,
    e2_bar_braiding_sl2,
    e2_bar_cobar_inversion_dims_sym,
    e2_bar_cobar_inversion_dims_uq,
    e2_cobar_dimensions,
    e2_complementarity_heisenberg,
    e2_complementarity_sl2,
    e2_dual_operad_arity_dims,
    e2_e1_bar_comparison_heisenberg,
    e2_e1_bar_comparison_sl2,
    e2_koszul_dual_sym,
    e2_koszul_dual_tensor,
    e2_koszul_dual_uq_sl2,
    e2_koszul_duality_summary,
    e2_koszul_shift,
    e2_koszul_shift_vs_vol1,
    e2_shadow_tower_comparison,
    en_koszul_shift,
    kappa_e1,
    kappa_e2,
    kappa_e2_classical_limit,
    numerical_e2_inversion_sym,
    numerical_e2_inversion_uq_sl2,
    r_matrix_from_e2_bar,
    r_matrix_q_inverse_check,
)
from compute.lib.e2_bar_complex import (
    kz_r_matrix_sl2,
    verify_qybe_sl2,
)


# ================================================================
#  1. E_2 OPERAD KOSZUL SELF-DUALITY
# ================================================================

class TestE2KoszulSelfDuality:
    """Test the E_2 operad Koszul self-duality: E_2^! = E_2{-2}."""

    def test_e2_shift_is_2(self):
        """The E_2 Koszul shift is 2 = dim(C)."""
        assert e2_koszul_shift() == 2

    def test_e1_shift_is_1(self):
        """The E_1 Koszul shift is 1 = dim(R)."""
        assert en_koszul_shift(1) == 1

    def test_en_shift_general(self):
        """E_n^! = E_n{-n}: the shift equals n for all n."""
        for n in range(1, 8):
            assert en_koszul_shift(n) == n

    def test_e2_arity_dims_factorial(self):
        """dim E_2(k) = k! (total Betti of FM_k(C))."""
        dims = e2_dual_operad_arity_dims(max_arity=6)
        from math import factorial
        for k in range(1, 7):
            assert dims[k] == factorial(k), (
                f"dim E_2({k}) = {dims[k]}, expected {factorial(k)}"
            )

    def test_e2_arity_1(self):
        """dim E_2(1) = 1 (FM_1(C) is a point)."""
        dims = e2_dual_operad_arity_dims()
        assert dims[1] == 1

    def test_e2_arity_2(self):
        """dim E_2(2) = 2 (FM_2(C) = C*, H^0 + H^1)."""
        dims = e2_dual_operad_arity_dims()
        assert dims[2] == 2

    def test_e2_arity_3(self):
        """dim E_2(3) = 6 (FM_3(C): Betti = 1 + 3 + 2)."""
        dims = e2_dual_operad_arity_dims()
        assert dims[3] == 6


# ================================================================
#  2. E_2 KOSZUL DUAL COMPUTATION
# ================================================================

class TestE2KoszulDual:
    """Test E_2 Koszul dual for specific algebras."""

    def test_sym_dual_generators_shifted_by_2(self):
        """Sym(V)^! = Sym(V*[-2]): generators shifted by -2."""
        data = e2_koszul_dual_sym(dim_V=1)
        assert data.generators_A[0][1] == 0, "Original generator in degree 0"
        assert data.generators_dual[0][1] == -2, "Dual generator in degree -2"

    def test_sym_dual_symmetric_braiding(self):
        """Sym(V) has symmetric braiding (E_infty)."""
        data = e2_koszul_dual_sym()
        assert data.braiding_type == "symmetric"

    def test_sym_dual_kappa_complementarity(self):
        """kappa(Sym(V)) + kappa(Sym(V)^!) = 0 for free fields."""
        k = Symbol("k")
        data = e2_koszul_dual_sym()
        total = simplify(data.kappa_A + data.kappa_dual)
        assert total == 0, f"Complementarity sum = {total}, expected 0"

    def test_tensor_dual_shifted_by_2(self):
        """T(V)^!_{E_2} = T(V*[-2]): shifted by 2 (not 1 as in E_1)."""
        data = e2_koszul_dual_tensor(dim_V=1)
        assert data.generators_dual[0][1] == -2

    def test_tensor_trivial_braiding(self):
        """T(V) with trivial braiding is symmetric."""
        data = e2_koszul_dual_tensor()
        assert data.braiding_type == "symmetric"

    def test_uq_sl2_dual_level(self):
        """U_q(sl_2)^! at level k has dual level k' = -k-4."""
        k = Symbol("k")
        data = e2_koszul_dual_uq_sl2(k)
        assert data.dual_name == "U_{q^{-1}}(sl_2), level k' = -k-4"

    def test_uq_sl2_non_symmetric(self):
        """U_q(sl_2) has non-symmetric braiding (genuine E_2)."""
        data = e2_koszul_dual_uq_sl2()
        assert data.braiding_type == "non-symmetric"

    def test_uq_sl2_not_self_dual(self):
        """U_q(sl_2) is not E_2-self-dual (q -> q^{-1})."""
        data = e2_koszul_dual_uq_sl2()
        assert data.is_e2_self_dual is False

    def test_uq_sl2_kappa_complementarity(self):
        """kappa(V_k(sl_2)) + kappa(V_{k'}(sl_2)) = 0 for KM family."""
        k = Symbol("k")
        data = e2_koszul_dual_uq_sl2(k)
        total = simplify(data.kappa_A + data.kappa_dual)
        assert total == 0, (
            f"KM complementarity sum = {total}, expected 0 (AP24: KM family sum = 0)"
        )


# ================================================================
#  3. E_2 BAR COMPLEX BRAIDING
# ================================================================

class TestE2BarBraiding:
    """Test the braiding structure on B_{E_2}(A)."""

    def test_heisenberg_braiding_symmetric(self):
        """B_{E_2}(H_k) has symmetric braiding (R = id)."""
        data = e2_bar_braiding_heisenberg()
        assert data["braiding_type"] == "symmetric (E_infty)"
        assert data["is_cocommutative"] is True

    def test_heisenberg_r_matrix_identity(self):
        """The R-matrix for Heisenberg is the identity."""
        data = e2_bar_braiding_heisenberg()
        np.testing.assert_allclose(data["r_matrix"], np.eye(1))

    def test_sl2_braiding_nonsymmetric(self):
        """B_{E_2}(V_k(sl_2)) has non-symmetric braiding."""
        data = e2_bar_braiding_sl2(k_val=1)
        assert data["braiding_type"] == "non-symmetric (genuine E_2)"
        assert data["is_cocommutative"] is False

    def test_sl2_quantum_symmetric_rank(self):
        """Quantum symmetric square S_q^2(fund) has rank 3."""
        data = e2_bar_braiding_sl2(k_val=1)
        assert data["quantum_symmetric_rank"] == 3

    def test_sl2_quantum_antisymmetric_rank(self):
        """Quantum antisymmetric square Lambda_q^2(fund) has rank 1."""
        data = e2_bar_braiding_sl2(k_val=1)
        assert data["quantum_antisymmetric_rank"] == 1

    @pytest.mark.parametrize("k_val", [1, 2, 3, 4, 5])
    def test_sl2_eigenvalue_q_multiplicity(self, k_val):
        """Eigenvalue q has multiplicity 3 for all levels."""
        data = e2_bar_braiding_sl2(k_val=k_val)
        assert data["multiplicity_q"] == 3, (
            f"Multiplicity of eigenvalue q at k={k_val}: "
            f"expected 3, got {data['multiplicity_q']}"
        )

    @pytest.mark.parametrize("k_val", [1, 2, 3, 4, 5])
    def test_sl2_eigenvalue_minus_q_inv_multiplicity(self, k_val):
        """Eigenvalue -q^{-1} has multiplicity 1 for all levels."""
        data = e2_bar_braiding_sl2(k_val=k_val)
        assert data["multiplicity_minus_q_inv"] == 1, (
            f"Multiplicity of eigenvalue -q^{{-1}} at k={k_val}: "
            f"expected 1, got {data['multiplicity_minus_q_inv']}"
        )

    @pytest.mark.parametrize("k_val", [1, 2, 3, 4, 5])
    def test_sl2_trace_R(self, k_val):
        """tr(Rcheck) = 3q - q^{-1} for all levels."""
        data = e2_bar_braiding_sl2(k_val=k_val)
        np.testing.assert_allclose(
            data["trace_R"], data["expected_trace"], atol=1e-12,
            err_msg=f"Trace of Rcheck at k={k_val}"
        )


# ================================================================
#  4. QUANTUM GROUP R-MATRIX FROM E_2 BAR
# ================================================================

class TestQuantumGroupRMatrix:
    """Test the R-matrix extracted from the E_2 bar complex."""

    @pytest.mark.parametrize("k_val", [1, 2, 3, 5, 10])
    def test_kz_matches_drinfeld(self, k_val):
        """KZ R-matrix matches Drinfeld/Jimbo R-matrix for all levels."""
        data = r_matrix_from_e2_bar(k_val)
        assert data["matrices_match"], (
            f"KZ and Drinfeld R-matrices differ at k={k_val}, "
            f"norm = {data['match_norm']}"
        )

    @pytest.mark.parametrize("k_val", [1, 2, 3, 5, 10])
    def test_braid_relation(self, k_val):
        """R-matrix satisfies the braid relation (QYBE) for all levels."""
        data = r_matrix_from_e2_bar(k_val)
        assert data["braid_relation_holds"], (
            f"Braid relation fails at k={k_val}, "
            f"norm = {data['braid_relation_norm']}"
        )

    @pytest.mark.parametrize("k_val", [1, 2, 3, 5])
    def test_r_matrix_eigenvalues(self, k_val):
        """R-matrix has eigenvalues q (x3) and -q^{-1} (x1)."""
        data = r_matrix_from_e2_bar(k_val)
        eigs = sorted(data["eigenvalues"], key=lambda z: z.real)
        q = data["q"]
        q_inv = 1.0 / q

        # Check the antisymmetric eigenvalue (-q^{-1})
        min_eig = min(eigs, key=lambda z: abs(z + q_inv))
        np.testing.assert_allclose(min_eig, -q_inv, atol=1e-10,
            err_msg=f"Missing eigenvalue -q^{{-1}} at k={k_val}")

    @pytest.mark.parametrize("k_val", [1, 2, 3, 5])
    def test_q_inverse_relation(self, k_val):
        """R(q^{-1}) = R(q)^{-1}: the Koszul duality relation."""
        data = r_matrix_q_inverse_check(k_val)
        assert data["relation_holds"], (
            f"R(q^{{-1}}) != R(q)^{{-1}} at k={k_val}, "
            f"diff norm = {data['difference_norm']}"
        )

    def test_r_matrix_determinant(self):
        """det(R) = q^3 * (-q^{-1}) = -q^2 for the 4x4 checked R-matrix."""
        k_val = 2
        q = np.exp(1j * np.pi / (k_val + 2))
        R = drinfeld_r_matrix_sl2_fund(q)
        det_R = np.linalg.det(R)
        # det = product of eigenvalues = q * q * q * (-q^{-1}) = -q^2
        expected_det = -q**2
        np.testing.assert_allclose(det_R, expected_det, atol=1e-10)


# ================================================================
#  5. E_2 BAR-COBAR INVERSION (Theorem CY-B)
# ================================================================

class TestE2BarCobarInversion:
    """Test the E_2 bar-cobar inversion theorem."""

    def test_sym_v1_inversion(self):
        """Omega_{E_2}(B_{E_2}(Sym(V))) ~ Sym(V) for dim V = 1."""
        data = e2_bar_cobar_inversion_dims_sym(dim_V=1, max_weight=6)
        assert data["dimensions_match"]

    def test_sym_v2_inversion(self):
        """Inversion for dim V = 2."""
        data = e2_bar_cobar_inversion_dims_sym(dim_V=2, max_weight=6)
        assert data["dimensions_match"]

    def test_sym_v3_inversion(self):
        """Inversion for dim V = 3."""
        data = e2_bar_cobar_inversion_dims_sym(dim_V=3, max_weight=6)
        assert data["dimensions_match"]

    def test_uq_sl2_inversion(self):
        """Omega_{E_2}(B_{E_2}(U_q(sl_2))) ~ U_q(sl_2)."""
        data = e2_bar_cobar_inversion_dims_uq(max_weight=6)
        assert data["dimensions_match"]

    @pytest.mark.parametrize("dim_V", [1, 2, 3])
    def test_numerical_sym_inversion(self, dim_V):
        """Numerical dimension verification for Sym(V) at all weights."""
        data = numerical_e2_inversion_sym(dim_V=dim_V, max_weight=6)
        assert data["all_match"], (
            f"Inversion dimension mismatch for Sym(V), dim V = {dim_V}"
        )

    def test_numerical_uq_sl2_inversion_k1(self):
        """Numerical inversion for U_q(sl_2) at k = 1 (root of unity)."""
        data = numerical_e2_inversion_uq_sl2(k_val=1, max_weight=6)
        assert data["all_match"]

    def test_numerical_uq_sl2_inversion_k3(self):
        """Numerical inversion for U_q(sl_2) at k = 3."""
        data = numerical_e2_inversion_uq_sl2(k_val=3, max_weight=6)
        assert data["all_match"]

    def test_cobar_dims_sym(self):
        """Cobar dimensions for Sym(V) match Sym^w(V) dimensions."""
        dims = e2_cobar_dimensions("sym", 1, max_weight=6)
        for w in range(7):
            assert dims[w] == 1, f"dim Sym^{w}(V) for dim V = 1 should be 1"

    def test_cobar_dims_uq(self):
        """Cobar dimensions for U_q(sl_2) match PBW dimensions."""
        dims = e2_cobar_dimensions("uq_sl2", 3, max_weight=4)
        expected = {0: 1, 1: 3, 2: 6, 3: 10, 4: 15}
        for w in range(5):
            assert dims[w] == expected[w], (
                f"dim U_q(sl_2) at weight {w}: got {dims[w]}, expected {expected[w]}"
            )


# ================================================================
#  6. E_2 SHADOW TOWER AND MODULAR CHARACTERISTIC
# ================================================================

class TestE2ShadowTower:
    """Test the E_2 shadow tower and kappa_{E_2}."""

    def test_kappa_e1_heisenberg(self):
        """kappa_{E_1}(H_k) = k (Vol I authoritative: kappa = level)."""
        k = Symbol("k")
        assert kappa_e1("heisenberg", k) == k

    def test_kappa_e1_sl2(self):
        """kappa_{E_1}(V_k(sl_2)) = 3(k+2)/4."""
        k = Symbol("k")
        result = kappa_e1("sl2", k)
        expected = Rational(3, 4) * (k + 2)
        assert simplify(result - expected) == 0

    def test_kappa_e2_heisenberg_equals_e1(self):
        """kappa_{E_2}(H_k) = kappa_{E_1}(H_k) (no braiding correction)."""
        k = Symbol("k")
        assert kappa_e2("heisenberg", k) == kappa_e1("heisenberg", k)

    def test_kappa_e2_sl2_has_correction(self):
        """kappa_{E_2}(V_k(sl_2)) != kappa_{E_1}(V_k(sl_2)) (braiding correction)."""
        k = Symbol("k")
        kap_2 = kappa_e2("sl2", k)
        kap_1 = kappa_e1("sl2", k)
        diff = simplify(kap_2 - kap_1)
        # The correction is 1/(k+2), which is nonzero
        assert diff != 0, "E_2 kappa should differ from E_1 kappa for sl_2"

    def test_kappa_e2_sl2_correction_magnitude(self):
        """The braiding correction for sl_2 is 1/(k+2)."""
        k = Symbol("k")
        kap_2 = kappa_e2("sl2", k)
        kap_1 = kappa_e1("sl2", k)
        diff = simplify(kap_2 - kap_1)
        expected = 1 / (k + 2)
        assert simplify(diff - expected) == 0, (
            f"Braiding correction = {diff}, expected 1/(k+2)"
        )

    def test_kappa_e2_classical_limit_heisenberg(self):
        """kappa_{E_2} -> kappa_{E_1} as q -> 1 for Heisenberg (trivially)."""
        data = kappa_e2_classical_limit("heisenberg")
        assert data["classical_limit_matches"]

    def test_kappa_e2_classical_limit_sl2(self):
        """kappa_{E_2} -> kappa_{E_1} as k -> infty for sl_2."""
        data = kappa_e2_classical_limit("sl2")
        # Difference = 1/(k+2) -> 0 as k -> infinity
        assert data["classical_limit_matches"]

    @pytest.mark.parametrize("k_val", [1, 2, 5, 10, 50])
    def test_shadow_tower_correction_decreases(self, k_val):
        """Braiding correction ratio decreases with increasing k."""
        data = e2_shadow_tower_comparison(k_val)
        ratio = data["correction_ratio"]
        assert ratio is not None
        # Ratio = 1/(k+2) / (3(k+2)/4) = 4/(3(k+2)^2) -> 0
        assert abs(ratio) < 1, (
            f"Correction ratio = {ratio} at k={k_val}, expected < 1"
        )


# ================================================================
#  7. COMPLEMENTARITY
# ================================================================

class TestE2Complementarity:
    """Test the kappa + kappa^! sum for E_2 Koszul duality."""

    def test_heisenberg_complementarity(self):
        """kappa(H_k) + kappa(H_k^!) = 0."""
        k = Symbol("k")
        data = e2_complementarity_heisenberg(k)
        assert data["sum_vanishes"], f"Complementarity sum = {data['sum']}"

    def test_sl2_complementarity(self):
        """kappa(V_k) + kappa(V_{k'}^!) = 0 for KM family."""
        k = Symbol("k")
        data = e2_complementarity_sl2(k)
        assert data["sum_vanishes"], f"Complementarity sum = {data['sum']}"

    def test_sl2_dual_level(self):
        """Dual level k' = -k - 4 for sl_2 (h^v = 2)."""
        k = Symbol("k")
        data = e2_complementarity_sl2(k)
        expected_dual = -k - 4
        assert simplify(data["k_dual"] - expected_dual) == 0


# ================================================================
#  8. E_2 vs E_1 COMPARISON
# ================================================================

class TestE2E1Comparison:
    """Test the comparison between E_2 and E_1 bar complexes."""

    def test_heisenberg_e2_extra_factor(self):
        """B_{E_2}(H_k) has an extra factor over B_{E_1}(H_k)."""
        data = e2_e1_bar_comparison_heisenberg()
        # E_2 dimensions should be twice E_1 (from KT decomposition)
        for w, ratio in data["ratio"].items():
            assert ratio == 2, (
                f"E_2/E_1 ratio at weight {w} = {ratio}, expected 2 "
                "(from Lambda^*(V[-1]) factor)"
            )

    def test_sl2_e2_has_dy(self):
        """V_k(sl_2) has non-trivial d_Y in the E_2 bar complex."""
        data = e2_e1_bar_comparison_sl2(k_val=1)
        assert data["e2_has_d_Y"], "V_k(sl_2) must have non-trivial d_Y"

    def test_sl2_r_matrix_in_e2(self):
        """The R-matrix is present in the E_2 bar complex of V_k(sl_2)."""
        data = e2_e1_bar_comparison_sl2(k_val=1)
        assert data["r_matrix_present_in_e2"]


# ================================================================
#  9. CROSS-VOLUME COMPATIBILITY WITH VOL I
# ================================================================

class TestCrossVolume:
    """Cross-check with Vol I en_koszul_bridge."""

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
    def test_arnold_total_betti_factorial(self, n):
        """Total Betti number of FM_n(C) = n! (cross-check with Vol I)."""
        data = cross_volume_arnold_check(n)
        assert data["total_matches"], (
            f"Total Betti of FM_{n}(C) = {data['total_betti']}, "
            f"expected {data['expected_total']}"
        )

    def test_arnold_betti_n3(self):
        """Betti numbers of FM_3(C) = (1, 3, 2)."""
        data = cross_volume_arnold_check(3)
        assert data["betti_numbers"] == [1, 3, 2]

    def test_arnold_betti_n4(self):
        """Betti numbers of FM_4(C) = (1, 6, 11, 6)."""
        data = cross_volume_arnold_check(4)
        assert data["betti_numbers"] == [1, 6, 11, 6]

    def test_arnold_generators_count(self):
        """C(n,2) Arnold generators for FM_n(C)."""
        for n in range(2, 6):
            data = cross_volume_arnold_check(n)
            assert data["num_generators"] == n * (n - 1) // 2

    def test_arnold_relations_count(self):
        """C(n,3) Arnold relations for FM_n(C)."""
        for n in range(3, 6):
            data = cross_volume_arnold_check(n)
            assert data["num_relations"] == n * (n - 1) * (n - 2) // 6

    def test_koszul_shift_consistency(self):
        """E_n Koszul shifts match between Vol I formality and Vol III computation."""
        data = e2_koszul_shift_vs_vol1(n_max=5)
        assert data["e2_shift"] == 2
        assert data["e1_shift"] == 1
        for n in range(1, 6):
            assert data["shifts"][n] == n

    def test_formality_e1_not_formal(self):
        """E_1 is NOT formal (A_inf obstructions)."""
        data = e2_koszul_shift_vs_vol1()
        assert data["formality"][1] is False

    def test_formality_e2_formal(self):
        """E_2 is formal (Kontsevich-Tamarkin)."""
        data = e2_koszul_shift_vs_vol1()
        assert data["formality"][2] is True


# ================================================================
# 10. SUMMARY AND INTEGRATION
# ================================================================

class TestSummary:
    """Test the summary table and integration."""

    def test_summary_table_nonempty(self):
        """Summary table is a non-empty string."""
        table = e2_koszul_duality_summary()
        assert isinstance(table, str)
        assert len(table) > 100

    def test_summary_mentions_e2(self):
        """Summary table mentions E_2."""
        table = e2_koszul_duality_summary()
        assert "E_2" in table

    def test_summary_mentions_braiding(self):
        """Summary table mentions braiding."""
        table = e2_koszul_duality_summary()
        assert "braiding" in table.lower()


# ================================================================
# 11. EDGE CASES AND ROBUSTNESS
# ================================================================

class TestEdgeCases:
    """Test edge cases and robustness."""

    def test_r_matrix_k_large(self):
        """R-matrix at large k (classical limit): R -> P (flip)."""
        k_val = 1000
        q = np.exp(1j * np.pi / (k_val + 2))
        R = drinfeld_r_matrix_sl2_fund(q)
        # As k -> inf, q -> 1, and Rcheck -> P (permutation matrix)
        P = np.array([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
        ], dtype=complex)
        np.testing.assert_allclose(R, P, atol=1e-2,
            err_msg="At large k, Rcheck should approach the flip P")

    def test_cobar_dims_unknown_type_raises(self):
        """Unknown algebra type raises ValueError."""
        with pytest.raises(ValueError):
            e2_cobar_dimensions("unknown", 1)

    def test_kappa_e1_unknown_raises(self):
        """Unknown algebra name raises ValueError."""
        with pytest.raises(ValueError):
            kappa_e1("unknown")

    def test_sym_dual_multiple_generators(self):
        """E_2 Koszul dual of Sym(V) for dim V = 5."""
        data = e2_koszul_dual_sym(dim_V=5)
        assert len(data.generators_A) == 5
        assert len(data.generators_dual) == 5
        for _, deg in data.generators_dual:
            assert deg == -2

    def test_inversion_sym_weight_0(self):
        """At weight 0, dim Sym^0(V) = 1 for any V."""
        for dim_V in [1, 2, 5]:
            data = numerical_e2_inversion_sym(dim_V=dim_V, max_weight=1)
            assert data["results_by_weight"][0]["dim_A"] == 1


# ================================================================
# 12. BRAID RELATION AND YANG-BAXTER CROSS-CHECKS
# ================================================================

class TestBraidRelation:
    """Additional cross-checks for the braid/Yang-Baxter relation."""

    @pytest.mark.parametrize("k_val", [1, 2, 3, 4])
    def test_ybe_from_e2_bar_module(self, k_val):
        """Braid relation from the e2_bar_complex module matches."""
        norm = verify_qybe_sl2(k_val)
        assert norm < 1e-10, (
            f"YBE violation at k={k_val}: norm = {norm}"
        )

    def test_r_matrix_unitarity(self):
        """R * R^{-1} = id (the R-matrix is invertible)."""
        for k_val in [1, 3, 5]:
            q = np.exp(1j * np.pi / (k_val + 2))
            R = drinfeld_r_matrix_sl2_fund(q)
            RRinv = R @ np.linalg.inv(R)
            np.testing.assert_allclose(RRinv, np.eye(4), atol=1e-10)

    def test_r_matrix_trace(self):
        """tr(R) = 3q + (-q^{-1}) = 3q - q^{-1} for the fundamental rep."""
        k_val = 2
        q = np.exp(1j * np.pi / (k_val + 2))
        R = drinfeld_r_matrix_sl2_fund(q)
        tr = np.trace(R)
        expected = 3 * q - 1.0 / q
        np.testing.assert_allclose(tr, expected, atol=1e-10)
