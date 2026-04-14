r"""Chiral R-matrix from E_3 braiding on C^3: the CFG derivation.

MATHEMATICAL CONTENT
====================

The Costello--Francis--Gwilliam (CFG) programme derives quantum R-matrices
from the E_n braiding on configuration spaces of C^n.  This engine implements
the DIRECT construction of the chiral R-matrix from E_3 holomorphic braiding
on C^3, following the CFG principle: the R-matrix IS the holonomy of the
holomorphic CS flat connection on configuration space.

KEY DISTINCTION: TOPOLOGICAL vs HOLOMORPHIC BRAIDING
=====================================================

In 3d (CFG25 for U_q(g) from CS on R^3):
  - Conf_2(R^3) = {(x_1,x_2) in (R^3)^2 : x_1 != x_2} ~ R^3 x S^2
  - pi_1(Conf_2(R^3)) = 0 (simply connected!)
  - The braiding is NOT topological (no braid group action)
  - Instead: the R-matrix comes from the HOLONOMY of the CS flat connection
    along a path in Conf_2(R^3) that exchanges the two points
  - The holonomy depends on the PATH (not just homotopy class) because
    the connection is flat but the space has pi_2 = Z
  - Result: z-INDEPENDENT R-matrix R(q) (quantum group, topological)

In 6d (this engine, holomorphic theory on C^3):
  - Conf_2(C^3) = {(z_1,z_2) in (C^3)^2 : z_1 != z_2}
  - As a real manifold: Conf_2(R^6) ~ R^6 x S^5, pi_1(S^5) = 0
  - Holomorphically: Conf_2(C^3) ~ C^3 x (C^3 \ {0})
  - The HOLOMORPHIC braiding assigns to each z = z_1 - z_2 in C^3 \ {0}
    a braiding operator R(z)
  - z is the SPECTRAL PARAMETER (Yangian, NOT worldsheet; AP-CY31)
  - Result: z-DEPENDENT R-matrix R(z) (rational, Yangian-type)

THE ORIGIN OF YBE AND ZTE FROM HOMOTOPY
=========================================

The E_n coherence conditions come from the homotopy type of Conf_k(C^n):

  E_2 (n=2): pi_1(Conf_2(C^2)) = Z (braid group)
    => Artin relation: sigma_1 sigma_2 sigma_1 = sigma_2 sigma_1 sigma_2
    => This IS the Yang--Baxter equation for R

  E_3 (n=3): pi_1(Conf_2(C^3)) = 0 (no braiding topologically)
             pi_2(Conf_2(C^3)) = Z (the 2-sphere pi_2(S^5) = 0, but...)
    WAIT: pi_2(S^5) = 0. The nontrivial structure comes from the
    OMEGA-BACKGROUND deformation, not from topology (rem:en-from-dimension).
    The E_3 coherence gives the PARAMETRIC tetrahedron equation on the
    z-dependent R-matrix R(z_1, z_2, z_3) via Conf_3(C^3).

HOLOMORPHIC HOLONOMY CONSTRUCTION
===================================

The holomorphic CS propagator on C^3 is:
  P(z_1, z_2) = Omega^{3,0} wedge 1 / |z_1 - z_2|^4
              = (1 / (4 pi^2)) * dz_1 dz_2 dz_3 / (z_12^a z_12^b z_12^c)

For the Omega-background (h_1, h_2, h_3), h_1 + h_2 + h_3 = 0:

The R-matrix on the charge-1 (Fock) representation is the structure function:
  R^{(1)}(z) = g(z) = prod_i (z - h_i) / (z + h_i)

where z = z_1 - z_2 is the HOLOMORPHIC separation (spectral parameter).

At higher charges, the R-matrix is a MATRIX acting on V tensor V,
constructed from the holonomy of the CS connection on Conf_2(C^3).

THE E_3 TWO-PARAMETER EXTENSION
=================================

C^3 has THREE complex directions. Choosing a Wilson line along z_3 leaves
TWO transverse directions (z_1, z_2). The full E_3 R-matrix depends on
BOTH transverse separations:

  R_ch(u, v) = holonomy along path in Conf_2(C^3) at separation (u, v, *)

At charge 1 (Zamolodchikov factorization):
  R_ch^{(1)}(u, v) = g(u) * g(v) * g(u - v)

The three factors: direction-1 braiding, direction-2 braiding, crossing.

THE K3 RESTRICTION
===================

For K3 x C (or K3 x E), the C^3 geometry is replaced by the product
geometry. The 24 Mukai lattice directions of K3 give 24 equivariant
parameters {h_a}_{a=1,...,24} with sum h_a = 0 (trace-free).

The K3 Yangian structure function is:
  g_{K3}(z) = prod_{a=1}^{24} (z - h_a) / (z + h_a)

This is a degree-(24, 24) rational function satisfying g(z)*g(-z) = 1
(CY inversion from the Mukai lattice structure).

CONVENTIONS
===========
  h_1, h_2, h_3: Omega-background parameters, h_1 + h_2 + h_3 = 0 (CY)
  sigma_2 = h_1 h_2 + h_1 h_3 + h_2 h_3
  sigma_3 = h_1 h_2 h_3 = kappa (Yangian Planck constant)
  z: spectral parameter (Yangian, NOT worldsheet; AP-CY31)
  g(z): one-parameter structure function (rational, Yangian)
  G(x): one-parameter structure function (trigonometric, DIM)
  q_i = e^{h_i}: multiplicative parameters, q_1 q_2 q_3 = 1

AP-CY COMPLIANCE
=================
  AP-CY6/AP-CY14: all d=3 results are CONJECTURAL (CY-A_3 not proved).
  AP-CY20: the (q,t) parameters arise from Omega-background, NOT from
           normal bundle grading directly.
  AP-CY31: z is a Yangian spectral parameter, NOT a worldsheet coordinate.
  AP154: the E_3 here is TOPOLOGICAL (configuration space), not algebraic
         (Deligne). Under formality, they agree rationally.
  AP-CY30: factored S-operator does NOT satisfy ZTE (thm:zte-failure).

MANUSCRIPT REFERENCES
  chapters/theory/en_factorization.tex: conj:topological-e3-comparison
  chapters/theory/quantum_chiral_algebras.tex: conj:6d-boundary-toroidal
  chapters/theory/cy_to_chiral.tex: sec:d3-drinfeld-center, eq:yangian-structure-function

REFERENCES
  Costello, "Supersymmetric gauge theory and the Yangian" (2013)
  Costello-Francis-Gwilliam, "Factorization algebras in QFT" I, II (2021)
  Costello-Gwilliam, "Holomorphic field theories and CS" (2025)
  Maulik-Okounkov, "Quantum groups and quantum cohomology" (2019)
"""

