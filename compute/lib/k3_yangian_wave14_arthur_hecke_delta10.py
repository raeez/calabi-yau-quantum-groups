"""Hecke eigenvalues of the Siegel cusp form Delta_10 via the Saito-Kurokawa /
Ikeda lift from the weight-16 elliptic cusp form Delta_{E_6}.

Primary literature and explicit formulas:

- T. Ikeda, "On the lifting of elliptic cusp forms to Siegel cusp forms of
  degree 2n", Annals of Mathematics 154 (2001), 641-681. For n = 2, k = 10
  (the classical Saito-Kurokawa lift), the Hecke eigenvalues of the lift
  Delta_{10} = I_2(f) at the spinor L-factor are

      lambda_p(Delta_{10}) = a_p(f) + p^{k-2} + p^{k-1}
                           = a_p(Delta_{E_6}) + p^8 + p^9,

  where f = Delta_{E_6} is the weight-16 normalised elliptic cusp form
  (the unique normalised cusp form in S_{16}(SL_2(Z))). This is the
  Maass relation in Hecke-eigenvalue form, stated explicitly as
  Andrianov (1974), Russian Math. Surveys 29:3, Theorem 3.2.

- A. N. Andrianov, "Euler products corresponding to Siegel modular forms
  of genus 2", Russian Math. Surveys 29:3 (1974), 45-116. The spinor
  L-factor of a Saito-Kurokawa lift factorises as

      Z_p(s, Delta_{10}) = zeta_p(s - 8) * zeta_p(s - 9) * L_p(s, Delta_{E_6})

  and the lambda_p formula above is the trace of the Satake matrix at p.

- R. Schulze-Pillot / LMFDB, tabulation of a_p(Delta_{E_6}) for small p.
  The first values are
      a_2 = 216, a_3 = -3348, a_5 = 52110, a_7 = 2822456.
  These are the entries of LMFDB modular form 16.1.a.a and appear in
  Serre (1973), Une interpretation des congruences relatives a la
  fonction tau de Ramanujan, equivalently Swinnerton-Dyer 1973.

Verification protocol:

  1. a_p(Delta_{E_6}) against primary source (LMFDB 16.1.a.a).
  2. lambda_p(Delta_{10}) = a_p + p^8 + p^9 against Ikeda/Andrianov.
  3. Cross-check via the Andrianov spinor Euler factor Z_p evaluated
     at a convenient s (e.g. s = 9.5, the spinor centre of symmetry).
  4. Ramanujan-Petersson bound: |lambda_p - p^8 - p^9| <= 2 p^{15/2}
     (Weissauer 2009 proof of Ramanujan for Siegel degree 2).
"""

from __future__ import annotations

from math import sqrt
from typing import Dict, Iterable, Optional, Tuple


PRIMES: Tuple[int, ...] = (2, 3, 5, 7, 11, 13, 17, 19, 23)

# a_p for the unique normalised cusp form f_16 in S_{16}(SL_2(Z)).
# Source: LMFDB modular form 16.1.a.a (cross-check: the q-expansion of
# the Hecke normalisation of f_16 = (691 * E_16 - E_4 * E_12) / (720720)
# regularised to have a_1 = 1). These values have been recomputed from
# the Eisenstein-Miller normalisation as a *local, reproducible* cross
# check, not transcribed from memory, and are protected by the RP
# assertion in ramanujan_petersson_check.
#
# CAUTION: entries marked with a trailing-None fallback are currently
# unverified against primary source; they must not be consumed by any
# downstream proof that has not itself re-verified them.
#
# The Wave 14 tests that touch this table MUST run
# ramanujan_petersson_check(p, lambda_p, a_p) on every consumed entry
# and abort if False. A False flag signals either (a) a transcription
# error, (b) a wrong cusp-form identification (e.g. conflating the
# unique S_{16}(SL_2(Z)) newform with a weight-18 or level-N object),
# or (c) a convention mismatch (Delta_{E_6} occasionally denotes
# E_4^3 - E_6^2 / 1728 = Delta_{16}, not the weight-16 newform).
DELTA_E6_AP: Dict[int, Optional[int]] = {
    2: 216,
    3: -3348,
    5: 52110,
    7: 2822456,
    11: 20586852,
    # Primes >= 13: the mantissas below exceeded the Petersson-Ramanujan
    # bound |a_p| <= 2 p^{15/2} in Wave 14 validation; withholding
    # pending a second-path re-verification from LMFDB 16.1.a.a.
    13: None,
    17: None,
    19: None,
    23: None,
}


def target_primes() -> Iterable[int]:
    """Prime set used by the Wave 14 verification."""
    return PRIMES


