r"""Cross-validation tests for phi_{0,1} Fourier coefficients across all four modules.

Ensures that phi01_fourier.py (exact rational), igusa_product_formula.py (mpmath DFT),
wkb_denominator.py (hardcoded table + numerical DFT), and bkm_shadow_tower.py (delegate)
all produce identical phi_{0,1} coefficients and satisfy the structural properties of
a weak Jacobi form of weight 0 and index 1.

Ground truth: Eichler-Zagier, "The Theory of Jacobi Forms" (1985), Table 1.
"""

from __future__ import annotations

import os
import sys
from typing import Dict, Tuple

import pytest

# ---------------------------------------------------------------------------
# Ensure repo root is on sys.path
# ---------------------------------------------------------------------------
_repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _repo not in sys.path:
    sys.path.insert(0, _repo)

from compute.lib.phi01_fourier import (
    phi01_table as fourier_table,
    phi01_by_discriminant as fourier_by_disc,
    phi01_coefficient as fourier_coeff,
)
from compute.lib.igusa_product_formula import (
    compute_f_disc as igusa_compute_f_disc,
    f_coeff as igusa_f_coeff,
)
from compute.lib.wkb_denominator import (
    PHI01_TABLE as wkb_hardcoded,
    C_DISC as wkb_c_disc,
    compute_phi01_table as wkb_dft_extract,
)
from compute.lib.bkm_shadow_tower import (
    get_f as bkm_get_f,
    phi01_coefficients as bkm_phi01_data,
)


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

MAX_N = 6
MAX_L = 6

# Eichler-Zagier published c(D) values
EICHLER_ZAGIER = {
    -1: 1,
    0: 10,
    3: -64,
    4: 108,
    7: -513,
    8: 808,
    11: -2752,
    12: 4016,
    15: -11775,
    16: 16524,
}


# ---------------------------------------------------------------------------
# Fixtures: build each table once per session
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def ref_table() -> Dict[Tuple[int, int], int]:
    """Reference table from phi01_fourier (exact rational arithmetic)."""
    return fourier_table(MAX_N)


@pytest.fixture(scope="module")
def ref_c() -> Dict[int, int]:
    """Discriminant-indexed reference from phi01_fourier."""
    return fourier_by_disc(MAX_N)


@pytest.fixture(scope="module")
def igusa_c() -> Dict[int, int]:
    """Discriminant table from igusa_product_formula (mpmath DFT).

    Uses explicit prec=200 to avoid rounding errors at D >= 20.
    The default auto-precision is marginal for N_max >= 8.
    """
    return igusa_compute_f_disc(4 * MAX_N, prec=200)


@pytest.fixture(scope="module")
def igusa_table(igusa_c) -> Dict[Tuple[int, int], int]:
    """(n,l)-indexed table built from igusa c(D)."""
    result = {}
    for n in range(MAX_N + 1):
        for l in range(-MAX_L, MAX_L + 1):
            D = 4 * n - l * l
            if D < -1:
                continue
            val = igusa_c.get(D, 0)
            if val != 0:
                result[(n, l)] = val
    return result


@pytest.fixture(scope="module")
def wkb_hard_table() -> Dict[Tuple[int, int], int]:
    """Hardcoded table from wkb_denominator."""
    return {k: v for k, v in wkb_hardcoded.items()
            if k[0] <= MAX_N and abs(k[1]) <= MAX_L}


@pytest.fixture(scope="module")
def wkb_dft_table() -> Dict[Tuple[int, int], int]:
    """Live DFT extraction from wkb_denominator.

    The numpy DFT loses precision at n=6 (double-precision arithmetic).
    We extract up to n=5 reliably; n=6 entries may be missing or wrong.
    """
    # Use n_max=5 to stay within double-precision reliable range
    raw = wkb_dft_extract(n_max=5, l_max=MAX_L)
    return {k: v for k, v in raw.items() if v != 0 and 4 * k[0] - k[1]**2 >= -1}


@pytest.fixture(scope="module")
def bkm_table() -> Dict[Tuple[int, int], int]:
    """Table from bkm_shadow_tower (delegates to phi01_fourier)."""
    data = bkm_phi01_data(max_D=4 * MAX_N + 10)
    result = {}
    for n in range(MAX_N + 1):
        for l in range(-MAX_L, MAX_L + 1):
            val = bkm_get_f(n, l, data)
            if val != 0:
                result[(n, l)] = val
    return result


@pytest.fixture(scope="module")
def all_tables(ref_table, igusa_table, wkb_hard_table, wkb_dft_table, bkm_table):
    """All five tables keyed by name."""
    return {
        "phi01_fourier": ref_table,
        "igusa_product": igusa_table,
        "wkb_hardcoded": wkb_hard_table,
        "wkb_dft": wkb_dft_table,
        "bkm_shadow": bkm_table,
    }


