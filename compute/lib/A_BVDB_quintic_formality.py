r"""Carrier-separated quintic/BVDB formality diagnostics.

This engine records exact data for the smooth Fermat quintic
``X_5 \subset P^4`` and the Bondal--Van den Bergh compact generator

    E_BVDB = O_X + O_X(1) + O_X(2) + O_X(3) + O_X(4).

It is deliberately not a proof that compact Calabi--Yau threefold
``Obs_Ainf`` vanishes, that ``HH^{-2}`` vanishes, that an ``S^3`` framing is
contractible, that compact ``Phi_3`` is constructed, or that Hall/CoHA,
PBW, or no-extra-relations data follow.

AP-CY34 firewall
================

The raw terminal-slot pair contraction ``B_term^(2)`` is not Costello's
corrected TCFT operator ``B_TCFT^(2)``.  The strict cyclic CY3 witness is

    [m_3,B_term^(2)][a|a|a|a|b] = 2 alpha [b] != 0

in characteristic zero.  A positive compact CY3 closure therefore requires
one of two supplied mechanisms:

* explicit ``B_TCFT^(2)`` correction/comparison data; or
* an ``HH^{-2}`` filtration theorem with comparison map, complete,
  exhaustive, separated strong convergence, and an empty total-degree
  ``-2`` line.

The quintic constants below are useful diagnostics:

* ``H^3 = 5`` for the hyperplane class on ``X_5``;
* ``n_1^(0) = 2875`` lines on the quintic;
* ``n_2^(0) = 609250`` conics, giving the Yukawa coefficient
  ``2875 + 8 * 609250 = 4876875`` at ``q^2``.

Those constants prove that the formal Yukawa series is not identically zero
at the large-radius expansion.  They do not by themselves prove global
non-vanishing on moduli or transfer a nonzero ``m_3`` from the
Kodaira--Spencer/polyvector carrier to this particular BVDB minimal model.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb
from typing import Dict, List, Tuple

F = Fraction


# ===========================================================================
# 0. Anti-implication firewall
# ===========================================================================

AUTOMATIC_SOURCE_MECHANISMS: Tuple[str, ...] = (
    "DGMS",
    "BTT",
    "Kaledin",
    "BVDB_compact_generator",
    "strict_or_curved_formality_label",
    "Yukawa_diagnostic",
    "quintic_numerics",
)

FORBIDDEN_AUTOMATIC_TARGETS: Tuple[str, ...] = (
    "universal_compact_cy3_Obs_Ainf_zero",
    "HH_minus_2_zero",
    "contractible_S3_framing",
    "compact_Phi_3_constructed",
    "Hall_or_CoHA_constructed",
    "PBW_flatness",
    "no_extra_relations",
)


def automatic_implication_firewall() -> Dict[str, object]:
    """Return the AP-CY34 firewall matrix.

    Every entry is intentionally ``False``: none of the listed mechanisms is
    allowed to imply any of the listed compact CY3 closure targets without
    the explicit comparison data checked elsewhere in this file.
    """

    matrix = {
        source: {target: False for target in FORBIDDEN_AUTOMATIC_TARGETS}
        for source in AUTOMATIC_SOURCE_MECHANISMS
    }
    return {
        "all_forbidden_implications_rejected": True,
        "sources": AUTOMATIC_SOURCE_MECHANISMS,
        "targets": FORBIDDEN_AUTOMATIC_TARGETS,
        "matrix": matrix,
        "normalization": (
            "DGMS/BTT/Kaledin/BVDB/formality/Yukawa/quintic diagnostics are "
            "evidence or input data only; they are not compact CY3 closure "
            "theorems."
        ),
    }


# ===========================================================================
# 1. Hodge data of the quintic and cohomology of O(d)
# ===========================================================================

QUINTIC_HODGE: Dict[Tuple[int, int], int] = {
    (0, 0): 1,
    (3, 3): 1,
    (0, 3): 1,
    (3, 0): 1,
    (1, 1): 1,
    (2, 2): 1,
    (2, 1): 101,
    (1, 2): 101,
}
for _p in range(4):
    for _q in range(4):
        QUINTIC_HODGE.setdefault((_p, _q), 0)


def hq_o_d_quintic(d: int) -> List[int]:
    """Return ``[h^0, h^1, h^2, h^3]`` of ``O_{X_5}(d)``.

    The calculation uses the hypersurface Koszul sequence
    ``0 -> O_{P^4}(d-5) -> O_{P^4}(d) -> O_X(d) -> 0`` and Serre duality on
    the Calabi--Yau threefold.
    """

    if d >= 0:
        h0_p_d = comb(d + 4, 4)
        h0_p_d5 = comb(d - 1, 4) if d >= 5 else 0
        h0 = h0_p_d - h0_p_d5
        h3 = 1 if d == 0 else 0
        return [h0, 0, 0, h3]

    md = -d
    h3 = comb(md + 4, 4) - (comb(md - 1, 4) if md >= 5 else 0)
    return [0, 0, 0, h3]


# ===========================================================================
# 2. A_BVDB structure: dimension, degree distribution, (-3)-CY pairing
# ===========================================================================


def a_bvdb_total_dimension() -> int:
    """Total cohomological dimension of ``End^*(E_BVDB)``."""

    return sum(
        sum(hq_o_d_quintic(j - i))
        for i in range(5)
        for j in range(5)
    )


def a_bvdb_dim_by_degree() -> Dict[int, int]:
    """Dimensions of ``A_BVDB`` in cohomological degrees ``0,1,2,3``."""

    by_deg: Dict[int, int] = {0: 0, 1: 0, 2: 0, 3: 0}
    for i in range(5):
        for j in range(5):
            for q, dim in enumerate(hq_o_d_quintic(j - i)):
                by_deg[q] += dim
    return by_deg


def a_bvdb_is_minus_3_cy() -> Dict[str, object]:
    """Record the Serre-duality dimension check for the ``(-3)`` pairing."""

    by_deg = a_bvdb_dim_by_degree()
    return {
        "dim_0": by_deg[0],
        "dim_1": by_deg[1],
        "dim_2": by_deg[2],
        "dim_3": by_deg[3],
        "serre_symmetry_0_3": by_deg[0] == by_deg[3],
        "serre_symmetry_1_2": by_deg[1] == by_deg[2],
        "total_dim": sum(by_deg.values()),
        "cy_degree": -3,
        "pairing_target": "H^3(O_{X_5}) = k",
        "scope": (
            "Serre duality gives the pairing datum. It is not an "
            "Obs_Ainf or HH^{-2} vanishing theorem."
        ),
    }


# ===========================================================================
# 3. The Yukawa coupling: exact large-radius coefficients
# ===========================================================================

QUINTIC_TRIPLE_INTERSECTION: int = 5

QUINTIC_BPS_GENUS_0: Dict[int, int] = {
    1: 2875,
    2: 609250,
    3: 317206375,
    4: 242467530000,
    5: 229305888887625,
}


def yukawa_classical() -> int:
    """Classical Yukawa coupling ``Y_3(0) = H^3 = 5``."""

    return QUINTIC_TRIPLE_INTERSECTION


def yukawa_q_expansion(d_max: int) -> Dict[int, Fraction]:
    r"""Expand ``Y_3(q)`` through ``q^d_max``.

    The convention is

    ``Y_3 = 5 + sum_{d>=1} n_d^(0) d^3 q^d/(1-q^d)``.
    """

    coeffs: Dict[int, Fraction] = {0: F(QUINTIC_TRIPLE_INTERSECTION)}
    for m in range(1, d_max + 1):
        coeffs[m] = F(0)
        for d in range(1, m + 1):
            if m % d == 0 and d in QUINTIC_BPS_GENUS_0:
                coeffs[m] += F(QUINTIC_BPS_GENUS_0[d]) * d**3
    return coeffs


def yukawa_is_nonvanishing() -> Dict[str, object]:
    """Safe nonzero diagnostic for the large-radius formal series.

    The old engine treated a nonzero formal expansion as a theorem that the
    Yukawa coupling is nowhere zero on moduli.  This function now records the
    weaker statement actually checked here: the formal series is not
    identically zero because its constant term is ``5``.
    """

    coeffs = yukawa_q_expansion(2)
    return {
        "constant_term": int(coeffs[0]),
        "q_coefficient": int(coeffs[1]),
        "q2_coefficient": int(coeffs[2]),
        "constant_term_is_classical_intersection": coeffs[0] == QUINTIC_TRIPLE_INTERSECTION,
        "formal_series_not_identically_zero": coeffs[0] != 0,
        "global_zero_locus_known_empty": False,
        "vanishing_locus_in_moduli": "not_computed_by_this_engine",
        "scope": (
            "Large-radius formal Yukawa diagnostic only; no universal compact "
            "CY3 obstruction closure follows."
        ),
    }


# ===========================================================================
# 4. Kodaira-Spencer carrier and BVDB transfer boundary
# ===========================================================================


def kodaira_spencer_dim_h1() -> int:
    """``dim H^1(T_{X_5}) = h^{2,1}(X_5) = 101``."""

    return QUINTIC_HODGE[(2, 1)]


def kodaira_spencer_dim_h2() -> int:
    """``dim H^2(T_{X_5}) = h^{2,2}(X_5) = 1``."""

    return QUINTIC_HODGE[(2, 2)]


def m3_kodaira_spencer_dimension() -> Dict[str, object]:
    """Dimension data for the Kodaira--Spencer Yukawa carrier."""

    h1 = kodaira_spencer_dim_h1()
    h2 = kodaira_spencer_dim_h2()
    sym3_dim = comb(h1 + 2, 3)
    return {
        "h1_T_dim": h1,
        "h2_T_dim": h2,
        "sym3_h1_dim": sym3_dim,
        "m3_source_dim": sym3_dim,
        "m3_target_dim": h2,
        "m3_is_zero_morphism_on_ks_carrier": False,
        "m3_is_yukawa_coupling_on_ks_carrier": True,
        "a_bvdb_transfer_map_supplied": False,
    }


def m3_obstruction_via_yukawa() -> Dict[str, object]:
    """Carrier-separated status of the Yukawa ``m_3`` diagnostic."""

    yukawa = yukawa_is_nonvanishing()
    m3_dim = m3_kodaira_spencer_dimension()
    return {
        "carrier": "Kodaira-Spencer/polyvector Frobenius-manifold carrier",
        "m3_obstruction_class": (
            "Yukawa series Y_3 = H^3 + sum n_d^(0) d^3 q^d/(1-q^d)"
        ),
        "classical_value": yukawa["constant_term"],
        "first_gw_correction": yukawa["q_coefficient"],
        "barannikov_kontsevich_identification_scope": "KS/polyvector carrier",
        "ks_yukawa_nonzero": yukawa["formal_series_not_identically_zero"],
        "a_bvdb_obstruction_nonzero_proved": False,
        "requires_bvdb_ks_comparison_map": True,
        "obstruction_dim_data": m3_dim,
        "vanishing_in_moduli": yukawa["vanishing_locus_in_moduli"],
        "consequence_for_formality": (
            "No strict A_BVDB formality verdict follows without an explicit "
            "comparison map from the KS/Yukawa carrier to the chosen BVDB "
            "minimal model."
        ),
    }


# ===========================================================================
# 5. Calaque--Halbout--Felder route: ambient torus does not restrict
# ===========================================================================


def torus_action_p4_dimension() -> int:
    """Dimension of the maximal torus ``(C^*)^4`` acting on ``P^4``."""

    return 4


def torus_action_preserves_quintic() -> bool:
    """The ambient ``(C^*)^4`` action does not preserve the Fermat quintic."""

    return False


def quintic_continuous_symmetry_group() -> Dict[str, object]:
    """Connected automorphism group data for the Fermat quintic.

    The vanishing of continuous vector fields follows from
    ``H^0(T_X) = H^{2,0}(X) = 0`` for a strict CY3.  This is not a BTT
    unobstructedness argument.
    """

    return {
        "connected_component": "trivial",
        "continuous_torus_exists": False,
        "max_torus_dim_acting": 0,
        "discrete_aut_fermat": "(Z/5)^3 rtimes S_5",
        "discrete_aut_order": 5**3 * 120,
        "reason": "H^0(T_X)=H^{2,0}(X)=0; BTT is not used.",
    }


def calaque_halbout_felder_applicability() -> Dict[str, object]:
    """The torus-equivariant formality criterion is unavailable for ``X_5``."""

    return {
        "x5_is_toric": False,
        "p4_torus_preserves_x5": torus_action_preserves_quintic(),
        "x5_connected_automorphism_group": "trivial",
        "calaque_halbout_felder_applies": False,
        "reason": (
            "The Fermat equation is preserved by fifth-root scalars and "
            "permutations, not by the continuous ambient torus."
        ),
        "does_not_imply": FORBIDDEN_AUTOMATIC_TARGETS,
        "actual_next_steps": (
            "Supply a BVDB-KS comparison map, corrected B_TCFT^(2) data, "
            "or the HH^{-2} filtration theorem."
        ),
    }


# ===========================================================================
# 6. Raw B_term^(2), corrected B_TCFT^(2), and HH^{-2} gates
# ===========================================================================


@dataclass(frozen=True)
class RawBTerm2Witness:
    """Strict cyclic CY3 witness for the raw pair-contraction operator."""

    alpha: Fraction
    input_word: Tuple[str, ...] = ("a", "a", "a", "a", "b")
    b_term2_output_coeff: Fraction = F(4)
    m3_after_b_term2_coeff: Fraction = F(4)
    b_term2_after_m3_coeff: Fraction = F(2)
    commutator_coeff: Fraction = F(2)

    @property
    def nonzero(self) -> bool:
        return self.commutator_coeff != 0

    @property
    def formula(self) -> str:
        return "[m_3,B_term^(2)][a|a|a|a|b] = 2 alpha [b] != 0"


def raw_b_term2_witness(alpha: Fraction | int = F(1)) -> Dict[str, object]:
    """Return the normalized raw ``B_term^(2)`` witness."""

    a = F(alpha)
    witness = RawBTerm2Witness(
        alpha=a,
        b_term2_output_coeff=4,
        m3_after_b_term2_coeff=4 * a,
        b_term2_after_m3_coeff=2 * a,
        commutator_coeff=2 * a,
    )
    return {
        "raw_operator": "B_term^(2)",
        "corrected_operator": "B_TCFT^(2)",
        "raw_is_corrected_tcft": False,
        "alpha": witness.alpha,
        "input_word": witness.input_word,
        "B_term_then_m3_coeff": witness.m3_after_b_term2_coeff,
        "m3_then_B_term_coeff": witness.b_term2_after_m3_coeff,
        "commutator_coeff": witness.commutator_coeff,
        "nonzero": witness.nonzero,
        "formula": witness.formula,
    }


BTCFT2_REQUIREMENTS: Tuple[str, ...] = (
    "corrected_operator_chosen",
    "costello_moduli_chain_correction_terms",
    "open_closed_tcft_chain_map",
    "orientation_signs_fixed",
    "comparison_map_from_raw_B_term_to_B_TCFT",
)

HH_MINUS_TWO_REQUIREMENTS: Tuple[str, ...] = (
    "comparison_map_to_obstruction_complex",
    "filtration_complete",
    "filtration_exhaustive",
    "filtration_separated",
    "strong_convergence",
    "empty_total_degree_minus_two_line",
)


def b_tcft2_comparison_check(
    *,
    corrected_operator_chosen: bool = False,
    costello_moduli_chain_correction_terms: bool = False,
    open_closed_tcft_chain_map: bool = False,
    orientation_signs_fixed: bool = False,
    comparison_map_from_raw_B_term_to_B_TCFT: bool = False,
) -> Dict[str, object]:
    """Check whether the corrected ``B_TCFT^(2)`` route has been supplied."""

    supplied = {
        "corrected_operator_chosen": corrected_operator_chosen,
        "costello_moduli_chain_correction_terms": costello_moduli_chain_correction_terms,
        "open_closed_tcft_chain_map": open_closed_tcft_chain_map,
        "orientation_signs_fixed": orientation_signs_fixed,
        "comparison_map_from_raw_B_term_to_B_TCFT": comparison_map_from_raw_B_term_to_B_TCFT,
    }
    missing = [name for name, ok in supplied.items() if not ok]
    return {
        "route": "corrected_B_TCFT^(2)",
        "established": not missing,
        "total_identity": "{sum_k b_k, B_TCFT^(2)} = 0" if not missing else None,
        "raw_operator_identified_with_tcft": False,
        "per_k_identity_claimed": False,
        "missing_hypotheses": missing,
    }


def hh_minus_two_filtration_check(
    *,
    comparison_map_to_obstruction_complex: bool = False,
    filtration_complete: bool = False,
    filtration_exhaustive: bool = False,
    filtration_separated: bool = False,
    strong_convergence: bool = False,
    empty_total_degree_minus_two_line: bool = False,
) -> Dict[str, object]:
    """Check the explicit hypotheses for ``HH^{-2}_{E_1}`` vanishing."""

    supplied = {
        "comparison_map_to_obstruction_complex": comparison_map_to_obstruction_complex,
        "filtration_complete": filtration_complete,
        "filtration_exhaustive": filtration_exhaustive,
        "filtration_separated": filtration_separated,
        "strong_convergence": strong_convergence,
        "empty_total_degree_minus_two_line": empty_total_degree_minus_two_line,
    }
    missing = [name for name, ok in supplied.items() if not ok]
    return {
        "route": "HH^{-2}_filtration",
        "vanishes": not missing,
        "missing_hypotheses": missing,
        "proof_summary": (
            "The total degree -2 line is empty on E_1; complete, exhaustive, "
            "separated strong convergence transfers the vanishing to the "
            "target obstruction group."
            if not missing
            else (
                "Connectivity, H^0(O_X)=k, DGMS, BTT, Kaledin, BVDB, "
                "and Yukawa data do not replace these checks."
            )
        ),
    }


def positive_closure_gate(
    *,
    corrected_operator_chosen: bool = False,
    costello_moduli_chain_correction_terms: bool = False,
    open_closed_tcft_chain_map: bool = False,
    orientation_signs_fixed: bool = False,
    comparison_map_from_raw_B_term_to_B_TCFT: bool = False,
    comparison_map_to_obstruction_complex: bool = False,
    filtration_complete: bool = False,
    filtration_exhaustive: bool = False,
    filtration_separated: bool = False,
    strong_convergence: bool = False,
    empty_total_degree_minus_two_line: bool = False,
) -> Dict[str, object]:
    """Return the compact CY3 closure verdict under supplied hypotheses."""

    witness = raw_b_term2_witness()
    tcft = b_tcft2_comparison_check(
        corrected_operator_chosen=corrected_operator_chosen,
        costello_moduli_chain_correction_terms=costello_moduli_chain_correction_terms,
        open_closed_tcft_chain_map=open_closed_tcft_chain_map,
        orientation_signs_fixed=orientation_signs_fixed,
        comparison_map_from_raw_B_term_to_B_TCFT=comparison_map_from_raw_B_term_to_B_TCFT,
    )
    hh = hh_minus_two_filtration_check(
        comparison_map_to_obstruction_complex=comparison_map_to_obstruction_complex,
        filtration_complete=filtration_complete,
        filtration_exhaustive=filtration_exhaustive,
        filtration_separated=filtration_separated,
        strong_convergence=strong_convergence,
        empty_total_degree_minus_two_line=empty_total_degree_minus_two_line,
    )
    closes = bool(tcft["established"] or hh["vanishes"])
    return {
        "raw_B_term_closes": False,
        "raw_witness": witness,
        "corrected_B_TCFT_route": tcft,
        "HH_minus_two_route": hh,
        "positive_closure_established": closes,
        "status": (
            "closed_under_supplied_corrected_TCFT_or_HH_minus_two_data"
            if closes
            else "open"
        ),
        "remaining_obligations": (
            []
            if closes
            else list(tcft["missing_hypotheses"]) + list(hh["missing_hypotheses"])
        ),
    }


# ===========================================================================
# 7. Formality status reports
# ===========================================================================


def a_bvdb_strict_formality_status() -> Dict[str, object]:
    """Safe status report for strict BVDB formality/non-formality."""

    yukawa = yukawa_is_nonvanishing()
    m3_obs = m3_obstruction_via_yukawa()
    chf = calaque_halbout_felder_applicability()
    return {
        "is_formal_strict": "not_established",
        "strict_formality_proved": False,
        "strict_nonformality_proved": False,
        "obstruction_class": "Yukawa diagnostic on KS/polyvector carrier",
        "obstruction_classical_value": yukawa["constant_term"],
        "obstruction_first_correction": yukawa["q_coefficient"],
        "calaque_halbout_felder_applicable": chf["calaque_halbout_felder_applies"],
        "barannikov_kontsevich_yukawa_is_m3_on_ks": True,
        "bvdb_ks_comparison_map_supplied": False,
        "a_bvdb_obstruction_nonzero_proved": m3_obs["a_bvdb_obstruction_nonzero_proved"],
        "automatic_implication_firewall": automatic_implication_firewall(),
        "compact_cy3_closure_gate": positive_closure_gate(),
        "mechanism": (
            "The engine verifies exact quintic Yukawa coefficients and the "
            "failure of the torus criterion. It does not transfer the KS "
            "m_3 to A_BVDB or prove a compact CY3 closure theorem."
        ),
    }


def a_bvdb_curved_formality_conjecture() -> Dict[str, object]:
    """Conditional curved-formality target, not a theorem from this engine."""

    return {
        "candidate_statement": (
            "A curved (-3)-CY A_inf model related to the quintic BVDB "
            "generator should compare with the BCOV cubic/Yukawa carrier "
            "after an explicit chain-level comparison is constructed."
        ),
        "curving_datum_candidate": "BCOV/Yukawa cubic vertex",
        "underlying_framework": "Costello-Li BCOV BV-quantization",
        "status": "OPEN_CONDITIONAL",
        "curved_formality_proved": False,
        "requires": [
            "explicit curved A_inf quasi-isomorphism",
            "comparison from BCOV cubic vertex to the BVDB minimal model",
            "separation of B_term^(2) from B_TCFT^(2)",
            "compact CY3 closure via corrected TCFT data or HH^{-2} theorem",
        ],
        "does_not_imply": FORBIDDEN_AUTOMATIC_TARGETS,
    }


def healed_platonic_statement() -> Dict[str, object]:
    """Attack-healed status summary for the quintic/BVDB lane."""

    return {
        "current_status_strict": (
            "OPEN: this engine proves neither strict formality nor strict "
            "non-formality of the chosen A_BVDB minimal model."
        ),
        "current_status_curved": "OPEN_CONDITIONAL",
        "ingredient_a_bvdb_compact_generator": "PROVED (Bondal-Van den Bergh compact generation)",
        "ingredient_b_ptvv_neg_3_shifted_symplectic": "PROVED (PTVV shifted symplectic input)",
        "ingredient_c_ks_yukawa_diagnostic": "COMPUTED (H^3=5, n_1=2875, q^2=4876875)",
        "ingredient_d_bvdb_ks_transfer": "OPEN",
        "ingredient_e_compact_s3_closure": "OPEN unless corrected TCFT or HH^{-2} data are supplied",
        "next_open_problem": (
            "Construct the BVDB-KS comparison and either B_TCFT^(2) "
            "comparison/correction data or the HH^{-2} filtration theorem."
        ),
    }


# ===========================================================================
# 8. Verify_all entry point
# ===========================================================================


def verify_all() -> Dict[str, object]:
    """Run all diagnostics and return the carrier-separated report."""

    return {
        "a_bvdb_total_dim": a_bvdb_total_dimension(),
        "a_bvdb_dim_by_degree": a_bvdb_dim_by_degree(),
        "a_bvdb_minus_3_cy": a_bvdb_is_minus_3_cy(),
        "yukawa_classical": yukawa_classical(),
        "yukawa_q_expansion_to_3": {k: int(v) for k, v in yukawa_q_expansion(3).items()},
        "yukawa_nonvanishing": yukawa_is_nonvanishing(),
        "kodaira_spencer_h1_T": kodaira_spencer_dim_h1(),
        "kodaira_spencer_h2_T": kodaira_spencer_dim_h2(),
        "m3_dimensions": m3_kodaira_spencer_dimension(),
        "m3_obstruction": m3_obstruction_via_yukawa(),
        "torus_p4_preserves_x5": torus_action_preserves_quintic(),
        "quintic_continuous_symmetry": quintic_continuous_symmetry_group(),
        "calaque_halbout_felder_applies": calaque_halbout_felder_applicability(),
        "raw_b_term2_witness": raw_b_term2_witness(),
        "positive_closure_gate": positive_closure_gate(),
        "automatic_implication_firewall": automatic_implication_firewall(),
        "strict_formality_status": a_bvdb_strict_formality_status(),
        "curved_formality_conjecture": a_bvdb_curved_formality_conjecture(),
        "healed_platonic": healed_platonic_statement(),
    }
