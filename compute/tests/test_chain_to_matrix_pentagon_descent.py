"""
Tests for chain-to-matrix Pentagon descent.

Verifies thm:chain-to-matrix-pentagon-unification (k3_yangian_chapter L3568)
at FIVE quadruples:
    1. (conifold, K3, E, E)             baseline single cross-class
    2. (K3,       K3, E, E)             baseline multi-K3
    3. (T^4,      K3, E, E)             abelian-surface anchor
    4. (conifold, conifold, K3, E)      double cross-class
    5. (LP^2,     K3, E, E)             Class-B noncompact anchor

For each quadruple, the matrix-level Pentagon cyclic sum (computed via the
V_4 Künneth bracketing-associator) must equal the chain-level Lefschetz
pushforward predictor (computed via the Cartan-coroot decomposition of
[omega]^Pentagon_{Y(g_K3)} + simply-laced uniformity).

Independent verification sources:
    derived_from -- the V_4 Künneth dichotomy + Drinfeld-coupling correction
                    Delta from thm:kunneth-dichotomy (k3_yangian L3156).
    verified_against -- the Cartan-coroot decomposition + simply-laced
                    Killing-form rank counting law from
                    thm:Yfg-Pentagon-cartan-coroot (e1_chiral L2503),
                    rem:killing-rank-counting (k3_yangian L3736).
                    These determine the Pentagon vanishing INDEPENDENTLY
                    of the V_4 character ring arithmetic.
"""

from __future__ import annotations

from compute.lib.independent_verification import independent_verification
from compute.lib.chain_to_matrix_pentagon_descent import (
    M_E, M_K3, M_T4, M_conf, M_LP2,
    Mx_pair, conv_v4, sigma_tot, chi, is_anti, is_generic,
    Delta_pair,
    bracketing_assoc_3_via_iteration,
    bracketing_assoc_3_via_closed_form,
    pentagon_vertices,
    verify_descent_on_quadruple,
    verify_all_quadruples,
    QUADRUPLES,
)


# ---------------------------------------------------------------------------
# Primitive matrix sanity checks
# ---------------------------------------------------------------------------

def test_M_E_trace_is_chi_zero():
    assert chi(M_E) == 0

def test_M_K3_trace_is_chi_two():
    assert chi(M_K3) == 2

def test_M_conf_trace_is_zero():
    assert chi(M_conf) == 0

def test_M_T4_trace_is_zero():
    assert chi(M_T4) == 0

def test_M_LP2_trace_is_zero():
    assert chi(M_LP2) == 0

def test_M_T4_equals_M_E_conv_M_E():
    assert M_T4 == conv_v4(M_E, M_E)

def test_M_K3_K3_equals_K3_K3_value():
    """M_{K3 x K3} = (450, -416, 130, -160) per L3149."""
    assert conv_v4(M_K3, M_K3) == (450, -416, 130, -160)

def test_sigma_tot_M_K3_equals_chapter_value():
    """sigma_tot M_{K3} = (13, -16, 5, 0) per L3193."""
    assert sigma_tot(M_K3) == (13, -16, 5, 0)


# ---------------------------------------------------------------------------
# Class assignments under sigma_tot
# ---------------------------------------------------------------------------

def test_M_E_is_anti_symmetric():
    assert is_anti(M_E)

def test_M_T4_is_anti_symmetric():
    assert is_anti(M_T4)

def test_M_K3_is_generic():
    assert is_generic(M_K3)

def test_M_conf_is_generic():
    assert is_generic(M_conf)

def test_M_LP2_is_generic():
    assert is_generic(M_LP2)


# ---------------------------------------------------------------------------
# Künneth dichotomy: case-by-case Delta_{X, Y}
# ---------------------------------------------------------------------------

def test_Delta_E_E_vanishes():
    """Both anti -> Delta = 0 (case 2)."""
    assert Delta_pair(M_E, M_E) == (0, 0, 0, 0)

def test_Delta_K3_K3_vanishes():
    """Both generic -> Delta = 0 (case 1)."""
    assert Delta_pair(M_K3, M_K3) == (0, 0, 0, 0)

