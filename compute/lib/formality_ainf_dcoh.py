r"""A_infinity formality of D^b(Coh(X)) for Calabi-Yau manifolds.

MATHEMATICAL CONTENT
====================

CENTRAL QUESTION: which formality and obstruction claims are certified for
D^b(Coh(X)) or D^coh(X), and which are only de Rham, spectral-sequence, or
model-dependent evidence?

The corrected obstruction theorem separates four assertions:

  (1) DGMS de Rham formality of the commutative cdga of X;
  (2) Hodge-to-de Rham degeneration for a smooth proper dg category;
  (3) A_infinity formality of a specified dg/A_infinity category;
  (4) vanishing of a derived S^3-framing obstruction through a named
      complex, degree, filtration, and comparison map.

Only (3) makes m_k = 0 for k >= 3.  Only (4), or a formal input with
m_3 = 0, can close the m_3--B^{(2)} obstruction.  Raw
[m_3, B^{(2)}_term] can be nonzero.

THE ANSWER: It depends on the geometry.  There are THREE notions of
formality that must be carefully distinguished:

==========================================================================
FORMALITY HIERARCHY (three levels)
==========================================================================

Level 1: DE RHAM FORMALITY (DGMS 1975)
  Statement: For compact Kahler X, the de Rham cdga (Omega^*(X), d, wedge)
  is formal: there exists a zig-zag of quasi-isomorphisms to (H^*(X), 0, cup).
  Scope: The COMMUTATIVE de Rham algebra of the MANIFOLD X.
  Applies to: All compact Kahler manifolds, including all smooth projective CY.
  Does NOT imply: formality of D^b(Coh(X)) as an A_infinity category.

Level 2: HODGE-TO-DE-RHAM DEGENERATION (Kaledin 2008)
  Statement: For a smooth proper dg category C over char 0, the
  Hochschild-to-cyclic spectral sequence degenerates at E_2.
  Scope: The CYCLIC HOMOLOGY spectral sequence of the dg CATEGORY.
  Applies to: All smooth proper dg categories, including D^b(Coh(X)) for
  smooth projective X.
  Does NOT imply: A_infinity formality of the category.
  What it implies: The Hodge filtration on periodic cyclic homology splits,
  giving HP_n(C) = prod_p HH_{n+2p}(C).  This is spectral sequence
  degeneration, not formality of the algebra structure.

Level 3: A_INFINITY FORMALITY of D^b(Coh(X))
  Statement: The minimal A_infinity model on Ext^*(E, E) (for a generator
  or exceptional collection E) has m_k = 0 for all k >= 3.
  Scope: The MULTIPLICATIVE A_infinity structure on the Ext algebra.
  This is the strongest condition: it means the derived category, as an
  A_infinity category, is quasi-isomorphic to its cohomology with only
  the cup product (a dg category with zero differential).

==========================================================================
WHEN DOES LEVEL 3 HOLD?
==========================================================================

THEOREM (Kaledin 2008, arXiv:0708.1444, Thm 1.2):
  Let X be a smooth proper variety over C.  If X admits a TILTING GENERATOR
  T (an object T in D^b(Coh(X)) such that Hom^i(T, T) = 0 for i != 0
  and T generates D^b(Coh(X))), then D^b(Coh(X)) is formal.

  More precisely: the dg algebra RHom(T, T) is formal (quasi-isomorphic
  to its cohomology as a dg algebra, hence the transferred A_infinity
  structure has m_k = 0 for k >= 3).

TILTING GENERATOR EXISTENCE:
  - Projective spaces P^n: YES (Beilinson 1978). T = O + O(1) + ... + O(n).
  - Toric varieties: YES (Kawamata 2006, conditional; proved by
    Efimov-Lunts-Orlov for smooth toric).
  - Smooth quadrics: YES.
  - Resolved conifold O(-1)+O(-1) -> P^1: YES. Tilting from the
    exceptional collection.  Hence formal.
  - Local P^2 = Tot(O(-3) -> P^2): The exceptional collection {O, O(1), O(2)}
    does NOT form a tilting generator in the CY sense.  The Ginzburg
    dg algebra model has nonzero m_3 from the potential.  NON-FORMAL.
  - Compact CY3 (quintic, bicubic, etc.): NO tilting generator in the
    Kaledin sense (because Hom^i(T, T) != 0 for i = 1, 2, 3 by Serre duality).
    For a CY3, Ext^3(E, E) = Ext^0(E, E)^* != 0, so NO single object
    has concentrated Ext.

CONCLUSION FOR COMPACT CY3:
  Kaledin's tilting formality theorem does NOT apply.  The question of
  A_infinity formality must be answered by other means.

==========================================================================
THE QUINTIC: FORMAL OR NOT?
==========================================================================

STATUS: This engine does not prove A_infinity formality or non-formality
of D^b(Coh(Q)) for the smooth quintic Q in P^4.

EVIDENCE:

(E1) Bogomolov-Tian-Todorov (BTT): The deformation space of Q is
     UNOBSTRUCTED.  HH^2(D^b(Coh(Q))) -> formal deformations is
     surjective, with no higher obstructions.  This means the Kodaira-
     Spencer dgla (controlling deformations of Q) is formal.
     But: BTT gives formality of the DEFORMATION PROBLEM, not of the
     full A_infinity category.

(E2) Kontsevich's argument: For a smooth projective variety X with
     ample (or anti-ample) canonical bundle, the Ext algebra is formal.
     For CY: K_X = O_X is neither ample nor anti-ample.  So Kontsevich's
     criterion does NOT apply directly.

(E3) Lunts-Orlov uniqueness: The dg enhancement of D^b(Coh(X)) is
     UNIQUE up to quasi-equivalence.  This means there is a well-defined
     answer: either the category is formal or it is not.

(E4) The Hochschild cohomology approach: For the quintic,
     HH^*(Q) = H^*(Q, wedge^* T_Q) has:
       HH^0 = H^0(O_Q) = C  (h^{0,0} = 1)
       HH^1 = H^1(T_Q) + H^0(Omega^1_Q) = C^{101} + 0 = C^{101}
       HH^2 = H^2(wedge^2 T_Q) + H^1(O_Q) + H^0(T_Q)
             = H^2(O_Q) + 0 + 0 = C  (using CY: wedge^3 T = O, so wedge^2 T = Omega^1)
             ... actually HH^2 = 1 (from H^0(wedge^2 T_Q) = H^0(Omega^1_Q) = 0 and
             H^1(T_Q) = C^{101} (already in HH^1), and H^2(O_Q) = 0)
       HH^3 = H^3(O_Q) = C  (h^{3,0} = 1)

     The key: ALL Massey products <alpha, beta, gamma> for alpha, beta, gamma
     in HH^1 = Ext^1(O_Q, O_Q) would need to be computed.

(E5) DGMS applied to Q: The quintic IS compact Kahler, so the de Rham
     algebra H^*(Q, C) is formal.  The Massey products on COHOMOLOGY vanish.
     But this is Level 1 formality, not Level 3.

(E6) The Gepner model: At the Gepner point in the quintic moduli space
     (the orbifold point z = infinity of the Picard-Fuchs equation),
     the quintic is described by the Landau-Ginzburg model
     W = x_0^5 + x_1^5 + x_2^5 + x_3^5 + x_4^5.
     The matrix factorization category MF(W) IS the CY3 category at
     this point (Orlov's equivalence D^b(Coh(Q)) = D^b(MF(W))/Perf).
     The A_infinity structure on MF(W) has m_3 coming from the potential.

     HOWEVER: the Gepner model describes a DIFFERENT point in moduli space
     from the large volume limit.  The A_infinity structure on the Ext
     algebra is NOT constant over the moduli space (it depends on the
     complex structure through the choice of harmonic representatives).

(E7) THE SAFE RESOLUTION: For the quintic at a fixed complex structure:
     - The de Rham algebra H^*(Q, C) is formal (DGMS).
     - The Ext algebra Ext^*(O_Q, O_Q) is trivially formal: it is C in
       degree 0 only (since Q is smooth projective with Pic(Q) = Z*H,
       we have Ext^i(O, O) = H^i(O_Q) = {C for i=0,3; 0 for i=1,2}).
     - For the FULL generator E = bigoplus O(d) (Orlov's theorem):
       the Ext algebra is much larger, and formality depends on whether
       the A_infinity operations are trivializable.

     The correct statement distinguishes:
     (a) Formality of a SINGLE endomorphism algebra Ext^*(O, O): TRIVIALLY
         formal (concentrated in degrees 0 and 3 only, all products zero
         except the cup product, which is determined by the CY pairing).
     (b) Formality of the FULL A_infinity CATEGORY D^b(Coh(Q)): this
         requires all multi-object A_infinity operations to vanish.
         These involve Ext^*(O(a), O(b)) for different a, b, and the
         transferred m_k on the total complex.

STATUS RECORD (this engine):
  For a smooth projective CY_d manifold X:
  (i)   d = 1 (elliptic curve): Polishchuk showed the A_infinity category
        is NOT formal (m_3 != 0 for products of line bundles, determined
        by theta functions).
  (ii)  d = 2 (K3): DGMS proves de Rham formality of the K3 surface, and
        Kaledin proves non-commutative HdR degeneration for the smooth
        proper dg category.  This engine does not promote either statement
        to A_infinity formality of D^b(Coh(K3)).
  (iii) d = 3 (quintic, bicubic, K3 x E): no universal compact CY3 closure
        is certified here.  Yukawa couplings and Landau--Ginzburg models are
        evidence for specific comparison problems, not a replacement for an
        explicit A_infinity model and comparison map.

        CRITICAL DISTINCTION: The m_3 lives on the KODAIRA-SPENCER dgla
        HH^*(D^b(Coh(Q)))[1], NOT on the Ext algebra of a single sheaf.
        For a single sheaf O_Q: Ext^*(O_Q, O_Q) is formal (trivially).
        For the CATEGORY: the m_3 maps
          Ext^1(O(a), O(b)) x Ext^1(O(b), O(c)) x Ext^1(O(c), O(d)) -> Ext^1(O(a), O(d))
        can be nonzero.

IMPLICATION FOR THE PROGRAMME:
  If D^b(Coh(Q)) were A_infinity-formal (m_3 = 0), then:
    - CY-A_3 holds TRIVIALLY: the chiral algebra is determined entirely
      by the cup product structure, with no higher corrections.
    - The [m_3, B^{(2)}] issue is MOOT.
    - The shadow tower has depth 0 (class G), the simplest case.

  When a nonzero m_3 is present in a witnessed model:
    - raw [m_3, B^{(2)}_term] may be nonzero;
    - the corrected Costello TCFT identity concerns B^{(2)}_TCFT with its
      correction datum and the total differential b = sum_k b_k;
    - derived vanishing requires the reduced Hochschild E_1-cochain
      HH^{-2} filtration theorem plus a comparison map into that complex.

==========================================================================
K3 x E: PRODUCT FORMALITY
==========================================================================

K3: de Rham formal by DGMS; A_infinity categorical formality is not
   certified by this engine.
E: formal as a MANIFOLD (DGMS + abelian variety), but the A_infinity
   CATEGORY D^b(Coh(E)) is NOT formal (Polishchuk).

K3 x E AS A CY3: the product category requires an explicit A_infinity
  product model.  Kunneth formality for de Rham cdgas is not such a model.

For the relative K3-fiber construction, formal fiber statements are valid
only after a formal A_infinity model or an equivalent strictifying datum is
supplied.  DGMS for the K3 manifold is not that datum.

For K3 x E as a CY3: the Kodaira-Spencer dgla has HH^1 = H^1(T_{K3xE})
  = H^1(T_{K3}) + H^0(T_{K3}) x H^1(O_E) + H^0(O_{K3}) x H^1(T_E)
  = 0 + 20*1 + 1*1 = 21.
The Yukawa coupling (m_3 on HH^1) is determined by the triple intersection
on H^2(K3) x H^1(E), which is nonzero in the B-model deformation problem.
This does not by itself prove non-formality of D^b(Coh(K3 x E)).

No equality between relative and absolute character-level constructions is
recorded here without that strictifying datum and the relevant comparison
map.

CONVENTIONS
===========
  - Cohomological grading: |d| = +1
  - CY dimension d: complex dimension, not real (AP-CY1)
  - kappa subscripted: kappa_ch, kappa_cat, kappa_BKM, kappa_fiber (AP113)
  - Exact arithmetic via fractions.Fraction
  - AP-CY6: any result conditional on CY-A_3 marked explicitly
  - AP-CY11: conditional propagation tracked
  - AP-CY17: MF(W) is CY_{n-2} for W: A^n -> A^1

REFERENCES
==========
  Deligne-Griffiths-Morgan-Sullivan, Inventiones 29 (1975): de Rham formality
  Kaledin, arXiv:0708.1444 (2007): non-commutative HdR degeneration
  Kaledin, arXiv:math/0308135 (2003): formality of Ext algebras
  Polishchuk, arXiv:math/0205149 (2002): A_infinity structure on elliptic curves
  Lunts-Orlov, JAMS 23 (2010): uniqueness of dg enhancements
  Kontsevich, ICM 1994: HMS conjecture
  Sheridan, arXiv:1507.03085 (2015): HMS for the quintic
  Costello, arXiv:math/0412149 (2004): TCFT and CY categories
  Bogomolov-Tian-Todorov: unobstructedness of CY deformations
  Orlov, arXiv:math/0302304 (2003): D^b(Coh) vs MF equivalences
  Lorgat Vol III: cy_to_chiral.tex, cyclic_ainf.tex, k3_times_e.tex
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Sequence, Tuple

F = Fraction


# =========================================================================
# 0. FORMALITY HIERARCHY: THREE LEVELS
# =========================================================================

@dataclass(frozen=True)
class FormalityLevel:
    r"""One of the three levels of formality for a CY manifold.

    Level 1: de Rham formality (DGMS, compact Kahler)
    Level 2: HdR degeneration (Kaledin, smooth proper dg cat)
    Level 3: A_infinity formality (m_k = 0 for k >= 3)
    """
    level: int
    name: str
    scope: str
    applies_to_manifold: bool
    applies_to_category: bool
    implies_m3_zero: bool


DE_RHAM_FORMALITY = FormalityLevel(
    level=1,
    name="de Rham formality (DGMS 1975)",
    scope="Commutative de Rham cdga of the manifold X",
    applies_to_manifold=True,
    applies_to_category=False,
    implies_m3_zero=False,
)

HDR_DEGENERATION = FormalityLevel(
    level=2,
    name="Hodge-to-de Rham degeneration (Kaledin 2008)",
    scope="HH-to-HC spectral sequence of smooth proper dg cat",
    applies_to_manifold=False,
    applies_to_category=True,
    implies_m3_zero=False,
)

AINF_FORMALITY = FormalityLevel(
    level=3,
    name="A_infinity formality (m_k = 0, k >= 3)",
    scope="Full A_infinity category structure",
    applies_to_manifold=False,
    applies_to_category=True,
    implies_m3_zero=True,
)

FORMALITY_HIERARCHY = [DE_RHAM_FORMALITY, HDR_DEGENERATION, AINF_FORMALITY]


def level_implication_chain() -> List[Tuple[int, int, bool]]:
    r"""Implication relationships between formality levels.

    Level 3 => Level 2 => Level 1?  NO.  The levels are mostly independent:
    - Level 3 (A_inf formal) does NOT imply Level 1 (de Rham formal):
      a formal dg category can sit on a non-Kahler manifold.
    - Level 1 (de Rham formal) does NOT imply Level 3 (A_inf formal):
      the elliptic curve is de Rham formal (compact Kahler) but
      D^b(Coh(E)) is not A_inf formal (Polishchuk).
    - Level 2 (HdR degeneration) is UNIVERSAL for smooth proper dg cats
      (Kaledin), so it does not distinguish geometries.

    Returns list of (from_level, to_level, implies).
    """
    return [
        (3, 2, True),   # A_inf formal => HdR degenerates (trivially)
        (3, 1, False),  # A_inf formal does NOT imply de Rham formal
        (2, 3, False),  # HdR degeneration does NOT imply A_inf formal
        (2, 1, False),  # HdR degeneration does NOT imply de Rham formal
        (1, 3, False),  # de Rham formal does NOT imply A_inf formal
        (1, 2, False),  # de Rham formal does NOT imply HdR degeneration
    ]


# =========================================================================
# 1. HODGE DATA FOR CY MANIFOLDS
# =========================================================================

@dataclass(frozen=True)
class CYHodgeData:
    r"""Hodge data for a CY_d manifold.

    For a smooth projective CY_d manifold X:
      h^{p,q} = dim H^q(X, Omega^p_X)
      chi(O_X) = sum_p (-1)^p h^{0,p}  (holomorphic Euler characteristic)

    The CY condition omega_X = O_X gives h^{d,0} = 1 and h^{p,0} = binom(d,p)
    ... no, that is for tori.  For CY: h^{d,0} = 1, and the rest depends on X.
    """
    name: str
    cy_dim: int
    hodge_diamond: Dict[Tuple[int, int], int]
    is_compact: bool = True
    is_projective: bool = True

    def h(self, p: int, q: int) -> int:
        """Hodge number h^{p,q}."""
        return self.hodge_diamond.get((p, q), 0)

    def chi_O(self) -> int:
        """Holomorphic Euler characteristic chi(O_X) = sum (-1)^q h^{0,q}."""
        return sum(
            (-1)**q * self.h(0, q) for q in range(self.cy_dim + 1)
        )

    def euler_char(self) -> int:
        """Topological Euler characteristic chi(X) = sum (-1)^{p+q} h^{p,q}."""
        return sum(
            (-1)**(p + q) * v
            for (p, q), v in self.hodge_diamond.items()
        )

    def hh_dim(self) -> int:
        """Total dimension of Hochschild cohomology HH^*(X).

        By HKR: HH^n(X) = bigoplus_{p+q=n} H^q(X, wedge^p T_X).
        For CY: wedge^d T_X = O_X (triviality of canonical), so
        H^q(wedge^p T_X) = H^q(Omega^{d-p}_X) = h^{d-p,q}.
        Total dim HH^* = sum_{p,q} h^{d-p,q} = sum_{p,q} h^{p,q} = chi_top (unsigned).
        """
        return sum(abs(v) for v in self.hodge_diamond.values())

    def ext_O_concentrated(self) -> bool:
        """Is Ext^*(O_X, O_X) concentrated in degrees 0 and d?

        For CY_d: Ext^i(O, O) = H^i(O_X).  For a 'strict' CY
        (h^{0,i} = 0 for 0 < i < d): YES, concentrated in {0, d}.
        """
        for i in range(1, self.cy_dim):
            if self.h(0, i) != 0:
                return False
        return True

    def ext_O_dims(self) -> List[int]:
        """Dimensions of Ext^i(O_X, O_X) = H^i(O_X) for i = 0, ..., d."""
        return [self.h(0, i) for i in range(self.cy_dim + 1)]

    def kodaira_spencer_dim(self) -> int:
        """Dimension of the Kodaira-Spencer space H^1(T_X).

        For CY_d: H^1(T_X) = H^1(Omega^{d-1}_X) = h^{d-1,1}.
        """
        return self.h(self.cy_dim - 1, 1)


# =========================================================================
# 2. STANDARD CY MANIFOLD DATA
# =========================================================================

def elliptic_curve() -> CYHodgeData:
    """CY_1: elliptic curve E."""
    return CYHodgeData(
        name="elliptic curve",
        cy_dim=1,
        hodge_diamond={(0, 0): 1, (1, 0): 1, (0, 1): 1, (1, 1): 1},
    )


def k3_surface() -> CYHodgeData:
    """CY_2: K3 surface S."""
    return CYHodgeData(
        name="K3 surface",
        cy_dim=2,
        hodge_diamond={
            (0, 0): 1, (1, 0): 0, (2, 0): 1,
            (0, 1): 0, (1, 1): 20, (2, 1): 0,
            (0, 2): 1, (1, 2): 0, (2, 2): 1,
        },
    )


def abelian_surface() -> CYHodgeData:
    """CY_2: abelian surface A = E x E."""
    return CYHodgeData(
        name="abelian surface",
        cy_dim=2,
        hodge_diamond={
            (0, 0): 1, (1, 0): 2, (2, 0): 1,
            (0, 1): 2, (1, 1): 4, (2, 1): 2,
            (0, 2): 1, (1, 2): 2, (2, 2): 1,
        },
    )


def quintic_threefold() -> CYHodgeData:
    """CY_3: smooth quintic Q in P^4."""
    return CYHodgeData(
        name="quintic threefold",
        cy_dim=3,
        hodge_diamond={
            (0, 0): 1, (1, 0): 0, (2, 0): 0, (3, 0): 1,
            (0, 1): 0, (1, 1): 1, (2, 1): 101, (3, 1): 0,
            (0, 2): 0, (1, 2): 101, (2, 2): 1, (3, 2): 0,
            (0, 3): 1, (1, 3): 0, (2, 3): 0, (3, 3): 1,
        },
    )


def k3_times_e() -> CYHodgeData:
    r"""CY_3: K3 x E (product).

    Hodge diamond of K3 x E from Kunneth:
      h^{p,q}(K3 x E) = sum_{a+c=p, b+d=q} h^{a,b}(K3) * h^{c,d}(E)
    """
    k3 = k3_surface()
    e = elliptic_curve()
    diamond: Dict[Tuple[int, int], int] = {}
    for (a, b), va in k3.hodge_diamond.items():
        for (c, d), vc in e.hodge_diamond.items():
            key = (a + c, b + d)
            diamond[key] = diamond.get(key, 0) + va * vc
    return CYHodgeData(
        name="K3 x E",
        cy_dim=3,
        hodge_diamond=diamond,
    )


def bicubic_threefold() -> CYHodgeData:
    """CY_3: complete intersection of two cubics in P^5."""
    return CYHodgeData(
        name="bicubic P^5[3,3]",
        cy_dim=3,
        hodge_diamond={
            (0, 0): 1, (1, 0): 0, (2, 0): 0, (3, 0): 1,
            (0, 1): 0, (1, 1): 1, (2, 1): 73, (3, 1): 0,
            (0, 2): 0, (1, 2): 73, (2, 2): 1, (3, 2): 0,
            (0, 3): 1, (1, 3): 0, (2, 3): 0, (3, 3): 1,
        },
    )


def conifold_resolved() -> CYHodgeData:
    """CY_3: resolved conifold Tot(O(-1)+O(-1) -> P^1).

    Non-compact, but we record the compact cohomology for the
    generator Ext algebra.  Not a compact CY3 manifold.
    """
    return CYHodgeData(
        name="resolved conifold",
        cy_dim=3,
        hodge_diamond={
            (0, 0): 1, (1, 0): 0, (2, 0): 0, (3, 0): 0,
            (0, 1): 0, (1, 1): 1, (2, 1): 0, (3, 1): 0,
            (0, 2): 0, (1, 2): 0, (2, 2): 1, (3, 2): 0,
            (0, 3): 0, (1, 3): 0, (2, 3): 0, (3, 3): 1,
        },
        is_compact=False,
    )


# =========================================================================
# 3. FORMALITY ANALYSIS FOR EACH GEOMETRY
# =========================================================================

@dataclass(frozen=True)
class FormalityVerdict:
    r"""Complete formality analysis for a CY manifold.

    Records the three levels of formality and the overall verdict for
    the A_infinity category D^b(Coh(X)).
    """
    geometry: str
    cy_dim: int
    # Level 1: de Rham
    de_rham_formal: bool
    de_rham_reason: str
    # Level 2: HdR degeneration
    hdr_degeneration: bool
    hdr_reason: str
    # Level 3: A_infinity formality of D^b.  None means not certified here.
    ainf_formal: Optional[bool]
    ainf_reason: str
    ainf_status: str
    # Massey product status
    has_nonzero_massey_derham: bool  # Massey products on H^*(X, C)
    has_nonzero_m3_category: Optional[bool]  # None means not certified here
    # Shadow class consequence
    shadow_class: str  # G, L, C, M, or unclassified
    # Whether TCFT resolution is needed
    tcft_needed: Optional[bool]
    obstruction_status: str
    # References
    references: List[str] = field(default_factory=list)


def analyze_formality(X: CYHodgeData) -> FormalityVerdict:
    r"""Complete formality analysis for a CY manifold X.

    Determines all three levels of formality and the consequences
    for the CY-to-chiral programme.
    """
    if X.name == "elliptic curve":
        return FormalityVerdict(
            geometry="elliptic curve E",
            cy_dim=1,
            de_rham_formal=True,
            de_rham_reason="Compact Kahler (DGMS 1975)",
            hdr_degeneration=True,
            hdr_reason="Smooth proper dg cat (Kaledin 2008)",
            ainf_formal=False,
            ainf_reason=(
                "Polishchuk (2002): D^b(Coh(E)) has m_3 != 0 from "
                "theta-function A_infinity operations on products of "
                "line bundles. The elliptic curve is de Rham formal "
                "but the A_infinity CATEGORY is not formal."
            ),
            ainf_status="proved_nonformal",
            has_nonzero_massey_derham=False,
            has_nonzero_m3_category=True,
            shadow_class="L",
            tcft_needed=False,  # d=1, no S^3-framing issue
            obstruction_status="not_applicable_to_S3_framing",
            references=[
                "Polishchuk arXiv:math/0205149",
                "DGMS Inventiones 29 (1975)",
            ],
        )

    elif X.name == "K3 surface":
        return FormalityVerdict(
            geometry="K3 surface S",
            cy_dim=2,
            de_rham_formal=True,
            de_rham_reason="Compact Kahler (DGMS 1975)",
            hdr_degeneration=True,
            hdr_reason="Smooth proper dg cat (Kaledin 2008)",
            ainf_formal=None,
            ainf_reason=(
                "K3 is compact Kahler, so DGMS proves de Rham formality "
                "of H^*(K3). Kaledin gives HH-to-HC degeneration for the "
                "smooth proper dg category. Neither statement is an "
                "A_infinity formality theorem for D^b(Coh(K3)); this "
                "engine therefore records the categorical status as not "
                "certified."
            ),
            ainf_status="not_certified_by_DGMS_or_Kaledin",
            has_nonzero_massey_derham=False,
            has_nonzero_m3_category=None,
            shadow_class="unclassified",
            tcft_needed=None,
            obstruction_status="not_certified",
            references=[
                "DGMS Inventiones 29 (1975)",
                "Kaledin arXiv:0708.1444",
            ],
        )

    elif X.name == "abelian surface":
        return FormalityVerdict(
            geometry="abelian surface A",
            cy_dim=2,
            de_rham_formal=True,
            de_rham_reason="Abelian variety: formal (Kahler + group structure)",
            hdr_degeneration=True,
            hdr_reason="Smooth proper dg cat (Kaledin 2008)",
            ainf_formal=None,
            ainf_reason=(
                "Abelian surface is de Rham formal as a compact Kahler "
                "abelian variety. Polishchuk proves non-formality for "
                "elliptic curve categories, but this engine does not use "
                "that result as an automatic product-formality theorem for "
                "D^b(Coh(A))."
            ),
            ainf_status="not_certified_by_product_DGMS",
            has_nonzero_massey_derham=False,
            has_nonzero_m3_category=None,
            shadow_class="unclassified",
            tcft_needed=None,
            obstruction_status="not_certified",
            references=[
                "Polishchuk arXiv:math/0205149",
                "DGMS Inventiones 29 (1975)",
            ],
        )

    elif X.name == "quintic threefold":
        return FormalityVerdict(
            geometry="quintic threefold Q in P^4",
            cy_dim=3,
            de_rham_formal=True,
            de_rham_reason="Compact Kahler (DGMS 1975): all Massey products on H^*(Q, C) vanish",
            hdr_degeneration=True,
            hdr_reason="Smooth proper dg cat (Kaledin 2008): HH-to-HC spectral seq degenerates",
            ainf_formal=None,
            ainf_reason=(
                "D^b(Coh(Q)) is not certified here as A_infinity formal or "
                "non-formal. DGMS, BTT, Kaledin K1, and the Yukawa coupling "
                "do not by themselves supply a strict A_infinity model and "
                "comparison map for the full category. Ext^*(O_Q,O_Q) alone "
                "is trivially formal, but this does not decide the full "
                "multi-object category."
            ),
            ainf_status="not_certified_for_full_category",
            has_nonzero_massey_derham=False,
            has_nonzero_m3_category=None,
            shadow_class="unclassified",
            tcft_needed=None,
            obstruction_status="requires_corrected_TCFT_or_HH_minus_2_hypothesis",
            references=[
                "DGMS Inventiones 29 (1975)",
                "Kaledin arXiv:0708.1444",
                "Sheridan arXiv:1507.03085 (HMS for quintic)",
                "Costello arXiv:math/0412149 (TCFT)",
                "Candelas-de la Ossa-Green-Parkes (1991)",
            ],
        )

    elif X.name == "K3 x E":
        return FormalityVerdict(
            geometry="K3 x E",
            cy_dim=3,
            de_rham_formal=True,
            de_rham_reason=(
                "Product of compact Kahler manifolds: K3 formal (DGMS), "
                "E formal (abelian variety). Product is formal (Kunneth "
                "for formal cdgas)."
            ),
            hdr_degeneration=True,
            hdr_reason="Smooth proper dg cat (Kaledin 2008)",
            ainf_formal=None,
            ainf_reason=(
                "D^b(Coh(K3 x E)) is not certified here as A_infinity "
                "formal or non-formal. The E factor supplies a proven "
                "non-formal elliptic curve category, and the B-model "
                "Yukawa expression is nonzero, but turning these facts into "
                "an absolute product-category verdict requires an explicit "
                "A_infinity model and comparison map. The K3 fiber may be "
                "used as a formal input only after a separate formal model "
                "or strictifying datum is supplied."
            ),
            ainf_status="not_certified_for_product_category",
            has_nonzero_massey_derham=False,
            has_nonzero_m3_category=None,
            shadow_class="unclassified",
            tcft_needed=None,
            obstruction_status="requires_corrected_TCFT_or_HH_minus_2_hypothesis",
            references=[
                "DGMS Inventiones 29 (1975)",
                "Polishchuk arXiv:math/0205149",
                "Costello arXiv:math/0412149",
            ],
        )

    elif X.name == "bicubic P^5[3,3]":
        return FormalityVerdict(
            geometry="bicubic P^5[3,3]",
            cy_dim=3,
            de_rham_formal=True,
            de_rham_reason="Compact Kahler (DGMS 1975)",
            hdr_degeneration=True,
            hdr_reason="Smooth proper dg cat (Kaledin 2008)",
            ainf_formal=None,
            ainf_reason=(
                "Complete-intersection CY3. DGMS and Kaledin K1 apply, "
                "and Yukawa data are relevant to the deformation problem, "
                "but this engine does not certify A_infinity formality or "
                "non-formality of the full category."
            ),
            ainf_status="not_certified_for_full_category",
            has_nonzero_massey_derham=False,
            has_nonzero_m3_category=None,
            shadow_class="unclassified",
            tcft_needed=None,
            obstruction_status="requires_corrected_TCFT_or_HH_minus_2_hypothesis",
            references=[
                "DGMS Inventiones 29 (1975)",
                "Kaledin arXiv:0708.1444",
            ],
        )

    elif X.name == "resolved conifold":
        return FormalityVerdict(
            geometry="resolved conifold",
            cy_dim=3,
            de_rham_formal=True,
            de_rham_reason="Toric CY3: formal (toric varieties are rational)",
            hdr_degeneration=True,
            hdr_reason="Smooth dg cat (Kaledin)",
            ainf_formal=True,
            ainf_reason=(
                "The resolved conifold is derived equivalent to the "
                "Klebanov-Witten quiver with quadratic potential. "
                "The Ext algebra of the tilting generator has m_k = 0 "
                "for k >= 3 (intrinsic formality from quadratic relations). "
                "Equivalently: the conifold is a toric CY3 with "
                "unobstructed deformations AND concentrated Ext."
            ),
            ainf_status="certified_formal_tilting_quadratic",
            has_nonzero_massey_derham=False,
            has_nonzero_m3_category=False,
            shadow_class="G",
            tcft_needed=False,
            obstruction_status="formal_input_m3_zero",
            references=[
                "Kaledin arXiv:math/0308135",
                "Bridgeland (2002) flop equivalences",
            ],
        )

    else:
        raise ValueError(f"Unknown geometry: {X.name}")


# =========================================================================
# 4. THE KALEDIN THEOREM: WHAT IT DOES AND DOES NOT SAY
# =========================================================================

@dataclass(frozen=True)
class KaledinAnalysis:
    r"""Analysis of Kaledin's theorem and its applicability.

    Kaledin proved TWO theorems:

    (K1) arXiv:0708.1444 (2007), Thm 1.2:
         Non-commutative Hodge-to-de Rham degeneration.
         For smooth proper dg categories over char 0, the HH-to-HC
         spectral sequence degenerates at E_2.
         This is UNIVERSAL: applies to ALL smooth proper dg categories.
         It does NOT imply formality.

    (K2) arXiv:math/0308135 (2003), Sec 5:
         Formality of Ext algebras for varieties with tilting generators.
         If X admits a tilting generator T with Hom^i(T,T) = 0 for i != 0,
         then RHom(T,T) is formal as a dg algebra.
         This requires a TILTING GENERATOR, which compact CY3 do not have.
    """
    geometry: str
    k1_applies: bool
    k1_conclusion: str
    k2_applies: bool
    k2_reason: str
    has_tilting_generator: bool
    formality_from_kaledin: bool


def kaledin_analysis(X: CYHodgeData) -> KaledinAnalysis:
    """Analyze applicability of Kaledin's theorems to X."""
    # K1 always applies to smooth proper
    k1 = X.is_compact and X.is_projective

    # K2 requires tilting generator: Hom^i(T,T) = 0 for i != 0
    # For compact CY_d with d >= 2: Ext^d(E,E) = Ext^0(E,E)^* != 0 by Serre
    # So no tilting generator exists in the compact CY sense.
    has_tilting = False
    k2_reason = ""

    if X.name == "resolved conifold":
        # Non-compact: can have tilting
        has_tilting = True
        k2_reason = (
            "Resolved conifold has exceptional collection {O, O(1)} "
            "on P^1 base, giving a tilting generator with concentrated Ext."
        )
    elif X.name == "K3 surface":
        # K3 does NOT have a tilting generator (Ext^2(E,E) != 0 by Serre duality)
        has_tilting = False
        k2_reason = (
            "K3 has no tilting generator: Serre duality gives "
            "Ext^2(E,E) = Ext^0(E,E)^* != 0 for any generator E. "
            "DGMS gives de Rham formality of the manifold, not an "
            "A_infinity formality theorem for D^b(Coh(K3))."
        )
    elif X.cy_dim == 3 and X.is_compact:
        has_tilting = False
        k2_reason = (
            f"Compact CY3 ({X.name}): no tilting generator. "
            "Serre duality gives Ext^3(E,E) = Ext^0(E,E)^* != 0 "
            "for any generator E. Kaledin K2 does not apply."
        )
    elif X.name == "elliptic curve":
        has_tilting = False
        k2_reason = (
            "Elliptic curve: Ext^1(O,O) = H^1(O) = C != 0 and "
            "Ext^0(O,O) = C. No tilting generator."
        )
    else:
        k2_reason = f"Analysis for {X.name}: case-specific."

    return KaledinAnalysis(
        geometry=X.name,
        k1_applies=k1,
        k1_conclusion=(
            "HH-to-HC spectral sequence degenerates at E_2"
            if k1 else "K1 requires smooth proper; not applicable"
        ),
        k2_applies=has_tilting,
        k2_reason=k2_reason,
        has_tilting_generator=has_tilting,
        formality_from_kaledin=has_tilting,
    )


