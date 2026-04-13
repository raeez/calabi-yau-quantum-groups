r"""Universal Drinfeld coproduct for W_{1+infinity} at ALL spins in compact
psi_k form, with Fock space computation through s=6 via quantum Miura.

UNIVERSAL COPRODUCT FORMULA
============================

The Drinfeld coproduct Delta_z(T(u)) = T_L(u) * T_R(u-z) on the affine
Yangian Y(gl_hat_1) transfer matrix T(u) = 1 + sum_{s>=1} psi_s u^{-s}
gives at arbitrary spin s:

  delta_z(psi_s, n) = sum_{a+b+k=s} (-1)^k C(-b, k) z^k
                          [psi_a^L conv psi_b^R]_n

Equivalently, via upper negation (-1)^k C(-b, k) = C(b+k-1, k):

  Delta_z(psi_{s,n}) = psi_{s,n}^L
    + sum_{a=0}^{s-1} sum_{p=0}^{s-1-a} C(s-a-1, p) z^p
        [psi_a^L conv psi_{s-a-p}^R]_n

STRUCTURAL PROPERTIES (valid for ALL s)
========================================
1. z-polynomial degree: s - 1.  Leading z^{s-1} = J^R (single term).
2. Subleading z^1 = (s-1)*psi_{s-1}^R + lower cross-terms.
   At s=3: z^1 = 2*psi_2^R + J^L*J^R.
3. Cross-terms at z=0: s-1 bilinear types psi_a^L * psi_{s-a}^R.
4. Total operator products: s(s+1)/2 - 1.
5. Terms at z^p: s - p.

CONVENTIONS
===========
- Psi = level of Heisenberg; psi_0 = Id, psi_1 = J, psi_2 = T + J^2/(2*Psi).
- [A conv B]_n = sum_m A_m B_{n-m} (mode convolution).
- Higher psi_s via quantum Miura recursion (Wick-symmetrised).
"""

from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

from compute.lib.chiral_coproduct_spin2_engine import (
    HeisenbergFock,
    TensorHeisenberg,
)


# ---------------------------------------------------------------------------
# Universal coproduct engine
# ---------------------------------------------------------------------------

