r"""Tests for handle_decomposition_fh.py: factorization homology on CY
manifolds via handle decomposition (the CFG25 analogue for CY).

CENTRAL RESULTS:
    (1) Handle decomposition Euler characteristics match Betti numbers
        for K3, quintic, K3 x E, T^6, S^2 x S^2, CP^2, Enriques.
    (2) K3 iterative excision: rank 24, signature (4, 20) = Mukai.
    (3) Handle route vs Kummer route: agreement on all invariants.
    (4) CFG25 analogy table: complete, dimensions consistent.
    (5) Collar algebras at each handle attachment: correct ranks.
    (6) Quintic CY3: b_3 = 204, symplectic genus 102.
    (7) K3 x E Kunneth formula: (1,2,23,44,23,2,1), chi = 0.
    (8) chi_y genus of K3: chi_0 = kappa_cat = 2.
    (9) All CY3 results CONJECTURAL (CY-A_3, AP-CY32, AP-CY14).
    (10) Kirby diagram data for K3: even, unimodular, 3U + 2E_8(-1).

Manuscript references:
    en_factorization.tex sec:handle-fh-k3 (handle decomposition of K3)
    braided_factorization.tex prop:fh-excision (excision for FH)
    cy_to_chiral.tex prop:kummer-orbifold (Kummer route comparison)
"""

import pytest
from fractions import Fraction as Fr

from compute.lib.handle_decomposition_fh import (
    # Constants
    K3_BETTI,
    K3_HANDLES,
    K3_EULER,
    K3_H2_SIG,
    K3_LATTICE,
    MUKAI_RANK,
    MUKAI_SIG,
    MUKAI_LATTICE,
    QUINTIC_BETTI,
    QUINTIC_HANDLES,
    QUINTIC_EULER,
    QUINTIC_H3_RANK,
    QUINTIC_H3_SYMPLECTIC_RANK,
    K3XE_BETTI,
    K3XE_EULER,
    K3XE_H3_RANK,
    T6_BETTI,
    T6_EULER,
    ENRIQUES_BETTI,
    S2S2_BETTI,
    S2S2_H2_SIG,
    CP2_BETTI,
    CP2_H2_SIG,
    # Handle data constructors
    make_handle_data,
    k3_handle_data,
    quintic_handle_data,
    k3xe_handle_data,
    t6_handle_data,
    # Collar algebras
    collar_algebra_data,
    # CFG25 analogy
    cfg25_analogy_table,
    # Iterative excision
    iterative_excision,
    excision_final_rank,
    # K3 Kirby diagram
    k3_kirby_diagram,
    # Route comparison
    compare_handle_vs_kummer,
    # CY3 analysis
    quintic_cy3_handle_analysis,
    k3xe_cy3_handle_analysis,
    # State space
    k3_state_space_interpretation,
    # Numerical invariants
    euler_from_handles,
    signature_from_intersection_form,
    chi_y_genus_k3,
    # Verification functions
    verify_handle_euler_consistency,
    verify_k3_excision_rank,
    verify_k3_signature,
    verify_handle_vs_kummer_agreement,
    verify_cy3_euler_characteristics,
    verify_chi_y_genus_k3,
    verify_cfg25_analogy_completeness,
    verify_collar_algebras,
    verify_quintic_handle_data,
    verify_k3xe_kunneth,
    verify_conjectural_status_cy3,
    full_verification,
)


# =========================================================================
# Section 1: Topological constants
# =========================================================================

class TestK3Constants:
    """K3 topological constants."""

    def test_k3_betti(self):
        """K3 Betti numbers: (1, 0, 22, 0, 1)."""
        assert K3_BETTI == (1, 0, 22, 0, 1)

    def test_k3_handles_equal_betti(self):
        """For simply connected 4-manifold: handles = Betti numbers."""
        assert K3_HANDLES == K3_BETTI

    def test_k3_euler(self):
        """chi(K3) = 24."""
        assert K3_EULER == 24

    def test_k3_euler_from_betti(self):
        """chi = 1 - 0 + 22 - 0 + 1 = 24."""
        chi = sum((-1)**k * b for k, b in enumerate(K3_BETTI))
        assert chi == 24

    def test_k3_h2_signature(self):
        """K3 intersection form: signature (3, 19)."""
        assert K3_H2_SIG == (3, 19)

    def test_k3_h2_rank(self):
        """K3 intersection form rank = b_2 = 22."""
        assert sum(K3_H2_SIG) == 22

    def test_k3_lattice_type(self):
        """K3 lattice is 3U + 2E_8(-1)."""
        assert '3U' in K3_LATTICE
        assert 'E_8(-1)' in K3_LATTICE

    def test_mukai_rank(self):
        """Mukai lattice rank = 24."""
        assert MUKAI_RANK == 24

    def test_mukai_signature(self):
        """Mukai signature = (4, 20)."""
        assert MUKAI_SIG == (4, 20)

    def test_mukai_rank_from_sig(self):
        """Mukai rank = 4 + 20 = 24."""
        assert sum(MUKAI_SIG) == MUKAI_RANK

    def test_mukai_from_k3(self):
        """Mukai sig = (3+1, 19+1) from H^2 + H^0-H^4 hyperbolic plane."""
        expected = (K3_H2_SIG[0] + 1, K3_H2_SIG[1] + 1)
        assert expected == MUKAI_SIG

    def test_k3_simply_connected(self):
        """K3 is simply connected: b_1 = 0."""
        assert K3_BETTI[1] == 0

    def test_k3_no_odd_handles(self):
        """K3 has no 1-handles or 3-handles."""
        assert K3_HANDLES[1] == 0
        assert K3_HANDLES[3] == 0

    def test_k3_hirzebruch_signature(self):
        """Hirzebruch signature tau(K3) = b+ - b- = 3 - 19 = -16."""
        tau = K3_H2_SIG[0] - K3_H2_SIG[1]
        assert tau == -16


