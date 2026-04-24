# Agent 13: Cross-Volume Coherence Attack-Heal

Date: 2026-04-24.

Scope: Vol I master synthesis, Vol I body anchors, Vol II manifesto, and the Vol III architecture/body files named in the assignment. Report-only. No commits. No manuscript edits.

## Verdict

The three-volume spine is mostly coherent after the recent rectifications, but seven scope collisions remain worth fixing. The load-bearing bridge is:

\[
\Phi_d^{(\Sigma_{d-1},C)}=\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C}\circ \Phi^{\mathrm{FA}}_d,
\qquad
\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2,
\qquad
\Phi_{10}=\Delta_5^2.
\]

At \(K3\times E\), the canonical total-space spectrum is
\[
\{\kappa_{\mathrm{cat}}(K3\times E)=0,\;\kappa_{\mathrm{ch}}^{\mathrm{Heis}}=3,\;\kappa_{\mathrm{BKM}}(\Delta_5)=5,\;\kappa_{\mathrm{fiber}}=24\}.
\]
The fibre value \(\chi(\mathcal O_{K3})=2\) is valid only as \(\kappa_{\mathrm{cat}}^{K3\text{-fiber}}\), not as the total-space \(K3\times E\) invariant.

## ATTACK_1: \(\Phi_2(K3)\) is sent directly to \(\mathbf H_{\Delta_5}\)

Anchors:
- Vol III body: `chapters/theory/cy_to_chiral.tex:9501` correctly says \(\Phi_2\) sends K3 to the Mukai-lattice chiral algebra, while \(\Phi_3\) is only a framed object-level assignment.
- Vol III body: `chapters/theory/cy_to_chiral.tex:9510-9514` then says \(\Phi(D^b\mathrm{Coh}(K3))\simeq \mathbf H_{\Delta_5}\text{-mod}^{ch}\).
- Vol III body: `chapters/theory/cy_to_chiral.tex:9574-9583` gives the correct bridge: \(\Phi_2(D^b\mathrm{Coh}(K3))=\mathcal H_{\mathrm{Muk}}\), and \(\Psi\) sends the Siegel-Borcherds input to \(\mathbf H_{\Delta_5}\).

Failure mode: direct \(\Phi_2\)-to-BKM conflates the CY-to-chiral output with the Borcherds pushforward / \(\Psi\)-extension.

HEAL_1:
Replace the line at `cy_to_chiral.tex:9513` by:
\[
\Phi_2(D^b\mathrm{Coh}(K3))\simeq \mathcal H_{\mathrm{Muk}},
\qquad
\Psi(\mathrm{II}_{3,2},\phi_{K3})\simeq \mathbf H_{\Delta_5}.
\]
Then state that \(\mathbf H_{\Delta_5}\)-modules are reached through the Borcherds pushforward \(\Phi_*^{\mathrm{Borch}}\), not by the raw \(\Phi_2\) functor.

## ATTACK_2: \(\Phi_3(K3\times E)=\mathbf H_{\Delta_5}\) is too strong

Anchors:
- Vol III six routes: `chapters/examples/cy_c_six_routes_convergence.tex:15-18`, `29-37`, `45-65` state that only R1 is a direct \(\Phi_3\) application; R2--R6 are independent constructions and comparison maps are CY-C content.
- Vol III theorem: `chapters/theory/cy_to_chiral.tex:720-727` gives a conditional comparison target \(\SpCh_{K3,E}(\PhiFA_3(\mathrm{Perf}(K3\times E)))\simeq U_{\mathrm{ch}}(\mathfrak g_{\Delta_5})\), conditional on hCS-to-Hall and Hall-Borcherds comparison.
- Vol III remark: `chapters/theory/cy_to_chiral.tex:9670-9677` writes \(\Phi_3^{(K3,E)}(K3\times E)=\mathbf H_{\Delta_5}\) on the banded framed locus.

Failure mode: the equality sign hides the conditional comparison and reads as a literal functor-output theorem.

HEAL_2:
Change the banding remark to:
\[
\SpCh_{K3,E}\bigl(\PhiFA_3(\mathrm{Perf}(K3\times E))\bigr)
\;\xrightarrow[\mathrm{cond.}]{\sim}\; U_{\mathrm{ch}}(\mathfrak g_{\Delta_5})
\]
as a \(\mu_8\)-banded comparison on the framed locus, with the same hypotheses as `thm:g-delta5-is-sp-k3`. Do not call R2--R6 \(\Phi_3\)-outputs; call them conjectural alternative stage-2 comparisons.

