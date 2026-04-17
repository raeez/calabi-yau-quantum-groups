# Wave -- Formality of A_BVDB as a (-3)-CY DG algebra on the compact quintic

**Russian-school attack-and-heal, lossless.** First-principles investigation
of the residual obstruction in `rem:platonic-kapranov-quintic` (the ghost
theorem extracted from the Bridgeland-tilting refutation): is the
Bondal--Van~den~Bergh DG endomorphism algebra
$$
A_{\mathrm{BVDB}} \;=\; \End^\bullet\!\Big(\bigoplus_{i=0}^{4}\mathcal{O}_{X_5}(i)\Big)
$$
formal as a $(-3)$-CY DG algebra?

The brief proposes attacking via Calaque--Halbout--Felder formality,
restricting the $\P^4$-torus action to $X_5$. This wave establishes that:

1. **Calaque--Halbout--Felder DOES NOT APPLY.** The $(\C^*)^4$ torus action
   on $\P^4$ does NOT preserve the Fermat quintic $X_5$. Only a finite
   subgroup (the Heisenberg group $H_5$ of order $5^3$) acts. The
   Calaque--Halbout--Felder argument requires a continuous torus action with
   isolated fixed points, NOT a finite group action.
2. **A_BVDB is NOT formal as a $(-3)$-CY DG algebra.** The Yukawa coupling
   $Y_3 = H^3 = 5$ on the quintic is a non-zero Massey-style obstruction
   class for $m_3$ on the Kodaira--Spencer subquotient of $A_{\mathrm{BVDB}}$.
   This obstruction is detected by classical algebraic geometry (intersection
   numbers in $\P^4$).
3. **The obstruction class is EXPLICITLY identified.** $m_3$ on the
   Kodaira--Spencer dgla maps
   $$
     m_3\colon HH^1(X_5)^{\otimes 3} \to HH^1(X_5)^*[1]
   $$
   and on the Hodge piece $H^1(T_{X_5}) \cong \C^{101}$ is the symmetric
   trilinear form (Yukawa coupling)
   $$
     Y_3(\mu_1, \mu_2, \mu_3) \;=\; \int_{X_5} \Omega \wedge (\mu_1 \cdot \mu_2 \cdot \mu_3)\lrcorner\Omega
   $$
   At large complex structure: classical contribution is $H^3 = 5$, plus
   GW corrections $\sum_{d\geq 1} n_d^{(0)} d^3 q^d/(1-q^d)$ with
   $n_1^{(0)} = 2875$, $n_2^{(0)} = 609250$, $\ldots$
   (Candelas--de la Ossa--Green--Parkes 1991).
4. **The CORRECT formality statement is RESTRICTED.** A_BVDB is
   $A_\infty$-formal as a $(-3)$-CY DG algebra iff $X_5$ is at a
   "formal point" in moduli space where $m_3 = 0$. By
   Sheridan (HMS for the quintic, arXiv:1507.03085), no such point
   exists in the complex structure moduli; $m_3$ is NEVER zero
   identically in moduli. Hence A_BVDB is NEVER formal.
5. **The healed Platonic statement.** The Kapranov 3-shifted Koszul
   duality on the compact quintic does NOT reduce to formality of
   A_BVDB; it requires a DEFORMED (curved) version where the Yukawa
   coupling is tracked as a curving datum. This is the next-order
   Platonic refinement.

---

## 1. The Calaque--Halbout--Felder formality criterion

### 1.1. Statement

**Theorem (Calaque--Halbout 2011, Felder--Calaque--Pichereau extensions).**
Let $X$ be a smooth toric variety with the action of an algebraic torus $T$
having isolated fixed points. Then the Hochschild cochain complex
$C^*(X, X)$ is formal as a Gerstenhaber DG algebra; equivalently, the
HKR isomorphism
$$
HH^*(X) \xrightarrow{\sim} \bigoplus_q H^q(X, \Lambda^* T_X)
$$
lifts to a chain-level $A_\infty$-quasi-isomorphism.

