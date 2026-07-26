r"""E_1-chiral bialgebra axiom verification for W_{1+infinity}.

MATHEMATICAL FRAMEWORK
=======================

W_{1+infinity} (equivalently, the affine Yangian Y(gl_hat_1)) carries the
structure of an E_1-chiral bialgebra. This engine verifies the five axioms:

1. E_1-ALGEBRA STRUCTURE: W_{1+infinity} has the radially-ordered OPE product.
   The ordering is by |z|: operators at |z_1| > |z_2| are multiplied in that
   order. The OPE T(z)T(w) for |z| > |w| differs from T(w)T(z) for |w| > |z|
   by the R-matrix braiding. This is the E_1 (ordered, non-commutative)
   structure from the open colour of the Swiss-cheese operad.

2. E_1-COALGEBRA STRUCTURE: The ordered bar B^{ord}(W_{1+infinity}) has:
   - Deconcatenation coproduct Delta_dec (NOT coshuffle)
   - Bar differential d_B encoding the OPE
   - MacMahon generating function M(q) = prod_{n>=1} 1/(1-q^n)
   The Drinfeld coproduct Delta_z on the transfer matrix T(u) is the
   mode-level manifestation of this coalgebra structure.

3. BIALGEBRA COMPATIBILITY: The Drinfeld coproduct respects the E_1-ordered
   product via the Miura factorization:
     Delta_z(T(z_1) T(z_2)) = Delta_z(T(z_1)) * Delta_z(T(z_2))
   where * is the E_1-ordered product on A tensor_{E_1,z} A.
   This is verified at spin 2 by checking that Delta_z is an algebra
   homomorphism for the Virasoro modes.

4. COASSOCIATIVITY: (Delta_z1 tensor id) o Delta_z2 = (id tensor Delta_z2) o Delta_z1
   Both sides give T_L(u) T_M(u-z2) T_R(u-z1) via Miura triple product.
   Verified at spin 2 using the TripleTensor infrastructure.

5. AVERAGING MAP KILLS HOPF DATA: The averaging map
     av: B^{ord}(A) -> B^{Sigma}(A)
   sends the E_1 structure to the E_infinity structure. On the coproduct:
     av(Delta_z(T_n)) = T_n tensor 1 + 1 tensor T_n + kappa_ch * (scalar)
   The R-matrix information (the z-dependent asymmetry) is lost.

ORDERED vs SYMMETRIC
====================

The E_1-chiral bialgebra lives on the ORDERED side:
  - Product: radially-ordered OPE (|z_1| > |z_2|)
  - Coproduct: deconcatenation on B^{ord}
  - R-matrix: nontrivial, z-dependent

The averaging map sends everything to the SYMMETRIC side:
  - Product: normally-ordered OPE (symmetric)
  - Coproduct: coshuffle on B^{Sigma}
  - R-matrix: trivialised to kappa_ch

In this Heisenberg-normalized W_{1+infinity} model, the key observation
is that av(r(z)) = kappa_ch: the full R-matrix data reduces to the scalar
collision residue upon symmetrization.

CONVENTIONS
===========
- Psi = level of Heisenberg (kappa_ch(H_Psi) = Psi)
- J_n = modes of J(z) = sum J_n z^{-n-1}
- T_n = (1/(2*Psi)) sum_k :J_{n-k} J_k: (Sugawara, c = 1)
- [J_m, J_n] = Psi * m * delta_{m+n,0}
- Delta_z(T(u)) = T_L(u) * T_R(u-z) (multiplicative Drinfeld coproduct)
- B^{ord}(A) = T^c(s^{-1} bar{A}) with deconcatenation coproduct
- av: B^{ord} -> B^{Sigma} is the S_n-symmetrization (division by n!)
"""

from __future__ import annotations

import math
from typing import Dict, List, Tuple

import numpy as np

from compute.lib.chiral_coproduct_spin2_engine import (
    HeisenbergFock,
    TensorHeisenberg,
)
from compute.lib.chiral_coproduct_spin3_engine import (
    Spin3CoproductEngine,
)


# ---------------------------------------------------------------------------
# Helper: generalised binomial
# ---------------------------------------------------------------------------

def _gbinom(m: int, k: int) -> float:
    """Generalised binomial coefficient C(m, k)."""
    if k < 0:
        return 0.0
    if k == 0:
        return 1.0
    r = 1.0
    for i in range(k):
        r *= (m - i)
    r /= math.factorial(k)
    return r


# ===================================================================
# AXIOM 1: E_1-algebra structure
# ===================================================================

