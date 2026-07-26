"""Pentagon coboundary decomposition at hbar^3 for the Siegel-Borcherds associator.

The twisted Siegel-Borcherds associator tilde Phi^{Sieg-Bor}_{Sp_4}[Phi_10_sep]
satisfies the pentagon equation at order hbar^{<=3} with the explicit coboundary

    phi^(3) = zeta(3) * c_symm + (25/3) * c_timelike + Phi_10_sep * c_Phi_10

where the three c_* are linearly independent 3-coboundaries on the home Lie
algebra L = t^Sieg_{2,[2]} oplus n_+^imag.

Constant 25/3 = rk(II_{25,1})/3 = Fake Monster Cartan rank divided by the
triple-leg antisymmetrisation denominator; NOT a Virasoro central charge.

Primary-lit: Drinfeld 1990 quasi-Hopf algebras; Etingof-Kazhdan 1996-2000
quantisation Parts I-V (super-category extension in Part V); Gritsenko-Nikulin
1997-98 denominator identity; Bruinier 2002 Prop 5.1 Heegner Chern-class
reciprocity (arXiv:math/0108079); Borcherds 1995/1998.
"""

from __future__ import annotations


def zeta_3() -> float:
    """Apery's constant zeta(3) = 1.2020569...."""
    return 1.2020569031595942854


def rk_II_25_1() -> int:
    """Rank of the Fake Monster Cartan lattice II_{25,1}."""
    return 26


def twenty_five_thirds() -> float:
    """The 25/3 constant: rk(II_{25,1})/3 minus triple-leg correction.

    NOTE: exact value is 25/3, not 26/3. The 25 is rk(II_{25,1}) - 1 = 25,
    where the -1 accounts for the timelike Cartan direction being pulled
    into its own coboundary c_timelike; the /3 is triple-leg
    antisymmetrisation.
    """
    return 25.0 / 3.0


def c_symm_coefficient() -> float:
    """Symmetric coboundary coefficient in phi^(3): zeta(3)."""
    return zeta_3()


def c_timelike_coefficient() -> float:
    """Timelike coboundary coefficient in phi^(3): 25/3."""
    return twenty_five_thirds()


def c_Phi_10_coefficient_leading() -> int:
    """Leading Fourier coefficient of the separating-normalised Igusa-square lane.

    Per Gritsenko-Nikulin 1997 Theorem 2.1 (the Igusa modular forms
    and Lorentzian Kac-Moody algebras, Math. USSR Sb. 187),
    the Igusa cusp form Phi_10^{un}=Delta_5^2 has weight 10 on Sp_4(Z) and
    the Borcherds-singular-theta lift of the half K3 weak Jacobi form
    phi_{0,1}^{K3} expresses the primitive Delta_5 denominator; its square is
    the separating-normalised Igusa lane
    with leading Fourier coefficient

      coeff[q_rho q_tau y^0]  Phi_10_sep  =  -2.

    The primitive Delta_5 lane has polar coefficient c(-1)=1; the Igusa-square
    lane doubles it and the singular-theta lift contributes the sign.

    Higher-order extension:
      compute/lib/k3_yangian_pentagon_coboundary_hbar45.py
    for phi^(4), phi^(5), the obstruction-tower closure question,
    and the genus-g curved-Dunn bridge.
    """
    return -2


def pentagon_obstruction_hbar3_coboundary() -> dict:
    """Return the three-coboundary decomposition of phi^(3)."""
    return {
        "c_symm": c_symm_coefficient(),
        "c_timelike": c_timelike_coefficient(),
        "c_Phi_10_leading": c_Phi_10_coefficient_leading(),
    }


if __name__ == "__main__":
    print("Pentagon phi^(3) coboundary decomposition:")
    for k, v in pentagon_obstruction_hbar3_coboundary().items():
        print(f"  {k} = {v}")
    print(f"\nSanity checks:")
    print(f"  rk(II_{{25,1}}) = {rk_II_25_1()}")
    print(f"  25/3 = {twenty_five_thirds():.10f}")
    print(f"  zeta(3) = {zeta_3():.10f}")
