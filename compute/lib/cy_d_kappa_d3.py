r"""
cy_d_kappa_d3.py -- CY-D at d=3: the kappa_ch formula and its obstruction.

MATHEMATICAL CONTENT
====================

Theorem CY-D states: kappa_ch(Phi(C)) = chi^CY(C).

At d=2 with h^{1,0}=0: PROVED (modular_koszul_bridge). The Serre duality
argument S_C=[2] kills the one-loop correction, and the Hodge-filtered
supertrace reduces to chi(O_X) = sum_{q=0}^2 (-1)^q h^{0,q}.

At d=3: the situation is fundamentally different.

THE chi(O_X) OBSTRUCTION AT ODD d
===================================

For ANY compact CY_d manifold X with d odd, the CY Serre duality
h^{0,q}(X) = h^{0,d-q}(X) forces:

    chi(O_X) = sum_{q=0}^d (-1)^q h^{0,q}(X) = 0.

Proof: pair the q-th term with the (d-q)-th term. Since d is odd, these
have opposite parity: (-1)^q + (-1)^{d-q} = (-1)^q + (-1)^{d-q} = 0
because d-q and q have opposite parities when d is odd. Each pair cancels;
if d is odd, all terms are paired (no middle term). QED.

Consequence: chi(O_X) = 0 for ALL compact CY manifolds of odd dimension.
This means the identification kappa_ch = chi(O_X) would force kappa_ch = 0
for every CY_3. But kappa_ch(K3 x E) = 3 (proved by additivity). THEREFORE:

    kappa_ch != chi(O_X)  at d = 3.

More precisely: the manuscript's conclusion (C4) in thm:cy-to-chiral-d3
states kappa_ch = chi^CY(C) = chi(O_X). The first equality is the content
of CY-D (conjectural). The second equality chi^CY = chi(O_X) is FALSE
at d=3. It is also false at d=1 (elliptic curve: kappa=1, chi(O)=0) and
at d=2 when h^{1,0} != 0 (abelian surface: kappa=2, chi(O)=0).

THE CORRECT FORMULA
====================

The Hodge-filtered supertrace (eq:kappa-hodge-filtered in cy_to_chiral.tex)
computes the CLASSICAL value of kappa_ch. The quantum correction delta
from the S^d-framing is nonzero when the obstruction group HH_{-1}(C) != 0.

For CY_d manifold X:
  HH_{-1}(X) = sum_{q-p=-1} h^{d-p, q} = sum_q h^{d-q-1, q}  (for p=q+1).

When d=2, h^{1,0}=0: HH_{-1} = 0, so delta=0 and kappa=chi(O_X). PROVED.
When d=2, h^{1,0}!=0: HH_{-1} = h^{1,0} != 0. delta != 0.
When d=3: HH_{-1} = sum_q h^{2-q, q} = h^{2,0} + h^{1,1} + h^{0,2}.
  For quintic: HH_{-1} = 0+1+0 = 1 (nonzero!).
  For K3 x E: HH_{-1} = 1+21+1 = 23 (nonzero!).

The correct CY-D at d=3 should state:
  kappa_ch(Phi_3(C)) = chi^CY(C)
where chi^CY is a CATEGORICAL invariant that in general differs from chi(O_X).
The identification chi^CY = chi(O_X) holds only when the quantum correction
vanishes (h^{1,0}=0 at d=2).

KNOWN kappa_ch VALUES
=====================

Compact:
  point (d=0): kappa_ch = 0. chi(O) = 1. kappa != chi(O).
  E (d=1): kappa_ch = 1. chi(O) = 0. kappa != chi(O).
  K3 (d=2): kappa_ch = 2 = chi(O). PROVED (Serre argument, h^{1,0}=0).
  Abelian surface (d=2): kappa_ch = 2. chi(O) = 0. kappa != chi(O).
  K3 x E (d=3): kappa_ch = 3. chi(O) = 0. kappa != chi(O).
  E^3 (d=3): kappa_ch = 3 (by additivity). chi(O) = 0. kappa != chi(O).
  Quintic (d=3): kappa_ch = OPEN. chi(O) = 0.

Non-compact:
  C^3 (d=3): kappa_ch = 1. (Heisenberg H_1.)
  Resolved conifold (d=3): kappa_ch = 1. (One compact cycle.)

Additivity: kappa_ch(X x Y) = kappa_ch(X) + kappa_ch(Y). (Vol I.)

CONVENTIONS
===========
  - kappa always subscripted: kappa_ch, kappa_BKM, kappa_cat, kappa_fiber (AP113)
  - CY-A_3: PROVED (inf-categorical framework)
  - CY-D at d=2: PROVED for h^{1,0}=0; OPEN for h^{1,0}!=0
  - CY-D at d=3: chi^CY(C) well-defined (CY-A_3 proved); chi^CY != chi(O_X)
  - chi(O_X) = 0 for ALL odd-dimensional CY: PROVED (Serre duality)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

from compute.lib.cy_euler import (
    HodgeDiamond,
    k3_hodge,
    elliptic_curve_hodge,
    product_hodge,
    k3_times_e_hodge,
    quintic_hodge,
)

F = Fraction


# =========================================================================
# 1. The chi(O_X) = 0 theorem for odd-dimensional CY
# =========================================================================

def chi_O(hd: HodgeDiamond) -> Fraction:
    r"""Holomorphic Euler characteristic chi(O_X) = sum (-1)^q h^{0,q}.

    For CY_d with d odd: chi(O_X) = 0 (Serre cancellation).
    For CY_d with d even: chi(O_X) = 2 * sum_{q=0}^{d/2-1} (-1)^q h^{0,q}
                                      + (-1)^{d/2} h^{0,d/2}.

    >>> chi_O(k3_hodge())
    Fraction(2, 1)
    >>> chi_O(elliptic_curve_hodge())
    Fraction(0, 1)
    >>> chi_O(k3_times_e_hodge())
    Fraction(0, 1)
    >>> chi_O(quintic_hodge())
    Fraction(0, 1)
    """
    d = hd.n
    return F(sum((-1)**q * hd.h(0, q) for q in range(d + 1)))


def serre_pairing_check(hd: HodgeDiamond) -> Dict[str, Any]:
    r"""Verify h^{0,q} = h^{0,d-q} for CY manifold (Serre duality on omega=O).

    For a CY_d manifold X with omega_X = O_X, Serre duality gives
    H^q(X, O_X) = H^{d-q}(X, O_X)^*, hence h^{0,q} = h^{0,d-q}.

    >>> r = serre_pairing_check(k3_hodge())
    >>> r['serre_holds']
    True
    """
    d = hd.n
    pairs = []
    all_match = True
    for q in range(d + 1):
        h0q = hd.h(0, q)
        h0dq = hd.h(0, d - q)
        match = (h0q == h0dq)
        if not match:
            all_match = False
        pairs.append((q, d - q, h0q, h0dq, match))

    return {
        'dimension': d,
        'serre_holds': all_match,
        'pairs': pairs,
        'h0_column': [hd.h(0, q) for q in range(d + 1)],
    }


def chi_O_vanishes_odd_d(hd: HodgeDiamond) -> Dict[str, Any]:
    r"""Prove chi(O_X) = 0 for odd-dimensional CY with Serre duality.

    For CY_d with d odd and h^{0,q} = h^{0,d-q}:
    chi(O_X) = sum_{q=0}^d (-1)^q h^{0,q}
    Pair q with d-q: (-1)^q h^{0,q} + (-1)^{d-q} h^{0,d-q}
    = (-1)^q h^{0,q} + (-1)^{d-q} h^{0,q}  (Serre)
    = h^{0,q} * [(-1)^q + (-1)^{d-q}]
    = 0  (since d odd => q and d-q have opposite parities).

    >>> r = chi_O_vanishes_odd_d(elliptic_curve_hodge())
    >>> r['chi_O_is_zero']
    True
    >>> r['d_is_odd']
    True
    >>> r = chi_O_vanishes_odd_d(k3_times_e_hodge())
    >>> r['chi_O_is_zero']
    True
    """
    d = hd.n
    serre = serre_pairing_check(hd)
    chi = chi_O(hd)

    # Demonstrate the cancellation pair by pair
    cancellations = []
    for q in range(d + 1):
        if q > d - q:
            break
        h0q = hd.h(0, q)
        h0dq = hd.h(0, d - q)
        contrib_q = (-1)**q * h0q
        contrib_dq = (-1)**(d - q) * h0dq
        total = contrib_q + contrib_dq
        cancellations.append({
            'q': q,
            'd-q': d - q,
            'h^{0,q}': h0q,
            'h^{0,d-q}': h0dq,
            '(-1)^q * h': contrib_q,
            '(-1)^{d-q} * h': contrib_dq,
            'sum': total,
            'cancels': (total == 0),
        })

    return {
        'dimension': d,
        'd_is_odd': (d % 2 == 1),
        'serre_holds': serre['serre_holds'],
        'chi_O': chi,
        'chi_O_is_zero': (chi == 0),
        'cancellation_pairs': cancellations,
        'all_pairs_cancel': all(c['cancels'] for c in cancellations),
        'proof_applies': (d % 2 == 1) and serre['serre_holds'],
        'theorem': (
            'For CY_d with d odd and Serre h^{0,q}=h^{0,d-q}: '
            'chi(O_X) = 0 by pairwise cancellation.'
        ),
    }


# =========================================================================
# 2. The HH_{-1} obstruction group
# =========================================================================

def hh_minus1_dim(hd: HodgeDiamond) -> Dict[str, Any]:
    r"""Compute dim HH_{-1}(X) for CY_d manifold X.

    HH_n(X) = sum_{q-p=n} h^{d-p, q} (HKR decomposition for CY_d).
    For n=-1: p = q+1, so HH_{-1} = sum_q h^{d-q-1, q}.

    This is the obstruction group for the Serre-kills argument:
    when HH_{-1} = 0, the quantum correction delta=0 and kappa=chi(O_X).
    When HH_{-1} != 0, the quantum correction may be nonzero.

    >>> hh_minus1_dim(k3_hodge())['dim']
    0
    >>> hh_minus1_dim(elliptic_curve_hodge())['dim']
    1
    >>> hh_minus1_dim(k3_times_e_hodge())['dim']
    23
    >>> hh_minus1_dim(quintic_hodge())['dim']
    1
    """
    d = hd.n
    contributions = []
    total = 0
    for q in range(d + 1):
        p = q + 1
        if p > d:
            break
        row = d - p  # = d - q - 1
        if 0 <= row <= d:
            val = hd.h(row, q)
            contributions.append({
                'p': p,
                'q': q,
                'h^{d-p,q}': f'h^{{{row},{q}}}',
                'value': val,
            })
            total += val

    return {
        'dimension': d,
        'dim': total,
        'vanishes': (total == 0),
        'contributions': contributions,
        'serre_argument_applies': (total == 0),
        'interpretation': (
            f'HH_{{-1}} = {total}. '
            + ('Serre argument applies: delta=0, kappa=chi(O_X).'
               if total == 0
               else 'Serre argument FAILS: quantum correction may be nonzero.')
        ),
    }


# =========================================================================
# 3. The kappa_ch != chi(O_X) falsification
# =========================================================================

class KappaFalsification(NamedTuple):
    """Record of a case where kappa_ch != chi(O_X)."""
    name: str
    dimension: int
    kappa_ch: Fraction
    chi_O: Fraction
    discrepancy: Fraction  # kappa_ch - chi(O)
    h10: int               # h^{1,0}
    hh_minus1: int         # dim HH_{-1}
    mechanism: str          # why they differ
    kappa_source: str       # how kappa is determined


def kappa_falsification_table() -> List[KappaFalsification]:
    r"""All known cases where kappa_ch != chi(O_X).

    >>> table = kappa_falsification_table()
    >>> len(table)
    4
    >>> all(f.kappa_ch != f.chi_O for f in table)
    True
    """
    e = elliptic_curve_hodge()
    k3e = k3_times_e_hodge()

    # Abelian surface = E x E
    ab = product_hodge(e, e)

    return [
        KappaFalsification(
            name='point',
            dimension=0,
            kappa_ch=F(0),
            chi_O=F(1),
            discrepancy=F(-1),
            h10=0,
            hh_minus1=0,
            mechanism='d=0: kappa=0 for trivial chiral algebra; chi(O_pt)=1.',
            kappa_source='trivial (no generators)',
        ),
        KappaFalsification(
            name='elliptic curve',
            dimension=1,
            kappa_ch=F(1),
            chi_O=chi_O(e),
            discrepancy=F(1) - chi_O(e),
            h10=e.h(1, 0),
            hh_minus1=hh_minus1_dim(e)['dim'],
            mechanism=(
                'd=1: chi(O_E)=0 (odd d, Serre cancellation). '
                'kappa=1 from Heisenberg H_1. '
                'HH_{-1}=1 (nonzero), so Serre argument fails.'
            ),
            kappa_source='Heisenberg level (Vol I)',
        ),
        KappaFalsification(
            name='abelian surface',
            dimension=2,
            kappa_ch=F(2),
            chi_O=chi_O(ab),
            discrepancy=F(2) - chi_O(ab),
            h10=ab.h(1, 0),
            hh_minus1=hh_minus1_dim(ab)['dim'],
            mechanism=(
                'd=2, h^{1,0}=2: chi(O)=1-2+1=0. '
                'kappa=2 from additivity kappa(E)+kappa(E)=1+1=2. '
                'HH_{-1}=h^{1,0}+h^{0,1}=4 (nonzero), so Serre argument fails.'
            ),
            kappa_source='additivity from kappa(E)=1 (Vol I)',
        ),
        KappaFalsification(
            name='K3 x E',
            dimension=3,
            kappa_ch=F(3),
            chi_O=chi_O(k3e),
            discrepancy=F(3) - chi_O(k3e),
            h10=k3e.h(1, 0),
            hh_minus1=hh_minus1_dim(k3e)['dim'],
            mechanism=(
                'd=3: chi(O)=0 (odd d, Serre cancellation). '
                'kappa=3 from additivity kappa(K3)+kappa(E)=2+1=3. '
                'HH_{-1}=23 (nonzero), so Serre argument fails.'
            ),
            kappa_source='additivity from kappa(K3)=2 and kappa(E)=1',
        ),
    ]


# =========================================================================
# 4. The correct scope of kappa_ch = chi(O_X)
# =========================================================================

class ScopeResult(NamedTuple):
    """Scope where kappa_ch = chi(O_X) is proved."""
    name: str
    dimension: int
    kappa_ch: Fraction
    chi_O: Fraction
    match: bool
    hh_minus1: int
    serre_kills: bool
    status: str


def kappa_equals_chi_O_scope() -> List[ScopeResult]:
    r"""Cases where kappa_ch = chi(O_X) IS and IS NOT proved.

    PROVED: CY_2 with h^{1,0}=0 (K3 and similar).
    FAILS:  d=0 (point), d=1 (E), d=2 with h^{1,0}!=0, d=3 (all).

    >>> scope = kappa_equals_chi_O_scope()
    >>> proved = [s for s in scope if s.match]
    >>> len(proved)
    1
    >>> proved[0].name
    'K3 surface'
    """
    k3 = k3_hodge()
    e = elliptic_curve_hodge()
    ab = product_hodge(e, e)
    k3e = k3_times_e_hodge()
    q5 = quintic_hodge()

    # Point (d=0)
    pt = HodgeDiamond(0, {(0, 0): 1})

    cases = [
        ('point', pt, F(0)),
        ('elliptic curve', e, F(1)),
        ('K3 surface', k3, F(2)),
        ('abelian surface', ab, F(2)),
        ('K3 x E', k3e, F(3)),
    ]

    results = []
    for name, hd, kappa in cases:
        co = chi_O(hd)
        hm1 = hh_minus1_dim(hd)['dim']
        match = (kappa == co)
        serre = (hm1 == 0)

        if match and serre:
            status = 'PROVED (Serre argument)'
        elif match and not serre:
            status = 'COINCIDENCE (Serre fails but values match)'
        elif not match:
            status = 'FALSE (kappa != chi(O_X))'
        else:
            status = 'UNKNOWN'

        results.append(ScopeResult(
            name=name,
            dimension=hd.n,
            kappa_ch=kappa,
            chi_O=co,
            match=match,
            hh_minus1=hm1,
            serre_kills=serre,
            status=status,
        ))

    return results


# =========================================================================
# 5. CY-D at d=3: corrected statement
# =========================================================================

def cy_d_d3_corrected() -> Dict[str, Any]:
    r"""The corrected CY-D statement at d=3.

    WRONG (conclusion C4 as written):
      kappa_ch(A_C) = chi^CY(C) = chi(O_X)

    CORRECT:
      kappa_ch(A_C) = chi^CY(C)
    where chi^CY is the categorical CY Euler characteristic.
    chi^CY(C) != chi(O_X) in general (they agree only when Serre kills).

    The categorical chi^CY is defined as the genus-1 bar obstruction scalar,
    i.e., the modular characteristic of the chiral algebra Phi(C).
    It is an intrinsic invariant of the CY category, computable from the
    S^d-framed cyclic bar complex, NOT from Hodge numbers alone.

    >>> r = cy_d_d3_corrected()
    >>> r['chi_O_k3xe']
    Fraction(0, 1)
    >>> r['kappa_ch_k3xe']
    Fraction(3, 1)
    >>> r['chi_O_equals_kappa']
    False
    """
    k3e = k3_times_e_hodge()
    q5 = quintic_hodge()

    return {
        'old_statement': (
            'kappa_ch(A_C) = chi^CY(C) = chi(O_X), '
            'the holomorphic Euler characteristic.'
        ),
        'new_statement': (
            'kappa_ch(A_C) = chi^CY(C), the categorical CY Euler characteristic. '
            'chi^CY is defined through the genus-1 bar obstruction of Phi(C) and '
            'in general differs from chi(O_X).'
        ),
        'obstruction_to_old': (
            'chi(O_X) = 0 for ALL compact CY_d with d odd (Serre duality forces '
            'h^{0,q} = h^{0,d-q}, and the alternating sum cancels pairwise). '
            'But kappa_ch(K3 x E) = 3 != 0. So kappa_ch != chi(O_X) at d=3.'
        ),
        'chi_O_k3xe': chi_O(k3e),
        'kappa_ch_k3xe': F(3),
        'chi_O_equals_kappa': (chi_O(k3e) == F(3)),
        'chi_O_quintic': chi_O(q5),
        'serre_vanishing': (
            'For CY_d with d odd: chi(O_X) = 0 unconditionally. '
            'Proof: Serre duality h^{0,q} = h^{0,d-q} and d odd => '
            '(-1)^q + (-1)^{d-q} = 0 for every pair.'
        ),
        'scope_of_chi_O_identification': (
            'kappa_ch = chi(O_X) is PROVED only for CY_2 with h^{1,0}=0 '
            '(Proposition prop:cy-kappa-d2). The proof uses HH_{-1}=0 '
            'to show the quantum correction vanishes. When HH_{-1} != 0 '
            '(h^{1,0} != 0 at d=2, or any d >= 3), the identification fails.'
        ),
        'known_kappa_values_d3': {
            'C^3': F(1),
            'K3 x E': F(3),
            'resolved conifold': F(1),
            'quintic': 'OPEN',
        },
        'quintic_status': (
            'kappa_ch(quintic) is OPEN. The existing value -25/3 in some engines '
            'is the BCOV constant-map F_1 coefficient, which equals chi_top/24 '
            'by the BCOV holomorphic anomaly equation. This is NOT kappa_ch in '
            'the Vol I sense (the shadow scalar). The identification of these '
            'two quantities is conjectural and likely WRONG: the BCOV F_1 includes '
            'all weight channels, while kappa_ch/24 is the uniform-weight scalar.'
        ),
    }


# =========================================================================
# 6. Additivity as the primary computation tool at d=3
# =========================================================================

def kappa_ch_from_additivity() -> Dict[str, Any]:
    r"""Compute kappa_ch values at d=3 via additivity.

    The Vol I result: kappa_ch(A tensor B) = kappa_ch(A) + kappa_ch(B).
    For CY products: Phi(D^b(X x Y)) = Phi(D^b(X)) tensor Phi(D^b(Y)).
    So: kappa_ch(X x Y) = kappa_ch(X) + kappa_ch(Y).

    Base values (PROVED):
      kappa_ch(E) = 1   (from Heisenberg H_1, Vol I)
      kappa_ch(K3) = 2  (from Prop prop:cy-kappa-d2, d=2 Serre argument)

    Derived values (by additivity):
      kappa_ch(K3 x E) = 2 + 1 = 3     (PROVED)
      kappa_ch(E^3) = 1 + 1 + 1 = 3    (PROVED)
      kappa_ch(K3 x E x E) = 2+1+1 = 4 (PROVED, d=4 CY)

    NOTE: additivity only applies to PRODUCT CY manifolds.
    For irreducible CY_3 (quintic, etc.), additivity gives no information.
    kappa_ch(quintic) remains OPEN.

    >>> r = kappa_ch_from_additivity()
    >>> r['K3 x E']
    Fraction(3, 1)
    >>> r['E^3']
    Fraction(3, 1)
    """
    base = {
        'E': F(1),
        'K3': F(2),
    }

    derived = {
        'K3 x E': base['K3'] + base['E'],
        'E x E': base['E'] + base['E'],
        'E^3': F(3) * base['E'],
        'K3 x K3': F(2) * base['K3'],
        'K3 x E x E': base['K3'] + F(2) * base['E'],
    }

    # Cross-check with chi(O_X) where available
    checks = {
        'K3': {
            'kappa': base['K3'],
            'chi_O': F(2),
            'match': True,
            'proved': True,
        },
        'E': {
            'kappa': base['E'],
            'chi_O': F(0),
            'match': False,
            'proved': True,  # from Heisenberg, not from chi(O)
        },
        'K3 x E': {
            'kappa': derived['K3 x E'],
            'chi_O': F(0),
            'match': False,
            'proved': True,  # from additivity
        },
    }

    return {
        **derived,
        'base_values': base,
        'cross_checks': checks,
        'method': 'Vol I additivity: kappa(A tensor B) = kappa(A) + kappa(B)',
        'scope': 'Products only. Irreducible CY_3 (quintic) OPEN.',
    }


# =========================================================================
# 7. The quantum correction at d=3
# =========================================================================

def quantum_correction_analysis() -> Dict[str, Any]:
    r"""Analyze the quantum correction delta = kappa_ch - chi(O_X).

    The classical (Hodge-filtered) value is chi(O_X).
    The quantum correction delta arises from the S^d-framing step of Phi.
    delta = 0 when HH_{-1} = 0 (Serre kills the one-loop anomaly).
    delta != 0 when HH_{-1} != 0.

    >>> r = quantum_correction_analysis()
    >>> r['K3']['delta']
    Fraction(0, 1)
    >>> r['K3 x E']['delta']
    Fraction(3, 1)
    >>> r['elliptic curve']['delta']
    Fraction(1, 1)
    """
    e = elliptic_curve_hodge()
    k3 = k3_hodge()
    ab = product_hodge(e, e)
    k3e = k3_times_e_hodge()

    cases = {
        'elliptic curve': (e, F(1)),
        'K3': (k3, F(2)),
        'abelian surface': (ab, F(2)),
        'K3 x E': (k3e, F(3)),
    }

    result = {}
    for name, (hd, kappa) in cases.items():
        co = chi_O(hd)
        delta = kappa - co
        hm1 = hh_minus1_dim(hd)['dim']

        result[name] = {
            'kappa_ch': kappa,
            'chi_O': co,
            'delta': delta,
            'dim_HH_minus1': hm1,
            'delta_equals_hh_minus1': (delta == F(hm1)),
        }

    # Note: delta = dim HH_{-1} does NOT hold in general.
    # E: delta=1, HH_{-1}=1: match.
    # K3: delta=0, HH_{-1}=0: match.
    # ab.surf: delta=2, HH_{-1}=2: match.
    # K3xE: delta=3, HH_{-1}=23: NO MATCH.
    result['delta_equals_dim_HH_minus1_universal'] = False
    result['counterexample'] = 'K3 x E: delta=3 but dim HH_{-1}=23'

    return result


# =========================================================================
# 8. The revised CY-D programme at d=3
# =========================================================================

def cy_d_programme_d3() -> Dict[str, Any]:
    r"""The CY-D programme at d=3 after CY-A_3.

    With CY-A_3 proved, Phi_3 exists and kappa_ch(Phi_3(C)) is well-defined.
    The programme:

    Level 0 (PROVED): kappa_ch is well-defined for all CY_3 categories.
    Level 1 (PROVED, products): kappa_ch(X x Y) = kappa_ch(X) + kappa_ch(Y).
    Level 2 (OPEN): Explicit formula for kappa_ch in terms of Hodge data.
    Level 3 (OPEN): Proof that kappa_ch = chi^CY (the categorical invariant).

    The OBSTRUCTION to Level 2: HH_{-1} != 0 at d=3 generically.
    The quantum correction delta = kappa - chi(O_X) depends on the
    full S^3-framing data, not just on Hodge numbers.

    >>> r = cy_d_programme_d3()
    >>> r['level_0']
    'PROVED'
    >>> r['level_2']
    'OPEN'
    """
    return {
        'level_0': 'PROVED',
        'level_0_content': (
            'kappa_ch(Phi_3(C)) is well-defined for all CY_3 C '
            'satisfying H1-H4 of thm:cy-to-chiral-d3.'
        ),
        'level_1': 'PROVED',
        'level_1_content': (
            'kappa_ch(X x Y) = kappa_ch(X) + kappa_ch(Y) for products. '
            'Gives kappa_ch(K3xE)=3, kappa_ch(E^3)=3, etc.'
        ),
        'level_2': 'OPEN',
        'level_2_content': (
            'Explicit Hodge-number formula for kappa_ch at d=3. '
            'chi(O_X) = 0 for all CY_3 (Serre), so a NEW formula is needed. '
            'The quantum correction from S^3-framing is the key unknown.'
        ),
        'level_3': 'OPEN',
        'level_3_content': (
            'kappa_ch = chi^CY as categorical invariant. '
            'chi^CY is defined through the cyclic bar complex. '
            'The identification with a geometric invariant is open.'
        ),
        'manuscript_correction': (
            'Conclusion (C4) of thm:cy-to-chiral-d3 must remove "= chi(O_X)". '
            'Replace with: kappa_ch(A_C) = chi^CY(C) (categorical invariant, '
            'distinct from chi(O_X) at d >= 3).'
        ),
        'open_problems': [
            'kappa_ch(quintic) = ???',
            'Explicit Hodge formula for chi^CY at d=3',
            'Role of HH_{-1} in the quantum correction',
            'Is chi^CY a deformation invariant (does it vary in families)?',
        ],
    }


# =========================================================================
# 9. Full landscape comparison
# =========================================================================

class KappaLandscapeEntry(NamedTuple):
    """Entry in the kappa_ch landscape at d <= 3."""
    name: str
    dimension: int
    compact: bool
    kappa_ch: Optional[Fraction]
    chi_O: Fraction
    chi_top: int
    kappa_equals_chi_O: Optional[bool]
    hh_minus1: int
    status: str


def kappa_landscape() -> List[KappaLandscapeEntry]:
    r"""Complete landscape of kappa_ch values at d <= 3.

    >>> table = kappa_landscape()
    >>> len(table)
    7
    >>> k3e = [e for e in table if e.name == 'K3 x E'][0]
    >>> k3e.kappa_ch
    Fraction(3, 1)
    >>> k3e.kappa_equals_chi_O
    False
    """
    e = elliptic_curve_hodge()
    k3 = k3_hodge()
    ab = product_hodge(e, e)
    k3e = k3_times_e_hodge()
    q5 = quintic_hodge()
    pt = HodgeDiamond(0, {(0, 0): 1})

    entries = [
        ('point', pt, True, F(0), 'PROVED (trivial)'),
        ('elliptic curve', e, True, F(1), 'PROVED (Heisenberg H_1)'),
        ('K3 surface', k3, True, F(2), 'PROVED (Serre argument, prop:cy-kappa-d2)'),
        ('abelian surface', ab, True, F(2), 'PROVED (additivity from kappa(E)=1)'),
        ('K3 x E', k3e, True, F(3), 'PROVED (additivity kappa(K3)+kappa(E))'),
    ]

    result = []
    for name, hd, compact, kappa, status in entries:
        co = chi_O(hd)
        result.append(KappaLandscapeEntry(
            name=name,
            dimension=hd.n,
            compact=compact,
            kappa_ch=kappa,
            chi_O=co,
            chi_top=hd.euler_characteristic,
            kappa_equals_chi_O=(kappa == co),
            hh_minus1=hh_minus1_dim(hd)['dim'],
            status=status,
        ))

    # Non-compact d=3
    result.append(KappaLandscapeEntry(
        name='C^3',
        dimension=3,
        compact=False,
        kappa_ch=F(1),
        chi_O=F(0),  # non-compact, but formally 0
        chi_top=1,
        kappa_equals_chi_O=False,
        hh_minus1=0,
        status='PROVED (Heisenberg H_1, thm:kappa-c3)',
    ))

    # Quintic: kappa OPEN
    result.append(KappaLandscapeEntry(
        name='quintic',
        dimension=3,
        compact=True,
        kappa_ch=None,
        chi_O=chi_O(q5),
        chi_top=q5.euler_characteristic,
        kappa_equals_chi_O=None,
        hh_minus1=hh_minus1_dim(q5)['dim'],
        status='OPEN (chi(O)=0 by Serre; kappa_ch unknown)',
    ))

    return result
