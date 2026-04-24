# Agent B2: quantum CE/bar integration audit

Date: 2026-04-24.

Scope:

```text
chapters/theory/cy3_chain_level_bridge.tex
notes/adversarial_swarm_20260424_total_resolution/agent_A2_quantum_ce_bar.md
```

No manuscript source was edited.

## Verdict

The main quantum BV-renormalised many-variable CE/bar integration is
correctly typed and conditional.  In the integrated block
`def:cy3-hcs-quantum-observables` through
`cor:cy3-quantum-bar-hall-conditional`, no theorem says
`Obs^q = Obs^cl[[\hbar]]`.  The quantum theorem is conditional on the
exact missing data identified by A2: Costello--Gwilliam/Costello--Li
renormalisation, anomaly cancellation, strict continuous completions,
a BV-to-bar transfer, and continuous loop coderivations
`D_r` forming
`D_B^\hbar=d_B+\sum_{r\geq 1}\hbar^rD_r`.

There is, however, a separate RED finding later in the same chapter:
the C3 and K3xE Hall-comparison sections still claim proved
chain-level hCS-to-Hall maps.  Those statements are not consequences of
the B2 quantum CE/bar theorem and conflict with the A1/A2 obstruction
analysis unless they are made conditional on a supplied local oriented
`Theta_{\hCS\to\Hall}` datum satisfying the full Cech/Ran obstruction
equations.

## Checks Passed

1. Quantum observables are not the classical CE complex with formal
   power series adjoined.

   Anchor:
   `chapters/theory/cy3_chain_level_bridge.tex:73`.

   The definition uses the Costello--Gwilliam renormalised local/multilocal
   functional space and the differential

   ```tex
   Q_{\hCS}+\{I[L],-\}_{\BV}+\hbar\Delta_L
   ```

   at `cy3_chain_level_bridge.tex:80-86`, and it states that the QME is
   part of the anomaly-cancellation hypothesis at
   `cy3_chain_level_bridge.tex:92-101`.  This is not
   `\Obs_{\cC}^{\mathrm{cl}}[[\hbar]]`.

2. The many-variable classical CE/bar proposition remains classical.

   Anchor:
   `chapters/theory/cy3_chain_level_bridge.tex:221`.

   The proposition identifies

   ```tex
   \Obs_{\cC}^{\mathrm{cl}}(P)
   \simeq
   \left(B_{E_3}U^{\mathrm{fact},E_3}_P(\mathfrak L_{\cC})\right)^\vee_b
   ```

   at `cy3_chain_level_bridge.tex:241-250`, and explicitly says that it
   does not construct the Hall comparison at
   `cy3_chain_level_bridge.tex:252-255`.

3. The quantum BV/bar theorem has the right hypotheses.

   Anchor:
   `chapters/theory/cy3_chain_level_bridge.tex:296`.

   The theorem assumes:

   - Stage-1 `E_3` formality and a Costello--Li holomorphic witness:
     `cy3_chain_level_bridge.tex:303-305`.
   - Costello--Gwilliam/Costello--Li renormalisation data satisfying RG
     flow and QME: `cy3_chain_level_bridge.tex:306-308`.
   - vanishing or counterterm cancellation of the Costello--Li quartic
     anomaly: `cy3_chain_level_bridge.tex:309-312`.
   - strict LF/DFS continuity of renormalised Feynman operations:
     `cy3_chain_level_bridge.tex:313-315`.
   - a continuous BV-to-bar transfer `T_L`:
     `cy3_chain_level_bridge.tex:316-324`.
   - continuous coderivations `D_r` with `(D_B^\hbar)^2=0`, and
     conjugation to the renormalised BV differential:
     `cy3_chain_level_bridge.tex:325-334`.

   The conclusion is therefore a conditional quasi-isomorphism with the
   deformed quantum bar coalgebra
   `B_{E_3}^{\hbar}:=(B_{E_3},D_B^\hbar)`, not the undeformed classical
   bar object tensored with `[[\hbar]]`; see
   `cy3_chain_level_bridge.tex:336-352`.

4. The proof keeps the transfer assumption visible.

   Anchor:
   `chapters/theory/cy3_chain_level_bridge.tex:355`.

   The proof says the transfer `T_L` transports the renormalised BV
   differential to the completed bar coalgebra and that assumption (vi)
   is exactly the statement that the transported differential is
   `D_B^\hbar`; see `cy3_chain_level_bridge.tex:356-368`.

5. The Hall corollary remains conditional on `Theta`.

   Anchor:
   `chapters/theory/cy3_chain_level_bridge.tex:371`.

   The corollary assumes the quantum BV/bar theorem and, in addition, an
   oriented hCS-to-Hall comparison on the DWR Cech/Ran nerve whose
   obstruction tuple vanishes; see
   `cy3_chain_level_bridge.tex:373-382`.  Its proof identifies the Hall
   arrow as the supplied oriented comparison datum, not something
   produced by CE/bar; see `cy3_chain_level_bridge.tex:401-409`.

