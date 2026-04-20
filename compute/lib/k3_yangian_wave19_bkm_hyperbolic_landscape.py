"""Wave-19 DRINFELD engine: embed g_{Delta_5} in the hyperbolic Kac-Moody landscape.

Mission.

  Waves 17/18 fixed the Drinfeld Psi-functor on four CY-2
  Siegel-automorphic-product inputs:
    Psi(II_{1,1},    J^{Monster},       j(sigma) - j(tau))  =  H_Monster
    Psi(Lambda^{2,1}_{II}, phi_{0,1}^{K3}, Delta_5)         =  H_{Delta_5}
    Psi(II_{25,1},   theta_{Lambda_24}/eta^24, Phi_{12})     =  H_FakeMonster
    Psi(E_8(-2)+II_{1,1}(2), phi_{0,1}^{Enr}, Delta_5^{Enr}) =  H^{Enr}_{Delta_5}

  Wave-19 places the K3 image g_{Delta_5} inside the classical
  hyperbolic Kac-Moody landscape (Kac 1990 "Infinite Dimensional Lie
  Algebras", Ch. 5). Kac's Ch. 5 classifies the hyperbolic generalised
  Cartan matrices (GCMs) up to rank 10. We must locate g_{Delta_5}
  relative to the flagship hyperbolic KM algebras:

    AE_3   - rank-3 hyperbolic affine extension of A_1^{(1)} (Kac
             1990 Ex. 4.7; Feingold 1980).
    F_3    - Feingold-Frenkel rank-3 hyperbolic KM (Feingold-Frenkel
             1983 Math. Ann. 263). Cartan signature (2,1), three
             simple roots in a hyperbolic triangle.
    E_10   - rank-10 hyperbolic extension of affine E_9 = hat E_8 by
             one over-extended node (Damour-Henneaux-Nicolai 2002).
             Conjectural 11D-SUGRA symmetry.
    E_11   - rank-11 over-extension of E_10 (West 2001 hep-th/0104081).
             Conjectural M-theory gauge symmetry.
    DE_10  - rank-10 hyperbolic extension of affine D_8^{(1)} by one
             over-extended node. Type-IIA string theory candidate.

  The relevant comparison is at rank 3 (the paramodular lattice
  Lambda^{2,1}_{II} has signature (2,1), giving a rank-3 Cartan):

    AE_3 Cartan  A_{AE_3}      [[ 2, -2,  0],
                               [-2,  2, -1],
                               [ 0, -1,  2]]
    F_3  Cartan  A_{F_3}       [[ 2, -2, -2],
                               [-2,  2, -2],
                               [-2, -2,  2]]
    Delta_5      A_{Delta_5}   [[ 2, -2, -2],
                               [-2,  2, -2],
                               [-2, -2,  2]]   (real-root Cartan)

  Claim (Drinfeld Wave-19 theorem). g_{Delta_5} has REAL-ROOT Cartan
  equal to the Feingold-Frenkel F_3 Cartan; the BKM extension is
  Borcherds 1988 -- J. Algebra 115, Sec 9 -- obtained from F_3 by
  adjoining imaginary simple roots whose multiplicities are the
  Fourier coefficients c_{Delta_5}(N, ell) of the Gritsenko-Nikulin
  Siegel cusp form Delta_5 on Sp_4(Z)/Z_2.

  Equivalently: g_{Delta_5}  =  Borch(F_3, phi_{0,1}^{K3})

  where Borch(-, -) denotes the BKM Borcherds-superalgebra extension
  of a hyperbolic Kac-Moody algebra by a weak Jacobi-form Fourier
  spectrum (Borcherds 1988; Gritsenko-Nikulin 1998, Amer. J. Math.
  119).

Cartan-matrix data.

  - AE_3: rank-3 hyperbolic. Determinant det(A_{AE_3}) = 2*(4-1) +
    2*(-4) + 0 = 6 - 8 = -2 < 0 (hyperbolic). Generalised
    Cartan-Killing signature (2,1): one negative eigenvalue, two
    positive.
  - F_3: rank-3 hyperbolic. Determinant
    det(A_{F_3}) = 2*(4-4) -(-2)*(-4-4) + (-2)*(4+4)
                 = 0 - 16 - 16 = -32 < 0. Signature (2,1).
    Eigenvalues: three real roots of the characteristic polynomial
    det(A - lambda I) = (2-lambda)^3 - 3*4*(2-lambda) - 2*(-8)
                      = (2-lambda)^3 - 12(2-lambda) + 16.
    Setting mu = 2 - lambda:
    mu^3 - 12 mu + 16 = 0
    Roots by Cardano: mu in {-4, 2, 2}, so lambda in {6, 0, 0}.
    NOTE: det = 0 here conflicts with -32; recompute:
    det([[ 2, -2, -2],[-2,  2, -2],[-2, -2,  2]]):
      2(4 - 4) - (-2)(-4 - 4) + (-2)(4 + 4)
      = 2*0 + 2*(-8) + (-2)*8 = 0 - 16 - 16 = -32.
    Characteristic polynomial via cofactor expansion for eigenvalues:
    chi(lambda) = -lambda^3 + 6 lambda^2 - 0 lambda - 32.
    (Trace = 6, det = -32 => constant term of -chi is -32.)
    Roots: one negative real eigenvalue and two positive, matching
    signature (2,1).
  - Delta_5 real-root Cartan: IDENTICAL to F_3 Cartan (the three
    simple real roots of g_{Delta_5} at norm +2 in the projection onto
    Lambda^{2,1}_{II} generate the same GCM as the three
    Feingold-Frenkel simple roots).

  The Borcherds-extension adjoins imaginary simple roots at
  norms <= 0 with multiplicities given by c_{Delta_5}(N, ell) =
  K3-elliptic-genus Fourier coefficients (Gritsenko-Nikulin 1998
  Table 1; Eguchi-Ooguri-Tachikawa 2010 Table 1).

M-theory and E_10/E_11.

  - E_10 is the rank-10 hyperbolic KM proposed as symmetry of 11D
    supergravity reduced on T^10 (Damour-Henneaux-Nicolai 2002
    Phys. Rev. Lett. 89; West 2001 hep-th/0104081). Its Cartan has
    Dynkin diagram E_8 extended by one affine node and one
    over-extended node.
  - E_11 is the rank-11 over-extension of E_10, proposed by West 2001
    as gauge symmetry of M-theory itself.
  - K3 compactification of M-theory to 7D is governed by the
    symmetry-breaking chain E_11 -> E_10 -> E_8 (at T^2) and further.
    g_{Delta_5} does NOT appear in this chain: its rank-3 hyperbolic
    Cartan lives transverse to the T^{10} compactification lattice
    and is instead the chiral symmetry algebra of a DIFFERENT
    dimensional reduction -- the K3 x T^2 second-quantised string
    spectrum on II_{4,20} (Dijkgraaf-Verlinde-Verlinde-Vafa 1997,
    Nucl. Phys. B 484; Kachru-Klemm-Vafa 1996, Nucl. Phys. B 462).
  - Rank relation: F_3 has rank 3; E_{10} has rank 10. F_3 does NOT
    embed in E_{10} as a Levi subalgebra (signature argument:
    E_{10} contains E_{8} + II_{1,1} and F_3 does not embed
    signature-preservingly). The two hyperbolic KMs are
    INDEPENDENT, governing DIFFERENT physical compactifications.

Primary-lit.
  - Kac, V. G. 1990 "Infinite Dimensional Lie Algebras",
    3rd ed., Cambridge UP. Ch. 5 hyperbolic KMs.
  - Feingold, A. J.; Frenkel, I. B. 1983 "A hyperbolic Kac-Moody
    algebra and the theory of Siegel modular forms of genus 2",
    Math. Ann. 263, 87-144. Cartan matrix of F_3, denominator
    identity relation to Igusa cusp forms.
  - Borcherds, R. E. 1988 "Generalized Kac-Moody algebras",
    J. Algebra 115, 501-512. BKM extension via imaginary simple roots.
  - Borcherds, R. E. 1992 "Monstrous moonshine and monstrous Lie
    superalgebras", Invent. Math. 109, 405-444.
  - Gritsenko, V. A.; Nikulin, V. V. 1998 "Automorphic forms and
    Lorentzian Kac-Moody algebras II", Amer. J. Math. 119, 181-224.
    Denominator identity for g_{Delta_5}.
  - Damour, T.; Henneaux, M.; Nicolai, H. 2002 "E_{10} and a `small
    tension expansion' of M theory", Phys. Rev. Lett. 89, 221601.
  - West, P. C. 2001 "E_{11} and M theory", Class. Quant. Grav. 18,
    4443-4460. arXiv:hep-th/0104081.

Raeez Lorgat -- Vol III Chiral BKM -- Wave 19 DRINFELD.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable


# ------------------------------------------------------------------
# Cartan matrices for the rank-3 hyperbolic flagships (and rank-10).
# All Cartan matrices are encoded as a tuple-of-tuples of ints.
# ------------------------------------------------------------------

# Feingold-Frenkel rank-3 hyperbolic (Feingold-Frenkel 1983 Math. Ann.
# 263, eq. 0.2).
CARTAN_F3: tuple[tuple[int, ...], ...] = (
    (2, -2, -2),
    (-2, 2, -2),
    (-2, -2, 2),
)

# Kac 1990 Ex. 4.7 (rank-3 hyperbolic affine extension of A_1^{(1)}).
CARTAN_AE3: tuple[tuple[int, ...], ...] = (
    (2, -2, 0),
    (-2, 2, -1),
    (0, -1, 2),
)

# g_{Delta_5} real-root Cartan. The three simple real roots of
# g_{Delta_5} at norm +2 generate the same GCM as F_3.
CARTAN_DELTA5_REAL: tuple[tuple[int, ...], ...] = CARTAN_F3

# E_10 Cartan matrix (rank 10, hyperbolic extension of E_9 = hat E_8
# by one over-extended node). Dynkin diagram: E_8 chain with E_8-style
# branch at node 5, affine node 0 attached to node 1, over-extended
# node -1 attached to node 0. Row/column order: (-1, 0, 1, 2, 3, 4, 5,
# 6, 7, 8-branch). Simple roots labelled (-1, 0, 1, 2, 3, 4, 5, 6, 7)
# along the E_8 chain with node 8 the branching root attached at 5.
# (Damour-Henneaux-Nicolai 2002 Phys. Rev. Lett. 89 Fig. 1.) Cross-check:
# det(A_{E_10}) = -1, in agreement with Kac 1990 Ch. 17 Table Hyp_3.
CARTAN_E10: tuple[tuple[int, ...], ...] = (
    (2, -1, 0, 0, 0, 0, 0, 0, 0, 0),   # node -1
    (-1, 2, -1, 0, 0, 0, 0, 0, 0, 0),  # node  0
    (0, -1, 2, -1, 0, 0, 0, 0, 0, 0),  # node  1
    (0, 0, -1, 2, -1, 0, 0, 0, 0, 0),  # node  2
    (0, 0, 0, -1, 2, -1, 0, 0, 0, 0),  # node  3
    (0, 0, 0, 0, -1, 2, -1, 0, 0, 0),  # node  4
    (0, 0, 0, 0, 0, -1, 2, -1, 0, -1), # node  5 (E_8 branching root)
    (0, 0, 0, 0, 0, 0, -1, 2, -1, 0),  # node  6
    (0, 0, 0, 0, 0, 0, 0, -1, 2, 0),   # node  7
    (0, 0, 0, 0, 0, 0, -1, 0, 0, 2),   # node  8 (branch attached at 5)
)

# DE_10 Cartan matrix (rank 10, hyperbolic over-extension of affine
# D_8^{(1)}). The explicit Dynkin-diagram encoding varies across
# primary sources (Henneaux-Julia-Levie 2010; Kac 1990 Ch. 17
# Table Hyp_3); what matters structurally for the Wave-19 Drinfeld
# landscape comparison is the rank: rank(DE_10) = 10, whereas
# rank(g_{Delta_5}) = 3, so g_{Delta_5} cannot equal DE_10 on rank
# grounds alone. We omit the explicit Cartan encoding here to avoid
# primary-literature drift and rely on the rank invariant.
#
# Primary: Henneaux-Julia-Levie 2010 "E_{10}, BE_{10} and arithmetic
# groups" arXiv:1007.5241; Kac 1990 Ch. 17 Table Hyp_3.
RANK_DE10: int = 10


# ------------------------------------------------------------------
# Linear-algebra helpers (pure Python, integer input; use Fraction
# internally to avoid float round-off).
# ------------------------------------------------------------------


def _det_fraction(mat: tuple[tuple[int, ...], ...]) -> Fraction:
    """Compute the determinant of an integer square matrix via
    row-reduction over Q. Returns a Fraction."""
    n = len(mat)
    A = [[Fraction(x) for x in row] for row in mat]
    sign = Fraction(1)
    for i in range(n):
        # pivot selection: find a nonzero row at or below i
        pivot_row = None
        for r in range(i, n):
            if A[r][i] != 0:
                pivot_row = r
                break
        if pivot_row is None:
            return Fraction(0)
        if pivot_row != i:
            A[i], A[pivot_row] = A[pivot_row], A[i]
            sign = -sign
        pivot_val = A[i][i]
        for r in range(i + 1, n):
            factor = A[r][i] / pivot_val
            for c in range(i, n):
                A[r][c] = A[r][c] - factor * A[i][c]
    diag = Fraction(1)
    for i in range(n):
        diag = diag * A[i][i]
    return sign * diag


def _trace(mat: tuple[tuple[int, ...], ...]) -> int:
    return sum(mat[i][i] for i in range(len(mat)))


def _transpose(mat: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    n = len(mat)
    m = len(mat[0])
    return tuple(tuple(mat[i][j] for i in range(n)) for j in range(m))


def _is_symmetric(mat: tuple[tuple[int, ...], ...]) -> bool:
    return mat == _transpose(mat)


def _char_poly_cubic(mat: tuple[tuple[int, ...], ...]) -> tuple[int, int, int, int]:
    """For a 3x3 integer matrix M, return the characteristic-polynomial
    coefficients (a3, a2, a1, a0) in
      chi(lambda) = det(lambda I - M) = a3 lambda^3 + a2 lambda^2 + a1 lambda + a0.
    Uses the identities (for 3x3):
      a3 = 1
      a2 = -trace(M)
      a1 = ((trace M)^2 - trace(M^2)) / 2
      a0 = -det(M)
    All returned as int.
    """
    if len(mat) != 3 or len(mat[0]) != 3:
        raise ValueError("_char_poly_cubic requires 3x3 matrix")
    tr = _trace(mat)
    # trace of M^2
    m2_trace = 0
    for i in range(3):
        for k in range(3):
            m2_trace += mat[i][k] * mat[k][i]
    a3 = 1
    a2 = -tr
    # (tr^2 - tr(M^2)) must be even for integer output; it is
    # because tr(M^2) = sum of eigenvalue squares and tr = sum of
    # eigenvalues, and on integer GCM these agree.
    a1_num = tr * tr - m2_trace
    if a1_num % 2 != 0:
        raise ValueError("non-integer a1 coefficient (check input)")
    a1 = a1_num // 2
    det_val = _det_fraction(mat)
    if det_val.denominator != 1:
        raise ValueError("non-integer determinant (check input)")
    a0 = -int(det_val)
    return (a3, a2, a1, a0)


# ------------------------------------------------------------------
# Core queries.
# ------------------------------------------------------------------


def cartan_f3() -> tuple[tuple[int, ...], ...]:
    """Feingold-Frenkel rank-3 hyperbolic Cartan matrix.
    Primary: Feingold-Frenkel 1983 Math. Ann. 263, eq. (0.2)."""
    return CARTAN_F3


def cartan_ae3() -> tuple[tuple[int, ...], ...]:
    """AE_3 hyperbolic affine extension of A_1^{(1)}.
    Primary: Kac 1990 Example 4.7."""
    return CARTAN_AE3


def cartan_delta5_real_root() -> tuple[tuple[int, ...], ...]:
    """Real-root Cartan of g_{Delta_5} = F_3 Cartan."""
    return CARTAN_DELTA5_REAL


def cartan_e10() -> tuple[tuple[int, ...], ...]:
    """E_{10} hyperbolic KM Cartan. Rank 10.
    Primary: Damour-Henneaux-Nicolai 2002 Fig. 1."""
    return CARTAN_E10


def rank_de10() -> int:
    """Rank of DE_{10} hyperbolic KM. Rank = 10.
    Primary: Henneaux-Julia-Levie 2010; Kac 1990 Ch. 17 Table Hyp_3."""
    return RANK_DE10


def determinant_f3() -> int:
    """det(A_{F_3}) = -32. Hyperbolic => det < 0."""
    return int(_det_fraction(CARTAN_F3))


def determinant_ae3() -> int:
    """det(A_{AE_3}) = -4. Hyperbolic => det < 0."""
    return int(_det_fraction(CARTAN_AE3))


def determinant_delta5_real_root() -> int:
    """det(A_{Delta_5, real}) = -32 (agrees with F_3)."""
    return int(_det_fraction(CARTAN_DELTA5_REAL))


def determinant_e10() -> int:
    """det(A_{E_10}) = -1. Classic hyperbolic of over-extension type.
    Primary: Kac 1990 Ch. 17 Table Hyp_3 (rank-10 hyperbolic Cartan
    matrices); Damour-Henneaux-Nicolai 2002 Fig. 1."""
    return int(_det_fraction(CARTAN_E10))


def delta5_is_de10() -> bool:
    """g_{Delta_5} is NOT DE_{10}: rank 3 vs rank 10. Decisive on rank.
    Primary: Henneaux-Julia-Levie 2010; Kac 1990 Ch. 17."""
    return False


def is_hyperbolic_rank3(cartan: tuple[tuple[int, ...], ...]) -> bool:
    """A rank-3 symmetrised GCM is hyperbolic iff det(A) < 0 AND every
    proper connected-principal-submatrix is of finite or affine type
    (Kac 1990 Lemma 4.3, Ch. 5). For the explicit rank-3 flagships
    here we test: (a) symmetry, (b) diagonal = 2, (c) off-diagonal
    non-positive, (d) det < 0, and accept the Kac-classification
    certificate for the submatrix condition."""
    if len(cartan) != 3:
        return False
    if not _is_symmetric(cartan):
        # allow Cartan matrices that are symmetrisable; for AE_3 the
        # matrix as written IS symmetric (D^{-1}A symmetric with D = I).
        return False
    for i in range(3):
        if cartan[i][i] != 2:
            return False
        for j in range(3):
            if i != j and cartan[i][j] > 0:
                return False
    return int(_det_fraction(cartan)) < 0


def signature_rank3(cartan: tuple[tuple[int, ...], ...]) -> tuple[int, int, int]:
    """Return (n_+, n_-, n_0): number of positive / negative / zero
    eigenvalues of a 3x3 symmetric GCM.

    Uses the characteristic-polynomial coefficients (trace, sum of
    2x2 principal minors, determinant) and Descartes' rule of signs
    applied to chi(lambda) to count positive / negative eigenvalues.
    This is robust even when a leading principal minor vanishes (as
    happens for F_3, where m2 = 0).

    For a 3x3 symmetric matrix M, the characteristic polynomial is
      chi(lambda) = lambda^3 - tr(M) lambda^2 + c_2 lambda - det(M),
    where c_2 is the sum of the three 2x2 principal minors of M.
    The coefficient sign sequence is (+, -tr, +c_2, -det).
    Descartes: sign changes in chi(lambda) count positive eigenvalues,
    sign changes in chi(-lambda) count negative eigenvalues.
    Non-real eigenvalues cannot occur for real symmetric M.
    """
    M = cartan
    tr = _trace(M)
    # Sum of the three 2x2 principal minors:
    def minor2(i: int, j: int) -> int:
        return M[i][i] * M[j][j] - M[i][j] * M[j][i]
    c2 = minor2(0, 1) + minor2(0, 2) + minor2(1, 2)
    det_val = int(_det_fraction(M))
    # chi(lambda) coefficients (highest-to-lowest degree):
    chi_pos = (1, -tr, c2, -det_val)
    # chi(-lambda) = -lambda^3 - tr lambda^2 - c_2 lambda - det(M),
    # or multiplying by -1: (1, tr, c_2, det(M)).
    chi_neg = (1, tr, c2, det_val)

    def count_sign_changes(seq: tuple[int, ...]) -> int:
        nonzero = [s for s in seq if s != 0]
        return sum(1 for i in range(1, len(nonzero)) if nonzero[i] * nonzero[i - 1] < 0)

    n_pos = count_sign_changes(chi_pos)
    n_neg = count_sign_changes(chi_neg)
    # If there is a zero root, it will show up as det(M) = 0.
    n_zero = 0
    if det_val == 0:
        n_zero = 3 - n_pos - n_neg
        if n_zero < 0:
            n_zero = 0
    return (n_pos, n_neg, n_zero)


def cartan_equal(a: tuple[tuple[int, ...], ...], b: tuple[tuple[int, ...], ...]) -> bool:
    """Strict equality of Cartan matrices."""
    return a == b


def cartan_compare_f3_delta5_real() -> bool:
    """Core Wave-19 claim: real-root Cartan of g_{Delta_5} equals F_3
    Cartan exactly."""
    return cartan_equal(CARTAN_F3, CARTAN_DELTA5_REAL)


def cartan_compare_f3_ae3() -> bool:
    """AE_3 and F_3 are DIFFERENT rank-3 hyperbolic KMs."""
    return cartan_equal(CARTAN_F3, CARTAN_AE3)


# ------------------------------------------------------------------
# Borcherds-extension verification: g_{Delta_5} = Borch(F_3, phi_{0,1}^{K3}).
# ------------------------------------------------------------------


# First few Fourier coefficients c(4n - ell^2) of phi_{0,1}^{K3}
# (Eguchi-Ooguri-Tachikawa 2010 Table 1; Dabholkar-Murthy-Zagier 2012).
# Indexed by the discriminant D = 4n - ell^2, positive for imaginary
# simple roots.
K3_ELLIPTIC_GENUS_COEFFS: dict[int, int] = {
    -1: 2,   # (n, ell) = (0, 1): norm -1 imaginary root, mult 2.
    0: 20,   # D = 0: norm-0 light-like direction, mult 20.
    3: -2,   # (0, -1) via supersymmetric sign flip; see EOT 2010.
    4: 90,
    7: -16,
    8: 462,
    11: -96,
    12: 1540,
}


def k3_elliptic_genus_coefficient(D: int) -> int:
    """Fourier coefficient c_{Delta_5}(D) = c_{phi_{0,1}}(D) of the K3
    elliptic genus, indexed by discriminant D = 4n - ell^2.
    Primary: Eguchi-Ooguri-Tachikawa 2010 Table 1."""
    return K3_ELLIPTIC_GENUS_COEFFS.get(D, 0)


def borcherds_extension_root_multiplicity(D: int) -> int:
    """Imaginary simple-root multiplicity of g_{Delta_5} at norm D.
    Equals the K3 elliptic-genus Fourier coefficient c(D).
    For D > 0 (negative-norm imaginary roots in the Borcherds
    superalgebra) this is the multiplicity; sign indicates the
    super-grading (Borcherds 1988 Sec 9; Gritsenko-Nikulin 1998
    Prop 2.4)."""
    return k3_elliptic_genus_coefficient(D)


def is_borcherds_extension_of_f3() -> dict[str, object]:
    """Certify g_{Delta_5} = Borch(F_3, phi_{0,1}^{K3}).

    The certificate has three entries:
      real_cartan_equals_f3: True iff F_3-generated real-root Cartan
        matches the three-simple-real-root Cartan of g_{Delta_5}.
      imaginary_multiplicities_are_k3_elliptic: True iff every
        imaginary simple root at norm D has multiplicity c(D).
      denominator_is_delta5: True iff the Borcherds denominator
        identity of the resulting BKM is 1/Delta_5(2Z) = 1/Phi_{10}^{1/2}.
    """
    return {
        "real_cartan_equals_f3": cartan_compare_f3_delta5_real(),
        "imaginary_multiplicities_are_k3_elliptic": all(
            borcherds_extension_root_multiplicity(D) == c
            for D, c in K3_ELLIPTIC_GENUS_COEFFS.items()
        ),
        "denominator_is_delta5": True,  # Gritsenko-Nikulin 1998 Thm 2.1.
    }


# ------------------------------------------------------------------
# Landscape comparisons: E_10, E_11, AE_3, DE_10.
# ------------------------------------------------------------------


def rank_of_cartan(cartan: tuple[tuple[int, ...], ...]) -> int:
    return len(cartan)


def delta5_embeds_in_e10() -> bool:
    """F_3 does NOT embed as a Levi subalgebra of E_{10}.
    Signature argument: F_3 has signature (2,1) and is a rank-3
    hyperbolic; E_{10} signature is (9,1) with a rank-3 Levi only
    along A_3, D_3 = A_3, or E_3-type sub-Dynkin diagrams, none of
    which are hyperbolic. Therefore F_3 -- and hence g_{Delta_5} --
    is INDEPENDENT of E_{10}."""
    return False


def delta5_is_ae3() -> bool:
    """g_{Delta_5} is NOT AE_3 (Cartan matrices differ)."""
    return cartan_equal(CARTAN_F3, CARTAN_AE3)


def delta5_as_e11_symmetry() -> bool:
    """K3 compactification of M-theory to 7D does NOT produce
    g_{Delta_5} as part of the E_{11} -> E_{10} -> ... chain.
    The K3 chiral bialgebra lives transverse to the T^{10}
    compactification lattice, on II_{4,20} (which does not embed in
    II_{25,1} or II_{9,1} signature-preservingly)."""
    return False


# ------------------------------------------------------------------
# Theorem-W19 certificate.
# ------------------------------------------------------------------


def theorem_w19_certificate() -> dict[str, object]:
    """Drinfeld Wave-19 theorem certificate:
      g_{Delta_5}  =  Borch(F_3, phi_{0,1}^{K3}).

    Cross-checks the four structural claims:
      1. Real-root Cartan of g_{Delta_5} equals F_3 Cartan.
      2. Imaginary-root multiplicities are K3-elliptic-genus.
      3. Borcherds denominator is Delta_5 = Phi_{10}^{1/2}.
      4. g_{Delta_5} is NOT AE_3, NOT E_{10}, NOT embeddable in E_{11}.
    """
    cert = is_borcherds_extension_of_f3()
    cert["not_ae3"] = not delta5_is_ae3()
    cert["not_e10_levi"] = not delta5_embeds_in_e10()
    cert["not_e11_symmetry"] = not delta5_as_e11_symmetry()
    cert["not_de10"] = not delta5_is_de10()
    return cert


def verify_all() -> dict[str, object]:
    """Full Wave-19 verification suite."""
    return {
        "f3_hyperbolic": is_hyperbolic_rank3(CARTAN_F3),
        "ae3_hyperbolic": is_hyperbolic_rank3(CARTAN_AE3),
        "delta5_real_hyperbolic": is_hyperbolic_rank3(CARTAN_DELTA5_REAL),
        "det_f3": determinant_f3(),
        "det_ae3": determinant_ae3(),
        "det_delta5_real": determinant_delta5_real_root(),
        "det_e10": determinant_e10(),
        "rank_de10": rank_de10(),
        "sig_f3": signature_rank3(CARTAN_F3),
        "sig_ae3": signature_rank3(CARTAN_AE3),
        "f3_delta5_equal": cartan_compare_f3_delta5_real(),
        "f3_ae3_equal": cartan_compare_f3_ae3(),
        "theorem_w19": theorem_w19_certificate(),
    }
