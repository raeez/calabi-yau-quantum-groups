# Wave V82 --- Adversarial Attack + Foundational Heal of V67-CB-Universal
## Does the boundary-data-forced mock-modular receptacle $\mathcal{M}^X$ exist *a priori*, or is its construction part of the conjecture?

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** V82, Russian-school
attack-then-heal (Beilinson dialectic; Chriss--Ginzburg discipline; Etingof--
Kazhdan rigour). Phase 1 attacks V67-CB-Universal's receptacle existence
claim from five angles; Phase 2 inscribes the survivor in its strongest
Platonic form. AP-CY61 governs every step (ghost theorem extraction
mandatory); AP-CY57 (construction not narration); HZ3-12 (first-principles
investigation).

**Posture.** No `.tex` edits, no `CLAUDE.md` updates, no commits, no test
runs, no manuscript edits. Read-only sandbox memorandum.

**Companion waves.** V67 (`wave_V67_attack_heal_V62_BCOV_MNOP_independence.md`)
established the universal Class-B residual; V62
(`wave_class_B_alien_derivation_quintic_LP2.md`) named the two boundary-data
specialisations; V55 (`wave_frontier_pentagon_E1_non_K3.md`) classified
non-K3 inputs into Class B / B0.

---

## §1. The V67-CB-Universal claim restated

The load-bearing statement of V67 is:

> **Conjecture (V67-CB-Universal).** Let $X$ be any Class-B CY3 input
> (non-K3-fibred, shadow class M, non-super-trace-vanishing). Let
> $Z^X(g_s, t)$ be its refined topological string partition function.
> Then there exists a mock-modular completion $\widehat{Z}^X$ in
> the **boundary-data-forced receptacle** $\mathcal{M}^X$ such that
> (a) $\widehat{Z}^X$ transforms modularly in $\mathcal{M}^X$, and
> (b) the shadow $\partial_{\bar\tau}\widehat{Z}^X$ vanishes identically.

V67 §4.3 supplies the dictionary
$$
X \;\longmapsto\; \mathcal{M}^X
$$
with three rows:

1. Compact CY3, $h^{1,1}=1$: $\mathcal{M}^X = M^!_w(\Gamma_0(N))$.
2. Compact CY3, $h^{1,1}>1$: $\mathcal{M}^X$ = multi-variable mock Jacobi
   for the Kähler cone.
3. Non-compact toric CY3: $\mathcal{M}^X$ = mock Jacobi form for the toric
   BPS algebra (e.g. mock $W_3$-Jacobi $(1,1)$ for $\mathrm{LP}^2$).

Quintic specialisation: $\mathcal{M}^Q = M^!_{3/2}(\Gamma_0(5))$.
$\mathrm{LP}^2$ specialisation: $\mathcal{M}^{\mathrm{LP}^2} = J^{\mathrm{mock},W_3}_{0,(1,1)}$.

V67 calls the receptacle "boundary-data-forced", suggesting that once the
boundary data of the refined-HAE (constant-map for compact, equivariant for
non-compact toric) is specified, the receptacle is *mechanically determined*.
This wording carries the strong implicature of a priori existence: pick $X$,
read off the receptacle.

The load-bearing claim under attack is the existence-and-construction claim:
**that $\mathcal{M}^X$ exists as a well-defined object before $\widehat{Z}^X$
is constructed, and that "boundary-data-forced" is mechanically deterministic
rather than itself part of the conjecture.**

---

## §2. ATTACK (5 angles)

### Attack 1. The space $M^!_{3/2}(\Gamma_0(5))$ exists, but does NOT a priori contain $\widehat Z^Q$

**The attack.** The space $M^!_{3/2}(\Gamma_0(5))$ of weakly-holomorphic
weight-$3/2$ modular forms on $\Gamma_0(5)$ is a well-defined countable-
dimensional vector space; this is classical (Kohnen--Zagier, Bruinier--Funke).
Its dimension and bases at low weight are computable. So the *space* exists
a priori.

But "existence of the receptacle" is NOT the same as "existence of the
mock-modular completion living in that receptacle". The conjecture
V67-CB-Universal asserts that the GV-weighted generating series
$$
f^{\mathrm{quintic}}(\tau) \;=\; \sum_{n\ge -N_0} K_1^{\mathrm{quintic}}\,
\mathrm{GV}_{0,n}^{\mathrm{quintic}}\, q^n
$$
admits a Zwegers completion $\widehat f^{\mathrm{quintic}} \in
\widehat M^!_{3/2}(\Gamma_0(5))$ (the space of harmonic Maass forms of
weight $3/2$ extending $M^!_{3/2}(\Gamma_0(5))$).