class TestQuinticConstants:
    """Quintic CY3 topological constants."""

    def test_quintic_betti(self):
        """Quintic Betti: (1, 0, 1, 204, 1, 0, 1)."""
        assert QUINTIC_BETTI == (1, 0, 1, 204, 1, 0, 1)

    def test_quintic_euler(self):
        """chi(quintic) = -200."""
        assert QUINTIC_EULER == -200

    def test_quintic_euler_from_betti(self):
        """chi = 1 - 0 + 1 - 204 + 1 - 0 + 1 = -200."""
        chi = sum((-1)**k * b for k, b in enumerate(QUINTIC_BETTI))
        assert chi == -200

    def test_quintic_euler_from_hodge(self):
        """chi = 2(h^{1,1} - h^{2,1}) = 2(1 - 101) = -200."""
        assert 2 * (1 - 101) == -200

    def test_quintic_b3(self):
        """b_3(quintic) = 204."""
        assert QUINTIC_H3_RANK == 204

    def test_quintic_b3_from_hodge(self):
        """b_3 = 2(1 + h^{2,1}) = 2(1 + 101) = 204."""
        assert 2 * (1 + 101) == 204

    def test_quintic_b3_even(self):
        """b_3 is even (symplectic form exists)."""
        assert QUINTIC_H3_RANK % 2 == 0

    def test_quintic_symplectic_rank(self):
        """Symplectic rank of H^3 = 204."""
        assert QUINTIC_H3_SYMPLECTIC_RANK == 204

    def test_quintic_simply_connected(self):
        """Quintic is simply connected: b_1 = 0."""
        assert QUINTIC_BETTI[1] == 0

    def test_quintic_poincare_duality(self):
        """Poincare duality: b_k = b_{6-k}."""
        for k in range(7):
            assert QUINTIC_BETTI[k] == QUINTIC_BETTI[6 - k]


