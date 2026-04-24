# Agent 15 -- Proof-Obligation and Metadata Convergence

Date: 2026-04-24.
Scope: theorem/status metadata, proof obligations, and executable evidence after
the available adversarial architecture reports.

Report-only. No commits. No destructive git. No manuscript or compute source
edits. Final files changed by this agent: this report only.

Only `agent_01` through `agent_12` existed in
`notes/adversarial_architecture_swarm_20260424/` during inspection. No
`agent_13` or `agent_14` report was present.

## Executive verdict

The metadata layer is not convergence-grade. The live TeX source has moved
past the checked-in `metadata/claims.jsonl` and `metadata/theorem_registry.md`;
the registry still records stale statuses for CY-A3 and the `E_1` sector, does
not index `ClaimStatusProvedHereConditional` or the live `openproblem` surface,
and still reports `Open = 0`.

The main body is also not fully status-honest. The strongest remaining
overclaims are:

1. global `G(X)` representability as `ProvedHere`;
2. the K3/BKM "super-Yangian" suite as `ProvedHere`;
3. compute oracles that still certify `kappa_ch(K3 x E) = 3` and the
   `5 = 3 + 2` decomposition under the unqualified name `kappa_ch`, while the
   manuscript now distinguishes compact `kappa_ch(K3 x E)=0` from the
   Heisenberg specialisation `kappa_ch^{Heis}=3`.

The targeted pytest surface is mechanically healthy: all focused slices run
below passed. That is evidence for arithmetic/local identities, not for the
global theorem upgrades attacked here.

## ATTACK_1 -- CY-A3 and E1-sector statuses are stale in metadata

Attack. The current source marks CY-A3 as conditional:

- `chapters/theory/cy_to_chiral.tex:4856-4858`:
  `thm:cy-to-chiral-d3` has `ClaimStatusConditional`.
- `chapters/theory/cy_to_chiral.tex:4860-4918`: H1--H4 and the fixed
  specialisation datum are load-bearing. The theorem explicitly excludes
  arbitrary CY3 morphisms and global `G(C)`.
- `chapters/theory/cy_to_chiral.tex:4927-4936`: convergence is only
  coefficient-level in finite-Leray-cover cases and OPE-level only in named
  Borel-summable regimes.

But checked-in metadata says:

- `metadata/claims.jsonl:966`: `thm:cy-to-chiral-d3` is `ProvedHere` and has
  stale source line `4318`.

The same drift appears for the native `E_1` sector:

- `chapters/theory/e1_chiral_algebras.tex:175-178`:
  `thm:e1-sector-d3` has `ClaimStatusConditional`.
- `metadata/claims.jsonl:1053`: same label is `ProvedElsewhere`.
- `chapters/theory/e1_chiral_algebras.tex:244` still says
  `(CY-A_3, proved)`, which is stronger than the theorem at `:177`.

Heal. Do not hand-edit `claims.jsonl`. After source cleanup, regenerate it.
Expected generated statuses:

- `thm:cy-to-chiral-d3`: `Conditional`.
- `thm:e1-sector-d3`: `Conditional`.
- `chapters/theory/e1_chiral_algebras.tex:244`: replace "proved" by
  "conditional on the framed CY-A3 H1--H4 locus".

Targeted verification command after edit:

```bash
python3 - <<'PY'
# read-only label/status comparison for thm:cy-to-chiral-d3 and thm:e1-sector-d3
PY
```

## ATTACK_2 -- The metadata extractor cannot represent the live status taxonomy

Attack. The generator only recognizes a narrow status regex:

- `scripts/generate_metadata.py:33-36`: `CLAIM_ENVS` omits `openproblem`.
- `scripts/generate_metadata.py:38-42`: `openproblem` is only
  theorem-like, not claim-scanned.
- `scripts/generate_metadata.py:44-45`: `STATUS_RE` does not include
  `ProvedHereConditional`, `Computed`, `Theorem`, `Definition`,
  `Definitional`, or the other live status macros.

Live scan found:

- `chapters/theory/cy_to_chiral.tex:341`: `ClaimStatusProvedHereConditional`.
- `chapters/examples/cy_c_six_routes_convergence.tex:393`:
  `ClaimStatusProvedHereConditional`.
- `chapters/theory/cy3_chain_level_bridge.tex:324-326`: live
  `openproblem` with `ClaimStatusOpen`.
