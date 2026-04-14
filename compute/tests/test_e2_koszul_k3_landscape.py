"""Tests for E_2-chiral Koszul duality across the K3 landscape.

Verifies the E_2 bar complex, Koszul dual, and landscape data for:
  (i)   Generic K3 (H_Muk, rank 24, class G)
  (ii)  Kummer K3 (H_Muk, class G)
  (iii) Fermat quartic K3 (H_Muk, class G)
  (iv)  A_1 singular K3 (V_1(sl_2) tensor H_21, class L)
  (v)   E_8 x E_8 K3 (V_1(e_8)^2 tensor H_8, class G)

SIX CLAIMS verified:
  (1) Both E_2 bar differentials vanish for class G (d_X = d_Y = 0)
  (2) Bigraded dimension = tau_{2r}(n) = [q^n] P(q)^{2r}
  (3) Koszul dual has reversed braiding and negated kappa
  (4) Kappa complementarity: kappa_ch + kappa_ch^! = 0 for all K3
  (5) E_2 -> E_3 promotion: P(q)^{72} from P(q)^{48} via convolution
  (6) ADE enhancement landscape: all conductors = 0 at level 1

Multi-path verification:
  Path 1: Recursive multipartition_count
  Path 2: Independent generating function convolution
  Path 3: Rank-1 cross-check against e2_koszul_heisenberg.py
  Path 4: E_3 = E_2 * E_1 convolution factorization
  Path 5: ADE Koszul dual level computation

Manuscript references:
  chapters/theory/e2_chiral_algebras.tex: Theorem thm:e2-koszul-heisenberg
  chapters/examples/derived_categories_cy.tex: subsec:k3-mirror-koszul
  chapters/connections/modular_koszul_bridge.tex: thm:cy-complementarity-d2
"""

import pytest
from fractions import Fraction

from compute.lib.e2_koszul_k3_landscape import (
    # Constants
    RANK,
    SIG_PLUS,
    SIG_MINUS,
    KAPPA_CH_K3,
    KAPPA_CH_K3_DUAL,
    E2_BAR_POWER,
    E2_BAR_BETTI_DIM,
    E3_BAR_POWER,
    # Core functions
    multipartition_count,
    multipartition_generating_function,
    # E_2 bar complex
    E2BarRankR,
    # K3 landscape
    K3ChiralAlgebra,
    generic_k3,
    kummer_k3,
    fermat_k3,
    a1_singular_k3,
    e8_k3,
    k3_landscape,
    STANDARD_K3_ALGEBRAS,
    # Landscape computations
    e2_bar_data_k3,
    e2_bar_landscape,
    # ADE enhancements
    ADEEnhancement,
    ADE_DATA,
    ade_enhancement,
    ade_koszul_landscape,
    # E_2 -> E_3 promotion
    e2_to_e3_promotion_data,
    # Cross-checks
    verify_rank1_consistency,
    verify_generating_function_consistency,
    # Full pipeline
    full_landscape_verification,
)
from compute.lib.e2_koszul_heisenberg import (
    TAU_2_GROUND_TRUTH,
    tau_2,
)
from compute.lib.holomorphic_cs_chiral_engine import _partition_count


# =========================================================================
# 1. Multipartition count basic correctness
# =========================================================================

