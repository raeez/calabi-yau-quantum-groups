# Calabi-Yau Quantum Groups

**Volume III** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
by Raeez Lorgat.

Constructs the functor Phi: CY_d-Cat -> E_n-ChirAlg from Calabi-Yau categories to chiral algebras, proved for all d (CY-A_2 at d=2; CY-A_3 at d=3 via the infinity-categorical proof that HH^{-2}_{E_1}=0 and the space of E_3-liftings is contractible). The E_n level is dimension-dependent: E_inf at d=1, E_2 at d=2, E_1 at d>=3, with the braided E_2 structure at d>=3 constructed via the Drinfeld center Z(Rep^{E_1}(A)) — the right adjoint to the forgetful functor, not a categorified averaging map. The K3 Yangian Y(g_{K3}) has 24 generators, Mukai-signature (4,20) Serre relations, and degree-(24,24) structure function. Six independent constructions approach G(K3 x E); their conjectural convergence is CY-C.

## The Three Volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* | E_n-chiral algebras as algebraic-geometric objects on curves and configuration spaces |
| **II** | *A-infinity Chiral Algebras and 3D HT QFT* | Derived centres interpreted physically as 3d HT gauge theories |
| **III** | *Calabi-Yau Quantum Groups* (this volume) | Concrete CY quantum groups as examples of Vol I's abstract E_1-chiral quantum groups |

## The CY-to-Chiral Functor

The programme flow:

```
CY category C  -->  cyclic A-infinity  -->  Lie conformal algebra
                                                     |
                                            factorization envelope
                                                     |
                                                chiral target A_X
                                                     |
                                              bar complex B(A_X)
                                                /            \
                                   Euler product              shadow obstruction tower
                                        |                             |
                               BKM denominator identity      Vol I Theta_A
```

For d=2: the functor Phi_2 is proved (Theorem CY-A_2). For d=3: the infinity-categorical proof resolves the chain-level S^3-framing obstruction (Theorem CY-A_3). For toric CY3: a separate proved E_1 CoHA/chart-gluing package provides independent verification. The E_n-chiral Koszul duality (Theorem CY-B) is proved at d=3 via the Verdier spectral functor: E_1-Koszul on A, inducing E_2 on the Drinfeld center. CY-C (quantum group realization) and CY-D (modular characteristic at d>=3) remain conjectural/programme.

## Connection to Volumes I-II

| Input | Source | Role in Vol III |
|-------|--------|-----------------|
| Shadow obstruction tower Theta_A | Vol I, Theorem D + MC2 | Conjecturally = automorphic correction of BKM |
| E_1 ordered bar B^{ord}(A) | Vol II, Part II | Toric CY3: proved E_1 sector; general d=3 use remains conditional |
| Modular characteristic kappa(A) | Vol I, Theorem D | Real roots + Weyl vector of BKM algebra |
| R-matrix braiding | Vol II, Part III | Abstract E_1 -> E_2 lift via Drinfeld center; d=3 applications require the E_1 input |

## Seven-Part Structure

- **I. Foundations**: CY categories, cyclic A-infinity, Hochschild calculus
- **II. CY-to-Chiral Functor**: Construction of Phi, the [m_3,B^{(2)}] saga, kappa-spectrum
- **III. E_n Hierarchy and Chiral Quantum Groups**: E_1/E_2-chiral algebras, E_n factorization, quantum groups, Drinfeld center, braided factorization
- **IV. The K3 Yangian**: Phi(K3) explicit, abelian Yangian, K3 x E BKM, quantum toroidal, six routes to G(K3 x E)
- **V. CY Landscape**: toric CY3 CoHA, Fukaya, derived, matrix factorizations, quantum group reps
- **VI. Seven Faces of r_CY(z)**: bar-cobar bridge, modular Koszul bridge, CY holographic datum
- **VII. Frontiers**: geometric Langlands, nonabelian Yangian, ZTE, root of unity

## Status (2026-04-17)

