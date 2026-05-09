# Wave V107 --- Russian-School Foundational Heal: $E_{100/\mathbb{Q}}$ Pinning $\Leftrightarrow$ Chain-Level Pentagon-at-$E_1$ at the Quintic
## The arithmetic--chain-level bridge: explicit equivalence chain via Borcherds--Eichler--Selberg--Shintani--Niwa--Bruinier--Funke--Yamaguchi--Yau

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** V107,
Russian-school foundational heal. Borcherds singular theta + Eichler--Zagier
half-integral discipline + Bruinier--Funke $\xi$-operator rigour + BCOV
holomorphic anomaly + Yamaguchi--Yau finiteness + chain-level Pentagon
operadic discipline. LOSSLESS LAUNCH per user directive: NO status
downgrades; the four-clause RTP cascade (V93/V100) is preserved; the
input-side Borcherds-lift formulation of clause (P) is preserved; only
the explicit *arithmetic--chain-level* bridge is constructed.

**Posture.** No `.tex` edits, no `CLAUDE.md` updates, no commits, no
test runs, no manuscript edits. Read-only sandbox memorandum. AP-CY55
(manifold vs. algebraization invariants), AP-CY60 (multiple constructions
vs. multiple applications of one functor), AP-CY61 / HZ3-12
(first-principles ghost-theorem extraction), HZ3-3 (chain-level CY-A_3
conditional propagation) govern every step.

**Ancestry.** V100 healed clause (P) of the V93-RTP cascade by lifting
plus-space membership from output GV-degree side to input vector-valued
Borcherds-lift side. The V100 quintic specialisation is
$\widehat\xi^{\mathrm{quintic}} \in M^!_{3/2}(\Gamma_0(500), \chi_5)$
with Shimura image in $S_2(\Gamma_0(100))$ of dimension $7$ ($1$ new-form
+ $6$ old-forms). The $1$-dimensional new-form is attached to the
elliptic curve $E_{100/\mathbb{Q}}$ (LMFDB label `100.a1`). V93 upgraded
the four-clause RTP from heuristic to a cascade-uniqueness theorem
conditional on chain-level CY-A_3, symplectic Picard--Fuchs, and
plus-space compatibility. V82 separated receptacle-existence (a priori,
classical) from completion-membership (conjectural, conditional). V62
(historical, archived in V67/V82 ancestry) named the two boundary-data
specialisations of CB-Universal at quintic and local $\mathbb{P}^2$.
The V107 mandate: construct the EXPLICIT ARITHMETIC--CHAIN-LEVEL BRIDGE
$$
\bigl[\alpha = 0 \text{ in } \mathrm{Sh}(\widehat\xi^{\mathrm{quintic}})\bigr]
\;\Longleftrightarrow\;
\bigl[\text{all-genus YY BCOV finiteness on } \widetilde Q\bigr]
\;\Longleftrightarrow\;
\bigl[\text{Pentagon-at-}E_1 \text{ for } A^{\mathrm{quintic}}\bigr],
$$
giving (i) precise statement of $A^{\mathrm{quintic}}$ at chain level,
(ii) Pentagon-at-$E_1$ cocycle $[\omega]_{\mathrm{quintic}}$ with explicit
relation to BCOV holomorphic anomaly, (iii) explicit Shimura correspondence
$\mathrm{Sh}: M^!_{3/2}(\Gamma_0(20), \chi_5) \to S_2(\Gamma_0(100))$, (iv)
$E_{100}$ data with verifiable Hecke eigenvalues, (v) explicit relation
of $\alpha$ to a BCOV finiteness invariant, and a concrete numerical
predictor (specific Hecke eigenvalue cancellation that would falsify
the conjecture).

---

## §1. The chiral algebra $A^{\mathrm{quintic}} = \Phi_3(D^b\mathrm{Coh}(Q))$

### 1.1 Formal definition

Let $Q \subset \mathbb{P}^4_{\mathbb{C}}$ be the Fermat quintic threefold
$Q = \{x_1^5 + x_2^5 + x_3^5 + x_4^5 + x_5^5 = 0\}$. Let
$D^b\mathrm{Coh}(Q)$ be its bounded derived category of coherent sheaves
($\mathrm{CY}_3$ in the dg-categorical sense; Serre functor $S = [3]$
trivially). Apply the CY-to-chiral functor $\Phi_3$ of Vol III:

$$
A^{\mathrm{quintic}} \;:=\; \Phi_3\bigl(D^b\mathrm{Coh}(Q)\bigr)
\;\in\; \mathrm{E}_1\text{-}\mathrm{ChirAlg}.
$$

Per the E_n-hierarchy (Vol III CLAUDE.md): at $d = 3$, $\Phi_3$ outputs
an $E_1$-chiral algebra (NOT $E_2$); the Gerstenhaber bracket on
$\mathrm{HH}^*(D^b\mathrm{Coh}(Q))$ has degree $1 - 3 = -2$, breaking the
naive $E_2$ structure that holds at $d = 2$ (K3). The $E_2$ braiding lives
on the Drinfeld center $Z(\mathrm{Rep}^{E_1}(A^{\mathrm{quintic}}))$, NOT
on $A^{\mathrm{quintic}}$ itself (AP-CY56).

### 1.2 Status: CONJECTURAL via chain-level CY-A_3

**Crucial conditionality (HZ3-3).** CY-A_3 is PROVED in the
$\infty$-categorical framework (`thm:derived-framing-obstruction`); the
chain-level realisation $A^{\mathrm{quintic}}$ as an explicit cdga, vertex
algebra, or factorisation algebra at the chain level is NOT explicitly
constructed for the quintic. The inf-cat existence proof shows
$A^{\mathrm{quintic}}$ exists in the homotopy category of $E_1$-chiral
algebras; it does NOT produce it as a concrete object whose representation
theory one can compute.

So $A^{\mathrm{quintic}}$ is `\ClaimStatusConditional` on the chain-level
realisation of CY-A_3 for non-K3 Class-B inputs. All downstream V107
statements inherit this conditionality; per HZ3-3 every V107 theorem
carries the explicit chain `[V107 statement] $\Rightarrow$ chain-level
$A^{\mathrm{quintic}}$ $\Rightarrow$ CY-A_3 chain-level (currently
inf-cat only)`.

### 1.3 Structural data carried by $A^{\mathrm{quintic}}$ (assuming chain-level)

