# Agent 14 Final Hostile Synthesis

Date: 2026-04-24

Scope: final hostile synthesis over Batch 1 and Batch 2 reports
`agent_01_*.md` through `agent_12_*.md`, plus the edited architecture
notes and live body anchors. This is report-only. No source edits,
commits, pushes, builds, or destructive git operations were run.

Verdict: the repaired core survives, but only after separating value
theorems from construction theorems. The integration has repaired the
main `cy_to_chiral.tex` spine more successfully than the surrounding
architecture notes, gluing notes, compute oracles, and metadata. The
largest remaining risk is status inflation: several files still state
global `G(X)`, compact `K3 \times E` Hall--Drinfeld doubles, super-Yangian
Hopf presentations, or all-loop hCS/holography as `ProvedHere` while the
current spine only supports conditional or conjectural status.

## Source Surface Read

Batch reports read:
`notes/adversarial_architecture_swarm_20260424/agent_01_*.md` through
`agent_12_*.md`.

High-load live anchors checked:

- `chapters/theory/cy_to_chiral.tex`
- `chapters/theory/gluing/sec_8_k3xe_master.tex`
- `chapters/theory/gluing/sec_10_unifying.tex`
- `chapters/theory/quantum_groups_foundations.tex`
- `chapters/examples/cy_d_kappa_stratification.tex`
- `chapters/examples/k3_yangian_chapter.tex`
- `chapters/examples/k3_chiral_bialgebra_platonic.tex`
- `chapters/connections/cy_holographic_datum_master.tex`
- `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md`
- `notes/vol3_rearchitecture_proposal.tex`
- `notes/platonic_synthesis_post_adversarial.tex`
- `compute/lib/diagonal_siegel_cy_orbifolds.py`
- `compute/lib/local_p2_four_kappa_engine.py`
- `compute/lib/macmahon_shadow_decomposition.py`
- `metadata/theorem_registry.md`
- `metadata/claims.jsonl`

## ATTACK_1: `\Phi_d` Is Still Overproved In The Integration Notes

The main chapter has largely repaired the theorem boundary, but the
architecture notes still overstate the repaired core.

Conflict anchors:

- `chapters/theory/cy_to_chiral.tex:22`--`32`: Stage 1 is pinned only
  after fixing an `E_d` formality/associator datum; before that, the
  `d=3` ambiguity is a GRT torsor.
- `chapters/theory/cy_to_chiral.tex:100`--`105`: `d=3` object-level
  loci are split from morphism-level functoriality.
- `chapters/theory/cy_to_chiral.tex:4846`--`4858`: the CY-A3 theorem is
  `Conditional` under H1--H4 and explicitly does not construct global
  `G(X)` or full morphism-level functoriality.
- `notes/vol3_rearchitecture_proposal.tex:813`--`818`: still says the
  CY-A3 theorem and `d=3` object-level theorem change from programme to
  proved.
- `notes/platonic_synthesis_post_adversarial.tex:77`--`165`: labels
  two-stage factorisation as `ClaimStatusTheorem` while mixing a
  contractible enhancement claim with the later GRT/open-integral
  caveat.
- `chapters/theory/gluing/sec_10_unifying.tex:660`--`671`: repeats
  Stage 1 canonical up to contractible choice without the torsor caveat.

Failure mode: the integration converts "object-level conditional
construction after choices" into "proved functorial theorem." That is
not a harmless wording difference; it changes the theorem class.

## HEAL_1: Exact `\Phi_d` Status Boundary

The surviving statement is:

```tex
\Phi_d^{(\Sigma_{d-1},C)}
  =
\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C}\circ \Phi_d^{\mathrm{FA}}.
```

Status levels:

- `ProvedHere` / cited-operadic theorem: the two-stage architecture as
  a formal factorisation schema once the required formality/framing
  data are fixed.
- `Conditional`: `d=3` object-level construction on the explicit
  H1--H4 framed CY-A3 loci in `cy_to_chiral.tex:4846`--`4858`.
- `Conjectured`: morphism-level functoriality of
  `\Phi_3^{(\Sigma_2,C)}` over general CY3 categories.
- `Conjectured`: global `G(X)` construction for compact CY3s.
- `Open`: fully explicit non-formal chain-level CY3 comparison beyond
  the verified framed loci.

Any global "CY-A3 is proved" title must be replaced by "CY-A3
object-level framed theorem, conditional on H1--H4." Any "contractible"
language must be scoped to "after the associator/formality datum is
fixed"; before that, the ambiguity is torsorial.

