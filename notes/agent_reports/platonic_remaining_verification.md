# Platonic Remaining Verification

Date: 2026-04-24
Lane: Vol III swarm lane 6, independent verification after compact/Heisenberg and CoHA repairs.
Scope: read-only attack pass, except this report.

## Verdict

The main manuscript surface is close but not converged.

RED:
- `chapters/theory/cy_to_chiral.tex:4781` still says the full Yangian
  `Y(\widehat{\mathfrak{gl}}_1)=\mathcal{W}_{1+\infty}` is obtained
  by Drinfeld-centre passage. This is too strong relative to the
  repaired positive-half/Drinfeld-double discipline. The safe statement is
  an evaluation/action map from the full Yangian to endomorphisms of the
  `\mathcal{W}_{1+\infty}[\lambda]` vacuum module, not equality of the
  Yangian with the VOA.
- `compute/tests/test_kappa_bkm_universal.py:190`, `:198`, `:547` still
  expects the old decomposition-success surface: seven failures, one
  success, and key `decomposition_successes`. The repaired oracle in
  `compute/lib/kappa_bkm_universal.py:282`--`:285` and `:812`--`:819`
  now reports falsification on CHL `N in {1,2,3,4,6}`, with five failures
  and zero successes. The narrow pytest slice exposes this mismatch.

BLUE:
- Changed notes still carry old compact/Heisenberg conflations. These are
  not the primary reader-facing theorem surface, but they are easy to
  reimport accidentally. Anchors:
  `notes/wave12_b2_cross_volume_consistency.tex:55`,
  `notes/wave13_a10_DT_wallcrossing_soibelman.tex:956`,
  `notes/wave14_a6_DT_GW_MNOP_soibelman.tex:1062`,
  `notes/physics_topological_strings.tex:966`,
  `notes/wave13_b5_meta_platonic_ideal.tex:316`,
  `notes/wave12_master_session_synthesis.tex:292`,
  `notes/wave12_a10_wall_crossing_soibelman.tex:470`,
  `notes/wave12_f5_programme_meta_audit.tex:521`.
  Pattern: unqualified `\kappa_{\mathrm{ch}}(K3 x E)=3` or equivalent
  `\kch` language. Under current discipline, compact total-space
  `\kappa_{\mathrm{ch}}(K3 x E)=0`; `3` is the scoped Heisenberg branch.
- Some compute tests pass while preserving stale names for route-dependent
  ranks as `kappa_ch`. Anchors:
  `compute/tests/test_cy_c_six_routes.py:89`--`:130`, `:222`;
  `compute/tests/test_kappa_spectrum_reconciliation.py:418`, `:491`;
  `compute/tests/test_k3e_yangian_phi3_identification.py:503`, `:524`,
  `:574`. This is semantic drift in the test prose/oracle naming, not an
  immediate proof failure, because the same tests also distinguish compact
  `0` and Heisenberg `3`.
- `chapters/theory/hochschild_calculus.tex:2825`--`:2868` has a remark
  titled "Delta_5 as kinematic input, not dynamical output..." This is
  defensible only relative to the AdS/CFT boundary-data discussion. It
  should explicitly say this is not contradicting the Wave-13
  one-loop-forced output theorem. Safer wording: "automorphic boundary
  datum for the AdS/CFT comparison".
- `chapters/examples/k3e_bkm_chapter.tex:169`--`:207` distinguishes
  denominator datum from one-loop output, but the word "input" appears in
  a high-risk context. This is lower severity because the proposition is
  already careful; consider replacing "Denominator input" with
  "Denominator datum" or "Borcherds-lift seed".

GREEN:
- No surviving reader-facing claim found that `\mathrm{CoHA}(\mathbb{C}^3)`
  directly equals `\mathcal{W}_{1+\infty}`. The corrected positive-half
  chain appears at
  `chapters/theory/quantum_groups_foundations.tex:708`--`:724`,
  `chapters/examples/toric_cy3_coha.tex:172`--`:190`, and
  `chapters/theory/cy3_chain_level_bridge.tex:430`--`:438`.
- No surviving reader-facing "six Phi applications" claim found. The
  current surface states six distinct constructions/routes, especially in
  `chapters/examples/cy_c_six_routes_convergence.tex`.
- No confirmed reader-facing claim found that
  `\kappa_{\mathrm{cat}}(K3 x E)=2`. The main K3 x E total-space lines
  are corrected to `0`; the inspected `en_factorization` hit is about the
  K3 handle/Kummer route, not the total product.
- No confirmed reader-facing theorem found that proves CY-C or the
  Super-Yangian unconditionally. The searched theorem surfaces are
  conditional/conjectural. One follow-up check remains useful around
  introduction occurrences of "Theorem CY-C" to ensure use-site wording
  remains conditional.
- BKM-as-Yangian confusion appears guarded: the BKM object is generally
  described as Hall-Drinfeld/Borcherds, while the K3 Yangian branch is
  separate or conditional.

## Verification Commands

Read required local doctrine:

```bash
sed -n '1,260p' CLAUDE.md
sed -n '261,620p' CLAUDE.md
```

Dirty tree and changed surface:

```bash
git status --short
git diff --stat
git diff -U0 -- '*.tex' | rg -n --pcre2 '^\+[^+].*\\kappa(?!_)'
```

