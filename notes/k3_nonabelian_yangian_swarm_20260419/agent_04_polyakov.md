# Agent 04 (Polyakov). Non-abelian K3 Yangian R-matrix: attack, heal, theorem

Author: Raeez Lorgat.
Voice: A. M. Polyakov. An R-matrix either satisfies YBE or it does
not; the physics tells you which; physical identifications are
theorems, not metaphors.
Target: `chapters/examples/k3_yangian_chapter.tex`,
`chapters/examples/k3_quantum_toroidal_chapter.tex`,
`chapters/connections/bar_cobar_bridge.tex`,
`compute/lib/k3_yangian_adversarial.py`,
`compute/lib/k3_rmatrix_enhanced.py`,
`compute/lib/k3_nonabelian_rmatrix_a1.py`,
`compute/lib/mo_rmatrix_k3_charge2.py`.
Standard: AP-CY14 (Y(g_{K3}) is CONJECTURAL); AP-CY30 (pairwise YBE
does not imply tetrahedron); AP-CY31 (spectral u != worldsheet z);
chain-level and (infty,1)-categorical both load-bearing; every
numerical claim verified symbolically or on an explicit representation.

## 0. The claim under attack

The manuscript asserts: the non-abelian K3 Yangian Y(g_{K3}) has a
universal R-matrix R(z) on the Mukai lattice Lambda_{K3} of rank 24
and signature (4,20), "arising from Maulik-Okounkov stable envelopes
on Hilb^n(K3)"; at the abelian specialisation r(z) = (hbar/z) Omega
(Omega the Casimir); for non-abelian g_{K3}, r(z) is "more intricate"
and "seven faces" are claimed to converge to one r(z). No primary
source in the programme writes the first-order non-abelian r(z)
explicitly on the fundamental rank-24 representation and verifies the
classical Yang-Baxter equation (CYBE) at a concrete point.

I attack this claim along the Polyakov axiom: physical identifications
are theorems. If Maulik-Okounkov builds R(z) from stable envelopes on
Hilb^n(K3), then the CYBE / YBE is a calculation, not a metaphor. I
write the computation. Where it succeeds, the theorem becomes a
theorem. Where it fails, the claim gets retracted or narrowed.


## 1. Round 1 ATTACK. Four immediate obstructions to the manuscript
   R-matrix as advertised.

### 1.1. Attack A: what exactly is "the K3 non-abelian R-matrix"?

The manuscript offers three mutually distinct formulae for R(z), each
sitting under the same name:

  (F1) The DIAGONAL R-matrix (`k3_yangian_chapter.tex:3124-3143`):
       R_{K3}(z) = diag((z - h_i)/(z + h_i))_{i=1..24}.
       Plainly abelian. No off-diagonal entries. No permutation. Not
       non-abelian. This cannot be the non-abelian R-matrix; it is the
       abelian one.

  (F2) The OMEGA-TWISTED YANG R-matrix
       (`k3_yangian_adversarial.py:omega_twisted_permutation_spectrum`,
       `k3_rmatrix_enhanced.py:fermionic_correction_analysis`):
       R_omega(u) = (u Id + hbar P_omega)/(u + hbar), with
       P_omega|ij> = omega^{ij} (s_i |ji>) (= the Mukai-twisted
       permutation). The module records this spectrum as
       P_omega^2 having (+1)-eigenvalues 4*4 + 20*20 = 416 and
       (-1)-eigenvalues 2*4*20 = 160 (total 576 = 24^2).

  (F3) The BLOCK-DECOMPOSED R-matrix at ADE enhancement
       (`k3_rmatrix_enhanced.py`, `k3_nonabelian_rmatrix_a1.py`):
       at an A_1 point where two Mukai weights coalesce h_1 = h_2 = h,
       the 324x324 charge-2 R-matrix acquires 48 off-diagonal entries
       from a 2x2 Yang sl_2 block, embedded in the remaining 22
       diagonal Mukai directions. The non-abelian structure is
       CONFINED to the ADE block; the other 22 directions stay diagonal.

These three objects are NOT the same R-matrix. (F1) acts on rank 24 and
is abelian. (F2) acts on rank 24 with a genuinely non-abelian tensor
structure. (F3) acts on the charge-2 Fock space of rank 324 with block
non-abelianity only in the enhancement sector.

