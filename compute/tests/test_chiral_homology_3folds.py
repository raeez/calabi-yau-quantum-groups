r"""Tests for chiral homology on stratified real 3-manifolds.

Manuscript references:
    en_factorization.tex:
        subsec:cfg25-analogy (surgery and state spaces)
        sec:stratified-fh-chiral (stratified FH for holomorphic curves)
        sec:chiral-homology-3folds (NEW: chiral homology on real 3-folds)

    CLAIM STATUS:
        S^3 E_inf FH: PROVED (rank 2).
        S^3 E_3 chain-level: CONJECTURAL (CY-A_3).
        Lens space E_inf: PROVED (rank 2).
        Lens space twisted sectors: CONJECTURAL.
        Sigma_g x S^1 = trace: PROVED for Heisenberg.
        Heegaard = excision: PROVED (Ayala-Francis).
        Link invariants (topological): PROVED (CFG25).
        Chiral refinement: CONJECTURAL (CY-A_3).
        Three-sector decomposition: structural.

Literature ground truth:
    [AF] Ayala-Francis arXiv:1206.5522: FH of topological manifolds.
    [AFT] Ayala-Francis-Tanaka arXiv:1706.09912: stratified FH.
    [CFG] Costello-Francis-Gwilliam: CS and factorisation homology (2024).
    [Milnor] S^3 = unit sphere in C^2, Hopf fibration S^1 -> S^3 -> S^2.
    [Saveliev] 3-manifold topology: surgery, Heegaard, lens spaces.
    [Verlinde] WZW conformal blocks: dim = (k+1)^g for su(2)_k.
    [Gottsche] chi(Hilb^n(K3)) = p_{24}(n): 1, 24, 324, 3200, 25650, ...
    Poincare duality: chi(M^3) = 0 for closed oriented 3-manifolds.
    CY inversion: g(z)*g(-z) = 1 for h1+h2+h3=0.
"""

import math

import numpy as np
import pytest
from fractions import Fraction as Fr

from compute.lib.chiral_homology_3folds import (
    # Data
    S3_DATA,
    S2_X_S1_DATA,
    T3_DATA,
    # Constructors
    lens_space_data,
    sigma_g_x_s1_data,
    # Verification
    verify_euler_zero,
    # E_inf FH
    EInfFHThreeManifold,
    # Heegaard
    HeegaardDecomposition,
    # Surgery
    SurgeryPresentation,
    s3_surgery,
    lens_space_surgery,
    s2_x_s1_surgery,
    poincare_homology_sphere_surgery,
    # Real subsectors
    RealSubsectorC3,
    # S^3
    S3ChiralHomology,
    # Lens spaces
    LensSpaceChiralHomology,
    # Product manifolds
    ProductChiralHomology,
    # E_3 bar cohomology
    E3BarCohomologyThreeManifold,
    # Link invariants
    StratifiedLinkInvariant,
    # Master summary
    chiral_homology_3folds_summary,
)


# ================================================================
# STANDARD TEST PARAMETERS
# ================================================================

# Pole-safe parameters (AP-CY28): h = (2.3, -0.7, -1.6)
# Poles of g(z) at z = -h_i = {-2.3, 0.7, 1.6}.
H1 = 2.3
H2 = -0.7
H3 = -(H1 + H2)  # = -1.6

# Pole-safe test spectral parameters
SAFE_U = 3.7


# ================================================================
# 1. 3-manifold topology: Poincare duality and Euler characteristic
# ================================================================