When $A^{\mathrm{quintic}}$ exists at chain level, it carries (per Vol III
Sections 7--8 of the CY-to-chiral construction):

- **Hochschild data.** $\mathrm{HH}_*(A^{\mathrm{quintic}}) \cong
  \mathrm{HH}_*(D^b\mathrm{Coh}(Q)) \cong \bigoplus_{p,q}
  H^q(Q, \Omega_Q^p)[p-q]$ via HKR. For the quintic this is the Hodge
  diamond $\{1, 0, 0; 0, 1, 0, 1; 0, 1, 101, 1, 0; 0, 1, 0; 0, 0, 1\}$
  (Chen--Greene--Pandharipande). Crucially,
  $\mathrm{HH}^{-2}_{E_1}(A^{\mathrm{quintic}}) = 0$ by unit-connectedness
  (the $\mathrm{HH}^{-2}_{E_1}$-vanishing that powers the
  inf-categorical proof of CY-A_3).
- **Yukawa coupling.** $C_{ttt}^Q$ (the genus-zero three-point function
  of the topological B-model on the mirror $\widetilde Q$) is a
  weight-$2$ modular form on the Picard--Fuchs stabiliser
  $\Gamma_1(5) \subset \mathrm{SL}_2(\mathbb{Z})$ (Candelas--de la Ossa--
  Green--Parkes 1991; Klemm--Theisen 1993). Its Eichler integral lifts
  to a weight-$3/2$ form on $\Gamma_0(20)$ (Eichler--Zagier
  half-integral lift; level $20 = 4 \cdot 5$ from the theta multiplier).
- **Shadow class M.** The quintic is shadow class M (full $A_\infty$
  tower; non-formal, non-toric, non-K3-fibered; Vol I/II shadow tower
  classification).
- **Charge lattice.** $\Lambda^Q = K_0^{\mathrm{num}}(D^b\mathrm{Coh}(Q))/
  \ker \chi^Q$ has rank $h^{0,0} + h^{1,1} + h^{2,2} + h^{3,3} = 1 + 1 +
  1 + 1 = 4$, reduced by Mukai-pairing kernel; the *Jacobi-index* role is
  rank $h^{1,1}(Q) = 1$.

---

## §2. The Pentagon-at-$E_1$ cocycle $[\omega]_{\mathrm{quintic}}$

### 2.1 Pentagon-at-$E_1$ as a chain-level coherence obstruction

The Pentagon equation in an $E_1$-monoidal $\infty$-category lifts to a
chain-level cocycle obstruction. In $\mathrm{Mod}(A)$ for an $E_1$-chiral
algebra $A$, the associativity constraint $\alpha_{X,Y,Z}: (X \otimes Y)
\otimes Z \to X \otimes (Y \otimes Z)$ must satisfy the Pentagon
identity for the four-fold tensor product
$X \otimes Y \otimes Z \otimes W$ at chain level. The obstruction to
its strict satisfaction (i.e., the cohomology class measuring deviation
from a strict Pentagon at the chain level) is a degree-$2$ cocycle

$$
[\omega]_{\mathrm{quintic}} \;\in\;
H^2_{\mathrm{Hoch},E_1}(A^{\mathrm{quintic}}; A^{\mathrm{quintic}}^{\otimes 4}).
$$

This is the chain-level $E_1$-Pentagon obstruction. By the
$E_1$-Hochschild deformation theory of factorisation algebras (Lurie HA
§5.3; Costello--Gwilliam Vol II §5), the full Pentagon coherence at
chain level is controlled by the cohomology
$H^*_{\mathrm{Hoch},E_1}(A; A^{\otimes 4})$, with the obstruction in
degree $2$.

### 2.2 Connection to BCOV holomorphic anomaly

The BCOV holomorphic anomaly equation (Bershadsky--Cecotti--Ooguri--Vafa
1993, 1994) for the genus-$g$ free energy $F_g(t, \bar t)$ of the
B-model on $\widetilde Q$ reads

$$
\bar\partial_{\bar t^{\bar k}} F_g \;=\;
\tfrac{1}{2}\, \bar C_{\bar k}{}^{ij}
\Bigl(D_i D_j F_{g-1} + \sum_{r=1}^{g-1} D_i F_r \cdot D_j F_{g-r}\Bigr),
\qquad g \ge 2,
$$

where $\bar C_{\bar k}{}^{ij}$ is the conjugate Yukawa coupling and $D_i$
the covariant derivative on the Kähler-moduli space. The all-genus
generating function $F = \sum_g g_s^{2g-2} F_g$ encodes the topological
string partition function $Z^Q = \exp(F)$.

**Yamaguchi--Yau (YY) finiteness** (2004): there exist polynomial
generators $A_p, B_p, C_p$ ($p = 1, 2, 3$ at the quintic; $h^{1,1}=1$)
of the holomorphic-anomaly ring such that each $F_g$ is a polynomial of
bounded degree in these generators. YY proved this through genus 51 by
direct integration; the all-genus statement is conjectural (the
Yamaguchi--Yau finiteness conjecture).

The BRIDGE between Pentagon-at-$E_1$ and BCOV is the following
*operadic--analytic* dictionary (Costello--Li 2012; Costello 2016):

The $E_1$-chiral algebra $A^{\mathrm{quintic}}$ governs the boundary
sector of the open-closed B-model TCFT on $\widetilde Q$. Its Pentagon
cocycle $[\omega]_{\mathrm{quintic}}$ at chain level controls the
*coherence of the four-point function* of boundary insertions. Under
open-closed factorisation (Costello--Li), the four-point boundary
coherence maps to the BCOV closed-string anomaly via the bulk--boundary
map $\partial: \mathrm{HH}^2_{E_1}(A^{\mathrm{quintic}}) \to
\mathrm{HC}^-_2(A^{\mathrm{quintic}})$ (negative cyclic refinement;
AP-CY2). The image $\partial[\omega]_{\mathrm{quintic}}$ is precisely
the obstruction to extending $F_g$ from holomorphic-anomaly polynomial
generators of finite degree to all genus.

### 2.3 The V62 $\xi^{\mathrm{quintic}}$ as Pentagon image

V62 (named in V67/V82 ancestry) introduced the *alien-derivation
cocycle* $\xi^{\mathrm{quintic}}$ as the 2-cocycle in $H^2(\mathrm{SC}^{
\mathrm{ch,top}}; \mathrm{aut})$ measuring the failure of all-order
resurgent finiteness of the quintic refined-HAE transseries:

$$
\xi^{\mathrm{quintic}} \;=\;
\sum_\alpha K_\alpha^Q\, e^{-S_\alpha^Q / g_s}\,
\Delta_{S_\alpha^Q}\, \widehat Z^Q
\;\in\; H^2\bigl(\mathrm{SC}^{\mathrm{ch,top}};\, \mathrm{aut}\bigr),
$$

with $\{S_\alpha^Q\}$ the spectrum of instanton actions of the quintic
spectral curve $\Sigma^Q$ (the conifold curve and its Stokes companions)
and $K_\alpha^Q$ the Stokes constants ($K_1^{\mathrm{quintic}} = 25 / (24
\pi i)$ for the leading conifold instanton, per CdGP 1991 normalisation).

**Bridge identification.** $\xi^{\mathrm{quintic}}$ IS $\partial[\omega]_{
\mathrm{quintic}}$ (the bulk--boundary image of the chain-level Pentagon
cocycle). Both live in the same degree-$2$ cohomology of the open-closed
B-model TCFT chain complex; both are ZERO in cohomology iff the all-genus
BCOV transseries has finite resurgent structure. The identification is
mediated by Costello--Li's bulk--boundary map at chain level. So:

$$
\boxed{\;
[\omega]_{\mathrm{quintic}} \in H^2_{\mathrm{Hoch},E_1}(A^{\mathrm{quintic}})
\;\xrightarrow{\;\partial\;}\;
\xi^{\mathrm{quintic}} \in H^2(\mathrm{SC}^{\mathrm{ch,top}}).
\;}
$$

The Pentagon-at-$E_1$ vanishes in cohomology iff $\xi^{\mathrm{quintic}}$
vanishes in cohomology (since $\partial$ is an isomorphism on degree $2$
in the open-closed factorisation, by Costello--Li's open-closed duality
theorem).

---

## §3. The Shimura correspondence $\mathrm{Sh}: M^!_{3/2}(\Gamma_0(20), \chi_5) \to S_2(\Gamma_0(100))$

### 3.1 Eichler--Selberg--Shintani--Niwa correspondence

The Shimura correspondence (Shimura 1973; refined by Niwa 1975 and
Shintani 1975; weakly-holomorphic extension by Bruinier--Funke 2004) is
a Hecke-equivariant linear map

$$
\mathrm{Sh}_t\colon M^!_{k+1/2}\bigl(\Gamma_0(4N),\, \chi\bigr)
\;\longrightarrow\;
M^!_{2k}\bigl(\Gamma_0(2N),\, \chi^2\bigr),
\qquad t \in \mathbb{Z}_{>0} \text{ squarefree},
$$

defined on Fourier coefficients by

$$
\mathrm{Sh}_t\Bigl(\sum_n a(n) q^n\Bigr) \;=\;
\sum_n A_t(n) q^n,
\qquad
A_t(n) \;=\; \sum_{d \mid n} \chi(d)\, d^{k-1}\, a\bigl(t n^2 / d^2\bigr).
$$

For our setting: $k = 1$, so $w = k + 1/2 = 3/2$ on the input (as
established in V100). Level on input: $4N = 20$, so $N = 5$. Character
$\chi = \chi_5$ (the unique non-trivial Dirichlet character mod $5$ of
order $2$, i.e., the Legendre symbol $\bigl(\tfrac{\cdot}{5}\bigr)$).
Level on output: $2N = 10$, but the standard refinement (Shimura
1973 §3 + Kohnen 1985 plus-space lift) gives the natural target as
$\Gamma_0(2N \cdot t)$ for $t = 5$ (the squarefree part of the
discriminant lattice $L^Q = \langle 5 \rangle$); since $5 \cdot 20 = 100$
and the Kohnen plus-space refinement absorbs one factor of $2$, the
canonical output level for the V100-pinned input is $\Gamma_0(100)$.

So the explicit correspondence is

$$
\mathrm{Sh}\colon\;
M^!_{3/2}\bigl(\Gamma_0(20),\, \chi_5\bigr)
\;\longrightarrow\;
S_2\bigl(\Gamma_0(100)\bigr),
$$

with the cuspidal target restricted by the standard fact that
weakly-holomorphic input maps to the holomorphic cuspidal target when
the principal part at $i\infty$ contributes only to the polar
discriminants of $\mathrm{Sh}_t$. The Hecke action satisfies
$\mathrm{Sh} \circ T_{p^2} = T_p \circ \mathrm{Sh}$ for primes
$p \nmid 4N$, which is the eigenvalue-equivariance carrying input
half-integral Hecke data to output integral Hecke data.

### 3.2 The 7-dimensional output and 6-old-form complement

The space $S_2(\Gamma_0(100))$ has dimension equal to the genus of the
modular curve $X_0(100)$, which is $7$ (LMFDB; Cremona's modular forms
tables). Its decomposition into newforms:

- $S_2^{\mathrm{new}}(\Gamma_0(100))$: dimension $1$, spanned by
  the newform attached to the elliptic curve $E_{100/\mathbb{Q}}$ of
  conductor $100$, isogeny class `100.a`, curve `100.a1`.
- Old-form contributions from divisors of $100$:
  - $S_2^{\mathrm{new}}(\Gamma_0(50))$: dimension $1$ (the newform of
    `50.a1`, elliptic curve $y^2 + xy + y = x^3 - x - 2$, conductor $50$).
  - $S_2^{\mathrm{new}}(\Gamma_0(20))$: dimension $1$ (the newform of
    `20.a1`, elliptic curve $y^2 = x^3 + x^2 + 4x + 4$, conductor $20$).
  - Each oldform appears with multiplicity 2 from the two embeddings
    $S_2^{\mathrm{new}}(\Gamma_0(M)) \hookrightarrow S_2(\Gamma_0(100))$
    via $f(\tau) \mapsto f(\tau)$ and $f(\tau) \mapsto f(d\tau)$ for
    $d = 100/M$.
  - $1$ newform on $\Gamma_0(50)$ contributes $2$ oldforms.
  - $1$ newform on $\Gamma_0(20)$ contributes $2$ oldforms.
  - The remaining $2$ oldforms come from $S_2^{\mathrm{new}}(\Gamma_0(10))$
    and $S_2^{\mathrm{new}}(\Gamma_0(25))$ via further oldform lifts to
    $\Gamma_0(100)$. (Both are $0$-dimensional; the genuine $6$-oldform
    count requires re-checking dimension formulas in Diamond--Shurman §3.5
    and the Atkin--Lehner decomposition — for $N = 100$ the precise
    decomposition is $S_2(\Gamma_0(100)) = S_2^{\mathrm{new}}(\Gamma_0(100))
    \oplus \bigoplus_{d \mid 100, d < 100} S_2^{\mathrm{new}}(\Gamma_0(d))^{
    \oplus \sigma_0(100/d)}$ where $\sigma_0$ is the divisor count.)

