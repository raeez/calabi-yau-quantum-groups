# Agent 14 -- Cross-Volume Consistency

Date: 2026-04-24.

Scope: cross-volume consistency for the chain-level holomorphic `E_3`
construction, chiral deformation theory, chiral Gerstenhaber brackets, and
the `K3 \times E` Stage-2 claims depending on them. Report only. No chapter,
appendix, compute, or bibliography file was edited.

## Sources Read

- `CLAUDE.md`.
- `.agents/skills/vol3-beilinson-loop/SKILL.md`.
- `.agents/skills/vol3-claim-verification/SKILL.md`.
- `.agents/skills/vol3-cross-volume-propagation/SKILL.md`.
- `chapters/theory/cy_to_chiral.tex`.
- `chapters/theory/cy3_chain_level_bridge.tex`.
- `chapters/theory/quantum_chiral_algebras.tex`.
- `chapters/theory/en_factorization.tex`.
- `chapters/theory/hochschild_calculus.tex`.
- `chapters/examples/cy_c_six_routes_convergence.tex`.
- `chapters/examples/k3e_cy3_programme.tex`.
- `chapters/examples/toric_cy3_coha.tex`.
- `chapters/examples/cy_d_kappa_stratification.tex`.
- `chapters/theory/gluing/sec_8_k3xe_master.tex`.
- `appendices/notation_conventions.tex`.
- Cross-volume anchors in
  `~/chiral-bar-cobar/chapters/examples/landscape_census.tex`,
  `~/chiral-bar-cobar/chapters/examples/w_algebras.tex`,
  `~/chiral-bar-cobar/chapters/examples/kac_moody.tex`,
  `~/chiral-bar-cobar/notes/cross_volume_aps.md`,
  `~/chiral-bar-cobar-vol2/chapters/theory/chiral_higher_deligne.tex`,
  `~/chiral-bar-cobar-vol2/chapters/theory/sc_chtop_heptagon.tex`, and
  `~/chiral-bar-cobar-vol2/notes/first_principles_cache_comprehensive.md`.

## Verification Surface

Tests/computations run: source-only adversarial audit with targeted `rg` and
`sed` reads. No TeX build and no compute test was run, in keeping with the
report-only scope and the session-end build discipline.

Files changed: this report only,
`notes/adversarial_swarm_20260424_hol_e3/agent_14_cross_volume_consistency.md`.

## Verdict

The live Vol III tree mostly contains the correct repairs: native CY3 output is
`E_1` after Stage-2 specialization; direct `E_3 -> E_2` restriction is
symmetric; non-symmetric braiding enters through the Drinfeld center; `CoHA` is
an associative/Hall source or positive half, not already
`\mathcal W_{1+\infty}`; and the principal `K3 \times E` BKM comparisons are
conditional rather than proved.

The remaining cross-volume risks are status hygiene and shorthand drift:
`K3 \times E` lines sometimes write `\kappa_{\mathrm{ch}}=3` where the
canonical invariant is `\kappa_{\mathrm{ch}}^{\mathrm{Heis}}=3`, one
`ProvedHere` tag packages a conditional global `hCS`/Hall comparison, and a
few summaries speak as if character-level or assembled-positive-half evidence
already gives the Hall-Drinfeld/Borcherds algebra.

## ATTACK -> HEAL Cycles

### Cycle 1 -- Bare or Axis-Conflated Kappa on `K3 \times E`

Claim attacked: the `K3 \times E` spectrum can be summarized as
`(\kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}})=(3,5)` or as an additive
relation between chiral and BKM weights.

Failure mode/proof: fatal if read as the compact CY3 Hodge supertrace. The
total-space Hodge/Euler axis gives zero for odd compact CY dimension, while
the Heisenberg rank and Borcherds weight are different axes. The formula
`\kappa_{\mathrm{BKM}}=\kappa_{\mathrm{ch}}+\chi(\mathcal O_{\mathrm{fiber}})`
fails already at `N=1`.

Local anchors: `chapters/theory/cy_to_chiral.tex:751-758`,
`chapters/theory/cy_to_chiral.tex:4688-4770`,
`chapters/theory/cy_to_chiral.tex:5448-5465`,
`chapters/examples/cy_c_six_routes_convergence.tex:68-81`,
`chapters/examples/k3e_cy3_programme.tex:4168-4178`,
`chapters/examples/cy_d_kappa_stratification.tex:1688-1707`,
`chapters/frame/preface.tex:1738-1762`.