from __future__ import annotations

import math
from typing import Dict, List, Optional, Tuple

import numpy as np


# =========================================================================
# 1. Configuration space topology
# =========================================================================

class ConfigurationSpaceTopology:
    r"""Homotopy type of Conf_k(C^n) and its consequences for E_n braiding.

    The fundamental group pi_1(Conf_2(C^n)) determines whether the braiding
    is topological (nontrivial pi_1) or holomorphic (trivial pi_1, but
    nontrivial higher homotopy or Omega-deformation).

    n=1: Conf_2(C) ~ C x C^* => pi_1 = Z (braid group, E_1 monodromy)
    n=2: Conf_2(C^2) ~ C^2 x (C^2 \ {0}) ~ C^2 x S^3 (real)
         pi_1(S^3) = 0. Braiding from Omega-background, not topology.
    n=3: Conf_2(C^3) ~ C^3 x (C^3 \ {0}) ~ C^3 x S^5 (real)
         pi_1(S^5) = 0. Braiding from Omega-background, not topology.
    """

    def __init__(self, n: int):
        """Initialize for C^n.

        Parameters
        ----------
        n : int
            Complex dimension (1, 2, or 3).
        """
        assert n in (1, 2, 3), f"Supported: n = 1, 2, 3; got {n}"
        self.n = n

    @property
    def real_dim(self) -> int:
        """Real dimension of C^n."""
        return 2 * self.n

    @property
    def conf2_link(self) -> str:
        """The link S^{2n-1} in Conf_2(C^n) ~ C^n x (C^n \\ {0}).

        C^n \\ {0} deformation-retracts onto S^{2n-1}.
        """
        return f"S^{2 * self.n - 1}"

    @property
    def pi1_conf2(self) -> str:
        """pi_1(Conf_2(C^n)) = pi_1(S^{2n-1}).

        S^1: pi_1 = Z (braids)
        S^3: pi_1 = 0
        S^5: pi_1 = 0
        """
        if self.n == 1:
            return "Z"  # S^1
        return "0"  # S^{2n-1} for n >= 2 is simply connected

    @property
    def pi2_conf2(self) -> str:
        """pi_2(Conf_2(C^n)) = pi_2(S^{2n-1}).

        S^1: pi_2 = 0
        S^3: pi_2 = 0
        S^5: pi_2 = 0
        """
        # pi_2(S^k) = 0 for all k >= 1
        return "0"

    @property
    def pi_2n_minus_1_conf2(self) -> str:
        r"""pi_{2n-1}(S^{2n-1}) = Z (the Hurewicz class).

        This is the first nontrivial homotopy group of the link sphere.
        For n=1: pi_1(S^1) = Z (braids).
        For n=2: pi_3(S^3) = Z (Hopf fibration, higher coherence for E_2).
        For n=3: pi_5(S^5) = Z (higher coherence for E_3).
        """
        return "Z"

    @property
    def braiding_type(self) -> str:
        """Type of braiding from the configuration space topology.

        n=1: topological (pi_1 = Z, braid group action)
        n=2: holomorphic (pi_1 = 0, Omega-background gives spectral param u)
        n=3: holomorphic (pi_1 = 0, Omega-background gives params (u,v))
        """
        if self.n == 1:
            return "topological"
        return "holomorphic"

    @property
    def r_matrix_type(self) -> str:
        """Type of R-matrix from the braiding.

        n=1: z-independent (quantum group, q = e^{2 pi i / (k + h^vee)})
        n=2: z-dependent, one spectral param (Yangian)
        n=3: z-dependent, two spectral params (quantum toroidal)
        """
        if self.n == 1:
            return "z-independent (quantum group)"
        elif self.n == 2:
            return "z-dependent, 1 parameter (Yangian)"
        else:
            return "z-dependent, 2 parameters (quantum toroidal)"

    @property
    def en_level(self) -> int:
        """E_n chiral level = complex dimension."""
        return self.n

    @property
    def coherence_equation(self) -> str:
        """The consistency equation from E_n coherence.

        E_1: associativity (no equation on R)
        E_2: Yang--Baxter equation (from pi_1(Conf_3) via braids)
        E_3: parametric tetrahedron equation (from the E_3 structure)
        """
        if self.n == 1:
            return "associativity"
        elif self.n == 2:
            return "Yang-Baxter equation"
        else:
            return "parametric tetrahedron equation"

    def summary(self) -> Dict[str, str]:
        """Summary of configuration space data."""
        return {
            "space": f"C^{self.n}",
            "Conf_2": f"C^{self.n} x (C^{self.n} \\ {{0}})",
            "link": self.conf2_link,
            "pi_1": self.pi1_conf2,
            "pi_2": self.pi2_conf2,
            f"pi_{2*self.n - 1}": self.pi_2n_minus_1_conf2,
            "braiding_type": self.braiding_type,
            "R_matrix_type": self.r_matrix_type,
            "E_n_level": str(self.en_level),
            "coherence": self.coherence_equation,
        }


# =========================================================================
# 2. Structure functions (rational and trigonometric)
# =========================================================================

def structure_function_rational(z: complex, h1: complex, h2: complex,
                                h3: complex = None) -> complex:
    """Rational (Yangian) structure function g(z) = prod_i (z-h_i)/(z+h_i).

    This is the charge-1 R-matrix: the holonomy of the holomorphic CS
    connection along the path from z_2 to z_1 with separation z = z_1 - z_2.

    The SPECTRAL parameter z is a Yangian parameter (AP-CY31), NOT a
    worldsheet insertion coordinate.

    Parameters
    ----------
    z : complex
        Spectral parameter (holomorphic separation).
    h1, h2 : complex
        Omega-background parameters.
    h3 : complex, optional
        Third parameter (default: -h1-h2 from CY condition).
    """
    if h3 is None:
        h3 = -(h1 + h2)
    numer = (z - h1) * (z - h2) * (z - h3)
    denom = (z + h1) * (z + h2) * (z + h3)
    if abs(denom) < 1e-30:
        raise ZeroDivisionError(f"g({z}) pole: denom ~ 0")
    return numer / denom


