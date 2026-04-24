# Agent 10: Kapranov--Bezrukavnikov Descent / NCCR Axis

Date: 2026-04-24.

Scope owned: this note only.

Manuscript files read:

- `CLAUDE.md`
- `AGENTS.md`
- `chapters/theory/quantum_groups_foundations.tex`
- `chapters/examples/coha_wall_crossing_platonic.tex`
- `chapters/examples/toric_cy3_coha.tex`

Auxiliary anchors checked because the target chapters cite them for the descent theorem:

- `chapters/theory/cy_to_chiral.tex`
- `chapters/theory/braided_factorization.tex`
- `chapters/theory/en_factorization.tex`

## Claim Under Attack

The local-to-global descent claim is the assertion that toric or NCCR-local
CoHA data glue to a global positive half, and then to a chiral quantum group
or Drinfeld-center object:
\[
  \{(Q_\alpha,W_\alpha)\}_\alpha
  \quad\rightsquigarrow\quad
  Y^+(X)
  \quad\rightsquigarrow\quad
  D(Y^+(X)),\ \mathcal Z(\mathrm{Rep}^{E_1}(Y^+(X))).
\]
The vulnerable points are the NCCR cover, the derived Morita cocycle, the
orientation gerbe, the descent target (ordinary QC descent versus Weiss/Ran
factorisation descent), and the replacement of the toric fan outside the
toric locus.

Verdict: **HEAL, but only after replacing the single descent statement by a
two-level descent diagram with explicit obstruction classes.** The current
manuscript already contains most of the ingredients, but they must not be
compressed into the slogan "pairwise wall-crossing data alone."

## Local Anchors

- `quantum_groups_foundations.tex:15-60`: effective BPS positive geometry
  requires orientation data for determinant-line square roots and a derived
  critical atlas; without these the datum is not constructed.
- `quantum_groups_foundations.tex:80-126`: the positive half and Drinfeld
  double are conditional on a Hall product, PBW integrality, and a
  non-degenerate Serre-duality Hall pairing.
- `quantum_groups_foundations.tex:129-186`: toric effective geometry is a
  terminal degeneration of the chambered BPS datum, not the general template.
- `quantum_groups_foundations.tex:631`: the MO route is restricted to
  ADE/Kummer loci; global K3-moduli descent requires extra cocycle assembly.
- `quantum_groups_foundations.tex:718-783`: representability of \(G^T(X)\)
  is conditional on torus-fixed MO/KV hypotheses and does not construct
  global \(G(X)\) for arbitrary compact CY3s.
- `toric_cy3_coha.tex:15-27`: the positive-half Cech descent theorem is
  already conditional on an NCCR cover, orientation-compatible Morita data,
  residual \(\mathbb Z/2\) orientation-gerbe trivialisation, and KS
  wall-crossing.
- `toric_cy3_coha.tex:74-87`: the raw critical CoHA still needs orientation,
  compact-support convention, shifts, Tate twists, and completion when
  compared with hCS/factorisation observables.
- `toric_cy3_coha.tex:595-597`: the Klebanov--Witten NCCR is global and is
  not a chart; chart-wise quivers are different objects.
- `toric_cy3_coha.tex:684-700`: the conifold derived Morita equivalence uses
  a compact generator and Ext-vanishing.
- `toric_cy3_coha.tex:779-797`: the conifold Cech gluing theorem uses the
  Fourier--Mukai transition \(T_{+-}\), but the later Weiss section narrows
  what this hocolim computes.
- `toric_cy3_coha.tex:905-974`: ordinary Cech/QC descent and Weiss/Ran
  factorisation descent are two distinct targets; the two-chart conifold
  cover is not Weiss.
- `toric_cy3_coha.tex:1337-1351`: local \(\mathbb P^2\) has a real triple
  overlap and an explicit Cech cocycle \(\tau_{ki}\tau_{jk}\tau_{ij}=1\);
  triple-overlap data are therefore not disposable.
- `toric_cy3_coha.tex:1619-1721`: the toric chiral quantum group theorem
  assembles the global \(E_1\)-chiral algebra by hocolim and says pairwise
  wall-crossing data determine it.
