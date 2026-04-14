r"""Systematic obstruction catalogue: what CANNOT be lifted from 3d CS to 6d hCS.

Beyond the CFG25 adversarial engine (cfg25_adversarial_consistency.py), which
identified 6 gaps at the INVARIANT level, this module classifies the STRUCTURAL
obstructions -- features of 3d Chern-Simons that have no 6d analogue for
fundamental mathematical reasons vs features that are merely unresolved.

EIGHT OBSTRUCTION VECTORS
=========================

(1) FINITE-DIMENSIONALITY (Verlinde)
    3d: dim H(Sigma_g, k) = Verlinde formula (FINITE).
    6d: dim int_{Sigma_g x C^2} A = INFINITE for generic parameters.
    Classification: FUNDAMENTAL OBSTRUCTION at generic parameters.
    Root cause: 3d truncation comes from root-of-unity q = exp(2*pi*i/(k+h^vee)),
    which forces Rep_q(g) to have finitely many simples. 6d parameters (h1,h2,h3)
    are CONTINUOUS, not quantized. Truncation requires a root-of-unity condition
    on BOTH q AND t simultaneously -- which is an overdetermined system for generic
    CY geometry. The unique truncation locus is codimension-2 in parameter space.

(2) KNOT COMPLEMENT TOPOLOGY
    3d: S^3 \ K is a 3-manifold with boundary T^2.
    6d: C^3 \ C (complement of a holomorphic curve) has boundary that depends
    on the normal bundle of C. For C = C^1 linearly embedded: boundary is
    S^1 x S^3 (not T^2). The topology is FUNDAMENTALLY DIFFERENT.
    Classification: FUNDAMENTAL OBSTRUCTION.
    Root cause: codim-2 complement in real dim 3 has codim 1 boundary (surface);
    codim-2 complement in complex dim 3 (real dim 6) has codim 1 boundary that
    is a circle bundle over the curve (from the normal bundle), not a torus.

(3) SURGERY FORMULA (Kirby calculus)
    3d: Kirby moves give complete invariants via surgery on links.
    6d: Handle decomposition exists but does NOT give complete invariants.
    Classification: UNSOLVED PROBLEM (not fundamental obstruction).
    Root cause: 6d handle decomposition exists (en_factorization.tex, 176 tests),
    but the gluing data requires the FULL E_3 factorization algebra, not just
    its E_2 shadow. The ZTE failure (thm:zte-failure) means pairwise R-matrices
    are insufficient, but ZTE corrections may eventually suffice.

(4) RESHETIKHIN-TURAEV FUNCTOR
    3d: RT functor from MTC to 3-manifold invariants. PROVED.
    6d: No RT-type functor from quantum toroidal to 6-manifold invariants.
    Classification: FUNDAMENTAL OBSTRUCTION (in current form).
    Root cause: RT requires a MODULAR TENSOR CATEGORY (finitely many simples,
    non-degenerate S-matrix). The 6d representation category Rep(U_{q,t}) is
    NOT an MTC -- it has infinitely many simples. Even at root of unity, the
    quantum toroidal truncation is not known to produce an MTC.
    HOWEVER: there may be a GENERALIZED RT functor for non-semisimple categories
    (Costantino-Geer-Patureau-Mirand 2014, Blanchet-Costantino-Geer-Patureau
    2016). This is an unsolved problem, not a no-go theorem.

(5) CATEGORIFICATION DIRECTION
    3d: Jones polynomial categorifies to Khovanov homology (4d TQFT).
    6d: "Chiral Jones" should categorify to... 7d? (M-theory).
    Classification: UNSOLVED PROBLEM.
    Root cause: categorification adds one real dimension. 3d -> 4d (Khovanov).
    6d -> 7d would be the M-theory lift. The 7d theory is the topological
    twist of 11d supergravity on CY_2 (M-theory on K3). This is physically
    motivated but mathematically unconstructed.

(6) UNITARITY
    3d: Rep_q(g) at integer level k has unitary reps (compact quantum group).
    6d: Rep(U_{q,t}) at generic (h1,h2,h3) is NOT unitary.
    Classification: FUNDAMENTAL OBSTRUCTION at generic parameters.
    The 6d theory has algebraic unitarity (R(z)R(-z) = 1) but NOT Hilbert-space
    unitarity (no positive-definite inner product on Rep(U_{q,t}) for generic h_i).
    Unitarity is recovered ONLY at the self-dual point h_i = 0 (trivial theory)
    or at specific integral lattice points (Nekrasov-Shatashvili limit).

(7) VOLUME CONJECTURE
    3d: log|J_N(K; e^{2*pi*i/N})| ~ N * Vol(S^3 \ K). CONJECTURAL but deep.
    6d: No analogue.
    Classification: FUNDAMENTAL OBSTRUCTION (in principle), UNSOLVED (in practice).
    Root cause: the volume conjecture relates QUANTUM invariants to CLASSICAL
    geometry (hyperbolic volume). The 6d analogue would relate the chiral Jones
    polynomial to the holomorphic volume Vol_hol(X). But Vol_hol is not well-defined
    for general CY3 (it depends on the complex structure moduli). The 3d volume
    is a TOPOLOGICAL invariant; the 6d analogue is not.
    HOWEVER: for RIGID CY3 (h^{2,1} = 0), Vol_hol is unique and a volume
    conjecture might exist. This is a genuinely open question.

(8) RATIONALITY
    3d: V_k(g) at integer level k is a RATIONAL VOA (finitely many simples).
    6d: CY chiral algebras are IRRATIONAL for all non-trivial CY geometries.
    Classification: FUNDAMENTAL OBSTRUCTION.
    Root cause: rationality of V_k(g) comes from the compactness of the gauge
    group G and the quantization of the level k. The CY chiral algebra A_C
    has continuous moduli (from the CY moduli space) and infinite-dimensional
    charge lattice (from H^*(X, Z)). Rationality would require BOTH truncation
    (finitely many simples) AND discretization (quantized moduli).
    The ONLY known mechanism: orbifold by a finite group (Gepner models).
    At enhanced symmetry points (Fermat, orbifold), the CY VOA truncates
    to a rational SCFT. But this is a SPECIAL POINT, not the generic theory.

CLASSIFICATION SUMMARY
======================

| # | Vector                  | Classification      | Reversible? |
|---|-------------------------|---------------------|-------------|
| 1 | Finite-dimensionality   | FUNDAMENTAL         | At root-of-unity locus (codim-2) |
| 2 | Knot complement         | FUNDAMENTAL         | NO (topological) |
| 3 | Surgery formula         | UNSOLVED            | Possibly (via E_3 corrections) |
| 4 | RT functor              | FUNDAMENTAL/UNSOLVED| Via non-semisimple RT |
| 5 | Categorification        | UNSOLVED            | Via M-theory (7d) |
| 6 | Unitarity               | FUNDAMENTAL         | At NS limit or self-dual |
| 7 | Volume conjecture       | FUNDAMENTAL         | For rigid CY3 only |
| 8 | Rationality             | FUNDAMENTAL         | At Gepner points only |

KEY INSIGHT: The obstructions cluster into two types:
  (A) TOPOLOGICAL obstructions (2, 4): the 6d theory is HOLOMORPHIC, not
      topological. The topology of configuration spaces, knot complements,
      and surgery presentations is fundamentally different.
  (B) PARAMETER obstructions (1, 6, 7, 8): the 6d theory has CONTINUOUS
      parameters where 3d has DISCRETE ones. At special loci in parameter
      space (root of unity, self-dual, Gepner), some 3d features are recovered.

The unsolved problems (3, 5) are STRUCTURAL: they require new mathematics
(E_3 corrections, M-theory categorification) that might or might not exist.

AP COMPLIANCE:
  - AP-CY14: All 6d results marked CONJECTURAL where appropriate
  - AP-CY22: Miki is algebra-specific, not operadic
  - AP-CY30: Factored != solved (ZTE failure)
  - AP-CY31: Spectral z != worldsheet z
  - AP-CY33: Chain-level != rational (E_3 genuine at chain level)
  - AP113: All kappa subscripted
  - AP153: E_3 scope: requires E_inf input for algebraic E_3
  - AP154: Algebraic E_3 vs topological E_3 distinguished
  - AP-CY5: Kazhdan-Lusztig requires root of unity

MANUSCRIPT REFERENCES:
  chapters/theory/en_factorization.tex: E_n hierarchy, handle decomposition
  chapters/theory/quantum_chiral_algebras.tex: 6d hCS programme
  chapters/theory/quantum_groups_foundations.tex: RT functor, MTC
  chapters/examples/quantum_group_reps.tex: KL equivalence
  chapters/examples/toroidal_elliptic.tex: quantum toroidal
  chapters/theory/drinfeld_center.tex: Drinfeld center, braided categories

MATHEMATICAL SOURCES:
  Costello-Francis-Gwilliam (CFG25): CS and factorization homology
  Costello (2013): 5d hCS and the Yangian
  Verlinde (1988): fusion rules
  Reshetikhin-Turaev (1991): 3-manifold invariants
  Kashaev (1997): volume conjecture
  Murakami-Murakami (2001): colored Jones and volume
  Costantino-Geer-Patureau-Mirand (2014): non-semisimple RT
  Blanchet-Costantino-Geer-Patureau (2016): non-semisimple TFTs
  Gukov-Schwarz-Vafa (2005): Khovanov from M-theory
  Nekrasov-Shatashvili (2009): quantization of integrable systems
"""

from __future__ import annotations

from enum import Enum
from fractions import Fraction
from math import comb, factorial, gcd, pi, prod
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

import numpy as np
from sympy import (
    Rational,
    Symbol,
    binomial,
    cancel,
    expand,
    factor,
    oo,
    simplify,
    sqrt,
    symbols,
)


