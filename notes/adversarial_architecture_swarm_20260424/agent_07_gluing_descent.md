# Agent 07: Gluing / Descent / Hocolim Architecture

Scope: hostile audit of Vol III gluing, descent, hocolim, Drinfeld-centre,
Drinfeld-double, Kummer, K3 x E, and six-route comparison claims against the
Vol I master synthesis and the Vol III design notes.

Files read:

- `CLAUDE.md`
- `AGENTS.md`
- `/Users/raeez/chiral-bar-cobar/notes/MASTER_PLATONIC_IDEAL_CROSS_VOLUME_BATTLE_HARDENED_2026_04_22.md`
- `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md`
- `notes/vol3_rearchitecture_proposal.tex`
- `notes/platonic_synthesis_post_adversarial.tex`
- `chapters/theory/cy_to_chiral.tex`
- `chapters/theory/gluing_chapter.tex`
- `chapters/theory/gluing/sec_1_abstract_framework.tex`
- `chapters/theory/gluing/sec_8_k3xe_master.tex`
- `chapters/theory/gluing/sec_9_obstructions.tex`
- `chapters/theory/gluing/sec_10_unifying.tex`
- `chapters/theory/hochschild_calculus.tex`
- `chapters/examples/cy_c_six_routes_convergence.tex`
- `chapters/examples/cy_c_six_routes_generator_level_platonic.tex`

Verdict:

The architecture is recoverable, but only with a hard separation:

1. `Phi_3` produces object-level `E_1`-chiral shadows on verified framed
   loci; it does not construct a global quantum vertex group.
2. Positive-half gluing by hocolim is not Drinfeld-double gluing.
3. Drinfeld centres and Drinfeld doubles do not commute with hocolims.
4. The sheaf-of-CoHAs on `Stk_Str` is conjectural as a uniform sheaf; the
   stratum-free compact-CY3 fallback is outside the fifteen non-empty cells.
5. `G(K3 x E)` is CY-C convergence data, not a proved common limit of the six
   routes.

## ATTACK_1: global `G(X)` silently promoted from candidate to construction

Claim attacked: Vol III constructs a global quantum vertex chiral group
`G(X)` or a globally-defined Hall bialgebra for general compact CY3 targets.

Failure mode:

- `chapters/theory/cy_to_chiral.tex:72-79` is correct: CY-A3 is an
  existence-and-rigidity theorem on objects and produces no global
  `G(C)`.
- `chapters/theory/cy_to_chiral.tex:99-105` puts global `G(C)` in S5:
  conjectural, obstructed by non-commutation of doubles with hocolims.
- `chapters/theory/cy_to_chiral.tex:8706-8730` defines `G(X)` only when the
  positive half, Hopf/stable-envelope pairing, completion, and framed
  specialisation are constructed; otherwise `G(X)` is conjectural data.
- `chapters/theory/cy_to_chiral.tex:9327-9345` states the `K3 x E`
  Hall--Borcherds double as a conjecture.
- The gluing chapter front matter overstates the result:
  `chapters/theory/gluing_chapter.tex:4-10` says local cocycles glue to a
  globally-defined Hall bialgebra, and `:73-89` says `K3 x E` verifies the
  master example.
- `chapters/theory/gluing/sec_8_k3xe_master.tex:531-541` says the ingredients
  "fuse into one Hopf-algebraic structure" and "the combined object is the
  chiral Hall--Drinfeld double".
- `chapters/theory/gluing/sec_8_k3xe_master.tex:748-770` says the double is
  well-defined and compatibility is established by the six-routes theorem.
  That conflicts with the CY-C status audit.

Exact formula:

```tex
G(X) := D(Y^+(\mathcal C_X))
```

is valid only after construction of `Y^+`, a nondegenerate Hopf pairing, the
completion, and bracket/centre comparison. In general:

```tex
D(\operatorname{hocolim}_\alpha Y^+_\alpha)
  \not\simeq
\operatorname{hocolim}_\alpha D(Y^+_\alpha).
```

HEAL_1:

Replace the gluing-chapter claim by:

```tex
The chart-wise cocycles assemble the global Hall positive-half, or a
sheaf-valued critical CoHA, on the loci where the cocycles are constructed.
The passage to a quantum vertex chiral group
G(X)=D(Y^+(\mathcal C_X)) requires a nondegenerate Hopf pairing,
completion, and bracket comparison; outside the constructed toric and
abelian loci this is CY-C-level conjectural data.
```

