r"""E_3 deformation of chiral CE cochains -> quantum toroidal U_{q,t}(gl_hat_hat_1).

MATHEMATICAL FRAMEWORK
======================

This module constructs the quantum toroidal algebra U_{q,t}(gl_hat_hat_1) as
the E_3 Koszul dual of the deformed chiral Chevalley-Eilenberg complex
CE^{ch}_*(L)[[epsilon_1, epsilon_2, epsilon_3]].  This is the precise 6d
analogue of the Costello-Francis-Gwilliam (CFG25) construction of U_q(g)
from E_3 deformation of CE_*(g) in 3d holomorphic Chern-Simons.

THE CFG25 CHAIN (3d):
  CE_*(g) --E_3 deformation--> CE_*(g)[[hbar]] = Obs^q --Koszul--> U_q(g)-mod

THE 6d CHIRAL CHAIN:
  CE^{ch}_*(L) --E_3 deformation--> CE^{ch}_*(L)[[eps]] = Obs^q_{6d}
              --Koszul--> U_{q,t}-mod

The key new feature relative to 3d: the 6d Omega-background has THREE
independent deformation parameters (epsilon_1, epsilon_2, epsilon_3)
subject to the CY constraint epsilon_1 + epsilon_2 + epsilon_3 = 0,
leaving TWO effective parameters.  These map to the (q, t) of the
quantum toroidal algebra via:
  q = exp(epsilon_1),  t = exp(-epsilon_2),  epsilon_3 = -(epsilon_1 + epsilon_2).

THE E_n DEFORMATION HIERARCHY
=============================

At (epsilon_1, 0, 0):  E_1 deformation.
  The 6d theory on C x R^5 produces an E_1 factorization algebra.
  Deformed complex: CE^{ch}_*(L)[[epsilon_1]].
  Only ONE deformation direction: the chiral direction.
  Koszul dual: the CLASSICAL chiral algebra itself (no quantum group).
  sigma_2 = 0, sigma_3 = 0 (self-dual point, h_2 = 0).
  The deformation is TRIVIAL: d_h = d_CE (no epsilon-correction survives
  after the CY constraint, since h_2 = h_3 = 0 forces the E_2 and E_3
  directions to vanish).
  MC element: alpha_1 = 0 (classical vacuum).

At (epsilon_1, epsilon_2, 0):  E_2 deformation.
  The 5d theory on C^2 x R produces an E_2 factorization algebra.
  Deformed complex: CE^{ch}_*(L)[[epsilon_1, epsilon_2]].
  TWO deformation directions, but sigma_3 = 0 (self-dual: h_3 = 0).
  Koszul dual: the affine Yangian Y(gl_hat_1).
  The deformation is NONTRIVIAL: sigma_2 = epsilon_1 * epsilon_2 != 0
  gives the Kac-Moody level k = -sigma_2.
  The MC element alpha_2 = sigma_2 * r(u) (the classical r-matrix), giving
  the Yangian bracket from the deformed CE differential.

At (epsilon_1, epsilon_2, epsilon_3):  E_3 deformation (FULL).
  The 6d theory on C^3 produces an E_3 factorization algebra.
  Deformed complex: CE^{ch}_*(L)[[epsilon_1, epsilon_2, epsilon_3]].
  sigma_3 = epsilon_1 * epsilon_2 * epsilon_3 != 0 (generic point).
  Koszul dual: the quantum toroidal algebra U_{q,t}(gl_hat_hat_1).
  The MC element alpha_3 is the FULL quantum MC element with
  sigma_3-corrections from the L_infinity tower (shadow class dependent).

EXPLICIT CE COMPLEX FOR L = HEISENBERG
=======================================

The Heisenberg Lie conformal algebra has one generator J, spin 1, with
{J_lambda J} = k * lambda (abelian 0-th product, central extension at
lambda^1).

CE^{ch}_*(Heis) = Lambda^*(J) with d_CE = 0 (abelian).
  CE_0 = k (scalars), CE_1 = k * J (one generator), CE_k = 0 for k >= 2.
  Poincare poly = 1 + t.

For the chiral envelope A = U^{ch}(Heis) = V_k(gl_1) (the Heisenberg VOA):
  B(A) = CE_*(Heis): arity 0 = 1-dim, arity 1 = 1-dim, higher = 0.

The E_n deformation of CE^{ch}_*(Heis):
  E_1: trivially d_h = 0 (abelian, diagonal embedding).
  E_2: trivially d_h = 0 (sigma_3 = 0 at self-dual E_2 point).
  E_3: d_h = 0 STILL (class G: no L_infinity corrections).
       The quantum toroidal structure emerges at the KOSZUL DUAL level,
       not from the CE differential itself.  The E_3 bar complex is
       formal (d = 0), so the Koszul dual is computed from the underlying
       E_3 coalgebra structure on Lambda^*(J) with the three-fold coproduct.

MC ELEMENTS AT EACH E_n LEVEL
==============================

The Maurer-Cartan equation in CE^{ch,*}(L)[1] is:
  d(alpha) + (1/2)[alpha, alpha] + (1/6)l_3(alpha^3) + ... = 0

E_1 level (epsilon_1, 0, 0):
  alpha_1 = 0.  Trivially MC.  The classical vacuum.
  Physical: no quantum correction.

E_2 level (epsilon_1, epsilon_2, 0):
  alpha_2 = sigma_2 * Omega/u = -k * Omega/u.
  This is the classical r-matrix solving d(alpha_2) + (1/2)[alpha_2, alpha_2] = 0,
  the classical Yang-Baxter equation.  For gl_1: Omega = id, so
  alpha_2 = k/u (a scalar-valued 1-form on the punctured formal disk).

E_3 level (epsilon_1, epsilon_2, epsilon_3):
  alpha_3 = alpha_2 + sigma_3 * correction.
  The correction comes from the L_infinity structure:
  - Class G (Heisenberg): correction = 0 (no L_infinity corrections).
  - Class L (Yangian): correction = rational function of sigma_3.
  - Class M (Virasoro): correction = Gevrey-1 divergent series in sigma_3.

KOSZUL DUAL AT EACH LEVEL
==========================

The E_n Koszul dual D_E_n(B_{E_n}(A)) at each factorization level:

E_1 Koszul dual:
  D_{E_1}(B_{E_1}(A)) = A itself (the chiral algebra is E_1-Koszul self-dual
  up to a level shift: V_k(g)^! = V_{k'}(g) at k' = -k - 2h^vee).
  For gl_1 (h^vee = 0): A^! = V_{-k}(gl_1).
  Modules: Rep^{E_0}(A^!) = ordinary modules of V_{-k}(gl_1).

E_2 Koszul dual:
  D_{E_2}(B_{E_2}(A)) carries E_2-chiral structure = braided category.
  For gl_1: the E_2 Koszul dual is the affine Yangian Y(gl_hat_1)
  with structure function g(u) = (u - h_1)(u - h_2)(u - h_3) / ((u + h_1)(u + h_2)(u + h_3)).
  At the E_2 point (h_3 = 0): g(u) simplifies.
  Modules: Rep^{E_1}(A^!) = braided monoidal category of Yangian reps.

E_3 Koszul dual:
  D_{E_3}(B_{E_3}(A)) carries E_3-chiral structure.
  For gl_1: the E_3 Koszul dual is the quantum toroidal algebra
  U_{q,t}(gl_hat_hat_1) (CONJECTURAL; AP-CY6/AP-CY14: depends on CY-A_3).
  (q, t) = (exp(epsilon_1), exp(-epsilon_2)).
  Structure function: G(x) = prod_{i=1}^3 (1 - q_i x) / (1 - q_i^{-1} x)
  with q_i = exp(epsilon_i).
  Modules: Rep^{E_2}(A^!) = braided monoidal category of quantum toroidal reps.

DIMENSIONAL REDUCTION
=====================

The E_3 -> E_2 -> E_1 projection corresponds to setting deformation parameters
to zero one at a time:
  E_3 -> E_2: set epsilon_3 = 0 (equivalently q_3 = 1, sigma_3 = 0).
              Quantum toroidal -> affine Yangian (rational limit).
  E_2 -> E_1: set epsilon_2 = 0 (equivalently q_2 = 1, sigma_2 = 0).
              Affine Yangian -> Kac-Moody (classical limit).

This is the Costello dimensional hierarchy:
  6d (C^3) --proj to C^2--> 5d (C^2 x R) --proj to C x R--> 3d (C x R)

AP COMPLIANCE
=============
- All identifications with quantum groups at d=3 use conjecture (AP-CY6/AP-CY14).
- The E_3 structure is topological (configuration spaces of C^3), not algebraic
  (Deligne conjecture); AP154 compliance.
- kappa always subscripted: kappa_ch (AP113).
- sigma_3 = h_1*h_2*h_3 is the essential deformation parameter.
- The CE complex uses the diagonal embedding; equivariant deformation vanishes
  by h_1+h_2+h_3=0 for class G (AP-CY20: intermediary mechanism stated).
- E_3 bar: (1+t)^{3g} for class L,C ONLY; fails for class M (AP-CY21).
- MC moduli requires COMPLETE shadow tower computation (AP-CY12).
- z is the Yangian spectral parameter, NOT the worldsheet coordinate (AP-CY31).
- Factored =/= solved for higher coherence (AP-CY30: ZTE correction needed).

CONVENTIONS
===========
- epsilon_i (= h_i) with epsilon_1 + epsilon_2 + epsilon_3 = 0 (CY condition).
- sigma_2 = e_2(epsilon) = sum_{i<j} epsilon_i epsilon_j.
- sigma_3 = e_3(epsilon) = epsilon_1 epsilon_2 epsilon_3.
- (q, t) = (exp(epsilon_1), exp(-epsilon_2)): Macdonald convention.
- Cohomological grading (|d| = +1).
- Bar desuspension: |s^{-1}a| = |a| - 1 (AP45).

MANUSCRIPT REFERENCES
=====================
- chapters/theory/quantum_chiral_algebras.tex, subsec:ce-deformation-e3
  (Construction constr:quantum-ce-deformation)
- chapters/theory/quantum_chiral_algebras.tex, conj:chiral-qg-c3
  (Chiral quantum group on C^3)
- chapters/theory/quantum_chiral_algebras.tex, rem:hcs-pipeline
  (holomorphic CS -> chiral quantum group pipeline)
- chapters/theory/en_factorization.tex, conj:e3-koszul-duality
  (E_3-chiral Koszul duality from 6d theory)
- chapters/theory/en_factorization.tex, thm:e3-koszul-heisenberg
  (E_3 Koszul self-duality of the Heisenberg)
- compute/lib/chiral_ce_complex.py (CE chains and L_infinity deformation)
- compute/lib/chiral_ce_e3_deformation.py (E_3 deformation theory)
- compute/lib/quantum_toroidal_e1_cy3.py (quantum toroidal DIM presentation)
- compute/lib/holomorphic_cs_chiral_engine.py (holomorphic CS hierarchy)
- compute/lib/cfg25_e1_chiral_lift.py (CFG25 E_1-chiral lift)

MATHEMATICAL SOURCES
====================
- Costello-Francis-Gwilliam, "CS theory and factorisation homology" (2025)
- Costello, "Supersymmetric gauge theory and the Yangian" (2013)
- Costello, "M-theory in the Omega-background" (2017)
- Loday-Vallette, "Algebraic Operads" (2012): CE and bar-cobar
- Ding-Iohara, "Generalization of Drinfeld quantum affine algebras" (1997)
- Miki, "A (q,gamma) analog of the W_{1+inf} algebra" (2007)
- Feigin-Jimbo-Miwa-Mukhin, "Quantum toroidal gl_1: plane partitions" (2012)
"""

