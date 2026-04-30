"""
Diagonal-divisor modular lattices for the primitive Gritsenko-Nikulin denominator Delta_5.

Implements the lattice structures from:
  "A Borcherds lift of the weak Jacobi form phi_{0,1}, generalized
   Borcherds-Kac-Moody superalgebras and the primitive Gritsenko-Nikulin denominator Delta_5"
   (Lorgat, 2020)

The ambient lattice Lambda^{3,2} of signature (3,2) decomposes as
Lambda^{1,1} + Lambda^{1,1} + [2], realised inside the exterior square
of a rank-4 free Z-module via the pfaffian inner product.  The
hyperbolic sublattice Lambda^{2,1} = Z f_2 + Z f_3 + Z f_{-2} and its
type-II sublattice Lambda^{2,1}_{II} carry the reflection groups and
fundamental polyhedra whose Weyl-Kac denominator identity gives the
infinite product for Delta_5.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray
from fractions import Fraction
from itertools import permutations
from typing import Sequence


# ---------------------------------------------------------------------------
# 1. Gram matrices
# ---------------------------------------------------------------------------

def gram_hyperbolic_plane() -> NDArray[np.int64]:
    """Gram matrix of the standard integral hyperbolic plane Lambda^{1,1}.

    Inner product: (e, f) = -1 with (e,e) = (f,f) = 0.
    Convention: off-diagonal -1 (matching the paper's
    \\begin{pmatrix} 0 & -1 \\\\ -1 & 0 \\end{pmatrix}).
    """
    return np.array([[0, -1],
                     [-1, 0]], dtype=np.int64)


def gram_lambda_32() -> NDArray[np.int64]:
    r"""Gram matrix of Lambda^{3,2} = Lambda^{1,1} + Lambda^{1,1} + [2].

    Basis ordering: (f_1, f_2, f_3, f_{-2}, f_{-1}) as defined in the
    paper (section 3).  The first copy of Lambda^{1,1} is spanned by
    (f_1, f_{-1}), the second by (f_2, f_{-2}), and [2] by f_3.

    Returns:
        5x5 integral symmetric matrix of signature (3,2).
    """
    G = np.zeros((5, 5), dtype=np.int64)
    # Lambda^{1,1} copy 1: f_1, f_{-1}  (indices 0, 4)
    G[0, 4] = G[4, 0] = -1
    # Lambda^{1,1} copy 2: f_2, f_{-2}  (indices 1, 3)
    G[1, 3] = G[3, 1] = -1
    # [2]: f_3 (index 2)
    G[2, 2] = 2
    return G


def gram_lambda_21() -> NDArray[np.int64]:
    r"""Gram matrix of the hyperbolic sublattice Lambda^{2,1}.

    Lambda^{2,1} = Lambda^{1,1} + [2] = Z f_2 + Z f_3 + Z f_{-2}
    with basis ordering (f_2, f_3, f_{-2}).

    Returns:
        3x3 integral symmetric matrix of signature (2,1).
    """
    G = np.zeros((3, 3), dtype=np.int64)
    # f_2 <-> f_{-2} pairing from Lambda^{1,1}
    G[0, 2] = G[2, 0] = -1
    # f_3 self-pairing from [2]
    G[1, 1] = 2
    return G


def gram_lambda_21_II() -> NDArray[np.int64]:
    r"""Gram matrix of Lambda^{2,1}_{II} in the basis (delta_1, delta_2, delta_3).

    delta_1 = 2 f_2 - f_3
    delta_2 = 2 f_{-2} - f_3
    delta_3 = f_3

    These are the type-II generators; the lattice Lambda^{2,1}_{II}
    consists of elements m f_2 + l f_3 + n f_{-2} with m, n even.

    Returns:
        The 3x3 Gram matrix  ((2,-2,-2),(-2,2,-2),(-2,-2,2)).
    """
    return np.array([[2, -2, -2],
                     [-2, 2, -2],
                     [-2, -2, 2]], dtype=np.int64)


def verify_gram_II_from_ambient() -> NDArray[np.int64]:
    """Compute the Gram matrix of (delta_1, delta_2, delta_3) directly
    from the ambient Lambda^{2,1} inner product, as a cross-check.

    delta_i are expressed in the (f_2, f_3, f_{-2}) basis of Lambda^{2,1}.
    """
    G21 = gram_lambda_21()
    # delta_1 = 2 f_2 - f_3   -> (2, -1, 0)
    # delta_2 = 2 f_{-2} - f_3 -> (0, -1, 2)
    # delta_3 = f_3            -> (0, 1, 0)
    deltas = np.array([[2, -1, 0],
                       [0, -1, 2],
                       [0,  1, 0]], dtype=np.int64)
    return deltas @ G21 @ deltas.T


# ---------------------------------------------------------------------------
# 2. Lattice classes
# ---------------------------------------------------------------------------

# Basis label conventions:
#   Lambda^{3,2}: indices 0..4 = (f_1, f_2, f_3, f_{-2}, f_{-1})
#   Lambda^{2,1}: indices 0..2 = (f_2, f_3, f_{-2})
#   Lambda^{2,1}_{II} (delta basis): indices 0..2 = (delta_1, delta_2, delta_3)

BASIS_LABELS_32 = ("f_1", "f_2", "f_3", "f_{-2}", "f_{-1}")
BASIS_LABELS_21 = ("f_2", "f_3", "f_{-2}")
BASIS_LABELS_II = ("delta_1", "delta_2", "delta_3")


def inner_product(v: NDArray, w: NDArray, G: NDArray) -> int | np.int64:
    """Compute (v, w) with respect to Gram matrix G."""
    return int(v @ G @ w)


def norm_sq(v: NDArray, G: NDArray) -> int | np.int64:
    """Compute (v, v) with respect to Gram matrix G."""
    return inner_product(v, v, G)


# ---------------------------------------------------------------------------
# 3. Embedding of Lambda^{2,1} into Lambda^{3,2}
# ---------------------------------------------------------------------------

def embedding_21_into_32() -> NDArray[np.int64]:
    r"""Return the 3x5 matrix E such that if v is a vector in the
    (f_2, f_3, f_{-2}) basis of Lambda^{2,1}, then E^T v gives the
    corresponding vector in the (f_1, f_2, f_3, f_{-2}, f_{-1}) basis
    of Lambda^{3,2}.

    Concretely, E maps:
        f_2  -> (0,1,0,0,0)
        f_3  -> (0,0,1,0,0)
        f_{-2} -> (0,0,0,1,0)

    Returns:
        3x5 integer matrix (row i is the image of the i-th basis vector).
    """
    E = np.zeros((3, 5), dtype=np.int64)
    E[0, 1] = 1   # f_2
    E[1, 2] = 1   # f_3
    E[2, 3] = 1   # f_{-2}
    return E


def embedding_II_into_21() -> NDArray[np.int64]:
    r"""Return the 3x3 change-of-basis matrix C such that if v is a
    vector in the (delta_1, delta_2, delta_3) basis of Lambda^{2,1}_{II},
    then C^T v gives the corresponding vector in the (f_2, f_3, f_{-2})
    basis of Lambda^{2,1}.

    delta_1 = 2 f_2 - f_3       -> (2, -1, 0)
    delta_2 = 2 f_{-2} - f_3    -> (0, -1, 2)
    delta_3 = f_3                -> (0,  1, 0)
    """
    return np.array([[2, -1, 0],
                     [0, -1, 2],
                     [0,  1, 0]], dtype=np.int64)


def delta_coords_in_f_basis() -> dict[str, NDArray[np.int64]]:
    """Return delta_1, delta_2, delta_3 as vectors in the (f_2, f_3, f_{-2}) basis."""
    C = embedding_II_into_21()
    return {
        "delta_1": C[0],
        "delta_2": C[1],
        "delta_3": C[2],
    }


# ---------------------------------------------------------------------------
# 4. Reflection group generators
# ---------------------------------------------------------------------------

def reflection_matrix(alpha: NDArray, G: NDArray) -> NDArray:
    r"""Compute the matrix of the reflection s_alpha in O(Lambda, G):

        s_alpha(x) = x - 2 * (x, alpha) / (alpha, alpha) * alpha

    For alpha with (alpha, alpha) = 2 this simplifies to
        s_alpha(x) = x - (x, alpha) * alpha.

    Args:
        alpha: Coordinates of the root in the given basis.
        G: Gram matrix of the lattice in that basis.

    Returns:
        Integer matrix of the reflection (n x n where n = len(alpha)).
    """
    n = len(alpha)
    aa = int(alpha @ G @ alpha)
    if aa == 0:
        raise ValueError("Cannot reflect in a null vector")
    # s_alpha(x)_i = x_i - (2/aa) * (sum_j x_j (G alpha)_j) * alpha_i
    # In matrix form: S_{ij} = delta_{ij} - (2/aa) * alpha_i * (G alpha)_j
    I = np.eye(n, dtype=np.int64)
    Ga = G @ alpha  # the vector (G alpha)_j = (e_j, alpha)
    # S = I - (2/aa) * outer(alpha, G @ alpha)
    # For integer arithmetic when aa | 2*(alpha_i * (G alpha)_j):
    S = aa * I - 2 * np.outer(alpha, Ga)
    if aa != 1:
        assert np.all(S % aa == 0), "Reflection does not preserve lattice"
        S = S // aa
    return S.astype(np.int64)


def type_II_reflection_generators() -> list[NDArray[np.int64]]:
    r"""Generators of W^{(2)}(Lambda^{2,1}_{II}).

    Returns reflections s_{delta_i} for i=1,2,3 as 3x3 integer matrices
    in the (delta_1, delta_2, delta_3) basis.
    """
    G = gram_lambda_21_II()
    e1 = np.array([1, 0, 0], dtype=np.int64)
    e2 = np.array([0, 1, 0], dtype=np.int64)
    e3 = np.array([0, 0, 1], dtype=np.int64)
    return [reflection_matrix(e1, G),
            reflection_matrix(e2, G),
            reflection_matrix(e3, G)]


def type_I_reflection_generators_f_basis() -> list[NDArray[np.int64]]:
    r"""Generators of W^{(2)}(Lambda^{2,1}_I) as reflections in the
    (f_2, f_3, f_{-2}) basis of Lambda^{2,1}.

    P_{I,prim} = {f_2 - f_3, f_{-2} - f_2, f_2 + f_3}.
    """
    G = gram_lambda_21()
    roots = [
        np.array([1, -1, 0], dtype=np.int64),   # f_2 - f_3
        np.array([-1, 0, 1], dtype=np.int64),    # f_{-2} - f_2
        np.array([1, 1, 0], dtype=np.int64),     # f_2 + f_3
    ]
    return [reflection_matrix(r, G) for r in roots]


def full_reflection_generators_f_basis() -> list[NDArray[np.int64]]:
    r"""Generators of W^{(2)}(Lambda^{2,1}) = Orth(Lambda^{2,1})_+ as
    reflections in the (f_2, f_3, f_{-2}) basis.

    P_{prim} = {f_2 - f_3, f_{-2} - f_2, f_3}.
    """
    G = gram_lambda_21()
    roots = [
        np.array([1, -1, 0], dtype=np.int64),   # f_2 - f_3
        np.array([-1, 0, 1], dtype=np.int64),    # f_{-2} - f_2
        np.array([0, 1, 0], dtype=np.int64),     # f_3
    ]
    return [reflection_matrix(r, G) for r in roots]


def automorphism_generators_P_II_f_basis() -> list[NDArray[np.int64]]:
    r"""Generators of Aut(P_{II}) = S_3 as reflections in the
    (f_2, f_3, f_{-2}) basis.

    Generated by s_{f_2 - f_3} and s_{f_{-2} - f_2}.
    """
    G = gram_lambda_21()
    return [
        reflection_matrix(np.array([1, -1, 0], dtype=np.int64), G),
        reflection_matrix(np.array([-1, 0, 1], dtype=np.int64), G),
    ]


def enumerate_S3_from_generators(gens: list[NDArray[np.int64]],
                                  max_iter: int = 100) -> list[NDArray[np.int64]]:
    """Enumerate all group elements generated by a list of involutory
    generators by iterated multiplication, up to max_iter rounds.

    Returns a list of distinct integer matrices forming the group.
    """
    def mat_key(M: NDArray) -> tuple:
        return tuple(M.flatten())

    seen: set[tuple] = set()
    n = gens[0].shape[0]
    elements = [np.eye(n, dtype=np.int64)]
    seen.add(mat_key(elements[0]))
    queue = list(elements)

    for _ in range(max_iter):
        new_queue = []
        for g in queue:
            for s in gens:
                prod = (g @ s).astype(np.int64)
                k = mat_key(prod)
                if k not in seen:
                    seen.add(k)
                    elements.append(prod)
                    new_queue.append(prod)
        if not new_queue:
            break
        queue = new_queue

    return elements


# ---------------------------------------------------------------------------
# 5. Weyl vector rho
# ---------------------------------------------------------------------------

def weyl_vector_delta_basis() -> NDArray:
    r"""Weyl vector rho in the (delta_1, delta_2, delta_3) basis.

    rho = (1/2) delta_1 + (1/2) delta_2 + (1/2) delta_3.

    Returns:
        Array of Fraction values [1/2, 1/2, 1/2].
    """
    return np.array([Fraction(1, 2), Fraction(1, 2), Fraction(1, 2)],
                    dtype=object)


def weyl_vector_f_basis() -> NDArray:
    r"""Weyl vector rho in the (f_2, f_3, f_{-2}) basis.

    rho = f_2 - (1/2) f_3 + f_{-2}.

    Derivation: rho = (1/2)(2f_2 - f_3) + (1/2)(2f_{-2} - f_3) + (1/2)(f_3)
              = f_2 - (1/2) f_3 + f_{-2}.

    Returns:
        Array of Fraction values [1, -1/2, 1].
    """
    return np.array([Fraction(1, 1), Fraction(-1, 2), Fraction(1, 1)],
                    dtype=object)


def verify_weyl_vector() -> bool:
    r"""Verify that (rho, delta_i) = -1 for each i = 1, 2, 3.

    The defining property of the lattice Weyl vector is
        (rho, delta_i) = -(delta_i, delta_i) / 2 = -1.
    """
    G_II = gram_lambda_21_II()
    rho = weyl_vector_delta_basis()
    for i in range(3):
        e_i = np.zeros(3, dtype=object)
        e_i[i] = Fraction(1, 1)
        ip = sum(rho[j] * G_II[j, k] * e_i[k]
                 for j in range(3) for k in range(3))
        if ip != Fraction(-1, 1):
            return False
    return True


def weyl_vector_norm_sq() -> Fraction:
    r"""Compute (rho, rho) using the Lambda^{2,1} inner product.

    rho = (1, -1/2, 1) in (f_2, f_3, f_{-2}) basis.
    G_{21} = ((0,0,-1),(0,2,0),(-1,0,0)).
    (rho, rho) = 2*(-1/2)^2 + 2*(1)*(1)*(-1) = 1/2 - 2 = -3/2.
    """
    G = gram_lambda_21()
    rho = weyl_vector_f_basis()
    result = Fraction(0)
    for i in range(3):
        for j in range(3):
            result += rho[i] * G[i, j] * rho[j]
    return result


# ---------------------------------------------------------------------------
# 6. Fundamental polyhedra and cones
# ---------------------------------------------------------------------------

def polyhedron_prim(which: str = "II") -> list[NDArray[np.int64]]:
    r"""Primitive orthogonal vectors defining a fundamental polyhedron.

    All vectors are in the (f_2, f_3, f_{-2}) basis of Lambda^{2,1}.

    Args:
        which: One of "full", "I", or "II".

    Returns:
        List of primitive vectors delta such that (delta, delta) = 2
        and the polyhedron is the intersection of half-spaces
        {x : (x, delta) <= 0}.
    """
    if which == "full":
        # P_{prim} = {f_2 - f_3, f_{-2} - f_2, f_3}
        return [
            np.array([1, -1, 0], dtype=np.int64),
            np.array([-1, 0, 1], dtype=np.int64),
            np.array([0, 1, 0], dtype=np.int64),
        ]
    elif which == "I":
        # P_{I,prim} = {f_2 - f_3, f_{-2} - f_2, f_2 + f_3}
        return [
            np.array([1, -1, 0], dtype=np.int64),
            np.array([-1, 0, 1], dtype=np.int64),
            np.array([1, 1, 0], dtype=np.int64),
        ]
    elif which == "II":
        # P_{II,prim} = {delta_1, delta_2, delta_3}
        #             = {2f_2 - f_3, 2f_{-2} - f_3, f_3}
        return [
            np.array([2, -1, 0], dtype=np.int64),
            np.array([0, -1, 2], dtype=np.int64),
            np.array([0, 1, 0], dtype=np.int64),
        ]
    else:
        raise ValueError(f"Unknown polyhedron type: {which!r}")


def is_in_half_space(x: NDArray, delta: NDArray, G: NDArray) -> bool:
    """Check whether x lies in the closed half-space H_{delta,+},
    i.e., (x, delta) <= 0."""
    ip = sum(x[i] * G[i, j] * delta[j]
             for i in range(len(x)) for j in range(len(x)))
    return ip <= 0


def is_in_polyhedron(x: NDArray, prims: list[NDArray], G: NDArray) -> bool:
    """Check whether x lies in the fundamental polyhedron defined by
    the intersection of half-spaces H_{delta,+} for delta in prims."""
    return all(is_in_half_space(x, d, G) for d in prims)


def cone_embedding_check() -> tuple[bool, bool]:
    r"""Verify the sequence of cone embeddings (Proposition from sec. 4):

        Delta(Lambda^{2,1}_{II})^*_+ \subset \overline{Cone(Lambda^{2,1})_+}
                                      \subset Delta(Lambda^{2,1}_{II})_+

    The positive cone Delta_{II,+} is generated by delta_1, delta_2, delta_3
    (positive real span).  Its dual cone Delta_{II,+}^* = {x : (x, delta_i) <= 0
    for all i}.

    The light cone Cone(Lambda^{2,1})_+ = {x : (x,x) < 0} (a connected
    component chosen so that rho lies in it).

    We verify:
    1. rho in Delta_{II,+}^* (by the Weyl vector property)
    2. rho in Cone_+ (by checking (rho, rho) < 0)

    Returns:
        (rho_in_dual_cone, rho_in_light_cone)
    """
    rho = weyl_vector_f_basis()
    G = gram_lambda_21()

    # Check rho in dual cone: (rho, delta_i) <= 0 for each delta_i
    prims = polyhedron_prim("II")
    in_dual = is_in_polyhedron(rho, prims, G)

    # Check (rho, rho) < 0  (light cone condition)
    rho_sq = weyl_vector_norm_sq()
    in_cone = rho_sq < 0

    return (in_dual, in_cone)


def primitive_elements_at_infinity() -> list[NDArray[np.int64]]:
    r"""The three primitive null elements a_0 in Lambda^{2,1}_{II} cap R_{>0} P_{II}.

    These are the primitive elements with (a_0, a_0) = 0 at the vertices
    at infinity of the hyperbolic triangle P_{II}.  The group Aut(P_{II})
    = S_3 acts transitively on them.

    In the (f_2, f_3, f_{-2}) basis:
        2 f_2, 2 f_{-2}, 2 f_2 - 2 f_3 + 2 f_{-2}.
    """
    return [
        np.array([2, 0, 0], dtype=np.int64),
        np.array([0, 0, 2], dtype=np.int64),
        np.array([2, -2, 2], dtype=np.int64),
    ]


def verify_null_elements() -> bool:
    """Verify that each primitive element at infinity has norm-squared 0."""
    G = gram_lambda_21()
    for a0 in primitive_elements_at_infinity():
        if norm_sq(a0, G) != 0:
            return False
    return True


# ---------------------------------------------------------------------------
# 7. Signature verification
# ---------------------------------------------------------------------------

def signature(G: NDArray) -> tuple[int, int, int]:
    """Compute the signature (p, q, z) of a real symmetric bilinear form
    given by Gram matrix G.

    Returns:
        (num_positive, num_negative, num_zero) eigenvalue counts.
    """
    eigs = np.linalg.eigvalsh(G.astype(np.float64))
    tol = 1e-10
    p = int(np.sum(eigs > tol))
    q = int(np.sum(eigs < -tol))
    z = int(np.sum(np.abs(eigs) <= tol))
    return (p, q, z)


# ---------------------------------------------------------------------------
# 8. Lattice membership predicates
# ---------------------------------------------------------------------------

def is_in_lambda_21_I(m: int, l: int, n: int) -> bool:
    r"""Check if m f_2 + l f_3 + n f_{-2} lies in Lambda^{2,1}_I.

    Condition: m + l + n = 0 mod 2.
    """
    return (m + l + n) % 2 == 0


def is_in_lambda_21_II(m: int, l: int, n: int) -> bool:
    r"""Check if m f_2 + l f_3 + n f_{-2} lies in Lambda^{2,1}_{II}.

    Condition: m = 0 mod 2 and n = 0 mod 2.
    """
    return m % 2 == 0 and n % 2 == 0


def dual_lattice_lambda_21_II() -> str:
    r"""Description of (Lambda^{2,1}_{II})^*.

    (Lambda^{2,1}_{II})^* = Z (1/2) f_2 + Z (1/2) f_3 + Z (1/2) f_{-2}
                           = (1/2) Lambda^{2,1}.
    """
    return "(1/2) Lambda^{2,1} = Z (1/2)f_2 + Z (1/2)f_3 + Z (1/2)f_{-2}"


# ---------------------------------------------------------------------------
# 9. Subgroup indices
# ---------------------------------------------------------------------------

def reflection_subgroup_indices() -> dict[str, int]:
    r"""Indices of reflection subgroups in Orth(Lambda^{2,1})_+.

    From the paper (section 4):
        [Orth(Lambda^{2,1})_+ : W^{(2)}(Lambda^{2,1}_I)] = 2
        [Orth(Lambda^{2,1})_+ : W^{(2)}(Lambda^{2,1}_{II})] = 6

    Equivalently:
        |Aut(P)| = 1  (trivial)
        |Aut(P_I)| = 2  (generated by s_{f_3})
        |Aut(P_{II})| = 6  (= S_3, generated by s_{f_2-f_3}, s_{f_{-2}-f_2})

    These are consistent: the index equals the order of the automorphism
    group of the fundamental polyhedron.
    """
    return {
        "W^{(2)}(Lambda^{2,1})": 1,
        "W^{(2)}(Lambda^{2,1}_I)": 2,
        "W^{(2)}(Lambda^{2,1}_{II})": 6,
    }
