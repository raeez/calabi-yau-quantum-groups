# 3B-C06 — Hecke--Borcherds (HB) identity: numerical verification at primitive real-simple-root pairs

## Terminal state

**C (fails).** The Hecke--Borcherds structure-constant identity
\[
  c(4n_1m_1 - l_1^2) \cdot c(4n_2m_2 - l_2^2) \cdot \langle \alpha_1, \alpha_2 \rangle_{II}
  \;=\;
  c(4nm - l^2) \cdot N^{\mathrm{HN}}_{\Delta_5}(\alpha_1, \alpha_2)
\]
does **not** hold numerically at any of the three primitive
real-simple-root pairs
$(\delta_i, \delta_j)$ with $i \neq j$. The numerical failure is
structural, not a sign/normalisation artefact: the ratio
$|\mathrm{LHS}|/|\mathrm{RHS}|$ is identical (and non-unit) at all three
pairs, because the Fourier labels $(n_i, l_i, m_i)$ C06 attaches to
$\delta_1, \delta_2, \delta_3$ all yield the same discriminant $D = 3$
and the same pair discriminant $D_{\mathrm{sum}} = 11$, regardless of
which permutation of real simple roots one chooses.

State C is the correct terminal state for this item at this level of the
statement. Promotion to A requires the (HB) identity to be restated with
its proper scope restriction — to **imaginary**-root pairs — and then
verified there; on the real-simple-root sector, (HB) is not merely
unproved, it is **false as stated**.

## Setup

### Lattice and basis

$\Lambda^{2,1}_{II}$ in basis $(f_2, f_3, f_{-2})$ with bilinear form
\[
  B = \begin{pmatrix} 0 & 0 & -1 \\ 0 & 2 & 0 \\ -1 & 0 & 0 \end{pmatrix}
  \qquad
  \Big(
    (f_2, f_2) = (f_{-2}, f_{-2}) = 0,\ (f_3, f_3) = 2,\
    (f_2, f_{-2}) = -1,\
    (f_2, f_3) = (f_{-2}, f_3) = 0
  \Big).
\]
Source: \texttt{chapters/examples/k3e\_bkm\_chapter.tex} lines 619--630.

### Three primitive real simple roots

From Gritsenko--Nikulin 1998 §2, realised in
\texttt{chapters/examples/k3e\_bkm\_chapter.tex} line 625:
\[
  \delta_1 = 2 f_2 - f_3,
  \qquad
  \delta_2 = 2 f_{-2} - f_3,
  \qquad
  \delta_3 = f_3.
\]
Gram matrix
\[
  \bigl((\delta_i, \delta_j)\bigr)_{i, j = 1, 2, 3}
  \;=\;
  \begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{pmatrix}
  \;=\;
  \mathrm{diag}(2, 2, 2) - 2(E - I),
\]
signature $(2, 1)$, eigenvalues $\{-2, 4, 4\}$.

### C06 Fourier parameterisation

Per C06 lines 112--113,
\[
  \alpha \;=\; (n - 1) f_2 - (l - 1) \tfrac{1}{2} f_3 + (m - 1) f_{-2}.
\]
Inverting: for $\alpha = a f_2 + b f_3 + c f_{-2}$,
\[
  n = a + 1, \qquad l = 1 - 2b, \qquad m = c + 1, \qquad D = 4nm - l^2.
\]

Apply to each real simple root:
\[
  \begin{array}{lclcl}
    \delta_1 = (2, -1, 0) & \mapsto & (n, l, m) = (3, 3, 1) & \Rightarrow & D = 12 - 9 = 3, \\
    \delta_2 = (0, -1, 2) & \mapsto & (n, l, m) = (1, 3, 3) & \Rightarrow & D = 12 - 9 = 3, \\
    \delta_3 = (0, 1, 0)  & \mapsto & (n, l, m) = (1, -1, 1) & \Rightarrow & D = 4 - 1 = 3.
  \end{array}
\]
All three Fourier labels give $D = 3$.

### K3 elliptic genus Fourier coefficients

Manuscript-canonical values from
\texttt{chapters/examples/k3e\_bkm\_chapter.tex}
Proposition~\texttt{prop:k3e-super-grading} (lines 1031--1034):
\[
  \begin{array}{c|ccccccccc}
    D & -1 & 0 & 3 & 4 & 7 & 8 & 11 & 12 & 15 \\ \hline
    c(D) & 2 & 10 & -64 & 108 & -513 & 808 & -2752 & 4016 & -11775
  \end{array}
\]

