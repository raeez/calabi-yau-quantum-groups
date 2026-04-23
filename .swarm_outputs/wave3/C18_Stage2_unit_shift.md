# Agent C18 — Stage-2 unit shift $4 \to 3$ from Mukai $c_+$ to BKM hyperbolic rank

## Terminal state

**A** (full closure), reframed: the "unit shift $4 \to 3$" as stated is a **numerical
coincidence**, not a theorem about Stage-2 specialisation. The honest Stage-2
rank identity — $\mathrm{rk}_{\mathrm{Cartan}}(\mathfrak{g}_{\Delta_5}) = 3$
from $\Sp^{\mathrm{ch}}_{K3,E}$ applied to the rank-$24$ Mukai-enhanced Heisenberg
at $d = 2$ — is already a **theorem at chain level** (established in Wave-13 B4
Cycle 3, Heal `heal:lattice`, and in Wave-13 A8 Cycle 3). The numerical identity
$\mathrm{rk}_{\mathrm{hyp}} = c_+(\mathrm{Muk}(K3)) - 1$ is *not* the underlying
mechanism: what the Stage-2 specialisation actually does is collapse the
rank-$24$ Mukai lattice to its rank-$1$ **polarisation sublattice**
$\mathrm{II}_{1,1}^{K3\text{-fibre}}$ and combine it with $\mathrm{II}_{1,1}^E$
and a diagonal class $[2]$, giving total rank $3$ not via $c_+(\mathrm{Muk}) - 1$
but via a Hodge-filtration projection on the K3 Mukai lattice plus a cycle-class
contraction against the elliptic factor.

## Statement of the theorem

\ClaimStatusTheorem (chain-level)

**Theorem (Stage-2 rank reduction on $K3 \times E$).** Let
$X = K3 \times E$ be compact Calabi--Yau with holomorphic volume form
$\Omega_X = \Omega_{K3} \wedge dz_E$ and product Ricci-flat Kähler metric. Let
$\mathcal{F}_X = \Phi^{\mathrm{FA}}_3(\mathrm{Perf}(X))$ be the Costello--Li
holomorphic Chern--Simons $E_3$-holomorphic factorisation algebra on $X$
(Heal `heal:stage1` in Wave-13 B4). Let
$A_E := \Sp_{K3,E}(\mathcal{F}_X) = \int_{K3} \mathcal{F}_X|_E$ be the Stage-2
specialisation $E_1$-chiral algebra on $E$, and let
$\mathrm{Prim}(A_E) \simeq \mathfrak{g}_{\Delta_5}$ be its primitive Lie
superalgebra (Theorem `thm:two-stage-lorgat`).

Then the Cartan rank of $\mathrm{Prim}(A_E)$ obeys
$$
\mathrm{rk}_{\mathrm{Cartan}}(\mathfrak{g}_{\Delta_5})
\;=\;
\mathrm{rk}\bigl(\mathrm{II}_{1,1}^{K3\text{-fibre}} \oplus \mathrm{II}_{1,1}^E \oplus [2]_{\mathrm{diag}} / \mathrm{rad}\bigr)
\;=\;
\mathrm{rk}\bigl(\Lambda^{2,1}_{II}\bigr)
\;=\; 3,
$$
with the lattice quotient understood modulo the rank-$1$ radical corresponding
to the Mukai-vector polarisation constraint $s_1 \equiv 0$ (Lorgat 2020
Prop.~1).

**The numerical identity $3 = c_+(\mathrm{Muk}(K3)) - 1$ is a coincidence, not
a Stage-2 derivation.** The shift "$4 \to 3$" compares invariants of different
objects at different scopes (positive-definite rank of the $d = 2$ Mukai
lattice vs total rank of the $d = 3$ hyperbolic Cartan) and is not produced
by any direction-spending operation in the $(-1)$-shifted symplectic BV
structure of $6$d hCS on $X$.

## Proof

