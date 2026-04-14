r"""E_3-chiral deformation theory of Chevalley-Eilenberg (co)chains.

MATHEMATICAL FRAMEWORK
======================

In CFG25 (Costello-Francis-Gwilliam), the 3d holomorphic CS theory on C x R
produces the CE chain complex CE_*(g) of a Lie algebra g. The CE chains carry
an E_3 structure from the 3d embedding, and the quantum deformation
CE_*(g)[[hbar]] = Obs^q(R^3) is the quantized CS observables. The E_3 Koszul
dual of CE_*(g) is the quantum group U_q(g).

This module develops the CHIRAL analogue: the E_3-chiral deformation theory
of CE^{ch}_*(L) where L is a Lie conformal algebra. The key innovation is the
replacement of C x R by C^3, and the three independent deformation directions
(hbar_1, hbar_2, hbar_3) corresponding to the Omega-background parameters
(h_1, h_2, h_3) with h_1 + h_2 + h_3 = 0 (CY condition).

THE SIX COMPONENTS
==================

1. CHIRAL CE COMPLEX CE^{ch}_*(L): Already implemented in chiral_ce_complex.py.
   Here we wrap it with E_3 metadata and the three-parameter deformation.

2. E_3 STRUCTURE FROM 6d EMBEDDING: The three independent commuting differentials
   d_1, d_2, d_3 on CE^{ch}_*(L) from the three complex directions on C^3.
   The total differential is d_h = d_CE + h_1*d_1 + h_2*d_2 + h_3*d_3.
   The CY condition h_1+h_2+h_3=0 ensures d_h^2 = 0.

3. QUANTUM DEFORMATION CE^{ch}_*(L)[[h_1,h_2,h_3]]: The formal power series
   deformation of the CE complex. The deformed differential d_h encodes the
   Omega-background. The deformation is TRIVIAL for class G (Heisenberg),
   RATIONAL for class L (Yangian), and GEVREY-1 DIVERGENT for class M (Virasoro).

4. E_3 KOSZUL DUAL: For L = gl_1 (Heisenberg), the E_3 Koszul dual is the
   quantum toroidal algebra U_{q,t}(gl_hat_hat_1). For L = g (Kac-Moody),
   the E_3 Koszul dual is the affine Yangian Y(g_hat). This is CONJECTURAL
   for d=3 (CY-A_3 not proved; AP-CY6/AP-CY14).

5. L_INFINITY DEFORMATION THEORY: Maurer-Cartan elements in CE^{ch,*}(L)[1]
   are the classical deformations of L. The MC equation
       d_CE(alpha) + (1/2)[alpha, alpha] + (1/6)l_3(alpha,alpha,alpha) + ... = 0
   has solutions parametrized by the shadow class:
   - Class G: MC space = point (no deformations of abelian Lie algebra)
   - Class L: MC space = finite-dimensional (rational)
   - Class M: MC space = infinite-dimensional (Gevrey-1)

6. DERIVED MODULI: MC(CE^{ch,*}(L)) as a derived stack. The tangent complex
   is CE^{ch,*}(L)[1], and the obstruction space is CE^{ch,2}(L). The
   formal moduli problem is governed by the L_infinity algebra CE^{ch,*}(L)[1].

THE THREE EXAMPLES
==================

HEISENBERG (class G):
  L = Heis, {J_lambda J} = k*lambda.
  CE^{ch}_*(Heis) = Lambda^*(J) with d_CE = 0 (abelian).
  d_h = 0 for all h (diagonal embedding: CY forces total deformation to vanish).
  E_3 Koszul dual: quantum toroidal at (q,t) with sigma_3 = 0 (free field limit).
  MC space: {0} (no nontrivial Maurer-Cartan elements).
  Derived moduli: point (no deformations).
  Deformation type: polynomial (trivial, already converges at order 0).

YANGIAN Y(gl_hat_1) (class L):
  L = Y, strict Lie conformal algebra with 3 generators e_0, e_1, e_2.
  CE^{ch}_*(Y) = Lambda^*(e_0, e_1, e_2) with standard CE differential.
  d_h deforms the bracket: {e_i, e_j}_h = {e_i, e_j} + h*delta_{ij}(...).
  E_3 Koszul dual: quantum toroidal U_{q,t}(gl_hat_hat_1) at generic parameters.
  MC space: affine space of dimension rank(g) (rational, finite).
  Derived moduli: smooth stack (BTT unobstructedness for class L).
  Deformation type: rational (converges in a disk, class L).

VIRASORO (class M):
  L = Vir, {T_lambda T} = (d+2*lambda)*T + (c/12)*lambda^3.
  CE^{ch}_*(Vir) = Lambda^*(T) with d_CE involving dT.
  d_h has ALL-ORDER corrections from the infinite shadow tower:
    d_h = d_CE + h*d_1 + h^2*d_2(l_3) + h^3*d_3(l_4) + ...
  where d_k(l_{k+1}) is built from the L_infinity map l_{k+1}.
  E_3 Koszul dual: W-algebra quantum group (CONJECTURAL, AP-CY14).
  MC space: formal neighborhood of 0 with Gevrey-1 divergent series.
  Derived moduli: singular stack (obstructions from l_3, l_4, ...).
  Deformation type: Gevrey-1 divergent (class M, Borel resummation needed).

SHADOW CLASS -> DEFORMATION ANALYTIC TYPE
==========================================

  G = polynomial:    deformation is polynomial in h (finitely many terms).
  L = rational:      deformation converges in a disk (rational series).
  C = convergent:    deformation converges (charge-conservation protects).
  M = Gevrey-1:      deformation is divergent, requires Borel resummation.

This is the dictionary from rem:shadow-ainfty-coproduct-vol3: the shadow
invariants S_k are the coefficients of the deformation, and the shadow class
controls the analytic type of the deformation series.

AP COMPLIANCE
=============
- All formal statements about d=3 use conjecture environment (AP-CY6/AP-CY14).
- The E_3 claim uses the topological E_3 from configuration spaces of C^3,
  NOT the algebraic E_3 from the Deligne conjecture (AP154).
- kappa always subscripted: kappa_ch (AP113).
- E_3 bar: (1+t)^{3g} for class L,C ONLY. Fails for class M (AP-CY21).
- MC moduli requires COMPLETE shadow tower computation (AP-CY12).

CONVENTIONS
===========
- h = (h_1, h_2, h_3) with h_1+h_2+h_3=0 (CY condition).
- sigma_2 = h_1*h_2 + h_1*h_3 + h_2*h_3 (the Kac-Moody level).
- sigma_3 = h_1*h_2*h_3 (the cubic invariant = kappa of the Yangian).
- Cohomological grading (|d| = +1).
- Bar desuspension: |s^{-1}a| = |a| - 1 (AP45).
- For L_infinity: d_CE = sum_{k>=2} d^{(k)} where d^{(k)} from l_k.

MANUSCRIPT REFERENCES
=====================
- chapters/theory/quantum_chiral_algebras.tex, subsec:ce-deformation-e3
  (Construction constr:quantum-ce-deformation)
- chapters/theory/quantum_chiral_algebras.tex, rem:two-e3-ap154
  (Two E_3 structures: algebraic vs topological)
- chapters/theory/en_factorization.tex, conj:e3-koszul-duality
  (E_3-chiral Koszul duality from 6d theory)
- compute/lib/chiral_ce_complex.py (CE chains and L_infinity deformation)
- compute/lib/deformed_chiral_ce_engine.py (deformed d_CE for V_k(gl_1))
- compute/lib/holomorphic_cs_chiral_engine.py (hol CS hierarchy)
- compute/lib/e3_two_parameter_rmatrix.py (two-parameter R-matrix)
- compute/lib/zamolodchikov_tetrahedron_engine.py (ZTE obstruction)

MATHEMATICAL SOURCES
====================
- Costello-Francis-Gwilliam, "CS theory and factorisation homology" (2024)
- Costello-Gwilliam, "Factorization algebras in QFT" I-II (2017, 2021)
- Costello, "Supersymmetric gauge theory and the Yangian" (2013)
- Loday-Vallette, "Algebraic Operads" (2012): CE and bar-cobar
- Lurie, "Higher Algebra" (2017): E_n operads, Koszul duality
- Kontsevich, "Deformation quantization of Poisson manifolds" (2003)
- Goldman-Millson (1988): MC moduli of dgLa
"""

