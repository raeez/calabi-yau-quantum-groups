r"""Rank-24 elliptic YBE verification for Costello's Mukai-diagonal R-matrix.

Polyakov Wave-2 theorem candidate. For the Mukai-diagonal Casimir Omega_eta =
sum_i s_i P_{ii} on V = C^{24} with Mukai signature (4, 20), the full elliptic
R-matrix

    R(z; tau) = exp( hbar * zeta(z; tau) * Omega_eta )

satisfies the quantum YBE at rank 24 EXACTLY (to all orders in hbar), because
Omega_eta is diagonal in the canonical basis {e_i otimes e_j} on V otimes V
and all three embeddings (Omega_{12}, Omega_{13}, Omega_{23}) are mutually
commuting diagonal operators on V otimes V otimes V.

We verify this numerically to machine precision at a small hbar and a generic
modular parameter tau, truncated Eisenstein, rank 24.

Raeez Lorgat sole author.
"""

from __future__ import annotations

import numpy as np
import time

from k3_yangian_wave2_elliptic_rmatrix import (
    make_perm, embed_12, embed_13, embed_23,
    weierstrass_zeta, mukai_casimir, elliptic_R_series,
)


def verify_elliptic_YBE_rank24_Mukai(order: int = 3, hbar: complex = 0.1 + 0j,
                                    u: complex = 2.3 + 0j, v: complex = 1.7 + 0j,
                                    tau: complex = 0.5 + 1.2j,
                                    N_trunc: int = 20,
                                    verbose: bool = True) -> dict:
    """Rank-24 elliptic YBE verification.

    The R-matrix at rank 24 has 24^2 = 576-dim space; embedded into V^{otimes 3}
    it becomes 24^3 = 13824-dim.  Matrix multiplication on 13824 x 13824 is
    feasible (requires ~1.5 GB scratch but numpy handles it).

    Returns YBE residual at given order in hbar.
    """
    N = 24
    signs = np.concatenate([np.ones(4), -np.ones(20)])
    Omega_eta = mukai_casimir(signs)

    t0 = time.time()
    z12 = weierstrass_zeta(complex(u - v), tau, N_trunc=N_trunc)
    z13 = weierstrass_zeta(complex(u),     tau, N_trunc=N_trunc)
    z23 = weierstrass_zeta(complex(v),     tau, N_trunc=N_trunc)

    R12 = elliptic_R_series(Omega_eta, z12, hbar, order)
    R13 = elliptic_R_series(Omega_eta, z13, hbar, order)
    R23 = elliptic_R_series(Omega_eta, z23, hbar, order)

    if verbose:
        print(f"  zeta values computed:  z12={z12:.6f}  z13={z13:.6f}  z23={z23:.6f}")

    R12_ = embed_12(R12, N)
    R13_ = embed_13(R13, N)
    R23_ = embed_23(R23, N)

    if verbose:
        print(f"  rank-24 YBE embeddings: 13824 x 13824 dense complex matrices.")

    LHS = R12_ @ R13_ @ R23_
    RHS = R23_ @ R13_ @ R12_
    residual = float(np.max(np.abs(LHS - RHS)))

    t1 = time.time()
    results = {
        "N": N,
        "signature": "(4,20) Mukai",
        "order_in_hbar": order,
        "hbar": hbar,
        "u": u, "v": v, "tau": tau,
        "Eisenstein_N_trunc": N_trunc,
        "YBE_residual": residual,
        "time_seconds": t1 - t0,
    }
    if verbose:
        print(f"Rank-24 elliptic YBE verification:")
        print(f"  signature: (4,20) Mukai")
        print(f"  order in hbar: {order}")
        print(f"  hbar = {hbar}")
        print(f"  Eisenstein truncation N = {N_trunc}")
        print(f"  YBE residual: {residual:.3e}")
        print(f"  time: {t1 - t0:.1f}s")
    return results


if __name__ == "__main__":
    verify_elliptic_YBE_rank24_Mukai(order=3, N_trunc=15, verbose=True)
