# Agent A6: K3 x E Hall-Borcherds closure and holography fence

## Scope

Task issues: 7 and 8.

Objects:

- `X = K3 x E`.
- `p_E: X -> E`.
- `Sigma_2 = p_E^{-1}(e_0) ~= K3`.
- `C = E`.
- Primitive Borcherds denominator: `Delta_5`.
- Dyonic / reduced-DT square: `Phi_10 = const * Delta_5^2`.

Question attacked: can the Hall-Borcherds hypotheses `HB1`--`HB5` be proved now, from the existing manuscript sources, as one clean algebra-level theorem strong enough to support holography/QG consequences?

Verdict: no.  The arithmetic and character side is theorem-grade.  The algebra-level Hall-Borcherds closure is still conditional on the same missing comparison data as the hCS-to-Hall bridge.  The correct repaired output is a conditional theorem package plus a physics fence.  I made three tiny normalization patches where the manuscript still contradicted the primitive/square distinction.

## Attack

### A. Primitive denominator versus square

The primitive BKM object is `g_{Delta_5}`.  Its denominator is `Delta_5`, with

```tex
c_Delta(0)=10,\qquad
\kappa_{\mathrm{BKM}}(\mathfrak g_{\Delta_5})
=\operatorname{wt}(\Delta_5)=c_Delta(0)/2=5.
```

The full K3 elliptic genus is `2 phi_{0,1}`.  Its Borcherds product is the dyonic square

```tex
\Phi_{10}=const\cdot\Delta_5^2,\qquad \operatorname{wt}(\Phi_{10})=20/2=10.
```

Surviving false formula attacked:

```tex
\kappa_{\mathrm{BKM}}=\operatorname{wt}(\Phi_{10})/2=5.
```

This is not the clean convention.  It accidentally gives the right number by applying a half-square operation to the wrong object.  The repaired statement names the primitive denominator first and records the square separately.

Local anchors:

- `chapters/examples/k3e_bkm_chapter.tex:470-472`: chapter convention separating `Delta_5` and `Phi_10`.
- `chapters/examples/k3e_bkm_chapter.tex:533-587`: three-route proof of `Z_red = pqt/Phi_10 = C/Delta_5^2`.
- `chapters/theory/cy_to_chiral.tex:765-774`: conditional K3-fibre specialisation and `kappa_BKM(Delta_5)=5`.
- `main.tex:1373-1375`: patched to primitive `Delta_5` denominator and dyonic square `Phi_10=Delta_5^2`.
- `chapters/examples/k3e_cy3_programme.tex:1057-1062`, `:2097-2099`, `:2210-2218`: patched to primitive `Delta_5` weight.
- `chapters/connections/modular_koszul_bridge.tex:336-342`, `:853-856`: patched to replace `wt(Phi_10)/2` and the wrong `phi_{-2,1}` input by the primitive/full-genus distinction.

### B. The false additive formula

The expression

```tex
\kappa_{\mathrm{BKM}}
\stackrel{?}{=}
\kappa_{\mathrm{ch}}^{\mathrm{Heis}}+\chi(\mathcal O_{\mathrm{fibre}})
```

does not become a theorem after correcting the fibre to `K3`.  It gives the accidental `N=1` equality

```tex
5=3+2
```

and fails to explain the CHL ladder

```tex
\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2=(5,4,3,2,1)
\quad (N=1,2,3,4,6).
```

The hidden structure is not additivity.  It is the Borcherds weight theorem applied to the chosen Jacobi input.

Local patch:

- `chapters/theory/cy_to_chiral.tex:799-803` now states that the K3-fibre equality is accidental at `N=1`, and that the uniform identity is `c_N(0)/2`.

### C. Algebra-level closure is not character-level closure

The following data are theorem-grade or externally theorem-grade:

- Oberdieck-Pandharipande / Oberdieck-Pixton reduced DT character at `N=1`.
- Gritsenko-Nikulin / Borcherds product for `Delta_5`.
- The square relation `Phi_10 = const * Delta_5^2`.
- The CHL weight table `c_N(0)=(10,8,6,4,2)`, `kappa_BKM=(5,4,3,2,1)`.
- Genus-2 BPS index arithmetic and Rademacher asymptotics for `1/Phi_10`.

These do not construct the algebra-level comparison

```tex
\SpCh_{K3,E}(\PhiFA_3(\mathrm{Perf}(K3\times E)))
\simeq U_{\mathrm{ch}}(\mathfrak g_{\Delta_5})
```

without the Hall/hCS comparison, orientation, completion, and specialization coherences.

Most serious remaining overclaim candidate:

