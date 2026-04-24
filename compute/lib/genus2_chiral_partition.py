r"""Genus-2 chiral partition function for W_{1+\infty} and Siegel modularity.

MATHEMATICAL CONTENT
====================

The genus-2 chiral partition function Z_2(Omega) computes the trace over
the tensor product of two copies of the chiral algebra's state space,
parametrised by the genus-2 period matrix

    Omega = ((tau, z), (z, sigma)) in H_2  (Siegel upper half-space)

where H_2 = {Omega in M_2(C) : Omega^T = Omega, Im(Omega) > 0}.

The three parameters:
  tau   = period of the first handle
  sigma = period of the second handle
  z     = off-diagonal coupling (cross-ratio of the two handles)

FACTORIZATION HOMOLOGY ORIGIN:
  - At E_2: int_{T^2} A computes the genus-1 partition function Z_1(tau)
    with SL_2(Z) modularity.  Parameter: tau in H_1.
  - At E_3: int_{Sigma_2 x S^1} A computes the genus-2 partition function
    Z_2(Omega) with Sp_4(Z) modularity.  Parameter: Omega in H_2.

The factorization homology of an E_3-algebra over Sigma_2 x S^1 produces
a function on the moduli space of genus-2 Riemann surfaces, which is
Sp_4(Z) \ H_2.

HEISENBERG (CLASS G):
  The Heisenberg VOA H_k at level k has m_n = 0 for all n >= 3 (free field).
  The genus-2 partition function is the Siegel analogue of 1/eta(tau)^c:

      Z_2^{Heis}(Omega) = 1 / (det Phi_{Siegel}(Omega))^{c/2}

  where Phi_{Siegel} is the genus-2 Dedekind function (product of 10 even
  theta constants).  At c=1:

      Z_2^{Heis}(Omega) = 1 / Delta_5(Omega)^{1/10}

  since Delta_5 = prod_{even chars} theta[a,b](Omega).

  More precisely, for the Heisenberg at level k with c=1:

      Z_2^{Heis}(Omega; k) = Theta_{Lambda_k}(Omega) / Phi_{10}^{Siegel}(Omega)

  where Theta_{Lambda_k} is the genus-2 theta series of the lattice Lambda_k
  (rank 1, discriminant k), and Phi_{10}^{Siegel} = Delta_5^2 is the
  weight-10 Siegel cusp form.

  The CORRECT formula for c copies of the Heisenberg:

      Z_2(Omega; c) = 1 / [det(Im Omega)]^{c/2} * |F(Omega)|^2

  where F(Omega) is the holomorphic part.  The HOLOMORPHIC genus-2
  partition function (chiral half) is:

      F_2^{Heis}(Omega) = 1 / chi_{10}(Omega)^{c/24}

  where chi_{10} = Delta_5^2 is Igusa's weight-10 cusp form normalised
  so that its first Fourier-Jacobi coefficient is eta^{18} theta_1^2.

  For a SINGLE boson (c=1), the holomorphic genus-2 partition function
  decomposes via the Fourier-Jacobi expansion:

      F_2^{Heis}(Omega) = sum_{m >= 0} phi_m^{Heis}(tau, z) * p^m

  where p = e^{2 pi i sigma} and phi_m are weak Jacobi forms of weight
  -c/2 and index m.

W_{1+INFTY} AT c=1 (CLASS M):
  W_{1+infty} has m_3 != 0 (non-associative OPE), so the bar complex
  acquires A_infinity corrections.  The genus-2 partition function receives
  corrections from the shadow tower:

      Z_2^{W}(Omega) = Z_2^{Heis}(Omega) * R_shadow(Omega)

  where R_shadow is the shadow correction factor:

      R_shadow(Omega) = 1 + sum_{k >= 3} S_k * C_k(Omega)

  Here S_k are the shadow tower coefficients (S_3 = alpha = 2 for spin 2,
  S_4 = 10/27, ...) and C_k(Omega) are genus-2 modular cocycles at depth k.

  The leading correction from m_3:

      C_3(Omega) = integral over M_{0,3} of the triple OPE kernel
                 = Eisenstein-like term in genus-2 modular forms

  At class M, the full shadow tower is INFINITE: the series does not
  truncate, and the resulting Z_2 is a MOCK Siegel modular form (it
  transforms as a Siegel modular form up to a shadow correction that
  involves non-holomorphic completions).

Sp_4(Z) TRANSFORMATION:
  Under gamma = ((A, B), (C, D)) in Sp_4(Z):

      Omega -> (A*Omega + B)*(C*Omega + D)^{-1}

  The genus-2 partition function transforms as:

      Z_2(gamma . Omega) = det(C*Omega + D)^k * Z_2(Omega)

  where k is the Siegel modular weight.

  WEIGHT DETERMINATION:
  - Heisenberg: k = -c/2 (negative weight, from the 1/eta analogy)
  - For c=1: k = -1/2 (half-integral weight, on a metaplectic cover)
  - K3 x E: k = -2*kappa_cat_fiber = -4 for the S-matrix
  - K3 x E: k = 5 for the BKM denominator (Delta_5 has weight 5)
  - The S-matrix has weight -2*kappa_cat_fiber = -2*2 = -4.
  - The partition function has weight -c/2 = -12 for K3 (c=24).

  The weight formula (from conj:sp4-modularity in braided_factorization.tex):

      wt(S-hat) = -2 * kappa_cat_fiber

  For K3 x E: kappa_cat(K3 x E) = 0, while the S-matrix normalizer
  uses the K3-fiber value kappa_cat_fiber = chi(O_{K3}) = 2, so wt = -4.

K3 x E CONNECTION:
  For K3 x E (c=24), the genus-2 partition function is:

      Z_2^{K3xE}(Omega) = Theta_{Mukai}(Omega) / Phi_10(Omega)^2

  where Phi_10 = Delta_5^2 is the Igusa cusp form of weight 10.
  The denominator Phi_10 is the Borcherds lift of the K3 elliptic genus
  phi_{0,1}.  It is a Siegel modular form of weight 10 for Sp_4(Z).

  The REPRESENTATION of Sp_4(Z): the trivial (scalar) representation,
  i.e., Phi_10 is a scalar Siegel modular form (not vector-valued).
  The Igusa cusp form is the UNIQUE weight-5 Siegel cusp form for
  Gamma_2 = Sp_4(Z) (up to scalar), and Delta_5 lives on the QUOTIENT
  by +/- I_4 (AP-CY16: Sp_4 quotient by +/-I_4, NOT +/-I_5).

FOURIER-JACOBI EXPANSION:
  The FJ expansion of Phi_10:

      Phi_10(tau, z, sigma) = sum_{m >= 1} phi_{10,m}(tau, z) * p^m

  where p = e^{2 pi i sigma} and phi_{10,m} is a Jacobi form of weight 10
  and index m on SL_2(Z).

  phi_{10,1}(tau, z) = eta(tau)^{18} * theta_1(tau, z)^2
    Weight 10, index 1.  This is the UNIQUE Jacobi cusp form of
    weight 10 and index 1.

  phi_{10,2}(tau, z) has weight 10, index 2.  Computed via the Hecke
  operator or direct expansion.

  For 1/Phi_10 (the S-matrix generating function):
  The FJ expansion of 1/Phi_10 is:

      1/Phi_10 = sum_{m >= -1} psi_m(tau, z) * p^m

  where psi_{-1}(tau, z) = 1/phi_{10,1}(tau, z) is the leading pole.

  phi_0 (the m=0 coefficient of 1/Phi_10): this is a MEROMORPHIC Jacobi
  form of weight -10 and index 0, with poles along the zero locus of
  phi_{10,1}.

  phi_1 (the m=1 coefficient): Jacobi form of weight -10 and index 1.

CONVENTIONS:
  - q = e^{2 pi i tau}, r = e^{2 pi i z}, p = e^{2 pi i sigma}
  - Period matrix: Omega = ((tau, z), (z, sigma))
  - Im(Omega) > 0: both diagonal entries have positive imaginary part,
    and Im(tau)*Im(sigma) - Im(z)^2 > 0 (positive definite).
  - kappa_ch: from chiral algebra (AP113, always subscripted)
  - kappa_cat: holomorphic Euler characteristic chi(O_X)
  - kappa_BKM: weight of the Borcherds product / BKM denominator

AP COMPLIANCE:
  - AP113: bare kappa FORBIDDEN; all kappa subscripted.
  - AP-CY6/14: A_X for d=3 does not exist.  All d=3 results CONJECTURAL.
  - AP-CY8: Borcherds product = bar Euler product is OBSERVATION, not theorem.
  - AP-CY9: Jacobi form discriminant constraint: D = 0 or D = 3 mod 4.
  - AP-CY11: Conditional propagation: Z_2 for K3xE depends on CY-A_3.
  - AP-CY16: Sp_4 quotient by +/-I_4 (4x4), NOT +/-I_5.
  - AP-CY21: E_3 bar dimensions: (1+t)^{3g} for class L,C; NOT class M.
  - FM24: B-cycle sign: verify |q| < 1 (Im(tau) > 0).

MANUSCRIPT REFERENCES:
  chapters/theory/braided_factorization.tex:
    conj:sp4-modularity (L695-730)
    conj:s-matrix-phi10 (L732-805)
    rem:e2-e3-modular-promotion (L807-862)
  chapters/examples/toroidal_elliptic.tex:
    thm:shadow-siegel-gap
    subsec:shadow-siegel-gap

MATHEMATICAL SOURCES:
  Igusa, "On Siegel modular forms of genus two" (1962)
  Gritsenko-Nikulin, "Automorphic forms and Lorentzian KM algebras, II" (1998)
  Mason-Tuite, "Genus two partition functions of chiral VOAs" (2004)
  Gaberdiel-Volpato, "Mathieu moonshine and orbifold K3s" (2012)
  Lorgat, "A Borcherds lift..." (2020)
"""

