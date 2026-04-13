r"""Tests for drinfeld_center_affine_km_engine.py: verification of
conj:v3-drinfeld-center-equals-bulk for A = V_k(sl_2).

CENTRAL RESULTS:
    (1) ChirHoch*(V_k(sl_2)) = [1, 3, 1], total dim 5 (THEOREM H + explicit).
    (2) Drin(V_k(sl_2)) has dim 7 = 2*dim(sl_2) + 1 (THEOREM: Drinfeld double).
    (3) kappa_ch(V_k(sl_2)) = 3(k+2)/4, with Sugawara shift decomposition (C3/C13).
    (4) kappa + kappa' = 0 for KM family (C18, Koszul conductor = 0).
    (5) Euler char chi = -1 = (-1)^{dim(sl_2)} (THEOREM H).
    (6) Shadow class L, depth 3 (THEOREM: shadow classification).
    (7) r-matrix: trace-form k*Omega/z, KZ Omega/((k+2)z) (C9/AP126/AP148).
    (8) At integrable k=1: Verlinde algebra dim 2 (2 simple modules).
    (9) P_3 bracket {X,Y} = (1/(k+2))*(X,Y) at E_3 level (prop:e3-explicit-sl2).
    (10) All numerical invariants CONSISTENT (level sweep over 6 values).

Ground truth sources:
    [DC] chirhoch_dimension_engine.py: chirhoch_affine_km("sl_2") -> (1, 3, 1)
    [DC] e3_bv_sl2_derived_center_engine.py: 5-dim derived center
    [DC] verlinde_bulk_check.py: Verlinde algebra dim k+1
    [LT] Kassel, "Quantum Groups" (1995), Ch. IX (Drinfeld doubles)
    [LT] Verlinde (1988), Huang (2005) (modular tensor categories)
    [LT] Feigin-Frenkel (1992) (dual levels, Koszul duality for affine KM)
    [LC] k=0: kappa = 3/2 = dim(g)/2 (NOT zero), r-matrix vanishes (trace-form)
    [LC] k=-2: critical level, kappa=0, Sugawara undefined
    [SY] kappa_ch + kappa_ch^! = 0 (C18: KM family)
    [CF] landscape_census.tex: kappa(V_k(sl_2)) = 3(k+2)/4, class L, depth 3

Manuscript references:
    Vol III: drinfeld_center.tex:558 (conj:v3-drinfeld-center-equals-bulk)
    Vol I:   chiral_hochschild_koszul.tex (Theorem H)
             en_koszul_duality.tex (prop:e3-explicit-sl2)
             landscape_census.tex (kappa census)
    Vol II:  thqg_holographic_reconstruction.tex (ChirHoch*)
             verlinde_bulk_check.py (Verlinde algebra)
"""

import pytest
import math
from fractions import Fraction

from compute.lib.drinfeld_center_affine_km_engine import (
    # Constants
    DIM_SL2,
    RANK_SL2,
    H_VEE_SL2,
    SL2_GENERATORS,
    SL2_BRACKET,
    SL2_KILLING_FORM,
    CASIMIR_COMPONENTS,
    ADJOINT_CASIMIR_EIGENVALUE,
    CHIRHOCH_GENERATORS,
    CHIRHOCH_DIMS,
    CHIRHOCH_TOTAL_DIM,
    CHIRHOCH_EULER_CHAR,
    SHADOW_CLASS,
    SHADOW_DEPTH,
    # ChirHoch
    chirhoch_graded_dims,
    chirhoch_poincare_eval,
    chirhoch_euler_char,
    chiral_derived_center_sl2,
    # Central charge and kappa
    central_charge_sl2,
    dual_level_sl2,
    kappa_ch_sl2,
    kappa_ch_dual_sl2,
    kappa_complementarity_sl2,
    sugawara_shift_check,
    # R-matrix
    r_matrix_sl2,
    # Drinfeld double
    drinfeld_double_sl2,
    drinfeld_double_bracket_sl2,
    center_of_drinfeld_double_sl2,
    # Verlinde
    verlinde_dim,
    verlinde_simple_modules,
    verlinde_fusion_sl2,
    verlinde_s_matrix_entry,
    # Comparison
    compare_grothendieck_invariants_sl2,
    compare_e3_structure_sl2,
    compare_at_integrable_level,
    # AP compliance
    ap126_r_matrix_check,
    ap132_bar_complex_check,
    ap141_kz_convention_check,
    # Cross-verification
    cross_verify_chirhoch_dims_sl2,
    cross_verify_kappa_sl2,
    cross_verify_verlinde_sl2,
    # Level sweep and full verification
    verify_at_level,
    verify_level_sweep,
    full_verification,
)

