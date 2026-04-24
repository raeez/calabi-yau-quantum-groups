r"""Tests for bkm_d3_explicit_generators.py: the 64 BKM Serre generators at D=3.

STATUS: ALL results are CONJECTURAL (AP-CY14).
Tests verify INTERNAL CONSISTENCY of the D=3 explicit construction,
not existence of a Yangian deformation of g_hat_{Delta_5}.

WHAT IS TESTED
==============

Section 1: Lattice vectors at D=3 (10 tests)
Section 2: Root space structure (12 tests)
Section 3: Inner product distribution and root addition (14 tests)
Section 4: Vertex operator construction (10 tests)
Section 5: Anticommutator algebra (12 tests)
Section 6: Serre kernel (10 tests)
Section 7: D=3/D=4 interaction (8 tests)
Section 8: Independence analysis (8 tests)
Section 9: Cross-engine verification (10 tests)
Section 10: Complete summary (6 tests)

Total: 100 tests

CRITICAL AP COMPLIANCE
======================

AP-CY7:  Vertex algebra methods, NOT CoHA.
AP-CY14: All Yangian results are CONJECTURAL.
AP-CY9:  Discriminant constraint: D = 0 or 3 mod 4 for index 1.
AP-CY20: Omega-background intermediary stated explicitly.
AP113:   kappa subscripts: kappa_BKM = 5, never bare kappa.
AP-CY24: All numerical values verified against function output.

Manuscript references:
    k3e_bkm_chapter.tex conj:deformed-serre-structure
    k3e_bkm_chapter.tex subsubsec:k3e-deformed-serre-ope
"""

import math
import pytest

from compute.lib.bkm_d3_explicit_generators import (
    # Constants
    STATUS,
    D3_DISCRIMINANT,
    D3_C_VALUE,
    D3_MULTIPLICITY,
    D3_PARITY,
    D3_NORM_SQ,
    D3_MUKAI_NORM_SQ,
    D3_SELF_OPE_EXPONENT,
    D3_POLE_ORDER,
    D4_DISCRIMINANT,
    D4_C_VALUE,
    D4_MULTIPLICITY,
    D4_PARITY,
    D4_NORM_SQ,
    D4_SELF_OPE_EXPONENT,
    D3_D4_CROSS_OPE,
    VALID_DISCRIMINANT_RESIDUES,
    GRAM_MATRIX,
    KNOWN_C_TABLE,
    # Lattice vectors
    lattice_vectors_at_d3,
    lattice_vector_count_at_d3,
    primitive_lattice_vector_d3,
    # Root space
    D3RootSpace,
    d3_root_space,
    verify_d3_root_space_consistency,
    # Inner products
    root_addition_table_d3,
    valid_inner_products_d3,
    invalid_inner_products_d3,
    # Generators
    D3Generator,
    d3_generators,
    # Anticommutator
    AnticommutatorLayer,
    anticommutator_layers,
    anticommutator_matrix_structure,
    # Serre kernel
    D3SerreKernel,
    d3_serre_kernel,
    # D=3/D=4
    d3_d4_interaction,
    D4RootSpace,
    d4_root_space,
    d4_interaction_with_d3,
    # Independence
    independence_analysis,
    # Summary
    d3_explicit_summary,
)


# ---------------------------------------------------------------------------
# Helper for cross-engine imports
# ---------------------------------------------------------------------------

def _import_bkm_bar():
    """Import k3_elliptic_genus_bkm_bar."""
    try:
        from compute.lib import k3_elliptic_genus_bkm_bar
        return k3_elliptic_genus_bkm_bar
    except (ImportError, ModuleNotFoundError):
        import importlib, os, sys
        _lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'lib')
        if _lib_dir not in sys.path:
            sys.path.insert(0, _lib_dir)
        return importlib.import_module('k3_elliptic_genus_bkm_bar')


def _import_deformed_serre():
    """Import bkm_deformed_serre."""
    try:
        from compute.lib import bkm_deformed_serre
        return bkm_deformed_serre
    except (ImportError, ModuleNotFoundError):
        import importlib, os, sys
        _lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'lib')
        if _lib_dir not in sys.path:
            sys.path.insert(0, _lib_dir)
        return importlib.import_module('bkm_deformed_serre')


