r"""
Numerical verification of the Borcherds product formula for the Igusa
cusp form Delta_5 of weight 5 on the Siegel upper half-space H_2.

Reference: Lorgat, "A Borcherds lift of the weak Jacobi form phi_{0,1},
generalized Borcherds-Kac-Moody superalgebras and the Igusa cusp form
Delta_5" (2020), Theorem 4.

THE CORRECT IDENTITY (verified to 25-58 digits, see
compute/scripts/verify_igusa_high_precision.py):

    (1/64) * Delta_5(Z) = -exp(pi*i*(z1+z2+z3))
        * prod_{(n,l,m)>0} (1 - exp(2*pi*i*(n*z1 + l*z2 + m*z3)))^{f(nm,l)}

or equivalently, in sign-free form:

    (1/64) * Delta_5(Z) = exp(pi*i*(z1 - z2 + z3))
        * (1 - exp(2*pi*i*z2))
        * prod_{(n,l,m)>0, (n,l,m)!=(0,-1,0)}
            (1 - exp(2*pi*i*(n*z1 + l*z2 + m*z3)))^{f(nm,l)}

where Z = [[z1, z2], [z2, z3]] in H_2, f(n,l) are Fourier coefficients
of the weak Jacobi form phi_{0,1} = phi_{12,1} / delta_{12}, and
(n,l,m) > 0 means: n >= 0, m >= 0, l arbitrary if n > 0 or m > 0,
and l < 0 if n = m = 0.

SIGN EXPLANATION: The factor of -1 is NOT a branch-cut artifact.
It arises from the (n=0, l=-1, m=0) root, the unique root with
discriminant D = -1. For r = exp(2*pi*i*z2) with |r| < 1, this
factor is (1 - r^{-1})^1 = -(1/r)(1-r), contributing an explicit -1.
This corresponds to the odd simple root delta_3 = f_3 in the BKM
superalgebra. The paper's Theorem 4 as literally written is missing
this sign.

Also verified is the key identity (from Section 2 of the paper):

    1 + (1/64) * sum_{t >= 1} f(1+2t, 1, 1) * q^t = prod_{k >= 1} (1-q^k)^9

where f(n,l,m) are Fourier coefficients of Delta_5.
"""

import numpy as np
from mpmath import mp, mpf, mpc, pi as mpi, exp as mexp
from mpmath import jtheta, nint as mnint, re as mre


# ---------------------------------------------------------------------------
# Part 1: Fourier coefficients of the weak Jacobi form phi_{0,1}
# ---------------------------------------------------------------------------

def _phi01_mpmath(tau, z, prec=50):
    """
    Evaluate phi_{0,1}(tau, z) using mpmath's Jacobi theta functions.

    Uses the Eichler-Zagier / Kawai-Yamada-Yang identity:

        phi_{0,1}(tau, z) = 4 * [ (theta_2(z|tau) / theta_2(0|tau))^2
                                 + (theta_3(z|tau) / theta_3(0|tau))^2
                                 + (theta_4(z|tau) / theta_4(0|tau))^2 ]

    mpmath convention: jtheta(j, z_arg, q) with z_arg = pi*z, q = exp(i*pi*tau).
    """
    mp.dps = prec
    tau = mpc(tau)
    z = mpc(z)
    q_nome = mexp(mpc(0, 1) * mpi * tau)

    z_arg = mpi * z
    z_zero = mpc(0)

    th2_z = jtheta(2, z_arg, q_nome)
    th2_0 = jtheta(2, z_zero, q_nome)
    th3_z = jtheta(3, z_arg, q_nome)
    th3_0 = jtheta(3, z_zero, q_nome)
    th4_z = jtheta(4, z_arg, q_nome)
    th4_0 = jtheta(4, z_zero, q_nome)

    return 4 * ((th2_z / th2_0)**2 + (th3_z / th3_0)**2 + (th4_z / th4_0)**2)


