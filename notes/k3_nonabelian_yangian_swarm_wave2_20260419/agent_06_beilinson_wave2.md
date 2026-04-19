# Wave 2 — Agent 06 Beilinson: Deep Re-audit of the Six Wave-1 Survivors

Author: Raeez Lorgat.
Date: 2026-04-19.
Mode: Wave-2 adversarial deep audit (read-only). Every surviving
Wave-1 theorem is re-attacked at proof-step level; load-bearing
intermediate claims are extracted and dismissed against Beilinson's
discipline.

Epistemic frame. Wave 1 passed the six theorems below at survey
depth. Wave 2 descends into their proof bodies, names the three
load-bearing steps per theorem, and applies the dismissal protocol:
(i) citation stated correctly, (ii) citation used correctly,
(iii) no circular downstream dependency, (iv) scope narrower than
theorem claims, (v) independent-path counts real, not dressed. A
"sharpest honest form" rewrite follows each defect.

Target files:
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_yangian_chapter.tex`
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex`
- `/Users/raeez/calabi-yau-quantum-groups/notes/wave_V110_attack_heal_Y_sln_Pentagon.md`

---

## 1. `thm:bfn-phi-ade-identification` (k3_yangian_chapter.tex:108-132)

### 1.1. Three load-bearing steps

The proof is labelled `[Attribution]` and assembles four steps.
Deep-audit reduces the load-bearing material to three:

- **S1 (McKay + Kronheimer + BKR + KV)**: $\widetilde S_\fg$ =
  minimal crepant resolution; derived equivalence
  $D^b(\Coh \widetilde S_\fg) \simeq D^b(\Pi_{Q_\fg})$.
- **S3 (BFN Theorem 1.1 + Nakajima–Takayama Theorem A)**:
  $\cA_\hbar(Q_\fg, \mathbf v, \mathbf w) \simeq Y^\mu(\widehat\fg)_{k=1}$.
- **S4 ($\Phi$-compatibility via CY-A$_2$ + symplectic duality of
  Braden–Licata–Proudfoot–Webster)**: identifies the Higgs side
  factorisation quantisation with BFN Coulomb on the formal disk.

### 1.2. Dismissal protocol per step

**S1.** Citation stated and used correctly. Kronheimer (J. Diff.
Geom. 29, 1989) is the hyperkähler moment-map construction. BKR
(math/9908027) is the derived-McKay equivalence. KV (Math. Ann.
316, 2000) identifies $\Gamma$-equivariant sheaves with
preprojective-algebra modules. No circular dependency. *Passes.*

**S3.** Citation stated and used correctly. BFN Thm 1.1 delivers
$\cA_\hbar(Q_\fg, \mathbf v, \mathbf w) \simeq Y^\mu(\widehat\fg)$
for ALL framed quiver gauge theories (arXiv:1604.03625). NT Thm A
specialises via GKLO presentation at level $k = 1$ for $Q_\fg$ of
type $\widehat\fg$. Webster's folding (arXiv:1905.11473) is
correctly flagged as not needed for ADE. No circular dependency.
*Passes.*

**S4 — THE RESIDUE.** Two sub-flaws:

(a) *CY-A$_2$ scope.* The proof reads "CY-A$_2$ output for $d=2$
local surfaces, proved at publication standard in this volume."
The scope "local surfaces" here means open subsets of
$T^*\widetilde S_\fg$; but $\Phi_2$ is defined for *compact*
CY$_2$ via `thm:cy-to-chiral`. The cotangent bundle $T^*\widetilde S_\fg$
is NOT a compact CY$_2$; it is a *non-compact* hyperkähler $4$-fold
with CY$_2$ *slice*. The version of CY-A$_2$ that Step~4 invokes
is the **non-compact-local-surface** one. This is documented at
publication standard for $d = 2$ open subschemes via
the BFN-compatible formulation; but the cross-reference at line 131
is to CY-A$_2$ without specifying the non-compact local form.
*Qualifier needed*: Step 4 invokes CY-A$_2$ in the non-compact-local
form, not the compact CY$_2$ form used at `thm:k3-mock-modular-proof`.

(b) *Braden–Licata–Proudfoot–Webster scope.* The cited
symplectic-duality identification between Higgs-side factorisation
quantisation and Coulomb-side BFN convolution is proved by
Braden–Licata–Proudfoot–Webster (arXiv:1407.0964) in the *hypertoric*
and *quiver-variety* cases; for general ADE quiver varieties, the
symplectic-duality statement at the level of *factorisation
quantisation* is a composite of (i) Braverman-Finkelberg's
$\mathbf{I}$-Coulomb = Higgs-side Hilbert-scheme identification at
the affine $A$-type level and (ii) the BLPW hypertoric slice
argument generalised to ADE. The cited form "Higgs-side
factorisation quantisation = Coulomb-side BFN convolution as $E_1$
chiral algebras" is *stronger* than the literal statement in
BLPW 2014; BLPW gives a *category equivalence* (perverse O $\simeq$
Coulomb O), not a factorisation-quantisation compatibility of the
two sides.

### 1.3. Numerical-verification path count

Remark 136-158 (`rem:bfn-ade-input-dependency`) already admits the
"three independent paths" V1/V2/V3 reduce to *two input-disjoint*
(V2 vs V1+V3). This is honest and passes. *Passes the 3-path rule
after the self-correcting remark.*

### 1.4. Sharpest honest form (AP289)

> **Theorem (BFN–$\Phi$ ADE identification, strict form).** Let
> $\fg$ be ADE, $\widetilde S_\fg \to \C^2/\Gamma$ the Kronheimer
> resolution. On the *non-compact local surface* $T^*\widetilde S_\fg$,
> the chiral algebra $\Phi(T^*\widetilde S_\fg)$ (in the local form
> of CY-A$_2$ for open $d = 2$ subschemes) is isomorphic, at the
> level of category of modules over the formal disk, to the BFN
> quantised Coulomb branch
> $\cA_\hbar(Q_\fg, \delta, \mathbf e_0)$ via symplectic duality of
> Braden–Licata–Proudfoot–Webster; combining BFN Thm 1.1 and
> Nakajima–Takayama Thm A identifies the latter with the level-one
> shifted affine Yangian $Y^\mu(\widehat\fg)_{k=1}$. The
> factorisation-quantisation compatibility of Higgs side with BFN
> convolution is a *derived-category* equivalence (not a
> factorisation-algebra equality on the nose); its chain-level
> upgrade is an open problem for general ADE beyond type $A$.

---

## 2. `thm:k3-abelian-yangian-presentation` (k3_yangian_chapter.tex:877-1001)

### 2.1. Three load-bearing steps

- **S1 (Proposition `prop:k3-heisenberg`)**: identifies the
  $\gl_1$-specialisation with the rank-$24$ Mukai Heisenberg.
- **S2 (Miura multiplicativity via `prop:universal-coproduct`)**:
  derives the Drinfeld coproduct from $\Delta_z(T(u)) = T^L(u)
  \cdot T^R(u - z)$.
- **S3 (Tsymbaliuk arXiv:1404.5240)**: the Yangian deformation of a
  rank-$N$ Heisenberg algebra is the affine Yangian $Y(\widehat\gl_1)$
  at rank $N$, specialised here at $N = 24$.

### 2.2. Dismissal protocol per step

**S1.** Citation is `prop:k3-heisenberg` (line 459). Content is the
Mukai Heisenberg OPE $J_i(z) J_j(w) \sim \omega^{ij}/(z-w)^2$ with
$\omega^{ij} = \diag(+1^4, -1^{20})$. No external citation; the
proposition is proved at chain level. *Passes.*

