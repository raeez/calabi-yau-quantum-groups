# Agent 02 - Drinfeld/Kazhdan operads

Date: 2026-04-24

Mode: adversarial ATTACK -> HEAL, report-only. No chapter or compute edits.

Scope: Deligne--Tamarkin braces, cyclic/framed \(E_2\)/BV, Dunn--Lurie additivity \(E_3 \simeq E_2 \otimes E_1\), canonicity up to \(\mathrm{GRT}_1\), and whether the present CY3 chain-level chapter promotes BV data too far.

## Files inspected

- `CLAUDE.md`
- `AGENTS.md`
- `chapters/theory/cy3_chain_level_bridge.tex`
- `chapters/theory/cy_to_chiral.tex`
- `chapters/theory/e2_chiral_algebras.tex`
- prior neighboring report: `notes/adversarial_swarm_20260424_cfg_e3/agent_02_drinfeld_kazhdan_e3_operads.md`

## Primary source anchors checked

- McClure--Smith, `A solution of Deligne's conjecture`, arXiv:math/9910126. The abstract states the Hochschild cochain complex has an action by chains on little 2-cubes: https://arxiv.org/abs/math/9910126.
- Kontsevich--Soibelman, `Deformations of algebras over operads and Deligne's conjecture`, arXiv:math/0001151. The abstract states the Hochschild complex carries a dg-algebra structure over chains on little discs and records a homotopic GT action: https://arxiv.org/abs/math/0001151.
- Tamarkin, `Another proof of M. Kontsevich formality theorem`, arXiv:math/9803025, and `Formality of Chain Operad of Small Squares`, arXiv:math/9809164. The latter explicitly says the small-squares chain operad is formal and the formality follows from an associator: https://arxiv.org/abs/math/9803025, https://arxiv.org/abs/math/9809164.
- Getzler, `Batalin-Vilkovisky algebras and two-dimensional topological field theories`, Commun. Math. Phys. 159 (1994), arXiv:hep-th/9212043. The abstract gives BV on cohomology of 2d TFTs: https://arxiv.org/abs/hep-th/9212043.
- Tradler, `The BV Algebra on Hochschild Cohomology Induced by Infinity Inner Products`, arXiv:math/0210150. The abstract gives BV on Hochschild cohomology of unital associative and \(A_\infty\) algebras with symmetric nondegenerate infinity inner product: https://arxiv.org/abs/math/0210150.
- Menichi, `Batalin-Vilkovisky algebras and cyclic cohomology of Hopf algebras`, arXiv:math/0311276. The abstract gives BV cohomology for cyclic operads with multiplication: https://arxiv.org/abs/math/0311276.
- Ginzburg, `Calabi-Yau algebras`, arXiv:math/0612139. The abstract gives the CY algebra framework and the 3-dimensional potential/critical-locus context: https://arxiv.org/abs/math/0612139.
- Lurie, `Higher Algebra`, Theorem 5.1.2.2. The theorem states the Dunn additivity tensor product of \(E_k\) and \(E_{k'}\) as \(E_{k+k'}\): https://www.math.ias.edu/~lurie/papers/HA2012.pdf.
- Willwacher, `M. Kontsevich's graph complex and the Grothendieck-Teichmueller Lie algebra`, arXiv:1009.1654. The abstract identifies \(H^0\) of Kontsevich's graph complex with \(\mathfrak{grt}_1\) and computes homotopy derivations of Gerstenhaber operads: https://arxiv.org/abs/1009.1654.

## Executive verdict

The safe theorem is narrower than the current CY3 chain-level bridge says.

1. Deligne--Tamarkin supplies a chain-level \(E_2\)-type action on Hochschild cochains, with the braces as an explicit chain model. It does not put a strict little-discs chain action on Hochschild cohomology itself.
2. Cyclicity supplies BV on Hochschild cohomology, and under cyclic Deligne technology supplies a homotopy framed-\(E_2\) refinement on cochains. It does not by itself produce a strict \(E_3\)-algebra.
3. Dunn--Lurie says \(E_2 \otimes E_1 \simeq E_3\) as operads. It does not say that a framed \(E_2\)-algebra tensored with an arbitrary/canonical line direction becomes an unframed \(E_3\)-algebra.
4. The formality datum is a \(\mathrm{GRT}_1(\mathbb Q)\)-torsor. It is not a contractible canonical choice. A Costello--Li propagator may pin a branch only after a graph-comparison theorem is named.
5. The chapter currently overclaims the route "braces + BV + Dunn = \(E_3\) on \(\HH^\bullet(\mathcal C)\)". Replace it by a conditional Stage-1 statement requiring a chosen \(E_3\)-formality/framing datum. The final CY3 chiral output remains \(E_1\), with \(E_2\) braiding recovered on the Drinfeld centre.

