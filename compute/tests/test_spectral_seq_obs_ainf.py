r"""Regression tests for the m_3--B^{(2)} obstruction theorem.

The theorem separates three carriers:

* the terminal-slot termwise operator B^{(2)}_term, which has a strict
  nonzero witness;
* the Costello corrected TCFT operator B^{(2)}_TCFT, which satisfies only
  the total boundary identity with b = sum_k b_k;
* the derived E_1-Hochschild obstruction class, whose vanishing requires an
  explicit HH^{-2} filtration hypothesis.

The spectral-sequence helper module still has useful combinatorics.  Its
universal exactness verdict is not a theorem for B^{(2)}_term, so tests below
do not certify that forbidden strengthening.
"""

from collections import Counter
from fractions import Fraction
from pathlib import Path

from compute.lib.spectral_seq_obs_ainf import (
    ArityFiltration,
    CommutatorTerm,
    FiltrationAnalysis,
    LocalP2Generator,
    SpectralPageComparison,
    SufficiencyAnalysis,
    analyze_sufficiency,
    b2_filtration_shift,
    compute_filtration_analysis,
    compute_spectral_seq_obs_ainf,
    enumerate_commutator_terms,
    local_p2_cy_pairing,
    local_p2_generators,
    local_p2_m3,
    local_p2_nonadjacent_analysis,
    mk_filtration_shift,
    spectral_comparison_by_class,
    stasheff_identity_at_arity,
    virasoro_d4_connection,
)

F = Fraction

DEGREES = {"e": 0, "a": 1, "b": 2, "w": 3}
DESUSPENDED_DEGREES = {name: degree - 1 for name, degree in DEGREES.items()}
PAIRING = {
    ("e", "w"): F(1),
    ("w", "e"): F(1),
    ("a", "b"): F(1),
    ("b", "a"): F(1),
}
ROOT = Path(__file__).resolve().parents[2]
STANDALONE = ROOT / "standalone" / "m3_b2_obstruction_vol3.tex"


def terminal_slot_b2(word):
    """Terminal-slot B_term convention used by the standalone witness."""
    word = tuple(word)
    terminal = word[-1]
    out = Counter()
    for i, entry in enumerate(word[:-1]):
        coeff = PAIRING.get((entry, terminal), F(0))
        if coeff:
            reduced = word[:i] + word[i + 1:-1]
            out[reduced] += coeff
    return out


def m3_bar(word, alpha=F(1)):
    """Minimal witness operation m_3(a,a,a)=alpha b on consecutive triples."""
    word = tuple(word)
    out = Counter()
    for start in range(len(word) - 2):
        if word[start:start + 3] == ("a", "a", "a"):
            reduced = word[:start] + ("b",) + word[start + 3:]
            out[reduced] += alpha
    return out


def compose(first, second, word):
    """Apply first, then second, to a linear combination of bar words."""
    total = Counter()
    for mid, coeff_mid in first(word).items():
        for out, coeff_out in second(mid).items():
            total[out] += coeff_mid * coeff_out
    return total


def witness_commutator(word, alpha=F(1)):
    m3 = lambda w: m3_bar(w, alpha=alpha)
    m3_after_b2 = compose(terminal_slot_b2, m3, word)
    b2_after_m3 = compose(m3, terminal_slot_b2, word)
    return m3_after_b2 - b2_after_m3