F = Fraction


# =========================================================================
# Section 1: Lie algebra constants
# =========================================================================

class TestSl2Constants:
    """Verify sl_2 Lie algebra constants."""

    def test_dim_sl2(self):
        """dim(sl_2) = 3."""
        # VERIFIED: [DC] standard Lie theory.
        assert DIM_SL2 == 3

    def test_rank_sl2(self):
        """rank(sl_2) = 1."""
        assert RANK_SL2 == 1

    def test_dual_coxeter_sl2(self):
        """h^v(sl_2) = 2."""
        # VERIFIED: [LT] Kac, "Infinite-dimensional Lie algebras", Table Aff 1.
        assert H_VEE_SL2 == F(2)

    def test_killing_form_nondeg(self):
        """Killing form is non-degenerate: det = (e,f)^2 * (h,h) != 0."""
        # VERIFIED: [DC] (e,f) = 1, (h,h) = 2. Matrix [[0,1,0],[1,0,0],[0,0,2]].
        # det = -1 * (-1) * 2 = 2 != 0 (or directly: 1 * 1 * 2 with sign).
        ef = SL2_KILLING_FORM[("e", "f")]
        hh = SL2_KILLING_FORM[("h", "h")]
        assert ef == F(1)
        assert hh == F(2)
        assert ef != F(0) and hh != F(0)

    def test_lie_bracket_efh(self):
        """[e, f] = h, [h, e] = 2e, [h, f] = -2f."""
        assert SL2_BRACKET[("e", "f")] == {"h": F(1)}
        assert SL2_BRACKET[("h", "e")] == {"e": F(2)}
        assert SL2_BRACKET[("h", "f")] == {"f": F(-2)}

    def test_lie_bracket_antisymmetry(self):
        """[X, Y] = -[Y, X] for all basis pairs."""
        for X in SL2_GENERATORS:
            for Y in SL2_GENERATORS:
                br_xy = SL2_BRACKET.get((X, Y), {})
                br_yx = SL2_BRACKET.get((Y, X), {})
                for gen in set(list(br_xy.keys()) + list(br_yx.keys())):
                    assert br_xy.get(gen, F(0)) == -br_yx.get(gen, F(0)), (
                        f"Antisymmetry fails for [{X}, {Y}] at generator {gen}"
                    )

    def test_adjoint_casimir_eigenvalue(self):
        """Adjoint Casimir eigenvalue = 2*h^v = 4 for sl_2."""
        # VERIFIED: [DC] tr(ad_e ad_f) = 4 (direct computation).
        # [LT] C_2(ad) = 2 * h^v for any simple g.
        assert ADJOINT_CASIMIR_EIGENVALUE == F(4)

    def test_casimir_trace(self):
        """tr(Omega) = sum (X^a, X_a) = dim(g) in normalised form.

        Omega = e tensor f + f tensor e + (1/2) h tensor h.
        Trace = (e,f) + (f,e) + (1/2)(h,h) = 1 + 1 + 1 = 3 = dim(sl_2).
        """
        # VERIFIED: [DC] direct computation.
        trace = F(0)
        for (a, b), coeff in CASIMIR_COMPONENTS.items():
            trace += coeff * SL2_KILLING_FORM.get((a, b), F(0))
        assert trace == F(DIM_SL2)


# =========================================================================
# Section 2: ChirHoch dimensions (derived center)
# =========================================================================