Cross-volume anchors: `~/chiral-bar-cobar/chapters/examples/landscape_census.tex:5255-5272`,
`~/chiral-bar-cobar/chapters/examples/landscape_census.tex:5281-5284`.

Exact formulas/constants:

```tex
\kappa_{\mathrm{cat}}(K3\times E)=
\chi(\mathcal O_{K3})\chi(\mathcal O_E)=2\cdot 0=0.

\kappa_{\mathrm{ch}}(K3\times E)=
\sum_q(-1)^q h^{0,q}(K3\times E)=0.

\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3\times E)=3,\qquad
\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2,\qquad
\kappa_{\mathrm{BKM}}(\Delta_5)=10/2=5,\qquad
\kappa_{\mathrm{fiber}}(K3)=24.
```

Heal: keep the spectrum as
`{0,3,5,24}={\kappa_{\mathrm{cat}},\kappa_{\mathrm{ch}}^{\mathrm{Heis}},
\kappa_{\mathrm{BKM}},\kappa_{\mathrm{fiber}}}`. Any short line using
`(3,5)` should say `(\kappa_{\mathrm{ch}}^{\mathrm{Heis}},
\kappa_{\mathrm{BKM}})=(3,5)`, not total-space
`\kappa_{\mathrm{ch}}=3`.

Status recommendation: correction-level hygiene, not a new theorem. Treat
the four-axis invariant table as `ProvedHere` only for the displayed
computations; keep BKM comparisons conditional on the denominator/Hall bridge.

Remaining obligations: normalize the shorthand in chapter summaries and
prefatory prose when the parent integration pass edits manuscript files.

### Cycle 2 -- `CoHA = \mathcal W_{1+\infty}` Confusion

Claim attacked: `\mathrm{CoHA}(\mathbb C^3)` or the `K3 \times E` CoHA can be
identified directly with `\mathcal W_{1+\infty}` or with the full chiral BKM
object.

Failure mode/proof: false object type. CoHA is associative/Hall-side data. For
`\mathbb C^3`, the CoHA is the positive half `Y^+`; the
`\mathcal W_{1+\infty}` object arises only after Drinfeld-center/double
operations on the representation side. For `K3 \times E`, character equality
with a DT/Borcherds product is not an algebra comparison.

Local anchors: `chapters/theory/cy_to_chiral.tex:2708-2719`,
`chapters/theory/cy_to_chiral.tex:9568-9670`,
`chapters/examples/toric_cy3_coha.tex:2358-2373`,
`chapters/examples/toric_cy3_coha.tex:2706-2727`,
`chapters/theory/gluing/sec_8_k3xe_master.tex:545-565`,
`chapters/theory/gluing/sec_8_k3xe_master.tex:688-695`,
`chapters/theory/hochschild_calculus.tex:996-1020`.

Cross-volume anchors: `~/chiral-bar-cobar/chapters/examples/w_algebras.tex:7279`,
`~/chiral-bar-cobar/chapters/examples/kac_moody.tex:6591`,
`~/chiral-bar-cobar-vol2/chapters/theory/sc_chtop_heptagon.tex:2652-2665`,
`~/chiral-bar-cobar-vol2/notes/first_principles_cache_comprehensive.md:120-123`.

Exact formulas/constants:

```tex
\mathrm{CoHA}(\mathbb C^3)=Y^+,
\qquad
\mathcal W_{1+\infty}\;\text{appears on the Drinfeld-double/center side}.
```

For `K3 \times E`, the safe statement is character-level unless the comparison
maps have been constructed:

```tex
\chi_{\mathrm{gr}}\mathrm{CoHA}(K3\times E)=Z_{\mathrm{DT}}^{\mathrm{red}\,\prime}
```

does not imply
`\mathrm{CoHA}(K3\times E)\simeq U_{\mathrm{ch}}(\mathfrak g_{\Delta_5})`.

Heal: phrase the target as the Hall-Drinfeld double or chiral image under
conditional comparison, not raw CoHA:

```tex
G(K3\times E)=\mathcal D(Y^+_{\mathrm{Hall}}(K3\times E))
```

only under the Hall-Borcherds hypotheses.

Status recommendation: `CoHA(\mathbb C^3)=Y^+` is stable; `K3 \times E`
Hall-Drinfeld/BKM algebra comparison remains conditional/conjectural.

Remaining obligations: summaries such as `sec_8_k3xe_master.tex:1244-1253`
should distinguish assembled positive halves and character evidence from the
full BKM algebra output.

### Cycle 3 -- False Non-Symmetric Braiding from Direct `E_3` Restriction

Claim attacked: restricting a holomorphic `E_3` algebra to `E_2` directly
produces the non-symmetric quantum-group braiding.

Failure mode/proof: topologically false. Direct restriction
`E_3 -> E_2` sees configuration spaces in `\mathbb R^3`, and
`\pi_1(\mathrm{Conf}_2(\mathbb R^3))=0`; the induced binary interchange is
symmetric. Non-symmetric braiding is a representation/category-level
half-braiding from `Z(\mathrm{Rep}^{E_1}(A))`, not a direct restriction of
the native CY3 algebra.

Local anchors: `chapters/theory/cy_to_chiral.tex:150-162`,
`chapters/theory/cy_to_chiral.tex:430-463`,
`chapters/theory/hochschild_calculus.tex:2899-2912`,
`chapters/theory/en_factorization.tex:558-567`,
`chapters/frame/preface.tex:2549-2572`,
`chapters/frame/preface.tex:2732-2768`,
`appendices/notation_conventions.tex:100-130`.

Cross-volume anchors: `~/chiral-bar-cobar/notes/cross_volume_aps.md:136`,
`~/chiral-bar-cobar-vol2/chapters/theory/chiral_higher_deligne.tex:425`,
`~/chiral-bar-cobar-vol2/chapters/theory/chiral_higher_deligne.tex:819`.

Exact formulas/constants:

```tex
\Phi_3^{(\Sigma_2,C)}
= \operatorname{SpCh}_{\Sigma_2,C}\circ\Phi^{\mathrm{FA}}_3
\in E_1\text{-}\mathrm{ChirAlg}(C).

E_2\text{-braiding at }d\ge 3
\text{ lives on }
Z(\mathrm{Rep}^{E_1}(A_C)),
\text{ not on }A_C.
```

Heal: keep the CY3 output as native `E_1` after Stage-2 specialization; write
the `E_2`/braided object only after applying the Drinfeld center to the
representation category.

Status recommendation: direct-symmetric restriction is `ProvedHere`/standard
topology; non-symmetric braiding for `K3 \times E` target categories remains
conditional on the Stage-2/Hall comparison data.

Remaining obligations: preserve this sentence in every summary of the
holomorphic `E_3` construction: direct `E_3 -> E_2` is symmetric; quantum
braiding is center-theoretic.

### Cycle 4 -- Six Routes Misread as Six Applications of `\Phi`

Claim attacked: the six routes to `G(K3\times E)` are six applications of the
CY-to-chiral functor.

Failure mode/proof: false functorial accounting. There is one Stage-1
functorial object and one canonical `\Phi_3` route; the remaining routes are
different construction machines or different Stage-2 specialization data.
Their comparison maps are the substance of CY-C, not formal consequences of
applying `\Phi` repeatedly.

Local anchors: `chapters/theory/cy_to_chiral.tex:430-463`,
`chapters/examples/cy_c_six_routes_convergence.tex:15-18`,
`chapters/examples/cy_c_six_routes_convergence.tex:24-38`,
`chapters/examples/cy_c_six_routes_convergence.tex:45-65`,
`chapters/examples/cy_c_six_routes_convergence.tex:444-451`,
`chapters/examples/cy_c_six_routes_convergence.tex:928-932`,
`chapters/examples/cy_c_six_routes_convergence.tex:1963-2016`,
`chapters/examples/k3e_cy3_programme.tex:3949-3961`,
`chapters/examples/k3e_cy3_programme.tex:4175-4178`.

Exact formulas/constants:

```tex
\Phi_d^{(\Sigma,C)}
=\operatorname{SpCh}_{\Sigma,C}\circ\Phi_d^{\mathrm{FA}}.
```