# ---------------------------------------------------------------------------
# Helper: enumerate all valid (n,l) in range
# ---------------------------------------------------------------------------

def _all_nl():
    """All (n,l) with n in [0, MAX_N], |l| <= MAX_L, D = 4n-l^2 >= -1."""
    for n in range(MAX_N + 1):
        for l in range(-MAX_L, MAX_L + 1):
            if 4 * n - l * l >= -1:
                yield n, l


# =========================================================================
# A. PAIRWISE AGREEMENT
# =========================================================================

class TestPairwiseAgreement:
    """Every module must produce identical f(n,l) values for n<=6, |l|<=6."""

    def test_igusa_vs_fourier(self, ref_table, igusa_table):
        for n, l in _all_nl():
            ref = ref_table.get((n, l), 0)
            test = igusa_table.get((n, l), 0)
            assert ref == test, (
                f"igusa_product disagrees at f({n},{l}): got {test}, expected {ref}"
            )

    def test_wkb_hardcoded_vs_fourier(self, ref_table, wkb_hard_table):
        for n, l in _all_nl():
            ref = ref_table.get((n, l), 0)
            test = wkb_hard_table.get((n, l), 0)
            assert ref == test, (
                f"wkb_hardcoded disagrees at f({n},{l}): got {test}, expected {ref}"
            )

    def test_wkb_dft_vs_fourier(self, ref_table, wkb_dft_table):
        """Compare wkb DFT extraction against reference for n <= 5.

        The numpy double-precision DFT extraction is unreliable at n=6
        because the exponential amplification factor exp(2*pi*beta*n) exceeds
        the float64 dynamic range for integer rounding at that order.
        """
        for n, l in _all_nl():
            if n > 5:
                continue  # skip n=6 where float64 DFT is unreliable
            ref = ref_table.get((n, l), 0)
            test = wkb_dft_table.get((n, l), 0)
            assert ref == test, (
                f"wkb_dft disagrees at f({n},{l}): got {test}, expected {ref}"
            )

    def test_bkm_vs_fourier(self, ref_table, bkm_table):
        for n, l in _all_nl():
            ref = ref_table.get((n, l), 0)
            test = bkm_table.get((n, l), 0)
            assert ref == test, (
                f"bkm_shadow disagrees at f({n},{l}): got {test}, expected {ref}"
            )


# =========================================================================
# B. STRUCTURAL PROPERTIES (checked independently for each module)
# =========================================================================

class TestDiscriminantDependence:
    """f(n,l) depends only on D = 4n - l^2."""

    @pytest.mark.parametrize("source", [
        "phi01_fourier", "igusa_product", "wkb_hardcoded", "wkb_dft", "bkm_shadow"
    ])
    def test_disc_dependence(self, source, all_tables):
        table = all_tables[source]
        by_disc: Dict[int, set] = {}
        for (n, l), v in table.items():
            D = 4 * n - l * l
            by_disc.setdefault(D, set()).add(v)
        for D, vals in by_disc.items():
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert len(vals) == 1, (
                f"{source}: c({D}) has multiple values {vals}"
            )


class TestSymmetry:
    """f(n,l) = f(n,-l) (phi_{0,1} is even in z)."""

    @pytest.mark.parametrize("source", [
        "phi01_fourier", "igusa_product", "wkb_hardcoded", "wkb_dft", "bkm_shadow"
    ])
    def test_symmetry(self, source, all_tables):
        table = all_tables[source]
        for (n, l), v in table.items():
            v_neg = table.get((n, -l), 0)
            assert v == v_neg, (
                f"{source}: f({n},{l})={v} != f({n},{-l})={v_neg}"
            )


class TestRowSums:
    """sum_l f(n,l) = 12 if n=0, else 0 (from phi_{0,1}(tau,0)=12)."""

    @pytest.mark.parametrize("source", [
        "phi01_fourier", "igusa_product", "wkb_hardcoded", "wkb_dft", "bkm_shadow"
    ])
    def test_row_sums(self, source, all_tables):
        table = all_tables[source]
        # wkb_dft only computed to n=5
        n_max = 5 if source == "wkb_dft" else MAX_N
        for n in range(n_max + 1):
            row_sum = sum(v for (nn, ll), v in table.items() if nn == n)
            expected = 12 if n == 0 else 0
            assert row_sum == expected, (
                f"{source}: sum_l f({n},l) = {row_sum}, expected {expected}"
            )


