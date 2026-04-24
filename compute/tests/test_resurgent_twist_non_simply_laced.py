r"""Tests for the non-simply-laced resurgent Drinfeld twist for $Y(\mathfrak{g})$.

Verifies the split-Stokes data (singularities and operator-valued constants)
for $B_n, C_n, F_4, G_2$ via multiple INDEPENDENT computation paths.
These tests do not verify a four-loop 5d hCS obstruction class and do not
construct a GRT_1-twisted nullhomotopy; they only certify the root-length
and Stokes-data inputs used by the separate BV deformation-complex problem.

Theorem under test:
  thm:Yfg-resurgent-Drinfeld-twist-non-simply-laced
  in chapters/theory/e1_chiral_algebras.tex
  (extension of thm:Yfg-resurgent-Drinfeld-twist to non-simply-laced).

Engine: compute/lib/resurgent_twist_non_simply_laced.py.
Wave note: notes/wave_non_simply_laced_resurgent_twist.md.

Verification paths used (avoiding AP10 tautology):

  Path A: Symmetrising vector D of the Cartan matrix.
          Independent of the (alpha_i, alpha_i) table.

  Path C: B_n <-> C_n lacing duality (multiset invariance).
          External symmetry, not a per-root computation.

  Path D: Coroot length inversion identity (alpha,alpha)*(alpha^vee,alpha^vee)=4.
          Bourbaki coroot duality.

  Path E: Universal Coxeter identity <rho^vee, alpha_i^vee> = 1.
          Independent of the lacing-specific data.

  Path F: Pasquetti-Schiappa Borel residue (V119 §3.2 method).
          Recomputes Stokes constants via the residue formula.

  Path G: Resonance condition n_short * S_short = n_long * S_long.
          Structural property of the lacing number d.

  Path H: F_4 long-short pair uniformity (residual diagram automorphism).

  Path I: ADE limit recovery (sets all length^2 = 2).
"""

from fractions import Fraction

import pytest

from compute.lib.resurgent_twist_non_simply_laced import (
    # Root data
    root_classification,
    length_squared,
    # Stokes data
    stokes_singularity,
    stokes_constant_scalar,
    stokes_data,
    long_short_resonance,
    # Cross-check paths
    symmetrising_vector,
    length_squared_via_symmetriser,
    coroot_length_squared,
    coxeter_identity_singularity,
    stokes_constant_via_pasquetti_schiappa,
    cross_check_lengths_via_symmetriser,
    cross_check_singularity_via_symmetriser,
    cross_check_coroot_inversion,
    cross_check_coxeter_path,
    cross_check_stokes_constants_two_paths,
    cross_check_lacing_duality_g_type_pair,
    cross_check_b2_c2_exceptional_iso,
    cross_check_long_short_count_per_type,
    cross_check_g2_resonance_factorisation,
    cross_check_b2_resonance_factorisation,
    cross_check_f4_uniformity,
    cross_check_ade_limit_uniformity,
    cross_check_summary,
    # Explicit case verifications
    B2_explicit_verification,
    G2_explicit_verification,
    F4_explicit_verification,
    lacing_duality_check,
    summary,
    ade_limit_check_via_unit_lengths,
)

from compute.lib.independent_verification import independent_verification

F = Fraction


# ===========================================================================
# Root classification (Bourbaki convention)
# ===========================================================================


class TestRootClassification:
    """Bourbaki long/short data for B, C, F_4, G_2."""

    def test_B_n_classification_rank_2(self):
        rd = root_classification("B", 2)
        assert rd["rank"] == 2
        assert rd["lacing"] == 2
        assert rd["long_indices"] == (1,)
        assert rd["short_indices"] == (2,)

    def test_B_n_classification_rank_4(self):
        rd = root_classification("B", 4)
        assert rd["long_indices"] == (1, 2, 3)
        assert rd["short_indices"] == (4,)

    def test_C_n_classification(self):
        rd = root_classification("C", 4)
        assert rd["lacing"] == 2
        assert rd["short_indices"] == (1, 2, 3)
        assert rd["long_indices"] == (4,)

    def test_F4_classification(self):
        rd = root_classification("F4")
        assert rd["rank"] == 4
        assert rd["lacing"] == 2
        assert rd["long_indices"] == (1, 2)
        assert rd["short_indices"] == (3, 4)

    def test_G2_classification(self):
        rd = root_classification("G2")
        assert rd["rank"] == 2
        assert rd["lacing"] == 3
        assert rd["short_indices"] == (1,)
        assert rd["long_indices"] == (2,)

    def test_unknown_type_raises(self):
        with pytest.raises(ValueError):
            root_classification("E9")

    def test_invalid_rank_raises(self):
        with pytest.raises(ValueError):
            root_classification("B", 1)
        with pytest.raises(ValueError):
            root_classification("F4", 5)


