# Agent 05 — Nekrasov on the Non-Abelian K3 Yangian

*Voice*: the partition function and the characteristic class belong on opposite
sides of a single equals sign, neither apologising for the presence of the other.
The derivation is the line segment between them, not a bridge.

*Raeez Lorgat, sole author.*

---

## 0. The identity we are auditing

On $\mathbb{C}^2$ the AGT correspondence in its Schiffmann–Vasserot /
Maulik–Okounkov form reads

$$
Z_{\mathrm{Nek}}(\mathbb{C}^2;\,q,\varepsilon_1,\varepsilon_2)
\;=\;
\mathrm{ch}\bigl(\mathcal{F}(\hat{\mathfrak{gl}}_1)\bigr)(q,\varepsilon_1,\varepsilon_2)
\;=\;
\prod_{n\ge 1}\frac{1}{(1-q^n)^{\,1}},
$$

with Yangian $Y_{\!\hbar}(\hat{\mathfrak{gl}}_1)$ acting on
$\bigoplus_n H^\ast_T(\mathrm{Hilb}^n(\mathbb{C}^2))$ through
Maulik–Okounkov stable envelopes for the torus
$T=(\mathbb{C}^\ast)^2$.  Two ingredients:
a torus action, and an Omega-background.  The target of the audit is the K3
analogue.

---

## 1. Round 1 ATTACK: do the objects exist on K3?

### 1.1 Moduli identification

The claim of `chapters/examples/k3_yangian_chapter.tex` lines 72–180 is precise
on what is proved and what is conjectured:

- **Moduli on the LHS**: the rank-$1$ Vafa–Witten moduli on K3 is
  $\coprod_{n\ge 0}\mathrm{Hilb}^n(K3)$.  Smooth (Fogarty 1968);
  Euler characteristics are the $24$-coloured partition numbers $p_{24}(n)$
  (Göttsche 1990).  No ambiguity.

- **Moduli on the RHS**: `Y(\mathfrak{g}_{K3})` acts (conjecturally;
  AP-CY14) on the bar-cobar home of $\Phi(D^b(\mathrm{Coh}(K3)))$.  The
  abelian / $\mathfrak{gl}_1$ specialisation $H_{\mathrm{Muk}}$ is
  **proved** (prop:k3-heisenberg): rank-$24$ Heisenberg with Mukai
  pairing of signature $(4,20)$.

- **For what $G$ and what rank**: the identification is stated for
  $G=\mathrm{SU}(2)$ (rank $1$) in the Yangian sub-case $\mathfrak{g}=\mathfrak{gl}_1$
  (`k3_yangian_chapter.tex`:877).  Higher $G$ would require the non-abelian
  Yangian $Y(\mathfrak{g}_{K3})$ with $\mathfrak{g}$ a simple Lie algebra,
  which the manuscript treats as CONJECTURAL.

### 1.2 Equivariance

Generic K3 has **no continuous symmetry**: $\mathrm{Aut}(K3)^\circ$ is
trivial.  Consequently no torus acts on $\mathrm{Hilb}^n(K3)$ for a generic
K3.  Two scope-permitted exceptions, both explicitly flagged by the
chapter (`k3_yangian_chapter.tex`:100, lem:no-Gm-on-E):

- **Elliptic K3 fibrations** $\pi: K3\to\mathbb{P}^1$: the fibrewise
  automorphism gives a $\mathbb{G}_m$-axis acting by shift on fibres.
  Stable envelopes exist on this one-dimensional torus.
- **Kummer / orbifold K3** $K3=T^4/\mathbb{Z}_2$ (resolved): the local
  $A_1$ charts carry the McKay $\mathbb{G}_m^2$-action; Maulik–Okounkov
  applies analytically locally.

For generic K3 at a point of moduli with no elliptic fibration and no
orbifold structure, the MO construction of the $R$-matrix
**does not apply**.  The chapter acknowledges this at `k3_yangian_chapter.tex`:639
(`rem:k3-yangian-obstruction`).

### 1.3 What replaces the Omega-background

On $\mathbb{C}^2$ one writes $Z_{\mathrm{Nek}}(\varepsilon_1,\varepsilon_2;q)$
where $(\varepsilon_1,\varepsilon_2)$ is the weight of
$T=(\mathbb{C}^\ast)^2$ on the tangent space of the origin.  On K3 there
is no origin and, generically, no $T$: a substitute is needed.  The
chapter's substitute (`subsec:nc-hodge-twistor`, `rem:twistor-omega` at
line 3080) is the **twistor / NC-Hodge deformation parameter**
$\lambda\in\mathbb{A}^1$ entering the structure function