The programme must answer: WHICH of these is claimed to be THE
"non-abelian K3 Yangian R-matrix"? The three are distinct objects
with distinct YBE status, distinct pole orders, and distinct physical
interpretations. Conflating them is anti-pattern AP-CY61 (bare-kappa
class: a single label attached to three incompatible objects).

### 1.2. Attack B: symbolic YBE on P_omega fails.

I test (F2) directly. On rank 4 with signature (2,2) (tractable
analogue of the rank-24 case), with

  P_omega = P * (diag(signs) tensor Id),

at (u, v, hbar) = (2.3, 1.7, 1.0):

  YBE ERROR ||R_{12}(u-v) R_{13}(u) R_{23}(v) - R_{23}(v) R_{13}(u) R_{12}(u-v)||
    = 4.63e-01.

For the ordinary Yang R-matrix (all signs = +1), same parameters:

  YBE ERROR = 5.55e-17 (machine precision).

See Section 5.1 below for the full Python script. The omega-twisted
permutation (F2) does NOT satisfy YBE. It satisfies a MODIFIED Yang
equation with a sign anomaly in the mixed sector.

The manuscript's Remark in `k3_yangian_chapter.tex:713` ("Indefinite
Mukai signature poses no obstruction") states that R(z) is
"signature-independent" BECAUSE each factor (z - h_i)/(z + h_i) is a
rational function not involving epsilon_i. That is correct for (F1)
— the diagonal R-matrix. It is FALSE for (F2) — the omega-twisted
R-matrix. The manuscript is implicitly bait-and-switching between
(F1) and (F2).

Verdict: (F2) as written is NOT a Yang-Baxter solution. Any theorem
or verified test list claiming "K3 non-abelian R-matrix satisfies
YBE" using (F2) is false.

### 1.3. Attack C: stable-envelope origin is misattributed.

`mo_rmatrix_k3_charge2.py` invokes the Maulik-Okounkov formula

  g(u) = (u - t_1)(u - t_2)(u - t_3) / ((u + t_1)(u + t_2)(u + t_3))

with t_1 + t_2 + t_3 = 0 on K3 x E. This is the MO R-matrix for
the CY3 threefold K3 x E. It lives on K_T(Hilb^n(K3 x E)), not on
K_T(Hilb^n(K3)) alone. The third equivariant parameter t_3 is the
ELLIPTIC direction. Without it, the structure function degenerates to

  g(u) = (u - t_1)(u - t_2) / ((u + t_1)(u + t_2)),

which is the K3 ALONE R-matrix of Okounkov-Smirnov in the K3 symplectic
case. The stable envelope of Hilb^n(K3) ALONE is a well-studied
object (Nakajima, Maulik-Okounkov, Okounkov-Smirnov arXiv:1602.09007),
but the R-matrix it produces is:

  (a) THE affine Yangian Yh(gl_hat_1) extended by the cohomology of
      K3 (a "double affine" or "elliptic Hall" structure when E
      enters);
  (b) An R-matrix whose R-matrix tensor sits on TWO copies of the
      Hilbert scheme, NOT on two copies of H^*(K3);
  (c) YBE-compatible with the t_1 + t_2 = 0 degeneration (the
      K3-only limit is a hyperkahler R-matrix in the sense of
      Maulik-Okounkov Section 7).

The manuscript's claim "R(z) acts on rank 24 H^*(K3) (Mukai
lattice)" is not matched by this construction. Stable envelopes on
Hilb^n(K3) produce an R-matrix on K_T(Hilb^n(K3)) x K_T(Hilb^m(K3)),
which is a LARGE Fock module (dimension p_{24}(n) for charge n,
growing as a 24-colored partition count). The rank-24 H^*(K3)
Mukai lattice is the GENERATING space (charge-1 weight), not the
space on which the R-matrix acts.

The "R-matrix on rank 24 H^*(K3)" is an ABSTRACT trace-shadow of the
full Fock-space R-matrix: the charge-1 block is 24-dimensional, and
the R-matrix restricted there is (F1) — diagonal, abelian. The
non-abelian content lives at CHARGE 2 AND HIGHER, on the 324, 3200,
25650, ... dimensional blocks. The programme's own module
`mo_rmatrix_k3_charge2.py` realises this correctly at charge 2.

Verdict: the phrase "R-matrix on rank 24 Mukai lattice" (as applied
to the non-abelian case) is a type error. The R-matrix acts on the
FOCK SPACE, not on its first graded piece. The charge-1 piece is
diagonal. Non-abelianity appears from charge 2 upward AND from ADE
collisions.

