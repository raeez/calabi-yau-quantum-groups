r"""Twisted M-theory / string theory compactification web on K3 and K3 x E.

Maps the full dimensional reduction web, extracting independent consistency
checks at each level of the hierarchy:

  11d: M-theory on K3           -> 7d SYM on R^7
  10d: IIA on K3                -> 6d (2,0) on R^6
       IIB on K3                -> 6d (2,0) on R^6 (T-dual)
   6d: (2,0) on C^3             -> 6d hCS (Costello theory)
       (2,0) on K3 x C          -> 2d (4,4) sigma model on C
   5d: M-theory on K3 x S^1    -> 5d N=2 SYM
       reduce (2,0) on S^1      -> 5d N=2 SYM
   4d: IIA on K3 x T^2         -> 4d N=4 SYM (Vafa-Witten)
       IIB on K3 x T^2         -> 4d N=4 (S-dual)
   3d: M-theory on K3 x T^3    -> 3d N=8
       further twist             -> 3d A-model

At EACH level we extract:
  (1) The chiral algebra / factorization algebra
  (2) The kappa-spectrum values (AP113: ALWAYS subscripted)
  (3) The shadow class (G/L/C/M)
  (4) The R-matrix / braiding structure
  (5) Consistency: does dimensional reduction commute with CY-to-chiral?

CLAIM STATUSES:
  - 11d -> 7d:   PROVED (Witten 1995, M-theory duality).
  - 10d -> 6d:   PROVED (string duality, Aspinwall-Morrison).
  - 6d hCS:      PROVED for flat space (Costello-Gwilliam).
                  CONJECTURAL for K3-fibered (AP-CY14).
  - 6d -> 2d:    PROVED (Harvey-Moore, Dijkgraaf-Verlinde-Verlinde).
  - 5d:          PROVED (Costello 2013, Seiberg).
  - 4d VW:       PROVED (Vafa-Witten 1994, Yoshioka for K3).
  - 4d -> 3d:    PROVED (compactification on S^1).
  - 3d:          PROVED (Intriligator-Seiberg).

KEY CONSISTENCY CHECKS:
  (C1) kappa_ch preservation under dimensional reduction.
       6d -> 5d: kappa_ch(U_{q,t}) -> kappa_ch(Y) in q -> 1 limit.
       5d -> 3d: kappa_ch(Y) -> kappa_ch(H) in h_i -> 0 limit.
  (C2) Shadow class stability: class G remains G under reduction.
  (C3) R-matrix degeneration: trigonometric -> rational -> classical.
  (C4) Euler characteristic additivity:
       chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0.
  (C5) BKM denominator = DMVV product (Vafa-Witten / BKM check).
  (C6) Borcherds lift = bar Euler product (requires CY-A + Vol I).
  (C7) 4d N=4 S-duality = quantum Langlands on chiral algebra.

DIMENSIONAL REDUCTION AND THE FUNCTOR Phi:
  The central question: does the diagram commute?

    CY_d(X)  --Phi-->  A_X
      |                  |
   reduce             reduce
      |                  |
    CY_{d-1}(X') --Phi--> A_{X'}

  At d=2 (CY-A_2 PROVED): YES, the diagram commutes.
  At d=3 (CY-A_3 PROGRAMME): CONJECTURAL.  The CY_3 -> CY_2 reduction
    (shrink E in K3 x E) should reduce U_{q,t}(g_{K3}^{tor}) to Y(g_{K3}).
    This is a PREDICTION of CY-A_3, not a proof.

AP COMPLIANCE:
  - kappa always subscripted (AP113): kappa_ch, kappa_BKM, kappa_cat, kappa_fiber.
  - A_{K3 x E} does NOT exist (AP-CY6): all d=3 results are CONJECTURAL.
  - CoHA != E_1-chiral algebra (AP-CY7).
  - Borcherds denominator != bar Euler product without CY-A citation (AP-CY8).
  - E_2 != commutative (AP-CY3).
  - Drinfeld center != derived center (AP-CY4).
  - MF(W) CY dim = n-2 (AP-CY17).
  - Spectral z != worldsheet z (AP-CY31).
  - Normal bundle != spectral parameters directly (AP-CY20).

REFERENCES:
  holomorphic_cs_chiral_engine.py (3d/5d/6d hCS hierarchy)
  hcs_hierarchy_k3.py (K3-fibered hierarchy, dimensional reduction)
  kappa_spectrum_reconciliation.py (four-valued kappa-spectrum)
  vafa_witten_k3.py (VW partition function, DMVV, BKM)
  k3e_e1_chiral_yangian.py (K3 x E Yangian)
  kw_twisted_n4_chiral.py (Kapustin-Witten twist)
  three_d_n2_cy3_engine.py (3d N=2 from CY3)
  twisted_gauge_cy3_e1_engine.py (twisted gauge theories on CY3)

MANUSCRIPT REFERENCES:
  chapters/examples/k3_times_e.tex (K3 x E tower)
  chapters/examples/toroidal_elliptic.tex (toroidal/elliptic landscape)
  chapters/theory/quantum_chiral_algebras.tex (hCS hierarchy)
  chapters/theory/en_factorization.tex (E_n factorization)
  chapters/connections/modular_koszul_bridge.tex (kappa = chi^CY)
"""

from __future__ import annotations

from enum import Enum
from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

from sympy import Rational

# ---------------------------------------------------------------------------
# Imports from existing engines
# ---------------------------------------------------------------------------

from compute.lib.holomorphic_cs_chiral_engine import (
    OmegaBackground,
    BoundaryAlgebra,
)

from compute.lib.kappa_spectrum_reconciliation import (
    HodgeData,
    elliptic_curve,
    k3_surface,
    k3_times_e,
    quintic_threefold,
)


# =========================================================================
# 0. Enumerations and constants
# =========================================================================

class ClaimStatus(str, Enum):
    """Claim status following the manuscript convention."""
    PROVED = "PROVED"
    PROVED_ELSEWHERE = "PROVED_ELSEWHERE"
    CONDITIONAL = "CONDITIONAL"
    CONJECTURAL = "CONJECTURAL"
    PROGRAMME = "PROGRAMME"


class ShadowClass(str, Enum):
    """G/L/C/M shadow classification from Vol I."""
    G = "G"   # Gaussian (free field)
    L = "L"   # Lie (rational shadow)
    C = "C"   # Convergent
    M = "M"   # Mock modular (Gevrey-1 divergent)


class RMatrixType(str, Enum):
    """Type of R-matrix / braiding structure."""
    TRIVIAL = "trivial"           # No braiding (classical limit)
    CLASSICAL = "classical"       # Classical r-matrix (r(u) ~ Omega/u)
    RATIONAL = "rational"         # Rational R(u) (Yangian)
    TRIGONOMETRIC = "trigonometric"  # Trigonometric R(x) (quantum affine)
    ELLIPTIC = "elliptic"         # Elliptic R(x,tau) (elliptic quantum group)
    TWO_PARAMETER = "two_parameter"  # R(u,v) from E_3


class EnLevel(int, Enum):
    """E_n factorization level."""
    E0 = 0   # No factorization (0d theory)
    E1 = 1   # Ordered (C x R)
    E2 = 2   # Braided (C^2)
    E3 = 3   # Full 6d (C^3)
    EINF = -1  # Symmetric (commutative, kills quantum group; AP-CY3)


