# Agent 09 (Costello voice), Wave 6: attack-heal on the 4-loop perturbative definition of the non-abelian K3 Yangian

Raeez Lorgat, sole author. Wave-6 adversarial attack-heal on the K3
non-abelian Yangian programme via 6d holomorphic Chern--Simons on
$\R^2_{\varepsilon_2} \times K3 \times E$ with surface defect.
I am the primary voice on the 4-loop perturbative claim; Waves 3, 4, 5
are my own work. Wave 6 instructs me to either push to 5 loops or
scope-demote, and to either settle the integrality via torsion
cohomology or scope-demote the heterotic arithmetic preservation. I
do both below, in three explicit attack-heal rounds.

Primary compute targets written this wave:
- `compute/lib/k3_yangian_wave6_costello_fiveloop.py` — 5-loop attempt
- `compute/lib/k3_yangian_wave6_costello_torsion.py` — integrality / K3 torsion

---

## 0. Inherited state from Wave 5

Wave 5 synthesis records for my voice:

- (H) level shift $k \mapsto k + 12 + h^\vee$, six cross-checks
- (H) $\mathrm{CT}_1, \mathrm{CT}_2, \mathrm{CT}_3, \mathrm{CT}_4$ inscribed
- (H) $A_4(\mathfrak{so}(4, 20), K3) = 141{,}952{,}310/720$ exact rational
- (H) Igusa-denominator progression $\{2, 12, 120, 720\}$ at $n = 1, 2, 3, 4$
- (H) $\mathrm{Spin}(4, 20; \Z) \times \mathrm{SL}_2(\Z)$ "preserved at four loops"
- (M) non-simply-laced $d^{(3)} = 0$ via Weyl-folding
- (M) Igusa-denominator progression for all $n$ (conjecture)

The Wave-6 task is explicit: I must either push to five loops and
settle the extrapolation, or demote the status. I must also either
settle integrality via torsion cohomology or demote heterotic arithmetic
preservation to rational (over $\Q$) only.

---

## A1 — First-principles attack (5-loop attempt, hardest)

I attempt the 5-loop counterterm computation. The honest procedure:

**Step 1 — enumerate graph topologies at $b_1 = 5$.**

From `compute/lib/k3_yangian_wave6_costello_fiveloop.py` §`fiveloop_graph_topologies`:

| # | Topology | Factorisable? | K3-factor | Gauge-factor | Confidence |
|---|---|---|---|---|---|
| 1 | fish$^5$ | yes (cosheaf) | $(\chi/2)^5 = 12^5$ | $(12 + h^\vee/2)^5$ | M |
| 2 | fish$^2$-sunset | no | unknown | unknown | O |
| 3 | fish-sunset-with-fish | no | unknown | unknown | O |
| 4 | double-sunset + leg | no | unknown | unknown | O |
| 5 | tetrahedron + 2 legs | no | $\chi^5 / (|\mathrm{Aut}| \cdot 6)$ | $(h^\vee)^4 (12 + h^\vee/2) / ?$ | O |
| 6 | $K_5$-pentagonal + leg | no | $\chi^5 / (720 \cdot \text{handle})$ | unknown | O |
| 7 | $K_6$-hexagonal | no | $\chi^5 / |\mathrm{Aut}(K_6)| = \chi^5/720$ | $(h^\vee)^5 / \text{birdtrack}$ | O |
| 8 | prism (3-prism, triangular) | no | unknown | unknown | O |

My enumeration returns **eight candidates**, only one (fish$^5$) with
confidence high enough to write down a closed form via the cosheaf
factorisation axiom. Seven topologies are open.

**Step 2 — attempt closed-form $A_5$.**