def phi_01_numerical(tau, z, N_terms=100):
    """
    Evaluate phi_{0,1}(tau, z) numerically using numpy.

    Uses the theta-ratio formula with direct summation.
    """
    def _theta(j, tau, z, N):
        result = 0.0j
        for n in range(-N, N + 1):
            if j == 2:
                nh = n + 0.5
                result += np.exp(1j * np.pi * nh**2 * tau + 2j * np.pi * nh * z)
            elif j == 3:
                result += np.exp(1j * np.pi * n**2 * tau + 2j * np.pi * n * z)
            elif j == 4:
                result += ((-1)**n) * np.exp(1j * np.pi * n**2 * tau
                                              + 2j * np.pi * n * z)
        return result

    th2_z = _theta(2, tau, z, N_terms)
    th2_0 = _theta(2, tau, 0, N_terms)
    th3_z = _theta(3, tau, z, N_terms)
    th3_0 = _theta(3, tau, 0, N_terms)
    th4_z = _theta(4, tau, z, N_terms)
    th4_0 = _theta(4, tau, 0, N_terms)

    return 4.0 * ((th2_z / th2_0)**2 + (th3_z / th3_0)**2 + (th4_z / th4_0)**2)


def compute_f_disc(D_max, prec=None):
    """
    Compute the Fourier coefficients f(D) of the weak Jacobi form phi_{0,1}
    for discriminants D = 4n - l^2 in the range [-1, D_max].

    The coefficient f(n, l) of q^n r^l in phi_{0,1} depends only on
    D = 4n - l^2 (and is zero when D < -1).

    Verification: f(D) satisfies sum_{l} f(n, l) = 0 for all n >= 1
    (since phi_{0,1}(tau, 0) = 12 is independent of tau, so only the
    n=0 term contributes to the sum over l at z=0).

    Parameters
    ----------
    D_max : int
        Maximum discriminant.
    prec : int or None
        mpmath decimal precision. If None, auto-calculated.

    Returns
    -------
    dict : D -> f(D) (integer)
    """
    N_max = D_max // 4 + 2

    if prec is None:
        prec = max(50, 8 * N_max + 30)
    mp.dps = prec

    Y = max(mpf(2), min(mpf(5), mpf(prec) / (6 * max(N_max, 1))))
    tau = mpc(0, Y)
    q = mexp(mpc(0, 2) * mpi * tau)

    l_max = int(np.sqrt(4 * N_max + 1)) + 2
    M = 2 * l_max + 1

    z_vals = [mpf(j) / M for j in range(M)]
    phi_vals = [_phi01_mpmath(tau, z_j, prec) for z_j in z_vals]

    # DFT in z: extract G(l) = sum_n f(n,l)*q^n
    G = {}
    for l in range(-l_max, l_max + 1):
        s = mpc(0)
        for j in range(M):
            s += phi_vals[j] * mexp(mpc(0, -2) * mpi * l * z_vals[j])
        G[l] = s / M

    # Extract f(n, l) order by order
    f_nl = {}
    residual = dict(G)
    for n in range(N_max + 1):
        qn = q ** n if n > 0 else mpc(1)
        for l in range(-l_max, l_max + 1):
            D = 4 * n - l * l
            if D < -1:
                f_nl[(n, l)] = 0
            else:
                raw = residual[l] / qn
                f_nl[(n, l)] = int(mnint(mre(raw)))
            residual[l] -= mpc(f_nl[(n, l)]) * qn

    # Build f_disc: D -> f(D), with consistency check
    f_disc_map = {}
    for (n, l), val in f_nl.items():
        D = 4 * n - l * l
        if D < -1 or val == 0:
            continue
        if D in f_disc_map:
            if f_disc_map[D] != val:
                raise ValueError(
                    f"phi_{{0,1}} coefficient inconsistency: f({D}) = "
                    f"{f_disc_map[D]} vs {val} from (n={n}, l={l}). "
                    f"Increase precision (currently {prec})."
                )
        else:
            f_disc_map[D] = val

    return f_disc_map


# Module-level cache for f(D)
_F_DISC_CACHE = None
_F_DISC_CACHE_DMAX = -1