## ATTACK -> HEAL cycles

### Cycle 1 - Deligne--Tamarkin braces act on cochains, not on \(\HH^\bullet\) as written

ATTACK.

`chapters/theory/cy3_chain_level_bridge.tex:417-439` states an operadic action
\[
\mathrm{Brace}_\bullet:C_\bullet(\Conf_2;\mathbb Q)\to \mathrm{End}(\HH^\bullet(\mathcal C)).
\]
There are two type errors.

- \(\Conf_2\) is not the little-discs operad; it is at best one arity or an overloaded notation. The operad is \(E_2\), little 2-discs/cubes, or a chain model quasi-isomorphic to it.
- The Deligne action is on the Hochschild cochain complex \(\CC^\bullet(\mathcal C,\mathcal C)\). Its cohomology \(\HH^\bullet(\mathcal C)\) carries the induced Gerstenhaber algebra. A chain-level action cannot literally land in \(\mathrm{End}(\HH^\bullet)\) unless \(\HH^\bullet\) is being used nonstandardly for the cochain complex.

Local supporting anchors:

- `chapters/theory/e2_chiral_algebras.tex:98-107` correctly states the canonical \(E_2\)-algebra as Hochschild cochains and the induced Gerstenhaber structure on Hochschild cohomology.
- `chapters/theory/e2_chiral_algebras.tex:117-129` again puts the \(E_2\) structure on \(\CC^\bullet(A,A)\), not on cohomology.
- `chapters/theory/cy3_chain_level_bridge.tex:441-450` cites the correct source lane, but the proposition statement above it is mistyped.

HEAL.

Proposed replacement for `chapters/theory/cy3_chain_level_bridge.tex:420-438`:

```tex
For a smooth proper cyclic \(\Ainf\)-category \(\cC\), the Hochschild
cochain complex \(\CC^\bullet(\cC,\cC)\) carries the Deligne--Tamarkin
\(E_2\)-structure. Equivalently, the brace operad acts by the
Getzler--Voronov brace operations and maps by a quasi-isomorphism of
operads to \(C_\bullet(E_2;\Q)\) after choosing the standard
Deligne--Tamarkin formality datum. The induced structure on
\(\HH^\bullet(\cC)\) is the Gerstenhaber cup product and bracket. The
comparison with \(C_\bullet(E_2;\Q)\) is canonical only up to the
\(\mathrm{GRT}_1(\Q)\)-torsor of Drinfeld associators.
```

Claim-status recommendation: `ClaimStatusProvedElsewhere` for the Deligne action; no `ProvedHere` content here.

### Cycle 2 - BV/framed \(E_2\) is a homology or homotopy-framed statement, not a strict chain equivalence with \(\BV\)

ATTACK.

`chapters/theory/cy3_chain_level_bridge.tex:455-473` says the cyclic pairing induces a chain-level BV operator \(\Delta\) on \(\HH^\bullet(\cC)\), with \(\Delta^2=0\) on cohomology, the BV identity "on the nose", and then states
\[
\BV\simeq C_\bullet(\Conf_2^{\mathrm{fr}};\Q).
\]
This conflates three levels.

- Tradler/Menichi/Ginzburg give BV on Hochschild cohomology under cyclic/Frobenius/CY hypotheses; chain-level cochains carry a homotopy BV or framed-\(E_2\) structure only with cyclic Deligne data.
- \(\Delta^2=0\) "on cohomology" and the BV identity "on the nose" are incompatible as a strict chain-level assertion unless a strict model has been chosen and proved.
- \(\BV\) is the homology operad of framed little 2-discs, \(H_\bullet(fE_2)\), not literally the singular-chain operad \(C_\bullet(fE_2)\). A chain operad statement needs \(C_\bullet(fE_2)\)-algebra or a chosen formality quasi-isomorphism.