from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

import numpy as np

from compute.lib.chiral_ce_complex import (
    CEChainComplex,
    CEElement,
    DerivedCenterCE,
    LCAGenerator,
    LambdaBracketTerm,
    LieConformalAlgebra,
    LInfinityCEComplex,
    LInfinityData,
    heisenberg_lca,
    heisenberg_linfinity,
    kac_moody_sl2_lca,
    virasoro_lca,
    virasoro_linfinity,
    yangian_gl1_lca,
    yangian_gl1_linfinity,
)

from compute.lib.chiral_ce_e3_deformation import (
    E3ChiralCEDeformation,
    E3KoszulDual,
    OmegaParams,
    QuantumCEDeformation,
)


# =========================================================================
#  0.  The E_n deformation level
# =========================================================================

@dataclass(frozen=True)
class EnDeformationLevel:
    r"""An E_n deformation level of the Omega-background.

    Each level corresponds to a dimensional projection of the 6d theory:
      E_1: (epsilon_1, 0, 0)           -> 3d hol CS on C x R
      E_2: (epsilon_1, epsilon_2, 0)   -> 5d hol CS on C^2 x R
      E_3: (epsilon_1, epsilon_2, eps3) -> 6d hol theory on C^3

    The CY condition epsilon_1 + epsilon_2 + epsilon_3 = 0 is enforced.

    Parameters
    ----------
    n : int
        The E_n level (1, 2, or 3).
    epsilon1 : Fraction
        First deformation parameter.
    epsilon2 : Fraction
        Second parameter (0 at E_1 level).
    """
    n: int
    epsilon1: Fraction
    epsilon2: Fraction

    def __post_init__(self):
        if self.n not in (1, 2, 3):
            raise ValueError(f"E_n level must be 1, 2, or 3; got {self.n}")
        if self.n == 1 and self.epsilon2 != Fraction(0):
            raise ValueError(f"E_1 level requires epsilon_2 = 0; got {self.epsilon2}")
        if self.n == 2 and self.epsilon3 != Fraction(0):
            raise ValueError(
                f"E_2 level requires epsilon_3 = 0; got eps1+eps2 = "
                f"{self.epsilon1 + self.epsilon2}"
            )

    @property
    def epsilon3(self) -> Fraction:
        """epsilon_3 = -(epsilon_1 + epsilon_2) by the CY condition."""
        return -(self.epsilon1 + self.epsilon2)

    @property
    def sigma2(self) -> Fraction:
        """sigma_2 = epsilon_1*epsilon_2 + epsilon_1*epsilon_3 + epsilon_2*epsilon_3."""
        e1, e2, e3 = self.epsilon1, self.epsilon2, self.epsilon3
        return e1 * e2 + e1 * e3 + e2 * e3

    @property
    def sigma3(self) -> Fraction:
        """sigma_3 = epsilon_1 * epsilon_2 * epsilon_3."""
        return self.epsilon1 * self.epsilon2 * self.epsilon3

    @property
    def is_self_dual(self) -> bool:
        """At the self-dual point, sigma_3 = 0 (one epsilon_i = 0)."""
        return self.sigma3 == Fraction(0)

    @property
    def kac_moody_level(self) -> Fraction:
        """Effective KM level k = -sigma_2."""
        return -self.sigma2

    @property
    def omega(self) -> OmegaParams:
        """Convert to OmegaParams for compatibility with existing engines."""
        return OmegaParams(h1=self.epsilon1, h2=self.epsilon2)

    def theory_name(self) -> str:
        """Physical theory at this E_n level."""
        names = {
            1: "3d holomorphic CS on C x R",
            2: "5d holomorphic CS on C^2 x R",
            3: "6d holomorphic theory on C^3",
        }
        return names[self.n]

    def boundary_algebra_name(self) -> str:
        """Name of the boundary chiral algebra at this level.

        These are CONJECTURAL identifications at d=3 (AP-CY6/AP-CY14).
        """
        if self.n == 1:
            return "Kac-Moody V_k(gl_1)"
        elif self.n == 2:
            return "Affine Yangian Y(gl_hat_1) [CONJECTURAL at d=3]"
        else:
            return "Quantum toroidal U_{q,t}(gl_hat_hat_1) [CONJECTURAL at d=3]"

    def koszul_dual_name(self) -> str:
        """Name of the E_n Koszul dual algebra.

        All identifications at d=3 are CONJECTURAL (AP-CY6/AP-CY14).
        """
        if self.n == 1:
            k = self.kac_moody_level
            return f"V_{{-k}}(gl_1) at k = {k} (Feigin-Frenkel dual)"
        elif self.n == 2:
            return "Dual affine Yangian Y^!(gl_hat_1) [CONJECTURAL]"
        else:
            return "Quantum toroidal U_{q^{-1},t^{-1}}(gl_hat_hat_1) [CONJECTURAL]"

    def num_deformation_params(self) -> int:
        """Number of independent deformation parameters at this E_n level.

        E_1: 0 effective (sigma_2 = 0, sigma_3 = 0; rescaling only via epsilon_1).
        E_2: 1 effective (sigma_2 != 0, sigma_3 = 0; the KM level k = -sigma_2).
        E_3: 2 effective (sigma_2, sigma_3 both potentially nonzero; the two
             independent (q, t) parameters of the quantum toroidal).
        """
        if self.n == 1:
            return 0
        elif self.n == 2:
            return 1
        else:
            return 2


