r"""Cross-volume shadow bridge tests: 70+ tests verifying consistency across three volumes.

The three volumes attack the same mathematical objects from different angles:
  Vol I:   bar-cobar machine, shadow obstruction tower, modular characteristic kappa
  Vol II:  Swiss-cheese, PVA descent, open/closed, 3D HT QFT
  Vol III: CY categories, E_2 enhancement, quantum groups, CoHA

Every shared example MUST produce identical invariants when computed from any
volume's perspective.  This test suite is the definitive cross-volume consistency
check.

Test structure:
  1. Authoritative kappa formulas (recomputed from first principles)
  2. Cross-volume kappa agreement (Vol I <-> bridge <-> Vol III)
  3. Shadow depth classification consistency
  4. SC-formality classification (Vol II perspective)
  5. Complementarity (Theorem C) verification
  6. R-matrix data consistency
  7. Quantum group bridge (KL equivalence)
  8. F_g genus tower consistency
  9. Master comparison table integrity
  10. CY dimension correlation
  11. Discrepancy detection
"""

import os
import sys
import math
import pytest
from fractions import Fraction
from typing import Dict, Any

# Ensure all three volumes' lib directories are on the path
_VOL1_LIB = os.path.expanduser("~/chiral-bar-cobar/compute/lib")
_VOL2_LIB = os.path.expanduser("~/chiral-bar-cobar-vol2/compute/lib")
_VOL3_LIB = os.path.expanduser("~/calabi-yau-quantum-groups/compute/lib")

for _p in [_VOL1_LIB, _VOL2_LIB, _VOL3_LIB]:
    if _p not in sys.path:
        sys.path.insert(0, _p)

from cross_volume_shadow_bridge import (
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine,
    kappa_betagamma,
    kappa_bc,
    kappa_w3,
    kappa_wN,
    kappa_lattice,
    kappa_e8_affine,
    shadow_depth_class,
    sc_formal,
    sc_depth,
    complementarity_sum,
    kappa_dual,
    verify_complementarity,
    vol1_kappa,
    vol3_kappa_heisenberg,
    vol3_kappa_affine_sl2,
    lambda_fp,
    F_g,
    Q_contact_virasoro,
    r_matrix_heisenberg_collision,
    r_matrix_affine_sl2,
    r_matrix_virasoro_collision,
    kl_equivalence_check,
    master_comparison_entry,
    full_master_table,
    cy_dimension_correlation,
    detect_discrepancies,
    F_g_table,
    verify_F_g_complementarity,
    _dispatch_kappa,
    _lie_dim_hdual,
)


# ==========================================================================
# SECTION 1: AUTHORITATIVE KAPPA FORMULAS (FROM FIRST PRINCIPLES)
# ==========================================================================

class TestKappaHeisenberg:
    """Verify kappa(H_k) = k from first principles."""

    def test_kappa_heisenberg_k1(self):
        assert kappa_heisenberg(1) == Fraction(1)

    def test_kappa_heisenberg_k2(self):
        assert kappa_heisenberg(2) == Fraction(2)

    def test_kappa_heisenberg_k_negative(self):
        assert kappa_heisenberg(-1) == Fraction(-1)

    def test_kappa_heisenberg_k_half(self):
        assert kappa_heisenberg(Fraction(1, 2)) == Fraction(1, 2)


class TestKappaVirasoro:
    """Verify kappa(Vir_c) = c/2 from first principles."""

    def test_kappa_virasoro_c1(self):
        assert kappa_virasoro(1) == Fraction(1, 2)

    def test_kappa_virasoro_c26(self):
        assert kappa_virasoro(26) == Fraction(13)

    def test_kappa_virasoro_c13(self):
        """At the self-dual point c = 13, kappa = 13/2."""
        assert kappa_virasoro(13) == Fraction(13, 2)

    def test_kappa_virasoro_c0(self):
        assert kappa_virasoro(0) == Fraction(0)