## ATTACK_3: \(\Phi_{10}\) and \(\Delta_5\) are still mixed at one point

Anchors:
- Correct normalization: `chapters/theory/cy_to_chiral.tex:10671-10679` says \(\Delta_5\) has \(c(0)=10\), \(\kappa_{\mathrm{BKM}}(\Delta_5)=5\), while \(\Phi_{10}=\Delta_5^2\) has weight \(10\).
- Correct verification: `chapters/connections/cy_holographic_datum_master.tex:359-375` says the factor \(2\) is squaring, not Serre duality.
- Bad line: `chapters/examples/cy_c_six_routes_convergence.tex:1820` says \(\kappa_{\mathrm{BKM}}(\Phi_{10})=c_1(0)/2=5\).

Failure mode: if the input is \(\Phi_{10}\), the weight is \(10\); if the invariant is \(5\), the named form is \(\Delta_5\).

HEAL_3:
At `cy_c_six_routes_convergence.tex:1820`, write:
\[
\kappa_{\mathrm{BKM}}(\Delta_5)=c_1(0)/2=5,
\qquad
\mathrm{wt}(\Phi_{10})=10=2\,\kappa_{\mathrm{BKM}}(\Delta_5).
\]
The later sentence about \(1/\Phi_{10}\) as the AdS\(_3\) counting denominator can remain.

## ATTACK_4: \(K\), \(K^\kappa\), and \(\kappa_{\mathrm{BKM}}\) are overloaded

Anchors:
- Vol I master: `MASTER...md:26` writes \(\hbar^2\cdot K^{\kappa_{\mathrm{ch}}}=-1\).
- Vol I master: `MASTER...md:214-218` uses \(\hbar^2K=-1\), \(K=2c_+(L)\), and separately the trace value \(c_N(0)/2\).
- Vol III synthesis: `VOL_III...md:149-152` says \(K(A_{X_N})=c_N(0)=2\kappa_{\mathrm{BKM}}(\Phi_N)\) with values \(\{10,4,2,2,2\}\).
- Vol I master: `MASTER...md:663-665` also uses \(K=8=2c_+(\mathrm{II}_{4,20})\) in the universal trace identity.

Failure mode: \(K=8\) and \(K=c_N(0)\) cannot be the same unqualified \(K\). The first is the \(\mathsf B\)-row conductor \(K_{\mathrm{cond}}\); the second is a CHL value-level bridge \(K_{\mathrm{CHL},N}\).

HEAL_4:
Split notation:
\[
K_{\mathrm{cond}}(L)=2c_+(L),\qquad
K_{\mathsf B}=8\quad(L=\mathrm{II}_{4,20}),\qquad
K_{\mathrm{CHL},N}=c_N(0)=2\kappa_{\mathrm{BKM}}(\Phi_N).
\]
Then state the universal trace identity only as
\[
\hbar^2 K_{\mathrm{cond}}(L)=-1.
\]
Never write \(K\circ\Phi=\kappa_{\mathrm{ch}}\), and never use \(K^{\kappa_{\mathrm{ch}}}\) without defining it as a named conductor, not exponentiation.

## ATTACK_5: The \(K3\times E\) spectrum has two incompatible defaults

Anchors:
- Current Vol III body: `chapters/examples/cy_c_six_routes_convergence.tex:68-81` gives \(\{0,3,5,24\}\).
- Current Vol III body: `chapters/connections/cy_holographic_datum_master.tex:101-107` gives \(\{0,3,5,24\}\).
- Vol I master: `MASTER...md:723-725` gives \(\{0,3,5,24\}\).
- Post-adversarial synthesis: `notes/platonic_synthesis_post_adversarial.tex:748-790` gives \(\{2,3,5,24\}\) and calls the K3-fibre reading the default.

Failure mode: \(\kappa_{\mathrm{cat}}(K3\times E)=\chi(\mathcal O_{K3})\chi(\mathcal O_E)=2\cdot 0=0\). The value \(2\) is a fibre invariant.

