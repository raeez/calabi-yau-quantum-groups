# Agent 15 -- Hostile synthesis / integration

Date: 2026-04-24.

Scope: synthesis of the holomorphic \(E_3\) adversarial reports for the
chain-level construction of the CY3 Stage-1 object, its chiral deformation
theory, and the chiral Gerstenhaber bracket.  Report only.  No manuscript
or compute file was edited.

## Evidence read

- Existing reports:
  `agent_01_gelfand_formal_moduli.md`,
  `agent_02_drinfeld_kazhdan_operads.md`,
  `agent_03_etingof_deformation_quantization.md`,
  `agent_04_beilinson_ran_descent.md`,
  `agent_05_costello_bv_hcs.md`,
  `agent_06_francis_gwilliam_factorization.md`,
  `agent_08_witten_polyakov_holography_qg.md`,
  `agent_09_gaiotto_defects_modules.md`,
  `agent_10_kapranov_manin_cyclic_ainf.md`,
  `agent_11_kontsevich_soibelman_hall.md`,
  `agent_12_topological_e3_trace.md`.
- Target chapters:
  `chapters/theory/cy3_chain_level_bridge.tex`,
  `chapters/theory/cy_to_chiral.tex`.
- Doctrine:
  `CLAUDE.md`, `AGENTS.md`,
  `.agents/skills/vol3-beilinson-loop/SKILL.md`,
  `.agents/skills/vol3-claim-verification/SKILL.md`.

## Verdict

The current left-end chapter is much healthier than the attack surface
that the first agents found.  It now has the right local objects:
compact-support hCS fields, quantum observables with QME, continuous
Dolbeault--chiral CE, the typed
\[
\PhiFA_3 \dashrightarrow \CoHA_{\mathrm{crit}}^{\mathrm{or}}
       \to Y^+ \to D(Y^+) \to \mathcal W_{1+\infty}
\]
chain, a quartic Costello--Li anomaly gate, and the statement that BV /
framed \(E_2\) does not itself manufacture \(E_3\).

The surviving danger is not a single false formula.  It is overpromotion
by transport: a correct local or finite-shadow theorem is moved into the
global holomorphic \(E_3\) theorem, the specialised \(E_1\) chiral output,
the Hall comparison, or the representation category without carrying the
missing datum.  The main integration owner should patch the remaining
wording so that every theorem states which datum is present.

## Surviving theorem spine

The theorem spine that survives attack is:

```tex
(\mathcal C,[\sigma_\mathcal C]\in HC^-_3(\mathcal C),F,\eta)
  --> \HH^\bullet(\mathcal C)_F in E_3-Alg
  --> \mathcal U^{FA}(\HH^\bullet(\mathcal C)_F) on R^3
  --> \PhiFA_3(\mathcal C)_F in E_3-HolFA(X)
  --> A_{\Sigma_2,C}=\SpCh_{\Sigma_2,C}(\PhiFA_3(\mathcal C)_F)
      in E_1-ChirAlg(C).
```

Here \(F\in\mathrm{Form}_3(\mathbb Q)\) is a chosen
\(\mathrm{GRT}_1(\mathbb Q)\)-torsor point and \(\eta\) is the
chain-level CY3 framing / Costello--Li witness.  Braces give the
Deligne--Tamarkin \(E_2\) cochain layer.  Cyclicity gives the
Tradler--Menichi--Ginzburg BV / homotopy framed-\(E_2\) layer.  The
actual \(E_3\) structure is the extra Stage-1 datum; it is not produced
by the BV operator.

The Hall branch survives only as a separate conditional map:

```tex
\Theta_{\hCS\to\Hall}^{or}:
  \Obs_{\hCS}^q(-,\mathfrak g)
  -> \CoHA_{\mathrm{crit}}^{or}(-)
```

in the oriented, completed Hall-valued factorisation-cosheaf category on
the full DWR Cech/Ran nerve.  The \(\mathbb C^3\) Hall core is
\(\CoHA(\mathbb C^3)=Y^+\).  The vertex algebra
\(\mathcal W_{1+\infty}\) appears only after Drinfeld doubling and
Fock/evaluation.

## ATTACK -> HEAL cycles

### Cycle 1 -- Stage-1 \(E_3\) versus specialised \(E_1\)