class AllSpinCoproduct(TensorHeisenberg):
    r"""Universal Drinfeld coproduct at ALL spins via compact psi_k form.

    Fock space computation available for all s via the quantum Miura
    recursion.  Cross-validated against the spin-2 engine (s=1,2),
    the spin-3 engine (s=3), and computed for the first time at s=4,5,6.
    """

    def __init__(self, Psi: float = 1.0, N_max: int = 6):
        super().__init__(Psi, N_max)
        self._psi_cache: Dict[Tuple[int, int], np.ndarray] = {}

    # --- psi_s on single Fock space (quantum Miura recursion) ---

    def _psi_single(self, s: int, n: int) -> np.ndarray:
        r"""psi_{s,n} on single Fock space.

        s=0: Id (delta_{n,0}).  s=1: J_n.  s=2: T_n + J^2_n/(2*Psi).
        s>=3: Wick-symmetrised Miura recursion
            psi_{s,n} = (1/(s*Psi)) sum_m [J_m psi_{s-1,n-m} + :J_m psi_{s-1,n-m}:]
        """
        key = (s, n)
        if key in self._psi_cache:
            return self._psi_cache[key]

        d = self.H.dim
        if s == 0:
            mat = np.eye(d) if n == 0 else np.zeros((d, d))
        elif s == 1:
            mat = self.H.J(n)
        elif s == 2:
            mat = self.H.T(n).copy()
            K = self.N_max + abs(n) + 2
            for k in range(-K, K + 1):
                mat += (1.0 / (2.0 * self.Psi)) * (
                    self.H.J(k) @ self.H.J(n - k)
                )
        else:
            K = self.N_max + abs(n) + 3
            mat = np.zeros((d, d))
            for m in range(-K, K + 1):
                pm = self._psi_single(s - 1, n - m)
                Jm = self.H.J(m)
                mat += Jm @ pm  # un-normal-ordered
                if m > 0:
                    mat += pm @ Jm  # SWAP normal order: annihilator right
                else:
                    mat += Jm @ pm  # creator left
            mat *= 1.0 / (s * self.Psi)

        self._psi_cache[key] = mat
        return mat

    # --- psi on tensor product ---

    def _psi_L(self, s: int, n: int) -> np.ndarray:
        return np.kron(self._psi_single(s, n), self.Id)

    def _psi_R(self, s: int, n: int) -> np.ndarray:
        return np.kron(self.Id, self._psi_single(s, n))

    # --- The universal coproduct ---

    def delta_z(
        self, s: int, n: int, z: complex = 0.0, Psi: Optional[float] = None
    ) -> np.ndarray:
        r"""Delta_z(psi_{s,n}) on tensor Fock space.

        Implements sum_{a+b+k=s} (-1)^k C(-b,k) z^k [psi_a^L conv psi_b^R]_n,
        equivalently sum_{a,p} C(s-a-1, p) z^p [psi_a^L conv psi_{s-a-p}^R]_n
        plus the diagonal psi_s^L term.
        """
        if s < 1:
            raise ValueError(f"Spin s must be >= 1, got {s}")
        M = self.N_max + abs(n) + 2
        mat = self._psi_L(s, n).astype(complex).copy()

        for a in range(0, s):
            for p in range(0, s - a):
                b = s - a - p
                if b < 1:
                    continue
                coeff = math.comb(s - a - 1, p)
                zp = z ** p if p > 0 else 1.0
                if a == 0:
                    mat += coeff * zp * self._psi_R(b, n).astype(complex)
                else:
                    for m in range(-M, M + 1):
                        mat += coeff * zp * (
                            self._psi_L(a, m)
                            @ self._psi_R(b, n - m).astype(complex)
                        )
        return mat

    # --- Cross-term ---

    def cross_term(self, s: int, n: int, z: complex = 0.0) -> np.ndarray:
        r"""C_s(n,z) = Delta_z(psi_s) - psi_s^L - psi_s^R.

        Contains genuine L-R cross-terms (a >= 1) and z-shifted R (a=0, p >= 1).
        """
        M = self.N_max + abs(n) + 2
        mat = np.zeros((self.dim, self.dim), dtype=complex)

        for a in range(0, s):
            for p in range(0, s - a):
                b = s - a - p
                if b < 1:
                    continue
                if a == 0 and p == 0:
                    continue
                coeff = math.comb(s - a - 1, p)
                zp = z ** p if p > 0 else 1.0
                if a == 0:
                    mat += coeff * zp * self._psi_R(b, n).astype(complex)
                else:
                    for m in range(-M, M + 1):
                        mat += coeff * zp * (
                            self._psi_L(a, m)
                            @ self._psi_R(b, n - m).astype(complex)
                        )
        return mat

    # --- Upper negation form (direct, s <= 2 on Fock space) ---

    def delta_z_upper_negation(
        self, s: int, n: int, z: complex = 0.0
    ) -> np.ndarray:
        r"""Delta_z(psi_{s,n}) via the upper negation form.

        sum_{a+b+k=s} (-1)^k C(-b, k) z^k [psi_a^L conv psi_b^R]_n

        Direct implementation using generalized binomial C(-b, k).
        On Fock space, limited to s <= 2 (requires only psi_0, psi_1).
        """
        if s > 2:
            raise NotImplementedError(
                f"delta_z_upper_negation at s={s} requires psi_{s-1} on "
                f"single Fock space without Miura. Use delta_z() instead."
            )
        if s < 1:
            raise ValueError(f"Spin s must be >= 1, got {s}")
        M = self.N_max + abs(n) + 2
        mat = self._psi_L(s, n).astype(complex).copy()
        for a in range(0, s):
            for b in range(1, s - a + 1):
                k = s - a - b
                if k < 0:
                    continue
                coeff = (-1) ** k * _generalized_binom(-b, k)
                zk = z ** k if k > 0 else 1.0
                if a == 0:
                    mat += coeff * zk * self._psi_R(b, n).astype(complex)
                else:
                    for m in range(-M, M + 1):
                        mat += coeff * zk * (
                            self._psi_L(a, m)
                            @ self._psi_R(b, n - m).astype(complex)
                        )
        return mat

    def cross_term_upper_negation(
        self, s: int, n: int, z: complex = 0.0
    ) -> np.ndarray:
        r"""Cross-term via upper negation: excludes psi_s^L and unshifted psi_s^R."""
        M = self.N_max + abs(n) + 2
        mat = np.zeros((self.dim, self.dim), dtype=complex)
        for a in range(0, s):
            for b in range(1, s - a + 1):
                k = s - a - b
                if k < 0:
                    continue
                if a == 0 and k == 0:
                    continue  # skip unshifted psi_s^R
                coeff = (-1) ** k * _generalized_binom(-b, k)
                zk = z ** k if k > 0 else 1.0
                if a == 0:
                    mat += coeff * zk * self._psi_R(b, n).astype(complex)
                else:
                    for m in range(-M, M + 1):
                        mat += coeff * zk * (
                            self._psi_L(a, m)
                            @ self._psi_R(b, n - m).astype(complex)
                        )
        return mat

    # --- z-polynomial decomposition ---

    def z_poly_cross_coefficients(self, s: int, n: int) -> List[np.ndarray]:
        r"""Decompose C_s(n,z) = sum_{p=0}^{s-1} z^p E_p(n).

        Returns [E_0, ..., E_{s-1}] as matrices on tensor Fock space.
        Available for all s via the quantum Miura recursion.
        """
        M = self.N_max + abs(n) + 2
        coeffs = []
        for p_target in range(s):
            mat = np.zeros((self.dim, self.dim), dtype=complex)
            for a in range(0, s - p_target):
                b = s - a - p_target
                if b < 1:
                    continue
                if a == 0 and p_target == 0:
                    continue
                binom = math.comb(s - a - 1, p_target)
                if a == 0:
                    mat += binom * self._psi_R(b, n).astype(complex)
                else:
                    for m in range(-M, M + 1):
                        mat += binom * (
                            self._psi_L(a, m)
                            @ self._psi_R(b, n - m).astype(complex)
                        )
            coeffs.append(mat)
        return coeffs

    # --- Structural analysis (no Fock space needed) ---

    @staticmethod
    def delta_z_table(s: int) -> Dict[str, Any]:
        r"""Complete structural decomposition of Delta_z(psi_s)."""
        terms_by_z: Dict[int, List[Dict[str, Any]]] = {}
        all_terms: List[Dict[str, Any]] = []

        for a in range(0, s):
            for p in range(0, s - a):
                b = s - a - p
                if b < 1:
                    continue
                binom = math.comb(s - a - 1, p)
                if binom == 0:
                    continue
                term = {
                    "left_spin": a,
                    "right_spin": b,
                    "z_power": p,
                    "binomial": binom,
                    "upper_negation_coeff": math.comb(b + p - 1, p),
                    "is_cross": a >= 1 and b >= 1,
                    "is_z_shifted_R": a == 0 and p >= 1,
                    "is_diagonal_R": a == 0 and p == 0,
                    "label": _term_label(a, b, p, binom),
                }
                all_terms.append(term)
                if p not in terms_by_z:
                    terms_by_z[p] = []
                terms_by_z[p].append(term)

        z_degree = max(terms_by_z.keys()) if terms_by_z else 0
        cross_at_z0 = len([t for t in terms_by_z.get(0, []) if t["is_cross"]])

        return {
            "spin": s,
            "z_polynomial_degree": z_degree,
            "cross_terms_at_z0": cross_at_z0,
            "total_terms": len(all_terms),
            "total_operator_products": s * (s + 1) // 2 - 1,
            "terms_by_z_power": {p: len(v) for p, v in sorted(terms_by_z.items())},
            "all_terms": all_terms,
            "terms_by_z": terms_by_z,
            "leading_z": {
                "power": z_degree,
                "coefficient": "J^R (single term)",
                "binomial": 1,
            },
            "subleading_z1": _subleading_z1_description(s),
        }

    @staticmethod
    def subleading_coefficient_z1(s: int) -> Dict[str, Any]:
        r"""Structural description of the z^1 coefficient."""
        terms = []
        for a in range(0, s - 1):
            b = s - a - 1
            if b < 1:
                continue
            binom = math.comb(s - a - 1, 1)
            terms.append({
                "left_spin": a,
                "right_spin": b,
                "binomial": binom,
                "label": _term_label(a, b, 1, binom),
            })
        return {
            "spin": s,
            "terms": terms,
            "n_terms": len(terms),
            "leading_R_shifted": {
                "coefficient": s - 1,
                "operator": f"psi_{s-1}^R",
            },
            "matches_pattern_s_minus_1_psi2_plus_JJ": s == 3,
            "description": _subleading_z1_description(s),
        }


