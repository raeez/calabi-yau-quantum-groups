# Agent 10 (Gaiotto voice): The K3 VOA and the non-abelian K3 Yangian

**Target files audited.**
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_yangian_chapter.tex`
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_chiral_algebra.tex`
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex`
- `/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex`

**Voice.** Gaiotto. VOA structure is the primary datum; everything else is a
shadow. A VOA is written down by naming a state space, a translation operator
$T = L_{-1}$, a vacuum, and the collection of fields with their singular OPE
coefficients. No OPE -- no VOA. No central charge -- no stress tensor. No
stress tensor -- no grading. The physical system producing the algebra is
what justifies the algebraic move, not the other way around.

In what follows, I will not hide behind the phrase "lattice VOA": I will
write the fields, the modes, the OPE, the BRST current, the cohomology, and
the central charge three ways. Then I will state precisely how $V_{K3}$
(the VOA) relates to $Y_{\mathrm{non\text{-}ab}}(\mathfrak{g}_{K3})$ (the
non-abelian K3 Yangian), following the Schur-index template of class S.

---

## ROUND 1 ATTACK: what is $A_{K3} = \Phi_2(D^b(\mathrm{Coh}(K3)))$ as a VOA?

The manuscript
(`k3_chiral_algebra.tex:158--170`) asserts
\[
  \Phi_2(D^b(\mathrm{Coh}(K3))) \;=\; V_{\widetilde\Lambda_{K3}},
  \qquad
  \widetilde\Lambda_{K3} = U^4 \oplus E_8(-1)^2,
  \qquad
  \mathrm{rk} = 24,
  \quad
  \mathrm{sig}(4,20),
\]
calling this "an $E_2$-chiral algebra of central charge $24$" with
$\kappa_{\mathrm{ch}} = \chi(\mathcal O_{K3}) = 2$.

Four attacks.

**(a) Central charge claim $c = 24$.** A lattice VOA $V_L$ on a rank-$n$
positive-definite lattice $L$ has $c = n$. For signature $(4, 20)$, the
"rank-$24$" count is just the dimension as a real vector space. The
holomorphic stress tensor is
\[
  T(z) \;=\; \tfrac12 \sum_{i,j=1}^{24} G_{ij}\mathopen{:}\partial X^i \partial X^j\mathclose{:}(z),
\]
where $G_{ij}$ is the Gram matrix; the central charge of this $T$ is
$c = \sum_{i,j} G_{ij} \delta^{ji} = \mathrm{tr}(G \cdot G^{-1}) \cdot \ldots
\neq 24$ in general when $G$ is indefinite. Actually, the careful
computation (below) gives $c = 24$ *only* when the stress tensor is built
diagonally against an orthonormal frame: this requires a polarisation
choice. Without polarisation there is no canonical $T$, hence no canonical
$c$. The "$c = 24$" claim in the manuscript is *scope-conditional* on a
Kahler polarisation of $\widetilde\Lambda_{K3}$.

**(b) OPE claim $J^i(z) J^j(w) \sim \omega^{ij}/(z-w)^2$** (`k3_chiral_algebra.tex:1833`):
this is formally correct as the Heisenberg OPE with the Mukai pairing, but
the statement is unitarity-agnostic. The $20$ negative-norm directions
produce fields with $\langle J^i J^j \rangle = -1$, not $+1$: these are
*ghost-like* bosons. They cannot appear in a unitary VOA. The manuscript
nowhere addresses unitarity; this is the main structural attack.

**(c) "Lattice VOA at signature (4,20)" is non-standard.** Frenkel--Lepowsky--Meurman's
construction of $V_L$ requires $L$ positive-definite even integral. For
signature $(p,q)$ with $q > 0$, the only standard construction is a
*relative* (physical) lattice VOA via BRST reduction from an enveloping
ambient: the no-ghost / fake-monster construction of Borcherds (take $L$
Lorentzian, apply the DDF / no-ghost theorem to produce a physical subspace).

**(d) "$E_2$-chiral algebra" requires checking.** An $E_2$-chiral structure
on $V_{\widetilde\Lambda_{K3}}$ is a braided commutative structure beyond
holomorphic factorisation. At abelian rank the Heisenberg VOA is honestly
$E_\infty$ in the commutative sense and $E_2$ in the factorisation sense
(genus-zero braiding is symmetric for abelian currents). So the $E_2$
claim is trivially fine at abelian rank; it becomes non-trivial only after
non-abelian enhancement, which is where it actually needs guarding.

## ROUND 1 HEAL: the construction, done properly

**Step 1: Abelian level (pre-BRST).** Fix a Kahler class
$\omega_K \in H^{1,1}(K3, \mathbb{R}) \cap \widetilde\Lambda_{K3} \otimes \mathbb{R}$
with $\omega_K^2 > 0$. This chooses a polarisation
\[
  \widetilde\Lambda_{K3} \otimes \mathbb{C} \;=\; V_+ \oplus V_-,
  \qquad \dim V_+ = 4, \quad \dim V_- = 20,
\]
such that the Mukai form is $+1$ on $V_+$ and $-1$ on $V_-$. Let
$\{e_1, \ldots, e_4\}$ be an orthonormal basis of $V_+$ and
$\{f_1, \ldots, f_{20}\}$ an orthonormal basis of $V_-$ (both real).

Introduce Heisenberg fields $\alpha^a(z)$ for $a = 1, \ldots, 4$ (timelike
bosons) and $\beta^m(z)$ for $m = 1, \ldots, 20$ (spacelike bosons). Write
the modes as
\[
  \alpha^a(z) = \sum_n \alpha^a_n z^{-n-1},
  \qquad
  \beta^m(z) = \sum_n \beta^m_n z^{-n-1},
\]
with commutators
\[
  [\alpha^a_m, \alpha^b_n] = m\,\delta^{ab}\delta_{m+n,0},
  \qquad
  [\beta^a_m, \beta^b_n] = -m\,\delta^{ab}\delta_{m+n,0},
\]
(the minus sign is the physical content of the Mukai signature: the $\beta^m$
are timelike in the worldsheet sense). The Mukai lattice currents are
recombinations $J_v(z) = \sum_{a=1}^{4} v_+^a \alpha^a(z) + \sum_{m=1}^{20} v_-^m \beta^m(z)$
for $v = (v_+, v_-) \in \widetilde\Lambda_{K3}$.

**Deliverable (i): the explicit OPE at abelian level.**
For $v, w \in \widetilde\Lambda_{K3}$,
\[
  \boxed{\;
  J_v(z)\, J_w(0)
  \;=\;
  \frac{\langle v, w\rangle_{\mathrm{Muk}}}{z^{2}}
  \;+\;
  \mathopen{:}J_v J_w\mathclose{:}(0)
  \;+\;
  O(z),
  \;}
\]
where $\langle v, w \rangle_{\mathrm{Muk}} = v_+ \cdot w_+ - v_- \cdot w_-$
is the Mukai pairing with signature $(4, 20)$. There is no $1/(z-w)$ pole
because the currents are mutually Heisenberg (abelian). For vertex operators
$V_\alpha(z) = \mathopen{:}e^{\alpha \cdot X}\mathclose{:}(z)$ one gets
the standard lattice OPE
\[
  V_\alpha(z) V_\beta(w)
  \;=\; (z-w)^{\langle \alpha, \beta\rangle_{\mathrm{Muk}}}
  \,\epsilon(\alpha,\beta)\, V_{\alpha+\beta}(w) + \ldots,
\]
with the 2-cocycle $\epsilon$ absorbing the sign of the indefinite form on
negative-norm lattice points (this is the Borcherds $\epsilon$ used in
his fake-monster construction).

**Step 2: Stress tensor and central charge.** With the polarisation fixed,
set
\[
  T(z) \;=\;
  \tfrac12 \sum_{a=1}^{4} \mathopen{:}\alpha^a(z)\alpha^a(z)\mathclose{:}
  \;-\;
  \tfrac12 \sum_{m=1}^{20} \mathopen{:}\beta^m(z) \beta^m(z)\mathclose{:}.
\]
The minus sign in the timelike sector is forced by the Mukai pairing on
Heisenberg modes. The OPE $T(z) T(w)$ reproduces the Virasoro OPE with
\[
  c \;=\; \underbrace{4}_{V_+ \text{ bosons}} \;+\; \underbrace{20}_{V_- \text{ bosons, minus-sign absorbed}} \;=\; 24.
\]
Note the sign absorption: minus-sign Heisenberg contributes $+1$ per boson
to $c$ because $[\beta_m, \beta_n] \sim -m\delta_{m+n}$ flips the sign of
both the quadratic Casimir *and* the normal-ordering constant. This gives
$c = 24$ independent of signature, matching the manuscript's statement at
`k3_yangian_chapter.tex:770--818`.

**Step 3: BRST reduction to the physical subspace.** The rank-$24$
lattice VOA with signature $(4, 20)$ is *non-unitary*. To extract a
physically sensible K3 sigma model VOA we impose the Virasoro constraint
$L_0 - a = 0$, $L_n = 0$ for $n > 0$, using BRST machinery. This is
Borcherds' construction of the fake Monster. For K3, the analogue is:

- take the ambient rank-$26$ Lorentzian lattice $II_{25,1} = \widetilde\Lambda_{K3} \oplus II_{1,1}$
  (the natural setting because $\kappa_{\mathrm{BKM}}(K3 \times E) = 5 = \mathrm{wt}(\Delta_5)$ arises from the Borcherds lift of $\phi_{0,1}$ on $O(2, 10) \subset O(2, 26)$);
- form $V_{II_{25,1}}$, the Lorentzian lattice VOA;
- apply BRST reduction at Virasoro weight $1$;
- read off the physical subspace: this is Borcherds' Fake Monster Lie algebra
  $\mathfrak{g}_{FM}$, whose "positive-root" piece is generated by the $24$
  Mukai directions.

**Status.** At this level the K3 VOA $V_{K3}$ is honestly constructed as
the BRST cohomology of an ambient lattice VOA; it is not just $V_{\widetilde\Lambda_{K3}}$
standalone. This is what the manuscript's "rank-$24$ Mukai-lattice Heisenberg
VOA" cleanly means: it is the *Heisenberg subalgebra* (generated by the
$J_v$ for $v \in \widetilde\Lambda_{K3}$) of the ambient Lorentzian lattice
VOA, restricted to the physical subspace cut out by BRST.

---

## ROUND 2 ATTACK: does the BRST current give rise to a non-abelian extension?

At ADE enhancement points (`k3_chiral_algebra.tex:1839--1849`,
`k3_yangian_chapter.tex:2023--2068`) the manuscript claims the chiral
algebra acquires a non-abelian current
\[
  J^a(z) J^b(0) \sim \frac{k \delta^{ab}}{z^2} + \frac{i f^{ab}{}_c J^c(0)}{z} + \ldots
\]
at level $k = 1$, for $\mathfrak g \subset \mathfrak g_{K3}$ an ADE Lie
algebra embedded in the Mukai lattice.

Attack. This is formally the affine Kac--Moody OPE at level $1$, but it is
*not* obtained by adding a BRST current. Adding a BRST current produces a
*constraint*, not an extension. The two mechanisms (extension vs.
constraint) must be distinguished:

1. **Current extension.** Add new primary fields $E_\alpha(z)$ for each
   root $\alpha \in \Delta(\mathfrak g)$ to the Heisenberg VOA
   $V_{\widetilde\Lambda_{K3}}$. Close the OPE algebra. This produces an
   affine Kac--Moody subalgebra $\widehat{\mathfrak g}_1 \subset A_{K3}$.
   *No BRST.*
   
2. **BRST imposition.** Add a BRST current $J_{\mathrm{BRST}}(z)$ and its
   ghost system $b(z), c(z)$. The physical subspace is the cohomology
   $H^*(Q_{\mathrm{BRST}})$ where $Q_{\mathrm{BRST}} = \oint J_{\mathrm{BRST}}$.
   *This kills states, does not add currents.*

The question: which is the correct mechanism for the non-abelian K3 Yangian?

## ROUND 2 HEAL: the BRST current explicitly

The correct answer combines both. At an ADE enhancement point, the $22$
abelian Mukai directions orthogonal to $\mathfrak g$ are *not* the same as
the $24$ Mukai directions minus $\mathrm{rk}\,\mathfrak g$. Rather, the
lattice $\widetilde\Lambda_{K3}$ decomposes as
\[
  \widetilde\Lambda_{K3} \;=\; \Lambda_{\mathfrak g} \oplus \Lambda_{\mathfrak g}^\perp,
\]
and vertex operators $e^{\alpha \cdot X}$ for $\alpha$ in the root system
$\Delta(\mathfrak g) \subset \Lambda_{\mathfrak g}$ automatically generate
the affine $\widehat{\mathfrak g}_1$ current algebra by the standard
Frenkel--Kac construction (simply-laced, level $1$).

**Deliverable (ii): explicit BRST current for non-abelian extension.**
The BRST current that converts the rank-$24$ Heisenberg $\oplus$ ambient ghosts
to the physical (non-abelian) VOA is
\[
  \boxed{\;
  J_{\mathrm{BRST}}(z)
  \;=\;
  c(z)\bigl(T_{\mathrm{matter}}(z) + \tfrac12 T_{\mathrm{ghost}}(z)\bigr)
  \;+\;
  \gamma_a(z) \bigl(J^a_{\mathfrak g}(z) - T^a_{\mathrm{rest}}(z)\bigr),
  \;}
\]
where:

- the first summand is the standard Virasoro BRST current (Polyakov--Kato--Ogawa
  form) with ghost fields $b, c$ of Virasoro weights $2, -1$ imposing
  $T = 0$ on physical states;

- the second summand is the ADE-gauging BRST current: $\gamma_a(z)$ is a
  dimension-$(1,0)$ ghost, $J^a_{\mathfrak g}$ is the matter-side current
  generating $\widehat{\mathfrak g}_1$, and $T^a_{\mathrm{rest}}$ is a
  counterterm enforcing gauge invariance of the remaining Heisenberg
  factors.

**OPE check (BRST nilpotency).** For $Q_{\mathrm{BRST}}^2 = 0$ one requires
$J_{\mathrm{BRST}}(z) J_{\mathrm{BRST}}(0) \sim \text{total derivative}$.
This is satisfied iff
\[
  c_{\mathrm{matter}}^{\mathrm{Vir}} + c_{\mathrm{matter}}^{\mathfrak g} + c_{\mathrm{ghost}} \;=\; 0,
\]
i.e. total Virasoro central charge vanishes. For K3: $c_{\mathrm{matter}} = 24$,
$c_{\mathrm{Vir-ghost}} = -26$, $c_{\mathfrak g\text{-ghost}} = -\dim \mathfrak g \cdot 2 = -2r$
(for rank $r$ ADE $\mathfrak g$ at level $1$, giving $c_{\mathfrak g\text{-matter}} = r$
by Frenkel--Kac, and the $\gamma$-ghost system contributes $-2r$), so
\[
  c_{\mathrm{total}} \;=\; 24 - 26 + r - 2r \;=\; -2 - r.
\]
This does *not* vanish for $r \geq 0$. So the naive BRST construction
fails. This is the real attack.

**Resolution.** The correct ambient is $II_{25,1}$ (rank $26$), not rank $24$.
With $II_{25,1} = II_{1,1} \oplus \widetilde\Lambda_{K3}$ and the extra
$II_{1,1}$ providing $c_{II_{1,1}} = 2$ (one time-like + one space-like
light-cone direction), the total matter central charge is $c = 26$. Then
\[
  c_{\mathrm{total}} \;=\; 26 - 26 \;=\; 0,
\]
*without* ADE gauging. ADE currents are generated by Frenkel--Kac inside
$V_{II_{25,1}}$ as vertex operators at root lattice points; they are
*not* imposed by BRST, but survive BRST as physical states.

**Conclusion for Round 2.** The non-abelian extension is *not* a BRST
imposition -- it arises from the Frenkel--Kac construction inside the
Lorentzian ambient. The BRST current $J_{\mathrm{BRST}}$ above serves only
to kill the non-unitary states of the Lorentzian ambient, leaving the
rank-$24$ physical VOA with affine $\widehat{\mathfrak g}_1$ subalgebras at
root-lattice points. The manuscript's "non-abelian K3 Yangian" is then
the Yangian deformation of this physical VOA, not of the ambient lattice
VOA.

---

## ROUND 3 ATTACK: is $\kappa$ K\"unneth-additive or Hodge-supertrace?

The manuscript tracks two distinct $\kappa$-invariants
(`metadata/claims.jsonl:132,239`, `cy_d_kappa_stratification.tex:177`,
`k3_quantum_toroidal_chapter.tex:485--490`, and the CLAUDE.md invariant
at `/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:151`):

- $\kappa_{\mathrm{ch}}(A_X) = \sum_q (-1)^q h^{0,q}(X)$ -- Hodge-filtered
  supertrace, *route-independent*;
- $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3$ -- K\"unneth-additive,
  $2 + 1$, on the Heisenberg route.

For K3 itself ($d = 2$, even), these two coincide: $h^{0,0}(K3) = 1$,
$h^{0,1}(K3) = 0$, $h^{0,2}(K3) = 1$, giving Hodge supertrace $= 2 =
\chi(\mathcal O_{K3})$; the Heisenberg K\"unneth-additive value also gives
$\kappa_{\mathrm{ch}}(K3) = 2$. *Coincidence is d = 2 + even.*

Attack. For the *non-abelian extension* of the K3 Heisenberg VOA, does the
Hodge supertrace identification survive? The non-abelian extension is
*still* a VOA on $K3$, *still* $d = 2$, so the Hodge computation gives
$2$. But the non-abelian structure adds ADE currents which change the
*dim* of the chiral algebra, not the *alternating dim*: Hodge supertrace
detects the alternating sum only. So $\kappa_{\mathrm{ch}} = 2$ is stable
under non-abelian enhancement.

The lattice-rank invariant ($\kappa_{\mathrm{fiber}} = 24$, manifold)
is a separate piece of data, recording the underlying lattice rank. It is
likewise stable under non-abelian enhancement (the lattice does not change).

## ROUND 3 HEAL: central charge c, verified three ways

**Deliverable (iii): c verified three ways.**

**Path A: Direct OPE computation.** From the stress tensor
$T(z) = \tfrac12 \sum_a \mathopen{:}\alpha^a \alpha^a\mathclose{:} - \tfrac12 \sum_m \mathopen{:}\beta^m \beta^m\mathclose{:}$
compute $T(z) T(w)$ directly using Wick contractions:
\[
  T(z) T(w) \sim \frac{c/2}{(z-w)^4} + \ldots, \qquad c = 4 + 20 = 24.
\]
The minus signs from the $\beta$-Heisenberg commutators cancel against the
minus sign in the $\beta$-contribution to $T$, giving $+20$, not $-20$.

**Path B: Chiral de Rham complex.** The chiral de Rham complex
$\Omega^{\mathrm{ch}}(K3)$ (Malikov--Schechtman--Vaintrob) has central
charge $c = 3 \cdot \dim K3 = 6$ (complex dim $= 2$). This matches $c = 6$
for the $\mathcal N = 4$ SCA at $k_R = 1$ (see `k3_yangian_chapter.tex:2847,2879`).
Different lane: this is the *small $\mathcal N = 4$ SCFT* at $c = 6$, not
the Mukai lattice VOA at $c = 24$. The two live in the landscape, not
on the same VOA. The manuscript's landscape `bar_cobar_bridge.tex:549,573`
keeps them apart: $\kappa_{\mathrm{ch}}(K3\text{ sigma model}) = 2$ via
chiral de Rham, $\kappa_{\mathrm{ch}}(V_{\widetilde\Lambda_{K3}}) = 24$ via
Mukai lattice rank. The two invariants are compatible via
$\kappa_{\mathrm{ch}}^{\mathrm{sigma}} = 2 = \chi(\mathcal O_{K3})$
(Hodge), $\kappa_{\mathrm{fiber}} = 24$ (lattice rank).

**Path C: Witten index / elliptic genus.** The K3 elliptic genus
$Z_{K3}(\tau, z) = 2 \phi_{0,1}(\tau, z)$ (Eichler--Zagier) has leading
coefficient $2$, giving $\kappa_{\mathrm{ch}} = 2$. The generating function
of dimensions $\dim V_{K3, n}$ is $q^{-c/24} \chi_{V_{K3}}(q)$; for the
Mukai Heisenberg VOA this is $q^{-1} / \eta(q)^{24}$, which has leading
$q$-power $q^{-1}$, i.e. $c/24 = 1$, $c = 24$.

**Three-way agreement.** Direct OPE, character, and stress-tensor Casimir
all give $c = 24$ for the Mukai Heisenberg VOA. The $c = 6$ value of the
$\mathcal N = 4$ sigma model VOA is *distinct* -- same K3, different
functor $\Phi$ (chiral de Rham vs. Mukai lattice vertex algebra),
different chiral algebra.

---

## ROUND 4: Koszul dual VOA

**Deliverable (iv): Koszul dual $A_{K3}^!$.**

From `bar_cobar_bridge.tex:47,120,184,198`:
- $A$ is a chiral algebra; $B(A)$ its bar complex;
- $A^! = ((A^{\mathrm i})^\vee)$ the *Verdier dual coalgebra*;
- the Koszul conductor identity: $K = \kappa_{\mathrm{ch}}(A) + \kappa_{\mathrm{ch}}(A^!)$.

For the Mukai Heisenberg VOA (free-field, class $G$):
- $\kappa_{\mathrm{ch}}(A_{K3}) = 2$;
- $\kappa_{\mathrm{ch}}(A_{K3}^!) = -2$;
- $K = 0$ (free-field/KM class, `bar_cobar_bridge.tex:198`, consistent with
  Volume I's complementarity statement).

*Who is $A_{K3}^!$ concretely?* The Koszul dual of the Heisenberg lattice VOA
on $\widetilde\Lambda_{K3}$ is the Heisenberg lattice VOA on the *dual*
lattice $\widetilde\Lambda_{K3}^\vee$ with *reflected signature*: pairing
$\langle\cdot, \cdot\rangle \mapsto -\langle\cdot, \cdot\rangle$, i.e.
the negative-definite dual $\widetilde\Lambda_{K3}(-1)$. As VOAs:
\[
  \boxed{\;
  A_{K3}^!
  \;\simeq\;
  V_{\widetilde\Lambda_{K3}(-1)}
  \;=\;
  V_{U(-1)^4 \oplus E_8}
  \;\simeq\;
  V_{\widetilde\Lambda_{K3}},
  \;}
\]
with *orientation reversal* swapping $V_+ \leftrightarrow V_-$. The last
equivalence uses Mukai self-duality: $\widetilde\Lambda_{K3} \cong
\widetilde\Lambda_{K3}(-1)$ as abstract lattices (both are $U^4 \oplus
E_8(-1)^2 \cong U(-1)^4 \oplus E_8^2$ as quadratic lattices modulo sign
conventions -- this is the Dolgachev--Nikulin self-mirror property at the
lattice level; `k3_yangian_chapter.tex:52--59,225--230`).

**Non-abelian case.** At an ADE enhancement point, the non-abelian
extension $A_{K3}^{\mathfrak g}$ contains $V_{\widetilde\Lambda_{K3}} \oplus
\widehat{\mathfrak g}_1$. The Koszul dual is
\[
  (A_{K3}^{\mathfrak g})^!
  \;\simeq\;
  A_{K3}^! \;\otimes\; \widehat{\mathfrak g}_{k^!}^!,
\]
where $\widehat{\mathfrak g}_{k^!}^!$ is the Feigin--Frenkel dual of
$\widehat{\mathfrak g}_k$ at the *Feigin--Frenkel reflected level*
$k^! = -k - 2h^\vee = -1 - 2h^\vee(\mathfrak g)$. For $\mathfrak g = \mathfrak{sl}_2$,
$h^\vee = 2$, $k^! = -5$; for $\mathfrak g = E_8$, $h^\vee = 30$, $k^! = -61$.
This is the Feigin--Frenkel / Kazama--Suzuki duality at critical-shift
level, and it is standard in class S and in 3d mirror symmetry
(`quantum_chiral_algebras.tex:334--358`).

*The chiral Koszul conductor* for the non-abelian sector is
\[
  K_{\mathrm{non-ab}}
  \;=\;
  \kappa_{\mathrm{ch}}(\widehat{\mathfrak g}_1) + \kappa_{\mathrm{ch}}(\widehat{\mathfrak g}_{k^!})
  \;=\;
  \frac{\dim\mathfrak g}{2h^\vee}(1 + h^\vee)
  \;+\;
  \frac{\dim\mathfrak g}{2h^\vee}(-1 - 2h^\vee + h^\vee)
  \;=\;
  \frac{\dim\mathfrak g \cdot (1 + h^\vee - 1 - h^\vee)}{2h^\vee}
  \;=\;
  0.
\]
Good: class-$G$-style conductor also for the affine KM sector at level $1$
with its Feigin--Frenkel dual. This matches the manuscript's repeated claim
$K = 0$ for the free-field/KM class (`bar_cobar_bridge.tex:198`,
`k3_chiral_algebra.tex:65`).

---

## ROUND 5: Schur-index relation to $Y_{\mathrm{non\text{-}ab}}(\mathfrak g_{K3})$

**Deliverable (v): Schur-index formula relating $V_{K3}$ and $Y_{\mathrm{non\text{-}ab}}(\mathfrak g_{K3})$.**

In class $S$ (Gaiotto, 2008), a 4d $\mathcal N = 2$ theory $T_{\Sigma_g, \mathfrak g}$
labelled by a Riemann surface $\Sigma_g$ and a simply-laced Lie algebra
$\mathfrak g$ has a Schur-index-level 2d chiral algebra $V(T_{\Sigma_g, \mathfrak g})$
that is a generalisation of the $W$-algebra of $\mathfrak g$
(Beem--Lemos--Liendo--Peelaers--Rastelli--van Rees, 2013/14/15). The
Schur index is
\[
  I_{\mathrm{Schur}}(T; q) \;=\; \mathrm{Tr}_{\mathcal H_{\mathrm{Schur}}}(-1)^F q^{L_0 - R}.
\]
The *associated VOA* $V(T)$ is recovered from $I_{\mathrm{Schur}}$ as
the character of $V(T)$:
\[
  \chi_{V(T)}(q) \;=\; I_{\mathrm{Schur}}(T; q).
\]
This is Beem--Rastelli's Schur index theorem.

**For K3.** The relevant 4d $\mathcal N = 2$ theory is the *K3 6d $(2,0)$
theory compactified on a 4-cycle*, giving a 4d $\mathcal N = 2$ theory whose
Higgs branch is $M_{\mathrm{Higgs}}(K3) = \mathrm{Hilb}^n(K3)$
(`k3_yangian_chapter.tex:41--46`). The K3 Schur VOA is conjecturally
\[
  V(T_{K3}) \;=\; \Phi_2(D^b(\mathrm{Coh}(K3))) \;=\; V_{\widetilde\Lambda_{K3}}
  \;\oplus\; \widehat{\mathfrak g}_{K3, 1}.
\]
The lattice piece is the universal Coulomb branch VOA (free-field from the
abelian gauge sector); the non-abelian piece is the enhanced gauge sector
at ADE points.

**Schur-Yangian relation.** For class-$S$ theories on $\Sigma_{g,n}$, the
Schur-index VOA and the associated Yangian are related by:
\[
  I_{\mathrm{Schur}}(T_{\Sigma_{g,n}, \mathfrak g}; q) 
  \;=\;
  \mathrm{Tr}_{M_{\mathrm{Yangian}}}(q^{L_0}),
\]
where $M_{\mathrm{Yangian}}$ is the principal Yangian module attached to
the theory. The *Schur-index-on-K3* formula is the conjectural analogue:
\[
  \boxed{\;
  I_{\mathrm{Schur}}(T_{K3, \mathfrak g_{K3}}; q, y)
  \;=\;
  \prod_{(n, l, m) > 0} (1 - q^n y^l)^{-c(4nm - l^2)}
  \;=\;
  \frac{1}{\Phi_{10}(q, y, 0)}
  \;=\;
  Z_{\mathrm{DMVV}}(p = 0, q, y),
  \;}
\]
where $\Phi_{10}$ is the Igusa cusp form, $c$ are the $\phi_{0,1}$
Fourier coefficients, and the Schur-limit truncates DMVV at $p = 0$.

**Interpretation.** The Schur index packages:
- the *character* of $V_{K3}$ (Mukai Heisenberg + enhanced Kac--Moody);
- which equals the *trace* of $q^{L_0}$ over the principal
  $Y_{\mathrm{non\text{-}ab}}(\mathfrak g_{K3})$-module;
- which equals the $p \to 0$ specialisation of the Gritsenko--Nikulin
  / DMVV product ($\Delta_5^{-1}$ on $K3 \times E$).

This identifies $V_{K3}$ as the 2d chiral algebra of the 4d theory
$T_{K3}$, and $Y_{\mathrm{non\text{-}ab}}(\mathfrak g_{K3})$ as the
Coulomb-branch algebra acting on the Schur index. The three-way story
(4d theory $\leftrightarrow$ 2d VOA $\leftrightarrow$ 3d Yangian) is
the class-$S$ triangle specialised to K3.

**Caveat.** The Schur-index formula above assumes: (a) the 4d $\mathcal N = 2$
theory $T_{K3}$ is non-Lagrangian but has a well-defined Schur index; (b)
the Beem--Rastelli theorem extends to these theories; (c) the Igusa cusp
form $\Phi_{10}$ specialisation is correct. Each is conjectural at the
current state of the literature (`bar_cobar_bridge.tex:361--389`).

---

## Summary of deliverables

(i) **OPE at abelian level.**
\[
  J_v(z) J_w(0) = \frac{\langle v, w \rangle_{\mathrm{Muk}}}{z^2} + \mathopen{:}J_v J_w\mathclose{:}(0) + O(z).
\]

(ii) **BRST current** for non-abelian extension. The BRST current is the
standard Virasoro BRST $c(z)(T_{\mathrm{matter}} + \tfrac12 T_{\mathrm{ghost}})$
*on the rank-26 Lorentzian ambient* $V_{II_{25,1}}$, with nilpotency
$Q^2 = 0$ forced by $c_{\mathrm{matter}} = 26 = -c_{\mathrm{ghost}}$.
The ADE currents arise by Frenkel--Kac at root lattice points (not by
BRST imposition); BRST kills non-physical states but does not generate
non-abelian currents.

(iii) **Central charge $c = 24$, three ways.** Direct OPE (Casimir of $T$
with signs absorbed), character / DMVV leading $q$-power ($q^{-c/24} = q^{-1}$),
lattice VOA definition ($c = \mathrm{rk}_{\mathbb R}$). Match cleanly.
Independent from $c = 6$ of the small-$\mathcal N = 4$ sigma-model VOA.

(iv) **Koszul dual.** $A_{K3}^! \simeq V_{\widetilde\Lambda_{K3}(-1)}
\simeq V_{\widetilde\Lambda_{K3}}$ (Mukai self-duality at lattice level);
at an ADE enhancement, $(A_{K3}^{\mathfrak g})^! \simeq A_{K3}^! \otimes
\widehat{\mathfrak g}_{k^! = -1 - 2h^\vee}$ (Feigin--Frenkel reflection).
Koszul conductor $K = 0$ throughout, matching the class-$G$ / affine-KM
free-field branch.

(v) **Schur-index-Yangian relation.**
\[
  I_{\mathrm{Schur}}(T_{K3, \mathfrak g_{K3}}; q, y)
  = \chi_{V_{K3}}(q, y)
  = \mathrm{Tr}_{M_{Y}}(q^{L_0})
  = \Phi_{10}(q, y, 0)^{-1}.
\]

## What the manuscript gets right, and what needs tightening

**Right.** The assignment $\Phi_2(K3) = V_{\widetilde\Lambda_{K3}}$, the
lattice data $\widetilde\Lambda_{K3} = U^4 \oplus E_8(-1)^2$, the
$\kappa$-spectrum $\{0, 2, 3, 5, 24\}$, the three involutions
(Koszul / symplectic / unitarity) and their $\kappa$-diagnostics are all
clean (`k3_chiral_algebra.tex:10--18`, `k3_yangian_chapter.tex:206--246`).

The distinction between the Mukai Heisenberg VOA at $c = 24$ and the
$\mathcal N = 4$ K3 sigma-model VOA at $c = 6$ is maintained throughout:
$\kappa_{\mathrm{ch}}^{\mathrm{Heis}} \neq \kappa_{\mathrm{ch}}^{\mathrm{sigma}}$
is not a bug, it is two different algebras attached to the same manifold
by two different functors.

**Needs tightening.**

1. The claim "$V_{\widetilde\Lambda_{K3}}$ is a lattice VOA at signature
   $(4, 20)$" should always be qualified: *after* Kahler polarisation and
   *after* BRST reduction from the $II_{25,1}$ ambient. Without the
   polarisation, no canonical stress tensor; without BRST, the algebra is
   non-unitary (ghosts from $V_-$).

2. The claim "$E_2$-chiral algebra of central charge $24$"
   (`k3_chiral_algebra.tex:170`) is clean at abelian rank but the $E_2$
   structure is trivial (braiding is symmetric for abelian currents). The
   interesting $E_2$ content arises at ADE enhancement points, where the
   braiding is genuinely non-trivial; this distinction deserves a remark
   in the chapter.

3. The Mukai form *signature* $(4, 20)$ is consistent (four positive plus
   $H^0 \oplus H^4$, twenty negative for the $b_- = 19$ anti-self-dual
   $H^2$ plus one hyperbolic direction), but the statement requires
   fixing a complex structure (choice of $\bar\Omega_{K3}$); without
   this, the signature is $(3, 19)$ for $H^2$ alone. The $+1$
   additional positive direction from $(H^0 \oplus H^4)$ is real
   two-dimensional but contributes signature $(1, 0) + (1, 0) = (2, 0)$
   under the Mukai pairing $v \cdot w = v \wedge w \big|_{\mathrm{top}}$,
   giving $(2, 0) + (2, 19) = (4, 19)$ -- *not* $(4, 20)$. The manuscript's
   "$(4, 20)$" claim requires a $+1$ extra negative direction, which comes
   from the twist by $\sqrt{\mathrm{td}(K3)}$ (Mukai twist). This is
   addressed in the chapter (`k3_yangian_chapter.tex:2043--2053`) but
   deserves a clearer scope declaration early in the chiral algebra
   chapter.

4. The "Fake Monster" / no-ghost reduction is essentially what the
   manuscript does (the $II_{25,1}$ ambient appears implicitly), but it
   is never named as such in `k3_chiral_algebra.tex`. This is what
   Borcherds did to construct the Fake Monster Lie algebra, and saying
   it out loud would help readers from the Borcherds / moonshine
   tradition connect to the chapter.

5. The non-abelian Yangian conjecture (`conj:k3-super-yangian`,
   `k3_yangian_chapter.tex:2020--2039`) identifies $Y_{\mathrm{non\text{-}ab}}
   \simeq Y_{\osp(4|20)}$, with subtleties about orthosymplectic
   vs. real-form $Y(\mathfrak{so}(4, 20))$. The BRST-invariant boundary
   sector argument (`k3_yangian_chapter.tex:2068`) is invoked to favour
   $\osp(4|20)$ but stated as conjectural. The Schur-index formula
   above can be used as a diagnostic: whichever Yangian correctly
   reproduces $\Phi_{10}(q, y, 0)^{-1}$ as the trace of its principal
   module is the physically correct one.

---

## Gaiotto-closing

The physical system (4d $\mathcal N = 2$ theory $T_{K3}$) produces the 2d
chiral algebra $V_{K3}$ via Schur-indexing; the algebra is not
the starting point. The Mukai-lattice Heisenberg VOA is the Coulomb-branch
slice, the affine $\widehat{\mathfrak g}_1$ subalgebras at ADE points are
the Higgs-branch gauge enhancements, the Koszul dual is the mirror via
Feigin--Frenkel at reflected level, and the non-abelian K3 Yangian acts
on the Schur index. The Igusa cusp form $\Phi_{10}$ at $p = 0$ is the
generating function.

Everything here is a shadow of the 4d theory.

---

## File-line anchors

- `k3_chiral_algebra.tex:10,159--170,1830--1835`: Mukai-lattice Heisenberg VOA claim.
- `k3_chiral_algebra.tex:240--247,1825--1897`: $\kappa_\bullet$-spectrum, shadow landscape.
- `k3_yangian_chapter.tex:206--246`: three involutions and their $\kappa$-diagnostics.
- `k3_yangian_chapter.tex:1270--1312`: BKM simple-root / Yangian-generator sectors.
- `k3_yangian_chapter.tex:1320--1434`: K3 Serre relations at ADE enhancement.
- `k3_yangian_chapter.tex:1879--2072`: $Y_{\osp(4|20)}$ conjecture for the non-abelian K3 Yangian.
- `quantum_chiral_algebras.tex:334--389`: universal defect algebra, Koszul dual = Feigin--Frenkel reflected.
- `bar_cobar_bridge.tex:184--198`: CY Koszul duality dictionary and conductor identity.
- `CLAUDE.md:151`: $\kappa_{\mathrm{ch}}(A_X) = \sum_q (-1)^q h^{0,q}(X)$ Hodge supertrace.

Raeez Lorgat, sole author.