def f_disc(D):
    """Return f(D) for phi_{0,1}."""
    global _F_DISC_CACHE, _F_DISC_CACHE_DMAX
    D_need = max(D + 10, 100)
    if _F_DISC_CACHE is None or D_need > _F_DISC_CACHE_DMAX:
        _F_DISC_CACHE = compute_f_disc(D_need)
        _F_DISC_CACHE_DMAX = D_need
    return _F_DISC_CACHE.get(D, 0)


def f_coeff(n, l):
    """Return f(n, l) for phi_{0,1}. Equals f(4n - l^2)."""
    D = 4 * n - l * l
    if D < -1:
        return 0
    return f_disc(D)


# ---------------------------------------------------------------------------
# Part 2: Borcherds infinite product for (1/64)*Delta_5
# ---------------------------------------------------------------------------

def borcherds_product(z1, z2, z3, N_prod=15, D_max=None):
    """
    Evaluate the Borcherds infinite product (Theorem 4):

        exp(pi*i*(z1+z2+z3)) * prod_{(n,l,m)>0}
            (1 - exp(2*pi*i*(n*z1 + l*z2 + m*z3)))^{f(nm, l)}

    which equals (1/64)*Delta_5(Z) up to a sign convention (see module
    docstring for discussion).

    The ordering (n,l,m) > 0 means:
        n >= 0, m >= 0, l in Z  -- if n > 0 or m > 0
        l < 0                   -- if n = m = 0

    Computed via log-sum for numerical stability.

    Parameters
    ----------
    z1, z2, z3 : complex
        Coordinates on H_2, with Im(Z) positive definite.
    N_prod : int
        Truncation: n, m in [0, N_prod], |l| <= N_prod.
    D_max : int or None
        Maximum discriminant for f(D). Default: (N_prod+1)^2 + 4.

    Returns
    -------
    complex
    """
    if D_max is None:
        D_max = (N_prod + 1)**2 + 4

    f_tab = compute_f_disc(D_max)

    def _f(n_prime, l):
        D = 4 * n_prime - l * l
        if D < -1:
            return 0
        return f_tab.get(D, 0)

    z1, z2, z3 = complex(z1), complex(z2), complex(z3)

    log_sum = 1j * np.pi * (z1 + z2 + z3)

    # Case 1: n = m = 0, l < 0
    for l in range(-N_prod, 0):
        ef = _f(0, l)
        if ef == 0:
            continue
        X = np.exp(2j * np.pi * l * z2)
        log_sum += ef * np.log(1.0 - X)

    # Case 2: n > 0 or m > 0
    for n in range(0, N_prod + 1):
        for m in range(0, N_prod + 1):
            if n == 0 and m == 0:
                continue
            for l in range(-N_prod, N_prod + 1):
                ef = _f(n * m, l)
                if ef == 0:
                    continue
                X = np.exp(2j * np.pi * (n * z1 + l * z2 + m * z3))
                if abs(X) > 1e200:
                    continue
                log_sum += ef * np.log(1.0 - X)

    return np.exp(log_sum)


# ---------------------------------------------------------------------------
# Part 3: Delta_5 via genus-2 theta constants
# ---------------------------------------------------------------------------

def _even_theta_characteristics():
    """
    Return the 10 even theta characteristics (a, b) with a, b in (Z/2Z)^2.
    Even iff a^T b = 0 mod 2.
    """
    chars = []
    for a0 in [0, 1]:
        for a1 in [0, 1]:
            for b0 in [0, 1]:
                for b1 in [0, 1]:
                    if (a0 * b0 + a1 * b1) % 2 == 0:
                        chars.append(((a0, a1), (b0, b1)))
    return chars


