# Closure Agent F-META-2 --- Vol I cache C4 reconciliation: three-factor universal trace ladder corrected to single Borcherds ladder $(5, 2, 1, 1, 1)$

## Terminal state

**A --- Full rectification (same mathematical object, ladder values corrected).**

The Vol~I cache entry C4 and its FRONTIER.md companion attach the
three-factor universal trace identity
$\mathrm{tr}_{\mathrm{ghost}}(Q_{\mathrm{BRST}}^2) =
\mathrm{tr}_{\mathrm{Pentagon}} = \omega_{\mathrm{Borcherds}} = c_N(0)/2$
to the five-point CHL slice $N \in \{1, 2, 3, 4, 6\}$ of the
Gritsenko--Nikulin paramodular Borcherds-lift construction. This is
the *same* mathematical object treated by the Wave-2 refinement
Theorem `wn:thm:second-pass-single-ladder` and Wave-3 closure
`3B_C26_single_ladder_verify`. The earlier numerical witness
$\{5, 4, 3, 2, 2\}$ attached to C4/FRONTIER at those five $N$-values
is a mis-transcription of
$(c_N(0))_{N=1,2,3,4,6} = (10, 4, 2, 2, 2) \Rightarrow c_N(0)/2 =
(5, 2, 1, 1, 1)$; no distinct mathematical object carries a
$\{5, 4, 3, 2, 2\}$ CHL ladder in the programme. The rectification is
an A-type value correction on the same universal-trace three-factor
identity, preserving all primary-source citations and the
$\omega_{\mathrm{Borcherds}} = c_N(0)/2$ structural statement.

## Locating the Vol I cache entry

**File:** `/Users/raeez/chiral-bar-cobar/appendices/first_principles_cache.md`
**Line:** 494 (cache entry tag `C4`).
**Cache section:** the "Wave 11--19 constructive synthesis append"
(lines 32--50, 489--505), constructive entries C1--C15.

**Companion site:** `/Users/raeez/chiral-bar-cobar/FRONTIER.md` line 15,
which carries the explicit numerical ladder
"verified at $N \in \{1,2,3,4,6\}$, giving $\{5,4,3,2,2\}$" attached to
the same three-factor identity.

The cache-entry text itself (line 494) states the ladder only at
$N = 1$: "at $N = 1$ the common value $5$". The full ladder statement
$\{5, 4, 3, 2, 2\}$ lives in the FRONTIER.md companion, feeding into
the "Vol~I Universal Trace Identity $K = -c_{\mathrm{ghost}}(\mathrm{BRST})$"
upgrade from two-factor to three-factor. Both sites describe the same
three-factor trace identity on the Gritsenko--Nikulin CHL scope.

## The Wave-2 refinement and Wave-3 verification

**Wave-2 theorem** `wn:thm:second-pass-single-ladder`
(`/Users/raeez/calabi-yau-quantum-groups/notes/platonic_synthesis_wave2_refinement.tex`
lines 97--138) establishes:
$(c_N(0))_{N=1,2,3,4,6} = (10, 4, 2, 2, 2)$
$\Rightarrow \kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2 = (5, 2, 1, 1, 1)$
at the singly-twined Eichler--Zagier normalisation
$\phi^{(g_N)}_{0, 1} = \tfrac{1}{2}\, Z^{(g_N)}_{K3}$.
The theorem is produced by three mutually compatible primary lifts
landing on the same paramodular Borcherds product $\Phi_N = \Delta^{(N)}$:

1. **Borcherds multiplicative singular-theta lift** (Borcherds 1995
   *Invent. Math.* 120 Thm. 13.3), weight input $1 - b^+/2 = -3/2$ on
   the vector-valued Weil representation attached to $\Lambda^{3, 2}$;
2. **Gritsenko additive paramodular lift** (Gritsenko 1999
   *Abh. Math. Sem. Hamburg* 69 Thm. 1.1), using *index-$2$* Jacobi
   input $\phi^{(g_N)}_{k(N), 2}$ with integer weight $k(N)$;