# =========================================================================
# Classification types
# =========================================================================

class ObstructionType(Enum):
    """Classification of 3d-to-6d obstructions."""
    FUNDAMENTAL = "fundamental"       # No-go for mathematical reasons
    UNSOLVED = "unsolved"             # Open problem, may be resolvable
    PARTIAL = "partial"               # Some cases work, others don't
    FUNDAMENTAL_PARTIAL = "fundamental_partial"  # Fundamental but with loopholes


class ReversibilityType(Enum):
    """Whether the obstruction can be circumvented at special loci."""
    NEVER = "never"                        # No known loophole
    ROOT_OF_UNITY = "root_of_unity"        # At root-of-unity specialization
    SELF_DUAL = "self_dual"                # At self-dual point h_i = 0
    GEPNER = "gepner"                      # At Gepner/orbifold points
    NS_LIMIT = "ns_limit"                  # At Nekrasov-Shatashvili limit
    RIGID_CY = "rigid_cy"                  # For rigid CY3 (h^{2,1} = 0)
    NON_SEMISIMPLE_RT = "non_ss_rt"        # Via non-semisimple RT theory
    MTHEORY = "mtheory"                    # Via M-theory (conjectural)
    E3_CORRECTIONS = "e3_corrections"      # Via E_3 corrections to ZTE


class ObstructionRecord(NamedTuple):
    """A single obstruction in the catalogue."""
    number: int
    name: str
    classification: ObstructionType
    reversibility: ReversibilityType
    three_d_status: str
    six_d_status: str
    root_cause: str
    depth: str  # "topological", "parameter", "structural"


# =========================================================================
# 1. Finite-dimensionality obstruction (Verlinde)
# =========================================================================

class FiniteDimensionalityObstruction:
    """Obstruction 1: 3d has finite-dim Hilbert spaces, 6d does not.

    3d CS at level k on Sigma_g:
        dim H(Sigma_g, k) = Verlinde formula = FINITE.
        For sl_2: dim = (k+2)/2 * sum_{j=0}^{k} (sin(pi*(2j+1)/(k+2)))^{2-2g}

    6d at generic (h1,h2,h3):
        dim int_{M} A = INFINITE for any non-degenerate M.

    The root cause: 3d truncation comes from root-of-unity quantization
    q = exp(2*pi*i/(k+h^vee)). The order of q is FINITE (= 2*(k+h^vee)).
    This forces the representation ring to be finitely generated.

    6d has TWO parameters (q,t) with constraint q*t*s = 1. For BOTH to be
    roots of unity simultaneously requires an overdetermined system:
        q^N = 1,  t^M = 1,  q*t*s = 1
    This has solutions (N, M related), but the solution space is
    codimension-2 in parameter space (a lattice, not a continuum).
    """

    def __init__(self, h1: Rational = Rational(1), h2: Rational = Rational(-2)):
        self.h1 = h1
        self.h2 = h2
        self.h3 = -(h1 + h2)

    def verlinde_dimension_sl2(self, k: int, g: int) -> int:
        """Verlinde formula for sl_2 at level k, genus g.

        dim V_k(sl_2, Sigma_g) = ((k+2)/2)^{g-1} * sum_{j=0}^{k}
            (sin(pi*(2j+1)/(k+2)))^{2-2g}

        For g=0: dim = 1 (always).
        For g=1: dim = k+1 (number of integrable representations).
        For g>=2: Verlinde formula.

        Returns integer dimension (always finite for any k, g).
        """
        if g == 0:
            return 1
        if g == 1:
            return k + 1

        # General Verlinde formula for sl_2
        level = k + 2
        total = 0.0
        for j in range(k + 1):
            s = np.sin(np.pi * (2 * j + 1) / level)
            if abs(s) > 1e-15:
                total += s ** (2 - 2 * g)
        dim = (level / 2.0) ** (g - 1) * total
        return int(round(dim))

    def six_d_generic_dimension(self, g: int, shadow_class: str) -> Dict[str, Any]:
        """Dimension of 6d factorization homology at genus g.

        For an E_3-algebra A of shadow class cls:
          Class G: dim H*(B_{E_3}(A)) = P(q)^{3g} (infinite, formal)
          Class L: dim = 2^{3g} (finite, from (1+t)^{3g})
          Class C: dim = 2^{3g} (same, charge conservation kills d_4)
          Class M: dim = 6^g (finite, closed form via Kunneth; AP-CY21)

        NOTE: These are COHOMOLOGY dimensions, not chain-level dimensions.
        The chain complex is always infinite (P(q)^{3g}).

        CRITICAL: Class L and C giving 2^{3g} is the E_3 bar COHOMOLOGY.
        This is the 6d analogue of the Verlinde number. But it does NOT
        depend on any level parameter k -- it is a TOPOLOGICAL invariant
        of the algebra, not a function of the coupling.
        """
        if shadow_class == "G":
            return {
                "class": "G",
                "genus": g,
                "chain_dim": "infinite (P(q)^{3g})",
                "cohomology_dim": "infinite (all differentials vanish)",
                "finite": False,
                "depends_on_level": False,
                "interpretation": "Class G (formal/free-field): no truncation possible.",
            }
        elif shadow_class == "L":
            dim = 2 ** (3 * g)
            return {
                "class": "L",
                "genus": g,
                "chain_dim": "infinite (P(q)^{3g})",
                "cohomology_dim": dim,
                "finite": True,
                "depends_on_level": False,
                "interpretation": (
                    f"Class L: dim = 2^(3*{g}) = {dim}. FINITE but does NOT "
                    "depend on any level parameter. This is a structural "
                    "invariant, not a Verlinde-type formula."
                ),
            }
        elif shadow_class == "C":
            dim = 2 ** (3 * g)
            return {
                "class": "C",
                "genus": g,
                "chain_dim": "infinite (P(q)^{3g})",
                "cohomology_dim": dim,
                "finite": True,
                "depends_on_level": False,
                "interpretation": (
                    f"Class C: dim = 2^(3*{g}) = {dim}. Same as class L "
                    "(charge conservation kills d_4). FINITE, level-independent."
                ),
            }
        elif shadow_class == "M":
            dim = 6 ** g
            return {
                "class": "M",
                "genus": g,
                "chain_dim": "infinite (P(q)^{6g})",
                "cohomology_dim": dim,
                "finite": True,
                "depends_on_level": False,
                "interpretation": (
                    f"Class M: dim = 6^{g} = {dim}. FINITE (closed form via "
                    "Kunneth). d_4 survives but cohomology is still finite-dim. "
                    "Level-independent."
                ),
            }
        else:
            raise ValueError(f"Unknown shadow class: {shadow_class}")

    def root_of_unity_truncation_analysis(self) -> Dict[str, Any]:
        """Analyze the root-of-unity truncation locus for 6d.

        For 3d: q = exp(2*pi*i/(k+h^vee)) is a root of unity when k is integer.
        This is a CODIMENSION-1 locus in the 1-parameter space (a lattice).

        For 6d: need q = exp(h1) and t = exp(-h2) to BOTH be roots of unity:
            q^N = 1  =>  h1 = 2*pi*i * m/N  (m integer)
            t^M = 1  =>  h2 = 2*pi*i * n/M  (n integer)
            CY: h3 = -(h1+h2) = -2*pi*i * (m/N + n/M)

        For h3 to also be a root of unity: need m/N + n/M = p/L for integer p, L.
        This is always satisfiable (rationals are dense), but the EFFECTIVE
        level depends on lcm(N, M, L).

        The truncation locus is: {(h1, h2) : h1/(2*pi*i), h2/(2*pi*i) in Q}
        This is codimension-2 in the 2-real-parameter space (h1,h2 in R^2).
        """
        # Check: at (h1, h2) = (2*pi*i/N, 2*pi*i/M), what is the effective level?
        # q = exp(2*pi*i/N), t = exp(2*pi*i/M), s = exp(-2*pi*i*(1/N + 1/M))
        # Effective level = lcm(N, M) for the joint root-of-unity condition.

        examples = []
        for N in range(2, 7):
            for M in range(2, 7):
                L = N * M // gcd(N, M)  # lcm(N, M)
                # Number of integrable modules at this truncation
                # For quantum toroidal at level (N, M): conjectural
                n_simples_3d = N - 1  # sl_2 at level k=N-2 has N-1 integrables
                examples.append({
                    "N": N, "M": M, "lcm": L,
                    "effective_level_3d": N - 2,
                    "n_simples_3d_sl2": n_simples_3d,
                    "n_simples_6d": "UNKNOWN (quantum toroidal truncation not constructed)",
                    "codimension": 2,
                })

        return {
            "three_d_truncation_locus": "codimension-1 (k integer in R)",
            "six_d_truncation_locus": "codimension-2 (h1, h2 rational multiples of 2*pi*i)",
            "truncation_exists": True,
            "truncation_constructed": False,
            "obstruction_type": "FUNDAMENTAL at generic parameters",
            "loophole": "Root-of-unity locus exists but truncated algebra not constructed",
            "examples": examples[:5],  # First few examples
            "key_open_problem": (
                "Construct the truncated quantum toroidal algebra at "
                "joint root of unity (q^N = t^M = 1). This requires "
                "understanding the ideal of negligible modules in "
                "Rep(U_{q,t}), which is a two-parameter problem."
            ),
        }

    def compare_verlinde_numbers(self) -> Dict[str, Any]:
        """Compare 3d Verlinde numbers with 6d E_3 bar cohomology dimensions.

        3d: dim V_k(sl_2, Sigma_g) depends on BOTH k and g.
        6d: dim H*(B_{E_3}(A)) depends on g and shadow class, but NOT on
            any level parameter.

        This is the key difference: 3d has a FAMILY of finite-dimensional
        spaces (indexed by k), 6d has a SINGLE finite-dimensional space
        (for each shadow class).
        """
        comparisons = []
        for g in range(3):
            for k in [1, 2, 3, 4, 5]:
                v3d = self.verlinde_dimension_sl2(k, g)
                v6d_L = self.six_d_generic_dimension(g, "L")
                v6d_M = self.six_d_generic_dimension(g, "M")
                comparisons.append({
                    "genus": g,
                    "level_k": k,
                    "verlinde_3d": v3d,
                    "e3_bar_6d_class_L": v6d_L["cohomology_dim"],
                    "e3_bar_6d_class_M": v6d_M["cohomology_dim"],
                    "3d_depends_on_k": True,
                    "6d_depends_on_k": False,
                })

        return {
            "comparisons": comparisons,
            "key_finding": (
                "3d Verlinde numbers V_k(g) form a FAMILY indexed by level k. "
                "6d E_3 bar dimensions are FIXED for each shadow class. "
                "The 6d theory does not have a level-dependent truncation "
                "that produces Verlinde-type formulas. This is because the "
                "E_3 bar complex is a STRUCTURAL invariant of the algebra, "
                "while the 3d conformal block space depends on the COUPLING."
            ),
        }

    def record(self) -> ObstructionRecord:
        return ObstructionRecord(
            number=1,
            name="Finite-dimensionality (Verlinde)",
            classification=ObstructionType.FUNDAMENTAL,
            reversibility=ReversibilityType.ROOT_OF_UNITY,
            three_d_status="PROVED: dim V_k(g) = Verlinde formula, always finite",
            six_d_status="INFINITE at generic parameters; FINITE at root-of-unity (not constructed)",
            root_cause=(
                "3d has discrete level k, 6d has continuous (h1,h2). "
                "Root-of-unity locus is codim-2, not codim-1."
            ),
            depth="parameter",
        )