class TestThreeManifoldTopology:
    """Verify topological invariants of closed oriented 3-manifolds."""

    def test_s3_betti(self):
        """S^3 has Betti numbers (1, 0, 0, 1)."""
        assert S3_DATA.betti == (1, 0, 0, 1)

    def test_s3_euler_zero(self):
        """chi(S^3) = 0 (Poincare duality for closed 3-mflds)."""
        r = verify_euler_zero(S3_DATA)
        assert r["ok"]

    def test_s2_x_s1_betti(self):
        """S^2 x S^1 has Betti numbers (1, 1, 1, 1)."""
        assert S2_X_S1_DATA.betti == (1, 1, 1, 1)

    def test_s2_x_s1_euler_zero(self):
        """chi(S^2 x S^1) = 0."""
        r = verify_euler_zero(S2_X_S1_DATA)
        assert r["ok"]

    def test_t3_betti(self):
        """T^3 has Betti numbers (1, 3, 3, 1).

        Ground truth: Kunneth for T^3 = S^1 x S^1 x S^1.
        b_k(T^3) = C(3,k).
        """
        assert T3_DATA.betti == (1, 3, 3, 1)

    def test_t3_euler_zero(self):
        """chi(T^3) = 0."""
        r = verify_euler_zero(T3_DATA)
        assert r["ok"]

    @pytest.mark.parametrize("p,q", [(2, 1), (3, 1), (5, 2), (7, 3)])
    def test_lens_space_betti(self, p, q):
        """Lens spaces L(p,q) have Betti (1, 0, 0, 1) over Q.

        Ground truth: H_1(L(p,q); Z) = Z/pZ (torsion, invisible over Q).
        """
        data = lens_space_data(p, q)
        assert data.betti == (1, 0, 0, 1)

    @pytest.mark.parametrize("p,q", [(2, 1), (3, 1), (5, 2), (7, 3)])
    def test_lens_space_euler_zero(self, p, q):
        """chi(L(p,q)) = 0."""
        r = verify_euler_zero(lens_space_data(p, q))
        assert r["ok"]

    def test_lens_space_l1_is_s3(self):
        """L(1,0) = S^3."""
        data = lens_space_data(1, 0)
        assert data.name == 'S^3'

    def test_lens_space_gcd_validation(self):
        """L(6,2) should be rejected: gcd(6,2) = 2."""
        with pytest.raises(ValueError, match="gcd"):
            lens_space_data(6, 2)

    @pytest.mark.parametrize("g,expected_b1", [(0, 1), (1, 3), (2, 5), (3, 7)])
    def test_sigma_g_x_s1_betti(self, g, expected_b1):
        """Sigma_g x S^1 has b_1 = 2g+1.

        Ground truth: Kunneth formula.
        """
        data = sigma_g_x_s1_data(g)
        assert data.betti[1] == expected_b1

    @pytest.mark.parametrize("g", [0, 1, 2, 3, 5])
    def test_sigma_g_x_s1_euler_zero(self, g):
        """chi(Sigma_g x S^1) = 0."""
        r = verify_euler_zero(sigma_g_x_s1_data(g))
        assert r["ok"]

    def test_poincare_duality_all(self):
        """All 3-manifold data satisfies Poincare duality: b_k = b_{3-k}."""
        manifolds = [
            S3_DATA, S2_X_S1_DATA, T3_DATA,
            lens_space_data(2, 1), lens_space_data(7, 3),
            sigma_g_x_s1_data(0), sigma_g_x_s1_data(3),
        ]
        for m in manifolds:
            r = verify_euler_zero(m)
            assert r["poincare_duality"], f"Poincare duality fails for {m.name}"

    def test_s3_simply_connected(self):
        """S^3 is simply connected."""
        assert S3_DATA.is_simply_connected

    def test_s2_x_s1_not_simply_connected(self):
        """S^2 x S^1 is NOT simply connected (pi_1 = Z)."""
        assert not S2_X_S1_DATA.is_simply_connected

    def test_heegaard_genus_s3(self):
        """Heegaard genus of S^3 is 0."""
        assert S3_DATA.heegaard_genus == 0

    def test_heegaard_genus_s2_x_s1(self):
        """Heegaard genus of S^2 x S^1 is 1."""
        assert S2_X_S1_DATA.heegaard_genus == 1

    def test_heegaard_genus_t3(self):
        """Heegaard genus of T^3 is 3."""
        assert T3_DATA.heegaard_genus == 3

    def test_heegaard_genus_lens(self):
        """Heegaard genus of L(p,q) is 1 for all p >= 2.

        Ground truth: lens spaces are genus-1 Heegaard.
        """
        for p in [2, 3, 5, 7, 13]:
            data = lens_space_data(p, 1)
            assert data.heegaard_genus == 1, f"L({p},1) genus != 1"


# ================================================================
# 2. E_inf factorization homology on 3-manifolds
# ================================================================

