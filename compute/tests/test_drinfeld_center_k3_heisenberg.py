r"""Tests for drinfeld_center_k3_heisenberg.py: Drinfeld center of Rep^{E_1}(H_Muk).

CENTRAL RESULTS:
    (1) Drin(H_Muk) has dimension 49 = 24 + 24 + 1 (THEOREM: Drinfeld double).
    (2) Z(Rep^{E_1}(H_Muk)) = Rep^{E_2}(Drin(H_Muk)) (THEOREM: Drinfeld).
    (3) R-matrix = exp(omega^{-1}), determined by Mukai signature (4,20) (THEOREM).
    (4) Braided tensor category: E_2, NOT symmetric, NOT modular (THEOREM).
    (5) Fock character = 1/eta^{48} (THEOREM: 48 oscillators from double).
    (6) Quantization to Y(g_{K3}): CONJECTURAL (AP-CY14).

Manuscript references:
    drinfeld_center_braided.tex (Drinfeld center construction)
    k3_times_e.tex L1165 (K3 double current algebra definition)
    Part IV (quantum groups and braided monoidal structure)
"""

import pytest
from fractions import Fraction

from compute.lib.drinfeld_center_k3_heisenberg import (
    # Constants
    DRINFELD_DOUBLE_GENERATORS,
    DRINFELD_DOUBLE_DIM,
    # Drinfeld double
    drinfeld_double_h_muk,
    drinfeld_double_bracket,
    # R-matrix
    r_matrix_drinfeld_center,
    r_matrix_on_fock_modules,
    # Braided category
    braided_category_structure,
    s_matrix_on_lattice,
    # Character
    drinfeld_double_character,
    # Quantization
    quantization_conjectural,
    # Verification
    verify_drinfeld_double_dimension,
    verify_bracket_antisymmetry,
    verify_r_matrix_properties,
    verify_braided_category,
    verify_character_coefficients,
    verify_quantization_status,
    verify_s_matrix_lattice_triviality,
    full_verification,
)

F = Fraction


# =========================================================================
# Section 1: Drinfeld double dimension and structure
# =========================================================================

class TestDrinfeldDoubleDimension:
    """Dimension and structure of Drin(H_Muk)."""

    def test_double_generators_count(self):
        """48 generators: 24 original + 24 dual."""
        assert DRINFELD_DOUBLE_GENERATORS == 48

    def test_double_total_dim(self):
        """Total dimension 49 = 48 generators + 1 central."""
        assert DRINFELD_DOUBLE_DIM == 49

    def test_double_data_fields(self):
        """DrinfeldDoubleHeisenberg has correct field values."""
        dd = drinfeld_double_h_muk()
        assert dd.total_dim == 49
        assert dd.original_generators == 24
        assert dd.dual_generators == 24
        assert dd.central_dim == 1

    def test_mukai_signature_in_double(self):
        """Mukai signature (4, 20) propagates to double."""
        dd = drinfeld_double_h_muk()
        assert dd.mukai_signature == (4, 20)

    def test_verify_dimension(self):
        """Full dimension verification path."""
        result = verify_drinfeld_double_dimension()
        assert result['match'] is True


# =========================================================================
# Section 2: Bracket structure of Drin(H_Muk)
# =========================================================================

class TestDrinfeldDoubleBracket:
    """Bracket structure: original, dual, and cross sectors."""

    def test_original_h0_h4(self):
        """[J_0, J_23] = -c (Mukai pairing H^0-H^4)."""
        coeff, _ = drinfeld_double_bracket(0, 23, 'original')
        assert coeff == -1

    def test_original_antisymmetry(self):
        """[J_0, J_23] = -[J_23, J_0]."""
        c1, _ = drinfeld_double_bracket(0, 23, 'original')
        c2, _ = drinfeld_double_bracket(23, 0, 'original')
        assert c1 == -c2

    def test_dual_sign_flip(self):
        """[J_i*, J_j*] = -omega(i,j)*c (opposite sign to original)."""
        c_orig, _ = drinfeld_double_bracket(0, 23, 'original')
        c_dual, _ = drinfeld_double_bracket(0, 23, 'dual')
        assert c_dual == -c_orig

    def test_dual_antisymmetry(self):
        """[J_0*, J_23*] = -[J_23*, J_0*]."""
        c1, _ = drinfeld_double_bracket(0, 23, 'dual')
        c2, _ = drinfeld_double_bracket(23, 0, 'dual')
        assert c1 == -c2

    def test_cross_diagonal(self):
        """[J_i, J_i*] = c for all i."""
        for i in [0, 5, 11, 22, 23]:
            coeff, _ = drinfeld_double_bracket(i, i, 'cross')
            assert coeff == 1, f"[J_{i}, J_{i}*] should be c"

    def test_cross_off_diagonal(self):
        """[J_i, J_j*] = 0 for i != j."""
        pairs = [(0, 1), (5, 10), (23, 0), (1, 22)]
        for i, j in pairs:
            coeff, _ = drinfeld_double_bracket(i, j, 'cross')
            assert coeff == 0, f"[J_{i}, J_{j}*] should be 0"

    def test_original_h2_block_generic(self):
        """[J_i, J_j] for i,j in H^2 block returns 0 (generic placeholder)."""
        coeff, _ = drinfeld_double_bracket(5, 10, 'original')
        assert coeff == 0

    def test_verify_antisymmetry(self):
        """Full antisymmetry verification path."""
        result = verify_bracket_antisymmetry()
        assert result['all_pass'] is True

    def test_invalid_sector_raises(self):
        """Invalid sector raises ValueError."""
        with pytest.raises(ValueError):
            drinfeld_double_bracket(0, 1, 'invalid')


