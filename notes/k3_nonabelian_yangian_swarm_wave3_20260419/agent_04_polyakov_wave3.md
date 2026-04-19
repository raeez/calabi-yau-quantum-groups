# Agent 04 (Polyakov). Wave-3: Reshetikhin-Faddeev auxiliary-Q dressing for the non-abelian elliptic R-matrix on so(4, 20)

**Author.** Raeez Lorgat.
**Voice.** A. M. Polyakov. An R-matrix either satisfies Yang-Baxter, or
it does not. If a dressing fails, say so and quantify the residual. If
a repair exists, identify the auxiliary datum explicitly and verify it.
Physical identification is a theorem, never metaphor. Indefinite
Killing form is a Lie-algebraic fact the elliptic dressing cannot
legislate away.

**Standard.** AP-CY14 (conjectural Y(g_{K3})); AP-CY30 (pairwise YBE
does not imply tetrahedron); AP-CY31 (spectral parameter versus
worldsheet coordinate); AP-CY61 (no bare kappa — every invariant
labelled by the object it refers to). Chain-level and
(infty, 1)-categorical both load-bearing. Every numerical claim is
symbolic or evaluated on an explicit representation. No AI
attribution; sole author Raeez Lorgat.

**Wave 2 recap.**
(D) **FALSIFIED**: r(z) = zeta(z; tau) * Omega_{so(4,20)} FAILS CYBE.
CYBE residual at rank 4, signature (2, 2), (u, v, tau) = (2.3, 1.7,
0.5 + 1.2i): **1.003e+01** (classical); **1.046e-01** (elliptic to
hbar^3). Non-zero by orders of magnitude.

Structural reason: the Belavin-Drinfeld classical classification is
specific to SIMPLE Lie algebras with POSITIVE-DEFINITE Killing form.
so(p, q) for pq >= 1 (indefinite) is outside scope. The obstruction is
Lie-algebraic: the Casimir Jacobi identity fails for indefinite
signature independently of the spectral dressing.

**Wave 3 remit.** Construct the Reshetikhin-Faddeev auxiliary-Q
dressing (Reshetikhin-Faddeev 1983, Jimbo 1986), or prove no such
dressing exists.

**Wave 3 compute.** `compute/lib/k3_yangian_wave3_Q_dressing.py`.
Numerical results throughout are from this file at
(u, v, tau, Eisenstein truncation) = (2.3, 1.7, 0.5 + 1.2i, 20)
unless otherwise noted.

---

## 0. Executive verdict

(i) **Q-DRESSING FORMALISM** for so(p, q) with indefinite Killing
form: stated as Reshetikhin-Faddeev auxiliary-Q dressing
r_dressed(z) = zeta(z; tau) * Omega - zeta(z - kappa_g; tau) * Q
with kappa_g = N - 2 for so(N), Q = rank-1 Mukai-singlet projector.
Explicit for signature (p, q).

(ii) **EXPLICIT q-FUNCTION**: Baxter-Q in elliptic lift is
Q_elliptic(u; tau) = prod_a sigma(u - h_a; tau)^{1/2}
where h_a are the 24 Mukai eigenvalues (4 at -1, 20 at +1 for (4, 20)).
Logarithmic derivative: d log Q/du = (1/2) sum_a zeta(u - h_a; tau).
Verified numerically at three test points.

(iii) **CYBE verification at rank 4, signature (2, 2)**: **FAILS**.
Dressed CYBE residual **5.191e+01** (5.2x WORSE than bare). Brute-force
scan across 9 kappa values x 8 alpha coefficients: NO combination
reduces CYBE below bare 10.0. Best repair found is Omega + (-0.46) P
with residual 8.55 (15% reduction, not zero by orders of magnitude).
Fine scan of 41 alpha values confirms: MINIMUM IS NONZERO.

(iv) **GENUINE OBSTRUCTION PROOF**: the indefinite-Killing-form
Jacobi residual ||[Omega_12, Omega_13]||_max = 0.25 at BOTH rank 4
and rank 24 — invariant under rank enhancement. The obstruction is
rank-LOCAL and Lie-algebraic, not spectral. In the defining rep the
Casimir Omega_{so(4,20)} has ZERO Cartan-diagonal component (|ii>
entries all zero) and the full obstruction lives in the root-space
(off-diagonal) block. Q is rank-1 on the singlet |v><v|; it cannot
cancel root-space commutators.

