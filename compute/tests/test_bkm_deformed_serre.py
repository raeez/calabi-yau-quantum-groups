r"""Tests for bkm_deformed_serre.py: BKM deformed Serre relations
from the Borcherds deformed OPE.

STATUS: ALL results are CONJECTURAL (AP-CY14).
Tests verify INTERNAL CONSISTENCY of the deformed OPE approach,
not existence of the BKM Yangian Y(g_hat_{Delta_5}).

WHAT IS TESTED
==============

Section 1: Deformed OPE exponent formula (13 tests)
Section 2: OPE singularity classification (12 tests)
Section 3: Discriminant-by-discriminant Serre analysis (10 tests)
Section 4: Cross-discriminant Serre table (8 tests)
Section 5: Imaginary-real mixing (adjoint action) (6 tests)
Section 6: Serre ideal finiteness analysis (10 tests)
Section 7: D = 3 explicit Serre relation (8 tests)
Section 8: D = 0 lightlike sector (8 tests)
Section 9: Complete summary and cross-engine verification (9 tests)

Total: 84 tests

CRITICAL AP COMPLIANCE
======================

AP-CY7:  Vertex algebra methods, NOT CoHA.
AP-CY14: All Yangian results are CONJECTURAL.
AP-CY9:  Discriminant constraint: D = 0 or 3 mod 4 for index 1.
AP-CY20: Omega-background intermediary stated explicitly.
AP-CY8:  Bar Euler = BKM denominator requires CY-A + Vol I anchor.
AP113:   kappa subscripts: kappa_BKM = 5, never bare kappa.
AP-CY31: Spectral parameter u is Yangian spectral, NOT worldsheet.
AP-CY24: All numerical values verified against function output.

Manuscript references:
    k3_times_e.tex sec:k3e-bkm-chiral-status
    k3_times_e.tex rem:borcherds-serre-obstruction
    k3_times_e.tex subsubsec:k3e-yangian-currents-serre
"""

import math
import pytest

from compute.lib.bkm_deformed_serre import (
    # Constants
    STATUS,
    GRAM_MATRIX,
    KNOWN_C_TABLE,
    VALID_DISCRIMINANT_RESIDUES,
    SERRE_CRITICAL_D,
    SERRE_KERNEL_SIZE,
    # OPE exponents
    deformed_ope_exponent_self,
    deformed_ope_exponent_cross,
    # Singularity classification
    classify_ope_singularity,
    OPESingularity,
    # Serre analysis
    serre_at_discriminant,
    serre_census,
    # Cross-Serre
    cross_serre_table,
    # Imaginary-real mixing
    imaginary_real_mixing,
    # Finiteness
    serre_ideal_finiteness,
    # D = 3
    d3_serre_relation,
    # D = 0
    d0_lightlike_serre,
    # Summary
    deformed_serre_summary,
)


# ---------------------------------------------------------------------------
# Helper for cross-engine imports
# ---------------------------------------------------------------------------

def _import_bkm_bar():
    """Import k3_elliptic_genus_bkm_bar for cross-checks."""
    try:
        from compute.lib import k3_elliptic_genus_bkm_bar
        return k3_elliptic_genus_bkm_bar
    except (ImportError, ModuleNotFoundError):
        import importlib, os, sys
        _lib_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '..', 'lib')
        if _lib_dir not in sys.path:
            sys.path.insert(0, _lib_dir)
        return importlib.import_module('k3_elliptic_genus_bkm_bar')


def _import_borcherds_vertex():
    """Import borcherds_vertex_yangian for cross-checks."""
    try:
        from compute.lib import borcherds_vertex_yangian
        return borcherds_vertex_yangian
    except (ImportError, ModuleNotFoundError):
        import importlib, os, sys
        _lib_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '..', 'lib')
        if _lib_dir not in sys.path:
            sys.path.insert(0, _lib_dir)
        return importlib.import_module('borcherds_vertex_yangian')


def _import_bkm_yangian():
    """Import bkm_yangian_generators for cross-checks."""
    try:
        from compute.lib import bkm_yangian_generators
        return bkm_yangian_generators
    except (ImportError, ModuleNotFoundError):
        import importlib, os, sys
        _lib_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '..', 'lib')
        if _lib_dir not in sys.path:
            sys.path.insert(0, _lib_dir)
        return importlib.import_module('bkm_yangian_generators')


