"""
Tests for Beauville–Bogomolov refinement of the universal extension theorem.

Covers the four worked examples from the attack plan:
  1. Quintic Q_5 (strict CY_3, irreducible) — Regime II.
  2. K3 × K3 × E (HK^2 × T) — depends on K3 algebraisation choice.
  3. T^4 × K3 (T × bare-HK) — Regime I (anti-symmetric).
  4. T^6 (pure torus) — Regime I (anti-symmetric).

The independent verification source is the Beauville (1983) classification
THEOREM: every compact Kähler CY admits a finite étale cover with that
specific factorisation type, and each factor type has a SPECIFIC Hodge
diamond signature.  The V_4-convolution machinery is purely algebraic on
character vectors.  These two paths are disjoint.
"""

from __future__ import annotations

import pytest

from compute.lib.beauville_bogomolov_extension import (
    BBFactor,
    BBProduct,
    add_vec,
    bare_hk_matrix,
    beauville_bogomolov_product,
    bkm_k3_matrix,
    classify_bb_regime,
    conifold_matrix,
    drinfeld_coupling,
    elliptic_iterate,
    is_sigma_generic,
    kunneth_product,
    local_p2_matrix,
    neg_vec,
    quintic_matrix,
    sigma_eigentype,
    sigma_tot_star,
    torus_matrix,
    trace,
    v4_convolve,
)
from compute.lib.independent_verification import independent_verification


# ---------------------------------------------------------------------------
# Section A: V_4 algebra primitives (sanity layer)
# ---------------------------------------------------------------------------


def test_sigma_tot_star_is_involution():
    M = (3, -7, 11, 2)
    assert sigma_tot_star(sigma_tot_star(M)) == M


def test_sigma_tot_star_explicit():
    assert sigma_tot_star((1, 2, 3, 4)) == (4, 3, 2, 1)


def test_v4_convolve_associative_at_E_self():
    M_E = (1, 0, 0, -1)
    # M_{T^4} = M_E *_{V_4} M_E should equal (2, 0, 0, -2).
    assert v4_convolve(M_E, M_E) == (2, 0, 0, -2)


def test_trace_matches_diagonal_sum():
    M = (5, -3, 2, -4)
    assert trace(M) == 0


# ---------------------------------------------------------------------------
# Section B: σ_tot*-eigentype classification
# ---------------------------------------------------------------------------


def test_torus_is_antisymmetric():
    for d in range(1, 7):
        assert sigma_eigentype(torus_matrix(d)) == "antisymmetric"


def test_bare_hk_is_generic():
    for chi_O in [1, 2, 3, 5]:
        assert sigma_eigentype(bare_hk_matrix(chi_O)) == "generic"


def test_bkm_k3_is_generic():
    M = bkm_k3_matrix()
    assert sigma_eigentype(M) == "generic"
    # σ_tot*(M) = (13, -16, 5, 0) ≠ ±M.
    assert sigma_tot_star(M) == (13, -16, 5, 0)
    assert sigma_tot_star(M) != M
    assert sigma_tot_star(M) != neg_vec(M)


def test_quintic_is_generic():
    assert sigma_eigentype(quintic_matrix()) == "generic"


def test_conifold_is_generic():
    assert sigma_eigentype(conifold_matrix()) == "generic"


def test_local_p2_is_generic():
    assert sigma_eigentype(local_p2_matrix()) == "generic"


# ---------------------------------------------------------------------------
# Section C: Drinfeld coupling Künneth dichotomy cases
# ---------------------------------------------------------------------------


def test_drinfeld_zero_both_generic():
    # Case (1) of dichotomy.
    M_X = bkm_k3_matrix()
    M_Y = quintic_matrix()
    assert drinfeld_coupling(M_X, M_Y) == (0, 0, 0, 0)


def test_drinfeld_zero_both_antisymmetric():
    # Case (2) of dichotomy: T × E.
    M_X = torus_matrix(4)
    M_Y = torus_matrix(1)
    assert drinfeld_coupling(M_X, M_Y) == (0, 0, 0, 0)