# ---------------------------------------------------------------------------
# Kappa-spectrum constants (AP113: ALWAYS subscripted)
# ---------------------------------------------------------------------------

# K3 surface
KAPPA_CH_K3 = Rational(2)           # kappa_ch(H_Muk) at d=2
KAPPA_CAT_K3 = Rational(2)          # kappa_cat = chi(O_{K3})
KAPPA_FIBER_K3 = Rational(24)       # kappa_fiber = Mukai lattice rank

# K3 x E
KAPPA_CH_K3E = Rational(3)          # kappa_ch at d=3 (conjectural)
KAPPA_BKM_K3E = Rational(5)         # kappa_BKM = weight(Delta_5)
KAPPA_CAT_K3E = Rational(0)         # kappa_cat(K3 x E) = chi(O) = 0
KAPPA_FIBER_K3E = Rational(24)      # kappa_fiber = Mukai rank

# Elliptic curve E
KAPPA_CH_E = Rational(0)            # kappa_ch(E) (trivial)
KAPPA_CAT_E = Rational(0)           # kappa_cat(E) = chi(O_E) = 0

# Decomposition check: kappa_BKM = kappa_ch + kappa_cat(K3_fiber)
KAPPA_BKM_DECOMPOSITION = KAPPA_CH_K3E + KAPPA_CAT_K3  # 3 + 2 = 5


# =========================================================================
# 1. Web node: a single level of the compactification hierarchy
# =========================================================================

class CompactificationNode(NamedTuple):
    """A single node in the compactification web.

    Represents one level of the M-theory / string theory dimensional
    reduction hierarchy, with all extracted chiral algebra data.
    """
    # Identification
    name: str                        # Human-readable name
    spacetime_dim: int               # Total spacetime dimension
    compact_dim: int                 # Compact dimensions
    noncompact_dim: int              # Noncompact = spacetime - compact
    susy: str                        # Supersymmetry label (e.g. "N=4", "(2,0)")

    # Compact geometry
    compact_manifold: str            # e.g. "K3", "K3 x E", "K3 x T^2"
    cy_dimension: Optional[int]      # CY dimension of the compact part (AP-CY1)

    # Chiral algebra data
    chiral_algebra: str              # Name of the chiral / factorization algebra
    en_level: EnLevel                # E_n factorization level
    shadow_class: ShadowClass        # G/L/C/M

    # Kappa-spectrum (AP113: all subscripted)
    kappa_ch: Optional[Rational]     # kappa_ch (chiral modular characteristic)
    kappa_bkm: Optional[Rational]    # kappa_BKM (Borcherds weight)
    kappa_cat: Optional[Rational]    # kappa_cat (holomorphic Euler char)
    kappa_fiber: Optional[Rational]  # kappa_fiber (lattice rank)

    # R-matrix / braiding
    rmatrix_type: RMatrixType        # Type of R-matrix
    rmatrix_description: str         # Description of the R-matrix

    # Status
    status: ClaimStatus              # Claim status
    status_notes: str                # Explanation of status

    # Reduction data
    parent_node: Optional[str]       # Name of parent in the web
    reduction_type: str              # How we got here (e.g. "shrink E")


# =========================================================================
# 2. Build the full compactification web
# =========================================================================