# ===========================================================================
# SECTION 1: DEFORMED OPE EXPONENT FORMULA
# ===========================================================================

class TestDeformedOPEExponent:
    """Deformed OPE exponent P(D, eps) at self and cross level."""

    def test_self_exponent_formula_d_minus1(self):
        """P_self(-1, 1) = (-1)((-1)-4) = (-1)(-5) = 5.

        Multi-path: (1) function, (2) direct formula D*(D-4).
        """
        # VERIFIED [DC] direct computation
        assert deformed_ope_exponent_self(-1, 1.0) == 5.0
        assert (-1) * ((-1) - 4) == 5

    def test_self_exponent_formula_d0(self):
        """P_self(0, 1) = 0*(0-4) = 0.

        Multi-path: (1) function, (2) direct formula.
        """
        # VERIFIED [DC] direct computation
        assert deformed_ope_exponent_self(0, 1.0) == 0.0
        assert 0 * (0 - 4) == 0

    def test_self_exponent_formula_d3(self):
        """P_self(3, 1) = 3*(3-4) = 3*(-1) = -3.

        Multi-path: (1) function, (2) formula, (3) undeformed + correction.
        """
        # VERIFIED [DC] direct computation
        P = deformed_ope_exponent_self(3, 1.0)
        assert P == -3.0
        assert 3 * (3 - 4) == -3
        # Path 3: undeformed + correction
        undeformed = -2 * 3  # = -6
        correction = 3**2 - 2 * 3  # = 3
        assert undeformed + 1.0 * correction == -3.0

    def test_self_exponent_formula_d4(self):
        """P_self(4, 1) = 4*(4-4) = 0.

        Multi-path: (1) function, (2) formula.
        """
        # VERIFIED [DC] direct computation
        assert deformed_ope_exponent_self(4, 1.0) == 0.0
        assert 4 * (4 - 4) == 0

    def test_self_exponent_formula_d7(self):
        """P_self(7, 1) = 7*(7-4) = 7*3 = 21.

        Multi-path: (1) function, (2) formula.
        """
        # VERIFIED [DC] direct computation
        assert deformed_ope_exponent_self(7, 1.0) == 21.0
        assert 7 * (7 - 4) == 21

    def test_self_exponent_formula_d8(self):
        """P_self(8, 1) = 8*(8-4) = 32.

        Multi-path: (1) function, (2) formula.
        """
        # VERIFIED [DC] direct computation
        assert deformed_ope_exponent_self(8, 1.0) == 32.0
        assert 8 * (8 - 4) == 32

    def test_self_exponent_undeformed(self):
        """At eps=0: P_self(D, 0) = -2D for all D.

        Multi-path: (1) function, (2) lattice inner product formula.
        """
        # VERIFIED [DC] direct computation
        for D in [-1, 0, 3, 4, 7, 8]:
            P = deformed_ope_exponent_self(D, 0.0)
            assert P == -2.0 * D, f"D={D}: expected {-2.0*D}, got {P}"

    def test_self_exponent_negative_only_at_d3(self):
        """Among valid discriminants, P_self(D, 1) < 0 ONLY for D = 3.

        Multi-path: (1) check all valid D up to 20, (2) algebraic argument.
        """
        # VERIFIED [DC] exhaustive check
        bkm_bar = _import_bkm_bar()
        table = bkm_bar.c_table_from_phi01(20)
        negative_D = []
        for D in sorted(table.keys()):
            if table[D] == 0:
                continue
            P = deformed_ope_exponent_self(D, 1.0)
            if P < -1e-10:
                negative_D.append(D)
        assert negative_D == [3], f"Expected [3], got {negative_D}"
        # Algebraic: D*(D-4) < 0 iff 0 < D < 4; valid D in (0,4) is only D=3
        for D in range(1, 4):
            if (D % 4) in VALID_DISCRIMINANT_RESIDUES and D > 0:
                assert D == 3

    def test_cross_exponent_generic_orthogonal(self):
        """P_cross(D1, D2, 1, ip=0) = D1*D2 for generic orthogonal roots.

        Multi-path: (1) function, (2) formula.
        """
        # VERIFIED [DC] direct computation
        for D1, D2 in [(3, 4), (0, 3), (7, 8), (-1, 3)]:
            P = deformed_ope_exponent_cross(D1, D2, 1.0, 0)
            assert P == float(D1 * D2), (
                f"D1={D1}, D2={D2}: expected {D1*D2}, got {P}"
            )

    def test_cross_exponent_weyl_to_spacelike(self):
        """P_cross(-1, 3, 1) = -1*3 = -3 (pole of order 3).

        Multi-path: (1) function, (2) formula.
        """
        # VERIFIED [DC] direct computation
        assert deformed_ope_exponent_cross(-1, 3, 1.0) == -3.0
        assert (-1) * 3 == -3

    def test_cross_exponent_with_inner_product(self):
        """Cross-OPE with nonzero inner product: P = 2*ip + D1*D2 at eps=1.

        Multi-path: (1) function, (2) formula ip*(1+eps) + eps*D1*D2.
        """
        # VERIFIED [DC] direct computation
        # D1=0, D2=0, ip=-1: P = -1*(1+1) + 1*0*0 = -2
        P = deformed_ope_exponent_cross(0, 0, 1.0, -1)
        assert P == -2.0
        assert (-1) * (1 + 1) + 1 * 0 * 0 == -2
        # D1=0, D2=0, ip=1: P = 1*(1+1) + 0 = 2
        P = deformed_ope_exponent_cross(0, 0, 1.0, 1)
        assert P == 2.0

    def test_cross_exponent_symmetric(self):
        """P_cross(D1, D2) = P_cross(D2, D1) for generic orthogonal roots.

        Multi-path: (1) function evaluation, (2) D1*D2 commutes.
        """
        for D1, D2 in [(3, 4), (-1, 7), (0, 8)]:
            P12 = deformed_ope_exponent_cross(D1, D2, 1.0)
            P21 = deformed_ope_exponent_cross(D2, D1, 1.0)
            assert P12 == P21

    def test_self_exponent_cross_engine_consistency(self):
        """Cross-check P_self against borcherds_vertex_yangian.ope_coefficient_matrix.

        Multi-path: (1) our formula, (2) borcherds_vertex engine.
        """
        bv = _import_borcherds_vertex()
        for D in [0, 3, 4, 7]:
            our_P = deformed_ope_exponent_self(D, 1.0)
            bv_ope = bv.ope_coefficient_matrix(D, D, epsilon=1.0)
            # bv computes: -2D + eps*(D^2 - 2D) = D^2 - 4D = our formula
            assert abs(our_P - bv_ope['ope_exponent_at_eps1']) < 1e-10, (
                f"D={D}: our P={our_P}, bv P={bv_ope['ope_exponent_at_eps1']}"
            )


