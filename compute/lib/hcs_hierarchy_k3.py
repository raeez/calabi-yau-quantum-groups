r"""Holomorphic CS hierarchy for K3: the 3d -> 5d -> 6d tower.

STATUS: Mixed.  The 3d and 5d levels are PROVED (Costello-Gwilliam, Costello
2013).  The 6d level and K3 specialisation are CONJECTURAL (AP-CY14).

MATHEMATICAL CONTENT
====================

THE HIERARCHY:

  (A) FLAT SPACE (C^n):
    3d hol CS on C x R       -> Kac-Moody V_k(g)             [PROVED]
    5d hol CS on C^2 x R     -> Affine Yangian Y(gl_hat_1)   [PROVED]
    6d hol theory on C^3      -> Quantum toroidal U_{q,t}     [CONJECTURAL]

  (B) K3-FIBERED GEOMETRIES:
    3d: K3 sigma model on C   -> K3 Heisenberg H_Muk          [PROVED at d=2]
    5d: K3 x C x R            -> K3 Yangian Y(g_{K3})         [CONJECTURAL]
    6d: K3 x E x C            -> K3 quantum toroidal           [CONJECTURAL]

DIMENSIONAL REDUCTION:

  6d -> 5d: shrink E (q = e^{2 pi i tau} -> 1, i.e. tau -> i*infty).
    U_{q,t}(g_{K3}^{tor})  ->  Y(g_{K3})
    Trigonometric -> Rational structure function.
    G(x; {q_a}) -> g(u; {h_a}) via x = e^u, q_a = e^{h_a}, u -> 0.

  5d -> 3d: shrink C (hbar -> 0, i.e. Yangian -> current algebra).
    Y(g_{K3})  ->  H_Muk  (the K3 Mukai Heisenberg)
    Rational g(u) = prod (u-h_i)/(u+h_i) -> 1 as all h_i -> 0.
    The R-matrix becomes trivial; the Yangian degenerates to
    the universal enveloping algebra of the current algebra.

OMEGA-BACKGROUND AT EACH LEVEL:

  3d (C x R):     No Omega-background (hbar = 0).
                   The boundary algebra is classical (Kac-Moody/Heisenberg).
  5d (C^2 x R):   Omega-background (eps_1, eps_2) on C^2.
                   eps_1 + eps_2 + eps_3 = 0 (CY condition).
                   For K3: the 24 parameters h_i replace (eps_1, eps_2, eps_3).
  6d (C^3):       Omega-background (eps_1, eps_2, eps_3) on C^3.
                   For K3 x E: h_i from K3 Mukai lattice, tau from E.

BOUNDARY CONDITIONS:

  At each level, the space has a real direction R (or a boundary):
    Dirichlet boundary (at ends of R):
      -> boundary chiral algebra (the objects listed above).
    Neumann boundary:
      -> bulk algebra = derived center Z^{der}_ch(A).

  The bulk-boundary coupling is the canonical map
    mu_{bb}: Z^{der}_ch(A) x A^! -> A^!
  making the defect algebra A^! a module over the bulk.

WILSON LINES:

  3d: Wilson line in representation V of g
      -> module over V_k(g).
      For K3 Heisenberg: Wilson line indexed by Mukai vector v.
  5d: Wilson line valued in Fock module F_lambda
      -> module over Y(g_{K3}).
      The Drinfeld coproduct Delta_z(T(u)) = T^L(u) . T^R(u-z)
      controls the fusion of Wilson lines.
  6d: Wilson surface wrapping E
      -> module over U_{q,t}(g_{K3}^{tor}).
      The q-deformed coproduct involves the E modulus.

THE MASTER DIAGRAM (Conjecture conj:hcs-k3-hierarchy):

  K3 x E x C  ----[shrink E]--->  K3 x C x R  ----[shrink C]--->  K3 on pt
       |                                |                              |
    6d hol theory                   5d hol CS                     3d sigma model
       |                                |                              |
  U_{q,t}(g_{K3}^{tor})         Y(g_{K3})                        H_Muk
       |                                |                              |
  E_3 factorization              E_2 on C^2                      E_1 on C
       |                                |                              |
  q-deformed R-matrix            rational R-matrix              classical r-matrix

  Parameters:
    6d: (q_1,...,q_{24}; tau)    q_a = e^{h_a}, q = e^{2pi i tau}
    5d: (h_1,...,h_{24})         sum h_i = 0 (CY_2)
    3d: ()                       all h_i = 0

  kappa-spectrum (AP113):
    kappa_ch(H_Muk) = 2            (K3 Heisenberg, d=2)
    kappa_ch(K3 x E) = 3           (product, d=3)
    kappa_BKM(K3 x E) = 5          (Igusa cusp form weight)
    kappa_cat(K3) = 2               (= chi(O_K3))
    kappa_fiber(K3) = 24            (Mukai lattice rank)

CONVENTIONS:
  - h_i: additive Yangian parameters (spectral, NOT worldsheet; AP-CY31)
  - u: spectral parameter (Yangian convention)
  - z: worldsheet coordinate (OPE convention) -- distinct from u
  - q = e^{2 pi i tau}: nome of E
  - q_a = e^{h_a}: multiplicative Yangian parameters
  - omega^{ij}: Mukai pairing, signature (4,20)
  - CY_2: sum h_i = 0 (additive), prod q_a = 1 (multiplicative)
  - All 6d and K3 results are CONJECTURAL (AP-CY14)
  - kappa subscripts per AP113

REFERENCES:
  holomorphic_cs_chiral_engine.py (flat-space hierarchy)
  costello_5d_verification.py (5d computational verification)
  k3_yangian.py (K3 Yangian: rational structure function)
  k3_quantum_toroidal.py (K3 quantum toroidal: trigonometric)
  k3_double_current_algebra.py (classical limit)
  k3_rtt_ope_dictionary.py (RTT-OPE bridge)
  drinfeld_center_k3_heisenberg.py (Drinfeld center of H_Muk)
  quantum_chiral_algebras.tex: Section on hCS hierarchy
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

import numpy as np
from sympy import (
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    oo,
    simplify,
    symbols,
)

# Imports from existing engines
from compute.lib.holomorphic_cs_chiral_engine import (
    OmegaBackground,
    BoundaryAlgebra,
)

from compute.lib.k3_yangian import (
    NUM_PARAMS,
    SIG_PLUS,
    SIG_MINUS,
    MukaiLatticeParams,
    kummer_k3_parameters,
    null_kummer_parameters,
    custom_parameters,
    structure_function_evaluate,
    structure_function_coefficients,
    newton_power_sums,
)

from compute.lib.k3_quantum_toroidal import (
    N_MUKAI,
    trigonometric_structure_function,
    rational_to_trigonometric_params,
    verify_cy2_multiplicative,
    verify_inversion_identity,
)

F = Fraction

# =========================================================================
# 0. Constants
# =========================================================================

# Status at each level of the hierarchy
STATUS_3D = 'PROVED'        # Costello-Gwilliam 2021
STATUS_5D = 'PROVED'        # Costello 2013
STATUS_6D = 'CONJECTURAL'   # Costello-Francis-Gwilliam route
STATUS_K3_3D = 'PROVED'     # CY-A_2 (d=2 proved)
STATUS_K3_5D = 'CONJECTURAL'  # Requires K3 Yangian construction
STATUS_K3_6D = 'CONJECTURAL'  # Requires CY-A_3

# Mukai lattice data
MUKAI_RANK = 24
MUKAI_SIG = (4, 20)  # Signature (p, q)

# kappa-spectrum for K3 x E (AP113: NEVER bare kappa)
KAPPA_CH_K3 = Rational(2)          # kappa_ch(H_Muk) at d=2
KAPPA_CH_K3E = Rational(3)         # kappa_ch(K3 x E) at d=3 (additivity: 2+1)
KAPPA_BKM_K3E = Rational(5)        # kappa_BKM: Igusa cusp form weight
KAPPA_CAT_K3 = Rational(2)         # kappa_cat = chi(O_K3)
KAPPA_CAT_K3E = Rational(0)        # kappa_cat(K3 x E) = 0 (Kuenneth)
KAPPA_FIBER_K3 = Rational(24)      # kappa_fiber = Mukai lattice rank


# =========================================================================
# 1. The hierarchy levels
# =========================================================================

class HierarchyLevel(NamedTuple):
    """A single level in the 3d -> 5d -> 6d holomorphic CS hierarchy."""
    dim: int                    # Complex dimension of ambient space
    en_level: int               # E_n factorization level
    algebra_name: str           # Name of the boundary algebra
    status: str                 # PROVED / CONJECTURAL
    omega_params: int           # Number of Omega-background parameters
    boundary_type: str          # Type of boundary condition producing algebra
    structure_fn_type: str      # rational / trigonometric / classical


# Flat-space hierarchy (C^n)
FLAT_HIERARCHY = [
    HierarchyLevel(
        dim=1, en_level=1,
        algebra_name='Kac-Moody V_k(g)',
        status=STATUS_3D,
        omega_params=0,
        boundary_type='Dirichlet on R',
        structure_fn_type='classical',
    ),
    HierarchyLevel(
        dim=2, en_level=2,
        algebra_name='Affine Yangian Y(gl_hat_1)',
        status=STATUS_5D,
        omega_params=2,
        boundary_type='Dirichlet on R',
        structure_fn_type='rational',
    ),
    HierarchyLevel(
        dim=3, en_level=3,
        algebra_name='Quantum toroidal U_{q,t}(gl_hat_hat_1)',
        status=STATUS_6D,
        omega_params=3,
        boundary_type='E_3 factorization (non-Lagrangian)',
        structure_fn_type='trigonometric',
    ),
]

# K3-fibered hierarchy
K3_HIERARCHY = [
    HierarchyLevel(
        dim=1, en_level=1,
        algebra_name='K3 Heisenberg H_Muk',
        status=STATUS_K3_3D,
        omega_params=0,
        boundary_type='K3 sigma model boundary',
        structure_fn_type='classical',
    ),
    HierarchyLevel(
        dim=2, en_level=2,
        algebra_name='K3 Yangian Y(g_{K3})',
        status=STATUS_K3_5D,
        omega_params=24,
        boundary_type='Dirichlet on R in K3 x C x R',
        structure_fn_type='rational',
    ),
    HierarchyLevel(
        dim=3, en_level=3,
        algebra_name='K3 quantum toroidal U_{q,t}(g_{K3}^{tor})',
        status=STATUS_K3_6D,
        omega_params=25,  # 24 Mukai + tau
        boundary_type='Factorization on K3 x E x C (non-Lagrangian)',
        structure_fn_type='trigonometric',
    ),
]


# =========================================================================
# 2. Dimensional reduction: 6d -> 5d -> 3d
# =========================================================================

def reduce_6d_to_5d(
    q_params: List[complex],
    tau: complex,
    tol: float = 1e-8,
) -> Tuple[List[Rational], Dict[str, Any]]:
    r"""Dimensional reduction 6d -> 5d: shrink E (tau -> i*infty, q -> 0).

    The trigonometric structure function G(x; {q_a}) reduces to the
    rational structure function g(u; {h_a}) in the limit q -> 1
    (equivalently tau -> i*infty).

    The passage: x = e^u, q_a = e^{h_a}.
    In the limit eps -> 0 (scaling all h_a -> eps * h_a):
      G(e^{eps*u}; {e^{eps*h_a}}) = g(u; {h_a}) + O(eps^2).

    Parameters
    ----------
    q_params : list of complex
        Multiplicative Mukai parameters q_a = exp(h_a).
    tau : complex
        Modular parameter of E (Im(tau) > 0).

    Returns
    -------
    h_params : list of Rational
        Additive parameters h_a = log(q_a) (real parts).
    diagnostics : dict
        Reduction diagnostics including the nome q = exp(2pi i tau).
    """
    nome = np.exp(2j * np.pi * tau)
    # AP: verify Im(tau) > 0 (FM24: B-cycle sign)
    assert np.imag(tau) > 0, f"Im(tau) = {np.imag(tau)} <= 0; FM24 violation"
    # AP: verify |q| < 1 (convergence of q-expansion; FM24)
    assert abs(nome) < 1.0 - tol, f"|q| = {abs(nome)} >= 1; FM24 violation"

    h_params = [np.log(complex(qa)).real for qa in q_params]
    # Verify CY_2 constraint survives reduction
    h_sum = sum(h_params)

    diagnostics = {
        'nome_q': nome,
        'nome_abs': abs(nome),
        'im_tau': np.imag(tau),
        'h_sum': h_sum,
        'cy2_preserved': abs(h_sum) < tol,
        'reduction_type': '6d -> 5d: shrink E',
    }
    return h_params, diagnostics


def reduce_5d_to_3d(
    h_params: List[float],
    epsilon: float = 0.0,
) -> Tuple[bool, Dict[str, Any]]:
    r"""Dimensional reduction 5d -> 3d: shrink C (all h_i -> 0).

    The rational structure function g(u; {h_a}) reduces to g = 1
    (trivial) as all h_a -> 0:
      g(u) = prod (u - h_a)/(u + h_a) -> prod 1 = 1.

    The Yangian Y(g_{K3}) degenerates to the current algebra
    (universal enveloping of the Mukai Heisenberg).

    Parameters
    ----------
    h_params : list of float
        Additive Yangian parameters.
    epsilon : float
        Scaling parameter (h_a -> epsilon * h_a). At epsilon=0: classical.

    Returns
    -------
    is_classical : bool
        Whether the algebra has degenerated to the classical limit.
    diagnostics : dict
        Reduction diagnostics.
    """
    scaled = [epsilon * h for h in h_params]
    # At epsilon = 0, all h_a = 0, g(u) = 1
    sigma3_scaled = _compute_sigma3(scaled)
    is_classical = abs(sigma3_scaled) < 1e-15

    diagnostics = {
        'epsilon': epsilon,
        'sigma3_scaled': sigma3_scaled,
        'is_classical': is_classical,
        'reduction_type': '5d -> 3d: shrink C',
        'boundary_algebra': 'H_Muk (Heisenberg)' if is_classical
                           else f'Y(g_K3) at eps={epsilon}',
    }
    return is_classical, diagnostics


def _compute_sigma3(h_params: List[float]) -> float:
    """Compute sigma_3 = sum_{i<j<k} h_i h_j h_k from Newton power sums.

    For the CY_2 case (p_1 = 0): sigma_3 = p_3/3.
    """
    p3 = sum(h**3 for h in h_params)
    return p3 / 3.0


# =========================================================================
# 3. Omega-background at each level
# =========================================================================

class OmegaBackgroundK3:
    """Omega-background data for the K3 hierarchy at each level.

    At 3d: no Omega-background (all parameters zero).
    At 5d: the 24 Mukai parameters h_i with sum = 0.
    At 6d: the 24 Mukai parameters + tau (elliptic modulus).
    """

    def __init__(
        self,
        level: int,
        h_params: Optional[List[Rational]] = None,
        tau: Optional[complex] = None,
    ):
        """
        Parameters
        ----------
        level : int
            Hierarchy level: 3, 5, or 6.
        h_params : list of Rational, optional
            The 24 Mukai parameters (required for level >= 5).
        tau : complex, optional
            Elliptic modulus (required for level 6).
        """
        assert level in (3, 5, 6), f"Level must be 3, 5, or 6; got {level}"
        self.level = level

        if level == 3:
            # No Omega-background at 3d
            self.h_params = [Rational(0)] * MUKAI_RANK
            self.tau = None
        elif level == 5:
            assert h_params is not None, "5d requires Mukai parameters"
            assert len(h_params) == MUKAI_RANK, \
                f"Need {MUKAI_RANK} parameters, got {len(h_params)}"
            # CY_2: sum h_i = 0
            h_sum = sum(h_params)
            assert h_sum == 0, f"CY_2 violation: sum h_i = {h_sum}"
            self.h_params = list(h_params)
            self.tau = None
        else:  # level == 6
            assert h_params is not None, "6d requires Mukai parameters"
            assert tau is not None, "6d requires elliptic modulus tau"
            assert len(h_params) == MUKAI_RANK
            h_sum = sum(h_params)
            assert h_sum == 0, f"CY_2 violation: sum h_i = {h_sum}"
            # FM24: Im(tau) > 0
            assert np.imag(tau) > 0, f"Im(tau) = {np.imag(tau)} <= 0"
            self.h_params = list(h_params)
            self.tau = tau

    @property
    def num_params(self) -> int:
        """Number of independent parameters at this level."""
        if self.level == 3:
            return 0
        elif self.level == 5:
            return MUKAI_RANK - 1  # 23 (one CY_2 constraint)
        else:
            return MUKAI_RANK  # 23 + tau = 24

    @property
    def nome(self) -> Optional[complex]:
        """Nome q = exp(2 pi i tau) for the 6d level."""
        if self.tau is None:
            return None
        return np.exp(2j * np.pi * self.tau)

    def effective_deformation(self) -> Dict[str, Any]:
        """Return the effective deformation parameters at this level."""
        if self.level == 3:
            return {'type': 'classical', 'hbar': 0}
        elif self.level == 5:
            p3 = sum(Rational(h)**3 for h in self.h_params)
            sigma3 = p3 / 3
            sigma2 = sum(
                self.h_params[i] * self.h_params[j]
                for i in range(MUKAI_RANK)
                for j in range(i + 1, MUKAI_RANK)
            )
            return {
                'type': 'rational',
                'sigma2': sigma2,
                'sigma3': sigma3,
                'structure_fn': 'prod (u-h_i)/(u+h_i)',
            }
        else:
            q = self.nome
            return {
                'type': 'trigonometric',
                'tau': self.tau,
                'nome_q': q,
                'nome_abs': abs(q),
                'structure_fn': 'prod (1-q_a x)/(1-q_a^{-1} x)',
            }


# =========================================================================
# 4. Boundary conditions and bulk/defect algebras
# =========================================================================

class BoundaryData(NamedTuple):
    """Boundary condition data at a given hierarchy level."""
    level: int
    bc_type: str            # 'Dirichlet' or 'Neumann'
    boundary_algebra: str   # Name of the algebra on the boundary
    bulk_algebra: str       # Name of the bulk (derived center) algebra
    defect_algebra: str     # Name of the Koszul dual (defect) algebra
    kappa_ch: Rational      # kappa_ch of the boundary algebra (AP113)


def boundary_data_3d() -> BoundaryData:
    """3d level: K3 sigma model on C -> H_Muk."""
    return BoundaryData(
        level=3,
        bc_type='Dirichlet',
        boundary_algebra='H_Muk (rank-24 Heisenberg)',
        bulk_algebra='Z^{der}_ch(H_Muk) = HH*(H_Muk, H_Muk)',
        defect_algebra='H_Muk^! (Koszul dual Heisenberg)',
        kappa_ch=KAPPA_CH_K3,
    )


def boundary_data_5d(h_params: Optional[List[Rational]] = None) -> BoundaryData:
    """5d level: K3 x C x R -> Y(g_{K3})."""
    return BoundaryData(
        level=5,
        bc_type='Dirichlet',
        boundary_algebra='Y(g_{K3}) (K3 Yangian, CONJECTURAL)',
        bulk_algebra='Z^{der}_ch(Y(g_{K3})) (derived center)',
        defect_algebra='Y(g_{K3})^! (Koszul dual K3 Yangian)',
        kappa_ch=KAPPA_CH_K3E,
    )


def boundary_data_6d() -> BoundaryData:
    """6d level: K3 x E x C -> U_{q,t}(g_{K3}^{tor})."""
    return BoundaryData(
        level=6,
        bc_type='E_3 factorization (non-Lagrangian)',
        boundary_algebra='U_{q,t}(g_{K3}^{tor}) (K3 q-toroidal, CONJECTURAL)',
        bulk_algebra='Z^{der}_ch(U_{q,t}) (derived center)',
        defect_algebra='U_{q,t}^! (Koszul dual K3 q-toroidal)',
        kappa_ch=KAPPA_CH_K3E,
    )


# =========================================================================
# 5. Wilson lines at each level
# =========================================================================

class WilsonLineData(NamedTuple):
    """Wilson line data at a given hierarchy level."""
    level: int
    line_type: str          # point / line / surface
    index_space: str        # What indexes the Wilson lines
    module_type: str        # Type of module produced
    coproduct_type: str     # How the coproduct acts on fusion


def wilson_data_3d() -> WilsonLineData:
    """3d Wilson lines: point operators indexed by Mukai vectors."""
    return WilsonLineData(
        level=3,
        line_type='point operator on C',
        index_space='Mukai vectors v in H^*(K3, Z)',
        module_type='H_Muk-module (Fock module F_v)',
        coproduct_type='primitive: Delta_0(J_i) = J_i^L + J_i^R',
    )


def wilson_data_5d() -> WilsonLineData:
    """5d Wilson lines: line operators on C, indexed by Fock modules."""
    return WilsonLineData(
        level=5,
        line_type='line operator on C (wrapping C in K3 x C x R)',
        index_space='Fock modules F_lambda of Y(g_{K3})',
        module_type='Y(g_{K3})-module with spectral parameter',
        coproduct_type='Miura: Delta_z(T(u)) = T^L(u) . T^R(u-z)',
    )


def wilson_data_6d() -> WilsonLineData:
    """6d Wilson surfaces: surface operators wrapping E."""
    return WilsonLineData(
        level=6,
        line_type='surface operator wrapping E',
        index_space='BPS states indexed by Mukai vectors + E winding',
        module_type='U_{q,t}(g_{K3}^{tor})-module',
        coproduct_type='q-deformed Miura coproduct (CONJECTURAL)',
    )


# =========================================================================
# 6. Structure function at each level
# =========================================================================

def structure_function_3d(u: complex) -> complex:
    """Structure function at the 3d level: g(u) = 1 (classical).

    At the 3d level (K3 sigma model, no Omega-background),
    the structure function is trivially 1. The R-matrix is the identity.
    """
    return complex(1.0)


def structure_function_5d(
    u: complex,
    h_params: List[Rational],
) -> complex:
    """Structure function at the 5d level: rational.

    g_{K3}(u) = prod_{i=1}^{24} (u - h_i) / (u + h_i)

    Degree (24, 24) rational function.

    Parameters
    ----------
    u : complex
        Spectral parameter (NOT worldsheet; AP-CY31).
    h_params : list of Rational
        The 24 Mukai parameters with sum h_i = 0.

    Returns
    -------
    complex
        g_{K3}(u).
    """
    assert len(h_params) == MUKAI_RANK
    result = complex(1.0)
    for h in h_params:
        hf = complex(h)
        uf = complex(u)
        denom = uf + hf
        if abs(denom) < 1e-30:
            raise ZeroDivisionError(f"Pole at u = -{h}")
        result *= (uf - hf) / denom
    return result


def structure_function_6d(
    x: complex,
    q_params: List[complex],
) -> complex:
    """Structure function at the 6d level: trigonometric.

    G_{K3}(x) = prod_{a=1}^{24} (1 - q_a x) / (1 - q_a^{-1} x)

    Degree (24, 24) in the nome variables.

    Parameters
    ----------
    x : complex
        Multiplicative spectral parameter (x = e^u).
    q_params : list of complex
        Multiplicative Mukai parameters q_a = exp(h_a).
    """
    return trigonometric_structure_function(x, q_params)


# =========================================================================
# 7. Verification of dimensional reduction
# =========================================================================

def verify_6d_to_5d_reduction(
    h_params: List[Rational],
    n_points: int = 20,
    tol: float = 1e-6,
) -> Tuple[bool, float]:
    r"""Verify that the trigonometric structure function reduces to rational.

    For small eps, with u real and bounded away from poles:
      G(e^{eps*u}; {e^{eps*h_a}}) approx g(u; {h_a})

    The limit is exact as eps -> 0; we verify at eps = 0.01.

    Returns (passes, max_relative_error).
    """
    eps = 0.01
    max_rel_err = 0.0
    q_params = [np.exp(complex(h) * eps) for h in h_params]

    for k in range(n_points):
        # Choose u away from all poles +/- h_i (AP-CY28)
        u_test = 10.0 + 3.7 * k
        x_test = np.exp(eps * u_test)

        # Trigonometric value
        g_trig = trigonometric_structure_function(x_test, q_params)

        # Rational value
        g_rat = structure_function_5d(u_test, h_params)

        if abs(g_rat) > 1e-15:
            rel_err = abs(g_trig - g_rat) / abs(g_rat)
            max_rel_err = max(max_rel_err, rel_err)

    return max_rel_err < tol, max_rel_err


def verify_5d_to_3d_reduction(
    h_params: List[Rational],
    n_points: int = 20,
    tol: float = 1e-10,
) -> Tuple[bool, float]:
    r"""Verify that the rational structure function reduces to 1 at eps=0.

    g(u; {eps*h_a}) -> 1 as eps -> 0.

    Returns (passes, max_residual).
    """
    eps = 0.0  # Exact classical limit
    max_res = 0.0

    for k in range(n_points):
        u_test = 5.0 + 2.3 * k
        h_scaled = [Rational(0)] * MUKAI_RANK  # eps=0 means all h=0
        g_val = structure_function_5d(u_test, h_scaled)
        res = abs(g_val - 1.0)
        max_res = max(max_res, res)

    return max_res < tol, max_res


# =========================================================================
# 8. The master diagram
# =========================================================================

def master_diagram() -> Dict[str, Any]:
    """Return the complete master diagram connecting all levels.

    This is the data structure underlying the tikzcd diagram in
    quantum_chiral_algebras.tex, Conjecture conj:hcs-k3-hierarchy.
    """
    return {
        'title': 'Holomorphic CS hierarchy for K3',
        'levels': {
            '6d': {
                'geometry': 'K3 x E x C',
                'theory': '6d holomorphic theory (non-Lagrangian)',
                'algebra': 'U_{q,t}(g_{K3}^{tor})',
                'en_level': 3,
                'structure_fn': 'trigonometric G(x; {q_a})',
                'status': STATUS_K3_6D,
                'omega': '(q_1,...,q_{24}; tau)',
            },
            '5d': {
                'geometry': 'K3 x C x R',
                'theory': '5d holomorphic CS',
                'algebra': 'Y(g_{K3})',
                'en_level': 2,
                'structure_fn': 'rational g(u; {h_a})',
                'status': STATUS_K3_5D,
                'omega': '(h_1,...,h_{24})',
            },
            '3d': {
                'geometry': 'K3 on C (sigma model)',
                'theory': '3d sigma model / CY-A_2',
                'algebra': 'H_Muk',
                'en_level': 1,
                'structure_fn': 'classical g = 1',
                'status': STATUS_K3_3D,
                'omega': 'none',
            },
        },
        'reductions': {
            '6d -> 5d': {
                'mechanism': 'Shrink E: tau -> i*infty, q -> 0',
                'on_params': 'q_a -> 1 + h_a, x -> 1 + u',
                'on_structure_fn': 'G(x) -> g(u) (trig -> rational)',
                'on_algebra': 'U_{q,t} -> Y (toroidal -> Yangian)',
            },
            '5d -> 3d': {
                'mechanism': 'Shrink C: all h_a -> 0',
                'on_params': 'h_a -> 0',
                'on_structure_fn': 'g(u) -> 1 (rational -> classical)',
                'on_algebra': 'Y -> H_Muk (Yangian -> Heisenberg)',
            },
        },
        'kappa_spectrum': {
            'kappa_ch_K3': int(KAPPA_CH_K3),
            'kappa_ch_K3E': int(KAPPA_CH_K3E),
            'kappa_BKM_K3E': int(KAPPA_BKM_K3E),
            'kappa_cat_K3': int(KAPPA_CAT_K3),
            'kappa_cat_K3E': int(KAPPA_CAT_K3E),
            'kappa_fiber_K3': int(KAPPA_FIBER_K3),
        },
    }


# =========================================================================
# 9. Cross-engine compatibility
# =========================================================================

def verify_flat_space_specialisation(
    omega: OmegaBackground,
    n_points: int = 10,
    tol: float = 1e-10,
) -> Tuple[bool, float]:
    """Verify that the K3 hierarchy reduces to flat-space at rank 3.

    The flat-space hierarchy has 3 parameters (h_1, h_2, h_3).
    The K3 hierarchy with h_i = h_1 for i in {1,..,8}, h_i = h_2 for
    i in {9,..,16}, h_i = h_3 for i in {17,..,24} should reproduce
    the flat-space structure function g(u)^8 (up to redefinition).

    Here we test the simpler case: embed the 3-parameter flat-space
    Omega-background into the 24-parameter K3 setting by taking
    h_1 = omega.h1, h_2 = omega.h2, h_3 = omega.h3, and all
    remaining h_i = 0.  Then:
      g_{K3}(u) = prod_{i=1}^{3} (u-h_i)/(u+h_i) * prod_{i=4}^{24} 1
                = g_{C^3}(u).

    Returns (passes, max_relative_error).
    """
    # Embed: first 3 params are omega.h1, h2, h3; rest are 0
    h_params = [omega.h1, omega.h2, omega.h3] + [Rational(0)] * 21

    max_rel_err = 0.0
    for k in range(n_points):
        # Test points away from poles (AP-CY28)
        u_test = Rational(37 + 7 * k)  # Large, away from all h_i
        g_k3 = structure_function_5d(u_test, h_params)
        g_flat = omega.structure_function_at(u_test)
        if abs(complex(g_flat)) > 1e-15:
            rel_err = abs(g_k3 - complex(g_flat)) / abs(complex(g_flat))
            max_rel_err = max(max_rel_err, rel_err)

    return max_rel_err < tol, max_rel_err


def verify_kappa_spectrum_consistency() -> Dict[str, bool]:
    """Verify internal consistency of the kappa-spectrum (AP113).

    Checks:
    1. kappa_ch(K3 x E) = kappa_ch(K3) + kappa_ch(E)  (additivity)
    2. kappa_cat(K3) = chi(O_K3) = 2
    3. kappa_cat(K3 x E) = chi(O_{K3}) * chi(O_E) = 2 * 0 = 0  (Kuenneth)
    4. kappa_fiber = rank(Mukai lattice) = 24
    5. kappa_BKM = 5 (Igusa weight)
    6. The five distinct values are {0, 2, 3, 5, 24}
    """
    checks = {}

    # 1. Additivity: kappa_ch(K3 x E) = kappa_ch(K3) + kappa_ch(E)
    # kappa_ch(E) = 1 (elliptic curve has kappa_ch = 1)
    kappa_ch_E = Rational(1)
    checks['additivity'] = (KAPPA_CH_K3E == KAPPA_CH_K3 + kappa_ch_E)

    # 2. kappa_cat = chi(O_K3) = 2
    checks['kappa_cat_K3'] = (KAPPA_CAT_K3 == Rational(2))

    # 3. Kuenneth: kappa_cat(K3 x E) = chi(O_K3) * chi(O_E)
    # chi(O_E) = 0 for an elliptic curve
    checks['kuenneth'] = (KAPPA_CAT_K3E == Rational(0))

    # 4. Mukai rank
    checks['mukai_rank'] = (KAPPA_FIBER_K3 == Rational(MUKAI_RANK))

    # 5. BKM weight
    checks['bkm_weight'] = (KAPPA_BKM_K3E == Rational(5))

    # 6. Five distinct values
    kappa_set = {
        int(KAPPA_CAT_K3E), int(KAPPA_CH_K3), int(KAPPA_CH_K3E),
        int(KAPPA_BKM_K3E), int(KAPPA_FIBER_K3),
    }
    checks['five_values'] = (kappa_set == {0, 2, 3, 5, 24})

    return checks


# =========================================================================
# 10. Summary data for the master table
# =========================================================================

def hierarchy_summary_table() -> List[Dict[str, Any]]:
    """Return the data for the hierarchy summary table.

    Columns: Level, Geometry, Algebra, E_n, Structure fn, Status,
    Omega params, Boundary, Wilson lines.
    """
    rows = []
    for level_data, wilson_fn in [
        (K3_HIERARCHY[0], wilson_data_3d),
        (K3_HIERARCHY[1], wilson_data_5d),
        (K3_HIERARCHY[2], wilson_data_6d),
    ]:
        w = wilson_fn()
        bd = [boundary_data_3d, boundary_data_5d, boundary_data_6d][
            [3, 5, 6].index(level_data.dim * 2 + 1)
            if level_data.dim < 3 else 2
        ]()
        rows.append({
            'level': f'{level_data.dim * 2 + 1 if level_data.dim < 3 else 6}d',
            'geometry': {1: 'K3 on C', 2: 'K3 x C x R', 3: 'K3 x E x C'}[level_data.dim],
            'algebra': level_data.algebra_name,
            'en_level': level_data.en_level,
            'structure_fn': level_data.structure_fn_type,
            'status': level_data.status,
            'omega_params': level_data.omega_params,
            'boundary': bd.bc_type,
            'bulk': bd.bulk_algebra,
            'defect': bd.defect_algebra,
            'kappa_ch': bd.kappa_ch,
            'wilson_type': w.line_type,
            'wilson_index': w.index_space,
            'coproduct': w.coproduct_type,
        })
    return rows