## ATTACK_2: `K3 \times E`, `H_{\Delta_5}`, And `G(X)` Are Still Being Built By Assertion

The live main spine says the compact `K3 \times E` double is conjectural,
but surrounding files state it as constructed.

Conflict anchors:

- `chapters/theory/cy_to_chiral.tex:8761`--`8785`: `G(X)` is defined
  only as a candidate when positive half, pairing, and completion are
  constructed.
- `chapters/theory/cy_to_chiral.tex:9382`--`9400`: `G(K3 \times E)` as
  Hall--Borcherds double is explicitly a conjecture.
- `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:233`--`235`:
  asserts a canonical equality
  `H_{\Delta_5}=D_\hbar(Y^{Hall}_\hbar(CoHA_{K3\times E}),...)`.
- `chapters/theory/gluing/sec_8_k3xe_master.tex:560`--`575`: labels
  assembly of 24 elliptic positive halves as `ClaimStatusProvedHere`.
- `chapters/theory/gluing/sec_8_k3xe_master.tex:696`--`728`: labels the
  `\Delta_5` associator on the Hall--Drinfeld double as
  `ClaimStatusProvedHere`.
- `chapters/theory/gluing/sec_8_k3xe_master.tex:750`--`772`: immediately
  after those proved labels, the text says the assembly of
  `D_\hbar(K3\times E)` and its CY-C compatibility are conjectural.
- `chapters/theory/quantum_groups_foundations.tex:555`--`599`: states
  global representability of `G(X)` for compact smooth CY3s, including
  quintic and `K3\times E`, as `ClaimStatusProvedHere`.
- `chapters/theory/quantum_groups_foundations.tex:4286`--`4429`: states
  strict motivic DT/CoHA/`\Phi_3(K3\times E)`/`\mathfrak g_{\Delta_5}`
  identifications, while `4431`--`4447` admits the compact motivic lift
  is conjectural.

Failure mode: the manuscript proves value fingerprints and then imports
the algebra object that would explain them. The value theorem does not
construct the Hall--Drinfeld double.

## HEAL_2: Compact `K3 \times E` Boundary

The surviving status split is:

- `ProvedHere` / cited theorem: Borcherds-product value statements such
  as `\kappa_{\mathrm{BKM}}(\Delta_5)=5` and
  `\Phi_{10}=\Delta_5^2` as genus-2 product identities.
- `Computed` / `Verified`: finite character, sign, and coefficient
  checks when backed by scripts or local tables.
- `Conditional`: any `\Phi_3^{(K3,E)}(K3\times E)=H_{\Delta_5}` statement
  only after the framed/banded specialisation, positive-half
  construction, pairing, completion, and bracket comparison are named.
- `Conjectured`: global `G(K3\times E)` as a Hall--Drinfeld/Borcherds
  double.
- `Conjectured`: compatibility of the compact `K3\times E` Hall object
  with CY-C descent and hCS/factorization constructions.

The correct compact mantra is: values first; object later. The `\Delta_5`
weight is theorem-grade. The compact Hall--Drinfeld double is not yet
theorem-grade.

## ATTACK_3: `\kappa` Normalisations Are Still Cross-Wired

The repaired reports agree that bare or mixed `\kappa` is the recurrent
source of false conclusions. The current tree still contains direct
contradictions.

Conflict anchors:

- `chapters/examples/cy_d_kappa_stratification.tex:1400`--`1414`:
  displays
  `{\kappa_cat,\kappa_ch,\kappa_BKM,\kappa_fibre}(K3\times E)={0,3,5,24}`
  and says the additive identity holds at `N=1`.
- `chapters/examples/cy_d_kappa_stratification.tex:2013`--`2041`: the
  same file correctly states
  `\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2` and that the additive formula
  fails at every `N in {1,2,3,4,6}`, including `N=1`.
- `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:147`--`151`:
  says the cross-volume bridge has conductor values `{10,4,2,2,2}`
  while the preceding line scopes to the K3-fibered CHL/class-A ladder,
  which should be `{10,8,6,4,2}` if it means the programme ladder.
- `chapters/examples/cy_d_kappa_stratification.tex:2130`--`2148`: the
  eight-form table still mixes rows and cover groups.
- `compute/lib/diagonal_siegel_cy_orbifolds.py:80`--`93`: the eight-order
  table gives `{5,4,3,2,2,1,1,1}`, neither the CHL five-row ladder nor
  the Clery--Gritsenko eight-form atlas.
