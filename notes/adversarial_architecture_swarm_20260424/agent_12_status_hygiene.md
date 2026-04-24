# Agent 12 -- Status Hygiene Attack-Heal Report

Date: 2026-04-24

Scope: `FRONTIER.md`, `metadata/theorem_registry.md`,
`metadata/claims.jsonl`, `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md`,
`notes/vol3_rearchitecture_proposal.tex`,
`notes/wave12_frontier_inventory.tex`, and theorem-status material in
`chapters/**.tex`.

Mode: report-only. No source edits, no commits, no pushes, no destructive git.

## Executive status

The current tree has one healthy status spine and several stale or
over-promoted pockets.

Healthy spine:

- CY-A_3 is conditional/object-level on verified framed loci, not an
  arbitrary CY_3 functorial theorem.
- CY-C and global `G(X)` remain conjectural outside specified value-level
  or generator-level loci.
- Six routes to `G(K3 x E)` are six different constructions, not six
  applications of `\Phi`.
- Universal `\kappa_{\mathrm{BKM}} = c_N(0)/2` is theorem-level for the
  automorphic/Borcherds weight identity, while geometric CY-host
  realization is separate and not automatically proved.
- The BKM-side K3 object is the Hall--Drinfeld double, not the historical
  "K3 Yangian" shorthand.

Main hygiene failures:

- `metadata/claims.jsonl` and some chapter blocks over-promote
  conditional or conjectural material as `ProvedHere`.
- `FRONTIER.md` preserves older memorial sections whose labels and theorem
  statuses now conflict with the current spine.
- `metadata/theorem_registry.md` reports `Open = 0`, while body text still
  contains at least one `\ClaimStatusOpen{}`.
- The Super-Yangian block in `k3_chiral_bialgebra_platonic.tex` claims to
  discharge an open conjecture, contradicting `FRONTIER.md`, Wave 12, and
  the battle-hardened note.

## ATTACK_1 -- CY-A_3 "proved" is overbroad outside H1--H4

Attack:

- `FRONTIER.md:911` says "CY-A_3 PROVED (inf-categorical)" in an older
  memorial section.
- `metadata/claims.jsonl:966` records `thm:cy-to-chiral-d3` as
  `ProvedHere`.
- `notes/vol3_rearchitecture_proposal.tex:149-155` still asks the
  introduction to present a "completed functor" and "CY-A proved (all d)".

Contrary anchors:

- `chapters/theory/cy_to_chiral.tex:37-39` says arbitrary CY morphism
  functoriality and general compact non-formal CY_3 chain strictification
  are deferred to `conj:phi-d-functoriality` and the compact CY_3 problem.
- `chapters/theory/cy_to_chiral.tex:92-105` separates chain/object-level
  assignment from `(infinity,1)` functoriality and says global `G(C)` is
  not produced there.
- `chapters/theory/cy_to_chiral.tex:793` states: proved functorially at
  `d <= 2`; framed object-level at `d = 3`; morphism functoriality remains
  conjectural.
- `chapters/theory/cy_to_chiral.tex:4810` marks `thm:cy-to-chiral-d3` as
  conditional under H1--H4.
- `chapters/theory/cy_to_chiral.tex:4873-4899` explicitly excludes
  arbitrary CY_3 morphism functoriality, hCS-to-Hall comparison, and global
  quantum vertex group construction.
- `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:13-15`
  gives the same boundary: Stage 1 canonicity holds on constructed
  holomorphic-twist/framing loci; arbitrary compact non-formal CY_3 is
  outside the strict theorem unless the hypotheses are witnessed.

HEAL_1:

- Status recommendation: `thm:cy-to-chiral-d3` should be indexed as
  `Conditional`, not unqualified `ProvedHere`.
- Wording recommendation: "CY-A_3 object-level theorem on verified framed
  H1--H4 loci; arbitrary morphism functoriality and global `G(X)` remain
  conjectural."
- Proposed edits:
  - `notes/vol3_rearchitecture_proposal.tex:149-155`: replace "completed
    functor" / "CY-A proved (all d)" with the later, correct table language
    already present at `notes/vol3_rearchitecture_proposal.tex:666-682`.
  - `FRONTIER.md:911`: either move the old memorial block into an explicit
    archive or restate it as "CY-A_3 conditional/object-level on framed
    loci".
  - Regenerate `metadata/claims.jsonl` so `thm:cy-to-chiral-d3` no longer
    outranks its body status.