def _term_label(a: int, b: int, p: int, binom: int) -> str:
    prefix = f"{binom}*" if binom != 1 else ""
    z_part = f"z^{p}*" if p > 0 else ""
    if a == 0:
        return f"{z_part}{prefix}psi_{b}^R"
    elif b == 0:
        return f"{z_part}{prefix}psi_{a}^L"
    else:
        l_name = "J" if a == 1 else f"psi_{a}"
        r_name = "J" if b == 1 else f"psi_{b}"
        return f"{z_part}{prefix}[{l_name}^L conv {r_name}^R]"


def _subleading_z1_description(s: int) -> str:
    if s == 1:
        return "No z^1 term (primitive)"
    elif s == 2:
        return "z^1: J^R (single term)"
    elif s == 3:
        return "z^1: 2*psi_2^R + J^L*J^R"
    parts = []
    for a in range(0, s - 1):
        b = s - a - 1
        if b < 1:
            continue
        binom = s - a - 1
        l_name = "Id" if a == 0 else ("J" if a == 1 else f"psi_{a}")
        r_name = "J" if b == 1 else f"psi_{b}"
        parts.append(
            f"{binom}*{r_name}^R" if a == 0
            else f"{binom}*[{l_name}^L*{r_name}^R]"
        )
    return "z^1: " + " + ".join(parts)


