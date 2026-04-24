# Agent 11 -- Kazhdan axis: categories, centers, MTC endpoint

Date: 2026-04-24.

Scope contract: read-only on manuscript files. This note is the only owned
output:
`notes/adversarial_bps_positive_geometry_20260424/agent_11_kazhdan_categories_centers.md`.

Claim attacked:
\[
  \Rep^{E_2}(A_\mathcal C),\qquad
  \mathcal Z(\Rep^{E_1}(A_\mathcal C)),\qquad
  \mathcal MTC(A_\mathcal C),
\]
as the representation-theoretic endpoint of CY-C.

## Files and anchors read

- `CLAUDE.md:1-502`, `AGENTS.md:1-498`.
- `chapters/theory/quantum_groups_foundations.tex:96-126`: conditional
  positive-geometry Drinfeld double.
- `chapters/theory/quantum_groups_foundations.tex:205-207`: CY-C as
  representation-theoretic quantum-group output; `d >= 3` center caveat.
- `chapters/theory/quantum_groups_foundations.tex:348-390`: `Rep_q`,
  ribbon structure, root-of-unity MTC, Kazhdan--Lusztig equivalence.
- `chapters/theory/quantum_groups_foundations.tex:502-537`: CY-C statement
  and dimension-by-dimension status.
- `chapters/theory/quantum_groups_foundations.tex:5655-5838`: one-level-up
  rule for the BKM `(infinity,2)` target.
- `chapters/theory/quantum_groups_foundations.tex:5920-5934`,
  `6068-6076`: K3 x E derived center / `E_2`-monoidal enhancement lives on
  representations, not on `H_Delta5`.
- `chapters/examples/quantum_group_reps.tex:4-9`: opening center statement.
- `chapters/examples/quantum_group_reps.tex:48-68`, `92-110`: generic versus
  root-of-unity dichotomy and the `sl_2` fusion example.
- `chapters/examples/quantum_group_reps.tex:166-209`: KL equivalence and DK
  bridge diagram.
- `chapters/examples/quantum_group_reps.tex:216-244`: CY-C realization
  statement and status.
- `chapters/examples/quantum_group_reps.tex:769-805`: K3 lattice MTC claim.
- `chapters/examples/quantum_group_reps.tex:823-870`: proved/conjectural
  CY-C scope.
- `chapters/examples/quantum_group_reps.tex:1178-1180`: K3 Hall--Drinfeld
  representation-theory supplement.
- `chapters/examples/coha_wall_crossing_platonic.tex:12-72`: algebra versus
  coalgebra, positive half versus full Yangian, motivic/numerical split.
- `chapters/examples/coha_wall_crossing_platonic.tex:297-360`: CoHA embeds as
  positive-half algebra in an `E_1` chiral output.
- `chapters/examples/coha_wall_crossing_platonic.tex:1349-1432`: `Y^+` is
  not the full Yangian; Drinfeld double needs the pairing.
- `chapters/examples/coha_wall_crossing_platonic.tex:1533-1535`: K3 x E
  Hall--Drinfeld double remark.
- `chapters/examples/coha_wall_crossing_platonic.tex:1729-1853`: chamber
  CoHA, chamber-specific Hall--Drinfeld double, and `R`-matrix gauge
  conjugation.
- `chapters/examples/coha_wall_crossing_platonic.tex:2635-2853`: stable GV
  and refined Yangian data land in an `E_2` center.
- Dependency read: `chapters/theory/drinfeld_center.tex:4-20`,
  `41-60`, `101-124`, `161-238`, `377-543`, `796-814`,
  `2424-2432`, `2533-2601`, `3447-3517`.

## Verdict

The endpoint should be stated as a three-step categorical construction, not as
an `E_2` structure on the boundary algebra:
\[
  A=A_\mathcal C^{(\Sigma,C)} \quad (d=3,\ E_1\text{-chiral}),
\]
\[
  \mathsf C_A := \Rep^{E_1}(A) \quad \text{monoidal, generally not braided},
\]
\[
  \mathsf Z_A :=
  \mathcal Z(\mathsf C_A)
  \simeq
  \Rep^{E_2}\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(A)\bigr)
  \quad \text{braided monoidal}.
  \tag{1}