# =========================================================================
# 5. MASSEY PRODUCTS AND THE DISTINCTION BETWEEN X AND D^b(Coh(X))
# =========================================================================

@dataclass(frozen=True)
class MasseyAnalysis:
    r"""Analysis of Massey products at the two levels.

    Level 1 (manifold): Massey products on H^*(X, C).
      For compact Kahler: ALL Massey products vanish (DGMS).

    Level 3 (category): A_infinity operations m_k on Ext^*.
      These are the CATEGORICAL Massey products.
      Can be nonzero even when Level 1 Massey products vanish.
    """
    geometry: str
    # Level 1 Massey products on H^*(X, C)
    derham_massey_vanish: bool
    derham_reason: str
    # Level 3 categorical Massey products (m_3 on Ext)
    category_m3_zero: Optional[bool]
    category_reason: str
    # The critical distinction
    levels_agree: Optional[bool]
    disagreement_explanation: str


def massey_analysis(X: CYHodgeData) -> MasseyAnalysis:
    """Analyze Massey products at both levels."""
    v = analyze_formality(X)

    derham_vanish = not v.has_nonzero_massey_derham
    cat_m3_zero = (
        None if v.has_nonzero_m3_category is None
        else not v.has_nonzero_m3_category
    )
    agree = None if cat_m3_zero is None else derham_vanish == cat_m3_zero

    if agree is True:
        explanation = "Both levels agree for this geometry."
    elif agree is None:
        explanation = (
            f"{X.name}: de Rham Massey products vanish at the manifold level, "
            "but the categorical m_3 status is not certified by this engine. "
            "DGMS, BTT, Kaledin K1, and Hodge data do not control the "
            "A_infinity structure of D^b(Coh(X))."
        )
    else:
        explanation = (
            f"{X.name}: de Rham Massey products vanish (compact Kahler, DGMS), "
            f"but categorical m_3 is {'zero' if cat_m3_zero else 'nonzero'}. "
            "The de Rham formality of H^*(X) does NOT control the A_infinity "
            "structure of D^b(Coh(X)). The categorical m_3 involves multi-object "
            "Ext operations that are invisible to the commutative de Rham algebra."
        )

    return MasseyAnalysis(
        geometry=X.name,
        derham_massey_vanish=derham_vanish,
        derham_reason=(
            "Compact Kahler (DGMS 1975)" if X.is_compact
            else "Not compact Kahler"
        ),
        category_m3_zero=cat_m3_zero,
        category_reason=v.ainf_reason,
        levels_agree=agree,
        disagreement_explanation=explanation,
    )