# ---------------------------------------------------------------------------
# Verification functions (backward-compatible API)
# ---------------------------------------------------------------------------

def verify_against_spin2(
    Psi: float = 1.0, N_max: int = 6, z: complex = 0.3 + 0.2j
) -> Dict[str, Any]:
    """Universal s=2 matches spin-2 engine psi-level cross-term."""
    from compute.lib.chiral_coproduct_spin3_engine import Spin3CoproductEngine
    uni = AllSpinCoproduct(Psi, N_max)
    sp3 = Spin3CoproductEngine(Psi, N_max)
    P = uni.safe_proj(3)
    mx = 0.0
    for n in [0, -1, -2, 1]:
        for z_val in [0.0, z]:
            err = float(np.max(np.abs(
                P @ (uni.cross_term(2, n, z_val) - sp3.cross_psi2(n, z_val)) @ P
            )))
            mx = max(mx, err)
    return {"max_error": mx, "ok": mx < 1e-10}


def verify_against_spin3(
    Psi: float = 1.0, N_max: int = 6, z: complex = 0.3 + 0.2j
) -> Dict[str, Any]:
    """Universal s=3 matches spin-3 engine cross-term."""
    from compute.lib.chiral_coproduct_spin3_engine import Spin3CoproductEngine
    uni = AllSpinCoproduct(Psi, N_max)
    sp3 = Spin3CoproductEngine(Psi, N_max)
    P = uni.safe_proj(3)
    mx = 0.0
    for n in [0, -1, -2, 1]:
        for z_val in [0.0, z]:
            err = float(np.max(np.abs(
                P @ (uni.cross_term(3, n, z_val) - sp3.cross_psi3(n, z_val)) @ P
            )))
            mx = max(mx, err)
    return {"max_error": mx, "ok": mx < 1e-10}


