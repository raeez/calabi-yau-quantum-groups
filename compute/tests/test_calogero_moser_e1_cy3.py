r"""Tests for the Calogero-Moser integrable system from E_1 algebra of Hilb^n(CY3).

Manuscript references:
    sec:cm-from-yangian (quantum_groups_e2_braided.tex):
        CM Hamiltonians as central elements of Y^+(gl_hat_1)
    thm:sv-c3 (toric_cy3_coha.tex):
        CoHA(C^3) = Y^+(gl_hat_1), with plane partitions as basis
    sec:cm-integrability (quantum_groups_e2_braided.tex):
        Integrability = commutativity of H_k

Literature:
    Etingof-Ginzburg (arXiv:math/0011114): Symplectic reflection algebras, CM space
    Nakajima (1997): Hilbert scheme, Heisenberg algebra
    Schiffmann-Vasserot (arXiv:1211.1287): CoHA = Y^+(gl_hat_1)
    Heckman-Polychronakos (1992): CM from W-algebras
    Awata-Matsuo-Odake-Shiraishi (arXiv:hep-th/9503028): Collective field theory
    Prochazka-Rapcak (arXiv:1910.07997): W_{1+infinity} = affine Yangian

Ground truth values (exact arithmetic with h1=1, h2=2, h3=-3):

    n=1: one plane partition [[1]].
         Boxes: (0,0,0). Content: 0.
         E_k = 0 for all k.

    n=2: three plane partitions:
         [[2]]: boxes (0,0,0), (0,0,1) -> contents 0, -3 -> E_1=-3, E_2=9, E_3=-27
         [[1,1]]: boxes (0,0,0), (0,1,0) -> contents 0, 2 -> E_1=2, E_2=4, E_3=8
         [[1],[1]]: boxes (0,0,0), (1,0,0) -> contents 0, 1 -> E_1=1, E_2=1, E_3=1

    n=3: six plane partitions:
         [[3]]: boxes {0,-3,-6} -> E_1=-9, E_2=45, E_3=-243
         [[2,1]]: boxes {0,-3,2} -> E_1=-1, E_2=13, E_3=-19
         [[1,1,1]]: boxes {0,2,4} -> E_1=6, E_2=20, E_3=72
         [[2],[1]]: boxes {0,-3,1} -> E_1=-2, E_2=10, E_3=-26
         [[1,1],[1]]: boxes {0,2,1} -> E_1=3, E_2=5, E_3=9
         [[1],[1],[1]]: boxes {0,1,2} -> E_1=3, E_2=5, E_3=9
         Note: last two are DEGENERATE in (E_1,E_2,E_3)!

    Plane partition counts (OEIS A000219):
        pp(0)=1, pp(1)=1, pp(2)=3, pp(3)=6, pp(4)=13, pp(5)=24

CAUTION (AP-CY1): CY dimension d != complex dimension n.
CAUTION (AP1): kappa formulas are family-specific.
CAUTION (AP35): Verify proof steps independently of the conclusion.
"""

import pytest
from fractions import Fraction
from sympy import Rational, expand, simplify

from compute.lib.calogero_moser_e1_cy3 import (
    bps_eigenstate_table,
    box_content,
    chern_number_eigenvalues,
    cm_comprehensive_computation,
    cm_eigenvalue,
    cm_eigenvalues_all,
    cm_hamiltonian_from_yangian,
    cm_hamiltonian_matrix,
    conifold_cm_eigenvalue,
    conifold_cm_full_spectrum,
    conifold_interaction_energy,
    cubic_hamiltonian_eigenvalues,
    enumerate_plane_partitions,
    first_casimirs,
    jack_eigenvalue_2d,
    plane_partition_boxes,
    plane_partition_volume,
    verify_2d_reduction,
    verify_cm_commutativity,
    verify_cm_eigenvalue_three_paths,
    verify_integrability_multipath,
    w_algebra_cm_eigenvalue,
    w_algebra_virasoro_eigenvalue,
    yangian_casimir_eigenvalue,
)


# ================================================================
# PLANE PARTITION COMBINATORICS
# ================================================================