## ATTACK_2 -- Global `G(X)` representability is over-promoted

Attack:

- `chapters/theory/quantum_groups_foundations.tex:540-610` presents
  "Functorial existence of `G(X)`: a representability theorem".
- `chapters/theory/quantum_groups_foundations.tex:570` has
  `thm:qgf-G-X-representability` with `\ClaimStatusProvedHere`.
- `metadata/claims.jsonl:1355` records this as `ProvedHere`.

Contrary anchors:

- `chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex:288-291`
  says the theorem does not construct global `G(X)` and generic compact
  CY_3 `G(X)` is unconstructed.
- `chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex:389-391`
  marks existence/obstruction for `G(X)` as `ClaimStatusConjectured`.
- `chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex:1237-1271`
  preserves the open problem: no global `G(X)` for every compact CY_3.
- `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:352`
  says K3 x E value-level equality at `N=1` does not prove global CY-C or
  arbitrary morphism functoriality.
- `notes/vol3_rearchitecture_proposal.tex:626-647` says global morphism
  functoriality remains conjectural and the six constructions have
  conjectural convergence.

HEAL_2:

- Status recommendation: downgrade `thm:qgf-G-X-representability` to a
  conditional representability criterion, or to a conjecture if it asserts
  existence for smooth proper compact CY_3 targets.
- Safe theorem split:
  - Proved/standard: formal presentability properties of the ambient
    category of chiral quantum groups, if cited correctly.
  - Conditional: Brown--Lurie-style representability if the functor
    `F_X` is accessible, preserves the required limits, and the CoHA/MO
    comparison data are actually constructed.
  - Conjectural: global functorial `G(X)` for arbitrary compact CY_3.
- Proposed edits:
  - `chapters/theory/quantum_groups_foundations.tex:540-610`: rename the
    section from a theorem of existence to a representability criterion.
  - `metadata/claims.jsonl`: expected generated status should be
    `Conditional` or `Conjectured`, not `ProvedHere`.

## ATTACK_3 -- Super-Yangian is claimed solved in one chapter but open everywhere else

Attack:

- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5014` says the
  chapter "discharges the conjectural super-Yangian status".
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5046-5052` states
  `thm:kcb-super-yangian-serre-BKM` as `ProvedHere`.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5176-5181`,
  `5222-5227`, `5286-5291`, and `5334-5339` mark PBW, coproduct,
  universal R-matrix, and Hopf axioms as `ProvedHere`.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5451-5468` again
  says the Super-Yangian conjecture is resolved.
- `metadata/claims.jsonl:399-403` records these as `ProvedHere`.

Contrary anchors:

- `FRONTIER.md:87` keeps the Super-Yangian open.
- `FRONTIER.md:159` says the `Y_{osp(4|20)}` candidate remains OPEN.
- `FRONTIER.md:792-812` lists unresolved rank `(4,20)` reflection
  equation, Berezinian denominator, spectral flow automorphism, and
  `osp` versus `so` decision.
- `notes/wave12_frontier_inventory.tex:174-178` says the explicit
  coproduct/relations remain conjectural at Hopf-superalgebra level.
- `chapters/theory/en_factorization.tex:1496-1524` keeps
  `Y_{osp}(4|20)` as `ClaimStatusConjectured`.
- `chapters/theory/phi_universal_trace_platonic.tex:1324-1348` calls it
  an open K3 Super-Yangian; all-orders quantisation and super-KT formality
  are open.
- `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:91` says
  one-loop hCS is proved here but all-orders quantisation is conjectural.

HEAL_3:

- Status recommendation: the Super-Yangian should remain `Conjectured`
  unless the missing reflection equation, Berezinian denominator, spectral
  flow, and all-orders quantisation are supplied in-tree or by precise
  citations.
- Proposed split:
  - Proved/conditional: a candidate Borcherds-current presentation and
    finite-depth checks, with exact checked order stated.
  - Conjectural: actual `Y_{osp}(4|20)` Hopf-superalgebra, full PBW,
    coproduct, universal R-matrix, and Hopf axioms.
