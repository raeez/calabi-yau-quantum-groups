# Frontier-resolution lane 5: Sigma_{0,24} to Delta_5 OPE bridge

## Claim attacked

The attacked claim is the strong OPE-level assertion that the class-S
Schur VOA
\[
V_\Sigma=\mathrm{Schur}(\mathcal T[A_1,\Sigma_{0,24}])
\]
is already identified with the \(\Delta_5\)-chamber BKM chiral algebra
\[
V_\Delta=V_{\mathrm{BKM}}(\mathfrak g_{\Delta_5})
\]
from the data \(c=-214\), the K3 elliptic-genus specialization, and the
Borcherds denominator \(\Delta_5\).

Verdict: false as an unconditional theorem.  Those data prove a
character-level and anomaly-level bridge.  They do not determine OPE
coefficients, Jacobi identities, module tensor products, or the
stress-tensor-preserving chiral morphism.

## Proved core

1. The class-S anomaly ledger is theorem-level for the source Schur VOA.
   In `working_notes.tex:20098-20118`, the \(A_1\) theory on
   \(\Sigma_{0,24}\) has \(22\) \(T_2\) trinions and \(21\)
   \(\mathfrak{su}(2)\) gauge tubes, hence
   \[
   (n_v,n_h)=(63,88),\qquad c_{4d}=\frac{107}{6},
   \qquad c_{2d}=-12c_{4d}=-214.
   \]
   The same computation is inscribed in
   `chapters/examples/k3_chiral_bialgebra_platonic.tex:1650-1729`.

2. The direct \(\Sigma_{2,0}\) Costello-Witten route is obstructed, not
   merely incomplete.  The genus-two ledger gives \(c_{4d}=13/6\) in the
   full-hypermultiplet convention, \(17/6\) in the doubled
   half-hypermultiplet convention, and \(31/3\) after the displayed
   regulator term.  None equals \(107/6\); see
   `working_notes.tex:20120-20173`.

3. The character-level bridge is the declared local theorem at
   \(K_0\)/denominator level, with the K3-Jacobi specialization as the
   load-bearing input:
   \[
   \mathcal I_{\mathrm{Schur}}\big|_{\mathrm{K3\ Jac}}
   =\phi_{0,1}\quad\longmapsto\quad
   \mathrm{Borch}(\phi_{0,1})=\Delta_5.
   \]
   It preserves the specialized vacuum character, the \(K(1)\)
   paramodular line, and the root-multiplicity grading
   \(c_{\phi_{0,1}}(D,\ell)\).  It explicitly does not preserve OPEs,
   stress-tensor normalization, or module tensor products; see
   `working_notes.tex:20215-20263`.

4. The target-side \(\mathbf H_{\Delta_5}\) structure is strong but not a
   bridge theorem.  The local source records:
   - target classification by
     \(H^2(\mathfrak g_{\Delta_5})^{\mathbb Z/2,K(1)}
       \cong \mathbb C\cdot\Delta_5\),
     `chapters/examples/k3_chiral_bialgebra_platonic.tex:1507-1537`;
   - BKM Chevalley generators and root multiplicities,
     `chapters/examples/k3_chiral_bialgebra_platonic.tex:4800-4865`;
   - the quantum determinant
     \(\mathrm{qdet}\,T(u,Z)=C(u)\Delta_5(Z)\mathrm{Id}\),
     `chapters/examples/k3_chiral_bialgebra_platonic.tex:5064-5118`;
   - conditional Serre-BKM current relations, with the non-orthogonal
     imaginary closure conditional on the compact Hall comparison,
     `chapters/examples/k3_chiral_bialgebra_platonic.tex:5226-5406`.

These target theorems kill target-side normalization ambiguity.  They do
not produce a field map \(V_\Sigma\to V_\Delta\).

## Conditional bridge

The truthful bridge is exactly the Maurer-Cartan lift in the restricted
chiral cochain complex:
\[
\mathfrak o_{\mathrm{OPE}}\in
H^2\!\left(
C^\bullet_{\mathrm{ch}}(V_\Sigma,V_\Delta)_
{\mathcal B^{\mathrm{char}}_{\Delta_5},\,T,\,M_{24}}
\right).
\]
The character functor lifts to an OPE-level chiral algebra bridge if and
only if this class vanishes and the resulting Maurer-Cartan element has
Virasoro component \(c=-214\).  If
\[
H^1\!\left(
C^\bullet_{\mathrm{ch}}(V_\Sigma,V_\Delta)_
{\mathcal B^{\mathrm{char}}_{\Delta_5},\,T,\,M_{24}}
\right)=0,
\]
the lift is unique up to inner chiral automorphism.  This is precisely
`working_notes.tex:20265-20327`.

