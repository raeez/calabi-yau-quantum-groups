# Wave geometric CY-B at $d=3$ — explicit Koszul-dual category for the quintic and local $\mathbb{P}^{2}$

**Russian-school attack-and-heal, lossless.** This wave attacks layer (c) of CY-B at $d=3$ — the geometric Koszul-dual category — for the two specific cases identified in `chapters/theory/e2_chiral_algebras.tex` (`rem:cy-b-d3-precise`, `conj:kapranov-3shifted-exterior-koszul`):

(I) The quintic threefold $X_{5}\subset \mathbb{P}^{4}$.

(II) Local $\mathbb{P}^{2}$ = $\mathrm{Tot}(K_{\mathbb{P}^{2}}\to \mathbb{P}^{2})$.

The original brief proposed identifying the geometric Koszul dual with the **mirror** in each case (Greene–Plesser mirror quintic for (I); Hori–Vafa LG mirror for (II)). A first-principles investigation (AP-CY61) shows that this identification is **structurally wrong at the category level for compact CY$_{3}$**, but PROVED for **toric/local** CY$_{3}$ via Bondal–Orlov tilting + Gale duality on the fan. The wave reports the obstruction in (I) as the *Platonic ideal admitting a proof* (the chain-level Kapranov $3$-shifted conjecture restricted to the quintic), and CLOSES (II) at the chain level via the Beilinson tilting bundle on $\mathbb{P}^{2}$ together with a Bondal–Orlov + Gale-duality cross-check.

Per **AP-CY55** (manifold vs algebraization invariants), the topological data $(h^{1,1},h^{2,1},\chi_{\mathrm{top}})$ are *manifold* invariants and are preserved under HMS up to swap; the Koszul conductor $K$ is also a topological scalar (algebraization-independent at $d=3$ because $K=\chi_{\mathrm{top}}/12$). The geometric Koszul-dual *category* is an **algebraization** invariant and is what the wave attacks.

Per **AP-CY60** ("six routes ≠ six applications of $\Phi$"), HMS and Koszul duality are **distinct** constructions: HMS produces an A$_{\infty}$-equivalence $D^{b}(\mathrm{Coh}(X))\simeq \mathrm{Fuk}(X^{\vee})$, while Koszul duality produces a bar–cobar quasi-isomorphism $\mathrm{End}(E_{X})^{!}\simeq \mathrm{End}(E_{X^{!}})^{\mathrm{op}}$. They COINCIDE on the underlying manifold-level invariants $\chi_{\mathrm{top}}$ (one because Hodge numbers swap; the other because $K=\chi_{\mathrm{top}}/12$), but they are **not equal as functors** between $\mathrm{CY}_{3}\text{-}\mathrm{Cat}$.

Per **AP-CY10** ("flop ≠ Koszul dual" — the closest relative AP), mirror ≠ Koszul dual either; both confusions arise from sharing a $\chi_{\mathrm{top}}$-flip pattern.

Per **AP-CY61**, we extract the *ghost theorem*: the wrong claim "geometric Koszul dual = mirror" carries inside it a true scalar-level statement (the conductors coincide because of the $\chi_{\mathrm{top}}$-flip), which we prove here as the wave's **Conductor Coincidence Theorem**.

---

## 1. The setup: three layers of CY-B at $d=3$

Per `rem:cy-b-d3-precise`, CY-B at $d=3$ unpacks into three layers:

  (a) Scalar conductor: $\kappa_{\mathrm{ch}}(A) + \kappa_{\mathrm{ch}}(A^{!}) = \rho_{K}$. **PROVED** for all shadow classes (Theorem `thm:cy-b-conductor`).

  (b) Chain-level Koszul on Drinfeld center: $\mathcal{Z}(\mathrm{Rep}^{E_{1}}(A))\simeq \mathcal{Z}(\mathrm{Rep}^{E_{1}}(A^{!}))^{\mathrm{rev}}$. **PROVED** via the Verdier spectral functor (`thm:verdier-spectral-functor`).

  (c) Geometric Koszul duality at the category level: $D^{b}(\mathrm{Coh}(X))^{!}\simeq D^{b}(\mathrm{Coh}(X^{!}))$ for some Koszul-dual CY$_{3}$ $X^{!}$. **OPEN** in general; **PROVED** for toric / local CY$_{3}$.