class TestEInfFH:
    """Tests for E_inf factorization homology ranks."""

    def test_s3_rank1_rank_2(self):
        """int_{S^3} H_1 has rank 2 (b_0 + b_3 = 1 + 1)."""
        fh = EInfFHThreeManifold(S3_DATA, 1)
        assert fh.fh_rank == 2

    def test_s3_rank24_rank_48(self):
        """int_{S^3} H_Muk has rank 48 (24 * 2)."""
        fh = EInfFHThreeManifold(S3_DATA, 24)
        assert fh.fh_rank == 48

    def test_s2_x_s1_rank1_rank_4(self):
        """int_{S^2 x S^1} H_1 has rank 4 (1+1+1+1)."""
        fh = EInfFHThreeManifold(S2_X_S1_DATA, 1)
        assert fh.fh_rank == 4

    def test_t3_rank1_rank_8(self):
        """int_{T^3} H_1 has rank 8 (1+3+3+1)."""
        fh = EInfFHThreeManifold(T3_DATA, 1)
        assert fh.fh_rank == 8

    def test_t3_rank24_rank_192(self):
        """int_{T^3} H_Muk has rank 192 (24 * 8)."""
        fh = EInfFHThreeManifold(T3_DATA, 24)
        assert fh.fh_rank == 192

    @pytest.mark.parametrize("p", [2, 3, 5, 7])
    def test_lens_space_rank_2(self, p):
        """int_{L(p,1)} H_1 has rank 2 (torsion invisible over Q)."""
        fh = EInfFHThreeManifold(lens_space_data(p, 1), 1)
        assert fh.fh_rank == 2

    @pytest.mark.parametrize("g,expected", [(0, 4), (1, 8), (2, 12)])
    def test_sigma_g_x_s1_rank(self, g, expected):
        """int_{Sigma_g x S^1} H_1 has rank 2(2g+1) + 2.

        Betti of Sigma_g x S^1: (1, 2g+1, 2g+1, 1), total = 4g+4.
        """
        fh = EInfFHThreeManifold(sigma_g_x_s1_data(g), 1)
        expected_rank = 4 * g + 4
        assert fh.fh_rank == expected_rank

    def test_graded_ranks_s3(self):
        """Graded ranks of int_{S^3} H_1: degree 0 and 3 contribute."""
        fh = EInfFHThreeManifold(S3_DATA, 1)
        graded = fh.fh_graded_ranks()
        assert graded == {0: 1, 1: 0, 2: 0, 3: 1}


# ================================================================
# 3. Heegaard decomposition and state spaces
# ================================================================

class TestHeegaardDecomposition:
    """Tests for Heegaard decomposition and conformal block dimensions."""

    def test_s3_genus_0(self):
        """S^3 has Heegaard genus 0: gluing along S^2."""
        hd = HeegaardDecomposition(S3_DATA)
        assert hd.genus == 0

    def test_heisenberg_block_dim_1(self):
        """Heisenberg conformal block is 1-dim at all genera.

        Ground truth: abelian theories have 1 block at every genus.
        """
        for data in [S3_DATA, S2_X_S1_DATA, T3_DATA]:
            hd = HeegaardDecomposition(data)
            assert hd.heisenberg_block_dim(level=1) == 1

    def test_wzw_su2_verlinde(self):
        """WZW su(2)_k at genus g has (k+1)^g blocks (Verlinde formula).

        Ground truth: Verlinde (1988).
        """
        hd = HeegaardDecomposition(S2_X_S1_DATA)  # genus 1
        assert hd.heisenberg_block_dim(level=2) == 3  # (2+1)^1 = 3
        assert hd.heisenberg_block_dim(level=3) == 4  # (3+1)^1 = 4

    def test_s3_partition_function(self):
        """Z(S^3) = 1 for the Heisenberg."""
        hd = HeegaardDecomposition(S3_DATA)
        pf = hd.partition_function_heisenberg()
        assert pf["Z_heisenberg"] == Fr(1)

    def test_state_space_en_level(self):
        """State space at Heegaard surface is E_1 (from R direction)."""
        hd = HeegaardDecomposition(S3_DATA)
        ss = hd.state_space_description()
        assert ss["en_level"] == 1


# ================================================================
# 4. Surgery presentations
# ================================================================