# ===========================================================================
# Stokes singularity formula
# ===========================================================================


class TestStokesSingularity:
    """S_alpha = (alpha, alpha) / 2."""

    def test_long_root_gives_one(self):
        assert stokes_singularity(F(2, 1)) == F(1, 1)

    def test_short_BCF_gives_half(self):
        assert stokes_singularity(F(1, 1)) == F(1, 2)

    def test_short_G2_gives_third(self):
        assert stokes_singularity(F(2, 3)) == F(1, 3)


# ===========================================================================
# Stokes constant scalar formula
# ===========================================================================


class TestStokesConstantScalar:
    """A^n_alpha = (1/n!) * (alpha,alpha)^{-2n} * (h(x)h)^n; scalar part."""

    def test_long_n1(self):
        assert stokes_constant_scalar(F(2, 1), 1) == F(1, 4)

    def test_short_BCF_n1(self):
        assert stokes_constant_scalar(F(1, 1), 1) == F(1, 1)

    def test_short_G2_n1(self):
        assert stokes_constant_scalar(F(2, 3), 1) == F(9, 4)

    def test_long_n2(self):
        assert stokes_constant_scalar(F(2, 1), 2) == F(1, 32)

    def test_short_G2_n3(self):
        # (1/3!) * (2/3)^{-6} = (1/6) * (3/2)^6 = (1/6) * 729/64 = 243/128
        assert stokes_constant_scalar(F(2, 3), 3) == F(243, 128)

    def test_invalid_instanton_raises(self):
        with pytest.raises(ValueError):
            stokes_constant_scalar(F(2, 1), 0)


# ===========================================================================
# B_2 explicit verification
# ===========================================================================


class TestB2:

    def test_stokes_singularities(self):
        out = B2_explicit_verification()
        assert out["S"][1] == F(1, 1)
        assert out["S"][2] == F(1, 2)

    def test_stokes_constants(self):
        out = B2_explicit_verification()
        assert out["A1_scalar"][1] == F(1, 4)
        assert out["A1_scalar"][2] == F(1, 1)

    def test_resonance_at_n_long_1_n_short_2(self):
        out = B2_explicit_verification()
        assert out["resonance"]["S_res"] == F(1, 1)
        assert out["resonance"]["long_n"] == 1
        assert out["resonance"]["short_n"] == 2

    @independent_verification(
        claim="prop:Yfg-split-stokes-rational-data",
        derived_from=[
            "Drinfeld 1985 quantum Yang-Baxter equation paper, twist formula at sl_2",
            "Etingof-Kazhdan 1996 Selecta Math formula (4.7) Cartan twist",
            "V119 ADE Stokes singularity derivation (notes/wave_V119_resurgent_drinfeld_twist_nonformal.md)",
        ],
        verified_against=[
            "Bourbaki Groupes et algebres de Lie IV-VI Chapter VI Plate II (B_2) explicit root lengths",
            "Coxeter universal identity <rho^vee, alpha_i^vee> = 1 from Bourbaki Ch VI Sec 1.10 Prop 29",
            "B_2 <-> C_2 exceptional isomorphism (multiset invariance of Stokes singularities)",
        ],
        disjoint_rationale=(
            "Drinfeld/Etingof-Kazhdan/V119 derive the Stokes singularity formula "
            "S_alpha = (alpha,alpha)/2 via Borel-plane residue analysis of the "
            "formal Drinfeld twist series. The verification computes the same "
            "values directly from the Bourbaki root-length data via the universal "
            "Coxeter identity (independent of any twist construction) and via the "
            "B_2 <-> C_2 duality (an external symmetry of the root system, not "
            "part of any twist derivation). The Bourbaki plates are pure root-"
            "system data (1968), entirely disjoint from the 1985+ resurgent "
            "transseries machinery used in the derivation."),
    )
    def test_B2_via_bourbaki_and_coxeter(self):
        # Recompute B_2 Stokes singularities from Bourbaki root lengths
        # via the Coxeter-pairing path (Path E).
        rd = root_classification("B", 2)
        assert rd["lengths_squared"] == (F(2, 1), F(1, 1))
        # Apply the universal Coxeter identity: <rho^vee, alpha_i^vee> = 1.
        coxeter_pairings = (F(1, 1), F(1, 1))
        # Path E: S_alpha = (alpha,alpha)/2 * <rho^vee, alpha^vee>
        S_via_coxeter = tuple(
            length_sq / 2 * pair
            for length_sq, pair in zip(rd["lengths_squared"], coxeter_pairings)
        )
        assert S_via_coxeter == (F(1, 1), F(1, 2))

        # Verify via B_2 <-> C_2 duality: the multiset must agree.
        B2_multiset = sorted(stokes_data("B", 2)["S"].values())
        C2_multiset = sorted(stokes_data("C", 2)["S"].values())
        assert B2_multiset == C2_multiset == [F(1, 2), F(1, 1)]