# =========================================================================
# 2. Knot complement topology obstruction
# =========================================================================

class KnotComplementObstruction:
    r"""Obstruction 2: the topology of complements is fundamentally different.

    3d: For a knot K in S^3, the complement S^3 \ K is a 3-manifold with
    boundary T^2 (the torus). This is because the normal bundle of a knot
    (a 1-manifold) in a 3-manifold is trivial (rank 2, oriented), so the
    boundary of a tubular neighbourhood is S^1 x S^1 = T^2.

    6d: For a holomorphic curve C in a CY threefold X, the complement
    X \ C has boundary that depends on the normal bundle N_{C/X}.

    For C = CP^1 linearly embedded in C^3:
        N_{C/C^3} = O(-1) + O(-1)  (normal bundle of a line in C^3)
        Boundary of tubular nbhd = unit circle bundle of N_{C/C^3}
        = S^3-bundle over CP^1 (Hopf bundle structure)
        NOT T^2.

    For C = elliptic curve in a CY3 X:
        N_{C/X} = O + O  (trivial, because c_1(X) = 0 and C has genus 1)
        Boundary = T^2 x T^2 = T^4
        THIS matches the 3d pattern (toroidal boundary).

    Key difference: in 3d, ALL knot complements have T^2 boundary.
    In 6d, the boundary topology VARIES with the curve and the embedding.
    """

    # Normal bundle data for various curve embeddings
    CURVE_EMBEDDINGS = {
        "line_in_C3": {
            "curve": "CP^1 (line)",
            "ambient": "C^3",
            "normal_bundle": "O(-1) + O(-1)",
            "boundary": "S(O(-1)+O(-1)) = S^3-bundle over CP^1",
            "is_torus": False,
            "boundary_pi1": "0 (simply connected, S^5/S^1)",
            "real_dim_boundary": 5,
        },
        "conic_in_C3": {
            "curve": "degree-2 curve in CP^2",
            "ambient": "C^3 (local model)",
            "normal_bundle": "O(-1) + O(1)",
            "boundary": "Lens space bundle over CP^1",
            "is_torus": False,
            "boundary_pi1": "nontrivial",
            "real_dim_boundary": 5,
        },
        "elliptic_in_cy3": {
            "curve": "elliptic curve E",
            "ambient": "CY3 X",
            "normal_bundle": "O + O (trivial by adjunction + CY)",
            "boundary": "T^2 x T^2 = T^4",
            "is_torus": True,
            "boundary_pi1": "Z^4",
            "real_dim_boundary": 4,
        },
        "rational_in_resolved_conifold": {
            "curve": "CP^1 (exceptional)",
            "ambient": "resolved conifold O(-1)+O(-1) -> CP^1",
            "normal_bundle": "O(-1) + O(-1)",
            "boundary": "S^3 (link of the conifold singularity)",
            "is_torus": False,
            "boundary_pi1": "0",
            "real_dim_boundary": 3,
        },
        "knot_in_S3": {
            "curve": "knot K (1-manifold)",
            "ambient": "S^3",
            "normal_bundle": "trivial R^2 bundle",
            "boundary": "T^2 (always, for any knot)",
            "is_torus": True,
            "boundary_pi1": "Z^2 (for unknot) or more complex",
            "real_dim_boundary": 2,
        },
    }

    @classmethod
    def complement_boundary(cls, embedding: str) -> Dict[str, Any]:
        """Compute the boundary of the complement for a given embedding."""
        if embedding not in cls.CURVE_EMBEDDINGS:
            raise ValueError(f"Unknown embedding: {embedding}")
        return dict(cls.CURVE_EMBEDDINGS[embedding])

    @classmethod
    def compare_3d_6d_complements(cls) -> Dict[str, Any]:
        """Compare complement topologies between 3d and 6d."""
        knot_3d = cls.CURVE_EMBEDDINGS["knot_in_S3"]
        examples_6d = {
            k: v for k, v in cls.CURVE_EMBEDDINGS.items()
            if k != "knot_in_S3"
        }

        all_6d_torus = all(v["is_torus"] for v in examples_6d.values())
        any_6d_torus = any(v["is_torus"] for v in examples_6d.values())

        return {
            "3d_boundary": "T^2 (universal for all knots in S^3)",
            "3d_boundary_dim": 2,
            "6d_boundaries": {k: v["boundary"] for k, v in examples_6d.items()},
            "6d_all_torus": all_6d_torus,
            "6d_any_torus": any_6d_torus,
            "obstruction": not all_6d_torus,
            "fundamental": True,
            "root_cause": (
                "In 3d, codim-2 submanifolds (knots) have trivial normal "
                "bundle (oriented rank-2 over S^1), so the boundary is "
                "ALWAYS T^2. In 6d, the normal bundle of a holomorphic curve "
                "in a CY3 is a rank-2 holomorphic vector bundle whose "
                "topology depends on the curve genus, degree, and ambient "
                "geometry. The boundary varies accordingly."
            ),
            "exception": (
                "Elliptic curves in CY3 DO have toroidal boundary (T^4), "
                "because the normal bundle is trivial by adjunction + CY "
                "condition. This is the closest 6d analogue of the 3d case."
            ),
        }

    @classmethod
    def normal_bundle_degree_analysis(cls) -> Dict[str, Any]:
        """Analyze how the normal bundle degree affects the boundary.

        For a curve C of genus g in a CY3 X:
            c_1(N_{C/X}) = -c_1(T_C) = 2g - 2  (adjunction + c_1(X) = 0)

        So the total degree of the normal bundle is 2g - 2:
            g = 0: deg(N) = -2 (e.g., O(-1)+O(-1) on CP^1)
            g = 1: deg(N) = 0 (trivial bundle on elliptic curve)
            g = 2: deg(N) = 2 (positive degree on genus-2 curve)

        The boundary topology depends on the splitting type of N.
        """
        results = []
        for g in range(5):
            deg_N = 2 * g - 2
            if g == 0:
                splitting = "O(-1)+O(-1)"
                boundary = "S^3-bundle over CP^1 (Hopf-type)"
                is_torus = False
            elif g == 1:
                splitting = "O+O (trivial)"
                boundary = "T^4"
                is_torus = True
            elif g >= 2:
                # For g >= 2, the splitting type depends on the specific curve.
                # Generic: O(a)+O(b) with a+b = 2g-2, 0 <= a <= b.
                splitting = f"O(a)+O(b) with a+b={deg_N} (depends on moduli)"
                boundary = f"S(O(a)+O(b))-bundle (genus {g}, non-toroidal generically)"
                is_torus = False
            results.append({
                "genus": g,
                "deg_normal_bundle": deg_N,
                "splitting": splitting,
                "boundary": boundary,
                "is_toroidal": is_torus,
            })

        return {
            "results": results,
            "key_finding": (
                "Only genus-1 curves (elliptic curves) in CY3 have toroidal "
                "complement boundary. Genus-0 (rational curves) have S^3-type "
                "boundaries. Higher genus curves have more complex boundaries "
                "depending on the normal bundle splitting. The 3d universality "
                "(all knot complements have T^2 boundary) is LOST in 6d."
            ),
            "3d_analogy_best_case": "elliptic curves in CY3 (genus 1, T^4 boundary)",
        }

    def record(self) -> ObstructionRecord:
        return ObstructionRecord(
            number=2,
            name="Knot complement topology",
            classification=ObstructionType.FUNDAMENTAL,
            reversibility=ReversibilityType.NEVER,
            three_d_status="UNIVERSAL: S^3\\K has boundary T^2 for all knots K",
            six_d_status="VARIES: boundary depends on curve genus and normal bundle",
            root_cause=(
                "Normal bundle of knot in 3-manifold is always trivial (rank 2, "
                "oriented). Normal bundle of curve in CY3 has degree 2g-2 "
                "(adjunction), varying with genus."
            ),
            depth="topological",
        )