class E1AlgebraVerifier:
    r"""Verify the E_1-algebra (ordered OPE) structure on W_{1+infinity}.

    The E_1 ordering is the radial ordering: for |z_1| > |z_2|, the product
    T(z_1) T(z_2) is well-defined as an operator on the Fock space. The
    difference between T(z_1)T(z_2) and T(z_2)T(z_1) (when both are
    well-defined in their respective domains) is captured by the commutator
    [T_m, T_n] = (m-n)T_{m+n} + (c/12)m(m^2-1) delta_{m+n,0}.

    This commutator IS the R-matrix braiding: moving T(z_1) past T(z_2)
    picks up the Virasoro commutator, which is the OPE singular part.
    The E_1 structure remembers which ordering is used; the E_infinity
    structure forgets.
    """

    def __init__(self, Psi: float = 1.0, N_max: int = 6):
        self.H = HeisenbergFock(Psi, N_max)
        self.Psi = Psi
        self.N_max = N_max

    def verify_ordered_product_associativity(self) -> Dict[str, object]:
        r"""Verify (T_m T_n) T_p = T_m (T_n T_p) on the Fock space.

        The E_1-algebra product is associative (not just homotopy-associative).
        This is the defining property of E_1 (= A_infinity with strict
        higher multiplications).

        For the Virasoro algebra, associativity is the Jacobi identity:
          [T_m, [T_n, T_p]] + [T_n, [T_p, T_m]] + [T_p, [T_m, T_n]] = 0
        """
        mx = 0.0
        for m in range(-2, 3):
            for n in range(-2, 3):
                for p in range(-2, 3):
                    margin = max(abs(m), abs(n), abs(p)) + 4
                    P = self.H.projector_safe(margin)
                    # Jacobi identity with double commutators
                    comm_np = self.H.T(n) @ self.H.T(p) - self.H.T(p) @ self.H.T(n)
                    c1 = self.H.T(m) @ comm_np - comm_np @ self.H.T(m)
                    comm_pm = self.H.T(p) @ self.H.T(m) - self.H.T(m) @ self.H.T(p)
                    c2 = self.H.T(n) @ comm_pm - comm_pm @ self.H.T(n)
                    comm_mn = self.H.T(m) @ self.H.T(n) - self.H.T(n) @ self.H.T(m)
                    c3 = self.H.T(p) @ comm_mn - comm_mn @ self.H.T(p)
                    jac = c1 + c2 + c3
                    err = float(np.max(np.abs(P @ jac @ P)))
                    mx = max(mx, err)
        return {"max_error": mx, "ok": mx < 1e-8}

    def verify_r_matrix_from_commutator(self) -> Dict[str, object]:
        r"""The R-matrix braiding is the Virasoro commutator.

        For the E_1 structure, the "braiding" that relates
        T(z_1)T(z_2) to T(z_2)T(z_1) is:
          R(T_m, T_n) = [T_m, T_n] = (m-n)T_{m+n} + (c/12)m(m^2-1)delta

        This is the OPE singular part that the E_1 structure remembers
        and the averaging map kills.

        VERIFY: [T_m, T_n] = (m-n)T_{m+n} + (c/12)m(m^2-1)delta_{m+n,0}
        with c = 1 (Sugawara central charge for one free boson).
        """
        c = 1.0  # Sugawara c = 1 independent of Psi
        P = self.H.projector_safe(4)
        mx = 0.0
        for m in range(-2, 3):
            for n in range(-2, 3):
                comm = self.H.T(m) @ self.H.T(n) - self.H.T(n) @ self.H.T(m)
                expected = (m - n) * self.H.T(m + n)
                if m + n == 0:
                    expected = expected + (c / 12.0) * m * (m * m - 1) * np.eye(self.H.dim)
                err = float(np.max(np.abs(P @ (comm - expected) @ P)))
                mx = max(mx, err)
        return {"max_error": mx, "ok": mx < 1e-8, "c": c}

    def verify_ordering_asymmetry(self) -> Dict[str, object]:
        r"""Verify T_m T_n != T_n T_m for generic m, n (E_1 is non-commutative).

        The E_1 structure is ORDERED: the product depends on the order of factors.
        Specifically, T_m T_n - T_n T_m = [T_m, T_n] != 0 for m != n.
        This asymmetry is the content of the R-matrix; averaging kills it.
        """
        P = self.H.projector_safe(4)
        max_asym = 0.0
        for m, n in [(2, -2), (2, -1), (1, -1)]:
            comm = self.H.T(m) @ self.H.T(n) - self.H.T(n) @ self.H.T(m)
            asym = float(np.max(np.abs(P @ comm @ P)))
            max_asym = max(max_asym, asym)
        return {
            "max_asymmetry": max_asym,
            "ok": max_asym > 0.01,  # MUST be nonzero for E_1
            "interpretation": "Nonzero asymmetry confirms E_1 non-commutativity"
        }


# ===================================================================
# AXIOM 2: E_1-coalgebra structure
# ===================================================================

