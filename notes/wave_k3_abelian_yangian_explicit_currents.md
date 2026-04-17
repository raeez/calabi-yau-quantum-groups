# Wave: K3 abelian Yangian explicit Drinfeld currents

Date: 2026-04-17
Working directory: /Users/raeez/calabi-yau-quantum-groups
Style: Beilinson-Drinfeld + Chriss-Ginzburg + Russian school

## Frontier targeted

Theorem `thm:cy-c-abelian-K3` (in chapters/examples/cy_c_six_routes_convergence.tex L518) asserts the existence of 24 x 3 Drinfeld currents `{E_a(z), F_a(z), psi^pm_a(z)}` and a structure function `G_K3(x)`, but the explicit OPE coefficients at all orders in (z-w)^{-1} have not been written out. The previous `k3_abelian_yangian_presentation.py` engine gives the high-level presentation (Heisenberg OPE, transfer matrix, structure function, Miura coproduct) but does not write down the explicit currents x^pm_i(z) and the lattice VOA half of the bridge.

This wave inscribes:

1. The 24 simple roots alpha_i in the Mukai lattice Lambda_Muk = U^3 + E_8(-1)^2 (signature (4,20), basis adapted to the diagonal Heisenberg).
2. The 24 x 3 Drinfeld currents x^+_i(z), x^-_i(z), h_i(z) for i = 1..24 in the abelian Heisenberg presentation.
3. The OPE coefficients of x^+_i(z) x^+_j(w) at orders (z-w)^{-2}, (z-w)^{-1}, (z-w)^0 in closed form.
4. The Cartan currents h_i(z) and the OPE h_i(z) x^pm_j(w).
5. The K3 elliptic genus matching: the bar Euler product of the abelian K3 Yangian agrees with the K3 lattice VOA character (1/eta(q)^{24}) via PBW.
6. The Drinfeld coproduct Delta_z(x^+_i(u)) = x^+_i(u) (x) 1 + 1 (x) x^+_i(u-z) at the abelian level (NO higher correction terms in the abelian case), and the explicit Cartan correction Delta_z(h_i(u)) = h_i(u) (x) 1 + 1 (x) h_i(u-z).

## Mathematical content (Platonic ideal)

### 1. The 24 simple roots of g_K3 at the abelian level

The Mukai lattice `Lambda_Muk = H^*(K3, Z)` has rank 24 and signature (4, 20).
In the standard decomposition

  Lambda_Muk = U + U + U + E_8(-1) + E_8(-1)
               H^0+H^4   H^{1,1}_{three U planes}   E_8 root lattices

choose a basis `{alpha_1, ..., alpha_24}` adapted to the orthogonal direct
sum, where the first 4 vectors span the 4 positive eigenspaces:

  alpha_1 = (1, 1, 0, 0, 0, 0)/sqrt 2 in U_1 (first hyperbolic plane H^0+H^4)
  alpha_2 = (1, 1, 0, 0, 0, 0)/sqrt 2 in U_2 (second hyperbolic plane)
  alpha_3 = (1, 1, 0, 0, 0, 0)/sqrt 2 in U_3 (third hyperbolic plane)
  alpha_4 = positive Killing direction in E_8(-1)+E_8(-1)
              (any norm > 0 vector in the negative-definite root system,
               unique up to Weyl orbit; we fix a canonical representative.)
  alpha_5..24 = the remaining 20 negative eigendirections.

For the *abelian* (g = gl_1) Yangian, only the LATTICE METRIC <alpha_i, alpha_j>_Muk = epsilon_i delta_{ij} matters, with epsilon_i in {+1,-1} and the count (4,20). The ROOT-SYSTEM structure (E_8 cup E_8) does not enter at the abelian level: it would enter only when we promote to the non-abelian super-Yangian Y(gl(4|20)) (CONJECTURAL, AP-CY58).

### 2. The 24 Drinfeld currents

For each simple root alpha_i (i = 1..24), define the abelian Drinfeld
currents as follows. Let `J_i(z)` be the Heisenberg current with OPE

  J_i(z) J_j(w) ~ epsilon_i delta_{ij} / (z-w)^2.

Set

  h_i(z) := epsilon_i J_i(z)         (Cartan current of i-th root)
  x^+_i(z) := V_{alpha_i}(z)         (lattice vertex operator at alpha_i)
  x^-_i(z) := V_{-alpha_i}(z)        (lattice vertex operator at -alpha_i)

Here `V_{alpha_i}(z) = :exp(integral J_i(z)):` is the standard lattice
vertex operator constructed from the Heisenberg J_i. The exponential
notation has the explicit mode form

  V_{alpha_i}(z) = exp(epsilon_i sum_{n<0} J_{i,n} z^{-n}/n)
                 . exp(epsilon_i sum_{n>0} J_{i,n} z^{-n}/n)
                 . z^{epsilon_i J_{i,0}} c_{alpha_i}