ATTACK.  Read \(B_{E_3}(A)\), \(\CE^{\mathrm{ch},E_3}\), or the
formal-moduli dgLa as attached to the final chiral algebra
\[
A=A_{\Sigma_2,C}=\Phi_3^{(\Sigma_2,C)}(\mathcal C).
\]

FAILURE MODE.  The final CY3 output is \(E_1\) by
`cy_to_chiral.tex:15-20`, `:278-284`, and `:5062-5071`.
The \(E_3\) bar in `cy3_chain_level_bridge.tex:139-142` is a local
Stage-1 object on \(\PhiFA_3(\mathcal C)|_P\), not the ordinary bar of
the specialised curve algebra after the Stage-1 datum has been forgotten.

HEAL.  Decorate all \(E_3\)-bar and \(E_3\)-CE notation by the retained
Stage-1 datum:
\[
B_{E_3,F,\eta}(\PhiFA_3(\mathcal C)|_P),\qquad
\CE^{\mathrm{ch},E_3}_{*,\mathrm{cont}}(\mathfrak L_{\mathcal C}(P)).
\]
The specialised algebra \(A_{\Sigma_2,C}\) has its \(E_1\)-bar unless the
text explicitly says that it is being considered together with
\((\PhiFA_3(\mathcal C)_F,\eta)\).

Patch targets:

- `cy3_chain_level_bridge.tex:139-142`: add `F,\eta` or a sentence after
  the display saying the \(E_3\)-bar is the retained Stage-1 bar, not the
  bar of a bare \(E_1\) curve algebra.
- `cy_to_chiral.tex:5075`: keep \(B^{E_1}(A_{\Sigma_2,C})\) as the
  specialised bar and refer any \(E_3\)-bar statement back to the
  retained Stage-1 object.

Status after heal: Stage-1 theorem conditional/definitional; final
chiral output theorem remains \(E_1\).

### Cycle 2 -- Torsor versus contractible canonicity

ATTACK.  Treat "pinned up to contractible choice" as a canonical
Stage-1 \(E_3\) structure, or treat the Costello--Li propagator as
unconditionally selecting the Kontsevich associator.

FAILURE MODE.  `cy_to_chiral.tex:325-347` correctly says the formality
space is a non-trivial \(\mathrm{GRT}_1(\mathbb Q)\)-torsor and
Stage-1 is pinned only after a torsor point is fixed.  This conflicts
with the looser "contractible choice" phrasing at
`cy_to_chiral.tex:22-24`, `:190-192`, `:221-223`, and `:260-268`, and
with `cy3_chain_level_bridge.tex:691-693`, `:717-721` if read as a
canonical graph-integral identification.

HEAL.  Use one formula everywhere:

```tex
After choosing a formality datum
\[
  F\in\mathrm{Form}_3(\mathbb Q),
  \qquad \mathrm{Form}_3(\mathbb Q)
  \text{ a free }\mathrm{GRT}_1(\mathbb Q)\text{-torsor},
\]
the remaining homotopies inside the chosen model are contractible.
Before \(F\) is fixed there is no canonical equality of Stage-1
\(E_3\)-models.
```

Patch targets:

- Replace "Stage 1 is pinned up to contractible choice" in
  `cy_to_chiral.tex:22-24`, `:190-192`, `:221-223`, `:260-268` by
  "after choosing the formality/associator datum; the residual homotopy
  space inside that chosen model is contractible".
- Replace `cy3_chain_level_bridge.tex:691-693` by a conditional
  sentence: the Costello--Li propagator may select a torsor point in a
  specified local graph-integral model; identifying it with the
  Kontsevich point is a separate graph-comparison assertion.
- Fix `cy_to_chiral.tex:342`: `\ClaimStatusProvedHereConditional`
  should be replaced by an existing status macro, preferably
  `\ClaimStatusConditional{}` or
  `\ClaimStatusProvedHere{}\textup{(conditional on the verified
  Stage-1 holomorphic locus)}`.

Status after heal: no fake canonical \(E_3\) object remains.

### Cycle 3 -- Toric Hall gluing versus hCS-to-Hall

ATTACK.  Use the toric chart theorem to say the hCS-to-critical-CoHA
comparison is proved.