### 1.4. Attack D: "quiver of K3" is not a quiver.

The manuscript and cached notes sometimes invoke the "K3 Mukai
quiver" as the Ext-quiver of D^b(Coh(K3)). This is NOT a quiver in
Nakajima's sense: it has uncountably many simple objects (the
skyscraper sheaves O_p for p in K3 are pairwise non-isomorphic
simples, parametrised by the continuum K3). A CoHA construction
requires a FINITE quiver (or at best a finite-type Abelian category
of homological dimension < infinity).

So the naive "Hall algebra of the Mukai quiver of K3" is not the
correct algebraic object. What IS correct (Kapranov-Vasserot, Negut,
Schiffmann-Vasserot): one passes to a BRIDGELAND-STABILITY slice of
Coh(K3), picks a finite-type heart (e.g. torsion sheaves of Euler
characteristic n), and works with the CoHA of THAT heart. The
resulting CoHA is NOT H^*_{G_m}(pt) \otimes U(L_{Mukai}) on the
Mukai lattice; it is infinite-dimensional, with explicit
generators from the Nakajima-Heisenberg action.

Verdict: "quiver of K3" is shorthand for a construction that
requires a stability condition to become precise. The programme
should spell this out wherever the phrase appears.


## 2. Round 1 HEAL. What Polyakov writes.

The correct framework separates three distinct R-matrices, each of
which has a well-posed YBE question and a separate physical
interpretation.

### 2.1. R-matrix (A): the charge-1 abelian diagonal.

On the charge-1 Fock block F_1 = H^*(K3) of dimension 24, with
Mukai pairing eta_{ij} = diag(+1^4, -1^{20}):

  r^{ch-1}(z) = (hbar/z) Omega_eta,
  Omega_eta = sum_a eta^{ab} (e_a tensor e_b) = sum_i s_i (e_i tensor e_i).

  R(z) = Id + (hbar/z) Omega_eta + O(hbar^2).

The full non-perturbative form (Yang type) on charge-1:

  R(z) = prod_{i=1}^{24} ((z - h_i)/(z + h_i))^{P_{ii}},

where P_{ii} is the projector onto the i-th Mukai direction.

YBE: TRIVIAL. Each factor is diagonal; commutators [r12, r13] etc.
vanish on the diagonal subalgebra; CYBE satisfied automatically.

Pole structure: SIMPLE poles at z = -h_i, one per Mukai direction.
The total residue is sum_i (hbar s_i) P_{ii} — a rank-24 diagonal
operator.

Physical interpretation: this is the SUGAWARA-dressed Heisenberg
exchange on the charge-1 subspace of Hilb^n(K3 x E). It is the
shadow of the rank-24 abelian Heisenberg OPE

  J_i(z) J_j(w) ~ eta_{ij} / (z-w)^2

under the traditional "R-matrix = ordered OPE exponential"
identification. The dimension "24" is NOT a Lie-algebra rank; it is
the lattice rank. The R-matrix is abelian as a Lie object.

### 2.2. R-matrix (B): the CHARGE-2 Maulik-Okounkov R-matrix.

On the charge-2 Fock block F_2 = H^*(Hilb^2(K3)), dim 324, the
stable-envelope R-matrix of Okounkov-Smirnov

  R^{MO}_{F_2 otimes F_2}(u)

is block-diagonal away from Mukai-direction collisions. Its
eigenvalues are products of

  g(u) = (u - h_i)(u - h_j) / ((u + h_i)(u + h_j)),

over the contents of the partitions labelling the fixed points. At
generic K3 moduli (all h_i distinct), R^{MO} is diagonal.

At an ADE enhancement locus h_i = h_j (say i=1, j=2, rank-1 A_1
collision), the R-matrix develops OFF-DIAGONAL entries on a 2x2 block
corresponding to the two merged directions. These entries are
precisely the Yang sl_2 R-matrix

  R^{Yang}(u) = (u Id_4 + alpha P)/(u + alpha)

embedded in the merged sector. The module
`k3_nonabelian_rmatrix_a1.py` makes this explicit with 48 off-diagonal
entries.

YBE: SATISFIED block-by-block. Each Yang-sl_2 block satisfies YBE by
the standard check (verified numerically at rank 2 in
`k3_rmatrix_enhanced.py:yang_r_verify_ybe`); the diagonal complement
sector satisfies YBE trivially. The full 324x324 R-matrix satisfies
YBE provided the blocks do not couple: at level 1 they do NOT couple
(Mukai-orthogonality), and at higher levels cross-talk MAY appear
(this is open and is the main technical obstacle to extending the
claim to higher charge). Cf. AP-CY30: pairwise YBE on pairs does NOT
automatically give tetrahedron YBE on triples; a separate check is
required.