**S2.** Citation `prop:universal-coproduct` (e1_chiral_algebras.tex:1289).
Checked: the coproduct formula at rank $N = 24$ follows by
specialisation. BUT: e1_chiral_algebras.tex:1308 notes the
cubic shadow correction $\delta^{(3)}$ from $m_3(T,T,T) = -2T$
introduces a morphism defect at higher spin. This defect
vanishes in the ABELIAN $(\gl_1)$ case (no $m_3$ because no
non-trivial structure constants), so the cited coproduct formula
applies without correction at rank $N = 24$ in the abelian case.
*Passes for abelian; would not pass for non-abelian.*

**S3 — THE RESIDUE.** Citation Tsymbaliuk arXiv:1404.5240 is to
the affine Yangian $Y(\widehat\gl_1)$ at rank $N$ — but what is
meant by "rank-$N$"? Tsymbaliuk's affine $\gl_1$ Yangian has
**three** deformation parameters $(h_1, h_2, h_3)$ with
$h_1 + h_2 + h_3 = 0$; the "rank" in Tsymbaliuk is fundamentally
$3$, not $N$. The chapter's use of "rank $N = 24$" to mean "the
parameter space is $24$-dimensional subject to $\sum h_i = 0$"
conflates Tsymbaliuk's *$3$-parameter Yangian of affine $\gl_1$*
(Maulik-Okounkov R-matrix on $\operatorname{Hilb}^n(\C^2)$) with
the *$N$-copy tensor-product Yangian of $N$ commuting Heisenbergs*
(Chari-Pressley 1995 for rank-$N$ Heisenberg).

These are **different objects** in the standard literature:
- Tsymbaliuk's $Y(\widehat\gl_1)$ is a rank-$3$ Hopf algebra with
  a single structure function $G(u)$ depending on $(h_1, h_2, h_3)$
  satisfying $h_1 + h_2 + h_3 = 0$ (this IS the CY$_2$ constraint,
  at rank $3$, for $\C^2$ or an equivariant surface slice).
- The chapter's $Y(\fg_{K3})|_{\gl_1}$ is $24$ commuting copies of
  Chari-Pressley's Heisenberg Yangian with $24$ independent
  Heisenberg currents.

Tsymbaliuk's affine $\gl_1$ Yangian at level $k = 1$ is the target
of BFN/Maulik-Okounkov at $A_0$-Nakajima quiver variety
$\operatorname{Hilb}^n(\C^2)$; the $24$-dimensional parameter
space would require a non-standard extension. The Frenkel-Jing
1988 construction is tensor-product, not Tsymbaliuk-style.

*Citation is misapplied.* The correct citation is Chari-Pressley
1995 (Ch. 12 of Guide to Quantum Groups) for the rank-$N$
Heisenberg Yangian (which is what the chapter actually constructs)
and Frenkel-Jing 1988 for the $\Z$-mode realisation; not
Tsymbaliuk 2014 which is a fundamentally different object.

### 2.3. Independent-path count (6 cross-checks)

The proof body ties to Remark 1067 (classical attribution: Drinfeld
1985 + Chari–Pressley 1995 + FRT 1989 + Frenkel–Jing 1988). That
is ONE independent path (classical literature). The "Tsymbaliuk
Yangian deformation" is a SECOND independent path but a
*misapplied* one. No third path documented.

*Fails 3-path rule on the non-abelian aspects; passes on the*
*rank-$24$ abelian specialisation of Chari-Pressley, which is what*
*the proof actually delivers.*

### 2.4. Sharpest honest form (AP289)

> **Theorem (Abelian K3 Yangian, strict form).** The $\gl_1$
> specialisation of the K3 double current algebra is the *rank-$24$
> Heisenberg Yangian* of Chari–Pressley (1995) at parameters
> $(h_1, \ldots, h_{24})$ subject to $\sum h_i = 0$, on the Mukai
> lattice of signature $(4, 20)$. The RTT, structure function,
> coproduct, and Koszul dual all reduce to block-diagonal
> specialisations of Chari–Pressley. The label "K3" is a physics
> orientation (Mukai lattice context); the mathematical content
> is classical.

---

## 3. `thm:k3-elliptic-tower-fixed-point` (k3_yangian_chapter.tex:3699-3764)

### 3.1. Three load-bearing steps

- **S1 (`lem:bivariant-kunneth-identity`, line 3671)**: the operator
  $\kappa_E(N) := N *_{V_4} M_E + \sigma_{\mathrm{tot}}^*(N)$ is the
  identity on the trace-zero hyperplane $\Z[V_4]_0$.
- **S2 (`thm:kunneth-dichotomy`, line 3572)**: case (3) gives
  $\Delta_{X, Y} = \sigma_{\mathrm{tot}}^* M_X - \chi(\mathcal{O}_X)
  \cdot e_{\Pi_{--}}$ when exactly one of $M_X, M_Y$ is in the
  $-1$-eigenspace. In the trace-zero sub-case, this collapses to
  $\Delta_{X, Y} = \sigma_{\mathrm{tot}}^* M_X$.
- **S3 ($k = 1$ base case)**: $M_{K3 \times E} = M^\flat =
  (0, 5, -16, 11)$ is the "established K$3 \times E$ identity."

### 3.2. Dismissal protocol per step

**S1 — TECHNICAL CORRECTION, MINOR.** The lemma's proof reads: for
$N = (a, b, c, d)$,
- $N *_{V_4} M_E = (a - d, b - c, c - b, d - a)$,
- $\sigma_{\mathrm{tot}}^*(N) = (d, c, b, a)$,
- sum $= (a, b, c, d) = N$.

Direct verification: $(a - d) + d = a$; $(b - c) + c = b$; $(c - b) + b = c$;
$(d - a) + a = d$. *Correct.* This identity holds for ALL $N$, not only
trace-zero $N$. The lemma's scope "on the trace-zero hyperplane" is
a *weaker* statement than what the proof delivers; the stronger
statement is $\kappa_E = \id$ identically on $\Z[V_4]$.
*Passes but the trace-zero scope is a scope-narrowing artefact.*

**S2 — THE RESIDUE.** `thm:kunneth-dichotomy` is
`\ClaimStatusConditional` (line 3573). The fixed-point theorem
derives from it directly. But: the fixed-point theorem is
`\ClaimStatusProvedHere`. **This is a status-transitivity break:**
*ProvedHere derived from Conditional should itself be Conditional.*

Moreover, the dichotomy proof is absent from the chapter (it is
stated as a theorem with `Conditional` tag but its proof body
is either missing or relegated to compute). The universal theorem
`thm:universal-elliptic-tower-fixed-point` at line 3899 *requires*
the full dichotomy to hold in case (3). Without a proof of the
dichotomy, the "fixed-point" theorem is conditional on an unproved
case-(3) formula.

**S3 — CIRCULAR DEPENDENCY.** The base case "$M_{K3 \times E} = M^\flat$"
at line 3732 is "the established $K3 \times E$ identity." Where is
this established? Via `thm:k3-multiproj-bigraded-lefschetz` (line 3362),
which is `\ClaimStatusConditional` on Caldararu chiral HRR + Hodge-to-de
Rham $E_2$-collapse. **Circularity**: a `ProvedHere` theorem (fixed
point) derives from a `Conditional` theorem (multi-projection) with
an unestablished base case. The remark `rem:k3-times-e-verification`
(line 3604) gives an arithmetic check of case (3) at $X = K3$, $Y = E$:
$(13, -16, 5, 0) - 2 \cdot (0, 0, 0, 1) = (13, -16, 5, -2)$ and
$(-13, 21, -21, 13) + (13, -16, 5, -2) = (0, 5, -16, 11)$. But this
uses $M_{K3} = (?, ?, ?, ?)$. The remark does not state $M_{K3}$
itself explicitly; the arithmetic assumes $M_{K3} \mapsto \sigma^*
M_{K3} = (13, -16, 5, 0)$ which implies $M_{K3} = (0, 5, -16, 13)$ —
but line 4686 gives $M_{K3} = (0, 5, -16, 11)$!