FAILURE MODE.  `cy3_chain_level_bridge.tex:410-466` makes
\(\Theta_{\hCS\to\Hall}^{or}\) the first missing lemma.  Yet
`cy_to_chiral.tex:4125-4148` marks toric chart gluing
`\ClaimStatusProvedHere{}` and includes part (iv), "Costello--Li
comparison", as an unconditional quasi-isomorphism.  The later summary
at `cy_to_chiral.tex:5141` says toric chart gluing is conditional on the
oriented comparison data.  These two local surfaces disagree.

HEAL.  Split the theorem:

1. proved: toric Hall-side atlas, mutation equivalences, and Hall
   hocolim under explicit toric hypotheses;
2. conditional corollary: comparison with hCS / Costello--Li boundary
   algebra, assuming the oriented comparison data of
   `op:cy3-hcs-hall-comparison` or an explicitly named 5d boundary
   comparison theorem;
3. open: non-toric compact CY3 global hCS-to-Hall descent.

Patch targets:

- `cy_to_chiral.tex:4127`: downgrade theorem status to conditional, or
  split the theorem into a proved Hall-side theorem and a conditional
  Costello--Li comparison corollary.
- `cy_to_chiral.tex:4138-4146`: make part (iv) a separate conditional
  corollary depending on a DWR-level comparison map, not a component of
  the proved toric hocolim theorem.
- `cy_to_chiral.tex:5031`: replace "establishes the Costello--Li
  comparison" by "establishes the Hall-side hocolim; comparison with
  Costello--Li/hCS is conditional on the oriented comparison datum".
- `cy_to_chiral.tex:5163`: if the table keeps "Toric CY3 chart gluing:
  Proved", add a qualifier "Hall side only"; otherwise mark it
  "conditional with comparison".

Status after heal: \(\Theta_{\hCS\to\Hall}^{or}\) remains the frontier,
not a hidden theorem.

### Cycle 4 -- \(E_1\)-descent degeneration is too universal

ATTACK.  Infer
\[
E_2^{p,q}=0\quad(p\ge2)
\]
for every \(E_1\)-algebra Cech descent spectral sequence from the
contractibility of \(E_1\) operation spaces.

FAILURE MODE.  Contractible operation spaces remove operadic braiding
coherences; they do not annihilate ordinary Cech cohomology of an
arbitrary atlas.  `cy_to_chiral.tex:4333-4374` proves too much: strict
algebra maps plus a cocycle condition do not imply all higher Cech
groups vanish unless the atlas is finite, acyclic for the completed
complexes, and the diagram has the required exactness properties.

HEAL.  State the theorem on tested finite acyclic DWR/toric atlases:

```tex
For a finite DWR-good atlas whose completed observable/Hall complexes
are acyclic in Cech degree \(p\ge2\), and whose transition maps are
\(E_1\)-quasi-isomorphisms satisfying the mutation cocycle, the
descent spectral sequence degenerates at \(E_2\).
```

Patch targets:

- `cy_to_chiral.tex:4333-4347`: replace the universal theorem statement
  by a finite acyclic atlas theorem.
- `cy_to_chiral.tex:4368-4374`: replace "strict algebras imply
  vanishing" by "the chosen atlas is acyclic for this diagram; the
  tests compute that acyclicity for the standard toric atlases".
- `cy3_chain_level_bridge.tex:327-340`: if this proof still says
  "Weiss descent then identifies", add "after both assignments have been
  proved homotopy factorisation cosheaves on the chosen DWR-good atlas".

Status after heal: local-to-toric descent remains usable; no universal
descent theorem is smuggled in.

### Cycle 5 -- Braided representation category is mistyped

ATTACK.  Write
\[
\Rep^{E_2}(A_\mathcal C)\simeq
\mathcal Z(\Rep^{E_1}(A_\mathcal C))
\]
for a raw \(E_1\)-chiral algebra \(A_\mathcal C\).

FAILURE MODE.  `cy_to_chiral.tex:4115-4118` has this mistype.  The same
chapter has the correct formulation at `cy_to_chiral.tex:437-443`: the
braided category is the Drinfeld centre, equivalently the representation
category of the derived chiral centre.

HEAL.  Replace the raw \(A_\mathcal C\) in \(\Rep^{E_2}\) by the centre:

```tex
\[
 \mathcal Z\bigl(\Rep^{\Eone}(A_\mathcal C)\bigr)
 \;\simeq\;
 \Rep^{\Etwo}\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(A_\mathcal C)\bigr).
\]
```

Patch target:

- `cy_to_chiral.tex:4115-4118`.