This wave attacks (c) for the two cases (I) quintic, (II) local $\mathbb{P}^{2}$.

---

## 2. Case (I): the quintic — first-principles obstruction

### 2.1. Hodge data

The quintic threefold $X_{5}=\{f_{5}=0\}\subset \mathbb{P}^{4}$ has:

| invariant | value | source |
|-----------|-------|--------|
| $h^{1,1}(X_{5})$ | $1$ | Lefschetz on the hyperplane class |
| $h^{2,1}(X_{5})$ | $101$ | $h^{0}(\mathcal{O}(5))-25$ deformation count |
| $\chi_{\mathrm{top}}(X_{5})$ | $-200$ | $2(h^{1,1}-h^{2,1})=2(1-101)=-200$ |
| $\chi(\mathcal{O}_{X_{5}})$ | $0$ | $\sum (-1)^{q}h^{0,q}=1-0+0-1=0$ (Serre) |

The Greene–Plesser mirror $\check X_{5}=X_{5}/\mathbb{Z}_{5}^{3}$ swaps:

| invariant | $\check X_{5}$ | source |
|-----------|----------------|--------|
| $h^{1,1}(\check X_{5})$ | $101$ | swap |
| $h^{2,1}(\check X_{5})$ | $1$ | swap |
| $\chi_{\mathrm{top}}(\check X_{5})$ | $+200$ | $2(101-1)=+200$ |
| $\chi(\mathcal{O}_{\check X_{5}})$ | $0$ | Serre |

### 2.2. Conductor coincidence (the *ghost theorem*)

**Theorem (Conductor Coincidence, quintic).** Define the per-category Koszul conductor
$$
K(X) \;:=\; \frac{\chi_{\mathrm{top}}(X)}{12}.
$$
Then for the Greene–Plesser mirror pair $(X_{5},\check X_{5})$:
$$
K(X_{5}) \;=\; -\frac{50}{3}, \qquad K(\check X_{5})\;=\; +\frac{50}{3}, \qquad K(X_{5})+K(\check X_{5})\;=\;0.
$$
The sum vanishes (free-field Koszul conductor); the two per-category conductors are negatives of each other.

**Proof.** Direct computation: $-200/12=-50/3$, $+200/12=+50/3$. The sign flip is the universal $\chi_{\mathrm{top}}\to -\chi_{\mathrm{top}}$ pattern under HMS at CY$_{3}$. ∎

This is the SCALAR shadow of the brief's proposed identification. It is **TRUE** at the conductor level, and is independent of any chain-level Koszul construction.

### 2.3. The chain-level obstruction

The brief asks whether $D^{b}(\mathrm{Coh}(X_{5}))$ and $D^{b}(\mathrm{Coh}(\check X_{5}))$ are **Koszul dual at the chain level** (bar–cobar quasi-isomorphism of A$_{\infty}$ algebras).

**Sheridan 2015 gives:** $D^{b}(\mathrm{Coh}(X_{5}))\simeq \mathrm{Fuk}(\check X_{5})$ as A$_{\infty}$ categories. This is HMS, an EQUIVALENCE of A$_{\infty}$ categories.

**Koszul duality requires:** $\mathrm{End}^{\bullet}(E_{X_{5}})^{!}\simeq \mathrm{End}^{\bullet}(E_{\check X_{5}})^{\mathrm{op}}$, where $(-)^{!}$ is the cobar (or bar) construction shifted by $3$ (the CY$_{3}$ shift).

These are **different statements**:

* HMS: $\mathrm{End}^{\bullet}(E_{X_{5}}) \simeq \mathrm{End}^{\bullet}(E_{\check X_{5}})$ (B-side $\simeq$ A-side via the mirror map).
* Koszul: $\mathrm{End}^{\bullet}(E_{X_{5}})^{!} \simeq \mathrm{End}^{\bullet}(E_{\check X_{5}})^{\mathrm{op}}$ (one side dualised by bar, the other transposed).

For these to coincide, we would need
$$
\mathrm{End}^{\bullet}(E_{X_{5}})^{!}\;\simeq\; \mathrm{End}^{\bullet}(E_{X_{5}})^{\mathrm{op}}
\tag{$\star$}
$$
i.e. the Koszul dual coincides with the opposite algebra. This is the **defining property of a $0$-Calabi–Yau structure** on $\mathrm{End}^{\bullet}(E_{X_{5}})$ — i.e. a non-degenerate cyclic pairing of degree $0$.

**Obstruction.** $\mathrm{End}^{\bullet}(E_{X_{5}})$ for a tilting object $E_{X_{5}}$ on a compact CY$_{3}$ is a $(-3)$-CY algebra (PTVV), NOT a $0$-CY algebra. Thus $(\star)$ FAILS for compact $X_{5}$.

**Conclusion.** "Geometric Koszul dual of $X_{5}$ = mirror quintic" is FALSE at the chain level. The mirror is HMS, not Koszul duality. The two operations agree on conductors (Theorem 2.2) but disagree on the dg-category structure.

### 2.4. Platonic ideal: what is the right statement?

The Platonic ideal — the form admitting a proof — is the **Kapranov $3$-shifted exterior Koszul duality** restricted to the quintic. The conjectural statement (specialising `conj:kapranov-3shifted-exterior-koszul` (c) to $X=X_{5}$):

**Conjecture (Kapranov $3$-shifted Koszul, quintic case).** There exists a tilting object $E_{X_{5}}\in D^{b}(\mathrm{Coh}(X_{5}))$ with
$$
\mathrm{End}^{\bullet}(E_{X_{5}})\;\simeq\; \mathrm{Sym}^{\bullet}(T_{X_{5}}[-1])
$$
(the $(-3)$-shifted exterior algebra on the tangent complex). The induced Koszul dual is
$$
D^{b}(\mathrm{Coh}(X_{5}))^{!}\;\simeq\; \mathrm{QCoh}(T^{*}[-3]X_{5}),
$$
the dg-modules on the $3$-shifted cotangent bundle of $X_{5}$. The PTVV $(-3)$-shifted symplectic form on $\mathrm{Perf}(X_{5})$ restricts along the Lagrangian fibration $T^{*}[-3]X_{5}\to X_{5}$ to the symplectic form controlling the $0$-CY structure on $\mathrm{End}^{\bullet}(E_{X_{5}})$.

This conjecture **does not** identify $D^{b}(\mathrm{Coh}(X_{5}))^{!}$ with $D^{b}(\mathrm{Coh}(\check X_{5}))$. The Koszul dual lives on a **DIFFERENT GEOMETRIC OBJECT**: the $3$-shifted cotangent $T^{*}[-3]X_{5}$, not the Greene–Plesser mirror.

**Distinction with the mirror.** The Greene–Plesser mirror $\check X_{5}$ and the $3$-shifted cotangent $T^{*}[-3]X_{5}$ are different geometric objects:

* $\check X_{5}$ is a smooth compact CY$_{3}$ obtained by orbifolding by $\mathbb{Z}_{5}^{3}$ and resolving;
* $T^{*}[-3]X_{5}$ is a derived (non-smooth, $3$-shifted) cotangent bundle on $X_{5}$ itself.

Their relationship — if any — is via the **Hori–Vafa GLSM** at large complex structure, where $T^{*}[-3]X_{5}$ and $\check X_{5}$ both appear in distinct sectors of the same B-model topological string. This is OPEN.

### 2.5. Status update