- `chapters/examples/k3e_bkm_chapter.tex:11935-11948` states an explicit Stage-2 decomposition as `ClaimStatusProvedHere`.  The Heisenberg/Mukai factor has external character support; the non-abelian BPS factor still depends on the Hall-Borcherds comparison.  The healed theorem should route this statement through the conditional theorem `thm:g-delta5-is-sp-k3`, or split it into a proved Heisenberg character statement plus a conditional BPS/Borcherds algebra statement.

I did not patch this larger theorem-status issue because it is not a tiny normalization repair.

## HB1--HB5 audit

`HB1`: oriented CY3 hCS-to-Hall comparison for `Perf(K3 x E)`.

Status: open.  The obstruction package in `chapters/theory/cy3_chain_level_bridge.tex:650-675` and `:677-725` names the missing orientation, shift, Tate, completion, Thom-Sebastiani, and factorisation obstructions.  Character agreement does not construct the map.

`HB2`: compatibility with K3-fibre specialization and pushforward to `E`.

Status: conditional.  `chapters/theory/cy_to_chiral.tex:765-789` states the right K3-fibre theorem conditionally.  The witnessed specialisation datum repairs the typing, but arbitrary pushforward/envelope commutation is not proved beyond witnessed loci.

`HB3`: Hall pairing and completion giving the Hall-Drinfeld double.

Status: partially external on the Hall side, not transported.  Kontsevich-Soibelman / Davison-Meinhardt supply Hall-side structures; the comparison with `PhiFA_3` and the completion compatible with hCS observables remain assumptions.

`HB4`: Hall denominator/root-multiplicity comparison with `Delta_5`.

Status: arithmetic theorem, algebra comparison conditional.  The equality of product exponents and partition functions is established in the automorphic/enumerative lane.  It does not by itself prove that the completed Hall double is the same algebra as the primitive `g_{Delta_5}` envelope produced by Stage 2.

`HB5`: coproduct, associator, and `R`-matrix compatibility.

Status: conditional.  `chapters/theory/cy_to_chiral.tex:806-860` correctly assumes coproduct/associator/`R` transport.  `chapters/theory/cy_to_chiral.tex:868-906` correctly isolates the associator scalar: arithmetic fixes `5` only after the transport line is built and nonzero.

Conclusion: `HB1`--`HB5` cannot be proved as a single clean theorem from existing sources.  They form the exact hypotheses of the clean conditional theorem.

## Repaired conditional theorem

Let

```tex
X=K3\times E,\qquad
\Sigma_2=p_E^{-1}(e_0)\simeq K3,\qquad
C=E.
```

Let `phi_Delta=phi_{0,1}^{EZ}` be normalized by

```tex
phi_Delta(\tau,z)=y^{-1}+10+y+O(q),
```

and let `Z_K3=2 phi_Delta`.  Then the arithmetic lane proves

```tex
Bor(phi_Delta)=\Delta_5,\qquad
\operatorname{wt}(\Delta_5)=10/2=5,
```

and

```tex
Bor(Z_K3)=\Phi_{10}=const\cdot\Delta_5^2,\qquad
\operatorname{wt}(\Phi_{10})=20/2=10.
```

Assume `HB1`--`HB4`.  Then the K3-fibre Stage-2 specialization has comparison target

```tex
\SpCh_{K3,E}(\PhiFA_3(\mathrm{Perf}(K3\times E)))
\simeq U_{\mathrm{ch}}(\mathfrak g_{\Delta_5})
```

as an `E_1` chiral algebra on `E`, with primitive denominator invariant

```tex
\kappa_{\mathrm{BKM}}(\mathfrak g_{\Delta_5})=5.
```

Assume additionally `HB5`.  Then this promotes to the chiral bialgebra / Hall-Drinfeld-double statement with the transported coproduct, Siegel-Borcherds associator, and elliptic dynamical `R`-matrix.

The reduced DT / MSW / DVV character is the dyonic square:

```tex
Z_{\mathrm{red}}(K3\times E)=C'\Phi_{10}^{-1}=C\Delta_5^{-2}.
```

The primitive chiral half is controlled by `Delta_5^{-1}`; the physical genus-2 BPS trace is controlled by `Phi_10^{-1}`.  These are different normalizations of adjacent objects, not competing values of one invariant.

## Holography / QG fence

The theorem-grade mathematical lane is:

```tex
Delta_5, Phi_10, c_N(0)/2, 1/Phi_10 Fourier coefficients,
Rademacher asymptotics.
```

The conditional physical lane is:

```tex
compact twisted M-theory reduction
  + all-loop hCS exponentiation
  + oriented hCS-to-Hall comparison
  + boundary/Hall trace comparison
  => boundary partition function C' Phi_10^{-1}
```

Allowed statement:

If the compact hCS/Hall and boundary comparison maps exist with the stated orientation and trace coherences, then the boundary/QG partition function is compatible with