Status after heal: no native \(E_2\) structure is assigned to the
specialised CY3 \(E_1\) algebra.

### Cycle 6 -- Chiral deformation dgLa is underspecified

ATTACK.  Let the finite vector-space count in the chiral deformation
stack stand as the formal moduli complex for the holomorphic \(E_3\)
Stage-1 object or for the specialised \(E_1\) chiral algebra.

FAILURE MODE.  `cy3_chain_level_bridge.tex:101-175` defines the local
CY3 object as completed continuous Dolbeault--jet CE.  The deformation
stack blocks at `cy_to_chiral.tex:5574-5588` and `:6024-6037` use
\(\ChirHoch^*(V,V)[1]\) but do not specify lambda powers, residue
conventions, translation covariance, completions, coefficients, or the
comparison between native \(E_3\) and specialised \(E_1\) deformation
complexes.  Finite Hom dimensions are useful toy shadows, not a proof
of chiral Gerstenhaber control.

HEAL.  Add a model qualifier and a completed dgLa:

```tex
\Def_{\mathrm{ch},E_1}(A)
  =
  \CHoch^\bullet_{\mathrm{ch},E_1}(A,A)[1],
\]
with chiral insertions, lambda-mode/residue convention, translation
covariance, and completed filtration fixed.  For the Stage-1 polydisc
object use
\[
  \Def_{\mathrm{CE}}^{\mathrm{ch,cont}}(P)
  =
  C^\bullet_{\mathrm{Lie,cont}}
  \bigl(\mathfrak L_\mathcal C(P),\mathfrak L_\mathcal C(P)\bigr)[s].
\]
The comparison between them is induced by
\(\SpCh_{\Sigma_2,C}\) and is extra data.
```

Patch targets:

- `cy_to_chiral.tex:5574-5588`: add "finite graded-vector-space model"
  and prevent the dimensions from being read as the completed chiral
  Hochschild dgLa.
- `cy_to_chiral.tex:6024-6037`: add lambda/residue/translation and
  completion conventions for \(L_V\).
- `cy3_chain_level_bridge.tex:101-175`: add a forward reference from the
  continuous CE definition to the deformation dgLa if the formal-moduli
  section will cite it.

Status after heal: formal deformation statements become typed; compute
CE shadows stop masquerading as full chiral Hochschild control.

### Cycle 7 -- Negative cyclic carrier versus raw Hochschild trace

ATTACK.  Treat the CY trace as a raw map \(\HH_d(\mathcal C)\to k\), or
identify Connes \(B\), the Tradler BV operator \(\Delta\), and the hCS BV
bracket.

FAILURE MODE.  `cy_to_chiral.tex:479` has the correct negative-cyclic
source definition.  But `cy_to_chiral.tex:147-160` and the hypotheses of
Theorem `thm:cy-to-chiral-d3` at `cy_to_chiral.tex:5053-5059` still read
primarily as a Serre pairing / Hochschild-shadow formulation.  Agent 10
found direct non-formal witnesses where cyclicity does not imply
termwise \([m_k,B^{(2)}]=0\).

HEAL.  The theorem hypotheses should name:

```tex
[\sigma_\mathcal C]\in HC^-_3(\mathcal C)
```

as the actual CY datum, with the Serre/Hochschild pairing as its shadow.
Reserve \(B\) for Connes-chain operators, \(\Delta\) for the
Tradler--Menichi cochain BV operator, and
\(\{-,-\}_{\BV}\) for the field-theoretic odd Poisson bracket.

Patch targets:

- `cy_to_chiral.tex:147-160`: replace "The trace is a map
  \(\HH_d(\mathcal C)\to\mathbb C\)" by "the Hochschild trace is the
  shadow of a negative-cyclic CY class".
- `cy_to_chiral.tex:5057-5059`: in (H3), require the negative-cyclic CY
  class and then mention the induced Serre pairing.
- `cy3_chain_level_bridge.tex:551-570`: keep \(\Delta\) explicitly a
  cochain BV operator and add one sentence that it is not Connes \(B\) on
  chains and not the hCS BV bracket.

Status after heal: cyclic \(A_\infty\) input is not overpromoted to
universal non-formal chain-level compatibility.

### Cycle 8 -- Downstream traces and class \(\mathbf M\)

ATTACK.  Use the holomorphic \(E_3\) construction or CFG traces to prove
BKM characters, black-hole/AdS statements, or the all-genus
class-\(\mathbf M\) equality \(E_\infty=6^g\).