## Obstruction coordinates

Killed:

- \(o_{c,\Sigma}=0\): source central charge \(c_{2d}=-214\) is proved.
- \(o_{\mathrm{char}}=0\): the \(K_0\)-level specialization to
  \(\phi_{0,1}\) and the Borcherds lift to \(\Delta_5\) are available.
- \(o_{\mathrm{line}}=0\): the \(K(1)\) paramodular denominator line is
  fixed at character level.
- \(o_{\mathrm{mult}}=0\): root multiplicities are the Fourier
  coefficients of the K3 elliptic genus in the stated normalization.
- \(o_{\Sigma_{2,0}}\neq 0\): the genus-two direct route is killed by the
  \(13/6,17/6,31/3\) arithmetic mismatch.

Surviving:

- \(o_{\mathrm{OPE}}\): no local theorem proves vanishing in the
  \(T\)- and \(M_{24}\)-equivariant chiral cochain complex.
- \(o_T^{\Delta}\): source central charge is fixed, but the
  stress-tensor-preserving target field map is not constructed.
  The stress-tensor sheaf discussion at
  `chapters/examples/k3_chiral_bialgebra_platonic.tex:3681-3713` is a
  stalk/global anomaly reconciliation, not an OPE bridge.
- \(o_{M_{24}}^{\mathrm{map}}\): projective \(\widetilde M_{24}\)
  target equivariance is present, but equivariance of the actual chiral
  map \(V_\Sigma\to V_\Delta\) is not proved.
- \(u_{\mathrm{OPE}}\): \(H^1=0\) uniqueness is unproved.
- \(o_{\otimes}\): fusion/module tensor compatibility is not encoded by
  the character functor.
- \(o_{\mathrm{base}}\): \(\Sigma_{0,24}\) is the 4d parent surface, not
  the chiral base of \(\mathbf H_{\Delta_5}\).  The bi-based
  \(E^{\mathrm{nod}}_{24}\)/\(\overline{\mathcal A_2}\) architecture
  packages this distinction, but does not by itself solve the OPE
  comparison.

## Can a local theorem kill \(o_{\mathrm{OPE}}\)?

Not currently.  The local \(\Delta_5\) theorems repackage the obstruction
as target data:

- \(H^2(\mathfrak g_{\Delta_5})=\mathbb C\Delta_5\) classifies the
  target Hall-Drinfeld/quasi-Hopf gauge class after the Manin-pair input
  is fixed.  It is not the bridge complex
  \(H^2(C^\bullet_{\mathrm{ch}}(V_\Sigma,V_\Delta)_{\cdots})\).
- \(\mathrm{qdet}\,T=C(u)\Delta_5\) identifies a central paramodular
  element.  It is not a field-level OPE map from the Schur VOA.
- The Serre-BKM current relations give the target OPE constraints; their
  non-orthogonal imaginary closure is itself conditional on the compact
  Hall comparison.  Even if promoted, they would define \(V_\Delta\), not
  identify it with \(V_\Sigma\).
- The \(c=-214\) ledger fixes only the Virasoro scalar.  Equal central
  charges do not imply equality of vertex algebras.

Thus a local theorem can kill \(o_{\mathrm{OPE}}\) only if it supplies
one of two new inputs:

1. an explicit \(M_{24}\)-equivariant, stress-tensor-preserving field map
   \(V_\Sigma\to V_\Delta\) and a checked Maurer-Cartan solution for its
   OPE coefficients; or
2. a vanishing theorem
   \(H^2(C^\bullet_{\mathrm{ch}}(V_\Sigma,V_\Delta)_{\cdots})=0\)
   for the restricted complex.

Everything currently present is evidence or packaging, not annihilation.

## Proposed final theorem statement

**Theorem (truthful Sigma-Delta bridge).** Let
\[
V_\Sigma=\mathrm{Schur}(\mathcal T[A_1,\Sigma_{0,24}]),\qquad
V_\Delta=V_{\mathrm{BKM}}(\mathfrak g_{\Delta_5}).
\]
The class-S ledger gives \(c(V_\Sigma)=-214\).  The K3-Jacobi
specialization of the Schur character defines a canonical character
functor
\[
\mathcal B^{\mathrm{char}}_{\Delta_5}:K_0(V_\Sigma)\to
\mathrm{Borch}_{\Delta_5}
\]
sending \(\phi_{0,1}\) to \(\Delta_5\) and preserving the
paramodular line and the BKM root-multiplicity grading.  An OPE-level
bridge \(V_\Sigma\to V_\Delta\) exists exactly when the obstruction
\(\mathfrak o_{\mathrm{OPE}}\) in the restricted
\((T,M_{24})\)-equivariant chiral cochain complex vanishes and the
resulting Maurer-Cartan element has Virasoro component \(c=-214\).  If
the corresponding \(H^1\) vanishes, the lift is unique up to inner
chiral automorphism.  The \(\Sigma_{2,0}\) route cannot replace this
condition, because its anomaly ledger does not produce \(107/6\).

