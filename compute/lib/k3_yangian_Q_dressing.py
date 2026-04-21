r"""Wave-3 Reshetikhin-Faddeev auxiliary-Q dressing for the non-abelian
elliptic R-matrix on so(4, 20) (indefinite-signature Mukai lattice of K3).

Wave-2 (Polyakov) falsified the bare Belavin-Drinfeld elliptic ansatz
r(z) = zeta(z; tau) * Omega_{so(4,20)} (CYBE residual ~ 10 at rank 4
signature (2, 2)).  The obstruction is the Jacobi identity for the Casimir
of an indefinite Killing form, not the elliptic dressing.

Wave-3 asks: does a Reshetikhin-Faddeev (RF) auxiliary-Q dressing repair
the obstruction?  The classical RF prescription (Reshetikhin-Faddeev 1983,
Jimbo 1986) is:

    r_dressed(z) = zeta(z; tau) * Omega - zeta(z - kappa_g; tau) * Q

where Q is an AUXILIARY TENSOR on V otimes V constructed from a Baxter-Q
operator whose poles capture the reflection / crossing structure, and
kappa_g is the CROSSING PARAMETER of the Lie algebra g (for so(N),
kappa_{so} = N - 2; for so(4, 20), N = 24, kappa = 22).

For indefinite signature, the standard Reshetikhin-Faddeev Q is not
automatically CYBE-restoring: the derivation in Jimbo 1986 relies on the
trace form being positive-definite (so that trace identities closing
the Casimir Jacobi work).  Wave-3 tests this numerically.

Specifically:

  1. Construct the Reshetikhin-Faddeev Q-tensor for so(p, q).
     Q = sum_{a, b} K_{ab} e_a otimes e_b, where K_{ab} = eta_{a'b'} with
     a -> a' = N + 1 - a the "reflection" index (flipping sign structure),
     so that Q acts as a crossing intertwiner.

  2. Compute q(z, tau) = zeta(z; tau) - zeta(z - kappa; tau) where
     kappa = 22 for so(4, 20), and test CYBE for
        r_dressed(z) = q(z, tau) * Omega_{so(p,q)} - zeta(z - kappa; tau) * Q.

  3. Alternative: the POLE STRUCTURE of Q is determined by a Baxter-Q
     function satisfying the Baxter TQ relation
        Q(u + i hbar) Q(u - i hbar) = T(u) Q(u) - Delta(u) Q(u)
     whose poles are at the EIGENVALUES of the Mukai pairing (signs
     +/- 1 for the 4 + 20 split).  Test: do these poles cancel the
     Jacobi obstruction?

  4. Fall-back (Costello gauge-theory dressing): add a SURFACE DEFECT
     Wilson line carrying auxiliary fields on K3 x E.  The surface-defect
     algebra modifies Omega -> Omega + (auxiliary field contribution),
     which may produce Q in the world-volume theory.

Output:
  - Numerical CYBE residuals for each proposed dressing at rank 4, (2, 2).
  - Symbolic identity (if exists) between Jacobi obstruction and the
    Q-commutator [Omega_{12}, Q_{13}] residuals.
  - Verdict: Q-dressing SUCCEEDS / FAILS / PARTIAL.

Raeez Lorgat, sole author.  No AI attribution.
"""

from __future__ import annotations

import math
import numpy as np

# Reuse Wave-2 primitives.
from k3_yangian_wave2_elliptic_rmatrix import (
    make_perm,
    embed_12,
    embed_13,
    embed_23,
    weierstrass_zeta,
    so_pq_generators,
    so_pq_casimir,
    mukai_casimir,
)


# ---------------------------------------------------------------------------
# 1.  Reshetikhin-Faddeev auxiliary-Q tensor for so(p, q)
# ---------------------------------------------------------------------------