class TestMultipartitionCount:
    """tau_k(n) = [q^n] P(q)^k: the k-component multipartition count."""

    def test_tau_1_is_partition_function(self):
        """tau_1(n) = p(n) (ordinary partition count)."""
        for n in range(12):
            assert multipartition_count(n, 1) == _partition_count(n)

    def test_tau_2_matches_oeis_a000712(self):
        """tau_2(n) matches OEIS A000712 ground truth."""
        for n, expected in enumerate(TAU_2_GROUND_TRUTH):
            assert multipartition_count(n, 2) == expected, \
                f"tau_2({n}) = {multipartition_count(n, 2)}, expected {expected}"

    def test_tau_2_matches_rank1_engine(self):
        """tau_2(n) from multipartition_count matches tau_2() standalone."""
        for n in range(10):
            assert multipartition_count(n, 2) == tau_2(n)

    def test_tau_k_at_0(self):
        """tau_k(0) = 1 for all k (empty multipartition)."""
        for k in [1, 2, 3, 24, 48, 72]:
            assert multipartition_count(0, k) == 1

    def test_tau_k_at_1(self):
        """tau_k(1) = k (one box in any of k slots)."""
        for k in [1, 2, 3, 5, 24, 48]:
            assert multipartition_count(1, k) == k

    def test_tau_k_at_2(self):
        """tau_k(2) = k*p(2) + C(k,2)*p(1)^2 = 2k + k(k-1)/2.

        At n=2: either both boxes in one component (k choices, p(2)=2 each)
        or one box in each of 2 components (C(k,2) choices, p(1)^2=1 each).
        Total = 2k + k(k-1)/2.
        """
        for k in [1, 2, 3, 5, 24, 48]:
            expected = 2 * k + k * (k - 1) // 2
            assert multipartition_count(2, k) == expected, \
                f"tau_{k}(2) = {multipartition_count(2, k)}, expected {expected}"

    def test_tau_negative_n(self):
        """tau_k(n) = 0 for n < 0."""
        for k in [1, 2, 48]:
            assert multipartition_count(-1, k) == 0
            assert multipartition_count(-5, k) == 0

    def test_hierarchy_tau_k_monotone_in_k(self):
        """tau_k(n) <= tau_{k+1}(n) for all n >= 0.

        More components => more multipartitions.
        """
        for n in range(8):
            for k in [1, 2, 3, 5]:
                assert multipartition_count(n, k) <= multipartition_count(n, k + 1), \
                    f"tau_{k}({n}) > tau_{k+1}({n})"


# =========================================================================
# 2. Generating function cross-check
# =========================================================================

class TestGeneratingFunctionCrossCheck:
    """Independent P(q)^k computation matches recursive multipartition_count."""

    def test_rank1_gf(self):
        """P(q)^2 coefficients match tau_2."""
        gf = multipartition_generating_function(2, 10)
        for n in range(10):
            assert gf[n] == tau_2(n)

    def test_rank24_gf_small(self):
        """P(q)^{48} coefficients match at small n."""
        gf = multipartition_generating_function(48, 3)
        for n in range(4):
            assert gf[n] == multipartition_count(n, 48), \
                f"P(q)^48 at n={n}: gf={gf[n]}, rec={multipartition_count(n, 48)}"

    def test_rank_3_gf(self):
        """P(q)^6 matches for rank 3."""
        gf = multipartition_generating_function(6, 8)
        for n in range(9):
            assert gf[n] == multipartition_count(n, 6)

    def test_verify_generating_function_consistency_rank1(self):
        """The verify function passes for rank 1."""
        result = verify_generating_function_consistency(1, 8)
        assert result["all_match"]

    def test_verify_generating_function_consistency_rank3(self):
        """The verify function passes for rank 3."""
        result = verify_generating_function_consistency(3, 5)
        assert result["all_match"]


# =========================================================================
# 3. E_2 bar complex for rank-r Heisenberg
# =========================================================================