from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

import numpy as np
from sympy import (
    Matrix,
    Rational,
    Symbol,
    binomial,
    cancel,
    expand,
    factor,
    oo,
    simplify,
    sqrt,
    symbols,
)

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


# =========================================================================
#  0.  Omega-background and CY condition
# =========================================================================

@dataclass(frozen=True)
class OmegaParams:
    r"""Omega-background parameters (h_1, h_2, h_3) with h_1+h_2+h_3=0.

    These parametrize the E_3-chiral deformation from the 6d holomorphic
    theory on C^3. The CY condition h_1+h_2+h_3=0 is enforced.

    sigma_2 = h_1*h_2 + h_1*h_3 + h_2*h_3 = -(h_1^2+h_2^2+h_3^2)/2
    sigma_3 = h_1*h_2*h_3

    For the Kac-Moody level: k = -sigma_2.
    For the Yangian: sigma_3 is the cubic Casimir.
    For quantum toroidal: (q,t) = (e^{h_1}, e^{-h_2}).
    """
    h1: Fraction
    h2: Fraction

    @property
    def h3(self) -> Fraction:
        return -(self.h1 + self.h2)

    @property
    def sigma2(self) -> Fraction:
        """sigma_2 = h_1*h_2 + h_1*h_3 + h_2*h_3."""
        return self.h1 * self.h2 + self.h1 * self.h3 + self.h2 * self.h3

    @property
    def sigma3(self) -> Fraction:
        """sigma_3 = h_1*h_2*h_3 = cubic invariant."""
        return self.h1 * self.h2 * self.h3

    @property
    def is_self_dual(self) -> bool:
        """At the self-dual point, one h_i = 0."""
        return self.h1 == 0 or self.h2 == 0 or self.h3 == 0

    @property
    def kac_moody_level(self) -> Fraction:
        """Effective Kac-Moody level k = -sigma_2."""
        return -self.sigma2

    def cy_check(self) -> bool:
        """Verify h_1+h_2+h_3 = 0."""
        return self.h1 + self.h2 + self.h3 == 0

    def structure_function(self, u: Fraction) -> Optional[Fraction]:
        """Evaluate g(u) = prod(u-h_i)/prod(u+h_i).

        Returns None if the denominator vanishes (pole at u = -h_i).
        AP-CY28: test points must avoid poles at z = +/- h_i.
        """
        num = (u - self.h1) * (u - self.h2) * (u - self.h3)
        den = (u + self.h1) * (u + self.h2) * (u + self.h3)
        if den == 0:
            return None
        return num / den


# =========================================================================
#  1.  E_3-chiral deformation of CE complex
# =========================================================================