def structure_function_trig(x: complex, q1: complex, q2: complex,
                            q3: complex = None) -> complex:
    """Trigonometric (DIM) structure function G(x) = prod_i (1-q_i x)/(1-q_i^{-1} x).

    Parameters
    ----------
    x : complex
        Multiplicative spectral parameter (x = e^{eps * z}).
    q1, q2 : complex
        Deformation parameters.
    q3 : complex, optional
        Third parameter (default: 1/(q1*q2) from CY condition).
    """
    if q3 is None:
        q3 = 1.0 / (q1 * q2)
    numer = (1 - q1 * x) * (1 - q2 * x) * (1 - q3 * x)
    denom = (1 - x / q1) * (1 - x / q2) * (1 - x / q3)
    if abs(denom) < 1e-30:
        raise ZeroDivisionError(f"G({x}) pole: denom ~ 0")
    return numer / denom


# =========================================================================
# 3. The holomorphic holonomy R-matrix
# =========================================================================

class HolomorphicHolonomyRMatrix:
    """R-matrix from holomorphic CS holonomy on Conf_2(C^n).

    The R-matrix R(z) at charge 1 is the structure function g(z).
    At higher charges, R(z) is a matrix acting on V tensor V,
    computed from the holonomy of the CS flat connection.

    At n=2 (5d, Yangian): one spectral parameter z.
    At n=3 (6d, toroidal): two spectral parameters (u, v).

    Parameters
    ----------
    h1, h2, h3 : float
        Omega-background parameters with h1 + h2 + h3 = 0.
    """

    def __init__(self, h1: float, h2: float, h3: float = None):
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3 if h3 is not None else -(h1 + h2)
        # Verify CY condition
        assert abs(self.h1 + self.h2 + self.h3) < 1e-12, \
            f"CY violation: h1+h2+h3 = {self.h1 + self.h2 + self.h3}"
        # Yangian Planck constant
        self.kappa = self.h1 * self.h2 * self.h3
        # Symmetric polynomials
        self.sigma2 = (self.h1 * self.h2 + self.h1 * self.h3
                       + self.h2 * self.h3)

    def g(self, z: complex) -> complex:
        """Charge-1 R-matrix: structure function g(z).

        g(z) = (z-h1)(z-h2)(z-h3) / ((z+h1)(z+h2)(z+h3))

        This IS the holonomy of the holomorphic CS flat connection
        along the holomorphic path at separation z in C^3 \\ {0}.
        """
        return structure_function_rational(z, self.h1, self.h2, self.h3)

    # ----- CY identities on g(z) -----

    def verify_unitarity(self, z: complex, tol: float = 1e-10) -> bool:
        """Verify g(z) * g(-z) = 1 (CY inversion / R-matrix unitarity).

        This is the algebraic identity prod_i (z-h_i)(-z-h_i) = prod_i (h_i^2 - z^2),
        which equals the denominator. Holds for ALL h_i (not just CY).
        """
        product = self.g(z) * self.g(-z)
        return abs(product - 1.0) < tol

    def verify_cy_normalization(self, tol: float = 1e-10) -> bool:
        """Verify g(z) -> 1 as z -> infinity (CY condition h1+h2+h3=0).

        The CY condition ensures the leading coefficient of numerator
        and denominator are equal (both z^3), so g(z) -> 1.
        Without CY: g(z) -> 1 trivially since both are degree 3 monic.
        The nontrivial CY content: g(z) = 1 - 2*sigma_2/z^2 + O(1/z^3)
        (the 1/z term vanishes iff h1+h2+h3=0).
        """
        z_large = 1e6
        return abs(self.g(z_large) - 1.0) < tol

    def verify_cy_sign(self, tol: float = 1e-10) -> bool:
        """Verify g(0) = -1 (the CY sign).

        g(0) = (-h1)(-h2)(-h3) / (h1 h2 h3) = -1.
        """
        return abs(self.g(0.0) + 1.0) < tol

    # ----- Classical r-matrix -----

    def classical_r_matrix_residue(self) -> float:
        """The classical r-matrix: r(z) = -sigma_2 / z + O(1).

        From g(z) = 1 + r(z)/z + ..., expanding at z -> infinity:
          g(z) = 1 - 2*sigma_2/z^2 + O(1/z^3)

        The classical r-matrix is:
          r_{cl}(z) = (1/2) * d/dz log g(z)|_{leading}
        which gives the residue -sigma_2.

        Level-prefixed form (HZ-1): r(z) = k * Omega / z with k = -sigma_2.
        """
        return -self.sigma2

    # ----- Charge-2 Yang R-matrix -----

    def yang_r_matrix_4x4(self, z: complex) -> np.ndarray:
        """Charge-2 Yang R-matrix R(z) = (z*Id + kappa*P) / (z + kappa).

        Acts on V tensor V where V = C^2 = span{|row>, |col>} (charge-2 Fock).
        Basis: {|row,row>, |row,col>, |col,row>, |col,col>}.

        The Yang R-matrix is the SIMPLEST nontrivial R-matrix satisfying YBE.
        It arises from the charge-2 sector of the Yangian Y(gl_hat_1).

        Parameters
        ----------
        z : complex
            Spectral parameter (Yangian, NOT worldsheet; AP-CY31).
        """
        # Permutation matrix P on C^2 x C^2
        P = np.array([[1, 0, 0, 0],
                       [0, 0, 1, 0],
                       [0, 1, 0, 0],
                       [0, 0, 0, 1]], dtype=complex)
        Id = np.eye(4, dtype=complex)
        denom = z + self.kappa
        if abs(denom) < 1e-30:
            raise ZeroDivisionError(f"Yang R pole at z = {z}")
        return (z * Id + self.kappa * P) / denom

    def verify_yang_ybe(self, u: complex, v: complex,
                        tol: float = 1e-10) -> Tuple[bool, float]:
        """Verify the Yang--Baxter equation for the charge-2 R-matrix.

        R_12(u-v) R_13(u) R_23(v) = R_23(v) R_13(u) R_12(u-v)

        on (C^2)^{tensor 3} (dim 8).

        This is the E_2 coherence condition from Conf_3(C^2).
        """
        # Embed R_{ij} in 8x8 via tensor product with Id on the third factor
        def _embed_12(R):
            return np.kron(R, np.eye(2, dtype=complex))

        def _embed_23(R):
            return np.kron(np.eye(2, dtype=complex), R)

        def _embed_13(R):
            # R_{13} on basis |abc>: acts on positions 1,3
            out = np.zeros((8, 8), dtype=complex)
            for a in range(2):
                for b in range(2):
                    for c in range(2):
                        idx_in = 4 * a + 2 * b + c
                        for a2 in range(2):
                            for c2 in range(2):
                                idx_out = 4 * a2 + 2 * b + c2
                                # R acts on (a,c) -> (a2,c2)
                                r_idx = 2 * a + c
                                c_idx = 2 * a2 + c2
                                out[idx_out, idx_in] += R[c_idx, r_idx]
            return out

        R12 = self.yang_r_matrix_4x4(u - v)
        R13 = self.yang_r_matrix_4x4(u)
        R23 = self.yang_r_matrix_4x4(v)

        lhs = _embed_12(R12) @ _embed_13(R13) @ _embed_23(R23)
        rhs = _embed_23(R23) @ _embed_13(R13) @ _embed_12(R12)

        diff = np.max(np.abs(lhs - rhs))
        return diff < tol, diff

    def verify_yang_unitarity(self, z: complex,
                              tol: float = 1e-10) -> Tuple[bool, float]:
        """Verify R(z) R(-z) = Id (unitarity from CY inversion g*g(-) = 1)."""
        R_plus = self.yang_r_matrix_4x4(z)
        R_minus = self.yang_r_matrix_4x4(-z)
        product = R_plus @ R_minus
        diff = np.max(np.abs(product - np.eye(4, dtype=complex)))
        return diff < tol, diff

    # ----- Diagonal Fock R-matrix (charge 2) -----

    def fock_r_matrix_diagonal_charge2(self, z: complex) -> np.ndarray:
        """Diagonal R-matrix on the charge-2 Fock space.

        For the affine Yangian on the Fock representation (partition basis),
        the R-matrix is DIAGONAL with entries that are products of g-values:

          R_row(z)  = g(z) * g(z + h2)    (for row-type partition (2))
          R_col(z)  = g(z) * g(z + h1)    (for column-type partition (1,1))

        These are the eigenvalues of the full (intertwiner) R-matrix on
        the charge-2 Fock module.

        Returns a 2x2 diagonal matrix diag(R_row, R_col).
        """
        R_row = self.g(z) * self.g(z + self.h2)
        R_col = self.g(z) * self.g(z + self.h1)
        return np.diag([R_row, R_col])

    def fock_r_unitarity_charge2(self, z: complex,
                                  tol: float = 1e-10) -> Tuple[bool, float]:
        """Verify R(z) R(-z) = Id for diagonal Fock R-matrix at charge 2.

        R_row(z)*R_row(-z) = g(z)g(-z) * g(z+h2)g(-z+h2)
                            = 1 * g(z+h2)*g(-(z+h2) + 2*h2)

        This is NOT simply 1 (unlike the charge-1 case) because
        g(z+h2)*g(-z+h2) != g(z+h2)*g(-(z+h2)) in general.

        At special points (z=0): R_row(0)*R_row(0) = g(0)^2 * g(h2)^2 * ...
        which is nontrivial.
        """
        R_plus = self.fock_r_matrix_diagonal_charge2(z)
        R_minus = self.fock_r_matrix_diagonal_charge2(-z)
        product = R_plus @ R_minus
        diff = np.max(np.abs(product - np.eye(2, dtype=complex)))
        return diff < tol, diff

    # ----- Charge-2 S-matrix (double braiding) -----

    def charge2_s_matrix(self, z: complex) -> np.ndarray:
        """Charge-2 categorical S-matrix from the diagonal Fock R-matrix.

        S_{lam,mu}(z) = R_{lam,mu}(z) * R_{mu,lam}(-z)

        For diagonal R:
          S_row(z) = R_row(z) * R_row(-z) = g(z+h2)*g(h2-z)
          S_col(z) = R_col(z) * R_col(-z) = g(z+h1)*g(h1-z)

        using g(z)*g(-z) = 1 to cancel the g(z)*g(-z) factor.
        """
        S_row = self.g(z + self.h2) * self.g(self.h2 - z)
        S_col = self.g(z + self.h1) * self.g(self.h1 - z)
        return np.diag([S_row, S_col])