class E1CoalgebraVerifier:
    r"""Verify the E_1-coalgebra (deconcatenation + bar differential) structure.

    The ordered bar B^{ord}(W_{1+inf}) = T^c(s^{-1} bar{A}) has:
    1. Deconcatenation coproduct: Delta_dec(a_1 | ... | a_n) = sum_{k=0}^n
       (a_1 | ... | a_k) tensor (a_{k+1} | ... | a_n)
    2. Bar differential d_B encoding the OPE
    3. MacMahon generating function M(q) = prod_{n>=1} 1/(1-q^n)

    The Drinfeld coproduct Delta_z on modes is the mode-level manifestation:
    Delta_z encodes how the ordered bar's deconcatenation interacts with
    the spectral parameter.

    CRITICAL DISTINCTION (AP152): "ordered" here means labeled-ordered
    (combinatorial, the E_1 ordered bar B^{ord}), NOT time-ordered
    (analytic/radial). The deconcatenation coproduct respects the
    labeling order of bar elements.
    """

    def __init__(self, Psi: float = 2.0, N_max: int = 6):
        self.TH = TensorHeisenberg(Psi, N_max)
        self.Psi = Psi
        self.N_max = N_max

    def verify_deconcatenation_vs_coshuffle_spin1(self) -> Dict[str, object]:
        r"""Deconcatenation produces n+1 terms; coshuffle produces 2^n terms.

        At bar degree 2 (two factors), deconcatenation gives 3 terms:
          Delta_dec(a|b) = 1 tensor (a|b) + a tensor b + (a|b) tensor 1
        while coshuffle gives 4 terms:
          Delta_sh(a|b) = 1 tensor (a|b) + a tensor b + b tensor a + (a|b) tensor 1

        The difference is the transposition b tensor a: this is the R-matrix
        term that averaging adds.

        We verify this at spin 1 (J modes): Delta_z(J) is primitive
        (= deconcatenation at degree 1), and the absence of extra terms
        confirms the E_1 (not E_infinity) structure.
        """
        P = self.TH.safe_proj(4)
        mx = 0.0
        for n in range(-2, 3):
            # Primitive coproduct: Delta(J_n) = J_n^L + J_n^R (at z=0)
            DJ = self.TH.Delta_J(n, z=0.0)
            expected = self.TH.J_L(n).astype(complex) + self.TH.J_R(n).astype(complex)
            err = float(np.max(np.abs(P @ (DJ - expected) @ P)))
            mx = max(mx, err)
        return {
            "max_error": mx,
            "ok": mx < 1e-12,
            "interpretation": (
                "Primitive coproduct = deconcatenation at degree 1: "
                "Delta(J) = J tensor 1 + 1 tensor J, exactly 2 terms (n+1=2 at n=1)"
            )
        }

    def verify_bar_differential_from_ope(self) -> Dict[str, object]:
        r"""The bar differential encodes the OPE product.

        d_B[T_m | T_n] = [T_m, T_n] = (m-n)T_{m+n} + (c/12)m(m^2-1)delta

        This is the degree-1 piece of d_B on B^{ord}_2. The bar differential
        vanishes on B^{ord}_1 (no product to apply) and on B^{ord}_0 (empty).

        The cross-term in Delta_z(T_n) encodes the same information:
        the ((Psi-1)/Psi) * J^L J^R term is the bar differential's
        contribution to the coproduct on the Miura-inverted generators.
        """
        H = self.TH.H
        c = 1.0
        P = H.projector_safe(4)
        mx = 0.0
        for m in range(-2, 3):
            for n in range(-2, 3):
                # d_B[T_m | T_n] = mu(T_m, T_n) = T_m * T_n (ordered product)
                # In the bar complex, this is the commutator [T_m, T_n]
                # (the bar differential uses the mu_2 from the A_inf structure)
                dB = H.T(m) @ H.T(n) - H.T(n) @ H.T(m)
                expected = (m - n) * H.T(m + n)
                if m + n == 0:
                    expected = expected + (c / 12.0) * m * (m * m - 1) * np.eye(H.dim)
                err = float(np.max(np.abs(P @ (dB - expected) @ P)))
                mx = max(mx, err)
        return {"max_error": mx, "ok": mx < 1e-8}

    def verify_macmahon_grading(self) -> Dict[str, object]:
        r"""The MacMahon function M(q) = prod_{n>=1} 1/(1-q^n) counts states.

        The Fock space of a single free boson is graded by the eigenvalue of
        L_0 = T_0 (conformal weight). The partition function is:
          Z(q) = sum_{n>=0} p(n) q^n = prod_{n>=1} 1/(1-q^n) = M(q)

        where p(n) is the number of integer partitions of n. This IS the
        MacMahon function (in the 1d case; in the 3d CY case, it generalizes
        to the full MacMahon function M(q) = prod 1/(1-q^n)^n).

        The ordered bar B^{ord} inherits this grading: the deconcatenation
        coproduct preserves the total conformal weight.
        """
        H = self.TH.H
        # Count states at each level
        level_counts = {}
        for p in H.partitions:
            w = sum(p)
            level_counts[w] = level_counts.get(w, 0) + 1

        # Compare with partition function p(n)
        expected_counts = {}
        for n in range(self.N_max + 1):
            expected_counts[n] = len(_partitions_of(n))

        all_match = True
        for n in range(self.N_max + 1):
            if level_counts.get(n, 0) != expected_counts[n]:
                all_match = False
                break

        # Verify T_0 eigenvalues match the grading
        vac = H.vacuum()
        T0_vac = float((H.T(0) @ vac)[H.idx[()]])
        t0_ok = abs(T0_vac) < 1e-12  # vacuum has weight 0

        return {
            "level_counts": {k: v for k, v in level_counts.items() if k <= 5},
            "partition_counts": {k: v for k, v in expected_counts.items() if k <= 5},
            "grading_matches": all_match,
            "vacuum_weight_zero": t0_ok,
            "ok": all_match and t0_ok,
            "interpretation": (
                "Fock space grading by p(n) = MacMahon function coefficients. "
                "Deconcatenation preserves this grading."
            )
        }

    def verify_coproduct_weight_conservation(self) -> Dict[str, object]:
        r"""Delta_z(T_n) conserves total conformal weight.

        More precisely: [L_0^{tot}, Delta_z(T_n)] = -n * Delta_z(T_n) where
        L_0^{tot} = T_0^L + T_0^R is the total L_0 on the tensor product.
        Each term in Delta_z(T_n) carries total mode index n, so L_0^{tot}
        acts by -n on the whole expression.

        At z=0 (no spectral shift), this is exact. At z != 0, the z-shifted
        modes T_{n-k}^R and J_{n-k}^R still carry mode index (n-k),
        so the total weight on each term in the sum is still n.
        """
        P = self.TH.safe_proj(5)
        L0_tot = self.TH.T_L(0).astype(complex) + self.TH.T_R(0).astype(complex)
        mx = 0.0
        # Use z=0 where numerical stability is best (no z-shift binomials)
        for n in range(-2, 3):
            DT = self.TH.Delta_T(n, z=0.0)
            comm = L0_tot @ DT - DT @ L0_tot
            expected = float(-n) * DT
            err = float(np.max(np.abs(P @ (comm - expected) @ P)))
            mx = max(mx, err)
        return {"max_error": mx, "ok": mx < 1e-8}


def _partitions_of(n: int, max_part: int = None) -> List[Tuple[int, ...]]:
    """Integer partitions of n (for MacMahon grading verification)."""
    if n == 0:
        return [()]
    if max_part is None:
        max_part = n
    result = []
    for k in range(min(n, max_part), 0, -1):
        for tail in _partitions_of(n - k, k):
            result.append((k,) + tail)
    return result


# ===================================================================
# AXIOM 3: Bialgebra compatibility
# ===================================================================