def _import_serre_higher_order():
    """Import bkm_serre_higher_order."""
    try:
        from compute.lib import bkm_serre_higher_order
        return bkm_serre_higher_order
    except (ImportError, ModuleNotFoundError):
        import importlib, os, sys
        _lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'lib')
        if _lib_dir not in sys.path:
            sys.path.insert(0, _lib_dir)
        return importlib.import_module('bkm_serre_higher_order')


# ===========================================================================
# Section 1: Lattice vectors at D=3 (10 tests)
# ===========================================================================

class TestLatticeVectorsD3:
    """Tests for lattice vector enumeration at discriminant D=3."""

    def test_primitive_vector(self):
        """The primitive lattice vector at D=3 is (1, 1)."""
        n, l = primitive_lattice_vector_d3()
        assert n == 1
        assert l == 1
        assert 4 * n - l * l == 3

    def test_primitive_vector_discriminant(self):
        """The primitive vector has discriminant 3."""
        n, l = primitive_lattice_vector_d3()
        assert 4 * n - l * l == D3_DISCRIMINANT

    def test_all_vectors_satisfy_discriminant(self):
        """All enumerated vectors satisfy D = 4n - l^2 = 3."""
        vecs = lattice_vectors_at_d3(20)
        for n, l in vecs:
            assert 4 * n - l * l == 3, f"({n}, {l}): 4*{n} - {l}^2 = {4*n - l*l} != 3"

    def test_vectors_include_primitive(self):
        """The enumeration includes (1, 1) and (1, -1)."""
        vecs = lattice_vectors_at_d3(5)
        assert (1, 1) in vecs
        assert (1, -1) in vecs

    def test_vectors_include_l3(self):
        """(3, 3) and (3, -3) are also valid vectors at D=3."""
        vecs = lattice_vectors_at_d3(5)
        assert (3, 3) in vecs
        assert (3, -3) in vecs
        assert 4 * 3 - 3 * 3 == 3

    def test_only_odd_l(self):
        """At D=3, only odd l values contribute (l^2 = 1 mod 4)."""
        vecs = lattice_vectors_at_d3(20)
        for n, l in vecs:
            assert l % 2 != 0, f"Even l = {l} found at D=3"

    def test_count_grows(self):
        """The count of lattice vectors grows with max_l."""
        c5 = lattice_vector_count_at_d3(5)
        c10 = lattice_vector_count_at_d3(10)
        c20 = lattice_vector_count_at_d3(20)
        assert c10 > c5
        assert c20 > c10

    def test_count_exceeds_64(self):
        """Lattice vector count exceeds 64 exactly after the odd-l threshold."""
        assert lattice_vector_count_at_d3(50) == 50

        count = lattice_vector_count_at_d3(65)
        assert count > 64, (
            f"Expected > 64 lattice vectors at large max_l, got {count}"
        )

    def test_n_nonnegative(self):
        """All enumerated vectors have n >= 0."""
        vecs = lattice_vectors_at_d3(20)
        for n, l in vecs:
            assert n >= 0

    def test_symmetric_in_l(self):
        """Vectors come in (n, l) and (n, -l) pairs."""
        vecs = lattice_vectors_at_d3(20)
        for n, l in vecs:
            if l != 0:
                assert (n, -l) in vecs, f"Missing partner (n, -l) for ({n}, {l})"


# ===========================================================================
# Section 2: Root space structure (12 tests)
# ===========================================================================