def test_Delta_K3_E_chapter_value():
    """sigma_tot(M_K3) - chi(O_K3) e_{Pi_{--}} = (13, -16, 5, 0) - 2(0,0,0,1)
       = (13, -16, 5, -2) per L3195."""
    assert Delta_pair(M_K3, M_E) == (13, -16, 5, -2)


# ---------------------------------------------------------------------------
# Composite manifold M
# ---------------------------------------------------------------------------

def test_M_K3_E_chapter_value():
    """M_{K3 x E} = (0, 5, -16, 11) per L3198."""
    assert Mx_pair(M_K3, M_E) == (0, 5, -16, 11)

def test_M_conf_E_absorber():
    """M_{conifold x E} = (-1, 1, 0, 0) per L3239 (absorber)."""
    assert Mx_pair(M_conf, M_E) == (-1, 1, 0, 0)


# ---------------------------------------------------------------------------
# Bracketing-associator: chapter values (closed-form)
# ---------------------------------------------------------------------------

def test_bracketing_assoc_conf_K3_E_chapter_value():
    """a(conifold, K3, E) = (0, 0, 2, -2) per L3497."""
    assert bracketing_assoc_3_via_iteration(M_conf, M_K3, M_E) == (0, 0, 2, -2)

def test_bracketing_assoc_K3_K3_E_chapter_value():
    """a(K3, K3, E) = (26, -32, 10, -4) per L3499."""
    assert bracketing_assoc_3_via_iteration(M_K3, M_K3, M_E) == (26, -32, 10, -4)

def test_bracketing_assoc_E_E_E_chapter_value():
    """a(E, E, E) = (0, 0, 0, 0) per L3507 (both anti, Delta=0)."""
    assert bracketing_assoc_3_via_iteration(M_E, M_E, M_E) == (0, 0, 0, 0)

def test_closed_form_matches_iteration_at_conf_K3_E():
    """Closed-form (L3486) must equal iteration definition (L3479)."""
    iterated = bracketing_assoc_3_via_iteration(M_conf, M_K3, M_E)
    closed = bracketing_assoc_3_via_closed_form(M_conf, M_K3, M_E)
    assert iterated == closed

def test_closed_form_matches_iteration_at_K3_K3_E():
    iterated = bracketing_assoc_3_via_iteration(M_K3, M_K3, M_E)
    closed = bracketing_assoc_3_via_closed_form(M_K3, M_K3, M_E)
    assert iterated == closed


# ---------------------------------------------------------------------------
# Pentagon vertex computations: chapter baselines
# ---------------------------------------------------------------------------

def test_pentagon_vertices_conf_K3_E_E_match_chapter():
    """Verify all 5 vertices for (conifold, K3, E, E) per L3530-3534."""
    r = pentagon_vertices(M_conf, M_K3, M_E, M_E, "conifold,K3,E,E")
    assert r.V1 == (5, -5, 29, -29)
    assert r.V2 == (5, -5, 27, -27)
    assert r.V3 == (5, -5, 27, -27)
    assert r.V4 == (39, -39, 61, -61)
    assert r.V5 == (39, -39, 63, -63)

def test_pentagon_vertices_K3_K3_E_E_match_chapter():
    """Verify all 5 vertices for (K3, K3, E, E) per L3540-3545."""
    r = pentagon_vertices(M_K3, M_K3, M_E, M_E, "K3,K3,E,E")
    assert r.V1 == (450, -416, 130, -164)
    assert r.V2 == (424, -384, 120, -160)
    assert r.V3 == (424, -384, 120, -160)
    assert r.V4 == (1034, -930, 666, -770)
    assert r.V5 == (1060, -962, 676, -774)


# ---------------------------------------------------------------------------
# Pentagon coherence (cyclic sum = 0) at all 5 quadruples
# ---------------------------------------------------------------------------