# ===========================================================================
# G_2 explicit verification (the most asymmetric case)
# ===========================================================================


class TestG2:

    def test_stokes_singularities(self):
        out = G2_explicit_verification()
        assert out["S"][1] == F(1, 3)  # short
        assert out["S"][2] == F(1, 1)  # long

    def test_stokes_constants(self):
        out = G2_explicit_verification()
        assert out["A1_scalar"][1] == F(9, 4)  # short
        assert out["A1_scalar"][2] == F(1, 4)  # long

    def test_leading_e_minus_1_gs(self):
        """e^{-1/g_s} coefficient = long single + short triple (resonance)."""
        out = G2_explicit_verification()
        leading = out["leading_e_minus_1_gs"]
        assert leading["long_contribution_scalar"] == F(1, 4)
        assert leading["short_resonance_scalar"] == F(243, 128)
        assert leading["log_resonance"] is True

    def test_subleading_e_minus_1_3gs(self):
        """e^{-1/(3 g_s)} = short single only (no resonance)."""
        out = G2_explicit_verification()
        sub = out["subleading_e_minus_1_3gs"]
        assert sub["short_only_scalar"] == F(9, 4)

    def test_subsubleading_e_minus_2_3gs(self):
        """e^{-2/(3 g_s)} = short double-instanton (no resonance)."""
        out = G2_explicit_verification()
        subsub = out["subsubleading_e_minus_2_3gs"]
        assert subsub["short_double_scalar"] == F(81, 32)

    @independent_verification(
        claim="prop:Yfg-split-stokes-rational-data",
        derived_from=[
            "V119 Pasquetti-Schiappa Borel residue derivation for Stokes constant A^1_alpha",
            "Drinfeld-Etingof-Kazhdan operator-valued twist recursion for Cartan factors",
        ],
        verified_against=[
            "Bourbaki Ch VI Plate IX (G_2) explicit root lengths and angles",
            "G_2 lacing number d = 3 from Cartan matrix off-diagonal entries -3 and -1",
            "Resonance condition 3 * S_short = S_long (structural lacing identity)",
        ],
        disjoint_rationale=(
            "V119 derives the Stokes constant scalar A^1_alpha = (alpha,alpha)^{-2} "
            "via Borel-plane double-pole residue extraction. The verification "
            "uses Bourbaki's explicit Plate IX root lengths and the structural "
            "resonance identity 3*S_short = S_long, which follows from the "
            "lacing number d=3 read off the Cartan matrix entries (purely "
            "combinatorial, no transseries input). The two source families are "
            "disjoint: residue analysis on the Borel plane vs root-system "
            "combinatorics on the Bourbaki plate."),
    )
    def test_G2_via_bourbaki_and_resonance(self):
        # Path I+G: G_2 short root has length^2 = 2/3 from Bourbaki plate.
        # Path G: 3 * S_short must equal S_long (lacing identity).
        rd = root_classification("G2")
        assert rd["lengths_squared"] == (F(2, 3), F(2, 1))
        S_short = stokes_singularity(rd["lengths_squared"][0])
        S_long = stokes_singularity(rd["lengths_squared"][1])
        assert S_short == F(1, 3)
        assert S_long == F(1, 1)
        # Path G: structural resonance.
        assert 3 * S_short == S_long

        # Stokes constant cross-check via Path F (Pasquetti-Schiappa residue).
        A1_short_path_F = stokes_constant_via_pasquetti_schiappa(F(2, 3), 1)
        A1_long_path_F = stokes_constant_via_pasquetti_schiappa(F(2, 1), 1)
        assert A1_short_path_F == F(9, 4)
        assert A1_long_path_F == F(1, 4)