class TestPlanePartitionCombinatorics:
    """Test plane partition enumeration and basic box computations."""

    def test_pp_count_0(self):
        """pp(0) = 1 (the empty partition)."""
        pps = enumerate_plane_partitions(0)
        assert len(pps) == 1

    def test_pp_count_1(self):
        """pp(1) = 1."""
        pps = enumerate_plane_partitions(1)
        assert len(pps) == 1

    def test_pp_count_2(self):
        """pp(2) = 3."""
        pps = enumerate_plane_partitions(2)
        assert len(pps) == 3

    def test_pp_count_3(self):
        """pp(3) = 6."""
        pps = enumerate_plane_partitions(3)
        assert len(pps) == 6

    def test_pp_count_4(self):
        """pp(4) = 13."""
        pps = enumerate_plane_partitions(4)
        assert len(pps) == 13

    def test_pp_count_5(self):
        """pp(5) = 24."""
        pps = enumerate_plane_partitions(5)
        assert len(pps) == 24

    def test_volume_consistency(self):
        """Volume of each plane partition of n equals n."""
        for n in range(6):
            pps = enumerate_plane_partitions(n)
            for pp in pps:
                assert plane_partition_volume(pp) == n, (
                    f"Volume mismatch for {pp}: got {plane_partition_volume(pp)}, expected {n}"
                )

    def test_box_enumeration_n2(self):
        """Box coordinates for n=2 plane partitions."""
        pps = enumerate_plane_partitions(2)
        for pp in pps:
            boxes = plane_partition_boxes(pp)
            assert len(boxes) == 2, f"Expected 2 boxes, got {len(boxes)} for {pp}"

    def test_box_content_origin(self):
        """content(0,0,0) = 0 for any h parameters."""
        for h1, h2 in [(Rational(1), Rational(2)),
                        (Rational(3), Rational(-1)),
                        (Rational(1, 2), Rational(1, 3))]:
            assert box_content(0, 0, 0, h1, h2) == 0


# ================================================================
# CM EIGENVALUES
# ================================================================

class TestCMEigenvalues:
    """Test CM Hamiltonian eigenvalue computations."""

    def test_E_k_trivial_n0(self):
        """E_k = 0 for the empty partition (n=0)."""
        pp = []
        for k in range(1, 6):
            assert cm_eigenvalue(pp, k, Rational(1), Rational(2)) == 0

    def test_E_k_n1_is_zero(self):
        """E_k(single box at origin) = 0 for all k.

        The only plane partition of 1 is [[1]], with one box at (0,0,0).
        content(0,0,0) = 0, so E_k = 0^k = 0 for k >= 1.
        """
        pp = [[1]]
        h1, h2 = Rational(1), Rational(2)
        for k in range(1, 6):
            ev = cm_eigenvalue(pp, k, h1, h2)
            assert ev == 0, f"E_{k} for [[1]] should be 0, got {ev}"

    def test_E_1_n2_column(self):
        """E_1 for [[2]] (column partition of 2).

        Boxes: (0,0,0) with content 0, (0,0,1) with content h3.
        E_1 = 0 + h3 = h3 = -(h1+h2).

        At h1=1, h2=2: h3=-3, E_1=-3.
        """
        pp = [[2]]
        h1, h2 = Rational(1), Rational(2)
        h3 = -(h1 + h2)
        ev = cm_eigenvalue(pp, 1, h1, h2)
        assert ev == h3, f"E_1 for [[2]] should be {h3}, got {ev}"
        assert ev == Rational(-3)

    def test_E_1_n2_row(self):
        """E_1 for [[1,1]] (row partition of 2).

        Boxes: (0,0,0) with content 0, (0,1,0) with content h2.
        E_1 = 0 + h2 = h2.

        At h1=1, h2=2: E_1=2.
        """
        pp = [[1, 1]]
        h1, h2 = Rational(1), Rational(2)
        ev = cm_eigenvalue(pp, 1, h1, h2)
        assert ev == h2, f"E_1 for [[1,1]] should be {h2}, got {ev}"
        assert ev == Rational(2)

    def test_E_1_n2_diagonal(self):
        """E_1 for [[1],[1]] (two rows, one box each).

        Boxes: (0,0,0) with content 0, (1,0,0) with content h1.
        E_1 = 0 + h1 = h1.

        At h1=1, h2=2: E_1=1.
        """
        pp = [[1], [1]]
        h1, h2 = Rational(1), Rational(2)
        ev = cm_eigenvalue(pp, 1, h1, h2)
        assert ev == h1, f"E_1 for [[1],[1]] should be {h1}, got {ev}"
        assert ev == Rational(1)

    def test_E_2_n2_all(self):
        """E_2 for all plane partitions of 2.

        At h1=1, h2=2, h3=-3:
          [[2]]:   E_2 = 0^2 + (-3)^2 = 9
          [[1,1]]: E_2 = 0^2 + 2^2 = 4
          [[1],[1]]: E_2 = 0^2 + 1^2 = 1
        """
        h1, h2 = Rational(1), Rational(2)
        assert cm_eigenvalue([[2]], 2, h1, h2) == Rational(9)
        assert cm_eigenvalue([[1, 1]], 2, h1, h2) == Rational(4)
        assert cm_eigenvalue([[1], [1]], 2, h1, h2) == Rational(1)

    def test_E_3_n2_all(self):
        """E_3 for all plane partitions of 2.

        At h1=1, h2=2, h3=-3:
          [[2]]:   E_3 = 0 + (-3)^3 = -27
          [[1,1]]: E_3 = 0 + 2^3 = 8
          [[1],[1]]: E_3 = 0 + 1^3 = 1
        """
        h1, h2 = Rational(1), Rational(2)
        assert cm_eigenvalue([[2]], 3, h1, h2) == Rational(-27)
        assert cm_eigenvalue([[1, 1]], 3, h1, h2) == Rational(8)
        assert cm_eigenvalue([[1], [1]], 3, h1, h2) == Rational(1)

    def test_E_1_n3_column(self):
        """E_1 for [[3]] (column of height 3).

        Boxes: (0,0,0), (0,0,1), (0,0,2). Contents: 0, h3, 2*h3.
        E_1 = 0 + h3 + 2*h3 = 3*h3.

        At h1=1, h2=2, h3=-3: E_1 = -9.
        """
        pp = [[3]]
        h1, h2 = Rational(1), Rational(2)
        h3 = -(h1 + h2)
        ev = cm_eigenvalue(pp, 1, h1, h2)
        assert ev == 3 * h3, f"E_1 for [[3]] should be {3*h3}, got {ev}"

    def test_E_1_n3_row(self):
        """E_1 for [[1,1,1]] (row of length 3).

        Boxes: (0,0,0), (0,1,0), (0,2,0). Contents: 0, h2, 2*h2.
        E_1 = 3*h2.

        At h1=1, h2=2, h3=-3: E_1 = 6.
        """
        pp = [[1, 1, 1]]
        h1, h2 = Rational(1), Rational(2)
        ev = cm_eigenvalue(pp, 1, h1, h2)
        assert ev == 3 * h2

    def test_eigenvalues_all_keys(self):
        """cm_eigenvalues_all returns correct keys."""
        pp = [[2, 1]]
        evs = cm_eigenvalues_all(pp, 5, Rational(1), Rational(2))
        for k in range(1, 6):
            assert k in evs

    def test_E_k_column_formula(self):
        """Column partition [[n]]: E_k = h3^k * sum_{l=0}^{n-1} l^k.

        This is a direct consequence of all boxes being at (0,0,l).
        """
        h1, h2 = Rational(1), Rational(2)
        h3 = -(h1 + h2)
        for n in range(1, 6):
            pp = [[n]]
            for k in range(1, 4):
                expected = h3 ** k * sum(Rational(l) ** k for l in range(n))
                actual = cm_eigenvalue(pp, k, h1, h2)
                assert actual == expected, (
                    f"Column formula failed: n={n}, k={k}, "
                    f"expected {expected}, got {actual}"
                )


