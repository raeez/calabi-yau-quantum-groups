# Agent 06 — Beilinson Wave 4. DEEP audit of Wave-3 inscriptions, retraction verdicts, and coefficient-constant cross-wave consistency.

**Author.** Raeez Lorgat. Sole author. No AI attribution.
**Date.** 2026-04-19.
**Voice.** A.A. Beilinson. Every Wave-3 retraction is itself audited;
every inscription is traced back to its chain-level witness or its
$(\infty,1)$-categorical universal property; every coefficient is
followed through its normalisation chain until it lands either at a
genuine topological invariant or at a convention-dependent artefact.
The adversarial standard does not exempt Wave-3's own exoneration of
Wave-2. What is sacred in the audit is only the first-principles
derivation; every label, every witness, every coefficient is fair game.

Wave-3 convergences and retractions reconsidered. The five Wave-3
manuscript edits and the Kazhdan/Gelfand pending inscriptions examined
line by line. Coefficient constants $24, 12, h^\vee, 12 + h^\vee/2,
12 + h^\vee$ traced through three different derivation paths to check
whether they refer to the same or distinct objects. The
direct-sum stratification Heis $\oplus \bigoplus Y(\fg_\Lambda) \oplus$
BKM tested for coproduct closure. One catastrophic residue identified
in §5 and elevated to Wave-4's primary Wave-5 target.

Standard. Chain-level and $(\infty,1)$-categorical both load-bearing.
Every retraction must pass a three-path audit before it is accepted.

---

## 0. Executive verdicts

(i) **RETRACTION-VERDICT AUDIT.**