where c_{alpha_i} is a cocycle factor (trivial for the abelian case).

### 3. OPE coefficients at orders (z-w)^{-2}, (z-w)^{-1}, (z-w)^0

The lattice OPE of two vertex operators V_alpha(z) V_beta(w) is

  V_alpha(z) V_beta(w) = (z-w)^{<alpha,beta>} :V_alpha(z) V_beta(w):
                          . (cocycle factor).

For the abelian K3 Yangian with diagonal Mukai metric, the explicit OPE
at small orders is:

(a) Same root, opposite sign. For x^+_i(z) x^-_i(w):
   <alpha_i, -alpha_i> = -epsilon_i, so

   x^+_i(z) x^-_i(w) = (z-w)^{-epsilon_i} :V_{alpha_i}(z) V_{-alpha_i}(w):

   Expanding around z = w, the OPE coefficients (Wick) are:

   (i) epsilon_i = +1 (i = 1..4):
       x^+_i(z) x^-_i(w) ~ (z-w)^{-1} . [identity term]
                          + (z-w)^0 . h_i(w)
                          + (z-w)^1 . [polynomial in h_i, partial h_i]/2
                          + ...

   (ii) epsilon_i = -1 (i = 5..24):
        x^+_i(z) x^-_i(w) is REGULAR at (z-w)^0 with leading term 1
        (negative metric direction; "anti-Heisenberg").

(b) Same root, same sign.
   <alpha_i, alpha_i> = epsilon_i, so

   x^+_i(z) x^+_i(w) = (z-w)^{epsilon_i} :V_{alpha_i}(z) V_{alpha_i}(w):

   For epsilon_i = +1: this is REGULAR (vanishes linearly at z=w, since
   the lattice vector 2 alpha_i has norm 4 not 0; the SAME-sign OPE
   has positive power, so the coefficient at (z-w)^{-2} and (z-w)^{-1}
   IS ZERO and the leading term is at (z-w)^0).

   For epsilon_i = -1: x^+_i(z) x^+_i(w) ~ (z-w)^{-1}, so the coefficient
   at (z-w)^{-1} is the OPE singular term :V_{2 alpha_i}(w):.

(c) Different roots. <alpha_i, alpha_j> = 0 for i != j (orthogonal basis),
   so

   x^+_i(z) x^+_j(w) = :V_{alpha_i}(z) V_{alpha_j}(w):  (REGULAR).

   In particular, the coefficients at (z-w)^{-2} and (z-w)^{-1} are
   IDENTICALLY ZERO for i != j.

These are the explicit OPE coefficients of the 24 abelian Drinfeld
currents at orders 0, 1, 2 in (z-w)^{-1} (where order n means coefficient
of (z-w)^{-n}).

### 4. The Cartan currents h_i(z)

In the abelian (gl_1) presentation, the Cartan currents are linear in J:

  h_i(z) = epsilon_i J_i(z)        (i = 1..24)

The Cartan-Cartan OPE is diagonal:

  h_i(z) h_j(w) ~ epsilon_i epsilon_j epsilon_i delta_{ij} / (z-w)^2
                = epsilon_i delta_{ij} / (z-w)^2.

(The factor epsilon_i^2 = 1 collapses the metric flip; the diagonal
metric (z-w)^{-2} pole has coefficient epsilon_i.)

The Cartan-current to ladder-operator OPE is

  h_i(z) x^pm_j(w) ~ +/- delta_{ij} epsilon_i x^pm_j(w) / (z-w)
                    = +/- A_{ij} x^pm_j(w) / (z-w)

where A_{ij} = epsilon_i delta_{ij} is the (DIAGONAL) "Cartan matrix" of the
abelian K3 Yangian -- diagonal because the Mukai pairing on simple roots
is diagonal in the chosen basis.

### 5. K3 lattice VOA character matching at the K3 elliptic genus

The Heisenberg lattice VOA F_{Lambda_Muk} associated to the Mukai lattice
has character

  ch F_{Lambda_Muk}(q) = Theta_{Lambda_Muk}(q) / eta(q)^{24}

where Theta_{Lambda_Muk}(q) = sum_{lambda in Lambda_Muk} q^{<lambda,lambda>/2}
is the lattice theta series (= 1 if we restrict to the trivial sector,
which is the relevant one for the chiral algebra A = U^ch(H_Muk)).