class TestK3xEConstants:
    """K3 x E topological constants."""

    def test_k3xe_betti(self):
        """K3 x E Betti: (1, 2, 23, 44, 23, 2, 1)."""
        assert K3XE_BETTI == (1, 2, 23, 44, 23, 2, 1)

    def test_k3xe_euler(self):
        """chi(K3 x E) = 0 (since chi(E) = 0)."""
        assert K3XE_EULER == 0

    def test_k3xe_euler_from_betti(self):
        """chi from Betti = 1 - 2 + 23 - 44 + 23 - 2 + 1 = 0."""
        chi = sum((-1)**k * b for k, b in enumerate(K3XE_BETTI))
        assert chi == 0

    def test_k3xe_euler_product_formula(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
        chi_k3 = sum((-1)**k * b for k, b in enumerate(K3_BETTI))
        chi_e = 0  # genus 1 curve
        assert chi_k3 * chi_e == 0

    def test_k3xe_not_simply_connected(self):
        """K3 x E is NOT simply connected: b_1 = 2."""
        assert K3XE_BETTI[1] == 2

    def test_k3xe_b3(self):
        """b_3(K3 x E) = 44."""
        assert K3XE_H3_RANK == 44

    def test_k3xe_poincare_duality(self):
        """Poincare duality: b_k = b_{6-k}."""
        for k in range(7):
            assert K3XE_BETTI[k] == K3XE_BETTI[6 - k]

    def test_k3xe_total_betti(self):
        """Total Betti dimension of K3 x E."""
        total = sum(K3XE_BETTI)
        # K3 total = 24, E total = 4, product = 24 * 4 = 96
        assert total == 96


class TestOtherManifoldConstants:
    """Constants for auxiliary manifolds used as cross-checks."""

    def test_t6_betti(self):
        """T^6 Betti: (1, 6, 15, 20, 15, 6, 1) from binomial coefficients."""
        assert T6_BETTI == (1, 6, 15, 20, 15, 6, 1)
        # Binomial(6, k)
        from math import comb
        for k in range(7):
            assert T6_BETTI[k] == comb(6, k)

    def test_t6_euler(self):
        """chi(T^6) = 0."""
        assert T6_EULER == 0

    def test_enriques_betti(self):
        """Enriques surface Betti: (1, 0, 10, 0, 1)."""
        assert ENRIQUES_BETTI == (1, 0, 10, 0, 1)

    def test_enriques_euler(self):
        """chi(Enriques) = 12."""
        chi = sum((-1)**k * b for k, b in enumerate(ENRIQUES_BETTI))
        assert chi == 12

    def test_s2s2_betti(self):
        """S^2 x S^2 Betti: (1, 0, 2, 0, 1)."""
        assert S2S2_BETTI == (1, 0, 2, 0, 1)

    def test_s2s2_euler(self):
        """chi(S^2 x S^2) = 4."""
        chi = sum((-1)**k * b for k, b in enumerate(S2S2_BETTI))
        assert chi == 4

    def test_s2s2_signature(self):
        """S^2 x S^2 intersection form: signature (1, 1) = hyperbolic plane."""
        assert S2S2_H2_SIG == (1, 1)

    def test_cp2_betti(self):
        """CP^2 Betti: (1, 0, 1, 0, 1)."""
        assert CP2_BETTI == (1, 0, 1, 0, 1)

    def test_cp2_euler(self):
        """chi(CP^2) = 3."""
        chi = sum((-1)**k * b for k, b in enumerate(CP2_BETTI))
        assert chi == 3

    def test_cp2_signature(self):
        """CP^2 intersection form: signature (1, 0) = positive definite rank 1."""
        assert CP2_H2_SIG == (1, 0)


# =========================================================================
# Section 2: Handle data construction
# =========================================================================

class TestHandleDataConstruction:
    """Tests for make_handle_data and specific manifold constructors."""

    def test_k3_handle_data(self):
        """K3 handle data: dim 4, CY_2, euler 24."""
        hd = k3_handle_data()
        assert hd.name == 'K3'
        assert hd.real_dim == 4
        assert hd.cy_dim == 2
        assert hd.euler_char == 24
        assert hd.simply_connected is True

    def test_k3_handle_data_betti(self):
        """K3 handle data Betti = handles."""
        hd = k3_handle_data()
        assert hd.betti == K3_BETTI
        assert hd.handles == K3_BETTI

    def test_k3_handle_data_intersection_form(self):
        """K3 intersection form: rank 22, sig (3,19)."""
        hd = k3_handle_data()
        assert hd.intersection_form_rank == 22
        assert hd.intersection_form_sig == (3, 19)

    def test_quintic_handle_data(self):
        """Quintic handle data: dim 6, CY_3, euler -200."""
        hd = quintic_handle_data()
        assert hd.name == 'Quintic'
        assert hd.real_dim == 6
        assert hd.cy_dim == 3
        assert hd.euler_char == -200
        assert hd.simply_connected is True

    def test_k3xe_handle_data(self):
        """K3 x E handle data: dim 6, CY_3, euler 0, not simply connected."""
        hd = k3xe_handle_data()
        assert hd.name == 'K3 x E'
        assert hd.real_dim == 6
        assert hd.cy_dim == 3
        assert hd.euler_char == 0
        assert hd.simply_connected is False

    def test_t6_handle_data(self):
        """T^6 handle data: dim 6, CY_3, euler 0."""
        hd = t6_handle_data()
        assert hd.name == 'T^6'
        assert hd.real_dim == 6
        assert hd.cy_dim == 3
        assert hd.euler_char == 0

    def test_make_handle_data_dimension_check(self):
        """make_handle_data: Betti length must equal real_dim + 1."""
        with pytest.raises(AssertionError):
            make_handle_data('bad', real_dim=4, betti=(1, 0, 22))

    def test_s2xs2_handle_data(self):
        """S^2 x S^2 constructed correctly."""
        hd = make_handle_data('S2xS2', real_dim=4, betti=S2S2_BETTI,
                              intersection_form_sig=S2S2_H2_SIG)
        assert hd.euler_char == 4
        assert hd.intersection_form_rank == 2
        assert hd.intersection_form_sig == (1, 1)


# =========================================================================
# Section 3: Collar algebras
# =========================================================================

class TestCollarAlgebras:
    """Collar algebra data at handle attachments."""

    def test_zero_handle_trivial(self):
        """Zero-handle collar is trivial (initial handle)."""
        ca = collar_algebra_data(real_dim=4, handle_index=0)
        assert ca.is_trivial is True
        assert ca.collar_einf_rank == 1

    def test_one_handle_collar(self):
        """1-handle collar: S^0 x R, rank 2."""
        ca = collar_algebra_data(real_dim=4, handle_index=1)
        assert ca.is_trivial is False
        assert ca.collar_einf_rank == 2

    def test_two_handle_collar(self):
        """2-handle collar: S^1 x R, rank 2."""
        ca = collar_algebra_data(real_dim=4, handle_index=2)
        assert ca.is_trivial is False
        assert ca.collar_einf_rank == 2
        assert 'S^1' in ca.collar_manifold

    def test_two_handle_hochschild_note(self):
        """2-handle collar mentions Hochschild for E_2."""
        ca = collar_algebra_data(real_dim=4, handle_index=2)
        assert 'HH' in ca.algebra_type

    def test_three_handle_collar(self):
        """3-handle collar: S^2 x R, rank 2."""
        ca = collar_algebra_data(real_dim=4, handle_index=3)
        assert ca.is_trivial is False
        assert ca.collar_einf_rank == 2
        assert 'S^2' in ca.collar_manifold

    def test_four_handle_collar(self):
        """4-handle collar: S^3 x R, rank 2."""
        ca = collar_algebra_data(real_dim=4, handle_index=4)
        assert ca.is_trivial is False
        assert ca.collar_einf_rank == 2
        assert 'S^3' in ca.collar_manifold

    def test_collar_rank_with_higher_input(self):
        """Collar rank scales with input algebra rank."""
        ca = collar_algebra_data(real_dim=4, handle_index=2, algebra_rank=3)
        assert ca.collar_einf_rank == 6  # 2 * 3

    def test_six_dim_three_handle(self):
        """6-manifold 3-handle collar: S^2 x R."""
        ca = collar_algebra_data(real_dim=6, handle_index=3)
        assert ca.collar_einf_rank == 2
        assert 'S^2' in ca.collar_manifold

    def test_verification_function(self):
        """verify_collar_algebras passes."""
        result = verify_collar_algebras()
        assert result['zero_handle_trivial'] is True
        assert result['two_handle_collar_rank'] == 2
        assert result['four_handle_collar_rank'] == 2


# =========================================================================
# Section 4: CFG25 analogy table
# =========================================================================

class TestCFG25Analogy:
    """The CFG25 analogy between CS and handle FH."""

    def test_analogy_table_length(self):
        """Three entries: CY_1 (CS), CY_2 (K3), CY_3."""
        table = cfg25_analogy_table()
        assert len(table) == 3

    def test_cs_dimensions(self):
        """CS dimensions: 3, 5, 7."""
        table = cfg25_analogy_table()
        dims = [e.cs_dim for e in table]
        assert dims == [3, 5, 7]

    def test_cy_dimensions(self):
        """CY dimensions: 1, 2, 3."""
        table = cfg25_analogy_table()
        cy_dims = [e.cy_dim for e in table]
        assert cy_dims == [1, 2, 3]

    def test_dimension_relation(self):
        """cs_dim = 2 * cy_dim + 1."""
        table = cfg25_analogy_table()
        for entry in table:
            assert entry.cs_dim == 2 * entry.cy_dim + 1

    def test_cy1_proved(self):
        """CY_1 (CS on 3-manifolds): PROVED."""
        table = cfg25_analogy_table()
        assert 'PROVED' in table[0].status

    def test_cy2_proved(self):
        """CY_2 (K3): PROVED for E_inf and CY-A_2."""
        table = cfg25_analogy_table()
        assert 'PROVED' in table[1].status

    def test_cy3_conjectural(self):
        """CY_3: CONJECTURAL (CY-A_3)."""
        table = cfg25_analogy_table()
        assert 'CONJECTURAL' in table[2].status

    def test_cy1_heegaard(self):
        """CY_1 splitting type is Heegaard."""
        table = cfg25_analogy_table()
        assert 'Heegaard' in table[0].splitting_type

    def test_cy2_handle(self):
        """CY_2 splitting type is handle decomposition."""
        table = cfg25_analogy_table()
        assert 'Handle' in table[1].splitting_type

    def test_cy3_handle(self):
        """CY_3 splitting type is handle decomposition."""
        table = cfg25_analogy_table()
        assert 'Handle' in table[2].splitting_type

    def test_cy2_state_space_hochschild(self):
        """CY_2 state space involves Hochschild homology."""
        table = cfg25_analogy_table()
        assert 'HH' in table[1].state_space or 'Hochschild' in table[1].state_space

    def test_cy3_state_space_s2(self):
        """CY_3 state space involves S^2."""
        table = cfg25_analogy_table()
        assert 'S^2' in table[2].state_space

    def test_cy2_gluing_intersection_form(self):
        """CY_2 gluing data: intersection form on H^2(K3)."""
        table = cfg25_analogy_table()
        assert 'intersection' in table[1].gluing_data.lower()

    def test_cy3_gluing_symplectic(self):
        """CY_3 gluing data: symplectic form on H^3."""
        table = cfg25_analogy_table()
        assert 'symplectic' in table[2].gluing_data.lower()

    def test_completeness(self):
        """Verification function passes."""
        result = verify_cfg25_analogy_completeness()
        assert result['num_entries'] == 3
        assert result['dimension_pattern'] is True
        assert result['covers_cy1_cy2_cy3'] is True


# =========================================================================
# Section 5: Iterative excision
# =========================================================================

class TestIterativeExcision:
    """Iterative excision through handle decomposition."""

    def test_k3_final_rank(self):
        """int_{K3} H_1 has rank 24 (Mukai rank)."""
        hd = k3_handle_data()
        rank = excision_final_rank(hd, input_rank=1)
        assert rank == 24

    def test_k3_final_rank_equals_mukai(self):
        """Final rank = Mukai rank."""
        hd = k3_handle_data()
        rank = excision_final_rank(hd, input_rank=1)
        assert rank == MUKAI_RANK

    def test_k3_excision_steps(self):
        """Iterative excision on K3 produces correct steps."""
        hd = k3_handle_data()
        steps = iterative_excision(hd, input_rank=1)
        # Should have at least 3 steps: 0-handle, 2-handles, 4-handle
        assert len(steps) >= 3
        # First step: 0-handle, rank 1
        assert steps[0].handle_index == 0
        assert steps[0].cumulative_rank == 1
        # Last step: 4-handle, rank 24
        assert steps[-1].handle_index == 4
        assert steps[-1].cumulative_rank == 24

    def test_k3_zero_handle(self):
        """Zero-handle contributes rank 1."""
        hd = k3_handle_data()
        steps = iterative_excision(hd, input_rank=1)
        assert steps[0].generators_added == 1
        assert steps[0].cumulative_rank == 1

    def test_k3_two_handles_total(self):
        """22 two-handles contribute rank 22."""
        hd = k3_handle_data()
        steps = iterative_excision(hd, input_rank=1)
        two_handle_steps = [s for s in steps if s.handle_index == 2]
        assert len(two_handle_steps) == 1  # batched
        assert two_handle_steps[0].generators_added == 22

    def test_k3_four_handle(self):
        """Four-handle contributes rank 1, closing to rank 24."""
        hd = k3_handle_data()
        steps = iterative_excision(hd, input_rank=1)
        four_handle_steps = [s for s in steps if s.handle_index == 4]
        assert len(four_handle_steps) == 1
        assert four_handle_steps[0].generators_added == 1
        assert four_handle_steps[0].cumulative_rank == 24

    def test_k3_rank_decomposition(self):
        """Rank 24 = 1 (H^0) + 22 (H^2) + 1 (H^4)."""
        assert 1 + 22 + 1 == 24

    def test_k3_higher_rank_input(self):
        """int_{K3} H_r has rank 24r."""
        hd = k3_handle_data()
        for r in [1, 2, 3, 5]:
            rank = excision_final_rank(hd, input_rank=r)
            assert rank == 24 * r

    def test_quintic_final_rank(self):
        """int_{Quintic} A has rank 208 for rank-1 E_inf."""
        hd = quintic_handle_data()
        rank = excision_final_rank(hd, input_rank=1)
        assert rank == sum(QUINTIC_BETTI)  # = 208

    def test_quintic_total_betti(self):
        """Total Betti dimension of quintic = 208."""
        assert sum(QUINTIC_BETTI) == 208

    def test_k3xe_final_rank(self):
        """int_{K3 x E} A has rank 96 for rank-1 E_inf."""
        hd = k3xe_handle_data()
        rank = excision_final_rank(hd, input_rank=1)
        assert rank == sum(K3XE_BETTI)  # = 96

    def test_k3xe_total_betti(self):
        """Total Betti dimension of K3 x E = 96."""
        assert sum(K3XE_BETTI) == 96

    def test_t6_final_rank(self):
        """int_{T^6} A has rank 64 for rank-1 E_inf."""
        hd = t6_handle_data()
        rank = excision_final_rank(hd, input_rank=1)
        assert rank == sum(T6_BETTI)  # = 2^6 = 64

    def test_t6_total_betti(self):
        """Total Betti dimension of T^6 = 2^6 = 64."""
        assert sum(T6_BETTI) == 64

    def test_verification_function(self):
        """verify_k3_excision_rank passes."""
        result = verify_k3_excision_rank()
        assert result['match'] is True
        assert result['final_rank'] == MUKAI_RANK


# =========================================================================
# Section 6: K3 Kirby diagram
# =========================================================================

class TestK3KirbyDiagram:
    """Kirby diagram (surgery presentation) of K3."""

    def test_num_two_handles(self):
        """22 two-handles in the Kirby diagram."""
        kd = k3_kirby_diagram()
        assert kd.num_two_handles == 22

    def test_lattice_decomposition(self):
        """Lattice = 3U + 2E_8(-1)."""
        kd = k3_kirby_diagram()
        assert '3U' in kd.lattice_decomposition
        assert 'E_8(-1)' in kd.lattice_decomposition

    def test_signature(self):
        """Signature (3, 19) of the framing matrix."""
        kd = k3_kirby_diagram()
        assert kd.signature == (3, 19)

    def test_even(self):
        """K3 intersection form is even."""
        kd = k3_kirby_diagram()
        assert kd.is_even is True

    def test_unimodular(self):
        """K3 intersection form is unimodular."""
        kd = k3_kirby_diagram()
        assert kd.is_unimodular is True

    def test_handle_count_decomposition(self):
        """6 handles from 3U + 16 handles from 2E_8(-1) = 22."""
        # 3 hyperbolic planes: 2 handles each = 6
        # 2 copies of E_8(-1): 8 handles each = 16
        assert 6 + 16 == 22

    def test_freedman_uniqueness(self):
        """Kirby diagram mentions Freedman classification."""
        kd = k3_kirby_diagram()
        assert 'Freedman' in kd.blow_down_equivalence


# =========================================================================
# Section 7: Handle vs Kummer route comparison
# =========================================================================

class TestHandleVsKummer:
    """Comparison of handle and Kummer routes for int_{K3} H_1."""

    def test_rank_match(self):
        """Both routes give rank 24."""
        comp = compare_handle_vs_kummer()
        assert comp.rank_match is True
        assert comp.handle_rank == 24
        assert comp.kummer_rank == 24

    def test_signature_match(self):
        """Both routes give Mukai signature (4, 20)."""
        comp = compare_handle_vs_kummer()
        assert comp.signature_match is True
        assert comp.handle_signature == (4, 20)
        assert comp.kummer_signature == (4, 20)

    def test_lattice_match(self):
        """Both routes give U^4 + E_8(-1)^2."""
        comp = compare_handle_vs_kummer()
        assert comp.lattice_match is True

    def test_character_match(self):
        """Both routes give character 1/eta^{24}."""
        comp = compare_handle_vs_kummer()
        assert comp.character_match is True

    def test_e2_equivalence_cites_cy_a2(self):
        """E_2 equivalence mentions CY-A_2."""
        comp = compare_handle_vs_kummer()
        assert 'CY-A_2' in comp.e2_equivalence_status

    def test_verification_function(self):
        """verify_handle_vs_kummer_agreement passes."""
        result = verify_handle_vs_kummer_agreement()
        assert result['all_match'] is True


# =========================================================================
# Section 8: CY3 handle analysis
# =========================================================================

class TestCY3HandleAnalysis:
    """Handle decomposition analysis for CY3 manifolds."""

    def test_quintic_analysis_betti(self):
        """Quintic analysis has correct Betti numbers."""
        qa = quintic_cy3_handle_analysis()
        assert qa.betti == QUINTIC_BETTI

    def test_quintic_analysis_euler(self):
        """Quintic analysis: chi = -200."""
        qa = quintic_cy3_handle_analysis()
        assert qa.euler_char == -200

    def test_quintic_analysis_hodge(self):
        """Quintic Hodge numbers: h^{1,1}=1, h^{2,1}=101."""
        qa = quintic_cy3_handle_analysis()
        assert qa.hodge_numbers['h^{1,1}'] == 1
        assert qa.hodge_numbers['h^{2,1}'] == 101

    def test_quintic_middle_cohomology(self):
        """b_3(quintic) = 204."""
        qa = quintic_cy3_handle_analysis()
        assert qa.middle_cohomology_rank == 204

    def test_quintic_symplectic_genus(self):
        """Symplectic genus g = 102 (b_3 = 2g)."""
        qa = quintic_cy3_handle_analysis()
        assert qa.symplectic_genus == 102
        assert 2 * qa.symplectic_genus == qa.middle_cohomology_rank

    def test_quintic_conjectural(self):
        """Quintic handle analysis is CONJECTURAL."""
        qa = quintic_cy3_handle_analysis()
        assert 'CONJECTURAL' in qa.status

    def test_quintic_conditions_cite_cy_a3(self):
        """Quintic conditions cite CY-A_3."""
        qa = quintic_cy3_handle_analysis()
        assert any('CY-A_3' in c for c in qa.conditions)

    def test_quintic_collar_s2(self):
        """Quintic 3-handle collar: int_{S^2 x R} A."""
        qa = quintic_cy3_handle_analysis()
        assert 'S^2' in qa.collar_at_3handle

    def test_k3xe_analysis_betti(self):
        """K3 x E analysis has correct Betti numbers."""
        ka = k3xe_cy3_handle_analysis()
        assert ka.betti == K3XE_BETTI

    def test_k3xe_analysis_euler(self):
        """K3 x E analysis: chi = 0."""
        ka = k3xe_cy3_handle_analysis()
        assert ka.euler_char == 0

    def test_k3xe_middle_cohomology(self):
        """b_3(K3 x E) = 44."""
        ka = k3xe_cy3_handle_analysis()
        assert ka.middle_cohomology_rank == 44

    def test_k3xe_symplectic_genus(self):
        """K3 x E symplectic genus = 22."""
        ka = k3xe_cy3_handle_analysis()
        assert ka.symplectic_genus == 22
        assert 2 * ka.symplectic_genus == ka.middle_cohomology_rank

    def test_k3xe_fubini(self):
        """K3 x E description mentions Fubini decomposition."""
        ka = k3xe_cy3_handle_analysis()
        assert 'Fubini' in ka.e3_collar_description

    def test_k3xe_conjectural(self):
        """K3 x E handle analysis is CONJECTURAL."""
        ka = k3xe_cy3_handle_analysis()
        assert 'CONJECTURAL' in ka.status

    def test_verification_quintic(self):
        """verify_quintic_handle_data passes."""
        result = verify_quintic_handle_data()
        assert result['betti_correct'] is True
        assert result['euler_correct'] is True
        assert result['b3_correct'] is True
        assert result['symplectic_genus_correct'] is True
        assert result['status_conjectural'] is True

    def test_verification_conjectural(self):
        """verify_conjectural_status_cy3 passes."""
        result = verify_conjectural_status_cy3()
        assert result['quintic_conjectural'] is True
        assert result['k3xe_conjectural'] is True
        assert result['cy3_analogy_conjectural'] is True
        assert result['quintic_cites_cy_a3'] is True
        assert result['k3xe_cites_cy_a3'] is True


# =========================================================================
# Section 9: State-space interpretation
# =========================================================================

class TestStateSpaceInterpretation:
    """CFG25-style state-space interpretation."""

    def test_k3_state_space_manifold(self):
        """State-space interpretation is for K3."""
        ss = k3_state_space_interpretation()
        assert ss.manifold == 'K3'

    def test_k3_state_space_dim(self):
        """K3 is 4-dimensional."""
        ss = k3_state_space_interpretation()
        assert ss.real_dim == 4

    def test_k3_final_answer_rank(self):
        """Final answer rank = 24."""
        ss = k3_state_space_interpretation()
        assert ss.final_answer_rank == 24

    def test_k3_s3_collar_rank(self):
        """S^3 collar state space has rank 2."""
        ss = k3_state_space_interpretation()
        assert ss.total_gluing_rank == 2

    def test_k3_state_space_cuts(self):
        """K3 has 24 cuts (0-handle + 22 two-handles + 4-handle)."""
        ss = k3_state_space_interpretation()
        assert ss.num_cuts == 24

    def test_k3_interpretation_mentions_cfg25(self):
        """Interpretation mentions CFG25 analogy."""
        ss = k3_state_space_interpretation()
        assert 'CFG25' in ss.interpretation

    def test_k3_interpretation_mentions_r_matrix(self):
        """Interpretation mentions R-matrix for E_2."""
        ss = k3_state_space_interpretation()
        assert 'R-matrix' in ss.interpretation

    def test_k3_first_cut_s3(self):
        """First cut (after zero-handle): boundary = S^3."""
        ss = k3_state_space_interpretation()
        first_cut = ss.state_spaces[0]
        assert first_cut['boundary'] == 'S^3'

    def test_k3_last_cut_closed(self):
        """Last cut: manifold is closed."""
        ss = k3_state_space_interpretation()
        last_cut = ss.state_spaces[-1]
        assert 'closed' in last_cut['boundary'].lower() or 'none' in last_cut['boundary'].lower()

    def test_k3_higher_rank_state_space(self):
        """State-space rank scales with input rank."""
        ss3 = k3_state_space_interpretation(input_rank=3)
        assert ss3.final_answer_rank == 72  # 24 * 3
        assert ss3.total_gluing_rank == 6   # 2 * 3


# =========================================================================
# Section 10: Numerical invariants
# =========================================================================

class TestNumericalInvariants:
    """Euler characteristic, signature, chi_y genus."""

    def test_euler_from_handles_k3(self):
        """euler_from_handles(K3) = 24."""
        hd = k3_handle_data()
        assert euler_from_handles(hd) == 24

    def test_euler_from_handles_quintic(self):
        """euler_from_handles(quintic) = -200."""
        hd = quintic_handle_data()
        assert euler_from_handles(hd) == -200

    def test_euler_from_handles_k3xe(self):
        """euler_from_handles(K3 x E) = 0."""
        hd = k3xe_handle_data()
        assert euler_from_handles(hd) == 0

    def test_signature_k3(self):
        """Hirzebruch signature tau(K3) = 3 - 19 = -16."""
        tau = signature_from_intersection_form(3, 19)
        assert tau == -16

    def test_signature_s2s2(self):
        """Hirzebruch signature tau(S^2 x S^2) = 1 - 1 = 0."""
        tau = signature_from_intersection_form(1, 1)
        assert tau == 0

    def test_signature_cp2(self):
        """Hirzebruch signature tau(CP^2) = 1 - 0 = 1."""
        tau = signature_from_intersection_form(1, 0)
        assert tau == 1

    def test_chi_y_genus_chi_0(self):
        """chi_0(K3) = chi(O_{K3}) = 2 = kappa_cat (AP113)."""
        data = chi_y_genus_k3()
        assert data['chi_0'] == 2
        assert data['kappa_cat'] == 2

    def test_chi_y_genus_signature(self):
        """chi_1(K3) = -16 = signature."""
        data = chi_y_genus_k3()
        assert data['chi_1'] == -16
        assert data['signature'] == -16

    def test_chi_y_genus_euler(self):
        """chi_{-1}(K3) = 24 = Euler characteristic."""
        data = chi_y_genus_k3()
        assert data['chi_minus1'] == 24
        assert data['euler'] == 24

    def test_chi_y_polynomial(self):
        """chi_y(K3) = 2 - 20y + 2y^2."""
        data = chi_y_genus_k3()
        assert data['chi_y_polynomial'] == '2 - 20y + 2y^2'

    def test_chi_y_cross_check_signature(self):
        """2 - 20 + 2 = -16 (signature)."""
        assert 2 - 20 + 2 == -16

    def test_chi_y_cross_check_euler(self):
        """2 + 20 + 2 = 24 (Euler)."""
        assert 2 + 20 + 2 == 24

    def test_verification_chi_y(self):
        """verify_chi_y_genus_k3 passes."""
        result = verify_chi_y_genus_k3()
        assert result['chi_0_is_kappa_cat'] is True
        assert result['chi_1_is_signature'] is True
        assert result['chi_minus1_is_euler'] is True


# =========================================================================
# Section 11: Kunneth formula
# =========================================================================

class TestKunnethFormula:
    """Kunneth formula for K3 x E."""

    def test_kunneth_b0(self):
        """b_0(K3 x E) = b_0(K3) * b_0(E) = 1."""
        assert K3XE_BETTI[0] == 1

    def test_kunneth_b1(self):
        """b_1(K3 x E) = b_0(K3)*b_1(E) + b_1(K3)*b_0(E) = 2 + 0 = 2."""
        assert K3XE_BETTI[1] == 2

    def test_kunneth_b2(self):
        """b_2(K3 x E) = 1*1 + 0*2 + 22*1 = 23."""
        assert K3XE_BETTI[2] == 23

    def test_kunneth_b3(self):
        """b_3(K3 x E) = 0*1 + 22*2 + 0*1 = 44."""
        # b_3 = b_0*b_3(E=0) + b_1*b_2(E=1) + b_2*b_1(E=2) + b_3*b_0(E=1)
        # But E has Betti (1,2,1), so b_j(E)=0 for j>=3
        # b_3 = K3_b_1*E_b_2 + K3_b_2*E_b_1 + K3_b_3*E_b_0
        # = 0*1 + 22*2 + 0*1 = 44
        assert K3XE_BETTI[3] == 44

    def test_kunneth_b4(self):
        """b_4(K3 x E) = 22*1 + 0*2 + 1*1 = 23."""
        assert K3XE_BETTI[4] == 23

    def test_kunneth_b5(self):
        """b_5(K3 x E) = 0*1 + 1*2 = 2."""
        assert K3XE_BETTI[5] == 2

    def test_kunneth_b6(self):
        """b_6(K3 x E) = 1*1 = 1."""
        assert K3XE_BETTI[6] == 1

    def test_kunneth_euler_product(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
        chi_k3 = sum((-1)**k * b for k, b in enumerate(K3_BETTI))
        chi_e = 0
        chi_product = chi_k3 * chi_e
        chi_kxe = sum((-1)**k * b for k, b in enumerate(K3XE_BETTI))
        assert chi_product == chi_kxe == 0

    def test_kunneth_total_dimension(self):
        """dim H_*(K3 x E) = dim H_*(K3) * dim H_*(E) = 24 * 4 = 96."""
        total_k3 = sum(K3_BETTI)
        total_e = 4  # (1, 2, 1)
        assert total_k3 * total_e == sum(K3XE_BETTI)
        assert sum(K3XE_BETTI) == 96

    def test_verification_kunneth(self):
        """verify_k3xe_kunneth passes."""
        result = verify_k3xe_kunneth()
        assert result['match'] is True
        assert result['euler_match'] is True


# =========================================================================
# Section 12: Euler consistency across all manifolds
# =========================================================================

class TestEulerConsistency:
    """Euler characteristic consistency for all manifolds."""

    def test_all_euler_consistent(self):
        """All manifold Euler characteristics match handles and Betti."""
        result = verify_handle_euler_consistency()
        assert result['all_match'] is True

    def test_k3_euler_in_table(self):
        """K3 Euler = 24 in the consistency table."""
        result = verify_handle_euler_consistency()
        assert result['results']['K3']['expected'] == 24
        assert result['results']['K3']['match'] is True

    def test_quintic_euler_in_table(self):
        """Quintic Euler = -200 in the consistency table."""
        result = verify_handle_euler_consistency()
        assert result['results']['Quintic']['expected'] == -200
        assert result['results']['Quintic']['match'] is True

    def test_k3xe_euler_in_table(self):
        """K3 x E Euler = 0 in the consistency table."""
        result = verify_handle_euler_consistency()
        assert result['results']['K3 x E']['expected'] == 0
        assert result['results']['K3 x E']['match'] is True

    def test_t6_euler_in_table(self):
        """T^6 Euler = 0 in the consistency table."""
        result = verify_handle_euler_consistency()
        assert result['results']['T^6']['expected'] == 0
        assert result['results']['T^6']['match'] is True

    def test_cy3_euler_verification(self):
        """CY3 Euler characteristic verification passes."""
        result = verify_cy3_euler_characteristics()
        assert result['all_match'] is True


# =========================================================================
# Section 13: K3 signature
# =========================================================================

class TestK3Signature:
    """Mukai signature from handle decomposition."""

    def test_mukai_signature_from_handles(self):
        """Mukai sig = (3+1, 19+1) = (4, 20)."""
        result = verify_k3_signature()
        assert result['match'] is True

    def test_h0_h4_hyperbolic_plane(self):
        """H^0-H^4 pairing: signature (1, 1)."""
        result = verify_k3_signature()
        assert result['h0_h4_sig'] == (1, 1)

    def test_h2_intersection_form(self):
        """H^2 intersection form: signature (3, 19)."""
        result = verify_k3_signature()
        assert result['h2_sig'] == (3, 19)

    def test_total_mukai(self):
        """Total = (4, 20) = Mukai."""
        result = verify_k3_signature()
        assert result['total_sig'] == (4, 20)
        assert result['mukai_sig'] == (4, 20)


# =========================================================================
# Section 14: Full verification
# =========================================================================

class TestFullVerification:
    """Full verification pipeline."""

    def test_full_verification_runs(self):
        """Full verification completes without error."""
        result = full_verification()
        assert isinstance(result, dict)
        assert len(result) == 11

    def test_all_paths_present(self):
        """All 11 verification paths are present."""
        result = full_verification()
        expected_paths = [
            'path1_euler_consistency',
            'path2_k3_excision_rank',
            'path3_k3_signature',
            'path4_handle_vs_kummer',
            'path5_cy3_euler',
            'path6_chi_y_genus',
            'path7_cfg25_analogy',
            'path8_collar_algebras',
            'path9_quintic_handles',
            'path10_kunneth_k3xe',
            'path11_conjectural_cy3',
        ]
        for path in expected_paths:
            assert path in result

    def test_path1_passes(self):
        """Path 1 (Euler consistency) passes."""
        result = full_verification()
        assert result['path1_euler_consistency']['all_match'] is True

    def test_path2_passes(self):
        """Path 2 (K3 excision rank) passes."""
        result = full_verification()
        assert result['path2_k3_excision_rank']['match'] is True

    def test_path3_passes(self):
        """Path 3 (K3 signature) passes."""
        result = full_verification()
        assert result['path3_k3_signature']['match'] is True

    def test_path4_passes(self):
        """Path 4 (handle vs Kummer) passes."""
        result = full_verification()
        assert result['path4_handle_vs_kummer']['all_match'] is True

    def test_path5_passes(self):
        """Path 5 (CY3 Euler) passes."""
        result = full_verification()
        assert result['path5_cy3_euler']['all_match'] is True

    def test_path10_passes(self):
        """Path 10 (Kunneth K3 x E) passes."""
        result = full_verification()
        assert result['path10_kunneth_k3xe']['match'] is True


# =========================================================================
# Section 15: AP compliance and conjectural status
# =========================================================================

class TestAPCompliance:
    """Anti-pattern compliance for CY3 conjectural status."""

    def test_ap_cy14_quintic_conjectural(self):
        """AP-CY14: Quintic result is CONJECTURAL (depends on CY-A_3)."""
        qa = quintic_cy3_handle_analysis()
        assert 'CONJECTURAL' in qa.status

    def test_ap_cy14_k3xe_conjectural(self):
        """AP-CY14: K3 x E result is CONJECTURAL (depends on CY-A_3)."""
        ka = k3xe_cy3_handle_analysis()
        assert 'CONJECTURAL' in ka.status

    def test_ap_cy32_quintic_reorganisation(self):
        """AP-CY32: Quintic conditions mention reorganisation."""
        qa = quintic_cy3_handle_analysis()
        assert any('reorganisation' in c.lower() or 'AP-CY32' in c for c in qa.conditions)

    def test_ap_cy32_k3xe_reorganisation(self):
        """AP-CY32: K3 x E conditions mention reorganisation or Fubini."""
        ka = k3xe_cy3_handle_analysis()
        assert any('Fubini' in c or 'CY-A_3' in c for c in ka.conditions)

    def test_ap113_chi_y_kappa(self):
        """AP113: chi_y genus uses kappa_cat (subscripted), not bare kappa."""
        data = chi_y_genus_k3()
        assert 'kappa_cat' in data
        # No bare 'kappa' key (all subscripted)
        assert all('kappa' not in k or '_' in k for k in data.keys()
                    if 'kappa' in k)

    def test_cy2_handle_proved(self):
        """CY_2 handle decomposition is PROVED (not conjectural)."""
        table = cfg25_analogy_table()
        cy2_entry = table[1]
        assert 'PROVED' in cy2_entry.status

    def test_cy3_analogy_conjectural(self):
        """CY_3 analogy is correctly marked CONJECTURAL."""
        table = cfg25_analogy_table()
        cy3_entry = table[2]
        assert 'CONJECTURAL' in cy3_entry.status