class E3ChiralCEDeformation:
    r"""E_3-chiral deformation of the CE complex of a Lie conformal algebra.

    The deformed differential is:
        d_h = d_CE + h_1 * partial_1 + h_2 * partial_2 + h_3 * partial_3

    where partial_i are the equivariant operators from the i-th C^* action
    on C^3. For the diagonal embedding (CY_3), w_i(n) = n for all i, and
    the CY condition h_1+h_2+h_3=0 forces h_1*w_1+h_2*w_2+h_3*w_3 = 0,
    so d_h = d_CE (the deformation is trivial for the diagonal embedding).

    The nontrivial deformation arises from the L_infinity corrections:
        d_h^{full} = d_CE + h*d_1 + h^2*d_2(l_3) + h^3*d_3(l_4) + ...

    where h = sigma_3 is the effective deformation parameter and d_k(l_{k+1})
    is the CE-type differential built from the L_infinity map l_{k+1}.

    The shadow class determines the analytic type of the deformation series:
        G: polynomial (truncates)
        L: rational (converges)
        C: convergent (charge-protected)
        M: Gevrey-1 divergent (Borel resummable)

    Parameters
    ----------
    lca : LieConformalAlgebra
        The underlying Lie conformal algebra.
    linf : LInfinityData
        The L_infinity structure data.
    omega : OmegaParams
        The Omega-background parameters.
    """

    def __init__(
        self,
        lca: LieConformalAlgebra,
        linf: LInfinityData,
        omega: OmegaParams,
    ):
        self.lca = lca
        self.linf = linf
        self.omega = omega
        self.ce = CEChainComplex(lca)
        self.linf_ce = LInfinityCEComplex(lca, linf)

    @property
    def shadow_class(self) -> str:
        return self.linf.shadow_class

    @property
    def deformation_type(self) -> str:
        """Analytic type of the deformation series.

        From the shadow class -> QGL analytic type dictionary:
            G = polynomial
            L = rational
            C = convergent
            M = Gevrey-1 divergent (Borel)
        """
        types = {
            "G": "polynomial",
            "L": "rational",
            "C": "convergent",
            "M": "Gevrey-1 divergent",
        }
        return types.get(self.shadow_class, "unknown")

    def d_h_arity1(self, gen_idx: int) -> CEElement:
        r"""Apply d_h on a single generator (arity 1).

        For diagonal embedding: d_h = d_CE on arity 1, since the
        equivariant deformation vanishes by h_1+h_2+h_3=0.

        d_CE(g_i) = 0 for arity 1 (no binary bracket to contract).
        """
        elem = CEElement.basis((gen_idx,))
        return self.ce.d_CE(elem)

    def d_h_arity2(self, i: int, j: int) -> CEElement:
        r"""Apply d_h on an arity-2 element g_i ^ g_j.

        d_h(g_i ^ g_j) = d_CE(g_i ^ g_j) + equivariant correction.

        For diagonal embedding: equivariant correction = 0 by CY.
        The result is the standard CE differential = [g_i, g_j].
        """
        elem = CEElement.basis((i, j))
        return self.ce.d_CE(elem)

    def d_h_full(self, elem: CEElement, max_order: int = 4) -> CEElement:
        r"""Apply the full deformed differential d_h through order max_order.

        d_h = d_CE + sigma_3 * d^{(3)} + sigma_3^2 * d^{(4)} + ...

        The L_infinity corrections are weighted by powers of sigma_3.
        For class G: sigma_3 * d^{(3)} = 0 (no l_3).
        For class L: terminates at finite order.
        For class M: infinite series, truncated at max_order.
        """
        # d_CE part (from l_2)
        result = self.ce.d_CE(elem)

        # L_infinity corrections weighted by sigma_3
        sigma3 = self.omega.sigma3
        if max_order >= 3 and sigma3 != 0:
            d3 = self.linf_ce._d3(elem)
            result = result + Fraction(sigma3) * d3

        if max_order >= 4 and sigma3 != 0:
            d4 = self.linf_ce._d4(elem)
            result = result + Fraction(sigma3 ** 2) * d4

        return result.cleaned()

    def d_h_squared_zero(self, max_arity: int = 3) -> bool:
        r"""Verify d_h^2 = 0 on basis elements up to given arity.

        For the Lie conformal algebra part: d_CE^2 = 0 by Jacobi identity.
        For the L_infinity corrections: (d_CE + d^{(3)} + d^{(4)} + ...)^2 = 0
        holds order by order in sigma_3 when l_k satisfy the L_infinity relations.

        For abelian (class G): trivially d_h = 0 on everything.
        For class L: d_CE^2 = 0 suffices (no higher corrections).
        For class M: checked to finite order.
        """
        n = self.lca.dim
        for k in range(1, min(max_arity + 1, n + 1)):
            from itertools import combinations
            for indices in combinations(range(n), k):
                elem = CEElement.basis(indices)
                d1 = self.d_h_full(elem)
                d2 = self.d_h_full(d1) if not d1.cleaned().is_zero() else CEElement.zero()
                if not d2.cleaned().is_zero():
                    return False
        return True

    def deformation_series_radius(self) -> str:
        """Convergence radius of the deformation series in sigma_3.

        Class G: radius = infinity (polynomial, finitely many terms).
        Class L: radius = finite nonzero (rational, converges in a disk).
        Class M: radius = 0 (Gevrey-1, divergent, needs Borel resummation).
        """
        radii = {
            "G": "infinity (polynomial: finite terms, exact)",
            "L": "finite nonzero (rational: converges in a disk)",
            "C": "finite nonzero (convergent: charge-conservation protects)",
            "M": "zero (Gevrey-1: divergent, Borel resummable)",
        }
        return radii.get(self.shadow_class, "unknown")

    def deformation_coefficients(self, max_order: int = 6) -> Dict[int, Fraction]:
        r"""Coefficients of the deformation series d_h = sum c_k * sigma_3^k * d^{(k)}.

        c_2 = 1 (the Lie bracket, always present)
        c_3 = sigma_3 * l_3 contribution
        c_4 = sigma_3^2 * l_4 contribution
        ...

        For class G: c_k = 0 for k >= 3.
        For class L: c_k = 0 for k >= shadow_depth + 1.
        For class M: c_k != 0 for all k.

        Returns {order: coefficient} from the shadow tower.
        """
        tower = self.linf_ce.shadow_tower_from_linfinity(max_order)
        return tower


# =========================================================================
#  2.  Quantum deformation algebra
# =========================================================================

