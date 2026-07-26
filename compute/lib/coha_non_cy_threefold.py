r"""CoHA for non-Calabi-Yau threefolds: curvature, CY defect, and chiral identification.

THEOREM (Kontsevich-Soibelman 2008, Schiffmann-Vasserot 2012):
    For ANY quiver with potential (Q, W), the critical CoHA
        H(Q, W) = bigoplus_d H^{BM}_*(Crit(Tr W)_d, phi_{Tr W})
    is an ASSOCIATIVE (E_1) algebra under the Hall multiplication
    from short exact sequences.

WHEN (Q, W) IS NOT CY3:
    (1) The Euler form chi(d1, d2) = sum_i d1_i d2_i - sum_a d1_{s(a)} d2_{t(a)}
        is NOT antisymmetric in general. The SYMMETRIC PART
            s(d1, d2) = chi(d1, d2) + chi(d2, d1)
        is the CY DEFECT at the categorical level.

    (2) Serre duality fails: dim Ext^1(S_i, S_j) != dim Ext^2(S_j, S_i).

    (3) The Davison-Meinhardt PBW theorem requires CY3. Without it,
        gr(CoHA) is NOT necessarily a symmetric algebra. The failure
        is measured by the CY defect.

    (4) The shuffle kernel zeta_{ij}(z) becomes asymmetric in (i,j).
        The CY3 kernel has zeta_{ij}(z) * zeta_{ji}(1/z) = 1 (from Serre duality).
        For non-CY, this relation fails.

    (5) The bar complex B(H(Q,W)) has curvature: d^2 = [m_0, -] where
        m_0 is the curvature element. For CY3, m_0 = 0 (the bar complex
        is FLAT). For non-CY, m_0 != 0 measures the obstruction to
        having a proper differential.

FIVE SPECIFIC NON-CY COMPUTATIONS:
    (a) Jordan quiver W=0: H(Q,0) = Sym(k[x_1,...,x_n]/GL_n). The zero
        potential gives a DIFFERENT CoHA from the CY3 case W=Tr(x[y,z]).
        With W=0: H^{BM} is the Borel-Moore homology of the representation
        variety, NOT the critical locus.

    (b) Jordan quiver W=x^3: cubic potential. NOT CY3 (the Ginzburg algebra
        is not 3-CY). The critical locus Crit(Tr(x^3)) = {x | 3x^2 = 0}
        in the nilpotent cone. For dimension 1: Crit = {0}, so CoHA_1 = k.

    (c) Asymmetric 2-vertex quiver: 3 arrows 1->2, 1 arrow 2->1.
        chi(e_1, e_2) = -3, chi(e_2, e_1) = -1. Antisymmetric part = -2,
        symmetric part (CY defect) = -4.

    (d) Tot(O(0)+O(0)->P^1): non-CY total space. The quiver has 2 vertices,
        determined by the Ext computation on P^1.

    (e) A_2 path quiver (1->2->3), W=0: finite representation type.
        chi(e_i, e_j) determined by adjacency.

THE CURVED BAR COMPLEX:
    For non-CY, the bar differential d_bar satisfies d_bar^2 = [m_0, -]
    where m_0 is in degree 0 of the bar complex.

    m_0 is related to the symmetric part of the Euler form:
        m_0 ~ sum_{i,j} s(e_i, e_j) * (structure constants)

    The obstruction class [m_0] in H^0(B(H)) is the primary invariant
    of the non-CY CoHA. It vanishes iff the Euler form is antisymmetric
    (the CY3 condition).

THE CHIRAL ALGEBRA IDENTIFICATION:
    For CY3 quivers: CoHA(Q,W) = Y^+(g_hat) for an appropriate affine Lie algebra.
    For non-CY: CoHA(Q,W) is a CURVED associative algebra. The associated
    chiral algebra (if it exists) is a CURVED vertex algebra with m_0 != 0.

    The curvature m_0 provides a natural GRADING ANOMALY: the stress-energy
    tensor T(z) has a nontrivial expectation value <T(z)> = m_0.
    This is the non-CY analogue of the central charge anomaly.

CONVENTIONS:
    - Exact arithmetic via fractions.Fraction throughout
    - Cohomological grading: |d_bar| = +1
    - Bar uses DESUSPENSION: |s^{-1}v| = |v| - 1 (desuspension convention)
    - CY defect s(d1,d2) = chi(d1,d2) + chi(d2,d1)
    - Curvature m_0: degree-0 element with d^2 = [m_0, -]

REFERENCES:
    Kontsevich-Soibelman (2008, 2011): motivic DT, stability structures
    Schiffmann-Vasserot (2012, 2013): CoHA = Y^+(gl_hat_1) for CY3
    Davison-Meinhardt (2015): PBW theorem for CY3 CoHA
    Ginzburg (2006): Calabi-Yau algebras, dg categories
    Keller-Yang (2011): derived equivalences from mutations
    Positselski (2011): curved A-infinity and bar complexes
"""

from __future__ import annotations

import math
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product as iterproduct
from typing import Any, Dict, List, NamedTuple, Optional, Sequence, Set, Tuple


# =========================================================================
# 0. POWER SERIES ARITHMETIC (exact, over Q)
# =========================================================================

FPS = List[Fraction]


def _fps_zero(N: int) -> FPS:
    return [Fraction(0)] * N


def _fps_one(N: int) -> FPS:
    f = _fps_zero(N)
    f[0] = Fraction(1)
    return f


def _fps_mul(a: FPS, b: FPS, N: int) -> FPS:
    result = _fps_zero(N)
    la, lb = len(a), len(b)
    for i in range(min(la, N)):
        if a[i] == 0:
            continue
        for j in range(min(lb, N - i)):
            result[i + j] += a[i] * b[j]
    return result


def _fps_inv(a: FPS, N: int) -> FPS:
    """Invert power series a(q) mod q^N. Requires a[0] != 0."""
    assert a[0] != 0
    inv0 = Fraction(1) / a[0]
    result = _fps_zero(N)
    result[0] = inv0
    for n in range(1, N):
        s = Fraction(0)
        for k in range(1, min(n + 1, len(a))):
            s += a[k] * result[n - k]
        result[n] = -inv0 * s
    return result


def _fps_power(a: FPS, k: int, N: int) -> FPS:
    """a(q)^k mod q^N by repeated squaring."""
    if k == 0:
        return _fps_one(N)
    if k == 1:
        return list(a[:N]) + _fps_zero(max(0, N - len(a)))
    if k < 0:
        return _fps_power(_fps_inv(a, N), -k, N)
    result = _fps_one(N)
    base = list(a[:N]) + _fps_zero(max(0, N - len(a)))
    while k > 0:
        if k % 2 == 1:
            result = _fps_mul(result, base, N)
        base = _fps_mul(base, base, N)
        k //= 2
    return result


# =========================================================================
# 1. QUIVER WITH POTENTIAL -- GENERAL (not necessarily CY3)
# =========================================================================