class TestSurgeryPresentation:
    """Tests for surgery presentations of 3-manifolds."""

    def test_s3_empty_surgery(self):
        """S^3 is the empty surgery (no components)."""
        sp = s3_surgery()
        assert sp.resulting_manifold() == 'S^3'
        assert sp.num_components == 0

    def test_lens_space_surgery(self):
        """L(5,1) = 5-surgery on the unknot."""
        sp = lens_space_surgery(5)
        assert sp.resulting_manifold() == 'L(5,1)'
        assert sp.num_components == 1

    def test_s2_x_s1_zero_surgery(self):
        """S^2 x S^1 = 0-surgery on the unknot."""
        sp = s2_x_s1_surgery()
        assert sp.resulting_manifold() == 'S^2 x S^1'

    def test_surgery_boundary_count(self):
        """Number of boundary tori = number of surgery components."""
        sp = SurgeryPresentation([(3, 1), (5, 1)], "two-component link")
        assert sp.boundary_algebras_count() == 2

    def test_poincare_sphere_surgery(self):
        """Poincare homology sphere = +1-surgery on left trefoil."""
        sp = poincare_homology_sphere_surgery()
        assert sp.num_components == 1
        assert sp.coefficients == [(1, 1)]

    def test_excision_description(self):
        """Excision description has correct structure."""
        sp = lens_space_surgery(7)
        desc = sp.excision_description()
        assert desc["resulting_manifold"] == "L(7,1)"
        assert desc["boundary_tori"] == 1

    def test_linking_matrix_single(self):
        """Single-component surgery has 1x1 linking matrix."""
        sp = lens_space_surgery(5)
        L = sp.linking_matrix
        assert L.shape == (1, 1)
        assert L[0, 0] == 5


# ================================================================
# 5. Real subsectors of C^3
# ================================================================

class TestRealSubsectors:
    """Tests for the three real 3-dimensional subsectors of C^3."""

    def test_all_dim_3(self):
        """All three subsectors have real dimension 3."""
        r = RealSubsectorC3.verify_dimensions()
        assert r["ok"]

    def test_r3_topological(self):
        """R^3 subsector gives topological CS."""
        data = RealSubsectorC3.get_subsector('R3')
        assert data['theory'] == 'topological Chern-Simons'
        assert data['en_level'] == 3
        assert data['status'] == 'PROVED (CFG25)'

    def test_cxr_holomorphic_topological(self):
        """C x R subsector gives 3d N=2 (E_1-chiral bialgebra)."""
        data = RealSubsectorC3.get_subsector('CxR')
        assert data['en_level'] == 1
        assert 'E_1-chiral' in data['output']

    def test_s3_cy_framing(self):
        """S^3 subsector gives CY_3 framing data (CONJECTURAL)."""
        data = RealSubsectorC3.get_subsector('S3')
        assert 'CONJECTURAL' in data['status']
        assert data['en_level'] == 3

    def test_three_subsectors_total(self):
        """Exactly three subsectors."""
        all_ss = RealSubsectorC3.all_subsectors()
        assert len(all_ss) == 3
        assert set(all_ss.keys()) == {'R3', 'CxR', 'S3'}

    def test_unknown_subsector_raises(self):
        """Requesting unknown subsector raises ValueError."""
        with pytest.raises(ValueError, match="Unknown subsector"):
            RealSubsectorC3.get_subsector('C3')


# ================================================================
# 6. S^3 chiral homology
# ================================================================

class TestS3ChiralHomology:
    """Tests for the S^3 factorization homology (CY-A_3 framing)."""

    def test_einf_rank_2(self):
        """E_inf FH on S^3 has rank 2."""
        s3 = S3ChiralHomology(H1, H2, H3)
        r = s3.verify_einf_computation()
        assert r["ok"]

    def test_einf_graded_correct(self):
        """Graded ranks: degree 0 and degree 3 each contribute 1."""
        s3 = S3ChiralHomology(H1, H2, H3)
        graded = s3.einf_graded_ranks(1)
        assert graded == {0: 1, 3: 1}

    def test_mukai_einf_rank_48(self):
        """E_inf FH on S^3 for H_Muk has rank 48."""
        s3 = S3ChiralHomology(H1, H2, H3)
        r = s3.verify_mukai_einf()
        assert r["ok"]

    def test_hopf_s2_contribution(self):
        """S^2 factor of Hopf has E_inf rank 2."""
        s3 = S3ChiralHomology(H1, H2, H3)
        s2 = s3.hopf_decomposition_s2_contribution()
        assert s2["einf_rank"] == 2
        assert s2["betti"] == (1, 0, 1)

    def test_hopf_s1_contribution(self):
        """S^1 factor contributes Connes B-operator."""
        s3 = S3ChiralHomology(H1, H2, H3)
        s1 = s3.hopf_decomposition_s1_contribution()
        assert s1["operation"] == "Connes B-operator"
        assert s1["grading"] == "+1 (degree raising)"

    def test_hopf_obstruction(self):
        """Hopf obstruction: topological component vanishes (PROVED)."""
        s3 = S3ChiralHomology(H1, H2, H3)
        obs = s3.hopf_obstruction_class()
        assert obs["euler_class"] == 1
        assert obs["components"]["topological"]["value"] == 0
        assert obs["components"]["topological"]["status"] == "PROVED"

    def test_hopf_bv_obstruction_conjectural(self):
        """BV obstruction is the hard part (CONJECTURAL)."""
        s3 = S3ChiralHomology(H1, H2, H3)
        obs = s3.hopf_obstruction_class()
        assert obs["components"]["bv"]["status"] == "CONJECTURAL (the hard part)"