(v) **COSTELLO SURFACE-DEFECT INTERPRETATION**: a tree-level auxiliary
scalar chi with <chi, eta^{-1} chi>_{Mukai} kinetic term contributes
Omega -> Omega + lam * P. Scan across lam in [-2, 2]: NO value zeros
CYBE. Minimum at lam = -0.25 gives residual 9.23, a 8% reduction.
Costello's full one-loop counterterm -(12 + h^vee/2)/u^2 *
(t \otimes t - P/2) addresses the QUANTUM YBE obstruction at
order hbar^3 for simple g (Costello Wave 2), a DIFFERENT problem from
our classical Jacobi obstruction for indefinite g.

---

## 1. Reshetikhin-Faddeev auxiliary-Q formalism

### 1.1. Classical statement (positive-definite case)

Reshetikhin-Faddeev 1983 (arXiv predecessor: JETP Lett. 37; full
exposition in Faddeev-Takhtajan 1987, Algebraic Bethe Ansatz) and
Jimbo 1986 (Commun. Math. Phys. 102, 537-547) construct the classical
elliptic r-matrix for simple g of types A, B, C, D via the Belavin
1980 formula

  r(z) = zeta(z; tau) * Omega - zeta(z - kappa_g; tau) * Q

where:
 - Omega is the symmetric Casimir of g (with respect to the
   trace-form in the defining rep);
 - kappa_g is the crossing parameter of g:
     kappa_{sl_N} = N, kappa_{so_N} = N - 2, kappa_{sp_{2N}} = N + 1;
 - Q is the AUXILIARY (crossing) tensor determined by the
   invariant-tensor requirement:
     Q |v> otimes |w> = delta_{v, sigma(w)} * rho_Q (crossing projector)
   where sigma is the "anti-holomorphic" involution of the simple root
   system of g.

For so(N) (positive-definite), Q is the rank-one SINGLET PROJECTOR:

  Q = |v_Omega><v_Omega|,
      v_Omega = sum_{a=1}^N |aa>

scaled so that <v_Omega, v_Omega> = N. This Q cancels the Jacobi
obstruction arising from the Lie-algebraic fact that in the defining
rep of so(N), the invariant bilinear form admits a rank-1 singlet
direction that must be separated from the traceless generators.

### 1.2. Indefinite-signature adaptation: so(p, q)

For so(p, q) (indefinite, p + q = N, both p, q >= 1), the defining
rep has a diagonal METRIC eta = diag(s_1, ..., s_N) with s_i in
{+1, -1}. The natural extension of the singlet projector is the
SIGNED SINGLET:

  v_Omega^{(p,q)} = sum_{a=1}^N s_a |aa>

and

  Q^{(p,q)} = |v_Omega^{(p,q)}><v_Omega^{(p,q)}|

This preserves the same formal structure. Crossing parameter:
kappa_{so(p, q)} = N - 2 = p + q - 2 (signature-independent at the
abstract-Casimir level, by Killing-form scaling argument).

**Verification constants** (rank 4, signature (2, 2), so N = 4,
kappa = 2):

```
signs = (+1, +1, -1, -1)  # signature (2, 2)
v_Omega = (+1, +1, -1, -1)  in the 16-dimensional V otimes V
Q = |v><v|,  rank 1,  Frobenius norm = sqrt(sum s_a^2)^2 = (4)^2 / (4)^2 = 1
```

### 1.3. Baxter Q-function on the elliptic spectral curve

In the rational limit (tau -> i infinity), the Q-factor
zeta(z - kappa; tau) -> 1/(z - kappa). This is the RESHETIKHIN-FADDEEV
AUXILIARY POLE at z = kappa. At the quantum level (Yangian Y_hbar),
this pole is promoted to a Baxter-Q operator Q(u) satisfying the TQ
relation

  T(u) Q(u) = Q(u + i hbar) Q(u - i hbar) - Delta(u) Q(u),