class TestM3B2ObstructionTheorem:
    """Direct oracle for the standalone obstruction theorem."""

    def test_cy3_degrees_and_pairing(self):
        assert DEGREES["a"] + DEGREES["b"] == 3
        assert DEGREES["e"] + DEGREES["w"] == 3
        assert PAIRING[("a", "b")] == F(1)
        assert PAIRING[("b", "a")] == F(1)

    def test_desuspended_terminal_slot_signs_are_positive(self):
        assert DESUSPENDED_DEGREES["a"] == 0
        assert DESUSPENDED_DEGREES["b"] == 1
        signs = [
            (-1) ** (DESUSPENDED_DEGREES["b"] * i * DESUSPENDED_DEGREES["a"])
            for i in range(4)
        ]
        assert signs == [1, 1, 1, 1]

    def test_strict_witness_arithmetic(self):
        x = ("a", "a", "a", "a", "b")
        assert terminal_slot_b2(x) == Counter({("a", "a", "a"): F(4)})
        assert len(next(iter(terminal_slot_b2(x)))) - len(x) == -2
        assert compose(terminal_slot_b2, m3_bar, x) == Counter({("b",): F(4)})
        assert m3_bar(x) == Counter({
            ("b", "a", "b"): F(1),
            ("a", "b", "b"): F(1),
        })
        assert compose(m3_bar, terminal_slot_b2, x) == Counter({("b",): F(2)})
        assert witness_commutator(x) == Counter({("b",): F(2)})

    def test_connectivity_does_not_imply_empty_hh_minus_two_line(self):
        p = 2
        input_degree = (DEGREES["a"] + 1) + (DEGREES["a"] + 1)
        output_degree = DEGREES["e"]
        q = output_degree - input_degree
        assert p + q == -2

    def test_standalone_separates_termwise_tcft_and_filtered_claims(self):
        text = STANDALONE.read_text()
        assert r"B^{(2)}_{\mathrm{term}}" in text
        assert r"B^{(2)}_{\TCFT}" in text
        assert r"No equality \(B^{(2)}_{\mathrm{term}}=B^{(2)}_{\TCFT}\)" in text
        assert r"E_1^{p,q}=0\qquad\text{whenever }p+q=-2" in text
        assert r"\{b_k,B^{(2)}_{\TCFT}\}=0" in text
        assert "stronger than the TCFT theorem" in text


# =========================================================================
# 1. ARITY FILTRATION BASICS
# =========================================================================

class TestArityFiltration:
    """Test the arity filtration data structure."""

    def test_total_degree(self):
        """Total degree = p + q."""
        # VERIFIED [DC] definition [DA] p + q
        af = ArityFiltration(p=5, q=3)
        assert af.total_degree == 8

    def test_zero_filtration(self):
        # VERIFIED [DC] edge case [DA] 0 + 0 = 0
        af = ArityFiltration(p=0, q=0)
        assert af.total_degree == 0


class TestFiltrationShifts:
    """Test filtration shifts of m_k and B^{(2)}."""

    def test_m2_shift(self):
        """m_2 lowers arity by 1 (replaces 2 factors with 1)."""
        # VERIFIED [DC] m_2 shift [DA] -(2-1) = -1
        assert mk_filtration_shift(2) == -1

    def test_m3_shift(self):
        """m_3 lowers arity by 2 (replaces 3 factors with 1)."""
        # VERIFIED [DC] m_3 shift [DA] -(3-1) = -2
        assert mk_filtration_shift(3) == -2

    def test_m4_shift(self):
        """m_4 lowers arity by 3."""
        # VERIFIED [DC] m_4 shift [DA] -(4-1) = -3
        assert mk_filtration_shift(4) == -3

    def test_mk_general(self):
        """m_k lowers arity by k-1 for all k >= 2."""
        # VERIFIED [DC] general formula [DA] -(k-1)
        for k in range(2, 10):
            assert mk_filtration_shift(k) == -(k - 1)

    def test_b2_shift(self):
        """B^{(2)} lowers arity by 1 (contracts 2 factors to scalar)."""
        # VERIFIED [DC] B^{(2)} shift [LT] cy_to_chiral.tex CC_n -> CC_{n-1}
        assert b2_filtration_shift() == -1

    def test_d_r_from_mk(self):
        """d_r comes from m_{r+1}: filtration shift -(r+1-1) = -r."""
        # VERIFIED [DC] spectral sequence [DA] d_r has shift -r
        for r in range(1, 8):
            assert mk_filtration_shift(r + 1) == -r


# =========================================================================
# 2. COMMUTATOR TERM ENUMERATION
# =========================================================================