Status recommendation:

- `G(C^3)`: proved/elsewhere via `Y^+(\widehat{gl}_1)` plus known double.
- `K3 x E` Hall--Borcherds double: `ClaimStatusConjectured`.
- `K3` abelian branch `D(Y^+(g_K3))`: evidence/proved in the abelian branch,
  not identical to compact `K3 x E` Hall--Borcherds double.
- General compact CY3 `G(X)`: `ClaimStatusConjectured`.

## ATTACK_2: bar-hocolim is used too close to centre/double hocolim

Claim attacked: bar/cobar hocolim descent is enough to globalise centres,
braidings, Drinfeld doubles, or all shadow data.

Failure mode:

- `chapters/theory/cy_to_chiral.tex:4288-4313` correctly states the
  centre-hocolim obstruction:

```tex
\operatorname{hocolim}_\alpha Z(Rep^{E_1}(CoHA_\alpha))
  \longrightarrow
Z(Rep^{E_1}(\operatorname{hocolim}_\alpha CoHA_\alpha))
```

  is not an equivalence in general. For the conifold, the hocolim of local
  centres has dimension `3`, the global centre has dimension `1`, and the
  obstruction is `2`.
- `chapters/theory/cy_to_chiral.tex:4317-4336` states

```tex
B^{E_1}(\operatorname{hocolim}_I D)
  \simeq
\operatorname{hocolim}_I B^{E_1}(D)
```

  for any finite-poset diagram and marks it `ClaimStatusProvedHere`.
  The proof then calls bar both a left derived functor and, correctly in
  bar-cobar, a right adjoint. A right adjoint preserves limits, not arbitrary
  homotopy colimits. This is too broad unless restricted to a Koszul locus
  where the comparison map is verified.
- Even if the bar comparison holds on a Koszul finite diagram, it proves a
  shadow/coalgebra statement, not an `E_2` centre statement and not a
  Drinfeld-double statement.

HEAL_2:

Narrow the bar-hocolim theorem to a comparison theorem:

```tex
For a finite diagram of cofibrant, conilpotent, Koszul `E_1`-chiral algebras
whose transition maps are `E_1`-equivalences, the canonical comparison map

B^{E_1}(\operatorname{hocolim}_I A_i)
  \longrightarrow
\operatorname{hocolim}_I B^{E_1}(A_i)

is an equivalence on the stated Koszul locus.
```

Then add:

```tex
No centre, `E_2` braiding, Hopf pairing, antipode, or Drinfeld double is
transported by this statement. Those structures require the separate global
centre/double construction, and Proposition `prop:center-hocolim` records the
obstruction.
```

Status recommendation:

- Bar-hocolim on arbitrary finite diagrams: downgrade to conditional until a
  precise left-adjoint/Koszul-dual argument is supplied.
- Centre-hocolim non-commutation: keep as theorem-level obstruction where the
  conifold dimension calculation is verified.

## ATTACK_3: the fifteen-cell sheaf contradicts the stratum-free fallback

Claim attacked: every CY3 lies in a non-empty stratum cell, and the sheaf of
CoHAs on `Stk_Str` covers all compact CY3s uniformly.

Failure mode:

- `chapters/theory/gluing_chapter.tex:16-19` says every CY3 carries a
  non-empty stratum-set and the classification reduces to the sixteen
  power-set cells.
- `chapters/theory/gluing/sec_1_abstract_framework.tex:630-690` excludes the
  empty subset and calls the remaining fifteen the non-empty cells.
- `chapters/theory/gluing/sec_10_unifying.tex:623-648` then introduces a
  "stratum-free fall-back" for the quintic, bicubic, and Schoen threefold:
  no toric structure, no residual `Aut_s^0`, no finite orbifold cover, no
  Humbert-lifted period structure. The sheaf is said to extend there as a
  constant sheaf.
- `chapters/theory/gluing/sec_10_unifying.tex:474-526` marks the sheaf of
  CoHAs as conjectural.
- `chapters/theory/gluing/sec_10_unifying.tex:735-749` says the descent axiom
  for `Stk_Str` still needs verification stratum by stratum.
