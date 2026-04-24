# Agent 08 report: bar/Hochschild/center attack-heal

Scope: five-object discipline for `A`, `B(A)`, `A^i`, `A^!`, and
`Z^{\mathrm{der}}_{\mathrm{ch}}(A)`; Hochschild/coderived claims;
Koszul duality; derived center; Theorem H/B dependencies.

Operating invariant from Vol I:

- `/Users/raeez/chiral-bar-cobar/CLAUDE.md:295`: `A`, `B(A)`, `A^i`,
  `A^!`, and `Z^{\mathrm{der}}_{\mathrm{ch}}(A)` are distinct.
- `/Users/raeez/chiral-bar-cobar/CLAUDE.md:299`: `\Omega(B(A))=A` is
  inversion, not Koszul duality; `A^!` is obtained via Verdier duality;
  bulk is Hochschild cochains.
- `/Users/raeez/chiral-bar-cobar/main.tex:836`: Theorem A is the
  bar-cobar adjunction/equivalence on the Koszul locus.
- `/Users/raeez/chiral-bar-cobar/main.tex:851`: Theorem B is chiral
  Positselski inversion in the coderived/completed ambient.
- `/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:472`:
  the explicit chain is `\bar B^{ch}(A) -> A^i -> A^!`, with
  `\Omega(\bar B^{ch}(A)) \simeq A` separate.

## ATTACK_1: U1 overstates naturality and calls bar/CY-trace inverse

Anchors:

- `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:23`
- `chapters/theory/cy_to_chiral.tex:805`
- `chapters/theory/cy_to_chiral.tex:846`
- Vol I comparison: `/Users/raeez/chiral-bar-cobar/main.tex:836`

Attack. `B^{ord}(\Phi(\mathcal C)) \simeq CC_\bullet(\mathcal C)` is
currently phrased as a natural equivalence over the moduli base and is
then glossed as "Bar and CY trace are inverse operations." This conflates
three maps:

1. the chiral bar `B(A)` of the output algebra `A`;
2. the cyclic/Hochschild chain complex `CC_\bullet(\mathcal C)` of the
   CY input;
3. the CY trace/negative-cyclic class on `\mathcal C`.

Vol I only gives the inverse statement
`\Omega^{ch}\bar B^{ch}(A) -> A` on the Koszul/coderived-completed
locus. It does not say that the CY trace is inverse to the bar functor.
At `d=3`, naturality in morphisms is exactly Conjecture
`conj:phi-d-functoriality`.

## HEAL_1

Replace `chapters/theory/cy_to_chiral.tex:805-809` with:

```tex
 \item\label{phi:U1} \emph{Bar-shadow comparison.} On the verified
 object-level locus, after fixing the admissible specialisation
 $(\Sigma_{d-1},C)$, the ordered chiral bar coalgebra of the output
 carries a comparison quasi-isomorphism
 \[
   B^{\mathrm{ord}}\bigl(\Phi_d^{(\Sigma_{d-1},C)}(\cC)\bigr)
   \;\simeq\; \mathrm{CC}_\bullet(\cC)
   \quad \text{in } \mathrm{ChirCoAlg}^{\mathrm{conil}}_{\cM_d}.
 \]
 This is a comparison of coalgebras on the constructed object-level
 locus. Naturality in CY morphisms and base change is part of
 Conjecture~\textup{\ref{conj:phi-d-functoriality}}, not part of U1.
```

Replace `chapters/theory/cy_to_chiral.tex:846` with:

```tex
The bar functor $B^{\mathrm{ord}}$ extracts the output's ordered
coalgebraic shadow. The inverse statement is the chiral counit
$\Omega^{\mathrm{ch}}B^{\mathrm{ord}}(A)\to A$ on the Koszul or
weight-completed coderived locus; the CY trace supplies the cyclic
input on $\cC$ and is not the cobar inverse of $B^{\mathrm{ord}}$.
```