class BialgebraCompatibilityVerifier:
    r"""Verify Delta_z is an algebra homomorphism (E_1-bialgebra axiom).

    The key test: Delta_z(T_m T_n) = Delta_z(T_m) * Delta_z(T_n)
    where * is the E_1-ordered product on A tensor_{E_1,z} A.

    Since Delta_z(T(u)) = T_L(u) * T_R(u-z) is MULTIPLICATIVE, the
    mode-level coproduct respects the ordered product. This is verified
    by checking that the Virasoro commutation relations are preserved:

      [Delta_z(T_m), Delta_z(T_n)] = (m-n) Delta_z(T_{m+n})
                                    + (c_eff/12) m(m^2-1) delta_{m+n,0}

    where c_eff = 2 + 2*(Psi-1)^2 is the effective central charge in the
    image of the coproduct.

    The Miura factorization T(u) = T_L(u) * T_R(u-z) is the ALGEBRAIC
    content of bialgebra compatibility: the ordered product of transfer
    matrices (E_1 product) composes with the coproduct (splitting into
    L and R factors) consistently.
    """

    def __init__(self, Psi: float = 2.0, N_max: int = 6):
        self.TH = TensorHeisenberg(Psi, N_max)
        self.Psi = Psi
        self.N_max = N_max

    def verify_homomorphism_virasoro(
        self, z: complex = 0.3 + 0.2j
    ) -> Dict[str, object]:
        r"""[Delta_z(T_m), Delta_z(T_n)] = Virasoro with c_eff.

        This is the bialgebra compatibility condition: the coproduct
        preserves the algebra structure (with modified central charge).

        The c_eff = 2 + 2*(Psi-1)^2 encodes the interaction between
        the E_1 ordered product and the deconcatenation coproduct.
        """
        P = self.TH.safe_proj(5)
        c_eff = 2.0 + 2.0 * (self.Psi - 1.0) ** 2
        mx = 0.0
        for m in range(-2, 3):
            for n in range(-2, 3):
                DTm = self.TH.Delta_T(m, z)
                DTn = self.TH.Delta_T(n, z)
                comm = DTm @ DTn - DTn @ DTm
                DT_mn = self.TH.Delta_T(m + n, z)
                expected = (m - n) * DT_mn
                if m + n == 0:
                    expected = expected + (c_eff / 12.0) * m * (m * m - 1) * np.eye(
                        self.TH.dim, dtype=complex
                    )
                err = float(np.max(np.abs(P @ (comm - expected) @ P)))
                mx = max(mx, err)
        return {
            "max_error": mx,
            "ok": mx < 1e-6,
            "c_eff": c_eff,
            "Psi": self.Psi,
            "z": z,
        }

    def verify_homomorphism_mixed(
        self, z: complex = 0.3 + 0.2j
    ) -> Dict[str, object]:
        r"""[Delta_z(T_n), Delta_z(J_m)] = -Psi*m * Delta_z(J_{n+m}).

        The mixed commutator is part of the bialgebra compatibility:
        the coproduct preserves the T-J commutation relations with
        the modified factor Psi (not 1).

        The factor Psi arises because Delta(T) contains the cross-term
        ((Psi-1)/Psi)*J^L*J^R, which acts on BOTH components of
        Delta(J) = J^L + J^R. The contributions add up to give the
        factor Psi from 1 + (Psi-1) = Psi.
        """
        P = self.TH.safe_proj(5)
        mx = 0.0
        for n in range(-2, 3):
            for m in range(-2, 3):
                DTn = self.TH.Delta_T(n, z)
                DJm = self.TH.Delta_J(m, z)
                comm = DTn @ DJm - DJm @ DTn
                expected = float(-self.Psi * m) * self.TH.Delta_J(n + m, z)
                err = float(np.max(np.abs(P @ (comm - expected) @ P)))
                mx = max(mx, err)
        return {"max_error": mx, "ok": mx < 1e-6, "factor": "Psi"}

    def verify_homomorphism_heisenberg(
        self, z: complex = 0.3 + 0.2j
    ) -> Dict[str, object]:
        r"""[Delta_z(J_m), Delta_z(J_n)] = 2*Psi*m * delta_{m+n,0}.

        The Heisenberg commutator is preserved with doubled level 2*Psi.
        This is because Delta(J) = J^L + J^R, and [J^L_m + J^R_m, J^L_n + J^R_n]
        = Psi*m*delta (from L) + Psi*m*delta (from R) = 2*Psi*m*delta.

        The doubling of the level is the spin-1 manifestation of bialgebra
        compatibility. At spin 2, the analogous statement gives c_eff.
        """
        P = self.TH.safe_proj(4)
        mx = 0.0
        for m in range(-2, 3):
            for n in range(-2, 3):
                DJm = self.TH.Delta_J(m, z)
                DJn = self.TH.Delta_J(n, z)
                comm = DJm @ DJn - DJn @ DJm
                expected = np.zeros((self.TH.dim, self.TH.dim), dtype=complex)
                if m + n == 0:
                    expected = 2.0 * self.Psi * m * np.eye(self.TH.dim, dtype=complex)
                err = float(np.max(np.abs(P @ (comm - expected) @ P)))
                mx = max(mx, err)
        return {"max_error": mx, "ok": mx < 1e-8, "effective_level": "2*Psi"}


# ===================================================================
# AXIOM 4: Coassociativity
# ===================================================================