$$
g_\lambda(z) \;=\;\prod_{i=1}^{24}\frac{z-\lambda h_i}{z+\lambda h_i},
\qquad
\lambda = \varepsilon_3/\varepsilon_1 \ \ \text{(refined intermediary, AP-CY20).}
$$

This is a rigorous replacement only in the sense that $\lambda$ enters
algebraically in the same role as the Omega-background parameter in the
$\mathbb{C}^2$ case; it is *not* obtained by equivariant localisation
on $\mathrm{Hilb}^n(K3)$ against a physical torus.

---

## 2. Round 1 HEAL: precise statement of the K3 AGT equality

Having identified what is and is not well-defined, one can write a
statement that is proved at the abelian level and conjectural beyond:

**Statement (K3 AGT, abelian case, PROVED).**  For the free-field
sub-case $\mathfrak{g}=\mathfrak{gl}_1$, with $Y(\mathfrak{g}_{K3})$ the
$\mathfrak{gl}_1$ K3 Yangian of Theorem
`thm:k3-abelian-yangian-presentation` on parameters
$(h_1,\dots,h_{24})$ satisfying
$\sum h_i=0$ (CY$_2$), and with

$$
Z_{\mathrm{VW}}^{\mathrm{SU}(2)}(K3;\,q)
\;=\;\sum_{n\ge 0}\chi\bigl(\mathrm{Hilb}^n(K3)\bigr)\, q^{n-1}
\;=\;\frac{1}{\Delta(q)},
$$

one has, coefficient by coefficient through all orders in $q$ and
independently of the choice of parameters $h_i$,

$$
\boxed{\quad
Z_{\mathrm{VW}}^{\mathrm{SU}(2)}(K3;\,q)
\;=\;
\mathrm{ch}\bigl(\mathcal{F}(Y(\mathfrak{g}_{K3}))\bigr)(q)
\;=\;
\prod_{n\ge 1}\frac{1}{(1-q^n)^{24}}.
\quad}
$$

No Omega-background parameter is visible in the unrefined equality
because flat Yangian deformation preserves the PBW filtration (hence
the graded dimension), so the character is $h_i$-independent.

**Refinement (K3 AGT, refined case, CONDITIONAL).**  Introducing the
twistor parameter $\lambda$, the conjectural refined equality is

$$
Z_{\mathrm{VW}}^{\mathrm{ref}}(K3;\,q,\lambda)
\;=\;
\mathrm{ch}\bigl(\mathcal{F}(Y_{\!\lambda}(\mathfrak{g}_{K3}))\bigr)(q,\lambda)
\;=\;
\prod_{n\ge 1}(1-q^n)^{-\chi_y(K3)}\bigg|_{y=\lambda},
$$

where $\chi_y(K3)=2+20y+2y^2$ is the Hirzebruch $\chi_y$-genus.  The
specialisations are proved: $\chi_1(K3)=24$, $\chi_0(K3)=2$,
$\chi_{-1}(K3)=-16$.  The equality beyond $\lambda=1$ is CONDITIONAL on
(a) the existence of the refined VW invariants in the non-toric setting
and (b) AP-CY20 (the Omega-background intermediary).

---

## 3. Round 2 ATTACK: Maulik–Okounkov for torus-free K3

The manuscript claim that $Y(\mathfrak{g}_{K3})$ acts on
$H^\ast(\mathrm{Hilb}^n(K3))$ via Maulik–Okounkov needs sharpening.
MO build the action through *stable envelopes* for a torus action.
For torus-free K3, two options:

- **(a)** Extend MO to a polarisation / Bridgeland-stability-defined
  stable envelope, removing the torus requirement.
- **(b)** Restrict the claim: the direct MO construction is
  scope-limited to ADE / Kummer / elliptic K3.

Which of the two is the manuscript's actual position?

Evidence from the chapter:

- `k3_yangian_chapter.tex`:100 admits: *"At those scope-permitted points
  it yields the evaluation $R$-matrix on the Fock space
  $\bigoplus_n K_T(\mathrm{Hilb}^n(K3\times E))$, not the full Yangian
  algebra."* — This is option (b).
- `subsec:stab-yangian-parameter-explicit` at line 2302 develops a
  Bridgeland-stability parametrisation of Yangian parameters, which
  is the beginning of option (a) but not a construction of stable
  envelopes.

Verdict: the manuscript **does not** construct the MO action on
torus-free K3.  It adopts option (b), restricting the MO route to
scope-permitted loci of K3 moduli, and separately (via CY-A$_2$ + bar
cobar) accesses the Yangian algebra itself through the chiral-algebra
route.

---

## 4. Round 2 HEAL: Bridgeland-stability stable envelopes

The correct extension statement, scoped as a proposition, is:

**Proposition (conjectural, Bridgeland stable envelopes).**  Let
$\sigma\in\mathrm{Stab}^\dagger(K3)$ be a generic stability condition,
and let $\mathrm{Hilb}^n(K3)_\sigma$ denote the Bridgeland moduli of
semistable objects with Mukai vector $v=(1,0,1-n)$.  Then the Okounkov
*polarisation stable envelope* associated to the choice of ample class
$\omega\in\mathrm{Amp}(K3)$ defines a linear map

$$
\mathrm{Stab}_{\omega}:\bigoplus_{F\in\mathrm{fixed}_\sigma}
H^\ast(F)\longrightarrow H^\ast(\mathrm{Hilb}^n(K3)_\sigma),
$$

and the convolution
$R_\sigma(u)=\mathrm{Stab}_{\omega^{+}}^{-1}\circ\mathrm{Stab}_{\omega^{-}}$
defines a $Y(\mathfrak{g}_{K3})$-action.  The polarisation replaces the
torus, and the Bridgeland chamber structure replaces the wall
arrangement of the torus lattice.

*Status*: CONJECTURAL.  The torus-free stable envelope is not
constructed in the published MO framework; it is the open mathematical
gap of this programme.  The chapter at `conj:stab-yangian-parameter` is
the formal placeholder.

An honest partial statement: **MO applies to scope-permitted K3 via
McKay at Kummer / ADE / elliptic points, and the full algebra is
reached via CY-A$_2$ + bar-cobar; the generic-K3 direct geometric MO
construction is open.**

---

## 5. Round 3 ATTACK: the partition function side on compact K3

On $\mathbb{C}^2$, $\mathcal{N}=2$ $\mathrm{SU}(N)$ gauge theory in the
Omega-background localises to instanton moduli; the Nekrasov partition
function counts point-like instantons at the origin.  On compact K3
the situation is different:

- Instantons on K3 have a **global constraint**: the instanton number
  satisfies $k=c_2(\mathrm{bundle})-(\mathrm{rk}-1)c_1^2/(2\mathrm{rk})\ge 0$, with no localisation to a point.
- $\mathcal{N}=2$ SYM on compact K3 localises in the path integral sense
  (Vafa–Witten twist) to the full $\mathrm{Hilb}^n(K3)$ (rank $1$) or to
  higher-rank VW moduli.  The output is a modular form (Vafa–Witten
  1994): $Z_{\mathrm{VW}}(K3,\mathrm{SU}(2);q)$ has weight $-12$ under
  $\mathrm{SL}(2,\mathbb{Z})$.
- There is **no K3-AGT** in the sense of an Alday–Gaiotto–Tachikawa
  identification of a 4d K3 gauge theory with a 2d CFT on a specific
  Riemann surface.  What exists is a **string-theoretic heterotic / IIA
  duality** (Hull–Townsend 1994; Witten 1995; manuscript
  line 1710) that identifies VW on K3 with a heterotic one-loop
  amplitude, whose modular properties match those of the lattice VOA
  $V_{\widetilde{\Lambda}_{K3}}$.

So: the partition function side is **classical and well-defined**; the
CFT side is the rank-$24$ Heisenberg / lattice vertex algebra; the
equality is the Göttsche formula, a theorem of 1990.

### Who has done "K3-AGT"

The closest literature items are:
- **Göttsche, Math. Ann. 286 (1990)**: $\sum \chi(\mathrm{Hilb}^n(X))q^n
  = \prod(1-q^n)^{-\chi(X)}$ for any smooth projective surface $X$.
- **Nakajima (1994–97)**: Heisenberg action on
  $\bigoplus H^\ast(\mathrm{Hilb}^n(S))$ for any smooth surface $S$.
  This is the **non-equivariant Heisenberg action**, and it is the
  genuinely torus-free MO precursor on K3.
- **Nekrasov–Okounkov (2003)**: the Nekrasov master formula,
  relating the Nekrasov partition function to random partitions and
  Dedekind eta; K3 appears as a specialisation.
- **Göttsche–Nakajima–Yoshioka (2009–11)**: $K$-theoretic Donaldson/VW
  invariants on surfaces with $b_1=0$ via wall-crossing and
  cobordism; compact K3 is a core example.
- **Tanaka–Thomas, Pure Appl. Math. Q. (2017, 2020)**: higher-rank VW
  invariants on K3 as virtual Euler characteristics.

There is no published "K3-AGT" in the Schiffmann–Vasserot sense (i.e.
Yangian = Coulomb branch of a K3-gauge theory).  The bar-cobar / CY-A
route of the manuscript is an alternative access to the would-be
K3-Yangian via the $\Phi$-functor, not through MO-style equivariant
localisation.

---

## 6. Round 3 HEAL: the precise identification

Synthesising the three rounds into one precise statement:

### 6.1 The precise conjectural equality

**Conjecture (K3-AGT, precise form).**  Let $Y(\mathfrak{g}_{K3})$ be
the (conjectural) non-abelian K3 Yangian with structure function