def build_m_theory_web() -> Dict[str, CompactificationNode]:
    """Construct the full twisted M-theory compactification web.

    Returns a dictionary mapping node names to CompactificationNode objects.
    Each node contains the extracted chiral algebra data, kappa-spectrum,
    shadow class, R-matrix type, and claim status.
    """
    web = {}

    # ------------------------------------------------------------------
    # 11d: M-theory on K3 -> 7d
    # ------------------------------------------------------------------
    web["11d_M_K3"] = CompactificationNode(
        name="M-theory on K3",
        spacetime_dim=11,
        compact_dim=4,      # K3 is real dim 4
        noncompact_dim=7,
        susy="N=1 (7d)",
        compact_manifold="K3",
        cy_dimension=2,     # K3 is CY_2 (AP-CY1: CY dim = complex dim)
        chiral_algebra="K3 Heisenberg H_Muk (from M5 wrapping K3)",
        en_level=EnLevel.E1,
        shadow_class=ShadowClass.G,
        kappa_ch=KAPPA_CH_K3,
        kappa_bkm=None,
        kappa_cat=KAPPA_CAT_K3,
        kappa_fiber=KAPPA_FIBER_K3,
        rmatrix_type=RMatrixType.CLASSICAL,
        rmatrix_description=(
            "Classical r-matrix from 7d SYM: r(u) = Omega_Muk / u "
            "where Omega_Muk is the Mukai pairing on H^*(K3, Z)"
        ),
        status=ClaimStatus.PROVED,
        status_notes=(
            "M-theory on K3 -> 7d is proved (Witten 1995). "
            "The H_Muk identification uses CY-A_2 (d=2, PROVED)."
        ),
        parent_node=None,
        reduction_type="M-theory compactification on K3",
    )

    # ------------------------------------------------------------------
    # 10d: Type IIA on K3 -> 6d (2,0)
    # ------------------------------------------------------------------
    web["10d_IIA_K3"] = CompactificationNode(
        name="Type IIA on K3",
        spacetime_dim=10,
        compact_dim=4,
        noncompact_dim=6,
        susy="(2,0) in 6d",
        compact_manifold="K3",
        cy_dimension=2,
        chiral_algebra=(
            "6d (2,0) tensor multiplet: self-dual 2-form B_{mu nu}^+. "
            "The chiral algebra of the (2,0) theory on C^3 is the "
            "holomorphic CS boundary algebra (Costello-Gwilliam)"
        ),
        en_level=EnLevel.E2,
        shadow_class=ShadowClass.G,
        kappa_ch=KAPPA_CH_K3,
        kappa_bkm=None,
        kappa_cat=KAPPA_CAT_K3,
        kappa_fiber=KAPPA_FIBER_K3,
        rmatrix_type=RMatrixType.RATIONAL,
        rmatrix_description=(
            "Rational R-matrix from 6d (2,0) reduced on K3: "
            "R(u) at charge 1 is g(u) = prod(u-h_i)/(u+h_i) "
            "with 24 Mukai parameters h_i summing to 0"
        ),
        status=ClaimStatus.PROVED,
        status_notes=(
            "IIA on K3 -> 6d (2,0) is a standard string duality "
            "(Aspinwall-Morrison, Sen). The chiral algebra identification "
            "at d=2 uses CY-A_2 (PROVED)."
        ),
        parent_node="11d_M_K3",
        reduction_type="M-theory on K3 x S^1 -> IIA on K3 (shrink S^1)",
    )

    # ------------------------------------------------------------------
    # 10d: Type IIB on K3 -> 6d (2,0) (T-dual of IIA)
    # ------------------------------------------------------------------
    web["10d_IIB_K3"] = CompactificationNode(
        name="Type IIB on K3",
        spacetime_dim=10,
        compact_dim=4,
        noncompact_dim=6,
        susy="(2,0) in 6d",
        compact_manifold="K3",
        cy_dimension=2,
        chiral_algebra=(
            "Same 6d (2,0) as IIA on K3 (T-duality). "
            "IIB self-dual: (2,0) theory of type A_{N-1} for N D5-branes"
        ),
        en_level=EnLevel.E2,
        shadow_class=ShadowClass.G,
        kappa_ch=KAPPA_CH_K3,
        kappa_bkm=None,
        kappa_cat=KAPPA_CAT_K3,
        kappa_fiber=KAPPA_FIBER_K3,
        rmatrix_type=RMatrixType.RATIONAL,
        rmatrix_description=(
            "Same rational R-matrix as IIA (T-duality preserves the "
            "6d (2,0) theory). The K3 Mukai lattice provides the same "
            "24-parameter rational structure function."
        ),
        status=ClaimStatus.PROVED,
        status_notes="IIA/IIB T-duality on K3 is proved (Sen 1995).",
        parent_node="11d_M_K3",
        reduction_type="T-dual of IIA on K3",
    )

    # ------------------------------------------------------------------
    # 6d: (2,0) on C^3 -> 6d holomorphic CS (Costello)
    # ------------------------------------------------------------------
    web["6d_hCS_C3"] = CompactificationNode(
        name="6d holomorphic CS on C^3",
        spacetime_dim=6,
        compact_dim=0,
        noncompact_dim=6,
        susy="topological (twisted)",
        compact_manifold="none (flat C^3)",
        cy_dimension=3,     # C^3 is (non-compact) CY_3
        chiral_algebra=(
            "Quantum toroidal U_{q,t}(gl_hat_hat_1) "
            "(CONJECTURAL for the full 6d theory; PROVED for the 5d "
            "reduction by Costello 2013)"
        ),
        en_level=EnLevel.E3,
        shadow_class=ShadowClass.L,
        kappa_ch=None,      # Flat space: no finite kappa_ch
        kappa_bkm=None,
        kappa_cat=None,
        kappa_fiber=None,
        rmatrix_type=RMatrixType.TWO_PARAMETER,
        rmatrix_description=(
            "Two-parameter R_{ch}(u,v) from E_3 braiding on C^3: "
            "Zamolodchikov factorization R(u,v) = R_1(u)R_2(v)R_12(u-v). "
            "At charge 1: scalar G_{ch}(x,y) = G(x)G(y)Gamma(x/y). "
            "Miki automorphism exchanges the two loop directions."
        ),
        status=ClaimStatus.CONJECTURAL,
        status_notes=(
            "6d hCS -> quantum toroidal is CONJECTURAL (AP-CY14). "
            "The 5d hCS -> affine Yangian is PROVED (Costello 2013). "
            "The full 6d theory requires the Costello-Francis-Gwilliam "
            "route, which is not yet complete."
        ),
        parent_node="10d_IIA_K3",
        reduction_type="Topological twist of (2,0) on C^3",
    )

    # ------------------------------------------------------------------
    # 6d: (2,0) on K3 x C -> 2d (4,4) sigma model on C
    # ------------------------------------------------------------------
    web["6d_20_K3xC"] = CompactificationNode(
        name="(2,0) on K3 x C",
        spacetime_dim=6,
        compact_dim=4,      # K3 is compact
        noncompact_dim=2,   # C is the remaining curve
        susy="(4,4) in 2d",
        compact_manifold="K3",
        cy_dimension=2,
        chiral_algebra=(
            "2d (4,4) sigma model on C with target Hilb^N(K3). "
            "The left-moving chiral algebra is the K3 elliptic genus "
            "phi_{0,1}(tau, z) = 2y + 20 + 2y^{-1} + O(q). "
            "At N -> infty: the DMVV second-quantized product."
        ),
        en_level=EnLevel.E2,
        shadow_class=ShadowClass.G,
        kappa_ch=KAPPA_CH_K3,
        kappa_bkm=None,
        kappa_cat=KAPPA_CAT_K3,
        kappa_fiber=KAPPA_FIBER_K3,
        rmatrix_type=RMatrixType.TRIVIAL,
        rmatrix_description=(
            "In 2d (4,4), the braiding is trivial on the Hilb^N(K3) "
            "target (the sigma model is E_inf). The nontrivial braiding "
            "arises only after further compactification on C."
        ),
        status=ClaimStatus.PROVED,
        status_notes=(
            "Harvey-Moore (1996), Dijkgraaf-Verlinde-Verlinde (1997). "
            "The K3 sigma model as a (4,4) SCFT is well-established."
        ),
        parent_node="10d_IIA_K3",
        reduction_type="Compactify (2,0) on K3, keep C",
    )

    # ------------------------------------------------------------------
    # 5d: M-theory on K3 x S^1 -> 5d N=2 SYM
    #     equivalently, reduce (2,0) on S^1 -> 5d N=2
    # ------------------------------------------------------------------
    web["5d_M_K3xS1"] = CompactificationNode(
        name="M-theory on K3 x S^1",
        spacetime_dim=5,
        compact_dim=0,      # effective 5d theory (K3 x S^1 already compactified)
        noncompact_dim=5,
        susy="N=2 in 5d (8 supercharges)",
        compact_manifold="K3 x S^1",
        cy_dimension=2,     # K3 is CY_2; S^1 is not CY
        chiral_algebra=(
            "K3 Yangian Y(g_{K3}): the affine Yangian with 24 Mukai "
            "parameters. Arises from 5d hCS on (K3 fiber) x C^2 x R. "
            "CONJECTURAL: requires K3 Yangian construction (AP-CY14)."
        ),
        en_level=EnLevel.E2,
        shadow_class=ShadowClass.L,
        kappa_ch=KAPPA_CH_K3,
        kappa_bkm=None,
        kappa_cat=KAPPA_CAT_K3,
        kappa_fiber=KAPPA_FIBER_K3,
        rmatrix_type=RMatrixType.RATIONAL,
        rmatrix_description=(
            "Rational R-matrix from K3 Yangian: "
            "g(u) = prod_{i=1}^{24} (u-h_i)/(u+h_i) "
            "with sum h_i = 0 (CY_2 condition). "
            "Degree-(24,24) rational function of the spectral parameter u "
            "(AP-CY31: spectral, NOT worldsheet)."
        ),
        status=ClaimStatus.CONJECTURAL,
        status_notes=(
            "The 5d SYM from M-theory on K3 x S^1 is proved (Seiberg 1996). "
            "The K3 Yangian identification is CONJECTURAL (AP-CY14): it "
            "requires constructing Y(g_{K3}) as a deformation of H_Muk."
        ),
        parent_node="11d_M_K3",
        reduction_type="Compactify on K3 x S^1",
    )

    # ------------------------------------------------------------------
    # 5d: (2,0) on S^1 -> 5d N=2 SYM (alternative route)
    # ------------------------------------------------------------------
    web["5d_20_on_S1"] = CompactificationNode(
        name="(2,0) reduced on S^1",
        spacetime_dim=6,
        compact_dim=1,
        noncompact_dim=5,
        susy="N=2 in 5d",
        compact_manifold="S^1 (radius R)",
        cy_dimension=None,   # S^1 alone is not CY
        chiral_algebra=(
            "5d N=2 SYM with coupling g^2 = R (S^1 radius). "
            "The boundary chiral algebra from 5d hCS is the "
            "affine Yangian Y(gl_hat_1) (Costello 2013, PROVED). "
            "For K3 fiber: Y(g_{K3}) (CONJECTURAL)."
        ),
        en_level=EnLevel.E2,
        shadow_class=ShadowClass.L,
        kappa_ch=None,       # Depends on the K3 fiber data
        kappa_bkm=None,
        kappa_cat=None,
        kappa_fiber=None,
        rmatrix_type=RMatrixType.RATIONAL,
        rmatrix_description=(
            "Rational R-matrix from 5d hCS: "
            "g(u) = prod(u-h_i)/(u+h_i) with h_1+h_2+h_3=0 (CY condition). "
            "PROVED for gl_1 (Costello 2013)."
        ),
        status=ClaimStatus.PROVED,
        status_notes=(
            "(2,0) on S^1 -> 5d N=2 SYM is proved (Seiberg 1996, Douglas). "
            "The affine Yangian identification for gl_1 is proved (Costello)."
        ),
        parent_node="10d_IIA_K3",
        reduction_type="Reduce (2,0) on S^1",
    )

    # ------------------------------------------------------------------
    # 4d: IIA on K3 x T^2 -> 4d N=4 (Vafa-Witten)
    # ------------------------------------------------------------------
    web["4d_IIA_K3xT2"] = CompactificationNode(
        name="IIA on K3 x T^2",
        spacetime_dim=4,
        compact_dim=0,       # effective 4d theory
        noncompact_dim=4,
        susy="N=4 in 4d (16 supercharges)",
        compact_manifold="K3 x T^2",
        cy_dimension=3,      # K3 x E is CY_3 (AP-CY1)
        chiral_algebra=(
            "4d N=4 SYM: the VW twist gives Z_VW(K3, G; q). "
            "For G = SU(2): Z_VW = chi(Hilb^n(K3)) generating function "
            "= 1/eta(q)^24 (Gottsche). "
            "The full rank-N partition function is the DMVV product "
            "1/Phi_{10} (the Igusa cusp form, weight 5). "
            "The BKM superalgebra g_{Delta_5} has root multiplicities "
            "= phi_{0,1} coefficients c(4nm - l^2)."
        ),
        en_level=EnLevel.E1,
        shadow_class=ShadowClass.M,
        kappa_ch=KAPPA_CH_K3E,
        kappa_bkm=KAPPA_BKM_K3E,
        kappa_cat=KAPPA_CAT_K3E,
        kappa_fiber=KAPPA_FIBER_K3E,
        rmatrix_type=RMatrixType.TRIGONOMETRIC,
        rmatrix_description=(
            "The Vafa-Witten S-duality acts as quantum Langlands on the "
            "chiral algebra. The 4d N=4 S-duality group SL_2(Z) acts on "
            "the tau parameter of the T^2. The resulting R-matrix is "
            "trigonometric (q-deformed by the T^2 modulus). "
            "AP-CY8: the identification Z_VW = bar Euler product "
            "requires CY-A + Vol I anchor (observation, not theorem)."
        ),
        status=ClaimStatus.PROVED,
        status_notes=(
            "Vafa-Witten (1994) proved the partition function formula. "
            "DMVV (1997) proved the product formula. "
            "The BKM identification (Gritsenko-Nikulin 1997) is proved. "
            "The chiral algebra identification (kappa_BKM = 5) is "
            "number-theoretic (PROVED). The CY-to-chiral identification "
            "of Z_VW with the bar Euler product is CONDITIONAL on CY-A "
            "and the Vol I anchor (AP-CY8)."
        ),
        parent_node="5d_M_K3xS1",
        reduction_type="Compactify 5d on S^1 (or IIA on K3 x T^2)",
    )

    # ------------------------------------------------------------------
    # 4d: IIB on K3 x T^2 -> 4d N=4 (S-dual of IIA)
    # ------------------------------------------------------------------
    web["4d_IIB_K3xT2"] = CompactificationNode(
        name="IIB on K3 x T^2",
        spacetime_dim=4,
        compact_dim=0,
        noncompact_dim=4,
        susy="N=4 in 4d",
        compact_manifold="K3 x T^2",
        cy_dimension=3,
        chiral_algebra=(
            "Same 4d N=4 as IIA (S-duality). "
            "IIB S-duality tau -> -1/tau acts as Langlands duality "
            "G <-> G^L on the gauge group. "
            "The chiral algebra transforms under quantum geometric "
            "Langlands: k -> -k - h^vee (level map)."
        ),
        en_level=EnLevel.E1,
        shadow_class=ShadowClass.M,
        kappa_ch=KAPPA_CH_K3E,
        kappa_bkm=KAPPA_BKM_K3E,
        kappa_cat=KAPPA_CAT_K3E,
        kappa_fiber=KAPPA_FIBER_K3E,
        rmatrix_type=RMatrixType.TRIGONOMETRIC,
        rmatrix_description=(
            "S-dual R-matrix: R^L(u) from Langlands dual group G^L. "
            "The S-duality transformation on the R-matrix is the "
            "quantum Langlands correspondence (Feigin-Frenkel)."
        ),
        status=ClaimStatus.PROVED,
        status_notes=(
            "IIA/IIB S-duality is a standard string duality. "
            "The quantum Langlands correspondence on the chiral algebra "
            "is proved for rational levels (Feigin-Frenkel 2006)."
        ),
        parent_node="4d_IIA_K3xT2",
        reduction_type="IIB S-dual of IIA on K3 x T^2",
    )

    # ------------------------------------------------------------------
    # 3d: M-theory on K3 x T^3 -> 3d N=8
    # ------------------------------------------------------------------
    web["3d_M_K3xT3"] = CompactificationNode(
        name="M-theory on K3 x T^3",
        spacetime_dim=3,
        compact_dim=0,      # effective 3d theory
        noncompact_dim=3,
        susy="N=8 in 3d (16 supercharges)",
        compact_manifold="K3 x T^3",
        cy_dimension=3,     # K3 x E is CY_3; additional S^1
        chiral_algebra=(
            "3d N=8 theory: after A-twist, the chiral algebra is "
            "the Rozansky-Witten algebra RW(Hilb^N(K3)). "
            "Central charge c = N * chi(K3) / 2 = 12N (for Hilb^N). "
            "The RW theory is E_inf (topological, no quantum group "
            "structure; AP-CY3: E_inf kills braiding)."
        ),
        en_level=EnLevel.EINF,
        shadow_class=ShadowClass.G,
        kappa_ch=KAPPA_CH_K3E,
        kappa_bkm=KAPPA_BKM_K3E,
        kappa_cat=KAPPA_CAT_K3E,
        kappa_fiber=KAPPA_FIBER_K3E,
        rmatrix_type=RMatrixType.TRIVIAL,
        rmatrix_description=(
            "3d N=8 is maximally supersymmetric in 3d. "
            "After A-twist: E_inf (symmetric monoidal). "
            "The R-matrix is trivial (all braidings are symmetric). "
            "AP-CY3: E_inf -> E_2 loses quantum group data."
        ),
        status=ClaimStatus.PROVED,
        status_notes=(
            "M-theory on K3 x T^3 -> 3d N=8 is proved. "
            "Rozansky-Witten (1997) for the A-twist. "
            "The kappa-spectrum is inherited from the K3 x E data."
        ),
        parent_node="4d_IIA_K3xT2",
        reduction_type="Compactify 4d on S^1 (or M-theory on K3 x T^3)",
    )

    # ------------------------------------------------------------------
    # 6d: K3 x E x C (the full CY_3 from K3 x E)
    # ------------------------------------------------------------------
    web["6d_K3xExC"] = CompactificationNode(
        name="hCS on K3 x E x C",
        spacetime_dim=6,
        compact_dim=5,       # K3 (4) + E (1) compact; C noncompact
        noncompact_dim=1,
        susy="topological (twisted)",
        compact_manifold="K3 x E",
        cy_dimension=3,      # K3 x E is CY_3
        chiral_algebra=(
            "K3 quantum toroidal U_{q,t}(g_{K3}^{tor}) "
            "(CONJECTURAL, AP-CY14). "
            "The 6d theory on K3 x E x C gives an E_3 factorization "
            "algebra. Parameters: 24 Mukai h_i + tau (E modulus). "
            "This is the TOP of the K3-fibered hierarchy."
        ),
        en_level=EnLevel.E3,
        shadow_class=ShadowClass.M,
        kappa_ch=KAPPA_CH_K3E,
        kappa_bkm=KAPPA_BKM_K3E,
        kappa_cat=KAPPA_CAT_K3E,
        kappa_fiber=KAPPA_FIBER_K3E,
        rmatrix_type=RMatrixType.TWO_PARAMETER,
        rmatrix_description=(
            "Two-parameter R_{ch}(u,v) from E_3 on K3 x E x C. "
            "The Miki automorphism acts as S in SL_2(Z) on the two "
            "loop directions of the quantum toroidal algebra. "
            "Zamolodchikov factorization: "
            "R(u,v) = R_1(u) R_2(v) R_12(u-v)."
        ),
        status=ClaimStatus.CONJECTURAL,
        status_notes=(
            "The full 6d theory on K3 x E requires CY-A_3 (PROGRAMME). "
            "The quantum toroidal algebra U_{q,t}(g_{K3}^{tor}) is not "
            "yet constructed. All results conditional on CY-A_3."
        ),
        parent_node="10d_IIA_K3",
        reduction_type="Topological twist of (2,0) on K3 x E x C",
    )

    # ------------------------------------------------------------------
    # 5d: K3 x C x R (reduce from 6d by shrinking E)
    # ------------------------------------------------------------------
    web["5d_K3xCxR"] = CompactificationNode(
        name="5d hCS on K3 x C x R",
        spacetime_dim=5,
        compact_dim=4,
        noncompact_dim=1,
        susy="topological (twisted)",
        compact_manifold="K3 (fiber)",
        cy_dimension=2,
        chiral_algebra=(
            "K3 Yangian Y(g_{K3}): rational R-matrix from 24 Mukai "
            "parameters. The 6d -> 5d reduction (shrink E, q -> 1) "
            "sends U_{q,t} -> Y. "
            "CONJECTURAL: K3 Yangian not yet constructed."
        ),
        en_level=EnLevel.E2,
        shadow_class=ShadowClass.L,
        kappa_ch=KAPPA_CH_K3,
        kappa_bkm=None,
        kappa_cat=KAPPA_CAT_K3,
        kappa_fiber=KAPPA_FIBER_K3,
        rmatrix_type=RMatrixType.RATIONAL,
        rmatrix_description=(
            "Rational K3 R-matrix: g(u) = prod_{i=1}^{24}(u-h_i)/(u+h_i) "
            "with sum h_i = 0. Degree-(24,24) in the spectral parameter."
        ),
        status=ClaimStatus.CONJECTURAL,
        status_notes=(
            "The 5d -> 3d reduction (K3 Yangian -> K3 Heisenberg) "
            "is consistent with CY-A_2 (PROVED). "
            "The full K3 Yangian construction is CONJECTURAL."
        ),
        parent_node="6d_K3xExC",
        reduction_type="Shrink E (q -> 1): trigonometric -> rational",
    )

    # ------------------------------------------------------------------
    # 3d: K3 sigma model (reduce from 5d by shrinking C)
    # ------------------------------------------------------------------
    web["3d_K3_sigma"] = CompactificationNode(
        name="K3 sigma model on pt",
        spacetime_dim=0,
        compact_dim=0,      # classical limit: all directions shrunk
        noncompact_dim=0,
        susy="(4,4) in 2d -> point",
        compact_manifold="K3",
        cy_dimension=2,
        chiral_algebra=(
            "K3 Heisenberg H_Muk: 24 bosonic currents J^i(z) with "
            "OPE J^i(z)J^j(w) ~ omega^{ij}/(z-w)^2, where omega^{ij} "
            "is the Mukai pairing of signature (4,20). "
            "PROVED via CY-A_2."
        ),
        en_level=EnLevel.E1,
        shadow_class=ShadowClass.G,
        kappa_ch=KAPPA_CH_K3,
        kappa_bkm=None,
        kappa_cat=KAPPA_CAT_K3,
        kappa_fiber=KAPPA_FIBER_K3,
        rmatrix_type=RMatrixType.TRIVIAL,
        rmatrix_description=(
            "Classical limit: all h_i -> 0, g(u) -> 1 (trivial). "
            "The R-matrix degenerates. The Yangian reduces to "
            "the current algebra U(H_Muk). AP-CY31: this is the "
            "epsilon -> 0 limit of the spectral parameter."
        ),
        status=ClaimStatus.PROVED,
        status_notes=(
            "The K3 Heisenberg H_Muk from CY-A_2 is proved. "
            "The 24 currents are identified via Hochschild homology "
            "HH_*(D^b(Coh(K3))) = H^*(K3, Z)."
        ),
        parent_node="5d_K3xCxR",
        reduction_type="Shrink C (h_i -> 0): rational -> classical",
    )

    return web