HEAL_5:
Make the total-space row canonical everywhere:
\[
\mathrm{Spec}_{\kappa_\bullet}^{\mathrm{total}}(K3\times E)=\{0,3,5,24\}.
\]
If the fibre value is needed, write:
\[
\kappa_{\mathrm{cat}}^{K3\text{-fiber}}=2.
\]
Proposed edit: in `notes/platonic_synthesis_post_adversarial.tex:751-782`, change “On \(K3\times E\), the four modular-characteristic values \(\{2,3,5,24\}\)” to “The fibre-marked auxiliary reading is \(\{2,3,5,24\}\); the total-space \(K3\times E\) spectrum is \(\{0,3,5,24\}\).”

## ATTACK_6: Theorem B scope is not a single locus

Anchors:
- Vol I master: `MASTER...md:18` states Theorem B on \(U^{\mathrm{adm}}=\overline{\mathcal A_2}\setminus\bigcup_{n\ \mathrm{admissible}}H_n\).
- Vol I body: `theorem_B_scope_platonic.tex:1482-1509` states strict Theorem B on the complement of all admissible Humbert divisors.
- Vol I body: `theorem_B_scope_platonic.tex:2820-2893` gives the four-lane global theorem: strict on \(U^{\mathrm{adm}}\), weight-completed on formal neighbourhoods, \(A_\infty\)-corrected at walls, Cech-glued globally.
- Vol III synthesis: `VOL_III...md:187-193` distinguishes \(\mathcal U^{\mathrm{adm}}_{\mathrm{Hum},4}\), \(\mathcal U^{\mathrm{adm}}_{\mathrm{Hum},8}\), and \(\mathcal U^{\mathrm{adm}}_{\mathrm{at}}\subset X\).
- Vol III synthesis: `VOL_III...md:344-352` correctly says the four-climax equivalence is expected on the intersection locus and does not prove CY-C or arbitrary morphism functoriality.

Failure mode: using one symbol \(U^{\mathrm{adm}}\) for Humbert, Atiyah, and global Positselski scopes invites false implications.

HEAL_6:
Use three symbols:
\[
\mathcal U_{\mathrm{Hum},8}^{\mathrm{adm}}\subset\overline{\mathcal A_2},
\qquad
\mathcal U_{\mathrm{at}}^{\mathrm{adm}}(X)\subset X,
\qquad
\mathcal U_{\Phi_3}^{\mathrm{can}}(X)=\mathcal U_{\mathrm{at}}^{\mathrm{adm}}(X)\cap \mathcal P^{-1}(\mathcal U_{\mathrm{Hum},8}^{\mathrm{adm}}).
\]
Then state: strict Theorem B is a Vol I Humbert statement; Stage-1 canonicity is a Vol III Atiyah-Connes statement; their intersection gives the \(K3\times E\) framed locus.

## ATTACK_7: The eight-form spread has conflicting constants

Anchors:
- Vol II manifesto: `CLAUDE.md:494-503` gives weights \((5,2,1,1,1/2,1,1/4,0)\) and \(c_N(0)=(10,4,2,2,1,2,1/2,0)\).
- Vol III synthesis: `VOL_III...md:136-144` gives the same eight-form spread.
- Vol III connection chapter: `chapters/connections/cy_holographic_datum_master.tex:120-130` first says the full 8-form weights are \((5,4,3,2,2,1,1,1)\), then immediately distinguishes the correct twined family \((5,2,1,1,1/2,1,1/4,0)\).
- Vol I master: `MASTER...md:260` explicitly distinguishes programme \((5,4,3,2,1)\), twined \((5,2,1,1,1)\), physical CHL \((10,6,4,2,1,0)\), and Clery-Gritsenko eight-form \((5,2,1,1,1/2,1,1/4,0)\).

Failure mode: `cy_holographic_datum_master.tex:125-128` imports the programme ladder into the eight-form atlas.

HEAL_7:
Edit `cy_holographic_datum_master.tex:125-128` to:
“Full 8-form Gritsenko-Clery slice \(N\in\{1,\ldots,8\}\): weights \((5,2,1,1,1/2,1,1/4,0)\), zero-coefficients \((10,4,2,2,1,2,1/2,0)\), with integral / metaplectic / quarter-metaplectic / degenerate cover assignment.”
Keep the programme ladder \((5,4,3,2,1)\) only under the separate CHL-averaged family.