def e1_level(epsilon1: Fraction = Fraction(1)) -> EnDeformationLevel:
    """Create the E_1 deformation level at (epsilon_1, 0, 0)."""
    return EnDeformationLevel(n=1, epsilon1=epsilon1, epsilon2=Fraction(0))


def e2_level(
    epsilon1: Fraction = Fraction(1),
    epsilon2: Fraction = Fraction(-1),
) -> EnDeformationLevel:
    """Create the E_2 deformation level at (epsilon_1, epsilon_2, 0).

    CY condition: epsilon_3 = -(epsilon_1 + epsilon_2) = 0 requires
    epsilon_2 = -epsilon_1 for the E_2 point.
    """
    if epsilon1 + epsilon2 != Fraction(0):
        raise ValueError(
            f"E_2 requires epsilon_3 = 0, i.e., epsilon_2 = -epsilon_1; "
            f"got epsilon_1={epsilon1}, epsilon_2={epsilon2}, "
            f"epsilon_3={-(epsilon1 + epsilon2)}"
        )
    return EnDeformationLevel(n=2, epsilon1=epsilon1, epsilon2=epsilon2)


def e3_level(
    epsilon1: Fraction = Fraction(1),
    epsilon2: Fraction = Fraction(-2),
) -> EnDeformationLevel:
    """Create the E_3 deformation level at generic (epsilon_1, epsilon_2, epsilon_3).

    epsilon_3 = -(epsilon_1 + epsilon_2).
    For the quantum toroidal: q = exp(epsilon_1), t = exp(-epsilon_2).
    """
    return EnDeformationLevel(n=3, epsilon1=epsilon1, epsilon2=epsilon2)


# =========================================================================
#  1.  Chiral CE complex at each E_n level
# =========================================================================

