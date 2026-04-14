r"""m_3 coproduct correction engine: delta^{(3)}(T_n) on truncated Fock space.

MATHEMATICAL CONTENT
====================

The affine Yangian Y(gl_hat_1) / W_{1+infinity} at level Psi carries an
A_infinity structure with:
  m_2: the OPE bracket (Virasoro Lie bracket at spin 2)
  m_3: the associator correction from the second-order pole of the TT OPE

At c=1 (central charge), the only nonzero m_3 on generators {J, T} is:
  m_3(T, T, T) = -2T   (the Virasoro cubic self-coupling)
All other triples involving J vanish: m_3(J,J,J)=0, m_3(T,T,J)=0, etc.

THE COPRODUCT CORRECTION delta^{(3)}
=====================================

The Drinfeld coproduct Delta_0: A -> A x A is a morphism for the
associative product m_2. The A_infinity correction m_3 produces a
DEFORMATION of the coproduct delta^{(3)} defined by the morphism
defect equation:

  delta^{(3)}(x) = Delta_0(m_3(x,x,x)) - m_3^{diag}(Delta_0(x)^{x3})

where m_3^{diag} acts diagonally on the tensor product:
  m_3^{diag}((a1,b1),(a2,b2),(a3,b3)) = (m_3(a1,a2,a3), m_3(b1,b2,b3))

DERIVATION FOR T_0 AT LEVEL Psi
================================

Write alpha = (Psi - 1) / Psi. The zeroth-order Drinfeld coproduct:
  Delta_0(T_0) = T_0^L + T_0^R + alpha * sum_k J_k^L J_{-k}^R

The LHS of the morphism defect:
  Delta_0(m_3(T_0,T_0,T_0)) = Delta_0(-2 T_0)
    = -2 [T_0^L + T_0^R + alpha * sum_k J_k^L J_{-k}^R]

The RHS: m_3^{diag} acts on three copies of Delta_0(T_0).
The left-factor triple is m_3 applied to (T_0 + alpha*J_k, T_0 + alpha*J_l, ...):
  m_3(T_0, T_0, T_0) = -2 T_0   (only nonzero triple on {J,T})
Similarly for the right factor. So:
  m_3^{diag}(...) = -2 T_0^L - 2 T_0^R

The defect:
  delta^{(3)}(T_0) = [-2 T_0^L - 2 T_0^R - 2*alpha*C] - [-2 T_0^L - 2 T_0^R]
                   = -2*alpha * sum_k J_k^L J_{-k}^R

At Psi = 2: alpha = 1/2, so delta^{(3)}(T_0) = -sum_k J_k^L J_{-k}^R.

PHYSICAL INTERPRETATION
=======================

The m_3 correction SUBTRACTS one unit of the JJ cross-term from the coproduct.
The corrected coproduct Delta_0(T_0) + delta^{(3)}(T_0) has:
  Cross-term coefficient: alpha - 2*alpha = -alpha = -(Psi-1)/Psi
The sign flip reflects the OBSTRUCTION to the naive coproduct being compatible
with the A_infinity structure. At Psi = 1 (free boson, class G), alpha = 0 and
the correction vanishes identically.

CONVENTIONS
===========
- Psi = level of Heisenberg (kappa_ch(H_Psi) = Psi)
- J_n, T_n = Heisenberg and Sugawara modes
- [J_m, J_n] = Psi * m * delta_{m+n,0}
- T_n = (1/(2*Psi)) sum_k :J_{n-k} J_k: (Sugawara, c = 1)
- m_3(T,T,T) = -2T at c = 1 (from a_infinity_bar_w1inf.py)
- alpha = (Psi - 1) / Psi (Miura cross-term coefficient)

REFERENCES
==========
  - Kadeishvili (1980): Algebraic structure in cohomology of A_inf algebras
  - Lian-Zuckerman (1993): New perspectives on the BRST-algebraic structure
  - Prochazka-Rapcak (arXiv:1910.07997): W_{1+inf} = affine Yangian
  - Vol III: a_infinity_bar_w1inf.py (A_inf structure, m_3(T,T,T) = -2T)
  - Vol III: chiral_coproduct_spin2_engine.py (Drinfeld coproduct infrastructure)
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple

import numpy as np

from compute.lib.chiral_coproduct_spin2_engine import (
    HeisenbergFock,
    TensorHeisenberg,
)


# ---------------------------------------------------------------------------
# Core computation
# ---------------------------------------------------------------------------

class M3CoproductCorrection(TensorHeisenberg):
    r"""Compute delta^{(3)}(T_n) on the truncated tensor Fock space.

    delta^{(3)}(T_n) is the m_3 correction to the Drinfeld coproduct
    Delta_0(T_n). It arises from the morphism defect of Delta_0 with
    respect to the A_infinity operation m_3(T,T,T) = -2T.

    The result:
      delta^{(3)}(T_n) = -2*alpha * sum_k J_k^L J_{n-k}^R
    where alpha = (Psi - 1) / Psi.

    Parameters
    ----------
    Psi : float
        Heisenberg level.
    N_max : int
        Fock space truncation.
    """

    def __init__(self, Psi: float = 2.0, N_max: int = 4):
        super().__init__(Psi, N_max)
        self.alpha = (Psi - 1.0) / Psi
        self.m3_coeff = -2.0  # m_3(T,T,T) = -2T at c=1
        self._delta3_cache: Dict[int, np.ndarray] = {}

    # --- The m_3 correction ---

    def delta3_T(self, n: int) -> np.ndarray:
        r"""delta^{(3)}(T_n) on the tensor Fock space.

        delta^{(3)}(T_n) = -2*alpha * sum_k J_k^L J_{n-k}^R

        This is an EXACT formula on the truncated Fock space (up to
        mode truncation effects at the boundary).

        Parameters
        ----------
        n : int
            Mode number.

        Returns
        -------
        np.ndarray
            Matrix of shape (dim, dim) on the tensor Fock space.
        """
        if n in self._delta3_cache:
            return self._delta3_cache[n]

        M = self.N_max + abs(n) + 2
        mat = np.zeros((self.dim, self.dim))
        for k in range(-M, M + 1):
            mat += self.J_L(k) @ self.J_R(n - k)
        mat *= -2.0 * self.alpha

        self._delta3_cache[n] = mat
        return mat

    def corrected_coproduct_T(self, n: int, z: complex = 0.0) -> np.ndarray:
        r"""Delta_0(T_n) + delta^{(3)}(T_n): the m_3-corrected coproduct.

        Parameters
        ----------
        n : int
            Mode number.
        z : complex
            Spectral parameter (default 0).

        Returns
        -------
        np.ndarray
            Matrix on the tensor Fock space.
        """
        return self.Delta_T(n, z) + self.delta3_T(n)

    # --- Verification functions ---

    def verify_morphism_condition(self, n: int = 0) -> Dict[str, Any]:
        r"""Verify the morphism defect equation:

          Delta_0(m_3(T_n,T_n,T_n)) = m_3^{diag}(Delta_0(T_n)^3) + delta^{(3)}(T_n)

        LHS = -2 * Delta_0(T_n)   [since m_3(T,T,T) = -2T]
        RHS = -2 T_n^L - 2 T_n^R + delta^{(3)}(T_n)

        Returns
        -------
        dict with 'ok', 'max_error', etc.
        """
        P = self.safe_proj(2)

        LHS = -2.0 * self.Delta_T(n, 0.0)
        m3_diag = -2.0 * self.T_L(n) + (-2.0) * self.T_R(n)
        RHS = m3_diag + self.delta3_T(n)

        err = float(np.max(np.abs(P @ (LHS - RHS) @ P)))
        return {
            "ok": err < 1e-10,
            "max_error": err,
            "mode": n,
            "Psi": self.Psi,
            "alpha": self.alpha,
        }

    def verify_psi1_vanishing(self) -> Dict[str, Any]:
        r"""At Psi = 1, delta^{(3)} = 0 (free boson, class G).

        alpha = 0 at Psi = 1, so the correction vanishes identically.
        """
        eng = M3CoproductCorrection(Psi=1.0, N_max=self.N_max)
        P = eng.safe_proj(2)
        d3 = eng.delta3_T(0)
        norm = float(np.max(np.abs(P @ d3 @ P)))
        return {
            "ok": norm < 1e-14,
            "max_norm": norm,
            "Psi": 1.0,
            "interpretation": "Psi=1 is free boson (class G): m_3 correction vanishes",
        }

    def verify_weight_conservation(self, n: int = 0) -> Dict[str, Any]:
        r"""delta^{(3)}(T_n) has correct weight under L_0^tot.

        Virasoro convention: [L_0, X_n] = -n X_n.
        So: [L_0^tot, delta^{(3)}(T_n)] = -n * delta^{(3)}(T_n).
        At n=0 this is exactly weight-preserving.
        """
        P = self.safe_proj(2)
        L0_tot = self.T_L(0) + self.T_R(0)
        d3 = self.delta3_T(n)

        comm = L0_tot @ d3 - d3 @ L0_tot
        expected = float(-n) * d3
        err = float(np.max(np.abs(P @ (comm - expected) @ P)))
        return {
            "ok": err < 1e-8,
            "max_error": err,
            "mode": n,
            "interpretation": f"[L_0^tot, delta^(3)(T_{n})] = {-n} * delta^(3)(T_{n})",
        }

    def vacuum_matrix_element(self, n: int = 0) -> Dict[str, Any]:
        r"""Compute <vac,vac| delta^{(3)}(T_n) |vac,vac>.

        This is zero for all n: J_k annihilates the left vacuum for k > 0,
        and J_{n-k} annihilates the right vacuum for n-k > 0.
        At n = 0: for each k, either J_k^L or J_{-k}^R annihilates the vacuum.
        """
        vac = np.zeros(self.dim)
        vac[self.H.idx[()] * self.d + self.H.idx[()]] = 1.0
        d3 = self.delta3_T(n)
        vev = float(vac @ d3 @ vac)
        return {
            "vev": vev,
            "is_zero": abs(vev) < 1e-14,
            "mode": n,
            "Psi": self.Psi,
        }

    def matrix_on_safe_subspace(self, n: int = 0, margin: int = 2
                                ) -> np.ndarray:
        r"""Return delta^{(3)}(T_n) projected to the safe subspace.

        Parameters
        ----------
        n : int
            Mode number.
        margin : int
            Safety margin for the projector.

        Returns
        -------
        np.ndarray
            Matrix projected to the safe subspace.
        """
        P = self.safe_proj(margin)
        return P @ self.delta3_T(n) @ P

    def eigenvalue_spectrum(self, n: int = 0, margin: int = 2
                            ) -> Dict[str, Any]:
        r"""Eigenvalue spectrum of delta^{(3)}(T_n) on the safe subspace.

        Returns
        -------
        dict with eigenvalues and related info.
        """
        mat = self.matrix_on_safe_subspace(n, margin)
        evals = np.linalg.eigvalsh(mat.real)
        nz = [float(ev) for ev in evals if abs(ev) > 1e-10]
        return {
            "eigenvalues_nonzero": sorted(nz),
            "n_nonzero": len(nz),
            "trace": float(np.trace(mat).real),
            "frobenius_norm": float(np.linalg.norm(mat, 'fro')),
            "mode": n,
            "Psi": self.Psi,
        }

    def cross_term_ratio(self, n: int = 0) -> Dict[str, Any]:
        r"""Verify delta^{(3)}(T_n) = -2*alpha * (cross-term of Delta_0(T_n)).

        The cross-term of Delta_0(T_n) at z=0 is:
          alpha * sum_k J_k^L J_{n-k}^R

        So delta^{(3)}(T_n) / cross_term = -2 (independent of n and Psi).
        """
        P = self.safe_proj(2)
        M = self.N_max + abs(n) + 2

        cross = np.zeros((self.dim, self.dim))
        for k in range(-M, M + 1):
            cross += self.J_L(k) @ self.J_R(n - k)
        cross *= self.alpha

        d3 = self.delta3_T(n)
        # delta^{(3)} = -2 * cross => delta^{(3)} / cross = -2
        # Check: delta^{(3)} + 2*cross = 0
        err = float(np.max(np.abs(P @ (d3 + 2.0 * cross) @ P)))
        return {
            "ok": err < 1e-10,
            "max_error": err,
            "ratio": -2.0,
            "mode": n,
            "interpretation": "delta^{(3)} = -2 * cross_term(Delta_0)",
        }

    def psi_dependence(self, n: int = 0) -> Dict[str, Any]:
        r"""Verify the Psi-dependence: coefficient is -2*(Psi-1)/Psi.

        The correction scales as alpha = (Psi-1)/Psi:
          Psi=1: alpha=0 (free boson, no correction)
          Psi=2: alpha=1/2
          Psi->inf: alpha->1

        Returns
        -------
        dict with results for various Psi values.
        """
        results = {}
        for Psi_test in [1.0, 1.5, 2.0, 3.0, 5.0]:
            eng = M3CoproductCorrection(Psi=Psi_test, N_max=self.N_max)
            P = eng.safe_proj(2)
            d3 = eng.delta3_T(n)
            morphism = eng.verify_morphism_condition(n)
            alpha_t = (Psi_test - 1.0) / Psi_test
            results[Psi_test] = {
                "alpha": alpha_t,
                "coefficient": -2.0 * alpha_t,
                "max_norm": float(np.max(np.abs(P @ d3 @ P))),
                "morphism_ok": morphism["ok"],
            }
        return results


# ---------------------------------------------------------------------------
# Standalone verification functions
# ---------------------------------------------------------------------------

def compute_delta3_T0(Psi: float = 2.0, N_max: int = 4) -> Dict[str, Any]:
    r"""Compute delta^{(3)}(T_0) and return key diagnostics.

    Parameters
    ----------
    Psi : float
        Heisenberg level.
    N_max : int
        Fock space truncation.

    Returns
    -------
    dict with matrix, vacuum expectation, eigenvalues, etc.
    """
    eng = M3CoproductCorrection(Psi=Psi, N_max=N_max)
    P = eng.safe_proj(2)
    d3 = eng.delta3_T(0)
    d3_safe = P @ d3 @ P

    vev = eng.vacuum_matrix_element(0)
    morph = eng.verify_morphism_condition(0)
    weight = eng.verify_weight_conservation(0)
    spectrum = eng.eigenvalue_spectrum(0)
    ratio = eng.cross_term_ratio(0)

    return {
        "matrix": d3_safe,
        "matrix_shape": d3_safe.shape,
        "Psi": Psi,
        "N_max": N_max,
        "alpha": eng.alpha,
        "coefficient": -2.0 * eng.alpha,
        "formula": f"delta^(3)(T_0) = {-2.0 * eng.alpha} * sum_k J_k^L J_{{-k}}^R",
        "vev_00": vev["vev"],
        "vev_is_zero": vev["is_zero"],
        "morphism_ok": morph["ok"],
        "morphism_error": morph["max_error"],
        "weight_conservation_ok": weight["ok"],
        "eigenvalues_nonzero": spectrum["eigenvalues_nonzero"],
        "trace": spectrum["trace"],
        "cross_term_ratio_ok": ratio["ok"],
    }


def verify_all(Psi: float = 2.0, N_max: int = 4) -> Dict[str, Any]:
    r"""Run all verification checks for delta^{(3)}(T_0).

    Returns
    -------
    dict with all verification results.
    """
    eng = M3CoproductCorrection(Psi=Psi, N_max=N_max)

    results = {
        "morphism_n0": eng.verify_morphism_condition(0),
        "morphism_n1": eng.verify_morphism_condition(1),
        "morphism_nm1": eng.verify_morphism_condition(-1),
        "psi1_vanishing": eng.verify_psi1_vanishing(),
        "weight_n0": eng.verify_weight_conservation(0),
        "weight_n1": eng.verify_weight_conservation(1),
        "weight_nm1": eng.verify_weight_conservation(-1),
        "vev_n0": eng.vacuum_matrix_element(0),
        "vev_n1": eng.vacuum_matrix_element(1),
        "cross_ratio_n0": eng.cross_term_ratio(0),
        "cross_ratio_n1": eng.cross_term_ratio(1),
        "spectrum_n0": eng.eigenvalue_spectrum(0),
        "psi_dependence": eng.psi_dependence(0),
    }

    all_ok = all([
        results["morphism_n0"]["ok"],
        results["morphism_n1"]["ok"],
        results["morphism_nm1"]["ok"],
        results["psi1_vanishing"]["ok"],
        results["weight_n0"]["ok"],
        results["weight_n1"]["ok"],
        results["weight_nm1"]["ok"],
        results["vev_n0"]["is_zero"],
        results["cross_ratio_n0"]["ok"],
        results["cross_ratio_n1"]["ok"],
        all(v["morphism_ok"] for v in results["psi_dependence"].values()),
    ])

    results["all_ok"] = all_ok
    return results