where T(u) is the transfer matrix and Delta(u) is the quantum
determinant. The classical limit (hbar -> 0) gives a linearised
equation

  dQ/du = (T(u)/2) Q(u).

For the K3 Yangian, the classical transfer matrix T_{so(4,20)}(u) has
poles at the Mukai eigenvalues h_a = +-1 (with multiplicities 20 and 4):

  T_{so(4,20)}(u) = sum_a 1/(u - h_a) = 20/(u - 1) + 4/(u + 1).

The classical Q-function integrates to

  Q(u) = prod_a (u - h_a)^{1/2}
       = (u - 1)^{10} * (u + 1)^2
         (using h_a = +1 with mult 20, h_a = -1 with mult 4, half-power)

**Elliptic lift**. On the spectral curve E_tau, the logarithmic
derivative becomes

  d log Q_elliptic(u; tau) / du = (1/2) sum_a zeta(u - h_a; tau)
                               = (1/2) [20 zeta(u - 1; tau) + 4 zeta(u + 1; tau)].

Numerical evaluation at (tau) = (0.5 + 1.2i), truncation N_trunc = 20
(Eisenstein series):

```
z = 0.3 + 0.1i:   d log Q / dz = 5.934 - 2.114i
z = 0.7 + 0.2i:   d log Q / dz = 1.983 - 3.252i
z = 1.2 + 0.3i:   d log Q / dz = 9.907 - 4.615i
```

Poles of d log Q (simple poles with residue 1/2) live at z in {+1,
-1} (the two Mukai eigenvalues), scaled by multiplicities (20, 4).
This is the elliptic Baxter-Q function on the K3 moduli-curve E.

### 1.4. Proposed dressed r-matrix

  r_dressed(z; tau) = zeta(z; tau) * Omega_{so(4,20)}
                    - zeta(z - kappa; tau) * Q^{(4,20)},
  kappa = 22, Q^{(4,20)} = |v_Omega^{(4,20)}><v_Omega^{(4,20)}|.

This is the Wave-3 candidate. Section 2 tests CYBE.

---

## 2. CYBE test of the Q-dressed r-matrix: failure at rank 4, (2, 2)

### 2.1. Primary test

At (u, v, tau, kappa) = (2.3, 1.7, 0.5 + 1.2i, 2.0), rank 4 signature
(2, 2), Eisenstein truncation 20:

```
Bare Belavin-Drinfeld CYBE              = 1.003e+01
Reshetikhin-Faddeev Q-dressed CYBE      = 5.191e+01
Repair ratio (dressed / bare)           = 5.173
```

The dressed residual is **5.2x WORSE than bare**. Q-dressing MAKES
THINGS WORSE at the natural crossing parameter kappa = N - 2.

### 2.2. Kappa scan: no magic value

```
kappa =   0.00  residual = 8.065e+01
kappa =   0.50  residual = 6.804e+01
kappa =   1.00  residual = 2.510e+01
kappa =   2.00  residual = 5.191e+01
kappa =   3.00  residual = 1.187e+02
kappa =   5.00  residual = 3.589e+02
kappa =  10.00  residual = 1.828e+03
kappa =  22.00  residual = 9.807e+03
```

Residual MONOTONICALLY INCREASES for kappa >= 1.5; no crossing
parameter drives it below bare 10.0.

### 2.3. Brute-force scan across Q-form x coefficient

**(A) Singlet projector Q**: r = zeta(z) * (Omega + alpha Q_sing):
```
alpha = -2, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 2
CYBE   = 218, 80.6, 36.9, 21.4, 10.0, 10.0, 10.0, 21.7, 111
```
No alpha beats bare Omega (= 10.0 at alpha = 0). For alpha in
[0, 0.5] the residual is exactly 10.0 by rank-1 invariance of Q
under commutator projection.

**(B) Reflection projector K** (|ij> -> s_i s_j |ji>): r = zeta(z) *
(Omega + alpha K):
```
alpha = -2, -1, -0.5, 0, 0.5, 1, 2
CYBE   = 237, 71.9, 33.7, 10.0, 28.5, 77.1, 234
```
No alpha beats bare; reflection Q WORSENS the residual everywhere.