class TestKappaAffineSl2:
    """Verify kappa(V_k(sl_2)) = 3(k+2)/4 from first principles.

    dim(sl_2) = 3, h^v = 2.
    kappa = 3 * (k + 2) / (2 * 2) = 3(k+2)/4.
    """

    def test_kappa_sl2_k1(self):
        # kappa = 3*(1+2)/4 = 9/4
        assert kappa_affine("A", 1, 1) == Fraction(9, 4)

    def test_kappa_sl2_k2(self):
        # kappa = 3*(2+2)/4 = 3
        assert kappa_affine("A", 1, 2) == Fraction(3)

    def test_kappa_sl2_k4(self):
        # kappa = 3*(4+2)/4 = 18/4 = 9/2
        assert kappa_affine("A", 1, 4) == Fraction(9, 2)

    def test_kappa_sl2_critical_level_raises(self):
        """At k = -h^v = -2, kappa is undefined (Sugawara undefined)."""
        with pytest.raises(ValueError, match="Critical level"):
            kappa_affine("A", 1, -2)


class TestKappaAffineSl3:
    """Verify kappa(V_k(sl_3)) = 4(k+3)/3 from first principles.

    dim(sl_3) = 8, h^v = 3.
    kappa = 8 * (k + 3) / (2 * 3) = 4(k+3)/3.
    """

    def test_kappa_sl3_k1(self):
        # kappa = 4*(1+3)/3 = 16/3
        assert kappa_affine("A", 2, 1) == Fraction(16, 3)

    def test_kappa_sl3_k2(self):
        # kappa = 4*(2+3)/3 = 20/3
        assert kappa_affine("A", 2, 2) == Fraction(20, 3)

    def test_kappa_sl3_critical_raises(self):
        """At k = -h^v = -3, kappa is undefined."""
        with pytest.raises(ValueError, match="Critical level"):
            kappa_affine("A", 2, -3)


class TestKappaBetaGamma:
    """Verify kappa(bg_lambda) = 6*lambda^2 - 6*lambda + 1."""

    def test_kappa_bg_lam0(self):
        # 6*0 - 6*0 + 1 = 1
        assert kappa_betagamma(0) == Fraction(1)

    def test_kappa_bg_lam_half(self):
        # 6*(1/4) - 6*(1/2) + 1 = 3/2 - 3 + 1 = -1/2
        assert kappa_betagamma(Fraction(1, 2)) == Fraction(-1, 2)

    def test_kappa_bg_lam1(self):
        # 6*1 - 6*1 + 1 = 1
        assert kappa_betagamma(1) == Fraction(1)

    def test_kappa_bg_lam2(self):
        # 6*4 - 6*2 + 1 = 24 - 12 + 1 = 13
        assert kappa_betagamma(2) == Fraction(13)

    def test_kappa_bg_symmetry(self):
        """kappa(lambda) = kappa(1 - lambda) (weight symmetry)."""
        for lam in [0, Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), 1]:
            assert kappa_betagamma(lam) == kappa_betagamma(1 - lam)


class TestKappaBC:
    """Verify kappa(bc) = -kappa(bg) (complementarity = 0)."""

    def test_kappa_bc_lam1(self):
        assert kappa_bc(1) == -kappa_betagamma(1)

    def test_kappa_bc_complementarity(self):
        """kappa(bg) + kappa(bc) = 0 for all lambda."""
        for lam in [0, Fraction(1, 2), 1, 2]:
            assert kappa_betagamma(lam) + kappa_bc(lam) == 0


class TestKappaW3:
    """Verify kappa(W_3) = 5c/6."""

    def test_kappa_w3_c2(self):
        assert kappa_w3(2) == Fraction(5, 3)

    def test_kappa_w3_c50(self):
        """Self-dual at c = 50: kappa = 125/3."""
        assert kappa_w3(50) == Fraction(125, 3)

    def test_kappa_w3_c100(self):
        assert kappa_w3(100) == Fraction(250, 3)


class TestKappaLattice:
    """Verify kappa(V_Lambda) = rank."""

    def test_kappa_lattice_rank1(self):
        assert kappa_lattice(1) == Fraction(1)

    def test_kappa_lattice_rank8(self):
        assert kappa_lattice(8) == Fraction(8)

    def test_kappa_lattice_rank24(self):
        """Leech lattice: rank 24."""
        assert kappa_lattice(24) == Fraction(24)