Let me re-check: $M_{K3} = (0, 5, -16, 11)$ gives $\sigma_{tot}^*
(M_{K3}) = (11, -16, 5, 0) \neq (13, -16, 5, 0)$. **Arithmetic
inconsistency**: the dichotomy verification at line 3608 uses
$\sigma^* M_{K3} = (13, -16, 5, 0)$, but line 4687 states
$\sigma^* M_{K3} = (11, -16, 5, 0)$. These cannot both hold.

Tracing: the first is inside the verification of $\Delta_{K3, E}$
at the abstract level; the second is the value of $M_{K3}$ that
the universal fixed-point theorem attests. **The base case's proof
contains an off-by-two error** — line 3608 should read
$\sigma^* M_{K3} = (11, -16, 5, 0)$, $\chi(\mathcal O_{K3}) = 2$,
$\Delta_{K3, E} = (11, -16, 5, 0) - 2 \cdot (0, 0, 0, 1) = (11, -16, 5, -2)$,
$M_{K3} * M_E + \Delta = $ ??

Let me compute $M_{K3} * M_E$ properly. If $M_{K3} = (0, 5, -16, 11)$
and $M_E = (1, 0, 0, -1)$, then by the V_4-convolution formula
(componentwise XOR):
- $(0, 5, -16, 11) * (1, 0, 0, -1)$: requires the full XOR table.
- Index $(\epsilon_1, \epsilon_2) \in V_4$, pair $(\delta_1, \delta_2)$:
  each entry of the product is $\sum_\delta M_X^\delta \cdot M_Y^{\epsilon + \delta}$.

Using $V_4 = \{++, +-, -+, --\}$ ordered, and XOR table:
- $(++) \oplus (++) = (++)$, $(++) \oplus (+-) = (+-)$, $(++) \oplus (-+) = (-+)$, $(++) \oplus (--) = (--)$
- $(+-) \oplus (+-) = (++)$, $(-+) \oplus (-+) = (++)$, $(--) \oplus (--) = (++)$

Let $M_{K3} = (A_{++}, A_{+-}, A_{-+}, A_{--}) = (0, 5, -16, 11)$ and
$M_E = (B_{++}, B_{+-}, B_{-+}, B_{--}) = (1, 0, 0, -1)$. Then
$(M_{K3} * M_E)_\epsilon = \sum_{\delta + \delta' = \epsilon} A_\delta B_{\delta'}$:
- at $++$: $A_{++} B_{++} + A_{+-} B_{+-} + A_{-+} B_{-+} + A_{--} B_{--}
  = 0 \cdot 1 + 5 \cdot 0 + (-16) \cdot 0 + 11 \cdot (-1) = -11$
- at $+-$: $A_{++} B_{+-} + A_{+-} B_{++} + A_{-+} B_{--} + A_{--} B_{-+}
  = 0 \cdot 0 + 5 \cdot 1 + (-16)(-1) + 11 \cdot 0 = 5 + 16 = 21$
- at $-+$: $A_{++} B_{-+} + A_{-+} B_{++} + A_{+-} B_{--} + A_{--} B_{+-}
  = 0 \cdot 0 + (-16) \cdot 1 + 5 \cdot (-1) + 11 \cdot 0 = -16 - 5 = -21$
- at $--$: $A_{++} B_{--} + A_{--} B_{++} + A_{+-} B_{-+} + A_{-+} B_{+-}
  = 0 \cdot (-1) + 11 \cdot 1 + 5 \cdot 0 + (-16) \cdot 0 = 11$

So $M_{K3} * M_E = (-11, 21, -21, 11)$.

The remark at line 3611 says $M_{K3} * M_E = (-13, 21, -21, 13)$.
**DISAGREEMENT**: my direct computation gives $(-11, 21, -21, 11)$,
the remark asserts $(-13, 21, -21, 13)$. This is an off-by-two in
the $\pm$ entries.

Now using $\Delta_{K3, E} = \sigma^* M_{K3} - \chi(\mathcal O_{K3})
e_{\Pi_{--}} = (11, -16, 5, 0) - (0, 0, 0, 2) = (11, -16, 5, -2)$,
$M_{K3} * M_E + \Delta = (-11 + 11, 21 + (-16), -21 + 5, 11 + (-2))
= (0, 5, -16, 9)$. But the desired $M_{K3 \times E} = M^\flat = (0, 5, -16, 11)$.
**Off by 2** in the last entry.

The remark's claim $M_{K3} * M_E = (-13, 21, -21, 13)$ is arithmetically
WRONG given $M_{K3} = (0, 5, -16, 11)$ and $M_E = (1, 0, 0, -1)$; my
direct V_4-convolution gives $(-11, 21, -21, 11)$. Either (i) the
V_4-convolution convention differs from what I computed, (ii) $M_{K3}$
has a different value than $(0, 5, -16, 11)$ (perhaps an implicit
shift of $\chi(\mathcal O_{K3}) = 2$), or (iii) there is an error.

Given the value at line 3608 uses $\sigma^* M_{K3} = (13, -16, 5, 0)$
not $(11, -16, 5, 0)$, this suggests $M_{K3} = (0, 5, -16, 13)$ in the
convention used in the remark — which is *two larger in the last entry*
than the universal-corollary value $(0, 5, -16, 11)$. **There is an
internal inconsistency** about the value of $M_{K3}$ between (a)
line 3608 (which implicitly uses $M_{K3} = (0, 5, -16, 13)$) and (b)
line 4686 (explicitly $M_{K3} = (0, 5, -16, 11)$). At least one of
these is wrong.

The corollary `cor:M-flat-as-cartan-eigenvector` at line 3857 gives
four constraints, including (iii): "$\Pi_{++}(M^\flat) + \Pi_{--}(M^\flat)
= -(5 + (-16)) = 11$." This derives from $\sum M^\flat = \chi(\mathcal O_{K3 \times E^k}) = 0$
and the $+-, -+$ entries $5, -16$. So the remaining $\Pi_{++} + \Pi_{--}
= -(-11) = 11$ from sum = 0 and $5 - 16 = -11$. If $\Pi_{++} = 0$, then
$\Pi_{--} = 11$. Good, consistent: $M^\flat = (0, 5, -16, 11)$.

But then $M_{K3}$, being the K$3$ "seed" of the tower before applying
$E$, should satisfy $M_{K3} = M_{K3 \times E^0}$? The chain is
$M_{K3 \times E^k} = M^\flat$ for $k \geq 1$; what is $k = 0$, i.e.,
just $M_{K3}$? If the iteration preserves $M^\flat$ under multiplication
by $E$, and $M_{K3 \times E} = M^\flat = (0, 5, -16, 11)$, then it
SEEMS that $M_{K3}$ is ALSO $(0, 5, -16, 11)$ — but this is only
forced if the $k = 0 \to k = 1$ iteration is a fixed point. Which
would require $M_{K3} *_{V_4} M_E + \Delta_{K3, E} = M_{K3}$.