# ===========================================================================
# SECTION 2: OPE SINGULARITY CLASSIFICATION
# ===========================================================================

class TestOPESingularityClassification:
    """Classification of OPE singularities into regular/marginal/pole."""

    def test_d_minus1_regular(self):
        """D = -1: self-OPE is REGULAR (P = 5 > 0)."""
        sing = classify_ope_singularity(-1, -1, 1.0)
        assert sing.singularity_type == 'regular'
        assert sing.pole_order == 0

    def test_d0_marginal(self):
        """D = 0: self-OPE is MARGINAL (P = 0)."""
        sing = classify_ope_singularity(0, 0, 1.0)
        assert sing.singularity_type == 'marginal'
        assert sing.pole_order == 0

    def test_d3_pole(self):
        """D = 3: self-OPE has POLE of order 3.

        Multi-path: (1) classification, (2) ceil(-P) = ceil(3) = 3.
        """
        sing = classify_ope_singularity(3, 3, 1.0)
        assert sing.singularity_type == 'pole'
        assert sing.pole_order == 3
        # Cross-check: ceil(-(-3)) = 3
        assert int(math.ceil(-(-3.0) - 1e-10)) == 3

    def test_d4_marginal(self):
        """D = 4: self-OPE is MARGINAL (P = 0)."""
        sing = classify_ope_singularity(4, 4, 1.0)
        assert sing.singularity_type == 'marginal'
        assert sing.pole_order == 0

    def test_d7_regular(self):
        """D = 7: self-OPE is REGULAR (P = 21 > 0)."""
        sing = classify_ope_singularity(7, 7, 1.0)
        assert sing.singularity_type == 'regular'
        assert sing.pole_order == 0

    def test_d8_regular(self):
        """D = 8: self-OPE is REGULAR (P = 32 > 0)."""
        sing = classify_ope_singularity(8, 8, 1.0)
        assert sing.singularity_type == 'regular'
        assert sing.pole_order == 0

    def test_cross_d3_d4_regular(self):
        """Cross D1=3, D2=4: P = 12 > 0, REGULAR."""
        sing = classify_ope_singularity(3, 4, 1.0, inner_product=0)
        assert sing.singularity_type == 'regular'
        assert sing.pole_order == 0

    def test_cross_dm1_d3_pole(self):
        """Cross D1=-1, D2=3: P = -3, POLE of order 3."""
        sing = classify_ope_singularity(-1, 3, 1.0, inner_product=0)
        assert sing.singularity_type == 'pole'
        assert sing.pole_order == 3

    def test_cross_d0_d3_marginal(self):
        """Cross D1=0, D2=3: P = 0, MARGINAL."""
        sing = classify_ope_singularity(0, 3, 1.0, inner_product=0)
        assert sing.singularity_type == 'marginal'
        assert sing.pole_order == 0

    def test_ope_type_self(self):
        """Self-OPE correctly labeled."""
        sing = classify_ope_singularity(3, 3, 1.0)
        assert sing.ope_type == 'self'

    def test_ope_type_cross(self):
        """Cross-OPE correctly labeled."""
        sing = classify_ope_singularity(3, 4, 1.0, inner_product=0)
        assert sing.ope_type == 'cross'

    def test_inner_product_stored(self):
        """Inner product is stored in the result."""
        sing = classify_ope_singularity(3, 3, 1.0)
        assert sing.inner_product == -6  # (alpha,alpha) = -2*3 = -6