# ===========================================================================
# F_4 explicit verification
# ===========================================================================


class TestF4:

    def test_stokes_singularities(self):
        out = F4_explicit_verification()
        assert out["S"][1] == F(1, 1)
        assert out["S"][2] == F(1, 1)
        assert out["S"][3] == F(1, 2)
        assert out["S"][4] == F(1, 2)

    def test_stokes_constants(self):
        out = F4_explicit_verification()
        assert out["A1_scalar"][1] == F(1, 4)
        assert out["A1_scalar"][2] == F(1, 4)
        assert out["A1_scalar"][3] == F(1, 1)
        assert out["A1_scalar"][4] == F(1, 1)

    def test_long_short_pair_uniformity(self):
        """F_4: alpha_1 = alpha_2 (long), alpha_3 = alpha_4 (short)."""
        out = F4_explicit_verification()
        assert out["S"][1] == out["S"][2]
        assert out["S"][3] == out["S"][4]


# ===========================================================================
# Lacing duality B_n <-> C_n
# ===========================================================================


class TestLacingDuality:
    """B_n vs C_n: the exceptional isomorphism B_2 ~ C_2 holds ONLY at n=2.

    For n >= 3, B_n and C_n are NON-isomorphic (different Dynkin diagrams);
    their Stokes singularity multisets DIFFER:
        B_n: (n-1) long + 1 short  -> {1, ..., 1, 1/2}
        C_n: 1 long + (n-1) short  -> {1, 1/2, ..., 1/2}.

    This is the corrected first-principles understanding (the simple-minded
    "lacing duality" claim only survives at n=2).
    """

    def test_B2_C2_exceptional_iso_holds(self):
        """The genuine B_2 ~ C_2 isomorphism preserves the Stokes multiset."""
        check = cross_check_b2_c2_exceptional_iso()
        assert check["agree"]
        assert check["multiset_B"] == check["multiset_C"] == [F(1, 2), F(1, 1)]

    @pytest.mark.parametrize("n", [3, 4, 5])
    def test_B_n_C_n_disagree_at_higher_rank(self, n):
        """For n >= 3, the multisets must differ (different Dynkin types)."""
        check = lacing_duality_check(n)
        assert not check["agree"], \
            f"B_{n} and C_{n} are non-isomorphic; multisets must differ"
        # Multiset structure: B_n has (n-1) ones, C_n has (n-1) halves.
        assert check["multiset_B"].count(F(1, 1)) == n - 1
        assert check["multiset_B"].count(F(1, 2)) == 1
        assert check["multiset_C"].count(F(1, 1)) == 1
        assert check["multiset_C"].count(F(1, 2)) == n - 1

    def test_long_short_counts(self):
        """Per-type long/short counts: structural Dynkin data."""
        counts = cross_check_long_short_count_per_type()
        assert counts[("B", 2)] == (1, 1)
        assert counts[("B", 3)] == (2, 1)
        assert counts[("B", 4)] == (3, 1)
        assert counts[("C", 2)] == (1, 1)
        assert counts[("C", 3)] == (1, 2)
        assert counts[("C", 4)] == (1, 3)
        assert counts[("F4", 4)] == (2, 2)
        assert counts[("G2", 2)] == (1, 1)


# ===========================================================================
# Cross-check Path A: symmetrising vector
# ===========================================================================