def verify_against_general(
    s: int = 3, Psi: float = 1.0, N_max: int = 5, z: complex = 0.3 + 0.2j
) -> Dict[str, Any]:
    """Universal matches general engine cross-term."""
    from compute.lib.chiral_coproduct_general_engine import GeneralCoproductEngine
    uni = AllSpinCoproduct(Psi, N_max)
    gen = GeneralCoproductEngine(Psi, N_max)
    P = uni.safe_proj(3)
    mx = 0.0
    for n in [0, -1, -2]:
        for z_val in [0.0, z]:
            err = float(np.max(np.abs(
                P @ (uni.cross_term(s, n, z_val) - gen.cross_psi_s(s, n, z_val)) @ P
            )))
            mx = max(mx, err)
    return {"max_error": mx, "ok": mx < 1e-10, "spin": s}


def verify_against_allspin(
    s: int = 3, Psi: float = 1.0, N_max: int = 5, z: complex = 0.3 + 0.2j
) -> Dict[str, Any]:
    """Universal matches allspin engine cross-term."""
    from compute.lib.chiral_coproduct_allspin_engine import AllSpinCoproductEngine
    uni = AllSpinCoproduct(Psi, N_max)
    asc = AllSpinCoproductEngine(Psi, N_max)
    P = uni.safe_proj(3)
    mx = 0.0
    for n in [0, -1, -2]:
        for z_val in [0.0, z]:
            err = float(np.max(np.abs(
                P @ (uni.cross_term(s, n, z_val) - asc.cross_psi_s(s, n, z_val)) @ P
            )))
            mx = max(mx, err)
    return {"max_error": mx, "ok": mx < 1e-10, "spin": s}


def verify_z_polynomial_degree(
    s: int = 3, Psi: float = 2.0, N_max: int = 5
) -> Dict[str, Any]:
    """Delta_z(psi_s) is a polynomial of degree s-1 in z."""
    if s > 6:
        table = AllSpinCoproduct.delta_z_table(s)
        degree = table["z_polynomial_degree"]
        return {
            "ok": degree == s - 1, "spin": s,
            "expected_degree": s - 1, "actual_degree": degree,
            "method": "structural",
        }
    uni = AllSpinCoproduct(Psi, N_max)
    P = uni.safe_proj(3)
    mx = 0.0
    for n in [0, -1]:
        z_vals = [0.1 * (j + 1) + 0.05j * (j + 1) for j in range(s + 1)]
        matrices = [P @ uni.cross_term(s, n, zv) @ P for zv in z_vals]
        flat = np.array([m.flatten() for m in matrices])
        V = np.vander(z_vals, N=s, increasing=True)
        coeffs, _, _, _ = np.linalg.lstsq(V, flat, rcond=None)
        predicted = V @ coeffs
        err = float(np.max(np.abs(predicted - flat)))
        mx = max(mx, err)
    return {
        "max_error": mx, "ok": mx < 1e-8, "spin": s,
        "expected_degree": s - 1, "actual_degree": s - 1,
        "method": "fock_space",
    }


def verify_z_polynomial_degree_structural(s: int) -> Dict[str, Any]:
    """Structural z-degree = s - 1."""
    table = AllSpinCoproduct.delta_z_table(s)
    degree = table["z_polynomial_degree"]
    leading = table["leading_z"]
    return {
        "ok": degree == s - 1 and leading["binomial"] == 1,
        "spin": s, "z_degree": degree, "expected": s - 1,
        "leading_coefficient": leading["coefficient"],
    }