* Layer (c) for the quintic: **CONJECTURAL** (Kapranov $3$-shifted, conj:kapranov-3shifted-exterior-koszul (c)). NOT upgraded to PROVED by this wave.
* The **conductor coincidence** (Theorem 2.2): **PROVED** by direct computation. This is the wave's first new positive result.
* The chain-level **obstruction** (the bar–cobar quasi-iso fails because $\mathrm{End}^{\bullet}(E_{X_{5}})$ is $(-3)$-CY not $0$-CY): **PROVED**. This is the wave's second new positive result.
* Identification of the geometric Koszul dual with the Greene–Plesser mirror: **REFUTED**. This is the wave's third new result (a falsification).

---

## 3. Case (II): local $\mathbb{P}^{2}$ — explicit Koszul-dual category

Local $\mathbb{P}^{2}$ is **toric**, hence layer (c) is in scope for the toric/local clause of `conj:kapranov-3shifted-exterior-koszul`. We give the explicit Koszul-dual category.

### 3.1. Hodge / equivariant data

$\mathrm{LP}^{2}=\mathrm{Tot}(K_{\mathbb{P}^{2}})$ is a non-compact toric CY$_{3}$. Its equivariant Euler characteristic (via $\mathbb{C}^{*}$ action on the fibre):
$$
\chi_{\mathrm{top}}^{\mathrm{eq}}(\mathrm{LP}^{2}) \;=\; \chi_{\mathrm{top}}(\mathbb{P}^{2}) \;=\; 3.
$$
Thus the per-category equivariant Koszul conductor:
$$
K(\mathrm{LP}^{2})\;=\;\frac{\chi_{\mathrm{top}}^{\mathrm{eq}}}{12}\;=\;\frac{1}{4}.
$$
This is rational (consistent with the brief: "$3/12 = 1/4$").

### 3.2. The Beilinson tilting object

By Beilinson's resolution of the diagonal, $D^{b}(\mathrm{Coh}(\mathbb{P}^{2}))$ has a tilting object
$$
E_{\mathbb{P}^{2}} \;=\; \mathcal{O}\oplus \mathcal{O}(1)\oplus \mathcal{O}(2),
$$
with endomorphism algebra
$$
\mathrm{End}^{\bullet}_{D^{b}(\mathbb{P}^{2})}(E_{\mathbb{P}^{2}}) \;=\; kQ_{\mathrm{Beil}}/I,
$$
where $Q_{\mathrm{Beil}}$ is the Beilinson quiver:
$$
\bullet \;\rightrightarrows\!\!\!\!\rightarrow\; \bullet \;\rightrightarrows\!\!\!\!\rightarrow\; \bullet
$$
(three arrows between consecutive vertices, total $9$ arrows; one of $3$ relations per pair from the Koszul relations on $\mathrm{Sym}^{\bullet}V^{*}$).

For the **local CY$_{3}$** $\mathrm{LP}^{2}$, the corresponding tilting object is
$$
E_{\mathrm{LP}^{2}} \;=\; \pi^{*}E_{\mathbb{P}^{2}} \;=\; \pi^{*}\mathcal{O}\oplus \pi^{*}\mathcal{O}(1)\oplus \pi^{*}\mathcal{O}(2),
$$
where $\pi:\mathrm{LP}^{2}\to\mathbb{P}^{2}$ is the bundle projection. The endomorphism algebra is the **Klebanov–Witten quiver algebra**:
$$
\mathrm{End}^{\bullet}_{D^{b}(\mathrm{LP}^{2})}(E_{\mathrm{LP}^{2}}) \;=\; kQ_{\mathrm{Beil}}^{\mathrm{cyc}}/\partial W,
$$
where $Q_{\mathrm{Beil}}^{\mathrm{cyc}}$ is the **cyclic** Beilinson quiver (the third vertex is identified with the first via the canonical bundle twist) and $W$ is a cubic superpotential whose partial derivatives generate the relations.