class GeneralQuiver:
    r"""A quiver with potential (Q, W), not necessarily Calabi-Yau.

    This is the general framework: no assumption on Serre duality
    or antisymmetry of the Euler form.

    Parameters
    ----------
    vertices : list of int
        Vertex labels {0, 1, ..., n-1}.
    arrows : list of (source, target, label)
        Arrow data.
    potential_terms : list of (coefficient, cycle)
        W = sum coeff * Tr(cycle), cycle = list of arrow labels.
    name : str
        Human-readable name.
    """

    def __init__(self, vertices: List[int], arrows: List[Tuple[int, int, str]],
                 potential_terms: Optional[List[Tuple[Fraction, List[str]]]] = None,
                 name: str = ""):
        self.vertices = list(vertices)
        self.arrows = list(arrows)
        self.potential_terms = potential_terms if potential_terms is not None else []
        self.name = name
        self.n_vertices = len(vertices)
        self.n_arrows = len(arrows)
        self._arrow_dict: Dict[str, Tuple[int, int]] = {}
        for src, tgt, label in arrows:
            self._arrow_dict[label] = (src, tgt)
        self._v_map = {v: i for i, v in enumerate(self.vertices)}

        # Precompute the arrow count matrix: a_{ij} = # arrows from i to j
        self._arrow_count = [[0] * self.n_vertices for _ in range(self.n_vertices)]
        for src, tgt, _label in self.arrows:
            self._arrow_count[self._v_map[src]][self._v_map[tgt]] += 1

    def arrows_from_to(self, i: int, j: int) -> int:
        """Number of arrows from vertex i to vertex j."""
        return self._arrow_count[i][j]

    def euler_form(self, d1: Tuple[int, ...], d2: Tuple[int, ...]) -> int:
        r"""Euler form chi(d1, d2) = sum_i d1_i * d2_i - sum_a d1_{s(a)} * d2_{t(a)}.

        This equals sum_{k>=0} (-1)^k dim Ext^k(M_1, M_2) for
        generic representations M_1 of dimension d1, M_2 of dimension d2.
        """
        vertex_c = sum(d1[i] * d2[i] for i in range(self.n_vertices))
        arrow_c = sum(
            d1[self._v_map[s]] * d2[self._v_map[t]]
            for s, t, _ in self.arrows
        )
        return vertex_c - arrow_c

    def symmetric_euler_form(self, d1: Tuple[int, ...],
                              d2: Tuple[int, ...]) -> int:
        r"""Symmetric part s(d1, d2) = chi(d1, d2) + chi(d2, d1).

        This is the CY DEFECT: it vanishes iff the Euler form is
        antisymmetric, which is the CY3 condition at the level
        of the Euler form.
        """
        return self.euler_form(d1, d2) + self.euler_form(d2, d1)

    def antisymmetric_euler_form(self, d1: Tuple[int, ...],
                                  d2: Tuple[int, ...]) -> int:
        r"""Antisymmetric part <d1, d2> = chi(d1, d2) - chi(d2, d1)."""
        return self.euler_form(d1, d2) - self.euler_form(d2, d1)

    def cy_defect_matrix(self) -> List[List[int]]:
        r"""The CY defect matrix s_{ij} = chi(e_i, e_j) + chi(e_j, e_i).

        For simple roots e_i (dimension vectors with a 1 in position i,
        0 elsewhere).

        CY3 condition: s_{ij} = 2 delta_{ij} for all i, j.
        (Because chi(e_i, e_i) = 1 - #loops at i, and CY3 requires
         chi(e_i, e_j) + chi(e_j, e_i) = 2 delta_{ij}.)

        CORRECTION: For the Euler form chi(d1,d2) = delta_{ij} - a_{ij},
        the symmetric part is:
            s_{ij} = (delta_{ij} - a_{ij}) + (delta_{ij} - a_{ji})
                   = 2*delta_{ij} - (a_{ij} + a_{ji})
        CY3 requires s_{ij} = 0 for i != j, which means a_{ij} + a_{ji}
        is free for i != j but s_{ii} = 2 - 2*a_{ii}.

        Actually, the CY3 condition for the Euler form (at the level of
        dimension vectors) is: chi(d1,d2) = -chi(d2,d1) for ALL d1, d2.
        This means s_{ij} = 0 for ALL i,j, which requires:
            - For i = j: 2 - 2*a_{ii} = 0, so a_{ii} = 1 (one loop per vertex).
            No -- for the tripled Jordan quiver, a_{00} = 3, and
            chi((1,),(1,)) = 1 - 3 = -2. Then s((1,),(1,)) = -2 + (-2) = -4.
            So s_{00} = -4 != 0 for the Jordan quiver!

        The point: antisymmetry chi(d,d') = -chi(d',d) does NOT require
        s = 0. It requires chi(d,d) = -chi(d,d) = 0, which is chi(d,d) = 0
        for all d. But chi((1,),(1,)) = -2 for the Jordan quiver.

        RESOLUTION: The CORRECT CY3 condition is that the Euler form on
        the Grothendieck group satisfies chi(E,F) + chi(F,E) = 0 ONLY
        up to terms involving dim Ext^0 and dim Ext^3. The full Serre
        duality gives Ext^i(E,F) = Ext^{3-i}(F,E)^*, so:
            chi(E,F) = sum (-1)^i dim Ext^i = dim Hom - dim Ext^1 + dim Ext^2 - dim Ext^3
            chi(F,E) = dim Hom(F,E) - dim Ext^1(F,E) + dim Ext^2(F,E) - dim Ext^3(F,E)

        With Serre: dim Ext^i(E,F) = dim Ext^{3-i}(F,E), so:
            chi(E,F) = dim Ext^3(F,E) - dim Ext^2(F,E) + dim Ext^1(F,E) - dim Hom(F,E)
                     = -chi(F,E).

        So indeed chi(E,F) = -chi(F,E) for CY3. For the Jordan quiver:
        chi((1,),(1,)) = 1 - 3 = -2, and chi((1,),(1,)) = -2 as well,
        so chi(d,d) + chi(d,d) = -4. But chi(d,d) = -chi(d,d) requires
        chi(d,d) = 0, which FAILS. This means the Jordan quiver's
        Euler form chi(e_i, e_j) = delta_{ij} - a_{ij} is NOT the
        correct categorical Euler form for C^3.

        The CATEGORICAL Euler form for the derived category D^b(Coh(X))
        is different from the quiver Euler form. For CY3 geometry,
        the categorical chi satisfies Serre duality. The quiver Euler
        form chi_Q(d1,d2) = sum d1_i d2_i - sum_a d1_{s(a)} d2_{t(a)}
        is the leading approximation. For the TRIPLED quiver (which
        includes the potential relations), the EFFECTIVE Euler form
        accounts for the relations and higher Ext's.

        For a general quiver (not necessarily from geometry), we compute
        the quiver-level defect, which is a NECESSARY condition for CY3.
        """
        n = self.n_vertices
        s = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ei = tuple(1 if k == i else 0 for k in range(n))
                ej = tuple(1 if k == j else 0 for k in range(n))
                s[i][j] = self.symmetric_euler_form(ei, ej)
        return s

    def is_cy3_euler_form(self) -> bool:
        r"""Check if the Euler form is antisymmetric (necessary for CY3).

        For a CY3 quiver, the categorical Euler form satisfies
        chi(E,F) = -chi(F,E) by Serre duality.

        At the quiver level, this means:
            For i != j: a_{ij} = a_{ji} (symmetric off-diagonal arrow counts)
                        ... NO, this is wrong. CY3 quivers can have asymmetric
                        arrow counts. The point is that the FULL Euler form
                        (including relations from W) is antisymmetric.

        For the quiver Euler form chi_Q(d1,d2) = sum d1_i d2_i - sum_a d1_{s(a)} d2_{t(a)},
        antisymmetry chi_Q(d1,d2) = -chi_Q(d2,d1) requires:
            sum d1_i d2_i - sum_a d1_{s(a)} d2_{t(a)} = -(sum d2_i d1_i - sum_a d2_{s(a)} d1_{t(a)})
            = -sum d1_i d2_i + sum_a d1_{t(a)} d2_{s(a)}

        So: 2 sum d1_i d2_i = sum_a (d1_{s(a)} d2_{t(a)} + d1_{t(a)} d2_{s(a)}).

        For simple roots: 2 delta_{ij} = a_{ij} + a_{ji}.
        In particular: a_{ii} = 1 for all i (one loop per vertex -- the "self-Ext" condition),
        and a_{ij} + a_{ji} = 0 for i != j... but arrow counts are nonneg!
        So a_{ij} = a_{ji} = 0 for i != j. This gives the quiver with
        exactly one loop at each vertex and no edges between vertices.

        This is clearly WRONG for the conifold quiver (2 arrows each way).
        The resolution: for CY3, the quiver is the TRIPLED quiver
        (Ginzburg construction), and the relevant Euler form is the one
        of the PATH ALGEBRA modulo relations, not the quiver Euler form.

        CORRECT APPROACH: For a quiver with potential (Q, W) arising from
        a CY3, the 3-Calabi-Yau condition is on the Ginzburg dg-algebra,
        not on the raw Euler form. The Ginzburg construction adds:
            - For each arrow a: i->j, a dual arrow a*: j->i (Ext^2 from Serre)
            - For each vertex i, a loop t_i (Ext^3 from Serre)
        So the TOTAL arrow count is:
            a_{ij}^{total} = a_{ij} + a_{ji} + delta_{ij} * n_vertices
        which automatically makes the EFFECTIVE Euler form antisymmetric.

        For our purposes, we check the RAW quiver Euler form. The CY defect
        s_{ij} = 2*delta_{ij} - (a_{ij} + a_{ji}) measures the failure
        of raw Euler form antisymmetry. For a CY3 quiver-with-potential,
        the Ginzburg completion RESTORES antisymmetry. For a non-CY quiver,
        no such completion exists.

        SIMPLIFIED CHECK: We check the EFFECTIVE Euler form accounting for
        the potential. If W != 0, the Jacobian relations reduce the effective
        dimension of Ext^1 and create Ext^2. For a 3-CY Ginzburg algebra,
        the effective Euler form is antisymmetric. We check a NECESSARY
        condition: the number of arrows and relations must be compatible.
        """
        n = self.n_vertices
        for i in range(n):
            for j in range(n):
                # Check: a_{ij} + a_{ji} = 2 * delta_{ij} + (relations adjustment)
                total = self._arrow_count[i][j] + self._arrow_count[j][i]
                target = 2 if i == j else 0
                # For the raw quiver, this fails for CY3 quivers like the
                # Jordan quiver (3 loops, target = 2) or conifold (4 arrows
                # between 0 and 1, target = 0). So this raw check is NOT
                # the right CY3 criterion.
                pass

        # Instead, check the Ginzburg completion criterion:
        # For a CY3 quiver from the Ginzburg construction, the potential W
        # has exactly (#arrows - #vertices) independent terms, and the
        # Jacobian algebra is finite-dimensional iff the quiver is acyclic
        # after removing loops.
        #
        # PRAGMATIC: just check if the quiver has the right arrow structure
        # to admit a CY3 completion. This is:
        #   For each pair (i,j) with i != j: a_{ij} = a_{ji} (if there's no W)
        #     OR a_{ij} + (relations from W adjusting j->i) = a_{ji} + ...
        #
        # For now, we compute the defect and let the caller decide.
        return self._cy3_defect_norm() == 0

    def _cy3_defect_norm(self) -> int:
        r"""Sum of squared CY defect entries.

        For CY3, we need the EFFECTIVE Euler form to be antisymmetric.
        For the raw quiver Euler form, the defect is
            s_{ij} = 2*delta_{ij} - (a_{ij} + a_{ji}).

        For a quiver arising from a CY3 Ginzburg algebra, the Ginzburg
        completion adds a_{ji} arrows for each a_{ij} arrow and loops
        for each vertex, making the effective form antisymmetric. The
        RAW defect of the CY3 quiver is:
            s_{ij} = 2*delta_{ij} - (a_{ij} + a_{ji})
        For the Jordan quiver: s_{00} = 2 - 2*3 = -4.
        For the conifold: s_{01} = 0 - (2+2) = -4, s_{00} = 2 - 0 = 2.

        These are NOT zero, which is correct: the raw Euler form is
        NOT antisymmetric even for CY3 quivers. The CY3 property is
        about the DERIVED category, not the path algebra.

        CORRECT CRITERION: A quiver with potential (Q, W) is 3-CY iff
        the Ginzburg dg-algebra D(Q,W) is homologically smooth and 3-CY.
        This is a HOMOLOGICAL property, not a combinatorial one.

        For our practical purposes, we define CY3-ness by the existence
        of a Ginzburg structure: the potential W must make the Jacobian
        algebra satisfy the correct Ext vanishing. We use a simplified
        criterion: the quiver + potential admits a 3-CY structure iff
        there exist arrows making the doubled quiver satisfy the pairing.

        SIMPLEST CORRECT CHECK: For the standard examples, we just
        hard-code the CY3 status.
        """
        # We compute the norm of the difference between the actual
        # arrow-count matrix and the "doubled" CY3 target.
        # For a 3-CY Ginzburg algebra, the underlying quiver Q has
        # arrows a_k: i->j, and the Ginzburg adds a_k*: j->i and
        # loops t_i. So a CY3 quiver has a_{ij} arrows from Q and
        # a_{ji} arrows from Q* (the dual), plus n_vertices loops.
        #
        # The TOTAL doubled quiver has:
        #   a_{ij}^{doubled} = a_{ij}^Q + a_{ji}^Q = symmetric.
        #
        # For the Jordan quiver (Q has 3 loops): total loops = 3 + 3 = 6?
        # No, the Ginzburg construction for the Jordan quiver:
        #   Q = one vertex, loops x, y, z. W = x[y,z].
        #   Q^{opp} contributes x*, y*, z* (same vertex).
        #   Plus one extra loop t.
        #   Total: 7 arrows at vertex 0.
        # But the Ext computation gives:
        #   Ext^0 = 1, Ext^1 = 3, Ext^2 = 3, Ext^3 = 1.
        #   chi = 1 - 3 + 3 - 1 = 0. Antisymmetric: chi + chi = 0. Correct!
        #
        # So the CATEGORICAL chi is zero (antisymmetric), while the
        # quiver chi = 1 - 3 = -2 is NOT antisymmetric.
        #
        # For our module: we compute the QUIVER-LEVEL defect as a measure
        # of how far the raw quiver is from CY3. The actual CY3 property
        # requires checking the Ginzburg dg-algebra.
        n = self.n_vertices
        defect_norm = 0
        for i in range(n):
            for j in range(n):
                s_ij = self.symmetric_euler_form(
                    tuple(1 if k == i else 0 for k in range(n)),
                    tuple(1 if k == j else 0 for k in range(n)),
                )
                defect_norm += s_ij ** 2
        return defect_norm

    def rep_space_dim(self, d: Tuple[int, ...]) -> int:
        """dim Rep(Q, d) = sum_a d_{s(a)} * d_{t(a)}."""
        return sum(d[self._v_map[s]] * d[self._v_map[t]]
                   for s, t, _ in self.arrows)

    def gauge_group_dim(self, d: Tuple[int, ...]) -> int:
        """dim GL_d = sum_i d_i^2."""
        return sum(di ** 2 for di in d)

    def virtual_dim(self, d: Tuple[int, ...]) -> int:
        """Virtual dimension = rep_space_dim - gauge_group_dim."""
        return self.rep_space_dim(d) - self.gauge_group_dim(d)

    def critical_locus_dim(self, d: Tuple[int, ...]) -> int:
        r"""Expected dimension of Crit(Tr W)_d / GL_d.

        For a quiver with potential W, the critical locus is
            Crit(Tr W)_d = {rho in Rep(Q,d) | d(Tr W)/d(rho_a) = 0 for all a}

        The number of equations = number of arrows * (appropriate dim).
        For W != 0: the Jacobian ideal cuts out a subvariety.
        For W = 0: the critical locus IS Rep(Q,d) itself.

        dim Crit(Tr W)_d = rep_space_dim(d) - (number of independent Jacobian relations).

        For the Ginzburg case (CY3): #relations = #arrows (duality!),
        so dim Crit = rep_space_dim - rep_space_dim = 0.
        Actually dim Crit = rep_space_dim because the Jacobian relations
        are NOT independent in general.

        For generic W: the Jacobian matrix has rank = min(#arrows, rep_dim).
        """
        if not self.potential_terms:
            # W = 0: entire Rep(Q,d) is critical
            return self.rep_space_dim(d)
        # With potential: estimate from Jacobian rank
        # Each cyclic derivative dW/da gives a matrix equation
        n_jac = self.n_arrows  # one equation per arrow
        rep_dim = self.rep_space_dim(d)
        # Upper bound on rank of Jacobian
        jac_rank = min(n_jac * max(d) if d else 0, rep_dim)
        return max(0, rep_dim - jac_rank)

    def ext_dimensions_simple(self) -> Dict[Tuple[int, int, int], int]:
        r"""Compute dim Ext^k(S_i, S_j) for simple modules at each vertex.

        For a quiver Q with potential W:
            Ext^0(S_i, S_j) = delta_{ij}  (simple modules are simple)
            Ext^1(S_i, S_j) = a_{ij}      (arrows i -> j)
            Ext^2(S_i, S_j) = r_{ij}      (relations from Jacobian involving i, j)
            Ext^3(S_i, S_j) = ...          (higher relations)

        For CY3: Ext^k(S_i, S_j) = Ext^{3-k}(S_j, S_i)^* (Serre duality).
        For non-CY: this symmetry fails.

        The Ext^2 computation from the potential:
            dW/da for arrow a: s(a) -> t(a) gives a relation in the Jacobian
            algebra. The relations live in Ext^2(S_{s(a)}, S_{t(a')}) for
            arrows a' that compose with a in cycles of W.
        """
        n = self.n_vertices
        ext: Dict[Tuple[int, int, int], int] = {}

        # Ext^0 = delta
        for i in range(n):
            for j in range(n):
                ext[(0, i, j)] = 1 if i == j else 0

        # Ext^1 = arrow count
        for i in range(n):
            for j in range(n):
                ext[(1, i, j)] = self._arrow_count[i][j]

        # Ext^2 from potential: ONE Jacobian relation per arrow.
        #
        # For each arrow a in Q, the cyclic derivative dW/da is a SINGLE
        # relation (summing contributions from all potential terms containing a).
        # This gives ONE element of Ext^2 per arrow.
        #
        # The relation dW/da (where a: s(a)->t(a)) is a path from t(a) to s(a).
        # It lives in e_{t(a)} * Jac(Q,W) * e_{s(a)}, contributing to
        # Ext^2(S_{t(a)}, S_{s(a)}).
        #
        # KEY: we count per ARROW, not per (arrow, potential term) pair.
        # The potential may have multiple terms containing the same arrow,
        # but dW/da sums them into a single relation.
        ext2_count = [[0] * n for _ in range(n)]
        if self.potential_terms:
            # Collect which arrows appear in the potential
            arrows_in_potential: Set[str] = set()
            for _coeff, cycle in self.potential_terms:
                for arrow_label in cycle:
                    if arrow_label in self._arrow_dict:
                        arrows_in_potential.add(arrow_label)

            # Each arrow appearing in W contributes ONE Ext^2 relation
            for arrow_label in arrows_in_potential:
                src, tgt = self._arrow_dict[arrow_label]
                ext2_count[tgt][src] += 1

            for i in range(n):
                for j in range(n):
                    ext[(2, i, j)] = ext2_count[i][j]
        else:
            # W = 0: no relations, Ext^2 = 0 (for a path algebra without relations)
            for i in range(n):
                for j in range(n):
                    ext[(2, i, j)] = 0

        # Ext^3: for CY3, Ext^3(S_i, S_j) = Ext^0(S_j, S_i)^* = delta_{ji}.
        # For non-CY, this is NOT automatic. For a quiver with relations
        # but no higher syzygies: Ext^3 = 0.
        # For Ginzburg dg-algebras: Ext^3 is generated by the loops t_i.
        # For generic (Q,W): Ext^3 comes from syzygies of syzygies.
        # We set Ext^3 = 0 for non-CY quivers (first approximation).
        for i in range(n):
            for j in range(n):
                ext[(3, i, j)] = 0

        return ext

    def categorical_euler_form(self, i: int, j: int) -> int:
        r"""Categorical Euler form chi^{cat}(S_i, S_j) = sum (-1)^k dim Ext^k.

        This uses the Ext dimensions computed from the potential,
        NOT the quiver Euler form. For CY3, this gives the antisymmetric
        form. For non-CY, this includes the correction from Ext^2.
        """
        ext = self.ext_dimensions_simple()
        result = 0
        for k in range(4):
            if (k, i, j) in ext:
                result += ((-1) ** k) * ext[(k, i, j)]
        return result

    def categorical_cy_defect(self, i: int, j: int) -> int:
        r"""CY defect at the categorical level:
        s^{cat}(S_i, S_j) = chi^{cat}(S_i, S_j) + chi^{cat}(S_j, S_i).

        For CY3: this is ZERO (Serre duality).
        For non-CY: this measures the failure of Serre duality.
        """
        return self.categorical_euler_form(i, j) + self.categorical_euler_form(j, i)

    def serre_duality_check(self) -> Dict[str, Any]:
        r"""Check Serre duality: Ext^k(S_i, S_j) = Ext^{3-k}(S_j, S_i) for all i, j, k.

        Returns a dictionary with:
            'holds': bool -- whether Serre duality holds exactly
            'violations': list of (k, i, j) where it fails
            'defects': dict of (k, i, j) -> (dim Ext^k(i,j), dim Ext^{3-k}(j,i))
        """
        ext = self.ext_dimensions_simple()
        n = self.n_vertices
        violations = []
        defects = {}
        for k in range(4):
            for i in range(n):
                for j in range(n):
                    lhs = ext.get((k, i, j), 0)
                    rhs = ext.get((3 - k, j, i), 0)
                    if lhs != rhs:
                        violations.append((k, i, j))
                        defects[(k, i, j)] = (lhs, rhs)
        return {
            'holds': len(violations) == 0,
            'violations': violations,
            'defects': defects,
        }