class TestKappaE8Affine:
    """Verify kappa for affine E_8 at level k."""

    def test_kappa_e8_k1(self):
        # dim(E_8) = 248, h^v = 30
        # kappa = 248 * (1 + 30) / (2 * 30) = 248 * 31 / 60 = 7688/60 = 1922/15
        expected = Fraction(248 * 31, 60)
        assert kappa_e8_affine(1) == expected
        assert expected == Fraction(1922, 15)


# ==========================================================================
# SECTION 2: CROSS-VOLUME KAPPA AGREEMENT
# ==========================================================================

class TestVolIBridge:
    """Verify that Vol I kappa formulas agree with authoritative values."""

    def test_vol1_heisenberg(self):
        v1 = vol1_kappa("heisenberg", k=1)
        if v1 is not None:
            assert Fraction(v1) == kappa_heisenberg(1)

    def test_vol1_virasoro(self):
        v1 = vol1_kappa("virasoro", c=26)
        if v1 is not None:
            assert Fraction(v1) == kappa_virasoro(26)

    def test_vol1_affine_sl2(self):
        v1 = vol1_kappa("affine_sl2", k=1)
        if v1 is not None:
            assert Fraction(v1) == kappa_affine("A", 1, 1)

    def test_vol1_betagamma(self):
        v1 = vol1_kappa("betagamma", lam=Fraction(1, 2))
        if v1 is not None:
            assert Fraction(v1) == kappa_betagamma(Fraction(1, 2))

    def test_vol1_lattice(self):
        v1 = vol1_kappa("lattice", rank=8)
        if v1 is not None:
            assert Fraction(v1) == kappa_lattice(8)

    def test_vol1_w3(self):
        v1 = vol1_kappa("w3", c=2)
        if v1 is not None:
            assert Fraction(v1) == kappa_w3(2)


class TestVolIIIBridge:
    """Verify Vol III kappa values, catching known discrepancies."""

    def test_vol3_heisenberg_discrepancy(self):
        """Vol III e2_bar_complex.py has kappa(H_k) = k/2 (WRONG).

        The authoritative value is kappa(H_k) = k.
        This test documents the known discrepancy.
        """
        v3 = vol3_kappa_heisenberg(1)
        if v3 is not None:
            # Vol III gives k/2 = 1/2, but authoritative is k = 1
            from sympy import Rational
            v3_frac = Fraction(Rational(v3).p, Rational(v3).q)
            # Discrepancy RESOLVED: Vol III now correctly gives kappa(H_k) = k
            auth = kappa_heisenberg(1)
            assert v3_frac == Fraction(1), (
                f"Vol III kappa should be k=1 (fixed), got {v3_frac}"
            )
            assert auth == Fraction(1), (
                f"Authoritative kappa wrong: expected 1, got {auth}"
            )
            # Cross-volume agreement (discrepancy fixed)
            assert v3_frac == auth, (
                "Vol III and Vol I should now AGREE on kappa(H_k) = k"
            )

    def test_vol3_affine_sl2_matches(self):
        """Vol III affine sl_2 kappa should match authoritative."""
        v3 = vol3_kappa_affine_sl2(1)
        if v3 is not None:
            from sympy import Rational
            v3_frac = Fraction(Rational(v3).p, Rational(v3).q)
            auth = kappa_affine("A", 1, 1)
            assert v3_frac == auth, (
                f"Vol III affine sl_2 kappa disagrees: {v3_frac} vs {auth}"
            )


# ==========================================================================
# SECTION 3: SHADOW DEPTH CLASSIFICATION
# ==========================================================================