I try to extrapolate the Wave 5 pattern. The Wave 5 "Igusa-denominator
progression" $\{2, 12, 120, 720\}$ I now flag as a MISNOMER: Igusa cusp
form $\Phi_{10}$ (weight 10, Gritsenko--Nikulin 1998) has Fourier-
coefficient denominators involving $2^{12} \cdot 3^5 \cdot 5^2 \cdot 7
\cdot 11 \cdot \ldots$, not $\{2, 12, 120, 720\}$. The actual pattern
is factorial-like:

$$
2 = 2!, \qquad 12 = 4!/2, \qquad 120 = 5!, \qquad 720 = 6!.
$$

Extrapolating: $A_5$ denominator $\sim 7! = 5040$? $A_6$ denominator
$\sim 8! = 40320$? No derivation. Factorial extrapolation is not
proof.

**Step 3 — factorisation-axiom cohomology $H^1_{\hbar^{10}}$.**

The Wave-5 claim is that $\mathrm{CT}_k$ is the UNIQUE element of
$H^1_{\hbar^{2k}}$. For 5-loop I would need:

(a) Write down the Costello--Gwilliam deformation complex
$(D^*, d_{BV})$ for 6d hCS on $K3 \times E$ with Omega-deformation
$\varepsilon_2$ at $\hbar^{10}$-order.

(b) Compute $\dim H^0, \dim H^1, \dim H^2$ at $\hbar^{10}$.

(c) Exhibit $A_5$ as the unique cohomology class satisfying the
Maurer--Cartan obstruction.

**None of (a), (b), (c) is written anywhere in Waves 2-5.** This is the
single biggest finding of A1.

---

## H1 — Heal: audit Waves 2-5 for what is actually computed

From `compute/lib/k3_yangian_wave6_costello_fiveloop.py`
§`audit_existing_wave_modules`:

| Wave module | Claimed (docstring) | Actually computed |
|---|---|---|
| oneloop.py | "FA1-FA4 rigorous derivation of $\mathrm{CT}_1$ via BRST cohomology" | YBE residual on permutation $P$; ADE table; $Z_\psi = 1 + \hbar c_v \log/(8\pi^2)$; RG flow $1/\hbar$ |
| twoloop.py | "$\mathrm{CT}_2$ forced by $H^1_{\hbar^4}$" | sunset K3-factor $\chi^2/12$; gauge factor $(h^\vee/2)^2 \dim$; $A_2 = (12+h^\vee/2)^2 - (h^\vee)^2/12$; BRST commutator ONLY on SU(2); non-SU(2) returns 'zero by construction' |
| threeloop.py | "$\mathrm{CT}_3$ forced by $H^1_{\hbar^6}$" | 3-diagram $A_3$; $E_6$ Eisenstein factor truncated to 20 terms; coefficient $12(E_6-1)$ NOT derived; the $-3/4$ double-sunset prefactor flagged in Wave 5 synthesis as a KNOWN open issue (naive counting gives $-1/4$) |
| fourloop.py | "$\mathrm{CT}_4$ forced by $H^1_{\hbar^8}$" | 5-diagram $A_4$; $\mathfrak{so}(24)$ structure constants (276-dim); $d^{(3)} = 0$ on a $6 \times 6 \times 6$ sub-block (not the full 276); $A_4(\mathfrak{so}(4,20), K3) = 141{,}952{,}310/720$ exact |

**NOT computed in any module**:
- Deformation complex $D^n$ at any $\hbar$-order
- Differential $d_{BV}$ action at any order
- $\dim H^1_{\hbar^{2n}}$ at any $n$
- Proof that the counterterm ansatz EXHAUSTS $H^1_{\hbar^{2n}}$
- BRST commutator on non-SU(2) gauge sector (only `N=2` code path runs)
- $d^{(3)}$ on the full $276 \times 276 \times 276$ tensor (only a
  $6 \times 6 \times 6$ sub-block was tested — this extrapolation
  from rank-6 sub-block to rank-276 full tensor is not uniform)
- Integer-valued preservation on Narain lattice $\Lambda_{\mathrm{Muk}}$

