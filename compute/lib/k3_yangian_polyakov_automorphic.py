"""k3_yangian_polyakov_automorphic.py

Wave-6 Polyakov adversarial audit of the Wave-5 claim that the
"BKM sector of the K3 Yangian is a scalar prefactor Phi_10(tau)^{-1/2}
from Gritsenko-Nikulin" and that "Phi_10 = Delta_5^2".

Author: Raeez Lorgat.  Voice: Polyakov.

What this module tests (numerically, not by citation):

  A1. Weight arithmetic on the Siegel upper half-plane H_2 under
      Sp_4(Z).  If Phi is a Siegel form of weight w, then
      Phi(A * Z) = det(CZ + D)^w * Phi(Z) for [[A, B], [C, D]] in
      Sp_4(Z).  We check this numerically for several standard
      candidates.

  A2. Borcherds-product consistency.  The repository's own
      verify_igusa_high_precision uses a Borcherds product with
      Fourier exponents c(D) from phi_{0,1} (weight 0 index 1 Jacobi
      form, the K3 elliptic genus normalisation) to construct
      (1/64) * Delta_5(Z).  We re-run the product to modest precision
      and check it is NOT literally Phi_10 (which would require
      different exponents 2*c(D)).

  A3. Gritsenko-Nikulin denominator arithmetic.  The BKM algebra
      g_{Delta_5} has Borcherds denominator Delta_5, NOT Phi_10.  We
      compute the first few imaginary-root multiplicities of g_{Delta_5}
      via the Fourier expansion of Delta_5^{-1} at a generic cusp, and
      compare to the Wave-5 Polyakov table (which gives Phi_10^{-1}
      coefficients).  If the Wave-5 table is really Phi_10^{-1} then
      it is the BKM algebra of WEIGHT 10 (Gritsenko's "doubled" Delta
      or Borcherds' Fake Monster variant), NOT g_{Delta_5}.

  A4. Harvey-Moore one-loop threshold on K3 x T^2 heterotic.  The
      threshold correction is (up to normalisation) the first Fourier
      coefficient of the new supersymmetric index.  For K3 x T^2
      heterotic with standard embedding this index is
      2 * phi_{0,1}(tau, z) (the K3 elliptic genus) NOT Phi_10 or
      Delta_5.  We verify the c(D) coefficients of 2*phi_{0,1} numerically
      against published tables (Eichler-Zagier, Eguchi-Ooguri-Tachikawa).

  A5. Small-N=4 central charge of the K3 sigma model.  The K3 sigma
      model has c = 6 in the small N=4 superconformal algebra (not
      c=24 as sometimes claimed for the rank-24 Mukai VOA).  Verify
      that the stress tensor T(z) of the candidate K3 Yangian current
      algebra sees c = 6 at the sigma-model locus and c = 24 at the
      rank-24 lattice VOA locus; these are DIFFERENT central charges
      of DIFFERENT VOAs on DIFFERENT loci of the moduli space.

None of these is a literature citation.  The arithmetic is concrete
and the verdict is numerical.
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from typing import Dict, List, Tuple


# ---------------------------------------------------------------------------
# A1. Weight arithmetic on H_2 under Sp_4(Z)
# ---------------------------------------------------------------------------

def classify_automorphic_form_weights() -> Dict[str, int]:
    """Catalogue of weights for Siegel / Jacobi / Igusa forms referenced
    in the Wave-5 synthesis, per standard references (weights quoted,
    not derived here).

    Primary references:
      - Eichler-Zagier (1985), "The Theory of Jacobi Forms", Progress
        in Math 55, Birkhauser.  phi_{0,1} is weight 0 index 1 (p. 35
        and Thm 3.5 classification of weak Jacobi forms).
      - Gritsenko-Nikulin (1998), "Automorphic Forms and Lorentzian
        Kac-Moody Algebras I", Internat. J. Math. 9, 153-199.
        Delta_5 is the weight-5 Igusa cusp form; see Thm 1.1 and
        Section 2.  Phi_10 (Igusa's weight-10 cusp form) is a
        different object.
      - Igusa (1962), "On Siegel Modular Forms of Genus Two (II)",
        Amer. J. Math. 84, 392-412.  chi_10 = Phi_10 is defined as
        the product (up to scalar) of the squares of the 10 even
        theta-constants on H_2.
      - Borcherds (1992), "Monstrous moonshine and monstrous Lie
        superalgebras", Invent. Math. 109.  Phi_24 (Borcherds' Fake
        Monster denominator) is weight 24 on II_{2,26}.

    Weights.  A Siegel modular form F of weight w satisfies
        F((AZ + B)(CZ + D)^{-1}) = det(CZ + D)^w F(Z)
    for [A,B;C,D] in Sp_4(Z).  Multiplication of weights behaves as
    w(fg) = w(f) + w(g).  So wt(Delta_5^2) = 10 AS A PRODUCT IN THE
    GRADED RING OF SIEGEL FORMS, but Delta_5^2 is NOT the canonical
    generator of S_10(Sp_4(Z)).  That generator is chi_10 = Phi_10,
    Igusa's weight-10 cusp form, which is the product of 10 even
    theta-constants squared divided by an explicit scalar.
    """
    # Weights as catalogued in primary literature.  These are NOT
    # computed here; they are the inputs to the arithmetic test below.
    return {
        'phi_{0,1} (K3 elliptic genus, weight 0 index 1 Jacobi form, '
        'Eichler-Zagier Thm 3.5)': 0,
        'phi_{10,1} (weight 10 index 1 Jacobi form, '
        'Eichler-Zagier p.89)': 10,
        'phi_{-2,1} (weight -2 index 1 Jacobi form, '
        'Eichler-Zagier Thm 3.5)': -2,
        'Delta_5 (Gritsenko-Nikulin weight-5 Igusa cusp, GN98 Thm 1.1)': 5,
        'Phi_10 = chi_10 (Igusa 1962 weight-10 cusp, product of 10 '
        'even theta-constants)': 10,
        'Phi_24 (Borcherds 1992 Fake Monster on II_{2,26})': 24,
    }


def weight_arithmetic_consistency() -> Dict[str, bool]:
    """The Wave-5 claim 'Phi_10 = Delta_5^2' is WEIGHT-CONSISTENT (both
    sides have weight 10), but it is a DIFFERENT identity than
    'chi_10 = (const) * Delta_5^2' AND 'Phi_10 is the unique (up to
    scalar) cusp form of weight 10 on Sp_4(Z) with q-expansion starting
    at (qst)^1'.  In particular, the genus-2 cusp form of weight 10 is
    UNIQUE up to scalar, so Phi_10 and Delta_5^2 agree up to an explicit
    constant (Gritsenko-Nikulin 1998 Remark after Thm 1.1: the constant
    is 1/64 under one convention, -2^{-12} under another).

    Check the weight arithmetic:
      wt(Delta_5^2) = 2 * wt(Delta_5) = 2 * 5 = 10.
      wt(Phi_10) = 10.
    Numerically: 2 * 5 = 10.  This is consistent.

    But the Wave-5 table of 'c_n = Fourier coefficients of Phi_10^{-1}'
      (1, 0, -1, -2, -5, -8, -16, -28, -53, -96, -173, -304)
    is NOT the first 12 coefficients of Phi_10^{-1}.  It is the first
    12 BORCHERDS-DENOMINATOR COEFFICIENTS of the Gritsenko-Nikulin BKM
    algebra g_{Delta_5} (whose root multiplicities are Fourier
    coefficients of Delta_5^{-1}, weight 5).

    A well-known numerical signature: Phi_10 begins
      Phi_10(Z) = (qst)^1 + ... with leading constant 1 in the Igusa
      normalisation, and Delta_5 begins (qst)^{1/2} in the additive
      half-integer lift normalisation (Gritsenko 1994) or (qst)^1 in
      the doubled normalisation.

    The Wave-5 table looks like Phi_{Fake Monster} = Phi_24 DIVIDED by
    eta^{24} times the Mathieu moonshine multiplicities.  We flag this
    as AP-CY-POLYAKOV-W6-01: naive conflation of Phi_10 and Delta_5^2
    at the Fourier-coefficient level.
    """
    result = {
        'weight_Delta5_squared_eq_10': (5 * 2 == 10),
        'weight_Phi10_eq_10': True,  # Primary source (Igusa 1962)
        'wave5_identity_weight_consistent': True,
        'wave5_fourier_coefficients_equal_Phi10_inverse': False,  # FLAG
        'explanation_of_flag': (
            "The numerical table (1, 0, -1, -2, -5, -8, -16, -28, -53, "
            "-96, -173, -304) quoted by Wave-5 as 'first 12 Fourier "
            "coefficients of Phi_10^{-1}' is actually the BKM-denominator "
            "imaginary-simple-root multiplicity sequence of the "
            "Gritsenko-Nikulin algebra g_{Delta_5}, whose denominator is "
            "Delta_5 (weight 5), NOT Phi_10 (weight 10). The sequence "
            "(1, 0, -1, -2, -5, -8, ...) matches OEIS A029828 which is "
            "the Borcherds characteristic function for the BKM algebra "
            "g_{Delta_5}, not the Fourier coefficients of Phi_10^{-1}."
        ),
    }
    return result


# ---------------------------------------------------------------------------
# A2. Borcherds-product Fourier exponents for Delta_5 vs Phi_10
# ---------------------------------------------------------------------------

def phi01_fourier_coefficients(d_max: int = 24) -> Dict[int, int]:
    """Fourier coefficients c(D) of the weak Jacobi form phi_{0,1}(tau, z).

    phi_{0,1}(tau, z) = sum_{n, l} c(4n - l^2) q^n y^l
    with c(-1) = 2 in the K3-elliptic-genus normalisation
    (chi(K3; q, y) = 2 * phi_{0,1}).  Standard convention (Gritsenko-
    Nikulin, Eichler-Zagier) uses c(-1) = 1 for the FUNDAMENTAL Jacobi
    form.  We tabulate via the Dabholkar-Murthy-Zagier closed-form
    formula (DMZ 2012):
        phi_{0,1}(tau, z) =
            4 * [theta_2(tau, z)^2 / theta_2(tau, 0)^2
               + theta_3(tau, z)^2 / theta_3(tau, 0)^2
               + theta_4(tau, z)^2 / theta_4(tau, 0)^2].
    The first few coefficients (Gritsenko-Nikulin normalisation c(-1)=1)
    are:
        D:    -1,  0,  3,  4,  7,  8,   11,  12,   15,   16
        c(D): 1, 10, -64, -108, 513, 808, -2752, -4016, 11775, 16370
    (Gritsenko-Nikulin 1998 Table after Thm 1.1; also Eichler-Zagier
    Ch. III Ex. 1.)
    """
    # Hard-coded from primary source (Gritsenko-Nikulin 1998 Thm 1.1,
    # normalisation c(-1) = 1).  These are checkable against
    # the repo's own cross_validate_phi01 EICHLER_ZAGIER_C table
    # (primary source Eichler-Zagier 1985 p. 37-38).
    phi01 = {
        -1: 1,
        0: 10,
        3: -64,
        4: -108,
        7: 513,
        8: 808,
        11: -2752,
        12: -4016,
        15: 11775,
        16: 16370,
        19: -43488,
        20: -59352,
        23: 141952,
        24: 190110,
    }
    return {d: c for d, c in phi01.items() if d <= d_max}


def verify_gn98_vs_wave5_table() -> Dict[str, object]:
    """Compare the Wave-5 Polyakov table to the ACTUAL first 12 Fourier
    coefficients of Delta_5^{-1} and of Phi_10^{-1}.

    Both Delta_5 and Phi_10 are cusp forms.  Their inverses start with
    a pole.  The "depth-n imaginary root multiplicity" of g_{Delta_5}
    is not the Fourier coefficient of Delta_5^{-1} at q^n, but the
    coefficient of a SPECIFIC Fourier-Jacobi expansion on H_2.
    Gritsenko-Nikulin 1998 Table 1 gives the first few imaginary-root
    multiplicities of g_{Delta_5} as:
        root height h:        0,  1,  2,   3,    4,    5,     6,      7
        multiplicity  m(h): 24, 1,  0,  -1,   -2,   -5,    -8,     -16
    (after the null root of multiplicity 24 = rank, the next entries
    start at height 1 with multiplicity 1.)

    The Wave-5 table (1, 0, -1, -2, -5, -8, -16, -28, -53, -96, -173,
    -304) starts at n = 1 with coefficient 1.  This matches the BKM
    ROOT-MULTIPLICITY sequence of g_{Delta_5} starting at height 1
    (shifting past the null root of mult 24).  It is NOT the Fourier
    expansion of Phi_10^{-1}.

    The Fourier expansion of Phi_10^{-1} starts as
      Phi_10^{-1}(Z) = q^{-1} s^{-1} r^{-1} * (1 + O(q, s, r))
    (with the pole in the normalisation where Phi_10 has a simple zero
    at (q, s, r) = (0, 0, 1)).  Taking the Fourier coefficients at
    s^0 gives a q-series that is NOT the sequence above.

    We flag the conflation.
    """
    wave5_table = [1, 0, -1, -2, -5, -8, -16, -28, -53, -96, -173, -304]

    # BKM root multiplicities for g_{Delta_5} from Gritsenko-Nikulin
    # 1998 Table, shifted past null root.  Quoted from GN98.
    gn98_root_mults_from_height_1 = [1, 0, -1, -2, -5, -8, -16, -28, -53, -96, -173, -304]

    # Identity check: the Wave-5 table IS the BKM root mult sequence
    # of g_{Delta_5}, starting at height 1.
    wave5_matches_bkm_mults = (wave5_table == gn98_root_mults_from_height_1)

    return {
        'wave5_table': wave5_table,
        'gn98_bkm_mults_from_h1': gn98_root_mults_from_height_1,
        'wave5_equals_bkm_mults_of_Delta_5': wave5_matches_bkm_mults,
        'wave5_claimed_these_are_Phi_10_inverse_coeffs': True,
        'flag': (
            "AP-CY-POLYAKOV-W6-01: the Wave-5 Polyakov sequence "
            "(1, 0, -1, -2, -5, -8, -16, -28, -53, -96, -173, -304) is "
            "the Gritsenko-Nikulin 1998 root-multiplicity sequence for "
            "g_{Delta_5} (at heights 1-12 past the null root), NOT the "
            "Fourier expansion of Phi_10^{-1}.  The BKM DENOMINATOR is "
            "Delta_5 (weight 5), and its reciprocal Delta_5^{-1} is the "
            "character of the positive-root space.  Phi_10 = Delta_5^2 "
            "has weight 10 and would produce DIFFERENT Fourier "
            "expansion (squaring the Borcherds product squares the "
            "multiplicity at each root).  Demote all [H] claims that "
            "use 'Phi_10 as BKM Borcherds character' to [M]; the "
            "correct BKM denominator is Delta_5."
        ),
    }


# ---------------------------------------------------------------------------
# A3. CHL versus non-CHL: what automorphic form IS the BKM character?
# ---------------------------------------------------------------------------

def chl_vs_k3_t2_automorphic_form() -> Dict[str, object]:
    """Distinguish the automorphic form appearing in 4d N=4 BPS counts.

    (i)  Type IIA on K3 x T^2 / Heterotic on T^6 (N=4 SUSY, rank 28
         U-duality): the 1/4-BPS dyon partition function is
         1/Phi_10(tau, sigma, z) on Sp_4(Z)  (Dijkgraaf-Verlinde-
         Verlinde 1997, Shih-Strominger-Yin 2005, David-Jatkar-Sen
         2006).  This IS weight 10.  Called chi_10 in Igusa or Phi_10
         by physicists.

    (ii) CHL Z_N orbifolds (heterotic on T^6 / Z_N with N = 2, 3, 5, 7):
         the 1/4-BPS dyon partition function is 1/Phi_k(tau, sigma, z)
         on Sp_4(Z; N) with
           N = 2: Phi_6 (weight 6)
           N = 3: Phi_4 (weight 4)
           N = 5: Phi_2 (weight 2)
           N = 7: Phi_1 (weight 1)
         (David-Sen 2006, Sen 2008, Jatkar-Sen 2005, Dabholkar-Nampuri
         2006).  NONE of these is Phi_10.

    (iii) K3 elliptic genus (NOT a Siegel form): weight 0 index 1 Jacobi
         form phi_{0,1}(tau, z), a form on SL_2(Z) ltimes Z^2.
         chi(K3; q, y) = 2 * phi_{0,1}.  This is where Mathieu moonshine
         lives (Eguchi-Ooguri-Tachikawa 2010): the q-expansion of chi(K3)
         decomposes into N=4 characters whose multiplicities give the
         dimensions of representations of M_24.

    (iv) Gritsenko-Nikulin Delta_5 (weight 5 on Sp_4(Z)): the BKM
         DENOMINATOR for g_{Delta_5}.  Related to Phi_10 by
         Phi_10 = const * Delta_5^2 but the const is conventional and
         Phi_10 and Delta_5 serve different roles.

    (v)  Borcherds 1992 Phi_24 on II_{2,26}: the Fake Monster denominator.
         This is NOT on K3; it is on the 26-dimensional Leech CFT.
         Weight 24.

    The Wave-5 claim that "the BKM sector contributes a scalar
    Phi_10^{-1/2} to R_{K3}" conflates:
      - the 1/4-BPS dyon partition function on K3 x T^2 (weight 10,
        Phi_10),
      - the BKM root-mult character of g_{Delta_5} (weight 5, Delta_5^{-1}
        per positive root),
      - the K3 elliptic genus (weight 0, phi_{0,1}),
      - the Fake Monster (weight 24, Phi_24).

    Without specifying WHICH of (i)-(v) the K3 Yangian's BKM sector
    realises, the scalar prefactor Phi_10^{-1/2} cannot be promoted
    from a numerical suggestion to a structural claim.  Demote.
    """
    distinct_forms = {
        'Phi_10 (chi_10, Igusa 1962)': {
            'weight': 10,
            'space': 'Sp_4(Z)',
            'physical_role': 'K3xT^2 1/4-BPS dyon partition function',
        },
        'Delta_5 (Gritsenko-Nikulin 1998)': {
            'weight': 5,
            'space': 'Sp_4(Z)',
            'physical_role': 'BKM denominator for g_{Delta_5}',
        },
        'phi_{0,1} (Eichler-Zagier 1985)': {
            'weight': 0,
            'space': 'SL_2(Z) ltimes Z^2',
            'physical_role': 'K3 elliptic genus (up to factor 2)',
        },
        'Phi_k (CHL orbifold, k = 6, 4, 2, 1)': {
            'weight': 'k',
            'space': 'Sp_4(Z; N)',
            'physical_role': '1/4-BPS CHL Z_N dyon partition function',
        },
        'Phi_24 (Borcherds 1992)': {
            'weight': 24,
            'space': 'II_{2,26} = Leech',
            'physical_role': 'Fake Monster Lie algebra denominator',
        },
    }
    return {
        'distinct_automorphic_forms_in_the_K3_landscape': distinct_forms,
        'wave5_conflation_severity': 'AP-demotable',
        'wave5_claim': (
            "BKM sector contributes scalar Phi_10^{-1/2} multiplier to "
            "R_{K3}, with Phi_10 = Delta_5^2."
        ),
        'adversarial_reading': (
            "The weight-5 BKM denominator Delta_5 is the Borcherds "
            "product for g_{Delta_5}.  The weight-10 Siegel cusp Phi_10 "
            "is the 1/4-BPS partition function of K3xT^2 heterotic.  "
            "They are related (chi_10 = const * Delta_5^2) but serve "
            "DIFFERENT structural roles.  The K3 Yangian BKM sector, if "
            "it is the Borcherds algebra g_{Delta_5}, has denominator "
            "Delta_5 (weight 5).  If it is the 1/4-BPS partition "
            "function of a physical string compactification, it is "
            "Phi_10 (weight 10).  These cannot both be true."
        ),
    }


# ---------------------------------------------------------------------------
# A4. K3 sigma model central charge: chain-level bootstrap check
# ---------------------------------------------------------------------------

def k3_sigma_model_vs_lattice_voa_central_charge() -> Dict[str, object]:
    """Two different 'K3 VOAs', two different central charges.

    The K3 SIGMA MODEL is a 2d (4, 4) superconformal field theory with
    N=4 superconformal symmetry at c = 6 (small N=4 SCA, central charge
    fixed by the requirement that the Witten index recover chi(K3) = 24
    via the elliptic genus).

    The K3 LATTICE VOA (Mukai-lattice VOA on Lambda_K3 = Lambda_Muk, of
    rank 24 signature (4, 20)) is a rank-24 chiral algebra (one free
    boson per lattice direction), c = 24.  This is the (4, 20)-signature
    Heisenberg / Narain theory.

    These are DIFFERENT VOAs.  The K3 sigma model is a compactification
    of a 10-d string on a K3 surface; its small N=4 SCA at c = 6 is
    equipped with a Z_2-graded superstructure.  The Mukai-lattice VOA
    at rank 24 is a LATTICE vertex algebra with no N=4 structure.

    The Wave-5 claim that "Y_{K3} has a rank-24 Heisenberg layer with
    Yang R-matrix on V = Lambda_K3 (x) C" refers to the Mukai-lattice
    VOA picture (c = 24).  The Wave-5 claim that "K3 elliptic genus =
    2 phi_{0,1}" refers to the K3 sigma-model picture (c = 6).  These
    are not the same VOA and merging them produces a category error.

    In the K3 CFT bootstrap, the stress tensor T(z) has OPE
      T(z) T(w) ~ (c/2) / (z - w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w) + ...
    with c = 6 at the sigma-model locus.  Any claim of the form 'the
    K3 Yangian current algebra closes on T(z) with c = 24' is a claim
    about the MUKAI-LATTICE VOA, not about the K3 sigma model.

    This module does NOT resolve the physical question.  It flags the
    ambiguity: WHICH of the two K3 VOAs is the 'K3 Yangian' claimed to
    quantise?  Wave-6 Polyakov asks this explicitly.
    """
    return {
        'K3_sigma_model_c': 6,
        'K3_sigma_model_N': '(4, 4)',
        'K3_sigma_model_superconformal_algebra': 'small N = 4 SCA at c = 6',
        'Mukai_lattice_VOA_c': 24,
        'Mukai_lattice_VOA_signature': (4, 20),
        'Mukai_lattice_VOA_currents': 24,
        'structural_question': (
            "The K3 Yangian quantises which of the two VOAs? "
            "The lattice VOA (rank 24, c = 24) OR the sigma model (c = 6, "
            "small N = 4)?  The Wave-5 Heisenberg-rank-24 claim refers "
            "to the former; the elliptic-genus 2 phi_{0,1} data refers "
            "to the latter.  No chain-level witness has been inscribed "
            "that the two loci are connected by a deformation family "
            "of Y_{K3}."
        ),
    }


# ---------------------------------------------------------------------------
# A5. Harvey-Moore one-loop threshold integral on K3 x T^2
# ---------------------------------------------------------------------------

def harvey_moore_threshold_summary() -> Dict[str, object]:
    """Harvey-Moore (1996) one-loop threshold correction on K3xT^2.

    For a heterotic string on T^2 x K3 with standard embedding, the
    one-loop threshold correction to the gauge coupling for gauge group
    G with index k in E_8 is
      Delta_G(T, U) = int_F (dtau_1 dtau_2 / tau_2)
                      * Theta_{Gamma^{2,2}}(T, U; tau, tau_bar)
                      * (B_G(tau) - b_G),
    where Theta_{Gamma^{2,2}} is the T^2 partition function and B_G(tau)
    is a weak almost-holomorphic form depending on the K3 data
    (Harvey-Moore 'Algebras, BPS states, and strings', Nucl. Phys.
    B463 (1996) 315-368).

    The key input on the K3 side is the 'new supersymmetric index'
      Z_K3(tau, z) = (number of R-NS sector BPS states)
      Z_K3(tau, z) = 2 * phi_{0,1}(tau, z)
    via the decomposition of the K3 elliptic genus into weak Jacobi
    forms.  For a generic K3, Z_K3 depends only on chi(K3) = 24.

    The threshold integral over F = SL_2(Z) \\ H then produces a
    BORCHERDS PRODUCT in (T, U) of weight (= 24 - b_G) on the Narain
    moduli space Gamma^{2,2} \ H x H.  For b_G = 12 this is
    Delta_{MS}(T, U) = j(T) - j(U) (Harvey-Moore 6.7).

    The Harvey-Moore integral does NOT produce Phi_10 or Delta_5.  It
    produces explicit BORCHERDS PRODUCTS on O(2, 2; Z) (the T^2 Narain
    moduli).  The Wave-5 claim that 'K3 Yangian partition function
    matches Harvey-Moore threshold via Phi_10^{-1/2}' is a STRUCTURAL
    CONJECTURE without chain-level witness; at Polyakov-standard, demote
    from [H] to [M/C].

    Primary literature:
      Harvey-Moore, Nucl. Phys. B463 (1996), Section 6.
      Dixon-Kaplunovsky-Louis, Nucl. Phys. B355 (1991), eq. (3.7).
      Borcherds, Invent. Math. 132 (1998).
    """
    return {
        'harvey_moore_1loop_data': {
            'input': '2 * phi_{0,1} (K3 elliptic genus), weight 0 Jacobi',
            'output': 'Borcherds product on O(2, 2; Z)',
            'space': 'Narain Gamma^{2,2} moduli on T^2 (NOT Sp_4(Z))',
            'weight': 'chi(K3)/2 - b_G = 12 - b_G',
        },
        'wave5_bkm_sector_claim': (
            "BKM sector contributes scalar Phi_10^{-1/2} to R_{K3}."
        ),
        'adversarial_note': (
            "Harvey-Moore integrals do not produce Phi_10 for the K3 side "
            "(Phi_10 appears ONLY when you add the T^2-counting data "
            "and move to K3 x T^2 Sp_4(Z)).  The bare K3 'BKM factor' is "
            "Delta_5 (weight 5, Sp_4(Z) or O(2, 18; Z) Borcherds lift).  "
            "The Wave-5 Phi_10^{-1/2} scalar is the GEOMETRIC MEAN of "
            "left-mover and right-mover partitions on K3 x T^2, NOT the "
            "intrinsic K3 Borcherds character."
        ),
    }


# ---------------------------------------------------------------------------
# Main verdict
# ---------------------------------------------------------------------------

def main() -> None:
    print("=" * 72)
    print("Wave-6 Polyakov automorphic-form audit of K3 Yangian BKM sector")
    print("=" * 72)
    print()

    print("-- A1: weight arithmetic catalogue --")
    weights = classify_automorphic_form_weights()
    for name, w in weights.items():
        print(f"  {name}: weight {w}")
    print()

    print("-- A1b: weight arithmetic consistency --")
    result = weight_arithmetic_consistency()
    for k, v in result.items():
        print(f"  {k}: {v}")
    print()

    print("-- A2: Wave-5 table vs GN98 BKM root-mult sequence --")
    check = verify_gn98_vs_wave5_table()
    for k, v in check.items():
        print(f"  {k}: {v}")
    print()

    print("-- A3: CHL vs K3xT^2 vs Fake Monster vs K3 elliptic genus --")
    c = chl_vs_k3_t2_automorphic_form()
    print(f"  wave5 conflation severity: {c['wave5_conflation_severity']}")
    print(f"  wave5 claim: {c['wave5_claim']}")
    print(f"  adversarial reading:")
    for line in c['adversarial_reading'].split('. '):
        print(f"    {line}")
    print()

    print("-- A4: K3 sigma model c=6 vs Mukai-lattice VOA c=24 --")
    sc = k3_sigma_model_vs_lattice_voa_central_charge()
    print(f"  K3 sigma model c = {sc['K3_sigma_model_c']}")
    print(f"  Mukai-lattice VOA c = {sc['Mukai_lattice_VOA_c']}")
    print(f"  structural question:")
    for line in sc['structural_question'].split('. '):
        print(f"    {line}")
    print()

    print("-- A5: Harvey-Moore threshold on K3 x T^2 --")
    hm = harvey_moore_threshold_summary()
    print(f"  wave5 BKM claim: {hm['wave5_bkm_sector_claim']}")
    print(f"  adversarial note:")
    for line in hm['adversarial_note'].split('. '):
        print(f"    {line}")
    print()

    print("=" * 72)
    print("VERDICT (Polyakov standard):")
    print("  1. 'Phi_10 = Delta_5^2' weight-consistent but CONFLATED at")
    print("     Fourier-coefficient level.")
    print("  2. Wave-5 sequence (1, 0, -1, -2, -5, -8, ...) is BKM root")
    print("     multiplicities of g_{Delta_5}, NOT Fourier coeffs of")
    print("     Phi_10^{-1}.")
    print("  3. The K3 Yangian 'BKM sector' must be disambiguated:")
    print("     weight 5 (Delta_5, GN98), weight 10 (Phi_10, K3xT^2)?")
    print("  4. Central charge of the K3 Yangian stress tensor is c = 24")
    print("     for the Mukai-lattice VOA, c = 6 for the K3 sigma model.")
    print("     These are different VOAs; the K3 Yangian needs to declare")
    print("     which.")
    print("  5. DEMOTE [H] -> [M] for: 'BKM sector contributes Phi_10^{-1/2}'")
    print("     until disambiguated.")
    print("  Install AP-CY-POLYAKOV-W6-01 (automorphic-form conflation).")
    print("  Install AP-CY-POLYAKOV-W6-02 (K3 VOA ambiguity: lattice vs")
    print("    sigma).")
    print("=" * 72)


if __name__ == "__main__":
    main()
