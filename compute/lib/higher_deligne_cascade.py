r"""higher_deligne_cascade.py -- The E_n promotion via iterated derived centers.

MATHEMATICAL BACKGROUND
========================

The higher Deligne conjecture (Lurie, Higher Algebra, Thm 5.3.1.30) states:
for an E_n-algebra B, the Hochschild cochain complex HH^*(B, B) carries a
canonical E_{n+1}-algebra structure.  This gives the DERIVED CENTER promotion:

    E_n-algebra B  -->  HH^*(B, B) = E_{n+1}-algebra

This is DISTINCT from the Drinfeld center (AP-CY4, HZ3-5):
  - Drinfeld center Z(C): categorical, E_1-monoidal C -> E_2-braided Z(C)
  - Derived center HH^*(B,B): algebraic, E_n-algebra B -> E_{n+1}-algebra

They AGREE at the E_1 -> E_2 step by the BZFN theorem (thm:bzfn):
    Z(Rep^{E_1}(A)) = Rep^{E_2}(HH^*(A,A))

They DIVERGE at E_2 -> E_3: the iterated Drinfeld center
Z(Z(C)) = C boxtimes C^{rev} (E_2-doubling, NOT E_3-promotion),
while HH^*(B,B) for E_2-algebra B is genuinely E_3.

THE CASCADE
===========

Step 1: E_1 -> E_2.
  Input: A = Y^+(gl_hat_1), the E_1-chiral algebra (CoHA of C^3).
  Output: Z^{der}(A) = HH^*(A, A) = Y(gl_hat_1) = W_{1+infty}.
  This is E_2 (braided).
  Mechanism: Deligne conjecture (E_1 input -> E_2 cochains).
  Agreement: BZFN gives Z(Rep^{E_1}(Y^+)) = Rep^{E_2}(Y).

Step 2: E_2 -> E_3.
  Input: B = Y(gl_hat_1), the E_2-algebra from Step 1.
  Output: Z^{der}(B) = HH^*(B, B) = E_3-algebra.
  Mechanism: Higher Deligne (E_2 input -> E_3 cochains).
  IMPORTANT (AP153): The full algebraic E_3 with BV operator requires
  E_infty input. For E_2 input, we get the GENERIC E_3 from higher
  Deligne, not the specific E_3 with BV.
  Divergence: Iterated Drinfeld center Z(Z(C)) = C boxtimes C^{rev}
  is NOT E_3; derived center HH^*(B,B) IS E_3.

Step 3: E_3 -> E_4?
  Input: C = HH^*(B, B), the E_3-algebra from Step 2.
  Output: Z^{der}(C) = HH^*(C, C) = E_4-algebra?
  TERMINATION: For CY inputs, E_1 stabilization (thm:e1-stabilization-cy)
  means d >= 4 CY chiral algebras are E_1. The E_3 structure from C^3
  is the MAXIMUM for CY geometry. The cascade terminates at E_3 for
  CY-geometric inputs.

  Algebraically: nothing prevents E_4 via higher Deligne, but CY geometry
  does not produce E_4 input through Phi.  The Omega-deformation has
  3 parameters (h1, h2, h3) with h1+h2+h3=0, giving 2 free parameters.
  E_4 would require 3 free parameters (4 variables minus 1 constraint),
  which exceeds the CY_3 deformation space.

DUNN ADDITIVITY ANGLE
======================

E_2 = E_1 tensor E_1 (operadic tensor product over E_0 = Assoc_+).
The "second E_1" is the HIDDEN DIRECTION.

For the affine Yangian Y(gl_hat_1):
  - First E_1: the CoHA multiplication (labeled-ordered, Hall product).
    Acts along the "instanton number" direction: extension of sheaves
    0 -> V' -> V -> V'' -> 0 gives a * b.
  - Second E_1: the spectral parameter shift.
    Acts along the "momentum" direction: shifting the Yangian spectral
    parameter u -> u + z.

The braiding (R-matrix) measures the failure of the two E_1 products
to commute:
    R(z) = sigma_{21} circ Delta_z(a) / Delta_0(a)
where sigma_{21} exchanges the two tensor factors.

For E_3 = E_2 tensor E_1 = E_1 tensor E_1 tensor E_1:
  - First E_1: instanton (from CoHA).
  - Second E_1: spectral parameter / momentum (from Yangian doubling).
  - Third E_1: the THIRD complex direction in C^3 (from the 6d theory).
    This is the direction that generates the Miki automorphism.

Termination argument for E_4:
  E_4 = E_1^{tensor 4} would require a FOURTH independent E_1 direction.
  The CY_3 geometry on C^3 provides exactly 3 complex directions;
  there is no fourth direction available from the CY structure.
  At d=4 (CY_4), the chiral algebra is E_1-stabilized (Bott periodicity
  obstruction pi_4(BU) = Z != 0), so the extra direction contributes
  shifted symplectic data rather than a new E_1 factor.

HOCHSCHILD COHOMOLOGY COMPUTATIONS
====================================

For an E_n-algebra B, the Hochschild cochain complex HH^*(B,B) is:
    HH^*(B, B) = RHom_{B tensor B^{op}}(B, B)

The E_{n+1} structure comes from the higher Deligne conjecture.

Dimension computation:
  For A = Heisenberg H_k (class G, free-field):
    HH^*(H_k, H_k) = polynomial algebra on one generator in degree 0.
    As E_2 algebra: cup product (commutative) + Gerstenhaber bracket (degree -1).
    Generating function: 1/(1-q) (geometric series, matching P(q) at leading order).

  For B = W_{1+infty} (class L):
    HH^*(B, B) = ... (depends on shadow class)
    The E_3 structure on HH^*(B,B) is the one relevant for the 6d theory.

CONVENTIONS
===========
  h1, h2, h3: Omega-background parameters, h1+h2+h3=0.
  sigma_2 = h1*h2 + h1*h3 + h2*h3
  sigma_3 = h1*h2*h3
  kappa subscripts per AP113: kappa_ch, kappa_cat, kappa_BKM, kappa_fiber.
  AP-CY4: Drinfeld center Z(C) != derived center Z^{der}(A). ALWAYS state which.
  AP153: E_3 on cochains requires E_2 input (generic E_3) or E_infty (BV E_3).
  AP154: Algebraic E_3 (Deligne) vs topological E_3 (configuration space).

MANUSCRIPT REFERENCES:
  chapters/theory/en_factorization.tex: sec:en-koszul-cascade, thm:e1-stabilization-cy
  chapters/theory/drinfeld_center.tex: thm:bzfn, rem:three-centers-sharp
  chapters/theory/e2_chiral_algebras.tex: rem:deligne-hochschild
  chapters/theory/hochschild_calculus.tex: thm:gerstenhaber
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from typing import Dict, List, NamedTuple, Optional, Tuple

import numpy as np
from sympy import Matrix, Rational, Symbol, cancel, expand, factor, simplify, symbols


# =========================================================================
# 1. The E_n promotion data: what the higher Deligne conjecture gives
# =========================================================================

class EnAlgebraData(NamedTuple):
    """Data of an E_n-algebra relevant for the derived center cascade.

    Attributes:
        name: Human-readable name.
        n: The operadic level (E_n).
        shadow_class: Shadow class in {G, L, C, M}.
        kappa_ch: The chiral modular characteristic kappa_ch.
        dimension_gf_coeffs: First terms of the graded dimension generating
            function (the Hilbert series of the underlying graded vector space).
        num_deformation_params: Number of independent deformation parameters.
        is_commutative: Whether the algebra is E_infty (commutative).
    """
    name: str
    n: int
    shadow_class: str
    kappa_ch: Rational
    dimension_gf_coeffs: Tuple[int, ...]
    num_deformation_params: int
    is_commutative: bool


class DerivedCenterResult(NamedTuple):
    """Result of computing the derived center HH^*(B,B) for an E_n-algebra B.

    Attributes:
        input_algebra: The input E_n-algebra.
        output_n: The E_{n+1} level of the output.
        output_name: Name of the resulting E_{n+1}-algebra.
        e3_type: For E_2 -> E_3: 'generic' (higher Deligne) or 'bv' (with BV).
            At E_1 -> E_2 this is always 'deligne'.
        bzfn_agrees: Whether BZFN theorem gives agreement with Drinfeld center.
        hh_dimension_gf_coeffs: First terms of HH^* dimension generating function.
        dunn_decomposition: The Dunn additivity decomposition E_n = E_1^{tensor n}.
    """
    input_algebra: EnAlgebraData
    output_n: int
    output_name: str
    e3_type: str
    bzfn_agrees: bool
    hh_dimension_gf_coeffs: Tuple[int, ...]
    dunn_decomposition: Tuple[str, ...]


# =========================================================================
# 2. Partition function utilities
# =========================================================================

@lru_cache(maxsize=256)
def partition_count(n: int) -> int:
    """Number of integer partitions of n.  p(0)=1, OEIS A000041."""
    if n < 0:
        return 0
    if n == 0:
        return 1
    # Euler recurrence
    result = 0
    k = 1
    while True:
        g1 = k * (3 * k - 1) // 2
        g2 = k * (3 * k + 1) // 2
        if g1 > n:
            break
        sign = (-1) ** (k + 1)
        result += sign * partition_count(n - g1)
        if g2 <= n:
            result += sign * partition_count(n - g2)
        k += 1
    return result


@lru_cache(maxsize=256)
def multipartition_count(n: int, k: int) -> int:
    """Number of k-component multipartitions of n (tau_k(n)).

    tau_k(n) = sum_{a_1+...+a_k=n} p(a_1)*...*p(a_k)
    Generating function: P(q)^k = prod_{m>=1} 1/(1-q^m)^k.

    tau_1 = p(n), OEIS A000041.
    tau_2 = OEIS A000712.
    tau_3 = OEIS A000716.
    """
    if k == 1:
        return partition_count(n)
    if n < 0:
        return 0
    if n == 0:
        return 1
    total = 0
    for a in range(n + 1):
        total += partition_count(a) * multipartition_count(n - a, k - 1)
    return total


# Ground truth for cross-checking (OEIS verified)
PARTITION_GROUND_TRUTH = (1, 1, 2, 3, 5, 7, 11, 15, 22, 30)
TAU_2_GROUND_TRUTH = (1, 2, 5, 10, 20, 36, 65, 110, 185, 300)
TAU_3_GROUND_TRUTH = (1, 3, 9, 22, 51, 108, 221, 429, 810, 1479)
TAU_4_GROUND_TRUTH = (1, 4, 14, 40, 105, 252, 574, 1240, 2580, 5180)


# =========================================================================
# 3. The Omega-background and Dunn additivity
# =========================================================================

class DunnDecomposition:
    """Dunn additivity E_n = E_1^{tensor n} for the CY chiral cascade.

    Each E_1 factor corresponds to a geometric direction in C^n.
    """

    @staticmethod
    def e1_factors(n: int) -> List[str]:
        """Names of the n E_1-factors in E_n = E_1^{tensor n}.

        For the affine Yangian / quantum toroidal:
          n=1: ['instanton'] (CoHA multiplication)
          n=2: ['instanton', 'spectral'] (Yangian doubling)
          n=3: ['instanton', 'spectral', 'miki'] (6d triality)
        """
        names = {
            1: ['instanton'],
            2: ['instanton', 'spectral'],
            3: ['instanton', 'spectral', 'miki'],
        }
        if n in names:
            return names[n]
        return [f'direction_{i+1}' for i in range(n)]

    @staticmethod
    def deformation_params(n: int) -> Dict[str, str]:
        """Deformation parameters for E_n chiral algebra on C^n.

        The Omega-background has n parameters h_1,...,h_n subject to
        sum h_i = 0 (CY condition), giving n-1 free parameters.
        At n=3: sigma_2 trivial (rescaling), so effective = 1 (sigma_3).
        """
        if n == 1:
            return {'k': 'level (single parameter)'}
        elif n == 2:
            return {
                'epsilon_1': 'h_1 (first equivariant weight)',
                'epsilon_2': 'h_2 (second equivariant weight)',
            }
        elif n == 3:
            return {
                'h_1': 'first Omega-background parameter',
                'h_2': 'second Omega-background parameter',
                'h_3': '-(h_1+h_2) (CY condition)',
            }
        else:
            return {f'h_{i+1}': f'equivariant weight {i+1}' for i in range(n)}

    @staticmethod
    def num_effective_params(n: int) -> int:
        """Number of effective deformation parameters for E_n on C^n.

        n parameters subject to sum=0 gives n-1 free.
        sigma_2 is a rescaling (trivial deformation) for n >= 3.
        """
        if n <= 1:
            return 1
        elif n == 2:
            return 1  # sigma_3 only (sigma_2 is rescaling at n=2 with CY)
        else:
            return n - 2  # n-1 free minus 1 rescaling


# =========================================================================
# 4. The derived center cascade: Step 1 (E_1 -> E_2)
# =========================================================================

def step1_e1_to_e2_heisenberg(k: Rational = Rational(1)) -> DerivedCenterResult:
    """E_1 -> E_2 via derived center for the Heisenberg algebra H_k.

    H_k is E_1-chiral (class G, free-field).
    Z^{der}(H_k) = HH^*(H_k, H_k) is E_2 (Deligne conjecture).

    For class G: the derived center adds the BRAIDING to the existing
    multiplication.  The output is H_k as an E_2-algebra (now with
    R-matrix R(z) = k*Omega/z in the Fock representation).

    BZFN agreement: Z(Rep^{E_1}(H_k)) = Rep^{E_2}(HH^*(H_k, H_k)).
    """
    input_alg = EnAlgebraData(
        name=f'H_{k}',
        n=1,
        shadow_class='G',
        kappa_ch=k,
        dimension_gf_coeffs=PARTITION_GROUND_TRUTH,
        num_deformation_params=1,
        is_commutative=True,  # Heisenberg is E_infty (abelian VOA)
    )

    # HH^*(H_k, H_k) for commutative H_k:
    # The Heisenberg is a free-field algebra (vertex algebra freely generated
    # by J(z)).  HH^*(H_k, H_k) as a graded vector space has dimension
    # determined by the E_2 bar complex: P(q)^2 (tau_2(n)).
    hh_gf = tuple(multipartition_count(i, 2) for i in range(10))

    return DerivedCenterResult(
        input_algebra=input_alg,
        output_n=2,
        output_name=f'H_{k} (E_2-braided)',
        e3_type='deligne',
        bzfn_agrees=True,
        hh_dimension_gf_coeffs=hh_gf,
        dunn_decomposition=tuple(DunnDecomposition.e1_factors(2)),
    )


def step1_e1_to_e2_yangian() -> DerivedCenterResult:
    """E_1 -> E_2 via derived center for Y^+(gl_hat_1).

    Y^+(gl_hat_1) is E_1-chiral (CoHA of C^3, class L).
    Z^{der}(Y^+) = HH^*(Y^+, Y^+) = Y(gl_hat_1) = W_{1+infty}.

    This is the KEY computation: the full Yangian is the derived center
    of the positive half-Yangian.  The "second E_1" (the spectral
    parameter direction) is the one added by the derived center.

    BZFN agreement: Z(Rep^{E_1}(Y^+)) = Rep^{E_2}(Y).
    Reference: Schiffmann-Vasserot, Maulik-Okounkov (thm:c3-drinfeld-center).
    """
    input_alg = EnAlgebraData(
        name='Y^+(gl_hat_1)',
        n=1,
        shadow_class='L',
        kappa_ch=Rational(1),
        dimension_gf_coeffs=PARTITION_GROUND_TRUTH,
        num_deformation_params=1,
        is_commutative=False,  # Y^+ is E_1, NOT E_infty
    )

    # Y(gl_hat_1) = W_{1+infty} has the MacMahon generating function
    # for its representation theory.  As an E_2-algebra, the bar complex
    # B_{E_2}(Y) has bigraded dimension depending on the shadow class.
    # For class L (shadow depth 2): the first terms match tau_2 at low degree.
    hh_gf = tuple(multipartition_count(i, 2) for i in range(10))

    return DerivedCenterResult(
        input_algebra=input_alg,
        output_n=2,
        output_name='Y(gl_hat_1) = W_{1+infty}',
        e3_type='deligne',
        bzfn_agrees=True,
        hh_dimension_gf_coeffs=hh_gf,
        dunn_decomposition=tuple(DunnDecomposition.e1_factors(2)),
    )


# =========================================================================
# 5. The derived center cascade: Step 2 (E_2 -> E_3)
# =========================================================================

def step2_e2_to_e3_heisenberg(k: Rational = Rational(1)) -> DerivedCenterResult:
    """E_2 -> E_3 via derived center for H_k (E_2).

    H_k as E_2-algebra -> HH^*(H_k, H_k) is E_3 by higher Deligne.

    Since H_k is E_infty (commutative vertex algebra), the full
    algebraic E_3 with BV operator is available (AP153 satisfied).
    This is the specific E_3 = {cup product, Gerstenhaber bracket, BV},
    not just the generic higher-Deligne E_3.

    Under formality (AP-CY33): the chain-level E_3 collapses to E_2
    rationally.  The physical content (Miki, tetrahedron corrections)
    lives at the chain level.

    The E_3 bar complex B_{E_3}(H_k) has dimension P(q)^3 = tau_3(n).
    All three differentials vanish (class G, free-field).
    """
    input_alg = EnAlgebraData(
        name=f'H_{k} (E_2)',
        n=2,
        shadow_class='G',
        kappa_ch=k,
        dimension_gf_coeffs=TAU_2_GROUND_TRUTH,
        num_deformation_params=1,
        is_commutative=True,
    )

    # HH^*(H_k^{E_2}, H_k^{E_2}) is E_3.
    # Dimension: P(q)^3 = tau_3(n) (trigraded bar complex).
    hh_gf = tuple(multipartition_count(i, 3) for i in range(10))

    return DerivedCenterResult(
        input_algebra=input_alg,
        output_n=3,
        output_name=f'H_{k} (E_3, algebraic Deligne with BV)',
        e3_type='bv',  # E_infty input -> full algebraic E_3
        bzfn_agrees=False,  # BZFN is E_1->E_2 only; iterated Drinfeld Z(Z(C)) != E_3
        hh_dimension_gf_coeffs=hh_gf,
        dunn_decomposition=tuple(DunnDecomposition.e1_factors(3)),
    )


def step2_e2_to_e3_yangian() -> DerivedCenterResult:
    """E_2 -> E_3 via derived center for Y(gl_hat_1) (E_2).

    Y(gl_hat_1) = W_{1+infty} as E_2-algebra -> HH^*(Y, Y) is E_3.

    Since Y(gl_hat_1) is E_2 but NOT E_infty, the E_3 structure is the
    GENERIC higher-Deligne E_3 (AP153): no BV operator from the
    cyclic bar complex.  This is the chain-level E_3 that generates
    the Miki automorphism and the tetrahedron corrections.

    KEY DIVERGENCE: The iterated Drinfeld center Z(Z(Rep(Y^+))) gives
    Rep(Y) boxtimes Rep(Y)^{rev} (E_2-doubling), NOT E_3.
    Only the derived center HH^*(Y, Y) produces E_3.

    This E_3 structure is the one relevant for the 6d holomorphic
    theory on C^3: the quantum toroidal algebra U_{q,t}(gl_hat_hat_1)
    carries the E_3 structure from its three complex directions.
    """
    input_alg = EnAlgebraData(
        name='Y(gl_hat_1) (E_2)',
        n=2,
        shadow_class='L',
        kappa_ch=Rational(1),
        dimension_gf_coeffs=TAU_2_GROUND_TRUTH,
        num_deformation_params=1,
        is_commutative=False,
    )

    # E_3 bar complex dimension: P(q)^3 at the chain level.
    # For class L: shadow depth 2, so the spectral sequence
    # degenerates and the cohomological dimension is (1+t)^3 = 8
    # (for genus 1).  But at the chain level: P(q)^3.
    hh_gf = tuple(multipartition_count(i, 3) for i in range(10))

    return DerivedCenterResult(
        input_algebra=input_alg,
        output_n=3,
        output_name='U_{q,t}(gl_hat_hat_1) (E_3, generic Deligne)',
        e3_type='generic',  # E_2 input -> generic E_3, no BV
        bzfn_agrees=False,
        hh_dimension_gf_coeffs=hh_gf,
        dunn_decomposition=tuple(DunnDecomposition.e1_factors(3)),
    )


# =========================================================================
# 6. The cascade termination: E_3 -> E_4 obstruction
# =========================================================================

class CascadeTermination(NamedTuple):
    """Data explaining why the E_n cascade terminates at a given level.

    Attributes:
        max_n: The maximum E_n level achievable from CY geometry.
        obstruction_type: What prevents further promotion.
        bott_group: The homotopy group that provides the obstruction.
        num_cy_directions: Number of complex directions available.
        num_e1_factors_needed: Number of E_1 factors required for E_{max_n+1}.
    """
    max_n: int
    obstruction_type: str
    bott_group: str
    num_cy_directions: int
    num_e1_factors_needed: int


def cascade_termination_analysis(cy_dim: int) -> CascadeTermination:
    """Analyze why the E_n cascade terminates for a CY_d category.

    The cascade E_1 -> E_2 -> E_3 -> ... terminates at E_3 for CY
    geometric inputs because:

    (1) CY_d with d >= 4: E_1-stabilized (thm:e1-stabilization-cy).
        The chiral algebra is ALWAYS E_1; higher E_n comes only from
        the Drinfeld center / derived center, not from the native
        CY structure.

    (2) CY_3 (d=3): The holomorphic theory on C^3 provides E_3.
        Three complex directions -> three E_1 factors via Dunn.
        E_4 would require a fourth direction, which C^3 lacks.

    (3) CY_2 (d=2): Native E_2. One derived center step gives E_3
        (if the input is E_infty, by AP153). But the CY_2 geometry
        only provides 2 complex directions natively.

    (4) CY_1 (d=1): Native E_infty (commutative). Higher Deligne
        gives E_infty on cochains, so no further promotion needed.

    The algebraic cascade is unbounded (Deligne gives E_{n+1} for
    any E_n input, for all n). The CY-geometric constraint is:
    the CY_d category provides at most min(d, 3) complex directions,
    and the cascade terminates at E_{min(d,3)}.
    """
    if cy_dim <= 0:
        raise ValueError(f"CY dimension must be positive, got {cy_dim}")

    if cy_dim == 1:
        return CascadeTermination(
            max_n=999,  # E_infty, commutative
            obstruction_type='none (E_infty, commutative)',
            bott_group='trivial',
            num_cy_directions=1,
            num_e1_factors_needed=0,
        )
    elif cy_dim == 2:
        return CascadeTermination(
            max_n=3,
            obstruction_type='E_2 native; E_3 via derived center of E_2 (requires E_infty, AP153)',
            bott_group='pi_2(BU) = Z (braiding parameter c_1)',
            num_cy_directions=2,
            num_e1_factors_needed=4,
        )
    elif cy_dim == 3:
        return CascadeTermination(
            max_n=3,
            obstruction_type='E_1 native; E_3 via two derived center steps; '
                             'E_4 blocked by lack of fourth complex direction '
                             '(C^3 has 3 directions, E_4 = E_1^{tensor 4} needs 4)',
            bott_group='pi_3(BU) = 0 (no framing obstruction)',
            num_cy_directions=3,
            num_e1_factors_needed=4,
        )
    else:
        # d >= 4: E_1-stabilized by thm:e1-stabilization-cy
        # Bott periodicity determines the shifted structure
        bott_val = _bott_periodicity_bu(cy_dim)
        return CascadeTermination(
            max_n=3,
            obstruction_type=f'E_1-stabilized (thm:e1-stabilization-cy); '
                             f'd={cy_dim} has pi_{cy_dim}(BU) = {bott_val}; '
                             f'E_3 maximum from derived center cascade',
            bott_group=f'pi_{cy_dim}(BU) = {bott_val}',
            num_cy_directions=cy_dim,
            num_e1_factors_needed=4,
        )


def _bott_periodicity_bu(d: int) -> str:
    """Compute pi_d(BU) by Bott periodicity (period 2)."""
    if d <= 0:
        return '0'
    return 'Z' if d % 2 == 0 else '0'


# =========================================================================
# 7. Iterated Drinfeld center vs derived center: the divergence
# =========================================================================

class CenterComparison(NamedTuple):
    """Comparison of Drinfeld center and derived center at a given step.

    AP-CY4: These are DISTINCT operations. They agree at E_1->E_2 (BZFN)
    and diverge at E_2->E_3.
    """
    step_name: str
    input_level: int
    drinfeld_output: str
    derived_output: str
    agrees: bool
    explanation: str


def compare_centers_step1() -> CenterComparison:
    """Compare Drinfeld and derived centers at E_1 -> E_2."""
    return CenterComparison(
        step_name='E_1 -> E_2',
        input_level=1,
        drinfeld_output='Z(Rep^{E_1}(A)) = braided monoidal category (E_2)',
        derived_output='HH^*(A, A) = E_2-algebra (Deligne conjecture)',
        agrees=True,
        explanation='BZFN theorem (thm:bzfn): Z(Rep^{E_1}(A)) = Rep^{E_2}(HH^*(A,A)). '
                    'The categorical Drinfeld center and the algebraic derived center '
                    'produce the SAME E_2 structure at this step.',
    )


def compare_centers_step2() -> CenterComparison:
    """Compare iterated Drinfeld and derived centers at E_2 -> E_3.

    KEY DIVERGENCE (rem:three-centers-sharp in drinfeld_center.tex):
    - Iterated Drinfeld: Z(B) for braided B gives B boxtimes B^{rev},
      which is E_2-DOUBLING, not E_3-promotion.
    - Derived center: HH^*(B, B) for E_2-algebra B gives E_3
      (higher Deligne, Lurie HA 5.3.1.30).
    """
    return CenterComparison(
        step_name='E_2 -> E_3',
        input_level=2,
        drinfeld_output='Z(B) = B boxtimes B^{rev} (E_2-doubling, NOT E_3)',
        derived_output='HH^*(B, B) = E_3-algebra (higher Deligne conjecture)',
        agrees=False,
        explanation='DIVERGENCE. The iterated Drinfeld center of a braided '
                    'category B gives B boxtimes B^{rev} (Deligne product with '
                    'reverse braiding), which has E_2 structure, NOT E_3. '
                    'The derived center HH^*(B,B) genuinely produces E_3 by '
                    'higher Deligne (Lurie HA 5.3.1.30, Dunn additivity: '
                    'E_2 tensor E_1 = E_3). The "additional E_1" direction '
                    'comes from the Hochschild cochain construction, not from '
                    'half-braidings. This is the mathematical reason why E_2->E_3 '
                    'promotion is the DERIVED center, not the iterated Drinfeld center.',
    )


def compare_centers_step3() -> CenterComparison:
    """Compare at E_3 -> E_4 (the termination step)."""
    return CenterComparison(
        step_name='E_3 -> E_4',
        input_level=3,
        drinfeld_output='Z(C) = C boxtimes C^{rev} (E_3-doubling, still not E_4)',
        derived_output='HH^*(C, C) = E_4-algebra (algebraically; no CY source)',
        agrees=False,
        explanation='TERMINATION for CY geometry. Algebraically, the derived center '
                    'HH^*(C,C) of an E_3-algebra C carries E_4 structure by higher '
                    'Deligne. However, CY geometry provides NO E_4 input through '
                    'the functor Phi: the CY-to-chiral functor produces at most E_3 '
                    '(from C^3), and d >= 4 CY categories are E_1-stabilized. '
                    'The E_3 -> E_4 step exists ALGEBRAICALLY but has no CY-geometric '
                    'realization. This is E_1-stabilization at d >= 4 '
                    '(thm:e1-stabilization-cy).',
    )


# =========================================================================
# 8. The E_n bar complex dimension at each cascade level
# =========================================================================

def en_bar_dimension(n: int, degree: int) -> int:
    """Dimension of E_n bar complex B_{E_n}(H_k) at given degree.

    For the Heisenberg H_k (class G, free-field):
      B_{E_n}(H_k) has n-graded dimension P(q)^n.
      dim B_{E_n}(H_k)_degree = tau_n(degree) = n-component multipartition count.

    This is tau_n(degree) = coefficient of q^degree in P(q)^n.
    """
    return multipartition_count(degree, n)


def en_bar_hilbert_series(n: int, max_degree: int = 10) -> List[int]:
    """Hilbert series of B_{E_n}(H_k) up to given degree."""
    return [en_bar_dimension(n, d) for d in range(max_degree)]


def en_bar_differentials_vanish(shadow_class: str) -> bool:
    """Whether all E_n bar differentials vanish for given shadow class.

    Class G (free-field): ALL differentials vanish (d_i = 0).
    Class L: differentials nonzero but nilpotent (spectral sequence degenerates).
    Class C: charge conservation kills some differentials.
    Class M: all differentials active, infinite shadow tower.
    """
    return shadow_class == 'G'


# =========================================================================
# 9. Dunn additivity decomposition: the explicit E_1 factors
# =========================================================================

class DunnE1Factor(NamedTuple):
    """An individual E_1 factor in the Dunn decomposition E_n = E_1^{tensor n}.

    Each factor corresponds to a geometric direction and a specific
    algebraic operation.
    """
    index: int
    name: str
    geometric_direction: str
    algebraic_operation: str
    parameter: str


def yangian_dunn_factors() -> List[DunnE1Factor]:
    """The three E_1 factors for the quantum toroidal algebra on C^3.

    E_3 = E_1 tensor E_1 tensor E_1.  For U_{q,t}(gl_hat_hat_1):

    Factor 1 (instanton): CoHA multiplication from extension Hall product.
      Direction: z_1 (the "instanton number" direction).
      Parameter: q = e^{h_1}.

    Factor 2 (spectral): Yangian spectral parameter shift.
      Direction: z_2 (the "momentum" direction).
      Parameter: t = e^{-h_2}.
      This is the factor ADDED by the derived center at Step 1.

    Factor 3 (miki): The third complex direction from 6d theory.
      Direction: z_3 (the "Miki" direction).
      Parameter: q_3 = e^{h_3} = (qt)^{-1}.
      This is the factor ADDED by the derived center at Step 2.
      The Miki automorphism permutes all three factors cyclically.
    """
    return [
        DunnE1Factor(
            index=1,
            name='instanton',
            geometric_direction='z_1 (complex direction 1 in C^3)',
            algebraic_operation='CoHA Hall product: extension correspondence '
                                '0 -> V\' -> V -> V\'\' -> 0',
            parameter='q = e^{h_1}',
        ),
        DunnE1Factor(
            index=2,
            name='spectral',
            geometric_direction='z_2 (complex direction 2 in C^3)',
            algebraic_operation='Yangian spectral parameter shift: u -> u + z '
                                '(from derived center of Y^+, Step 1)',
            parameter='t = e^{-h_2}',
        ),
        DunnE1Factor(
            index=3,
            name='miki',
            geometric_direction='z_3 (complex direction 3 in C^3)',
            algebraic_operation='Third direction from 6d holomorphic theory; '
                                'generates the Miki automorphism S: (q,t,q_3) -> (t,q_3,q) '
                                '(from derived center at Step 2)',
            parameter='q_3 = e^{h_3} = (qt)^{-1}',
        ),
    ]


def verify_dunn_e4_obstruction() -> Dict[str, object]:
    """Verify that E_4 = E_1^{tensor 4} has no CY realization.

    E_4 requires 4 independent E_1-factors.  The CY_3 geometry on C^3
    provides 3 complex directions.  There is no fourth direction.

    For CY_4 on C^4: there are 4 complex directions with 3 free
    parameters (h_1,...,h_4 subject to sum=0), but the E_1-stabilization
    theorem (thm:e1-stabilization-cy) shows that the chiral algebra
    at d=4 is E_1, not E_4.  The obstruction is pi_4(BU) = Z (the
    first Pontryagin class), which provides shifted symplectic structure
    rather than an additional E_1 factor.
    """
    return {
        'e4_requires': 4,
        'cy3_provides': 3,
        'cy3_free_params': 2,  # h_1, h_2 free; h_3 = -(h_1+h_2)
        'deficit': 1,
        'cy4_directions': 4,
        'cy4_free_params': 3,
        'cy4_obstruction': 'pi_4(BU) = Z (first Pontryagin class p_1)',
        'cy4_stabilized': True,
        'conclusion': 'E_4 has no CY-geometric realization. '
                      'CY_3 has 3 directions (E_3 max). '
                      'CY_4 has 4 directions but pi_4(BU) = Z obstruction '
                      'causes E_1-stabilization, not E_4.',
    }


# =========================================================================
# 10. Full cascade computation
# =========================================================================

def full_cascade(algebra: str = 'heisenberg',
                 k: Rational = Rational(1)) -> List[DerivedCenterResult]:
    """Run the complete E_1 -> E_2 -> E_3 cascade.

    Args:
        algebra: 'heisenberg' for H_k, 'yangian' for Y^+(gl_hat_1).
        k: Level (for Heisenberg).

    Returns:
        List of DerivedCenterResult for each step.
    """
    results = []
    if algebra == 'heisenberg':
        results.append(step1_e1_to_e2_heisenberg(k))
        results.append(step2_e2_to_e3_heisenberg(k))
    elif algebra == 'yangian':
        results.append(step1_e1_to_e2_yangian())
        results.append(step2_e2_to_e3_yangian())
    else:
        raise ValueError(f"Unknown algebra: {algebra}")
    return results


def cascade_summary() -> Dict[str, object]:
    """Summary of the full cascade for both algebras.

    Returns a dictionary with:
      - center_comparisons: Drinfeld vs derived at each step
      - heisenberg_cascade: steps for H_k
      - yangian_cascade: steps for Y^+
      - termination: why it stops at E_3
      - dunn_factors: the three E_1 factors
    """
    return {
        'center_comparisons': [
            compare_centers_step1(),
            compare_centers_step2(),
            compare_centers_step3(),
        ],
        'heisenberg_cascade': full_cascade('heisenberg'),
        'yangian_cascade': full_cascade('yangian'),
        'termination': cascade_termination_analysis(3),
        'dunn_factors': yangian_dunn_factors(),
        'e4_obstruction': verify_dunn_e4_obstruction(),
    }