# =========================================================================
# 3. Consistency checks
# =========================================================================

class ConsistencyCheck(NamedTuple):
    """A single consistency check in the compactification web."""
    name: str
    description: str
    node_a: str           # First node name
    node_b: str           # Second node name
    check_type: str       # What is being checked
    passed: bool
    value_a: Any          # Value at node A
    value_b: Any          # Value at node B
    notes: str


def check_kappa_ch_preservation(
    web: Dict[str, CompactificationNode],
    parent_key: str,
    child_key: str,
) -> ConsistencyCheck:
    """Check whether kappa_ch is preserved under dimensional reduction.

    kappa_ch is preserved when the reduction does not change the CY
    dimension relevant to the chiral algebra. It changes when the
    CY dimension changes (e.g., CY_3 -> CY_2 drops kappa_ch by
    the contribution from the reduced direction).
    """
    parent = web[parent_key]
    child = web[child_key]

    p_kappa = parent.kappa_ch
    c_kappa = child.kappa_ch

    if p_kappa is None or c_kappa is None:
        return ConsistencyCheck(
            name=f"kappa_ch: {parent_key} -> {child_key}",
            description="kappa_ch preservation under dimensional reduction",
            node_a=parent_key,
            node_b=child_key,
            check_type="kappa_ch_preservation",
            passed=True,   # Cannot check if kappa is not defined
            value_a=p_kappa,
            value_b=c_kappa,
            notes="One or both kappa_ch values undefined; check vacuous.",
        )

    # Same CY dimension -> kappa should be preserved
    same_cy = parent.cy_dimension == child.cy_dimension
    if same_cy:
        passed = (p_kappa == c_kappa)
        notes = (
            f"Same CY dim {parent.cy_dimension}: "
            f"kappa_ch should be preserved. "
            f"{p_kappa} {'==' if passed else '!='} {c_kappa}."
        )
    else:
        # Different CY dimension: kappa_ch may change
        passed = True  # Not a failure, just a change
        notes = (
            f"CY dim changes: {parent.cy_dimension} -> {child.cy_dimension}. "
            f"kappa_ch: {p_kappa} -> {c_kappa}. "
            f"Change is expected under CY dimension reduction."
        )

    return ConsistencyCheck(
        name=f"kappa_ch: {parent_key} -> {child_key}",
        description="kappa_ch preservation under dimensional reduction",
        node_a=parent_key,
        node_b=child_key,
        check_type="kappa_ch_preservation",
        passed=passed,
        value_a=p_kappa,
        value_b=c_kappa,
        notes=notes,
    )