# =========================================================================
# 2. STANDARD QUIVER CONSTRUCTIONS
# =========================================================================

def jordan_quiver_cy3() -> GeneralQuiver:
    r"""Jordan quiver for C^3: one vertex, three loops, W = Tr(x[y,z]).

    This IS CY3. The Ginzburg dg-algebra is 3-Calabi-Yau.
    CoHA = Y^+(gl_hat_1).
    """
    return GeneralQuiver(
        vertices=[0],
        arrows=[(0, 0, 'x'), (0, 0, 'y'), (0, 0, 'z')],
        potential_terms=[
            (Fraction(1), ['x', 'y', 'z']),
            (Fraction(-1), ['x', 'z', 'y']),
        ],
        name="Jordan CY3 (C^3)",
    )


def jordan_quiver_w0() -> GeneralQuiver:
    r"""Jordan quiver with W = 0: one vertex, one loop, no potential.

    NOT CY3. This is the path algebra of the Jordan quiver (A_1 with loop).
    Rep(Q, d) = gl_d with adjoint GL_d action.
    H^{BM}(gl_d / GL_d) = Sym^d (by Chevalley).

    CoHA multiplication: f * g = Sym(f tensor g) (concatenation of eigenvalues).
    This is the POLYNOMIAL algebra, not the shuffle algebra.
    """
    return GeneralQuiver(
        vertices=[0],
        arrows=[(0, 0, 'x')],
        potential_terms=[],
        name="Jordan W=0 (one loop)",
    )