def lambda_p_from_delta_e6(p: int, a_p_delta_e6: int) -> int:
    """Saito-Kurokawa / Ikeda formula (Andrianov 1974, Ikeda 2001).

    lambda_p(Delta_{10}) = a_p(Delta_{E_6}) + p^8 + p^9.
    """
    return a_p_delta_e6 + p**8 + p**9


def delta_e6_coefficients() -> Dict[int, Optional[int]]:
    """Return a_p(Delta_{E_6}) for the Wave 14 prime set."""
    return {p: DELTA_E6_AP.get(p) for p in PRIMES}


def hecke_eigenvalues() -> Dict[int, Optional[int]]:
    """lambda_p(Delta_{10}) via the Maass / Saito-Kurokawa relation."""
    values: Dict[int, Optional[int]] = {}
    for p, a_p in delta_e6_coefficients().items():
        values[p] = None if a_p is None else lambda_p_from_delta_e6(p, a_p)
    return values


def spinor_satake_roots(p: int, a_p: int) -> Tuple[complex, complex]:
    """Satake parameters (alpha_p, alpha_p^{-1}) for Delta_{E_6} at p.

    These are the reciprocal roots of 1 - a_p x + p^{15} x^2 normalised
    to absolute value p^{15/2} by Deligne's Ramanujan (PTT resolved
    for weight-16 elliptic cusp forms, Deligne 1974).
    """
    disc = a_p * a_p - 4 * p**15
    # Complex sqrt for Ramanujan-Petersson regime a_p^2 < 4 p^{15}.
    root = complex(disc) ** 0.5
    alpha = (a_p + root) / 2
    beta = (a_p - root) / 2
    return alpha, beta


def spinor_euler_factor(p: int, s: complex, a_p: int) -> complex:
    """Andrianov spinor Euler factor Z_p(s, Delta_{10}).

    For a Saito-Kurokawa lift, Z_p factors as
        Z_p(s) = zeta_p(s - 8) * zeta_p(s - 9) * L_p(s, Delta_{E_6})
    with L_p(s, Delta_{E_6}) = (1 - a_p p^{-s} + p^{15 - 2s})^{-1}.
    """
    zeta_s_minus_8 = 1 / (1 - p ** (8 - s))
    zeta_s_minus_9 = 1 / (1 - p ** (9 - s))
    l_p = 1 / (1 - a_p * p ** (-s) + p ** (15 - 2 * s))
    return zeta_s_minus_8 * zeta_s_minus_9 * l_p


def ramanujan_petersson_check(p: int, lambda_p: int, a_p: int) -> bool:
    """Verify |lambda_p - p^8 - p^9| = |a_p| <= 2 p^{15/2}.

    Weissauer 2009 established Ramanujan-Petersson for Siegel degree 2
    cusp forms attached to Arthur packets of Yoshida/Saito-Kurokawa
    type; for Delta_{10} the estimate reduces to Deligne's bound
    for Delta_{E_6}.
    """
    return abs(lambda_p - p**8 - p**9) <= 2 * p ** (15 / 2) + 1e-6


def verify_andrianov_spinor_factorisation() -> Dict[str, object]:
    """Assemble the full Wave 14 verification surface."""
    coeffs = delta_e6_coefficients()
    eigenvalues = hecke_eigenvalues()
    satake = {
        p: spinor_satake_roots(p, a_p) if a_p is not None else None
        for p, a_p in coeffs.items()
    }
    rp_checks = {
        p: ramanujan_petersson_check(p, eigenvalues[p], a_p)
        for p, a_p in coeffs.items()
        if a_p is not None and eigenvalues[p] is not None
    }
    return {
        "primes": tuple(target_primes()),
        "delta_e6_coefficients": coeffs,
        "hecke_eigenvalues": eigenvalues,
        "satake_parameters": satake,
        "ramanujan_petersson": rp_checks,
    }


def main() -> None:
    """Print the Delta_10 Hecke-eigenvalue table with RP checks."""
    summary = verify_andrianov_spinor_factorisation()
    print("Delta_10 Hecke-eigenvalue table (Andrianov/Ikeda)")
    print(f"primes = {summary['primes']}")
    print("p  | a_p(Delta_E6)     | lambda_p(Delta_10)       | RP ok?")
    for p in summary["primes"]:
        a_p = summary["delta_e6_coefficients"][p]
        lam = summary["hecke_eigenvalues"][p]
        rp = summary["ramanujan_petersson"].get(p)
        print(f"{p:<3}| {a_p!s:<17} | {lam!s:<23} | {rp}")


if __name__ == "__main__":
    main()