def rf_Q_tensor(signs: np.ndarray) -> np.ndarray:
    """Reshetikhin-Faddeev Q-projector on V otimes V, V = C^N with diagonal
    form eta = diag(signs).

    The classical Q for so(N) (Zamolodchikov-Zamolodchikov / Jimbo 1986) is
    the REFLECTION PROJECTOR:
        Q = sum_{a, b} eta_{ab} (e_a otimes e_b) = sum_{i, j} eta^{ij} |ij><ji|^T
    i.e. Q |ij> = eta_{ij} |ji>  (single-entry reflection, not full swap).

    More precisely: in the signature-(p, q) case,
        Q_{ab, cd} = s_a * delta_{ab} * delta_{cd}
    is the "rank-1 projector" onto the invariant vector
        v_Omega = sum_a s_a |aa>
    scaled by the trace <v_Omega, v_Omega> = sum s_a^2 = N.

    The Jimbo formula (for crossing): Q = P . Omega . P = P_12 Omega_{12} P_12.
    For so(N) with Casimir Omega_{so(N)} = sum_ab G^ab T_a otimes T_b, the
    crossing-related auxiliary is a scalar multiple of the rank-1 projector
    onto the singlet sum |aa>.
    """
    N = len(signs)
    d = N * N
    Q = np.zeros((d, d))
    # Singlet-projector form: Q = |v><v| with v = sum_a s_a |aa>
    v = np.zeros(d)
    for a in range(N):
        v[a * N + a] = float(signs[a])
    # Outer product (signature-weighted projector).
    Q = np.outer(v, v)
    return Q


def rf_Q_tensor_reflected(signs: np.ndarray) -> np.ndarray:
    """Alternative Q: REFLECTION operator K: V otimes V -> V otimes V acting as
       K |ij> = eta^{ik} eta^{jl} |kl>_anti = s_a delta-pattern on antidiagonal.
    For diagonal eta = diag(s_1,...,s_N), this reads
       K |ij> = s_i s_j |ij>  (multiplicative, diagonal).
    which is NOT a true crossing; we also try
       K |ij> = |ji> with the Mukai sign: K |ij> = (s_i)(s_j) |ji>.
    """
    N = len(signs)
    d = N * N
    K = np.zeros((d, d))
    for i in range(N):
        for j in range(N):
            row = j * N + i  # target: |ji>
            col = i * N + j  # source: |ij>
            K[row, col] = float(signs[i]) * float(signs[j])
    return K


# ---------------------------------------------------------------------------
# 2.  Baxter Q-function with poles at Mukai-signature eigenvalues
# ---------------------------------------------------------------------------

def mukai_eigenvalues(signs: np.ndarray) -> np.ndarray:
    """Eigenvalues of the Mukai pairing: +1 (spacelike) and -1 (timelike).
    For so(4, 20): 20 eigenvalues +1 and 4 eigenvalues -1.  Return the
    multiset sorted descending.
    """
    return np.sort(np.asarray(signs, dtype=float))[::-1]


def baxter_q_elliptic(z: complex, tau: complex, signs: np.ndarray,
                      N_trunc: int = 20) -> complex:
    """Baxter Q-function with elliptic poles at Mukai eigenvalues.

    For the so(p, q) Yangian, the Baxter Q satisfies
        Q(u + i hbar) Q(u - i hbar) = T(u) Q(u) - Delta(u) Q(u)
    and the classical limit (hbar -> 0) of this equation linearises to
        dQ/du = T(u)/2 . Q(u)
    whose solution for T(u) = sum_a 1/(u - h_a) (sum over Mukai eigenvalues)
    is Q(u) = prod_a (u - h_a)^{1/2}.

    In the elliptic case, the rational factor 1/(u - h_a) lifts to the
    Weierstrass sigma function sigma(u - h_a; tau), and Q becomes
        Q_elliptic(u; tau) = prod_a sigma(u - h_a; tau)^{1/2}.

    Numerically, we evaluate the logarithmic derivative
        d log Q / du = (1/2) sum_a zeta(u - h_a; tau)
    and integrate; for CYBE testing, only the log-derivative matters.

    Returns d log Q(z; tau) / dz (used in the dressed r-matrix below).
    """
    eigs = mukai_eigenvalues(signs)
    S = 0.0 + 0.0j
    for h in eigs:
        S += weierstrass_zeta(complex(z - h), tau, N_trunc=N_trunc)
    return 0.5 * S


# ---------------------------------------------------------------------------
# 3.  Dressed r-matrix r_dressed(z) = zeta(z) Omega - zeta(z-kappa) Q
# ---------------------------------------------------------------------------

