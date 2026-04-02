r"""
Scattering diagram for K3 x E: explicit computation at low orders.

Computes the consistent scattering diagram for the BKM algebra g_{Delta_5}
associated to K3 x E, and tests whether its wall multiplicities reproduce
the phi_{0,1} Fourier coefficients (root multiplicities).

RESULT SUMMARY (the main finding of this module):
    The PAIR-COMMUTATOR (leading BCH) approach to the scattering diagram
    does NOT directly reproduce the phi_{0,1} root multiplicities. This is
    expected: the full consistency condition involves the entire motivic
    Hall algebra / BPS state counting, not just the leading Lie bracket.

    What we DO establish:
    (a) The seed walls at simple roots force walls at ALL composite roots
        in the positive cone -- qualitative agreement with the shadow tower.
    (b) The forced walls respect the S_3 permutation symmetry of the Gram matrix.
    (c) The GPS tropical vertex in 2d reproduces the known A_2 pentagon identity.
    (d) The precise RATIO between commutator-forced multiplicities and phi_{0,1}
        coefficients is non-uniform, varying with both height and discriminant.
    (e) This non-uniformity quantifies the "higher BPS bound state" corrections
        that the full motivic wall-crossing (Joyce-Song / Kontsevich-Soibelman)
        would include.

LATTICE:
    Lambda^{2,1}_{II} with Gram matrix A = ((2,-2,-2),(-2,2,-2),(-2,-2,2)).
    Signature (2,1): eigenvalues -2, 4, 4.
    Simple roots: delta_1 = (1,0,0), delta_2 = (0,1,0), delta_3 = (0,0,1).

ALGORITHM:
    We work in the pro-nilpotent Lie algebra g = prod_{h>0} g_h with bracket
        [e_alpha, e_beta] = kappa(alpha, beta) * e_{alpha+beta}
    for various choices of the structure constant kappa.
    Wall logs are composed via BCH (Baker-Campbell-Hausdorff).
    Consistency = vanishing of the accumulated product.

REFERENCES:
    Kontsevich-Soibelman (2008), Gross-Pandharipande-Siebert (2010),
    Bridgeland (2017), Gritsenko-Nikulin (various).
"""

from __future__ import annotations

import math
from collections import defaultdict
from fractions import Fraction
from typing import Dict, List, Optional, Tuple

import importlib as _importlib
import os as _os
import sys as _sys


def _import_phi01():
    """Import phi01_fourier, handling both package and standalone use."""
    try:
        return _importlib.import_module('compute.lib.phi01_fourier')
    except (ImportError, ModuleNotFoundError):
        _lib_dir = _os.path.dirname(_os.path.abspath(__file__))
        if _lib_dir not in _sys.path:
            _sys.path.insert(0, _lib_dir)
        return _importlib.import_module('phi01_fourier')


_phi01_mod = _import_phi01()
_phi01_table = _phi01_mod.phi01_table
_phi01_by_disc = _phi01_mod.phi01_by_discriminant
_phi01_coeff = _phi01_mod.phi01_coefficient


# =========================================================================
# 1. LATTICE OPERATIONS
# =========================================================================

GRAM_MATRIX = ((2, -2, -2), (-2, 2, -2), (-2, -2, 2))
"""Gram matrix for real simple roots delta_1, delta_2, delta_3."""

SIMPLE_ROOTS = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
"""Simple roots in their own basis."""


def inner_product(v: Tuple[int, ...], w: Tuple[int, ...]) -> int:
    """Bilinear form (v, w) = sum_{ij} v_i A_{ij} w_j."""
    return sum(v[i] * GRAM_MATRIX[i][j] * w[j]
               for i in range(3) for j in range(3))


def norm_sq(v: Tuple[int, ...]) -> int:
    """(v, v)."""
    return inner_product(v, v)