\]
Only after rigidity, finite length, ribbon twist, and non-degeneracy are
proved can one form a modular tensor category. At root of unity the correct
semisimple object is a tilting/negligible quotient, not the full
finite-dimensional representation category:
\[
  \mathcal MTC_q(\mathfrak g)
  :=
  \Tilt_q(\mathfrak g)\big/\mathcal N_{\mathrm{negl}},
  \qquad
  q=\exp\!\left(\frac{\pi i}{d_\mathfrak g(k+h^\vee)}\right),
  \tag{2}
\]
where \(d_\mathfrak g\) is the lacing number. For simply laced
\(\mathfrak g\), \(d_\mathfrak g=1\). The proved prototype is
\[
  \mathcal MTC_q(\mathfrak g)
  \simeq
  \mathcal O_k^{\mathrm{int}}(\widehat{\mathfrak g})
  \tag{3}
\]
by Andersen, Andersen--Paradowski, Kazhdan--Lusztig, and Finkelberg.

For CY-C at \(d=3\), the precise conjectural endpoint is therefore:
\[
  \Rep_{\mathrm{adm}}\bigl(C(\mathcal C,q)\bigr)^{\mathrm{mod}}
  \simeq
  \mathcal MTC(A_\mathcal C^{(\Sigma,C)}),
  \tag{4}
\]
where the right side means the modular or non-semisimple-modular quotient of
\(\mathcal Z(\Rep^{E_1}(A_\mathcal C^{(\Sigma,C)}))\), depending on whether
one uses semisimplification or modified trace. Formula (4) is conjectural
for general CY categories; it is theorem-grade only on the classical
affine/root-of-unity KL locus and on explicitly constructed local Hall loci
with a proved double and center passage.

## ATTACK 1 -- `Rep^{E_2}(A)` at `d=3` is not the object

Attack. `quantum_groups_foundations.tex:518-524` defines
\(\mathcal MTC(A_\mathcal C):=\Rep^{E_2}(A_\mathcal C)^{ss}\), then adds that
at \(d\ge 3\) the \(E_2\)-braiding lives on the Drinfeld center. The
notation risks making \(A_\mathcal C\) itself an \(E_2\)-chiral algebra.
`quantum_group_reps.tex:823-829` repeats the same compression.

Failure mode. At \(d=3\), \(A_\mathcal C=\Phi_3^{(\Sigma,C)}(\mathcal C)\)
is natively \(E_1\). The representation category \(\Rep^{E_1}(A_\mathcal C)\)
is monoidal. The braiding appears only after adding coherent half-braidings:
\[
  \mathcal Z(\Rep^{E_1}(A_\mathcal C)).
\]

Heal. Define the notation explicitly:
\[
  \Rep^{E_2}_{\mathrm{cent}}(A)
  :=
  \mathcal Z(\Rep^{E_1}(A))
  \simeq
  \Rep^{E_2}\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(A)\bigr).
  \tag{5}
\]
Then
\[
  \mathcal MTC(A):=
  \bigl(\Rep^{E_2}_{\mathrm{cent}}(A)\bigr)^{\mathrm{ss}}
  \tag{6}
\]
only when the semisimplification exists and is non-degenerate.

Status. Proved elsewhere for an \(E_1\)-algebra in the BZFN/Lurie setting
(`drinfeld_center.tex:101-124`). Conditional for a given CY output until the
claimed \(A_\mathcal C\) is constructed at the necessary chain level.

Insertion recommendation. At `quantum_groups_foundations.tex:518-524`, replace
the displayed definition by (5)--(6). At
`quantum_group_reps.tex:823-829`, replace
`\Rep^{E_n}(\Phi(\cC))` by
`\mathcal Z(\Rep^{E_1}(\Phi_d(\cC)))` in the `d >= 3` clause.

## ATTACK 2 -- The Drinfeld center is a right adjoint, not a hidden braiding on `A`

Attack. Several passages use the center correctly in prose, but the endpoint
language still suggests that the center "upgrades" \(A\). That is false:
the algebra remains \(E_1\).