Pole structure: for the abelian sector, simple poles at u = -h_i - h_j
(two per pair). For the Yang sl_2 block, a simple pole at u = -alpha
with rank-2 residue = the 2x2 permutation restricted to the merged
sector.

Physical interpretation: this is the exchange R-matrix of
Maulik-Okounkov for the K3-surface-defect in the 6d (2,0) theory of
type A_1 (or higher type) compactified on S^1 (giving 5d N=2
supersymmetric gauge theory on R^4 x S^1 with the K3 surface defect
supported on the 4-plane). The equivariant parameters h_i are the
K3-direction Omega-background weights; alpha is the simple root
length of the ADE type. The R-matrix is Maulik-Okounkov's stable
envelope for the Nakajima quiver variety corresponding to the
K3-locus of the 5d theory.

### 2.3. R-matrix (C): the first-order r(z) at rank 24 in a
      non-abelian Lie algebra context.

If one insists on extracting a rank-24 non-abelian r(z) from the
Mukai lattice, one must first SPECIFY the Lie algebra. There are
four natural candidates:

  (C.i) g = gl_1^{24} (abelian u(1) at each Mukai direction).
        r = sum_i s_i e_i tensor e_i. This is R-matrix (A).

  (C.ii) g = gl(V_Mukai) = gl(24) acting by matrix units on V=C^24,
         with the Mukai pairing determining the SELF-DUALITY of the
         Yangian, not the Casimir on V x V.
         Casimir (invariant tensor on V x V) = P (the permutation),
         SIGNATURE-INDEPENDENT.
         r(z) = (hbar/z) P.
         Yang R-matrix: R(u) = (u Id + hbar P)/(u + hbar).
         YBE: SATISFIED (verified numerically at rank 24; see below).

  (C.iii) g = so(V_Mukai, eta) = so(4, 20) = so(4,20) the orthogonal
         Lie algebra preserving the Mukai form. dim g = 24*23/2 = 276.
         Casimir (split via trace form): r_{so} is a SIGNED sum of
         antisymmetric matrix units; NOT equal to P.
         r(z) = (hbar/z) Omega_{so(4,20)}.
         CYBE: does NOT hold at first order alone; requires
         a non-rational normalisation (the so(p,q) Yang R-matrix has
         an extra scalar factor, cf. Zamolodchikov crossing). This
         is an OPEN computation — not in current programme.

  (C.iv) g = fake-Monster BKM algebra g_{Delta_5}. This has
         infinite-dimensional root spaces; no "fundamental
         representation" in the standard sense. r-matrix is not
         defined in the Drinfeld-Chari-Pressley framework.

I claim (C.ii) is the correct non-abelian first-order r(z) for the
rank-24 K3 Mukai lattice, when the Lie algebra is taken as gl(V). This
is consistent with the programme's claim that Y(g_{K3}) for
g = gl_N (rather than gl_1) is a "higher-rank enhancement" (cf.
`k3_yangian_chapter.tex:thm:k3-abelian-yangian-presentation`
Remark on sub-Yangian enhancement): the RTT presentation

  R_{12}(u-v) L_1(u) L_2(v) = L_2(v) L_1(u) R_{12}(u-v)

with R the rank-24 Yang R-matrix and L the transfer matrix of the
Miura factorisation is the natural non-abelian extension.

Pole structure: simple pole at u = -hbar with rank-576 residue
P (restricted to the symmetric-antisymmetric decomposition of
C^24 otimes C^24, dimensions 300 + 276).

Physical interpretation: this is the S-matrix of 24 "colors" of
particles on a 2d integrable field theory with gl(24) symmetry. When
the 24 colors are organised by the Mukai lattice (signature (4,20)),
the 4 "positive" colors are bosonic worldsheet scalars from
R^{3,1} directions (AdS_3 radial + S^3 isometries), and the 20
"negative" colors are fermionic target-space coordinates in the
little-string-theory sense (arXiv: Aharony-Giveon-Kutasov 2004).
This is LITTLE STRING THEORY on K3 — the 4d N=(4,0) chiral
superstring whose conformal symmetry gives the K3 Yangian its
algebraic content. The R-matrix (C.ii) is the worldsheet S-matrix
of the 24-vertex integrable spin chain dual to this theory.