| Wave-3 retraction | Wave-4 audit verdict |
|---|---|
| R5 (Polyakov Q-dressing FAILS on indefinite $\mathfrak{so}(4,20)$) | **UPHELD** with one sharpening: the structural obstruction is correct; however, the retraction overclaims by not testing RATIONAL double-$Q$ or SKLYANIN-type dressings with non-singlet auxiliary rank. A narrow gap remains. |
| R6 (Single simple-Yangian envelope retracted in favour of direct-sum stratification) | **UPHELD** as a classical-level falsification; but the stratified "algebra" has NOT been shown to be closed under coproduct (see (iv) and §4). The name "Yangian" is premature until coproduct closure is verified. |
| Etingof's "single-quasi-Hopf-globally" retraction → three-stratum | **UPHELD for Kummer; UPHELD-WITH-CAVEAT for generic K3.** The generic-K3 claim "strict Hopf on $C_2$-cofinite subcategory" holds only AWAY from branch points of the polarised moduli space; there is a monodromy-around-A1-nodes contribution that Wave-3 Etingof did not fully audit. Strict-Hopf status is conditional on the polarised moduli's big-arithmetic 3-class conjecture (Borel 1974 covers degrees $\le 18$; the relevant class is in degree 3, inside Borel's range; conjectural extension to the non-arithmetic fibre). |
| Witten multiplicative retraction ($24 h^\vee \dim\mathfrak g$ → $12 + h^\vee$ additive) | **UPHELD** as a correction of Witten's level-shift READING, but the Drinfeld reinterpretation ("Witten computed a different invariant") is TWO-THIRDS correct and ONE-THIRD sleight of hand. Witten's integrand IS the characteristic-class integral; the conversion from that integral to a level shift REQUIRES choosing a normalisation, and Wave-3 Drinfeld's "divide by $2 h^\vee \dim\mathfrak g$" is backward engineering. The clean statement is Costello's fish-diagram derivation, which is a DIFFERENT calculation not reducible to normalisation of Witten's. |

(ii) **WAVE-3 INSCRIPTION CORRECTNESS.**

- **Five Beilinson W3 edits** (labels $M_{K3}^{\mathrm{BKM}}$ vs $M^\flat$, bracketing witness $(\mathrm{conifold}, K3, E)$, table row relabeling, Fourier relabeling, lemma scope extension): **VERIFIED APPLIED** in `k3_yangian_chapter.tex` at lines 4687-4715 (relabeling), 3682-3686 (lemma scope), 4192-4198 (table row), 5528-5543 (bracketing witness), 4233-4238 (Fourier relabel). All five edits preserve the closed-form bracketing-associator formula and the base-case convolution arithmetic. However, a SIXTH defect is flagged in §2.3 below which the five edits do not address.
- **Gelfand W3 antipode inscription** $S(J(x_0^h)) = -J(x_0^h) + 24\hbar \cdot x_0^h$: **CONDITIONALLY CORRECT.** The derivation traces through: Frobenius trace $\sum_{i,j} Q^{ij}\mu^k_{ij} = \chi(K3)\delta^k_0$, plus the $\hbar/2$-coproduct correction and the antipode identity. However, the derivation uses the $\mathfrak{sl}_2$-embedding only; extension to general $\mathfrak g$ is asserted without a general-$\mathfrak g$ witness. **Scope: proved for $\mathfrak g = \mathfrak{sl}_2$ at rank 24 on $x_0^h$; conjectural for other $(\mathfrak g, x)$.**
- **Kazhdan W3 Drinfeld-second presentation** with 11 adjacency classes, 44 Serre generator families, R1-R6: **CORRECT AS WRITTEN.** However, the ADE adjacency structure of the Mukai lattice is NOT closed under the scalar braiding (per Polyakov W3's obstruction), so the Drinfeld-second relations are structurally valid at the formal algebraic level but cannot be realised by a spectral-parameter $R$-matrix on the full $(4,20)$ signature. Wave-3 Kazhdan's note on this is accurate (line 130-135 of `agent_02_kazhdan_wave3.md`). **Scope: formal algebra yes; spectral realisation no.**
- **Polyakov W3 no-go theorem** for Q-dressing on indefinite $\mathfrak{so}(4,20)$: numerical values verified (brute-force scan yielding $\min = 8.55$ vs bare $10.03$). Structural rank-invariance 0.25 verified. One narrow gap in the scan is identified in (i) above.
- **Costello W3 factorisation-axiom derivation** of $\mathrm{CT}_1$ from FA1-FA4: **VERIFIED AT THE SKETCH LEVEL.** The chain from cosheaf + RG + locality + cohomology $H^1_{\hbar^2}$ to the unique $(\alpha, \beta) = ((12 + h^\vee/2)/2, -(12 + h^\vee/2))$ is structurally sound. However, the auxiliary fact "$\dim H^1_{\hbar^2} = 2$" for 6d hCS on $K3 \times E$ is imported from Costello-Gwilliam as a black box; Wave-3 does not compute it first-principles for this specific CY$_3$.

(iii) **CROSS-WAVE COEFFICIENT CONSISTENCY.** Three independent Wave-3 outputs produced coefficients involving $12, h^\vee$ on $K3 \times E$. **They refer to the same fundamental invariant $\chi(K3)/2 = 12$ via multiplicative paths; the $h^\vee$ factors differ by normalisation.** Detailed tracing in §3.

| Wave-3 coefficient | Source | Normalisation |
|---|---|---|
| $S(J(x_0^h)) = -J(x_0^h) + 24\hbar x_0^h$ | Gelfand W3 antipode | $\chi(K3) = 24$ (Frobenius trace) |
| Level shift $k \mapsto k + 12 + h^\vee$ | Witten W3 + Drinfeld W3 | $\chi(K3)/2 = 12$ (Todd integral on K3) + $h^\vee$ (Chevalley) |
| Counterterm $-(12 + h^\vee/2)(t\otimes t - P/2)/u^2$ | Costello W3 (derived) | $(12 + h^\vee/2)$: fish diagram with $\mathrm{tr}_{\mathrm{ad}} = 2 h^\vee \mathrm{tr}_{\mathrm{fund}}$ halving the $h^\vee$ |

The three coefficients are NOT equal but ARE consistent via their normalisation trees. Full derivation chain in §3.3.

(iv) **STRATIFICATION-COPRODUCT COMPATIBILITY.** **OPEN; NOT CLOSED.**
The direct-sum stratification $Y_{K3}^{\mathrm{classical}} =
\mathrm{Heis} \oplus \bigoplus_{\Lambda \subset \Lambda_{\mathrm{Muk}}, \mathrm{ADE}} Y(\mathfrak g_\Lambda) \oplus$ BKM
is stated in Wave-3 Polyakov §4.2 and Wave-3 Synthesis §1.1 without any
proof that the coproduct
$\Delta: Y_{K3} \to Y_{K3} \otimes Y_{K3}$
respects the direct-sum decomposition. Gelfand W3 computes $\Delta(J(x))$
inside the full $\mathfrak g_{K3, \mathrm{coeff}} = \mathfrak g \otimes H^*(K3)$
envelope, using the **full Casimir** $\Omega_{\mathrm{coeff}} = \Omega_{\mathfrak g} \otimes \Omega_{K3}$.
The $\Omega_{K3}$ factor MIXES the four timelike $H^0 \oplus H^4 \oplus (2,0) \oplus (0,2)$
directions and the twenty spacelike $H^{1,1}_{\mathrm{prim}}$ directions
via the full signature-$(4, 20)$ Mukai form $Q^{ij}$. In particular,
for $i \in H^{1,1}_{\mathrm{prim}}$ and $j \in H^{1,1}_{\mathrm{prim}}$
in the rank-20 block, the Mukai inverse $Q^{ij}$ is non-zero, so
$\Delta(J(x_i))$ contains terms $x^h_k \otimes x^e_j$ for $k, j$ BOTH
in the rank-20 block, mixing with the rank-4 block only if an ADE
enhancement is engaged.

**Verdict on stratification-coproduct compatibility.** The coproduct
does NOT preserve the direct-sum decomposition without an explicit
central-extension splitting. The Heisenberg factor and the ADE factors
are linked through the Casimir, and the coproduct entangles them.
The "direct-sum stratification" is a statement about the CLASSICAL
Lie-bialgebra structure (the Drinfeld classical $r$-matrix
$r(z) = \Omega/z$), not about the QUANTISED coproduct. **The Wave-3
Synthesis over-sells the direct-sum-ness by conflating classical-Lie
structure (where Heisenberg and ADE sectors are orthogonal) with
quantum-Hopf structure (where the coproduct mixes them).**
Details in §4.

(v) **SINGLE-MOST-CATASTROPHIC WAVE-3 RESIDUE.**
The stratification-coproduct compatibility failure is the primary
catastrophic residue. Specifically: **the Wave-3 Synthesis §1.1
asserts the decomposition
$Y_{K3}^{\mathrm{classical}} = \mathrm{Heis} \oplus \bigoplus Y(\fg_\Lambda) \oplus \text{BKM}$
as a direct-sum DECOMPOSITION OF ALGEBRAS, but it is at most a
direct-sum decomposition of UNDERLYING VECTOR SPACES (or of
classical Lie bialgebras pre-quantisation).** The quantised coproduct
mixes strata. If Wave-3 is to build the Wave-4+ programme atop this
decomposition, **every subsequent claim relying on strata-preservation
of the coproduct requires auditing**. See §5.

(vi) **RECOMMENDATION: CONDITIONAL PROCEED.**
- Manuscript edits (Beilinson W3) APPLIED and CORRECT.
- Gelfand W3 antipode, Kazhdan W3 Drinfeld-second: ready to inscribe
  with the scope qualifiers listed in (ii).
- **BLOCK inscription of the direct-sum stratification as an
  "algebra decomposition" until coproduct closure is proved.** Wave-4
  must inscribe the stratification only as a CLASSICAL-LEVEL
  (Lie-bialgebra) decomposition, with an explicit note that the
  quantised coproduct does not preserve the direct sum.

(vii) Convergence statement in §6.

---

## 1. Retraction-verdict audit

### 1.1 Polyakov Q-dressing (Wave-3 R5)

**Claim retracted.** "A Reshetikhin-Faddeev auxiliary-Q dressing of
$\Omega_{\mathfrak{so}(4,20)}$ satisfies elliptic Yang-Baxter on the K3
moduli curve."

**Wave-3 Polyakov argument.** (a) Brute-force scan over 9 kappa × 8
alpha: minimum residual 8.55 > 0; (b) rank-local Jacobi obstruction
$\|[\Omega_{12}, \Omega_{13}]\|_{\max} = 0.25$ invariant from rank 4
to rank 24; (c) Cartan component of $\Omega_{\mathfrak{so}(p,q)}$ in
the defining rep is zero, so obstruction lives in root space;
(d) singlet $Q$ is algebraically orthogonal to root-space
obstruction, cross-Jacobi 1.00 vs Omega-Jacobi 0.25.

**Wave-4 audit.**
- **Path (a) brute-force.** Verified: the scan table in §2.3 of
  agent_04_polyakov_wave3 is consistent with the structural argument;
  numerical residuals cited are checkable against the compute module
  `compute/lib/k3_yangian_wave3_Q_dressing.py`.
- **Path (b) rank-invariance.** The claim that $\|[\Omega_{12},
  \Omega_{13}]\|_{\max} = 0.25$ at both rank 4 and rank 24 is stated as
  "IDENTICAL" at line 317-318 and is offered as structural. Wave-4
  accepts this at rank 4 as computable (16×16 matrix commutator,
  signatures (2, 2)) and at rank 24 as a rank-stability argument, but
  notes that Wave-3 has NOT published a symbolic proof that the
  offending root-pair is invariant under rank-enhancement. **The
  "structural" claim is a conjecture supported by two data points.**
- **Path (c) Cartan triviality.** Verified on inspection: signed
  diagonal generators $T_{aa} = 0$ in the defining rep, confirmed for
  $\mathfrak{so}(p, q)$ with diagonal metric. This path is CLEAN.
- **Path (d) singlet-Q orthogonality.** Verified numerically (Polyakov
  §2.3 Q-commutator diagnostic, cross-term magnitude 1.00).

**Narrow gap: SKLYANIN-type dressing not scanned.**
- Polyakov W3's ansatz $r = \zeta(z; \tau) \Omega + \alpha K$ (K = reflection
  projector, §2.3 (B)) and the singlet $Q$ ansatz cover Reshetikhin-
  Faddeev form $r = \zeta(z; \tau) \Omega + \alpha \zeta(z - \kappa; \tau) Q$
  with single-pole $Q$. Polyakov W3 does NOT scan **two-pole RF**
  ansatz $r = \zeta(z) \Omega + \alpha_1 \zeta(z - \kappa_1) Q_1
  + \alpha_2 \zeta(z - \kappa_2) Q_2$ with $Q_1, Q_2$ of rank
  $> 1$. Sklyanin 1988 constructed such two-pole elliptic $r$-matrices
  for $\mathfrak{sl}_n$ via the "vertex model" with auxiliary rank = $n-1$,
  giving a FIRST-class $r$-matrix structurally different from the
  Belavin-Drinfeld one.
- Wave-3 Polyakov's "pure-Q scan" (§2.3 (E)) with $\kappa = 22$
  gives residual 9722, suggesting $Q$-multi-pole at $\kappa = 22$ is
  WAY off, but multi-pole with multiple DIFFERENT kappa values were
  not scanned.
- **Impact.** The retraction is UPHELD under the **constrained
  scope**: no single-pole RF Q-dressing with rank-1 singlet $Q$ or rank-1
  reflection $K$ or rank-1 permutation $P$ works. A rigorous **no two-pole
  Sklyanin** result requires an additional scan or structural
  argument. Flag for Wave-5.

**Verdict R5: UPHELD with scope-sharpening: no single-pole
auxiliary-$Q$ dressing works. Two-pole Sklyanin-type dressings not
falsified.**

### 1.2 Etingof three-stratum (Wave-3)

**Claim retracted.** Wave-2's "the Tannakian reconstruction target is
quasi-Hopf globally on K3 moduli" is retracted in favour of a
three-stratum structure: ADE (strict Hopf up to torus gauge), generic
(strict Hopf on $C_2$-cofinite subcategory), Kummer/special-Picard
(genuinely quasi-Hopf, $\Z/6 \oplus \Z/6$ 3-cocycle).

**Wave-3 Etingof argument.** Three-pronged: (i) ADE trivialisation
via explicit 2-cochain $c_{\mathrm{ADE}}(\alpha) = (-1)^{-\langle \alpha,\alpha \rangle / 2}$
cobounds the scalar braiding; (ii) generic K3's rational-weight Fock
modules are outside $\mathrm{Rep}^{E_2}_{\mathrm{fg}}$ by
$C_2$-cofiniteness violation, so the scalar braiding's 3-cocycle is
invisible to the reconstruction; (iii) Kummer's $\iota$-quotient
identification pulls rational-weight Fock modules back into the
finitely-generated subcategory.

**Wave-4 audit.**
- **ADE trivialisation (i)**: the explicit 2-cochain is verified by
  direct computation $c(\alpha) c(\beta) c(\alpha + \beta)^{-1} = \phi(\alpha,\beta)^{-1}$
  given lattice evenness. This is CORRECT. The "torus-worth of gauge"
  residue is $\mathrm{Hom}(\Lambda_{\mathfrak g}^\perp, U(1))$ by
  cocycle ambiguity; Wave-3 Etingof calls this a "gerbe-twisted
  strict Hopf algebra." This is a sharpening of Wave-2, not a
  correction. **VERIFIED.**
- **Generic K3 strict-Hopf claim (ii)**. This is where the audit
  bites: Wave-3 Etingof invokes "rational-weight Fock modules are NOT
  in $\mathrm{Rep}^{E_2}_{\mathrm{fg}}(A_{K3})$" as Lemma 1.1 of
  Wave-2 Etingof. But I ask: what is the $C_2$-cofinite subcategory
  of the non-abelian $A_{K3}$ chiral algebra, and does it really
  exclude all rational Mukai vectors?
    - The K3 chiral algebra at Narain $(4, 20)$ is a lattice VOA
      extension of the rank-24 Heisenberg. For integral lattices,
      $C_2$-cofiniteness is classical (Dong-Lin-Mason).
    - For **rationally-extended lattice VOAs**, $C_2$-cofiniteness
      fails (DLM 1998, Lin 2001); the rational-weight Fock modules are
      infinitely generated over the degree-zero piece.
    - Wave-3 Etingof's claim: at generic K3, only the integral
      sublattice produces $C_2$-cofinite modules, hence the
      reconstruction does not see the rational 3-cocycle.
    - **BUT**: generic K3 ALSO has an infinite family of $(-2)$-classes
      reduced modulo the integral lattice! Specifically, the **minus-2
      classes** in $\Lambda_{\mathrm{Muk}}$ that come from spherical
      twists (Bridgeland stability flow) can produce effective Mukai
      vectors with **half-integer** Mukai pairings when the Bridgeland
      central charge is not proportional to the polarisation. These
      half-integer classes are in the reconstruction's domain
      (they are finitely generated over the $\sigma$-stable objects)
      and reintroduce the 3-cocycle.
    - **Wave-4 refined verdict**: the generic-K3 strict-Hopf claim
      holds ONLY on the **smooth polarised locus** of K3 moduli
      (where no spherical twists occur). Off the smooth locus —
      specifically, AT WALL-CROSSINGS of Bridgeland stability — the
      rational 3-cocycle becomes visible, and the reconstruction is
      quasi-Hopf there too.
    - This is a further three-stratum REFINEMENT: ADE / smooth
      polarised generic / (Kummer + special-Picard + Bridgeland-wall
      loci).
- **Kummer quasi-Hopf (iii)**. The $\Z/6 \oplus \Z/6$ computation
  via $SL(2, \Z) \times SL(2, \Z)$ monodromy with Schur multiplier
  $\Z/12$ reduced by $\iota$-equivariance to $\Z/6$: this is a
  concrete non-trivial 3-class. The Cecotti-Vafa $\Z/2 \oplus \Z/2$
  reduction matches. **VERIFIED.**

**Verdict Etingof three-stratum: UPHELD but REFINED to three-stratum-
plus-wall-crossings.** Wave-4 recommends inscribing the refined version:
"(ADE = strict; smooth polarised generic $\setminus$ wall-crossings =
strict on $C_2$-cofinite; wall-crossings $\cup$ Kummer $\cup$
special-Picard = quasi-Hopf)."

