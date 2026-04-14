r"""Quantum groups from factorization homology: 3d CS vs 6d hCS comparison.

Traces the quantum group construction at BOTH levels:
  (A) CFG25: U_q(g) from 3d Chern-Simons on R^3  [PROVED]
  (B) 6d hCS: U_{q,t}(gl_hat_hat_1) from 6d holomorphic theory on C^3  [CONJECTURAL]

THE TWO ROUTES:
===============

Route A (3d topological CS on R^3):
  1. Start with CS on R^3 with gauge algebra g, coupling k
  2. Obs^q(R^3) is an E_3 factorization algebra (framed little 3-disks on R^3)
  3. Koszul duality: Obs^q(R^3)^! gives modules = Rep(U_q(g))
  4. R-matrix from E_3 braiding on Conf_2(R^3) ~ S^2
     pi_1(Conf_2(R^3)) = pi_1(S^2) = 0, but the FRAMED E_3 braiding
     is nontrivial: pi_1(SO(3)) = Z/2, giving the sign twist q^{<lambda,mu>}
  5. Parameter: q = exp(2*pi*i / (k + h^vee))  [single parameter]

Route B (6d holomorphic theory on C^3):
  1. Start with 6d hol theory on C^3 with gl_1, Omega-background (h1,h2,h3)
  2. Obs^q(C^3) is E_3-chiral (holomorphic, NOT topological E_6)
  3. Koszul duality: Obs^q(C^3)^! should give modules = Rep(U_{q,t}(gl_hat_hat_1))
  4. R-matrix from E_3-chiral braiding on holomorphic Conf_2(C^3)
     Topologically: Conf_2(C^3) ~ S^5, pi_1(S^5) = 0 (trivial braiding)
     The nontrivial braiding is from the OMEGA-BACKGROUND, not from topology
  5. Parameters: (q,t) = (exp(h1), exp(-h2)), with h1+h2+h3=0  [two parameters]

KEY QUESTION: does Route A DIRECTLY generalize to Route B?

ANSWER: NO, with three obstructions:
  (O1) HOLOMORPHIC vs TOPOLOGICAL: R^3 supports a topological E_3 with
       nontrivial braiding from pi_1(SO(3)) = Z/2. C^3 supports a holomorphic
       E_3 with TRIVIAL topological braiding (pi_1(S^5) = 0). The 6d braiding
       is entirely from the Omega-background deformation, which has no analogue
       in the purely topological 3d theory.
  (O2) TWO-PARAMETER vs ONE-PARAMETER: R^3 has ONE coupling constant k giving
       q = exp(2*pi*i/(k+h^vee)). C^3 has the Omega-background (h1,h2,h3) with
       CY constraint h1+h2+h3=0, giving TWO independent parameters. The second
       parameter (sigma_3 vs sigma_2) has no 3d analogue.
  (O3) THE MIKI AUTOMORPHISM: C^3 has an S_3 = Weyl(CY torus) symmetry permuting
       the three complex directions (and hence (q1,q2,q3)). R^3 has SO(3) symmetry,
       which is continuous and does not produce a discrete S_3 action on parameters.
       The Miki is ALGEBRA-SPECIFIC (AP-CY22), not operadic.

WHAT DOES GENERALIZE:
  (G1) E_3 -> Koszul duality -> quantum group: the LOGICAL PATTERN is identical.
       Both construct quantum groups as Koszul duals of E_3 factorization algebras.
  (G2) The R-matrix from E_3 braiding: both get R-matrices, but from different
       sources (topological framing vs Omega-background).
  (G3) Dimensional projection E_3 -> E_2 -> E_1: both support the cascade,
       losing R-matrix data at each projection.
  (G4) kappa_ch preservation under projection: structural invariant independent
       of the ambient dimension.

INTERMEDIATE LEVEL: 5d hol CS on C^2 x R
  This interpolates between the two routes:
    - R direction: topological, like Route A
    - C^2 directions: holomorphic, like Route B
    - Boundary algebra: Y(gl_hat_1) = affine Yangian [PROVED, Costello 2013]
    - Parameters: (h1,h2,h3) with h3 = -(h1+h2), ONE effective parameter sigma_3
    - Miki: no (only S_2 from C^2, not S_3) -- partially present as q<->t duality

AP COMPLIANCE:
  - AP-CY22: Miki is algebra-specific, not operadic. Stated throughout.
  - AP-CY31: z is spectral (Yangian), NOT worldsheet. Distinguished in coproducts.
  - AP-CY14: 6d results are CONJECTURAL. Route A is PROVED, Route B is PROGRAMME.
  - AP113: All kappa subscripted (kappa_ch, kappa_cat, kappa_BKM, kappa_fiber).
  - AP150: The composite arrow at 6d is conjectural; each ingredient is verified.
  - AP154: Algebraic E_3 (Deligne) vs topological E_3 (config space) distinguished.
  - AP-CY3: E_2 != commutative. E_3 braiding is NOT symmetric (at generic h_i).

MANUSCRIPT REFERENCES:
  chapters/theory/quantum_chiral_algebras.tex: Conj conj:6d-defect-c3
  chapters/theory/en_factorization.tex: Sec sec:e3-from-hcs
  chapters/theory/e1_chiral_algebras.tex: E_1 primacy
  chapters/theory/e2_chiral_algebras.tex: E_2 bar complex

MATHEMATICAL SOURCES:
  Costello-Francis-Gwilliam, "CS theory and factorisation homology" (2024)
  Costello, "Supersymmetric gauge theory and the Yangian" (2013)
  Costello-Gwilliam, "Factorization algebras in QFT" (2021)
  Miki, "A (q,gamma) analog of W_{1+infty}" (2007)
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

import numpy as np
from sympy import (
    Matrix,
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    oo,
    pi,
    simplify,
    sqrt,
    symbols,
)

from compute.lib.holomorphic_cs_chiral_engine import (
    BoundaryAlgebra,
    ChiralCEComplex,
    DimensionalProjection,
    EnStructureVerifier,
    KoszulDual,
    OmegaBackground,
)


# =========================================================================
# 1. Configuration space topology: the fundamental obstruction
# =========================================================================

class ConfigurationSpaceBraiding:
    """Braiding data from configuration spaces at each dimension.

    For n particles on a manifold M:
      Conf_n(M) = M^n - {diagonals}

    The braiding is pi_1(Conf_2(M)):
      R^3: Conf_2(R^3) ~ S^2,  pi_1 = 0  (but framed: pi_1(SO(3)) = Z/2)
      C^2: Conf_2(C^2) ~ S^3,  pi_1 = 0
      C^3: Conf_2(C^3) ~ S^5,  pi_1 = 0
      R^2: Conf_2(R^2) ~ S^1,  pi_1 = Z   (braid group!)

    The key point: for dim >= 3 (real), the configuration space is
    simply connected, so the topological braiding is TRIVIAL.
    The nontrivial braiding in the quantum group comes from
    DEFORMATIONS (framings or Omega-backgrounds), not topology.
    """

    # Topology of Conf_2(M) for various M
    TOPOLOGY = {
        "R^2": {"link": "S^1", "pi_1": "Z", "braiding": "nontrivial",
                "source": "topology"},
        "R^3": {"link": "S^2", "pi_1": "0", "braiding": "trivial_bare",
                "source": "framing (SO(3), pi_1=Z/2)"},
        "C^2": {"link": "S^3", "pi_1": "0", "braiding": "trivial_bare",
                "source": "Omega-background (h1,h2)"},
        "C^3": {"link": "S^5", "pi_1": "0", "braiding": "trivial_bare",
                "source": "Omega-background (h1,h2,h3)"},
    }

    @staticmethod
    def conf2_link_sphere_dim(real_dim: int) -> int:
        """The link of the diagonal in Conf_2(R^d) is S^{d-1}.

        Conf_2(R^d) ~ R^d x (R^d - {0}) ~ R^d x S^{d-1} x R_{>0}

        For R^d: link sphere dimension = d-1
        For C^n (= R^{2n}): link sphere dimension = 2n-1
        """
        return real_dim - 1

    @staticmethod
    def fundamental_group_link(link_dim: int) -> str:
        """pi_1(S^n) for the configuration space link.

        pi_1(S^0) = Z (two points)
        pi_1(S^1) = Z (braid group source)
        pi_1(S^n) = 0 for n >= 2 (simply connected)
        """
        if link_dim == 0:
            return "Z"
        if link_dim == 1:
            return "Z"
        return "0"

    @classmethod
    def braiding_analysis(cls, manifold: str) -> Dict[str, Any]:
        """Complete braiding analysis for a given ambient manifold."""
        if manifold not in cls.TOPOLOGY:
            raise ValueError(f"Unknown manifold: {manifold}")

        data = cls.TOPOLOGY[manifold]
        return {
            "manifold": manifold,
            "conf2_link": data["link"],
            "pi_1_conf2": data["pi_1"],
            "topological_braiding": data["braiding"],
            "braiding_source": data["source"],
            "nontrivial_braiding_from_topology": data["pi_1"] != "0",
            "requires_deformation": data["pi_1"] == "0",
        }

    @classmethod
    def compare_3d_vs_6d(cls) -> Dict[str, Any]:
        """Compare the braiding sources for R^3 (3d CS) vs C^3 (6d hCS).

        This is obstruction O1: the braiding mechanisms are fundamentally
        different despite the same E_3 structure level.
        """
        r3 = cls.braiding_analysis("R^3")
        c3 = cls.braiding_analysis("C^3")

        return {
            "R^3_analysis": r3,
            "C^3_analysis": c3,
            "same_en_level": True,  # Both E_3
            "same_braiding_source": False,  # Different!
            "obstruction_O1": True,
            "R^3_braiding_from": "SO(3) framing, pi_1(SO(3)) = Z/2",
            "C^3_braiding_from": "Omega-background (h1,h2,h3)",
            "explanation": (
                "R^3 gets braiding from the framed little 3-disks operad: "
                "framings of R^3 form SO(3) with pi_1 = Z/2, giving a Z/2 "
                "twist (the sign q^{<lambda,mu>} in U_q(g)). "
                "C^3 has trivial topological braiding (pi_1(S^5)=0) but "
                "nontrivial holomorphic braiding from the equivariant "
                "Omega-background parameters (h1,h2,h3)."
            ),
        }


# =========================================================================
# 2. Route A: U_q(g) from 3d CS on R^3 (CFG25)
# =========================================================================

class RouteA_3dCS:
    """U_q(g) from 3d Chern-Simons on R^3.

    STATUS: PROVED (Costello-Francis-Gwilliam 2024/2025).

    The construction:
      1. CS action: S = (k/4pi) int_{R^3} tr(A dA + 2/3 A^3)
      2. Observables: Obs^q(R^3) is an E_3 factorization algebra
      3. Koszul duality: Obs^q(R^3)^! ~ Rep(U_q(g))
      4. R-matrix: from framed E_3 braiding, R in End(V tensor V)
      5. q = exp(2*pi*i / (k + h^vee))

    The E_3 is TOPOLOGICAL: from the framed little 3-disks operad on R^3.
    The braiding is from pi_1(SO(3)) = Z/2 (the framing group).
    """

    def __init__(self, gauge_algebra: str, k: Rational, rank: int = 1):
        """Initialize the 3d CS theory.

        Args:
            gauge_algebra: Name of the gauge algebra (e.g., "sl_2", "gl_1")
            k: Chern-Simons level
            rank: Rank of the gauge algebra
        """
        self.gauge_algebra = gauge_algebra
        self.k = Rational(k)
        self.rank = rank
        self._h_vee = self._compute_dual_coxeter()

    def _compute_dual_coxeter(self) -> Rational:
        """Dual Coxeter number h^vee of the gauge algebra."""
        table = {
            "gl_1": Rational(0),
            "sl_2": Rational(2),
            "sl_3": Rational(3),
            "sl_n": Rational(self.rank),  # h^vee(sl_n) = n
            "so_3": Rational(2),  # = sl_2
            "sp_4": Rational(3),
            "g_2": Rational(4),
        }
        return table.get(self.gauge_algebra, Rational(self.rank))

    @property
    def dual_coxeter(self) -> Rational:
        return self._h_vee

    @property
    def q_parameter(self) -> Dict[str, Any]:
        """The single deformation parameter q = exp(2*pi*i / (k + h^vee)).

        For generic k (not a root of unity): Rep_q(g) is semisimple.
        At root of unity (k + h^vee integer): non-semisimple, KL theory.
        """
        if self.k + self._h_vee == 0:
            return {"q": "undefined (critical level)", "regime": "critical"}

        return {
            "q_formula": f"exp(2*pi*i / ({self.k} + {self._h_vee}))",
            "effective_level": self.k + self._h_vee,
            "is_root_of_unity": isinstance(self.k, Rational) and self.k.denominator == 1,
            "regime": "root_of_unity" if (isinstance(self.k, Rational) and
                                          self.k.denominator == 1 and
                                          self.k + self._h_vee > 0)
                      else "generic",
            "num_parameters": 1,
        }

    @property
    def en_level(self) -> int:
        """The E_n level of the factorization algebra: E_3 from R^3."""
        return 3

    @property
    def en_type(self) -> str:
        """Type of E_3: topological (from framed little 3-disks on R^3)."""
        return "topological_framed"

    def configuration_space_braiding(self) -> Dict[str, Any]:
        """Braiding from framed Conf_2(R^3).

        Conf_2(R^3) ~ S^2, pi_1 = 0 (bare).
        But the FRAMED configuration space has pi_1(Conf^{fr}_2(R^3))
        containing pi_1(SO(3)) = Z/2, which provides the nontrivial
        braiding twist responsible for the q-deformation.
        """
        return {
            "conf2_link": "S^2",
            "pi_1_bare": "0",
            "pi_1_framed": "Z/2 (from pi_1(SO(3)))",
            "braiding_type": "framed_topological",
            "braiding_parameter": "q = exp(2*pi*i/(k+h^vee))",
            "explanation": (
                "The bare configuration space S^2 is simply connected, "
                "but the framed E_3 operad on R^3 includes SO(3) framings "
                "with pi_1(SO(3)) = Z/2, giving a nontrivial braiding. "
                "This Z/2 twist, combined with the representation theory "
                "weight lattice, produces the full q^{<lambda,mu>} factor."
            ),
        }

    def koszul_duality(self) -> Dict[str, Any]:
        """Koszul duality: Obs^q(R^3)^! ~ Rep(U_q(g)).

        The Koszul dual of the E_3 factorization algebra of observables
        is the category of representations of the quantum group U_q(g).
        """
        return {
            "input": f"Obs^q(R^3) [E_3 factorization algebra, gauge {self.gauge_algebra}]",
            "output": f"Rep(U_q({self.gauge_algebra}))",
            "mechanism": "E_3-Koszul duality = Verdier dual of E_3 bar complex",
            "parameter_inversion": f"q -> q^{{-1}} (level k -> -k - 2*{self._h_vee})",
            "status": "PROVED (CFG25)",
        }

    def r_matrix(self) -> Dict[str, Any]:
        """R-matrix from the E_3 braiding on Conf_2(R^3).

        The universal R-matrix R in U_q(g) tensor U_q(g) comes from
        the braiding of the framed E_3 factorization algebra.
        """
        return {
            "source": "framed E_3 braiding on Conf_2(R^3)",
            "lives_in": f"U_q({self.gauge_algebra}) tensor U_q({self.gauge_algebra})",
            "satisfies_YBE": True,
            "satisfies_ZTE": "not applicable (3d, no tetrahedron structure)",
            "type": "single-parameter (q)",
            "formula_sl2": "R = q^{H tensor H / 2} * sum_n q^{n(n-1)/2} * "
                           "(q-q^{-1})^n / [n]_q! * E^n tensor F^n",
        }

    def miki_automorphism(self) -> Dict[str, Any]:
        """Miki automorphism: ABSENT for 3d CS."""
        return {
            "exists": False,
            "reason": (
                "R^3 has SO(3) continuous rotation symmetry, not a discrete "
                "S_3 permutation of coordinates. The Miki automorphism "
                "requires three distinguished complex directions (z_1,z_2,z_3) "
                "in C^3, permutable by S_3 = Weyl(CY torus). R^3 has no "
                "complex structure and no distinguished coordinate triple."
            ),
            "AP_ref": "AP-CY22",
        }

    def summary(self) -> Dict[str, Any]:
        """Complete summary of Route A."""
        return {
            "route": "A (3d CS on R^3)",
            "status": "PROVED (CFG25)",
            "gauge_algebra": self.gauge_algebra,
            "level": self.k,
            "quantum_group": f"U_q({self.gauge_algebra})",
            "en_level": 3,
            "en_type": "topological_framed",
            "num_parameters": 1,
            "braiding_source": "framed E_3 (pi_1(SO(3)) = Z/2)",
            "miki": False,
            "omega_background": False,
            "config_space_link": "S^2 (Conf_2(R^3))",
            "koszul_dual_parameter": f"q -> q^{{-1}}",
        }


# =========================================================================
# 3. Route B: U_{q,t}(gl_hat_hat_1) from 6d hCS on C^3 (CONJECTURAL)
# =========================================================================

class RouteB_6dHCS:
    """U_{q,t}(gl_hat_hat_1) from 6d holomorphic theory on C^3.

    STATUS: CONJECTURAL (AP-CY14).

    The construction:
      1. 6d holomorphic theory on C^3 with gl_1 and Omega-background (h1,h2,h3)
      2. Obs^q(C^3) is an E_3-chiral factorization algebra (holomorphic E_3)
      3. Koszul duality: Obs^q(C^3)^! should give modules = Rep(U_{q,t}(gl_hat_hat_1))
      4. R-matrix from E_3-chiral braiding (Omega-background, not topology)
      5. Parameters: (q,t) = (exp(h1), exp(-h2)), with h1+h2+h3=0

    The E_3 is HOLOMORPHIC: from the holomorphic constraint on C^3.
    The topological shadow is E_6 (real dim 6), reduced to E_3 by holomorphy.
    The braiding is from the Omega-background, NOT from topology.
    """

    def __init__(self, h1: Rational, h2: Rational):
        """Initialize the 6d theory with Omega-background parameters.

        The CY condition h1+h2+h3=0 is enforced.
        """
        self.omega = OmegaBackground(h1, h2)
        self.h1 = self.omega.h1
        self.h2 = self.omega.h2
        self.h3 = self.omega.h3
        self.boundary = BoundaryAlgebra(3, self.omega)

    @property
    def q_parameter(self) -> Dict[str, Any]:
        """The TWO deformation parameters (q, t).

        q = exp(h1), t = exp(-h2), with constraint q*t*s = 1
        where s = exp(h3) = exp(-h1-h2).

        The effective deformation is sigma_3 = h1*h2*h3.
        sigma_2 generates a rescaling (not a true deformation).
        """
        return {
            "q_formula": f"exp({self.h1})",
            "t_formula": f"exp(-({self.h2}))",
            "constraint": "q * t * s = 1 (CY: h1+h2+h3=0)",
            "sigma_2": self.omega.sigma2,
            "sigma_3": self.omega.sigma3,
            "num_parameters": 2,
            "effective_parameter": "sigma_3 (single essential deformation)",
            "regime": "self_dual" if self.omega.is_self_dual else "generic",
        }

    @property
    def en_level(self) -> int:
        """The E_n level: E_3 from C^3 (3 complex dimensions)."""
        return 3

    @property
    def en_type(self) -> str:
        """Type of E_3: holomorphic (from holomorphic constraint on C^3)."""
        return "holomorphic_chiral"

    @property
    def topological_shadow_en(self) -> int:
        """The topological E_n level (ignoring holomorphy): E_6 from R^6."""
        return 6

    def configuration_space_braiding(self) -> Dict[str, Any]:
        """Braiding from Conf_2(C^3).

        Conf_2(C^3) ~ S^5, pi_1(S^5) = 0.
        The topological braiding is TRIVIAL.
        The nontrivial braiding comes entirely from the Omega-background.
        """
        return {
            "conf2_link": "S^5",
            "pi_1_bare": "0",
            "pi_1_framed": "0 (pi_1(SO(6)) = Z/2, but holomorphic constraint "
                           "reduces to pi_1(U(3)) = Z; the Omega-background "
                           "breaks U(3) to T^3, replacing topological braiding "
                           "with equivariant parameters)",
            "braiding_type": "holomorphic_equivariant",
            "braiding_parameters": f"(q,t) from Omega ({self.h1},{self.h2},{self.h3})",
            "explanation": (
                "S^5 is simply connected (pi_1 = 0), so the bare topological "
                "braiding on Conf_2(C^3) is trivial. The Omega-background "
                "(h1,h2,h3) with CY constraint h1+h2+h3=0 deforms the "
                "holomorphic factorization structure, producing a nontrivial "
                "E_3-chiral braiding. At (h1,h2,h3) = (0,0,0), the braiding "
                "becomes symmetric (E_3 -> E_inf). The nontriviality of the "
                "braiding at generic (h1,h2,h3) is the content of Costello 2017, "
                "Section 5 (equivariant refinement)."
            ),
        }

    def structure_function(self, u: Rational) -> Rational:
        """The rational structure function g(u) = prod(u-h_i)/prod(u+h_i).

        This is the key invariant of the affine Yangian (5d projection).
        The 6d theory has the TRIGONOMETRIC lift:
          G(x) = prod(x - q_i) / prod(x - q_i^{-1})
        with x = exp(u), q_i = exp(h_i).
        """
        return self.omega.structure_function_at(u)

    def koszul_duality(self) -> Dict[str, Any]:
        """Koszul duality: Obs^q(C^3)^! ~ Rep(U_{q,t}(gl_hat_hat_1)).

        STATUS: CONJECTURAL (AP-CY14).
        """
        return {
            "input": "Obs^q(C^3) [E_3-chiral factorization algebra, gl_1]",
            "output": "Rep(U_{q,t}(gl_hat_hat_1))",
            "mechanism": "E_3-chiral Koszul duality = Verdier dual of E_3 bar",
            "parameter_inversion": "(h1,h2,h3) -> (-h1,-h2,-h3), "
                                   "equivalently (q,t) -> (q^{-1},t^{-1})",
            "status": "CONJECTURAL (AP-CY14)",
            "depends_on": [
                "6d holomorphic factorization algebra existence",
                "E_3-chiral Koszul duality (conj:e3-koszul-duality)",
                "Identification of Koszul dual with quantum toroidal",
            ],
        }

    def r_matrix(self) -> Dict[str, Any]:
        """R-matrix from the E_3-chiral braiding on C^3.

        The two-parameter R-matrix R(u,v) factorizes as:
          R_ch(u,v) = R_1(u) * R_2(v) * R_12(u-v)
        (Zamolodchikov factorization from the two independent spectral parameters).
        """
        return {
            "source": "E_3-chiral braiding via Omega-background on C^3",
            "lives_in": "U_{q,t}(gl_hat_hat_1) tensor U_{q,t}(gl_hat_hat_1)",
            "satisfies_YBE": True,
            "satisfies_ZTE": "FAILS at O(kappa^2) (thm:zte-failure)",
            "type": "two-parameter (q,t)",
            "factorization": "R_ch(u,v) = R_1(u) R_2(v) R_12(u-v)",
        }

    def miki_automorphism(self) -> Dict[str, Any]:
        """Miki automorphism: PRESENT for 6d on C^3 with gl_1.

        The S_3 permutation of (q_1, q_2, q_3) comes from the Weyl group
        of the CY torus T^3 acting on C^3. This is ALGEBRA-SPECIFIC
        (AP-CY22): it requires the specific algebra U_{q,t}(gl_hat_hat_1),
        not just any E_3 algebra.
        """
        return {
            "exists": True,
            "type": "S_3 Weyl group of CY torus",
            "action_on_params": "(q_1, q_2, q_3) -> cyclic permutation",
            "action_on_generators": "E(z) <-> K^+(z), F(z) <-> K^-(z)",
            "is_operadic": False,  # AP-CY22
            "requires_specific_algebra": True,
            "counterexample": "k[x]/(x^2) is E_3 but has no Miki",
            "AP_ref": "AP-CY22",
        }

    def omega_background_role(self) -> Dict[str, Any]:
        """The Omega-background: unique to 6d, no 3d analogue.

        The Omega-background (h1, h2, h3) on C^3 is the equivariant
        deformation by the T^3 action (z_1, z_2, z_3) -> (e^{ih_1 t} z_1, ...).
        R^3 has no complex structure and hence no holomorphic T^3 action.
        """
        return {
            "role": "Source of ALL nontrivial braiding in C^3",
            "parameters": f"(h1, h2, h3) = ({self.h1}, {self.h2}, {self.h3})",
            "constraint": "h1 + h2 + h3 = 0 (CY condition)",
            "at_zero": "E_3-chiral -> E_inf (symmetric, no quantum group)",
            "3d_analogue": "NONE (R^3 has no Omega-background)",
            "produces": {
                "braiding": "nontrivial E_3-chiral braiding",
                "two_parameters": "(q,t) from (h1,h2)",
                "miki": "S_3 from permuting (h1,h2,h3)",
                "CY_condition": "one-loop anomaly cancellation",
            },
        }

    def summary(self) -> Dict[str, Any]:
        """Complete summary of Route B."""
        return {
            "route": "B (6d hCS on C^3)",
            "status": "CONJECTURAL (AP-CY14)",
            "gauge_algebra": "gl_1",
            "omega": f"({self.h1}, {self.h2}, {self.h3})",
            "quantum_group": "U_{q,t}(gl_hat_hat_1)",
            "en_level": 3,
            "en_type": "holomorphic_chiral",
            "topological_shadow": "E_6 (from R^6)",
            "num_parameters": 2,
            "braiding_source": "Omega-background (h1,h2,h3)",
            "miki": True,
            "omega_background": True,
            "config_space_link": "S^5 (Conf_2(C^3))",
            "koszul_dual_parameter": "(q,t) -> (q^{-1}, t^{-1})",
        }


# =========================================================================
# 4. The 5d interpolation: affine Yangian from C^2 x R
# =========================================================================

class Route5d_Interpolation:
    """Y(gl_hat_1) from 5d holomorphic CS on C^2 x R.

    STATUS: PROVED (Costello 2013).

    This interpolates between Route A (3d, topological) and Route B (6d, holomorphic):
      - R direction: topological (like Route A)
      - C^2 directions: holomorphic (like Route B)
      - E_2-chiral from C^2, projected to E_1 on a curve C
      - ONE effective parameter sigma_3 (like Route A, unlike Route B)
    """

    def __init__(self, h1: Rational, h2: Rational):
        self.omega = OmegaBackground(h1, h2)
        self.h1 = self.omega.h1
        self.h2 = self.omega.h2
        self.h3 = self.omega.h3
        self.boundary = BoundaryAlgebra(2, self.omega)

    @property
    def en_level(self) -> int:
        """E_2 from C^2 (holomorphic)."""
        return 2

    @property
    def en_type(self) -> str:
        return "holomorphic_chiral"

    def interpolation_analysis(self) -> Dict[str, Any]:
        """How the 5d theory interpolates between 3d and 6d."""
        return {
            "topological_direction": "R (contributes E_1, like 3d CS)",
            "holomorphic_directions": "C^2 (contributes E_2, like 6d hCS)",
            "total_en": "E_2 (= E_1 from R x E_1 from holomorphic on C^2, by Dunn)",
            "parameters": {
                "num_free": 2,
                "effective": 1,
                "explanation": "sigma_2 is a rescaling; sigma_3 is the single "
                               "effective deformation, like Route A's k",
            },
            "miki": {
                "exists": False,
                "partial": "SL_2(Z) duality (swap two C-directions), not S_3",
            },
            "comparison_to_3d": {
                "shared": ["E_n Koszul duality pattern", "single effective parameter",
                           "no Miki"],
                "different": ["holomorphic (not topological)", "R-matrix from "
                              "Omega-background (not framing)"],
            },
            "comparison_to_6d": {
                "shared": ["Omega-background", "holomorphic E_n structure",
                           "structure function g(u)"],
                "different": ["E_2 not E_3", "one parameter not two",
                              "no Miki", "no third direction"],
            },
        }

    def dimensional_reduction_to_3d(self) -> Dict[str, Any]:
        """6d -> 5d -> 3d: shrink directions to recover lower-dimensional theories.

        5d -> 3d: take h_i -> 0 (all Omega-background parameters vanish).
        The Yangian degenerates to the current algebra (Kac-Moody).
        g(u) -> 1 (structure function becomes trivial).
        R-matrix -> trivial (braiding becomes symmetric).
        """
        return {
            "limit": "h_i -> 0",
            "structure_function": "g(u) -> 1 (trivial)",
            "boundary_algebra": "Y(gl_hat_1) -> Heisenberg (current algebra)",
            "r_matrix": "trivial (commutative limit)",
            "kappa_ch_preserved": True,
        }

    def summary(self) -> Dict[str, Any]:
        return {
            "route": "5d interpolation (C^2 x R)",
            "status": "PROVED (Costello 2013)",
            "quantum_group": "Y(gl_hat_1) (affine Yangian)",
            "en_level": 2,
            "en_type": "holomorphic_chiral",
            "num_parameters": 1,
            "braiding_source": "Omega-background (h1,h2)",
        }


# =========================================================================
# 5. Systematic comparison: three obstructions to direct generalization
# =========================================================================

class ObstructionAnalysis:
    """The three obstructions to direct generalization from Route A to Route B.

    O1: Holomorphic vs topological (different braiding sources)
    O2: Two-parameter vs one-parameter (extra deformation from C^3)
    O3: Miki automorphism (S_3 symmetry of C^3, absent for R^3)
    """

    def __init__(self, route_a: RouteA_3dCS, route_b: RouteB_6dHCS):
        self.route_a = route_a
        self.route_b = route_b

    def obstruction_O1_braiding_source(self) -> Dict[str, Any]:
        """O1: Holomorphic vs topological E_3.

        R^3: topological E_3 from framed little 3-disks.
          Braiding from pi_1(SO(3)) = Z/2. Nontrivial even without deformation.
        C^3: holomorphic E_3 from holomorphic factorization.
          Topological braiding TRIVIAL (pi_1(S^5)=0).
          Nontrivial braiding ONLY from Omega-background.
          At h_i = 0: E_3 -> E_inf (braiding becomes symmetric).

        This means the 6d braiding is "softer": it can be continuously
        turned off by sending h_i -> 0, while the 3d braiding (from the
        discrete pi_1(SO(3)) = Z/2) persists at any coupling.
        """
        return {
            "obstruction": "O1: holomorphic vs topological E_3",
            "route_a": {
                "en_type": "topological_framed",
                "braiding_source": "pi_1(SO(3)) = Z/2",
                "deformable": False,
                "at_zero_coupling": "still E_3 (not E_inf)",
            },
            "route_b": {
                "en_type": "holomorphic_chiral",
                "braiding_source": "Omega-background",
                "deformable": True,
                "at_zero_coupling": "E_inf (symmetric, no quantum group)",
            },
            "consequence": (
                "The 3d E_3 structure is robust (topological), while the 6d "
                "E_3-chiral structure is parameter-dependent. The quantum group "
                "U_q(g) exists at any level k; the quantum toroidal algebra "
                "degenerates to U(gl_hat_hat_1) at h_i = 0."
            ),
            "severity": "structural",
        }

    def obstruction_O2_parameters(self) -> Dict[str, Any]:
        """O2: Two-parameter vs one-parameter deformation.

        R^3: ONE parameter (CS level k -> q = exp(2*pi*i/(k+h^vee))).
        C^3: TWO parameters (h1,h2) -> (q,t) = (exp(h1), exp(-h2)).

        The extra parameter arises because C^3 has THREE complex directions
        with equivariant weights (h1,h2,h3) subject to ONE constraint
        (h1+h2+h3=0), leaving TWO free parameters. R^3 has no such structure.

        However: sigma_3 = h1*h2*h3 is the SINGLE effective deformation
        (sigma_2 generates a rescaling). So the extra parameter is in some
        sense "inessential" for the algebra structure, but ESSENTIAL for
        the R-matrix (which sees both q and t independently).
        """
        q_a = self.route_a.q_parameter
        q_b = self.route_b.q_parameter
        return {
            "obstruction": "O2: two-parameter vs one-parameter",
            "route_a_params": q_a["num_parameters"],
            "route_b_params": q_b["num_parameters"],
            "extra_parameter_origin": "third complex direction in C^3",
            "essential_deformation": "sigma_3 = h1*h2*h3 (same for both, up to identification)",
            "inessential_parameter": "sigma_2 (rescaling in Route B, absent in Route A)",
            "r_matrix_sensitivity": (
                "The R-matrix R(u,v) of U_{q,t} depends on BOTH parameters; "
                "the single-parameter R-matrix R(u) of U_q is recovered by "
                "setting one spectral parameter to zero (v=0)."
            ),
            "5d_interpolation": "ONE effective parameter (sigma_3), like Route A",
            "severity": "moderate",
        }

    def obstruction_O3_miki(self) -> Dict[str, Any]:
        """O3: Miki automorphism (present in 6d, absent in 3d).

        The Miki S: (q_1,q_2,q_3) -> (q_2,q_3,q_1) is the S_3 Weyl
        group of the CY torus T^3 acting on C^3.

        R^3 has SO(3) continuous symmetry, NOT a discrete S_3 permutation.

        The Miki is ALGEBRA-SPECIFIC (AP-CY22): it requires the specific
        algebra U_{q,t}(gl_hat_hat_1), not just any E_3 factorization algebra.
        """
        return {
            "obstruction": "O3: Miki automorphism",
            "route_a_miki": False,
            "route_b_miki": True,
            "origin": "S_3 = Weyl(CY torus T^3) acting on (z_1,z_2,z_3) in C^3",
            "3d_analogue": "NONE (SO(3) is continuous, not discrete S_3)",
            "algebra_specific": True,  # AP-CY22
            "counterexample": "k[x]/(x^2) is E_3 but has no Miki",
            "physical_meaning": (
                "The Miki swaps the three 'loop directions' of the quantum "
                "toroidal algebra: it exchanges creation/annihilation operators "
                "E(z) <-> K^+(z) with Cartan currents. This is the SL_3(Z) "
                "action on the torus C^3/Z^3. No analogue in 3d topology."
            ),
            "severity": "fundamental",
        }

    def what_generalizes(self) -> Dict[str, Any]:
        """What DOES generalize from Route A to Route B."""
        return {
            "G1_logical_pattern": {
                "description": "E_3 -> Koszul duality -> quantum group",
                "route_a": "Obs^q(R^3)^! ~ Rep(U_q(g))",
                "route_b": "Obs^q(C^3)^! ~ Rep(U_{q,t}(gl_hat_hat_1))",
                "generalizes": True,
            },
            "G2_r_matrix_from_braiding": {
                "description": "R-matrix from E_3 braiding",
                "route_a": "from framed topological E_3",
                "route_b": "from Omega-background holomorphic E_3",
                "generalizes": True,
                "with_caveat": "different braiding SOURCES",
            },
            "G3_dimensional_projection": {
                "description": "E_3 -> E_2 -> E_1 cascade",
                "route_a": "E_3 -> E_2 (forget one axis) -> E_1 (forget two axes)",
                "route_b": "E_3-chiral -> E_2-chiral -> E_1-chiral",
                "generalizes": True,
            },
            "G4_kappa_preservation": {
                "description": "kappa_ch preserved under projection",
                "route_a": "kappa_ch(U_q(g)) invariant under dim projection",
                "route_b": "kappa_ch(U_{q,t}) invariant under dim projection",
                "generalizes": True,
            },
        }

    def full_comparison(self) -> Dict[str, Any]:
        """Complete comparison of Routes A and B."""
        return {
            "routes": {
                "A": self.route_a.summary(),
                "B": self.route_b.summary(),
            },
            "obstructions": {
                "O1": self.obstruction_O1_braiding_source(),
                "O2": self.obstruction_O2_parameters(),
                "O3": self.obstruction_O3_miki(),
            },
            "generalizations": self.what_generalizes(),
            "verdict": (
                "The CFG25 construction does NOT directly generalize from R^3 to C^3. "
                "The LOGICAL PATTERN (E_3 factorization -> Koszul duality -> quantum group) "
                "is identical, but the IMPLEMENTATION differs fundamentally in three ways: "
                "(O1) the braiding source (topological framing vs Omega-background), "
                "(O2) the number of parameters (1 vs 2), and "
                "(O3) the Miki automorphism (absent vs present). "
                "The 5d theory on C^2 x R interpolates: it shares the logical pattern with "
                "both, has one effective parameter like 3d, and gets its braiding from "
                "Omega-background like 6d."
            ),
        }


# =========================================================================
# 6. Numerical verification: structure functions and R-matrices
# =========================================================================

class NumericalVerification:
    """Numerical checks for the comparison.

    Uses safe test points far from poles (AP-CY28).
    """

    def __init__(self, h1: Rational = Rational(37), h2: Rational = Rational(41)):
        """Initialize with safe Omega-background parameters.

        AP-CY28: avoid h_i = 0, +/- small integers for test points.
        Use h = (37, 41, -78) for large-parameter safety.
        """
        self.omega = OmegaBackground(h1, h2)
        self.h1 = self.omega.h1
        self.h2 = self.omega.h2
        self.h3 = self.omega.h3

    def verify_cy_condition(self) -> bool:
        """h1 + h2 + h3 = 0."""
        return self.h1 + self.h2 + self.h3 == 0

    def verify_structure_function_symmetry(self) -> bool:
        """g(u) * g(-u) = 1 (unitarity of the structure function).

        This is the algebraic statement that g * g^{-} = 1,
        where g^{-}(u) = g(-u). Consequence of the CY condition.
        """
        # Use safe test point far from all poles +/- h_i
        u = Rational(1000)
        g_u = self.omega.structure_function_at(u)
        g_neg_u = self.omega.structure_function_at(-u)
        product = g_u * g_neg_u
        return product == 1

    def verify_classical_limit(self) -> Dict[str, Any]:
        """At the self-dual point (sigma_3 = 0), g(u) = 1.

        When one h_i = 0, sigma_3 = h1*h2*h3 = 0, and g(u) = 1
        identically (the Yangian degenerates to Heisenberg).
        """
        omega_sd = OmegaBackground(Rational(1), Rational(-1))
        # h3 = 0, so sigma_3 = 0
        assert omega_sd.h3 == 0
        assert omega_sd.is_self_dual

        u_test = Rational(1000)
        g_val = omega_sd.structure_function_at(u_test)
        return {
            "self_dual_g_trivial": g_val == 1,
            "sigma_3_at_self_dual": omega_sd.sigma3,
        }

    def verify_koszul_parameter_inversion(self) -> bool:
        """The Koszul dual has inverted parameters: g^!(u) = g(-u) = 1/g(u).

        This is the manifestation of (h1,h2,h3) -> (-h1,-h2,-h3) on the
        structure function. Equivalently, (q,t) -> (q^{-1}, t^{-1}).
        """
        u = Rational(1000)
        g_u = self.omega.structure_function_at(u)
        # Koszul dual: inverted Omega
        omega_dual = OmegaBackground(-self.h1, -self.h2)
        g_dual_u = omega_dual.structure_function_at(u)
        # g^!(u) should equal 1/g(u)
        return g_u * g_dual_u == 1

    def verify_5d_to_6d_lift(self) -> Dict[str, Any]:
        """The trigonometric lift of the rational structure function.

        Rational (5d): g(u) = prod(u - h_i) / prod(u + h_i)
        Trigonometric (6d): G(x) = prod(x - q_i) / prod(x - q_i^{-1})
        with x = exp(u), q_i = exp(h_i).

        In the limit u -> 0 (small spectral parameter), the trig G(x)
        reduces to the rational g(u) via x = 1 + u + O(u^2).

        We verify this numerically at a safe test point.
        """
        u_test = Rational(1, 10)  # Small u for the expansion
        g_rational = self.omega.structure_function_at(u_test)

        # Trigonometric structure function (exact, using floats)
        h1_f = float(self.h1)
        h2_f = float(self.h2)
        h3_f = float(self.h3)
        x = np.exp(float(u_test))
        q1 = np.exp(h1_f)
        q2 = np.exp(h2_f)
        q3 = np.exp(h3_f)
        G_trig = ((x - q1) * (x - q2) * (x - q3) /
                  ((x - 1/q1) * (x - 1/q2) * (x - 1/q3)))

        # Compare: they should be close for small u, but NOT equal
        # (the rational is the leading order of the trigonometric)
        g_rat_f = float(g_rational)

        return {
            "g_rational": g_rat_f,
            "G_trigonometric": float(G_trig),
            "ratio": float(G_trig) / g_rat_f if g_rat_f != 0 else None,
            "close_at_small_u": abs(float(G_trig) - g_rat_f) / abs(g_rat_f) < 0.1,
        }

    def verify_en_cascade_dimensions(self) -> Dict[str, Any]:
        """Verify the bar complex dimension hierarchy across E_n levels.

        E_1 bar: P(q)     (partition function)
        E_2 bar: P(q)^2   (bigraded, from Dunn: E_2 = E_1 x E_1)
        E_3 bar: P(q)^3   (trigraded, for class L/G)

        At arity n, the chain-level dimensions are:
          E_1: p(n) (partitions)
          E_2: tau_2(n) = sum_{a+b=n} p(a)*p(b)  (2-component multipartitions)
          E_3: tau_3(n) = sum_{a+b+c=n} p(a)*p(b)*p(c) (3-component)
        """
        from compute.lib.holomorphic_cs_chiral_engine import _partition_count

        max_n = 8
        results = {}
        for n in range(max_n + 1):
            p_n = _partition_count(n)
            tau_2_n = sum(_partition_count(a) * _partition_count(n - a)
                         for a in range(n + 1))
            tau_3_n = sum(_partition_count(a) * _partition_count(b) *
                         _partition_count(n - a - b)
                         for a in range(n + 1)
                         for b in range(n - a + 1))
            results[n] = {
                "E_1 (partitions)": p_n,
                "E_2 (2-multipartitions)": tau_2_n,
                "E_3 (3-multipartitions)": tau_3_n,
                "E_2 >= E_1": tau_2_n >= p_n,
                "E_3 >= E_2": tau_3_n >= tau_2_n,
            }
        return results

    def verify_kappa_ch_under_projection(self) -> Dict[str, Any]:
        """kappa_ch is preserved under dimensional projection E_3 -> E_2 -> E_1.

        This is a structural invariant: the modular characteristic depends
        only on the E_1 data (the chiral algebra on a curve), not on the
        ambient E_n structure.
        """
        b3 = BoundaryAlgebra(3, self.omega)
        b2 = BoundaryAlgebra(2, self.omega)
        b1 = BoundaryAlgebra(1, self.omega)

        k3 = b3.kappa_ch()
        k2 = b2.kappa_ch()
        k1 = b1.kappa_ch()

        return {
            "kappa_ch(E_3)": k3,
            "kappa_ch(E_2)": k2,
            "kappa_ch(E_1)": k1,
            "E_3 == E_2": k3 == k2,
            "E_2 == E_1": k2 == k1,
            "all_equal": k3 == k2 == k1,
        }


# =========================================================================
# 7. The dimensional reduction chain: 6d -> 5d -> 3d
# =========================================================================

class DimensionalReductionChain:
    """The chain of dimensional reductions connecting the three routes.

    6d on C^3      --(shrink z_3)-->   5d on C^2 x R   --(shrink C^2)-->   3d on R^3
    U_{q,t}(...)   --(q->1)-------->   Y(gl_hat_1)     --(h_i->0)------->  Heisenberg

    Each reduction:
      - Forgets one complex (or real) direction
      - Lowers the E_n level by 1
      - Reduces the number of parameters
      - The quantum group degenerates to a simpler algebra
    """

    def __init__(self, h1: Rational, h2: Rational):
        self.omega = OmegaBackground(h1, h2)
        self.route_6d = RouteB_6dHCS(h1, h2)
        self.route_5d = Route5d_Interpolation(h1, h2)

    def reduction_6d_to_5d(self) -> Dict[str, Any]:
        """6d -> 5d: shrink one complex direction (e.g., z_3 -> 0).

        C^3 -> C^2 x R (the z_3 direction becomes a real line).
        U_{q,t}(gl_hat_hat_1) -> Y(gl_hat_1) (quantum toroidal -> affine Yangian).
        Trigonometric structure function -> rational structure function.
        """
        return {
            "geometric": "C^3 -> C^2 x R (collapse z_3 direction)",
            "algebraic": "U_{q,t}(gl_hat_hat_1) -> Y(gl_hat_1)",
            "structure_fn": "G(x;q) -> g(u;h) via x=exp(u), q=exp(h), u->0",
            "en_level": "E_3 -> E_2",
            "parameters": "2 (q,t) -> 1 (sigma_3)",
            "miki": "S_3 -> S_2 (partial: lose one permutation)",
            "r_matrix": "two-parameter R(u,v) -> one-parameter R(u)",
            "status": "CONJECTURAL (6d end) -> PROVED (5d end)",
        }

    def reduction_5d_to_3d(self) -> Dict[str, Any]:
        """5d -> 3d: shrink the holomorphic C^2 (h_i -> 0).

        C^2 x R -> R^3 (in the limit h_i -> 0).
        Y(gl_hat_1) -> Heisenberg (current algebra at level k).
        The Yangian becomes the universal enveloping algebra of the current algebra.
        """
        return {
            "geometric": "C^2 x R -> R^3 (Omega-background -> 0)",
            "algebraic": "Y(gl_hat_1) -> Heisenberg / V_k(gl_1)",
            "structure_fn": "g(u) -> 1 (trivial, commutative limit)",
            "en_level": "E_2 -> E_1",
            "parameters": "1 (sigma_3) -> 0 (classical)",
            "miki": "S_2 -> NONE",
            "r_matrix": "R(u) -> trivial (braiding -> symmetric)",
            "status": "PROVED (both ends)",
        }

    def full_chain(self) -> Dict[str, Any]:
        """The complete 6d -> 5d -> 3d reduction chain."""
        return {
            "chain": [
                {
                    "level": "6d (C^3)",
                    "algebra": "U_{q,t}(gl_hat_hat_1)",
                    "en": "E_3-chiral",
                    "params": 2,
                    "status": "CONJECTURAL",
                },
                {
                    "level": "5d (C^2 x R)",
                    "algebra": "Y(gl_hat_1)",
                    "en": "E_2-chiral",
                    "params": 1,
                    "status": "PROVED",
                },
                {
                    "level": "3d (R^3)",
                    "algebra": "U_q(g) [or Heisenberg for gl_1]",
                    "en": "E_3 (topological!)",
                    "params": 1,
                    "status": "PROVED",
                },
            ],
            "reductions": [
                self.reduction_6d_to_5d(),
                self.reduction_5d_to_3d(),
            ],
            "key_observation": (
                "The 3d theory is topological E_3, while 5d is holomorphic E_2 "
                "and 6d is holomorphic E_3. The 5d theory lives at the interface: "
                "its R-direction is topological (like 3d) and its C^2-directions "
                "are holomorphic (like 6d). The 6d -> 5d reduction is a "
                "deformation-theoretic limit (trigonometric -> rational); "
                "the 5d -> 3d reduction is a classical limit (quantum -> classical)."
            ),
        }


# =========================================================================
# 8. The E_3 braiding comparison: topological vs holomorphic
# =========================================================================

class E3BraidingComparison:
    """Detailed comparison of the E_3 braiding in 3d vs 6d.

    The central technical point: both routes produce E_3 factorization
    algebras, but the braiding mechanisms are fundamentally different.

    3d (topological): braiding from pi_1(SO(3)) = Z/2 (the framing group)
    6d (holomorphic): braiding from Omega-background deformation

    This class computes explicit invariants that distinguish the two.
    """

    def __init__(self, h1: Rational = Rational(37), h2: Rational = Rational(41)):
        self.omega = OmegaBackground(h1, h2)

    def topological_braiding_3d(self) -> Dict[str, Any]:
        """The framed E_3 braiding on R^3 (Route A).

        The framed little 3-disks operad fE_3 acts on Conf_n(R^3).
        Framings of R^3 form a torsor over SO(3).
        pi_1(SO(3)) = Z/2 provides the sign twist.

        For U_q(g): the R-matrix R_{VW} acting on V tensor W satisfies
          R_{VW} = q^{sum_i H_i tensor H_i / 2} * (1 + ...)
        The leading term q^{H tensor H / 2} is the framing contribution.
        """
        return {
            "type": "topological_framed",
            "framing_group": "SO(3)",
            "pi_1": "Z/2",
            "braiding_invariant": "sign twist from double cover Spin(3) -> SO(3)",
            "leading_r_matrix_term": "q^{H tensor H / 2}",
            "at_q_equals_1": "R = identity (trivial braiding, but still E_3)",
            "depends_on_omega_bg": False,
        }

    def holomorphic_braiding_6d(self) -> Dict[str, Any]:
        """The E_3-chiral braiding on C^3 (Route B).

        Conf_2(C^3) ~ S^5, pi_1 = 0.
        The holomorphic E_3 braiding is ENTIRELY from the Omega-background.

        For U_{q,t}(gl_hat_hat_1): the R-matrix is the two-parameter
        R_ch(u,v) = R_1(u) * R_2(v) * R_12(u-v) (Zamolodchikov factorization).
        """
        h1, h2, h3 = self.omega.h1, self.omega.h2, self.omega.h3
        sigma2 = self.omega.sigma2
        sigma3 = self.omega.sigma3

        return {
            "type": "holomorphic_equivariant",
            "framing_group": "U(3) (broken to T^3 by Omega)",
            "pi_1_bare": "0 (from pi_1(S^5) = 0)",
            "pi_1_effective": "Z^3 (from T^3 torus action)",
            "braiding_invariant": f"sigma_3 = {sigma3} (the effective deformation)",
            "leading_r_matrix_term": "g(u-v) (structure function)",
            "at_h_equals_0": "R = identity AND E_3 -> E_inf (symmetric!)",
            "depends_on_omega_bg": True,
            "omega_params": {"h1": h1, "h2": h2, "h3": h3},
        }

    def comparison_table(self) -> Dict[str, Any]:
        """Side-by-side comparison of the two E_3 braidings."""
        return {
            "feature": [
                "E_n level",
                "E_n type",
                "Configuration space link",
                "pi_1 of link",
                "Braiding source",
                "At zero deformation",
                "Parameter count",
                "Miki automorphism",
                "R-matrix type",
                "Zamolodchikov tetrahedron",
                "Status",
            ],
            "3d_CS_R3": [
                "E_3", "topological (framed)", "S^2", "0",
                "pi_1(SO(3)) = Z/2", "still E_3 (not E_inf)", "1 (q)",
                "NO", "single-parameter", "N/A", "PROVED (CFG25)",
            ],
            "6d_hCS_C3": [
                "E_3", "holomorphic (chiral)", "S^5", "0",
                "Omega-background (h1,h2,h3)", "E_inf (symmetric)", "2 (q,t)",
                "YES (S_3)", "two-parameter", "FAILS at O(kappa^2)", "CONJECTURAL",
            ],
        }


# =========================================================================
# 9. Synthesis: the master comparison engine
# =========================================================================

def run_full_comparison(
    gauge_algebra: str = "gl_1",
    k: Rational = Rational(1),
    h1: Rational = Rational(37),
    h2: Rational = Rational(41),
) -> Dict[str, Any]:
    """Run the complete 3d vs 6d comparison.

    This is the master function that produces the full analysis.
    """
    route_a = RouteA_3dCS(gauge_algebra, k)
    route_b = RouteB_6dHCS(h1, h2)
    route_5d = Route5d_Interpolation(h1, h2)
    obstruction = ObstructionAnalysis(route_a, route_b)
    numerical = NumericalVerification(h1, h2)
    reduction = DimensionalReductionChain(h1, h2)
    braiding = E3BraidingComparison(h1, h2)
    config = ConfigurationSpaceBraiding()

    return {
        "route_a": route_a.summary(),
        "route_b": route_b.summary(),
        "route_5d": route_5d.summary(),
        "config_space_comparison": config.compare_3d_vs_6d(),
        "obstructions": obstruction.full_comparison(),
        "braiding_comparison": braiding.comparison_table(),
        "dimensional_reduction": reduction.full_chain(),
        "numerical_checks": {
            "cy_condition": numerical.verify_cy_condition(),
            "g_unitarity": numerical.verify_structure_function_symmetry(),
            "classical_limit": numerical.verify_classical_limit(),
            "koszul_inversion": numerical.verify_koszul_parameter_inversion(),
            "kappa_preservation": numerical.verify_kappa_ch_under_projection(),
        },
    }


# =========================================================================
# 10. Trigonometric vs rational structure functions
# =========================================================================

class StructureFunctionComparison:
    """Compare rational (5d/Yangian) vs trigonometric (6d/toroidal) structure functions.

    Rational (Yangian, from 5d):
      g(u) = prod_{i=1}^{3} (u - h_i) / (u + h_i)
      Poles at u = -h_i, zeros at u = h_i.

    Trigonometric (quantum toroidal, from 6d):
      G(x) = prod_{i=1}^{3} (x - q_i) / (x - q_i^{-1})
      where q_i = exp(h_i), x = exp(u).
      Poles at x = q_i^{-1}, zeros at x = q_i.

    The relationship: G(exp(u)) -> g(u) as h_i -> 0 (rational limit).
    """

    def __init__(self, h1: Rational, h2: Rational):
        self.omega = OmegaBackground(h1, h2)
        self.h1 = self.omega.h1
        self.h2 = self.omega.h2
        self.h3 = self.omega.h3

    def rational_structure_function(self, u: float) -> float:
        """g(u) = prod(u - h_i) / prod(u + h_i)."""
        h1, h2, h3 = float(self.h1), float(self.h2), float(self.h3)
        num = (u - h1) * (u - h2) * (u - h3)
        den = (u + h1) * (u + h2) * (u + h3)
        if abs(den) < 1e-15:
            return float('inf')
        return num / den

    def trigonometric_structure_function(self, x: float) -> float:
        """G(x) = prod(x - q_i) / prod(x - q_i^{-1}).

        where q_i = exp(h_i).
        """
        h1, h2, h3 = float(self.h1), float(self.h2), float(self.h3)
        q1, q2, q3 = np.exp(h1), np.exp(h2), np.exp(h3)
        num = (x - q1) * (x - q2) * (x - q3)
        den = (x - 1/q1) * (x - 1/q2) * (x - 1/q3)
        if abs(den) < 1e-15:
            return float('inf')
        return num / den

    def verify_rational_limit(self, u_test: float = 0.01) -> Dict[str, Any]:
        """Verify G(exp(u)) -> g(u) as h_i -> 0 (the rational limit).

        For small h_i, exp(h_i) ~ 1 + h_i, and the trigonometric function
        reduces to the rational one up to a multiplicative factor.

        More precisely: with x = exp(u) and q_i = exp(epsilon * h_i),
        as epsilon -> 0:
          G(x; q_i) / G(1; q_i) -> g(u; h_i)
        up to O(epsilon) corrections.
        """
        g_rat = self.rational_structure_function(u_test)
        G_trig = self.trigonometric_structure_function(np.exp(u_test))

        # The ratio G_trig / g_rat should approach a constant as u -> 0
        ratio = G_trig / g_rat if abs(g_rat) > 1e-15 else float('inf')

        return {
            "u_test": u_test,
            "g_rational": g_rat,
            "G_trigonometric": G_trig,
            "ratio": ratio,
            "note": (
                "For GENERIC (large) h_i, the rational and trigonometric "
                "functions differ significantly. They agree in the limit "
                "h_i -> 0 (which sends both to 1). The trigonometric is the "
                "'correct' 6d structure function; the rational is its 5d projection."
            ),
        }

    def miki_s3_action_on_G(self, x: float) -> Dict[str, Any]:
        """The S_3 Miki action on the trigonometric structure function.

        The Miki automorphism permutes (q_1, q_2, q_3) cyclically:
          G(x; q_1, q_2, q_3) -> G(x; q_2, q_3, q_1)

        Since G is symmetric in (q_1, q_2, q_3) [the numerator is
        prod(x - q_i) and the denominator is prod(x - q_i^{-1}),
        both symmetric], the Miki action on G itself is TRIVIAL.
        The nontrivial action is on the GENERATORS E(z), F(z), K(z)
        of U_{q,t}(gl_hat_hat_1), not on the structure function.
        """
        h1, h2, h3 = float(self.h1), float(self.h2), float(self.h3)
        q1, q2, q3 = np.exp(h1), np.exp(h2), np.exp(h3)

        G_original = self.trigonometric_structure_function(x)
        # Under Miki S: (q1,q2,q3) -> (q2,q3,q1)
        num_miki = (x - q2) * (x - q3) * (x - q1)
        den_miki = (x - 1/q2) * (x - 1/q3) * (x - 1/q1)
        G_miki = num_miki / den_miki if abs(den_miki) > 1e-15 else float('inf')

        return {
            "G_original": G_original,
            "G_after_miki": G_miki,
            "are_equal": abs(G_original - G_miki) < 1e-10,
            "explanation": (
                "G is symmetric in (q_1,q_2,q_3), so the Miki S_3 action "
                "on G is trivial. The nontrivial Miki action is on the "
                "GENERATORS of U_{q,t}: E(z) <-> K^+(z), F(z) <-> K^-(z). "
                "This generator permutation is NOT visible at the level of "
                "the structure function."
            ),
        }


# =========================================================================
# 11. Koszul duality comparison: 3d vs 6d
# =========================================================================

class KoszulDualityComparison:
    """Compare Koszul duality in the 3d and 6d settings.

    3d: A^! = V_{k'}(g) at reflected level k' = -k - 2h^vee
    6d: A^! carries E_3-chiral structure with (h1,h2,h3) -> (-h1,-h2,-h3)

    Both implement the same abstract pattern:
      E_n factorization algebra -> bar complex -> Verdier dual -> defect algebra

    The PARAMETER INVERSION is the hallmark of Koszul duality at each level.
    """

    def __init__(self, h1: Rational = Rational(37), h2: Rational = Rational(41)):
        self.omega = OmegaBackground(h1, h2)

    def koszul_at_3d(self, k: Rational, h_vee: Rational) -> Dict[str, Any]:
        """Koszul duality in 3d CS.

        A = V_k(g): boundary algebra at level k
        A^! = V_{k'}(g): defect algebra at reflected level k' = -k - 2h^vee
        kappa_ch(A) + kappa_ch(A^!) = rho_K (family-dependent conductor)
        """
        k_dual = -k - 2 * h_vee
        return {
            "input": f"V_{k}(g) (Kac-Moody at level k={k})",
            "output": f"V_{k_dual}(g) (Kac-Moody at reflected level k'={k_dual})",
            "parameter_inversion": f"k -> k' = -k - 2*h^vee = {k_dual}",
            "at_critical": f"k = -h^vee = {-h_vee}: k' = -(-h^vee) - 2*h^vee = -h^vee "
                           "(self-dual at critical level!)",
        }

    def koszul_at_5d(self) -> Dict[str, Any]:
        """Koszul duality in 5d hol CS.

        A = Y(gl_hat_1): affine Yangian at parameters (h1,h2,h3)
        A^! = Y(gl_hat_1): at inverted parameters (-h1,-h2,-h3)
        g(u) * g^!(u) = g(u) * g(-u) = 1 (unitarity = Koszul pairing)
        """
        return {
            "input": "Y(gl_hat_1) at (h1,h2,h3)",
            "output": "Y(gl_hat_1) at (-h1,-h2,-h3)",
            "parameter_inversion": "(h1,h2,h3) -> (-h1,-h2,-h3)",
            "structure_fn_relation": "g^!(u) = g(-u) = 1/g(u)",
            "kappa_ch_relation": "kappa_ch + kappa_ch^! = 0 (conductor = 0)",
        }

    def koszul_at_6d(self) -> Dict[str, Any]:
        """Koszul duality in 6d holomorphic theory.

        A = U_{q,t}(gl_hat_hat_1) at parameters (q,t)
        A^! = U_{q^{-1},t^{-1}}(gl_hat_hat_1)^{cop} at inverted parameters
        G(x) * G^!(x) = G(x) * G(1/x) = 1 (trigonometric unitarity)

        STATUS: CONJECTURAL (conj:e3-koszul-duality).
        """
        return {
            "input": "U_{q,t}(gl_hat_hat_1) at (q,t)",
            "output": "U_{q^{-1},t^{-1}}(gl_hat_hat_1)^{cop}",
            "parameter_inversion": "(q,t) -> (q^{-1},t^{-1})",
            "structure_fn_relation": "G^!(x) = G(1/x) = 1/G(x)",
            "kappa_ch_relation": "kappa_ch + kappa_ch^! = 0 (conductor = 0, free-field)",
            "status": "CONJECTURAL (conj:e3-koszul-duality)",
            "miki_commutes": True,  # Miki commutes with parameter inversion
        }

    def comparison(self) -> Dict[str, Any]:
        """Compare Koszul duality at all three levels."""
        return {
            "3d": self.koszul_at_3d(Rational(1), Rational(0)),
            "5d": self.koszul_at_5d(),
            "6d": self.koszul_at_6d(),
            "universal_pattern": (
                "At ALL levels, Koszul duality inverts the deformation parameters. "
                "3d: k -> -k - 2h^vee. 5d: h_i -> -h_i. 6d: q -> q^{-1}, t -> t^{-1}. "
                "The structure function relation g * g^! = 1 (unitarity) holds at all levels. "
                "The kappa complementarity kappa + kappa^! = rho_K is the characteristic-level "
                "manifestation of parameter inversion."
            ),
        }


# =========================================================================
# 12. Summary verdict
# =========================================================================

def verdict() -> str:
    """The answer to the KEY QUESTION: does CFG25 directly generalize?

    Short answer: the LOGICAL PATTERN generalizes; the IMPLEMENTATION does not.
    """
    return (
        "The CFG25 construction of U_q(g) from 3d CS on R^3 and the conjectural "
        "construction of U_{q,t}(gl_hat_hat_1) from 6d hCS on C^3 share the SAME "
        "LOGICAL PATTERN: E_3 factorization algebra -> Koszul duality -> quantum group. "
        "However, the jump from R^3 (real) to C^3 (complex) introduces THREE new features "
        "that prevent direct generalization:\n\n"
        "(O1) HOLOMORPHIC vs TOPOLOGICAL: The 3d braiding is topological (from framed E_3, "
        "robust at any coupling). The 6d braiding is holomorphic (from Omega-background, "
        "disappears at h_i = 0). The nontrivial 6d braiding is PARAMETER-DEPENDENT; "
        "the 3d braiding is not.\n\n"
        "(O2) TWO PARAMETERS vs ONE: C^3 has three complex directions with equivariant "
        "weights (h1,h2,h3) subject to one CY constraint, giving two free parameters "
        "(q,t). R^3 has one coupling constant k giving one parameter q. The extra "
        "parameter governs the second affinization (the second hat in gl_hat_hat_1).\n\n"
        "(O3) MIKI AUTOMORPHISM: C^3 has an S_3 symmetry permuting its three complex "
        "directions, producing the Miki automorphism of U_{q,t}. R^3 has continuous SO(3) "
        "symmetry with no discrete S_3 analogue. The Miki is algebra-specific (AP-CY22), "
        "not operadic.\n\n"
        "The 5d theory on C^2 x R interpolates: it has the Omega-background (like 6d) but "
        "only one effective parameter (like 3d). The dimensional reduction chain "
        "6d -> 5d -> 3d systematically strips away these new features."
    )