# ================================================================
# CM INTEGRABILITY (COMMUTATIVITY)
# ================================================================

class TestCMIntegrability:
    """Test that all CM Hamiltonians commute."""

    def test_commutativity_n1(self):
        """All H_k commute at n=1 (trivial: 1x1 matrices)."""
        result = verify_cm_commutativity(1, 5, Rational(1), Rational(2))
        assert result["all_commutators_zero"]

    def test_commutativity_n2(self):
        """All H_k commute at n=2 (3x3 diagonal matrices)."""
        result = verify_cm_commutativity(2, 5, Rational(1), Rational(2))
        assert result["all_commutators_zero"]

    def test_commutativity_n3(self):
        """All H_k commute at n=3 (6x6 diagonal matrices)."""
        result = verify_cm_commutativity(3, 5, Rational(1), Rational(2))
        assert result["all_commutators_zero"]

    def test_commutativity_n4(self):
        """All H_k commute at n=4 (13x13 diagonal matrices)."""
        result = verify_cm_commutativity(4, 5, Rational(1), Rational(2))
        assert result["all_commutators_zero"]

    def test_spectrum_generic_n2(self):
        """Spectrum is generic (all tuples distinct) at n=2."""
        result = verify_cm_commutativity(2, 5, Rational(1), Rational(2))
        assert result["spectrum_generic"], (
            f"Expected generic spectrum at n=2, got "
            f"{result['num_distinct_tuples']}/{result['dimension']} distinct"
        )

    def test_dimension_matches_pp_count(self):
        """Number of states matches plane partition count."""
        expected = {0: 1, 1: 1, 2: 3, 3: 6, 4: 13, 5: 24}
        for n, pp_n in expected.items():
            if n == 0:
                continue
            result = verify_cm_commutativity(n, 3, Rational(1), Rational(2))
            assert result["dimension"] == pp_n, (
                f"Dimension at n={n}: expected {pp_n}, got {result['dimension']}"
            )

    def test_multipath_integrability_n2(self):
        """Multi-path integrability verification at n=2."""
        result = verify_integrability_multipath(2, Rational(1), Rational(2))
        assert result["all_paths_confirm"]

    def test_multipath_integrability_n3(self):
        """Multi-path integrability verification at n=3."""
        result = verify_integrability_multipath(3, Rational(1), Rational(2))
        assert result["path1_all_diagonal"]
        assert result["path3_algebraic_independence"]

    def test_multipath_integrability_n4(self):
        """Multi-path integrability verification at n=4."""
        result = verify_integrability_multipath(4, Rational(1), Rational(2))
        assert result["path1_all_diagonal"]


# ================================================================
# CASIMIR ELEMENTS
# ================================================================