class TestChirHochDimensions:
    """ChirHoch*(V_k(sl_2)) = [1, 3, 1], total dim 5."""

    def test_graded_dims(self):
        """Graded dimensions [1, 3, 1]."""
        # VERIFIED: [DC] chirhoch_dimension_engine.py
        # [DC] e3_bv_sl2_derived_center_engine.py
        assert CHIRHOCH_DIMS == [1, 3, 1]

    def test_total_dim(self):
        """Total dimension = 5."""
        # VERIFIED: [DC] 1 + 3 + 1 = 5.
        # [CF] sl_2 is the minimal counterexample to old "dim <= 4" claim.
        assert CHIRHOCH_TOTAL_DIM == 5

    def test_euler_char(self):
        """Euler characteristic chi = 1 - 3 + 1 = -1."""
        # VERIFIED: [DC] direct computation.
        # [SY] chi = (-1)^{dim(g)} = (-1)^3 = -1.
        assert CHIRHOCH_EULER_CHAR == -1
        assert chirhoch_euler_char() == -1

    def test_poincare_at_minus_1(self):
        """P(-1) = 1 - 3 + 1 = -1 (= Euler char)."""
        assert chirhoch_poincare_eval(F(-1)) == F(-1)

    def test_poincare_at_1(self):
        """P(1) = 1 + 3 + 1 = 5 (= total dimension)."""
        assert chirhoch_poincare_eval(F(1)) == F(5)

    def test_concentrated_in_0_1_2(self):
        """ChirHoch^n = 0 for n >= 3 (Theorem H amplitude bound)."""
        dims = chirhoch_graded_dims(6)
        for n in range(3, 7):
            assert dims[n] == 0, f"ChirHoch^{n} should be 0"

    def test_generators_structure(self):
        """Generators: 1 in deg 0, {e,f,h} in deg 1, eta in deg 2."""
        assert CHIRHOCH_GENERATORS["unit"]["degree"] == 0
        assert CHIRHOCH_GENERATORS["unit"]["dim"] == 1
        assert CHIRHOCH_GENERATORS["currents"]["degree"] == 1
        assert CHIRHOCH_GENERATORS["currents"]["dim"] == 3
        assert CHIRHOCH_GENERATORS["deformation"]["degree"] == 2
        assert CHIRHOCH_GENERATORS["deformation"]["dim"] == 1

    def test_cdc_structure(self):
        """Full chiral derived center data at k=1."""
        cdc = chiral_derived_center_sl2(F(1))
        assert cdc["total_dim"] == 5
        assert cdc["euler_char"] == -1
        assert cdc["concentrated_in"] == [0, 1, 2]
        assert cdc["shadow_class"] == "L"
        assert cdc["shadow_depth"] == 3
        assert cdc["p3_bracket_coefficient"] == F(1, 3)  # 1/(1+2) = 1/3

    def test_cdc_critical_level_raises(self):
        """Critical level k=-2 raises ValueError."""
        with pytest.raises(ValueError, match="Critical level"):
            chiral_derived_center_sl2(F(-2))


# =========================================================================
# Section 3: Central charge and kappa
# =========================================================================

class TestCentralChargeKappa:
    """c(V_k(sl_2)) and kappa_ch(V_k(sl_2))."""

    def test_central_charge_k0(self):
        """c(V_0(sl_2)) = 0."""
        assert central_charge_sl2(F(0)) == F(0)

    def test_central_charge_k1(self):
        """c(V_1(sl_2)) = 3*1/(1+2) = 1."""
        assert central_charge_sl2(F(1)) == F(1)

    def test_central_charge_k_minus_4(self):
        """c(V_{-4}(sl_2)) = 3*(-4)/(-4+2) = -12/(-2) = 6."""
        assert central_charge_sl2(F(-4)) == F(6)

    def test_central_charge_critical_raises(self):
        """c at k=-2 raises ValueError (Sugawara undefined)."""
        with pytest.raises(ValueError, match="Critical level"):
            central_charge_sl2(F(-2))

    def test_dual_level(self):
        """k' = -k - 4."""
        assert dual_level_sl2(F(1)) == F(-5)
        assert dual_level_sl2(F(0)) == F(-4)
        assert dual_level_sl2(F(-1)) == F(-3)

    def test_dual_level_involution(self):
        """(k')' = k (the duality is an involution)."""
        for k_val in [F(0), F(1), F(-1), F(1, 2)]:
            assert dual_level_sl2(dual_level_sl2(k_val)) == k_val

    def test_kappa_k0(self):
        """kappa_ch(V_0(sl_2)) = 3*2/4 = 3/2 = dim(g)/2 (NOT zero; C3)."""
        # VERIFIED: [DC] C3: k=0 -> dim(g)/2 = 3/2.
        # [LC] This is the boundary value check for KM kappa.
        assert kappa_ch_sl2(F(0)) == F(3, 2)

    def test_kappa_k1(self):
        """kappa_ch(V_1(sl_2)) = 3*3/4 = 9/4."""
        assert kappa_ch_sl2(F(1)) == F(9, 4)

    def test_kappa_critical(self):
        """kappa_ch(V_{-2}(sl_2)) = 3*0/4 = 0 (critical level)."""
        assert kappa_ch_sl2(F(-2)) == F(0)

    def test_kappa_complementarity(self):
        """kappa + kappa' = 0 for all test levels (C18)."""
        # VERIFIED: [SY] KM family: Koszul conductor = 0.
        for k_val in [F(0), F(1), F(-1), F(1, 2), F(7), F(-3, 2)]:
            kc = kappa_complementarity_sl2(k_val)
            assert kc["match"], f"Complementarity failed at k={k_val}"
            assert kc["sum"] == F(0)

    def test_sugawara_shift_decomposition(self):
        """kappa = kappa_dp + kappa_sp = 3k/4 + 3/2 (C13/FM11)."""
        # VERIFIED: [DC] C13: av(r) + dim(g)/2 = kappa for non-abelian KM.
        for k_val in [F(0), F(1), F(-1), F(1, 2)]:
            sug = sugawara_shift_check(k_val)
            assert sug["decomposition_match"], (
                f"Sugawara decomposition failed at k={k_val}"
            )