# =========================================================================
# Section 3: R-matrix structure
# =========================================================================

class TestRMatrix:
    """R-matrix of Z(Rep^{E_1}(H_Muk))."""

    def test_r_matrix_is_rational(self):
        """R-matrix is rational (exponential truncates for Heisenberg)."""
        r = r_matrix_drinfeld_center()
        assert r.is_rational is True

    def test_r_matrix_signature(self):
        """R-matrix determined by Mukai signature (4, 20)."""
        r = r_matrix_drinfeld_center()
        assert r.pairing_signature == (4, 20)
        assert r.num_positive_eigenvalues == 4
        assert r.num_negative_eigenvalues == 20

    def test_r_matrix_ybe(self):
        """R-matrix satisfies Yang-Baxter (automatic for Drinfeld doubles)."""
        r = r_matrix_drinfeld_center()
        assert r.satisfies_ybe is True

    def test_exponent_positive_direction(self):
        """R(e_1, e_1) = exp(+1) in the positive signature direction."""
        lam = [1] + [0] * 23
        exp = r_matrix_on_fock_modules(lam, lam)
        assert exp == F(1)

    def test_exponent_negative_direction(self):
        """R(e_{24}, e_{24}) = exp(-1) in the negative signature direction."""
        lam = [0] * 23 + [1]
        exp = r_matrix_on_fock_modules(lam, lam)
        assert exp == F(-1)

    def test_exponent_orthogonal(self):
        """R(e_1, e_{24}) = exp(0) for orthogonal directions."""
        lam1 = [1] + [0] * 23
        lam2 = [0] * 23 + [1]
        exp = r_matrix_on_fock_modules(lam1, lam2)
        assert exp == F(0)

    def test_exponent_mixed(self):
        """R(e_1 + e_5, e_1 + e_5) = 1 + (-1) = 0 (mixed signature)."""
        lam = [1, 0, 0, 0] + [1] + [0] * 19
        exp = r_matrix_on_fock_modules(lam, lam)
        assert exp == F(0)  # +1 from e_1 direction, -1 from e_5 direction

    def test_exponent_bilinearity(self):
        """Exponent is bilinear: <2*e_1, e_1> = 2 * <e_1, e_1> = 2."""
        lam1 = [2] + [0] * 23
        lam2 = [1] + [0] * 23
        exp = r_matrix_on_fock_modules(lam1, lam2)
        assert exp == F(2)

    def test_exponent_full_positive_block(self):
        """Sum over all 4 positive directions: exponent = 4."""
        lam = [1, 1, 1, 1] + [0] * 20
        exp = r_matrix_on_fock_modules(lam, lam)
        assert exp == F(4)

    def test_vector_length_validation(self):
        """Vectors of wrong length raise ValueError."""
        with pytest.raises(ValueError):
            r_matrix_on_fock_modules([1, 0], [0, 1])

    def test_verify_r_matrix(self):
        """Full R-matrix verification path."""
        result = verify_r_matrix_properties()
        assert result['all_pass'] is True


# =========================================================================
# Section 4: Braided tensor category
# =========================================================================

class TestBraidedCategory:
    """Properties of Z(Rep^{E_1}(H_Muk)) as braided tensor category."""

    def test_is_braided(self):
        """Drinfeld center is braided monoidal (E_2)."""
        cat = braided_category_structure()
        assert cat.is_braided is True

    def test_not_symmetric(self):
        """Braiding is NOT symmetric (indefinite signature prevents sigma^2=id)."""
        cat = braided_category_structure()
        assert cat.is_symmetric is False

    def test_not_modular(self):
        """NOT modular: continuous family of simples (Fock modules)."""
        cat = braided_category_structure()
        assert cat.is_modular is False

    def test_is_ribbon(self):
        """Drin(H_Muk) is a ribbon Hopf algebra."""
        cat = braided_category_structure()
        assert cat.ribbon is True

    def test_central_charge_equals_rank(self):
        """Fock central charge = 24 = kappa_fiber (AP113: NOT kappa_ch)."""
        cat = braided_category_structure()
        assert cat.central_charge_fock == 24

    def test_verify_braided_category(self):
        """Full braided category verification path."""
        result = verify_braided_category()
        assert result['all_pass'] is True