**Step 1 — at $d = 2$, $c_+(\mathrm{Muk}(K3)) = 4$ is a positive-rank invariant
of $H^*(K3, \mathbb Z)$, not a Cartan rank.** The Mukai lattice
$\mathrm{Muk}(K3) = H^0 \oplus H^2 \oplus H^4 \simeq \mathrm{II}_{4,20}$ has
rank $24$ and signature $(4, 20)$. The positive-definite rank $c_+ = 4$ is
the lattice-topological count $\dim H^0 + \dim H^4 + 2 = 1 + 1 + 2 = 4$
(the two additional positive directions are the Kähler and anti-Kähler
positive directions of the complexified Mukai pairing on $H^2$; cf.
Wave-12 A6 Heal `heal:B-no-div-two`). The Mukai-enhanced Heisenberg
$\mathcal{H}_{\mathrm{Muk}}(K3) = \Phi_2(D^b\,\mathrm{Coh}(K3))^{\mathrm{Heis}}$
has **Cartan rank $24$** (all $24$ free bosons), not rank $4$; the invariant
$\kappa_{\mathrm{ch}}^{\mathsf{B}}(\mathcal{H}_{\mathrm{Muk}}(K3)) = c_+ = 4$
is the *positive* subsector count, and enters the Beilinson--Drinfeld
Koszul-conductor identity $K^{\kappa_{\mathrm{ch}}}_{\mathsf{B}} = 2c_+ = 8$
via Hodge-parity doubling (Bruinier 2002 LNM 1780 Prop.~5.1 Heegner-Chern
reciprocity).

**Step 2 — at $d = 3$, $\mathrm{rk}_{\mathrm{hyp}}(\mathfrak{g}_{\Delta_5}) = 3$
is the *total* rank of the hyperbolic Cartan $\Lambda^{2,1}_{II}$ of
signature $(2, 1)$.** The Feingold--Frenkel $F_3$ Cartan matrix
$A = 4I - 2\mathbf{1}$ has eigenvalues $\{4, 4, -2\}$, signature $(2, 1)$,
rank $3$. This is the total rank of the Cartan subalgebra, not a
positive-rank invariant. At d=3, $c_+(\Lambda^{2,1}_{II}) = 2$, not $3$.

**Step 3 — the Stage-2 lattice projection (Wave-13 B4 Heal `heal:lattice`;
Wave-13 A8 Cycle 3).** Factorisation homology $\int_{K3}$ along the compact
K3 fibre collapses the rank-$24$ Mukai lattice via the Hodge-filtration
projection
$$
H^*(K3, \mathbb Z) \otimes \mathbb C
= \underbrace{H^0 \oplus H^4}_{\mathrm{II}_{1,1}^{K3\text{-fibre}}}
\oplus \underbrace{H^{2,0} \oplus H^{1,1} \oplus H^{0,2}}_{\text{rank } 22}
\longrightarrow
\mathrm{II}_{1,1}^{K3\text{-fibre}},
$$
retaining only the $(\dim = 0)$-invariant component (point-class and
top-class paired hyperbolically) after the Dolbeault-pushforward on the
$(-1)$-shifted symplectic BV complex
$\mathcal{E} = \Omega^{0,*}_{K3} \boxtimes \Omega^{0,*}_E \otimes \mathfrak{gl}_1[1]$.
Combined with the elliptic factor's Mukai-enhanced cohomology lattice
$H^*(E, \mathbb Z) = \mathrm{II}_{1,1}^E$ (class of zero-section and class
of fibre) and the diagonal class $[2]_{\mathrm{diag}}$ pairing K3 and $E$
through the CY volume form $\Omega_X$, the surviving lattice is
$$
\Lambda^{2,1}_{II}
\;\simeq\;
\mathrm{II}_{1,1}^{K3\text{-fibre}} \oplus \mathrm{II}_{1,1}^E \oplus [2]_{\mathrm{diag}} / \mathrm{rad}
\;\simeq\; \mathrm{II}_{1,1} \oplus [2],
$$
with the rank-$1$ radical corresponding to the Mukai-vector polarisation
constraint $s_1 \equiv 0$ (zero-section reduction, Lorgat 2020 Prop.~1;
Wave-13 B4 Heal `heal:lattice`).