class TestE2BarRankR:
    """B_{E_2}(H_{r,omega}) for the rank-r Heisenberg."""

    def setup_method(self):
        """Create the K3 Mukai Heisenberg (rank 24, signature (4,20))."""
        self.mukai = E2BarRankR(
            rank=RANK, sig_plus=SIG_PLUS, sig_minus=SIG_MINUS,
            kappa_ch=KAPPA_CH_K3,
        )

    def test_signature(self):
        assert self.mukai.signature == (4, 20)
        assert self.mukai.rank == 24

    def test_shadow_class_G(self):
        assert self.mukai.shadow_class == "G"
        assert self.mukai.shadow_depth == 2

    def test_e2_bar_power(self):
        """E_2 bar power = 2 * 24 = 48."""
        assert self.mukai.e2_bar_power == 48

    def test_e3_bar_power(self):
        """E_3 bar power = 3 * 24 = 72."""
        assert self.mukai.e3_bar_power == 72

    def test_betti_dimension(self):
        """Betti dimension = 2^{48}."""
        assert self.mukai.betti_dimension == 2 ** 48

    def test_differentials_vanish(self):
        assert self.mukai.differentials_vanish()

    def test_bigraded_dimension_n0(self):
        """B_{E_2}(H_Muk)_0 = 1."""
        assert self.mukai.bigraded_dimension(0) == 1

    def test_bigraded_dimension_n1(self):
        """B_{E_2}(H_Muk)_1 = 48 (one box in any of 48 multipartition slots)."""
        assert self.mukai.bigraded_dimension(1) == 48

    def test_bigraded_dimension_n2(self):
        """B_{E_2}(H_Muk)_2 = 2*48 + C(48,2) = 96 + 1128 = 1224."""
        expected = 2 * 48 + 48 * 47 // 2
        assert expected == 1224
        assert self.mukai.bigraded_dimension(2) == 1224

    def test_per_direction_dimension_n1(self):
        """Each E_1 direction: P(q)^{24}, so dim at n=1 is 24."""
        assert self.mukai.bigraded_dimension_per_direction(1) == 24

    def test_kappa_ch(self):
        assert self.mukai.kappa_ch == Fraction(2)

    def test_kappa_ch_dual(self):
        assert self.mukai.kappa_ch_dual == Fraction(-2)

    def test_koszul_conductor_zero(self):
        assert self.mukai.koszul_conductor == Fraction(0)

    def test_kappa_complementarity(self):
        assert self.mukai.verify_kappa_complementarity()

    def test_dual_signature(self):
        """Koszul dual has negated pairing: (4,20) -> (20,4)."""
        assert self.mukai.dual_signature == (20, 4)

    def test_braiding_reversed(self):
        assert self.mukai.braiding_reversed

    def test_r_matrix_eigenvalue_counts(self):
        eig = self.mukai.r_matrix_eigenvalue_counts()
        assert eig["positive_sector"] == 4
        assert eig["negative_sector"] == 20
        assert eig["total"] == 24
        assert eig["r_at_0"] == 1  # (-1)^24 = 1
        assert eig["r_at_inf"] == 1

    def test_e3_trigraded_dimension_n0(self):
        assert self.mukai.e3_trigraded_dimension(0) == 1

    def test_e3_trigraded_dimension_n1(self):
        """E_3 bar at n=1: 72 (one box in any of 72 slots)."""
        assert self.mukai.e3_trigraded_dimension(1) == 72

    def test_e3_from_e2_convolution(self):
        """tau_{72}(n) = sum tau_{48}(m) * tau_{24}(n-m)."""
        assert self.mukai.verify_e3_from_e2_convolution(max_n=3)


# =========================================================================
# 4. Rank-1 cross-check
# =========================================================================

class TestRank1Consistency:
    """The rank-1 case must match e2_koszul_heisenberg.py exactly."""

    def test_rank1_verification(self):
        result = verify_rank1_consistency()
        assert result["all_match"]

    def test_rank1_e2bar_matches_tau2(self):
        rank1 = E2BarRankR(rank=1, sig_plus=1, sig_minus=0, kappa_ch=Fraction(1))
        for n in range(10):
            assert rank1.bigraded_dimension(n) == tau_2(n)

    def test_rank1_e2_power(self):
        rank1 = E2BarRankR(rank=1, sig_plus=1, sig_minus=0, kappa_ch=Fraction(1))
        assert rank1.e2_bar_power == 2

    def test_rank1_betti(self):
        rank1 = E2BarRankR(rank=1, sig_plus=1, sig_minus=0, kappa_ch=Fraction(1))
        assert rank1.betti_dimension == 4  # 2^2