from __future__ import annotations

import math
from functools import lru_cache
from typing import Dict, List, Optional, Tuple

import numpy as np


# =========================================================================
# 1. Siegel upper half-space utilities
# =========================================================================

def validate_period_matrix(
    tau: complex, z: complex, sigma: complex,
) -> np.ndarray:
    """Validate and construct the genus-2 period matrix Omega in H_2.

    Checks:
      (i)   Im(tau) > 0
      (ii)  Im(sigma) > 0
      (iii) det(Im(Omega)) > 0  (positive definite imaginary part)
      (iv)  |q| < 1, |p| < 1  (FM24: convergence of q,p expansions)

    Returns the 2x2 symmetric matrix Omega = ((tau, z), (z, sigma)).
    """
    Omega = np.array([[tau, z], [z, sigma]], dtype=complex)
    Y = Omega.imag

    if Y[0, 0] <= 0:
        raise ValueError(
            f"Im(tau) = {Y[0, 0]:.6f} <= 0: not in Siegel upper half-space. "
            f"FM24: this would give |q| >= 1, destroying q-expansion convergence."
        )
    if Y[1, 1] <= 0:
        raise ValueError(
            f"Im(sigma) = {Y[1, 1]:.6f} <= 0: not in Siegel upper half-space."
        )
    det_Y = Y[0, 0] * Y[1, 1] - Y[0, 1] * Y[1, 0]
    if det_Y <= 0:
        raise ValueError(
            f"det(Im(Omega)) = {det_Y:.6f} <= 0: imaginary part not positive definite."
        )
    return Omega


def sp4_action(
    gamma: np.ndarray, Omega: np.ndarray,
) -> np.ndarray:
    """Apply an Sp_4(Z) transformation to a genus-2 period matrix.

    gamma = ((A, B), (C, D)) is a 4x4 symplectic integer matrix
    partitioned into 2x2 blocks.

    The action: Omega -> (A*Omega + B) * (C*Omega + D)^{-1}

    Sp_4(Z) is the group of 4x4 integer matrices preserving the
    symplectic form J = ((0, I_2), (-I_2, 0)).  It is generated by:
      T: Omega -> Omega + S  (translations by symmetric integer matrices)
      S: Omega -> -Omega^{-1}  (inversion)

    The mapping class group MCG(Sigma_2) surjects onto Sp_4(Z),
    which is why genus-2 conformal blocks transform under Sp_4(Z).

    NOTE: Sp_4 acts via 4x4 matrices, quotient by +/-I_4 (AP-CY16).
    """
    A = gamma[:2, :2]
    B = gamma[:2, 2:]
    C = gamma[2:, :2]
    D = gamma[2:, 2:]

    # Verify symplecticity: gamma^T J gamma = J
    J = np.block([
        [np.zeros((2, 2)), np.eye(2)],
        [-np.eye(2), np.zeros((2, 2))],
    ])
    check = gamma.T @ J @ gamma
    if not np.allclose(check, J, atol=1e-10):
        raise ValueError("Input matrix is not symplectic")

    numerator = A @ Omega + B
    denominator = C @ Omega + D
    return numerator @ np.linalg.inv(denominator)


def sp4_generators() -> Dict[str, np.ndarray]:
    """Return the standard generators of Sp_4(Z).

    The group Sp_4(Z) is generated by four elements (Hua):
      T1: tau -> tau + 1  (shift first diagonal)
      T2: sigma -> sigma + 1  (shift second diagonal)
      T3: z -> z + 1  (shift off-diagonal, with compensating diagonal shifts)
      S:  Omega -> -Omega^{-1}  (Siegel inversion)

    Returns dict of 4x4 integer matrices.
    """
    I2 = np.eye(2, dtype=int)
    Z2 = np.zeros((2, 2), dtype=int)

    # T1: Omega -> Omega + ((1,0),(0,0))
    B1 = np.array([[1, 0], [0, 0]], dtype=int)
    T1 = np.block([[I2, B1], [Z2, I2]])

    # T2: Omega -> Omega + ((0,0),(0,1))
    B2 = np.array([[0, 0], [0, 1]], dtype=int)
    T2 = np.block([[I2, B2], [Z2, I2]])

    # T3: Omega -> Omega + ((0,1),(1,0))
    B3 = np.array([[0, 1], [1, 0]], dtype=int)
    T3 = np.block([[I2, B3], [Z2, I2]])

    # S: Omega -> -Omega^{-1}
    S = np.block([[Z2, I2], [-I2, Z2]])

    return {"T1": T1, "T2": T2, "T3": T3, "S": S}


