# Agent 5 cross-volume attack/heal report

Date: 2026-04-24.

Scope: report-only audit of CY3 bridge language against Vol I/II/III coherence.
Write scope honored: this file only.

Method: loaded Vol III `AGENTS.md`, `CLAUDE.md`, and the Beilinson/cross-volume
workflow.  Ran targeted greps and local reads in:

- `~/calabi-yau-quantum-groups`
- `~/chiral-bar-cobar`
- `~/chiral-bar-cobar-vol2`

No chapters, compute files, metadata, or build products were edited.

## Verdict

The fixed abelian `C3` chart theorem is useful and correctly scoped when read
literally: it kills only the positive torus-fixed finite-mode projection of the
local hCS--Hall chart obstruction.  The false shortcut is to use that finite
chart as a certificate for any of the following:

1. direct `CoHA(C3) = W_{1+infty}`;
2. global compact `K3 x E` hCS--Hall descent;
3. Hall--Drinfeld/BKM closure;
4. protected physics closure;
5. native `E_2` CY3 output on the algebra rather than on the centre;
6. six-route CY-C convergence as automatic functoriality.

The executable normal-form gate is a good start, but its current default
supplies the `drinfeld_double_before_w` gate before a full double, pairing,
completion, and Fock/evaluation model are explicitly supplied.  That creates a
latent cross-volume over-read.

## Brutal attack list

### 1. Unconditional Stage-1/Hall comparison on `C3`

Anchor: `chapters/examples/toric_cy3_coha.tex:102-125`.

Attack: `thm:sv-c3-e3-factorization` is now `\ClaimStatusProvedHere` and says
`PhiFA_3(Perf(C3))` is computed by `U -> H^*_T(Hilb^bullet(U))`, with Hall
global sections giving `CoHA(C3)=Y^+`.  This can be read as an unconditional
identification of the Stage-1 holomorphic `E_3` factorisation algebra with the
associative Hall algebra.  That breaks the new normal-form discipline, where
the Hall comparison requires typed hCS--Hall chart data.

Heal language:

> On `C3`, Schiffmann--Vasserot identifies the Hall cohomology target
> `CoHA(C3)` with the positive half `Y^+`.  A comparison from
> `PhiFA_3(Perf(C3))` to this Hall target is a Hall-valued shadow, conditional
> on the fixed Stage-1 `E_3` formality/locality witness and the supplied
> hCS--Hall chart map.  It is not an equality between `PhiFA_3` and the
> associative CoHA.

Propagation targets: `chapters/examples/toric_cy3_coha.tex`,
`chapters/theory/cy3_chain_level_bridge.tex`, any standalone excerpt of
`toric_cy3_coha`.

### 2. Fixed abelian chart overpromoted to full local closure

Anchor: `chapters/theory/cy3_chain_level_bridge.tex:3210-3260`.

Attack: the theorem correctly says
`pr_{fp,+}(o_theta)=0`, but any later prose that shortens this to
`o_theta=0` or "the `C3` bridge is closed" is false.  The proof itself says it
makes no claim about analytic extension to full renormalised hCS observables or
descent over a non-affine cover.

Heal language:

> The fixed abelian chart kills only `o_theta^{fp,+}`.  The residual local
> obstruction is the pair `o_theta^{ren} + o_theta^{des}`: renormalised analytic
> extension plus descent/gluing.  No full local hCS--Hall comparison follows
> until those residual terms vanish.

Propagation targets: any reference to `thm:c3-fixed-abelian-chart-map`,
especially `cy3_chain_level_bridge`, `toric_cy3_coha`, and normal-form tests.

### 3. Executable gate supplies the W-passage too early

Anchors:

- `compute/lib/cy3_bridge_normal_form.py:220-223`
- `compute/tests/test_cy3_bridge_normal_form.py:25-31`

Attack: `c3_local_datum()` includes `drinfeld_double_before_w` by default, so
adding only `supply_hcs_hall_map=True` makes the test assert
`datum.closes("w_infty_representation")`.  This is stronger than the fixed
abelian theorem.  The chart map should close local `C3 -> Y^+`, not the
Drinfeld double/Fock/evaluation representation.

Heal language:

> Split `drinfeld_double_before_w` into two gates: (i) `typed_no_direct_w`
> forbidding the shortcut, and (ii) `drinfeld_double_fock_evaluation` supplying
> the actual double, Hopf pairing/completion, and Fock/evaluation model.  The
> fixed abelian chart supplies (i), not (ii).

Propagation targets: `compute/lib/cy3_bridge_normal_form.py`,
`compute/tests/test_cy3_bridge_normal_form.py`, manuscript references to the
oracle.

### 4. Direct object equality between the Drinfeld double and `W_{1+infty}`

Anchors:

- Vol I `compute/lib/theorem_coha_dt_shadow_engine.py:84-85`
- Vol I `compute/lib/theorem_coha_dt_shadow_engine.py:947-948`
- Vol I `compute/lib/c3_functor_chain.py:58-65`

