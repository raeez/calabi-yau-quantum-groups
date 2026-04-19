r"""Wave-6 Costello attack: integrality — K3 torsion cohomology vs
rational arithmetic preservation of Spin(4, 20; Z) x SL_2(Z) at 4 loops.

Raeez Lorgat, sole author. Wave-6 adversarial attack-heal.

CENTRAL CLAIM UNDER ATTACK
==========================

Wave 5:
    "heterotic Spin(4, 20; Z) x SL_2(Z) arithmetic preserved at all
     four loops" and
    "A_4(so(4,20), K3) = 141952310/720 — denominator divides the
     Igusa weight-4 denominator 720 = 2^4 * 3^2 * 5"

The Wave 5 verification is RATIONAL (over Q): show A_4 times 720
is an integer. This is necessary but not sufficient for integral
arithmetic preservation.

For genuine integral arithmetic preservation, one needs control of
the factorisation-algebra obstruction cohomology with COEFFICIENTS in
Z, not in Q. The obstruction complex depends on H^*(K3; Z), and
K3's integral cohomology has TORSION in degree 2.

THE TORSION IN H^*(K3; Z)
=========================

Standard fact: K3 has

    H^0(K3; Z) = Z
    H^1(K3; Z) = 0
    H^2(K3; Z) = Z^{22}                  (torsion-free, rank 22)
    H^3(K3; Z) = 0
    H^4(K3; Z) = Z

Wait — is H^2(K3; Z) really torsion-free?

Careful citation: K3 is simply connected (pi_1(K3) = 1 by the Kodaira
classification), hence H^1(K3; Z) = 0 and by Poincare duality
H^3(K3; Z) = 0. The intersection form on H^2(K3; Z) is the Lorentzian
lattice of signature (3, 19), the "K3 lattice" with Gram matrix
    (-E_8)^2 + U^3 = 2(-E_8) + 3U
(Barth-Hulek-Peters-Van de Ven, "Compact Complex Surfaces" II,
ch. VIII.3).

Crucially: H^2(K3; Z) IS TORSION-FREE, rank 22.

So K3 is SIMPLY-CONNECTED and TORSION-FREE IN INTEGRAL COHOMOLOGY.

This means: there is NO Z/2 or Z/n in H^*(K3; Z) to worry about in
the direct cohomology. The Igusa denominator 720 = 2^4 * 3^2 * 5 could
conceivably come from REPRESENTATION-THEORETIC torsion in the
Spin(4, 20; Z) action, but not from topological torsion of K3.

BUT: the Spin(4, 20; Z) acts on the MUKAI lattice which is rank 24,
with natural cocycle structure. Mukai introduced
    Lambda_Mukai = H^0(K3; Z) (+) H^2(K3; Z) (+) H^4(K3; Z)
                 = Z (+) Z^{22} (+) Z = Z^{24}
with signature (4, 20).

Does Lambda_Mukai have 2-torsion SOMEWHERE that enters the
factorisation algebra? Let me check:

(a) Lambda_Mukai IS Z^{24} as an abelian group — torsion-free.
(b) The Z/2 automorphism "Hodge star" on H^2(K3; R) acts on Lambda_Mukai
    via the signature symmetry. This is an ISOMETRY of order 2, not
    a torsion element of the lattice.
(c) The Weyl group of Spin(4, 20) acting on Lambda_Mukai has order
    |W(D_{12}) x Z/2| = 2^{11} * 12! * 2 which is divisible by 2^{14};
    elements of the Weyl group have order 2 in an abstract sense.
(d) Schur multipliers: H^2(Spin(4, 20); Z) = Z/2 (Spin is a Z/2 cover
    of SO(4, 20)).

So the torsion that matters is NOT in K3's cohomology (which is torsion
free) but in the GROUP COHOMOLOGY H^2(Spin(4, 20); U(1)) of the
symmetry group acting on the Narain lattice. This is where the
Gritsenko-Nikulin cocycle lives and where the Wave 5 Kummer
quasi-Hopf 3-cocycle Z/6 + Z/6 emerges.

INTEGRAL VS RATIONAL PRESERVATION — THE PROPER STATEMENT
=========================================================

Wave 5's "Spin(4, 20; Z) preserved at 4 loops" is verifying:

    A_4 x 720 = 141,952,310 (exact integer)

This is saying: the 4-loop correction is a rational number whose
denominator divides 720. Since 720 is coprime to the Narain-lattice
prime structure of Spin(4, 20; Z), this IS the rational preservation
statement. To upgrade to integral preservation, one would verify that
the R-matrix 4-loop correction, evaluated on the Narain lattice
Z^{4, 20}, takes INTEGER VALUES on Z-valued Narain lattice elements.

That IS a stronger statement than "A_4 rational with denom | 720".
It would require:

(i) Extract the R-matrix 4-loop correction from A_4 via the
    permutation-and-Casimir tensor (3P/2 - tt) (x) t (x) t (x) t.
(ii) Evaluate this on a pair of Narain lattice elements
    (v, w) in Lambda_Mukai (x) Lambda_Mukai.
(iii) Show the result is in Z, not merely in (1/720) Z.

For (iii), the structure (3P/2 - tt) (x) t (x) t (x) t acting on
Lambda_Mukai^{(x)4} returns a value in Lambda_Mukai modulo
4th-power-Casimir terms. The COEFFICIENT in front is A_4 = 141952310/720,
and there is NO guarantee that a Z-lattice element maps to a
Z-lattice element.

To fix: show the structure constant itself is INTEGER-VALUED after
an appropriate rescaling by the lattice Gram determinant (which is
-1 for Lambda_Mukai, since it is unimodular).

THIS IS A SIGNIFICANT GAP. The Wave 5 claim is rational arithmetic
preservation; the integral arithmetic preservation would require
evaluating A_4 times the specific Casimir-tensor-on-Lambda_Mukai
pairing and showing the result is in Z^{4, 20}.

This module does NOT close that gap. It documents it.

WHAT WOULD A HONEST STATEMENT LOOK LIKE?
========================================

"The 4-loop coefficient A_4(so(4, 20), K3) = 141,952,310/720 is
rational with denominator 720. When multiplied by a Narain lattice
Gram determinant times 720, it gives the integer 141,952,310. This
is a RATIONAL preservation statement: the Spin(4, 20; Q) symmetry
acts consistently at 4 loops with a determinant controlled by the
rational number 720. Whether the stronger INTEGRAL preservation
Spin(4, 20; Z) holds — i.e., whether every Z-valued Narain lattice
pair (v, w) gives an integer in the 4-loop R-matrix value — requires
a separate computation with the full (3P/2 - tt) (x) t (x) t (x) t
tensor evaluated on Lambda_Mukai^{(x)4} and then shown to be in
Lambda_Mukai (x) Lambda_Mukai (not merely in (1/720) Lambda_Mukai
(x) Lambda_Mukai). Not done in Wave 5; scope open for Wave 6."

Raeez Lorgat, sole author.
"""