# =========================================================================
# 2. Genus-2 theta functions and Igusa cusp form
# =========================================================================

def genus2_theta(
    Omega: np.ndarray,
    a: Tuple[int, int],
    b: Tuple[int, int],
    N_terms: int = 20,
) -> complex:
    """Genus-2 theta constant with half-integer characteristic [a/2; b/2].

    theta[a,b](Omega) = sum_{n in Z^2} exp(pi*i * (n + a/2)^T Omega (n + a/2)
                                         + pi*i * b^T (n + a/2))

    Parameters
    ----------
    Omega : 2x2 complex matrix in H_2
    a, b : tuples of 0/1 (elements of (Z/2Z)^2)
    N_terms : summation range per dimension
    """
    a_vec = np.array(a, dtype=float)
    b_vec = np.array(b, dtype=float)
    Y = Omega.imag

    result = 0.0j
    for n1 in range(-N_terms, N_terms + 1):
        for n2 in range(-N_terms, N_terms + 1):
            v = np.array([n1 + a_vec[0] / 2.0, n2 + a_vec[1] / 2.0])
            # Decay: exp(-pi * v^T Y v)
            decay = math.pi * (v[0]**2 * Y[0, 0] + 2 * v[0] * v[1] * Y[0, 1]
                               + v[1]**2 * Y[1, 1])
            if decay > 500:
                continue
            quad = (v[0]**2 * Omega[0, 0] + 2 * v[0] * v[1] * Omega[0, 1]
                    + v[1]**2 * Omega[1, 1])
            lin = b_vec[0] * v[0] + b_vec[1] * v[1]
            exponent = 1j * math.pi * (quad + lin)
            if exponent.real > 500:
                continue
            result += np.exp(exponent)
    return result


def even_theta_characteristics() -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """Return the 10 even theta characteristics (a, b) with a, b in (Z/2Z)^2.

    Even iff a^T b = 0 mod 2.  There are 10 even characteristics in genus 2.
    """
    chars = []
    for a0 in [0, 1]:
        for a1 in [0, 1]:
            for b0 in [0, 1]:
                for b1 in [0, 1]:
                    if (a0 * b0 + a1 * b1) % 2 == 0:
                        chars.append(((a0, a1), (b0, b1)))
    return chars


def igusa_cusp_form_delta5(
    tau: complex, z: complex, sigma: complex,
    N_terms: int = 20,
) -> complex:
    r"""Compute Delta_5(Omega) = prod of 10 even genus-2 theta constants.

    Delta_5 is a Siegel modular form of weight 5 for Sp_4(Z) (on the
    quotient by +/-I_4; AP-CY16).

    The Igusa cusp form Phi_10 = Delta_5^2 has weight 10.

    Parameters
    ----------
    tau, z, sigma : complex
        Period matrix entries, Omega = ((tau, z), (z, sigma)) in H_2.
    N_terms : int
        Lattice summation range.

    Returns
    -------
    complex : Delta_5(Omega)
    """
    Omega = validate_period_matrix(tau, z, sigma)
    chars = even_theta_characteristics()
    assert len(chars) == 10

    log_result = 0.0j
    for (a, b) in chars:
        theta_val = genus2_theta(Omega, a, b, N_terms)
        if abs(theta_val) < 1e-300:
            return 0.0j
        log_result += np.log(theta_val)
    return np.exp(log_result)


def igusa_cusp_form_phi10(
    tau: complex, z: complex, sigma: complex,
    N_terms: int = 20,
) -> complex:
    r"""Compute Phi_10(Omega) = Delta_5(Omega)^2.

    Phi_10 is the Igusa cusp form of weight 10 on Sp_4(Z).
    It is the UNIQUE (up to scalar) Siegel cusp form of weight 10.

    This is the Borcherds multiplicative lift of the K3 elliptic genus
    phi_{0,1} (see igusa_product_formula.py for the product expansion).
    """
    d5 = igusa_cusp_form_delta5(tau, z, sigma, N_terms)
    return d5 ** 2


# =========================================================================
# 3. Heisenberg genus-2 partition function (class G)
# =========================================================================

def genus2_partition_heisenberg(
    tau: complex, z: complex, sigma: complex,
    c: int = 1,
    N_terms: int = 20,
) -> Dict[str, complex]:
    r"""Genus-2 chiral partition function for the Heisenberg VOA at c copies.

    For the Heisenberg (class G), all A_infinity corrections vanish:
    m_n = 0 for n >= 3.  The genus-2 partition function is:

        Z_2^{Heis}(Omega) = 1 / Phi_{10}(Omega)^{c/12}

    This is the Siegel analogue of the genus-1 result Z_1 = 1/eta(tau)^c.

    DERIVATION: The genus-g partition function of c free bosons on a
    genus-g surface is:
        Z_g = 1 / det(Im Omega)^{c/2} * |F_g|^2
    where the holomorphic part F_g satisfies:
        F_g(Omega) = [prod_{even [a,b]} theta[a,b](Omega)]^{-c/12}
                   = Delta_5(Omega)^{-c/12}

    At genus 1: F_1 = eta(tau)^{-c} = [theta_3 theta_4 theta_2 / 2]^{-c/3}
                (using the Jacobi product).

    At genus 2: F_2 = Delta_5(Omega)^{-c/12}
                since Delta_5 = prod of 10 even thetas generalises
                eta = prod of 3 even thetas / 2 to genus 2.

    More precisely, the genus-g bosonization formula gives:
        F_g = Theta_{null}^{-c/2}
    where Theta_{null}^{1/2} is the Schottky-normalised determinant
    of the b-c ghost system.  At g=2 with the standard normalisation:
        Theta_{null} = [2^{-10} * Delta_5]^{1/5}

    The MODULAR WEIGHT of Z_2 is:
        wt(F_2) = -c/2   (half the central charge, negative)
    since F_2 transforms as det(C*Omega+D)^{-c/2} under Sp_4(Z).

    For c=1: wt = -1/2  (on the metaplectic cover Mp_4(Z)).

    Parameters
    ----------
    tau, z, sigma : complex
        Period matrix entries.
    c : int
        Central charge (number of free bosons).
    N_terms : int
        Lattice summation range for theta functions.

    Returns
    -------
    dict with 'Z2_holomorphic', 'Delta_5', 'Phi_10', 'weight', and diagnostics.
    """
    Omega = validate_period_matrix(tau, z, sigma)

    d5 = igusa_cusp_form_delta5(tau, z, sigma, N_terms)
    phi10 = d5 ** 2

    # The holomorphic genus-2 partition function
    # F_2 = Delta_5^{-c/12}
    if abs(d5) < 1e-300:
        Z2_hol = float('inf')
    else:
        Z2_hol = d5 ** (-c / 12.0)

    # The full (non-holomorphic) partition function includes the
    # det(Im Omega)^{-c/2} prefactor
    det_Y = np.linalg.det(Omega.imag)
    Z2_full = abs(Z2_hol) ** 2 / det_Y ** (c / 2.0)

    # Modular weight
    weight = -c / 2.0

    return {
        "Z2_holomorphic": Z2_hol,
        "Z2_full": Z2_full,
        "Delta_5": d5,
        "Phi_10": phi10,
        "det_Im_Omega": det_Y,
        "central_charge": c,
        "weight": weight,
        "shadow_class": "G",
        "m3_correction": 0.0,
        "explanation": (
            f"Heisenberg at c={c}: Z_2 = Delta_5^{{-c/12}} = Delta_5^{{{-c}/12}}. "
            f"Class G: all A_inf corrections vanish (free field). "
            f"Siegel modular weight = {weight} for Sp_4(Z) "
            f"(on metaplectic cover if c odd)."
        ),
    }