# =========================================================================
# 4. E_3 two-parameter R-matrix from holomorphic braiding
# =========================================================================

class E3ChiralRMatrix:
    """E_3 chiral R-matrix from holomorphic braiding on C^3.

    The E_3 R-matrix R_ch(u, v) depends on TWO spectral parameters
    (u, v) arising from the two transverse directions in C^3
    (after choosing a Wilson line along the third direction).

    The key difference from the E_2 case:
      E_2: R(z) from ONE spectral parameter z in C \\ {0}
      E_3: R_ch(u, v) from TWO spectral parameters (u, v) in C^2 \\ {0, diags}

    STATUS: CONJECTURAL (AP-CY6/AP-CY14, depends on CY-A_3).

    Parameters
    ----------
    h1, h2, h3 : float
        Omega-background parameters with h1 + h2 + h3 = 0.
    """

    def __init__(self, h1: float, h2: float, h3: float = None):
        self.holonomy = HolomorphicHolonomyRMatrix(h1, h2, h3)
        self.h1 = self.holonomy.h1
        self.h2 = self.holonomy.h2
        self.h3 = self.holonomy.h3
        self.kappa = self.holonomy.kappa

    def g(self, z: complex) -> complex:
        """Delegate to holonomy structure function."""
        return self.holonomy.g(z)

    # ----- Charge-1 E_3 R-matrix (Zamolodchikov factorization) -----

    def charge1_rmatrix(self, u: complex, v: complex) -> complex:
        """Charge-1 E_3 R-matrix: R_ch^{(1)}(u,v) = g(u) * g(v) * g(u-v).

        The Zamolodchikov factorization at charge 1 is EXACT (scalars commute).

        Three factors:
          g(u): braiding from transverse direction 1
          g(v): braiding from transverse direction 2
          g(u-v): crossing factor (Miki automorphism kernel)
        """
        return self.g(u) * self.g(v) * self.g(u - v)

    def verify_charge1_inversion(self, u: complex, v: complex,
                                  tol: float = 1e-10) -> bool:
        """Verify R_ch(u,v) * R_ch(-u,-v) = 1 (E_3 unitarity).

        Proof: g(u)g(-u) * g(v)g(-v) * g(u-v)g(-(u-v)) = 1*1*1 = 1.
        """
        product = self.charge1_rmatrix(u, v) * self.charge1_rmatrix(-u, -v)
        return abs(product - 1.0) < tol

    def verify_charge1_miki_exchange(self, u: complex, v: complex,
                                      tol: float = 1e-10) -> Tuple[bool, float]:
        """Verify R_ch(u,v) / R_ch(v,u) = g(u-v)^2 (Miki exchange phase).

        R_ch(u,v) / R_ch(v,u) = [g(u)g(v)g(u-v)] / [g(v)g(u)g(v-u)]
                               = g(u-v) / g(v-u)
                               = g(u-v) / g(-(u-v))
                               = g(u-v)^2      (using g(z)*g(-z)=1 => g(-z)=1/g(z))

        This is the BRAIDING PHASE: it measures the asymmetry between
        the two transverse directions under the Miki automorphism (SL_2(Z)
        acting on the two loop directions of the quantum toroidal algebra).
        """
        R_uv = self.charge1_rmatrix(u, v)
        R_vu = self.charge1_rmatrix(v, u)
        if abs(R_vu) < 1e-30:
            return False, float('inf')
        ratio = R_uv / R_vu
        expected = self.g(u - v) ** 2
        diff = abs(ratio - expected)
        return diff < tol, diff

    def verify_charge1_tetrahedron(
        self, u1: complex, v1: complex, u2: complex, v2: complex,
        tol: float = 1e-10,
    ) -> Tuple[bool, float]:
        """Verify the parametric tetrahedron equation at charge 1.

        At charge 1, all R-matrices are SCALARS, so the tetrahedron equation
        reduces to commutativity of multiplication and is AUTOMATICALLY SATISFIED.

        The constraint surface:
          u3 = u1 - u2, v3 = v1 - v4, u4 = v2
        The parametric tetrahedron:
          R(u1,v1) R(u2,v2) R(u3,v3) R(u4,v4)
            = R(u4,v4) R(u3,v3) R(u2,v2) R(u1,v1)

        For scalars: both sides = R(u1,v1)*R(u2,v2)*R(u3,v3)*R(u4,v4).
        """
        # Constraint surface
        u3 = u1 - u2
        v4 = v1 - (u1 - u2)  # from v3 = v1 - v4 and u3 = u1 - u2
        u4 = v2
        v3 = v1 - v4

        R1 = self.charge1_rmatrix(u1, v1)
        R2 = self.charge1_rmatrix(u2, v2)
        R3 = self.charge1_rmatrix(u3, v3)
        R4 = self.charge1_rmatrix(u4, v4)

        lhs = R1 * R2 * R3 * R4
        rhs = R4 * R3 * R2 * R1

        diff = abs(lhs - rhs)
        return diff < tol, diff

    # ----- Charge-2 E_3 R-matrix (Zamolodchikov factorization) -----

    def charge2_rmatrix_zamolodchikov(self, u: complex, v: complex) -> np.ndarray:
        """Charge-2 E_3 R-matrix via Zamolodchikov factorization.

        R_ch^{(2)}(u,v) = R(u) * R(v) * R(u-v)

        where R(z) is the charge-2 diagonal Fock R-matrix.

        STATUS: this is the LEADING APPROXIMATION at charge 2.
        The full E_3 R-matrix requires corrections from the tetrahedron
        equation (thm:zte-failure, AP-CY30).
        """
        Ru = self.holonomy.fock_r_matrix_diagonal_charge2(u)
        Rv = self.holonomy.fock_r_matrix_diagonal_charge2(v)
        Ruv = self.holonomy.fock_r_matrix_diagonal_charge2(u - v)
        return Ru @ Rv @ Ruv

    def charge2_s_matrix_e3(self, u: complex, v: complex) -> np.ndarray:
        """E_3 categorical S-matrix at charge 2.

        S^{E_3}(u,v) = S(u) * S(v) * S(u-v)

        where S(z) is the charge-2 E_2 S-matrix.
        """
        Su = self.holonomy.charge2_s_matrix(u)
        Sv = self.holonomy.charge2_s_matrix(v)
        Suv = self.holonomy.charge2_s_matrix(u - v)
        return Su @ Sv @ Suv

    def verify_charge2_inversion(self, u: complex, v: complex,
                                  tol: float = 1e-10) -> Tuple[bool, float]:
        """Verify R_ch(u,v) R_ch(-u,-v) = Id at charge 2 (E_3 unitarity).

        For the diagonal Fock R-matrix:
          R_ch(u,v) R_ch(-u,-v) = [R(u)R(v)R(u-v)] [R(-u)R(-v)R(-(u-v))]

        For diagonal matrices, this factorizes entry-by-entry.
        Each diagonal entry of R(z)*R(-z) = g_lam(z)*g_lam(-z).
        But g_lam(z)*g_lam(-z) != 1 in general for charge >= 2.
        """
        R_plus = self.charge2_rmatrix_zamolodchikov(u, v)
        R_minus = self.charge2_rmatrix_zamolodchikov(-u, -v)
        product = R_plus @ R_minus
        diff = np.max(np.abs(product - np.eye(2, dtype=complex)))
        return diff < tol, diff