6. A2 report and integrated theorem agree in substance.

   Anchors:
   `agent_A2_quantum_ce_bar.md:28-70`,
   `agent_A2_quantum_ce_bar.md:74-95`,
   `agent_A2_quantum_ce_bar.md:276-345`,
   `agent_A2_quantum_ce_bar.md:347-384`.

   The report correctly says that the quantum theorem is not obtained by
   adding `[[\hbar]]`, identifies the missing coderivations `D_r`, gives
   the conditional theorem now present in the chapter, and keeps Hall
   conditional on the oriented comparison map.

## Findings

### RED-1: later C3 Hall comparison overclaims the A2/A1 gate

Anchor:
`chapters/theory/cy3_chain_level_bridge.tex:2013`.

The theorem `thm:r6-quad-equivalence-c3` is marked
`\ClaimStatusProvedHere{}` at `cy3_chain_level_bridge.tex:2015` and
asserts a pentagon containing

```tex
\Theta_{\hCS\to\Hall}^{\C^3}\colon
(\mathrm B)\to(\mathrm H)
```

at `cy3_chain_level_bridge.tex:2021-2023`.  It further states

```tex
H^\bullet(\Obs_{\hCS}^{q}(\C^3;\ghat))\cong
Y^+(\ghat)\cong\CoHA(\C^3)
```

at `cy3_chain_level_bridge.tex:2027-2030`.

The proof tries to build the Hall edge by BV-equivariant localisation
and a Nakajima pullback at `cy3_chain_level_bridge.tex:2090-2150`.
This does not supply the oriented critical-CoHA datum of
`def:cy3-oriented-hcs-hall-comparison-datum`, nor does it prove the
five obstruction classes of `def:hcs-hall-descent-obstruction` vanish
on the DWR Cech/Ran nerve.  It is therefore outside what the B2 quantum
CE/bar theorem can justify.

Minimal repair:

```diff
-\begin{theorem}[Five-way quasi-isomorphism on $\C^3$]
+\begin{theorem}[Conditional five-way comparison on $\C^3$]
 \label{thm:r6-quad-equivalence-c3}
-\ClaimStatusProvedHere{}
+\ClaimStatusConditional{} \textup{(conditional on
+Theorem~\ref{thm:cy3-quantum-bv-bar-conditional} and a supplied local
+oriented comparison datum
+$\Theta_{\hCS\to\Hall}^{\C^3}$ satisfying
+Definition~\ref{def:cy3-oriented-hcs-hall-comparison-datum})}
```

The proof should then be rewritten as a construction of finite
cohomological evidence for the local Hall edge, plus a conditional
transport statement once the oriented `Theta` datum has been supplied.

### RED-2: the C3 problem-closure remark is false as written

Anchor:
`chapters/theory/cy3_chain_level_bridge.tex:2177`.

The remark `rem:r6-op-closed-at-c3` is marked
`\ClaimStatusProvedHere{}` at `cy3_chain_level_bridge.tex:2179` and says
that Theorem `thm:r6-quad-equivalence-c3` "closes" the hCS-to-Hall
problem at the affine toric base case; see
`cy3_chain_level_bridge.tex:2180-2195`.

After A1 and A2, this is too strong.  The C3 computations may be
evidence for a local normal form, but the explicit chain-level
quasi-isomorphism

```tex
\Obs_{\hCS}^{q}(\C^3;\ghat)
\to
\CoHA_{\mathrm{crit}}^{\mathrm{or}}(\C^3)
```

still requires the quantum BV transfer, the oriented Hall comparison,
and the obstruction-vanishing data.

Minimal repair:

```diff
-\begin{remark}[Base-case resolution of Problem~\ref{op:cy3-hcs-hall-comparison}]
+\begin{remark}[Base-case reduction of Problem~\ref{op:cy3-hcs-hall-comparison}]
 \label{rem:r6-op-closed-at-c3}
-\ClaimStatusProvedHere{}
-Theorem~\ref{thm:r6-quad-equivalence-c3} closes
+Assuming the local oriented comparison datum required in
+Theorem~\ref{thm:r6-quad-equivalence-c3}, the $\C^3$ chart reduces
```

Replace "is an explicit chain-level quasi-isomorphism" by "is the
expected local normal form of the supplied comparison datum".

### RED-3: the BV bracket reconciliation assumes the missing `Theta`

Anchor:
`chapters/theory/cy3_chain_level_bridge.tex:2198`.

The proposition `prop:r6-convolution-vs-bv-bracket` is marked
`\ClaimStatusProvedHere{}` and says the BV bracket and Nakajima
convolution are intertwined by
`\Theta^{\C^3}_{\hCS\to\Hall}` up to a Costello--Li chain homotopy;
see `cy3_chain_level_bridge.tex:2200-2211`.

This is at best a conditional compatibility once the local comparison
map and the homotopy have been constructed in the same renormalised
continuous category as Theorem `thm:cy3-quantum-bv-bar-conditional`.

Minimal repair:

```diff
-\ClaimStatusProvedHere{}
+\ClaimStatusConditional{} \textup{(conditional on the supplied
+local comparison map
+$\Theta_{\hCS\to\Hall}^{\C^3}$ and a continuous Costello--Li
+BV-to-Hall homotopy)}
```

