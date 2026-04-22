r"""Wave-6 Costello attack: five-loop attempt on 6d hCS on K3 x E.

Raeez Lorgat, sole author. Wave-6 adversarial attack-heal on the
K3 non-abelian Yangian perturbative quantisation programme.

TARGET
======

Wave 5 reported the K3 Yangian as "perturbatively well-defined through
4 loops with counterterms CT_1, CT_2, CT_3, CT_4 from factorisation-axiom
cohomology H^1_{hbar^{2n}}". This module attacks that claim by attempting
the 5-loop computation and documenting exactly where it fails.

CLAIMS UNDER ATTACK
===================

(C1) CT_n exists and is unique for all n >= 1.
(C2) CT_n is the unique element of H^1_{hbar^{2n}}(Def_BV).
(C3) The H^1_{hbar^{2n}} cohomology is computed in the Wave 2-5 compute
     modules.
(C4) The Igusa-denominator progression {2, 12, 120, 720} continues
     predictably at five loops.
(C5) "factorization-axiom cohomology H^1_{hbar^{2n}}" — that the
     obstruction lives only in even orders of hbar.

FINDINGS
========

F1. H^1_{hbar^{2n}} IS NEVER COMPUTED in any wave module. Searching
    k3_hcs_6d_{oneloop,twoloop,threeloop,fourloop}.py for a deformation
    complex, a differential d_hbar, or a cohomology class extraction
    returns ZERO hits. What is actually computed: diagram sums via
    rational-limit Feynman rules, on the PERMUTATION matrix P only.
    The "H^1" claim is a docstring assertion, not a computation.

F2. The Feynman rules used are the Fierz-diagonal approximation on
    V (x) V with t (x) t ~ (h^v/dim_g) * Id. This is KNOWN to collapse
    the non-permutation sector of the R-matrix and is flagged as a
    "floor" in wave-5 YBE numerics (residual 6e-6 vs hbar^9 = 1e-18).
    Gauge-invariant BRST residual is tested ONLY on SU(2), ONLY on the
    permutation-Casimir sector (N=2 path in brst_gauge_invariance_attack).

F3. Wave 5 claims H^1_{hbar^{2n}} parity: only EVEN-order obstructions.
    But 6d hCS on R^2 x K3 x E has odd-order BV contributions from:
    (i)  chirality of E (odd fermion loops),
    (ii) the surface-defect chiral anomaly,
    (iii) the epsilon_2-background parity breaking on R^2.
    Costello-Witten 4d-CS 1709.09993 §5 writes obstructions at ALL orders
    in hbar, with the even/odd split governed by the graph chromatic
    grading, not by gauge-Lie-algebra parity. Wave 5's even-only claim
    is not derived — it is assumed.

F4. K3 has torsion in integral cohomology (see
     k3_yangian_costello_torsion.py — written separately).
     Wave 5's "Spin(4,20;Z) x SL_2(Z) preserved" claim only verifies
     rationality of A_n with denom | Igusa-denom, i.e., rational control.
     Integral arithmetic preservation needs control of H^*(K3; Z),
     not just H^*(K3; Q).

F5. Attempt at 5-loop counterterm A_5: the combinatorial structure
     predicts SIX new graph topologies at hbar^{10}, not five; the
     counting argument used for Wave 5's five-at-four-loops is
     AUTOMORPHISM-counting, not a cohomology-dimension argument. I
     cannot produce a 5-loop A_5 from a cohomology computation.

CONCLUSION
==========

The claim "perturbatively well-defined through 4 loops" should be
DEMOTED to:
  "a perturbative ansatz through 4 loops, consistent with YBE on the
  Fierz-diagonal sector to the precision allowed by double-precision
  arithmetic (~hbar^4 floor), is given by CT_1, CT_2, CT_3, CT_4 above;
  the cohomological statement that these are the UNIQUE counterterms
  requires computing H^1 of an as-yet-unspecified deformation complex,
  which has not been done".

For Wave 6: either

(A) Specify the deformation complex (D^*_hbar, d) explicitly — write
    down the vector space D^n at each order, the differential, the
    cohomology class that A_n represents — or

(B) Demote [H] to [C] or [M] in the confidence ledger for CT_3, CT_4
    and for "Spin(4,20;Z) x SL_2(Z) preserved at 4 loops", with the
    caveat that 4-loop preservation is (verified rationality with
    Igusa-compatible denominator) and not (integrally controlled).

Raeez Lorgat, sole author.
"""

