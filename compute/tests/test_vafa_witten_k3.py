"""Tests for vafa_witten_k3: VW partition function on K3 and the BKM
superalgebra g_{Delta_5}.

Claims tested:
1. chi(Hilb^n(K3)) matches known values (Gottsche formula)
2. DMVV exponents = phi_{0,1} discriminant coefficients (root multiplicities)
3. Low-order root multiplicities: c(-1)=1, c(0)=10, c(3)=-64, c(4)=108
4. Closed loop: CY3 geometry -> DT -> root mult -> VW -> geometry
5. Hilbert scheme chi from 1/eta(q)^{24} matches OEIS values

Ground truth:
    Gottsche (1990): chi(Hilb^n(K3))
    Dijkgraaf-Moore-Verlinde-Verlinde hep-th/9607026
    Gritsenko-Nikulin (1997): Siegel automorphic forms
    chi(Hilb^0)=1, chi(Hilb^1)=24, chi(Hilb^2)=324, chi(Hilb^3)=3200
"""

import pytest
from fractions import Fraction

from compute.lib.vafa_witten_k3 import (
    hilb_euler_characteristics,
    KNOWN_HILB_CHI,
    verify_root_multiplicities_low_order,
    verify_dmvv_vs_hilb_k3,
    verify_closed_loop,
    verify_dmvv_exponents_equal_phi01,
    phi01_by_discriminant,
)


# ======================================================================
# 1. Hilbert scheme Euler characteristics
# ======================================================================

class TestHilbEulerCharacteristics:
    """Verify chi(Hilb^n(K3)) from 1/eta(q)^{24}."""

    def test_hilb_0(self):
        """chi(Hilb^0(K3)) = 1 (a point)."""
        hilb = hilb_euler_characteristics(0)
        # VERIFIED [DC] Hilbert scheme chi [LT] Gottsche formula
        assert hilb[0] == 1

    def test_hilb_1(self):
        """chi(Hilb^1(K3)) = 24 = chi(K3)."""
        hilb = hilb_euler_characteristics(1)
        assert hilb[1] == 24

    def test_hilb_2(self):
        """chi(Hilb^2(K3)) = 324."""
        hilb = hilb_euler_characteristics(2)
        assert hilb[2] == 324

    def test_hilb_3(self):
        """chi(Hilb^3(K3)) = 3200."""
        hilb = hilb_euler_characteristics(3)
        assert hilb[3] == 3200

    def test_matches_known_table(self):
        """All values match the KNOWN_HILB_CHI table (multi-path)."""
        max_n = max(KNOWN_HILB_CHI.keys())
        hilb = hilb_euler_characteristics(max_n)
        for n, expected in KNOWN_HILB_CHI.items():
            assert hilb[n] == expected, f"chi(Hilb^{n}(K3)): {hilb[n]} != {expected}"

    def test_integrality(self):
        """All chi(Hilb^n(K3)) are positive integers."""
        hilb = hilb_euler_characteristics(10)
        for n, val in enumerate(hilb):
            assert isinstance(val, int)
            assert val > 0


# ======================================================================
# 2. DMVV exponents = phi_{0,1} root multiplicities
# ======================================================================

class TestDMVVExponents:
    """Verify the central claim: DMVV product exponents are phi_{0,1} coefficients."""

    def test_dmvv_equals_phi01(self):
        """All DMVV exponents match phi_{0,1} discriminant coefficients."""
        result = verify_dmvv_exponents_equal_phi01(3)
        assert result['all_match'] is True

    def test_spot_checks(self):
        """Specific c(D) values match known root multiplicities."""
        result = verify_dmvv_exponents_equal_phi01(3)
        assert result['spot_checks_pass'] is True

    def test_c_neg1_is_1(self):
        """c(-1) = 1: the unique real simple root."""
        c = phi01_by_discriminant(5)
        # VERIFIED [DC] BKM root multiplicity [LT] Gritsenko-Nikulin
        assert c[-1] == 1

    def test_c_0_is_10(self):
        """c(0) = 10: the 10 imaginary simple roots."""
        c = phi01_by_discriminant(5)
        assert c[0] == 10

    def test_fermionic_root(self):
        """c(3) = -64: negative multiplicity indicates fermionic root."""
        c = phi01_by_discriminant(5)
        assert c[3] == -64

    def test_nontrivial_count(self):
        """Many root multiplicities checked (not vacuous test)."""
        result = verify_dmvv_exponents_equal_phi01(3)
        assert result['count'] > 20


# ======================================================================
# 3. Root multiplicity verification
# ======================================================================

class TestRootMultiplicities:
    """Verify root multiplicities at low order."""

    def test_low_order(self):
        """verify_root_multiplicities_low_order passes at max_ord=4."""
        result = verify_root_multiplicities_low_order(4)
        assert result['all_pass'] is True
        assert result['count'] > 0

    def test_root_count_nontrivial(self):
        """Significant number of roots verified."""
        result = verify_root_multiplicities_low_order(3)
        assert result['count'] > 10


# ======================================================================
# 4. Closed loop verification
# ======================================================================

class TestClosedLoop:
    """Verify the closed loop: CY3 -> DT -> root mult -> VW -> geometry."""

    def test_closed_loop_passes(self):
        """verify_closed_loop at max_ord=3 passes all checks."""
        result = verify_closed_loop(3)
        assert result['all_pass'] is True

    def test_closed_loop_steps(self):
        """Each step in the closed loop produces expected data."""
        result = verify_closed_loop(2)
        # Must have computed all intermediate steps
        assert 'hilb_chi' in result
        assert 'root_multiplicities' in result


# ======================================================================
# 5. Cross-check: Hilbert scheme and DMVV consistency
# ======================================================================

class TestDMVVvsHilb:
    """Verify DMVV diagonal sector relates to Hilb^n(K3) data."""

    def test_dmvv_diagonal_structure(self):
        """DMVV diagonal sector has expected structure."""
        result = verify_dmvv_vs_hilb_k3(3)
        assert 'diagonal_coefficients' in result
        # Diagonal coefficient at N=0 should be 1
        assert result['diagonal_coefficients'][0] == 1