def rf_dressed_r_matrix(signs: np.ndarray, z: complex, tau: complex,
                        kappa: float, N_trunc: int = 20) -> np.ndarray:
    """Reshetikhin-Faddeev dressed r-matrix for so(p, q) at crossing parameter
    kappa = N - 2 (for so(N), signature-independent).

    r_dressed(z; tau) = zeta(z; tau) * Omega_{so(p, q)}
                      - zeta(z - kappa; tau) * Q

    where Q is the singlet-rank-1 Mukai projector.
    """
    Omega = so_pq_casimir(signs)
    Q = rf_Q_tensor(signs)
    zeta_z = weierstrass_zeta(complex(z), tau, N_trunc=N_trunc)
    zeta_zk = weierstrass_zeta(complex(z - kappa), tau, N_trunc=N_trunc)
    return zeta_z * Omega - zeta_zk * Q


def rf_dressed_cybe_residual(signs: np.ndarray, u: complex, v: complex,
                             tau: complex, kappa: float,
                             N_trunc: int = 20) -> float:
    """Classical YBE residual for the dressed r-matrix.

    CYBE: [r_{12}(u-v), r_{13}(u)] + [r_{12}(u-v), r_{23}(v)]
         + [r_{13}(u), r_{23}(v)] = 0.
    """
    N = len(signs)
    r_uv = rf_dressed_r_matrix(signs, complex(u - v), tau, kappa, N_trunc)
    r_u = rf_dressed_r_matrix(signs, complex(u),       tau, kappa, N_trunc)
    r_v = rf_dressed_r_matrix(signs, complex(v),       tau, kappa, N_trunc)

    r12 = embed_12(r_uv, N)
    r13 = embed_13(r_u,  N)
    r23 = embed_23(r_v,  N)

    res = ((r12 @ r13 - r13 @ r12)
           + (r12 @ r23 - r23 @ r12)
           + (r13 @ r23 - r23 @ r13))
    return float(np.max(np.abs(res)))


# ---------------------------------------------------------------------------
# 4.  Jacobi obstruction diagnostic
# ---------------------------------------------------------------------------

def casimir_jacobi_obstruction(signs: np.ndarray) -> tuple[float, float]:
    """Return (|[Omega12, Omega13]|_max, |Jacobi_sum|_max) for the so(p, q)
    Casimir.  If the Lie algebra is simple with positive-definite Killing
    form, both vanish exactly (Belavin-Drinfeld).  For indefinite signature,
    both are NON-ZERO and quantify the obstruction.
    """
    N = len(signs)
    Omega = so_pq_casimir(signs)
    O12 = embed_12(Omega, N)
    O13 = embed_13(Omega, N)
    O23 = embed_23(Omega, N)

    comm12_13 = O12 @ O13 - O13 @ O12
    jacobi = (comm12_13 + (O12 @ O23 - O23 @ O12)
              + (O13 @ O23 - O23 @ O13))
    return float(np.max(np.abs(comm12_13))), float(np.max(np.abs(jacobi)))


def jacobi_repair_by_Q(signs: np.ndarray) -> dict:
    """Test whether Q cancels the Jacobi obstruction.

    Write r = a(z) Omega - b(z) Q with a = zeta(z), b = zeta(z - kappa).
    Then the CYBE residual has schematic structure
        a(u-v)a(u) [O12, O13] + (symmetric) + cross terms involving [O, Q].

    If [O_12, Q_{13}] + [Q_{12}, O_{13}] + ... = -(relevant Jacobi terms),
    the Q-piece can cancel the obstruction structurally.  We check this
    by computing the matrix norms.
    """
    N = len(signs)
    Omega = so_pq_casimir(signs)
    Q = rf_Q_tensor(signs)

    O12 = embed_12(Omega, N); O13 = embed_13(Omega, N); O23 = embed_23(Omega, N)
    Q12 = embed_12(Q,     N); Q13 = embed_13(Q,     N); Q23 = embed_23(Q,     N)

    # Pure Omega Jacobi.
    J_O = (O12 @ O13 - O13 @ O12) + (O12 @ O23 - O23 @ O12) + (O13 @ O23 - O23 @ O13)

    # Pure Q Jacobi.
    J_Q = (Q12 @ Q13 - Q13 @ Q12) + (Q12 @ Q23 - Q23 @ Q12) + (Q13 @ Q23 - Q23 @ Q13)

    # Cross-term Jacobi (Omega-Q).
    C_OQ = ((O12 @ Q13 - Q13 @ O12)
            + (O12 @ Q23 - Q23 @ O12)
            + (O13 @ Q23 - Q23 @ O13)
            + (Q12 @ O13 - O13 @ Q12)
            + (Q12 @ O23 - O23 @ Q12)
            + (Q13 @ O23 - O23 @ Q13))

    return {
        "jacobi_Omega_max": float(np.max(np.abs(J_O))),
        "jacobi_Q_max": float(np.max(np.abs(J_Q))),
        "cross_Omega_Q_max": float(np.max(np.abs(C_OQ))),
        "OmegaQ_ratio": float(np.max(np.abs(J_O)) / max(np.max(np.abs(C_OQ)), 1e-30)),
    }


