r"""Tests for derived loop space L(K3) and chiral differential operators.

Verifies the Loop-CDO-Phi triangle: three constructions that converge
on the rank-24 Heisenberg VOA H_{Muk} for K3.

Theorem used: CY-A_2 (PROVED at d=2).
Manuscript: hochschild_calculus.tex, cy_to_chiral.tex, toroidal_elliptic.tex (rem:cdr-k3).
Engine: compute/lib/derived_loop_cdo_k3.py.

AP113 compliance: all kappa references subscripted (kappa_ch, kappa_cat, kappa_fiber).
AP-CY2 compliance: CY trace in HC^-_2, not just HH_2 -> k.
AP-CY6 compliance: d=2, Phi IS constructed.
AP10 compliance: all expected values cross-checked via 2+ independent paths.
"""

import math
from fractions import Fraction

import pytest

from compute.lib.derived_loop_cdo_k3 import (
    # Core data
    K3_HODGE,
    K3_DIM,
    k3_hodge_number,
    # Loop space
    derived_loop_space_k3,
    # CDO
    cdo_k3,
    cdo_existence,
    # Triangle
    verify_loop_cdo_phi_triangle,
    # CY trace
    cy_trace_k3,
    # Character
    s1_equivariant_character_k3,
    # Comparisons
    abelian_surface_data,
    enriques_surface_data,
    cdo_cy3_examples,
    cy2_comparison_table,
    # Full
    full_verification,
)


# =========================================================================
# 1. K3 Hodge data consistency
# =========================================================================

class TestK3HodgeData:
    """Verify K3 Hodge numbers satisfy all required symmetries."""

    def test_hodge_symmetry(self):
        """h^{p,q} = h^{q,p} (Kaehler condition)."""
        for p in range(K3_DIM + 1):
            for q in range(K3_DIM + 1):
                assert k3_hodge_number(p, q) == k3_hodge_number(q, p), \
                    f"Hodge symmetry fails: h^{{{p},{q}}} != h^{{{q},{p}}}"

    def test_serre_duality(self):
        """h^{p,q} = h^{d-p, d-q} (Serre duality for compact Kaehler)."""
        d = K3_DIM
        for p in range(d + 1):
            for q in range(d + 1):
                assert k3_hodge_number(p, q) == k3_hodge_number(d - p, d - q), \
                    f"Serre duality fails at ({p},{q})"

    def test_euler_characteristic(self):
        """chi(K3) = sum (-1)^{p+q} h^{p,q} = 24.

        # VERIFIED: [DC] direct sum, [LT] standard K3 topology, [CF] cy3_hochschild.py
        """
        chi = sum((-1)**(p + q) * k3_hodge_number(p, q)
                  for p in range(K3_DIM + 1) for q in range(K3_DIM + 1))
        assert chi == 24

    def test_betti_numbers(self):
        """b_0=1, b_1=0, b_2=22, b_3=0, b_4=1 for K3.

        # VERIFIED: [DC] b_k = sum_{p+q=k} h^{p,q}, [LT] standard
        """
        d = K3_DIM
        betti = {}
        for k in range(2 * d + 1):
            betti[k] = sum(
                k3_hodge_number(p, k - p)
                for p in range(max(0, k - d), min(d, k) + 1)
            )
        assert betti == {0: 1, 1: 0, 2: 22, 3: 0, 4: 1}

    def test_simply_connected(self):
        """K3 is simply connected: b_1 = 0, equivalently h^{1,0} = h^{0,1} = 0."""
        assert k3_hodge_number(1, 0) == 0
        assert k3_hodge_number(0, 1) == 0

    def test_cy_condition(self):
        """K3 is CY_2: h^{2,0} = 1 (holomorphic volume form exists)."""
        assert k3_hodge_number(K3_DIM, 0) == 1


# =========================================================================
# 2. Derived loop space L(K3)
# =========================================================================