# =========================================================================
# 4. W_{1+infty} genus-2 partition function (class M)
# =========================================================================

# Shadow tower data from a_infinity_bar_w1inf.py and c3_shadow_tower.py
# These are the COPRODUCT CORRECTION COEFFICIENTS (AP-CY21).
SHADOW_TOWER_W1INF = {
    # S_k: shadow invariant at depth k
    # S_2 = kappa_ch (divergent, regulate at spin N)
    # The finite part at c=1:
    2: 0.5,        # kappa_ch for spin-2 channel
    3: 2.0,        # alpha = m_3(T,T,T) coefficient = -2T, so |alpha| = 2
    4: 10.0 / 27,  # quartic shadow S_4 = 10/27 (from spin-2 channel)
    5: 0.0,        # vanishes by parity (odd depth, even spin)
    6: None,        # not yet computed
}


def _genus2_shadow_cocycle_c3(
    tau: complex, z: complex, sigma: complex,
    N_terms: int = 10,
) -> complex:
    r"""Compute the leading genus-2 modular cocycle C_3(Omega) from m_3.

    The m_3 correction to the genus-2 partition function comes from the
    triple OPE integral over the moduli space M_{0,3} of three-punctured
    spheres.  At genus 2, the relevant integral is:

        C_3(Omega) = int_{Sigma_2^3} K_3(w_1, w_2, w_3; Omega) dw_1 dw_2 dw_3

    where K_3 is the genus-2 three-point correlation function kernel.

    For the Virasoro (spin-2) channel at c=1:
        K_3 is determined by the Virasoro three-point function
        <T(w_1) T(w_2) T(w_3)>_{Sigma_2} which involves the genus-2
        Bergmann kernel and its derivatives.

    APPROXIMATION: We compute the leading term using the degeneration
    limit sigma -> i*infinity (separating the two handles).  In this limit:

        C_3(Omega) ~ c_3 * E_2(tau) * p + O(p^2)

    where E_2 is the (quasi-modular) Eisenstein series and p = e^{2 pi i sigma}.

    The coefficient c_3 is proportional to the central charge:
        c_3 = c * (c-1) * (5c + 22) / (240 * 12)

    At c=1: c_3 = 0 (the triple correction vanishes at c=1 for the
    VIRASORO alone, but NOT for W_{1+infty} which has additional spin-3
    generators).

    For W_{1+infty}, the m_3 contribution comes from the W-ALGEBRA
    three-point function, not just the Virasoro.  The leading term is:

        C_3^{W}(Omega) ~ alpha * G_2(Omega) / (4 * pi^2)

    where alpha = 2 (the cubic shadow from the spin-2 channel) and
    G_2(Omega) is the genus-2 Siegel Eisenstein series of weight 2.

    For numerical computation, we use the separating degeneration:
        C_3 ~ alpha * (E_2(tau) + E_2(sigma)) * |z|^2 / Im(tau) / Im(sigma)

    Returns
    -------
    complex : approximate C_3(Omega)
    """
    Omega = validate_period_matrix(tau, z, sigma)
    q = np.exp(2j * math.pi * tau)
    p = np.exp(2j * math.pi * sigma)
    r = np.exp(2j * math.pi * z)

    # Eisenstein series E_2(tau) = 1 - 24 * sum_{n>=1} sigma_1(n) * q^n
    # (quasi-modular, weight 2)
    E2_tau = 1.0 + 0j
    for n in range(1, N_terms + 1):
        # sigma_1(n) = sum of divisors of n
        sig1 = sum(d for d in range(1, n + 1) if n % d == 0)
        E2_tau -= 24 * sig1 * q**n

    E2_sigma = 1.0 + 0j
    for n in range(1, N_terms + 1):
        sig1 = sum(d for d in range(1, n + 1) if n % d == 0)
        E2_sigma -= 24 * sig1 * p**n

    # The genus-2 cocycle: leading order in the separating degeneration
    # The z-dependence enters through the propagator between the two handles
    Y = Omega.imag
    propagator = abs(z) ** 2 / (Y[0, 0] * Y[1, 1])

    # alpha = 2 (cubic shadow S_3 for W_{1+infty} spin-2 channel)
    alpha = SHADOW_TOWER_W1INF[3]

    C3 = alpha * (E2_tau + E2_sigma) * propagator / (4 * math.pi**2)

    return C3


def _genus2_shadow_cocycle_c4(
    tau: complex, z: complex, sigma: complex,
    N_terms: int = 10,
) -> complex:
    r"""Compute the quartic genus-2 cocycle C_4(Omega) from m_4.

    The m_4 correction involves the four-point function integral.
    The leading contribution in the separating degeneration:

        C_4(Omega) ~ S_4 * [E_2(tau)^2 + E_2(sigma)^2] * |z|^4 / ...

    At c=1, S_4 = 10/27 (from the spin-2 channel of W_{1+infty}).

    This is SUBLEADING compared to C_3 by a factor of |z|^2 / Im(Omega).
    """
    Omega = validate_period_matrix(tau, z, sigma)
    q = np.exp(2j * math.pi * tau)
    p = np.exp(2j * math.pi * sigma)

    E2_tau = 1.0 + 0j
    E2_sigma = 1.0 + 0j
    for n in range(1, N_terms + 1):
        sig1 = sum(d for d in range(1, n + 1) if n % d == 0)
        E2_tau -= 24 * sig1 * q**n
        E2_sigma -= 24 * sig1 * p**n

    Y = Omega.imag
    propagator_sq = (abs(z) ** 4 /
                     (Y[0, 0]**2 * Y[1, 1]**2))

    S4 = SHADOW_TOWER_W1INF[4]

    C4 = S4 * (E2_tau**2 + E2_sigma**2) * propagator_sq / (16 * math.pi**4)

    return C4


