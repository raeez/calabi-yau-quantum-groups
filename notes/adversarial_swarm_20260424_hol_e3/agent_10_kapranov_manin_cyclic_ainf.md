# Agent 10 -- Kapranov/Manin cyclic Ainf adversarial report

Date: 2026-04-24.

Scope: cyclic `A_infinity` input for the holomorphic `E_3`/CY3 surface:
smooth properness, Calabi--Yau pairing degree, Hochschild chains versus
cochains, the Connes operator, the BV operator, Koszul signs, and the
correct carrier `HH^bullet` versus `HH_bullet`. This report reads the live
working tree and proposes replacement language only. No chapter or compute
file is edited here.

## Verification surface

Primary manuscript anchors:

- `chapters/theory/cyclic_ainf.tex:55`: cyclic `A_infinity` algebra definition.
- `chapters/theory/cyclic_ainf.tex:59`: pairing degree `-d`.
- `chapters/theory/cyclic_ainf.tex:61`: nonzero pairing only when `|a|+|b|=d`.
- `chapters/theory/cyclic_ainf.tex:63`: cyclic invariance sign.
- `chapters/theory/cyclic_ainf.tex:73`: Hochschild pairing on chains.
- `chapters/theory/cyclic_ainf.tex:80`: negative cyclic lift.
- `chapters/theory/cyclic_ainf.tex:84`: trace lives in `HC^-_d`, not a raw `HH_d -> k` slogan.
- `chapters/theory/cyclic_ainf.tex:115`: cyclic invariance controls adjacent contractions only.
- `chapters/theory/cyclic_ainf.tex:210`: three Hochschild theories are distinct.
- `chapters/theory/cyclic_ainf.tex:242`: CY3 chain-level `S^3` framing is input or separately verified witness.
- `chapters/theory/cy_to_chiral.tex:147`: CY trace versus chiral OPE gap.
- `chapters/theory/cy_to_chiral.tex:149`: cyclic `A_infinity`, Connes `B`, and `S^d` framing live on Hochschild homology.
- `chapters/theory/cy_to_chiral.tex:153`: `d=3` output is `E_1` after specialization.
- `chapters/theory/cy_to_chiral.tex:287`: Stage 1 uses `HH^bullet(C)` as the cochain algebra.
- `chapters/theory/cy_to_chiral.tex:290`: hypotheses H1--H4.
- `chapters/theory/cy_to_chiral.tex:300`: Step (a) is Kontsevich/Tamarkin formality on `HH^bullet`.
- `chapters/theory/cy_to_chiral.tex:473`: source is `CY_d-Cat^dg`.
- `chapters/theory/cy_to_chiral.tex:479`: CY datum is a degree `-d` cyclic pairing witnessed by `C ~= C^vee[d]`.
- `chapters/theory/cy3_chain_level_bridge.tex:542`: Tradler--Menichi--Ginzburg BV operator.
- `chapters/theory/cy3_chain_level_bridge.tex:549`: `Delta: HH^bullet -> HH^{bullet-1}`.
- `chapters/theory/cy3_chain_level_bridge.tex:583`: `E_3` lift is extra Stage-1 data.
- `chapters/theory/cy3_chain_level_bridge.tex:590`: BV/framed `E_2` does not by itself produce `E_3`.
- `chapters/theory/drinfeld_center.tex:330`: TCFT statement for `{b,B^(2)}=0`.
- `chapters/theory/drinfeld_center.tex:337`: Connes `B` is a chain operator of degree `-1` in that chapter's cohomological convention.
- `chapters/theory/drinfeld_center.tex:1139`: `S^3` framing on `HH_bullet(C)` gives an `E_3` structure whose `E_2` restriction is symmetric.

Primary compute anchors:

- `compute/lib/cy3_hochschild.py:434`: HKR convention for `HH_p`.
- `compute/lib/cy3_hochschild.py:488`: Connes rank convention `B: HH_p -> HH_{p+1}` in the homological/HKR engine.
- `compute/lib/cy3_hochschild.py:1193`: `S^1` data is only the first step toward `S^3` framing.
- `compute/lib/ks_cyclic_minimal_obs_ainf.py:10`: `Obs_Ainf` recorded as a genuine open obstruction for non-formal CY3.
- `compute/lib/ks_cyclic_minimal_obs_ainf.py:14`: bidegree proof recorded as retracted in the KS engine.
- `compute/lib/ks_cyclic_minimal_obs_ainf.py:70`: cyclic sign convention matching the chapter definition.
- `compute/lib/ks_cyclic_minimal_obs_ainf.py:320`: direct non-vanishing statement for `[m_3,B^(2)]`.
- `compute/lib/obs_ainf_local_p2.py:402`: explicit CY3 Serre pairing.
- `compute/lib/obs_ainf_local_p2.py:417`: pairing vanishes unless degrees sum to `3`.
- `compute/lib/obs_ainf_local_p2.py:153`: scratch discussion of `B^(2)` ambiguity.
- `compute/lib/obs_ainf_local_p2.py:315`: explicit local P2 finite model.
- `compute/lib/connes_b_obs_ainf.py:504`: bidegree engine claims individual `[m_k,B^(j)]=0`.
- `compute/lib/connes_b_obs_ainf.py:551`: bidegree engine claims `[m_k,B^(2)]=0`.
- `compute/tests/test_ks_cyclic_minimal_obs_ainf.py:357`: test suite says the bidegree engine exists even though its proof was retracted.
- `compute/tests/test_obs_ainf_local_p2.py:5`: local P2 test suite asserts `[m_3,B^(2)] != 0` for non-formal cyclic CY3.
- `compute/tests/test_connes_b_obs_ainf.py:343`: Connes bidegree test suite asserts the opposite theorem.

Tests run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider \
  compute/tests/test_ks_cyclic_minimal_obs_ainf.py \
  compute/tests/test_obs_ainf_local_p2.py \
  compute/tests/test_connes_b_obs_ainf.py \
  compute/tests/test_cy3_hochschild.py \
  compute/tests/test_e3_hochschild_deformation.py
```

Result: `316 passed in 1.53s`.

The passing suite does not resolve the mathematics: it contains mutually
inconsistent theorem-status assertions. The `connes_b` tests encode the
bidegree proof as true; the KS/local-P2 tests encode the non-formal
counterexample as true.

Direct probes:

```text
KS perspective, max_length=4:
  C^3, m_3: 0/256 nonzero.
  local P^2, m_3: 2/256 nonzero.
  example: ('a','a','b','e') -> {(): -2}.

local P2 8-generator model:
  [a|a|a|a|b] -> 2*[b].
  [a|a|b|a|a] -> 4*[b].
  CC_4: 10 nonzero elements out of 243.
  CC_5: 57 nonzero elements out of 729.
  master status: obs_ainf_vanishes=False, gap_status=REAL.

HKR chain dimensions:
  K3xE: HH = {0:4, 1:44, 2:44, 3:4}, total 96, HC^- = {0:48, 1:48, 2:44, 3:4}.
  quintic: HH = {0:2, 1:102, 2:102, 3:2}, total 208, HC^- = {0:104, 1:104, 2:102, 3:2}.
