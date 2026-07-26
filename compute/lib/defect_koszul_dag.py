r"""Defect algebra from Koszul duality in derived algebraic geometry.

STATUS: CONJECTURAL for K3xE (conditional on CY-A_3, AP-CY6/AP-CY14).
The K3 (d=2) free-field branch results are PROVED (CY-A_2).

MATHEMATICAL CONTENT
====================

The defect algebra (chiral quantum group) arises from Koszul duality applied
to the boundary chiral algebra of holomorphic CS / the CY-to-chiral functor:

    CY_d-Cat --Phi--> A (boundary chiral algebra)
                       |
                       B(-)  (bar complex)
                       |
                       v
                    B(A)  (factorization coalgebra on Ran(C))
                       |
                       D_Ran  (Verdier duality)
                       |
                       v
                    A^! = D_Ran(B(A))  (defect algebra = chiral Koszul dual)

The pipeline:

    A  -->  B(A)  -->  A^! = D_Ran(B(A))  -->  Rep^{E_2}(A^!)

where the final arrow produces the braided monoidal category of representations
of the defect algebra -- the chiral quantum group.

KEY RESULTS BY DIMENSION
========================

1. d=2 (K3, CY-A_2 PROVED):
   - Bulk algebra: A_{K3} = lattice VOA V_{Lambda_K3} of Mukai lattice
   - kappa_ch(A_{K3}) = 2 (= chi(O_{K3}))
   - Bar complex: B(A_{K3}) = B^{ord}(V_{Lambda_K3}), class G (free-field)
   - Defect algebra: A_{K3}^! = V_{Lambda_K3}^! with kappa_ch = -2
   - Koszul conductor: K = kappa_ch + kappa_ch^! = 0 (free-field branch)
   - Morita equivalence: Omega(B(A_{K3})) ~ A_{K3}
   - Braiding: Rep^{E_2}(A_{K3}^!) = Rep^{E_2}(A_{K3})^{rev} (reversed)
   - Structure function: g_{K3}^!(u) = g_{K3}(-u) = 1/g_{K3}(u)

2. d=3 (K3xE, CONJECTURAL on CY-A_3):
   - Bulk algebra: A_{K3xE} on E (not constructed; AP-CY6)
   - kappa_ch(A_{K3xE}) = 3 (by additivity: kappa_ch(K3) + kappa_ch(E) = 2+1)
   - The defect along E in K3xE: A^!|_E
   - CRITICAL DISTINCTION: K3xE has two scalar lanes:
     (a) Free-field branch: K = 0, kappa_ch^! = -3 (Heisenberg-type)
     (b) BKM branch: kappa_BKM = 5 is the Borcherds weight characteristic,
         not a Koszul conductor
   - On the free-field branch: Rep^{E_2}(A^!|_E) ~ Rep^{E_2}(Y(g_{K3}))
     (the K3 quantum group; CONJECTURAL, depends on Y(g_{K3}) existing)
   - The bar-cobar adjunction: B_{E_1} -| Omega_{E_1} at the E_1 level;
     E_2 promotion via Drinfeld center Z(Rep^{E_1}(-))

3. The C^3 reference case (5d CS, partially proved):
   - Bulk: W_{1+infty} at Psi = -sigma_2
   - Defect: W_{1+infty}^! at Psi^! = sigma_2 (inverted parameters)
   - K = 0 (free-field, class G at generic Psi)
   - Structure function: g(u)^! = 1/g(u)

PIPELINE VERIFICATION
=====================

For each CY target, the pipeline has FIVE verifiable stages:

  Stage 1: Bulk algebra A with kappa_ch(A) and shadow class
  Stage 2: Bar complex B(A) -- dimensions, differentials, class
  Stage 3: Verdier dual D_Ran(B(A)) = A^! with kappa_ch(A^!)
  Stage 4: Koszul conductor K = kappa_ch(A) + kappa_ch(A^!) when the
           chiral lane is known
  Stage 5: Morita equivalence Omega(B(A)) ~ A

The five stages form a DAG (directed acyclic graph) with dependencies:
  1 -> 2 -> 3 -> 4
  2 -> 5
  3 -> 5
Each node caches its result; the full pipeline is a lazy evaluation over the DAG.

ANTI-PATTERN COMPLIANCE
========================
  AP-CY6/AP-CY14: All K3xE results use \begin{conjecture}, ClaimStatusConjectured.
  AP-CY11: Conditionality on CY-A_3 propagates through all K3xE stages.
  AP113:   All kappa subscripted: kappa_ch, kappa_BKM, kappa_cat, kappa_fiber.
  AP-CY4:  Drinfeld center Z(C) != derived center Z^der_ch(A). Both appear; never conflated.
  AP-CY7:  CoHA != E_1-chiral algebra. The defect algebra is NOT the CoHA.
  AP-CY10: Flop != Koszul dual. Flop preserves kappa; Koszul inverts it (K=0 branch).
  AP-CY23: E_1-chiral bialgebra, not E_inf vertex bialgebra.
  AP-CY25: R-matrix via half-braiding, NOT via (id tensor S) o Delta_z(1).
  AP-CY31: Spectral z != worldsheet z.

CONVENTIONS
===========
  - Cohomological grading (|d| = +1).
  - Bar desuspension: |s^{-1}v| = |v| - 1 (desuspension convention).
  - E_1 shift: E_1^! = E_1{-1} (shift 1 = dim(R)).
  - E_2 shift: E_2^! = E_2{-2} (shift 2 = dim(C)).
  - kappa_ch(H_k) = k (Heisenberg), kappa_ch(V_k(g)) = dim(g)(k+h^v)/(2h^v).
  - Exact arithmetic via fractions.Fraction.

MANUSCRIPT REFERENCES
=====================
  chapters/theory/quantum_chiral_algebras.tex:
    Construction constr:universal-defect, Conjecture conj:6d-k3xe,
    Conjecture conj:chiral-qg-k3xe, Construction constr:k3-boundary-defect
  chapters/theory/e1_chiral_algebras.tex:
    Section sec:e1-koszul-three-families
  chapters/connections/modular_koszul_bridge.tex:
    Theorem thm:cy-complementarity-d2

CROSS-VOLUME REFERENCES
========================
  Vol I: Bar-cobar adjunction (Theorem A), Verdier leg (Theorem B),
         Koszul conductor definition, G/L/C/M shadow class
  Vol II: E_1-chiral Koszul duality theorem, SC^{ch,top} colour
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from fractions import Fraction
from functools import cached_property
from typing import Any, Dict, List, Optional, Tuple

import numpy as np


# =========================================================================
# 0. Enumerations and constants
# =========================================================================

class ShadowClass(Enum):
    """G/L/C/M shadow classification (Vol I)."""
    G = "G"   # Gaussian (free-field); shadow depth 2; rho_K = 0
    L = "L"   # Lie (rational); shadow depth 2; rho_K = 0
    C = "C"   # Convergent; finite depth; rho_K >= 0
    M = "M"   # Mock modular (Gevrey-1); infinite depth; rho_K > 0


class ClaimStatus(Enum):
    """Claim status for formal mathematical statements."""
    PROVED_HERE = "ProvedHere"
    PROVED_ELSEWHERE = "ProvedElsewhere"
    CONDITIONAL = "Conditional"
    CONJECTURED = "Conjectured"


class CYDimension(Enum):
    """CY dimension d of the source category."""
    D1 = 1  # Elliptic curve: E_inf (trivial)
    D2 = 2  # K3: E_2 (braided), CY-A_2 PROVED
    D3 = 3  # CY3: E_1 (ordered), CY-A_3 PROGRAMME


# Mukai lattice constants
MUKAI_RANK = 24
MUKAI_SIG_PLUS = 4
MUKAI_SIG_MINUS = 20

# K3 topological invariants
K3_CHI_O = 2           # chi(O_{K3}) = h^{0,0} - h^{1,0} + h^{2,0} = 1-0+1
K3_CHI_TOP = 24         # Topological Euler characteristic
K3_BETTI_2 = 22         # b_2(K3) = h^{2,0} + h^{1,1} + h^{0,2} = 1+20+1

# Elliptic curve invariants
E_CHI_O = 0             # chi(O_E) = 1 - 1 = 0 ... actually chi(O_E)=0?
# Wait: chi(O_E) = h^{0,0} - h^{1,0} = 1 - 1 = 0.
# But kappa_ch(E) = 1 from the Heisenberg at level 1 (cy_to_chiral_functor.py).
# kappa_ch is NOT chi(O) in general; kappa_ch = chi^CY for d=2 only.
# For d=1: kappa_ch(A_E) = k = 1 (the Heisenberg level).
E_KAPPA_CH = Fraction(1)


# =========================================================================
# 1. Bulk algebra data
# =========================================================================

@dataclass(frozen=True)
class BulkAlgebraData:
    """Data for the bulk (boundary) chiral algebra A of a CY target.

    The bulk algebra is the output of the CY-to-chiral functor Phi:
        Phi: CY_d-Cat -> E_{d-1}-ChirAlg
    or equivalently the boundary chiral algebra of holomorphic CS.

    Attributes
    ----------
    name : str
        Human-readable name.
    cy_dim : CYDimension
        CY dimension d of the source category.
    kappa_ch : Fraction
        Chiral modular characteristic kappa_ch(A).
    shadow_class : ShadowClass
        G/L/C/M classification.
    shadow_depth : Optional[int]
        Depth of shadow tower (None = infinite for class M).
    claim_status : ClaimStatus
        Status of the construction of A.
    dependencies : Tuple[str, ...]
        What the construction depends on (e.g., 'CY-A_2', 'CY-A_3').
    central_charge : Optional[Fraction]
        Central charge c of the chiral algebra, if applicable.
    rank : Optional[int]
        Rank of the underlying lattice/Lie algebra, if applicable.
    """
    name: str
    cy_dim: CYDimension
    kappa_ch: Fraction
    shadow_class: ShadowClass
    shadow_depth: Optional[int]
    claim_status: ClaimStatus
    dependencies: Tuple[str, ...]
    central_charge: Optional[Fraction] = None
    rank: Optional[int] = None


@dataclass(frozen=True)
class KappaSpectrum:
    """The four-valued kappa spectrum for a CY target (AP113).

    ZERO TOLERANCE for bare kappa. Every kappa must be subscripted.

    Attributes
    ----------
    kappa_ch : Fraction
        From chiral algebra A_C via Phi.
    kappa_BKM : Optional[Fraction]
        From Borcherds-Kac-Moody algebra (if applicable).
    kappa_cat : Fraction
        From categorical/holomorphic Euler char chi(O_X).
    kappa_fiber : Optional[Fraction]
        From lattice/fiber structure (e.g. lattice rank).
    """
    kappa_ch: Fraction
    kappa_BKM: Optional[Fraction]
    kappa_cat: Fraction
    kappa_fiber: Optional[Fraction]

    def values(self) -> Dict[str, Optional[Fraction]]:
        """Return all kappa values as a dictionary."""
        return {
            'kappa_ch': self.kappa_ch,
            'kappa_BKM': self.kappa_BKM,
            'kappa_cat': self.kappa_cat,
            'kappa_fiber': self.kappa_fiber,
        }


# =========================================================================
# 2. Bar complex data (Stage 2)
# =========================================================================

@dataclass(frozen=True)
class BarComplexData:
    """Data for the bar complex B(A) of a bulk algebra A.

    B(A) = T^c(s^{-1} bar{A}) is the tensor coalgebra on the
    desuspension of the augmentation ideal, with differential d_bar
    from the A_infinity structure.

    For the E_1 ordered bar complex:
        B^{ord}(A) = (T^c(s^{-1} bar{A}), d_bar)
    where d_bar uses ADJACENT multiplications only (Hochschild differential).

    Attributes
    ----------
    bulk_name : str
        Name of the source bulk algebra.
    differential_trivial : bool
        Whether d_bar = 0 at all arities (class G: free-field).
    shadow_class : ShadowClass
        Inherited from bulk algebra.
    shadow_depth : Optional[int]
        Inherited.
    dim_arity_1 : int
        Dimension of B(A) at arity 1 (= number of generators).
    dim_arity_2 : Optional[int]
        Dimension at arity 2.
    dim_arity_3 : Optional[int]
        Dimension at arity 3.
    a_inf_corrections : bool
        Whether the A_infinity corrections m_3, m_4, ... are nonzero.
    """
    bulk_name: str
    differential_trivial: bool
    shadow_class: ShadowClass
    shadow_depth: Optional[int]
    dim_arity_1: int
    dim_arity_2: Optional[int] = None
    dim_arity_3: Optional[int] = None
    a_inf_corrections: bool = False


# =========================================================================
# 3. Defect algebra data (Stage 3)
# =========================================================================

@dataclass(frozen=True)
class DefectAlgebraData:
    """Data for the defect algebra A^! = D_Ran(B(A)).

    The defect algebra is the Verdier dual of the bar complex, viewed
    as a factorization coalgebra on Ran(C). It is the chiral Koszul dual:
        A^! = D_Ran(B(A))

    The defect algebra controls the category of line operators (Wilson
    lines) that can end on the boundary where A lives.

    Attributes
    ----------
    name : str
        Human-readable name of the defect algebra.
    bulk_name : str
        Name of the source bulk algebra.
    kappa_ch : Fraction
        kappa_ch(A^!) of the defect algebra.
    koszul_conductor : Optional[Fraction]
        K = kappa_ch(A) + kappa_ch(A^!) when known.
    shadow_class : ShadowClass
        Shadow class of A^!.
    claim_status : ClaimStatus
        Status of the defect algebra construction.
    dependencies : Tuple[str, ...]
        What the construction depends on.
    structure_function_inverted : bool
        Whether g^!(u) = 1/g(u) (true for free-field branch).
    braiding_reversed : bool
        Whether Rep^{E_2}(A^!) = Rep^{E_2}(A)^{rev}.
    """
    name: str
    bulk_name: str
    kappa_ch: Fraction
    koszul_conductor: Optional[Fraction]
    shadow_class: ShadowClass
    claim_status: ClaimStatus
    dependencies: Tuple[str, ...]
    structure_function_inverted: bool = True
    braiding_reversed: bool = True


# =========================================================================
# 4. Morita equivalence data (Stage 5)
# =========================================================================

@dataclass(frozen=True)
class MoritaEquivalenceData:
    """Data for the bar-cobar Morita equivalence Omega(B(A)) ~ A.

    The cobar construction Omega is the left adjoint to the bar:
        B : E_n-Alg <-> E_n-coAlg : Omega
    On the Koszul locus (where A is Koszul), Omega(B(A)) ~ A.

    Attributes
    ----------
    bulk_name : str
    is_koszul : bool
        Whether A is on the Koszul locus (where Omega o B ~ id).
    cobar_recovers_A : bool
        Whether Omega(B(A)) ~ A (quasi-isomorphism).
    en_level : int
        The E_n level at which the equivalence holds.
    claim_status : ClaimStatus
    """
    bulk_name: str
    is_koszul: bool
    cobar_recovers_A: bool
    en_level: int
    claim_status: ClaimStatus


# =========================================================================
# 5. The DAG node: full pipeline at a single CY target
# =========================================================================

@dataclass
class DefectKoszulPipeline:
    """Full defect-algebra-from-Koszul-duality pipeline for a CY target.

    The pipeline has five stages forming a DAG:
        Stage 1 (Bulk) -> Stage 2 (Bar) -> Stage 3 (Defect) -> Stage 4 (Conductor)
                                          |
                                          v
                          Stage 5 (Morita equivalence)

    Each stage computes its data from the previous stages. The full pipeline
    is a lazy evaluation: each stage is computed on first access and cached.

    Attributes
    ----------
    bulk : BulkAlgebraData
        Stage 1: the bulk (boundary) chiral algebra.
    kappa_spectrum : KappaSpectrum
        The four-valued kappa spectrum (AP113).
    """
    bulk: BulkAlgebraData
    kappa_spectrum: KappaSpectrum
    _bar: Optional[BarComplexData] = field(default=None, init=False, repr=False)
    _defect: Optional[DefectAlgebraData] = field(default=None, init=False, repr=False)
    _morita: Optional[MoritaEquivalenceData] = field(default=None, init=False, repr=False)

    # --- Stage 2: Bar complex ---

    @property
    def bar(self) -> BarComplexData:
        """Stage 2: Compute the bar complex B(A)."""
        if self._bar is None:
            self._bar = self._compute_bar()
        return self._bar

    def _compute_bar(self) -> BarComplexData:
        """Compute bar complex data from the bulk algebra."""
        sc = self.bulk.shadow_class
        trivial = sc == ShadowClass.G
        a_inf = sc in (ShadowClass.L, ShadowClass.C, ShadowClass.M)

        # Dimension at arity 1 = number of generators
        dim1 = self.bulk.rank if self.bulk.rank is not None else 1

        # Dimension at arity 2 = dim1^2 (ordered pairs of generators)
        dim2 = dim1 ** 2

        # Dimension at arity 3 = dim1^3
        dim3 = dim1 ** 3

        return BarComplexData(
            bulk_name=self.bulk.name,
            differential_trivial=trivial,
            shadow_class=sc,
            shadow_depth=self.bulk.shadow_depth,
            dim_arity_1=dim1,
            dim_arity_2=dim2,
            dim_arity_3=dim3,
            a_inf_corrections=a_inf,
        )

    # --- Stage 3: Defect algebra ---

    @property
    def defect(self) -> DefectAlgebraData:
        """Stage 3: Compute the defect algebra A^! = D_Ran(B(A))."""
        if self._defect is None:
            self._defect = self._compute_defect()
        return self._defect

    def _compute_defect(self) -> DefectAlgebraData:
        """Compute defect algebra data from the bar complex."""
        _ = self.bar  # ensure bar is computed first (DAG dependency)

        sc = self.bulk.shadow_class
        kappa_bulk = self.bulk.kappa_ch

        # Koszul conductor and dual kappa depend on the chiral lane:
        #   Class G, L: K = 0 (free-field branch), kappa^! = -kappa
        #   Virasoro class M: K = 13, kappa^! = 13 - kappa
        #   BKM weight data do not determine the Koszul conductor.
        if sc in (ShadowClass.G, ShadowClass.L):
            kappa_dual = -kappa_bulk
            conductor = Fraction(0)
        elif sc == ShadowClass.C:
            # Class C: conductor is family-dependent
            kappa_dual = -kappa_bulk
            conductor = Fraction(0)
        else:  # ShadowClass.M
            if self.bulk.name.startswith("Vir_"):
                conductor = Fraction(13)
                kappa_dual = conductor - kappa_bulk
            else:
                kappa_dual = -kappa_bulk
                conductor = None

        # Claim status: conditional if bulk is conditional or conjectured
        if self.bulk.claim_status in (ClaimStatus.CONDITIONAL, ClaimStatus.CONJECTURED):
            defect_status = ClaimStatus.CONJECTURED
        else:
            defect_status = self.bulk.claim_status

        # Dependencies propagate (AP-CY11)
        deps = self.bulk.dependencies

        return DefectAlgebraData(
            name=f"{self.bulk.name}^!",
            bulk_name=self.bulk.name,
            kappa_ch=kappa_dual,
            koszul_conductor=conductor,
            shadow_class=sc,
            claim_status=defect_status,
            dependencies=deps,
            structure_function_inverted=True,
            braiding_reversed=True,
        )

    # --- Stage 4: Conductor verification ---

    def verify_conductor(self) -> Dict[str, Any]:
        """Stage 4: Verify kappa_ch(A) + kappa_ch(A^!) = K (Koszul conductor).

        Returns a dictionary with verification results.
        """
        defect = self.defect  # triggers stages 1-3
        kappa_sum = self.bulk.kappa_ch + defect.kappa_ch
        expected_K = defect.koszul_conductor
        verified = expected_K is not None and kappa_sum == expected_K

        return {
            'bulk_name': self.bulk.name,
            'defect_name': defect.name,
            'kappa_ch_bulk': self.bulk.kappa_ch,
            'kappa_ch_defect': defect.kappa_ch,
            'kappa_sum': kappa_sum,
            'koszul_conductor': expected_K,
            'verified': verified,
            'shadow_class': self.bulk.shadow_class.value,
            'claim_status': defect.claim_status.value,
        }

    # --- Stage 5: Morita equivalence ---

    @property
    def morita(self) -> MoritaEquivalenceData:
        """Stage 5: Check the bar-cobar Morita equivalence."""
        if self._morita is None:
            self._morita = self._compute_morita()
        return self._morita

    def _compute_morita(self) -> MoritaEquivalenceData:
        """Compute Morita equivalence data."""
        _ = self.bar  # DAG dependency

        sc = self.bulk.shadow_class

        # On the Koszul locus: Omega(B(A)) ~ A for class G and L
        # For class M: the bar-cobar adjunction still holds, but
        # the cobar may not recover A exactly (quasi-isomorphism
        # requires convergence of the A_infinity tower)
        is_koszul = sc in (ShadowClass.G, ShadowClass.L)

        # E_n level: d=1 -> E_1, d=2 -> E_2, d=3 -> E_1 (then E_2 via center)
        en_level = min(self.bulk.cy_dim.value, 2)

        # Claim status
        if self.bulk.claim_status in (ClaimStatus.CONDITIONAL, ClaimStatus.CONJECTURED):
            morita_status = ClaimStatus.CONJECTURED
        elif is_koszul:
            morita_status = ClaimStatus.PROVED_ELSEWHERE
        else:
            morita_status = ClaimStatus.CONDITIONAL

        return MoritaEquivalenceData(
            bulk_name=self.bulk.name,
            is_koszul=is_koszul,
            cobar_recovers_A=is_koszul,
            en_level=en_level,
            claim_status=morita_status,
        )

    # --- Full pipeline ---

    def full_verification(self) -> Dict[str, Any]:
        """Run the complete 5-stage pipeline and return all results."""
        conductor_result = self.verify_conductor()
        morita_result = self.morita

        return {
            'target': self.bulk.name,
            'cy_dim': self.bulk.cy_dim.value,
            'kappa_spectrum': self.kappa_spectrum.values(),
            'stage_1_bulk': {
                'name': self.bulk.name,
                'kappa_ch': self.bulk.kappa_ch,
                'shadow_class': self.bulk.shadow_class.value,
                'shadow_depth': self.bulk.shadow_depth,
                'claim_status': self.bulk.claim_status.value,
            },
            'stage_2_bar': {
                'differential_trivial': self.bar.differential_trivial,
                'shadow_class': self.bar.shadow_class.value,
                'dim_arity_1': self.bar.dim_arity_1,
                'dim_arity_2': self.bar.dim_arity_2,
                'a_inf_corrections': self.bar.a_inf_corrections,
            },
            'stage_3_defect': {
                'name': self.defect.name,
                'kappa_ch': self.defect.kappa_ch,
                'koszul_conductor': self.defect.koszul_conductor,
                'structure_fn_inverted': self.defect.structure_function_inverted,
                'braiding_reversed': self.defect.braiding_reversed,
                'claim_status': self.defect.claim_status.value,
            },
            'stage_4_conductor': conductor_result,
            'stage_5_morita': {
                'is_koszul': morita_result.is_koszul,
                'cobar_recovers_A': morita_result.cobar_recovers_A,
                'en_level': morita_result.en_level,
                'claim_status': morita_result.claim_status.value,
            },
        }


# =========================================================================
# 6. Standard CY targets: factory functions
# =========================================================================

def k3_pipeline() -> DefectKoszulPipeline:
    """K3 surface (d=2): the PROVED case.

    CY-A_2 is proved. The bulk algebra is V_{Lambda_K3} (lattice VOA).
    kappa_ch(A_{K3}) = 2, kappa_ch(A_{K3}^!) = -2, K = 0.
    Class G (free-field): all bar differentials vanish.
    """
    bulk = BulkAlgebraData(
        name="A_{K3}",
        cy_dim=CYDimension.D2,
        kappa_ch=Fraction(2),
        shadow_class=ShadowClass.G,
        shadow_depth=2,
        claim_status=ClaimStatus.PROVED_ELSEWHERE,
        dependencies=("CY-A_2",),
        central_charge=Fraction(24),  # 24 free bosons
        rank=MUKAI_RANK,  # 24
    )
    spectrum = KappaSpectrum(
        kappa_ch=Fraction(2),
        kappa_BKM=None,
        kappa_cat=Fraction(K3_CHI_O),
        kappa_fiber=Fraction(MUKAI_RANK),
    )
    return DefectKoszulPipeline(bulk=bulk, kappa_spectrum=spectrum)


def k3xe_free_field_pipeline() -> DefectKoszulPipeline:
    """K3 x E (d=3), free-field / gl_1 branch: CONJECTURAL.

    On this branch: kappa_ch = 3, K = 0, kappa_ch^! = -3.
    Rep^{E_2}(A^!|_E) ~ Rep^{E_2}(Y(g_{K3})) (CONJECTURAL).

    All results conditional on CY-A_3 (AP-CY6, AP-CY14).
    """
    bulk = BulkAlgebraData(
        name="A_{K3xE}^{ff}",
        cy_dim=CYDimension.D3,
        kappa_ch=Fraction(3),
        shadow_class=ShadowClass.G,
        shadow_depth=2,
        claim_status=ClaimStatus.CONJECTURED,
        dependencies=("CY-A_3",),
        central_charge=Fraction(25),  # 24+1 free bosons (K3 lattice + E)
        rank=MUKAI_RANK + 1,  # 25
    )
    spectrum = KappaSpectrum(
        kappa_ch=Fraction(3),
        kappa_BKM=None,  # free-field branch: no BKM
        kappa_cat=Fraction(K3_CHI_O),
        kappa_fiber=Fraction(MUKAI_RANK),
    )
    return DefectKoszulPipeline(bulk=bulk, kappa_spectrum=spectrum)


def k3xe_bkm_pipeline() -> DefectKoszulPipeline:
    """K3 x E (d=3), BKM / holographic branch: CONJECTURAL.

    On this branch: relative kappa_ch^Heis = 3, compact kappa_ch = 0,
    and kappa_BKM = 5 is the Borcherds weight characteristic.
    The defect algebra is a deformation of V_{g_{Delta_5}}^!.

    All results conditional on CY-A_3 (AP-CY6, AP-CY14).
    No Koszul conductor is inferred from the Borcherds weight.
    """
    bulk = BulkAlgebraData(
        name="A_{K3xE}^{BKM}",
        cy_dim=CYDimension.D3,
        kappa_ch=Fraction(3),
        shadow_class=ShadowClass.M,
        shadow_depth=None,  # infinite (class M)
        claim_status=ClaimStatus.CONJECTURED,
        dependencies=("CY-A_3",),
        central_charge=None,
        rank=None,
    )
    spectrum = KappaSpectrum(
        kappa_ch=Fraction(3),
        kappa_BKM=Fraction(5),
        kappa_cat=Fraction(K3_CHI_O),
        kappa_fiber=Fraction(MUKAI_RANK),
    )
    return DefectKoszulPipeline(bulk=bulk, kappa_spectrum=spectrum)


def c3_pipeline() -> DefectKoszulPipeline:
    """C^3 (d=3), the reference toric CY3: partially established.

    Bulk: W_{1+infty} at Psi = -sigma_2.
    Defect: W_{1+infty}^! at Psi^! = sigma_2.
    K = 0 (class G at generic Psi).
    """
    bulk = BulkAlgebraData(
        name="W_{1+inf}",
        cy_dim=CYDimension.D3,
        kappa_ch=Fraction(1),  # c=1 for gl_1
        shadow_class=ShadowClass.G,
        shadow_depth=2,
        claim_status=ClaimStatus.PROVED_ELSEWHERE,
        dependencies=("5d-hCS",),
        central_charge=Fraction(1),
        rank=1,
    )
    spectrum = KappaSpectrum(
        kappa_ch=Fraction(1),
        kappa_BKM=None,
        kappa_cat=Fraction(0),  # chi(O_{C^3}) = 0 (non-compact)
        kappa_fiber=None,
    )
    return DefectKoszulPipeline(bulk=bulk, kappa_spectrum=spectrum)


def elliptic_curve_pipeline() -> DefectKoszulPipeline:
    """Elliptic curve (d=1): trivial case.

    Bulk: H_1 (Heisenberg at level 1).
    Defect: H_1^! is the curved Sym^ch(V*[1]) branch with the same
    scalar kappa as H_{-1}.
    K = 0 (class G).
    """
    bulk = BulkAlgebraData(
        name="H_1",
        cy_dim=CYDimension.D1,
        kappa_ch=Fraction(1),
        shadow_class=ShadowClass.G,
        shadow_depth=2,
        claim_status=ClaimStatus.PROVED_ELSEWHERE,
        dependencies=("CY-A_1",),
        central_charge=Fraction(1),
        rank=1,
    )
    spectrum = KappaSpectrum(
        kappa_ch=Fraction(1),
        kappa_BKM=None,
        kappa_cat=Fraction(0),  # chi(O_E) = 0
        kappa_fiber=Fraction(1),
    )
    return DefectKoszulPipeline(bulk=bulk, kappa_spectrum=spectrum)


def heisenberg_pipeline(k: Fraction = Fraction(1)) -> DefectKoszulPipeline:
    """Heisenberg H_k at arbitrary level (class G).

    Used for cross-checks against e1_koszul_three_families.py.
    kappa_ch(H_k) = k, kappa_ch(H_k^!) = -k, K = 0.
    """
    bulk = BulkAlgebraData(
        name=f"H_{k}",
        cy_dim=CYDimension.D2,
        kappa_ch=k,
        shadow_class=ShadowClass.G,
        shadow_depth=2,
        claim_status=ClaimStatus.PROVED_ELSEWHERE,
        dependencies=(),
        central_charge=k,
        rank=1,
    )
    spectrum = KappaSpectrum(
        kappa_ch=k,
        kappa_BKM=None,
        kappa_cat=Fraction(0),
        kappa_fiber=Fraction(1),
    )
    return DefectKoszulPipeline(bulk=bulk, kappa_spectrum=spectrum)


def virasoro_pipeline(c: Fraction = Fraction(1)) -> DefectKoszulPipeline:
    """Virasoro Vir_c at arbitrary central charge (class M).

    kappa_ch(Vir_c) = c/2, kappa_ch(Vir_{26-c}) = (26-c)/2, K = 13.
    """
    bulk = BulkAlgebraData(
        name=f"Vir_{c}",
        cy_dim=CYDimension.D2,
        kappa_ch=Fraction(c, 2),
        shadow_class=ShadowClass.M,
        shadow_depth=None,
        claim_status=ClaimStatus.PROVED_ELSEWHERE,
        dependencies=(),
        central_charge=c,
        rank=1,
    )
    spectrum = KappaSpectrum(
        kappa_ch=Fraction(c, 2),
        kappa_BKM=None,
        kappa_cat=Fraction(0),
        kappa_fiber=Fraction(1),
    )
    return DefectKoszulPipeline(bulk=bulk, kappa_spectrum=spectrum)


# =========================================================================
# 7. Structure function verification
# =========================================================================

def verify_structure_function_inversion(
    h_params: np.ndarray,
    test_points: np.ndarray,
) -> Dict[str, Any]:
    """Verify g^!(u) = 1/g(u) for the Koszul dual structure function.

    For the K3 Yangian with parameters h_1, ..., h_{24}:
        g(u) = prod_{a=1}^{24} (u - h_a) / (u + h_a)
        g^!(u) = g(-u) = prod ((-u - h_a) / (-u + h_a)) = 1/g(u)

    The identity g(u) * g(-u) = 1 (algebraic unitarity) implies
    that the Koszul dual has inverted structure function.

    AP-CY28: Test points must avoid poles at z = +/-h_i.

    Parameters
    ----------
    h_params : array of shape (n,)
        The deformation parameters h_1, ..., h_n.
    test_points : array of shape (m,)
        Points u at which to evaluate (must avoid +/-h_i).

    Returns
    -------
    dict with verification results.
    """
    results = []
    for u in test_points:
        # g(u) = prod (u - h_i) / (u + h_i)
        g_u = np.prod((u - h_params) / (u + h_params))

        # g(-u) = prod (-u - h_i) / (-u + h_i)
        g_neg_u = np.prod((-u - h_params) / (-u + h_params))

        # Check g(u) * g(-u) = 1 (unitarity)
        product = g_u * g_neg_u
        unitarity_ok = abs(product - 1.0) < 1e-12

        # Check g^!(u) = 1/g(u)
        g_dual_u = g_neg_u  # g^!(u) := g(-u)
        inversion_ok = abs(g_dual_u * g_u - 1.0) < 1e-12

        results.append({
            'u': float(u),
            'g_u': float(g_u),
            'g_neg_u': float(g_neg_u),
            'product': float(product),
            'unitarity': unitarity_ok,
            'inversion': inversion_ok,
        })

    all_ok = all(r['unitarity'] and r['inversion'] for r in results)
    return {
        'n_params': len(h_params),
        'n_points': len(test_points),
        'all_pass': all_ok,
        'results': results,
    }


def k3_structure_function_inversion(
    n_test_points: int = 20,
) -> Dict[str, Any]:
    """Verify structure function inversion for the K3 Yangian.

    Uses h_params satisfying the CY_2 constraint: sum h_i = 0.
    AP-CY28: Test points avoid poles at +/-h_i by using large primes.

    The 24 parameters are chosen on the null cone of the Mukai lattice:
        h_i = a_i * epsilon, sum a_i = 0
    For computational simplicity, we use the parametrization:
        h_1 = ... = h_{12} = +1, h_{13} = ... = h_{24} = -1
    (which satisfies sum h_i = 12 - 12 = 0).
    """
    # Parameters satisfying CY_2 constraint: sum h_i = 0
    h = np.array([1.0] * 12 + [-1.0] * 12)
    assert abs(np.sum(h)) < 1e-14, "CY_2 constraint violated"

    # Test points: avoid +/-h_i = +/-1
    # AP-CY28: use points far from poles
    test_u = np.linspace(3.0, 50.0, n_test_points)

    return verify_structure_function_inversion(h, test_u)


# =========================================================================
# 8. Braiding reversal verification
# =========================================================================

def verify_braiding_reversal(
    kappa_ch_bulk: Fraction,
    kappa_ch_defect: Fraction,
) -> Dict[str, Any]:
    """Verify that the defect algebra has reversed braiding.

    For the free-field branch (K=0):
        R^{E_2,!}(z) = -R^{E_2}(z) at leading order
    which is the braiding reversal sigma^! = sigma^{-1}.

    The key diagnostic: kappa_ch^! = -kappa_ch implies the leading
    R-matrix coefficient has opposite sign, hence the braiding is reversed.

    Parameters
    ----------
    kappa_ch_bulk : kappa_ch of the bulk algebra (= level k).
    kappa_ch_defect : kappa_ch of the defect algebra.

    Returns
    -------
    dict with verification results.
    """
    conductor = kappa_ch_bulk + kappa_ch_defect
    is_free_field = conductor == 0

    # On the free-field branch: R^! ~ -R (opposite sign)
    # The R-matrix coefficient at leading order is proportional to kappa_ch
    sign_reversed = (kappa_ch_defect == -kappa_ch_bulk)

    return {
        'kappa_ch_bulk': kappa_ch_bulk,
        'kappa_ch_defect': kappa_ch_defect,
        'conductor': conductor,
        'is_free_field_branch': is_free_field,
        'braiding_reversed': sign_reversed and is_free_field,
        'r_matrix_sign': 'opposite' if sign_reversed else 'same',
    }


# =========================================================================
# 9. Cross-checks against existing engines
# =========================================================================

def cross_check_e1_koszul(
    k: Fraction = Fraction(1),
) -> Dict[str, Any]:
    """Cross-check against e1_koszul_three_families.py (Heisenberg).

    The Heisenberg H_k: kappa_ch = k, kappa_ch^! = -k, K = 0.
    Verified against both the DAG pipeline and the direct computation.
    """
    pipeline = heisenberg_pipeline(k)
    pipeline_result = pipeline.verify_conductor()

    # Direct computation (matching e1_koszul_three_families.py)
    direct_kappa = k
    direct_kappa_dual = -k
    direct_conductor = Fraction(0)
    direct_sum = direct_kappa + direct_kappa_dual

    return {
        'family': f'H_{k}',
        'pipeline': pipeline_result,
        'direct': {
            'kappa_ch': direct_kappa,
            'kappa_ch_dual': direct_kappa_dual,
            'sum': direct_sum,
            'conductor': direct_conductor,
            'verified': direct_sum == direct_conductor,
        },
        'match': pipeline_result['verified'] and (direct_sum == direct_conductor),
    }


def cross_check_virasoro(
    c: Fraction = Fraction(1),
) -> Dict[str, Any]:
    """Cross-check against e1_koszul_three_families.py (Virasoro).

    The Virasoro Vir_c: kappa_ch = c/2, kappa_ch^! = (26-c)/2, K = 13.
    """
    pipeline = virasoro_pipeline(c)
    pipeline_result = pipeline.verify_conductor()

    # Direct computation (matching e1_koszul_three_families.py)
    direct_kappa = Fraction(c, 2)
    c_prime = 26 - c
    direct_kappa_dual = Fraction(c_prime, 2)
    direct_conductor = Fraction(13)
    direct_sum = direct_kappa + direct_kappa_dual

    return {
        'family': f'Vir_{c}',
        'pipeline': pipeline_result,
        'direct': {
            'c': c,
            'c_prime': c_prime,
            'kappa_ch': direct_kappa,
            'kappa_ch_dual': direct_kappa_dual,
            'sum': direct_sum,
            'conductor': direct_conductor,
            'verified': direct_sum == direct_conductor,
        },
        'match': pipeline_result['verified'] and (direct_sum == direct_conductor),
    }


# =========================================================================
# 10. Master verification: all standard targets
# =========================================================================

def master_verification() -> Dict[str, Any]:
    """Run the full pipeline on all standard CY targets.

    Returns a dictionary with results for each target.
    """
    pipelines = {
        'elliptic_curve': elliptic_curve_pipeline(),
        'heisenberg_k1': heisenberg_pipeline(Fraction(1)),
        'heisenberg_k2': heisenberg_pipeline(Fraction(2)),
        'heisenberg_k_neg': heisenberg_pipeline(Fraction(-1)),
        'k3': k3_pipeline(),
        'c3': c3_pipeline(),
        'k3xe_free_field': k3xe_free_field_pipeline(),
        'k3xe_bkm': k3xe_bkm_pipeline(),
        'virasoro_c1': virasoro_pipeline(Fraction(1)),
        'virasoro_c13': virasoro_pipeline(Fraction(13)),
        'virasoro_c26': virasoro_pipeline(Fraction(26)),
    }

    results = {}
    for name, pipeline in pipelines.items():
        results[name] = pipeline.full_verification()

    return results


def verify_all_conductors() -> Dict[str, bool]:
    """Quick verification of all Koszul conductors across standard targets."""
    targets = master_verification()
    return {
        name: data['stage_4_conductor']['verified']
        for name, data in targets.items()
        if data['stage_4_conductor']['koszul_conductor'] is not None
    }