- `main.tex:139-146`: both `ClaimStatusOpen` and
  `ClaimStatusProvedHereConditional` are first-class macros.
- `metadata/theorem_registry.md:1-23`: stale generated snapshot
  `2026-04-23`, `Total tagged claims 1388`, `Open 0`.

I accidentally invoked `python3 scripts/generate_metadata.py --help`; because
the script has no help mode, it rewrote metadata. I immediately restored the
five generated metadata files to their pre-run tracked contents. The transient
output is still useful evidence: the current generator would produce
`1582` claims, `ProvedHere 838`, `Conditional 100`, `Open 0`, still missing the
live open-problem surface and still unable to model composite statuses.

Heal. Choose one mechanical taxonomy:

- Preferred: normalize composite tags in TeX to canonical statuses with the
  hypothesis in the status text, e.g. `ClaimStatusConditional{...}` instead of
  `ClaimStatusProvedHereConditional`.
- Alternative: make composite statuses first-class in the generator, add a
  word boundary or negative lookahead so `ProvedHereConditional` cannot be
  parsed as `ProvedHere`, and scan `openproblem` environments.

Only after the body statuses are repaired, run:

```bash
python3 scripts/generate_metadata.py
git diff -- metadata/claims.jsonl metadata/theorem_registry.md
```

## ATTACK_3 -- Global `G(X)` representability is stronger than its proof body

Attack. The manuscript still asserts an abstract global quantum vertex chiral
group as a theorem:

- `chapters/theory/quantum_groups_foundations.tex:555-559`: introduces
  functorial existence of `G(X)` as a representability theorem, including
  compact/noncompact cases beyond constructed examples.
- `chapters/theory/quantum_groups_foundations.tex:583-599`:
  `thm:qgf-G-X-representability` is `ClaimStatusProvedHere`.
- `chapters/theory/quantum_groups_foundations.tex:601-608`: the proof applies
  Brown--Lurie style representability to a custom category
  `QChirGrp_k`.
- `chapters/theory/quantum_groups_foundations.tex:614-624`: the verification
  paths still depend on CoHA-site and MO stable-envelope hypotheses.
- `chapters/theory/quantum_groups_foundations.tex:632-639`: the remark says
  the theorem "produces `G(X)`" and converts construction into presentation.

This is stronger than the evidence. The proof does not establish the
presentability/accessibility of the bespoke `QChirGrp_k`, the limit
preservation of `F_X` with all CoHA/MO compatibility constraints, or the
concrete Hall--Drinfeld/vertex group for generic compact CY3 inputs.

Heal. Split the result.

- `ProvedElsewhere` or `Conditional`: abstract adjoint-functor theorem schema
  once `QChirGrp_k` is proved presentable and `F_X` is proved limit-preserving.
- `ProvedHere`: constructed examples only, e.g. `C^3` and explicitly verified
  toric/ADE-Kummer loci.
- `Conjectured`: global `G(X)` for arbitrary compact CY3 and the
  identification `G(X) = Phi(C)` in the quantum vertex chiral group sense.

Minimal patch plan:

1. Change `thm:qgf-G-X-representability` from `ClaimStatusProvedHere` to
   `ClaimStatusConditional`.
2. Retitle to "Conditional representability criterion for `G(X)`".
3. Add hypotheses: presentability of `QChirGrp_k`, accessibility of the
   CoHA-compatible functor, MO fixed-point/stable-envelope scope, and
   pro-completion convergence.
4. Add a separate `conjecture` for generic `G(X)`.

## ATTACK_4 -- The K3/BKM super-Yangian suite conflicts with the open osp frontier

Attack. One chapter correctly keeps the orthosymplectic super-Yangian open:

- `chapters/examples/k3_yangian_chapter.tex:2870-2876`:
  `conj:osp-yangian-mukai`, `ClaimStatusConjectured`.
- `FRONTIER.md:81-87`, `:159`, `:210`, `:792-809`: the
  `Y_{osp}(4|20)` reflection-equation construction remains open.

But another chapter has a suite of `ProvedHere` super-Yangian claims:

- `metadata/claims.jsonl:399-403`: five K3/BKM super-Yangian claims are
  indexed as `ProvedHere`.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5049-5055`:
  `thm:kcb-super-yangian-serre-BKM`, `ClaimStatusProvedHere`.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5179-5182`:
  `prop:kcb-super-yangian-PBW`, `ClaimStatusProvedHere`.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5225-5231`:
  `thm:kcb-super-yangian-coproduct`, `ClaimStatusProvedHere`.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5289-5295`:
  `prop:kcb-super-yangian-quasitriangular`, `ClaimStatusProvedHere`.