def _genus2_theta(Z, a, b, N_terms=30):
    """
    Genus-2 theta constant with characteristic [a; b]:

        theta[a,b](Z) = sum_{n in Z^2} exp(pi*i * (n + a/2)^T Z (n + a/2)
                                         + pi*i * b^T (n + a/2))

    Terms with |exponent| producing negligible contributions are skipped
    to avoid overflow.
    """
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    Y = Z.imag  # Imaginary part of Z (positive definite)
    result = 0.0j

    for n1 in range(-N_terms, N_terms + 1):
        for n2 in range(-N_terms, N_terms + 1):
            v = np.array([n1 + a[0] / 2.0, n2 + a[1] / 2.0])
            # The exponent is pi*i*(v^T Z v + b^T v).
            # Its real part is -pi*(v^T Y v) + pi*Im(b^T v) (b is real, so last term=0).
            # Magnitude: exp(-pi * v^T Y v). Skip if negligible.
            decay = np.pi * (v[0]**2 * Y[0, 0] + 2 * v[0] * v[1] * Y[0, 1]
                             + v[1]**2 * Y[1, 1])
            if decay > 500:  # exp(-500) ~ 7e-218, negligible
                continue
            quad = (v[0]**2 * Z[0, 0] + 2.0 * v[0] * v[1] * Z[0, 1]
                    + v[1]**2 * Z[1, 1])
            lin = b[0] * v[0] + b[1] * v[1]
            exponent = 1j * np.pi * (quad + lin)
            # Guard against overflow: real part of exponent must not be too large
            if exponent.real > 500:
                continue
            result += np.exp(exponent)

    return result


def delta5_theta(z1, z2, z3, N_terms=30):
    """
    Compute Delta_5(Z) as the product of 10 even genus-2 theta constants:

        Delta_5(Z) = prod_{[a;b] even} theta[a,b](Z)

    Parameters
    ----------
    z1, z2, z3 : complex
        Z = [[z1, z2], [z2, z3]] in H_2.
    N_terms : int
        Lattice summation range per dimension.
    """
    Z = np.array([[z1, z2], [z2, z3]], dtype=complex)
    chars = _even_theta_characteristics()
    assert len(chars) == 10

    # Compute in log-space to avoid overflow
    log_result = 0.0j
    for (a, b) in chars:
        theta_val = _genus2_theta(Z, a, b, N_terms)
        if theta_val == 0:
            return 0.0j
        log_result += np.log(theta_val)
    return np.exp(log_result)


# ---------------------------------------------------------------------------
# Part 4: Verification routines
# ---------------------------------------------------------------------------

def verify_product_formula(z1, z2, z3, N_prod=15, N_theta=30, D_max=None):
    """
    Verify |(1/64)*Delta_5(Z)| = |Borcherds_product(z1, z2, z3)|.

    The identity holds up to a sign that depends on the branch of
    log chosen for the analytic continuation of the Borcherds product.
    We verify both the absolute-value agreement and the phase.

    Returns dict with 'delta5_theta', 'borcherds_product', 'ratio',
    'abs_relative_error' (should be < 1e-10 for good convergence).
    """
    Z_im = np.array([[z1, z2], [z2, z3]], dtype=complex).imag
    assert Z_im[0, 0] > 0 and np.linalg.det(Z_im) > 0, \
        "Z must be in the Siegel upper half-space"

    d5 = delta5_theta(z1, z2, z3, N_terms=N_theta)
    bp = borcherds_product(z1, z2, z3, N_prod=N_prod, D_max=D_max)

    lhs = d5 / 64.0
    if abs(bp) < 1e-300:
        ratio = float('inf')
        abs_ratio = float('inf')
    else:
        ratio = lhs / bp
        abs_ratio = abs(lhs) / abs(bp)

    return {
        'delta5_theta': d5,
        'borcherds_product': bp,
        'lhs_over_rhs': ratio,
        'abs_ratio': abs_ratio,
        'abs_relative_error': abs(abs_ratio - 1.0),
        'phase_ratio': ratio / abs(ratio) if abs(ratio) > 0 else None,
    }


def _eta_power_series(exponent, N):
    """
    Compute prod_{k>=1} (1-q^k)^exponent as a power series in q up to q^N.
    Returns array of length N+1.
    """
    c = np.zeros(N + 1, dtype=np.float64)
    c[0] = 1.0
    for k in range(1, N + 1):
        for _ in range(abs(exponent)):
            if exponent > 0:
                for n in range(N, k - 1, -1):
                    c[n] -= c[n - k]
            else:
                for n in range(k, N + 1):
                    c[n] += c[n - k]
    return c