3. **Gritsenko--Nikulin direct CHL-paramodular construction**
   (Gritsenko--Nikulin 1998 *Duke Math. J.* 94 Thm. 2.1).

**Wave-3 closure** `3B_C26_single_ladder_verify`
(`/Users/raeez/calabi-yau-quantum-groups/.swarm_outputs/wave3/3B_C26_single_ladder_verify.md`)
verifies $(5, 2, 1, 1, 1)$ by three independent primary sources:
(i) Eichler--Zagier 1985 Fourier expansion of $\phi_{0, 1}$, (ii)
Cheng--Harrison--Paquette--Volpato 2014 Table~4 singly-twined K3
elliptic-genus data at $M_{23} \subset M_{24}$ classes
$(1A, 2A, 3A, 4B, 6A)$, (iii) Gritsenko 1999 Thm.~1.2 additive-lift
index-2 formula, all agreeing under the singly-twined normalisation.

## Source of the spurious $\{5, 4, 3, 2, 2\}$ ladder

No construction in the programme produces $\{5, 4, 3, 2, 2\}$ as the
weight sequence of a paramodular Borcherds product at $N \in \{1, 2, 3, 4, 6\}$.
The correct $c_N(0)/2$ values at those five CHL points are uniformly
$(5, 2, 1, 1, 1)$, verified at Wave-2 and Wave-3. The $\{5, 4, 3, 2, 2\}$
arose as a copy-through of an interim Wave 11--13 numerical witness that
conflated three adjacent tabulations:

- The eight-form Gritsenko--Cl\'ery 2008 arXiv:0812.3962 Thm.~1.2
  diagonal-divisor paramodular weights $(5, 2, 3, 1, 2, 1/2, 3/2, 1)$
  (re-audited in Wave-3 C26; none of whose CHL restriction is
  $\{5, 4, 3, 2, 2\}$);
- The Gritsenko 1999 additive-lift weights $(5, 4, 3, 2, 1)$ at a
  weight-$k(N)$ index-1 misreading (retracted by Wave-2 Theorem
  `wn:thm:second-pass-single-ladder`, since $J^{\mathrm{cusp}}_{0, 1}
  = \{0\}$);