These claims are acceptable only as formal consequences inside a defined
topological current algebra with imposed Borcherds/Drinfeld relations. They do
not prove the open `Y_{osp}(4|20)` reflection-equation object, the rank
`(4,20)` osp R-matrix relations, the Berezinian/Delta_5 denominator
identification, or the BKM-to-Yangian lift.

Heal. Split or demote.

- If the section is retained as a formal algebra, retitle it
  "formal BKM-current envelope" and keep only tautological relation/PBW facts
  as `ProvedHere`.
- The actual `Y_{osp}(4|20)` identification must be `ClaimStatusConjectured`
  and cross-reference `conj:osp-yangian-mukai`.
- Coproduct and universal R-matrix should be `Conditional` unless the
  reflection-equation Hopf structure is proved in the chapter.

Targeted test command for future repair:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider \
  compute/tests/test_k3_yangian_adversarial.py \
  compute/tests/test_k3_yangian_borcherds_weight_theta_refinement.py \
  compute/tests/test_hyperkahler_BKM_lift.py \
  compute/tests/test_k3_yangian_unified_cross_check.py
```

This currently passes, but it verifies separation of BKM/Yangian evidence, not
the open osp reflection equation.

## ATTACK_5 -- Passing kappa tests still certify a stale K3 x E decomposition

Attack. The source now distinguishes compact supertrace from Heisenberg
specialisation:

- `chapters/examples/cy_d_kappa_stratification.tex:1400-1417`:
  `{kcat, kappa_ch^{Heis}, kBKM, kappa_fibre}(K3 x E) = {0,3,5,24}`;
  compact `kappa_ch(K3 x E)=0`; the additive identity
  `kBKM = kch + chi(O_fibre)` fails already at `N=1`.

But compute still has an unqualified older oracle:

- `compute/lib/kappa_spectrum_reconciliation.py:30-36`: advertises
  `kappa_BKM(K3 x E)=kappa_ch(K3 x E)+kappa_cat(K3)=3+2=5`.
- `compute/lib/kappa_spectrum_reconciliation.py:172-193`: returns
  `kappa_ch(K3xE)=3`.
- `compute/lib/kappa_spectrum_reconciliation.py:346-375`: returns
  `decomposition_holds=True`.
- `compute/tests/test_kappa_spectrum_reconciliation.py:193-198`:
  asserts `kappa_ch(K3 x E)=3`.
- `compute/tests/test_kappa_spectrum_reconciliation.py:310-322`:
  asserts the decomposition holds.
- `compute/tests/test_kappa_bkm_adversarial.py:117-144`: asserts the
  decomposition holds at `N=1`.

Direct command output:

```text
{'kappa_ch_K3xE': 3, 'kappa_BKM_K3xE': 5, 'kappa_cat_K3': 2,
 'kappa_cat_K3xE': 0, 'decomposition_holds': True, ...}
live_source_expected: compact_hodge_supertrace=0; additive identity fails at N=1
```

This is the highest-priority compute/prose mismatch. The tests pass because
they assert the stale oracle.

Heal. Rename the compute lane and make the negative oracle explicit.

1. In `kappa_spectrum_reconciliation.py`, rename the current `kappa_ch(K3xE)`
   value to `kappa_ch_Heis_K3xE` or equivalent.
2. Add a compact-CY oracle returning `kappa_ch_compact(K3xE)=0`.
3. Change `verify_BKM_decomposition_k3e()` to return
   `decomposition_holds=False` under the canonical compact theorem, with
   observed failures `5 != 0+0` and `5 != 0+2`.
4. Keep the `3+2=5` equality only as a named Heisenberg-specialisation
   coincidence, not a universal or canonical decomposition.
5. Update `test_kappa_spectrum_reconciliation.py` and
   `test_kappa_bkm_adversarial.py` accordingly.

Targeted test command after repair:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider \
  compute/tests/test_cy_d_kappa_stratification.py \
  compute/tests/test_kappa_spectrum_reconciliation.py \
  compute/tests/test_kappa_consistency_adversarial.py \
  compute/tests/test_kappa_bkm_adversarial.py \
  compute/tests/test_cy_euler.py
```

## ATTACK_6 -- ZTE exact matrix is computed on charge 2, not an all-sector theorem