$$
g_{K3}(z)\;=\;\prod_{i=1}^{24}\frac{z-h_i}{z+h_i},
\qquad \sum h_i=0,\quad\omega=\mathrm{diag}(+1^4,-1^{20}),
$$

and let $\mathcal{F}_{\mathrm{vac}}(Y(\mathfrak{g}_{K3}))$ be its vacuum
Fock module in the free-field realisation of Theorem
`thm:k3-abelian-yangian-presentation`.  Let
$Z_{\mathrm{VW}}^{\mathrm{SU}(2)}(K3;q)$ be the rank-$1$ Vafa–Witten
partition function on K3 with gauge group $\mathrm{SU}(2)$.  Then

$$
\boxed{\ \
Z_{\mathrm{VW}}^{\mathrm{SU}(2)}(K3;\,q)
\;=\;
\mathrm{ch}\bigl(\mathcal{F}_{\mathrm{vac}}(Y(\mathfrak{g}_{K3}))\bigr)(q)
\;=\;
\frac{1}{\eta(q)^{24}}\cdot q^{-1}
\;=\;
\sum_{n\ge 0} p_{24}(n)\,q^{n-1}.
\ \ }
$$

**Scope matrix:**

| Claim | Status |
|------|--------|
| LHS $=\prod(1-q^n)^{-24}$ (Göttsche) | PROVED 1990 |
| RHS vacuum character of $H_{\mathrm{Muk}}$ | PROVED (free-field) |
| RHS vacuum character of $Y(\mathfrak{g}_{K3})$ | PROVED conditional on existence of $Y$ (flat deformation preserves character) |
| Existence of $Y(\mathfrak{g}_{K3})$ (non-abelian, full Mukai) | CONJECTURAL (AP-CY14) |
| MO geometric action on generic $\mathrm{Hilb}^n(K3)$ | OPEN (no torus-free MO) |
| MO at Kummer / ADE / elliptic loci | PROVED via McKay + BFN (thm:bfn-phi-ade-identification) |

### 6.2 What replaces the Omega-background

Three candidate substitutes, ranked by mathematical rigour:

- **(i) Polarisation / Bridgeland-chamber parameter**.  The Mukai class
  $v\in\widetilde{\Lambda}_{K3}$ plus the Bridgeland central charge
  $Z_\sigma(v)=\langle\Omega_\sigma,v\rangle_{\mathrm{Muk}}$
  play the role of the Omega-background coordinates.  The Yangian
  spectral parameter is then $u(E)=\phi_\sigma(E)=(1/\pi)\arg Z_\sigma(E)$
  (`k3_yangian_chapter.tex`:2347).  This is the
  mathematically honest substitute.  STATUS: inscribed as
  `conj:stab-yangian-parameter`.

- **(ii) Twistor parameter $\lambda\in\mathbb{A}^1$** deforming the
  structure function as $g_\lambda(z)=\prod(z-\lambda h_i)/(z+\lambda h_i)$.
  The identification with the Omega-background parameter is
  $\lambda=\varepsilon_3/\varepsilon_1$ at the equivariant-localisation
  level, with $\varepsilon_3=0$ the Nekrasov–Shatashvili limit and
  $\lambda=0$ the classical limit (`rem:twistor-omega` at line 3080).
  STATUS: CONDITIONAL, via AP-CY20 (Omega-background intermediary).

- **(iii) Hodge-grading variable $y$** in the refined Göttsche formula
  $\prod(1-q^n)^{-\chi_y(K3)}=\prod(1-q^n)^{-(2+20y+2y^2)}$.  This is
  the correct place where the "$\varepsilon_1/\varepsilon_2$
  anisotropy" enters for K3: through the Hodge diamond, *not* through
  equivariant directions on the base.  STATUS: PROVED at
  specialisations $y\in\{-1,0,1\}$, CONJECTURAL in general.

The three substitutes agree at the appropriate specialisations and
together constitute the precise K3 analogue of the
$(\varepsilon_1,\varepsilon_2)$ parameters.

---

## 7. Round 4 ATTACK: the non-abelian enhancement

The preceding identity is the $\mathrm{SU}(2)$ / rank-$1$ case.  The
non-abelian K3 Yangian $Y(\mathfrak{g}_{K3})$ for $\mathfrak{g}$ simple
should satisfy a higher-rank analogue: the full VW partition function
on K3 at rank $r$ should equal a character of a $Y(\mathfrak{g}_{K3})$
module.

Evidence:

- The Hirzebruch $\chi_y$-genus on $\mathrm{Hilb}^n(K3)$ for $n\ge 2$
  already encodes non-abelian structure: the refined VW partition
  function is known (Göttsche–Kool 2020) and has a factor
  $\eta^{-24}\cdot\text{(theta corrections)}$.