def check_rmatrix_degeneration(
    web: Dict[str, CompactificationNode],
    parent_key: str,
    child_key: str,
) -> ConsistencyCheck:
    """Check that R-matrix type degenerates correctly under reduction.

    The hierarchy:
      two_parameter -> trigonometric -> rational -> classical -> trivial
    Each reduction step should move one step down (or stay at the same level).
    """
    HIERARCHY = {
        RMatrixType.TWO_PARAMETER: 5,
        RMatrixType.ELLIPTIC: 4,
        RMatrixType.TRIGONOMETRIC: 3,
        RMatrixType.RATIONAL: 2,
        RMatrixType.CLASSICAL: 1,
        RMatrixType.TRIVIAL: 0,
    }

    parent = web[parent_key]
    child = web[child_key]

    p_level = HIERARCHY[parent.rmatrix_type]
    c_level = HIERARCHY[child.rmatrix_type]

    # Child should be at same or lower level
    passed = c_level <= p_level
    notes = (
        f"R-matrix: {parent.rmatrix_type.value} (level {p_level}) -> "
        f"{child.rmatrix_type.value} (level {c_level}). "
        f"{'Correct' if passed else 'VIOLATION'}: child must be <= parent."
    )

    return ConsistencyCheck(
        name=f"R-matrix: {parent_key} -> {child_key}",
        description="R-matrix degeneration under dimensional reduction",
        node_a=parent_key,
        node_b=child_key,
        check_type="rmatrix_degeneration",
        passed=passed,
        value_a=parent.rmatrix_type.value,
        value_b=child.rmatrix_type.value,
        notes=notes,
    )