- `chapters/theory/gluing/sec_10_unifying.tex:751-754` says the cocycle
  cohomology is not computed in any cell beyond cell `1`.

HEAL_3:

Choose one of two consistent architectures:

1. Keep a strict fifteen-cell stack:

```tex
`Stk_Str^{nonempty}` classifies CY targets with at least one explicit
equivariance/period gluing datum. Compact CY3s with no such datum are not
objects of the fifteen-cell cocycle classification; they enter through the
Davison--Meinhardt critical-CoHA fallback.
```

2. Add a genuine base cell:

```tex
Cell `0` is the stratum-free critical-CoHA cell. Its sheaf is constant with
stalk `CoHA_crit(X)` and has no transition cocycle. The fifteen non-empty
cells are the explicit cocycle cells.
```

Status recommendation:

- Uniform sheaf `underline H` on all `Stk_Str`: `ClaimStatusConjectured`.
- Fifteen-cell support and named cocycle targets: theorem-level only
  pointwise where the cited stratum data are actually constructed.
- Stratum-free compact CY3 fallback: separate critical-CoHA fallback, not
  proof of the fifteen-cell descent theorem.

## ATTACK_4: Cech--Ran descent assumes local coordinates supply global CoHA

Claim attacked: an analytic `C^3` cover plus FM kernels constructs
`PhiFA_3(Perf(X))` for compact CY3s and recovers K3 CoHA globally.

Failure mode:

- `chapters/theory/gluing/sec_10_unifying.tex:831-843` uses analytic
  polydisc charts. That is valid as complex geometry, but a local
  biholomorphism to `C^3` does not by itself identify the moduli of sheaves
  on compact `X` with the Jordan-loop critical CoHA.
- `chapters/theory/gluing/sec_10_unifying.tex:889-913` takes local tilting
  data on `C^3` and identifies each chart-wise critical CoHA with
  `Y^+(\widehat{gl}_1)`. This is a local model, not a global compact-CoHA
  theorem.
- `chapters/theory/gluing/sec_10_unifying.tex:935-974` correctly tags the
  Cech--Ran descent theorem as conjectural, but item (iii) at `:963-966`
  says naturality follows from Bondal--Orlov FM-kernel naturality. That
  does not prove CY3 morphism functoriality of `Phi_3`.
- `chapters/theory/gluing/sec_10_unifying.tex:1033-1054` says the
  product-compatible cover of `K3 x E` recovers globally the
  Schiffmann--Vasserot K3 CoHA / preprojective Yangian. The same subsection
  then marks the super-Yangian emergence conjectural at `:1056-1072` and
  lists the missing descent frontiers at `:1106-1124`.

HEAL_4:

Replace the compact CY3 descent theorem's operative text by:

```tex
Assume an analytic `C^3` cover, holomorphic transition FM-kernel datum,
orientation data for the BBJ/PTVV d-critical charts, and compatibility of
the chart-wise critical CoHAs with the global compact moduli stack. Then
the Ran--Cech total complex is a candidate model for `PhiFA_3(Perf(X))`.
Functoriality under CY3 morphisms is a further conjectural compatibility
with cyclic A-infinity/FM kernels, not a consequence of Bondal--Orlov alone.
```

Proof obligations:

- Construct the transition FM kernels on every pairwise overlap.
- Prove triple and quadruple homotopy coherence.
- Verify `bar partial`-closedness in the Dolbeault bicomplex.
- Compare local d-critical potentials with the global PTVV/BBJ orientation.
- For `K3 x E`, compute the `24` curve-stalk assembly and the
  `Y_osp(4|20)` RTT/current presentation separately.

Status recommendation:

- Cech--Ran descent on compact CY3: keep `ClaimStatusConjectured`.
- Singleton toric charts: theorem-level local input.
- `K3 x E` recovery of the full Hall/Borcherds object: conjectural pending
  D1--D3.

## ATTACK_5: K3 x E quasi-NCCR substitute is used as if it were a global NCCR

Claim attacked: the Serre-equivariant quasi-NCCR is enough to construct the
global Hall--Drinfeld double of `K3 x E`.

Failure mode:

- `chapters/theory/gluing/sec_9_obstructions.tex:1084-1153` proves the
  five-fold obstruction to a global NCCR on `K3 x E`.