Attack: phrases such as "Drinfeld double = W_{1+infty}" and
"the full affine Yangian is isomorphic to W_{1+infinity}" collapse an
algebraic double into a vertex-algebra representation/evaluation target.  This
is exactly the CoHA/W shortcut the Vol III gates forbid.

Heal language:

> `CoHA(C3)=Y^+(\widehat{gl}_1)` is the positive-half Hall theorem.  The full
> affine Yangian is reached by the Drinfeld double after the Hopf pairing and
> completion are fixed; `W_{1+infty}` is then accessed through the
> Prochazka--Rapcak/Gaiotto--Rapcak Fock/evaluation representation, not by
> identifying the CoHA or the double with the vertex algebra as a bare object.

Propagation targets: Vol I compute comments/tests and any manuscript prose that
uses "Drinfeld double = W" as an equality.

### 5. Toric `C3` chiral quantum group corollary still says too much

Anchor: `chapters/examples/toric_cy3_coha.tex:2050-2077`.

Attack: the corollary is now `\ClaimStatusConditional`, but the body still ends
"All five components are unconditional" and includes a Drinfeld centre
equivalence.  That contradicts its own status and the new gate discipline.

Heal language:

> The positive-half Hall component is unconditional by Schiffmann--Vasserot.
> The full Yangian, Fock/evaluation `W_{1+infty}` passage, and Drinfeld-centre
> equivalence are conditional on the Hopf pairing/completion and the centre
> comparison theorem in the stated category.

Propagation targets: `chapters/examples/toric_cy3_coha.tex` and downstream
standalone builds.

### 6. Six routes re-collapsed through one Stage-1 object

Anchor: `chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex:1952-2025`.

Attack: the section title and conjecture recast the six CY-C routes as six
`(Sigma_2,C)`-specialisations of one `PhiFA_3(D^bCoh(K3 x E))`.  This avoids
"six `Phi_3` applications" verbally, but can still collapse the independent
input data: Borcherds Jacobi-form input, lattice VOA input, reduced DT input,
orbifold input, and half-twist input are not automatically specialisations of
one canonical Stage-1 object.  The phrase "The six applications" at line 2010
is especially dangerous.

Heal language:

> The six routes are six independent construction machines.  A single
> Stage-1 `PhiFA_3(K3 x E)` may serve as a comparison hub only after each route
> is connected to it by a named, status-labelled bridge.  CY-C is the
> conjectural convergence of those bridges, not a consequence of Stage-2
> specialisation functoriality.

Propagation targets:
`chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex`,
`chapters/examples/cy_c_six_routes_convergence.tex`, Vol I/II frontier prose.

### 7. Global `K3 x E` DWR cover language is too toric

Anchor: `chapters/theory/cy3_chain_level_bridge.tex:3401-3413`.

Attack: an algebraic cover of compact `K3 x E` by affine toric charts
`U_i ~= C3` is too strong.  Kummer/ADE charts are local models; generic K3
requires Stein polydiscs, not global toric `C3` charts.  If this is read as a
proved global toric DWR cover, it falsely supplies the descent input.

Heal language:

> Use a DWR-good Stein/polydisc cover as a hypothesis.  On the Kummer/ADE
> locus, selected local charts have toric `C3` or McKay models; they are local
> witnesses, not a global toric atlas of compact `K3 x E`.

Propagation targets: `cy3_chain_level_bridge`,
`k3e_cy3_programme`, any note claiming "K3 x E DWR closure".

### 8. Hall-side orientation and TS data mistaken for relative comparison data

Anchor: `chapters/theory/cy3_chain_level_bridge.tex:3444-3509`.

Attack: the current text mostly warns correctly, but this is a common
over-read.  Trivialising the Hall orientation torsor and checking Hall-side
Thom--Sebastiani associativity do not kill the relative hCS--Hall comparison
classes.  They prepare the target; they do not produce the map.

Heal language:

> Hall orientation, grading/Tate normalisation, and Thom--Sebastiani
> coherence are target-side preparatory data.  The relative classes
> `o_or`, `o_gr`, `o_TS`, and `o_fact` vanish only after a chartwise
> hCS--Hall map is fixed and checked on overlaps.

Propagation targets: `cy3_chain_level_bridge`, `k3e_cy3_programme`,
`notes/bps_positive_geometry_total_resolution_20260424/*`.

### 9. Native `E_2` CY3 output through "Drinfeld double" wording

Anchor: Vol I `compute/tests/test_dunn_obstruction.py:469-477`.

Attack: "CY3 enhanced to `E_2` via Drinfeld double" and
"CY3 `E_1 -> E_2` obstruction is ZERO" are safe only if the object is the
Drinfeld centre / representation category.  Read literally, they assert native
`E_2` structure on the CY3 chiral algebra, contradicting the Vol III rule:
at `d >= 3`, `A` is `E_1`; `E_2` lives on `Z(Rep(A))`.