class TestD3RootSpace:
    """Tests for the D=3 root space."""

    def test_dimension(self):
        """D=3 root space has dimension 64."""
        rs = d3_root_space()
        assert rs.dimension == 64

    def test_c_value(self):
        """c(3) = -64."""
        rs = d3_root_space()
        assert rs.c_value == -64

    def test_fermionic(self):
        """D=3 generators are fermionic (c < 0)."""
        rs = d3_root_space()
        assert rs.parity == 'fermionic'
        assert rs.c_value < 0

    def test_norm_squared(self):
        """Mukai norm^2 = -2D = -6."""
        rs = d3_root_space()
        assert rs.norm_sq == -6
        assert rs.norm_sq == -2 * rs.discriminant

    def test_conformal_weight(self):
        """Undeformed conformal weight is D+1 = 4."""
        rs = d3_root_space()
        assert rs.conformal_weight == 4

    def test_deformed_weight(self):
        """Deformed weight at eps=1 is 1 (universal weight collapse)."""
        rs = d3_root_space()
        assert rs.deformed_weight == 1

    def test_pole_order(self):
        """Triple pole: |P(3,1)| = 3."""
        rs = d3_root_space()
        assert rs.pole_order == 3

    def test_self_ope_exponent(self):
        """P(3,1) = 3*(3-4) = -3."""
        rs = d3_root_space()
        assert rs.self_ope_exponent == -3

    def test_s3_decomposition_sums(self):
        """S_3 decomposition sums to 64."""
        rs = d3_root_space()
        s3 = rs.s3_decomposition
        total = s3['trivial'] + s3['sign'] + 2 * s3['standard']
        assert total == 64

    def test_s3_trivial_count(self):
        """10 S_3-trivial generators."""
        rs = d3_root_space()
        assert rs.s3_decomposition['trivial'] == 10

    def test_s3_sign_count(self):
        """10 S_3-sign generators."""
        rs = d3_root_space()
        assert rs.s3_decomposition['sign'] == 10

    def test_consistency_verification(self):
        """Cross-engine consistency check passes."""
        checks = verify_d3_root_space_consistency()
        assert checks['all_pass'], f"Consistency check failed: {checks}"


# ===========================================================================
# Section 3: Inner product distribution and root addition (14 tests)
# ===========================================================================

class TestRootAddition:
    """Tests for inner product distribution and root addition table."""

    def test_root_addition_table_completeness(self):
        """Table covers inner products from -6 to 6 (Cauchy-Schwarz bound)."""
        table = root_addition_table_d3()
        for ip in range(-6, 7):
            assert ip in table

    def test_self_inner_product(self):
        """Self inner product ip=-6 gives D(sum) = 12."""
        table = root_addition_table_d3()
        assert table[-6]['output_discriminant'] == 12
        assert table[-6]['output_valid']

    def test_orthogonal_invalid(self):
        """Orthogonal roots (ip=0) give D(sum) = 6 which is INVALID."""
        table = root_addition_table_d3()
        assert table[0]['output_discriminant'] == 6
        assert not table[0]['output_valid']

    def test_ip_minus1_gives_d7(self):
        """ip=-1 gives D(sum) = 7 (fermionic, c(7) = -513)."""
        table = root_addition_table_d3()
        assert table[-1]['output_discriminant'] == 7
        assert table[-1]['output_valid']
        assert table[-1]['output_c_value'] == -513

    def test_ip_minus2_gives_d8(self):
        """ip=-2 gives D(sum) = 8 (bosonic, c(8) = 808)."""
        table = root_addition_table_d3()
        assert table[-2]['output_discriminant'] == 8
        assert table[-2]['output_valid']
        assert table[-2]['output_c_value'] == 808

    def test_ip_plus2_gives_d4(self):
        """ip=2 gives D(sum) = 4 (bosonic, c(4) = 108)."""
        table = root_addition_table_d3()
        assert table[2]['output_discriminant'] == 4
        assert table[2]['output_valid']
        assert table[2]['output_c_value'] == 108

    def test_ip_plus3_gives_d3(self):
        """ip=3 gives D(sum) = 3 (self-referential, fermionic)."""
        table = root_addition_table_d3()
        assert table[3]['output_discriminant'] == 3
        assert table[3]['output_valid']
        assert table[3]['output_c_value'] == -64

    def test_ip_plus6_gives_d0(self):
        """ip=6 (anti-parallel) gives D(sum) = 0 (lightlike sector)."""
        table = root_addition_table_d3()
        assert table[6]['output_discriminant'] == 0
        assert table[6]['output_valid']
        assert table[6]['output_c_value'] == 10

    def test_valid_inner_products(self):
        """Valid inner products produce valid output discriminants."""
        valid = valid_inner_products_d3()
        table = root_addition_table_d3()
        for ip in valid:
            assert table[ip]['output_valid']
            d_out = table[ip]['output_discriminant']
            assert d_out % 4 in VALID_DISCRIMINANT_RESIDUES or d_out < 0

    def test_invalid_inner_products(self):
        """Invalid inner products produce invalid output discriminants."""
        invalid = invalid_inner_products_d3()
        table = root_addition_table_d3()
        for ip in invalid:
            assert not table[ip]['output_valid']

    def test_valid_and_invalid_partition(self):
        """Valid and invalid inner products partition -6..6."""
        valid = set(valid_inner_products_d3())
        invalid = set(invalid_inner_products_d3())
        all_ips = set(range(-6, 7))
        assert valid | invalid == all_ips
        assert valid & invalid == set()

    def test_d6_not_valid_discriminant(self):
        """D=6 is not a valid discriminant (6 mod 4 = 2)."""
        assert 6 % 4 == 2
        assert 6 % 4 not in VALID_DISCRIMINANT_RESIDUES

    def test_output_formula(self):
        """D(sum) = 6 - ip for all inner products."""
        table = root_addition_table_d3()
        for ip in range(-6, 7):
            assert table[ip]['output_discriminant'] == 6 - ip

    def test_cauchy_schwarz_bound(self):
        """Inner product bounded by Cauchy-Schwarz: |ip| <= sqrt(6*6) = 6."""
        # For roots with norm^2 = -6 (Lorentzian), the bound is |(a,b)| <= 6
        # with equality iff a || b.
        valid = valid_inner_products_d3()
        invalid = invalid_inner_products_d3()
        all_ips = valid + invalid
        assert all(abs(ip) <= 6 for ip in all_ips)