- `compute/lib/diagonal_siegel_cy_orbifolds.py:600`--`650`: unsuperscripted
  `kappa_ch` assigns `3` to `K3\times E`, colliding with the compact
  Hodge/PhiFA value `0`.
- `chapters/examples/cy_d_kappa_stratification.tex:1774`--`1813`: assigns
  local `\mathbb P^2` and conifold `\kappa_{\mathrm{BKM}}` values.
- `compute/lib/local_p2_four_kappa_engine.py:260`--`317`: says
  `\kappa_{\mathrm{BKM}}` is undefined for local `\mathbb P^2`.

Failure mode: one symbol is being used for raw Hodge supertrace,
Heisenberg-Cartan rank, Borcherds weight, conductor, and noncompact
vertex/DT exponents.

## HEAL_3: Exact Invariant Ledger

The surviving invariant ledger is:

- Compact raw Hodge/PhiFA:
  `\kappa_{\mathrm{ch}}^{\mathrm{Hodge}}(K3\times E)=0`.
- Categorical:
  `\kappa_{\mathrm{cat}}(K3\times E)=\chi(\mathcal O_{K3\times E})=0`.
- Stage-2 Heisenberg-Cartan specialisation:
  `\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3\times E)=3`.
- Fibre witness:
  `\kappa_{\mathrm{cat}}(K3)=2` and fibre-count lane `24`.
- Borcherds:
  `\kappa_{\mathrm{BKM}}(\Delta_5)=5`.
- Universal BKM formula:
  `\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2`.
- Naive additive split:
  `\kappa_{\mathrm{BKM}}\ne
  \kappa_{\mathrm{ch}}+\chi(\mathcal O_{\mathrm{fiber}})` for every
  `N in {1,2,3,4,6}`; at `N=1`, `5 != 0+0`.

Normalisation table:

- Programme / CHL denominator ladder:
  `c_N(0)=(10,8,6,4,2)`, so
  `\kappa_{\mathrm{BKM}}=(5,4,3,2,1)`.
- Twined / singly-twined ladder:
  `c_N(0)=(10,4,2,2,2)`, so
  `\kappa_{\mathrm{BKM}}=(5,2,1,1,1)`.
- Clery--Gritsenko eight-form atlas:
  `\kappa_{\mathrm{BKM}}=(5,2,1,1,1/2,1,1/4,0)`, with the cover group
  recorded row-by-row.

Noncompact toric examples must not use `\kappa_{\mathrm{BKM}}` unless a
genuine genus-2 Borcherds denominator is constructed. Use
`\kappa_{\mathrm{vertex}}`, `\kappa_{\mathrm{DT}}`, or another explicit
local invariant instead.

## ATTACK_4: CoHA, `Y^+`, `W_{1+\infty}`, And hCS Are Still Collapsing In Compute/Body Edges

The main chapter has the right distinction; some compute and body files
still use the old collapse.

Conflict anchors:

- `chapters/theory/cy_to_chiral.tex:8788`--`8841`: correct current
  statement: `G(\mathbb C^3)` is the full affine Yangian obtained from
  the Drinfeld double of the positive half; the `\mathcal W` algebra
  appears through Fock/evaluation, not as the CoHA itself.
- `compute/lib/macmahon_shadow_decomposition.py:10`--`13`: still says if
  the `d=3` functor exists then `A_{\mathbb C^3}=\mathcal W_{1+\infty}`.
- `chapters/theory/quantum_groups_foundations.tex:4330`--`4363`: states
  strict compact `CoHA(K3\times E) \simeq U(Y^+(\mathfrak g_{\Delta_5}))`.
- `chapters/theory/cy3_chain_level_bridge.tex:324`--`330`: the
  hCS-to-Hall comparison is explicitly `ClaimStatusOpen`.

Failure mode: `CoHA=Y^+` is correct for `\mathbb C^3`; `CoHA=W` is not.
The compact `K3\times E` Hall-positive half has not been constructed at
the theorem level.

## HEAL_4: Algebra Object Boundary

The surviving algebra chain is:

- `ProvedHere` / standard toric computation:
  `\mathrm{CoHA}(\mathbb C^3)=Y^+`, the positive half.
- `ProvedHere` / conditional on standard pairing/completion:
  `G(\mathbb C^3)=D(Y^+)`, the full affine Yangian.
- `External/Conditional`:
  `\mathcal W_{1+\infty}` arises via Fock/evaluation/representation
  functors from the double; it is not the raw CoHA.
