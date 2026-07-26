"""Source-surface guard for scalar traces versus full genus coefficients."""

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def _read(relative: str) -> str:
    return (REPO_ROOT / relative).read_text(encoding="utf-8")


def _squash(text: str) -> str:
    return " ".join(text.split())


def test_scalar_formula_is_not_the_cross_channel_carrier() -> None:
    surface = "\n".join(
        _read(path)
        for path in (
            "chapters/connections/modular_koszul_bridge.tex",
            "chapters/theory/braided_factorization.tex",
            "chapters/theory/modular_trace.tex",
            "chapters/theory/cy_to_chiral.tex",
            "chapters/examples/k3e_cy3_programme.tex",
            "chapters/examples/k3e_bkm_chapter.tex",
            "chapters/connections/bar_cobar_bridge.tex",
        )
    )

    for verb in ("receives", "acquires"):
        forbidden = "scalar formula " + verb
        assert forbidden not in surface
    assert "scalar formula " + "fails and requires" not in surface
    assert "all-weight, " + "with cross-channel correction" not in surface
    assert "F_g = " + r"\kappa_{\mathrm{ch}}" not in surface


def test_modular_bridge_names_scalar_trace_and_full_coefficient() -> None:
    text = _squash(_read("chapters/connections/modular_koszul_bridge.tex"))

    assert (
        r"F_g(A_\cC) \;=\; F_g^{\mathrm{sc}}(A_\cC) + "
        r"\delta F_g^{\mathrm{cross}}(A_\cC)"
    ) in text
    assert (
        r"F_g(\cA_{K3 \times E}) = "
        r"F_g^{\mathrm{sc}}(\cA_{K3 \times E}) + "
        r"\delta F_g^{\mathrm{cross}}(\cA_{K3 \times E})"
    ) in text
    assert (
        r"F_g(\cW_{1+\infty}) = "
        r"F_g^{\mathrm{sc}}(\cW_{1+\infty}) + "
        r"\delta F_g^{\mathrm{cross}}(\cW_{1+\infty})"
    ) in text


def test_braided_factorization_names_scalar_trace_and_full_coefficient() -> None:
    text = _squash(_read("chapters/theory/braided_factorization.tex"))

    assert "This is the scalar trace of the genus coefficient." in text
    assert (
        r"F_g(\cA) \;=\; F_g^{\mathrm{sc}}(\cA) + "
        r"\delta F_g^{\mathrm{cross}}(\cA)"
    ) in text
    assert (
        r"F_g^{\mathrm{sc}}(\cA)=\kappa_{\mathrm{ch}}(\cA)\lambda_g"
    ) in text


def test_vol3_active_shadow_surfaces_name_full_coefficient() -> None:
    modular_trace = _squash(_read("chapters/theory/modular_trace.tex"))
    cy_to_chiral = _squash(_read("chapters/theory/cy_to_chiral.tex"))
    k3e = _squash(_read("chapters/examples/k3e_cy3_programme.tex"))

    assert (
        r"\mathrm{obs}_g^{\mathrm{sc}}(A_\cC)="
        r"\kappa_{\mathrm{ch}}(A_\cC)\cdot\lambda_g"
    ) in modular_trace
    assert (
        r"F_g(A_\cC)=F_g^{\mathrm{sc}}(A_\cC)+"
        r"\delta F_g^{\mathrm{cross}}(A_\cC)"
    ) in modular_trace
    assert (
        r"F_g^{\DT}(X)=F_g^{\mathrm{sc}}(A_X)+"
        r"\delta F_g^{\mathrm{cross}}(A_X)"
    ) in cy_to_chiral
    assert (
        r"F_g(\cA^!)=F_g^{\mathrm{sc}}(\cA^!)+"
        r"\delta F_g^{\mathrm{cross}}(\cA^!)"
    ) in k3e
    assert (
        r"F_g(V_{K3})=F_g^{\mathrm{sc}}(V_{K3})+"
        r"\delta F_g^{\mathrm{cross}}(V_{K3})"
    ) in k3e


def test_bkm_and_bar_cobar_bridges_type_scalar_lane() -> None:
    bkm = _squash(_read("chapters/examples/k3e_bkm_chapter.tex"))
    bar_cobar = _squash(_read("chapters/connections/bar_cobar_bridge.tex"))

    assert (
        r"F_g = F_g^{\mathrm{sc}} + "
        r"[\text{higher-degree shadow corrections}]"
    ) in bkm
    assert (
        r"F_g^{\mathrm{sc}} = \kappa_{\mathrm{ch}} \cdot \hat{A}_g"
    ) in bkm
    assert (
        r"F_g^{\mathrm{sc}} = "
        r"\kappa_{\mathrm{ch}} \cdot \lambda_g^{\mathrm{FP}}"
    ) in bar_cobar