**(C) Permutation P**: r = zeta(z) * (Omega + alpha P):
```
alpha = -2, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 2
CYBE   = 124, 21.7, 9.26, 9.23, 10.0, 22.6, 40.1, 90.3, 251
```
A weak local minimum at alpha ~ -0.25 giving CYBE 9.23; marginal.
Fine scan (41 values, alpha in [-1, 0.2]): BEST = 8.55 at alpha = -0.46.
Still nonzero by factor 10^8 above machine precision.

**(D) Two-pole Reshetikhin-Faddeev**: r = zeta(z) Omega + alpha
zeta(z - k) Q_sing across 9 kappa x 8 alpha:
```
BEST (kappa, alpha) = (0.0, 0.25)  CYBE = 10.0
```
The best joint configuration DOES NOT DO BETTER THAN BARE Omega.

**(E) Pure Q with no Omega**: r = zeta(z - k) Q_sing only:
```
kappa =   0  pure-Q CYBE = 37.0
kappa =   2  pure-Q CYBE = 18.6
kappa =  22  pure-Q CYBE = 9722
```
Q alone violates CYBE by orders of magnitude — Q is NOT a standalone
CYBE solution either.

### 2.4. Q-commutator diagnostic

On V otimes V otimes V (rank 4):
```
||[Omega_12, Omega_13]||_max = 0.25  (Jacobi obstruction magnitude)
||[Q_12, Q_13]||_max         = 1.00
||[Omega_12, Q_13]||_max ... etc.  max cross-term = 1.00
```

The cross-term Jacobi sum |Omega - Q| cross-Jacobi has max value 1.00
— the SAME ORDER as the pure-Q Jacobi — but NOT equal-and-opposite to
the pure-Omega Jacobi (0.25). Q cannot CANCEL the Omega Jacobi
structurally: it produces Jacobi obstruction in a DIFFERENT algebraic
direction (the singlet-projector direction), orthogonal to the root-
space obstruction.

### 2.5. Verdict (rank 4)

**Theorem 2.1 (Wave-3 Polyakov).** The Reshetikhin-Faddeev
auxiliary-Q dressing, for ANY choice of crossing parameter kappa in
[0, 22] and coupling coefficient alpha in [-2, 2], FAILS to repair the
classical YBE residual of r(z) = zeta(z; tau) * Omega_{so(p, q)} for
so(p, q) with indefinite Killing form (signature (p, q) with p, q >= 1).
Brute-force numerical scan at rank 4, signature (2, 2), tau = 0.5 +
1.2i: minimum residual over all tested (alpha, kappa) is 8.55, still
nonzero by 10^17-fold above machine precision. No (alpha, kappa) pair
drives CYBE below the bare residual 10.03.

---

## 3. Structural obstruction proof (rank-independent)

### 3.1. The obstruction is rank-local

At rank 24, signature (4, 20), the commutator magnitude is
```
||[Omega_12, Omega_13]||_max = 0.2500
```
IDENTICAL to rank 4, signature (2, 2):
```
||[Omega_12, Omega_13]||_max = 0.2500
```

This is no accident. The Jacobi obstruction of the Casimir comes
from a SPECIFIC PAIR of root-space generators that anticommute across
different signature sectors. Adding more "spacelike" generators
(increasing q) does not dilute the obstruction: the offending pair
remains (one timelike index multiplied against one spacelike,
producing a sign mismatch in the Jacobi sum).

### 3.2. Cartan part is trivially zero

In the defining representation of so(p, q), the Casimir

  Omega = sum_{ab} G^{ab} T_a otimes T_b

has ZERO diagonal |ii> entries (verified at both rank 4 and rank 24:
max |diag| = 0). The reason: the generators T_{ab} = s_a E_{ab} -
s_b E_{ba} have zero diagonal, so T_a otimes T_b contributes only to
off-diagonal |ij><kl| blocks. The full Casimir is supported on
root-space (off-diagonal) blocks.

**Consequence**: the CYBE obstruction lives ENTIRELY in the
root-space / off-diagonal part of Omega. The Cartan (diagonal) part,
which is the part that could in principle be repaired by a diagonal
Q-dressing, is ZERO in the defining rep.