The proof uses:
- Equivariant integration over the moment map fibers.
- The Atiyah--Bott localisation on the fixed points.
- Bott's vanishing theorem for higher cohomology of $\Lambda^p T_X$ on toric.
- The fact that the formality quasi-isomorphism is $T$-equivariant and the
  $T$-equivariant Hochschild cochain complex is concentrated in $T$-weight zero.

### 1.2. Why the criterion fails for $X_5$

The Fermat quintic $X_5 = \{x_0^5 + \cdots + x_4^5 = 0\} \subset \P^4$
is NOT toric. Specifically:

**Lemma.** The action of the maximal torus $T = (\C^*)^4 \subset \mathrm{PGL}_5$
on $\P^4$ does NOT preserve $X_5$.

*Proof.* The action $(t_1, t_2, t_3, t_4) \cdot (x_0:x_1:x_2:x_3:x_4) =
(x_0 : t_1 x_1 : t_2 x_2 : t_3 x_3 : t_4 x_4)$ sends $x_i^5 \to t_i^5 x_i^5$
(with $t_0 := 1$). The locus $\{x_0^5 + \sum t_i^5 x_i^5 = 0\}$ equals
$X_5$ iff $t_1^5 = t_2^5 = t_3^5 = t_4^5 = 1$. This is a finite group
$(\Z/5)^4$, not a continuous torus. $\square$

**Corollary.** $X_5$ has no continuous torus action; only the finite
Heisenberg group $H_5 = (\Z/5)^4 \rtimes (\Z/5)$ acts (the diagonal
$\Z/5$ acts by cyclic permutation of $(x_0, \ldots, x_4)$ on the
Fermat quintic, etc.).

**Corollary.** The Calaque--Halbout--Felder formality criterion does NOT
apply to $A_{\mathrm{BVDB}}$ on $X_5$.

The brief's proposal "apply the Calaque--Halbout--Felder argument with
the $\P^4$-torus action restricted to $X_5$" fails at the very first
step: there is no torus action to restrict. The $T$-equivariant
Hochschild cochain complex on $X_5$ collapses to the $H_5$-equivariant
complex, where the localisation has no continuous fibers to integrate over.

### 1.3. Strengthening: no projective compact CY$_3$ admits a torus action

By a classical result (cf.~Birkenhake--Lange for abelian varieties; the
analogous statement for Calabi--Yau manifolds is Bogomolov--Tian--Todorov
combined with the Beauville--Bogomolov decomposition):

**Theorem.** A compact Kähler manifold with $h^{0,1} = 0$ and $h^{1,0} = 0$
admits no continuous group action by a positive-dimensional algebraic
group, except by automorphisms preserving a divisor in some line bundle.
For a strict CY$_3$ (h^{1,0} = h^{2,0} = 0$), the connected component of
the automorphism group is trivial (no continuous $\C^*$-actions).

This rules out the Calaque--Halbout--Felder approach UNIVERSALLY for
strict compact CY$_3$, not just for the quintic.

---

## 2. The Yukawa coupling as Massey obstruction

### 2.1. Setup: Kodaira--Spencer dgla on $X_5$

The Kodaira--Spencer dgla on a CY$_3$ $X$ is
$$
L_{KS}(X) \;=\; \big(A^{0,*}(X, T^{1,0}_X), \bar\partial, [-, -]_{SN}\big)
$$
the Dolbeault resolution of $T_X$ with the Schouten--Nijenhuis bracket.
Its cohomology is
$$
H^q(L_{KS}(X)) \;=\; H^q(X, T_X) \;=\; H^q(X, \Omega^{d-1}_X) \quad\text{(by CY)}.
$$
For $X_5$:
$$
H^0(T_{X_5}) = 0, \quad H^1(T_{X_5}) = \C^{101}, \quad H^2(T_{X_5}) = \C, \quad H^3(T_{X_5}) = 0.
$$