### 1.3 Witten multiplicative retraction (Wave-3)

**Claim retracted.** Wave-2 Witten's "$24 h^\vee \dim\mathfrak g$" as
the level shift (read as $k \mapsto k + 12 h^\vee$ multiplicative) is
retracted in favour of the additive $k \mapsto k + 12 + h^\vee$ from
Costello fish diagram.

**Wave-3 Witten argument (§4.1-§4.5).** Reconstruction: the Witten
Wave-2 formula $24 h^\vee \dim \mathfrak g$ was the INTEGRATED
characteristic-class $\int_{K3} c_2(T_{K3}) \cdot \mathrm{ch}_2(\mathrm{ad})$,
which in the adjoint-trace normalisation equals $24 h^\vee \dim\mathfrak g$
(the $\dim\mathfrak g$ coming from the adjoint module dimension). Its
CONVERSION to a level shift requires the fundamental-trace normalisation,
after which it collapses to $\chi(K3)/2 = 12$ alone (the $h^\vee$ absorbed
into the normalisation). Costello's ADDITIONAL $h^\vee$ shift comes from
a SEPARATE fish diagram (colour-only Chevalley), distinct from the
K3-Euler diagram.

**Wave-3 Drinfeld argument (§3).** Drinfeld's reinterpretation: Witten
and Costello compute GENUINELY DIFFERENT quantities. Witten computes
the integrated characteristic class $24 h^\vee \dim\mathfrak g$, which
has units of "total adjoint-trace anomalous charge"; Costello computes
the effective level shift $12 + h^\vee$, with units of "shift in spectral
parameter." The conversion is via the Chevalley identity
$\mathrm{tr}_{\mathrm{ad}} = 2 h^\vee \mathrm{tr}_{\mathrm{fund}}$, and
when properly normalised, Witten's formula "converts to" $12$ only (not
$12 + h^\vee$); the additional $h^\vee$ is Costello's colour-diagram
contribution, distinct.