The space of weight-$3/2$ harmonic Maass forms on $\Gamma_0(5)$ is *strictly
larger* than $M^!_{3/2}(\Gamma_0(5))$: it contains the holomorphic part
plus an Eichler integral of a weight-$1/2$ shadow on $\Gamma_0(5)$. Not
every Fourier series with bounded principal part qualifies as the
holomorphic part of a harmonic Maass form: the Bruinier--Funke
$\xi$-operator
$$
\xi_k\colon H_k(\Gamma) \;\longrightarrow\; S_{2-k}(\Gamma),
\qquad
\xi_k = 2 i\, y^k\, \overline{\partial_{\bar\tau}}
$$
is *surjective* onto the cusp forms, but a generic GV-weighted series is
NOT the image of $\xi_{3/2}$ applied to any harmonic Maass form.

So the V67 phrase "receptacle exists a priori" elides a critical distinction:
- The ambient space $\widehat M^!_{3/2}(\Gamma_0(5))$ exists a priori
  (Bruinier--Funke 2004).
- The specific Maass extension of $f^{\mathrm{quintic}}$ existing INSIDE
  this space is the CONJECTURE, not a consequence of receptacle existence.
- Equivalently: the receptacle is a vector space with infinitely many
  weight-$3/2$ Maass forms, but the conjecture asserts that
  $f^{\mathrm{quintic}}$ is the holomorphic part of one of them. This
  selection is not automatic.

**Ghost theorem extraction (AP-CY61 a/b/c).**
- (a) RIGHT: V67 correctly identifies that $M^!_{3/2}(\Gamma_0(5))$ and its
  Maass extension are well-defined classical spaces; their existence is
  proved in the modular forms literature.
- (b) WRONG: V67 conflates "existence of the ambient space" with "membership
  of $f^{\mathrm{quintic}}$ in that space's Maass extension". The receptacle
  is a vector space; the conjecture is that $f^{\mathrm{quintic}}$ is the
  holomorphic part of a specific harmonic Maass form. Existence of the
  space does NOT imply existence of the completion.
- (c) CORRECT: Two-step structure. **Step (i) (proved):** the ambient space
  $\widehat M^!_{3/2}(\Gamma_0(5))$ of weight-$3/2$ harmonic Maass forms
  on $\Gamma_0(5)$ exists, classically constructed. **Step (ii) (conjecture):**
  the specific GV-weighted series $f^{\mathrm{quintic}}$ is the holomorphic
  part of an element of $\widehat M^!_{3/2}(\Gamma_0(5))$. Step (ii) is
  the actual content of V67-CB-Universal at the quintic specialisation.

**Verdict on Attack 1.** The receptacle ambient space exists a priori; the
specific completion's existence inside that space is the conjecture. V67's
"boundary-data-forced" phrasing collapses these two distinct claims and
must be split.

### Attack 2. Selection conditions are not specified by V67

**The attack.** Even granted that $\mathcal{M}^Q = \widehat M^!_{3/2}(\Gamma_0(5))$
contains a candidate Maass extension of $f^{\mathrm{quintic}}$, V67 does
NOT specify the selection conditions that pick out THE candidate. The
extension is unique only after additional data are fixed:

- **Principal part at all cusps.** A weight-$3/2$ harmonic Maass form on
  $\Gamma_0(5)$ has principal parts at the four cusps $\infty, 0, 1/5,
  1/(5\!\cdot\!\text{neg})$ ... (number of cusps depends on the precise
  index of $\Gamma_0(5)$ in $\mathrm{SL}_2(\mathbb{Z})$). Bruinier--Funke
  Theorem 3.7 says the principal part at each cusp is needed to specify
  the form uniquely. V67 specifies the principal part only at $i\infty$
  via $K_1^{\mathrm{quintic}}\cdot\mathrm{GV}_{0,n}^{\mathrm{quintic}}$.
- **Multiplier system.** The weight $3/2$ is half-integral, so the form
  carries a multiplier system (theta multiplier or its twist). The
  Picard--Fuchs monodromy of the quintic singles out $\Gamma_1(5)\subset
  \Gamma_0(5)$ as the actual modular group; the lift to $\Gamma_0(5)$ by
  twisting requires a specific character which V67 does not specify.
- **Shadow uniqueness.** The shadow $g^{\mathrm{quintic}}\in S_{1/2}(\Gamma_0(5))$
  (cusp forms of weight $1/2$) is a specific element of a
  finite-dimensional space; V67 conjectures $g^{\mathrm{quintic}}\equiv 0$
  but does not specify the projection that produces $g^{\mathrm{quintic}}$
  before the conjectural vanishing is invoked.
- **Boundary growth at cusps other than $i\infty$.** V67 specifies the
  $q$-expansion at $i\infty$ but not the behaviour at the other cusps
  of $\Gamma_0(5)$. A modular form on $\Gamma_0(5)$ is determined by its
  expansions at all cusps simultaneously.