- `Open/Conjectured`:
  hCS-to-Hall comparison for compact CY3s.
- `Conjectured`:
  compact `K3\times E` Hall-positive half and its BKM bracket
  identification.

The compute docstrings and tests must enforce this exact chain:
`CoHA(C^3)=Y^+ -> double -> representation/W`, never
`CoHA(C^3)=W`.

## ATTACK_5: Descent And Gluing Still Transport Too Much

Some repaired locations correctly demote descent; the `K3\times E`
gluing chapter still proves the object it later calls expected.

Conflict anchors:

- `chapters/theory/cy_to_chiral.tex:4347`--`4382`: bar-hocolim is now
  `Conditional`, restricted to finite cofibrant Koszul diagrams, and
  explicitly does not transport centres or doubles.
- `chapters/theory/gluing/sec_10_unifying.tex:935`--`956`: Cech--Ran
  descent is correctly `Conjectured`.
- `chapters/theory/gluing/sec_8_k3xe_master.tex:560`--`575`: 24 elliptic
  positive-half assembly is `ClaimStatusProvedHere`.
- `chapters/theory/gluing/sec_8_k3xe_master.tex:696`--`728`: the
  `\Delta_5` associator on the double is `ClaimStatusProvedHere`.
- `chapters/theory/gluing/sec_8_k3xe_master.tex:750`--`772`: later says
  full double assembly and CY-C compatibility are conjectural.

Failure mode: a hocolim statement about bar/Koszul shadows is being used
as if it transported Drinfeld centres, Hall pairings, doubles, and BKM
brackets.

## HEAL_5: Descent Boundary

The surviving descent spine is:

- `Conditional`: finite cofibrant Koszul bar-hocolim comparison at the
  bar-shadow level.
- `Conjectured`: compact Cech--Ran descent for `\Phi_3` on global CY3s.
- `Conjectured`: descent of positive halves, pairings, completions,
  doubles, and centres.
- `Conditional`: `K3\times E` 24-fibre assembly only as an atlas-level
  witness after overlap cocycles, Mukai-lattice compatibility, and
  Hall pairing descent are supplied.
- `Open`: proof that the descended compact object agrees with the
  Borcherds `\Delta_5` double.

Bar-hocolim can support the shadow. It cannot by itself manufacture the
compact double.

## ATTACK_6: The K3 Yangian / Super-Yangian Repair Is Half-Integrated

The K3 Yangian chapter now has the right caution, but the bialgebra
chapter still announces the conjectural object as realized.

Conflict anchors:

- `chapters/examples/k3_yangian_chapter.tex:2233`--`2248`: correctly
  states that the super-Yangian is only a candidate presentation and
  that the Hall--Drinfeld comparison remains conjectural.