# ===========================================================================
# Section 4: Vertex operator construction (10 tests)
# ===========================================================================

class TestD3Generators:
    """Tests for the explicit construction of 64 generators."""

    def test_generator_count(self):
        """Exactly 64 generators are constructed."""
        gens = d3_generators()
        assert len(gens) == 64

    def test_all_norm_minus6(self):
        """All generators have norm^2 = -6."""
        gens = d3_generators()
        assert all(g.norm_sq == -6 for g in gens)

    def test_indices_1_to_64(self):
        """Generator indices run from 1 to 64."""
        gens = d3_generators()
        indices = [g.index for g in gens]
        assert sorted(indices) == list(range(1, 65))

    def test_s3_trivial_generators(self):
        """10 generators are S_3-trivial."""
        gens = d3_generators()
        trivial = [g for g in gens if g.s3_representation == 'trivial']
        assert len(trivial) == 10

    def test_s3_sign_generators(self):
        """10 generators are S_3-sign."""
        gens = d3_generators()
        sign = [g for g in gens if g.s3_representation == 'sign']
        assert len(sign) == 10

    def test_s3_standard_generators(self):
        """44 generators are S_3-standard (22 copies * 2)."""
        gens = d3_generators()
        standard = [g for g in gens if g.s3_representation == 'standard']
        assert len(standard) == 44

    def test_s3_decomposition_matches_root_space(self):
        """S_3 decomposition of generators matches root space data."""
        gens = d3_generators()
        rs = d3_root_space()
        s3 = rs.s3_decomposition

        trivial = sum(1 for g in gens if g.s3_representation == 'trivial')
        sign = sum(1 for g in gens if g.s3_representation == 'sign')
        standard = sum(1 for g in gens if g.s3_representation == 'standard')

        assert trivial == s3['trivial']
        assert sign == s3['sign']
        assert standard == 2 * s3['standard']  # 2 basis vectors per copy

    def test_cartan_weights_are_tuples(self):
        """Cartan weights are 3-tuples."""
        gens = d3_generators()
        for g in gens:
            assert len(g.cartan_weights) == 3

    def test_generator_named_tuple(self):
        """Each generator is a D3Generator namedtuple."""
        gens = d3_generators()
        assert all(isinstance(g, D3Generator) for g in gens)

    def test_representations_are_valid(self):
        """All representations are one of the 3 S_3 irreps."""
        gens = d3_generators()
        valid_reps = {'trivial', 'sign', 'standard'}
        assert all(g.s3_representation in valid_reps for g in gens)


# ===========================================================================
# Section 5: Anticommutator algebra (12 tests)
# ===========================================================================