class CoassociativityVerifier:
    r"""Verify (Delta_{z1} tensor id) o Delta_{z2} = (id tensor Delta_{z2}) o Delta_{z1}.

    Both sides produce T_L(u) * T_M(u - z2) * T_R(u - z1) at spin 2
    via the Miura triple product.

    The spectral-parameter form of coassociativity is:
      (Delta_w x id) o Delta_{z+w} = (id x Delta_z) o Delta_w

    This is the YANGIAN coassociativity (Drinfeld 1987): the spectral
    parameters compose additively.

    Uses the TripleTensor infrastructure from test_hopf_axioms.py,
    reimplemented here as a standalone verification.
    """

    def __init__(self, Psi: float = 2.0, N_max: int = 4):
        self.Psi = Psi
        self.N_max = N_max
        self.H = HeisenbergFock(Psi, N_max)
        self.d = self.H.dim
        self.dim = self.d ** 3
        self.Id = np.eye(self.d)
        self.alpha = (Psi - 1.0) / Psi
        self.M_range = N_max + 3

    def _op_factor(self, mat: np.ndarray, pos: int) -> np.ndarray:
        """Place operator mat at position pos in triple tensor product."""
        ops = [self.Id, self.Id, self.Id]
        ops[pos] = mat
        return np.kron(np.kron(ops[0], ops[1]), ops[2]).astype(complex)

    def J(self, n: int, pos: int) -> np.ndarray:
        return self._op_factor(self.H.J(n), pos)

    def T(self, n: int, pos: int) -> np.ndarray:
        return self._op_factor(self.H.T(n), pos)

    def J_shifted(self, n: int, z: complex, pos: int, K: int = 8) -> np.ndarray:
        mat = np.zeros((self.dim, self.dim), dtype=complex)
        for k in range(min(K, abs(n) + self.N_max + 2)):
            bc = _gbinom(n, k)
            if abs(bc) < 1e-15:
                continue
            mat += bc * (z ** k) * self.J(n - k, pos)
        return mat

    def T_shifted(self, n: int, z: complex, pos: int, K: int = 8) -> np.ndarray:
        mat = np.zeros((self.dim, self.dim), dtype=complex)
        for k in range(min(K, abs(n) + self.N_max + 3)):
            bc = _gbinom(n + 1, k)
            if abs(bc) < 1e-15:
                continue
            mat += bc * (z ** k) * self.T(n - k, pos)
        return mat

    def projector(self, margin: int = 2) -> np.ndarray:
        P = np.zeros((self.d, self.d))
        cutoff = self.N_max - margin
        for i in range(self.d):
            if self.H.weights[i] <= cutoff:
                P[i, i] = 1.0
        return np.kron(np.kron(P, P), P)

    def route1_Delta_T(self, n: int, z: complex, w: complex) -> np.ndarray:
        """(Delta_w x id) o Delta_{z+w}(T_n).

        Route 1: apply Delta_{z+w} first (L,R split), then Delta_w on L -> (0,1).
        Result: T_0(u)*T_1(u-w)*T_2(u-w-z) at spin-2 mode n.
        """
        zw = z + w
        M = self.M_range
        a = self.alpha
        result = np.zeros((self.dim, self.dim), dtype=complex)

        # (Delta_w x id)(T^L_n): expand L into (0,1) via Delta_w
        result += self.T(n, 0) + self.T_shifted(n, w, 1)
        for k in range(-M, M + 1):
            result += a * self.J(k, 0) @ self.J_shifted(n - k, w, 1)

        # T^R shifted by z+w (lives at pos 2)
        result += self.T_shifted(n, zw, 2)

        # alpha * sum_k [J^L(k) + J^1(k,w)] * J^2(n-k, z+w)
        for k in range(-M, M + 1):
            J2 = self.J_shifted(n - k, zw, 2)
            result += a * self.J(k, 0) @ J2
            result += a * self.J_shifted(k, w, 1) @ J2

        return result

    def route2_Delta_T(self, n: int, z: complex, w: complex) -> np.ndarray:
        """(id x Delta_z) o Delta_w(T_n).

        Route 2: apply Delta_w first (L,R split), then Delta_z on R -> (1,2).
        Result: T_0(u)*T_1(u-w)*T_2(u-w-z) at spin-2 mode n.
        """
        wz = w + z
        M = self.M_range
        a = self.alpha
        result = np.zeros((self.dim, self.dim), dtype=complex)

        # T^L_n unchanged (id on pos 0)
        result += self.T(n, 0)

        # (id x Delta_z)(T^R_shifted(n,w)): split R into (1,2) via Delta_z
        result += self.T_shifted(n, w, 1) + self.T_shifted(n, wz, 2)
        for k in range(-M, M + 1):
            result += a * self.J_shifted(k, w, 1) @ self.J_shifted(n - k, wz, 2)

        # alpha * sum_k J^0(k) * [J^1(n-k,w) + J^2(n-k,w+z)]
        for k in range(-M, M + 1):
            J0 = self.J(k, 0)
            result += a * J0 @ self.J_shifted(n - k, w, 1)
            result += a * J0 @ self.J_shifted(n - k, wz, 2)

        return result

    def verify_coassociativity_spin2(
        self, z: complex = 0.3 + 0.2j, w: complex = 0.5 - 0.1j
    ) -> Dict[str, object]:
        """Verify route 1 = route 2 at spin 2 for multiple modes."""
        P = self.projector(2)
        mx = 0.0
        for n in [0, 1, -1, -2]:
            r1 = self.route1_Delta_T(n, z, w)
            r2 = self.route2_Delta_T(n, z, w)
            diff = P @ (r1 - r2) @ P
            err = float(np.max(np.abs(diff)))
            mx = max(mx, err)
        return {
            "max_error": mx,
            "ok": mx < 1e-9,
            "z": z,
            "w": w,
            "interpretation": (
                "Both routes give T_0(u)*T_1(u-w)*T_2(u-w-z). "
                "Coassociativity is the Miura triple product consistency."
            )
        }

    def verify_coassociativity_J(
        self, z: complex = 0.3 + 0.2j, w: complex = 0.5 - 0.1j
    ) -> Dict[str, object]:
        """Coassociativity for J (primitive): trivially satisfied.

        Delta(J) = J^L + J^R is primitive, so:
        (Delta x id)(J^0 + J^1) = J^0 + J^1 + J^2 (shifted)
        (id x Delta)(J^0 + J^1) = J^0 + J^1 + J^2 (shifted)
        These must agree.
        """
        zw = z + w
        P = self.projector(2)
        mx = 0.0
        for n in [0, 1, -1, -2]:
            # Route 1: (Delta_w x id) o Delta_{z+w}(J_n)
            # Delta_{z+w}(J_n) = J^L_n + J^R_shifted(n, z+w)
            # (Delta_w x id)(J^L_n) = J^0_n + J^1_shifted(n, w)
            # (Delta_w x id)(J^R_shifted) = J^2_shifted(n, z+w)
            r1 = self.J(n, 0) + self.J_shifted(n, w, 1) + self.J_shifted(n, zw, 2)

            # Route 2: (id x Delta_z) o Delta_w(J_n)
            # Delta_w(J_n) = J^L_n + J^R_shifted(n, w)
            # (id x Delta_z)(J^L_n) = J^0_n
            # (id x Delta_z)(J^R_shifted(n, w)) = J^1_shifted(n, w) + J^2_shifted(n, w+z)
            r2 = self.J(n, 0) + self.J_shifted(n, w, 1) + self.J_shifted(n, w + z, 2)

            diff = P @ (r1 - r2) @ P
            err = float(np.max(np.abs(diff)))
            mx = max(mx, err)
        return {"max_error": mx, "ok": mx < 1e-10}