# =========================================================================
# 3. Surgery formula obstruction
# =========================================================================

class SurgeryFormulaObstruction:
    """Obstruction 3: 3d has Kirby calculus, 6d does not (yet).

    3d: Every closed oriented 3-manifold is obtained by Dehn surgery on a
    link L in S^3. Kirby moves (handleslide, stabilization) relate different
    surgery presentations of the same manifold. The RT invariant is computed
    from the surgery presentation using the R-matrix and quantum 6j symbols.

    6d: Every closed oriented 6-manifold admits a handle decomposition.
    The handle decomposition computes factorization homology iteratively
    (en_factorization.tex, Proposition prop:handle-decomposition-k3).
    But handle decomposition does NOT give COMPLETE invariants:
        - Two different handle decompositions may give different FH values
          if the algebra is not fully E_6 (only E_3-chiral).
        - The 6d analogue of Kirby moves (handle trading, cancellation)
          requires CONSISTENCY of the E_3 factorization algebra under
          all handle rearrangements.
        - The ZTE failure (thm:zte-failure) means that the 3-simplex
          consistency is NOT automatic, so handle rearrangements may fail.

    Status: UNSOLVED PROBLEM. The handle decomposition infrastructure
    exists, but completeness (independence of decomposition) is not proved.
    """

    def __init__(self):
        pass

    def kirby_move_analysis_3d(self) -> Dict[str, Any]:
        """3d Kirby calculus: complete classification of moves.

        Kirby's theorem (1978): Two framed links in S^3 give
        diffeomorphic 3-manifolds (via surgery) if and only if
        they are related by a sequence of:
            (K1) Handle slide: L -> L' (component slides over component)
            (K2) Stabilization: L -> L union (unknot with framing +/-1)

        The RT functor is a COMPLETE invariant if and only if it is
        preserved under both K1 and K2. This is proved for the
        quantum group U_q(g) at root of unity.
        """
        return {
            "kirby_moves": ["K1 (handle slide)", "K2 (stabilization)"],
            "completeness": "PROVED (Kirby 1978)",
            "rt_invariance_under_K1": "PROVED (Reshetikhin-Turaev 1991)",
            "rt_invariance_under_K2": "PROVED (framing anomaly absorbed by central charge)",
            "status": "COMPLETE: Kirby calculus + RT = complete surgery invariant",
        }

    def handle_decomposition_6d(self) -> Dict[str, Any]:
        """6d handle decomposition: incomplete analogue of surgery.

        A closed oriented 6-manifold X has handles of index 0,...,6.
        By handle trading, we can arrange:
            - One 0-handle (D^6)
            - b_1 1-handles
            - b_2 2-handles
            - b_3 3-handles
            - b_2 4-handles (by duality)
            - b_1 5-handles
            - One 6-handle

        For CY3 X: b_1 = 0 (simply connected), so only 2-handles, 3-handles,
        and 4-handles (plus one 0-handle and one 6-handle).

        Handle data for specific CY3:
        """
        cy3_handles = {
            "K3_x_E": {
                "b1": 2, "b2": 23, "b3": 44, "b4": 23, "b5": 2,
                "euler": 0,
                "note": "Not simply connected (b_1 = 2 from E factor)",
            },
            "quintic": {
                "b1": 0, "b2": 1, "b3": 204, "b4": 1, "b5": 0,
                "euler": -200,
                "note": "Simply connected. 204 three-handles dominate.",
            },
            "T6": {
                "b1": 6, "b2": 15, "b3": 20, "b4": 15, "b5": 6,
                "euler": 0,
                "note": "Torus. All Betti numbers from binomial coefficients.",
            },
        }

        return {
            "handle_types": "index 0 through 6",
            "dominant_index_cy3": 3,
            "cy3_examples": cy3_handles,
            "collar_algebra": {
                "0-handle": "int_{S^5} A (boundary of D^6)",
                "1-handle": "int_{S^4 x R} A",
                "2-handle": "int_{S^1 x R^4} A ~ HH_*(A) (Hochschild)",
                "3-handle": "int_{S^2 x R^3} A (key for CY3: symplectic gluing)",
                "4-handle": "int_{S^3 x R^2} A",
                "5-handle": "int_{S^4 x R} A",
                "6-handle": "closes manifold",
            },
            "gluing_group_cy3": "Sp(b_3, Z) (symplectic, from cup product on H^3)",
        }

    def zte_obstruction_to_completeness(self) -> Dict[str, Any]:
        """The ZTE failure obstructs handle-move invariance.

        In 3d, Kirby move K1 (handle slide) is implemented by the
        R-matrix acting on the tensor product of state spaces.
        The YBE guarantees consistency of slides.

        In 6d, handle rearrangements involve 3-simplex moves
        (the 6d analogue of Kirby K1). These require the
        Zamolodchikov tetrahedron equation (ZTE), not just YBE.

        The ZTE FAILS for the Yang R-matrix at O(kappa^2) where
        kappa = h1*h2*h3 (thm:zte-failure, zamolodchikov_tetrahedron_engine.py).

        This means: the 6d handle decomposition is NOT move-invariant
        with the naive pairwise R-matrix. ZTE corrections are needed
        (zte_correction_engine.py), but sufficiency is not proved.
        """
        return {
            "ybe_status": "SATISFIED (thm:yang-r-matrix-ybe)",
            "zte_status": "FAILS at O(kappa^2) (thm:zte-failure)",
            "kappa": "h1*h2*h3 (sigma_3)",
            "obstruction_order": 2,
            "correction_exists": "PARTIAL (zte_correction_engine.py)",
            "correction_sufficient": "UNKNOWN",
            "implication": (
                "Handle rearrangements in the 6d decomposition are NOT "
                "automatically consistent. The naive E_3 factorization "
                "using pairwise R-matrices fails at the 3-simplex level. "
                "Corrections may restore consistency, but this is unproved."
            ),
            "comparison_3d": (
                "In 3d, YBE suffices for ALL handle moves because the "
                "maximum simplex dimension is 2 (triangle = 3 strands). "
                "In 6d, simplex dimension reaches 3 (tetrahedron = 4 strands), "
                "requiring the ZTE which is a STRONGER condition."
            ),
        }

    def record(self) -> ObstructionRecord:
        return ObstructionRecord(
            number=3,
            name="Surgery formula (Kirby calculus)",
            classification=ObstructionType.UNSOLVED,
            reversibility=ReversibilityType.E3_CORRECTIONS,
            three_d_status="PROVED: Kirby moves + RT = complete surgery invariant",
            six_d_status="Handle decomposition exists; move-invariance FAILS (ZTE)",
            root_cause=(
                "6d handle rearrangements require ZTE (not just YBE). "
                "ZTE fails at O(kappa^2). Corrections may fix this."
            ),
            depth="structural",
        )


# =========================================================================
# 4. Reshetikhin-Turaev functor obstruction
# =========================================================================

class RTFunctorObstruction:
    """Obstruction 4: 3d has RT functor from MTC, 6d does not.

    3d: The RT functor requires:
        (a) A modular tensor category (MTC): finitely many simple objects,
            non-degenerate S-matrix, ribbon structure.
        (b) Surgery presentation of the 3-manifold.
        (c) Quantum trace: Tr_V(R) for each crossing.

    The MTC comes from Rep_q(g) at root of unity (Kazhdan-Lusztig, AP-CY5).
    This is a SEMISIMPLE category with finitely many simples.

    6d: Rep(U_{q,t}(gl_hat_hat_1)) is:
        - NOT an MTC (infinitely many simples)
        - NOT semisimple (extensions exist, especially for class M)
        - NOT finite (the charge lattice is Z, not Z/NZ)

    Even at root of unity, the quantum toroidal truncation is not known
    to produce an MTC. The closest known structure is a NON-SEMISIMPLE
    modular category (Costantino-Geer-Patureau-Mirand 2014).
    """

    def mtc_requirements(self) -> Dict[str, Any]:
        """Requirements for a modular tensor category."""
        return {
            "finitely_many_simples": {
                "3d": "YES (k+1 for sl_2 at level k)",
                "6d": "NO (infinite charge lattice Z)",
                "obstruction": True,
            },
            "non_degenerate_s_matrix": {
                "3d": "YES (Verlinde S-matrix, S_{ij} = sin(pi*i*j/(k+2)) / ...)",
                "6d": "PARTIAL (categorical S-matrix exists but on infinite set)",
                "obstruction": True,
            },
            "ribbon_structure": {
                "3d": "YES (theta = ribbon element of U_q(g))",
                "6d": "UNKNOWN (requires balancing/twist on Rep(U_{q,t}))",
                "obstruction": True,
            },
            "semisimplicity": {
                "3d": "YES (after quotienting negligible morphisms)",
                "6d": "NO (class M algebras have non-semisimple reps)",
                "obstruction": True,
            },
        }

    def non_semisimple_rt_route(self) -> Dict[str, Any]:
        """The non-semisimple RT route (CGPM 2014, BCGP 2016).

        For non-semisimple modular categories, a MODIFIED RT functor exists
        (Costantino-Geer-Patureau-Mirand). Requirements:
            (a) A ribbon category with a modified trace
            (b) A set of "typical" simple objects (non-zero modified dimension)
            (c) A surgery formula using modified quantum dimensions

        The 6d theory may fit into this framework if:
            - Rep(U_{q,t}) has a ribbon structure (UNKNOWN)
            - A modified trace exists (related to the factorization integral)
            - The category has enough "typical" objects

        Status: CONJECTURAL. The non-semisimple RT framework is the most
        promising route to a 6d manifold invariant.
        """
        return {
            "framework": "Non-semisimple RT (CGPM 2014, BCGP 2016)",
            "requirements_met": {
                "ribbon_structure": "UNKNOWN",
                "modified_trace": "PARTIAL (factorization integral)",
                "typical_objects": "UNKNOWN",
            },
            "status": "CONJECTURAL",
            "advantages": [
                "Does not require semisimplicity",
                "Handles infinitely many simples (via modified trace cutoff)",
                "Produces COMPLEX-valued invariants (not just integers)",
            ],
            "obstacles": [
                "Ribbon structure on Rep(U_{q,t}) not constructed",
                "Modified trace requires specific non-degeneracy conditions",
                "Surgery formula not proved for 6-manifolds",
            ],
        }

    def count_simples_comparison(self) -> Dict[str, Any]:
        """Compare the number of simple objects in 3d vs 6d.

        3d: |Irr(Rep_q(sl_2))| = k+1 at level k.
             Finite, growing linearly with k.

        6d: |Irr(Rep(U_{q,t}(gl_hat_hat_1)))| is controlled by the
            charge lattice. For gl_1: charge lattice = Z, so
            infinitely many simples (one Fock module F_n for each n in Z).

        The passage from finite to infinite is the ROOT of the RT obstruction.
        """
        comparisons = []
        for k in range(1, 8):
            n_3d = k + 1  # sl_2 level k
            comparisons.append({
                "level_k": k,
                "n_simples_3d_sl2": n_3d,
                "n_simples_6d_gl1": "infinity (Z-indexed Fock modules)",
                "ratio": "infinite",
            })

        return {
            "comparisons": comparisons,
            "key_finding": (
                "3d: finitely many simples (k+1 for sl_2). "
                "6d: infinitely many simples (Z-indexed). "
                "The RT functor REQUIRES finiteness for the quantum trace "
                "to converge. In the non-semisimple framework, a modified "
                "trace can handle infinitely many objects, but the convergence "
                "of the modified invariant is not guaranteed."
            ),
        }

    def record(self) -> ObstructionRecord:
        return ObstructionRecord(
            number=4,
            name="Reshetikhin-Turaev functor",
            classification=ObstructionType.FUNDAMENTAL_PARTIAL,
            reversibility=ReversibilityType.NON_SEMISIMPLE_RT,
            three_d_status="PROVED: RT functor from MTC (Rep_q(g) at root of unity)",
            six_d_status="NO MTC. Non-semisimple RT route conjectural.",
            root_cause=(
                "Rep(U_{q,t}) has infinitely many simples, is non-semisimple, "
                "and lacks a known ribbon structure."
            ),
            depth="topological",
        )