| Component | Status |
|-----------|--------|
| CY-A (CY-to-chiral functor) | **Proved** at all d (CY-A_2 at d=2; CY-A_3 at d=3 via infinity-categorical framework) |
| CY-B (E_n-chiral Koszul duality) | **Proved** at d=3 via Verdier spectral functor; d-stratified scope documented |
| K3 Yangian Y(g_{K3}) | **Proved** (24 generators, Mukai signature (4,20), (24,24) structure function, pentagon-at-E_1 architecture) |
| Phi(K3) explicit | **Proved** (H_Muk, kappa_ch=2) |
| CoHA as E_1 sector (toric CY3) | **Proved** (CoHA(C^3) = Y^+, positive half of affine Yangian) |
| Drinfeld center E_1 -> E_2 | **Proved** (right adjoint to forgetful, explicit half-braiding sigma_A(z) construction) |
| CY-C (six routes convergence) | **Proved** at scalar kappa_BKM level via kappa_BKM(Phi_N) = c_N(0)/2 universal (Borcherds weight); generator-relation identification across routes remains CONJECTURAL |
| CY-D (dimension stratification) | **Proved**: thm:kappa-hodge-supertrace-identification for compact CY_d all d; explicit stratification across d in {1,2,3,4,5} |
| CY_4 p_1-twisted family | **Proved** (double current algebra with c(x,y) = <x∪y∪p_1(T_X),[X]>/24; K3 x K3 unobstructed E_4) |
| Langlands = Koszul | **Conjectural** |

| Metric | Value |
|--------|------:|
| Pages | ~820 |
| Parts | 7 (with Part openers and 3 reading paths) |
| Theory chapters | 16 |
| Example chapters | 15 (including CY-C six-routes + CY-D stratification + CoHA wall-crossing Platonic additions) |
| Connection chapters | 4 |
| Working notes | migrated into permanent notes/ workspace (60+ wave files) |
| Compute engines | ~600 (3 new: chain-to-matrix Pentagon descent, CY_4 p_1-twisted, non-simply-laced resurgent twist) |
| Compute tests | ~40,000 |
| Anti-patterns | AP-CY1-67 + AP150-AP187 + FM24-FM247 + Wave V49-V121 heal/attack cycle |
| HOT ZONE entries | HZ3-1 through HZ3-11 (Independent Verification Protocol added) |
| First-principles cache | 240+ entries covering 2026-04-16 reconstitution wave |
| Bibliography | 45+ bibitems (updated with Guay-Regelskis-Wendlandt, Francis-Gaitsgory, Hoefel-Livernet, and +15 others) |
| HZ-IV decorators installed | 26 / 315 ProvedHere (8.3%, up from 2/283 at baseline); tautological decorations 0; orphans 1 |

## Build

All compiled output goes to `out/`.

```bash
make fast                    # quick converging build → out/main.pdf
make                         # full build → out/
make release                 # full rebuild → out/ + iCloud
make test                    # compute test suite
make clean-builds            # remove /tmp/mkd-* isolated build directories
```

Each build runs in its own `/tmp/mkd-calabi-yau-quantum-groups-<NS>/`
directory, so parallel agents never clobber each other. Set
`MKD_BUILD_NS` for warm rebuilds across invocations:

```bash
export MKD_BUILD_NS="agent-$$"
make fast                         # warm on second call
```

Requires TeX Live 2024+ with pdflatex.

## Independent Verification Protocol

Every `\ClaimStatusProvedHere` theorem should be paired with a test module
decorated with `@independent_verification(claim, derived_from, verified_against, disjoint_rationale)`.
The decorator enforces token-level disjointness between the programme-internal
derivation and the external-source verification; tautological decoration fails
at import, not silently.

**Audit state (2026-04-17, post-rewrite-loop):** Vol III audit is **PASSing**
with zero tautological decorations and zero orphan entries. Coverage snapshot:
128/412 ProvedHere labels with installed IV (31.0%). 264 Conjectured/Conditional
+ 208 remark/definition/construction labels recognised as valid decoration
targets. Vol III has the highest IV coverage among the three volumes, reflecting
48 consecutive +1 ticks of systematic IV installation this rewrite-loop session
across the K3-Yangian Pentagon edge architecture, CY-D classification,
cy_to_chiral foundational corollaries, and the full Item 11b cross-volume
Universal Trace Identity bridging diagram.

**Full Item 11b cross-volume bridging diagram IV-complete:**
- Parent theorems: `thm:universal-trace-identity-k3-fibered` +
  `thm:universal-trace-identity-non-k3-fibered`.
- Three K3-fibered sub-constructions: Z-functoriality of Koszul reflections,
  supertrace-Trinity-centre collapse, Borcherds character lift.
- Three non-K3-fibered Bruinier-Funke sub-constructions: BF regularised
  functoriality, Eisenstein-cusp Trinity-supertrace commutation, BF product
  expansion at non-unimodular Λ.
- K3 × E base case: both sides equal κ_BKM = 5 via phi01_fourier theta-ratio
  + Igusa cusp form weight + M_24 Frame shape (three disjoint sources).

**Cross-volume audit state:** Vol I 166/2718 (6.1%) + Vol II 115/1469 (7.8%) +
Vol III 128/412 (31.0%) = 409 / 4599 total (8.9%). All three volumes PASS
simultaneously.

Make targets:
```
make verify-independence           # summary audit (no tautology / no orphan gate)
make verify-independence-verbose   # full list of uncovered claims
```