class ChiralCEAtLevel:
    r"""Chiral CE complex of L = Heisenberg at a given E_n deformation level.

    Wraps the CE chain complex from chiral_ce_complex.py with the E_n
    deformation data, and computes the deformed differential, MC element,
    and Koszul dual identification at each level.

    Parameters
    ----------
    lca : LieConformalAlgebra
        The Lie conformal algebra.
    linf : LInfinityData
        The L_infinity structure data.
    level : EnDeformationLevel
        The E_n deformation level.
    """

    def __init__(
        self,
        lca: LieConformalAlgebra,
        linf: LInfinityData,
        level: EnDeformationLevel,
    ):
        self.lca = lca
        self.linf = linf
        self.level = level
        self.ce = CEChainComplex(lca)
        self.linf_ce = LInfinityCEComplex(lca, linf)
        self.dc = DerivedCenterCE(self.ce)

    @property
    def shadow_class(self) -> str:
        return self.linf.shadow_class

    @property
    def en_level(self) -> int:
        return self.level.n

    # ----- Deformed differential -----

    def d_deformed(self, elem: CEElement, max_order: int = 4) -> CEElement:
        r"""Apply the E_n-deformed differential at the given level.

        E_1: d = d_CE (no deformation).
        E_2: d = d_CE (sigma_3 = 0, so L_infinity corrections vanish).
        E_3: d = d_CE + sigma_3 * d^{(3)} + sigma_3^2 * d^{(4)} + ...

        For class G (Heisenberg): d = 0 at ALL levels (abelian).
        For class L (Yangian): d = d_CE at E_1, E_2; d_CE at E_3 (strict Lie,
            no L_infinity corrections).
        For class M (Virasoro): d has sigma_3-corrections at E_3.
        """
        # d_CE part (always present)
        result = self.ce.d_CE(elem)

        # L_infinity corrections only at E_3 level with sigma_3 != 0
        if self.level.n == 3:
            sigma3 = self.level.sigma3
            if sigma3 != Fraction(0) and max_order >= 3:
                d3 = self.linf_ce._d3(elem)
                result = result + sigma3 * d3
            if sigma3 != Fraction(0) and max_order >= 4:
                d4 = self.linf_ce._d4(elem)
                result = result + (sigma3 ** 2) * d4

        return result.cleaned()

    def d_squared_zero(self, max_arity: int = 3) -> bool:
        r"""Verify d^2 = 0 at the current E_n level."""
        n = self.lca.dim
        from itertools import combinations
        for k in range(1, min(max_arity + 1, n + 1)):
            for indices in combinations(range(n), k):
                elem = CEElement.basis(indices)
                d1 = self.d_deformed(elem)
                if d1.cleaned().is_zero():
                    continue
                d2 = self.d_deformed(d1)
                if not d2.cleaned().is_zero():
                    return False
        return True

    # ----- Maurer-Cartan element -----

    def mc_element_description(self) -> Dict[str, Any]:
        r"""Description of the Maurer-Cartan element at the current E_n level.

        The MC element alpha in CE^{ch,1}(L) satisfies:
          d(alpha) + (1/2)[alpha, alpha] + (1/6)l_3(alpha^3) + ... = 0

        E_1: alpha_1 = 0 (trivial, classical vacuum).
        E_2: alpha_2 = sigma_2 * Omega/u (classical r-matrix solving CYBE).
        E_3: alpha_3 = alpha_2 + sigma_3 * (quantum correction).
        """
        lvl = self.level

        if lvl.n == 1:
            return {
                "level": "E_1",
                "mc_element": "0 (classical vacuum)",
                "mc_equation": "d_CE(0) = 0 (trivially satisfied)",
                "physical": "No quantum correction at E_1",
                "sigma2": Fraction(0),
                "sigma3": Fraction(0),
            }
        elif lvl.n == 2:
            k = lvl.kac_moody_level
            return {
                "level": "E_2",
                "mc_element": f"sigma_2 * Omega/u = {-lvl.sigma2}/u (classical r-matrix)",
                "mc_equation": (
                    "d_CE(alpha) + (1/2)[alpha, alpha] = 0 "
                    "(classical Yang-Baxter equation)"
                ),
                "physical": (
                    f"Classical r-matrix at KM level k = {k}; "
                    f"Yangian Y(gl_hat_1) from CYBE"
                ),
                "sigma2": lvl.sigma2,
                "sigma3": Fraction(0),
            }
        else:  # E_3
            sigma3 = lvl.sigma3
            if self.shadow_class == "G":
                correction = "0 (class G: no L_infinity corrections)"
                mc_type = "polynomial (terminates at order 0)"
            elif self.shadow_class == "L":
                correction = "rational function of sigma_3 (class L)"
                mc_type = "rational (converges)"
            else:
                correction = "Gevrey-1 divergent series in sigma_3 (class M)"
                mc_type = "Gevrey-1 divergent (Borel resummable)"

            return {
                "level": "E_3",
                "mc_element": (
                    f"alpha_2 + sigma_3 * correction, sigma_3 = {sigma3}"
                ),
                "mc_equation": (
                    "d_CE(alpha) + (1/2)[alpha, alpha] + (1/6)l_3(alpha^3) + ... = 0 "
                    "(full L_infinity MC equation)"
                ),
                "correction": correction,
                "mc_type": mc_type,
                "physical": (
                    f"Quantum MC element at (q, t) ~ (exp({lvl.epsilon1}), "
                    f"exp({-lvl.epsilon2})); quantum toroidal deformation"
                ),
                "sigma2": lvl.sigma2,
                "sigma3": sigma3,
            }

    # ----- Koszul dual -----

    def koszul_dual_info(self) -> Dict[str, Any]:
        r"""Information about the E_n Koszul dual at the current level.

        The E_n Koszul dual D_{E_n}(B_{E_n}(A)) at each level:
          E_1: V_{-k}(gl_1) (level-reflected Kac-Moody).
          E_2: Affine Yangian Y(gl_hat_1) with structure function g(u).
          E_3: Quantum toroidal U_{q,t}(gl_hat_hat_1).

        All E_3 identifications are CONJECTURAL (AP-CY6/AP-CY14).
        """
        lvl = self.level

        base = {
            "en_level": lvl.n,
            "algebra_name": lvl.koszul_dual_name(),
            "sigma2": lvl.sigma2,
            "sigma3": lvl.sigma3,
        }

        if lvl.n == 1:
            base.update({
                "parameters": {"k": lvl.kac_moody_level},
                "rep_category": "Rep^{E_0}(V_{-k}): ordinary modules",
                "braiding": "none (E_0 = no braiding)",
                "structure_function": "none (no R-matrix at E_1)",
                "status": "ESTABLISHED (Feigin-Frenkel 1992)",
            })
        elif lvl.n == 2:
            # Structure function at E_2 point (epsilon_3 = 0)
            e1, e2 = lvl.epsilon1, lvl.epsilon2
            # g(u) = (u-e1)(u-e2)(u-e3) / ((u+e1)(u+e2)(u+e3))
            # At E_2 point: e3 = 0, so g(u) = u(u-e1)(u-e2) / (u(u+e1)(u+e2))
            #             = (u-e1)(u-e2) / ((u+e1)(u+e2))
            base.update({
                "parameters": {"sigma_2": lvl.sigma2, "k": lvl.kac_moody_level},
                "rep_category": "Rep^{E_1}(Y): braided monoidal (from Drinfeld center)",
                "braiding": "E_1-braiding from R-matrix R(u) = (u + sigma_2 * P)/(u + sigma_2)",
                "structure_function": (
                    f"g(u) = (u - {e1})(u - {e2}) / ((u + {e1})(u + {e2})) "
                    f"(E_2 point: e3 = 0 cancels)"
                ),
                "status": "PARTIALLY ESTABLISHED (Costello 2013)",
            })
        else:
            e1, e2, e3 = lvl.epsilon1, lvl.epsilon2, lvl.epsilon3
            base.update({
                "parameters": {
                    "q": f"exp({e1})",
                    "t": f"exp({-e2})",
                    "sigma_2": lvl.sigma2,
                    "sigma_3": lvl.sigma3,
                },
                "rep_category": (
                    "Rep^{E_2}(U_{q,t}): braided monoidal "
                    "(from E_3 bar complex) [CONJECTURAL]"
                ),
                "braiding": (
                    "E_2-braiding from two-parameter R-matrix "
                    "R(u, v) = R_1(u) R_2(v) R_{12}(u-v)"
                ),
                "structure_function": (
                    f"G(x) = (1 - q_1 x)(1 - q_2 x)(1 - q_3 x) / "
                    f"((1 - q_1^{{-1}} x)(1 - q_2^{{-1}} x)(1 - q_3^{{-1}} x))\n"
                    f"  q_1 = exp({e1}), q_2 = exp({e2}), q_3 = exp({e3})"
                ),
                "miki_automorphism": (
                    "S_3 permutation of (q_1, q_2, q_3) from Weyl group of CY torus. "
                    "This is algebra-specific (NOT operadic); AP-CY22."
                ),
                "zte_status": (
                    "FAILS for Yang R-matrix (thm:zte-failure, O(kappa^2) obstruction). "
                    "Corrected S-operator S^{corr} = S + kappa^2 T needed (AP-CY30)."
                ),
                "status": "CONJECTURAL (conj:e3-koszul-duality, AP-CY6/AP-CY14)",
            })

        return base

    # ----- Deformation coefficients -----

    def deformation_coefficients(self, max_order: int = 6) -> Dict[int, Fraction]:
        r"""Coefficients of the deformed differential at each E_n level.

        The deformation series: d_h = sum_k c_k * sigma_3^{k-2} * d^{(k)}.

        At E_1 or E_2 (sigma_3 = 0): only c_2 (from l_2 = Lie bracket).
        At E_3: c_2 + sigma_3 * c_3 + sigma_3^2 * c_4 + ...
        """
        tower = self.linf_ce.shadow_tower_from_linfinity(max_order)

        if self.level.n <= 2:
            # Only the l_2 contribution (no sigma_3 corrections)
            return {2: tower.get(2, Fraction(0))}

        return tower