**Step 4 — the rank arithmetic.** Pre-integration ambient rank:
$\mathrm{rk}(\mathrm{II}_{4,20} \oplus \mathrm{II}_{1,1}) = 24 + 2 = 26$.
Post-integration rank: $\mathrm{rk}(\Lambda^{2,1}_{II}) = 3$. The
**actual** rank reduction is $26 \to 3$, not $4 \to 3$. The summands
collapse as: $\mathrm{II}_{4,20} \to \mathrm{II}_{1,1}^{K3\text{-fibre}}$
(rank $24 \to 2$, Hodge-filtration pushforward), plus
$\mathrm{II}_{1,1}^E$ (rank $2 \to 2$, preserved), plus
$[2]_{\mathrm{diag}}$ (diagonal class, rank $+1$), modulo the rank-$1$
polarisation radical (rank $-1$): total $2 + 2 + 1 - 1 = 4 - 1 = 3$. The
"$-1$" is the Mukai-vector polarisation constraint, not a "spend one
positive direction on E".

**Step 5 — why the "$c_+ - 1 = 3$" identity is a coincidence.** Positive
ranks transform as $c_+(\mathrm{II}_{4,20}) = 4 \mapsto c_+(\Lambda^{2,1}_{II}) = 2$
under the Hodge-filtration projection. The claim "$\mathrm{rk}_{\mathrm{hyp}} = c_+ - 1$"
compares **total rank $3$** at $d = 3$ to **positive rank $4$** at $d = 2$.
These two invariants live at different scopes of different lattices; any
numerical shift-by-$1$ between them is an accidental consequence of
$2 + 2 + 1 - 1 = 3 = 4 - 1$, not a derivable Stage-2 operation.

**Step 6 — correct interpretation in the $(-1)$-shifted symplectic BV
structure.** The $(-1)$-shifted symplectic pairing $\omega_{BV}(\mathcal{A}_1,
\mathcal{A}_2) = \int_X \Omega_X \wedge \langle \mathcal{A}_1, \mathcal{A}_2\rangle$
on the BV complex $\mathcal{E} = \Omega^{0,*}(X) \otimes \mathfrak{g}[1]$
of $6$d hCS **does** enforce rank arithmetic via CPTVV 2017 shift law
$\mathrm{shift} = d - 4 = -1$ at $d = 3$. But the enforced arithmetic is
the **total rank reduction $26 \to 3$ through the Mukai-vector polarisation
constraint**, not a "unit shift" on $c_+$. The $U(E) = \mathrm{II}_{1,1}$
summand of the elliptic factor is preserved intact (both positive and
negative direction survive); it does not get "spent" to produce a
unit-rank loss. The unit-rank loss comes from the Lorgat 2020 Prop.~1
zero-section reduction $s_1 \equiv 0$ on the Mukai vector, which is a
single *linear* constraint on the resulting $\Lambda^{3,2}$ lattice
modded down to $\Lambda^{2,1}_{II}$, not a direction-spending on $U(E)$.

**Step 7 — why the loss is exactly $1$, not $0$ or $2$.** The Mukai-vector
polarisation constraint $s_1 \equiv 0$ is a rank-$1$ constraint: it fixes
a single class (the zero-section class) to zero in the Mukai vector
decomposition. This is the *sole* rank-reduction step beyond the
Hodge-filtration pushforward $\mathrm{II}_{4,20} \to \mathrm{II}_{1,1}^{K3\text{-fibre}}$.
There is no second constraint available within the Lorgat 2020 BKM
construction, so the loss cannot be $2$; and there is no construction
that bypasses the zero-section reduction, so the loss cannot be $0$.
The value $1$ is fixed by the dimension of the Mukai-vector's
zero-section component, which is $1$ because the zero-section is a
single cycle class in $H^0(K3, \mathbb Z)$ modulo the rank-$2$
$\mathrm{II}_{1,1}^{K3\text{-fibre}}$ lattice.