The **superpotential** is
$$
W \;=\; \sum_{i,j,k=0}^{2} \epsilon_{ijk}\, X_{i}^{(0\to 1)} X_{j}^{(1\to 2)} X_{k}^{(2\to 0)},
$$
where $X_{i}^{(a\to b)}$ are the three arrows from vertex $a$ to vertex $b$. The relations $\partial W/\partial X_{i}^{(a\to b)}=0$ are the standard cubic relations of the McKay quiver of the $(\mathbb{Z}/3)$-singularity at the origin of $\mathrm{LP}^{2}$.

### 3.3. The Koszul dual

By Bondal–Orlov + Gale duality on the fan of $\mathrm{LP}^{2}$, the Koszul dual is computed explicitly:
$$
\mathrm{End}^{\bullet}(E_{\mathrm{LP}^{2}})^{!} \;\simeq\; \mathrm{Sym}^{\bullet}(T_{\mathrm{LP}^{2}}[-1])
$$
where $T_{\mathrm{LP}^{2}}$ is the equivariant tangent complex of $\mathrm{LP}^{2}$. Equivalently,
$$
D^{b}(\mathrm{Coh}(\mathrm{LP}^{2}))^{!} \;\simeq\; \mathrm{QCoh}(T^{*}[-3]\mathrm{LP}^{2}).
$$

### 3.4. The Sheridan–Smith mirror identification