# ===========================================================================
# SECTION 3: DISCRIMINANT-BY-DISCRIMINANT SERRE
# ===========================================================================

class TestSerreAtDiscriminant:
    """Serre analysis at individual discriminants."""

    def test_d1_not_valid(self):
        """D = 1 is not a valid discriminant (AP-CY9: 1 mod 4 = 1).

        Multi-path: (1) serre_at_discriminant, (2) discriminant constraint.
        """
        # VERIFIED [DC] 1 mod 4 = 1, not in {0, 3}
        result = serre_at_discriminant(1)
        assert result['has_generators'] is False
        assert result['multiplicity'] == 0
        assert 1 % 4 not in VALID_DISCRIMINANT_RESIDUES

    def test_d2_not_valid(self):
        """D = 2 is not a valid discriminant (AP-CY9: 2 mod 4 = 2)."""
        result = serre_at_discriminant(2)
        assert result['has_generators'] is False
        assert 2 % 4 not in VALID_DISCRIMINANT_RESIDUES

    def test_d3_has_generators(self):
        """D = 3 has 64 fermionic generators."""
        result = serre_at_discriminant(3)
        assert result['has_generators'] is True
        assert result['multiplicity'] == 64
        assert result['parity'] == 'fermionic'

    def test_d3_self_ope_exponent(self):
        """D = 3: self-OPE exponent is -3.

        Multi-path: (1) serre_at_discriminant, (2) direct formula.
        """
        result = serre_at_discriminant(3)
        assert result['self_ope_exponent'] == -3.0
        assert 3 * (3 - 4) == -3

    def test_d0_has_10_generators(self):
        """D = 0 has 10 bosonic generators (kappa_BKM = 5)."""
        result = serre_at_discriminant(0)
        assert result['multiplicity'] == 10
        assert result['parity'] == 'bosonic'

    def test_d_minus1_has_1_generator(self):
        """D = -1 has 1 bosonic generator (Weyl vector)."""
        result = serre_at_discriminant(-1)
        assert result['multiplicity'] == 1
        assert result['parity'] == 'bosonic'

    def test_d_minus1_regular(self):
        """D = -1: self-OPE is regular (free generator)."""
        result = serre_at_discriminant(-1)
        assert result['singularity']['singularity_type'] == 'regular'

    def test_status_conjectural(self):
        """All results are CONJECTURAL (AP-CY14)."""
        result = serre_at_discriminant(3)
        assert result['status'] == 'CONJECTURAL'

    def test_census_serre_kernel_size(self):
        """Serre kernel has 182 generators (10 + 64 + 108).

        Multi-path: (1) SERRE_KERNEL_SIZE constant, (2) sum.
        """
        # VERIFIED [DC] 10 + 64 + 108 = 182
        assert SERRE_KERNEL_SIZE == 182
        assert abs(KNOWN_C_TABLE[0]) + abs(KNOWN_C_TABLE[3]) + abs(KNOWN_C_TABLE[4]) == 182

    def test_census_only_d3_has_pole(self):
        """Among all valid discriminants up to D=20, only D=3 has a pole.

        Multi-path: (1) serre_census, (2) algebraic argument.
        """
        census = serre_census(D_max=20)
        pole_sectors = census['pole']['sectors']
        pole_discriminants = [s['discriminant'] for s in pole_sectors]
        assert pole_discriminants == [3], f"Expected [3], got {pole_discriminants}"