class QuantumCEDeformation:
    r"""The quantum deformation CE^{ch}_*(L)[[h_1,h_2,h_3]].

    This is the formal power series deformation of the chiral CE complex
    by the Omega-background parameters. The deformation is controlled by
    three parameters (h_1, h_2, h_3) satisfying h_1+h_2+h_3=0, leaving
    two independent parameters.

    The deformed algebra carries:
    1. A deformed differential d_h (from E3ChiralCEDeformation)
    2. A deformed product (from the Omega-deformed OPE)
    3. A deformed coproduct (from the chiral coproduct of Vol I)

    The E_3 structure manifests as THREE commuting differentials:
        d_1: from the first complex direction on C^3
        d_2: from the second complex direction on C^3
        d_3: from the third complex direction on C^3

    with d_h = d_1 + d_2 + d_3 (not the sum h_i*d_i, which vanishes by CY).

    Parameters
    ----------
    e3_def : E3ChiralCEDeformation
        The E_3-chiral deformation data.
    """

    def __init__(self, e3_def: E3ChiralCEDeformation):
        self.e3 = e3_def
        self.omega = e3_def.omega
        self.shadow_class = e3_def.shadow_class

    @property
    def num_deformation_params(self) -> int:
        """Number of independent deformation parameters.

        h_1+h_2+h_3=0 gives 2 free parameters. But sigma_2 is a trivial
        deformation (rescaling of the bracket), leaving sigma_3 as the
        single essential parameter.

        For E_3: 2 independent from (h_1,h_2) with h_3=-h_1-h_2.
        """
        return 2

    @property
    def essential_param(self) -> Fraction:
        """The essential (non-rescaling) deformation parameter sigma_3.

        sigma_2 rescales the bracket: {a,b} -> sigma_2 * {a,b}.
        sigma_3 is the genuine deformation (cubic Casimir).
        """
        return self.omega.sigma3

    def quantum_differential_order(self, order: int) -> str:
        r"""Description of the quantum differential at given order in sigma_3.

        Order 0: d_CE (classical)
        Order 1: sigma_3 * d^{(3)} from l_3 (first quantum correction)
        Order 2: sigma_3^2 * d^{(4)} from l_4 (second quantum correction)
        ...

        The shadow tower coefficient S_{k+2} controls the order-k correction.
        """
        if order == 0:
            return "d_CE (classical Lie bracket)"
        elif order == 1:
            if self.shadow_class == "G":
                return "0 (class G: l_3 = 0, no quantum correction)"
            return "sigma_3 * d^{(3)} from l_3 (Jacobiator/associator)"
        elif order == 2:
            if self.shadow_class == "G":
                return "0 (class G: l_4 = 0)"
            if self.shadow_class == "L":
                return "0 (class L: shadow terminates before order 2)"
            return "sigma_3^2 * d^{(4)} from l_4 (quartic correction)"
        else:
            if self.shadow_class == "G":
                return f"0 (class G: truncated at order 0)"
            if self.shadow_class == "L":
                depth = self.e3.linf.shadow_depth or 2
                if order >= depth - 1:
                    return f"0 (class L: shadow terminates at depth {depth})"
            return f"sigma_3^{order} * d^{{({order+2})}} from l_{order+2}"

    def e3_tricomplex_page(self, genus: int) -> Dict[str, Any]:
        r"""The E_3 tricomplex page at given genus.

        For the E_3 bar at genus g, the tricomplex has three commuting
        differentials d_1, d_2, d_3 and the chain-level dimension is P(q)^{3g}.

        The COHOMOLOGY depends on the shadow class (AP-CY21):
            Class G: P(q)^{3g} (formal, chain = cohomology for free field)
            Class L: (1+t)^{3g} (dim 2^{3g} = 8^g)
            Class C: (1+t)^{3g} (charge conservation kills d_4)
            Class M: 6^g at E_4 page (d_4 survives, (3t(1+t))^g)
        """
        n = self.e3.lca.dim
        if self.shadow_class in ("G", "L", "C"):
            total_dim = 2 ** (n * 3 * genus)
            cohomology_dim = 2 ** (n * 3 * genus)
            poincare_formula = f"(1+t)^{{{n * 3 * genus}}}"
        else:  # class M
            # E_4 page: (3t(1+t))^g, dim 6^g
            total_dim = 2 ** (n * 3 * genus)  # chain level
            cohomology_dim = 6 ** genus  # E_4 = E_inf for g <= 3
            poincare_formula = f"(3t(1+t))^{genus} (E_4 page)"

        return {
            "genus": genus,
            "shadow_class": self.shadow_class,
            "chain_dim": total_dim,
            "cohomology_dim": cohomology_dim,
            "poincare": poincare_formula,
            "n_generators": n,
            "n_differentials": 3,
        }


# =========================================================================
#  3.  E_3 Koszul dual identification
# =========================================================================

class E3KoszulDual:
    r"""E_3 Koszul dual of the chiral CE complex.

    The E_3 Koszul dual A^! = D_{C^3}(B_{E_3}(A)) is the Verdier dual
    of the E_3 bar complex on C^3.

    For V_k(g) (Kac-Moody): A^! carries E_3-chiral structure with
    inverted parameters (h_1,h_2,h_3) -> (-h_1,-h_2,-h_3).

    The conductor relation: kappa_ch(A) + kappa_ch(A^!) = rho_K
    where rho_K is the family-dependent conductor.

    All identifications with quantum groups are CONJECTURAL for d=3
    (AP-CY6/AP-CY14: CY-A_3 not proved). We use conjecture status throughout.

    Parameters
    ----------
    e3_def : E3ChiralCEDeformation
        The E_3-chiral deformation data.
    """

    def __init__(self, e3_def: E3ChiralCEDeformation):
        self.e3 = e3_def
        self.omega = e3_def.omega
        self.shadow_class = e3_def.shadow_class

    @property
    def dual_omega(self) -> OmegaParams:
        """Inverted Omega-background for the Koszul dual.

        (h_1,h_2,h_3) -> (-h_1,-h_2,-h_3).
        sigma_2 -> sigma_2 (even), sigma_3 -> -sigma_3 (odd).
        """
        return OmegaParams(h1=-self.omega.h1, h2=-self.omega.h2)

    @property
    def conductor(self) -> Fraction:
        r"""The Koszul conductor rho_K: kappa_ch(A) + kappa_ch(A^!) = rho_K.

        Class G (Heisenberg): rho_K = 0 (self-dual, kappa_ch + kappa_ch^! = 0).
        Class L (Yangian): rho_K depends on the family.
        Class M (Virasoro): rho_K = K (central charge dependent).

        For K3: rho_K = 0 (free-field/KM branch, from CLAUDE.md).
        """
        if self.shadow_class == "G":
            return Fraction(0)
        elif self.shadow_class == "L":
            # For Yangian: conductor from the bracket structure
            # At the self-dual point: rho_K = 0
            if self.omega.is_self_dual:
                return Fraction(0)
            return -2 * self.omega.sigma2  # 2k for KM at level k
        else:
            # Class M: central-charge-dependent
            return Fraction(0)  # Placeholder

    def koszul_dual_algebra_name(self) -> str:
        """Conjectural identification of the E_3 Koszul dual algebra.

        CONJECTURAL (AP-CY6/AP-CY14): all identifications with quantum groups
        at d=3 are conditional on CY-A_3.
        """
        if self.shadow_class == "G":
            return "Quantum toroidal U_{q^{-1},t^{-1}}(gl_hat_hat_1) [CONJECTURAL]"
        elif self.shadow_class == "L":
            return "Dual affine Yangian Y^!(g_hat) [CONJECTURAL]"
        elif self.shadow_class == "M":
            return "W-algebra quantum group [CONJECTURAL]"
        return "Unknown [CONJECTURAL]"

    def parameter_inversion_check(self) -> Dict[str, Any]:
        """Verify the parameter inversion symmetry of Koszul duality.

        sigma_2 is EVEN under inversion: sigma_2(-h) = sigma_2(h).
        sigma_3 is ODD: sigma_3(-h) = -sigma_3(h).

        The level k = -sigma_2 is preserved: k^! = k.
        The cubic parameter flips: sigma_3^! = -sigma_3.
        """
        dual = self.dual_omega
        return {
            "sigma2_preserved": self.omega.sigma2 == dual.sigma2,
            "sigma3_flipped": self.omega.sigma3 == -dual.sigma3,
            "level_preserved": self.omega.kac_moody_level == dual.kac_moody_level,
            "conductor": self.conductor,
        }

    def koszul_dual_shadow_class(self) -> str:
        """Shadow class of the Koszul dual algebra.

        The Koszul dual preserves the shadow class (it inverts parameters
        but does not change the analytic type of the structure functions).
        """
        return self.shadow_class