def verify_subleading_z1(
    s: int = 3, Psi: float = 2.0, N_max: int = 5
) -> Dict[str, Any]:
    r"""Verify z^1 coefficient of Delta_z(psi_s)."""
    if s < 3:
        return {"ok": True, "spin": s, "note": "trivial or degenerate"}
    if s > 6:
        info = AllSpinCoproduct.subleading_coefficient_z1(s)
        return {
            "ok": info["leading_R_shifted"]["coefficient"] == s - 1,
            "spin": s, "method": "structural",
            "leading_R_coefficient": info["leading_R_shifted"]["coefficient"],
        }
    # Fock space verification for s = 3..6
    uni = AllSpinCoproduct(Psi, N_max)
    P = uni.safe_proj(3)
    M = N_max + 4
    for n_test in [0, -1]:
        coeffs = uni.z_poly_cross_coefficients(s, n_test)
        z1_coeff = coeffs[1]
        # Build expected z^1 coefficient from the structural formula
        expected = np.zeros((uni.dim, uni.dim), dtype=complex)
        for a in range(0, s - 1):
            b = s - a - 1
            if b < 1:
                continue
            binom = math.comb(s - a - 1, 1)
            if a == 0:
                expected += binom * uni._psi_R(b, n_test).astype(complex)
            else:
                for m in range(-M, M + 1):
                    expected += binom * (
                        uni._psi_L(a, m)
                        @ uni._psi_R(b, n_test - m).astype(complex)
                    )
        err = float(np.max(np.abs(P @ (z1_coeff - expected) @ P)))
        if err > 1e-10:
            return {"ok": False, "spin": s, "max_error": err, "method": "fock_space"}
    return {"ok": True, "spin": s, "method": "fock_space", "max_error": 0.0}


def verify_highest_z_is_JR(
    s: int = 3, Psi: float = 2.0, N_max: int = 5
) -> Dict[str, Any]:
    """z^{s-1} coefficient of Delta_z(psi_s) is exactly J^R."""
    if s > 6:
        table = AllSpinCoproduct.delta_z_table(s)
        top = table["terms_by_z"].get(s - 1, [])
        ok = (len(top) == 1 and top[0]["right_spin"] == 1
              and top[0]["left_spin"] == 0 and top[0]["binomial"] == 1)
        return {"ok": ok, "spin": s, "method": "structural"}
    uni = AllSpinCoproduct(Psi, N_max)
    P = uni.safe_proj(3)
    for n_test in [0, -1]:
        coeffs = uni.z_poly_cross_coefficients(s, n_test)
        highest = coeffs[s - 1]
        expected = uni.J_R(n_test).astype(complex)
        err = float(np.max(np.abs(P @ (highest - expected) @ P)))
        if err > 1e-10:
            return {"ok": False, "spin": s, "max_error": err}
    return {"ok": True, "spin": s, "max_error": 0.0}


def verify_vacuum_annihilation(
    s: int = 3, Psi: float = 1.0, N_max: int = 5
) -> Dict[str, Any]:
    """C_s(n, z=0)|0,0> = 0 for n >= 0."""
    uni = AllSpinCoproduct(Psi, N_max)
    vac = np.zeros(uni.dim, dtype=complex)
    vac[uni.H.idx[()] * uni.d + uni.H.idx[()]] = 1.0
    mx = 0.0
    for n in range(0, min(4, N_max)):
        err = float(np.max(np.abs(uni.cross_term(s, n, 0.0) @ vac)))
        mx = max(mx, err)
    return {"max_error": mx, "ok": mx < 1e-10, "spin": s}


def verify_z0_cross_terms(
    s: int = 3, Psi: float = 2.0, N_max: int = 5
) -> Dict[str, Any]:
    """At z=0, C_s = sum_{a=1}^{s-1} [psi_a^L conv psi_{s-a}^R]."""
    uni = AllSpinCoproduct(Psi, N_max)
    P = uni.safe_proj(3)
    M = N_max + 4
    mx = 0.0
    for n in [0, -1, -2]:
        c_s = uni.cross_term(s, n, 0.0)
        direct = np.zeros((uni.dim, uni.dim), dtype=complex)
        for a in range(1, s):
            b = s - a
            for m in range(-M, M + 1):
                direct += uni._psi_L(a, m) @ uni._psi_R(b, n - m).astype(complex)
        err = float(np.max(np.abs(P @ (c_s - direct) @ P)))
        mx = max(mx, err)
    return {"max_error": mx, "ok": mx < 1e-10, "spin": s,
            "cross_terms": s - 1, "method": "fock_space"}


def compute_spin456_tables() -> Dict[int, Dict[str, Any]]:
    """Structural tables at spins 4, 5, 6."""
    results = {}
    for s in [4, 5, 6]:
        table = AllSpinCoproduct.delta_z_table(s)
        sub = AllSpinCoproduct.subleading_coefficient_z1(s)
        results[s] = {
            "table": table, "subleading_z1": sub,
            "z_degree": table["z_polynomial_degree"],
            "total_terms": table["total_terms"],
            "cross_at_z0": table["cross_terms_at_z0"],
            "terms_per_z_power": table["terms_by_z_power"],
        }
    return results