# ===========================================================================
# SECTION 4: CROSS-DISCRIMINANT SERRE TABLE
# ===========================================================================

class TestCrossSerreTable:
    """Cross-discriminant Serre table."""

    def test_cross_table_has_entries(self):
        """Cross-Serre table has entries for the default D list."""
        table = cross_serre_table()
        assert table['total_pairs'] > 0

    def test_cross_d3_d4_regular(self):
        """D1=3, D2=4: cross-OPE is regular (P = 12 > 0)."""
        table = cross_serre_table(D_list=[3, 4])
        entries = table['entries']
        assert len(entries) == 1
        assert entries[0]['singularity_type'] == 'regular'
        assert entries[0]['cross_ope_exponent'] == 12.0

    def test_cross_dm1_d3_pole(self):
        """D1=-1, D2=3: cross-OPE has pole (P = -3)."""
        table = cross_serre_table(D_list=[-1, 3])
        nontrivial = table['nontrivial']
        assert len(nontrivial) >= 1
        dm1_d3 = [e for e in nontrivial
                   if e['D1'] == -1 and e['D2'] == 3]
        assert len(dm1_d3) == 1
        assert dm1_d3[0]['cross_ope_exponent'] == -3.0

    def test_cross_d0_d3_marginal(self):
        """D1=0, D2=3: cross-OPE is marginal (P = 0)."""
        table = cross_serre_table(D_list=[0, 3])
        entries = table['entries']
        d0_d3 = [e for e in entries if e['D1'] == 0 and e['D2'] == 3]
        assert len(d0_d3) == 1
        assert d0_d3[0]['singularity_type'] == 'marginal'

    def test_spacelike_spacelike_all_regular(self):
        """All cross-OPE between D1, D2 > 0 are regular (P = D1*D2 > 0).

        Multi-path: (1) cross_serre_table, (2) algebraic argument.
        """
        # VERIFIED [DC] D1*D2 > 0 for D1, D2 > 0
        table = cross_serre_table(D_list=[3, 4, 7, 8])
        for entry in table['entries']:
            assert entry['singularity_type'] == 'regular', (
                f"D1={entry['D1']}, D2={entry['D2']}: "
                f"expected regular, got {entry['singularity_type']}"
            )

    def test_nontrivial_involves_d_minus1_or_d0(self):
        """All nontrivial cross-Serre involve D = -1 or D = 0."""
        table = cross_serre_table()
        for entry in table['nontrivial']:
            assert entry['D1'] <= 0 or entry['D2'] <= 0, (
                f"Nontrivial cross-Serre between D1={entry['D1']} and "
                f"D2={entry['D2']} -- both positive, should be regular"
            )

    def test_cross_exponent_formula_d1d2(self):
        """Cross-OPE exponent is D1*D2 for generic orthogonal roots.

        Multi-path: (1) table entries, (2) formula verification.
        """
        table = cross_serre_table(D_list=[-1, 0, 3, 4])
        for entry in table['entries']:
            expected = float(entry['D1'] * entry['D2'])
            assert abs(entry['cross_ope_exponent'] - expected) < 1e-10

    def test_status_conjectural(self):
        """Status is CONJECTURAL."""
        table = cross_serre_table()
        assert table['status'] == 'CONJECTURAL'


# ===========================================================================
# SECTION 5: IMAGINARY-REAL MIXING (ADJOINT ACTION)
# ===========================================================================