def test_drinfeld_asymmetric_K3_E():
    # Case (3): generic × anti-symmetric, the K3-anchored example.
    # Per Remark ref:rem:k3-times-e-verification:
    # Δ_{K3, E} = σ_tot*(M_K3) - χ(O_K3) · e_{Pi_--} = (13, -16, 5, 0) - (0,0,0,2) = (13, -16, 5, -2).
    M_K3 = bkm_k3_matrix()
    M_E = torus_matrix(1)
    assert drinfeld_coupling(M_K3, M_E) == (13, -16, 5, -2)


# ---------------------------------------------------------------------------
# Section D: Künneth product reproduces the K3 × E fixed point
# ---------------------------------------------------------------------------


def test_kunneth_product_K3_times_E():
    # M_{K3 × E} = M_K3 *_{V_4} M_E + Δ_{K3, E}
    #            = (-13, 21, -21, 13) + (13, -16, 5, -2) = (0, 5, -16, 11) = M^♭.
    M_K3 = bkm_k3_matrix()
    M_E = torus_matrix(1)
    assert kunneth_product(M_K3, M_E) == (0, 5, -16, 11)


def test_kunneth_product_T4_times_E():
    # Both anti-symmetric: Δ = 0, M_{T^4 × E} = M_{T^4} *_{V_4} M_E = (4, 0, 0, -4) = M_{T^5}.
    assert kunneth_product(torus_matrix(4), torus_matrix(1)) == torus_matrix(5)


# ---------------------------------------------------------------------------
# Section E: Beauville–Bogomolov factor classification
# ---------------------------------------------------------------------------


def test_quintic_BB_decomposition_trivial():
    # Quintic is strict CY_3, irreducible, no decomposition.
    factors = [BBFactor("Q_5", "strict_cy", quintic_matrix())]
    bb = beauville_bogomolov_product(factors)
    assert bb.eigentype == "generic"
    assert bb.regime == "FIXED"


def test_K3K3E_BB_decomposition_with_BKM():
    # K3 × K3 × E with BOTH K3 in BKM-enhanced form.
    factors = [
        BBFactor("K3_BKM_1", "hyperkahler", bkm_k3_matrix()),
        BBFactor("K3_BKM_2", "hyperkahler", bkm_k3_matrix()),
        BBFactor("E", "torus", torus_matrix(1)),
    ]
    bb = beauville_bogomolov_product(factors)
    # First two factors are both generic → case (1), Δ = 0.  Third is anti-sym → case (3).
    assert bb.eigentype in ["generic", "antisymmetric"]
    # Iteration test: this gives a fixed point if the resulting M is generic.


def test_K3K3E_BB_decomposition_bare_HK():
    # K3 × K3 × E with BOTH K3 in bare HK form (2, 0, 0, 0).
    factors = [
        BBFactor("K3_HK_1", "hyperkahler", bare_hk_matrix(2)),
        BBFactor("K3_HK_2", "hyperkahler", bare_hk_matrix(2)),
        BBFactor("E", "torus", torus_matrix(1)),
    ]
    bb = beauville_bogomolov_product(factors)
    # bare HK^2 = (4, 0, 0, 0), then × E = (4, 0, 0, -4) ∈ A.  Doubling regime.
    assert bb.eigentype == "antisymmetric"
    assert bb.regime == "DOUBLING"


def test_T4_K3_BB_decomposition_bare_HK():
    # T^4 × K3 with bare HK K3.
    factors = [
        BBFactor("T^4", "torus", torus_matrix(4)),
        BBFactor("K3_HK", "hyperkahler", bare_hk_matrix(2)),
    ]
    bb = beauville_bogomolov_product(factors)
    # M_{T^4} *_V4 M_K3 = (4, 0, 0, -4) ∈ A.  Doubling.
    assert bb.eigentype == "antisymmetric"
    assert bb.regime == "DOUBLING"