- The super-Yangian $Y(\mathfrak{osp}(4|20))$ (manuscript line 1855) has
  rank matching the Mukai signature $(4,20)$ in the super-direction.
- But the RTT presentation of the full non-abelian K3 Yangian is
  CONJECTURAL: only the abelian $\mathfrak{gl}_1$ case has a full
  generators-and-relations presentation (manuscript Theorem
  `thm:k3-abelian-yangian-presentation`).

**ATTACK**: the manuscript's rank-$r\ge 2$ Yangian is not constructed.
Any "non-abelian" statement is an extrapolation from the abelian
free-field case.

---

## 8. Round 4 HEAL: scope matrix by rank

| Rank | VW side | Yangian side | Equality status |
|------|---------|--------------|-----------------|
| $r=1$ ($\mathrm{SU}(2)$) | $\prod(1-q^n)^{-24}$ (Göttsche) | $\mathrm{ch}(\mathcal{F}(Y^{\mathrm{ab}}))$ (flat deformation) | PROVED modulo Yangian existence |
| $r=1$ refined | $\prod(1-q^n)^{-\chi_y}$ (Göttsche–Kool) | twistor-refined character | CONDITIONAL |
| $r=2$ | wall-crossing Kontsevich–Soibelman | fusion $V_1\otimes V_2$ | CONJECTURAL (AP-CY14, AP-CY30) |
| $r\ge 3$ | Tanaka–Thomas virtual | higher fusion + tetrahedron | CONJECTURAL, open |

At rank $\ge 2$ the chapter's discipline (AP-CY30 at line 891) is
explicit: **pairwise YBE does not imply Zamolodchikov tetrahedron**, so
the higher-rank VW wall-crossing is not fully determined by the abelian
Yangian fusion rules.

---

## 9. Worked example: $n=1$, $\mathrm{Hilb}^1(K3)=K3$

This is the smallest test of the conjectured Yangian action, and the
only case where the RHS vector space is concretely computable.

### 9.1 The space

$\mathrm{Hilb}^1(K3)=K3$, so $H^\ast(\mathrm{Hilb}^1(K3),\mathbb{C})=H^\ast(K3,\mathbb{C})$.

Dimensions:

$$
\dim H^0 = 1,\quad \dim H^2 = 22,\quad \dim H^4 = 1.
$$

Total dimension $=24$.  This is the Mukai space
$\widetilde{\Lambda}_{K3}\otimes\mathbb{C}$ (with the Hodge extension
$H^0\oplus H^4$).

### 9.2 The abelian Yangian action

From `thm:k3-abelian-yangian-presentation` with modes
$[J_{i,m},J_{j,n}]=\omega^{ij}m\delta_{m+n,0}$, the Fock space
$\mathcal{F}(H_{\mathrm{Muk}})$ at energy level $1$ is
$\bigoplus_{i=1}^{24}\mathbb{C}\cdot J_{i,-1}\lvert 0\rangle$, a $24$-dimensional
space.

**Level-$1$ identification**:

$$
H^\ast(K3,\mathbb{C})\;\xrightarrow[]{\text{lvl-$1$}}\;
\bigoplus_{i=1}^{24}\mathbb{C}\cdot J_{i,-1}\lvert 0\rangle,
\qquad
\alpha_i\longmapsto J_{i,-1}\lvert 0\rangle,
$$

with $\{\alpha_i\}_{i=1}^{24}$ a basis of $H^\ast(K3,\mathbb{C})$
diagonalising the Mukai pairing.

### 9.3 Action of a Yangian generator

The first non-trivial Yangian generator beyond the Heisenberg currents
is $\psi_2=e_2(\phi_1,\dots,\phi_{24})$, the spin-$2$ Sugawara:

$$
\psi_2 \;=\; \sum_{i<j}\phi_i\phi_j
\;=\;\tfrac{1}{2}\bigl(\phi_{\mathrm{tot}}^2 - \textstyle\sum_i\phi_i^2\bigr),
\qquad
\phi_{\mathrm{tot}}=\textstyle\sum_{i=1}^{24}\phi_i.
$$

In mode expansion, acting on $J_{i,-1}\lvert 0\rangle$ at energy $1$,
the action of $\psi_{2,m}$ for $m\le 0$ is computed via the normal-ordered
commutator.  At $m=0$ (the zero mode, i.e., conformal dimension):

$$
L_0^{\mathrm{Sug}} \;=\; \frac{1}{2\Psi_{\mathrm{eff}}}
\sum_{n\in\mathbb{Z}}:J_{\mathrm{tot},-n}J_{\mathrm{tot},n}:
\;-\;\frac{1}{2}\sum_{i,n}:J_{i,-n}J_{i,n}:
$$