The user-provided values in the prompt ($c(-1) = 2$, $c(0) = 20$,
$c(3) = 180$, $c(4) = 924$, $c(7) = 5728$) do **not** match the
manuscript's canonical Fourier coefficients of $\phi_{0,1}^{K3}$ and do
not uniformly match either Eichler--Zagier 1985 Theorem~9.3 or Cheng
2010 Mathieu-moonshine $H(\tau)$ expansion values
($2, 90, 462, 1540, 4554, 11592, \ldots$ in the Mathieu convention, with
variants double-counted to $2, 180, 924, 3080, 9108, \ldots$). The
identity is tested below with **both** the manuscript-canonical values
and the user-provided values. The identity fails in both.

## Three pairs and their Fourier data

### Pair 1: $(\alpha_1, \alpha_2) = (\delta_1, \delta_2)$

- $\alpha_1 + \alpha_2 = 2 f_2 - 2 f_3 + 2 f_{-2}$
- Fourier label: $(N, L, M) = (3, 5, 3)$
  (correcting the C06 line 123 formula:
  $L = l_1 + l_2 - 1 = 3 + 3 - 1 = 5$; the C06 statement "$L = l_1 + l_2$" is a typo relative to direct lattice
  addition and the shift convention $\alpha_i = (n_i - 1) f_2 - (l_i - 1)(1/2) f_3 + (m_i - 1) f_{-2}$)
- $D_{\mathrm{sum}} = 4 \cdot 3 \cdot 3 - 5^2 = 11$
- $\langle \delta_1, \delta_2 \rangle_{II} = -2$

### Pair 2: $(\alpha_1, \alpha_2) = (\delta_1, \delta_3)$

- $\alpha_1 + \alpha_2 = 2 f_2 + 0 \cdot f_3 + 0 \cdot f_{-2}$
- Fourier label: $(N, L, M) = (3, 1, 1)$
- $D_{\mathrm{sum}} = 4 \cdot 3 \cdot 1 - 1 = 11$
- $\langle \delta_1, \delta_3 \rangle_{II} = -2$

### Pair 3: $(\alpha_1, \alpha_2) = (\delta_2, \delta_3)$

- $\alpha_1 + \alpha_2 = 0 \cdot f_2 + 0 \cdot f_3 + 2 f_{-2}$
- Fourier label: $(N, L, M) = (1, 1, 3)$
- $D_{\mathrm{sum}} = 4 \cdot 1 \cdot 3 - 1 = 11$
- $\langle \delta_2, \delta_3 \rangle_{II} = -2$

**Observation.** $S_3 = \mathrm{Aut}(\mathcal{P}_{II})$ acts transitively
on the three pairs (line 674 of the chapter), so $D_{\mathrm{sum}} = 11$
and $\langle \cdot, \cdot \rangle = -2$ on every pair.

## Parity and $N^{\mathrm{HN}}_{\Delta_5}$

Per C06 lines 151--154 and
\texttt{chapters/theory/quantum\_groups\_foundations.tex}
\texttt{prop:qgfnd-gd5-super-grading}: bosonic if $D \equiv 0 \pmod 4$,
fermionic if $D \equiv 3 \pmod 4$. All three $\delta_i$ have $D = 3$,
fermionic.

$N^{\mathrm{HN}}_{\Delta_5}(\alpha_1, \alpha_2)
= \epsilon(\alpha_1, \alpha_2) \bigl(1 - (-1)^{(|\alpha_1|, |\alpha_2|)}\bigr)
= \pm (1 - (-1)^{1 \cdot 1}) = \pm 2$.

$|N^{\mathrm{HN}}| = 2$ on every fermion-fermion pair.

## Numerical verification

### With manuscript-canonical $c(D)$

$c(3) = -64$, $c(11) = -2752$.

\[
  \begin{array}{l|rrr}
    & \text{LHS} = c(D_1) c(D_2) \langle \cdot, \cdot \rangle_{II}
    & \text{RHS} = c(D_{\mathrm{sum}}) \cdot N^{\mathrm{HN}}
    & |\text{LHS}|/|\text{RHS}| \\ \hline
    (\delta_1, \delta_2)
    & (-64)(-64)(-2) = -8192
    & (-2752)(\pm 2) = \mp 5504
    & 8192/5504 = \mathbf{64/43} \\
    (\delta_1, \delta_3)
    & (-64)(-64)(-2) = -8192
    & (-2752)(\pm 2) = \mp 5504
    & 64/43 \\
    (\delta_2, \delta_3)
    & (-64)(-64)(-2) = -8192
    & (-2752)(\pm 2) = \mp 5504
    & 64/43
  \end{array}
\]