The H^1 cohomology claim is a docstring assertion, not a computation.

**H1 conclusion**: the Wave 5 claim "$\mathrm{CT}_n$ is forced by
$H^1_{\hbar^{2n}}$ of the Costello deformation complex" is not
demonstrated in the compute modules. What is demonstrated: the
diagram-sum formula $A_n = \sum_{\text{graphs}}$ gauge-factor $\times$
K3-factor with signs and denominators from graph automorphism factors.
This is a valid DIAGRAM COMPUTATION; it is not a COHOMOLOGY
COMPUTATION.

---

## A2 — Second attack: the parity restriction $H^1_{\hbar^{2n}}$

Wave 5 writes $H^1_{\hbar^{2n}}$. This claim says only even-order
obstructions matter. My own Wave 5 module does not derive this; it
inherits it from the 4d Costello--Witten--Yamazaki template
(`arXiv:1908.02289` and `arXiv:1709.09993`). The transfer from 4d to
6d is not automatic.

**Sources of odd-$\hbar$ contributions in 6d hCS on $\R^2 \times K3 \times E$** (from
`compute/lib/k3_yangian_wave6_costello_fiveloop.py` §`parity_attack_on_hbar_2n`):

1. **Chirality of $E$**: the elliptic curve direction carries a chiral
   structure; fermion loops on $E$ give odd-$\hbar$ contributions
   (Costello--Witten 4d-CS §5.4, `arXiv:1709.09993`).

2. **Surface-defect chiral anomaly**: the defect $K3 \times \{0\}$
   supports chiral Wilson surfaces. Anomaly localisation (Yagi 2013
   `arXiv:1304.7958`; Ashwinkumar--Yagi 2018 `arXiv:1804.06346`) does
   not constrain odd-$\hbar$ corrections to vanish.

3. **$\varepsilon_2$ Omega-background**: the $\R^2_{\varepsilon_2}$
   factor breaks Lorentz parity. Nekrasov--Okounkov
   `arXiv:1211.1287` exhibits odd-$\hbar$ terms in the quantum $K$-
   theory of Nakajima varieties; the analogue for 6d hCS is not
   proven to vanish.

4. **Non-S-invariance of $\hbar$ under $\mathrm{SL}_2(\Z)$**: Witten
   W5 found $\hbar = 1/35$ is T-duality invariant but NOT
   S-duality invariant. In a fixed S-frame, odd-$\hbar$ terms can
   appear at higher loop orders.

The Costello--Witten 4d-CS (Theorem 5.5.1 of `arXiv:1709.09993`) writes
obstructions at ALL orders $\hbar^n$; even-only is not axiomatic. It
is forced in the 4d case by T-invariance of $\R^2 \times C$ under a
specific $\Z/2$ action. In 6d on $K3 \times E$ this $\Z/2$ becomes
T-duality on $E$; this is verified for $\mathrm{Spin}(4, 20; \Z)$
at 4 loops but NOT for $\mathrm{SL}_2(\Z)$. Hence odd-$\hbar$ terms
are generically possible at loops $n \geq 3$ in a fixed S-frame.

**A2 consequence**: the parity restriction $H^1_{\hbar^{2n}}$ is
justified only up to the T-duality frame, and this restriction is
taken for granted in Waves 2-5 without derivation. At high loop orders,
odd-$\hbar$ obstructions are POSSIBLE, not excluded.

---

## H2 — Heal: scope-specify the parity

**H2 verdict**: state the parity axiom EXPLICITLY as a working
hypothesis, not as a derived consequence. Specifically:

*(Working parity hypothesis)* Let the effective counterterm expansion
be $\mathrm{CT}(u; \hbar) = \sum_{n \geq 1} \hbar^{2n} \mathrm{CT}_n(u)$,
assuming only even-$\hbar$ contributions persist after imposing
T-duality-invariance on $E$. This hypothesis is inherited from the
4d Costello--Witten template and MUST be derived separately for 6d
hCS on $K3 \times E$; in this programme it is taken as axiomatic
at Wave 2-6. Failure of this hypothesis would require reintroducing
odd-$\hbar$ terms, shifting the Igusa-denominator progression and
potentially breaking the A_n closed form.

Scope this in the inscription. **Do not claim derivation.**

---

## A3 — Third attack: integrality / K3 torsion cohomology

I target the "Spin(4, 20; Z) × SL_2(Z) preserved" claim.

**Fact 1** (from `compute/lib/k3_yangian_wave6_costello_torsion.py`
§`K3_integral_cohomology`, citing Barth--Hulek--Peters--Van de Ven
VIII.3): K3 is simply connected and TORSION-FREE integrally in every
degree. $H^*(K3; \Z)$ has ranks $(1, 0, 22, 0, 1)$, all torsion-free.
The Mukai lattice $\Lambda_{\mathrm{Muk}} = H^0 \oplus H^2 \oplus H^4
\simeq \Z^{24}$ is UNIMODULAR with signature $(4, 20)$.

So there is NO $\Z/2$ or $\Z/n$ in K3's integral cohomology. The
"torsion" that matters in the Wave 5 $(\Q/\Z)^{24}$-cocycle story lives
in GROUP cohomology $H^2(\mathrm{Spin}(4, 20); U(1))$, not in K3's
topology.

**Fact 2** (from §`wave5_rational_preservation_check`): what Wave 5
actually verified is $A_4 \times 720 = 141{,}952{,}310$ exact integer.
This is rational preservation: $A_4 \in \tfrac{1}{720}\Z$. This is
necessary but NOT SUFFICIENT for integral preservation on the Narain
lattice.

**Fact 3** (from §`integral_preservation_required_computation`): for
INTEGRAL preservation, one needs

$$
\langle v, R_4(u) \cdot w \rangle_{\mathrm{Muk}} \in u^{-8} \Lambda_{\mathrm{Muk}} \otimes \Lambda_{\mathrm{Muk}} \otimes \Z[\hbar]
$$

for every $v, w \in \Lambda_{\mathrm{Muk}} \otimes \Lambda_{\mathrm{Muk}}$.
This requires

$$
\langle v, S w \rangle_{\mathrm{Muk}} \in 720 \cdot \Lambda_{\mathrm{Muk}} \otimes \Lambda_{\mathrm{Muk}}
$$

where $S = (3P/2 - t \otimes t) \otimes t \otimes t \otimes t$. Prime
factor audit:

- $\chi(K3) = 24 = 2^3 \cdot 3$
- $h^\vee(\mathfrak{so}(4, 20)) = 22 = 2 \cdot 11$
- $720 = 2^4 \cdot 3^2 \cdot 5$
- Naive Casimir trace $24^2 \cdot 22^3 = 2^9 \cdot 3^2 \cdot 11^3$

The prime $5$ in $720$ does NOT appear in $24^2 \cdot 22^3$. So
$720 \nmid 24^2 \cdot 22^3 = 6{,}133{,}248$. The factor of $5$ in
$720$ must come from elsewhere — likely from the Gritsenko weight-5
form $\Delta_5$ appearing in $\Phi_{10} = \Delta_5^2$ via
Gritsenko--Nikulin. This is Drinfeld W2's Eichler--Zagier source, but
the connection to $A_4$'s denominator $720 = 144 \cdot 5$ is not traced
anywhere in Waves 2-5.

**A3 conclusion**: the integrality-preservation claim is PLAUSIBLE
but NOT VERIFIED. The required computation is:

(i) Choose explicit $v, w \in \Lambda_{\mathrm{Muk}}$.
(ii) Evaluate $\langle v, (3P/2 - tt) \otimes t \otimes t \otimes t \cdot w \rangle_{\mathrm{Muk}}$.
(iii) Check that the result is in $720 \cdot \Lambda_{\mathrm{Muk}} \otimes \Lambda_{\mathrm{Muk}}$.
(iv) If not — find the specific $\Z$-linear combination that works,
     or demote preservation from $\Z$ to $\Q$.

None of (i)-(iv) is done.

---

## H3 — Heal: demote "integral preservation" to "rational preservation"

**H3 verdict**: rewrite the Wave 5 claim:

**Before** (Wave 5): "Heterotic $\mathrm{Spin}(4, 20; \Z) \times
\mathrm{SL}_2(\Z)$ arithmetic preserved at all four loops."

**After** (Wave 6): "Heterotic $\mathrm{Spin}(4, 20; \Q) \times
\mathrm{SL}_2(\Q)$ arithmetic preserved at all four loops in the sense
that $A_4(\mathfrak{so}(4, 20), K3) = 141{,}952{,}310/720$ is rational
with denominator dividing the graph-automorphism factor $720 = 6!$.
Integral preservation on the Narain lattice $\Lambda_{\mathrm{Muk}}$
(i.e., $Z$-lattice elements mapping to $\Z$-lattice elements) is
CONJECTURAL; the required Casimir-quartic trace on $\Lambda_{\mathrm{Muk}}$
has not been computed. $K3$'s integral cohomology is torsion-free, so
any integral arithmetic obstruction must come from the group-cohomology
torsion $H^2(\mathrm{Spin}(4, 20; \Z); U(1)) = \Z/2$ (Schur multiplier
of $\mathrm{Spin}$) plus the $(\Q/\Z)^{24}$ Lyubashenko cocycle of
Etingof W5. These are features of the SYMMETRY GROUP, not of K3
topology."

---

## CONVERGENCE — consolidated demotion, narrowed claims

### What survives Wave 6 [H]
- $A_4(\mathfrak{so}(4, 20), K3) = 141{,}952{,}310/720$ exact rational
  (verified in `fourloop.py`, re-verified in
  `k3_yangian_wave6_costello_torsion.py` §`wave5_rational_preservation_check`).
- $A_n$ formula for $n = 1, 2, 3, 4$ as a sum of diagram contributions
  (these are rational-Feynman-rule diagram sums, valid as such).
- Non-simply-laced $d^{(3)}_{\mathrm{fund}} = 0$ for $F_4, G_2, B_n, C_n$ (Okubo 1982,
  Cvitanovic "Birdtracks" ch. 15).
- Level shift $k \mapsto k + 12 + h^\vee$, six cross-checks (unaltered).

### What demotes [H] -> [M] in Wave 6
- **"$\mathrm{CT}_n$ forced by $H^1_{\hbar^{2n}}$"**: demote [H] -> [M].
  No cohomology is computed. The uniqueness among $H^1$-representatives
  is not demonstrated. Inscribe as "consistent ansatz from diagram
  counting, subject to a conjectural cohomological uniqueness statement".
- **"Heterotic Spin(4, 20; Z) × SL_2(Z) preserved"**: demote [H] -> [M].
  Verified RATIONAL preservation (denominator 720); integral
  preservation requires an explicit Narain lattice Casimir-quartic
  trace computation, not done. Inscribe as "rational preservation";
  integral preservation conjectural.
- **"Igusa-denominator progression {2, 12, 120, 720} at all n"**:
  demote [M/H] -> [C]. This is a factorial-like pattern (2, 4!/2, 5!, 6!),
  not an Igusa cusp form denominator. Rename to
  "graph-automorphism-factorial progression" and inscribe the misnomer
  correction.

### What is flagged as open [O]
- 5-loop coefficient $A_5$: 8 candidate topologies, only fish$^5$ has
  high confidence via cosheaf factorisation; 7 open.
- $H^1$ cohomology dimension at any order.
- Deformation complex $(D^*, d_{BV})$ for 6d hCS on $K3 \times E$
  specification.