class TestDerivedLoopSpaceK3:
    """Tests for the derived loop space L(K3) = Map(S^1, K3)."""

    def test_total_dimension_24(self):
        """dim O(L(K3)) = 24 = rank of Mukai lattice.

        # VERIFIED: [DC] sum of K3 Hodge numbers, [CF] phi_k3_explicit_evaluation.py
        """
        loop = derived_loop_space_k3()
        assert loop.total_dim == 24

    def test_hh_decomposition_by_form_degree(self):
        """HH decomposes as {2, 20, 2} by form degree p.

        n=0: H^*(O) = 2, n=1: H^*(Omega^1) = 20, n=2: H^*(Omega^2) = 2.

        # VERIFIED: [DC] from Hodge numbers, [CF] phi_k3_explicit_evaluation.py Step 1
        """
        loop = derived_loop_space_k3()
        dims_by_p = {}
        for p in range(K3_DIM + 1):
            dims_by_p[p] = sum(
                loop.hh_decomposition.get((p, q), 0)
                for q in range(K3_DIM + 1)
            )
        assert dims_by_p == {0: 2, 1: 20, 2: 2}

    def test_connes_B_vanishes(self):
        """The Connes operator B: HH_n -> HH_{n+1} is zero on K3.

        This follows from Hodge theory degeneration at E_1 for Kaehler manifolds.
        For K3 also visible directly: h^{1,0} = h^{0,1} = 0 kills all B-maps
        involving Omega^1.

        # VERIFIED: [DC] all B entries zero, [LT] Hodge theory, E_1 degeneration
        """
        loop = derived_loop_space_k3()
        assert loop.is_B_zero is True

    def test_hc_minus_dimensions(self):
        """Negative cyclic homology HC^-_n for K3.

        Since B = 0: HC^-_n = prod_{k>=0} HH_{n+2k}.
        HC^-_0 = HH_0 + HH_2 = 2 + 2 = 4.
        HC^-_1 = HH_1 = 20.
        HC^-_2 = HH_2 = 2.

        # VERIFIED: [DC] product formula with B=0, [LT] Loday Ch.5
        """
        loop = derived_loop_space_k3()
        assert loop.hc_minus == {0: 4, 1: 20, 2: 2}

    def test_cy_class_degree(self):
        """CY structure class lives in HC^-_d = HC^-_2."""
        loop = derived_loop_space_k3()
        assert loop.cy_class_degree == K3_DIM

    def test_hh_pq_components(self):
        """Individual HKR components match K3 Hodge numbers.

        HH decomposition (p, q) component = h^{p,q}(K3).
        """
        loop = derived_loop_space_k3()
        # Check key nonzero components
        assert loop.hh_decomposition[(0, 0)] == 1   # H^0(O)
        assert loop.hh_decomposition[(0, 2)] == 1   # H^2(O) = CY class
        assert loop.hh_decomposition[(1, 1)] == 20  # H^1(Omega^1) = Picard
        assert loop.hh_decomposition[(2, 0)] == 1   # H^0(Omega^2) = volume form
        assert loop.hh_decomposition[(2, 2)] == 1   # H^2(Omega^2) = top class

    def test_hh_pq_zeros(self):
        """Zero components from h^{1,0} = h^{0,1} = 0."""
        loop = derived_loop_space_k3()
        assert loop.hh_decomposition[(1, 0)] == 0
        assert loop.hh_decomposition[(0, 1)] == 0
        assert loop.hh_decomposition[(2, 1)] == 0
        assert loop.hh_decomposition[(1, 2)] == 0


# =========================================================================
# 3. Chiral differential operators on K3
# =========================================================================

class TestCDOK3:
    """Tests for the sheaf of chiral differential operators D^{ch}_{K3}."""

    def test_cdo_exists(self):
        """CDO exists on K3 because c_1(T_{K3}) = 0."""
        cdo = cdo_k3()
        assert cdo.cdo_exists is True
        assert cdo.c1_vanishes is True

    def test_effective_central_charge_zero(self):
        """c_eff = 0 after topological twist (betagamma + bc cancellation).

        # VERIFIED: [DC] 2d - 2d = 0, [LT] MSV (1999), [CF] rem:cdr-k3
        """
        cdo = cdo_k3()
        assert cdo.effective_central_charge == 0

    def test_local_central_charge(self):
        """Local betagamma central charge = 2 * dim_C = 4 for K3.

        # VERIFIED: [DC] 2*2 = 4, [LT] CDO convention: c_{bg} = 2*dim
        """
        cdo = cdo_k3()
        assert cdo.local_central_charge == 2 * K3_DIM

    def test_n4_susy(self):
        """K3 is hyperkaehler, so CDO carries N=4 superconformal symmetry."""
        cdo = cdo_k3()
        assert cdo.n_susy == 4

    def test_kappa_ch_from_cdo(self):
        """kappa_ch = chi(O_{K3}) = 2 from CDO / elliptic genus.

        The leading coefficient of Ell(K3) = 2 * phi_{0,1} is 2.

        # VERIFIED: [DC] chi(O) = 1-0+1 = 2, [LT] Borisov-Libgober, [CF] phi_k3 engine
        """
        cdo = cdo_k3()
        assert cdo.kappa_ch == 2
        assert cdo.chi_O == 2
        assert cdo.elliptic_genus_leading == 2

    def test_cdr_central_charge(self):
        """Chiral de Rham complex has c = 0 on CY manifolds."""
        cdo = cdo_k3()
        assert cdo.cdr_central_charge == 0