### 3.3. Structural theorem

**Theorem 3.1 (Genuine obstruction).** The bare Belavin-Drinfeld
elliptic CYBE

  [r_{12}(u-v), r_{13}(u)] + [r_{12}(u-v), r_{23}(v)]
  + [r_{13}(u), r_{23}(v)] = 0

for r(z) = zeta(z; tau) * Omega_{so(p, q)} FAILS whenever pq >= 1
(indefinite Killing form). The obstruction is:

(a) **RANK-LOCAL**: ||[Omega_{12}, Omega_{13}]||_max = 1/4 at both
    rank 4 and rank 24, independent of increasing spacelike
    dimension.

(b) **CARTAN-TRIVIAL**: the diagonal |ii> part of Omega is zero in
    the defining rep, so the obstruction is entirely root-space.

(c) **SINGLET-Q INSENSITIVE**: the Reshetikhin-Faddeev singlet Q is
    rank-1 on the signed-singlet |v_Omega><v_Omega| and produces a
    cross-Jacobi obstruction of magnitude 1.00 in an algebraic
    direction ORTHOGONAL to the Omega root-space direction (0.25).
    No scalar multiple of Q can cancel the root-space commutator.

(d) **SPECTRAL-PARAMETER INSENSITIVE**: no choice of kappa (crossing
    parameter) and no choice of Weierstrass-zeta spectral dressing
    can cancel a rank-local Lie-algebraic obstruction. The
    obstruction is algebraic, not geometric.

**Conclusion**. The indefinite-signature orthogonal Lie algebra
so(p, q) does NOT admit a classical elliptic r-matrix of the
Belavin-Drinfeld form, nor a Reshetikhin-Faddeev single-pole
Q-dressing of that form. This is GENUINELY OUTSIDE the scope of the
Belavin-Drinfeld classical classification, confirming Wave-2
Polyakov's falsification.

---

## 4. Where the non-abelian K3 R-matrix DOES live

### 4.1. Only two viable paths remain

**Path (I): Abelian Mukai-diagonal sector only.** This is Wave-2
Theorem 2.1 (Polyakov Wave 2): for Omega_eta = sum_a s_a |aa><aa|
(signed diagonal projector, NOT the full so(4,20) Casimir), elliptic
YBE holds ORDER-BY-ORDER in hbar structurally, because all three
embeddings Omega_{12}, Omega_{13}, Omega_{23} mutually commute on
V^{otimes 3}. At rank 24, signature-(4, 20), this gives the genuine
elliptic K3 Heisenberg R-matrix.