```

## Verdict

The cyclic `A_infinity` input is not a license to identify all Hochschild
carriers. The correct local convention is a carrier split:

- `HC^-_bullet(C)` and its associated `HH_bullet(C)` carry the Calabi--Yau
  trace, Connes `S^1` data, and `S^d` framing input.
- `HH^bullet(C)` carries the Gerstenhaber/Deligne cochain algebra used in
  Stage 1 of `PhiFA_d`.
- The Tradler--Menichi--Ginzburg BV operator is a cochain operator
  `Delta: HH^bullet -> HH^{bullet-1}` after the cyclic pairing has been
  fixed.
- The `E_3` lift at CY3 is extra Stage-1 data on the verified locus; a
  framed `E_2`/BV structure does not manufacture it.
- The final CY3 chiral output after specialization is `E_1`, not `E_3`.
- Smooth properness plus a cyclic pairing is necessary source data; it is
  not enough to assert automatic non-formal CY3 chain-level compatibility.

The current safe theorem is formal/verified-locus conditional. For formal
models such as the flat `C^3` minimal model, the `A_infinity` obstruction
vanishes trivially because `m_k=0` for `k>=3`. For non-formal models, local
compute witnesses show that cyclic invariance alone does not imply
termwise `[m_3,B^(2)]=0`.

## Exact conventions

1. Grading: cohomological, `|d|=+1`.

2. `A_infinity` operations:
   \[
     \mu_n:A^{\otimes n}\to A,\qquad |\mu_n|=2-n.
   \]

3. CY pairing:
   \[
     \langle-,-\rangle:A\otimes A\to k[-d],
   \]
   non-degenerate and graded symmetric. It is nonzero only on homogeneous
   pairs with `|a|+|b|=d`. For geometric CY3, this is Serre duality:
   \[
     Ext^i(F,G)\otimes Ext^{3-i}(G,F)\to H^3(X,\omega_X)\simeq k.
   \]

4. Cyclic sign:
   \[
     w(a_0,\ldots,a_n)
     =
     (-1)^{n+|a_0|(|a_1|+\cdots+|a_n|)}
     w(a_1,\ldots,a_n,a_0),
   \]
   where
   \[
     w(a_0,\ldots,a_n)=\langle a_0,\mu_n(a_1,\ldots,a_n)\rangle.
   \]
   Equivalently, in the chapter indexing,
   \[
     \langle\mu_n(a_1,\ldots,a_n),a_{n+1}\rangle
     =
     (-1)^{n+|a_1|(|a_2|+\cdots+|a_{n+1}|)}
     \langle a_1,\mu_n(a_2,\ldots,a_{n+1})\rangle.
   \]

5. Negative cyclic CY structure: the CY trace is a negative cyclic class
   \[
     [\sigma_C]\in HC^-_d(C),
   \]
   or equivalently a cyclically invariant non-degenerate trace compatible
   with Connes `B`. A raw map `HH_d(C)->k` is only the shadow after
   forgetting the `S^1`-equivariant structure.

6. HKR chain convention for compact CY `d`:
   \[
     HH_p(Perf(X))=\bigoplus_q H^q(X,\wedge^p T_X)
     \simeq \bigoplus_q H^q(X,\Omega_X^{d-p}).
   \]

7. Connes convention: in the HKR homological engine, `B: HH_p -> HH_{p+1}`.
   In cohomological manuscript conventions the same circle generator may
   be recorded with degree `-1` after duality/shift. The sign of `B` must
   always be stated with its carrier.

8. BV convention: the Tradler--Menichi--Ginzburg operator is
   \[
     \Delta:HH^\bullet(C)\to HH^{\bullet-1}(C).
   \]
   It is not the same object as Connes `B` on chains, although it is
   obtained from the cyclic structure by duality and cyclic Deligne
   homotopies.

## ATTACK -> HEAL cycles

### Cycle 1 -- Smooth properness is necessary, not sufficient

ATTACK. Treat any smooth proper cyclic `A_infinity` category as an
automatic CY3 Stage-1 holomorphic `E_3` input.

FAILURE MODE. The source category definition requires smooth properness,
connected unit, and a degree `-d` cyclic pairing witnessed by
`C ~= C^vee[d]`. The CY3 theorem adds a fixed specialization datum and
chain-level witnesses. The chapter explicitly says the CY3 chain-level
`S^3` framing is an input datum or separately verified toric/formal
witness, not a consequence of smooth properness alone.

HEAL. State smooth properness as the source finiteness condition, then
state the CY3 framing separately.

Replacement language:

```tex
A CY$_d$ input is a smooth proper dg-category $\mathcal C$ over
$\mathbb C$ with $\HH^0(\mathcal C)=\mathbb C$ and a negative-cyclic
Calabi--Yau class $[\sigma_{\mathcal C}]\in HC^-_d(\mathcal C)$,
equivalently a non-degenerate cyclic pairing of degree $-d$ witnessed by
$\mathcal C\simeq\mathcal C^\vee[d]$ as a bimodule.  For $d=3$ this is
only the source datum: the Stage-1 holomorphic object additionally
requires the chosen chain-level $S^3$-framing and Costello--Li witness on
the verified locus.
```

Status recommendation: any theorem saying "smooth proper cyclic CY3
therefore Stage-1 `E_3`" should be weakened to "on the verified
framed/TCFT/formal locus".

### Cycle 2 -- The CY trace is not a raw `HH_d -> k` datum

ATTACK. Use the phrase "the trace is a map `HH_d(C)->k`" as if it were
the complete cyclic input.

FAILURE MODE. The cyclic chapter immediately refines the trace to a
negative cyclic class closed under the Connes differential. The raw
Hochschild map forgets the `S^1`-equivariance required for the framing.

HEAL. Keep both levels visible: raw Hochschild trace as shadow, negative
cyclic class as actual CY datum.

Replacement language:

```tex
The Hochschild trace $\HH_d(\mathcal C)\to k$ is the underlying
Hochschild shadow of the Calabi--Yau structure.  The structure used by
$\Phi_d$ is the negative-cyclic lift
$[\sigma_{\mathcal C}]\in HC^-_d(\mathcal C)$; its Connes-closedness is
the $S^1$-equivariant datum from which the framed Hochschild theory is
built.
```

Status recommendation: replace isolated "trace on `HH_d`" claims in
CY-to-chiral construction statements by "negative-cyclic CY trace, whose
Hochschild shadow is `HH_d -> k`".

### Cycle 3 -- `HH^bullet` and `HH_bullet` are both correct, in different slots

ATTACK. Ask whether `HH^bullet` or `HH_bullet` is the correct carrier and
force a single answer.

FAILURE MODE. The chapters use both, but not interchangeably. The cyclic
trace and `S^d` framing are on `HH_bullet` refined to `HC^-_bullet`.
Stage 1 uses Kontsevich/Tamarkin formality on the Hochschild cochain
complex `HH^bullet(C)`. The BV operator in the chain-level bridge is also
written on `HH^bullet(C)`. PTVV-style loop-space language points back to
`HC^-_bullet` for the `S^1`-equivariant loop object.

HEAL. Install a carrier table.

Replacement language:

```tex
There are two Hochschild carriers.  The Calabi--Yau trace, Connes
operator, and $S^d$-framing live on Hochschild chains, more precisely on
the negative-cyclic refinement $HC^-_\bullet(\mathcal C)$.  The
Gerstenhaber bracket, Deligne action, and Stage-1 formality algebra live
on Hochschild cochains $\HH^\bullet(\mathcal C)$.  The cyclic pairing
identifies the two only after the degree-$d$ duality convention has been
fixed; it does not license replacing one by the other in formulas.
```

Status recommendation: theorem statements should name the carrier in
each sentence. Never write "the Hochschild complex" in this lane unless
the next clause says chains, cochains, or negative cyclic.

### Cycle 4 -- Connes `B^(2)` is the dangerous operator

ATTACK. Prove `[m_k,B^(2)]=0` from cyclic invariance, or from the
pairing-weight decomposition in `compute/lib/connes_b_obs_ainf.py`.

FAILURE MODE. The cyclic chapter says cyclic invariance controls adjacent
contractions only. The KS engine and local P2 engine produce explicit
nonzero commutators in non-formal models while cyclic invariance still
holds. The bidegree engine asserts individual vanishing, but the KS tests
state the proof was retracted: the mixed complex axiom for the ordinary
Connes operator does not by itself imply `[b,B^(j)]=0` for each higher
hierarchy component. "Pairing weight" is metadata about which operation
was used, not automatically a grading of the target endomorphism complex
unless an actual projected Connes hierarchy has been constructed.

HEAL. Separate three statements.

Replacement language:

```tex
Cyclicity of the $A_\infty$ operations does not imply the termwise
identity $[m_k,B^{(2)}]=0$.  It controls the cyclic block containing
$m_k$ and its pairing partner; non-adjacent contractions of the
Connes-hierarchy operator are a separate chain-level condition.  On
formal minimal models the commutator vanishes trivially because
$m_k=0$ for $k\ge3$.  On a non-formal cyclic CY$_3$ minimal model, the
naive all-pairs contraction gives nonzero witnesses.  A positive theorem
must therefore use the true TCFT Connes-hierarchy operator together with
an explicit homotopy, or restrict to the verified formal/TCFT locus.
```

Status recommendation: do not cite `compute/lib/connes_b_obs_ainf.py` as
a proof of universal `Obs_Ainf=0` until the premise "higher
`B^(j)` components split as chain maps in the required projected
hierarchy" is independently reconstructed. The local tests passing only
prove the code's internal assertions.

### Cycle 5 -- The BV operator is not Connes `B`, and not an `E_3` machine

ATTACK. Identify the BV operator with Connes `B` on chains, or use the
framed `E_2`/BV layer to assert the missing `E_3` lift.

FAILURE MODE. The chain-level bridge defines the BV operator as
`Delta: HH^bullet(C) -> HH^{bullet-1}(C)`. Its proof uses cyclic
rotation averages, the cyclic pairing, and the cyclic Deligne theorem.
The same bridge says this gives framed `E_2`/`BV_infinity`, and does not
by itself produce `E_3`; the `E_3` lift is extra Stage-1 data fixed by a
formality point, a CY3 chain-level framing, and a Costello--Li witness.
The hCS BV bracket is a second BV object: an odd Poisson bracket on local
functionals, not the Tradler cochain operator.

HEAL. Keep the BV layers disjoint.

Replacement language:

```tex
The cyclic pairing gives the Tradler--Menichi--Ginzburg operator
$\Delta:\HH^\bullet(\mathcal C)\to\HH^{\bullet-1}(\mathcal C)$ and hence
a framed $E_2/BV_\infty$ structure on Hochschild cochains.  This operator
is obtained from the chain-level cyclic structure by duality; it is not
the Connes boundary on chains.  The CY$_3$ $E_3$ lift is an additional
Stage-1 datum and remains conditional outside the verified framed locus.
```

Status recommendation: reserve `B` for Connes-chain operators and
`Delta` for BV cochain operators. Reserve `{-,-}_{BV}` for field-theory
odd Poisson brackets on observables.

### Cycle 6 -- The signs are load-bearing

ATTACK. Suppress the cyclic sign and rely on "up to Koszul sign" in the
cyclic `A_infinity` input.

FAILURE MODE. The local P2 witnesses are pure sign-sensitive statements:
`[m_3,B^(2)](a,a,b,e)=-2` in the KS model, and
`[a|a|a|a|b] -> 2*[b]` in the 8-generator model. The sign convention also
fixes the degree of `mu_3` as `-1` and the pairing as degree `-3` in CY3.

HEAL. Write the sign once and use it everywhere.

Replacement language:

```tex
We use cohomological grading and $|\mu_n|=2-n$.  For
$w(a_0,\ldots,a_n)=\langle a_0,\mu_n(a_1,\ldots,a_n)\rangle$, cyclicity
means
\[
  w(a_0,\ldots,a_n)
  =
  (-1)^{n+|a_0|(|a_1|+\cdots+|a_n|)}
  w(a_1,\ldots,a_n,a_0).
\]
The pairing is graded symmetric of degree $-d$ and vanishes unless
$|a|+|b|=d$.
```

Status recommendation: any future compute witness for `B^(2)` must print
the sign convention next to the nonzero example; otherwise it is not a
mathematical witness.

### Cycle 7 -- Universal `Obs_Ainf=0` is not supported

ATTACK. State that cyclic `A_infinity` compatibility kills the `A_infinity`
obstruction for all CY3 inputs.

FAILURE MODE. Formal `C^3` is harmless. Non-formal local P2 is not:
cyclic invariance holds, `A_infinity` relations hold through the tested
range, the pairing has CY3 degree, and the commutator remains nonzero in
two independent local engines. The live manuscript already carries the
safer scope: CY3 Stage 1 is on a verified object-level locus with
chain-level witnesses.

HEAL. State the theorem as a verified-locus theorem, and state the
non-formal obstruction as the named proof obligation.

Replacement language:

```tex
On the formal CY$_3$ locus, and on loci where the Costello open-closed
TCFT supplies the actual Connes-hierarchy homotopy, the cyclic
$A_\infty$ input is compatible with the Stage-1 framing.  Outside those
loci the termwise identity $[m_k,B^{(2)}]=0$ is not a consequence of
cyclic invariance; non-formal minimal models exhibit nonzero naive
commutators.  The open proof obligation is to construct the true
TCFT-level $B^{(2)}$ operator and its homotopy, or to keep the CY$_3$
statement restricted to the verified framed locus.
```

Status recommendation: mark universal non-formal `Obs_Ainf=0` as
unsupported. Mark formal `C^3` and explicit verified TCFT loci as
available.

## Replacement theorem block

The following block is the safe replacement for overloaded cyclic
`A_infinity` input claims:

```tex
\begin{theorem}[Cyclic input, carriers, and CY$_3$ scope]
Let $\mathcal C$ be a smooth proper dg-category over $\mathbb C$ with
$\HH^0(\mathcal C)=\mathbb C$ and a negative-cyclic Calabi--Yau class
$[\sigma_{\mathcal C}]\in HC^-_d(\mathcal C)$, equivalently a
non-degenerate degree-$(-d)$ cyclic pairing witnessed by
$\mathcal C\simeq\mathcal C^\vee[d]$ as a bimodule.  The Hochschild-chain
carrier $HC^-_\bullet(\mathcal C)\to\HH_\bullet(\mathcal C)$ contains the
trace, Connes operator, and framing data.  The Hochschild-cochain carrier
$\HH^\bullet(\mathcal C)$ contains the Gerstenhaber bracket, Deligne
action, and the Stage-$1$ formality algebra.  The cyclic pairing relates
the two carriers by Calabi--Yau duality after the degree convention has
been fixed.

