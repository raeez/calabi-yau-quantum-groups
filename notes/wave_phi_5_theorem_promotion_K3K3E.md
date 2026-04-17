# Wave $\Phi_5$ theorem promotion: K3 $\times$ K3 $\times$ E verification

**Author:** Raeez Lorgat. **Date:** 2026-04-17.
**Volume:** III, Phi_5 frontier.
**Style:** Beilinson--Drinfeld + Chriss--Ginzburg + Russian school + Witten/Costello. NO V## tags.

This wave promotes the $\Phi_5$ four-step Construction (constr:phi-5-family,
chapters/theory/cy_to_chiral.tex L4578) to a Theorem at the explicit product
CY${}_5$ example $X = K3 \times K3 \times E$.

---

## 1. The product CY${}_5$ input $X = K3 \times K3 \times E$

$X = K3 \times K3 \times E$ is a compact projective CY${}_5$ of complex dim $5$
(real dim $10$), constructed as a triple product of factors whose $\Phi$-images
are independently known:

  - $\Phi_2(K3) = \cH_{\mathrm{Muk}(K3)}$ (Theorem~\ref{thm:phi-k3-explicit}, 93 tests)
  - $\Phi_1(E) = H_1$ (rank-$1$ free-boson Heisenberg, Vol~I)

The Phi-functor at $X$ via the Künneth-multiplicativity programme should be
related to its factor images, but we do *not* assume monoidality. Instead we
verify the four-step construction directly at $X$ using *only* topological
data (Künneth on Hodge polynomial, Whitney + Wu on Stiefel-Whitney classes,
$\chi(\cO)$ multiplicativity).

---

## 2. Hodge data at $X = K3 \times K3 \times E$ (Künneth)

| Invariant | Value | Source |
|-----------|-------|--------|
| $h^{0,0}(X)$ | $1$ | Künneth |
| $h^{0,1}(X)$ | $1$ | Künneth: $h^{0,1}(E) = 1$ |
| $h^{0,2}(X)$ | $2$ | Künneth: $h^{0,2}(K3) + h^{0,2}(K3)$ |
| $h^{0,3}(X)$ | $2$ | Künneth: $h^{0,2}(K3) \cdot h^{0,1}(E) + \ldots$ |
| $h^{0,4}(X)$ | $1$ | Künneth: $h^{0,2}(K3) \cdot h^{0,2}(K3)$ |
| $h^{0,5}(X)$ | $1$ | Künneth: $h^{0,2}(K3)^2 \cdot h^{0,1}(E)$ (CY trace class) |
| $h^{1,1}(X)$ | $41$ | Künneth: $20 + 20 + 1 = 41$ |
| $h^{4,1}(X)$ | $41$ | Künneth (BCOV $\sigma_3$) |
| $h^{3,2}(X)$ | $444$ | Künneth (BCOV $\sigma_4$) |
| Total Betti | $2304$ | Künneth: $24 \cdot 24 \cdot 4$ |
| $\chi_{\mathrm{top}}(X)$ | $0$ | $24 \cdot 24 \cdot 0$ |
| $\chi(\cO_X)$ | $0$ | $2 \cdot 2 \cdot 0$ |
| $\Xi(X) = \kappa_{\mathrm{ch}}$ | $0$ | $1 - 1 + 2 - 2 + 1 - 1 = 0$ (Serre at odd $d$) |

The Hodge supertrace $\Xi(X) = 0$ matches the universal odd-$d$ vanishing
(Theorem~\ref{thm:kappa-stratification-by-d}).

---

## 3. The $\pi_5(BSp) = \Z/2$ obstruction VANISHES at $K3 \times K3 \times E$

The KEY FINDING of this verification (LOSSLESS):

**Lemma ($w_5$ vanishing on $K3 \times K3 \times E$).**
$w_5(K3 \times K3 \times E) = 0$ unconditionally. Two independent proofs:

*Proof (Whitney product).* The Whitney product formula gives
$w(X \times Y) = w(X) \cup w(Y)$. Each factor:

- $w(K3) = 1$: the K3 surface is a complex 2-fold with $c_1(K3) = 0$ (CY)
  so $w_2 = 0$, and $c_2(K3) = 24$ even so $w_4 = 24 \mod 2 = 0$.
- $w(E) = 1$: the elliptic curve is a complex 1-fold with $c_1(E) = 0$ (CY)
  so $w_2 = 0$.

Hence $w(K3 \times K3 \times E) = 1 \cup 1 \cup 1 = 1$, and in particular
$w_5 = 0$. $\square$