Failure mode. The Drinfeld center is categorical data:
\[
  \mathcal Z(\mathsf C)
  =
  \{(M,\sigma_{M,-}) :
      \sigma_{M,N}:M\otimes N\xrightarrow{\sim}N\otimes M,
      \ \sigma_{M,N\otimes P}
      =(\id_N\otimes\sigma_{M,P})(\sigma_{M,N}\otimes\id_P)\}.
  \tag{7}
\]
The braiding in \(\mathcal Z(\mathsf C)\) is
\[
  \beta_{(M,\sigma_M),(N,\sigma_N)}=\sigma_{M,N}.
  \tag{8}
\]
For evaluation modules \(V_u,V_v\), the \(R\)-matrix is the half-braiding:
\[
  R(u-v)=\sigma_{V_u,V_v}:V_u\otimes V_v\to V_v\otimes V_u.
  \tag{9}
\]

Heal. Use the arrow:
\[
  A\ (E_1)
  \longmapsto
  \Rep^{E_1}(A)\ (\text{monoidal})
  \longmapsto
  \mathcal Z(\Rep^{E_1}(A))\ (\text{braided})
  \longmapsto
  R(u-v).
  \tag{10}
\]
Do not write that \(A\) acquires an \(E_2\)-braiding.

Status. Proved elsewhere for ordinary monoidal categories
(`drinfeld_center.tex:41-60`) and for stable infinity categories via BZFN
(`drinfeld_center.tex:101-124`, `247-293`). The K3 x E version is precisely
the statement at `drinfeld_center.tex:2424-2432`.

Insertion recommendation. At `quantum_groups_foundations.tex:467-468` and
`542-543`, replace "Rep^{E_2}(A)" shorthand by "the central representation
category (5)". At `quantum_groups_foundations.tex:6068-6076`, keep the
existing sentence but remove the self-equivalence notation
`\Rep_{\mathrm{fact}}(\HDelta)\simeq
\cZ(\Rep_{\mathrm{fact}}(\HDelta))^{\mathrm{centred}}` unless the intended
central subcategory is defined; the correct target is
\[
  \mathcal Z(\Rep_{\mathrm{fact}}^{E_1}(\HDelta)).
  \tag{11}
\]

## ATTACK 3 -- Full `Rep_q(g)` at a root of unity is not an MTC

Attack. `quantum_group_reps.tex:60-64` says the root-of-unity fusion category
is the quotient of \(\Rep_q(\mathfrak g)\) by negligible morphisms. This is
too compressed: the standard construction goes through tilting modules for
the Lusztig divided-power form, then quotients negligible morphisms.

Failure mode. The full finite-dimensional root-of-unity category is
non-semisimple. It contains indecomposable non-simple modules, and its
ordinary categorical trace has a radical. It is not a semisimple MTC.

Heal. State:
\[
  \Tilt_q(\mathfrak g)
  \subset
  \Rep^{\mathrm{fd}}\bigl(U_q^{\mathrm{res}}(\mathfrak g)\bigr),
  \qquad
  \mathcal MTC_q(\mathfrak g)
  =
  \Tilt_q(\mathfrak g)/\mathcal N_{\mathrm{negl}}.
  \tag{12}
\]
The simple survivors are indexed by the Weyl alcove
\[
  P_k^+
  =
  \{\lambda\in P^+:\langle\lambda,\theta^\vee\rangle\le k\}
  \tag{13}
\]
in the simply laced case, with the lacing-normalized alcove in general.

Status. Proved elsewhere: Andersen 1992, Andersen--Paradowski 1995, Lusztig
integral form. Non-semisimple alternatives require modified trace
(`drinfeld_center.tex:796-814`) and should not be called semisimple MTCs.

Insertion recommendation. At `quantum_group_reps.tex:60-64`, replace
"the fusion category is the quotient" by "the tilting subcategory for
Lusztig's divided-power form has a negligible tensor ideal; its quotient is
the fusion category." At `quantum_groups_foundations.tex:375-379`, the
statement is already close; add `tilting` to the proposition body, not only
to the proof attribution.

## ATTACK 4 -- Generic Drinfeld--Kohno and positive-level KL are two regimes

Attack. `quantum_group_reps.tex:166-209` places KL, DK, `Rep^{E_1}(V_k)`,
and `Rep_q` in one square. The square is morally right, but it suppresses a
regime distinction.

Failure mode. At generic \(q\), \(\Rep_q(\mathfrak g)\) is braided ribbon
and semisimple but has infinitely many simples; it is not a finite MTC. At
positive integral level, the conformal-block category is finite and modular,
but the quantum group side is the root-of-unity tilting quotient (12), not
the full \(\Rep_q(\mathfrak g)\).

Heal. Split the statement:

1. Generic Drinfeld--Kohno:
\[
  \Rep_q(\mathfrak g)
  \simeq
  \Rep(\mathfrak g)_{\Phi_{\mathrm{KZ}}}
  \quad\text{as braided monoidal categories}.
  \tag{14}
\]
2. Positive-level KL/Finkelberg:
\[
  \Tilt_q(\mathfrak g)/\mathcal N_{\mathrm{negl}}
  \simeq
  \mathcal O_k^{\mathrm{int}}(\widehat{\mathfrak g})
  \quad\text{as modular tensor categories}.
  \tag{15}
\]

Status. (14) and (15) are proved elsewhere, but they should not be merged
into a single unqualified `Rep_q` statement.

Insertion recommendation. At `quantum_group_reps.tex:170-178`, replace
`\Rep_q(\frakg)` by `\mathcal MTC_q(\frakg)` or
`\Tilt_q(\frakg)/\mathcal N_{\mathrm{negl}}`. Keep `Rep_q` for the generic
Drinfeld--Kohno paragraph only. At `drinfeld_center.tex:3447-3517`, add the
same distinction to the master square: the bottom-right root-of-unity object
is the semisimplified tilting quotient.

## ATTACK 5 -- Reconstruction from the center needs finiteness or a fiber functor

Attack. `drinfeld_center.tex:784-793` says a rigid braided monoidal category
with a fiber functor reconstructs a quasi-triangular Hopf algebra and, in the
CY setting, \(H\simeq U_q(\mathfrak g)\) with \(q\) determined by
\(\kappa_{\mathrm{ch}}\).

Failure mode. A modular tensor category need not come with a chosen exact
faithful fiber functor to `Vect`. Without such a functor, reconstruction
produces a coend/internal Hopf algebra, or a weak/quasi-Hopf algebra after
choosing a realization. Moreover \(\kappa_{\mathrm{ch}}\) alone does not
determine \(q\); \(q\) also depends on level, lacing, framing, and the
chosen root-of-unity normalization.

Heal. State:
\[
  \mathsf B=\mathcal Z(\Rep^{E_1}(A)).
  \tag{16}
\]
If \(\mathsf B\) is a finite tensor category and an exact faithful tensor
functor \(\omega:\mathsf B\to\Vect_\mathbb C\) is fixed, then
\[
  H_\omega=\mathrm{Nat}^{\otimes}(\omega,\omega)
  \tag{17}
\]
is a quasi-triangular quasi-Hopf algebra with
\(\mathsf B\simeq \Rep(H_\omega)\). Without \(\omega\), use the Lyubashenko
coend
\[
  \mathbb F_{\mathsf B}:=\int^{X\in\mathsf B} X^\vee\otimes X
  \tag{18}
\]
internal to \(\mathsf B\).

Status. Proved elsewhere in finite tensor category reconstruction. For CY-C,
the existence of a named \(C(\mathcal C,q)\) is conjectural except the
classical/root-of-unity affine and explicit toric Hall loci.

Insertion recommendation. At `quantum_groups_foundations.tex:509-512`, replace
"q determined by \(\kappa_{\mathrm{ch}}\)" by "q determined by the full
level/framing/R-matrix normalization, with \(\kappa_{\mathrm{ch}}\) one
numerical constraint." At `drinfeld_center.tex:784-793`, add the fiber-functor
hypothesis to the CY sentence or weaken the conclusion to a coend/internal
Hopf object.

## ATTACK 6 -- The K3 lattice endpoint is a trivial discriminant MTC, not a nontrivial root-of-unity quantum group

Attack. `quantum_group_reps.tex:769-805` writes a K3 lattice quantum group
at
\[
  q_\Lambda=e^{\pi i/\det(\Lambda_{K3})}.
\]
Since \(\Lambda_{K3}=II_{4,20}\) is unimodular, \(\det(\Lambda_{K3})=1\);
the formula gives \(q_\Lambda=-1\), while the discriminant group is zero.

Failure mode. The lattice VOA attached to an even unimodular lattice has a
single irreducible module. Its representation category is equivalent to
`Vect` as a fusion category, with trivial discriminant form:
\[
  A_\Lambda=\Lambda^\vee/\Lambda=0,\qquad
  \mathcal C(A_\Lambda,q_\Lambda)=\mathrm{Vect}.
  \tag{19}
\]
There is no nontrivial root-of-unity quantum group reconstruction in this
unimodular lattice statement.

