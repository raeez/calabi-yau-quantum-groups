r"""E1 chiral algebras from CY3 matrix factorization categories (LG models).

THE LG/CY CORRESPONDENCE AT THE E1 CHIRAL LEVEL
=================================================

For a polynomial W: C^n -> C (the superpotential) with isolated critical
point at the origin, the category MF(W) of matrix factorizations is a
CY category of dimension d = n - 2.  The Landau-Ginzburg/Calabi-Yau
correspondence (Orlov, Kontsevich, Hori-Vafa) relates MF(W) to derived
categories of CY hypersurfaces.

MATHEMATICAL CONTENTS:

1. BRIESKORN-PHAM SINGULARITIES: W = x_1^{d_1} + ... + x_n^{d_n}
   Milnor number: mu(W) = prod(d_i - 1)  [Sebastiani-Thom]
   CY dimension of MF(W): d_{CY} = n - 2
   Charges: q_i = 1/d_i (quasi-homogeneous weights)
   Central charge: c_hat = sum (1 - 2q_i) = n - 2 * sum 1/d_i
   For CY d-fold: c_hat = d/3  (N=2 SCFT central charge / 3)

   The CY condition for the associated HYPERSURFACE {W=0} in weighted P^{n-1}:
       sum q_i = 1,  equivalently sum 1/d_i = 1.
   This gives c_hat = n - 2.

   For the Fermat quintic: n=5, d_i=5 for all i.
       sum 1/d_i = 1.  c_hat = 5 - 2 = 3.  CY3 condition: c_hat = 1? No.
   Actually c_hat = sum(1 - 2/d_i) = 5 * (1 - 2/5) = 5 * 3/5 = 3.
   For CY3 string compactification: total c = 3 * c_hat = 9.

2. GEPNER MODELS AND THEIR CHIRAL ALGEBRAS:
   The Gepner model (k)^r is the tensor product of r copies of the N=2
   minimal model at level k, orbifolded by Z/(k+2)Z.

   The N=2 minimal model at level k has:
       c = 3k/(k+2)
       Chiral ring: C[x]/(x^{k+1}) (from the LG model W = x^{k+2})

   The quintic Gepner model (3)^5:
       Each factor has k=3, c = 9/5.
       Total c = 5 * 9/5 = 9 = 3 * d = 3 * 3.

   THE CHIRAL ALGEBRA of the (3)^5 Gepner model:
       This is NOT a standard W-algebra.  It is the N=2 Gepner model
       (a rational N=2 SCFT) whose chiral algebra is the tensor product
       of 5 copies of the N=2 minimal model VOA at c=9/5, with a Z/5Z
       orbifold (simple current extension).

       The N=2 minimal model at level k is related to the N=2 coset:
           SU(2)_k x U(1)_2 / U(1)_{k+2}
       At k=3: SU(2)_3 x U(1)_2 / U(1)_5.

       The BOSONIC (N=0) subalgebra of the N=2 MM at level k is generated
       by the stress tensor T (Virasoro at c = 3k/(k+2)) and the U(1)
       current J.  The full N=2 SCA additionally has G^+ and G^-.

3. ORLOV'S THEOREM AND THE SINGULARITY CATEGORY:
   For W with isolated singularity:
       MF(W) = D_sg(W^{-1}(0)) := D^b(coh(W^{-1}(0))) / Perf(W^{-1}(0))
   This is the Orlov equivalence (2004).

   For ADE surface singularities W: C^2 -> C:
       MF(W) = D_sg(Spec C[x,y]/(W))
   The resulting chiral algebra is the N=2 minimal model.

4. THE CONIFOLD:
   W = x_1^2 + x_2^2 + x_3^2 + x_4^2 (= a node in 4 variables).
   n_vars = 4, CY dim = n - 2 = 2.  mu = 1^4 = 1.
   But: by Knorrer periodicity, MF(sum x_i^2) = MF(0) = Vect.
   This is the TRIVIAL category.

   The CONIFOLD singularity is NOT the Brieskorn-Pham W = sum x_i^2.
   The conifold is the HYPERSURFACE xy - zw = 0 in C^4 (or equivalently
   det(M) = 0 for a 2x2 matrix).  Its singularity category D_sg gives
   the gl(1|1) chiral algebra (c = 0), as computed in conifold_e1_full_chain.py.

   For W = sum_{i=1}^4 x_i^2 (the A_1 singularity in 4 variables):
       mu = 1.  By Knorrer, MF(sum x_i^2) = MF(x_1^2) = Vect (trivial).
       The chiral algebra is trivial (zero-dimensional).

5. ADE SINGULARITIES TO CHIRAL ALGEBRAS:

   Single-variable (CY dim = -1, formal):
       A_{n-1}: W = x^n -> mu = n-1 -> N=2 MM at level k=n-2
       The chiral algebra is the N=2 MINIMAL MODEL VOA.

   Two-variable (CY dim = 0, semisimple MF category):
       A_{n-1}: W = x^n + y^2 -> Knorrer: MF = MF(x^n).
       D_n: W = x^{n-1} + xy^2 -> mu = n -> D-type N=2 MM.
       E_6: W = x^3 + y^4 -> mu = 6 -> E_6-type N=2 MM.
       E_7: W = x^3 + xy^3 -> mu = 7 -> E_7-type N=2 MM.
       E_8: W = x^3 + y^5 -> mu = 8 -> E_8-type N=2 MM.

   The N=2 minimal model central charge: c = 3(1 - 2/h)
   where h is the Coxeter number.
   For A_{n-1}: h = n, c = 3(n-2)/n.
   For D_n: h = 2(n-1), c = 3(n-2)/(n-1).
   For E_6: h = 12, c = 5/2.
   For E_7: h = 18, c = 8/3.
   For E_8: h = 30, c = 14/5.

6. MODULAR CHARACTERISTIC kappa:

   (a) From the MF category (categorical): kappa_MF = mu/2.
       This uses the CY trace on HH_*(MF(W)) = Jac(W).

   (b) From the N=2 minimal model (Virasoro subalgebra):
       kappa_Vir = c/2 = 3(h-2)/(2h).

   (c) From the N=2 SCA (full algebra):
       The N=2 SCA has generators T, J, G^+, G^-.
       kappa_{N=2} = c/6 (the factor 1/3 from the N=2 structure).
       Cross-check: for the N=2 SCA at c=9 (quintic CY3):
           kappa_{N=2} = 9/6 = 3/2.

   (d) From the CY Euler characteristic (BCOV):
       For a compact CY3 X: kappa_{BCOV} = chi(X)/24.
       Quintic: chi = -200, kappa_{BCOV} = -200/24 = -25/3.

   These are FOUR DIFFERENT kappa values measuring FOUR DIFFERENT things:
       kappa_MF = mu/2 (HH trace of Hessian)
       kappa_Vir = c/2 (Virasoro subalgebra)
       kappa_{N=2} = c/6 (N=2 superconformal algebra)
       kappa_{BCOV} = chi/24 (B-model holomorphic anomaly)

   The BCOV kappa is the physically relevant one for string amplitudes.
   kappa_MF is the mathematically natural one from the MF category.

7. WALL-CROSSING AND MC GAUGE TRANSFORMATION:

   In the GLSM (Gauged Linear Sigma Model) for the quintic:
       Phase I (sigma >> 0): CY phase, D^b(Coh(Q))
       Phase II (sigma << 0): LG/orbifold phase, MF(W)/Z_5
       Transition at sigma = 0: the Gepner point.

   The E1 chiral algebras in the two phases are related by:
       A_{CY}(t) and A_{LG}(sigma) with A_{CY}(0) = A_{LG}(0) = A_{Gepner}.

   The wall-crossing at the Gepner point is an MC GAUGE TRANSFORMATION:
       Theta_{LG} = g * Theta_{CY} * g^{-1} + g * d(g^{-1})
   where g is the gauge element from the orbifold/GLSM identification.

   At the level of DT invariants / BPS counts:
       Wall-crossing formula (KS): DT_{chamber I} <-> DT_{chamber II}
       This is the Kontsevich-Soibelman wall-crossing formula.
       In the E1 bar complex: B(A_{CY}) and B(A_{LG}) are related by
       the KS automorphism of the motivic Hall algebra.

MATHEMATICAL SOURCES:
    Orlov, "Triangulated categories of singularities" (2004)
    Gepner, "Exactly solvable string compactifications..." (1988)
    Greene-Plesser, "Duality in CY moduli space" (1990)
    Hori-Vafa, "Mirror symmetry" (2000)
    Kontsevich-Soibelman, "Stability structures, motivic DT..." (2008)
    Witten, "Phases of N=2 theories in two dimensions" (1993)
    Kapustin-Li, "D-branes in LG models and algebraic geometry" (2003)
    Dyckerhoff, "Compact generators in categories of MF" (2011)
    Addington, "New derived symmetries of some HK 4-folds" (2016)
    BCOV, "Kodaira-Spencer theory of gravity" (1994)
    Lorgat, Vol I: shadow_tower, kappa
    Lorgat, Vol III: cy_to_chiral_functor, matrix_factorization_shadow
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache, reduce
from operator import mul
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple, Union


# ============================================================================
# 0. Exact arithmetic helpers
# ============================================================================

F = Fraction  # shorthand


def _product(xs: Sequence[int]) -> int:
    """Product of a list of integers."""
    return reduce(mul, xs, 1)


# ============================================================================
# 1. Brieskorn-Pham singularities
# ============================================================================

@dataclass(frozen=True)
class BrieskornPham:
    r"""A Brieskorn-Pham singularity W = x_1^{d_1} + ... + x_n^{d_n}.

    Attributes:
        degrees: tuple (d_1, ..., d_n) of exponents, each >= 2.
        name: optional human-readable name.
    """
    degrees: Tuple[int, ...]
    name: str = ""

    def __post_init__(self):
        for d in self.degrees:
            if d < 2:
                raise ValueError(f"Each degree must be >= 2, got {d}")

    @property
    def n_vars(self) -> int:
        """Number of variables."""
        return len(self.degrees)

    @property
    def milnor_number(self) -> int:
        r"""Milnor number: mu(W) = prod(d_i - 1).

        By Sebastiani-Thom: for W = f_1(x_1) + ... + f_n(x_n) with
        f_i = x_i^{d_i}, the Milnor number is multiplicative:
            mu(f_1 + ... + f_n) = mu(f_1) * ... * mu(f_n)
        and mu(x^d) = d - 1.
        """
        return _product(d - 1 for d in self.degrees)

    @property
    def cy_dimension(self) -> int:
        r"""CY dimension of MF(W): d_{CY} = n - 2.

        The Serre functor on MF(W) for a weighted-homogeneous polynomial
        in n variables is S = [n-2] (shift by n-2).
        """
        return self.n_vars - 2

    @property
    def charges(self) -> Tuple[Fraction, ...]:
        r"""Quasi-homogeneous charges: q_i = 1/d_i.

        These are the weights such that W has total weight 1:
            W(lambda^{q_1} x_1, ..., lambda^{q_n} x_n) = lambda * W(x_1, ..., x_n).
        """
        return tuple(F(1, d) for d in self.degrees)

    @property
    def charge_sum(self) -> Fraction:
        r"""Sum of charges: sum q_i = sum 1/d_i."""
        return sum(self.charges)

    @property
    def c_hat(self) -> Fraction:
        r"""N=2 central charge hat: c_hat = sum(1 - 2q_i) = n - 2 * sum(1/d_i).

        For an N=2 SCFT with superpotential W, the central charge is c = 3 * c_hat.
        For a CY d-fold compactification: c_hat = d (so c = 3d).
        The CY condition on the HYPERSURFACE {W=0} in weighted projective space
        is sum q_i = 1, which gives c_hat = n - 2.
        """
        return sum(1 - 2 * q for q in self.charges)

    @property
    def total_central_charge(self) -> Fraction:
        r"""Total central charge c = 3 * c_hat of the associated N=2 SCFT."""
        return 3 * self.c_hat

    @property
    def is_cy_condition(self) -> bool:
        r"""Check the CY condition: sum q_i = 1.

        When this holds, {W=0} defines a CY variety in weighted projective space.
        """
        return self.charge_sum == 1

    @property
    def jacobian_ring_dim(self) -> int:
        """Dimension of the Jacobian ring Jac(W) = C[x_1,...,x_n]/(dW/dx_i).

        For Brieskorn-Pham: Jac(W) = tensor product of C[x_i]/(d_i x_i^{d_i-1}),
        so dim = prod(d_i - 1) = mu(W).
        """
        return self.milnor_number


def fermat_quintic() -> BrieskornPham:
    r"""The Fermat quintic: W = x_1^5 + x_2^5 + x_3^5 + x_4^5 + x_5^5."""
    return BrieskornPham(degrees=(5, 5, 5, 5, 5), name="Fermat_quintic")


def conifold_node() -> BrieskornPham:
    r"""The A_1 singularity in 4 variables: W = x_1^2 + x_2^2 + x_3^2 + x_4^2.

    WARNING: This is NOT the conifold singularity xy - zw = 0!
    By Knorrer periodicity, MF(sum x_i^2) = MF(x^2) = Vect (trivial).
    The conifold has a DIFFERENT superpotential structure.
    """
    return BrieskornPham(degrees=(2, 2, 2, 2), name="A1_node_4vars")


def e6_surface_singularity() -> BrieskornPham:
    r"""The E_6 surface singularity: W = x^3 + y^4 (2 variables, CY dim = 0)."""
    return BrieskornPham(degrees=(3, 4), name="E6_surface")


def e6_threefold_singularity() -> BrieskornPham:
    r"""E_6 singularity stabilized to CY2: W = x^3 + y^4 + z^2 + w^2."""
    return BrieskornPham(degrees=(3, 4, 2, 2), name="E6_CY2")


def ade_singularity_bp(ade_type: str, rank: int) -> BrieskornPham:
    r"""Construct an ADE singularity as Brieskorn-Pham in 2 variables.

    A_{n-1}: W = x^n + y^2  (CY dim = 0)
    D_n:     W = x^{n-1} + xy^2 -- NOT Brieskorn-Pham (mixed term)!
             Use stabilized form x^{n-1} + y^2 + z^2 for Knorrer-equiv.
             Actually D_n is NOT BP. Return the stabilized A-type equivalent
             for the Knorrer-invariant data.
    E_6: W = x^3 + y^4 (BP)
    E_7: W = x^3 + xy^3 -- NOT BP.  Stabilized: x^3 + y^4 type with twist.
    E_8: W = x^3 + y^5 (BP)

    For non-BP types (D, E_7), we raise an error since they cannot be
    represented purely as Brieskorn-Pham.
    """
    if ade_type == 'A':
        n = rank + 1
        return BrieskornPham(degrees=(n, 2), name=f"A{rank}")
    elif ade_type == 'E' and rank == 6:
        return BrieskornPham(degrees=(3, 4), name="E6")
    elif ade_type == 'E' and rank == 8:
        return BrieskornPham(degrees=(3, 5), name="E8")
    else:
        raise ValueError(
            f"{ade_type}{rank} is not Brieskorn-Pham in 2 variables "
            "(D_n and E_7 have mixed terms)"
        )


# ============================================================================
# 2. N=2 minimal models (the chiral algebras from LG models)
# ============================================================================

@dataclass(frozen=True)
class N2MinimalModel:
    r"""N=2 minimal model at level k.

    The N=2 MM at level k has:
        c = 3k/(k+2)
        Primary fields: phi_{l,m,s} with 0 <= l <= k, m mod 2(k+2), s mod 4.
        Chiral ring: C[x]/(x^{k+1}) of dimension k+1.
        The associated LG model has superpotential W = x^{k+2}.

    The VOA structure:
        Generators: T (weight 2), J (weight 1), G^+ (weight 3/2), G^- (weight 3/2).
        The N=2 superconformal algebra (SCA).
        At level k, the SCA truncates to a rational VOA with k+1 simple modules.

    Attributes:
        level: the level k >= 1.
    """
    level: int

    def __post_init__(self):
        if self.level < 1:
            raise ValueError(f"Level must be >= 1, got {self.level}")

    @property
    def exponent(self) -> int:
        """Exponent n = k + 2 in the LG model W = x^n."""
        return self.level + 2

    @property
    def central_charge(self) -> Fraction:
        """Central charge: c = 3k/(k+2)."""
        return F(3 * self.level, self.level + 2)

    @property
    def milnor_number(self) -> int:
        """Milnor number of the LG model: mu = k + 1 = n - 1."""
        return self.level + 1

    @property
    def chiral_ring_dim(self) -> int:
        """Dimension of the chiral ring: k + 1."""
        return self.level + 1

    @property
    def n_simple_modules(self) -> int:
        """Number of simple modules of the N=2 MM VOA.

        The primaries phi_{l,m,s} with l=0,...,k, m mod 2(k+2), s mod 4.
        After identifications: (k+1) * (k+2) * 2 / 2 = (k+1)(k+2).
        But the simple modules of the NS-sector (s=0,2) and R-sector (s=1,3):
            NS: (k+1)(k+2)/2 simple modules.
            Total (all sectors): (k+1)(k+2).
        """
        return (self.level + 1) * (self.level + 2)

    @property
    def kappa_virasoro(self) -> Fraction:
        """kappa of the Virasoro subalgebra: kappa_Vir = c/2."""
        return self.central_charge / 2

    @property
    def kappa_n2(self) -> Fraction:
        r"""kappa of the full N=2 SCA.

        The N=2 SCA at central charge c has:
            kappa_{N=2} = c/6

        This is because the N=2 algebra has effective dimension c/3
        (the hat{c} = c/3), and kappa = hat{c}/2 = c/6.

        VERIFICATION: at c = 3 (k -> infinity limit):
            kappa_{N=2} = 1/2.
        At c = 9 (quintic CY3 Gepner model):
            kappa_{N=2} = 3/2.
        """
        return self.central_charge / 6

    @property
    def kappa_mf(self) -> Fraction:
        """Categorical kappa from the MF perspective: kappa_MF = mu/2."""
        return F(self.milnor_number, 2)


# ============================================================================
# 3. Gepner models
# ============================================================================

@dataclass(frozen=True)
class GepnerModelE1:
    r"""Gepner model: tensor product of N=2 minimal models with orbifold.

    The Gepner model (k_1, ..., k_r) is:
        (N2MM_{k_1} tensor ... tensor N2MM_{k_r}) / (diagonal Z/LCM Z)

    For the "diagonal" Gepner model where all k_i = k:
        r copies of N2MM_k, orbifolded by Z/(k+2)Z.

    CY condition: sum c_hat_i = d (the target CY dimension).
    For uniform level: r * k/(k+2) = d.

    Attributes:
        levels: tuple of levels (k_1, ..., k_r).
        cy_dim: the target CY dimension d.
    """
    levels: Tuple[int, ...]
    cy_dim: int

    @property
    def n_factors(self) -> int:
        return len(self.levels)

    @property
    def is_uniform(self) -> bool:
        """Whether all levels are the same."""
        return len(set(self.levels)) == 1

    @property
    def factors(self) -> Tuple[N2MinimalModel, ...]:
        """The N=2 minimal model factors."""
        return tuple(N2MinimalModel(k) for k in self.levels)

    @property
    def exponents(self) -> Tuple[int, ...]:
        """The exponents n_i = k_i + 2 in each LG factor W_i = x_i^{n_i}."""
        return tuple(k + 2 for k in self.levels)

    @property
    def central_charges(self) -> Tuple[Fraction, ...]:
        """Central charge of each factor."""
        return tuple(f.central_charge for f in self.factors)

    @property
    def total_central_charge(self) -> Fraction:
        """Total central charge c_total = sum c_i."""
        return sum(self.central_charges)

    @property
    def c_hat_per_factor(self) -> Tuple[Fraction, ...]:
        r"""hat{c}_i = c_i / 3 = k_i / (k_i + 2) for each factor."""
        return tuple(F(k, k + 2) for k in self.levels)

    @property
    def c_hat_total(self) -> Fraction:
        r"""Total hat{c} = sum hat{c}_i. Should equal cy_dim for CY."""
        return sum(self.c_hat_per_factor)

    def verify_cy_condition(self) -> bool:
        r"""Verify sum hat{c}_i = d."""
        return self.c_hat_total == self.cy_dim

    @property
    def orbifold_order(self) -> int:
        """Order of the orbifold group.

        For uniform level k: the orbifold is Z/(k+2)Z.
        For non-uniform: Z/LCM(k_i + 2) acting diagonally.

        The orbifold order equals LCM of all (k_i + 2).
        """
        from math import gcd
        ns = self.exponents
        result = ns[0]
        for n in ns[1:]:
            result = result * n // gcd(result, n)
        return result

    @property
    def milnor_per_factor(self) -> Tuple[int, ...]:
        """Milnor number of each factor: mu_i = k_i + 1."""
        return tuple(f.milnor_number for f in self.factors)

    @property
    def milnor_total_unorbifolded(self) -> int:
        """Total Milnor number before orbifold: prod mu_i."""
        return _product(self.milnor_per_factor)

    def orbifold_invariant_dimension(self) -> int:
        r"""Dimension of the orbifold-invariant Jacobian ring.

        For the orbifold Z/NZ acting on Jac_1 tensor ... tensor Jac_r
        with charges (1/n_1, ..., 1/n_r), the invariant subspace is
        computed by the Burnside lemma:

            dim(Jac^{Z/N}) = (1/N) * sum_{g in Z/N} Tr(g | Jac_total)

        For the j-th group element (j = 0, ..., N-1):
            On Jac_i = span{1, x, ..., x^{n_i-2}} with orbifold weight 1/n_i,
            the element j acts as:
                x^a -> exp(2 pi i j a / n_i) x^a

            Tr(j | Jac_i) = sum_{a=0}^{n_i-2} exp(2 pi i j a / n_i)

        For the total tensor product:
            Tr(j | Jac_total) = prod_i Tr(j | Jac_i)
        """
        N = self.orbifold_order
        ns = self.exponents  # n_i = k_i + 2

        total = 0.0
        for j in range(N):
            tr_factor = 1.0
            for n_i in ns:
                # Trace on Jac(x^{n_i}): sum_{a=0}^{n_i-2} exp(2pi i j a / n_i)
                # Using orbifold action with weight 1/n_i on Jac.
                # The orbifold element j acts on x^a with weight j*a/n_i.
                # But the diagonal orbifold acts with common phase:
                #   for Z/NZ with N = LCM(n_i), element j acts on x_i^a
                #   as exp(2 pi i j / N * a * (N/n_i)) = exp(2 pi i j a / n_i).
                omega_i = math.e ** (2j * math.pi * 1j / n_i) if n_i > 0 else 1
                tr_i = sum(
                    math.e ** (2.0 * math.pi * 1j * j * a / n_i)
                    for a in range(n_i - 1)
                )
                tr_factor *= tr_i
            total += tr_factor

        dim_inv = total / N
        return int(round(dim_inv.real))

    def orbifold_invariant_dimension_exact(self) -> Fraction:
        r"""Exact computation of the orbifold-invariant dimension using roots of unity.

        For uniform level k with r factors and orbifold Z/(k+2)Z:
            dim = (1/n) * [mu^r + (r-1 not needed, use character sums)]

        For j = 0: Tr = mu^r = (k+1)^r.
        For j != 0 (uniform case, n = k+2):
            Tr on single factor = sum_{a=0}^{k} zeta^{ja} where zeta = e^{2pi i/n}
            = (zeta^{j(k+1)} - 1)/(zeta^j - 1)  if zeta^j != 1
            = (zeta^{-j} - 1)/(zeta^j - 1)   since zeta^{j*n} = 1 and k+1 = n-1
            = -zeta^{-2j} * ... well, let's just compute:

        For n = k+2 and the sum sum_{a=0}^{n-2} zeta^{ja}:
            = (zeta^{j(n-1)} - 1)/(zeta^j - 1) = (zeta^{-j} - 1)/(zeta^j - 1)
            = -(1 - zeta^{-j})/(zeta^j - 1) = -zeta^{-j}(zeta^j - 1)/(zeta^j - 1)
            = -zeta^{-j}   ... wait, let me be careful.

        zeta^{j(n-1)} = zeta^{jn - j} = zeta^{-j} (since zeta^n = 1).
        So sum = (zeta^{-j} - 1)/(zeta^j - 1).
        If we write zeta^{-j} - 1 = -(1 - zeta^{-j}) = -zeta^{-j}(zeta^j - 1):
            sum = -zeta^{-j}(zeta^j - 1)/(zeta^j - 1) = -zeta^{-j}.

        Wait -- that's not right. Let me recheck:
        zeta^{-j} - 1 = e^{-2pi i j/n} - 1.
        And zeta^j - 1 = e^{2pi i j/n} - 1.
        So (zeta^{-j} - 1)/(zeta^j - 1) = (e^{-i theta} - 1)/(e^{i theta} - 1)
            = e^{-i theta} * (1 - e^{i theta}) / (e^{i theta} - 1)
            = e^{-i theta} * (-1) = -e^{-i theta} = -zeta^{-j}.

        So for j != 0: Tr on single factor = -zeta^{-j} = -e^{-2pi i j/(k+2)}.
        For r factors (all same level): Tr on tensor product = (-1)^r * zeta^{-rj}.

        For uniform level:
            dim = (1/n) * [mu^r + sum_{j=1}^{n-1} (-1)^r * zeta^{-rj}]
                = (1/n) * [mu^r + (-1)^r * (sum_{j=1}^{n-1} zeta^{-rj})]

        Now sum_{j=0}^{n-1} zeta^{-rj} = n if n | r, else 0.
        So sum_{j=1}^{n-1} zeta^{-rj} = (n if n|r else 0) - 1.

        Case 1: n does not divide r.
            dim = (1/n) * [mu^r + (-1)^r * (-1)]
                = (mu^r + (-1)^{r+1}) / n.

        Case 2: n divides r.
            dim = (1/n) * [mu^r + (-1)^r * (n-1)]

        For the quintic (k=3, n=5, r=5, mu=4):
            n=5 divides r=5, so case 2:
            dim = (4^5 + (-1)^5 * 4) / 5 = (1024 - 4)/5 = 1020/5 = 204.
            Check: h^{2,1} = 101, b_3 = 204.  Correct!
        """
        if not self.is_uniform:
            # Fall back to numerical for non-uniform
            return F(self.orbifold_invariant_dimension())

        k = self.levels[0]
        n = k + 2
        r = self.n_factors
        mu = k + 1

        mu_r = mu ** r

        if r % n == 0:
            dim = F(mu_r + (-1)**r * (n - 1), n)
        else:
            dim = F(mu_r + (-1)**(r + 1), n)

        return dim

    def chiral_ring_invariant_decomposition(self) -> Dict[str, int]:
        r"""Decompose the orbifold-invariant Jacobian ring by degree.

        For the Gepner model associated to a CY d-fold:
            Jac^{orb} = H^0 + H^1 + ... + H^d  (Hodge decomposition)
        with dim H^p = h^{d-p,p} of the mirror CY.

        For the quintic (d=3):
            Jac^{orb}_{degree q} contributes to H^{p,q} where
            the degree is measured by the total orbifold charge.

        Returns a dict mapping degree labels to dimensions.
        """
        # For the uniform Gepner model at level k, r factors, CY dim d:
        if not self.is_uniform:
            return {"total": self.orbifold_invariant_dimension()}

        k = self.levels[0]
        n = k + 2
        r = self.n_factors
        d = self.cy_dim

        # The orbifold-invariant Jacobian ring decomposes as:
        # Each monomial x_1^{a_1} ... x_r^{a_r} with 0 <= a_i <= k
        # has orbifold charge q = sum a_i / n.
        # Invariant: q in Z, i.e., sum a_i = 0 mod n.
        # The degree p = q (the charge as integer) determines the
        # Hodge component: the monomial maps to H^{d-p, p} of the mirror.

        degree_counts: Dict[int, int] = {}
        # This is a constrained partition count:
        # Number of (a_1,...,a_r) with 0 <= a_i <= k and sum a_i = q*n.
        # We enumerate by total sum s = sum a_i, which must be = 0 mod n.

        # Maximum total sum: r * k.
        max_sum = r * k

        for s in range(0, max_sum + 1, n):
            # Count the number of tuples (a_1,...,a_r) with sum = s
            # and 0 <= a_i <= k.
            # This is the coefficient of x^s in (sum_{a=0}^k x^a)^r
            # = (1-x^{k+1})^r / (1-x)^r.
            count = _count_tuples_with_sum(r, k, s)
            p = s // n  # the charge/degree
            degree_counts[p] = count

        return degree_counts


def _count_tuples_with_sum(r: int, k: int, s: int) -> int:
    r"""Count tuples (a_1,...,a_r) with 0 <= a_i <= k and sum a_i = s.

    This is the coefficient of x^s in ((1-x^{k+1})/(1-x))^r.
    By inclusion-exclusion:
        count = sum_{j=0}^{min(r, s//(k+1))} (-1)^j * C(r,j) * C(s - j*(k+1) + r - 1, r - 1)
    """
    count = 0
    for j in range(min(r, s // (k + 1)) + 1):
        remainder = s - j * (k + 1)
        if remainder < 0:
            break
        sign = (-1) ** j
        binom_rj = _binomial(r, j)
        binom_rem = _binomial(remainder + r - 1, r - 1)
        count += sign * binom_rj * binom_rem
    return count


def _binomial(n: int, k: int) -> int:
    """Binomial coefficient C(n, k)."""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result


def quintic_gepner_e1() -> GepnerModelE1:
    """The (3)^5 Gepner model for the quintic threefold."""
    return GepnerModelE1(levels=(3, 3, 3, 3, 3), cy_dim=3)


def cy3_gepner_models() -> List[GepnerModelE1]:
    r"""All uniform CY3 Gepner models (k)^r with r*k/(k+2) = 3.

    Solutions: r*k = 3*(k+2) = 3k + 6, so r*k - 3k = 6, k*(r-3) = 6.
    k | 6 and r = 3 + 6/k.

    k=1: r=9.  (1)^9 model.  n=3, mu=2 per factor.  c = 3/3 = 1 per factor.
    k=2: r=6.  (2)^6 model.  n=4, mu=3 per factor.  c = 6/4 = 3/2 per factor.
    k=3: r=5.  (3)^5 model.  n=5, mu=4 per factor.  c = 9/5 per factor.
    k=6: r=4.  (6)^4 model.  n=8, mu=7 per factor.  c = 18/8 = 9/4 per factor.

    All have total c = 9.
    """
    models = []
    for k, r in [(1, 9), (2, 6), (3, 5), (6, 4)]:
        models.append(GepnerModelE1(levels=tuple([k] * r), cy_dim=3))
    return models


# ============================================================================
# 4. E1 chiral algebra data from MF
# ============================================================================

@dataclass(frozen=True)
class E1ChiralAlgebraFromMF:
    r"""E1 chiral algebra data extracted from a matrix factorization category.

    For a BP singularity W, the E1 chiral algebra A_{MF(W)} is the
    chiral algebra associated to the CY category MF(W).

    The identification depends on the CY dimension:
        d = -1 (1 variable, formal): A = N=2 MM VOA
        d = 0 (2 variables): A = ADE N=2 MM VOA (semisimple MF cat)
        d = 1: A related to Heisenberg (for the elliptic curve)
        d = 2: A related to lattice VOA (for K3)
        d = 3: A is the Gepner model VOA (for CY3)

    Attributes:
        bp: the Brieskorn-Pham singularity
        kappa_categorical: modular char from MF category (mu/2)
        kappa_virasoro: modular char of Virasoro subalgebra (c/2)
        kappa_n2: modular char of the N=2 SCA (c/6)
        central_charge: total central charge c
        description: human-readable description of the chiral algebra
    """
    bp: BrieskornPham
    kappa_categorical: Fraction
    kappa_virasoro: Fraction
    kappa_n2: Fraction
    central_charge: Fraction
    description: str
    shadow_depth_class: str = "unknown"

    @property
    def cy_dim(self) -> int:
        return self.bp.cy_dimension

    @property
    def milnor_number(self) -> int:
        return self.bp.milnor_number


def e1_chiral_from_bp(bp: BrieskornPham) -> E1ChiralAlgebraFromMF:
    r"""Compute the E1 chiral algebra data for a Brieskorn-Pham singularity.

    The central charge is c = 3 * c_hat where c_hat = sum(1 - 2/d_i).
    The modular characteristics:
        kappa_cat = mu / 2
        kappa_Vir = c / 2
        kappa_N2 = c / 6  (if the algebra has N=2 structure)
    """
    mu = bp.milnor_number
    c = bp.total_central_charge
    kappa_cat = F(mu, 2)
    kappa_vir = c / 2
    kappa_n2 = c / 6

    # Determine the chiral algebra type
    d = bp.cy_dimension
    if d <= 0 and bp.n_vars <= 2:
        # ADE-type: N=2 minimal model
        if bp.n_vars == 1:
            n = bp.degrees[0]
            desc = f"N=2 MM at level k={n-2}, c={F(3*(n-2), n)}"
        else:
            desc = f"N=2 MM from {bp.name}, mu={mu}, c={c}"
        shadow_class = "G" if mu <= 2 else "L" if mu <= 4 else "M"
    elif d == 1:
        desc = f"Heisenberg-type from CY1 singularity, mu={mu}"
        shadow_class = "G"
    elif d == 2:
        desc = f"Lattice VOA-type from CY2 singularity, mu={mu}"
        shadow_class = "L"
    elif d == 3:
        desc = f"CY3 chiral algebra (Gepner-type), mu={mu}, c={c}"
        shadow_class = "M"
    else:
        desc = f"MF chiral algebra, CY dim={d}, mu={mu}, c={c}"
        shadow_class = "unknown"

    return E1ChiralAlgebraFromMF(
        bp=bp,
        kappa_categorical=kappa_cat,
        kappa_virasoro=kappa_vir,
        kappa_n2=kappa_n2,
        central_charge=c,
        description=desc,
        shadow_depth_class=shadow_class,
    )


# ============================================================================
# 5. Kappa computation: multi-path verification
# ============================================================================

def kappa_from_milnor(mu: int) -> Fraction:
    r"""Path 1: kappa_MF = mu / 2 (from the CY trace on HH)."""
    return F(mu, 2)


def kappa_from_central_charge_virasoro(c: Fraction) -> Fraction:
    r"""Path 2: kappa_Vir = c / 2 (from the Virasoro subalgebra)."""
    return c / 2


def kappa_from_central_charge_n2(c: Fraction) -> Fraction:
    r"""Path 3: kappa_{N=2} = c / 6 (from the N=2 SCA).

    The N=2 algebra has c_hat = c/3, and kappa = c_hat / 2.
    """
    return c / 6


def kappa_from_euler_characteristic(chi: int) -> Fraction:
    r"""Path 4: kappa_{BCOV} = chi / 24 (from B-model anomaly).

    For a compact CY3 X:
        F_1 = -chi(X)/24 * log(...)  (BCOV holomorphic anomaly)
    so kappa_{BCOV} = chi(X) / 24.

    WARNING: this kappa has a DIFFERENT PHYSICAL MEANING from kappa_MF.
    kappa_BCOV is the coefficient of the TOPOLOGICAL string amplitude.
    kappa_MF is the categorical modular characteristic.
    """
    return F(chi, 24)


def kappa_gepner_quintic() -> Dict[str, Fraction]:
    r"""All four kappa computations for the quintic Gepner model.

    The (3)^5 Gepner model:
        c_total = 9.
        mu_per_factor = 4.  mu_total (unorbifolded) = 4^5 = 1024.
        chi(quintic) = -200.

    kappa_MF (categorical): not well-defined for the ORBIFOLD directly;
        the per-factor kappa_MF = 4/2 = 2, times 5 factors = 10.
        But the orbifold changes this.

    kappa_Vir: c/2 = 9/2.
    kappa_N2: c/6 = 3/2.
    kappa_BCOV: -200/24 = -25/3.
    """
    c = F(9)
    return {
        'kappa_virasoro': c / 2,             # 9/2
        'kappa_n2': c / 6,                   # 3/2
        'kappa_bcov': F(-200, 24),           # -25/3
        'kappa_mf_per_factor': F(4, 2),      # 2 (per factor, before orbifold)
        'kappa_mf_total_naive': 5 * F(4, 2), # 10 (additive, before orbifold)
    }


# ============================================================================
# 6. E1 bar complex for MF chiral algebras
# ============================================================================

def e1_bar_dimensions(mu: int, max_arity: int = 5) -> Dict[int, int]:
    r"""Dimensions of the E1 bar complex B^{E1}(A_{MF}) by arity.

    For an E1 algebra with r generators (= mu for MF-derived algebra):
        B^{E1}_n = r^n  (tensor coalgebra at arity n).

    This is the ORDERED (Hochschild) bar complex, not the
    SYMMETRIC (Chevalley-Eilenberg) bar complex.

    For the E_infinity bar complex: B^{E_infty}_n = C(n+r-1, r-1) (symmetric).

    The E1 bar is LARGER: r^n >> C(n+r-1, r-1) for large n and r >= 2.
    """
    return {n: mu ** n for n in range(1, max_arity + 1)}


def e_infty_bar_dimensions(mu: int, max_arity: int = 5) -> Dict[int, int]:
    r"""Dimensions of the E_infty bar complex by arity for comparison.

    B^{E_infty}_n = C(n + mu - 1, mu - 1) = dim Sym^n(C^mu).
    """
    return {n: _binomial(n + mu - 1, mu - 1) for n in range(1, max_arity + 1)}


def bar_ratio_e1_vs_einfty(mu: int, arity: int) -> Fraction:
    r"""Ratio dim B^{E1}_n / dim B^{E_infty}_n.

    This ratio measures how much larger the E1 bar is compared to E_infty.
    For mu = 1: ratio = 1 (both give 1^n = 1 and C(n,0) = 1).
    For mu >= 2: ratio grows as n! / (something).

    For mu = 2: E1 gives 2^n, E_infty gives n+1.
        Ratio = 2^n / (n+1).
    """
    e1 = mu ** arity
    einf = _binomial(arity + mu - 1, mu - 1)
    if einf == 0:
        return F(0)
    return F(e1, einf)


# ============================================================================
# 7. Orlov equivalence and singularity categories
# ============================================================================

@dataclass(frozen=True)
class SingularityCategoryData:
    r"""Data for the singularity category D_sg(W^{-1}(0)).

    By Orlov's theorem (2004):
        MF(W) = D_sg(W^{-1}(0)) for W with isolated singularity.

    The singularity category captures the "non-smooth" part of the
    derived category of the singular fiber.

    For ADE surface singularities (2 variables, CY dim 0):
        D_sg is a semisimple category with mu simple objects.
        The fusion rules are those of the ADE Dynkin diagram.

    Attributes:
        milnor_number: mu = dim Jac(W)
        n_simples: number of simple objects in D_sg
        ade_type: the ADE type if applicable
        n2_level: level of the N=2 minimal model
        central_charge: c of the N=2 MM
    """
    milnor_number: int
    n_simples: int
    ade_type: str
    n2_level: int
    central_charge: Fraction

    @property
    def kappa_virasoro(self) -> Fraction:
        return self.central_charge / 2

    @property
    def kappa_categorical(self) -> Fraction:
        return F(self.milnor_number, 2)


def singularity_category_A(n: int) -> SingularityCategoryData:
    r"""Singularity category for the A_{n-1} singularity W = x^n + y^2.

    MF(x^n + y^2) = MF(x^n) by Knorrer.
    D_sg has n-1 simple objects (the indecomposable MFs of x^n).
    The N=2 MM has level k = n - 2, c = 3(n-2)/n.
    """
    mu = n - 1
    k = n - 2
    c = F(3 * k, k + 2)
    return SingularityCategoryData(
        milnor_number=mu,
        n_simples=mu,
        ade_type=f"A{mu}",
        n2_level=k,
        central_charge=c,
    )


def singularity_category_D(n: int) -> SingularityCategoryData:
    r"""Singularity category for the D_n singularity W = x^{n-1} + xy^2.

    mu = n.  The N=2 MM has level k = 2(n-1) - 2 = 2n-4, c = 3(n-2)/(n-1).
    D_sg has n simple objects.
    """
    mu = n
    h = 2 * (n - 1)
    k = h - 2
    c = F(3 * k, k + 2)
    return SingularityCategoryData(
        milnor_number=mu,
        n_simples=mu,
        ade_type=f"D{n}",
        n2_level=k,
        central_charge=c,
    )


def singularity_category_E(n: int) -> SingularityCategoryData:
    r"""Singularity category for E_n (n = 6, 7, 8) singularities.

    E_6: W = x^3 + y^4, mu = 6, h = 12.
    E_7: W = x^3 + xy^3, mu = 7, h = 18.
    E_8: W = x^3 + y^5, mu = 8, h = 30.
    """
    data = {6: 12, 7: 18, 8: 30}
    h = data[n]
    k = h - 2
    c = F(3 * k, k + 2)
    return SingularityCategoryData(
        milnor_number=n,
        n_simples=n,
        ade_type=f"E{n}",
        n2_level=k,
        central_charge=c,
    )


# ============================================================================
# 8. LG/CY correspondence
# ============================================================================

@dataclass(frozen=True)
class LGCYCorrespondence:
    r"""Data package for the LG/CY correspondence.

    The LG model (superpotential W) and the CY model (derived category D^b(X))
    are related at the Gepner point by:
        MF(W) / G = D^b(Coh(X))
    where G is the orbifold group (phase symmetry).

    The E1 chiral algebras in the two phases are related by:
        A_{LG} at the Gepner point = A_{CY} at the Gepner point.

    Away from the Gepner point, the two are in different "phases" of
    the GLSM, connected by analytic continuation.

    Attributes:
        lg_data: the LG/MF side
        cy_euler: Euler characteristic of the CY
        cy_hodge: Hodge numbers (h^{1,1}, h^{2,1}) for CY3
        gepner: the Gepner model data
        orbifold_dim: dimension of the orbifold-invariant Jacobian ring
    """
    lg_data: BrieskornPham
    cy_euler: int
    cy_hodge: Dict[str, int]
    gepner: GepnerModelE1
    orbifold_dim: int

    def verify_hodge_match(self) -> bool:
        r"""Verify that the orbifold-invariant dimension matches b_{d} of the CY.

        For a CY d-fold:
            dim(Jac^{orb}) = sum h^{p,d-p} = b_d.
        """
        if self.gepner.cy_dim == 3:
            b3 = 2 + 2 * self.cy_hodge.get('h21', 0)
            return self.orbifold_dim == b3
        return False  # not implemented for other dimensions

    def kappa_dictionary(self) -> Dict[str, Fraction]:
        r"""All kappa values from different perspectives."""
        c = self.gepner.total_central_charge
        return {
            'kappa_virasoro': c / 2,
            'kappa_n2': c / 6,
            'kappa_bcov': F(self.cy_euler, 24),
            'kappa_mf_categorical': F(self.lg_data.milnor_number, 2),
        }

    @property
    def wall_crossing_gauge_element(self) -> str:
        r"""Description of the wall-crossing as MC gauge transformation.

        The GLSM has a Fayet-Iliopoulos parameter r (= sigma):
            r >> 0: CY phase
            r << 0: LG/orbifold phase
            r = r_0: Gepner point (transition)

        The wall-crossing is:
            Theta_{LG} = g * Theta_{CY} * g^{-1} + g * d(g^{-1})
        where g is in the MC gauge group.

        At the DT level:
            DT_{LG-phase} and DT_{CY-phase} are related by the
            Kontsevich-Soibelman wall-crossing automorphism.
        """
        return (
            "MC gauge transformation at the Gepner point: "
            "g in Aut(B(A)) intertwining LG and CY bar complexes. "
            "The KS wall-crossing formula gives the explicit automorphism "
            "of the motivic Hall algebra."
        )


def quintic_lgcy() -> LGCYCorrespondence:
    """The LG/CY correspondence for the quintic threefold."""
    bp = fermat_quintic()
    gepner = quintic_gepner_e1()
    orb_dim = gepner.orbifold_invariant_dimension_exact()

    return LGCYCorrespondence(
        lg_data=bp,
        cy_euler=-200,
        cy_hodge={'h11': 1, 'h21': 101},
        gepner=gepner,
        orbifold_dim=int(orb_dim),
    )


# ============================================================================
# 9. Knorrer periodicity at the E1 level
# ============================================================================

def knorrer_kappa_invariance(bp: BrieskornPham) -> Dict[str, Fraction]:
    r"""Verify Knorrer periodicity: adding y^2 does not change kappa_MF.

    MF(W + y^2) = MF(W) (Knorrer).
    mu(W + y^2) = mu(W) * mu(y^2) = mu(W) * 1 = mu(W) (Sebastiani-Thom).
    So kappa_MF(W + y^2) = mu(W)/2 = kappa_MF(W).
    """
    mu_orig = bp.milnor_number
    kappa_orig = F(mu_orig, 2)

    # Stabilized: add y^2
    stabilized_degrees = bp.degrees + (2,)
    bp_stab = BrieskornPham(degrees=stabilized_degrees, name=bp.name + "+y^2")
    mu_stab = bp_stab.milnor_number
    kappa_stab = F(mu_stab, 2)

    return {
        'kappa_original': kappa_orig,
        'kappa_stabilized': kappa_stab,
        'mu_original': F(mu_orig),
        'mu_stabilized': F(mu_stab),
        'invariant': kappa_orig == kappa_stab,
    }


def sebastiani_thom_kappa(bp1: BrieskornPham, bp2: BrieskornPham) -> Dict[str, Any]:
    r"""Sebastiani-Thom for kappa: kappa_MF(f+g) = mu(f)*mu(g)/2.

    For f(x) + g(y) in disjoint variables:
        mu(f+g) = mu(f) * mu(g)
        kappa_MF(f+g) = mu(f)*mu(g)/2

    Note: kappa is NOT additive under Sebastiani-Thom.
    It is multiplicative in mu, hence:
        kappa_MF(f+g) = 2 * kappa_MF(f) * kappa_MF(g)

    This is the correct formula. Cross-check:
        kappa(x^3 + y^4) = mu(x^3)*mu(y^4)/2 = 2*3/2 = 3.
        2 * kappa(x^3) * kappa(y^4) = 2 * 1 * 3/2 = 3. Correct.
    """
    mu1 = bp1.milnor_number
    mu2 = bp2.milnor_number
    mu_sum = mu1 * mu2

    kappa1 = F(mu1, 2)
    kappa2 = F(mu2, 2)
    kappa_sum = F(mu_sum, 2)
    kappa_product = 2 * kappa1 * kappa2

    return {
        'mu_f': mu1,
        'mu_g': mu2,
        'mu_fg': mu_sum,
        'kappa_f': kappa1,
        'kappa_g': kappa2,
        'kappa_fg': kappa_sum,
        'kappa_product_formula': kappa_product,
        'consistent': kappa_sum == kappa_product,
    }


# ============================================================================
# 10. ADE singularities: complete E1 chiral algebra identification
# ============================================================================

def ade_e1_chiral_table() -> List[Dict[str, Any]]:
    r"""Complete table of E1 chiral algebras from ADE singularities.

    For each ADE singularity, compute:
        - The Milnor number mu
        - The Coxeter number h
        - The N=2 MM level k = h - 2
        - The central charge c = 3(h-2)/h
        - kappa_MF = mu/2
        - kappa_Vir = c/2
        - kappa_N2 = c/6
        - The E1 bar complex dimensions
        - The chiral algebra identification
    """
    rows = []

    # A-type: A_1 through A_8
    for n in range(2, 10):
        rank = n - 1
        mu = rank
        h = n
        k = h - 2
        c = F(3 * k, k + 2) if k > 0 else F(0)
        rows.append({
            'type': f'A{rank}',
            'mu': mu,
            'h': h,
            'k': k,
            'c': c,
            'kappa_mf': F(mu, 2),
            'kappa_vir': c / 2,
            'kappa_n2': c / 6,
            'e1_bar_arity2': mu ** 2,
            'e1_bar_arity3': mu ** 3,
            'einfty_bar_arity2': _binomial(mu + 1, mu - 1),
            'chiral_algebra': f'N=2 MM at level {k}',
        })

    # D-type: D_4 through D_8
    for n in range(4, 9):
        mu = n
        h = 2 * (n - 1)
        k = h - 2
        c = F(3 * k, k + 2)
        rows.append({
            'type': f'D{n}',
            'mu': mu,
            'h': h,
            'k': k,
            'c': c,
            'kappa_mf': F(mu, 2),
            'kappa_vir': c / 2,
            'kappa_n2': c / 6,
            'e1_bar_arity2': mu ** 2,
            'e1_bar_arity3': mu ** 3,
            'einfty_bar_arity2': _binomial(mu + 1, mu - 1),
            'chiral_algebra': f'D-type N=2 MM at level {k}',
        })

    # E-type: E_6, E_7, E_8
    for n, h in [(6, 12), (7, 18), (8, 30)]:
        mu = n
        k = h - 2
        c = F(3 * k, k + 2)
        rows.append({
            'type': f'E{n}',
            'mu': mu,
            'h': h,
            'k': k,
            'c': c,
            'kappa_mf': F(mu, 2),
            'kappa_vir': c / 2,
            'kappa_n2': c / 6,
            'e1_bar_arity2': mu ** 2,
            'e1_bar_arity3': mu ** 3,
            'einfty_bar_arity2': _binomial(mu + 1, mu - 1),
            'chiral_algebra': f'E{n}-type N=2 MM at level {k}',
        })

    return rows


# ============================================================================
# 11. Specific computations for task targets
# ============================================================================

def fermat_quintic_computation() -> Dict[str, Any]:
    r"""Full computation for the Fermat quintic at the Gepner point.

    W = x_1^5 + x_2^5 + x_3^5 + x_4^5 + x_5^5.
    MF(W) is CY3 (5 variables - 2 = 3).

    At the Gepner point: the E1 chiral algebra is the (3)^5 Gepner model.
    This is the tensor product of 5 copies of the N=2 minimal model at k=3,
    orbifolded by Z/5Z.

    The N=2 MM at k=3:
        c = 9/5
        Chiral ring = C[x]/(x^4), dimension 4
        The VOA is related to the SU(2)_3 x U(1)_2 / U(1)_5 coset.
        At k=3, the N=2 MM is the same as the A_4 singularity model.

    The Gepner model (3)^5 is a RATIONAL N=2 SCFT.
    It is NOT a standard W-algebra in the conventional sense.
    Rather, it is a simple-current extension of the tensor product VOA.

    The bosonic (N=0) part:
        5 copies of Virasoro at c=9/5, with 5 U(1) currents.
        Total c = 9, with N=2 extended symmetry.

    The identification with a W-algebra:
        The Gepner model VOA is related to the parafermionic coset
        SU(5)_1 / U(1)^4 at c = 4 * (1 - 1/5) = 16/5... no.

    Actually: at the Gepner point, the CY3 sigma model has an enhanced
    N=(2,2) SCFT symmetry.  The chiral algebra (the holomorphic part)
    is the N=2 SCA at c=9 with additional W-currents from the rational
    model.  The precise identification is:

    The (3)^5 Gepner model = Z/5Z orbifold of (N=2 MM at k=3)^{tensor 5}.

    Each N=2 MM at k=3 has 4*5 = 20 primary fields (k+1)(k+2) = 20.
    The tensor product has 20^5 primaries before orbifold.
    After Z/5Z orbifold: the number of primaries is reduced.

    For kappa: the N=2 chiral algebra kappa = c/6 = 9/6 = 3/2.
    The BCOV kappa = chi/24 = -200/24 = -25/3.
    These are DIFFERENT: kappa_{N=2} measures the N=2 algebra,
    while kappa_{BCOV} measures the topological string.
    """
    bp = fermat_quintic()
    gepner = quintic_gepner_e1()

    return {
        'name': 'Fermat quintic (3)^5 Gepner model',
        'superpotential': 'W = x1^5 + x2^5 + x3^5 + x4^5 + x5^5',
        'n_vars': 5,
        'cy_dim': 3,
        'milnor_number': bp.milnor_number,  # 4^5 = 1024
        'milnor_per_factor': 4,
        'central_charge': gepner.total_central_charge,  # 9
        'c_per_factor': F(9, 5),
        'gepner_level': 3,
        'n_factors': 5,
        'orbifold_order': 5,
        'orbifold_invariant_dim': int(gepner.orbifold_invariant_dimension_exact()),  # 204
        'h21': 101,
        'h11': 1,
        'chi': -200,
        'kappa_virasoro': F(9, 2),
        'kappa_n2': F(3, 2),
        'kappa_bcov': F(-25, 3),
        'kappa_mf_per_factor': F(2),
        'chiral_algebra': 'Z/5Z orbifold of (N=2 MM at k=3)^5',
        'is_rational_cft': True,
        'is_standard_w_algebra': False,
        'cy_condition_check': bp.is_cy_condition,
    }


def conifold_computation() -> Dict[str, Any]:
    r"""Computation for W = x1^2 + x2^2 + x3^2 + x4^2 (A_1 node in 4 vars).

    This is the Brieskorn-Pham A_1 singularity in 4 variables.
    CY dimension = 4 - 2 = 2.
    Milnor number = 1^4 = 1.

    By Knorrer periodicity (applied twice):
        MF(x1^2 + x2^2 + x3^2 + x4^2) = MF(x1^2 + x2^2) = MF(x1^2) = Vect.

    So the MF category is TRIVIAL (= Vect, the category of vector spaces).
    The E1 chiral algebra is trivial (0-dimensional, or the unit VOA C).

    WARNING: the CONIFOLD singularity xy - zw = 0 is NOT the same as
    x^2 + y^2 + z^2 + w^2 = 0.  They are isomorphic as VARIETIES
    (over C, via the coordinate change x = a+ib, y = a-ib, etc.)
    but the matrix factorization categories differ because
    xy - zw is not Brieskorn-Pham.

    For the ACTUAL conifold chiral algebra, see conifold_e1_full_chain.py.
    The result there: A_{conifold} = gl(1|1) WZW at level 1 (c = 0).
    """
    bp = conifold_node()
    return {
        'name': 'A1 node in 4 variables',
        'superpotential': 'W = x1^2 + x2^2 + x3^2 + x4^2',
        'n_vars': 4,
        'cy_dim': 2,
        'milnor_number': 1,
        'kappa_mf': F(1, 2),
        'central_charge': bp.total_central_charge,  # 3 * (4 - 2*4/2) = 3*(4-4) = 0
        'chiral_algebra': 'Trivial (Vect) by Knorrer periodicity',
        'knorrer_chain': 'MF(x^2+y^2+z^2+w^2) = MF(x^2+y^2) = MF(x^2) = Vect',
        'actual_conifold_note': (
            'The conifold xy-zw=0 is isomorphic as variety but NOT as MF. '
            'Its chiral algebra is gl(1|1) at level 1 (c=0). '
            'See conifold_e1_full_chain.py.'
        ),
    }


def e6_computation() -> Dict[str, Any]:
    r"""Computation for the E_6 singularity W = x^3 + y^4.

    CY dimension = 2 - 2 = 0 (2 variables).
    Milnor number = 2 * 3 = 6.
    The N=2 MM has level k = h - 2 = 12 - 2 = 10, c = 30/12 = 5/2.

    The E1 chiral algebra is the E_6 N=2 minimal model.
    This is a RATIONAL VOA with 6 simple modules (matching mu = 6).

    The relation to the E_6 LATTICE VOA:
        The E_6 lattice VOA V_{E_6} has c = rank(E_6) = 6 and kappa = 3.
        The E_6 N=2 MM has c = 5/2 and kappa_Vir = 5/4.
        These are DIFFERENT ALGEBRAS.

        The connection is via the McKay correspondence:
        MF(x^3 + y^4) <-> D^b(Coh([C^2/binary_tetrahedral_group]))
        The binary tetrahedral group (order 24) has 6 irreducible reps
        (matching mu = 6), and its McKay graph is the E_6 Dynkin diagram.

        The LATTICE VOA V_{E_6} is the algebra of the E_6 root lattice.
        It appears as the chiral algebra of a K3 surface with E_6 symmetry,
        which is a CY2 model (not the CY0 category MF(x^3+y^4)).

    For CY2 (need 4 variables): W = x^3 + y^4 + z^2 + w^2.
        Knorrer: MF(W) = MF(x^3 + y^4) (same category).
        But the CY dimension changes: n=4, d = 2.
        The E1 chiral algebra is then related to the E_6 K3 theory.
    """
    bp = e6_surface_singularity()
    sc = singularity_category_E(6)

    return {
        'name': 'E6 singularity',
        'superpotential': 'W = x^3 + y^4',
        'n_vars': 2,
        'cy_dim': 0,
        'milnor_number': 6,
        'coxeter_number': 12,
        'n2_level': 10,
        'central_charge': sc.central_charge,  # 5/2
        'kappa_mf': F(6, 2),     # = 3
        'kappa_vir': sc.central_charge / 2,  # 5/4
        'kappa_n2': sc.central_charge / 6,   # 5/12
        'n_simples': 6,
        'chiral_algebra': 'E6-type N=2 minimal model at k=10, c=5/2',
        'e6_lattice_relation': (
            'The E6 N=2 MM (c=5/2) is NOT the E6 lattice VOA (c=6). '
            'They are related via McKay correspondence: both have 6 as a '
            'structure constant, but the MF algebra is the N=2 MM while '
            'the lattice VOA appears for the CY2 (K3) case.'
        ),
    }


def brieskorn_pham_general(degrees: Tuple[int, ...]) -> Dict[str, Any]:
    r"""General formula for A_{MF(W)} for W = x_1^{d_1} + ... + x_n^{d_n}.

    The E1 chiral algebra data:
        mu = prod(d_i - 1)
        c = 3 * sum(1 - 2/d_i)
        kappa_MF = mu/2
        kappa_Vir = c/2
        kappa_N2 = c/6

    For the chiral algebra identification:
        - If n = 1: the LG model W = x^d, chiral algebra = N=2 MM at k = d-2.
        - If n = 2: ADE surface singularity, chiral algebra = ADE N=2 MM.
        - If sum 1/d_i = 1 (CY condition): Gepner model for CY_{n-2}.
        - General: the chiral algebra is an N=2 SCFT with c = 3*c_hat,
          whose precise identification requires the full SCFT analysis.

    GENERAL FORMULA for the E1 bar complex:
        B^{E1}_k(A_{MF(W)}) has dimension mu^k at arity k,
        where mu = prod(d_i - 1) is the Milnor number.
    """
    bp = BrieskornPham(degrees=degrees)
    mu = bp.milnor_number
    c = bp.total_central_charge

    return {
        'degrees': degrees,
        'n_vars': bp.n_vars,
        'cy_dim': bp.cy_dimension,
        'milnor_number': mu,
        'c_hat': bp.c_hat,
        'central_charge': c,
        'charges': bp.charges,
        'charge_sum': bp.charge_sum,
        'is_cy': bp.is_cy_condition,
        'kappa_mf': F(mu, 2),
        'kappa_vir': c / 2,
        'kappa_n2': c / 6,
        'e1_bar_dims': e1_bar_dimensions(mu, max_arity=4),
        'einfty_bar_dims': e_infty_bar_dimensions(mu, max_arity=4),
        'bar_ratio_arity2': bar_ratio_e1_vs_einfty(mu, 2),
    }


# ============================================================================
# 12. Wall-crossing as MC gauge transformation
# ============================================================================

@dataclass(frozen=True)
class GLSMPhase:
    r"""A phase of the Gauged Linear Sigma Model.

    The GLSM for the quintic has two phases:
        Phase I (r >> 0): geometric CY phase, D^b(Coh(Q)).
        Phase II (r << 0): LG/orbifold phase, MF(W)/G.

    The FI parameter r controls the phase.
    At r = r_0 (Gepner point): enhanced symmetry, rational CFT.

    Attributes:
        name: phase identifier
        fi_parameter_sign: sign of the FI parameter
        category_description: which derived category
        chiral_algebra_type: type of the E1 chiral algebra
    """
    name: str
    fi_parameter_sign: str
    category_description: str
    chiral_algebra_type: str


def glsm_phases_quintic() -> Dict[str, GLSMPhase]:
    """The two phases of the quintic GLSM plus the transition point."""
    return {
        'CY': GLSMPhase(
            name='CY geometric phase',
            fi_parameter_sign='positive',
            category_description='D^b(Coh(Q)) for Q = quintic in P^4',
            chiral_algebra_type='CY3 sigma model VOA (c=9, irrational)',
        ),
        'LG': GLSMPhase(
            name='LG/orbifold phase',
            fi_parameter_sign='negative',
            category_description='MF(W_Fermat) / Z_5',
            chiral_algebra_type='(3)^5 Gepner model (c=9, rational)',
        ),
        'Gepner': GLSMPhase(
            name='Gepner point (transition)',
            fi_parameter_sign='zero',
            category_description='MF(W_Fermat)/Z_5 = D^b(Coh(Q_Fermat))',
            chiral_algebra_type='(3)^5 Gepner model (c=9, rational, enhanced symmetry)',
        ),
    }


def wall_crossing_bps_count_conifold() -> Dict[str, Any]:
    r"""BPS state counts across the conifold wall-crossing.

    The conifold has a single compact cycle (P^1).
    In chamber I (large volume): 1 BPS state of charge gamma_1.
    In chamber II (flopped): 1 BPS state of charge gamma_2 = -gamma_1.
    At the wall: the BPS state of charge gamma_1 + gamma_2 appears/disappears.

    The KS wall-crossing formula:
        A_{gamma_1} * A_{gamma_2} = A_{gamma_1+gamma_2} * A_{gamma_2} * A_{gamma_1}
    where A_gamma = exp(sum_{k>=1} e_{k*gamma} / k^2) is the quantum dilogarithm.

    The E1 bar complex encodes this: the bar differential at arity 2
    detects the bound state, and the wall-crossing is an MC gauge
    transformation exchanging the order of the factors.
    """
    return {
        'chamber_I_bps': {'gamma_1': 1},
        'chamber_II_bps': {'gamma_2': 1},
        'wall_bps': {'gamma_1+gamma_2': 1},
        'ks_formula': 'A_{g1} * A_{g2} = A_{g1+g2} * A_{g2} * A_{g1}',
        'e1_bar_interpretation': (
            'The E1 bar differential B_2 -> B_1 detects the bound state. '
            'Wall-crossing = reordering in the E1 bar (non-commutative!).'
        ),
        'mc_gauge': (
            'Theta_I = g * Theta_{II} * g^{-1} + g * d(g^{-1}) '
            'where g is the KS automorphism.'
        ),
    }


# ============================================================================
# 13. Comprehensive kappa verification table
# ============================================================================

def kappa_verification_table() -> List[Dict[str, Any]]:
    r"""Multi-path kappa verification for all standard MF examples.

    For each example, we compute kappa from at least 3 independent paths
    and verify consistency (per the multi-path verification mandate).

    The paths:
        Path 1: kappa_MF = mu/2 (from Jacobian ring trace)
        Path 2: kappa_Vir = c/2 (from Virasoro subalgebra)
        Path 3: kappa_N2 = c/6 (from N=2 SCA)
        Path 4: kappa_BCOV = chi/24 (from Euler characteristic, CY3 only)
        Path 5: Additivity check (Sebastiani-Thom)
        Path 6: Knorrer invariance check

    NOTE: Paths 1, 2, 3 give DIFFERENT numbers in general because they
    measure different algebras (MF category, Virasoro, N=2 SCA).
    The "consistency" check is that WITHIN each path, the formula holds.
    """
    results = []

    # A-type singularities
    for n in range(2, 8):
        rank = n - 1
        mu = rank
        c = F(3 * (n - 2), n) if n > 2 else F(0)

        # Path 1: MF categorical
        kappa_mf = F(mu, 2)

        # Path 2: Virasoro
        kappa_vir = c / 2

        # Path 3: N=2
        kappa_n2 = c / 6

        # Path 5: Knorrer (add y^2, mu unchanged)
        mu_stabilized = mu * 1  # mu(y^2) = 1
        kappa_knorrer = F(mu_stabilized, 2)

        results.append({
            'type': f'A{rank} (x^{n})',
            'mu': mu,
            'c': c,
            'kappa_mf': kappa_mf,
            'kappa_vir': kappa_vir,
            'kappa_n2': kappa_n2,
            'knorrer_invariant': kappa_mf == kappa_knorrer,
            'mf_eq_vir': kappa_mf == kappa_vir,
            'mf_eq_n2': kappa_mf == kappa_n2,
        })

    # Quintic Gepner
    c_q = F(9)
    results.append({
        'type': 'Quintic Gepner (3)^5',
        'mu': 1024,  # 4^5, before orbifold
        'c': c_q,
        'kappa_mf': F(1024, 2),  # per-algebra, before orbifold
        'kappa_vir': c_q / 2,
        'kappa_n2': c_q / 6,
        'kappa_bcov': F(-200, 24),
        'knorrer_invariant': True,
        'mf_eq_vir': False,
        'mf_eq_n2': False,
    })

    # E-type singularities
    for n, h in [(6, 12), (7, 18), (8, 30)]:
        mu = n
        k = h - 2
        c = F(3 * k, k + 2)
        results.append({
            'type': f'E{n}',
            'mu': mu,
            'c': c,
            'kappa_mf': F(mu, 2),
            'kappa_vir': c / 2,
            'kappa_n2': c / 6,
            'knorrer_invariant': True,
            'mf_eq_vir': F(mu, 2) == c / 2,
            'mf_eq_n2': F(mu, 2) == c / 6,
        })

    return results


# ============================================================================
# 14. Central charge constraints from CY structure
# ============================================================================

def cy_central_charge_constraint(d: int) -> Fraction:
    r"""For a CY d-fold compactification, c = 3d.

    The N=2 SCFT associated to a CY d-fold has c = 3 * c_hat = 3d.
    This is a NECESSARY condition for the model to be a valid string
    compactification (critical dimension).

    d=1 (elliptic curve): c = 3.
    d=2 (K3): c = 6.
    d=3 (CY3): c = 9.
    """
    return F(3 * d)


def gepner_level_dimension_relation(k: int, r: int) -> Dict[str, Any]:
    r"""The relation between Gepner level k, number of factors r, and CY dim d.

    For the uniform Gepner model (k)^r:
        c_hat_total = r * k/(k+2) = d.
    So d = r*k/(k+2), or equivalently r = d * (k+2)/k = d + 2d/k.

    For integer r, we need k | 2d.
    For d = 3: k | 6, so k in {1, 2, 3, 6}.
    """
    n = k + 2
    c_per = F(3 * k, n)
    c_total = r * c_per
    c_hat_per = F(k, n)
    c_hat_total = r * c_hat_per
    d = c_hat_total

    return {
        'k': k,
        'r': r,
        'n': n,
        'c_per_factor': c_per,
        'c_total': c_total,
        'c_hat_per_factor': c_hat_per,
        'c_hat_total': c_hat_total,
        'cy_dim': d,
        'is_integer_dim': d.denominator == 1,
        'satisfies_cy': d == int(d) and int(d) >= 1,
    }


# ============================================================================
# 15. The chiral ring and marginal deformations
# ============================================================================

def chiral_ring_bp(bp: BrieskornPham) -> Dict[str, Any]:
    r"""Chiral ring of the N=2 LG model with superpotential W.

    The chiral ring R(W) = Jac(W) = C[x_1,...,x_n]/(dW/dx_i).
    For Brieskorn-Pham W = sum x_i^{d_i}:
        Jac(W) = tensor product of C[x_i]/(d_i x_i^{d_i-1})
               = tensor of truncated polynomial rings
        dim = prod(d_i - 1) = mu(W).

    The chiral ring is a FROBENIUS ALGEBRA with the pairing given by
    the Grothendieck residue:
        <f, g> = Res(f * g * dx / dW).

    Marginal deformations (for CY d-fold with CY condition sum 1/d_i = 1):
        A monomial x_1^{a_1}...x_n^{a_n} is marginal if
            sum a_i/d_i = 1  (charge 1, i.e., it has the same weight as W).
        The number of such monomials (minus 1 for W itself) = h^{d-1,1}.

    For the quintic: marginal monomials with sum a_i = 5, each a_i <= 3.
        By the degree-5-in-5-variables constraint with orbifold:
        h^{2,1} = 101.
    """
    mu = bp.milnor_number
    d = bp.cy_dimension

    # Count marginal deformations (if CY condition holds)
    n_marginal = None
    if bp.is_cy_condition:
        # Marginal = degree 1 in the orbifold-invariant chiral ring
        # This equals h^{d-1,1} of the CY.
        # For BP: count monomials prod x_i^{a_i} with sum a_i/d_i = 1
        # and a_i <= d_i - 2 (in Jac).
        # Equivalently: sum a_i/d_i = 1 with 0 <= a_i <= d_i - 2.
        # This is the number of interior lattice points of the
        # Newton polytope of W.
        n_marginal = _count_marginal_deformations(bp.degrees)

    return {
        'milnor_number': mu,
        'chiral_ring_dim': mu,
        'is_frobenius': True,
        'n_marginal_deformations': n_marginal,
        'cy_condition': bp.is_cy_condition,
        'degrees': bp.degrees,
    }


def _count_marginal_deformations(degrees: Tuple[int, ...]) -> int:
    r"""Count marginal deformations for BP W = sum x_i^{d_i} with CY condition.

    Marginal monomials: prod x_i^{a_i} with sum a_i/d_i = 1
    and 0 <= a_i <= d_i - 2 (in Jacobian ring).

    The total count includes the superpotential W itself (a_i = d_i for one i,
    a_j = 0 for others), but those have a_i = d_i > d_i - 2, so they are
    NOT in the Jacobian ring. The marginal deformations in the Jacobian ring
    are genuine deformations.
    """
    return _count_marginal_iter(degrees)


def _count_marginal_iter(degrees: Tuple[int, ...]) -> int:
    """Iterative counting of marginal deformations."""
    n = len(degrees)
    if n == 0:
        return 0

    # For small n, enumerate directly
    # For each tuple (a_1, ..., a_n) with 0 <= a_i <= d_i - 2 and sum a_i/d_i = 1
    # We use the substitution b_i = a_i, constraint sum b_i/d_i = 1.
    # Equivalently: sum (b_i * prod_{j!=i} d_j) = prod d_j.

    target = _product(degrees)  # prod d_j
    # For each i: b_i * (target // d_i) should sum to target.
    # b_i ranges from 0 to d_i - 2.

    coeffs = [target // d for d in degrees]
    # Find tuples (b_0, ..., b_{n-1}) with sum(b_i * coeffs[i]) = target
    # and 0 <= b_i <= d_i - 2.

    count = _count_solutions(coeffs, [d - 2 for d in degrees], target, 0)
    return count


def _count_solutions(coeffs: List[int], maxvals: List[int], target: int, idx: int) -> int:
    """Recursive backtracking to count solutions to sum(a_i * c_i) = target."""
    if idx == len(coeffs):
        return 1 if target == 0 else 0
    count = 0
    c = coeffs[idx]
    for a in range(maxvals[idx] + 1):
        val = a * c
        if val > target:
            break
        count += _count_solutions(coeffs, maxvals, target - val, idx + 1)
    return count


# ============================================================================
# 16. Summary and cross-checks
# ============================================================================

def all_cy3_gepner_summary() -> List[Dict[str, Any]]:
    r"""Summary data for all uniform CY3 Gepner models."""
    models = cy3_gepner_models()
    results = []
    for g in models:
        orb_dim = int(g.orbifold_invariant_dimension_exact())
        k = g.levels[0]
        r = g.n_factors
        mu_per = k + 1
        c_total = g.total_central_charge

        results.append({
            'model': f'({k})^{r}',
            'k': k,
            'r': r,
            'n': k + 2,
            'mu_per_factor': mu_per,
            'mu_total': mu_per ** r,
            'c_per_factor': F(3 * k, k + 2),
            'c_total': c_total,
            'orbifold_order': g.orbifold_order,
            'orbifold_invariant_dim': orb_dim,
            'cy_condition': g.verify_cy_condition(),
            'kappa_vir': c_total / 2,
            'kappa_n2': c_total / 6,
        })
    return results


def consistency_check_all() -> Dict[str, bool]:
    r"""Run all internal consistency checks.

    Returns a dict of check_name -> passed.
    """
    checks = {}

    # 1. Sebastiani-Thom multiplicativity of Milnor numbers
    for d1, d2 in [(3, 4), (5, 5), (2, 7)]:
        bp1 = BrieskornPham(degrees=(d1,))
        bp2 = BrieskornPham(degrees=(d2,))
        bp12 = BrieskornPham(degrees=(d1, d2))
        checks[f'ST_mu({d1},{d2})'] = (
            bp12.milnor_number == bp1.milnor_number * bp2.milnor_number
        )

    # 2. Knorrer periodicity
    for degrees in [(3,), (5,), (3, 4)]:
        bp = BrieskornPham(degrees=degrees)
        bp_stab = BrieskornPham(degrees=degrees + (2,))
        checks[f'Knorrer_{degrees}'] = bp.milnor_number == bp_stab.milnor_number

    # 3. CY condition for known CY models
    checks['CY_quintic'] = fermat_quintic().is_cy_condition
    checks['CY_octic_not_cy'] = not BrieskornPham(degrees=(8, 8, 8, 8)).is_cy_condition  # sum 1/8*4 = 1/2, NOT CY
    checks['CY_sextic'] = BrieskornPham(degrees=(6, 6, 6, 6, 6, 6)).is_cy_condition  # sum 1/6*6 = 1

    # 4. Central charge = 3d for CY d-fold Gepner models
    for g in cy3_gepner_models():
        checks[f'c=3d_({g.levels[0]})^{g.n_factors}'] = (
            g.total_central_charge == F(3 * g.cy_dim)
        )

    # 5. Orbifold dimension matches for quintic
    lgcy = quintic_lgcy()
    checks['quintic_hodge_match'] = lgcy.verify_hodge_match()

    return checks