class TestImaginaryRealMixing:
    """Imaginary-real mixing: adjoint action of Cartan on imaginary roots."""

    def test_d3_has_mixing(self):
        """D = 3 imaginary root has mixing with real Cartan."""
        result = imaginary_real_mixing(3)
        assert result['has_mixing'] is True
        assert result['multiplicity'] == 64

    def test_d0_has_mixing(self):
        """D = 0 lightlike root has mixing with Cartan."""
        result = imaginary_real_mixing(0)
        assert result['has_mixing'] is True
        assert result['multiplicity'] == 10

    def test_d1_no_mixing(self):
        """D = 1 is not a valid discriminant: no mixing."""
        result = imaginary_real_mixing(1)
        assert result['has_mixing'] is False

    def test_cartan_eigenvalue_integer(self):
        """Cartan eigenvalues are integers (lattice inner products)."""
        result = imaginary_real_mixing(3)
        assert result['cartan_eigenvalue_type'] == 'integer (lattice inner product)'

    def test_deformation_stability(self):
        """Deformation preserves the Cartan-imaginary OPE at leading order."""
        result = imaginary_real_mixing(3)
        assert 'PRESERVED' in result['deformation_stability']

    def test_status_conjectural(self):
        """Status is CONJECTURAL."""
        result = imaginary_real_mixing(3)
        assert result['status'] == 'CONJECTURAL'


# ===========================================================================
# SECTION 6: SERRE IDEAL FINITENESS
# ===========================================================================

class TestSerreIdealFiniteness:
    """Finiteness analysis of the BKM Yangian Serre ideal."""

    def test_infinitely_generated(self):
        """Serre ideal is infinitely generated (infinite discriminants)."""
        result = serre_ideal_finiteness()
        assert result['infinitely_generated'] is True

    def test_finitely_determined(self):
        """Serre ideal is finitely determined (finite kernel)."""
        result = serre_ideal_finiteness()
        assert result['finitely_determined'] is True

    def test_kernel_discriminants(self):
        """Serre kernel is at D in {0, 3, 4}.

        Multi-path: (1) finiteness analysis, (2) SERRE_CRITICAL_D constant.
        """
        result = serre_ideal_finiteness()
        assert set(result['serre_kernel']['discriminants']) == {0, 3, 4}
        assert set(result['serre_kernel']['discriminants']) == SERRE_CRITICAL_D

    def test_kernel_total_182(self):
        """Serre kernel has 182 generators total.

        Multi-path: (1) finiteness analysis, (2) 10 + 64 + 108 = 182.
        """
        result = serre_ideal_finiteness()
        assert result['serre_kernel']['total'] == 182
        assert 10 + 64 + 108 == 182

    def test_kernel_sizes(self):
        """Kernel sizes: D=0: 10, D=3: 64, D=4: 108.

        Multi-path: (1) finiteness analysis, (2) KNOWN_C_TABLE.
        """
        result = serre_ideal_finiteness()
        sizes = result['serre_kernel']['sizes']
        assert sizes[0] == 10
        assert sizes[3] == 64
        assert sizes[4] == 108

    def test_critical_boundary_at_5(self):
        """Critical boundary: D >= 5 has trivial self-Serre."""
        result = serre_ideal_finiteness()
        assert result['critical_boundary']['D'] == 5

    def test_unique_nontrivial_pole_at_d3(self):
        """Unique nontrivial pole is at D = 3."""
        result = serre_ideal_finiteness()
        assert result['unique_nontrivial_pole']['discriminant'] == 3
        assert result['unique_nontrivial_pole']['pole_order'] == 3
        assert result['unique_nontrivial_pole']['parity'] == 'fermionic'

    def test_commutativity_broken_only_d3(self):
        """Standard Borcherds-Serre commutativity broken ONLY at D = 3."""
        result = serre_ideal_finiteness()
        broken = result['commutativity_comparison']['deformation_breaks_commutativity']
        assert broken['D_values'] == [3]

    def test_tail_generators_positive(self):
        """Serre tail (free generators at D >= 5) is nonempty."""
        result = serre_ideal_finiteness()
        assert result['serre_tail']['generators'] > 0

    def test_status_conjectural(self):
        """Status is CONJECTURAL."""
        result = serre_ideal_finiteness()
        assert result['status'] == 'CONJECTURAL'


# ===========================================================================
# SECTION 7: D = 3 EXPLICIT SERRE RELATION
# ===========================================================================

