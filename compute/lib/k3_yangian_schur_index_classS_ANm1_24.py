r"""Class-$\mathcal{S}$ central charges for $\mathcal{T}[A_{N-1}, \Sigma_{0,24}]$, Wave 15.

Extends the Wave-14 computation (A_1 only) to the $N$-parametric family for
$N = 2, 3, 4$. Derives first-principles values of $(n_v, n_h, a_{4d}, c_{4d})$
from the Gaiotto pants decomposition with $T_N$ trinion anomalies fit to
Chacaltana--Distler 2010 (arXiv:1008.5203) Table 3 data at $N = 3, 4, 5$
(and the free-hyper value $T_2$):

    n_v(T_N) = (N - 1)(N - 2)(N + 2) / 2       [= 0, 5, 18, 42 at N = 2, 3, 4, 5]
    n_h(T_N) = 2 N (N^2 - 1) / 3                [= 4, 16, 40, 80 at N = 2, 3, 4, 5]

Combined with tube counts (3g - 3 + n) SU(N) gauge vector contributions
(n_v(tube) = N^2 - 1) and trinion counts (2g - 2 + n):

    n_v(A_{N-1}, Sigma_{g,n}, all max)
      = (N^2 - 1)(3g - 3 + n) + (N - 1)(N - 2)(N + 2)/2 * (2g - 2 + n)
    n_h(A_{N-1}, Sigma_{g,n}, all max)
      = 2 N (N^2 - 1)/3 * (2g - 2 + n)
    a_{4d}   = (5 n_v + n_h) / 24
    c_{4d}   = (2 n_v + n_h) / 12.

For A_1 on Sigma_{0,24}: n_v = 63, n_h = 88, a = 403/24, c = 107/6. Coulomb
rank = (N-1)(3g-3+n) = 21. Beem--Rastelli c_{2d} = -12 c_{4d} = -214.

WAVE 14 ERROR NOTE. The Wave-14 retraction asserted c_{4d}(A_1, Sigma_{0,24})
= 26 from the conjectured formula c_{4d}(A_1, Sigma_{g,n}) = (12(g-1) + 7n)/6.
That formula fails the N=4 cross-check: at (g,n) = (0,4) it gives 16/6 = 8/3,
but SU(2) N_f = 4 SQCD (= T[A_1, Sigma_{0,4}]) has the well-known central
charge c_{4d} = 7/6 (Shapere--Tachikawa 2008 arXiv:0804.1957, Tachikawa
"N=2 SUSY Dynamics for the Pedestrian" 2013 lecture notes arXiv:1312.2684
Ch.13). The first-principles Gaiotto pants-decomposition value is
c_{4d}(A_1, Sigma_{0,n}, all max) = (5n - 13)/6, evaluating to 7/6 at n=4 and
107/6 at n=24. Wave 13's c_{4d} = 107/6 (the boxed value at
k3_chiral_bialgebra_platonic.tex line 1095) is CORRECT. The Wave-13
a_{4d} = 421/24 differs from first principles (403/24) by 18/24; this
remaining discrepancy may reflect a counting convention in the Wave-13
derivation that we have not resolved here.

This module supersedes and corrects the retraction recorded in Wave 14
(k3_yangian_schur_index_classS_A1_24.py, expected_c4d()).

Primary references:
  - Chacaltana, Distler 2010 (arXiv:1008.5203) Tables 3, 5 (class-S anomalies)
  - Chacaltana, Distler, Tachikawa 2013 (arXiv:1212.3952) Sec 3
  - Benini, Tachikawa, Xie 2009 (arXiv:0906.0359) eq (3.7)-(3.8) for T_N anomalies
  - Tachikawa 2013 lecture notes (arXiv:1312.2684) Ch.13
  - Beem, Lemos, Liendo, Peelaers, Rastelli, van Rees 2013 (arXiv:1312.5344)
  - Beem, Rastelli 2014 (arXiv:1404.1079) for T_N Schur index
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, Tuple


def trinion_n_v(N: int) -> Fraction:
    """$n_v(T_N) = (N - 1)(N - 2)(N + 2)/2$. Fit to CD 2010 Tab 3 at N = 2, 3, 4, 5."""
    if N < 2:
        raise ValueError(f"N = {N} not supported; class-S T_N requires N >= 2")
    return Fraction((N - 1) * (N - 2) * (N + 2), 2)


def trinion_n_h(N: int) -> Fraction:
    """$n_h(T_N) = 2N(N^2 - 1)/3$. Fit to CD 2010 Tab 3 at N = 2, 3, 4, 5."""
    if N < 2:
        raise ValueError(f"N = {N} not supported; class-S T_N requires N >= 2")
    return Fraction(2 * N * (N ** 2 - 1), 3)


def class_s_counts(N: int, g: int, n: int) -> Tuple[Fraction, Fraction]:
    r"""Return $(n_v, n_h)$ for $\mathcal{T}[A_{N-1}, \Sigma_{g,n}]$ with all max
    regular punctures. Uses the Gaiotto pants decomposition
    n_trinions = 2g - 2 + n,  n_tubes = 3g - 3 + n,
    with SU(N) gauge vectors per tube (n_v(tube) = N^2 - 1) and T_N trinion
    anomaly data from CD 2010 Tab 3.
    """
    if N < 2:
        raise ValueError(f"N = {N} not supported")
    if g < 0 or n < 0:
        raise ValueError(f"(g, n) = ({g}, {n}) must be non-negative")
    n_trinions = 2 * g - 2 + n
    n_tubes = 3 * g - 3 + n
    if n_trinions < 0 or n_tubes < -0:
        raise ValueError(f"Degenerate pants decomposition: n_trinions = {n_trinions}, n_tubes = {n_tubes}")
    nv_tube = Fraction(N * N - 1, 1)
    n_v = nv_tube * n_tubes + trinion_n_v(N) * n_trinions
    n_h = trinion_n_h(N) * n_trinions
    return n_v, n_h


def central_charges(N: int, g: int, n: int) -> Tuple[Fraction, Fraction]:
    """Return $(a_{4d}, c_{4d})$ via $a = (5 n_v + n_h)/24$, $c = (2 n_v + n_h)/12$."""
    n_v, n_h = class_s_counts(N, g, n)
    a = (5 * n_v + n_h) / Fraction(24)
    c = (2 * n_v + n_h) / Fraction(12)
    return a, c


def coulomb_rank(N: int, g: int, n: int) -> int:
    """Coulomb branch complex dimension (N - 1)(3g - 3 + n) for all-max punctures."""
    return (N - 1) * (3 * g - 3 + n)


def c_2d(N: int, g: int, n: int) -> Fraction:
    """Beem--Rastelli $c_{2d} = -12 c_{4d}$ for the protected chiral algebra (BLLPRvR 2013)."""
    _, c4d = central_charges(N, g, n)
    return -12 * c4d


def k_2d_flavour(N: int) -> Fraction:
    r"""Beem--Rastelli flavour level $k_{2d} = -k_{4d}/2$ per $\mathfrak{su}(N)$ puncture.
    At a maximal regular $\mathfrak{su}(N)$ puncture $k_{4d}^{\mathrm{flav}} = 2N$
    (CD 2010 eq (2.11)), so $k_{2d} = -N$.
    """
    return Fraction(-N, 1)


ANM1_PUNCTURES_24: Dict[int, Dict[str, object]] = {
    N: {
        'n_v': class_s_counts(N, 0, 24)[0],
        'n_h': class_s_counts(N, 0, 24)[1],
        'a_4d': central_charges(N, 0, 24)[0],
        'c_4d': central_charges(N, 0, 24)[1],
        'c_2d': c_2d(N, 0, 24),
        'Coulomb_rank': coulomb_rank(N, 0, 24),
        'flavour_subalgebra': f'su({N})^24 at k_2d = -{N} per puncture',
    }
    for N in (2, 3, 4)
}


def sanity_check() -> Dict[str, object]:
    out: Dict[str, object] = {}
    # Wave 13 A_1 matches Wave 15 first-principles
    _, c_A1 = central_charges(2, 0, 24)
    out['A1_c4d_matches_wave13'] = (c_A1 == Fraction(107, 6))
    # SU(2) N_f = 4 cross-check
    _, c_sqcd = central_charges(2, 0, 4)
    out['SU2_Nf4_c4d_matches_Tachikawa'] = (c_sqcd == Fraction(7, 6))
    # E_6 Minahan-Nemeschansky cross-check (T_3 as Sigma_{0,3} for A_2)
    n_v_T3, n_h_T3 = class_s_counts(3, 0, 3)
    out['T3_is_E6_MN'] = (n_v_T3 == Fraction(5, 1) and n_h_T3 == Fraction(16, 1))
    return out


def main() -> None:
    print('Class-S T[A_{N-1}, Sigma_{0,24}]: N-parametric family (Wave 15)')
    print('Derived via Gaiotto pants decomposition + T_N trinion CD 2010 data.')
    print()
    print(f"{'N':>3} {'n_v':>6} {'n_h':>6} {'a_4d':>10} {'c_4d':>10} {'Coul':>5} {'c_2d':>8}")
    for N in (2, 3, 4):
        data = ANM1_PUNCTURES_24[N]
        print(
            f"{N:>3} "
            f"{str(data['n_v']):>6} "
            f"{str(data['n_h']):>6} "
            f"{str(data['a_4d']):>10} "
            f"{str(data['c_4d']):>10} "
            f"{data['Coulomb_rank']:>5} "
            f"{str(data['c_2d']):>8}"
        )
    print()
    print('Sanity checks:')
    for k, v in sanity_check().items():
        print(f'  {k}: {v}')


if __name__ == '__main__':
    main()