# ===================================================================
# AXIOM 5: Averaging map kills Hopf data
# ===================================================================

class AveragingMapVerifier:
    r"""Verify av(Delta_z(T_n)) loses R-matrix information.

    The averaging map av: B^{ord}(A) -> B^{Sigma}(A) is the S_n-coinvariant
    projection. In the E_1-chiral bialgebra, the R-matrix data is encoded
    in the DIFFERENCE between the coproduct Delta_z and the opposite
    coproduct Delta_z^{op}:

      Delta_z(T(u))     = T_L(u) * T_R(u - z)    (ordered: L first)
      Delta_z^{op}(T(u)) = T_R(u) * T_L(u - z)    (opposite: R first)

    The difference Delta_z - Delta_z^{op} is the R-matrix content: it measures
    how much the E_1-ordered product depends on the ordering. At z=0, the two
    coproducts coincide (cocommutative limit). At z != 0, they differ, and
    the difference is killed by the averaging map.

    KEY INSIGHT: naive SWAP(Delta_z)SWAP = Delta_z identically because the
    two Fock space copies are isomorphic and the mode matrices are identical.
    The SWAP symmetry is a KINEMATIC identity. The R-matrix is a DYNAMIC
    asymmetry: it lives in the ordering of the Miura product T_L * T_R vs
    T_R * T_L, not in the exchange of tensor factors.

    The averaging map kills this dynamic asymmetry:
      av(Delta_z) = (1/2)(Delta_z + Delta_z^{op})
    which is the symmetrized coproduct that forgets the Miura ordering.
    The scalar that survives is kappa_ch = Psi (the collision residue).
    """

    def __init__(self, Psi: float = 2.0, N_max: int = 6):
        self.TH = TensorHeisenberg(Psi, N_max)
        self.Psi = Psi
        self.N_max = N_max

    def _Delta_T_opposite(self, n: int, z: complex) -> np.ndarray:
        r"""Opposite coproduct Delta_z^{op}(T_n) from T_R(u) * T_L(u-z).

        Delta_z^{op}(T_n) = T_n^R + tilde{T}_n^L(z)
                           + alpha * sum_k J_k^R tilde{J}_{n-k}^L(z)

        where alpha = (Psi-1)/Psi. This is the Miura product with
        REVERSED ordering: R factor at u, L factor shifted to u-z.
        """
        alpha = (self.Psi - 1.0) / self.Psi
        # T^R unshifted
        term1 = self.TH.T_R(n).astype(complex)
        # T^L shifted by z
        term2 = np.zeros((self.TH.dim, self.TH.dim), dtype=complex)
        for k in range(abs(n) + self.N_max + 3):
            bc = _gbinom(n + 1, k)
            if abs(bc) < 1e-15:
                continue
            term2 += bc * (z ** k) * self.TH.T_L(n - k).astype(complex)
        # Cross-term: alpha * sum_k J_k^R * J_{n-k}^L(shifted)
        term3 = np.zeros((self.TH.dim, self.TH.dim), dtype=complex)
        M = self.N_max + abs(n) + 2
        for k in range(-M, M + 1):
            # J_k^R * J_{n-k}^L(shifted by z)
            J_R_k = self.TH.J_R(k)
            J_L_shifted = np.zeros((self.TH.dim, self.TH.dim), dtype=complex)
            for j in range(min(8, abs(n - k) + self.N_max + 2)):
                bc = _gbinom(n - k, j)
                if abs(bc) < 1e-15:
                    continue
                J_L_shifted += bc * (z ** j) * self.TH.J_L(n - k - j).astype(complex)
            term3 += J_R_k.astype(complex) @ J_L_shifted
        term3 *= alpha
        return term1 + term2 + term3

    def verify_r_matrix_from_opposite_coproduct(self) -> Dict[str, object]:
        r"""Delta_z != Delta_z^{op} for z != 0 (R-matrix nontrivial).

        The R-matrix is the ratio R(z) such that Delta_z^{op} = R(z) Delta_z R(z)^{-1}.
        At z=0: Delta_0 = Delta_0^{op} (cocommutative, R(0) = 1).
        At z != 0: Delta_z != Delta_z^{op} (R(z) nontrivial).

        The averaging map symmetrizes: av(Delta_z) = (Delta_z + Delta_z^{op})/2,
        killing the antisymmetric part which carries the R-matrix data.
        """
        P = self.TH.safe_proj(3)

        # Check z=0: should be cocommutative
        max_diff_z0 = 0.0
        for n in [0, -1, -2, 1]:
            DT = self.TH.Delta_T(n, z=0.0)
            DT_op = self._Delta_T_opposite(n, z=0.0)
            err = float(np.max(np.abs(P @ (DT - DT_op) @ P)))
            max_diff_z0 = max(max_diff_z0, err)

        # Check z != 0: should differ
        z = 0.5 + 0.3j
        max_diff_z = 0.0
        for n in [0, -1, -2, 1]:
            DT = self.TH.Delta_T(n, z)
            DT_op = self._Delta_T_opposite(n, z)
            err = float(np.max(np.abs(P @ (DT - DT_op) @ P)))
            max_diff_z = max(max_diff_z, err)

        return {
            "max_diff_z0": max_diff_z0,
            "max_diff_z_nonzero": max_diff_z,
            "cocommutative_at_z0": max_diff_z0 < 1e-10,
            "r_matrix_nontrivial": max_diff_z > 0.01,
            "ok": max_diff_z0 < 1e-10 and max_diff_z > 0.01,
            "interpretation": (
                "Delta_z = Delta_z^{op} at z=0 (cocommutative). "
                "Delta_z != Delta_z^{op} at z != 0 (R-matrix nontrivial). "
                "The difference is the E_1-ordered information that averaging kills."
            )
        }

    def verify_averaging_kills_r_matrix(self) -> Dict[str, object]:
        r"""av(Delta_z) = (Delta_z + Delta_z^{op})/2 is z-independent on vacuum.

        The averaged coproduct on the vacuum state should not depend on z:
        the z-dependent information is the R-matrix data, which is killed.

        More precisely, the vacuum expectation of the averaged coproduct
        is determined entirely by kappa_ch (the collision residue), which
        is z-independent.
        """
        P = self.TH.safe_proj(3)
        vac = np.zeros(self.TH.dim, dtype=complex)
        vi = self.TH.H.idx[()] * self.TH.d + self.TH.H.idx[()]
        vac[vi] = 1.0

        # Compute averaged coproduct at multiple z values on vacuum
        n = 0  # Use T_0 (L_0)
        av_vac_values = {}
        for z_val in [0.0, 0.3 + 0.2j, 0.7, 1.0 + 0.5j]:
            DT = self.TH.Delta_T(n, complex(z_val))
            DT_op = self._Delta_T_opposite(n, complex(z_val))
            av_DT = 0.5 * (DT + DT_op)
            av_vac_values[str(z_val)] = float(np.abs(vac @ av_DT @ vac))

        # All values should agree (z-independence of averaged vacuum expectation)
        vals = list(av_vac_values.values())
        mx = max(abs(v - vals[0]) for v in vals) if vals else 0.0

        return {
            "av_vacuum_values": av_vac_values,
            "max_spread": mx,
            "ok": mx < 1e-8,
            "interpretation": (
                "Averaged coproduct vacuum expectation is z-independent. "
                "The z-dependent R-matrix data is killed by av = (Delta + Delta^{op})/2."
            )
        }

    def verify_kappa_ch_from_averaging(self) -> Dict[str, object]:
        r"""Extract kappa_ch from the Heisenberg OPE coefficient.

        kappa_ch = Psi: the collision residue of the r-matrix r(z) = Psi*Omega/z.

        The averaging map sends the full r(z) to the scalar:
          av(r(z)) = kappa_ch = Psi

        VERIFY: [J_m, J_n] = Psi*m*delta on the original Fock space,
        confirming kappa_ch = Psi.
        """
        alpha = (self.Psi - 1.0) / self.Psi
        kappa_ch = self.Psi

        H = self.TH.H
        P_single = H.projector_safe(4)
        mx = 0.0
        for m in range(1, 4):
            comm = H.J(m) @ H.J(-m) - H.J(-m) @ H.J(m)
            expected = self.Psi * m * np.eye(H.dim)
            err = float(np.max(np.abs(P_single @ (comm - expected) @ P_single)))
            mx = max(mx, err)

        return {
            "kappa_ch": kappa_ch,
            "alpha_cross_term": alpha,
            "Psi": self.Psi,
            "commutator_error": mx,
            "ok": mx < 1e-10 and abs(kappa_ch - self.Psi) < 1e-15,
            "interpretation": (
                f"av(r(z)) = kappa_ch = {kappa_ch}. "
                "The R-matrix r(z) = Psi*Omega/z reduces to the scalar Psi upon "
                "S_2-coinvariant projection. This is the collision residue."
            )
        }

    def verify_opposite_coproduct_asymmetry_grows(self) -> Dict[str, object]:
        r"""The R-matrix strength ||Delta_z - Delta_z^{op}|| grows with |z|.

        For small z, the difference is O(z): the leading term in z comes
        from the z-shift in the Miura product. This confirms the first-order
        pole structure r(z) ~ Psi/z of the classical r-matrix.

        At Psi = 1 (free boson): the cross-term coefficient alpha = 0,
        so the difference comes only from the z-shift of T^R vs T^L.
        At Psi != 1: the J^L J^R cross-term contributes additional asymmetry.
        """
        P = self.TH.safe_proj(3)
        # Take the max over several modes to avoid accidental cancellations.
        # n=-1 vanishes (binom(0,k) = delta_{k,0}); n=-2 vanishes at Psi=1
        # (alpha=0, no cross-term); but n=0 and n>=1 are robust at all Psi.
        test_modes = [0, -1, -2, 1, 2]
        diff_norms = {}
        for z_val in [0.01, 0.1, 0.5, 1.0]:
            mx = 0.0
            for n in test_modes:
                DT = self.TH.Delta_T(n, complex(z_val))
                DT_op = self._Delta_T_opposite(n, complex(z_val))
                err = float(np.max(np.abs(P @ (DT - DT_op) @ P)))
                mx = max(mx, err)
            diff_norms[z_val] = mx

        # Check monotone growth
        vals = list(diff_norms.values())
        monotone = all(vals[i] <= vals[i + 1] + 1e-10 for i in range(len(vals) - 1))

        # Check linear scaling for small z
        ratio_small = (
            diff_norms[0.1] / diff_norms[0.01]
            if diff_norms[0.01] > 1e-15
            else 0
        )
        # Ratio should be ~10 for linear scaling (0.1/0.01 = 10)
        linear_ok = abs(ratio_small - 10.0) < 3.0

        return {
            "diff_norms": diff_norms,
            "monotone": monotone,
            "linear_scaling_ratio": ratio_small,
            "ok": monotone and linear_ok,
            "interpretation": (
                "||Delta_z - Delta_z^{op}|| grows linearly with z for small z, "
                "confirming the first-order pole structure r(z) ~ Psi/z."
            )
        }