# =========================================================================
# 6. QUINTIC EXT ALGEBRA: DETAILED ANALYSIS
# =========================================================================

@dataclass(frozen=True)
class QuinticExtAnalysis:
    r"""Detailed analysis of the quintic Ext algebra.

    For the quintic Q in P^4:
      Ext^*(O_Q, O_Q) = H^*(O_Q) = {C in degrees 0, 3}
    This is trivially formal (only identity and Serre class).

    For the FULL generator (Orlov):
      The derived category D^b(Coh(Q)) requires a generator involving
      line bundles O(d) for various d.  The Ext algebra
      bigoplus_{a,b} Ext^*(O(a), O(b)) has a rich A_infinity structure
      with m_3 coming from the Yukawa coupling.
    """
    # Ext^*(O, O) analysis
    ext_OO_dims: List[int]
    ext_OO_formal: bool
    ext_OO_reason: str
    # Full generator analysis
    full_generator_formal: Optional[bool]
    full_generator_reason: str
    # Yukawa coupling (the source of m_3)
    yukawa_classical: int  # Classical triple intersection H^3
    yukawa_has_gw_corrections: bool
    # Consequence for m_3
    m3_on_ext_OO: bool    # m_3 on Ext^*(O,O)
    m3_on_full_cat: Optional[bool]  # None means not certified here