# ================================================================
# 7. Lens space chiral homology
# ================================================================

class TestLensSpaceChiralHomology:
    """Tests for lens space chiral homology and orbifold structure."""

    def test_rp3_einf_rank_2(self):
        """int_{RP^3} H_1 has rank 2 (E_inf, over Q)."""
        ls = LensSpaceChiralHomology(2, 1, H1, H2, H3)
        r = ls.verify_einf_rank()
        assert r["ok"]

    @pytest.mark.parametrize("p", [2, 3, 5, 7, 11, 13])
    def test_all_lens_einf_rank_2(self, p):
        """All lens spaces have E_inf FH rank 2 over Q."""
        ls = LensSpaceChiralHomology(p, 1, H1, H2, H3)
        assert ls.einf_rank() == 2

    @pytest.mark.parametrize("p,expected_twisted", [
        (2, 1), (3, 2), (5, 4), (7, 6), (11, 10),
    ])
    def test_twisted_sector_count(self, p, expected_twisted):
        """L(p,q) has p-1 twisted sectors.

        Ground truth: Z_p orbifold has p-1 nontrivial sectors.
        """
        ls = LensSpaceChiralHomology(p, 1, H1, H2, H3)
        r = ls.verify_twisted_sector_count()
        assert r["ok"]
        assert r["num_twisted"] == expected_twisted

    def test_twisted_phases_on_circle(self):
        """Twisted sector phases lie on the unit circle."""
        ls = LensSpaceChiralHomology(5, 2, H1, H2, H3)
        phases = ls.twisted_sector_phases()
        assert len(phases) == 4  # p-1 = 4
        for ph in phases:
            assert abs(abs(ph) - 1.0) < 1e-12

    def test_twisted_phases_are_roots_of_unity(self):
        """Phases are p-th roots of unity (omega^k for k=1,...,p-1)."""
        p = 5
        ls = LensSpaceChiralHomology(p, 1, H1, H2, H3)
        phases = ls.twisted_sector_phases()
        for k, ph in enumerate(phases, 1):
            expected = np.exp(2j * np.pi * k / p)
            assert abs(ph - expected) < 1e-12

    def test_kummer_connection_rp3(self):
        """L(2,1) = RP^3 connects to Kummer construction."""
        ls = LensSpaceChiralHomology(2, 1, H1, H2, H3)
        kc = ls.kummer_connection()
        assert kc is not None
        assert kc["num_singularities"] == 16
        assert kc["twisted_conformal_weight"] == Fr(1, 2)
        assert kc["total_twisted"] == 16

    def test_kummer_connection_none_for_other(self):
        """Kummer connection is None for p != 2."""
        ls = LensSpaceChiralHomology(5, 1, H1, H2, H3)
        assert ls.kummer_connection() is None

    def test_orbifold_partition_function(self):
        """Orbifold PF for Heisenberg is 1 (trivial Z_p action)."""
        ls = LensSpaceChiralHomology(3, 1, H1, H2, H3)
        opf = ls.orbifold_partition_function()
        assert opf["heisenberg_Z"] == Fr(1)

    def test_lens_space_validation(self):
        """L(1, q) raises error since p must be >= 2."""
        with pytest.raises(ValueError):
            LensSpaceChiralHomology(1, 0)


# ================================================================
# 8. Product manifolds: Sigma_g x S^1
# ================================================================