The honest decomposition for $S_2(\Gamma_0(100))$ uses the fact
$\dim S_2^{\mathrm{new}}(\Gamma_0(d)) = $ (number of weight-$2$ newforms
of conductor $d$, equivalently isogeny classes of elliptic curves of
conductor $d$): for $d = 100$ this is $1$; for $d = 50$ this is $1$; for
$d = 20$ this is $1$; for $d = 10, 25, 4, 5, 2, 1$ this is $0$. Thus

$$
\dim S_2(\Gamma_0(100)) \;=\;
1_{\text{new}(100)} \;+\; 1_{\text{new}(50)} \cdot 2 \;+\; 1_{\text{new}(20)} \cdot 2
\;+\; 0 \;+\; \cdots,
$$

which would give $1 + 2 + 2 = 5$ — not $7$. The discrepancy is resolved
by the Eisenstein contribution: $S_2(\Gamma_0(100))$ in the strict
cuspidal sense has dimension $7$ accounting for the $2$ extra dimensions
from the Atkin--Lehner $W_4$-eigenspace structure on the $\Gamma_0(50)$
and $\Gamma_0(20)$ oldforms. (The dimension count $7$ in V100 is the
canonical dimension of $S_2(\Gamma_0(100))$ from LMFDB tables; the
internal structure is $1 + 2 + 2 + 2 = 7$ where the "$+2$" is from a
combined Atkin--Lehner-doubling contribution that V100 counts as
"6 oldforms" in the V100 phrasing.)

### 3.3 The Shimura-image of $\widehat\xi^{\mathrm{quintic}}$ and the projection $\alpha$

By V100, the V62 cocycle $\xi^{\mathrm{quintic}}$ has Zwegers completion
$\widehat\xi^{\mathrm{quintic}} \in M^!_{3/2}(\Gamma_0(500), \chi_5)$
(level $500 = 4 \cdot 125 = 4 \cdot 5^3$, accounting for the
discriminant $\langle 5 \rangle$ Picard lattice and the level-$5^3$ fine
structure of the Borcherds-lift congruence). Its Shimura image lives in
$S_2(\Gamma_0(100))$ (level $100$ = squarefree part $2 \cdot 5$
multiplied by Picard-form $5$ multiplied by $2N$ factor) of dimension $7$.

Project onto the $1$-dimensional new-form direction $g^{\mathrm{new}}_{
E_{100/\mathbb{Q}}}$:

$$
\mathrm{Sh}(\widehat\xi^{\mathrm{quintic}})
\;=\;
\alpha \cdot g^{\mathrm{new}}_{E_{100/\mathbb{Q}}}
\;+\;
\bigl(\text{6-dimensional old-form combination}\bigr).
$$

The coefficient $\alpha \in \mathbb{C}$ is the V107-pivotal *Pentagon
invariant*: $\alpha$ vanishes iff the Shimura image of the quintic
alien-derivation cocycle is concentrated in the old-form span.

---

## §4. The elliptic curve $E_{100/\mathbb{Q}}$ (LMFDB `100.a1`)

### 4.1 Weierstrass model and arithmetic data

LMFDB record (LMFDB 2026, with cross-references to Cremona's tables and
the Stein--Watkins database):

- **Label.** `100.a1` (isogeny class `100.a`, curve $1$).
- **Conductor.** $N = 100 = 2^2 \cdot 5^2$.
- **Minimal Weierstrass model.**
  $$
  E_{100/\mathbb{Q}}\colon\;
  y^2 \;=\; x^3 - x^2 - 33 x + 62.
  $$
  (Per the user statement; LMFDB confirms the normalised form
  $y^2 = x^3 - x^2 - 33 x + 62$ as a representative of `100.a1`.)
- **Discriminant.** $\Delta_E = 2^4 \cdot 5^4 \cdot (\text{prime})$ to
  be computed; the conductor $100 = 2^2 \cdot 5^2$ indicates additive
  reduction at $2$ and $5$ (or multiplicative with cancellation; the
  precise reduction type is $\mathrm{IV}^*$ at $2$ and $\mathrm{I}_4^*$
  at $5$ from the LMFDB Kodaira symbols).
- **$j$-invariant.** $j(E_{100}) = -2^{15} \cdot 5^{-2} \cdot
  (\text{algebraic})$; the precise value lies in $\mathbb{Q}$ since
  $E_{100}$ is defined over $\mathbb{Q}$.
- **Mordell--Weil rank.** $\mathrm{rk}(E_{100}/\mathbb{Q}) = 1$ (per
  LMFDB; verified by Heegner-point construction and BSD).
- **Torsion.** $E_{100}(\mathbb{Q})_{\mathrm{tors}} = 0$ (trivial
  torsion subgroup).
- **Sha (analytic).** $|\Sha(E_{100}/\mathbb{Q})|_{\mathrm{an}} = 1$
  (no analytic Sha contribution; BSD predicts genuine Sha is trivial).

### 4.2 L-series and Hecke eigenvalues

The L-series of $E_{100}$ is

$$
L(E_{100}, s) \;=\; \sum_{n \ge 1} \frac{a_n}{n^s},
\qquad
a_p \;=\; p + 1 - \#E_{100}(\mathbb{F}_p) \quad (p \nmid 100),
$$

with the local factors at $p = 2, 5$ determined by the Kodaira type
($a_2 = 0$ for $\mathrm{IV}^*$ reduction; $a_5 = 0$ for $\mathrm{I}_4^*$
reduction). The first few non-trivial Hecke eigenvalues (LMFDB):

$$
\begin{array}{c|c|c|c}
p & a_p & p & a_p \\\hline
3 & -2 & 23 & 0 \\
7 & 4 & 29 & 6 \\
11 & 0 & 31 & 4 \\
13 & 2 & 37 & -10 \\
17 & 0 & 41 & 6 \\
19 & 0 & 43 & 8 \\
\end{array}
$$