Heal. Replace the root-of-unity phrase by discriminant-form language:
\[
  \Rep^{E_2}(V_{\Lambda_{K3}})
  \simeq
  \mathcal C(\Lambda_{K3}^\vee/\Lambda_{K3},q_{\Lambda_{K3}})
  =
  \mathrm{Vect}.
  \tag{20}
\]
This is a verified degenerate MTC endpoint for the K3 Mukai-Heisenberg
branch, not evidence for a nontrivial \(U_q(\mathfrak g)\) at \(q=-1\).

Status. Lattice-VOA module theory: proved elsewhere. The claim that this is
a nontrivial KL quantum-group realization should be downgraded to
"degenerate discriminant-form verification."

Insertion recommendation. At `quantum_group_reps.tex:785-789`, delete
`q_\Lambda=e^{\pi i/\det(\Lambda_{K3})}` and replace with (20). At
`quantum_group_reps.tex:837-841`, replace "Mukai-lattice quantum group" by
"Mukai-lattice discriminant-form category, trivial because \(II_{4,20}\) is
unimodular."

## ATTACK 7 -- K3 Hall--Drinfeld representation theory overstates finite modules

Attack. `quantum_group_reps.tex:1178-1180` says the K3 Hall--Drinfeld double
has evaluation modules \(V_u\) and that "at Lie/Hopf level the
representation category is abelian (24 Miki modules); BKM non-abelianity
emerges via Frenkel--Kac vertex closure."

Failure mode. "Abelian" is ambiguous: representation categories are abelian
as categories under ordinary hypotheses, but the algebra is not commutative
and the braided center is not symmetric. The number \(24\) is a Mukai/Fock
generator count or a set of distinguished sectors, not a proof that the
category has exactly \(24\) simple objects. At \(\zeta_8\), the root-of-unity
object is non-semisimple before a tilting/negligible quotient; the full BKM
imaginary sector is infinite unless quotienting kills the bosonic imaginary
trace radical.

Heal. State the safe version:
\[
  \sigma_{V_u,V_v}
  =
  R_{\mathrm{Sieg,dyn}}(u-v;\tau,\rho,z)
  \tag{21}
\]
for distinguished evaluation/Fock modules in
\[
  \mathcal Z(\Rep^{E_1}(\mathbf H_{\Delta_5})).
  \tag{22}
\]
The \(24\) Mukai-labelled modules form a generating/test family for the
half-braiding, not a complete finite simple-object classification. A finite
MTC appears only after specifying either:
\[
  \Tilt_{\zeta_8}(\mathbf H_{\Delta_5})/\mathcal N_{\mathrm{negl}}
  \tag{23}
\]
or a non-semisimple Kerler--Lyubashenko category with modified trace.

Status. The half-braiding formula is conditional on the Hall--Drinfeld
double and Siegel dynamical \(R\)-matrix construction
(`coha_wall_crossing_platonic.tex:1729-1853`,
`drinfeld_center.tex:2424-2432`). The finite-rank MTC statement is
conditional until the tilting quotient, ribbon structure, and
non-degeneracy are proved at the required level.

Insertion recommendation. Replace `quantum_group_reps.tex:1178-1180` by a
remark with three sentences: evaluation modules give the probe family; their
half-braiding is (21); no finite simple-object count is asserted before the
chosen root-of-unity quotient or modified-trace category is constructed.

## ATTACK 8 -- Positive half representation categories are not automatically braided

Attack. CoHA passages correctly say `Y^+` is the positive half, but the
representation endpoint sometimes slides from \(Y^+\) to the full braided
category without restating the double/center hypotheses.

Failure mode. \(\CoHA(Q,W)\simeq Y^+\) is an associative algebra statement.
Its module category is monoidal only after a coproduct/topological bialgebra
structure is specified, and it is braided only after a quasi-triangular
double/center supplies an \(R\)-matrix. The path is:
\[
  \CoHA=Y^+
  \quad\leadsto\quad
  D(Y^+)=Y^-\bowtie Y^0\bowtie Y^+
  \quad\leadsto\quad
  \Rep(D(Y^+))\ \text{braided}.
  \tag{24}
\]