# =========================================================================
# Section 4: R-matrix
# =========================================================================

class TestRMatrix:
    """Classical r-matrix for V_k(sl_2)."""

    def test_trace_form_coefficient(self):
        """Trace-form: r-matrix coefficient = k."""
        # VERIFIED: [DC] C9: r(z) = k*Omega/z.
        for k_val in [F(1), F(-1), F(1, 2)]:
            r = r_matrix_sl2(k_val, "trace")
            assert r["coefficient"] == k_val

    def test_ap126_trace_k0_vanishes(self):
        """AP126: r(z)|_{k=0} = 0 in trace-form convention."""
        # VERIFIED: [LC] trace-form r = 0*Omega/z = 0.
        r = r_matrix_sl2(F(0), "trace")
        assert r["k_equals_0_vanishes"]

    def test_kz_k0_nonzero(self):
        """KZ: r(z)|_{k=0} = Omega/(2z) != 0 (non-abelian bracket persists)."""
        # VERIFIED: [DC] C9: KZ convention gives Omega/(h^v*z) at k=0.
        r = r_matrix_sl2(F(0), "KZ")
        assert r["k_equals_0_nonzero"]
        assert r["k_equals_0_value"] == F(1, 2)

    def test_kz_critical_raises(self):
        """KZ convention diverges at k=-2 (critical level)."""
        with pytest.raises(ValueError, match="KZ convention diverges"):
            r_matrix_sl2(F(-2), "KZ")

    def test_pole_order(self):
        """r-matrix pole order 1 (OPE pole 2, d-log absorbs 1; AP19/C12)."""
        r = r_matrix_sl2(F(1), "trace")
        assert r["pole_order"] == 1
        assert r["ope_pole_order"] == 2

    def test_kz_coefficient_at_k1(self):
        """KZ: coefficient = 1/(k+2) = 1/3 at k=1."""
        r = r_matrix_sl2(F(1), "KZ")
        assert r["coefficient"] == F(1, 3)


# =========================================================================
# Section 5: Drinfeld double
# =========================================================================