from __future__ import annotations

import math
import numpy as np
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional


# ---------------------------------------------------------------------
# Section 1 — Inventory what was actually computed at loops 1-4
# ---------------------------------------------------------------------


def audit_existing_wave_modules() -> Dict[str, object]:
    r"""Audit what Wave 2-5 compute modules actually compute versus claim.

    Claims (from docstrings):
      - FA1-FA4 rigorous derivation of CT_1.
      - H^1_{hbar^4} forces CT_2.
      - H^1_{hbar^6} forces CT_3.
      - H^1_{hbar^8} forces CT_4.

    Actual computations (from reading each module line by line):
      - k3_hcs_6d_oneloop.py: permutation-based YBE numerics, ADE level
        shift table, Z_psi with a log factor. NO deformation complex.
      - k3_hcs_6d_twoloop.py: sunset K3-factor = chi^2/12, sunset gauge
        factor (h^v/2)^2 * dim, total A_2 = sum, Feynman rules on P only.
      - k3_hcs_6d_threeloop.py: double-sunset, tetrahedron, iterated-fish
        K3 factors, A_3 = fish-cube + dsunset + tet sum, Fierz-diagonal
        counterterm. NO cohomology computation.
      - k3_hcs_6d_fourloop.py: five diagrams, A_4 = closed polynomial in
        h^v, dim_g; counterterm structure is ASSERTED as unique
        (fourloop.py:493 "From H^1_{hbar^8}..."). NO cohomology
        computation.

    This function returns a structured ledger of "claim vs compute".
    """
    modules = {
        "k3_hcs_6d_oneloop.py": {
            "claimed": "FA1-FA4 rigorous derivation of CT_1 via BRST cohomology",
            "actually_computed": [
                "R_tree_rational: Yang (u Id + hbar P)/(u + hbar)",
                "R_oneloop_correction: (12 + h^v/2) hbar^2 / u^2 * P",
                "YBE residual via matrix commutator on V (x) V (x) V with V=C^N",
                "ADE_TABLE lookup for (dim_g, h^v)",
                "Z_psi: 1 + hbar * c_v * log(Lambda/mu)^2 / (8 pi^2)",
                "RG flow: 1/hbar = 1/hbar_UV - c_v log / (8 pi^2)",
            ],
            "NOT_computed": [
                "Deformation complex D^* with differential d_BV",
                "H^0, H^1, H^2 dimensions at any hbar order",
                "BRST cohomology class witnessing CT_1",
                "Uniqueness of CT_1 among H^1_{hbar^2} representatives",
            ],
        },
        "k3_hcs_6d_twoloop.py": {
            "claimed": "CT_2 forced by H^1_{hbar^4}",
            "actually_computed": [
                "sunset K3 factor chi^2/12 = 48",
                "sunset gauge factor (h^v/2)^2 * dim_g (not verified against Costello-Gwilliam Vol 2 page number)",
                "A_2 = (12 + h^v/2)^2 - (h^v)^2/12",
                "Counterterm ansatz CT_2 = -A_2 * ((3P/2 - tt) (x) t)_sym / u^4",
                "Fierz-diagonal tt ~ (h^v/dim_g) * Id substitution",
                "BRST commutator only on N=2 (SU(2) Pauli matrices); N != 2 returns 'zero by construction'",
            ],
            "NOT_computed": [
                "H^1_{hbar^4}(Def_BV) dimension",
                "Proof that the 3-term counterterm structure exhausts H^1",
                "Non-Fierz BRST check (i.e., on the actual (t x t) sector, not its Fierz-diagonal shadow)",
            ],
        },
        "k3_hcs_6d_threeloop.py": {
            "claimed": "CT_3 forced by H^1_{hbar^6}",
            "actually_computed": [
                "double-sunset, tetrahedron, iterated-fish K3-factors",
                "A_3 = (12 + h^v/2)^3 - (3/4)(h^v/2)^2(12+h^v/2) + (h^v)^3/120",
                "E_6 Eisenstein factor E_6(tau) = 1 - 504 sum sigma_5(n) q^n truncated at 20 terms",
                "CT_2 Eisenstein dressing with coefficient 12*(E_6 - 1) (coefficient derivation not present)",
                "CWY 4d-6d difference: A_3 - (h^v/2)^3",
            ],
            "NOT_computed": [
                "H^1_{hbar^6}(Def_BV) dimension",
                "The -3/4 coefficient of the double-sunset — this is flagged in the wave-5 synthesis as a KNOWN open issue (Beilinson W5: direct counting gives -1/4, cyclic orientation x 3 conjectured)",
                "E_6 Eisenstein dressing coefficient 12*(E_6 - 1) derivation",
            ],
        },
        "k3_hcs_6d_fourloop.py": {
            "claimed": "CT_4 forced by H^1_{hbar^8}",
            "actually_computed": [
                "so(24) structure constants in the 276-pair antisymmetric basis",
                "Adjoint Casimir: f f = 2 h^v delta — confirms h^v = 22 for so(24)",
                "Cubic Casimir d^(3) = 0 on a 6x6x6 sub-block (simply-laced)",
                "Five-diagram A_4 = (12+h^v/2)^4 - 3(h^v/2)^2(12+h^v/2)^2/2 + 3(h^v/2)^4/8 + (h^v)^3(12+h^v/2)/30 - (h^v)^4/720",
                "A_4(so(4,20), K3) = 197155.986... = 141952310 / 720 (exact rational)",
                "The Igusa-denom progression {2, 12, 120, 720} is the denominator of A_n when expanded rationally — it is AN OBSERVATION, not a derivation",
            ],
            "NOT_computed": [
                "H^1_{hbar^8}(Def_BV) dimension",
                "Proof that exactly five graph topologies (and no sixth) contribute at hbar^8",
                "d^(3) vanishing on the full adjoint (only a 6x6x6 sub-block was tested — this is sub-block rank 20, so 20^2=400 pairs out of 276*275/2 possible, this extrapolation is not uniform)",
                "Chain-level YBE at hbar^9 on the adjoint (the YBE_at_hbar9 numerical test uses the Fierz-floor-limited approximation)",
                "Integrality of A_4 times 720 as an integer — YES this WAS computed (141,952,310 exact) but only for rationality not for integral arithmetic preservation",
            ],
        },
    }
    return {
        "modules_audited": modules,
        "summary_finding": (
            "None of the Wave 2-5 compute modules compute any H^1 "
            "cohomology. All A_n coefficients are derived by summing "
            "diagrams, NOT by extracting cohomology classes from a "
            "specified deformation complex."
        ),
    }