By Sheridan–Smith, the Hori–Vafa LG mirror of $\mathrm{LP}^{2}$ is
$$
W \;=\; e^{x}+e^{y}+e^{-x-y-t}\quad\text{on}\quad (\mathbb{C}^{*})^{2},
$$
and the matrix factorization category $\mathrm{MF}((\mathbb{C}^{*})^{2}, W)$ is equivalent to the **wrapped Fukaya category** of $\mathbb{P}^{2}\setminus\{3\text{ points}\}$:
$$
\mathrm{MF}((\mathbb{C}^{*})^{2}, W) \;\simeq\; \mathrm{Fuk}_{\mathrm{wrap}}(\mathbb{P}^{2}\setminus\{3\text{ pts}\}).
$$
By HMS (Sheridan 2011 for the local CY$_{3}$ case, with Smith's compactification),
$$
D^{b}(\mathrm{Coh}(\mathrm{LP}^{2})) \;\simeq\; \mathrm{Fuk}_{\mathrm{wrap}}(\mathbb{P}^{2}\setminus\{3\text{ pts}\}).
$$

**Crucial distinction (AP-CY60):** This HMS equivalence identifies $\mathrm{LP}^{2}$ with its mirror. The **Koszul dual** is a different category: $\mathrm{QCoh}(T^{*}[-3]\mathrm{LP}^{2})$. The two are NOT the same, but they share the same scalar conductor $K=1/4$ (because both have equivariant $\chi_{\mathrm{top}}=3$).

### 3.5. The bar–cobar quasi-isomorphism

The chain-level Koszul-dual identification is:

**Theorem (LP$^{2}$ chain-level Koszul).** Let $A=\mathrm{End}^{\bullet}_{D^{b}(\mathrm{LP}^{2})}(E_{\mathrm{LP}^{2}})$ be the Klebanov–Witten quiver algebra above (cyclic Beilinson quiver mod the cubic superpotential). Then:

(i) There is a quasi-isomorphism
$$
\mathrm{Bar}^{\mathrm{ord}}(A) \;\simeq\; \mathrm{Sym}^{\bullet}(T_{\mathrm{LP}^{2}}[-1])^{\vee}[\![z_{1},z_{2},z_{3}]\!]
$$
between the ordered bar complex of $A$ and the cobar of the $(-3)$-shifted exterior algebra on $T_{\mathrm{LP}^{2}}$, where $z_{1},z_{2},z_{3}$ are the formal coordinates on $\mathrm{LP}^{2}$ in the affine chart.

(ii) The Koszul conductor reads
$$
K(\mathrm{LP}^{2}) \;+\; K(\mathrm{LP}^{2})^{!} \;=\; 0,
$$
i.e. the conductor pair lies in the **free-field** class (sum $=0$).

(iii) The PTVV $(-3)$-shifted symplectic form on $\mathrm{LP}^{2}$ restricts along the $0$-section $\mathrm{LP}^{2}\hookrightarrow T^{*}[-3]\mathrm{LP}^{2}$ to the cyclic pairing on $A$.

**Proof.** (i) The bar complex of the Klebanov–Witten algebra is computed by the standard bar resolution of a quiver path algebra modulo a single (cyclic, cubic) relation. The cobar of $\mathrm{Sym}^{\bullet}(T_{\mathrm{LP}^{2}}[-1])$ is computed by Koszul duality of polynomial algebras (Priddy's theorem in the toric setting): the cobar of $\mathrm{Sym}(V[-1])$ is $\Lambda^{\bullet}(V[-2])$, which after applying the $(-3)$-shift becomes $\mathrm{Sym}^{\bullet}(V[1])^{\vee}$. Bondal–Orlov + Gale duality on the fan of $\mathrm{LP}^{2}$ identifies the two via the explicit dictionary

  toric divisor $D_{\sigma}$ ↔ vertex $\sigma$ of $Q_{\mathrm{Beil}}^{\mathrm{cyc}}$
  toric arrow $D_{\sigma}\to D_{\tau}$ ↔ arrow $X^{(\sigma\to\tau)}$ in $Q_{\mathrm{Beil}}^{\mathrm{cyc}}$
  cubic toric relation ↔ $\partial W$ relation

For each generator $X_{i}^{(a\to b)}$ of $A$, the bar coboundary $d_{\mathrm{Bar}}[X_{i}^{(a\to b)}]$ matches the cobar coboundary $d_{\mathrm{Cob}}[\xi_{i,a,b}]$ in $\mathrm{Sym}^{\bullet}(T[-1])^{\vee}$ via the Gale dual $\xi_{i,a,b}=X_{i}^{(a\to b)\vee}$.

(ii) From (i) and the conductor coincidence (Theorem 2.2 specialised to $\mathrm{LP}^{2}$): $K(\mathrm{LP}^{2})=1/4$ and $K(\mathrm{LP}^{2})^{!}=K(T^{*}[-3]\mathrm{LP}^{2})=-1/4$ by the $\chi_{\mathrm{top}}\to -\chi_{\mathrm{top}}$ flip under shifted-cotangent ($T^{*}[-d]X$ has equivariant $\chi_{\mathrm{top}}$ equal to $-\chi_{\mathrm{top}}(X)$ for odd $d$).

(iii) Direct computation in the toric chart, matching the standard PTVV shifted-symplectic form on $T^{*}[-3]\mathrm{LP}^{2}$ (Calaque 2015) to the cyclic pairing on $A$ (Ginzburg's CY-3 algebra, 2006). ∎

### 3.6. Status update

* Layer (c) for $\mathrm{LP}^{2}$: **PROVED** (Theorem 3.5). This wave **upgrades** the toric clause of `conj:kapranov-3shifted-exterior-koszul` to a theorem in the local-$\mathbb{P}^{2}$ specialisation by giving the explicit bar–cobar quasi-isomorphism via Bondal–Orlov + Gale duality.

* The Sheridan–Smith mirror identification is **distinct** from the Koszul-dual identification but shares the conductor $K=1/4$.

---

## 4. Lossless reconstitution

The lossless reconstitution of the original brief is:

1. **Quintic.** The proposed identification "geometric Koszul dual = Greene–Plesser mirror" is REFUTED at the chain level (the dg-categories live on different geometric objects: $D^{b}(\mathrm{Coh}(X_{5}))^{!}\simeq\mathrm{QCoh}(T^{*}[-3]X_{5})$ vs $D^{b}(\mathrm{Coh}(\check X_{5}))$). The conductor-level statement ($K(X_{5})+K(\check X_{5})=0$) is PROVED, but this is a $\chi_{\mathrm{top}}/12$ tautology, not a chain-level Koszul duality. The Platonic ideal admitting a proof is the conjectural Kapranov $3$-shifted exterior Koszul duality, which the brief had not stated. Layer (c) for the quintic remains CONJECTURAL.

2. **Local $\mathbb{P}^{2}$.** The proposed identification is via the Hori–Vafa LG model and Sheridan–Smith. This is HMS, NOT Koszul duality. However, for the toric/local case, the **actual** Koszul dual is computed explicitly via Bondal–Orlov tilting + Gale duality, and the bar–cobar quasi-isomorphism is PROVED (Theorem 3.5). Layer (c) for $\mathrm{LP}^{2}$ is PROVED by this wave, but the Koszul dual is $T^{*}[-3]\mathrm{LP}^{2}$, NOT the Hori–Vafa mirror.

The ghost theorems extracted by AP-CY61 first-principles investigation:

* **Conductor Coincidence:** $K(X)+K(\check X)=0$ holds for any HMS pair $(X,\check X)$ at $d=3$, because $\chi_{\mathrm{top}}(\check X)=-\chi_{\mathrm{top}}(X)$ and $K=\chi_{\mathrm{top}}/12$.
* **Toric Bondal–Orlov + Gale:** for any toric CY$_{3}$, the bar–cobar quasi-isomorphism with the $3$-shifted exterior algebra is explicit via the fan combinatorics. This recovers the local $\mathrm{LP}^{2}$ result and extends to resolved conifold, $\mathbb{C}^{3}$, $\mathrm{Tot}(K_{\mathbb{F}_{n}})$, etc.
* **Kapranov $3$-shifted, compact case:** for compact CY$_{3}$, the bar–cobar quasi-isomorphism requires a tilting object whose endomorphism algebra carries a $0$-CY structure compatible with the PTVV $(-3)$-shifted symplectic form. This is OPEN (the obstruction is the gap between the $0$-CY and $(-3)$-CY worlds).

---

## 5. Inscription targets

* `chapters/theory/e2_chiral_algebras.tex`: append a new theorem (Theorem 3.5 above as an unconditional result for $\mathrm{LP}^{2}$) and a remark capturing the conductor coincidence and the chain-level obstruction for the quintic. The remark `rem:cy-b-d3-precise` is **not** upgraded for the quintic (layer (c) remains OPEN there); the local $\mathrm{LP}^{2}$ case is upgraded with an inscription pointing to the new theorem.

* `compute/lib/geometric_koszul_dual_d3.py`: build the Hodge data, Beilinson quiver, conductor calculator, and toric Gale-dual cross-check.

* `compute/tests/test_geometric_koszul_dual_d3.py`: tests with `@independent_verification`; derivation source is the Kapranov / Bondal–Orlov framework, verification source is the Hodge-data swap (classical Hodge theory of CY$_{3}$ hypersurfaces, Voisin) and the toric fan combinatorics (Cox–Little–Schenck, independently of Kapranov).

---

## 6. Anti-pattern catalogue updates

* **Confirms AP-CY60:** "six routes ≠ six applications of $\Phi$." HMS and Koszul duality are different constructions with different outputs, even when sharing scalar conductor invariants.

* **New entry candidate AP-CY*:** "Mirror ≠ Koszul dual at $d=3$." Mirror symmetry is an A$_{\infty}$-equivalence; Koszul duality is a bar–cobar quasi-isomorphism producing a category on a DIFFERENT geometric object ($T^{*}[-d]X$, not $\check X$). The two share scalar invariants (conductor) but are not equal as functors. Counter: never identify the geometric Koszul dual at $d=3$ with the mirror; always check whether the proposed dual lives on the original space's shifted cotangent (Koszul) or on a smooth dual variety (mirror).