class TestDrinfeldDouble:
    """Drinfeld double Drin(V_k(sl_2))."""

    def test_dim_is_7(self):
        """Drin(V_k(sl_2)) has dim 7 = 2*3 + 1."""
        # VERIFIED: [DC] 3 original + 3 dual + 1 central = 7.
        dd = drinfeld_double_sl2(F(1))
        assert dd.dim == 7

    def test_generators_count(self):
        """3 original + 3 dual generators."""
        dd = drinfeld_double_sl2(F(1))
        assert dd.original_generators == 3
        assert dd.dual_generators == 3
        assert dd.central_dim == 1

    def test_cross_bracket_coeff(self):
        """Cross-bracket coefficient = 1/(k+2) = h_KZ."""
        dd = drinfeld_double_sl2(F(1))
        assert dd.cross_bracket_coeff == F(1, 3)  # 1/(1+2) = 1/3

    def test_dual_level(self):
        """Dual level k' = -k-4."""
        dd = drinfeld_double_sl2(F(1))
        assert dd.dual_level == F(-5)

    def test_original_bracket_ef(self):
        """Original sector: [e, f] = h."""
        br = drinfeld_double_bracket_sl2(F(1), "e", "f", "original")
        assert br == {"h": F(1)}

    def test_dual_bracket_ef_negated(self):
        """Dual sector: [e', f'] = -h (co-opposite)."""
        br = drinfeld_double_bracket_sl2(F(1), "e", "f", "dual")
        assert br == {"h": F(-1)}

    def test_cross_bracket_ef(self):
        """Cross: [e, f'] = h_KZ * (e,f) * c = (1/3)*1*c = (1/3)c."""
        br = drinfeld_double_bracket_sl2(F(1), "e", "f", "cross")
        assert br == {"c": F(1, 3)}

    def test_cross_bracket_hh(self):
        """Cross: [h, h'] = h_KZ * (h,h) * c = (1/3)*2*c = (2/3)c."""
        br = drinfeld_double_bracket_sl2(F(1), "h", "h", "cross")
        assert br == {"c": F(2, 3)}

    def test_cross_bracket_ee_vanishes(self):
        """Cross: [e, e'] = h_KZ * (e,e) * c = 0 (orthogonal)."""
        br = drinfeld_double_bracket_sl2(F(1), "e", "e", "cross")
        assert br == {}

    def test_center_dim_generic(self):
        """At generic k != -2: center = span{c}, dim 1."""
        # VERIFIED: [DC] non-degenerate Killing form forces center = {c}.
        for k_val in [F(0), F(1), F(-1), F(1, 2)]:
            z = center_of_drinfeld_double_sl2(k_val)
            assert z["dim"] == 1
            assert not z["is_degenerate"]

    def test_center_k0_still_dim1(self):
        """At k=0: center still dim 1 (unlike Heisenberg where k=0 -> dim 3).

        For sl_2: the Lie bracket [e,f]=h is NON-TRIVIAL even at k=0.
        The double has h_KZ = 1/2 != 0, so cross-bracket non-degenerate.
        """
        # VERIFIED: [DC] Non-abelian g -> center always 1-dim at non-critical.
        z = center_of_drinfeld_double_sl2(F(0))
        assert z["dim"] == 1


# =========================================================================
# Section 6: Verlinde algebra at integrable levels
# =========================================================================

class TestVerlinde:
    """Verlinde algebra of V_k(sl_2) at integrable levels."""

    def test_verlinde_dim_k1(self):
        """k=1: dim = 2 (two simple modules L_0, L_1)."""
        # VERIFIED: [LT] Verlinde (1988). [DC] verlinde_bulk_check.py.
        assert verlinde_dim(1) == 2

    def test_verlinde_dim_k2(self):
        """k=2: dim = 3 (three simple modules L_0, L_1, L_2)."""
        assert verlinde_dim(2) == 3

    def test_verlinde_dim_general(self):
        """k -> k+1 for k = 1, ..., 5."""
        for k_val in range(1, 6):
            assert verlinde_dim(k_val) == k_val + 1

    def test_simple_modules_k1(self):
        """k=1: L_0 (trivial, dim 1, h=0) and L_1 (fund, dim 2, h=3/8)."""
        modules = verlinde_simple_modules(1)
        assert len(modules) == 2
        assert modules[0]["highest_weight"] == 0
        assert modules[0]["conformal_weight"] == F(0)
        assert modules[0]["is_vacuum"]
        assert modules[1]["highest_weight"] == 1
        assert modules[1]["conformal_weight"] == F(1, 4)
        # h_j = j(j+2)/(4(k+2)). At j=1, k=1: 1*3/(4*3) = 1/4.
        # Convention: j is the Dynkin label = 2*spin.
        # For spin-1/2 (the fundamental): j=1, h = 1/4.

    def test_fusion_k1(self):
        """k=1: L_1 x L_1 = L_0 (Z/2 fusion)."""
        # VERIFIED: [DC] truncated tensor: 1+1=2 > k=1, so truncate to 2*1-1-1=0.
        assert verlinde_fusion_sl2(1, 1, 1) == [0]

    def test_fusion_k1_trivial(self):
        """k=1: L_0 x L_j = L_j (vacuum is identity)."""
        assert verlinde_fusion_sl2(1, 0, 0) == [0]
        assert verlinde_fusion_sl2(1, 0, 1) == [1]

    def test_fusion_k2(self):
        """k=2: L_1 x L_1 = L_0 + L_2."""
        assert verlinde_fusion_sl2(2, 1, 1) == [0, 2]

    def test_fusion_k2_fund_adj(self):
        """k=2: L_1 x L_2 = L_1."""
        assert verlinde_fusion_sl2(2, 1, 2) == [1]

    def test_s_matrix_unitarity_k1(self):
        """S-matrix is unitary at k=1 (2x2 matrix)."""
        # S^dagger S = I. For real S: S^T S = I.
        tol = 1e-12
        k_val = 1
        n = k_val + 1
        for i in range(n):
            for j in range(n):
                dot = sum(
                    verlinde_s_matrix_entry(k_val, i, m)
                    * verlinde_s_matrix_entry(k_val, j, m)
                    for m in range(n)
                )
                expected = 1.0 if i == j else 0.0
                assert abs(dot - expected) < tol, (
                    f"S-matrix not unitary at ({i},{j}): {dot} != {expected}"
                )

    def test_s_matrix_symmetry_k2(self):
        """S-matrix is symmetric at k=2."""
        k_val = 2
        n = k_val + 1
        tol = 1e-12
        for i in range(n):
            for j in range(n):
                assert abs(
                    verlinde_s_matrix_entry(k_val, i, j)
                    - verlinde_s_matrix_entry(k_val, j, i)
                ) < tol


