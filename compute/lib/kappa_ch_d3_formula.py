#!/usr/bin/env python3
r"""
kappa_ch_d3_formula.py -- Constructed kappa_ch values and d=3 candidates.

RESOLUTION OF THE CY-D INCONSISTENCY
=====================================

The old CY-D confusion treated several d=3 shadows as if they were the
same invariant as the compact Hodge/PhiFA value kappa_ch = chi(O_X):

  For ANY strict compact CY_d with d odd:
    h^{0,q} = (1, 0, ..., 0, 1)  with d+1 entries,
    chi(O_X) = 1 - 0 + ... - 0 + (-1)^d * 1 = 1 + (-1)^d.
    For d odd: chi(O_X) = 0.

  But the d=3 scalar lanes already separate:
    K3 x E:  compact kappa_ch = 0, kappa_ch_Heis = 3
    Quintic: kappa_BCOV_shadow_conjectural = -25/3, chi(O) = 0
    C^3:     kappa_ch = 1,     (non-compact MacMahon/Heisenberg lane)

The CORRECT analysis separates the compact Hodge/PhiFA supertrace from
Heisenberg, BCOV, and local-surface shadows.  The compact value is
chi(O_X); the additive value 3 on K3 x E is kappa_ch_Heis.

THE CORRECT FORMULA (DIMENSION-STRATIFIED)
==========================================

There is NO single closed formula covering compact, Heisenberg, BCOV,
and local-surface lanes.  The formulas are DIMENSION-STRATIFIED:

  d=0: compact kappa_ch = chi(O_pt) = 1.

  d=1: compact kappa_ch = chi(O_X) = 0 for an elliptic curve.
       The Heisenberg shadow is kappa_ch_Heis(E) = 1.

  d=2: kappa_ch = chi(O_X) = 1 - h^{1,0} + h^{2,0}.  PROVED.
       For K3: kappa_ch = 2.  For T^4: kappa_ch = 0.
       delta_kappa = 0 (Serre duality kills it).

  d=3 (compact):
       compact kappa_ch = chi(O_X) = 0.
       kappa_BCOV_shadow_conjectural = chi_top(X) / 24.
       For quintic:
       kappa_BCOV_shadow_conjectural = -200/24 = -25/3.

  d=3 (K3-fibered S x E): kappa_ch_Heis = kappa_ch_Heis(S) + kappa_ch_Heis(E).
       For K3 x E: kappa_ch_Heis = 2 + 1 = 3.
       For Enr x E: kappa_ch_Heis = 1 + 1 = 2.

  d=3 (local surface Tot(K_S -> S)): kappa_ch = chi_top(S) / 2.  CONJECTURAL.
       For local P^2: kappa_ch = 3/2.
       For local P^1 x P^1: kappa_ch = 2.
       Domain: genuine local surfaces ONLY (AP182).

  d=3 (C^3, toric non-compact): kappa_ch = 1.  PROVED.
       From MacMahon/Heisenberg identification.

  d=3 (resolved conifold): kappa_ch = 1.  PROVED.
       From the single compact BPS cycle.

ADDITIVITY VS MULTIPLICATIVITY
===============================

The root cause of the old CY-D confusion at d >= 3 is the clash between:

  kappa_ch_Heis: ADDITIVE under products.
  kappa_ch_Heis(X x Y) = kappa_ch_Heis(X) + kappa_ch_Heis(Y).
  chi(O_X): MULTIPLICATIVE under products.  chi(O_{X x Y}) = chi(O_X) * chi(O_Y).

These are compatible only when chi(O) = 0 (K3 x E: 0 = 2*0, OK) or when
the product structure is trivial.  For the d=2 PROVED case, the formula
kappa_ch = chi(O_X) holds for INDIVIDUAL CY2s, but the product formula
kappa_ch_Heis(S x E) = kappa_ch_Heis(S) + kappa_ch_Heis(E)
need not equal chi(O_{S x E}) = 0
ALREADY breaks at d=3.

This is the fundamental reason the old generic API drifted: kappa_ch_Heis is
additive, while compact chi(O_X) is multiplicative.  They may agree on
individual d=2 surfaces, but their product behaviour already separates at d=3.

SHADOW GAP MECHANISM
====================

At d=1: the free boson from H^{1,0} = H^0(Omega^1_X) is NOT killed by Serre duality
  (S_C = [1] pairs HH_0 with HH_1, but does not force the anomaly to vanish).
  The correction delta_kappa = h^{1,0}(X) counts the free-boson zero modes.

At d=2: Serre duality S_C = [2] forces HH^3(C) = HH_{-1}^vee = 0, killing
  the one-loop anomaly.  delta_kappa = 0.

At d=3: Serre duality S_C = [3] does NOT force the anomaly to vanish.
  The obstruction group HH^4(C) = HH_{-1}^vee; for h^{1,0}=0 CY3,
  HH_{-1} = 0, so the anomaly vanishes in HH^4, BUT this does not control
  BCOV-shadow or Heisenberg-shadow values.  Those shadows are not promoted to
  compact kappa_ch without the missing chain-level proof.

  For compact CY3 with h^{1,0}=0:
    the BCOV-shadow candidate is chi_top / 24 =
    (h^{1,1} - h^{2,1}) / 12.  It is not promoted to constructed
    kappa_ch without the missing chain-level proof.

  For product CY3 (S x E):
    Heisenberg gap = kappa_ch_Heis(S) + kappa_ch_Heis(E) - chi(O_{S x E}).
    For K3 x E: Heisenberg gap = 3 - 0 = 3.


AP COMPLIANCE
=============

AP113: All kappa values subscripted (kappa_ch, kappa_cat, kappa_BKM, kappa_fiber).
AP-CY6: No unconstructed A_X invoked at theorem level.
AP-CY11: All d=3 results conditional on CY-A_3 unless otherwise stated.
AP-CY8: Borcherds identification is observational.
AP155: Not claiming novelty for known invariants.
AP157: Degeneration type specified where relevant.

Ground truth:
  chapters/theory/cy_to_chiral.tex (Proposition prop:cy-kappa-d2, PROVED at d=2)
  chapters/theory/cy_to_chiral.tex (Conjecture conj:cy-kappa-identification, REFUTED)
  chapters/examples/k3_chiral_algebra.tex (kappa-spectrum proposition, items i-vii)
  chapters/connections/modular_koszul_bridge.tex (Definition def:cy-categorical-kappa)
  CLAUDE.md (kappa-spectrum table, AP113)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, NamedTuple, Optional, Tuple


# =========================================================================
# 1. Hodge data for CY manifolds
# =========================================================================

class CYHodgeData(NamedTuple):
    """Hodge data sufficient to compute all kappa invariants.

    Stores the full h^{0,q} column (sufficient for chi(O_X)),
    plus h^{1,1} and h^{2,1} for CY3s (sufficient for chi_top).
    """
    name: str
    dim_C: int               # CY dimension d
    h0q: Tuple[int, ...]     # h^{0,0}, h^{0,1}, ..., h^{0,d}
    chi_top: Optional[int]   # topological Euler characteristic (None if non-compact)
    h11: Optional[int]       # h^{1,1} (for CY3 chi_top formula)
    h21: Optional[int]       # h^{2,1} (for CY3 Hodge data)
    compact: bool            # whether X is compact
    product_of: Optional[Tuple[str, str]]  # if X = Y x Z, the factor names

    def chi_O(self) -> int:
        """Holomorphic Euler characteristic chi(O_X) = sum (-1)^q h^{0,q}."""
        return sum((-1) ** q * h for q, h in enumerate(self.h0q))


class KappaChAssessment(NamedTuple):
    """A scalar value together with its theorem status and proof lane."""
    manifold: str
    dim_C: int
    value: Fraction
    label: str
    status: str
    constructed: bool
    proof_lane: str


# =========================================================================
# 2. Standard CY manifolds
# =========================================================================

def point() -> CYHodgeData:
    """Point: CY_0."""
    return CYHodgeData("point", 0, (1,), 1, None, None, True, None)


def elliptic_curve() -> CYHodgeData:
    """Elliptic curve E: CY_1."""
    return CYHodgeData("E", 1, (1, 1), 0, None, None, True, None)


def abelian_surface() -> CYHodgeData:
    """Abelian surface T^4: CY_2."""
    return CYHodgeData("T^4", 2, (1, 2, 1), 0, 4, None, True, None)


def k3_surface() -> CYHodgeData:
    """K3 surface: CY_2."""
    return CYHodgeData("K3", 2, (1, 0, 1), 24, 20, None, True, None)


def enriques_surface() -> CYHodgeData:
    """Enriques surface (generalized CY_2, torsion canonical)."""
    return CYHodgeData("Enr", 2, (1, 0, 0), 12, 10, None, True, None)


def k3_times_e() -> CYHodgeData:
    """K3 x E: CY_3 (product)."""
    return CYHodgeData("K3xE", 3, (1, 1, 1, 1), 0, 21, 21, True, ("K3", "E"))


def enriques_times_e() -> CYHodgeData:
    """Enriques x E: generalized CY_3."""
    return CYHodgeData("EnrxE", 3, (1, 1, 0, 0), 0, None, None, True, ("Enr", "E"))


def quintic_threefold() -> CYHodgeData:
    """Quintic threefold in P^4: CY_3."""
    return CYHodgeData("Quintic", 3, (1, 0, 0, 1), -200, 1, 101, True, None)


def c3_affine() -> CYHodgeData:
    """C^3: non-compact CY_3."""
    return CYHodgeData("C^3", 3, (1,), None, None, None, False, None)


def resolved_conifold() -> CYHodgeData:
    """Resolved conifold O(-1)+O(-1) -> P^1: non-compact CY_3."""
    return CYHodgeData("ResCon", 3, (1,), 2, None, None, False, None)


def local_p2() -> CYHodgeData:
    """Local P^2 = Tot(K_{P^2}): non-compact CY_3."""
    return CYHodgeData("LocalP2", 3, (1,), 3, None, None, False, None)


def local_p1p1() -> CYHodgeData:
    """Local P^1 x P^1 = Tot(K_{P^1xP^1}): non-compact CY_3."""
    return CYHodgeData("LocalP1P1", 3, (1,), 4, None, None, False, None)


def t6_abelian() -> CYHodgeData:
    """T^6 = E x E x E: abelian threefold, CY_3."""
    return CYHodgeData("T^6", 3, (1, 3, 3, 1), 0, 9, 9, True, None)


# =========================================================================
# 3. The four kappa invariants
# =========================================================================

def kappa_cat(X: CYHodgeData) -> int:
    r"""Categorical modular characteristic = chi(O_X).

    This is the Hodge-filtered supertrace: the F^0-column of the
    Hodge diamond.  Defined for any smooth projective variety.

    For ANY strict CY_d with d odd and h^{1,0}=0: chi(O_X) = 0.
    """
    return X.chi_O()


def bcov_shadow_candidate(X: CYHodgeData) -> Fraction:
    r"""Return the compact-CY3 BCOV shadow scalar chi_top(X)/24.

    This is an exact candidate scalar, not a constructed chiral
    modular characteristic.
    """
    if not (X.dim_C == 3 and X.compact and len(X.h0q) == 4 and X.h0q[1] == 0):
        raise ValueError(
            "bcov_shadow_candidate applies only to compact strict CY3 data "
            "with h^{1,0}=0"
        )
    if X.chi_top is None:
        raise ValueError(f"chi_top required for compact CY3 {X.name}")
    return Fraction(X.chi_top, 24)


def kappa_ch_assessment(X: CYHodgeData) -> KappaChAssessment:
    r"""Assess the d-dependent scalar without erasing its proof status."""
    if X.compact:
        return KappaChAssessment(
            manifold=X.name,
            dim_C=X.dim_C,
            value=kappa_ch(X),
            label="kappa_ch_compact_hodge",
            status="PROVED",
            constructed=True,
            proof_lane="compact Hodge/PhiFA supertrace chi(O_X)",
        )

    value = kappa_ch(X)
    if X.name in ("C^3", "ResCon"):
        status = "PROVED"
        constructed = True
    elif X.name in ("LocalP2", "LocalP1P1", "EnrxE", "T^6"):
        status = "CONJECTURAL"
        constructed = False
    else:
        status = "OPEN"
        constructed = False

    if X.name in ("LocalP2", "LocalP1P1"):
        label = "kappa_local_surface_conjectural"
        proof_lane = "local-surface chi_top(base)/2 shadow"
    elif X.name in ("EnrxE", "T^6"):
        label = "kappa_ch_product_conjectural"
        proof_lane = "product additivity candidate outside the strict proved lane"
    else:
        label = "kappa_ch"
        proof_lane = "constructed chiral lane"

    return KappaChAssessment(
        manifold=X.name,
        dim_C=X.dim_C,
        value=value,
        label=label,
        status=status,
        constructed=constructed,
        proof_lane=proof_lane,
    )


def kappa_ch(X: CYHodgeData) -> Fraction:
    r"""Compact chiral modular characteristic: the Hodge/PhiFA supertrace.

    This is the CORRECT dimension-stratified formula:

      compact: kappa_ch = chi(O_X) = sum (-1)^q h^{0,q}.  PROVED.
      d=3 (product S x E): kappa_ch_Heis = kappa_ch_Heis(S) + kappa_ch_Heis(E).
      d=3 (local surface Tot(K_S)): kappa_ch = chi_top(S) / 2.
      d=3 (C^3): kappa_ch = 1.  PROVED.
      d=3 (resolved conifold): kappa_ch = 1.  PROVED.

    Returns Fraction for the compact/noncompact lane.  Use
    kappa_ch_Heis() for additive product shadows and
    bcov_shadow_candidate() for BCOV chi_top/24 shadows.
    """
    if X.compact:
        return Fraction(X.chi_O())
    if X.dim_C == 3:
        return _kappa_ch_d3(X)
    raise NotImplementedError(
        f"kappa_ch not implemented for noncompact d={X.dim_C}."
    )


def kappa_ch_Heis(X: CYHodgeData) -> Fraction:
    r"""Relative Heisenberg/free-field scalar.

    This is the additive product lane.  It is not the compact total-space
    Hodge/PhiFA supertrace.
    """
    if X.product_of is not None:
        fiber_name, base_name = X.product_of
        return kappa_ch_Heis(_get_manifold_by_name(fiber_name)) + kappa_ch_Heis(_get_manifold_by_name(base_name))
    if X.name == "point":
        return Fraction(0)
    if X.name == "E":
        return Fraction(1)
    if X.name == "K3":
        return Fraction(2)
    if X.name == "Enr":
        return Fraction(1)
    if X.name == "T^4":
        return Fraction(2)
    if X.name == "T^6":
        return Fraction(3)
    return kappa_ch(X)


def _kappa_ch_d3(X: CYHodgeData) -> Fraction:
    """Compute kappa_ch at d=3 using the correct stratified formula."""

    # C^3: proved via Heisenberg identification
    if X.name == "C^3":
        return Fraction(1)

    # Resolved conifold: proved via single BPS cycle
    if X.name == "ResCon":
        return Fraction(1)

    # Local surfaces: kappa_ch = chi_top(base) / 2 (AP182)
    if X.name in ("LocalP2", "LocalP1P1"):
        if X.chi_top is None:
            raise ValueError(f"chi_top required for local surface {X.name}")
        return Fraction(X.chi_top, 2)

    raise NotImplementedError(
        f"kappa_ch for noncompact CY3 {X.name} is not in the implemented lane."
    )


def _get_manifold_by_name(name: str) -> CYHodgeData:
    """Look up a CY manifold by name (for product decomposition)."""
    registry = {
        "E": elliptic_curve(),
        "K3": k3_surface(),
        "Enr": enriques_surface(),
        "T^4": abelian_surface(),
    }
    if name not in registry:
        raise ValueError(f"Unknown manifold: {name}")
    return registry[name]


# =========================================================================
# 4. Quantum correction analysis
# =========================================================================

class QuantumCorrection(NamedTuple):
    """The gap between the selected scalar lane and compact chi(O_X)."""
    manifold: str
    dim_C: int
    chi_O: int                  # classical value = chi(O_X)
    kappa_ch: Fraction          # compact kappa_ch or labelled candidate
    delta_kappa: Fraction       # selected scalar minus chi(O_X)
    delta_vanishes: bool        # whether delta_kappa = 0
    mechanism: str              # explanation of the correction
    label: str                  # kappa_ch or a labelled candidate lane
    status: str                 # theorem status of the scalar lane
    constructed: bool           # whether this is constructed kappa_ch


def quantum_correction(X: CYHodgeData) -> QuantumCorrection:
    """Compute selected scalar minus chi(O_X).

    For compact kappa_ch this vanishes by construction.  BCOV and
    Heisenberg shadows should be compared by their own named helpers.
    """
    chi = X.chi_O()
    assessment = kappa_ch_assessment(X)
    k_ch = assessment.value
    delta = k_ch - chi

    if X.dim_C == 0:
        mechanism = "trivial (d=0)"
    elif X.dim_C == 1:
        mechanism = "compact odd-dimensional Hodge supertrace"
    elif X.dim_C == 2:
        mechanism = (
            "compact Hodge/PhiFA supertrace equals chi(O_X)"
        )
    elif X.dim_C == 3:
        if X.compact and len(X.h0q) == 4 and X.h0q[1] == 0:
            mechanism = (
                f"Compact odd-dimensional Hodge supertrace: chi(O_X)=0. "
                f"The separate BCOV-shadow candidate is {X.chi_top}/24."
            )
        elif X.product_of is not None:
            mechanism = (
                f"Compact product value: kappa_ch=chi(O_X)={chi}. "
                f"The Heisenberg shadow is additive and equals "
                f"{kappa_ch_Heis(X)}."
            )
        else:
            mechanism = (
                f"Non-compact or special case: kappa_ch = {k_ch} from "
                f"independent computation."
            )
    else:
        mechanism = "Unknown (d >= 4)"

    return QuantumCorrection(
        manifold=X.name,
        dim_C=X.dim_C,
        chi_O=chi,
        kappa_ch=k_ch,
        delta_kappa=delta,
        delta_vanishes=(delta == 0),
        mechanism=mechanism,
        label=assessment.label,
        status=assessment.status,
        constructed=assessment.constructed,
    )


# =========================================================================
# 5. Compact CY-D and shadow separation
# =========================================================================

def verify_cyd_refutation() -> Dict[str, Any]:
    r"""Verify the compact CY-D statement and separate shadow lanes.

    The quintic supplies only a BCOV-shadow candidate at this level:
      kappa_BCOV_shadow_conjectural(Quintic) = -25/3.
    """
    results: Dict[str, Any] = {}

    # d=1 counterexample
    e = elliptic_curve()
    results["E_kappa_ch"] = int(kappa_ch(e))           # 0
    results["E_kappa_ch_Heis"] = int(kappa_ch_Heis(e))  # 1
    results["E_chi_O"] = kappa_cat(e)                    # 0
    results["E_CYD_holds"] = kappa_ch(e) == kappa_cat(e)  # True

    # d=2 verification (CY-D holds)
    k3 = k3_surface()
    results["K3_kappa_ch"] = int(kappa_ch(k3))          # 2
    results["K3_chi_O"] = kappa_cat(k3)                  # 2
    results["K3_CYD_holds"] = kappa_ch(k3) == kappa_cat(k3)  # True

    t4 = abelian_surface()
    results["T4_kappa_ch"] = int(kappa_ch(t4))          # 0
    results["T4_chi_O"] = kappa_cat(t4)                  # 0
    results["T4_CYD_holds"] = kappa_ch(t4) == kappa_cat(t4)  # True

    # d=3 compact value and Heisenberg shadow
    k3e = k3_times_e()
    results["K3xE_kappa_ch"] = int(kappa_ch(k3e))       # 0
    results["K3xE_kappa_ch_Heis"] = int(kappa_ch_Heis(k3e))  # 3
    results["K3xE_chi_O"] = kappa_cat(k3e)               # 0
    results["K3xE_CYD_holds"] = kappa_ch(k3e) == kappa_cat(k3e)  # True

    q = quintic_threefold()
    q_assessment = kappa_ch_assessment(q)
    q_bcov = bcov_shadow_candidate(q)
    results["Quintic_BCOV_shadow_candidate"] = q_bcov  # -25/3
    results["Quintic_chi_O"] = kappa_cat(q)               # 0
    results["Quintic_candidate_differs_from_CYD"] = (
        q_bcov != kappa_cat(q)
    )
    results["Quintic_compact_kappa_ch"] = kappa_ch(q)
    results["Quintic_constructed_kappa_ch"] = q_assessment.constructed

    # Heisenberg additivity is separate from compact multiplicativity.
    results["additivity_test"] = kappa_ch_Heis(k3e) == kappa_ch_Heis(k3) + kappa_ch_Heis(e)  # True (3 = 2+1)
    results["multiplicativity_test"] = kappa_cat(k3e) == kappa_cat(k3) * kappa_cat(e)  # True (0 = 2*0)
    results["shadow_differs_from_compact"] = (
        kappa_ch_Heis(k3e) != kappa_ch(k3e)
    )  # True (3 != 0)
    results["clash"] = results["shadow_differs_from_compact"]

    # chi(O_X) = 0 for ALL strict CY3s with h^{1,0}=0
    results["chi_O_vanishes_for_strict_CY3"] = True
    for X in [quintic_threefold()]:
        if X.chi_O() != 0:
            results["chi_O_vanishes_for_strict_CY3"] = False

    return results


# =========================================================================
# 6. The correct CY-D replacement
# =========================================================================

class CYDStatus(NamedTuple):
    """Status of the CY-D identification at each dimension."""
    dimension: int
    formula: str
    status: str                # "PROVED", "CONJECTURAL", "REFUTED"
    delta_kappa_formula: str   # formula for the quantum correction
    examples: str              # verification examples


def cyd_status_table() -> Dict[int, CYDStatus]:
    """The correct CY-D status at each dimension."""
    return {
        0: CYDStatus(
            dimension=0,
            formula="compact kappa_ch = chi(O_pt) = 1",
            status="PROVED",
            delta_kappa_formula="compact delta = 0",
            examples="point: compact kappa_ch = 1 = chi(O)",
        ),
        1: CYDStatus(
            dimension=1,
            formula="compact kappa_ch = chi(O_X); kappa_ch_Heis = h^{1,0}(X)",
            status="PROVED",
            delta_kappa_formula="compact delta = 0; Heisenberg gap = h^{1,0}",
            examples="E: compact kappa_ch = 0 = chi(O_E); kappa_ch_Heis = 1",
        ),
        2: CYDStatus(
            dimension=2,
            formula="kappa_ch = chi(O_X)",
            status="PROVED",
            delta_kappa_formula="delta = 0 (Serre duality S_C=[2] kills it)",
            examples="K3: kappa_ch = 2 = chi(O_K3); T^4: kappa_ch = 0 = chi(O_{T^4})",
        ),
        3: CYDStatus(
            dimension=3,
            formula="compact kappa_ch = chi(O_X); shadows are separately labelled",
            status="PROVED for compact Hodge/PhiFA; shadow comparisons OPEN/CONJECTURAL",
            delta_kappa_formula=(
                "compact delta = 0; BCOV shadow = chi_top/24; "
                "products S x E have kappa_ch_Heis by additivity"
            ),
            examples=(
                "K3xE: compact kappa_ch=0, kappa_ch_Heis=3; "
                "Quintic: kappa_BCOV_shadow_conjectural=-25/3, "
                "compact kappa_ch=0; "
                "C^3: kappa_ch=1"
            ),
        ),
    }


# =========================================================================
# 7. Landscape table
# =========================================================================

class KappaLandscapeEntry(NamedTuple):
    """Entry in the kappa_ch and d=3 candidate landscape table."""
    name: str
    dim_C: int
    kappa_ch: Fraction
    chi_O: int
    delta_kappa: Fraction
    chi_top: Optional[int]
    formula_used: str
    status: str
    label: str
    constructed: bool
    kappa_ch_Heis: Optional[Fraction] = None


def kappa_ch_landscape() -> list:
    """Complete landscape of constructed kappa_ch values and candidates.

    This table is authoritative only together with the label/status columns.
    """
    manifolds = [
        (point(), "compact chi(O_X)", "PROVED"),
        (elliptic_curve(), "compact chi(O_X)", "PROVED"),
        (abelian_surface(), "chi(O_X) at d=2", "PROVED"),
        (k3_surface(), "chi(O_X) at d=2", "PROVED"),
        (enriques_surface(), "chi(O_X) at d=2", "PROVED"),
        (c3_affine(), "MacMahon/Heisenberg", "PROVED"),
        (resolved_conifold(), "BPS cycle count", "PROVED"),
        (local_p2(), "chi_top(base)/2", "CONJECTURAL"),
        (local_p1p1(), "chi_top(base)/2", "CONJECTURAL"),
        (k3_times_e(), "compact chi(O_X)", "PROVED"),
        (enriques_times_e(), "compact chi(O_X)", "PROVED"),
        (quintic_threefold(), "compact chi(O_X); BCOV shadow separate", "PROVED"),
        (t6_abelian(), "compact chi(O_X)", "PROVED"),
    ]

    table = []
    for X, formula, status in manifolds:
        assessment = kappa_ch_assessment(X)
        k_ch = assessment.value
        chi = X.chi_O()
        delta = k_ch - chi
        table.append(KappaLandscapeEntry(
            name=X.name,
            dim_C=X.dim_C,
            kappa_ch=k_ch,
            chi_O=chi,
            delta_kappa=delta,
            chi_top=X.chi_top,
            formula_used=formula,
            status=assessment.status if status == "CONJECTURAL" else status,
            label=assessment.label,
            constructed=assessment.constructed,
            kappa_ch_Heis=kappa_ch_Heis(X) if X.compact else None,
        ))
    return table


# =========================================================================
# 8. Additivity vs multiplicativity analysis
# =========================================================================

def additivity_vs_multiplicativity() -> Dict[str, Any]:
    r"""Demonstrate compact multiplicativity versus Heisenberg additivity.

    kappa_ch_Heis(X x Y) = kappa_ch_Heis(X) + kappa_ch_Heis(Y) [additive]
    chi(O_{X x Y})  = chi(O_X) * chi(O_Y)            [multiplicative, Kunneth]
    """
    e = elliptic_curve()
    k3 = k3_surface()
    k3e = k3_times_e()
    t4 = abelian_surface()

    results: Dict[str, Any] = {}

    results["K3xE"] = {
        "kappa_ch_Heis_additive": kappa_ch_Heis(k3) + kappa_ch_Heis(e),   # 2 + 1 = 3
        "kappa_ch_Heis_actual": kappa_ch_Heis(k3e),                    # 3
        "kappa_ch_compact": kappa_ch(k3e),                             # 0
        "chi_O_multiplicative": kappa_cat(k3) * kappa_cat(e),  # 2 * 0 = 0
        "chi_O_actual": kappa_cat(k3e),                      # 0
        "additivity_holds": kappa_ch_Heis(k3e) == kappa_ch_Heis(k3) + kappa_ch_Heis(e),
        "multiplicativity_holds": kappa_cat(k3e) == kappa_cat(k3) * kappa_cat(e),
        "compact_agrees": kappa_ch(k3e) == kappa_cat(k3e),
        "shadow_differs_from_compact": kappa_ch_Heis(k3e) != kappa_ch(k3e),
    }

    # T^4 x E (hypothetical): kappa_ch_Heis(T^4) + kappa_ch_Heis(E) = 2 + 1 = 3
    # chi(O_{T^4 x E}) = chi(O_{T^4}) * chi(O_E) = 0 * 0 = 0
    results["T4xE_hypothetical"] = {
        "kappa_ch_Heis_predicted": kappa_ch_Heis(t4) + kappa_ch_Heis(e),  # 2 + 1 = 3
        "chi_O_predicted": kappa_cat(t4) * kappa_cat(e),   # 0 * 0 = 0
        "shadow_differs_from_compact": (kappa_ch_Heis(t4) + kappa_ch_Heis(e)) != (kappa_cat(t4) * kappa_cat(e)),
    }

    # Why they agree at d=2 individually but not under products:
    # At d=2, kappa_ch(X) = chi(O_X) for each individual X.
    # But kappa_ch(X x E) = chi(O_X) + 1 != chi(O_X) * 0 = 0.
    results["d2_individual_agreement"] = {
        "K3": kappa_ch(k3) == Fraction(kappa_cat(k3)),       # True
        "T4": kappa_ch(t4) == Fraction(kappa_cat(t4)),       # True
    }
    results["d3_product_disagreement"] = {
        "K3xE_compact": kappa_ch(k3e) == Fraction(kappa_cat(k3e)),  # True
        "K3xE_Heis": kappa_ch_Heis(k3e) != Fraction(kappa_cat(k3e)),  # True
    }

    return results


# =========================================================================
# 9. The corrected CY-D conjecture
# =========================================================================

def corrected_cyd_statement() -> str:
    r"""The corrected CY-D conjecture.

    ORIGINAL (REFUTED):
      kappa_ch(A_C) = chi^{CY}(C) = chi(O_X)  for all d.

    CORRECTED:
      compact kappa_ch(A_C) = chi(O_X).
      At d=3 the additional scalar shadows are dimension-stratified:

        (i) For compact CY3 with h^{1,0}=0:
            kappa_BCOV_shadow_conjectural = chi_top(X) / 24.
            This is not the compact kappa_ch.

        (ii) For product CY3 of the form S x E:
             kappa_ch_Heis = kappa_ch_Heis(S) + kappa_ch_Heis(E).
             [Additivity of the chiral de Rham complex]

        (iii) For local surfaces Tot(K_S -> S):
              kappa_ch = chi_top(S) / 2.
              [MNOP degree-zero DT]

        (iv) The three cases are consistent where they overlap:
             K3 x E satisfies both (ii) and (i)+(ii) mixed,
             giving kappa_ch_Heis = 2 + 1 = 3 while compact kappa_ch=0.
             The BCOV formula does NOT apply to K3 x E (h^{1,0}=1).

    The root cause of the old confusion is that kappa_ch_Heis is additive
    while chi(O_X) is multiplicative under products.
    """
    return "See docstring"


# =========================================================================
# 10. Master verification
# =========================================================================

def verify_all() -> Dict[str, Any]:
    """Run all verifications of the corrected CY-D formula."""
    results: Dict[str, Any] = {}

    # 1. CY-D compact/shadow separation
    results["cyd_refutation"] = verify_cyd_refutation()

    # 2. Landscape table
    results["landscape"] = [
        {
            "name": e.name,
            "d": e.dim_C,
            "kappa_ch": str(e.kappa_ch),
            "label": e.label,
            "chi_O": e.chi_O,
            "delta": str(e.delta_kappa),
            "formula": e.formula_used,
            "status": e.status,
            "constructed": e.constructed,
        }
        for e in kappa_ch_landscape()
    ]

    # 3. Additivity vs multiplicativity
    results["add_vs_mult"] = additivity_vs_multiplicativity()

    # 4. Status table
    results["status_table"] = {
        d: {
            "formula": s.formula,
            "status": s.status,
            "examples": s.examples,
        }
        for d, s in cyd_status_table().items()
    }

    # 5. Quantum corrections
    manifolds = [
        point(), elliptic_curve(), k3_surface(), abelian_surface(),
        k3_times_e(), quintic_threefold(), c3_affine(),
        resolved_conifold(), local_p2(), local_p1p1(),
    ]
    results["quantum_corrections"] = [
        {
            "manifold": qc.manifold,
            "d": qc.dim_C,
            "chi_O": qc.chi_O,
            "kappa_ch": str(qc.kappa_ch),
            "delta": str(qc.delta_kappa),
            "vanishes": qc.delta_vanishes,
        }
        for qc in [quantum_correction(X) for X in manifolds]
    ]

    # 6. Key numerical checks
    results["numerical_checks"] = {
        "kappa_ch_E": kappa_ch(elliptic_curve()) == 0,
        "kappa_ch_Heis_E": kappa_ch_Heis(elliptic_curve()) == 1,
        "kappa_ch_K3": kappa_ch(k3_surface()) == 2,
        "kappa_ch_K3xE": kappa_ch(k3_times_e()) == 0,
        "kappa_ch_Heis_K3xE": kappa_ch_Heis(k3_times_e()) == 3,
        "kappa_BCOV_shadow_candidate_Quintic": (
            bcov_shadow_candidate(quintic_threefold()) == Fraction(-25, 3)
        ),
        "Quintic_compact_kappa_ch": (
            kappa_ch(quintic_threefold()) == 0
        ),
        "kappa_ch_C3": kappa_ch(c3_affine()) == 1,
        "kappa_ch_LocalP2": kappa_ch(local_p2()) == Fraction(3, 2),
        "kappa_ch_ResCon": kappa_ch(resolved_conifold()) == 1,
        "kappa_ch_T6": kappa_ch(t6_abelian()) == 0,
        "kappa_ch_Heis_T6": kappa_ch_Heis(t6_abelian()) == 3,
        "chi_O_vanishes_for_all_strict_CY3": all(
            X.chi_O() == 0
            for X in [quintic_threefold(), k3_times_e(), t6_abelian()]
        ),
    }

    return results