Targeted searches:

```bash
rg -n --pcre2 '\\k(?:appa_\{\\mathrm\{ch\}\}|ch)\s*\(?K3\s*(?:\\times|x|\\\*|\\\\times)\s*E\)?\s*=?\s*3|K3\\s*\\times\\s*E.*\\k(?:appa_\{\\mathrm\{ch\}\}|ch).*3|\\k(?:appa_\{\\mathrm\{ch\}\}|ch).*K3\\s*\\times\\s*E.*3' chapters notes compute tests --glob '*.tex' --glob '*.py'
rg -n --pcre2 'kappa_\{\\mathrm\{cat\}\}.*K3.*E.*2|K3.*E.*kappa_\{\\mathrm\{cat\}\}.*2|chi\\(\\mathcal\\{O\\}_\\{K3\\s*\\\\times\\s*E\\}\\).*2' chapters notes compute tests --glob '*.tex' --glob '*.py'
rg -n --pcre2 'kappa_\{\\mathrm\{BKM\}\}.*kappa_\{\\mathrm\{ch\}\}.*(?:fiber|fibre|chi)|kBKM.*kch.*(?:fiber|fibre|chi)' chapters notes compute tests --glob '*.tex' --glob '*.py'
rg -n --pcre2 'CoHA.*(?:C\\^3|\\mathbb\\{C\\}\\^3).*W_\{?1\\+\\infty\\}?|CoHA.*(?:C\\^3|\\mathbb\\{C\\}\\^3).*full Yangian|Y\^\\+.*not.*W|full Yangian.*W_\{?1\\+\\infty\\}?' chapters notes compute tests --glob '*.tex' --glob '*.py'
rg -n --pcre2 'six\\s+(?:applications|Phi applications|\\\\Phi applications)|six.*\\\\Phi|\\\\Phi.*six.*routes' chapters notes compute tests --glob '*.tex' --glob '*.py'
rg -n --pcre2 'BKM.*Yangian|Yangian.*BKM|Drinfeld Yangian|Hall--Drinfeld|Hall-Drinfeld' chapters notes compute tests --glob '*.tex' --glob '*.py'
rg -n --pcre2 'Delta_5.*(?:input|output)|(?:input|output).*Delta_5|Delta\\_5|\\\\Delta_5' chapters notes compute tests --glob '*.tex' --glob '*.py'
rg -n --pcre2 'CY-C|Super-Yangian|Y_\\{osp\\}|osp\\(4\\|20\\)|ClaimStatusProvedHere|ClaimStatusConditional|conjectur|conditional' chapters notes compute tests --glob '*.tex' --glob '*.py'
```

Narrow pytest planning and results:

```bash
python3 -m pytest compute/tests/test_kappa_ch_d3_formula.py ...
# Failed before collection: /usr/bin/python3 has no pytest installed.

pytest compute/tests/test_kappa_ch_d3_formula.py \
  compute/tests/test_cy_d_kappa_d3.py \
  compute/tests/test_k3e_yangian_phi3_identification.py \
  compute/tests/test_kappa_bkm_adversarial.py \
  compute/tests/test_kappa_spectrum_reconciliation.py \
  compute/tests/test_cy_c_six_routes.py \
  compute/tests/test_cy3_bridge_normal_form.py -q
# 353 passed in 0.66s

pytest compute/tests/test_k3_yangian_borcherds_weight_theta_refinement.py \
  compute/tests/test_kappa_bkm_universal.py -q
# 183 passed, 3 failed.
```

The three failures are exactly the stale BKM decomposition expectations
in `compute/tests/test_kappa_bkm_universal.py`; the theta-refinement file
passes alone:

```bash
pytest compute/tests/test_k3_yangian_borcherds_weight_theta_refinement.py -q
# 79 passed in 0.07s
```

## Recommended Next Edits

1. In `chapters/theory/cy_to_chiral.tex:4781`, replace the full-Yangian
   equality to `\mathcal{W}_{1+\infty}` by an evaluation/action statement
   through the Drinfeld double/center.
2. Update `compute/tests/test_kappa_bkm_universal.py` to match the
   repaired oracle: five literal-additive failures, zero successes, and
   the new keys in `compute/lib/kappa_bkm_universal.py`.
3. Sweep the listed changed notes for unqualified
   `\kappa_{\mathrm{ch}}(K3 x E)=3`; either add the Heisenberg superscript
   or change compact total-space statements to `0`.
4. Cross-qualify the `Delta_5` input/output wording so "input" only means
   boundary datum or Borcherds-lift seed, never denial of the one-loop
   output theorem.
5. Optionally clean stale test names/docstrings that call route-dependent
   ranks `kappa_ch`; the executable assertions already know compact `0`
   versus Heisenberg `3`, but the prose invites future regression.

## Surface Convergence

Not fully converged. The core chapter repairs mostly hold, but there is
one reader-facing CoHA/Yangian equality to fix, one failing compute-test
surface after the BKM repair, several changed notes with old compact
K3 x E language, and moderate-risk `Delta_5` input/output wording.

No chapters, compute files, tests, scripts, `CLAUDE.md`, or `AGENTS.md`
were edited by this lane.