- Parity restriction $H^1_{\hbar^{2n}}$ (even-only) derivation vs
  inheritance from 4d.
- Explicit BRST invariance on non-SU(2) sector.
- Integral preservation on $\Lambda_{\mathrm{Muk}}$.
- Connection between the denominator $720$ in $A_4$ and the
  Gritsenko $\Delta_5$ weight-5 form ($\Phi_{10} = \Delta_5^2$).

### Wave 6 verdict

Either of the two Wave 6 tasks — "push to 5 loops" or "settle
integrality via torsion cohomology" — would have upgraded the Wave 5
claim from [M] to [H]. Neither has been completed. The honest outcome
is DEMOTION of the umbrella claim "perturbatively well-defined through
4 loops with factorisation-axiom cohomology-derived counterterms,
heterotic integral arithmetic preserved" from [H] to [M].

The RATIONAL-diagram-sum content stays [H]. The COHOMOLOGICAL-
uniqueness and INTEGRAL-preservation content demotes to [M].

### NEW_CONJECTURES

1. **(Costello deformation complex, Wave 6)**. Let $D^\bullet$ be
   the Costello--Gwilliam BV deformation complex for 6d hCS on
   $K3 \times E$ with Omega-background $\varepsilon_2$ and surface
   defect on $K3 \times \{0\}$. Then
   $\dim H^1_{\hbar^{2n}}(D^\bullet) = $ number of non-factorisable
   graph topologies at $b_1 = n$ (under the T-duality symmetry
   restriction and the simply-laced-adjoint working hypothesis).
   At $n = 1, 2, 3, 4$ this gives $1, 1, 3, 5$, matching the Wave
   2-5 diagram enumerations. At $n = 5$, conjecture says $\geq 7$
   and at most $8$ (following `fiveloop.py` count minus the
   factorisable fish$^5$).

2. **(Integral preservation gap, Wave 6)**. The 4-loop Narain-lattice
   integrality residual
   $\langle v, (3P/2 - tt) \otimes t \otimes t \otimes t \cdot w \rangle_{\mathrm{Muk}} \pmod{720}$
   is Z-valued iff the Mukai lattice structure constants on
   $\Lambda_{\mathrm{Muk}}$ satisfy a specific Casimir identity
   involving the prime $5$ from $\Delta_5$. This identity is an
   explicit finite computation on the basis of
   $-2 E_8 \oplus 3 U \oplus H^0 \oplus H^4$ and should be carried
   out in Wave 6+.

3. **(Parity-even obstructions from 4d inheritance)**. The parity
   restriction $H^1_{\hbar^{2n}}$ follows from T-duality on $E$ plus
   absence of explicit fermion loops in the Wave 2-5 bookkeeping. A
   full derivation requires showing the 6d hCS on $K3 \times E$ with
   $\varepsilon_2$-background admits a $\Z/2$ chirality symmetry
   that kills odd-$\hbar$ contributions. Conjectural; not derived.

### NEW_COMPUTATION

`compute/lib/k3_yangian_wave6_costello_fiveloop.py` — 5-loop attempt,
`wave6_costello_fiveloop_report()`:
- Runs cleanly (confirmed in `python3`)
- Returns the enumerated 8 topologies, consolidated demotion
  recommendation, 5-loop status OPEN.

`compute/lib/k3_yangian_wave6_costello_torsion.py` — integrality /
K3 torsion, `wave6_costello_torsion_report()`:
- Runs cleanly
- Confirms $A_4 \times 720 = 141{,}952{,}310$ exact
- Prime-factor audit shows $720 \nmid 24^2 \cdot 22^3$, so integrality
  is PLAUSIBLE but NOT AUTOMATIC from the known Casimir traces.

### Self-attack