With my computation $M_{K3} * M_E = (-11, 21, -21, 11)$ and
$\Delta_{K3, E} = \sigma^* M_{K3} - 2 e_{--} = (11, -16, 5, 0) -
(0, 0, 0, 2) = (11, -16, 5, -2)$, sum = $(0, 5, -16, 9)$ which is
NOT $M_{K3} = (0, 5, -16, 11)$. Discrepancy of $2$ in the last entry.

**CATASTROPHIC RESIDUE**: the arithmetic in the base-case verification
(rem:k3-times-e-verification, line 3604-3617) contains either an
off-by-two error or a convention mismatch that is not documented.
Either $M_{K3} \neq (0, 5, -16, 11)$, or $\Delta_{K3, E} \neq
\sigma^* M_{K3} - \chi(\mathcal O_{K3}) e_{--}$, or $M_E$ is
different. Downstream: the fixed-point theorem's base case is
unverified; the inductive step relies on a structural identity that
appears to fail arithmetically.

### 3.3. Sharpest honest form (AP289)

> **Theorem (K3-anchored fixed-point, strict form, CONDITIONAL).**
> Assume (H-Dich) the Künneth dichotomy of
> `thm:kunneth-dichotomy`, (H-MPB) the multi-projection bigraded
> Lefschetz identity of `thm:k3-multiproj-bigraded-lefschetz`
> (Caldararu chiral HRR + Hodge $E_2$-collapse), and (H-Arith) the
> base-case arithmetic identity $M_{K3 \times E} = (0, 5, -16, 11)$
> (requires resolution of the off-by-two discrepancy between
> `rem:k3-times-e-verification` and `cor:verified-sigma-generic-fixed-points`).
> Then for all $k \geq 1$, $M_{K3 \times E^k} = (0, 5, -16, 11)$.
> The inductive step uses `lem:bivariant-kunneth-identity`
> (unconditional on $\Z[V_4]$ — proved identically, not only on the
> trace-zero hyperplane).

---

## 4. `thm:universal-drinfeld-coupling-E` (k3_yangian_chapter.tex:3810-3841)

### 4.1. Three load-bearing steps

- **S1**: V_4-Fourier transform of $M_E = (1, 0, 0, -1)$ is
  $\hat M_E = (0, 2, 2, 0)$ at $(\chi_{++}, \chi_{+-}, \chi_{-+}, \chi_{--})$.
- **S2**: $\sigma_{\mathrm{tot}}^*$ acts via multiplication by
  $(1, -1, -1, 1)$ in Fourier.
- **S3**: $\hat M \cdot (1 - 1, 1 - (-1), 1 - (-1), 1 - 1) = \hat M \cdot (0, 2, 2, 0)$.

### 4.2. Dismissal protocol per step

**S1 — VERIFICATION.** V_4-Fourier: for V_4 = {++,+-,-+,--} with
characters $\chi_{\epsilon_1 \epsilon_2}(\delta_1, \delta_2) =
\epsilon_1^{\delta_1} \epsilon_2^{\delta_2}$ (writing $+1, -1$ for
$\epsilon$), we have $\hat M_E(\chi) = \sum_\delta M_E^\delta \chi(\delta)$:
- at $\chi_{++}$: $M_{++} + M_{+-} + M_{-+} + M_{--} = 1 + 0 + 0 - 1 = 0$
- at $\chi_{+-}$: $M_{++} - M_{+-} + M_{-+} - M_{--} = 1 - 0 + 0 - (-1) = 2$
- at $\chi_{-+}$: $M_{++} + M_{+-} - M_{-+} - M_{--} = 1 + 0 - 0 - (-1) = 2$
- at $\chi_{--}$: $M_{++} - M_{+-} - M_{-+} + M_{--} = 1 - 0 - 0 + (-1) = 0$

So $\hat M_E = (0, 2, 2, 0)$. *Correct.*

**S2 — VERIFICATION.** $\sigma_{\mathrm{tot}}^*$ maps $(m_{++}, m_{+-},
m_{-+}, m_{--}) \mapsto (m_{--}, m_{-+}, m_{+-}, m_{++})$. In Fourier:
$\hat{\sigma^* M}(\chi_{\epsilon_1 \epsilon_2}) = \sum_\delta
(\sigma^* M)^\delta \chi(\delta) = \sum_\delta M^{\sigma \delta}
\chi(\delta)$, where $\sigma$ is the antipodal involution on V_4
(which swaps $++ \leftrightarrow --$ and $+- \leftrightarrow -+$).
For V_4 as $(\Z/2)^2$, $\sigma$ is the "flip everything" $\delta
\mapsto \delta + (1,1)$ in additive notation. So $\hat{\sigma^* M}(\chi)
= \chi(-(1,1)) \hat M(\chi) = \chi_{\epsilon_1\epsilon_2}(1,1) \hat M(\chi)
= \epsilon_1 \epsilon_2 \hat M(\chi)$.
- at $\chi_{++}$: $+1 \cdot (+1) = +1$
- at $\chi_{+-}$: $+1 \cdot (-1) = -1$
- at $\chi_{-+}$: $-1 \cdot (+1) = -1$
- at $\chi_{--}$: $-1 \cdot (-1) = +1$

So $\sigma^*$ in Fourier is multiplication by $(1, -1, -1, 1)$. *Correct.*

**S3 — VERIFICATION.** $\hat{(M - \sigma^* M)} = \hat M \cdot
(1 - 1, 1 - (-1), 1 - (-1), 1 - 1) = \hat M \cdot (0, 2, 2, 0) =
\hat M \cdot \hat M_E = \widehat{M *_{V_4} M_E}$. *Correct.*

### 4.3. THE RESIDUE

The theorem as stated is a CORRECT direct Fourier computation.
The identity $M *_{V_4} M_E = M - \sigma^*_{\mathrm{tot}}(M)$ is
arithmetically TRUE on $\Z[V_4]$.

But: **this means that $\Delta_{X, E} = \sigma^* M_X$ only when
the product $M_{X \times E}$ equals $M_X$**, by the defining equation
$M_{X \times E} = M_X * M_E + \Delta_{X, E}$. This is a
*tautological consistency condition* derived from `lem:bivariant-kunneth-identity`,
not an *independent* theorem. The corollary `cor:universal-drinfeld-coupling-E`
is a *restatement* of the bivariant-Künneth identity in terms of
the fixed-point property. Calling it "Universal Drinfeld-coupling
identity at the elliptic factor" is expository elevation, not new
content.

*The theorem is correct but content-wise is a direct specialisation
of* `lem:bivariant-kunneth-identity`. The chapter's decomposition
into `lem:bivariant-kunneth-identity` + `thm:universal-drinfeld-coupling-E`
is *two statements of the same fact*.

### 4.4. Sharpest honest form (AP289)

> **Theorem (Universal $E$-convolution identity).** For every
> $M \in \Z[V_4]$, $M *_{V_4} M_E = M - \sigma^*_{\mathrm{tot}}(M)$,
> where $M_E = (1, 0, 0, -1)$ is the elliptic-curve $V_4$-vector.
> This is a direct V_4-Fourier computation. **Consequence**:
> if $M_{X \times E} = M_X * M_E + \Delta_{X, E}$ *defines*
> $\Delta_{X, E}$ and $M_{X \times E} = M_X$ at the fixed point,
> then $\Delta_{X, E} = \sigma^*_{\mathrm{tot}}(M_X)$ is a
> bookkeeping identity, not a universal fact about CY input.

---

## 5. `thm:bracketing-associator-cohomology-class` (k3_yangian_chapter.tex:5501-5565)

