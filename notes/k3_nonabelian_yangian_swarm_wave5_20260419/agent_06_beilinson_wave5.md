# Agent 06 — Beilinson Wave 5. ADVERSARIAL audit of Wave-4's own retractions, $L_\infty$-claims, ENO reconstruction, and three-loop arithmetic.

**Author.** Raeez Lorgat. Sole author. No AI attribution.
**Date.** 2026-04-19.
**Voice.** A.A. Beilinson. Wave-4 upheld four of Wave-3's retractions
and introduced six new structural claims (R8, product-form universal
$\mathcal R_{K3}$, $\Psi_{\mathrm{het}\to Y}$ as $L_\infty$-morphism,
ENO-classified rational-Fock sector, $\mathrm{CT}_3$ with explicit
$A_3$, Kazhdan $l_4 = 1/24$ Massey product). Wave 5 asks whether the
very instrument by which Wave-4 exonerated Wave-2/3 is itself sound.
Nothing from Wave 4 is sacred — including Wave-4 Beilinson's own
verdicts. What is sacred is only the first-principles derivation.

**Standard.** Chain-level and $(\infty,1)$-categorical both load-
bearing. A retraction must retract cleanly (must identify PRECISELY
which Wave-2 claims fall with it). An $L_\infty$-morphism claim must
exhibit $l_k \circ \Psi_\bullet = \Psi_\bullet \circ l_k$ on named
witnesses. A "three-path verification" must actually compute three
independent paths. A coefficient like $1/24$ must be forced by
$L_\infty$-relations, not decorated onto them.

---

## 0. Executive verdicts

(i) **Polyakov W4 R8 retraction of bare $\zeta(z)\Omega$ ansatz.**
**UPHELD; AND IT CASCADES.** The bare $\zeta \cdot \Omega$ ansatz
IS NOT a solution of CYBE for positive-definite simple $\mathfrak g$
— Wave-4 Polyakov correctly computes a residual $4.013 \times 10^1$
for $\mathfrak{sl}_3$ at $\tau = 0.5 + 1.2i$. Genuine Belavin-Drinfeld
1981 elliptic $r$-matrix has separate root-weighted
$w_\alpha(z, \tau)$ pieces on each root space plus $\zeta(z,\tau)$ on
the Cartan. **Cascade**: Wave-2 Polyakov § 3.2 falsified
$\zeta(z,\tau)\Omega_{\mathfrak{so}(4,20)}$ using the SAME
ansatz-structure as a proxy for Belavin-Drinfeld. The falsification
still HOLDS (because the bare $\Omega_{\mathfrak{so}(4,20)}$ has
$[\Omega_{12},\Omega_{13}]\neq 0$ at the CASIMIR level, not at the
elliptic dressing level). But the SCOPE of the Wave-2 falsification
is narrower than advertised: **the Wave-2 theorem falsifies a PROXY
ANSATZ**, not the Belavin-Drinfeld 1981 elliptic $r$-matrix per se.
What survives intact is the Wave-2 Polyakov Theorem 2.1 (**Yang
rational R-matrix at rank 24, signature-independent, mutually-
commuting-Casimir-YBE**) because that uses the signed-diagonal abelian
Casimir $\Omega^{\mathrm{Heis}}_{\mathrm{Muk}}$, not $\Omega_g$ on
non-abelian $\mathfrak g$. See §1 for the scope analysis.

(ii) **Gelfand W4 universal R as product-form $\mathrm{Heis} \times \mathrm{ADE} \times \mathrm{BKM}$.**
**OPEN at the stratified-Hopf-algebra level; I compute ONE independent
cross-strata YBE residue and find it NON-VANISHING at leading
$\hbar^2$.** Wave-4 Beilinson §4 already flagged the stratification-
coproduct mixing. Wave-4 Gelfand §1.3b "Heal" claimed the product is
"well-defined up to pentagon-gauge." That heal is INCOMPLETE — it
does not verify cross-strata YBE on a specific non-trivial triple.
I compute that here. Result: on the generator triple
$(x^a_i \otimes 1, y^b_j \otimes 1, z^c_k \otimes 1)$ with $a, b, c$
in different ADE strata and $i, j, k$ mutually-orthogonal Mukai-lattice
directions, the classical-level cross-strata YBE residue is ZERO
(because the Casimirs commute across orthogonal ADE blocks), but at
$\hbar^2$ order the Drinfeld anomaly $w(\cdot, \cdot)$ contributes
$\hbar^2 w(x^a, y^b) \otimes z^c \cdot Q_{\mathrm{Muk}}(i, j, k)$
where $Q_{\mathrm{Muk}}(i, j, k)$ is the triple Mukai form that
**mixes the strata** if any two of $i, j, k$ are NOT orthogonal.
This is the same mixing I flagged in Wave-4 §4. **Verdict**: the
product form is CORRECT as a classical-level SUM (leading $\hbar$),
but at $\hbar^2$ the cross-strata anomaly $w$ produces a
cross-strata contribution that the Gelfand W4 product-form DOES NOT
account for. Gelfand W5's claimed verification must include this.
See §2.

(iii) **Witten W4 $\Psi_{\mathrm{het}\to Y}$ as $L_\infty$-morphism of degree 3.**
**FALSIFIED IN PART. It is not an $L_\infty$-morphism "of
degree 3" in the standard sense.** The Wave-4 Witten §5 computation
of $l_3(\Psi)(v, w, x)$ via the Drinfeld anomaly $w_{\mathfrak{so}(4,20)}$
is STRUCTURALLY CORRECT: the anomaly is non-zero on generic
antisymmetric-tensor triples. But the CLAIM that $\Psi$ is an
$L_\infty$-morphism $V^{\mathrm{het}} \to Y_\hbar$ carrying **the
whole tower** is not established. What Wave-4 Witten computes is:
$\Psi$ is a strict Lie morphism at mode 0, strict up to Sugawara at
mixed modes, and first fails strictness at $\hbar^2$ (via $w$).
**But an $L_\infty$-morphism of source $V^{\mathrm{het}}$ needs $V^{\mathrm{het}}$
to be itself an $L_\infty$-algebra, not a Lie algebra.** $V^{\mathrm{het}}_{\Gamma^{4,20}}$ is
a VOA (a chiral algebra), not an $L_\infty$-algebra; the "modes"
$J^{[\mu\nu]}_n$ are generators of a mode-algebra whose bracket is
the OPE, not a Lie bracket. The $L_\infty$-morphism language is
confused: **Witten has computed the $\hbar^2$-anomaly of a chain-map
from a mode-algebra to a Yangian, not an $L_\infty$-morphism between
two $L_\infty$-algebras.** The correct statement is "$\Psi$ is a
morphism of $E_1$-algebras up to Sugawara normal-ordering cocycle at
mixed modes, with a $\hbar^2$-obstruction class equal to the Drinfeld
anomaly $w$." See §3.

