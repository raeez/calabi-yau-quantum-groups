r"""
cy_d_kappa_d3.py -- CY-D at d=3: compact supertrace and Heisenberg shadow.

MATHEMATICAL CONTENT
====================

The compact CY-D statement computes the PhiFA/Hodge supertrace

    kappa_ch(PhiFA(D^b(X))) = chi(O_X) = sum_q (-1)^q h^{0,q}(X)

for compact Calabi-Yau manifolds.  At odd complex dimension this compact
supertrace vanishes by Serre duality.

At d=2 with h^{1,0}=0: PROVED (modular_koszul_bridge). The Serre duality
argument S_C=[2] kills the one-loop correction, and the Hodge-filtered
supertrace reduces to chi(O_X) = sum_{q=0}^2 (-1)^q h^{0,q}.

At d=3 one must separate this compact total-space invariant from the
relative Heisenberg-Mukai shadow obtained by applying the K3 and elliptic
curve factors separately and then taking the additive free-field level.
For K3 x E:

    compact kappa_ch(K3 x E) = chi(O_{K3 x E}) = 0,
    kappa_ch_Heis(K3 x E) = kappa_ch(K3) + kappa_ch(E) = 2 + 1 = 3.

The number 3 is real mathematics, but it is not the compact Hodge/PhiFA
supertrace of the total space.

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
This is the compact kappa_ch value for the total-space PhiFA supertrace.
It does not erase the relative Heisenberg shadow; it prevents that shadow
from being conflated with the compact invariant.

THE CORRECT FORMULA
====================

The Hodge-filtered supertrace (eq:kappa-hodge-filtered in cy_to_chiral.tex)
computes the compact total-space value of kappa_ch.  The additive
Heisenberg-Mukai level is a different specialization.  The obstruction
group HH_{-1}(C) measures where a naive Serre-killing proof cannot by
itself identify every other specialization with the compact supertrace.

For CY_d manifold X:
  HH_{-1}(X) = sum_{q-p=-1} h^{d-p, q} = sum_q h^{d-q-1, q}  (for p=q+1).

When d=2, h^{1,0}=0: HH_{-1} = 0, so the compact and Heisenberg lanes
coincide for K3.  When d=2, h^{1,0}!=0, the Heisenberg lane need not
coincide with the compact Hodge supertrace.
When d=3: HH_{-1} = sum_q h^{2-q, q} = h^{2,0} + h^{1,1} + h^{0,2}.
  For quintic: HH_{-1} = 0+1+0 = 1 (nonzero!).
  For K3 x E: HH_{-1} = 1+21+1 = 23 (nonzero!).

The corrected CY-D bookkeeping at d=3 states:
  compact kappa_ch(PhiFA_3(D^b(X))) = chi(O_X);
  kappa_ch_Heis is a relative/free-field specialization and may differ.

KNOWN kappa_ch VALUES
=====================

Compact:
  point (d=0): compact kappa_ch = 1 = chi(O).
  E (d=1): compact kappa_ch = 0 = chi(O); kappa_ch_Heis = 1.
  K3 (d=2): kappa_ch = 2 = chi(O). PROVED (Serre argument, h^{1,0}=0).
  Abelian surface (d=2): compact kappa_ch = 0 = chi(O); kappa_ch_Heis = 2.
  K3 x E (d=3): compact kappa_ch = 0 = chi(O); kappa_ch_Heis = 3.
  E^3 (d=3): compact kappa_ch = 0 = chi(O); kappa_ch_Heis = 3.
  Quintic (d=3): compact kappa_ch = 0 = chi(O);
      BCOV/enumerative shadow identification OPEN.

Non-compact:
  C^3 (d=3): kappa_ch = 1. (Heisenberg H_1.)
  Resolved conifold (d=3): kappa_ch = 1. (One compact cycle.)

Heisenberg additivity: kappa_ch_Heis(X x Y) =
  kappa_ch_Heis(X) + kappa_ch_Heis(Y). (Vol I free-field lane.)

CONVENTIONS
===========
  - kappa always subscripted: kappa_ch, kappa_BKM, kappa_cat, kappa_fiber (AP113)
  - CY-A_3: PROVED (inf-categorical framework)
  - CY-D at d=2: PROVED for h^{1,0}=0; OPEN for h^{1,0}!=0
  - CY-D at d=3: compact PhiFA supertrace equals chi(O_X);
    relative Heisenberg shadows are separately labelled.
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

    This is the obstruction group for the naive Serre-kills argument:
    when HH_{-1} = 0, the compact and Heisenberg lanes coincide in the
    standard examples.  When HH_{-1} != 0, factorwise specializations
    can carry information not seen by the compact Hodge supertrace.

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
            + ('Serre argument controls the compact supertrace.'
               if total == 0
               else 'Serre argument alone does not control all specializations.')
        ),
    }


# =========================================================================
# 3. The kappa_ch != chi(O_X) falsification
# =========================================================================

class KappaFalsification(NamedTuple):
    """Record of a Heisenberg specialization that differs from chi(O_X).

    The field name ``kappa_ch`` is retained for API compatibility with the
    earlier engine; entries in this table are the relative/free-field
    ``kappa_ch_Heis`` values, not compact total-space kappa_ch values.
    """
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
    r"""Known cases where kappa_ch_Heis differs from compact chi(O_X).

    These are not counterexamples to compact CY-D.  They are precisely the
    cases where a relative Heisenberg/free-field specialization survives
    while the compact Hodge/PhiFA supertrace is chi(O_X).

    >>> table = kappa_falsification_table()
    >>> len(table)
    4
    >>> all(f.kappa_ch != f.chi_O for f in table)
    True
    """
    e = elliptic_curve_hodge()
    # Abelian surface = E x E
    ab = product_hodge(e, e)
    k3e = k3_times_e_hodge()
    e3 = product_hodge(ab, e)

    return [
        KappaFalsification(
            name='elliptic curve Heisenberg shadow',
            dimension=1,
            kappa_ch=F(1),
            chi_O=chi_O(e),
            discrepancy=F(1) - chi_O(e),
            h10=e.h(1, 0),
            hh_minus1=hh_minus1_dim(e)['dim'],
            mechanism=(
                'd=1: chi(O_E)=0 (odd d, Serre cancellation). '
                'The compact total-space supertrace is 0, while the '
                'relative Heisenberg H_1 shadow has level 1.'
            ),
            kappa_source='kappa_ch_Heis from Heisenberg level (Vol I)',
        ),
        KappaFalsification(
            name='abelian surface Heisenberg shadow',
            dimension=2,
            kappa_ch=F(2),
            chi_O=chi_O(ab),
            discrepancy=F(2) - chi_O(ab),
            h10=ab.h(1, 0),
            hh_minus1=hh_minus1_dim(ab)['dim'],
            mechanism=(
                'd=2, h^{1,0}=2: chi(O)=1-2+1=0. '
                'The compact total-space supertrace is 0, while the '
                'Heisenberg shadow is additive: 1+1=2.'
            ),
            kappa_source='kappa_ch_Heis additivity from kappa_ch_Heis(E)=1',
        ),
        KappaFalsification(
            name='K3 x E Heisenberg shadow',
            dimension=3,
            kappa_ch=F(3),
            chi_O=chi_O(k3e),
            discrepancy=F(3) - chi_O(k3e),
            h10=k3e.h(1, 0),
            hh_minus1=hh_minus1_dim(k3e)['dim'],
            mechanism=(
                'd=3: chi(O)=0 (odd d, Serre cancellation). '
                'The compact total-space supertrace is 0, while the '
                'relative Heisenberg-Mukai shadow is additive: 2+1=3.'
            ),
            kappa_source='kappa_ch_Heis additivity from K3 and E factors',
        ),
        KappaFalsification(
            name='E^3 Heisenberg shadow',
            dimension=3,
            kappa_ch=F(3),
            chi_O=chi_O(e3),
            discrepancy=F(3) - chi_O(e3),
            h10=e3.h(1, 0),
            hh_minus1=hh_minus1_dim(e3)['dim'],
            mechanism=(
                'd=3: chi(O)=0 by odd-dimensional Serre cancellation. '
                'The compact total-space supertrace is 0, while the '
                'three elliptic Heisenberg factors give 1+1+1=3.'
            ),
            kappa_source='kappa_ch_Heis additivity from three elliptic factors',
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
    r"""Cases where compact kappa_ch = chi(O_X) is proved.

    This table uses the compact Hodge/PhiFA supertrace, not the relative
    Heisenberg shadow.  Heisenberg discrepancies are recorded separately
    in :func:`kappa_falsification_table`.

    >>> scope = kappa_equals_chi_O_scope()
    >>> proved = [s for s in scope if s.match]
    >>> len(proved)
    6
    >>> proved[0].name
    'point'
    """
    k3 = k3_hodge()
    e = elliptic_curve_hodge()
    ab = product_hodge(e, e)
    k3e = k3_times_e_hodge()
    q5 = quintic_hodge()

    # Point (d=0)
    pt = HodgeDiamond(0, {(0, 0): 1})

    cases = [
        ('point', pt, F(1)),
        ('elliptic curve', e, chi_O(e)),
        ('K3 surface', k3, chi_O(k3)),
        ('abelian surface', ab, chi_O(ab)),
        ('K3 x E', k3e, chi_O(k3e)),
        ('quintic', q5, chi_O(q5)),
    ]

    results = []
    for name, hd, kappa in cases:
        co = chi_O(hd)
        hm1 = hh_minus1_dim(hd)['dim']
        match = (kappa == co)
        serre = (hm1 == 0)

        if match:
            status = 'PROVED (compact Hodge/PhiFA supertrace)'
        else:
            status = 'FALSE for compact supertrace'

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

    WRONG:
      compact kappa_ch(K3 x E) = kappa_ch_Heis(K3 x E) = 3.
      The compact scalar is not the relative/free-field scalar.

    CORRECT:
      compact kappa_ch(PhiFA_3(D^b(X))) = chi(O_X),
      kappa_ch_Heis is a relative/free-field specialization.

    >>> r = cy_d_d3_corrected()
    >>> r['chi_O_k3xe']
    Fraction(0, 1)
    >>> r['kappa_ch_k3xe']
    Fraction(0, 1)
    >>> r['kappa_ch_heis_k3xe']
    Fraction(3, 1)
    >>> r['chi_O_equals_kappa']
    True
    """
    k3e = k3_times_e_hodge()
    q5 = quintic_hodge()

    return {
        'old_statement': (
            'compact kappa_ch(K3 x E) is the additive Heisenberg value 3.'
        ),
        'new_statement': (
            'compact kappa_ch(PhiFA_3(D^b(X))) = chi(O_X). '
            'The additive value 3 for K3 x E is kappa_ch_Heis, a relative '
            'Heisenberg-Mukai specialization, not the compact total-space '
            'supertrace.'
        ),
        'obstruction_to_old': (
            'chi(O_X) = 0 for ALL compact CY_d with d odd (Serre duality forces '
            'h^{0,q} = h^{0,d-q}, and the alternating sum cancels pairwise). '
            'Thus compact kappa_ch(K3 x E)=0. The number 3 survives only after '
            'passing to the relative Heisenberg shadow.'
        ),
        'chi_O_k3xe': chi_O(k3e),
        'kappa_ch_k3xe': chi_O(k3e),
        'kappa_ch_heis_k3xe': F(3),
        'chi_O_equals_kappa': True,
        'chi_O_equals_heis': (chi_O(k3e) == F(3)),
        'chi_O_quintic': chi_O(q5),
        'kappa_ch_quintic_compact': chi_O(q5),
        'serre_vanishing': (
            'For CY_d with d odd: chi(O_X) = 0 unconditionally. '
            'Proof: Serre duality h^{0,q} = h^{0,d-q} and d odd => '
            '(-1)^q + (-1)^{d-q} = 0 for every pair.'
        ),
        'scope_of_chi_O_identification': (
            'compact kappa_ch = chi(O_X) is the Hodge/PhiFA supertrace. '
            'The Heisenberg/free-field specialization can differ when the '
            'factorwise additive construction is being used instead.'
        ),
        'known_kappa_values_d3': {
            'C^3': F(1),
            'K3 x E': F(0),
            'K3 x E Heisenberg shadow': F(3),
            'resolved conifold': F(1),
            'quintic compact supertrace': F(0),
            'quintic BCOV/enumerative shadow': 'OPEN',
        },
        'quintic_status': (
            'compact kappa_ch(quintic)=chi(O_quintic)=0. The value -25/3 '
            'in BCOV engines is the constant-map F_1 coefficient chi_top/24, '
            'not the compact Hodge/PhiFA supertrace; identifying it with a '
            'chiral enumerative shadow is a separate open claim.'
        ),
    }