# =========================================================================
#  4.  L_infinity deformation theory and Maurer-Cartan
# =========================================================================

class ChiralMCDeformation:
    r"""Maurer-Cartan deformation theory of the chiral CE cochains.

    The L_infinity algebra governing deformations of L is CE^{ch,*}(L)[1],
    the shifted CE cochains. Maurer-Cartan elements are solutions to:

        d(alpha) + (1/2)[alpha, alpha] + (1/3!)l_3(alpha,...) + ... = 0

    where d is the CE codifferential, [,] is the Gerstenhaber bracket, and
    l_k are the L_infinity corrections.

    The MC moduli space is the formal moduli problem:
        MC(CE^{ch,*}(L)[1]) = {alpha | MC equation} / gauge

    The tangent complex at 0 is CE^{ch,*}(L)[1]:
        T_0 MC = CE^{ch,1}(L)  (tangent = degree-1 cochains)
        Obs_0 MC = CE^{ch,2}(L) (obstruction = degree-2 cochains)

    Goldman-Millson (1988): for a dgLa, the MC moduli is a formal
    derived stack with tangent complex = shifted cochains.

    Parameters
    ----------
    lca : LieConformalAlgebra
        The Lie conformal algebra.
    linf : LInfinityData
        The L_infinity data.
    """

    def __init__(
        self,
        lca: LieConformalAlgebra,
        linf: LInfinityData,
    ):
        self.lca = lca
        self.linf = linf
        self.ce = CEChainComplex(lca)
        self.dc = DerivedCenterCE(self.ce)
        self.n = lca.dim

    @property
    def shadow_class(self) -> str:
        return self.linf.shadow_class

    def tangent_dimension(self) -> int:
        r"""Dimension of the tangent space T_0 MC = CE^{ch,1}(L).

        dim CE^1(L) = dim L = n (the number of generators).

        For Heisenberg (n=1): tangent = 1 (the current J).
        For sl_2 (n=3): tangent = 3 (e, f, h).
        For Yangian_3 (n=3): tangent = 3 (e_0, e_1, e_2).
        For Virasoro (n=1 as LCA): tangent = 1 (the generator T).
        """
        return self.dc.cochain_dimension(1)

    def obstruction_dimension(self) -> int:
        r"""Dimension of the obstruction space Obs_0 MC = CE^{ch,2}(L).

        dim CE^2(L) = binom(n, 2) = n(n-1)/2.

        For Heisenberg (n=1): obstruction = 0 (UNOBSTRUCTED).
        For sl_2 (n=3): obstruction = 3.
        For Yangian_3 (n=3): obstruction = 3.
        For Virasoro (n=1 as LCA): obstruction = 0 (BUT: L_infinity
            corrections from the full VOA produce obstructions at the
            bar complex level; the LCA-level obstruction is 0).
        """
        return self.dc.cochain_dimension(2)

    def mc_moduli_dimension(self) -> str:
        r"""Expected dimension of the MC moduli space.

        For a dgLa with tangent T and obstruction Obs:
            virtual dim = dim T - dim Obs = dim CE^1 - dim CE^2
                        = n - binom(n,2) = n - n(n-1)/2

        For n=1: virtual dim = 1 - 0 = 1 (but actual dim depends on d).
        For n=3: virtual dim = 3 - 3 = 0 (balanced tangent/obstruction).

        The ACTUAL dimension depends on whether obstructions vanish:
        - Class G: unobstructed, MC = point (abelian: all brackets zero).
        - Class L: generically unobstructed by BTT (Bogomolov-Tian-Todorov).
        - Class M: obstructed in general (l_3, l_4 provide genuine constraints).
        """
        tang = self.tangent_dimension()
        obs = self.obstruction_dimension()
        vdim = tang - obs

        if self.shadow_class == "G":
            return f"point (class G: abelian, MC = {{0}}, vdim = {vdim})"
        elif self.shadow_class == "L":
            return (
                f"smooth of dimension {tang} "
                f"(class L: BTT unobstructedness, CE^2 = {obs} "
                f"but obstructions killed by Jacobi, vdim = {vdim})"
            )
        elif self.shadow_class == "M":
            return (
                f"singular of virtual dimension {vdim} "
                f"(class M: L_infinity obstructions from shadow tower, "
                f"tangent = {tang}, obstruction = {obs})"
            )
        return f"unknown (vdim = {vdim})"

    def mc_equation_order_by_order(self, max_order: int = 4) -> Dict[int, str]:
        r"""The Maurer-Cartan equation expanded order by order.

        Order 1: d_CE(alpha) = 0  (cocycle condition)
        Order 2: d_CE(alpha) + (1/2)[alpha, alpha] = 0  (MC for dgLa)
        Order 3: + (1/6)l_3(alpha, alpha, alpha) = 0
        Order 4: + (1/24)l_4(alpha, alpha, alpha, alpha) = 0
        ...

        For class G: only order 1 matters (d = 0, so alpha = anything is MC).
        For class L: orders 1,2 suffice (strict Lie, l_k=0 for k>=3).
        For class M: ALL orders contribute (infinite shadow tower).
        """
        equations = {}
        equations[1] = "d_CE(alpha) = 0 (cocycle)"

        if self.shadow_class == "G":
            equations[2] = "0 = 0 (abelian: bracket vanishes)"
            for k in range(3, max_order + 1):
                equations[k] = "0 = 0 (class G: all higher terms vanish)"
        elif self.shadow_class == "L":
            equations[2] = (
                "d_CE(alpha) + (1/2)[alpha, alpha] = 0 "
                "(strict MC for Lie algebra)"
            )
            for k in range(3, max_order + 1):
                equations[k] = "0 = 0 (class L: l_k = 0 for k >= 3)"
        else:  # class M
            equations[2] = (
                "d_CE(alpha) + (1/2)[alpha, alpha] = 0 (leading MC)"
            )
            for k in range(3, max_order + 1):
                coeff_str = f"1/{math.factorial(k)}"
                equations[k] = (
                    f"+ ({coeff_str}) * l_{k}(alpha^{k}) "
                    f"(shadow tower correction S_{k})"
                )

        return equations

    def formal_moduli_description(self) -> Dict[str, Any]:
        r"""Description of the formal moduli problem MC(CE^{ch,*}(L)[1]).

        The formal moduli problem in the sense of Lurie (DAG-X, 2011):
        a functor from artinian cdga's to spaces, whose tangent complex
        is CE^{ch,*}(L)[1].

        For L_infinity algebras: MC(g) = {alpha in g^1 | MC eqn} / exp(g^0).

        Gauge group: exp(CE^{ch,0}(L)) = exp(k) acts trivially on MC.

        The moduli of chiral deformations of L IS the moduli of boundary
        conditions for the holomorphic CS theory on C^3.
        """
        tang = self.tangent_dimension()
        obs = self.obstruction_dimension()

        return {
            "tangent_complex": f"CE^{{ch,*}}(L)[1], dim = {self.n}",
            "tangent_dim": tang,
            "obstruction_dim": obs,
            "virtual_dim": tang - obs,
            "gauge_group_dim": self.dc.cochain_dimension(0),
            "shadow_class": self.shadow_class,
            "unobstructed": obs == 0 or self.shadow_class in ("G", "L"),
            "mc_space_type": self.mc_moduli_dimension(),
            "hcs_interpretation": (
                "Moduli of boundary conditions for holomorphic CS on C^3 "
                f"(CONJECTURAL for d=3; AP-CY6)"
            ),
        }