from __future__ import annotations

import math
import numpy as np
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional


# ---------------------------------------------------------------------
# K3 integral cohomology: facts
# ---------------------------------------------------------------------


def K3_integral_cohomology() -> Dict[str, object]:
    r"""Integral cohomology of K3.

    Standard reference: Barth-Hulek-Peters-Van de Ven "Compact Complex
    Surfaces" Vol I.VIII.3.

    K3 is simply-connected, torsion-free in every degree:
        H^0(K3; Z) = Z
        H^1(K3; Z) = 0
        H^2(K3; Z) = Z^{22}           (rank 22, torsion-free)
        H^3(K3; Z) = 0
        H^4(K3; Z) = Z

    Intersection form on H^2: Lorentzian lattice of signature (3, 19),
    isometric to -2 E_8 (+) 3 U (where U = hyperbolic plane).
    """
    return {
        "H^0": {"rank": 1, "torsion": "trivial", "description": "Z"},
        "H^1": {"rank": 0, "torsion": "trivial", "description": "0 (simply connected)"},
        "H^2": {
            "rank": 22,
            "torsion": "trivial",
            "description": "Z^{22} with intersection form -2 E_8 (+) 3 U, signature (3, 19)",
        },
        "H^3": {"rank": 0, "torsion": "trivial", "description": "0 (Poincare dual of H^1)"},
        "H^4": {"rank": 1, "torsion": "trivial", "description": "Z (fundamental class)"},
        "mukai_lattice": {
            "rank": 24,
            "signature": "(4, 20)",
            "description": "H^0 (+) H^2 (+) H^4, with Mukai bilinear form, UNIMODULAR",
            "determinant_of_Gram": -1,
            "reference": "Mukai 1984, BHPV VIII.3",
        },
        "no_torsion_in_H_star": True,
        "K3_IS_simply_connected": True,
        "implication": (
            "K3's cohomology is TORSION-FREE integrally. Any integral "
            "arithmetic obstruction must therefore come from the "
            "SPIN(4, 20; Z) GROUP COHOMOLOGY (Schur multipliers, "
            "Lyubashenko cocycles), NOT from K3's topology. This is "
            "where Wave 5's '(Q/Z)^{24} cocycle' and 'Kummer Z/6 + Z/6' "
            "live."
        ),
    }