Local supporting anchors:

- `chapters/theory/e2_chiral_algebras.tex:117-129` uses the safer language \(fE_2\simeq E_2\rtimes S^1\).
- `chapters/theory/e2_chiral_algebras.tex:139-148` correctly says the CY dimension shifts the cyclic trace data, not the underlying \(E_2\) operad.
- `chapters/theory/cy_to_chiral.tex:407-409` warns that the \(\mathrm{GRT}_1\)-torsor does not rigidify the chain-level \(S^3\)-framing obstruction.

HEAL.

Proposed replacement for `chapters/theory/cy3_chain_level_bridge.tex:458-473`:

```tex
For a smooth proper cyclic \(\Ainf\)-category \(\cC\) of CY dimension
\(d\), the cyclic pairing identifies Hochschild cochains with shifted
Hochschild chains and transports Connes' \(B\)-operator to a degree
\(-1\) operator \(\Delta\). On Hochschild cohomology this gives the
Tradler--Menichi--Ginzburg BV algebra:
\[
\{a,b\}_{\Ger}=\Delta(a\cup b)-\Delta(a)\cup b
-(-1)^{|a|}a\cup\Delta(b).
\]
At chain level the corresponding statement is a homotopy framed-\(E_2\)
structure, or a strict \(C_\bullet(fE_2;\Q)\)-algebra only after choosing
and recording a cyclic Deligne model. Its homology operad is
\(H_\bullet(fE_2;\Q)\cong \BV\).
```

Claim-status recommendation: BV on cohomology is `ClaimStatusProvedElsewhere`; strict chain-level framed-\(E_2\) is `ClaimStatusConditional` unless the cyclic Deligne model is named.

### Cycle 3 - Dunn additivity does not turn framed \(E_2\) plus a line into unframed \(E_3\)

ATTACK.

`chapters/theory/cy3_chain_level_bridge.tex:493-518` claims the framed \(E_2\)-structure of the BV proposition combines with an \(E_1\)-structure on the third real direction to produce a chain-level \(E_3\)-algebra on \(\HH^\bullet(\cC)\). The proof says
\[
fE_2\otimes_{\mathrm{Dunn}}E_1\simeq E_3^{\mathrm{top}}
\]
and then erases the framing because \(\pi_1(\Conf_2(\mathbb R^3))=0\).