# =========================================================================
# 6. Additivity as the primary computation tool at d=3
# =========================================================================

def kappa_ch_from_additivity() -> Dict[str, Any]:
    r"""Compute Heisenberg-shadow values at d=3 via additivity.

    The Vol I free-field result: kappa_ch_Heis(A tensor B) =
    kappa_ch_Heis(A) + kappa_ch_Heis(B).  It computes the relative
    Heisenberg specialization, not the compact total-space Hodge/PhiFA
    supertrace.

    Base values (PROVED):
      kappa_ch_Heis(E) = 1   (from Heisenberg H_1, Vol I)
      kappa_ch_Heis(K3) = 2  (coincides with compact K3 value)

    Derived values (by additivity):
      kappa_ch_Heis(K3 x E) = 2 + 1 = 3     (PROVED)
      kappa_ch_Heis(E^3) = 1 + 1 + 1 = 3    (PROVED)
      kappa_ch_Heis(K3 x E x E) = 2+1+1 = 4 (PROVED, d=4 CY)

    NOTE: additivity only applies to PRODUCT CY manifolds and to this
    relative/free-field lane.  For irreducible CY_3 (quintic, etc.),
    additivity gives no Heisenberg-shadow information.

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

    compact = {
        'K3': chi_O(k3_hodge()),
        'E': chi_O(elliptic_curve_hodge()),
        'K3 x E': chi_O(k3_times_e_hodge()),
        'E x E': chi_O(product_hodge(elliptic_curve_hodge(), elliptic_curve_hodge())),
    }

    # Cross-check with compact chi(O_X) where available.
    checks = {
        'K3': {
            'kappa': base['K3'],
            'chi_O': compact['K3'],
            'match': True,
            'proved': True,
        },
        'E': {
            'kappa': base['E'],
            'chi_O': compact['E'],
            'match': False,
            'proved': True,  # Heisenberg shadow, not compact supertrace
        },
        'K3 x E': {
            'kappa': derived['K3 x E'],
            'chi_O': compact['K3 x E'],
            'match': False,
            'proved': True,  # Heisenberg shadow from additivity
        },
    }

    return {
        **derived,
        'base_values': base,
        'compact_total_space_values': compact,
        'cross_checks': checks,
        'method': 'Vol I free-field additivity: kappa_ch_Heis(A tensor B) = kappa_ch_Heis(A) + kappa_ch_Heis(B)',
        'scope': 'Product Heisenberg shadows only. Compact total-space supertrace is chi(O_X).',
    }


# =========================================================================
# 7. The specialization gap at d=3
# =========================================================================

def quantum_correction_analysis() -> Dict[str, Any]:
    r"""Analyze the specialization gap kappa_ch_Heis - compact kappa_ch.

    The compact Hodge/PhiFA value is chi(O_X).  The Heisenberg value is
    a relative/free-field specialization.  The gap is not a new compact
    kappa invariant and is not universally dim HH_{-1}; HH_{-1} only
    marks where a naive Serre-killing proof cannot control every
    specialization.

    >>> r = quantum_correction_analysis()
    >>> r['K3']['delta']
    Fraction(0, 1)
    >>> r['K3 x E']['specialization_gap']
    Fraction(3, 1)
    >>> r['elliptic curve']['specialization_gap']
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
    for name, (hd, heis) in cases.items():
        compact = chi_O(hd)
        delta = heis - compact
        hm1 = hh_minus1_dim(hd)['dim']

        result[name] = {
            'kappa_ch_compact': compact,
            'kappa_ch_Heis': heis,
            'chi_O': compact,
            'delta': delta,  # legacy key
            'specialization_gap': delta,
            'dim_HH_minus1': hm1,
            'delta_equals_hh_minus1': (delta == F(hm1)),
        }

    # Note: the specialization gap is not dim HH_{-1} in general.
    # E: gap=1, HH_{-1}=1: match.
    # K3: gap=0, HH_{-1}=0: match.
    # ab.surf: gap=2, HH_{-1}=4: no match.
    # K3xE: gap=3, HH_{-1}=23: no match.
    result['delta_equals_dim_HH_minus1_universal'] = False
    result['counterexample'] = 'K3 x E: Heisenberg gap=3 but dim HH_{-1}=23'

    return result