class TestCasimirElements:
    """Test Casimir elements of Y^+(gl_hat_1)."""

    def test_first_5_casimirs_n2(self):
        """First 5 Casimir spectra at n=2."""
        casimirs = first_casimirs(2, 5, Rational(1), Rational(2))
        for k in range(1, 6):
            assert k in casimirs
            assert casimirs[k]["dimension"] == 3

    def test_first_5_casimirs_n3(self):
        """First 5 Casimir spectra at n=3."""
        casimirs = first_casimirs(3, 5, Rational(1), Rational(2))
        for k in range(1, 6):
            assert k in casimirs
            assert casimirs[k]["dimension"] == 6

    def test_casimir_1_is_total_content(self):
        """C_1 eigenvalue = total content = E_1."""
        h1, h2 = Rational(1), Rational(2)
        casimir_data = yangian_casimir_eigenvalue(1, 2, h1, h2)
        # The spectrum should match E_1 values
        expected = sorted([Rational(-3), Rational(2), Rational(1)])
        actual = sorted(casimir_data["spectrum"])
        assert actual == expected, f"C_1 spectrum mismatch: {actual} vs {expected}"

    def test_casimir_2_is_energy(self):
        """C_2 eigenvalue = energy = E_2."""
        h1, h2 = Rational(1), Rational(2)
        casimir_data = yangian_casimir_eigenvalue(2, 2, h1, h2)
        expected = sorted([Rational(9), Rational(4), Rational(1)])
        actual = sorted(casimir_data["spectrum"])
        assert actual == expected

    def test_casimir_consistency_with_hamiltonian(self):
        """Casimir eigenvalue = CM Hamiltonian eigenvalue."""
        h1, h2 = Rational(1), Rational(2)
        for n in range(1, 4):
            for k in range(1, 4):
                cas = yangian_casimir_eigenvalue(k, n, h1, h2)
                ham = cm_hamiltonian_from_yangian(k, n, h1, h2)
                assert sorted(cas["all_eigenvalues"]) == sorted(ham["all_eigenvalues"])


# ================================================================
# CUBIC HAMILTONIAN (3D PHENOMENON)
# ================================================================

class TestCubicHamiltonian:
    """Test the cubic CM Hamiltonian H_3."""

    def test_cubic_n1(self):
        """H_3 at n=1: single box at origin, E_3=0."""
        result = cubic_hamiltonian_eigenvalues(1, Rational(1), Rational(2))
        assert result["spectrum"] == [Rational(0)]

    def test_cubic_n2_values(self):
        """H_3 at n=2: exact values.

        At h1=1, h2=2, h3=-3:
          [[2]]:     E_3 = (-3)^3 = -27
          [[1,1]]:   E_3 = 2^3 = 8
          [[1],[1]]: E_3 = 1^3 = 1
        """
        result = cubic_hamiltonian_eigenvalues(2, Rational(1), Rational(2))
        spectrum = sorted(result["spectrum"])
        expected = sorted([Rational(-27), Rational(8), Rational(1)])
        assert spectrum == expected, f"H_3 spectrum at n=2: {spectrum} vs {expected}"

    def test_cubic_column_formula(self):
        """Column partition [[n]]: E_3 = h3^3 * [n(n-1)/2]^2.

        Sum of cubes: sum_{l=0}^{n-1} l^3 = [n(n-1)/2]^2.
        """
        h1, h2 = Rational(1), Rational(2)
        h3 = -(h1 + h2)
        for n in range(1, 6):
            result = cubic_hamiltonian_eigenvalues(n, h1, h2)
            assert result["column_match"], (
                f"Column formula failed at n={n}: "
                f"got {result['column_eigenvalue']}, "
                f"expected {result['column_expected']}"
            )

    def test_cubic_genuinely_3d(self):
        """The cubic Hamiltonian distinguishes 2D and 3D partitions.

        For n >= 2, there exist 3D partitions (with boxes in the l-direction)
        whose E_3 differs from any 2D partition E_3 at the same n.
        This is the "genuinely 3D" property.
        """
        h1, h2 = Rational(1), Rational(2)
        result = cubic_hamiltonian_eigenvalues(2, h1, h2)
        # The 3D partition [[2]] has E_3 = -27
        # The 2D partitions [[1,1]] and [[1],[1]] have E_3 = 8 and 1
        # These are all distinct, confirming 3D sensitivity.
        assert result["num_distinct"] >= 2, (
            "H_3 should distinguish between different plane partitions"
        )


# ================================================================
# BPS EIGENSTATES
# ================================================================