# ---------------------------------------------------------------------
# What Wave 5 actually verified — rational denominator check
# ---------------------------------------------------------------------


def wave5_rational_preservation_check() -> Dict[str, object]:
    r"""Re-verify what Wave 5 actually showed: A_4 * 720 = integer.

    For so(4, 20): h^v = 22, dim = 276.
        A_4 = (12 + 11)^4 - (3/2) * 121 * 529 + (3/8) * 14641
              + 22^3 * 23 / 30 - 22^4 / 720
            = 279841 - 96013.5 + 5490.375 + 8163.4666... - 325.3555...
            = 197155.986...
        A_4 * 720 = 141,952,310 exactly (integer).

    What this verifies: A_4 is rational, denominator 720.
    What this does NOT verify: the integer-valued-on-Z-lattice property
    of the actual R-matrix evaluation.

    For reference: the Igusa cusp form Phi_10 has integer coefficients
    when expanded in the Fourier basis, with a LEADING DENOMINATOR of
    2^5 * 3^4 * 5 * 7 = 10080 (Ibukiyama 2012 convention) or similar
    after normalisation. 720 is a FACTOR but not the full Igusa
    denominator.
    """
    h_v = 22.0
    W1 = 12.0 + h_v / 2.0
    hv2 = h_v / 2.0

    fish4 = W1 ** 4
    fish_sunset = -1.5 * hv2 ** 2 * W1 ** 2
    double_sunset = 0.375 * hv2 ** 4
    tet_leg = h_v ** 3 * W1 / 30.0
    K5_pent = -h_v ** 4 / 720.0

    A4 = fish4 + fish_sunset + double_sunset + tet_leg + K5_pent
    A4_times_720 = A4 * 720.0
    residual = A4_times_720 - round(A4_times_720)

    return {
        "h_v": h_v,
        "A4_components": {
            "fish_quartic_W1^4": fish4,
            "fish_sunset_cross": fish_sunset,
            "double_sunset": double_sunset,
            "tetrahedron_with_leg": tet_leg,
            "K5_pentagonal": K5_pent,
        },
        "A4_total": A4,
        "A4_times_720": A4_times_720,
        "A4_times_720_rounded": round(A4_times_720),
        "rationality_residual": abs(residual),
        "A4_is_rational_with_denom_720": abs(residual) < 1e-6,
        "what_this_verifies": (
            "A_4 is a rational number whose denominator is a divisor "
            "of 720. When expressed as p/720, p = 141,952,310 is an "
            "integer. This is the 'Spin(4, 20; Q) preservation' "
            "statement."
        ),
        "what_this_does_NOT_verify": [
            "Integrality of R-matrix values on Lambda_Mukai^{(x)4} "
            "lattice elements (needs explicit Casimir evaluation).",
            "Integrality of the counterterm tensor (3P/2 - tt)(x)t(x)t(x)t "
            "evaluated on a Z-valued lattice pair.",
            "That no Spin(4, 20; Z) lattice element is mapped outside "
            "Lambda_Mukai (x) Lambda_Mukai by the 4-loop correction.",
        ],
    }


# ---------------------------------------------------------------------
# The integral preservation question — what would be required
# ---------------------------------------------------------------------