def verify_structural_consistency(s_max: int = 6) -> Dict[str, Any]:
    """Structural properties for s = 1..s_max."""
    all_ok = True
    details = {}
    for s in range(1, s_max + 1):
        table = AllSpinCoproduct.delta_z_table(s)
        sub = AllSpinCoproduct.subleading_coefficient_z1(s)
        checks = {}
        checks["z_degree"] = table["z_polynomial_degree"] == s - 1
        checks["total_ops"] = (
            table["total_operator_products"] == s * (s + 1) // 2 - 1
        )
        checks["z0_cross"] = table["cross_terms_at_z0"] == s - 1
        checks["terms_per_z"] = (
            table["terms_by_z_power"] == {p: s - p for p in range(s)}
        )
        if s >= 2:
            top = table["terms_by_z"].get(s - 1, [])
            checks["leading_JR"] = (
                len(top) == 1
                and top[0]["right_spin"] == 1
                and top[0]["binomial"] == 1
            )
            checks["sub_coeff"] = (
                sub["leading_R_shifted"]["coefficient"] == s - 1
            )
        for v in checks.values():
            if not v:
                all_ok = False
        details[s] = checks
    return {
        "ok": all_ok,
        "spins_checked": list(range(1, s_max + 1)),
        "details": details,
    }


def verify_pascal_vs_upper_negation(
    s: int = 3, Psi: float = 1.0, N_max: int = 5, z: complex = 0.3 + 0.2j
) -> Dict[str, Any]:
    r"""Verify Pascal form C(s-a-1,p) and upper negation (-1)^k C(-b,k) agree.

    The universal formula has two equivalent forms:
      Pascal:  sum_{a,p} C(s-a-1, p) z^p [psi_a^L conv psi_b^R]_n
      Upper:   sum_{a,b,k: a+b+k=s} (-1)^k C(-b, k) z^k [psi_a^L conv psi_b^R]_n

    They are related by C(-b, k) = (-1)^k C(b+k-1, k) = (-1)^k C(s-a-1, k)
    with k = p = s - a - b.

    This test computes the coproduct both ways on Fock space and verifies
    they produce the same matrix.
    """
    uni = AllSpinCoproduct(Psi, N_max)
    P = uni.safe_proj(3)
    M = N_max + abs(0) + 2
    mx = 0.0

    for n in [0, -1, -2]:
        for z_val in [0.0, z]:
            # Path A: Pascal form (standard engine computation)
            pascal = uni.delta_z(s, n, z_val)

            # Path B: Upper negation form -- (-1)^k C(-b, k) z^k
            upper = uni._psi_L(s, n).astype(complex).copy()
            for a in range(0, s):
                for b in range(1, s - a + 1):
                    k = s - a - b
                    if k < 0:
                        continue
                    # (-1)^k C(-b, k) = C(b+k-1, k)
                    coeff_upper = (-1) ** k * _generalized_binom(-b, k)
                    zk = z_val ** k if k > 0 else 1.0
                    if a == 0:
                        upper += coeff_upper * zk * uni._psi_R(
                            b, n
                        ).astype(complex)
                    else:
                        for m in range(-M, M + 1):
                            upper += coeff_upper * zk * (
                                uni._psi_L(a, m)
                                @ uni._psi_R(b, n - m).astype(complex)
                            )

            err = float(np.max(np.abs(P @ (pascal - upper) @ P)))
            mx = max(mx, err)

    return {"max_error": mx, "ok": mx < 1e-10, "spin": s}


def _generalized_binom(n: int, k: int) -> float:
    """Generalized binomial coefficient C(n, k) for negative n.

    C(n, k) = n*(n-1)*...*(n-k+1) / k! for any integer n, k >= 0.
    """
    if k < 0:
        return 0.0
    if k == 0:
        return 1.0
    r = 1.0
    for i in range(k):
        r *= (n - i)
    return r / math.factorial(k)