Attack. The ZTE oracle is strong but scoped:

- `compute/lib/zte_t_matrix_exact.py:13-25`: exact rational construction and
  verification.
- `compute/lib/zte_t_matrix_exact.py:19-23`: projection to the charge-2
  sector, system shape `36 x 80`.
- `compute/lib/zte_t_matrix_exact.py:220-255`: obstruction is computed in
  full then extracted to charge 2.
- `compute/tests/test_zte_t_matrix_exact.py:155-190`: rank `35` and
  exact consistency for the charge-2 linearized system.
- `compute/tests/test_zte_t_matrix_exact.py:453-489`: structural checks at a
  second parameter set.

The command `python3 -m pytest -q compute/tests/test_zte_t_matrix_exact.py`
passed with `35 passed`. That proves the charge-2 exact rational correction
and parameter stability, not an all-charge/all-parameter ZTE theorem.

Heal. Keep the current computation, but make every metadata/prose citation say
"computed charge-2 exact rational ZTE correction" unless a full-sector smoke
residual or all-sector theorem is added. If the manuscript keeps
`ClaimStatusProvedHere` for `prop:zte-explicit-correction` and downstream ZTE
claims, the theorem statement must explicitly restrict to the charge-2
projection and `O(kappa^4)` residual scope.

## Commands and tests run

Inspection:

```bash
git status --short
sed -n '1,240p' AGENTS.md
sed -n '1,220p' CLAUDE.md
sed -n '1,220p' .agents/skills/vol3-beilinson-loop/SKILL.md
sed -n '1,240p' .agents/skills/vol3-build-surface/SKILL.md
sed -n '1,220p' .agents/skills/vol3-claim-verification/SKILL.md
find notes/adversarial_architecture_swarm_20260424 -maxdepth 1 -type f -name 'agent_*.md' -print | sort
rg / nl / sed targeted over metadata, FRONTIER, chapters, compute, and reports
```

Read-only status scans:

```bash
python3 - <<'PY'
# live ClaimStatus token scan over chapters/, appendices/, main.tex
PY

python3 - <<'PY'
# read-only comparison of selected metadata rows against live label windows
PY

PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=compute/lib python3 - <<'PY'
from kappa_spectrum_reconciliation import verify_BKM_decomposition_k3e
print(verify_BKM_decomposition_k3e())
PY
```

Accidental generator invocation and restoration:

```bash
python3 scripts/generate_metadata.py --help
git status --short metadata
for f in metadata/census.json metadata/claims.jsonl metadata/dependency_graph.dot metadata/label_index.json metadata/theorem_registry.md; do git show HEAD:$f > $f; done
git status --short metadata
```

The command rewrote generated metadata because no help mode exists; all
metadata files were restored immediately. Final metadata worktree status was
clean before writing this report.

Targeted pytest results:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider \
  compute/tests/test_cy_d_kappa_stratification.py \
  compute/tests/test_kappa_ch_d3_formula.py \
  compute/tests/test_local_p2_four_kappa_engine.py \
  compute/tests/test_kappa_bkm_adversarial.py \
  compute/tests/test_cy_euler.py
# 299 passed in 1.11s
```

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider \
  compute/tests/test_zte_t_matrix_exact.py
# 35 passed in 11.76s
```

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider \
  compute/tests/test_cy_c_six_routes.py
# 21 passed in 0.06s
```

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider \
  compute/tests/test_igusa_product_formula.py \
  compute/tests/test_phi01.py \
  compute/tests/test_phi01_cross.py
# 122 passed in 2.29s
```

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider \
  compute/tests/test_costello_5d_verification.py \
  compute/tests/test_holomorphic_cs_chiral_engine.py \
  compute/tests/test_costello_paquette_defect_chiral.py \
  compute/tests/test_k3_yangian_twisted_11dsugra_1loop.py
# 237 passed in 22.25s
```

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider \
  compute/tests/test_k3_yangian_adversarial.py \
  compute/tests/test_k3_yangian_borcherds_weight_theta_refinement.py \
  compute/tests/test_hyperkahler_BKM_lift.py \
  compute/tests/test_k3_yangian_unified_cross_check.py
# 240 passed in 4.35s
```

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider \
  compute/tests/test_e1_refined_macmahon_engine.py \
  compute/tests/test_macmahon_shadow_decomposition.py \
  compute/tests/test_coha_drinfeld_bulk.py \
  compute/tests/test_c3_envelope_comparison.py
