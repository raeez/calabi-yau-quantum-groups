"""Gritsenko 1999 additive lift Delta_5 = Grit(eta^9 theta_1).

Verifies the Gritsenko (not Ikeda) origin of the K3 BKM Igusa cusp form
by computing the first N Fourier coefficients of Delta_5 via the additive
lift and cross-checking against the Gritsenko-Nikulin product formula.

Primary-lit: Gritsenko 1999; Gritsenko-Nikulin 1998; Borcherds 1998.
"""

from __future__ import annotations


def eta_9_theta_1_fourier_coefficients(n_max: int = 20):
    """First N coefficients of eta^9 theta_1, the Gritsenko source (weight 9/2, index 1/2)."""
    raise NotImplementedError("TODO: q-expansion of eta^9 * theta_1")


def gritsenko_additive_lift(source_coeffs, n_max: int = 20):
    """Gritsenko lift: Jacobi source -> paramodular form.

    Grit(phi)(rho, z, tau) = sum_{d>0} d^{k-1} phi(d*rho, d*z, tau/d).
    """
    raise NotImplementedError("TODO: Gritsenko lift")


def cross_check_gritsenko_nikulin_product(n_max: int = 20) -> bool:
    """Verify Delta_5 = Grit(eta^9 theta_1) matches GN 1998 product formula."""
    raise NotImplementedError("TODO: cross-check")


if __name__ == "__main__":
    print("Gritsenko additive lift scaffold: TODO")