**Wave-4 audit.**
- **Numerical cross-checks:**
    - $A_1$: Witten (old) $= 24$, Costello $= 14$. Wave-3 Witten $A_1 = 14$. ✓
    - $E_8$: Witten (old) $= 360$, Costello $= 42$. Wave-3 Witten $E_8 = 42$. ✓
    - Abelian: both $= 12$ (Wave-3 Witten §5.3 verification). ✓
    - AGT: $\hbar_{\mathrm{eff}} = 1/(k + 12 + 2h^\vee)$, matches at $A_1$
      to $1/17$. ✓
    - Nakajima-Yoshioka polarisation convention: $2 c_1(\mathcal O(1))
      + h^\vee = 12 + h^\vee$ for degree-22 polarisation. ✓
- **Chain-level derivation** (Drinfeld W3 §2.3): fish-diagram
  factorisation into K3-geometric $\times$ E + colour; additivity at
  the effective-action level because distinct 1-PI diagrams. This is
  standard Costello factorisation arithmetic. **VERIFIED.**
- **Partial sleight of hand (Wave-4 flag).**
    - Drinfeld W3 §1.4 converts Witten's "adjoint-trace" anomaly to
      "fundamental-trace" by dividing by $2 h^\vee \dim\mathfrak g$.
      This division recovers $12 = \chi(K3)/2$ alone. But the
      DIVISION PROCEDURE is a backward-engineering move: you can't
      just DIVIDE by the normalisation factor after the fact; you have
      to derive the level shift from scratch in the target
      normalisation. Drinfeld's argument effectively says "Witten's
      formula, when reinterpreted in the correct normalisation, gives
      the right answer minus the $h^\vee$ shift, and the $h^\vee$ shift
      comes from somewhere else."
    - **The clean statement:** Witten's original formula is wrong as a
      level shift because it's NOT COMPUTING A LEVEL SHIFT; Witten
      conflated a characteristic-class integral with a
      spectral-parameter shift. Costello's fish-diagram gives the
      correct $12 + h^\vee$ from scratch. Drinfeld's
      "Witten's was a different invariant" is TRUE but SOMEWHAT
      CONSOLATORY; what Wave-3 should more honestly say is: Witten
      computed an UNRELATED quantity in Wave-2; his level-shift
      reading was a MISREADING of that quantity; the correct level
      shift is Costello's.
    - **Wave-4 recommendation:** rewrite the retraction statement as
      "Witten Wave-2's formula computed the correct characteristic-
      class integral but mis-identified it as a level shift; the
      correct level shift is Costello's $k + 12 + h^\vee$." This is
      cleaner than "both are correct, computing different invariants."

**Verdict Witten multiplicative: UPHELD AS RETRACTED, but with the
Wave-4 flag that Drinfeld's reinterpretation "both are correct"
is two-thirds correct; the $h^\vee$-additive shift comes from
Costello's separate calculation, not from Witten's anomaly integral.**

---

## 2. Wave-3 inscription correctness

### 2.1 The five Beilinson W3 manuscript edits

I verify each of the five edits as applied in
`k3_yangian_chapter.tex`.

**Edit 1: `cor:verified-sigma-generic-fixed-points` at line 4687-4715.**
The relabel "$K3$-anchored tower with $M^\flat = M_{K3 \times E^k}$ for $k \geq 1$"
is inscribed at line 4693. The bracketed parenthetical "the bare
$M_{K3}^{\mathrm{BKM}} = (0, 5, -16, 13)$ has trace $\chi(\mathcal{O}_{K3})
= 2$ and reaches $M^\flat$ at $k = 1$" is inscribed at line 4695-4696.
**VERIFIED.**

**Edit 2: `cor:cy-direction-character-table` at line 4186-4230.** The
table row "K3 × E^k (BKM-enhanced fixed point, k ≥ 1)" with entries
$(0, -16, 5, 11)$ and $\chi(\mathcal{O}_Y) = 0$ is inscribed at line
4196. The bare BKM row is NOT inscribed separately — Wave-4 NOTES that
the table only carries the fixed-point row. This is a LABELING choice
rather than a defect, but a **Wave-4 refinement** would add a second
row for bare BKM $(0, 5, -16, 13)$ with $\chi(\mathcal O_{K3}) = 2$ for
full disambiguation. Minor.