class TestAnticommutator:
    """Tests for the anticommutator algebra at D=3."""

    def test_three_layers(self):
        """Anticommutator has exactly 3 layers (triple pole)."""
        layers = anticommutator_layers()
        assert len(layers) == 3

    def test_pole_orders(self):
        """Pole orders are 3, 2, 1."""
        layers = anticommutator_layers()
        assert [l.pole_order for l in layers] == [3, 2, 1]

    def test_independent_components(self):
        """Each layer has 2080 = 64*65/2 independent components."""
        layers = anticommutator_layers()
        expected = 64 * 65 // 2
        assert all(l.independent_components == expected for l in layers)

    def test_layer3_output_at_d12(self):
        """Layer 3 (most singular) has output at D=12."""
        layers = anticommutator_layers()
        assert layers[0].output_discriminant == 12

    def test_matrix_symmetric(self):
        """The anticommutator matrix is symmetric (fermionic {e_a, e_b} = {e_b, e_a})."""
        matrix = anticommutator_matrix_structure()
        assert matrix['symmetric']

    def test_matrix_size(self):
        """Matrix is 64 x 64."""
        matrix = anticommutator_matrix_structure()
        assert matrix['matrix_size'] == '64 x 64'

    def test_total_serre_data(self):
        """Total Serre data: 3 * 2080 = 6240."""
        matrix = anticommutator_matrix_structure()
        assert matrix['total_serre_data'] == 3 * 64 * 65 // 2

    def test_valid_ips_in_matrix(self):
        """Matrix reports valid inner products."""
        matrix = anticommutator_matrix_structure()
        assert len(matrix['valid_inner_products']) > 0

    def test_invalid_ips_in_matrix(self):
        """Matrix reports invalid inner products (Serre vanishing)."""
        matrix = anticommutator_matrix_structure()
        assert len(matrix['invalid_inner_products']) > 0

    def test_rank_bound(self):
        """Rank bound is at most min(2080, 4016) = 2080."""
        matrix = anticommutator_matrix_structure()
        assert '2080' in matrix['rank_bound']

    def test_layers_are_named_tuples(self):
        """Each layer is an AnticommutatorLayer namedtuple."""
        layers = anticommutator_layers()
        assert all(isinstance(l, AnticommutatorLayer) for l in layers)

    def test_total_matrix_entries(self):
        """Total matrix entries: 64^2 = 4096."""
        matrix = anticommutator_matrix_structure()
        assert matrix['total_entries'] == 64 * 64


# ===========================================================================
# Section 6: Serre kernel (10 tests)
# ===========================================================================

class TestSerreKernel:
    """Tests for the D=3 Serre kernel."""

    def test_total_pairs(self):
        """2080 independent anticommutator pairs."""
        kernel = d3_serre_kernel()
        assert kernel.total_pairs == 64 * 65 // 2

    def test_vanishing_ips_nonempty(self):
        """Some inner products give vanishing anticommutators."""
        kernel = d3_serre_kernel()
        assert len(kernel.vanishing_pairs_by_ip) > 0

    def test_nonvanishing_ips_nonempty(self):
        """Some inner products give nonvanishing anticommutators."""
        kernel = d3_serre_kernel()
        assert len(kernel.nonvanishing_inner_products) > 0

    def test_self_ip_nonvanishing(self):
        """Self inner product ip=-6 is nonvanishing."""
        kernel = d3_serre_kernel()
        assert -6 in kernel.nonvanishing_inner_products

    def test_orthogonal_vanishing(self):
        """Orthogonal roots (ip=0) give vanishing anticommutator."""
        kernel = d3_serre_kernel()
        assert 0 in kernel.vanishing_pairs_by_ip

    def test_serre_relations_nonempty(self):
        """Serre relations are described."""
        kernel = d3_serre_kernel()
        assert len(kernel.serre_relations) >= 2

    def test_jacobi_identity_present(self):
        """Jacobi identity for fermionic generators is described."""
        kernel = d3_serre_kernel()
        assert 'graded Jacobi' in kernel.jacobi_identity.lower() or \
               'Jacobi' in kernel.jacobi_identity

    def test_jacobi_count(self):
        """C(64, 3) = 41664 Jacobi relations."""
        kernel = d3_serre_kernel()
        expected = 64 * 63 * 62 // 6
        assert str(expected) in kernel.jacobi_identity

    def test_kernel_is_named_tuple(self):
        """Kernel is a D3SerreKernel namedtuple."""
        kernel = d3_serre_kernel()
        assert isinstance(kernel, D3SerreKernel)

    def test_status_conjectural(self):
        """Status is CONJECTURAL."""
        kernel = d3_serre_kernel()
        assert kernel.status == 'CONJECTURAL'