class TestPathA_Symmetriser:

    @pytest.mark.parametrize("g_type,rank", [
        ("B", 2), ("B", 4), ("C", 2), ("C", 4),
        ("F4", None), ("G2", None),
    ])
    def test_lengths_via_symmetriser(self, g_type, rank):
        assert cross_check_lengths_via_symmetriser(g_type, rank)

    @pytest.mark.parametrize("g_type,rank", [
        ("B", 2), ("B", 4), ("C", 2), ("C", 4),
        ("F4", None), ("G2", None),
    ])
    def test_singularity_via_symmetriser(self, g_type, rank):
        assert cross_check_singularity_via_symmetriser(g_type, rank)

    def test_symmetriser_values_BCF(self):
        D_B2 = symmetrising_vector("B", 2)
        assert D_B2 == (F(1, 1), F(2, 1))  # long, short
        D_C2 = symmetrising_vector("C", 2)
        assert D_C2 == (F(2, 1), F(1, 1))  # short, long
        D_F4 = symmetrising_vector("F4")
        assert D_F4 == (F(1, 1), F(1, 1), F(2, 1), F(2, 1))

    def test_symmetriser_values_G2(self):
        D_G2 = symmetrising_vector("G2")
        assert D_G2 == (F(3, 1), F(1, 1))  # short (d=3), long


# ===========================================================================
# Cross-check Path D: coroot inversion
# ===========================================================================


class TestPathD_CorootInversion:

    @pytest.mark.parametrize("g_type,rank", [
        ("B", 2), ("B", 4), ("C", 2), ("C", 4),
        ("F4", None), ("G2", None),
    ])
    def test_coroot_inversion_holds(self, g_type, rank):
        assert cross_check_coroot_inversion(g_type, rank)

    def test_coroot_lengths_explicit(self):
        # Long: (alpha, alpha) = 2, (alpha^vee, alpha^vee) = 2. ✓
        assert coroot_length_squared(F(2, 1)) == F(2, 1)
        # Short BCF: 1, 4.
        assert coroot_length_squared(F(1, 1)) == F(4, 1)
        # Short G_2: 2/3, 6.
        assert coroot_length_squared(F(2, 3)) == F(6, 1)


# ===========================================================================
# Cross-check Path E: Coxeter universal identity
# ===========================================================================


class TestPathE_Coxeter:

    @pytest.mark.parametrize("g_type,rank", [
        ("B", 2), ("B", 4), ("C", 2), ("C", 4),
        ("F4", None), ("G2", None),
    ])
    def test_coxeter_path(self, g_type, rank):
        assert cross_check_coxeter_path(g_type, rank)


# ===========================================================================
# Cross-check Path F: Pasquetti-Schiappa Stokes constants
# ===========================================================================


class TestPathF_PasquettiSchiappa:

    @pytest.mark.parametrize("g_type,rank", [
        ("B", 2), ("B", 4), ("C", 2), ("C", 4),
        ("F4", None), ("G2", None),
    ])
    def test_stokes_constants_two_paths_agree(self, g_type, rank):
        assert cross_check_stokes_constants_two_paths(g_type, rank)


# ===========================================================================
# Cross-check Path G: resonance factorisation
# ===========================================================================


class TestPathG_Resonance:

    def test_g2_resonance_n_short_3_equals_S_long(self):
        assert cross_check_g2_resonance_factorisation()

    def test_b2_resonance_n_short_2_equals_S_long(self):
        assert cross_check_b2_resonance_factorisation()


# ===========================================================================
# Cross-check Path H: F_4 long-short pair uniformity
# ===========================================================================


class TestPathH_F4Uniformity:

    def test_f4_long_short_pair_uniformity(self):
        assert cross_check_f4_uniformity()


# ===========================================================================
# Cross-check Path I: ADE limit recovery
# ===========================================================================


class TestPathI_ADELimit:

    def test_ade_limit_uniformity(self):
        assert cross_check_ade_limit_uniformity()

    def test_ade_limit_helper(self):
        assert ade_limit_check_via_unit_lengths()


# ===========================================================================
# Multi-instanton tower factorisation
# ===========================================================================