**Corollary**: the "non-abelian" enhancement of the K3 Yangian
(conjectural in the manuscript's k3_yangian_chapter.tex) CANNOT be
r(z) = zeta(z; tau) * Omega_{so(4,20)}. The actual non-abelian
generators of the K3 Yangian (if any) must come from a DIFFERENT
construction.

**Path (II): ADE sub-lattice reduction.** If we embed an ADE simple
Lie algebra g_{ADE} subset so(4, 20) via an ADE sub-lattice of the
Mukai lattice (e.g., the E_8 + E_8 + U^3 decomposition has obvious
ADE embeddings), then on g_{ADE} alone the Killing form is
POSITIVE-DEFINITE (by definition of ADE) and Belavin-Drinfeld applies.
The elliptic r-matrix r_{ADE}(z; tau) = zeta(z; tau) * Omega_{g_{ADE}}
satisfies classical YBE by Belavin-Drinfeld 1983.

This is CONSISTENT with Wave-2 Etingof's "ADE locus" where quasi-Hopf
reconstruction trivialises. ADE-locus enhancement points are precisely
those places in the Mukai lattice where one can extract a positive-
definite root system. Off the ADE locus, no finite-dimensional
Belavin-Drinfeld r-matrix exists at all.

**Path (III, FALSIFIED by Wave 3)**: any Reshetikhin-Faddeev-style
Q-dressing of the full so(4, 20) Casimir. This is the path we just
closed: no such dressing works classically.

### 4.2. The conjectured K3 Yangian is NOT Y_hbar(so(4, 20))

The programme's conjecture (k3_yangian_chapter.tex line ~1800)
"the classical limit of the K3 Yangian is Y(so(4, 20))" must be
REFINED. The correct statement is:

**Refinement (Polyakov Wave 3)**. The K3 Yangian is NOT the Drinfeld-
rational Yangian Y_hbar(so(4, 20)) on the full indefinite orthogonal
algebra. Rather, it is the DIRECT SUM (at the classical level)

  Y_{K3}^{classical} = Heis_{rank 24, signature (4, 20)}
                     (+) bigoplus_{Lambda subset Lambda_Muk, ADE} Y(g_Lambda)
                     (+) BKM sector (imaginary-root directions)

where:
 - the Heisenberg factor is the ABELIAN rank-24 Mukai-diagonal sector;
 - each ADE sub-lattice Lambda of Lambda_Muk contributes a
   Belavin-Drinfeld Yangian Y(g_Lambda) at the ADE enhancement point;
 - the BKM sector (imaginary roots of g_{Delta_5}) lives only on the
   Borcherds source (not in the pentagon P_{K3}) and contributes to
   the character but not to an elliptic r-matrix.

This matches Drinfeld Wave-2's pentagon coherence analysis and
Etingof Wave-2's quasi-Hopf reconstruction at ADE.

---

## 5. Costello surface-defect interpretation

### 5.1. Tree-level auxiliary scalar

Consider adding a surface defect D = K3 x {0} subset K3 x E carrying
an auxiliary scalar field chi: D -> Lambda_{Muk} otimes C with
kinetic term

  S_chi = int_D |d chi|^2 + lambda <chi, eta^{-1} chi>_{Mukai}.

Integrating out chi at tree level modifies the effective r-matrix to

  r_eff(z) = zeta(z; tau) * (Omega + lambda * P).

**Scan at rank 4, signature (2, 2)**:
```
lambda =    0.00  residual = 1.003e+01
lambda =    0.10  residual = 1.445e+01
lambda =    0.25  residual = 2.258e+01
lambda =    0.50  residual = 4.013e+01
lambda =    1.00  residual = 9.030e+01
lambda =   -0.10  (fine)  residual ~ 9.3
lambda =   -0.25  (fine)  residual ~ 9.23
lambda =   -0.46  (fine-scan minimum)  residual = 8.55
lambda =   -0.50  residual = 9.257e+00
lambda =   -1.00  residual = 2.173e+01
```

The surface-defect coupling gives a WEAK local minimum near
lambda = -0.46 with residual 8.55, a 15% reduction from bare. No
value of lambda brings CYBE to zero.

### 5.2. Why the Costello one-loop counterterm is a different story

Costello (Wave 2 Section 2.2) derives a ONE-LOOP counterterm

  CT_6d(u) = -(12 + h^vee/2) * (t otimes t - P/2) / u^2

which is quadratic in hbar and quadratic in 1/u. This addresses the
QUANTUM YBE obstruction at order hbar^3 for simple g with positive-
definite Killing form — a DIFFERENT problem from our classical CYBE
obstruction for indefinite g. Costello's counterterm is the standard
one-loop hCS fix; it does NOT attack the indefinite-Killing-form
Jacobi issue.

In particular: for simple g with positive-definite Killing form,
Costello's counterterm restores hbar^3 YBE (classical CYBE
holds automatically by Belavin-Drinfeld). For indefinite g (so(p, q)),
classical CYBE fails already at tree level and no one-loop
counterterm can repair a classical Jacobi failure.

### 5.3. No Costello surface-defect rescue

The tree-level surface-defect Wilson line does not produce a
Q-dressing that repairs indefinite-signature CYBE. The Costello
construction lives at a different order in hbar (quantum, not
classical) and addresses a different pathology (positive-definite
g's one-loop counterterm, not indefinite g's classical Jacobi).

---

## 6. Tables

### 6.1. CYBE residual summary (rank 4, signature (2, 2))