- Proposed edits:
  - `chapters/examples/k3_chiral_bialgebra_platonic.tex:5014-5468`:
    remove "discharges/resolves the conjecture"; replace with "candidate
    presentation and finite-order checks".
  - Downgrade `thm:kcb-super-yangian-serre-BKM` and dependent PBW/
    coproduct/R-matrix/Hopf statements to `Conditional` or `Conjectured`
    unless the missing data are explicitly proved.
  - `FRONTIER.md:857`: if the older memorial is kept, replace stale
    `Y(gl(4|20))` language with the current `Y_{osp}(4|20)` candidate or
    mark the block as historical.

## ATTACK_4 -- Class M `E_3` bar status mixes cohomological and chain-level claims

Attack:

- `FRONTIER.md:5` summarizes Wave 12 as leaving class-M `E_3` bar `6^g`
  beyond `g=3` as frontier.
- `notes/wave12_frontier_inventory.tex:327` says `g >= 4` is
  conjectural pending higher differentials.
- `FRONTIER.md:882-884` in an older memorial says Class M `E_3` bar
  `6^g` is PROVED.
- `metadata/claims.jsonl:1309-1310` records
  `prop:tricomplex-dimensions` and `prop:e3-spectral-degeneration` as
  `ProvedHere`.

Clarifying anchors:

- `chapters/theory/quantum_chiral_algebras.tex:2516-2580` proves finite
  tricomplex dimension and spectral sequence degeneration in the stated
  model.
- `chapters/theory/quantum_chiral_algebras.tex:2639` marks the
  MC-shadow identification conjectural because the explicit `E_3`-chiral
  tricomplex structure on `A` for CY_3 targets is open.
- Repo guidance says "Class M `E_3` bar = `6^g` at cohomology, NOT
  infinite"; the Wave 12 roster narrows the older frontier as `g <= 3`
  proved and `g >= 4` open pending `d_5`.

HEAL_4:

- Status recommendation: do not use one status for three claims.
  - Cohomological/tricomplex model dimension: `ProvedHere`, if the local
    degeneration proof is accepted.
  - Explicit non-formal CY_3 `E_3` chain-level realization: `Conjectured`
    or `Conditional`.
  - MC/shadow tower identification: `Conjectured`, as already stated at
    `quantum_chiral_algebras.tex:2639`.
- Proposed edits:
  - `FRONTIER.md:5` and `notes/wave12_frontier_inventory.tex:327` need a
    scope note if the all-`g` cohomological proof supersedes Wave 12:
    "cohomological model proved; chain-level CY_3/MC identification open".
  - `FRONTIER.md:882-884` should not simply say PROVED without that scope.

## ATTACK_5 -- Universal Borcherds theorem is healthy, but geometric scope can drift

Attack:

- Older and design material sometimes lets the universal
  `\kappa_{\mathrm{BKM}}` formula read as if it also proves the geometric
  CY-host realization and all BKM-side constructions.
- `FRONTIER.md:917` uses the stale label `prop:bkm-weight-universal`.
- `FRONTIER.md:968` has stale bare-`\kappa` language and says
  "`\kappa = \chi(\mathcal O_X)` FAILS at `d=3`", which is misleading
  against the current four-invariant taxonomy.

Supporting anchors:

- `chapters/examples/cy_d_kappa_stratification.tex` carries the correct
  theorem-level weight identities:
  - `metadata/claims.jsonl:220`: `thm:borcherds-weight-kappa-BKM-universal`
    is `ProvedHere` for the five CHL frame shapes.
  - `metadata/claims.jsonl:221`: eight-form CY-host catalogue is
    `ProvedHere` as an automorphic catalogue.
  - `metadata/claims.jsonl:222`: Borcherds-weight scope for all eight
    Nikulin orders is `ProvedElsewhere`.
- `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:136-145`
  confirms the additive split is false and the universal formula is
  `\kappa_{\mathrm{BKM}} = c_N(0)/2`.
- `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:393`
  separates the CHL ladder from the Gritsenko--Clery eight-form atlas.
- `notes/wave12_frontier_inventory.tex:209-239` keeps non-CHL/geometric
  CY_3 host realization as open or conjectural.

HEAL_5:

- Status recommendation: keep the Borcherds weight identity as theorem;
  keep geometric CY-host realization as separate conjectural/open
  material unless constructed.