class TestProductChiralHomology:
    """Tests for chiral homology on product 3-manifolds Sigma_g x S^1."""

    def test_genus_0_block_dim_1(self):
        """Genus-0 conformal block is 1-dimensional (vacuum)."""
        pm = ProductChiralHomology(0, "heisenberg", 24)
        r = pm.verify_genus_0()
        assert r["ok"]

    def test_genus_0_trace_1(self):
        """Trace of identity on 1-dim block = 1."""
        pm = ProductChiralHomology(0, "heisenberg", 24)
        assert pm.trace_of_identity() == Fr(1)

    def test_genus_1_character(self):
        """Genus-1 character matches 1/eta^{24} at q=0.1.

        Ground truth: Gottsche formula for chi(Hilb^n(K3)).
        """
        pm = ProductChiralHomology(1, "heisenberg", 24)
        r = pm.verify_genus_1_character(q_val=0.1)
        assert r["ok"], f"Character mismatch: {r}"

    def test_genus_1_character_small_q(self):
        """Genus-1 character converges for small |q|."""
        pm = ProductChiralHomology(1, "heisenberg", 24)
        r = pm.verify_genus_1_character(q_val=0.01)
        assert r["ok"]

    def test_genus_1_coefficients(self):
        """24-coloured partition numbers are correct.

        Ground truth (OEIS A006922, Gottsche 1990):
        p_{24}(0)=1, p_{24}(1)=24, p_{24}(2)=324,
        p_{24}(3)=3200, p_{24}(4)=25650, p_{24}(5)=176256,
        p_{24}(6)=1073720.
        """
        pm = ProductChiralHomology(1, "heisenberg", 24)
        coeffs = pm.genus_1_coefficients()
        assert coeffs[0] == 1
        assert coeffs[1] == 24
        assert coeffs[2] == 324
        assert coeffs[3] == 3200
        assert coeffs[4] == 25650
        assert coeffs[5] == 176256
        assert coeffs[6] == 1073720

    def test_genus_1_q_divergence(self):
        """Character diverges for |q| >= 1 (FM24: convergence check)."""
        pm = ProductChiralHomology(1, "heisenberg", 24)
        with pytest.raises(ValueError, match="diverges"):
            pm.genus_1_character(1.0)

    def test_genus_2_block_dim(self):
        """Genus-2 Heisenberg block is still 1-dimensional."""
        pm = ProductChiralHomology(2, "heisenberg", 24)
        assert pm.conformal_block_dim == 1


# ================================================================
# 9. E_3 bar cohomology on 3-manifolds
# ================================================================

class TestE3BarCohomology:
    """Tests for E_3 bar cohomology dimensions, by shadow class."""

    def test_s3_class_g_dim_1(self):
        """E_3 bar cohomology on S^3 is 1-dim for class G.

        (1+t)^{3*0} = (1+t)^0 = 1.
        """
        bar = E3BarCohomologyThreeManifold(S3_DATA, 'G')
        r = bar.verify_s3()
        assert r["ok"]

    @pytest.mark.parametrize("cls", ['G', 'L', 'C'])
    def test_s3_all_finite_classes(self, cls):
        """S^3 E_3 bar = 1-dim for all finite shadow classes."""
        bar = E3BarCohomologyThreeManifold(S3_DATA, cls)
        assert bar.bar_cohomology_total_dim() == 1

    def test_s2_x_s1_class_l_polynomial(self):
        """E_3 bar on S^2 x S^1, class L: (1+t)^3 = 1 + 3t + 3t^2 + t^3."""
        bar = E3BarCohomologyThreeManifold(S2_X_S1_DATA, 'L')
        poly = bar.bar_cohomology_polynomial()
        assert poly == [1, 3, 3, 1]

    def test_s2_x_s1_class_l_total_dim_8(self):
        """Total dim of E_3 bar on S^2 x S^1, class L: 2^3 = 8."""
        bar = E3BarCohomologyThreeManifold(S2_X_S1_DATA, 'L')
        assert bar.bar_cohomology_total_dim() == 8

    def test_s2_x_s1_class_c_same_as_l(self):
        """Class C has same bar cohomology as class L (charge conservation).

        AP-CY21: charge conservation kills d_4 for class C,
        giving the same (1+t)^{3g} as class L.
        """
        bar_l = E3BarCohomologyThreeManifold(S2_X_S1_DATA, 'L')
        bar_c = E3BarCohomologyThreeManifold(S2_X_S1_DATA, 'C')
        assert bar_l.bar_cohomology_polynomial() == bar_c.bar_cohomology_polynomial()

    def test_class_m_infinite(self):
        """Class M has infinite E_3 bar cohomology (AP-CY21).

        AP-CY21: d_4 survives for class M, giving infinite-dim cohomology.
        NEVER claim (1+t)^{3g} for class M.
        """
        bar = E3BarCohomologyThreeManifold(S2_X_S1_DATA, 'M')
        assert bar.bar_cohomology_polynomial() is None
        assert bar.bar_cohomology_total_dim() is None

    def test_t3_class_g_polynomial(self):
        """E_3 bar on T^3, class G: (1+t)^9 (Heegaard genus 3)."""
        bar = E3BarCohomologyThreeManifold(T3_DATA, 'G')
        poly = bar.bar_cohomology_polynomial()
        assert len(poly) == 10  # degree 0 through 9
        # (1+t)^9 coefficients: C(9,k)
        for k in range(10):
            assert poly[k] == math.comb(9, k)

    def test_t3_total_dim(self):
        """Total dim on T^3: 2^9 = 512."""
        bar = E3BarCohomologyThreeManifold(T3_DATA, 'G')
        assert bar.bar_cohomology_total_dim() == 512

    def test_invalid_shadow_class(self):
        """Invalid shadow class raises ValueError."""
        with pytest.raises(ValueError, match="Shadow class"):
            E3BarCohomologyThreeManifold(S3_DATA, 'X')