# 259 passed in 4.10s
```

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider \
  compute/tests/test_bps_entropy_shadow.py \
  compute/tests/test_bps_microstate_shadow.py \
  compute/tests/test_genus2_chiral_partition.py \
  compute/tests/test_twisted_holography_k3e.py
# 271 passed in 3.49s
```

No pytest command failed. The failures above are semantic: stale metadata and
tests that encode stale theorem strength.

## Proof-obligation ledger

### ProvedHere

- `thm:kappa-hodge-supertrace-identification`
  (`metadata/claims.jsonl:207`, source
  `chapters/examples/cy_d_kappa_stratification.tex`): compact CY Hodge
  supertrace formula. For `K3 x E`, compact `kappa_ch=0`.
- `thm:borcherds-weight-kappa-BKM-universal`
  (`metadata/claims.jsonl:220`): five CHL frame-shape identity
  `kappa_BKM(Phi_N)=c_N(0)/2`; geometric-host/eight-form extensions retain
  their stated scope.
- `thm:k3-abelian-yangian-presentation`
  (`metadata/claims.jsonl:465`): abelian K3 Yangian generators/relations.
- Formal/local identities verified in compute: Phi01/Igusa coefficient
  checks, CoHA positive-half coefficient checks, hCS flat-model algebraic
  identities, K3/BKM separation guardrails.

### ProvedElsewhere

- Primary-source inputs: Borcherds/Gritsenko weights, MO stable envelopes on
  their published scope, Costello--Li/Costello--Gwilliam formal-local
  constructions, Schiffmann--Vasserot toric CoHA where cited.
- ZTE background: Yang R-matrix/ZTE definitions and the external algebraic
  setting are cited elsewhere; the exact charge-2 correction is local compute
  evidence.

### Conditional

- `thm:cy-to-chiral-d3`: conditional on H1--H4 and fixed
  `(Sigma_2,C)` specialisation; metadata must be regenerated.
- `thm:e1-sector-d3`: conditional on CY-A3 H1--H4; metadata must be
  regenerated and local prose at `e1_chiral_algebras.tex:244` narrowed.
- `thm:qgf-G-X-representability`: should become conditional unless the
  presentability/limit-preservation/pro-completion hypotheses are proved.
- hCS-to-Hall comparison and compact CY3 BV quantisation beyond named loci.
- K3/BKM formal super-current algebra claims, unless retitled as formal
  imposed-relation consequences.

### Conjectured

- Global `G(X)` for arbitrary compact CY3 and the identification
  `G(X)=Phi(C)`.
- CY-C in general.
- `Y_{osp}(4|20)` reflection-equation super-Yangian and BKM-to-Yangian lift.
- K3 x E algebra-level Hall--BKM equivalence beyond numerical/graded data.
- Global hCS-to-Hall map outside verified toric/formal loci.

### Computed

- ZTE exact rational correction: charge-2 projection, `36 x 80` system,
  rank `35`, exact solution, `35` tests. Scope must not be enlarged.
- Kappa/BKM test surface: many tests pass, but `kappa_spectrum_reconciliation`
  currently computes a Heisenberg-specialisation value under the unqualified
  `kappa_ch` name and must be renamed.
- Phi01/Delta5 coefficient tests: `122` focused tests passed; sign-sensitive
  high-precision script should still be promoted to pytest if CI coverage is
  desired.
- Local `P2`/conifold BKM guard: current compute correctly records local
  `P2` `kappa_BKM=None`; manuscript row now uses `kappa_vertex`, so this
  earlier mismatch is largely healed.

## Open obligations for the integration owner

1. Repair `kappa_spectrum_reconciliation.py` and its tests before using any
   kappa test count as theorem evidence.
2. Demote or split `thm:qgf-G-X-representability`.
3. Demote or retitle the K3/BKM super-Yangian suite in
   `k3_chiral_bialgebra_platonic.tex`.
4. Normalize `ClaimStatusProvedHereConditional` and `ClaimStatusOpen`, or make
   them first-class in `scripts/generate_metadata.py`.
5. Regenerate metadata once, after source-status repairs; inspect the diff
   before treating registry totals as evidence.
6. Quarantine stale archival `FRONTIER.md:840-980` language or prefix it with a
   machine-readable supersession warning. It still contains `Y(gl(4|20))`,
   bare `kappa` prose, and several "PROVED" claims already corrected in the
   live top spine.