class TestCommutatorTerms:
    """Test enumeration of [m_k, B^{(2)}] terms."""

    def test_m3_on_4_elements(self):
        """[m_3, B^{(2)}] on CC_4 has both adjacent and non-adjacent terms."""
        terms = enumerate_commutator_terms(n=4, k=3)
        # VERIFIED [DC] term count [DA] combinatorial enumeration
        assert len(terms) > 0

        adj = [t for t in terms if t.is_adjacent]
        nonadj = [t for t in terms if not t.is_adjacent]
        # VERIFIED [DC] both types exist [DA] n=4, k=3 has room for outside factors
        assert len(adj) > 0
        assert len(nonadj) > 0

    def test_m3_on_3_elements_all_adjacent(self):
        """[m_3, B^{(2)}] on CC_3: m_3 block = entire element, all adjacent."""
        terms = enumerate_commutator_terms(n=3, k=3)
        # VERIFIED [DC] all adjacent [DA] m_3 block spans all 3 factors
        nonadj = [t for t in terms if not t.is_adjacent]
        adj = [t for t in terms if t.is_adjacent]
        assert len(nonadj) == 0
        assert len(adj) > 0

    def test_m3_on_5_elements_has_nonadj(self):
        """[m_3, B^{(2)}] on CC_5 has non-adjacent terms."""
        terms = enumerate_commutator_terms(n=5, k=3)
        nonadj = [t for t in terms if not t.is_adjacent]
        # VERIFIED [DC] non-adj exist [DA] 2 factors outside the m_3 block
        assert len(nonadj) > 0

    def test_symmetry_mk_first_and_b2_first(self):
        """Each configuration has both mk_first and b2_first terms."""
        terms = enumerate_commutator_terms(n=5, k=3)
        mk_first = [t for t in terms if t.order == "mk_first"]
        b2_first = [t for t in terms if t.order == "b2_first"]
        # VERIFIED [DC] paired terms [DA] commutator has two orderings
        assert len(mk_first) == len(b2_first)

    def test_empty_for_small_n(self):
        """No terms if n < k."""
        assert enumerate_commutator_terms(n=2, k=3) == []
        assert enumerate_commutator_terms(n=1, k=3) == []

    def test_nonadj_fraction_low_arity_values(self):
        """Fraction of non-adjacent terms has the exact low-arity profile."""
        fracs = []
        for n in range(4, 9):
            terms = enumerate_commutator_terms(n=n, k=3)
            nonadj = [t for t in terms if not t.is_adjacent]
            fracs.append(F(len(nonadj), len(terms)))

        assert fracs == [
            F(1, 2),
            F(3, 5),
            F(3, 5),
            F(4, 7),
            F(15, 28),
        ]
        assert any(fracs[i] > fracs[i + 1] for i in range(len(fracs) - 1))


# =========================================================================
# 3. FILTRATION ANALYSIS
# =========================================================================

class TestFiltrationAnalysis:
    """Test the filtration analysis for [m_k, B^{(2)}]."""

    def test_m3_n4_has_nonadj(self):
        """Filtration analysis for [m_3, B^{(2)}] on CC_4."""
        fa = compute_filtration_analysis(n=4, k=3)
        # VERIFIED [DC] non-adj exists [DA] n=4 > k=3
        assert fa.num_nonadjacent > 0
        assert fa.nonadjacent_spectral_page == 2  # k-1 = 3-1 = 2

    def test_m3_n3_no_nonadj(self):
        """Filtration analysis for [m_3, B^{(2)}] on CC_3: no non-adjacent."""
        fa = compute_filtration_analysis(n=3, k=3)
        # VERIFIED [DC] no non-adj [DA] m_3 block = full element
        assert fa.num_nonadjacent == 0

    def test_nonadj_spectral_page_is_k_minus_1(self):
        """Non-adjacent terms retain the legacy d_{k-1} page diagnostic."""
        for k in range(3, 6):
            fa = compute_filtration_analysis(n=k + 2, k=k)
            assert fa.nonadjacent_spectral_page == k - 1

    def test_nonadj_not_proved_exact_when_present(self):
        """The termwise helper does not prove exactness for non-adjacent terms."""
        for k in range(3, 6):
            for n in range(k + 1, k + 4):
                fa = compute_filtration_analysis(n, k)
                assert fa.num_nonadjacent > 0
                assert not fa.nonadjacent_exact

    def test_termwise_commutator_not_proved_in_abutment_when_nonadjacent(self):
        """The diagnostic helper does not prove termwise abutment vanishing."""
        for k in range(3, 6):
            for n in range(k + 1, k + 3):
                fa = compute_filtration_analysis(n, k)
                assert fa.num_nonadjacent > 0
                assert not fa.commutator_vanishes_in_abutment

    def test_adjacent_cancel_by_cyclic(self):
        """Adjacent terms always cancel by cyclic invariance."""
        fa = compute_filtration_analysis(n=5, k=3)
        # VERIFIED [DC] cyclic cancellation [LT] G1 identity in cy_to_chiral.tex
        assert fa.adjacent_cancel_by_cyclic

    def test_adjacent_filtration_shift(self):
        """Adjacent terms have filtration shift -(k+1)."""
        for k in range(3, 6):
            fa = compute_filtration_analysis(n=k + 2, k=k)
            # VERIFIED [DC] shift formula [DA] -(k-1) from m_k + (-2) from B^{(2)}
            assert fa.adjacent_filtration == -(k + 1)