- Proposed edits:
  - `FRONTIER.md:917`: update label to
    `thm:borcherds-weight-kappa-BKM-universal`.
  - `FRONTIER.md:968`: replace bare `\kappa` and `\chi(\mathcal O_X)`
    phrasing with the four-invariant taxonomy:
    `\kappa_{\mathrm{ch}}`, `\kappa_{\mathrm{cat}}`,
    `\kappa_{\mathrm{BKM}}`, `\kappa_{\mathrm{fiber}}`.
  - Any future registry entry should distinguish "automorphic/Borcherds
    theorem" from "geometric CY-host realization".

## ATTACK_6 -- Six routes and the K3 Yangian/BKM split are mostly fixed, but older FRONTIER text is stale

Attack:

- `FRONTIER.md:631` still says "Extend K3 Yangian to non-abelian sector
  using BKM real root generators", blending the Mukai/Yangian branch with
  the Hall--Drinfeld/BKM branch.
- `FRONTIER.md:680` has an older heading "The K3 Yangian `Y(g_K3)`".
- `FRONTIER.md:857` retains stale `Y(gl(4|20))` language.

Healthy anchors:

- `FRONTIER.md:98-110` explicitly says the BKM-side object is the K3
  chiral Hall--Drinfeld double and that plain BKM-side "K3 Yangian"
  language was retracted.
- `FRONTIER.md:153-159` keeps CY-C pentagon material on the
  Hall--Drinfeld double and says the Super-Yangian remains open.
- `FRONTIER.md:184-187` keeps F19 open as the split between the
  Hall--Drinfeld double and the historical K3 Yangian branch.
- `chapters/examples/cy_c_six_routes_convergence.tex:15-17` says six
  routes are six different constructions of still-conjectural
  `G(K3 x E)`, not six `\Phi` applications.
- `chapters/examples/cy_c_six_routes_convergence.tex:87-100` keeps the
  six-routes isomorphism and full non-abelian extension conjectural.
- `metadata/claims.jsonl:188` records
  `conj/thm:six-routes-isomorphism` as `Conjectured`.

HEAL_6:

- Status recommendation: no downgrade needed for the current six-routes
  body; the stale issue is archival `FRONTIER.md` language.
- Proposed edits:
  - `FRONTIER.md:631` and `FRONTIER.md:680`: rename or qualify K3
    Yangian language as the Mukai self-mirror branch; reserve BKM-side
    language for the Hall--Drinfeld double.
  - `FRONTIER.md:850-1008`: add a visible "historical memorial; not
    authoritative status spine" marker, or move these blocks into notes.
  - Keep `metadata/claims.jsonl:575` scope-restricted if it is the
    ADE/Kummer-locus MO Yangian statement, not a global BKM-side claim.

## ATTACK_7 -- CY-B/C/D status taxonomy needs dependency discipline

Attack:

- `metadata/claims.jsonl:187` records
  `thm:cy-c-pentagon-convergence-unconditional` with status
  `Conditional`; the label/title says "unconditional" while the status is
  not.
- `metadata/claims.jsonl:134` records
  `thm:cy-c-beyond-six-routes-as-stage-2-specialisations` as theorem env
  but `Conjectured`.
- `metadata/claims.jsonl:1107` records `thm:cy-b-d3` as `ProvedHere`;
  the current body label is at
  `chapters/theory/e2_chiral_algebras.tex:2015`. This cannot be stronger
  than the CY-A_3 framed-locus theorem if it depends on that construction.

Healthy anchors:

- `notes/vol3_rearchitecture_proposal.tex:666-682` gives the correct
  status table: CY-A `d=2` proved; CY-A `d=3` object-level on verified
  loci; morphisms conjectural; CY-B programme; CY-C conjectural; CY-D
  programme/theorem according to dimension-stratified claim.
- `chapters/examples/cy_c_six_routes_generator_level_platonic.tex:268-269`
  keeps six-routes generator-level convergence `Conditional`.
- `chapters/examples/cy_d_kappa_stratification.tex` has the correct
  dimension-stratified theorem and universal Borcherds statuses in the
  registry around `metadata/claims.jsonl:207`, `213`, `220`, and `221`.
- `chapters/theory/e2_chiral_algebras.tex:1351` says the compact CY_3
  case remains conjectural for the missing chain-level Koszul layer.