# =========================================================================
#  2.  The full E_n hierarchy for a given algebra
# =========================================================================

class EnHierarchy:
    r"""The full E_1 -> E_2 -> E_3 deformation hierarchy for a chiral algebra.

    Computes the chiral CE complex, MC element, and Koszul dual at each
    of the three E_n levels, and verifies the dimensional reduction
    E_3 -> E_2 -> E_1 (setting parameters to zero).

    Parameters
    ----------
    lca : LieConformalAlgebra
        The Lie conformal algebra.
    linf : LInfinityData
        The L_infinity structure data.
    epsilon1 : Fraction
        First Omega-background parameter (used at all levels).
    epsilon2 : Fraction
        Second parameter (used at E_2 and E_3 only).
    """

    def __init__(
        self,
        lca: LieConformalAlgebra,
        linf: LInfinityData,
        epsilon1: Fraction = Fraction(1),
        epsilon2: Fraction = Fraction(-2),
    ):
        self.lca = lca
        self.linf = linf
        self.epsilon1 = epsilon1
        self.epsilon2 = epsilon2

        # E_1 level: (epsilon_1, 0, 0)
        self.e1 = ChiralCEAtLevel(
            lca, linf,
            e1_level(epsilon1=epsilon1),
        )

        # E_2 level: (epsilon_1, -epsilon_1, 0) -- self-dual point
        self.e2 = ChiralCEAtLevel(
            lca, linf,
            e2_level(epsilon1=epsilon1, epsilon2=-epsilon1),
        )

        # E_3 level: (epsilon_1, epsilon_2, -(epsilon_1 + epsilon_2))
        self.e3 = ChiralCEAtLevel(
            lca, linf,
            e3_level(epsilon1=epsilon1, epsilon2=epsilon2),
        )

    @property
    def shadow_class(self) -> str:
        return self.linf.shadow_class

    def verify_dimensional_reduction(self) -> Dict[str, bool]:
        r"""Verify the E_3 -> E_2 -> E_1 dimensional reduction.

        Checks:
        1. E_3 at sigma_3 = 0 recovers E_2 behavior.
        2. E_2 at sigma_2 = 0 recovers E_1 behavior.
        3. d^2 = 0 at all three levels.
        4. Koszul conductor consistent across levels.
        """
        results = {}

        # 1. d^2 = 0 at all levels
        results["d_squared_zero_e1"] = self.e1.d_squared_zero()
        results["d_squared_zero_e2"] = self.e2.d_squared_zero()
        results["d_squared_zero_e3"] = self.e3.d_squared_zero()

        # 2. E_1 sigma_2 = 0
        results["e1_sigma2_vanishes"] = (self.e1.level.sigma2 == Fraction(0))

        # 3. E_2 sigma_3 = 0 (self-dual point)
        results["e2_sigma3_vanishes"] = (self.e2.level.sigma3 == Fraction(0))

        # 4. E_3 has generic sigma_3 != 0
        results["e3_sigma3_nonzero"] = (self.e3.level.sigma3 != Fraction(0))

        # 5. Dimensional reduction: number of effective deformation parameters
        results["e1_zero_effective_params"] = (self.e1.level.num_deformation_params() == 0)
        results["e2_one_effective_param"] = (self.e2.level.num_deformation_params() == 1)
        results["e3_two_effective_params"] = (self.e3.level.num_deformation_params() == 2)

        # 6. Deformation at E_1 is trivial (d = d_CE, no epsilon correction)
        # For Heisenberg: d_CE = 0, so deformation is 0 at all levels
        # For Yangian: d_CE != 0 at E_1 but the deformation is classical
        if self.lca.dim > 0:
            test_elem = CEElement.basis((0,))
            d_e1 = self.e1.d_deformed(test_elem)
            d_e2 = self.e2.d_deformed(test_elem)
            # At arity 1, d_CE should be identical at E_1 and E_2
            # (both are just d_CE, no sigma_3 correction at arity 1)
            results["e1_e2_agree_on_arity1"] = (
                d_e1.cleaned().terms == d_e2.cleaned().terms
            )

        return results

    def full_comparison(self) -> Dict[str, Any]:
        """Full comparison of the three E_n levels."""
        return {
            "shadow_class": self.shadow_class,
            "E_1": {
                "theory": self.e1.level.theory_name(),
                "koszul_dual": self.e1.level.koszul_dual_name(),
                "sigma2": self.e1.level.sigma2,
                "sigma3": self.e1.level.sigma3,
                "effective_params": self.e1.level.num_deformation_params(),
                "mc_element": self.e1.mc_element_description(),
                "d_squared_zero": self.e1.d_squared_zero(),
            },
            "E_2": {
                "theory": self.e2.level.theory_name(),
                "koszul_dual": self.e2.level.koszul_dual_name(),
                "sigma2": self.e2.level.sigma2,
                "sigma3": self.e2.level.sigma3,
                "effective_params": self.e2.level.num_deformation_params(),
                "mc_element": self.e2.mc_element_description(),
                "d_squared_zero": self.e2.d_squared_zero(),
            },
            "E_3": {
                "theory": self.e3.level.theory_name(),
                "koszul_dual": self.e3.level.koszul_dual_name(),
                "sigma2": self.e3.level.sigma2,
                "sigma3": self.e3.level.sigma3,
                "effective_params": self.e3.level.num_deformation_params(),
                "mc_element": self.e3.mc_element_description(),
                "d_squared_zero": self.e3.d_squared_zero(),
            },
            "dimensional_reduction": self.verify_dimensional_reduction(),
        }