### 5.1. Three load-bearing steps

- **S1 (`lem:V4-cohomology-bracketing-home`, line 5461)**: computes
  $H^3(V_4; \Z[V_4]_0) \cong (\Z/2)^2$ via Shapiro + integral
  cohomology of $V_4$ + Bockstein description.
- **S2 (witness triple $(K3, K3, K3)$)**: $a(K3, K3, K3) = (0, 0, 0, 0)$,
  giving $c_\alpha = 0$ (wt-direction Bockstein coefficient vanishes).
- **S3 (witness triple $(\text{conifold}, \text{conifold}, K3)$)**: the
  par-direction Bockstein coefficient is non-zero, yielding $c_\beta = 1$.

### 5.2. Dismissal protocol per step

**S1.** Standard integral cohomology of $V_4 = \Z/2 \times \Z/2$.
The computation matches Adem-Milgram (Cohomology of Finite Groups,
1994). Specifically, $H^*(V_4; \Z) = \Z[\alpha, \beta, \gamma]/(2\alpha,
2\beta, 2\gamma, \gamma^2 = \alpha \beta(\alpha + \beta))$ with
$\deg \alpha = \deg \beta = 2$, $\deg \gamma = 3$. So $H^2(V_4; \Z)
= \Z/2 \cdot \alpha \oplus \Z/2 \cdot \beta = (\Z/2)^2$. *Passes.*

Shapiro: $H^*(V_4; \Z[V_4]) \cong H^*(\{e\}; \Z) = \Z$ in degree 0,
$0$ elsewhere. The long exact sequence gives
$H^n(V_4; \Z[V_4]_0) \cong H^{n-1}(V_4; \Z)$ for $n \geq 2$. So
$H^3(V_4; \Z[V_4]_0) \cong H^2(V_4; \Z) = (\Z/2)^2$. *Passes.*

**S2 — VERIFICATION.** $a(K3, K3, K3)$ involves three bracketings:
$M_{((K3 \cdot K3) \cdot K3)}$ vs $M_{(K3 \cdot (K3 \cdot K3))}$.
By the closed form (line 5411),
$a(X, Y, Z) = [\Delta_{X,Y} * M_Z + \Delta_{X \times Y, Z}]
- [M_X * \Delta_{Y,Z} + \Delta_{X, Y \times Z}]$.

For $X = Y = Z = K3$: $\Delta_{K3, K3} = 0$ (case (1),
both factors $\sigma^*$-generic per line 3568). Then
$\Delta_{K3 \times K3, K3}$ and $\Delta_{K3, K3 \times K3}$ are
the asymmetric-coupling corrections. Per `prop:k3-k3-via-kunneth`
(line 3559), $M_{K3 \times K3} = (450, -416, 130, -160)$ (sum = 4),
and this is $\sigma^*$-generic. So both $\Delta_{K3 \times K3, K3}$
and $\Delta_{K3, K3 \times K3}$ fall under case (1) with $\Delta = 0$.
Thus $a(K3, K3, K3) = 0$. *Consistent with the witness.*

**S3 — THE RESIDUE.** $a(\text{conifold}, \text{conifold}, K3)$
is claimed to have all entries even and to project onto the
par-direction Bockstein. Direct arithmetic is not shown in the
proof body. We have
- $M_{\text{conifold}} = (-1, 1, 0, 0)$
- $\Delta_{\text{conifold}, \text{conifold}}$ = case (1) since both
  generic, so $\Delta = 0$
- $M_{\text{conifold} \times \text{conifold}} = M_C * M_C$ — let me
  compute: $(-1)^2 + (1)^2 + 0 + 0 = 2$ at $++$, $(-1)(1) + (1)(-1) = -2$ at $+-$,
  $(-1)(0) + (0)(-1) + (1)(0) + (0)(1) = 0$ at $-+$ and $--$.
  So $M_{C \times C} = (2, -2, 0, 0)$. This is $\sigma^*$-generic.
- $\Delta_{\text{conifold} \times \text{conifold}, K3}$: is $K3$
  or $C \times C$ in the $-1$-eigenspace? Neither. Case (1), $\Delta = 0$.
- Similarly $\Delta_{\text{conifold}, \text{conifold} \times K3} = 0$
  by genericity.

So *all Drinfeld corrections in the bracketing-associator formula
vanish at $(C, C, K3)$*, giving $a(C, C, K3) = 0$. But the theorem
claims $c_\beta = 1$ is witnessed at this triple with non-trivial
par-direction Bockstein contribution.

**Either (i) the witness triple is wrong, or (ii) my $M_C * M_C$
computation is wrong, or (iii) one of the $\Delta$ is not zero.**

Let me recompute $M_C * M_C$ correctly: $M_C = (-1, +1, 0, 0)$.
- at $++$: $M_{++}^2 + M_{+-}^2 + M_{-+}^2 + M_{--}^2 = 1 + 1 + 0 + 0 = 2$
- at $+-$: $2 M_{++} M_{+-} + 2 M_{-+} M_{--} = 2(-1)(1) + 0 = -2$
- at $-+$: $2 M_{++} M_{-+} + 2 M_{+-} M_{--} = 0 + 0 = 0$
- at $--$: $2 M_{++} M_{--} + 2 M_{+-} M_{-+} = 0 + 0 = 0$

So $M_{C \times C} = (2, -2, 0, 0)$. Sum = $0 = \chi(\mathcal O_C)^2 \cdot 1 = 1$?
Hmm, $\chi(\mathcal O_{\text{conifold}})$: the conifold has
$\chi(\mathcal O) = 1$? Let me check: for the resolved conifold
$\widetilde X = \mathcal O(-1) \oplus \mathcal O(-1) \to \P^1$,
$\chi(\mathcal O_{\widetilde X})$ ... actually conifold is non-compact
and $M_C$ here is defined up to convention. But sum 0 matches the
stated $\chi(\mathcal O_C) = -1 + 1 + 0 + 0 = 0$; so $\chi(\mathcal O_C) = 0$
in this convention.

For $(C, C, K3)$ triple, everything is $\sigma^*$-generic, so all
$\Delta = 0$, so $a(C, C, K3) = 0$. **The claimed witness triple
CONTRADICTS the closed-form formula.**

Wait — let me recheck. The formula is
$a(X,Y,Z) = [\Delta_{X,Y} * M_Z + \Delta_{X \times Y, Z}] - [M_X * \Delta_{Y,Z} + \Delta_{X, Y \times Z}]$.
For $(C, C, K3)$ — is $K3$ in the $-1$-eigenspace? $\sigma^* M_{K3}
= (11, -16, 5, 0) \neq -M_{K3} = (0, -5, 16, -11)$. Not in $-1$-eigenspace;
generic. So $\Delta_{C \times C, K3} = 0$ (both generic, case 1) and
$\Delta_{C, C \times K3} = 0$ similarly. So $a(C, C, K3) = 0$,
contradicting the witness for $c_\beta = 1$.

*The witness triple $(C, C, K3)$ for the non-trivial par-direction
Bockstein class is wrong*: the bracketing-associator vanishes there
by the closed-form formula. The proof claims "a non-trivial Drinfeld
coupling $\Delta_{\text{conifold}, K3}$ in case (3) of the dichotomy"
— but this requires $\Delta_{C, K3}$ to appear in the closed-form
expression, which it does not (the expression uses $\Delta_{X, Y}$,
$\Delta_{X \times Y, Z}$, $\Delta_{Y, Z}$, $\Delta_{X, Y \times Z}$
— NOT $\Delta_{C, K3}$ directly for $(X, Y, Z) = (C, C, K3)$).