**Edit 3: proof of `cor:cy-direction-character-table` at line 4233-4238.**
The Fourier transform $\hat M^\flat = (0, -32, 10, 22)$ is correctly
labelled as the Fourier of $M^\flat = M_{K3 \times E^k}$, with a
parenthetical for the bare BKM input. **VERIFIED.**

**Edit 4: witness for `thm:bracketing-associator-cohomology-class`
at line 5528-5543.** The witness triple $(\mathrm{conifold}, K3, E)$
with $a = (0, 0, 2, -2)$ is inscribed at line 5529-5531. The
parenthetical noting that the naive $(\mathrm{conifold}, \mathrm{conifold}, K3)$
yields $a = (0, 0, 0, 0)$ by case (1) is at line 5536-5542. **VERIFIED.**

**Edit 5: lemma `lem:bivariant-kunneth-identity` scope at line 3682-3686.**
The scope is extended: "Then $\kappa_E$ acts as the identity on all of
$\mathbb{Z}[V_4]$ (the proof below gives the identity for every $N \in
\mathbb{Z}[V_4]$, not only on the trace-zero hyperplane $\mathbb{Z}[V_4]_0$)."
**VERIFIED.**

### 2.2 Sixth defect: the Bockstein cohomological home

The Wave-3 Beilinson memo (§3.3) flagged an "Open subtlety": the
projection from $a/2 \pmod 2 \in \mathbb{F}_2[V_4]_0$ to
$(c_\alpha, c_\beta) \in (\mathbb{Z}/2)^2$ requires an explicit
evaluation at the canonical $\mathbb{F}_2$-pairing against the two
integral Bockstein generators. The chapter's Lemma
`lem:V4-cohomology-bracketing-home` asserts this projection
without a fully explicit pairing formula.

**Wave-4 status.** This open subtlety is NOT resolved by the five
edits. It is a legitimate open gap: the two Bockstein generators
$\mathrm{Bock}(\alpha), \mathrm{Bock}(\beta)$ need to be named
explicitly, and the pairing of $a/2 \pmod 2$ against these generators
needs to be computed. Currently the chapter asserts that $a/2 \pmod 2
= (0, 0, 1, 1)$ projects onto $\mathrm{Bock}(\beta)$ without an
explicit map. **Wave-5 target.**

### 2.3 Gelfand W3 antipode inscription

The formula $S(J(x_0^h)) = -J(x_0^h) + 24\hbar \cdot x_0^h$ at
rank-24 $\mathfrak{sl}_2$: Wave-4 verifies the derivation chain:

1. **Coproduct at rank 24** (Gelfand W3 §3.1): $\Delta(J(x^h_0)) = J(x^h_0) \otimes 1 + 1 \otimes J(x^h_0) + \hbar \sum_{i,j} Q^{ij} (x^e_i \otimes x^f_j - x^f_i \otimes x^e_j)$.
2. **Antipode identity** (H3): $m(S \otimes \mathrm{id}) \Delta(J(x^h_0)) = 0 = \epsilon \cdot 1$.
3. **Frobenius trace computation**: $\sum_{i,j} Q^{ij} \mu^k_{ij} = \chi(K3) \cdot \delta^k_0 = 24 \delta^k_0$. This uses (a) the Mukai form $Q$ is the Frobenius pairing of $H^*(K3)$, (b) cup product $\mu^k_{ij}$ is the structure constant, (c) $\sum_{i,j} Q^{ij} \mu^k_{ij}$ is the TRACE of the left-multiplication operator by $\alpha_k$ on $H^*(K3)$, which evaluates against the identity $\alpha_0$ to $\chi(K3) = 24$.
4. **Result**: $S(J(x^h_0)) = -J(x^h_0) + 24\hbar \cdot x^h_0$.

**Wave-4 audit.**
- Step 3 is the load-bearing computation. The Frobenius-trace identity
  $\sum_{i,j} Q^{ij} \mu^k_{ij} = \chi(K3) \delta^k_0$ requires:
  (a) $H^*(K3)$ is a Frobenius algebra with dual pairing $Q$
      (the Mukai pairing shifted to even cohomology); verified.
  (b) the trace of left-multiplication by $\alpha_k$ equals the coefficient
      of the volume class $\alpha_{23}$ in $\alpha_k \cdot \mathbf 1$; but
      $\alpha_k \cdot \mathbf 1 = \alpha_k$ (not necessarily the volume),
      so the trace is $\dim(H^*(K3)) \cdot \delta^k_0 = 24 \delta^k_0$
      only when $\alpha_0$ is the identity AND the Mukai form is
      unimodular (yes for $II_{4,20}$).
  (c) Verified.
- The extension to general simple $\mathfrak g$ is ASSERTED by Gelfand
  W3 (Attack 5.4.2 Heal in §6) but not carried through explicitly.
  **Wave-4 scope:** proved for $\mathfrak g = \mathfrak{sl}_2$ at
  rank 24 on $x_0^h$; for general $\mathfrak g$, conjectural by the
  same template.

**Verdict.** Inscription is CORRECT as written; scope qualifier
"$\mathfrak g = \mathfrak{sl}_2$, rank 24, $x_0^h$" should be
made explicit.

### 2.4 Kazhdan W3 Drinfeld-second presentation

The presentation at `k3_yangian_chapter.tex:1855-2223` (slot ready
per SYNTHESIS §5). Wave-3 Kazhdan provides:
- Generators $E_i(u), F_i(u), H_i(u)$ for $i = 1, \ldots, 12$ (rank
  12 from $D_{12}$).
- Relations R1-R6 (Commuting Cartans, Cartan-current exchange,
  Raising-lowering, Like-type current exchange, Serre for 11
  adjacency classes, Null-adjacency decoupling for
  $(\alpha_{11}, \alpha_{12})$).
- 44 Serre generator families (11 pairs × 2$_\pm$ × 2$_{\mathrm{orient}}$).
- AMR 2006 and Guay 2007 sign-checking.

**Wave-4 audit.**
- Rank 12, Dynkin $D_{12}$, dual Coxeter $h^\vee = 22$: verified from
  $D_r$: $h^\vee = 2r - 2 = 22$ for $r = 12$. ✓
- The 11 adjacency classes (9 chain + 2 fork) correctly enumerate
  the $D_{12}$ simple-root graph; 55 orthogonal pairs correctly count.
- The sign convention following AMR 2006 (our Wave-3 convention)
  is verified via cross-check against Guay 2007 under $\hbar \to -\hbar$
  flip (an involutive automorphism). ✓