def integral_preservation_required_computation() -> Dict[str, object]:
    r"""Specify what a genuine integral preservation computation would be.

    Given A_4 = 141,952,310 / 720 and the structure tensor
        S = (3P/2 - t (x) t) (x) t (x) t (x) t
    on V^{(x)5} with V = Lambda_Mukai (x) C (rank 24), the 4-loop
    R-matrix correction is
        R_4(u) = -A_4 * S / u^8
    evaluated on a pair (v, w) in Lambda_Mukai (x) Lambda_Mukai.

    For INTEGRAL preservation the required statement is:

    For every v, w in Lambda_Mukai (x) Lambda_Mukai (both Z-valued),
    the value
        <v, R_4(u) w>_{Muk}
    lies in
        u^{-8} * Lambda_Mukai (x) Lambda_Mukai (x) Z[1]

    as a formal power series. This means
        <v, S w>_{Muk}
    must be in 720 * Lambda_Mukai (x) Lambda_Mukai, so that
    A_4 * <v, S w>_{Muk} = (141,952,310 / 720) * 720 * (something)
    = 141,952,310 * (something) is in Lambda_Mukai (x) Lambda_Mukai.

    The structure tensor S acts on V^{(x)5}. For a 2-index pairing, we
    need to contract 3 of the 5 legs with the identity. But then the
    remaining structure is rank 2, and the Casimir traces
        tr_{Muk}(t (x) t) = h^v_{(4,20)} = 22
    and
        tr_{Muk}(t (x) t (x) t) = related to cubic Casimir
    give factors of 22 and 22^2. These combine with the permutation
    trace tr(P) = 24 to give factors of 24, 22, 22^2 etc.

    So the question becomes: does 720 divide
        24^2 * 22^3 = 576 * 10648 = 6,133,248
    or similar? Let's factorise:
        24 = 2^3 * 3
        22 = 2 * 11
        720 = 2^4 * 3^2 * 5
        24^2 * 22^3 = 2^6 * 3^2 * 2^3 * 11^3 = 2^9 * 3^2 * 11^3
    720 | 2^9 * 3^2 * 11^3? 720 = 2^4 * 3^2 * 5, we have 2^9 and 3^2 but
    5 does not divide 2^9 * 11^3. So 720 does NOT divide the naive
    Casimir trace evaluation.

    Conclusion: to preserve integrality, the 4-loop correction on
    Narain lattice elements needs an ADDITIONAL factor of 5 from the
    K3-Euler structure (e.g., chi(K3) = 24 does NOT contribute a 5;
    the primitive cohomology rank 22 doesn't either; but the weight-5
    Gritsenko cusp form Delta_5 DOES contribute a 5).

    This is not a proof of failure — just a combinatorial check showing
    that integrality is NOT automatic from the rational formula.

    A proper integral preservation proof would need to:
    (A) Choose a specific v, w in Lambda_Mukai (x) Lambda_Mukai.
    (B) Compute <v, S w>_{Muk} mod 720 using the explicit structure.
    (C) Verify that <v, S w>_{Muk} is in 720 * Lambda_Mukai (x) Lambda_Mukai
        for all such v, w.

    OR: use the Borcherds weight identity kappa_BKM(Phi_10) = 5 to
    argue that the Delta_5 Gritsenko form is the natural extension and
    absorb the 5-prime into the lattice normalisation. This is the
    Eichler-Zagier / Gritsenko-Nikulin lift discussed by Drinfeld W2.

    Such a computation is a Wave 6+ target. NOT done here.
    """
    return {
        "prime_factor_audit": {
            "Lambda_Mukai_Gram_det": -1,
            "chi_K3": 24,
            "24_equals": "2^3 * 3",
            "h_v_so_4_20": 22,
            "22_equals": "2 * 11",
            "720_equals": "2^4 * 3^2 * 5",
            "Naive_Casimir_trace_24_squared_22_cubed_equals": 6_133_248,
            "6_133_248_equals": "2^9 * 3^2 * 11^3",
            "does_720_divide_it": "NO — 720 has prime 5 which does not appear in 24^2 * 22^3",
        },
        "therefore": (
            "A_4 x (naive Casimir trace) is RATIONAL but NOT INTEGER "
            "a priori. The factor of 5 in 720 must come from elsewhere "
            "— likely the Gritsenko-Nikulin weight-5 form Delta_5 "
            "contributing an additional factor of 5 in a product with "
            "chi(K3) = 24 and h^v = 22. This is NOT checked anywhere "
            "in Wave 5."
        ),
        "required_for_integral_preservation": [
            "Explicit v, w in Lambda_Mukai.",
            "Evaluate <v, (3P/2 - tt) (x) t (x) t (x) t w>_{Muk}.",
            "Check result is in 720 * Lambda_Mukai (x) Lambda_Mukai.",
            "If not, find the specific Z-linear combination that makes it so, or demote preservation to Q.",
        ],
        "honest_status": (
            "Wave 5's 'integral preservation' claim is rational "
            "preservation in disguise. The denominator 720 is consistent "
            "but not sufficient. True integral preservation on the "
            "Narain lattice requires the specific Casimir trace "
            "computation, which has not been done."
        ),
    }