The ratio $64/43$ is not a unit, not a simple rational indicating a
normalisation factor, and is identical on all three pairs (by the
$S_3$-symmetry). Identity (HB) **fails at every real-simple-root pair**.

### With user-provided $c(D)$

$c(3) = 180$. $c(11)$ not provided; tested at plausible candidates:

\[
  \begin{array}{l|rrr}
    c(11) & \text{LHS} & \text{RHS} = c(11) \cdot 2 & |\text{LHS}|/|\text{RHS}| \\ \hline
    3080 & (180)(180)(-2) = -64800 & \pm 6160  & 10.52 \\
    2752 & -64800                  & \pm 5504  & 11.77 \\
    5728 & -64800                  & \pm 11456 & 5.66
  \end{array}
\]

Identity **fails** under every candidate $c(11)$. No rational
normalisation of the user's $c$-sequence recovers unit ratio.

### In the unshifted Fourier convention

If one replaces the C06 shifted parameterisation
$\alpha = (n-1)f_2 - (l-1)(1/2)f_3 + (m-1)f_{-2}$
with the direct lattice parameterisation
$\alpha = n f_2 + l (1/2 f_3) + m f_{-2}$
(for which $\mathrm{mult}_{\mathrm{BKM}}(\alpha) = c(-\alpha^2/2)$ is the
consistent BKM-root-space formula on imaginary roots), then each real
simple root has Fourier label $D_{\mathrm{unshifted}} = -4$, and
$c(-4) = 0$ (outside the support of $\phi_{0,1}^{K3}$). Then
$\mathrm{LHS} = 0 \neq \pm 20 = \mathrm{RHS}$
(using $c(D_{\mathrm{sum,unshifted}} = 0) = 10$, $N^{\mathrm{HN}} = 2$).
Identity **fails more dramatically** in the unshifted convention.

## Structural diagnosis

The failure is not a computational error. Three structural reasons.

**(1) Real-simple-root multiplicity is $1$, not $c(D)$.**
For a real simple root $\delta$ of any Kac--Moody or Borcherds algebra,
$\dim \mathfrak{g}_{\delta} = 1$ by definition (Serre generator
$e_\delta$). The Borcherds-product exponent
$\mathrm{mult}(\alpha) = |c(4nm - l^2)|$ in
\texttt{chapters/examples/k3e\_bkm\_chapter.tex} line 814
applies to **imaginary** roots ($\alpha^2 \leq 0$); at real simple roots
($\alpha^2 = 2$), the formula gives $c(-4) = 0$ (unshifted) or
$c(3) = -64$ (shifted), neither of which equals the true multiplicity
$1$. The (HB) identity, built on the formula
$\mathrm{mult}(\alpha) = c(4nm - l^2)$ applied to $\mathrm{LHS}$ factors,
cannot hold at real-simple-root pairs as a numerical arithmetic
identity: the input factors $c(D_i)$ do not encode the correct dimensions.

**(2) The bracket on real-simple-root pairs is Kac--Moody, not
Borcherds.**
For real simple roots $\delta_i, \delta_j$ with Cartan matrix entry
$a_{ij} = (\delta_i, \delta_j) = -2$, the bracket
$[e_{\delta_i}, e_{\delta_j}]$ sits in the root space
$\mathfrak{g}_{\delta_i + \delta_j}$, which is governed by the
**Kac--Moody Serre relation** $(\mathrm{ad}\, e_i)^{1 - a_{ij}} e_j = 0$,
i.e., $(\mathrm{ad}\, e_i)^3 e_j = 0$ at $a_{ij} = -2$. The structure
constant at $[e_{\delta_i}, e_{\delta_j}]$ is a Kac--Moody normalisation
constant (often taken $= 1$ in a Chevalley basis), not an arithmetic
combination of $\phi_{0,1}^{K3}$ Fourier coefficients. The (HB) identity
encodes an arithmetic relation on **imaginary-root** brackets (where
Borcherds BKM combinatorics dictates structure constants via
$\phi_{0,1}^{K3}$); applying it to real-simple-root pairs conflates two
incompatible bracket regimes.