See `notes/INDEPENDENT_VERIFICATION.md` for the three-healing rubric
(find disjoint source / restrict scope / downgrade status) and
`compute/lib/independent_verification.py` for the decorator implementation.

## Recent Inscriptions and Audit (2026-04-17 wave)

The 2026-04-17 reconstitution wave inscribed Vol III's contribution to the
universal-trace-identity bridge, healed the CY-C pentagon stratification, and
propagated the wave-14 anchor cross-references throughout. Items added or
healed since the last README revision:

- **Seven-part rearchitecture realised losslessly** (commit d3063b9).
  Two-agent parallel audit confirmed all seven `\part{}` declarations at
  `main.tex:523, 583, 661, 748, 843, 939, 1007` with Part-openers all
  carrying substantive prose (35-63 lines each) rather than stubs. 22 of 26
  chapter assignments match the platonic-ideal proposal exactly; the four
  refinements are intentional content-org decisions improving on the April
  draft.

- **Show-don't-tell preface and Part-bridge installation** (commit e53be2a).
  Each Part-opener now closes with a forward-bridge paragraph to the next
  Part. Seven bridges installed. The preface was rewritten in
  construct-don't-narrate form: state the objects and arrows explicitly;
  defer narration to remarks.

- **CY-D dimension stratification** (`chapters/examples/cy_d_kappa_stratification.tex`,
  1,328 lines). Inscribes `thm:kappa-hodge-supertrace-identification`:
  `κ_ch(A_X) = Σ_q (-1)^q h^{0,q}(X)` Hodge-filtered supertrace,
  unconditional for compact CY_d, and `thm:kappa-stratification-by-d` with
  explicit values across d ∈ {1, 2, 3, 4, 5} (E: κ_ch = 0; K3: 2;
  abelian/bielliptic: 0; quintic/K3 × E/E^3: per family; CY_4 sextic: 2;
  CY_5 generic: 0). Local P^2 (d = 3) gives `κ_ch = 3/2` via
  `thm:local-p2-shadow`. Resolves the long-standing `κ = χ` confusion: the
  formula changes at odd d because Serre duality kills `χ(O_X)` when
  h^{1,0} > 0. Closes AP-CY34, AP-CY44.

- **Borcherds-weight universality** (`prop:bkm-weight-universal`).
  `κ_BKM = c_N(0)/2` proved universal for all K3-fibered Class A
  (8 diagonal Z/N orbifolds + STU model, N ∈ {1, 2, 3, 4, 6}; the N = 5
  Frame shape is exceptional, separately verified). Proof: K3 elliptic
  genus + orbifold averaging + Borcherds 1998 weight theorem. Does NOT
  depend on CY-A. For non-K3-fibered Class B (quintic, C^3, conifold,
  local P^2), `κ_BKM` is UNDEFINED; replacement invariants are
  `κ_BCOV = χ(X)/24` (BCOV 1994) and shadow depth (conditional on CY-A).
  The N = 1 K3 × E coincidence `κ_BKM = κ_ch + χ(O_fiber)` FAILS at N ≥ 2
  per `rem:bkm-decomposition-adversarial` (62 adversarial tests).

- **CY-C pentagon stratification healing** (commit cade61c). The notorious
  `κ_ch = 3 vs κ_BKM = 5` contradiction is resolved by the recognition that
  `κ_BKM` is stratified by GENERATOR RANK `ρ^{R_i}`, NOT by `κ_ch`. The
  universal stratification reads `{3, 12, 24}` against the route index, with
  `κ_ch = 0` route-independent (Hodge-supertrace invariant for K3 × E). The
  decomposition `κ_BKM = κ_ch + χ(O_fiber)` is the N = 1 K3 × E numerical
  coincidence. Manifest invariants (κ_cat, κ_fiber) are topological; only
  algebraization invariants (κ_ch, κ_BKM) depend on the chiral-algebra
  realisation.

- **Six routes to G(K3 × E) WITNESS framing**. Six different constructions
  (Borcherds lift, Mukai pairing, McKay quiver, MO instanton lift,
  factorisation homology, Costello 5d hCS) WITNESS the same `Φ_3(K3 × E)`
  output, NOT six applications of the Φ functor. Φ gives ONE output per
  category; the six routes are six distinct proofs of consistency that
  converge at the kappa-spectrum level. AP-CY57 construction-not-narration
  guard inscribed across the six-route discussion.