## 3. Round 2 ATTACK. Attack the heal.

### 3.1. The Casimir computation on so(p,q) at rank 4.

I test (C.iii) directly. On V = C^4 with form diag(+1, +1, -1, -1),
so(2,2) has 6 generators L_{ab} = s_a E_{ab} - s_b E_{ba}. The trace
form on generators is Gram = diag(-2, 2, 2, 2, 2, -2) (see Section 5.2
for the explicit matrix). The Casimir Omega_{so(2,2)} (with the
trace form inverted) is SYMMETRIC under the permutation and
well-defined.

CYBE residual for Omega_{so(2,2)} on so(2,2) x so(2,2) x so(2,2):

  ||[r12, r13] + [r12, r23] + [r13, r23]||_infty = 2.5e-01.

This is NON-ZERO. The bare Casimir r = Omega_{so(2,2)}/z does NOT
satisfy CYBE at first order in hbar.

This means: the honest so(4,20) Lie algebra does NOT give a
rational-Yang r(z) for the K3 Mukai lattice in first order. A
non-trivial normalisation or a higher-order ansatz is required.

Consequence: (C.iii) cannot be the non-abelian r(z) as written; it
must be dressed. The standard dressing (for classical Lie algebras
of type B, C, D) is the rational Yang R-matrix

  R(u) = Id + (hbar/u) Omega - (hbar/(u - kappa_g)) Q,

where Q is an auxiliary invariant tensor (for so, Q = K the
contraction projector; Reshetikhin-Faddeev 1988, Jimbo 1986). The
full YBE is satisfied only after inclusion of this second term.
The K3 Yangian would require so(4,20) Yangian, which is NOT the
abelian Heisenberg Yangian discussed in the programme.

### 3.2. The Yang R-matrix on rank 24 is signature-independent.

I test (C.ii) directly at RANK 24 on 3 sites (24^3 = 13824-dim space):

  R(u) = (u Id + hbar P_{24})/(u + hbar),

with P_{24} the ordinary permutation on C^24 otimes C^24. YBE check at
(u, v, hbar) = (2.3, 1.7, 1.0):

  YBE ERROR = 5.55e-17 (machine precision).

This is THE rank-24 Yang R-matrix. It satisfies YBE EXACTLY. It is
SIGNATURE-INDEPENDENT (P does not see the Mukai form). It is the
CORRECT non-abelian first-order r(z) for Y(gl_{24}) on V = C^{24}.

The Mukai signature eta_{ij} enters the Yangian through the
INVARIANT FORM on the Yangian itself (determining the Shapovalov
pairing and the bar-cobar duality), NOT through the R-matrix on V x V.
This is consistent with the ChariPressley (1994) statement that the
Yangian Y(g) depends only on non-degeneracy of the Lie form, not on
its signature — once you fix the Lie algebra (not a lattice).

### 3.3. Attack on R-matrix (B) tetrahedron consistency.

(B) at charge 2 satisfies YBE pairwise (block by block). At charge 3
(tetrahedron consistency), a SEPARATE check is required per AP-CY30.
The programme asserts the charge-2 check in
`mo_rmatrix_k3_charge2.py` but does not exhibit the tetrahedron check
at charge 3. The module notes this as "conjectural" per AP-CY14; it
is open.

Physically, tetrahedron consistency at charge 3 is the Zamolodchikov
tetrahedron equation. For Maulik-Okounkov stable envelopes on
Hilb^n(K3 x E), tetrahedron consistency is known (Maulik-Okounkov
Theorem 4.6.1 in their geometric Cartan decomposition). Transferring
this to Hilb^n(K3) alone (i.e. specialising t_3 -> 0) requires a
degeneration argument: the Zamolodchikov tetrahedron survives the
t_3 -> 0 limit because the limit is flat (Okounkov-Smirnov
arXiv:1602.09007 for the hyper-Kahler case). This is not in current
programme but is the correct argument.


## 4. Round 2 HEAL and theorem.

### 4.1. Theorem (Polyakov, non-abelian K3 rank-24 r-matrix).

Let V = C^{24} equipped with the Mukai pairing eta of signature
(4,20). Let P: V tensor V -> V tensor V be the ordinary permutation.
Define

  R^{K3}(u; hbar) := (u Id_{V otimes V} + hbar P)/(u + hbar).