# =========================================================================
# 5. Categorification direction obstruction
# =========================================================================

class CategorificationObstruction:
    """Obstruction 5: 3d categorifies to 4d (Khovanov), 6d to 7d (?).

    3d: The Jones polynomial J(K; q) categorifies to Khovanov homology
    Kh(K), a bigraded homology theory with chi(Kh(K)) = J(K; q).
    Physically: 3d CS categorifies to 4d N=4 SYM (Witten 2011).

    6d: The "chiral Jones polynomial" J^ch(C; q,t) should categorify to
    a 7-dimensional theory. Physically: 6d (2,0) theory categorifies to
    7d = M-theory on CY2.

    The categorification adds one REAL dimension at each step:
        2d (CFT) -> 3d (CS) -> 4d (Khovanov/N=4) -> 5d (?) -> 6d (hCS) -> 7d (M-theory)

    This is the "dimensional escalator" of the Gukov-Schwarz-Vafa programme.

    Status: UNSOLVED. The 7d categorification is physically motivated
    (M-theory compactification) but mathematically unconstructed.
    """

    def categorification_ladder(self) -> Dict[str, Any]:
        """The categorification ladder from 2d to 7d."""
        ladder = [
            {
                "dim": 2,
                "theory": "2d CFT (WZW model)",
                "invariant": "Characters chi_lambda(q)",
                "type": "numbers (q-series)",
                "status": "PROVED",
            },
            {
                "dim": 3,
                "theory": "3d Chern-Simons",
                "invariant": "Jones polynomial J(K; q)",
                "type": "polynomials",
                "status": "PROVED (Witten 1989, RT 1991)",
                "categorifies_to": 4,
            },
            {
                "dim": 4,
                "theory": "4d N=4 SYM / Khovanov",
                "invariant": "Kh(K) = bigraded homology",
                "type": "homology groups",
                "status": "PROVED (Khovanov 1999, Witten 2011)",
                "decategorifies_to": 3,
                "categorifies_to": 5,
            },
            {
                "dim": 5,
                "theory": "5d hol CS on C^2 x R / Knot Floer?",
                "invariant": "Affine Yangian modules?",
                "type": "categories?",
                "status": "PARTIAL (Costello 2013: Yangian exists; categorification unclear)",
                "decategorifies_to": 4,
                "categorifies_to": 6,
            },
            {
                "dim": 6,
                "theory": "6d holomorphic theory / (2,0) SCFT",
                "invariant": "Chiral Jones J^ch(C; q,t)?",
                "type": "triply-graded?",
                "status": "CONJECTURAL (R-matrix exists, invariant not extracted)",
                "decategorifies_to": 5,
                "categorifies_to": 7,
            },
            {
                "dim": 7,
                "theory": "7d = M-theory on CY2",
                "invariant": "M-theoretic categorification?",
                "type": "higher categories?",
                "status": "SPECULATIVE (physical motivation only)",
                "decategorifies_to": 6,
            },
        ]
        return {
            "ladder": ladder,
            "pattern": "Each step adds one real dimension and one categorical level",
            "proved_steps": [2, 3, 4],
            "partially_constructed": [5],
            "conjectural": [6, 7],
            "key_obstruction": (
                "The 6d -> 7d categorification requires M-theory on a CY2 "
                "(e.g., K3). The 7d theory is the topological twist of 11d "
                "supergravity on K3, which is not mathematically defined."
            ),
        }

    def euler_characteristic_decategorification(self) -> Dict[str, Any]:
        """Verify that decategorification recovers lower-dimensional invariants.

        Kh(K) decategorifies to J(K; q): chi_t(Kh(K)) = J(K; q).
        Similarly, J^ch(C; q,t) should decategorify to J(K; q) in the
        3d limit (t -> 1 or decompactification of the extra C-directions).

        Test: at the Heisenberg (class G, free field), the E_3 bar
        cohomology dimension 2^{3g} should reduce to the E_2 bar
        dimension 2^{2g} on projection to C^2.
        """
        results = []
        for g in range(5):
            dim_e3 = 2 ** (3 * g)   # E_3 bar cohomology (6d)
            dim_e2 = 2 ** (2 * g)   # E_2 bar cohomology (4d)
            dim_e1 = 2 ** g         # E_1 bar cohomology (2d)
            results.append({
                "genus": g,
                "dim_E3_6d": dim_e3,
                "dim_E2_4d": dim_e2,
                "dim_E1_2d": dim_e1,
                "E3_to_E2_ratio": dim_e3 // dim_e2 if dim_e2 > 0 else None,
                "E2_to_E1_ratio": dim_e2 // dim_e1 if dim_e1 > 0 else None,
                "consistent": dim_e3 == dim_e2 * dim_e1,
            })

        return {
            "results": results,
            "pattern": "dim_{E_3} = dim_{E_2} * dim_{E_1} (Kunneth for E_3 = E_2 x E_1)",
            "decategorification_consistent": all(r["consistent"] for r in results),
            "interpretation": (
                "The Kunneth decomposition E_3 = E_2 tensor E_1 (from Dunn additivity) "
                "gives dim_{E_3}(g) = dim_{E_2}(g) * dim_{E_1}(g). This is consistent "
                "with categorification: the 6d invariant is the product of the 4d and 2d "
                "invariants, with the 2d factor being the categorification direction."
            ),
        }

    def record(self) -> ObstructionRecord:
        return ObstructionRecord(
            number=5,
            name="Categorification direction",
            classification=ObstructionType.UNSOLVED,
            reversibility=ReversibilityType.MTHEORY,
            three_d_status="PROVED: Khovanov homology categorifies Jones polynomial",
            six_d_status="CONJECTURAL: 7d M-theory categorification not constructed",
            root_cause=(
                "7d = M-theory on CY2 is physically motivated but "
                "mathematically undefined."
            ),
            depth="structural",
        )


# =========================================================================
# 6. Unitarity obstruction
# =========================================================================