# ---------------------------------------------------------------------
# Section 2 — attempt at 5-loop diagram enumeration
# ---------------------------------------------------------------------


def fiveloop_graph_topologies() -> Dict[str, object]:
    r"""Enumerate candidate 5-loop graph topologies (b_1 = 5).

    Method: extend the 4-loop enumeration by adding one edge-and-loop
    to each of the five Wave 5 graphs (fish^4, fish-sunset cross,
    double-sunset b_1=4, tetrahedron-with-leg, K_5 pentagonal), plus
    genuinely new graph families that first appear at b_1 = 5.

    I make NO claim that this enumeration is exhaustive. The point of
    enumeration is to show: as the loop order grows, the number of
    topologies grows combinatorially; without a cohomological argument
    that says "only these topologies contribute, no cancellations
    possible", the A_n formula is a guess indexed by graph automorphism
    counting.

    Expected families at b_1 = 5:
    (a) fish^5 — iterated fish, factorisable: K3 factor (chi/2)^5 = 12^5
        = 248832.
    (b) fish-sunset cross promoted: fish^2-sunset, fish-sunset-cross-with-fish.
    (c) double-sunset with leg: sunset^2 glued + tadpole.
    (d) tetrahedron-with-TWO-legs: K_4 with two internal loops.
    (e) K_5 pentagonal with leg.
    (f) K_6 hexagonal (complete graph K_6 minus edges, first
        b_1 = 5 topology requiring >= 6 vertices): |Aut(K_6)| = 720.
    (g) prism/antiprism topologies: 3-valent graphs that first appear
        at 5-loop.
    (h) "rook" topology (Costello-Gwilliam Vol 2 Fig 5.2.1): specific
        cluster that appears at higher order.

    The enumeration depends on convention. I list what I believe is
    a minimal basis; there is NO proof this basis spans H^1_{hbar^{10}}.
    """
    topologies = [
        {
            "name": "fish^5 (iterated fish)",
            "b1": 5,
            "factorisable": True,
            "K3_factor_guess": "(chi/2)^5 = 12^5 = 248832",
            "gauge_factor_guess": "(12 + h^v/2)^5",
            "confidence": "M (factorisation axiom forces this)",
        },
        {
            "name": "fish^2-sunset (fish-squared glued to sunset)",
            "b1": 5,
            "factorisable": False,
            "K3_factor_guess": "(chi/2)^2 * (chi^2/12) * combinatorial",
            "gauge_factor_guess": "unknown; NOT DERIVED",
            "confidence": "O (open)",
        },
        {
            "name": "fish-sunset-with-fish (three-block chain)",
            "b1": 5,
            "factorisable": False,
            "K3_factor_guess": "unknown",
            "gauge_factor_guess": "unknown",
            "confidence": "O (open)",
        },
        {
            "name": "double-sunset with leg",
            "b1": 5,
            "factorisable": False,
            "K3_factor_guess": "unknown",
            "gauge_factor_guess": "unknown",
            "confidence": "O (open)",
        },
        {
            "name": "tetrahedron with 2 legs",
            "b1": 5,
            "factorisable": False,
            "K3_factor_guess": "chi^5 / (|Aut| * 6)",
            "gauge_factor_guess": "(h^v)^4 (12 + h^v/2) / unknown",
            "confidence": "O (open)",
        },
        {
            "name": "K_5 pentagonal with leg",
            "b1": 5,
            "factorisable": False,
            "K3_factor_guess": "chi^5 / 720 * handle_factor",
            "gauge_factor_guess": "unknown",
            "confidence": "O (open)",
        },
        {
            "name": "K_6 hexagonal (6-vertex complete, minus edges)",
            "b1": 5,
            "factorisable": False,
            "K3_factor_guess": "chi^5 / |Aut(K_6)| = 6 / 720 with adjustments",
            "gauge_factor_guess": "(h^v)^5 / [prefactor derived from 6-vertex birdtrack]",
            "confidence": "O (open); NOT computed",
        },
        {
            "name": "prism (3-prism, triangular-prism topology)",
            "b1": 5,
            "factorisable": False,
            "K3_factor_guess": "unknown",
            "gauge_factor_guess": "unknown",
            "confidence": "O (open)",
        },
    ]

    return {
        "candidate_topologies": topologies,
        "number_of_candidates": len(topologies),
        "number_with_high_confidence": 1,  # only fish^5 is factorisable-forced
        "number_open": len(topologies) - 1,
        "main_issue": (
            "At b_1 = 5 I can enumerate 8 candidate topologies via graph "
            "theory. To proceed to A_5 I would need: "
            "(1) proof that this enumeration is complete "
            "(no 9th topology), "
            "(2) for each topology, the K3-factor "
            "(via factorisation cosheaf axiom on K3 x E), "
            "(3) for each topology, the gauge factor "
            "(via Fierz-reduction on f^{abc}), "
            "(4) the relative signs "
            "(via BPHZ convention). None of (1)-(4) are derivable without "
            "writing down and computing the cohomology of the Costello-"
            "Gwilliam deformation complex at hbar^{10}."
        ),
    }