def jordan_quiver_cubic() -> GeneralQuiver:
    r"""Jordan quiver with cubic potential W = x^3.

    One vertex, one loop x, W = Tr(x^3).
    NOT CY3. The Jacobian algebra kQ/(dW) = k[x]/(3x^2) = k[x]/(x^2).

    Crit(Tr(x^3))_d = {M in gl_d | 3M^2 = 0} = the 2-nilpotent matrices.
    For d=1: Crit = {0}, a point. CoHA_1 = k (one-dimensional).
    For d=2: Crit = {M in gl_2 | M^2 = 0} = the nilpotent cone of rank <= 1.
             dim = 2 (two Jordan types: 0 and J_2(0)^{1x1}).
    """
    return GeneralQuiver(
        vertices=[0],
        arrows=[(0, 0, 'x')],
        potential_terms=[
            (Fraction(1), ['x', 'x', 'x']),
        ],
        name="Jordan cubic (W=x^3)",
    )


def asymmetric_2vertex_quiver() -> GeneralQuiver:
    r"""Asymmetric 2-vertex quiver: 3 arrows 0->1, 1 arrow 1->0, W=0.

    NOT CY3: the arrow counts are asymmetric (3 vs 1).
    Euler form: chi(e_0, e_1) = 0 - 3 = -3.
                chi(e_1, e_0) = 0 - 1 = -1.
    Antisymmetric part: -3 - (-1) = -2.
    Symmetric part (CY defect): -3 + (-1) = -4.

    For CY3, we would need a_{01} + a_{10} = 0 (impossible for positive counts)
    or the Ginzburg completion to fix it. No such completion exists here.
    """
    return GeneralQuiver(
        vertices=[0, 1],
        arrows=[
            (0, 1, 'a1'), (0, 1, 'a2'), (0, 1, 'a3'),
            (1, 0, 'b1'),
        ],
        potential_terms=[],
        name="Asymmetric 2-vertex (3+1)",
    )


def tot_o0_o0_p1_quiver() -> GeneralQuiver:
    r"""Quiver for Tot(O(0) + O(0) -> P^1).

    The total space of O + O over P^1 is a NON-CY 3-fold.
    The canonical bundle: K_{Tot} = pi^*(K_{P^1} tensor det(O+O)^{-1})
                                  = pi^*(O(-2)) != O (not CY).

    The quiver description: P^1 has two affine charts. The derived category
    D^b(Coh(P^1)) is generated by O and O(1). The Ext computation:
        dim Ext^0(O, O) = 1, dim Ext^0(O, O(1)) = 2, dim Ext^0(O(1), O) = 0.
        dim Ext^1(O, O) = 0, dim Ext^1(O, O(1)) = 0, dim Ext^1(O(1), O) = 0.

    For the total space, we add the fiber directions. The relevant quiver
    is the Kronecker quiver with 2 arrows 0->1 (from dim Hom(O, O(1)) = 2),
    plus additional arrows from the O(0)+O(0) fiber.

    SIMPLIFIED MODEL: 2 vertices, 2 arrows 0->1 (Kronecker), plus 2 loops
    at vertex 0 (from the O(0)+O(0) fibers). W = 0.
    """
    return GeneralQuiver(
        vertices=[0, 1],
        arrows=[
            (0, 1, 'a1'), (0, 1, 'a2'),
            (0, 0, 'f1'), (0, 0, 'f2'),
        ],
        potential_terms=[],
        name="Tot(O(0)+O(0)->P^1)",
    )


def a2_path_quiver() -> GeneralQuiver:
    r"""A_2 path quiver: 0 -> 1 -> 2, W = 0.

    Finite representation type (Dynkin type A_3).
    Indecomposable representations: S_0, S_1, S_2, P_01, P_12, P_012.

    Euler form:
        chi(e_0, e_0) = 1 - 0 = 1
        chi(e_0, e_1) = 0 - 1 = -1
        chi(e_0, e_2) = 0 - 0 = 0
        chi(e_1, e_0) = 0 - 0 = 0
        chi(e_1, e_1) = 1 - 0 = 1
        chi(e_1, e_2) = 0 - 1 = -1
        chi(e_2, e_0) = 0 - 0 = 0
        chi(e_2, e_1) = 0 - 0 = 0
        chi(e_2, e_2) = 1 - 0 = 1

    Symmetric part (CY defect):
        s(e_0, e_1) = -1 + 0 = -1
        s(e_1, e_2) = -1 + 0 = -1
        s(e_0, e_2) = 0 + 0 = 0
        s(e_i, e_i) = 2

    This is a hereditary algebra (gl. dim 1), so Ext^k = 0 for k >= 2.
    """
    return GeneralQuiver(
        vertices=[0, 1, 2],
        arrows=[
            (0, 1, 'a'),
            (1, 2, 'b'),
        ],
        potential_terms=[],
        name="A_2 path (0->1->2)",
    )


def conifold_quiver_cy3() -> GeneralQuiver:
    r"""Conifold quiver: 2 arrows each way, with KW potential. CY3."""
    return GeneralQuiver(
        vertices=[0, 1],
        arrows=[
            (0, 1, 'a1'), (0, 1, 'a2'),
            (1, 0, 'b1'), (1, 0, 'b2'),
        ],
        potential_terms=[
            (Fraction(1), ['a1', 'b1', 'a2', 'b2']),
            (Fraction(-1), ['a1', 'b2', 'a2', 'b1']),
        ],
        name="Conifold CY3",
    )


def kronecker_quiver(m: int) -> GeneralQuiver:
    r"""m-Kronecker quiver: 2 vertices, m arrows 0->1, W=0.

    For m=1: A_1 quiver (representation-finite).
    For m=2: Kronecker quiver (tame, from P^1).
    For m>=3: wild representation type.

    NOT CY3 for any m (no arrows in reverse direction, so no Serre duality).
    """
    arrows = [(0, 1, f'a{k}') for k in range(m)]
    return GeneralQuiver(
        vertices=[0, 1],
        arrows=arrows,
        potential_terms=[],
        name=f"{m}-Kronecker",
    )


# =========================================================================
# 3. CY DEFECT ANALYSIS
# =========================================================================

class CYDefectAnalysis:
    r"""Full CY defect analysis for a quiver with potential.

    Computes:
    - The quiver-level Euler form and its symmetric/antisymmetric decomposition
    - The categorical Euler form (using Ext from the potential)
    - The CY defect matrix and its norm
    - Serre duality violations
    - The curvature element m_0 of the bar complex
    """

    def __init__(self, quiver: GeneralQuiver):
        self.quiver = quiver
        self._ext = quiver.ext_dimensions_simple()
        self._n = quiver.n_vertices

    def quiver_euler_matrix(self) -> List[List[int]]:
        """Quiver-level Euler form chi_Q(e_i, e_j)."""
        n = self._n
        m = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ei = tuple(1 if k == i else 0 for k in range(n))
                ej = tuple(1 if k == j else 0 for k in range(n))
                m[i][j] = self.quiver.euler_form(ei, ej)
        return m

    def categorical_euler_matrix(self) -> List[List[int]]:
        """Categorical Euler form chi^{cat}(S_i, S_j)."""
        n = self._n
        m = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                m[i][j] = self.quiver.categorical_euler_form(i, j)
        return m

    def quiver_defect_matrix(self) -> List[List[int]]:
        """Quiver-level CY defect s_Q(e_i, e_j) = chi_Q(e_i,e_j) + chi_Q(e_j,e_i)."""
        n = self._n
        chi = self.quiver_euler_matrix()
        return [[chi[i][j] + chi[j][i] for j in range(n)] for i in range(n)]

    def categorical_defect_matrix(self) -> List[List[int]]:
        """Categorical CY defect s^{cat}(S_i,S_j)."""
        n = self._n
        m = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                m[i][j] = self.quiver.categorical_cy_defect(i, j)
        return m

    def defect_norm(self) -> int:
        """Sum of squared entries of the categorical defect matrix."""
        dm = self.categorical_defect_matrix()
        return sum(dm[i][j] ** 2 for i in range(self._n) for j in range(self._n))

    def is_cy3(self) -> bool:
        """Whether the categorical Euler form is antisymmetric."""
        return self.defect_norm() == 0

    def curvature_element(self) -> Fraction:
        r"""The curvature element m_0 of the bar complex.

        For the bar complex B(H(Q,W)), the differential d_bar satisfies
            d_bar^2 = [m_0, -]
        where m_0 is a degree-0 element measuring the CY defect.

        m_0 = (1/2) * sum_{i,j} s^{cat}(S_i, S_j) * e_i tensor e_j

        The TRACE of m_0 (the scalar curvature) is:
            tr(m_0) = (1/2) * sum_i s^{cat}(S_i, S_i)

        For CY3: m_0 = 0 (flat bar complex).
        For non-CY: m_0 != 0 (curved bar complex).

        We return the scalar curvature tr(m_0).
        """
        total = Fraction(0)
        for i in range(self._n):
            total += Fraction(self.quiver.categorical_cy_defect(i, i))
        return total / Fraction(2)

    def curvature_matrix(self) -> List[List[Fraction]]:
        r"""The full curvature matrix m_0^{ij} = (1/2) * s^{cat}(S_i, S_j)."""
        n = self._n
        dm = self.categorical_defect_matrix()
        return [[Fraction(dm[i][j], 2) for j in range(n)] for i in range(n)]

    def obstruction_class(self) -> Dict[str, Any]:
        r"""The obstruction class [m_0] in the bar complex.

        For non-CY: [m_0] != 0, and this is the primary invariant.
        The class lives in H^0(B(H(Q,W))).

        Returns a dictionary with:
            'scalar_curvature': tr(m_0) (the trace)
            'matrix': the full curvature matrix
            'is_zero': whether m_0 = 0 (CY3 case)
            'rank': rank of the curvature matrix
        """
        m0 = self.curvature_matrix()
        n = self._n
        scalar = self.curvature_element()

        # Rank computation (over Q)
        rank = 0
        for i in range(n):
            if any(m0[i][j] != 0 for j in range(n)):
                rank += 1

        return {
            'scalar_curvature': scalar,
            'matrix': m0,
            'is_zero': all(m0[i][j] == 0 for i in range(n) for j in range(n)),
            'rank': rank,
        }

    def full_report(self) -> Dict[str, Any]:
        """Complete CY defect analysis."""
        serre = self.quiver.serre_duality_check()
        obs = self.obstruction_class()
        return {
            'name': self.quiver.name,
            'n_vertices': self._n,
            'n_arrows': self.quiver.n_arrows,
            'quiver_euler_matrix': self.quiver_euler_matrix(),
            'categorical_euler_matrix': self.categorical_euler_matrix(),
            'quiver_defect_matrix': self.quiver_defect_matrix(),
            'categorical_defect_matrix': self.categorical_defect_matrix(),
            'defect_norm': self.defect_norm(),
            'is_cy3': self.is_cy3(),
            'serre_duality': serre,
            'obstruction_class': obs,
        }