# =========================================================================
# 5. Dimensional hierarchy: 3d -> 5d -> 6d
# =========================================================================

class DimensionalHierarchy:
    """The CFG dimensional hierarchy for R-matrices.

    3d hol CS on C x R   -> E_1 Kac-Moody          -> no R-matrix
    5d hol CS on C^2 x R -> E_2 Yangian             -> R(z) one param
    6d hol theory on C^3  -> E_3 quantum toroidal   -> R(u,v) two params

    The key point: higher dimension gives MORE spectral parameters
    because there are more transverse directions, hence a richer
    R-matrix.  The "loss" is that pi_1(Conf_2) becomes trivial,
    so the braiding is holomorphic (z-dependent) not topological.

    Parameters
    ----------
    h1, h2, h3 : float
        Omega-background parameters with h1 + h2 + h3 = 0.
    """

    def __init__(self, h1: float, h2: float, h3: float = None):
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3 if h3 is not None else -(h1 + h2)
        assert abs(self.h1 + self.h2 + self.h3) < 1e-12

    def e1_kac_moody_level(self) -> float:
        """E_1 Kac-Moody level k = -sigma_2 = h1*h2 + h1*h3 + h2*h3.

        The 3d holomorphic CS on C x R produces Kac-Moody V_k(g)
        at level k = -sigma_2.  No R-matrix at E_1 (monoidal, no braiding).
        """
        return -(self.h1 * self.h2 + self.h1 * self.h3 + self.h2 * self.h3)

    def e2_yangian_structure_function(self, z: complex) -> complex:
        """E_2 Yangian structure function g(z) from 5d hol CS on C^2 x R.

        The R-matrix depends on ONE spectral parameter z (the holomorphic
        separation in the transverse C direction).
        """
        return structure_function_rational(z, self.h1, self.h2, self.h3)

    def e3_toroidal_structure_function(self, u: complex,
                                        v: complex) -> complex:
        """E_3 quantum toroidal structure function from 6d theory on C^3.

        R_ch(u,v) = g(u) * g(v) * g(u-v)

        The R-matrix depends on TWO spectral parameters (u,v)
        from the two transverse directions.
        """
        g = lambda z: structure_function_rational(z, self.h1, self.h2, self.h3)
        return g(u) * g(v) * g(u - v)

    def verify_dimensional_consistency(self, z: complex,
                                        tol: float = 1e-10) -> Dict[str, bool]:
        """Verify consistency of the dimensional hierarchy.

        Setting v=0 in the E_3 structure function should recover E_2:
          R_ch(u, 0) = g(u) * g(0) * g(u) = g(u) * (-1) * g(u) = -g(u)^2

        This is NOT simply g(u) -- there is a sign and squaring.
        The correct restriction E_3 -> E_2 is obtained by taking v = 0
        AND dividing by g(0) = -1:
          R_ch(u, 0) / g(0) = g(u) * g(u) = g(u)^2

        At the level of CONFIGURATION SPACES:
          Conf_2(C^3) projected to Conf_2(C^2 x {0}) gives Conf_2(C^2)
          but the transverse C direction contributes a factor g(0) = -1.
        """
        results = {}

        # E_2 value
        g_z = self.e2_yangian_structure_function(z)

        # E_3 at v=0
        R_ch_v0 = self.e3_toroidal_structure_function(z, 0.0)

        # g(0) = -1
        g_0 = self.e2_yangian_structure_function(0.0)
        results["g(0) = -1"] = abs(g_0 + 1.0) < tol

        # R_ch(u, 0) = g(u) * g(0) * g(u) = -g(u)^2
        results["R_ch(u,0) = -g(u)^2"] = abs(R_ch_v0 - (-g_z ** 2)) < tol

        # Normalized projection: R_ch(u,0) / g(0) = g(u)^2
        results["R_ch(u,0)/g(0) = g(u)^2"] = abs(R_ch_v0 / g_0 - g_z ** 2) < tol

        return results

    def verify_miki_s3_symmetry(self, u: complex, v: complex,
                                 tol: float = 1e-10) -> Dict[str, bool]:
        """Verify S_3 symmetry of the E_3 structure function.

        The Miki automorphism is the S-transformation in SL_2(Z) acting
        on the two loop directions. The full symmetry group is S_3,
        generated by:
          sigma_12: (u, v) -> (v, u)  (exchange of transverse directions)
          sigma_23: (u, v) -> (u, u-v) (shift by crossing)

        At the level of g(u)*g(v)*g(u-v):
          sigma_12: g(v)*g(u)*g(v-u) = g(u)*g(v)*g(v-u)
                  = g(u)*g(v)*g(u-v) * [g(v-u)/g(u-v)]
                  = R_ch(u,v) * g(v-u)/g(u-v)
                  = R_ch(u,v) * g(u-v)^{-2} * g(u-v) * g(v-u)
                  ... this is the Miki exchange.

        Instead of full S_3 on R_ch, we check that the ABSOLUTE VALUE
        |R_ch| is S_3-invariant (the phase carries the braiding data):
          |R_ch(u,v)| = |R_ch(v,u)| fails in general
          |R_ch(u,v)|^2 = |R_ch(v,u)|^2 should hold if |g(z)| = |g(-z)| ... no.

        Actually S_3 acts on the PARAMETERS (h_1,h_2,h_3), not on (u,v).
        Check: R_ch is S_3-symmetric under permutation of (h_1,h_2,h_3).
        """
        results = {}

        g12 = structure_function_rational(u, self.h1, self.h2, self.h3)
        g21 = structure_function_rational(u, self.h2, self.h1, self.h3)
        results["g(z) S_3-sym in h: (12)"] = abs(g12 - g21) < tol

        g13 = structure_function_rational(u, self.h3, self.h2, self.h1)
        results["g(z) S_3-sym in h: (13)"] = abs(g12 - g13) < tol

        # R_ch is S_3-symmetric in (h1,h2,h3)
        R_original = self.e3_toroidal_structure_function(u, v)
        R_perm = structure_function_rational(u, self.h2, self.h1, self.h3) \
            * structure_function_rational(v, self.h2, self.h1, self.h3) \
            * structure_function_rational(u - v, self.h2, self.h1, self.h3)
        results["R_ch S_3-sym in h: (12)"] = abs(R_original - R_perm) < tol

        return results