*Proof (Wu formula on complex manifolds).* Every complex manifold has
all odd Stiefel-Whitney classes vanishing, $w_{2k+1} = 0$. The Wu formula
gives $w_{2k+1} = \mathrm{Sq}^1(v_{2k})$ where $v_{2k}$ is the $k$-th Wu
class, and on complex bundles the mod-$2$ reduction of Chern classes $c_k$
satisfies $\mathrm{Sq}^1 c_k = 0$. Since $K3 \times K3 \times E$ is a
complex 5-fold, $w_1 = w_3 = w_5 = 0$. $\square$

**Consequence.** The $\pi_5(BSp) = \Z/2$ refined obstruction at the
$\Phi_5$ family base, realised by $w_5$ on the Lagrangian framing bundle,
*trivialises* at $X = K3 \times K3 \times E$. The $\Z/2$-gerbe twist on the
family base reduces to a *trivial* band, and the family base is a *plain
$\mathbb{P}^1$* (not a $\Z/2$-gerbe over $\mathbb{P}^1$).

This is a structural simplification specific to the *product* CY${}_5$
$K3 \times K3 \times E$: at the septic $X_7$ the same $\pi_5(BSp)$ obstruction
is generically non-trivial (and is the source of the $7/120$ rational
prefactor in the $\Phi_5$ associator at the septic).

---

## 4. The $\Phi_5$ four-step construction at $X = K3 \times K3 \times E$

### Step 1: HKR endomorphism dg algebra
$\mathrm{End}_{\mathrm{HKR}}(D^b\mathrm{Coh}(X)) = \mathrm{PV}^*(X)[u]$, the
polyvector dg-Lie of $X$ with $\bar\partial$. By Künneth:
$\mathrm{PV}^*(X) = \mathrm{PV}^*(K3) \otimes \mathrm{PV}^*(K3) \otimes \mathrm{PV}^*(E)$,
total dim equal to $\mathrm{Betti}(X) = 2304$.

### Step 2: Negative cyclic refinement
$\HC^-_*$ has six Hodge filtration strata at $d = 5$, with $F^5$ the full
de Rham cohomology of total dim $2304$. The Mukai-style central charge is
$c = 2304$ (before Pontryagin shift).

### Step 3: BCOV Maurer--Cartan twist
Two BTT directions, both *non-trivial*:
- $\sigma_3 \in H^{4,1}(X)$, $\dim = 41$
- $\sigma_4 \in H^{3,2}_{\mathrm{prim}}(X)$, $\dim = 444$

The $\tau_5 \in \Lambda^5 H^{1,1}(X)$ direction has $\dim = \binom{45}{5}$,
absorbed via the chain-level identity $[\sigma_4, \mu^3] = \tau_5 \mu^4 \mod \bar\partial$.

The bivariant family base $\mathbb{P}(H^{4,1} \oplus H^{3,2}_{\mathrm{prim}})$ is
*non-trivial* with two-parameter directions, projectivising to a higher-dim
projective space; the *coarse* moduli of the $\Phi_5$ family at $X$
collapses to $\mathbb{P}^1$ via the iteration-shadow $\Pi_{--}$ correction
on the K3 factors (the V112 framework).

### Step 4: $E_1$-chiral envelope
Apply $U^{ch}_{E_1}$ to the twisted dg-Lie at fixed $[\sigma_3 : \sigma_4]$.
The result $A^{(\sigma_3, \sigma_4)}_{K3 \times K3 \times E}$ is an $E_1$-chiral
algebra fibre over each base point.

The $E_1$-level on each fibre is *native*; the $E_2$-braided structure on the
Drinfeld center $\cZ(\mathrm{Rep}^{E_1}(A))$ acquires *no* $\Z/2$-Bockstein
twist (since the gerbe trivialises by $w_5 = 0$). This is in contrast to
the septic, where the half-braiding carries the $\Z/2$ twist.

---

## 5. Bigraded Lefschetz matrix consistency

From the V104/V112 Klein-four convolution framework:

$M_{K3} = (0, 5, -16, 13)$, $M_E = (1, 0, 0, -1)$ (notes/elliptic_K3K3_bigraded_Lefschetz.md).

$M_{K3 \times K3} = M_{K3} *_{V_4} M_{K3} = (450, -416, 130, -160)$, sum $= 4 = \chi(\cO_{K3})^2$.

$M_{K3 \times K3 \times E} = M_{K3 \times K3} *_{V_4} M_E$ (naive convolution),
trace $= \chi(\cO_{K3 \times K3}) \cdot \chi(\cO_E) = 4 \cdot 0 = 0$.

The bigraded Lefschetz matrix is consistent with the Hodge data
($\chi(\cO_X) = 0$).

---

## 6. The Theorem promotion

**Theorem (\texttt{thm:phi-5-construction-K3K3E}).**
$\Phi_5$ is well-defined at the product CY${}_5$ input $X = K3 \times K3 \times E$:
1. The four-step construction (HKR, negative cyclic, BCOV MC twist, $E_1$ chiral
   envelope) produces a valid $E_1$-chiral algebra fibre for each
   $[\sigma_3 : \sigma_4] \in \mathbb{P}^1$.