For `K3 \times E`, only the canonical route is the direct
`\Phi_3^{(K3,E)}` specialization. The six-route list is a list of distinct
constructions/comparison targets.

Heal: state "six routes" as six construction machines or six specialization
data, not as six functor applications. Route-dependent generator ranks
`\rho^{R_i}\in\{3,12,24\}` are not `\kappa_{\mathrm{ch}}`.

Status recommendation: CY-C remains conjectural; the formal implication "if
all bridge isomorphisms are constructed, then convergence follows" can remain
`ProvedHere`, but the bridge closures themselves cannot.

Remaining obligations: integration owner should keep theorem/status tags
attached to the bridge maps, not to the informal route count.

### Cycle 5 -- CFG Ordinary Chern-Simons Confused with CY3 hCS

Claim attacked: the Calaque-Francis-Gwilliam ordinary `3d` Chern-Simons
factorization theorem proves the `6d` holomorphic Chern-Simons-to-Hall
comparison on a CY3.

Failure mode/proof: category and dimension mismatch. CFG supplies the
locally constant/topological grammar for ordinary `3d` Chern-Simons; the CY3
object is Dolbeault, holomorphic, and six-real-dimensional. The open map is
the oriented hCS-to-critical-CoHA comparison on the full descent/Ran nerve.

Local anchors: `chapters/theory/cy3_chain_level_bridge.tex:1-9`,
`chapters/theory/cy3_chain_level_bridge.tex:11-99`,
`chapters/theory/cy3_chain_level_bridge.tex:101-142`,
`chapters/theory/cy3_chain_level_bridge.tex:210-239`,
`chapters/theory/cy3_chain_level_bridge.tex:317-340`,
`chapters/theory/cy3_chain_level_bridge.tex:398-422`,
`chapters/theory/cy_to_chiral.tex:731-742`,
`chapters/theory/en_factorization.tex:558-567`.

Exact formula/status:

```tex
\Theta_{\mathrm{hCS}\to\mathrm{Hall}}^{\mathrm{or}}:
\mathrm{Obs}_{\mathrm{hCS}}^{q}(-,\mathfrak g)
\longrightarrow
\mathrm{CoHA}_{\mathrm{crit}}^{\mathrm{or}}(-)
```

is `ClaimStatusOpen` at `chapters/theory/cy3_chain_level_bridge.tex:410-422`.

Heal: cite CFG only as the ordinary/topological analogue. Do not use it as a
source theorem for `6d` hCS-to-Hall or for global CY3 chain-level functoriality.

Status recommendation: local/topological grammar may be proved or standard;
the global hCS-to-Hall comparison remains open/conditional.

Remaining obligations: when a theorem combines CFG, hCS, and cyclic
Hochschild, split chartwise/topological assertions from the global comparison.

### Cycle 6 -- CHL/Gritsenko-Clery Tower Overclaims

Claim attacked: the CHL/Gritsenko-Clery catalogue automatically supplies a
proved `K3 \times E` BKM/chiral algebra tower for every
`N\in\{1,2,3,4,6\}`.

Failure mode/proof: the automorphic denominator and its weight are not the
same as the CY3 hCS-to-Hall, equivariant CoHA, shuffle-lift, or Stage-2
specialization comparison. The catalogue controls candidate Borcherds products
and constants; it does not by itself construct the chiral algebra as the image
of `\Phi_3`.

Local anchors: `chapters/theory/cy_to_chiral.tex:719-749`,
`chapters/theory/cy_to_chiral.tex:760-801`,
`chapters/theory/cy_to_chiral.tex:806-807`,
`chapters/theory/cy_to_chiral.tex:5136-5144`,
`chapters/examples/k3e_cy3_programme.tex:3949-3961`,
`chapters/examples/toric_cy3_coha.tex:2358-2373`.

Exact formulas/constants:

```tex
\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2,\qquad
\kappa_{\mathrm{BKM}}(\Delta_5)=5.
```

For the crown case:

```tex
\operatorname{SpCh}_{K3,E}
\bigl(\Phi^{\mathrm{FA}}_3(\operatorname{Perf}(K3\times E))\bigr)
\simeq U_{\mathrm{ch}}(\mathfrak g_{\Delta_5})
```