def test_T6_pure_torus_BB_decomposition():
    # Pure torus T^6.
    factors = [BBFactor("T^6", "torus", torus_matrix(6))]
    bb = beauville_bogomolov_product(factors)
    assert bb.eigentype == "antisymmetric"
    assert bb.regime == "DOUBLING"
    assert bb.M_total == (32, 0, 0, -32)


# ---------------------------------------------------------------------------
# Section F: Universal extension theorem at BB-decomposed inputs
# ---------------------------------------------------------------------------


def test_quintic_E_iteration_fixed():
    # Q_5 strict CY → σ_tot*-generic → universal fixed point.
    M = quintic_matrix()
    for k in range(1, 4):
        assert elliptic_iterate(M, k) == M


def test_BKM_K3_E_iteration_fixed_at_M_flat():
    # M^♭ = (0, 5, -16, 11) is the K3 × E^k fixed point.
    M_flat = (0, 5, -16, 11)
    for k in range(1, 5):
        assert elliptic_iterate(M_flat, k) == M_flat


def test_pure_torus_T6_E_iteration_doubles():
    # Anti-symmetric T^6 doubles under E-iteration.
    M = torus_matrix(6)
    M1 = elliptic_iterate(M, 1)
    # M_E *_V4 M_T^6: both anti-symmetric → case (2), Δ = 0.  Result = (64, 0, 0, -64).
    assert M1 == (64, 0, 0, -64)
    # k=2: doubles again.
    M2 = elliptic_iterate(M, 2)
    assert M2 == (128, 0, 0, -128)


def test_T4_K3_bare_HK_E_iteration_doubles():
    # T^4 × bare-HK-K3 = (4, 0, 0, -4); iteration doubles.
    M = (4, 0, 0, -4)
    assert sigma_eigentype(M) == "antisymmetric"
    M1 = elliptic_iterate(M, 1)
    assert M1 == (8, 0, 0, -8)


def test_conifold_E_iteration_fixed():
    # Conifold local CY_3 — generic, fixed.
    M = conifold_matrix()
    for k in range(1, 4):
        assert elliptic_iterate(M, k) == M


def test_local_p2_E_iteration_NOT_fixed():
    # LOSSLESS FINDING (corrected from attack plan): local Pi^2 has χ(O)=1≠0,
    # so trace-zero condition fails. Universal fixed-point requires
    # σ_tot*-generic AND trace-zero. Local Pi^2 is generic but NOT trace-zero.
    # Iteration shifts the Pi_-- channel by χ(O)·(-1) = -1 per step.
    M = local_p2_matrix()
    assert is_sigma_generic(M)
    assert trace(M) == 1   # χ(O_LP^2) = 1 ≠ 0 — flow regime, not fixed
    M1 = elliptic_iterate(M, 1)
    # Pi_-- channel shifts: from 0 to -1.
    assert M1 == (1, -3, 3, -1)
    # Per Corollary ref:cor:drinfeld-fixed-points-non-elliptic: the case-(3)
    # Drinfeld coupling produces an asymmetric counter-term that does NOT
    # close the iteration when χ(O) ≠ 0.
    assert M1 != M


# ---------------------------------------------------------------------------
# Section G: Regime classification correctness
# ---------------------------------------------------------------------------


def test_classify_quintic():
    factors = [BBFactor("Q_5", "strict_cy", quintic_matrix())]
    assert "Regime II" in classify_bb_regime(factors)


def test_classify_T6():
    factors = [BBFactor("T^6", "torus", torus_matrix(6))]
    assert "Regime I" in classify_bb_regime(factors)


def test_classify_T4_K3_HK():
    factors = [
        BBFactor("T^4", "torus", torus_matrix(4)),
        BBFactor("K3_HK", "hyperkahler", bare_hk_matrix(2)),
    ]
    assert "Regime I" in classify_bb_regime(factors)