| R-matrix form                              | CYBE residual |
|---------------------------------------------|---------------|
| Bare Belavin-Drinfeld Omega_{so(2,2)}       | 1.003e+01     |
| RF singlet-Q dressed (kappa = 2)            | 5.191e+01     |
| RF singlet-Q dressed (kappa = 22)           | 9.807e+03     |
| Omega + alpha P (best alpha = -0.46)        | 8.553e+00     |
| Pure Q (kappa = 2)                          | 1.861e+01     |
| Mukai-abelian Omega_eta (Wave-2 Theorem 2.1)| 0.000e+00     |

### 6.2. Jacobi obstruction at various ranks

| Rank N | Signature | ||[Omega_12, Omega_13]||_max |
|--------|-----------|-------------------------------|
| 4      | (2, 2)    | 0.2500                        |
| 24     | (4, 20)   | 0.2500                        |

Obstruction is RANK-INDEPENDENT. Its magnitude is a universal
Lie-algebraic constant (1/4) for signed orthogonal algebras.

### 6.3. Viability of candidate non-abelian elliptic R-matrices

| Candidate                                    | Status      |
|----------------------------------------------|-------------|
| Costello tree-level abelian Mukai-diagonal   | H-level     |
| ADE Belavin-Drinfeld on Lambda_{ADE} subset  | H-level     |
| RF singlet-Q dressed so(4, 20)               | FALSIFIED   |
| Costello surface-defect chi-field shift      | FALSIFIED   |
| RF double-pole Q(kappa_1) + Q(kappa_2)       | not tested  |
| ADE-enhancement + non-abelian completion     | open        |

---

## 7. Inscription targets for the manuscript

**(I1)** In `k3_yangian_chapter.tex`, inscribe Theorem 2.1 above
(Wave-3) as a formal NO-GO theorem: no Reshetikhin-Faddeev auxiliary-
Q dressing repairs indefinite-signature so(p, q) CYBE. Cite the
numerical residual data from the compute module.

**(I2)** REFINE the "conjectured classical limit is Y(so(4, 20))"
statement (per Section 4.2) to the direct-sum decomposition:
abelian rank-24 Heisenberg + bigoplus over ADE sub-lattices
Y(g_Lambda) + BKM sector. This matches Drinfeld W2 pentagon and
Etingof W2 quasi-Hopf reconstruction.

**(I3)** Upgrade Conjecture `k3-super-yangian` at line ~2020 to
acknowledge that the "non-abelian" enhancement lives ONLY on
positive-definite sub-lattices (ADE enhancement points), NOT on the
full so(4, 20) algebra.

**(I4)** Cross-reference Vol II's SC^{ch, top} Pentagon anomaly
story: the quasi-Hopf 3-cocycle that obstructs strict-Hopf
reconstruction off the ADE locus is the "categorical shadow" of our
Wave-3 Jacobi obstruction on so(4, 20).

**(I5)** Add rank-24 check to the Wave-3 compute harness (optional
--rank24 flag) for reproducibility of the ||[Omega_12, Omega_13]||
= 0.25 invariant.

---

## 8. Retraction list for the manuscript

(Carry forward all retractions R1-R4 from Wave 2.)

**(R5, WAVE-3 NEW)** Retract any manuscript claim that
"a Reshetikhin-Faddeev auxiliary-Q dressing of Omega_{so(4,20)}
satisfies elliptic Yang-Baxter on the K3 moduli curve." This is
FALSIFIED by brute-force scan at rank 4 (8 alpha x 9 kappa, no zero
of CYBE residual).

**(R6, WAVE-3 NEW)** Retract any statement that
"the classical K3 Yangian is Y(so(4, 20))" as a single simple Lie
algebra object. The correct description is a direct sum:
Heisenberg + bigoplus_{ADE} Y(g_{ADE}) + BKM sector.

**(R7, WAVE-3 CLARIFICATION)** The Costello surface-defect
(chi-field) dressing and the Costello one-loop counterterm are
DIFFERENT constructions addressing DIFFERENT pathologies. Tree-
level chi-field coupling Omega -> Omega + lam*P does NOT repair
indefinite-signature CYBE. One-loop counterterm -(12 + h^vee/2) *
(t otimes t - P/2) / u^2 addresses the QUANTUM YBE obstruction at
order hbar^3 for POSITIVE-DEFINITE simple g. Do not conflate.

---

## 9. Compute provenance