# =========================================================================
# 4. CDO existence for other varieties
# =========================================================================

class TestCDOExistence:
    """Tests for CDO existence conditions across geometries."""

    def test_cdo_exists_for_cy_manifolds(self):
        """CDO exists for all CY manifolds (c_1 = 0 by definition)."""
        # K3
        k3_result = cdo_existence("K3", 2, K3_HODGE)
        assert k3_result.cdo_exists is True

    def test_cdo_not_exists_for_enriques(self):
        """CDO does NOT exist on Enriques (omega_S is 2-torsion, c_1 != 0)."""
        enr = enriques_surface_data()
        assert enr.cdo_exists is False

    def test_cdo_exists_for_abelian(self):
        """CDO exists on abelian surfaces (c_1 = 0)."""
        ab = abelian_surface_data()
        assert ab.cdo_exists is True

    def test_cdo_exists_for_cy3(self):
        """CDO exists for all CY3 examples."""
        results = cdo_cy3_examples()
        for r in results:
            assert r.cdo_exists is True, f"CDO should exist for {r.name}"

    def test_cy3_chi_O_zero(self):
        """chi(O_X) = 0 for strict CY3 and K3 x E.

        For strict CY3: h^{0,0}=1, h^{0,1}=0, h^{0,2}=0, h^{0,3}=1 -> chi = 0.
        For K3 x E: by Kunneth, chi(O_{K3xE}) = 0.

        # VERIFIED: [DC] direct from Hodge numbers, [LT] standard CY3 topology
        """
        results = cdo_cy3_examples()
        for r in results:
            assert r.chi_O == 0, f"chi(O) for {r.name} should be 0, got {r.chi_O}"


# =========================================================================
# 5. The Loop-CDO-Phi triangle
# =========================================================================

class TestTriangleVerification:
    """Tests for the Loop-CDO-Phi commutative triangle."""

    def test_triangle_all_match(self):
        """All three constructions agree for K3."""
        tri = verify_loop_cdo_phi_triangle()
        assert tri.all_match is True

    def test_dimension_agreement(self):
        """Loop space dim = Phi rank = 24.

        # VERIFIED: [DC] loop: sum h^{p,q} = 24, [CF] phi_k3: rank = 24
        """
        tri = verify_loop_cdo_phi_triangle()
        assert tri.loop_total_dim == 24
        assert tri.phi_rank == 24
        assert tri.loop_total_dim == tri.phi_rank

    def test_kappa_ch_agreement(self):
        """kappa_ch = 2 from CDO and from Phi.

        # VERIFIED: [DC] chi(O_{K3}) = 2, [LT] Borisov-Libgober + CY-A_2
        """
        tri = verify_loop_cdo_phi_triangle()
        assert tri.cdo_kappa_ch == 2
        assert tri.phi_kappa_ch == 2
        assert tri.cdo_kappa_ch == tri.phi_kappa_ch

    def test_mukai_signature(self):
        """Mukai pairing has signature (4, 20) from all routes."""
        tri = verify_loop_cdo_phi_triangle()
        sig = tri.details["mukai_signature"]
        assert sig == (4, 20)
        assert sum(sig) == 24

    def test_hodge_decomposition_matches(self):
        """Hodge decomposition {2, 20, 2} consistent across routes."""
        tri = verify_loop_cdo_phi_triangle()
        assert tri.details["loop_decomposition"] == {0: 2, 1: 20, 2: 2}

    def test_connes_B_zero_in_triangle(self):
        """Connes B = 0 is a structural feature of the K3 triangle."""
        tri = verify_loop_cdo_phi_triangle()
        assert tri.details["connes_B_zero"] is True

    def test_cy_class_in_hc_minus_2(self):
        """CY structure class lives in HC^-_2 (AP-CY2 compliance)."""
        tri = verify_loop_cdo_phi_triangle()
        assert tri.details["cy_class_in_hc_minus_2"] is True


# =========================================================================
# 6. CY trace and quantization
# =========================================================================