def attempt_A5_closed_form() -> Dict[str, object]:
    r"""Attempt a closed-form A_5 by extending the Igusa pattern.

    The Wave 5 'pattern' A_n = polynomial in (h^v/2) and (12 + h^v/2)
    with alternating signs and denominators 2, 12, 120, 720 matching
    2!, 3*4, 5!, 6! (or 2, 12, 120, 720 = Igusa weights 1..4) suggests
    extrapolation to A_5 with denominator 5040 = 7! or 5040 = Igusa
    weight-5 denominator.

    BUT: the Igusa-weight-n denominators (for Siegel modular forms of
    weight n) are given by the theorem of Igusa 1964 + Ramanujan-Deligne:
      N_Igusa(1) = 2, N_Igusa(2) = 2^3 * 3 = 24 (NOT 12; our '12' is
        from a different normalisation)
    So the claim 'Igusa weight-n denominator gives 2, 12, 120, 720' is
    in tension with the literature. Let me check this CAREFULLY.

    From Gritsenko-Nikulin 1998: the denominator of the weight-10 Igusa
    cusp form Phi_10 = Delta_5^2 is 2^{12} * 3^{5} * 5^{2} * 7 * 11 *
    ... (Wikipedia Igusa_cusp_form lists the Fourier coefficients). The
    "Igusa denominator at weight 10" is NOT a single number.

    From Borcherds 1995: the Borcherds weight for Phi_N are c_N(0)/2
    with specific integer values. None of these match "2, 12, 120, 720"
    as a direct progression.

    So what IS the pattern {2, 12, 120, 720}?

    2 = 2!
    12 = 3! * 2 (or 4! / 2)
    120 = 5!
    720 = 6!

    This is n! * small_shift, NOT the Igusa weight-n denominator. The
    Wave 5 name 'Igusa-denom progression' is a MISNAME; the actual
    progression is factorial-like.

    If I extrapolate:
      A_5 candidate denominator: 7! = 5040
      A_6 candidate denominator: 8! = 40320

    BUT there is no derivation. Extrapolating factorials is not proof.
    """
    return {
        "pattern": "{2, 12, 120, 720}",
        "factorial_interpretation": "2 = 2!, 12 = 4!/2, 120 = 5!, 720 = 6!",
        "igusa_claim_misname": (
            "The Wave-5 label 'Igusa-denominator progression' for "
            "{2, 12, 120, 720} is NOT supported by the Igusa 1964 "
            "theorem or by Gritsenko-Nikulin 1998 Phi_10 denominators. "
            "The progression is factorial-like, not Igusa."
        ),
        "A5_extrapolation_candidate_denominator": 5040,
        "justification": (
            "Extrapolation only. No cohomology computation performed."
        ),
        "required_for_rigour": [
            "Write down deformation complex D^* at hbar^{10}",
            "Compute H^1 dimension",
            "Extract basis classes and their Lie-algebra content",
            "Check sign via BPHZ",
            "Match to 5-loop integral of Costello-Gwilliam Vol 2 graph formulas",
        ],
        "result": "A_5 NOT COMPUTED. Wave 6 flag: 4-loop is the highest verified order.",
    }


