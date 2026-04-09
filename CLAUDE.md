# CLAUDE.md -- Volume III: CY Categories, Quantum Groups, and BPS Algebras

**Canonical reference for all shared content (Beilinson Principle, AP tables, RS safeguards, Symphonic Standard, verification mandate, session protocol, audit/rectification loops, LaTeX/git rules): ~/chiral-bar-cobar/CLAUDE.md. This file contains ONLY Vol III-specific material.**

## Identity

Volume III constructs the geometric source: the functor Phi: CY_d-Cat -> E_2-ChirAlg that provides input data for the Vols I-II bar-cobar machine. Flow: CY category -> chiral algebra -> bar complex -> modular characteristic -> partition function.

~206pp, this repo, 17,199 tests. Clean build. Five parts: I (CY Engine), II (CY Characteristic Datum), III (CY Landscape), IV (Seven Faces of r_CY(z)), V (CY Frontier).

**12 skeletal stub chapters** (<50 lines, no theorems): cy_categories, cyclic_ainf, hochschild_calculus, quantum_groups_foundations, braided_factorization, drinfeld_center, fukaya_categories, derived_categories_cy, matrix_factorizations, quantum_group_reps, modular_koszul_bridge, geometric_langlands. Each must be developed or commented out (AP114).

## Main Theorems (Targets)

| Theorem | Status | Notes |
|---------|--------|-------|
| **CY-A** (CY-to-chiral functor) | d=2 PROVED; d=3 PROGRAMME | d=3 conditional on chain-level S^3-framing |
| **CY-B** (E_2-chiral Koszul duality) | PROGRAMME | Depends on CY-A |
| **CY-C** (Quantum group realization) | CONJECTURAL | C(g,q) not constructed. Uses \begin{conjecture}. |
| **CY-D** (Modular CY characteristic) | PROGRAMME | kappa well-defined only when A_C exists |

## The kappa-Spectrum (AP113, CRITICAL)

Bare "kappa" is FORBIDDEN in Vol III. A single CY manifold can give rise to multiple chiral algebraizations, each with its own kappa. ALWAYS subscript:

| Subscript | Meaning | K3 x E value |
|-----------|---------|--------------|
| kappa_ch | From chiral algebra A_C via Phi | 3 |
| kappa_BKM | From Borcherds-Kac-Moody algebra | 5 (weight of Delta_5) |
| kappa_cat | From categorical/holomorphic Euler char | 2 = chi(O_{K3}) |
| kappa_fiber | From lattice/fiber structure | 24 (lattice rank) |

The kappa(K3 x E) = 3 vs 5 contradiction arose from conflating kappa_ch and kappa_BKM. Full spectrum Spec_kappa(K3 x E) = {2,3,5,24}.

## E_1/E_2 Chiral Hierarchy

E_1-chiral (Vol II): associative factorization on C x R. Monoidal rep categories. E_2-chiral (this volume): braided factorization on C x C. Braided monoidal rep categories: habitat of quantum groups. E_1 -> E_2 via Dunn additivity. For d=2: S^2-framing of HH_*(C) gives E_2. For d=3: holomorphic CS breaks E_2 to E_1; recover E_2 via Drinfeld center Z(Rep^{E_1}(A)) = Rep^{E_2}(Z^der_ch(A)).

The Drinfeld center is the categorified averaging map av: E_1-Cat -> E_2-Cat. Quantum groups, Yangians, braided tensor categories are natively E_1. E_2 structure is derived.

## CY-Specific Anti-Patterns (AP-CY1 through AP-CY8)

| AP-CY | Name | Rule |
|-------|------|------|
| 1 | CY dimension d != complex dimension n | Fuk(X) is CY_n, D^b(Coh(X)) is CY_n. Do not confuse with real dimension 2n. |
| 2 | CY trace is in HC^-_d(C) | NOT just HH_d -> k. Negative cyclic refinement essential for S^d-framing. |
| 3 | E_2 != commutative | E_2 braiding is NOT symmetric in general. E_2 -> E_inf loses quantum group structure. |
| 4 | Drinfeld center != derived center | Z(C) (monoidal category) vs Z^der_ch(A) (chiral). Agree under specific hypotheses. State which. |
| 5 | Kazhdan-Lusztig requires root of unity | At generic q, Rep_q(g) is semisimple. Interesting structure at roots of unity. |
| 6 | A_X for CY3 does NOT exist | It is the content of the d=3 programme. NEVER write as if defined. |
| 7 | CoHA != E_1-chiral algebra | CoHA is associative. Calling it "E_1-sector of G(X)" assumes G(X) exists. G(X) is AP43 (undefined). |
| 8 | Borcherds denominator != bar Euler product | Identification requires CY-to-chiral functor to exist. For K3 x E (d=3): observation, not theorem. |

## Dependencies on Vols I-II

| Volume | Provides | Used here |
|--------|----------|-----------|
| I | Bar-cobar machine, Theta_A, kappa, five theorems, G/L/C/M | CY bar complex, modular trace, shadow depth |
| II | SC^{ch,top}, PVA descent, DK bridge, E_1 sector, H(T) | E_1 chiral theory, braided structure, bulk-boundary |

## Build

```
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast    # Vol III
cd ~/chiral-bar-cobar && make fast                                # Vol I
cd ~/chiral-bar-cobar-vol2 && make                                # Vol II
make test                                                         # Vol III tests
```

## Session Entry (Vol III-specific additions)

1. Read ~/chiral-bar-cobar/CLAUDE.md first (canonical reference)
2. Then read this file (CY-specific pitfalls, kappa-spectrum, AP-CY1-8)
3. Check AP113 compliance: bare kappa -> subscripted kappa_{ch,BKM,cat,fiber}
4. Check AP114: do not cite theorems from the 12 stub chapters
5. CY-A at d=2 PROVED. CY-A at d=3 PROGRAMME. Scope every CY-A claim by dimension.
6. CY-C is CONJECTURE. Never \begin{theorem} for CY-C (AP40).

## Git

All commits authored by Raeez Lorgat. NEVER credit an LLM. git stash FORBIDDEN.