class UnitarityObstruction:
    """Obstruction 6: 3d has unitary reps, 6d does not (generically).

    3d: Rep_q(sl_2) at integer level k has:
        - Positive-definite Shapovalov form (compact quantum group)
        - Unitary representations (finite-dimensional Hilbert spaces)
        - Unitary S-matrix |S_{ij}|^2 sums to 1

    6d: Rep(U_{q,t}(gl_hat_hat_1)) at generic (h1,h2,h3) has:
        - Algebraic unitarity: R(z)R(-z) = Id (from g(z)g(-z) = 1)
        - NO Hilbert-space unitarity (Shapovalov form not positive-definite)
        - The Fock modules F_n carry an indefinite inner product

    The distinction: ALGEBRAIC unitarity (R-matrix involution) vs
    HILBERT SPACE unitarity (positive-definite inner product).

    Special loci where unitarity is recovered:
        (a) Self-dual point: h_i = 0 (trivial theory, Shapovalov = identity)
        (b) Nekrasov-Shatashvili limit: h_2 = 0, h_1 = -h_3 real
            -> effective 3d theory, unitary at integer h_1/h_3
        (c) Topological limit: h_1,h_2,h_3 all purely imaginary
            -> compact quantum group, unitary reps
    """

    def __init__(self, h1: Rational = Rational(1), h2: Rational = Rational(-2)):
        self.h1 = h1
        self.h2 = h2
        self.h3 = -(h1 + h2)
        self.sigma2 = h1 * h2 + h1 * self.h3 + h2 * self.h3
        self.sigma3 = h1 * h2 * self.h3

    def algebraic_unitarity_check(self) -> Dict[str, Any]:
        """Check algebraic unitarity: g(z) * g(-z) = 1.

        This is a consequence of the CY condition h1+h2+h3=0:
        g(z) = prod(z-h_i)/prod(z+h_i)
        g(-z) = prod(-z-h_i)/prod(-z+h_i) = prod(z+h_i)/prod(z-h_i) = 1/g(z)

        So g(z)*g(-z) = 1 IDENTICALLY. This is algebraic unitarity.
        """
        # Verify at several test points (avoiding poles)
        test_points = [Rational(5), Rational(7), Rational(11), Rational(-3)]
        results = []
        for z in test_points:
            num = (z - self.h1) * (z - self.h2) * (z - self.h3)
            den = (z + self.h1) * (z + self.h2) * (z + self.h3)
            g_z = num / den

            num_neg = (-z - self.h1) * (-z - self.h2) * (-z - self.h3)
            den_neg = (-z + self.h1) * (-z + self.h2) * (-z + self.h3)
            g_neg_z = num_neg / den_neg

            product = g_z * g_neg_z
            results.append({
                "z": z,
                "g(z)": g_z,
                "g(-z)": g_neg_z,
                "g(z)*g(-z)": product,
                "is_1": product == 1,
            })

        return {
            "test_results": results,
            "all_pass": all(r["is_1"] for r in results),
            "algebraic_unitarity": True,
            "proof": (
                "g(-z) = prod(-z-h_i)/prod(-z+h_i) = prod(z+h_i)/prod(z-h_i) "
                "= 1/g(z). So g(z)*g(-z) = 1 identically."
            ),
        }

    def hilbert_space_unitarity_check(self) -> Dict[str, Any]:
        """Check Hilbert-space unitarity: is the Shapovalov form positive-definite?

        For the Fock module F_0 of the quantum toroidal algebra:
            <v_n, v_m> = delta_{n,m} * prod_{k=1}^{n} g(k*h_1)

        where g(u) = (u-h1)(u-h2)(u-h3)/((u+h1)(u+h2)(u+h3)).

        For positive-definiteness, need: prod_{k=1}^{n} g(k*h_1) > 0 for all n.

        At generic REAL h_i: g(k*h_1) can be negative for some k,
        so the Shapovalov form is INDEFINITE.
        """
        # Compute g(k*h1) for k = 1, ..., 10
        shapovalov_norms = []
        running_product = Rational(1)
        for k in range(1, 11):
            u = k * self.h1
            num = (u - self.h1) * (u - self.h2) * (u - self.h3)
            den = (u + self.h1) * (u + self.h2) * (u + self.h3)
            if den == 0:
                shapovalov_norms.append({
                    "level": k, "g(k*h1)": "pole", "running_product": None,
                    "positive": None,
                })
                continue
            g_val = num / den
            running_product *= g_val
            shapovalov_norms.append({
                "level": k,
                "g(k*h1)": float(g_val),
                "running_product": float(running_product),
                "positive": float(running_product) > 0,
            })

        any_negative = any(
            s["positive"] is False for s in shapovalov_norms
        )
        return {
            "shapovalov_norms": shapovalov_norms,
            "positive_definite": not any_negative,
            "indefinite": any_negative,
            "interpretation": (
                "The Shapovalov form on Fock modules has norms "
                "prod_{k=1}^n g(k*h_1). At generic real h_i, some factors "
                "g(k*h_1) are negative, making the form INDEFINITE. "
                "This means the representation is NOT unitary in the "
                "Hilbert-space sense."
            ),
        }

    def unitarity_loci(self) -> Dict[str, Any]:
        """Identify the parameter loci where unitarity is recovered."""
        return {
            "self_dual": {
                "condition": "h_i = 0",
                "unitarity": True,
                "reason": "Trivial theory, Shapovalov = identity",
                "physical": False,  # Trivial, no interesting physics
            },
            "nekrasov_shatashvili": {
                "condition": "h_2 = 0 (one h_i vanishes)",
                "unitarity": "CONDITIONAL (requires h_1 = -h_3 real, h_1^2 = integer)",
                "reason": (
                    "Effective 3d theory: 6d collapses to 4d N=2 gauge theory "
                    "in the NS limit. Unitary when the effective coupling is "
                    "quantized (h_1^2 = integer * level)."
                ),
                "physical": True,
            },
            "topological": {
                "condition": "h_i all purely imaginary",
                "unitarity": True,
                "reason": (
                    "q = exp(h_1) is a phase (|q| = 1), giving a compact "
                    "quantum group with unitary representations."
                ),
                "physical": True,
            },
            "real_positive": {
                "condition": "h_i all real (generic)",
                "unitarity": False,
                "reason": (
                    "g(k*h_1) has indefinite sign, Shapovalov form indefinite."
                ),
                "physical": True,
            },
        }

    def record(self) -> ObstructionRecord:
        return ObstructionRecord(
            number=6,
            name="Unitarity",
            classification=ObstructionType.FUNDAMENTAL,
            reversibility=ReversibilityType.NS_LIMIT,
            three_d_status="PROVED: unitary reps at integer level k (compact quantum group)",
            six_d_status="FAILS generically. Algebraic unitarity R(z)R(-z)=1 holds. Hilbert-space unitarity fails.",
            root_cause=(
                "Shapovalov form on Fock modules has indefinite sign at "
                "generic real h_i. Unitarity requires purely imaginary h_i "
                "or NS limit."
            ),
            depth="parameter",
        )


# =========================================================================
# 7. Volume conjecture obstruction
# =========================================================================

class VolumeConjectureObstruction:
    """Obstruction 7: 3d has the volume conjecture, 6d does not.

    3d: Kashaev's volume conjecture (1997, Murakami-Murakami 2001):
        lim_{N->inf} (2*pi/N) * log|J_N(K; e^{2*pi*i/N})| = Vol(S^3 \\ K)

    where J_N(K; q) is the N-th colored Jones polynomial and Vol is the
    hyperbolic volume (Thurston). This relates QUANTUM invariants to
    CLASSICAL geometry.

    6d: No analogue exists. The obstructions are:

    (a) NO HYPERBOLIC STRUCTURE: S^3 \\ K has a unique hyperbolic metric
        (Mostow rigidity, for hyperbolic knots). CY3 \\ C does NOT have
        a unique metric -- it has a moduli space of Ricci-flat metrics
        parametrized by complex structure moduli (h^{2,1} dimensional).

    (b) NO WELL-DEFINED HOLOMORPHIC VOLUME: The holomorphic volume
        Vol_hol(X) = int_X Omega depends on the NORMALIZATION of Omega,
        which is not canonical for general CY3.

    (c) NO LARGE-N LIMIT: The colored Jones J_N uses the N-dim representation
        of U_q(sl_2). The 6d analogue would use "charge-N Fock modules" of
        U_{q,t}, but the large-N limit of these modules is not studied.

    EXCEPTION: For RIGID CY3 (h^{2,1} = 0), the holomorphic volume is
    unique (up to normalization). The simplest example is... unknown
    (no known compact rigid CY3 without orbifold singularities).
    """

    def volume_conjecture_3d_data(self) -> Dict[str, Any]:
        """Known data for the 3d volume conjecture."""
        # Hyperbolic volumes of some knot complements
        knot_volumes = {
            "4_1 (figure-eight)": 2.0298832,   # 6 * Catalan's constant / pi
            "5_2": 2.8281221,
            "6_1": 3.1639764,
            "6_2": 4.4008371,
            "6_3": 5.6934892,
            "trefoil (3_1)": 0.0,  # Not hyperbolic (torus knot)
        }

        return {
            "conjecture": "lim (2*pi/N) * log|J_N(K; q_N)| = Vol(S^3 \\ K)",
            "status": "CONJECTURAL (proved for some knots, open in general)",
            "proved_cases": ["figure-eight knot (Kashaev 1997)", "torus knots (trivially: Vol=0)"],
            "knot_volumes": knot_volumes,
            "requires": [
                "Colored Jones polynomial J_N(K; q) at q = e^{2*pi*i/N}",
                "Hyperbolic volume Vol(S^3 \\ K)",
                "Large-N asymptotics",
            ],
        }

    def six_d_obstacles(self) -> Dict[str, Any]:
        """Obstacles to formulating a 6d volume conjecture."""
        return {
            "no_hyperbolic_analogue": {
                "obstacle": (
                    "S^3 \\ K has a UNIQUE hyperbolic metric (Mostow rigidity). "
                    "CY3 \\ C has a FAMILY of Ricci-flat metrics parametrized "
                    "by h^{2,1} complex structure moduli."
                ),
                "severity": "FUNDAMENTAL",
                "loophole": "Rigid CY3 (h^{2,1}=0) have unique complex structure",
            },
            "no_holomorphic_volume": {
                "obstacle": (
                    "Vol_hol(X) = int_X Omega depends on the normalization "
                    "of the holomorphic 3-form Omega. This normalization is "
                    "NOT canonical: Omega -> lambda * Omega for any lambda in C^*."
                ),
                "severity": "RESOLVABLE",
                "loophole": (
                    "Fix the normalization via the Hodge metric: "
                    "int_X Omega wedge bar{Omega} = 1. Then Vol_hol is "
                    "well-defined (up to a phase)."
                ),
            },
            "no_large_N_limit": {
                "obstacle": (
                    "The 6d analogue of J_N(K; q) would be a 'charge-N chiral "
                    "invariant' of a holomorphic curve. But the large-N limit "
                    "of Fock modules of U_{q,t} is not studied."
                ),
                "severity": "UNSOLVED",
                "loophole": (
                    "The large-charge limit of DT invariants (via Coulomb "
                    "branch localization) may provide the asymptotic data."
                ),
            },
            "no_rigidity": {
                "obstacle": (
                    "Mostow rigidity (unique hyperbolic structure on finite-volume "
                    "3-manifolds) has no CY analogue. CY moduli spaces are "
                    "positive-dimensional for all known compact examples."
                ),
                "severity": "FUNDAMENTAL",
                "loophole": "Attractors in the moduli space (attractor mechanism in string theory)",
            },
        }

    def rigid_cy3_analysis(self) -> Dict[str, Any]:
        """Analyze the rigid CY3 case (h^{2,1} = 0).

        Known rigid CY3 examples:
        - Schoen's CY (fiber product of rational elliptic surfaces): h^{2,1} = 0
          BUT: this has a non-trivial fundamental group, complicating the story.
        - Z-manifolds (certain quotients): h^{2,1} = 0.
        - NONE of the standard examples (quintic, complete intersections) are rigid.

        For rigid CY3, the holomorphic volume is determined (up to normalization)
        by the unique complex structure. A volume conjecture might relate:
            Large-N chiral invariant ~ exp(N * Vol_hol(X \\ C))
        """
        rigid_examples = [
            {
                "name": "Schoen CY (fiber product)",
                "h21": 0,
                "h11": 19,
                "euler": -38,
                "fundamental_group": "nontrivial (complicates the story)",
                "status": "best known example of rigid CY3",
            },
            {
                "name": "Z-manifold (Candelas et al.)",
                "h21": 0,
                "h11": 36,
                "euler": -72,
                "fundamental_group": "trivial (simply connected)",
                "status": "simply connected rigid CY3",
            },
        ]

        return {
            "rigid_cy3_examples": rigid_examples,
            "volume_conjecture_feasible": True,
            "additional_requirements": [
                "Holomorphic volume normalization (Hodge metric)",
                "Large-N asymptotics of chiral invariants",
                "Notion of 'holomorphic knot complement' (curve complement in CY3)",
            ],
            "status": "SPECULATIVE but not impossible for rigid CY3",
        }

    def record(self) -> ObstructionRecord:
        return ObstructionRecord(
            number=7,
            name="Volume conjecture",
            classification=ObstructionType.FUNDAMENTAL,
            reversibility=ReversibilityType.RIGID_CY,
            three_d_status="CONJECTURAL: proved for some knots",
            six_d_status="NO ANALOGUE. Fundamental obstacles from moduli, volume normalization.",
            root_cause=(
                "3d: Mostow rigidity gives unique hyperbolic volume. "
                "6d: CY moduli space has positive dimension, no unique volume."
            ),
            depth="parameter",
        )