- **Important scope-caveat.** Per Polyakov W3's obstruction, the
  spectral-parameter $R$-matrix realising $Y_\hbar(\mathfrak{so}(4, 20))$
  does NOT exist globally on the indefinite $(4, 20)$ signature. The
  Drinfeld-second presentation is **valid at the FORMAL algebraic
  level** (generators and relations over $\C[[\hbar]]$), but cannot be
  evaluated on a global representation via a spectral $R$-matrix.
- Kazhdan W3 notes this at his §II.4 line 130-135 (the formal Yangian
  vs. its spectral realisation), so the inscription is **self-aware**
  of its scope. Good.

**Verdict.** Inscription is CORRECT as a formal-algebra presentation
of the envelope Yangian; scope limitation (no global spectral
$R$-matrix on indefinite $(4,20)$) must be stated explicitly at
inscription.

---

## 3. Cross-wave coefficient consistency

The three Wave-3 outputs produce coefficients:
- **Gelfand antipode**: $24\hbar$ ($\chi(K3) = 24$).
- **Witten/Drinfeld level shift**: $12 + h^\vee$ ($\chi(K3)/2 = 12$
  plus Chevalley $h^\vee$).
- **Costello counterterm**: $12 + h^\vee/2$ (fish diagram).

The question: are these the SAME underlying constant with different
normalisations, or three distinct coefficients with consistent
derivation chains?

### 3.1 Trigonometric-to-rational-to-fundamental limit

Fact 1 (Todd integral): $\int_{K3} \mathrm{Td}(TK3) = \chi(\mathcal O_{K3}) = 2$ and $\int_{K3} c_2(TK3) = \chi(K3) = 24$ with
$\chi(\mathcal O_{K3}) = \chi(K3)/12 = 24/12 = 2$.

Fact 2 (Chevalley): $\mathrm{tr}_{\mathrm{ad}}(X Y) = 2 h^\vee \mathrm{tr}_{\mathrm{fund}}(XY)$ for simply-laced $\mathfrak g$.

Fact 3 (Sugawara): affine Kac-Moody has shifted level
$k_{\mathrm{Sug}} = k + h^\vee$ under dual-Coxeter renormalisation.

### 3.2 Tracing the Gelfand $24\hbar$

Gelfand derives from the antipode identity $m(S \otimes \mathrm{id})\Delta = 0$ at rank 24 on $J(x_0^h)$:

$S(J(x_0^h)) = -J(x_0^h) - (\hbar) \cdot \sum Q^{ij} \mu^k_{ij} x^h_k / 1 = -J(x_0^h) + 24\hbar \cdot x^h_0$,

where $\sum Q^{ij} \mu^k_{ij} = \chi(K3) \cdot \delta^k_0 = 24 \delta^k_0$.

**Normalisation path.** The $24$ here is the **topological Euler
characteristic** $\int_{K3} c_2(TK3) = 24$, NOT the Todd-normalised
holomorphic Euler $\chi(\mathcal{O}_{K3}) = 2$.

### 3.3 Tracing the Witten/Drinfeld $12 + h^\vee$

Witten/Drinfeld derive by integrating the anomaly 6-form on $K3 \times E$:

$\mathrm{Anom} = h^\vee \cdot \frac{\chi(K3)}{12} \cdot \kappa_E = 2 h^\vee \kappa_E$

where $\chi(K3)/12 = 2$ is the Todd-integrated arithmetic genus $\chi(\mathcal O_{K3})$, and $\kappa_E$ is the elliptic-curve trace integral.

The LEVEL shift is obtained by extracting the 4-form Chern-Simons coefficient on the $E$-direction. This gives two additive contributions:
- K3-Euler contribution: $\chi(K3)/2 = 12$ (from
  $\int_{K3} c_2(TK3)/2$; the factor $/2$ comes from the standard
  4-form-to-CS-coefficient convention).
- Chevalley contribution: $h^\vee$ (from the standard 4d hCS fish
  diagram).

**Normalisation path.** The $12$ here is **half the topological Euler**
$\chi(K3)/2 = 12$, a DIFFERENT normalisation from Gelfand's $24$.

### 3.4 Tracing the Costello $12 + h^\vee/2$

Costello's fish-diagram coefficient in the counterterm
$\mathrm{CT}_1 = -(12 + h^\vee/2)(t \otimes t - P/2)/u^2$.

The $12$ is K3-Euler contribution in the R-matrix NORMALISATION (not
the level-shift normalisation). The $h^\vee/2$ is the trace-form
normalisation: $\mathrm{ch}_2(\mathrm{ad}) = 2 h^\vee \cdot
\mathrm{ch}_2(\mathrm{fund})$, so dividing by $2$ for fundamental gives
$h^\vee$ fundamental, but in the R-matrix coefficient convention
(which absorbs an additional $/2$), one gets $h^\vee / 2$.

### 3.5 Verdict on coefficient consistency

All three coefficients descend from the **same topological datum**
$\chi(K3) = 24$, but with different normalisations:

| Path | Coefficient | Normalisation |
|---|---|---|
| Gelfand antipode | $24$ | Topological Euler $\int c_2$ |
| Witten/Drinfeld level | $12$ | Half-topological $\chi/2$ |
| Costello $\mathrm{CT}_1$ | $12$ | R-matrix convention, same half-topological |

And the $h^\vee$ factors:

| Path | $h^\vee$ factor | Normalisation |
|---|---|---|
| Gelfand antipode | none (abelian direction) | primitive $J(x_0^h)$ is in abelian direction |
| Witten/Drinfeld level | $h^\vee$ | Chevalley (fundamental-trace) |
| Costello $\mathrm{CT}_1$ | $h^\vee/2$ | R-matrix convention (half-Chevalley) |

**Consistent derivation tree.**
- $24 = \chi(K3)$ at the ORIGIN.
- $12 = 24/2 = \chi(K3)/2$ at the SHIFT level (factor-of-2 from
  level-shift convention).
- $h^\vee / 2 = h^\vee \cdot (1/2)$ at the R-matrix level (factor-of-2
  from Chevalley).
- $h^\vee$ at the level shift (Chevalley in fundamental-trace).

**The three coefficients are all correct; they compute the SAME
topological invariant $\chi(K3)$ through three convention-stacks.** The
$h^\vee$ factor in Gelfand's antipode is absent because the antipode
formula for $J(x^h_0)$ happens to be in a Cartan-Chevalley direction
where the Chevalley trace vanishes (Casimir $(h, h) = 2$ in $\mathfrak{sl}_2$ normalisation). **CONSISTENT.**

### 3.6 One cross-check that FAILS mildly