# =========================================================================
# Section 7: Grothendieck invariant comparison
# =========================================================================

class TestGrothendieckComparison:
    """Compare numerical invariants of Z(U_{V_k}) and Z^{der}_{ch}(V_k)."""

    def test_all_match_k1(self):
        """All invariants match at k=1."""
        result = compare_grothendieck_invariants_sl2(F(1))
        assert result["all_match"]
        assert result["status"] == "CONSISTENT"

    def test_all_match_k0(self):
        """All invariants match at k=0."""
        result = compare_grothendieck_invariants_sl2(F(0))
        assert result["all_match"]

    def test_euler_char_comparison(self):
        """Euler char = -1 on both sides."""
        result = compare_grothendieck_invariants_sl2(F(1))
        check = result["checks"]["euler_char"]
        assert check["match"]
        assert check["chirhoch_euler"] == -1
        assert check["categorical_euler"] == -1

    def test_kappa_complementarity_comparison(self):
        """kappa + kappa' = 0 on both sides."""
        result = compare_grothendieck_invariants_sl2(F(1))
        check = result["checks"]["kappa_complementarity"]
        assert check["match"]
        assert check["sum"] == F(0)

    def test_p3_bracket_comparison(self):
        """P_3 bracket coefficient = 1/(k+2) on both sides."""
        result = compare_grothendieck_invariants_sl2(F(1))
        check = result["checks"]["p3_bracket_coeff"]
        assert check["match"]
        assert check["chirhoch_coeff"] == F(1, 3)


# =========================================================================
# Section 8: E_3 structure comparison
# =========================================================================

class TestE3Structure:
    """E_3 structure on Z^{der}_{ch}(V_k(sl_2))."""

    def test_p3_ef_bracket(self):
        """P_3 bracket {e, f} = h_KZ * (e,f) = 1/(k+2)."""
        result = compare_e3_structure_sl2(F(1))
        assert result["e3_data"]["p3_ef"] == F(1, 3)

    def test_p3_hh_bracket(self):
        """P_3 bracket {h, h} = h_KZ * (h,h) = 2/(k+2)."""
        result = compare_e3_structure_sl2(F(1))
        assert result["e3_data"]["p3_hh"] == F(2, 3)

    def test_h_kz_coefficient(self):
        """h_KZ = 1/(k+2) at various levels."""
        for k_val, expected in [(F(1), F(1, 3)), (F(2), F(1, 4)),
                                 (F(0), F(1, 2))]:
            result = compare_e3_structure_sl2(k_val)
            assert result["h_KZ"] == expected


# =========================================================================
# Section 9: Integrable level comparison
# =========================================================================

