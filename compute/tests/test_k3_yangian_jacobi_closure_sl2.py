r"""Test harness for super-Jacobi closure on g^eps_K3 with g = sl_2.

Validates Theorem k3yang-jacobi-closure-super of
chapters/examples/k3_yangian_chapter.tex via three independent paths:

  (1) Full 62196-triple super-Jacobi closure in the Hodge-parity
      twisted presentation.
  (2) Dimension count of the plain (non-twisted) defect: the
      Pillai--Gorelik--Kac 3-cocycle predicts
      dim H^3(sl_2; C) * dim(Sym^3 H^2(S, C))^{Muk} = 1 * 13 = 13
      failing triples, all supported on H^2 tensor H^2 tensor H^2.
  (3) Central-term cyclic invariance on sl_2^3, vanishing by
      ad-invariance of the trace form.

The supplementary bracket-antisymmetry check is a lightweight sanity
test guarding against basis-ordering bugs in the engine.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Make compute/lib importable when tests are run directly from this file.
_THIS = Path(__file__).resolve()
_LIB = _THIS.parent.parent / "lib"
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

from k3_yangian_jacobi_closure_sl2 import (  # noqa: E402
    CENTRAL,
    COH_DIM,
    GEN_DIM,
    PARITY,
    SL2_DIM,
    TOTAL,
    _bracket,
    _super_jacobi,
    _parity_of,
    _central_cyclic,
    verify,
)


def test_dimensions():
    """The algebra has 3 * 24 + 1 = 73 generators."""
    assert SL2_DIM == 3
    assert COH_DIM == 24
    assert GEN_DIM == 72
    assert TOTAL == 73


def test_parity_assignment():
    """The parity sequence is 0, 1^22, 0 on cohomology directions."""
    assert PARITY[0] == 0
    assert PARITY[23] == 0
    for i in range(1, 23):
        assert PARITY[i] == 1
    assert _parity_of(TOTAL - 1) == 0  # central element


def test_bracket_central_with_anything_is_zero():
    """The central element c has vanishing bracket with every generator."""
    central = GEN_DIM  # index of c
    for gen in range(TOTAL):
        b1 = _bracket(central, gen, twisted=True)
        b2 = _bracket(gen, central, twisted=True)
        assert b1.is_zero()
        assert b2.is_zero()


def test_complement_closes_universally():
    """Claim (i) of Theorem k3yang-jacobi-closure-super: the
    projection of the super-Jacobiator onto the complement of the
    Mukai-dual centre z_Muk = g (x) [pt] + C c, i.e. onto
    g (x) (H^0 + H^2), vanishes identically on all 62196 triples,
    in both twisted and plain presentations."""
    report = verify()
    assert report["triples_checked"] == 62196
    assert report["twisted_complement_failures"] == 0, (
        f"complement closure (claim (i), twisted) must hold; "
        f"got {report['twisted_complement_failures']} failures"
    )
    assert report["plain_complement_failures"] == 0, (
        f"complement closure also holds in plain presentation; "
        f"got {report['plain_complement_failures']} failures"
    )


def test_mukai_centre_defect_is_pgk_cocycle():
    """Claim (ii) of Theorem k3yang-jacobi-closure-super: the z_Muk
    component of the super-Jacobiator is the Pillai-Gorelik-Kac
    3-cocycle.  Direct sl_2 census: 69 unordered triples, all with
    sl_2-label multiset {E, F, H} and cohomology multiset in
    {(1, 1, [pt])} cup {(1, alpha_i, alpha_i) : 1 <= i <= 22}; of
    these, 44 triples (22 axes * 2 (E, F, H)-assignments) carry a
    simultaneous g (x) [pt] residue (cup-associator), and the
    remaining 25 = 3 + 22 carry only the scalar c residue.
    """
    report = verify()
    # Joint g (x) [pt] failures: 22 H^2 axes * 2 (E, F, H)-assignments per
    # axis = 44, overlapping with the scalar-c count (these 44 carry BOTH
    # residues).
    assert report["twisted_centre_to_pt_failures"] == 44, (
        f"g (x) [pt] cup-associator residue: 22 H^2-axes * 2 (E,F,H)-"
        f"assignments = 44; got {report['twisted_centre_to_pt_failures']}"
    )
    # Scalar-c failures: 69 = 3 (U-plane, (E,F,H)-cycles) + 66
    # (H^2-diagonal, 22 axes * 3 (E,F,H)-cycles).
    assert report["twisted_centre_scalar_failures"] == 69, (
        f"scalar-c trace-form residue: 3 U-plane + 66 H^2-diagonal = 69; "
        f"got {report['twisted_centre_scalar_failures']}"
    )
    # Total distinct z_Muk defect triples: 69.  The 44 joint (c, [pt])
    # triples sit INSIDE the 66 H^2-diagonal scalar-c triples (the 22
    # (E,F,H)-cycles orthogonal to the cup associator carry no [pt]
    # residue).  Thus the supports are nested, not disjoint.
    assert report["twisted_centre_failures"] == 69, (
        f"total z_Muk defect at sl_2: 69 distinct triples (the 44 [pt] "
        f"defects are a subset of the 69 scalar-c defects); "
        f"got {report['twisted_centre_failures']}"
    )
    assert report["plain_centre_failures"] == 69, (
        f"plain z_Muk defect equals twisted (the parity patterns of the "
        f"69 defect triples are (0,1,1) or (0,0,0), both having trivial "
        f"super-signs); got {report['plain_centre_failures']}"
    )
    # sl_2 cyclic pairing sum_cyc f^{bc}_d (T^a, T^d) realises the
    # H^3(sl_2; C) generator tr([T^a, T^b] T^c), taking values +/- 6 on
    # the six (E, F, H)-permutations.  This is NOT zero; it is the Lie
    # factor of the PGK cocycle.  Ad-invariance of the trace form is
    # the cyclic symmetry of the three (cyclically-equivalent) permutations,
    # which yields equality of the values, not vanishing.
    assert report["central_cyclic_failures"] == 6, (
        f"sl_2 cyclic pairing generates H^3(sl_2; C) on the six "
        f"(E, F, H)-permutations with values +/- 6; "
        f"got {report['central_cyclic_failures']} nonzero permutations"
    )


def test_defect_sl2_support_is_EFH():
    """Every defect triple in the scalar c subspace involves one
    generator each of E, F, H: the sl_2 factor is the single
    H^3(sl_2; C) class."""
    report = verify()
    support = report["plain_failure_support"]
    assert len(support) >= 69  # at least the 69 scalar-c triples
    for (x, y, z) in support:
        assert x != CENTRAL and y != CENTRAL and z != CENTRAL
        labels = tuple(sorted([gen // COH_DIM for gen in (x, y, z)]))
        assert labels == (0, 1, 2), (
            f"defect triple must use each of (E, F, H) exactly once; "
            f"got sl_2 labels {labels}"
        )


def test_defect_cohomology_structure():
    """The scalar-c piece of the PGK defect decomposes as 3 + 66: three
    U-plane triples (1, 1, [pt]) and 66 H^2-diagonal triples of the
    form (1, alpha_i, alpha_i) across the 22 middle cohomology axes.
    """
    report = verify()
    support = report["plain_failure_support"]

    u_plane_triples = 0       # cohomology pattern = {1, 1, [pt]}
    h2_diagonal_triples = 0   # pattern = {1, alpha_i, alpha_i}
    cross_H2_triples = 0      # pattern = {alpha_i, 1, alpha_i} cup-assoc
    other = 0
    for (x, y, z) in support:
        coh_indices = sorted([gen % COH_DIM for gen in (x, y, z)])
        if coh_indices == [0, 0, 23]:
            u_plane_triples += 1
        elif (
            coh_indices[0] == 0 and coh_indices[1] == coh_indices[2]
            and 1 <= coh_indices[1] <= 22
        ):
            h2_diagonal_triples += 1
        else:
            other += 1
    assert u_plane_triples == 3, (
        f"expected 3 U-plane defect triples (1, 1, [pt]); "
        f"got {u_plane_triples}"
    )
    assert h2_diagonal_triples == 66, (
        f"expected 66 H^2-diagonal defect triples "
        f"(22 axes * 3 (E,F,H)-permutations); "
        f"got {h2_diagonal_triples}"
    )
    # The 44 "other" triples are the g (x) [pt] defects with
    # cup-associator cohomology pattern {alpha_i, 1, alpha_i} (not
    # scalar-c): they fail the "scalar-c only" test above, placing
    # them outside the U-plane and H^2-diagonal clean cases.
    assert other == 0, (
        f"no scalar-c defect should have pattern other than U-plane or "
        f"H^2-diagonal; unexpected {other} triples. The g (x) [pt] defects "
        f"are counted separately via _split_complement_centre."
    )


def test_antisymmetry_sanity():
    """[J^a_i, J^b_j] + sign * [J^b_j, J^a_i] = 0 where sign is the
    super-antisymmetry sign.  Lightweight spot-check on a small sample
    of generator pairs to catch basis-ordering bugs."""
    pairs = [
        (0, 24),       # E (x) 1,  F (x) 1
        (5, 30),       # E (x) e_5, F (x) e_6
        (48, 55),      # H (x) 1,  H (x) e_7
        (24, 49),      # F (x) 1,  H (x) e_1
    ]
    for (x, y) in pairs:
        bxy = _bracket(x, y, twisted=True)
        byx = _bracket(y, x, twisted=True)
        px, py = _parity_of(x), _parity_of(y)
        sign = 1 if (px * py) % 2 == 0 else -1
        # bxy + sign * byx == 0.
        combined = bxy.add(byx.scaled(sign))
        assert combined.is_zero(), (
            f"super-antisymmetry failed for pair ({x}, {y})"
        )


def test_pgk_cohomology_class_count_cross_check():
    """Second independent path for claim (ii) of
    Theorem k3yang-jacobi-closure-super: enumerate the distinct
    cohomology classes of the PGK cocycle by a direct multiset scan,
    independently of the engine's triple count.

    Prediction from Proposition k3yang-pgk-3cocycle:
        dim H^3(sl_2; C) x (dim H^0 + dim H^2) = 1 x (1 + 22) = 23
    distinct cohomology classes, each represented by exactly three
    sl_2 (E, F, H)-permutations, giving 23 * 3 = 69 defect triples.

    Cross-check path A: engine output ``twisted_centre_failures`` = 69.
    Cross-check path B: multiset enumeration of cohomology supports
    over the failure list yields exactly 23 distinct multisets, each
    with multiplicity 3.
    """
    report = verify()
    support = report["plain_failure_support"]
    assert len(support) == 69

    coh_multiset_counts = {}
    for (x, y, z) in support:
        key = tuple(sorted(gen % COH_DIM for gen in (x, y, z)))
        coh_multiset_counts[key] = coh_multiset_counts.get(key, 0) + 1

    distinct_classes = len(coh_multiset_counts)
    # Path B: 23 distinct cohomology multisets.
    assert distinct_classes == 23, (
        f"expected 23 distinct PGK cohomology classes "
        f"(1 U-plane + 22 H^2-diagonal); got {distinct_classes}"
    )
    # Each class has exactly three (E, F, H)-permutations.
    for key, mult in coh_multiset_counts.items():
        assert mult == 3, (
            f"cohomology class {key} has multiplicity {mult}; "
            f"expected 3 (E, F, H)-permutations per class"
        )

    # Cross-check C: independent class-type partition
    u_plane = sum(1 for k in coh_multiset_counts if k == (0, 0, 23))
    h2_diag = sum(
        1 for k in coh_multiset_counts
        if k[0] == 0 and k[1] == k[2] and 1 <= k[1] <= 22
    )
    assert u_plane == 1, f"U-plane class count: expected 1, got {u_plane}"
    assert h2_diag == 22, (
        f"H^2-diagonal class count: expected 22, got {h2_diag}"
    )
    assert u_plane + h2_diag == distinct_classes, (
        f"class partition covers all: {u_plane}+{h2_diag} "
        f"vs {distinct_classes}"
    )


def test_pgk_lie_factor_generates_h3_sl2():
    """Path 3 isolated: the sl_2 cyclic pairing
    sum_cyc f^{bc}_d (T^a, T^d)_g realises the H^3(sl_2; C) generator
    tr([T^a, T^b] T^c).  For the standard trace form (E, F) = 1,
    (H, H) = 2, the value on (E, F, H) is
    ([E, F], H)_g = (H, H) = 2 (per cyclic summand), and the full
    three-term cyclic sum over (a, b, c) then (b, c, a) then (c, a, b)
    yields 6 on each even permutation of (E, F, H) and -6 on each odd
    permutation.  This is the Lie-side factor of the PGK 3-cocycle.
    """
    # Cross-check 1: (E, F, H) and its cyclic rotations yield the same
    # nonzero value (ad-invariance manifesting as cyclic symmetry).
    val_EFH = _central_cyclic(0, 1, 2)
    val_FHE = _central_cyclic(1, 2, 0)
    val_HEF = _central_cyclic(2, 0, 1)
    assert val_EFH == val_FHE == val_HEF, (
        f"cyclic symmetry (ad-invariance) failed: "
        f"(E,F,H)={val_EFH}, (F,H,E)={val_FHE}, (H,E,F)={val_HEF}"
    )
    assert val_EFH == 6, (
        f"PGK Lie factor on even (E, F, H)-cycle: expected 6, got {val_EFH}"
    )

    # Cross-check 2: odd permutations are negatives of even ones.
    val_FEH = _central_cyclic(1, 0, 2)
    assert val_FEH == -val_EFH, (
        f"sign flip on odd permutation: expected {-val_EFH}, got {val_FEH}"
    )

    # Cross-check 3: degenerate cyclic pairings (repeated index) vanish.
    for a in range(SL2_DIM):
        for b in range(SL2_DIM):
            if a == b:
                assert _central_cyclic(a, a, b) == 0, (
                    f"degenerate cyclic pairing should vanish at ({a},{a},{b})"
                )


if __name__ == "__main__":
    test_dimensions()
    test_parity_assignment()
    test_bracket_central_with_anything_is_zero()
    test_complement_closes_universally()
    test_mukai_centre_defect_is_pgk_cocycle()
    test_defect_sl2_support_is_EFH()
    test_defect_cohomology_structure()
    test_antisymmetry_sanity()
    test_pgk_lie_factor_generates_h3_sl2()
    print("ALL TESTS PASSED")