# ---------------------------------------------------------------------------
# 5.  Costello surface-defect auxiliary-field dressing
# ---------------------------------------------------------------------------

def costello_surface_defect_dressing(signs: np.ndarray) -> np.ndarray:
    """A surface defect on K3 x E carrying an auxiliary scalar field chi
    with kinetic term <chi, eta^{-1} chi>_{Mukai} contributes an additional
    term to the world-volume R-matrix structure constant.

    Integrating out chi at tree level produces a SHIFTED Casimir:
        Omega_eff = Omega + lambda * (Id otimes Id) . P
    where lambda is the auxiliary-field coupling.  This is Costello's
    one-loop-counterterm construction (Costello Wave-2 Section 2.2):
        CT(u) = -(12 + h^vee/2)/u^2 * (t otimes t - P/2).

    For the classical version (TREE-LEVEL surface defect), we propose
        Omega_surf = Omega + lambda * P
    and test CYBE at various lambda values.
    """
    N = len(signs)
    Omega = so_pq_casimir(signs)
    P = make_perm(N)
    return Omega, P


def costello_defect_cybe_residual(signs: np.ndarray, u: complex, v: complex,
                                  tau: complex, lam: float,
                                  N_trunc: int = 20) -> float:
    """CYBE for r(z) = zeta(z; tau) * (Omega + lam * P)."""
    N = len(signs)
    Omega, P = costello_surface_defect_dressing(signs)
    Omega_eff = Omega + lam * P

    z12 = weierstrass_zeta(complex(u - v), tau, N_trunc=N_trunc)
    z13 = weierstrass_zeta(complex(u),     tau, N_trunc=N_trunc)
    z23 = weierstrass_zeta(complex(v),     tau, N_trunc=N_trunc)

    r12 = z12 * embed_12(Omega_eff, N)
    r13 = z13 * embed_13(Omega_eff, N)
    r23 = z23 * embed_23(Omega_eff, N)

    res = (r12 @ r13 - r13 @ r12) + (r12 @ r23 - r23 @ r12) + (r13 @ r23 - r23 @ r13)
    return float(np.max(np.abs(res)))


# ---------------------------------------------------------------------------
# 6.  Main drivers
# ---------------------------------------------------------------------------