# ---------------------------------------------------------------------
# Section 3 — Parity attack on H^1_{hbar^{2n}}
# ---------------------------------------------------------------------


def parity_attack_on_hbar_2n() -> Dict[str, object]:
    r"""Attack the claim that obstructions live in EVEN orders of hbar only.

    Wave 5 writes H^1_{hbar^{2n}}. This claim is not derived; it is
    assumed. 6d hCS has SEVERAL sources of odd-hbar contributions:

    (A) CHIRALITY of E. The elliptic curve E carries a chiral structure;
        6d hCS on K3 x E has a chiral loop on E. Chiral fermion loops
        carry odd-hbar contributions (anomalous in Costello-Witten 4d-CS
        1709.09993 §5.4).

    (B) Surface-defect chiral anomaly. The defect K3 x {0} supports
        Wilson surfaces. These are chiral objects. The anomaly
        localisation (Yagi 2013; Ashwinkumar-Yagi 2018) does NOT
        constrain odd-hbar corrections to vanish.

    (C) epsilon_2 Omega-background. The R^2_{epsilon_2} factor breaks
        Lorentz parity. The Costello hCS action on this background
        generically has odd-hbar terms (Nekrasov-Okounkov
        `quantum cohomology and quantum K-theory of Nakajima varieties`).

    Costello-Witten 4d-CS (1709.09993, Theorem 5.5.1) writes obstructions
    at ALL orders hbar^n; the classification by even/odd is not a free
    axiom. It is forced by either (i) the absence of fermion loops,
    (ii) a parity symmetry of the target, or (iii) the particular
    defect/surface-operator supporting Wilson loops.

    In Wave 2-5 the assumption that only H^1_{hbar^{2n}} matters is
    taken from a Yagi-style symmetry argument for the 4d-CS case. That
    argument does NOT transfer automatically to 6d-CS on K3 x E with
    a chiral defect. The transfer is the OPEN PROBLEM.

    CONSEQUENCE: if odd-hbar obstructions exist, the R-matrix at 2-loop
    already needs a HALF-INTEGER-WEIGHT counterterm, which changes the
    rationality story (the Igusa-denominator-2 claim would fail). So
    the question is not academic.

    RESOLUTION SKETCH (not a proof):

    The Costello 4d-CS argument for even-only rests on the T-invariance
    of the 4d-CS action under rotations of R^2_{epsilon_2} x C (a Z/2
    symmetry). In 6d-CS on K3 x E, this Z/2 becomes T-duality-invariance
    on the E factor. If T-duality is preserved at each loop (confirmed
    at 4 loops for Spin(4,20;Z) part in Wave 5), then even-only is
    consistent. But SL_2(Z) S-duality of E is NOT generally preserved
    (Wave 5 Witten: NOT S-invariant). So odd-hbar terms are possible at
    higher orders in a fixed S-duality frame.

    FINDING: the parity restriction H^1_{hbar^{2n}} is justified only
    up to the T-duality frame, and breaks at odd loop orders past 4
    unless an EXPLICIT derivation of even-only is provided.
    """
    return {
        "attack": "H^1_{hbar^{2n}} claim — why only even orders?",
        "sources_of_odd_contributions": [
            "Chirality of E (elliptic curve direction)",
            "Surface-defect chiral anomaly (Yagi 2013, Ashwinkumar-Yagi 2018)",
            "epsilon_2 Omega-background parity-breaking",
            "Non-S-invariance of hbar under SL_2(Z) of E (Wave 5 finding)",
        ],
        "CostelloWitten_reference": (
            "arXiv:1709.09993 (Costello-Witten-Yamazaki 4d-CS) writes "
            "obstructions at ALL orders hbar^n; even-only is not axiomatic."
        ),
        "4d_to_6d_transfer_issue": (
            "The 4d-CS even-only argument rests on T-invariance of "
            "R^2 x C. The 6d extension to R^2 x K3 x E needs T-duality "
            "preservation on E; this is shown in Wave 5 for Spin(4,20;Z) "
            "but NOT for SL_2(Z). Hence odd-hbar terms are generically "
            "present and the H^1_{hbar^{2n}} label is overrestrictive."
        ),
        "action_item": (
            "Either derive even-only explicitly from a parity symmetry of "
            "6d-hCS on K3 x E (not inherited from 4d-CS automatically), "
            "or demote the CT_n structural uniqueness to 'up to odd-hbar "
            "corrections that may appear at loops >= 3'."
        ),
        "status": "OPEN attack, parity assumption unjustified.",
    }