# =========================================================================
#  5.  Derived moduli stack
# =========================================================================

class DerivedModuliStack:
    r"""The derived moduli stack MC(CE^{ch,*}(L)) for the chiral CE cochains.

    The derived stack structure captures both:
    1. The classical moduli (MC elements modulo gauge)
    2. The derived structure (higher tangent data from the L_infinity algebra)

    For class G (Heisenberg): the derived stack is a point.
    For class L (Yangian): smooth derived scheme, dim = rank(g).
    For class M (Virasoro): singular derived stack with obstructions.

    The E_3 deformation QUANTIZES this derived stack:
        MC_classical -> MC_quantum(sigma_3)

    The quantized MC moduli is the moduli of Omega-deformed boundary conditions.

    Parameters
    ----------
    mc : ChiralMCDeformation
        The MC deformation theory.
    omega : OmegaParams
        The Omega-background parameters.
    """

    def __init__(self, mc: ChiralMCDeformation, omega: OmegaParams):
        self.mc = mc
        self.omega = omega

    @property
    def shadow_class(self) -> str:
        return self.mc.shadow_class

    def classical_moduli_description(self) -> str:
        """Description of the classical (undeformed) MC moduli."""
        if self.shadow_class == "G":
            return "point: abelian L has trivial MC space {0}"
        elif self.shadow_class == "L":
            t = self.mc.tangent_dimension()
            return f"smooth scheme of dimension {t} (BTT unobstructed)"
        elif self.shadow_class == "M":
            return (
                "singular stack: L_infinity obstructions from infinite shadow tower"
            )
        return "unknown"

    def quantized_moduli_description(self) -> str:
        """Description of the quantized (Omega-deformed) MC moduli."""
        sigma3 = self.omega.sigma3
        if self.shadow_class == "G":
            return (
                f"point: quantum correction vanishes (class G, "
                f"sigma_3 = {sigma3} is immaterial)"
            )
        elif self.shadow_class == "L":
            return (
                f"smooth quantum family over Spec k[[sigma_3]] "
                f"(sigma_3 = {sigma3}, rational convergence)"
            )
        elif self.shadow_class == "M":
            return (
                f"formal Gevrey-1 family over Spec k[[sigma_3]] "
                f"(sigma_3 = {sigma3}, Borel resummation needed)"
            )
        return "unknown"

    def cotangent_complex_dimension(self, degree: int) -> int:
        r"""Dimension of the cotangent complex L_{MC} in given degree.

        The cotangent complex of the derived MC stack is:
            L_{MC} = CE^{ch,*}(L)[1]
        with:
            L^0 = CE^{ch,1}(L)  (tangent, dim = n)
            L^1 = CE^{ch,2}(L)  (obstruction, dim = binom(n,2))
            L^{-1} = CE^{ch,0}(L) = k  (gauge, dim = 1)
        """
        # Shifted: degree p in L_{MC} = degree p+1 in CE^*
        return self.mc.dc.cochain_dimension(degree + 1)

    def euler_characteristic_stack(self) -> int:
        r"""Euler characteristic of the derived stack.

        chi(MC) = sum (-1)^k dim L^k = sum (-1)^k dim CE^{k+1}
                = -chi(CE^*) + dim CE^0
                = -0 + 1 = 1  (for any n, since chi((1+t)^n) = 0).

        Wait: chi(CE^*) = (1+(-1))^n = 0 for n >= 1. And
        chi(L_{MC}) = sum (-1)^k dim L^k_{MC}. With the shift:
            L^{-1} = CE^0 = 1
            L^0 = CE^1 = n
            L^1 = CE^2 = binom(n,2)
            ...
        chi(L) = 1 - n + binom(n,2) - ... = (1-1)^n = 0 (alternating sum).

        Actually chi = sum_{k>=0} (-1)^k dim CE^k = (1+(-1))^n = 0 for n >= 1.
        """
        n = self.mc.n
        if n == 0:
            return 1
        return 0  # chi((1+t)^n) at t=-1 = 0 for n >= 1

    def full_description(self) -> Dict[str, Any]:
        """Complete description of the derived moduli stack."""
        return {
            "shadow_class": self.shadow_class,
            "classical": self.classical_moduli_description(),
            "quantized": self.quantized_moduli_description(),
            "cotangent_dims": {
                k: self.cotangent_complex_dimension(k)
                for k in range(-1, self.mc.n)
            },
            "euler_char": self.euler_characteristic_stack(),
            "deformation_type": (
                "polynomial" if self.shadow_class == "G" else
                "rational" if self.shadow_class == "L" else
                "convergent" if self.shadow_class == "C" else
                "Gevrey-1 divergent"
            ),
            "omega_params": {
                "h1": self.omega.h1,
                "h2": self.omega.h2,
                "h3": self.omega.h3,
                "sigma2": self.omega.sigma2,
                "sigma3": self.omega.sigma3,
            },
        }


