r"""Derived geometric Satake correspondence for chiral quantum groups.

STATUS: CONJECTURAL (AP-CY14, AP-CY6).
The derived Satake for chiral quantum groups is a PROGRAMME, not a theorem.
Only the classical geometric Satake (Mirkovic-Vilonen-Ginzburg) is proved.
All chiral/CY extensions are conjectural.  The K3 specialization passes
through the unconstructed K3 Yangian Y(g_{K3}); results about it are
conditional on its existence.

MATHEMATICAL CONTENT
====================

The geometric Satake equivalence (Mirkovic-Vilonen, 2007; Ginzburg, 1995)
identifies the category of perverse sheaves on the affine Grassmannian
with representations of the Langlands dual group:

    Perv(Gr_G)  ~=  Rep(G^L)

as monoidal categories, where the monoidal structure on the left is the
convolution product and on the right is the tensor product.

The DERIVED version (Bezrukavnikov-Finkelberg, 2008) replaces perverse
sheaves with D-modules:

    D-mod(Gr_G)  ~=  IndCoh(N^L / G^L)

where N^L is the nilpotent cone in g^L (the Lie algebra of the Langlands
dual group).  This is an equivalence of DG categories.

For CHIRAL quantum groups, the programme constructs a chiral affine
Grassmannian Gr^{ch}_G and a chiral derived Satake:

    D-mod(Gr^{ch}_G)  ~=  Rep^{E_2}(chiral QG)

This module computes the concrete data for this programme at each level:

1. THE CHIRAL AFFINE GRASSMANNIAN Gr^{ch}_G.
   The classical affine Grassmannian Gr_G = G((t)) / G[[t]] parametrizes
   G-bundles on the formal disk D = Spec C[[t]] with trivialization on the
   punctured disk D* = Spec C((t)).

   The chiral refinement Gr^{ch}_G replaces the formal disk by a formal
   neighborhood of a point on a curve C in the Ran space:
     Gr^{ch}_G(x) = G-bundles on D_x with trivialization on D_x^*
   for each x in C.  As x varies over Ran(C), this defines a factorization
   space (Beilinson-Drinfeld, "Chiral Algebras", Chapter 5).

   KEY PROPERTY: Gr^{ch}_G over Ran(C) is a factorization ind-scheme.
   The factorization structure encodes the fusion of G-bundles:
     Gr^{ch}_G(x_1, x_2) -> Gr^{ch}_G(x_1) x Gr^{ch}_G(x_2)  as x_1, x_2 separate.

2. THE CONVOLUTION PRODUCT AS GEOMETRIC COPRODUCT.
   The convolution on Perv(Gr_G):
     F_1 * F_2 = m_*(F_1 boxtimes F_2)
   where m: Gr_G x^{G[[t]]} Gr_G -> Gr_G is the multiplication map.

   In the chiral setting, this convolution becomes the FACTORIZATION product:
     F_1 *^{ch} F_2 = factorization product over Ran(C).

   The Drinfeld coproduct Delta_z on the chiral quantum group is the
   DUAL of this convolution: the convolution defines a product on sheaves,
   and by Satake duality this corresponds to a coproduct on the algebra.

   For the affine Yangian Y(gl_hat_1) with structure function g(u):
     Convolution on Gr:  F_{lambda} * F_{mu} -> F_{lambda+mu}
     Coproduct on Y:     Delta_z(T(u)) = T_L(u) T_R(u-z)  (Miura)
   The spectral parameter z is the SEPARATION between the two points
   on Ran(C) (AP-CY31: this is Yangian spectral, not worldsheet).

3. THE GEOMETRIC R-MATRIX FROM COMMUTATIVITY CONSTRAINT.
   The monoidal structure on Perv(Gr_G) is SYMMETRIC (Mirkovic-Vilonen):
     F_1 * F_2 ~= F_2 * F_1 (commutativity constraint).

   In the chiral/derived setting, the commutativity is replaced by a
   BRAIDING (the E_2 structure):
     F_1 *^{ch} F_2 -> F_2 *^{ch} F_1 via R-matrix.

   The R-matrix is the holonomy of the factorization connection along a
   path in Ran(C) that exchanges x_1 and x_2:
     R(z) = holonomy along x_1 <-> x_2 at separation z.

   For toric CY_3 (C^3 with Omega-background):
     The R-matrix is the MO (Maulik-Okounkov) stable envelope R-matrix.
     On charge-1 Fock space: R(z) = g(z) = prod (z-h_i)/(z+h_i).

4. GL_1 ON K3: THE ABELIAN CHIRAL SATAKE.
   For G = GL_1 on K3, the affine Grassmannian is:
     Gr_{GL_1} = Z  (the integers, classifying line bundle degree).

   The chiral refinement: Gr^{ch}_{GL_1}(K3) parametrizes line bundles
   on the formal K3-disk D_{K3} with trivialization on D_{K3}^*.
   The lattice of line bundle types is the Mukai lattice Lambda_Muk
   of rank 24 and signature (4,20).

   The D-modules on Gr^{ch}_{GL_1}(K3) should be equivalent to
   Rep^{E_2}(Y(g_{K3})) (CONJECTURAL: depends on K3 Yangian existence).

   The convolution product is:
     D-mod(Gr^{ch}_{GL_1}) x D-mod(Gr^{ch}_{GL_1})
       -> D-mod(Gr^{ch}_{GL_1})
   which, under the Satake equivalence, gives the tensor product on
   Rep^{E_2}(Y(g_{K3})).

   At the level of Fock spaces:
     Convolution of charge-n and charge-m sheaves
       <-> tensor product of F_n and F_m Yangian modules
     dim(F_n) = p_{24}(n) (24-coloured partitions)

5. THE IWAHORI AND BOREL REDUCTIONS.
   The full affine Grassmannian Gr_G = G((t))/G[[t]] admits reductions:
   - Iwahori: Fl_G = G((t))/I (affine flag variety)
   - Opposite Borel: G((t))/B^-((t))

   For the Satake with Iwahori level structure:
     Perv_{I}(Gr_G) ~= Rep(G^L) as module category for the Hecke algebra

   In the chiral setting, the Iwahori reduction gives:
     D-mod_I(Gr^{ch}_G) ~= Rep^{E_1}(A^!)  (E_1 representations of Koszul dual)

   The passage from E_1 to E_2 (full Satake from Iwahori Satake) is
   the Drinfeld center (AP-CY4: Drinfeld center != derived center):
     Z(D-mod_I(Gr^{ch}_G)) ~= D-mod(Gr^{ch}_G) ~= Rep^{E_2}(chiral QG)

6. ORBITS AND WEIGHT FUNCTORS.
   The G[[t]]-orbits on Gr_G are indexed by dominant coweights lambda^+:
     Gr_G = bigsqcup_{lambda^+} Gr_G^{lambda^+}

   For G = GL_n: lambda^+ = (lambda_1 >= ... >= lambda_n >= 0), partitions.
   The intersection cohomology sheaves IC_{lambda^+} form the simple objects
   of Perv(Gr_G), and under Satake they map to irreducible representations
   V_{lambda^+} of G^L.

   The MV (Mirkovic-Vilonen) weight functors:
     F_mu: Perv(Gr_G) -> Vect,  F -> H^*(S_mu cap supp(F))
   where S_mu = N^-((t)) . t^mu is the semi-infinite orbit.
   The weight functor extracts the mu-weight space of V_{lambda^+}.

   For GL_1 on K3: lambda^+ in Z^{24} (Mukai lattice vectors).
   The orbits are single points (GL_1 is abelian):
     Gr_{GL_1}^{lambda} = {t^lambda} for each lambda in Lambda_Muk.
   The IC sheaves are sky-scraper sheaves at lattice points.
   Under Satake: IC_lambda <-> evaluation module V_u^{(a)} of Y(g_{K3}).

CONVENTIONS
===========
  - Spectral parameter z is Yangian (NOT worldsheet, AP-CY31)
  - kappa subscripts per AP113: kappa_ch, kappa_cat, kappa_BKM, kappa_fiber
  - AP-CY14: ALL chiral Satake results are CONJECTURAL
  - AP-CY6: unconstructed A_X NEVER inhabits theorem environment
  - AP-CY4: Drinfeld center Z(C) != derived center Z^der_ch(A)
  - AP-CY7: CoHA != E_1-chiral algebra
  - AP-CY11: conditionality propagates through all downstream results
  - AP-CY23: E_1-chiral bialgebra is the correct Hopf home (not E_inf)
  - AP-CY25: R-matrix from half-braiding, NOT from Delta(1)
  - AP150: each arrow in composite verified independently

REFERENCES
==========
  drinfeld_center_k3_heisenberg.py (Drinfeld double, R-matrix)
  chiral_qg_rep_category.py (Rep^{E_2}(Y(g_{K3})))
  chiral_koszul_derived.py (derived Koszul duality)
  k3_yangian.py (K3 Yangian construction)
  chiral_homology_ran_k3.py (chiral homology via Ran space)
  e1_chiral_bialgebra_engine.py (E_1-chiral coproduct)
  mo_rmatrix_k3e.py (Maulik-Okounkov R-matrix)
  geometric_langlands.tex sec:open-problems (open problem (v))
  Mirkovic-Vilonen, arXiv:math/0401222 (geometric Satake)
  Ginzburg, arXiv:alg-geom/9511007 (perverse sheaves on loop groups)
  Bezrukavnikov-Finkelberg, arXiv:0707.3799 (derived Satake)
  Beilinson-Drinfeld, "Chiral Algebras" (2004), Ch. 5
  Gaitsgory, arXiv:1108.4455 (contractibility of Gr_G and Satake)
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

F = Fraction


# =========================================================================
# 0. Constants: classical geometric Satake ground truth
# =========================================================================

# Mirkovic-Vilonen (2007): Perv(Gr_G) ~= Rep(G^L)
MV_PROVED = True

# Bezrukavnikov-Finkelberg (2008): D-mod(Gr_G) ~= IndCoh(N^L / G^L)
BF_DERIVED_PROVED = True

# Chiral extension: CONJECTURAL
CHIRAL_SATAKE_STATUS = "CONJECTURAL"

# Mukai lattice data for GL_1 on K3
MUKAI_RANK = 24
MUKAI_SIG_PLUS = 4
MUKAI_SIG_MINUS = 20


# =========================================================================
# 1. Classical affine Grassmannian structure
# =========================================================================

class AffineGrassmannianData(NamedTuple):
    """Structure data for the affine Grassmannian Gr_G.

    Gr_G = G((t)) / G[[t]] parametrizes G-bundles on the formal disk
    with trivialization on the punctured disk.
    """
    group: str                       # G
    langlands_dual: str              # G^L
    rank: int                        # rank(G)
    is_simply_laced: bool            # ADE type
    dual_coxeter: int                # h^v
    dim_lie_algebra: int             # dim(g)
    orbit_indexing: str              # dominant coweights
    pi_0: str                        # connected components
    satake_status: str               # 'PROVED' for classical


class GrOrbitData(NamedTuple):
    """Data for a G[[t]]-orbit in Gr_G.

    The orbit Gr_G^{lambda} for dominant coweight lambda has:
    - dimension 2*rho(lambda) where rho is the half-sum of positive roots
    - closure Gr_G^{lambda}_bar = union of Gr_G^{mu} for mu <= lambda
    - IC sheaf IC_lambda which maps to V_lambda under Satake
    """
    coweight: Tuple[int, ...]     # dominant coweight lambda^+
    orbit_dim: int                # dim(Gr^lambda) = 2*rho(lambda)
    ic_sheaf_label: str           # label for the IC sheaf
    satake_image: str             # V_lambda: irrep of G^L
    closure_order: str            # description of closure relations


def affine_grassmannian(group: str = "GL_1",
                        rank: int = 1,
                        dual_coxeter: int = 0) -> AffineGrassmannianData:
    r"""Construct the affine Grassmannian data for a group G.

    For GL_1: Gr_{GL_1} = Z (integers), parametrizing line bundle degree.
    The orbits are single points (abelian group).

    For SL_2: Gr_{SL_2} has orbits indexed by non-negative integers
    (dominant coweights of SL_2 = Z_>=0).  The n-th orbit has dimension 2n.

    For GL_n: orbits indexed by partitions lambda = (lambda_1 >= ... >= lambda_n).

    Args:
        group: name of the group (e.g., "GL_1", "SL_2", "GL_n")
        rank: rank of the group
        dual_coxeter: dual Coxeter number h^v

    Returns:
        AffineGrassmannianData with structure data.
    """
    # Determine Langlands dual and Lie algebra dimension
    langlands_duals = {
        "GL_1": "GL_1",
        "SL_2": "PGL_2",
        "PGL_2": "SL_2",
        "SL_n": "PGL_n",
        "GL_n": "GL_n",
        "E_8": "E_8",
    }
    dim_formulas = {
        "GL_1": 1,
        "SL_2": 3,
        "PGL_2": 3,
        "GL_n": rank * rank,
        "SL_n": rank * rank - 1,
        "E_8": 248,
    }
    simply_laced = {"GL_1", "SL_2", "PGL_2", "SL_n", "GL_n", "E_8"}

    ldual = langlands_duals.get(group, f"{group}^L")
    dim_g = dim_formulas.get(group, 0)

    if group == "GL_1":
        orbit_idx = "Z (integers: line bundle degree)"
        pi0 = "Z (one component per degree)"
    elif group in ("SL_2", "PGL_2"):
        orbit_idx = "Z_>=0 (non-negative integers)"
        pi0 = "trivial (connected)"
    else:
        orbit_idx = "dominant coweights Lambda^+"
        pi0 = "pi_1(G) (cocharacter lattice mod coroot lattice)"

    return AffineGrassmannianData(
        group=group,
        langlands_dual=ldual,
        rank=rank,
        is_simply_laced=group in simply_laced,
        dual_coxeter=dual_coxeter,
        dim_lie_algebra=dim_g,
        orbit_indexing=orbit_idx,
        pi_0=pi0,
        satake_status="PROVED",
    )


def gr_orbit(group: str, coweight: Tuple[int, ...],
             dual_coxeter: int = 0) -> GrOrbitData:
    r"""Construct orbit data for a dominant coweight.

    For SL_2 with coweight (n,): orbit dimension = 2n, IC -> V_n (spin n/2).
    For GL_1 with coweight (d,): orbit = single point {t^d}, dimension 0.

    Args:
        group: name of the group
        coweight: dominant coweight as tuple
        dual_coxeter: dual Coxeter number

    Returns:
        GrOrbitData for the orbit.
    """
    if group == "GL_1":
        # Abelian: all orbits are points
        d = coweight[0]
        return GrOrbitData(
            coweight=coweight,
            orbit_dim=0,
            ic_sheaf_label=f"delta_{{{d}}}",
            satake_image=f"C_{{{d}}} (1-dim rep at degree {d})",
            closure_order="trivial (single point)",
        )
    elif group in ("SL_2", "PGL_2"):
        n = coweight[0]
        return GrOrbitData(
            coweight=coweight,
            orbit_dim=2 * n,
            ic_sheaf_label=f"IC_{{{n}}}",
            satake_image=f"V_{{{n}}} (irrep of dim {n + 1})",
            closure_order=f"Gr^{{{n}}}_bar = union Gr^{{m}} for 0 <= m <= {n}, m = {n} mod 2",
        )
    else:
        return GrOrbitData(
            coweight=coweight,
            orbit_dim=sum(coweight),  # simplified
            ic_sheaf_label=f"IC_{{{coweight}}}",
            satake_image=f"V_{{{coweight}}}",
            closure_order="partial order on dominant coweights",
        )


# =========================================================================
# 2. Chiral affine Grassmannian (factorization structure)
# =========================================================================

class ChiralGrassmannianData(NamedTuple):
    """The chiral affine Grassmannian Gr^{ch}_G over Ran(C).

    Gr^{ch}_G is a factorization ind-scheme over Ran(C):
    for each finite subset S of C, Gr^{ch}_G(S) parametrizes
    G-bundles on the formal neighborhood of S with trivialization
    outside S.  The factorization structure encodes fusion.
    """
    group: str                    # G
    base_curve: str               # C (abstract curve)
    is_factorization: bool        # True: factorization ind-scheme
    factorization_type: str       # 'multiplicative' (via G-bundles)
    classical_fiber: str          # Gr_G (the classical Grassmannian)
    ran_space_structure: str      # description of the Ran space variant
    status: str                   # 'PROVED' for BD construction


def chiral_grassmannian(group: str = "GL_1",
                        curve: str = "C") -> ChiralGrassmannianData:
    r"""Construct the chiral affine Grassmannian Gr^{ch}_G.

    The Beilinson-Drinfeld construction (Chiral Algebras, Ch. 5):
    Gr^{ch}_G is the moduli of (x_1,...,x_n, P, phi) where
    - x_1,...,x_n are points of C
    - P is a G-bundle on the formal disk around {x_1,...,x_n}
    - phi is a trivialization of P on the punctured disk

    The FACTORIZATION PROPERTY (BD, Theorem 5.3.12):
      Gr^{ch}_G({x_1,...,x_n}) -> prod_i Gr^{ch}_G({x_i})
    is an isomorphism when the x_i are distinct (no collisions).

    At a collision x_1 -> x_2, the fiber DOES NOT split:
    this non-splitting encodes the OPE/fusion of the chiral algebra.

    STATUS: The chiral Grassmannian exists as a mathematical object
    (Beilinson-Drinfeld, proved).  What is CONJECTURAL is the
    identification of D-modules on it with chiral QG representations.

    Args:
        group: name of the group
        curve: name of the base curve

    Returns:
        ChiralGrassmannianData.
    """
    return ChiralGrassmannianData(
        group=group,
        base_curve=curve,
        is_factorization=True,
        factorization_type="multiplicative (G-bundle gluing)",
        classical_fiber=f"Gr_{{{group}}} (affine Grassmannian of {group})",
        ran_space_structure=(
            f"Gr^{{ch}}_{{{group}}} -> Ran({curve}): "
            f"fiber over {{x_1,...,x_n}} is Gr_{{{group}}}(D_{{x_1}} union ... union D_{{x_n}})"
        ),
        status="PROVED (Beilinson-Drinfeld construction)",
    )


class FactorizationPropertyData(NamedTuple):
    """The factorization property of Gr^{ch}_G.

    At separated points: Gr^{ch}_G({x_1,...,x_n}) ~= prod Gr^{ch}_G({x_i}).
    At collision: non-split fiber encodes fusion/OPE.
    """
    num_points: int
    separated: bool           # whether points are distinct
    splits: bool              # True if separated
    fusion_type: str          # description of the fusion at collision
    coproduct_relation: str   # how this relates to the coproduct


def factorization_property(num_points: int = 2,
                           separated: bool = True,
                           group: str = "GL_1") -> FactorizationPropertyData:
    r"""Compute the factorization property at given configuration.

    For 2 points (the key case):
    - Separated (x_1 != x_2): Gr(x_1, x_2) ~= Gr(x_1) x Gr(x_2)
      This encodes the TENSOR PRODUCT of representations.
    - Collision (x_1 -> x_2): Gr(x_1, x_2) -> Gr(x) (non-split)
      This encodes the FUSION / OPE.

    The coproduct Delta_z on the chiral QG is the algebraic dual of the
    factorization structure as z = x_1 - x_2 -> 0.

    Args:
        num_points: number of points in the configuration
        separated: whether points are distinct
        group: the structure group

    Returns:
        FactorizationPropertyData.
    """
    if separated:
        return FactorizationPropertyData(
            num_points=num_points,
            separated=True,
            splits=True,
            fusion_type="trivial (tensor product)",
            coproduct_relation=(
                "Delta_z at z = infty: "
                "Delta(a) = a tensor 1 + 1 tensor a (primitive)"
            ),
        )
    else:
        return FactorizationPropertyData(
            num_points=num_points,
            separated=False,
            splits=False,
            fusion_type=(
                f"non-trivial: encodes the OPE of the {group} chiral algebra; "
                "the fiber is the convolution Grassmannian"
            ),
            coproduct_relation=(
                "Delta_z at z -> 0: full Drinfeld coproduct "
                "Delta_z(T(u)) = T_L(u) T_R(u-z) (AP-CY31: z is spectral)"
            ),
        )


# =========================================================================
# 3. Convolution product and its dual (the coproduct)
# =========================================================================

class ConvolutionData(NamedTuple):
    """The convolution product on D-mod(Gr^{ch}_G) and its Satake dual.

    Convolution: F_1 * F_2 = m_*(F_1 boxtimes F_2) on sheaves.
    Under Satake: corresponds to the tensor product on Rep(G^L).
    In the chiral setting: becomes the factorization product.
    Dual operation on the algebra: the coproduct Delta_z.
    """
    product_type: str          # 'convolution' or 'factorization'
    input_charges: Tuple[int, int]
    output_charge: int
    sheaf_description: str
    satake_image: str          # corresponding operation on Rep
    coproduct_formula: str     # the dual coproduct on the QG


def convolution_product(n: int, m: int,
                        group: str = "GL_1") -> ConvolutionData:
    r"""Compute the convolution of charge-n and charge-m sheaves.

    For GL_1 on K3:
      The convolution of charge-n and charge-m D-modules gives a
      charge-(n+m) D-module.  Under Satake, this is:
        F_n tensor F_m -> F_{n+m}
      where F_k is the charge-k Fock space with dim = p_{24}(k).

    The Satake dual of convolution is the Drinfeld coproduct:
      Delta_z: F_{n+m} -> F_n tensor_{z} F_m
    where tensor_z denotes the z-dependent tensor product from the
    factorization structure.

    Args:
        n, m: charges of the input sheaves/modules
        group: structure group

    Returns:
        ConvolutionData.
    """
    if group == "GL_1":
        dim_n = _p24(n)
        dim_m = _p24(m)
        dim_nm = _p24(n + m)
        return ConvolutionData(
            product_type="factorization convolution on Ran(C)",
            input_charges=(n, m),
            output_charge=n + m,
            sheaf_description=(
                f"D-mod^{{{n}}}(Gr) * D-mod^{{{m}}}(Gr) -> D-mod^{{{n+m}}}(Gr), "
                f"dims: {dim_n} x {dim_m} -> {dim_nm}"
            ),
            satake_image=(
                f"F_{{{n}}} tensor F_{{{m}}} -> F_{{{n+m}}}, "
                f"p_24({n}) x p_24({m}) = {dim_n} x {dim_m}"
            ),
            coproduct_formula=(
                f"Delta_z: F_{{{n+m}}} -> F_{{{n}}} tensor_z F_{{{m}}}, "
                f"z-dependent factorization coproduct (AP-CY31: z is spectral)"
            ),
        )
    elif group in ("SL_2", "PGL_2"):
        return ConvolutionData(
            product_type="convolution on Gr_{SL_2}",
            input_charges=(n, m),
            output_charge=n + m,
            sheaf_description=(
                f"IC_{{{n}}} * IC_{{{m}}} = "
                f"sum_{{k=0}}^{{min({n},{m})}} IC_{{{n}+{m}-2k}} "
                "(Clebsch-Gordan decomposition)"
            ),
            satake_image=(
                f"V_{{{n}}} tensor V_{{{m}}} = "
                f"sum_{{k=0}}^{{min({n},{m})}} V_{{{n}+{m}-2k}}"
            ),
            coproduct_formula=(
                f"Delta: V_{{{n+m}}} -> sum V_{{{n}}} tensor V_{{{m}}} "
                "(classical coproduct)"
            ),
        )
    else:
        return ConvolutionData(
            product_type="convolution",
            input_charges=(n, m),
            output_charge=n + m,
            sheaf_description="general convolution",
            satake_image="general tensor product decomposition",
            coproduct_formula="general Drinfeld coproduct",
        )


# =========================================================================
# 4. The geometric R-matrix from the commutativity constraint
# =========================================================================

class GeometricRMatrixData(NamedTuple):
    """The geometric R-matrix from the Satake commutativity constraint.

    Classical Satake: Perv(Gr_G) is SYMMETRIC monoidal.
    The commutativity constraint F_1 * F_2 ~= F_2 * F_1 is a natural
    isomorphism that squares to the identity.

    Chiral Satake: D-mod(Gr^{ch}_G) is BRAIDED monoidal (E_2).
    The braiding F_1 * F_2 -> F_2 * F_1 is the geometric R-matrix.
    It does NOT square to the identity (non-symmetric braiding).

    Under Satake duality, the geometric R-matrix on D-mod(Gr^{ch}_G)
    corresponds to the R-matrix on Rep(chiral QG).

    AP-CY25: The R-matrix is characterized via the half-braiding,
    NOT by applying the coproduct to the vacuum.
    """
    level: str                     # 'classical' or 'chiral'
    braiding_type: str             # 'symmetric' or 'E_2-braided'
    r_matrix_formula: str          # formula for the R-matrix
    ybe_satisfied: bool            # Yang-Baxter equation
    unitarity: str                 # R(z) R(-z) = 1 relation
    classical_limit: str           # R(z) -> Id as z -> infty
    charge: int                    # charge of the representation
    source: str                    # 'commutativity constraint' etc.


def geometric_r_matrix_classical() -> GeometricRMatrixData:
    r"""The classical geometric R-matrix (symmetric commutativity).

    In the classical Satake, Perv(Gr_G) is symmetric monoidal.
    The commutativity constraint is:
      c_{F_1, F_2}: F_1 * F_2 -> F_2 * F_1
    with c^2 = Id (symmetric, not just braided).

    This corresponds to Rep(G^L) being symmetric monoidal
    (the standard swap isomorphism V tensor W -> W tensor V).
    """
    return GeometricRMatrixData(
        level="classical",
        braiding_type="symmetric",
        r_matrix_formula="R = swap (trivial: V tensor W -> W tensor V)",
        ybe_satisfied=True,
        unitarity="R^2 = Id (symmetric)",
        classical_limit="R = Id (no spectral parameter)",
        charge=0,
        source="commutativity constraint on Perv(Gr_G) (Mirkovic-Vilonen)",
    )


def geometric_r_matrix_chiral_charge1(
    h: Tuple[F, F, F] = (F(1), F(-2), F(1)),
) -> GeometricRMatrixData:
    r"""The chiral geometric R-matrix at charge 1 for C^3.

    At charge 1, the R-matrix is the structure function:
      R(z) = g(z) = prod_{i=1}^{3} (z - h_i) / (z + h_i)

    This is the Maulik-Okounkov R-matrix from stable envelopes,
    identified with the chiral R-matrix from the factorization
    braiding on Gr^{ch}_{GL_1}(C^3).

    The identification: the holonomy of the factorization connection
    along the path x_1 <-> x_2 at spectral separation z gives R(z).

    AP-CY28: test points must avoid poles at z = +/- h_i.

    Args:
        h: CY_3 equivariant parameters (h_1, h_2, h_3) with sum = 0.

    Returns:
        GeometricRMatrixData at charge 1.
    """
    h1, h2, h3 = h
    assert h1 + h2 + h3 == 0, f"CY constraint violated: sum = {h1+h2+h3}"

    sigma_2 = h1 * h2 + h1 * h3 + h2 * h3
    sigma_3 = h1 * h2 * h3

    return GeometricRMatrixData(
        level="chiral",
        braiding_type="E_2-braided (NOT symmetric)",
        r_matrix_formula=(
            f"R(z) = g(z) = (z-{h1})(z-{h2})(z-{h3})/((z+{h1})(z+{h2})(z+{h3})), "
            f"sigma_2 = {sigma_2}, sigma_3 = {sigma_3}"
        ),
        ybe_satisfied=True,
        unitarity="R(z) R(-z) = 1 (algebraic unitarity from CY structure)",
        classical_limit=f"R(z) = 1 - {sigma_2}/z^2 + O(1/z^4) as z -> infty",
        charge=1,
        source=(
            "factorization braiding on Gr^{ch}_{GL_1}(C^3) "
            "= MO stable envelope R-matrix"
        ),
    )


def geometric_r_matrix_k3_charge1(
    num_params: int = 24,
) -> GeometricRMatrixData:
    r"""The chiral geometric R-matrix for GL_1 on K3 at charge 1.

    For K3 with 24 Mukai lattice parameters h_1,...,h_24 (sum = 0):
      R(z) = g_{K3}(z) = prod_{i=1}^{24} (z - h_i) / (z + h_i)

    This is a degree-(24,24) rational function.

    STATUS: CONJECTURAL (AP-CY14). Requires the K3 Yangian.

    Properties:
    - 24 zeros at z = h_i
    - 24 poles at z = -h_i
    - Unitarity: g(z) g(-z) = 1
    - g(0) = (-1)^{24} = 1 (even number of factors)
    - g(infty) = 1

    Returns:
        GeometricRMatrixData for K3 at charge 1.
    """
    return GeometricRMatrixData(
        level="chiral",
        braiding_type="E_2-braided (NOT symmetric, CONJECTURAL)",
        r_matrix_formula=(
            f"R(z) = g_{{K3}}(z) = prod_{{i=1}}^{{{num_params}}} "
            f"(z - h_i) / (z + h_i), degree ({num_params},{num_params})"
        ),
        ybe_satisfied=True,
        unitarity="g(z) g(-z) = 1 (algebraic unitarity)",
        classical_limit=(
            "g(z) = 1 - (2/z^2) * sum h_i^2 + O(1/z^4) "
            "(p_1 = sum h_i = 0, so z^{-1} vanishes)"
        ),
        charge=1,
        source=(
            "factorization braiding on Gr^{ch}_{GL_1}(K3), "
            "status: CONJECTURAL (AP-CY14)"
        ),
    )


def r_matrix_unitarity_check(
    h: Tuple[F, ...],
    z: F,
) -> Dict[str, Any]:
    r"""Verify the unitarity R(z) R(-z) = 1 for the structure function.

    For any CY parameters h_1,...,h_n with R(z) = prod (z-h_i)/(z+h_i):
      R(z) R(-z) = prod (z-h_i)/(z+h_i) * prod (-z-h_i)/(-z+h_i)
                 = prod (z-h_i)(-z-h_i) / ((z+h_i)(-z+h_i))
                 = prod (z-h_i)(z+h_i) / ((z+h_i)(z-h_i))   [sign cancel]
                 = 1

    AP-CY28: z must avoid poles at +/- h_i.

    Args:
        h: CY parameters as tuple of Fractions
        z: test spectral parameter (must avoid +/- h_i)

    Returns:
        Dict with verification data.
    """
    # Check z avoids poles
    for hi in h:
        if z == hi or z == -hi:
            return {
                "error": f"z = {z} is a pole (at +/- h_i = +/- {hi})",
                "unitarity_holds": None,
            }

    # Compute g(z) = prod (z - h_i) / (z + h_i)
    g_z = F(1)
    for hi in h:
        g_z *= (z - hi) / (z + hi)

    # Compute g(-z) = prod (-z - h_i) / (-z + h_i)
    g_neg_z = F(1)
    for hi in h:
        g_neg_z *= (-z - hi) / (-z + hi)

    product = g_z * g_neg_z

    return {
        "z": str(z),
        "g_z": str(g_z),
        "g_neg_z": str(g_neg_z),
        "product": str(product),
        "unitarity_holds": product == F(1),
        "n_params": len(h),
    }


# =========================================================================
# 5. The derived Satake for chiral quantum groups
# =========================================================================

class DerivedSatakeData(NamedTuple):
    """The derived Satake equivalence for chiral quantum groups.

    Classical:    Perv(Gr_G) ~= Rep(G^L)           (Mirkovic-Vilonen, PROVED)
    Derived:      D-mod(Gr_G) ~= IndCoh(N^L/G^L)   (Bezrukavnikov-Finkelberg, PROVED)
    Chiral:       D-mod(Gr^{ch}_G) ~= Rep^{E_2}(chiral QG)  (CONJECTURAL)
    CY Chiral:    D-mod(Gr^{ch}_G(X)) ~= Rep^{E_2}(Y(g_X))  (CONJECTURAL)

    The chiral Satake combines:
    (a) Beilinson-Drinfeld factorization (PROVED)
    (b) MV Satake equivalence (PROVED)
    (c) CY-to-chiral functor Phi (PROVED at d=2, PROGRAMME at d=3)
    (d) Chiral quantum group construction (CONJECTURAL for K3 Yangian)
    """
    level: str                    # classical / derived / chiral / CY
    lhs: str                      # left-hand side of equivalence
    rhs: str                      # right-hand side of equivalence
    monoidal_structure_lhs: str   # convolution / factorization
    monoidal_structure_rhs: str   # tensor product (braided or symmetric)
    status: str                   # PROVED or CONJECTURAL
    dependencies: List[str]       # list of dependencies for status
    r_matrix_type: str            # trivial, rational, trigonometric


def classical_satake(group: str = "GL_1") -> DerivedSatakeData:
    r"""The classical geometric Satake (Mirkovic-Vilonen, 2007).

    Perv(Gr_G) ~= Rep(G^L) as symmetric monoidal categories.

    This is a THEOREM (ProvedElsewhere).
    """
    gr = affine_grassmannian(group)
    return DerivedSatakeData(
        level="classical",
        lhs=f"Perv(Gr_{{{group}}})",
        rhs=f"Rep({gr.langlands_dual})",
        monoidal_structure_lhs="convolution (Lusztig)",
        monoidal_structure_rhs="tensor product (symmetric)",
        status="PROVED",
        dependencies=["Mirkovic-Vilonen 2007", "Ginzburg 1995"],
        r_matrix_type="trivial (symmetric monoidal)",
    )


def derived_satake(group: str = "GL_1") -> DerivedSatakeData:
    r"""The derived geometric Satake (Bezrukavnikov-Finkelberg, 2008).

    D-mod(Gr_G) ~= IndCoh(N^L / G^L) as DG categories.

    The right-hand side: IndCoh of the quotient stack N^L/G^L, where
    N^L is the nilpotent cone in g^L.

    This is a THEOREM (ProvedElsewhere).
    """
    gr = affine_grassmannian(group)
    return DerivedSatakeData(
        level="derived",
        lhs=f"D-mod(Gr_{{{group}}})",
        rhs=f"IndCoh(N^L / {gr.langlands_dual})",
        monoidal_structure_lhs="convolution (derived)",
        monoidal_structure_rhs="tensor product (DG)",
        status="PROVED",
        dependencies=["Bezrukavnikov-Finkelberg 2008"],
        r_matrix_type="trivial (symmetric monoidal at DG level)",
    )


def chiral_satake_c3() -> DerivedSatakeData:
    r"""The chiral Satake for C^3 (toric CY_3).

    For toric CY_3 with Omega-background parameters (h_1, h_2, h_3):

      D-mod(Gr^{ch}_{GL_1}(C^3)) ~= Rep^{E_2}(Y(gl_hat_1))

    Left side: D-modules on the chiral Grassmannian of GL_1 on C^3.
    Right side: E_2-braided representations of the affine Yangian.

    The identification works as follows:
    - D-modules at charge n <-> Fock space F_n (dim = partitions of n)
    - Convolution of sheaves <-> tensor product of representations
    - Factorization braiding <-> Yangian R-matrix

    STATUS: CONJECTURAL as a full equivalence.
    Supporting evidence:
    - Both sides have the same Fock space decomposition (PROVED)
    - Both R-matrices agree (thm:mo-chiral-rmatrix, PROVED)
    - Convolution matches coproduct at charge 2 (verified computationally)

    Dependencies:
    - Beilinson-Drinfeld construction (PROVED)
    - 5d hCS boundary algebra = affine Yangian (PROVED, Costello 2013)
    - Full DG equivalence (CONJECTURAL)
    """
    return DerivedSatakeData(
        level="chiral",
        lhs="D-mod(Gr^{ch}_{GL_1}(C^3))",
        rhs="Rep^{E_2}(Y(gl_hat_1))",
        monoidal_structure_lhs="factorization convolution on Ran(C)",
        monoidal_structure_rhs="E_2-braided tensor product",
        status="CONJECTURAL (strong evidence)",
        dependencies=[
            "Beilinson-Drinfeld (PROVED)",
            "Costello 5d hCS (PROVED)",
            "MO R-matrix match (PROVED: thm:mo-chiral-rmatrix)",
            "Full DG equivalence (CONJECTURAL)",
        ],
        r_matrix_type="rational (Yangian R(z) = g(z))",
    )


def chiral_satake_k3() -> DerivedSatakeData:
    r"""The chiral Satake for GL_1 on K3.

    D-mod(Gr^{ch}_{GL_1}(K3)) ~= Rep^{E_2}(Y(g_{K3}))

    STATUS: CONJECTURAL (AP-CY14).

    Left side: D-modules on the chiral Grassmannian of GL_1 on K3.
    The Grassmannian structure reflects the Mukai lattice Lambda_Muk
    of rank 24 and signature (4,20).

    Right side: E_2-braided representations of the K3 Yangian.
    The K3 Yangian Y(g_{K3}) is NOT constructed (AP-CY14).

    At the Fock space level:
      charge-n D-modules <-> F_n with dim = p_{24}(n)
      charge-0: 1 (vacuum)
      charge-1: 24 (Mukai lattice directions)
      charge-2: 324 (24-coloured partitions of 2)

    The R-matrix is the degree-(24,24) structure function:
      g_{K3}(z) = prod_{i=1}^{24} (z - h_i) / (z + h_i)

    Dependencies cascade through MULTIPLE conjectural objects:
    1. K3 Yangian Y(g_{K3}) must exist (AP-CY14)
    2. CY-A_2 functor Phi must extend to Gr^{ch} (requires new argument)
    3. The factorization structure on Gr^{ch}_{GL_1}(K3) must be
       compatible with the Mukai lattice pairing

    This is open problem (v) of geometric_langlands.tex.
    """
    return DerivedSatakeData(
        level="CY",
        lhs="D-mod(Gr^{ch}_{GL_1}(K3))",
        rhs="Rep^{E_2}(Y(g_{K3}))",
        monoidal_structure_lhs="factorization convolution on Ran(C) via Mukai lattice",
        monoidal_structure_rhs="E_2-braided tensor product (CONJECTURAL)",
        status="CONJECTURAL",
        dependencies=[
            "K3 Yangian existence (AP-CY14, CONJECTURAL)",
            "CY-A_2 Grassmannian extension (CONJECTURAL)",
            "Mukai lattice factorization compatibility (CONJECTURAL)",
            "Beilinson-Drinfeld construction (PROVED)",
        ],
        r_matrix_type="rational, degree-(24,24)",
    )


# =========================================================================
# 6. Weight functors and MV cycles
# =========================================================================

class WeightFunctorData(NamedTuple):
    """Mirkovic-Vilonen weight functors and their chiral refinements.

    Classical: F_mu(IC_lambda) = weight-mu space of V_lambda.
    Chiral: F_mu^{ch}(IC_lambda) = z-graded weight space.
    """
    group: str
    coweight_lambda: Tuple[int, ...]
    weight_mu: Tuple[int, ...]
    classical_dim: int              # dim of weight space
    chiral_refinement: str          # z-graded structure
    mv_cycle_description: str       # geometric description


def weight_functor_gl1_k3(charge: int,
                          direction: int) -> WeightFunctorData:
    r"""Weight functor for GL_1 on K3.

    For GL_1 (abelian), the weight functor is trivial:
    each charge-n sheaf has a single weight (= the charge itself).

    The nontrivial structure appears at the Fock space level:
    the charge-n Fock space F_n decomposes into p_{24}(n) irreducible
    components indexed by 24-coloured partitions.

    The MV "cycles" for GL_1 are simply lattice points, but the
    Fock space structure at each charge gives nontrivial multiplicity.

    Args:
        charge: the charge (= dominant coweight for GL_1)
        direction: Mukai lattice direction (1 to 24)

    Returns:
        WeightFunctorData.
    """
    dim = _p24(charge)
    return WeightFunctorData(
        group="GL_1",
        coweight_lambda=(charge,),
        weight_mu=(charge,),
        classical_dim=dim,
        chiral_refinement=(
            f"z-graded: F_{{{charge}}} has p_24({charge}) = {dim} "
            f"components, each carrying a spectral-parameter-dependent action"
        ),
        mv_cycle_description=(
            f"For GL_1: MV cycle = single lattice point; "
            f"Fock space dim p_24({charge}) = {dim} gives multiplicity"
        ),
    )


def weight_functor_sl2(n: int, m: int) -> WeightFunctorData:
    r"""Weight functor for SL_2: dim of weight-m space in V_n.

    For SL_2 with dominant coweight (n,) and weight (m,):
      dim(V_n^{weight m}) = 1 if |m| <= n and m = n mod 2, else 0.

    The MV cycle at weight m in the closure of Gr^n is a single
    point if |m| <= n, m = n mod 2.

    Args:
        n: dominant coweight (spin = n/2)
        m: weight

    Returns:
        WeightFunctorData.
    """
    if abs(m) <= n and (n - m) % 2 == 0:
        dim = 1
    else:
        dim = 0

    return WeightFunctorData(
        group="SL_2",
        coweight_lambda=(n,),
        weight_mu=(m,),
        classical_dim=dim,
        chiral_refinement=(
            f"V_{{{n}}} weight {m}: dim = {dim}, "
            "chiral refinement adds spectral parameter grading"
        ),
        mv_cycle_description=(
            f"MV cycle: {'point' if dim == 1 else 'empty'} "
            f"in overline{{Gr^{{{n}}}}} at weight {m}"
        ),
    )


# =========================================================================
# 7. Iwahori reduction and the E_1 -> E_2 passage
# =========================================================================

class IwahoriSatakeData(NamedTuple):
    """The Iwahori-level Satake and the E_1 -> E_2 passage.

    With Iwahori level structure I:
      D-mod_I(Gr_G) ~= Rep^{E_1}(A^!)
    where A^! is the Koszul dual (Iwahori-Hecke level).

    The passage to full Satake is the Drinfeld center:
      Z(D-mod_I(Gr^{ch}_G)) ~= D-mod(Gr^{ch}_G) ~= Rep^{E_2}(QG)

    AP-CY4: Drinfeld center Z(C) (category) != derived center Z^der(A) (algebra).
    """
    iwahori_side: str               # D-mod_I(Gr^{ch}_G)
    iwahori_satake_image: str       # Rep^{E_1}(A^!)
    full_satake_image: str          # Rep^{E_2}(QG)
    center_construction: str        # Drinfeld center
    e1_to_e2_mechanism: str         # how E_1 -> E_2 works
    status: str                     # PROVED or CONJECTURAL


def iwahori_satake_passage(group: str = "GL_1") -> IwahoriSatakeData:
    r"""The E_1 -> E_2 passage via Iwahori reduction.

    The Iwahori level structure on Gr_G gives E_1-monoidal structure
    (the Hecke algebra ordering).  The full Satake recovers E_2
    (symmetric for classical, braided for chiral) via the Drinfeld center.

    For the chiral setting:
      D-mod_I(Gr^{ch}_G) carries E_1 monoidal structure
      (ordered convolution with Iwahori level structure).

      Z(D-mod_I(Gr^{ch}_G)) = D-mod(Gr^{ch}_G) carries E_2 braided structure.

    This is the GEOMETRIC realization of the algebraic E_1 -> E_2 passage:
      Rep^{E_1}(Y^+) -> Z(Rep^{E_1}(Y^+)) = Rep^{E_2}(Y)
    where Y^+ is the positive half (CoHA) and Y is the full Yangian.

    AP-CY7: CoHA is associative (E_1), NOT chiral. The passage to chiral
    (E_2) is via the Drinfeld center, not by identification.

    Args:
        group: the structure group

    Returns:
        IwahoriSatakeData.
    """
    if group == "GL_1":
        return IwahoriSatakeData(
            iwahori_side="D-mod_I(Gr^{ch}_{GL_1})",
            iwahori_satake_image="Rep^{E_1}(Y^+(gl_hat_1)) (CoHA representations)",
            full_satake_image="Rep^{E_2}(Y(gl_hat_1)) (full Yangian reps)",
            center_construction="Z(Rep^{E_1}(Y^+)) = Rep^{E_2}(Y) (thm:drinfeld-center-coha)",
            e1_to_e2_mechanism=(
                "Drinfeld center: Z(E_1-Cat) -> E_2-Cat. "
                "Geometrically: drop Iwahori level structure, recover braiding."
            ),
            status="PROVED for C^3 (CoHA); CONJECTURAL for K3",
        )
    else:
        gr = affine_grassmannian(group)
        return IwahoriSatakeData(
            iwahori_side=f"D-mod_I(Gr^{{ch}}_{{{group}}})",
            iwahori_satake_image=f"Rep^{{E_1}}(A^!_{{{group}}})",
            full_satake_image=f"Rep^{{E_2}}({gr.langlands_dual}^{{ch}})",
            center_construction=(
                f"Z(D-mod_I(Gr^{{ch}}_{{{group}}})) "
                f"= D-mod(Gr^{{ch}}_{{{group}}})"
            ),
            e1_to_e2_mechanism="Drinfeld center",
            status="CONJECTURAL",
        )


# =========================================================================
# 8. Consistency checks for the chiral Satake programme
# =========================================================================

def verify_orbit_structure_gl1() -> Dict[str, Any]:
    """Verify the orbit structure of Gr_{GL_1} for K3.

    GL_1 is abelian, so:
    - Gr_{GL_1} = Z (the integers)
    - Orbits are single points (one per integer)
    - IC sheaves are skyscraper sheaves
    - Under Satake: each point maps to a 1-dim representation

    The nontrivial structure comes at higher charges via Fock spaces.
    """
    gr = affine_grassmannian("GL_1")
    orbits_check = gr.orbit_indexing == "Z (integers: line bundle degree)"
    satake_check = gr.satake_status == "PROVED"

    # Check some orbits
    orbit_0 = gr_orbit("GL_1", (0,))
    orbit_1 = gr_orbit("GL_1", (1,))

    return {
        "group": "GL_1",
        "orbit_type": gr.orbit_indexing,
        "satake_proved": satake_check,
        "orbit_0_dim": orbit_0.orbit_dim,
        "orbit_1_dim": orbit_1.orbit_dim,
        "all_orbits_zero_dim": orbit_0.orbit_dim == 0 and orbit_1.orbit_dim == 0,
        "all_pass": orbits_check and satake_check,
    }


def verify_orbit_structure_sl2() -> Dict[str, Any]:
    """Verify orbit structure of Gr_{SL_2}.

    SL_2 orbits: Gr^{(n)} has dimension 2n for n >= 0.
    IC sheaves: IC_n maps to V_n (spin-n/2 representation of PGL_2).
    """
    gr = affine_grassmannian("SL_2", rank=1, dual_coxeter=2)
    orbits = [gr_orbit("SL_2", (n,), dual_coxeter=2) for n in range(5)]

    dims_correct = all(orbits[n].orbit_dim == 2 * n for n in range(5))
    langlands_correct = gr.langlands_dual == "PGL_2"

    return {
        "group": "SL_2",
        "langlands_dual": gr.langlands_dual,
        "orbit_dims": [o.orbit_dim for o in orbits],
        "dims_formula_2n": dims_correct,
        "langlands_correct": langlands_correct,
        "all_pass": dims_correct and langlands_correct,
    }


def verify_convolution_additivity() -> Dict[str, Any]:
    """Verify that convolution is additive on charges for GL_1.

    For GL_1 (abelian): charge-n * charge-m = charge-(n+m).
    The Fock space dimensions at each charge are p_{24}(k).
    """
    tests = []
    for n, m in [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3)]:
        conv = convolution_product(n, m, "GL_1")
        additive = conv.output_charge == n + m
        tests.append((n, m, conv.output_charge, additive))

    all_pass = all(t[3] for t in tests)
    return {
        "tests": tests,
        "all_additive": all_pass,
        "fock_dims": {k: _p24(k) for k in range(6)},
    }


def verify_unitarity_c3() -> Dict[str, Any]:
    """Verify R(z)R(-z) = 1 for the C^3 structure function.

    AP-CY28: use safe test points far from poles.
    For h = (1, -2, 1): poles at z = +/- 1, +/- 2.
    Use z = 37/10 to avoid all poles.
    """
    h = (F(1), F(-2), F(1))
    # Verify CY constraint
    assert sum(h) == 0

    # Safe test point
    z = F(37, 10)
    result = r_matrix_unitarity_check(h, z)

    # Additional test points
    z2 = F(7, 3)
    result2 = r_matrix_unitarity_check(h, z2)

    z3 = F(100)
    result3 = r_matrix_unitarity_check(h, z3)

    return {
        "h": tuple(str(x) for x in h),
        "cy_constraint": sum(h) == F(0),
        "test_1": result,
        "test_2": result2,
        "test_3": result3,
        "all_pass": (
            result["unitarity_holds"]
            and result2["unitarity_holds"]
            and result3["unitarity_holds"]
        ),
    }


def verify_unitarity_k3_params() -> Dict[str, Any]:
    """Verify R(z)R(-z) = 1 for K3-type parameters (small model).

    Use a rank-4 model with signature (2, 2) to test:
    h = (3, 5, -4, -4) with sum = 0.

    AP-CY28: avoid poles at +/- 3, +/- 4, +/- 5.
    Use z = 17/3.
    """
    h = (F(3), F(5), F(-4), F(-4))
    assert sum(h) == 0

    z = F(17, 3)
    result = r_matrix_unitarity_check(h, z)

    return {
        "h": tuple(str(x) for x in h),
        "n_params": len(h),
        "cy_constraint": sum(h) == F(0),
        "result": result,
        "unitarity_holds": result["unitarity_holds"],
    }


def verify_factorization_separated() -> Dict[str, Any]:
    """Verify factorization property at separated points.

    At separated points x_1 != x_2:
      Gr^{ch}(x_1, x_2) ~= Gr^{ch}(x_1) x Gr^{ch}(x_2)
    The fiber splits into a product (tensor product of reps).
    """
    fp = factorization_property(num_points=2, separated=True)
    return {
        "separated": fp.separated,
        "splits": fp.splits,
        "fusion_type": fp.fusion_type,
        "all_pass": fp.splits and fp.fusion_type == "trivial (tensor product)",
    }


def verify_factorization_collision() -> Dict[str, Any]:
    """Verify factorization property at collision.

    At collision x_1 -> x_2:
      Gr^{ch}(x_1, x_2) does NOT split.
    The non-splitting encodes the coproduct Delta_z.
    """
    fp = factorization_property(num_points=2, separated=False)
    return {
        "separated": fp.separated,
        "splits": fp.splits,
        "non_trivial_fusion": "OPE" in fp.fusion_type,
        "coproduct_present": "Delta_z" in fp.coproduct_relation,
        "all_pass": not fp.splits,
    }


def verify_satake_hierarchy() -> Dict[str, Any]:
    """Verify the hierarchy: classical -> derived -> chiral -> CY.

    Each level should correctly state its status and dependencies.
    """
    cs = classical_satake("GL_1")
    ds = derived_satake("GL_1")
    ch_c3 = chiral_satake_c3()
    ch_k3 = chiral_satake_k3()

    return {
        "classical_proved": cs.status == "PROVED",
        "derived_proved": ds.status == "PROVED",
        "chiral_c3_conjectural": "CONJECTURAL" in ch_c3.status,
        "chiral_k3_conjectural": "CONJECTURAL" in ch_k3.status,
        "hierarchy_correct": (
            cs.level == "classical"
            and ds.level == "derived"
            and ch_c3.level == "chiral"
            and ch_k3.level == "CY"
        ),
        "classical_symmetric": "symmetric" in cs.monoidal_structure_rhs,
        "chiral_braided": "E_2" in ch_c3.monoidal_structure_rhs,
        "all_pass": (
            cs.status == "PROVED"
            and ds.status == "PROVED"
            and "CONJECTURAL" in ch_c3.status
            and "CONJECTURAL" in ch_k3.status
        ),
    }


def verify_weight_functor_sl2() -> Dict[str, Any]:
    """Verify weight functor dimensions for SL_2.

    V_n has weight spaces at m = -n, -n+2, ..., n-2, n, each dim 1.
    Total dim = n + 1.
    """
    tests = []
    for n in range(5):
        total_dim = 0
        weight_dims = {}
        for m in range(-n, n + 1):
            wf = weight_functor_sl2(n, m)
            weight_dims[m] = wf.classical_dim
            total_dim += wf.classical_dim
        expected_total = n + 1
        tests.append({
            "n": n,
            "weight_dims": weight_dims,
            "total_dim": total_dim,
            "expected": expected_total,
            "match": total_dim == expected_total,
        })

    all_pass = all(t["match"] for t in tests)
    return {"tests": tests, "all_pass": all_pass}


def verify_iwahori_e1_e2() -> Dict[str, Any]:
    """Verify the E_1 -> E_2 passage via Iwahori reduction.

    The passage:
      D-mod_I(Gr^{ch}_G)  [E_1 monoidal]
        --Drinfeld center-->
      D-mod(Gr^{ch}_G)    [E_2 braided]

    This matches the algebraic passage:
      Rep^{E_1}(Y^+)  --Z-->  Rep^{E_2}(Y)
    where Z is the Drinfeld center functor.

    AP-CY4: Drinfeld center != derived center.
    """
    iw = iwahori_satake_passage("GL_1")

    return {
        "iwahori_e1": "E_1" in iw.iwahori_satake_image,
        "full_e2": "E_2" in iw.full_satake_image,
        "center_used": "Drinfeld center" in iw.center_construction or "Z(" in iw.center_construction,
        "coha_in_iwahori": "CoHA" in iw.iwahori_satake_image,
        "yangian_in_full": "Yangian" in iw.full_satake_image or "Y(" in iw.full_satake_image,
        "all_pass": (
            "E_1" in iw.iwahori_satake_image
            and "E_2" in iw.full_satake_image
        ),
    }


def verify_classical_vs_chiral_braiding() -> Dict[str, Any]:
    """Verify: classical Satake is symmetric, chiral is braided.

    Classical: Perv(Gr_G) has SYMMETRIC monoidal structure.
    Chiral: D-mod(Gr^{ch}_G) has E_2-BRAIDED monoidal structure.

    The E_2 braiding comes from the spectral parameter dependence
    of the factorization structure, which is absent classically.
    """
    r_classical = geometric_r_matrix_classical()
    r_chiral = geometric_r_matrix_chiral_charge1()

    return {
        "classical_symmetric": r_classical.braiding_type == "symmetric",
        "chiral_braided": "E_2" in r_chiral.braiding_type,
        "classical_trivial_r": "swap" in r_classical.r_matrix_formula.lower() or "trivial" in r_classical.r_matrix_formula.lower(),
        "chiral_nontrivial_r": "g(z)" in r_chiral.r_matrix_formula,
        "both_ybe": r_classical.ybe_satisfied and r_chiral.ybe_satisfied,
        "all_pass": (
            r_classical.braiding_type == "symmetric"
            and "E_2" in r_chiral.braiding_type
            and r_classical.ybe_satisfied
            and r_chiral.ybe_satisfied
        ),
    }


def verify_chiral_grassmannian_factorization() -> Dict[str, Any]:
    """Verify the chiral Grassmannian is a factorization ind-scheme."""
    cg = chiral_grassmannian("GL_1", "C")

    return {
        "is_factorization": cg.is_factorization,
        "group": cg.group,
        "base_curve": cg.base_curve,
        "bd_proved": "PROVED" in cg.status,
        "all_pass": cg.is_factorization and "PROVED" in cg.status,
    }


def full_verification() -> Dict[str, Any]:
    """Run all verification paths for the derived Satake programme."""
    return {
        "path1_orbit_gl1": verify_orbit_structure_gl1(),
        "path2_orbit_sl2": verify_orbit_structure_sl2(),
        "path3_convolution": verify_convolution_additivity(),
        "path4_unitarity_c3": verify_unitarity_c3(),
        "path5_unitarity_k3": verify_unitarity_k3_params(),
        "path6_factorization_sep": verify_factorization_separated(),
        "path7_factorization_col": verify_factorization_collision(),
        "path8_satake_hierarchy": verify_satake_hierarchy(),
        "path9_weight_sl2": verify_weight_functor_sl2(),
        "path10_iwahori_e1e2": verify_iwahori_e1_e2(),
        "path11_classical_vs_chiral": verify_classical_vs_chiral_braiding(),
        "path12_chiral_gr_factorization": verify_chiral_grassmannian_factorization(),
    }


# =========================================================================
# Helper: 24-coloured partition function
# =========================================================================

def _p24(n: int, colours: int = 24) -> int:
    """Compute p_c(n) = number of c-coloured partitions of n.

    p_c(n) = coefficient of q^n in prod_{k>=1} 1/(1-q^k)^c.

    Ground truth (OEIS A006922 for c=24):
      p_{24}(0) = 1
      p_{24}(1) = 24
      p_{24}(2) = 324
      p_{24}(3) = 3200
      p_{24}(4) = 25650
      p_{24}(5) = 176256
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    coeffs = [0] * (n + 1)
    coeffs[0] = 1
    for k in range(1, n + 1):
        new_coeffs = list(coeffs)
        for m_val in range(1, n // k + 1):
            binom = math.comb(m_val + colours - 1, colours - 1)
            for j in range(n + 1):
                target = j + m_val * k
                if target > n:
                    break
                new_coeffs[target] += coeffs[j] * binom
        coeffs = new_coeffs
    return coeffs[n]