FAILURE MODE.  CFG proves real 3d topological CS traces, not CY3
Dolbeault--hCS/Hall traces.  The BKM and holographic claims require
additional character, BPS, and physical comparison maps.  The class
\(\mathbf M\) compute surface proves \(E_4=(3t(1+t))^g\) and
\(\dim E_4=6^g\) for all \(g\), but \(E_\infty=E_4\) only for \(g\le3\);
for \(g\ge4\), \(d_5\) can act.

HEAL.  Keep trace claims stratified:

- CFG real topological CS trace: proved elsewhere.
- CY3 hCS/Hall trace: conditional on
  \(\Theta_{\hCS\to\Hall}^{or}\), orientation, shifts, Tate twists,
  completion, and Thom--Sebastiani.
- \(K3\times E\) character identities: theorem-grade as character data,
  not algebra-level construction of the Hall--Borcherds object.
- Class \(\mathbf M\): \(E_4=6^g\) for all \(g\); \(E_\infty=6^g\) only
  for \(g\le3\).

Patch targets:

- Not in the two target chapters: `e2_chiral_algebras.tex:2101-2114` and
  `compute/lib/e3_bar_higher_genus_class_m.py:14-26,453-458` should say
  \(E_4\), not all-genus \(E_\infty\).
- In `cy_to_chiral.tex:9700`, keep "each face carries its own
  hypotheses" and do not let any \(E_3\) bridge sentence imply the BKM /
  DT / holographic comparisons follow from Stage-1.

Status after heal: trace and gravity readings remain downstream
evidence, not proofs of the holomorphic \(E_3\) bridge.

## Killed claims

1. BV / framed \(E_2\) plus Dunn additivity proves the CY3 \(E_3\)
   Stage-1 structure.
2. The final specialised CY3 chiral algebra is \(E_3\), or has native
   \(E_2\) braiding.
3. \(B_{E_3}(A)\) is meaningful for a bare specialised \(E_1\) algebra
   \(A\) without retained Stage-1 data.
4. \(\CoHA(\mathbb C^3)=\mathcal W_{1+\infty}\) directly.
5. CFG 2026 proves the CY3 Dolbeault--hCS object or the
   hCS-to-Hall comparison.
6. Toric Hall chart gluing proves the oriented hCS-to-critical-CoHA map.
7. Contractibility of \(E_1\) operation spaces forces all Cech
   \(E_2^{p,*}\) terms to vanish on arbitrary atlases.
8. The \(\mathrm{GRT}_1(\mathbb Q)\)-torsor is a canonical or
   contractible choice before a torsor point is fixed.
9. A raw map \(\HH_3(\mathcal C)\to k\) is the full CY trace datum.
10. BTT or finite CE dimensions prove Yangian / chiral Hochschild
    unobstructedness in the full holomorphic \(E_3\) deformation problem.
11. \(K3\times E\) character identities construct the full
    Hall--Borcherds double.
12. Class \(\mathbf M\) has \(\dim E_\infty=6^g\) for all \(g\).

## Exact manuscript patch queue

Highest priority in the two target chapters:

1. `chapters/theory/cy_to_chiral.tex:4115-4118`: repair
   \(\Rep^{\Etwo}(A_\mathcal C)\) to
   \(\Rep^{\Etwo}(Z^{\mathrm{der}}_{\mathrm{ch}}(A_\mathcal C))\).
2. `chapters/theory/cy_to_chiral.tex:4125-4148`, `:4156-4158`,
   `:5031`, `:5163`: split toric Hall gluing from the hCS/Costello--Li
   comparison; make the latter conditional on the oriented comparison
   datum.
3. `chapters/theory/cy_to_chiral.tex:4333-4374`: restrict
   `thm:e1-descent-degeneration` to finite acyclic/tested atlases.
4. `chapters/theory/cy_to_chiral.tex:22-24`, `:190-192`, `:221-223`,
   `:260-268`: replace "contractible choice" by "after choosing a
   formality torsor point; residual homotopies inside the model are
   contractible".
5. `chapters/theory/cy3_chain_level_bridge.tex:691-693`, `:717-721`:
   conditionalise "Costello--Li propagator picking the Kontsevich point".