# =========================================================================
#  6.  Factory functions for the three examples
# =========================================================================

def heisenberg_e3_deformation(
    omega: Optional[OmegaParams] = None,
    k: Fraction = Fraction(1),
) -> Dict[str, Any]:
    r"""Complete E_3-chiral CE deformation theory for the Heisenberg (class G).

    L = Heis, {J_lambda J} = k*lambda.
    Shadow class: G (Gaussian, no higher corrections).
    Deformation type: polynomial (trivial, d_h = d_CE = 0).
    E_3 Koszul dual: quantum toroidal at degenerate parameters (CONJECTURAL).
    MC moduli: point {0} (abelian, no deformations).
    Derived moduli: point.

    Parameters
    ----------
    omega : OmegaParams, optional
        Omega-background parameters. Defaults to (1, -2, 1).
    k : Fraction
        Level of the Heisenberg.
    """
    if omega is None:
        omega = OmegaParams(h1=Fraction(1), h2=Fraction(-2))

    lca = heisenberg_lca(k=k)
    linf = heisenberg_linfinity()
    e3_def = E3ChiralCEDeformation(lca, linf, omega)
    quantum = QuantumCEDeformation(e3_def)
    koszul = E3KoszulDual(e3_def)
    mc = ChiralMCDeformation(lca, linf)
    moduli = DerivedModuliStack(mc, omega)

    return {
        "name": "Heisenberg",
        "shadow_class": "G",
        "lca": lca,
        "lca_dim": lca.dim,
        "e3_deformation": e3_def,
        "quantum_deformation": quantum,
        "koszul_dual": koszul,
        "mc_deformation": mc,
        "derived_moduli": moduli,
        # Key invariants
        "kappa_ch": k / Fraction(2),
        "deformation_type": "polynomial",
        "d_h_trivial": True,  # d_h = d_CE = 0 for abelian
        "mc_moduli_dim": "point",
        "conductor": koszul.conductor,
        "e3_bar_genus3_dim": 2 ** (lca.dim * 3),
        "tangent_dim": mc.tangent_dimension(),
        "obstruction_dim": mc.obstruction_dimension(),
    }


def yangian_e3_deformation(
    omega: Optional[OmegaParams] = None,
) -> Dict[str, Any]:
    r"""Complete E_3-chiral CE deformation theory for the Yangian (class L).

    L = Y(gl_hat_1) truncated to 3 generators.
    Shadow class: L (strict Lie, rational structure functions).
    Deformation type: rational (converges in a disk).
    E_3 Koszul dual: quantum toroidal at generic parameters (CONJECTURAL).
    MC moduli: smooth, dim = 3.
    Derived moduli: smooth derived scheme.

    Parameters
    ----------
    omega : OmegaParams, optional
        Omega-background parameters. Defaults to (1, -2, 1).
    """
    if omega is None:
        omega = OmegaParams(h1=Fraction(1), h2=Fraction(-2))

    lca = yangian_gl1_lca()
    linf = yangian_gl1_linfinity()
    e3_def = E3ChiralCEDeformation(lca, linf, omega)
    quantum = QuantumCEDeformation(e3_def)
    koszul = E3KoszulDual(e3_def)
    mc = ChiralMCDeformation(lca, linf)
    moduli = DerivedModuliStack(mc, omega)

    return {
        "name": "Yangian Y(gl_hat_1)",
        "shadow_class": "L",
        "lca": lca,
        "lca_dim": lca.dim,
        "e3_deformation": e3_def,
        "quantum_deformation": quantum,
        "koszul_dual": koszul,
        "mc_deformation": mc,
        "derived_moduli": moduli,
        # Key invariants
        "kappa_ch": Fraction(1),
        "deformation_type": "rational",
        "d_h_trivial": False,  # d_CE != 0 (nonabelian)
        "mc_moduli_dim": "smooth, dim 3",
        "conductor": koszul.conductor,
        "e3_bar_genus3_dim": 2 ** (lca.dim * 3),  # 2^9 = 512
        "tangent_dim": mc.tangent_dimension(),
        "obstruction_dim": mc.obstruction_dimension(),
    }