# =========================================================================
# 5. K3 landscape: all five algebras
# =========================================================================

class TestK3Landscape:
    """All five standard K3 chiral algebras."""

    def test_landscape_has_five_entries(self):
        assert len(k3_landscape()) == 5

    def test_all_kappa_ch_equal_2(self):
        """kappa_ch = 2 for ALL K3 (CY-A_2 invariant)."""
        for alg in k3_landscape():
            assert alg.kappa_ch == Fraction(2), \
                f"{alg.name}: kappa_ch = {alg.kappa_ch}, expected 2"

    def test_all_kappa_complementarity(self):
        """kappa_ch + kappa_ch^! = 0 for all K3."""
        for alg in k3_landscape():
            assert alg.verify_kappa_complementarity(), \
                f"{alg.name}: kappa complementarity failed"

    def test_generic_is_class_G(self):
        alg = generic_k3()
        assert alg.shadow_class == "G"
        assert alg.total_rank == 24
        assert alg.e2_bar_differential_trivial

    def test_kummer_is_class_G(self):
        alg = kummer_k3()
        assert alg.shadow_class == "G"
        assert alg.total_rank == 24
        assert alg.picard_rank == 16

    def test_fermat_is_class_G(self):
        alg = fermat_k3()
        assert alg.shadow_class == "G"
        assert alg.total_rank == 24
        assert alg.picard_rank == 20

    def test_a1_is_class_L(self):
        alg = a1_singular_k3()
        assert alg.shadow_class == "L"
        assert alg.heisenberg_rank == 21
        assert alg.enhanced_rank == 3
        assert alg.total_rank == 24
        assert not alg.e2_bar_differential_trivial

    def test_e8_is_class_G(self):
        """E_8 x E_8 at level 1 is a lattice VOA (class G)."""
        alg = e8_k3()
        assert alg.shadow_class == "G"
        assert alg.heisenberg_rank == 8
        assert alg.enhanced_rank == 16
        assert alg.total_rank == 24
        assert alg.e2_bar_differential_trivial

    def test_all_total_rank_24(self):
        """Total rank = 24 for all K3 (Mukai lattice rank invariant)."""
        for alg in k3_landscape():
            assert alg.total_rank == 24, \
                f"{alg.name}: total rank = {alg.total_rank}, expected 24"


# =========================================================================
# 6. E_2 bar data for each landscape entry
# =========================================================================

class TestE2BarLandscapeData:
    """E_2 bar complex data across the landscape."""

    def test_generic_class_G_bar_data(self):
        data = e2_bar_data_k3(generic_k3(), max_n=3)
        assert data["shadow_class"] == "G"
        assert data["kappa_complementarity"]
        assert data["e2_bar_power"] == 48
        assert "e2_bar_dimensions" in data
        assert data["e2_bar_dimensions"][0] == 1
        assert data["e2_bar_dimensions"][1] == 48

    def test_a1_class_L_bar_data(self):
        data = e2_bar_data_k3(a1_singular_k3(), max_n=3)
        assert data["shadow_class"] == "L"
        assert data["kappa_complementarity"]
        assert "e2_bar_chain_dimensions" in data
        assert data["e2_bar_cohomology"] == "requires spectral sequence"

    def test_landscape_bar_data_all_kappa_ok(self):
        landscape_data = e2_bar_landscape(max_n=2)
        for entry in landscape_data:
            assert entry["kappa_complementarity"], \
                f"{entry['name']}: kappa complementarity failed"

    def test_landscape_all_braiding_reversed(self):
        landscape_data = e2_bar_landscape(max_n=2)
        for entry in landscape_data:
            assert entry["braiding_reversed"]

    def test_class_G_dimensions_match(self):
        """All class G algebras with rank 24 have the same E_2 bar dimensions."""
        class_g_entries = [
            e2_bar_data_k3(f(), max_n=3)
            for f in [generic_k3, kummer_k3, fermat_k3, e8_k3]
        ]
        ref_dims = class_g_entries[0]["e2_bar_dimensions"]
        for entry in class_g_entries[1:]:
            assert entry["e2_bar_dimensions"] == ref_dims, \
                f"{entry['name']}: dims differ from generic"

    def test_betti_dimension_generic(self):
        data = e2_bar_data_k3(generic_k3())
        assert data["betti_dimension"] == 2 ** 48