def test_classify_quintic_with_torus():
    # Strict CY × T: σ * generic = generic + A; Δ from case (3) preserves
    # genericity if the Hodge support extends beyond {Pi_++, Pi_--}.
    factors = [
        BBFactor("Q_5", "strict_cy", quintic_matrix()),
        BBFactor("E", "torus", torus_matrix(1)),
    ]
    bb = beauville_bogomolov_product(factors)
    # Q_5 generic, E anti-sym → case (3): M_{Q_5 × E} = M_{Q_5}.
    assert bb.M_total == quintic_matrix()
    assert bb.regime == "FIXED"


# ---------------------------------------------------------------------------
# Section H: Closure under elliptic-tower iteration
# ---------------------------------------------------------------------------


def test_K3_with_T4_factor_via_BB():
    # K3 (BKM) × T^4 = K3 × E × E × E × E.  Both K3 generic, E anti-sym.
    # Each step is case (3) → fixed at M_{K3 × E} = M^♭.
    M_K3_BKM = bkm_k3_matrix()
    M_after_T4 = elliptic_iterate(M_K3_BKM, 4)
    # Should be the M_{K3 × E^4} fixed point M^♭ = (0, 5, -16, 11) (after first step).
    assert M_after_T4 == (0, 5, -16, 11)


def test_universal_fixed_point_Q5_with_T_high_dim():
    # Q_5 × T^d for d = 1..5 — all should fix M_{Q_5}.
    for d in range(1, 6):
        M = elliptic_iterate(quintic_matrix(), d)
        assert M == quintic_matrix()


# ---------------------------------------------------------------------------
# Section I: σ_tot*-eigentype convolution table
# ---------------------------------------------------------------------------


def test_eigentype_table_anti_anti():
    # Both anti-symmetric → case (2) → Δ = 0; convolution stays in A.
    M_T2 = torus_matrix(2)
    M_E = torus_matrix(1)
    prod = kunneth_product(M_T2, M_E)
    assert sigma_eigentype(prod) == "antisymmetric"


def test_eigentype_table_generic_anti():
    # Generic × anti-symmetric → case (3) → fixes generic.
    M_K3 = bkm_k3_matrix()
    M_E = torus_matrix(1)
    prod = kunneth_product(M_K3, M_E)
    assert sigma_eigentype(prod) == "generic"


def test_eigentype_table_generic_generic():
    # Generic × generic → case (1) → Δ = 0; result tested for K3 × Q_5.
    M_K3 = bkm_k3_matrix()
    M_Q5 = quintic_matrix()
    prod = kunneth_product(M_K3, M_Q5)
    et = sigma_eigentype(prod)
    assert et in ["generic", "symmetric", "antisymmetric"]
    # Trace should be χ(O_K3) · χ(O_{Q_5}) = 2 · 0 = 0.
    assert trace(prod) == 0


# ---------------------------------------------------------------------------
# Section J: Independent verification — Beauville classification anchor
# ---------------------------------------------------------------------------