def quintic_ext_analysis() -> QuinticExtAnalysis:
    """Detailed Ext algebra analysis for the quintic."""
    Q = quintic_threefold()
    ext_dims = Q.ext_O_dims()  # [1, 0, 0, 1]

    return QuinticExtAnalysis(
        ext_OO_dims=ext_dims,
        ext_OO_formal=True,
        ext_OO_reason=(
            "Ext^i(O_Q, O_Q) = H^i(O_Q) has dimensions [1, 0, 0, 1]. "
            "The algebra is concentrated in degrees 0 and 3 with no "
            "intermediate terms. The only product is the CY pairing "
            "Ext^0 x Ext^3 -> C. All higher m_k = 0 trivially "
            "(no room for Massey products in a 2-term algebra)."
        ),
        full_generator_formal=None,
        full_generator_reason=(
            "The full category D^b(Coh(Q)) has Ext^*(O(a), O(b)) != 0 "
            "for many (a,b). Yukawa and LG data are evidence for specific "
            "models, but this engine does not certify that the full "
            "multi-object A_infinity category has nonzero m_3 without an "
            "explicit model and comparison map."
        ),
        yukawa_classical=5,
        yukawa_has_gw_corrections=True,
        m3_on_ext_OO=False,
        m3_on_full_cat=None,
    )