# =========================================================================
# 7. ADE enhancement landscape
# =========================================================================

class TestADEEnhancement:
    """E_2 Koszul dual data at ADE singularities."""

    def test_a1_enhancement(self):
        enh = ade_enhancement("A_1")
        assert enh.g_rank == 1
        assert enh.heisenberg_remainder == 23
        assert enh.is_lattice_voa  # level 1
        assert enh.koszul_dual_level == -1
        assert enh.shadow_class == "G"

    def test_e8_enhancement(self):
        enh = ade_enhancement("E_8")
        assert enh.g_rank == 8
        assert enh.heisenberg_remainder == 16
        assert enh.is_lattice_voa
        assert enh.koszul_dual_level == -1
        assert enh.dual_coxeter == 30

    def test_all_level1_are_lattice_voa(self):
        """At level 1, all simply-laced ADE algebras are lattice VOAs."""
        for ade_type in ADE_DATA:
            enh = ade_enhancement(ade_type, level=1)
            assert enh.is_lattice_voa, f"{ade_type} at level 1 should be lattice VOA"
            assert enh.shadow_class == "G"

    def test_all_level1_koszul_dual_level_minus_1(self):
        """At level 1 (lattice VOA), Koszul dual level = -1."""
        for ade_type in ADE_DATA:
            enh = ade_enhancement(ade_type, level=1)
            assert enh.koszul_dual_level == -1

    def test_all_kappa_ch_equal_2(self):
        """kappa_ch = 2 for all K3 ADE enhancements."""
        for ade_type in ADE_DATA:
            enh = ade_enhancement(ade_type)
            assert enh.kappa_ch == Fraction(2)

    def test_all_conductors_zero(self):
        """Koszul conductor = 0 for all K3 ADE enhancements."""
        for ade_type in ADE_DATA:
            enh = ade_enhancement(ade_type)
            assert enh.koszul_conductor == Fraction(0)

    def test_heisenberg_remainder_correct(self):
        """Heisenberg remainder = 24 - rank(g)."""
        for ade_type, d in ADE_DATA.items():
            enh = ade_enhancement(ade_type)
            assert enh.heisenberg_remainder == 24 - d["g_rank"]

    def test_ade_koszul_landscape(self):
        results = ade_koszul_landscape()
        assert len(results) == len(ADE_DATA)
        for entry in results:
            assert entry["koszul_conductor"] == Fraction(0)
            assert entry["braiding_reversed"]

    def test_level_2_is_not_lattice_voa(self):
        """At level 2, V_2(g) is NOT a lattice VOA."""
        enh = ade_enhancement("A_1", level=2)
        assert not enh.is_lattice_voa
        assert enh.shadow_class == "L"

    def test_feigin_frenkel_at_level_2(self):
        """At level 2 (class L), Koszul dual uses Feigin-Frenkel: k'=-k-2h^v."""
        enh = ade_enhancement("A_1", level=2)
        # k' = -2 - 2*2 = -6
        assert enh.koszul_dual_level == -6

    def test_unknown_ade_raises(self):
        with pytest.raises(ValueError):
            ade_enhancement("G_2")  # Not ADE


# =========================================================================
# 8. E_2 -> E_3 promotion (K3 -> K3 x E)
# =========================================================================