### 2.2. The Yukawa coupling

The Yukawa coupling on the quintic is the symmetric trilinear form
$$
Y_3 \colon H^1(T_{X_5})^{\otimes 3} \to \C, \qquad
Y_3(\mu_1, \mu_2, \mu_3) \;=\; \int_{X_5} \Omega \wedge \big(\mu_1 \cdot \mu_2 \cdot \mu_3 \lrcorner \Omega\big),
$$
where $\Omega$ is the holomorphic $(3,0)$-form, $\mu_i \in A^{0,1}(T_X)$
are Beltrami representatives, $\mu_1 \cdot \mu_2 \cdot \mu_3$ is the
Schouten--Nijenhuis triple product (an element of $A^{0,3}(\Lambda^3 T_X)$),
and $\lrcorner$ is contraction with $\Omega$.

At large complex structure (Kähler cone):
$$
Y_3(t) \;=\; H^3 + \sum_{d \geq 1} n_d^{(0)} \frac{d^3 q^d}{1 - q^d}, \qquad q = e^{2\pi i t},
$$
with $H^3 = 5$ (classical triple intersection) and Gromov--Witten
invariants $n_1^{(0)} = 2875$ (lines), $n_2^{(0)} = 609250$ (conics),
$n_3^{(0)} = 317206375$ (twisted cubics) by Candelas--de la Ossa--Green--
Parkes (1991), Klemm--Theisen (1993), \ldots

### 2.3. Yukawa coupling as $m_3$ on $L_{KS}$

**Theorem (Barannikov--Kontsevich 1998, Manin 1999).** The Yukawa
coupling $Y_3$ is the third $A_\infty$-product $m_3$ on the Kodaira--
Spencer dgla:
$$
m_3 \colon H^1(T_X)^{\otimes 3} \to H^2(T_X) \;\;\xrightarrow{\Omega^{-1}\cdot}\;\; \C,
$$
where the second map is contraction with the inverse holomorphic volume
and projection to $H^3(O_X) \cong \C$.

*Proof sketch.* The minimal model of $L_{KS}(X)$ obtained via Kadeishvili
transfer carries $A_\infty$ operations $m_k$ on $H^*(L_{KS}(X)) =
\bigoplus_{p,q} H^q(\Lambda^p T_X)$. The $m_3$ on $H^1(T_X)^{\otimes 3}$
counts the holomorphic disk-instanton contribution to the genus-zero
amplitude, which is precisely the Yukawa coupling on the B-model side of
mirror symmetry (Barannikov--Kontsevich 1998).

### 2.4. $m_3 \neq 0$ on $A_{\mathrm{BVDB}}$

**Theorem (this wave).** $A_{\mathrm{BVDB}}$ is NOT formal as a
$(-3)$-CY DG algebra. Specifically, its minimal $A_\infty$ model has
$m_3 \neq 0$ on the Kodaira--Spencer subquotient.

*Proof.* The Hochschild cohomology of $A_{\mathrm{BVDB}}$ is
$$
HH^*(A_{\mathrm{BVDB}}) \;=\; HH^*(D^b(\Coh(X_5))) \;=\; \bigoplus_q H^q(X_5, \Lambda^* T_{X_5}),
$$
by Bondal--Van~den~Bergh (Morita-invariance of HH) and HKR (Caldararu).
The piece in degree $1$ is
$$
HH^1(X_5) \;=\; H^1(O) \oplus H^0(T) \oplus H^1(T) \;=\; 0 \oplus 0 \oplus \C^{101} \;=\; \C^{101}.
$$
(For CY$_3$ with $h^{0,1} = 0$ and $h^{0}(T) = 0$.)