6. `chapters/theory/cy_to_chiral.tex:342`: replace the nonstandard
   `\ClaimStatusProvedHereConditional` status macro.
7. `chapters/theory/cy3_chain_level_bridge.tex:139-142` and
   `chapters/theory/cy_to_chiral.tex:5075`: decorate \(E_3\)-bar
   notation by the retained Stage-1 datum and keep the final bar
   \(E_1\).
8. `chapters/theory/cy_to_chiral.tex:147-160`, `:5057-5059`: name the
   negative-cyclic CY class as the real source datum.
9. `chapters/theory/cy_to_chiral.tex:5574-5588`, `:6024-6037`: qualify
   the deformation stack as a completed chiral Hochschild dgLa, with the
   finite Hom count marked as a model/shadow.
10. `chapters/theory/cy3_chain_level_bridge.tex:178-200`, `:403`,
    `:508`, `:786`: make the arrow notation consistently
    \(\Theta_{\hCS\to\Hall}^{or}\) and the target
    \(\CoHA_{\mathrm{crit}}^{or}\) wherever the oriented comparison is
    meant.

Adjacent, not in the two requested target chapters:

1. `chapters/theory/e2_chiral_algebras.tex:2101-2114`: replace
   all-genus \(E_\infty=6^g\) language by \(E_4=6^g\), with
   \(E_\infty=E_4\) only for \(g\le3\).
2. `compute/lib/e3_bar_higher_genus_class_m.py:453-458` and
   `compute/tests/test_e3_bar_higher_genus_class_m.py:234-243`: rename
   all-genus `einf` API/test headings to `e4`, or guard `E_inf` for
   \(g\ge4\).
3. `compute/lib/chiral_ce_e3_deformation.py`: mark finite CE output as a
   shadow; do not advertise it as the completed chiral deformation
   dgLa; fix the abelian flag, stale \(\sigma_2\) docstring, and
   class-L conductor mismatch noted by Agents 01 and 03.
4. `compute/lib/chiral_rmatrix_e3_braiding.py`: retitle as an
   Omega-background/structure-function witness, not the source of the
   non-symmetric centre half-braiding.

## Proof obligations that remain

1. Construct \(\Theta_{\hCS\to\Hall}^{or}\) on the full DWR Cech/Ran
   nerve, including compact-support variance, orientation transport,
   shifts, Tate twists, completions, vanishing cycles, and
   Thom--Sebastiani coherence.
2. Give the completed continuous chiral deformation dgLa and the chiral
   Gerstenhaber bracket with lambda-mode, residue, translation, and
   filtration conventions.
3. Prove or state the comparison from the native Stage-1 \(E_3\)
   deformation complex to the specialised \(E_1\) chiral Hochschild
   complex through \(\SpCh_{\Sigma_2,C}\).
4. Construct the true TCFT-level Connes hierarchy operator
   \(B^{(2)}\) and homotopy, or keep non-formal CY3 inputs restricted to
   verified framed loci.
5. Prove finite-atlas acyclicity for each descent theorem; do not infer
   it from \(E_1\)-operad contractibility.
6. Build holomorphic defect/module categories and their Hall/DT module
   comparison before using boundary or holographic traces as algebra
   theorems.
7. For class \(\mathbf M\), compute \(d_5,d_6,\ldots\) for \(g\ge4\) or
   keep \(E_\infty=6^g\) conjectural there.

## Verification to run

No build was run by this synthesis agent.  Before integration closes,
run the narrow checks below after patching:

```bash
rg -n 'Rep\^\{\\Etwo\}\(A_|CoHA\(\\C\^3\).*\\mathcal W|contractible choice|ClaimStatusProvedHereConditional|dim E_\\infty = 6\^g|B_\{E_3\}\(A\)' \
  chapters/theory/cy3_chain_level_bridge.tex \
  chapters/theory/cy_to_chiral.tex \
  chapters/theory/e2_chiral_algebras.tex
```

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider \
  compute/tests/test_chiral_ce_e3_deformation.py \
  compute/tests/test_holomorphic_cs_chiral_engine.py \
  compute/tests/test_hcs_codim2_defect_ope.py \
  compute/tests/test_chiral_rmatrix_e3_braiding.py \
  compute/tests/test_e3_bar_higher_genus_class_m.py \
  compute/tests/test_cech_descent_e1.py
```

At session end, with the main integration owner present, run the usual
manuscript check:

```bash
make fast
```