# =========================================================================
# 7. PRODUCT FORMALITY FOR K3 x E
# =========================================================================

@dataclass(frozen=True)
class ProductFormalityAnalysis:
    r"""Formality analysis for the product K3 x E.

    De Rham level: H^*(K3 x E) = H^*(K3) x H^*(E) by Kunneth.
    Product of formal cdgas is formal.  So Level 1: FORMAL.

    Category level: D^b(Coh(K3 x E)) requires an explicit A_infinity product
    model and comparison map.  DGMS formality of the factors as manifolds does
    not prove A_infinity formality of the product category.  Relative K3-fiber
    formal statements are valid only after a formal fiber model is supplied.
    """
    # Factor formality
    k3_formal: Optional[bool]  # None means not certified here
    e_formal: bool   # E is NOT A_inf formal by Polishchuk
    # Product formality
    derham_product_formal: bool   # H^*(K3 x E) is formal
    ainf_product_formal: Optional[bool]
    # The critical observation
    relative_construction_works: Optional[bool]
    relative_reason: str


def product_formality_k3xe() -> ProductFormalityAnalysis:
    """Formality analysis for K3 x E."""
    return ProductFormalityAnalysis(
        k3_formal=None,
        e_formal=False,
        derham_product_formal=True,
        ainf_product_formal=None,
        relative_construction_works=None,
        relative_reason=(
            "The relative construction may use a formal K3 fiber only after "
            "a formal A_infinity model or strictifying datum is supplied. "
            "DGMS formality of H^*(K3) and Kunneth formality of de Rham cdgas "
            "do not by themselves certify the product A_infinity category or "
            "character-level agreement between relative and absolute models."
        ),
    )