class TestD3SerreRelation:
    """Explicit Serre relation at D = 3 (the unique nontrivial case)."""

    def test_d3_pole_order_3(self):
        """D = 3 self-OPE has pole of order 3.

        Multi-path: (1) d3_serre_relation, (2) P = -3 -> pole order 3.
        """
        result = d3_serre_relation()
        assert result['pole_order'] == 3
        assert result['self_ope_exponent'] == -3.0

    def test_d3_fermionic(self):
        """D = 3 generators are fermionic (c(3) = -64 < 0)."""
        result = d3_serre_relation()
        assert result['parity'] == 'fermionic'
        assert result['c_value'] == -64

    def test_d3_multiplicity_64(self):
        """D = 3 has 64 generators."""
        result = d3_serre_relation()
        assert result['multiplicity'] == 64

    def test_d6_not_valid(self):
        """D = 6 is NOT a valid discriminant (6 mod 4 = 2).

        Multi-path: (1) d3 result, (2) AP-CY9 constraint.
        """
        result = d3_serre_relation()
        assert result['d6_not_valid']['valid'] is False
        assert 6 % 4 == 2
        assert 2 not in VALID_DISCRIMINANT_RESIDUES

    def test_d3_bracket_output_at_d12(self):
        """D = 3 bracket output is at D = 12 (not D = 6).

        The vertex operator V(alpha + alpha) has norm 4*(alpha,alpha) = -24,
        giving discriminant D = 12. Multi-path: (1) d3 result,
        (2) norm doubling computation, (3) c(12) = 4016 check.
        """
        result = d3_serre_relation()
        layer1 = result['layers']['layer_1']
        assert layer1['actual_target_discriminant'] == 12
        # Norm doubling: (2*alpha, 2*alpha) = 4 * (-6) = -24
        # D = -(-24)/2 = 12
        assert 4 * (-6) == -24
        assert -(-24) // 2 == 12
        # c(12) = 4016
        assert KNOWN_C_TABLE[12] == 4016

    def test_d3_three_layers(self):
        """D = 3 triple pole gives 3 layers of Serre data."""
        result = d3_serre_relation()
        assert 'layer_3' in result['layers']
        assert 'layer_2' in result['layers']
        assert 'layer_1' in result['layers']
        assert result['layers']['layer_3']['pole_order'] == 3
        assert result['layers']['layer_2']['pole_order'] == 2
        assert result['layers']['layer_1']['pole_order'] == 1

    def test_d3_layer3_output_d12(self):
        """Most singular term (z-w)^{-3} outputs at D = 12."""
        result = d3_serre_relation()
        assert result['layers']['layer_3']['output_discriminant'] == 12
        assert result['layers']['layer_3']['output_c_value'] == 4016

    def test_d3_status_conjectural(self):
        """D = 3 Serre status is CONJECTURAL."""
        result = d3_serre_relation()
        assert result['status'] == 'CONJECTURAL'


# ===========================================================================
# SECTION 8: D = 0 LIGHTLIKE SECTOR
# ===========================================================================

class TestD0LightlikeSerre:
    """D = 0 lightlike sector: 10 generators, marginal self-OPE."""

    def test_d0_multiplicity_10(self):
        """D = 0 has 10 generators."""
        result = d0_lightlike_serre()
        assert result['multiplicity'] == 10

    def test_d0_bosonic(self):
        """D = 0 generators are bosonic (c(0) = 10 > 0)."""
        result = d0_lightlike_serre()
        assert result['parity'] == 'bosonic'

    def test_d0_self_ope_marginal(self):
        """D = 0 self-OPE is marginal (P = 0)."""
        result = d0_lightlike_serre()
        assert result['self_ope_exponent'] == 0.0
        assert result['self_ope_type'] == 'marginal'

    def test_d0_kappa_bkm_5(self):
        """kappa_BKM = c(0)/2 = 5 (weight of Delta_5, AP113 compliant)."""
        result = d0_lightlike_serre()
        assert result['kappa_BKM'] == 5

    def test_d0_cross_ope_orthogonal_marginal(self):
        """Cross-OPE between orthogonal D=0 roots: P = 0 (marginal)."""
        result = d0_lightlike_serre()
        ip0 = result['cross_ope_by_inner_product'][0]
        assert ip0['singularity'] == 'marginal'
        assert ip0['cross_ope_exponent'] == 0.0

    def test_d0_cross_ope_positive_regular(self):
        """Cross-OPE with (alpha,beta) = 1: P = 2 (regular, commuting)."""
        result = d0_lightlike_serre()
        ip1 = result['cross_ope_by_inner_product'][1]
        assert ip1['singularity'] == 'regular'
        assert ip1['cross_ope_exponent'] == 2.0

    def test_d0_cross_ope_negative_pole(self):
        """Cross-OPE with (alpha,beta) = -1: P = -2 (double pole).

        Multi-path: (1) d0 result, (2) formula 2*(-1) + 0*0 = -2.
        """
        result = d0_lightlike_serre()
        ipm1 = result['cross_ope_by_inner_product'][-1]
        assert ipm1['singularity'] == 'pole'
        assert ipm1['cross_ope_exponent'] == -2.0
        assert ipm1['pole_order'] == 2
        # Cross-check: formula
        assert 2 * (-1) + 0 * 0 == -2

    def test_d0_status_conjectural(self):
        """Status is CONJECTURAL."""
        result = d0_lightlike_serre()
        assert result['status'] == 'CONJECTURAL'