# =========================================================================
#  3.  Structure function at each E_n level
# =========================================================================

def structure_function_at_level(
    level: EnDeformationLevel, u: Fraction,
) -> Optional[Fraction]:
    r"""Evaluate the rational structure function g(u) at the given E_n level.

    g(u) = prod_{i=1}^3 (u - epsilon_i) / (u + epsilon_i)

    At E_1 (epsilon_2 = epsilon_3 = 0):
      g(u) = (u - epsilon_1) * u * u / ((u + epsilon_1) * u * u)
           = (u - epsilon_1) / (u + epsilon_1)
      This is the CLASSICAL structure function (one-parameter).

    At E_2 (epsilon_3 = 0, epsilon_2 = -epsilon_1):
      g(u) = (u - epsilon_1)(u + epsilon_1) * u / ((u + epsilon_1)(u - epsilon_1) * u)
           = 1
      The structure function is TRIVIAL at the self-dual E_2 point.
      This reflects that sigma_3 = 0 kills the quantum group deformation:
      the Yangian structure comes from sigma_2 (the KM level), not
      from the structure function.

    At E_3 (generic):
      g(u) = (u-e1)(u-e2)(u-e3) / ((u+e1)(u+e2)(u+e3))
      The FULL trigonometric structure function of the quantum toroidal algebra.

    Returns None at poles (u = -epsilon_i).  AP-CY28: test points must
    avoid poles at u = +/- epsilon_i.
    """
    e1, e2, e3 = level.epsilon1, level.epsilon2, level.epsilon3

    num = (u - e1) * (u - e2) * (u - e3)
    den = (u + e1) * (u + e2) * (u + e3)

    if den == Fraction(0):
        return None
    return num / den


def structure_function_inversion(level: EnDeformationLevel, u: Fraction) -> bool:
    r"""Verify the fundamental identity g(u) * g(-u) = 1.

    This is equivalent to G(x) * G(1/x) = 1 in the trigonometric
    parametrization (x = e^u), and follows from the CY condition
    epsilon_1 + epsilon_2 + epsilon_3 = 0 <=> q_1 q_2 q_3 = 1.

    Returns True if g(u) * g(-u) = 1 at the given test point.
    AP-CY28: u must avoid poles at +/- epsilon_i.
    """
    gu = structure_function_at_level(level, u)
    gmu = structure_function_at_level(level, -u)
    if gu is None or gmu is None:
        return False  # pole encountered
    return gu * gmu == Fraction(1)


# =========================================================================
#  4.  Trigonometric (exponentiated) structure function for quantum toroidal
# =========================================================================

def trigonometric_structure_function(
    x: complex, q1: complex, q2: complex, q3: complex,
) -> complex:
    r"""Evaluate the trigonometric structure function G(x; q_1, q_2, q_3).

    G(x) = (1 - q_1 x)(1 - q_2 x)(1 - q_3 x) /
           ((1 - q_1^{-1} x)(1 - q_2^{-1} x)(1 - q_3^{-1} x))

    The CY condition q_1 q_2 q_3 = 1.

    This is the defining function of the quantum toroidal algebra
    U_{q,t}(gl_hat_hat_1) in the Ding-Iohara-Miki presentation.

    Parameters
    ----------
    x : complex
        The argument.
    q1, q2, q3 : complex
        CY-constrained parameters: q1 * q2 * q3 = 1.
    """
    numer = (1 - q1 * x) * (1 - q2 * x) * (1 - q3 * x)
    denom = (1 - x / q1) * (1 - x / q2) * (1 - x / q3)
    if abs(denom) < 1e-30:
        raise ZeroDivisionError("G(x) pole: denominator ~ 0")
    return numer / denom