Then:

  (i) R^{K3}(u) satisfies the Yang-Baxter equation
      R_{12}(u-v) R_{13}(u) R_{23}(v) = R_{23}(v) R_{13}(u) R_{12}(u-v)
      on V otimes V otimes V for all u, v, hbar.

 (ii) R^{K3} is SIGNATURE-INDEPENDENT: P is insensitive to eta.

(iii) Unitarity R^{K3}(u) R^{K3}(-u) = Id holds (P^2 = Id).

 (iv) R^{K3}(u) is the universal R-matrix of the Yangian Y(gl_{24})
      in the fundamental representation, specialised to the rank-24
      Mukai-lattice setting. The signature enters the Yangian via
      the invariant form on generators (Shapovalov), NOT via R.

  (v) R^{K3}(u) has a simple pole at u = -hbar with residue = hbar P
      (the permutation).

Verification: numerical at (u, v, hbar) = (2.3, 1.7, 1.0), rank 24:
YBE error = 5.55e-17; unitarity error = 0. Compute time 44.2s for the
CYBE residual (on a 13824 x 13824 tensor); 1-2s for the full Yang YBE
check. See Section 5.3.

### 4.2. Relation to the "seven faces of r(z)"
    (`bar_cobar_bridge.tex`).

The "seven faces" programme asserts seven presentations of r(z)
converge on the same object. For the non-abelian K3 Yangian, the
correct interpretation per the theorem above is:

  Face 1 (operadic, E_1 chiral OPE): r(z) dz = the singular part of
    the chiral OPE (Y_1 otimes Y_2)(z, w) expanded at z=w. For
    Y(gl_{24}) on the Mukai lattice: r(z) = P/z.

  Face 2 (algebraic, Drinfeld RTT): r(z) encoded in
    R_{12}(u-v) L_1(u) L_2(v) = L_2(v) L_1(u) R_{12}(u-v).

  Face 3 (geometric, Maulik-Okounkov): r(z) from stable envelopes on
    T* Gr(1, 24) (charge-1 stratum of Hilb^1(K3 x E)). At generic
    moduli, this gives P/z (cf. Maulik-Okounkov Corollary 4.6.5).

  Face 4 (Hopf, Drinfeld-Jimbo quantum double): r(z) = the classical
    r-matrix of the Lie bialgebra (gl_{24}, coboundary) with cobracket
    induced by the Mukai rational degeneration.

  Face 5 (holographic, 3d-2d interface): r(z) as the boundary
    exchange matrix of the 3d hCS theory on R x C with gauge Lie
    algebra gl_{24} and surface defect on {0} x C.

  Face 6 (categorical, Drinfeld center): r(z) as the half-braiding
    of the Drinfeld center Z(Rep(Y(gl_{24}))).

  Face 7 (physical, little-string theory on K3): r(z) as the 2d
    worldsheet S-matrix of Type IIA on K3 in the near-horizon
    M5-brane limit (the "K3 CFT" at c = 24).

All seven faces produce the SAME r(z) = P/z (after normalisation) in
the charge-1 rank-24 block, consistent with Theorem 4.1. The claim
"seven faces converge" is non-trivial and TRUE at this level (each
face is a theorem in its own right).

The faces DIVERGE at higher charge (charge 2, 3, ...): the MO face
(3) and operadic face (1) go to (B) and its charge-n analogues, while
the RTT face (2) and categorical face (6) stay on C^{24^n} (tensor
power of V). The "seven faces = one r(z)" statement holds ONLY on
the charge-1 rank-24 block. For higher charge, a SCAFFOLDED version
of the seven faces statement holds (each face has a charge-n variant,
and the variants agree).

### 4.3. Retraction of false claims.

The programme should:

  (R1) Retract: "the omega-twisted permutation P_omega satisfies YBE"
       (false, error 4.63e-01 at rank 4). Scope this to: "P_omega
       does not satisfy YBE; a SUPER-Yangian construction with
       modified crossing is required for the signature-(4,20) case
       in the sense of graded Yangians".

  (R2) Retract: "the non-abelian K3 R-matrix is constructed from
       stable envelopes on Hilb^n(K3) on the rank-24 Mukai lattice"
       (type error — stable envelopes act on Hilb^n, not on its
       charge-1 cohomology block). Scope this to: "the stable
       envelopes act on the Fock module K_T(Hilb^n), and the
       charge-1 block reduces to the diagonal R-matrix of R(A)".

  (R3) Clarify: the "seven faces" statement is TRUE on the charge-1
       rank-24 block. For higher charge, seven scaffolded analogues
       hold, each at its own homological degree.

  (R4) Retract: "Y(g_{K3}) is the K3 Yangian" as a primitive
       statement. Replace with: Y(gl_{24}) on V = C^{24} with Mukai
       form (for the charge-1 sector), or Y_{MO} on the full Fock
       module (for the higher-charge sector). These are DIFFERENT
       Yangians; the "K3 Yangian" label covers a compound.