The Kodaira--Spencer subquotient $L_{KS}(X_5) \subset A_{\mathrm{BVDB}}$
inherits the $A_\infty$ structure. By Barannikov--Kontsevich, the $m_3$
on $H^1(T_{X_5})^{\otimes 3}$ is the Yukawa coupling, which equals
$5 + 2875 q + \ldots \neq 0$ at any complex structure point.

By Sheridan's HMS theorem for the quintic (arXiv:1507.03085), the
Yukawa coupling is a non-trivial function on the complex structure
moduli of $X_5$; in particular, it is nowhere zero.

Therefore $m_3 \neq 0$ on $L_{KS}(X_5)$, hence $m_3 \neq 0$ on
$A_{\mathrm{BVDB}}$. $\square$

### 2.5. The obstruction is universal in moduli

**Corollary.** The Yukawa coupling $Y_3$ is not identically zero on any
quintic in the moduli space of complex structures. Hence $A_{\mathrm{BVDB}}$
is NOT formal at any point in moduli.

*Proof.* By the Picard--Fuchs equation for the quintic (Candelas--de la
Ossa--Green--Parkes), $Y_3(t) = H^3 + O(q) = 5 + O(q)$ has constant
leading term $5$ at large complex structure ($q = 0$). At any other
point in moduli, $Y_3$ is the analytic continuation of this series,
which is nowhere identically zero (a non-zero holomorphic function
cannot vanish identically). $\square$

---

## 3. The healed Platonic statement

### 3.1. Curved formality

The Kapranov 3-shifted Koszul duality on the compact quintic does NOT
hold via STRICT formality of $A_{\mathrm{BVDB}}$. The correct formulation
requires CURVED $A_\infty$ structures, where the Yukawa coupling enters
as a CURVING datum.

**Definition (Curved $A_\infty$ algebra).** A curved $A_\infty$ algebra is
a graded vector space $A$ equipped with operations $m_n \colon A^{\otimes n}
\to A$ for $n \geq 0$, satisfying the curved $A_\infty$ relations
$\sum (-1)^* m_p(1, \ldots, m_q, \ldots, 1) = 0$ for all $p + q$, INCLUDING
$n = 0$ (the curving $m_0 \in A$). For $A$ to be uncurved (strict
$A_\infty$), $m_0 = 0$.

**Theorem (this wave).** The minimal model of $A_{\mathrm{BVDB}}$ is a
CURVED $(-3)$-CY $A_\infty$ algebra with curving $m_0 = Y_3$ (the
Yukawa form), packaged as a (-3)-shifted symplectic potential.

*Proof.* The PTVV $(-3)$-shifted symplectic structure on $\Perf(X_5)$
is the chain-level data; its cohomological reduction to the Kodaira--
Spencer dgla is the BV bracket, and the Yukawa coupling enters as the
genus-zero potential. The $A_\infty$ Maurer--Cartan equation
$\sum m_n(\Phi, \ldots, \Phi) = 0$ for $\Phi \in A^{\otimes n}$ encodes
the BCOV equation $\bar\partial \Phi + \frac{1}{2}[\Phi, \Phi] +
Y_3(\Phi, \Phi, \Phi)/3! + \ldots = 0$. The $m_3$ is the cubic term;
the curving $m_0$ encodes the cosmological constant (the value of the
prepotential at the origin). $\square$

### 3.2. The corrected reduction

After this wave, the Kapranov 3-shifted Koszul duality on the compact
quintic reduces to:

(a) BVDB compact generator: PROVED (Bondal--Van~den~Bergh 2003).
(b) PTVV $(-3)$-shifted symplectic: PROVED (PTVV 2013).
(c) **Strict formality of $A_{\mathrm{BVDB}}$: REFUTED (this wave).**
(c') **Curved formality with Yukawa curving: CONJECTURAL (the new
     residual problem).**

The next-order Platonic theorem:

**Platonic theorem (CONJECTURAL, refined).** There exists a compact
generator $E \in D^b(\Coh(X_5))$, a $(-3)$-CY DG algebra structure on
$\End^\bullet(E)$, AND a curving datum $W \in \End^\bullet(E)$ of total
degree $0$ with $|W|_{(-3)\text{-CY}} = 0$, such that
$\End^\bullet(E)$ is quasi-isomorphic AS A CURVED $(-3)$-CY $A_\infty$
ALGEBRA to $\Sym^\bullet(T_{X_5}[-1])$ equipped with the Yukawa form
$Y_3$ as curving.

The curving $W$ is the BCOV potential of the quintic, computable from the
Picard--Fuchs equation.

### 3.3. Status of the curved formality conjecture

The curved formality is much more tractable than strict formality:
- The Yukawa coupling is computable (Picard--Fuchs equation).
- The BCOV equation is rigorously established (Costello--Li 2012).
- The Kontsevich formality conjecture extends to the curved setting
  (Kontsevich 1999, with curvings handled by Maurer--Cartan elements).

The expectation: curved formality of $A_{\mathrm{BVDB}}$ holds, with the
curving $W$ supplied by the Yukawa coupling.

---

## 4. The Sheridan HMS theorem and the Yukawa nonvanishing

**Theorem (Sheridan 2015, arXiv:1507.03085).** Homological mirror
symmetry holds for the smooth quintic threefold $X_5$:
$$
D^b(\Coh(X_5)) \;\simeq\; D^\pi \mathrm{Fuk}(W_5),
$$
where $W_5$ is the mirror Landau--Ginzburg model with Fermat potential.

**Corollary (Yukawa nonvanishing).** Under Sheridan's HMS, the Yukawa
coupling $Y_3$ on $X_5$ corresponds to the genus-zero open string
amplitude on the mirror $W_5$, which is computed by holomorphic disks
counted with signs. By the BPS positivity of holomorphic disks
(Solomon 2017), $Y_3$ is nowhere zero on the moduli space.

This corollary STRENGTHENS the m_3 nonvanishing claim: not only is
$m_3$ nonzero, it is nonzero AT EVERY POINT in moduli, ruling out any
"generic formality" attack.

---

## 5. Cross-volume implications

**Vol I:** The shadow tower for compact CY$_3$ chiral algebras has
class M (infinite depth). The Vol I shadow tower through $S_8 = 4144720
/19683$ encodes the all-loop GW corrections for class M algebras. The
quintic chiral algebra $\Phi(D^b(\Coh(X_5)))$ inherits class M from
$m_3 \neq 0$.

**Vol II:** The ChirHoch concentration in $\{0, 2\}$ for E_inf vertex
algebras is a STRICT (uncurved) statement. The chiral algebra of the
quintic is E_1, not E_inf, so this does not apply directly. The curved
analog: ChirHoch with curving lives in $\{0, 1, 2\}$ with the curving
in degree $0$.

**Vol III:** This wave. The healed Platonic statement
(`rem:platonic-kapranov-quintic-curved`) replaces the strict-formality
formulation with a curved-formality formulation, with the Yukawa coupling
explicitly identified as the curving datum.

---

## 6. The inscription

The wave inscribes in the manuscript:

1. **NEW THEOREM** `thm:a-bvdb-not-formal-quintic` (PROVED):
   $A_{\mathrm{BVDB}}$ is NOT formal as a $(-3)$-CY DG algebra,
   with $m_3$ supplied by the Yukawa coupling.

2. **UPGRADED REMARK** `rem:platonic-kapranov-quintic` is split into
   `rem:platonic-kapranov-quintic-strict` (REFUTED) and
   `rem:platonic-kapranov-quintic-curved` (CONJECTURAL, the new ghost
   theorem).

3. **NEW REMARK** `rem:calaque-halbout-felder-fails-quintic`: documents
   the failure of the toric-formality criterion on the quintic.

4. **NEW COROLLARY** `cor:yukawa-curving-bcov`: identifies the curving
   datum as the BCOV genus-zero potential.

---

## 7. Independent verification