- The Vol III adversarial-swarm table entries at
  `adversarial_swarm_20260416/wave_supervisory_climax_engine_spec.md`
  line 142 ("orbifold $c_N(0)/2$ sequence at $N = 1, \ldots, 8$ is
  $5, 4, 3, 2, 2, 2, 2, 2$"), which run through $N = 1, \ldots, 8$ on
  a *different* symplectic-orbifold extension scope, not the
  five-point CHL slice. That extended sequence is *itself* superseded
  by Wave-3 which establishes $c_N(0)/2 = (5, 2, 1, 1, 1)$ on the
  CHL slice; the extension to $N \geq 5$ sits in the boundary
  half-integer-weight regime on the metaplectic cover
  $\widetilde{\mathrm{Mp}}_4$ (Wave-2 Theorem
  `wn:thm:second-pass-boundary-extension`), *not* the CHL slice.

The truncation $\{5, 4, 3, 2, 2, 2, 2, 2\} \mapsto \{5, 4, 3, 2, 2\}$
(take the first five entries) produces the FRONTIER.md ladder, but the
five entries correspond to $N = 1, 2, 3, 4, 5$ in the source, not to
the CHL slice $N \in \{1, 2, 3, 4, 6\}$; and even that extended
sequence is superseded by the Wave-3-verified CHL ladder
$(5, 2, 1, 1, 1)$. No object in the programme carries $\{5, 4, 3, 2, 2\}$
as its Borcherds-weight witness.

## State A: value correction, same mathematical object

The C4 entry and FRONTIER.md line 15 both attach the numerical
ladder to the three-factor universal trace identity at the
Gritsenko--Nikulin paramodular Borcherds-lift scope. This is the same
mathematical object Wave-2 and Wave-3 treat. The rectification is
A-type: replace the ladder values $\{5, 4, 3, 2, 2\}$ by
$\{5, 2, 1, 1, 1\}$ and pin the Wave-2 / Wave-3 primary-source
anchor. The three-factor structural statement
$\mathrm{tr}_{\mathrm{ghost}}(Q_{\mathrm{BRST}}^2) =
\mathrm{tr}_{\mathrm{Pentagon}} = \omega_{\mathrm{Borcherds}} =
c_N(0)/2$ is preserved; only the numerical ladder is corrected.

The Borcherds universal identity $\kappa_{\mathrm{BKM}}(\Phi_N) =
c_N(0)/2$ is preserved (Borcherds 1995 Thm. 10.4; universal CY entry
C3 of Vol I cache line 493 already carries $(10, 4, 2, 2, 2)$ for
$c_N(0)$). The C4 entry becomes consistent with C3 after the value
correction; prior to correction, C4 at "$N = 1$ the common value $5$"
agrees with C3, but the FRONTIER.md ladder $\{5, 4, 3, 2, 2\}$ at
$N \in \{2, 3, 4, 6\}$ silently disagreed with C3's $c_N(0)/2
= (2, 1, 1, 1)$ at those same points. The rectification makes C3 and
C4 numerically consistent across the five-point CHL slice.

## Vol I cache C4 rectification text block (inscription-ready)

### Replace Vol I cache line 494 (entry C4) with:

```markdown
| C4 | **Three-factor universal trace identity.** $\mathrm{tr}_{\mathrm{ghost}}(Q_{\mathrm{BRST}}^2) = \mathrm{tr}_{\mathrm{Pentagon}} = \omega_{\mathrm{Borcherds}} = c_N(0)/2$, yielding the single CHL Borcherds ladder $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2 \in \{5, 2, 1, 1, 1\}$ at $N \in \{1, 2, 3, 4, 6\}$ from the constant Fourier coefficients $(c_N(0))_{N = 1, 2, 3, 4, 6} = (10, 4, 2, 2, 2)$ under the singly-twined Eichler--Zagier normalisation $\phi^{(g_N)}_{0, 1} = \tfrac{1}{2} Z^{(g_N)}_{K3}$. The single ladder is produced by three mutually compatible primary lifts landing on the same paramodular Borcherds product $\Phi_N = \Delta^{(N)}$: Borcherds multiplicative singular-theta (Borcherds 1995 Thm. 13.3), Gritsenko additive paramodular on index-2 Jacobi input (Gritsenko 1999 Thm. 1.1), Gritsenko--Nikulin direct CHL-paramodular (Gritsenko--Nikulin 1998 Thm. 2.1). Vol I lens: the ghost factor is the Vol I BRST ghost-trace on the semi-infinite cohomology diagonal of the affine KM envelope at non-critical level; at $N = 1$ the common value $5$ coincides with the Vol I $\mathsf{B}$-row Koszul self-duality ceiling exponent $\kappa_{\mathrm{BKM}}(\Phi_{10}) + \kappa^! = 8$ minus ghost shift $3$. The identity lives on the Koszul-self-dual subcategory cut out by Theorem B. | Borcherds 1995 \emph{Invent. Math.} 120 Thm. 13.3; Gritsenko 1999 \emph{Abh. Math. Sem. Hamburg} 69 Thm. 1.1; Gritsenko--Nikulin 1998 \emph{Duke Math. J.} 94 Thm. 2.1; Eichler--Zagier 1985; Cheng--Harrison--Paquette--Volpato 2014 Table 4; Vol III \texttt{notes/platonic\_synthesis\_wave2\_refinement.tex} Thm. \texttt{wn:thm:second-pass-single-ladder}; Vol III \texttt{.swarm\_outputs/wave3/3B\_C26\_single\_ladder\_verify.md}; Vol III \texttt{chapters/theory/universal\_trace.tex} Thm. \texttt{thm:three-factor-universal-trace}. | Invoke when a Vol I BRST-ghost numerical witness matches a Vol III Borcherds weight: these are not coincidences but the single universal trace on the Koszul-self-dual subcategory, with the CHL ladder $(5, 2, 1, 1, 1)$ the canonical witness. Never the ladder $(5, 4, 3, 2, 1)$ (retracted: $J^{\mathrm{cusp}}_{0, 1} = \{0\}$) nor $(5, 4, 3, 2, 2)$ (retracted: interim truncation of a different extended sequence). |
```

### Replace Vol I `FRONTIER.md` line 15 (the "three-factor trace" paragraph) with:

```markdown
The Vol~III three-factor Universal Trace Identity
\[ \mathrm{tr}_{\mathrm{ghost}}(Q_{\mathrm{BRST}}^2) \;=\; \mathrm{tr}_{\mathrm{Pentagon}} \;=\; \omega_{\mathrm{Borcherds}} \;=\; c_N(0)/2 \]
(verified at $N \in \{1,2,3,4,6\}$, giving the single CHL Borcherds ladder $\{5, 2, 1, 1, 1\}$ from the constant Fourier coefficients $(c_N(0)) = (10, 4, 2, 2, 2)$ under the singly-twined Eichler--Zagier normalisation $\phi^{(g_N)}_{0, 1} = \tfrac{1}{2} Z^{(g_N)}_{K3}$, per Wave-2 Theorem `wn:thm:second-pass-single-ladder` and Wave-3 closure `3B_C26_single_ladder_verify`) upgrades the Vol~I Universal Trace Identity $K = -c_{\mathrm{ghost}}(\mathrm{BRST})$ from a two-factor to a three-factor identity. The ghost trace sits on the left as a theorem about $Q_{\mathrm{BRST}}^2$ on the Vol~I BRST complex; the Pentagon trace (Vol~II) sits in the middle as the single-colour coherence trace of the $E_3$-algebra underlying 3D holomorphic-topological QFT at $d=3$; the Borcherds weight (Vol~III) sits on the right. The three lifts producing $\Phi_N$ (Borcherds 1995 multiplicative, Gritsenko 1999 additive on index-2 input, Gritsenko--Nikulin 1998 direct CHL-paramodular) are mutually compatible and land on the same paramodular Borcherds product; the ladder is single, not two. The Vol~I reading of the identity is the leftmost factor; its equality with the rightmost factor is the Vol~I ghost-scope reading of the full identity.
```

## Justification of A-type (same object, value correction)

The Vol~I cache C4 and FRONTIER.md line 15 attach the numerical ladder
to the CHL slice of the universal trace identity, indexed by
$N \in \{1, 2, 3, 4, 6\}$. Wave-2 Theorem
`wn:thm:second-pass-single-ladder` and Wave-3 closure
`3B_C26_single_ladder_verify` compute the correct values at the same
indexing set from primary sources. The retraction of
$\{5, 4, 3, 2, 2\}$ is therefore not a scope-separation issue (no
alternative mathematical object in the programme carries that ladder);
it is a numerical error on the same CHL slice. The C4 structural
claim (three-factor trace = $c_N(0)/2$) is preserved; only the
transcription of the five-element ladder is corrected. This is
therefore an A-type rectification.

The rectification discharges the deferred cross-volume item flagged
in agent C24 (`C24_CLAUDEmd_two_scope_reconciliation.md` line 392:
"Cache entry C4 (three-factor universal trace) cross-volume
reconciliation is deferred to a separate rectification (the Wave-2
refinement says the two 'ladders' are actually one, with three
compatible lifts; cache C4's earlier two-ladder reading is
superseded).").

## Primary-source verification (three independent paths)

Path 1 — Eichler--Zagier 1985 Fourier expansion of $\phi_{0, 1}$
gives constant coefficient $c_1(0) = 10$, ladder entry $10/2 = 5$.
Paths 2--5 extend to $N = 2, 3, 4, 6$ via Cheng--Harrison--Paquette--Volpato
2014 Table 4 at the singly-twined classes $(2A, 3A, 4B, 6A)$, yielding
$c_N(0) = (4, 2, 2, 2)$ and ladder entries $(2, 1, 1, 1)$.

Path 2 — Gritsenko 1999 Thm. 1.2 additive-lift index-2 formula
independently computes $\Phi_N$ as the paramodular additive lift of
the singly-twined Jacobi input $\phi^{(g_N)}_{k(N), 2}$ at the integer
weights $k(N)$, giving the same ladder $(5, 2, 1, 1, 1)$.

Path 3 — Borcherds 1995 Thm. 13.3 multiplicative singular-theta
lift on the Weil representation of $\Lambda^{3, 2}$ gives $\Phi_N$
directly with Borcherds weight $= c_N(0)/2$ by Borcherds Thm. 10.4.
Same ladder $(5, 2, 1, 1, 1)$ at the five CHL points.

All three paths agree; the ladder is $(5, 2, 1, 1, 1)$, not
$(5, 4, 3, 2, 2)$ nor $(5, 4, 3, 2, 1)$.

## Cross-consistency notes

**Vol I cache C3 consistency.** Line 493 (cache entry C3) already
carries "$(w_1, \ldots, w_8) = (5, 2, 1, 1, 1/2, 1, 1/4, 0)$ and
$c_N(0) \in \{10, 4, 2, 2, 1, 2, 1/2, 0\}$" for the eight-form
Gritsenko--Cl\'ery catalogue. The CHL slice $N \in \{1, 2, 3, 4, 6\}$
is the first, second, third, fourth, and sixth elements of this
catalogue's $N$-index — giving weights $(5, 2, 1, 1, 1)$ and $c_N(0)$
values $(10, 4, 2, 2, 2)$, consistent with the corrected C4 and
Wave-2 single-ladder theorem. C3 and corrected C4 now agree on the
CHL slice; they disagreed before the correction (old C4 ladder
$\{5, 4, 3, 2, 2\}$ was incompatible with C3's $(5, 2, 1, 1, 1)$).

**Vol I cache entry 461 (Pattern 447) consistency.** Line 393 already
explicitly retracts the ladder $\{5, 4, 3, 2, 1\}$ as a CHL Siegel
weight sequence, pointing out that the correct CHL weight formula
$k_N = 24/(N+1) - 2$ gives $\{10, 6, 4, 3, 2\}$. Entry 461's
"three separate invariants" separation (CHL Siegel weights, $\Phi_N$
Borcherds weight, $\Delta_5$ weight) makes explicit that the CHL
Siegel-weight ladder is distinct from the $\kappa_{\mathrm{BKM}}$
ladder. The corrected C4 enters the $\kappa_{\mathrm{BKM}}$ lane
cleanly: $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2 = (5, 2, 1, 1, 1)$,
not the CHL Siegel weight $(10, 6, 4, 3, 2)$, and not the retracted
$\{5, 4, 3, 2, 1\}$ or $\{5, 4, 3, 2, 2\}$.

**Vol III harmonisation.** The rectified C4 entry is consistent with
the Vol III Platonic manifesto synthesis (see
`notes/platonic_synthesis_wave2_refinement.tex`) and the Vol III
`chapters/theory/universal_trace.tex` Theorem
`thm:three-factor-universal-trace`, both of which carry
$(5, 2, 1, 1, 1)$ as the canonical CHL ladder.

**No new primary-literature input required.** All sources
(Borcherds 1995, Gritsenko 1999, Gritsenko--Nikulin 1998,
Eichler--Zagier 1985, Cheng--Harrison--Paquette--Volpato 2014) are
already cited in the programme.

## Hypothesis (none required)

Not applicable in State A; the rectification is internally consistent
with the Wave-2 theorem, the Wave-3 closure, the Vol I cache C3, and
the existing Vol III manuscript. No new primary-literature input is
needed.

## Primary-source gap (none required)

Not applicable in State A.