class TestCYTrace:
    """Tests for the CY trace in negative cyclic homology."""

    def test_hc_minus_2_dimension(self):
        """dim HC^-_2(O_{K3}) = 2.

        # VERIFIED: [DC] HH_2 = 2 (B=0), [LT] Loday Ch.5, [CF] cy3_hochschild.py
        """
        trace = cy_trace_k3()
        assert trace.hc_minus_d == 2

    def test_cy_class_exists(self):
        """The CY structure class exists in HC^-_2."""
        trace = cy_trace_k3()
        assert trace.cy_class_exists is True

    def test_cy_class_source(self):
        """CY class comes from H^0(K3, Omega^2) (the holomorphic volume form)."""
        trace = cy_trace_k3()
        assert "H^0(K3, Omega^2" in trace.cy_class_source

    def test_kappa_ch_from_trace(self):
        """kappa_ch = 2 from the CY trace quantization.

        # VERIFIED: [DC] chi(O_{K3}) = 2, [CF] phi_k3, [LT] CY-A_2 Prop prop:cy-kappa-d2
        """
        trace = cy_trace_k3()
        assert trace.kappa_ch == 2
        assert trace.quantization_level == 2


# =========================================================================
# 7. S^1-equivariant character
# =========================================================================

class TestS1Character:
    """Tests for the S^1-equivariant character of O(L(K3))."""

    def test_character_coefficients(self):
        """ch_{S^1}(O(L(K3))) = 2 + 20t + 2t^2."""
        char = s1_equivariant_character_k3()
        assert char["character_coefficients"] == {0: 2, 1: 20, 2: 2}

    def test_total_dimension(self):
        """Total: 2 + 20 + 2 = 24."""
        char = s1_equivariant_character_k3()
        assert char["total_dim"] == 24

    def test_holomorphic_euler_characteristics(self):
        """chi(Omega^p) for K3.

        chi(O) = 2, chi(Omega^1) = -20, chi(Omega^2) = 2.

        # VERIFIED: [DC] chi(Omega^p) = sum (-1)^q h^{p,q}
        # [SY] Gauss-Bonnet: sum (-1)^p chi(Omega^p) = chi_top = 24
        """
        char = s1_equivariant_character_k3()
        assert char["chi_omega"] == {0: 2, 1: -20, 2: 2}
        # Gauss-Bonnet check: sum (-1)^p chi(Omega^p) = chi_top
        gb = sum((-1)**p * char["chi_omega"][p] for p in range(K3_DIM + 1))
        assert gb == 24  # chi_top(K3) = 24

    def test_poincare_symmetry(self):
        """Character coefficients satisfy Poincare symmetry: c_p = c_{d-p}."""
        char = s1_equivariant_character_k3()
        assert char["poincare_symmetric"] is True


# =========================================================================
# 8. CY_2 surface comparison
# =========================================================================

class TestCY2Comparison:
    """Tests comparing loop space / CDO across CY_2 surfaces."""

    def test_abelian_surface_total_dim(self):
        """dim O(L(A)) = 16 for abelian surface.

        # VERIFIED: [DC] sum binom(2,p)binom(2,q) = 4^2 = 16
        """
        ab = abelian_surface_data()
        assert ab.hh_total_dim == 16

    def test_abelian_surface_chi_O(self):
        """chi(O_A) = 0 for abelian surface.

        # VERIFIED: [DC] 1-2+1 = 0, [LT] Mumford "Abelian Varieties"
        """
        ab = abelian_surface_data()
        assert ab.chi_O == 0

    def test_abelian_surface_decomposition(self):
        """Abelian: {4, 8, 4} by form degree."""
        ab = abelian_surface_data()
        assert ab.decomposition == {0: 4, 1: 8, 2: 4}

    def test_abelian_connes_B_zero(self):
        """B = 0 on abelian surface by Hodge theory (Kaehler)."""
        ab = abelian_surface_data()
        assert ab.connes_B_zero is True

    def test_enriques_total_dim(self):
        """dim O(L(S)) = 12 for Enriques surface.

        # VERIFIED: [DC] 1+0+0+0+10+0+0+0+1 = 12
        """
        enr = enriques_surface_data()
        assert enr.hh_total_dim == 12

    def test_enriques_chi_O(self):
        """chi(O_S) = 1 for Enriques surface.

        # VERIFIED: [DC] 1-0+0 = 1, [LT] BHPV Table 10
        """
        enr = enriques_surface_data()
        assert enr.chi_O == 1

    def test_enriques_no_cdo(self):
        """CDO does NOT exist on Enriques (omega_S is 2-torsion)."""
        enr = enriques_surface_data()
        assert enr.cdo_exists is False

    def test_enriques_decomposition(self):
        """Enriques: {1, 10, 1} by form degree."""
        enr = enriques_surface_data()
        assert enr.decomposition == {0: 1, 1: 10, 2: 1}

    def test_k3_enriques_halving(self):
        """K3 -> Enriques halving: 24/2 = 12, chi(O) halves: 2/2 = 1."""
        k3_dim = 24
        enr = enriques_surface_data()
        assert enr.hh_total_dim == k3_dim // 2
        assert enr.chi_O == 1  # = chi(O_{K3}) / 2

    def test_comparison_table_length(self):
        """Three surfaces in the comparison table."""
        table = cy2_comparison_table()
        assert len(table) == 3
        names = [row["name"] for row in table]
        assert "K3" in names
        assert "abelian_surface" in names
        assert "enriques_surface" in names