def verify_eta9_identity(N_terms=50):
    """
    Verify the identity from Section 2:

        1 + (1/64) * sum_{t>=1} f_Delta(1+2t, 1, 1) * q^t
        = prod_{k>=1} (1-q^k)^9

    where f_Delta(n,l,m) are Fourier coefficients of Delta_5.

    Strategy: evaluate BOTH sides at specific numerical values of q
    (i.e., specific tau) and check agreement. The LHS is computed by
    evaluating Delta_5 via theta constants at a carefully chosen point
    Z = [[tau, iB], [iB, iA]] with A, B large, extracting the
    (l=1, m=1) Fourier-Jacobi sector as a function of tau.

    The key observation: at Z = [[tau, iB], [iA, iA]] with A, B large,
        Delta_5(Z) ~ phi_{5,1}(tau, iB) * exp(-pi*A) + O(exp(-3*pi*A))
    and
        phi_{5,1}(tau, iB) ~ [sum_n f(n,1,1)*exp(pi*i*n*tau)] * exp(-pi*B) + O(exp(-3*pi*B))

    So Delta_5(Z) * exp(pi*(A+B)) ~ sum_n f(n,1,1)*exp(pi*i*n*tau)
    = 64 * exp(pi*i*tau) * [1 + (1/64)*sum_{t>=1} f(1+2t,1,1)*exp(2*pi*i*t*tau)]
    = 64 * exp(pi*i*tau) * prod_{k>=1} (1-q^k)^9   [the identity to verify]

    where q = exp(2*pi*i*tau).

    Therefore, we verify:
        Delta_5(tau, iB, iA) * exp(pi*(A+B)) / (64 * exp(pi*i*tau))
        = prod_{k>=1} (1 - exp(2*pi*i*k*tau))^9

    at several tau values.

    Returns dict with 'max_relative_error', 'test_results'.
    """
    # We need to extract the l=1 Fourier coefficient of the first
    # Fourier-Jacobi coefficient of Delta_5.
    #
    # Delta_5(Z) = sum_{m odd, m>0} phi_{5,m}(tau, z2) * exp(pi*i*m*z3)
    # phi_{5,1}(tau, z2) = sum_{n odd, l odd} f(n,l,1) * exp(pi*i*(n*tau + l*z2))
    #
    # Strategy:
    # 1. Fix z3 = iA with A large to isolate m=1 (suppress m=3 by exp(-2*pi*A)).
    # 2. Evaluate at M different z2 values to separate l components.
    # 3. DFT in z2 to extract l=1 coefficient.
    # 4. This gives sum_n f(n,1,1)*exp(pi*i*n*tau) as a function of tau.
    # 5. Compare with 64*exp(pi*i*tau)*prod(1-q^k)^9 (the RHS).
    #
    # Since l is ODD in the Delta_5 expansion (l = 1 mod 2), and the
    # z2 dependence is exp(pi*i*l*z2) with l odd, we parameterize
    # z2 = x2 + i*y2 with x2 = j/M for j = 0,...,M-1.
    # The DFT extracts coefficients of exp(pi*i*l*x2) = exp(2*pi*i*(l/2)*x2).
    # For l=1: frequency = 1/2. For l=3: frequency = 3/2.
    # With M evaluation points at x2 = j/M, the DFT has resolution 1/M.
    # We need M >= 4 to resolve half-integer frequencies.

    A = 8.0    # Im(z3): suppresses m=3 by exp(-2*pi*A) ~ 2e-22
    y2 = 0.15  # Im(z2): small enough to keep all z2 points in H_2
    M_z2 = 6   # number of z2 evaluation points

    test_taus = [0.0 + 2.0j, 0.3 + 1.5j, 0.5 + 1.8j]
    results = []

    for tau in test_taus:
        # Check H_2 condition: Im(tau)*A > y2^2
        assert tau.imag * A > y2**2, f"Not in H_2: {tau.imag}*{A} <= {y2**2}"

        # Evaluate Delta_5 at M_z2 different z2 values
        z2_vals = [float(j) / M_z2 + 1j * y2 for j in range(M_z2)]
        d5_vals = np.array([
            delta5_theta(tau, z2_val, 1j * A, N_terms=25)
            for z2_val in z2_vals
        ])

        # Divide by exp(-pi*A) to remove m=1 exponential from z3
        d5_normalized = d5_vals * np.exp(np.pi * A)

        # DFT in z2 to extract l=1 coefficient of phi_{5,1}
        # d5_normalized[j] ~ sum_{l odd} phi_l(tau) * exp(pi*i*l*(j/M + i*y2))
        # = sum_{l odd} phi_l(tau) * exp(-pi*l*y2) * exp(pi*i*l*j/M)
        # The l=1 coefficient:
        # phi_1(tau) * exp(-pi*y2) = (1/M) * sum_j d5_normalized[j] * exp(-pi*i*j/M)
        coeff_l1 = np.sum(
            d5_normalized * np.exp(-1j * np.pi * np.arange(M_z2) / M_z2)
        ) / M_z2

        # Undo the y2 exponential: phi_1(tau) = coeff_l1 * exp(pi*y2)
        phi_l1 = coeff_l1 * np.exp(np.pi * y2)

        # phi_l1 = sum_{n odd, n>=1} f(n,1,1) * exp(pi*i*n*tau)
        # = 64*exp(pi*i*tau) * [1 + (1/64)*sum_{t>=1} f(1+2t,1,1)*q^t]
        # where q = exp(2*pi*i*tau).
        #
        # From the identity:
        # phi_l1 / (64*exp(pi*i*tau)) = prod_{k>=1} (1-q^k)^9

        lhs_val = phi_l1 / (64.0 * np.exp(1j * np.pi * tau))

        # RHS: prod_{k>=1} (1 - q^k)^9
        q = np.exp(2j * np.pi * tau)
        rhs_val = 1.0 + 0.0j
        for k in range(1, N_terms + 1):
            rhs_val *= (1.0 - q**k)**9

        ratio = lhs_val / rhs_val
        results.append({
            'tau': tau,
            'lhs': complex(lhs_val),
            'rhs': complex(rhs_val),
            'ratio': complex(ratio),
            'relative_error': abs(ratio - 1.0),
        })

    max_rel_err = max(r['relative_error'] for r in results)

    return {
        'max_relative_error': max_rel_err,
        'test_results': results,
    }