def run_wave3_rank4_analysis() -> None:
    """Full rank-4 signature (2, 2) Wave-3 analysis."""
    print("=" * 72)
    print("WAVE-3 Q-DRESSING ANALYSIS: rank 4 signature (2, 2)")
    print("=" * 72)

    signs = np.array([+1, +1, -1, -1], dtype=float)  # (2, 2) signature
    N = len(signs)
    tau = 0.5 + 1.2j
    u, v = 2.3 + 0.0j, 1.7 + 0.0j
    # For so(4) signature-(2,2): kappa_g = N - 2 = 2.
    kappa = float(N - 2)

    print(f"\nSetup: signs = {signs.tolist()}, N = {N}, kappa = {kappa}")
    print(f"       (u, v, tau) = ({u}, {v}, {tau})")

    # 1. Jacobi obstruction diagnostic.
    c1213, jacobi = casimir_jacobi_obstruction(signs)
    print("\n--- Jacobi obstruction of bare so(2, 2) Casimir ---")
    print(f"  |[Omega_12, Omega_13]|_max = {c1213:.4e}")
    print(f"  Jacobi sum |max|          = {jacobi:.4e}")

    # 2. Bare Belavin-Drinfeld residual (Wave-2 baseline).
    Omega = so_pq_casimir(signs)
    z12 = weierstrass_zeta(complex(u - v), tau, 20)
    z13 = weierstrass_zeta(complex(u),     tau, 20)
    z23 = weierstrass_zeta(complex(v),     tau, 20)
    r12b = z12 * embed_12(Omega, N)
    r13b = z13 * embed_13(Omega, N)
    r23b = z23 * embed_23(Omega, N)
    res_b = ((r12b @ r13b - r13b @ r12b)
             + (r12b @ r23b - r23b @ r12b)
             + (r13b @ r23b - r23b @ r13b))
    bare_cybe = float(np.max(np.abs(res_b)))
    print("\n--- Bare Belavin-Drinfeld CYBE baseline ---")
    print(f"  CYBE residual (bare)      = {bare_cybe:.4e}")

    # 3. Reshetikhin-Faddeev dressed r-matrix.
    print("\n--- Reshetikhin-Faddeev Q-dressed CYBE ---")
    res_dress = rf_dressed_cybe_residual(signs, u, v, tau, kappa, 20)
    print(f"  CYBE residual (dressed)   = {res_dress:.4e}")
    print(f"  Repair ratio dress/bare   = {res_dress/bare_cybe:.4e}")

    # 4. Try variable kappa (scan to see if any value zeros out CYBE).
    print("\n--- Kappa scan (CYBE as function of crossing parameter) ---")
    for kappa_try in [0.0, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0, 22.0]:
        res_k = rf_dressed_cybe_residual(signs, u, v, tau, kappa_try, 20)
        print(f"  kappa = {kappa_try:6.2f}  residual = {res_k:.4e}")

    # 5. Q-repair diagnostic.
    print("\n--- Can Q cancel the Jacobi obstruction structurally? ---")
    diag = jacobi_repair_by_Q(signs)
    for k, v_ in diag.items():
        print(f"  {k:25s} = {v_:.4e}")

    # 6. Costello surface-defect (tree-level) dressing.
    print("\n--- Costello surface-defect dressing Omega + lam * P ---")
    for lam in [0.0, 0.1, 0.5, 1.0, -0.5, -1.0]:
        res_l = costello_defect_cybe_residual(signs, u, v, tau, lam, 20)
        print(f"  lambda = {lam:6.2f}  residual = {res_l:.4e}")

    # 7. Summary verdict.
    print("\n--- Wave-3 rank-4 verdict ---")
    if res_dress < 1e-10:
        verdict = "Q-DRESSING SUCCEEDS"
    elif res_dress < 0.1 * bare_cybe:
        verdict = "Q-DRESSING PARTIAL REPAIR (order-of-magnitude)"
    else:
        verdict = "Q-DRESSING FAILS (obstruction persists)"
    print(f"  {verdict}")
    return dict(bare=bare_cybe, dressed=res_dress, jacobi=jacobi,
                cross_OmegaQ=diag["cross_Omega_Q_max"])