class TestBPSEigenstates:
    """Test BPS eigenstate table."""

    def test_bps_table_n0(self):
        """BPS table at n=0: one state with all E_k=0."""
        table = bps_eigenstate_table(0, Rational(1), Rational(2))
        assert len(table[0]) == 1
        for k, ev in table[0][0]["eigenvalues"].items():
            assert ev == 0

    def test_bps_table_n1(self):
        """BPS table at n=1: one state with all E_k=0."""
        table = bps_eigenstate_table(1, Rational(1), Rational(2))
        assert len(table[1]) == 1
        for k, ev in table[1][0]["eigenvalues"].items():
            assert ev == 0

    def test_bps_table_n2_count(self):
        """BPS table at n=2: three states."""
        table = bps_eigenstate_table(2, Rational(1), Rational(2))
        assert len(table[2]) == 3

    def test_bps_table_n5_count(self):
        """BPS table at n=5: 24 states."""
        table = bps_eigenstate_table(5, Rational(1), Rational(2))
        assert len(table[5]) == 24

    def test_chern_number_normalization(self):
        """Chern character ch_k = E_k / k!."""
        pp = [[2]]
        h1, h2 = Rational(1), Rational(2)
        for k in range(1, 4):
            ev = cm_eigenvalue(pp, k, h1, h2)
            ch = chern_number_eigenvalues(pp, k, h1, h2)
            factorial = Rational(1)
            for i in range(1, k + 1):
                factorial *= i
            assert ch == ev / factorial, (
                f"ch_{k} = E_{k}/k! failed: {ch} vs {ev}/{factorial}"
            )


# ================================================================
# 2D REDUCTION (JACK POLYNOMIALS)
# ================================================================

class TestJackReduction:
    """Test that CY3 CM reduces to 2D (Jack polynomial) CM."""

    def test_2d_reduction_n1(self):
        """2D reduction at n=1."""
        result = verify_2d_reduction(1, 1, Rational(1), Rational(2))
        assert result["all_match"]

    def test_2d_reduction_n2_k1(self):
        """2D reduction at n=2, k=1."""
        result = verify_2d_reduction(2, 1, Rational(1), Rational(2))
        assert result["all_match"]

    def test_2d_reduction_n2_k2(self):
        """2D reduction at n=2, k=2."""
        result = verify_2d_reduction(2, 2, Rational(1), Rational(2))
        assert result["all_match"]

    def test_2d_reduction_n3_k1(self):
        """2D reduction at n=3, k=1."""
        result = verify_2d_reduction(3, 1, Rational(1), Rational(2))
        assert result["all_match"]

    def test_2d_reduction_n3_k2(self):
        """2D reduction at n=3, k=2."""
        result = verify_2d_reduction(3, 2, Rational(1), Rational(2))
        assert result["all_match"]

    def test_2d_reduction_n3_k3(self):
        """2D reduction at n=3, k=3."""
        result = verify_2d_reduction(3, 3, Rational(1), Rational(2))
        assert result["all_match"]

    def test_2d_reduction_n4_k2(self):
        """2D reduction at n=4, k=2."""
        result = verify_2d_reduction(4, 2, Rational(1), Rational(2))
        assert result["all_match"]

    def test_2d_reduction_different_h(self):
        """2D reduction with different equivariant parameters."""
        for h1, h2 in [(Rational(3), Rational(-1)),
                        (Rational(1, 2), Rational(1, 3)),
                        (Rational(5), Rational(7))]:
            result = verify_2d_reduction(3, 2, h1, h2)
            assert result["all_match"], (
                f"2D reduction failed for h=({h1},{h2})"
            )

    def test_jack_eigenvalue_beta_1(self):
        """Jack eigenvalue at beta=1 (free fermion / Schur case).

        At beta=1: content(i,j) = j - i.
        E_1(lambda) = sum (j-i) for (i,j) in lambda.
        For lambda=(2): boxes (0,0) and (0,1), E_1 = 0 + 1 = 1.
        For lambda=(1,1): boxes (0,0) and (1,0), E_1 = 0 + (-1) = -1.
        """
        assert jack_eigenvalue_2d((2,), 1, Rational(1)) == Rational(1)
        assert jack_eigenvalue_2d((1, 1), 1, Rational(1)) == Rational(-1)

    def test_jack_eigenvalue_beta_1_k2(self):
        """Jack E_2 at beta=1.

        For lambda=(2): E_2 = 0^2 + 1^2 = 1.
        For lambda=(1,1): E_2 = 0^2 + (-1)^2 = 1.
        Both give 1 (degenerate!).
        """
        assert jack_eigenvalue_2d((2,), 2, Rational(1)) == Rational(1)
        assert jack_eigenvalue_2d((1, 1), 2, Rational(1)) == Rational(1)


# ================================================================
# CONIFOLD (TWO-CENTER CM)
# ================================================================