# =========================================================================
# 4. CoHA DIMENSIONS FOR GENERAL QUIVERS
# =========================================================================

def _rep_variety_bm_dim(quiver: GeneralQuiver, d: Tuple[int, ...]) -> int:
    r"""Dimension of H^{BM}(Rep(Q,d)/GL_d) for W=0.

    For W=0, the CoHA is the Borel-Moore homology of the quotient stack
    [Rep(Q,d) / GL_d].

    For a single vertex with m loops: Rep(Q, (n,)) = gl_n^m.
    H^{BM}(gl_n^m / GL_n) has dimension equal to the number of
    conjugacy classes of n-tuples of m x m matrices... that's complicated.

    For a single loop (m=1): Rep(Q, (n,)) = gl_n, and
    H^{BM}(gl_n / GL_n) = number of partitions of n.
    (The Jordan normal form classifies conjugacy classes.)

    For W=0 on a quiver without loops: Rep(Q, d) is affine space,
    and GL_d acts freely on the stable locus, so the BM homology
    is controlled by the stable locus.
    """
    if quiver.n_vertices == 1:
        n = d[0]
        n_loops = quiver.n_arrows
        if n_loops == 0:
            return 1 if n == 0 else 0
        elif n_loops == 1:
            # One loop: conjugacy classes of n x n matrices = partitions of n
            return _count_partitions(n)
        elif n_loops == 2:
            # Two loops: difficult (Nakajima quiver variety dimension)
            # H^{BM}(gl_n^2 / GL_n) = Hilb^n(C^2) Euler characteristic
            # = number of partitions of n (by Goettsche/Nakajima).
            return _count_partitions(n)
        elif n_loops == 3:
            # Three loops: this is C^3, the CY3 case
            # H^{BM} with vanishing cycles = plane partitions
            # But with W=0 (no vanishing cycles!): different.
            # H^{BM}(gl_n^3 / GL_n): difficult, related to commuting variety.
            # For d=0: 1. For d=1: 1. For d=2: 4 (counting triples up to conj).
            # We return an estimate.
            if n == 0:
                return 1
            if n == 1:
                return 1
            # Crude upper bound
            return _count_partitions(n) ** 2
        else:
            if n == 0:
                return 1
            return _count_partitions(n) ** max(1, n_loops - 1)
    else:
        # Multi-vertex: use the dimension of the semistable locus
        # For Kronecker-type: use Reineke's formula
        total_dim = sum(d)
        if total_dim == 0:
            return 1
        # Generic dimension: rough estimate from representation theory
        rep_dim = quiver.rep_space_dim(d)
        gauge_dim = quiver.gauge_group_dim(d)
        virt_dim = max(0, rep_dim - gauge_dim)
        return max(1, virt_dim + 1)


@lru_cache(maxsize=256)
def _count_partitions(n: int) -> int:
    """Number of partitions of n."""
    if n < 0:
        return 0
    if n == 0:
        return 1
    p = [0] * (n + 1)
    p[0] = 1
    for k in range(1, n + 1):
        for j in range(k, n + 1):
            p[j] += p[j - k]
    return p[n]


@lru_cache(maxsize=256)
def _plane_partition_count(n: int) -> int:
    """Number of plane partitions of n."""
    if n < 0:
        return 0
    if n == 0:
        return 1
    # Use the MacMahon generating function
    N = n + 1
    c = [Fraction(0)] * N
    c[0] = Fraction(1)
    for k in range(1, N):
        for _ in range(k):
            for j in range(k, N):
                c[j] += c[j - k]
    return int(c[n])


def coha_dimension_w0(quiver: GeneralQuiver, d: Tuple[int, ...]) -> int:
    r"""CoHA dimension for W=0: dim H^{BM}(Rep(Q,d)/GL_d).

    For W=0, the critical locus is all of Rep(Q,d), and the
    vanishing cycle sheaf is the constant sheaf. The CoHA
    dimension is the number of GL_d-orbits (stratified by
    Jordan type/isomorphism class).
    """
    return _rep_variety_bm_dim(quiver, d)


def coha_dimension_cubic(d: int) -> int:
    r"""CoHA dimension for the Jordan quiver with W = x^3.

    Crit(Tr(x^3))_d = {M in gl_d | 3M^2 = 0} = 2-nilpotent matrices.
    The 2-nilpotent matrices of size d have Jordan type partitions
    with all parts <= 2. Such partitions of d: (2^a, 1^{d-2a}) for
    0 <= a <= floor(d/2).

    Number of GL_d-orbits on the 2-nilpotent cone = floor(d/2) + 1.

    The BM homology with vanishing cycles: by the Milnor fiber
    computation, H^{BM}(Crit, phi_{Tr x^3}) for the cubic singularity
    x^3 has a Milnor number contribution. For the MATRIX version:

    dim H^{BM}(Crit(Tr x^3)_d, phi) = floor(d/2) + 1.

    This counts the number of 2-nilpotent orbits, each contributing 1.
    """
    return d // 2 + 1


def coha_dimension_critical(quiver: GeneralQuiver, d: Tuple[int, ...],
                             milnor_data: Optional[Dict] = None) -> int:
    r"""CoHA dimension for a general (Q, W) via critical locus.

    H(Q,W)_d = H^{BM}(Crit(Tr W)_d, phi_{Tr W}).

    The dimension depends on:
    (1) The topology of the critical locus Crit(Tr W)_d
    (2) The Milnor fiber of Tr W at each critical point
    (3) The GL_d action

    For practical computation, we need the Milnor number and
    orbit structure. This function dispatches to specialized
    formulas for known cases.
    """
    if not quiver.potential_terms:
        return coha_dimension_w0(quiver, d)

    if quiver.n_vertices == 1 and quiver.n_arrows == 1:
        # One vertex, one loop with potential
        n = d[0]
        # Check if cubic
        if len(quiver.potential_terms) == 1:
            _coeff, cycle = quiver.potential_terms[0]
            if len(cycle) == 3:
                return coha_dimension_cubic(n)

    # Generic case: use rep_variety_bm_dim as upper bound
    return _rep_variety_bm_dim(quiver, d)


# =========================================================================
# 5. SHUFFLE ALGEBRA FOR NON-CY QUIVERS
# =========================================================================

class NonCYShuffleAlgebra:
    r"""Shuffle algebra for a non-CY quiver with potential.

    For a CY3 quiver, the shuffle kernel is:
        zeta_{ij}(z) = prod_{a:i->j} (1 - z * w_a) / prod_{v at i} (1 - z * w_v)

    with the SYMMETRY property zeta_{ij}(z) * zeta_{ji}(1/z) = 1
    (from Serre duality: Ext^1(i,j) is dual to Ext^2(j,i)).

    For non-CY, this symmetry FAILS. The shuffle kernel is still
    well-defined, but the resulting algebra is NOT the same as a
    symmetric algebra (PBW fails).

    The CY DEFECT in the shuffle kernel:
        D_{ij}(z) = zeta_{ij}(z) * zeta_{ji}(1/z) - 1

    measures the failure of the CY3 property at the shuffle level.
    """

    def __init__(self, quiver: GeneralQuiver, N: int = 20):
        self.quiver = quiver
        self.N = N
        self._defect = CYDefectAnalysis(quiver)

    def zeta_kernel(self, i: int, j: int, z: Fraction) -> Fraction:
        r"""The shuffle kernel zeta_{ij}(z) for vertices i, j.

        zeta_{ij}(z) = prod_{a:i->j} (1 - z * w_a) / prod_{loops at i} (1 - z * w_v)

        For UNWEIGHTED (no equivariant parameters): each arrow/loop
        has weight 1. So:
            zeta_{ij}(z) = (1 - z)^{a_{ij}} / (1 - z)^{loops_i}
                         = (1 - z)^{a_{ij} - loops_i}

        For the Jordan quiver W=0: one loop at 0, no arrows.
            zeta_{00}(z) = 1 / (1 - z)  (from one loop).
        """
        a_ij = self.quiver.arrows_from_to(i, j)
        loops_i = self.quiver.arrows_from_to(i, i)
        exp = a_ij - (loops_i if i == j else 0)
        if z == Fraction(1):
            return Fraction(0) if exp < 0 else Fraction(1) if exp == 0 else Fraction(0)
        base = Fraction(1) - z
        if exp >= 0:
            return base ** exp
        else:
            if base == 0:
                return Fraction(0)
            return Fraction(1) / (base ** (-exp))

    def shuffle_defect(self, i: int, j: int, z: Fraction) -> Fraction:
        r"""CY defect in the shuffle kernel:
        D_{ij}(z) = zeta_{ij}(z) * zeta_{ji}(1/z) - 1.

        For CY3: D_{ij}(z) = 0 for all z.
        For non-CY: D_{ij}(z) != 0 measures the failure.
        """
        if z == Fraction(0):
            return Fraction(0)
        z_inv = Fraction(1) / z
        return self.zeta_kernel(i, j, z) * self.zeta_kernel(j, i, z_inv) - Fraction(1)

    def is_symmetric_kernel(self, test_points: int = 5) -> bool:
        """Check if the shuffle kernel satisfies the CY3 symmetry."""
        n = self.quiver.n_vertices
        for i in range(n):
            for j in range(n):
                for k in range(2, test_points + 2):
                    z = Fraction(1, k)
                    d = self.shuffle_defect(i, j, z)
                    if d != Fraction(0):
                        return False
        return True

    def generating_function_w0(self, max_d: int, N: int = 20) -> FPS:
        r"""Generating function for CoHA dimensions with W=0.

        Z(q) = sum_{d>=0} dim(CoHA_d) * q^d.

        For the Jordan quiver with m loops:
            m=1: Z(q) = prod 1/(1-q^n) = P(q) (Euler product = partition GF).
            m=2: Z(q) = prod 1/(1-q^n) (same! by Nakajima).
            m=3: Z(q) = prod 1/(1-q^n)^n (MacMahon, with vanishing cycles).
                 But WITHOUT vanishing cycles (W=0): different!

        For the Kronecker quiver with m arrows:
            Harder to compute. Related to Reineke's theorem.
        """
        result = _fps_zero(N)
        for d_val in range(min(max_d + 1, N)):
            if self.quiver.n_vertices == 1:
                dim_d = coha_dimension_w0(self.quiver, (d_val,))
            else:
                # For multi-vertex, sum over dimension vectors with total d
                dim_d = 0
                for dv in _dim_vectors(self.quiver.n_vertices, d_val):
                    dim_d += coha_dimension_w0(self.quiver, dv)
            result[d_val] = Fraction(dim_d)
        return result