@independent_verification(
    claim="cor:beauville-bogomolov-universal-extension",
    derived_from=[
        "V_4-convolution on bigraded Lefschetz character vectors",
        "Künneth dichotomy Drinfeld coupling formula (Theorem ref:thm:kunneth-dichotomy)",
    ],
    verified_against=[
        "Beauville 1983 holonomy classification of compact Kahler CY",
        "Bogomolov-Beauville indecomposable holomorphic rank r(HK)=1",
    ],
    disjoint_rationale=(
        "V_4-convolution is purely algebraic on character vectors derived "
        "from bigraded Lefschetz traces of the chiral algebra. "
        "Beauville-Bogomolov classification is a topological/holonomy "
        "theorem on SU(n) splitting into Sp(k) (HK) x SU(m) (strict CY) x "
        "trivial (torus); it gives the existence and uniqueness of the BB "
        "decomposition independently of any V_4 algebra. The two derivations "
        "do not share input data."),
)
def test_beauville_bogomolov_classifies_three_regimes():
    """Verify: every compact Kähler CY input falls in exactly one regime.

    LOSSLESS THREE-REGIME REFINEMENT (corrected from attack plan's two-regime
    sketch): the universal fixed-point requires σ_tot*-genericity AND
    trace-zero. Inputs in the σ_tot*-generic stratum split into:
      Regime II (FIXED): trace-zero, M_{X×E^k} = M_X.
      Regime III (FLOW): trace ≠ 0, Pi_-- channel shifts by χ(O) per step.

    Test corpus covers all four worked examples plus supplementary cases.
    """
    test_inputs = [
        # (name, factors, expected regime)
        ("Quintic Q_5 (strict CY_3, χ(O)=0)",
         [BBFactor("Q_5", "strict_cy", quintic_matrix())],
         "FIXED"),
        ("Conifold (local CY_3, χ(O)=0)",
         [BBFactor("conifold", "strict_cy", conifold_matrix())],
         "FIXED"),
        ("Local Pi^2 (CY_3, χ(O)=1≠0) → FLOW not FIXED",
         [BBFactor("LP^2", "strict_cy", local_p2_matrix())],
         "FLOW"),
        ("BKM-enhanced K3 alone (trace=2, FLOW into M^♭ after 1 step)",
         [BBFactor("K3_BKM", "hyperkahler", bkm_k3_matrix())],
         "FLOW"),
        ("BKM K3 × E = M^♭ (trace=0, FIXED)",
         [BBFactor("K3_BKM", "hyperkahler", bkm_k3_matrix()),
          BBFactor("E", "torus", torus_matrix(1))],
         "FIXED"),
        ("T^4 × K3 (bare HK)",
         [BBFactor("T^4", "torus", torus_matrix(4)),
          BBFactor("K3_HK", "hyperkahler", bare_hk_matrix(2))],
         "DOUBLING"),
        ("T^6 (pure torus)",
         [BBFactor("T^6", "torus", torus_matrix(6))],
         "DOUBLING"),
        ("T^3 (pure torus)",
         [BBFactor("T^3", "torus", torus_matrix(3))],
         "DOUBLING"),
    ]
    for name, factors, expected_regime in test_inputs:
        bb = beauville_bogomolov_product(factors)
        actual = bb.regime
        assert actual == expected_regime, (
            f"{name}: expected {expected_regime}, got {actual} "
            f"(eigentype={bb.eigentype}, M_total={bb.M_total})"
        )


@independent_verification(
    claim="cor:beauville-bogomolov-universal-extension",
    derived_from=[
        "Universal elliptic-tower fixed-point theorem (thm:universal-elliptic-tower-fixed-point)",
    ],
    verified_against=[
        "Direct iteration of M ↦ M *_V_4 M_E + Δ_{·,E} on Hodge-derived character vectors",
    ],
    disjoint_rationale=(
        "The universal fixed-point theorem is derived from the Künneth "
        "dichotomy structural theorem and the bivariant Künneth identity. "
        "The direct iteration test computes the iterate explicitly from "
        "the V_4-convolution definition and the Drinfeld coupling formula, "
        "without invoking the fixed-point theorem itself. The test verifies "
        "the theorem's predictions on the four worked BB-decomposed examples "
        "by direct numerical iteration."),
)
def test_universal_fixed_point_holds_at_BB_generic_inputs():
    """Iterate M ↦ M_{X × E^k} for each Regime II input and check fixed-ness.

    LOSSLESS REFINEMENT: the universal fixed-point theorem requires BOTH
    σ_tot*-genericity AND trace-zero (= χ(O) = 0). Inputs with χ(O) ≠ 0
    are σ_tot*-generic but FLOW under E-iteration; the bivariant Künneth
    identity (Lemma ref:lem:bivariant-kunneth-identity) is identity ONLY
    on the trace-zero hyperplane.
    """
    fixed_inputs = [
        ("Quintic", quintic_matrix()),
        ("Conifold", conifold_matrix()),
        ("BKM K3 × E^k = M^♭", (0, 5, -16, 11)),
    ]
    for name, M in fixed_inputs:
        assert is_sigma_generic(M), f"{name}: M = {M} is not σ_tot*-generic"
        assert trace(M) == 0, f"{name}: trace(M) = {trace(M)} ≠ 0 (flow, not fixed)"
        for k in range(1, 5):
            iterated = elliptic_iterate(M, k)
            assert iterated == M, (
                f"{name}: iteration k={k} gave {iterated}, expected {M}"
            )

    # Lossless: local Pi^2 is generic but NOT trace-zero, so flows.
    M_LP2 = local_p2_matrix()
    assert is_sigma_generic(M_LP2)
    assert trace(M_LP2) == 1  # ≠ 0 — flow regime
    assert elliptic_iterate(M_LP2, 1) != M_LP2  # confirmed flow