class TestConifoldCM:
    """Test the conifold 2-center Calogero-Moser system."""

    def test_conifold_zero_separation(self):
        """At separation=0, conifold = single center."""
        pp1 = [[1]]
        pp2 = [[1]]
        h1, h2 = Rational(1), Rational(2)
        sep = Rational(0)
        ev = conifold_cm_eigenvalue(pp1, pp2, 1, h1, h2, separation=sep)
        # Two boxes, both at origin, E_1 = 0 + 0 = 0
        assert ev == Rational(0)

    def test_conifold_interaction_zero_sep(self):
        """Interaction energy at sep=0 vanishes for k=1."""
        pp1 = [[1]]
        pp2 = [[1]]
        h1, h2 = Rational(1), Rational(2)
        delta = conifold_interaction_energy(pp1, pp2, 1, h1, h2, separation=Rational(0))
        assert delta == Rational(0)

    def test_conifold_separation_shift_k1(self):
        """At nonzero separation, E_1 shifts linearly.

        With one box at each center, sep = Delta:
          E_1 = content(box1) + content(box2) + Delta
              = 0 + (0 + Delta) = Delta.
        """
        pp1 = [[1]]
        pp2 = [[1]]
        h1, h2 = Rational(1), Rational(2)
        sep = Rational(5)
        ev = conifold_cm_eigenvalue(pp1, pp2, 1, h1, h2, separation=sep)
        assert ev == sep, f"E_1 with sep should be {sep}, got {ev}"

    def test_conifold_interaction_nonzero_k2(self):
        """Interaction energy is nonzero for k >= 2 with separation.

        E_2^{global} = content1^2 + (content2 + Delta)^2
        E_2^{naive} = content1^2 + content2^2
        Delta_2 = 2*content2*Delta + Delta^2

        For pp1=[[1]], pp2=[[1]] (both at origin):
          content1 = content2 = 0
          Delta_2 = Delta^2.
        """
        pp1 = [[1]]
        pp2 = [[1]]
        h1, h2 = Rational(1), Rational(2)
        sep = Rational(3)
        delta = conifold_interaction_energy(pp1, pp2, 2, h1, h2, separation=sep)
        expected = sep ** 2  # 0 + (0+3)^2 - (0 + 0) = 9
        assert delta == expected, f"Interaction E_2 should be {expected}, got {delta}"

    def test_conifold_full_spectrum_11(self):
        """Full conifold spectrum at (n1, n2) = (1, 1)."""
        result = conifold_cm_full_spectrum(1, 1, 3, Rational(1), Rational(2),
                                            separation=Rational(1))
        assert result["num_states"] == 1  # pp(1) * pp(1) = 1 * 1

    def test_conifold_full_spectrum_21(self):
        """Full conifold spectrum at (n1, n2) = (2, 1)."""
        result = conifold_cm_full_spectrum(2, 1, 3, Rational(1), Rational(2),
                                            separation=Rational(1))
        assert result["num_states"] == 3  # pp(2) * pp(1) = 3 * 1

    def test_conifold_interaction_k1_vanishes_at_zero_sep(self):
        """The interaction energy for k=1 always vanishes at sep=0.

        At sep=0, the shifted content = unshifted content,
        so E_1^{global}(0) = E_1^{naive}.
        """
        h1, h2 = Rational(1), Rational(2)
        for n1 in range(1, 3):
            for n2 in range(1, 3):
                pps1 = enumerate_plane_partitions(n1)
                pps2 = enumerate_plane_partitions(n2)
                for pp1 in pps1:
                    for pp2 in pps2:
                        delta = conifold_interaction_energy(
                            pp1, pp2, 1, h1, h2, separation=Rational(0)
                        )
                        assert delta == 0, (
                            f"Interaction E_1 at sep=0 should vanish "
                            f"for ({pp1}, {pp2}), got {delta}"
                        )


# ================================================================
# W_{1+infinity} AT c=N
# ================================================================

class TestWAlgebra:
    """Test W_{1+infinity}[N] CM eigenvalues."""

    def test_w_algebra_n1_partition_21(self):
        """W_{1+infinity}[1] eigenvalue for partition (2,1).

        At N=1: h1=1, h2=-1, h3=0.
        Partition (2,1): boxes (0,0), (0,1), (1,0).
        Contents: 0, -1, 1. E_1 = 0, E_2 = 2.
        """
        ev1 = w_algebra_cm_eigenvalue((2, 1), 1, 1)
        ev2 = w_algebra_cm_eigenvalue((2, 1), 2, 1)
        assert ev1 == Rational(0)
        assert ev2 == Rational(2)

    def test_w_algebra_n2_partition_2(self):
        """W_{1+infinity}[2] eigenvalue for partition (2).

        At N=2: h1=1, h2=-2, h3=1.
        Partition (2): boxes (0,0), (0,1).
        Contents: 0, -2. E_1 = -2, E_2 = 4.
        """
        ev1 = w_algebra_cm_eigenvalue((2,), 1, 2)
        ev2 = w_algebra_cm_eigenvalue((2,), 2, 2)
        assert ev1 == Rational(-2)
        assert ev2 == Rational(4)

    def test_virasoro_L0(self):
        """Virasoro L_0 eigenvalue from W_{1+infinity}."""
        result = w_algebra_virasoro_eigenvalue((2,), 1)
        # N=1: h1=1, h2=-1, h3=0. (2): contents 0, -1. E_2 = 1.
        assert result["L_0"] == Rational(1)
        assert result["central_charge"] == Rational(1)

    def test_virasoro_central_charge(self):
        """Central charge of W_{1+infinity}[N] is N."""
        for N in [1, 2, 3, 5]:
            result = w_algebra_virasoro_eigenvalue((1,), N)
            assert result["central_charge"] == Rational(N)