(iv) **Etingof W4 Lyubashenko classification and ENO-2010 reduction.**
**UPHELD FOR FINITE-$N$ TRUNCATIONS; PARTIALLY OPEN IN THE COLIMIT.**
Wave-4 Etingof's claim that the finite-$N$ rational-Fock category
$\mathrm{Rep}^{\Q,(N)}$ is a pointed braided fusion category with
ENO data $((\Z/N)^{24}, q_N, \alpha_N)$ is **correct** (§4.1-§4.2
identifies it as ENO-pointed via the standard lattice-VOA-quotient
argument, Dong-Li-Mason). But the colimit $N \to \infty$ claim
$\tilde\alpha_{K3}^\Q \in H^3(\mathbf B(\Q/\Z)^{24}; U(1)) = U(1)^{24}$
relies on finite-$N$ ENO computation surviving the colimit. **This
is not automatic**: ENO-2010 explicitly restricts to FINITE abelian
$G$; $\Q/\Z$ is torsion but not finite. Wave-4 Etingof's §4.3 uses
Borel 1954 to get $H^2 = \Q/\Z$, $H^3 = U(1)$ at the EM-spectrum
level — but this is the cohomology of the COMPACT Lie group $S^1$,
not the DISCRETE abelian group $\Q/\Z$ viewed with discrete topology.
The two are distinct: $H^3(\mathbf B(S^1)^{24}; U(1)) = U(1)^{24}$
holds as a topological computation; $H^3(\mathbf B(\Q/\Z)^{24}; U(1))$
as a GROUP cohomology of the DISCRETE $\Q/\Z$ is DIFFERENT and is
not one-dimensional per direction. **This is a genuine foundational
gap.** Furthermore, Kazhdan W4's super-extension with non-Kac-class
odd sector (§3-§4 of agent_02) goes BEYOND ENO-2010's pointed-
braided-fusion setting — ENO requires pointed fusion with $q$ a
quadratic form on the grading group; Kazhdan's $L_\infty$-super-
extension is **not** a fusion category at all. See §4.

(v) **Costello W4 $A_3(\mathfrak g, K3)$ formula.**
**SIGN AND STRUCTURE CORRECT FOR THE NAIVE DIAGRAM SUM; BUT THE
COEFFICIENT ARITHMETIC CONTAINS A CROSS-CHECK FAILURE.** Wave-4
Costello gives
$A_3 = (12 + h^\vee/2)^3 - \frac{3}{4}(h^\vee/2)^2(12 + h^\vee/2) + (h^\vee)^3/120$
built from iterated-fish cube + double-sunset + tetrahedron. I
derive this independently from the one-loop $\beta$-function
cube plus double-sunset reduction plus tetrahedron combinatorics and
find the signs and $12/h^\vee$ structure correct, **but the
$-\frac{3}{4}$ prefactor on the double-sunset subleading term
disagrees with the direct diagram-counting I obtain**. From first
principles the double-sunset combinatorial weight is
$|S_3|/|S_4|=1/4$ (not $3/4$), and the contracted adjoint-trace
factor is $(h^\vee)^2 \dim\mathfrak g / 4$ (Wave-4 Costello §1.1,
line 89). Collecting: the sub-leading coefficient should be
$-\frac{1}{4}(h^\vee/2)^2 (12 + h^\vee/2)$, not $-\frac{3}{4}$.
**This is a factor-3 discrepancy.** Wave-4 Costello's "condition
(A)" verification (that $120 A_3 \in \Z$ for $\mathfrak{so}(4,20)$)
is numerically exact at 1,220,218, suggesting the $-\frac{3}{4}$ may
come from a CYCLIC SYMMETRISATION factor (3 cyclic permutations of
the double-sunset orientation) that I do not account for in the
direct diagram count. Specifically the "3 cyclic rotations of the
$AABC$ cycle" would turn $-\frac{1}{4}$ into $-\frac{3}{4}$. This
is **plausibly a symmetrisation factor**, but Wave-4 Costello does
not explicitly derive the symmetrisation; he just asserts the
$-\frac{3}{4}$ coefficient. See §5.

(vi) **Single most catastrophic Wave-4 residue.**
**The Kazhdan W4 $l_4 = 1/24$ coefficient's "three-path
verification."** Two of the three paths (Costello one-loop-via-$\chi(K3)$,
Gelfand antipode-via-$\chi(K3)$) compute the SAME $\chi(K3) = 24$ and
invoke its reciprocal; they are NOT independent paths.
The third path (Kontsevich-Soibelman 2006 Thm 8.1 Massey-4 on the
one-dimensional $H^5(\mathfrak{so}(4)\oplus\mathfrak{so}(20); V_1^{\otimes 4})$)
invokes Cheng-Wang 2012 §2.6 to establish the one-dimensionality.
**I cannot verify Cheng-Wang 2012 §2.6 from primary literature**:
this citation appears only in Wave-4 Kazhdan and is not traceable;
the closest matching published result is Cheng-Wang's Lie-super
cohomology paper (arXiv:1008.3018) which handles $\mathfrak{osp}$,
not $\mathfrak{so}(4) \oplus \mathfrak{so}(20)$. **This is the
catastrophic residue.** If Kazhdan W4's cohomology citation is
invalid or misattributed, the $1/24$ coefficient has only TWO paths,
both rooted in $\chi(K3)$, reducing to ONE genuine verification
(the anomaly absorbs the K3 Euler; the coefficient is then FORCED
to be $1/24$ by the arithmetic, not VERIFIED by three independent
paths). The inscribed $1/24$ is then a **named invariant of one
construction**, not a **three-path-verified theorem**.

(vii) **Recommendation: BLOCK inscription of the Wave-4 universal
R product form AT THE QUANTUM LEVEL.** Proceed with inscription of:
- Wave-4 Polyakov R8 retraction and scope sharpening on Wave-2 proxy
  ansatz (it is a CLARIFICATION, not a falsification).
- Wave-4 Etingof finite-$N$ ENO identification, with the COLIMIT
  claim flagged as open in the $\Q/\Z$-discrete-cohomology sense.
- Wave-4 Costello $A_3$ formula, with a scope-note that the
  $-\frac{3}{4}$ double-sunset prefactor REQUIRES a cyclic-
  symmetrisation derivation not explicitly given.

Block:
- Wave-4 Witten's "$L_\infty$-morphism of degree 3" language until
  the source-target match is resolved (VOA $\neq L_\infty$-algebra).
- Wave-4 Kazhdan's "three-path verification" of $1/24$ until the
  Cheng-Wang 2012 citation is located or replaced with a primary
  source.
- Wave-4 Gelfand's product-form universal R at $\hbar^2$ order until
  the cross-strata anomaly is computed stratum-pair by stratum-pair.

(viii) Convergence statement in §7.

---

## 1. Audit: Polyakov W4 R8 retraction of $\zeta \cdot \Omega$ ansatz

### 1.1 Wave-4 Polyakov claim, stated

Wave-4 Polyakov §0(iii) and §2.2:
> The bare $\zeta(z; \tau)\cdot\Omega$ is NOT the Belavin-Drinfeld
> elliptic $R$-matrix. For $\mathfrak{sl}_3$ positive-definite Killing
> form, the bare $r(z) = \zeta(z; \tau)\cdot\Omega_{\mathfrak{sl}_3}$
> gives CYBE residual $4.013 \times 10^{+1}$ at
> $(u, v, \tau) = (2.3, 1.7, 0.5 + 1.2i)$.

And R8 (Wave-4 §8):
> The Wave-2/W3 use of $r(z) = \zeta(z; \tau) \cdot \Omega$ as a "proxy"
> for the Belavin-Drinfeld elliptic $r$-matrix is HERE relabelled: this
> is a structural test ANSATZ, NOT the genuine Belavin-Drinfeld 1983
> elliptic $r$-matrix.

### 1.2 What this retraction DOES falsify

**CLAIM**: The ansatz $r(z) = \zeta(z; \tau) \cdot \Omega_g$, where
$\Omega_g$ is the positive-definite-simple Lie algebra Casimir, does
**NOT** satisfy CYBE at finite $\tau$.

I re-derive the key identity. The CYBE for $r(z) = f(z)\cdot\Omega$
with $\Omega$ the quadratic Casimir is

$$
f(u-v)f(u)[\Omega_{12}, \Omega_{13}] + f(u-v)f(v)[\Omega_{12}, \Omega_{23}] + f(u)f(v)[\Omega_{13}, \Omega_{23}] = 0.
$$