class TestE2ToE3Promotion:
    """The E_2 -> E_3 step via K3 -> K3 x E."""

    def test_promotion_powers(self):
        data = e2_to_e3_promotion_data(max_n=3)
        assert data["e2_power"] == 48
        assert data["e3_power"] == 72
        assert data["e1_power"] == 24

    def test_convolution_e3_from_e2(self):
        """tau_{72}(n) = sum_{m=0}^n tau_{48}(m) * tau_{24}(n-m)."""
        data = e2_to_e3_promotion_data(max_n=3)
        assert data["convolution_ok"]

    def test_e2_dims_at_n0(self):
        data = e2_to_e3_promotion_data(max_n=2)
        assert data["e2_dims"][0] == 1

    def test_e2_dims_at_n1(self):
        data = e2_to_e3_promotion_data(max_n=2)
        assert data["e2_dims"][1] == 48

    def test_e3_dims_at_n1(self):
        data = e2_to_e3_promotion_data(max_n=2)
        assert data["e3_dims"][1] == 72

    def test_betti_dimensions(self):
        data = e2_to_e3_promotion_data(max_n=2)
        assert data["e2_betti"] == 2 ** 48
        assert data["e3_betti"] == 2 ** 72

    def test_status_labels(self):
        data = e2_to_e3_promotion_data(max_n=2)
        assert "PROVED" in data["status_e2"]
        assert "CONDITIONAL" in data["status_e3"]


# =========================================================================
# 9. Mukai pairing signature effects
# =========================================================================

class TestMukaiPairingEffects:
    """The Mukai pairing affects the R-matrix but NOT the bar dimensions."""

    def test_signature_invariance_of_dimensions(self):
        """Bar dimensions depend on rank, not signature.

        Two Heisenberg algebras with the same rank but different signatures
        have the same E_2 bar dimensions (the differential is zero for both).
        """
        h_pos = E2BarRankR(rank=24, sig_plus=24, sig_minus=0, kappa_ch=Fraction(2))
        h_neg = E2BarRankR(rank=24, sig_plus=0, sig_minus=24, kappa_ch=Fraction(2))
        h_muk = E2BarRankR(rank=24, sig_plus=4, sig_minus=20, kappa_ch=Fraction(2))

        for n in range(4):
            assert h_pos.bigraded_dimension(n) == h_neg.bigraded_dimension(n) == \
                h_muk.bigraded_dimension(n)

    def test_dual_signature_swap(self):
        """The Koszul dual swaps signature: (p,q) -> (q,p)."""
        h = E2BarRankR(rank=24, sig_plus=4, sig_minus=20, kappa_ch=Fraction(2))
        assert h.dual_signature == (20, 4)

    def test_positive_definite_signature(self):
        """Positive-definite pairing: dual is negative-definite."""
        h = E2BarRankR(rank=3, sig_plus=3, sig_minus=0, kappa_ch=Fraction(1))
        assert h.dual_signature == (0, 3)

    def test_r_matrix_at_0_even_rank(self):
        """For even rank, R(0) = (-1)^{rank} = 1."""
        h = E2BarRankR(rank=24, sig_plus=4, sig_minus=20, kappa_ch=Fraction(2))
        assert h.r_matrix_eigenvalue_counts()["r_at_0"] == 1

    def test_r_matrix_at_0_odd_rank(self):
        """For odd rank, R(0) = (-1)^{rank} = -1."""
        h = E2BarRankR(rank=3, sig_plus=2, sig_minus=1, kappa_ch=Fraction(1))
        assert h.r_matrix_eigenvalue_counts()["r_at_0"] == -1


# =========================================================================
# 10. Convolution factorization
# =========================================================================