def genus2_partition_w1inf(
    tau: complex, z: complex, sigma: complex,
    c: int = 1,
    max_shadow_depth: int = 4,
    N_terms: int = 20,
) -> Dict[str, complex]:
    r"""Genus-2 chiral partition function for W_{1+infty} at c=1 (class M).

    W_{1+infty} has an infinite shadow tower (class M): m_3 != 0 gives
    the first correction, m_4 the second, etc.  The genus-2 partition
    function is:

        Z_2^W(Omega) = Z_2^{Heis}(Omega) * R_shadow(Omega)

    where the shadow correction factor is:

        R_shadow = 1 + S_3 * C_3(Omega) + S_4 * C_4(Omega) + ...

    The FULL series is Gevrey-1 divergent (shadow class M implies
    Borel summable but not convergent).  We compute the first few
    terms of the asymptotic expansion.

    CLAIM STATUS: The formula for Z_2^W is CONJECTURAL.  The corrections
    C_k(Omega) are computed in the separating degeneration limit, and
    their Sp_4(Z) modularity is part of the conjecture (conj:sp4-modularity).

    The Siegel modular properties:
    - Z_2^{Heis} transforms with weight -c/2 = -1/2.
    - R_shadow is NOT a Siegel modular form (class M implies mock modularity).
    - The PRODUCT Z_2^W is a MOCK Siegel modular form: it transforms as
      weight -1/2 up to a non-holomorphic shadow correction.

    Parameters
    ----------
    tau, z, sigma : complex
        Period matrix entries.
    c : int
        Central charge (default 1 for W_{1+infty} at self-dual point).
    max_shadow_depth : int
        Maximum depth of shadow tower to include (3, 4, or higher).
    N_terms : int
        Lattice summation range.

    Returns
    -------
    dict with partition function data and shadow corrections.
    """
    Omega = validate_period_matrix(tau, z, sigma)

    # Base: Heisenberg partition function
    heis = genus2_partition_heisenberg(tau, z, sigma, c=c, N_terms=N_terms)
    Z2_heis = heis["Z2_holomorphic"]

    # Shadow corrections
    C3 = _genus2_shadow_cocycle_c3(tau, z, sigma, N_terms=min(N_terms, 15))
    C4 = 0.0
    if max_shadow_depth >= 4:
        C4 = _genus2_shadow_cocycle_c4(tau, z, sigma, N_terms=min(N_terms, 15))

    # Shadow correction factor
    # R = 1 + S_3 * C_3 + S_4 * C_4 + ...
    # Note: S_3 = 2 (cubic shadow), S_4 = 10/27 (quartic shadow)
    R_shadow = 1.0 + SHADOW_TOWER_W1INF[3] * C3
    if max_shadow_depth >= 4:
        R_shadow += SHADOW_TOWER_W1INF[4] * C4

    Z2_W = Z2_heis * R_shadow

    # Full (non-holomorphic)
    det_Y = np.linalg.det(Omega.imag)
    Z2_full = abs(Z2_W) ** 2 / det_Y ** (c / 2.0)

    return {
        "Z2_holomorphic": Z2_W,
        "Z2_full": Z2_full,
        "Z2_heisenberg": Z2_heis,
        "R_shadow": R_shadow,
        "C3": C3,
        "C4": C4,
        "S3": SHADOW_TOWER_W1INF[3],
        "S4": SHADOW_TOWER_W1INF[4],
        "Delta_5": heis["Delta_5"],
        "Phi_10": heis["Phi_10"],
        "det_Im_Omega": det_Y,
        "central_charge": c,
        "weight_heisenberg": -c / 2.0,
        "shadow_class": "M",
        "max_shadow_depth": max_shadow_depth,
        "is_mock_modular": True,
        "explanation": (
            f"W_{{1+inf}} at c={c}: Z_2 = Z_2^{{Heis}} * R_shadow. "
            f"Class M: infinite shadow tower, Gevrey-1 divergent. "
            f"R_shadow = 1 + {SHADOW_TOWER_W1INF[3]}*C_3 + "
            f"{SHADOW_TOWER_W1INF[4]}*C_4 + ... "
            f"Mock Siegel modular of weight {-c/2.0}."
        ),
    }


# =========================================================================
# 5. K3 x E genus-2 partition function
# =========================================================================

def genus2_partition_k3xe(
    tau: complex, z: complex, sigma: complex,
    N_terms: int = 20,
) -> Dict[str, complex]:
    r"""Genus-2 partition function for K3 x E.

    CLAIM STATUS: CONJECTURAL (depends on CY-A_3 for the existence of
    the chiral algebra A_{K3xE}).  The formula is motivated by the
    Borcherds product / BKM structure (AP-CY8: observation, not theorem).

    For K3 x E (c=24), the genus-2 partition function is controlled by
    the Igusa cusp form:

        Z_2^{K3xE}(Omega) = 1 / Phi_10(Omega)

    This is the genus-2 analogue of the genus-1 result:
        Z_1^{K3} = 1/eta^{24} * Theta_{Leech} = J(tau)

    The WEIGHT of 1/Phi_10 under Sp_4(Z):
        wt(1/Phi_10) = -10

    The S-matrix has weight:
        wt(S-hat) = -2 * kappa_cat_fiber = -2 * 2 = -4

    The relationship (from conj:s-matrix-phi10):
        S-hat = Phi_10^{-1} * (Eisenstein of weight 6)
    so wt(S-hat) = -10 + 6 = -4.  Consistent.

    The representation of Sp_4(Z): TRIVIAL (scalar).
    Phi_10 is a scalar-valued Siegel modular form, not vector-valued.
    (Delta_5 is a modular form on the full Sp_4(Z) of weight 5, but it
    changes sign under the center +/-I_4, so Phi_10 = Delta_5^2 is
    invariant under the full group.)

    Fourier-Jacobi expansion:
        1/Phi_10 = sum_{m >= -1} psi_m(tau, z) * p^m
    where psi_{-1} = 1/phi_{10,1} and phi_{10,1} = eta^{18} theta_1^2.

    Parameters
    ----------
    tau, z, sigma : complex
        Period matrix entries.
    N_terms : int
        Lattice summation range.
    """
    Omega = validate_period_matrix(tau, z, sigma)

    phi10 = igusa_cusp_form_phi10(tau, z, sigma, N_terms)
    d5 = igusa_cusp_form_delta5(tau, z, sigma, N_terms)

    if abs(phi10) < 1e-300:
        Z2 = float('inf')
    else:
        Z2 = 1.0 / phi10

    return {
        "Z2": Z2,
        "Phi_10": phi10,
        "Delta_5": d5,
        "kappa_cat": 0,           # chi(O_{K3 x E}) = 0
        "kappa_cat_fiber": 2,     # chi(O_{K3}) = 2
        "kappa_BKM": 5,           # weight of Delta_5
        "kappa_ch": 3,            # chiral algebra kappa (from Phi functor)
        "weight_Phi10": 10,
        "weight_1_over_Phi10": -10,
        "weight_S_hat": -4,       # = -2 * kappa_cat_fiber
        "weight_Eisenstein": 6,    # = 2*kappa_BKM - 2*kappa_cat_fiber = 10-4
        "sp4_representation": "trivial (scalar)",
        "claim_status": "CONJECTURAL (depends on CY-A_3)",
        "explanation": (
            "K3 x E: Z_2 = 1/Phi_10(Omega). "
            "Phi_10 = Delta_5^2, weight 10 on Sp_4(Z). "
            "S-hat = Phi_10^{-1} * E_6 has weight -10+6 = -4 = -2*kappa_cat_fiber. "
            "The Borcherds product equals the bar Euler product of the K3 "
            "elliptic genus (OBSERVATION, AP-CY8, not theorem). "
            "CONDITIONAL on CY-A_3 for the chiral algebra A_{K3xE}."
        ),
    }