# =========================================================================
# Section 5: S-matrix on Mukai lattice
# =========================================================================

class TestSMatrix:
    """S-matrix (monodromy) on the Mukai lattice."""

    def test_s_matrix_exponent_integer(self):
        """S-matrix exponent is integer for lattice vectors."""
        v1 = [1] + [0] * 23
        v2 = [1] + [0] * 23
        exp = s_matrix_on_lattice(v1, v2)
        assert exp.denominator == 1

    def test_s_matrix_lattice_trivial(self):
        """Braiding is trivial on the lattice: S = exp(2*pi*i * Z) = 1."""
        result = verify_s_matrix_lattice_triviality()
        assert result['lattice_braiding_trivial'] is True

    def test_s_matrix_various_vectors(self):
        """S-matrix exponents for various lattice vectors are all integers."""
        vectors = [
            [1] + [0] * 23,
            [0] * 23 + [1],
            [1, 1, 0, 0] + [0] * 20,
            [1, -1, 1, -1] + [1, -1] * 10,
        ]
        for v1 in vectors:
            for v2 in vectors:
                exp = s_matrix_on_lattice(v1, v2)
                assert exp.denominator == 1, (
                    f"S-matrix exponent {exp} is not integer for lattice vectors"
                )


# =========================================================================
# Section 6: Character of Drinfeld double
# =========================================================================

class TestCharacter:
    """Character of Fock(Drin(H_Muk)) = 1/eta^{48}."""

    def test_character_q0(self):
        """Coefficient of q^0 = 1."""
        ch = drinfeld_double_character(3)
        assert ch[0] == 1

    def test_character_q1(self):
        """Coefficient of q^1 = 48 (48 oscillators at energy 1)."""
        ch = drinfeld_double_character(3)
        assert ch[1] == 48

    def test_character_q2(self):
        """Coefficient of q^2 = 1224 = C(49,2) + 48."""
        ch = drinfeld_double_character(3)
        assert ch[2] == 1224

    def test_character_factorization(self):
        """1/eta^{48} = (1/eta^{24})^2: double character is square of single.

        Verify by computing 1/eta^{24} and convolving with itself.
        """
        from compute.lib.k3_double_current_algebra import partition_function
        N = 6
        single = partition_function(N)
        double = drinfeld_double_character(N)

        # Convolution of single with itself
        convolved = {}
        for n in range(N + 1):
            s = 0
            for k in range(n + 1):
                s += single.get(k, 0) * single.get(n - k, 0)
            convolved[n] = s

        for n in range(N + 1):
            assert double.get(n, 0) == convolved.get(n, 0), (
                f"q^{n}: double={double.get(n,0)}, convolved={convolved.get(n,0)}"
            )

    def test_verify_character(self):
        """Full character verification path."""
        result = verify_character_coefficients()
        assert result['match'] is True


# =========================================================================
# Section 7: Quantization (CONJECTURAL, AP-CY14)
# =========================================================================

class TestQuantization:
    """Quantization from H_Muk to Y(g_{K3}): conjectural status checks."""

    def test_status_conjectural(self):
        """Quantization is marked CONJECTURAL."""
        q = quantization_conjectural()
        assert q.status == 'CONJECTURAL'

    def test_dependency_stated(self):
        """Dependency on open K3 Yangian construction is stated."""
        q = quantization_conjectural()
        assert 'open' in q.dependency.lower()

    def test_cy_a_2_acknowledged(self):
        """CY-A_2 (proved at d=2) is acknowledged as partial foundation."""
        q = quantization_conjectural()
        assert 'CY-A_2' in q.dependency

    def test_verify_quantization(self):
        """Full quantization status verification."""
        result = verify_quantization_status()
        assert result['ap_cy14_compliant'] is True


# =========================================================================
# Section 8: Full verification
# =========================================================================

class TestFullVerification:
    """Integration tests: all verification paths."""

    def test_full_verification_all_pass(self):
        """All 7 verification paths pass."""
        result = full_verification()
        assert result['path1_double_dimension']['match'] is True
        assert result['path2_bracket_antisymmetry']['all_pass'] is True
        assert result['path3_r_matrix']['all_pass'] is True
        assert result['path4_braided_category']['all_pass'] is True
        assert result['path5_character']['match'] is True
        assert result['path6_quantization_status']['ap_cy14_compliant'] is True
        assert result['path7_s_matrix_lattice']['lattice_braiding_trivial'] is True