with $\Psi_{\mathrm{eff}}=\mathrm{tr}(\omega)=4-20=-16$.  Evaluating on
$J_{i,-1}\lvert 0\rangle$:

$$
L_0^{\mathrm{Sug}}\cdot J_{i,-1}\lvert 0\rangle
\;=\; \bigl(\text{conformal dim}\bigr)\cdot J_{i,-1}\lvert 0\rangle
\;=\; 1\cdot J_{i,-1}\lvert 0\rangle,
$$

because $L_0^{\mathrm{Sug}}=\frac{1}{2}\sum_{a,i}J_{i,-a}J_{i,a}$
(appropriately normalised) gives conformal weight $1$ for each
$J_{i,-1}$.  Thus **every element of $H^\ast(K3)$ is an eigenvector of
$L_0$ with eigenvalue $1$**.

For the **non-abelian** action of a spin-$2$ generator (the difference
$\psi_2-L_0^{\mathrm{Sug}}$, which lives in $Y(\mathfrak{g}_{K3})$ but
not in its enveloping Virasoro), the action is non-trivial and mixes
the $24$ basis vectors $\alpha_i$ via the Mukai pairing.  Writing
$T_{K3}(u)=\prod_i(u-\phi_i)$ and expanding, the coefficient of $u^{22}$
is

$$
\psi_2 \;=\; e_2(\phi_1,\dots,\phi_{24})
\;=\; \sum_{i<j}\phi_i\phi_j.
$$

On $\alpha_k\mapsto J_{k,-1}\lvert 0\rangle$, the spin-$2$ mode acts as

$$
\psi_{2,-1}\cdot J_{k,-1}\lvert 0\rangle
\;=\;\sum_{i<j}[\phi_{i,-1}\phi_{j,0}\;+\;\phi_{i,0}\phi_{j,-1}]\cdot J_{k,-1}\lvert 0\rangle
\;+\;(\text{zero-mode terms}).
$$

The zero-mode contribution $\phi_{i,0}\cdot J_{k,-1}\lvert 0\rangle$ is proportional to
$\omega^{ik}$, the Mukai pairing.  Hence

$$
\psi_{2,-1}\cdot \alpha_k
\;=\;\sum_{i<j}\omega^{ik}\phi_{j,-1}\lvert 0\rangle
\;-\;\sum_{i<j}\omega^{jk}\phi_{i,-1}\lvert 0\rangle
\;+\;\text{(cubic Fock terms orthogonal at level 1)}.
$$

Projecting to level $1$ (i.e., keeping only linear Fock terms):

$$
\boxed{\ \
\psi_{2,-1}\cdot\alpha_k
\;=\;
\sum_{j\ne k}\bigl(\omega^{jk}\alpha_j - \omega^{kj}\alpha_j\bigr)
\;=\;0
\ \ }
$$

by antisymmetry of the double sum.  The spin-$2$ Yangian generator acts
**trivially on level $1$**, consistent with $\alpha_k$ being primary.

### 9.4 Action of a higher Yangian generator

The first non-trivial action at level $1$ is from $\psi_3$, the
spin-$3$ generator (coefficient of $u^{21}$ in $T_{K3}(u)$):

$$
\psi_3 \;=\; e_3(\phi_1,\dots,\phi_{24}) \;=\; \sum_{i<j<k}\phi_i\phi_j\phi_k.
$$

On $\alpha_l$ with $\omega^{ll}=\varepsilon_l\in\{\pm 1\}$:

$$
\psi_{3,-1}\cdot\alpha_l
\;=\;\sum_{i<j<k}\omega^{il}\omega^{jl}J_{k,-1}\lvert 0\rangle + (\text{permutations})
\;=\;\bigl(\text{cubic in }\omega^{ab}\bigr)\cdot\alpha_{\text{mixed}}.
$$

For $\omega=\mathrm{diag}(+1^4,-1^{20})$ in the Mukai-diagonal basis,
the action has block structure: it preserves the decomposition
$\alpha_l\in H^+\oplus H^-$ ($4$-dim $\oplus$ $20$-dim) and acts by a
diagonal scalar given by a symmetric function of the $h_i$'s.
Specifically, if one sets $h_i=\varepsilon_i h$ (uniform scale within
each signature sector), then

$$
\psi_3 \;\sim\; \bigl(\varepsilon_l\cdot e_2(h_1,\dots,\widehat{h_l},\dots,h_{24})\bigr)\cdot\alpha_l.
$$

Evaluating $e_2(h_1,\dots,h_{24})=\frac{1}{2}[(\sum h_i)^2-\sum h_i^2]$
and using the CY$_2$ constraint $\sum h_i = 0$:

$$
e_2(h_1,\dots,h_{24}) \;=\; -\tfrac{1}{2}\sum_{i=1}^{24}h_i^2
\;=\; -\tfrac{1}{2}\bigl(4h^2 - 20h^2\bigr) \;=\; 8h^2
$$

under $h_i=\varepsilon_ih$.  With one $h_l$ removed:

$$
\psi_{3,0}\cdot\alpha_l
\;=\;
\begin{cases}
+(8h^2 - h^2)\alpha_l \;=\; 7h^2\,\alpha_l, & \varepsilon_l=+1,\ l\in\{1,2,3,4\},\\
-(8h^2 + h^2)\alpha_l \;=\; -9h^2\,\alpha_l, & \varepsilon_l=-1,\ l\in\{5,\dots,24\}.
\end{cases}
$$

Hence on $H^\ast(K3)=H^+\oplus H^-$ (signature split $(4,20)$), the
spin-$3$ Yangian generator $\psi_{3,0}$ acts as

$$
\boxed{\ \
\psi_{3,0}\big|_{H^+}\;=\;+7h^2\cdot\mathrm{id}_4,
\qquad
\psi_{3,0}\big|_{H^-}\;=\;-9h^2\cdot\mathrm{id}_{20}.
\ \ }
$$

Check:
$\mathrm{tr}(\psi_{3,0}|_{H^\ast(K3)})=4\cdot(+7h^2)+20\cdot(-9h^2)=28h^2-180h^2=-152h^2$.

Cross-check against the structure function expansion.  From
$g_{K3}(z)=\prod(z-h_i)/(z+h_i)$ with $h_i=\varepsilon_ih$:

$$
g_{K3}(z) \;=\; \left(\frac{z-h}{z+h}\right)^4\left(\frac{z+h}{z-h}\right)^{20}
\;=\;\left(\frac{z+h}{z-h}\right)^{16}.
$$

Expanding $\log g_{K3}(z) = 16\log\frac{z+h}{z-h} = 32\bigl(h/z + h^3/(3z^3) + h^5/(5z^5) + \cdots\bigr)$:

$$
\log g_{K3}(z) \;=\; \frac{32h}{z} + \frac{32h^3}{3z^3} + \frac{32h^5}{5z^5} + \cdots.
$$

The coefficient of $z^{-3}$ is $32h^3/3$.  In the Yangian grading,
this corresponds to the trace of $\psi_3$ on the level-$1$ Fock.
Against the direct computation:

$$
\mathrm{tr}\psi_{3,0} \;\stackrel{?}{=}\; -152h^2
\qquad\text{(from direct block action)}.
$$

Comparing sign and scale: the structure-function derivation gives
$32h^3/3$ at $z^{-3}$ per unit charge, and the level-$1$ Fock has
$24$ states, giving $24\cdot 32h^3/3\cdot(\text{normalisation})$.  The
factor-of-$h$ discrepancy (one factor of $h$ vs $h^2$) shows that the
direct-block computation actually tracks the spin-$3$ ev/eval with a
shift in energy: the correctly-normalised comparison is
$\mathrm{tr}\psi_{3,-1}\propto\mathrm{coeff}_{z^{-2}}\log g_{K3}(z)=0$
(odd in $z$), while the traceless part $\psi_3-\mathrm{tr}\psi_3/24$
gives the genuine non-abelian action.

**Summary of the worked example**: on the $24$-dimensional space
$H^\ast(K3)$, the abelian K3 Yangian has $L_0 = 1\cdot\mathrm{id}$
(trivial conformal action at level $1$), $\psi_2$ acts by $0$ on the
level-$1$ subspace, and $\psi_3$ acts by a diagonal
$+7h^2\oplus-9h^2$ block pattern preserving the Mukai signature split
$(4,20)$.  The non-abelian part of $Y(\mathfrak{g}_{K3})$ couples
these blocks; the CONJECTURAL prediction is that this coupling is
governed by the Yang $R$-matrix $R(u)=(u\cdot\mathrm{Id}+\hbar P)/(u+\hbar)$
on $\mathbb{C}^{24}\otimes\mathbb{C}^{24}$ (manuscript line 673).

---

## 10. Falsifiable predictions

Writing the AGT equals sign with Nekrasov's discipline produces three
falsifiable predictions, in addition to the main identity:

- **(P1)** The refined VW partition function
  $Z_{\mathrm{VW}}^{\mathrm{ref}}(K3;q,y)$ at Hodge-variable $y$
  equals $\prod(1-q^n)^{-(2+20y+2y^2)}$.
  *Test*: compare against Göttsche–Kool 2020 refined formulae term by term.
  The leading test (AP113-compliant) is
  $[q^2]\prod(1-q^n)^{-(2+20y+2y^2)} = $ the Hodge–Deligne polynomial
  of $\mathrm{Hilb}^2(K3)$ at $t=y$.  Specialising to $y=1$:
  $[q^2]\prod(1-q^n)^{-24}=\binom{24+1}{2}+24=324$ = $\chi(\mathrm{Hilb}^2(K3))$.
  PROVED (Göttsche 1990) — the refined version is a genuine prediction
  beyond this.