# ===========================================================================
# Section 7: D=3/D=4 interaction (8 tests)
# ===========================================================================

class TestD3D4Interaction:
    """Tests for the interaction between D=3 and D=4 sectors."""

    def test_cross_ope_exponent(self):
        """P_cross(3, 4, 1) = 12."""
        result = d3_d4_interaction()
        assert result['cross_ope_exponent'] == 12

    def test_decoupled(self):
        """D=3 and D=4 are decoupled (regular cross-OPE)."""
        result = d3_d4_interaction()
        assert result['decoupled']

    def test_d4_root_space_dimension(self):
        """D=4 root space has dimension 108."""
        rs = d4_root_space()
        assert rs.dimension == 108

    def test_d4_bosonic(self):
        """D=4 generators are bosonic (c > 0)."""
        rs = d4_root_space()
        assert rs.parity == 'bosonic'
        assert rs.c_value > 0

    def test_d4_marginal(self):
        """D=4 self-OPE is marginal (P=0)."""
        rs = d4_root_space()
        assert rs.self_ope_exponent == 0

    def test_d4_s3_decomposition_sums(self):
        """D=4 S_3 decomposition sums to 108."""
        rs = d4_root_space()
        s3 = rs.s3_decomposition
        total = s3['trivial'] + s3['sign'] + 2 * s3['standard']
        assert total == 108

    def test_combined_dimension(self):
        """D=3 + D=4 = 64 + 108 = 172."""
        result = d4_interaction_with_d3()
        assert result['combined_dimension'] == 172

    def test_full_kernel_size(self):
        """Full Serre kernel: 10 + 64 + 108 = 182."""
        assert KNOWN_C_TABLE[0] + D3_MULTIPLICITY + D4_MULTIPLICITY == 182


# ===========================================================================
# Section 8: Independence analysis (8 tests)
# ===========================================================================

class TestIndependence:
    """Tests for independence analysis of the 64 generators."""

    def test_generators_independent(self):
        """64 generators are linearly independent."""
        result = independence_analysis()
        assert result['generators_independent']

    def test_generator_count(self):
        """Generator count is 64."""
        result = independence_analysis()
        assert result['generator_count'] == 64

    def test_yangian_rank(self):
        """Yangian rank at D=3 is 64."""
        result = independence_analysis()
        assert result['yangian_rank']['rank'] == 64

    def test_product_constraints_total(self):
        """2080 independent product entries."""
        result = independence_analysis()
        assert result['product_constraints']['total_independent_products'] == 2080

    def test_jacobi_count(self):
        """41664 Jacobi relations."""
        result = independence_analysis()
        expected = 64 * 63 * 62 // 6
        assert result['product_constraints']['jacobi_relations'] == expected

    def test_no_serre_reduction(self):
        """No Serre relation reduces the generator count."""
        result = independence_analysis()
        assert 'no Serre relation reduces' in result['no_serre_reduction'].lower() or \
               'No Serre relation reduces' in result['no_serre_reduction']

    def test_status_conjectural(self):
        """Status is CONJECTURAL."""
        result = independence_analysis()
        assert result['status'] == 'CONJECTURAL'

    def test_discriminant_vanishing_count(self):
        """Number of invalid inner products is consistent."""
        result = independence_analysis()
        invalid = invalid_inner_products_d3()
        assert result['product_constraints']['discriminant_vanishing_ips'] == len(invalid)


# ===========================================================================
# Section 9: Cross-engine verification (10 tests)
# ===========================================================================