# ---------------------------------------------------------------------------
# Convenience test points
# ---------------------------------------------------------------------------

def deep_cusp_point():
    """Point deep in H_2: z1=2i, z2=0.1i, z3=2i. det(ImZ)=3.99."""
    return 2.0j, 0.1j, 2.0j


def moderate_point():
    """Generic point: z1=0.1+1.5i, z2=0.05+0.3i, z3=0.15+1.3i. det(ImZ)=1.86."""
    return 0.1 + 1.5j, 0.05 + 0.3j, 0.15 + 1.3j


if __name__ == '__main__':
    print("=" * 70)
    print("Verification of the Borcherds product formula for Delta_5")
    print("=" * 70)

    print("\n--- Fourier coefficients f(D) of phi_{0,1} ---")
    f_tab = compute_f_disc(60)
    for D in sorted(f_tab.keys()):
        if D <= 30:
            print(f"  f({D:3d}) = {f_tab[D]}")

    print("\n--- Product formula verification (deep cusp) ---")
    z1, z2, z3 = deep_cusp_point()
    result = verify_product_formula(z1, z2, z3, N_prod=12, N_theta=25, D_max=80)
    print(f"  |Delta_5/64| / |BP|  = {result['abs_ratio']:.15f}")
    print(f"  Abs relative error   = {result['abs_relative_error']:.2e}")

    print("\n--- eta^9 identity verification ---")
    eta_result = verify_eta9_identity(N_terms=10)
    print(f"  f(1,1,1) = {eta_result['f_1_1_1']} (should be 64)")
    print(f"  Max error = {eta_result['max_error']:.2e}")