# =========================================================================
# 6. K3 Yangian restriction
# =========================================================================

class K3YangianRMatrix:
    """R-matrix for the K3 Yangian from restricting C^3 -> K3 x C.

    For K3 x C (or K3 x E), the 24 Mukai lattice directions give
    24 equivariant parameters {h_a}_{a=1,...,24}.

    The K3 Yangian structure function is:
      g_{K3}(z) = prod_{a=1}^{24} (z - h_a) / (z + h_a)

    This is a degree-(24,24) rational function satisfying:
      g_{K3}(z) * g_{K3}(-z) = 1  (CY inversion)
      g_{K3}(0) = (-1)^{24} = 1   (EVEN rank: g(0) = +1, not -1!)

    The Mukai lattice is Lambda = U^3 + (-E_8)^2 (signature (4,20)).
    The 24 parameters h_a are the eigenvalues of the Cartan matrix
    of the Mukai lattice (or more precisely, a choice of equivariant
    splitting of the K3 tangent bundle).

    STATUS: CONJECTURAL (AP-CY14, depends on CY-A_3).

    Parameters
    ----------
    h_values : list of float
        The 24 equivariant parameters with sum(h_values) = 0.
    """

    def __init__(self, h_values: List[float] = None):
        if h_values is None:
            # Default: simplest nontrivial choice with sum = 0
            # Use paired values h_a = -h_{a+12} for a=1,...,12
            h_values = []
            for k in range(1, 13):
                h_values.append(float(k))
                h_values.append(float(-k))
        assert len(h_values) == 24, f"K3 Mukai lattice requires 24 parameters; got {len(h_values)}"
        total = sum(h_values)
        assert abs(total) < 1e-10, f"CY condition: sum(h_a) = {total} != 0"
        self.h_values = list(h_values)
        self.rank = 24

    def g_k3(self, z: complex) -> complex:
        """K3 Yangian structure function.

        g_{K3}(z) = prod_{a=1}^{24} (z - h_a) / (z + h_a)

        Degree (24, 24) rational function.
        """
        numer = 1.0 + 0j
        denom = 1.0 + 0j
        for h in self.h_values:
            numer *= (z - h)
            denom *= (z + h)
        if abs(denom) < 1e-30:
            raise ZeroDivisionError(f"g_K3({z}) pole")
        return numer / denom

    def verify_unitarity(self, z: complex, tol: float = 1e-10) -> bool:
        """Verify g_{K3}(z) * g_{K3}(-z) = 1."""
        return abs(self.g_k3(z) * self.g_k3(-z) - 1.0) < tol

    def verify_even_rank_sign(self, tol: float = 1e-10) -> bool:
        """Verify g_{K3}(0) = +1 (even rank, 24 parameters).

        g(0) = prod (-h_a / h_a) = prod (-1) = (-1)^{24} = +1.

        Contrast with C^3: g(0) = (-1)^3 = -1.
        This is a KEY difference between the C^3 and K3 cases.
        """
        return abs(self.g_k3(0.0) - 1.0) < tol

    def verify_degree(self, tol: float = 1e-10) -> bool:
        """Verify g_{K3}(z) -> 1 as z -> infinity (degree (24,24)).

        The sum condition sum(h_a) = 0 ensures the subleading 1/z
        term vanishes (just as h1+h2+h3=0 does for C^3).
        """
        z_large = 1e8 + 1e7j
        return abs(self.g_k3(z_large) - 1.0) < tol

    def two_param_rmatrix(self, u: complex, v: complex) -> complex:
        """Two-parameter E_3 R-matrix for K3.

        R_{K3,ch}(u,v) = g_{K3}(u) * g_{K3}(v) * g_{K3}(u-v)

        Zamolodchikov factorization for the K3 Yangian.
        """
        return self.g_k3(u) * self.g_k3(v) * self.g_k3(u - v)

    def verify_k3_inversion(self, u: complex, v: complex,
                             tol: float = 1e-10) -> bool:
        """Verify R_{K3,ch}(u,v) * R_{K3,ch}(-u,-v) = 1."""
        product = self.two_param_rmatrix(u, v) * self.two_param_rmatrix(-u, -v)
        return abs(product - 1.0) < tol