## ATTACK_8: The rearchitecture proposal overstates \(d=3\) as proved

Anchors:
- Rearchitecture: `notes/vol3_rearchitecture_proposal.tex:47-57` correctly says \(d=3\) is proved only on verified framed object-level loci, with arbitrary morphism functoriality and global \(G(\mathcal C)\) outside.
- Rearchitecture: `notes/vol3_rearchitecture_proposal.tex:813-818` later says CY-A\(_3\) and \(d=3\) change to PROVED.
- Vol III body: `chapters/theory/cy_to_chiral.tex:9501-9503` gives the correct scope.

Failure mode: roadmap language collapses object-level existence into full functoriality/global \(G\).

HEAL_8:
Replace “CY-A\(_3\): status changes from PROGRAMME to PROVED” with:
“CY-A\(_3\): framed object-level assignment proved on verified H1--H4 specialisation loci; arbitrary CY\(_3\) morphism functoriality and global \(G(\mathcal C)\) remain conjectural.”

## Proposed Manuscript Edits

1. `chapters/theory/cy_to_chiral.tex:9510-9514`: replace direct \(\Phi(D^b\mathrm{Coh}(K3))\to\mathbf H_{\Delta_5}\)-modules with \(\Phi_2\to\mathcal H_{\mathrm{Muk}}\), followed by \(\Psi/\Phi_*^{\mathrm{Borch}}\to\mathbf H_{\Delta_5}\).
2. `chapters/theory/cy_to_chiral.tex:9670-9677`: replace equality by conditional \(\mu_8\)-banded comparison, using the hypotheses of `thm:g-delta5-is-sp-k3`.
3. `chapters/examples/cy_c_six_routes_convergence.tex:1820`: replace \(\kappa_{\mathrm{BKM}}(\Phi_{10})=5\) with \(\kappa_{\mathrm{BKM}}(\Delta_5)=5\), and state \(\mathrm{wt}(\Phi_{10})=10\).
4. `notes/platonic_synthesis_post_adversarial.tex:748-790`: make \(\{0,3,5,24\}\) the total-space default; mark \(\{2,3,5,24\}\) fibre-marked.
5. `chapters/connections/cy_holographic_datum_master.tex:125-130`: correct the eight-form spread to \((5,2,1,1,1/2,1,1/4,0)\).
6. `notes/vol3_rearchitecture_proposal.tex:813-818`: replace “PROVED” with “proved object-level on verified framed loci; morphism/global \(G\) conjectural.”
7. Vol I master synthesis: split \(K_{\mathrm{cond}}\), \(K_{\mathsf B}\), and \(K_{\mathrm{CHL},N}\); remove unqualified \(K^{\kappa_{\mathrm{ch}}}\).

## Commands and Checks

Read/grep commands included:
- `git status --short`
- `sed -n` on `CLAUDE.md`, `~/ecosystem/INVARIANTS.md`, `~/ecosystem/AGENTS-HARNESS.md`, and the triggered skill files.
- `rg -n` over the named Vol III files, the Vol I master synthesis, Vol I theorem body anchors, and the Vol II manifesto for `Phi_3`, `Phi10`, `Delta_5`, `BKM`, `kappa`, `Theorem B`, `universal trace`, and `object-level`.
- `nl -ba ... | sed -n ...` for every local anchor cited above.

Executable check:

```bash
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider \
  compute/tests/test_k3e_yangian_phi3_identification.py \
  compute/tests/test_kappa_chart_gluing.py \
  compute/tests/test_genus2_chiral_partition.py
```

Result: `266 passed in 2.32s`.

No `make fast` run. No commit. No push. No destructive git.

## Open Obligations

1. Decide whether the public-facing Vol III manifesto should use four \(\kappa_\bullet\) invariants or five including \(\kappa_{\mathrm{ch,BV}}\). Current body can support five, but the canonical quick-reference still says four in some places.
2. Normalize notation for the CHL programme ladder versus twined / Gritsenko-Clery ladder. The formulas are known; the issue is naming.
3. Audit all occurrences of unqualified \(K\), \(K^\kappa\), and \(K^{\kappa_{\mathrm{ch}}}\) across Vol I/II/III before any next synthesis.
4. After the proposed manuscript edits land, run the targeted pytest command above and a session-end `make fast` only on user opt-in.