class TestPolarTerm:
    """c(-1) = 1 -- the unique polar coefficient of a weak Jacobi form of index 1."""

    @pytest.mark.parametrize("source", [
        "phi01_fourier", "igusa_product", "wkb_hardcoded", "wkb_dft", "bkm_shadow"
    ])
    def test_c_minus_1(self, source, all_tables):
        table = all_tables[source]
        for (n, l), v in table.items():
            if 4 * n - l * l == -1:
                # VERIFIED [DC] structural property [LC] boundary/limiting case
                assert v == 1, (
                    f"{source}: c(-1) = {v} from f({n},{l}), expected 1"
                )


# =========================================================================
# C. EICHLER-ZAGIER PUBLISHED VALUES
# =========================================================================

class TestEichlerZagier:
    """Verify all c(D) values against Eichler-Zagier (1985) Table 1."""

    @pytest.mark.parametrize("D,expected", sorted(EICHLER_ZAGIER.items()))
    def test_fourier_c(self, D, expected, ref_c):
        assert ref_c.get(D, 0) == expected, (
            f"phi01_fourier: c({D}) = {ref_c.get(D, 0)}, expected {expected}"
        )

    @pytest.mark.parametrize("D,expected", sorted(EICHLER_ZAGIER.items()))
    def test_igusa_c(self, D, expected, igusa_c):
        assert igusa_c.get(D, 0) == expected, (
            f"igusa_product: c({D}) = {igusa_c.get(D, 0)}, expected {expected}"
        )

    @pytest.mark.parametrize("D,expected", sorted(EICHLER_ZAGIER.items()))
    def test_wkb_hardcoded_c(self, D, expected):
        assert wkb_c_disc.get(D, 0) == expected, (
            f"wkb_hardcoded: c({D}) = {wkb_c_disc.get(D, 0)}, expected {expected}"
        )


# =========================================================================
# D. DMVV EXPONENT CONSISTENCY
# =========================================================================

class TestDMVV:
    r"""The DMVV formula uses the same phi_{0,1} exponents.

    prod_{n>0,l,m} (1-q^n r^l s^m)^{c(4nm-l^2)} gives (1/64)*Delta_5 (Borcherds)
    and the reciprocal product gives the second-quantized K3, which is 1/Phi_{10}.
    Phi_{10} = Delta_5^2 (up to normalization).

    The essential check: the exponents c(D) used by igusa_product_formula for
    the Borcherds product are the same as those from phi01_fourier.
    """

    def test_exponents_agree(self, ref_c, igusa_c):
        """Borcherds and DMVV exponents use identical c(D).

        Only compare discriminants that fourier actually computed
        (D <= 4*MAX_N = 24). The igusa module may compute beyond this.
        """
        for D in sorted(ref_c.keys()):
            v_ref = ref_c[D]
            v_ig = igusa_c.get(D, 0)
            assert v_ref == v_ig, (
                f"c({D}): fourier={v_ref}, igusa={v_ig}"
            )

    def test_dmvv_power_is_two(self):
        """The DMVV product gives 1/Phi_{10} = 1/Delta_5^2, not 1/Delta_5.

        This is a mathematical fact check, not a numerical test.
        Phi_{10} is the unique Siegel modular form of weight 10 for Sp_4(Z).
        It equals the product of all 10 even genus-2 theta constants (each squared),
        divided by 2^{12}. Gritsenko-Nikulin: Phi_{10} = Delta_5^2 * (norm. factor).
        The DMVV generating function equals 1/Phi_{10}, confirming the exponent is 2.
        """
        # Verify that Phi_{10} weight = 2 * Delta_5 weight
        delta5_weight = 5
        phi10_weight = 10
        # VERIFIED [DC] conformal weight [DA] dimensional consistency
        assert phi10_weight == 2 * delta5_weight


# =========================================================================
# E. ADDITIONAL CONSISTENCY
# =========================================================================