class TestIntegrableComparison:
    """Comparison at integrable levels."""

    def test_k1_two_simples(self):
        """At k=1: 2 simple modules."""
        result = compare_at_integrable_level(1)
        assert result["num_simples"] == 2
        assert result["verlinde_dim"] == 2

    def test_k2_three_simples(self):
        """At k=2: 3 simple modules."""
        result = compare_at_integrable_level(2)
        assert result["num_simples"] == 3

    def test_algebraic_vs_categorical_center(self):
        """Algebraic center dim 1 vs categorical center dim k+1."""
        result = compare_at_integrable_level(1)
        assert result["algebraic_center_dim"] == 1
        assert result["verlinde_dim"] == 2

    def test_chirhoch_total_dim_constant(self):
        """ChirHoch total dim = 5 regardless of integrable level."""
        for k_val in [1, 2, 3]:
            result = compare_at_integrable_level(k_val)
            assert result["chirhoch_total_dim"] == 5


# =========================================================================
# Section 10: AP compliance checks
# =========================================================================

class TestAPCompliance:
    """Anti-pattern compliance checks."""

    def test_ap126_r_matrix_k0(self):
        """AP126: trace-form r-matrix vanishes at k=0."""
        result = ap126_r_matrix_check(F(1))
        assert result["vanishes_at_k0"]
        assert result["level_prefix_present"]

    def test_ap132_bar_complex(self):
        """AP132: bar complex uses augmentation ideal."""
        result = ap132_bar_complex_check()
        assert result["uses_augmentation_ideal"]
        assert "V_k(sl_2)-bar" in result["formula"]

    def test_ap141_both_conventions(self):
        """AP141/AP148: both r-matrix conventions correct at k=0."""
        result = ap141_kz_convention_check()
        assert result["trace_k0_vanishes"]
        assert result["kz_k0_nonzero"]
        assert result["kz_k0_value"] == F(1, 2)
        assert result["both_correct"]

    def test_shadow_class_l(self):
        """Affine KM is class L, shadow depth 3."""
        assert SHADOW_CLASS == "L"
        assert SHADOW_DEPTH == 3

    def test_theorem_h_amplitude(self):
        """Theorem H: ChirHoch concentrated in {0, 1, 2}."""
        cdc = chiral_derived_center_sl2(F(1))
        assert cdc["concentrated_in"] == [0, 1, 2]


# =========================================================================
# Section 11: Multi-path cross-verification (AP10)
# =========================================================================

class TestCrossVerifyChirHoch:
    """AP10: cross-verify ChirHoch dims [1, 3, 1] via 4 paths."""

    def test_all_paths_agree(self):
        """All 4 verification paths agree on dims [1, 3, 1]."""
        result = cross_verify_chirhoch_dims_sl2()
        assert result["all_match"]

    def test_euler_char_path(self):
        """Euler char path: (-1)^3 = -1 matches 1 - 3 + 1 = -1."""
        result = cross_verify_chirhoch_dims_sl2()
        assert result["path4_euler_char"] == -1
        assert result["path4_expected"] == -1
        assert result["path4_match"]


class TestCrossVerifyKappa:
    """AP10: cross-verify kappa_ch via Sugawara decomposition."""

    def test_all_levels(self):
        """All test levels have consistent kappa decomposition."""
        result = cross_verify_kappa_sl2()
        assert result["all_match"]

    def test_k0_boundary(self):
        """k=0: kappa = 3/2 = dim(g)/2."""
        result = cross_verify_kappa_sl2()
        assert result["boundary_k0"]["match"]
        assert result["boundary_k0"]["value"] == F(3, 2)


class TestCrossVerifyVerlinde:
    """AP10: cross-verify Verlinde dimensions."""

    def test_all_integrable_levels(self):
        """Verlinde dim = k+1 for k = 1, ..., 5."""
        result = cross_verify_verlinde_sl2()
        assert result["all_match"]


# =========================================================================
# Section 12: Level sweep
# =========================================================================

class TestLevelSweep:
    """Sweep over multiple levels for consistency."""

    def test_all_levels_consistent(self):
        """All 6 test levels give consistent invariants."""
        results = verify_level_sweep()
        for level_str, data in results.items():
            assert data["all_match"], (
                f"Inconsistency at level k={level_str}"
            )

    def test_kappa_sum_always_zero(self):
        """kappa_ch + kappa_ch^! = 0 at all test levels."""
        results = verify_level_sweep()
        for level_str, data in results.items():
            assert data["kappa_sum"] == F(0), (
                f"kappa sum != 0 at k={level_str}"
            )