class TestCrossEngine:
    """Cross-engine consistency verification against parent engines."""

    def test_c3_matches_bkm_bar(self):
        """c(3) matches k3_elliptic_genus_bkm_bar.py."""
        bkm_bar = _import_bkm_bar()
        table = bkm_bar.c_table_from_phi01(30)
        assert table[3] == D3_C_VALUE

    def test_c4_matches_bkm_bar(self):
        """c(4) matches k3_elliptic_genus_bkm_bar.py."""
        bkm_bar = _import_bkm_bar()
        table = bkm_bar.c_table_from_phi01(30)
        assert table[4] == D4_C_VALUE

    def test_ope_exponent_matches_deformed_serre(self):
        """P(3,1) matches bkm_deformed_serre.py."""
        deformed = _import_deformed_serre()
        P = deformed.deformed_ope_exponent_self(3, 1.0)
        assert abs(P - D3_SELF_OPE_EXPONENT) < 1e-10

    def test_d4_ope_matches_deformed_serre(self):
        """P(4,1) matches bkm_deformed_serre.py."""
        deformed = _import_deformed_serre()
        P = deformed.deformed_ope_exponent_self(4, 1.0)
        assert abs(P - D4_SELF_OPE_EXPONENT) < 1e-10

    def test_cross_ope_matches_deformed_serre(self):
        """P_cross(3,4,1) matches bkm_deformed_serre.py."""
        deformed = _import_deformed_serre()
        P = deformed.deformed_ope_exponent_cross(3, 4, 1.0)
        assert abs(P - D3_D4_CROSS_OPE) < 1e-10

    def test_serre_kernel_size_matches(self):
        """Serre kernel size 182 matches bkm_deformed_serre.py."""
        deformed = _import_deformed_serre()
        assert deformed.SERRE_KERNEL_SIZE == 182

    def test_p2_zero_from_higher_order(self):
        """P_2(3) = 0 from bkm_serre_higher_order.py (EXACT formula)."""
        higher = _import_serre_higher_order()
        from fractions import Fraction
        assert higher.ope_exponent_order2(3) == Fraction(0, 1)

    def test_exact_exponent_matches(self):
        """Exact OPE exponent matches from bkm_serre_higher_order.py."""
        higher = _import_serre_higher_order()
        P_exact = higher.ope_exponent_exact(3, 1.0)
        assert abs(P_exact - D3_SELF_OPE_EXPONENT) < 1e-10

    def test_gram_matrix_matches(self):
        """Gram matrix matches bkm_deformed_serre.py."""
        deformed = _import_deformed_serre()
        assert GRAM_MATRIX == deformed.GRAM_MATRIX

    def test_c_table_consistency(self):
        """KNOWN_C_TABLE is consistent with bkm_deformed_serre.py."""
        deformed = _import_deformed_serre()
        for D in KNOWN_C_TABLE:
            if D in deformed.KNOWN_C_TABLE:
                assert KNOWN_C_TABLE[D] == deformed.KNOWN_C_TABLE[D], \
                    f"Mismatch at D={D}: {KNOWN_C_TABLE[D]} vs {deformed.KNOWN_C_TABLE[D]}"


# ===========================================================================
# Section 10: Complete summary (6 tests)
# ===========================================================================

class TestCompleteSummary:
    """Tests for the complete D=3 explicit summary."""

    def test_summary_has_key_results(self):
        """Summary contains all 6 key results."""
        summary = d3_explicit_summary()
        assert len(summary['key_results']) == 6

    def test_summary_generator_count(self):
        """Summary reports 64 generators."""
        summary = d3_explicit_summary()
        assert summary['generators']['count'] == 64

    def test_summary_s3_decomposition(self):
        """Summary S_3 decomposition sums to 64."""
        summary = d3_explicit_summary()
        g = summary['generators']
        assert g['s3_trivial'] + g['s3_sign'] + g['s3_standard'] == 64

    def test_summary_anticommutator_layers(self):
        """Summary contains 3 anticommutator layers."""
        summary = d3_explicit_summary()
        assert len(summary['anticommutator']['layers']) == 3

    def test_summary_serre_kernel(self):
        """Summary reports Serre kernel data."""
        summary = d3_explicit_summary()
        assert summary['serre_kernel']['total_pairs'] == 2080

    def test_summary_status(self):
        """Summary status is CONJECTURAL."""
        summary = d3_explicit_summary()
        assert summary['status'] == 'CONJECTURAL'