So "boundary-data-forced" must be unpacked: the boundary data of the refined
HAE (Faber--Pandharipande constant-map for $X=Q$) does not directly determine
the four cuspidal principal parts of the half-integral-weight Maass form.
The map "HAE boundary data $\to$ principal parts at all cusps" is itself a
non-trivial conjecture, not a mechanical derivation.

**Ghost theorem extraction.**
- (a) RIGHT: V67 correctly identifies that the holomorphic principal part
  at $i\infty$ is determined by the GV invariants and Stokes constant.
- (b) WRONG: V67 does not specify principal parts at the other cusps,
  multiplier system, or shadow projection. The receptacle is not pinned
  down by the data V67 provides.
- (c) CORRECT: Selection conditions for the receptacle Maass form $\widehat
  f^{\mathrm{quintic}}\in\widehat M^!_{3/2}(\Gamma_0(5))$ require: (i)
  principal parts at all cusps of $\Gamma_0(5)$, (ii) explicit theta
  multiplier matched to Picard--Fuchs monodromy lift, (iii) explicit shadow
  $g^{\mathrm{quintic}}\in S_{1/2}(\Gamma_0(5))$. The cuspidal data at
  cusps other than $i\infty$ are conjecturally given by Stokes
  discontinuities at OTHER instanton actions, but these are
  not enumerated in V67.

**Verdict on Attack 2.** The "boundary-data-forced" map is a non-trivial
auxiliary conjecture. V67 underspecified the selection data; the receptacle
is at most a vector space, and the candidate completion inside it requires
data V67 omitted.

### Attack 3. Uniqueness of the receptacle is not established

**The attack.** V67 §4.3 presents the dictionary $X\mapsto\mathcal{M}^X$ as
a function with a single output. But for the quintic, multiple receptacles
fit the V67 ansatz:

- **Weight ambiguity.** Weight $3/2$ comes from "Eichler integration of the
  weight-$2$ Yukawa coupling lifted to a weight-$1/2$ Mukai character".
  But the quintic has a $5$-fold Mukai symmetry whose Eichler lift could
  produce weight $3/2 = 2 - 1/2$ OR weight $5/2 = 2 + 1/2$ depending on
  whether one twists with the inverse Mukai character. Both are weight-
  half-integral receptacles compatible with the Picard--Fuchs monodromy.
- **Level ambiguity.** $\Gamma_0(5)$ vs $\Gamma_1(5)$. Picard--Fuchs
  acts faithfully on $\Gamma_1(5)$; lifting to $\Gamma_0(5)$ adds a
  character. Both are admissible levels; V67 picks $\Gamma_0(5)$ but
  does not eliminate $\Gamma_1(5)$.
- **Subgroup ambiguity.** $\Gamma_0(5)$ vs the Atkin--Lehner extension
  $\Gamma_0(5)^+$ (adjoining the Fricke involution $\tau\mapsto -1/(5\tau)$).
  CY mirror symmetry typically respects Fricke involution, suggesting
  $\Gamma_0(5)^+$ might be the "true" receptacle.
- **Plus-space ambiguity.** Kohnen plus-space $M^{!,+}_{3/2}(\Gamma_0(5))$
  (forms whose Fourier coefficients vanish unless $n\equiv 0,1\pmod 4$)
  vs full $M^!_{3/2}(\Gamma_0(5))$. Shimura correspondence picks plus-space.

So the receptacle is at most determined up to a 2-dimensional grid of
ambiguities (weight $\{3/2,5/2\}$ × level $\{\Gamma_0(5),\Gamma_1(5),
\Gamma_0(5)^+\}$ × plus-or-not). Without an additional pinning principle,
$\mathcal{M}^Q$ is not unique.

For local $\mathbb{P}^2$ the analogous issue arises in mock $W_3$-Jacobi:
weight $0$ vs $-1$, indices $(1,1)$ vs $(1,2)$ vs $(2,1)$ depending on the
$W_3$ embedding into $U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)$, and
plus-space Bringmann--Folsom--Kane refinement.

**Ghost theorem extraction.**
- (a) RIGHT: V67 correctly identifies a *family* of receptacles compatible
  with the boundary data.
- (b) WRONG: V67 picks one receptacle from this family
  (weight $3/2$, level $\Gamma_0(5)$) without justifying the elimination
  of competitors. Uniqueness is asserted, not proved.
- (c) CORRECT: The receptacle dictionary $X\mapsto\mathcal{M}^X$ is at most
  a *multi-valued* map; V67 must be supplemented by a pinning principle
  (e.g., minimality of weight, maximality of multiplier kernel, or
  representation-theoretic match to the chiral algebra $A^X$) to single
  out a unique receptacle. Without this pinning principle, $\mathcal{M}^X$
  is well-defined only as a finite set, not as a single object.