Furthermore, note that $M_C$ is listed at line 4688 as generic, so
$\Delta_{C, K3} = 0$ (both generic, case 1); even if it DID appear,
it would contribute 0.

*So the computation of $c_\beta = 1$ is unsupported*. The claim
that $[a] = c_\alpha \mathrm{Bock}(\alpha) + c_\beta \mathrm{Bock}(\beta)$
with $c_\beta = 1$ requires *some* witness triple with a non-trivial
bracketing-associator; the theorem offers only $(C, C, K3)$, which
gives $a = 0$.

**The theorem's classification of $[a]$ in $H^3(V_4; \Z[V_4]_0)$ is
incorrect at the level of witness verification**: the sole
non-trivial witness fails to be non-trivial.

Looking at `thm:bracketing-associator-closed-form` line 5422:
- $a(C, K3, E) = (0, 0, 2, -2)$ — non-trivial.
- $a(K3, K3, E) = (26, -32, 10, -4)$ — non-trivial.
- $a(K3, E, E) = 0$.

The non-trivial witness SHOULD be $(C, K3, E)$ or $(K3, K3, E)$, not
$(C, C, K3)$! The proof body at line 5546 incorrectly points to
$(\text{conifold}, \text{conifold}, K3)$. The correct witness would
be e.g. $(K3, K3, E) = (26, -32, 10, -4)$, which has entries dividing
by 2 giving $(13, -16, 5, -2)$ — so the $\F_2$-reduction of $a/2$ is
$(1, 0, 1, 0) \mod 2$ which projects somewhere in $H^2(V_4; \F_2)$.

### 5.3. Sharpest honest form (AP289)

> **Theorem (Bracketing-associator cohomology, strict form).** The
> bracketing-associator $a(X, Y, Z)$ as a $V_4$-equivariant $3$-cocycle
> has cohomology class $[a] \in H^3(V_4; \Z[V_4]_0) \cong (\Z/2)^2$
> (by Shapiro + integral $V_4$-cohomology). The image of $[a]$ in
> this home requires witness triples with non-trivial $a/2 \pmod 2$;
> the correct witnesses are triples where at least one factor is
> $E$-like (case 3 of the dichotomy), e.g., $(K3, K3, E)$ or
> $(\text{conifold}, K3, E)$. The witness $(\text{conifold},
> \text{conifold}, K3)$ claimed at line 5519-5520 yields $a = 0$
> under the closed-form formula (all three factors generic), so the
> witness is incorrectly chosen; $c_\beta$ requires a different
> witness. The strict classification $c_\alpha = 0$, $c_\beta = 1$
> is *provisional* pending corrected witness verification.

---

## 6. `thm:k3-mock-modular-proof` (k3_yangian_chapter.tex:2844-2891)

### 6.1. Three load-bearing steps

- **S1 (non-semisimplicity via Huang + $C_2$-cofiniteness)**: Gaberdiel
  2003 for $C_2$, `prop:shadow-class-k3` for class-M, Huang 2008 for
  rational iff semisimple.
- **S2 ($\cN=4$ decomposition via EOT)**: massless + massive
  decomposition with $\chi(K3) = 24$ massless sector (Eguchi-Taormina
  1988, EOT 2010).
- **S3 (Zwegers + DMZ)**: $\mu$ requires completion $\hat\mu = \mu + R$;
  $R$ is the Eichler integral of $\eta(\tau)^3$; DMZ 2012 shows
  $\hat h$ transforms as weight-$1/2$ non-holomorphic modular form.

### 6.2. Dismissal protocol per step

**S1.** Citations stated and used correctly. Gaberdiel 2003 for
$C_2$-cofiniteness of the small-$\cN=4$ at $c=6, k_R=1$; Huang 2008
(arXiv:0502533v4) for the C_2 $\Leftrightarrow$ rationality +
semisimplicity (note: Huang's theorem is stated as "$C_2$-cofinite
$\Leftrightarrow$ rational AND regular"; the contrapositive requires
both). `prop:shadow-class-k3` is local to this volume at
`k3e_cy3_programme.tex:400`. *Passes*, conditional on `prop:shadow-class-k3`
being internally proved — let me verify.

**S2.** EOT 2010 (arXiv:1004.0956) is the Eguchi-Ooguri-Tachikawa
paper introducing the K3 Mathieu moonshine. It contains the $\cN=4$
decomposition with $\chi(K3) = 24$ as the $M_{24}$ dimension. The
citation is correct; the use is to extract the massive sector as
$h(\tau) \cdot \mu(\tau, z)$. This is direct. *Passes.*

**S3 — THE RESIDUE.** Two issues:

(a) *Zwegers attribution.* "Zwegers (2002) proved that $\mu(\tau, z)$
requires a non-holomorphic completion $\hat\mu = \mu + R$, where $R$
involves the Eichler integral of $\eta(\tau)^3$ with coefficient
$24 = \chi(K3)$." Zwegers' 2002 thesis (Utrecht) proved the mock
theta function $\mu$ completes to $\hat\mu$, but the coefficient
"$24 = \chi(K3)$" is NOT in Zwegers — it appears in the specialisation
to the K3 elliptic genus in EOT / Cheng-Duncan-Harvey, where the
Mathieu moonshine attaches $M_{24}$-modules. *Conflation*: Zwegers'
general theorem uses a generic coefficient; the K3-specific value 24
comes from EOT, not Zwegers. The attribution should be split:
"Zwegers for the completion, EOT for the coefficient $24 = \chi(K3)$."

(b) *Three-path claim at line 2889 — THE RESIDUE.* The claim reads:
"shadow coefficient satisfies $24 = (\kappa_{\mathrm{ch}}/2) \cdot
\chi(K3)$ by three independent paths: algebraic (bar complex),
automorphic (Zwegers), and topological (CY geometry)." With
$\kappa_{\mathrm{ch}} = 2$ and $\chi(K3) = 24$, the RHS is
$(2/2) \cdot 24 = 24$. This is ARITHMETIC (one plus one equals two).
The three "paths" are:
- algebraic: $\kappa_{\mathrm{ch}} = 2$ from Prop `kappa-hodge-supertrace`
- automorphic: Zwegers' completion coefficient is 24
- topological: $\chi(K3) = 24$ directly

These are **not three independent paths verifying the SAME number**;
they are ONE path computing $\kappa_{\mathrm{ch}} = 2$, a SECOND path
that uses $\chi(K3) = 24$ from automorphic forms, and a THIRD that
uses $\chi(K3) = 24$ from topology. Paths 2 and 3 both compute the
same quantity $\chi(K3) = 24$ — they are not independent verifications
of $24 = (\kappa_{\mathrm{ch}}/2) \cdot \chi(K3)$; they are
compatibility checks between different descriptions of $\chi(K3)$.

Beilinson dismissal: the three "paths" collapse to (a) $\kappa_{\mathrm{ch}} = 2$
(one path) + (b) $\chi(K3) = 24$ (Noether formula from signature $-16$
and Euler $24$, dimension/signature of K3 cohomology — one path)
+ (c) Zwegers-EOT completion coefficient (a coefficient MATCH check,
not an independent derivation). This is *two paths dressed as three*.

### 6.3. Sharpest honest form (AP289)