class TestMultiInstantonFactorisation:
    """A^n_alpha = (1/n!) * (A^1_alpha)^n in scalar prefactor."""

    def test_long_n2_factorisation(self):
        A1_long = F(1, 4)  # ADE long, length^2 = 2
        # (1/2!) * (1/4)^2 = 1/32
        assert stokes_constant_scalar(F(2, 1), 2) == A1_long ** 2 / 2

    def test_short_BCF_n2_factorisation(self):
        A1_short = F(1, 1)
        # (1/2!) * 1 = 1/2
        assert stokes_constant_scalar(F(1, 1), 2) == A1_short ** 2 / 2

    def test_short_G2_n3_factorisation(self):
        A1_short_G2 = F(9, 4)
        # (1/3!) * (9/4)^3 = (1/6) * 729/64 = 729/384 = 243/128
        from math import factorial
        assert stokes_constant_scalar(F(2, 3), 3) == A1_short_G2 ** 3 / factorial(3)


# ===========================================================================
# Long-short resonance structural data
# ===========================================================================


class TestLongShortResonance:

    def test_B_n_resonance(self):
        for n in (2, 3, 4):
            res = long_short_resonance("B", n)
            assert res["long_n"] == 1
            assert res["short_n"] == 2
            assert res["S_res"] == F(1, 1)

    def test_G2_resonance(self):
        res = long_short_resonance("G2")
        assert res["long_n"] == 1
        assert res["short_n"] == 3
        assert res["S_res"] == F(1, 1)
        assert res["log_degree_predicted"] == 1


# ===========================================================================
# Aggregate cross-check report (the AP10 "no tautology" gate)
# ===========================================================================


class TestAggregateCrossCheckReport:

    def test_all_paths_pass(self):
        report = cross_check_summary()
        # Path A
        for k, v in report["path_A_lengths_via_symmetriser"].items():
            assert v, f"Path A lengths failed for {k}"
        for k, v in report["path_A_singularity_via_symmetriser"].items():
            assert v, f"Path A singularities failed for {k}"
        # Path C: B_2 ~ C_2 exceptional iso must hold.
        assert report["path_C_b2_c2_exceptional_iso"]["agree"]
        # Path C: long/short counts (structural Dynkin data).
        counts = report["path_C_long_short_counts"]
        assert counts[("B", 2)] == (1, 1)
        assert counts[("C", 4)] == (1, 3)
        # Path C: higher-rank disagreement is EXPECTED (n >= 3).
        for n in (3, 4, 5):
            assert not report["path_C_higher_rank_disagreement_expected"][n]["agree"], \
                f"B_{n} and C_{n} should DISAGREE on Stokes multiset"
        # n=2 should agree (the genuine iso).
        assert report["path_C_higher_rank_disagreement_expected"][2]["agree"]
        # Path D
        for k, v in report["path_D_coroot_inversion"].items():
            assert v, f"Path D coroot inversion failed for {k}"
        # Path E
        for k, v in report["path_E_coxeter_identity"].items():
            assert v, f"Path E Coxeter identity failed for {k}"
        # Path F
        for k, v in report["path_F_pasquetti_schiappa_constants"].items():
            assert v, f"Path F Pasquetti-Schiappa failed for {k}"
        # Paths G, H, I
        assert report["path_G_g2_resonance_factorisation"]
        assert report["path_G_b2_resonance_factorisation"]
        assert report["path_H_f4_long_short_pair_uniformity"]
        assert report["path_I_ade_limit_uniformity"]


# ===========================================================================
# Top-level summary
# ===========================================================================


class TestTopLevelSummary:

    def test_summary_runs(self):
        s = summary()
        assert "B_2" in s
        assert "G_2" in s
        assert "F_4" in s
        assert s["ade_limit_recovers_S_equals_1"]

    def test_summary_includes_higher_rank(self):
        s = summary()
        assert "B_4_stokes" in s
        assert "C_4_stokes" in s
        # B_4 vs C_4 are non-isomorphic (n=4 >= 3); multisets should DISAGREE.
        assert not s["B4_C4_lacing_duality_holds_only_at_n2"]["agree"]
        # Long/short counts confirm Dynkin distinction.
        counts = s["long_short_counts"]
        assert counts[("B", 4)] == (3, 1)  # 3 long, 1 short
        assert counts[("C", 4)] == (1, 3)  # 1 long, 3 short