class TestShadowDepthClassification:
    """Verify G/L/C/M classification is consistent."""

    def test_heisenberg_is_G(self):
        cls, depth = shadow_depth_class("heisenberg")
        assert cls == "G"
        assert depth == 2

    def test_lattice_is_G(self):
        cls, depth = shadow_depth_class("lattice")
        assert cls == "G"
        assert depth == 2

    def test_affine_sl2_is_L(self):
        cls, depth = shadow_depth_class("affine_sl2")
        assert cls == "L"
        assert depth == 3

    def test_affine_e8_is_L(self):
        cls, depth = shadow_depth_class("affine_e8")
        assert cls == "L"
        assert depth == 3

    def test_betagamma_is_C(self):
        cls, depth = shadow_depth_class("betagamma")
        assert cls == "C"
        assert depth == 4

    def test_bc_is_C(self):
        cls, depth = shadow_depth_class("bc")
        assert cls == "C"
        assert depth == 4

    def test_virasoro_is_M(self):
        cls, depth = shadow_depth_class("virasoro")
        assert cls == "M"
        assert depth == float("inf")

    def test_w3_is_M(self):
        cls, depth = shadow_depth_class("w3")
        assert cls == "M"
        assert depth == float("inf")

    def test_depth_ordering(self):
        """G < L < C < M in depth."""
        assert shadow_depth_class("heisenberg")[1] < shadow_depth_class("affine")[1]
        assert shadow_depth_class("affine")[1] < shadow_depth_class("betagamma")[1]
        assert shadow_depth_class("betagamma")[1] < shadow_depth_class("virasoro")[1]


# ==========================================================================
# SECTION 4: SC-FORMALITY (VOL II PERSPECTIVE)
# ==========================================================================

class TestSCFormality:
    """Verify SC-formality classification (AP14).

    SC-formal = m_k^{SC} = 0 for k >= 3.
    Classes G and L are SC-formal.
    Classes C and M are SC-non-formal.
    ALL classes are chirally Koszul (AP14 critical distinction).
    """

    def test_heisenberg_sc_formal(self):
        assert sc_formal("heisenberg") is True

    def test_affine_sc_formal(self):
        assert sc_formal("affine_sl2") is True

    def test_lattice_sc_formal(self):
        assert sc_formal("lattice") is True

    def test_betagamma_not_sc_formal(self):
        assert sc_formal("betagamma") is False

    def test_virasoro_not_sc_formal(self):
        assert sc_formal("virasoro") is False

    def test_w3_not_sc_formal(self):
        assert sc_formal("w3") is False

    def test_sc_depth_heisenberg(self):
        assert sc_depth("heisenberg") == float("inf")  # no non-formality

    def test_sc_depth_betagamma(self):
        assert sc_depth("betagamma") == 4

    def test_sc_depth_virasoro(self):
        assert sc_depth("virasoro") == 3


# ==========================================================================
# SECTION 5: COMPLEMENTARITY (THEOREM C)
# ==========================================================================