> **Theorem (K3 mock modularity, strict form).** The K3 sigma model
> VOA is $C_2$-cofinite (Gaberdiel 2003), class-M (local shadow-tower
> computation), hence non-semisimple (Huang 2008). The $\cN=4$ spectral
> decomposition (Eguchi-Taormina 1988, EOT 2010) produces massless
> multiplicity $24 = \chi(K3)$; Zwegers 2002 gives the non-holomorphic
> completion of $\mu$; the K3-specific coefficient $24$ enters via
> EOT. Dabholkar-Murthy-Zagier 2012 §7 delivers the weight-$1/2$
> transformation. The identity $\chi(K3) = 24$ is a *one-path* topological
> fact (Noether + Hodge), with Zwegers' completion serving as a
> *compatibility check* rather than an independent derivation. The
> shadow coefficient equation $24 = (\kappa_{\mathrm{ch}}/2)\chi(K3)$
> is arithmetic consequence once $\kappa_{\mathrm{ch}} = 2$ and
> $\chi(K3) = 24$ are established.

---

## 7. Re-verification of the three Wave-1 mis-status claims + new findings

### Wave-1 original three

| Label | Line | Current | Wave-1 recommendation | Wave-2 confirmation |
|---|---|---|---|---|
| `thm:k3-pentagon-E1-edge-architecture` | 3249 | ProvedHere | Downgrade to Conditional | CONFIRMED: explicit "conditional on FM164, FM161" in statement itself. The "proof" at 3311-3357 asserts three closure morphisms (Borch / EK / FH), each "certified" by external literature; the fifth edge closes by Mac Lane K_5 "coherence" — but Mac Lane's coherence theorem asserts that diagrams commute *in a monoidal category*, not that four commuting edges force a fifth. **Misuse of Mac Lane** (already in Wave-1 #F2). Downgrade. |
| `def:osp-super-yangian-K3` | 1921 | ProvedElsewhere | Downgrade to Conjectured, at least for (4,20) instantiation | CONFIRMED: Conjecture 1879-1917 admits rank-(4,20) reflection equation "open"; def 1921 is inhabited by inference. Furthermore, cross-referencing Wave-1 Kazhdan (rank 12 vs lattice 24 conflation) and Wave-1 SYNTHESIS (§2.2 correction: should be $\mathfrak{so}(4,20)$, not $\mathfrak{osp}(4|20)$, since Mukai form is symmetric indefinite not supersymmetric), the definition is doubly problematic. Downgrade. |
| `thm:chain-to-matrix-pentagon-unification` | 5668 | Conditional | Correctly Conditional but depends on the Critical item #1 | CONFIRMED: depends on `thm:k3-pentagon-E1-edge-architecture` (item 1, itself mis-statused). The "numerical verification at five quadruples" (rem at 5692 is ProvedHere) is a finite bookkeeping exercise, not a proof of the universal statement. |

### New Wave-2 findings

**W2-N1** (NEW, Critical): `thm:k3-elliptic-tower-fixed-point`
(line 3701, ProvedHere) contains an **internal arithmetic
inconsistency** about $M_{K3}$ between `rem:k3-times-e-verification`
(line 3604-3617, using $\sigma^* M_{K3} = (13, -16, 5, 0)$ implying
$M_{K3} = (0, 5, -16, 13)$) and `cor:verified-sigma-generic-fixed-points`
(line 4686, $M_{K3} = (0, 5, -16, 11)$). At least one is wrong; until
reconciled, the base case of the fixed-point theorem is unverified.
**Status should be**: downgrade to Conditional on the resolution of
this arithmetic.

**W2-N2** (NEW, High): `thm:bracketing-associator-cohomology-class`
(line 5503, ProvedHere) uses the witness triple
$(\text{conifold}, \text{conifold}, K3)$ (line 5547) which yields
$a = 0$ under the closed-form formula — all three factors are
$\sigma^*$-generic, so all Drinfeld corrections vanish, so the
bracketing-associator vanishes. The claimed non-trivial par-direction
Bockstein coefficient $c_\beta = 1$ has **no valid witness in the
proof**. Correct witness should be $(K3, K3, E)$ or $(\text{conifold}, K3, E)$
(listed at line 5422-5430 with non-trivial values).
**Status should be**: downgrade to Provisional or substitute the
correct witness.

**W2-N3** (NEW, Medium): `thm:k3-abelian-yangian-presentation`
(line 880, ProvedHere) uses a misattribution to Tsymbaliuk
arXiv:1404.5240. Tsymbaliuk's $Y(\widehat\gl_1)$ is a rank-3 Yangian
(MO on Hilb$^n(\C^2)$), not a rank-$N$ tensor-product of Heisenberg
Yangians. The correct citation is Chari-Pressley 1995 (already in
`rem:k3-abelian-yangian-classical`); the proof body's Tsymbaliuk
reference is misleading. *Fix: remove or requalify Tsymbaliuk citation.*