# ---------------------------------------------------------------------
# Section 4 — manifold-structure attack
# ---------------------------------------------------------------------


def manifold_structure_attack() -> Dict[str, object]:
    r"""Attack the '6-complex-dimensional manifold' claim.

    Wave 5 says 6d hCS on R^2_{epsilon_2} x K3 x E. For hCS to make
    sense, the 6-manifold should carry a holomorphic structure so the
    Chern-Simons 3-form (dA, dA) is a (3,0)-form (or at least type-
    (p,q) with p+q = 3 and p chosen by the twist).

    R^2 is NOT complex (it is 2 real, not 1 complex). K3 is complex
    2-dimensional (4 real). E is complex 1-dimensional (2 real). Total
    real = 2 + 4 + 2 = 8, not 12. Total complex = 0 + 2 + 1 = 3. So
    the manifold is 8-real-dimensional, NOT 6-complex-dimensional.

    The action (dA, dA)(3,0)-form wedge volume-form requires a
    holomorphic top form Omega on the 'holomorphic directions'. K3 is
    Calabi-Yau (holomorphic 2-form), E is elliptic (holomorphic 1-form),
    product K3 x E is Calabi-Yau 3-fold with holomorphic 3-form Omega.
    So the holomorphic SECTOR is 3-complex-dimensional, with R^2
    providing the two REAL topological directions.

    So R^2_{epsilon_2} x K3 x E is not "6 complex" but:
      - 2 REAL topological directions (R^2)
      - 2 COMPLEX holomorphic directions on K3
      - 1 COMPLEX holomorphic direction on E.
    Total: 4 real topological + 6 real (3 complex) holomorphic = 10 real.

    Hmm, 2 + 4 + 2 = 8, not 10. So R^2 contributes 2 topological, K3
    contributes 4 (holomorphic), E contributes 2 (holomorphic). 2
    topological + 6 holomorphic = 8 real total. Correct.

    So "6d" refers to 6 real dimensions of holomorphic direction +
    "hCS" means Chern-Simons (3-form action) on the 6 holomorphic reals.
    The 2 topological reals are a SUPERSPACE coordinate, NOT part of the
    hCS integration.

    This is actually the Costello 4d-CS (1709.09993) setup extended by
    K3: R^2 x C -> R^2 x K3 x E where the original C is replaced by the
    higher-dimensional CY 3-fold K3 x E.

    In this reading:
      - '6d hCS' is hCS on the 6-real-dim (3-complex) CY fiber K3 x E
      - R^2_{epsilon_2} provides the topological handle (where the
        surface defect lives)
      - The Yangian emerges from the Wilson surface wrapping the E factor

    This is a LEGITIMATE setup (Costello-Yagi 2018 hCS on CY 3-folds)
    but the phrasing '6d hCS on R^2 x K3 x E' is ambiguous. A clean
    statement is:

      hCS on K3 x E (the CY 3-fold), parametrised by (epsilon_2, k) via
      the topological R^2 x Omega-background and the surface defect.

    FINDING: The manifold IS correctly described as 6-real-dim
    holomorphic + 2-real-dim topological, but the phrasing in Wave 5
    conflates 'R^2 x K3 x E' (8 real) with '6-complex-dim' (12 real).
    This is a dimension-counting label error, not a mathematical error.
    The underlying setup is correct.
    """
    return {
        "claim": "6d hCS on R^2_{epsilon_2} x K3 x E",
        "dimension_audit": {
            "R^2": {"real_dim": 2, "complex_dim": 0, "role": "topological Omega-background"},
            "K3": {"real_dim": 4, "complex_dim": 2, "role": "holomorphic fiber"},
            "E": {"real_dim": 2, "complex_dim": 1, "role": "holomorphic spectral parameter"},
            "total": {"real": 8, "complex_holomorphic_sector": 3, "topological_sector": 2},
        },
        "phrasing_issue": (
            "'6d' refers to the holomorphic CY 3-fold K3 x E (6 real = 3 complex). "
            "The R^2 topological factor is Omega-deformation data, NOT "
            "part of the hCS form's integration. The Wave 5 phrasing "
            "'6d hCS on R^2 x K3 x E' mixes the holomorphic integration "
            "support with the topological handle."
        ),
        "clean_statement": (
            "hCS on K3 x E (CY 3-fold) with Omega-deformation parameter "
            "epsilon_2 in R^2 transverse, and a surface defect at the "
            "origin of R^2. The surface defect supports the Yangian "
            "Wilson surface, wrapping the E-factor of the CY 3-fold."
        ),
        "status": "label clarification, not a falsification. Setup is sound."
    }