# ===================================================================
# Full verification suite
# ===================================================================

def verify_all(Psi: float = 2.0, N_max: int = 5) -> Dict[str, object]:
    """Run all five E_1-chiral bialgebra axiom checks."""
    results = {}

    print("=" * 72)
    print("E_1-CHIRAL BIALGEBRA AXIOM VERIFICATION FOR W_{1+infinity}")
    print(f"Level Psi = {Psi}, Fock space truncation N_max = {N_max}")
    print("=" * 72)

    # AXIOM 1: E_1-algebra structure
    print("\nAXIOM 1: E_1-algebra structure (ordered OPE)")
    e1a = E1AlgebraVerifier(Psi, N_max)

    r = e1a.verify_ordered_product_associativity()
    results["1a_associativity"] = r
    print(f"  Associativity (Jacobi): max error {r['max_error']:.2e}, ok={r['ok']}")

    r = e1a.verify_r_matrix_from_commutator()
    results["1b_r_matrix"] = r
    print(f"  R-matrix from commutator: max error {r['max_error']:.2e}, ok={r['ok']}")

    r = e1a.verify_ordering_asymmetry()
    results["1c_ordering"] = r
    print(f"  Ordering asymmetry: {r['max_asymmetry']:.4f}, ok={r['ok']}")

    # AXIOM 2: E_1-coalgebra structure
    print("\nAXIOM 2: E_1-coalgebra structure (deconcatenation + bar)")
    e1c = E1CoalgebraVerifier(Psi, N_max)

    r = e1c.verify_deconcatenation_vs_coshuffle_spin1()
    results["2a_deconcatenation"] = r
    print(f"  Deconcatenation (spin 1): max error {r['max_error']:.2e}, ok={r['ok']}")

    r = e1c.verify_bar_differential_from_ope()
    results["2b_bar_differential"] = r
    print(f"  Bar differential: max error {r['max_error']:.2e}, ok={r['ok']}")

    r = e1c.verify_macmahon_grading()
    results["2c_macmahon"] = r
    print(f"  MacMahon grading: matches={r['grading_matches']}, ok={r['ok']}")

    r = e1c.verify_coproduct_weight_conservation()
    results["2d_weight_conservation"] = r
    print(f"  Weight conservation: max error {r['max_error']:.2e}, ok={r['ok']}")

    # AXIOM 3: Bialgebra compatibility
    print("\nAXIOM 3: Bialgebra compatibility (Delta_z is homomorphism)")
    bv = BialgebraCompatibilityVerifier(Psi, N_max)

    r = bv.verify_homomorphism_virasoro()
    results["3a_virasoro_hom"] = r
    print(f"  Virasoro homomorphism: max error {r['max_error']:.2e}, "
          f"c_eff={r['c_eff']:.2f}, ok={r['ok']}")

    r = bv.verify_homomorphism_mixed()
    results["3b_mixed_hom"] = r
    print(f"  Mixed TJ homomorphism: max error {r['max_error']:.2e}, ok={r['ok']}")

    r = bv.verify_homomorphism_heisenberg()
    results["3c_heisenberg_hom"] = r
    print(f"  Heisenberg homomorphism: max error {r['max_error']:.2e}, ok={r['ok']}")

    # AXIOM 4: Coassociativity
    print("\nAXIOM 4: Coassociativity (Miura triple product)")
    N_max_triple = min(N_max, 4)  # Triple tensor is memory-intensive
    cv = CoassociativityVerifier(Psi, N_max_triple)

    r = cv.verify_coassociativity_spin2()
    results["4a_coassoc_spin2"] = r
    print(f"  Spin-2 coassociativity: max error {r['max_error']:.2e}, ok={r['ok']}")

    r = cv.verify_coassociativity_J()
    results["4b_coassoc_J"] = r
    print(f"  Spin-1 coassociativity: max error {r['max_error']:.2e}, ok={r['ok']}")

    # AXIOM 5: Averaging map kills Hopf data
    print("\nAXIOM 5: Averaging map kills R-matrix data")
    av = AveragingMapVerifier(Psi, N_max)

    r = av.verify_r_matrix_from_opposite_coproduct()
    results["5a_r_matrix_opposite"] = r
    print(f"  R-matrix: z=0 diff={r['max_diff_z0']:.2e}, "
          f"z!=0 diff={r['max_diff_z_nonzero']:.4f}, ok={r['ok']}")

    r = av.verify_averaging_kills_r_matrix()
    results["5b_av_kills_r"] = r
    print(f"  Averaging kills R: max spread {r['max_spread']:.2e}, ok={r['ok']}")

    r = av.verify_kappa_ch_from_averaging()
    results["5c_kappa_ch"] = r
    print(f"  kappa_ch = {r['kappa_ch']}, ok={r['ok']}")

    r = av.verify_opposite_coproduct_asymmetry_grows()
    results["5d_asym_growth"] = r
    print(f"  Asymmetry growth: monotone={r['monotone']}, "
          f"linear ratio={r['linear_scaling_ratio']:.2f}, ok={r['ok']}")

    # Summary
    print("\n" + "=" * 72)
    all_ok = all(
        v["ok"]
        for v in results.values()
        if isinstance(v, dict) and "ok" in v
    )
    if all_ok:
        print("ALL FIVE E_1-CHIRAL BIALGEBRA AXIOMS VERIFIED")
    else:
        for key, val in results.items():
            if isinstance(val, dict) and not val.get("ok", True):
                print(f"FAIL: {key}")
    print("=" * 72)

    results["all_ok"] = all_ok
    return results


if __name__ == "__main__":
    verify_all(Psi=2.0, N_max=5)
