r"""Genus-3 Siegel modular forms, chiral partition functions, and Sp_6(Z).

MATHEMATICAL CONTENT
====================

The genus-3 chiral partition function Z_3(Omega_3) computes the
factorization homology of the chiral algebra over a genus-3 surface
Sigma_3 x S^1, parametrised by the genus-3 period matrix

    Omega_3 in H_3  (Siegel upper half-space of degree 3)

where H_3 = {Omega in M_3(C) : Omega^T = Omega, Im(Omega) > 0}.

The Siegel upper half-space H_3 has complex dimension g(g+1)/2 = 6,
parametrised by the six independent entries of the symmetric 3x3 matrix:

    Omega_3 = ((tau_1,   z_12,  z_13),
               (z_12,   tau_2,  z_23),
               (z_13,   z_23,  tau_3))

  tau_i = period of the i-th handle (diagonal entries)
  z_ij  = off-diagonal coupling between handles i and j

FACTORIZATION HOMOLOGY ORIGIN:
  - At E_2: int_{T^2} A  ->  Z_1(tau) with SL_2(Z) modularity
  - At E_3: int_{Sigma_2 x S^1} A  ->  Z_2(Omega_2) with Sp_4(Z) modularity
  - At E_3: int_{Sigma_3 x S^1} A  ->  Z_3(Omega_3) with Sp_6(Z) modularity

Sp_6(Z) STRUCTURE:
  The genus-3 modular group Sp_6(Z) consists of 6x6 integer matrices
  gamma = ((A, B), (C, D)) preserving the symplectic form
  J_6 = ((0, I_3), (-I_3, 0)), where A, B, C, D are 3x3 integer blocks.

  It acts on H_3 via:
      Omega -> (A*Omega + B) * (C*Omega + D)^{-1}

  The quotient by +/-I_6 gives PSp_6(Z) (AP-CY16 generalised: +/-I_{2g}).

  Generators (Hua-Reiner):
    T_{ij}: Omega -> Omega + e_{ij} (translation by symmetric matrices)
    S:      Omega -> -Omega^{-1}    (Siegel inversion)
  There are 6 independent T-generators (matching dim H_3 = 6).

GENUS-3 THETA FUNCTIONS:
  The genus-3 theta constant with characteristic [a/2; b/2],
  a, b in (Z/2Z)^3, is:

    theta[a,b](Omega) = sum_{n in Z^3} exp(pi*i*(n+a/2)^T*Omega*(n+a/2)
                                         + pi*i*b^T*(n+a/2))

  Number of even characteristics: 2^{g-1}(2^g + 1) = 4*(8+1) = 36 at g=3.
  Number of odd characteristics: 2^{g-1}(2^g - 1) = 4*(8-1) = 28 at g=3.
  Total: 36 + 28 = 64 = 2^{2g} = 2^6.

HEISENBERG GENUS-3 PARTITION FUNCTION (CLASS G):
  For c free bosons, the holomorphic genus-3 partition function is:

      F_3^{Heis}(Omega_3) = [prod_{even [a,b]} theta[a,b](Omega_3)]^{-c/36}

  since there are 36 even characteristics at genus 3.  The product
  of 36 even theta characteristics is the genus-3 analogue of:
    - genus 1: prod of 3 even thetas / 2 (related to eta)
    - genus 2: prod of 10 even thetas = Delta_5

  Denote chi_{18} = prod of 36 even theta constants.  This is a Siegel
  modular form of weight 18 on Sp_6(Z) with a theta multiplier system.
  (Weight = (1/2) * 36 = 18, since each theta has weight 1/2.)

  Then:
      F_3^{Heis}(Omega_3) = chi_{18}(Omega_3)^{-c/36}

  Modular weight of F_3:
      wt(F_3) = -c/2  (genus-independent: always -c/2)

  Check: wt(chi_{18}^{-c/36}) = 18 * (-c/36) = -c/2.  Consistent.

  For c=1: wt = -1/2 (metaplectic).
  For c=24 (K3): wt = -12.

SHADOW CORRECTIONS (CLASS M):
  For class M algebras (W_{1+inf}, K3 sigma model), the genus-3
  shadow corrections generalise the genus-2 cocycles:

      Z_3^{W}(Omega_3) = Z_3^{Heis}(Omega_3) * R_shadow^{(3)}(Omega_3)

  where R_shadow^{(3)} = 1 + sum_{k>=3} S_k * C_k^{(3)}(Omega_3)

  The genus-3 cocycles C_k^{(3)} involve integrals of k-point OPE
  kernels over Sigma_3^k and depend on the six propagators between
  the three handles.

E_3 BAR COHOMOLOGY AT GENUS 3:
  Class L,C:  dim = 2^{3g} = 2^9 = 512
  Class M:    dim = 6^g = 6^3 = 216
  Deficit:    512 - 216 = 296

  For g=3: E_4 = E_inf UNCONDITIONALLY (proved in e3_bar_higher_genus_class_m.py:
  support in degrees {3,...,6}, d_5 shift = 4, mapping degree 6 to degree 2
  which is outside the support range [3,6]).

SCHOTTKY PROBLEM AT GENUS 3:
  At g=3:
    dim M_3 = 3g - 3 = 6
    dim A_3 = g(g+1)/2 = 6
    codim(J_3) = 0

  The Torelli map j: M_3 -> A_3 is DOMINANT (surjective onto a dense
  open subset).  The Jacobian locus J_3 = j(M_3) is dense in A_3.
  The Schottky problem is TRIVIAL at genus 3: every principally
  polarised abelian threefold is (generically) a Jacobian.

  This is the LAST genus where Schottky is trivial.  At g=4:
  codim(J_4) = 1, and the Schottky-Igusa form J in S_8(Sp(8,Z))
  cuts out J_4.

  Consequence for the chiral programme: at genus 3, the shadow tower
  on M_3 and Siegel modular forms on A_3 live on the same space
  (up to codimension-0 complement).  No Schottky obstruction.
  This is obstruction (O4) from thm:shadow-siegel-gap, which is
  ABSENT at g <= 3.

K3 x E AT GENUS 3:
  The genus-3 K3 x E partition function is controlled by genus-3
  Siegel modular forms on Sp_6(Z).  Unlike genus 2, there is NO
  unique cusp form at low weight.  The ring S_*(Sp_6(Z)) is richer:

    - S_12(Sp_6(Z)): contains the Schottky form chi_{12} (Igusa-Tsuyumine)
    - S_18(Sp_6(Z)): contains chi_{18} = prod of 36 even thetas

  The genus-3 analogue of the DMVV formula is:

      Z_3^{DMVV}(Omega_3) = sum over genus-3 Hecke operators applied to
                             the elliptic genus

  This is NOT a single Siegel modular form (unlike genus 2 where
  Z_2^{DMVV} = 1/Phi_10).  The genus-3 DMVV answer involves
  contributions from multiple Siegel modular forms.

  CLAIM STATUS: CONJECTURAL. All genus-3 K3xE results are conditional
  on CY-A_3 (AP-CY6/14).

CONVENTIONS:
  - Omega_3 = 3x3 symmetric complex matrix in H_3
  - q_i = e^{2*pi*i*tau_i}, r_{ij} = e^{2*pi*i*z_{ij}}
  - Im(Omega_3) > 0: positive definite imaginary part (3x3)
  - kappa_ch: from chiral algebra (AP113, always subscripted)
  - kappa_cat: holomorphic Euler characteristic chi(O_X)
  - kappa_BKM: weight of the Borcherds product / BKM denominator

AP COMPLIANCE:
  - AP113: bare kappa FORBIDDEN; all kappa subscripted.
  - AP-CY6/14: A_X for d=3 does not exist. All d=3 results CONJECTURAL.
  - AP-CY8: Borcherds product = bar Euler product is OBSERVATION.
  - AP-CY11: Conditional propagation: Z_3 for K3xE depends on CY-A_3.
  - AP-CY16: Sp_6 quotient by +/-I_6 (6x6), NOT +/-I_7.
  - AP-CY21: E_3 bar dimensions: (1+t)^{3g} for class L,C; NOT class M.
  - FM24: B-cycle sign: verify |q_i| < 1 (Im(tau_i) > 0).
  - AP157: Degeneration type specified where relevant.

MANUSCRIPT REFERENCES:
  chapters/examples/k3e_cy3_programme.tex:
    op:programme-d-schottky, conj:shadow-taut-projection
  chapters/theory/braided_factorization.tex:
    conj:sp4-modularity (genus-2 analogue)
  chapters/examples/toroidal_elliptic.tex:
    thm:shadow-siegel-gap

MATHEMATICAL SOURCES:
  Igusa, "On Siegel modular forms of genus two" (1962)
  Tsuyumine, "On Siegel modular forms of degree three" (1986)
  Poor-Yuen, "Computations of spaces of Siegel modular cusp forms" (2007)
  Salvati Manni, "Slopes of cusp forms of genus 3" (2003)
  Fay, "Theta functions on Riemann surfaces" (1973)
  Grushevsky, "The Schottky problem" (2010)
  Codogni-Shepherd-Barron, "The absence of stable Schottky forms" (2022)
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

from compute.lib.genus2_chiral_partition import (
    _eta_function,
    _theta1_function,
    SHADOW_TOWER_W1INF,
)

from compute.lib.genus2_k3e_full import (
    K3_ALPHA,
    K3_KAPPA_CH,
    K3_S4,
    K3E_CENTRAL_CHARGE,
    K3E_KAPPA_BKM,
    K3E_KAPPA_CAT,
    K3E_KAPPA_CAT_FIBER,
    K3E_KAPPA_CH,
    K3E_KAPPA_FIBER,
    k3_shadow_tower,
)


# =========================================================================
# 1. Siegel upper half-space H_3 utilities
# =========================================================================

def validate_period_matrix_g3(
    Omega: np.ndarray,
) -> np.ndarray:
    r"""Validate a genus-3 period matrix Omega in H_3.

    Checks:
      (i)   Omega is 3x3
      (ii)  Omega is symmetric
      (iii) Im(Omega) is positive definite (all eigenvalues > 0)
      (iv)  |q_i| < 1 for all diagonal entries (FM24: convergence)

    Parameters
    ----------
    Omega : 3x3 complex numpy array

    Returns
    -------
    The validated Omega (unchanged).

    Raises
    ------
    ValueError if any condition fails.
    """
    if Omega.shape != (3, 3):
        raise ValueError(
            f"Period matrix must be 3x3, got shape {Omega.shape}"
        )
    if not np.allclose(Omega, Omega.T, atol=1e-12):
        raise ValueError("Period matrix must be symmetric: Omega != Omega^T")

    Y = Omega.imag
    eigenvalues = np.linalg.eigvalsh(Y)
    if any(ev <= 0 for ev in eigenvalues):
        raise ValueError(
            f"Im(Omega) not positive definite: eigenvalues = {eigenvalues}. "
            f"FM24: this would give |q_i| >= 1, destroying q-expansion convergence."
        )

    # Check diagonal entries individually for clearer error messages
    for i in range(3):
        if Y[i, i] <= 0:
            raise ValueError(
                f"Im(Omega[{i},{i}]) = {Y[i, i]:.6f} <= 0: "
                f"not in Siegel upper half-space H_3."
            )

    return Omega


def make_period_matrix_g3(
    tau1: complex, tau2: complex, tau3: complex,
    z12: complex, z13: complex, z23: complex,
) -> np.ndarray:
    r"""Construct a genus-3 period matrix from its six entries.

    Omega_3 = ((tau_1,  z_12, z_13),
               (z_12,  tau_2, z_23),
               (z_13,  z_23, tau_3))

    Parameters
    ----------
    tau1, tau2, tau3 : complex
        Diagonal entries (handle periods). Must have Im > 0.
    z12, z13, z23 : complex
        Off-diagonal couplings.

    Returns
    -------
    Validated 3x3 period matrix.
    """
    Omega = np.array([
        [tau1, z12, z13],
        [z12, tau2, z23],
        [z13, z23, tau3],
    ], dtype=complex)
    return validate_period_matrix_g3(Omega)


# =========================================================================
# 2. Sp_6(Z) action and generators
# =========================================================================

def sp6_action(
    gamma: np.ndarray, Omega: np.ndarray,
) -> np.ndarray:
    r"""Apply an Sp_6(Z) transformation to a genus-3 period matrix.

    gamma = ((A, B), (C, D)) is a 6x6 symplectic integer matrix
    partitioned into 3x3 blocks.

    The action: Omega -> (A*Omega + B) * (C*Omega + D)^{-1}

    Sp_6(Z) preserves the symplectic form J_6 = ((0, I_3), (-I_3, 0)).

    NOTE: Sp_6(Z) quotient by +/-I_6 (6x6), NOT +/-I_7 (AP-CY16).
    """
    if gamma.shape != (6, 6):
        raise ValueError(f"Sp_6(Z) element must be 6x6, got {gamma.shape}")

    A = gamma[:3, :3]
    B = gamma[:3, 3:]
    C = gamma[3:, :3]
    D = gamma[3:, 3:]

    # Verify symplecticity: gamma^T J gamma = J
    J = np.block([
        [np.zeros((3, 3)), np.eye(3)],
        [-np.eye(3), np.zeros((3, 3))],
    ])
    check = gamma.T @ J @ gamma
    if not np.allclose(check, J, atol=1e-10):
        raise ValueError("Input matrix is not symplectic (Sp_6(Z))")

    numerator = A @ Omega + B
    denominator = C @ Omega + D
    return numerator @ np.linalg.inv(denominator)


def sp6_generators() -> Dict[str, np.ndarray]:
    r"""Return the standard generators of Sp_6(Z).

    Generators (Hua-Reiner):
      T_{ij}: Omega -> Omega + e_{ij}  (6 independent translations)
      S:      Omega -> -Omega^{-1}     (Siegel inversion)

    The 6 translations correspond to the 6 independent entries of
    a symmetric 3x3 matrix: (1,1), (2,2), (3,3), (1,2), (1,3), (2,3).

    Returns dict of 6x6 integer matrices.
    """
    I3 = np.eye(3, dtype=int)
    Z3 = np.zeros((3, 3), dtype=int)

    generators = {}

    # Diagonal translations: T_{ii}, shifting tau_i -> tau_i + 1
    for idx, (i, j) in enumerate([(0, 0), (1, 1), (2, 2)]):
        B = np.zeros((3, 3), dtype=int)
        B[i, j] = 1
        T = np.block([[I3, B], [Z3, I3]])
        generators[f"T{i+1}{j+1}"] = T

    # Off-diagonal translations: T_{ij}, shifting z_{ij} -> z_{ij} + 1
    # For symmetry, B_{ij} = B_{ji} = 1
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        B = np.zeros((3, 3), dtype=int)
        B[i, j] = 1
        B[j, i] = 1
        T = np.block([[I3, B], [Z3, I3]])
        generators[f"T{i+1}{j+1}"] = T

    # Siegel inversion: S: Omega -> -Omega^{-1}
    S = np.block([[Z3, I3], [-I3, Z3]])
    generators["S"] = S

    return generators


def sp6_symplectic_form() -> np.ndarray:
    """Return the 6x6 symplectic form J_6 = ((0, I_3), (-I_3, 0))."""
    return np.block([
        [np.zeros((3, 3)), np.eye(3)],
        [-np.eye(3), np.zeros((3, 3))],
    ])


# =========================================================================
# 3. Genus-3 theta functions
# =========================================================================

def genus3_theta(
    Omega: np.ndarray,
    a: Tuple[int, int, int],
    b: Tuple[int, int, int],
    N_terms: int = 8,
) -> complex:
    r"""Genus-3 theta constant with half-integer characteristic [a/2; b/2].

    theta[a,b](Omega) = sum_{n in Z^3} exp(pi*i*(n+a/2)^T*Omega*(n+a/2)
                                         + pi*i*b^T*(n+a/2))

    Parameters
    ----------
    Omega : 3x3 complex matrix in H_3
    a, b : tuples of 0/1 (elements of (Z/2Z)^3)
    N_terms : summation range per dimension (truncation of Z^3 sum)

    Returns
    -------
    complex : theta[a,b](Omega)

    Note: The computation cost scales as (2*N_terms+1)^3, so N_terms
    should be kept moderate.  For Im(Omega) deep in H_3 (large
    imaginary parts), even N_terms=5 gives high accuracy.
    """
    a_vec = np.array(a, dtype=float)
    b_vec = np.array(b, dtype=float)
    Y = Omega.imag

    result = 0.0j
    for n1 in range(-N_terms, N_terms + 1):
        for n2 in range(-N_terms, N_terms + 1):
            for n3 in range(-N_terms, N_terms + 1):
                v = np.array([
                    n1 + a_vec[0] / 2.0,
                    n2 + a_vec[1] / 2.0,
                    n3 + a_vec[2] / 2.0,
                ])
                # Decay: exp(-pi * v^T Y v)
                decay = math.pi * (v @ Y @ v)
                if decay > 300:
                    continue
                # Full exponent: pi*i * (v^T Omega v + b^T v)
                quad = v @ Omega @ v
                lin = b_vec @ v
                exponent = 1j * math.pi * (quad + lin)
                if exponent.real > 300:
                    continue
                result += np.exp(exponent)
    return result


def even_theta_characteristics_g3() -> List[Tuple[Tuple[int, int, int], Tuple[int, int, int]]]:
    r"""Return the 36 even theta characteristics for genus 3.

    A characteristic (a, b) with a, b in (Z/2Z)^3 is even iff
    a^T b = 0 mod 2.

    At genus g: number of even chars = 2^{g-1}(2^g + 1).
    At g=3: 4*(8+1) = 36.
    """
    chars = []
    for a0 in [0, 1]:
        for a1 in [0, 1]:
            for a2 in [0, 1]:
                for b0 in [0, 1]:
                    for b1 in [0, 1]:
                        for b2 in [0, 1]:
                            if (a0 * b0 + a1 * b1 + a2 * b2) % 2 == 0:
                                chars.append(((a0, a1, a2), (b0, b1, b2)))
    return chars


def odd_theta_characteristics_g3() -> List[Tuple[Tuple[int, int, int], Tuple[int, int, int]]]:
    r"""Return the 28 odd theta characteristics for genus 3.

    A characteristic (a, b) with a, b in (Z/2Z)^3 is odd iff
    a^T b = 1 mod 2.

    At genus g: number of odd chars = 2^{g-1}(2^g - 1).
    At g=3: 4*(8-1) = 28.
    """
    chars = []
    for a0 in [0, 1]:
        for a1 in [0, 1]:
            for a2 in [0, 1]:
                for b0 in [0, 1]:
                    for b1 in [0, 1]:
                        for b2 in [0, 1]:
                            if (a0 * b0 + a1 * b1 + a2 * b2) % 2 == 1:
                                chars.append(((a0, a1, a2), (b0, b1, b2)))
    return chars


def chi18_genus3(
    Omega: np.ndarray,
    N_terms: int = 8,
) -> complex:
    r"""Compute chi_{18}(Omega) = product of 36 even genus-3 theta constants.

    chi_{18} is a Siegel modular form of weight 18 on Sp_6(Z) with a
    theta multiplier system (analogous to Delta_5 of weight 5 at genus 2).

    Weight: each theta constant has weight 1/2, so the product of 36
    has weight 36/2 = 18.

    At genus 2: Delta_5 = product of 10 even thetas, weight 10/2 = 5.
    At genus 3: chi_{18} = product of 36 even thetas, weight 36/2 = 18.

    The SQUARE chi_{18}^2 = chi_{36} is a Siegel modular form of weight 36
    with trivial multiplier (analogous to Phi_10 = Delta_5^2 at genus 2).

    Parameters
    ----------
    Omega : 3x3 complex matrix in H_3
    N_terms : int
        Lattice summation range per dimension.

    Returns
    -------
    complex : chi_{18}(Omega)
    """
    Omega = validate_period_matrix_g3(Omega)
    chars = even_theta_characteristics_g3()
    assert len(chars) == 36

    log_result = 0.0j
    for (a, b) in chars:
        theta_val = genus3_theta(Omega, a, b, N_terms)
        if abs(theta_val) < 1e-300:
            return 0.0j
        log_result += np.log(theta_val)
    return np.exp(log_result)


def chi36_genus3(
    Omega: np.ndarray,
    N_terms: int = 8,
) -> complex:
    r"""Compute chi_{36}(Omega) = chi_{18}(Omega)^2.

    chi_{36} is the genus-3 analogue of Phi_10 = Delta_5^2:
    a Siegel modular form of weight 36 on Sp_6(Z) with TRIVIAL
    multiplier (the squared theta multiplier is trivial).

    Weight: 2 * 18 = 36.
    """
    c18 = chi18_genus3(Omega, N_terms)
    return c18 ** 2


# =========================================================================
# 4. Heisenberg genus-3 partition function (class G)
# =========================================================================

def genus3_partition_heisenberg(
    Omega: np.ndarray,
    c: int = 1,
    N_terms: int = 8,
) -> Dict[str, Any]:
    r"""Genus-3 chiral partition function for the Heisenberg VOA at c copies.

    For the Heisenberg (class G), all A_infinity corrections vanish:
    m_n = 0 for n >= 3.  The genus-3 partition function is:

        F_3^{Heis}(Omega) = chi_{18}(Omega)^{-c/36}

    This generalises the genus-g formula for c free bosons:

        F_g^{Heis}(Omega) = [prod_{even chars} theta[a,b](Omega)]^{-c/N_even(g)}

    where N_even(g) = 2^{g-1}(2^g + 1) is the number of even characteristics.
    Weight: (1/2) * N_even(g) * (-c/N_even(g)) = -c/2.

    At genus 1: N_even = 3, weight -c/2.  (eta^{-c} convention.)
    At genus 2: N_even = 10, weight -c/2. (Delta_5^{-c/12} in our normalisation.)
    At genus 3: N_even = 36, weight -c/2.

    NOTE on genus-2 normalisation: the genus-2 engine uses Delta_5^{-c/12}
    because it parametrises via the automorphy factor det(C*Omega+D)^{weight}
    with weight = -c/2, and Delta_5 has weight 5, so the exponent is
    (-c/2)/5 = -c/10.  However the engine uses Delta_5^{-c/12} which
    includes a normalisation difference.  Here we use the uniform convention:

        F_g = [product of N_even thetas]^{-c/N_even}

    which always gives weight -c/2.

    Modular weight of F_3:
        wt(F_3) = -c/2

    For c=1: wt = -1/2 (metaplectic cover Mp_6(Z)).
    For c=24 (K3): wt = -12.

    Parameters
    ----------
    Omega : 3x3 period matrix in H_3
    c : int
        Central charge (number of free bosons).
    N_terms : int
        Lattice summation range.

    Returns
    -------
    dict with partition function data.
    """
    Omega = validate_period_matrix_g3(Omega)

    c18 = chi18_genus3(Omega, N_terms)
    c36 = c18 ** 2

    # F_3 = chi_{18}^{-c/36}
    if abs(c18) < 1e-300:
        Z3_hol = float('inf')
    else:
        Z3_hol = c18 ** (-c / 36.0)

    # Full (non-holomorphic) partition function
    det_Y = np.linalg.det(Omega.imag)
    if abs(Z3_hol) < float('inf') and det_Y > 0:
        Z3_full = abs(Z3_hol) ** 2 / det_Y ** (c / 2.0)
    else:
        Z3_full = float('inf')

    weight = -c / 2.0

    return {
        "Z3_holomorphic": Z3_hol,
        "Z3_full": Z3_full,
        "chi_18": c18,
        "chi_36": c36,
        "det_Im_Omega": det_Y,
        "central_charge": c,
        "weight": weight,
        "shadow_class": "G",
        "m3_correction": 0.0,
        "genus": 3,
        "modular_group": "Sp_6(Z)",
        "siegel_dim": 6,
        "n_even_theta": 36,
        "explanation": (
            f"Heisenberg at c={c}: F_3 = chi_{{18}}^{{-c/36}} "
            f"= chi_{{18}}^{{{-c}/36}}. "
            f"Class G: all A_inf corrections vanish (free field). "
            f"Siegel modular weight = {weight} for Sp_6(Z) "
            f"(on metaplectic cover if c odd)."
        ),
    }


# =========================================================================
# 5. Genus-3 Eisenstein series and shadow cocycles
# =========================================================================

def _sigma1(n: int) -> int:
    """Sum of divisors of n: sigma_1(n) = sum_{d|n} d."""
    return sum(d for d in range(1, n + 1) if n % d == 0)


def _eisenstein_e2(tau: complex, N_terms: int = 15) -> complex:
    """Quasi-modular Eisenstein series E_2(tau) = 1 - 24*sum sigma_1(n)*q^n."""
    q = np.exp(2j * math.pi * tau)
    result = 1.0 + 0j
    for n in range(1, N_terms + 1):
        result -= 24 * _sigma1(n) * q**n
    return result


def genus3_propagator_matrix(
    Omega: np.ndarray,
) -> np.ndarray:
    r"""Compute the 3x3 propagator matrix for genus-3 shadow cocycles.

    The propagator P_{ij} between handles i and j is:

        P_{ij} = |z_{ij}|^2 / (Im(tau_i) * Im(tau_j))    for i != j
        P_{ii} = 0                                          (no self-propagator)

    This generalises the genus-2 propagator:
        P_{12} = |z|^2 / (Im(tau) * Im(sigma))

    Parameters
    ----------
    Omega : 3x3 period matrix

    Returns
    -------
    3x3 real numpy array of propagators.
    """
    Y = Omega.imag
    P = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            if i != j:
                P[i, j] = abs(Omega[i, j]) ** 2 / (Y[i, i] * Y[j, j])
    return P


def genus3_cocycle_c3(
    Omega: np.ndarray,
    N_terms: int = 10,
) -> complex:
    r"""Genus-3 shadow cocycle C_3^{(3)}(Omega_3) from m_3.

    The cubic correction involves the three-point OPE kernel integrated
    over Sigma_3^3.  In the separating degeneration, the leading
    contribution is:

        C_3^{(3)} ~ alpha * sum_{i<j} (E_2(tau_i) + E_2(tau_j)) * P_{ij}
                     / (4*pi^2)

    This is the genus-3 analogue of the genus-2 formula:
        C_3^{(2)} ~ alpha * (E_2(tau) + E_2(sigma)) * P_{12} / (4*pi^2)

    The three propagators P_{12}, P_{13}, P_{23} connect pairs of handles.

    Returns
    -------
    complex : approximate C_3^{(3)}(Omega)
    """
    Omega = validate_period_matrix_g3(Omega)
    P = genus3_propagator_matrix(Omega)

    E2 = np.array([
        _eisenstein_e2(Omega[i, i], N_terms) for i in range(3)
    ])

    alpha = float(K3_ALPHA)

    result = 0.0j
    for i in range(3):
        for j in range(i + 1, 3):
            result += (E2[i] + E2[j]) * P[i, j]

    return alpha * result / (4 * math.pi**2)


def genus3_cocycle_c4(
    Omega: np.ndarray,
    N_terms: int = 10,
) -> complex:
    r"""Genus-3 shadow cocycle C_4^{(3)}(Omega_3) from m_4.

    The quartic correction at genus 3.  In the separating degeneration:

        C_4^{(3)} ~ S_4 * sum_{i<j} (E_2(tau_i)^2 + E_2(tau_j)^2) * P_{ij}^2
                     / (16*pi^4)

    Returns
    -------
    complex : approximate C_4^{(3)}(Omega)
    """
    Omega = validate_period_matrix_g3(Omega)
    P = genus3_propagator_matrix(Omega)

    E2 = np.array([
        _eisenstein_e2(Omega[i, i], N_terms) for i in range(3)
    ])

    S4 = float(K3_S4)

    result = 0.0j
    for i in range(3):
        for j in range(i + 1, 3):
            result += (E2[i]**2 + E2[j]**2) * P[i, j]**2

    return S4 * result / (16 * math.pi**4)


def genus3_cocycle_ck(
    k: int,
    Omega: np.ndarray,
    N_terms: int = 10,
) -> complex:
    r"""Generic genus-3 shadow cocycle C_k^{(3)}(Omega) for the K3 sigma model.

    Dispatches to specialised functions for k=3,4 and uses the asymptotic
    formula for k >= 5.
    """
    if k == 3:
        return genus3_cocycle_c3(Omega, N_terms)
    if k == 4:
        return genus3_cocycle_c4(Omega, N_terms)

    Omega = validate_period_matrix_g3(Omega)
    P = genus3_propagator_matrix(Omega)

    E2 = np.array([
        _eisenstein_e2(Omega[i, i], N_terms) for i in range(3)
    ])

    tower = k3_shadow_tower(max_depth=k + 2)
    Sk = float(tower.get(k, Fraction(0)))

    # Asymptotic: higher cocycles with propagator power k-2
    result = 0.0j
    for i in range(3):
        for j in range(i + 1, 3):
            eis_product = (E2[i] + E2[j]) ** (k - 2)
            prop_power = P[i, j] ** (k - 2)
            result += eis_product * prop_power

    norm = (4 * math.pi**2) ** (k - 2)
    return Sk * result / norm


# =========================================================================
# 6. Shadow correction factor at genus 3
# =========================================================================

def shadow_correction_factor_g3(
    Omega: np.ndarray,
    max_depth: int = 8,
    N_terms: int = 10,
) -> Dict[str, Any]:
    r"""Compute the genus-3 shadow correction factor R_shadow^{(3)}(Omega).

    R_shadow^{(3)} = 1 + sum_{k=3}^{max_depth} S_k * C_k^{(3)}(Omega)

    For class M (K3 sigma model), this is Gevrey-1 divergent.

    Returns dict with R_shadow, individual cocycles, and convergence data.
    """
    Omega = validate_period_matrix_g3(Omega)
    tower = k3_shadow_tower(max_depth=max_depth + 2)

    cocycles = {}
    contributions = {}
    for k in range(3, max_depth + 1):
        Ck = genus3_cocycle_ck(k, Omega, N_terms)
        Sk = float(tower.get(k, Fraction(0)))
        cocycles[k] = Ck
        contributions[k] = Sk * Ck

    R_shadow = 1.0 + sum(contributions.values())

    # Partial sums
    partial_sums = {}
    running = 1.0
    for k in range(3, max_depth + 1):
        running += contributions[k]
        partial_sums[k] = running

    # Growth ratios
    growth_ratios = {}
    for k in range(4, max_depth + 1):
        if abs(contributions.get(k - 1, 0)) > 1e-30:
            growth_ratios[k] = abs(contributions[k]) / abs(contributions[k - 1])

    return {
        "R_shadow": R_shadow,
        "cocycles": cocycles,
        "contributions": contributions,
        "partial_sums": partial_sums,
        "growth_ratios": growth_ratios,
        "max_depth": max_depth,
        "shadow_tower": {k: float(tower.get(k, 0)) for k in range(2, max_depth + 1)},
        "is_gevrey_1": True,
        "shadow_class": "M",
        "genus": 3,
    }


# =========================================================================
# 7. W_{1+inf} genus-3 partition function (class M)
# =========================================================================

def genus3_partition_w1inf(
    Omega: np.ndarray,
    c: int = 1,
    max_shadow_depth: int = 4,
    N_terms: int = 8,
) -> Dict[str, Any]:
    r"""Genus-3 chiral partition function for W_{1+infty} at c=1 (class M).

    Z_3^{W}(Omega) = Z_3^{Heis}(Omega) * R_shadow^{(3)}(Omega)

    CLAIM STATUS: CONJECTURAL.  The corrections C_k^{(3)}(Omega) are
    computed in the separating degeneration limit, and their Sp_6(Z)
    modularity is part of the conjecture.

    Returns dict with partition function data and shadow corrections.
    """
    Omega = validate_period_matrix_g3(Omega)

    heis = genus3_partition_heisenberg(Omega, c=c, N_terms=N_terms)
    Z3_heis = heis["Z3_holomorphic"]

    # Shadow corrections
    C3 = genus3_cocycle_c3(Omega, N_terms=min(N_terms, 10))
    C4 = 0.0
    if max_shadow_depth >= 4:
        C4 = genus3_cocycle_c4(Omega, N_terms=min(N_terms, 10))

    R_shadow = 1.0 + SHADOW_TOWER_W1INF[3] * C3
    if max_shadow_depth >= 4:
        R_shadow += SHADOW_TOWER_W1INF[4] * C4

    Z3_W = Z3_heis * R_shadow

    det_Y = np.linalg.det(Omega.imag)
    Z3_full = abs(Z3_W) ** 2 / det_Y ** (c / 2.0)

    return {
        "Z3_holomorphic": Z3_W,
        "Z3_full": Z3_full,
        "Z3_heisenberg": Z3_heis,
        "R_shadow": R_shadow,
        "C3": C3,
        "C4": C4,
        "S3": SHADOW_TOWER_W1INF[3],
        "S4": SHADOW_TOWER_W1INF[4],
        "chi_18": heis["chi_18"],
        "chi_36": heis["chi_36"],
        "det_Im_Omega": det_Y,
        "central_charge": c,
        "weight_heisenberg": -c / 2.0,
        "shadow_class": "M",
        "max_shadow_depth": max_shadow_depth,
        "is_mock_modular": True,
        "genus": 3,
        "modular_group": "Sp_6(Z)",
        "explanation": (
            f"W_{{1+inf}} at c={c}, genus 3: Z_3 = Z_3^{{Heis}} * R_shadow. "
            f"Class M: infinite shadow tower, Gevrey-1 divergent. "
            f"Mock Siegel modular of weight {-c/2.0} for Sp_6(Z)."
        ),
    }


# =========================================================================
# 8. E_3 bar cohomology at genus 3
# =========================================================================

def e3_bar_genus3() -> Dict[str, Any]:
    r"""E_3 bar cohomology dimensions at genus 3 for all shadow classes.

    PROVED (e3_bar_higher_genus_class_m.py):

    Class G (Heisenberg):
      E_inf = P(q)^{3g} (formal power series, infinite-dimensional)

    Class L,C (Yangian, betagamma):
      E_inf = (1+t)^{3g} = (1+t)^9
      dim = 2^9 = 512

    Class M (Virasoro):
      E_inf = (3t(1+t))^g = (3t(1+t))^3
            = 27*t^3*(1+t)^3
            = 27*t^3*(1 + 3t + 3t^2 + t^3)
            = 27t^3 + 81t^4 + 81t^5 + 27t^6
      dim = 27 + 81 + 81 + 27 = 216 = 6^3

    At g=3: E_4 = E_inf UNCONDITIONALLY.
    Proof: E_4 supported in degrees {3,4,5,6}.  d_5 shifts by 4,
    mapping degree 6 to degree 2 (OUTSIDE support) and degree 7 to
    degree 3 (but degree 7 is empty).  So d_5 = 0 on E_4.
    Hence E_4 = E_5 = E_inf.

    Deficit: 2^9 - 6^3 = 512 - 216 = 296.
    This is the number of cohomology classes killed by d_4 at genus 3.
    """
    g = 3
    dim_class_LC = 2 ** (3 * g)   # = 512
    dim_class_M = 6 ** g           # = 216
    deficit = dim_class_LC - dim_class_M  # = 296

    # Poincare polynomial for class L,C: (1+t)^9
    poincare_LC = {}
    for n in range(3 * g + 1):
        val = math.comb(3 * g, n)
        if val > 0:
            poincare_LC[n] = val

    # Poincare polynomial for class M: (3t(1+t))^3 = 27t^3(1+t)^3
    poincare_M = {}
    for k in range(g + 1):
        n = g + k  # degree ranges from g to 2g
        poincare_M[n] = 3**g * math.comb(g, k)
    # Explicitly: {3: 27, 4: 81, 5: 81, 6: 27}

    return {
        "genus": g,
        "class_LC": {
            "dimension": dim_class_LC,
            "poincare": poincare_LC,
            "formula": "(1+t)^{3g} = (1+t)^9",
            "claim_status": "PROVED (Kunneth + charge conservation)",
        },
        "class_M": {
            "dimension": dim_class_M,
            "poincare": poincare_M,
            "formula": "(3t(1+t))^g = (3t(1+t))^3",
            "claim_status": "PROVED (e3_bar_higher_genus_class_m.py)",
        },
        "deficit": deficit,
        "E4_equals_Einf": True,
        "reason_E4_terminal": (
            "g=3: E_4 supported in degrees {3,4,5,6}. "
            "d_5 shifts by 4, mapping degree 6->2 and 7->3 "
            "(both outside support). So d_5 = 0, E_4 = E_inf."
        ),
        "AP_CY21_compliance": (
            "dim = 6^g = 216 for class M at g=3, "
            "NOT 8^g = 512 (that is class L,C). "
            "Deficit = 296."
        ),
    }


# =========================================================================
# 9. Schottky problem at genus 3
# =========================================================================

def schottky_genus3() -> Dict[str, Any]:
    r"""The Schottky problem at genus 3.

    At genus g, the moduli space M_g of curves has dimension 3g-3,
    and the Siegel modular variety A_g = Sp_{2g}(Z)\H_g has dimension
    g(g+1)/2.  The Torelli map j: M_g -> A_g sends a curve to its
    Jacobian (principally polarised abelian variety).

    The Schottky problem asks: which principally polarised abelian
    varieties are Jacobians?  I.e., what is the image j(M_g) = J_g?

    At genus 3:
      dim M_3 = 3*3 - 3 = 6
      dim A_3 = 3*4/2 = 6
      codim(J_3) = dim A_3 - dim M_3 = 0

    The Torelli map is DOMINANT at genus 3: every generic point of A_3
    is a Jacobian.  The Schottky problem is trivial.

    More precisely: the complement A_3 \ J_3 has codimension 1 in A_3
    (the hyperelliptic locus boundary), but J_3 is DENSE in A_3.
    Every Siegel modular form on A_3 is determined by its restriction
    to J_3 (analytic continuation).

    This is the LAST genus where Schottky is trivial:
      g=1: dim M_1 = 0, dim A_1 = 1, but j is an isomorphism.
      g=2: dim M_2 = 3, dim A_2 = 3, codim = 0. Torelli birational.
      g=3: dim M_3 = 6, dim A_3 = 6, codim = 0. Torelli dominant.
      g=4: dim M_4 = 9, dim A_4 = 10, codim = 1. NONTRIVIAL.
           The Schottky-Igusa form J in S_8(Sp_8(Z)) vanishes on J_4.

    Consequence for the chiral programme:
      At g <= 3, the shadow tower on M_g and Siegel modular forms on A_g
      live on spaces of the same dimension.  Obstruction (O4) from
      thm:shadow-siegel-gap is ABSENT.
      At g >= 4, (O4) is present: the shadow tower lives on a
      lower-dimensional space than A_g.

    GENUS-DIMENSION TABLE:
      g  | dim M_g | dim A_g | codim(J_g) | Schottky status
      1  |   0     |   1     |    ---     | Isomorphism
      2  |   3     |   3     |    0       | Birational
      3  |   6     |   6     |    0       | Dominant
      4  |   9     |  10     |    1       | Schottky-Igusa J
      5  |  12     |  15     |    3       | Nontrivial
    """
    g = 3
    dim_Mg = 3 * g - 3   # = 6
    dim_Ag = g * (g + 1) // 2  # = 6
    codim = dim_Ag - dim_Mg    # = 0

    # Table for comparison
    table = {}
    for gg in range(1, 11):
        dM = max(3 * gg - 3, 0) if gg >= 2 else 0
        dA = gg * (gg + 1) // 2
        cd = max(dA - dM, 0)
        table[gg] = {
            "dim_Mg": dM,
            "dim_Ag": dA,
            "codim_Jg": cd,
        }

    return {
        "genus": g,
        "dim_Mg": dim_Mg,
        "dim_Ag": dim_Ag,
        "codim_Jg": codim,
        "schottky_trivial": codim == 0,
        "torelli_dominant": True,
        "last_trivial_genus": 3,
        "first_nontrivial_genus": 4,
        "schottky_igusa_form": {
            "genus": 4,
            "weight": 8,
            "group": "Sp_8(Z)",
            "description": (
                "The Schottky-Igusa form J in S_8(Sp_8(Z)) is the UNIQUE "
                "cusp form of weight 8 vanishing exactly on the Jacobian "
                "locus J_4 in A_4."
            ),
        },
        "shadow_obstruction_O4": {
            "present_at_g3": False,
            "reason": (
                "codim(J_3) = 0: shadow tower on M_3 and Siegel modular "
                "forms on A_3 live on spaces of equal dimension. "
                "No Schottky obstruction at genus 3."
            ),
        },
        "genus_dimension_table": table,
        "claim_status": "PROVED (classical: Torelli theorem, Riemann, Schottky)",
    }


# =========================================================================
# 10. K3 x E at genus 3 (CONJECTURAL)
# =========================================================================

def genus3_partition_k3xe(
    Omega: np.ndarray,
    max_shadow_depth: int = 6,
    N_terms: int = 8,
) -> Dict[str, Any]:
    r"""Genus-3 chiral partition function for K3 x E.

    CLAIM STATUS: CONJECTURAL. Conditional on CY-A_3 for the existence
    of the chiral algebra A_{K3xE} (AP-CY6/14).

    The formula:
      Z_3^{K3xE}(Omega) = Z_3^{Heis,c=24}(Omega) * R_shadow^{K3,(3)}(Omega)

    where:
      Z_3^{Heis,c=24} = chi_{18}^{-24/36} = chi_{18}^{-2/3}
      R_shadow^{K3,(3)} = 1 + sum_{k>=3} S_k^{K3} * C_k^{(3)}(Omega)

    UNLIKE genus 2, there is NO single DMVV-target Siegel modular form.
    The genus-3 analogue of the DMVV formula involves multiple Siegel
    modular forms on Sp_6(Z).  The simple 1/Phi_10 story does not
    generalise directly.

    Weight: -c/2 = -12 for c=24.

    Sp_6(Z) transformation: mock Siegel modular of weight -12
    (the shadow corrections break true modularity).

    The Schottky obstruction (O4) is ABSENT at g=3 (codim J_3 = 0).

    Parameters
    ----------
    Omega : 3x3 period matrix in H_3
    max_shadow_depth : int
        Maximum depth of shadow tower (3 through 8).
    N_terms : int
        Lattice summation range.
    """
    Omega = validate_period_matrix_g3(Omega)

    # Base: Heisenberg at c=24
    heis = genus3_partition_heisenberg(Omega, c=K3E_CENTRAL_CHARGE, N_terms=N_terms)
    Z3_heis = heis["Z3_holomorphic"]
    c18 = heis["chi_18"]

    # Shadow correction
    shadow_data = shadow_correction_factor_g3(
        Omega, max_shadow_depth, N_terms=min(N_terms, 10))
    R_shadow = shadow_data["R_shadow"]

    Z3_k3e = Z3_heis * R_shadow

    det_Y = np.linalg.det(Omega.imag)
    Z3_full = abs(Z3_k3e) ** 2 / det_Y ** (K3E_CENTRAL_CHARGE / 2.0)

    return {
        # Partition functions
        "Z3_k3e": Z3_k3e,
        "Z3_heisenberg_c24": Z3_heis,
        "Z3_full": Z3_full,
        # Shadow data
        "R_shadow": R_shadow,
        "shadow_data": shadow_data,
        "max_shadow_depth": max_shadow_depth,
        # Theta product
        "chi_18": c18,
        "chi_36": c18**2 if abs(c18) < float('inf') else float('inf'),
        "det_Im_Omega": det_Y,
        # Kappa spectrum (AP113)
        "kappa_ch": float(K3E_KAPPA_CH),
        "kappa_cat": float(K3E_KAPPA_CAT),
        "kappa_cat_fiber": float(K3E_KAPPA_CAT_FIBER),
        "kappa_BKM": float(K3E_KAPPA_BKM),
        "kappa_fiber": float(K3E_KAPPA_FIBER),
        # Weights
        "weight_Z3_heis": -K3E_CENTRAL_CHARGE / 2.0,  # -12
        "weight_Z3_k3e": -K3E_CENTRAL_CHARGE / 2.0,   # -12 (mock)
        # Classification
        "central_charge": K3E_CENTRAL_CHARGE,
        "shadow_class": "M",
        "is_mock_modular": True,
        "genus": 3,
        "modular_group": "Sp_6(Z)",
        # Schottky
        "schottky_obstruction_absent": True,
        "schottky_codim": 0,
        # No DMVV target at genus 3
        "dmvv_target_exists": False,
        "dmvv_note": (
            "Unlike genus 2 (where Z_2^{DMVV} = 1/Phi_10), there is no "
            "single DMVV-target Siegel modular form at genus 3. The "
            "genus-3 DMVV answer involves multiple Siegel modular forms."
        ),
        "claim_status": (
            "CONJECTURAL (conditional on CY-A_3 for A_{K3xE}). "
            "Shadow tower data PROVED at d=2. "
            "Schottky obstruction (O4) absent at g=3."
        ),
    }


# =========================================================================
# 11. Sp_6(Z) modularity verification
# =========================================================================

def verify_sp6_modularity_chi18(
    Omega: np.ndarray,
    N_terms: int = 6,
    tol: float = 1e-3,
) -> Dict[str, Any]:
    r"""Verify Sp_6(Z) transformation of chi_{18} under T-generators.

    chi_{18} has weight 18 on Sp_6(Z) with theta multiplier system chi.

    Under T_{ii} (tau_i -> tau_i + 1):
        chi_{18}(Omega + e_{ii}) = chi_mult * chi_{18}(Omega)

    where chi_mult is the theta multiplier (a root of unity).

    chi_{36} = chi_{18}^2 has TRIVIAL multiplier:
        chi_{36}(Omega + e_{ij}) = chi_{36}(Omega)

    NOTE: Sp_6 quotient by +/-I_6 (6x6), NOT +/-I_7 (AP-CY16).
    """
    Omega = validate_period_matrix_g3(Omega)
    c18_orig = chi18_genus3(Omega, N_terms)
    c36_orig = c18_orig ** 2

    results = {}

    # Test diagonal T-translations
    for idx in range(3):
        shift = np.zeros((3, 3), dtype=complex)
        shift[idx, idx] = 1.0
        Omega_new = Omega + shift
        c18_new = chi18_genus3(Omega_new, N_terms)
        c36_new = c18_new ** 2

        # chi_{18} may pick up a sign or root of unity
        if abs(c18_orig) > 1e-300:
            ratio_18 = c18_new / c18_orig
        else:
            ratio_18 = float('inf')

        # chi_{36} should be invariant
        if abs(c36_orig) > 1e-300:
            ratio_36 = c36_new / c36_orig
        else:
            ratio_36 = float('inf')

        results[f"T{idx+1}{idx+1}"] = {
            "chi18_ratio": ratio_18,
            "chi36_ratio": ratio_36,
            "chi36_invariant": (
                abs(ratio_36 - 1.0) < tol
                if np.isfinite(ratio_36) else False
            ),
        }

    # Test off-diagonal T-translations
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        shift = np.zeros((3, 3), dtype=complex)
        shift[i, j] = 1.0
        shift[j, i] = 1.0
        Omega_new = Omega + shift
        c18_new = chi18_genus3(Omega_new, N_terms)
        c36_new = c18_new ** 2

        if abs(c18_orig) > 1e-300:
            ratio_18 = c18_new / c18_orig
        else:
            ratio_18 = float('inf')

        if abs(c36_orig) > 1e-300:
            ratio_36 = c36_new / c36_orig
        else:
            ratio_36 = float('inf')

        results[f"T{i+1}{j+1}"] = {
            "chi18_ratio": ratio_18,
            "chi36_ratio": ratio_36,
            "chi36_invariant": (
                abs(ratio_36 - 1.0) < tol
                if np.isfinite(ratio_36) else False
            ),
        }

    chi36_all_pass = all(
        r["chi36_invariant"] for r in results.values()
    )

    return {
        "generator_tests": results,
        "chi36_all_pass": chi36_all_pass,
        "weight_chi18": 18,
        "weight_chi36": 36,
        "group": "Sp_6(Z) / +/-I_6",
        "n_generators_tested": len(results),
    }


# =========================================================================
# 12. Weight table and summary
# =========================================================================

def genus3_weight_table() -> Dict[str, Any]:
    r"""Weight table for genus-3 Siegel modular forms.

    Collects all modular weights, kappa values, and representations.

    KEY DIFFERENCE from genus 2:
      At genus 2, there is a UNIQUE cusp form Phi_10 of weight 10.
      At genus 3, the ring of Siegel modular forms is richer:
        - chi_{12}: Siegel cusp form of weight 12 (Tsuyumine).
          This is the first nonzero cusp form for Sp_6(Z).
        - chi_{18}: product of 36 even thetas, weight 18.
        - chi_{36} = chi_{18}^2: weight 36, trivial multiplier.

    The genus-3 ring of Siegel modular forms M_*(Sp_6(Z)) is generated
    by forms of weights 4, 6, 10, 12, 14, 16, 18 (Tsuyumine).
    The first CUSP form has weight 12 (chi_{12}, unique up to scalar).
    """
    return {
        "siegel_modular_forms_genus3": {
            "chi_12": {
                "weight": 12,
                "description": (
                    "First Siegel cusp form for Sp_6(Z). "
                    "Unique up to scalar. Tsuyumine (1986)."
                ),
                "analogue_genus2": "Phi_10 (weight 10)",
            },
            "chi_18": {
                "weight": 18,
                "description": (
                    "Product of 36 even genus-3 theta constants. "
                    "Has theta multiplier system. Weight = 36/2 = 18."
                ),
                "analogue_genus2": "Delta_5 (weight 5)",
            },
            "chi_36": {
                "weight": 36,
                "description": (
                    "chi_{18}^2. Trivial multiplier. "
                    "Analogue of Phi_10 = Delta_5^2."
                ),
                "analogue_genus2": "Phi_10 (weight 10)",
            },
        },
        "heisenberg_weights": {
            "c1": {"weight": -0.5, "formula": "chi_{18}^{-1/36}",
                    "group": "Mp_6(Z)"},
            "c24": {"weight": -12, "formula": "chi_{18}^{-2/3}",
                     "group": "Sp_6(Z)"},
        },
        "kappa_spectrum_k3xe": {
            "kappa_ch": {"value": 3, "status": "PROVED (additivity at d=2)"},
            "kappa_cat": {"value": 0, "status": "PROVED (Kunneth)"},
            "kappa_cat_fiber": {"value": 2, "status": "PROVED (classical)"},
            "kappa_BKM": {"value": 5, "status": "PROVED (Borcherds)"},
            "kappa_fiber": {"value": 24, "status": "PROVED (classical)"},
        },
        "weight_formula": (
            "wt(F_g^{Heis}) = -c/2 (genus-independent). "
            "At g=3: wt(chi_{18}^{-c/36}) = 18 * (-c/36) = -c/2."
        ),
        "genus_weight_comparison": {
            "g=1": {"theta_product_weight": 0.5, "n_even": 3,
                     "notes": "eta is related but different normalisation"},
            "g=2": {"theta_product_weight": 5, "n_even": 10,
                     "notes": "Delta_5 = prod of 10 even thetas"},
            "g=3": {"theta_product_weight": 18, "n_even": 36,
                     "notes": "chi_{18} = prod of 36 even thetas"},
        },
        "e3_bar_genus3": e3_bar_genus3(),
        "schottky": schottky_genus3(),
    }


def genus3_full_summary(
    Omega: np.ndarray,
    max_shadow_depth: int = 6,
    N_terms: int = 8,
) -> Dict[str, Any]:
    r"""Complete summary of the genus-3 computation.

    Combines: Heisenberg, W_{1+inf}, K3xE, E_3 bar, Schottky,
    Sp_6(Z) modularity, weight table.
    """
    heis = genus3_partition_heisenberg(Omega, c=1, N_terms=N_terms)
    w1inf = genus3_partition_w1inf(Omega, c=1, max_shadow_depth=min(max_shadow_depth, 4), N_terms=N_terms)
    k3xe = genus3_partition_k3xe(Omega, max_shadow_depth, N_terms)
    e3_bar = e3_bar_genus3()
    schottky = schottky_genus3()
    weights = genus3_weight_table()
    modularity = verify_sp6_modularity_chi18(Omega, N_terms=min(N_terms, 6))

    return {
        "heisenberg_c1": heis,
        "w1inf_c1": w1inf,
        "k3xe": k3xe,
        "e3_bar": e3_bar,
        "schottky": schottky,
        "weight_table": weights,
        "modularity": modularity,
        "genus": 3,
        "modular_group": "Sp_6(Z)",
        "siegel_dim": 6,
        "n_even_theta": 36,
        "n_odd_theta": 28,
    }