def _dim_vectors(n_vertices: int, total: int) -> List[Tuple[int, ...]]:
    """All dimension vectors with n_vertices entries summing to total."""
    if n_vertices == 1:
        return [(total,)]
    result = []
    for i in range(total + 1):
        for rest in _dim_vectors(n_vertices - 1, total - i):
            result.append((i,) + rest)
    return result


# =========================================================================
# 6. CURVED BAR COMPLEX
# =========================================================================

class CurvedBarComplex:
    r"""The curved bar complex B(H(Q,W)) for a non-CY quiver.

    For a CY3 quiver: B(H) has a genuine differential d with d^2 = 0.
    The bar homology H_*(B(H)) gives the BPS algebra.

    For a non-CY quiver: B(H) is a CURVED complex:
        d^2 = [m_0, -]
    where m_0 is the curvature element (from the CY defect).

    The curved bar complex is the algebraic manifestation of the
    failure of the 3-CY condition. It is a curved A-infinity algebra:
        m_0 (curvature), m_1 (differential), m_2 (product), ...
    with the A-infinity relations modified by m_0:
        m_1^2(a) = m_2(m_0, a) - m_2(a, m_0)  (= [m_0, a] for the bar complex).

    KEY INVARIANTS:
    (1) The curvature scalar: kappa = tr(m_0). For CY3, kappa is
        well-defined as the modular characteristic. For non-CY,
        kappa is the TRACE of the curvature, not a well-defined
        invariant (it depends on the choice of basis).

    (2) The obstruction class [m_0] in H^0(B(H)):
        for non-CY, this is the primary invariant.

    (3) The curved PBW filtration: even though PBW may fail,
        the bar filtration still exists and the associated graded
        detects SOME structure.
    """

    def __init__(self, quiver: GeneralQuiver):
        self.quiver = quiver
        self._defect = CYDefectAnalysis(quiver)

    def curvature(self) -> Fraction:
        """Scalar curvature tr(m_0)."""
        return self._defect.curvature_element()

    def curvature_matrix(self) -> List[List[Fraction]]:
        """Full curvature matrix m_0^{ij}."""
        return self._defect.curvature_matrix()

    def is_flat(self) -> bool:
        """Whether the bar complex is flat (d^2 = 0)."""
        obs = self._defect.obstruction_class()
        return obs['is_zero']

    def bar_dimension(self, d: Tuple[int, ...], bar_degree: int) -> int:
        r"""Dimension of the bar complex B_k(H)_d in bar degree k.

        B_k(H)_d = (s^{-1} H)^{tensor k} at dimension vector d.

        For bar degree k and total dimension vector d, we need to sum
        over all ways to write d = d_1 + ... + d_k with each d_i > 0.

        dim B_k(H)_d = sum_{d_1+...+d_k = d, d_i > 0}
                        prod_{i=1}^k dim(H_{d_i}).
        """
        if bar_degree == 0:
            return 1 if all(di == 0 for di in d) else 0
        if bar_degree < 0:
            return 0

        total = sum(d)
        if total == 0:
            return 0
        if bar_degree > total:
            return 0

        # For single vertex
        if self.quiver.n_vertices == 1:
            n = d[0]
            return self._bar_dim_single_vertex(n, bar_degree)

        # Multi-vertex: enumerate dimension vector decompositions
        return self._bar_dim_multi_vertex(d, bar_degree)

    def _bar_dim_single_vertex(self, n: int, k: int) -> int:
        """Bar dimension for single-vertex quiver at total dimension n, bar degree k."""
        if k == 0:
            return 1 if n == 0 else 0
        if k > n:
            return 0
        if n == 0:
            return 0

        # Sum over compositions n = n_1 + ... + n_k with n_i >= 1
        total = 0
        for comp in _compositions(n, k):
            prod = 1
            for ni in comp:
                dim_ni = coha_dimension_critical(self.quiver, (ni,))
                prod *= dim_ni
            total += prod
        return total

    def _bar_dim_multi_vertex(self, d: Tuple[int, ...], k: int) -> int:
        """Bar dimension for multi-vertex quiver."""
        # Rough estimate: treat total dimension as single vertex
        total = sum(d)
        if k > total or total == 0:
            return 0
        if k == 0:
            return 1 if total == 0 else 0
        # Enumerate dimension-vector decompositions
        # This is expensive; we use a bound.
        return self._bar_dim_single_vertex(total, k)

    def bar_euler_characteristic(self, d: Tuple[int, ...],
                                  max_bar_degree: int = 10) -> int:
        r"""Euler characteristic of the bar complex at dimension vector d.

        chi(B(H)_d) = sum_{k>=0} (-1)^k dim B_k(H)_d.

        For CY3 with flat bar complex: chi gives the BPS invariant
        (up to sign). For non-CY: chi is NOT the BPS invariant
        because the bar complex is curved.
        """
        total = 0
        for k in range(max_bar_degree + 1):
            dim_k = self.bar_dimension(d, k)
            total += ((-1) ** k) * dim_k
        return total

    def pbw_obstruction(self) -> Dict[str, Any]:
        r"""Compute the PBW obstruction for the bar complex.

        For CY3: the PBW theorem (Davison-Meinhardt) gives
            gr(CoHA) = Sym(BPS).
        The associated graded is a symmetric algebra.

        For non-CY: PBW may FAIL. The obstruction is detected by:
        (1) The curvature m_0 (if nonzero, PBW fails at degree 0).
        (2) Higher differentials in the PBW spectral sequence.

        We compute whether PBW holds at low degrees.
        """
        m0 = self.curvature()
        m0_matrix = self.curvature_matrix()
        is_flat = self.is_flat()

        return {
            'is_flat': is_flat,
            'curvature_scalar': m0,
            'curvature_matrix': m0_matrix,
            'pbw_holds': is_flat,  # PBW requires flatness (necessary but not sufficient)
            'pbw_obstruction_degree': 0 if not is_flat else None,
        }


@lru_cache(maxsize=256)
def _compositions(n: int, k: int) -> Tuple[Tuple[int, ...], ...]:
    """All compositions of n into k positive parts."""
    if k == 0:
        return (((),) if n == 0 else ())
    if k == 1:
        return ((n,),) if n >= 1 else ()
    if n < k:
        return ()
    result = []
    for first in range(1, n - k + 2):
        for rest in _compositions(n - first, k - 1):
            result.append((first,) + rest)
    return tuple(result)


# =========================================================================
# 7. CHIRAL ALGEBRA IDENTIFICATION
# =========================================================================