# =========================================================================
# 7. The 3d vs 6d comparison: topological vs rational R-matrix
# =========================================================================

class TopologicalVsRational:
    """Compare the 3d (topological) and 6d (rational) R-matrices.

    3d hol CS on R^3 (CFG25):
      - Conf_2(R^3) ~ R^3 x S^2
      - pi_1(S^2) = 0: no topological braiding
      - The R-matrix R(q) is z-INDEPENDENT (quantum group)
      - q = e^{2 pi i / (k + h^vee)} (from the Kac-Moody level)
      - R(q) satisfies YBE (E_2 coherence)

    6d hol theory on C^3 (this engine):
      - Conf_2(C^3) ~ C^3 x (C^3 \\ {0})
      - pi_1 = 0: no topological braiding
      - The R-matrix R(z) is z-DEPENDENT (Yangian)
      - z = spectral parameter from holomorphic separation
      - R(z) satisfies YBE (E_2) and parametric ZTE (E_3)

    THE KEY DISTINCTION:
      3d: quantization parameter q lives in C^* (one number)
      6d: spectral parameter z lives in C^3 \\ {0} (continuous family)

    The Yangian R(z) DEGENERATES to the quantum group R(q) in the
    trigonometric limit (compactification C -> C^* -> C/Lambda).

    CONVENTION NOTE: The trigonometric G(x) = prod (1-q_i x)/(1-x/q_i)
    reduces to 1/g(z) (not g(z)) in the rational limit eps -> 0.
    This is a numerator/denominator swap between the two conventions.
    """

    def __init__(self, h1: float, h2: float, h3: float = None):
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3 if h3 is not None else -(h1 + h2)

    def rational_r_charge1(self, z: complex) -> complex:
        """6d rational (Yangian) R-matrix at charge 1."""
        return structure_function_rational(z, self.h1, self.h2, self.h3)

    def trigonometric_r_charge1(self, x: complex) -> complex:
        """5d trigonometric (DIM) R-matrix at charge 1.

        G(x) = prod_i (1 - q_i x) / (1 - q_i^{-1} x)
        with q_i = e^{h_i}.
        """
        q1 = np.exp(self.h1)
        q2 = np.exp(self.h2)
        q3 = np.exp(self.h3)
        return structure_function_trig(x, q1, q2, q3)

    def verify_rational_limit(self, z: complex, eps: float = 1e-4,
                               tol: float = 1e-3) -> Tuple[bool, float]:
        """Verify that the trigonometric R-matrix reduces to the rational one.

        In the limit eps -> 0 with x = e^{eps*z}, q_i = e^{eps*h_i}:

          G(x; q_i) = prod (1 - q_i x)/(1 - x/q_i)
                    -> prod (-(h_i + z))/(-(z - h_i))
                    = prod (z + h_i)/(z - h_i)
                    = 1 / g(z)

        The convention difference: the trigonometric structure function
        G(x) has numerator zeros at x = 1/q_i (z = -h_i in rat. limit)
        and denominator poles at x = q_i (z = h_i). This INVERTS the
        rational convention where g(z) has zeros at z = h_i and poles
        at z = -h_i. So G_trig -> 1/g_rat as eps -> 0.

        We verify this inversion relation at small eps.
        """
        g_rat = structure_function_rational(z, self.h1, self.h2, self.h3)
        g_rat_inv = 1.0 / g_rat  # The correct target

        q1 = np.exp(eps * self.h1)
        q2 = np.exp(eps * self.h2)
        q3 = np.exp(eps * self.h3)
        x = np.exp(eps * z)
        G_trig = structure_function_trig(x, q1, q2, q3)

        diff = abs(g_rat_inv - G_trig)
        return diff < tol, diff


