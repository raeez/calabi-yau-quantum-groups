r"""Shadow tower behaviour at the conifold transition.

A CY3 X develops a nodal singularity (S^3 shrinks to zero size) then
resolves by replacing S^3 with S^2 (small resolution).  This is the
conifold transition.  The Hodge numbers change:

    h^{1,1} -> h^{1,1} + 1,   h^{2,1} -> h^{2,1} - 1.

Example: quintic (1, 101) -> conifold point -> resolved (2, 100).

MATHEMATICAL CONTENT
====================

1. SMOOTH PHASE (before transition).

   The smooth quintic Q in P^4 has h^{1,1}=1, h^{2,1}=101, chi=-200.
   BCOV-shadow candidate chi/24 = -25/3 (fractional; AP-CY157: this is
   the CONIFOLD degeneration type, not large complex structure).  This is
   not promoted to constructed kappa_ch in this engine.

   The shadow tower is class M (infinite depth) because the quintic
   has infinitely many nonzero GV invariants n^0_d for all d >= 1.
   The shadow coefficients S_k receive contributions from each BPS state.

2. AT THE CONIFOLD POINT.

   A single massless BPS hypermultiplet appears: the D3-brane wrapping
   the vanishing 3-cycle (S^3 -> 0).  The period integral has a log
   singularity:

       Pi(t) ~ t * log(t) + (regular)    near t = 0.

   This log singularity enters the chiral algebra through the deformation
   parameter: the chiral algebra OPE acquires a logarithmic correction.

   SHADOW TOWER AT THE CONIFOLD POINT:
     - The shadow metric Q_L(t) develops a zero: Delta -> 0 as the
       vanishing cycle shrinks.  This is the shadow-tower manifestation
       of the massless BPS state.
     - The shadow depth remains infinite (class M), but the shadow
       coefficients S_k acquire a log-divergent correction:
         S_k^{conifold} = S_k^{smooth} + delta_k^{log}
       where delta_k^{log} ~ (-1)^k / k (from the log period).

3. AFTER RESOLUTION (resolved phase).

   The resolved CY3 X' has h^{1,1}=2, h^{2,1}=100, chi=-196.
   The new P^1 = S^2 contributes a new curve class beta_new.

   GV invariant: n^0_{beta_new} = 1 (the vanishing cycle, now resolved).
   This is the SEED of the new shadow channel.

   Each GV invariant n^g_beta contributes to the shadow tower:
     - genus 0 BPS state: contributes to S_2 (arity 2, = kappa sector)
     - genus g BPS state: contributes to S_{2+2g} (arity 2+2g)

   The GV-to-shadow dictionary:
     S_k^{GV} = sum_{g,beta} n^g_beta * K_k(g, beta)
   where K_k is the multi-cover kernel at arity k.

4. HODGE NUMBER CHANGE AND KAPPA.

   chi = 2*(h^{1,1} - h^{2,1}).
   Before: chi = 2*(1-101) = -200.  After: chi = 2*(2-100) = -196.
   Change: Delta_chi = 4 = 2 * (Delta_h11 + Delta_h21) with
           Delta_h11 = +1, Delta_h21 = -1.

   The conifold transition changes chi by +4 per node resolved.
   For k nodes: Delta_chi = 4k.

   In the BCOV-shadow candidate lane chi/24:
     Before: -200/24 = -25/3.
     After:  -196/24 = -49/12.
     Delta_kappa = 4/24 = 1/6 per node.

5. THE SEED MECHANISM: n^0_1 = 1.

   The GV invariant n^0_1 = 1 for the vanishing cycle is the minimal
   nontrivial input to the shadow tower.  A single genus-0 BPS state
   of charge beta contributes:
     S_2 += 1 (from the genus-0 BPS state, arity 2)
     S_k = 0 for k >= 3 (genus 0 has no higher arity)

   This is a CLASS G contribution (Gaussian, depth 2) -- the simplest
   possible shadow channel.  The conifold transition ADDS a single
   class-G shadow channel on top of the existing class-M tower.

   Schematically:
     shadow_tower(X') = shadow_tower(X) + class_G_channel(n^0_1=1)

   The class-G channel has kappa = 1 (matching the resolved conifold's
   kappa_ch = 1).  This is the shadow-tower explanation for why the
   resolved conifold is class G: it is PRECISELY the class-G channel
   that the conifold transition adds.

CONVENTIONS
===========

  - Degeneration type: CONIFOLD (AP-CY157). Not large complex structure.
  - kappa subscripts required (AP113): kappa_ch, kappa_BKM, kappa_cat.
  - CY dimension n-2 for MF(W) (AP-CY17).
  - All formal statements are CONJECTURAL at d=3 (AP-CY6/AP-CY14).
  - GV invariants n^g_beta are INTEGERS (Gopakumar-Vafa integrality).
  - chi = 2*(h^{1,1} - h^{2,1}) for CY3 (Hodge diamond symmetry).
  - Exact arithmetic via fractions.Fraction.

REFERENCES
==========

  Candelas-de la Ossa-Green-Parkes, NPB 359 (1991) 21
  Gopakumar-Vafa, hep-th/9809187, hep-th/9812127
  Greene-Morrison-Strominger, hep-th/9504145 (conifold transition)
  Strominger, hep-th/9504090 (massless black hole at conifold)
  Clemens, "Double solids" (Adv. Math. 47, 1983)
  Friedman, "Simultaneous resolution of threefold double points"
  Reid, "The moduli space of 3-folds with K=0" (Math. Ann. 278, 1987)
  Vol I: shadow obstruction tower, kappa, bar complex
  Vol III: conifold_wall_crossing.py, conifold_bar_complex.py
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Tuple
import math


# =========================================================================
# 1. CY3 DATA ACROSS THE CONIFOLD TRANSITION
# =========================================================================

class ConifoldTransitionData(NamedTuple):
    """Hodge and shadow data for a CY3 undergoing a conifold transition.

    Tracks Hodge numbers, Euler characteristic, and conjectural kappa
    on both sides of the transition, plus the number of nodes resolved.
    """
    name: str
    # Before transition (smooth phase)
    h11_before: int
    h21_before: int
    chi_before: int
    kappa_ch_before: Fraction  # legacy field: BCOV-shadow candidate chi/24
    # After transition (resolved phase)
    h11_after: int
    h21_after: int
    chi_after: int
    kappa_ch_after: Fraction   # legacy field: BCOV-shadow candidate chi/24
    # Transition data
    num_nodes: int             # number of nodes resolved
    delta_chi: int             # chi_after - chi_before = 4 * num_nodes
    delta_kappa: Fraction      # kappa_after - kappa_before


def conifold_transition_data(name: str, h11: int, h21: int,
                             num_nodes: int = 1) -> ConifoldTransitionData:
    """Compute Hodge and kappa data across a conifold transition.

    The conifold transition resolves num_nodes ordinary double points:
      h^{1,1} -> h^{1,1} + num_nodes
      h^{2,1} -> h^{2,1} - num_nodes

    BCOV-shadow candidate = chi/24 for compact CY3 (AP-CY157: conifold
    degeneration type).  The field names are legacy API names; their
    values are not constructed kappa_ch.
    """
    chi_before = 2 * (h11 - h21)
    h11_after = h11 + num_nodes
    h21_after = h21 - num_nodes
    chi_after = 2 * (h11_after - h21_after)
    delta_chi = chi_after - chi_before

    kappa_before = Fraction(chi_before, 24)
    kappa_after = Fraction(chi_after, 24)
    delta_kappa = kappa_after - kappa_before

    return ConifoldTransitionData(
        name=name,
        h11_before=h11,
        h21_before=h21,
        chi_before=chi_before,
        kappa_ch_before=kappa_before,
        h11_after=h11_after,
        h21_after=h21_after,
        chi_after=chi_after,
        kappa_ch_after=kappa_after,
        num_nodes=num_nodes,
        delta_chi=delta_chi,
        delta_kappa=delta_kappa,
    )


def quintic_conifold_transition() -> ConifoldTransitionData:
    """The standard quintic conifold transition.

    Quintic P^4[5]: h^{1,1}=1, h^{2,1}=101.
    One node: (1,101) -> (2,100).
    """
    return conifold_transition_data("quintic", 1, 101, num_nodes=1)


def multi_node_quintic_transition(num_nodes: int) -> ConifoldTransitionData:
    """Quintic with multiple nodes resolved simultaneously.

    The quintic admits up to 125 ordinary double points (Barth's bound
    is not saturated; the actual maximum for quintic threefolds is 130
    due to Werner-van Geemen, but the standard conifold family has
    fewer nodes).

    For k nodes: (1, 101) -> (1+k, 101-k), valid for k <= 101.
    """
    if num_nodes > 101:
        raise ValueError(f"Cannot resolve {num_nodes} nodes: h^{{2,1}}=101")
    return conifold_transition_data("quintic", 1, 101, num_nodes=num_nodes)


# Standard conifold transition examples
CONIFOLD_TRANSITIONS: Dict[str, Tuple[int, int, int]] = {
    "quintic_1node": (1, 101, 1),
    "quintic_16nodes": (1, 101, 16),
    "P5[3,3]_1node": (1, 73, 1),
    "P5[2,4]_1node": (1, 89, 1),
    "Schoen_1node": (19, 19, 1),
}


def all_conifold_transitions() -> List[ConifoldTransitionData]:
    """Compute conifold transition data for all standard examples."""
    results = []
    for name, (h11, h21, nodes) in CONIFOLD_TRANSITIONS.items():
        results.append(conifold_transition_data(name, h11, h21, nodes))
    return results


# =========================================================================
# 2. CONIFOLD PERIOD AND LOG SINGULARITY
# =========================================================================

def conifold_period_expansion(psi: Fraction, num_terms: int = 10,
                              ) -> List[Fraction]:
    r"""Power series expansion of the conifold period near the conifold point.

    Near the conifold point z = z_c (Candelas et al.), the period integral
    has a log singularity. Writing t = z - z_c as the local coordinate:

        Pi_conifold(t) = a_0 * t * log(t) + sum_{k>=1} b_k * t^k

    where a_0 = 1/(2*pi*i) and b_k are the regular part coefficients.

    The log term comes from the monodromy around the conifold point:
    the monodromy matrix M_c has a unipotent part (M_c - I)^2 = 0 but
    (M_c - I) != 0. This is the signature of a single vanishing cycle.

    For the quintic: z_c = 1/5^5 = 1/3125, and the conifold monodromy is
        M_c = I + N_c, where N_c is a single nilpotent Jordan block
        with N_c^2 = 0 (rank 1 nilpotent from the single vanishing S^3).

    Parameters:
        psi: the deformation parameter (= 5*z^{1/5} in the quintic mirror)
        num_terms: number of terms in the regular part expansion

    Returns:
        List of Fraction coefficients [b_0, b_1, ..., b_{num_terms-1}]
        representing the REGULAR part of the period.
        The LOG coefficient a_0 = 1 (normalized).

    The full period is: Pi = t * log(t) + sum b_k * t^k.
    """
    # Regular part coefficients for the conifold period
    # These come from expanding the Meijer G-function near z = z_c
    # b_k = (-1)^k * H_k / k! where H_k = harmonic number
    coeffs = []
    harmonic = Fraction(0)
    factorial_inv = Fraction(1)
    for k in range(num_terms):
        if k == 0:
            coeffs.append(Fraction(1))  # b_0 = 1 (normalization)
        else:
            harmonic += Fraction(1, k)
            factorial_inv = factorial_inv / Fraction(k)
            # b_k = (-1)^k * H_k / k!
            coeffs.append(Fraction((-1) ** k) * harmonic * factorial_inv)
    return coeffs


def conifold_monodromy_data() -> Dict[str, Any]:
    r"""Monodromy data at the conifold point.

    The monodromy matrix M_c around the conifold point in the (h^{2,1}+1)-
    dimensional period vector space has the form:

        M_c = I + N_c

    where N_c is nilpotent of index 2 (N_c^2 = 0) and rank 1.
    The log of the monodromy is N_c itself (since N_c^2 = 0):

        log(M_c) = N_c - N_c^2/2 + ... = N_c.

    The Picard-Lefschetz formula for the monodromy around a vanishing
    cycle delta (an S^3 with [delta]^2 = 0 in H_3(X)):

        M_c(gamma) = gamma + <gamma, delta> * delta

    where <,> is the intersection pairing on H_3(X, Z).

    For the quintic: H_3(Q, Z) has rank 4 = 2*(h^{2,1}+1) = 2*102 = 204.
    The vanishing cycle delta spans a rank-1 sublattice of H_3.
    """
    return {
        "monodromy_type": "unipotent_index_2",
        "nilpotent_rank": 1,
        "nilpotent_index": 2,
        "formula": "M_c(gamma) = gamma + <gamma, delta> * delta",
        "log_monodromy": "N_c = M_c - I, with N_c^2 = 0",
        "vanishing_cycle_self_intersection": 0,
        "degeneration_type": "conifold",  # AP-CY157
    }


# =========================================================================
# 3. GOPAKUMAR-VAFA INVARIANTS AND THE SEED MECHANISM
# =========================================================================

# GV invariants for the vanishing cycle class (genus 0)
# n^0_{beta_vanishing} = 1 for a single conifold node
GV_CONIFOLD_SEED: Dict[Tuple[int, int], int] = {
    # (genus, degree): n^g_d
    (0, 1): 1,   # THE SEED: single genus-0 BPS state from vanishing cycle
}

# Known GV invariants for the quintic (genus 0, low degree)
# From Candelas et al. and subsequent work
QUINTIC_GV_GENUS0: Dict[int, int] = {
    1: 2875,
    2: 609250,
    3: 317206375,
    4: 242467530000,
    5: 229305888887625,
    6: 248249742118022000,
    7: 295091050570845659250,
    8: 375632160937476603550000,
    9: 503840510416985243645106250,
    10: 704288164978454686113488249750,
}


def gv_seed_contribution(n_g_beta: int, genus: int,
                         ) -> Dict[str, Any]:
    r"""Shadow tower contribution from a single GV invariant n^g_beta.

    A genus-g BPS state of GV multiplicity n contributes to the
    shadow tower at arity 2 + 2g:

      S_{2+2g} += n * (universal coefficient at genus g)

    The universal coefficient comes from the multi-cover formula:
    the contribution of a genus-g curve to the genus-g' topological
    string amplitude involves the Hodge integral

        integral_{M_{g,0}} lambda_g^{2g-2}

    which gives the Faber-Pandharipande constant:
        F_g^{const} = |B_{2g}| / (2g * (2g-2)!)

    where B_{2g} is the Bernoulli number.

    For genus 0: contributes to S_2 (arity 2 = kappa sector).
        delta_S_2 = n (direct count of BPS states).

    For genus 1: contributes to S_4 (arity 4).
        delta_S_4 = n * 1/12 (from lambda_1 integral on M_{1,1}).

    For genus g >= 2: contributes to S_{2+2g}.
        delta_S_{2+2g} = n * |B_{2g}| / (2g * (2g-2)!).
    """
    target_arity = 2 + 2 * genus

    if genus == 0:
        coefficient = Fraction(1)
    elif genus == 1:
        coefficient = Fraction(1, 12)
    else:
        # |B_{2g}| / (2g * (2g-2)!)
        # Bernoulli numbers (absolute values of even-index)
        bernoulli_abs = _bernoulli_even_abs(genus)
        factorial_val = _factorial(2 * genus - 2)
        coefficient = bernoulli_abs / (Fraction(2 * genus) * factorial_val)

    contribution = Fraction(n_g_beta) * coefficient

    # Shadow class determination from the seed
    if genus == 0:
        shadow_class_contribution = "G"
        shadow_depth_contribution = 2
    else:
        shadow_class_contribution = "M"
        shadow_depth_contribution = target_arity

    return {
        "genus": genus,
        "n_g_beta": n_g_beta,
        "target_arity": target_arity,
        "coefficient": str(coefficient),
        "contribution_to_shadow": str(contribution),
        "shadow_class_contribution": shadow_class_contribution,
        "shadow_depth_contribution": shadow_depth_contribution,
    }


def _bernoulli_even_abs(g: int) -> Fraction:
    """Absolute value of B_{2g} for small g.

    B_2 = 1/6, B_4 = -1/30, B_6 = 1/42, B_8 = -1/30, B_10 = 5/66, ...
    |B_{2g}| is always positive.
    """
    # Precomputed |B_{2g}| for g = 0, 1, ..., 10
    bernoulli_table = {
        0: Fraction(1),
        1: Fraction(1, 6),
        2: Fraction(1, 30),
        3: Fraction(1, 42),
        4: Fraction(1, 30),
        5: Fraction(5, 66),
        6: Fraction(691, 2730),
        7: Fraction(7, 6),
        8: Fraction(3617, 510),
        9: Fraction(43867, 798),
        10: Fraction(174611, 330),
    }
    if g in bernoulli_table:
        return bernoulli_table[g]
    raise ValueError(f"|B_{{2g}}| not tabulated for g={g}")


def _factorial(n: int) -> Fraction:
    """n! as a Fraction."""
    result = Fraction(1)
    for k in range(2, n + 1):
        result *= Fraction(k)
    return result


# =========================================================================
# 4. SHADOW TOWER ACROSS THE TRANSITION
# =========================================================================

class ShadowTowerData(NamedTuple):
    """Shadow tower data for a CY3 at a specific phase."""
    phase: str          # "smooth", "conifold_point", "resolved"
    kappa_ch: Fraction  # legacy field: constructed kappa_ch or BCOV-shadow candidate
    shadow_class: str   # "G", "L", "C", "M"
    shadow_depth: int   # 2 for G, infinity for M (encoded as -1)
    S_2: Fraction       # arity-2 shadow in the same scalar lane
    S_3: Fraction       # cubic shadow
    S_4: Fraction       # quartic shadow
    log_correction: bool  # whether log period correction is present


def shadow_tower_smooth_quintic() -> ShadowTowerData:
    """Shadow tower of the smooth quintic (before conifold transition).

    BCOV-shadow candidate = -25/3 (from chi/24).
    Class M: infinite depth (from GV invariants).
    S_2 = -25/3 in this conjectural shadow lane.
    S_3: unknown (requires the quintic chiral algebra OPE).
    S_4: unknown (requires quartic contact invariant).

    We set S_3, S_4 to formal placeholders (0) since we do not have
    the quintic chiral algebra explicitly.
    """
    kappa = Fraction(-25, 3)
    return ShadowTowerData(
        phase="smooth",
        kappa_ch=kappa,
        shadow_class="M",
        shadow_depth=-1,    # infinite
        S_2=kappa,
        S_3=Fraction(0),    # unknown: placeholder
        S_4=Fraction(0),    # unknown: placeholder
        log_correction=False,
    )


def shadow_tower_conifold_point() -> ShadowTowerData:
    r"""Shadow tower at the conifold point.

    At the conifold point, the period has a log singularity:
        Pi ~ t * log(t).

    This produces a logarithmic correction to the shadow coefficients.
    The constructed kappa_ch is ill-defined at the singular point (the
    chiral algebra degenerates), but the BCOV-shadow limit from the
    smooth side gives -25/3.

    The massless BPS state contributes an additional term to S_2:
        delta_S_2 = 1 (from n^0_1 = 1, the vanishing cycle).

    But this contribution is offset by the degeneration of the
    existing spectrum, so the NET change in S_2 is:
        S_2^{conifold} = S_2^{smooth} + delta_S_2^{massless}

    The log correction enters through the period matrix:
        tau_{ij} -> tau_{ij} + (1/(2*pi*i)) * log(t) * delta_{ij}^{sing}
    where delta^{sing} is supported on the vanishing cycle.
    """
    kappa = Fraction(-25, 3)
    return ShadowTowerData(
        phase="conifold_point",
        kappa_ch=kappa,          # limit from smooth side
        shadow_class="M",
        shadow_depth=-1,         # infinite
        S_2=kappa + Fraction(1), # smooth contribution + massless BPS
        S_3=Fraction(0),         # placeholder
        S_4=Fraction(0),         # placeholder
        log_correction=True,
    )


def shadow_tower_resolved(num_nodes: int = 1) -> ShadowTowerData:
    """Shadow tower after the conifold transition (resolved phase).

    The resolved CY3 X' has:
        h^{1,1} = 1 + num_nodes
        h^{2,1} = 101 - num_nodes
        chi = -200 + 4*num_nodes

    BCOV-shadow candidate = chi'/24 (conjectural).
    Class M: still infinite depth.

    The new shadow data decomposes as:
        shadow(X') = shadow(X)_surviving + sum_i seed_channel(node_i)

    Each resolved node contributes a class-G seed channel with
    kappa = 1/6 (= delta_kappa per node).

    The shadow tower of the resolved phase is still class M because
    the surviving smooth-phase contributions have infinite depth.
    The seed channels are class G (depth 2) and do not affect the
    overall depth classification.
    """
    kappa = Fraction(-200 + 4 * num_nodes, 24)
    return ShadowTowerData(
        phase="resolved",
        kappa_ch=kappa,
        shadow_class="M",
        shadow_depth=-1,       # infinite (from surviving class-M tower)
        S_2=kappa,
        S_3=Fraction(0),       # placeholder
        S_4=Fraction(0),       # placeholder
        log_correction=False,
    )


def shadow_transition_comparison(num_nodes: int = 1,
                                 ) -> Dict[str, Any]:
    """Compare shadow tower data across all three phases.

    Returns a dictionary with the shadow data at each phase and
    the transition analysis.
    """
    smooth = shadow_tower_smooth_quintic()
    conifold = shadow_tower_conifold_point()
    resolved = shadow_tower_resolved(num_nodes)

    hodge = conifold_transition_data("quintic", 1, 101, num_nodes)

    return {
        "smooth_phase": {
            "kappa_ch": str(smooth.kappa_ch),
            "shadow_class": smooth.shadow_class,
            "S_2": str(smooth.S_2),
            "log_correction": smooth.log_correction,
        },
        "conifold_point": {
            "kappa_ch": str(conifold.kappa_ch),
            "shadow_class": conifold.shadow_class,
            "S_2": str(conifold.S_2),
            "log_correction": conifold.log_correction,
        },
        "resolved_phase": {
            "kappa_ch": str(resolved.kappa_ch),
            "shadow_class": resolved.shadow_class,
            "S_2": str(resolved.S_2),
            "log_correction": resolved.log_correction,
        },
        "transition_data": {
            "num_nodes": num_nodes,
            "delta_chi": hodge.delta_chi,
            "delta_kappa": str(hodge.delta_kappa),
            "hodge_before": (hodge.h11_before, hodge.h21_before),
            "hodge_after": (hodge.h11_after, hodge.h21_after),
        },
        "seed_data": {
            "gv_invariant": "n^0_1 = 1 (vanishing cycle)",
            "seed_class": "G (Gaussian, depth 2)",
            "seed_kappa": str(Fraction(1, 6)),
        },
    }


# =========================================================================
# 5. GV-TO-SHADOW DICTIONARY
# =========================================================================

def gv_to_shadow_tower(gv_invariants: Dict[Tuple[int, int], int],
                       max_arity: int = 8,
                       ) -> Dict[int, Fraction]:
    r"""Convert GV invariants to shadow tower contributions.

    The GV-to-shadow dictionary maps each GV invariant n^g_beta to
    a shadow tower contribution at arity 2 + 2g:

        S_k^{GV} = sum_{g: 2+2g=k} sum_beta n^g_beta * C_g

    where C_g is the genus-g BPS-to-shadow coefficient:
        C_0 = 1 (genus 0: direct count)
        C_1 = 1/12 (genus 1: from lambda_1 on M_{1,1})
        C_g = |B_{2g}| / (2g * (2g-2)!) for g >= 2

    Parameters:
        gv_invariants: dict of {(genus, degree): n^g_d}
        max_arity: maximum arity to compute

    Returns:
        dict of {arity: S_arity} shadow tower contributions
    """
    shadow = {}
    for k in range(2, max_arity + 1, 2):
        shadow[k] = Fraction(0)

    for (genus, degree), n_gd in gv_invariants.items():
        arity = 2 + 2 * genus
        if arity > max_arity:
            continue

        if genus == 0:
            coeff = Fraction(1)
        elif genus == 1:
            coeff = Fraction(1, 12)
        else:
            try:
                bernoulli_abs = _bernoulli_even_abs(genus)
                factorial_val = _factorial(2 * genus - 2)
                coeff = bernoulli_abs / (Fraction(2 * genus) * factorial_val)
            except ValueError:
                continue

        if arity not in shadow:
            shadow[arity] = Fraction(0)
        shadow[arity] += Fraction(n_gd) * coeff

    return shadow


def conifold_seed_shadow() -> Dict[str, Any]:
    r"""The shadow tower contribution from the conifold seed n^0_1 = 1.

    The vanishing cycle contributes a single genus-0 BPS state with
    GV invariant n^0_1 = 1. This is the minimal nontrivial input
    to the shadow tower.

    The contribution is:
        S_2 += 1 (arity 2, the kappa sector)
        S_k = 0 for k >= 3 (no higher-genus contributions)

    This is a class G (Gaussian) channel of depth 2.
    """
    gv = {(0, 1): 1}
    shadow = gv_to_shadow_tower(gv, max_arity=8)

    return {
        "gv_invariant": "n^0_1 = 1",
        "shadow_tower": {str(k): str(v) for k, v in shadow.items()},
        "shadow_class": "G",
        "shadow_depth": 2,
        "interpretation": (
            "The conifold seed n^0_1 = 1 contributes a single class-G "
            "shadow channel with S_2 = 1 (kappa = 1 for the vanishing "
            "cycle). This is the minimal nontrivial shadow input: a "
            "single genus-0 BPS state produces a Gaussian channel of "
            "depth 2, matching the resolved conifold's shadow data."
        ),
    }


def quintic_gv_shadow(max_degree: int = 5) -> Dict[str, Any]:
    r"""Shadow tower contributions from the quintic GV invariants.

    The quintic has large genus-0 GV invariants (2875, 609250, ...),
    all of which contribute to S_2.  The rapid growth of n^0_d implies
    S_2 diverges as we include all degrees, reflecting the need for
    regularization (analogous to the MacMahon divergence for C^3).

    For finite degree cutoff d <= max_degree, S_2 is finite.
    """
    gv = {}
    for d in range(1, max_degree + 1):
        if d in QUINTIC_GV_GENUS0:
            gv[(0, d)] = QUINTIC_GV_GENUS0[d]

    shadow = gv_to_shadow_tower(gv, max_arity=4)

    # S_2 = sum of all genus-0 GV invariants through degree max_degree
    s2_total = sum(QUINTIC_GV_GENUS0.get(d, 0)
                   for d in range(1, max_degree + 1))

    return {
        "max_degree": max_degree,
        "gv_invariants_used": {str(d): QUINTIC_GV_GENUS0[d]
                                for d in range(1, max_degree + 1)
                                if d in QUINTIC_GV_GENUS0},
        "shadow_S2_from_gv": str(Fraction(s2_total)),
        "shadow_tower": {str(k): str(v) for k, v in shadow.items()},
        "growth_rate": "faster than exponential (class M)",
        "interpretation": (
            f"The quintic GV invariants through degree {max_degree} "
            f"contribute S_2 = {s2_total} to the shadow tower. The "
            f"rapid growth of n^0_d (2875, 609250, 317206375, ...) "
            f"confirms class M (infinite depth, divergent tower)."
        ),
    }


# =========================================================================
# 6. LOG PERIOD CORRECTION TO SHADOW COEFFICIENTS
# =========================================================================

def log_period_shadow_correction(max_arity: int = 8,
                                 ) -> Dict[str, Any]:
    r"""Logarithmic correction to shadow coefficients at the conifold point.

    The conifold period Pi ~ t*log(t) introduces a log correction to
    the shadow coefficients via the deformation parameter.

    The correction arises because the central charge Z(gamma) of the
    massless BPS state vanishes at the conifold point:

        Z(gamma_vanishing) = integral_{S^3} Omega -> 0

    The vanishing of Z produces a log term in the prepotential:

        F_0 = (1/2) * t^2 * log(t) + (polynomial in t)

    where t = Z(gamma_vanishing) is the period of the vanishing cycle.

    At the level of the shadow tower, this produces:

        delta_S_k = (-1)^{k} * (1/k) * (residue coefficient)

    for each arity k. The sign alternation comes from the expansion
    of log(1 + x) = x - x^2/2 + x^3/3 - ... applied to the
    deformation of the shadow metric.

    The residue coefficient is 1 (normalized): one vanishing cycle,
    one massless state, Picard-Lefschetz monodromy of rank 1.
    """
    corrections = {}
    for k in range(2, max_arity + 1):
        # delta_S_k = (-1)^k / k
        corrections[k] = Fraction((-1) ** k, k)

    return {
        "max_arity": max_arity,
        "corrections": {str(k): str(v) for k, v in corrections.items()},
        "log_coefficient": "1 (one vanishing cycle, rank-1 nilpotent)",
        "degeneration_type": "conifold",  # AP-CY157
        "alternating_sign_source": "expansion of log(1+x) in deformation",
        "interpretation": (
            "The conifold log period produces alternating corrections "
            "to all shadow arities: delta_S_k = (-1)^k / k. These "
            "corrections are the shadow-tower manifestation of the "
            "massless BPS state. The corrections vanish as the "
            "deformation parameter t -> infinity (smooth phase) and "
            "diverge as t -> 0 (conifold point)."
        ),
    }


# =========================================================================
# 7. SHADOW METRIC AND DISCRIMINANT ACROSS THE TRANSITION
# =========================================================================

def shadow_metric_transition(kappa: Fraction,
                             alpha: Fraction = Fraction(0),
                             S_4: Fraction = Fraction(0),
                             ) -> Dict[str, Any]:
    r"""Shadow metric Q_L(t) for a CY3 with given shadow data.

    Q_L(t) = 4*kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 16*kappa*S_4)*t^2

    The discriminant: Delta = (12*kappa*alpha)^2 - 4*(4*kappa^2)*(9*alpha^2 + 16*kappa*S_4)
                            = 144*kappa^2*alpha^2 - 16*kappa^2*(9*alpha^2 + 16*kappa*S_4)
                            = 144*kappa^2*alpha^2 - 144*kappa^2*alpha^2 - 256*kappa^3*S_4
                            = -256*kappa^3*S_4

    Simplified: Delta = -256 * kappa^3 * S_4.

    Shadow depth classification from Delta:
        Delta = 0 and alpha = 0: class G (depth 2)
        Delta = 0 and alpha != 0: class L (depth 3)
        Delta != 0: class M (infinite depth) or class C
    """
    Q_at_0 = 4 * kappa ** 2
    discriminant = Fraction(-256) * kappa ** 3 * S_4

    # Classification
    if alpha == Fraction(0) and S_4 == Fraction(0):
        shadow_class = "G"
        depth = 2
    elif discriminant == Fraction(0) and alpha != Fraction(0):
        shadow_class = "L"
        depth = 3
    else:
        shadow_class = "M"
        depth = -1  # infinite

    return {
        "kappa_ch": str(kappa),
        "alpha": str(alpha),
        "S_4": str(S_4),
        "Q_at_0": str(Q_at_0),
        "discriminant": str(discriminant),
        "shadow_class": shadow_class,
        "shadow_depth": depth,
    }


def shadow_metric_across_transition(num_nodes: int = 1,
                                    ) -> Dict[str, Any]:
    """Compare shadow metrics before and after the transition.

    Before (smooth quintic): kappa = -25/3, alpha and S_4 unknown.
    After (resolved): kappa = (-200 + 4*num_nodes)/24.

    We compute the shadow metric assuming alpha = S_4 = 0 (class G
    approximation) and with illustrative nonzero values.
    """
    kappa_before = Fraction(-25, 3)
    kappa_after = Fraction(-200 + 4 * num_nodes, 24)

    # Class G approximation (alpha = S_4 = 0)
    metric_before_G = shadow_metric_transition(kappa_before)
    metric_after_G = shadow_metric_transition(kappa_after)

    return {
        "before_transition": {
            "kappa_ch": str(kappa_before),
            "class_G_metric": metric_before_G,
        },
        "after_transition": {
            "kappa_ch": str(kappa_after),
            "class_G_metric": metric_after_G,
        },
        "num_nodes": num_nodes,
        "delta_kappa": str(kappa_after - kappa_before),
    }


# =========================================================================
# 8. COMPREHENSIVE SHADOW TRANSITION ANALYSIS
# =========================================================================

def conifold_shadow_transition_comprehensive(
        num_nodes: int = 1,
        max_gv_degree: int = 5,
        max_arity: int = 8,
) -> Dict[str, Any]:
    """Comprehensive analysis of the shadow tower across the conifold transition.

    Combines:
        1. Hodge/kappa data across the transition
        2. Shadow tower in all three phases
        3. GV-to-shadow dictionary
        4. Conifold seed mechanism
        5. Log period corrections
        6. Shadow metric comparison

    All claims conditional on CY-A_3 (AP-CY6/AP-CY14).
    Degeneration type: conifold (AP-CY157).
    """
    # 1. Transition data
    transition = conifold_transition_data("quintic", 1, 101, num_nodes)

    # 2. Shadow towers in all phases
    smooth = shadow_tower_smooth_quintic()
    conifold = shadow_tower_conifold_point()
    resolved = shadow_tower_resolved(num_nodes)

    # 3. GV contributions
    gv_quintic = quintic_gv_shadow(max_gv_degree)
    gv_seed = conifold_seed_shadow()

    # 4. Log corrections
    log_corr = log_period_shadow_correction(max_arity)

    # 5. Shadow metrics
    metric = shadow_metric_across_transition(num_nodes)

    # 6. Monodromy
    monodromy = conifold_monodromy_data()

    # 7. Period expansion
    period = conifold_period_expansion(Fraction(1), num_terms=6)

    return {
        "transition_data": {
            "name": transition.name,
            "hodge_before": (transition.h11_before, transition.h21_before),
            "hodge_after": (transition.h11_after, transition.h21_after),
            "chi_before": transition.chi_before,
            "chi_after": transition.chi_after,
            "delta_chi": transition.delta_chi,
            "kappa_ch_before": str(transition.kappa_ch_before),
            "kappa_ch_after": str(transition.kappa_ch_after),
            "delta_kappa": str(transition.delta_kappa),
            "num_nodes": num_nodes,
        },
        "shadow_phases": {
            "smooth": {
                "kappa_ch": str(smooth.kappa_ch),
                "class": smooth.shadow_class,
                "depth": smooth.shadow_depth,
                "S_2": str(smooth.S_2),
            },
            "conifold_point": {
                "kappa_ch": str(conifold.kappa_ch),
                "class": conifold.shadow_class,
                "depth": conifold.shadow_depth,
                "S_2": str(conifold.S_2),
                "log_correction": conifold.log_correction,
            },
            "resolved": {
                "kappa_ch": str(resolved.kappa_ch),
                "class": resolved.shadow_class,
                "depth": resolved.shadow_depth,
                "S_2": str(resolved.S_2),
            },
        },
        "gv_analysis": {
            "quintic_shadow": gv_quintic,
            "seed": gv_seed,
        },
        "log_period_corrections": log_corr,
        "shadow_metrics": metric,
        "monodromy": monodromy,
        "period_regular_coeffs": [str(c) for c in period],
        "claim_status": "CONJECTURAL (conditional on CY-A_3)",
        "degeneration_type": "conifold (AP-CY157)",
    }


# =========================================================================
# Runner
# =========================================================================

if __name__ == "__main__":
    print("=" * 72)
    print("CONIFOLD SHADOW TRANSITION ANALYSIS")
    print("=" * 72)

    print("\n1. TRANSITION DATA")
    print("-" * 40)
    t = quintic_conifold_transition()
    print(f"  Before: h11={t.h11_before}, h21={t.h21_before}, chi={t.chi_before}")
    print(f"  After:  h11={t.h11_after}, h21={t.h21_after}, chi={t.chi_after}")
    print(f"  Delta chi: {t.delta_chi}, Delta kappa: {t.delta_kappa}")

    print("\n2. SHADOW TOWER COMPARISON")
    print("-" * 40)
    comp = shadow_transition_comparison()
    for phase, data in comp.items():
        if isinstance(data, dict) and "kappa_ch" in data:
            print(f"  {phase}: kappa_ch={data['kappa_ch']}, class={data['shadow_class']}")

    print("\n3. GV SEED")
    print("-" * 40)
    seed = conifold_seed_shadow()
    print(f"  {seed['gv_invariant']}")
    print(f"  Shadow class: {seed['shadow_class']}, depth: {seed['shadow_depth']}")

    print("\n4. LOG CORRECTIONS")
    print("-" * 40)
    lc = log_period_shadow_correction(6)
    for k, v in sorted(lc["corrections"].items()):
        print(f"  delta_S_{k} = {v}")

    print("\n5. QUINTIC GV SHADOW")
    print("-" * 40)
    qgv = quintic_gv_shadow(5)
    print(f"  S_2 from GV (degree <= 5): {qgv['shadow_S2_from_gv']}")
