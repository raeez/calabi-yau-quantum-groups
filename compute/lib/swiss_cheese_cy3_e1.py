r"""Swiss-cheese structure of CY3-derived E_1 chiral algebras.

Connects Vol II's SC^{ch,top} theory to the CY3-derived E_1 algebras
of Vol III. The E_1 bar complex has a Swiss-cheese algebra structure
where the E_1 (associative/ordered) direction is the R-direction
(boundary) and the chiral direction is the C-direction (bulk).

MATHEMATICAL BACKGROUND:
========================

1. SC^{E_1,ch} OPERAD FOR E_1-CHIRAL ALGEBRAS FROM CY3.
   Vol II proves (thm:homotopy-Koszul, def:SC-operations) that B(A) is
   an algebra over SC^{ch,top} = FM(C) x Conf(R). For CY3-derived E_1
   algebras, the E_1 direction is PRIMITIVE data: the factorization on
   ordered configurations comes from the CoHA multiplication (critical
   equivariant cohomology), NOT from a symmetric OPE.

   The SC^{E_1,ch} operad has operation spaces:
     SC^{E_1,ch}(n_c, n_o) = FM_{n_c}(C) x Conf^{ord}_{n_o}(R)
   where n_c = number of closed (bulk/chiral) inputs,
         n_o = number of open (boundary/E_1) inputs.

   KEY DISTINCTION from SC^{ch,top} for vertex algebras:
   For E_inf-chiral algebras (all vertex algebras), the R-direction
   factorization is DERIVED from the local OPE via monodromy
   (Vol II, AP36). For genuinely E_1-chiral algebras (CoHA, quantum
   vertex algebras), the R-direction factorization is INDEPENDENT
   INPUT -- part of the defining data.

   The CoHA product m: H_{d1} x H_{d2} -> H_{d1+d2} gives the E_1
   structure; the chiral bracket (if present) gives the C-direction.

2. E_1 BAR COMPLEX B^{E_1}(A).
   The E_1 bar complex uses only the ORDERED bar construction:
     B^{E_1}_k(A) = (s^{-1}A)^{tensor k}  (NO S_k coinvariants)
   with bar differential from the associative product.

   For the full bar complex (E_inf): B^{Sigma}_k(A) = (s^{-1}A)^{tensor k} / S_k.
   The E_1 bar complex has STRICTLY MORE generators than the E_inf bar complex
   at each bar degree k >= 2 (Vol II, AP37, AP38).

   Consequence: the E_1 shadow obstruction tower has MORE terms at
   each arity, but the R-matrix descent B^{ord} -> B^{Sigma} (twisted
   by R) produces the same scalar shadow on the symmetric quotient.

3. SHADOW DEPTH FOR CY3 ALGEBRAS.
   The shadow depth classification (G/L/C/M) depends on the OPE
   structure of the chiral algebra, not on the E_1/E_inf distinction.

   For CY3-derived algebras:
     C^3 -> W_{1+inf}: class M (infinite tower). Each spin-s
       channel contributes independently. Spin 1 (Heisenberg) = G.
       Spin 2 (Virasoro at c=1) = M. Total: M.
     Resolved conifold -> H_1 (Heisenberg from compact cycle): class G.
     Local P^2 -> McKay quiver CoHA: class M (AP-CY12: infinite depth;
       leading-order OPE is Lie-type from shuffle product, but
       higher-degree BPS states generate an infinite tower).
     Quintic -> class M (infinite GW invariants drive infinite tower).
     K3 x E -> class M (BKM superalgebra, infinite Borcherds product).

4. E_1-SWISS-CHEESE FORMALITY OBSTRUCTION.
   Vol I proves: only class G is SC-formal (m_k^{SC} = 0 for k >= 3).
   Class L already has m_3^{SC} != 0. Class C has shadow depth 4.
   Class M has infinite depth.

   For CY3 algebras:
     C^3 (W_{1+inf}): class M => SC NON-FORMAL. Infinite tower of
       higher A_inf operations from the MacMahon function.
     Conifold: class G => SC FORMAL. The Heisenberg structure from
       a single compact cycle gives a formal SC algebra.
     Local P^2: class M => SC NON-FORMAL (AP-CY12: infinite tower).
     Quintic: class M => SC NON-FORMAL.
     K3 x E: class M => SC NON-FORMAL.

5. QUARTIC SHADOW Q^{E_1} FOR CY3 ALGEBRAS.
   The E_1 bar complex has FEWER symmetrization terms than E_inf.
   At arity 4, the E_inf quartic contact invariant Q^contact involves
   S_4-coinvariants (24 terms reduced by symmetry); the E_1 quartic
   contact Q^{E_1,contact} involves all 24 ordered terms.

   For W_{1+inf} at c=1:
     The spin-2 (Virasoro) channel has Q^contact_Vir = 10/[c(5c+22)].
     At c=1: Q^contact_Vir(c=1) = 10/27.
     The E_1 quartic is Q^{E_1} = sum over ordered 4-tuples, NOT
     over S_4-orbits. But the quartic CONTACT invariant (the piece
     that enters the shadow obstruction tower) is the same after
     cyclization: Q^{E_1,contact} = Q^contact (cyclic invariance
     of the contact term).

   The key computation: Q^{E_1,contact}(W_{1+inf}) is determined
   channel-by-channel. Each spin-s channel contributes Q^contact_s.
   The total is a sum over channels (by independent-sum factorization).

6. E_1-KOSZUL DUAL OF W_{1+inf}.
   In the E_inf setting: Koszul duality uses the full chiral structure.
   In E_1: only the associative (ordered) part.

   The E_1-Koszul dual (W_{1+inf})^{!,E_1} is the linear dual of the
   ORDERED bar cohomology H*(B^{ord}(W_{1+inf})).

   For an E_inf algebra A, the E_1-Koszul dual carries MORE data than
   the E_inf Koszul dual (because B^{ord} has more generators). But
   for a genuinely E_1 algebra, B^{ord} IS the canonical bar complex.

   For W_{1+inf} at c=1 (which IS E_inf, being a vertex algebra):
     (W_{1+inf})^{!,E_inf} uses the symmetric bar -> produces the
     W-algebra at dual level.
     (W_{1+inf})^{!,E_1} uses the ordered bar -> produces a LARGER
     algebra (the ordered Koszul dual) that surjects onto (W_{1+inf})^{!,E_inf}.

   The E_1-Koszul dual of the Heisenberg H_k:
     B^{ord}_1(H_k) = s^{-1}H_k (generators)
     B^{ord}_2(H_k) = (s^{-1}H_k)^{tensor 2} (2 ordered generators)
     d_bar[a|b] = a*b (the OPE product)
     H*(B^{ord}) = Ext^*_{H_k-mod}(k, k) in the ORDERED sense.

   For H_k: the ordered bar and symmetric bar give the SAME cohomology
   because the OPE is symmetric (AP41: R(z) = exp(k*hbar/z) is scalar
   on the 1-generator space). The E_1 and E_inf Koszul duals coincide.

   For W_{1+inf}: the multi-generator OPE is NOT symmetric between
   different spins (W_s * W_t != +/- W_t * W_s in general). The
   ordered bar has genuinely more cohomology classes.

7. SHADOW DEPTH AND CY3 GEOMETRY.
   The shadow depth of a CY3 chiral algebra encodes:
     - Euler characteristic: kappa = chi^CY(X), the leading coefficient.
     - Hodge numbers: affect the number of independent channels.
     - DT invariants: the GV invariants n^g_d drive the infinite tower
       for class-M algebras. The shadow tower IS the topological string
       partition function reorganized as an MC element.

   The deep structural question: shadow depth = complexity of DT
   theory. Finite shadow depth (G/L) means finitely generated BPS
   spectrum. Infinite depth (M) means infinitely generated BPS
   spectrum with nontrivial bound-state dynamics.

CONVENTIONS:
  - Cohomological grading (|d| = +1).
  - Bar uses DESUSPENSION: |s^{-1}v| = |v| - 1 (AP45).
  - E_1 bar = ordered bar (no S_n coinvariants).
  - E_inf bar = symmetric bar (S_n coinvariants).
  - kappa(A) = modular characteristic from Vol I.
  - For CY3 algebras: kappa = chi^CY(X) (Theorem CY-D).
  - Q^contact = quartic contact invariant (arity-4 shadow).
  - All Fraction arithmetic for exact computations.

REFERENCES:
  Vol II: factorization_swiss_cheese.tex (SC^{ch,top})
  Vol II: ordered_associative_chiral_kd_core.tex (E_1 vs E_inf bars)
  Vol I:  higher_genus_modular_koszul.tex (shadow obstruction tower)
  Vol I:  bar_cobar_adjunction_curved.tex (bar complex)
  Schiffmann-Vasserot, arXiv:1211.1287 (CoHA = Y^+(gl_hat_1))
  Etingof-Kazhdan, arXiv:q-alg/9709040 (quantum vertex algebras)
  Kontsevich, ICM 1994 (HMS)
  Costello, arXiv:math/0412149 (TCFT and CY categories)
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, NamedTuple, Optional, Tuple


# =========================================================================
# 1. SC^{E_1,ch} OPERAD STRUCTURE
# =========================================================================

class SCE1ChOperadData(NamedTuple):
    """Data of the SC^{E_1,ch} operad at arity (n_c, n_o).

    n_c = number of closed (chiral/bulk) inputs
    n_o = number of open (E_1/boundary) inputs

    The operation space is FM_{n_c}(C) x Conf^{ord}_{n_o}(R).

    dim_closed: real dimension of FM_{n_c}(C) = 2*n_c (for n_c >= 2)
    dim_open: real dimension of Conf^{ord}_{n_o}(R) = n_o (for n_o >= 1)
    total_dim: dim_closed + dim_open
    """
    n_closed: int
    n_open: int
    dim_closed: int
    dim_open: int
    total_dim: int


def sc_e1_ch_operad_data(n_c: int, n_o: int) -> SCE1ChOperadData:
    """Compute dimension data of the SC^{E_1,ch} operation space.

    FM_{n_c}(C) has real dimension 2*n_c - 3 for n_c >= 2 (remove
    translations and dilations from C^{n_c}).
    Actually: FM_k(C) is a real manifold with corners of dimension 2k.
    After removing overall translation (2 dims) and dilation (1 dim):
    dim = 2k - 3 for k >= 2, dim = 0 for k = 0, 1.

    Conf^{ord}_{n_o}(R) = {t_1 < t_2 < ... < t_{n_o}} modulo translation.
    dim = n_o - 1 for n_o >= 1.
    """
    if n_c <= 1:
        dim_c = 0
    else:
        dim_c = 2 * n_c - 3

    if n_o <= 0:
        dim_o = 0
    else:
        dim_o = max(0, n_o - 1)

    return SCE1ChOperadData(
        n_closed=n_c,
        n_open=n_o,
        dim_closed=dim_c,
        dim_open=dim_o,
        total_dim=dim_c + dim_o,
    )


def sc_e1_operation_count(n_c: int, n_o: int) -> int:
    """Number of generators of the SC^{E_1,ch} operad at arity (n_c, n_o).

    For the E_1 direction: n_o! orderings (since ordered configurations
    have n_o! connected components when discretized to a lattice).
    For the closed direction: 1 (the FM compactification is connected).

    Total: n_o! for n_o >= 1, 1 for n_o = 0.

    But actually, for the operad, the generators are the top cells:
    for the Stasheff associahedron, there is 1 top cell in each dimension.
    The correct count is the Euler characteristic of the operation space.

    For Swiss-cheese: the number of TREES (generators) at arity (n_c, n_o)
    is the number of planar trees with n_c + n_o leaves, n_c of which
    are marked "closed" (unordered among themselves) and n_o are "open"
    (ordered).

    For small arities we just enumerate.
    """
    if n_c == 0 and n_o == 0:
        return 0
    if n_c + n_o == 1:
        return 1  # identity operation
    if n_c + n_o == 2:
        return 1  # binary product (closed-closed, closed-open, or open-open)

    # For general arities: the number of planar rooted trees with
    # k = n_c + n_o leaves where n_o leaves are ordered.
    # This is the (n_c + n_o - 1)-th Catalan number times a binomial.
    # Catalan(n) = (2n)! / ((n+1)! * n!)
    k = n_c + n_o
    # Number of binary planar trees with k leaves: Catalan(k-1)
    catalan = math.comb(2 * (k - 1), k - 1) // k
    # The closed inputs can be assigned to any n_c of the k positions
    # (but the open inputs preserve their order).
    return catalan * math.comb(k, n_c)


# =========================================================================
# 2. E_1 BAR COMPLEX DIMENSIONS
# =========================================================================

class E1BarDimensions(NamedTuple):
    """Dimensions of the E_1 bar complex at each bar degree.

    For a graded vector space V with dim_graded = {degree: dim}:
    B^{E_1}_k(V) = V^{tensor k} (ordered, no coinvariants)
    dim B^{E_1}_k = (dim V)^k

    B^{Sigma}_k(V) = Sym^k(V) (graded symmetric)
    dim B^{Sigma}_k = C(dim V + k - 1, k) for all-even generators
                     or the graded symmetric power.

    The ratio dim(B^{E_1}_k) / dim(B^{Sigma}_k) = k! for uniform-degree V.
    """
    name: str
    generators_dim: int      # dim(V) = number of generators
    bar_e1: Dict[int, int]   # k -> dim B^{E_1}_k
    bar_sigma: Dict[int, int]  # k -> dim B^{Sigma}_k
    ratio: Dict[int, int]    # k -> dim(E_1) / dim(Sigma) = k! for uniform


def e1_bar_dimensions(name: str, dim_v: int,
                      max_bar: int = 6) -> E1BarDimensions:
    """Compute E_1 and E_inf bar complex dimensions.

    Assumes all generators in the same degree (uniform-weight).
    For multi-graded generators, the symmetric power computation
    is more complex (use graded_symmetric_power).
    """
    bar_e1: Dict[int, int] = {}
    bar_sigma: Dict[int, int] = {}
    ratio: Dict[int, int] = {}

    for k in range(1, max_bar + 1):
        # E_1 bar: ordered tensor product
        bar_e1[k] = dim_v ** k
        # E_inf bar: symmetric power (for uniform-even generators)
        bar_sigma[k] = math.comb(dim_v + k - 1, k)
        if bar_sigma[k] > 0:
            ratio[k] = bar_e1[k] // bar_sigma[k]
        else:
            ratio[k] = 0

    return E1BarDimensions(
        name=name,
        generators_dim=dim_v,
        bar_e1=bar_e1,
        bar_sigma=bar_sigma,
        ratio=ratio,
    )


def e1_bar_excess(dim_v: int, k: int) -> int:
    """Excess generators in E_1 bar vs E_inf bar at bar degree k.

    excess = dim(B^{E_1}_k) - dim(B^{Sigma}_k)

    For uniform-degree generators:
      B^{E_1}_k = V^{tensor k}, dim = n^k
      B^{Sigma}_k = Sym^k(V), dim = C(n+k-1, k)
      excess = n^k - C(n+k-1, k)

    At k=1: excess = 0 (both have dim = n).
    At k=2: excess = n^2 - n(n+1)/2 = n(n-1)/2.
    """
    e1 = dim_v ** k
    sigma = math.comb(dim_v + k - 1, k)
    return e1 - sigma


# =========================================================================
# 3. SHADOW DEPTH CLASSIFICATION FOR CY3 ALGEBRAS
# =========================================================================

class CY3ShadowData(NamedTuple):
    """Shadow data for a CY3-derived E_1 chiral algebra.

    Fields:
      name: geometry name
      kappa: modular characteristic chi^CY(X)
      shadow_class: G/L/C/M
      r_max: maximum arity with nonzero shadow (-1 = infinity)
      sc_formal: whether the SC structure is formal
      euler_chi: topological Euler characteristic chi_top(X)
      h11: Hodge number h^{1,1}
      h21: Hodge number h^{2,1}
      bps_finite: whether the BPS spectrum is finitely generated
      e1_koszul_dual: description of E_1-Koszul dual
      reasoning: explanation
    """
    name: str
    kappa: Fraction
    shadow_class: str
    r_max: int
    sc_formal: bool
    euler_chi: int
    h11: int
    h21: int
    bps_finite: bool
    e1_koszul_dual: str
    reasoning: str


def cy3_shadow_data_c3() -> CY3ShadowData:
    r"""Shadow data for C^3 -> W_{1+inf} at c=1.

    W_{1+inf} has generators at all spins s >= 1.
    - Spin 1: Heisenberg, class G, r_max=2
    - Spin 2: Virasoro at c=1, class M, r_max=inf
    - Spin s >= 3: generically class M

    Total: class M (the Virasoro channel drives infinite depth).

    kappa = divergent (harmonic series). Regulated: kappa(W_N) = c*H_N.
    For the computation we use kappa = kappa_2 = c/2 = 1/2 (the
    leading finite channel, the Virasoro contribution).

    SC formality: class M => NON-FORMAL.
    BPS spectrum: infinite (MacMahon function, plane partitions).
    E_1-Koszul dual: the dual CoHA / dual affine Yangian Y^-(gl_hat_1).
    """
    return CY3ShadowData(
        name="C^3",
        kappa=Fraction(1, 2),  # Virasoro channel at c=1
        shadow_class="M",
        r_max=-1,
        sc_formal=False,
        euler_chi=1,  # non-compact
        h11=0,
        h21=0,
        bps_finite=False,
        e1_koszul_dual="Y^-(gl_hat_1) (dual affine Yangian)",
        reasoning=(
            "W_{1+inf} at c=1: spin-2 channel (Virasoro at c=1) is class M "
            "(Q^contact = 10/27 != 0, Delta = 40/27). Total kappa diverges "
            "(harmonic series). BPS spectrum = plane partitions (MacMahon). "
            "SC non-formal due to infinite shadow depth."
        ),
    )


def cy3_shadow_data_conifold() -> CY3ShadowData:
    r"""Shadow data for resolved conifold O(-1)+O(-1) -> P^1.

    Chiral algebra: Heisenberg H_1 from single compact P^1 cycle.
    kappa = 1, shadow class G, SC formal.

    BPS spectrum: Omega(n*beta) = 1 for all n >= 1 (class 0 states).
    But these are all Heisenberg excitations of a SINGLE field.
    The chiral algebra is class G because the OPE is purely quadratic
    (double pole, no first-order pole for a single free field).
    """
    return CY3ShadowData(
        name="resolved conifold",
        kappa=Fraction(1),
        shadow_class="G",
        r_max=2,
        sc_formal=True,
        euler_chi=2,
        h11=1,
        h21=0,
        bps_finite=True,
        e1_koszul_dual="H_{-1} (Heisenberg at level -1, same class as H_1^!)",
        reasoning=(
            "Single compact cycle: Heisenberg H_1. Alpha=0, S_4=0. "
            "Gaussian shadow terminates at arity 2. SC formal. "
            "BPS: Omega(n*beta) = 1 all n, but all from single generator."
        ),
    )


def cy3_shadow_data_local_p2() -> CY3ShadowData:
    r"""Shadow data for local P^2 = O(-3) -> P^2.

    McKay quiver CoHA from Z_3 action on C^3.
    3 BPS states at degree 1 (chi(P^2) = 3).
    The quiver has 3 vertices, 9 arrows, potential from CY condition.

    The OPE structure: the CoHA shuffle product has a first-order pole
    from the quiver intersection pairing. At leading order this looks
    Lie-type, but the full BPS spectrum is infinite (higher-degree
    curve classes contribute infinitely many BPS states), forcing
    class M (infinite shadow depth).  AP-CY12: leading approximation
    misses the infinite tower.

    kappa(LP^2) = chi(P^2)/2 = 3/2 (from genus-1 GV).
    """
    # AP-CY12: local P^2 is class M (infinite depth), not G/L/C.
    # Leading approximation (quiver with cubic potential) misses the infinite
    # tower from higher-degree BPS states.  The full BPS spectrum is infinite
    # (bps_finite=False), which forces class M.
    return CY3ShadowData(
        name="local P^2",
        kappa=Fraction(3, 2),  # 3 generators, each kappa = 1/2
        shadow_class="M",
        r_max=-1,  # infinite: class M
        sc_formal=False,  # class M is NOT SC-formal
        euler_chi=3,  # chi(P^2) = 3, non-compact total space
        h11=1,
        h21=0,
        bps_finite=False,  # infinitely many BPS states at higher degree
        e1_koszul_dual="Ext algebra of McKay quiver (Q_{Z_3}, W)",
        reasoning=(
            "McKay quiver of Z_3: 3 nodes, 9 arrows, cubic potential. "
            "Leading-order OPE has first-order poles (Lie type), but "
            "higher-degree BPS states generate an infinite shadow tower. "
            "Class M (infinite depth), r_max=infinity. NOT SC-formal. "
            "AP-CY12: leading approximation misses the infinite tower."
        ),
    )


def cy3_shadow_data_quintic() -> CY3ShadowData:
    r"""Shadow data for quintic CY3.

    Rigid CY3, h^{1,1}=1, h^{2,1}=101.
    kappa = chi_top/24 = -200/24 = -25/3 (CONJECTURAL, from BCOV).
    Shadow class M: infinite tower from GW invariants n^g_d.
    SC non-formal: the topological string partition function
    encodes infinitely many higher A_inf operations.
    """
    return CY3ShadowData(
        name="quintic",
        kappa=Fraction(-200, 24),
        shadow_class="M",
        r_max=-1,
        sc_formal=False,
        euler_chi=-200,
        h11=1,
        h21=101,
        bps_finite=False,
        e1_koszul_dual="dual B-model chiral algebra at Omega_Q",
        reasoning=(
            "Rigid CY3: h^{2,1}=101 complex structure deformations. "
            "GW invariants are nonzero at all genera and arbitrarily "
            "high degree. kappa = chi_top/24 = -25/3 (CONJECTURAL). "
            "Class M, infinite shadow tower = topological string PF."
        ),
    )


def cy3_shadow_data_k3xe() -> CY3ShadowData:
    r"""Shadow data for K3 x E (CY3, non-rigid).

    kappa = 5 (Theorem CY-D, from weight of Delta_5).
    Shadow class M: BKM superalgebra gives infinite Borcherds product.
    SC non-formal.
    """
    return CY3ShadowData(
        name="K3 x E",
        kappa=Fraction(5),
        shadow_class="M",
        r_max=-1,
        sc_formal=False,
        euler_chi=0,
        h11=21,
        h21=21,
        bps_finite=False,
        e1_koszul_dual="BKM dual algebra (Borcherds product involution)",
        reasoning=(
            "K3 x E: kappa=5 from Borcherds/Theta lift. "
            "BKM superalgebra encodes infinite product structure. "
            "Class M, SC non-formal."
        ),
    )


def all_cy3_shadow_data() -> Dict[str, CY3ShadowData]:
    """All CY3 shadow data as a dictionary."""
    data = [
        cy3_shadow_data_c3(),
        cy3_shadow_data_conifold(),
        cy3_shadow_data_local_p2(),
        cy3_shadow_data_quintic(),
        cy3_shadow_data_k3xe(),
    ]
    return {d.name: d for d in data}


# =========================================================================
# 4. QUARTIC SHADOW Q^{E_1} FOR CY3 ALGEBRAS
# =========================================================================

def quartic_contact_virasoro(c: Fraction) -> Fraction:
    r"""Quartic contact invariant Q^contact_Vir(c).

    From Vol I: Q^contact_Vir = 10 / [c * (5c + 22)].

    At c=1: Q^contact = 10/27.
    At c=1/2 (Ising): Q^contact = 10/(1/2 * 24.5) = 10/12.25 = 40/49.
    """
    if c == 0:
        raise ValueError("Q^contact undefined at c=0 (uncurved)")
    return Fraction(10) / (c * (5 * c + 22))


def quartic_contact_heisenberg() -> Fraction:
    """Quartic contact invariant for Heisenberg: Q^contact = 0.

    Heisenberg is class G: alpha=0, S_4=0, so Q^contact=0.
    """
    return Fraction(0)


def quartic_contact_e1_single_channel(
    kappa: Fraction,
    alpha: Fraction,
    S4: Fraction,
) -> Fraction:
    r"""Quartic contact invariant on a single primary line.

    Q^contact = S_4 (the arity-4 coefficient of the shadow tower).

    For the E_1 bar complex: the quartic contact invariant is the SAME
    as for the E_inf bar complex, because the contact term is CYCLIC
    invariant (it comes from a trace over the 4-point function on the
    moduli space M_{0,4}). The cyclic quotient Z/4Z of S_4 is the
    same whether we start from ordered or unordered tensors.

    Formally: Q^{E_1,contact} = Q^{E_inf,contact} = S_4.
    The E_1 bar has ADDITIONAL terms at arity 4 (the non-cyclic
    ordered 4-tuples), but these terms lie outside the contact
    subspace and do not contribute to the shadow tower.
    """
    return S4


def quartic_contact_w1inf_channel(s: int, c: Fraction = Fraction(1)) -> Fraction:
    r"""Quartic contact invariant for spin-s channel of W_{1+inf}.

    Spin 1 (Heisenberg): S_4 = 0 (class G).
    Spin 2 (Virasoro at c): S_4 = Q^contact_Vir = 10/[c(5c+22)].
    Spin s >= 3: the quartic contact depends on the W_s self-OPE
    structure. For c=1, the spin-s channel has kappa_s = 1/s,
    and the quartic contact is determined by the Virasoro-type
    formula scaled by the conformal weight.

    For spin s at c=1:
      kappa_s = 1/s
      The self-OPE of W_s has maximum pole order 2s.
      The quartic contact is Q^contact_s = s^2 * 10 / [c(5c+22)] / s^2
      = 10 / [c(5c+22)] (independent of s for the universal W-algebra).

    CAUTION: This is the UNIVERSAL W-algebra formula. The simple
    quotient may differ at special values of c.
    """
    if s == 1:
        return Fraction(0)
    if c == 0:
        raise ValueError("Q^contact undefined at c=0")
    return Fraction(10) / (c * (5 * c + 22))


def quartic_e1_w1inf_total(N: int, c: Fraction = Fraction(1)) -> Fraction:
    r"""Total E_1 quartic contact for W_{1+inf} regulated at spin N.

    Q^{E_1,contact}(W_{1+inf}, N) = sum_{s=1}^{N} Q^contact_s.

    Since Q^contact_s = 10/[c(5c+22)] for all s >= 2, and Q^contact_1 = 0:
      Total = (N-1) * 10/[c(5c+22)].

    At c=1, N=infinity: Q^{E_1,contact} = sum_{s>=2} 10/27 = divergent.
    At c=1, N=10: Q^{E_1,contact} = 9 * 10/27 = 10/3.
    """
    if N < 1:
        return Fraction(0)
    q_per_channel = quartic_contact_virasoro(c)
    return (N - 1) * q_per_channel


# =========================================================================
# 5. E_1-KOSZUL DUALITY FOR CY3 ALGEBRAS
# =========================================================================

class E1KoszulDualData(NamedTuple):
    """Data of the E_1-Koszul dual of a CY3-derived algebra.

    The E_1-Koszul dual uses the ORDERED bar cohomology.
    For an E_inf algebra A:
      (A)^{!,E_1} = (H*(B^{ord}(A)))^v
    which SURJECTS onto the E_inf Koszul dual:
      (A)^{!,E_1} -> (A)^{!,E_inf} -> 0.

    The kernel measures the R-matrix twist:
      0 -> ker -> (A)^{!,E_1} -> (A)^{!,E_inf} -> 0.
    """
    name: str
    e1_dual_name: str
    einf_dual_name: str
    bar_dim_e1: Dict[int, int]     # bar degree -> dim of E_1 bar
    bar_dim_einf: Dict[int, int]   # bar degree -> dim of E_inf bar
    excess_dim: Dict[int, int]     # bar degree -> dim(E_1) - dim(E_inf)
    kappa_dual: Fraction           # kappa of the dual algebra


def e1_koszul_dual_heisenberg(k: Fraction) -> E1KoszulDualData:
    """E_1-Koszul dual of Heisenberg H_k.

    H_k has 1 generator of weight 1. The ordered and symmetric bars
    are identical at all bar degrees (since there is only 1 generator,
    all orderings are the same).

    Bar dims: B_k = 1 for all k (one k-fold tensor of the single generator).
    Actually: B^{ord}_n has dim = 1 for each n (one element [a|a|...|a]).
    B^{Sigma}_n has dim = 1 (same, since S_n acts trivially on identical elements).

    kappa_dual = -k (from Koszul duality, AP33: H_k^! = Sym^ch(V*)).
    """
    bar_e1: Dict[int, int] = {}
    bar_einf: Dict[int, int] = {}
    for n in range(1, 7):
        bar_e1[n] = 1
        bar_einf[n] = 1

    return E1KoszulDualData(
        name=f"H_{k}",
        e1_dual_name=f"H_{k}^{{!,E_1}} = Sym^ch(V*)",
        einf_dual_name=f"H_{k}^{{!,E_inf}} = Sym^ch(V*)",
        bar_dim_e1=bar_e1,
        bar_dim_einf=bar_einf,
        excess_dim={n: 0 for n in range(1, 7)},
        kappa_dual=-k,
    )


def e1_koszul_dual_sl2(k: Fraction) -> E1KoszulDualData:
    """E_1-Koszul dual of V_k(sl_2).

    V_k(sl_2) has 3 generators {e, f, h} of weight 1.
    Bar dims:
      B^{ord}_n: 3^n (all ordered n-tuples of {e,f,h})
      B^{Sigma}_n: C(3+n-1, n) = C(n+2, n) (symmetric, all even degree)

    The excess measures the R-matrix twist content.
    kappa_dual = -3*(k+2)/(2*2) = -3(k+2)/4  (from kappa = dim(g)(k+h^v)/(2h^v))

    Actually for sl_2: kappa(V_k(sl_2)) = 3*(k+2)/(2*2) = 3(k+2)/4.
    And kappa_dual = -kappa by Feigin-Frenkel (KM family: kappa + kappa' = 0).
    """
    bar_e1: Dict[int, int] = {}
    bar_einf: Dict[int, int] = {}
    excess: Dict[int, int] = {}
    for n in range(1, 7):
        bar_e1[n] = 3 ** n
        bar_einf[n] = math.comb(n + 2, n)
        excess[n] = bar_e1[n] - bar_einf[n]

    kappa_v = Fraction(3) * (k + 2) / 4
    return E1KoszulDualData(
        name=f"V_{k}(sl_2)",
        e1_dual_name=f"V_{k}(sl_2)^{{!,E_1}} (ordered Koszul dual)",
        einf_dual_name=f"V_{{-k-4}}(sl_2) (Feigin-Frenkel dual)",
        bar_dim_e1=bar_e1,
        bar_dim_einf=bar_einf,
        excess_dim=excess,
        kappa_dual=-kappa_v,
    )


def e1_koszul_dual_w1inf_regulated(
    N: int, c: Fraction = Fraction(1)
) -> E1KoszulDualData:
    """E_1-Koszul dual of W_{1+inf} regulated at spin cutoff N.

    W_{1+inf} at spin cutoff N has N generators (spins 1, 2, ..., N).
    Bar dims at bar degree k:
      B^{ord}_k: N^k (ordered k-tuples)
      B^{Sigma}_k: C(N+k-1, k) (symmetric k-tuples)

    E_1-Koszul dual: the dual affine Yangian Y^-(gl_hat_1), regulated.
    E_inf-Koszul dual: W_{1+inf} at dual level (c -> alpha_inf - c).
    """
    bar_e1: Dict[int, int] = {}
    bar_einf: Dict[int, int] = {}
    excess: Dict[int, int] = {}
    for k in range(1, 7):
        bar_e1[k] = N ** k
        bar_einf[k] = math.comb(N + k - 1, k)
        excess[k] = bar_e1[k] - bar_einf[k]

    # Regulated kappa: kappa(W_{1+inf}, N) = c * H_N
    from fractions import Fraction as F
    kappa_reg = c * sum(F(1, s) for s in range(1, N + 1))

    return E1KoszulDualData(
        name=f"W_{{1+inf}}(N={N})",
        e1_dual_name=f"Y^-(gl_hat_1, N={N})",
        einf_dual_name=f"W_{{1+inf}}^{{!,E_inf}}(N={N})",
        bar_dim_e1=bar_e1,
        bar_dim_einf=bar_einf,
        excess_dim=excess,
        kappa_dual=-kappa_reg,
    )


# =========================================================================
# 6. SHADOW DEPTH AND CY3 GEOMETRY
# =========================================================================

class ShadowGeometryBridge(NamedTuple):
    """Bridge between shadow depth and CY3 geometric invariants.

    This encodes the structural question: does shadow depth encode
    invariants of the CY3 geometry?

    For compact CY3s:
      kappa = chi_top/24 (CONJECTURAL for rigid CY3s)
      kappa is a rational number determined by Hodge numbers.

    Shadow class:
      G: free-field realization (no bound states). CY3 geometry: local
         model with single compact cycle (conifold).
      L: Lie-type. CY3 geometry: quiver description with finite-type
         interaction (local P^2, finite McKay quiver).
      C: contact type. CY3 geometry: not observed for CY3 algebras
         (contact class requires beta-gamma systems).
      M: mixed/infinite. CY3 geometry: either infinite-rank algebra
         (W_{1+inf} from C^3) or infinite GW invariants (compact CY3s).
    """
    name: str
    kappa: Fraction
    shadow_class: str
    euler_chi: int
    h11: int
    h21: int
    dt_finite: bool
    gw_finite: bool
    depth_encodes_geometry: str


def shadow_geometry_bridge(name: str) -> ShadowGeometryBridge:
    """Compute the shadow-geometry bridge for a CY3."""
    data = all_cy3_shadow_data()
    if name not in data:
        raise ValueError(f"Unknown CY3: {name}. Known: {list(data.keys())}")
    d = data[name]
    return ShadowGeometryBridge(
        name=d.name,
        kappa=d.kappa,
        shadow_class=d.shadow_class,
        euler_chi=d.euler_chi,
        h11=d.h11,
        h21=d.h21,
        dt_finite=d.bps_finite,
        gw_finite=(d.shadow_class in ('G', 'L')),
        depth_encodes_geometry=_depth_geometry_description(d),
    )


def _depth_geometry_description(d: CY3ShadowData) -> str:
    """Describe what shadow depth encodes geometrically."""
    if d.shadow_class == 'G':
        return (
            f"Class G (r_max={d.r_max}): kappa={d.kappa} encodes Euler "
            f"characteristic. Shadow terminates: BPS spectrum finitely "
            f"generated, only quadratic OPE data."
        )
    elif d.shadow_class == 'L':
        return (
            f"Class L (r_max={d.r_max}): kappa={d.kappa} + cubic shadow "
            f"encode Euler characteristic + first GW correction. "
            f"Cubic shadow from 3-vertex quiver interaction."
        )
    elif d.shadow_class == 'M':
        return (
            f"Class M (r_max=inf): kappa={d.kappa} is the leading "
            f"coefficient. The full infinite tower encodes ALL GW/DT "
            f"invariants: F_g = kappa * lambda_g + higher-arity "
            f"corrections. Shadow depth = complexity of DT theory."
        )
    else:
        return f"Class {d.shadow_class}: unclassified."


# =========================================================================
# 7. CRITICAL DISCRIMINANT FOR CY3 CHANNELS
# =========================================================================

def critical_discriminant_cy3(kappa: Fraction, S4: Fraction) -> Fraction:
    r"""Critical discriminant Delta = 8 * kappa * S_4.

    Delta = 0 <=> finite shadow depth (class G or L).
    Delta != 0 <=> infinite shadow depth (class M).

    For CY3 algebras:
      C^3 (Virasoro channel): Delta = 8 * (1/2) * 10/27 = 40/27.
      Conifold: Delta = 0 (Heisenberg, S_4 = 0).
      Local P^2: Delta != 0 (class M, AP-CY12: infinite tower).
    """
    return 8 * kappa * S4


def critical_discriminant_w1inf_spin2(c: Fraction = Fraction(1)) -> Fraction:
    """Critical discriminant for the spin-2 (Virasoro) channel of W_{1+inf}.

    kappa_T = c/2, S_4 = 10/[c(5c+22)].
    Delta = 8 * (c/2) * 10/[c(5c+22)] = 40/(5c+22).
    At c=1: Delta = 40/27.
    """
    return Fraction(40) / (5 * c + 22)


# =========================================================================
# 8. E_1 SHADOW TOWER COMPUTATION
# =========================================================================

def e1_shadow_tower_channel(
    kappa: Fraction,
    alpha: Fraction,
    S4: Fraction,
    max_r: int = 20,
) -> Dict[int, Fraction]:
    r"""Compute E_1 shadow tower on a single primary line.

    The E_1 shadow tower at the scalar (contact) level is the SAME
    as the E_inf shadow tower, because the contact term is cyclic
    invariant. The E_1 bar complex has more generators at each arity,
    but the shadow tower (the MC element projected to the cyclic
    deformation complex) uses only the cyclic part.

    Uses the Vol I convolution recursion:
      Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
      f(t) = sqrt(Q_L(t)) = sum a_n t^n
      S_r = a_{r-2} / r

    Returns {r: S_r} for r = 2, ..., max_r.
    """
    if kappa == 0:
        raise ValueError("kappa = 0: shadow tower undefined (uncurved)")

    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4

    a0 = 2 * kappa
    a = [a0]

    max_n = max_r - 2
    if max_n >= 1:
        a1 = q1 / (2 * a0)
        a.append(a1)

    if max_n >= 2:
        a2 = (q2 - a[1] ** 2) / (2 * a0)
        a.append(a2)

    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        an = -conv / (2 * a0)
        a.append(an)

    result: Dict[int, Fraction] = {}
    for r in range(2, max_r + 1):
        idx = r - 2
        if idx < len(a):
            result[r] = a[idx] / r

    return result


def e1_shadow_tower_w1inf_virasoro_channel(
    c: Fraction = Fraction(1),
    max_r: int = 20,
) -> Dict[int, Fraction]:
    """E_1 shadow tower for the Virasoro (spin-2) channel of W_{1+inf}.

    kappa_T = c/2, alpha_T = 2, S_4 = 10/[c(5c+22)].
    """
    kappa = c / 2
    alpha = Fraction(2)
    S4 = Fraction(10) / (c * (5 * c + 22))
    return e1_shadow_tower_channel(kappa, alpha, S4, max_r)


# =========================================================================
# 9. SC FORMALITY CLASSIFICATION
# =========================================================================

class SCFormalityData(NamedTuple):
    """Swiss-cheese formality data for a CY3-derived E_1 algebra.

    sc_formal: whether all m_k^{SC} = 0 for k >= 3.
    formality_depth: the first k where m_k^{SC} != 0, or -1 if formal.
    obstruction_source: what drives the non-formality.
    """
    name: str
    sc_formal: bool
    formality_depth: int  # -1 if formal
    obstruction_source: str


def sc_formality_cy3(name: str) -> SCFormalityData:
    """SC formality classification for a CY3 algebra."""
    data = all_cy3_shadow_data()
    if name not in data:
        raise ValueError(f"Unknown CY3: {name}")
    d = data[name]

    if d.sc_formal:
        return SCFormalityData(
            name=d.name,
            sc_formal=True,
            formality_depth=-1,
            obstruction_source="none (SC formal)",
        )

    # Non-formal: the first obstruction depth
    if d.shadow_class == 'M':
        return SCFormalityData(
            name=d.name,
            sc_formal=False,
            formality_depth=3,  # First non-formal operation at arity 3
            obstruction_source=(
                f"Shadow class M: infinite tower of higher A_inf operations. "
                f"The quartic contact Q^contact = S_4 != 0 forces non-formality "
                f"starting at arity 3 (cubic shadow) for algebras with alpha != 0."
            ),
        )
    elif d.shadow_class == 'C':
        return SCFormalityData(
            name=d.name,
            sc_formal=False,
            formality_depth=4,
            obstruction_source="Contact class: quartic shadow terminates the tower.",
        )

    if d.shadow_class == 'L':
        return SCFormalityData(
            name=d.name,
            sc_formal=False,
            formality_depth=3,
            obstruction_source="Class L: m_3^{SC} != 0 (Lie bracket, NOT SC-formal).",
        )

    return SCFormalityData(
        name=d.name,
        sc_formal=True,
        formality_depth=-1,
        obstruction_source="formal (class G only)",
    )


# =========================================================================
# 10. FULL LANDSCAPE CENSUS
# =========================================================================

class CY3LandscapeCensus(NamedTuple):
    """Complete landscape census of CY3 Swiss-cheese data."""
    entries: List[CY3ShadowData]
    class_counts: Dict[str, int]    # G/L/C/M -> count
    formal_count: int
    nonformal_count: int
    total: int


def cy3_landscape_census() -> CY3LandscapeCensus:
    """Compute the full CY3 landscape census."""
    data = all_cy3_shadow_data()
    entries = list(data.values())
    class_counts: Dict[str, int] = {}
    formal_count = 0
    nonformal_count = 0

    for d in entries:
        cls = d.shadow_class
        class_counts[cls] = class_counts.get(cls, 0) + 1
        if d.sc_formal:
            formal_count += 1
        else:
            nonformal_count += 1

    return CY3LandscapeCensus(
        entries=entries,
        class_counts=class_counts,
        formal_count=formal_count,
        nonformal_count=nonformal_count,
        total=len(entries),
    )


# =========================================================================
# 11. E_1 BAR DIFFERENTIAL TERMS
# =========================================================================

def e1_bar_differential_terms(n: int) -> int:
    """Number of terms in the E_1 bar differential at bar degree n.

    The E_1 bar differential:
      d_bar[a_1|...|a_n] = sum_{i=1}^{n-1} +/- [a_1|...|m(a_i,a_{i+1})|...|a_n]

    has n-1 terms (one for each adjacent pair).

    For comparison, the E_inf bar differential at bar degree n has
    the same number of composition terms (n-1), but each term involves
    the SYMMETRIC product (which is the same as the ordered product
    for an E_inf algebra due to the commutativity constraint).
    """
    if n < 2:
        return 0
    return n - 1


def e1_bar_differential_matrix_dim(n_generators: int, bar_degree: int) -> Tuple[int, int]:
    """Dimensions of the E_1 bar differential matrix at given bar degree.

    d: B^{E_1}_{bar_degree} -> B^{E_1}_{bar_degree - 1}

    dim(source) = n_generators^{bar_degree}
    dim(target) = n_generators^{bar_degree - 1}

    Returns (n_rows, n_cols) = (dim_target, dim_source).
    """
    if bar_degree < 2:
        return (0, 0)
    source = n_generators ** bar_degree
    target = n_generators ** (bar_degree - 1)
    return (target, source)


# =========================================================================
# 12. VERIFICATION: SHADOW TOWER VALUES
# =========================================================================

def verify_shadow_tower_virasoro_c1(max_r: int = 10) -> Dict[str, Any]:
    """Verify shadow tower for Virasoro at c=1 against known values.

    The Virasoro at c=1 has:
      kappa = 1/2
      alpha = 2
      S_4 = Q^contact = 10/27

    S_2 = kappa = 1/2  (by definition)
    S_3 = alpha/3 * kappa ... actually from the recursion:
      a_0 = 2*kappa = 1, a_1 = q_1/(2*a_0) = 12*(1/2)*2 / (2*1) = 6.
      S_3 = a_1/3 = 2.

    Actually let me recompute: S_r = a_{r-2}/r.
    a_0 = 2*kappa = 1.  S_2 = a_0/2 = 1/2. Check: matches kappa = 1/2. Good.
    a_1 = q_1/(2*a_0) = 12*(1/2)*2 / (2*1) = 12/2 = 6. S_3 = 6/3 = 2.
    """
    tower = e1_shadow_tower_w1inf_virasoro_channel(Fraction(1), max_r)
    return {
        'tower': tower,
        'S_2': tower.get(2, None),
        'S_3': tower.get(3, None),
        'S_2_matches_kappa': tower.get(2) == Fraction(1, 2),
    }


# =========================================================================
# 13. MAIN RESULTS SUMMARY
# =========================================================================

def main_results() -> Dict[str, Any]:
    """Summary of main results from this module."""
    census = cy3_landscape_census()
    return {
        'census': census,
        'c3_shadow': cy3_shadow_data_c3(),
        'conifold_shadow': cy3_shadow_data_conifold(),
        'local_p2_shadow': cy3_shadow_data_local_p2(),
        'quintic_shadow': cy3_shadow_data_quintic(),
        'k3xe_shadow': cy3_shadow_data_k3xe(),
        'virasoro_tower_c1': verify_shadow_tower_virasoro_c1(),
        'delta_w1inf_spin2_c1': critical_discriminant_w1inf_spin2(Fraction(1)),
        'quartic_e1_w1inf_N10': quartic_e1_w1inf_total(10, Fraction(1)),
        'e1_bar_heisenberg': e1_bar_dimensions("H_1", 1, 6),
        'e1_bar_sl2': e1_bar_dimensions("V_k(sl_2)", 3, 6),
        'e1_bar_w1inf_N5': e1_bar_dimensions("W_{1+inf}(N=5)", 5, 6),
    }