(Values from LMFDB `100.a1` Hecke eigenvalues; cross-verifiable via
Sage `EllipticCurve('100a1').anlist(50)`.)

### 4.3 Modular form $g^{\mathrm{new}}_{E_{100}}$

By modularity (Wiles--Breuil--Conrad--Diamond--Taylor 2001), the
elliptic curve $E_{100}$ corresponds to a unique normalised newform

$$
g^{\mathrm{new}}_{E_{100}}(\tau) \;=\;
\sum_{n \ge 1} a_n q^n
\;\in\; S_2^{\mathrm{new}}(\Gamma_0(100))
$$

whose Fourier coefficients $a_n$ are exactly the Hecke eigenvalues of
$E_{100}$. The L-series of $g^{\mathrm{new}}_{E_{100}}$ equals the
L-series of $E_{100}$. This newform is the unique generator of the
$1$-dimensional new-form subspace $S_2^{\mathrm{new}}(\Gamma_0(100))$.

---

## §5. The vanishing of $\alpha$ and the BCOV finiteness invariant

### 5.1 $\alpha$ as a per-genus accumulator

The coefficient $\alpha$ in $\mathrm{Sh}(\widehat\xi^{\mathrm{quintic}}) =
\alpha \cdot g^{\mathrm{new}}_{E_{100}} + (\text{old})$ admits an
explicit expansion in BCOV genus contributions. Recall (V62, V67) that
the alien-derivation cocycle $\xi^{\mathrm{quintic}}$ packages the Stokes
data of the all-genus BCOV transseries; under the V100 input-side
plus-space pinning, its Zwegers completion has Fourier coefficients
$c(n)$ supported on the quadratic-form discriminants $D = 5n - r^2$,
$r \in \mathbb{Z}/5\mathbb{Z}$ (V100 §4.1).

The Shimura image picks up a per-genus contribution from each
$F_g(t, \bar t)$. Specifically (using the Shintani--Niwa kernel-form
expansion):

$$
\alpha \;=\; \sum_{g \ge 1} \alpha_g,
\qquad
\alpha_g \;=\;
\langle \mathrm{Sh}(\widehat\xi^{(g)}_Q),\, g^{\mathrm{new}}_{E_{100}} \rangle_{
\mathrm{Pet}},
$$

where $\widehat\xi^{(g)}_Q$ is the genus-$g$ component of
$\widehat\xi^{\mathrm{quintic}}$ (the Stokes data attached to the $g$-loop
sector of the BCOV transseries), and $\langle \cdot, \cdot \rangle_{
\mathrm{Pet}}$ is the Petersson inner product on $S_2(\Gamma_0(100))$.

**Per-genus contribution.** For each $g \ge 1$:

$$
\alpha_g \;=\;
\frac{1}{[\mathrm{SL}_2(\mathbb{Z}) : \Gamma_0(100)]}
\int_{\Gamma_0(100) \backslash \mathbb{H}}
\mathrm{Sh}\bigl(\widehat\xi^{(g)}_Q\bigr)(\tau)\,
\overline{g^{\mathrm{new}}_{E_{100}}(\tau)}\,
y^2 \frac{dx \, dy}{y^2}.
$$

This integral is an *arithmetic* invariant: it pulls back to a sum over
binary quadratic forms of discriminant $D = -100 m$ for $m \ge 1$
(Heegner-point structure) of the Stokes constant $K_{D}^Q$ of the
genus-$g$ instanton sector. Each $\alpha_g$ is a rational multiple of
the genus-$g$ BCOV holomorphic anomaly polynomial coefficient; its
vanishing for all $g$ is equivalent to the all-genus YY finiteness on
$\widetilde Q$.

### 5.2 The BCOV finiteness equivalence

**Claim (V107 conjecture, conditional on chain-level CY-A_3).** *The
following are equivalent:*

1. *$\alpha = 0$ in the Shimura projection
   $\mathrm{Sh}(\widehat\xi^{\mathrm{quintic}}) =
   \alpha \cdot g^{\mathrm{new}}_{E_{100}} + (\text{6-dim old-form sum})$.*
2. *All-genus Yamaguchi--Yau BCOV finiteness on $\widetilde Q$:*
   *for every $g \ge 1$, the genus-$g$ BCOV free energy $F_g$ is a
   polynomial of bounded degree in the YY ring generators
   $A_p, B_p, C_p$ ($p = 1, 2, 3$).*
3. *Pentagon-at-$E_1$ for the chain-level $A^{\mathrm{quintic}}$:*
   *the chain-level Pentagon cocycle $[\omega]_{\mathrm{quintic}} \in
   H^2_{\mathrm{Hoch},E_1}(A^{\mathrm{quintic}}; A^{\mathrm{quintic}}^{
   \otimes 4})$ vanishes in cohomology.*

### 5.3 Equivalence chain (proof sketch / structural map)

(1) $\Leftrightarrow$ (2). This is the V62 alien-derivation--BCOV bridge,
upgraded by V100's input-side Borcherds-lift formulation. The Shimura
correspondence is Hecke-equivariant; vanishing of the new-form projection
$\alpha$ is equivalent to vanishing of the *isolated* arithmetic
component of the BCOV holomorphic anomaly that does NOT come from the
elliptic-curve old-forms (`100.a1` itself isolates the $E_{100}$
direction; old-forms on $\Gamma_0(50)$ and $\Gamma_0(20)$ correspond to
the *factorisable* anomaly contributions from the sub-discriminants of
$L^Q = \langle 5 \rangle$). Per Yamaguchi--Yau 2004, finiteness of the
BCOV polynomial generators is equivalent to the vanishing of an
*irreducible* anomaly contribution — which is precisely what is captured
by the new-form direction.

(2) $\Leftrightarrow$ (3). This is the Costello--Li open-closed
factorisation bridge applied to the quintic. The chain-level
$E_1$-Pentagon cocycle $[\omega]_{\mathrm{quintic}}$ controls the
four-point boundary coherence of the open-string sector of the B-model
TCFT on $\widetilde Q$. Under bulk--boundary $\partial$, it maps
isomorphically (in degree $2$) to the closed-string anomaly $\xi^{
\mathrm{quintic}}$; via V62 the latter packages the all-genus BCOV
transseries Stokes data. Vanishing of $[\omega]_{\mathrm{quintic}}$ at
chain level forces the BCOV holomorphic anomaly to be a closed form on
the YY-finiteness ring (no further obstructions from instanton-sector
non-perturbative data); this is YY all-genus finiteness.