# ---------------------------------------------------------------------
# Explicit Casimir trace check on the simplest Lambda_Mukai element
# ---------------------------------------------------------------------


def simplest_lambda_Mukai_Casimir_trace() -> Dict[str, object]:
    r"""Attempt the explicit Casimir trace on the simplest Lambda_Mukai element.

    Let v = (1, 0, ..., 0) in H^0(K3; Z) component of Lambda_Mukai.
    Then <v, v>_{Muk} = 2 (point-class pairing with itself = 2 x top-class).

    Actually, Mukai form on Lambda_Mukai = H^0 (+) H^2 (+) H^4:
        <(a_0, a_2, a_4), (b_0, b_2, b_4)>_{Muk}
            = <a_2, b_2>_{K3} - a_0 b_4 - a_4 b_0
    The canonical H^0 generator is the class of a point (degree 0),
    the H^4 is the fundamental class.

    Pairing <(1, 0, 0), (1, 0, 0)>_{Muk}:
    a_2 = 0, a_0 = 1, a_4 = 0, b_0 = 1, b_4 = 0.
        = 0 - 1 * 0 - 0 * 1 = 0.
    So <e_0, e_0> = 0. Not helpful.

    Try <(1, 0, 0), (0, 0, 1)>: a_0 = 1, a_4 = 0, b_0 = 0, b_4 = 1.
        = 0 - 1 * 1 - 0 * 0 = -1.
    So <e_0, e_24> = -1. This pair has standard Mukai pairing -1.

    Using this pair as a lattice element:
    Let v = (e_0 + e_24) - a "dual pair" with <v, v> = 0 + 0 - 2 = -2.

    Now the Casimir: in so(4, 20) acting on V = Lambda_Mukai (x) C,
    the Casimir C_2 = sum_a T^a T_a acts on a vector v in the
    defining rep V_{(1,0,...,0)} of so(4, 20) by the value
        C_2 | vector rep = h^v - 2 = 20 (for so(N): C_2 on vector rep
        = N - 2; for so(24): C_2 = 22).

    Hmm — C_2 on vector rep of so(N) is N - 2? Let me re-check.

    For so(N), with generators T^a normalised to <T^a, T^b>_Killing =
    2 h^v delta^{ab}:
        Casimir C_2 on defining rep V_vec (dim N):
            (C_2)_vec = (N - 2) * Id

    Wait, actually:
        C_2 | V_vec (dim N) = h^v * Id / h^v_normalisation
    depends on convention. Standard: for so(N), h^v = N - 2, and
    C_2 on V_vec = (N - 2) in one convention or (N - 2)/(h^v) in another.

    For so(24): C_2 on V_vec (rank 24) = 22 (if normalised so that
    the longest root has length sqrt(2)).

    Now the question: does 720 divide the trace
        tr_{V_vec} (T^a T_a T^b T_b T^c T_c)
    on Lambda_Mukai = V_vec of so(4, 20)?

    Cubic Casimir trace: sum_{abc} f^{abc} T_a T_b T_c = 0 for simply-
    laced so (it's the "d^{(3)}" which vanishes for ADE).

    Quartic Casimir trace: sum_{abcd} d^{(4)}_{abcd} T_a T_b T_c T_d
    has a known form for so(N) involving the Pfaffian or the 4th-symmetric
    invariant.

    For so(24), there are TWO independent quartic Casimir invariants:
        C_2^2 = (h^v)^2 on V_vec = 22^2 = 484
        C_4 = symmetric degree-4 trace = ??? (not immediate from standard formulas)

    The coefficient 720 in A_4 comes from K3 * K5_pentagonal +
    tet-leg + ... with denominator 720. For integer evaluation on
    Lambda_Mukai, the combination 141,952,310 times the C_2^2 and C_4
    traces on the vector rep must be in the lattice, i.e., give integers
    modulo 720.

    Without computing C_2^2 and C_4 on Lambda_Mukai explicitly (in the
    BASIS of Lambda_Mukai), I cannot settle integrality.

    Partial check: 484 * 720 / 720 = 484, which is an integer. So at
    least the C_2^2 piece is fine. The issue is C_4.

    CONCLUSION: the integer-preservation claim is PLAUSIBLE but not
    verified. A proper verification would require an explicit basis of
    Lambda_Mukai = -2 E_8 + 3 U + H^0 + H^4 and an explicit computation
    of the quartic Casimir trace matrix. This is a concrete Wave 6+
    computational project that I have not completed here.
    """
    return {
        "simplest_lattice_pair": "(1, 0, 0) + (0, 0, 1), i.e., H^0 + H^4 generators",
        "mukai_pairing": -1,
        "casimir_on_vector_rep_so_24": 22,
        "quartic_casimir_invariants_so_24": {
            "C_2_squared": "22^2 = 484",
            "C_4_independent": "NOT computed here; requires explicit basis",
        },
        "verdict": (
            "Without explicit Lambda_Mukai basis and quartic Casimir "
            "matrix, integrality of A_4 x Casimir_quartic_trace is NOT "
            "verified. The 4-loop correction is RATIONAL with "
            "denominator 720; INTEGRAL preservation is PLAUSIBLE but "
            "not CONFIRMED."
        ),
    }


