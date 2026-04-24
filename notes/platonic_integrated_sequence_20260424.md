# Platonic Integrated Sequence for Volume III

Date: 2026-04-24.

## 1. Primitive

Volume I begins with the ordered bar complex on a curve:
\[
B^{\mathrm{ord}}(A)=T^c(s^{-1}\overline A).
\]
The five theorem packages A, B, C, D, H are not introduced as a
programme. They are forced by this object: bar-cobar inversion, the
curved coderived ambient, complementarity, modular curvature, and
Hochschild concentration are the successive obstructions that appear
when the ordered bar is asked to survive from genus zero to the modular
tower.

Volume III must begin with the geometric input to that bar complex. The
primitive is not a list of quantum groups. It is the two-stage passage
\[
\Phi_d^{(\Sigma_{d-1},C)}
 =
\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C}\circ \Phi_d^{\mathrm{FA}},
\]
where Stage 1 is the native holomorphic \(E_d\)-factorisation algebra
on the Calabi-Yau target and Stage 2 is the chiral shadow on a curve.
The bar complex of Volume I receives the Stage-2 output.

The front matter should make this inevitable by one worked object:
\[
X=K3\times E.
\]
At this object the generic is already contained in the particular:
\[
\kappa_{\mathrm{cat}}(X)=0,\qquad
\kappa_{\mathrm{ch}}^{\mathrm{Hodge}}(X)=0,\qquad
\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(X)=3,\qquad
\kappa_{\mathrm{BKM}}(\Delta_5)=5,\qquad
\kappa_{\mathrm{fiber}}(K3)=24.
\]
These numbers cannot be values of one invariant. The false idea
\[
\kappa_{\mathrm{BKM}}
=
\kappa_{\mathrm{ch}}+\chi(\mathcal O_{\mathrm{fiber}})
\]
already fails at \(N=1\) in the total-space convention:
\(5\ne 0+0\). Dismissing that false idea is the opening movement. The
correct architecture is forced: different invariants live at different
tiers of the two-stage construction.

## 2. Front-Matter Roles

### Abstract

The abstract should be one mathematical object, one formula, one
crystallisation, one universal identity.

1. A CY category produces \(\Phi_d^{\mathrm{FA}}(\mathcal C)\), an
   \(E_d\)-holomorphic factorisation algebra on the CY target.
2. A pair \((\Sigma_{d-1},C)\) produces an \(E_1\)-chiral shadow on
   \(C\), with native curve level \(E_\infty,E_2,E_1\) for
   \(d=1,2,\ge 3\).
3. Positive effective geometry gives \(Y^+(X)\); after pairing and
   completion, the quantum group is \(D(Y^+(X))\).
4. \(K3\times E\) supplies the seed: the categorical, Hodge,
   Heisenberg, BKM, and fibre measurements separate.
5. The Gritsenko-Clery atlas satisfies
   \(\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2\) with its cover-group
   assignment.
6. The volume proves the pieces it names and reduces the remaining
   compact comparison maps to explicit proof obligations.

The current abstract contains the right mathematics but performs too
many jobs: abstract, theorem ledger, retraction record, and outline. The
ideal abstract should not include the full CY-A/B/C/D status ledger or
the complete frontiers.

### Preface

The preface should be Serre-style: the seed of the generic lies in the
particular.

Order:

1. Display the \(K3\times E\) measurements.
2. Show why one-invariant thinking fails.
3. Let the two-stage factorisation appear as the only construction that
   can carry all measurements without conflation.
4. Write the six-dimensional hCS action as physics, not metaphor:
   \[
   S_{\mathrm{hCS}}(\mathcal A)
   =
   \int_X \Omega_X\wedge
   \langle\mathcal A,\overline\partial\mathcal A
   +\tfrac13[\mathcal A,\mathcal A]\rangle.
   \]