class TestConvolutionFactorization:
    """tau_{a+b}(n) = sum_{m=0}^n tau_a(m) * tau_b(n-m)."""

    def test_tau_48_from_tau_24_squared(self):
        """P(q)^{48} = P(q)^{24} * P(q)^{24}."""
        for n in range(4):
            t48 = multipartition_count(n, 48)
            conv = sum(
                multipartition_count(m, 24) * multipartition_count(n - m, 24)
                for m in range(n + 1)
            )
            assert t48 == conv, f"n={n}: tau_48={t48} != conv={conv}"

    def test_tau_72_from_tau_48_times_tau_24(self):
        """P(q)^{72} = P(q)^{48} * P(q)^{24}."""
        for n in range(3):
            t72 = multipartition_count(n, 72)
            conv = sum(
                multipartition_count(m, 48) * multipartition_count(n - m, 24)
                for m in range(n + 1)
            )
            assert t72 == conv

    def test_tau_2_from_tau_1_squared(self):
        """P(q)^2 = P(q) * P(q) (sanity check at rank 1)."""
        for n in range(10):
            t2 = multipartition_count(n, 2)
            conv = sum(
                _partition_count(m) * _partition_count(n - m)
                for m in range(n + 1)
            )
            assert t2 == conv


# =========================================================================
# 11. Kappa spectrum cross-check with k3_mirror_koszul
# =========================================================================

class TestKappaSpectrumCrossCheck:
    """Cross-check kappa values with k3_mirror_koszul.py."""

    def test_kappa_ch_matches(self):
        from compute.lib.k3_mirror_koszul import k3_kappa_spectrum
        spectrum = k3_kappa_spectrum()
        assert spectrum["kappa_ch"] == Fraction(2)
        assert KAPPA_CH_K3 == Fraction(2)

    def test_kappa_dual_matches(self):
        from compute.lib.k3_mirror_koszul import koszul_dual_kappa_k3
        assert koszul_dual_kappa_k3() == Fraction(-2)
        assert KAPPA_CH_K3_DUAL == Fraction(-2)

    def test_conductor_matches(self):
        from compute.lib.k3_mirror_koszul import koszul_conductor_k3
        assert koszul_conductor_k3() == Fraction(0)

    def test_mukai_rank_24(self):
        from compute.lib.k3_mirror_koszul import mukai_lattice_rank
        assert mukai_lattice_rank() == 24
        assert RANK == 24

    def test_mukai_signature_4_20(self):
        from compute.lib.k3_mirror_koszul import mukai_lattice_signature
        assert mukai_lattice_signature() == (4, 20)


# =========================================================================
# 12. Full landscape verification pipeline
# =========================================================================

class TestFullLandscapeVerification:
    """End-to-end verification of the E_2 Koszul K3 landscape."""

    def test_full_pipeline(self):
        result = full_landscape_verification(max_n=3)
        assert result["all_kappa_complementarity_ok"]
        assert result["all_ade_conductor_zero"]
        assert result["e2_e3_convolution_ok"]
        assert result["rank1_consistency"]["all_match"]

    def test_landscape_has_five_entries(self):
        result = full_landscape_verification(max_n=2)
        assert len(result["landscape"]) == 5

    def test_ade_landscape_has_six_entries(self):
        result = full_landscape_verification(max_n=2)
        assert len(result["ade_landscape"]) == 6  # A_1, A_2, D_4, E_6, E_7, E_8


# =========================================================================
# 13. Constants and dimensional sanity
# =========================================================================

class TestConstants:
    """Verify module-level constants."""

    def test_rank(self):
        assert RANK == 24

    def test_signature(self):
        assert SIG_PLUS == 4
        assert SIG_MINUS == 20
        assert SIG_PLUS + SIG_MINUS == RANK

    def test_e2_bar_power(self):
        assert E2_BAR_POWER == 48

    def test_e3_bar_power(self):
        assert E3_BAR_POWER == 72

    def test_e2_betti_dim(self):
        assert E2_BAR_BETTI_DIM == 2 ** 48

    def test_kappa_ch_k3(self):
        assert KAPPA_CH_K3 == Fraction(2)

    def test_kappa_ch_k3_dual(self):
        assert KAPPA_CH_K3_DUAL == Fraction(-2)

    def test_kappa_sum_zero(self):
        assert KAPPA_CH_K3 + KAPPA_CH_K3_DUAL == Fraction(0)