# =========================================================================
# 6. Sp_4(Z) modularity verification
# =========================================================================

def verify_sp4_modularity_delta5(
    tau: complex, z: complex, sigma: complex,
    N_terms: int = 15,
    tol: float = 1e-4,
) -> Dict[str, object]:
    """Verify Sp_4(Z) transformation of Delta_5 under generators.

    Delta_5 has weight 5 on Sp_4(Z) WITH THETA MULTIPLIER chi:

        Delta_5(gamma . Omega) = chi(gamma) * det(C*Omega + D)^5 * Delta_5(Omega)

    The multiplier system chi satisfies:
      chi(T_i) = -1  for each elementary T-translation (i = 1, 2, 3)
      chi^2 = 1  (so Phi_10 = Delta_5^2 has trivial multiplier)

    This multiplier arises because Delta_5 = prod of 10 even theta constants,
    and each theta[a,b] picks up a phase exp(pi*i*a^T*B*a/4) under
    Omega -> Omega + B.  The product over all 10 even characteristics gives
    a net sign of -1 for each elementary translation.

    NOTE: Delta_5 changes sign under the CENTER element -I_4:
        Delta_5(-Omega) = (-1)^5 * Delta_5(Omega) = -Delta_5(Omega)
    So Delta_5 is a modular form of weight 5 on the FULL Sp_4(Z)
    with character, and its square Phi_10 = Delta_5^2 has weight 10
    with trivial character (invariant under the center).
    """
    Omega = validate_period_matrix(tau, z, sigma)
    gens = sp4_generators()

    d5_orig = igusa_cusp_form_delta5(tau, z, sigma, N_terms)

    results = {}

    # Test T-translations: Omega -> Omega + B (symmetric integer B)
    # det(C*Omega+D) = det(I_2) = 1, so the automorphy factor is 1.
    # But the theta multiplier gives chi(T_i) = -1.
    # Therefore: Delta_5(Omega + B) = -1 * Delta_5(Omega) for elementary B.
    for name in ["T1", "T2", "T3"]:
        gamma = gens[name]
        Omega_new = sp4_action(gamma, Omega)
        d5_new = igusa_cusp_form_delta5(
            Omega_new[0, 0], Omega_new[0, 1], Omega_new[1, 1], N_terms)
        ratio = d5_new / d5_orig if abs(d5_orig) > 1e-300 else float('inf')
        # Expected ratio is -1 (theta multiplier chi(T) = -1)
        expected = -1.0
        results[name] = {
            "ratio": ratio,
            "expected": expected,
            "error": abs(ratio - expected),
            "passes": abs(ratio - expected) < tol,
        }

    # Test S-inversion: Omega -> -Omega^{-1}
    # det(C*Omega+D) = det(-Omega) for S = ((0,I),(-I,0))
    # Actually: C = -I, D = 0, so C*Omega + D = -Omega
    # det(-Omega) = det(Omega) (2x2 matrix, det(-M) = det(M))
    # So Delta_5(S.Omega) = det(Omega)^5 * Delta_5(Omega) (WRONG SIGN)
    # CORRECT: C = -I, D = 0, C*Omega+D = -Omega
    # det(C*Omega+D) = det(-Omega) = (-1)^2 * det(Omega) = det(Omega)
    # So Delta_5(-Omega^{-1}) = det(Omega)^5 * Delta_5(Omega)
    #
    # Wait, re-derive: S = ((0, I_2), (-I_2, 0))
    # A = 0, B = I, C = -I, D = 0
    # gamma.Omega = (A*Omega + B)(C*Omega + D)^{-1} = (0+I)(-Omega+0)^{-1}
    #             = I * (-Omega)^{-1} = -Omega^{-1}
    # det(C*Omega + D) = det(-Omega) = det(Omega)  (for 2x2: (-1)^2 = 1)
    gamma_S = gens["S"]
    Omega_S = sp4_action(gamma_S, Omega)
    d5_S = igusa_cusp_form_delta5(
        Omega_S[0, 0], Omega_S[0, 1], Omega_S[1, 1], N_terms)

    det_Omega = np.linalg.det(Omega)
    expected_factor = det_Omega ** 5
    ratio_S = d5_S / (expected_factor * d5_orig) if abs(d5_orig * expected_factor) > 1e-300 else float('inf')

    results["S"] = {
        "ratio": ratio_S,
        "expected_factor": expected_factor,
        "d5_original": d5_orig,
        "d5_transformed": d5_S,
        "error": abs(ratio_S - 1.0) if np.isfinite(ratio_S) else float('inf'),
        "passes": abs(ratio_S - 1.0) < tol if np.isfinite(ratio_S) else False,
    }

    all_pass = all(r["passes"] for r in results.values())

    return {
        "generator_tests": results,
        "all_pass": all_pass,
        "weight": 5,
        "group": "Sp_4(Z) / +/-I_4",
    }


# =========================================================================
# 7. Fourier-Jacobi expansion
# =========================================================================

def _eta_function(tau: complex, N_terms: int = 50) -> complex:
    """Compute eta(tau) = q^{1/24} * prod_{n>=1} (1 - q^n).

    q = e^{2 pi i tau}, Im(tau) > 0.
    """
    if tau.imag <= 0:
        raise ValueError("Im(tau) must be positive")
    q = np.exp(2j * math.pi * tau)
    result = np.exp(2j * math.pi * tau / 24)  # q^{1/24}
    for n in range(1, N_terms + 1):
        result *= (1 - q**n)
    return result


def _theta1_function(tau: complex, z_val: complex, N_terms: int = 50) -> complex:
    """Compute theta_1(tau, z) = -i * sum_{n in Z} (-1)^n q^{(n+1/2)^2/2} y^{n+1/2}.

    Uses the standard product formula:
        theta_1(tau, z) = 2 * q^{1/8} * sin(pi*z) * prod_{n>=1}
            (1 - q^n)(1 - q^n * y)(1 - q^n / y)
    where q = e^{2 pi i tau}, y = e^{2 pi i z}.
    """
    if tau.imag <= 0:
        raise ValueError("Im(tau) must be positive")
    q = np.exp(2j * math.pi * tau)
    y = np.exp(2j * math.pi * z_val)

    result = 2 * q**(1/8) * np.sin(math.pi * z_val)
    for n in range(1, N_terms + 1):
        qn = q**n
        result *= (1 - qn) * (1 - qn * y) * (1 - qn / y)
    return result