## Proof skeleton

1. Compute the class-S ledger:
   \(N_T=2g-2+n=22\), \(N_G=3g-3+n=21\), hence
   \((n_v,n_h)=(63,88)\) and \(c_{4d}=107/6\).  Apply BLLPRvR
   \(c_{2d}=-12c_{4d}\).  Local anchors:
   `working_notes.tex:20141-20152`,
   `chapters/examples/k3_chiral_bialgebra_platonic.tex:1691-1729`.

2. Run the same ledger for \(\Sigma_{2,0}\).  The outputs
   \(13/6,17/6,31/3\) miss \(107/6\).  Local anchor:
   `working_notes.tex:20154-20173`.

3. Pass only to character data:
   \(\mathcal I_{\mathrm{Schur}}\mapsto \phi_{0,1}\mapsto\Delta_5\).
   This preserves graded dimensions and denominator/root data, not OPE.
   Local anchor: `working_notes.tex:20215-20263`.

4. Place the missing data in deformation theory: an OPE-level lift is a
   Maurer-Cartan element in the restricted chiral cochain complex.  The
   obstruction is \(H^2\); uniqueness is \(H^1\).  Local anchor:
   `working_notes.tex:20265-20327`.

5. Compare against local \(\Delta_5\)-theorems.  Classification,
   current relations, quantum determinant, and \(M_{24}\) cocycle are
   target-side coordinates.  None is a cochain vanishing theorem for
   \(C^\bullet_{\mathrm{ch}}(V_\Sigma,V_\Delta)\).

## Primary source anchors needed

- Beem--Lemos--Liendo--Peelaers--Rastelli--van Rees 2013,
  arXiv:1312.5344, Theorem 3.1 and eqs. (3.14), (3.18):
  \(c_{2d}=-12c_{4d}\), \(k_{2d}=-k_{4d}/2\).
- Chacaltana--Distler 2010, arXiv:1008.5203, Section 5 / eq. (5.14),
  plus Shapere--Tachikawa 2008 eq. (2.20): class-S anomaly ledger.
- Gaiotto 2009, arXiv:0904.2715: class-S \(A_1\) construction and
  pants decomposition.
- Eguchi--Ooguri--Tachikawa 2011, arXiv:1004.0956: K3 elliptic genus
  normalization and Mathieu coefficients.
- Borcherds 1998, Invent. Math. 132, Theorem 13.3, and
  Gritsenko--Nikulin 1998, Theorem 2.1: Borcherds product and
  \(\Delta_5\) denominator/root multiplicities.
- Gritsenko 1999, Theorem 6.1: uniqueness/normalization of the
  weight-5 paramodular form.
- Beilinson--Drinfeld, *Chiral Algebras*, Chapter 3, and
  Francis--Gaitsgory 2012: chiral/factorization deformation framework
  for the restricted cochain complex.

## Computations and searches run

- Read `CLAUDE.md` and local `AGENTS.md` doctrine.
- `rg` over `working_notes.tex`, `notes`, and `chapters` for
  `c=-214`, `Sigma_{0,24}`, `Delta_5`, `Schur`, `OPE`, and `BLLPRvR`.
- Inspected the requested labels in `working_notes.tex`:
  `wn:thm:cw-c214-direct-chain`,
  `wn:thm:sigma024-delta5-bridge-criterion`,
  `wn:thm:sigma024-delta5-character-bridge`,
  `wn:thm:sigma024-delta5-final-ope-obstruction`,
  `wn:thm:compact-cy3-apex-closure`.
- Inspected target-side chapter anchors in
  `chapters/examples/k3_chiral_bialgebra_platonic.tex`.
- Arithmetic checked directly:
  \[
  (2\cdot 63+88)/12=107/6,\quad
  -12(107/6)=-214,
  \]
  and the \(\Sigma_{2,0}\) alternatives \(13/6,17/6,31/3\).
- No build run; this was a notes-only report and the repo requests
  session-end builds only on user opt-in.

## Files changed

- Created `notes/frontier_resolution_swarm_20260424_sigma_delta_ope.md`.
