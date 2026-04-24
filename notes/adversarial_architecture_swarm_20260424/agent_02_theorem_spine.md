# Agent 02 theorem spine audit: A/B/C/D/H

Date: 2026-04-24.

Scope: theorem spine A/B/C/D/H, with anchors in `metadata/theorem_registry.md`, `metadata/claims.jsonl`, Vol III theorem chapters, `chapters/examples/cy_d_kappa_stratification.tex`, and Vol I `chapters/connections/{master_concordance,concordance}.tex`.

Files changed: this report only.
Build/tests: not run; this was a source audit and report write.

## Verdict

The theorem spine is usable only after five demotions/sharpenings. The fatal pattern is not a single false formula; it is promotion pressure around conditional CY-A3, bar-hocolim, and Hochschild/derived-centre language. The local TeX often knows the right scope, but metadata and downstream prose frequently restate conditional results as proved global infrastructure.

## ATTACK_1 / HEAL_1: Theorem A/B bar-hocolim overreach

Attack. `chapters/theory/cy_to_chiral.tex:4205` states `thm:bar-hocolim` as `\ClaimStatusProvedHere`, and `4208--4212` asserts
`B^{E_1}(hocolim D) \simeq hocolim B^{E_1}(D)` for any finite-poset diagram of `E_1`-chiral algebras. The proof contradicts the stated adjunction: `4218` says `\Omega^{E_1} \dashv B^{E_1}` with cobar left, bar right. A right adjoint does not preserve homotopy colimits. The line `4216` tries to make `B^{E_1}` a left derived indecomposables functor, but this is not reconciled with `4218`.

Damage. CY-A3 conclusion `concl:shadow` depends on this theorem at `chapters/theory/cy_to_chiral.tex:4736`. Therefore the A/B inversion spine is being used as global gluing infrastructure without the actual colimit-preservation proof.

Heal. Demote `thm:bar-hocolim` to `\ClaimStatusConditional{}` unless a separate proof is supplied. Replace the theorem statement by:

> For diagrams whose transition maps are `E_1` quasi-isomorphisms between cofibrant Koszul objects, the induced bar diagrams are objectwise quasi-isomorphic, so the comparison from the bar of any chosen chart to the hocolim bar is a quasi-isomorphism. No assertion is made for arbitrary finite homotopy colimits.

Exact edits:
- `chapters/theory/cy_to_chiral.tex:4203`: replace "The bar construction commutes with homotopy colimits" by "On the Koszul chart-equivalence locus, the bar construction is compatible with the chart hocolim up to the stated comparison map."
- `chapters/theory/cy_to_chiral.tex:4207`: change `\ClaimStatusProvedHere{}` to `\ClaimStatusConditional{}`.
- `chapters/theory/cy_to_chiral.tex:4208--4212`: restrict to diagrams with equivalence transition maps, or replace the displayed equivalence by a named comparison map.
- `chapters/theory/cy_to_chiral.tex:4215--4218`: remove the left-derived/right-adjoint argument and cite the actual Koszul-locus comparison.

## ATTACK_2 / HEAL_2: CY-A3 status drift infects downstream spine

Attack. The TeX theorem is correctly conditional: `chapters/theory/cy_to_chiral.tex:4691--4693` labels `thm:cy-to-chiral-d3` as a framed object-level `d=3` locus, `\ClaimStatusConditional{}`. Its proof narrows further at `4765--4769`: connectivity, unit-connectedness, finite Leray cover, and Borel-summable positivity regimes are load-bearing. But `metadata/claims.jsonl:966` records the same label as `ProvedHere`, and `metadata/claims.jsonl:1053` records `thm:e1-sector-d3` as `ProvedElsewhere` although the TeX at `chapters/theory/e1_chiral_algebras.tex:175--178` is `\ClaimStatusConditional{}`.

Damage. This drift lets downstream lines read "proved via Phi_3" when the local theorem says "conditional framed object-level assignment." Example: `chapters/theory/cy_to_chiral.tex:4363` marks the quintic row "Proved (via Phi_3)," while `chapters/theory/cy_to_chiral.tex:4802` correctly calls framed `\Phi_3` a conditional theorem.

Heal. Treat metadata as stale and regenerate only after source scope is repaired. The mathematical statement should be:

> CY-A3 is a conditional framed object-level construction on H1--H4 and the named analytic completion regimes. Toric Hall outputs are separately verified. It is not a global functor on arbitrary CY3 morphisms and not a global quantum group construction.

Exact edits:
- `metadata/claims.jsonl:966`: status must be `Conditional`, and the line number must be regenerated from the current source.
- `metadata/claims.jsonl:1053`: status must be `Conditional`.
- `chapters/theory/cy_to_chiral.tex:4363`: replace "Proved (via `\Phi_3`...)" by "Conditional on the framed object-level `\Phi_3` locus; genus-1 BCOV comparison separately verified where cited."
- Keep `chapters/theory/cy_to_chiral.tex:4802` as the controlling status language.

## ATTACK_3 / HEAL_3: Theorem D / CY-D mixes three kappa readings

Attack. `chapters/theory/modular_trace.tex:25--27` marks CY-D as `ProvedHere`, but the theorem begins with unrestricted `A_\cC=\Phi(\cC)` at `39--40`, even though `\Phi_3` is conditional. It also defines operational `\kappa_{\mathrm{ch}}` as Kunneth-additive at `28--37`, while `chapters/examples/cy_d_kappa_stratification.tex:1688--1703` says odd compact CY has `\kappa_{\mathrm{ch}}=0` by Hodge supertrace cancellation. Those are not the same invariant. `chapters/theory/cy_to_chiral.tex:4720--4735` adds a third reading: Stage-2 Heisenberg/BCOV/local values.

Damage. Theorem D's scalar leading coefficient is no longer typed. The same symbol `\kappa_{\mathrm{ch}}` denotes: Hodge comparator, Stage-2 Heisenberg rank, and BCOV/local shadow reading. This is exactly the drift that the four-kappa discipline was meant to prevent.

Heal. Split CY-D into one proved theorem plus two scoped comparisons:

1. Proved: CY-D2, `d=2`, `h^{1,0}=0`, `\kappa_{\mathrm{ch}}=\chi(\mathcal O_X)`.
2. Proved comparator: `\kappa_{\mathrm{ch}}^{\mathrm{Hodge}}(X)=\sum_q(-1)^q h^{0,q}(X)`, hence zero for odd compact CY.
3. Conditional/stage-specific: operational `\kappa_{\mathrm{ch}}^{\mathrm{Stage2}}` values for CY3 shadows, including Heisenberg, BCOV, and local readings.

Exact edits:
- `chapters/theory/modular_trace.tex:27`: demote the current omnibus theorem to `\ClaimStatusConditional{}` or split it.
- `chapters/theory/modular_trace.tex:39--40`: replace `A_\cC=\Phi(\cC)` by "where the relevant `\Phi_d` output is constructed."
- `chapters/theory/modular_trace.tex:51--59`: replace "bare `\kappa_{\mathrm{ch}}` need not vanish" with "`\kappa_{\mathrm{ch}}^{\mathrm{Hodge}}` vanishes; Stage-2 operational readings are separate."
- `chapters/examples/cy_d_kappa_stratification.tex:1690` and `1701--1703`: replace `\kappa_{\mathrm{ch}}=0` by `\kappa_{\mathrm{ch}}^{\mathrm{Hodge}}=0`.
- `chapters/theory/modular_trace.tex:223` and `228`: replace "CY-A3 settles the existence" / "accessible via CY-A3" by "on the framed object-level CY-A3 locus."

## ATTACK_4 / HEAL_4: Theorem C / derived-centre statements are overtyped

Attack. Vol I is precise: Theorem A produces reconstruction and duality separately (`/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:763--769`), and the canonical Theorem C five-element bucket is an archetype bucket, not a universal bound (`175--230`). Vol III sometimes respects this, e.g. `chapters/examples/cy_d_kappa_stratification.tex:1916--1934`. But the derived-centre layer overstates its scope:

- `chapters/theory/drinfeld_center.tex:116--127` states `cor:zder-drinfeld` for any `E_1`-chiral algebra, while the proof uses bar-cobar inversion "on the Koszul locus" at `132--133`.
- `chapters/theory/e2_chiral_algebras.tex:2435--2465` states `thm:e2ca-coend-equals-derived-centre` as `ProvedHere`, identifying a Lyubashenko coend in a finite braided tensor category with an `E_2`-chiral derived centre of `\mathbf H_{\Delta_5}`. The proof at `2485--2493` depends on an additional identification of `Rep^{fd}(u_{\zeta_8})` with `\Phi_2(D^bCoh(K3))` as an `E_2`-chiral algebra.
- `chapters/theory/e2_chiral_algebras.tex:2262--2275` declares derived conductor preservation for any class `G/L/C/M` algebra by a telescoping identity, but no convergence/summability condition is included in the theorem statement even though class M has factorial growth just above it at `2252--2259`.