- `chapters/theory/gluing/sec_9_obstructions.tex:1155-1181` is precise:
  the quasi-NCCR provides local tilting data for Davison--Meinhardt critical
  CoHA and `PhiFA_3`; it does not provide a global `End(T)`-representation.
- `chapters/theory/gluing/sec_8_k3xe_master.tex:558-574` marks assembly of
  the `24` elliptic positive halves as `ClaimStatusProvedHere`.
- `chapters/theory/gluing/sec_8_k3xe_master.tex:694-726` marks the
  `Delta_5` associator as `ClaimStatusProvedHere`, but it is phrased as
  endowing the Hall--Drinfeld double with a quasi-Hopf associator.
- The object being endowed is precisely what
  `chapters/theory/cy_to_chiral.tex:9327-9345` leaves conjectural.

Exact constants:

```tex
\Phi_{10} = 64\,\Delta_5^2,
\qquad
\kappa_{BKM}(\Delta_5)=c_1(0)/2=10/2=5,
\qquad
\mathrm{Spec}_{\kappa_\bullet}(K3\times E)=\{0,3,5,24\}.
```

HEAL_5:

Split the statements:

```tex
The reduced DT/Igusa denominator and the Gritsenko--Nikulin Borcherds
product determine a graded-character shadow with
`\kappa_{BKM}=5`. Assuming the Hall positive half
`Y^+_{Hall}(K3 x E)`, nondegenerate Hopf pairing, completion, and
bracket comparison have been constructed, the Borcherds cocycle supplies
the quasi-Hopf associator of the Hall--Drinfeld double. Without those
data, `Delta_5` is an automorphic cocycle/denominator, not a constructed
Hopf pairing.
```

Status recommendation:

- `Phi_10 = 64 Delta_5^2` and `kappa_BKM=5`: theorem-level automorphic
  constants.
- Positive-half character shadow: theorem/conditional depending on the
  exact local input.
- Hall--Drinfeld double and associator as a quasi-Hopf algebra on `K3 x E`:
  conditional/conjectural.

## ATTACK_6: six-route comparison is sometimes stated as established

Claim attacked: the six routes to `G(K3 x E)` are already a proved
convergence theorem or six presentations of one algebra.

Failure mode:

- `chapters/examples/cy_c_six_routes_convergence.tex:15-17` is correct:
  CY-C is the last open conjecture; comparison maps and pairwise
  isomorphisms are the content, not a derivation from functoriality.
- `chapters/examples/cy_c_six_routes_convergence.tex:549-553` is correct:
  CY-C remains conjectural; only two pairwise bridges are unconditional.
- `chapters/examples/cy_c_six_routes_generator_level_platonic.tex:190-205`
  proves no simultaneous six-way isomorphism exists because the generator
  ranks stratify as `{3,12,24}`.
- `chapters/examples/cy_c_six_routes_generator_level_platonic.tex:216-260`
  identifies the pentagon colimit with `G(K3 x E)` only conditionally.
- `notes/platonic_synthesis_post_adversarial.tex:1480-1486` corrects another
  failure mode: only three routes admit `(Sigma_2,C)` cycle-class indexing;
  the other three consume non-cycle-class data.
- `chapters/theory/gluing/sec_8_k3xe_master.tex:763-770` conflicts with
  this by saying compatibility is established by a six-routes theorem.

HEAL_6:

Use this replacement everywhere the gluing chapter references six routes:

```tex
The six routes supply six different construction machines. Their scalar
and presentation-level invariants agree on specified loci, but the
chiral-algebra convergence is CY-C: a conjectural pentagon/bridge diagram
with arrows of type isomorphism, injection, and surjection. The common
object is the conditional colimit `G(K3 x E)`, not a simultaneous
six-way isomorphism and not six applications of `Phi_3`.
```

Status recommendation:

- Route separation and invariant stratification: `ClaimStatusProvedHere`.
- Pairwise bridge diagram / colimit identification with `G(K3 x E)`:
  `ClaimStatusConditional` or `ClaimStatusConjectured`, depending on the
  named bridge.
- Any sentence saying "compatibility is established" must be weakened to
  "compatibility is the CY-C conjecture, with the proved pieces listed in
  the six-routes status audit".

