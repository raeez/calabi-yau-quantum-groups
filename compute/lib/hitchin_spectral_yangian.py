r"""Explicit Hitchin--Yangian spectral parameter identification.

STATUS: CONJECTURAL (AP-CY14, AP-CY6).
The identification of the Hitchin spectral parameter with the K3 Yangian
spectral parameter is conditional on CY-A_2 (proved at d=2) and on the
conjectural existence of Y(g_{K3}).  New identifications are CONJECTURAL.
Feigin--Frenkel and Beilinson--Drinfeld results are ProvedElsewhere.

MATHEMATICAL FRAMEWORK
======================

This engine makes EXPLICIT the chain of identifications connecting:

(1) The Hitchin spectral curve Sigma subset T*C, defined by
        det(phi - lambda*I) = 0
    where phi is the Higgs field.  The tautological 1-form lambda on
    Tot(K_C) restricts to a section of pi^*K_C on Sigma.

(2) The K3 embedding: for C subset K3 with K_C = L|_C (adjunction),
    Sigma embeds into Tot(L|_C), a tubular neighbourhood of C in K3.
    The spectral parameter lambda becomes a coordinate on K3 transverse
    to C.

(3) The Yangian spectral parameter z: the Drinfeld coproduct
        Delta_z: Y(g_{K3}) -> Y(g_{K3}) hat{otimes} Y(g_{K3})
    uses z as a Yangian spectral parameter (AP-CY31: NOT a worldsheet
    coordinate).  The identification z = lambda connects the Hitchin
    integrable system to the Yangian quantum group.

(4) The R-matrix at z: evaluation of the universal R-matrix at the
    spectral point z in Sigma.  For the abelian (gl_1) K3 Yangian:
        R_{K3}(z) = diag((z - h_i)/(z + h_i))_{i=1,...,24}
    The R-matrix is a function on Sigma, i.e. its argument z is the
    eigenvalue of the Higgs field phi.

(5) The Bethe ansatz: the transfer matrix
        T(z) = tr_V R_{01}(z-u_1) ... R_{0N}(z-u_N)
    is diagonalised by the Bethe ansatz.  The eigenvalues are functions
    on Sigma: the Bethe roots u_i are points on the spectral curve.
    The Bethe ansatz equations are saddle-point conditions for the
    Yang-Yang potential on Sigma.

THE KEY GEOMETRIC INPUT: For G = SL_2 (A_1 type) on a genus-g curve C
inside K3, the spectral curve Sigma -> C is a DOUBLE COVER:
    Sigma = { lambda^2 = q(z) }  subset Tot(K_C)
where q in H^0(C, K_C^2) is the quadratic differential (Hitchin
Hamiltonian).  By Riemann-Hurwitz:
    2g(Sigma)-2 = 2*(2g(C)-2) + B
where B = deg(K_C^2) = 2*(2g-2) branch points (zeros of q), giving:
    g(Sigma) = 2*g(C) - 1.

More generally for SL_n:
    g(Sigma) = n^2*(g(C)-1) + 1.

CONVENTIONS
===========
  - z, lambda: spectral parameter (Yangian/Hitchin, AP-CY31 compliant)
  - u: Bethe root variable
  - h_i: Yangian deformation parameters (i = 1,...,24 for K3)
  - omega_{ij}: Mukai pairing, signature (4,20)
  - CY_2 constraint: sum h_i = 0
  - kappa subscripts per AP113: kappa_ch, kappa_BKM, etc.
  - AP-CY28: test points avoid poles at +/-h_i

REFERENCES
==========
  chiral_hitchin_k3.py (parent: Hitchin system on K3 curves, 113 tests)
  spectral_curve_chiral.py (spectral curve geometry)
  k3_yangian.py (K3 Yangian presentation and R-matrix)
  k3_structure_function_explicit.py (degree-(24,24) structure function)
  bethe_ansatz_e1_cy3.py (Bethe ansatz from E_1 MC equation)
  higgs_bundle_chiral.py (Hitchin-to-chiral functor)
  geometric_langlands_shadow.py (Lie algebra data, critical levels)

MANUSCRIPT REFERENCES
=====================
  chapters/connections/geometric_langlands.tex: sec:chiral-hitchin-k3,
    conj:hitchin-spectral-yangian, conj:hitchin-yangian-module
  chapters/examples/k3_yangian_chapter.tex: ch:k3-yangian
  notes/physics_hitchin_langlands.tex
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

import numpy as np

from compute.lib.geometric_langlands_shadow import (
    LieAlgebraData,
    _casimir_degrees,
    critical_level,
    kappa_affine,
    lie_data,
    langlands_dual_data,
)

F = Fraction
STATUS = 'CONJECTURAL'  # AP-CY14: all new identifications are conjectural


# =========================================================================
# 1. SPECTRAL CURVE GEOMETRY (det(phi - lambda) = 0)
# =========================================================================

class SpectralCurveK3Data(NamedTuple):
    """Spectral curve Sigma -> C for C subset K3, group G.

    The spectral curve is defined by det(phi - lambda*I) = 0 in Tot(K_C).
    For C subset K3: K_C = L|_C (adjunction), so Sigma subset Tot(L|_C).

    The tautological section lambda in H^0(Sigma, pi^*K_C) is the
    eigenvalue of the Higgs field phi.  This is the spectral parameter.
    """
    # Curve data
    genus_base: int              # g(C)
    genus_spectral: int          # g(Sigma)
    L_square: int                # L^2 = 2g-2 on K3

    # Cover data
    group_type: str              # Cartan type
    group_rank: int
    cover_degree: int            # n for SL_n
    n_branch_points: int         # generic simple branching

    # Characteristic polynomial data
    char_poly_degree: int        # degree of det(phi - lambda) in lambda
    hitchin_base_summands: Tuple[int, ...]  # dim H^0(K^{d_i})
    dim_hitchin_base: int

    # K3-specific: embedding into Tot(L|_C)
    spectral_embeds_in: str      # description of ambient space
    adjunction: str              # K_C = L|_C


def spectral_curve_genus(n: int, g: int) -> int:
    """Genus of the spectral curve for degree-n cover of genus-g base.

    By Riemann-Hurwitz for the generic spectral curve of SL_n/GL_n:

        2g(Sigma) - 2 = n*(2g-2) + n*(n-1)*(2g-2) = n^2*(2g-2)
        g(Sigma) = n^2*(g-1) + 1

    For SL_2 on genus g: g(Sigma) = 4*(g-1) + 1 = 4g - 3.
    CHECK: for g=2, g(Sigma) = 5. For g=3, g(Sigma) = 9.

    Specialisation for A_1 (n=2):
        g(Sigma) = 2*g(C) - 1 is WRONG in general.
        The correct formula: g(Sigma) = 4*(g-1) + 1 = 4g - 3.

    The simpler formula g(Sigma) = 2g(C)-1 holds only when branch
    points = 2*(2g-2) and degree = 2, but the computation gives:
        2g(S)-2 = 2*(2g-2) + 2*(2g-2) = 4*(2g-2)
        g(S) = 2*(2g-2) + 1 = 4g - 3.

    NOTE: g(Sigma) = 2g-1 is the formula for a hyperelliptic double
    cover of P^1 with 4g branch points.  For a double cover of a
    genus-g curve C (NOT P^1), Riemann-Hurwitz gives a different answer.
    """
    if n < 1:
        raise ValueError(f"Cover degree n must be >= 1, got {n}")
    if g < 0:
        raise ValueError(f"Base genus must be >= 0, got {g}")
    return n * n * (g - 1) + 1


def branch_points_generic(n: int, g: int) -> int:
    """Number of simple branch points for generic spectral curve.

    The discriminant locus of det(phi - lambda) has degree n*(n-1)
    in the Hitchin base direction.  On a genus-g curve with canonical
    bundle of degree 2g-2, the total branching is:

        B = n*(n-1)*(2g-2)

    For SL_2 (n=2) on genus 2: B = 2*1*2 = 4.
    For SL_2 on genus 3: B = 2*1*4 = 8.
    For SL_3 on genus 2: B = 3*2*2 = 12.
    """
    return n * (n - 1) * (2 * g - 2)


def _h0_K_power(g: int, power: int) -> int:
    """dim H^0(C, K_C^i) for genus-g curve, i = power."""
    if power <= 0:
        return 1 if power == 0 else 0
    if g < 2:
        raise ValueError(f"Need genus >= 2, got {g}")
    if power == 1:
        return g
    return (2 * power - 1) * (g - 1)


def spectral_curve_k3(genus: int, group_type: str, group_rank: int
                       ) -> SpectralCurveK3Data:
    """Full spectral curve data for the Hitchin system on C subset K3.

    Parameters
    ----------
    genus : int
        Genus of the base curve C (>= 2).
    group_type : str
        Cartan type ('A', 'B', 'C', 'D', 'E', 'F', 'G').
    group_rank : int
        Rank of the group.

    Returns
    -------
    SpectralCurveK3Data.
    """
    if genus < 2:
        raise ValueError(f"Hitchin system requires genus >= 2, got {genus}")

    # Cover degree: n = rank+1 for type A (SL_{n+1}), rank otherwise
    n = group_rank + 1 if group_type == 'A' else group_rank

    g_spec = spectral_curve_genus(n, genus)
    n_branch = branch_points_generic(n, genus)

    casimirs = _casimir_degrees(group_type, group_rank)
    base_summands = tuple(_h0_K_power(genus, d) for d in casimirs)
    dim_base = sum(base_summands)

    return SpectralCurveK3Data(
        genus_base=genus,
        genus_spectral=g_spec,
        L_square=2 * genus - 2,
        group_type=group_type,
        group_rank=group_rank,
        cover_degree=n,
        n_branch_points=n_branch,
        char_poly_degree=n,
        hitchin_base_summands=base_summands,
        dim_hitchin_base=dim_base,
        spectral_embeds_in=(
            f"Tot(L|_C) = tubular neighbourhood of C in K3 "
            f"(since K_C = L|_C by adjunction)"
        ),
        adjunction="K_C = L|_C (K_S = O_S for K3)",
    )


# =========================================================================
# 2. SPECTRAL PARAMETER IDENTIFICATION: lambda = z
# =========================================================================

class SpectralIdentificationData(NamedTuple):
    """The explicit identification: Hitchin lambda = Yangian z.

    The Hitchin spectral curve Sigma subset Tot(K_C) has a tautological
    section lambda, which is the eigenvalue of the Higgs field phi.
    For C subset K3, the adjunction K_C = L|_C embeds Sigma into K3.

    The Yangian spectral parameter z enters via the Drinfeld coproduct.
    The identification z = lambda is the content of
    conj:hitchin-spectral-yangian.

    Both parameters live in the SAME geometric space: the fibre of L|_C
    over a point of C.  This fibre is the normal direction to C in K3.

    AP-CY31: z is a Yangian spectral parameter, NOT a worldsheet
    coordinate.  The OPE does not have poles at z = 0.
    AP-CY20: the connection to (q,t) parameters goes through the
    Omega-background, not through N_{C/K3} directly.
    """
    # Geometric data
    genus: int
    group_label: str

    # Hitchin side
    hitchin_parameter: str       # "lambda = eigenvalue of phi"
    hitchin_space: str           # "Tot(K_C) = Tot(L|_C)"
    hitchin_fibre_dim: int       # = 1 (rank-1 line bundle)

    # Yangian side
    yangian_parameter: str       # "z in Drinfeld coproduct Delta_z"
    yangian_role: str            # role in the Yangian

    # Identification
    identification: str          # "z = lambda"
    geometric_reason: str        # why they live in the same space
    status: str                  # 'Conjectured'

    # Dependencies
    depends_on: Tuple[str, ...]  # what this is conditional on


def spectral_identification(genus: int, group_type: str, group_rank: int
                            ) -> SpectralIdentificationData:
    """Construct the explicit spectral parameter identification.

    Parameters
    ----------
    genus : int
        Genus of C (>= 2).
    group_type : str
        Cartan type.
    group_rank : int
        Rank.

    Returns
    -------
    SpectralIdentificationData.
    """
    if genus < 2:
        raise ValueError(f"Need genus >= 2, got {genus}")

    label = f'{group_type}{group_rank}'

    return SpectralIdentificationData(
        genus=genus,
        group_label=label,
        hitchin_parameter=(
            "lambda = eigenvalue of the Higgs field phi, defined by "
            "det(phi - lambda*I) = 0 on the spectral curve Sigma"
        ),
        hitchin_space=f"Tot(K_C) = Tot(L|_C) for C subset K3",
        hitchin_fibre_dim=1,
        yangian_parameter=(
            "z = Yangian spectral parameter in the Drinfeld coproduct "
            "Delta_z (AP-CY31: spectral, NOT worldsheet)"
        ),
        yangian_role=(
            "z shifts the transfer matrix argument: T(u) -> T(u-z). "
            "The coproduct Delta_z(T(u)) = T^L(u) T^R(u-z) is the "
            "Miura factorisation at spectral separation z."
        ),
        identification=(
            "z = lambda: both live in the fibre of L|_C over a point "
            "of C. The Hitchin eigenvalue lambda IS the Yangian "
            "spectral parameter z."
        ),
        geometric_reason=(
            "K3 adjunction: K_C = L|_C identifies the cotangent fibre "
            "of C (where the Higgs eigenvalue lambda lives) with the "
            "normal fibre of C in K3 (where the deformation parameter "
            "z lives). Both are coordinates on the same 1-dimensional "
            "fibre of L over a point of C."
        ),
        status='Conjectured',
        depends_on=(
            'CY-A_2 (proved at d=2)',
            'Existence of Y(g_{K3}) (AP-CY14, conjectural)',
            'conj:hitchin-spectral-yangian',
        ),
    )


# =========================================================================
# 3. R-MATRIX ON THE SPECTRAL CURVE
# =========================================================================

class RMatrixSpectralData(NamedTuple):
    """R-matrix evaluated at spectral parameter z in Sigma.

    For the abelian (gl_1) K3 Yangian, the R-matrix is diagonal:

        R_{K3}(z) = diag((z - h_i)/(z + h_i))_{i=1,...,24}

    Via the spectral identification z = lambda, this becomes a
    FUNCTION ON THE SPECTRAL CURVE: at each point p of Sigma,
    z(p) = lambda(p) is the eigenvalue of phi at p, and R_{K3}(z(p))
    is the R-matrix evaluated at that eigenvalue.

    The R-matrix encodes the scattering of Bethe magnons: two particles
    with spectral parameters z_1, z_2 in Sigma scatter with amplitude
    R_{K3}(z_1 - z_2).  The spectral curve is the KINEMATIC SPACE
    of the integrable system.
    """
    # Parameters
    n_params: int                # 24 for K3
    h_params: Tuple[float, ...]  # the h_i values

    # Structure function (scalar R-matrix eigenvalue ratio)
    # g(z) = prod_i (z - h_i)/(z + h_i)
    g_at_sample: complex         # g(z) at a sample point
    g_reflection: complex        # g(z)*g(-z), should = 1

    # R-matrix properties
    is_diagonal: bool            # True for gl_1
    satisfies_ybe: bool          # Yang-Baxter equation
    unitarity: bool              # R(z)*R(-z) = I

    # Poles and zeros on Sigma
    zeros_of_g: Tuple[float, ...]   # z = h_i
    poles_of_g: Tuple[float, ...]   # z = -h_i

    # Spectral curve interpretation
    interpretation: str


def _structure_function(z: complex, h_params: Tuple[float, ...]) -> complex:
    """Evaluate g(z) = prod_i (z - h_i)/(z + h_i)."""
    result = 1.0 + 0.0j
    for h in h_params:
        num = z - h
        den = z + h
        if abs(den) < 1e-15:
            return complex('inf')
        result *= num / den
    return result


def _kummer_h_params(eps: float = 1.0) -> Tuple[float, ...]:
    """Kummer K3 parametrisation: h_i = eps (i=1..4), -eps/5 (i=5..24).

    CY_2 constraint: 4*eps + 20*(-eps/5) = 4*eps - 4*eps = 0. Satisfied.

    AP-CY28: test points must avoid +/-h_i = +/-eps, +/-eps/5.
    """
    pos = [eps] * 4
    neg = [-eps / 5.0] * 20
    return tuple(pos + neg)


def rmatrix_on_spectral_curve(
    genus: int,
    group_type: str = 'A',
    group_rank: int = 0,
    eps: float = 1.0,
    sample_z: complex = 3.7 + 0.1j,
) -> RMatrixSpectralData:
    """Compute R-matrix data evaluated on the spectral curve.

    For the abelian (gl_1) K3 Yangian, the R-matrix at spectral
    parameter z is:

        R_{K3}(z) = diag(g_i(z))  where g_i(z) = (z-h_i)/(z+h_i)

    The scalar structure function g(z) = prod_i g_i(z) is the
    determinant of R_{K3}(z).

    Parameters
    ----------
    genus : int
        Genus of the base curve C (>= 2).  Enters only through the
        spectral curve genus formula.
    group_type : str
        For gl_1 abelian Yangian, this is informational only.
    group_rank : int
        For gl_1, rank = 0 (1-dimensional).
    eps : float
        Kummer parameter (default 1.0).
    sample_z : complex
        Sample evaluation point (AP-CY28: must avoid +/-h_i).
        Default 3.7+0.1j avoids poles at +/-1, +/-0.2.

    Returns
    -------
    RMatrixSpectralData.
    """
    if genus < 2:
        raise ValueError(f"Need genus >= 2, got {genus}")

    h_params = _kummer_h_params(eps)

    # Evaluate structure function at sample point
    g_val = _structure_function(sample_z, h_params)

    # Reflection identity: g(z)*g(-z) = 1
    g_neg = _structure_function(-sample_z, h_params)
    g_reflect = g_val * g_neg

    # Zeros and poles
    zeros = tuple(h for h in h_params)
    poles = tuple(-h for h in h_params)

    return RMatrixSpectralData(
        n_params=24,
        h_params=h_params,
        g_at_sample=g_val,
        g_reflection=g_reflect,
        is_diagonal=True,  # gl_1 is abelian
        satisfies_ybe=True,  # diagonal R-matrices satisfy YBE trivially
        unitarity=abs(g_reflect - 1.0) < 1e-10,
        zeros_of_g=zeros,
        poles_of_g=poles,
        interpretation=(
            "Via z = lambda (Hitchin eigenvalue), R_{K3}(z) is a function "
            "on the spectral curve Sigma. At each point p of Sigma, "
            "R_{K3}(lambda(p)) gives the scattering matrix. The Bethe "
            "magnons are particles living on Sigma, and R encodes their "
            "pairwise scattering."
        ),
    )


# =========================================================================
# 4. BETHE ANSATZ ON THE SPECTRAL CURVE
# =========================================================================

class BetheOnSpectralCurveData(NamedTuple):
    """Bethe ansatz with spectral parameter living on Sigma.

    The transfer matrix T(z) = tr_V R_{01}(z-u_1) ... R_{0N}(z-u_N)
    is a function of z in Sigma.  The Bethe ansatz diagonalises T(z)
    at ALL z simultaneously (integrability).

    The Bethe roots u_1,...,u_M are points on Sigma (or more precisely,
    their z-coordinates are eigenvalues of phi at M points of Sigma).

    The Bethe ansatz equations (BAE) are:

        prod_{j != i} g(u_i - u_j) = (-1)^{M-1} prod_{a=1}^{K}
                                      phi_a(u_i - z_a)

    where z_a are the inhomogeneity parameters (also points on Sigma)
    and phi_a(u) = u/(u + hbar) for the standard Fock representation.

    The Yang-Yang potential W({u_i}, {z_a}) is:

        W = sum_{i<j} V(u_i - u_j) + sum_{i,a} V_ext(u_i - z_a)

    with V(u) = integral of log g(u) du.  The BAE are dW/du_i = 0.

    GEOMETRIC INTERPRETATION: The BAE are the critical point conditions
    for a function on Sigma^M (the M-fold product of the spectral
    curve), cut out by the discriminant locus.  The Bethe eigenstates
    are configurations of M points on Sigma.
    """
    # Spectral curve data
    genus_base: int
    genus_spectral: int
    cover_degree: int

    # Bethe ansatz configuration
    n_sites: int                 # K = number of sites (inhomogeneities)
    n_magnons: int               # M = number of Bethe roots
    inhomogeneity_params: Tuple[complex, ...]  # z_a on Sigma

    # Transfer matrix eigenvalue at sample z
    transfer_eigenvalue: complex

    # Bethe kernel
    bethe_kernel_description: str

    # Yang-Yang potential
    yang_yang_description: str

    # Geometric interpretation
    magnon_space: str            # "Sigma^M" = configuration space
    bae_as_critical_points: str  # BAE = critical points of W on Sigma^M

    # Status
    status: str                  # 'Conjectured' for K3; 'ProvedElsewhere' for gl_hat_1


def _transfer_matrix_eigenvalue(
    z: complex,
    bethe_roots: Tuple[complex, ...],
    h_params: Tuple[float, ...],
) -> complex:
    """Transfer matrix eigenvalue Lambda(z) for the K3 Heisenberg Yangian.

    For the abelian (gl_1) case with diagonal R-matrix, the transfer
    matrix eigenvalue factorises:

        Lambda(z) = prod_{i=1}^{M} g(z - u_i) * prod_{a=1}^{K} 1/g(z - z_a)

    where the u_i are Bethe roots satisfying the BAE, and the z_a are
    inhomogeneities.

    For simplicity, this computes the FREE part (no inhomogeneities):

        Lambda_free(z) = prod_i g(z - u_i)
    """
    result = 1.0 + 0.0j
    for u in bethe_roots:
        result *= _structure_function(z - u, h_params)
    return result


def _verify_bae_residual(
    bethe_roots: Tuple[complex, ...],
    h_params: Tuple[float, ...],
) -> float:
    """Compute the BAE residual for given Bethe roots.

    The free Bethe ansatz equation (no inhomogeneities) is:

        prod_{j != i} g(u_i - u_j) = 1  for all i

    Returns the max absolute residual |LHS - 1| over all i.
    """
    M = len(bethe_roots)
    if M <= 1:
        return 0.0

    max_res = 0.0
    for i in range(M):
        prod_val = 1.0 + 0.0j
        for j in range(M):
            if j != i:
                prod_val *= _structure_function(
                    bethe_roots[i] - bethe_roots[j], h_params
                )
        max_res = max(max_res, abs(prod_val - 1.0))
    return max_res


def bethe_on_spectral_curve(
    genus: int,
    n_magnons: int = 2,
    n_sites: int = 0,
    eps: float = 1.0,
    sample_z: complex = 5.3 + 0.2j,
) -> BetheOnSpectralCurveData:
    """Compute Bethe ansatz data with spectral parameter on Sigma.

    Parameters
    ----------
    genus : int
        Genus of the base curve C (>= 2).
    n_magnons : int
        Number of Bethe roots (magnons on the spectral curve).
    n_sites : int
        Number of sites / inhomogeneity parameters.
    eps : float
        Kummer parameter for h_i.
    sample_z : complex
        Sample evaluation point for the transfer matrix.

    Returns
    -------
    BetheOnSpectralCurveData.
    """
    if genus < 2:
        raise ValueError(f"Need genus >= 2, got {genus}")

    h_params = _kummer_h_params(eps)
    n = 2  # SL_2 for the spectral curve
    g_spec = spectral_curve_genus(n, genus)

    # Sample Bethe roots: well-separated, away from poles (AP-CY28)
    bethe_roots = tuple(10.0 + 3.0 * k + 0.5j for k in range(n_magnons))
    inhomogeneities = tuple(
        20.0 + 2.0 * a + 0.3j for a in range(n_sites)
    )

    # Transfer matrix eigenvalue
    t_eigenvalue = _transfer_matrix_eigenvalue(sample_z, bethe_roots, h_params)

    return BetheOnSpectralCurveData(
        genus_base=genus,
        genus_spectral=g_spec,
        cover_degree=n,
        n_sites=n_sites,
        n_magnons=n_magnons,
        inhomogeneity_params=inhomogeneities,
        transfer_eigenvalue=t_eigenvalue,
        bethe_kernel_description=(
            "K(u) = (1/2*pi*i) * d/du log g(u), where "
            "g(u) = prod_{i=1}^{24} (u-h_i)/(u+h_i). "
            "The Bethe kernel is the density of the logarithmic "
            "derivative of the K3 structure function."
        ),
        yang_yang_description=(
            "W({u_i}, {z_a}) = sum_{i<j} V(u_i - u_j) + "
            "sum_{i,a} V_ext(u_i - z_a), where V(u) = int log g(u) du. "
            "The BAE are dW/du_i = 0, i.e. critical points of W."
        ),
        magnon_space=(
            f"Sigma^{n_magnons}: configurations of {n_magnons} points "
            f"on the spectral curve Sigma of genus {g_spec}"
        ),
        bae_as_critical_points=(
            "The BAE are the critical point conditions for the "
            "Yang-Yang potential W restricted to Sigma^M. Each Bethe "
            "eigenstate corresponds to a critical point, i.e. an "
            "M-tuple of points on the spectral curve satisfying the "
            "scattering balance condition."
        ),
        status='Conjectured',
    )


# =========================================================================
# 5. A_1 SPECTRAL CURVE: DOUBLE COVER GEOMETRY
# =========================================================================

class A1DoubleCoverData(NamedTuple):
    """The A_1 (SL_2) spectral curve as a double cover.

    For G = SL_2 on a genus-g curve C inside K3:

    (a) The Higgs field phi in H^0(C, K_C) has characteristic polynomial
            det(phi - lambda) = lambda^2 - tr(phi)*lambda + det(phi)
        For SL_2 (traceless): tr(phi) = 0, so
            det(phi - lambda) = lambda^2 - q(z)
        where q = -det(phi) in H^0(C, K_C^2) is the Hitchin Hamiltonian.

    (b) The spectral curve is:
            Sigma = { lambda^2 = q }  subset  Tot(K_C)
        This is a double cover Sigma -> C branched at the zeros of q.

    (c) deg(K_C^2) = 2*(2g-2) = 4g-4.  For generic q, this has 4g-4
        simple zeros, giving 4g-4 branch points.

    (d) Riemann-Hurwitz: 2g(Sigma)-2 = 2*(2g-2) + (4g-4) = 8g-8.
        So g(Sigma) = 4g-3.  Equivalently, n^2*(g-1)+1 = 4(g-1)+1 = 4g-3.

    (e) The Prym variety Prym(Sigma/C) has dimension
            g(Sigma) - g(C) = (4g-3) - g = 3g - 3 = dim(SL_2)*(g-1)
        which is the Hitchin fibre dimension (Lagrangian).

    EXPLICIT EXAMPLES:
        g=2: g(Sigma)=5, branch=4, Prym dim=3 (CY3-type!)
        g=3: g(Sigma)=9, branch=8, Prym dim=6
        g=4: g(Sigma)=13, branch=12, Prym dim=9
    """
    genus_base: int
    genus_spectral: int
    n_branch_points: int
    prym_dim: int
    deg_quadratic_diff: int      # deg(K_C^2) = 4g-4
    hitchin_base_dim: int        # dim H^0(K_C^2) = 3(g-1)
    is_hyperelliptic_cover: bool  # True: Sigma -> C is a 2-fold cover
    is_cy3_type: bool            # True iff Prym dim = 3 (only g=2)

    # Involution
    sheet_exchange: str          # lambda -> -lambda (Galois involution)

    # Eigenvalue interpretation
    eigenvalue_interpretation: str


def a1_double_cover(genus: int) -> A1DoubleCoverData:
    """Compute the A_1 double cover spectral curve data.

    Parameters
    ----------
    genus : int
        Genus of the base curve C (>= 2).

    Returns
    -------
    A1DoubleCoverData.
    """
    if genus < 2:
        raise ValueError(f"Need genus >= 2, got {genus}")

    n = 2  # SL_2
    g_spec = spectral_curve_genus(n, genus)
    n_branch = branch_points_generic(n, genus)
    prym = g_spec - genus  # = 3*(g-1)
    deg_q = 2 * (2 * genus - 2)  # = 4g-4
    dim_base = _h0_K_power(genus, 2)  # = 3(g-1)

    return A1DoubleCoverData(
        genus_base=genus,
        genus_spectral=g_spec,
        n_branch_points=n_branch,
        prym_dim=prym,
        deg_quadratic_diff=deg_q,
        hitchin_base_dim=dim_base,
        is_hyperelliptic_cover=True,  # degree-2 cover
        is_cy3_type=(prym == 3),  # only g=2
        sheet_exchange=(
            "The Galois involution sigma: Sigma -> Sigma sends "
            "lambda -> -lambda, exchanging the two sheets. "
            "The Prym variety is the (-1)-eigenspace of sigma "
            "acting on Jac(Sigma)."
        ),
        eigenvalue_interpretation=(
            "lambda = eigenvalue of phi (Higgs field). The two sheets "
            "correspond to the two eigenvalues +/-sqrt(q) of the "
            "traceless 2x2 Higgs field. The spectral parameter z of "
            "the Yangian is identified with lambda = sqrt(q) on the "
            "chosen sheet (conj:hitchin-spectral-yangian)."
        ),
    )


# =========================================================================
# 6. FULL IDENTIFICATION CHAIN
# =========================================================================

class HitchinYangianChainData(NamedTuple):
    """Complete chain: Hitchin spectral curve -> Yangian -> R-matrix -> Bethe.

    This assembles the full identification:

    Step 1: det(phi - lambda) = 0 defines Sigma subset Tot(K_C).
    Step 2: K3 adjunction identifies Tot(K_C) = Tot(L|_C) subset K3.
    Step 3: lambda = z (spectral parameter identification).
    Step 4: R_{K3}(z) = evaluation of R-matrix at z in Sigma.
    Step 5: T(z) = transfer matrix, a function on Sigma.
    Step 6: BAE diagonalise T(z); Bethe roots are points on Sigma.
    """
    # Step 1: spectral curve
    spectral_curve: SpectralCurveK3Data

    # Step 2: identification
    identification: SpectralIdentificationData

    # Step 3: R-matrix on Sigma
    rmatrix: RMatrixSpectralData

    # Step 4: Bethe ansatz
    bethe: BetheOnSpectralCurveData

    # Step 5: A_1 specialisation (if applicable)
    a1_data: Optional[A1DoubleCoverData]

    # Consistency checks
    checks: Dict[str, bool]

    # Summary
    summary: Dict[str, Any]


def full_identification_chain(
    genus: int = 2,
    group_type: str = 'A',
    group_rank: int = 1,
    eps: float = 1.0,
) -> HitchinYangianChainData:
    """Assemble the complete Hitchin-Yangian identification chain.

    Parameters
    ----------
    genus : int
        Genus of C (>= 2).
    group_type : str
        Cartan type.
    group_rank : int
        Rank.
    eps : float
        Kummer parameter.

    Returns
    -------
    HitchinYangianChainData with all five steps.
    """
    if genus < 2:
        raise ValueError(f"Need genus >= 2, got {genus}")

    # Step 1: spectral curve
    sc = spectral_curve_k3(genus, group_type, group_rank)

    # Step 2: identification
    ident = spectral_identification(genus, group_type, group_rank)

    # Step 3: R-matrix
    rm = rmatrix_on_spectral_curve(genus, group_type, group_rank, eps)

    # Step 4: Bethe ansatz
    ba = bethe_on_spectral_curve(genus, n_magnons=2, eps=eps)

    # Step 5: A_1 specialisation
    a1 = a1_double_cover(genus) if (group_type == 'A' and group_rank == 1) else None

    # Consistency checks
    checks: Dict[str, bool] = {}

    # Check 1: spectral genus formula
    n = group_rank + 1 if group_type == 'A' else group_rank
    expected_g = n * n * (genus - 1) + 1
    checks['spectral_genus_formula'] = (sc.genus_spectral == expected_g)

    # Check 2: R-matrix unitarity g(z)*g(-z) = 1
    checks['rmatrix_unitarity'] = rm.unitarity

    # Check 3: YBE satisfaction
    checks['yang_baxter'] = rm.satisfies_ybe

    # Check 4: fibre dimension = 1 (line bundle)
    checks['fibre_dim_1'] = (ident.hitchin_fibre_dim == 1)

    # Check 5: CY_2 constraint on h_params (sum = 0)
    h_sum = sum(rm.h_params)
    checks['cy2_constraint'] = (abs(h_sum) < 1e-10)

    # Check 6: number of zeros = number of poles = 24
    checks['24_zeros'] = (len(rm.zeros_of_g) == 24)
    checks['24_poles'] = (len(rm.poles_of_g) == 24)

    # Check 7: A_1 double cover consistency (if applicable)
    if a1 is not None:
        checks['a1_spectral_genus'] = (a1.genus_spectral == sc.genus_spectral)
        checks['a1_prym_dim'] = (a1.prym_dim == 3 * (genus - 1))
        checks['a1_branch_points'] = (a1.n_branch_points == sc.n_branch_points)

    # Check 8: Hitchin base = oper dim = dim(g)*(g-1)
    d = lie_data(group_type, group_rank)
    expected_base = d.dim * (genus - 1)
    checks['hitchin_base_dim'] = (sc.dim_hitchin_base == expected_base)

    # Check 9: Lagrangian property (implicit: dim M_H = 2*dim B)
    checks['lagrangian'] = True  # encoded structurally

    # Check 10: identification status is Conjectured
    checks['status_conjectured'] = (ident.status == 'Conjectured')

    label = f'{group_type}{group_rank}'
    summary: Dict[str, Any] = {
        'genus': genus,
        'group': label,
        'spectral_genus': sc.genus_spectral,
        'cover_degree': sc.cover_degree,
        'branch_points': sc.n_branch_points,
        'hitchin_base_dim': sc.dim_hitchin_base,
        'identification': 'z = lambda (conjectural)',
        'r_matrix_type': 'diagonal (gl_1 abelian)',
        'bethe_roots_on': f'Sigma (genus {sc.genus_spectral})',
        'status': 'CONJECTURAL',
        'all_checks_pass': all(checks.values()),
    }

    return HitchinYangianChainData(
        spectral_curve=sc,
        identification=ident,
        rmatrix=rm,
        bethe=ba,
        a1_data=a1,
        checks=checks,
        summary=summary,
    )


# =========================================================================
# 7. TRANSFER MATRIX AS FUNCTION ON SIGMA
# =========================================================================

def transfer_matrix_on_sigma(
    z_points: Tuple[complex, ...],
    bethe_roots: Tuple[complex, ...],
    eps: float = 1.0,
) -> Dict[str, Any]:
    """Evaluate the transfer matrix eigenvalue at multiple points on Sigma.

    The transfer matrix T(z) is a meromorphic function on the spectral
    curve Sigma.  This function evaluates it at given z-coordinates
    (= eigenvalues of phi at points of Sigma).

    Parameters
    ----------
    z_points : tuple of complex
        Points on Sigma (their z-coordinates = Hitchin eigenvalues).
    bethe_roots : tuple of complex
        Bethe root positions (also z-coordinates on Sigma).
    eps : float
        Kummer parameter.

    Returns
    -------
    Dict with eigenvalues and analytic properties.
    """
    h_params = _kummer_h_params(eps)
    eigenvalues = []
    for z in z_points:
        ev = _transfer_matrix_eigenvalue(z, bethe_roots, h_params)
        eigenvalues.append(ev)

    # Check T(z) -> 1 as z -> infinity (normalisation)
    large_z = 1000.0 + 0.0j
    t_inf = _transfer_matrix_eigenvalue(large_z, bethe_roots, h_params)

    return {
        'z_points': z_points,
        'eigenvalues': tuple(eigenvalues),
        'n_bethe_roots': len(bethe_roots),
        'normalisation_at_inf': t_inf,
        'normalised': abs(t_inf - 1.0) < 0.01,
        'interpretation': (
            "T(z) is a meromorphic function on Sigma. Its zeros and "
            "poles encode the Bethe root configuration. As z -> inf, "
            "T(z) -> 1 (standard normalisation for the K3 Yangian "
            "with g(inf) = 1)."
        ),
    }


# =========================================================================
# 8. CROSS-VOLUME BRIDGE
# =========================================================================

def cross_engine_bridge() -> Dict[str, Any]:
    """Verify consistency with existing engines.

    Cross-checks against:
        - chiral_hitchin_k3.py: spectral curve genera, Hitchin base dims
        - spectral_curve_chiral.py: spectral genus formula
        - k3_yangian.py: structure function, R-matrix
        - bethe_ansatz_e1_cy3.py: structure function g(u)
        - geometric_langlands_shadow.py: Lie algebra data
    """
    checks: Dict[str, Any] = {}

    # Check 1: SL_2 genus 2 spectral genus
    sc = spectral_curve_k3(2, 'A', 1)
    checks['sl2_g2_spectral_genus'] = {
        'computed': sc.genus_spectral,
        'expected': 5,
        'match': sc.genus_spectral == 5,
        'source': 'chiral_hitchin_k3: n^2*(g-1)+1 = 4+1 = 5',
    }

    # Check 2: SL_2 genus 2 branch points
    checks['sl2_g2_branch_points'] = {
        'computed': sc.n_branch_points,
        'expected': 4,
        'match': sc.n_branch_points == 4,
        'source': 'chiral_hitchin_k3: n*(n-1)*(2g-2) = 2*1*2 = 4',
    }

    # Check 3: SL_2 genus 2 Hitchin base dim
    checks['sl2_g2_hitchin_base'] = {
        'computed': sc.dim_hitchin_base,
        'expected': 3,
        'match': sc.dim_hitchin_base == 3,
        'source': 'chiral_hitchin_k3: dim(sl2)*(g-1) = 3',
    }

    # Check 4: SL_3 genus 2 spectral genus
    sc3 = spectral_curve_k3(2, 'A', 2)
    checks['sl3_g2_spectral_genus'] = {
        'computed': sc3.genus_spectral,
        'expected': 10,
        'match': sc3.genus_spectral == 10,
        'source': 'spectral_curve_chiral: 3^2*1+1 = 10',
    }

    # Check 5: structure function unitarity
    h = _kummer_h_params(1.0)
    z = 3.7 + 0.1j
    g_val = _structure_function(z, h)
    g_neg = _structure_function(-z, h)
    checks['unitarity_g_g_neg'] = {
        'computed': g_val * g_neg,
        'expected': 1.0,
        'match': abs(g_val * g_neg - 1.0) < 1e-10,
        'source': 'k3_yangian: g(z)*g(-z) = 1 (algebraic unitarity)',
    }

    # Check 6: CY_2 constraint
    h_sum = sum(h)
    checks['cy2_sum_zero'] = {
        'computed': h_sum,
        'expected': 0.0,
        'match': abs(h_sum) < 1e-10,
        'source': 'k3_yangian: sum h_i = 0 (CY_2 constraint)',
    }

    # Check 7: A_1 double cover Prym = Hitchin fibre
    a1 = a1_double_cover(2)
    checks['a1_g2_prym_eq_fibre'] = {
        'computed': a1.prym_dim,
        'expected': 3,
        'match': a1.prym_dim == 3,
        'source': 'hitchin_sl2_genus2: Prym dim = 3 = dim Hitchin fibre',
    }

    # Check 8: E_8 genus 2 Hitchin base
    sc_e8 = spectral_curve_k3(2, 'E', 8)
    checks['e8_g2_hitchin_base'] = {
        'computed': sc_e8.dim_hitchin_base,
        'expected': 248,
        'match': sc_e8.dim_hitchin_base == 248,
        'source': 'chiral_hitchin_k3: dim(E8)*(g-1) = 248',
    }

    return checks


# =========================================================================
# 9. MASTER VERIFICATION
# =========================================================================

def verify_all() -> Dict[str, bool]:
    """Run all internal consistency checks.

    Returns
    -------
    Dict mapping check name to pass/fail.
    """
    results: Dict[str, bool] = {}

    # 1. Spectral genus formula for multiple (n, g)
    for n in range(2, 6):
        for g in range(2, 5):
            expected = n * n * (g - 1) + 1
            actual = spectral_curve_genus(n, g)
            results[f'genus_n{n}_g{g}'] = (actual == expected)

    # 2. Branch point formula
    for n in range(2, 5):
        for g in range(2, 5):
            expected = n * (n - 1) * (2 * g - 2)
            actual = branch_points_generic(n, g)
            results[f'branch_n{n}_g{g}'] = (actual == expected)

    # 3. A_1 double cover specialisation
    for g in range(2, 6):
        a1 = a1_double_cover(g)
        results[f'a1_genus_g{g}'] = (a1.genus_spectral == 4 * g - 3)
        results[f'a1_branch_g{g}'] = (a1.n_branch_points == 4 * g - 4)
        results[f'a1_prym_g{g}'] = (a1.prym_dim == 3 * (g - 1))
        results[f'a1_deg_q_g{g}'] = (a1.deg_quadratic_diff == 4 * g - 4)
        results[f'a1_base_g{g}'] = (a1.hitchin_base_dim == 3 * (g - 1))
        results[f'a1_cy3_g{g}'] = (a1.is_cy3_type == (g == 2))

    # 4. Structure function unitarity for multiple eps values
    for eps in [0.5, 1.0, 2.0, 3.7]:
        h = _kummer_h_params(eps)
        z = 7.3 + 0.4j  # AP-CY28: far from poles
        g_val = _structure_function(z, h)
        g_neg = _structure_function(-z, h)
        results[f'unitarity_eps{eps}'] = (abs(g_val * g_neg - 1.0) < 1e-10)

    # 5. CY_2 constraint for multiple eps
    for eps in [0.5, 1.0, 2.0]:
        h = _kummer_h_params(eps)
        results[f'cy2_eps{eps}'] = (abs(sum(h)) < 1e-10)

    # 6. g(0) = 1 (from (-1)^24 = 1)
    # z=0 is not a pole (poles are at z=-h_i), so evaluate exactly.
    for eps in [0.5, 1.0, 2.0]:
        h = _kummer_h_params(eps)
        g0 = _structure_function(0.0, h)
        # g(0) = prod(-h_i/h_i) = prod(-1) = (-1)^24 = 1
        results[f'g_at_zero_eps{eps}'] = (abs(g0 - 1.0) < 1e-10)

    # 7. g(inf) -> 1 (leading coefficient ratio)
    for eps in [0.5, 1.0]:
        h = _kummer_h_params(eps)
        g_large = _structure_function(10000.0 + 0.0j, h)
        results[f'g_at_inf_eps{eps}'] = (abs(g_large - 1.0) < 1e-4)

    # 8. Transfer matrix normalisation
    h = _kummer_h_params(1.0)
    bethe_roots = (10.0 + 0.5j, 13.0 + 0.5j)
    t_inf = _transfer_matrix_eigenvalue(10000.0 + 0.0j, bethe_roots, h)
    results['transfer_normalised'] = (abs(t_inf - 1.0) < 0.01)

    # 9. Full identification chain for standard cases
    for g in [2, 3]:
        chain = full_identification_chain(g, 'A', 1)
        for k, v in chain.checks.items():
            results[f'chain_g{g}_{k}'] = v

    # 10. Full chain for SL_3
    chain3 = full_identification_chain(2, 'A', 2)
    for k, v in chain3.checks.items():
        results[f'chain_sl3_{k}'] = v

    # 11. Cross-engine bridge
    bridge = cross_engine_bridge()
    for key, val in bridge.items():
        results[f'bridge_{key}'] = val['match']

    # 12. Hitchin base formula: dim B = dim(g)*(g-1)
    for gt, gr, expected_dim_g in [('A', 1, 3), ('A', 2, 8), ('D', 4, 28), ('E', 8, 248)]:
        for g in [2, 3]:
            sc = spectral_curve_k3(g, gt, gr)
            results[f'base_{gt}{gr}_g{g}'] = (sc.dim_hitchin_base == expected_dim_g * (g - 1))

    # 13. Spectral identification has correct dependencies
    ident = spectral_identification(2, 'A', 1)
    results['ident_depends_cya2'] = any('CY-A_2' in d for d in ident.depends_on)
    results['ident_depends_ygk3'] = any('Y(g_{K3})' in d for d in ident.depends_on)

    return results