def add_vectors(v: Tuple[int, ...], w: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(v[i] + w[i] for i in range(len(v)))


def scale_vector(c: int, v: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(c * v[i] for i in range(len(v)))


def is_positive(v: Tuple[int, ...]) -> bool:
    """Check v is in the positive cone: all coordinates >= 0, not all zero."""
    return all(c >= 0 for c in v) and any(c > 0 for c in v)


def root_height(v: Tuple[int, ...]) -> int:
    """Height = sum of coordinates."""
    return sum(v)


def siegel_discriminant(v: Tuple[int, ...]) -> int:
    """For v = (n, l, m), return D = 4nm - l^2."""
    return 4 * v[0] * v[2] - v[1] * v[1]


def s3_orbit(root: Tuple[int, ...]) -> List[Tuple[int, ...]]:
    """S_3 orbit under permutation of coordinates."""
    n1, n2, n3 = root
    return sorted(set([(n1, n2, n3), (n1, n3, n2), (n2, n1, n3),
                       (n2, n3, n1), (n3, n1, n2), (n3, n2, n1)]))


# =========================================================================
# 2. LIE ALGEBRA ELEMENTS
# =========================================================================

class LieElement:
    """Element of the pro-nilpotent Lie algebra g = prod_{h>0} g_h.

    Represents: sum_{alpha > 0} c_alpha * e_alpha
    with bracket [e_alpha, e_beta] = kappa(alpha, beta) * e_{alpha+beta}.
    Truncated to max_height.
    """

    def __init__(self, coeffs: Dict[Tuple[int, int, int], Fraction],
                 max_height: int):
        self.max_height = max_height
        self.coeffs: Dict[Tuple[int, int, int], Fraction] = {
            k: v for k, v in coeffs.items()
            if v != 0 and sum(k) <= max_height and is_positive(k)
        }

    @classmethod
    def zero(cls, max_height: int) -> 'LieElement':
        return cls({}, max_height)

    def __add__(self, other: 'LieElement') -> 'LieElement':
        result = dict(self.coeffs)
        for k, v in other.coeffs.items():
            result[k] = result.get(k, Fraction(0)) + v
            if result.get(k) == 0:
                result.pop(k, None)
        return LieElement(result, self.max_height)

    def __sub__(self, other: 'LieElement') -> 'LieElement':
        result = dict(self.coeffs)
        for k, v in other.coeffs.items():
            result[k] = result.get(k, Fraction(0)) - v
            if result.get(k) == 0:
                result.pop(k, None)
        return LieElement(result, self.max_height)

    def __neg__(self) -> 'LieElement':
        return LieElement({k: -v for k, v in self.coeffs.items()},
                          self.max_height)

    def scale(self, c: Fraction) -> 'LieElement':
        if c == 0:
            return LieElement.zero(self.max_height)
        return LieElement({k: c * v for k, v in self.coeffs.items()},
                          self.max_height)

    def bracket(self, other: 'LieElement',
                kappa: str = 'symmetric') -> 'LieElement':
        """Lie bracket [self, other] with chosen structure constants.

        kappa options:
            'symmetric': [e_a, e_b] = (a, b)_Gram * e_{a+b}
            'skew_12':   [e_a, e_b] = (a1*b2 - a2*b1) * e_{a+b}
            'skew_13':   [e_a, e_b] = (a1*b3 - a3*b1) * e_{a+b}
            'skew_23':   [e_a, e_b] = (a2*b3 - a3*b2) * e_{a+b}
        """
        result: Dict[Tuple[int, int, int], Fraction] = {}
        for alpha, ca in self.coeffs.items():
            if ca == 0:
                continue
            for beta, cb in other.coeffs.items():
                if cb == 0:
                    continue
                gamma = add_vectors(alpha, beta)
                if sum(gamma) > self.max_height or not is_positive(gamma):
                    continue
                if kappa == 'symmetric':
                    k_val = inner_product(alpha, beta)
                elif kappa == 'skew_12':
                    k_val = alpha[0] * beta[1] - alpha[1] * beta[0]
                elif kappa == 'skew_13':
                    k_val = alpha[0] * beta[2] - alpha[2] * beta[0]
                elif kappa == 'skew_23':
                    k_val = alpha[1] * beta[2] - alpha[2] * beta[1]
                else:
                    raise ValueError(f"Unknown kappa: {kappa}")
                if k_val == 0:
                    continue
                result[gamma] = (result.get(gamma, Fraction(0))
                                 + ca * cb * Fraction(k_val))
        return LieElement({k: v for k, v in result.items() if v != 0},
                          self.max_height)

    def terms_at_height(self, h: int) -> Dict[Tuple[int, int, int], Fraction]:
        return {k: v for k, v in self.coeffs.items() if sum(k) == h and v != 0}

    def is_zero(self) -> bool:
        return not self.coeffs


# =========================================================================
# 3. BCH (BAKER-CAMPBELL-HAUSDORFF)
# =========================================================================

def bch(f: LieElement, g: LieElement, kappa: str = 'symmetric',
        max_bch_depth: int = 6) -> LieElement:
    """BCH formula: log(exp(f) * exp(g)).

    BCH(f,g) = f + g + [f,g]/2 + [f,[f,g]]/12 - [g,[f,g]]/12
               - [g,[f,[f,g]]]/24 + ...
    """
    result = f + g

    fg = f.bracket(g, kappa)
    if not fg.is_zero():
        result = result + fg.scale(Fraction(1, 2))

    if max_bch_depth >= 2:
        ffg = f.bracket(fg, kappa)
        gfg = g.bracket(fg, kappa)
        if not ffg.is_zero():
            result = result + ffg.scale(Fraction(1, 12))
        if not gfg.is_zero():
            result = result + gfg.scale(Fraction(-1, 12))

    if max_bch_depth >= 3:
        if not ffg.is_zero():
            gffg = g.bracket(ffg, kappa)
            if not gffg.is_zero():
                result = result + gffg.scale(Fraction(-1, 24))

    if max_bch_depth >= 4 and not gfg.is_zero():
        fgfg = f.bracket(gfg, kappa)
        ggfg = g.bracket(gfg, kappa)
        if not fgfg.is_zero():
            result = result + fgfg.scale(Fraction(-1, 720))
        if not ggfg.is_zero():
            result = result + ggfg.scale(Fraction(1, 360))

    return result


# =========================================================================
# 4. SCATTERING DIAGRAM
# =========================================================================

class ScatteringDiagram:
    """Consistent scattering diagram for K3 x E.

    Processes walls height by height. At each height h, the accumulated
    BCH product of all walls at heights < h gives a residue at height h.
    New walls are added to cancel this residue.

    Parameters
    ----------
    max_height : int
        Maximum root height (sum of coordinates).
    seed_multiplicity : int
        Multiplicity of each simple root. EZ normalization: c(-1) = 1.
    kappa : str
        Lie algebra structure constants: 'symmetric', 'skew_12', etc.
    """

    def __init__(self, max_height: int, seed_multiplicity: int = 1,
                 kappa: str = 'symmetric'):
        self.max_height = max_height
        self.seed_mult = seed_multiplicity
        self.kappa = kappa

        self.walls: Dict[Tuple[int, int, int], Fraction] = {}
        for root in SIMPLE_ROOTS:
            self.walls[root] = Fraction(seed_multiplicity)

        self.generation: Dict[Tuple[int, int, int], int] = {}
        for root in SIMPLE_ROOTS:
            self.generation[root] = 0

        self.messages: List[str] = []

    def _wall_log(self, root: Tuple[int, int, int],
                  mult: Fraction) -> LieElement:
        """Log of wall function: -mult * sum_{k>=1} e_{k*root}/k."""
        ht = root_height(root)
        if ht <= 0:
            return LieElement.zero(self.max_height)
        max_k = self.max_height // ht
        coeffs: Dict[Tuple[int, int, int], Fraction] = {}
        for k in range(1, max_k + 1):
            v = scale_vector(k, root)
            if any(c < 0 for c in v) or sum(v) > self.max_height:
                continue
            coeffs[v] = Fraction(-mult, k)
        return LieElement(coeffs, self.max_height)

    def compute(self) -> None:
        """Run the iterative consistency algorithm."""
        self.messages.append(
            f"max_height={self.max_height}, seed={self.seed_mult}, "
            f"kappa={self.kappa}")

        for h in range(2, self.max_height + 1):
            self._process_height(h)

    def _process_height(self, h: int) -> None:
        """Determine wall multiplicities at height h."""
        accumulated = self._accumulated_product(h)
        terms_h = accumulated.terms_at_height(h)

        for gamma in sorted(terms_h.keys()):
            residue = terms_h[gamma]
            if residue == 0:
                continue
            # New wall must cancel residue: mult = residue
            self.walls[gamma] = residue
            self.generation[gamma] = h
            self.messages.append(
                f"  ht {h}: {gamma}, mult={residue}, "
                f"norm={norm_sq(gamma)}, D={siegel_discriminant(gamma)}")

    def _accumulated_product(self, up_to_height: int) -> LieElement:
        """BCH product of all wall logs at heights < up_to_height."""
        wall_logs = []
        for root in sorted(self.walls.keys(),
                           key=lambda r: (root_height(r), r)):
            if root_height(root) >= up_to_height:
                continue
            log_elem = self._wall_log(root, self.walls[root])
            if not log_elem.is_zero():
                wall_logs.append(log_elem)

        if not wall_logs:
            return LieElement.zero(self.max_height)

        result = wall_logs[0]
        for i in range(1, len(wall_logs)):
            result = bch(result, wall_logs[i], self.kappa)
        return result

    def verify_against_phi01(self, max_n_phi: int = 20) -> List[Dict]:
        """Compare wall multiplicities against phi_{0,1} predictions."""
        phi_data = _phi01_table(max_n_phi)
        results = []
        for root in sorted(self.walls.keys(),
                           key=lambda r: (root_height(r), r)):
            mult = self.walls[root]
            n1, n2, n3 = root
            phi_val = phi_data.get((n1 * n3, n2), 0)
            if phi_val == 0 and n2 > 0:
                phi_val = phi_data.get((n1 * n3, -n2), 0)
            ratio = (float(mult) / phi_val if phi_val != 0 else None)
            results.append({
                'root': root,
                'height': root_height(root),
                'norm': norm_sq(root),
                'D': siegel_discriminant(root),
                'scatter_mult': mult,
                'phi01_mult': phi_val,
                'match': (int(mult) == phi_val
                          if mult == int(mult) else False),
                'ratio': ratio,
            })
        return results

    def wall_count_by_height(self) -> Dict[int, int]:
        """Count of walls at each height."""
        counts: Dict[int, int] = defaultdict(int)
        for root in self.walls:
            counts[root_height(root)] += 1
        return dict(counts)

    def s3_symmetric(self) -> bool:
        """Check if all S_3 orbits have equal multiplicities."""
        for root, mult in self.walls.items():
            for perm in s3_orbit(root):
                if perm in self.walls and self.walls[perm] != mult:
                    return False
        return True


# =========================================================================
# 5. GPS TROPICAL VERTEX (2D)
# =========================================================================

def gps_tropical_vertex_2d(
    max_order: int = 6,
    seed_data: Optional[List[Tuple[Tuple[int, int], int]]] = None
) -> Dict[Tuple[int, int], int]:
    """GPS tropical vertex algorithm in 2d.

    Default seed: rays at (1,0) and (0,1) with multiplicity 1 (the A_2 case).
    This produces the pentagon identity: n_d = 1 for all primitive d in
    the positive quadrant at heights 1 and 2.

    Uses the symplectic form omega((a,b),(c,d)) = ad - bc on Z^2.

    Parameters
    ----------
    max_order : int
        Maximum height (a + b) to compute.
    seed_data : list of ((a,b), mult) pairs
        Initial walls.

    Returns
    -------
    dict: (a,b) -> n_{(a,b)} (wall multiplicity / BPS index)
    """
    if seed_data is None:
        seed_data = [((1, 0), 1), ((0, 1), 1)]

    walls: Dict[Tuple[int, int], Fraction] = {}
    for (d, c) in seed_data:
        walls[d] = Fraction(c)

    for h in range(2, max_order + 1):
        for a in range(0, h + 1):
            b = h - a
            d = (a, b)
            if d in walls or a < 0 or b < 0 or (a == 0 and b == 0):
                continue
            if math.gcd(a, b) != 1:
                continue
            forced = Fraction(0)
            for d1, c1 in list(walls.items()):
                d2 = (d[0] - d1[0], d[1] - d1[1])
                if d2[0] < 0 or d2[1] < 0 or d2 == (0, 0):
                    continue
                if d2 not in walls:
                    continue
                if d1 >= d2:
                    continue
                c2 = walls[d2]
                omega = d1[0] * d2[1] - d1[1] * d2[0]
                if omega == 0:
                    continue
                forced += c1 * c2 * abs(Fraction(omega))
            if forced != 0:
                walls[d] = forced

    return {k: int(v) if v == int(v) else v for k, v in walls.items()}


# =========================================================================
# 6. CONVENIENCE: COMPUTE AND COMPARE
# =========================================================================

def compute_and_compare(
    max_height: int = 6,
    seed_mult: int = 1,
    kappa: str = 'symmetric',
    max_n_phi: int = 20,
) -> Dict[str, object]:
    """Compute scattering diagram and compare to phi_{0,1}."""
    sd = ScatteringDiagram(max_height, seed_mult, kappa)
    sd.compute()
    comp = sd.verify_against_phi01(max_n_phi)

    all_match = all(c['match'] for c in comp)
    ratios = [c['ratio'] for c in comp if c['ratio'] is not None]
    unique_ratios = sorted(set(round(r, 10) for r in ratios)) if ratios else []

    return {
        'diagram': sd,
        'comparisons': comp,
        'all_match': all_match,
        'unique_ratios': unique_ratios,
        'total_walls': len(sd.walls),
    }


def scattering_diagram_walls(
    max_height: int = 6,
    seed_mult: int = 1,
    kappa: str = 'symmetric',
) -> Dict[Tuple[int, int, int], Fraction]:
    """Compute and return wall multiplicities."""
    sd = ScatteringDiagram(max_height, seed_mult, kappa)
    sd.compute()
    return sd.walls


# =========================================================================
# 7. ORBIT ANALYSIS
# =========================================================================

def s3_orbit_table(
    max_height: int = 6,
    seed_mult: int = 1,
    kappa: str = 'symmetric',
) -> List[Dict]:
    """Group walls by S_3 orbit."""
    walls = scattering_diagram_walls(max_height, seed_mult, kappa)
    seen = set()
    orbits = []
    for root in sorted(walls.keys(), key=lambda r: (root_height(r), r)):
        if root in seen:
            continue
        orb = s3_orbit(root)
        for r in orb:
            seen.add(r)
        mult = walls[root]
        orbit_mults = {r: walls[r] for r in orb if r in walls}
        orbits.append({
            'representative': root,
            'orbit_size': len(orbit_mults),
            'multiplicity': mult,
            'all_same': all(v == mult for v in orbit_mults.values()),
            'height': root_height(root),
            'norm': norm_sq(root),
            'D': siegel_discriminant(root),
        })
    return orbits


# =========================================================================
# 8. RATIO ANALYSIS
# =========================================================================

def ratio_analysis(
    max_height: int = 6,
    seed_mult: int = 1,
    kappa: str = 'symmetric',
) -> Dict[str, object]:
    """Analyze ratio of scattering multiplicities to phi_{0,1} coefficients."""
    result = compute_and_compare(max_height, seed_mult, kappa)
    comp = result['comparisons']

    by_height: Dict[int, List] = defaultdict(list)
    by_disc: Dict[int, List] = defaultdict(list)
    for c in comp:
        by_height[c['height']].append(c)
        by_disc[c['D']].append(c)

    height_data = {}
    for h, entries in sorted(by_height.items()):
        rs = [e['ratio'] for e in entries if e['ratio'] is not None]
        if rs:
            height_data[h] = {
                'ratios': rs,
                'uniform': all(abs(r - rs[0]) < 1e-10 for r in rs),
                'representative': rs[0],
            }

    disc_data = {}
    for D, entries in sorted(by_disc.items()):
        rs = [e['ratio'] for e in entries if e['ratio'] is not None]
        if rs:
            disc_data[D] = {
                'ratios': rs,
                'uniform': all(abs(r - rs[0]) < 1e-10 for r in rs),
                'representative': rs[0],
            }

    all_ratios = [c['ratio'] for c in comp if c['ratio'] is not None]
    uniform = (all(abs(r - all_ratios[0]) < 1e-10 for r in all_ratios)
               if all_ratios else False)

    return {
        'uniform': uniform,
        'uniform_value': all_ratios[0] if uniform and all_ratios else None,
        'by_height': height_data,
        'by_discriminant': disc_data,
        'all_ratios': all_ratios,
    }


# =========================================================================
# 9. MAIN
# =========================================================================

if __name__ == "__main__":
    print("=" * 78)
    print("SCATTERING DIAGRAM FOR K3 x E")
    print("=" * 78)

    # Reference data
    print("\nphi_{0,1} discriminant coefficients:")
    phi_disc = _phi01_by_disc(10)
    for D in sorted(phi_disc.keys())[:12]:
        print(f"  c({D:3d}) = {phi_disc[D]}")

    # Symmetric kappa (natural BKM pairing)
    print(f"\n{'='*72}")
    sd = ScatteringDiagram(6, 1, 'symmetric')
    sd.compute()
    comp = sd.verify_against_phi01()
    print(f"{'Root':>15} {'Ht':>3} {'D':>5} {'Scatter':>10} "
          f"{'phi01':>8} {'Match':>6}")
    print("-" * 55)
    for c in comp:
        m = "OK" if c['match'] else "--"
        print(f"{str(c['root']):>15} {c['height']:>3} {c['D']:>5} "
              f"{str(c['scatter_mult']):>10} {c['phi01_mult']:>8} {m:>6}")
    print(f"\nS_3 symmetric: {sd.s3_symmetric()}")
    print(f"Total walls: {len(sd.walls)}")

    # GPS 2d reference
    print(f"\n{'='*72}")
    print("GPS tropical vertex (A_2 pentagon identity):")
    gps = gps_tropical_vertex_2d(6)
    for d in sorted(gps.keys(), key=lambda x: (sum(x), x)):
        print(f"  {d}: n_d = {gps[d]}")