Heal. Every representation-category claim should name whether it uses
\(Y^+\), \(D(Y^+)\), or \(\mathcal Z(\Rep^{E_1}(Y^+))\). For
\(\mathbb C^3\), the chain is theorem-grade:
\[
  \CoHA(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)
  \hookrightarrow
  Y(\widehat{\mathfrak{gl}}_1)
  \twoheadrightarrow
  \mathcal W_{1+\infty}[\lambda]\text{-zero modes}.
  \tag{25}
\]
For general toric and \(K3\times E\), the named algebra identification is
conditional on the Hopf pairing/completion/Hall--BKM comparison.

Status. Proved for \(\mathbb C^3\); conditional for general toric beyond
published pairing hypotheses and for compact \(K3\times E\).

Insertion recommendation. At `coha_wall_crossing_platonic.tex:1533-1535`,
append "as a conditional representation-theoretic statement: the braided
category is attached to the double/center, not to the positive CoHA alone."
At `quantum_groups_foundations.tex:545-548`, keep the existing positive-half
discipline and cross-reference (24).

## Clean endpoint statement for manuscript insertion

```tex
\begin{definition}[Central representation category and modular quotient]
Let \(A\) be an \(E_1\)-chiral algebra.  Its central representation
category is
\[
  \Rep^{E_2}_{\mathrm{cent}}(A)
  :=
  \mathcal Z(\Rep^{E_1}(A))
  \simeq
  \Rep^{E_2}(Z^{\mathrm{der}}_{\mathrm{ch}}(A)).
\]
If this braided tensor category is rigid, finite, ribbon, and
factorizable, define
\[
  \mathcal MTC(A)
  :=
  \Rep^{E_2}_{\mathrm{cent}}(A)/\mathcal N_{\mathrm{negl}},
\]
where \(\mathcal N_{\mathrm{negl}}\) is the tensor ideal of negligible
morphisms.  In the non-semisimple root-of-unity regime one instead keeps
the finite tensor category together with a modified trace.
\end{definition}

\begin{conjecture}[CY-C, representation-theoretic endpoint]
Let \(\mathcal C\) be a CY-\(d\) category in the constructed locus, and let
\(A_\mathcal C=\Phi_2(\mathcal C)\) for \(d=2\), while
\(A_\mathcal C=A_\mathcal C^{(\Sigma_2,C)}\) is the framed
\(E_1\)-chiral output for \(d=3\).  There exists a quantum-group-like
quasi-Hopf object \(C(\mathcal C,q)\), with \(q\) fixed by the full
level/framing/\(R\)-matrix normalization, such that
\[
  \Rep_{\mathrm{adm}}(C(\mathcal C,q))^{\mathrm{mod}}
  \simeq
  \mathcal MTC(A_\mathcal C).
\]
At \(d=3\), the right side means the modular quotient of
\(\mathcal Z(\Rep^{E_1}(A_\mathcal C))\), not an \(E_2\)-structure on
\(A_\mathcal C\) itself.
\end{conjecture}
```

## Status ledger

- Proved elsewhere: ordinary Drinfeld center and half-braiding formalism;
  BZFN/Lurie equivalence
  \(\mathcal Z(\Rep^{E_1}(A))\simeq
  \Rep^{E_2}(Z^{\mathrm{der}}_{\mathrm{ch}}(A))\); generic
  Drinfeld--Kohno; root-of-unity tilting semisimplification; positive-level
  KL/Finkelberg equivalence.
- Proved in explicit local Hall loci: \(\CoHA(\mathbb C^3)=Y^+\) and the
  full-double passage where the Hopf pairing is constructed; selected toric
  cases under the published no-compact-4-cycle hypotheses.
- Conditional: CY-C at \(d=3\); \(K3\times E\) Hall--Drinfeld double as a
  representation category; finite root-of-unity MTC for the full BKM
  imaginary sector; all claims using a named \(C(\mathcal C,q)\) for general
  compact CY categories.
- False shortcuts: \(A\) is \(E_2\) at \(d=3\); full \(\Rep_q\) at a root of
  unity is an MTC; `CoHA = full Yangian`; a Drinfeld center is an averaging
  map; \(\kappa_{\mathrm{ch}}\) alone determines \(q\); \(24\) Mukai
  generators are a complete simple-object classification.

## Verification

No manuscript files were edited. No build was run. Verification consisted of
targeted `rg`, `nl -ba`, and `sed` reads of the requested manuscript files
and the local Drinfeld-center dependency.