# =========================================================================
# 8. PROGRAMME IMPLICATIONS
# =========================================================================

@dataclass(frozen=True)
class FormalityImplication:
    r"""Implications of formality status for the CY-to-chiral programme.

    If D^b(Coh(X)) IS A_infinity formal:
      - CY-A_d holds trivially (no higher corrections)
      - [m_3, B^{(2)}] = 0 trivially (m_3 = 0)
      - Shadow tower has depth 0 (class G)
      - The chiral algebra is determined by the cup product structure

    If a non-formal model has nonzero m_3:
      - raw [m_3, B^{(2)}_term] can be nonzero
      - corrected TCFT closure requires B^{(2)}_TCFT plus correction datum
      - derived closure requires the HH^{-2} filtration/comparison theorem
    """
    geometry: str
    ainf_formal: Optional[bool]
    # If formal: trivial consequences
    cya_trivial: Optional[bool]
    m3_b2_moot: Optional[bool]
    shadow_depth_zero: Optional[bool]
    # If non-formal: corrected TCFT/filtration resolution
    tcft_applies: Optional[bool]
    obs_ainf_class_zero: Optional[bool]
    shadow_class: str
    # For the programme
    cy_a_status: str  # ProvedHere, Programme, Conditional
    obstruction_status: str


def programme_implication(X: CYHodgeData) -> FormalityImplication:
    """Compute implications of formality status for the programme."""
    v = analyze_formality(X)

    if v.ainf_formal is True:
        return FormalityImplication(
            geometry=X.name,
            ainf_formal=True,
            cya_trivial=True,
            m3_b2_moot=True,
            shadow_depth_zero=True,
            tcft_applies=False,  # not needed
            obs_ainf_class_zero=True,  # trivially
            shadow_class="G",
            cy_a_status=(
                "ProvedHere" if X.cy_dim <= 2
                else "Programme (formal case simplifies but S^d-framing still needed)"
            ),
            obstruction_status="formal_input_m3_zero",
        )
    elif v.has_nonzero_m3_category is True:
        return FormalityImplication(
            geometry=X.name,
            ainf_formal=False,
            cya_trivial=False,
            m3_b2_moot=False,
            shadow_depth_zero=False,
            tcft_applies=(X.cy_dim == 3),
            obs_ainf_class_zero=False,
            shadow_class=v.shadow_class,
            cy_a_status=(
                "Not an S^3-framing obstruction" if X.cy_dim != 3
                else "Open: requires corrected TCFT datum or HH^{-2} filtration theorem"
            ),
            obstruction_status=(
                "not_applicable_to_S3_framing" if X.cy_dim != 3
                else "requires_corrected_TCFT_or_HH_minus_2_hypothesis"
            ),
        )
    else:
        return FormalityImplication(
            geometry=X.name,
            ainf_formal=None,
            cya_trivial=None,
            m3_b2_moot=None,
            shadow_depth_zero=None,
            tcft_applies=None,
            obs_ainf_class_zero=None,
            shadow_class=v.shadow_class,
            cy_a_status=(
                "Open: A_infinity status and obstruction comparison not certified"
            ),
            obstruction_status=v.obstruction_status,
        )