```tex
Z_{\mathrm{boundary}}=C'\Phi_{10}^{-1}=C\Delta_5^{-2},
```

and its primitive algebraic half has `kappa_BKM=5`.

Forbidden statement:

The arithmetic identity `Phi_10=Delta_5^2` or the one-loop `2+3=5` weight witness proves compact holography, quantum gravity, or the Hall-Drinfeld double construction.

Local fence anchors:

- `chapters/examples/k3e_bkm_chapter.tex:11750-11807`: genus-2 BPS / MSW / Harvey-Moore statement.
- `chapters/examples/k3e_bkm_chapter.tex:11825-11829`: good epistemic fence separating modular identities from AdS/CFT and M5 reductions.
- `chapters/examples/k3e_bkm_chapter.tex:11831-11855`: primary literature list for the physics/arithmetic bridge.
- `chapters/connections/cy_holographic_datum_master.tex:424-461`: `Delta_5` as Borcherds theorem and one-loop physics witness, not all-orders proof.

## Claim-status recommendations

- Keep `thm:g-delta5-is-sp-k3` conditional.
- Keep `thm:g-delta5-sp-k3-bialgebra` conditional.
- Keep the associator-scalar statement conditional on nonzero transport of the CY3 formality cocycle to the Hall-Borcherds cohomology line.
- Split `thm:plat-Sp-K3E` into a proved Heisenberg/Mukai character statement plus a conditional non-abelian BPS/Borcherds algebra comparison.
- Holography/QG claims may be theorem-grade as arithmetic statements about `1/Phi_10` coefficients and asymptotics; as consequences of `Phi_3` or hCS/Hall, they remain conditional on the algebra maps.

## Commands and verification

Read/search commands included `rg`, `nl -ba`, and targeted `git status` over:

- `chapters/theory/cy_to_chiral.tex`
- `chapters/theory/cy3_chain_level_bridge.tex`
- `chapters/examples/k3e_bkm_chapter.tex`
- `chapters/examples/k3e_cy3_programme.tex`
- `chapters/connections/cy_holographic_datum_master.tex`
- `main.tex`
- previous A6 report under `notes/adversarial_swarm_20260424_frontier_resolution/`

Executable checks:

```bash
python3 -m compute.lib.borcherds_denominator_phi10_engine
```

Result: all checks passed; pointwise `|ratio|-1` errors `1.62e-13`, `2.96e-14`, `2.57e-13`; `kappa_BKM=5`, `wt(BP)=5`, `wt(chi_10)=10`.

```bash
python3 -m pytest \
  compute/tests/test_k3_yangian_borcherds_weight_theta_refinement.py \
  compute/tests/test_borcherds_denominator_phi10_engine.py \
  compute/tests/test_modular_cy_characteristic.py \
  compute/tests/test_twisted_holography_k3e.py \
  -q
```

Result: `334 passed in 34.97s`.

```bash
perl -ne '$b++ if /\\begin\{/; $e++ if /\\end\{/; END {print "main begin=$b end=$e\n"}' main.tex
perl -ne '$b++ if /\\begin\{/; $e++ if /\\end\{/; END {print "cy_to_chiral begin=$b end=$e\n"}' chapters/theory/cy_to_chiral.tex
perl -ne '$b++ if /\\begin\{/; $e++ if /\\end\{/; END {print "k3e_cy3 begin=$b end=$e\n"}' chapters/examples/k3e_cy3_programme.tex
perl -ne '$b++ if /\\begin\{/; $e++ if /\\end\{/; END {print "modular_koszul_bridge begin=$b end=$e\n"}' chapters/connections/modular_koszul_bridge.tex
```

Results: `main begin=19 end=19`, `cy_to_chiral begin=703 end=703`, `k3e_cy3 begin=345 end=345`, `modular_koszul_bridge begin=151 end=151`.

Import-path note: direct file execution of `compute/lib/borcherds_denominator_phi10_engine.py` and `compute/lib/modular_cy_characteristic.py` failed under the script path because those entry points expect module imports from the repo root.  Running with `python3 -m ...` from the repo root succeeds.

No `make fast` build was run.

## Files changed

- `notes/adversarial_swarm_20260424_total_resolution/agent_A6_k3e_hb_holography.md` -- this report.
- `main.tex` -- tiny primitive/square denominator patch.
- `chapters/theory/cy_to_chiral.tex` -- tiny false-additivity/fibre patch.
- `chapters/examples/k3e_cy3_programme.tex` -- tiny `Delta_5` versus `Phi_10` normalization patch.
- `chapters/connections/modular_koszul_bridge.tex` -- tiny `Delta_5` versus `Phi_10` normalization patch.