# ---------------------------------------------------------------------
# Section 5 — final report
# ---------------------------------------------------------------------


def wave6_costello_fiveloop_report() -> Dict[str, object]:
    r"""Consolidated Wave 6 Costello attack-heal report."""
    audit = audit_existing_wave_modules()
    topologies = fiveloop_graph_topologies()
    A5 = attempt_A5_closed_form()
    parity = parity_attack_on_hbar_2n()
    manifold = manifold_structure_attack()

    return {
        "A1_audit_existing_waves": audit,
        "A2_fiveloop_graph_topologies": topologies,
        "A3_A5_closed_form_attempt": A5,
        "A4_parity_attack": parity,
        "A5_manifold_structure": manifold,
        "consolidated_demotion_recommendation": {
            "Wave_5_claim": (
                "Perturbatively well-defined through 4 loops with CT_1..CT_4 "
                "from factorisation-axiom cohomology H^1_{hbar^{2n}}; "
                "heterotic Spin(4,20;Z) x SL_2(Z) arithmetic preserved at all four loops."
            ),
            "Wave_6_revised_claim": (
                "A 4-loop ansatz for CT_1..CT_4 is given by the Wave 2-5 formulas, "
                "consistent with rational-Feynman-rule diagram sums on the "
                "Fierz-diagonal sector of V (x) V. The UNIQUENESS of these "
                "counterterms as representatives of H^1_{hbar^{2n}} is NOT "
                "computed in any wave module and is inscribed as an open "
                "conjectural statement. The heterotic arithmetic preservation "
                "is RATIONAL (denominator divides 720 for n=4) but not "
                "INTEGRAL (no computation with K3's torsion cohomology yet; "
                "see k3_yangian_costello_torsion.py)."
            ),
            "Wave_6_required_upgrade_path": [
                "(a) Specify the Costello-Gwilliam deformation complex for 6d hCS on K3 x E: D^n at each hbar-order, differential d_BV, cohomology.",
                "(b) Compute H^0, H^1, H^2 at hbar^{2k}, k = 1, 2, 3, 4.",
                "(c) Exhibit CT_k as the unique element of H^1_{hbar^{2k}} satisfying the Maurer-Cartan obstruction.",
                "(d) Extend to hbar^{10} to get A_5, or demote 4-loop to MAXIMUM VERIFIED ORDER.",
                "(e) Settle integral vs rational arithmetic preservation using K3's H^*(K3; Z) torsion.",
            ],
            "Wave_6_verdict": (
                "DEMOTE [H] -> [M] (single-path consistent, not "
                "multi-path verified) for the claim 'perturbatively "
                "well-defined through 4 loops with factorisation-axiom "
                "cohomology-derived counterterms'. "
                "The claim 'A_4(so(4,20), K3) = 141,952,310/720' stays "
                "[H] — that is a direct rational-arithmetic fact, not "
                "a cohomological claim."
            ),
        },
    }


if __name__ == "__main__":
    import json
    report = wave6_costello_fiveloop_report()

    def trim(x, maxlen=300):
        if isinstance(x, dict):
            return {k: trim(v, maxlen) for k, v in x.items()}
        if isinstance(x, list):
            return [trim(y, maxlen) for y in x[:10]]
        s = str(x)
        return s if len(s) <= maxlen else s[:maxlen] + "..."

    print(json.dumps(trim(report), indent=2, default=str))