- `toric_cy3_coha.tex:1815-1834`: the Drinfeld centre does not commute with
  homotopy colimits; global \(E_2\)-braiding cannot be assembled
  chart-by-chart.
- `toric_cy3_coha.tex:2136-2163`: extension to compact CY3s has four toric
  dependencies; the tilting-chart cover is conjectural.
- `toric_cy3_coha.tex:2173-2188`: \(K3\times E\) is not recovered by a toric
  specialisation; the non-toric Hall--Drinfeld double carries new
  automorphic and imaginary-Cartan data.
- `coha_wall_crossing_platonic.tex:703-731`: the CoHA-to-chiral MC map is
  constructed for \(\mathbb C^3\), conjectural for toric CY3 without compact
  4-cycles, and outside that locus lies in non-formal CY-A3.
- `coha_wall_crossing_platonic.tex:851-857`: conifold chiralisation is
  conditional on local-to-global \(E_1\)-chiral descent.
- `coha_wall_crossing_platonic.tex:1490-1519`: the open frontiers include
  Hopf-pairing non-degeneracy, chart-gluing descent outside \(\mathbb C^3\),
  and chiralisation of cluster mutation; the non-toric replacement is
  \(\mathfrak P^{\mathrm{BPS}}_\sigma(X)\).
- `cy_to_chiral.tex:4053-4077`: the tilting chart cover is conjectural for
  smooth projective CY3s; toric charts are explicit.
- `cy_to_chiral.tex:4124-4163`: toric chart gluing is stated as
  ProvedHere, with hocolim determined by pairwise wall-crossing.
- `cy_to_chiral.tex:4332-4372`: the \(E_1\) descent degeneration argument
  claims \(E_2^{p,*}=0\) for \(p\geq 2\) by strictness.
- `braided_factorization.tex:473-505` and `en_factorization.tex:103-149`:
  Weiss descent is separate from ordinary QC descent; the comparison is an
  equivalence exactly when the original cover is already Weiss.

## ATTACK / HEAL 1: NCCR Covers

ATTACK. "NCCR cover" is not a harmless synonym for a toric open cover.
The conifold itself exposes the problem: the Klebanov--Witten algebra is a
global NCCR of the affine node, not one of the two analytic \(\mathbb C^3\)
charts of the resolved conifold (`toric_cy3_coha.tex:595-597`). A cover by
affine toric patches supplies ordinary geometric opens; a Van den Bergh NCCR
supplies an endomorphism algebra of a tilting generator. These live in
different sites.

HEAL. Separate three layers:

1. geometric open atlas \(\mathfrak U=\{U_\alpha\}\);
2. local algebra models \(\Lambda_\alpha=J(Q_\alpha,W_\alpha)\), defined only
   after choosing a tilting/NCCR presentation on \(U_\alpha\);
3. global NCCR presentation \(\Lambda_X=\mathrm{End}_X(T)\), when it exists.

The Cech descent theorem should assert descent of the sheaf
\(\alpha\mapsto \mathrm{CoHA}(\Lambda_\alpha)\) only after the local
presentations are tied to the geometric opens by explicit Morita functors.
For the conifold, \(\Lambda_X=J_{\mathrm{KW}}\) is the global comparison
object; it is not an atlas element. For local \(\mathbb P^2\), the McKay
stack cover supplies the bridge because \(K_{\mathbb P^2}\simeq
[\mathbb C^3/\mathbb Z_3]^{\mathrm{res}}\) (`toric_cy3_coha.tex:1317-1335`).

Status recommendation: keep toric NCCR descent **conditional** unless the
specific geometry has a written local tilting cover and comparison with the
global NCCR.

## ATTACK / HEAL 2: Morita Cocycles

ATTACK. Derived Morita equivalence on pairwise overlaps is not enough. The
transition object is a class
\[
  [T_{\alpha\beta}]
  \in \mathrm{DPic}(\Lambda_{\alpha\beta}),
\]
and descent requires a specified 2-cell
\[
  \eta_{\alpha\beta\gamma}\colon
  T_{\beta\gamma}\otimes^{\mathbb L}_{\Lambda_\beta}T_{\alpha\beta}
  \xRightarrow{\sim} T_{\alpha\gamma}
\]
on triple overlaps. KS wall-crossing controls Hall/DT chamber
transformations; it does not automatically trivialise this derived-Picard
2-cocycle. The local \(\mathbb P^2\) section proves the point: the triple
overlap cocycle is explicit and reduces to \(x_0x_1x_2=1\), equivalently
\(\epsilon_1+\epsilon_2+\epsilon_3=0\)
(`toric_cy3_coha.tex:1337-1351`).