@independent_verification(
    claim="rem:chain-to-matrix-pentagon-five-quadruples",
    derived_from=[
        "V_4 Künneth dichotomy thm:kunneth-dichotomy "
        "(k3_yangian_chapter.tex L3156)",
        "Drinfeld-coupling correction Delta_{X,Y} formula "
        "(rem:k3-times-e-verification L3193)",
    ],
    verified_against=[
        "Cartan-coroot decomposition of Y(g_K3) Pentagon cocycle "
        "thm:Yfg-Pentagon-cartan-coroot (e1_chiral_algebras.tex L2503)",
        "Killing-form rank counting law rem:killing-rank-counting "
        "(k3_yangian_chapter.tex L3736)",
    ],
    disjoint_rationale=(
        "The Künneth dichotomy + Delta correction are statements about "
        "the V_4-character convolution algebra (matrix-level shadow). "
        "The Cartan-coroot decomposition + Killing-form rank counting "
        "are statements about the chain-level Y(g_K3) Pentagon cocycle "
        "in H^2(SC^{ch,top}; aut), with simply-laced ADE uniformity "
        "(alpha,alpha)=2 forcing each h_alpha^4 trace summand to vanish. "
        "Neither derivation references the other: the matrix side knows "
        "no Lie-algebra Cartan structure, the chain side knows no V_4 "
        "regular-representation arithmetic.")
)
def test_pentagon_coherence_at_all_five_quadruples():
    """The matrix-level Pentagon cyclic sum equals the chain-level Lefschetz
    pushforward predictor (zero) at all five quadruples."""
    results = verify_all_quadruples()
    assert len(results) == 5
    for r in results:
        assert r["matrix_cyclic_sum"] == r["chain_predicted"], (
            f"Pentagon descent FAILED at {r['name']}: matrix sum "
            f"{r['matrix_cyclic_sum']} != chain prediction "
            f"{r['chain_predicted']}")
        assert r["descent_verified"], (
            f"Descent verification FAILED at {r['name']}")


# ---------------------------------------------------------------------------
# NEW quadruples: explicit Pentagon vertex inscriptions
# ---------------------------------------------------------------------------

def test_pentagon_vertices_T4_K3_E_E():
    """NEW: (T^4, K3, E, E) - abelian-surface vs conifold contrast.

    T^4 is sigma_tot-anti (like E), unlike conifold which is generic.
    Predicted edge pattern: e23 = e45 = 0 (same K3-anchored fixed-point
    rigidity as in the (K3, K3, E, E) case where e23 = 0).
    """
    r = pentagon_vertices(M_T4, M_K3, M_E, M_E, "T^4,K3,E,E")
    # All vertices have trace = chi(O_T4) * chi(O_K3) * chi(O_E) * chi(O_E) = 0*2*0*0 = 0
    assert chi(r.V1) == 0
    assert chi(r.V2) == 0
    assert chi(r.V3) == 0
    assert chi(r.V4) == 0
    assert chi(r.V5) == 0
    # Pentagon coherence
    assert r.coherent
    # Edge structure: e_{23} = 0 (XY = T^4 x K3 -> (T^4 x K3) x E = (T^4 x K3) x E)
    e12, e23, e34, e45, e51 = r.edges
    assert e23 == (0, 0, 0, 0)
    # K3-anchored elliptic-tower fixed point along (X(YZ)): X = K3, YZ = T^4,
    # so (K3 x T^4) iterated K3-anchored... e_{45} should also vanish here.
    assert e45 == (0, 0, 0, 0)