**(3) Permutation-invariance under $S_3$.**
The three real simple roots are $S_3$-permuted by
$\mathrm{Aut}(\mathcal{P}_{II})$; consequently, all three pairs
$(\delta_i, \delta_j)$ with $i \neq j$ yield identical numerical LHS,
RHS, and ratio. The ratio $64/43$ is a group-invariant arithmetic
obstruction, not a sporadic numerical coincidence. Any identity that is
supposed to hold for "every pair of BPS-primitive roots" must, in
particular, hold for the three $S_3$-related pairs on the
real-simple-root sector; it does not.

## Corrected statement (pathway to future closure)

The (HB) identity as stated in C06 should be **restricted** to
imaginary-root pairs:

> **Hecke--Borcherds identity, imaginary-root scope.** For every pair
> $(\alpha_1, \alpha_2)$ of **imaginary** primitive roots
> ($\alpha_1^2 \leq 0$, $\alpha_2^2 \leq 0$) with
> $\alpha_1 + \alpha_2$ in the positive BPS cone,
> $c(D_1) c(D_2) \langle \alpha_1, \alpha_2 \rangle_{II}
> = c(D_{\mathrm{sum}}) N^{\mathrm{HN}}_{\Delta_5}(\alpha_1, \alpha_2)$.

Three pieces of evidence support the imaginary-root-only scope.

(i) The Borcherds denominator identity
$\prod_{\alpha > 0} (1 - e^{-\alpha})^{\mathrm{mult}(\alpha)} =
\sum_w \mathrm{sgn}(w) w(e^{-\rho} \Delta_5^{-1})$
of Gritsenko--Nikulin 1998 §3 Theorem~3.1 is a statement about the
**full** positive root cone, but the **bilinear** structure constants
extracted from logarithmic differentiation live on the imaginary-root
sector. The real-simple-root contributions factor out as the Weyl-sum
$e^{-\rho}$ piece.

(ii) The Davison PBW theorem
(Davison 2017, \emph{Proc.~LMS}~112 Theorem~1.1;
Davison--Meinhardt 2020, \emph{Invent.~Math.}~221 Theorem~A) identifies
$\mathfrak{g}_{\mathrm{BPS}, \gamma}$ as the BPS Lie algebra at charge
$\gamma$. The "primitive" in
"primitive BPS roots $\alpha_\gamma$" in the Oberdieck--Pixton
identification means primitive in the DT/Hilbert-scheme sense, not
"real simple" in the Kac--Moody sense. The $\mathfrak{g}_{\mathrm{BPS}}$
side has no "real simple roots" as a distinguished Kac--Moody
substructure; its roots are all BPS charges, and its bracket is the
semi-classical Hall bracket governed by the skew Euler form and BPS
multiplicities.

(iii) On the $\mathfrak{g}_{\Delta_5}$ side, the real simple roots are a
**distinct** structural input (generators of the Kac--Moody base
$F_3 \subset \mathfrak{g}_{\Delta_5}$, per
Proposition~\texttt{prop:bkm-delta5-real-cartan-is-F3} in
\texttt{k3e\_bkm\_chapter.tex}). They are not encoded by the Fourier
coefficients $c(D)$ of $\phi_{0,1}^{K3}$; they are encoded by the Cartan
matrix $\mathrm{diag}(2,2,2) - 2(E - I)$. The correspondence
$\gamma \mapsto \alpha_\gamma$ of Oberdieck--Pixton 2018 Theorem~1
restricts to the imaginary-root sector of $\mathfrak{g}_{\Delta_5}$; it
does not produce real simple roots.

Under the imaginary-root restriction, (HB) becomes a cleaner arithmetic
identity on $\phi_{0,1}^{K3}$ Fourier coefficients and $\Lambda^{2,1}_{II}$
intersections, verifiable by the Gritsenko--Nikulin 1998 denominator
expansion (C06 Route A) or the Harvey--Moore 1996 threshold integral
(C06 Route B). The real-simple-root Kac--Moody relations are a
**separate** input (standard Drinfeld 1985 Yangian Serre relations at
$a_{ij} = -2$; see
\texttt{chapters/examples/k3\_yangian\_chapter.tex} line 2290).

## Impact on C06 closure