HEAL. The descent datum must be a 2-groupoid object:
\[
  \Bigl(
    \{\Lambda_\alpha\},
    \{T_{\alpha\beta}\},
    \{\eta_{\alpha\beta\gamma}\}
  \Bigr)
  \in \check C^\bullet(\mathfrak U,\mathrm{Alg}^{\mathrm{Mor}}_{E_1}).
\]
The global positive half is then
\[
  Y^{+,\mathrm{QC}}(X)
  :=
  \mathrm{Tot}\,
  \check C^\bullet
  \bigl(\mathfrak U,
  \mathrm{CoHA}(\Lambda_\alpha)\bigr),
\]
not merely a pairwise pushout. In a two-chart conifold cover the triple
condition is vacuous, but in local \(\mathbb P^2\) and larger fans it is a
real condition.

Status recommendation: replace "pairwise wall-crossing data alone" by
"pairwise Morita data plus the explicit derived-Picard triple cocycle; in
two-chart covers the triple cocycle is vacuous."

## ATTACK / HEAL 3: Orientation Gerbes

ATTACK. The determinant-line square root is an independent obstruction.
The target theorem names the residual \(\mathbb Z/2\) orientation-gerbe
trivialisation (`toric_cy3_coha.tex:17`) and says KS wall-crossing does not
derive it (`toric_cy3_coha.tex:26`). The universal positive-geometry grammar
also requires orientation data before the effective BPS geometry exists
(`quantum_groups_foundations.tex:24-60`). Therefore the orientation gerbe
cannot be hidden inside the Morita cocycle or the KS scattering diagram.

HEAL. Include an oriented refinement of the previous 2-groupoid. For each
chart choose \(o_\alpha\), a square root of the virtual determinant line of
the critical stack. On overlaps choose isomorphisms
\[
  \xi_{\alpha\beta}\colon
  T_{\alpha\beta}^*o_\beta \xRightarrow{\sim} o_\alpha.
\]
On triple overlaps the obstruction is
\[
  \delta\xi_{\alpha\beta\gamma}
  \in \check C^2(\mathfrak U,\mathbb Z/2).
\]
The oriented descent condition is
\[
  \delta[T]=1\ \text{in }\mathrm{DPic},
  \qquad
  \delta\xi=0\ \text{in }\check C^2(\mathfrak U,\mathbb Z/2).
\]
The first condition is Morita descent. The second is orientation descent.
They are independent.

Status recommendation: every global \(Y^+(X)\) built from critical CoHAs
should carry a superscript or phrase "oriented" until the determinant-line
trivialisation is explicitly supplied.

## ATTACK / HEAL 4: Weiss Versus QC Descent

ATTACK. Ordinary Cech descent computes a sheaf of associative algebras;
factorisation descent computes a Ran-space cosheaf. These are not the same.
The conifold section states the failure sharply: the two-chart cover
\(\{U_+,U_-\}\) is not Weiss, since a two-point configuration with one point
in each chart is contained in no single chart
(`toric_cy3_coha.tex:905-923`). The factorisation product on
\(U_+'\sqcup U_-'\) is invisible to the unrefined cover
(`toric_cy3_coha.tex:919`). The comparison is strict unless the cover is
already Weiss (`braided_factorization.tex:483-505`,
`en_factorization.tex:117-149`).

HEAL. Use two different global objects:
\[
  Y^{+,\mathrm{QC}}_\sigma(X)
  :=
  \mathrm{Tot}\,\check C^\bullet(\mathfrak U,\mathrm{CoHA}^{\mathrm{or}})
\]
for the motivic Hall / DT / associative \(E_1\) sheaf, and
\[
  Y^{+,\mathrm{FA}}_\sigma(X)
  :=
  \mathrm{hocolim}_{\mathfrak U^\sqcup}
  \Phi^{\mathrm{FA,or}}_3(U_\alpha)
\]
for the \(E_3\)-factorisation-stage object. There is a comparison
\[
  \iota_{\mathrm{Ran}}\colon
  Y^{+,\mathrm{QC}}_\sigma(X)\longrightarrow
  Y^{+,\mathrm{FA}}_\sigma(X)
\]
which is an equivalence only if the cover is Weiss or if all
\(\mathrm{Conf}_{\ge 2}\)-factorisation data are trivial. The categorical
\(R\)-matrix and Drinfeld-centre braiding live on the Weiss/Ran side; the
ordinary CoHA and DT characters live on the QC side.