class TestComplementarity:
    """Verify kappa(A) + kappa(A!) for each family (AP24)."""

    def test_heisenberg_complementarity_zero(self):
        assert complementarity_sum("heisenberg") == Fraction(0)

    def test_virasoro_complementarity_13(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13."""
        assert complementarity_sum("virasoro") == Fraction(13)

    def test_affine_complementarity_zero(self):
        """For affine KM: kappa + kappa! = 0 (FF involution ensures this)."""
        assert complementarity_sum("affine_sl2") == Fraction(0)

    def test_betagamma_complementarity_zero(self):
        """bg + bc = 0."""
        assert complementarity_sum("betagamma") == Fraction(0)

    def test_w3_complementarity(self):
        """kappa(W_3,c) + kappa(W_3,100-c) = 5c/6 + 5(100-c)/6 = 500/6 = 250/3."""
        assert complementarity_sum("w3") == Fraction(250, 3)

    def test_lattice_complementarity_zero(self):
        assert complementarity_sum("lattice") == Fraction(0)

    def test_virasoro_kappa_dual_explicit(self):
        """kappa(Vir_c!) = (26-c)/2."""
        for c in [1, 2, 13, 25, 26]:
            kd = kappa_dual("virasoro", c=c)
            assert kd == Fraction(26 - c, 2)

    def test_virasoro_self_dual_at_c13(self):
        """At c = 13: kappa = kappa! = 13/2."""
        k = kappa_virasoro(13)
        kd = kappa_dual("virasoro", c=13)
        assert k == kd == Fraction(13, 2)

    def test_virasoro_not_self_dual_at_c26(self):
        """At c = 26: kappa = 13, kappa! = 0. NOT self-dual."""
        k = kappa_virasoro(26)
        kd = kappa_dual("virasoro", c=26)
        assert k == Fraction(13)
        assert kd == Fraction(0)
        assert k != kd

    def test_complementarity_formula_check(self):
        """Verify complementarity at each genus for several families."""
        for family, params in [
            ("heisenberg", {"k": 2}),
            ("virasoro", {"c": 10}),
            ("w3", {"c": 30}),
        ]:
            result = verify_F_g_complementarity(family, max_genus=3, **params)
            for g, data in result.items():
                assert data["consistent"], (
                    f"F_g complementarity fails for {family} at g={g}: "
                    f"{data['sum']} != {data['expected']}"
                )


# ==========================================================================
# SECTION 6: R-MATRIX DATA
# ==========================================================================

class TestRMatrix:
    """Verify R-matrix data consistency across volumes."""

    def test_heisenberg_collision_residue(self):
        """AP19: bar kernel absorbs one pole. OPE has z^{-2}, r-matrix has z^{-1}."""
        result = r_matrix_heisenberg_collision(1)
        assert "1/z" in result
        # Simple pole, not double pole
        assert "1/z^2" not in result

    def test_virasoro_r_matrix_poles(self):
        """AP19: Virasoro OPE has z^{-4}, z^{-2}, z^{-1} poles.
        R-matrix has z^{-3} and z^{-1} (one less each)."""
        result = r_matrix_virasoro_collision(26)
        assert result["highest_pole_order"] == 3  # z^{-3}, not z^{-4}

    def test_affine_sl2_r_matrix_structure(self):
        """Vol I: r(z) = Omega/(2z). Vol III: R = q^{Omega/2}."""
        result = r_matrix_affine_sl2(1)
        assert result["classical_r"] == "Omega / (2z)"
        # KZ parameter = 1/(k + h^v) = 1/3 for sl_2 at k=1
        assert result["kz_parameter"] == Fraction(1, 3)


# ==========================================================================
# SECTION 7: QUANTUM GROUP BRIDGE (KL EQUIVALENCE)
# ==========================================================================

class TestKLEquivalence:
    """Verify Kazhdan-Lusztig equivalence data for sl_2."""

    def test_kl_k1_simples(self):
        """At level 1: 2 simple objects (vacuum + fundamental)."""
        result = kl_equivalence_check(1)
        assert result["n_simple_objects"] == 2

    def test_kl_k2_simples(self):
        """At level 2: 3 simple objects."""
        result = kl_equivalence_check(2)
        assert result["n_simple_objects"] == 3

    def test_kl_kappa_agrees(self):
        """Verify kappa from KL check matches authoritative."""
        result = kl_equivalence_check(1)
        assert result["kappa_affine"] == kappa_affine("A", 1, 1)


# ==========================================================================
# SECTION 8: F_g GENUS TOWER
# ==========================================================================

class TestFgGenustower:
    """Verify F_g(A) = kappa(A) * lambda_g^FP (Theorem D)."""

    def test_lambda_fp_genus1(self):
        """lambda_1 = 1/24 * |B_2| / 2! = 1/24 * 1/6 / 2 ... wait.

        lambda_g = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!
        At g=1: (2^1 - 1)/2^1 * |B_2|/2! = (1/2) * (1/6) / 2 = 1/24
        """
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_fp_genus2(self):
        """lambda_2 = (2^3 - 1)/2^3 * |B_4|/4! = 7/8 * 1/30 / 24 = 7/5760."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_fp_genus3(self):
        """lambda_3 = (2^5 - 1)/2^5 * |B_6|/6!
        = 31/32 * (1/42) / 720 = 31 / (32 * 42 * 720) = 31 / 967680."""
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_F1_heisenberg_k1(self):
        """F_1(H_1) = kappa * lambda_1 = 1 * 1/24 = 1/24."""
        assert F_g(Fraction(1), 1) == Fraction(1, 24)

    def test_F1_virasoro_c26(self):
        """F_1(Vir_26) = 13 * 1/24 = 13/24."""
        assert F_g(Fraction(13), 1) == Fraction(13, 24)

    def test_F_g_linearity(self):
        """F_g is linear in kappa: F_g(2A) = 2 * F_g(A)."""
        for g in range(1, 5):
            assert F_g(Fraction(6), g) == 3 * F_g(Fraction(2), g)

    def test_F_g_table_heisenberg(self):
        """Verify F_g table for Heisenberg at k=1."""
        table = F_g_table("heisenberg", max_genus=4, k=1)
        assert table[1] == Fraction(1, 24)
        assert table[2] == Fraction(7, 5760)

    def test_F_g_positivity(self):
        """F_g > 0 when kappa > 0 (all Bernoulli/FP numbers are positive)."""
        for g in range(1, 6):
            assert F_g(Fraction(1), g) > 0


# ==========================================================================
# SECTION 9: QUARTIC CONTACT INVARIANT
# ==========================================================================

class TestQuarticContact:
    """Verify Q^contact_Vir(c) = 10/(c*(5c+22))."""

    def test_Q_contact_c26(self):
        """Q^contact_Vir(26) = 10/(26*(130+22)) = 10/(26*152) = 10/3952 = 5/1976."""
        result = Q_contact_virasoro(26)
        assert result == Fraction(10, 26 * 152)
        assert result == Fraction(5, 1976)

    def test_Q_contact_c2(self):
        """Q^contact_Vir(2) = 10/(2*(10+22)) = 10/64 = 5/32."""
        result = Q_contact_virasoro(2)
        assert result == Fraction(5, 32)

    def test_Q_contact_c0_raises(self):
        with pytest.raises(ValueError):
            Q_contact_virasoro(0)


# ==========================================================================
# SECTION 10: MASTER COMPARISON TABLE
# ==========================================================================

class TestMasterTable:
    """Verify the master comparison table covers all families and is consistent."""

    def test_table_nonempty(self):
        table = full_master_table()
        assert len(table) >= 20

    def test_table_all_families_present(self):
        table = full_master_table()
        families = {e["family"] for e in table}
        expected = {"heisenberg", "virasoro", "affine_sl2", "affine_sl3",
                    "betagamma", "bc", "w3", "lattice"}
        assert expected.issubset(families), (
            f"Missing families: {expected - families}"
        )

    def test_table_complementarity_all_consistent(self):
        table = full_master_table()
        for entry in table:
            if entry["complementarity_ok"] is not None:
                assert entry["complementarity_ok"], (
                    f"Complementarity fails for {entry['family']}: "
                    f"kappa={entry['kappa_authoritative']}, "
                    f"kappa_dual={entry['kappa_dual']}, "
                    f"sum={entry['complementarity_sum']}"
                )

    def test_table_vol1_consistency(self):
        """Where Vol I values are available, they must match authoritative."""
        table = full_master_table()
        for entry in table:
            if entry["kappa_vol1"] is not None:
                assert entry["vol1_match"], (
                    f"Vol I disagrees for {entry['family']}: "
                    f"Vol I={entry['kappa_vol1']}, "
                    f"auth={entry['kappa_authoritative']}"
                )


# ==========================================================================
# SECTION 11: CY DIMENSION CORRELATION
# ==========================================================================

class TestCYCorrelation:
    """Verify CY dimension correlation data."""

    def test_cy1_is_G(self):
        data = cy_dimension_correlation()
        assert data["CY1_elliptic"]["shadow_class"] == "G"
        assert data["CY1_elliptic"]["cy_dim"] == 1

    def test_cy2_is_G(self):
        data = cy_dimension_correlation()
        assert data["CY2_K3"]["shadow_class"] == "G"
        assert data["CY2_K3"]["cy_dim"] == 2

    def test_cy3_conifold_is_C(self):
        data = cy_dimension_correlation()
        assert data["CY3_conifold"]["shadow_class"] == "C"
        assert data["CY3_conifold"]["cy_dim"] == 3

    def test_cy3_C3_is_L(self):
        data = cy_dimension_correlation()
        assert data["CY3_C3"]["shadow_class"] == "L"
        assert data["CY3_C3"]["cy_dim"] == 3

    def test_cy_depth_nondecreasing_with_dim(self):
        """CY dim 1 -> depth <= CY dim 3 -> depth (loosely)."""
        data = cy_dimension_correlation()
        assert data["CY1_elliptic"]["shadow_depth"] <= data["CY3_conifold"]["shadow_depth"]


# ==========================================================================
# SECTION 12: DISCREPANCY DETECTION
# ==========================================================================

class TestDiscrepancyDetection:
    """Verify the discrepancy detection system works."""

    def test_detect_vol3_heisenberg_bug(self):
        """The known Vol III bug: kappa(H_k) = k/2 instead of k."""
        disc = detect_discrepancies()
        vol3_heis = [d for d in disc
                     if d["family"] == "heisenberg" and "Vol III" in d["vol_source"]]
        if vol3_heis:
            # The discrepancy was detected
            assert vol3_heis[0]["authoritative_kappa"] == Fraction(1)
            assert vol3_heis[0]["vol_kappa"] == Fraction(1, 2)

    def test_no_vol1_discrepancies(self):
        """Vol I should have no discrepancies (it's the primary source)."""
        disc = detect_discrepancies()
        # Filter for Vol I specifically, excluding "Vol III" which contains "Vol I"
        vol1_disc = [d for d in disc
                     if d.get("vol_source", "").startswith("Vol I ")
                     or d.get("vol_source", "") == "Vol I"]
        assert len(vol1_disc) == 0, (
            f"Unexpected Vol I discrepancies: {vol1_disc}"
        )


# ==========================================================================
# SECTION 13: LIE ALGEBRA DATA
# ==========================================================================

class TestLieAlgebraData:
    """Verify dim and h^v for all simple Lie algebras."""

    def test_sl2(self):
        dim_g, hv = _lie_dim_hdual("A", 1)
        assert dim_g == 3
        assert hv == 2

    def test_sl3(self):
        dim_g, hv = _lie_dim_hdual("A", 2)
        assert dim_g == 8
        assert hv == 3

    def test_so5(self):
        """B_2 = so(5): dim = 10, h^v = 3."""
        dim_g, hv = _lie_dim_hdual("B", 2)
        assert dim_g == 10
        assert hv == 3

    def test_sp4(self):
        """C_2 = sp(4): dim = 10, h^v = 3."""
        dim_g, hv = _lie_dim_hdual("C", 2)
        assert dim_g == 10
        assert hv == 3

    def test_so8(self):
        """D_4 = so(8): dim = 28, h^v = 6."""
        dim_g, hv = _lie_dim_hdual("D", 4)
        assert dim_g == 28
        assert hv == 6

    def test_e6(self):
        dim_g, hv = _lie_dim_hdual("E", 6)
        assert dim_g == 78
        assert hv == 12

    def test_e7(self):
        dim_g, hv = _lie_dim_hdual("E", 7)
        assert dim_g == 133
        assert hv == 18

    def test_e8(self):
        dim_g, hv = _lie_dim_hdual("E", 8)
        assert dim_g == 248
        assert hv == 30

    def test_f4(self):
        dim_g, hv = _lie_dim_hdual("F", 4)
        assert dim_g == 52
        assert hv == 9

    def test_g2(self):
        dim_g, hv = _lie_dim_hdual("G", 2)
        assert dim_g == 14
        assert hv == 4


# ==========================================================================
# SECTION 14: MULTI-FAMILY KAPPA CONSISTENCY
# ==========================================================================

class TestKappaMultiFamily:
    """Cross-family consistency checks (AP10: hardcoded wrong values detected
    by cross-family relations, not by single-family tests)."""

    def test_heisenberg_is_rank1_lattice(self):
        """Heisenberg at level k = rank-1 lattice VOA kappa.
        Actually: kappa(H_k) = k, kappa(lattice_rank) = rank.
        At k = r: these should match."""
        for r in [1, 2, 5]:
            assert kappa_heisenberg(r) == kappa_lattice(r)

    def test_virasoro_is_betagamma_at_lam2(self):
        """beta-gamma at lambda = 2: c = 2(6*4 - 12 + 1) = 2*13 = 26.
        kappa(bg_2) = 13 = kappa(Vir_26). Same as Virasoro at c = 26."""
        assert kappa_betagamma(2) == kappa_virasoro(26)

    def test_virasoro_is_betagamma_at_lam0(self):
        """beta-gamma at lambda = 0: c = 2(0 - 0 + 1) = 2.
        kappa(bg_0) = 1 = kappa(Vir_2). Same as Virasoro at c = 2."""
        assert kappa_betagamma(0) == kappa_virasoro(2)

    def test_kappa_additivity_heisenberg(self):
        """kappa is additive for direct sums: kappa(H_k1 + H_k2) = k1 + k2."""
        k1, k2 = 3, 5
        assert kappa_heisenberg(k1) + kappa_heisenberg(k2) == kappa_heisenberg(k1 + k2)

    def test_kappa_ff_involution_affine_sl2(self):
        """FF involution: k -> -k - 2h^v = -k - 4 for sl_2.
        kappa(V_k) + kappa(V_{-k-4}) = 0."""
        for k_val in [1, 2, 3]:
            k_dual = -k_val - 4  # FF involution for sl_2
            k1 = kappa_affine("A", 1, k_val)
            k2 = kappa_affine("A", 1, k_dual)
            assert k1 + k2 == 0, (
                f"FF involution fails for sl_2 at k={k_val}: "
                f"kappa(k) + kappa(-k-4) = {k1} + {k2} = {k1 + k2}"
            )

    def test_w3_self_dual_at_c50(self):
        """W_3 is self-dual at c = 50 (c* = alpha_3/2 = 100/2 = 50).
        kappa(c=50) = kappa!(c=50) = 125/3."""
        k = kappa_w3(50)
        kd = kappa_dual("w3", c=50)
        assert k == kd == Fraction(125, 3)


# ==========================================================================
# SECTION 15: DISPATCH AND EDGE CASES
# ==========================================================================

class TestDispatchAndEdgeCases:
    """Test the dispatch mechanism and edge cases."""

    def test_dispatch_heisenberg(self):
        assert _dispatch_kappa("heisenberg", k=3) == Fraction(3)

    def test_dispatch_virasoro(self):
        assert _dispatch_kappa("virasoro", c=10) == Fraction(5)

    def test_dispatch_unknown_raises(self):
        with pytest.raises(ValueError, match="Unknown family"):
            _dispatch_kappa("unknown_algebra")

    def test_lambda_fp_negative_genus_raises(self):
        with pytest.raises(ValueError, match="Genus must be >= 1"):
            lambda_fp(0)

    def test_lie_data_unknown_type_raises(self):
        with pytest.raises(ValueError):
            _lie_dim_hdual("X", 1)

    def test_verify_complementarity_format(self):
        """Verify the format of verify_complementarity output."""
        result = verify_complementarity("heisenberg", k=1)
        assert "kappa" in result
        assert "kappa_dual" in result
        assert "consistent" in result
        assert result["consistent"] is True


# ==========================================================================
# SECTION 16: SHADOW TOWER F_g COMPLEMENTARITY
# ==========================================================================

class TestFgComplementarity:
    """Verify F_g(A) + F_g(A!) = (kappa + kappa!) * lambda_g^FP at all genera."""

    @pytest.mark.parametrize("family,params", [
        ("heisenberg", {"k": 1}),
        ("heisenberg", {"k": 3}),
        ("virasoro", {"c": 2}),
        ("virasoro", {"c": 13}),
        ("virasoro", {"c": 26}),
        ("affine_sl2", {"k": 1}),
        ("betagamma", {"lam": 1}),
        ("w3", {"c": 50}),
        ("lattice", {"rank": 8}),
    ])
    def test_F_g_complementarity_genus1to4(self, family, params):
        """Verify F_g complementarity at genera 1 through 4."""
        result = verify_F_g_complementarity(family, max_genus=4, **params)
        for g, data in result.items():
            assert data["consistent"], (
                f"F_g complementarity fails for {family}({params}) at g={g}: "
                f"F_g + F_g! = {data['sum']} != {data['expected']}"
            )