**Verdict on Attack 3.** V67's receptacle map is multi-valued at the
quintic. The single-valued statement "$\mathcal{M}^Q = M^!_{3/2}(\Gamma_0(5))$"
is a CHOICE within the admissible set; V67 owes a uniqueness argument.

### Attack 4. Compact vs non-compact receptacles are NOT instances of one universal type

**The attack.** V67 claims a unified compact/non-compact framework where
the receptacle differs only in "boundary data". But the receptacles
$M^!_{3/2}(\Gamma_0(5))$ (classical scalar mock-modular form) and
$J^{\mathrm{mock},W_3}_{0,(1,1)}$ (rank-2 mock Jacobi form for a
$W$-algebra) are GENUINELY DIFFERENT mathematical objects:

- $M^!_{3/2}(\Gamma_0(5))$ is a vector space of scalar functions on the
  upper half-plane, transforming under a 1-dimensional representation
  (multiplier) of $\Gamma_0(5)$.
- $J^{\mathrm{mock},W_3}_{0,(1,1)}$ is a vector space of bivariate functions
  $\phi(\tau, z_1, z_2)$ transforming under a 2-dimensional representation
  of $\mathrm{SL}_2(\mathbb{Z})\ltimes\mathbb{Z}^2$ via the Jacobi action.

There is no "unified receptacle theory" that contains both as
specialisations of a single ambient object. V67's prior universal
conjecture (one conjecture, two specialisations, per V67 §4.1) presumes
such a unifying ambient theory, but the modular-forms literature has no
such unified theory connecting scalar half-integral-weight mock theta
functions and rank-$n$ mock Jacobi forms for $W$-algebras.

The closest unification would be the Eichler--Zagier--Skoruppa
*Jacobi-of-rank-zero* construction (where a scalar mock theta is realised
as a Jacobi form in $0$ elliptic variables), or its inverse, the
*theta-decomposition* of a Jacobi form into vector-valued mock theta
components. But this connects scalar mock theta to *trivial-rank*
Jacobi, not to rank-$n$ mock Jacobi for $W$-algebras.

So the V67 dichotomy "compact $\Rightarrow$ classical mock theta;
non-compact toric $\Rightarrow$ mock $W_n$-Jacobi" presents two genuinely
different categorical types (scalar vs vector-valued; trivial Jacobi
index vs rank-$n$ Jacobi index) as instances of one universal receptacle
type. This is a category error.

**Ghost theorem extraction.**
- (a) RIGHT: V67 correctly identifies that both compact and non-compact
  cases require *some* mock-modular receptacle, and that the receptacles
  are genuinely two.