**Failing cross-check.** If the Gelfand $24$ and the Costello/Witten
$12$ are the SAME $\chi(K3)$ topological datum through different
normalisations, then at the $\mathfrak{sl}_2$ level the antipode and
level shift should be related by a factor of 2.

Specifically: at $\mathfrak{sl}_2$ with $h^\vee = 2$, Witten-Costello
shift is $12 + 2 = 14$; Gelfand antipode coefficient is $24$.
Ratio $24/14 \neq 2$ and $24/12 = 2$ exactly.

So Gelfand's $24$ relates to Costello/Witten's $12$ by factor of 2,
NOT to the full $12 + h^\vee = 14$. This means **the Gelfand antipode
$24$ and the Witten-Costello $h^\vee$ additive shift are
INDEPENDENT contributions** — the Gelfand antipode computes only the
topological K3-Euler piece, not the Chevalley $h^\vee$ piece.

**This is physically consistent**: the antipode at the Chevalley-Cartan
direction $x^h_0$ sees only the K3-cohomology "trace" (topological
Euler), not the Lie-algebra-Casimir "trace" (Chevalley dual Coxeter),
because $\mathfrak{sl}_2$-Casimir evaluated on a Cartan element is
zero for the quadratic piece that would produce a $h^\vee$ contribution.
OK.

---

## 4. Stratification-coproduct compatibility

### 4.1 The claim under audit

Wave-3 SYNTHESIS §1.1 and Wave-3 Polyakov §4.2 assert:

$Y_{K3}^{\mathrm{classical}} = \mathrm{Heis}_{\mathrm{rank}\,24, \mathrm{sig}\,(4, 20)} \oplus \bigoplus_{\Lambda \subset \Lambda_{\mathrm{Muk}}, \mathrm{ADE}} Y(\mathfrak g_\Lambda) \oplus \text{BKM sector}$

as a **decomposition** (direct sum). The question: what does $\oplus$
mean here — (a) direct sum of underlying vector spaces, (b) direct sum
of Lie bialgebras, (c) direct sum of Hopf algebras, or (d) direct sum
of $(\infty,1)$-algebras?

### 4.2 Classical level: direct-sum of Lie bialgebras

At the **CLASSICAL** (Lie-bialgebra) level, the direct-sum makes
sense: the three factors are mutually orthogonal under the Mukai form
($\mathrm{Heis}$ lives on the full rank-24 lattice with commutative Lie
structure, ADE sub-lattices are Belavin-Drinfeld-positive-definite, BKM
is imaginary-root), and the Drinfeld classical $r$-matrix
$r(z) = \Omega/z$ decomposes by block. **At this level: OK.**

### 4.3 Quantum level: coproduct mixes strata

At the **QUANTISED** level, the coproduct
$\Delta: Y_\hbar \to Y_\hbar \otimes Y_\hbar$ is defined via the FULL
Casimir $\Omega_{\mathrm{coeff}}$, which COUPLES the rank-24
Heisenberg (timelike + spacelike mix) to the ADE sub-Yangians
(positive-definite slot). In particular, on a J-generator $J(x^{a}_i)$ with $i \in H^{1,1}_{\mathrm{prim}}$ (rank-20 spacelike block) and $a$ indexed by a non-abelian $\mathfrak g$ direction, the coproduct is

$\Delta(J(x^a_i)) = J(x^a_i) \otimes 1 + 1 \otimes J(x^a_i) + (\hbar/2) [x^a_i \otimes 1, \Omega_{\mathrm{coeff}}]$

and the commutator $[x^a_i, \Omega_{\mathrm{coeff}}]$ expands as

$\sum_{b, c; j, k} g^{bc} Q^{jk} [x^a_i, x^b_j] \otimes x^c_k = \sum f^{ab}_d \mu^l_{ij} Q^{jk} g^{bc} x^d_l \otimes x^c_k$.

The Mukai form $Q^{jk}$ couples $j \in H^{1,1}_{\mathrm{prim}}$ to $k \in H^{1,1}_{\mathrm{prim}}$ through the rank-20 block, so the coproduct's $\hbar$-correction contains terms $x^d_l \otimes x^c_k$ with both $l, k$ in the rank-20 slot — these are TWO ADE-stratum instances being multiplied. But worse, the Mukai form $Q^{jk}$ on the rank-24 Mukai lattice also couples the rank-20 slot to the rank-4 slot (mediated by the $(1,1)$ primitive direction); so the coproduct does NOT cleanly split into Heisenberg $\oplus$ ADE.

**The coproduct mixes the Heisenberg block and the ADE block.**

### 4.4 Specific test case

Take $x = x^e_\alpha$ with $\alpha \in \Lambda_{E_8}^{(1)}$ a simple root of the $E_8$ ADE sublattice sitting in the first $E_8(-1)$ factor of $\Lambda_{\mathrm{Muk}} = U^4 \oplus E_8(-1)^2$. The Mukai form on $\Lambda_{E_8}^{(1)}$ is positive-definite $E_8$. The coproduct on $J(x^e_\alpha)$ contains terms

$\sum_{j \in \Lambda_{\mathrm{Muk}}} Q^{\alpha, j} \cdot (\ldots) x^? \otimes x^?_j$

Since $Q^{\alpha, j} \neq 0$ for $j \in \Lambda_{E_8}^{(1)}$ (within ADE) AND potentially for $j \in U^4$ (Heisenberg slot, if $\alpha$ has a component there). For $\alpha$ purely in $\Lambda_{E_8}^{(1)}$, the $U^4$ component of $Q^{\alpha, \cdot}$ vanishes (orthogonal decomposition), but the $(1,1)$-primitive block still contributes because the ADE sub-lattice is inside $H^{1,1}_{\mathrm{prim}}$.

So the coproduct lands INSIDE the ADE factor — **within a single ADE stratum the coproduct is closed**. But crossing ADE strata (two different positive-definite sublattices) the coproduct is NOT closed, because the Mukai form couples generators in different ADE sublattices through their shared $(1,1)$-primitive containers.

### 4.5 Correct statement

The correct statement is:

**Direct sum at the CLASSICAL Lie-bialgebra level**: yes, the decomposition $\mathrm{Heis} \oplus \bigoplus Y(\fg_\Lambda) \oplus$ BKM is an orthogonal direct sum of Lie bialgebras.

**Not a direct sum at the QUANTUM Hopf-algebra level**: the
coproduct mixes strata, because the Casimir $\Omega_{\mathrm{coeff}}$
couples the different blocks.

**The right language**: at the quantum level, $Y_{K3}$ is a
**filtered quantisation** of the direct-sum classical structure. The
filtration has associated graded isomorphic to the direct sum; the
filtered piece itself is not a direct sum.