This is not a valid Dunn inference. Lurie's Theorem 5.1.2.2 gives \(E_k\otimes E_{k'}\simeq E_{k+k'}\) for the unframed little-cubes operads. The semidirect \(S^1\)-rotation datum in \(fE_2=E_2\rtimes SO(2)\) is extra structure. Tensoring with \(E_1\) does not automatically identify it with unframed \(E_3\), and \(\pi_1\) of a binary configuration space does not remove the full framed-operad datum. At best, the underlying unframed \(E_2\)-part can be tensored with \(E_1\) once a compatible \(E_1\)-action is supplied.

Local supporting anchors:

- `chapters/theory/cy_to_chiral.tex:437-443` says the Dunn restriction of the \(S^3\)-framed \(E_3\) structure to \(E_2\) is symmetric, while the nonsymmetric quantum-group \(R\)-matrix comes from the Drinfeld centre.
- `chapters/theory/cy_to_chiral.tex:540-550` says Stage-2 at \(d\ge 3\) Dunn-restricts to \(E_1\), not \(E_3\) or native \(E_2\) on the curve output.
- `chapters/theory/e2_chiral_algebras.tex:15-46` already records the correct \(d=3\) placement: \(E_2\) lives on the chiral Drinfeld centre, not on \(A\).

HEAL.

Proposed replacement for `chapters/theory/cy3_chain_level_bridge.tex:493-518`:

```tex
\begin{proposition}[Dunn restriction and the missing \(E_3\) datum]
\label{prop:cy3-dunn-restriction-not-bv-e3}
\ClaimStatusConditional{}
The Deligne--Tamarkin braces give the unframed \(E_2\)-part on
\(\CC^\bullet(\cC,\cC)\), and cyclicity gives a homotopy framed-\(E_2\)
refinement. Dunn--Lurie additivity identifies \(E_2\otimes E_1\) with
\(E_3\) as \(\infty\)-operads, but it produces an \(E_3\)-algebra on
Hochschild cochains only after an independent compatible \(E_1\)-direction
and an \(E_3\)-formality/framing datum have been fixed. The BV operator
alone is not that datum.
\end{proposition}
```

Delete the sentence `framed \(\Etwo\otimes_{\mathrm{Dunn}}\Eone\simeq\Ethree^{\mathrm{top}}\) is the unframed \(\Ethree\)` unless a primary source proving precisely that framed-operad comparison is supplied.

### Cycle 4 - \(\mathrm{GRT}_1\) canonicity is a torsor, not a contractible choice

ATTACK.

The current bridge has mixed canonicity language.

- `chapters/theory/cy3_chain_level_bridge.tex:436-438` correctly says the \(E_2\) action is canonical up to a \(\mathrm{GRT}_1(\Q)\)-torsor.
- `chapters/theory/cy3_chain_level_bridge.tex:501-503` says the claimed \(E_3\) structure is canonical under a single \(\mathrm{GRT}_1(\Q)\)-torsor.
- `chapters/theory/cy3_chain_level_bridge.tex:578-580` says the Costello--Li propagator picks the Kontsevich point.
- `chapters/theory/e2_chiral_algebras.tex:447-460` says the Dunn--Lurie decomposition is up to contractible choice after fixing a cyclic lift, then calls the choice a torsor over a cyclic subgroup of \(\mathrm{GRT}_1\).

This is unstable. A torsor is not contractible unless a point has already been chosen. The main functor chapter has the better guardrail:

- `chapters/theory/cy_to_chiral.tex:313-347` states that \(E_3\)-formality choices form a \(\mathrm{GRT}_1(\Q)\)-torsor and that Stage-1 is pinned only after a torsor point is fixed.
- `chapters/theory/cy_to_chiral.tex:407-409` states that the torsor does not supply a canonical associator, does not rigidify the \(S^3\)-framing obstruction, and does not commute with Stage-2 specialisation.

HEAL.

Use one canonicity formula everywhere:

```tex
After choosing a rational formality datum
\[
F\in \mathrm{Form}_3(\Q),
\qquad \mathrm{Form}_3(\Q)\ \text{a free }
\mathrm{GRT}_1(\Q)\text{-torsor},
\]
the Stage-1 construction has a pinned \(E_3\)-operadic presentation on the
verified framed/holomorphic locus. Replacing \(F\) by \(gF\) transports the
presentation by the \(\mathrm{GRT}_1(\Q)\)-action; it does not give a
canonical equality before the datum is fixed.
```

Replace "contractible choice" at `chapters/theory/e2_chiral_algebras.tex:447-460` by "choice of a torsor point, followed by contractible homotopies inside the chosen model" if that is the intended meaning.

Replace `chapters/theory/cy3_chain_level_bridge.tex:578-580` by:

```tex
Canonicity is relative to the chosen \(\mathrm{GRT}_1(\Q)\)-torsor point.
The Costello--Li propagator may determine such a point on a specified local
graph-integral model; identifying it with the Kontsevich associator is a
separate graph-comparison assertion and must be cited or left conditional.
```

### Cycle 5 - The current CY3 bridge overclaims "BV implies \(E_3\)" in the Stage-1 envelope theorem

ATTACK.

`chapters/theory/cy3_chain_level_bridge.tex:399-415` summarizes the left end as:

1. Deligne--Tamarkin gives \(E_2\);
2. Tradler--Menichi--Ginzburg promotes this to BV;
3. Costello--Gwilliam's envelope sends the resulting \(E_3\)-algebra to a factorisation algebra on \(\mathbb R^3\).

The theorem `chapters/theory/cy3_chain_level_bridge.tex:547-580` then states
\[
\PhiFA_3(\cC)=\mathrm{Hol}_X(\cU^\FA(\HH^\bullet(\cC)))
\]
with \(\HH^\bullet(\cC)\in E_3\)-Alg by `prop:cy3-e3-structure-hochschild`.

This depends on the invalid Cycle 3 inference. The main `cy_to_chiral` file can support a conditional Stage-1 \(E_3\) statement, but through `chapters/theory/cy_to_chiral.tex:287-300` and `chapters/theory/cy_to_chiral.tex:313-351`: choose an \(E_3\)-formality datum, assemble topologically, then apply the Costello--Li holomorphic twist on the verified locus. That is not "BV gives \(E_3\)".

The line also risks conflict with the final-output rule:

- `chapters/theory/cy_to_chiral.tex:278-284` says the curve shadow \(A_\cC=\Phi_d(\cC)\) is \(E_1\) for \(d\ge 3\).
- `chapters/theory/e2_chiral_algebras.tex:31-46` says at \(d=3\), the \(E_2\)-braided structure lives on \(\mathcal Z(\Rep^{E_1}(A))\), not on \(A\).

HEAL.

Proposed replacement for `chapters/theory/cy3_chain_level_bridge.tex:402-415`:

```tex
The status ledger records \(\PhiFA_3(\cC)\dashrightarrow
\CoHA_{\mathrm{crit}}(X)\) as the open arrow. Its left end is assembled
from separate chain-level data: Deligne--Tamarkin braces give the
unframed \(E_2\) Hochschild cochain structure; cyclicity gives the
Tradler--Menichi--Ginzburg BV structure on cohomology, or a homotopy
framed-\(E_2\) refinement after choosing a cyclic Deligne model; an
independent \(E_3\)-formality/framing datum is then required before the
Costello--Gwilliam factorisation envelope can be applied in the \(E_3\)
lane. The resulting Stage-1 object is conditional on that datum and on
the Costello--Li holomorphic twist hypotheses. The Stage-2 CY3 chiral
output remains \(E_1\); its \(E_2\)-braiding is recovered on the
Drinfeld centre.
```

Proposed replacement for theorem status at `chapters/theory/cy3_chain_level_bridge.tex:547-580`:

```tex
\ClaimStatusConditional{}\textup{(on a chosen \(E_3\)-formality datum,
the cyclic/framed model, and the verified Stage-1 holomorphic locus)}
```

and replace item (1) at `chapters/theory/cy3_chain_level_bridge.tex:568-569` with:

```tex
\item \(\CC^\bullet(\cC,\cC)\) carries the Deligne--Tamarkin \(E_2\)
structure and the cyclic homotopy framed-\(E_2\) refinement; it is used
as an \(E_3\)-input only after the additional \(E_3\)-formality/framing
datum of Theorem~\ref{thm:cfg-e3-formality-stage-1-phiFA3-torsor} is fixed;
```

### Cycle 6 - Dunn additivity is not a canonical tensor-factor decomposition of a given Stage-1 algebra

ATTACK.

`chapters/theory/e2_chiral_algebras.tex:424-439` says the Stage-1 output \(\cF_\cC=\PhiFA_3(\cC)\) is an \(E_3\)-holomorphic factorisation algebra and that Dunn--Lurie decomposes it into two independently travelling structures. `chapters/theory/e2_chiral_algebras.tex:441-460` states a theorem:
\[
\cF_\cC\simeq \cF^{E_1}_\cC\otimes_{E_0}\cF^{E_2}_\cC.
\]

Dunn additivity identifies the tensor product of operads \(E_1\otimes E_2\simeq E_3\). It lets an \(E_3\)-algebra be regarded as an \(E_1\)-algebra object in \(E_2\)-algebras, or conversely depending on conventions. It does not canonically factor a particular \(E_3\)-algebra as a tensor product of an \(E_1\)-algebra and an \(E_2\)-algebra. Such a splitting requires extra product/separation data on the space, a collar/product chart, or a factorisation-homology/Fubini theorem with hypotheses.

The problem propagates to `chapters/theory/e2_chiral_algebras.tex:504-557`, where the transverse factor is claimed `ProvedHere` equal to the derived Drinfeld centre. The centre identification may be true under the Ben-Zvi--Francis--Nadler/Francis hypotheses, but it cannot be proved by a nonexistent canonical Dunn tensor-factor split.

HEAL.

Proposed replacement for `chapters/theory/e2_chiral_algebras.tex:428-439`:

```tex
At \(d=3\), the Stage-1 object is treated on the verified locus as an
\(E_3\)-holomorphic factorisation algebra after a formality/framing datum
has been fixed. Dunn--Lurie additivity identifies the operadic grammar
\(E_3\simeq E_1\otimes E_2\); it permits restriction to a longitudinal
\(E_1\)-structure and exposes the transverse \(E_2\)-centraliser problem.
It does not by itself split \(\cF_\cC\) as a tensor product of two
independent factorisation algebras. The transverse \(E_2\) object is the
derived chiral centre only after the factorisation-homology/Fubini and
dualisability hypotheses are imposed.
```

Proposed status change for `chapters/theory/e2_chiral_algebras.tex:441-489`:

```tex
\ClaimStatusConditional{}
```

and replace the displayed tensor-product decomposition by:

```tex
\[
\cF_\cC \in \Alg_{E_1}\bigl(\Alg_{E_2}(\HolFA(X))\bigr)
\]
after choosing the Dunn presentation \(E_3\simeq E_1\otimes E_2\);
no canonical factorisation
\(\cF_\cC\simeq \cF^{E_1}_\cC\otimes_{E_0}\cF^{E_2}_\cC\) is asserted.
```

For `chapters/theory/e2_chiral_algebras.tex:504-557`, downgrade to:

```tex
\ClaimStatusConditional{}\textup{(dualisability, factorisation-homology
Fubini, and chiral Hochschild comparison hypotheses)}
```

unless those hypotheses are verified in the surrounding chapter.

## Consolidated replacement doctrine

Use the following hierarchy consistently:

```tex
Deligne--Tamarkin:
  \(\CC^\bullet(\cC,\cC)\) has an \(E_2\)-structure via braces.

Cyclic CY data:
  \(\HH^\bullet(\cC)\) has a BV algebra; chain level has homotopy
  framed-\(E_2\) after cyclic Deligne data.

Stage-1 CY3 \(E_3\):
  conditional on a chosen \(E_3\)-formality/framing datum and the verified
  Costello--Li holomorphic locus; not a consequence of BV alone.

Stage-2 CY3 output:
  \(\Phi_3^{(\Sigma_2,C)}(\cC)\in E_1\)-ChirAlg\((C)\).

Braiding at \(d=3\):
  lives on \(\mathcal Z(\Rep^{E_1}(A))\) or
  \(\Rep^{E_2}(Z^{\mathrm{der}}_{\mathrm{ch}}(A))\), not on \(A\).
```

## Exact local anchors for integration

- Main overclaim block: `chapters/theory/cy3_chain_level_bridge.tex:399-415`.
- Braces proposition to retitle/retype: `chapters/theory/cy3_chain_level_bridge.tex:417-453`.
- BV/framed \(E_2\) proposition to weaken at chain level: `chapters/theory/cy3_chain_level_bridge.tex:455-491`.
- Dunn \(E_3\)-from-BV proposition to replace: `chapters/theory/cy3_chain_level_bridge.tex:493-518`.
- Stage-1 envelope theorem whose hypothesis/status must be conditional: `chapters/theory/cy3_chain_level_bridge.tex:547-609`.
- Correct native curve-level rule: `chapters/theory/cy_to_chiral.tex:278-284`.
- Correct three-step/formality source lane: `chapters/theory/cy_to_chiral.tex:287-300`, `chapters/theory/cy_to_chiral.tex:313-351`.
- Correct non-rigidification warning: `chapters/theory/cy_to_chiral.tex:407-409`.
- Correct \(E_2\)-on-centre location: `chapters/theory/cy_to_chiral.tex:437-443`.
- Correct Stage-2 \(E_1\) output rule: `chapters/theory/cy_to_chiral.tex:540-568`.
- Correct \(d=3\) chapter-scope warning: `chapters/theory/e2_chiral_algebras.tex:15-46`.
- Cyclic \(E_2\)/framed source statement: `chapters/theory/e2_chiral_algebras.tex:117-129`.
- \(d=3\) centre conjecture statement: `chapters/theory/e2_chiral_algebras.tex:188-210`.
- Dunn-splitting overclaim: `chapters/theory/e2_chiral_algebras.tex:424-489`.
- Derived-centre theorem needing hypotheses/status pressure: `chapters/theory/e2_chiral_algebras.tex:504-557`.

## Tests/build

No tests or builds run. This was a report-only operadic audit; user instructed no chapter or compute edits.

Files changed: `notes/adversarial_swarm_20260424_hol_e3/agent_02_drinfeld_kazhdan_operads.md` only.