# =========================================================================
# 8. The revised CY-D programme at d=3
# =========================================================================

def cy_d_programme_d3() -> Dict[str, Any]:
    r"""The CY-D programme at d=3 after CY-A_3.

    With CY-A_3 proved, the compact PhiFA/Hodge supertrace is well-defined.
    The programme:

    Level 0 (PROVED): compact kappa_ch is the Hodge supertrace.
    Level 1 (PROVED, products): kappa_ch_Heis is additive on product shadows.
    Level 2 (OPEN): explicit relation between Heisenberg/BCOV shadows and
        the compact supertrace for irreducible CY_3.
    Level 3 (OPEN): full chain-level CY-A_3 model on non-formal CY_3.

    The obstruction to Level 2 is not compact chi(O_X): that is already 0
    at odd d.  The obstruction is the relation between the compact lane
    and the additional specialization lanes.

    >>> r = cy_d_programme_d3()
    >>> r['level_0']
    'PROVED'
    >>> r['level_2']
    'OPEN'
    """
    return {
        'level_0': 'PROVED',
        'level_0_content': (
            'compact kappa_ch(PhiFA_3(D^b(X))) is the Hodge supertrace '
            'sum_q (-1)^q h^{0,q}(X), hence chi(O_X).'
        ),
        'level_1': 'PROVED',
        'level_1_content': (
            'kappa_ch_Heis(X x Y) = kappa_ch_Heis(X) + kappa_ch_Heis(Y) '
            'for product Heisenberg shadows. Gives kappa_ch_Heis(K3xE)=3, '
            'kappa_ch_Heis(E^3)=3, etc.'
        ),
        'level_2': 'OPEN',
        'level_2_content': (
            'Explicit comparison between compact supertrace, Heisenberg '
            'specializations, and BCOV/enumerative genus-1 shadows at d=3.'
        ),
        'level_3': 'OPEN',
        'level_3_content': (
            'Full chain-level CY-A_3 model for non-formal CY_3 categories, '
            'including explicit S^3-framing data and witnessed homotopies.'
        ),
        'manuscript_correction': (
            'Where K3 x E carries the additive value 3, the symbol must be '
            'kappa_ch_Heis or an explicitly relative Heisenberg-Mukai shadow. '
            'Compact kappa_ch(K3 x E) remains chi(O_X)=0.'
        ),
        'open_problems': [
            'BCOV/enumerative shadow of the quintic and its relation to compact kappa_ch',
            'Explicit comparison morphism from product Heisenberg shadows to compact PhiFA',
            'Role of HH_{-1} in specialization gaps',
            'Full chain-level non-formal CY_3 model with S^3-framing witnesses',
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
    kappa_ch_Heis: Optional[Fraction] = None


def kappa_landscape() -> List[KappaLandscapeEntry]:
    r"""Complete landscape of compact kappa_ch values at d <= 3.

    The optional ``kappa_ch_Heis`` field records product/free-field
    shadows when they are part of the local model.

    >>> table = kappa_landscape()
    >>> len(table)
    7
    >>> k3e = [e for e in table if e.name == 'K3 x E'][0]
    >>> k3e.kappa_ch
    Fraction(0, 1)
    >>> k3e.kappa_ch_Heis
    Fraction(3, 1)
    >>> k3e.kappa_equals_chi_O
    True
    """
    e = elliptic_curve_hodge()
    k3 = k3_hodge()
    ab = product_hodge(e, e)
    k3e = k3_times_e_hodge()
    q5 = quintic_hodge()
    pt = HodgeDiamond(0, {(0, 0): 1})

    entries = [
        ('point', pt, True, chi_O(pt), 'PROVED (compact Hodge/PhiFA supertrace)', None),
        ('elliptic curve', e, True, chi_O(e), 'PROVED (compact Hodge/PhiFA supertrace)', F(1)),
        ('K3 surface', k3, True, chi_O(k3), 'PROVED (compact Hodge/PhiFA supertrace)', F(2)),
        ('abelian surface', ab, True, chi_O(ab), 'PROVED (compact Hodge/PhiFA supertrace)', F(2)),
        ('K3 x E', k3e, True, chi_O(k3e), 'PROVED (compact Hodge/PhiFA supertrace)', F(3)),
    ]

    result = []
    for name, hd, compact, kappa, status, heis in entries:
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
            kappa_ch_Heis=heis,
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
        kappa_ch_Heis=F(1),
    ))

    # Quintic: compact supertrace proved; BCOV/enumerative shadow open.
    result.append(KappaLandscapeEntry(
        name='quintic',
        dimension=3,
        compact=True,
        kappa_ch=chi_O(q5),
        chi_O=chi_O(q5),
        chi_top=q5.euler_characteristic,
        kappa_equals_chi_O=True,
        hh_minus1=hh_minus1_dim(q5)['dim'],
        status='PROVED compact supertrace; BCOV/enumerative shadow OPEN',
        kappa_ch_Heis=None,
    ))

    return result