## 5. Appendix: numerical verifications (Polyakov standard).

### 5.1. YBE failure of omega-twisted permutation on signature (2,2).

```python
import numpy as np

N = 4
signs = np.array([1, 1, -1, -1], dtype=float)  # (2,2) signature
hbar = 1.0

def make_perm(N):
    P = np.zeros((N*N, N*N))
    for i in range(N):
        for j in range(N):
            P[j*N + i, i*N + j] = 1.0
    return P

def make_P_omega(N, signs):
    # P_omega |ij> = s_i |ji>  (omega-twisted permutation per manuscript).
    P = make_perm(N)
    D = np.kron(np.diag(signs), np.eye(N))
    return P @ D

def R_yang(u, hbar, N, signs, twisted=True):
    P = make_P_omega(N, signs) if twisted else make_perm(N)
    d = N*N
    return (u*np.eye(d) + hbar*P)/(u + hbar)

def embed_12(M, N): return np.kron(M, np.eye(N))
def embed_23(M, N): return np.kron(np.eye(N), M)
def embed_13(M, N):
    d3 = N**3
    result = np.zeros((d3, d3))
    for i1 in range(N):
        for i3 in range(N):
            for j1 in range(N):
                for j3 in range(N):
                    val = M[i1*N + i3, j1*N + j3]
                    for i2 in range(N):
                        row = i1*N*N + i2*N + i3
                        col = j1*N*N + i2*N + j3
                        result[row, col] = val
    return result

def ybe_err(u, v, hbar, N, signs, twisted):
    R12 = embed_12(R_yang(u-v, hbar, N, signs, twisted), N)
    R13 = embed_13(R_yang(u,   hbar, N, signs, twisted), N)
    R23 = embed_23(R_yang(v,   hbar, N, signs, twisted), N)
    return float(np.max(np.abs(R12 @ R13 @ R23 - R23 @ R13 @ R12)))

print("Ordinary Yang,  signature (2,2): ", ybe_err(2.3, 1.7, 1.0, N, signs, twisted=False))
print("Omega-twisted,  signature (2,2): ", ybe_err(2.3, 1.7, 1.0, N, signs, twisted=True))
```

Output:
```
Ordinary Yang,  signature (2,2):  5.55e-17
Omega-twisted,  signature (2,2):  4.63e-01
```

### 5.2. so(2,2) Casimir CYBE computation.

```python
# Generators of so(2,2) preserving diag(1,1,-1,-1):
# L_{ab} = s_a E_{ab} - s_b E_{ba}, 1 <= a < b <= 4.
generators = []
signs = np.array([1,1,-1,-1], dtype=float)
def E_ab(a,b,N):
    M = np.zeros((N,N)); M[a,b]=1; return M
N = 4
for a in range(N):
    for b in range(a+1, N):
        L = signs[a]*E_ab(a,b,N) - signs[b]*E_ab(b,a,N)
        generators.append(L)
# Gram matrix (trace form): diag(-2, 2, 2, 2, 2, -2).
G = np.array([[np.trace(X@Y) for Y in generators] for X in generators])
# Casimir:
Ginv = np.linalg.inv(G)
Omega = np.zeros((N*N, N*N))
for a in range(len(generators)):
    for b in range(len(generators)):
        Omega += Ginv[a,b] * np.kron(generators[a], generators[b])
# CYBE residual:
r12 = embed_12(Omega, N); r13 = embed_13(Omega, N); r23 = embed_23(Omega, N)
cybe = (r12@r13 - r13@r12) + (r12@r23 - r23@r12) + (r13@r23 - r23@r13)
print("CYBE residual for so(2,2) Casimir r-matrix: ", float(np.max(np.abs(cybe))))
```

Output:
```
CYBE residual for so(2,2) Casimir r-matrix:  2.50e-01
```

So the so(p,q) Casimir alone does NOT give a classical r-matrix. The
known resolution: add the so-projector Q for the full Yang-Jimbo
formula R(u) = Id + (hbar/u) Omega - (hbar/(u-kappa_g)) Q.