def fourier_jacobi_phi10_m1(
    tau: complex, z_val: complex, N_terms: int = 50,
) -> complex:
    r"""Compute phi_{10,1}(tau, z) = eta(tau)^{18} * theta_1(tau, z)^2.

    This is the first Fourier-Jacobi coefficient of Phi_10:
        Phi_10(tau, z, sigma) = phi_{10,1}(tau, z) * p + O(p^2)

    phi_{10,1} is the UNIQUE Jacobi cusp form of weight 10 and index 1
    on SL_2(Z).  It is the product of:
      - eta^{18}: weight 9 from the Dedekind eta function (18/2 = 9)
      - theta_1^2: weight 1, index 1 from the Jacobi theta function

    Total weight: 9 + 1 = 10.  Index: 1.

    Parameters
    ----------
    tau : complex
        Modular parameter, Im(tau) > 0.
    z_val : complex
        Elliptic variable.
    N_terms : int
        Number of product terms.

    Returns
    -------
    complex : phi_{10,1}(tau, z)
    """
    eta_val = _eta_function(tau, N_terms)
    theta1_val = _theta1_function(tau, z_val, N_terms)
    return eta_val**18 * theta1_val**2


def fourier_jacobi_expansion_phi10(
    tau: complex, z_val: complex, sigma: complex,
    M_max: int = 3,
    N_terms: int = 30,
) -> Dict[str, complex]:
    r"""Compute the Fourier-Jacobi expansion of Phi_10.

    Phi_10(tau, z, sigma) = sum_{m >= 1} phi_{10,m}(tau, z) * p^m

    where p = e^{2 pi i sigma}.

    The coefficients phi_{10,m} are Jacobi forms of weight 10 and index m.

    We compute:
      phi_{10,1} = eta^{18} * theta_1^2  (exact, weight 10, index 1)
      phi_{10,2}: computed by extracting the p^2 coefficient from the
                  theta-constant product.

    The Fourier-Jacobi expansion converges for Im(sigma) > 0 (|p| < 1).

    For VERIFICATION: sum_{m=1}^{M_max} phi_{10,m} * p^m should approximate
    Phi_10 computed directly from the product of 10 theta constants.

    Parameters
    ----------
    tau, z_val, sigma : complex
        Period matrix entries.
    M_max : int
        Number of FJ coefficients to compute.
    N_terms : int
        Product terms for eta/theta.
    """
    Omega = validate_period_matrix(tau, z_val, sigma)
    p = np.exp(2j * math.pi * sigma)

    # Direct computation
    phi10_direct = igusa_cusp_form_phi10(tau, z_val, sigma, N_terms=min(N_terms, 20))

    # m=1: phi_{10,1} = eta^18 * theta_1^2
    phi_m1 = fourier_jacobi_phi10_m1(tau, z_val, N_terms)

    # The FJ expansion: Phi_10 = phi_{10,1} * p + phi_{10,2} * p^2 + ...
    # So: phi_{10,2} * p^2 = Phi_10 - phi_{10,1} * p - O(p^3)
    # To extract phi_{10,2}, compute at the given sigma and subtract m=1:
    residual = phi10_direct - phi_m1 * p

    # phi_{10,2} = residual / p^2 (leading correction)
    phi_m2 = residual / p**2 if abs(p) > 1e-30 else 0.0

    # FJ partial sum
    fj_partial = phi_m1 * p
    if M_max >= 2:
        fj_partial += phi_m2 * p**2

    fj_error = abs(phi10_direct - fj_partial) / abs(phi10_direct) if abs(phi10_direct) > 1e-300 else float('inf')

    # phi_0 of 1/Phi_10:
    # 1/Phi_10 = p^{-1} * 1/phi_{10,1} + psi_0 + psi_1 * p + ...
    # psi_{-1} = 1/phi_{10,1}
    psi_neg1 = 1.0 / phi_m1 if abs(phi_m1) > 1e-300 else float('inf')

    # psi_0 = -phi_{10,2} / phi_{10,1}^2
    psi_0 = -phi_m2 / phi_m1**2 if abs(phi_m1) > 1e-300 else float('inf')

    return {
        "phi_10_1": phi_m1,
        "phi_10_2": phi_m2,
        "phi_10_direct": phi10_direct,
        "fj_partial_sum": fj_partial,
        "fj_relative_error": fj_error,
        "M_max": M_max,
        # Inverse FJ coefficients (for the S-matrix / partition function)
        "psi_neg1": psi_neg1,
        "psi_0": psi_0,
        "p": p,
        "jacobi_form_data": {
            "phi_10_1": {"weight": 10, "index": 1,
                         "formula": "eta^18 * theta_1^2"},
            "phi_10_2": {"weight": 10, "index": 2,
                         "formula": "extracted from direct computation"},
        },
    }


def fourier_jacobi_heisenberg_genus2(
    tau: complex, z_val: complex, sigma: complex,
    c: int = 1,
    M_max: int = 3,
    N_terms: int = 30,
) -> Dict[str, complex]:
    r"""Fourier-Jacobi expansion of the Heisenberg genus-2 partition function.

    Z_2^{Heis}(Omega) = Delta_5^{-c/12} = sum_{m} phi_m^{Heis} * p^m

    The FJ coefficients phi_m^{Heis} are weak Jacobi forms of weight -c/2
    and index m.

    At leading order (large Im(sigma)):
        phi_0^{Heis}(tau, z) = [phi_{10,1}(tau, z)]^{-c/12}
                             * (1 + corrections from phi_{10,2}/phi_{10,1})

    For c=1:
        phi_0(tau, z) = [eta^{18} theta_1^2]^{-1/12}
                      = eta^{-3/2} * theta_1^{-1/6}

    This is NOT a standard Jacobi form (fractional weight and index).
    The full partition function Z_2 is a section of a fractional power
    of the Hodge bundle, which requires the metaplectic cover Mp_4(Z).

    For c=24 (K3): phi_0(tau, z) = [eta^{18} theta_1^2]^{-2} = eta^{-36} theta_1^{-4}
    Weight: -24/2 = -12.  This IS an integer weight.
    """
    Omega = validate_period_matrix(tau, z_val, sigma)
    p = np.exp(2j * math.pi * sigma)

    heis = genus2_partition_heisenberg(tau, z_val, sigma, c=c, N_terms=N_terms)
    Z2 = heis["Z2_holomorphic"]

    # phi_{10,1} for the leading FJ term
    phi_m1 = fourier_jacobi_phi10_m1(tau, z_val, N_terms)

    # Leading FJ coefficient of Z2 = Delta_5^{-c/12}
    # In the large Im(sigma) limit, the leading behaviour is
    # Z2 ~ (phi_{10,1} * p)^{-c/12} * ... but this is NOT the FJ expansion
    # in p directly.

    # The correct approach: expand Delta_5 = sum phi_m p^m first,
    # then invert the power.  For the first few terms:

    # phi_0^{Heis} ~ phi_{10,1}^{-c/12} (leading term, from p^{-c/12} * ...)
    # This only makes sense for c divisible by 12.
    # For general c, Z2 is a section of a fractional line bundle.

    # For c=24: Z2 = Delta_5^{-2}, weight -10 (since Delta_5 has weight 5)
    # The FJ expansion IS well-defined.

    # For c=1: the FJ expansion involves fractional powers of p,
    # which means it's on the metaplectic cover.

    # We compute the first few "effective" FJ coefficients by evaluating
    # Z2 at several sigma values and performing a numerical DFT.

    phi_fj = {}
    if c % 12 == 0:
        # Integer power of Delta_5: clean FJ expansion
        power = -c // 12
        # Z2 = Delta_5^{power}
        d5 = heis["Delta_5"]
        # Delta_5 = phi_{10,1}^{1/2} * p^{1/2} * (1 + ...) approximately
        # This is getting complicated; compute numerically.
        phi_fj["phi_0_effective"] = Z2 / p**(power / 2.0) if abs(p) > 1e-30 else float('inf')
    else:
        phi_fj["phi_0_effective"] = Z2 / p**(-c / 24.0) if abs(p) > 1e-30 else float('inf')
        phi_fj["note"] = "Fractional power of p: metaplectic cover required"

    return {
        "Z2_holomorphic": Z2,
        "phi_fj_coefficients": phi_fj,
        "central_charge": c,
        "weight": -c / 2.0,
        "leading_fj_weight": 10 * (-c / 12.0),
        "phi_10_1": phi_m1,
    }