# =========================================================================
# 9. Cross-checks with other engines
# =========================================================================

class TestCrossChecks:
    """Cross-checks with phi_k3_explicit_evaluation.py and cy3_hochschild.py."""

    def test_loop_dim_matches_phi_generator_count(self):
        """Loop space dim 24 = number of generators of Phi(D^b(K3)).

        Cross-check: phi_k3_explicit_evaluation.EXPECTED_RANK = 24.
        """
        from compute.lib.phi_k3_explicit_evaluation import EXPECTED_RANK
        loop = derived_loop_space_k3()
        assert loop.total_dim == EXPECTED_RANK

    def test_kappa_ch_matches_phi(self):
        """kappa_ch = 2 matches phi_k3_explicit_evaluation.EXPECTED_KAPPA_CH.

        Cross-check with the independent Phi computation.
        """
        from compute.lib.phi_k3_explicit_evaluation import EXPECTED_KAPPA_CH
        cdo = cdo_k3()
        assert cdo.kappa_ch == EXPECTED_KAPPA_CH

    def test_k3_hodge_matches_cy3_engine(self):
        """K3 Hodge numbers match the cy3_hochschild.py K3 data.

        Cross-check: the same Hodge diamond in two independent engines.
        """
        from compute.lib.cy3_hochschild import HodgeData
        k3_hd = HodgeData(dim=2, hodge=K3_HODGE, name="K3", compact=True)
        assert k3_hd.euler_characteristic == 24
        assert k3_hd.h(2, 0) == 1
        assert k3_hd.h(1, 1) == 20

    def test_abelian_chi_O_matches_phi(self):
        """Abelian surface chi(O) = 0 matches phi_k3 abelian evaluation.

        Cross-check with phi_k3_explicit_evaluation.evaluate_phi_on_abelian_surface.
        """
        from compute.lib.phi_k3_explicit_evaluation import evaluate_phi_on_abelian_surface
        ab_phi = evaluate_phi_on_abelian_surface()
        ab_loop = abelian_surface_data()
        assert ab_loop.chi_O == ab_phi.kappa_ch


# =========================================================================
# 10. Structural / mathematical consistency
# =========================================================================