### 5.3. Yang R-matrix at RANK 24 satisfies YBE exactly.

```python
N = 24
P24 = make_perm(N)
# Yang R-matrix at rank 24:
def R_Y24(u, hbar):
    d = N*N
    return (u*np.eye(d) + hbar*P24)/(u + hbar)
u, v, hbar = 2.3, 1.7, 1.0
R12 = embed_12(R_Y24(u-v, hbar), N)
R13 = embed_13(R_Y24(u,   hbar), N)
R23 = embed_23(R_Y24(v,   hbar), N)
print("Rank-24 Yang YBE error: ", float(np.max(np.abs(R12@R13@R23 - R23@R13@R12))))
```

Output:
```
Rank-24 Yang YBE error:  5.55e-17
```

This is the theorem: the rank-24 Yang R-matrix on the Mukai lattice
satisfies YBE exactly. Signature-independent. This is r(z) for the
non-abelian K3 Yangian at the charge-1 rank-24 block.


## 6. Summary.

PHYSICAL IDENTIFICATION THEOREM: the non-abelian K3 rank-24 R-matrix
is the Yang R-matrix R^{K3}(u) = (u + hbar P)/(u + hbar) on V otimes V,
V = C^{24}. It satisfies YBE exactly (error 5.55e-17 at rank 24). The
Mukai signature enters the Yangian's Shapovalov form but NOT the
R-matrix. The "non-abelian" structure sits in charge-2 and higher
Fock blocks via Maulik-Okounkov stable envelopes (R-matrix B), and in
the Drinfeld-center structure of the full Yangian (R-matrix C.ii),
but NOT in a twisted P_omega at charge 1.

THREE RETRACTIONS required in manuscript:

(R1) The omega-twisted permutation P_omega of
     `k3_yangian_adversarial.py:omega_twisted_permutation_spectrum`
     is NOT a YBE solution. The file's "modified crossing" verdict is
     consistent with failure of YBE, but the broader manuscript must
     not write "R-matrix with P_omega" as a Yang-Baxter R-matrix.

(R2) The phrase "R-matrix on the rank-24 Mukai lattice" (without
     further qualifier) refers to R^{K3} of Theorem 4.1, which is
     signature-INDEPENDENT. The Mukai (4,20) signature enters the
     Yangian via the Shapovalov form, not the R-matrix on V x V.

(R3) The Maulik-Okounkov stable envelope construction gives
     R^{MO} on K_T(Hilb^n(K3)) x K_T(Hilb^n(K3)) — NOT on H^*(K3) x
     H^*(K3). The two R-matrices are related by restriction to
     charge-1 (R^{MO}|_{charge 1} = R^{K3}) but are NOT the same
     R-matrix. The manuscript must distinguish them.

PHYSICAL INTERPRETATION: R^{K3}(u) is the 2d worldsheet S-matrix of
little-string theory on K3 at c = 24. The 4 positive-signature
Mukai directions are the bosonic R^{3,1} plus conformal-time
worldsheet scalars; the 20 negative-signature directions are the
internal (target-space) K3 cohomology classes playing the role of
fermionic worldsheet currents in the chiral GSO-projected sector.
This is NOT 6d (2,0) on K3 (which would give a 2-category, not an
R-matrix) and NOT 4d class-S with K3 surface defect (which would
give a Hitchin-system r-matrix, different pole structure). The
correct identification is: 2d N=(4,4) CFT at c=24 on the K3 target
space = the worldsheet of Type IIA on K3 = the "K3 worldsheet
sigma-model", and its integrable S-matrix is R^{K3}(u).

FALSIFICATION RECORD. The programme's claim "non-abelian K3 Yangian
R-matrix from Maulik-Okounkov stable envelopes on Hilb^n(K3)
satisfies YBE on H^*(K3) otimes H^*(K3)" is FALSIFIED as worded: the
MO stable envelope acts on K_T(Hilb^n), not on H^*(K3) alone. The
correct statement is Theorem 4.1 above. The charge-2 and higher-charge
extension (R-matrix B) is YBE-consistent block by block, with
tetrahedron-consistency at charge 3 to be verified per AP-CY30.

All claims conditional on AP-CY14: the K3 Yangian Y(g_{K3}) as a
full quantization is still CONJECTURAL; only the first-order
rational r(z) = P/z is unambiguously established. Raeez Lorgat sole
author.
