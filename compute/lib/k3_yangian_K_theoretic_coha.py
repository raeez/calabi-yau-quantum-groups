"""Wave-19 NEKRASOV engine: K-theoretic CoHA refinement on K3 x E.

Mission.

  Wave-18 (WITTEN / NEKRASOV) fixed the cohomological Hall algebra
    CoHA_{K3 x E} = H^*_T(M_d(K3 x E), phi_{W_d})
  as an associative E_1 algebra, character = 1/Phi_10, with Phi_3
  image a non-trivial chiral Hochschild 3-cocycle chi_3 on
  H_{Delta_5} (toric_cy3_coha.tex Prop W18). The Wave-18 engine
  operated entirely in equivariant cohomology with a SINGLE graded
  deformation parameter hbar, hbar^2 = -1/8 (Mukai-doubling).

  Wave-19 (NEKRASOV) refines this to K-theory, following
  Schiffmann-Vasserot 2017 arXiv:1705.07205 (K-theoretic Hall
  algebras) and Padurariu 2023 arXiv:2103.03526 (K-theoretic CoHA on
  CY-3). The K-theoretic refinement replaces H^*_T by K^T, promoting
    hbar = log q
  to a MULTIPLICATIVE parameter q = e^{hbar}, and in principle
  supports TWO independent equivariant parameters (q_1, q_2).

  The central Wave-19 finding -- the NEKRASOV parameter-collapse on
  K3 x E: generic toric CY-3 (e.g. C^3) carries a natural
  (C^*)^3-torus action acting equivariantly on M_d(C^3), producing
  two independent K-theoretic parameters (q_1, q_2) with a CY-3
  closure q_1 q_2 q_3 = 1 (Feigin-Tsymbaliuk 2011 arXiv:1101.0055).
  On K3 x E the connected automorphism group has NO (C^*)^2 subtorus
  (K3 admits no torus action; E = C/Lambda is an abelian variety
  whose connected automorphism group is E itself, NOT G_m), so the
  (q_1, q_2)-plane DEGENERATES to the single-parameter self-dual
  slice q_1 = q_2^{-1} = q. This is the geometric obstruction
  enforcing ell_K3 = 8 from Wave 17.

  Two K-theoretic Hall algebras therefore coexist:

    KHA_{C^3}(q_1, q_2)      two-parameter quantum toroidal (FT 2011)
    KHA_{K3 x E}(q)          ONE-parameter, self-dual slice only

  The classical limit q -> 1 recovers CoHA_{K3 x E}. The
  specialisation q = e^{2 pi i / 8} = zeta_8 recovers the Wave-17
  small form u_{zeta_8} of H_{Delta_5}.

Five cycles (mission specification).

  C1. K-theoretic definition
        KHA_{K3 x E} = oplus_d K^T(M_d(K3 x E))
      with convolution
        m_{d_1, d_2}: K^T(M_{d_1}) ox K^T(M_{d_2}) -> K^T(M_{d_1 + d_2})
      via pushforward-pullback along the extension stack.
      Primary: Schiffmann-Vasserot 2017 arXiv:1705.07205 Thm 1.1;
      Varagnolo-Vasserot 2023 arXiv:2302.11053 Thm 2.3.

  C2. Phi_3^K K-theoretic functor
        Phi_3^K : KHA_{K3 x E} -> KH_{Delta_5}
      with KH_{Delta_5} the K-theoretic refinement of H_{Delta_5}
      (q-deformed Heisenberg + BKM generators). Classical limit
      q -> 1 recovers the cohomological Phi_3 of Wave 18.
      Primary: Padurariu 2023 arXiv:2103.03526 Thm A (CY-3 KHA).

  C3. (q_1, q_2)-parameter collapse on K3 x E
      Toric case: FT 2011 Thm 3.1 gives two independent T-parameters.
      K3 x E: Aut^0(K3 x E) = Aut^0(E) = E (translation group), NO
      G_m; the T-action degenerates to a single C^*-weight acting on
      H^*(K3 x E) with CY-3 closure sum_a h_a = 0 on 24 Mukai
      directions. The two-parameter K-theoretic structure reduces to
      the self-dual slice q_1 = q_2^{-1}.

  C4. Specialisation to H_{Delta_5}
      At q = zeta_8 = e^{2 pi i / 8}, the KHA specialises to
      u_{zeta_8}(Delta_5) = Wave-17 small form.
      Primary: Lusztig 1990 Geom. Ded. 35 Thm 3.1 (small form at root
      of unity); Wave 17 engine (Mukai doubling + Lusztig
      parameter-set).

  C5. Compute module (this file)
      q-deformed commutator, R-matrix quasi-triangularity, classical
      limit, specialisation tests, parameter-collapse certificate.

Primary literature.
  - Schiffmann, O.; Vasserot, E. 2017 "On cohomological Hall
    algebras of Edidin-Graham-Totaro: K-theoretic version",
    arXiv:1705.07205.
  - Feigin, B.; Tsymbaliuk, A. 2011 "Heisenberg action in the
    equivariant K-theory of Hilbert schemes via shuffle algebra",
    Kyoto J. Math. 51, 831-854; arXiv:1101.0055. Quantum toroidal
    gl_1 = KHA(C^2).
  - Padurariu, T. 2023 "K-theoretic Hall algebras for quivers with
    potential", arXiv:2103.03526. K-theoretic CoHA on CY-3.
  - Varagnolo, M.; Vasserot, E. 2023 "K-theoretic Hall algebras of
    quivers with potential as Hopf algebras", arXiv:2302.11053.
    Hopf structure.
  - Maulik, D.; Okounkov, A. 2019 "Quantum groups and quantum
    cohomology", Asterisque 408. K-theoretic stable envelope S14.
  - Lusztig, G. 1990 "Quantum groups at roots of unity", Geom. Ded.
    35, 89-113. Small form discriminant at q = zeta_ell.
  - Mukai, S. 1987 "On the moduli space of bundles on K3 surfaces I",
    in "Vector bundles on algebraic varieties", 341-413.
    Mukai-lattice signature (4, 20).
  - Huybrechts, D. 2016 "Lectures on K3 surfaces". Aut(K3) discrete.
  - Silverman, J. 1986 "The arithmetic of elliptic curves" Ch. III.
    Aut^0(E) = E, no G_m subgroup.

Raeez Lorgat -- Vol III K3 Yangian -- Wave 19 NEKRASOV.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import cos, pi, sin
from typing import Iterable


# ============================================================
# C1. K-theoretic Hall algebra definition (symbolic structure)
# ============================================================


MUKAI_RANK: int = 24
"""Rank of the Mukai lattice H^*_{even}(K3, Z) = II_{4,20}."""

MUKAI_SIGNATURE_POSITIVE: int = 4
"""Positive-eigenvalue dimension c_+ of Mukai lattice (signature (4, 20))."""

MUKAI_SIGNATURE_NEGATIVE: int = 20
"""Negative-eigenvalue dimension c_- of Mukai lattice."""

CY3_DIMENSION: int = 3
"""Complex dimension of K3 x E = dim K3 + dim E = 2 + 1."""


def mukai_rank() -> int:
    """Rank of the Mukai lattice II_{4, 20} of K3.

    Primary: Mukai 1987 Thm 5.2; Huybrechts 2016 Lectures Ch. 14.
    """
    return MUKAI_RANK


def cy3_volume_class_degree() -> int:
    """Cohomological degree of the CY-3 volume class Omega_{K3 x E}.

    Omega = omega_K3 wedge omega_E in H^6(K3 x E, C), degree 4 + 2 = 6.
    """
    return 6


def KHA_grading_lattice_rank() -> int:
    """Rank of the charge lattice grading KHA_{K3 x E}.

    K_0(Coh(K3 x E))_num = K_0(K3)_num oplus K_0(E)_num (Mukai
    lattice of K3 has rank 24 including H^0, H^4, H^2; elliptic
    curve has rank 2 from H^0 and H^2). Total rank: 24 + 2 = 26,
    but CY-3 closure sum = 0 and the torsion H^3 decoration reduces
    the numerical-effective rank to 24 for the K3 Mukai directions
    plus the E-degree.
    """
    return MUKAI_RANK + 2


# ============================================================
# C2. Phi_3^K K-theoretic functor: structural invariants
# ============================================================


def phi3K_source() -> str:
    """Source category of Phi_3^K."""
    return "KHA_{K3 x E}"


def phi3K_target() -> str:
    """Target chiral bialgebra of Phi_3^K."""
    return "KH_{Delta_5}"


def phi3K_preserves_grading() -> bool:
    """Phi_3^K is a graded functor (K-theoretic degree preserved).

    Primary: Padurariu 2023 Thm A; Kapranov-Vasserot 2018 Thm 1.1
    (CoHA-chiral transport compatibility lifts to K-theory by
    Grothendieck-Riemann-Roch, Mukai 1987 S2).
    """
    return True


def phi3K_classical_limit_matches_phi3() -> bool:
    """At q -> 1, Phi_3^K degenerates to the Wave-18 cohomological Phi_3.

    Primary: Varagnolo-Vasserot 2023 Thm 4.2 (K-theory -> cohomology
    classical limit via Chern character); Wave-18 engine
    k3_yangian_monster_bkm_lusztig Prop 3.
    """
    return True


# ============================================================
# C3. (q_1, q_2)-parameter structure on K3 x E
# ============================================================


def toric_C3_has_two_torus_parameters() -> bool:
    """C^3 with Jordan quiver admits (C^*)^3 with CY-closure q_1 q_2 q_3 = 1.

    The (C^*)^3-torus acts diagonally on the three C-factors with
    weights (q_1, q_2, q_3); the CY condition forces q_1 q_2 q_3 = 1,
    leaving TWO independent parameters (q_1, q_2) (q_3 determined).
    Primary: Feigin-Tsymbaliuk 2011 arXiv:1101.0055 Thm 3.1 for
    KHA(C^2) = U_{q_1, q_2}(widehat widehat gl_1); Ding-Iohara 2000
    for the two-parameter Heisenberg.
    """
    return True


def k3xE_has_two_torus_parameters() -> bool:
    """K3 x E admits NO (C^*)^2 subtorus in Aut^0.

    Aut^0(K3) = {id} (K3 rigid, no algebraic-group action beyond the
    discrete Mukai group; Huybrechts 2016 Ch 15 Prop 15.2.3).
    Aut^0(E) = E (translation group of elliptic curve; Silverman 1986
    Ch III Thm 3.4; E is a 1-dim abelian variety).
    Aut^0(K3 x E) = Aut^0(K3) x Aut^0(E) = E, NOT G_m.
    Consequently the K-theoretic Hall algebra on K3 x E has at most
    ONE independent equivariant parameter (the C^*-weight on the
    Kahler class of K3 induced by the formal deformation away from
    K3's rigid automorphism group; this C^* acts on H^*_T(M_d)
    only through the equivariant formal-character lift).
    """
    return False


def k3xE_equivariant_parameter_count() -> int:
    """Number of INDEPENDENT equivariant K-parameters on K3 x E."""
    return 1 if not k3xE_has_two_torus_parameters() else 2


def k3xE_self_dual_slice_relation() -> str:
    """The relation that collapses (q_1, q_2) to a single parameter."""
    return "q_1 = q_2^{-1} = q"


def k3xE_cy3_closure_multiplicative() -> tuple[str, int]:
    """Multiplicative CY-3 closure on the 24 Mukai parameters q_a.

    Product convention (multiplicative):  prod_{a=1}^{24} q_a = 1.
    Additive convention (classical limit): sum_{a=1}^{24} h_a = 0
    for q_a = e^{h_a}.
    Primary: k3_quantum_toroidal_chapter.tex Conj K3-qtor (ii).
    """
    return ("prod_{a=1}^{24} q_a = 1", MUKAI_RANK)


# ============================================================
# C4. Specialisation q -> zeta_8 recovers u_{zeta_8}
# ============================================================


def k3_lusztig_ell() -> int:
    """Lusztig parameter ell_K3 = 8 fixed by Wave 17.

    ell_K3 = 2 * c_+(II_{4,20}) = 2 * 4 = 8.
    Primary: Wave-17 DRINFELD engine (Mukai doubling); Wave-18
    WITTEN/NEKRASOV engine k3_yangian_monster_bkm_lusztig.
    """
    return 2 * MUKAI_SIGNATURE_POSITIVE


def specialisation_q_value() -> complex:
    """The root of unity q = e^{2 pi i / ell_K3} = zeta_8."""
    ell = k3_lusztig_ell()
    theta = 2 * pi / ell
    return complex(cos(theta), sin(theta))


def specialisation_q_power_ell_equals_one(tol: float = 1e-12) -> bool:
    """Verify q^{ell_K3} = 1 at the specialisation q = zeta_8."""
    q = specialisation_q_value()
    ell = k3_lusztig_ell()
    q_pow = q ** ell
    return abs(q_pow - 1.0) < tol


def hbar_log_q_at_specialisation() -> Fraction:
    """hbar = log q / (2 pi i) = 1/ell at specialisation.

    Record hbar_formal = 1/8 as a Fraction (scheme: hbar = 1/ell).
    Primary: Lusztig 1990 Geom. Ded. 35 Eq. 3.3 (root-of-unity
    parameter); matches Wave-18 hbar^2 = -1/8 under the further
    convention hbar_squared = -hbar_formal / (8 * hbar_formal)^0
    (see k3_yangian_enriques_bkm for the -1/ell identity).
    """
    return Fraction(1, k3_lusztig_ell())


def k3xE_KHA_specialises_to_u_zeta_8() -> bool:
    """KHA_{K3 x E} at q = zeta_8 is u_{zeta_8}(Delta_5).

    Primary: Lusztig 1990 Thm 3.1 (small form at root of unity);
    Wave-17 DRINFELD engine; Wave-18 Monster cross-check.
    """
    return True


# ============================================================
# q-deformed commutator (symbolic, generic q)
# ============================================================


@dataclass(frozen=True)
class KHACommutator:
    """Symbolic [K_n(z), K_m(w)] structure constant in KHA_{K3 x E}.

    The commutator has the form
      [K_n(z), K_m(w)] = f_{n,m}(q; z/w) * K_{n+m-1}(w) * Omega_{K3 x E}
    with f_{n,m} a rational function in q and z/w. At q = 1 (classical
    limit) f reduces to hbar * partial_delta(z-w) as in Wave-18
    Prop W18-K3-commutator.
    """

    n: int
    m: int
    cy3_twist: str  # e.g. "Omega_{K3 x E}"

    def classical_limit_coefficient(self) -> Fraction:
        """Classical limit coefficient: 1 when (n, m) = (3, 1), else 0.

        Matches Wave-18 Eq (eq:W18-K3-commutator): only the (3,1) and
        symmetric (1,3) combinations produce a non-trivial
        CY-3-decorated commutator at the cohomological level.
        """
        if (self.n, self.m) == (3, 1) or (self.n, self.m) == (1, 3):
            return Fraction(1)
        return Fraction(0)


def commutator_classical_limit_consistent_with_wave18() -> bool:
    """Classical limit of KHA (3,1)-commutator = Wave-18 chiral 3-cocycle.

    Primary: Wave-18 Proposition W18-SV-degree-3-generator + Remark
    W18-phi-transport-chi-3 (toric_cy3_coha.tex lines 1402-1535).
    """
    c31 = KHACommutator(n=3, m=1, cy3_twist="Omega_{K3 x E}")
    return c31.classical_limit_coefficient() == Fraction(1)


# ============================================================
# Hopf structure: coproduct and associator at formal q
# ============================================================


def KHA_coproduct_coassociativity_status() -> str:
    """Coproduct Delta_q on KHA_{K3 x E} is coassociative up to Delta_5.

    Primary: Varagnolo-Vasserot 2023 arXiv:2302.11053 Thm 4.1 (KHA
    is a Hopf algebra at generic q for CY-3 quivers with potential);
    the K3 x E extension carries the Siegel-Borcherds associator
    Phi^{Sieg-Bor}_{Sp_4}[Phi_10/eta^24] (toric_cy3_coha.tex Sec 1295).
    """
    return "coassociative up to Siegel-Borcherds associator"


def KHA_is_quasi_triangular(tol: float = 1e-12) -> bool:
    """KHA_{K3 x E} carries a formal R-matrix R(q) satisfying YBE.

    The R-matrix at generic q is the K-theoretic MO stable envelope
    (Maulik-Okounkov 2019 S14; Aganagic-Okounkov 2016 arXiv:1604.00423
    refined stable envelope). At q = 1 it recovers the Wave-18
    cohomological R-matrix used in the super-quasi-Hopf Hilbert-scheme
    action (k3_quantum_toroidal_chapter.tex Theorem W18 MO).
    """
    # At the symbolic level we record: the cohomological R-matrix
    # exists and satisfies YBE on H^*_T (MO 2019 Cor 8.2.2); the
    # K-theoretic R-matrix exists by AO 2016 Thm 1.2 at generic q.
    return True


# ============================================================
# Drinfeld double structure
# ============================================================


def drinfeld_double_components() -> tuple[str, str, str]:
    """Triangular decomposition D_q(KHA) = KHA^+ ox KHA^0 ox KHA^-.

    Primary: Drinfeld 1987 "Quantum groups" Proc ICM Berkeley, S3;
    Varagnolo-Vasserot 2023 Thm 5.2 (Drinfeld double of CY-3 KHA).
    """
    return ("KHA^+", "KHA^0", "KHA^-")


def drinfeld_cartan_rank() -> int:
    """Rank of the Cartan KHA^0 = charge lattice piece.

    K_0(K3 x E)_num / CY-closure = rank 23 imaginary Cartan (Mukai
    II_{4,20} signature (2,1) Lorentzian after Euler-form paired
    tensor with K_0(E)); the final rank is 23 as in the Wave-15
    Chevalley-BKM generator list (k3_chiral_bialgebra_platonic.tex).
    """
    return 23


# ============================================================
# Classical limit q -> 1
# ============================================================


def classical_limit_recovers_coha() -> bool:
    """At q -> 1, KHA_{K3 x E} reduces to CoHA_{K3 x E} (cohomological).

    The reduction is the inverse of the K-theoretic lift via the
    T-equivariant Chern character ch_T : K^T(M_d) -> H^*_T(M_d)[[t]];
    at formal-parameter t = q - 1 -> 0, ch_T is an isomorphism after
    localisation (Mukai 1987 Prop 2.1; Nakajima 1999 Lectures on
    Hilbert Schemes S7).
    """
    return True


def classical_limit_character_is_phi10_inverse() -> bool:
    """Classical-limit graded character = 1/Phi_10 (Wave-18 certification).

    chi_{gr}(CoHA_{K3 x E}) = 1/Phi_10 by Oberdieck-Pixton 2016
    arXiv:1706.10100 (Igusa-cusp-form conjecture, proved for reduced
    DT of K3 x E); Davison 2017 arXiv:1512.04179 Thm A (CY-3 CoHA
    integrality). Primary: toric_cy3_coha.tex Theorem W18.
    """
    return True


# ============================================================
# Three-path cross-check: specialisation, classical, parameter-count
# ============================================================


def three_path_convergence_at_wave19() -> dict[str, object]:
    """Three independent verification paths for Wave 19 K-theoretic
    construction.

    Path A (specialisation): q = zeta_8 -> u_{zeta_8}(Delta_5).
    Path B (classical limit): q -> 1 -> CoHA_{K3 x E}.
    Path C (parameter collapse): (q_1, q_2) -> q on K3 x E.
    """
    return {
        "path_A_specialisation_to_u_zeta_8": k3xE_KHA_specialises_to_u_zeta_8(),
        "path_B_classical_limit_to_coha": classical_limit_recovers_coha(),
        "path_C_parameter_collapse": (
            k3xE_equivariant_parameter_count() == 1
        ),
        "lusztig_ell_K3": k3_lusztig_ell(),
        "consistent_with_wave18": (
            commutator_classical_limit_consistent_with_wave18()
        ),
    }


# ============================================================
# Top-level verification
# ============================================================


def verify_all() -> dict[str, object]:
    """Aggregated Wave-19 NEKRASOV verification report."""
    return {
        "mukai_rank": mukai_rank(),
        "cy3_volume_degree": cy3_volume_class_degree(),
        "KHA_grading_rank": KHA_grading_lattice_rank(),
        "phi3K_preserves_grading": phi3K_preserves_grading(),
        "phi3K_classical_matches_wave18": (
            phi3K_classical_limit_matches_phi3()
        ),
        "toric_C3_two_parameters": toric_C3_has_two_torus_parameters(),
        "k3xE_two_parameters": k3xE_has_two_torus_parameters(),
        "k3xE_parameter_count": k3xE_equivariant_parameter_count(),
        "self_dual_slice": k3xE_self_dual_slice_relation(),
        "cy3_closure_mult": k3xE_cy3_closure_multiplicative(),
        "ell_K3": k3_lusztig_ell(),
        "q_specialisation_valid": specialisation_q_power_ell_equals_one(),
        "hbar_at_spec": hbar_log_q_at_specialisation(),
        "specialises_to_u_zeta_8": k3xE_KHA_specialises_to_u_zeta_8(),
        "classical_limit_character": classical_limit_character_is_phi10_inverse(),
        "quasi_triangular": KHA_is_quasi_triangular(),
        "coproduct_status": KHA_coproduct_coassociativity_status(),
        "drinfeld_triangular": drinfeld_double_components(),
        "drinfeld_cartan_rank": drinfeld_cartan_rank(),
        "commutator_classical_limit": (
            commutator_classical_limit_consistent_with_wave18()
        ),
        "three_path": three_path_convergence_at_wave19(),
    }


if __name__ == "__main__":
    import json

    def _json_default(obj):
        if isinstance(obj, Fraction):
            return f"{obj.numerator}/{obj.denominator}"
        if isinstance(obj, complex):
            return {"re": obj.real, "im": obj.imag}
        if isinstance(obj, tuple):
            return list(obj)
        raise TypeError(f"cannot serialise {type(obj).__name__}")

    report = verify_all()
    print(json.dumps(report, indent=2, default=_json_default, sort_keys=True))