# ================================================================
# 10. Link invariants from stratified chiral homology
# ================================================================

class TestStratifiedLinkInvariant:
    """Tests for link invariants from stratified chiral homology on M^3."""

    def test_unknot_is_1(self):
        """Unknot invariant = 1."""
        li = StratifiedLinkInvariant(H1, H2, H3)
        r = li.verify_unknot()
        assert r["ok"]

    def test_hopf_link_cy_inversion(self):
        """Hopf link charge-1 S-matrix = 1 (CY inversion g(u)*g(-u) = 1)."""
        li = StratifiedLinkInvariant(H1, H2, H3)
        r = li.verify_hopf_link_cy_inversion(u=SAFE_U)
        assert r["ok"]

    def test_hopf_link_multiple_u(self):
        """CY inversion at multiple spectral parameters (multi-path AP10)."""
        li = StratifiedLinkInvariant(H1, H2, H3)
        for u in [0.5, 1.1, 3.0, 4.5]:
            r = li.verify_hopf_link_cy_inversion(u=u)
            assert r["ok"], f"CY inversion failed at u={u}"

    def test_hopf_link_complex_u(self):
        """CY inversion with complex spectral parameter."""
        li = StratifiedLinkInvariant(H1, H2, H3)
        r = li.verify_hopf_link_cy_inversion(u=0.3 + 0.7j)
        assert r["ok"]

    def test_topological_limit_cy_condition(self):
        """Topological limit preserves h_1 + h_2 + h_3 = 0."""
        li = StratifiedLinkInvariant(H1, H2, H3)
        r = li.verify_topological_limit()
        assert r["ok"]

    def test_topological_limit_kappa_nonzero(self):
        """Topological limit has nonzero kappa."""
        li = StratifiedLinkInvariant(H1, H2, H3)
        params = li.topological_limit(0.5)
        assert abs(params["kappa"]) > 1e-12

    def test_hopf_link_alternative_params(self):
        """CY inversion with alternative parameters (multi-path AP10)."""
        li = StratifiedLinkInvariant(3.1, -1.2, -1.9)
        r = li.verify_hopf_link_cy_inversion(u=2.5)
        assert r["ok"]


# ================================================================
# 11. Cross-engine consistency checks
# ================================================================