# =========================================================================
# 4. LOCAL P^2 EXPLICIT COMPUTATION
# =========================================================================

class TestLocalP2Generators:
    """Test the local P^2 Ext algebra generators."""

    def test_generator_count(self):
        """18 generators: 3 + 6 + 6 + 3 by Ext degree."""
        gens = local_p2_generators()
        # VERIFIED [DC] count [LT] cy_to_chiral.tex comp:local-p2-nonformality
        assert len(gens) == 18

    def test_ext_degree_distribution(self):
        """Distribution: 3 at Ext^0, 6 at Ext^1, 6 at Ext^2, 3 at Ext^3."""
        gens = local_p2_generators()
        counts = {0: 0, 1: 0, 2: 0, 3: 0}
        for g in gens:
            counts[g.ext_degree] += 1
        # VERIFIED [DC] distribution [DA] McKay quiver of Z_3
        assert counts == {0: 3, 1: 6, 2: 6, 3: 3}

    def test_euler_characteristic_zero(self):
        """Euler characteristic = 3 - 6 + 6 - 3 = 0 (CY_3 check)."""
        gens = local_p2_generators()
        chi = sum((-1)**g.ext_degree for g in gens)
        # VERIFIED [DC] Euler char [DA] CY_3 implies chi = 0
        assert chi == 0


class TestLocalP2Pairing:
    """Test the CY_3 pairing for local P^2."""

    def test_ext1_ext2_pairing(self):
        """<x_{01}, y_{10}>_2 = 1 (dual pairing)."""
        x01 = LocalP2Generator("x_01", 0, 1, 1)
        y10 = LocalP2Generator("y_10", 1, 0, 2)
        # VERIFIED [DC] Serre duality [DA] Ext^1 pairs with Ext^2
        assert local_p2_cy_pairing(x01, y10) == F(1)

    def test_non_composable_pairing_zero(self):
        """<x_{01}, y_{01}>_2 = 0 (not composable: target != source)."""
        x01 = LocalP2Generator("x_01", 0, 1, 1)
        y01 = LocalP2Generator("y_01", 0, 1, 2)
        # VERIFIED [DC] composability [DA] target(x) = 1 != 0 = source(y)
        assert local_p2_cy_pairing(x01, y01) == F(0)

    def test_same_degree_pairing_zero(self):
        """<x_{01}, x_{10}>_2 = 0 (both Ext^1, not degree-2 pairing)."""
        x01 = LocalP2Generator("x_01", 0, 1, 1)
        x10 = LocalP2Generator("x_10", 1, 0, 1)
        # VERIFIED [DC] degree mismatch [DA] need Ext^1 + Ext^2 = 3
        assert local_p2_cy_pairing(x01, x10) == F(0)


