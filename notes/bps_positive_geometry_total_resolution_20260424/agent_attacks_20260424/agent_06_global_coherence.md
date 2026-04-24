# Agent 06 Global Coherence Attack

Date: 2026-04-24.

Scope: `chapters/theory/bps_positive_geometry_closure.tex`,
`main.tex`, `compute/lib/bps_positive_truncation.py`,
`compute/tests/test_bps_positive_truncation.py`, and
`notes/bps_positive_geometry_total_resolution_20260424/`.

Verdict: the finite-first object is the surviving core.  The fatal
failure mode is not the definition of the object; it is the promotion of
typed residual equations into actual solved points by inserting zero
vectors and a toy Gram matrix.  The healing theorem is stronger: the
global object is a derived zero-locus machine whose named closed
substacks become actual solutions only when their geometric obstruction
vectors are computed from the named chamber and vanish compatibly in the
finite-to-pro tower.

Executable checks run:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider \
  compute/tests/test_bps_positive_truncation.py

29 passed in 0.70s
```

Additional runtime inspection:

```text
derived_solution_stack passed=True exact=True checked=156
seven_extension_resolution passed=True exact=False checked=449
k3e_unquotiented_radical passed=True exact=False checked=8
```

No bare scalar invariant violation was found on the audited manuscript
and compute files.  The scalar-invariant hits in the scoped notes were
subscripted as `\kappa_{\mathrm{BKM}}`.

I did not run `make fast`: this lane's write scope is the report note,
and a full LaTeX build writes auxiliary/log/PDF surfaces.  Macro risk was
checked by source inspection: `\BPS`, `\CoHA`, `\hCS`, `\Hall`,
`\Obs`, `\frakg`, and `\gDelta` are provided in `main.tex`.

## Attack 1: finite quotients are not automatically Hall quotient algebras

- claim attacked

  `thm:bps-positive-finite-first-existence` asserts that the set
  `Gamma_{S,<=N,<=R}` gives finite quotient Hall algebras and that
  terms leaving the set are killed by a closed two-sided Hall ideal.

- strongest failure mode

  The retained set is defined by simultaneous bounds
  `h(gamma)<=N`, `|Z(gamma)|<=R`, and `Q(gamma)>=0`.  This set is finite
  under the support property, but finiteness does not imply that its
  complement is a Hall ideal.  Radius is not monotone under addition in a
  strict sector of width `< pi`; a charge outside a radius ball can be
  added to another charge and re-enter the ball.  The proof also uses
  properness of the Hall correspondence on the finite quotient, but a
  finite charge set does not by itself make the extension stack proper or
  admissible for the chosen motivic pushforward.

- fatal/nonfatal verdict

  Fatal for the theorem as written.  Nonfatal for the programme: replace
  rectangular truncations by finite saturated lower sets and add
  Hall-admissibility of extension correspondences.

- exact repair/heal theorem statement

  Let `L subset Gamma^+_{sigma,S}` be a finite saturated lower subset of
  the active charge monoid such that `Gamma^+_{sigma,S}\setminus L`
  generates a closed two-sided Hall ideal, and assume that all
  semistable stacks and extension stacks over `L` are admissible for the
  chosen vanishing-cycle motivic coefficient theory.  Then
  `H^{Mot,o}_{sigma,S,L}` is an associative oriented motivic Hall algebra.
  For any cofinal Mittag-Leffler tower of such lower subsets `L`, the
  completed chambered BPS positive geometry is
  `varprojlim_L H^{Mot,o}_{sigma,S,L}`.  The displayed
  `(N,R)` truncation is valid only after replacing it by its saturated
  Hall-lower closure or by a cofinal lower-set refinement.

- local file anchors

  `chapters/theory/bps_positive_geometry_closure.tex:43-73`,
  `chapters/theory/bps_positive_geometry_closure.tex:99-155`,
  `compute/lib/bps_positive_truncation.py:375-399`,
  `compute/lib/bps_positive_truncation.py:314-326`.

- primary/literature anchors if needed from existing bibliography or local notes

  Kontsevich-Soibelman CoHA and motivic DT:
  `bibliography/references.tex:553-554`.  Worker 09 already states the
  quotient must be by the closed Hall ideal `I_{>N,>R}`:
  `notes/bps_positive_geometry_total_resolution_20260424/agent_09_compute_truncation_engine.md:12-42`.

- executable checks proposed or run

  Run: focused test file passes.  Proposed: add a test constructing a
  truncation where the retained set is not lower closed and assert that
  quotient construction refuses it.  Add `finite_lower_set_certificate`
  checking additive ideal closure:
  if `gamma notin L` and `delta in Gamma^+`, then every retained
  extension charge `gamma+delta` is outside `L`.

- remaining point-construction obligation

  Construct the cofinal tower of saturated Hall-lower finite charge sets
  for each compact chamber and prove the extension stacks are
  Hall-admissible in the chosen motivic coefficient target.

## Attack 2: `ExCert` is used before it is defined in the manuscript

- claim attacked

  The proposition on quintic and Schoen certificates uses
  `operatorname{ExCert}` and marks the certificate theorem
  `ProvedHere`.

- strongest failure mode

  `ExCert` is not defined in the manuscript chapter before first use.
  The notes define it as a full tuple, but the reader-facing theorem
  only names it.  An undefined predicate cannot carry an iff theorem.

- fatal/nonfatal verdict

  Fatal as a manuscript proof-form issue.  Nonfatal mathematically,
  because the exact tuple is already present in local notes.

- exact repair/heal theorem statement

  Define
  `ExCert(X;sigma,Q,S,o,T_eq,Mot)` to be the tuple consisting of:
  the 3-CY category, numerical charge lattice, skew Euler form,
  Bridgeland or explicitly named Hall stability datum, support form,
  active-ray-free strict sector, orientation output or gerbe-twisted
  orientation output, oriented critical atlas, motivic coefficient
  target, equivariance, finite HN control, motivic integration, and
  realization tower.  Then
  `ExCert(X;...) => P^{BPS}_{sigma,S,o,T_eq}(X)` by the finite-first
  theorem, after the finite lower-set and Hall-admissibility hypotheses
  of Attack 1.

- local file anchors

  `chapters/theory/bps_positive_geometry_closure.tex:220-253`,
  `notes/bps_positive_geometry_total_resolution_20260424/agent_10_compact_examples_and_falsification.md:17-79`,
  `notes/bps_positive_geometry_total_resolution_20260424/seven_extension_resolution_20260424.md:31-83`.

- primary/literature anchors if needed from existing bibliography or local notes

  Bridgeland stability: `bibliography/references.tex:683-684`.
  Bayer-Macri-Stellari compact non-toric input:
  `bibliography/references.tex:391-392`.
  PTVV shifted symplectic input: `bibliography/references.tex:342`.

- executable checks proposed or run

  Run: `quintic_excert_surface_certificate()` passes but returns
  `exact=False`.  Proposed: add a serialization test for the exact
  `ExCert` fields so the manuscript tuple and compute certificate cannot
  drift.

- remaining point-construction obligation

  For the quintic: construct actual Bridgeland/support/HN data and the
  Hall-admissible finite lower-set tower.  For Schoen: construct compact
  Hall gluing on overlaps, not merely local banana shadow data.

## Attack 3: derived solution stack exactness is overpromoted in compute

- claim attacked

  `derived_solution_stack_certificate()` returns `exact=True`, and tests
  assert it is exact and passed.

- strongest failure mode

  The function inserts zero obstruction vectors for quintic, Schoen,
  theta comparison, and hCS.  It also treats non-exact ledger
  certificates as solved factors because `SolutionStackFactor.solved`
  ignores the certificate's `exact` flag.  Thus a placeholder ledger
  becomes an actual zero-fiber point.

- fatal/nonfatal verdict

  Fatal for compute-manuscript coherence.  The derived zero-locus
  construction can be exact; the claim that the named factors are solved
  is not exact until their obstruction coordinates are computed from
  geometry.

- exact repair/heal theorem statement

  The finite residual solution stack
  `Sol^{BPS}_{<=N,<=R}` is exactly the derived zero locus of the finite
  obstruction map.  A named factor gives an actual point if and only if
  its certificate is exact, discrepancy-free, and its obstruction vector
  is computed from the named finite geometric data and vanishes.  A
  discrepancy-free `exact=False` ledger defines a closed equation target;
  it does not define a point.

- local file anchors

  `compute/lib/bps_positive_truncation.py:283-294`,
  `compute/lib/bps_positive_truncation.py:829-894`,
  `compute/lib/bps_positive_truncation.py:897-923`,
  `compute/tests/test_bps_positive_truncation.py:292-312`,
  `chapters/theory/bps_positive_geometry_closure.tex:538-590`.

- primary/literature anchors if needed from existing bibliography or local notes

  Local notes already impose this distinction:
  `notes/bps_positive_geometry_total_resolution_20260424/seven_extension_resolution_20260424.md:351-385`.

- executable checks proposed or run

  Run: runtime inspection shows all factors report `solved=True`,
  including `exact=False` ledgers.  Proposed tests:
  `assert not factor.solved` for every factor with
  `not factor.certificate.exact`, and
  `assert not derived_solution_stack_certificate(bound).exact` until all
  non-exact factors are replaced by computed exact obstruction vectors.

- remaining point-construction obligation

  Replace zero placeholders by actual obstruction values for the quintic,
  Schoen, raw `K3 x E`, theta comparison, and named hCS compact examples.

## Attack 4: raw `K3 x E` radical-zero is replaced by a toy diagonal matrix

- claim attacked

  The manuscript states the raw `K3 x E` Hall-Borcherds theorem is
  equivalent to vanishing of every finite automorphic radical, while the
  derived solution stack factor marks the raw radical solved by a
  diagonal `FiniteLinearMap((2,3,5))`.

- strongest failure mode

  The diagonal matrix is not constructed from a finite Hall quotient of
  `CoHA^{Mot,o}_{crit}(K3 x E)`, not from the automorphic denominator
  pairing, and not from the orientation character.  It is a full-rank
  witness for the linear algebra routine, not the `K3 x E` radical.

- fatal/nonfatal verdict

  Fatal for any unquotiented `K3 x E` solution claim.  Nonfatal for the
  quotient theorem: the Igusa denominator quotient remains the correct
  theorem-grade object.

- exact repair/heal theorem statement

  For each finite lower-set quotient `L`, let `G_{Aut,L}` be the
  automorphic Gram pairing induced by the denominator supertrace,
  orientation character, and Borcherds root pairing on the actual finite
  primitive Hall quotient.  Then the unquotiented positive Hall-BKM
  theorem holds if and only if `ker(G_{Aut,L})=0` for every `L`, and the
  kernels are compatible under the pro-transition maps.  The currently
  proved theorem is the radical quotient
  `CoHA/Rad_Aut ~= Uhat(g_Delta^+)`.

- local file anchors

  `chapters/theory/bps_positive_geometry_closure.tex:257-301`,
  `compute/lib/bps_positive_truncation.py:706-719`,
  `compute/lib/bps_positive_truncation.py:787-808`,
  `compute/lib/bps_positive_truncation.py:857-871`,
  `compute/tests/test_bps_positive_truncation.py:214-220`,
  `compute/tests/test_bps_positive_truncation.py:272-281`.

- primary/literature anchors if needed from existing bibliography or local notes

  Borcherds and Gritsenko product normalization:
  `bibliography/references.tex:325-326`,
  `bibliography/references.tex:313-314`.  Local Igusa separation:
  `notes/bps_positive_geometry_total_resolution_20260424/five_gate_resolution_20260424.md:176-260`.

- executable checks proposed or run

  Run: `k3e_unquotiented_radical_certificate()` returns
  `passed=True, exact=False`; the derived stack uses a different
  `exact=True` matrix.  Proposed: remove the toy matrix from the named
  `K3 x E` factor; keep it only in the unit test for linear algebra.
  Add a test asserting that the named raw `K3 x E` factor delegates to
  `k3e_unquotiented_radical_certificate()` or to a computed
  `G_{Aut,L}` source.

- remaining point-construction obligation

  Construct the actual finite automorphic Gram matrices from the finite
  primitive Hall quotient and prove zero kernel in a cofinal tower.

## Attack 5: hCS obstruction theorem conflicts with the twisted orientation branch

- claim attacked

  The hCS-to-Hall theorem states that the morphism exists iff the seven
  obstruction classes vanish, including the orientation square-root Cech
  class `o_or=0`.

- strongest failure mode

  The orientation oracle and tests explicitly allow a gerbe-twisted
  orientation output: a nonzero Cech 2-class can be retained by changing
  coefficients.  Requiring `o_or=0` absolutely contradicts the stronger
  orientation-output object.  The correct condition is not necessarily
  absolute triviality of the square-root gerbe; it is equality of the
  hCS and Hall orientation coefficient systems in the chosen twisted or
  untwisted target.

- fatal/nonfatal verdict

  Fatal if the theorem is read as excluding all twisted orientations.
  Nonfatal after healing the obstruction coordinate as a relative
  comparison class.

- exact repair/heal theorem statement

  In a fixed orientation output `o`, untwisted or gerbe-twisted, the
  oriented hCS-to-Hall morphism exists iff the relative seven-tuple
  vanishes:
  Maurer-Cartan defect, relative orientation-system mismatch, grading/Tate
  mismatch, Thom-Sebastiani associator defect, Ran disjoint-union defect,
  compact-support Beck-Chevalley defect, and completion incompatibility.
  The orientation coordinate is zero in the torsor of coefficient
  systems over `o`, not necessarily zero as an absolute Cech class.

- local file anchors

  `chapters/theory/bps_positive_geometry_closure.tex:305-342`,
  `compute/lib/bps_positive_truncation.py:129-181`,
  `compute/tests/test_bps_positive_truncation.py:78-90`,
  `compute/lib/bps_positive_truncation.py:750-770`,
  `compute/lib/bps_positive_truncation.py:880-892`.

- primary/literature anchors if needed from existing bibliography or local notes

  Local orientation oracle:
  `notes/bps_positive_geometry_total_resolution_20260424/agent_02_orientation_oracle.md`.
  Local hCS/Ran lane:
  `notes/bps_positive_geometry_total_resolution_20260424/agent_05_hcs_hall_dwr_ran.md`.

- executable checks proposed or run

  Run: `test_orientation_twisted_class_is_retained` passes and exhibits a
  retained nonzero orientation class.  Proposed: add a test that hCS
  obstruction certificates distinguish absolute orientation triviality
  from relative orientation compatibility with a twisted coefficient
  target.

- remaining point-construction obligation

  Compute the seven relative obstruction classes in the named compact CY3
  geometry and prove their compatibility in the completed Hall topology.

## Attack 6: hCS named zero fiber is forged by zero coordinates

- claim attacked

  The derived solution stack factor for hCS uses
  `obstruction_zero_certificate` with all seven coordinates set to zero
  and `exact=True`.

- strongest failure mode

  This bypasses `hcs_named_obstruction_certificate()`, which correctly
  has `exact=False`.  The code therefore proves the tautology
  "zero vector has zero obstruction" instead of computing the obstruction
  vector of any named compact CY3.

- fatal/nonfatal verdict

  Fatal for named hCS localization.  Nonfatal for the criterion theorem.

- exact repair/heal theorem statement

  The hCS named substack is the zero fiber of the seven-class obstruction
  map.  It has a point for a named CY3 iff the seven classes computed
  from that CY3's DWR/Ran Cech nerve vanish.  A formal zero vector is an
  admissible unit test for `obstruction_zero_certificate`, not a
  geometric solution.

- local file anchors

  `compute/lib/bps_positive_truncation.py:750-770`,
  `compute/lib/bps_positive_truncation.py:773-784`,
  `compute/lib/bps_positive_truncation.py:880-892`,
  `compute/tests/test_bps_positive_truncation.py:230-235`,
  `compute/tests/test_bps_positive_truncation.py:260-269`.

- primary/literature anchors if needed from existing bibliography or local notes

  Local hCS total obstruction list:
  `notes/bps_positive_geometry_total_resolution_20260424/seven_extension_resolution_20260424.md:256-307`.

- executable checks proposed or run

  Run: focused test file passes.  Proposed: add
  `test_hcs_named_factor_is_not_exact_until_classes_are_computed`.

- remaining point-construction obligation

  Compute the actual seven-class vector for the target compact CY3.

## Attack 7: theta basis theorem is conditional but notes overstate compact realization

- claim attacked

  The manuscript constructs intrinsic Hall theta elements under identity
  joint holonomy; the notes then say this is a genuine non-toric theta
  package for compact BMS chambers.

- strongest failure mode

  The executable theta check uses the rank-two `A_2` scattering witness,
  not a compact BMS chamber scattering diagram.  The theorem is valid as
  a conditional finite Hall-factorization theta package.  It is not an
  actual compact BMS theta basis until identity holonomies and
  transition compatibility are computed for that compact chamber.

- fatal/nonfatal verdict

  Nonfatal for the intrinsic Hall theta criterion.  Fatal only for the
  stronger claim that compact BMS theta bases have been constructed.

- exact repair/heal theorem statement

  For each finite lower-set quotient and base chamber, define
  `vartheta_p^{lambda,c}=Phi^{KS}_{b->c}(x_p)`.  If all retained joint
  holonomies in the actual chamber scattering diagram are identity, these
  elements are path-independent and form the intrinsic Hall theta
  package.  GHKK, GMN, and broken-line theta packages agree with it iff
  the comparison cocycle vanishes in every finite quotient and is
  compatible in the pro-limit.

- local file anchors

  `chapters/theory/bps_positive_geometry_closure.tex:344-388`,
  `compute/lib/bps_positive_truncation.py:722-747`,
  `notes/bps_positive_geometry_total_resolution_20260424/platonic_closure_20260424.md:168-201`,
  `notes/bps_positive_geometry_total_resolution_20260424/seven_extension_resolution_20260424.md:201-255`.

- primary/literature anchors if needed from existing bibliography or local notes

  Kontsevich-Soibelman wall crossing:
  `bibliography/references.tex:707-708`.  Local theta lane:
  `notes/bps_positive_geometry_total_resolution_20260424/agent_08_theta_enhancement.md`.

- executable checks proposed or run

  Run: `theta_comparison_certificate(_bound())` passes with
  `exact=False`.  Proposed: add chamber name to theta certificates; only
  `A2_rank2_test` may be exact for the present scattering check.

- remaining point-construction obligation

  Construct the actual compact chamber scattering diagram or Hall
  transport category and compute joint holonomies and comparison
  cocycles.

## Attack 8: `ProvedHere` corollary lacks a proof body

- claim attacked

  `cor:bps-positive-theta-comparison` is marked `ClaimStatusProvedHere`
  but is stated without a proof environment before the next section.

- strongest failure mode

  A ProvedHere claim without a proof body can evade the theorem registry
  while carrying a strong comparison statement.  The statement is
  plausible as a formal corollary, but the proof must name the comparison
  cocycle and show both directions.

- fatal/nonfatal verdict

  Fatal for manuscript proof hygiene.  Nonfatal mathematically once the
  two-line proof is inserted.

- exact repair/heal theorem statement

  Proof: a comparison package gives a second finite parallel-transport
  system.  The difference between the intrinsic Hall transport and the
  external transport is a Cech 1-cocycle with values in finite quantum
  torus automorphisms.  Vanishing of this cocycle gives equality of
  theta elements and multiplication constants; equality of packages makes
  the difference cocycle zero.  Compatibility with transition maps gives
  the completed statement.

- local file anchors

  `chapters/theory/bps_positive_geometry_closure.tex:382-390`.

- primary/literature anchors if needed from existing bibliography or local notes

  KS transport anchor: `bibliography/references.tex:707-708`.

- executable checks proposed or run

  Proposed: registry check that every `ClaimStatusProvedHere` theorem,
  proposition, lemma, or corollary in the new chapter is followed by a
  proof environment unless its environment is a definition.

- remaining point-construction obligation

  For each external package, construct the comparison cocycle in the
  actual chamber.

## Attack 9: finite-to-pro equivalences need Mittag-Leffler and separatedness

- claim attacked

  Several proofs pass from finite quotients to completed pro-objects by
  saying the completed object or radical is the inverse limit of finite
  objects.

- strongest failure mode

  "All finite quotients vanish" implies pro-vanishing only in a separated
  completion with compatible surjective transition maps, or after
  controlling derived `lim^1` terms.  The manuscript states these
  conclusions but does not name the needed ML/separatedness hypotheses.

- fatal/nonfatal verdict

  Fatal for raw unquotiented and completed solution-stack equivalences as
  written.  Nonfatal after adding explicit pro-exactness hypotheses.

- exact repair/heal theorem statement

  Let `{L_i}` be a cofinal tower of finite saturated Hall-lower subsets
  with surjective quotient maps, and suppose the Hall algebra,
  automorphic radical, theta transports, and obstruction complexes are
  complete and separated for the induced filtration.  Then a compatible
  pro-section lies in the zero fiber iff its image lies in the finite
  zero fiber for every `L_i`; the completed radical is the inverse limit
  of finite radicals; and no derived `lim^1` obstruction appears.

- local file anchors

  `chapters/theory/bps_positive_geometry_closure.tex:153-154`,
  `chapters/theory/bps_positive_geometry_closure.tex:298-300`,
  `chapters/theory/bps_positive_geometry_closure.tex:378-379`,
  `chapters/theory/bps_positive_geometry_closure.tex:580-583`,
  `notes/bps_positive_geometry_total_resolution_20260424/integration_spine.md:105-118`.

- primary/literature anchors if needed from existing bibliography or local notes

  Local finite-first compute lane:
  `notes/bps_positive_geometry_total_resolution_20260424/agent_09_compute_truncation_engine.md:12-59`.

- executable checks proposed or run

  Proposed: add transition-map tests between bounds `N=3` and `N=4`
  checking restriction compatibility for support, Hall multiplication,
  theta generators, and obstruction vectors.

- remaining point-construction obligation

  Prove the selected finite lower-set tower is cofinal, surjective,
  complete, and separated in each named compact chamber.

## Attack 10: the executable theorem overstates what the tests certify

- claim attacked

  The executable theorem says the oracle implements finite certificates
  for the residual derived solution stack and aggregate seven-lane
  resolution.  The tests assert all derived factors pass.

- strongest failure mode

  The tests currently verify that the code's placeholders are internally
  consistent.  They do not verify that the placeholders are geometric
  obstruction values.  In particular, `test_derived_solution_stack_factors`
  asserts every factor's obstruction vanishes, including factors whose
  certificates are explicitly `exact=False`.

- fatal/nonfatal verdict

  Fatal if read as computational evidence for named example solutions.
  Nonfatal if read as an executable schema for the residual zero-fiber
  architecture.

- exact repair/heal theorem statement

  The oracle proves the finite schema: exact arithmetic for support,
  orientation, Hall associativity, sector descent, toric collapse,
  conifold pentagon, rank-two KS scattering, and Igusa normalization
  checks.  It registers named residual lanes as certificates, radical
  quotients, comparison cocycles, or obstruction vectors.  It proves a
  named residual point only when the named obstruction vector is computed
  from that geometry and the certificate is exact.

- local file anchors

  `chapters/theory/bps_positive_geometry_closure.tex:390-426`,
  `compute/tests/test_bps_positive_truncation.py:198-320`,
  `compute/lib/bps_positive_truncation.py:897-956`.

- primary/literature anchors if needed from existing bibliography or local notes

  Worker 09's certificate schema:
  `notes/bps_positive_geometry_total_resolution_20260424/agent_09_compute_truncation_engine.md:983-1005`.

- executable checks proposed or run

  Run: focused tests pass.  Proposed: split tests into
  `schema_passes` and `named_point_realized`.  The latter must fail or be
  skipped with an explicit point-construction obligation until real
  obstruction vectors are supplied.

- remaining point-construction obligation

  Attach each residual factor to geometry-derived data rather than
  hardcoded zero values.

## Attack 11: Part VII placement creates a stale-status ambiguity

- claim attacked

  `main.tex` includes the new closure chapter and then immediately
  presents frontier obligations and structural residue.

- strongest failure mode

  The new chapter says the BPS positive geometry gap is closed at the
  finite-first source-object level and that the residual named problems
  are closed substacks.  The subsequent Part VII frontier text speaks of
  CY-A3 chain-level models for non-formal CY3s, including the quintic, as
  construction obligations.  This is not a direct contradiction, but
  without one sentence it is easy to read the old frontier table as
  reopening the just-typed residual lanes.

- fatal/nonfatal verdict

  Nonfatal.  It is a reader-facing coherence risk.

- exact repair/heal theorem statement

  Insert a transition sentence after the closure chapter: the following
  Part VII frontier table concerns classification-level and stage-two
  refinements after the chambered BPS positive geometry source object has
  been constructed; the quintic/Schoen/raw `K3 x E` issues are named
  closed substacks of the residual solution stack, not missing
  foundations.

- local file anchors

  `main.tex:1821-1858`,
  `chapters/theory/bps_positive_geometry_closure.tex:430-590`.

- primary/literature anchors if needed from existing bibliography or local notes

  Local seven-extension ledger:
  `notes/bps_positive_geometry_total_resolution_20260424/seven_extension_resolution_20260424.md:431-460`.

- executable checks proposed or run

  Proposed: add a simple `rg` hygiene check for "quintic" in Part VII
  after the closure chapter and classify each occurrence as either
  residual closed substack, classification frontier, or unrelated CY-A3
  chain-level obligation.

- remaining point-construction obligation

  None for the source object; point construction remains in the named
  substacks listed above.

## Final healed core

The strongest coherent resolution is:

```tex
data-realized Hall-admissible compact CY3 chamber
  + finite saturated Hall-lower tower
  + orientation output
  + motivic coefficient target
  + ML/separated completion
  =>
  chambered BPS positive geometry
  P^{BPS}_{sigma,S,o,T_eq}(X).
```

The toric effective positive geometry is the degenerate critical-quiver
specialization.  Compact non-toric source objects exist in the
Bayer-Macri-Stellari class after the Hall-admissibility and orientation
output are included.  The quintic, Schoen, raw `K3 x E`, external theta,
and named hCS problems are not vague gaps; they are named closed
substacks cut out by explicit obstruction maps.  They are not yet actual
points merely because the schema exists.

The compute layer must reflect exactly that:

```text
schema exactness != named point exactness.
```

The next proof-grade upgrade is to make every residual factor carry one
of three statuses in code:

```text
schema_exact,
geometric_vector_computed,
point_realized.
```

Only the third status may be used to say that a named residual problem is
solved as a point of `Sol^{BPS}`.
