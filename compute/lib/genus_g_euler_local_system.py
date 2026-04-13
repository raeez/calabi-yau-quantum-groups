#!/usr/bin/env python3
r"""
genus_g_euler_local_system.py -- Euler characteristic of degree-2 KZB
local systems on punctured surfaces of arbitrary genus and rank.

Ground truth:
  chapters/theory/higher_genus_modular_koszul.tex
  (Proposition prop:genus-g-euler-general, eq:genus-g-euler-general).

The formula:

  chi(Sigma_g \ {0}, L_KZB^{(2)}) = d^2 * (1 - 2g)

where d = dim(V) for sl_d with defining representation V = C^d,
and the local system on Sigma_g \ {0} has rank d^2 (from V tensor V).

Derivation:
  chi_top(Sigma_g \ {s punctures}) = 2 - 2g - s.
  For s = 1: chi_top = 1 - 2g.
  Twisted Euler characteristic = rank * chi_top = d^2 * (1 - 2g).
"""


def chi_top_punctured_surface(g, s=1):
    r"""Topological Euler characteristic of Sigma_g \ {s punctures}.

    Formula: chi_top = 2 - 2g - s.

    Parameters
    ----------
    g : int
        Genus of the surface.
    s : int
        Number of punctures (default 1).

    Returns
    -------
    int
        The topological Euler characteristic.
    """
    return 2 - 2 * g - s


def kzb_local_system_rank(d, degree=2):
    """Rank of the degree-n KZB local system for sl_d with V = C^d.

    At degree 2, the fibre is V tensor V, which has dimension d^2.

    Parameters
    ----------
    d : int
        Dimension of the defining representation.
    degree : int
        Degree of the chiral homology (default 2).

    Returns
    -------
    int
        Rank of the local system = d^degree.
    """
    return d ** degree


def euler_char_kzb_degree2(d, g, s=1):
    """Twisted Euler characteristic of the degree-2 KZB local system.

    chi = d^2 * (2 - 2g - s).

    For the standard case s = 1 (one puncture):
    chi = d^2 * (1 - 2g).

    Parameters
    ----------
    d : int
        Dimension of the defining representation (d for sl_d).
    g : int
        Genus of the surface.
    s : int
        Number of punctures (default 1).

    Returns
    -------
    int
        The twisted Euler characteristic.
    """
    rank = kzb_local_system_rank(d, degree=2)
    chi_top = chi_top_punctured_surface(g, s)
    return rank * chi_top


def euler_table(d_values, g_values, s=1):
    """Compute a table of Euler characteristics.

    Parameters
    ----------
    d_values : list of int
        Dimensions of the defining representation.
    g_values : list of int
        Genera.
    s : int
        Number of punctures (default 1).

    Returns
    -------
    dict
        Mapping (d, g) -> chi.
    """
    result = {}
    for d in d_values:
        for g in g_values:
            result[(d, g)] = euler_char_kzb_degree2(d, g, s)
    return result


def verify_all():
    """Run all internal consistency checks.

    Returns
    -------
    list of str
        Descriptions of checks passed.
    """
    checks = []

    # Check 1: g=0, d=2, s=1 -> chi = 4
    # VERIFIED [DC] direct formula [LC] punctured sphere has chi_top = 1
    val = euler_char_kzb_degree2(2, 0)
    assert val == 4, f"g=0, d=2: expected 4, got {val}"
    checks.append("g=0, d=2: chi=4 (punctured sphere)")

    # Check 2: g=1, d=2, s=1 -> chi = -4
    # VERIFIED [DC] direct formula [LT] higher_genus_modular_koszul.tex:32947
    val = euler_char_kzb_degree2(2, 1)
    assert val == -4, f"g=1, d=2: expected -4, got {val}"
    checks.append("g=1, d=2: chi=-4 (punctured torus)")

    # Check 3: g=2, d=2, s=1 -> chi = -12
    # VERIFIED [DC] direct formula [LT] higher_genus_modular_koszul.tex:32816
    val = euler_char_kzb_degree2(2, 2)
    assert val == -12, f"g=2, d=2: expected -12, got {val}"
    checks.append("g=2, d=2: chi=-12 (genus-2, rank 4)")

    # Check 4: g=2, d=3 -> chi = -27
    # VERIFIED [DC] d^2*(1-2g) = 9*(-3) = -27 [CF] d=2 cross-check
    val = euler_char_kzb_degree2(3, 2)
    assert val == -27, f"g=2, d=3: expected -27, got {val}"
    checks.append("g=2, d=3: chi=-27 (genus-2, rank 9)")

    # Check 5: Linearity in d^2
    # chi(d, g) / d^2 should be independent of d
    for g in [0, 1, 2, 3]:
        ratios = [euler_char_kzb_degree2(d, g) / d**2 for d in [2, 3, 4]]
        assert len(set(ratios)) == 1, (
            f"Linearity in d^2 failed at g={g}: ratios={ratios}"
        )
    checks.append("Linearity in d^2 verified for g=0,1,2,3")

    # Check 6: Sign pattern
    for d in [2, 3, 4]:
        assert euler_char_kzb_degree2(d, 0) > 0, f"g=0, d={d}: should be positive"
        for g in [1, 2, 3]:
            assert euler_char_kzb_degree2(d, g) < 0, (
                f"g={g}, d={d}: should be negative"
            )
    checks.append("Sign pattern: positive at g=0, negative for g>=1")

    return checks


if __name__ == "__main__":
    results = verify_all()
    for r in results:
        print(f"  PASS: {r}")
    print(f"\nAll {len(results)} checks passed.")

    print("\nFull table (d=2,3,4; g=0,1,2,3):")
    table = euler_table([2, 3, 4], [0, 1, 2, 3])
    print(f"  {'d\\g':>4}  {'g=0':>6}  {'g=1':>6}  {'g=2':>6}  {'g=3':>6}")
    for d in [2, 3, 4]:
        row = "  "
        row += f"{d:>4}  "
        for g in [0, 1, 2, 3]:
            row += f"{table[(d, g)]:>6}  "
        print(row)