Damage. Theorem C is being turned from a scoped complementarity theorem into a universal derived-centre/coend/conductor machine.

Heal. Keep the derived-centre theorem, but type every arrow:

- `chapters/theory/drinfeld_center.tex:119`: add "For a modular Koszul `E_1`-chiral algebra `A` on the Koszul locus..." and keep `ProvedHere`.
- `chapters/theory/e2_chiral_algebras.tex:2437`: demote to `\ClaimStatusConditional{}` unless the `Rep^{fd}(u_{\zeta_8}) \simeq \Phi_2(D^bCoh(K3))` equivalence is proved in-tree with exact reference.
- `chapters/theory/e2_chiral_algebras.tex:2265`: restrict to convergence-complete `A_\infty` structures: class G/L proved; class C under exponential convergence; class M only under Borel-summability hypotheses. Otherwise demote `thm:derived-conductor` to Conditional.

## ATTACK_5 / HEAL_5: Theorem H is conflating chiral and categorical Hochschild

Attack. Vol I explicitly separates the three Hochschild theories at `/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:236--292`, and says Theorem H is chiral Hochschild concentrated in `{0,1,2}` for modular Koszul algebras (`254--260`). It also records a critical-level failure at `7639--7645`. Vol III mostly knows this: `chapters/theory/hochschild_calculus.tex:845--860` states ordinary chiral Theorem H, then `863--900` introduces a CY-dimension promotion. But `chapters/theory/drinfeld_center.tex:753--760` gives a "Categorical Theorem H" with `HH^k(C)=0 for k>d` "from smoothness and properness." That categorical claim is false in the usual HKR grading: for a smooth proper variety of dimension d, Hochschild cohomology has contributions up to degree `2d`.

Damage. Theorem H's proven chiral concentration is being used to assert a categorical Hochschild vanishing theorem. This breaks the typed separation in Vol I and can feed false deformation-obstruction claims.

Heal. Replace `thm:categorical-thm-h` with a convention/proposition that does not assert categorical vanishing:

> For a smooth proper CY_d category, categorical Hochschild cohomology is governed by HKR/Toën deformation theory and carries its CY shifted Poisson structure. The chiral Hochschild concentration theorem applies only after a constructed modular Koszul chiral output `A_C=\Phi_d(C)` is fixed; at CY-dimension promoted loci the stated chiral amplitude is conditional on the corresponding `\Phi_d` construction.

Exact edits:
- `chapters/theory/drinfeld_center.tex:753--760`: delete item (i), or replace it with the correct HKR amplitude statement.
- Keep `\ClaimStatusConditional` at `755`, but change title to "Categorical Hochschild comparison with Theorem H" rather than "Categorical Theorem H."
- `chapters/theory/hochschild_calculus.tex:893--900`: demote the general CY-d pattern to `Expected/Conditional` unless a proof is supplied for every `d`; retain the `d=3` K3xE statement only under the stated Humbert/Koszul scope.

## Remaining open obligations

1. Rebuild the theorem registry after source status corrections. Current `metadata/theorem_registry.md` is only a 2026-04-23 summary, while `metadata/claims.jsonl` contains stale line numbers and wrong statuses for CY-A3 and `thm:e1-sector-d3`.
2. Decide whether `thm:bar-hocolim` is to be proved as a genuine bar-colimit theorem or replaced by chart-equivalence descent. Without that decision, `concl:shadow` in CY-A3 remains underived.
3. Normalize Theorem D notation across `modular_trace.tex`, `cy_to_chiral.tex`, and `cy_d_kappa_stratification.tex`: Hodge comparator, Stage-2 Heisenberg rank, BCOV reading, and BKM weight must not share an unqualified `\kappa_{\mathrm{ch}}` assertion.

## Convergence status

CONVERGED for report scope: five attack/heal cycles completed; no source edits made; exact recommendations supplied for main-thread integration.