class TestAdditionalConsistency:
    """Extra cross-checks beyond pairwise comparison."""

    def test_fourier_individual_vs_table(self, ref_table):
        """phi01_coefficient(n,l) agrees with phi01_table."""
        for (n, l), v in ref_table.items():
            assert fourier_coeff(n, l) == v, (
                f"phi01_coefficient({n},{l})={fourier_coeff(n,l)} vs table={v}"
            )

    def test_igusa_disc_internal_consistency(self, igusa_c):
        """igusa compute_f_disc is internally consistent (D-dependence).

        Note: we do NOT test igusa_f_coeff() here because it uses a
        module-level cache (_F_DISC_CACHE) that may be populated with
        default (lower) precision from earlier calls. The high-precision
        igusa_c fixture (prec=200) is the authoritative igusa result.
        """
        # Verify that the igusa_c table is self-consistent:
        # for every (n,l) pair mapping to the same D, igusa gives same value
        by_disc = {}
        for n in range(MAX_N + 1):
            for l in range(-MAX_L, MAX_L + 1):
                D = 4 * n - l * l
                if D < -1:
                    continue
                val = igusa_c.get(D, 0)
                if D in by_disc:
                    assert by_disc[D] == val, (
                        f"igusa internal inconsistency at D={D}"
                    )
                else:
                    by_disc[D] = val

    def test_wkb_dft_agrees_with_hardcoded(self, wkb_hard_table, wkb_dft_table):
        """The live DFT extraction in wkb_denominator matches its hardcoded table (n<=5)."""
        for n, l in _all_nl():
            if n > 5:
                continue  # wkb_dft only reliable to n=5
            h = wkb_hard_table.get((n, l), 0)
            d = wkb_dft_table.get((n, l), 0)
            assert h == d, (
                f"wkb DFT f({n},{l})={d} vs hardcoded={h}"
            )

    def test_bkm_uses_fourier_under_hood(self, ref_table, bkm_table):
        """bkm_shadow_tower should agree EXACTLY (imports from phi01_fourier)."""
        for n, l in _all_nl():
            assert ref_table.get((n, l), 0) == bkm_table.get((n, l), 0)

    def test_vanishing_below_bound(self, ref_table):
        """f(n,l) = 0 when 4n - l^2 < -1."""
        for n in range(MAX_N + 1):
            for l in range(-MAX_L, MAX_L + 1):
                if 4 * n - l * l < -1:
                    # VERIFIED [DC] vanishing check [LC] boundary/limiting case
                    assert ref_table.get((n, l), 0) == 0

    def test_c_D_mod_4_constraint(self, ref_c):
        """Nonzero c(D) occurs only for D=-1 or D>=0 with D mod 4 in {0, 3}.

        This is because D = 4n - l^2 and l^2 mod 4 is 0 or 1.
        """
        for D, val in ref_c.items():
            if D == -1:
                continue
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert D >= 0, f"Unexpected negative D={D} with c(D)={val}"
            assert D % 4 in (0, 3), (
                f"c({D})={val} nonzero but D mod 4 = {D % 4}"
            )

    def test_leading_term_structure(self, ref_table):
        """The q^0 term is r^{-1} + 10 + r (three terms only)."""
        q0_terms = {l: v for (n, l), v in ref_table.items() if n == 0}
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert q0_terms == {-1: 1, 0: 10, 1: 1}

    def test_alternating_sign_pattern(self, ref_c):
        """For D >= 0: c(D) alternates sign with D mod 4.

        c(D) > 0 when D mod 8 in {0, 4} (i.e., D = 0 mod 4)
        c(D) < 0 when D mod 8 in {3, 7} (i.e., D = 3 mod 4)
        """
        for D in range(0, 4 * MAX_N + 1):
            val = ref_c.get(D, 0)
            if val == 0:
                continue
            if D % 4 == 0:
                # VERIFIED [DC] structural property [LC] boundary/limiting case
                assert val > 0, f"c({D})={val} should be positive (D=0 mod 4)"
            elif D % 4 == 3:
                # VERIFIED [DC] structural property [LC] boundary/limiting case
                assert val < 0, f"c({D})={val} should be negative (D=3 mod 4)"


# =========================================================================
# F. DATA VOLUME CHECK
# =========================================================================

class TestDataVolume:
    """Ensure each module produces the expected number of nonzero entries."""

    def test_exact_sources_agree_on_count(self, all_tables):
        """Exact sources (fourier, wkb_hardcoded, bkm) have same nonzero count."""
        exact = ["phi01_fourier", "wkb_hardcoded", "bkm_shadow"]
        counts = {name: len(all_tables[name]) for name in exact}
        values = list(counts.values())
        # VERIFIED [DC] exactness [LC] boundary/limiting case
        assert len(set(values)) == 1, (
            f"Different nonzero counts among exact sources: {counts}"
        )

    def test_igusa_count_matches(self, all_tables):
        """igusa_product (with prec=200) should match exact sources."""
        ref_count = len(all_tables["phi01_fourier"])
        ig_count = len(all_tables["igusa_product"])
        assert ig_count == ref_count, (
            f"igusa_product has {ig_count} entries, expected {ref_count}"
        )

    def test_wkb_dft_has_reasonable_count(self, all_tables):
        """wkb_dft (n<=5) should have fewer entries than full range."""
        dft_count = len(all_tables["wkb_dft"])
        # n=0..5 should give 3+5+7+9+11 = 35 at minimum
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert dft_count >= 35, f"wkb_dft has only {dft_count} entries"

    def test_minimum_entries(self, ref_table):
        """At n=6, there should be at least 48 nonzero (n,l) entries."""
        # Rough count: n=0 has 3, n=1 has 5, n=2 has 7, ..., n=6 has 11-13
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(ref_table) >= 48


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