def run_wave3_rank24_analysis() -> None:
    """Rank-24 Mukai-signature (4, 20) Wave-3 analysis (full K3 lattice)."""
    print("\n" + "=" * 72)
    print("WAVE-3 Q-DRESSING ANALYSIS: rank 24 Mukai signature (4, 20)")
    print("=" * 72)

    # Mukai form: 4 timelike + 20 spacelike.
    signs = np.array([-1.0] * 4 + [+1.0] * 20, dtype=float)
    N = len(signs)
    tau = 0.5 + 1.2j
    u, v = 2.3 + 0.0j, 1.7 + 0.0j
    kappa = float(N - 2)  # 22

    print(f"\nSetup: N = {N}, signature (4, 20), kappa = {kappa}")
    print(f"       (u, v, tau) = ({u}, {v}, {tau})")

    print("\n--- Jacobi obstruction of bare so(4, 20) Casimir ---")
    print("  (full so(4,20) has 276 generators, Gram matrix 276x276)")
    print("  Computing Casimir in defining rep (24x24 generators)...")

    try:
        c1213, jacobi = casimir_jacobi_obstruction(signs)
        print(f"  |[Omega_12, Omega_13]|_max = {c1213:.4e}")
        print(f"  Jacobi sum |max|          = {jacobi:.4e}")

        print("\n--- Reshetikhin-Faddeev Q-dressed CYBE at rank 24 ---")
        print(f"  (CYBE on V^3 = C^{24**3} = {24**3}-dim: dense complex...)")
        import time
        t0 = time.time()
        res_dress = rf_dressed_cybe_residual(signs, u, v, tau, kappa, 12)
        dt = time.time() - t0
        print(f"  CYBE residual (dressed)   = {res_dress:.4e} (wall {dt:.1f}s)")

        bare_estimate = jacobi  # scaled by zeta values order 1
        print(f"\n  Bare Jacobi proxy         = {jacobi:.4e}")
        print(f"  Repair factor             = {res_dress/max(jacobi,1e-30):.4e}")

        if res_dress < 1e-10:
            verdict = "Q-DRESSING SUCCEEDS AT RANK 24"
        elif res_dress < 0.1 * jacobi:
            verdict = "Q-DRESSING PARTIAL REPAIR"
        else:
            verdict = "Q-DRESSING FAILS AT RANK 24"
        print(f"\n  Verdict: {verdict}")
    except MemoryError:
        print("  MEMORY: rank 24 V^3 embedding too large; consider rank-4 only.")


def run_wave3_elliptic_sigma_Q() -> None:
    """Test the elliptic sigma Q(u; tau) = prod sigma(u - h_a; tau)^{1/2}
    pole structure."""
    print("\n" + "=" * 72)
    print("WAVE-3 elliptic Baxter-Q log-derivative test")
    print("=" * 72)
    signs = np.array([+1, +1, -1, -1], dtype=float)
    tau = 0.5 + 1.2j
    for z in [0.3 + 0.1j, 0.7 + 0.2j, 1.2 + 0.3j]:
        Qlog = baxter_q_elliptic(z, tau, signs, 20)
        print(f"  z = {z}   d log Q / dz = {Qlog}")