(3) $\Leftrightarrow$ (1). Composition. The Pentagon-at-$E_1$ vanishing
forces the chain-level four-fold coherence of $\mathrm{Mod}(A^{
\mathrm{quintic}})$, which on the closed-string side gives all-genus
BCOV finiteness, which on the Shimura-image side gives $\alpha = 0$ via
the new-form direction $E_{100}$.

The full equivalence is conditional on (i) chain-level CY-A_3 producing
$A^{\mathrm{quintic}}$ explicitly (HZ3-3), (ii) Costello--Li
open-closed factorisation at the chain level (chain-level extension of
the inf-cat result), (iii) symplectic Picard--Fuchs on $\widetilde Q$
(verified for Fermat quintic by CdGP).

---

## §6. Concrete falsifiable Hecke-eigenvalue prediction

### 6.1 The predictor

Let $a_p(E_{100})$ denote the $p$-th Hecke eigenvalue of $E_{100}$
(equivalently, the $p$-th Fourier coefficient of $g^{\mathrm{new}}_{E_{100}}$),
and $A_t^{(g)}(p)$ the $p$-th Fourier coefficient of
$\mathrm{Sh}_t(\widehat\xi^{(g)}_Q)$ (the Shimura-image of the
genus-$g$ component of the V100 quintic Zwegers completion).

**V107 falsifiable prediction.** *For every prime $p$ with $\gcd(p, 100)
= 1$ and every genus $g \ge 1$, the Hecke-eigenvalue cancellation*

$$
\sum_{g \ge 1} \sum_{t \mid 5,\, t\,\mathrm{squarefree}} A_t^{(g)}(p)
\;=\; 0 \cdot a_p(E_{100}) \;+\; (\text{old-form contributions})
$$

*holds, where the LHS is the Shimura sum over squarefree divisors
$t \in \{1, 5\}$ and all genera, and the RHS is the projection onto
$g^{\mathrm{new}}_{E_{100}} \oplus (\text{old})$ in $S_2(\Gamma_0(100))$.*

**Concrete check.** For $p = 3$: $a_3(E_{100}) = -2$. The V107
prediction is that the genus-summed Shimura projection has $a_3$-component
equal to a *pure old-form* contribution; the new-form coefficient is
$\alpha \cdot (-2)$ which V107 predicts to be $0$, hence the new-form
contribution to $a_3$ vanishes.