Status recommendation: every theorem invoking an \(R\)-matrix, Drinfeld
centre, or \(E_3\)-factorisation output must name the Weiss refinement.

## ATTACK / HEAL 5: \(E_1\) Degeneration and Pairwise Data

ATTACK. Contractibility of \(E_1\) operation spaces does not by itself
force ordinary Cech cohomology \(E_2^{p,*}\) to vanish for \(p\ge 2\).
It says that the algebraic operations carry no braiding coherences; it does
not erase the topology of the cover nerve or the algebra-valued Cech
2-cocycles. The manuscript's broad statement in
`cy_to_chiral.tex:4332-4372` is therefore too strong if read literally.
Local \(\mathbb P^2\) has three charts and a triple-overlap cocycle
(`toric_cy3_coha.tex:1337-1351`), so the correct statement cannot be
"pairwise wall-crossing data alone" in that example.

HEAL. Replace the universal degeneration assertion by a scoped descent
lemma:

- for two-chart covers, \(C^p=0\) for \(p\ge 2\), so pairwise data suffice;
- for toric fans with triple overlaps, the \(p=2\) obstruction is the
  explicitly written derived-Picard/orientation cocycle and must be checked;
- for general NCCR covers, one needs either acyclicity of the oriented
  CoHA sheaf on the chosen site or an explicit proof that the Cech
  2-cocycle is a coboundary.

The \(E_1\) operad makes the maps strict once the descent datum is chosen;
it does not choose or trivialise that datum.

Status recommendation: toric chart gluing remains valid in examples where
the cocycle is written and checked; the general "ProvedHere for all toric
CY3" status should be read as conditional on those explicit cocycle checks.

## ATTACK / HEAL 6: Non-Toric Substitutes

ATTACK. The toric fan cannot be replaced by an "NCCR atlas" in the quintic,
generic \(K3\times E\), or compact CY3 cases. The toric hypothesis enters
through explicit McKay charts, equivariant localisation, MO stable envelopes,
and finite fan gluing (`toric_cy3_coha.tex:2136-2163`). For non-toric
geometries, the replacement named in the manuscript is not another fan but
the effective BPS positive geometry
\(\mathfrak P^{\mathrm{BPS}}_\sigma(X)\)
(`coha_wall_crossing_platonic.tex:1500-1519`,
`quantum_groups_foundations.tex:172-186`).

HEAL. The non-toric descent object is chambered and stack-theoretic:
\[
  \mathfrak P^{\mathrm{BPS}}_\sigma(X)
  =
  \bigl(
    \Gamma_X,\Gamma_{\mathrm{eff},\sigma}^+,
    \mathcal M^+_{\mathrm{eff},\sigma}(X),
    \phi_W,\Omega_\sigma,\mathfrak D^{\mathrm{KS}}_\sigma,
    \Theta^{\mathrm{BPS}}_\sigma
  \bigr),
\]
with oriented critical atlas, PBW integrality, and non-degenerate Serre
Hall pairing as separate hypotheses. Then
\[
  Y^+_\sigma(X)
  =
  H^\bullet_{\mathrm{eq}}
  \bigl(\mathcal M^+_{\mathrm{eff},\sigma}(X),\phi_W\bigr)
\]
exists only after those inputs. The Drinfeld double
\(D(Y^+_\sigma(X))\) is conditional on the pairing and completion.
For \(K3\times E\), the toric stalks are at most local tangents; the full
Hall--Drinfeld double has the imaginary rank-23 Cartan and \(\Delta_5\)
associator not visible on a toric fan (`toric_cy3_coha.tex:2173-2188`).

Status recommendation: outside toric/MO-accessible loci, write
"non-toric positive-geometry descent" rather than "NCCR descent."