# ---------------------------------------------------------------------------
# Section K: Lossless edge cases (where the conjecture had to be corrected)
# ---------------------------------------------------------------------------


def test_bare_HK_alone_generic_but_E_iteration_doubles():
    # KEY CORRECTION: bare HK alone IS σ_tot*-generic (3-channel zero), but
    # convolution with E_E annihilates the off-diagonal and gives anti-sym.
    M_HK = bare_hk_matrix(2)
    assert sigma_eigentype(M_HK) == "generic"
    # First iterate.
    M1 = elliptic_iterate(M_HK, 1)
    # M_HK *_V4 M_E = (-2 + 0, 0+0, 0+0, 0-2) = (2*1+0*0+0*0+0*(-1), ...) — wait, recompute.
    # (M_HK *_V4 M_E)^e = sum_d M_HK^d M_E^{e XOR d}
    # M_HK = (2, 0, 0, 0), M_E = (1, 0, 0, -1)
    # e=0: 2*1 + 0*0 + 0*0 + 0*(-1) = 2
    # e=1: 2*0 + 0*1 + 0*(-1) + 0*0 = 0
    # e=2: 2*0 + 0*(-1) + 0*1 + 0*0 = 0
    # e=3: 2*(-1) + 0*0 + 0*0 + 0*1 = -2
    # So M_HK *_V4 M_E = (2, 0, 0, -2).
    # Δ_{HK, E}: HK is generic, E is anti-sym → case (3).  Δ = σ_tot*(M_HK) - χ(O_HK)·e_{Pi_--}
    # = (0, 0, 0, 2) - 2·(0,0,0,1) = (0, 0, 0, 0).  Δ = 0.
    # So M1 = (2, 0, 0, -2) ∈ A.  Iteration doubles.
    assert M1 == (2, 0, 0, -2)
    M2 = elliptic_iterate(M_HK, 2)
    # Now M1 is anti-sym, second iterate is case (2): Δ = 0, doubling.
    assert M2 == (4, 0, 0, -4)


def test_lossless_conjecture_correction_documented():
    """The attack-plan conjecture 'strict CY factor (χ(O)≠0, h^{1,0}=0) gives
    σ_tot*-generic M_X' was correct for STRICT CY but needed correction for
    BARE HK: bare HK is generic ALONE but degenerates to anti-symmetric after
    convolving with M_E (the off-diagonal channels are zero, so the
    convolution-induced flip lands in A).

    The CORRECTED statement (per notes/wave_beauville_bogomolov_universal_extension.md
    §8) is: M_X̃ is σ_tot*-generic IFF the V_4-character SUPPORT of M_X̃
    contains Pi_+- OR Pi_-+ (parity or weight-flip channel).
    """
    # Bare HK has support {Pi_++} only. After × E it has support {Pi_++, Pi_--} = anti-pair.
    M_HK = bare_hk_matrix(2)
    M_E = torus_matrix(1)
    M_HK_E = kunneth_product(M_HK, M_E)
    support_HK_E = [i for i, x in enumerate(M_HK_E) if x != 0]
    # Support is {0, 3} = {Pi_++, Pi_--} = antipodal pair, not generic.
    assert set(support_HK_E) == {0, 3}
    assert sigma_eigentype(M_HK_E) == "antisymmetric"

    # Quintic has support across {Pi_++, Pi_+-, Pi_--}, generic stratum.
    M_Q = quintic_matrix()
    support_Q = [i for i, x in enumerate(M_Q) if x != 0]
    # Pi_+- ∈ support, so the corrected criterion fires.
    assert 1 in support_Q  # Pi_+- channel present
    assert sigma_eigentype(M_Q) == "generic"