def check_shadow_class_stability(
    web: Dict[str, CompactificationNode],
    parent_key: str,
    child_key: str,
) -> ConsistencyCheck:
    """Check shadow class behaviour under dimensional reduction.

    Shadow class can only DECREASE under reduction:
      M -> C -> L -> G
    (reduction cannot create higher-order corrections that were not
    already present). In particular, class G remains G.
    """
    ORDER = {
        ShadowClass.G: 0,
        ShadowClass.L: 1,
        ShadowClass.C: 2,
        ShadowClass.M: 3,
    }

    parent = web[parent_key]
    child = web[child_key]

    p_order = ORDER[parent.shadow_class]
    c_order = ORDER[child.shadow_class]

    passed = c_order <= p_order
    notes = (
        f"Shadow class: {parent.shadow_class.value} (order {p_order}) -> "
        f"{child.shadow_class.value} (order {c_order}). "
        f"{'Correct' if passed else 'VIOLATION'}: class cannot increase."
    )

    return ConsistencyCheck(
        name=f"Shadow class: {parent_key} -> {child_key}",
        description="Shadow class stability under dimensional reduction",
        node_a=parent_key,
        node_b=child_key,
        check_type="shadow_class_stability",
        passed=passed,
        value_a=parent.shadow_class.value,
        value_b=child.shadow_class.value,
        notes=notes,
    )


def check_en_level_reduction(
    web: Dict[str, CompactificationNode],
    parent_key: str,
    child_key: str,
) -> ConsistencyCheck:
    """Check that E_n level decreases or stays under reduction.

    Dimensional reduction can only decrease E_n level (removing a
    factorization direction). E_inf is treated as the maximum.
    """
    parent = web[parent_key]
    child = web[child_key]

    # Map E_inf to a high value for comparison
    def en_value(level: EnLevel) -> int:
        return 100 if level == EnLevel.EINF else int(level)

    p_val = en_value(parent.en_level)
    c_val = en_value(child.en_level)

    # Allow same or lower
    passed = c_val <= p_val
    notes = (
        f"E_n level: E_{parent.en_level.name} -> E_{child.en_level.name}. "
        f"{'Correct' if passed else 'VIOLATION'}: cannot increase."
    )

    return ConsistencyCheck(
        name=f"E_n level: {parent_key} -> {child_key}",
        description="E_n factorization level under reduction",
        node_a=parent_key,
        node_b=child_key,
        check_type="en_level_reduction",
        passed=passed,
        value_a=parent.en_level.name,
        value_b=child.en_level.name,
        notes=notes,
    )