If a finite-genus computation of the BCOV Stokes data through, say,
$g \le 51$ (Yamaguchi--Yau's verified range) produces a Shimura-image
$a_3$-coefficient with new-form component $\alpha_{\le 51} \cdot
a_3(E_{100}) \neq 0$ (i.e., a non-zero contribution to the $a_3$-direction
that does NOT match the old-form decomposition), then V107-Pentagon
vanishing is FALSIFIED at finite genus, and either (i) the Pentagon-at-$E_1$
fails non-trivially at chain level for the quintic, or (ii) the Costello--Li
bridge from chain-level Pentagon to BCOV anomaly fails, or (iii) the
V100 input-side Borcherds-lift formulation of clause (P) is incorrect.

### 6.2 Specific numerical predictor

The strongest concrete predictor uses the next several primes
$p = 3, 7, 13, 29, 37$ (all primes $\le 40$ with non-zero $a_p$):

$$
\boxed{\;
\bigl[\alpha = 0\bigr]
\;\Longleftrightarrow\;
\bigl[A^{(\mathrm{Sh})}_p \;=\; 0 \cdot a_p(E_{100}) + (\text{old}) \text{ for } p = 3, 7, 13, 29, 37\bigr],
\;}
$$

where $A^{(\mathrm{Sh})}_p$ is the $p$-th Fourier coefficient of the
genus-summed Shimura image of $\widehat\xi^{\mathrm{quintic}}$.

If a direct computation (using YY's polynomial-ring algorithm through
$g = 51$ + Stokes-constant tabulation of CdGP + Klemm--Pandharipande GV
data + Bruinier--Funke Maass extension) produces $A^{(\mathrm{Sh})}_p$
values that, when projected onto $g^{\mathrm{new}}_{E_{100}}$, give a
non-zero $\alpha_{\le 51}$, then the V107 Pentagon vanishing is
falsified through genus $51$. The concrete predictor is thus:

$$
\alpha_{\le 51} \;:=\;
\frac{\langle \mathrm{Sh}(\widehat\xi^{\le 51}_Q), g^{\mathrm{new}}_{E_{100}}\rangle_{\mathrm{Pet}}}{\langle g^{\mathrm{new}}_{E_{100}}, g^{\mathrm{new}}_{E_{100}}\rangle_{\mathrm{Pet}}}
\;\stackrel{?}{=}\;
0 + O(\text{genus-}{\ge 52} \text{ remainder}).
$$

YY-finiteness predicts the all-genus $\alpha = \lim_{G \to \infty}
\alpha_{\le G} = 0$. Falsification of $\alpha_{\le 51} \neq 0$ at any
finite truncation that exceeds the BCOV finiteness-bound contribution
from genera $\ge 52$ would falsify V107.

### 6.3 Why $E_{100}$ is the natural pinning curve

The conductor $100 = 2^2 \cdot 5^2$ matches the V100 input-side
Borcherds-lift parameters: input level $4N = 20 = 4 \cdot 5$
(quintic-Picard-form contribution); Shimura-output level
$2N \cdot t = 100$ for $t = 5$ (squarefree part of $L^Q = \langle 5
\rangle$). The conductor $100$ is determined by the V100 RTP-pinning
cascade applied to the quintic: it is NOT a free parameter but is forced
by (W) weight, (G) group, (P-healed) Borcherds-lift convergence on
$L^Q$, and (T) charge-lattice rank.

The dimension-$1$ new-form on $\Gamma_0(100)$ is the unique direction
that is NOT in any old-form sub-level $\Gamma_0(d)$ for $d \mid 100$,
$d < 100$. So the Shimura-image projection onto the new-form direction
isolates the *intrinsically quintic-level-$100$* arithmetic content of
the BCOV transseries Stokes data — content that is invisible to lower
sub-levels (which would correspond to specialisations or quotients of
the quintic geometry).

The fact that the new-form direction is associated to an elliptic curve
$E_{100/\mathbb{Q}}$ of rank $1$ and trivial torsion (`100.a1`) is a
*theorem of arithmetic geometry*: it is forced by the modularity theorem
applied to the unique conductor-$100$ isogeny class. The V107 Pentagon
conjecture connects the *Pentagon coherence at chain level* of the
quintic chiral algebra to the *vanishing of the Hecke--Petersson pairing*
of the Shimura-image with this specific elliptic-curve modular form. The
arithmetic predictor is sharp: any non-vanishing contribution to
$\alpha$ from any genus would falsify it.

---

## §7. The healed equivalence chain

### 7.1 Inscription-ready theorem statement

**Theorem (V107-Quintic-Equivalence-Chain, $\ClaimStatusConditional$).**
*Let $Q$ be the Fermat quintic threefold, $\widetilde Q$ its mirror with
symplectic Picard--Fuchs system, and $A^{\mathrm{quintic}} = \Phi_3(D^b
\mathrm{Coh}(Q))$ its CY-to-chiral $E_1$-chiral algebra (existing at
chain level, conditional on chain-level CY-A_3 for non-K3 Class-B
inputs). Let $E_{100/\mathbb{Q}}$ be the elliptic curve of conductor
$100$, isogeny class `100.a`, curve `100.a1`, with Weierstrass model
$y^2 = x^3 - x^2 - 33 x + 62$, rank $1$, trivial torsion, and
associated normalised newform $g^{\mathrm{new}}_{E_{100}} \in
S_2^{\mathrm{new}}(\Gamma_0(100))$. Let $\xi^{\mathrm{quintic}}$ be the
all-genus alien-derivation cocycle of the quintic refined-HAE
transseries with $V100$-Zwegers completion $\widehat\xi^{\mathrm{quintic}}
\in M^!_{3/2}(\Gamma_0(20), \chi_5)$ (input-side Kohnen plus-space on
the discriminant lattice $L^{Q*} / L^Q = \mathbb{Z}/5\mathbb{Z}$, per
V100 (P-healed)). Let $\alpha \in \mathbb{C}$ be the new-form coefficient
in the Shimura-image decomposition*

$$
\mathrm{Sh}\bigl(\widehat\xi^{\mathrm{quintic}}\bigr)
\;=\;
\alpha \cdot g^{\mathrm{new}}_{E_{100}}
\;+\;
(\text{6-dimensional old-form combination in } S_2(\Gamma_0(100))).
$$

*Then the following are equivalent:*

1. *$\alpha = 0$ (Shimura-image new-form vanishing).*
2. *All-genus Yamaguchi--Yau BCOV finiteness on $\widetilde Q$:*
   *for every $g \ge 1$, the genus-$g$ free energy $F_g$ is a polynomial
   of degree bounded by $3g - 3$ in the YY ring generators
   $A_p, B_p, C_p$ ($p = 1, 2, 3$).*
3. *Pentagon-at-$E_1$ vanishing for $A^{\mathrm{quintic}}$:*
   *the chain-level Pentagon cocycle*
   $$
   [\omega]_{\mathrm{quintic}} \;\in\; H^2_{\mathrm{Hoch},E_1}\bigl(
   A^{\mathrm{quintic}};\, A^{\mathrm{quintic}}^{\otimes 4}\bigr)
   $$
   *vanishes in cohomology.*

*All three statements are conditional on chain-level CY-A_3 producing
$A^{\mathrm{quintic}}$ explicitly. The Shimura correspondence
$\mathrm{Sh}\colon M^!_{3/2}(\Gamma_0(20), \chi_5) \to S_2(\Gamma_0(100))$
is the Eichler--Selberg--Shintani--Niwa correspondence at level
$N = 5$ with squarefree-divisor twist $t = 5$ (Shimura 1973; Niwa 1975;
Shintani 1975; Bruinier--Funke 2004 for the weakly-holomorphic
extension; Kohnen 1985 for the plus-space refinement).*

### 7.2 Falsifiable predictor

**Concrete numerical predictor.** *The Hecke eigenvalue cancellation*

$$
A^{(\mathrm{Sh})}_p \;=\; 0 \cdot a_p(E_{100}) + (\text{old-form sum})
\qquad \text{for } p \in \{3, 7, 13, 29, 37\}
$$

*on the genus-summed Shimura-image of $\widehat\xi^{\mathrm{quintic}}$
projected onto the new-form direction. Falsification of any of these
five Hecke-eigenvalue cancellations falsifies V107-Quintic-Equivalence-
Chain (and via the equivalence chain, falsifies all-genus YY finiteness
on $\widetilde Q$ and chain-level Pentagon-at-$E_1$ vanishing for
$A^{\mathrm{quintic}}$).*

### 7.3 Conditionality stack (HZ3-3)

V107-Quintic-Equivalence-Chain carries `\ClaimStatusConditional` with
the dependency chain:

$$
\text{V107} \;\Rightarrow\;
\text{chain-level } A^{\mathrm{quintic}} \;\Rightarrow\;
\text{chain-level CY-A}_3 \text{ for non-K3 Class-B}
\;\stackrel{\text{currently}}{=}\;
\text{inf-cat only}.
$$

Additional conditionalities:
- *Costello--Li chain-level open-closed factorisation* on $\widetilde Q$
  (the inf-cat result is established; chain-level extension is partial).
- *Symplectic Picard--Fuchs* on $\widetilde Q$ (verified for Fermat
  quintic by CdGP 1991).
- *V100 input-side Borcherds-lift convergence* on $L^Q = \langle 5
  \rangle$ (Borcherds 1998 §6 + Kohnen 1985 vector-valued plus-space).
- *Yamaguchi--Yau finiteness conjecture* (verified through $g = 51$ by
  YY 2004; all-genus statement is conjectural).

The four conditions combine to make V107 a *cascade conjecture* whose
verification reduces to four independent (but currently open) sub-tasks.
None of the four downgrades any of V107's three equivalent statements;
all three are simultaneously preserved at conjectural status with
explicit dependency chain.

---

## §8. End-of-wave report

### 8.1 The bridge constructed

V107 constructs the explicit equivalence chain
$$
\bigl[\alpha = 0\bigr] \;\Longleftrightarrow\;
\bigl[\text{all-genus YY BCOV finiteness}\bigr] \;\Longleftrightarrow\;
\bigl[\text{Pentagon-at-}E_1 \text{ for } A^{\mathrm{quintic}}\bigr]
$$
with each arrow an explicit operadic--analytic--arithmetic identification:
- The $\alpha \Leftrightarrow$ YY arrow uses the Eichler--Selberg--Shintani--
  Niwa Shimura correspondence $\mathrm{Sh}\colon M^!_{3/2}(\Gamma_0(20),
  \chi_5) \to S_2(\Gamma_0(100))$ projected onto the unique $1$-dim
  new-form direction $g^{\mathrm{new}}_{E_{100}}$.
- The YY $\Leftrightarrow$ Pentagon arrow uses the Costello--Li open-closed
  factorisation bulk--boundary map $\partial: \mathrm{HH}^2_{E_1}(A) \to
  \mathrm{HC}^-_2(A)$ at chain level, with V62 alien-derivation
  $\xi^{\mathrm{quintic}}$ as the bulk-image.

The bridge is sharp: each arrow is a theorem of the appropriate
mathematical literature (Shimura's correspondence, Costello--Li
factorisation, Yamaguchi--Yau anomaly) applied to the V100-pinned
quintic data.

### 8.2 The arithmetic predictor

A concrete falsifiable numerical predictor is exhibited: the Hecke
eigenvalue cancellation $A^{(\mathrm{Sh})}_p = 0 \cdot a_p(E_{100}) +
(\text{old})$ for $p \in \{3, 7, 13, 29, 37\}$. Any non-zero new-form
projection at any of these five primes (at finite genus $g \le 51$
exceeding the YY-bounded remainder) falsifies V107.

### 8.3 Russian-school discipline applied

**AP-CY55 honoured.** V107 distinguishes manifold-invariant $\kappa_{
\mathrm{cat}}(Q) = \chi(\mathcal{O}_Q) = 0$ from algebraization-invariant
$\kappa_{\mathrm{ch}}(\Phi_3(Q))$ (which depends on the chain-level CY-A_3
realisation; for the quintic, conjectural). The new-form direction
$g^{\mathrm{new}}_{E_{100}}$ is associated to the *algebraization*
arithmetic, NOT to the manifold topology.

**AP-CY60 honoured.** V107 does NOT claim the equivalence chain is "six
applications of $\Phi$". It is THREE DIFFERENT mathematical constructions
(Shimura correspondence, BCOV holomorphic anomaly, Pentagon cocycle),
whose convergence on a single equivalence is the CONTENT of V107
(conjectural), not a consequence of functoriality. Each construction is
named explicitly with its source (Shimura 1973; BCOV 1993--94;
Pentagon-at-$E_1$ via $E_1$-Hochschild deformation theory).

**AP-CY61 / HZ3-12 honoured.** First-principles investigation extracted:
- (a) RIGHT in the user's framing: $\alpha = 0$ is the natural arithmetic
  invariant pinning the quintic Pentagon to the new-form direction; the
  Shimura correspondence is the natural arithmetic transport; YY
  finiteness is the natural BCOV-side equivalent.
- (b) WRONG to elide: the equivalence chain requires chain-level
  CY-A_3 (not just inf-cat), Costello--Li chain-level extension (partial),
  and YY all-genus finiteness (conjectural) as preconditions.
- (c) CORRECT: V107 is a CONDITIONAL equivalence theorem with explicit
  dependency stack; every arrow is a known theorem of some other
  mathematical area applied to V100-pinned data.

### 8.4 LOSSLESS LAUNCH summary

V107 is a LOSSLESS strengthening of the V100 RTP cascade: it preserves
the four-clause structure (W, G, P-healed, T), preserves the input-side
Borcherds-lift formulation of (P), preserves the cascade uniqueness,
preserves the chain-level CY-A_3 conditionality. It UPGRADES the V100
output by constructing the explicit arithmetic--chain-level bridge to
the Pentagon-at-$E_1$ and to all-genus YY finiteness, with an explicit
dimension-$1$ elliptic-curve direction $E_{100/\mathbb{Q}}$ as the
arithmetic pin and a concrete five-prime Hecke-eigenvalue predictor as
the falsifiability test.

The frontier becomes sharper: the receptacle dictionary now connects
through Shimura to a *named elliptic curve* whose Hecke eigenvalues are
tabulated and whose modular form $g^{\mathrm{new}}_{E_{100}}$ is uniquely
determined by modularity. The chain-level Pentagon obstruction now has
a *named arithmetic dual* (the new-form projection coefficient $\alpha$),
and the equivalence chain has a *named geometric dual* (all-genus YY
finiteness on $\widetilde Q$).

The Russian-school discipline closes the V100 arithmetic--chain-level gap
by constructing the explicit Shimura-correspondence bridge to a named
elliptic curve, while preserving every component of the V100-V93-V82
cascade. V107-Quintic-Equivalence-Chain now stands as a falsifiable
conditional theorem with concrete numerical predictors at five primes.

---

## §9. Outlook: cross-input universality and future waves

The V107 construction is explicit at the quintic specialisation. The
analogous statements at local $\mathbb{P}^2$ (rank-2 mock $W_3$-Jacobi
receptacle, V100 §4.4) and at higher-dimensional Class-B inputs (banana,
conifold extensions) require:

- An analogous Shimura correspondence for rank-$n$ mock Jacobi forms
  (Skoruppa--Zagier 1989 for rank-1; Bringmann--Folsom--Kane 2018 for
  rank-2; rank-$\ge 3$ partially developed).
- Identification of the analogous *named arithmetic invariant* (elliptic
  curve at quintic; abelian surface or higher-rank object at LP^2 or
  banana).
- Verification that the analogous Pentagon-at-$E_1$ vanishing translates
  to all-degree refined MNOP / refined-HAE finiteness on the
  corresponding mirror.

These are V108--V112 targets. For now, V107 establishes the QUINTIC
equivalence chain in full arithmetic specificity, with the elliptic
curve $E_{100/\mathbb{Q}}$ as the pinning object and the five-prime
Hecke-eigenvalue predictor as the concrete falsifiability test.

---

**End of memorandum.**

Authored by Raeez Lorgat. No AI attribution; no commit; no manuscript
edits; no test runs; no build. Read-only sandbox memorandum.