Heal language:

> CY3 native output is `E_1`.  The `E_2` structure is the braided structure on
> the Drinfeld centre of the `E_1` representation category, after the relevant
> pairing/completion data are supplied.  The obstruction is zero for the centre
> construction, not for upgrading `A` itself to native `E_2`.

Propagation targets: Vol I Dunn obstruction engine/tests, Vol II prefatory
bridges, Vol III `e1/e2` hierarchy references.

### 10. `\kappa_{\mathrm{BKM}}` additive formula and denominator indexing

Anchor: Vol II `main.tex:1438-1451` is currently a good pattern: it states the
additive split is false and uses `c_N(0)/2`.

Attack: any future CY3 bridge prose that recovers `5` by
`\kappa_{\mathrm{ch}} + \chi(O_fiber)` or omits the input denominator will
break Vol I/II/III coherence.  The report grep found many cache and note
anchors preserving this warning; the active manuscript must keep the same
discipline.

Heal language:

> Always write `\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2` and name the
> denominator convention.  For the K3/paramodular lane this is the
> `Delta_5`/`Phi_{10}` convention giving `5`; for Fake-Monster lanes this is a
> different denominator and a different value.  Never derive the BKM scalar
> from `\kappa_{\mathrm{ch}}` plus a fibre Euler term.

Propagation targets: Vol I landscape/census references, Vol II universal trace
paragraphs, Vol III `cy_d_kappa_stratification` and K3xE chapters.

## Integration language block

Use this paragraph, with local notation adjusted, whenever citing the fixed
abelian chart:

> The fixed abelian `C3` chart theorem supplies a finite-mode positive-sector
> witness
> `theta_C3^{fp}: Obs_hCS^{q,fp,+}(C3; ghat) -> Y_T^+(ghat)`.  It proves
> `pr_{fp,+}(o_theta)=0`, hence verifies the Schiffmann--Vasserot shuffle
> normal form on the torus-fixed abelian sector.  It does not construct the
> full renormalised hCS--Hall morphism, does not perform DWR/Ran descent, does
> not form the Hall--Drinfeld double, and does not identify the CoHA with
> `W_{1+infty}`.  The admissible typed route is
> `CoHA(C3)=Y^+ -> D(Y^+) -> W_{1+infty}` after the double, pairing,
> completion, and Fock/evaluation gates are separately supplied.

Use this paragraph for compact `K3 x E`:

> On `K3 x E`, local `C3`/polydisc charts are witnesses for the positive-half
> normal form.  A global theorem requires a DWR-good cover, chartwise
> hCS--Hall maps, Maurer--Cartan descent, orientation transport,
> grading/Tate compatibility, Thom--Sebastiani compatibility, and
> factorisation compatibility.  Hall-side orientation or local anomaly
> vanishing alone does not supply the global comparison.

Use this paragraph for six-route CY-C:

> The six routes to `G(K3 x E)` are six independent constructions with distinct
> input data.  A common Stage-1 factorisation object may be used only as a
> comparison hub after named bridges from each route have been supplied and
> status-labelled.  CY-C is the convergence assertion for those bridges, not a
> formal consequence of applying `Phi_3` or `SpCh` six times.

## Top 10 recommendations

1. Downgrade or re-scope `thm:sv-c3-e3-factorization` from unconditional
   `ProvedHere` to a conditional Hall-shadow comparison.
2. Keep `thm:c3-fixed-abelian-chart-map` exactly finite-mode/projected:
   `pr_{fp,+}(o_theta)=0`, never `o_theta=0`.
3. Split the executable W-gate into "shortcut forbidden" and "actual
   double/Fock supplied".
4. Replace every "Drinfeld double = W" phrase in Vol I compute comments with
   "Drinfeld double plus Fock/evaluation representation reaches W".
5. Remove "All five components are unconditional" from the conditional `C3`
   chiral quantum group corollary unless every component is independently
   supplied.
6. Reframe "six applications" in the CY-C beyond chapter as six independent
   constructions with optional comparison bridges to a Stage-1 hub.
7. Replace global toric `C3` cover language for `K3 x E` with a DWR-good
   Stein/polydisc cover hypothesis and local toric/McKay witnesses.
8. Preserve the target-side vs relative-comparison distinction for orientation,
   grading, Thom--Sebastiani, and factorisation data.
9. Audit Vol I/II `E_1 -> E_2` language so `E_2` is always on the Drinfeld
   centre / representation category, not on the CY3 algebra `A`.
10. Keep `\kappa_{\mathrm{BKM}}` denominator-indexed by `c_N(0)/2`; never use
    the false additive fibre formula.

## Files changed

- `notes/swarm_20260424_remaining/agent_5_cross_volume_attack_heal.md`

## Verification

No build or test run.  This was a targeted cross-volume grep/read audit and
report-only integration note.