class TestLocalP2M3:
    """Test the m_3 operation for local P^2."""

    def test_m3_composable_triple(self):
        """m_3(x_{01}, x_{12}, x_{20}) = e_0."""
        x01 = LocalP2Generator("x_01", 0, 1, 1)
        x12 = LocalP2Generator("x_12", 1, 2, 1)
        x20 = LocalP2Generator("x_20", 2, 0, 1)
        result = local_p2_m3(x01, x12, x20)
        # VERIFIED [DC] m_3 value [LT] cy_to_chiral.tex Ginzburg potential
        assert result is not None
        out_gen, coeff = result
        assert out_gen.name == "e_0"
        assert coeff == F(1)

    def test_m3_cyclic_permutation(self):
        """m_3(x_{12}, x_{20}, x_{01}) = e_1 (cyclic)."""
        x12 = LocalP2Generator("x_12", 1, 2, 1)
        x20 = LocalP2Generator("x_20", 2, 0, 1)
        x01 = LocalP2Generator("x_01", 0, 1, 1)
        result = local_p2_m3(x12, x20, x01)
        # VERIFIED [DC] cyclic m_3 [DA] Ginzburg potential cyclic symmetry
        assert result is not None
        assert result[0].name == "e_1"

    def test_m3_non_composable_zero(self):
        """m_3(x_{01}, x_{01}, x_{01}) = 0 (not composable)."""
        x01 = LocalP2Generator("x_01", 0, 1, 1)
        result = local_p2_m3(x01, x01, x01)
        # VERIFIED [DC] non-composable [DA] target(x_{01})=1 != source(x_{01})=0
        assert result is None

    def test_m3_ext0_zero(self):
        """m_3 on non-Ext^1 generators is zero."""
        e0 = LocalP2Generator("e_0", 0, 0, 0)
        x01 = LocalP2Generator("x_01", 0, 1, 1)
        x10 = LocalP2Generator("x_10", 1, 0, 1)
        result = local_p2_m3(e0, x01, x10)
        # VERIFIED [DC] degree constraint [DA] m_3 only on Ext^1 triples
        assert result is None


class TestLocalP2NonadjacentAnalysis:
    """Test the full non-adjacent analysis for local P^2."""

    def setup_method(self):
        self.analysis = local_p2_nonadjacent_analysis()

    def test_has_nonzero_triples(self):
        """Local P^2 has nonzero m_3 triples (non-formal)."""
        # VERIFIED [DC] non-formality [LT] cy_to_chiral.tex class M
        assert self.analysis["num_nonzero_triples"] > 0

    def test_nonzero_triple_count(self):
        """6 composable triples: (01,12,20), (02,21,10), and cyclic perms."""
        # VERIFIED [DC] triple count [DA] Z_3 McKay quiver: 2 orientations x 3 vertices
        assert self.analysis["num_nonzero_triples"] == 6

    def test_all_nonadj_exact(self):
        """The local P^2 enumeration no longer certifies termwise exactness."""
        assert not self.analysis["all_nonadj_exact"]

    def test_spectral_page_is_1(self):
        """No exactness page is assigned without a correction homotopy."""
        assert self.analysis["spectral_page_of_exactness"] is None

    def test_mechanism_names_repaired_inputs(self):
        """The mechanism points to the corrected theorem, not a Stasheff shortcut."""
        assert "TCFT" in self.analysis["mechanism"]
        assert "HH^{-2}" in self.analysis["mechanism"]


# =========================================================================
# 5. SPECTRAL COMPARISON BY SHADOW CLASS
# =========================================================================

class TestSpectralComparisonByClass:
    """Test the spectral sequence comparison across shadow classes."""

    def setup_method(self):
        self.comp = spectral_comparison_by_class(k=3)

    def test_class_g_trivial(self):
        """Class G: m_3 = 0, no non-adjacent terms."""
        # VERIFIED [DC] class G [LT] m_3 = 0 for Heisenberg
        assert self.comp["G"].nonadj_page == 0
        assert self.comp["G"].vanishes_in_abutment

    def test_class_l_e1(self):
        """Class L has a legacy page count, not a termwise proof."""
        assert self.comp["L"].nonadj_page == 1
        assert not self.comp["L"].vanishes_in_abutment

    def test_class_c_charge(self):
        """Class C: charge conservation blocks non-adjacent pairings."""
        # VERIFIED [DC] class C [LT] betagamma charge grading
        assert self.comp["C"].nonadj_page == 1
        assert self.comp["C"].vanishes_in_abutment

    def test_class_m_e2(self):
        """Class M keeps the page diagnostic and fails termwise vanishing."""
        assert self.comp["M"].nonadj_page == 2
        assert not self.comp["M"].vanishes_in_abutment

    def test_no_universal_termwise_vanishing(self):
        """The class comparison rejects universal termwise vanishing."""
        assert {cls for cls, data in self.comp.items()
                if data.vanishes_in_abutment} == {"G", "C"}

    def test_class_g_chain_level(self):
        """Class G has chain-level vanishing (strongest form)."""
        assert self.comp["G"].chain_level_vanishing

    def test_class_m_not_chain_level(self):
        """Class M does NOT have chain-level vanishing (only cohomological)."""
        assert not self.comp["M"].chain_level_vanishing