- `chapters/examples/k3_yangian_chapter.tex:2250`--`2264`: labels BKM
  simple roots as Yangian generators as a conjecture.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5008`--`5015`:
  says the presentation realizes `Y_\hbar^{super}(\mathfrak g_{\Delta_5})`
  and discharges the conjectural status.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5049`--`5052`:
  labels the Serre--BKM relations for the super-Yangian
  `ClaimStatusProvedHere`.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:7034`--`7035`:
  says the full bialgebra/M-theory synthesis remains conjectural.

Failure mode: finite-depth presentation checks are being promoted to a
full Hopf-superalgebra and Hall--Drinfeld identification.

## HEAL_6: Super-Yangian Boundary

The surviving K3/BKM/Yangian status is:

- `ProvedHere` or `Computed`: finite relation checks, BKM Serre-pattern
  witnesses, and low-depth PBW/character consistency where scripts or
  explicit algebra support them.
- `Conjectured`: existence of the full
  `Y_\hbar^{super}(\mathfrak g_{\Delta_5})` as a Hopf super-Yangian with
  coproduct, R-matrix, and correct completions.
- `Conjectured`: identification of that object with the compact
  `K3\times E` Hall--Drinfeld double.
- `Historical shorthand only`: "K3 Yangian" for the Mukai self-mirror
  branch. The BKM-side object is the Hall--Drinfeld double, not a
  Drinfeld Yangian.

The bialgebra chapter should be split into a proved finite
presentation-check theorem and a separate conjectural full
super-Yangian theorem.

## ATTACK_7: hCS, Factorization, And Holography Still Promote Evidence To Proof

The holographic master file has several good repairs, but architecture
and foundations files still overstate all-loop and boundary claims.

Conflict anchors:

- `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:332`--`336`:
  promotes an all-orders `1/\Phi_{10}` statement from a two-loop result
  using unproved BV-exponentiation/Gilkey vanishing.
- `chapters/theory/quantum_groups_foundations.tex:5672`--`5755`: labels
  the CLP bulk-boundary to `H_{\Delta_5}` as `ClaimStatusProvedHere`,
  with an "on the nose at chain level" conclusion.
- `chapters/theory/quantum_groups_foundations.tex:5937`--`5967`: the
  fingerprint corollary inherits that over-statused boundary theorem.
- `notes/platonic_synthesis_post_adversarial.tex:1135`--`1183`: labels
  near-horizon throat and dyon count as theorem and uses
  `1/\Phi_{k_N}^2` without a square-root convention.
- `chapters/connections/cy_holographic_datum_master.tex:948`--`977`:
  correctly splits Face 7 into proved Gaudin commutativity plus
  conditional `W` and DT/PT Bethe parts.

Failure mode: physics witnesses, perturbative hCS computations, and
Borcherds denominator theorems are being merged into one theorem.

## HEAL_7: hCS/Holography Boundary

The surviving hCS/holography status is:

- `ProvedHere` / `Computed`: local/flat hCS tests and finite graph-weight
  computations actually covered by the scripts.
- `External theorem`: Borcherds denominator identities and genus-2
  product weights.
- `Heuristic` / `Physics evidence`: AdS3 throat, black-hole, and
  one-loop hCS interpretations unless a formal comparison theorem is
  supplied.
- `Conditional`: CLP bulk-boundary to `H_{\Delta_5}` after the boundary
  functor, compact hCS-to-Hall map, and Hall double are constructed.
- `Conjectured`: all-loop compact `K3\times E` hCS exponentiation to the
  Igusa/Borcherds product.

The dyon denominator should be `1/\Phi_{k_N}` by default. Use
`1/\Phi_{k_N}^2` only if the text explicitly chooses a square-root or
left/right-moving convention and tracks it through the formula.

## ATTACK_8: Status Hygiene And Metadata Are Now A Mathematical Risk

The repaired source and the machine metadata no longer agree.

Conflict anchors:

- `metadata/theorem_registry.md`: generated 2026-04-23, reports
  `Open: 0`.
- `chapters/theory/cy3_chain_level_bridge.tex:324`--`330`: contains a
  live `ClaimStatusOpen` hCS-to-Hall comparison.
- `metadata/claims.jsonl`: still records stale `ProvedHere` rows for
  `thm:cy-to-chiral-d3`, `thm:qgf-G-X-representability`, and
  `thm:kcb-super-yangian-serre-BKM`.
- `chapters/theory/cy_to_chiral.tex:341` and
  `chapters/examples/cy_c_six_routes_convergence.tex:393`: use the
  composite status `ClaimStatusProvedHereConditional`.
- `FRONTIER.md`: the top caveat says historical sections are preserved,
  but stale lines still advertise resolved or historical claims in a way
  that can be grep-promoted back into theorem text.

Failure mode: status labels are being treated as evidence. Here they are
stale artifacts.

## HEAL_8: Status Protocol

The surviving status protocol is:

- Source TeX beats metadata until the registry is regenerated.
- Composite status labels must be normalized or the extractor must be
  taught to count them correctly.
- `ClaimStatusOpen` must appear in the theorem registry if open claims
  exist.
- Architecture notes and FRONTIER historical sections must be explicitly
  quarantined as historical when they preserve superseded claims.
- Any claim touching `G(X)`, compact Hall doubles, CY-C, Super-Yangian,
  hCS-to-Hall, or all-loop holography defaults to `Conjectured` or
  `Conditional` unless the proof body names the construction and its
  comparison map.

## Final Surviving Core

No more than twelve items:

1. The two-stage formula survives:
   `\Phi_d^{(\Sigma_{d-1},C)}=
   \mathrm{Sp}^{ch}_{\Sigma_{d-1},C}\circ \Phi_d^{FA}`.
2. Stage 1 is an `E_d` holomorphic/factorization assignment after the
   required formality/framing datum is fixed; at `d=3`, the pre-choice
   ambiguity is torsorial.
3. For `d=3`, only object-level framed H1--H4 loci are theorem-grade;
   morphism-level `\Phi_3` and global `G(X)` remain conjectural.
4. Stage 2 has native output levels: `d=1` chiral/commutative,
   `d=2` `E_2`-chiral, `d>=3` `E_1`-chiral; at `d>=3`, `E_2` lives on
   centres/representations, not on `A` itself.
5. `CoHA(\mathbb C^3)=Y^+`; the full Yangian is obtained by Drinfeld
   double, and `\mathcal W_{1+\infty}` appears through representation
   or evaluation, not as the raw CoHA.
6. `G(\mathbb C^3)` is the controlled model; compact `G(K3\times E)` and
   general compact `G(X)` are candidate/conjectural until positive
   halves, pairings, completions, and descent are constructed.
7. The `K3\times E` invariant ledger is:
   `\kappa_cat=0`, `\kappa_ch^{Hodge/PhiFA}=0`,
   `\kappa_ch^{Heis}=3`, `\kappa_BKM(\Delta_5)=5`, fibre lane `24`,
   and K3 fibre witness `2`.
8. The universal BKM formula is
   `\kappa_BKM(\Phi_N)=c_N(0)/2`; the additive formula with
   `\kappa_ch+\chi(\mathcal O_fiber)` is false at every
   `N in {1,2,3,4,6}`.
9. Six routes to `G(K3\times E)` are six distinct construction machines,
   not six applications of `\Phi`; their convergence is conjectural.
10. The BKM-side `K3\times E` object is the Hall--Drinfeld/Borcherds
    double; "K3 Yangian" is historical shorthand for the separate
    Mukai self-mirror branch.
11. hCS/factorization and holography currently provide local
    computations, physics evidence, and conditional comparison
    frameworks, not an all-loop compact theorem.
12. Metadata and frontier summaries are non-authoritative until
    regenerated after the status repairs.

## High-Priority Edits Still Needed

1. Replace the global "CY-A3 proved" language in
   `notes/vol3_rearchitecture_proposal.tex:813`--`818` with the
   H1--H4 object-level conditional theorem.
2. Repair all "contractible Stage 1" claims in architecture/gluing notes
   by adding the fixed-datum/GRT torsor distinction.
3. Fix `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:147`
   --`151`: separate programme/CHL and twined conductor ladders.
4. Downgrade or condition the canonical
   `H_{\Delta_5}=D_\hbar(...)` climax in
   `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:233`
   --`235`.
5. Repair `chapters/examples/cy_d_kappa_stratification.tex:1400`--`1414`
   and `2130`--`2148`: split raw Hodge, Heisenberg, fibre, BKM, CHL,
   twined, and Clery--Gritsenko rows.
6. Rename or re-scope noncompact local `\kappa_{\mathrm{BKM}}` entries
   in `cy_d_kappa_stratification.tex:1774`--`1813` to match
   `compute/lib/local_p2_four_kappa_engine.py:260`--`317`.
7. Downgrade `thm:qgf-G-X-representability` and the motivic
   `K3\times E` CoHA/`\Phi_3` theorem in
   `chapters/theory/quantum_groups_foundations.tex`.
8. Downgrade the CLP bulk-boundary and fingerprint consequences in
   `chapters/theory/quantum_groups_foundations.tex:5672`--`5967`.
9. Downgrade `chapters/theory/gluing/sec_8_k3xe_master.tex:560`--`575`
   and `696`--`728` to conditional/conjectural statements.
10. Split `chapters/examples/k3_chiral_bialgebra_platonic.tex` into
    proved finite relation checks and conjectural full super-Yangian
    structure.
11. Fix stale compute oracles/docstrings in
    `compute/lib/diagonal_siegel_cy_orbifolds.py` and
    `compute/lib/macmahon_shadow_decomposition.py`; add a regression test
    preventing `CoHA(C^3)=W_{1+\infty}`.
12. Normalize composite statuses, regenerate `metadata/theorem_registry.md`
    and `metadata/claims.jsonl`, and quarantine stale `FRONTIER.md`
    historical claims so they cannot be mistaken for current theorem
    statements.

## Final Classification

GREEN core: the two-stage architecture, object-level d=3 framed locus,
`CoHA(\mathbb C^3)=Y^+`, BKM weight formula, and distinct-route
discipline survive.

YELLOW core: CY-C convergence, compact descent, `K3\times E` Hall double,
hCS-to-Hall, CLP boundary, and holographic comparison survive only as
conditional/conjectural programmes.

RED residue: any file still saying global `G(X)`, compact
`H_{\Delta_5}` Hall--Drinfeld construction, full super-Yangian, all-loop
hCS, or `CY-A3 proved` without hypotheses is out of sync with the
surviving architecture.