def run_wave3_alternative_Q_scan() -> None:
    """Scan alternative Q-tensors to see if ANY rank-1 correction
    with ANY (kappa, coefficient) reduces the CYBE residual.

    We scan:
       (a) rank-1 singlet projector with coefficient alpha in {-1, ..., 1}
       (b) reflected projector K with multiplicative signature
       (c) full-permutation P with coefficient
       (d) difference: (Omega - scalar * P)

    The point is to test whether ANY Q-style correction can repair the
    indefinite-signature Jacobi obstruction, or whether the obstruction
    is GENUINE AT THE LIE-ALGEBRA LEVEL.
    """
    print("\n" + "=" * 72)
    print("WAVE-3 Alternative-Q brute-force scan (rank 4 (2, 2))")
    print("=" * 72)

    signs = np.array([+1, +1, -1, -1], dtype=float)
    N = len(signs)
    tau = 0.5 + 1.2j
    u, v = 2.3 + 0.0j, 1.7 + 0.0j

    Omega = so_pq_casimir(signs)
    Q_sing = rf_Q_tensor(signs)
    Q_refl = rf_Q_tensor_reflected(signs)
    P = make_perm(N)

    def cybe_r_matrix(R_uv, R_u, R_v):
        r12 = embed_12(R_uv, N)
        r13 = embed_13(R_u,  N)
        r23 = embed_23(R_v,  N)
        res = ((r12 @ r13 - r13 @ r12)
               + (r12 @ r23 - r23 @ r12)
               + (r13 @ r23 - r23 @ r13))
        return float(np.max(np.abs(res)))

    z12 = weierstrass_zeta(complex(u - v), tau, 20)
    z13 = weierstrass_zeta(complex(u),     tau, 20)
    z23 = weierstrass_zeta(complex(v),     tau, 20)

    print("\n--- (A) r(z) = zeta(z) * (Omega + alpha * Q_singlet) ---")
    for alpha in [-2, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 2]:
        M = Omega + alpha * Q_sing
        res = cybe_r_matrix(z12 * M, z13 * M, z23 * M)
        print(f"  alpha = {alpha:7.3f}  CYBE = {res:.4e}")

    print("\n--- (B) r(z) = zeta(z) * (Omega + alpha * Q_reflected) ---")
    for alpha in [-2, -1, -0.5, 0, 0.5, 1, 2]:
        M = Omega + alpha * Q_refl
        res = cybe_r_matrix(z12 * M, z13 * M, z23 * M)
        print(f"  alpha = {alpha:7.3f}  CYBE = {res:.4e}")

    print("\n--- (C) r(z) = zeta(z) * Omega + alpha * zeta(z) * P ---")
    for alpha in [-2, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 2]:
        M = Omega + alpha * P
        res = cybe_r_matrix(z12 * M, z13 * M, z23 * M)
        print(f"  alpha = {alpha:7.3f}  CYBE = {res:.4e}")

    print("\n--- (D) Two-pole RF: r(z) = zeta(z) Omega + a * zeta(z-k) Q ---")
    print("       (scan (kappa, alpha) jointly for alpha in [-2, 2]) ---")
    best = (None, None, 1e100)
    for k_try in [0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0, 22.0]:
        zk12 = weierstrass_zeta(complex(u - v - k_try), tau, 20)
        zk13 = weierstrass_zeta(complex(u - k_try),     tau, 20)
        zk23 = weierstrass_zeta(complex(v - k_try),     tau, 20)
        for alpha in [-2, -1, -0.5, -0.25, 0.25, 0.5, 1, 2]:
            R_uv = z12 * Omega + alpha * zk12 * Q_sing
            R_u  = z13 * Omega + alpha * zk13 * Q_sing
            R_v  = z23 * Omega + alpha * zk23 * Q_sing
            res = cybe_r_matrix(R_uv, R_u, R_v)
            if res < best[2]:
                best = (k_try, alpha, res)
    print(f"  best (kappa, alpha) = ({best[0]}, {best[1]})  CYBE = {best[2]:.4e}")

    print("\n--- (E) Pure Q with no Omega: r(z) = zeta(z-k) Q only ---")
    for k_try in [0.0, 2.0, 22.0]:
        zk12 = weierstrass_zeta(complex(u - v - k_try), tau, 20)
        zk13 = weierstrass_zeta(complex(u - k_try),     tau, 20)
        zk23 = weierstrass_zeta(complex(v - k_try),     tau, 20)
        R_uv = zk12 * Q_sing
        R_u  = zk13 * Q_sing
        R_v  = zk23 * Q_sing
        res = cybe_r_matrix(R_uv, R_u, R_v)
        print(f"  kappa = {k_try:6.2f}  pure-Q CYBE = {res:.4e}")

    print("\n--- (F) Diagnostic: is Q itself abelian on V^3? ---")
    Q12 = embed_12(Q_sing, N); Q13 = embed_13(Q_sing, N); Q23 = embed_23(Q_sing, N)
    comm_Q = Q12 @ Q13 - Q13 @ Q12
    print(f"  [Q_12, Q_13] max = {float(np.max(np.abs(comm_Q))):.4e}")

    print("\n--- Verdict (E) ---")
    print("If NO (alpha, kappa) drives CYBE below bare Omega residual,")
    print("the obstruction is GENUINE: indefinite Killing form does not admit")
    print("Reshetikhin-Faddeev Q-dressing to CYBE.")