5. Push it along the \(K3\)-fibre to the elliptic curve \(E\).
6. Let \(\Delta_5\) appear as the one-loop or Borcherds output, not as
   decorative input.
7. Only then state the general grammar \(\Phi_d=\mathrm{Sp}\circ
   \Phi_d^{\mathrm{FA}}\).

The preface should not be a duplicate introduction. It should not carry
long status ledgers. It should teach by constructing the phenomenon.

### Introduction

The introduction should be the theorem machine.

Order:

1. Define CY category, cyclic trace, Hochschild calculus.
2. State Stage 1 and Stage 2 with exact hypotheses.
3. State native operadic levels and the centre rule:
   \(A\) is \(E_1\)-chiral at \(d\ge 3\), while \(E_2\) lives on
   \(\mathcal Z(\mathrm{Rep}^{E_1}(A))\).
4. Define \(Y^+(X)\) and the precise additional data needed for
   \(D(Y^+(X))\): positive half, pairing, completion, descent.
5. Give the three worked inputs in increasing complexity:
   \(\mathbb C^3\), \(K3\), \(K3\times E\).
6. State CY-A/B/C/D/H in dependency order, not as a status catalogue.
7. Present the proof obligations as named missing lemmas or comparison
   maps, so the manuscript asks for proof rather than deflation.

The current introduction has the material but repeats the preface,
repeats the outline, and sometimes states global objects before their
construction data have been installed. The ideal introduction should
make every theorem depend on the previous construction.

## 3. Ideal Seven-Part Sequence

### Part I. Calabi-Yau Input

Question: what datum can be fed to the Vol I bar-cobar machine?

Contents:

- CY categories.
- Cyclic \(A_\infty\)-structures.
- Negative cyclic trace.
- Hochschild calculus.
- Gerstenhaber bracket of degree \(1-d\).

Output:
\[
(\mathrm{CC}_\bullet(\mathcal C),\ \mathrm{HH}^\bullet(\mathcal C),
\mathrm{Tr},\ \mathbb S^d\text{-framing}).
\]

This part should not announce the quantum group. It prepares the
input.

### Part II. The Two-Stage Functor

Question: how does CY input become a chiral algebra on a curve?

Contents:

- \(\Phi_d^{\mathrm{FA}}\) on the CY target.
- \(\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C}\) by factorisation
  homology.
- CY-A as the existence theorem.
- hCS as the \(d=3\) physical realisation.
- The chain-level versus \((\infty,1)\)-categorical lanes with equal
  status.

Output:
\[
A_{\mathcal C}^{(\Sigma,C)}
=
\mathrm{Sp}^{\mathrm{ch}}_{\Sigma,C}
\Phi_d^{\mathrm{FA}}(\mathcal C).
\]

### Part III. Operadic Level and Centre

Question: what algebraic structure does the shadow carry?

Contents:

- \(E_\infty,E_2,E_1\) levels by dimension.
- \(E_1\)-chiral bialgebra axioms.
- Drinfeld centre and derived chiral centre.
- Quantum group foundations.
- \(R\)-matrices as half-braidings and stable-envelope residues.

Output:
\[
\mathcal Z(\mathrm{Rep}^{E_1}(A))
\simeq
\mathrm{Rep}^{E_2}(Z^{\mathrm{der}}_{\mathrm{ch}}(A)).
\]

This is where the reader learns why \(E_2\) cannot be placed directly
on \(A\) at \(d\ge 3\).

### Part IV. The Seed Crown: \(K3\) and \(K3\times E\)

Question: what does the construction actually make in the first
nontrivial CY family?

Order:

1. \(K3\): Mukai lattice, Heisenberg, abelian Yangian.
2. \(K3\times E\): four \(\kappa_\bullet\)-invariants, the
   Hodge/Heisenberg split of \(\kappa_{\mathrm{ch}}\), no conflation.
