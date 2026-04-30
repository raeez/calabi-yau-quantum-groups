r"""
quintic_shadow_obstruction.py -- Shadow obstruction tower and chi/24 analysis
for the quintic CY3 and compact Calabi-Yau threefolds.

THE CHI/24 OBSTRUCTION
======================

For K3 x E (non-rigid CY3): chi_top = 0, but the BKM denominator lane has
    kappa_BKM(Delta_5) = weight(Delta_5) = c_1(0)/2 = 10/2 = 5.
    Thus chi_top/24 = 0 and kappa_BKM = 5 are different scalar lanes.

For the quintic Q in P^4: chi = -200, so chi/24 = -25/3, NOT an integer.
This non-integrality is often cited as an obstruction to a naive BKM structure.

KEY DISTINCTION (AP20/AP48):
    kappa_ch(A) is the modular characteristic of a constructed chiral algebra A.
    For the quintic, such an A is not constructed in this engine.
    chi/24 is the ratio of topological Euler characteristic to 24.
    kappa_BKM is the automorphic denominator weight when a BKM denominator
    identity is actually present.
    These are DIFFERENT quantities that coincide only under an identified
    comparison theorem.

For non-compact CY3s (toric, local models):
    kappa_ch = chi_loc/2 where chi_loc counts compact cycles.
    Example: resolved conifold, kappa_ch = 1.

For K3 x E:
    kappa_BKM = 5 (weight of Borcherds product Delta_5).
    chi_top/24 = 0/24 = 0.  So kappa_BKM != chi_top/24.

For compact rigid CY3s (quintic, etc.):
    CONJECTURAL: a shadow scalar might equal chi_top/24 = -25/3.
    This is a candidate value, not a constructed kappa_ch.
    ALTERNATIVE: the scalar is constrained by full BCOV/DT data, not chi alone.

THE BCOV ALTERNATIVE
====================

The BCOV holomorphic anomaly equation gives the genus-g free energy F_g
of the topological string. At genus 1:

    F_1 = (1/2) log |det G_ij| - (1/2)(3 + h^{1,1} - chi/12) log(Im tau)
                                 + (holomorphic piece)

The coefficient (3 + h^{1,1} - chi/12)/2 = c_1^{BCOV} is the BCOV anomaly
coefficient. For the quintic:

    c_1^{BCOV} = (3 + 1 + 200/12) / 2 = (3 + 1 + 50/3) / 2 = 62/(2*3) = 31/3.

The constant map contribution to F_1 is chi/24 = -25/3 (from the Euler
characteristic of M_{1,1} integrated against c_{top}).

SHADOW TOWER CANDIDATES
========================

If we set the candidate scalar to chi/24 = -25/3, the shadow tower
machinery still works formally (the formulas accept any rational scalar):

    F_g = kappa_candidate * a_hat_g = (-25/3) * a_hat_g

    F_1 = (-25/3) * (1/24) = -25/72
    F_2 = (-25/3) * (7/5760) = -175/17280 = -35/3456

The shadow metric Q_L(t) and discriminant Delta = 8*kappa_candidate*S_4
also work formally with a fractional candidate.

ALTERNATIVE: If the true scalar is NOT chi/24 but some other quantity (perhaps
related to the BCOV anomaly coefficient, or the Borcherds lift weight),
then the shadow tower gives different predictions.

CHI/24 INTEGRALITY SURVEY
=========================

For a CY3 X with h^{1,1} and h^{2,1}:
    chi(X) = 2(h^{1,1} - h^{2,1})

chi/24 is integer iff (h^{1,1} - h^{2,1}) is divisible by 12.

Examples:
    Quintic P4[5]:          h11=1, h21=101, chi=-200, chi/24=-25/3 (NOT int)
    P5[3,3]:                h11=1, h21=73,  chi=-144, chi/24=-6    (integer!)
    P5[2,4]:                h11=1, h21=89,  chi=-176, chi/24=-22/3 (NOT int)
    P7[2,2,2,2]:            h11=1, h21=65,  chi=-128, chi/24=-16/3 (NOT int)
    WP4(1,1,2,2,2)[8]:     h11=1, h21=149, chi=-296, chi/24=-37/3 (NOT int)
    WP4(1,1,1,1,2)[6]:     h11=1, h21=89,  chi=-176, chi/24=-22/3 (NOT int)
    K3 x E:                 h11=21, h21=21, chi=0,    chi/24=0     (integer!)

Observation: chi/24 is integral when 12 | (h^{1,1} - h^{2,1}).

SHADOW DEPTH FOR THE QUINTIC
=============================

With the conjectural candidate kappa_candidate = -25/3, the shadow tower data is:
    alpha: unknown (requires the quintic chiral algebra OPE)
    S_4: unknown (requires quartic contact invariant)

But we CAN analyze the shadow metric assuming the quintic chiral algebra
(if it exists) has the standard form:
    Q_L(t) = 4*kappa_candidate^2 + 12*kappa_candidate*alpha*t
             + (9*alpha^2 + 16*kappa_candidate*S_4)*t^2

With kappa = -25/3: Q_L(0) = 4*(625/9) = 2500/9 > 0.
The shadow metric is well-defined for any nonzero kappa.

If alpha = 0 (no cubic shadow) and S_4 = 0: class G (Gaussian), depth 2.
If alpha != 0 and Delta = 0: class L, depth 3.
If Delta != 0: class M, depth infinity.

Given that the quintic has infinitely many nonzero GV invariants n^0_d,
the EXPECTED class is M (mixed, infinite depth), since the GV generating
function is transcendental and the shadow tower should encode this complexity.

COMPACT CY3 CLOSURE BOUNDARY
============================

None of the scalar diagnostics in this module proves compact CY3
S^3-framing closure.  The following implications are deliberately rejected:

    chi/24, DGMS, BTT, Kaledin K1, or GV/shadow growth
        ==> Obs_Ainf = 0,
        ==> HH^{-2}_{E_1}(A,A) = 0,
        ==> contractible S^3-framing space,
        ==> compact Phi_3 closure.

The raw AP-CY34 witness is retained:

    m_3 B_term^{(2)}[a|a|a|a|b] = 4 alpha [b],
    B_term^{(2)} m_3[a|a|a|a|b] = 2 alpha [b],
    [m_3,B_term^{(2)}][a|a|a|a|b] = 2 alpha [b] != 0
        for alpha != 0.

Therefore B_term^{(2)} is not B_TCFT^{(2)}.  A positive compact CY3
closure claim is conditional on either explicit Costello
B_TCFT^{(2)} correction/comparison data for the chosen chain model or a
precise HH^{-2}_{E_1} filtration theorem.

MATHEMATICAL CONTENT
====================

This module computes:
    1. chi/24 for standard compact CY3s (integrality analysis)
    2. Conjectural scalar candidates for the quintic
    3. Shadow tower with fractional candidate scalar
    4. Shadow metric and discriminant analysis
    5. BCOV anomaly coefficient and comparison
    6. GV invariant growth rates as shadow data
    7. Obstruction analysis: what fails when chi/24 is not integer
    8. Closure diagnostics: what is not implied by chi/24, DGMS, BTT,
       Kaledin, or raw shadow data

Conventions:
    - Cohomological grading (|d| = +1), bar uses desuspension
    - every scalar is lane-specific; K3 x E uses kappa_BKM
    - chi is the topological Euler characteristic
    - A-hat coefficients are POSITIVE (AP22: Bernoulli signs after i-rotation)
    - The BCOV convention differs from DVV by normalization (AP38)

References:
    Bershadsky-Cecotti-Ooguri-Vafa (BCOV), hep-th/9309140
    Gopakumar-Vafa, hep-th/9809187, hep-th/9812127
    Huang-Klemm-Quackenbush (HKQ), hep-th/0612308
    Candelas-de la Ossa-Green-Parkes, NPB 359 (1991) 21
    Faber-Pandharipande, Duke Math. J. 120 (2003) 1-21
    Vol I: higher_genus_modular_koszul.tex (shadow obstruction tower)
    Vol III: bkm_shadow_tower.py (K3 x E comparison)
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Tuple


# =========================================================================
# 1. CY3 Hodge data and chi/24 analysis
# =========================================================================

class CY3HodgeData(NamedTuple):
    """Hodge data and chi/24 analysis for a compact CY3."""
    name: str
    h11: int
    h21: int
    chi: int                    # = 2*(h11 - h21)
    chi_over_24: Fraction       # chi/24
    chi_over_24_integral: bool  # whether chi/24 is an integer
    h11_minus_h21_mod_12: int   # (h11 - h21) mod 12


def cy3_hodge_data(name: str, h11: int, h21: int) -> CY3HodgeData:
    """Compute CY3 Hodge data with chi/24 integrality analysis."""
    chi = 2 * (h11 - h21)
    ratio = Fraction(chi, 24)
    return CY3HodgeData(
        name=name,
        h11=h11,
        h21=h21,
        chi=chi,
        chi_over_24=ratio,
        chi_over_24_integral=(ratio.denominator == 1),
        h11_minus_h21_mod_12=(h11 - h21) % 12,
    )


# Standard compact CY3 examples
STANDARD_CY3S: Dict[str, Tuple[int, int]] = {
    "quintic P4[5]": (1, 101),
    "P5[3,3]": (1, 73),
    "P5[2,4]": (1, 89),
    "P6[2,2,3]": (1, 73),
    "P7[2,2,2,2]": (1, 65),
    "WP4(1,1,2,2,2)[8]": (1, 149),
    "WP4(1,1,1,1,2)[6]": (1, 89),
    "WP4(1,1,2,2,4)[10]": (1, 145),
    "K3 x E": (21, 21),
    # Two-parameter models
    "P1xP1xP1xP1[2,2,2,2]_1": (4, 68),
    # Schoen manifold (fiber product of two rational elliptic surfaces)
    "Schoen": (19, 19),
    # Self-mirror CY3 (h11=h21 => chi=0)
    "self-mirror h11=h21=11": (11, 11),
    # Quotient examples
    "Z5-quotient quintic": (1, 21),
    # Hyperplane CICYs with chi/24 integer
    "CICY chi=-144 (6|diff)": (1, 73),    # h11-h21 = -72, mod 12 = 0
    "CICY chi=-252 (10.5|diff)": (1, 127), # h11-h21 = -126, mod 12 = 6
}


def all_cy3_chi_over_24() -> List[CY3HodgeData]:
    """Compute chi/24 for all standard CY3s."""
    results = []
    for name, (h11, h21) in STANDARD_CY3S.items():
        results.append(cy3_hodge_data(name, h11, h21))
    return results


def chi_over_24_integral_criterion(h11: int, h21: int) -> bool:
    """chi/24 is integral iff 12 | (h11 - h21).

    Proof: chi = 2*(h11 - h21), so chi/24 = (h11 - h21)/12.
    This is an integer iff 12 | (h11 - h21).
    """
    return (h11 - h21) % 12 == 0


# =========================================================================
# 2. BCOV anomaly coefficients
# =========================================================================

class BCOVAnomalyData(NamedTuple):
    """BCOV holomorphic anomaly data for a CY3."""
    name: str
    chi: int
    h11: int
    h21: int
    c1_bcov: Fraction           # BCOV genus-1 anomaly coefficient
    chi_over_24: Fraction       # constant map contribution
    chi_over_12: Fraction       # coefficient in BCOV formula


def bcov_anomaly(name: str, h11: int, h21: int) -> BCOVAnomalyData:
    """Compute BCOV anomaly data.

    The BCOV genus-1 anomaly coefficient:
        c_1^{BCOV} = (3 + h^{1,1} - chi/12) / 2

    The constant map contribution to F_1:
        F_1^{const} = chi/24 * integral_{M_{1,1}} lambda_1
                     = chi/24 * 1/24  (since lambda_1 on M_{1,1} gives 1/24)
    Wait -- F_1^{const} = chi(X) * chi(M_1) / ... actually:

    The genus-g constant map contribution is:
        F_g^{const} = (-1)^g * chi(X) / 2 * integral_{M_g} lambda_g^{g-1} c_{g-1}

    At genus 1: F_1^{const} = -chi(X)/2 * integral_{M_{1,1}} c_0
                             = -chi(X)/2 * 1/24  ... conventions vary.

    We just record the raw BCOV coefficient.
    """
    chi = 2 * (h11 - h21)
    c1 = (Fraction(3) + Fraction(h11) - Fraction(chi, 12)) / Fraction(2)
    return BCOVAnomalyData(
        name=name, chi=chi, h11=h11, h21=h21,
        c1_bcov=c1,
        chi_over_24=Fraction(chi, 24),
        chi_over_12=Fraction(chi, 12),
    )


def bcov_quintic() -> BCOVAnomalyData:
    """BCOV data for the quintic."""
    return bcov_anomaly("quintic", 1, 101)


def bcov_k3_times_e() -> BCOVAnomalyData:
    """BCOV data for K3 x E."""
    return bcov_anomaly("K3 x E", 21, 21)


# =========================================================================
# 3. Kappa candidates for compact CY3s
# =========================================================================

class KappaCandidate(NamedTuple):
    """A candidate scalar for a compact CY3 shadow lane."""
    name: str
    formula_description: str
    value: Fraction
    is_integer: bool
    source: str


def quintic_kappa_candidates() -> List[KappaCandidate]:
    """All candidate scalar values for the quintic CY3.

    Multiple candidates appear because the chiral algebra A_Q is not
    constructed here.  Therefore this function does not compute
    kappa_ch(A_Q); it records exact rational candidates whose status is
    explicit.  K3 x E is different: the value 5 belongs to the BKM
    denominator lane, kappa_BKM(Delta_5).

    IMPORTANT (AP48): kappa_ch depends on the full algebra, not the
    Virasoro subalgebra.  For a general VOA, it must be computed from
    the full bar complex.
    """
    chi = -200
    h11 = 1
    h21 = 101
    c2 = 50  # integral_Q c_2(T_Q) . H = c_2 . hyperplane = 10 * 5 = 50
    c2_int = 50  # same

    candidates = [
        KappaCandidate(
            name="chi/24",
            formula_description="chi(Q)/24 = -200/24 = -25/3",
            value=Fraction(chi, 24),
            is_integer=False,
            source="Conjectural BCOV-shadow candidate; naive BKM integrality fails",
        ),
        KappaCandidate(
            name="chi/2",
            formula_description="chi(Q)/2 = -100 (MacMahon exponent)",
            value=Fraction(chi, 2),
            is_integer=True,
            source="MacMahon: M(q)^{chi/2} prefactor in GV formula",
        ),
        KappaCandidate(
            name="c2/12",
            formula_description="integral c_2/12 = 50/12 = 25/6",
            value=Fraction(c2, 12),
            is_integer=False,
            source="Todd class: td_2(Q) = c_2(Q)/12",
        ),
        KappaCandidate(
            name="c2/24",
            formula_description="integral c_2/24 = 50/24 = 25/12",
            value=Fraction(c2, 24),
            is_integer=False,
            source="Half the Todd invariant",
        ),
        KappaCandidate(
            name="BCOV c1",
            formula_description="c_1^{BCOV} = (3 + 1 + 200/12)/2 = 31/3",
            value=Fraction(31, 3),
            is_integer=False,
            source="BCOV genus-1 anomaly coefficient",
        ),
        KappaCandidate(
            name="h21+1",
            formula_description="h^{2,1} + 1 = 102 (complex structure moduli + 1)",
            value=Fraction(102),
            is_integer=True,
            source="Dimension of deformation space (speculative)",
        ),
        KappaCandidate(
            name="-chi/24 (positive)",
            formula_description="-chi/24 = 25/3 (positive version)",
            value=Fraction(-chi, 24),
            is_integer=False,
            source="Sign-corrected chi/24 (still fractional)",
        ),
    ]
    return candidates


# =========================================================================
# 4. Shadow tower with rational kappa
# =========================================================================

# A-hat genus coefficients (from Vol I, all POSITIVE)
A_HAT_COEFFICIENTS: Dict[int, Fraction] = {
    1: Fraction(1, 24),
    2: Fraction(7, 5760),
    3: Fraction(31, 967680),
    4: Fraction(127, 154828800),
    5: Fraction(73, 3503554560),
}


def shadow_amplitude_scalar(kappa: Fraction, g: int) -> Fraction:
    """Scalar shadow amplitude F_g = kappa * a_hat_g.

    Works for any rational kappa, including fractional values.
    """
    if g < 1 or g > 5:
        raise ValueError(f"genus must be in [1,5], got {g}")
    return kappa * A_HAT_COEFFICIENTS[g]


def shadow_tower_scalar(
    kappa: Fraction, max_genus: int = 5
) -> Dict[int, Fraction]:
    """Scalar shadow tower for rational kappa."""
    tower: Dict[int, Fraction] = {}
    for g in range(1, min(max_genus, 5) + 1):
        tower[g] = shadow_amplitude_scalar(kappa, g)
    return tower


def shadow_metric_data(
    kappa: Fraction,
    alpha: Fraction = Fraction(0),
    S4: Fraction = Fraction(0),
) -> Dict[str, Fraction]:
    """Shadow metric Q_L(t) = q_0 + q_1*t + q_2*t^2 data.

    Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
    where Delta = 8*kappa*S_4 (critical discriminant).

    Works for any rational kappa, alpha, S_4.
    """
    q0 = 4 * kappa**2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha**2 + 16 * kappa * S4
    Delta = 8 * kappa * S4

    return {
        "q0": q0,
        "q1": q1,
        "q2": q2,
        "Delta": Delta,
        "kappa": kappa,
        "alpha": alpha,
        "S4": S4,
    }


def shadow_depth_classification(
    kappa: Fraction,
    alpha: Fraction = Fraction(0),
    S4: Fraction = Fraction(0),
) -> str:
    """Shadow depth class (G/L/C/M) from kappa, alpha, S_4.

    G (Gaussian): alpha=0, S_4=0  => depth 2
    L (Lie):      alpha!=0, Delta=0 => depth 3
    C (Contact):  stratum separation => depth 4
    M (Mixed):    Delta!=0 => depth infinity
    """
    Delta = 8 * kappa * S4

    if alpha == 0 and S4 == 0:
        return "G"
    elif Delta == 0 and alpha != 0:
        return "L"
    elif Delta != 0:
        return "M"
    else:
        # alpha=0 but S4!=0 and Delta=0 => kappa=0 and S4 arbitrary
        # This is a degenerate case: kappa=0 means uncurved
        return "G"  # trivially terminates


def shadow_growth_rate(
    kappa: Fraction,
    alpha: Fraction,
    S4: Fraction,
) -> Optional[float]:
    """Shadow growth rate rho from shadow metric data.

    rho = sqrt(9*alpha^2 + 2*Delta) / (2*|kappa|)
    where Delta = 8*kappa*S_4.

    Returns None if kappa = 0 or depth is finite.
    """
    if kappa == 0:
        return None
    Delta = 8 * kappa * S4
    if Delta == 0 and alpha == 0:
        return None  # finite depth

    numerator_sq = float(9 * alpha**2 + 2 * Delta)
    if numerator_sq < 0:
        # Complex growth rate (oscillatory suppression)
        return None
    denominator = 2 * abs(float(kappa))
    if denominator == 0:
        return None
    return math.sqrt(numerator_sq) / denominator


def shadow_tower_recursive(
    kappa: Fraction,
    alpha: Fraction,
    S4: Fraction,
    max_arity: int = 30,
) -> Dict[int, Fraction]:
    """Compute shadow coefficients S_r for r = 2, ..., max_arity.

    Uses the recursion from sqrt(Q_L(t)):
        H(t) = t^2 * sqrt(Q_L(t)) = sum_{r>=2} r * S_r * t^r
        S_r = a_{r-2} / r

    where a_n = [t^n] sqrt(Q_L(t)) satisfies:
        a_0 = 2*|kappa|  (with sign = sign(kappa))
        a_1 = q_1 / (2*a_0) = 3*alpha
        a_2 = (q_2 - a_1^2) / (2*a_0)
        a_n = -(sum_{j=1}^{n-1} a_j * a_{n-j}) / (2*a_0)  for n >= 3

    Works for any rational kappa != 0.
    """
    if kappa == 0:
        # kappa = 0: all shadow coefficients vanish at the scalar level
        return {r: Fraction(0) for r in range(2, max_arity + 1)}

    q0 = 4 * kappa**2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha**2 + 16 * kappa * S4

    # a_0 = sqrt(q0) = 2*kappa (keeping sign)
    a0 = 2 * kappa
    a = [Fraction(0)] * (max_arity + 1)
    a[0] = a0

    if max_arity >= 1:
        a[1] = q1 / (2 * a0) if a0 != 0 else Fraction(0)

    if max_arity >= 2:
        a[2] = (q2 - a[1]**2) / (2 * a0) if a0 != 0 else Fraction(0)

    for n in range(3, max_arity + 1):
        s = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -s / (2 * a0) if a0 != 0 else Fraction(0)

    # S_r = a_{r-2} / r
    tower: Dict[int, Fraction] = {}
    for r in range(2, max_arity + 1):
        idx = r - 2
        if idx <= max_arity:
            tower[r] = a[idx] / r if r > 0 else Fraction(0)

    return tower


# =========================================================================
# 5. Quintic-specific computations
# =========================================================================

def quintic_shadow_tower_chi24(max_genus: int = 5) -> Dict[int, Fraction]:
    """Shadow tower for quintic with kappa = chi/24 = -25/3."""
    kappa = Fraction(-25, 3)
    return shadow_tower_scalar(kappa, max_genus)


def quintic_shadow_tower_recursive(
    alpha: Fraction = Fraction(0),
    S4: Fraction = Fraction(0),
    max_arity: int = 20,
) -> Dict[int, Fraction]:
    """Recursive shadow tower for quintic with conjectural kappa = -25/3."""
    kappa = Fraction(-25, 3)
    return shadow_tower_recursive(kappa, alpha, S4, max_arity)


def quintic_chi24_scalar_amplitudes() -> Dict[str, Fraction]:
    """Scalar shadow amplitudes F_g for the quintic at kappa = -25/3.

    F_g = (-25/3) * a_hat_g.
    All NEGATIVE (since kappa < 0 and a_hat_g > 0).
    """
    kappa = Fraction(-25, 3)
    result: Dict[str, Fraction] = {}
    for g in range(1, 6):
        key = f"F_{g}"
        result[key] = shadow_amplitude_scalar(kappa, g)
    result["kappa"] = kappa
    return result


# =========================================================================
# 6. GV invariant analysis as shadow data
# =========================================================================

# Known genus-0 GV invariants of the quintic
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


def gv_growth_analysis(max_d: int = 10) -> Dict[str, Any]:
    """Analyze growth of GV invariants as shadow data.

    The GV invariants n^0_d grow like exp(C * sqrt(d)) * d^{-alpha}
    (Huang-Klemm-Quackenbush conjecture, verified numerically).

    If these are root multiplicities of a BKM-type algebra, the growth
    rate constrains the shadow depth class.
    """
    gv = QUINTIC_GV_GENUS0
    available = sorted(d for d in gv if d <= max_d)

    if len(available) < 2:
        return {"error": "insufficient data"}

    # Log growth analysis: log(n_d) vs d
    log_gv = [(d, math.log(float(gv[d]))) for d in available if gv[d] > 0]

    # Consecutive growth ratios
    ratios = []
    for i in range(1, len(log_gv)):
        d1, l1 = log_gv[i - 1]
        d2, l2 = log_gv[i]
        if d2 > d1:
            ratios.append({
                "d": d2,
                "log_ratio": (l2 - l1) / (d2 - d1),
                "ratio": float(gv[d2]) / float(gv[d1]) if gv[d1] != 0 else None,
            })

    # Fit log(n_d) ~ A * d + B (exponential growth)
    # and log(n_d) ~ C * sqrt(d) + D (subexponential = GKP prediction)
    exp_slopes = [(l2 - l1) / (d2 - d1)
                  for (d1, l1), (d2, l2) in zip(log_gv[:-1], log_gv[1:])]
    avg_exp_slope = sum(exp_slopes) / len(exp_slopes) if exp_slopes else 0

    return {
        "n_values": {d: gv[d] for d in available},
        "log_gv": log_gv,
        "growth_ratios": ratios,
        "avg_exponential_slope": avg_exp_slope,
        "growth_type": "exponential" if avg_exp_slope > 1 else "subexponential",
        "implication": (
            "Exponential GV growth is evidence for infinite shadow depth "
            "(class M); it does not construct compact Phi_3 closure"
            if avg_exp_slope > 1 else
            "Subexponential growth is consistent with class M but does not "
            "construct compact Phi_3 closure"
        ),
    }


def gv_to_shadow_s4_estimate() -> Dict[str, Any]:
    """Estimate S_4 for the quintic from GV data.

    The quartic shadow S_4 encodes the leading correction beyond the
    cubic shadow. For an algebra with known OPE, S_4 is computable
    directly. For the quintic, we can only estimate from the structure
    of the GV generating function.

    The genus-0 prepotential F_0(t) = (5/6)*t^3 + sum_d N_{0,d} e^{-dt}
    has the cubic classical piece (intersection number) plus instanton
    corrections. The shadow tower extends this to all genera.

    The "effective S_4" can be estimated from the genus-2 amplitude:
        F_2 = kappa * (7/5760) + delta_pf^{(2,0)}
    where delta_pf is the planted-forest correction.

    For the quintic, F_2 is known from BCOV:
        F_2^{quintic} = known value from BCOV computation.

    We return what's computable without BCOV.
    """
    kappa = Fraction(-25, 3)

    # At genus 1: F_1 = kappa/24 = -25/72
    F1_shadow = kappa / 24

    # The BCOV constant map F_1:
    # F_1^{const} = chi * chi(M_{1,1}) = -200 * (1/24) = -25/3
    # Wait, chi(M_{1,1}) = -1/12, so F_1^{const} = -200 * (-1/12) = 50/3.
    # Convention-dependent (AP38).
    #
    # Using Faber-Pandharipande: integral_{M_1} lambda_1 = 1/24.
    # F_1 = kappa * lambda_1^FP = (-25/3) * (1/24) = -25/72.
    # The instanton part adds sum_d n^0_d * (...) * q^d.

    return {
        "kappa": kappa,
        "F1_scalar_shadow": F1_shadow,
        "note": (
            "S_4 cannot be determined from chi alone; "
            "requires the quintic chiral algebra OPE structure"
        ),
        "estimate_method": "OPEN: requires either explicit OPE or BCOV genus-2 data",
    }


# =========================================================================
# 7. Obstruction analysis
# =========================================================================

class ObstructionAnalysis(NamedTuple):
    """Analysis of the chi/24 obstruction for a CY3."""
    name: str
    chi_over_24: Fraction
    is_integral: bool
    bkm_obstruction: str        # nature of the BKM obstruction
    shadow_status: str           # status of the shadow tower
    kappa_candidate: Fraction
    shadow_class: str


class RawBTermWitness(NamedTuple):
    """Exact AP-CY34 witness for the raw bar pair-contraction."""
    word: Tuple[str, ...]
    alpha: Fraction
    m3_after_b_term_coeff: Fraction
    b_term_after_m3_coeff: Fraction
    commutator_coeff: Fraction
    output_basis: str
    raw_operator: str
    corrected_operator: str
    raw_closure_holds: bool
    blocks_raw_closure: bool
    costello_comparison_required: bool
    statement: str


class CompactCY3ClosureDiagnostics(NamedTuple):
    """Verdict separating scalar/formality diagnostics from compact closure."""
    name: str
    chi_over_24: Fraction
    dgms_derham_formal: bool
    btt_unobstructed_deformations: bool
    kaledin_hdr_degeneration: bool
    raw_witness: RawBTermWitness
    costello_correction_comparison_data: bool
    hh_minus_two_filtration_theorem: bool
    obs_ainf_zero: Optional[bool]
    hh_minus_two_zero: Optional[bool]
    s3_framing_contractible: Optional[bool]
    compact_phi3_closure: Optional[bool]
    positive_claim_allowed: bool
    positive_claim_status: str
    forbidden_implications: List[str]
    remaining_proof_obligations: List[str]


def ap_cy34_raw_b_term_witness(alpha: Fraction = Fraction(1)) -> RawBTermWitness:
    r"""Return the exact raw ``B_term^{(2)}`` commutator witness.

    The word is ``[a|a|a|a|b]``.  With the CY3 toy pairing used in the
    AP-CY34 counterexample, applying the raw pair-contraction first and
    then ``m_3`` gives ``4 alpha [b]``; applying ``m_3`` first and then
    the raw pair-contraction gives ``2 alpha [b]``.  Hence

        [m_3, B_term^{(2)}][a|a|a|a|b] = 2 alpha [b].

    This is a diagnostic for the raw operator only.  It is not a theorem
    about Costello's corrected ``B_TCFT^{(2)}`` operator.
    """
    alpha = Fraction(alpha)
    commutator = 2 * alpha
    return RawBTermWitness(
        word=("a", "a", "a", "a", "b"),
        alpha=alpha,
        m3_after_b_term_coeff=4 * alpha,
        b_term_after_m3_coeff=2 * alpha,
        commutator_coeff=commutator,
        output_basis="[b]",
        raw_operator="B_term^{(2)}",
        corrected_operator="B_TCFT^{(2)}",
        raw_closure_holds=(commutator == 0),
        blocks_raw_closure=(commutator != 0),
        costello_comparison_required=True,
        statement=(
            "[m_3,B_term^{(2)}][a|a|a|a|b] = 2 alpha [b] "
            f"= {commutator} [b] != 0"
            if alpha != 0 else
            "[m_3,B_term^{(2)}][a|a|a|a|b] = 0 for alpha = 0"
        ),
    )


def compact_cy3_positive_claim_allowed(
    *,
    costello_correction_comparison_data: bool = False,
    hh_minus_two_filtration_theorem: bool = False,
) -> bool:
    """Whether a positive compact CY3 obstruction claim has named hypotheses."""
    return bool(
        costello_correction_comparison_data or hh_minus_two_filtration_theorem
    )


def quintic_closure_diagnostics(
    *,
    costello_correction_comparison_data: bool = False,
    hh_minus_two_filtration_theorem: bool = False,
    alpha: Fraction = Fraction(1),
) -> CompactCY3ClosureDiagnostics:
    """Attack-heal verdict for quintic compact CY3 closure implications.

    Positive scalar data for the quintic are kept separate from compact
    ``Phi_3`` closure.  DGMS proves de Rham formality of the compact
    Kahler manifold; BTT proves unobstructed complex-structure
    deformations; Kaledin K1 gives noncommutative Hodge-to-de Rham
    degeneration for smooth proper dg categories.  None of these proves
    the derived ``S^3``-framing obstruction vanishes.
    """
    witness = ap_cy34_raw_b_term_witness(alpha)
    allowed = compact_cy3_positive_claim_allowed(
        costello_correction_comparison_data=costello_correction_comparison_data,
        hh_minus_two_filtration_theorem=hh_minus_two_filtration_theorem,
    )

    if allowed:
        status = (
            "conditional positive obstruction claim allowed: Obs_Ainf "
            "vanishing may be asserted only relative to the supplied "
            "Costello B_TCFT^{(2)} comparison datum or HH^{-2}_{E_1} "
            "filtration theorem; compact Phi_3 closure still requires "
            "analytic/OPE completion data"
        )
        obs_ainf_zero: Optional[bool] = True
    else:
        status = (
            "not established: chi/24, DGMS, BTT, Kaledin K1, and raw shadow "
            "diagnostics do not prove compact CY3 Obs_Ainf=0, HH^{-2}=0, "
            "contractible S^3 framing, or Phi_3 closure"
        )
        obs_ainf_zero = None
    compact_phi3_closure: Optional[bool] = None

    hh_minus_two_zero: Optional[bool] = (
        True if hh_minus_two_filtration_theorem else None
    )
    s3_framing_contractible: Optional[bool] = (
        True if hh_minus_two_filtration_theorem else None
    )

    obligations: List[str] = []
    if not costello_correction_comparison_data:
        obligations.append(
            "Construct Costello B_TCFT^{(2)} correction/comparison data for "
            "the chosen compact quintic chain model."
        )
    if not hh_minus_two_filtration_theorem:
        obligations.append(
            "Or prove a precise HH^{-2}_{E_1} filtration theorem for that "
            "model, including target complex and comparison map."
        )
    obligations.append(
        "Verify analytic/OPE completion needed for compact Phi_3 closure; "
        "scalar shadow arithmetic and obstruction flags alone are not enough."
    )

    return CompactCY3ClosureDiagnostics(
        name="quintic P4[5]",
        chi_over_24=Fraction(-25, 3),
        dgms_derham_formal=True,
        btt_unobstructed_deformations=True,
        kaledin_hdr_degeneration=True,
        raw_witness=witness,
        costello_correction_comparison_data=costello_correction_comparison_data,
        hh_minus_two_filtration_theorem=hh_minus_two_filtration_theorem,
        obs_ainf_zero=obs_ainf_zero,
        hh_minus_two_zero=hh_minus_two_zero,
        s3_framing_contractible=s3_framing_contractible,
        compact_phi3_closure=compact_phi3_closure,
        positive_claim_allowed=allowed,
        positive_claim_status=status,
        forbidden_implications=[
            "chi/24 => kappa_ch(A_Q) or compact Phi_3 closure",
            "DGMS de Rham formality => Obs_Ainf = 0",
            "BTT unobstructed deformations => HH^{-2}_{E_1}(A,A) = 0",
            "Kaledin K1 degeneration => contractible S^3-framing space",
            "raw B_term^{(2)} commutator data => B_TCFT^{(2)} closure",
        ],
        remaining_proof_obligations=obligations,
    )


def quintic_obstruction_analysis() -> ObstructionAnalysis:
    """Full obstruction analysis for the quintic CY3."""
    kappa = Fraction(-25, 3)
    return ObstructionAnalysis(
        name="quintic P4[5]",
        chi_over_24=kappa,
        is_integral=False,
        bkm_obstruction=(
            "chi/24 = -25/3 is NOT integer. This obstructs a naive BKM "
            "denominator identity because the Weyl vector rho must satisfy "
            "(rho, rho) = (integer) for an integral lattice. The quintic "
            "charge lattice is integral, so rho^2 being fractional means "
            "the standard product formula fails."
        ),
        shadow_status=(
            "The shadow tower machinery works with a fractional candidate scalar. "
            "F_g = (-25/3) * a_hat_g is well-defined for all g. "
            "The shadow metric Q_L(t) requires additional data (alpha, S_4) "
            "from the quintic chiral algebra OPE, which is not known explicitly."
        ),
        kappa_candidate=kappa,
        shadow_class="M (conjectural: infinite depth from infinite GV tower)",
    )


def compact_cy3_obstruction_survey() -> List[ObstructionAnalysis]:
    """Survey of chi/24 obstruction for all standard compact CY3s."""
    results = []
    for name, (h11, h21) in STANDARD_CY3S.items():
        chi = 2 * (h11 - h21)
        ratio = Fraction(chi, 24)
        is_int = ratio.denominator == 1

        if is_int:
            bkm_obs = f"chi/24 = {ratio} is integer. No chi/24 obstruction."
            shadow_st = f"Shadow tower formally well-defined with candidate scalar {ratio}."
        else:
            bkm_obs = (
                f"chi/24 = {ratio} is NOT integer. "
                f"Naive BKM structure obstructed."
            )
            shadow_st = (
                f"Shadow tower works formally with fractional candidate scalar {ratio}. "
                f"F_g = ({ratio}) * a_hat_g."
            )

        results.append(ObstructionAnalysis(
            name=name,
            chi_over_24=ratio,
            is_integral=is_int,
            bkm_obstruction=bkm_obs,
            shadow_status=shadow_st,
            kappa_candidate=ratio,
            shadow_class="M" if abs(chi) > 0 else "G",
        ))
    return results


# =========================================================================
# 8. Cross-verification: chi/24 vs other kappa formulas
# =========================================================================

def kappa_formula_comparison() -> Dict[str, Any]:
    """Compare scalar sources across CY families.

    The key point is lane separation.  A chiral modular characteristic,
    a BKM denominator weight, and a compact BCOV chi/24 candidate are not
    interchangeable scalars.

    For K3 x E: chi = 0, kappa_BKM = 5.   chi/24 = 0 != 5.
    For elliptic: chi = 0, kappa_ch = 1.  chi/24 = 0 != 1.
    For K3: chi = 24, kappa_cat = 2.      chi/24 = 1 != 2.

    The formula "the selected scalar equals chi/24" fails for all listed
    cases where the selected scalar is independently determined.
    """
    comparisons = [
        {
            "name": "elliptic curve E",
            "chi": 0,
            "chi/24": Fraction(0),
            "kappa": Fraction(1),
            "kappa_label": "kappa_ch",
            "match": False,
            "kappa_source": "Heisenberg H_1",
        },
        {
            "name": "K3 surface",
            "chi": 24,
            "chi/24": Fraction(1),
            "kappa": Fraction(2),
            "kappa_label": "kappa_cat",
            "match": False,
            "kappa_source": "chi(O_K3) = 2",
        },
        {
            "name": "K3 x E",
            "chi": 0,
            "chi/24": Fraction(0),
            "kappa": Fraction(5),
            "kappa_label": "kappa_BKM",
            "match": False,
            "kappa_source": "Borcherds weight: c_1(0)/2 = 10/2",
        },
        {
            "name": "resolved conifold",
            "chi": 2,
            "chi/24": Fraction(1, 12),
            "kappa": Fraction(1),
            "kappa_label": "kappa_ch",
            "match": False,
            "kappa_source": "Heisenberg from compact P1",
        },
        {
            "name": "quintic",
            "chi": -200,
            "chi/24": Fraction(-25, 3),
            "kappa": Fraction(-25, 3),
            "kappa_label": "kappa_BCOV_shadow_conjectural",
            "match": True,
            "kappa_source": "CONJECTURAL (chi/24)",
        },
    ]

    # Count matches
    n_match = sum(1 for c in comparisons if c["match"])
    n_total = len(comparisons)
    n_known = sum(1 for c in comparisons
                  if c["kappa_source"] != "CONJECTURAL (chi/24)")

    return {
        "comparisons": comparisons,
        "n_match": n_match,
        "n_total": n_total,
        "conclusion": (
            f"chi/24 matches the selected scalar in {n_match}/{n_total} cases. "
            f"In the {n_known} cases where the selected scalar is independently "
            f"known, chi/24 differs from it in every case. "
            f"This forbids using chi/24 as a universal scalar formula."
        ),
    }


# =========================================================================
# 9. The correct interpretation: BCOV + shadow machinery
# =========================================================================

def correct_interpretation() -> Dict[str, str]:
    """The correct mathematical interpretation of the chi/24 quantity.

    chi/24 appears in two distinct roles in topological string theory:

    1. CONSTANT MAP CONTRIBUTION: F_g^{const} is proportional to chi(X).
       This is the contribution to F_g from constant maps X -> X
       (degree 0 in H_2(X, Z)). It is NOT the full shadow amplitude.

    2. BKM WEYL VECTOR: For BKM superalgebras, the Weyl vector norm
       involves chi/24. Non-integrality of chi/24 obstructs the
       standard BKM product formula.

    Neither role identifies chi/24 with kappa_ch(A_X).  The chiral modular
    characteristic is determined by the full chiral algebra, not by the
    topological Euler characteristic alone.

    For compact rigid CY3s where no explicit chiral algebra is known,
    kappa is UNDETERMINED (not chi/24 by default).
    """
    return {
        "chi/24 role 1": (
            "Constant map contribution: F_g^{const} ~ chi(X) * chi(M_g). "
            "This is one TERM in the full genus-g amplitude, not the full thing."
        ),
        "chi/24 role 2": (
            "BKM Weyl vector: (rho, rho) involves chi/24. Non-integrality "
            "obstructs the denominator identity in the standard form."
        ),
        "kappa determination": (
            "kappa_ch(A_X) is the modular characteristic of a constructed "
            "chiral algebra A_X. For K3 x E, the cited value is "
            "kappa_BKM(Delta_5) = 5 from the Borcherds denominator. "
            "For the quintic: kappa_ch is UNDETERMINED (no known chiral "
            "algebra). The assignment chi/24 is a CONJECTURAL shadow scalar, "
            "not a theorem."
        ),
        "shadow tower status": (
            "The shadow obstruction tower machinery works for any rational scalar. "
            "With candidate -25/3: F_g = (-25/3) * a_hat_g. "
            "The sign is data to be interpreted, not a proof of the candidate."
        ),
        "resolution paths": (
            "Path 1: Construct the quintic chiral algebra explicitly and compute kappa_ch. "
            "Path 2: Use BCOV holomorphic anomaly to constrain the scalar. "
            "Path 3: Use the DT/GV correspondence to identify the automorphic form "
            "   whose weight gives a BKM scalar if such a lift exists. "
            "Path 4: Accept a fractional candidate as a feature of rigid CY3s, "
            "   requiring an orbifold/fractional BKM structure."
        ),
        "closure boundary": (
            "None of chi/24, DGMS, BTT, Kaledin K1, or raw shadow diagnostics "
            "proves compact CY3 Obs_Ainf=0, HH^{-2}=0, a contractible "
            "S^3-framing space, or Phi_3 closure.  Positive closure claims "
            "require Costello B_TCFT^{(2)} comparison data or a precise "
            "HH^{-2}_{E_1} filtration theorem."
        ),
    }


# =========================================================================
# 10. Complementarity analysis for CY3
# =========================================================================

def quintic_complementarity() -> Dict[str, Any]:
    """Complementarity analysis: quintic vs its mirror.

    Mirror of quintic: h11=101, h21=1, chi=+200.
    kappa(mirror) = chi(mirror)/24 = +200/24 = +25/3 (conjectural).

    Complementarity sum: kappa + kappa' = -25/3 + 25/3 = 0.
    This is EXACTLY the anti-symmetry expected for Koszul dual pairs
    in the KM/free-field class (AP24: kappa + kappa' = 0 for KM/free).

    For W-algebras: kappa + kappa' = rho * K (nonzero).
    The quintic-mirror pair having kappa + kappa' = 0 would place it
    in the KM/free-field complementarity class.

    CAUTION (AP24): This anti-symmetry is CONJECTURAL and depends on
    the unproved identification kappa = chi/24 for both the quintic
    and its mirror.
    """
    kappa_q = Fraction(-25, 3)   # quintic
    kappa_m = Fraction(25, 3)    # mirror quintic
    comp_sum = kappa_q + kappa_m

    return {
        "quintic_kappa": kappa_q,
        "mirror_kappa": kappa_m,
        "complementarity_sum": comp_sum,
        "sum_vanishes": comp_sum == 0,
        "interpretation": (
            "kappa(Q) + kappa(Q_mirror) = 0. "
            "Consistent with KM/free-field anti-symmetry (AP24). "
            "CONJECTURAL: depends on kappa = chi/24 for both."
        ),
        "mirror_chi": 200,
        "mirror_h11": 101,
        "mirror_h21": 1,
    }


# =========================================================================
# 11. Master summary
# =========================================================================

def quintic_shadow_summary() -> Dict[str, Any]:
    """Complete summary of the quintic shadow obstruction analysis."""
    kappa = Fraction(-25, 3)
    tower = shadow_tower_scalar(kappa, 5)
    candidates = quintic_kappa_candidates()
    obstruction = quintic_obstruction_analysis()
    comparison = kappa_formula_comparison()
    complement = quintic_complementarity()
    bcov = bcov_quintic()
    growth = gv_growth_analysis()
    closure = quintic_closure_diagnostics()

    return {
        "kappa_conjectural": kappa,
        "chi": -200,
        "chi_over_24": kappa,
        "chi_over_24_integral": False,
        "scalar_tower": {g: str(f) for g, f in tower.items()},
        "n_kappa_candidates": len(candidates),
        "candidates": [
            {"name": c.name, "value": str(c.value), "integer": c.is_integer}
            for c in candidates
        ],
        "obstruction": obstruction.bkm_obstruction,
        "shadow_class": "M (conjectural)",
        "bcov_c1": str(bcov.c1_bcov),
        "complementarity_sum": str(complement["complementarity_sum"]),
        "gv_growth_type": growth["growth_type"],
        "key_conclusion": comparison["conclusion"],
        "closure_status": closure.positive_claim_status,
        "raw_B_term_commutator": str(closure.raw_witness.commutator_coeff),
    }