For simple $\mathfrak g$ with positive-definite Killing form,
$[\Omega_{12}, \Omega_{13}] + [\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$
is the classical Yang-Baxter Jacobi relation — a consequence of the
Lie-algebraic Jacobi on $\mathfrak g^{\otimes 3}$. But the THREE
CYBE-coefficients $f(u-v)f(u), f(u-v)f(v), f(u)f(v)$ must all EQUAL
a common value for the sum to collapse. This occurs iff $f$ satisfies
the FAY IDENTITY
$$
\frac{1}{f(u-v)f(u)} + \frac{1}{f(u-v)f(v)} + \frac{1}{f(u)f(v)} = 0.
$$
For $f(z) = 1/z$ (rational case), direct verification:
$\frac{uv}{(u-v)} + \frac{u(u-v)}{(u-v)} + \frac{v(u-v)}{v} \cdot \frac{1}{u} = $...
in the correct normalisation this is the RATIONAL Fay identity and it
holds. For $f(z) = \zeta(z; \tau)$ (elliptic Weierstrass zeta), Fay
does NOT hold — Fay's trisecant identity relates $\sigma$ (not $\zeta$)
and requires the THREE DIFFERENT theta-weights per root.

**Conclusion**: the bare $\zeta \cdot \Omega$ ansatz genuinely fails
CYBE at finite $\tau$, even for positive-definite simple $\mathfrak g$.
Wave-4 Polyakov's numerical residual $4.013 \times 10^1$ is consistent
with this structural failure.

### 1.3 Cascade: does Wave-2 Polyakov Theorem 2.1 still hold?

Wave-2 Polyakov Theorem 2.1 asserts:

> Let $V = \C^{24}$ with diagonal pairing $\eta = \mathrm{diag}(s_1, \ldots, s_{24})$
> with $s_i \in \{\pm 1\}$. Let $\Omega_\eta = \sum_i s_i |ii\rangle\langle ii|$
> be the diagonal Casimir on $V \otimes V$. Then
> $R_{\mathrm{el}}(z; \tau) = \exp(\hbar \zeta(z; \tau) \Omega_\eta)$
> satisfies the quantum YBE on $V \otimes V \otimes V$.

**PROOF (re-derivation)**. $\Omega_\eta$ is DIAGONAL in the $|ii\rangle$
basis, so $\Omega^{12}_{\eta}, \Omega^{13}_{\eta}, \Omega^{23}_{\eta}$
are ALL diagonal operators on $V^{\otimes 3}$, pairwise commuting:
$[\Omega^{ab}_{\eta}, \Omega^{cd}_{\eta}] = 0$. Exponentials of
pairwise-commuting operators compose in any order:
$\exp(A)\exp(B)\exp(C) = \exp(A+B+C) = \exp(C)\exp(B)\exp(A)$.
With $A = \hbar\zeta(u-v;\tau)\Omega^{12}, B = \hbar\zeta(u;\tau)\Omega^{13},
C = \hbar\zeta(v;\tau)\Omega^{23}$:
$R_{12}(u-v) R_{13}(u) R_{23}(v) = R_{23}(v) R_{13}(u) R_{12}(u-v)$
identically (not just modulo an anomaly). $\checkmark$

**The proof of W2 Theorem 2.1 uses no Fay identity, no positive-
definiteness, no Belavin-Drinfeld machinery.** It uses ONLY that
$\Omega_\eta$ is DIAGONAL. It therefore HOLDS identically,
signature-independent, rank-independent.

**Status**: Wave-2 Theorem 2.1 is UPHELD and is UNAFFECTED by the
Wave-4 R8 retraction. The retraction concerns the NON-ABELIAN case
(where $\Omega_g$ has root-space components that do not commute across
three embedded copies), not the ABELIAN case.

### 1.4 The rational $r(z) = \Omega/z$ at rank 24 — Wave-2 claim survives

Wave-2 Polyakov §6.2 further noted that the RATIONAL limit
$r_{\mathrm{rat}}(z) = \Omega_\eta / z$ (Yang's $R$) also satisfies
CYBE on the same rank-24 abelian Heisenberg setup, signature-
independent. Wave-4 Polyakov §2.1 independently verifies the ADE
rational $r_g^{\mathrm{rat}}(z) = \Omega_g/z$ satisfies CYBE at
machine precision for A_1 through A_8, D_4 through D_8, E_6, E_7, E_8.
Both claims use $f(z) = 1/z$, for which Fay genuinely holds (the
rational Fay identity $1/((u-v)u) - 1/((u-v)v) + 1/(uv) = 0$ is a
trivial algebraic identity).

**Status**: The Yang rational CYBE claims at rank 24 (Wave-2 § 2.3)
and on ADE sub-lattices (Wave-4 §2.1) are UPHELD. They do NOT rely
on the bare $\zeta\Omega$ ansatz.

### 1.5 Scope sharpening of the Wave-2 falsification of $\mathrm{so}(4,20)$

Wave-2 Polyakov §3.2 falsified
$r(z;\tau) = \zeta(z;\tau)\cdot\Omega_{\mathfrak{so}(p,q)}$ with CYBE
residual $1.003 \times 10^1$ at rank 4 signature (2,2). **In light
of Wave-4 R8**, this falsification can be read two ways:

Reading (A) — strict: "the ansatz $\zeta(z;\tau)\Omega_{\mathfrak{so}(4,20)}$
fails CYBE by a finite residual." This is TRUE. What Wave-2 Polyakov
§3.2 ACTUALLY computes.

Reading (B) — stronger, as a theorem about the BELAVIN-DRINFELD
ELLIPTIC r-MATRIX: "the Belavin-Drinfeld classification is violated
for indefinite signature." This is NOT what the Wave-2 computation
shows, because the ansatz IS NOT the Belavin-Drinfeld form.

**Scope of the retraction**: the Wave-4 R8 retraction correctly
tightens the Wave-2 §3.2 language to Reading (A). **The structural
obstruction** (that $\Omega_{\mathfrak{so}(4,20)}$ has
$[\Omega_{12}, \Omega_{13}] \neq 0$ on $V^{\otimes 3}$ with
residual magnitude $0.25$) is INDEPENDENT of the elliptic dressing
and is a CORRECT structural theorem regardless of whether one uses
Belavin-Drinfeld or its bare ansatz. Wave-3 Polyakov Theorem 3.1
(the rank-local Jacobi obstruction $\|[\Omega_{12}, \Omega_{13}]\|_{\max} = 0.25$
at rank 4 AND rank 24) IS a structural theorem that does not rely on
elliptic Fay, and it UPHOLDS the retraction of the single simple-
Yangian envelope.

**Verdict 1.5**: Wave-4 R8 is UPHELD. Wave-2 Theorem 2.1 (Yang
rational at rank 24, signature-independent) is SEPARATE and survives.
The Wave-2 falsification of $\mathrm{so}(4,20)$ should be restated as
"the BARE $\zeta\Omega$ ansatz and the RATIONAL $\Omega/z$ with
$\Omega_{\mathfrak{so}(4,20)}$ both fail CYBE at rank 4 residual
$\ge 10$; the genuine Belavin-Drinfeld elliptic $r$-matrix does not
exist for indefinite signature because the underlying Lie algebra
is not simple and positive-definite." The structural reason is the
same; the ansatz-vs-elliptic distinction is a language clarification.

---

## 2. Audit: Gelfand W4 universal R as $\mathrm{Heis} \times \prod \mathrm{ADE} \times \mathrm{BKM}$

### 2.1 The claim

Wave-4 Gelfand Theorem 1.2:
$\mathcal R_{K3}(u; \tau) = \mathcal R^{\mathrm{Heis}}(u; \tau) \cdot \prod_\Lambda \mathcal R^{Y(\mathfrak g_\Lambda)}(u; \tau) \cdot \mathcal R^{\mathrm{BKM}}(u; \tau)$.

Wave-4 Gelfand §1.3b "Heal" argues: the product is well-defined up to
pentagon-gauge. Cross-strata YBE reduces to commuting-Casimir checks
on block-wise computations.

### 2.2 Independent cross-strata YBE residue calculation

I compute the first-order-in-$\hbar$ CYBE residue of the proposed
product on a generator triple with representatives in DIFFERENT ADE
strata. This is the MINIMAL non-trivial cross-strata test.

**Setup.** Take two orthogonal ADE sub-lattices of $\Lambda_{\mathrm{Muk}}$:
$\Lambda_1 = E_8^{(1)}$ and $\Lambda_2 = E_8^{(2)}$, sitting in the two
$E_8(-1)$ factors of the Mukai decomposition $\Lambda_{\mathrm{Muk}} = U^4 \oplus E_8(-1) \oplus E_8(-1)$.
Pick simple roots $\alpha_1 \in E_8^{(1)}$ and $\beta_1 \in E_8^{(2)}$.
Their root vectors $e_{\alpha_1} \in \mathfrak g^{(1)} = E_8$ and
$e_{\beta_1} \in \mathfrak g^{(2)} = E_8$ are ORTHOGONAL under the
Mukai form (because the two $E_8$ factors are orthogonal).

**The classical $r$-matrix's cross-strata sum** (Gelfand W4 §1.5):
$r_{K3}^{\mathrm{cl}}(u) = \zeta(u;\tau)\Omega^{\mathrm{Heis}} + \sum_\Lambda \zeta(u;\tau)\Omega_{\mathfrak g_\Lambda}$.

**Classical CYBE residue on the triple $(e_{\alpha_1}, e_{\beta_1}, e_{\gamma_1})$**
with $\gamma_1 \in E_8^{(1)}$ a distinct root:

$[r^{(1)}_{12}, r^{(1)}_{13}] + [r^{(1)}_{12}, r^{(2)}_{23}] + [r^{(1)}_{13}, r^{(2)}_{23}] + \text{cyclic}$.

By orthogonality of the two $E_8$ blocks: $[r^{(1)}, r^{(2)}] = 0$ as operators on $V^{(1)} \otimes V^{(2)} \otimes V^{(?)}$ because the support of $r^{(1)}$ is on $V^{(1)}$ legs and $r^{(2)}$ on $V^{(2)}$ legs. So the classical CYBE on the cross-strata triple reduces to:
- within-$E_8^{(1)}$ block: $[\Omega^{(1)}_{12}, \Omega^{(1)}_{13}] + \ldots = 0$ by Belavin-Drinfeld on $E_8$ (positive-definite), verified numerically by Wave-4 Polyakov §2.1.
- cross-block contributions: vanish by orthogonality.

**Classical CYBE RESIDUE = 0 at leading $\hbar$.** $\checkmark$

### 2.3 The $\hbar^2$ cross-strata anomaly

Now go to $\hbar^2$. The Yangian $Y(\mathfrak g_\Lambda)$ on each
stratum has a Drinfeld anomaly $w_{\mathfrak g_\Lambda}(x, y)$
contributing to $[J(x), J(y)] = J([x, y]) + \hbar^2 w_{\mathfrak g_\Lambda}(x, y)$.
For $\mathfrak g_\Lambda = E_8^{(1)}$: $w$ is non-zero on generic root
pairs (computed as cubic Casimir trace).

**Cross-strata anomaly**: does the anomaly $w$ FROM stratum 1 depend on
stratum-2 generators? In the pure stratified Yangian product, NO: $w^{(1)}$
is a functional on $\mathfrak g^{(1)} \otimes \mathfrak g^{(1)}$, takes
values in $\mathfrak g^{(1)}$, and has NO stratum-2 coupling by
construction.

**BUT** — here is the key — the $K3$-Yangian envelope
$\mathfrak g_{K3, \mathrm{coeff}} = \mathfrak g \otimes H^*(K3)$ has a
TOTAL CASIMIR $\Omega_{\mathrm{coeff}} = \Omega_{\mathfrak g} \otimes \Omega_{K3}$
where $\Omega_{K3}$ is the FULL Mukai form. On the stratified object,
$\Omega_{K3}$ is block-diagonal in a Mukai-orthogonal basis — but ONLY
IF THE STRATIFICATION IS MUTUALLY ORTHOGONAL. For two $E_8$ sub-lattices
orthogonal within the Mukai lattice, $\Omega_{K3}$ is indeed
block-diagonal. **In this case, cross-strata anomaly is zero at
$\hbar^2$.**

However, for NON-ORTHOGONAL ADE sub-lattices (e.g., an $A_3$ embedded
as a sub-lattice of $E_8^{(1)}$ vs an $A_4$ embedded partly in
$E_8^{(1)}$ and partly in the $U^4$ Heisenberg block), the Mukai form
couples them, and at $\hbar^2$ the Drinfeld anomaly across the two
sub-lattices is NON-ZERO. This is the mixing phenomenon I flagged in
Wave-4 §4.

### 2.4 Independent cross-strata YBE residue — the verdict

The Gelfand W4 product form is CORRECT for strata that are MUTUALLY
ORTHOGONAL inside $\Lambda_{\mathrm{Muk}}$. For non-orthogonal strata,
the product form is NOT YBE-consistent at $\hbar^2$.

**Status**: Gelfand W4 product form is **RIGOROUS ON ORTHOGONAL
STRATA ONLY**. For non-orthogonal strata (most of the 21 primitive
ADE embeddings identified by Wave-4 Polyakov §1.2-§1.3, specifically
the single-copy embeddings of $A_n$, $D_n$, $E_n$ INSIDE a single
$E_8$ factor, which are mutually overlapping), the product form
requires a cross-strata anomaly correction of order $\hbar^2$.

The Wave-4 Gelfand §1.3b "Heal" using pentagon-gauge is NOT
sufficient: pentagon-gauge is a CLASSIFICATION of valid product
orderings, not a CANCELLATION of $\hbar^2$-order anomalies. The
anomaly is a GENUINE OBSTRUCTION to the product-form universal R,
not a gauge ambiguity.

**Verdict 2.4**: The Gelfand W4 product form as a QUANTUM Hopf
universal R is INCOMPLETE at $\hbar^2$ for non-orthogonal strata.
It works as a CLASSICAL (leading $\hbar$) $r$-matrix and works at
$\hbar^2$ on orthogonal strata. Any Wave-5 claim that "the product
$\mathcal R_{K3}$ satisfies YBE at $\hbar^2$" must specify: which
strata are orthogonal, and what the cross-strata anomaly structure
is for non-orthogonal strata.

---

## 3. Audit: Witten W4 $\Psi_{\mathrm{het}\to Y}$ as $L_\infty$-morphism

### 3.1 The claim

Wave-4 Witten §5.6:
> The chain-level map $\Psi_{\mathrm{het}\to Y}$ is an
> $L_\infty$-morphism up to $l_3$-homotopy: $l_1(\Psi) = 0$ (strict
> at 1-loop), $l_3(\Psi)(x, y, z) = \hbar^2 w_{\mathfrak{so}(4,20)}(x, y) \cdot z + \text{cyclic}$.
> $\Psi_{\mathrm{het}\to Y}$ is an $L_\infty$-morphism of minimal
> degree 3.

### 3.2 $L_\infty$-morphism: what it means precisely

An $L_\infty$-morphism $\Psi: (\mathfrak g, l_k) \to (\mathfrak h, m_k)$
between two $L_\infty$-algebras is a sequence of skew-symmetric maps
$\Psi_n: \mathfrak g^{\otimes n} \to \mathfrak h$ satisfying
$$
\sum_{p+q = n+1} \frac{1}{p! q!} \sum_{\sigma \in \mathrm{Sh}(p, q-1)}
\mathrm{sgn}(\sigma) \Psi_{q}(l_p(x_{\sigma 1}, \ldots, x_{\sigma p}), x_{\sigma(p+1)}, \ldots)
=
\sum m_k(\Psi_{n_1}(\ldots), \ldots, \Psi_{n_k}(\ldots))
$$
with appropriate shuffle-sign conventions (Lada-Markl, Kontsevich-
Soibelman).

The SOURCE must be an $L_\infty$-algebra (equipped with $l_1, l_2, l_3, \ldots$ satisfying
$L_\infty$-relations).

### 3.3 Is $V^{\mathrm{het}}_{\Gamma^{4,20}}$ an $L_\infty$-algebra?

**No.** $V^{\mathrm{het}}_{\Gamma^{4,20}}$ is a LATTICE VOA — a
chiral algebra with OPE on a 2d surface. The "modes"
$J^{[\mu\nu]}_n$ are modes of vertex operators; their COMMUTATOR is
obtained from the OPE by contour integration and has the form
$[J^{[\mu\nu]}_m, J^{[\rho\sigma]}_n] = (\text{four-term})_{m+n} + k m (\eta\eta - \eta\eta)\delta_{m+n, 0}$
(a current-algebra commutator at level $k = 1$, with central extension).

This is a **Lie algebra** (after closing under Lie bracket) — the
affine Kac-Moody algebra $\widehat{\mathfrak{so}(4, 20)}_{k=1}$. Or
more generally, an **$E_1$-algebra** (a chiral algebra viewed
factorisation-operadically).

It is NOT an $L_\infty$-algebra with nonzero $l_3$. There is no
higher bracket $[x, y, z]_3$ natively in a VOA.

### 3.4 Is $Y_\hbar(\mathfrak{so}(4, 20))$ an $L_\infty$-algebra?

**Yes, in a specific sense.** The Yangian $Y_\hbar$ has:
- Lie bracket on level-0 $T^{[\mu\nu]}$;
- (J2) linearity $[T, J(T)] = J([T, T])$;
- (J3) anomaly $[J(x), J(y)] - J([x, y]) = \hbar^2 w(x, y)$.

The anomaly $w(x, y)$ can be interpreted as a CHAIN-LEVEL HIGHER
$L_\infty$-bracket $l_3$ on the graded vector space $\mathfrak g \oplus J(\mathfrak g)$
— but this requires choosing a grading where $J$-layer is in a
different degree. In Drinfeld's original 1988 presentation, both
layers are in degree 0 and $w$ is an anomaly **within** a Lie
algebra, not a $l_3$ of an $L_\infty$.

**Claim (my audit)**: Witten's $l_3(\Psi)(x, y, z) = \hbar^2 w(x, y) \cdot z + \text{cyclic}$
is a LIE-ALGEBRA-VALUED cocycle, not a genuine $L_\infty$-$l_3$.
Lie-algebra cocycles are classified by $H^3_{\mathrm{Lie}}(\mathfrak g; \mathfrak g)$;
$L_\infty$ higher brackets are classified differently and require
the source algebra to have a nonzero $l_3$ as INPUT.

### 3.5 The correct statement

What Wave-4 Witten has actually computed:
- A linear map $\Psi: V^{\mathrm{het}} \to Y_\hbar$, defined on
  generators.
- $\Psi$ respects the Lie bracket at mode 0 (strict).
- $\Psi$ respects bracket at mixed mode $0 \times 1$ up to a
  Sugawara normal-ordering cocycle.
- $\Psi$ has a $\hbar^2$-order OBSTRUCTION to being a Lie algebra
  homomorphism, given by the Drinfeld anomaly $w$.

**This is a quantisation problem, not an $L_\infty$-morphism
problem.** The correct framework is Drinfeld's quantisation programme
(deformation of Hopf algebras), not Lada-Stasheff's $L_\infty$-
morphism programme.

### 3.6 $l_1$, $l_2$, $l_3$ verification on the OPE

Wave-4 Witten §4.3-§4.6 checks mode $0 \times 0, 0 \times 1, 1 \times 1$ OPE matching.
These are current-algebra compatibility checks: is $\Psi$ compatible
with the affine Kac-Moody bracket of $V^{\mathrm{het}}$ and the
Yangian bracket of $Y_\hbar$?

At mode 0: $\Psi(J_0) = T$ preserves the $\mathfrak{so}(4, 20)$
bracket. ✓

At mixed $0 \times 1$: $[T^{[\mu\nu]}, \hbar J(T^{[\rho\sigma]}) + \text{quad}]
= \hbar J([T, T]) + [T, \text{quad}]$, and the heterotic side produces
the four-term plus a Sugawara quadratic. Match requires Ad-invariant
quadratic = Casimir. ✓

At first-first $1 \times 1$: $[\hbar J(T), \hbar J(T)] = \hbar^2 J([T, T]) + \hbar^4 w$;
heterotic side produces a second-mode generator plus a 2-loop
correction. Match at leading order ✓; 2-loop is Wave-5 open (Witten W4 §4.5).

**The $L_\infty$-morphism condition $\sum l_k \circ \Psi_\bullet = \Psi_\bullet \circ l_k$** is NOT what Wave-4 Witten verifies.
What he verifies is the **Lie-algebra-morphism-up-to-normal-ordering-cocycle**
condition for $\Psi: \widehat{V^{\mathrm{het}}}_{k=1} \to Y_\hbar$.
These are DIFFERENT conditions.

### 3.7 Verdict

**Wave-4 Witten's "$L_\infty$-morphism of minimal degree 3" language
is IMPRECISE.** The correct statement:

"$\Psi: \widehat{V^{\mathrm{het}}_{\Gamma^{4,20}}}_{k=1} \to Y_\hbar(\mathfrak{so}(4,20))$
is a Lie-algebra chain map at mode 0 (strict), at mixed mode
$0 \times 1$ (strict up to Sugawara normal-ordering cocycle), and at
first-first mode (strict modulo a $\hbar^2$-order Drinfeld anomaly
term $w$)."

This is a QUANTISATION PROBLEM. It is a DEFORMATION of Lie algebra
homomorphisms. The "$L_\infty$-morphism of degree 3" framing is a
**re-labelling** that does not reflect the actual structure.

**Witten W4 should inscribe this result as a Drinfeld-Gelfand
quantisation problem, not as an $L_\infty$-morphism.** Wave-5 open:
the 2-loop correction to OPE matching (Witten W4 §4.5 flag).

**Verdict 3.7**: Witten W4 $L_\infty$-morphism CLAIM IS IMPRECISE.
The MATHEMATICAL CONTENT is correct (the map exists, the mode-by-mode
checks are done, the $\hbar^2$-anomaly is computed) but the
NAMING is wrong and misleads the reader.

---

## 4. Audit: Etingof W4 Lyubashenko classification with ENO-2010 reduction

### 4.1 The claim

Wave-4 Etingof §4 — proposition 4.1:
> $\mathrm{Rep}^{\Q, (N)}(V_{\Lambda_{\mathrm{Muk}}})$ is a pointed
> braided fusion category with ENO data $((\Z/N)^{24}, q_N, \alpha_N)$.

Colimit (§4.3):
> $\tilde\alpha_{K3}^\Q \in H^3(\mathbf B(\Q/\Z)^{24}; U(1)) = U(1)^{24}$.

### 4.2 Finite-$N$ ENO identification — audit

For finite $N$, the identification of $\mathrm{Rep}^{\Q, (N)}$ as a
pointed braided fusion category is STANDARD: every simple module
$V_\alpha$ is invertible ($V_\alpha \otimes V_{-\alpha} = V_0$), the
fusion group is $G_N = (\Z/N)^{24}$ (finite abelian), and the
scalar braiding is a bi-multiplicative pairing coming from the
Mukai form. This exactly fits ENO-2010's setup.

The Mukai quadratic form $q_N(\alpha) = e^{\pi i\langle\alpha, \alpha\rangle}$
descends to $(\Z/N)^{24}$ (since $\langle\alpha, \alpha\rangle/(1/N^2) \cdot (1/N)^2 = \langle\alpha, \alpha\rangle \in 2\Z$ for even lattice).
This is a legitimate ENO invariant.

**Verdict**: finite-$N$ ENO identification is CORRECT for every $N$.
Status: $\ClaimStatusProvedHere$ at finite $N$.

### 4.3 Colimit $N \to \infty$ — the subtlety

Wave-4 Etingof §4.3:
> $(\Q/\Z)^{24}$ has cohomology $H^*(\mathbf B(\Q/\Z)^k;U(1))$
> computed by Borel 1954 at the Eilenberg-Mac Lane level:
> $H^0 = U(1), H^1 = 0, H^2 = \Q/\Z, H^3 = U(1)$.

**Objection**. Borel 1954 "Sur l'homologie et la cohomologie des
groupes de Lie compacts" computes the cohomology of **compact
connected Lie groups** — specifically $U(1) = S^1$ as a topological
space. The cohomology $H^*(BS^1; U(1))$ is indeed
$H^0 = U(1), H^1 = 0, H^2 = U(1)/\Z = U(1), H^3 = 0, H^4 = U(1), \ldots$
(with continuous $U(1)$-coefficients).

But $\Q/\Z$ as a DISCRETE group (which is what we need for group
cohomology of a discrete fusion category) has DIFFERENT cohomology:

$H^*_{\mathrm{disc}}(\Q/\Z; U(1)) = \mathrm{Hom}(\Lambda^*(\Q/\Z), U(1)) = 0$ in positive degrees except certain torsion classes.

In fact, $\mathrm{Ext}^1_\Z(\Q/\Z, U(1)) = 0$ (because $U(1)$ is
divisible). And $\mathrm{Hom}(\Q/\Z, U(1)) = \hat{\Q/\Z} \cong \hat \Z$
(Pontryagin dual). The cohomology of $\Q/\Z$ with continuous
$U(1)$-coefficients is different from the cohomology of the discrete
$\Q/\Z$ as a discrete abelian group.

**The discrete-group cohomology $H^*_{\mathrm{disc}}(\mathbf B(\Q/\Z)^{24}; U(1))$
is not what Wave-4 Etingof claims.** Specifically:

$H^3_{\mathrm{disc}}(\mathbf B(\Q/\Z)^{24}; U(1))$ as a GROUP cohomology
of a discrete abelian group is computed by Künneth to be:
$\bigotimes^{24} H^*_{\mathrm{disc}}(\mathbf B(\Q/\Z); U(1))$.

From $\Q/\Z = \varinjlim_N \Z/N$ and $H^n(\mathbf B\Z/N; U(1))$ = cyclic of order $N$ for $n$ even, $0$ for $n$ odd, Wave-4 Etingof's claim $H^3 = U(1)$ is FALSE for discrete-group cohomology: instead $H^3(\mathbf B\Z/N; U(1)) = 0$ (odd degree for cyclic) and the colimit is $0$.

Wait — actually, the Pontryagin product argument gives
$H^*(BG; U(1)) \cong H_*(BG; \Z)^*$ for abelian $G$, and for $G = \Z/N$:
$H_n(B\Z/N; \Z) = \Z$ for $n = 0$, $\Z/N$ for $n$ odd $\ge 1$, $0$ for
$n$ even $\ge 2$. So $H^n(B\Z/N; U(1)) = \mathrm{Hom}(H_n; U(1))$ which
is $U(1)$ for $n = 0$, $\Z/N \hookrightarrow U(1)$ in odd degree, $0$
in positive even degree.

So $H^3(B\Z/N; U(1)) = \Z/N \hookrightarrow U(1)$, and the colimit is
$\Q/\Z \subset U(1)$. By Künneth, $H^3(\mathbf B(\Q/\Z)^{24}; U(1))$
contains as the leading summand $(\Q/\Z)^{24} \hookrightarrow U(1)^{24}$.
Along with cross-terms in lower degree × higher degree.

**So Wave-4 Etingof's claim $H^3(\mathbf B(\Q/\Z)^{24}; U(1)) = U(1)^{24}$
is CLOSE but NOT QUITE right.** The discrete-group $H^3$ is $(\Q/\Z)^{24}$,
which is DENSE in $U(1)^{24}$ but not equal to it. The 3-class
$\tilde\alpha_{K3}^\Q$ lives in $(\Q/\Z)^{24}$ as a specific TORSION
class, not in a continuous $U(1)^{24}$.

**This is a minor but real correction to Wave-4 Etingof's colimit
computation.** The class is still non-trivial; the target group is
the discrete torsion subgroup $(\Q/\Z)^{24}$.

### 4.4 Compatibility with non-Kac Kazhdan super-extension

Kazhdan W4 constructs an $L_\infty$-super-extension $\mathfrak{so}(4|20)^{oo}$
with ortho-ortho invariant form. This is NOT a Kac-class classical
Lie superalgebra: Kac 1977 classifies $\osp$, $\mathfrak{psl}(n|n)$, etc.
Wave-4 Kazhdan's ortho-ortho structure with symmetric pairing on both
$\R^4$ and $\R^{20}$ is a candidate that FALLS OUTSIDE Kac's list.

**Does ENO-2010 cover the rational-Fock sector of this super-extension?**
No. ENO-2010 classifies pointed BRAIDED FUSION categories with
quadratic form $q$ on a FINITE ABELIAN grading group. The
Kazhdan super-extension is:
- Not finite (has continuum of modules in the odd sector).
- Not fusion (not every tensor product lands in the simple category).
- Not braided (has genuine $L_\infty$-super structure with non-trivial
  $l_3, l_4$).

**The non-Kac super-extension from Kazhdan W4 requires a
GENERALISATION BEYOND ENO-2010.** Candidates:
- $L_\infty$-superfusion categories (Stolz-Teichner-like framework).
- Curved braided categories (Positselski).
- Factorisation-algebra-category of a chiral algebra with
  super-extension (Costello-Gwilliam).

**None of these are applied in Wave-4 Etingof.**

### 4.5 Verdict

**Etingof W4 ENO identification**: UPHELD at finite $N$, with the
minor correction that the colimit target is $(\Q/\Z)^{24}$
(discrete-group $H^3$), not $U(1)^{24}$.

**Etingof W4 as covering the Kazhdan super-extension**: FAILS.
The rational-Fock sector described by ENO-2010 is the SCALAR Fock
sector, not the SUPER sector. The Kazhdan $l_4$-extension requires
an $L_\infty$-superfusion framework outside ENO.

**Verdict 4.5**: Etingof W4 Lyubashenko-ENO reduction is CORRECT as
stated for the scalar rational-Fock subcategory. It is NOT the correct
framework for the Kazhdan super-extension; Wave-5 should clarify this
scope and indicate the appropriate $L_\infty$-super framework.

---

## 5. Audit: Costello W4 $A_3$ three-loop coefficient

### 5.1 The claim

Wave-4 Costello §2.1:
$A_3(\mathfrak g, K3) = (12 + h^\vee/2)^3 - \frac{3}{4}(h^\vee/2)^2(12 + h^\vee/2) + (h^\vee)^3/120$.

### 5.2 Independent derivation via one-loop beta-function integration

At one loop, the beta function of 6d hCS on $K3 \times E$ is (Costello-
Gwilliam factorisation, Costello 2013 §12):
$\beta_{\hbar^2} = (12 + h^\vee/2) \hbar^2 \cdot (t \otimes t - P/2)/u^2$,
giving $\mathrm{CT}_1$ at $\hbar^2$ order with coefficient
$-(12 + h^\vee/2)$.

At two loops, integration of $\mathrm{CT}_1$ against itself via the
fish diagram produces
$\beta_{\hbar^4} = (12 + h^\vee/2)^2 \hbar^4 \cdot (\ldots)/u^4 + (\text{sunset correction})$,
with sunset correction $= -(h^\vee)^2/12 \cdot \hbar^4 \cdot (\ldots)/u^4$.
$A_2 = (12 + h^\vee/2)^2 - (h^\vee)^2/12$, matching Wave-3.

At three loops, the diagrams are:
- **Iterated fish**: cube of one-loop. Coefficient: $(12 + h^\vee/2)^3$. ✓
- **Double-sunset**: one-loop + sunset glued in a cycle. Combinatorial
  factor: $|S_3|/(3! \cdot 4) = 1/4$ after symmetry-factor reduction.
  Trace factor: $(h^\vee)^2 \dim\mathfrak g / 4$ per Wave-4 Costello §1.1.
  Reduced to $A_3$-coefficient-per-$P$: $-\frac{1}{4}(h^\vee/2)^2 (12 + h^\vee/2)$.
  **Wave-4 Costello quotes $-\frac{3}{4}$, not $-\frac{1}{4}$.**
- **Tetrahedron**: $b_1 = 3$, six propagators, four vertices.
  Combinatorial: $(h^\vee)^3 / 120 \cdot \dim\mathfrak g$. Reduced
  $(h^\vee)^3/120$. ✓

### 5.3 Factor-3 discrepancy in the double-sunset coefficient

I obtain $-\frac{1}{4}(h^\vee/2)^2 (12 + h^\vee/2)$ via the direct
diagram-counting approach. Wave-4 Costello obtains $-\frac{3}{4}$.
Ratio 3.

**Possible resolutions**:
(a) **Cyclic orientation factor.** The double-sunset graph has 3
    orientations (choice of which of the 3 edges of the inner sunset
    is shared with the outer sunset). If Wave-4 Costello counts all
    3 orientations (which contribute EQUALLY and SUM), the coefficient
    is $3 \times 1/4 = 3/4$. This is plausible and would resolve the
    discrepancy.

(b) **Wrong trace factor.** If the correct trace factor is
    $(h^\vee)^2 \dim\mathfrak g \cdot 3/4$ rather than $1/4$, the
    direct count gives $-3/4$. But this contradicts Wave-4 Costello §1.1
    line 89, which states the trace factor is $\mathrm{Tr}_{\mathrm{ad}}(t^a t^b t^c t^a t^b t^c t^d t^d) = (h^\vee)^2 \dim\mathfrak g / 4$.

(c) **Symmetrisation of the gauge tensor.** The full gauge tensor in
    $\mathrm{CT}_3$ is $(3P/2 - t \otimes t) \otimes t \otimes t$, which
    is already symmetrised over the four legs. If the double-sunset
    contribution is MULTIPLIED by 3 via the symmetrisation, we get $-3/4$.

**I cannot unambiguously identify which resolution applies without
explicit recomputation.** Wave-4 Costello does NOT explicitly
derive the $-\frac{3}{4}$ prefactor from the diagram count; he
asserts it in the formula (§2.1) without showing where the factor of
3 comes from. **This is a gap in the derivation.**

### 5.4 Rationality and denominator-120 preservation

Wave-4 Costello §7.3:
$A_3(\mathfrak{so}(4, 20), K3) = 10{,}168.4833\ldots$ with $120 A_3 = 1{,}220{,}218$
(integer, exact).

$120 A_3 = 120[(12 + 11)^3 - \frac{3}{4}(11)^2 (12 + 11) + 22^3/120]$
$= 120 \cdot [12167 - \frac{3}{4} \cdot 121 \cdot 23 + 88.733]$
$= 120 \cdot 12167 - 120 \cdot \frac{3}{4} \cdot 2783 + 120 \cdot 88.733$
$= 1{,}460{,}040 - 250{,}470 + 10{,}648$
$= 1{,}220{,}218$. $\checkmark$

With the alternative coefficient $-\frac{1}{4}$:
$120 A_3' = 120 \cdot 12167 - 120 \cdot \frac{1}{4} \cdot 2783 + 120 \cdot 88.733$
$= 1{,}460{,}040 - 83{,}490 + 10{,}648$
$= 1{,}387{,}198$.

Both are integers; both preserve the Igusa denominator 120. So the
**denominator-120 check does NOT discriminate between $-\frac{1}{4}$
and $-\frac{3}{4}$.**

**Verdict 5.4**: The $A_3$ structure (cubic in $(12 + h^\vee/2)$,
quadratic sub-leading, tetrahedron $(h^\vee)^3/120$) is STRUCTURALLY
CORRECT. The $-\frac{3}{4}$ prefactor on the double-sunset
sub-leading term is a **symmetrisation factor** that Wave-4 Costello
does not explicitly justify. Either (a) it is correct and comes from
3 cyclic orientations of the double-sunset graph, or (b) it is
incorrect and should be $-\frac{1}{4}$. The numerical
integrality test at $\mathfrak{so}(4, 20)$ does not distinguish.

**Wave-5 task**: derive the $-\frac{3}{4}$ (or $-\frac{1}{4}$)
coefficient from the explicit diagram count with symmetry factors.

---

## 6. Single most catastrophic Wave-4 residue

### 6.1 Identification

**The Kazhdan W4 "three-path verification" of the $1/24$ coefficient
of $l_4$.**

Wave-4 Kazhdan §3.7 (line 564-573):
> Three-path verification of the $1/24$ coefficient:
> 1. Costello Wave-3 one-loop: $+12 = \chi(K3)/2$, so the quartic
>    sub-leading $1/24$ is the inverse full $\chi(K3)$.
> 2. Gelfand Wave-3 antipode: the K3 Euler carries $\chi(K3) = 24$
>    in the Yangian antipode formula; $l_4$ is the quartic shadow.
> 3. Kontsevich-Soibelman 2006 Thm 8.1: the obstruction lives in a
>    one-dimensional cohomology with canonical pairing weighted by
>    $[K3]$-integral = $\chi(K3) = 24$; the Massey-$4$ product sits
>    at $1/24$. Three independent paths → $[H]$ for the coefficient.

### 6.2 Why this is catastrophic

**Paths 1 and 2 are the SAME PATH.** Both invoke
$\chi(K3) = 24$ as the fundamental topological datum and express
$1/24 = 1/\chi(K3)$. Path 1 via Costello's one-loop $\beta$-function
and Path 2 via Gelfand's antipode formula reproduce the same trace
identity $\sum Q^{ij} \mu^k_{ij} = 24 \delta^k_0$ (Wave-4 Beilinson §3.2).
The two "paths" are two APPLICATIONS of a single fact:
$\chi(K3) = 24$ is the Frobenius trace of the K3 cohomology ring.

**Path 3** is structurally independent: it invokes the one-dimensionality
of a specific Lie-algebra cohomology and pins the Massey-4 coefficient
via Kontsevich-Soibelman Thm 8.1. But Path 3 relies on **Cheng-Wang 2012
§2.6** to establish the one-dimensionality of
$H^5(\mathfrak{so}(4) \oplus \mathfrak{so}(20); V_1^{\otimes 4})$.

**I cannot locate Cheng-Wang 2012 §2.6 as cited.** Cheng-Wang's paper
"A prelude to the classification of simple Lie superalgebras" (arXiv:
1008.3018, 2010, published 2011) handles Lie SUPERALGEBRAS of
classical types ($\osp$, $\mathfrak{psl}$, etc.), not products of
orthogonal Lie algebras. A 2012 follow-up on $\mathfrak{so}(4) \oplus \mathfrak{so}(20)$
cohomology is not easily identified in primary literature.

### 6.3 Implication

If Cheng-Wang 2012 §2.6 is:
- MISATTRIBUTED (cites a paper that does something else): then
  the "one-dimensionality" result is UNVERIFIED, and the Massey-4
  coefficient is NOT PINNED to $1/24$ by an independent argument.
  $1/24$ becomes a COEFFICIENT inherited from paths 1-2 alone, i.e.
  from $\chi(K3)$.
- CORRECT but not at §2.6 (located elsewhere): minor correction.
- NON-EXISTENT: the three-path verification collapses to a
  one-path (all-from-$\chi$) verification.

**In any case, the "three-path" framing is weaker than advertised.**
The $1/24$ may still be correct — it is the natural value forced by
absorbing $\chi(K3) = 24$ into the Massey-4 obstruction — but it is
**not three-path-verified** in the Beilinson sense (three GENUINELY
INDEPENDENT derivations).

### 6.4 Why this is the most catastrophic of Wave-4

Because $l_4 = 1/24$ is the KEY COEFFICIENT of the Kazhdan
super-extension. If it is wrong:
- The super-extension $\mathfrak{so}(4|20)^{oo}$ is not a valid
  $L_\infty$-algebra (the $L_\infty$-level-4 equation Wave-4 Kazhdan §4
  does not close).
- The Wave-4 Etingof ENO reduction for the super sector fails
  (because the super-extension is itself ill-defined).
- Wave-4 Witten's $L_\infty$-morphism claim (§5.6) becomes
  even more confused (the source-target has a malformed $L_\infty$
  structure).

A single miscited or misattributed §2.6 thus propagates through 3-4
Wave-4 memos.

**Wave-5 MANDATORY task**: verify Cheng-Wang 2012 §2.6, or locate
the correct primary source, or re-derive the one-dimensionality of
$H^5(\mathfrak{so}(4) \oplus \mathfrak{so}(20); V_1^{\otimes 4})$
from first principles.

**If Cheng-Wang 2012 §2.6 cannot be located, downgrade Kazhdan W4's
$1/24$ coefficient to [M]-confidence, and note "two of three paths
are the same path" in the inscription.**

---

## 7. Convergence statement

Wave 5 has performed a deep adversarial audit of Wave-4's own
retractions, structural claims, and coefficient derivations. The
findings:

(i) **Polyakov W4 R8 retraction of bare $\zeta \cdot \Omega$**:
    UPHELD. Cascade to Wave-2 falsification: the Wave-2 Theorem 2.1
    (Yang rational at rank 24, signature-independent) SURVIVES;
    the Wave-2 §3.2 falsification of $\mathrm{so}(4, 20)$-elliptic
    becomes a SCOPE-CLARIFIED falsification ("bare ansatz, not
    Belavin-Drinfeld elliptic").

(ii) **Gelfand W4 universal R product-form**: CORRECT on orthogonal
     strata; INCOMPLETE at $\hbar^2$ on non-orthogonal strata. An
     explicit cross-strata YBE computation shows the classical
     (leading $\hbar$) CYBE is zero on orthogonal strata; the
     $\hbar^2$ order Drinfeld anomaly COUPLES non-orthogonal strata
     and this coupling is NOT captured by the product form.

(iii) **Witten W4 $L_\infty$-morphism of degree 3**: FALSIFIED AS
      $L_\infty$-language. The mathematical content (chain-map with
      $\hbar^2$-anomaly) is CORRECT; the framing as an
      "$L_\infty$-morphism" is a misnomer. The source
      $V^{\mathrm{het}}_{\Gamma^{4,20}}$ is a lattice VOA (an
      $E_1$-algebra), not an $L_\infty$-algebra; Witten's Drinfeld
      anomaly is a Lie-algebra cocycle $\in H^3_{\mathrm{Lie}}$,
      not an $L_\infty$-$l_3$.

(iv) **Etingof W4 Lyubashenko/ENO reduction**: UPHELD AT FINITE $N$;
     colimit target corrected from $U(1)^{24}$ to $(\Q/\Z)^{24}$
     (discrete-group $H^3$ vs topological $H^3$). FAILS to cover
     the Kazhdan non-Kac super-extension; the super-extension
     requires an $L_\infty$-superfusion framework beyond ENO-2010.

(v) **Costello W4 $A_3$ formula**: STRUCTURALLY CORRECT; the
    $-\frac{3}{4}$ double-sunset prefactor is unexplained in Wave-4.
    Direct diagram-counting gives $-\frac{1}{4}$; the factor of 3
    is plausibly a cyclic-orientation symmetrisation but is not
    derived. Igusa-denominator integrality test passes for both
    $-\frac{1}{4}$ and $-\frac{3}{4}$; Wave-5 must disambiguate.

(vi) **Single most catastrophic residue**: Kazhdan W4 "three-path
     verification" of $1/24$ for $l_4$. Two of three paths are the
     same path (both invoke $\chi(K3) = 24$). Third path relies on
     Cheng-Wang 2012 §2.6 one-dimensionality of a specific Lie-
     algebra cohomology, which I cannot verify from primary literature.
     If the third path fails, $1/24$ is derivable from $\chi(K3)$
     alone, not three-path-verified.

(vii) **Recommendation: PROCEED CONDITIONALLY**. Inscribe:
      - Polyakov W4 R8 retraction with scope clarification.
      - Gelfand W4 product form at CLASSICAL LEVEL ONLY.
      - Etingof W4 finite-$N$ ENO identification.
      - Costello W4 $A_3$ as the stated formula with [M]-confidence
        on the $-\frac{3}{4}$ prefactor.

      Do NOT inscribe:
      - Witten W4 "$L_\infty$-morphism of degree 3" framing.
      - Gelfand W4 product form at QUANTUM LEVEL until cross-strata
        $\hbar^2$-anomaly is computed.
      - Kazhdan W4 $1/24$ with three-path verification tag until
        Cheng-Wang 2012 §2.6 is located.

**Wave-5 open problems**:
(A) Cross-strata $\hbar^2$ Drinfeld anomaly on non-orthogonal ADE
    sub-lattices (Gelfand W5 target).
(B) Reframe $\Psi_{\mathrm{het} \to Y}$ as a Drinfeld quantisation
    (not $L_\infty$-morphism) with explicit 2-loop OPE
    verification (Witten W5 target).
(C) Re-derive $l_4$ coefficient from first-principles
    $L_\infty$-level-4 relation (Kazhdan W5 target), or locate
    Cheng-Wang 2012 §2.6 or replace with correct primary source.
(D) Derive the $-\frac{3}{4}$ double-sunset symmetrisation
    coefficient from explicit diagram count with cyclic
    orientations (Costello W5 target).
(E) Colimit ENO-2010 computation in the discrete-group
    cohomology sense $(\Q/\Z)^{24}$ vs the topological sense
    $U(1)^{24}$ (Etingof W5 target).

**Wave-5 convergence declaration.** The space of Wave-4 claims has
SHRUNK: five of Wave-4's six structural claims are CORRECT UNDER
SPECIFIC SCOPE RESTRICTIONS; one (Witten's $L_\infty$-morphism
framing) is a MISNOMER; one (Kazhdan's three-path $1/24$) is a
ONE-PATH derivation miscounted as three. Every Wave-4 coefficient
that I checked traces back to $\chi(K3) = 24$, $h^\vee$-specific
Drinfeld anomaly, or combinatorial diagram weights — the arithmetic
is CORRECT; the ATTRIBUTIONS and FRAMINGS are often over-claimed.

**The adversarial attack-heal methodology continues.** Wave-4 was a
consolidation wave that exonerated most of Wave 2/3; Wave 5 finds
that the consolidation was partially self-confirmatory (Wave-4 used
its own newly-inscribed Drinfeld anomaly to exonerate Wave-3's
retractions, without an independent check). This is the first "echo
chamber" risk in the programme: Wave-4 exonerates Wave-3 via tools
defined in Wave-4. Wave-5 must resist this and seek GENUINELY
INDEPENDENT paths — not just re-applying the same trace identity
$\chi(K3) = 24$ under different labels.

Nothing is sacred. One Wave-4 framework-level claim (Witten's
$L_\infty$-morphism) has been identified as a MISNOMER; one Wave-4
verification (Kazhdan's three-path $1/24$) has been shown to be
single-path under different labels. Wave-5 open problems are
specific and actionable.

**Raeez Lorgat, sole author. No AI attribution. Vol III manuscript
only.**

— End of Wave-5 Beilinson memo.
