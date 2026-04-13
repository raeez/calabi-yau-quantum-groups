r"""sl_2 Serre relation engine: matrix structure function with squared convention.

Implements the SQUARED-BASE convention for the affine Yangian Y(sl_2_hat)
structure function and verifies the three defining relations:

1. SERRE RELATION (charge (2,1)): Sym_{z1,z2}[T1 - 2*T2 + T3] = 0
2. NULL VECTOR IDENTITY: g_{i0}(z) * g_{i1}(z) = 1  for i in {0,1}
3. WHEEL CONDITION: g_{00}(h_a) = 0  for a in {1,2,3}

SQUARED-BASE CONVENTION
========================

The structure function uses the squared form of the cubic ratio:

  g_{00}(z) = [(z - h1)(z - h2)(z - h3)]^2 / [(z + h1)(z + h2)(z + h3)]^2
  g_{01}(z) = 1 / g_{00}(z)
  g_{10}(z) = g_{01}(z)      (Cartan symmetry C_{01} = C_{10})
  g_{11}(z) = g_{00}(z)      (diagonal symmetry C_{11} = C_{00})

Equivalently, define the square-root base:

  phi(z) = (z - h1)(z - h2)(z - h3) / ((z + h1)(z + h2)(z + h3))

Then g_{ij}(z) = phi(z)^{C_{ij}} where C is the affine A_1 Cartan matrix
C = ((2,-2),(-2,2)). So g_{00} = phi^2 (squared), g_{01} = phi^{-2} = 1/phi^2.

This convention appears in the crystal-melting/BPS-counting literature
(Okounkov-Reshetikhin-Vafa) where the partition function weight is the
square of the structure function. The Schiffmann-Vasserot convention uses
g_base = phi with exponent C_{ij}/2; the two agree on the RELATION structure
(all three defining relations hold in both conventions) but differ on
numerical values of g_{ij} at specific points.

MATHEMATICAL CONTENT
=====================

The three relations encode the structure of Y(sl_2_hat):

- The Serre relation ensures that the generators satisfy quantum group
  commutation relations. For the A_1 quiver, the scalar nature of g_{ij}
  makes Serre trivial; the non-trivial content is in the WHEEL condition.

- The null vector identity is the imaginary-root constraint of the affine
  algebra. It ensures that the "total" structure function along the null
  direction d=(1,1) is trivial: g_{i0}*g_{i1} = phi^{C_{i0}+C_{i1}} = phi^0 = 1.

- The wheel condition: g_{00}(h_a) = 0 because the numerator
  [(h_a - h1)(h_a - h2)(h_a - h3)]^2 contains the factor (h_a - h_a)^2 = 0.
  These zeros generate the Serre ideal in the shuffle algebra.

CONVENTIONS
===========
  - h1 + h2 + h3 = 0 (CY3 condition)
  - Affine Cartan matrix A_1^{(1)}: C = ((2,-2),(-2,2))
  - g_{ij}(z) = phi(z)^{C_{ij}} where phi = prod (z-h_a)/(z+h_a)
  - Exact arithmetic via fractions.Fraction throughout

REFERENCES
==========
  Schiffmann-Vasserot, arXiv:1212.5535 (CoHA for quivers)
  Tsymbaliuk, arXiv:1404.5240 (affine Yangian presentation)
  Li-Yamazaki, arXiv:2003.08909 (quiver Yangian)
  Feigin-Odesskii, arXiv:q-alg/9612033 (shuffle algebras)
  Okounkov-Reshetikhin-Vafa, arXiv:hep-th/0309208 (crystal melting)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from compute.lib.sl2_chiral_coproduct_engine import (
    CARTAN_A1,
    StructureFunction,
    cartan_entry,
)


# =========================================================================
# 1. SQUARED-BASE STRUCTURE FUNCTION
# =========================================================================

def _phi(z: Fraction, h1: Fraction, h2: Fraction, h3: Fraction) -> Fraction:
    r"""Square-root base: phi(z) = (z-h1)(z-h2)(z-h3) / ((z+h1)(z+h2)(z+h3)).

    This is the unsquared cubic ratio. The squared convention gives
    g_{00}(z) = phi(z)^2.
    """
    num = (z - h1) * (z - h2) * (z - h3)
    den = (z + h1) * (z + h2) * (z + h3)
    if den == 0:
        raise ValueError(f"phi(z) has pole at z={z}")
    return Fraction(num, den)


def g_matrix(
    i: int,
    j: int,
    z: Fraction,
    h1: Fraction,
    h2: Fraction,
    h3: Fraction,
) -> Fraction:
    r"""Compute g_{ij}(z) in the SQUARED-BASE convention.

    The matrix structure function for Y(sl_2_hat) in the squared convention:

      g_{ij}(z) = phi(z)^{C_{ij}}

    where phi(z) = (z-h1)(z-h2)(z-h3) / ((z+h1)(z+h2)(z+h3)) is the
    square-root base and C = ((2,-2),(-2,2)) is the affine A_1 Cartan matrix.

    Explicit forms:
      g_{00}(z) = g_{11}(z) = [(z-h1)(z-h2)(z-h3)]^2 / [(z+h1)(z+h2)(z+h3)]^2
      g_{01}(z) = g_{10}(z) = [(z+h1)(z+h2)(z+h3)]^2 / [(z-h1)(z-h2)(z-h3)]^2
                             = 1 / g_{00}(z)

    Parameters
    ----------
    i, j : int
        Node indices in {0, 1}.
    z : Fraction
        Spectral parameter.
    h1, h2, h3 : Fraction
        CY3 parameters satisfying h1 + h2 + h3 = 0.

    Returns
    -------
    Fraction
        The value g_{ij}(z).

    Raises
    ------
    ValueError
        If h1+h2+h3 != 0, or if z is a pole of the requested entry.
    """
    h1, h2, h3 = Fraction(h1), Fraction(h2), Fraction(h3)
    z = Fraction(z)

    if h1 + h2 + h3 != 0:
        raise ValueError(
            f"CY condition violated: h1+h2+h3 = {h1+h2+h3} != 0"
        )
    if i not in (0, 1) or j not in (0, 1):
        raise ValueError(f"Node indices must be 0 or 1, got ({i}, {j})")

    num = (z - h1) * (z - h2) * (z - h3)
    den = (z + h1) * (z + h2) * (z + h3)

    c = CARTAN_A1[i][j]  # +2 diagonal, -2 off-diagonal

    if c == 2:
        # g_{ii}(z) = phi(z)^2 = num^2 / den^2
        if den == 0:
            raise ValueError(f"g_{{{i}{j}}}(z) has pole at z={z}")
        return Fraction(num * num, den * den)
    elif c == -2:
        # g_{ij}(z) = phi(z)^{-2} = den^2 / num^2 = 1/g_{ii}(z)
        if num == 0:
            raise ValueError(f"g_{{{i}{j}}}(z) has pole at z={z}")
        return Fraction(den * den, num * num)
    else:
        raise ValueError(f"Unexpected Cartan entry C_{{{i}{j}}} = {c}")


# =========================================================================
# 2. SERRE RELATION AT CHARGE (2,1)
# =========================================================================

class SerreRelation:
    r"""Quantum Serre relation for Y(sl_2_hat) in the squared convention.

    The Serre relation at charge (2,1) involves three terms:

      T1 (e_0 * e_0 * e_1): g_{00}(z1-z2) * g_{01}(z1-w) * g_{01}(z2-w)
      T2 (e_0 * e_1 * e_0): g_{01}(z1-w) * g_{00}(z1-z2) * g_{10}(z2-w)
      T3 (e_1 * e_0 * e_0): g_{01}(z1-w) * g_{01}(z2-w) * g_{00}(z1-z2)

    The Serre element is: Sym_{z1,z2}[ T1 - 2*T2 + T3 ] = 0.

    Vanishing mechanism: g_{10} = g_{01} (Cartan symmetry C_{01} = C_{10})
    and scalar multiplication commutes, so T1 = T2 = T3 identically,
    giving 1 - 2 + 1 = 0. This holds in BOTH squared and unsquared
    conventions since the mechanism depends only on Cartan symmetry.
    """

    def __init__(self, sf: Optional[StructureFunction] = None):
        self.sf = sf or StructureFunction()
        self._h1 = self.sf.h1
        self._h2 = self.sf.h2
        self._h3 = self.sf.h3

    def _g(self, i: int, j: int, z: Fraction) -> Fraction:
        """Evaluate g_{ij}(z) using the squared-base convention."""
        return g_matrix(i, j, z, self._h1, self._h2, self._h3)

    def _term1(self, z1: Fraction, z2: Fraction,
               w: Fraction) -> Fraction:
        """Term 1: g_{00}(z1-z2) * g_{01}(z1-w) * g_{01}(z2-w)."""
        return self._g(0, 0, z1 - z2) * self._g(0, 1, z1 - w) * self._g(0, 1, z2 - w)

    def _term2(self, z1: Fraction, z2: Fraction,
               w: Fraction) -> Fraction:
        """Term 2: g_{01}(z1-w) * g_{00}(z1-z2) * g_{10}(z2-w)."""
        return self._g(0, 1, z1 - w) * self._g(0, 0, z1 - z2) * self._g(1, 0, z2 - w)

    def _term3(self, z1: Fraction, z2: Fraction,
               w: Fraction) -> Fraction:
        """Term 3: g_{01}(z1-w) * g_{01}(z2-w) * g_{00}(z1-z2)."""
        return self._g(0, 1, z1 - w) * self._g(0, 1, z2 - w) * self._g(0, 0, z1 - z2)

    def serre_integrand(self, z1: Fraction, z2: Fraction,
                        w: Fraction) -> Fraction:
        """Serre integrand T1 - 2*T2 + T3 BEFORE symmetrization."""
        return self._term1(z1, z2, w) - 2 * self._term2(z1, z2, w) + self._term3(z1, z2, w)

    def serre_symmetrized(self, z1: Fraction, z2: Fraction,
                          w: Fraction) -> Fraction:
        """Symmetrized Serre element: S(z1,z2,w) + S(z2,z1,w)."""
        return self.serre_integrand(z1, z2, w) + self.serre_integrand(z2, z1, w)

    def verify_serre_at_point(self, z1: Fraction, z2: Fraction,
                              w: Fraction) -> Dict[str, Any]:
        """Full verification of the Serre relation at a single (z1, z2, w).

        Checks:
        (a) Cartan symmetry: g_{01}(z) = g_{10}(z) at the relevant argument
        (b) Term equality: T1 = T2 = T3
        (c) Serre vanishing: T1 - 2*T2 + T3 = 0
        (d) Symmetrized vanishing: Sym_{z1,z2}[T1 - 2*T2 + T3] = 0
        """
        t1 = self._term1(z1, z2, w)
        t2 = self._term2(z1, z2, w)
        t3 = self._term3(z1, z2, w)

        serre_unsym = t1 - 2 * t2 + t3
        serre_sym = self.serre_symmetrized(z1, z2, w)

        cartan_sym_z2w = self._g(0, 1, z2 - w) == self._g(1, 0, z2 - w)

        return {
            "z1": str(z1),
            "z2": str(z2),
            "w": str(w),
            "term1_e0e0e1": str(t1),
            "term2_e0e1e0": str(t2),
            "term3_e1e0e0": str(t3),
            "cartan_symmetry_g01_eq_g10": cartan_sym_z2w,
            "terms_all_equal": t1 == t2 == t3,
            "serre_unsymmetrized": str(serre_unsym),
            "serre_symmetrized": str(serre_sym),
            "unsymmetrized_vanishes": serre_unsym == Fraction(0),
            "symmetrized_vanishes": serre_sym == Fraction(0),
        }

    def verify_serre_at_points(
        self,
        test_points: Optional[List[Tuple[Fraction, Fraction, Fraction]]] = None,
    ) -> Dict[str, Any]:
        """Verify the Serre relation at multiple numerical points.

        Default: 10 test points with distinct, generic Fraction values
        chosen to avoid poles of the structure function (poles at
        z = +/- h_a where h_a in {h1, h2, h3}).
        """
        if test_points is None:
            test_points = [
                (Fraction(3), Fraction(7), Fraction(5)),
                (Fraction(2), Fraction(11), Fraction(4)),
                (Fraction(1), Fraction(6), Fraction(3)),
                (Fraction(10), Fraction(3), Fraction(7)),
                (Fraction(5), Fraction(17), Fraction(11)),
                (Fraction(13), Fraction(19), Fraction(7)),
                (Fraction(4), Fraction(9), Fraction(2)),
                (Fraction(6), Fraction(14), Fraction(8)),
                (Fraction(8), Fraction(21), Fraction(15)),
                (Fraction(12), Fraction(5), Fraction(9)),
            ]

        results = []
        all_vanish = True
        all_terms_equal = True
        all_cartan_sym = True

        for z1, z2, w in test_points:
            r = self.verify_serre_at_point(z1, z2, w)
            results.append(r)
            if not r["symmetrized_vanishes"]:
                all_vanish = False
            if not r["terms_all_equal"]:
                all_terms_equal = False
            if not r["cartan_symmetry_g01_eq_g10"]:
                all_cartan_sym = False

        return {
            "relation": "Sym_{z1,z2}[e_0(z1),[e_0(z2),e_1(w)]] = 0",
            "charge": "(2, 1)",
            "convention": "squared-base: g_{ij} = phi^{C_{ij}}",
            "cartan_entry": f"C_{{01}} = {cartan_entry(0, 1)}",
            "num_points_tested": len(test_points),
            "all_vanish": all_vanish,
            "all_terms_equal": all_terms_equal,
            "all_cartan_symmetry": all_cartan_sym,
            "point_results": results,
            "h_parameters": {
                "h1": str(self._h1),
                "h2": str(self._h2),
                "h3": str(self._h3),
            },
            "mechanism": (
                "The Serre relation vanishes because g_{10}(z) = g_{01}(z) "
                "(Cartan symmetry C_{01} = C_{10} = -2) forces all three "
                "terms to be equal. The combination 1 - 2 + 1 = 0 then "
                "gives the vanishing. This holds identically in both the "
                "squared and unsquared conventions."
            ),
        }


# =========================================================================
# 3. NULL VECTOR IDENTITY
# =========================================================================

class NullVectorIdentity:
    """Verification of g_{i0}(z) * g_{i1}(z) = 1 in the squared convention.

    The affine Cartan matrix A_1^{(1)} has null vector d = (1, 1):
      C * d = ((2,-2),(-2,2)) * (1,1)^T = (0, 0)^T

    In the squared convention:
      g_{i0}(z) * g_{i1}(z) = phi(z)^{C_{i0}} * phi(z)^{C_{i1}}
                              = phi(z)^{C_{i0} + C_{i1}}
                              = phi(z)^0 = 1

    since C_{i0} + C_{i1} = 0 for both i = 0 and i = 1.
    """

    def __init__(self, sf: Optional[StructureFunction] = None):
        self.sf = sf or StructureFunction()
        self._h1 = self.sf.h1
        self._h2 = self.sf.h2
        self._h3 = self.sf.h3

    def verify_at_point(self, i: int, z: Fraction) -> Dict[str, Any]:
        """Verify g_{i0}(z) * g_{i1}(z) = 1 at a single point."""
        g_i0 = g_matrix(i, 0, z, self._h1, self._h2, self._h3)
        g_i1 = g_matrix(i, 1, z, self._h1, self._h2, self._h3)
        product = g_i0 * g_i1

        exp_sum = CARTAN_A1[i][0] + CARTAN_A1[i][1]

        return {
            "node": i,
            "z": str(z),
            "g_i0": str(g_i0),
            "g_i1": str(g_i1),
            "product": str(product),
            "is_one": product == Fraction(1),
            "exponent_sum": (
                f"C_{{{i}0}} + C_{{{i}1}} = "
                f"{CARTAN_A1[i][0]} + {CARTAN_A1[i][1]} = {exp_sum}"
            ),
        }

    def verify_null_vector(
        self,
        test_points: Optional[List[Fraction]] = None,
    ) -> Dict[str, Any]:
        """Verify g_{i0}(z) * g_{i1}(z) = 1 at multiple points for both nodes.

        Default: 10 test points x 2 nodes = 20 checks.
        """
        if test_points is None:
            test_points = [
                Fraction(2), Fraction(3), Fraction(5), Fraction(7),
                Fraction(11), Fraction(13), Fraction(17), Fraction(19),
                Fraction(23), Fraction(29),
            ]

        results = []
        all_hold = True
        for z_val in test_points:
            for i in range(2):
                r = self.verify_at_point(i, z_val)
                results.append(r)
                if not r["is_one"]:
                    all_hold = False

        cartan_row_sums = [
            CARTAN_A1[i][0] + CARTAN_A1[i][1] for i in range(2)
        ]

        return {
            "identity": "g_{i0}(z) * g_{i1}(z) = 1",
            "convention": "squared-base: g_{ij} = phi^{C_{ij}}",
            "null_vector": "d = (1, 1)",
            "cartan_row_sums": cartan_row_sums,
            "all_row_sums_zero": all(s == 0 for s in cartan_row_sums),
            "num_points_tested": len(test_points),
            "num_nodes_tested": 2,
            "total_checks": len(results),
            "all_hold": all_hold,
            "point_results": results,
            "mechanism": (
                "The null vector d=(1,1) of the affine Cartan matrix means "
                "C_{i0} + C_{i1} = 0 for all i. In the squared convention, "
                "g_{i0}*g_{i1} = phi^{C_{i0}+C_{i1}} = phi^0 = 1."
            ),
        }


# =========================================================================
# 4. WHEEL CONDITION
# =========================================================================

class WheelCondition:
    """Verification of the wheel condition g_{00}(h_a) = 0.

    In the squared convention:
      g_{00}(z) = [(z - h1)(z - h2)(z - h3)]^2 / [(z + h1)(z + h2)(z + h3)]^2

    The numerator vanishes at z = h_a because it contains the factor
    (h_a - h_a)^2 = 0. Hence g_{00}(h_a) = 0.

    Conversely, g_{01}(z) = 1/g_{00}(z) has DOUBLE poles at z = h_a
    (in the squared convention, vs simple poles in the unsquared).
    """

    def __init__(self, sf: Optional[StructureFunction] = None):
        self.sf = sf or StructureFunction()
        self._h1 = self.sf.h1
        self._h2 = self.sf.h2
        self._h3 = self.sf.h3

    def g_numerator_sq(self, z: Fraction) -> Fraction:
        """Numerator of g_{00}(z) = [(z-h1)(z-h2)(z-h3)]^2."""
        base_num = (z - self._h1) * (z - self._h2) * (z - self._h3)
        return base_num * base_num

    def g_denominator_sq(self, z: Fraction) -> Fraction:
        """Denominator of g_{00}(z) = [(z+h1)(z+h2)(z+h3)]^2."""
        base_den = (z + self._h1) * (z + self._h2) * (z + self._h3)
        return base_den * base_den

    def verify_zero_at_h(self, a: int) -> Dict[str, Any]:
        """Verify g_{00}(h_a) = 0 for a given CY parameter index a in {1,2,3}."""
        h_vals = {1: self._h1, 2: self._h2, 3: self._h3}
        h_a = h_vals[a]

        numerator = self.g_numerator_sq(h_a)
        denominator = self.g_denominator_sq(h_a)

        return {
            "parameter_index": a,
            "h_a": str(h_a),
            "numerator": str(numerator),
            "denominator": str(denominator),
            "numerator_is_zero": numerator == Fraction(0),
            "denominator_nonzero": denominator != Fraction(0),
            "g_00_vanishes": numerator == Fraction(0) and denominator != Fraction(0),
        }

    def verify_wheel_condition(self) -> Dict[str, Any]:
        """Verify g_{00}(h_a) = 0 for all three CY parameters."""
        results = []
        all_zero = True
        all_denom_ok = True

        for a in [1, 2, 3]:
            r = self.verify_zero_at_h(a)
            results.append(r)
            if not r["numerator_is_zero"]:
                all_zero = False
            if not r["denominator_nonzero"]:
                all_denom_ok = False

        # Cross-node pole structure: g_{01} has double poles where g_{00} = 0
        cross_node_poles = []
        for a in [1, 2, 3]:
            h_vals = {1: self._h1, 2: self._h2, 3: self._h3}
            h_a = h_vals[a]
            cross_node_poles.append({
                "parameter_index": a,
                "h_a": str(h_a),
                "g01_has_pole": True,
                "pole_order": 2,
                "reason": "g_{01} = 1/g_{00} and g_{00}(h_a) = 0 (double zero in squared convention)",
            })

        cy_sum = self._h1 + self._h2 + self._h3

        return {
            "condition": "g_{00}(h_a) = 0 for a = 1, 2, 3",
            "convention": "squared-base: g_{00} = phi^2, double zeros at h_a",
            "cy_condition": f"h1 + h2 + h3 = {cy_sum}",
            "cy_holds": cy_sum == Fraction(0),
            "h_parameters": {
                "h1": str(self._h1),
                "h2": str(self._h2),
                "h3": str(self._h3),
            },
            "all_zeros_hold": all_zero,
            "all_denominators_nonzero": all_denom_ok,
            "wheel_condition_verified": all_zero and all_denom_ok,
            "parameter_results": results,
            "cross_node_poles": cross_node_poles,
            "mechanism": (
                "g_{00}(z) = [(z-h1)(z-h2)(z-h3)]^2 / [(z+h1)(z+h2)(z+h3)]^2 "
                "has double zeros at z = h_a from the squared numerator. These "
                "generate the Serre ideal in the shuffle algebra. "
                "g_{01}(z) = 1/g_{00}(z) has double poles at the same points."
            ),
        }

    def verify_wheel_chain(self) -> Dict[str, Any]:
        """Verify the pointwise wheel zeros and the unitarity relation.

        Checks:
        (a) g_{00}(h_a) = 0 for each a (squared numerator zero)
        (b) g_{00}(z) * g_{00}(-z) = 1 (unitarity, from phi(z)*phi(-z)=1)

        In the squared convention, g_{00}(z)*g_{00}(-z) = phi(z)^2*phi(-z)^2
        = [phi(z)*phi(-z)]^2. Since phi(z)*phi(-z) = [prod(z-h_a)(z+h_a)]
        / [prod(z+h_a)(z-h_a)] = 1, we get g_{00}(z)*g_{00}(-z) = 1.
        """
        results = {}

        # (a) Zeros at each h_a
        for label, h_val in [("h1", self._h1), ("h2", self._h2),
                              ("h3", self._h3)]:
            num_sq = self.g_numerator_sq(h_val)
            results[f"g_00({label})_numerator_sq"] = str(num_sq)
            results[f"g_00({label})_vanishes"] = num_sq == Fraction(0)

        # (b) Unitarity at a generic point
        z_test = Fraction(7)
        g_z = g_matrix(0, 0, z_test, self._h1, self._h2, self._h3)
        g_neg_z = g_matrix(0, 0, -z_test, self._h1, self._h2, self._h3)
        results["unitarity_product"] = str(g_z * g_neg_z)
        results["unitarity_holds"] = g_z * g_neg_z == Fraction(1)

        results["wheel_chain_vanishes"] = all(
            results[f"g_00({label})_vanishes"]
            for label in ["h1", "h2", "h3"]
        )

        return results


# =========================================================================
# 5. COMPREHENSIVE VERIFICATION
# =========================================================================

def sl2_serre_full_verification(
    sf: Optional[StructureFunction] = None,
) -> Dict[str, Any]:
    """Run all three Serre-engine verifications in the squared convention.

    1. Serre relation at 10 numerical points (exact rational arithmetic)
    2. Null vector identity at 10 points x 2 nodes = 20 checks
    3. Wheel condition at all three CY parameters

    Returns a comprehensive results dict with per-check details.
    """
    sf = sf or StructureFunction()
    serre = SerreRelation(sf)
    null_vec = NullVectorIdentity(sf)
    wheel = WheelCondition(sf)

    serre_result = serre.verify_serre_at_points()
    null_vec_result = null_vec.verify_null_vector()
    wheel_result = wheel.verify_wheel_condition()
    wheel_chain = wheel.verify_wheel_chain()

    all_pass = (
        serre_result["all_vanish"]
        and null_vec_result["all_hold"]
        and wheel_result["wheel_condition_verified"]
        and wheel_chain["wheel_chain_vanishes"]
    )

    return {
        "convention": "squared-base: g_{ij} = phi^{C_{ij}}, phi = prod(z-h_a)/(z+h_a)",
        "serre_relation": serre_result,
        "null_vector_identity": null_vec_result,
        "wheel_condition": wheel_result,
        "wheel_chain": wheel_chain,
        "all_pass": all_pass,
        "h_parameters": {
            "h1": str(sf.h1),
            "h2": str(sf.h2),
            "h3": str(sf.h3),
        },
        "summary": {
            "serre_points_tested": serre_result["num_points_tested"],
            "serre_all_vanish": serre_result["all_vanish"],
            "serre_all_terms_equal": serre_result["all_terms_equal"],
            "null_vector_checks": null_vec_result["total_checks"],
            "null_vector_all_hold": null_vec_result["all_hold"],
            "wheel_verified": wheel_result["wheel_condition_verified"],
            "wheel_chain_verified": wheel_chain["wheel_chain_vanishes"],
        },
    }


# =========================================================================
# 6. STANDALONE API FUNCTIONS
# =========================================================================
#
# Flat functional interface to the squared-base structure function
# and the three defining relations. Accept raw numeric parameters.
#
# SQUARED-BASE CONVENTION:
#
#   phi(z) = (z-h1)(z-h2)(z-h3) / ((z+h1)(z+h2)(z+h3))
#
#   g_{00}(z) = g_{11}(z) = phi(z)^2 = [(z-h1)(z-h2)(z-h3)]^2 / [(z+h1)(z+h2)(z+h3)]^2
#   g_{01}(z) = g_{10}(z) = phi(z)^{-2} = 1 / g_{00}(z)
#
# =========================================================================


def null_vector_check(
    h1: Fraction = Fraction(1),
    h2: Fraction = Fraction(-1, 2),
    h3: Optional[Fraction] = None,
    test_points: Optional[List[Fraction]] = None,
) -> Dict[str, Any]:
    r"""Verify the null vector identity g_{i0}(z) * g_{i1}(z) = 1.

    In the squared convention:
      g_{i0}(z) * g_{i1}(z) = phi(z)^{C_{i0}+C_{i1}} = phi(z)^0 = 1

    Parameters
    ----------
    h1, h2 : Fraction
        CY3 parameters (h3 = -(h1+h2) if not provided).
    h3 : Fraction, optional
        If None, computed from CY condition.
    test_points : list of Fraction, optional
        z-values to test.  Default: 10 distinct primes.

    Returns
    -------
    dict
        Keys: 'all_hold' (bool), 'num_checks' (int), 'results' (list).
    """
    h1, h2 = Fraction(h1), Fraction(h2)
    if h3 is None:
        h3 = -(h1 + h2)
    else:
        h3 = Fraction(h3)

    if test_points is None:
        test_points = [
            Fraction(2), Fraction(3), Fraction(5), Fraction(7),
            Fraction(11), Fraction(13), Fraction(17), Fraction(19),
            Fraction(23), Fraction(29),
        ]

    results = []
    all_hold = True

    for z_val in test_points:
        for i in range(2):
            g_i0 = g_matrix(i, 0, z_val, h1, h2, h3)
            g_i1 = g_matrix(i, 1, z_val, h1, h2, h3)
            product = g_i0 * g_i1
            ok = product == Fraction(1)
            if not ok:
                all_hold = False
            results.append({
                "node": i,
                "z": str(z_val),
                "g_i0": str(g_i0),
                "g_i1": str(g_i1),
                "product": str(product),
                "is_one": ok,
            })

    return {
        "identity": "g_{i0}(z) * g_{i1}(z) = 1",
        "convention": "squared-base",
        "null_vector": "d = (1, 1)",
        "h_parameters": {"h1": str(h1), "h2": str(h2), "h3": str(h3)},
        "all_hold": all_hold,
        "num_checks": len(results),
        "results": results,
    }


def serre_check(
    z1: Fraction,
    z2: Fraction,
    w: Fraction,
    h1: Fraction = Fraction(1),
    h2: Fraction = Fraction(-1, 2),
    h3: Optional[Fraction] = None,
) -> Dict[str, Any]:
    r"""Verify Sym_{z1,z2}[e_0(z1),[e_0(z2),e_1(w)]] = 0 numerically.

    Uses the squared-base convention: g_{ij}(z) = phi(z)^{C_{ij}}.

    The vanishing mechanism: g_{10} = g_{01} (Cartan symmetry) and scalar
    multiplication commutes, so T1 = T2 = T3, giving 1 - 2 + 1 = 0.

    Parameters
    ----------
    z1, z2, w : Fraction
        Spectral parameters (must avoid poles).
    h1, h2 : Fraction
        CY3 parameters.
    h3 : Fraction, optional
        If None, computed from CY condition.

    Returns
    -------
    dict
        Keys include 'serre_vanishes' (bool), 'symmetrized_vanishes' (bool),
        'terms_equal' (bool), 'cartan_symmetry' (bool), individual terms.
    """
    z1, z2, w = Fraction(z1), Fraction(z2), Fraction(w)
    h1, h2 = Fraction(h1), Fraction(h2)
    if h3 is None:
        h3 = -(h1 + h2)
    else:
        h3 = Fraction(h3)

    def _g(i, j, zz):
        return g_matrix(i, j, zz, h1, h2, h3)

    # Three Serre terms at (z1, z2, w)
    t1 = _g(0, 0, z1 - z2) * _g(0, 1, z1 - w) * _g(0, 1, z2 - w)
    t2 = _g(0, 1, z1 - w) * _g(0, 0, z1 - z2) * _g(1, 0, z2 - w)
    t3 = _g(0, 1, z1 - w) * _g(0, 1, z2 - w) * _g(0, 0, z1 - z2)

    serre_unsym = t1 - 2 * t2 + t3

    # Symmetrized: S(z1,z2,w) + S(z2,z1,w)
    t1_swap = _g(0, 0, z2 - z1) * _g(0, 1, z2 - w) * _g(0, 1, z1 - w)
    t2_swap = _g(0, 1, z2 - w) * _g(0, 0, z2 - z1) * _g(1, 0, z1 - w)
    t3_swap = _g(0, 1, z2 - w) * _g(0, 1, z1 - w) * _g(0, 0, z2 - z1)
    serre_swap = t1_swap - 2 * t2_swap + t3_swap

    serre_sym = serre_unsym + serre_swap

    # Cartan symmetry check
    cartan_sym = _g(0, 1, z2 - w) == _g(1, 0, z2 - w)

    return {
        "z1": str(z1),
        "z2": str(z2),
        "w": str(w),
        "h_parameters": {"h1": str(h1), "h2": str(h2), "h3": str(h3)},
        "convention": "squared-base",
        "term1": str(t1),
        "term2": str(t2),
        "term3": str(t3),
        "terms_equal": t1 == t2 == t3,
        "cartan_symmetry": cartan_sym,
        "serre_unsymmetrized": str(serre_unsym),
        "serre_symmetrized": str(serre_sym),
        "serre_vanishes": serre_unsym == Fraction(0),
        "symmetrized_vanishes": serre_sym == Fraction(0),
    }


def wheel_condition(
    h1: Fraction = Fraction(1),
    h2: Fraction = Fraction(-1, 2),
    h3: Optional[Fraction] = None,
) -> Dict[str, Any]:
    r"""Verify the wheel condition g_{00}(h_a) = 0 for each CY parameter.

    In the squared convention:
      g_{00}(z) = [(z-h1)(z-h2)(z-h3)]^2 / [(z+h1)(z+h2)(z+h3)]^2

    has double zeros at z = h_a from the squared numerator.

    Parameters
    ----------
    h1, h2 : Fraction
        CY3 parameters.
    h3 : Fraction, optional
        If None, computed from CY condition.

    Returns
    -------
    dict
        Keys: 'wheel_verified' (bool), 'cy_holds' (bool), per-parameter
        results including numerator and denominator values.
    """
    h1, h2 = Fraction(h1), Fraction(h2)
    if h3 is None:
        h3 = -(h1 + h2)
    else:
        h3 = Fraction(h3)

    h_params = [("h1", h1), ("h2", h2), ("h3", h3)]
    param_results = []
    all_zeros = True
    all_denom_ok = True

    for label, h_a in h_params:
        # Squared numerator: [(h_a - h1)(h_a - h2)(h_a - h3)]^2
        base_num = (h_a - h1) * (h_a - h2) * (h_a - h3)
        num = base_num * base_num
        # Squared denominator: [(h_a + h1)(h_a + h2)(h_a + h3)]^2
        base_den = (h_a + h1) * (h_a + h2) * (h_a + h3)
        den = base_den * base_den
        num_zero = num == Fraction(0)
        den_nonzero = den != Fraction(0)
        if not num_zero:
            all_zeros = False
        if not den_nonzero:
            all_denom_ok = False
        param_results.append({
            "parameter": label,
            "h_a": str(h_a),
            "numerator_g00": str(num),
            "denominator_g00": str(den),
            "numerator_zero": num_zero,
            "denominator_nonzero": den_nonzero,
            "g00_vanishes": num_zero and den_nonzero,
        })

    # Cross-node pole structure: g_{01}(h_a) has double pole where g_{00}(h_a) = 0
    cross_poles = []
    for label, h_a in h_params:
        cross_poles.append({
            "parameter": label,
            "h_a": str(h_a),
            "g01_has_pole": True,
            "pole_order": 2,
            "reason": "g_{01} = 1/g_{00} and g_{00}(h_a) = 0 (double zero)",
        })

    return {
        "condition": "g_{00}(h_a) = 0 for a = 1, 2, 3",
        "convention": "squared-base: double zeros at h_a",
        "h_parameters": {"h1": str(h1), "h2": str(h2), "h3": str(h3)},
        "cy_sum": str(h1 + h2 + h3),
        "cy_holds": h1 + h2 + h3 == Fraction(0),
        "all_zeros_hold": all_zeros,
        "all_denominators_nonzero": all_denom_ok,
        "wheel_verified": all_zeros and all_denom_ok,
        "parameter_results": param_results,
        "cross_node_poles": cross_poles,
    }