# =========================================================================
# 9. CORRECTED HH^{-2} OBSTRUCTION CRITERION
# =========================================================================

@dataclass(frozen=True)
class ObstructionVanishingCriterion:
    r"""Exact hypothesis package for derived S^3-framing obstruction vanishing."""
    complex_name: str
    filtration: str
    first_page: str
    target_total_degree: int
    comparison_map: str
    hypotheses: List[str]
    conclusion: str
    proves_universal_compact_cy3_closure: bool
    proves_raw_termwise_commutator_vanishing: bool


def hh_minus_two_obstruction_criterion() -> ObstructionVanishingCriterion:
    r"""Return the corrected derived obstruction theorem's hypothesis package.

    This is the only cohomological vanishing criterion recorded by this
    engine.  It is not DGMS, Kaledin HdR degeneration, BTT, or a
    chain-formality shortcut.
    """
    return ObstructionVanishingCriterion(
        complex_name="reduced Hochschild E_1-cochain complex C^bullet_{E_1}(A,A)",
        filtration="bar-length filtration on a connective unit-connected strictified Hochschild E_1-model A",
        first_page="E_1^{p,q}=Hom((s overline A)^{tensor p}, A)^q",
        target_total_degree=-2,
        comparison_map=(
            "chain-level map from the S^3-framing obstruction complex to "
            "C^bullet_{E_1}(A,A)[2]"
        ),
        hypotheses=[
            "the filtration is complete",
            "the filtration is exhaustive",
            "the filtration is separated",
            "the spectral sequence is strongly convergent",
            "E_1^{p,q}=0 whenever p+q=-2",
            "the obstruction cocycle lands in total degree -2 under the comparison map",
        ],
        conclusion="HH^{-2}_{E_1}(A,A)=0 for that strictified model, so the compared derived obstruction class vanishes",
        proves_universal_compact_cy3_closure=False,
        proves_raw_termwise_commutator_vanishing=False,
    )


# =========================================================================
# 10. CORRECTION TO CECH_HTT_CONVERGENCE.PY CLAIM
# =========================================================================

@dataclass(frozen=True)
class FormalityCorrectionRecord:
    r"""Record of the correction needed in cech_htt_convergence.py.

    The function quintic_cover() in cech_htt_convergence.py claims:
      is_formal=True, shadow_class="G"
    with the comment citing BTT/Kaledin.

    This conflates two things:
    (a) BTT: the quintic has UNOBSTRUCTED DEFORMATIONS (HH^2 maps
        surjectively to the deformation space). This is about the
        deformation problem, not A_infinity formality.
    (b) Kaledin K1: HdR degeneration. This is about the spectral
        sequence, not A_infinity formality.

    Neither (a) nor (b) implies A_infinity formality.

    The correct statement: the quintic is de Rham formal (DGMS, Level 1)
    and has HdR degeneration (Kaledin, Level 2), but this does not decide
    A_infinity formality of the full category.

    HOWEVER: this subtlety does not affect the Cech-HTT computation itself.
    The Cech contracting homotopy construction works regardless of formality:
    it computes the CHAIN-LEVEL A_infinity operations, and the convergence
    bound applies to both formal and non-formal geometries.
    """
    file_path: str
    current_claim: str
    correct_claim: str
    impact_on_computation: str


def formality_correction() -> FormalityCorrectionRecord:
    """Record the correction needed."""
    return FormalityCorrectionRecord(
        file_path="compute/lib/cech_htt_convergence.py",
        current_claim=(
            "quintic_cover(): is_formal=True, shadow_class='G'. "
            "Comment: 'BTT: unobstructed Kodaira-Spencer deformations "
            "imply formality of D^b(Coh(X)) as a CY3 category, by "
            "Kaledin's theorem applied to the smooth case.'"
        ),
        correct_claim=(
            "The quintic is de Rham formal (DGMS, compact Kahler) and "
            "has HdR degeneration (Kaledin K1), but neither statement "
            "certifies A_infinity formality of D^b(Coh(Q)). BTT gives "
            "unobstructed deformations, not A_infinity formality. "
            "Kaledin K2 (tilting formality) does not apply because "
            "compact CY3 has no tilting generator (Ext^3 != 0 by Serre "
            "duality). Yukawa and LG data require an explicit "
            "A_infinity model and comparison map before they decide the "
            "full category or its shadow class."
        ),
        impact_on_computation=(
            "The Cech-HTT convergence computation is UNAFFECTED by this "
            "correction. The convergence bound applies to both formal "
            "and non-formal geometries. The is_formal flag and shadow_class "
            "are metadata, not inputs to the convergence estimate."
        ),
    )


# =========================================================================
    # 11. COMPREHENSIVE FORMALITY TABLE
# =========================================================================