- **Universal Trace Identity bridge inscription** (Vol III side,
  `chapters/connections/bar_cobar_bridge.tex`). The cross-volume identity
  `κ_BKM(X) = K(Φ(X))/2` for K3-fibered Class A is inscribed as
  `conj:universal-trace-identity` mediated by the κ_ch Hodge supertrace. The
  Vol I side (`K(A) = -c_ghost(BRST(A))`) is the universal conductor; the
  Vol III side is the Borcherds weight specialised to K3-fibered Class A.
  Status: organising principle, conjectural at programme level, per-family
  verified across the 8 + STU diagonal Class A. Class B explicitly excluded;
  Class B uses `κ_BCOV = χ(X)/24` instead.

- **Beilinson adversarial swarm audit**
  (`notes/beilinson_swarm_audit_vol3_2026_04_17.md`). 33 chapters audited
  across the C1-C5 swarm bundles plus frame matter. 21 surgical fixes
  across 4 files. Critical finds: 17 bare-κ AP113 residuals all fixed
  (HZ3-2 zero tolerance now green); 4 broken cross-refs
  `cor:cy-c-pentagon-colimit` → `prop:` retargeted at 4 callsites
  (main.tex, preface.tex, introduction.tex). Convention clash discovered:
  frontier sections used `\kappa` for the affine KM level (Feigin-Frenkel
  convention), conflicting with the Vol III invariant convention; surgically
  converted to `k` matching `V_k(\fg)` from landscape_census. AP160, AP161,
  AP-CY54, AP-CY7, AP-CY8, AP182, AP185 all clean. Six-routes WITNESS
  framing + ρ^{R_i} pentagon framing verified Beilinson-rectified.
  Residual flagged: 102 em-dash hits across 16 files (deferred to dedicated
  sweep — see Vol II elite-prose kickstart for the launch protocol).

- **Six Vol III stub chapter developments** (drinfeld_center +89 lines;
  braided_factorization expanded; derived_categories_cy +89; matrix_factorizations
  +187; fukaya_categories +465; quantum_group_reps +582). drinfeld_center now
  carries the categorified-averaging-via-right-adjoint construction
  (AP-CY54), the BZFN identification, the E_n circle, and
  `conj:v3-drinfeld-center-equals-bulk` with three honest obstructions.
  matrix_factorizations carries Knörrer periodicity in detail, the quintic
  LG model and chiral matching, the full ADE table stabilised,
  Hochschild residue → R-matrix data, and a mirror-LG preview.
  quantum_group_reps carries AP170 two-Yangian-defs discipline,
  AP159 four-Yangian-types discipline, KL realisation at d = 2, and a
  CY-C honest accounting with 7 enumerated sub-cases.

- **Chriss-Ginzburg rectification harness**
  (`.agents/skills/chriss-ginzburg-rectify/`,
  `.claude/commands/chriss-ginzburg-rectify.md`). 616 lines of harness
  configuration (smaller than Vol II's 1,524-line set because Vol III's
  chunk-by-chunk rectification was started under the canonical command
  directly, omitting v1 retention and Vol I-targeted variant). Repo-local;
  consumed by the Vol III bundles E9-E10 of the elite-prose rectification
  swarm queued by the Vol I `notes/elite_prose_rectification_swarm_kickstart.md`.

- **working_notes.pdf snapshot** (`out/working_notes.pdf`, 851 KB,
  build 2026-04-17 14:07). Author-side companion artifact tracked under the
  `!out/*.pdf` unignore rule. Reflects post-2026-04-17 state including
  seven-part rearchitecture, Hodge-supertrace stratification, Borcherds
  universality, and CY-C pentagon healing. Regenerable by
  `make working-notes` from `working_notes.tex`; cross-machine reference
  for the most recent reconstitution state without requiring full rebuild.

Forward direction. Two systemic debts surviving the wave:

(a) Em-dash sweep. 102 ASCII `---` instances flagged across 16 chapter
files (cy_to_chiral, modular_koszul_bridge, drinfeld_center, several
Part IV K3 chapters); plus 43 U+2014 Unicode em-dashes (k3_yangian_chapter
holds 26 of these alone) surfaced as a follow-up scope by the Vol III em-dash
sweep agent. Each requires contextual rewrite (hyphen for compound nouns;
parens or commas for parentheticals; colon or semicolon for strong pauses;
sentence split for amplification). Dedicated sweep, 1-2 sessions; the
table-cell, math-subscript, and section-break placeholders preserved
intact (per Vol I CLAUDE.md HZ-10 protocol).

(b) Line-by-line elite-prose rectification programme queued by the Vol I
`notes/elite_prose_rectification_swarm_kickstart.md`. Vol III owns
bundles E9 (frame + theory + first-batch examples) and E10 (second-batch
examples + connections + frontier). Confidence interval on completion:
4-6 sessions, smaller than Vol II's because Vol III is ~700 pages versus
Vol II's ~1,950 pages.