## Healed Descent Diagram

The corrected descent is a two-level diagram with independent orientation
and Morita obstruction data.

```text
Input:
  oriented local critical charts
    (U_alpha, Q_alpha, W_alpha, o_alpha)

Morita/QC layer:
  Lambda_alpha = Jac(Q_alpha, W_alpha)
  T_alpha beta in DPic(Lambda_alpha beta)
  eta_alpha beta gamma :
      T_beta gamma tensor^L T_alpha beta  ==>  T_alpha gamma
  xi_alpha beta :
      T_alpha beta^* o_beta  ==>  o_alpha

  obstruction classes:
    delta[T] in Cech^2(U, DPic)
    delta[xi] in Cech^2(U, Z/2)

  if delta[T]=1 and delta[xi]=0:
    Y_sigma^{+,QC}(X)
      = Tot Cech(U, CoHA(Lambda_alpha, o_alpha))
      = R Gamma(X, Y_X^{+,or})

Weiss/Ran layer:
  U^sqcup = Weiss refinement generated by U
  F_alpha^{or} = Phi_3^{FA,or}(U_alpha)

  Y_sigma^{+,FA}(X)
      = hocolim_{U^sqcup} F_alpha^{or}

Comparison:
  iota_Ran : Y_sigma^{+,QC}(X) -> Y_sigma^{+,FA}(X)
  iota_Ran is an equivalence only if U is already Weiss
  or if Conf_{>=2}(X)-factorisation data are trivial.

Double/centre layer:
  if the Serre Hall pairing on Y_sigma^{+,QC}(X) is non-degenerate
  after completion:
      G_sigma(X) = D(Y_sigma^{+,QC}(X))

  if the Weiss/Ran factorisation category is constructed:
      R-matrix and Drinfeld-centre braiding are read from
      the two-point configuration sector of Y_sigma^{+,FA}(X).
```

In formulas:
\[
\begin{aligned}
Y^{+,\mathrm{QC}}_\sigma(X)
&=
\mathrm{Tot}\,
\check C^\bullet
\bigl(
  \mathfrak U,\,
  \{\mathrm{CoHA}(\Lambda_\alpha,o_\alpha),
    \mathrm{Ad}(T_{\alpha\beta}),
    \eta_{\alpha\beta\gamma},
    \xi_{\alpha\beta}\}
\bigr),\\
Y^{+,\mathrm{FA}}_\sigma(X)
&=
\mathrm{hocolim}_{\mathfrak U^\sqcup}
\Phi^{\mathrm{FA,or}}_3(U_\alpha),\\
G_\sigma(X)
&=
D(Y^{+,\mathrm{QC}}_\sigma(X))
\quad\text{only after the Hopf pairing is non-degenerate.}
\end{aligned}
\]

## Obstruction List

1. **NCCR existence.** A local Van den Bergh/NCCR model must exist on every
   chart. The conifold KW algebra is global, not a chart; generic compact
   CY3s need a different input.
2. **Local algebra-to-geometry comparison.** Each \(\Lambda_\alpha\) must be
   tied to \(U_\alpha\) by a tilting object or equivalence with the geometric
   chart category.
3. **Derived-Picard cocycle.** Pairwise tilting bimodules must close on
   triple overlaps as a 2-cocycle in \(\mathrm{DPic}\), with specified
   coherent 2-cells.
4. **Orientation gerbe.** Determinant-line square roots must glue; the
   obstruction is an independent class in \(\check C^2(\mathfrak U,\mathbb
   Z/2)\).
5. **Critical atlas.** The vanishing-cycle sheaves \(\phi_W\) must be
   globally compatible under Thom--Sebastiani and Morita transition.
6. **QC/Weiss target mismatch.** Ordinary Cech descent sees only the
   \(k=1\) stratum; factorisation descent requires the Weiss/Ran refinement.
7. **Hopf pairing.** The Drinfeld double requires a non-degenerate completed
   Hall pairing. This is proved for \(\mathbb C^3\) and specific toric cases,
   not in general.
8. **MO accessibility.** The stable-envelope route requires a rank \(\ge 2\)
   torus and suitable fixed loci; generic \(K3\times E\) and the quintic do
   not satisfy this hypothesis.