def virasoro_e3_deformation(
    omega: Optional[OmegaParams] = None,
    c: Fraction = Fraction(1),
) -> Dict[str, Any]:
    r"""Complete E_3-chiral CE deformation theory for the Virasoro (class M).

    L = Vir, {T_lambda T} = (d+2*lambda)*T + (c/12)*lambda^3.
    Shadow class: M (infinite shadow tower, mock modular).
    Deformation type: Gevrey-1 divergent (Borel resummable).
    E_3 Koszul dual: W-algebra quantum group (CONJECTURAL).
    MC moduli: singular (L_infinity obstructions from l_3, l_4, ...).
    Derived moduli: singular derived stack.

    Parameters
    ----------
    omega : OmegaParams, optional
        Omega-background parameters. Defaults to (1, -2, 1).
    c : Fraction
        Central charge.
    """
    if omega is None:
        omega = OmegaParams(h1=Fraction(1), h2=Fraction(-2))

    lca = virasoro_lca(c=c)
    linf = virasoro_linfinity(c=c)
    e3_def = E3ChiralCEDeformation(lca, linf, omega)
    quantum = QuantumCEDeformation(e3_def)
    koszul = E3KoszulDual(e3_def)
    mc = ChiralMCDeformation(lca, linf)
    moduli = DerivedModuliStack(mc, omega)

    kappa_ch = c / Fraction(2)

    return {
        "name": "Virasoro",
        "shadow_class": "M",
        "lca": lca,
        "lca_dim": lca.dim,
        "e3_deformation": e3_def,
        "quantum_deformation": quantum,
        "koszul_dual": koszul,
        "mc_deformation": mc,
        "derived_moduli": moduli,
        # Key invariants
        "kappa_ch": kappa_ch,
        "deformation_type": "Gevrey-1 divergent",
        "d_h_trivial": False,
        "mc_moduli_dim": "singular",
        "conductor": koszul.conductor,
        "e3_bar_genus3_dim": "6^g (E_4 page, class M, AP-CY21)",
        "tangent_dim": mc.tangent_dimension(),
        "obstruction_dim": mc.obstruction_dimension(),
        # Shadow tower data
        "shadow_tower": {
            "S_2": kappa_ch,
            "S_3": Fraction(2) * c,
            "S_4": Fraction(10) / (c * (5 * c + 22)),
        },
        "central_charge": c,
    }


# =========================================================================
#  7.  Comparative analysis across shadow classes
# =========================================================================

def e3_deformation_comparison() -> Dict[str, Any]:
    r"""Compare E_3-chiral CE deformation across all three shadow classes.

    Returns a comparative table showing how each shadow class determines:
    1. Deformation type (polynomial/rational/Gevrey-1)
    2. MC moduli (point/smooth/singular)
    3. E_3 bar cohomology ((1+t)^{3g} vs 6^g)
    4. Koszul conductor
    5. Quantum group identification (CONJECTURAL)

    Cross-references:
    - deformed_chiral_ce_engine.py: d_h for V_k(gl_1) (the Heisenberg case)
    - e3_two_parameter_rmatrix.py: the two-parameter R-matrix from E_3
    - zamolodchikov_tetrahedron_engine.py: ZTE obstruction at E_3
    - e3_bar_higher_genus_class_m.py: class M E_3 bar cohomology
    """
    omega = OmegaParams(h1=Fraction(1), h2=Fraction(-2))

    heis = heisenberg_e3_deformation(omega=omega)
    yang = yangian_e3_deformation(omega=omega)
    vir = virasoro_e3_deformation(omega=omega)

    return {
        "comparison": {
            "G (Heisenberg)": {
                "deformation_type": heis["deformation_type"],
                "mc_moduli": heis["mc_moduli_dim"],
                "e3_bar_g3": heis["e3_bar_genus3_dim"],
                "conductor": heis["conductor"],
                "tangent": heis["tangent_dim"],
                "obstruction": heis["obstruction_dim"],
                "kappa_ch": heis["kappa_ch"],
            },
            "L (Yangian)": {
                "deformation_type": yang["deformation_type"],
                "mc_moduli": yang["mc_moduli_dim"],
                "e3_bar_g3": yang["e3_bar_genus3_dim"],
                "conductor": yang["conductor"],
                "tangent": yang["tangent_dim"],
                "obstruction": yang["obstruction_dim"],
                "kappa_ch": yang["kappa_ch"],
            },
            "M (Virasoro)": {
                "deformation_type": vir["deformation_type"],
                "mc_moduli": vir["mc_moduli_dim"],
                "e3_bar_g3": vir["e3_bar_genus3_dim"],
                "conductor": vir["conductor"],
                "tangent": vir["tangent_dim"],
                "obstruction": vir["obstruction_dim"],
                "kappa_ch": vir["kappa_ch"],
            },
        },
        "omega": {"h1": omega.h1, "h2": omega.h2, "h3": omega.h3},
        "sigma2": omega.sigma2,
        "sigma3": omega.sigma3,
    }


# =========================================================================
#  8.  Main computation suite
# =========================================================================

def compute_e3_chiral_ce_deformation() -> Dict[str, Any]:
    r"""Run the full E_3-chiral CE deformation computation suite.

    Returns all results for the three examples and the comparison table.
    """
    results = {}

    omega = OmegaParams(h1=Fraction(1), h2=Fraction(-2))

    # --- 1. Heisenberg (class G) ---
    heis = heisenberg_e3_deformation(omega=omega)
    results["heisenberg"] = heis

    # --- 2. Yangian (class L) ---
    yang = yangian_e3_deformation(omega=omega)
    results["yangian"] = yang

    # --- 3. Virasoro (class M) ---
    vir = virasoro_e3_deformation(omega=omega)
    results["virasoro"] = vir

    # --- 4. Comparison table ---
    results["comparison"] = e3_deformation_comparison()

    # --- 5. E_3 structure verification ---
    # d_h^2 = 0 for all three examples
    results["d_h_squared_zero"] = {
        "heisenberg": heis["e3_deformation"].d_h_squared_zero(),
        "yangian": yang["e3_deformation"].d_h_squared_zero(),
        "virasoro": vir["e3_deformation"].d_h_squared_zero(),
    }

    # --- 6. Parameter inversion (Koszul duality check) ---
    results["koszul_param_inversion"] = {
        "heisenberg": heis["koszul_dual"].parameter_inversion_check(),
        "yangian": yang["koszul_dual"].parameter_inversion_check(),
        "virasoro": vir["koszul_dual"].parameter_inversion_check(),
    }

    # --- 7. MC equation structure ---
    results["mc_equations"] = {
        "heisenberg": heis["mc_deformation"].mc_equation_order_by_order(),
        "yangian": yang["mc_deformation"].mc_equation_order_by_order(),
        "virasoro": vir["mc_deformation"].mc_equation_order_by_order(),
    }

    # --- 8. Derived moduli ---
    results["derived_moduli"] = {
        "heisenberg": heis["derived_moduli"].full_description(),
        "yangian": yang["derived_moduli"].full_description(),
        "virasoro": vir["derived_moduli"].full_description(),
    }

    return results