def test_pentagon_vertices_conf_conf_K3_E():
    """NEW: (conifold, conifold, K3, E) - double cross-class.

    Both first two factors are conifolds (generic, not in elliptic tower).
    The K3 sits at position 3, E at position 4. The Pentagon coherence
    test tests cross-class consistency at TWO conifolds.

    Predicted edge pattern: e_{12} = e_{23} = e_{45} = 0 because:
      e_{12}: WX = conf x conf is build-path independent
      e_{23}: same conf x conf x K3 differing only in association
      e_{45}: K3 x E = absorber-type behavior on the elliptic side
    Only e_{34} and e_{51} carry the cyclic discrepancy.
    """
    r = pentagon_vertices(M_conf, M_conf, M_K3, M_E, "conf,conf,K3,E")
    assert chi(r.V1) == 0
    assert r.coherent
    e12, e23, e34, e45, e51 = r.edges
    # e_{12} = e_{23} = e_{45} = 0 (verified empirically)
    assert e12 == (0, 0, 0, 0)
    assert e23 == (0, 0, 0, 0)
    assert e45 == (0, 0, 0, 0)
    # The Pentagon discrepancy is concentrated on (e_{34}, e_{51})
    assert e34 == tuple(-x for x in e51)

def test_pentagon_vertices_LP2_K3_E_E():
    """NEW: (LP^2, K3, E, E) - Class-B noncompact anchored.

    LP^2 is generic (mirror of conifold). The Pentagon edge pattern
    should have the same SHAPE as (conifold, K3, E, E) but with different
    numerical values because LP^2 = +(1, -1, 0, 0) vs conifold = -(1, -1, 0, 0).

    Predicted: edges of (LP^2, K3, E, E) are sign-related to edges of
    (conifold, K3, E, E) by overall flip on appropriate channels.
    """
    r = pentagon_vertices(M_LP2, M_K3, M_E, M_E, "LP^2,K3,E,E")
    # Trace check
    assert chi(r.V1) == 0
    assert r.coherent
    e12, e23, e34, e45, e51 = r.edges
    # e_{23} = 0 by the same K3-anchored fixed point as conifold case
    assert e23 == (0, 0, 0, 0)
    # Edge structure: same SHAPE as conifold case but signs flip
    # because M_LP2 = -M_conf on (Pi_{++}, Pi_{+-}) channels.
    # For (conifold, K3, E, E): edges = ((0,0,-2,2), 0, (34,-34,34,-34), (0,0,2,-2), (-34,34,-34,34))
    # For (LP^2, K3, E, E):    edges = ((0,0,2,-2), 0, (-34,34,-34,34), (0,0,-2,2), (34,-34,34,-34))
    # Mirror under M_conf <-> M_LP2 (overall sign flip on conifold-ish channels)
    assert e12 == (0, 0, 2, -2)
    assert e34 == (-34, 34, -34, 34)
    assert e45 == (0, 0, -2, 2)
    assert e51 == (34, -34, 34, -34)


# ---------------------------------------------------------------------------
# Trace-zero of the bracketing-associator
# ---------------------------------------------------------------------------

def test_a_traces_zero_at_all_triples():
    """tr(a(X, Y, Z)) = 0 universally (forced by Künneth-multiplicativity)."""
    triples = [
        (M_conf, M_K3, M_E),
        (M_K3, M_K3, M_E),
        (M_K3, M_E, M_E),
        (M_K3, M_T4, M_E),
        (M_E, M_E, M_E),
        (M_T4, M_K3, M_E),
        (M_LP2, M_K3, M_E),
        (M_conf, M_conf, M_K3),
    ]
    for X, Y, Z in triples:
        a = bracketing_assoc_3_via_iteration(X, Y, Z)
        assert chi(a) == 0, f"tr(a) != 0 at ({X}, {Y}, {Z}): a = {a}"


# ---------------------------------------------------------------------------
# Pentagon coherence summary
# ---------------------------------------------------------------------------

def test_descent_holds_at_each_quadruple_individually():
    """Each individual quadruple satisfies chain-to-matrix descent."""
    for name, W, X, Y, Z in QUADRUPLES:
        r = verify_descent_on_quadruple(W, X, Y, Z, name=name)
        assert r["descent_verified"], (
            f"Descent failed at {name}: {r}")


def test_all_quadruples_collectively_verify_descent():
    """All 5 quadruples taken together verify the descent."""
    results = verify_all_quadruples()
    n_verified = sum(1 for r in results if r["descent_verified"])
    assert n_verified == 5
    n_coherent = sum(1 for r in results if r["matrix_coherent"])
    assert n_coherent == 5
