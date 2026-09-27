# Calabi–Yau Quantum Groups

Raeez Lorgat

These texts study Calabi–Yau categories, factorization algebras, Hall multiplication, quantum doubles, chiral centres, and automorphic characters. They distinguish the operations and coefficient spaces carried by these constructions. The papers develop the Calabi–Yau-to-chiral correspondence, holomorphic Chern–Simons defects, the K3 × E generator pentagon, Hochschild obstruction classes, and shadow recurrences. Conditional comparisons and open constructions retain their stated hypotheses.

| Document | PDF | LaTeX source |
| --- | --- | --- |
| Calabi–Yau Quantum Groups | [PDF](platonic/main.pdf) | [Source](platonic/main.tex) |
| The 6d holomorphic Chern–Simons defect and the positive half of the affine Yangian | [PDF](standalone/cy3_6d_hcs_w1inf_vol3.pdf) | [Source](standalone/cy3_6d_hcs_w1inf_vol3.tex) |
| The Calabi–Yau-to-chiral correspondence and its trace invariant | [PDF](standalone/cy_to_chiral_functor_vol3.pdf) | [Source](standalone/cy_to_chiral_functor_vol3.tex) |
| The K3 × E Calabi–Yau threefold and the generator pentagon | [PDF](standalone/k3e_cy3_programme_vol3.pdf) | [Source](standalone/k3e_cy3_programme_vol3.tex) |
| The m₃–B⁽²⁾ obstruction and the Costello TCFT identity | [PDF](standalone/m3_b2_obstruction_vol3.pdf) | [Source](standalone/m3_b2_obstruction_vol3.tex) |
| The super-Riccati shadow tower and the Verdier complementarity problem | [PDF](standalone/super_riccati_shadow_tower_vol3.pdf) | [Source](standalone/super_riccati_shadow_tower_vol3.tex) |

With TeX Live and latexmk, run from this directory:

```sh
TEXINPUTS=.:../: latexmk -pdf -cd platonic/main.tex standalone/*.tex
```