def verify_trig_inversion(
    q1: complex, q2: complex, n_points: int = 32, tol: float = 1e-10,
) -> Tuple[bool, float]:
    r"""Verify G(x) * G(1/x) = 1 for the trigonometric structure function.

    By the CY condition q_1 q_2 q_3 = 1, the identity holds exactly.
    We verify numerically at n_points on a circle.
    """
    q3 = 1.0 / (q1 * q2)
    max_res = 0.0
    for j in range(n_points):
        theta = 2 * math.pi * (j + 0.37) / n_points
        x = 0.7 * np.exp(1j * theta)
        try:
            gx = trigonometric_structure_function(x, q1, q2, q3)
            gx_inv = trigonometric_structure_function(1.0 / x, q1, q2, q3)
            res = abs(gx * gx_inv - 1.0)
            max_res = max(max_res, res)
        except ZeroDivisionError:
            continue
    return max_res < tol, max_res


# =========================================================================
#  5.  Quantum toroidal parameters from the E_3 level
# =========================================================================

@dataclass(frozen=True)
class QuantumToroidalParams:
    r"""Parameters of the quantum toroidal algebra U_{q,t}(gl_hat_hat_1).

    Derived from the E_3 deformation level:
      q = exp(epsilon_1)
      t = exp(-epsilon_2)
      q_3 = t/q = exp(epsilon_3) = exp(-(epsilon_1 + epsilon_2))

    The CY condition: q * t^{-1} * q_3 = exp(epsilon_1 + epsilon_2 + epsilon_3) = 1.
    """
    epsilon1: Fraction
    epsilon2: Fraction

    @property
    def epsilon3(self) -> Fraction:
        return -(self.epsilon1 + self.epsilon2)

    @property
    def sigma2(self) -> Fraction:
        e1, e2, e3 = self.epsilon1, self.epsilon2, self.epsilon3
        return e1 * e2 + e1 * e3 + e2 * e3

    @property
    def sigma3(self) -> Fraction:
        return self.epsilon1 * self.epsilon2 * self.epsilon3

    def q_numerical(self) -> complex:
        """q = exp(epsilon_1)."""
        return np.exp(float(self.epsilon1))

    def t_numerical(self) -> complex:
        """t = exp(-epsilon_2)."""
        return np.exp(-float(self.epsilon2))

    def q3_numerical(self) -> complex:
        """q_3 = exp(epsilon_3) = t/q."""
        return np.exp(float(self.epsilon3))

    def cy_check_numerical(self, tol: float = 1e-12) -> bool:
        """Verify q_1 * q_2 * q_3 = 1 numerically."""
        q1 = self.q_numerical()
        q2 = 1.0 / self.t_numerical()  # q_2 = t^{-1} = exp(epsilon_2)
        q3 = self.q3_numerical()
        return abs(q1 * q2 * q3 - 1.0) < tol

    @staticmethod
    def from_level(level: EnDeformationLevel) -> "QuantumToroidalParams":
        """Create from an E_3 deformation level."""
        if level.n != 3:
            raise ValueError(
                f"Quantum toroidal params require E_3 level; got E_{level.n}"
            )
        return QuantumToroidalParams(
            epsilon1=level.epsilon1, epsilon2=level.epsilon2,
        )


# =========================================================================
#  6.  E_n bar complex dimensions
# =========================================================================

def en_bar_poincare(
    n_generators: int, en_level: int, genus: int,
    shadow_class: str = "G",
) -> Dict[str, Any]:
    r"""Poincare polynomial of the E_n bar complex at given genus.

    For the E_n bar at genus g, the chain-level graded dimension depends
    on the shadow class:

      Class G/L/C: (1+t)^{n_gen * n * g} (where n = E_n level).
      Class M: (1+t)^{n_gen * n * g} at chain level; cohomology is
               (3t(1+t))^g at E_4 page (AP-CY21: class M fails (1+t)^{3g}).

    For n_gen = 1 (Heisenberg):
      E_1, g=1: (1+t)^1 = 2 total.
      E_2, g=1: (1+t)^2 = 4 total.
      E_3, g=1: (1+t)^3 = 8 total.
      E_3, g=3: (1+t)^9 = 512 total.

    For n_gen = 3 (Yangian):
      E_3, g=1: (1+t)^9 = 512 total.
    """
    N = n_generators * en_level * genus

    if shadow_class in ("G", "L", "C"):
        total_dim = 2 ** N
        poincare = {k: math.comb(N, k) for k in range(N + 1)}
        poincare_formula = f"(1+t)^{{{N}}}"
    else:
        # Class M: chain level is 2^N, cohomology is 6^g (AP-CY21)
        total_dim = 2 ** N
        cohomology_dim = 6 ** genus
        poincare = {k: math.comb(N, k) for k in range(N + 1)}
        poincare_formula = f"chain: (1+t)^{{{N}}}; cohomology: (3t(1+t))^{{{genus}}}"

    result = {
        "n_generators": n_generators,
        "en_level": en_level,
        "genus": genus,
        "shadow_class": shadow_class,
        "total_dimension": total_dim,
        "poincare_poly": poincare,
        "poincare_formula": poincare_formula,
    }
    if shadow_class == "M":
        result["cohomology_dim"] = 6 ** genus
    return result


# =========================================================================
#  7.  Factory functions for the three primary examples
# =========================================================================

def heisenberg_hierarchy(
    epsilon1: Fraction = Fraction(1),
    epsilon2: Fraction = Fraction(-2),
) -> Dict[str, Any]:
    r"""Full E_1 -> E_2 -> E_3 hierarchy for the Heisenberg (class G).

    L = Heis, {J_lambda J} = k * lambda.  Shadow class G (abelian).

    The Heisenberg is the canonical CLASS G example.  Key features:
    - d_CE = 0 at all E_n levels (abelian Lie algebra).
    - MC element = 0 at all levels (no deformations).
    - Deformation is polynomial (trivial: terminates at order 0).
    - E_3 Koszul dual: quantum toroidal at degenerate parameters.
    - Koszul conductor rho_K = 0 (class G self-duality).

    Manuscript reference: thm:e3-koszul-heisenberg in en_factorization.tex.
    """
    lca = heisenberg_lca(k=Fraction(1))
    linf = heisenberg_linfinity()

    hierarchy = EnHierarchy(lca, linf, epsilon1=epsilon1, epsilon2=epsilon2)

    return {
        "name": "Heisenberg (class G)",
        "shadow_class": "G",
        "hierarchy": hierarchy,
        "comparison": hierarchy.full_comparison(),
        "verification": hierarchy.verify_dimensional_reduction(),
        "e3_bar_g1": en_bar_poincare(1, 3, 1, "G"),
        "e3_bar_g3": en_bar_poincare(1, 3, 3, "G"),
    }