# ===========================================================================
# SECTION 9: COMPLETE SUMMARY AND CROSS-ENGINE VERIFICATION
# ===========================================================================

class TestDeformedSerreSummary:
    """Complete summary and cross-engine verification."""

    def test_summary_has_all_answers(self):
        """Summary contains answers to all 7 questions."""
        summary = deformed_serre_summary(D_max=8)
        answers = summary['answers']
        assert 'Q1_D_minus1_self_OPE' in answers
        assert 'Q2_D0_ten_currents' in answers
        assert 'Q3_D3_first_spacelike' in answers
        assert 'Q4_D1_discriminant_validity' in answers
        assert 'Q5_imaginary_real_adjoint' in answers
        assert 'Q6_finiteness' in answers
        assert 'Q7_commutativity_breaking' in answers

    def test_key_formula(self):
        """Key formula is P_self(D, 1) = D * (D - 4)."""
        summary = deformed_serre_summary(D_max=8)
        assert 'D * (D - 4)' in summary['key_formula']

    def test_q1_d_minus1_exponent(self):
        """Q1: D = -1 exponent is 5 (regular)."""
        summary = deformed_serre_summary(D_max=8)
        q1 = summary['answers']['Q1_D_minus1_self_OPE']
        assert q1['exponent'] == 5.0

    def test_q2_d0_self_exponent(self):
        """Q2: D = 0 self-exponent is 0 (marginal)."""
        summary = deformed_serre_summary(D_max=8)
        q2 = summary['answers']['Q2_D0_ten_currents']
        assert q2['self_exponent'] == 0.0

    def test_q3_d3_exponent(self):
        """Q3: D = 3 exponent is -3 (triple pole)."""
        summary = deformed_serre_summary(D_max=8)
        q3 = summary['answers']['Q3_D3_first_spacelike']
        assert q3['exponent'] == -3.0

    def test_cross_engine_c_table(self):
        """Cross-check: KNOWN_C_TABLE matches bkm_yangian_generators.

        Multi-path: (1) our table, (2) bkm_yangian_generators.KNOWN_MULTIPLICITIES.
        """
        bkm_yang = _import_bkm_yangian()
        for D, c_val in KNOWN_C_TABLE.items():
            if D in bkm_yang.KNOWN_MULTIPLICITIES:
                assert abs(c_val) == abs(bkm_yang.KNOWN_MULTIPLICITIES[D]), (
                    f"D={D}: our |c|={abs(c_val)}, "
                    f"bkm_yang |c|={abs(bkm_yang.KNOWN_MULTIPLICITIES[D])}"
                )

    def test_cross_engine_borcherds_vertex_gram(self):
        """Cross-check: GRAM_MATRIX matches borcherds_vertex_yangian."""
        bv = _import_borcherds_vertex()
        assert GRAM_MATRIX == bv.GRAM_MATRIX

    def test_cross_engine_c_table_live(self):
        """Cross-check: KNOWN_C_TABLE matches live phi01 computation.

        Multi-path: (1) our table, (2) k3_elliptic_genus_bkm_bar.c_table_from_phi01.
        """
        bkm_bar = _import_bkm_bar()
        live = bkm_bar.c_table_from_phi01(20)
        for D, c_val in KNOWN_C_TABLE.items():
            assert c_val == live[D], (
                f"D={D}: our c={c_val}, live c={live[D]}"
            )

    def test_status_conjectural(self):
        """Overall status is CONJECTURAL (AP-CY14)."""
        summary = deformed_serre_summary(D_max=8)
        assert summary['status'] == 'CONJECTURAL'