def formality_table() -> List[Dict[str, Any]]:
    r"""Comprehensive formality table for all standard CY manifolds.

    Returns a list of dicts, one per geometry, with all three formality
    levels and the consequences.
    """
    geometries = [
        elliptic_curve(),
        k3_surface(),
        abelian_surface(),
        quintic_threefold(),
        k3_times_e(),
        bicubic_threefold(),
        conifold_resolved(),
    ]

    table = []
    for X in geometries:
        v = analyze_formality(X)
        k = kaledin_analysis(X)
        m = massey_analysis(X)
        p = programme_implication(X)

        table.append({
            "geometry": X.name,
            "cy_dim": X.cy_dim,
            "chi_O": X.chi_O(),
            "chi_top": X.euler_char(),
            "ext_O_concentrated": X.ext_O_concentrated(),
            # Three levels
            "L1_derham_formal": v.de_rham_formal,
            "L2_hdr_degeneration": v.hdr_degeneration,
            "L3_ainf_formal": v.ainf_formal,
            # Kaledin
            "kaledin_k1": k.k1_applies,
            "kaledin_k2": k.k2_applies,
            "has_tilting": k.has_tilting_generator,
            # Massey
            "derham_massey_vanish": m.derham_massey_vanish,
            "category_m3_zero": m.category_m3_zero,
            "levels_agree": m.levels_agree,
            # Programme
            "shadow_class": v.shadow_class,
            "tcft_needed": v.tcft_needed,
            "obs_ainf_zero": p.obs_ainf_class_zero,
            "ainf_status": v.ainf_status,
            "obstruction_status": p.obstruction_status,
        })

    return table


# =========================================================================
# 12. MASTER VERIFICATION
# =========================================================================

def verify_formality_hierarchy() -> Dict[str, Any]:
    r"""Master verification of the formality hierarchy.

    Checks internal consistency of the entire analysis.
    """
    results: Dict[str, Any] = {}

    # 1. Check level implication chain
    implications = level_implication_chain()
    results["implication_chain"] = implications
    # Only 3 => 2 should be True
    for fr, to, imp in implications:
        if fr == 3 and to == 2:
            assert imp is True, f"Level 3 should imply Level 2"
        else:
            assert imp is False, f"Level {fr} should NOT imply Level {to}"
    results["implication_chain_consistent"] = True

    # 2. Check all geometries
    table = formality_table()
    results["table"] = table

    for row in table:
        geo = row["geometry"]

        # L2 (Kaledin K1) should apply to all smooth proper
        if geo != "resolved conifold":
            assert row["L2_hdr_degeneration"], f"HdR should degenerate for {geo}"

        # de Rham Massey products vanish for all compact Kahler
        assert row["derham_massey_vanish"], f"DGMS should give vanishing Massey for {geo}"

        # If L3 (A_inf formal), then m3 = 0
        if row["L3_ainf_formal"]:
            assert row["category_m3_zero"], f"A_inf formal => m3 = 0 for {geo}"

        # Obs_Ainf is closed here only for certified formal input cases.
        if row["obs_ainf_zero"] is True:
            assert row["L3_ainf_formal"] is True, (
                f"Obs_Ainf closure for {geo} requires formal input or the "
                "explicit HH^{-2} criterion"
            )

    results["all_geometries_consistent"] = True

    # 3. Check the critical cases
    # Quintic: L1 formal; L3 full-category status not certified here
    quintic_row = [r for r in table if r["geometry"] == "quintic threefold"][0]
    assert quintic_row["L1_derham_formal"] is True
    assert quintic_row["L3_ainf_formal"] is None
    assert quintic_row["levels_agree"] is None
    results["quintic_l3_not_certified"] = True

    # K3: L1 formal; L3 is not certified by DGMS/Kaledin here
    k3_row = [r for r in table if r["geometry"] == "K3 surface"][0]
    assert k3_row["L1_derham_formal"] is True
    assert k3_row["L3_ainf_formal"] is None
    assert k3_row["levels_agree"] is None
    results["k3_not_certified_by_dgms"] = True

    # Elliptic curve: L1 formal, L3 NOT formal
    e_row = [r for r in table if r["geometry"] == "elliptic curve"][0]
    assert e_row["L1_derham_formal"] is True
    assert e_row["L3_ainf_formal"] is False
    results["elliptic_l1_ne_l3"] = True

    # K3 x E: L1 formal; L3 product-category status not certified here
    k3e_row = [r for r in table if r["geometry"] == "K3 x E"][0]
    assert k3e_row["L1_derham_formal"] is True
    assert k3e_row["L3_ainf_formal"] is None
    results["k3xe_not_certified"] = True

    # Conifold: L3 formal
    con_row = [r for r in table if r["geometry"] == "resolved conifold"][0]
    assert con_row["L3_ainf_formal"] is True
    results["conifold_formal"] = True

    # 4. Kaledin analysis check
    for X_fn in [quintic_threefold, k3_surface, elliptic_curve, conifold_resolved]:
        X = X_fn()
        k = kaledin_analysis(X)
        if X.name == "resolved conifold":
            assert k.k2_applies is True, "Conifold should have tilting"
        elif X.is_compact:
            assert k.k2_applies is False, f"Compact CY should not have tilting: {X.name}"
    results["kaledin_analysis_consistent"] = True

    # 5. Quintic Ext analysis
    qea = quintic_ext_analysis()
    assert qea.ext_OO_dims == [1, 0, 0, 1], "Quintic Ext^*(O,O) dims wrong"
    assert qea.ext_OO_formal is True, "Ext^*(O,O) should be trivially formal"
    assert qea.m3_on_ext_OO is False, "m3 on Ext^*(O,O) should be zero"
    assert qea.m3_on_full_cat is None, "full-category m3 is not certified here"
    assert qea.yukawa_classical == 5, "Classical Yukawa = H^3 = 5"
    results["quintic_ext_analysis_correct"] = True

    # 6. Product formality check
    pf = product_formality_k3xe()
    assert pf.k3_formal is None
    assert pf.e_formal is False
    assert pf.derham_product_formal is True
    assert pf.ainf_product_formal is None
    assert pf.relative_construction_works is None
    results["product_formality_correct"] = True

    # 7. Hodge data consistency
    Q = quintic_threefold()
    assert Q.chi_O() == 0, "chi(O_Q) = 0 for CY3"
    assert Q.euler_char() == -200, "chi(Q) = -200 for quintic"
    assert Q.kodaira_spencer_dim() == 101, "h^{2,1} = 101 for quintic"
    assert Q.ext_O_concentrated() is True, "Ext^*(O,O) concentrated for quintic"

    K3 = k3_surface()
    assert K3.chi_O() == 2, "chi(O_{K3}) = 2"
    assert K3.euler_char() == 24, "chi(K3) = 24"

    K3E = k3_times_e()
    assert K3E.chi_O() == 0, "chi(O_{K3xE}) = 0 (CY3)"
    assert K3E.cy_dim == 3

    E = elliptic_curve()
    assert E.chi_O() == 0, "chi(O_E) = 0"

    results["hodge_data_consistent"] = True

    criterion = hh_minus_two_obstruction_criterion()
    assert criterion.complex_name.startswith("reduced Hochschild E_1-cochain")
    assert criterion.target_total_degree == -2
    assert criterion.proves_universal_compact_cy3_closure is False
    assert criterion.proves_raw_termwise_commutator_vanishing is False
    results["hh_minus_two_criterion_precise"] = True

    results["all_passed"] = True
    return results