class TestSpectralComparisonHigherK:
    """Test the legacy page diagnostic for k > 3."""

    def test_m4_class_m_page(self):
        """The class M m_4 page diagnostic is E_3."""
        comp = spectral_comparison_by_class(k=4)
        # VERIFIED [DC] spectral page [DA] k=4, d_{k-1} = d_3
        assert comp["M"].nonadj_page == 3

    def test_m5_class_m_page(self):
        """The class M m_5 page diagnostic is E_4."""
        comp = spectral_comparison_by_class(k=5)
        # VERIFIED [DC] spectral page [DA] k=5, d_{k-1} = d_4
        assert comp["M"].nonadj_page == 4

    def test_page_increases_with_k(self):
        """Higher m_k gives higher spectral page for class M."""
        pages = []
        for k in range(3, 6):
            comp = spectral_comparison_by_class(k)
            pages.append(comp["M"].nonadj_page)
        # VERIFIED [DC] monotonicity [DA] page = k-1
        assert pages == [2, 3, 4]


# =========================================================================
# 6. STASHEFF IDENTITY MECHANISM
# =========================================================================

class TestStasheffIdentity:
    """Test the Stasheff identity data."""

    def test_arity_3(self):
        """Stasheff identity at arity 3: the associator."""
        data = stasheff_identity_at_arity(3)
        # VERIFIED [DC] arity 3 [DA] m_2(m_2(a,b),c) - m_2(a,m_2(b,c)) + m_3 = 0
        assert data["arity"] == 3

    def test_arity_4(self):
        """Stasheff identity at arity 4: the key identity for [m_3, B^{(2)}]."""
        data = stasheff_identity_at_arity(4)
        # VERIFIED [DC] arity 4 [DA] A_inf relation at n=4
        assert data["arity"] == 4
        # Must have (m_3, m_2) terms (relating m_3 and m_2)
        assert (3, 2) in data["ij_distribution"]
        assert (2, 3) in data["ij_distribution"]

    def test_arity_4_relevance(self):
        """Arity 4 identity is relevant to [m_3, B^{(2)}] non-adjacent terms."""
        data = stasheff_identity_at_arity(4)
        assert "non-adjacent" in data["relevance_to_nonadj"]

    def test_term_count_arity_3(self):
        """Arity 3 Stasheff identity has the right number of terms."""
        data = stasheff_identity_at_arity(3)
        # n=3: (i,j) pairs with i+j=4: (1,3),(2,2),(3,1)
        # (1,3): r=1 only (1 term)
        # (2,2): r=1,2 (2 terms)
        # (3,1): r=1,2,3 (3 terms)
        # Total: 1 + 2 + 3 = 6
        # VERIFIED [DC] term count [DA] combinatorial enumeration
        assert data["total_terms"] == 6

    def test_term_count_arity_4(self):
        """Arity 4 Stasheff identity has the right number of terms."""
        data = stasheff_identity_at_arity(4)
        # n=4: (i,j) pairs with i+j=5: (1,4),(2,3),(3,2),(4,1)
        # (1,4): r=1 (1 term)
        # (2,3): r=1,2 (2 terms)
        # (3,2): r=1,2,3 (3 terms)
        # (4,1): r=1,2,3,4 (4 terms)
        # Total: 1 + 2 + 3 + 4 = 10
        # VERIFIED [DC] term count [DA] combinatorial enumeration
        assert data["total_terms"] == 10


# =========================================================================
# 7. SUFFICIENCY ANALYSIS
# =========================================================================