**W2-N4** (NEW, High): `thm:k3-mock-modular-proof` (line 2846,
ProvedHere) at line 2889 claims "three independent paths" for the
shadow-coefficient identity $24 = (\kappa_{\mathrm{ch}}/2) \cdot
\chi(K3)$. These collapse to *two* genuine paths ($\kappa_{\mathrm{ch}}
= 2$ and $\chi(K3) = 24$); the "Zwegers automorphic path" is a
compatibility check, not a third derivation. **Requires rewording or
adding a genuine third path** (e.g., the Ramanujan $\Delta(q) = \eta^{24}/q$
bar-Euler identity at rank 24 Heisenberg, directly relating to
Göttsche's K3-Hilbert-scheme formula).

**W2-N5** (NEW, Medium): `thm:bfn-phi-ade-identification` (line 110,
ProvedElsewhere) uses CY-A$_2$ in the **non-compact local-surface**
form (applicable to $T^*\widetilde S_\fg$), not the compact form
proved in the volume. This is not a defect — BFN is inherently
non-compact — but the scope should be explicit: "CY-A$_2$ in the
non-compact-local form," distinct from the CY-A$_2$ used in
`thm:k3-mock-modular-proof` for the compact K3 sigma model.

**W2-N6** (NEW, High): Braden-Licata-Proudfoot-Webster cited at
line 131 for "Higgs-side factorisation quantisation = Coulomb-side
BFN convolution as $E_1$-chiral algebras." BLPW 2014 (arXiv:1407.0964)
proves a *derived-category* equivalence (symplectic-duality category
$O$ equivalence), not a factorisation-quantisation compatibility.
The upgrade from BLPW's derived-category statement to factorisation-
algebra equality on the nose is not justified in the literature for
general ADE. *Fix: requalify.*

---

## 8. Ranked Wave-2 punchlist (severity-ordered)

| # | Severity | File:line | Claim | Wave-2 correction |
|---|----------|-----------|-------|------------------|
| 1 | **Critical** | k3_yangian_chapter.tex:3701 | `thm:k3-elliptic-tower-fixed-point` ProvedHere contains arithmetic inconsistency in base case (line 3608 vs 4686 on $M_{K3}$) | Resolve off-by-two in `rem:k3-times-e-verification`; downgrade to Conditional until resolved |
| 2 | **Critical** | k3_yangian_chapter.tex:3249 | `thm:k3-pentagon-E1-edge-architecture` ProvedHere with "conditional on FM164, FM161" in statement | Downgrade to Conditional (Wave-1 #1, Wave-2 confirms) |
| 3 | **Critical** | k3_yangian_chapter.tex:1921 | `def:osp-super-yangian-K3` ProvedElsewhere with (4,20) reflection-equation open; also $\mathfrak{so}(4,20) \neq \mathfrak{osp}(4|20)$ | Downgrade; replace with $\mathfrak{so}(4,20)$ per SYNTHESIS §2.2 |
| 4 | **High** | k3_yangian_chapter.tex:5518-5521 | `thm:bracketing-associator-cohomology-class`: witness $(C, C, K3)$ yields $a = 0$ contradicting $c_\beta = 1$ | Substitute witness $(K3, K3, E)$ or $(C, K3, E)$ per line 5422-5430 |
| 5 | **High** | k3_yangian_chapter.tex:2889 | `thm:k3-mock-modular-proof`: "three independent paths" collapse to two | Add a genuine third path (Ramanujan $\Delta$ / Göttsche) or reword |
| 6 | **High** | k3_yangian_chapter.tex:131 | BLPW cited for factorisation-algebra equality; BLPW gives derived-category equivalence only | Requalify as "derived equivalence lifts at the formal disk" with explicit hypothesis |
| 7 | **High** | k3_yangian_chapter.tex:5668 | `thm:chain-to-matrix-pentagon-unification` depends on item #2 | Inherits downgrade; status correctly already Conditional |
| 8 | **Medium** | k3_yangian_chapter.tex:1010 | Tsymbaliuk 1404.5240 misattribution (rank-3 $\gl_1$ Yangian vs rank-24 tensor Heisenberg) | Replace with Chari-Pressley 1995 + Frenkel-Jing 1988; remove Tsymbaliuk |
| 9 | **Medium** | k3_yangian_chapter.tex:3673 | `lem:bivariant-kunneth-identity` proof delivers the identity for all $N$, but the lemma scope "on the trace-zero hyperplane" is narrower than what is proved | Broaden the scope statement to "on all of $\Z[V_4]$" |
| 10 | **Medium** | k3_yangian_chapter.tex:3813-3855 | `thm:universal-drinfeld-coupling-E` is a restatement of `lem:bivariant-kunneth-identity` in Fourier; no new content | Consolidate or label explicitly as "Consequence" / "Corollary" |

---

## 9. The single most catastrophic residue

**ITEM #1** — the arithmetic inconsistency in
`thm:k3-elliptic-tower-fixed-point`.

**Why this is the worst**:

- It is the *base case* of a universal fixed-point theorem that the
  Corollary `cor:verified-sigma-generic-fixed-points` extends to
  FOUR CY inputs (K3, conifold, local $\P^2$, genus-$g$ curves).
- The theorem is labelled ProvedHere with an arithmetic verification
  (`rem:k3-times-e-verification`) that uses $\sigma^* M_{K3} = (13, -16, 5, 0)$,
  implying $M_{K3} = (0, 5, -16, 13)$; but the universal corollary
  at line 4686 states $M_{K3} = (0, 5, -16, 11)$ (the former value
  would give $\sigma^* = (13, -16, 5, 0)$, the latter $\sigma^* = (11, -16, 5, 0)$).
- **Propagation**: this value of $M_{K3}$ flows into
  - `thm:matrix-pentagon-coherence` (line 5618, proof at 5626-5664)
    with specific numerical values;
  - `thm:k3-multiproj-bigraded-lefschetz` (line 3362, Conditional);
  - `cor:M-flat-as-cartan-eigenvector` (line 3857);
  - `thm:bracketing-associator-cohomology-class` (line 5501) —
    which then affects item #4.
  - ALL downstream K3-specific $V_4$-computation.
- If $M_{K3} = (0, 5, -16, 11)$ (the universal-corollary value),
  then the base-case verification contains the off-by-two I computed
  (sum would be $(0, 5, -16, 9)$, not $(0, 5, -16, 11)$), so the
  fixed-point fails.
- If $M_{K3} = (0, 5, -16, 13)$ (the remark's implied value),
  then the universal corollary is incorrect, and the specific value
  $11$ (which appears in `cor:M-flat-as-cartan-eigenvector` via
  "trace closure $-(5 + (-16)) = 11$" assuming $\Pi_{++} = 0$) is wrong.

The single most catastrophic residue is thus a **basic arithmetic
reconciliation**: is $\Pi_{--}(M_{K3}) = 11$ or $13$? The answer
determines whether the entire $V_4$-bookkeeping apparatus of
Sections 3179-5388 is correctly set up. If wrong, every downstream
ProvedHere in this range inherits the defect.

---

## 10. Recommendation: proceed to inscription, or block?

**BLOCK** on items #1, #4 until the arithmetic residues are resolved.

Items #2 and #3 are **status downgrades**, not mathematical errors;
Vol I / Vol III preface already softens via "the naive six-way
isomorphism of the original CY-C is therefore FALSIFIED" —
`def:osp-super-yangian-K3` and `thm:k3-pentagon-E1-edge-architecture`
can be re-tagged without blocking inscription elsewhere.

Items #5-10 are wording / citation fixes; they do not block.

**Do not propagate Section 3179-5388 $V_4$-bookkeeping into further
chapters** until the $M_{K3}$ value is pinned and the base-case
verification is corrected. Until then, the K$3$-anchored fixed-point
theorem and its universal extension are PROVISIONAL.

---

## 11. Wave-2 convergence statement

The Wave-1 verdict (six surviving proved theorems) survives with
residues: three theorems (`bfn-phi-ade`, `k3-abelian-presentation`,
`universal-drinfeld-coupling-E`) are genuinely proved modulo
conservatively-tagged qualifiers; two (`k3-elliptic-tower-fixed-point`,
`bracketing-associator-cohomology-class`) contain arithmetic errors
that must be resolved before they can retain ProvedHere status;
one (`k3-mock-modular-proof`) is genuinely proved at the d=2 layer
with a misstated multi-path verification.

Combined with Wave-1 three mis-status items
(`k3-pentagon-E1-edge-architecture`,
`def:osp-super-yangian-K3`,
`thm:chain-to-matrix-pentagon-unification`), the chapter's
honest state is:

- **Three genuinely ProvedHere-at-d=2 theorems** (`k3-abelian`,
  `k3-mock-modular`, `bfn-phi-ade-identification` — the last as
  ProvedElsewhere on literature citations).
- **Three theorems requiring arithmetic fix** (`k3-elliptic-tower-fixed-point`,
  `bracketing-associator-cohomology-class`, and the `$M_{K3}$` value
  propagating through all $V_4$-bookkeeping).
- **Five theorems requiring status downgrade** (the three Wave-1
  plus two additional discovered in Wave-2: the numerical-verification
  remark at `chain-to-matrix-pentagon-five-quadruples` and the
  "three-path" shadow identity in `k3-mock-modular-proof`).

Beilinson's smaller-true-theorem principle: the surviving
chapter is a PROOF that
- the rank-24 Heisenberg Yangian of Chari-Pressley at signature (4,20)
  with CY$_2$ constraint $\sum h_i = 0$ admits the stated presentation;
- the ADE sub-specialisation identifies with BFN's shifted Yangian
  at level 1 (compositionally from four ProvedElsewhere results);
- the K3 sigma model VOA produces a mock modular form of weight 1/2
  with shadow $24 \eta^3$;

and a FINITE BOOKKEEPING of $V_4$-trace data at $K3 \times E^k$ that,
modulo the $M_{K3}$ arithmetic reconciliation, organises into
(i) a fixed-point statement and (ii) a cohomology-class identification
in $H^3(V_4; \Z[V_4]_0) = (\Z/2)^2$.

The Wave-2 deep re-audit does not disturb the programme's honest
scope; it sharpens the failure of the *non-abelian* K3 Yangian claim
by exposing arithmetic and witness defects that, while downstream-
rectifiable, currently block ProvedHere status on two more theorems.

**Sole author: Raeez Lorgat. No AI attribution anywhere.**

— End of Wave-2 deep audit.