# =========================================================================
# Section 13: Full verification
# =========================================================================

class TestFullVerification:
    """Integration tests: full verification pipeline."""

    def test_full_verification_generic(self):
        """Full verification at generic level gives CONSISTENT."""
        result = full_verification()
        assert "CONSISTENT" in result["generic_level"]["status"]

    def test_full_verification_all_levels(self):
        """All levels in sweep are consistent."""
        result = full_verification()
        for level_str, data in result["level_sweep"].items():
            assert data["all_match"], (
                f"Full verification failed at k={level_str}"
            )

    def test_full_verification_integrable_k1(self):
        """Integrable k=1: Verlinde dim = 2."""
        result = full_verification()
        assert result["integrable_k1"]["verlinde_dim"] == 2
        assert result["integrable_k1"]["num_simples"] == 2

    def test_full_verification_integrable_k2(self):
        """Integrable k=2: Verlinde dim = 3."""
        result = full_verification()
        assert result["integrable_k2"]["verlinde_dim"] == 3

    def test_full_verification_cross_checks(self):
        """All cross-verification suites pass (AP10 compliance)."""
        result = full_verification()
        assert result["cross_verify_chirhoch"]["all_match"]
        assert result["cross_verify_kappa"]["all_match"]
        assert result["cross_verify_verlinde"]["all_match"]

    def test_full_verification_shadow(self):
        """Shadow classification is L, depth 3."""
        result = full_verification()
        assert result["shadow_class"] == "L"
        assert result["shadow_depth"] == 3

    def test_full_verification_theorem_h(self):
        """Theorem H amplitude bound is [0, 1, 2]."""
        result = full_verification()
        assert result["theorem_h_amplitude"] == [0, 1, 2]

    def test_full_verification_conjecture_label(self):
        """Conjecture label is correctly referenced."""
        result = full_verification()
        assert result["conjecture"] == "conj:v3-drinfeld-center-equals-bulk"

    def test_full_verification_ap_compliance(self):
        """AP compliance checks pass."""
        result = full_verification()
        ap = result["ap_compliance"]
        assert ap["ap126"]["vanishes_at_k0"]
        assert ap["ap132"]["uses_augmentation_ideal"]
        assert ap["ap141_ap148"]["both_correct"]


# =========================================================================
# Section 14: Heisenberg vs sl_2 comparison (upgrade validation)
# =========================================================================

class TestHeisenbergVsSl2Upgrade:
    """Validate the upgrade from Heisenberg (abelian) to sl_2 (non-abelian)."""

    def test_dim_upgrade(self):
        """ChirHoch total: Heis = 3, sl_2 = 5."""
        assert CHIRHOCH_TOTAL_DIM == 5  # sl_2
        # Heisenberg has total 3 (from drinfeld_center_heisenberg_bulk.py)

    def test_euler_sign_flip(self):
        """Euler char: Heis = +1, sl_2 = -1."""
        # Heisenberg: chi = 1 - 1 + 1 = 1 (odd rank 1)
        # sl_2: chi = 1 - 3 + 1 = -1 (odd rank 3)
        assert chirhoch_euler_char() == -1

    def test_shadow_class_upgrade(self):
        """Shadow class: Heis = G (depth 2), sl_2 = L (depth 3)."""
        assert SHADOW_CLASS == "L"
        assert SHADOW_DEPTH == 3

    def test_center_k0_differs(self):
        """At k=0: Heis double center = 3 (degenerate), sl_2 = 1 (non-degenerate).

        This is the KEY DIFFERENCE: non-abelian g has a Lie bracket
        independent of k, so the double center stays 1-dimensional.
        """
        z = center_of_drinfeld_double_sl2(F(0))
        assert z["dim"] == 1  # sl_2: non-degenerate even at k=0

    def test_kappa_k0_differs(self):
        """At k=0: kappa(Heis) = 0, kappa(sl_2) = 3/2."""
        # Heisenberg: kappa = k, so k=0 -> 0
        # sl_2: kappa = 3(k+2)/4, so k=0 -> 3/2 (Sugawara shift)
        assert kappa_ch_sl2(F(0)) == F(3, 2)