class TestCrossEngineConsistency:
    """Cross-checks with other engines for consistency."""

    def test_s3_rank_matches_handle_engine(self):
        """S^3 E_inf rank 2 matches handle_decomposition_fh convention.

        S^3 has Betti (1, 0, 0, 1), dim H_* = 2.
        """
        fh = EInfFHThreeManifold(S3_DATA, 1)
        assert fh.betti_rank == 2

    def test_t3_betti_matches_known(self):
        """T^3 Betti (1,3,3,1) is consistent with T^3 = T^2 x S^1.

        Ground truth: b_k(T^n) = C(n,k).
        For T^3: C(3,0)=1, C(3,1)=3, C(3,2)=3, C(3,3)=1.
        """
        for k in range(4):
            assert T3_DATA.betti[k] == math.comb(3, k)

    def test_kummer_connection_16_singularities(self):
        """Kummer has 16 A_1 singularities, matching prop:kummer-orbifold.

        Ground truth: T^4/Z_2 has 2^4 = 16 fixed points.
        """
        ls = LensSpaceChiralHomology(2, 1, H1, H2, H3)
        kc = ls.kummer_connection()
        assert kc["num_singularities"] == 16

    def test_gottsche_p24_coefficients(self):
        """Gottsche numbers p_{24}(n) match OEIS A006922.

        Direct computation: p_{24}(n) = coefficient of q^n in
        prod_{k>=1} (1-q^k)^{-24}.
        """
        pm = ProductChiralHomology(1, "heisenberg", 24)
        coeffs = pm.genus_1_coefficients()
        # Cross-check: compute directly via power series
        max_n = 6
        N_trunc = 50
        # Initialize coefficient array
        a = np.zeros(max_n + 1)
        a[0] = 1.0
        for k in range(1, N_trunc + 1):
            # Multiply by (1 - q^k)^{-24} = sum_{j>=0} C(j+23,23) q^{jk}
            new_a = np.zeros(max_n + 1)
            for n in range(max_n + 1):
                for j in range(n // k + 1) if k > 0 else [0]:
                    if n - j * k >= 0:
                        new_a[n] += a[n - j * k] * math.comb(j + 23, 23)
            a = new_a
        for n in range(max_n + 1):
            assert abs(a[n] - coeffs[n]) < 0.5, \
                f"p_{{24}}({n}): engine={coeffs[n]}, direct={a[n]}"


# ================================================================
# 12. AP compliance tests
# ================================================================

class TestAPCompliance:
    """Tests for anti-pattern compliance."""

    def test_ap_cy6_s3_conjectural(self):
        """AP-CY6: S^3 E_3 chain-level is CONJECTURAL (CY-A_3)."""
        s3 = S3ChiralHomology(H1, H2, H3)
        obs = s3.hopf_obstruction_class()
        assert obs["e3_obstruction"] == "OPEN (CY-A_3)"

    def test_ap_cy21_class_m_not_finite(self):
        """AP-CY21: NEVER claim (1+t)^{3g} for class M."""
        bar = E3BarCohomologyThreeManifold(S2_X_S1_DATA, 'M')
        assert bar.bar_cohomology_polynomial() is None

    def test_ap_cy32_reorganisation_not_bypass(self):
        """AP-CY32: S^3 FH reorganises CY-A_3, does NOT bypass.

        The S^3 subsector status must be CONJECTURAL.
        """
        data = RealSubsectorC3.get_subsector('S3')
        assert 'CONJECTURAL' in data['status']

    def test_ap113_kappa_subscripted(self):
        """AP113: kappa in code comments/docstrings should be subscripted.

        We verify that the engine uses kappa (= h1*h2*h3) as a
        computation variable, not as a bare physics claim.
        The physics claims use kappa_ch, kappa_BKM, etc.
        """
        # Structural test: the engine computes kappa = h1*h2*h3
        s3 = S3ChiralHomology(H1, H2, H3)
        expected_kappa = H1 * H2 * H3
        assert abs(s3.kappa - expected_kappa) < 1e-12

    def test_ap154_two_e3_distinguished(self):
        """AP154: algebraic E_3 (Deligne) vs topological E_3 (config space).

        The R^3 subsector uses topological E_3.
        The C^3/S^3 subsector uses algebraic E_3 (from hCS).
        """
        r3 = RealSubsectorC3.get_subsector('R3')
        s3 = RealSubsectorC3.get_subsector('S3')
        assert r3['theory'] == 'topological Chern-Simons'
        assert s3['theory'] == 'S^3-framing of CY_3 category'


# ================================================================
# 13. Master summary
# ================================================================

class TestMasterSummary:
    """Test the master summary function."""

    def test_summary_all_ok(self):
        """Master summary passes all checks."""
        r = chiral_homology_3folds_summary(H1, H2, H3)
        assert r["all_ok"], f"Summary failed: {[k for k, v in r.items() if isinstance(v, dict) and not v.get('ok', True)]}"

    def test_summary_alternative_params(self):
        """Master summary passes with alternative parameters (multi-path)."""
        r = chiral_homology_3folds_summary(3.1, -1.2, -1.9)
        assert r["all_ok"]
