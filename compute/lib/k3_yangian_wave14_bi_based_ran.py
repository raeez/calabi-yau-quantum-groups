"""Bi-based Ran-space factorization datum for K3 chiral bialgebra.

Averaging morphism av: Ran(P^1)_{M_24} -> A_2-bar as
av = Torelli_K3 o KugaSatake o j_Kodaira.

Primary-lit: Beilinson-Drinfeld 2004; Francis-Gaitsgory 2012; Kuga-Satake
1967; Piatetski-Shapiro-Shafarevich 1971; Baily-Borel 1966; Bruinier 2002.
"""

from __future__ import annotations


def kodaira_j_24_point_config(elliptic_k3_data):
    """24 j-invariants from the I_1 fibres."""
    raise NotImplementedError("TODO")


def kuga_satake_lift(hodge_k3):
    """Kuga-Satake 1967: K3 Hodge -> abelian 4-fold."""
    raise NotImplementedError("TODO")


def k3_torelli_period(abelian_4fold):
    """Period map -> A_2-bar via Baily-Borel."""
    raise NotImplementedError("TODO")


def averaging_morphism(config_24_points):
    """av = Torelli_K3 o KugaSatake o j_Kodaira."""
    hodge = {"j_invariants": config_24_points}
    a4 = kuga_satake_lift(hodge)
    return k3_torelli_period(a4)


def nearby_cycles_at_node(node_position):
    """Kashiwara-Malgrange nearby cycles at each node."""
    raise NotImplementedError("TODO")


def bruinier_prop_5_1_check(chern_class):
    """Chern class of L^Delta_5 on H_1 is order-8 in CH^1(H_1)."""
    raise NotImplementedError("TODO")


if __name__ == "__main__":
    print("Bi-based Ran scaffold: TODO")