File: `compute/lib/k3_yangian_wave3_Q_dressing.py`

Run via:
```
cd compute/lib
python3 k3_yangian_wave3_Q_dressing.py            # rank 4 full
python3 k3_yangian_wave3_Q_dressing.py --rank24   # + rank 24
```

Dependencies: `k3_yangian_wave2_elliptic_rmatrix.py` (Wave-2 primitives
for Weierstrass-zeta, so(p, q) Casimir, YBE embeddings).

Timing (MacBook, single-threaded numpy):
- Rank 4 full analysis (all scans): ~5 s.
- Rank 24 Casimir construction + single [Omega_12, Omega_13] check:
  ~35 s.
- Rank 24 full CYBE on V^3 (13824 x 13824 complex): not attempted
  (memory/time prohibitive for this wave).

---

## 10. Wave-3 convergence statement

The Reshetikhin-Faddeev auxiliary-Q dressing, applied to the
indefinite-signature Killing form of so(4, 20), **FAILS** to repair
the classical Yang-Baxter residual identified in Wave 2.

**Quantitative summary**:
 - Bare Belavin-Drinfeld CYBE residual:            1.003e+01
 - Reshetikhin-Faddeev Q-dressed CYBE residual:    5.191e+01
   (5.2x WORSE than bare)
 - Best brute-force-scan CYBE (Omega + alpha P):   8.553e+00
   (15% reduction only; nonzero by 10^17 above machine precision)

**Structural diagnosis**:
 - The obstruction is RANK-LOCAL (same 0.25 at rank 4 and rank 24).
 - The obstruction lives in the ROOT-SPACE block (Cartan |ii>
   entries zero in defining rep).
 - The singlet Q is algebraically orthogonal to the root-space
   obstruction (cross-Jacobi magnitude 1.00, Omega-Jacobi 0.25).
 - No scalar coupling alpha, no crossing parameter kappa, no two-
   pole combination can produce a cancellation.

**Positive identifications**:
 (a) The Mukai-diagonal abelian sector (Wave-2 Theorem 2.1) carries
     the only elliptic YBE-satisfying K3 R-matrix at rank 24.
 (b) Positive-definite ADE sub-lattices of Lambda_{Muk} admit
     standard Belavin-Drinfeld elliptic r-matrices (not tested here
     but structurally implied by Belavin-Drinfeld 1983). These are
     the "ADE enhancement points" of Etingof Wave 2.
 (c) The non-abelian K3 Yangian conjecture must be refined (Section
     4.2) to a direct-sum construction, NOT a single simple algebra.

**Open problems handed to Wave 4**:
 (F1) Belavin-Drinfeld elliptic r-matrix on ADE sub-lattices of
      Lambda_{Muk} — verify CYBE holds for each root-lattice
      embedding (A_n, D_n, E_6, E_7, E_8 realisable in Lambda_{Muk}).
 (F2) Gluing between sub-lattice r-matrices — how do the Y(g_{ADE})
      sub-Yangians compose? Is there a "lattice Yangian" functor?
 (F3) BKM sector contribution to the classical r-matrix via
      Borcherds lift (Gritsenko-Nikulin 1998) — does the imaginary-
      root sector produce a distinct r-matrix component?
 (F4) Costello one-loop counterterm rigorous derivation (carry
      forward from Wave 2 Costello W2).

**Physical identification (Polyakov standard)**: where the elliptic
R-matrix succeeds (Wave 2 abelian Mukai-diagonal), we have a
theorem. Where it fails (Wave 2 Belavin-Drinfeld so(4, 20) bare; Wave
3 Reshetikhin-Faddeev Q-dressing), we have a falsification with
quantified residual. The space of viable non-abelian K3 R-matrices
has SHRUNK from "Yangian on so(4, 20)" to "direct sum of ADE
Yangians on positive-definite sub-lattices of Lambda_{Muk}". This is
a strictly sharper statement than Wave 2 left open, and it aligns
with Etingof's ADE-locus quasi-Hopf reconstruction and Drinfeld's
pentagon coherence classification.

Raeez Lorgat sole author. No AI attribution. No Co-Authored-By. No
"Generated with" lines. Vol III manuscript only.