Status recommendation: keep the parent theorem `\ClaimStatusConditional`;
do not use U1 as a morphism-natural property at `d=3`.

## ATTACK_2: object uniqueness is advertised beyond the data

Anchors:

- `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:23`
- `chapters/theory/cy_to_chiral.tex:875`
- `chapters/theory/cy_to_chiral.tex:879`

Attack. U1+U3+U4 do not characterize the object-level assignment on the
whole smooth proper locus. U1 determines `A` only after Koszul/completion
hypotheses make `\Omega B(A) -> A` effective. U3 determines the level
and the center target, not the algebra. U4 gives four calibration points,
not a density theorem. The architecture note itself observes that
central-charge twisting can pass the object-level tests off the
Koszul-self-dual locus.

## HEAL_2

Replace `chapters/theory/cy_to_chiral.tex:875-883` with:

```tex
\begin{remark}[Conditional rigidity supplied by \textup{(U1), (U3), (U4)}]
\label{rem:phi-uniqueness}
On the Koszul-self-dual locus where the ordered bar coalgebra is
conilpotent or weight-completed and the chiral counit
$\Omega^{\mathrm{ch}}B^{\mathrm{ord}}(A)\to A$ is a quasi-isomorphism,
properties \textup{(U1), (U3), (U4)} give a rigidity criterion for the
object-level assignment. Property~\textup{(U1)} fixes the bar coalgebra;
Theorem~A of Vol.~I recovers $A$ from that coalgebra only in this
ambient. Property~\textup{(U3)} fixes the native operadic level and, for
$d\geq3$, the centre target
$\cZ(\Rep^{\Eone}(A))$, not an intrinsic $\Etwo$-structure on $A$.
Property~\textup{(U4)} fixes the standard calibration objects. Off the
Koszul-self-dual locus these properties are diagnostic rather than
characterizing; Fourier--Mukai kernel rigidification is an additional
hypothesis. Property~\textup{\ref{phi:U2}} remains the separate
morphism-action conjecture.
\end{remark}
```

Status recommendation: change "uniquely characterised" wording to
"conditional rigidity" everywhere it depends on U1/U3/U4 only.

Open obligation: prove a density/rigidification theorem for the standard
inputs or state U5 as a formal hypothesis.

## ATTACK_3: `A^! = \Phi_d(\mathcal C^!)` is stated as fact

Anchors:

- `chapters/theory/cy_to_chiral.tex:4948`
- `chapters/theory/cy_to_chiral.tex:4957`
- `chapters/examples/k3e_bkm_chapter.tex:2393`
- Vol I comparison:
  `/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:472`

Attack. The sentence "The Koszul dual `A_\cC^! = \Phi_d(\cC^!)` is the
chiral algebra of the mirror category" promotes the conjecture before
the conjecture. Vol I fixes the object chain:

```tex
B(A) \longrightarrow A^i := H^*B(A) \xrightarrow{\mathbb D_{\Ran}} A^!.
```

The expected mirror statement is `\Phi(\cC^\vee)\simeq A_\cC^!`; it is
not the definition of `A_\cC^!`.

## HEAL_3

Replace `chapters/theory/cy_to_chiral.tex:4948` with:

```tex
The CY-to-chiral correspondence interacts with the Koszul-duality engine
of Vol.~I through the output algebra $A_\cC=\Phi_d(\cC)$. Its bar
coalgebra is $B(A_\cC)$; its bar cohomology coalgebra is
$A_\cC^i:=H^*B(A_\cC)$; its chiral Koszul dual algebra is
$A_\cC^!:=\mathbb D_{\Ran}(A_\cC^i)$. The bar-shadow comparison with
$\mathrm{CC}_\bullet(\cC)$ is U1. The further identification
$\Phi_d(\cC^\vee)\simeq A_\cC^!$ for a mirror CY category
$\cC^\vee$ is Conjecture~\ref{conj:cy-koszul-mirror}.
```