# ================================================================
# MULTI-PATH VERIFICATION
# ================================================================

class TestMultiPathVerification:
    """Test multi-path eigenvalue verification."""

    def test_three_paths_n2_k2(self):
        """Three-path verification for n=2, k=2."""
        pp = [[2]]
        result = verify_cm_eigenvalue_three_paths(pp, 2, Rational(1), Rational(2))
        assert result["all_match"], (
            f"Three paths disagree: "
            f"P1={result['path1_direct_sum']}, "
            f"P2={result['path2_newton_identity']}, "
            f"P3={result['path3_horner']}"
        )

    def test_three_paths_n3_k3(self):
        """Three-path verification for n=3, k=3."""
        pp = [[2, 1]]
        result = verify_cm_eigenvalue_three_paths(pp, 3, Rational(1), Rational(2))
        assert result["all_match"]

    def test_three_paths_all_n2(self):
        """Three-path verification for all plane partitions of 2."""
        h1, h2 = Rational(1), Rational(2)
        pps = enumerate_plane_partitions(2)
        for pp in pps:
            for k in range(1, 5):
                result = verify_cm_eigenvalue_three_paths(pp, k, h1, h2)
                assert result["all_match"], (
                    f"Three paths disagree for pp={pp}, k={k}"
                )

    def test_three_paths_all_n3(self):
        """Three-path verification for all plane partitions of 3."""
        h1, h2 = Rational(1), Rational(2)
        pps = enumerate_plane_partitions(3)
        for pp in pps:
            for k in range(1, 4):
                result = verify_cm_eigenvalue_three_paths(pp, k, h1, h2)
                assert result["all_match"], (
                    f"Three paths disagree for pp={pp}, k={k}"
                )

    def test_three_paths_different_h(self):
        """Three-path verification with different equivariant parameters."""
        for h1, h2 in [(Rational(3), Rational(-1)),
                        (Rational(1, 2), Rational(1, 3)),
                        (Rational(5), Rational(7))]:
            pp = [[2, 1]]
            result = verify_cm_eigenvalue_three_paths(pp, 3, h1, h2)
            assert result["all_match"], (
                f"Three paths disagree for h=({h1},{h2})"
            )


# ================================================================
# CM HAMILTONIAN AS MATRIX
# ================================================================

class TestCMHamiltonianMatrix:
    """Test CM Hamiltonian matrix construction."""

    def test_matrix_diagonal_n2(self):
        """H_k matrix is diagonal at n=2."""
        h1, h2 = Rational(1), Rational(2)
        for k in range(1, 4):
            mat = cm_hamiltonian_matrix(k, 2, h1, h2)
            dim = len(mat)
            assert dim == 3
            for i in range(dim):
                for j in range(dim):
                    if i != j:
                        assert mat[i][j] == 0

    def test_matrix_trace_n2_k1(self):
        """Tr(H_1) at n=2 = sum of all E_1 eigenvalues.

        E_1 values: -3, 2, 1. Sum = 0.
        Check: h1+h2+h3 = 0 by CY, and each E_1 is a single content.
        Total = sum over all pp's of their total content.
        """
        h1, h2 = Rational(1), Rational(2)
        mat = cm_hamiltonian_matrix(1, 2, h1, h2)
        trace = sum(mat[i][i] for i in range(len(mat)))
        assert trace == Rational(-3) + Rational(2) + Rational(1)
        assert trace == Rational(0)

    def test_matrix_eigenvalues_match_direct(self):
        """Matrix diagonal entries match direct eigenvalue computation."""
        h1, h2 = Rational(1), Rational(2)
        pps = enumerate_plane_partitions(3)
        for k in range(1, 4):
            mat = cm_hamiltonian_matrix(k, 3, h1, h2)
            for idx, pp in enumerate(pps):
                ev_direct = cm_eigenvalue(pp, k, h1, h2)
                assert mat[idx][idx] == ev_direct, (
                    f"Matrix entry [{idx},{idx}] = {mat[idx][idx]} "
                    f"!= direct ev = {ev_direct} for pp={pp}, k={k}"
                )


# ================================================================
# COMPREHENSIVE COMPUTATION
# ================================================================