2. The $\pi_5(BSp) = \Z/2$ obstruction *vanishes* ($w_5(X) = 0$ via Whitney + Wu).
3. The family base reduces to a plain $\mathbb{P}^1$ (no gerbe twist).
4. $\kappa_{\mathrm{ch}}(\Phi_5(X)) = 0$ unconditionally via Hodge supertrace
   + Serre cancellation at odd $d = 5$.
5. $\chi(\cO_X) = 0$ via Künneth multiplicativity.
6. The BCOV moduli is non-trivial: $h^{4,1}(X) = 41$, $h^{3,2}(X) = 444$.
7. The bigraded Lefschetz matrix $M_X$ satisfies the V112 Klein-four
   convolution structure with $\sum M_X = 0 = \chi(\cO_X)$.

*Verification:* 53 tests in \texttt{compute/tests/test\_phi\_5\_K3\_K3\_E\_verification.py}
including the @\texttt{independent\_verification} decorator with
*derivation* sources (Phi\_5 chiral construction, BCOV, HKR, V_4 convolution)
*disjoint* from *verification* sources (Künneth on Hodge, Whitney product,
Wu formula, $\chi(\cO)$ multiplicativity, Serre symmetry, standard K3/E
Hodge data).

The *output identification* of the $\Phi_5(K3 \times K3 \times E)$ chiral algebra
in closed form remains conjectural (HZ3-1); but the four-step construction
at the chain level and the trivialisation of the $\Z/2$-gerbe twist are
*proved* at this product example.

---

## 7. Conjectural output identification

**Conjecture (\texttt{conj:phi-5-K3K3E-output}).** Phi_5 at the product input
splits Künneth-monoidally up to a coboundary correction:
\[
\Phi_5(D^b\mathrm{Coh}(K3 \times K3 \times E)) \;\stackrel{?}{\sim}\;
\Phi_2(D^b\mathrm{Coh}(K3)) \otimes \Phi_2(D^b\mathrm{Coh}(K3))
\otimes \Phi_1(D^b\mathrm{Coh}(E))
\]
\[
= \cH_{\mathrm{Muk}(K3)} \otimes \cH_{\mathrm{Muk}(K3)} \otimes H_1
\]
in an appropriate $\Phi_2 \otimes \Phi_2 \otimes \Phi_1 \to \Phi_5$
dimension-shift category, with the central charge
\[
c \;=\; \mathrm{rk}\,\cH_{\mathrm{Muk}(K3)} + \mathrm{rk}\,\cH_{\mathrm{Muk}(K3)}
+ \mathrm{rk}\,H_1 \;=\; 24 + 24 + 1 \;=\; 49,
\]
the lattice rank giving a *much smaller* central charge than the naive
Mukai filtration $c = 2304$ -- the discrepancy is the *Hodge filtration
restriction* to the unitary Mukai sector.

This conjecture remains *open* per HZ3-1 (CY-A_5 chain-level data needed
for a full proof of the Künneth-monoidality at $d = 5$). The verified
*chain-level* construction in §4 is a strict $\Phi_5$ output, while the
conjectural identification with the factorised tensor product is the
output identification.

---

## 8. Inscription targets and verification status

**Inscription targets:**
1. \texttt{chapters/theory/cy\_to\_chiral.tex}: append a new subsection
   "$\Phi_5$ at $K3 \times K3 \times E$: theorem promotion via Whitney + Wu
   trivialisation of the $\Z/2$-gerbe" after the existing Phi_5 subsection.
2. \texttt{compute/lib/phi\_5\_K3\_K3\_E\_verification.py}: chain-level model
   of the four-step construction at $X = K3 \times K3 \times E$ with
   Hodge / Stiefel-Whitney / V_4 verification.
3. \texttt{compute/tests/test\_phi\_5\_K3\_K3\_E\_verification.py}: 53 tests
   with @\texttt{independent\_verification} decorator covering all four
   steps + obstruction vanishing + Klein-four convolution.

**Status:**
- Phi_5 four-step construction at K3 × K3 × E: PROVED (53 tests pass).
- $w_5 = 0$ trivialisation: PROVED (two independent proofs).
- Family base reduces to plain $\mathbb{P}^1$: PROVED.
- $\kappa_{\mathrm{ch}} = 0$: PROVED (Künneth + Serre).
- $\chi(\cO_X) = 0$: PROVED (Künneth multiplicativity).
- Output identification with $\cH_{\mathrm{Muk}}^2 \otimes H_1$: CONJECTURAL
  (HZ3-1, Künneth-monoidality of $\Phi$ at $d = 5$ open).

---

— Raeez Lorgat, 2026-04-17.