### RED-4: K3xE gluing inherits the unproved C3 Hall edge

Anchor:
`chapters/theory/cy3_chain_level_bridge.tex:2396`.

The theorem `thm:r6-k3e-local-chart-qiso-inscribed` is formally
conditional on a DWR cover and abelian gauge, but it also states that
the chartwise quasi-isomorphisms are "obtained by"
`thm:r6-quad-equivalence-c3`, and that all five obstruction classes
vanish; see `cy3_chain_level_bridge.tex:2400-2420`.

The proof kills `o_{\mathrm{MC}}` by appealing to the C3 pentagon and
restriction compatibility at `cy3_chain_level_bridge.tex:2427-2432`.
That does not prove the Cech/Ran Maurer--Cartan equation for a
chartwise family on K3xE.  It assumes the missing chartwise maps and
their overlap coherences.

Minimal repair:

```diff
-\ClaimStatusConditional{} \textup{(conditional on the DWR cover of
-Definition~\ref{def:r6-dwr-cover-k3e-inscribed} and abelian $\ghat$)}
+\ClaimStatusConditional{} \textup{(conditional on the DWR cover of
+Definition~\ref{def:r6-dwr-cover-k3e-inscribed}, abelian $\ghat$,
+the local oriented comparison data
+$\{\Theta_i\}$, and vanishing of the full obstruction tuple
+$\mathfrak o(\{\Theta_i\})$)}
```

The conclusion should be phrased as an application of
`thm:hcs-hall-descent-criterion`, not as a proof of the obstruction
vanishing.

### RED-5: the seven-condition status remark advertises closure

Anchor:
`chapters/theory/cy3_chain_level_bridge.tex:2479`.

The remark `rem:r6-seven-conditions-status` is marked
`\ClaimStatusProvedHere{}` and says all seven conditions hold on the DWR
cover; see `cy3_chain_level_bridge.tex:2482-2508`.  That outruns the
conditional Hall corollary at `cy3_chain_level_bridge.tex:371-410`.

Minimal repair:

```diff
-\ClaimStatusProvedHere{}
+\ClaimStatusConditional{} \textup{(conditional on
+Theorem~\ref{thm:r6-k3e-local-chart-qiso-inscribed} after its full
+Theta-obstruction hypotheses are included)}
```

Replace "All seven conditions hold" by "Under those hypotheses, the
seven conditions reduce to the listed checks."

## Minor Note-Only Drift

The A2 report quotes the pre-repair quantum source with
`\mathcal O(\cE_{\hCS,c})[[\hbar]]` at
`agent_A2_quantum_ce_bar.md:31-38` and again at
`agent_A2_quantum_ce_bar.md:99-111`.  The manuscript has already been
sharpened to
`\mathcal O_{\mathrm{ren,loc/multiloc}}` at
`cy3_chain_level_bridge.tex:80-91`.  This is not a mathematical defect
in the manuscript; it is only stale wording in the historical A2 report.

Optional note-only repair:

```diff
-    \mathcal O(\cE_{\hCS,c}(U,\mathfrak g))[[\hbar]],
+    \mathcal O_{\mathrm{ren,loc/multiloc}}
+    (\cE_{\hCS,c}(U,\mathfrak g))[[\hbar]],
```

## Integration Recommendation

Keep the B2 quantum theorem and the Hall corollary as integrated:

- `def:cy3-hcs-quantum-observables`:
  `cy3_chain_level_bridge.tex:73-103`.
- `prop:cy3-continuous-e3-bar-ce`:
  `cy3_chain_level_bridge.tex:221-255`.
- `thm:cy3-quantum-bv-bar-conditional`:
  `cy3_chain_level_bridge.tex:296-352`.
- `cor:cy3-quantum-bar-hall-conditional`:
  `cy3_chain_level_bridge.tex:371-410`.

Patch the later C3/K3xE Hall-comparison material before using it as a
theorem dependency.  The true surviving structure is:

```text
quantum CE/bar comparison
  = conditional source-side theorem

Hall comparison
  = separate oriented Theta datum with obstruction vanishing

C3 and K3xE Hall claims
  = conditional applications once that Theta datum and its coherences
    are supplied
```

## Verification Performed

Text audit only.  Commands used:

```bash
rg -n -F '[[\hbar]]' \
  chapters/theory/cy3_chain_level_bridge.tex \
  notes/adversarial_swarm_20260424_total_resolution/agent_A2_quantum_ce_bar.md

rg -n -F 'Obs_{\hCS}^{q}' chapters/theory/cy3_chain_level_bridge.tex

rg -n 'label\{(thm:cy3-quantum-bv-bar-conditional|cor:cy3-quantum-bar-hall-conditional|op:cy3-hcs-hall-comparison|def:hcs-hall-descent-obstruction|thm:hcs-hall-descent-criterion)\}' \
  chapters/theory/cy3_chain_level_bridge.tex
```

No tests or LaTeX build were run, because this was a no-edit text
integration audit.