## ATTACK_7: `Phi` as a sheaf map on `Stk_Str` overstates morphism functoriality

Claim attacked: the CY-to-chiral functor acts on `Stk_Str` as a sheaf map
and the full `r_CY` theory is its monodromy.

Failure mode:

- The Vol I synthesis at
  `/Users/raeez/chiral-bar-cobar/notes/MASTER_PLATONIC_IDEAL_CROSS_VOLUME_BATTLE_HARDENED_2026_04_22.md:721`
  says the two-stage factorisation is the canonical reading and cells index
  Vol I/II/III data. It does not prove global sheaf functoriality.
- `chapters/theory/cy_to_chiral.tex:787-803` says the collection
  `{Phi_d}` is a correspondence programme, not a single functor.
- `chapters/theory/cy_to_chiral.tex:810-815` keeps morphism functoriality
  conjectural and puts `E_2` braiding on the Drinfeld centre, not on
  `Phi(C)` itself.
- `chapters/theory/gluing/sec_10_unifying.tex:1126-1142` says `Phi` acts on
  `Stk_Str` as a sheaf map and `r_CY` is the monodromy of the `Phi`-sheaf.
  That wording is too strong unless explicitly marked conjectural.

HEAL_7:

Replace with:

```tex
On constructed cells, the object-level assignment
`Phi_3^{(Sigma_2,C)} = SpCh_{Sigma_2,C} \circ PhiFA_3` transports the
cell cocycle to an `E_1`-chiral shadow. A genuine sheaf map on
`Stk_Str`, functorial in CY morphisms and compatible with closed loops in
the stratum stack, is the conjectural morphism-level refinement of the
correspondence. The seven faces of `r_CY` are presently evaluations of
constructed cell shadows plus conjectural monodromy data, not a proved
global monodromy theorem.
```

Status recommendation:

- Object-level cell evaluations: theorem/conditional per cell.
- `Phi` as sheaf map on `Stk_Str`: `ClaimStatusConjectured`.
- `r_CY` as monodromy of that sheaf: conjectural synthesis unless each loop
  is reduced to constructed arrows.

## Primary-source anchors used locally

- Ben-Zvi--Francis--Nadler 2010, JAMS 23: Drinfeld centre / higher centre
  framework cited in `cy_to_chiral.tex`.
- Beilinson--Drinfeld 2004, `Chiral Algebras` section 3.4: chiral descent.
- Francis--Gaitsgory 2012: chiral Koszul / Ran totalisation.
- Lurie `Higher Algebra` 5.1.2 and `HTT` 6.2.3: Dunn additivity and sheaves
  on higher stacks.
- Toën--Vezzosi `arXiv:math/0404373`: homotopy descent on derived stacks.
- Davison--Meinhardt `arXiv:1601.02479`: critical CoHA and vanishing cycles.
- Bridgeland--King--Reid `arXiv:math/9908027`: finite McKay descent.
- Borcherds 1995/1998 and Gritsenko--Nikulin: Borcherds lifts and
  `kappa_BKM=c(0)/2`.
- Costello--Gwilliam / Costello--Li: factorisation algebras and holomorphic
  twist locality.

## Files changed

- Created `notes/adversarial_architecture_swarm_20260424/agent_07_gluing_descent.md`.

No manuscript, compute, or cross-volume source file was edited.

## Computations / tests run

No mathematical compute tests were run. This was a report-only adversarial
audit. Shell verification was limited to `git status --short`, `rg`, `wc`,
`nl -ba`, `sed`, and a file-existence check for the target report.

## Open questions

1. Decide whether the gluing chapter uses a strict fifteen-cell
   non-empty-stratum stack plus external stratum-free fallback, or a sixteen
   cell stack with an explicit cell `0`.
2. Supply or downgrade the bar-hocolim theorem; the current proof uses a
   right adjoint as if it preserved homotopy colimits.
3. Write the exact positive-half-to-double proof obligation for
   `K3 x E`: positive half, pairing, completion, bracket comparison,
   and centre compatibility.
4. Replace every "six routes establish compatibility" sentence by the CY-C
   status table language: proved invariants, conditional bridges,
   conjectural colimit.
5. Keep `Phi` as a sheaf map on `Stk_Str` conjectural until morphism
   functoriality and loop-monodromy coherence are proved.