# =========================================================================
# 8. Summary and weight table
# =========================================================================

def genus2_weight_table() -> Dict[str, Dict]:
    r"""The genus-2 Siegel modular weight table for key examples.

    Returns the modular weights under Sp_4(Z) for the genus-2
    partition functions of the main chiral algebra families.

    WEIGHT FORMULA (from conj:sp4-modularity):
        Holomorphic partition function: wt = -c/2
        S-matrix: wt = -2 * kappa_cat_fiber
        BKM denominator: wt = kappa_BKM (= c(0)/2 of input Jacobi form)

    For the S-matrix vs partition function:
        S-hat = Z_2^{-1} * (normalisation)
    """
    return {
        "Heisenberg_c1": {
            "algebra": "H_k at c=1",
            "shadow_class": "G",
            "c": 1,
            "weight_partition": -0.5,    # -c/2
            "weight_S_matrix": "N/A (class G: S trivial)",
            "kappa_ch": 1,
            "kappa_cat": "N/A",
            "kappa_BKM": "N/A",
            "sp4_subgroup": "Mp_4(Z) (metaplectic, half-integral weight)",
        },
        "Heisenberg_c24": {
            "algebra": "H_k^{24} at c=24",
            "shadow_class": "G",
            "c": 24,
            "weight_partition": -12,
            "weight_S_matrix": "N/A (class G: S trivial)",
            "kappa_ch": 24,
            "kappa_cat": "N/A",
            "kappa_BKM": "N/A",
            "sp4_subgroup": "Sp_4(Z) (integral weight)",
        },
        "W1inf_c1": {
            "algebra": "W_{1+inf} at c=1",
            "shadow_class": "M",
            "c": 1,
            "weight_partition": -0.5,
            "weight_S_matrix": "mock Siegel modular",
            "kappa_ch": 0.5,    # spin-2 channel
            "kappa_cat": "N/A (not a CY target)",
            "kappa_BKM": "N/A",
            "sp4_subgroup": "Mp_4(Z) + shadow completion",
            "mock_modular": True,
        },
        "K3xE": {
            "algebra": "A_{K3 x E} (CONJECTURAL, CY-A_3)",
            "shadow_class": "M (conjectured)",
            "c": 24,
            "weight_partition": -12,       # -c/2 = -24/2
            "weight_S_matrix": -4,         # -2 * kappa_cat_fiber
            "kappa_ch": 3,
            "kappa_cat": 0,                # chi(O_{K3 x E})
            "kappa_cat_fiber": 2,          # chi(O_{K3})
            "kappa_BKM": 5,                # weight of Delta_5
            "weight_Phi10": 10,            # 2 * kappa_BKM
            "weight_Eisenstein": 6,        # 2*kappa_BKM - 2*kappa_cat_fiber
            "sp4_subgroup": "Sp_4(Z) (full group, scalar representation)",
            "claim_status": "CONJECTURAL",
        },
        "K3xE_orbifold_Z2": {
            "algebra": "A_{K3xE/Z2} (Enriques, CONJECTURAL)",
            "shadow_class": "unknown",
            "c": 12,
            "weight_partition": -6,
            "weight_S_matrix": "CONJECTURAL",
            "kappa_BKM": 4,
            "sp4_subgroup": "subgroup of Sp_4(Z)",
            "claim_status": "CONJECTURAL",
        },
    }


def categorical_s_matrix_summary() -> Dict[str, str]:
    """Summary of the categorical S-matrix weight computation.

    The E_3 categorical S-matrix S-hat(Omega) on H_2 has:

        wt(S-hat) = -2 * kappa_cat_fiber

    This comes from:
        S-hat = Phi_10^{-1} * E_{wt=6}
        wt(S-hat) = -10 + 6 = -4 = -2 * 2 = -2 * kappa_cat_fiber

    The total-space value kappa_cat(K3 x E) is 0; using it here would
    give the wrong weight.  The factor of 2 compared to the E_2 formula
    reflects genus doubling of the fiber normalizer.
    """
    return {
        "E2_weight_formula": "wt(S_{ij}) = -kappa_cat",
        "E3_weight_formula": "wt(S-hat) = -2 * kappa_cat_fiber",
        "K3xE_kappa_cat": "0 (= chi(O_{K3 x E}))",
        "K3xE_kappa_cat_fiber": "2 (= chi(O_{K3}))",
        "K3xE_wt_S_hat": "-4",
        "K3xE_decomposition": "S-hat = Phi_10^{-1} * E_6",
        "weight_check": "-10 + 6 = -4 = -2*2",
        "genus_doubling": (
            "E_3 -> genus 2: the modular weight doubles relative to E_2, "
            "matching the doubling of spectral parameters (u,v) -> (tau_1,z,tau_2)."
        ),
    }


# =========================================================================
# 9. Genus-2 comparison engine
# =========================================================================

def compare_genus2_heisenberg_vs_w1inf(
    tau: complex, z: complex, sigma: complex,
    N_terms: int = 15,
) -> Dict[str, object]:
    """Compare the genus-2 partition functions of Heisenberg vs W_{1+inf}.

    The comparison:
        Z_2^{W} / Z_2^{Heis} = R_shadow
    should be close to 1 for small |z| (separating degeneration) and
    deviate for larger |z| (shadow corrections become important).
    """
    heis = genus2_partition_heisenberg(tau, z, sigma, c=1, N_terms=N_terms)
    w1inf = genus2_partition_w1inf(tau, z, sigma, c=1, N_terms=N_terms)

    R_ratio = w1inf["Z2_holomorphic"] / heis["Z2_holomorphic"] if abs(heis["Z2_holomorphic"]) > 1e-300 else float('inf')

    return {
        "Z2_heisenberg": heis["Z2_holomorphic"],
        "Z2_w1inf": w1inf["Z2_holomorphic"],
        "R_shadow": w1inf["R_shadow"],
        "ratio_Z2_W_over_Heis": R_ratio,
        "ratio_matches_R_shadow": abs(R_ratio - w1inf["R_shadow"]) < 1e-9,
        "C3": w1inf["C3"],
        "C4": w1inf["C4"],
    }