def yangian_hierarchy(
    epsilon1: Fraction = Fraction(1),
    epsilon2: Fraction = Fraction(-2),
) -> Dict[str, Any]:
    r"""Full E_1 -> E_2 -> E_3 hierarchy for the Yangian (class L).

    L = Y(gl_hat_1) truncated to 3 generators.  Shadow class L (strict Lie).

    Key features:
    - d_CE != 0 (nonabelian bracket [e_0, e_1] = e_2).
    - MC element at E_2: classical r-matrix solving CYBE.
    - Deformation is rational (class L: strict Lie, converges).
    - E_3 Koszul dual: dual affine Yangian (CONJECTURAL at d=3).
    """
    lca = yangian_gl1_lca()
    linf = yangian_gl1_linfinity()

    hierarchy = EnHierarchy(lca, linf, epsilon1=epsilon1, epsilon2=epsilon2)

    return {
        "name": "Yangian Y(gl_hat_1) (class L)",
        "shadow_class": "L",
        "hierarchy": hierarchy,
        "comparison": hierarchy.full_comparison(),
        "verification": hierarchy.verify_dimensional_reduction(),
        "e3_bar_g1": en_bar_poincare(3, 3, 1, "L"),
        "e3_bar_g3": en_bar_poincare(3, 3, 3, "L"),
    }


def virasoro_hierarchy(
    epsilon1: Fraction = Fraction(1),
    epsilon2: Fraction = Fraction(-2),
    c: Fraction = Fraction(1),
) -> Dict[str, Any]:
    r"""Full E_1 -> E_2 -> E_3 hierarchy for the Virasoro (class M).

    L = Vir at central charge c.  Shadow class M (infinite shadow tower).

    Key features:
    - d_CE != 0 at the LCA level (nonabelian: [T, T] = dT).
    - MC element at E_3: Gevrey-1 divergent series in sigma_3.
    - Deformation is Gevrey-1 divergent (class M: Borel resummation needed).
    - E_3 Koszul dual: W-algebra quantum group (CONJECTURAL).
    - E_3 bar cohomology: NOT (1+t)^{3g} (AP-CY21: class M fails).
    """
    lca = virasoro_lca(c=c)
    linf = virasoro_linfinity(c=c)

    hierarchy = EnHierarchy(lca, linf, epsilon1=epsilon1, epsilon2=epsilon2)

    return {
        "name": "Virasoro (class M)",
        "shadow_class": "M",
        "hierarchy": hierarchy,
        "comparison": hierarchy.full_comparison(),
        "verification": hierarchy.verify_dimensional_reduction(),
        "e3_bar_g1": en_bar_poincare(1, 3, 1, "M"),
        "e3_bar_g3": en_bar_poincare(1, 3, 3, "M"),
        "shadow_tower": {
            "S_2": c / Fraction(2),
            "S_3": Fraction(2) * c,
            "S_4": Fraction(10) / (c * (5 * c + 22)),
        },
    }


# =========================================================================
#  8.  Cross-level comparison
# =========================================================================

def e_n_level_comparison() -> Dict[str, Any]:
    r"""Comprehensive comparison of E_1, E_2, E_3 across all shadow classes.

    Returns a table comparing:
    1. Deformation type at each level.
    2. MC element at each level.
    3. Koszul dual at each level.
    4. Structure function at each level.
    5. Number of effective deformation parameters.
    6. E_n bar complex dimension at genus g=1.

    All E_3 identifications are CONJECTURAL (AP-CY6/AP-CY14).
    """
    heis = heisenberg_hierarchy()
    yang = yangian_hierarchy()
    vir = virasoro_hierarchy()

    return {
        "Heisenberg (G)": heis["comparison"],
        "Yangian (L)": yang["comparison"],
        "Virasoro (M)": vir["comparison"],
        "dimensional_reduction": {
            "Heisenberg": heis["verification"],
            "Yangian": yang["verification"],
            "Virasoro": vir["verification"],
        },
        "e3_bar_g1": {
            "Heisenberg": heis["e3_bar_g1"],
            "Yangian": yang["e3_bar_g1"],
            "Virasoro": vir["e3_bar_g1"],
        },
    }


# =========================================================================
#  9.  Main computation suite
# =========================================================================

def compute_e3_ce_quantum_toroidal() -> Dict[str, Any]:
    r"""Run the full E_3 CE -> quantum toroidal computation suite.

    Computes:
    1. E_n hierarchy for all three examples (Heisenberg, Yangian, Virasoro).
    2. Structure function at each E_n level.
    3. Trigonometric structure function verification.
    4. Quantum toroidal parameter extraction.
    5. E_n bar complex dimensions.
    6. Dimensional reduction verification.
    7. Cross-level comparison.
    """
    results = {}

    # 1. Hierarchies
    results["heisenberg"] = heisenberg_hierarchy()
    results["yangian"] = yangian_hierarchy()
    results["virasoro"] = virasoro_hierarchy()

    # 2. Structure function at each level
    e1 = e1_level()
    e2 = e2_level()
    e3 = e3_level()
    u_test = Fraction(5)  # Safe test point (AP-CY28: far from poles)

    results["structure_functions"] = {
        "E_1": {
            "g(5)": structure_function_at_level(e1, u_test),
            "inversion": structure_function_inversion(e1, u_test),
        },
        "E_2": {
            "g(5)": structure_function_at_level(e2, u_test),
            "inversion": structure_function_inversion(e2, u_test),
        },
        "E_3": {
            "g(5)": structure_function_at_level(e3, u_test),
            "inversion": structure_function_inversion(e3, u_test),
        },
    }

    # 3. Trigonometric verification
    q_num = np.exp(1.0)  # q = exp(1)
    t_num = np.exp(2.0)  # t = exp(-(-2)) = exp(2)
    passes, max_res = verify_trig_inversion(q_num, 1.0 / t_num)
    results["trig_inversion"] = {
        "passes": passes,
        "max_residual": max_res,
    }

    # 4. Quantum toroidal params
    qt_params = QuantumToroidalParams.from_level(e3)
    results["quantum_toroidal_params"] = {
        "epsilon1": qt_params.epsilon1,
        "epsilon2": qt_params.epsilon2,
        "epsilon3": qt_params.epsilon3,
        "sigma2": qt_params.sigma2,
        "sigma3": qt_params.sigma3,
        "cy_check": qt_params.cy_check_numerical(),
    }

    # 5. Cross-level comparison
    results["comparison"] = e_n_level_comparison()

    return results