class TestSufficiencyAnalysis:
    """Test whether the termwise helper suffices for the obstruction."""

    def test_class_g_sufficient(self):
        """Class G: chain-level vanishing, trivially sufficient."""
        s = analyze_sufficiency("G")
        # VERIFIED [DC] class G [DA] m_k = 0 for k >= 3
        assert s.chain_level
        assert s.cohomological
        assert s.sufficient_for_framing

    def test_class_l_sufficient(self):
        """Class L needs a correction homotopy or HH^{-2} theorem."""
        s = analyze_sufficiency("L")
        assert not s.chain_level
        assert not s.cohomological
        assert not s.sufficient_for_framing

    def test_class_c_sufficient(self):
        """Class C: chain-level vanishing from charge conservation."""
        s = analyze_sufficiency("C")
        # VERIFIED [DC] class C [DA] charge grading
        assert s.chain_level
        assert s.sufficient_for_framing

    def test_class_m_sufficient(self):
        """Class M is blocked by the strict termwise witness."""
        s = analyze_sufficiency("M")
        assert not s.chain_level
        assert not s.cohomological
        assert not s.sufficient_for_framing

    def test_all_classes_sufficient(self):
        """Only classes with direct chain-level vanishing suffice here."""
        sufficient = {
            cls for cls in ["G", "L", "C", "M"]
            if analyze_sufficiency(cls).sufficient_for_framing
        }
        assert sufficient == {"G", "C"}

    def test_all_classes_upgrade_prop(self):
        """The termwise helper does not provide a universal upgrade."""
        upgrades = {
            cls for cls in ["G", "L", "C", "M"]
            if analyze_sufficiency(cls).upgrades_prop_status
        }
        assert upgrades == {"G", "C"}


# =========================================================================
# 8. VIRASORO d_4 CONNECTION
# =========================================================================

class TestVirasoroD4Connection:
    """Test the connection with prop:virasoro-d4."""

    def setup_method(self):
        self.conn = virasoro_d4_connection()

    def test_d_r_hierarchy(self):
        """d_1 from m_2, d_2 from m_3, d_3 from m_4."""
        # VERIFIED [DC] spectral sequence [DA] d_r = m_{r+1}
        assert "m_2" in self.conn["d_r_from_mk"]["d_1"]
        assert "m_3" in self.conn["d_r_from_mk"]["d_2"]
        assert "m_4" in self.conn["d_r_from_mk"]["d_3"]

    def test_nonadj_m3_at_e2(self):
        """The m_3 page entry is explicitly diagnostic."""
        entry = self.conn["nonadj_mk_page"]["[m_3, B^{(2)}]_non-adj"]
        assert "diagnostic" in entry
        assert "not a termwise exactness proof" in entry

    def test_nonadj_m4_at_e3(self):
        """The m_4 page entry is explicitly diagnostic."""
        entry = self.conn["nonadj_mk_page"]["[m_4, B^{(2)}]_non-adj"]
        assert "diagnostic" in entry
        assert "not a termwise exactness proof" in entry

    def test_d4_coefficient(self):
        """The d_4 coefficient is 40/27 at c=1."""
        # VERIFIED [DC] d_4 value [LT] prop:virasoro-d4
        assert "40/27" in self.conn["virasoro_d4"]["coefficient"]

    def test_independence(self):
        """Non-adjacent [m_3, B^{(2)}] and d_4 are independent."""
        # VERIFIED [DC] independence [DA] d_2 acts before d_4
        assert "independent" in self.conn["independence"].lower()

    def test_nonadj_killed_before_d4(self):
        """Independence requires the corrected TCFT or HH^{-2} input."""
        assert "TCFT" in self.conn["independence"]
        assert "HH^{-2}" in self.conn["independence"]


# =========================================================================
# 9. FULL COMPUTATION
# =========================================================================