- (b) WRONG: V67 claims these two receptacles are instances of one
  universal receptacle type ("boundary-data-forced from a single
  conjecture"). They are not: scalar half-integral mock theta and rank-2
  mock Jacobi for $W_3$ are different mathematical species, not
  specialisations of a common type.
- (c) CORRECT: Two-tier structure. **Tier 1 (universal residual):** the
  alien-derivation cocycle $\xi(A^X)\in H^2$ vanishes. This statement
  IS universal, independent of the receptacle. **Tier 2
  (input-dependent):** the *witness* of $\xi(A^X) = 0$ is a mock-modular
  completion in a receptacle whose mathematical type depends on the
  representation theory of $A^X$ (scalar mock theta for compact
  rank-1 monodromy; rank-$n$ mock Jacobi for non-compact toric with
  $W_n$-symmetry; possibly other types for inputs not in V67's
  three-row dictionary). The Tier-1 conjecture is one; the Tier-2
  receptacle dictionary is itself a conjectural family of constructions,
  not a single universal type.

**Verdict on Attack 4.** V67 conflates "one universal residual" (correct,
inherited from V67 attack-on-V62) with "one universal receptacle type"
(incorrect: receptacles are genuinely different mathematical species).
The healed structure is a two-tier conjecture with a universal Tier 1
and a multi-type Tier 2.

### Attack 5. Hidden CY-A_3 chain-level dependency

**The attack.** V67 names $\mathcal{M}^X$ as "boundary-data-forced" without
specifying what "the boundary data of $X$" means at the level of inputs to
the conjecture. Tracing back: the boundary data of the refined HAE for $X$
is determined by the *chiral algebra* $A^X = \Phi_3(D^b\mathrm{Coh}(X))$
through its representation theory (which determines the Yukawa coupling
$C_{ijk}^X$, the conjugate Yukawa coupling $\bar C^{ij,X}$, and the
boundary-data term).

But CY-A_3 is PROVED only in the $\infty$-categorical framework
(thm:derived-framing-obstruction). At the *chain level*, $A^X$ for a
generic non-K3 Class-B input $X$ (quintic, conifold, $\mathrm{LP}^2$,
banana) is NOT explicitly constructed: the inf-cat existence proof
shows that a chain-level $A^X$ EXISTS in the homotopy category, but
does not produce it as a concrete cdga or vertex algebra one can read
off the Yukawa coupling from.

So V67's "boundary-data-forced" inherits the chain-level CY-A_3
conditionality:
$$
\mathcal{M}^X \text{ specified by } A^X \stackrel{\text{CY-A}_3}{\Longleftarrow}
\Phi_3(D^b\mathrm{Coh}(X)) \text{ at chain level}.
$$

The chain-level $A^X$ for non-K3 Class-B inputs is the load-bearing
unstated assumption. Without it, the boundary data of the refined HAE
cannot be read off the chiral side, and the receptacle dictionary loses
its computability claim.

This is a textbook AP-CY11 violation (conditional propagation): V67
states the receptacle conjecture without flagging the CY-A_3 chain-level
dependency. Per HZ3-3 decision tree:
$$
\text{Q: Does V67-CB-Universal's receptacle map depend on chain-level }A^X?
\quad
\text{A: YES (via boundary-data extraction)}.
$$
Therefore V67-CB-Universal carries chain-level CY-A_3 conditionality, even
though the inf-cat CY-A_3 is proved.

**Ghost theorem extraction.**
- (a) RIGHT: V67 correctly identifies that the receptacle is determined by
  the input $X$ and the geometry of the refined HAE.
- (b) WRONG: V67 does not flag that "input determines receptacle" routes
  through the chiral algebra $A^X$, which is only inf-cat-existing for
  non-K3 Class-B $X$. The chain-level boundary-data extraction is
  conjectural.
- (c) CORRECT: The receptacle dictionary $X\mapsto\mathcal{M}^X$ requires
  chain-level $A^X$ (not just inf-cat $A^X$) to be computable. For Class-B
  inputs not yet endowed with explicit chain-level chiral algebraisation,
  the receptacle dictionary is conjecturally determined; V67-CB-Universal
  is therefore CONDITIONAL on chain-level CY-A_3 for non-K3 inputs.

**Verdict on Attack 5.** V67-CB-Universal inherits chain-level CY-A_3
conditionality through the receptacle dictionary. This must be flagged
as `\ClaimStatusConditional` per HZ3-3, with the dependency chain
"V67-CB-Universal $\Rightarrow$ receptacle map $\Rightarrow$ chain-level
$A^X$ $\Rightarrow$ CY-A_3 chain-level for Class-B inputs (currently
inf-cat only)" stated in the body.

---

## §3. WHAT SURVIVES

After all five attacks, the surviving core is:

**S1 (existence vs membership).** The ambient receptacle space (e.g.
$\widehat M^!_{3/2}(\Gamma_0(5))$ of harmonic Maass forms) exists a priori
as a classical modular-forms object (Bruinier--Funke). The conjectural
content is the membership of the specific GV-weighted series
$f^{\mathrm{quintic}}$ in this ambient space. V67 conflates these two
distinct claims; healing requires explicit separation.

**S2 (selection conditions).** V67 underspecifies the selection data
needed to pin $\widehat f^{\mathrm{quintic}}$ inside $\widehat
M^!_{3/2}(\Gamma_0(5))$: principal parts at all cusps, multiplier system,
shadow projection. These are auxiliary conjectural data, not consequences
of "boundary-data-forced".

**S3 (uniqueness of receptacle).** V67 picks one receptacle from a
$2\times 3\times 2 = 12$-element grid of admissible candidates without
justification. A pinning principle (e.g., minimal weight + Fricke-fixed
+ Kohnen plus-space) must be added to make the receptacle unique.

**S4 (compact vs non-compact = different mathematical types).** Scalar
mock theta and rank-$n$ mock Jacobi for $W$-algebras are genuinely
different species, not specialisations of one universal receptacle type.
V67's "two boundary-data specialisations of one universal conjecture"
is correct at the level of the universal residual ($\xi(A^X) = 0$) but
NOT at the level of the witness (the receptacle).

**S5 (CY-A_3 chain-level conditionality).** The receptacle dictionary
$X\mapsto\mathcal{M}^X$ is conjecturally determined by chain-level $A^X$,
which is only inf-cat-proved for Class-B inputs. V67-CB-Universal must
carry the conditional flag.

---

## §4. FOUNDATIONAL HEAL — V82-CB-Universal-Healed

The healed Platonic ideal is a TWO-TIER conjecture with explicit
existence-construction separation, an explicit pinning principle, and an
explicit conditional flag.

### 4.1 Tier 1 (universal residual, conditional on chain-level CY-A_3)

**Conjecture (V82-CB-Universal Tier 1, $\ClaimStatusConditional$).** *Let
$X$ be any Class-B CY3 input. Conditional on chain-level CY-A_3 producing
an explicit chiral algebra $A^X = \Phi_3(D^b\mathrm{Coh}(X))$, the
alien-derivation cocycle*
$$
\xi(A^X) \;=\; \sum_\alpha K_\alpha^X\, e^{-S_\alpha^X/g_s}\,
\Delta_{S_\alpha^X}\,\widehat Z^X
\;\in\; H^2(\mathrm{SC}^{\mathrm{ch,top}};\mathrm{aut})
$$
*vanishes in cohomology, where $\{S_\alpha^X\}$ is the spectrum of instanton
actions of the spectral curve $\Sigma^X$.*

This is the universal residual. It is INPUT-INDEPENDENT in form
(same cocycle structure for all Class-B $X$); INPUT-DEPENDENT in data
(spectrum and Stokes constants depend on $X$).

### 4.2 Tier 2 (witness-and-receptacle, multi-type and conjectural)

**Conjecture (V82-CB-Universal Tier 2, $\ClaimStatusConditional$).** *The
witness of $\xi(A^X) = 0$ is a mock-modular completion $\widehat Z^X$
constructed in a receptacle $\mathcal{M}^X$, where $\mathcal{M}^X$ is
selected from the admissible family*
$$
\mathfrak{A}^X \;=\; \bigl\{\mathcal{M}^X_\alpha\bigr\}_{\alpha\in I^X}
$$
*by the **representation-theoretic pinning principle** (RTP):*

1. **Weight pinning.** $w(\mathcal{M}^X)$ = minimum weight compatible with
   Eichler-lifted Yukawa coupling.
2. **Group pinning.** $\Gamma(\mathcal{M}^X)$ = stabiliser of the
   Picard--Fuchs system on the Greene--Plesser orbifold $\widetilde X$,
   intersected with the Fricke-involution-fixed subgroup when CY mirror
   symmetry respects Fricke.
3. **Plus-space pinning.** When $w$ is half-integral, $\mathcal{M}^X$ is
   the Kohnen plus-space.
4. **Multi-variable type pinning.** $\mathcal{M}^X$ is scalar (Jacobi
   index 0) when $A^X$ has rank-1 charge lattice; rank-$n$ Jacobi
   ($n = $ rank of charge lattice) when $A^X$ has rank-$n$ charge lattice;
   $W$-Jacobi when $A^X$ admits $W$-algebra symmetry.

*The receptacle ambient space $\mathcal{M}^X$ exists a priori (classical
modular forms / mock Jacobi forms / $W$-Jacobi forms literature). The
conjectural content of Tier 2 is that the GV-weighted (compact) or
refined-GV-weighted (non-compact toric) generating series is the
holomorphic part of an element of $\widehat{\mathcal{M}}^X$ (the harmonic
extension of $\mathcal{M}^X$).*

### 4.3 Existence-vs-construction taxonomy

The V82 healing makes precise:

| Object | Existence status | Construction status |
|---|---|---|
| Ambient receptacle space $\mathcal{M}^X$ | A PRIORI (modular forms literature) | Classical, computable. |
| Harmonic extension $\widehat{\mathcal{M}}^X$ | A PRIORI (Bruinier--Funke) | Classical, computable. |
| Specific completion $\widehat Z^X \in \widehat{\mathcal{M}}^X$ | CONJECTURAL | Conditional on Tier 2 pinning; conditional on chain-level $A^X$ via Tier 1. |
| Pinning principle RTP selecting $\mathcal{M}^X$ | CONJECTURAL | Currently a 4-clause heuristic; Vol III research direction to prove RTP uniqueness. |
| Boundary-data $\to$ receptacle map | CONJECTURAL | Conditional on chain-level $A^X$ producing computable boundary data. |

The V67 phrasing "boundary-data-forced receptacle" is replaced by:
"receptacle pinned by the four-clause representation-theoretic pinning
principle RTP, with chain-level $A^X$ producing the input data; existence
of the ambient space is a priori, existence of the specific completion is
conjectural".

### 4.4 Quintic specialisation (V82-healed)

**Receptacle (a priori).** $\mathcal{M}^Q = M^{!,+}_{3/2}(\Gamma_0(5)^+)$:
weakly-holomorphic weight-$3/2$ Kohnen plus-space on the Fricke-extended
group $\Gamma_0(5)^+ = \Gamma_0(5)\cup w_5\Gamma_0(5)$ where $w_5\colon
\tau\mapsto -1/(5\tau)$. Selected from $\mathfrak{A}^Q = \{(w,\Gamma,\pm)
: w\in\{3/2,5/2\}, \Gamma\in\{\Gamma_0(5),\Gamma_1(5),\Gamma_0(5)^+\},
\pm\in\{\text{plus},\text{full}\}\}$ via RTP clauses:
- W-pin: $w = 3/2$ (minimum half-integral weight from Eichler lift of
  weight-2 Yukawa coupling).
- G-pin: $\Gamma = \Gamma_0(5)^+$ (Fricke-extended; CY mirror symmetry
  respects Fricke for Fermat quintic).
- P-pin: Kohnen plus-space (Shimura correspondence to weight-2 cusp
  forms on $\Gamma_0(5)^+$).
- T-pin: scalar (rank-1 charge lattice for $h^{1,1}(Q) = 1$).

**Conjectural completion.** The GV-weighted series
$f^{\mathrm{quintic}}(\tau) = \sum_n K_1^{\mathrm{quintic}}\cdot
\mathrm{GV}_{0,n}^{\mathrm{quintic}}\, q^n$ is the holomorphic part of an
element $\widehat f^{\mathrm{quintic}}\in\widehat M^{!,+}_{3/2}(\Gamma_0(5)^+)$
with shadow $g^{\mathrm{quintic}}\equiv 0$.

**Equivalence (per V67).** This conjecture is equivalent to all-genus
Yamaguchi--Yau BCOV finiteness on $\widetilde Q$.

### 4.5 Local $\mathbb{P}^2$ specialisation (V82-healed)

**Receptacle (a priori).** $\mathcal{M}^{\mathrm{LP}^2} =
J^{\mathrm{mock},W_3,+}_{0,(1,1)}$: rank-2 Kohnen plus-space mock
$W_3$-Jacobi forms of weight $0$ and indices $(1,1)$. Selected from
$\mathfrak{A}^{\mathrm{LP}^2} = \{(w,\mathrm{type},(\mathbf{m}),\pm)\}$
via RTP clauses:
- W-pin: $w = 0$ (refined topological string is weight-0 elliptic genus).
- G-pin: $W_3$-Jacobi (forced by $W_3$-truncation of $U_{q,t}(
  \widehat{\widehat{\mathfrak{gl}}}_1)$ on equivariant cohomology of
  framed sheaves on $\mathbb{P}^2$).
- P-pin: Bringmann--Folsom--Kane plus-space refinement.
- T-pin: rank-2 (charge lattice = $\mathrm{rk}\,K_0(\mathbb{P}^2) = 3$;
  reduced rank after charge conservation = 2; Jacobi indices $(1,1)$).

**Conjectural completion.** Refined-GV series $\phi^{\mathrm{LP}^2}(\tau,
z_1, z_2) = \sum c^{\mathrm{LP}^2}(n,r_1,r_2) q^n y_1^{r_1} y_2^{r_2}$ is
the holomorphic part of an element of
$\widehat J^{\mathrm{mock},W_3,+}_{0,(1,1)}$ with rank-2 shadow $\equiv 0$.

**Equivalence (per V67).** Equivalent to all-degree refined MNOP for
local $\mathbb{P}^2$, equivalent to all-degree refined-HAE finiteness
via GW/DT correspondence.

### 4.6 Compact vs non-compact: the two-type structure

The V82 healing keeps Tier 1 universal but acknowledges that Tier 2
admits TWO MATHEMATICAL TYPES at present:

- **Type I (compact, $h^{1,1}=1$).** Scalar weight-$w$ mock theta on
  $\Gamma_0(N)^+$, Kohnen plus-space, with $w$ half-integral and shadow
  in $S_{2-w}$.
- **Type II (non-compact toric).** Rank-$n$ mock Jacobi for the toric
  BPS algebra, weight $0$, indices given by the charge lattice, with
  $W$-symmetry from the algebra's truncation.

V82 does NOT claim a unifying receptacle type. The conjecture has two
mathematical species at the witness level, even though Tier 1 is one
universal residual. Future receptacle types (compact $h^{1,1}>1$, banana,
etc.) are anticipated but not yet enumerated.

---

## §5. The V82 Single Platonic Display

$$
\boxed{\;
\begin{aligned}
&\textbf{Tier 1 (universal residual, } \ClaimStatusConditional\text{):}\\
&\xi(A^X) \;=\; \sum_\alpha K_\alpha^X\, e^{-S_\alpha^X/g_s}\,
\Delta_{S_\alpha^X}\,\widehat Z^X \;=\; 0 \\
&\quad \Longleftrightarrow\;
\text{all-order refined-HAE finiteness on } X.\\[6pt]
&\textbf{Tier 2 (witness-receptacle, } \ClaimStatusConditional\text{):}\\
&\widehat Z^X \in \widehat{\mathcal{M}}^X,\quad
\mathcal{M}^X = \mathrm{RTP}(A^X) \in \mathfrak{A}^X.\\
&\text{Ambient } \widehat{\mathcal{M}}^X\text{ exists a priori; specific }
\widehat Z^X\text{ membership is conjectural.}\\[3pt]
&\text{Conditional on chain-level CY-A}_3\text{ for non-K3 Class-B inputs.}
\end{aligned}
\;}
$$

This is ONE display, two tiers. Tier 1 is universal; Tier 2 is
input-dependent and multi-typed. The V67 single-tier display collapses
"existence of receptacle" and "membership of completion" into a single
phrase; the V82 two-tier display separates them.

---

## §6. End-of-wave report

**Receptacle existence status.** TWO-TIERED.
*Ambient* receptacle space $\mathcal{M}^X$ (e.g., $M^{!,+}_{3/2}(\Gamma_0(5)^+)$
for quintic, $J^{\mathrm{mock},W_3,+}_{0,(1,1)}$ for LP^2): exists A PRIORI
as a classical modular-forms object (Bruinier--Funke for Maass extensions;
Eichler--Zagier and Bringmann--Folsom--Kane for mock Jacobi). *Specific
completion* $\widehat Z^X\in\widehat{\mathcal{M}}^X$: existence is the
CONJECTURAL content of V82-CB-Universal Tier 2. V67's collapse of these
two distinct claims into "boundary-data-forced receptacle" is healed by
explicit two-tier separation.

**Uniqueness verdict.** Receptacle is unique only after the
representation-theoretic pinning principle (RTP) is applied, with four
clauses (weight, group, plus-space, type). RTP itself is a conjectural
selection principle currently functioning as a 4-clause heuristic; proving
RTP uniqueness is a Vol III research direction. Without RTP, the
receptacle is at most determined as a finite admissible set
$\mathfrak{A}^X$ (size $\sim 12$ for the quintic).

**CY-A_3 inheritance.** V82-CB-Universal (both tiers) is conditional on
chain-level CY-A_3 for non-K3 Class-B inputs. The dependency chain:
"V82-CB-Universal $\Rightarrow$ receptacle map RTP $\Rightarrow$ chain-level
$A^X$ $\Rightarrow$ CY-A_3 chain-level (currently inf-cat only for
non-K3 Class-B)". Per HZ3-3, both tiers carry $\ClaimStatusConditional$
with this chain stated in the body. Inf-cat CY-A_3 is insufficient because
the receptacle map needs explicit chain-level boundary data.

**v3.4 directive.** RANK_1_FRONTIER_v3.4 (succeeding v3.3 from V67) must:

1. Replace V67's "boundary-data-forced receptacle $\mathcal{M}^X$" with
   the V82 two-tier formulation (universal residual Tier 1 + RTP-pinned
   receptacle Tier 2).
2. Add explicit existence-vs-construction taxonomy table (V82 §4.3) to
   the Class-B paragraph.
3. State the four-clause RTP pinning principle (V82 §4.2) as the
   selector that makes $\mathcal{M}^X$ unique within the admissible
   family $\mathfrak{A}^X$.
4. Flag chain-level CY-A_3 conditionality on V82-CB-Universal for non-K3
   Class-B inputs (HZ3-3 dependency-chain notation).
5. Remove the implicature that Type I (scalar mock theta) and Type II
   (rank-$n$ mock Jacobi for $W$-algebra) are instances of one universal
   receptacle type; acknowledge two-type structure at Tier 2.
6. Open research direction: "Prove RTP uniqueness for Class B" (i.e.,
   prove that the four pinning clauses single out a unique receptacle
   from $\mathfrak{A}^X$) and "Enumerate Tier 2 types beyond Type I/II"
   (compact $h^{1,1}>1$, banana, conifold extension).
7. The CCC retirement (V67 directive) and "two boundary-data
   specialisations" framing remain in v3.4; only the receptacle existence
   structure is updated.

**LOSSLESS LAUNCH summary.** The V82 two-tier formulation is a LOSSLESS
strengthening of V67-CB-Universal: it preserves the universal residual
content (Tier 1), preserves the receptacle dictionary for the two
canonical inputs (quintic, LP^2), preserves the equivalences to
Yamaguchi--Yau and refined MNOP, while sharpening the existence-vs-
construction structure, the pinning principle, the chain-level CY-A_3
conditionality, and the two-type (rather than uni-type) Tier 2 structure.
The frontier becomes sharper: V82 specifies what is a priori, what is
conjectural, what is conditional, and what selection principles are at
work. The Russian-school discipline closes the receptacle gap that V67
left implicit.

---

**End of memorandum.**

Authored by Raeez Lorgat. No AI attribution; no commit; no manuscript
edits; no test runs; no build. Read-only sandbox memorandum.