is conditional on `op:cy3-hcs-hall-comparison` and the K3-fibre
Hall-Borcherds comparison.

Heal: separate the proved automorphic constants from the conditional
geometric/chiral realization. For `N=2`, require equivariant hCS-to-Hall and
specialization data; for `N=3,4,6`, require equivariant CoHA/shuffle lift,
`\Sigma_2^{(N)}`, and Hall-Borcherds denominator comparison.

Status recommendation: denominator-weight computations are proved/verified;
the Stage-2 chiral tower remains conditional except where the manuscript has a
separate constructed comparison.

Remaining obligations: keep Humbert/Niemeier and equivariant lift language out
of `ProvedHere` statements unless the comparison maps are actually built.

### Cycle 7 -- Wrong K3-Fibre Projection and Residual Dimension

Claim attacked: Stage-2 specialization projects to the K3 fibre or leaves a
chiral algebra on K3, so K3 fibre invariants can be substituted for total
`K3 \times E` invariants.

Failure mode/proof: wrong projection. `SpCh_{K3,E}` is holomorphic pushforward
along `p_E:K3\times E\to E`; K3 is the complex surface fibre
`\Sigma_2=p_E^{-1}(e)`, and the residual chiral algebra lives on the elliptic
curve `E`, hence is `E_1`-chiral. The value `2` belongs to
`\chi(\mathcal O_{K3})`, not to `\kappa_{\mathrm{cat}}(K3\times E)`.

Local anchors: `chapters/theory/cy_to_chiral.tex:731-742`,
`chapters/theory/cy_to_chiral.tex:751-758`,
`chapters/examples/k3e_cy3_programme.tex:4168-4178`,
`chapters/examples/cy_c_six_routes_convergence.tex:1990-1992`,
`appendices/notation_conventions.tex:329-333`,
`appendices/notation_conventions.tex:445-455`.

Cross-volume anchor: `~/chiral-bar-cobar/chapters/examples/landscape_census.tex:5255-5272`.

Exact formulas/constants:

```tex
p_E:K3\times E\to E,\qquad
\Sigma_2=p_E^{-1}(e)\simeq K3,
\qquad
\operatorname{SpCh}_{K3,E}=\text{holomorphic pushforward along }p_E.
```

```tex
\kappa_{\mathrm{cat}}(K3\times E)=0,\qquad
\kappa_{\mathrm{cat}}(K3)=2,\qquad
\kappa_{\mathrm{fiber}}(K3)=24.
```

Heal: whenever the surface fibre is used, write it as fibre data
`\Sigma_2=K3` or `\kappa_{\mathrm{fiber}}=24`; do not replace the total
space categorical or chiral invariant by the K3 fibre value.

Status recommendation: projection geometry is definitional/proved; any BKM
realization after this specialization remains conditional on the comparison
maps named above.

Remaining obligations: preserve the distinction between total CY3, fibre K3,
and residual curve E in Stage-2 diagrams and captions.

### Cycle 8 -- `ProvedHere` Tags on Conditional hCS/Hall/Borcherds Packages

Claim attacked: composite statements involving holomorphic `E_3`, CFG,
CY3-cyclic Hochschild, hCS-to-Hall, and BKM comparison can be marked
`ProvedHere` when only the chartwise/topological piece is established.

Failure mode/proof: status overreach. The live `K3 \times E` BKM theorems in
`cy_to_chiral.tex` are correctly marked conditional, but
`quantum_chiral_algebras.tex` packages a three-way `E_3` compatibility theorem
with a `ClaimStatusProvedHere` tag while the statement itself says global
compatibility is conditional on `\Theta_{\mathrm{hCS}\to\mathrm{Hall}}`.

Local anchors: `chapters/theory/quantum_chiral_algebras.tex:2528-2554`,
`chapters/theory/cy_to_chiral.tex:719-749`,
`chapters/theory/cy_to_chiral.tex:760-801`,
`chapters/theory/cy3_chain_level_bridge.tex:410-422`,
`chapters/theory/cy_to_chiral.tex:5136-5144`.

Exact status split:

```tex
\text{Chartwise/local KT-formality or topological CFG comparison: ProvedHere.}
```

```tex
\text{Global compact CY3 hCS--Hall/cyclic-Hochschild compatibility: Conditional/Open.}
```