- State of C06 moves from **B** (conditional on (HB) verified at all
  primitive root pairs) to **C** (HB as stated is false, because the
  real-simple-root sector is inside the quantified range "every pair"
  but the identity does not hold there).
- A refined C06 can recover state **B** with the restricted hypothesis
  "(HB) for imaginary-root pairs only". This is the pathway forward:
  re-state the identity with its proper scope, then verify numerically
  and/or via Gritsenko--Nikulin 1998 §3 Theorem~3.1 denominator
  logarithmic differentiation.
- The Vol III manuscript's
  \texttt{chapters/examples/coha\_wall\_crossing\_platonic.tex}
  reference to "structure-constant identity on the Gritsenko 1999
  paramodular family" should be reviewed: if the current text claims
  (HB) at full quantified scope, the scope restriction needs to be
  inscribed; if the text already scopes to imaginary roots, no change
  needed.

## Cross-consistency notes

1. **C06 internal typo.** C06 line 123 states
   "$\alpha_1 + \alpha_2 = (n_1 + n_2 - 1, l_1 + l_2, m_1 + m_2 - 1)$".
   Direct lattice addition yields $L = l_1 + l_2 - 1$, not $l_1 + l_2$;
   the C06 expression is off by 1 in the middle slot.
   The three pairs computed above use the corrected lattice-addition
   formula. This correction is minor relative to the structural failure
   of (HB) on real simple roots.

2. **Vol III convention vs.\ Mathieu moonshine.**
   Manuscript $c(D)$ values are Fourier coefficients of
   $\phi_{0,1}^{K3} = q^{-1}(y^{-1} + 10 + y) + O(q)$ (a weak Jacobi
   form). Mathieu moonshine values
   ($2, 90, 462, 1540, 4554, \ldots$ at $D = -1, 3, 7, 11, 15$) are
   different: they come from the mock-modular function $H(\tau)$
   attached to the $M_{24}$ representation content of the K3 elliptic
   genus. The two sequences agree at $D = -1$ ($c = 2$); diverge
   elsewhere (manuscript $c(3) = -64$, Mathieu $A_3 = 90$). The user's
   prompt list ($2, 20, 180, 924, 5728$) partially matches
   $2 \cdot$ Mathieu values ($c(3), c(4)$) but introduces $5728$ which
   matches neither sequence; its provenance is unclear.
   **In both conventions**, (HB) fails at real-simple-root pairs, so
   the convention ambiguity is not the decisive factor.

3. **Pattern-236 ambient-qualifier discipline.** The real-simple-root
   failure is a chain-level arithmetic failure: explicit $c(D)$ values,
   explicit bilinear pairings, explicit rational ratios. The
   $(\infty, 1)$-categorical extension to
   $\Phi_3$-as-functor (Conjecture
   \texttt{conj:harvey-moore-functorial} in
   \texttt{chapters/examples/cy\_c\_six\_routes\_convergence.tex}) is
   untouched by this verification; it concerns the functor on
   $\infty$-categories of CY$_3$-data, not the pointwise Lie-bracket
   identification.

4. **Lorgat 2020 Conjecture 1 unaffected.** The universal Borcherds
   weight identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ holds
   independently of (HB); it is a statement about the weight of
   $\Delta_5 = \Phi_1$ (namely $5$), not about bilinear bracket structure
   constants. Lorgat 2020 Conjecture 1's 8-form atlas survives as
   stated.

5. **Wave-1 A08 reformulation reappraisal.** A08's formulation
   "$c_{\gamma_1} c_{\gamma_2} B(\gamma_1, \gamma_2) = \sum c_\gamma
   \langle \alpha_{\gamma_1}, \alpha_{\gamma_2} \rangle$" was a
   **schematic** version of the identity. The precise (HB) of C06
   sharpens the schematic to an arithmetic identity, and this
   verification now sharpens it further: the precise (HB), applied to
   real simple roots, is false. A future revision should restrict the
   "sum over $\gamma$" in A08 to the imaginary-DT-charge sector only.

## Summary

Three specific pairs tested. All fail. Same $|$LHS$|/|$RHS$| = 64/43$
under the manuscript-canonical $c(D)$ in all three. Structural reason:
on real simple roots, $\mathrm{mult}_{\mathrm{BKM}}(\delta) = 1 \neq c(D)$
for any consistent $D$-labelling, so the identity (HB) as quantified is
false. Corrected scope: imaginary-root pairs only. **Terminal state C.**