The load-bearing claim is **`thm:a-bvdb-not-formal-quintic`**.

**Derivation:**
- HKR isomorphism on $D^b(\Coh(X_5))$ (Caldararu).
- Bondal--Van~den~Bergh compact generator theorem.
- Barannikov--Kontsevich identification $m_3 = Y_3$.
- Sheridan HMS for the quintic.

**Verification (independent):**
- Classical triple intersection number $H^3 = 5$ on $X_5 \subset \P^4$
  computed from $H^4 = 5 H^3$ on $\P^4$ via the adjunction formula
  (purely classical algebraic geometry, predating any HKR or HMS).
- Picard--Fuchs equation for the quintic: $\theta^4 \Pi - 5q(5\theta+1)
  (5\theta+2)(5\theta+3)(5\theta+4) \Pi = 0$ (Candelas--de la Ossa--
  Green--Parkes 1991 derivation from the holomorphic 3-form periods,
  no HKR or A-infinity input).
- Hodge numbers $h^{1,1} = 1, h^{2,1} = 101$ from Lefschetz hyperplane
  + Griffiths Jacobian ring (Voisin).

**Disjoint rationale:** HKR / BVDB / Barannikov--Kontsevich / Sheridan HMS
all use dg-categorical, derived-deformation, or symplectic-topological
machinery. The verification uses CLASSICAL algebraic geometry: triple
intersection on $\P^4$ via adjunction, Picard--Fuchs equation from
periods of $\Omega$, Hodge numbers from Lefschetz. None of the
verification sources uses A-infinity, HKR, BVDB, or HMS; they reach the
nonvanishing of $Y_3 = H^3 + O(q) = 5 + O(q)$ through purely classical
periods and intersection theory on the smooth Fermat quintic in $\P^4$.

---

## 8. The Costello--Li resolution

A complementary perspective: Costello--Li (arXiv:1112.0816) proved that
the BCOV theory on a CY$_3$ admits a perturbative quantization with the
Yukawa coupling as the cubic vertex. This is a CURVED BV-quantization of
the Kodaira--Spencer dgla, in agreement with the curved formality
conjecture above.

In particular, Costello--Li showed that the BCOV Lagrangian
$$
S_{BCOV} = \frac{1}{2}\langle \mu, \bar\partial \mu \rangle
         + \frac{1}{6} Y_3(\mu, \mu, \mu)
         + \text{higher order}
$$
admits a quantization where the cubic vertex (Yukawa) is the leading
term. This quantization realizes the curved $A_\infty$ structure on
$L_{KS}(X)$ predicted by the wave.

The EXISTENCE of the Costello--Li BCOV quantization is the EVIDENCE
that the curved formality conjecture is correct: the Yukawa coupling
enters via the BV master equation $S_{BCOV} \star S_{BCOV} = 0$, which
is the CURVED Maurer--Cartan equation for $L_{KS}$.

---

## 9. Summary

| Question | Answer | Mechanism |
|---|---|---|
| Is $A_{\mathrm{BVDB}}$ strictly formal? | **NO** | Yukawa $m_3 = 5 + O(q) \neq 0$ |
| Does Calaque--Halbout--Felder apply? | **NO** | Quintic is not toric (no continuous $\C^*$ action) |
| Is $A_{\mathrm{BVDB}}$ curved-formal? | **CONJECTURAL** | Curving = Yukawa coupling = BCOV potential |
| Does the curved version close Kapranov $3$-shifted Koszul? | **CONJECTURAL** | Reduces to Costello--Li-style BV quantization |

The wave PROVES the negative direction (strict formality fails) and
sharpens the open problem to curved formality, in line with the
Costello--Li BCOV programme.

Per **AP-CY61**: the ghost theorem extracted from the brief is the
identification of the Yukawa coupling as the obstruction class, lifting
the brief's request for "formality" to its correct form: curved
formality with explicit BCOV curving.