HEAL_7:

- Status recommendation:
  - CY-B at `d=3`: `Conditional` unless its proof is independent of
    CY-A_3 H1--H4 and all its own hypotheses are discharged.
  - CY-C: `Conjectured` for global convergence/existence; `Conditional`
    for generator/value-level comparisons under explicit loci.
  - CY-D: keep theorem-level status for `\kappa_{\mathrm{ch}}` Hodge
    supertrace and universal Borcherds weight identities, with the
    geometric-host caveat from HEAL_5.
- Proposed edits:
  - Rename `thm:cy-c-pentagon-convergence-unconditional` or downgrade the
    title so it does not fight its `Conditional` status.
  - Audit theorem environments with `Conjectured` status: either leave the
    theorem environment but make the title explicit ("Conjectural
    theorem") or convert to a conjecture environment for reader hygiene.

## ATTACK_8 -- Registry and FRONTIER archival hygiene hide live open problems

Attack:

- `metadata/theorem_registry.md` reports `Open | 0`.
- Body text contains at least one explicit open status:
  `chapters/theory/cy3_chain_level_bridge.tex:319` has
  `\ClaimStatusOpen{}`.
- `FRONTIER.md:65-77` preserves "nine retractions" as a status record.
- `FRONTIER.md:850-1008` preserves older session memorials whose labels
  and theorem statuses conflict with the current top-level spine.

HEAL_8:

- Status recommendation: choose one taxonomy and enforce it mechanically.
  - If `Open` is permitted, registry extraction must count
    `\ClaimStatusOpen{}`.
  - If `Open` is not permitted, replace it with
    `\ClaimStatusConjectured{Open problem: ...}` and regenerate metadata.
- Proposed edits:
  - `metadata/theorem_registry.md`: regenerate after status cleanup.
  - `FRONTIER.md:65-77` and `FRONTIER.md:850-1008`: move historical
    retractions/memorials to an archive note or label them visibly as
    non-authoritative historical record.
  - `metadata/claims.jsonl`: after body edits, rerun the extractor rather
    than hand-editing JSONL.

## Proposed edit queue

1. Downgrade or split `thm:qgf-G-X-representability` in
   `chapters/theory/quantum_groups_foundations.tex:540-610`.
2. Downgrade/scope the Super-Yangian block in
   `chapters/examples/k3_chiral_bialgebra_platonic.tex:5014-5468`.
3. Align CY-A_3 metadata and old `FRONTIER.md` language with
   `chapters/theory/cy_to_chiral.tex:793` and `4810-4899`.
4. Quarantine or archive stale `FRONTIER.md:850-1008` memorial sections.
5. Clarify class-M `E_3` bar scope: cohomological model versus chain-level
   CY_3/MC realization.
6. Clean theorem names whose title says "unconditional" while status says
   `Conditional`.
7. Regenerate `metadata/claims.jsonl` and `metadata/theorem_registry.md`
   after source-status edits.

## Tests and computations run

Commands run were inspection-only:

- `git status --short`
- `test -e notes/adversarial_architecture_swarm_20260424/agent_12_status_hygiene.md`
- `wc -l` on scoped files
- targeted `rg` over `FRONTIER.md`, `metadata/**`, `notes/**`, and
  `chapters/**.tex`
- targeted `sed -n` context reads on the anchors listed above

No build, pytest, LaTeX compilation, or mathematical computation was run.
This is appropriate for a report-only status-hygiene agent.

## Open questions for integration owner

1. Is the Super-Yangian block in
   `k3_chiral_bialgebra_platonic.tex:5014-5468` intended to supersede the
   current FRONTIER/Wave 12 spine, or should it be downgraded to candidate
   finite-depth evidence?
2. Should `thm:qgf-G-X-representability` be removed entirely, or retained
   as a conditional representability criterion?
3. Has the class-M `E_3` bar `6^g` result been accepted for all `g` at
   the cohomological model level after Wave 12, or does the `g >= 4`
   `d_5` obstruction remain live?
4. Should `\ClaimStatusOpen{}` be a first-class registry status, or should
   all open problems be normalized to `\ClaimStatusConjectured{Open
   problem: ...}`?
5. Should old `FRONTIER.md` memorial sections be moved to notes so
   `FRONTIER.md` becomes an authoritative current frontier document again?