The bar Euler product of the abelian K3 Yangian Y(g_K3) matches:

  E_bar(Y(g_K3))(q) = prod_{n>=1} (1 - q^n)^{24} = eta(q)^{24}/q

  ch F_{Lambda_Muk}^{trivial sector}(q) = 1/eta(q)^{24}

The PBW filtration identifies the associated graded of Y(g_K3) with
Sym(H_Muk[u]) = Sym(C^{24}[u]), whose Euler product gives 1/eta(q)^{24}.
The bar/cobar duality between Y(g_K3) and its Koszul dual then gives the
TWO factors: the BAR side eta(q)^{24} and the COBAR side 1/eta(q)^{24}.

Their product is 1: this is the Koszul conductor K = 0, equivalent to
kappa_ch + kappa_ch^! = 0 (free-field branch).

### 6. Drinfeld coproduct: ABELIAN case has NO correction

The general Drinfeld coproduct on a Yangian has the form

  Delta_z(x^+_i(u)) = x^+_i(u) (x) 1 + 1 (x) x^+_i(u-z) + correction terms.

For the *abelian* (gl_1) K3 Yangian, the correction terms VANISH:

  Delta_z^{ab}(x^+_i(u)) = x^+_i(u) (x) 1 + 1 (x) x^+_i(u-z)
  Delta_z^{ab}(x^-_i(u)) = x^-_i(u) (x) 1 + 1 (x) x^-_i(u-z)
  Delta_z^{ab}(h_i(u))   = h_i(u)   (x) 1 + 1 (x) h_i(u-z).

The reason: the correction terms in the non-abelian Drinfeld coproduct
come from the structure constants f^{ab}_c of the underlying Lie algebra,
which are ZERO for gl_1 (abelian). The abelian Yangian is therefore
strictly cocommutative (modulo the spectral shift z), and the coproduct is
"primitive" in the spectral parameter shift.

The shift z is the abelian-level avatar of the Yangian SPECTRAL parameter:
shifting u -> u - z creates an evaluation module V_{u-z} from V_u, and the
coproduct is the standard Yangian "shifted" coproduct on evaluation modules.

This is the explicit form of the universal coproduct from
`prop:universal-coproduct` (k3_times_e.tex) at the abelian (gl_1) level.

## Verification strategy (per HZ3-11)

The independent verification of the explicit Drinfeld currents must compare:

DERIVATION SOURCE: lattice vertex operator construction
  - Mukai lattice Lambda_Muk = U^3 + E_8(-1)^2 with signature (4,20).
  - Standard lattice VOA construction V_alpha = :exp(integral J_alpha):.
  - OPE V_alpha(z) V_beta(w) = (z-w)^{<alpha,beta>} :V_alpha V_beta:(w).

VERIFICATION SOURCE: Heisenberg current OPE + K3 elliptic genus
  - Heisenberg OPE [J_{i,m}, J_{j,n}] = m epsilon_i delta_{ij} delta_{m+n,0}
    derived from the Mukai pairing as a SYMPLECTIC form.
  - K3 elliptic genus phi_{0,1}(tau,z) coefficient c(0) = 20 + 4 = 24
    (NOT taken from the Mukai signature; computed from the EZ theta series).
  - PBW filtration on Y(g_K3) gives associated graded Sym(C^{24}[u]).

The two sources are DISJOINT:
  - Lattice VOA construction is an algebraic recipe given a SYMMETRIC pairing.
  - Heisenberg OPE + K3 elliptic genus are independent: the Heisenberg OPE
    needs only the antisymmetrized pairing, the elliptic genus computes c(0)
    from theta-function ratios, and the rank-24 truncation is a topological
    fact (b_0 + b_2 + b_4 = 24) NOT used in the lattice VOA derivation.

## Artifacts to produce

1. notes/wave_k3_abelian_yangian_explicit_currents.md (this file).
2. compute/lib/k3_abelian_yangian_currents.py (~600 lines of explicit
   construction).
3. compute/tests/test_k3_abelian_yangian_currents.py (~30 tests with
   @independent_verification decorator).
4. Inscribed extension in chapters/examples/cy_c_six_routes_convergence.tex
   after thm:cy-c-abelian-K3 (~80 lines): explicit subsection
   "The 24 Drinfeld currents at the abelian K3 level: explicit form".

## Status discipline

The presentation theorem (existence of 24 currents, OPE coefficients at
small orders, lattice VOA matching, primitive abelian coproduct) is at
d=2, conditional on CY-A_2 (PROVED). The IDENTIFICATION of the resulting
Yangian with the CY-C "chiral quantum group C(g_{K3}, q)" remains
CONJECTURAL (AP-CY6, AP-CY40). We use \begin{theorem} for the explicit
construction and \begin{remark} for the identification with CY-C.