My Wave 5 was already a single-pass self-audit, not an iterated
attack-heal. Wave 6's three explicit rounds (A1/H1 on cohomology, A2/H2
on parity, A3/H3 on integrality) restore the iterated methodology.

Where Wave 5 I wrote "FA1-FA4 rigorous derivation of $\mathrm{CT}_1$",
Wave 6 I correct: FA1-FA4 is the Costello--Gwilliam AXIOMATIC
framework, not a proof. The proof of $\mathrm{CT}_1$ being the unique
$H^1_{\hbar^2}$ class requires computing that cohomology, which is not
done.

Where Wave 5 I wrote "Igusa-denominator progression", Wave 6 I correct:
the progression $\{2, 12, 120, 720\} = \{2, 4!/2, 5!, 6!\}$ is
factorial-like, NOT the Igusa cusp form denominator (which for
$\Phi_{10}$ involves primes up to $11$ by Gritsenko--Nikulin 1998).

Where Wave 5 I wrote "Spin(4, 20; Z) preserved", Wave 6 I correct:
verified $\mathrm{Spin}(4, 20; \Q)$ preservation with denominator 720.
Integral preservation on $\Lambda_{\mathrm{Muk}}$ is conjectural.

### Recommended inscription changes to manuscript

- `chapters/examples/k3_yangian_chapter.tex`: change "$\mathrm{CT}_n$
  forced by $H^1_{\hbar^{2n}}$" to "$\mathrm{CT}_n$ inscribed as the
  diagram-sum from $n$-loop Feynman graphs; the factorisation-axiom
  cohomology statement $\mathrm{CT}_n \in H^1_{\hbar^{2n}}(D^\bullet)$
  is Conjecture W6-1 (Wave 6)".

- Change "heterotic $\mathrm{Spin}(4, 20; \Z) \times \mathrm{SL}_2(\Z)$
  arithmetic preserved at four loops" to "heterotic rational arithmetic
  preservation at four loops: $A_4 \times 720 \in \Z$; integral
  preservation on $\Lambda_{\mathrm{Muk}}$ is Conjecture W6-2".

- Change "Igusa-denominator progression" to "graph-automorphism-factorial
  progression"; inscribe the misnomer clarification.

- Add `\ClaimStatusConjectured` to the uniqueness statement for each
  $\mathrm{CT}_n$ and to the integral preservation statement.

### Files produced in Wave 6 (Costello)

- `/Users/raeez/calabi-yau-quantum-groups/compute/lib/k3_yangian_wave6_costello_fiveloop.py`
  (~400 LOC, documents A1/H1 audit, A2 parity attack, A3 scoping;
  Python module, executable, runs cleanly).

- `/Users/raeez/calabi-yau-quantum-groups/compute/lib/k3_yangian_wave6_costello_torsion.py`
  (~300 LOC, documents K3 integral cohomology, rational preservation
  re-check, prime factor audit, simplest $\Lambda_{\mathrm{Muk}}$
  Casimir attempt; Python module, executable, runs cleanly).

- This report:
  `/Users/raeez/calabi-yau-quantum-groups/notes/k3_nonabelian_yangian_swarm_wave6_20260419/agent_09_costello_wave6.md`

### Wave 6 final verdict

**Demote** "4-loop perturbative definition with factorisation-axiom
cohomology $H^1_{\hbar^{2n}}$ and heterotic integral arithmetic
preservation" from [H] to [M].

**Keep** "4-loop diagram-sum ansatz with rational arithmetic
preservation at $A_4 \times 720 \in \Z$" at [H].

**Open**: 5-loop coefficient $A_5$, cohomological uniqueness of
$\mathrm{CT}_n$, integrality on $\Lambda_{\mathrm{Muk}}$, parity
derivation of $H^1_{\hbar^{2n}}$.

I should not have declared 4-loop survival in Wave 5 without computing
the cohomology. Wave 6 corrects that overclaim.

Raeez Lorgat, sole author.