# ---------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------


def wave6_costello_torsion_report() -> Dict[str, object]:
    r"""Wave-6 Costello torsion / integrality report."""
    return {
        "T1_K3_integral_cohomology": K3_integral_cohomology(),
        "T2_wave5_rational_check": wave5_rational_preservation_check(),
        "T3_integral_preservation_requirements": integral_preservation_required_computation(),
        "T4_simplest_Lambda_Mukai_check": simplest_lambda_Mukai_Casimir_trace(),
        "consolidated_finding": {
            "K3_torsion": (
                "K3 is simply connected and torsion-free in integral "
                "cohomology in all degrees. The Igusa denominator "
                "720 = 2^4 * 3^2 * 5 does NOT come from K3 topology; "
                "it comes from the graph-automorphism factorials of "
                "the 4-loop Feynman diagrams."
            ),
            "Q_vs_Z_preservation": (
                "Wave 5's arithmetic-preservation claim is RATIONAL "
                "(A_4 * 720 is an integer); it is NOT integral "
                "(A_4 * <v, Casimir^{(4)} w>_{Lambda_Mukai} is not "
                "verified to be a Z-valued tensor on the Narain lattice). "
                "The distinction matters for Spin(4, 20; Z) preservation, "
                "where Z-valued lattice vectors must map to Z-valued "
                "lattice vectors."
            ),
            "where_Schur_multipliers_live": (
                "The Wave 5 '(Q/Z)^{24} cocycle = 24 Niemeier lattices' "
                "is a legitimate group-cohomology torsion result "
                "(H^2(Spin(4,20); U(1)) vs H^*(K3; Z)). But it is a "
                "STATEMENT ABOUT THE SYMMETRY GROUP, not about K3 "
                "topology. The two are often conflated; they should "
                "not be."
            ),
            "verdict": (
                "Demote 'integral arithmetic preservation at 4 loops' "
                "to 'rational arithmetic preservation at 4 loops, with "
                "integral preservation conjectural, requiring a "
                "separate computation on the explicit Mukai lattice "
                "basis'."
            ),
        },
    }


if __name__ == "__main__":
    import json
    report = wave6_costello_torsion_report()

    def trim(x, maxlen=400):
        if isinstance(x, dict):
            return {k: trim(v, maxlen) for k, v in x.items()}
        if isinstance(x, list):
            return [trim(y, maxlen) for y in x[:10]]
        s = str(x)
        return s if len(s) <= maxlen else s[:maxlen] + "..."

    print(json.dumps(trim(report), indent=2, default=str))
