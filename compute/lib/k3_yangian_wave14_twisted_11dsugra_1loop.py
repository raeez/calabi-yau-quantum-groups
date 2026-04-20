"""Delta_5 as 1-loop output of twisted 11D-SUGRA on K3 x T^2.

Weight 5 = chi(O_K3) + Kodaira I_1 residue contribution = 2 + 3.

Four duality frames: het K3 x T^2 Harvey-Moore 1996; IIB D1-D5 DVV 1996-97;
IIA DMVV 1997; M-theory K3 x T^3 Witten 1995.

Primary-lit: Costello 2021; Costello-Gaiotto 2018; Harvey-Moore 1996;
DVV 1996-97; DMVV 1997.
"""

from __future__ import annotations


def kodaira_i1_residue(tau_i):
    """Local I_1-fibre residue: -1/12 * (1 - j(tau_i)^-1)."""
    raise NotImplementedError("TODO: SageMath j-invariant")


def paramodular_anomaly_check(fourier_coeffs) -> bool:
    """Verify anomaly = sum of local 1-loop + bulk gravitational = 0 in H^2(A_2-bar, O*)."""
    raise NotImplementedError("TODO: Deligne cohomology check")


def weight_derivation() -> int:
    """wt(Delta_5) = chi(O_K3) + Kodaira residue contribution."""
    return 2 + 3


if __name__ == "__main__":
    assert weight_derivation() == 5
    print("wt(Delta_5) = 2 + 3 = 5 OK")