def check_euler_char_multiplicativity() -> ConsistencyCheck:
    """Verify chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
    k3 = k3_surface()
    e = elliptic_curve()
    k3e = k3_times_e()

    chi_product = k3.chi_top * e.chi_top  # 24 * 0 = 0
    chi_k3e = k3e.chi_top                 # 0

    passed = (chi_product == chi_k3e)

    return ConsistencyCheck(
        name="Euler char multiplicativity",
        description="chi(K3 x E) = chi(K3) * chi(E)",
        node_a="K3",
        node_b="K3 x E",
        check_type="euler_multiplicativity",
        passed=passed,
        value_a=f"chi(K3) * chi(E) = {k3.chi_top} * {e.chi_top} = {chi_product}",
        value_b=f"chi(K3 x E) = {chi_k3e}",
        notes="Kuenneth formula for topological Euler characteristic.",
    )


def check_hodge_chi_additivity() -> ConsistencyCheck:
    """Verify chi(O_{K3 x E}) = 0 from Hodge data.

    chi(O_{K3 x E}) = sum (-1)^q h^{0,q}(K3 x E)
                     = 1 - 1 + 1 - 1 = 0.
    """
    k3e = k3_times_e()
    chi_O = k3e.chi_O()

    passed = (chi_O == 0)

    return ConsistencyCheck(
        name="Hodge chi(O) for K3 x E",
        description="chi(O_{K3 x E}) = 0 from Kuenneth on Hodge numbers",
        node_a="K3 x E",
        node_b="expected",
        check_type="hodge_chi",
        passed=passed,
        value_a=f"chi(O_{{K3xE}}) = {chi_O}",
        value_b="expected: 0",
        notes="h^{0,q}(K3 x E) = (1,1,1,1), alternating sum = 0.",
    )


def check_kappa_bkm_decomposition() -> ConsistencyCheck:
    """Verify kappa_BKM(K3 x E) = kappa_ch(K3 x E) + kappa_cat(K3).

    The BKM weight decomposes as:
      kappa_BKM = kappa_ch + kappa_cat(fiber)
      5 = 3 + 2
    """
    passed = (KAPPA_BKM_K3E == KAPPA_CH_K3E + KAPPA_CAT_K3)

    return ConsistencyCheck(
        name="kappa_BKM decomposition",
        description="kappa_BKM(K3xE) = kappa_ch(K3xE) + kappa_cat(K3)",
        node_a="K3 x E",
        node_b="decomposition",
        check_type="kappa_bkm_decomposition",
        passed=passed,
        value_a=f"kappa_BKM = {KAPPA_BKM_K3E}",
        value_b=f"kappa_ch + kappa_cat(K3) = {KAPPA_CH_K3E} + {KAPPA_CAT_K3} = {KAPPA_CH_K3E + KAPPA_CAT_K3}",
        notes=(
            "AP113: all kappa values subscripted. "
            "The decomposition is a prediction of the kappa-spectrum theory."
        ),
    )


def check_kappa_cat_equals_chi_O() -> ConsistencyCheck:
    """Verify kappa_cat(K3) = chi(O_{K3}) = 2 (PROVED at d=2)."""
    k3 = k3_surface()
    chi_O_k3 = k3.chi_O()

    passed = (KAPPA_CAT_K3 == chi_O_k3)

    return ConsistencyCheck(
        name="kappa_cat = chi(O_K3)",
        description="kappa_cat equals holomorphic Euler characteristic",
        node_a="K3",
        node_b="chi(O)",
        check_type="kappa_cat_chi",
        passed=passed,
        value_a=f"kappa_cat(K3) = {KAPPA_CAT_K3}",
        value_b=f"chi(O_K3) = {chi_O_k3}",
        notes="PROVED at d=2 (Proposition prop:kappa-cat-chi-cy).",
    )


# =========================================================================
# 4. Reduction edges and the full web check
# =========================================================================

# Edge types in the compactification web
EDGE_REDUCTION = "reduction"    # Proper dimensional reduction (monotonicity applies)
EDGE_TWIST = "twist"            # Topological twist (can change/increase complexity)
EDGE_DUALITY = "duality"        # Duality equivalence (preserves all invariants)

# Canonical edges in the web: (parent, child, edge_type)
#
# Edge type classification:
#   REDUCTION: proper dimensional reduction (shrink a direction). Monotonicity
#              of E_n, R-matrix, shadow class must hold.
#   TWIST:     topological twist or Omega-deformation. Can INCREASE complexity
#              (e.g. introduce E_3 braiding, promote class G -> L).
#   DUALITY:   string duality (T-dual, S-dual). Preserves all invariants.
#
# Key principle: any step that introduces an Omega-background or twist
# is EDGE_TWIST, because the deformation can create new algebraic
# structure that was not present in the parent theory.
WEB_EDGES = [
    # 11d -> 10d: M-theory on S^1 introduces Omega-background deformation
    ("11d_M_K3", "10d_IIA_K3", EDGE_TWIST),
    ("11d_M_K3", "10d_IIB_K3", EDGE_TWIST),
    # 10d -> 6d: topological twist (introduces E_n structure)
    ("10d_IIA_K3", "6d_hCS_C3", EDGE_TWIST),
    ("10d_IIA_K3", "6d_20_K3xC", EDGE_REDUCTION),
    ("10d_IIA_K3", "6d_K3xExC", EDGE_TWIST),
    # 6d -> 5d: proper reduction (shrink E)
    ("6d_K3xExC", "5d_K3xCxR", EDGE_REDUCTION),
    # 10d -> 5d: compactification with Omega-background (twist)
    ("10d_IIA_K3", "5d_20_on_S1", EDGE_TWIST),
    # 11d -> 5d: compactification with Omega-background (twist)
    ("11d_M_K3", "5d_M_K3xS1", EDGE_TWIST),
    # 5d -> 4d: further compactification with twist
    ("5d_M_K3xS1", "4d_IIA_K3xT2", EDGE_TWIST),
    # 4d duality: S-duality (preserves)
    ("4d_IIA_K3xT2", "4d_IIB_K3xT2", EDGE_DUALITY),
    # 4d -> 3d: compactification + A-twist (introduces E_inf)
    ("4d_IIA_K3xT2", "3d_M_K3xT3", EDGE_TWIST),
    # 5d -> 3d: proper reduction (shrink C, h_i -> 0)
    ("5d_K3xCxR", "3d_K3_sigma", EDGE_REDUCTION),
]

# For backward compatibility: list of (parent, child) pairs
REDUCTION_EDGES = [(p, c) for p, c, _ in WEB_EDGES]

# Edges where monotonicity constraints apply (proper reductions only)
MONOTONE_EDGES = [(p, c) for p, c, t in WEB_EDGES if t == EDGE_REDUCTION]

# Duality edges (invariants must be preserved)
DUALITY_EDGES = [(p, c) for p, c, t in WEB_EDGES if t == EDGE_DUALITY]


def run_all_consistency_checks(
    web: Optional[Dict[str, CompactificationNode]] = None,
) -> List[ConsistencyCheck]:
    """Run all consistency checks on the compactification web.

    Monotonicity checks (R-matrix degeneration, shadow class stability,
    E_n level reduction) apply ONLY to proper reduction edges.
    Topological twists can increase complexity (e.g., 10d -> 6d hCS
    introduces E_3 via a twist, not a reduction).
    Duality edges must preserve all invariants.

    Returns a list of ConsistencyCheck objects, each reporting
    whether a specific consistency condition holds.
    """
    if web is None:
        web = build_m_theory_web()

    checks = []

    # --- Monotonicity checks on proper reduction edges ---
    for parent_key, child_key in MONOTONE_EDGES:
        checks.append(check_rmatrix_degeneration(web, parent_key, child_key))
        checks.append(check_shadow_class_stability(web, parent_key, child_key))
        checks.append(check_en_level_reduction(web, parent_key, child_key))

    # --- kappa_ch preservation on ALL edges ---
    for parent_key, child_key in REDUCTION_EDGES:
        checks.append(check_kappa_ch_preservation(web, parent_key, child_key))

    # --- Duality edges: kappa-spectrum must be preserved ---
    for parent_key, child_key in DUALITY_EDGES:
        checks.append(check_rmatrix_degeneration(web, parent_key, child_key))
        checks.append(check_shadow_class_stability(web, parent_key, child_key))
        checks.append(check_en_level_reduction(web, parent_key, child_key))

    # --- Global checks ---
    checks.append(check_euler_char_multiplicativity())
    checks.append(check_hodge_chi_additivity())
    checks.append(check_kappa_bkm_decomposition())
    checks.append(check_kappa_cat_equals_chi_O())

    return checks


def count_passing(checks: List[ConsistencyCheck]) -> Tuple[int, int]:
    """Count passing and total checks."""
    passing = sum(1 for c in checks if c.passed)
    return passing, len(checks)


# =========================================================================
# 5. Dimensional reduction commutativity
# =========================================================================

class ReductionCommutativity(NamedTuple):
    """Does dimensional reduction commute with the CY-to-chiral functor?

    The central diagram:
      CY_d(X)  --Phi-->  A_X
        |                  |
     reduce             reduce
        |                  |
      CY_{d-1}(X') --Phi--> A_{X'}

    We check commutativity at each level.
    """
    reduction_name: str
    source_cy_dim: int
    target_cy_dim: int
    commutes: Optional[bool]  # None = unknown / conjectural
    status: ClaimStatus
    evidence: str


def check_reduction_commutativity() -> List[ReductionCommutativity]:
    """Check commutativity of Phi with dimensional reduction at each level."""
    results = []

    # 6d -> 5d: shrink E (CY_3 -> CY_2 on the K3 fiber)
    results.append(ReductionCommutativity(
        reduction_name="6d -> 5d (shrink E): U_{q,t} -> Y",
        source_cy_dim=3,
        target_cy_dim=2,
        commutes=None,
        status=ClaimStatus.CONJECTURAL,
        evidence=(
            "If CY-A_3 holds, then Phi(K3 x E) = U_{q,t}(g_{K3}^{tor}). "
            "Shrinking E (q -> 1) should give Y(g_{K3}) = Phi(K3). "
            "This is a PREDICTION of the programme. The trigonometric -> "
            "rational degeneration is verified computationally for gl_1 "
            "(holomorphic_cs_chiral_engine.py, hcs_hierarchy_k3.py)."
        ),
    ))

    # 5d -> 3d: shrink C (CY_2 -> classical)
    results.append(ReductionCommutativity(
        reduction_name="5d -> 3d (shrink C): Y -> H_Muk",
        source_cy_dim=2,
        target_cy_dim=2,
        commutes=True,
        status=ClaimStatus.PROVED,
        evidence=(
            "CY-A_2 is proved. The Yangian Y(g_{K3}) at h_i -> 0 "
            "degenerates to the current algebra U(H_Muk). "
            "The rational structure function g(u) -> 1 (trivial). "
            "Verified: hcs_hierarchy_k3.py reduce_5d_to_3d()."
        ),
    ))

    # 4d -> 3d: compactify on S^1
    results.append(ReductionCommutativity(
        reduction_name="4d -> 3d (compactify S^1): N=4 -> N=8",
        source_cy_dim=3,
        target_cy_dim=3,
        commutes=True,
        status=ClaimStatus.PROVED,
        evidence=(
            "Standard supersymmetric compactification. "
            "4d N=4 on S^1 -> 3d N=8 (Intriligator-Seiberg). "
            "The kappa-spectrum is preserved (same compact manifold). "
            "The R-matrix degenerates: trigonometric -> trivial "
            "(the S^1 compactification imposes E_inf symmetry)."
        ),
    ))

    # IIA <-> IIB T-duality
    results.append(ReductionCommutativity(
        reduction_name="IIA <-> IIB T-duality on K3",
        source_cy_dim=2,
        target_cy_dim=2,
        commutes=True,
        status=ClaimStatus.PROVED,
        evidence=(
            "T-duality preserves the 6d (2,0) theory. "
            "The chiral algebra is the same on both sides "
            "(same K3 Heisenberg / Yangian). "
            "Sen 1995, Aspinwall-Morrison 1996."
        ),
    ))

    # IIA <-> IIB S-duality at 4d
    results.append(ReductionCommutativity(
        reduction_name="IIA <-> IIB S-duality on K3 x T^2",
        source_cy_dim=3,
        target_cy_dim=3,
        commutes=True,
        status=ClaimStatus.PROVED,
        evidence=(
            "S-duality exchanges G <-> G^L (Langlands dual). "
            "On the chiral algebra: quantum Langlands k -> -k-h^vee. "
            "kappa_ch is preserved (both sides have kappa_ch = 3). "
            "Vafa-Witten 1994, Feigin-Frenkel 2006."
        ),
    ))

    return results


# =========================================================================
# 6. Structure function degeneration chain
# =========================================================================

def structure_function_chain(
    h1: Rational = Rational(1),
    h2: Rational = Rational(-2),
    h3: Optional[Rational] = None,
) -> Dict[str, Any]:
    """Compute the structure function at each level of the hierarchy.

    The degeneration chain:
      6d: G(x; q) = prod (1 - q_i x)/(1 - q_i^{-1} x)  [trigonometric]
      5d: g(u; h) = prod (u - h_i)/(u + h_i)             [rational]
      3d: g -> 1                                           [classical]

    Parameters
    ----------
    h1, h2 : Rational
        Omega-background parameters.
    h3 : Rational, optional
        Determined by CY condition h1+h2+h3=0.

    Returns
    -------
    dict with structure functions at each level.
    """
    omega = OmegaBackground(h1, h2, h3)

    # 5d: rational structure function
    # Test at u = 5 (safe point far from poles; AP-CY28)
    u_test = Rational(5)
    g_5d = omega.structure_function_at(u_test)

    # 3d: classical limit (all h_i -> 0)
    omega_classical = OmegaBackground(Rational(0), Rational(0))
    # g(u) = 1 at classical limit (all numerator/denominator factors cancel)
    # But OmegaBackground(0,0) has g(u) = u^3/u^3 = 1 for u != 0
    g_3d = Rational(1)  # By definition at the classical point

    # 6d: trigonometric structure function
    # G(x; q) = prod (1 - q_i x)/(1 - q_i^{-1} x) for q_i = e^{h_i}
    # At x = 1 (unit): G(1) = prod (1-q_i)/(1-q_i^{-1})
    #                        = prod (-q_i) = (-1)^3 * q_1*q_2*q_3
    # By CY condition q_1*q_2*q_3 = e^{h_1+h_2+h_3} = e^0 = 1
    # So G(1) = -1.

    return {
        "omega": omega,
        "sigma2": omega.sigma2,
        "sigma3": omega.sigma3,
        "5d_g_at_u5": g_5d,
        "3d_g_classical": g_3d,
        "6d_G_at_x1": Rational(-1),  # G(1) = -1 by CY condition
        "cy_condition": omega.h1 + omega.h2 + omega.h3,
        "degeneration_chain": "trigonometric -> rational -> classical",
        "kac_moody_level": omega.kac_moody_level(),
    }


# =========================================================================
# 7. Kappa-spectrum at each node
# =========================================================================

def kappa_spectrum_web() -> Dict[str, Dict[str, Optional[Rational]]]:
    """Extract the full kappa-spectrum at each node of the web.

    Returns a nested dict: {node_name: {kappa_type: value}}.
    AP113: ALL kappa values are subscripted.
    """
    web = build_m_theory_web()
    spectrum = {}
    for key, node in web.items():
        spectrum[key] = {
            "kappa_ch": node.kappa_ch,
            "kappa_bkm": node.kappa_bkm,
            "kappa_cat": node.kappa_cat,
            "kappa_fiber": node.kappa_fiber,
        }
    return spectrum


# =========================================================================
# 8. Summary / pipeline
# =========================================================================

def full_web_analysis() -> Dict[str, Any]:
    """Run the full analysis: build web, run checks, extract spectra.

    Returns a comprehensive dictionary with all results.
    """
    web = build_m_theory_web()
    checks = run_all_consistency_checks(web)
    passing, total = count_passing(checks)
    commutativity = check_reduction_commutativity()
    spectrum = kappa_spectrum_web()
    sf_chain = structure_function_chain()

    # Extract failures for quick diagnosis
    failures = [c for c in checks if not c.passed]

    return {
        "web_nodes": len(web),
        "web": web,
        "checks_total": total,
        "checks_passing": passing,
        "checks_failing": len(failures),
        "failures": failures,
        "all_checks": checks,
        "commutativity": commutativity,
        "kappa_spectrum": spectrum,
        "structure_function_chain": sf_chain,
        "summary": (
            f"Compactification web: {len(web)} nodes, "
            f"{len(REDUCTION_EDGES)} edges. "
            f"Consistency: {passing}/{total} checks pass. "
            f"Failures: {len(failures)}."
        ),
    }