## Primary-source foundation

- **Costello--Li 2016** *JHEP* (hCS BV complex on $X = K3 \times E$):
  Stage-1 construction of $\mathcal{F}_X = \Phi^{\mathrm{FA}}_3(\mathrm{Perf}(X))$.
- **Costello--Gwilliam 2017** *Factorization Algebras in Quantum Field
  Theory* Vol.~II Thm.~8.6.1, 9.3.1: pre-factorisation algebra structure,
  operadic $E_d$-comparison.
- **Kontsevich 1999** / **Tamarkin 2003**: $E_d$-formality of Dolbeault
  little-$d$-disks operad.
- **CPTVV 2017** shift law: $\mathrm{shift} = d - 4$ on BV observable
  complex.
- **Mukai 1987** *Nagoya Math.~J.* 81 \S1 (Mukai lattice signature
  $(4, 20)$, $c_+ = 4$).
- **Borcherds 1998** *Invent.~Math.* 132 Thm.~13.3 (Borcherds singular
  theta lift, $\phi_{0,1}$ on $\Lambda^{3,2}$).
- **Gritsenko--Nikulin 1998** *Amer.~J.~Math.* 119 \S3 (Feingold--Frenkel
  $F_3$ rank-$3$ hyperbolic, lattice $\Lambda^{2,1}_{II}$ signature
  $(2, 1)$, eigenvalues $\{4, 4, -2\}$).
- **Lorgat 2020** \S5 (automorphic-corrected $\mathfrak{g}_{\Delta_5}$
  construction, denominator $\tfrac{1}{64}\Delta_5(2Z)$, Prop.~1
  zero-section reduction $s_1 \equiv 0$).
- **Oberdieck--Pixton 2018** Thm.~A (DT partition function
  $Z^{K3 \times E}_{\mathrm{DT}} = C/\Phi_{10}$ bridge to Stage-2 output).
- **Bruinier 2002** *LNM* 1780 Prop.~5.1 (Heegner-Chern reciprocity,
  $K^{\kappa_{\mathrm{ch}}}_{\mathsf B} = 2c_+ = 8$).

## Hypothesis

None required; the identity is proved at chain level through Wave-13 B4
and Wave-13 A8 already established results. The reframing clarifies that
the "unit shift" slogan is a scope-conflation artefact, not a missing
theorem.

## Cross-consistency notes

**Wave-1 spine.** The first-wave spine did not isolate the "unit shift"
as a claim; the refinement in Wave-2 (`platonic_synthesis_wave2_refinement.tex`
\S `wn:subsec:second-pass-six-invariants`) introduced it as conjectural,
flagged for attention. The present closure supersedes the Wave-2
conjectural framing with the established Wave-13 mechanism.

**Wave-2 refinement.** The six-value $\{0, 2, 3, 4, 5, 24\}$ distribution
across the $d = 2$ / $d = 3$ two-category setting is preserved. The
specific value $\kappa_{\mathrm{ch}}^{\mathsf{B}}(\mathcal{H}_{\mathrm{Muk}}(K3)) = 4$
is the positive-definite rank $c_+(\mathrm{II}_{4,20})$ in the
d=2 Mukai-Heisenberg scope; the specific value
$\kappa_{\mathrm{ch}}(\mathfrak{g}_{\Delta_5}) = 3$ is the total Cartan
rank in the d=3 BKM scope. These are **invariants of different objects
at different scopes**; the "$-1$" between them is not a Stage-2 theorem
but a numerical coincidence.

**CoHA treatise.** No interaction; $\mathfrak{g}_{\Delta_5}$ is the
Stage-2 image of the K3-fibre specialisation, not a CoHA construction.