9. **Drinfeld centre versus hocolim.** The centre does not commute with
   homotopy colimits, so global \(E_2\)-braiding is not obtained by
   centering local charts.
10. **Non-toric replacement.** Outside toric loci, the replacement is
    \(\mathfrak P^{\mathrm{BPS}}_\sigma(X)\), not a disguised toric fan.

## Proposed Text

Target location: after the Cech-descent theorem in
`chapters/examples/toric_cy3_coha.tex`, or before the toric chiral quantum
group theorem.

```tex
\begin{remark}[Two descent targets and the orientation cocycle]
The positive-half descent has two outputs.  The ordinary Cech diagram of
NCCR charts produces the quasi-coherent Hall object
\[
Y^{+,\mathrm{QC}}_\sigma(X)
=
\mathrm{Tot}\,
\check C^\bullet\bigl(\mathfrak U,
\mathrm{CoHA}(\Lambda_\alpha,o_\alpha)\bigr),
\]
where the transition from \(\alpha\) to \(\beta\) is the action of a
tilting bimodule \(T_{\alpha\beta}\in\mathrm{DPic}(\Lambda_{\alpha\beta})\).
On triple overlaps the Morita cocycle
\[
T_{\beta\gamma}\otimes^{\mathbb L}T_{\alpha\beta}
\simeq T_{\alpha\gamma}
\]
and the determinant-line square-root cocycle
\(\delta o\in\check C^2(\mathfrak U,\mathbb Z/2)\) are separate
conditions.  Kontsevich--Soibelman wall-crossing identifies the Hall
chamber transformations; it does not trivialise the orientation gerbe.

The factorisation output is the Weiss-refined Ran object
\[
Y^{+,\mathrm{FA}}_\sigma(X)
=
\mathrm{hocolim}_{\mathfrak U^\sqcup}
\Phi^{\mathrm{FA,or}}_3(U_\alpha).
\]
The comparison
\[
Y^{+,\mathrm{QC}}_\sigma(X)\longrightarrow
Y^{+,\mathrm{FA}}_\sigma(X)
\]
is an equivalence only for a Weiss cover, or when all higher
configuration-space products are trivial.  Thus motivic-DT and ordinary
CoHA statements live on the QC side, while the \(R\)-matrix,
Drinfeld-centre braiding, and factorisation products live on the
Weiss/Ran side.
\end{remark}
```

Target location: after the non-toric positive-geometry paragraph in
`chapters/examples/coha_wall_crossing_platonic.tex`.

```tex
\begin{remark}[Non-toric replacement for the fan]
Outside the toric and MO-accessible loci there is no NCCR fan to glue.
The replacement datum is the chambered effective BPS positive geometry
\[
\mathfrak P^{\mathrm{BPS}}_\sigma(X)
=
\bigl(\Gamma_X,\Gamma^+_{\mathrm{eff},\sigma},
\mathcal M^+_{\mathrm{eff},\sigma}(X),\phi_W,
\Omega_\sigma,\mathfrak D^{\mathrm{KS}}_\sigma,
\Theta^{\mathrm{BPS}}_\sigma\bigr),
\]
equipped with oriented critical charts.  Its positive half
\[
Y^+_\sigma(X)=
H^\bullet_{\mathrm{eq}}
\bigl(\mathcal M^+_{\mathrm{eff},\sigma}(X),\phi_W\bigr)
\]
has a Drinfeld double only after Davison--Meinhardt PBW integrality and a
non-degenerate completed Serre Hall pairing are supplied.  The toric fan is
the terminal rational-polyhedral degeneration of this datum, not its
definition.
\end{remark}
```

## Final Status

Healed statement:

> Local-to-global descent is valid only as oriented Morita descent on the
> QC/Hall side plus Weiss/Ran descent on the factorisation side.  The
> obstruction classes are \(\delta[T]\in\check C^2(\mathfrak U,\mathrm{DPic})\),
> \(\delta o\in\check C^2(\mathfrak U,\mathbb Z/2)\), the critical-atlas
> compatibility of \(\phi_W\), the non-degeneracy of the Hall pairing, and
> the MO accessibility / non-toric positive-geometry hypotheses.

No manuscript files edited. No build run.
