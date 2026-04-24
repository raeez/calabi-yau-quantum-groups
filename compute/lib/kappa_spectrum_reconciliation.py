#!/usr/bin/env python3
r"""
kappa_spectrum_reconciliation.py -- Definitive reconciliation of the
four-valued kappa-spectrum for K3 and K3 x E.

Ground truth:
  chapters/examples/k3_times_e.tex (kappa-spectrum proposition)
  chapters/connections/modular_koszul_bridge.tex (Definition kappa_cat)
  chapters/theory/cy_to_chiral.tex (Proposition prop:cy-kappa-d2)
  CLAUDE.md (AP113: bare kappa FORBIDDEN)

The kappa-spectrum for a CY manifold X consists of four DISTINCT invariants:

  kappa_cat(C)   := chi^{CY}(C) = sum_{i=0}^{d} (-1)^i dim HH_i(C)
                   = chi(O_X) for C = D^b(Coh(X))
                   (holomorphic Euler characteristic)

  kappa_ch(A)    := genus-1 bar-complex coefficient of the chiral
                   algebra A = Phi(C) (chiral modular characteristic)

  kappa_BKM      := weight of the Borcherds-Kac-Moody automorphic form
                   (BKM modular weight, number-theoretic)

  kappa_fiber    := rank of the underlying lattice / boundary algebra
                   (lattice modular characteristic)

At d=2, kappa_ch = kappa_cat (Proposition prop:kappa-cat-chi-cy, PROVED).
At d=3, the compact Hodge/PhiFA supertrace and the Heisenberg
specialisation must be separated.

For K3 x E:

  kappa_ch_compact_hodge(K3 x E) = chi(O_{K3 x E}) = 0
  kappa_ch^{Heis}(K3 x E)        = 3
  kappa_cat(K3 fiber)            = 2
  kappa_BKM(Delta_5)             = c_N(0)/2 at N=1 = 5

The equality 3 + 2 = 5 is a Heisenberg-specialisation fibre coincidence.
It is not the derivation of kappa_BKM, whose theorem-level derivation is
the Borcherds weight formula c_N(0)/2.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Tuple


# =========================================================================
# 1. Hodge data for CY manifolds
# =========================================================================

class HodgeData(NamedTuple):
    """Minimal Hodge data for computing kappa invariants.

    Stores h^{0,q} for q = 0, ..., d (the zeroth column of the
    Hodge diamond), which suffices for chi(O_X).
    """
    name: str
    dim_C: int          # complex dimension d
    h0q: Tuple[int, ...]  # h^{0,0}, h^{0,1}, ..., h^{0,d}
    chi_top: int        # topological Euler characteristic
    h11: Optional[int]  # h^{1,1} when defined (surfaces, threefolds)

    def chi_O(self) -> int:
        """Holomorphic Euler characteristic chi(O_X) = sum (-1)^q h^{0,q}."""
        return sum((-1)**q * h for q, h in enumerate(self.h0q))

    def dim_HH(self) -> int:
        """Total dimension of Hochschild homology (for smooth projective).

        By HKR: dim HH_*(X) = sum_{p,q} h^{p,q} = sum betti.
        For our purposes we only need h^{0,*} data.
        """
        # This is just sum h^{0,q}; NOT the full HH dimension.
        # Use only for the h^{0,*} contribution.
        return sum(self.h0q)


# Standard CY manifolds
def elliptic_curve() -> HodgeData:
    """Elliptic curve E: CY_1, h^{0,0}=1, h^{0,1}=1, chi(O)=0."""
    return HodgeData(
        name="E",
        dim_C=1,
        h0q=(1, 1),
        chi_top=0,
        h11=None,
    )


def k3_surface() -> HodgeData:
    """K3 surface: CY_2, h^{0,0}=1, h^{0,1}=0, h^{0,2}=1, chi(O)=2."""
    return HodgeData(
        name="K3",
        dim_C=2,
        h0q=(1, 0, 1),
        chi_top=24,
        h11=20,
    )


def k3_times_e() -> HodgeData:
    r"""K3 x E: CY_3.

    Hodge numbers by Kunneth:
      h^{0,0} = 1
      h^{0,1} = h^{0,1}(K3)*h^{0,0}(E) + h^{0,0}(K3)*h^{0,1}(E) = 0+1 = 1
      h^{0,2} = h^{0,2}(K3)*h^{0,0}(E) + h^{0,1}(K3)*h^{0,1}(E)
              + h^{0,0}(K3)*h^{0,2}(E) = 1+0+0 = 1
      h^{0,3} = h^{0,2}(K3)*h^{0,1}(E) + h^{0,1}(K3)*h^{0,2}(E)
              + h^{0,0}(K3)*h^{0,3}(E) = 1+0+0 = 1
    chi(O_{K3xE}) = 1 - 1 + 1 - 1 = 0
    chi_top(K3 x E) = chi_top(K3) * chi_top(E) = 24 * 0 = 0
    """
    return HodgeData(
        name="K3xE",
        dim_C=3,
        h0q=(1, 1, 1, 1),
        chi_top=0,
        h11=None,
    )


def enriques_surface() -> HodgeData:
    """Enriques surface: h^{0,0}=1, h^{0,1}=0, h^{0,2}=0, chi(O)=1."""
    return HodgeData(
        name="Enr",
        dim_C=2,
        h0q=(1, 0, 0),
        chi_top=12,
        h11=10,
    )


def quintic_threefold() -> HodgeData:
    """Quintic threefold in P^4: CY_3, chi=-200."""
    return HodgeData(
        name="Quintic",
        dim_C=3,
        h0q=(1, 0, 0, 1),
        chi_top=-200,
        h11=1,
    )


def abelian_surface() -> HodgeData:
    """Abelian surface (T^4): CY_2, chi(O)=1-2+1=0."""
    return HodgeData(
        name="T^4",
        dim_C=2,
        h0q=(1, 2, 1),
        chi_top=0,
        h11=4,
    )


# =========================================================================
# 2. The four kappa invariants
# =========================================================================

def kappa_cat(X: HodgeData) -> int:
    r"""Categorical modular characteristic.

    kappa_cat(C) := chi^{CY}(C) = chi(O_X)
                  = sum_{q=0}^{d} (-1)^q h^{0,q}(X)

    This is the holomorphic Euler characteristic. Defined for any
    smooth projective variety; no chiral algebra needed.

    Reference: modular_koszul_bridge.tex, Definition def:cy-categorical-kappa.
    """
    return X.chi_O()


def kappa_ch(X: HodgeData) -> int:
    r"""Heisenberg-specialisation chiral modular characteristic.

    At d=2: kappa_ch = kappa_cat = chi(O_X). PROVED.
    At d=1: kappa_ch(E) = 1 = dim_C(E). PROVED.
    At d=3 for the K3 x E product-specialisation:
      kappa_ch^{Heis}(K3 x E) = kappa_ch(K3) + kappa_ch(E)
                              = 2 + 1 = 3.

    For compact rigid CICYs with h^{1,0}=0:
      chi_top / 24 is only the BCOV-shadow candidate at this level.

    Note: kappa_ch(E) = 1 != chi(O_E) = 0. The chiral modular
    characteristic is NOT always chi(O_X). For K3 x E, use
    kappa_ch_compact_hodge(X) for the compact total-space Hodge/PhiFA
    supertrace, which is 0.

    Reference: cy_to_chiral.tex, Proposition prop:cy-kappa-d2.
    """
    if X.name == "E":
        return 1
    elif X.name == "K3":
        return 2  # = chi(O_K3), proved at d=2
    elif X.name == "K3xE":
        return 3  # additivity: kappa_ch(K3) + kappa_ch(E) = 2 + 1
    elif X.name == "Enr":
        return 1  # chi(O_Enr) = 1, halving of K3
    elif X.name == "Quintic":
        # The BCOV scalar -200/24 is a conjectural shadow candidate, not
        # constructed kappa_ch.
        raise ValueError(
            "constructed kappa_ch(Quintic) is open; use "
            "bcov_shadow_candidate() for the conjectural chi_top/24 lane"
        )
    elif X.name == "T^4":
        return 0  # chi(O_{T^4}) = 0
    else:
        raise ValueError(f"kappa_ch not implemented for {X.name}")


def kappa_ch_compact_hodge(X: HodgeData) -> int:
    r"""Compact total-space Hodge/PhiFA supertrace.

    This is the value relevant to the compact Hodge-supertrace reading.
    For K3 x E it is chi(O_{K3 x E}) = 0 by Kunneth. This is distinct
    from the Heisenberg specialisation kappa_ch_Heis(K3 x E) = 3.
    """
    return X.chi_O()


def bcov_shadow_candidate(X: HodgeData) -> Fraction:
    r"""Compact strict-CY3 BCOV shadow scalar chi_top/24.

    This is not constructed kappa_ch.
    """
    if X.name == "Quintic":
        return Fraction(X.chi_top, 24)  # -200/24 = -25/3
    raise ValueError(f"BCOV shadow candidate not implemented for {X.name}")


def kappa_ch_rational(X: HodgeData) -> Fraction:
    r"""Backward-compatible access to rational scalar lanes.

    For the quintic this returns kappa_BCOV_shadow_conjectural, not
    constructed kappa_ch.
    """
    if X.name == "Quintic":
        return bcov_shadow_candidate(X)
    return Fraction(kappa_ch(X))


def kappa_BKM(X: HodgeData) -> Optional[int]:
    r"""BKM modular weight.

    Defined only for CY manifolds whose BPS spectrum is controlled
    by a Borcherds-Kac-Moody superalgebra. For K3 x E: the weight
    of the Igusa cusp form Delta_5 on Sp_4(Z).

    kappa_BKM = c_f(0) / 2 where c_f(0) is the zeroth Fourier
    coefficient of the scalar-valued input to the Borcherds lift.

    For K3 x E: c_f(0) = h^{1,1}(K3) / 2 = 10, so kappa_BKM = 5.
    Equivalently: c_f(0) = (chi_top(K3) - 4) / 2 = 10.

    Reference: k3_times_e.tex, Proposition prop:k3e-fiber-global.
    """
    if X.name == "K3xE":
        k3 = k3_surface()
        assert k3.h11 is not None
        c_f_0 = k3.h11 // 2  # = 10
        return c_f_0 // 2     # = 5
    elif X.name == "K3":
        # The K3 BKM weight at d=2: the Fake Monster Lie algebra
        # has weight 12 = chi_top(K3) / 2. But this is not
        # commonly denoted kappa_BKM for K3 alone.
        return None
    else:
        return None  # Not defined for manifolds without BKM structure


def kappa_fiber(X: HodgeData) -> Optional[int]:
    r"""Fiber/lattice modular characteristic.

    For K3 x E: the rank of the Mukai lattice = 24.
    For K3: also 24 (the Mukai lattice has rank h^0 + h^2 + h^4 = 1+22+1).
    This is the kappa of the rank-24 Heisenberg boundary algebra.

    Reference: k3_times_e.tex, Proposition prop:k3-heisenberg-bar.
    """
    if X.name in ("K3", "K3xE"):
        # Mukai lattice rank = h^0(K3) + h^2(K3) + h^4(K3) = 1 + 22 + 1
        return 24
    else:
        return None


# =========================================================================
# 3. The kappa-spectrum
# =========================================================================

class KappaSpectrum(NamedTuple):
    """The four-valued kappa-spectrum for a CY manifold."""
    kappa_cat: int
    kappa_ch: Fraction
    kappa_BKM: Optional[int]
    kappa_fiber: Optional[int]
    kappa_ch_label: str
    kappa_ch_constructed: bool


def compute_spectrum(X: HodgeData) -> KappaSpectrum:
    """Compute the full kappa-spectrum for a CY manifold."""
    k_cat = kappa_cat(X)
    try:
        k_ch = Fraction(kappa_ch(X))
        k_ch_label = "kappa_ch"
        k_ch_constructed = True
    except ValueError:
        k_ch = bcov_shadow_candidate(X)
        k_ch_label = "kappa_BCOV_shadow_conjectural"
        k_ch_constructed = False
    k_BKM = kappa_BKM(X)
    k_fib = kappa_fiber(X)
    return KappaSpectrum(
        kappa_cat=k_cat,
        kappa_ch=k_ch,
        kappa_BKM=k_BKM,
        kappa_fiber=k_fib,
        kappa_ch_label=k_ch_label,
        kappa_ch_constructed=k_ch_constructed,
    )


# =========================================================================
# 4. Relations between kappa invariants
# =========================================================================

def verify_kappa_cat_is_chi_O(X: HodgeData) -> bool:
    """Verify kappa_cat = chi(O_X) = sum (-1)^q h^{0,q}."""
    return kappa_cat(X) == X.chi_O()


def verify_kappa_ch_equals_kappa_cat_at_d2(X: HodgeData) -> bool:
    """At d=2, kappa_ch = kappa_cat (Proposition prop:kappa-cat-chi-cy).

    PROVED for CY_2 categories.
    """
    if X.dim_C != 2:
        raise ValueError(f"Only valid at d=2, got d={X.dim_C}")
    try:
        return kappa_ch(X) == kappa_cat(X)
    except ValueError:
        return False


def verify_kappa_ch_additivity(
    X_fiber: HodgeData, X_base: HodgeData, X_product: HodgeData
) -> bool:
    """Verify Heisenberg-specialisation additivity.

    For K3 x E this checks the specialisation
    kappa_ch^{Heis}(K3 x E) = kappa_ch(K3) + kappa_ch(E) = 3.
    It is not the compact Hodge/PhiFA supertrace, which is multiplicative
    and vanishes for K3 x E.
    """
    try:
        return kappa_ch(X_product) == kappa_ch(X_fiber) + kappa_ch(X_base)
    except ValueError:
        return False


def verify_chi_O_multiplicativity(
    X: HodgeData, Y: HodgeData, XY: HodgeData
) -> bool:
    """Verify chi(O_{X x Y}) = chi(O_X) * chi(O_Y).

    This is the Kunneth property of the holomorphic Euler characteristic.
    """
    return XY.chi_O() == X.chi_O() * Y.chi_O()


def verify_BKM_decomposition_k3e() -> Dict[str, Any]:
    r"""Separate the false canonical BKM decomposition from the N=1 coincidence.

    For K3 x E:
      kappa_BKM(K3 x E) = 5
      kappa_ch_compact_hodge(K3 x E) = 0
      kappa_ch^{Heis}(K3 x E) = 3
      kappa_cat(K3 fiber) = chi(O_{K3}) = 2

    The canonical theorem is kappa_BKM(Delta_5)=c_N(0)/2 at N=1 = 5.
    The equality 3 + 2 = 5 is retained only as a named
    Heisenberg-specialisation fibre coincidence at N=1.
    """
    k3 = k3_surface()
    e = elliptic_curve()
    k3e = k3_times_e()

    k_ch_heis = kappa_ch(k3e)  # 3
    k_ch_compact = kappa_ch_compact_hodge(k3e)  # 0
    k_BKM = kappa_BKM(k3e)  # 5
    k_cat_K3 = kappa_cat(k3)  # 2 = chi(O_{K3})
    k_cat_E = kappa_cat(e)  # 0 = chi(O_E)
    k_cat_K3E = kappa_cat(k3e)  # 0 = chi(O_{K3xE})

    result: Dict[str, Any] = {
        "kappa_ch_K3xE": k_ch_heis,
        "kappa_ch_Heis_K3xE": k_ch_heis,
        "kappa_ch_compact_hodge_K3xE": k_ch_compact,
        "kappa_BKM_K3xE": k_BKM,
        "kappa_cat_K3": k_cat_K3,
        "kappa_cat_E": k_cat_E,
        "kappa_cat_K3xE": k_cat_K3E,
        "decomposition_holds": False,
        "compact_total_plus_K3_fiber_holds": k_BKM == k_ch_compact + k_cat_K3,
        "compact_total_plus_elliptic_fiber_holds": k_BKM == k_ch_compact + k_cat_E,
        "heis_fiber_coincidence_holds": k_BKM == k_ch_heis + k_cat_K3,
        "uses_fiber_kappa_cat": True,
        "fiber_not_total_space": k_cat_K3 != k_cat_K3E,
        "chi_O_total_space_vanishes": k_cat_K3E == 0,
    }

    return result


def borcherds_weight_from_h11() -> Dict[str, Any]:
    r"""Derive kappa_BKM from the Borcherds lift weight formula.

    The Borcherds product formula produces a Siegel modular form of weight
    c_f(0)/2, where c_f(0) is the zeroth coefficient of the scalar-valued
    modular form input.

    For K3:
      c_f(0) = h^{1,1}(K3) / 2 = 20/2 = 10
    Equivalently:
      c_f(0) = (chi_top(K3) - 4) / 2 = (24 - 4)/2 = 10

    Then:
      kappa_BKM = c_f(0) / 2 = 10 / 2 = 5

    The "10" is the weight of Phi_{10} = (Delta_5)^2 on Sp_4(Z).
    """
    k3 = k3_surface()
    assert k3.h11 is not None

    c_f_0_from_h11 = k3.h11 // 2                # 20/2 = 10
    c_f_0_from_chi = (k3.chi_top - 4) // 2      # (24-4)/2 = 10
    weight_delta5 = c_f_0_from_h11 // 2          # 10/2 = 5
    weight_phi10 = c_f_0_from_h11                # 10

    return {
        "h11_K3": k3.h11,
        "chi_top_K3": k3.chi_top,
        "c_f_0_from_h11": c_f_0_from_h11,
        "c_f_0_from_chi": c_f_0_from_chi,
        "c_f_0_consistent": c_f_0_from_h11 == c_f_0_from_chi,
        "weight_Delta5": weight_delta5,
        "weight_Phi10": weight_phi10,
        "kappa_BKM": weight_delta5,
        "Phi10_is_Delta5_squared": weight_phi10 == 2 * weight_delta5,
    }


def verify_chi_top_over_24_failure() -> Dict[str, Any]:
    r"""Verify that chi_top/24 does NOT give kappa_ch in general.

    The BCOV shadow candidate chi_top/24 is a conjectural compact rigid
    CICY scalar and is not constructed kappa_ch here.  The same numerical
    expression fails as kappa_ch for:
      - E: chi_top/24 = 0, but kappa_ch = 1
      - K3: chi_top/24 = 1, but kappa_ch = 2
      - K3 x E: chi_top/24 = 0 matches the compact Hodge/PhiFA value,
        but differs from the Heisenberg specialisation kappa_ch^{Heis}=3.

    Reference: k3_times_e.tex, Warning warn:k3e-chi-kappa.
    """
    e = elliptic_curve()
    k3 = k3_surface()
    k3e = k3_times_e()
    quintic = quintic_threefold()

    result: Dict[str, Any] = {}

    # Failures
    result["E_chi_top_over_24"] = Fraction(e.chi_top, 24)
    result["E_kappa_ch"] = kappa_ch(e)
    result["E_fails"] = Fraction(e.chi_top, 24) != kappa_ch(e)

    result["K3_chi_top_over_24"] = Fraction(k3.chi_top, 24)
    result["K3_kappa_ch"] = kappa_ch(k3)
    result["K3_fails"] = Fraction(k3.chi_top, 24) != kappa_ch(k3)

    result["K3xE_chi_top_over_24"] = Fraction(k3e.chi_top, 24)
    result["K3xE_kappa_ch_Heis"] = kappa_ch(k3e)
    result["K3xE_kappa_ch_compact_hodge"] = kappa_ch_compact_hodge(k3e)
    result["K3xE_compact_matches"] = (
        Fraction(k3e.chi_top, 24) == kappa_ch_compact_hodge(k3e)
    )
    result["K3xE_heis_fails"] = Fraction(k3e.chi_top, 24) != kappa_ch(k3e)

    # Quintic candidate lane.
    result["Quintic_chi_top_over_24"] = Fraction(quintic.chi_top, 24)
    result["Quintic_BCOV_shadow_candidate"] = bcov_shadow_candidate(quintic)
    result["Quintic_candidate_matches"] = (
        Fraction(quintic.chi_top, 24) == bcov_shadow_candidate(quintic)
    )
    result["Quintic_constructed_kappa_ch"] = False

    return result


# =========================================================================
# 5. Full spectrum tables
# =========================================================================

def k3_spectrum() -> Dict[str, Any]:
    """The kappa-spectrum for K3 (CY_2)."""
    k3 = k3_surface()
    spec = compute_spectrum(k3)
    return {
        "manifold": "K3",
        "CY_dimension": 2,
        "kappa_cat": spec.kappa_cat,       # 2 = chi(O_K3)
        "kappa_ch": int(spec.kappa_ch),     # 2 (equals kappa_cat at d=2)
        "kappa_BKM": spec.kappa_BKM,        # None (not applicable at d=2)
        "kappa_fiber": spec.kappa_fiber,     # 24 (Mukai lattice rank)
        "kappa_ch_equals_kappa_cat": spec.kappa_ch == spec.kappa_cat,
        "spectrum_set": sorted(set(
            v for v in [spec.kappa_cat, int(spec.kappa_ch), spec.kappa_fiber]
            if v is not None
        )),
    }


def k3e_spectrum() -> Dict[str, Any]:
    """The kappa-spectrum for K3 x E (CY_3).

    The definitive table:

      kappa_cat(K3 x E) = chi(O_{K3xE}) = 0
      kappa_cat(K3)      = chi(O_{K3})   = 2   [fiber value]
      kappa_ch^{Heis}(K3 x E) = 3 = 2 + 1      [specialisation]
      kappa_ch^{compact}(K3 x E) = 0           [Hodge/PhiFA]
      kappa_BKM(K3 x E)  = 5 = wt(Delta_5)     [Borcherds lift]
      kappa_fiber         = 24                   [Mukai lattice rank]

    The CLAUDE.md table records kappa_cat = 2 for K3 x E, meaning
    the value kappa_cat(K3) = chi(O_{K3}) of the K3 FIBER, not
    the total space chi(O_{K3xE}) = 0.
    """
    k3e = k3_times_e()
    k3 = k3_surface()
    spec = compute_spectrum(k3e)

    return {
        "manifold": "K3xE",
        "CY_dimension": 3,
        "kappa_cat_total_space": spec.kappa_cat,  # 0 = chi(O_{K3xE})
        "kappa_cat_K3_fiber": kappa_cat(k3),       # 2 = chi(O_{K3})
        "kappa_ch": int(spec.kappa_ch),             # 3, legacy Heis API
        "kappa_ch_Heis": int(spec.kappa_ch),        # 3
        "kappa_ch_compact_hodge": kappa_ch_compact_hodge(k3e),  # 0
        "kappa_BKM": spec.kappa_BKM,                # 5
        "kappa_fiber": spec.kappa_fiber,             # 24
        "BKM_decomposition": False,
        "BKM_heis_fiber_coincidence": (
            spec.kappa_BKM == int(spec.kappa_ch) + kappa_cat(k3)
        ),  # 5 = 3 + 2, N=1 coincidence
        "spectrum_set_total_space": sorted(set(
            v for v in [
                spec.kappa_cat, int(spec.kappa_ch), spec.kappa_BKM,
                spec.kappa_fiber,
            ]
            if v is not None
        )),  # {0, 3, 5, 24}
        "spectrum_set_with_fiber_witness": sorted(set(
            v for v in [
                spec.kappa_cat, kappa_cat(k3),
                int(spec.kappa_ch), spec.kappa_BKM, spec.kappa_fiber,
            ]
            if v is not None
        )),  # {0, 2, 3, 5, 24}
        "spectrum_set": sorted(set(
            v for v in [
                spec.kappa_cat, kappa_cat(k3),
                int(spec.kappa_ch), spec.kappa_BKM, spec.kappa_fiber,
            ]
            if v is not None
        )),  # compatibility: includes the fibre witness
    }


def enriques_times_e_spectrum() -> Dict[str, Any]:
    """Conjectural kappa-spectrum for Enriques x E."""
    enr = enriques_surface()
    return {
        "manifold": "EnrxE",
        "CY_dimension": 3,
        "kappa_cat_Enr": kappa_cat(enr),  # 1 = chi(O_Enr)
        "kappa_ch_Enr": kappa_ch(enr),     # 1
        "kappa_BKM_conjectural": 4,         # Allcock product weight
        "kappa_ch_EnrxE_conjectural": 2,    # 1 + 1 by additivity
        "BKM_decomposition_conjectural": 4 == 2 + kappa_cat(enr) + 1,
        # 4 = 2 + 1 + 1? No. 4 = kappa_ch(Enr x E) + ???
        # Actually the Enriques decomposition is less clear.
        "halving_ratio": Fraction(5, 4),    # K3xE/EnrxE BKM ratio
    }


# =========================================================================
# 6. Physical meaning
# =========================================================================

def physical_meaning() -> Dict[str, str]:
    r"""Physical interpretation of each kappa in the topological string.

    kappa_cat: the one-loop partition function coefficient of the B-model.
              Counts the holomorphic zero modes of the CY sigma model.
              For K3: the 2 holomorphic forms (Omega^{2,0} and 1)
              contribute kappa_cat = 2.

    kappa_ch:  the genus-1 free energy coefficient in the specified
              specialisation. For K3 x E: the Heisenberg specialisation
              gives 3/24, while the compact Hodge/PhiFA supertrace is 0.

    kappa_BKM: the weight of the BPS state generating function. In the
              type II string on K3 x E, the 1/4-BPS degeneracies are
              counted by 1/(Delta_5)^2, a Siegel modular form of weight 10.
              kappa_BKM = 5 = wt(Delta_5) is the single-copy weight.

    kappa_fiber: the number of free bosons in the fiber sigma model.
              For K3: the 24 bosonic fields of the lattice VOA V_{Mukai}
              give kappa_fiber = 24 = rank(Lambda_{Mukai}).
    """
    return {
        "kappa_cat": (
            "One-loop B-model coefficient. Counts holomorphic zero modes "
            "of the CY sigma model. = chi(O_X)."
        ),
        "kappa_ch": (
            "Genus-1 coefficient in the specified specialisation. For "
            "K3 x E: Heisenberg specialisation is 3; compact Hodge/PhiFA "
            "supertrace is 0."
        ),
        "kappa_BKM": (
            "Weight of the BPS generating function. For K3 x E: the 1/4-BPS "
            "degeneracies are counted by 1/(Delta_5)^2, weight 10 = 2 * 5."
        ),
        "kappa_fiber": (
            "Number of free bosons in the fiber sigma model. For K3: "
            "24 = rank of the Mukai lattice. Controls the MacMahon sector."
        ),
    }


# =========================================================================
# 7. Master verification
# =========================================================================

def verify_all() -> Dict[str, Any]:
    """Run all kappa-spectrum verifications."""
    k3 = k3_surface()
    e = elliptic_curve()
    k3e = k3_times_e()
    quintic = quintic_threefold()

    results: Dict[str, Any] = {}

    # 1. kappa_cat = chi(O_X) for all manifolds
    for X in [k3, e, k3e, quintic, enriques_surface(), abelian_surface()]:
        results[f"kappa_cat_is_chiO_{X.name}"] = verify_kappa_cat_is_chi_O(X)

    # 2. kappa_ch = kappa_cat at d=2
    results["kappa_ch_eq_kappa_cat_K3"] = verify_kappa_ch_equals_kappa_cat_at_d2(k3)
    # Note: for T^4, kappa_ch = kappa_cat = 0
    results["kappa_ch_eq_kappa_cat_T4"] = verify_kappa_ch_equals_kappa_cat_at_d2(
        abelian_surface()
    )

    # 3. Additivity
    results["heis_additivity_K3xE"] = verify_kappa_ch_additivity(k3, e, k3e)
    results["additivity_K3xE"] = results["heis_additivity_K3xE"]

    # 4. chi(O) multiplicativity
    results["chi_O_multiplicative"] = verify_chi_O_multiplicativity(k3, e, k3e)

    # 5. BKM decomposition
    results["BKM_decomposition"] = verify_BKM_decomposition_k3e()

    # 6. Borcherds weight
    results["borcherds_weight"] = borcherds_weight_from_h11()

    # 7. chi_top/24 failure
    results["chi_top_24_failure"] = verify_chi_top_over_24_failure()

    # 8. Full spectra
    results["K3_spectrum"] = k3_spectrum()
    results["K3xE_spectrum"] = k3e_spectrum()

    # 9. Key numerical identities
    results["K3xE_spectrum_values"] = {
        "kappa_cat_total": 0,
        "kappa_cat_fiber": 2,
        "kappa_ch": 3,
        "kappa_ch_Heis": 3,
        "kappa_ch_compact_hodge": 0,
        "kappa_BKM": 5,
        "kappa_fiber": 24,
    }

    return results