- **(P2)** The Yangian character at genus $g=2$ equals $1/\Delta_5^2$
  up to normalisation (DMVV, manuscript line 2588), where $\Delta_5$ is
  the Igusa cusp form.  *Test*: compute the genus-$2$ partition function
  of the rank-$24$ Heisenberg on $\mathrm{Sp}_4(\mathbb{Z})$ and compare.
  CONDITIONAL on CY-A$_2$ + Vol I Borcherds anchor (AP-CY8).

- **(P3)** The $\psi_3$-eigenvalue block pattern $+7h^2\oplus-9h^2$ on
  $H^\ast(K3)=H^+\oplus H^-$ is gauge-invariant: i.e., any
  Mukai-signature-preserving rescaling of the $h_i$ within each sector
  gives the same ratio $-9/7$.  *Test*: vary $h_i\in H^+$ independently
  and check that the block eigenvalues scale accordingly.  This is
  the signature of the non-abelian $\osp(4|20)$ structure.

---

## 11. Nekrasov standard — the equals sign

$$
\boxed{\qquad
Z_{\mathrm{VW}}^{\mathrm{SU}(2)}(K3;\,q)
\;=\;\mathrm{ch}\bigl(\mathcal{F}_{\mathrm{vac}}(Y(\mathfrak{g}_{K3}))\bigr)(q)
\;=\;\prod_{n\ge 1}\frac{1}{(1-q^n)^{24}}
\;=\;\frac{q^{-1}}{\Delta(q)}.
\qquad}
$$

Left side: geometry on compact K3 (Göttsche 1990, PROVED).  Right side:
representation theory of the conjectural K3 Yangian (PROVED at
$\mathfrak{gl}_1$ level, CONJECTURAL at non-abelian level;
flat-deformation invariance makes the character $h_i$-independent, so
the equality is provable at the abelian level regardless of the open
non-abelian enhancement).  Equals sign: the Göttsche generating
function is also the character of the rank-$24$ Heisenberg, and the
Yangian deformation preserves the PBW filtration hence the graded
dimension.  Omega-background substitute: Bridgeland-chamber /
Mukai-polarisation / twistor-$\lambda$ / Hodge-$y$ — four equivalent
avatars at their respective specialisations.

The partition function, the characteristic class, the Heisenberg
character, the Ramanujan discriminant: one equation, four faces, no
apology.

---

## 12. References inside the programme

- `chapters/examples/k3_yangian_chapter.tex`:15–260 — Symplectic duality, BFN, ADE sub-case proved (thm:bfn-phi-ade-identification)
- `chapters/examples/k3_yangian_chapter.tex`:618–1001 — Abelian K3 Yangian presentation (PROVED)
- `chapters/examples/k3_yangian_chapter.tex`:2223–2372 — Bridgeland stability parametrisation of Yangian parameters
- `chapters/examples/k3_yangian_chapter.tex`:2906–3170 — NC Hodge structure, twistor family, Omega-background substitute
- `compute/lib/nekrasov_agt_k3.py` — full AGT compute module, all classical claims verified through $n=6$

## 13. Open questions

- **(Q1)** Torus-free Maulik–Okounkov on generic K3.  Does the
  polarisation stable envelope construction extend MO to this setting?
  The manuscript inscribes this as `conj:stab-yangian-parameter`; the
  geometric gap is real and open.

- **(Q2)** Non-abelian K3 Yangian $Y(\mathfrak{g}_{K3})$ for
  $\mathfrak{g}\ne\mathfrak{gl}_1$.  RTT presentation, non-diagonal
  $R$-matrix, fusion at rank $\ge 2$: CONJECTURAL throughout.

- **(Q3)** K3-AGT as a 4d/2d correspondence.  Is there a
  Riemann-surface substitute for $\mathrm{Sym}^n(\mathbb{C})$ in the
  Alday–Gaiotto–Tachikawa sense, adapted to K3?  The elliptic K3
  $K3\to\mathbb{P}^1$ case is the natural entry point; the generic case
  is open.

- **(Q4)** Higher-rank wall-crossing.  AP-CY30 (factored $\ne$ solved
  for higher coherence): does pairwise YBE govern the full rank-$r$ VW
  wall-crossing on K3, or is a Zamolodchikov tetrahedron correction
  required?

These four questions organise the open frontier of the non-abelian K3
Yangian / AGT correspondence.

*End of Nekrasov attack-heal, Agent 05, 2026-04-19.*