Replace `chapters/examples/k3e_bkm_chapter.tex:2393-2395` with:

```tex
 \item \emph{Koszul dual} $A^!_{K3 \times E}$. Let
 $A=A_{K3\times E}$, let $B(A)$ be its ordered chiral bar coalgebra,
 and set $A^i:=H^*B(A)$. The Koszul dual algebra is
 $A^!:=\mathbb D_{\Ran(E)}(A^i)$. Equivalently,
 $\mathbb D_{\Ran(E)}(B(A))$ computes the bar coalgebra of the
 homotopy Koszul dual after passing to bar cohomology and the
 completed/coderived ambient.
```

Status recommendation: keep `conj:cy-koszul-mirror` conjectural; do not
use mirror symmetry to define `A^!`.

## ATTACK_4: Theorem B is used to make bar-cobar "strict" and imply center equivalence

Anchors:

- `chapters/theory/quantum_groups_foundations.tex:3403`
- `chapters/theory/quantum_groups_foundations.tex:3406`
- Vol I scope comparison:
  `/Users/raeez/chiral-bar-cobar/chapters/theory/theorem_B_scope_platonic.tex:32`

Attack. The text says Theorem A is "strict (Theorem B); hence the
derived centre receives Drinfeld's centre-equivalence." This is two
separate overclaims. Theorem B is a coderived/weight-completed
Positselski inversion theorem, not strict equality in the raw chiral
coalgebra category. Drinfeld center equivalence is a Hochschild/Morita
statement about `\Rep^{E_1}(A)` and does not follow from
`\Omega B(A)\simeq A`.

## HEAL_4

Replace `chapters/theory/quantum_groups_foundations.tex:3403-3408` with:

```tex
\emph{(iii) Vanishing on the Koszul locus.} On the admissible Koszul
locus
$\overline{\mathcal A_2}\smallsetminus\bigcup_{n\;\text{admissible}}H_n$,
the chiral bar--cobar counit
$\Omega^{\mathrm{ch}}B^{\mathrm{ch}}(\mathbf H_{\Delta_5})\to
\mathbf H_{\Delta_5}$ is a quasi-isomorphism in the Koszul or
weight-completed coderived ambient of Vol.~I Theorems A and B. This
recovers the boundary algebra from its bar coalgebra; it is not the
derived-centre construction. Separately, under the Morita/representation
hypotheses for the $E_1$-module category of $\mathbf H_{\Delta_5}$, the
Drinfeld centre identifies with the representation category of the
derived chiral centre
$Z^{\mathrm{der}}_{\mathrm{ch}}(\mathbf H_{\Delta_5})$.
```

Status recommendation: bar-cobar recovery is `ProvedElsewhere` in its
Vol I ambient; the application to the `\mathbf H_{\Delta_5}` center is
`Conditional` on the Morita/representation hypotheses.

## ATTACK_5: genus-2 derived-center character is marked proved

Anchors:

- `chapters/theory/hochschild_calculus.tex:2886`
- `chapters/theory/hochschild_calculus.tex:2888`
- `chapters/theory/hochschild_calculus.tex:2945`
- `chapters/theory/hochschild_calculus.tex:2989`

Attack. Lurie/Dunn proves that the Drinfeld center of an `E_1` module
category carries the higher center structure. Gritsenko/Borcherds proves
the modular identity `\Delta_5^2=\Delta_{10}`. Neither proves that the
factorization-homology genus-2 character of
`Z(\Rep_E(\mathbf H_{\Delta_5}))` is exactly `\Delta_{10}`. That
requires the concrete `\mathbf H_{\Delta_5}` model, the character map
from the center, and compatibility with the framed `\Phi_3` output.

## HEAL_5

Split the proposition. Replacement for status and opening:

```tex
\begin{proposition}[$E_2$-chiral structure on
\texorpdfstring{$Z(\RepE(\mathbf H_{\Delta_5}))$}{Z(RepE(H-Delta-5))}
and conditional genus-\texorpdfstring{$2$}{2}
\texorpdfstring{$\Delta_{10}$}{Delta-10} character]
\label{prop:hochcalc-e2-chiral-drinfeld-centre-hdelta5-delta10}
\ClaimStatusConditional{Drinfeld-centre $E_2$ structure proved
elsewhere by Lurie/Dunn; identification of its genus-$2$ character with
$\Delta_{10}$ conditional on the $K3\times E$ boundary model and the
framed $\Phi_3$ character comparison.}
Let $A=\mathbf H_{\Delta_5}$ be the constructed $E_1$-chiral algebra on
$E$ on the framed $K3\times E$ locus, and let $\RepE(A)$ be its
$E_1$-chiral module category. Then the Drinfeld centre
$Z(\RepE(A))$ carries the standard $E_2$-centre structure. If, in
addition, the boundary character of $A$ is the Gritsenko
$\Delta_5$ character and the center factorization-homology character
is compatible with the separating-gluing map, then
\[
Z_{g=2}\bigl(Z(\RepE(A))\bigr)=\Delta_5^2=\Delta_{10}.
\]
```

Status recommendation: part (b) `ProvedElsewhere`; part (c)
`Conditional`, not `Proved`.

Open obligation: construct the character map
`Z(\RepE(A)) -> M_{10}(\mathrm{Sp}_4(\mathbb Z))` and prove
separating-gluing multiplicativity in the chiral factorization model.

## ATTACK_6: Costello-Li-Paquette bulk-boundary proposition is over-statused

Anchors:

- `chapters/theory/quantum_groups_foundations.tex:5699`
- `chapters/theory/quantum_groups_foundations.tex:5701`
- `chapters/theory/quantum_groups_foundations.tex:5732`
- `chapters/theory/quantum_groups_foundations.tex:5750`
- consistency anchor: `chapters/theory/hochschild_calculus.tex:2341`

Attack. The proposition is marked `\ClaimStatusProvedHere` and asserts
chain-level boundary identification
`\iota^*\cF_{T_{\mathrm{HT}}[X_6]}\simeq\HDelta` and bulk center
identification
`Z^{\mathrm{der}}_{\mathrm{ch}}(\HDelta)\simeq\Obsbulk(...)`. But the
Hochschild chapter itself says the Costello-Gaiotto bulk identification
is conjectural modulo Costello-Paquette higher-genus partition-function
input. The cited Costello-Gwilliam restriction theorem supplies the
formal restriction mechanism, not the specific identification with the
paramodular BKM chiral bialgebra.

## HEAL_6

Replace the proposition status/opening with:

```tex
\begin{proposition}[Conditional bulk-boundary factorization of the
\texorpdfstring{$3$}{3}d HT theory on \texorpdfstring{$K3\times E$}{K3x E};
\texorpdfstring{$\SCchtop$}{SCchtop}-datum of
\texorpdfstring{$\HDelta$}{HDelta};
\ClaimStatusConditional{formal Costello--Gwilliam restriction proved
elsewhere; identification of the boundary with $\HDelta$ and of the
bulk with $Z^{\mathrm{der}}_{\mathrm{ch}}(\HDelta)$ conditional on the
Costello--Paquette $K3\times E$ HT comparison and the framed
$\Phi_3$ boundary model}]
Assume the Costello--Paquette $K3\times E$ holomorphic-topological
comparison identifies the boundary observables of
$T_{\mathrm{HT}}[K3\times E]$ with the framed $E_1$-chiral algebra
$\HDelta$. Then the Costello--Gwilliam restriction formalism gives the
following $\SCchtop$-datum.
```

Replace item (b) first sentence with:

```tex
Under the above comparison hypothesis, the boundary factorization
algebra identifies with $\HDelta$ as an $E_1$-chiral algebra on $E$.
```

Replace item (c) first sentence with:

```tex
Under the same Morita/center comparison hypothesis, the derived chiral
centre of $\HDelta$ computes the closed-colour bulk factorization
algebra.
```

Status recommendation: `Conditional`. The formal SC-colored operad
structure can be `ProvedElsewhere`; the `\HDelta` identification cannot.

## ATTACK_7: Theorem H CY3 extension is labelled ProvedElsewhere while using internal transport

Anchors:

- `chapters/theory/hochschild_calculus.tex:935`
- `chapters/theory/hochschild_calculus.tex:937`
- `chapters/theory/hochschild_calculus.tex:941`
- `chapters/examples/toric_cy3_coha.tex:2546`

Attack. The theorem on non-vanishing `\ChirHoch^3` is not purely
"ProvedElsewhere." It relies on an internal cocycle
`prop:tcy3-chi-3-nonvanishing-triangle` and on transport from CoHA/CY3
data to the chiral `\mathbf H_{\Delta_5}` side through `\Phi_3`. The
explicit reduced-DT/cocycle pairing may be proved here; the transport to
`\ChirHoch^3(\mathbf H_{\Delta_5})` is conditional on the framed
`Phi_3` comparison.

## HEAL_7

Replace the theorem status/opening with:

```tex
\begin{theorem}[Non-vanishing \texorpdfstring{$\ChirHoch^3$}{ChirHoch-3}
and Koszul-duality obstruction]
\label{thm:hoch-chi3-koszul-obstruction}
\ClaimStatusConditional{explicit reduced-DT/chiral cocycle pairing
proved here; transport to $\ChirHoch^3(\mathbf H_{\Delta_5})$
conditional on the framed $\Phi_3$ CoHA-to-chiral comparison}
\emph{Statement.} Assume the framed $K3\times E$ output
$\mathbf H_{\Delta_5}$ and the CoHA-to-chiral transport of
Prop.~\ref{prop:tcy3-chi-3-nonvanishing-triangle}. Let
$\chi_3\in\ChirHoch^3(\mathbf H_{\Delta_5})$ denote the transported
chiral $3$-cocycle. Then:
```

Status recommendation: split the result into:

- `ProvedHere`: explicit cocycle and triangle pairing in the reduced-DT
  model.
- `Conditional`: transport to `\ChirHoch^3(\mathbf H_{\Delta_5})` and
  Koszul-duality obstruction for the `\Phi_3` output.

## ATTACK_8: HDelta inversion cycles conflate general bar-cobar theorems with the specific automorphic application

Anchors:

- `chapters/theory/hochschild_calculus.tex:3284`
- `chapters/theory/hochschild_calculus.tex:3293`
- `chapters/theory/hochschild_calculus.tex:3328`
- `chapters/theory/hochschild_calculus.tex:3388`
- `chapters/theory/hochschild_calculus.tex:3425`

Attack. The inversion-cycle propositions are useful, but the statuses
collapse three levels:

1. general curved/coderived bar-cobar formalism, proved elsewhere;
2. completed conilpotence hypotheses for the specific
   `\mathbf H_{\Delta_5}` bar coalgebra;
3. automorphic curvature identification with the `\Delta_5`/`\Delta_{10}`
   tower.

Only (1) is imported theorem-grade. The specific `\HDelta` application
must assume the completed curved bar coalgebra and the automorphic
curvature model.

## HEAL_8

Replace the opening paragraph at `chapters/theory/hochschild_calculus.tex:3284-3289`
with:

```tex
Assume $\mathbf H_{\Delta_5}$ is equipped with the completed curved
$E_1$-chiral bar coalgebra on $E$ constructed from the framed
$K3\times E$ output. In that completed/coderived ambient, the counit
$\Omegach(\barB^{\mathrm{ch}}(\mathbf H_{\Delta_5}))\to
\mathbf H_{\Delta_5}$ is the Vol.~I bar-cobar inversion map. The
general curved/coderived equivalence is proved elsewhere; the
$K3\times E$-specific content is the identification of its curvature
and completion data with the Gritsenko--Nikulin automorphic tower.
Five obstruction--resolution pairs below keep these layers separate.
```