3. \(\Delta_5\), \(\Phi_{10}=\Delta_5^2\), Borcherds denominator.
4. Hall-Drinfeld/Borcherds branch.
5. Six routes as measurements/specialisations, not six \(\Phi\)
   applications.
6. Pentagon and intertwiners.

Output:
the crown object is presented as a construction problem with proved
value theorems and explicit comparison maps to be proved, not as a
status compromise.

### Part V. The Landscape

Question: what changes when the CY input changes?

Order:

1. CY-D dimension stratification.
2. Toric \(\mathbb C^3\): \(\mathrm{CoHA}(\mathbb C^3)=Y^+\), then
   double, then representation/VOA faces.
3. Conifold and local \(\mathbb P^2\) as falsification tests for wrong
   surface analogies.
4. Matrix factorisations and Fukaya categories.
5. Eight-form and CHL/non-CHL host geometry after the basic examples
   are stable.

The landscape should function as a laboratory, not a catalogue.

### Part VI. Seven Faces and Cross-Volume Trace

Question: why do the many constructions see the same element?

Contents:

- Seven faces of \(r_{\mathrm{CY}}(z)\).
- Three-tier stratification: CY-intrinsic, Stage-1, Stage-2.
- Vol I bar-cobar shadow.
- Vol II \(\mathsf{SC}^{\mathrm{ch,top}}\) and hCS/holography.
- Universal trace identity at its proved scope:
  \[
  \mathrm{tr}_{\mathrm{ghost}}(Q_{\mathrm{BRST}}^2)
  =
  \mathrm{tr}_{\mathrm{Pentagon}}
  =
  \omega_{\mathrm{Borcherds}}
  =
  c_N(0)/2.
  \]

This is the Dirac movement: the physics and mathematics are the same
object viewed under different projections.

### Part VII. Proof Obligations and Frontiers

Question: what exact proofs remain to make the construction complete?

The frontiers should be written as missing lemmas, not as promotional
directions.

Examples:

- Positive-half descent for compact \(K3\times E\).
- Hall pairing and completion for the compact double.
- hCS-to-Hall comparison on compact CY3s.
- Bracket-level BPS-to-BKM comparison.
- Full non-abelian K3 Yangian/Hall-Drinfeld comparison.
- Non-CHL host construction for \(N=5,7,8\).
- Chain-level \(S^3\)-framing beyond verified framed loci.

Every broken proof becomes a proof obligation with a route to closure.

## 4. Proof Repair Principle

The manuscript should not be degraded when a proof breaks. A broken
proof is repaired in this order:

1. Find the exact failing step.
2. Insert the missing lemma if the existing hypotheses prove it.
3. Strengthen the hypothesis by deriving the missing property from the
   geometry already present.
4. Replace the false route by a stronger true route that proves the
   same conceptual theorem.
5. If the construction genuinely requires new mathematics, state the
   exact comparison map and build the surrounding chapter so that this
   map is the next theorem to prove.

Status language is not a repair. The repair is a construction, a
lemma, a computation, or a comparison theorem.

## 5. Immediate Front-Matter Rebuild

The first concrete rebuild should be surgical.

1. Replace the abstract by a short theorem-level abstract.
2. Rewrite the opening of the preface around \(K3\times E\):
   the four \(\kappa_\bullet\)-invariants, the five seed measurements,
   the false additive idea, the two-stage construction, hCS,
   \(\Delta_5\).
3. Cut duplicate theorem ledgers from the preface.
4. Rebuild the introduction as the dependency graph of definitions and
   theorems.
5. Move long proof-status inventories into the relevant chapter
   openings or into `FRONTIER.md`.
6. Keep the seven-part structure only insofar as each part answers one
   forced question.

The guiding sentence is:

\[
\text{The particular object }K3\times E\text{ forces the general
two-stage functor.}
\]

That is the Volume III analogue of Volume I's opening:

\[
\text{The ordered bar complex forces the modular Koszul tower.}
\]