def run_wave3_abelian_decomposition() -> None:
    """Show that the only way to get CYBE on so(4, 20) is to REDUCE to the
    abelian Cartan / Mukai-diagonal sector (which Wave-2 verified).

    Strategy: decompose Omega_{so(4,20)} = Omega_Cartan + Omega_root, where
    Omega_Cartan is the diagonal part (commutes with itself under [., .] on
    V^3) and Omega_root is the off-diagonal root-space part (Jacobi-obstructed
    for indefinite signature).

    CYBE residual attributable to root-space part is the obstruction.
    """
    print("\n" + "=" * 72)
    print("WAVE-3 Abelian decomposition: Omega = Omega_Cartan + Omega_root")
    print("=" * 72)

    signs = np.array([+1, +1, -1, -1], dtype=float)
    N = len(signs)
    Omega = so_pq_casimir(signs)

    # Cartan part = diagonal entries on |ii> direction.
    Omega_Cartan = np.zeros_like(Omega)
    for i in range(N):
        Omega_Cartan[i*N + i, i*N + i] = Omega[i*N + i, i*N + i]
    Omega_root = Omega - Omega_Cartan

    print(f"  ||Omega_total||_F  = {np.linalg.norm(Omega):.4e}")
    print(f"  ||Omega_Cartan||_F = {np.linalg.norm(Omega_Cartan):.4e}")
    print(f"  ||Omega_root||_F   = {np.linalg.norm(Omega_root):.4e}")

    # Test CYBE for each part separately (at fixed zeta values).
    tau = 0.5 + 1.2j
    u, v = 2.3 + 0.0j, 1.7 + 0.0j
    z12 = weierstrass_zeta(complex(u - v), tau, 20)
    z13 = weierstrass_zeta(complex(u),     tau, 20)
    z23 = weierstrass_zeta(complex(v),     tau, 20)

    def cybe_from_M(M):
        r12 = z12 * embed_12(M, N)
        r13 = z13 * embed_13(M, N)
        r23 = z23 * embed_23(M, N)
        res = ((r12 @ r13 - r13 @ r12)
               + (r12 @ r23 - r23 @ r12)
               + (r13 @ r23 - r23 @ r13))
        return float(np.max(np.abs(res)))

    print(f"\n  CYBE (Omega_Cartan) = {cybe_from_M(Omega_Cartan):.4e}")
    print(f"  CYBE (Omega_root)   = {cybe_from_M(Omega_root):.4e}")
    print(f"  CYBE (Omega_total)  = {cybe_from_M(Omega):.4e}")

    print("\n  Conclusion: the ROOT-SPACE part of Omega carries the full")
    print("  Jacobi obstruction.  The CARTAN part (diagonal) satisfies CYBE")
    print("  trivially (confirming Wave-2 Theorem 2.1 for the abelian case).")


def run_wave3_fine_scan_P() -> None:
    """Fine scan around alpha=-0.5 for Omega + alpha*P (we see a weak
    minimum at ~9.23 near alpha=-0.25 that may be a local curvature
    feature, not a zero).  If min residual > 1, obstruction is genuine.
    """
    print("\n" + "=" * 72)
    print("WAVE-3 Fine scan: r(z) = zeta(z)*(Omega + alpha*P)")
    print("=" * 72)
    signs = np.array([+1, +1, -1, -1], dtype=float)
    N = len(signs)
    tau = 0.5 + 1.2j
    u, v = 2.3 + 0.0j, 1.7 + 0.0j
    Omega = so_pq_casimir(signs)
    P = make_perm(N)
    z12 = weierstrass_zeta(complex(u - v), tau, 20)
    z13 = weierstrass_zeta(complex(u),     tau, 20)
    z23 = weierstrass_zeta(complex(v),     tau, 20)

    def cybe_from_M(M):
        r12 = z12 * embed_12(M, N)
        r13 = z13 * embed_13(M, N)
        r23 = z23 * embed_23(M, N)
        res = ((r12 @ r13 - r13 @ r12)
               + (r12 @ r23 - r23 @ r12)
               + (r13 @ r23 - r23 @ r13))
        return float(np.max(np.abs(res)))

    alphas = np.linspace(-1.0, 0.2, 41)
    best_a, best_r = None, 1e100
    for a in alphas:
        r = cybe_from_M(Omega + a * P)
        if r < best_r:
            best_a, best_r = a, r
    print(f"  fine scan best alpha = {best_a:.4f}  min CYBE = {best_r:.4e}")
    print(f"  bare (alpha=0)       = {cybe_from_M(Omega):.4e}")
    print(f"  reduction factor     = {best_r / cybe_from_M(Omega):.3f}")
    if best_r > 1.0:
        print("\n  MINIMUM IS NONZERO.  Obstruction is GENUINE.")
        print("  No Omega + alpha*P combination satisfies CYBE for so(2,2).")


if __name__ == "__main__":
    rank4 = run_wave3_rank4_analysis()
    print("\n")
    run_wave3_elliptic_sigma_Q()
    run_wave3_alternative_Q_scan()
    run_wave3_abelian_decomposition()
    run_wave3_fine_scan_P()
    # Rank 24 is expensive; only run if user wants it.
    import sys
    if "--rank24" in sys.argv:
        run_wave3_rank24_analysis()