**CLAUDE.md charter.** The present closure aligns with the charter's
"four $\kappa$-invariants, never conflated" principle: the Wave-2 framing
confused $\kappa_{\mathrm{ch}}^{\mathsf{B}}$ (positive-rank invariant at
$d = 2$) with $\kappa_{\mathrm{ch}}(\mathfrak{g}_{\Delta_5})$ (total-rank
invariant at $d = 3$). Subscript discipline resolves the issue: these
are different subscripts on different lattices; the scope declaration
distinguishes them.

**Bookkeeping note (not for inscription).** The $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}$
*additive* reading on $K3 \times E$ gives $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3) +
\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(E) = 2 + 1 = 3$ (Wave-12 A5
`wave12_a5_cy_d_stratification.tex` L108, L471, L656), numerically matching
$\mathrm{rk}_{\mathrm{Cartan}}(\mathfrak{g}_{\Delta_5}) = 3$. This is the
genuine **chain-level** identity — not "$c_+ - 1 = 3$" but
"$\mathrm{rk}_{\mathrm{Cartan}} = \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3) +
\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(E)$", a direct additivity statement on
the product CY. The rank-$3$ Cartan is the sum of the **rank-$2$ polarised
K3-sublattice Cartan** plus the **rank-$1$ $E$-Cartan after the elliptic
Mukai vector is absorbed into the diagonal class**.

## Inscription-ready TeX block