Status recommendations:

- `prop:hochcalc-hdelta5-inversion-I`: `\ClaimStatusConditional{curved
  bar-cobar formalism proved elsewhere; HDelta curvature model
  conditional on the framed K3xE chiral algebra}`
- `prop:hochcalc-hdelta5-inversion-II`: `\ClaimStatusConditional`
  until the filtration/pro-conilpotence hypotheses are proved for the
  actual `\HDelta` mode algebra.
- `prop:hochcalc-hdelta5-inversion-IV`: `\ClaimStatusProvedElsewhere`
  for Positselski/Booth-Lazarev formalism, with a conditional sentence
  for `\HDelta`.
- `prop:hochcalc-hdelta5-inversion-V`: `\ClaimStatusConditional`
  because automorphic curvature is an application, not Vol I Theorem A
  itself.

## Cross-file status recommendations

- `chapters/theory/cy_to_chiral.tex`: keep parent `Phi_d` theorem
  conditional; rewrite U1 as bar-shadow comparison; remove "bar and CY
  trace are inverse."
- `chapters/theory/hochschild_calculus.tex`: split center and character
  claims; downgrade the `\Delta_{10}` center-character and `\HDelta`
  inversion applications to conditional where they use the framed
  `\Phi_3` boundary model.
- `chapters/theory/quantum_groups_foundations.tex`: downgrade the
  Costello-Li-Paquette/HDelta bulk-boundary proposition to conditional;
  do not infer center equivalence from Theorem B.
- `chapters/examples/k3e_bkm_chapter.tex`: insert `A -> B(A) -> A^i
  -> A^!` explicitly in the holographic datum.

## Tests and commands run

No builds, no commits, and no destructive git commands.

Commands run:

- `git status --short`
- targeted `rg` sweeps for `Omega`, `B(A)`, `A^i`, `A^!`,
  `Z^{\mathrm{der}}_{\mathrm{ch}}`, `Hochschild`, `coderived`,
  `Koszul`, `Verdier`, `Theorem H`, `Theorem B`, and claim-status tags
  across the scoped Vol III files.
- targeted `nl -ba ... | sed -n ...` reads for all anchors cited above.
- Vol I comparison reads from `CLAUDE.md`, `main.tex`,
  `chiral_hochschild_koszul.tex`, and `theorem_B_scope_platonic.tex`.

No pytest was run. This was a report-only adversarial audit; the relevant
surface is theorem wording and dependency/status discipline, not a
compute engine. Existing compute files relevant to this scope include
`compute/tests/test_drinfeld_center_e1_cy3.py`,
`compute/tests/test_drinfeld_center_heisenberg_bulk.py`,
`compute/tests/test_chiral_koszul_derived.py`,
`compute/tests/test_cy3_hochschild.py`, and
`compute/tests/test_bkm_yangian_J_cubic.py`, but none directly proves
the over-statused functorial/bulk-center identifications attacked above.

## Open obligations

1. Prove or state as a hypothesis the rigidification theorem turning
   U1/U3/U4 from diagnostics into object uniqueness.
2. Construct the center character map
   `Z(\RepE(\mathbf H_{\Delta_5})) -> M_{10}(\mathrm{Sp}_4(\mathbb Z))`
   and prove separating-gluing multiplicativity.
3. Prove the Costello-Paquette `K3\times E` HT comparison identifies
   boundary observables with the specific `\HDelta` presentation.
4. Prove the CoHA-to-chiral transport sending the explicit reduced-DT
   `\chi_3` cocycle to `\ChirHoch^3(\mathbf H_{\Delta_5})`.
5. Verify completed conilpotence and filtration nilpotence for the
   actual `\mathbf H_{\Delta_5}` mode algebra, not only for a formal
   curved model.