class TestComprehensive:
    """Test the comprehensive CM computation."""

    def test_comprehensive_runs(self):
        """Comprehensive computation completes without error."""
        result = cm_comprehensive_computation(
            max_n=3, h1=Rational(1), h2=Rational(2), max_k=3
        )
        assert "bps_table" in result
        assert "integrability" in result
        assert "cubic" in result
        assert "reduction_2d" in result

    def test_comprehensive_integrability(self):
        """All integrability checks pass in comprehensive computation."""
        result = cm_comprehensive_computation(
            max_n=3, h1=Rational(1), h2=Rational(2), max_k=3
        )
        for n, integ in result["integrability"].items():
            assert integ["all_commutators_zero"], (
                f"Integrability failed at n={n}"
            )

    def test_comprehensive_cubic_column(self):
        """All column formula checks pass in comprehensive computation."""
        result = cm_comprehensive_computation(
            max_n=4, h1=Rational(1), h2=Rational(2), max_k=3
        )
        for n, cub in result["cubic"].items():
            assert cub["column_match"], f"Column formula failed at n={n}"

    def test_comprehensive_2d_reduction(self):
        """All 2D reduction checks pass."""
        result = cm_comprehensive_computation(
            max_n=3, h1=Rational(1), h2=Rational(2), max_k=3
        )
        for key, red in result["reduction_2d"].items():
            assert red["all_match"], f"2D reduction failed at {key}"


# ================================================================
# PARAMETER INDEPENDENCE
# ================================================================

class TestParameterIndependence:
    """Test with multiple parameter choices to ensure robustness."""

    @pytest.mark.parametrize("h1,h2", [
        (Rational(1), Rational(2)),
        (Rational(3), Rational(-1)),
        (Rational(1, 2), Rational(1, 3)),
        (Rational(5), Rational(7)),
        (Rational(-2), Rational(5)),
    ])
    def test_E1_n1_always_zero(self, h1, h2):
        """E_1 at n=1 is always 0 (box at origin)."""
        pp = [[1]]
        assert cm_eigenvalue(pp, 1, h1, h2) == 0

    @pytest.mark.parametrize("h1,h2", [
        (Rational(1), Rational(2)),
        (Rational(3), Rational(-1)),
        (Rational(1, 2), Rational(1, 3)),
    ])
    def test_commutativity_different_h(self, h1, h2):
        """Integrability holds for different equivariant parameters."""
        result = verify_cm_commutativity(3, 3, h1, h2)
        assert result["all_commutators_zero"]

    @pytest.mark.parametrize("h1,h2", [
        (Rational(1), Rational(2)),
        (Rational(3), Rational(-1)),
    ])
    def test_column_formula_different_h(self, h1, h2):
        """Column formula E_3 = h3^3 * [n(n-1)/2]^2 for different h."""
        for n in range(1, 5):
            result = cubic_hamiltonian_eigenvalues(n, h1, h2)
            assert result["column_match"], (
                f"Column formula failed at n={n} for h=({h1},{h2})"
            )


# ================================================================
# EDGE CASES AND CONSISTENCY
# ================================================================

class TestEdgeCases:
    """Test edge cases and consistency conditions."""

    def test_empty_partition_eigenvalue(self):
        """Empty partition has E_k = 0 for all k."""
        pp: List[List[int]] = []
        h1, h2 = Rational(1), Rational(2)
        for k in range(1, 6):
            assert cm_eigenvalue(pp, k, h1, h2) == 0

    def test_CY_condition_content_sum(self):
        """CY condition implies specific content sum identities.

        For any plane partition pi, the contents c_i = h1*a_i + h2*b_i + h3*l_i
        satisfy: if we sum c_i over a SINGLE ROW of the 2D base at height 0,
        the sum is a multiple of h2.
        """
        h1, h2 = Rational(1), Rational(2)
        h3 = -(h1 + h2)
        # Row partition [[1,1,...,1]] of length m: all at (0, j, 0)
        for m in range(1, 5):
            pp = [[1] * m]
            ev1 = cm_eigenvalue(pp, 1, h1, h2)
            expected = h2 * m * (m - 1) / 2  # sum of h2*j for j=0..m-1
            assert ev1 == expected

    def test_symmetry_under_h1_h2_swap(self):
        """Swapping h1 <-> h2 permutes eigenvalue spectrum.

        Under h1 <-> h2, the content of box (i,j,l) becomes h2*i + h1*j + h3*l.
        This is equivalent to reflecting the plane partition in the i<->j axis.
        The SPECTRUM (set of eigenvalues with multiplicities) is preserved
        because reflection is a bijection on plane partitions.
        """
        h1, h2 = Rational(1), Rational(2)
        for n in range(1, 4):
            for k in range(1, 4):
                data_12 = cm_hamiltonian_from_yangian(k, n, h1, h2)
                data_21 = cm_hamiltonian_from_yangian(k, n, h2, h1)
                spec_12 = sorted(data_12["all_eigenvalues"])
                spec_21 = sorted(data_21["all_eigenvalues"])
                assert spec_12 == spec_21, (
                    f"Spectrum not invariant under h1<->h2 swap "
                    f"at n={n}, k={k}: {spec_12} vs {spec_21}"
                )

    def test_hamiltonian_from_yangian_dimension(self):
        """Hamiltonian spectrum dimension matches pp(n)."""
        pp_counts = {1: 1, 2: 3, 3: 6, 4: 13, 5: 24}
        h1, h2 = Rational(1), Rational(2)
        for n, expected_dim in pp_counts.items():
            data = cm_hamiltonian_from_yangian(1, n, h1, h2)
            assert data["dimension"] == expected_dim