Heal: split composite theorem status into two statements, or downgrade the
combined theorem to `ClaimStatusConditional`. The current `cy_to_chiral.tex`
K3xE BKM and bialgebra statements already have the right conditional status;
the main risk is propagation from the stronger tag in
`quantum_chiral_algebras.tex`.

Status recommendation: `thm:deligne-n3-three-e3` should be `ProvedHere` only
for the chartwise/local/formality component and `Conditional` for the global
compatibility. K3xE Hall/Borcherds comparisons should remain conditional.

Remaining obligations: integration owner should ensure theorem index tooling
does not count the combined global statement as a proved hCS-to-Hall theorem.

### Cycle 9 -- Chiral Gerstenhaber and Deformation-Theory Scope Drift

Claim attacked: the chiral Gerstenhaber bracket, the ordered chain-level
`K3 \times E` obstruction, and the symmetric shadow are interchangeable.

Failure mode/proof: false if the ordered/chiral operation is replaced by its
averaged shadow before the obstruction is evaluated. The Vol III local formula
uses ordered configuration/OPE data and a Mukai pairing; the symmetric average
is a later shadow. CoHA has its own associative/Koszul deformation theory; the
chiral obstruction is the `\Phi_3` image, not literally the same object.

Local anchors: `chapters/theory/hochschild_calculus.tex:996-1020`,
`chapters/theory/hochschild_calculus.tex:1038-1075`,
`chapters/theory/hochschild_calculus.tex:1204-1220`,
`chapters/theory/hochschild_calculus.tex:1478-1485`,
`appendices/notation_conventions.tex:413-455`,
`chapters/theory/cy3_chain_level_bridge.tex:101-142`.

Cross-volume anchors: `~/chiral-bar-cobar/notes/cross_volume_aps.md:149`,
`~/chiral-bar-cobar-vol2/chapters/theory/chiral_higher_deligne.tex:876`,
`~/chiral-bar-cobar-vol2/chapters/theory/chiral_higher_deligne.tex:966`.

Exact formula/status:

```tex
\chi_3^{\mathrm{chain}}(a_1,a_2,a_3;z_1,z_2,z_3)
=
\sum_{\sigma\in S_3}
\operatorname{sgn}(\sigma)
\frac{
\langle
\mu_3^{\mathrm{CoHA}}(a_{\sigma(1)},a_{\sigma(2)},a_{\sigma(3)}),
\Omega_{K3\times E}
\rangle_{\mathrm{Mukai}}
}{
(z_{\sigma(1)}-z_{\sigma(2)})
(z_{\sigma(2)}-z_{\sigma(3)})
(z_{\sigma(3)}-z_{\sigma(1)})
}.
```

Heal: keep the ordered chiral Hochschild/CE operation as the chain-level
object; only after closure by Arnold-type relations and the ordered-to-
symmetric comparison should it be recorded as a symmetric shadow class.

Status recommendation: local chain formula and shadow comparison can be
`ProvedHere` where explicitly computed; any claim identifying this with the
global hCS-to-Hall/BKM deformation package remains conditional.

Remaining obligations: cross-volume summaries should say "chiral image of the
CoHA obstruction" rather than "the CoHA obstruction itself" when discussing
`\chi_3` on the chiral side.

## Final Recommendations for Parent Integration

1. Normalize all `K3 \times E` short forms to the four-axis table:
   `\kappa_{\mathrm{cat}}=0`, total-space `\kappa_{\mathrm{ch}}=0`,
   `\kappa_{\mathrm{ch}}^{\mathrm{Heis}}=3`,
   `\kappa_{\mathrm{BKM}}=c_N(0)/2`, and `\kappa_{\mathrm{fiber}}=24`.
2. Keep native CY3 Stage-2 output in `E_1` and route non-symmetric braiding
   through `Z(\mathrm{Rep}^{E_1}(A))`.
3. Treat CFG as topological grammar, not as a proof of CY3 hCS-to-Hall.
4. Treat CHL/Gritsenko-Clery weights as automorphic/denominator data; the
   chiral realization needs the named comparison maps.
5. Split composite `ProvedHere` tags whenever a theorem contains both a proved
   chartwise/formality assertion and a conditional global hCS/Hall/Borcherds
   assertion.