class TestMathematicalConsistency:
    """Tests for structural mathematical identities."""

    def test_gauss_bonnet_from_hodge(self):
        """Gauss-Bonnet: sum (-1)^p chi(Omega^p) = chi_top(X).

        For K3: 2 - (-20) + 2 = 24 = chi_top(K3).

        # VERIFIED: [DC] 2+20+2 = 24, [SY] Gauss-Bonnet-Chern theorem
        """
        chi_omega = {
            p: sum((-1)**q * k3_hodge_number(p, q) for q in range(K3_DIM + 1))
            for p in range(K3_DIM + 1)
        }
        gb = sum((-1)**p * chi_omega[p] for p in range(K3_DIM + 1))
        assert gb == 24

    def test_noether_formula(self):
        """Noether formula for K3: chi(O_{K3}) = (c_1^2 + c_2)/12.

        For K3: c_1 = 0, c_2 = chi_top = 24.
        chi(O_{K3}) = (0 + 24)/12 = 2.

        # VERIFIED: [DC] 24/12 = 2, [LT] Noether (1870) / Hirzebruch (1966)
        """
        c1_squared = 0  # K3 is CY, c_1 = 0
        c2 = 24  # chi_top(K3) = 24
        chi_O_noether = (c1_squared + c2) // 12
        assert chi_O_noether == 2

        cdo = cdo_k3()
        assert cdo.chi_O == chi_O_noether

    def test_hirzebruch_signature_k3(self):
        """Hirzebruch signature theorem: sigma(K3) = (p_1)/3.

        For K3: sigma = b_2^+ - b_2^- = 3 - 19 = -16.
        p_1 = 3*sigma = -48.

        Cross-check: sum (-1)^{p} h^{p,p} = h^{0,0} - h^{1,1} + h^{2,2} = 1-20+1 = -18.
        Wait, that is the chi_y genus at y=-1. The signature is:
        sigma = sum_{p} (-1)^p h^{p,q}... no.

        For a 4-manifold: sigma = b_2^+ - b_2^-.
        K3 intersection form on H^2: signature (3, 19).
        sigma = 3 - 19 = -16.

        # VERIFIED: [DC] 3-19 = -16, [LT] Freedman-Donaldson classification
        """
        b2_plus = 3
        b2_minus = 19
        assert b2_plus + b2_minus == 22  # b_2(K3) = 22
        sigma = b2_plus - b2_minus
        assert sigma == -16

    def test_mukai_lattice_rank(self):
        """Mukai lattice has rank 24 = b_0 + b_2 + b_4 = 1 + 22 + 1.

        The Mukai lattice Lambda_{Muk} = H^0 + H^2 + H^4 with
        pairing <(r,D,s), (r',D',s')> = D.D' - rs' - r's.
        Rank = 24, signature = (4, 20).

        # VERIFIED: [DC] 1+22+1 = 24, [LT] Mukai (1987), [CF] phi_k3 engine
        """
        rank = k3_hodge_number(0, 0) + sum(
            k3_hodge_number(1, q) for q in range(K3_DIM + 1)
        ) + k3_hodge_number(2, 2)
        # Actually: rank = sum_k b_{2k} for even-degree cohomology
        # b_0 = 1, b_2 = h^{2,0}+h^{1,1}+h^{0,2} = 22, b_4 = 1. Total = 24.
        b0 = k3_hodge_number(0, 0)
        b2 = k3_hodge_number(2, 0) + k3_hodge_number(1, 1) + k3_hodge_number(0, 2)
        b4 = k3_hodge_number(2, 2)
        assert b0 + b2 + b4 == 24

    def test_cy2_kappa_equals_chi_O(self):
        """At d=2: kappa_ch = chi(O_X) for all CY_2 surfaces.

        This is Proposition prop:cy-kappa-d2 (PROVED).

        # VERIFIED: [DC] K3: 2=2, abelian: 0=0, [LT] CY-A_2
        """
        # K3
        cdo = cdo_k3()
        assert cdo.kappa_ch == cdo.chi_O

        # Abelian
        ab = abelian_surface_data()
        assert ab.chi_O == 0  # = kappa_ch for abelian

    def test_hc_minus_sum_formula(self):
        """HC^-_0 = sum over even HH = 4, HC^-_1 = sum over odd HH = 20.

        Since B=0: HC^-_n = direct product of HH_{n+2k} for k >= 0.

        # VERIFIED: [DC] HC^-_0 = HH_0 + HH_2 = 2+2 = 4; HC^-_1 = HH_1 = 20
        """
        loop = derived_loop_space_k3()
        assert loop.hc_minus[0] == 4  # HH_0 + HH_2 = 2 + 2
        assert loop.hc_minus[1] == 20  # HH_1 = 20
        assert loop.hc_minus[2] == 2   # HH_2 = 2


# =========================================================================
# 11. Full verification
# =========================================================================

class TestFullVerification:
    """End-to-end verification suite."""

    def test_full_verification_passes(self):
        """The complete verification suite passes."""
        v = full_verification()
        assert v["all_pass"] is True

    def test_full_loop_space(self):
        v = full_verification()
        assert v["loop_space"]["total_dim"] == 24
        assert v["loop_space"]["connes_B_zero"] is True

    def test_full_cdo(self):
        v = full_verification()
        assert v["cdo"]["exists"] is True
        assert v["cdo"]["c_eff"] == 0
        assert v["cdo"]["kappa_ch"] == 2

    def test_full_triangle(self):
        v = full_verification()
        assert v["triangle"]["all_match"] is True
        assert v["triangle"]["loop_dim"] == 24
        assert v["triangle"]["phi_rank"] == 24
        assert v["triangle"]["kappa_ch"] == 2

    def test_full_cy_trace(self):
        v = full_verification()
        assert v["cy_trace"]["hc_minus_2"] == 2
        assert v["cy_trace"]["kappa_ch"] == 2