class TestFullComputation:
    """Test the complete diagnostic analysis."""

    def setup_method(self):
        self.results = compute_spectral_seq_obs_ainf(n_max=7, k_max=5)

    def test_main_result_statement(self):
        """Main result rejects termwise universal exactness."""
        assert "nonzero strict witnesses" in self.results["main_result"]["statement"]

    def test_all_filtrations_consistent(self):
        """The termwise vanishing check fails once non-adjacent terms exist."""
        assert not self.results["main_result"]["all_filtrations_consistent"]

    def test_all_classes_sufficient(self):
        """The termwise helper is not sufficient for all classes."""
        assert not self.results["main_result"]["all_classes_sufficient"]

    def test_upgrades_proposition(self):
        """The diagnostic analysis does not upgrade the proposition."""
        assert not self.results["main_result"]["upgrades_proposition"]

    def test_chain_level_false_in_class_m(self):
        """Termwise chain-level vanishing is false in class M."""
        verdict = self.results["main_result"]["chain_level_open"].lower()
        assert "false in class m" in verdict
        assert "strict m3-b2 witness" in verdict

    def test_local_p2_all_exact(self):
        """Local P^2 enumeration is not a proof of termwise exactness."""
        assert not self.results["local_p2"]["all_nonadj_exact"]

    def test_filtration_data_nonempty(self):
        """Filtration data computed for multiple (n,k) pairs."""
        assert len(self.results["filtration_data"]) > 0

    def test_stasheff_data_present(self):
        """Stasheff identity data computed."""
        assert len(self.results["stasheff_identities"]) > 0


# =========================================================================
# 10. CROSS-VALIDATION WITH EXISTING ENGINES
# =========================================================================

class TestCrossValidation:
    """Cross-validate with a_infinity_bar_w1inf.py and hopf_fibration_s3_framing.py."""

    def test_m3_ttt_nonzero(self):
        """m_3(T,T,T) = -2T (Virasoro at c=1 is non-formal)."""
        from compute.lib.a_infinity_bar_w1inf import AInfBarComplex, T
        bar_cx = AInfBarComplex()
        m3_result = bar_cx.m3(T, T, T).simplify()
        # VERIFIED [DC] m_3 value [LT] a_infinity_bar_w1inf.py
        assert len(m3_result.terms) == 1
        assert m3_result.terms[0].coeff == Fraction(-2)
        # This means class M non-adjacent terms are genuine (m_3 != 0)

    def test_m3_jjj_zero(self):
        """m_3(J,J,J) = 0 (Heisenberg is formal, class G)."""
        from compute.lib.a_infinity_bar_w1inf import AInfBarComplex, J
        bar_cx = AInfBarComplex()
        m3_result = bar_cx.m3(J, J, J).simplify()
        # VERIFIED [DC] m_3 = 0 [LT] a_infinity_bar_w1inf.py class G
        assert m3_result.is_zero
        # Class G has no non-adjacent terms (m_3 = 0 chain-level)

    def test_virasoro_shadow_class_m(self):
        """Virasoro at c=1 is class M (infinite shadow depth)."""
        from compute.lib.holomorphic_cs_chiral_engine import (
            E3BarSpectralSequenceVirasoro,
        )
        from sympy import Rational
        vir = E3BarSpectralSequenceVirasoro(c=Rational(1))
        # VERIFIED [DC] class M [LT] holomorphic_cs_chiral_engine.py
        assert vir.shadow_class == "M"
        # Class M is the hardest case for non-adjacent terms

    def test_d4_coefficient_40_over_27(self):
        """d_4 coefficient = 40/27 (from prop:virasoro-d4)."""
        from compute.lib.holomorphic_cs_chiral_engine import (
            E3BarSpectralSequenceVirasoro,
        )
        from sympy import Rational
        vir = E3BarSpectralSequenceVirasoro(c=Rational(1))
        # VERIFIED [DC] d_4 value [LT] holomorphic_cs_chiral_engine.py
        assert vir.d4_coefficient() == Rational(40, 27)
        # This is a d_3-type differential, independent of [m_3, B^{(2)}] non-adj

    def test_hopf_decomposition_exists(self):
        """The Hopf fibration decomposition module exists and loads."""
        from compute.lib.hopf_fibration_s3_framing import (
            HopfFibrationData,
            ConnesHierarchy,
        )
        # VERIFIED [DC] module existence [DA] import succeeds
        hopf = HopfFibrationData()
        assert hopf.topological_obstruction_vanishes()
        hierarchy = ConnesHierarchy.for_cy3()
        assert len(hierarchy.levels) == 4