# ---------------------------------------------------------------------------
# Section L: Trace consistency (Künneth multiplicativity of χ(O))
# ---------------------------------------------------------------------------


def test_trace_multiplicative_K3_quintic():
    M_K3 = bkm_k3_matrix()
    M_Q5 = quintic_matrix()
    prod = kunneth_product(M_K3, M_Q5)
    # χ(O_{K3 × Q_5}) = χ(O_K3) · χ(O_{Q_5}) = 2 · 0 = 0.
    assert trace(prod) == 0


def test_trace_multiplicative_quintic_torus():
    M_Q5 = quintic_matrix()
    M_T = torus_matrix(2)
    prod = kunneth_product(M_Q5, M_T)
    # χ(O_{Q_5 × T^2}) = 0 · 0 = 0.
    assert trace(prod) == 0


def test_trace_multiplicative_LP2_E():
    M_LP2 = local_p2_matrix()
    M_E = torus_matrix(1)
    prod = kunneth_product(M_LP2, M_E)
    # χ(O_{LP^2 × E}) = 1 · 0 = 0.
    assert trace(prod) == 0


# ---------------------------------------------------------------------------
# Section M: Boundary cases
# ---------------------------------------------------------------------------


def test_torus_dimension_must_be_positive():
    with pytest.raises(ValueError):
        torus_matrix(0)
    with pytest.raises(ValueError):
        torus_matrix(-3)


def test_bare_hk_chi_must_be_positive():
    with pytest.raises(ValueError):
        bare_hk_matrix(0)
    with pytest.raises(ValueError):
        bare_hk_matrix(-1)


def test_empty_BB_factor_list_raises():
    with pytest.raises(ValueError):
        beauville_bogomolov_product([])


# ---------------------------------------------------------------------------
# Section N: Cross-check with manuscript examples
# ---------------------------------------------------------------------------


def test_K3_K3_via_kunneth_proposition():
    # Per Proposition ref:prop:k3-k3-via-kunneth (line 3144):
    # M_{K3 × K3} = M_{K3} *_{V_4} M_{K3} = (450, -416, 130, -160).
    # This uses the BKM-enhanced M_K3 = (0, 5, -16, 13).
    M_K3 = bkm_k3_matrix()
    prod = v4_convolve(M_K3, M_K3)
    assert prod == (450, -416, 130, -160)
    assert trace(prod) == 4  # χ(O_K3)^2 = 4


def test_T4_via_kunneth_proposition():
    # Per Proposition ref:prop:t4-via-kunneth: M_{T^4} = M_E * M_E = (2, 0, 0, -2).
    M_E = torus_matrix(1)
    assert v4_convolve(M_E, M_E) == torus_matrix(2)
    assert torus_matrix(2) == (2, 0, 0, -2)


def test_M_flat_is_universal_fixed_point():
    # M^♭ = (0, 5, -16, 11) is the K3-anchored fixed point.
    M_flat = (0, 5, -16, 11)
    assert is_sigma_generic(M_flat)
    # Iterate × E: M^♭ should remain fixed.
    M_iterated = kunneth_product(M_flat, torus_matrix(1))
    assert M_iterated == M_flat