# =========================================================================
# 8. Summary and verification suite
# =========================================================================

def full_verification(h1: float = 1.3, h2: float = -0.5,
                      h3: float = None,
                      tol: float = 1e-8) -> Dict[str, bool]:
    """Run the full verification suite for the chiral R-matrix from E_3 braiding.

    Test points chosen to avoid poles at z = +/- h_i (AP-CY28):
    h = (1.3, -0.5, -0.8), poles at z = +/-1.3, +/-0.5, +/-0.8.
    Test spectral parameters: u = 3.7, v = 2.1 (far from all poles).

    Returns a dict of test_name -> pass/fail.
    """
    if h3 is None:
        h3 = -(h1 + h2)

    results = {}

    # -- Configuration space topology --
    for n in (1, 2, 3):
        cs = ConfigurationSpaceTopology(n)
        results[f"C^{n} E_n level = {n}"] = (cs.en_level == n)
        if n == 1:
            results["C^1 pi_1 = Z"] = (cs.pi1_conf2 == "Z")
        else:
            results[f"C^{n} pi_1 = 0"] = (cs.pi1_conf2 == "0")

    # -- Holomorphic holonomy R-matrix --
    hol = HolomorphicHolonomyRMatrix(h1, h2, h3)
    # AP-CY28: test points far from poles +/-h_i
    z_test = 3.7 + 1.1j
    u_test = 3.7 + 0.5j
    v_test = 2.1 - 0.3j

    results["g(z)*g(-z) = 1 (unitarity)"] = hol.verify_unitarity(z_test)
    results["g(inf) -> 1 (CY normalization)"] = hol.verify_cy_normalization()
    results["g(0) = -1 (CY sign)"] = hol.verify_cy_sign()

    # Yang R-matrix YBE
    ybe_pass, ybe_diff = hol.verify_yang_ybe(u_test, v_test, tol)
    results["Yang R-matrix: YBE satisfied"] = ybe_pass

    # Yang R-matrix unitarity
    yang_unit_pass, yang_unit_diff = hol.verify_yang_unitarity(z_test, tol)
    results["Yang R-matrix: R(z)R(-z) = Id"] = yang_unit_pass

    # -- E_3 chiral R-matrix --
    e3 = E3ChiralRMatrix(h1, h2, h3)

    results["R_ch(u,v)*R_ch(-u,-v) = 1 (charge 1)"] = e3.verify_charge1_inversion(
        u_test, v_test, tol)

    miki_pass, miki_diff = e3.verify_charge1_miki_exchange(u_test, v_test, tol)
    results["Miki exchange: R_ch(u,v)/R_ch(v,u) = g(u-v)^2"] = miki_pass

    tet_pass, tet_diff = e3.verify_charge1_tetrahedron(u_test, v_test,
                                                         u_test - 1.0, v_test + 0.5,
                                                         tol)
    results["Parametric tetrahedron (charge 1, trivial)"] = tet_pass

    # -- Dimensional hierarchy --
    dh = DimensionalHierarchy(h1, h2, h3)
    dim_results = dh.verify_dimensional_consistency(z_test, tol)
    results.update(dim_results)

    s3_results = dh.verify_miki_s3_symmetry(u_test, v_test, tol)
    results.update(s3_results)

    # -- K3 Yangian --
    k3 = K3YangianRMatrix()  # Default paired parameters
    z_k3_test = 25.0 + 7.0j  # Far from all poles (poles at +/-1,...,+/-12)
    u_k3_test = 25.0 + 3.0j
    v_k3_test = 17.0 - 2.0j

    results["K3: g(z)*g(-z) = 1"] = k3.verify_unitarity(z_k3_test)
    results["K3: g(0) = +1 (even rank)"] = k3.verify_even_rank_sign()
    results["K3: g(inf) -> 1 (degree (24,24))"] = k3.verify_degree()
    results["K3: R_ch(u,v)*R_ch(-u,-v) = 1"] = k3.verify_k3_inversion(
        u_k3_test, v_k3_test, tol)

    # -- Topological vs rational --
    tvr = TopologicalVsRational(h1, h2, h3)
    rat_lim_pass, rat_lim_diff = tvr.verify_rational_limit(z_test, eps=1e-4, tol=1e-3)
    results["Rational limit: trig -> rat as eps -> 0"] = rat_lim_pass

    return results


def summary() -> str:
    """Print a summary of the engine results."""
    results = full_verification()
    lines = ["Chiral R-matrix from E_3 braiding: verification summary",
             "=" * 60]
    n_pass = sum(1 for v in results.values() if v)
    n_total = len(results)
    for name, passed in results.items():
        status = "PASS" if passed else "FAIL"
        lines.append(f"  [{status}] {name}")
    lines.append(f"\n{n_pass}/{n_total} tests passed.")
    return "\n".join(lines)