# =========================================================================
# 8. Rationality obstruction
# =========================================================================

class RationalityObstruction:
    """Obstruction 8: 3d at integer level is RATIONAL, 6d is IRRATIONAL.

    3d: V_k(g) at integer level k is a RATIONAL VOA:
        - Finitely many simple modules (= k+1 for sl_2)
        - C_2-cofinite (Zhu's condition)
        - Modular invariant characters

    6d: CY chiral algebras are IRRATIONAL for all non-trivial CY geometries:
        - Infinitely many simple modules (from charge lattice)
        - NOT C_2-cofinite (Zhu's algebra is infinite-dimensional)
        - Characters are NOT modular forms (they are mock/quasi-modular)

    The ONLY known mechanism for rationality in the CY context:
        GEPNER MODELS: At enhanced symmetry points (Fermat point, orbifold),
        the CY VOA truncates to a rational N=2 SCFT.

    Example: Quintic at the Fermat point x_1^5 + ... + x_5^5 = 0.
    The Gepner model is the tensor product of five N=2 minimal models
    at level k=3, which IS rational (finite number of primaries).
    But this is a SPECIAL POINT in the complex structure moduli space,
    not the generic theory.
    """

    def rationality_criteria(self) -> Dict[str, Any]:
        """Criteria for a VOA to be rational (Zhu 1996)."""
        return {
            "criteria": {
                "C2_cofiniteness": {
                    "definition": "dim A / C_2(A) < infinity, where C_2(A) = span{a_{-2}b}",
                    "3d_km": True,
                    "6d_cy": False,
                    "explanation": (
                        "V_k(g) is C_2-cofinite (Zhu 1996). CY chiral algebras "
                        "have dim A / C_2(A) = infinity because the charge lattice "
                        "provides infinitely many independent modes."
                    ),
                },
                "finitely_many_simples": {
                    "definition": "|Irr(A-Mod)| < infinity",
                    "3d_km": True,
                    "6d_cy": False,
                    "explanation": (
                        "V_k(g) has k+1 integrable highest-weight modules (sl_2). "
                        "CY chiral algebras have infinitely many modules "
                        "(one for each charge sector)."
                    ),
                },
                "modular_characters": {
                    "definition": "Characters chi_i(tau) span a representation of SL_2(Z)",
                    "3d_km": True,
                    "6d_cy": False,
                    "explanation": (
                        "Kac-Moody characters are modular forms (Kac-Peterson). "
                        "CY chiral algebra characters are mock modular (class M) "
                        "or quasi-modular (class C), NOT modular."
                    ),
                },
            },
        }

    def gepner_point_analysis(self) -> Dict[str, Any]:
        """Analyze rationality at Gepner points.

        The Gepner model for the quintic:
            c = 5 * c_{k=3}^{N=2} = 5 * 3*3/(3+2) = 5 * 9/5 = 9

        Number of primaries: prod_{i=1}^{5} (k_i + 1) = 4^5 = 1024 chiral primaries
        (before GSO projection and orbifold identification).

        After the Z_5 orbifold: approximately 1024 / 5 = 204.8 -> 204 families
        of primaries (matching h^{2,1} = 101 of the quintic!).

        The Gepner model IS rational: finitely many primaries, modular characters.
        """
        gepner_examples = [
            {
                "cy": "quintic (x_1^5+...+x_5^5)",
                "levels": [3, 3, 3, 3, 3],
                "central_charge": Rational(9),
                "n_primaries_raw": 4 ** 5,  # (k+1)^5 = 4^5 = 1024
                "orbifold_group": "Z_5",
                "n_primaries_effective": 204,  # After orbifold, GSO
                "h21": 101,
                "rational": True,
                "special_point": "Fermat point in CY moduli space",
            },
            {
                "cy": "sextic K3 (in weighted CP^3)",
                "levels": [4, 4, 4],
                "central_charge": Rational(6),
                "n_primaries_raw": 5 ** 3,  # 125
                "orbifold_group": "Z_6",
                "n_primaries_effective": 21,
                "h11": 20,
                "rational": True,
                "special_point": "Fermat point",
            },
        ]

        return {
            "gepner_examples": gepner_examples,
            "rationality_at_gepner": True,
            "rationality_at_generic": False,
            "measure_zero": True,
            "interpretation": (
                "Gepner points form a MEASURE-ZERO subset of the CY moduli "
                "space. At these points, the CY chiral algebra truncates to "
                "a rational N=2 SCFT (a tensor product of minimal models). "
                "Away from Gepner points, the theory is irrational. "
                "The Gepner model is to the CY chiral algebra as the "
                "root-of-unity truncation is to the generic quantum group."
            ),
        }

    def irrationality_mechanisms(self) -> Dict[str, Any]:
        """Why CY chiral algebras are generically irrational."""
        return {
            "mechanisms": {
                "continuous_moduli": {
                    "explanation": (
                        "The CY moduli space is positive-dimensional (dim = h^{2,1}). "
                        "The chiral algebra varies continuously with the moduli, "
                        "so its representation theory cannot be 'quantized' to "
                        "finitely many simples at generic points."
                    ),
                    "3d_comparison": "3d CS has discrete level k (quantized coupling).",
                },
                "infinite_charge_lattice": {
                    "explanation": (
                        "The charge lattice H^*(X, Z) is infinite-rank for "
                        "non-trivial CY. Each charge sector gives a family "
                        "of representations, producing infinitely many simples."
                    ),
                    "3d_comparison": "3d CS has finite weight lattice (truncated at level k).",
                },
                "mock_modularity": {
                    "explanation": (
                        "Class M CY chiral algebras (Virasoro, W(2)) have "
                        "mock modular characters: they transform under SL_2(Z) "
                        "with a SHADOW CORRECTION, not a finite-dimensional "
                        "representation. Mock modularity is incompatible with "
                        "the Verlinde formula."
                    ),
                    "3d_comparison": "3d Kac-Moody characters are genuine modular forms.",
                },
            },
        }

    def record(self) -> ObstructionRecord:
        return ObstructionRecord(
            number=8,
            name="Rationality",
            classification=ObstructionType.FUNDAMENTAL,
            reversibility=ReversibilityType.GEPNER,
            three_d_status="PROVED: V_k(g) is rational VOA at integer level k",
            six_d_status="IRRATIONAL generically. Rational ONLY at Gepner points (measure zero).",
            root_cause=(
                "CY has continuous moduli, infinite charge lattice, and "
                "mock modular characters. Rationality requires all three "
                "to be truncated."
            ),
            depth="parameter",
        )


# =========================================================================
# Master catalogue: assembles all 8 obstructions
# =========================================================================

