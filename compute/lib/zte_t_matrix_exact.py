"""Exact rational ZTE correction T-matrix.

MATHEMATICAL FRAMEWORK:

The Zamolodchikov tetrahedron equation (ZTE) for the Yang R-matrix
    R(z) = (z*Id + kappa*P) / (z + kappa)
fails at O(kappa^2).  The numerical engines (zte_correction_engine,
zte_correction_explicit_final) construct the correction T by Newton
iteration in floating point.  This engine computes T with EXACT
RATIONAL entries using Python's fractions.Fraction for fast exact
arithmetic and sympy only for the final linear solve.

METHOD:
    1. Fix rational spectral parameters u = (u0, u1, u2, u3) and
       rational kappa = h1*h2*h3.
    2. Build all R-matrices R_{ij}(u_i - u_j) as 16x16 matrices with
       Fraction entries.
    3. Build face S-operators S_{ijk} = R_{ij} R_{ik} R_{jk} (exact).
    4. Project everything to the charge-2 sector (6x6) EARLY for speed.
    5. Compute the ZTE obstruction O = LHS - RHS on charge-2 (exact).
    6. Build the linearized ZTE system A*x = -O_{c2} using ONLY 6x6
       projected S-operators (36 rows, 80 cols).
    7. Solve via sympy's exact rref on the augmented matrix.
    8. Extract per-face correction matrices with exact rational entries.
    9. VERIFY: S^{corr} = S + C satisfies ZTE to O(kappa^4).

PERFORMANCE:
    The key optimization is projecting to the charge-2 sector (6x6)
    BEFORE building the linearized system.  This avoids 80 multiplications
    of 16x16 sympy matrices and replaces them with fast Fraction arithmetic
    on 6x6 matrices.

CONVENTIONS:
    V = C^2 = span{|0>, |1>}
    R(z) = (z*Id + kappa*P)/(z + kappa) on V tensor V
    S_{ijk} = R_{ij}(u_i-u_j) R_{ik}(u_i-u_k) R_{jk}(u_j-u_k) on V^4
    ZTE: S012 S013 S023 S123 = S123 S023 S013 S012
    Charge-2 basis of V^4: |0011>, |0101>, |0110>, |1001>, |1010>, |1100>

REFERENCES:
    thm:zte-failure (en_factorization.tex): ZTE fails for Yang R-matrix.
    prop:zte-deformation-cohomology: H^2_ext trivial, correction EXISTS.
    prop:zte-explicit-correction: Newton iteration converges.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, List, Optional, Tuple

from sympy import Matrix, Rational, eye, zeros


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_FACE_ORDER = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]

# Charge sectors of V^{otimes 3} (dim 8): index -> charge (popcount)
_CHARGES_V3: Dict[int, List[int]] = {}
for _idx in range(8):
    _c = ((_idx >> 2) & 1) + ((_idx >> 1) & 1) + (_idx & 1)
    _CHARGES_V3.setdefault(_c, []).append(_idx)

# Charge sectors of V^{otimes 4} (dim 16)
_CHARGES_V4: Dict[int, List[int]] = {}
for _idx in range(16):
    _c = bin(_idx).count("1")
    _CHARGES_V4.setdefault(_c, []).append(_idx)

# Charge-2 sector of V^4: C(4,2) = 6 basis states
_C2_IDX = _CHARGES_V4[2]  # [3, 5, 6, 9, 10, 12]

# Charge-2 labels
_C2_LABELS = ["|0011>", "|0101>", "|0110>", "|1001>", "|1010>", "|1100>"]

# Default parameters: rational, generic, well-separated
_U_DEFAULT = [Fraction(0), Fraction(1), Fraction(3), Fraction(7)]
_KAPPA_DEFAULT = Fraction(1, 5)  # kappa = 1/5


# ---------------------------------------------------------------------------
# Fraction matrix arithmetic (pure Python, no sympy overhead)
# ---------------------------------------------------------------------------

def _fmat_zeros(n: int, m: int) -> List[List[Fraction]]:
    """Create n x m zero matrix of Fractions."""
    return [[Fraction(0)] * m for _ in range(n)]


def _fmat_eye(n: int) -> List[List[Fraction]]:
    """Create n x n identity matrix of Fractions."""
    M = _fmat_zeros(n, n)
    for i in range(n):
        M[i][i] = Fraction(1)
    return M


def _fmat_mul(A: List[List[Fraction]], B: List[List[Fraction]]
              ) -> List[List[Fraction]]:
    """Multiply two Fraction matrices."""
    n = len(A)
    m = len(B[0])
    p = len(B)
    C = _fmat_zeros(n, m)
    for i in range(n):
        for j in range(m):
            s = Fraction(0)
            for k in range(p):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    return C


def _fmat_add(A: List[List[Fraction]], B: List[List[Fraction]]
              ) -> List[List[Fraction]]:
    """Add two Fraction matrices."""
    n = len(A)
    m = len(A[0])
    return [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]


def _fmat_sub(A: List[List[Fraction]], B: List[List[Fraction]]
              ) -> List[List[Fraction]]:
    """Subtract two Fraction matrices."""
    n = len(A)
    m = len(A[0])
    return [[A[i][j] - B[i][j] for j in range(m)] for i in range(n)]


def _fmat_extract(M: List[List[Fraction]], rows: List[int],
                  cols: List[int]) -> List[List[Fraction]]:
    """Extract submatrix at given rows and cols."""
    return [[M[r][c] for c in cols] for r in rows]


def _fmat_neg(A: List[List[Fraction]]) -> List[List[Fraction]]:
    """Negate a Fraction matrix."""
    n = len(A)
    m = len(A[0])
    return [[-A[i][j] for j in range(m)] for i in range(n)]


def _fmat_transpose(A: List[List[Fraction]]) -> List[List[Fraction]]:
    """Transpose a Fraction matrix."""
    n = len(A)
    m = len(A[0])
    return [[A[j][i] for j in range(n)] for i in range(m)]


# ---------------------------------------------------------------------------
# Yang R-matrix: exact Fraction arithmetic
# ---------------------------------------------------------------------------

def _yang_r_frac(z: Fraction, kappa: Fraction) -> List[List[Fraction]]:
    """4x4 Yang R-matrix R(z) = (z*Id + kappa*P)/(z + kappa), exact.

    Basis: {|00>, |01>, |10>, |11>}.
    P is the permutation: P|ij> = |ji>.
    """
    denom = z + kappa
    # R = (z*I + kappa*P) / denom
    # Diagonal: z/denom except (1,1) and (2,2) which also get kappa contrib
    # Off-diag: only (1,2) and (2,1) from P
    R = _fmat_zeros(4, 4)
    # I contribution: diagonal
    zd = z / denom
    kd = kappa / denom
    R[0][0] = zd + kd  # P[0,0]=1
    R[1][1] = zd       # P[1,1]=0
    R[1][2] = kd       # P[1,2]=1
    R[2][1] = kd       # P[2,1]=1
    R[2][2] = zd       # P[2,2]=0
    R[3][3] = zd + kd  # P[3,3]=1
    return R


# ---------------------------------------------------------------------------
# Embedding R_{ij} into V^{tensor 4} (16x16): exact
# ---------------------------------------------------------------------------

def _embed_r_frac(z: Fraction, kappa: Fraction, i: int, j: int
                  ) -> List[List[Fraction]]:
    """Embed R_{ij}(z) into V^{tensor 4} (dim 16), exact Fraction."""
    R = _yang_r_frac(z, kappa)
    result = _fmat_zeros(16, 16)

    for src in range(16):
        bits_src = [(src >> (3 - k)) & 1 for k in range(4)]
        bi, bj = bits_src[i], bits_src[j]
        two_bit_src = bi * 2 + bj

        for two_bit_dst in range(4):
            coeff = R[two_bit_dst][two_bit_src]
            if coeff == Fraction(0):
                continue
            bits_dst = list(bits_src)
            bits_dst[i] = (two_bit_dst >> 1) & 1
            bits_dst[j] = two_bit_dst & 1
            dst = sum(bits_dst[k] << (3 - k) for k in range(4))
            result[dst][src] += coeff

    return result


# ---------------------------------------------------------------------------
# Face S-operator and ZTE: exact, full 16x16
# ---------------------------------------------------------------------------

def _s_operator_frac(u: List[Fraction], kappa: Fraction,
                     i: int, j: int, k: int) -> List[List[Fraction]]:
    """S_{ijk} = R_{ij}(u_i-u_j) R_{ik}(u_i-u_k) R_{jk}(u_j-u_k), exact."""
    R_ij = _embed_r_frac(u[i] - u[j], kappa, i, j)
    R_ik = _embed_r_frac(u[i] - u[k], kappa, i, k)
    R_jk = _embed_r_frac(u[j] - u[k], kappa, j, k)
    return _fmat_mul(_fmat_mul(R_ij, R_ik), R_jk)


def _zte_obstruction_frac(u: List[Fraction], kappa: Fraction) -> Dict:
    """Compute exact ZTE obstruction. Returns S_dict and charge-2 obs."""
    S_dict = {}
    for (i, j, k) in _FACE_ORDER:
        S_dict[(i, j, k)] = _s_operator_frac(u, kappa, i, j, k)

    # LHS = S012 S013 S023 S123
    lhs = _fmat_mul(
        _fmat_mul(
            _fmat_mul(S_dict[(0, 1, 2)], S_dict[(0, 1, 3)]),
            S_dict[(0, 2, 3)]
        ),
        S_dict[(1, 2, 3)]
    )
    # RHS = S123 S023 S013 S012
    rhs = _fmat_mul(
        _fmat_mul(
            _fmat_mul(S_dict[(1, 2, 3)], S_dict[(0, 2, 3)]),
            S_dict[(0, 1, 3)]
        ),
        S_dict[(0, 1, 2)]
    )
    obs_full = _fmat_sub(lhs, rhs)
    obs_c2 = _fmat_extract(obs_full, _C2_IDX, _C2_IDX)

    # Also project S-operators to charge-2
    S_c2 = {}
    for f in _FACE_ORDER:
        S_c2[f] = _fmat_extract(S_dict[f], _C2_IDX, _C2_IDX)

    return {
        "S_dict": S_dict,
        "S_c2": S_c2,
        "obs_full": obs_full,
        "obs_c2": obs_c2,
    }


# ---------------------------------------------------------------------------
# Ternary basis elements projected to charge-2 of V^4
#
# For each face (i,j,k) and each charge-preserving elementary matrix
# E_{pq} on V^3 (8x8), we embed E into V^4 (16x16) and project to
# the charge-2 sector (6x6).  This gives a list of 6x6 Fraction
# matrices, one per (face, basis element).
# ---------------------------------------------------------------------------

def _embed_ternary_to_c2_frac(
    p_local: int, q_local: int, i: int, j: int, k: int
) -> List[List[Fraction]]:
    """Embed elementary matrix E_{p,q} on V_i V_j V_k into V^4,
    then project to charge-2 sector.  Returns 6x6 Fraction matrix.

    p_local, q_local: indices in {0,...,7} for V^{otimes 3}.
    """
    ijk = (i, j, k)
    C = _fmat_zeros(6, 6)

    # For each charge-2 source basis vector in V^4
    for ci, src_full in enumerate(_C2_IDX):
        bits_src = [(src_full >> (3 - m)) & 1 for m in range(4)]
        # Extract the (i,j,k) bits to form the local source index
        lb = [bits_src[ijk[0]], bits_src[ijk[1]], bits_src[ijk[2]]]
        local_src = lb[0] * 4 + lb[1] * 2 + lb[2]

        if local_src != q_local:
            continue  # E_{p,q} only acts on source = q_local

        # The local destination is p_local
        ld = ((p_local >> 2) & 1, (p_local >> 1) & 1, p_local & 1)
        # Charge preservation check
        if sum(ld) != sum(lb):
            continue

        # Build the destination in V^4
        bits_dst = list(bits_src)
        bits_dst[ijk[0]] = ld[0]
        bits_dst[ijk[1]] = ld[1]
        bits_dst[ijk[2]] = ld[2]
        dst_full = sum(bits_dst[m] << (3 - m) for m in range(4))

        # Check destination is also in charge-2
        if dst_full not in _C2_IDX:
            continue

        ri = _C2_IDX.index(dst_full)
        C[ri][ci] = Fraction(1)

    return C


def _ternary_basis_c2_frac() -> List[Tuple[int, int, int, int, int,
                                            List[List[Fraction]]]]:
    """Build ternary basis elements projected to charge-2.

    Returns list of (face_idx, basis_idx, charge, p, q, C_c2_6x6)
    where C_c2_6x6 is the 6x6 Fraction matrix.
    """
    basis_info = []
    for face_idx, (fi, fj, fk) in enumerate(_FACE_ORDER):
        b_idx = 0
        for c in sorted(_CHARGES_V3.keys()):
            indices = _CHARGES_V3[c]
            for p in indices:
                for q in indices:
                    C_c2 = _embed_ternary_to_c2_frac(p, q, fi, fj, fk)
                    basis_info.append((face_idx, b_idx, c, p, q, C_c2))
                    b_idx += 1
    return basis_info


# ---------------------------------------------------------------------------
# Linearized ZTE system: fast charge-2 computation
#
# The linearized ZTE at face f replaces S_f by C_f in the product:
#   LHS_f = S_012 ... C_f ... S_123  (C at position of face f)
#   RHS_f = S_123 ... C_f ... S_012  (C at position of face f, reversed)
#   column = (LHS_f - RHS_f)|_{charge-2}
#
# Since all S-operators are block-diagonal in charge sectors, and C
# only connects states within the same charge sector, we can compute
# everything using the 6x6 charge-2 projections.
# ---------------------------------------------------------------------------

def _build_linearized_system_c2(
    S_c2: Dict[Tuple, List[List[Fraction]]],
    obs_c2: List[List[Fraction]],
) -> Tuple[List[List[Fraction]], List[Fraction]]:
    """Build linearized ZTE system A*x = b using only charge-2 data.

    A: 36 x 80 Fraction matrix
    b: length-36 Fraction vector (= -obs_c2 flattened)

    Returns (A_rows, b_vec) where A_rows is list of 80 Fractions per row,
    b_vec is list of 36 Fractions.
    """
    basis_c2 = _ternary_basis_c2_frac()

    # Pre-group by face
    face_basis = [[] for _ in range(4)]
    for (face_idx, b_idx, c, p, q, C_c2) in basis_c2:
        face_basis[face_idx].append((b_idx, C_c2))

    columns = []  # list of 36-element lists

    for face_idx, (fi, fj, fk) in enumerate(_FACE_ORDER):
        face_key = (fi, fj, fk)
        rev_faces = list(reversed(_FACE_ORDER))
        rev_idx = rev_faces.index(face_key)

        for (b_idx, C_c2) in face_basis[face_idx]:
            # LHS: product with C at position face_idx
            factors_L = [S_c2[f] for f in _FACE_ORDER]
            factors_L[face_idx] = C_c2
            lt = factors_L[0]
            for f in factors_L[1:]:
                lt = _fmat_mul(lt, f)

            # RHS: product with C at position rev_idx in reversed order
            factors_R = [S_c2[f] for f in rev_faces]
            factors_R[rev_idx] = C_c2
            rt = factors_R[0]
            for f in factors_R[1:]:
                rt = _fmat_mul(rt, f)

            diff = _fmat_sub(lt, rt)
            # Flatten to 36-element column
            col = []
            for r in range(6):
                for c in range(6):
                    col.append(diff[r][c])
            columns.append(col)

    # Build A: rows are indexed by (row of obs, col of obs), columns by parameters
    n_cols = len(columns)
    A = [[columns[j][i] for j in range(n_cols)] for i in range(36)]

    # b = -obs_c2 flattened
    b_vec = []
    for r in range(6):
        for c in range(6):
            b_vec.append(-obs_c2[r][c])

    return A, b_vec


# ---------------------------------------------------------------------------
# Exact solver using sympy (convert Fraction -> Rational for rref)
# ---------------------------------------------------------------------------

def _solve_exact(A_frac: List[List[Fraction]],
                 b_frac: List[Fraction]) -> Tuple[List[Fraction], int]:
    """Solve A*x = b exactly using sympy rref on augmented matrix.

    Returns (x_solution, rank) where x_solution is list of 80 Fractions.
    Uses the minimum-norm approach: rref with free variables set to 0,
    then project onto row space of A for true minimum norm.
    """
    n_rows = len(A_frac)
    n_cols = len(A_frac[0])

    # Convert to sympy Matrix
    aug_data = []
    for i in range(n_rows):
        row = []
        for j in range(n_cols):
            f = A_frac[i][j]
            row.append(Rational(f.numerator, f.denominator))
        f_b = b_frac[i]
        row.append(Rational(f_b.numerator, f_b.denominator))
        aug_data.append(row)

    aug = Matrix(aug_data)
    rref_mat, pivots = aug.rref()

    # Check consistency
    if n_cols in pivots:
        raise ValueError("System is inconsistent.")

    rank = len(pivots)

    # Extract particular solution (free vars = 0)
    x = [Rational(0)] * n_cols
    for row_idx, piv_col in enumerate(pivots):
        if piv_col < n_cols:
            x[piv_col] = rref_mat[row_idx, n_cols]

    # Convert to Fraction
    x_frac = [Fraction(int(v.p), int(v.q)) for v in x]

    # For minimum-norm: project onto row space of A.
    # Build A as sympy, compute A^T (A A^T)^{-1} A x = projection.
    # But this is expensive for 80x80.  Instead, use the independent-row
    # approach: extract rank-many independent rows, solve A_sub x = b_sub
    # with x = A_sub^T (A_sub A_sub^T)^{-1} b_sub.

    # Convert A to sympy for projection
    A_sym = Matrix(n_rows, n_cols,
                   lambda r, c: Rational(A_frac[r][c].numerator,
                                         A_frac[r][c].denominator))

    # Find independent rows via rref of A^T
    AT_rref, AT_pivots = A_sym.T.rref()
    indep_rows = sorted(AT_pivots)

    if len(indep_rows) == n_rows:
        # Full row rank: x_min = A^T (A A^T)^{-1} b
        b_sym = Matrix(n_rows, 1,
                       lambda r, c: Rational(b_frac[r].numerator,
                                             b_frac[r].denominator))
        AAT = A_sym * A_sym.T
        AAT_inv = AAT.inv()
        x_min_sym = A_sym.T * AAT_inv * b_sym
    else:
        # Rank deficient: use independent rows
        A_sub = A_sym.extract(indep_rows, list(range(n_cols)))
        b_sub_data = [b_frac[r] for r in indep_rows]
        b_sub = Matrix(len(indep_rows), 1,
                       lambda r, c: Rational(b_sub_data[r].numerator,
                                             b_sub_data[r].denominator))
        AAT_sub = A_sub * A_sub.T
        AAT_sub_inv = AAT_sub.inv()
        x_min_sym = A_sub.T * AAT_sub_inv * b_sub

    x_min_frac = [Fraction(int(x_min_sym[i].p), int(x_min_sym[i].q))
                  for i in range(n_cols)]

    return x_min_frac, rank


# ---------------------------------------------------------------------------
# Embed correction back into 8x8 V^3 and 16x16 V^4 (Fraction)
# ---------------------------------------------------------------------------

def _embed_ternary_full_frac(
    E_8x8: List[List[Fraction]], i: int, j: int, k: int
) -> List[List[Fraction]]:
    """Embed 8x8 ternary operator on V_i V_j V_k into V^4 (16x16)."""
    C = _fmat_zeros(16, 16)
    ijk = (i, j, k)

    for src in range(16):
        bits_src = [(src >> (3 - m)) & 1 for m in range(4)]
        lb = [bits_src[ijk[0]], bits_src[ijk[1]], bits_src[ijk[2]]]
        local_src = lb[0] * 4 + lb[1] * 2 + lb[2]

        for local_dst in range(8):
            val = E_8x8[local_dst][local_src]
            if val == Fraction(0):
                continue
            ld = ((local_dst >> 2) & 1, (local_dst >> 1) & 1, local_dst & 1)
            if sum(ld) != sum(lb):
                continue
            bits_dst = list(bits_src)
            bits_dst[ijk[0]] = ld[0]
            bits_dst[ijk[1]] = ld[1]
            bits_dst[ijk[2]] = ld[2]
            dst = sum(bits_dst[m] << (3 - m) for m in range(4))
            C[dst][src] += val

    return C


# ---------------------------------------------------------------------------
# Ternary basis enumeration (for reconstructing C_faces from x vector)
# ---------------------------------------------------------------------------

def _ternary_basis_info() -> List[Tuple[int, int, int]]:
    """Enumerate (charge, p, q) for each of the 20 ternary basis elements."""
    info = []
    for c in sorted(_CHARGES_V3.keys()):
        indices = _CHARGES_V3[c]
        for p in indices:
            for q in indices:
                info.append((c, p, q))
    return info


# ---------------------------------------------------------------------------
# Main: compute exact T-matrix
# ---------------------------------------------------------------------------

def compute_exact_t_matrix(
    kappa: Optional[Fraction] = None,
    u: Optional[List[Fraction]] = None,
) -> Dict:
    """Compute the ZTE correction T with exact rational entries.

    This is the LINEARIZED correction (first Newton step).  For the
    Yang R-matrix at the given parameters, the linearized ZTE correction
    resolves the O(kappa^2) obstruction exactly.

    Parameters:
        kappa: Fraction Yangian parameter (default 1/5)
        u: list of 4 Fraction spectral parameters (default [0,1,3,7])

    Returns dict with:
        C_faces: dict (i,j,k) -> 8x8 list-of-lists Fraction
        T_full_16: 16x16 correction on V^4 (Fraction)
        T_c2: 6x6 correction on charge-2 sector (Fraction)
        obs_c2: 6x6 original obstruction (Fraction)
        obs_corr_c2: 6x6 residual after correction (Fraction)
        rank: rank of the linearized system
        kappa: the kappa value used
        u: the spectral parameters used
        entries: dict mapping (i,j) -> Fraction for T_c2
    """
    if kappa is None:
        kappa = _KAPPA_DEFAULT
    if u is None:
        u = list(_U_DEFAULT)

    # Step 1: exact obstruction
    obs_data = _zte_obstruction_frac(u, kappa)
    S_dict = obs_data["S_dict"]
    S_c2 = obs_data["S_c2"]
    obs_c2 = obs_data["obs_c2"]

    # Step 2: build linearized system in charge-2 sector
    A_frac, b_frac = _build_linearized_system_c2(S_c2, obs_c2)

    # Step 3: solve exactly
    x_frac, rank = _solve_exact(A_frac, b_frac)

    # Step 4: extract per-face corrections as 8x8
    basis_info = _ternary_basis_info()
    n_basis = len(basis_info)  # 20

    C_faces = {}
    for face_idx, (fi, fj, fk) in enumerate(_FACE_ORDER):
        C_local = _fmat_zeros(8, 8)
        for b_idx, (c, p, q) in enumerate(basis_info):
            param_idx = face_idx * n_basis + b_idx
            C_local[p][q] += x_frac[param_idx]
        C_faces[(fi, fj, fk)] = C_local

    # Step 5: build corrected S and verify on full 16x16
    S_corr = {}
    T_full_16 = _fmat_zeros(16, 16)
    for (fi, fj, fk) in _FACE_ORDER:
        C_embed = _embed_ternary_full_frac(C_faces[(fi, fj, fk)],
                                           fi, fj, fk)
        S_corr[(fi, fj, fk)] = _fmat_add(S_dict[(fi, fj, fk)], C_embed)
        T_full_16 = _fmat_add(T_full_16, C_embed)

    # Corrected ZTE on full 16x16
    lhs_corr = _fmat_mul(
        _fmat_mul(
            _fmat_mul(S_corr[(0, 1, 2)], S_corr[(0, 1, 3)]),
            S_corr[(0, 2, 3)]
        ),
        S_corr[(1, 2, 3)]
    )
    rhs_corr = _fmat_mul(
        _fmat_mul(
            _fmat_mul(S_corr[(1, 2, 3)], S_corr[(0, 2, 3)]),
            S_corr[(0, 1, 3)]
        ),
        S_corr[(0, 1, 2)]
    )
    obs_corr_full = _fmat_sub(lhs_corr, rhs_corr)
    obs_corr_c2 = _fmat_extract(obs_corr_full, _C2_IDX, _C2_IDX)

    T_c2 = _fmat_extract(T_full_16, _C2_IDX, _C2_IDX)

    # Extract entries as plain Fractions for inspection
    entries = {}
    for r in range(6):
        for c in range(6):
            entries[(r, c)] = T_c2[r][c]

    return {
        "C_faces": C_faces,
        "T_full_16": T_full_16,
        "T_c2": T_c2,
        "obs_c2": obs_c2,
        "obs_corr_c2": obs_corr_c2,
        "rank": rank,
        "kappa": kappa,
        "u": u,
        "entries": entries,
        "x_solution": x_frac,
    }


# ---------------------------------------------------------------------------
# Structural analysis of exact T
# ---------------------------------------------------------------------------

def analyze_exact_structure(T_c2: List[List[Fraction]]) -> Dict:
    """Analyze structural properties of exact rational T_c2.

    Checks: symmetry, persymmetry, rank, zero anti-diagonal,
    trace, determinant (via sympy for the determinant).
    """
    n = 6

    # Symmetry: T = T^T
    is_symmetric = all(T_c2[i][j] == T_c2[j][i]
                       for i in range(n) for j in range(n))

    # Persymmetry: JTJ = T, i.e. T[i,j] = T[n-1-i, n-1-j]
    # For symmetric T, this is equivalent to T[i,j] = T[n-1-j, n-1-i].
    is_persymmetric = all(T_c2[i][j] == T_c2[n - 1 - i][n - 1 - j]
                          for i in range(n) for j in range(n))

    # Zero anti-diagonal: T[i, n-1-i] = 0
    antidiag = [T_c2[i][n - 1 - i] for i in range(n)]
    has_zero_antidiag = all(v == Fraction(0) for v in antidiag)

    # Trace
    trace = sum(T_c2[i][i] for i in range(n))

    # Convert to sympy for rank and determinant
    T_sym = Matrix(n, n,
                   lambda r, c: Rational(T_c2[r][c].numerator,
                                         T_c2[r][c].denominator))
    rank = T_sym.rank()
    det = T_sym.det()

    # Characteristic polynomial
    from sympy import Symbol, Poly
    lam = Symbol("lambda")
    char_poly = (T_sym - lam * eye(n)).det()
    char_poly_expanded = Poly(char_poly, lam)

    return {
        "is_symmetric": is_symmetric,
        "is_persymmetric": is_persymmetric,
        "has_zero_antidiag": has_zero_antidiag,
        "antidiag_values": antidiag,
        "rank": rank,
        "trace": Fraction(int(trace.numerator), int(trace.denominator))
                 if isinstance(trace, Fraction) else trace,
        "determinant": det,
        "char_poly_coeffs": char_poly_expanded.all_coeffs(),
    }


# ---------------------------------------------------------------------------
# Verify corrected ZTE residual
# ---------------------------------------------------------------------------

def verify_correction(result: Dict) -> Dict:
    """Verify that the correction resolves the O(kappa^2) obstruction.

    Checks:
    1. Original obs_c2 is nonzero (ZTE fails)
    2. Corrected obs_corr_c2 structure (should be O(kappa^4))
    3. Improvement ratio
    """
    obs_c2 = result["obs_c2"]
    obs_corr_c2 = result["obs_corr_c2"]
    kappa = result["kappa"]

    # Original nonzero
    obs_nonzero = any(obs_c2[r][c] != Fraction(0)
                      for r in range(6) for c in range(6))

    # Residual zero?
    residual_zero = all(obs_corr_c2[r][c] == Fraction(0)
                        for r in range(6) for c in range(6))

    # Max absolute entry
    max_obs = max(abs(obs_c2[r][c]) for r in range(6) for c in range(6))
    max_corr = max(abs(obs_corr_c2[r][c])
                   for r in range(6) for c in range(6))

    improvement = max_obs / max_corr if max_corr != Fraction(0) else None

    # Antisymmetry of original obstruction
    obs_antisym = all(obs_c2[i][j] == -obs_c2[j][i]
                      for i in range(6) for j in range(6))

    return {
        "original_nonzero": obs_nonzero,
        "original_antisymmetric": obs_antisym,
        "residual_is_zero": residual_zero,
        "max_original_entry": max_obs,
        "max_residual_entry": max_corr,
        "improvement": improvement,
    }


# ---------------------------------------------------------------------------
# Pretty-print the T-matrix
# ---------------------------------------------------------------------------

def format_t_matrix(T_c2: List[List[Fraction]]) -> str:
    """Format the 6x6 T-matrix with rational entries for display."""
    lines = []
    lines.append("T_c2 (6x6 correction on charge-2 sector of V^4):")
    lines.append("Basis: " + ", ".join(_C2_LABELS))
    lines.append("")

    strs = []
    for r in range(6):
        row = []
        for c in range(6):
            val = T_c2[r][c]
            if val == Fraction(0):
                row.append("0")
            else:
                row.append(str(val))
        strs.append(row)

    max_w = max(len(s) for row in strs for s in row)

    for r in range(6):
        entries = [s.rjust(max_w) for s in strs[r]]
        lines.append("  [ " + "  ".join(entries) + " ]")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Full pipeline
# ---------------------------------------------------------------------------

def run_full_exact_pipeline(
    kappa: Optional[Fraction] = None,
    u: Optional[List[Fraction]] = None,
) -> Dict:
    """Run the complete exact ZTE correction pipeline.

    Computes T, analyzes structure, verifies correction, formats output.
    """
    result = compute_exact_t_matrix(kappa=kappa, u=u)
    structure = analyze_exact_structure(result["T_c2"])
    verification = verify_correction(result)
    display = format_t_matrix(result["T_c2"])

    return {
        "result": result,
        "structure": structure,
        "verification": verification,
        "display": display,
    }