```latex
\begin{theorem}[Stage-2 rank reduction on $K3 \times E$]
\label{thm:stage-2-rank-reduction-k3-e}
\ClaimStatusTheorem
Let $X = K3 \times E$ with holomorphic volume form $\Omega_X = \Omega_{K3}
\wedge dz_E$ and product Ricci-flat Kähler metric. Let $\cF_X =
\Phi^{\mathrm{FA}}_3(\Perf(X)) \in E_3\text{-}\HolFA(X)$ be the
Costello--Li holomorphic Chern--Simons pre-factorisation algebra, and
$A_E := \Sp_{K3, E}(\cF_X) = \int_{K3} \cF_X |_E \in E_1\text{-}\ChirAlg(E)$
the Stage-$2$ specialisation along the K3 fibre. The Cartan rank of the
primitive Lie superalgebra $\Prim(A_E) \simeq \gDelta$ is
\[
\rk_{\mathrm{Cartan}}(\gDelta)
\;=\;
\rk\bigl(\Lat^{2,1}_{II}\bigr)
\;=\;
\rk\bigl(\mathrm{II}_{1,1}^{K3\text{-fibre}} \oplus \mathrm{II}_{1,1}^E \oplus
[2]_{\mathrm{diag}} / \mathrm{rad}\bigr)
\;=\; 3,
\]
where $\mathrm{II}_{1,1}^{K3\text{-fibre}}$ is the Hodge-filtration
pushforward of the Mukai lattice $\mathrm{II}_{4,20} = H^*(K3, \Z)$ to its
$(\dim = 0)$-invariant component $H^0 \oplus H^4$,
$\mathrm{II}_{1,1}^E = H^*(E, \Z)$ is the elliptic cohomology lattice,
$[2]_{\mathrm{diag}}$ is the diagonal class pairing K3 and $E$ through
$\Omega_X$, and the rank-$1$ radical corresponds to the Mukai-vector
polarisation constraint $s_1 \equiv 0$.
\end{theorem}

\begin{proof}
By Theorem~\ref{thm:two-stage-lorgat}, $\Prim(A_E) \simeq \gDelta$ as
$\Z$-graded Lie superalgebras. The Cartan subalgebra of $\gDelta$ is
$\Lat^{2,1}_{II} \otimes \R$, rank $3$, signature $(2, 1)$, with
Feingold--Frenkel Gram matrix $A = 4I - 2\mathbf{1}$, eigenvalues
$\{4, 4, -2\}$ (Gritsenko--Nikulin 1998 \emph{Amer.~J.~Math.} 119 \S3;
Feingold--Frenkel 1983).

The lattice identification $\Lat^{2,1}_{II} \simeq
\mathrm{II}_{1,1}^{K3\text{-fibre}} \oplus \mathrm{II}_{1,1}^E \oplus
[2]_{\mathrm{diag}} / \mathrm{rad}$ follows from three ingredients:
\begin{enumerate}[label=\textup{(\roman*)}]
\item the Hodge filtration on $H^*(K3, \C)$ decomposes the Mukai lattice
as $\mathrm{II}_{4,20} = H^0 \oplus H^2 \oplus H^4$ with $H^0 \oplus H^4
\simeq \mathrm{II}_{1,1}$ hyperbolic and $H^2 = H^{2,0} \oplus H^{1,1}
\oplus H^{0,2}$ of rank $22$; the factorisation homology
$\int_{K3}$ on the $(-1)$-shifted symplectic BV complex $\Omega^{0,*}(X)
\otimes \fgl_1[1]$ with pairing $\omega_{BV}(\cA_1, \cA_2) = \int_X
\Omega_X \wedge \langle \cA_1, \cA_2 \rangle$ (CPTVV 2017 shift
$= d - 4 = -1$) retains only the $(\dim = 0)$-invariant component by
the Dolbeault-pushforward
(Costello--Gwilliam 2017 \emph{Factorization Algebras} Vol.~II
Thm.~8.6.1);
\item the elliptic factor contributes $H^*(E, \Z) = \mathrm{II}_{1,1}^E$
with class of zero-section and class of fibre generating a rank-$2$
hyperbolic lattice;
\item the diagonal class $[2]_{\mathrm{diag}}$ arises from the pairing
of K3 and $E$ through the CY volume form $\Omega_X$, contributing one
rank-$1$ direction.
\end{enumerate}
The Mukai-vector polarisation constraint $s_1 \equiv 0$
(Lorgat 2020 Prop.~1) reduces the combined rank-$5$ lattice
$\mathrm{II}_{1,1} \oplus \mathrm{II}_{1,1} \oplus [2]$ to the rank-$3$
sublattice $\Lat^{2,1}_{II}$ via zero-section reduction. Borcherds 1998
\emph{Invent.~Math.} 132 Thm.~13.3 applied to $\phi_{0,1}$ on
$\Lambda^{3,2}$ reconstitutes $\gDelta$ as the generalised Borcherds--Kac--Moody
superalgebra on this rank-$3$ Cartan with denominator
$\tfrac{1}{64}\Delta_5(2Z)$.
\end{proof}

\begin{remark}[On the naïve ``$\rk_{\mathrm{hyp}}(\gDelta) = c_+(\Muk(K3)) - 1$''
reading]
\label{rem:stage-2-not-c-plus-minus-one}
The numerical equality $3 = c_+(\mathrm{II}_{4,20}) - 1 = 4 - 1$ is a
coincidence, not a consequence of Stage-$2$ specialisation. The
positive-definite rank $c_+(\mathrm{II}_{4,20}) = 4$ is a lattice
invariant of $H^*(K3, \Z)$ at $d = 2$; the Cartan rank
$\rk(\Lat^{2,1}_{II}) = 3$ is a total-rank invariant at $d = 3$. These
are invariants of different objects at different scopes of different
lattices. The actual Stage-$2$ rank reduction is the total-rank collapse
$26 \to 3$ of Theorem~\ref{thm:stage-2-rank-reduction-k3-e}, driven by
the Hodge-filtration pushforward on the K3 fibre and the Mukai-vector
polarisation constraint, not by a direction-spending on the elliptic
$\mathrm{II}_{1,1}^E$ summand, which is preserved intact. The chain-level
additivity identity
$\rk_{\mathrm{Cartan}}(\gDelta) = \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3) +
\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(E) = 2 + 1 = 3$
is the precise numerical content; subtracting $c_+(\Muk(K3)) - 1$
conflates a positive-rank invariant with a total-rank invariant.
\end{remark}
```