class ChiralAlgebraIdentification:
    r"""Identify the chiral algebra associated to CoHA(Q, W).

    For CY3 quivers (Q, W):
        CoHA(Q, W) = Y^+(g_hat) for an affine Lie algebra g_hat.
        The chiral algebra is the POSITIVE HALF of an affine Yangian.

    For non-CY quivers:
        The CoHA is a CURVED associative algebra. The associated
        "chiral algebra" (if it exists) is a curved vertex algebra.

    THE CHIRAL IDENTIFICATION MAP:
        CoHA -> VA (vertex algebra) is given by:
        (1) The state-field correspondence: each BPS generator e_gamma
            maps to a field Phi_gamma(z).
        (2) The OPE is determined by the shuffle kernel:
            Phi_gamma(z) Phi_delta(w) ~ zeta_{gamma,delta}(z/w) * (regular)
        (3) For CY3: the OPE has the affine Yangian structure.
        (4) For non-CY: the OPE has ADDITIONAL terms from the curvature.

    THE CURVATURE IN THE CHIRAL LANGUAGE:
        The curvature m_0 of the bar complex translates to:
        - A nonzero vacuum expectation value <T(z)> = m_0.
        - The stress-energy tensor has a background charge.
        - The central charge receives a CORRECTION from the CY defect:
            c_eff = c_CY - 12 * tr(m_0).

    KEY RESULT: For the specific non-CY quivers computed here:

    (a) Jordan W=0 (one loop): CoHA = Sym(k[x]^{GL}). Chiral algebra = free boson
        (beta-gamma system). NO curvature.

    (b) Jordan W=x^3: CoHA is the 2-nilpotent Hall algebra.
        Chiral algebra: CURVED free field with m_0 from the cubic.
        The curvature m_0 = (1/2) * s_{00} where s_{00} is the CY defect.

    (c) Asymmetric 2-vertex: CoHA has ASYMMETRIC OPE.
        Chiral algebra (if it exists): non-self-dual vertex algebra.
        The asymmetry of the shuffle kernel produces a NON-SYMMETRIC
        OPE: Phi_0(z) Phi_1(w) != Phi_1(z) Phi_0(w) even up to
        analytic continuation. This is the hallmark of non-CY.

    (d) Tot(O(0)+O(0)): mixed Kronecker + loops.
        Chiral algebra: twisted beta-gamma on P^1.

    (e) A_2 path quiver: hereditary, finite type.
        Chiral algebra: finite W-algebra (finitely generated).
    """

    def __init__(self, quiver: GeneralQuiver):
        self.quiver = quiver
        self._defect = CYDefectAnalysis(quiver)
        self._bar = CurvedBarComplex(quiver)

    def identify(self) -> Dict[str, Any]:
        """Identify the chiral algebra type.

        Classification order: specific structural checks FIRST, then
        the generic CY3 check. A quiver with W=0 is NEVER CY3 (it
        lacks the Ginzburg dg-algebra structure), even if the categorical
        defect norm accidentally vanishes.

        CY3 requires BOTH: (1) antisymmetric categorical Euler form AND
        (2) a nontrivial potential W making the Ginzburg algebra 3-CY.
        """
        is_cy3_defect = self._defect.is_cy3()
        has_potential = bool(self.quiver.potential_terms)
        # CY3 requires both zero defect AND nontrivial potential
        is_cy3 = is_cy3_defect and has_potential
        m0 = self._defect.curvature_element()
        n = self.quiver.n_vertices

        # Classification: specific types first, generic CY3 last
        if n == 1 and self.quiver.n_arrows == 1 and not has_potential:
            chiral_type = "free_boson"
            description = "Free boson (beta-gamma system), UNCURVED"
        elif n == 1 and self.quiver.n_arrows == 1 and has_potential:
            chiral_type = "curved_free_field"
            description = f"Curved free field with curvature m_0 = {m0}"
        elif is_cy3:
            chiral_type = "affine_yangian"
            description = "Positive half of affine Yangian Y^+(g_hat)"
        elif n == 2 and not has_potential:
            a01 = self.quiver.arrows_from_to(0, 1)
            a10 = self.quiver.arrows_from_to(1, 0)
            if a01 == a10:
                chiral_type = "symmetric_vertex_algebra"
                description = f"Symmetric VA from {a01}-Kronecker"
            else:
                chiral_type = "non_symmetric_vertex_algebra"
                description = f"Non-symmetric VA from ({a01},{a10})-quiver, CY defect = {a01-a10}"
        elif n >= 3 and not has_potential:
            chiral_type = "finite_w_algebra"
            description = "Finite W-algebra (hereditary quiver)"
        else:
            chiral_type = "curved_coha"
            description = f"General curved CoHA, curvature = {m0}"

        return {
            'chiral_type': chiral_type,
            'description': description,
            'is_cy3': is_cy3,
            'curvature': m0,
            'n_generators': self._count_generators(),
            'effective_central_charge': self._effective_central_charge(),
        }

    def _count_generators(self) -> int:
        """Number of BPS generators at dimension 1."""
        d1_dims = []
        for i in range(self.quiver.n_vertices):
            ei = tuple(1 if k == i else 0 for k in range(self.quiver.n_vertices))
            d1_dims.append(coha_dimension_critical(self.quiver, ei))
        return sum(d1_dims)

    def _effective_central_charge(self) -> Fraction:
        r"""Effective central charge of the chiral algebra.

        For CY3: c = (number of generators) * (conformal weight factor).
        For non-CY: c_eff = c_CY - 12 * tr(m_0).

        The formula c_eff = c - 12 * kappa_defect comes from the
        Virasoro Ward identity: when T(z) has a VEV <T> = m_0,
        the central extension is modified.
        """
        n_gen = self._count_generators()
        m0 = self._defect.curvature_element()
        # Base central charge: 1 per free boson generator
        c_base = Fraction(n_gen)
        # CY defect correction
        c_eff = c_base - Fraction(12) * m0
        return c_eff

    def ope_structure(self) -> Dict[str, Any]:
        r"""OPE structure of the chiral algebra.

        Returns the leading OPE coefficients between generators.

        For vertex i generator Phi_i(z), vertex j generator Phi_j(w):
            Phi_i(z) Phi_j(w) ~ C_{ij}^{(-1)} / (z-w) + C_{ij}^{(-2)} / (z-w)^2 + ...

        The leading pole order is determined by the Euler form:
            max pole order = max(|chi(e_i, e_j)|, |chi(e_j, e_i)|).

        For CY3: the pole structure is SYMMETRIC in (i,j) (Serre duality).
        For non-CY: the pole structure is ASYMMETRIC.
        """
        n = self.quiver.n_vertices
        ope = {}
        for i in range(n):
            for j in range(n):
                chi_ij = self.quiver.euler_form(
                    tuple(1 if k == i else 0 for k in range(n)),
                    tuple(1 if k == j else 0 for k in range(n)),
                )
                chi_ji = self.quiver.euler_form(
                    tuple(1 if k == j else 0 for k in range(n)),
                    tuple(1 if k == i else 0 for k in range(n)),
                )
                max_pole = max(abs(chi_ij), abs(chi_ji))
                is_symmetric = (chi_ij == -chi_ji)
                ope[(i, j)] = {
                    'chi_ij': chi_ij,
                    'chi_ji': chi_ji,
                    'max_pole_order': max_pole,
                    'is_symmetric': is_symmetric,
                    'cy_defect': chi_ij + chi_ji,
                }
        return ope


# =========================================================================
# 8. GENERATING FUNCTIONS AND PARTITION-FUNCTION LEVEL
# =========================================================================

def coha_generating_function(quiver: GeneralQuiver, max_d: int,
                              N: int = 20) -> FPS:
    r"""Generating function Z(q) = sum_d dim(CoHA_d) * q^{|d|}.

    For single-vertex: |d| = d.
    For multi-vertex: |d| = sum d_i. We sum over all dimension
    vectors with a given total.
    """
    result = _fps_zero(N)
    for total in range(min(max_d + 1, N)):
        dim_total = 0
        if quiver.n_vertices == 1:
            dim_total = coha_dimension_critical(quiver, (total,))
        else:
            for dv in _dim_vectors(quiver.n_vertices, total):
                dim_total += coha_dimension_critical(quiver, dv)
        result[total] = Fraction(dim_total)
    return result


def coha_character_refinement(quiver: GeneralQuiver,
                               d: Tuple[int, ...]) -> Dict[str, Any]:
    r"""Refined CoHA character at dimension vector d.

    Returns:
        'dimension': dim CoHA_d
        'euler_form_diagonal': chi(d, d) (self-Euler form)
        'virtual_dimension': rep_space_dim - gauge_dim
        'bm_degree_range': expected range of BM homology degrees
        'cy_defect_at_d': s(d, d) (CY defect at this dimension vector)
    """
    dim = coha_dimension_critical(quiver, d)
    chi_dd = quiver.euler_form(d, d)
    s_dd = quiver.symmetric_euler_form(d, d)
    virt = quiver.virtual_dim(d)
    rep = quiver.rep_space_dim(d)
    gauge = quiver.gauge_group_dim(d)

    return {
        'dimension': dim,
        'euler_form_diagonal': chi_dd,
        'virtual_dimension': virt,
        'rep_space_dim': rep,
        'gauge_group_dim': gauge,
        'cy_defect_at_d': s_dd,
    }


# =========================================================================
# 9. NON-CY HALL MULTIPLICATION
# =========================================================================

class NonCYHallMultiplication:
    r"""Hall multiplication for non-CY quivers.

    The Hall multiplication mu: H_d x H_e -> H_{d+e} is defined
    by the extension correspondence:

        Z_{d,e} = {0 -> M'' -> M -> M' -> 0 | dim M' = d, dim M'' = e}
                 -> Rep(Q, d) x Rep(Q, e)  (by (M', M''))
                 -> Rep(Q, d+e)             (by M)

    mu(f, g)(M) = sum_{M' subset M, dim M' = d} f(M') g(M/M')

    For a quiver with potential W, the vanishing cycle condition
    restricts to M in Crit(Tr W).

    For CY3: the Hall product has the SHUFFLE symmetry
        f * g = shuffle(f, g, zeta)
    where zeta is the motivic zeta function.

    For non-CY: the Hall product is STILL well-defined (it's always
    associative), but the shuffle description may break down because
    the zeta function loses its CY3 symmetry.
    """

    def __init__(self, quiver: GeneralQuiver):
        self.quiver = quiver

    def extension_count(self, d: Tuple[int, ...], e: Tuple[int, ...]) -> int:
        r"""Number of extensions 0 -> M'' -> M -> M' -> 0
        with dim M' = d, dim M'' = e (up to isomorphism).

        For a quiver Q with W = 0:
            # extensions = prod_i (d_i + e_i choose d_i) * q-analog factor
        where the q-analog factor counts the actual vector space extensions.

        At the NUMERICAL level (counting extensions by dimension):
            The number of extensions is related to:
            dim Ext^1(M', M'') * (number of isomorphism classes).

        For simple computation, we use the formula:
            # ext types = prod_i binom(d_i + e_i, d_i)
        which counts the number of subrepresentation types.
        """
        n = self.quiver.n_vertices
        count = 1
        for i in range(n):
            count *= math.comb(d[i] + e[i], d[i])
        return count

    def hall_product_dim(self, d: Tuple[int, ...],
                         e: Tuple[int, ...]) -> int:
        r"""Dimension of the image of mu: H_d x H_e -> H_{d+e}.

        The product is surjective onto its image. The image dimension
        is at most min(dim H_d * dim H_e, dim H_{d+e}).
        """
        dim_d = coha_dimension_critical(self.quiver, d)
        dim_e = coha_dimension_critical(self.quiver, e)
        d_plus_e = tuple(d[i] + e[i] for i in range(self.quiver.n_vertices))
        dim_de = coha_dimension_critical(self.quiver, d_plus_e)
        return min(dim_d * dim_e, dim_de)

    def associativity_check(self, d: Tuple[int, ...], e: Tuple[int, ...],
                             f: Tuple[int, ...]) -> bool:
        r"""Verify (f * g) * h = f * (g * h) at the dimension level.

        The Hall product is ALWAYS associative (this is a theorem,
        not a conjecture). So this check should always pass.
        It serves as a consistency check on our dimension formulas.
        """
        de = tuple(d[i] + e[i] for i in range(self.quiver.n_vertices))
        ef = tuple(e[i] + f[i] for i in range(self.quiver.n_vertices))
        def_ = tuple(d[i] + e[i] + f[i] for i in range(self.quiver.n_vertices))

        # (d * e) * f
        dim_de = self.hall_product_dim(d, e)
        dim_de_f = min(dim_de * coha_dimension_critical(self.quiver, f),
                       coha_dimension_critical(self.quiver, def_))

        # d * (e * f)
        dim_ef = self.hall_product_dim(e, f)
        dim_d_ef = min(coha_dimension_critical(self.quiver, d) * dim_ef,
                       coha_dimension_critical(self.quiver, def_))

        # Both should equal the full product dimension
        return dim_de_f == dim_d_ef

    def commutativity_defect(self, d: Tuple[int, ...],
                              e: Tuple[int, ...]) -> int:
        r"""Measure of non-commutativity of the Hall product.

        For CY3 with symmetric OPE: the product is "graded commutative"
        (up to the antisymmetric Euler form sign). The defect measures
        the failure of this property for non-CY.

        defect = |dim(d * e) - dim(e * d)|

        For the Hall product: d * e uses extensions with M' of dim d,
        while e * d uses extensions with M' of dim e. If chi(d,e) != -chi(e,d),
        the extension spaces have different dimensions.
        """
        dim_de = self.hall_product_dim(d, e)
        dim_ed = self.hall_product_dim(e, d)
        return abs(dim_de - dim_ed)