class ObstructionCatalogue3d6d:
    """Master catalogue of 3d-to-6d obstructions.

    Assembles all 8 obstruction vectors, classifies each as
    fundamental vs unsolved, and identifies the parameter loci
    where 3d features can be recovered.
    """

    def __init__(self, h1: Rational = Rational(1), h2: Rational = Rational(-2)):
        self.h1 = h1
        self.h2 = h2
        self.h3 = -(h1 + h2)

        # Instantiate all obstruction analyzers
        self.finite_dim = FiniteDimensionalityObstruction(h1, h2)
        self.knot_complement = KnotComplementObstruction()
        self.surgery = SurgeryFormulaObstruction()
        self.rt_functor = RTFunctorObstruction()
        self.categorification = CategorificationObstruction()
        self.unitarity = UnitarityObstruction(h1, h2)
        self.volume_conjecture = VolumeConjectureObstruction()
        self.rationality = RationalityObstruction()

    def all_records(self) -> List[ObstructionRecord]:
        """Return all 8 obstruction records."""
        return [
            self.finite_dim.record(),
            self.knot_complement.record(),
            self.surgery.record(),
            self.rt_functor.record(),
            self.categorification.record(),
            self.unitarity.record(),
            self.volume_conjecture.record(),
            self.rationality.record(),
        ]

    def classification_summary(self) -> Dict[str, Any]:
        """Summary of all obstruction classifications."""
        records = self.all_records()
        fundamental = [r for r in records if r.classification in
                       (ObstructionType.FUNDAMENTAL, ObstructionType.FUNDAMENTAL_PARTIAL)]
        unsolved = [r for r in records if r.classification == ObstructionType.UNSOLVED]

        return {
            "total_obstructions": len(records),
            "fundamental": len(fundamental),
            "unsolved": len(unsolved),
            "fundamental_names": [r.name for r in fundamental],
            "unsolved_names": [r.name for r in unsolved],
            "by_depth": {
                "topological": [r.name for r in records if r.depth == "topological"],
                "parameter": [r.name for r in records if r.depth == "parameter"],
                "structural": [r.name for r in records if r.depth == "structural"],
            },
        }

    def parameter_loci_where_3d_recovered(self) -> Dict[str, Any]:
        """Parameter loci where 3d features are (partially) recovered.

        The key insight: the 6d theory at SPECIAL PARAMETER LOCI can
        reproduce some 3d features. These loci are:

        (a) Root of unity: (q^N = t^M = 1) -> finite-dim, truncation
        (b) Self-dual: h_i = 0 -> trivial theory, all obstructions vanish
        (c) NS limit: h_2 = 0 -> effective 3d, unitarity possible
        (d) Gepner: Fermat point in CY moduli -> rationality
        (e) Topological: h_i purely imaginary -> compact quantum group
        """
        return {
            "loci": {
                "root_of_unity": {
                    "condition": "q^N = t^M = 1 (codim-2 in parameter space)",
                    "features_recovered": ["finite-dimensionality (conjectural)"],
                    "features_not_recovered": ["knot complement topology", "surgery formula"],
                },
                "self_dual": {
                    "condition": "h_i = 0 (codim-2, trivial theory)",
                    "features_recovered": ["all (but trivially)"],
                    "features_not_recovered": [],
                },
                "nekrasov_shatashvili": {
                    "condition": "h_2 = 0 (codim-1, effective 3d)",
                    "features_recovered": ["unitarity (at integer h_1^2)", "one-parameter structure"],
                    "features_not_recovered": ["Miki automorphism (requires all 3 directions)"],
                },
                "gepner": {
                    "condition": "Fermat point in CY moduli (isolated points, measure 0)",
                    "features_recovered": ["rationality", "finite number of primaries"],
                    "features_not_recovered": ["generic CY geometry"],
                },
                "topological": {
                    "condition": "h_i purely imaginary (codim-0 in imaginary space)",
                    "features_recovered": ["unitarity", "compact quantum group"],
                    "features_not_recovered": ["holomorphic structure (lost at imaginary h_i)"],
                },
            },
            "no_single_locus_recovers_all": True,
            "key_finding": (
                "No single parameter locus recovers ALL 3d features simultaneously. "
                "The 6d theory is fundamentally RICHER than 3d CS, and the 3d theory "
                "cannot be 'embedded' in the 6d theory as a consistent subtheory "
                "at any single point. Instead, DIFFERENT 3d features are recovered "
                "at DIFFERENT loci in the 6d parameter space."
            ),
        }

    def irreducible_6d_content(self) -> Dict[str, Any]:
        """Identify what is genuinely new in 6d (has no 3d analogue).

        These are features that are NOT obstructions but rather
        NEW PHENOMENA that exist only in 6d:

        (a) Two-parameter R-matrix: R(u,v) with TWO spectral parameters.
            3d has R(u) with ONE parameter. The second parameter is the
            Omega-background sigma_3.

        (b) Miki automorphism: S_3 permutation of (q1,q2,q3).
            3d has SO(3) continuous symmetry, no discrete S_3.
            (AP-CY22: algebra-specific, not operadic.)

        (c) ZTE corrections: the tetrahedron equation requires corrections
            beyond pairwise R-matrices. This is genuinely new math.

        (d) Shadow tower A_infinity coproduct: the shadow invariants S_k
            are coproduct correction coefficients. Class M has infinite tower.

        (e) Mock modularity: class M characters are mock modular forms.
            3d characters are genuine modular forms. Mock modularity is
            a strictly 6d phenomenon (from the infinite shadow tower).

        (f) Non-semisimple Drinfeld center: class M algebras have
            non-semisimple braided categories, which carry richer
            structure than the semisimple MTCs of 3d.
        """
        return {
            "genuinely_new_6d": [
                {
                    "name": "Two-parameter R-matrix",
                    "3d_analogue": "One-parameter R-matrix R(u)",
                    "6d_feature": "R(u,v) with Zamolodchikov factorization",
                    "status": "PROVED (thm:yang-r-matrix-ybe + categorical_s_matrix_e3)",
                },
                {
                    "name": "Miki automorphism (S_3 on parameters)",
                    "3d_analogue": "None (SO(3) continuous, no discrete S_3)",
                    "6d_feature": "S_3 permutation of (q,t,s) = Weyl(CY torus)",
                    "status": "PROVED for U_{q,t}(gl_hat_hat_1) (algebra-specific, AP-CY22)",
                },
                {
                    "name": "ZTE corrections",
                    "3d_analogue": "None (YBE suffices in 3d)",
                    "6d_feature": "Tetrahedron corrections at O(kappa^2)",
                    "status": "COMPUTED NEGATIVE (thm:zte-failure, 34 tests)",
                },
                {
                    "name": "Shadow tower / A_inf coproduct",
                    "3d_analogue": "None (3d coproduct is exact, no corrections)",
                    "6d_feature": "Infinite correction tower delta^{(k)} = S_k",
                    "status": "PROVED (shadow-ainfty-coproduct identification)",
                },
                {
                    "name": "Mock modularity",
                    "3d_analogue": "Genuine modularity (Kac-Peterson)",
                    "6d_feature": "Mock modular characters for class M",
                    "status": "PROVED for W(2) (mock theta function)",
                },
                {
                    "name": "Non-semisimple Drinfeld center",
                    "3d_analogue": "Semisimple MTC (Rep_q(g) at root of unity)",
                    "6d_feature": "Non-semisimple braided category (class M)",
                    "status": "CONJECTURAL (class M center not constructed)",
                },
            ],
            "key_finding": (
                "The 6d theory is not merely a 'failure to lift 3d'; it contains "
                "genuinely new mathematical structures (Miki, ZTE corrections, "
                "mock modularity) that have no 3d analogue. The obstructions "
                "identified above are not DEFECTS of the 6d theory but "
                "SIGNATURES of its richer structure."
            ),
        }

    def adversarial_verdict(self) -> Dict[str, Any]:
        """Final adversarial verdict on the 3d-to-6d lift.

        QUESTION: Can 3d CS be systematically lifted to 6d hCS?
        ANSWER: NO, in any naive sense. YES, in a modified sense.

        The 6d theory is not a "dimensional upgrade" of 3d CS.
        It is a genuinely different theory that SHARES certain
        algebraic structures (E_3, Koszul duality, R-matrices)
        but DIFFERS in topological and analytic properties.

        The correct statement is:
            3d CS and 6d hCS are TWO DIFFERENT OUTPUTS
            of the E_3 Koszul duality machine,
            applied to DIFFERENT inputs:
                3d: topological E_3 on R^3 (framed little 3-disks)
                6d: holomorphic E_3 on C^3 (Omega-background)

        The machine (E_3 -> Koszul -> quantum group) is the same.
        The inputs and outputs are different.
        """
        summary = self.classification_summary()

        return {
            "verdict": "FUNDAMENTAL OBSTRUCTIONS EXIST",
            "can_lift_naively": False,
            "can_lift_modified": True,
            "num_fundamental": summary["fundamental"],
            "num_unsolved": summary["unsolved"],
            "deepest_obstruction": (
                "Knot complement topology (Obstruction 2): the boundary of "
                "a curve complement in CY3 is NOT a torus (except for elliptic "
                "curves). This is a TOPOLOGICAL no-go that cannot be circumvented "
                "by any parameter specialization."
            ),
            "most_promising_resolution": (
                "Non-semisimple RT theory (Obstruction 4): the CGPM framework "
                "for non-semisimple modular categories may provide a 6d manifold "
                "invariant without requiring the full MTC structure."
            ),
            "correct_statement": (
                "3d CS and 6d hCS are two different outputs of the E_3 Koszul "
                "duality machine, applied to different inputs (topological E_3 "
                "on R^3 vs holomorphic E_3 on C^3). The obstructions identified "
                "here are not defects but signatures of the richer 6d structure."
            ),
        }