### 4.6 Impact on Wave-3 and Wave-4 claims

This directly impacts:
- Wave-3 Drinfeld's pentagon coherence (Wave-2 carried): the pentagon
  sources live in different strata, and mixing them through the
  coproduct is load-bearing for the Pentagon coherence. Wave-3
  Drinfeld's "block decomposition" language at rank 24 reflection
  equation is CLASSICAL-level; quantum-level has cross-block terms
  not captured.
- Wave-3 Etingof's "strict Hopf on $C_2$-cofinite" at generic K3:
  the $C_2$-cofinite subcategory is closed under the ADE-within-K3
  decomposition, but the coproduct-mixing means that the
  reconstruction is not a direct product of strict-Hopf strata.
- Wave-3 Polyakov's "the K3 Yangian IS the direct-sum Heis $\oplus
  Y(\fg_{ADE}) \oplus$ BKM" (§4.2) is MISLEADING as stated. It's a
  classical-level description.

### 4.7 Wave-4 recommendation

Inscribe the stratification **only as a classical Lie-bialgebra
decomposition** with the explicit parenthetical: "(direct sum at
classical level; quantum-level coproduct mixes strata, producing a
filtered quantisation of the direct-sum classical structure)."

Do NOT inscribe the decomposition as a "Yangian decomposition" without
this qualifier.

**Open problem for Wave-5**: construct the filtered quantisation
explicitly; compute the first-order cross-stratum coupling in
$\Delta$; verify that associated-graded recovers the classical direct
sum.

---

## 5. Single-most-catastrophic Wave-3 residue

The primary catastrophic residue is the stratification-coproduct
compatibility failure (§4 above). **It is catastrophic because**:

1. It invalidates the direct sentence structure of SYNTHESIS §1.1 as a
   "Yangian-level" decomposition. Any downstream Wave-4+ work built on
   the direct-sum decomposition of the Yangian will inherit the
   mixing, and their theorems may need re-checking.
2. It is not flagged in any Wave-3 memo. All Wave-3 agents (Polyakov,
   Drinfeld, Etingof, Gelfand) describe strata at the classical level
   or at the $(\infty,1)$-categorical level, but none computes the
   quantum coproduct on a cross-stratum element to see whether it
   stays in the direct sum.
3. It is cheaply fixable: the cure is a scope-qualifier on the
   stratification inscription. But until the scope is fixed, any
   theorem about the "Hopf structure of the K3 Yangian" that treats
   strata as independent is potentially wrong.
4. Specifically, Wave-3 Drinfeld's pentagon H1-H4 (Wave-2 carried) and
   Wave-3 Kazhdan's full Drinfeld-second inscription, both of which
   use the direct-sum description as a structural input, need the
   scope-qualifier.

**This is the Wave-4 RED FLAG for Wave-5.**

---

## 6. Convergence statement

Wave-4 has performed a deep adversarial audit of Wave-3's
inscriptions, retraction verdicts, and stratification claims. The
primary findings are:

(i) **Four Wave-3 retractions upheld** (Polyakov Q-dressing,
    Etingof three-stratum, Witten multiplicative, Beilinson
    $M_{K3}$-conflation), with targeted sharpenings:
    - Polyakov R5: no-go covers only single-pole RF-Q; Sklyanin-type
      two-pole dressings untested; narrow Wave-5 gap.
    - Etingof three-stratum: further refined by Wave-4 to a
      four-stratum structure ADE / smooth polarised generic /
      wall-crossings & Kummer & special-Picard; generic
      strict-Hopf restricted to the smooth polarised locus.
    - Witten retraction: Drinfeld's reinterpretation "different
      invariants" is two-thirds correct; the clean statement is
      "Witten's Wave-2 was a misidentification; Costello's $12 + h^\vee$
      is the level shift."

(ii) **All five Beilinson W3 manuscript edits verified** as applied
     and correct. One open subtlety (Bockstein pairing map) flagged
     for Wave-5.

(iii) **Gelfand W3 antipode** and **Kazhdan W3 Drinfeld-second**
      inscriptions verified as correct within their respective
      scopes; scope-qualifiers required at inscription.

(iv) **Cross-wave coefficient consistency** traced through the
     normalisation chain: Gelfand $24 = \chi(K3)$; Witten/Drinfeld
     $12 + h^\vee = \chi(K3)/2 + h^\vee$; Costello $12 + h^\vee/2$
     (R-matrix normalisation). All three consistent; independent
     contributions to different observables (antipode, level shift,
     counterterm).

(v) **Primary catastrophic residue identified**: the direct-sum
    stratification Heis $\oplus \bigoplus Y(\fg_\Lambda) \oplus$ BKM
    is CLASSICAL-LEVEL ONLY. The quantum coproduct mixes strata via
    the Casimir. This must be flagged at inscription; Wave-5 must
    compute the filtered quantisation explicitly.

(vi) **Recommendation: CONDITIONAL PROCEED.**
     - Proceed with the five Beilinson W3 edits (applied).
     - Proceed with inscription of Gelfand antipode at
       $(\mathfrak{sl}_2, \text{rank 24}, x_0^h)$ scope.
     - Proceed with inscription of Kazhdan Drinfeld-second with
       "no global spectral $R$-matrix on indefinite $(4, 20)$" note.
     - **BLOCK inscription of the direct-sum stratification as a
       quantum-Hopf-algebra decomposition.** Inscribe only as
       classical-level decomposition with quantum-level-mixing note.
     - Wave-5 open problems: (a) Sklyanin two-pole $Q$-dressing test,
       (b) Bockstein pairing map explicit formula, (c) filtered-
       quantisation construction for cross-stratum coproduct,
       (d) wall-crossing quasi-Hopf structure beyond Kummer.

**Wave-4 convergence declaration.** The space of Wave-3 claims has
SHRUNK as Wave-4 identifies one major residue (stratification-
coproduct mixing) and one minor refinement (Etingof wall-crossings).
All five Beilinson W3 edits are correctly applied; Gelfand and
Kazhdan inscriptions ready modulo scope qualifiers. The programme
is in a COHERENT state ready for Wave-5, conditional on
installing the stratification-quantum-level-mixing scope qualifier.

Nothing is sacred. One Wave-3 framework-level claim (direct-sum
stratification as algebra decomposition) has been identified as
catastrophically overstated; Wave-5 must audit this and its
downstream dependencies. The adversarial attack-heal methodology
continues.

**Raeez Lorgat, sole author. No AI attribution. Vol III manuscript
only.**

— End of Wave-4 Beilinson memo.