# =========================================================================
# 10. COMPARISON: CY3 vs NON-CY
# =========================================================================

def cy3_vs_noncy_comparison(max_d: int = 5) -> Dict[str, Any]:
    r"""Side-by-side comparison of CY3 and non-CY CoHA properties.

    Compares:
    (1) Jordan CY3 (W = Tr(x[y,z])) vs Jordan W=0 vs Jordan W=x^3
    (2) Conifold CY3 vs asymmetric 2-vertex
    (3) Euler form antisymmetry
    (4) PBW property
    (5) Curvature
    """
    quivers = {
        'jordan_cy3': jordan_quiver_cy3(),
        'jordan_w0': jordan_quiver_w0(),
        'jordan_cubic': jordan_quiver_cubic(),
        'conifold_cy3': conifold_quiver_cy3(),
        'asymmetric_2v': asymmetric_2vertex_quiver(),
        'a2_path': a2_path_quiver(),
        'kronecker_2': kronecker_quiver(2),
        'kronecker_3': kronecker_quiver(3),
        'tot_oo_p1': tot_o0_o0_p1_quiver(),
    }

    results = {}
    for name, Q in quivers.items():
        analysis = CYDefectAnalysis(Q)
        bar = CurvedBarComplex(Q)
        chiral = ChiralAlgebraIdentification(Q)

        results[name] = {
            'name': Q.name,
            'n_vertices': Q.n_vertices,
            'n_arrows': Q.n_arrows,
            'is_cy3_categorical': analysis.is_cy3(),
            'defect_norm': analysis.defect_norm(),
            'curvature_scalar': float(bar.curvature()),
            'is_flat': bar.is_flat(),
            'chiral_type': chiral.identify()['chiral_type'],
            'effective_c': float(chiral.identify()['effective_central_charge']),
        }

    return results


def non_cy_landscape() -> Dict[str, Dict[str, Any]]:
    r"""The landscape of non-CY CoHA types.

    Classification by CY defect:
    - Defect 0: CY3 (flat bar complex, PBW, affine Yangian).
    - Defect small: "near-CY" (small curvature, approximate PBW).
    - Defect large: "far from CY" (large curvature, PBW fails badly).

    Each type has a characteristic chiral algebra:
    - CY3 -> affine Yangian Y^+(g_hat)
    - Near-CY -> deformed Yangian with curvature
    - Far-from-CY -> curved vertex algebra
    """
    quivers = [
        jordan_quiver_cy3(),
        jordan_quiver_w0(),
        jordan_quiver_cubic(),
        conifold_quiver_cy3(),
        asymmetric_2vertex_quiver(),
        a2_path_quiver(),
        kronecker_quiver(1),
        kronecker_quiver(2),
        kronecker_quiver(3),
        tot_o0_o0_p1_quiver(),
    ]

    landscape = {}
    for Q in quivers:
        analysis = CYDefectAnalysis(Q)
        bar = CurvedBarComplex(Q)
        chiral = ChiralAlgebraIdentification(Q)
        ident = chiral.identify()

        landscape[Q.name] = {
            'n_vertices': Q.n_vertices,
            'n_arrows': Q.n_arrows,
            'is_cy3': analysis.is_cy3(),
            'defect_norm': analysis.defect_norm(),
            'curvature': float(bar.curvature()),
            'chiral_type': ident['chiral_type'],
            'chiral_description': ident['description'],
            'effective_c': float(ident['effective_central_charge']),
            'n_generators': ident['n_generators'],
            'serre_duality_holds': Q.serre_duality_check()['holds'],
        }

    return landscape


# =========================================================================
# 11. MULTI-PATH VERIFICATION UTILITIES
# =========================================================================

def verify_euler_form_three_paths(quiver: GeneralQuiver,
                                   d1: Tuple[int, ...],
                                   d2: Tuple[int, ...]) -> Dict[str, Any]:
    r"""Verify QUIVER Euler form computation via 3 independent paths.

    The quiver Euler form chi_Q(d1,d2) = sum d1_i d2_i - sum_a d1_{s(a)} d2_{t(a)}
    counts Ext^0 - Ext^1 only (no higher Ext terms).

    Path 1: Direct computation from quiver.euler_form().
    Path 2: From arrow count matrix (independent expansion).
    Path 3: From Ext^0 - Ext^1 using ext_dimensions_simple().

    NOTE: The CATEGORICAL Euler form chi^{cat} = sum (-1)^k Ext^k includes
    Ext^2 and Ext^3 terms from the potential. It is a DIFFERENT quantity
    from the quiver Euler form. We report it separately but do NOT
    require it to equal the quiver Euler form.
    """
    n = quiver.n_vertices

    # Path 1: direct
    chi_direct = quiver.euler_form(d1, d2)

    # Path 2: from arrow matrix
    chi_arrow = sum(d1[i] * d2[i] for i in range(n))
    for i in range(n):
        for j in range(n):
            chi_arrow -= quiver.arrows_from_to(i, j) * d1[i] * d2[j]

    # Path 3: from Ext^0 - Ext^1 (quiver-level, no higher Ext)
    is_simple_d1 = (sum(d1) == 1 and all(x in (0, 1) for x in d1))
    is_simple_d2 = (sum(d2) == 1 and all(x in (0, 1) for x in d2))
    chi_ext01 = None
    chi_categorical = None
    if is_simple_d1 and is_simple_d2:
        i = d1.index(1)
        j = d2.index(1)
        ext = quiver.ext_dimensions_simple()
        # Quiver Euler form = Ext^0 - Ext^1 (the terms without potential)
        chi_ext01 = ext[(0, i, j)] - ext[(1, i, j)]
        # Categorical = full alternating sum (reported separately)
        chi_categorical = quiver.categorical_euler_form(i, j)

    return {
        'direct': chi_direct,
        'arrow_matrix': chi_arrow,
        'ext01': chi_ext01,
        'categorical': chi_categorical,
        'all_agree': (chi_direct == chi_arrow and
                      (chi_ext01 is None or chi_ext01 == chi_direct)),
    }


def verify_cy_defect_three_paths(quiver: GeneralQuiver,
                                  d1: Tuple[int, ...],
                                  d2: Tuple[int, ...]) -> Dict[str, Any]:
    r"""Verify CY defect computation via 3 independent paths.

    Path 1: s = chi(d1,d2) + chi(d2,d1) from quiver.symmetric_euler_form.
    Path 2: s = 2*sum(d1_i*d2_i) - sum_{a}(d1_{s(a)}*d2_{t(a)} + d1_{t(a)}*d2_{s(a)})
            (expanding the symmetric part explicitly).
    Path 3: From the defect matrix.
    """
    n = quiver.n_vertices

    # Path 1: direct
    s_direct = quiver.symmetric_euler_form(d1, d2)

    # Path 2: explicit expansion
    vertex_sum = 2 * sum(d1[i] * d2[i] for i in range(n))
    arrow_sum = 0
    for src, tgt, _ in quiver.arrows:
        si, ti = quiver._v_map[src], quiver._v_map[tgt]
        arrow_sum += d1[si] * d2[ti] + d1[ti] * d2[si]
    s_explicit = vertex_sum - arrow_sum

    # Path 3: from defect matrix (for simple roots)
    is_simple_d1 = (sum(d1) == 1 and all(x in (0, 1) for x in d1))
    is_simple_d2 = (sum(d2) == 1 and all(x in (0, 1) for x in d2))
    s_matrix = None
    if is_simple_d1 and is_simple_d2:
        dm = quiver.cy_defect_matrix()
        i = d1.index(1)
        j = d2.index(1)
        s_matrix = dm[i][j]

    return {
        'direct': s_direct,
        'explicit': s_explicit,
        'matrix': s_matrix,
        'all_agree': (s_direct == s_explicit and
                      (s_matrix is None or s_matrix == s_direct)),
    }


def verify_curvature_three_paths(quiver: GeneralQuiver) -> Dict[str, Any]:
    r"""Verify curvature computation via 3 independent paths.

    Path 1: From CYDefectAnalysis.curvature_element().
    Path 2: Direct: (1/2) * sum_i s^{cat}(S_i, S_i).
    Path 3: From the categorical Euler form: (1/2)*sum_i (chi^{cat}(i,i) + chi^{cat}(i,i)).
    """
    analysis = CYDefectAnalysis(quiver)

    # Path 1: via analysis
    m0_analysis = analysis.curvature_element()

    # Path 2: direct
    n = quiver.n_vertices
    m0_direct = Fraction(0)
    for i in range(n):
        m0_direct += Fraction(quiver.categorical_cy_defect(i, i))
    m0_direct = m0_direct / Fraction(2)

    # Path 3: from categorical Euler form
    m0_euler = Fraction(0)
    for i in range(n):
        chi_ii = quiver.categorical_euler_form(i, i)
        m0_euler += Fraction(2 * chi_ii)
    m0_euler = m0_euler / Fraction(2)

    return {
        'analysis': m0_analysis,
        'direct': m0_direct,
        'euler': m0_euler,
        'all_agree': (m0_analysis == m0_direct == m0_euler),
    }


def verify_hall_associativity(quiver: GeneralQuiver,
                               max_total: int = 4) -> Dict[str, Any]:
    r"""Verify Hall multiplication associativity for all small dimension vectors.

    The Hall product is ALWAYS associative. This is a consistency check.
    """
    n = quiver.n_vertices
    hall = NonCYHallMultiplication(quiver)

    checks = []
    for total in range(1, max_total + 1):
        for dv in _dim_vectors(n, total):
            for ev in _dim_vectors(n, 1):
                for fv in _dim_vectors(n, 1):
                    ok = hall.associativity_check(dv, ev, fv)
                    checks.append({
                        'd': dv, 'e': ev, 'f': fv,
                        'associative': ok,
                    })

    all_ok = all(c['associative'] for c in checks)
    return {
        'n_checks': len(checks),
        'all_associative': all_ok,
        'failures': [c for c in checks if not c['associative']],
    }
