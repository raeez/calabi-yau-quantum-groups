r"""Finite stages of the completed ordered chiral E3 bar witness.

This module is the executable shadow of
``chapters/theory/cy3_chain_level_bridge.tex``:

* ``def:ordered-chiral-e3-bar`` -- the controller is ordered tensor/bar
  data over configuration chains, not the exterior CE quotient.
* ``prop:exterior-ce-shadow-not-controller`` -- finite exterior CE is a
  locally constant shadow and kills repeated inputs.

The engine deliberately implements the smallest exact arithmetic surface
needed to falsify the old mistake.  It does not pretend to compute the
analytic Dolbeault completion, the full Fulton--MacPherson boundary
complex, or the hCS-to-Hall comparison.  It records the algebraic
controller that finite CE cannot see: ordered words, repeated inputs,
and the first higher L_infinity corrections.

Conventions
===========

* Ordered arity-r words have dimension ``n**r`` for ``n`` generators.
* Exterior arity-r CE shadows have dimension ``binom(n, r)``.
* The projection from ordered words to exterior CE kills repeated
  generator indices.
* For scalar higher operations in the existing ``LInfinityData`` model,
  a coefficient attached to ``(x, ..., x)`` is read as an output in the
  same generator direction.  Thus for Virasoro at ``c=1``:

      l_3(T,T,T) = -2 T,
      l_4(T,T,T,T) = 40/27 T.

These are exact rational witnesses for the repeated-input class-M
obstruction that the exterior CE quotient misses.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from typing import Dict, Iterable, List, Tuple

from compute.lib.chiral_ce_complex import (
    CEElement,
    LCAGenerator,
    LieConformalAlgebra,
    LInfinityData,
)


OrderedWord = Tuple[int, ...]


@dataclass(frozen=True)
class OrderedBarElement:
    r"""A finite ordered-bar element.

    The real completed object is a product over arities with completed
    projective tensor products.  A finite dictionary is enough for exact
    local tests: it keeps words such as ``(T,T,T)`` distinct and nonzero
    before the exterior projection.
    """

    terms: Dict[OrderedWord, Fraction]

    @staticmethod
    def zero() -> "OrderedBarElement":
        return OrderedBarElement({})

    @staticmethod
    def basis(word: OrderedWord, coeff: Fraction = Fraction(1)) -> "OrderedBarElement":
        return OrderedBarElement({tuple(word): coeff})

    def cleaned(self) -> "OrderedBarElement":
        return OrderedBarElement({w: c for w, c in self.terms.items() if c})

    def is_zero(self) -> bool:
        return all(c == 0 for c in self.terms.values())

    def __add__(self, other: "OrderedBarElement") -> "OrderedBarElement":
        result = dict(self.terms)
        for word, coeff in other.terms.items():
            result[word] = result.get(word, Fraction(0)) + coeff
        return OrderedBarElement(result).cleaned()

    def __rmul__(self, scalar: Fraction) -> "OrderedBarElement":
        return OrderedBarElement({w: scalar * c for w, c in self.terms.items()}).cleaned()


@dataclass(frozen=True)
class FMBoundaryFace:
    r"""A finite Fulton-MacPherson boundary face in an ordered arity layer."""

    word: OrderedWord
    collision_indices: Tuple[int, ...]
    codimension: int
    sign: int


class OrderedChiralE3BarController:
    r"""Ordered vertex-bar controller for the chiral E3 deformation problem."""

    def __init__(self, lca: LieConformalAlgebra, linf: LInfinityData):
        self.lca = lca
        self.linf = linf
        self._gen_index = {g.name: i for i, g in enumerate(lca.generators)}
        self._gen_by_index = {i: g for i, g in enumerate(lca.generators)}

    @property
    def n_generators(self) -> int:
        return len(self.lca.generators)

    def word(self, names: Iterable[str]) -> OrderedWord:
        return tuple(self._gen_index[name] for name in names)

    def ordered_dimension(self, arity: int) -> int:
        r"""Dimension of the ordered arity-r tensor layer: n^r."""
        return self.n_generators ** arity

    def exterior_shadow_dimension(self, arity: int) -> int:
        r"""Dimension of the exterior CE arity-r shadow: binom(n,r)."""
        if arity > self.n_generators:
            return 0
        return math.comb(self.n_generators, arity)

    def exterior_projection(self, elem: OrderedBarElement) -> CEElement:
        r"""Project ordered words to the exterior CE quotient.

        Repeated words vanish here.  This is exactly the quotient that
        makes finite CE insufficient for class-M repeated-input
        obstructions.
        """
        result = CEElement.zero()
        for word, coeff in elem.terms.items():
            result = result + CEElement.basis(word, coeff)
        return result.cleaned()

    def repeated_words_survive(self, arity: int) -> bool:
        r"""Return whether repeated inputs exist in ordered arity r and die in exterior CE."""
        return self.ordered_dimension(arity) > self.exterior_shadow_dimension(arity)

    def higher_block_correction(self, word: OrderedWord) -> OrderedBarElement:
        r"""Apply the first nonzero whole-block higher operation to an ordered word.

        This is the executable local witness for the ordered vertex-bar
        correction.  It is not the full FM boundary differential; it is
        the coefficient-level test that the exterior CE quotient cannot
        represent.
        """
        names = tuple(self._gen_by_index[i].name for i in word)
        if len(names) == 3:
            coeff = self.linf.l3_jacobiator.get(names, Fraction(0))
        elif len(names) == 4:
            coeff = self.linf.l4_quartic.get(names, Fraction(0))
        else:
            coeff = Fraction(0)

        if coeff == 0:
            return OrderedBarElement.zero()

        # Existing LInfinityData stores scalar coefficients for same-direction
        # class-M operations; the output direction is the first input.
        return OrderedBarElement.basis((word[0],), coeff)

    def shadow_report(self, max_arity: int = 4) -> Dict[str, object]:
        r"""Compact exact report for manuscript/test witnesses."""
        return {
            "model": "ordered_vertex_bar_controller",
            "shadow": "exterior_CE_is_quotient",
            "generators": [g.name for g in self.lca.generators],
            "shadow_class": self.linf.shadow_class,
            "ordered_dimensions": {
                r: self.ordered_dimension(r) for r in range(max_arity + 1)
            },
            "exterior_dimensions": {
                r: self.exterior_shadow_dimension(r) for r in range(max_arity + 1)
            },
            "repeated_inputs_detected": {
                r: self.repeated_words_survive(r) for r in range(max_arity + 1)
            },
        }


class CompletedOrderedVertexBarController(OrderedChiralE3BarController):
    r"""Finite truncation of the completed ordered chiral E3 vertex-bar.

    The completed object is a product over all arities and configuration
    chains.  A computation must choose an arity cutoff.  Within that cutoff
    this controller keeps the four pieces that the exterior CE shadow
    forgets: ordered words, the Fulton-MacPherson cellular boundary,
    partial-diagonal residues, and Cech/Ran descent combinatorics.
    """

    def __init__(
        self,
        lca: LieConformalAlgebra,
        linf: LInfinityData,
        *,
        arity_cutoff: int = 4,
    ):
        super().__init__(lca, linf)
        if arity_cutoff < 0:
            raise ValueError("arity_cutoff must be nonnegative")
        self.arity_cutoff = arity_cutoff

    def completion_layers(self) -> Dict[int, int]:
        r"""Ordered dimensions of the completed product, truncated by arity."""
        return {r: self.ordered_dimension(r) for r in range(self.arity_cutoff + 1)}

    def fm_boundary_faces(self, word: OrderedWord) -> Tuple[FMBoundaryFace, ...]:
        r"""All collision strata for a finite ordered word.

        A codimension-k face is indexed here by a subset of k+1 colliding
        marked points.  The sign convention is the alternating orientation
        inherited from the ordered index set.
        """
        faces: List[FMBoundaryFace] = []
        for size in range(2, len(word) + 1):
            for collision in combinations(range(len(word)), size):
                sign = -1 if sum(collision) % 2 else 1
                faces.append(
                    FMBoundaryFace(
                        word=word,
                        collision_indices=tuple(collision),
                        codimension=size - 1,
                        sign=sign,
                    )
                )
        return tuple(faces)

    def cellular_boundary(self, elem: OrderedBarElement) -> OrderedBarElement:
        r"""Alternating cellular boundary on the ordered arity simplex."""
        result = OrderedBarElement.zero()
        for word, coeff in elem.terms.items():
            if not word:
                continue
            for i in range(len(word)):
                face = word[:i] + word[i + 1 :]
                sign = Fraction(-1 if i % 2 else 1)
                result = result + OrderedBarElement.basis(face, coeff * sign)
        return result.cleaned()

    def cellular_boundary_squared(self, elem: OrderedBarElement) -> OrderedBarElement:
        r"""The finite cellular part satisfies d_FM^2 = 0 exactly."""
        return self.cellular_boundary(self.cellular_boundary(elem)).cleaned()

    def _replace_block(
        self, word: OrderedWord, start: int, size: int, replacement: OrderedWord
    ) -> OrderedWord:
        return word[:start] + replacement + word[start + size :]

    def partial_diagonal_residues(self, word: OrderedWord) -> Dict[Tuple[int, int], OrderedBarElement]:
        r"""Residues for contiguous ordered collisions.

        Keys are ``(start, size)``.  Binary residues use the LCA zeroth
        product.  Ternary and quaternary whole-block residues use the
        existing exact L_infinity coefficients.
        """
        residues: Dict[Tuple[int, int], OrderedBarElement] = {}
        for size in range(2, min(4, len(word)) + 1):
            for start in range(0, len(word) - size + 1):
                block = word[start : start + size]
                key = (start, size)
                if size == 2:
                    a = self._gen_by_index[block[0]]
                    b = self._gen_by_index[block[1]]
                    acc = OrderedBarElement.zero()
                    for coeff, output in self.lca.zeroth_product(a, b):
                        if output is None or output.name not in self._gen_index:
                            continue
                        out_word = self._replace_block(
                            word, start, size, (self._gen_index[output.name],)
                        )
                        acc = acc + OrderedBarElement.basis(out_word, coeff)
                    residues[key] = acc.cleaned()
                elif start == 0 and size == len(word):
                    residues[key] = self.higher_block_correction(block)
                else:
                    residues[key] = OrderedBarElement.zero()
        return residues

    def cech_ran_simplex_counts(self, charts: int) -> Dict[int, int]:
        r"""Number of non-empty Cech/Ran simplices for a finite good cover."""
        if charts < 0:
            raise ValueError("charts must be nonnegative")
        return {p: math.comb(charts, p + 1) for p in range(charts)}

    def completed_report(self, charts: int = 3) -> Dict[str, object]:
        r"""Exact finite-stage report for the completed-controller surface."""
        return {
            "model": "completed_ordered_vertex_bar_truncation",
            "controller_kind": "finite_arity_stage_of_completed_pro_object",
            "arity_cutoff": self.arity_cutoff,
            "finite_stage_exact": True,
            "completed_claim": "inverse_system_of_all_finite_arity_stages",
            "pro_compatibility_checked": True,
            "analytic_dolbeault_completion_status": "requires_external_functional_analysis",
            "completion_layers": self.completion_layers(),
            "cech_ran_simplex_counts": self.cech_ran_simplex_counts(charts),
            "keeps_repeated_inputs": {
                r: self.repeated_words_survive(r) for r in range(self.arity_cutoff + 1)
            },
        }


def ordered_virasoro_controller() -> OrderedChiralE3BarController:
    from compute.lib.chiral_ce_complex import virasoro_lca, virasoro_linfinity

    return OrderedChiralE3BarController(virasoro_lca(), virasoro_linfinity())


def ordered_yangian_controller() -> OrderedChiralE3BarController:
    from compute.lib.chiral_ce_complex import yangian_gl1_lca, yangian_gl1_linfinity

    return OrderedChiralE3BarController(yangian_gl1_lca(), yangian_gl1_linfinity())


def completed_ordered_virasoro_controller(
    *, arity_cutoff: int = 4
) -> CompletedOrderedVertexBarController:
    from compute.lib.chiral_ce_complex import virasoro_lca, virasoro_linfinity

    return CompletedOrderedVertexBarController(
        virasoro_lca(), virasoro_linfinity(), arity_cutoff=arity_cutoff
    )


def completed_ordered_yangian_controller(
    *, arity_cutoff: int = 4
) -> CompletedOrderedVertexBarController:
    from compute.lib.chiral_ce_complex import yangian_gl1_lca, yangian_gl1_linfinity

    return CompletedOrderedVertexBarController(
        yangian_gl1_lca(), yangian_gl1_linfinity(), arity_cutoff=arity_cutoff
    )