For $d=3$, this source datum does not by itself give an unconditional
Stage-$1$ holomorphic $E_3$ object.  The construction is valid on the
verified framed locus: a formality point, the CY$_3$ chain-level
$S^3$-framing, and the Costello--Li holomorphic witness are part of the
input.  After admissible specialization $(\Sigma_2,C)$ the output is an
$E_1$-chiral algebra on $C$.
\end{theorem}
```

## Patches to avoid

- Do not replace `HH_bullet` by `HH^bullet` globally.
- Do not cite `HH_d -> k` without the negative cyclic lift.
- Do not use `Delta` and `B` for the same operator.
- Do not assert `[m_k,B^(2)]=0` from cyclic invariance alone.
- Do not cite the bidegree engine as theorem support until the
  higher-Connes hierarchy premise is repaired.
- Do not upgrade the final CY3 chiral output from `E_1` to `E_3`.

## Open proof obligation

The exact missing object is not another status label. It is a chain-level
operator/homotopy package:

```tex
(CC_\bullet(\mathcal C), b=\sum_k m_k, B^{(0)}, B^{(1)}, B^{(2)},\ldots; H)
```

with:

1. a carrier specified as cyclic chains or negative cyclic chains;
2. a formula for the true `B^(2)`, not the naive all-pairs contraction;
3. Koszul signs fixed relative to `|\mu_n|=2-n`;
4. a homotopy identity showing the relevant TCFT compatibility;
5. a comparison explaining why the local P2 naive nonzero witnesses are
   outside the true operator, or else a restriction excluding non-formal
   inputs.

Until that package is written, the honest statement is conditional on the
formal/verified TCFT locus.
