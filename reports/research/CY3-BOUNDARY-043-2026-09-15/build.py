from pathlib import Path
import hashlib
import json
import os
import subprocess

ROOT = Path(__file__).resolve().parents[3]
REPORT = Path(__file__).resolve().parent
BUILD = REPORT / "build"
BUILD.mkdir(exist_ok=True)
env = dict(os.environ, SOURCE_DATE_EPOCH="1789394400", FORCE_SOURCE_DATE="1",
           TEXINPUTS=str(ROOT) + ":/Users/raeez/latex-template:")
command = [
    "pdflatex", "-no-shell-escape", "-interaction=nonstopmode",
    "-halt-on-error", "-file-line-error", "-recorder",
    "-output-directory=" + str(BUILD), "standalone/polynomial_boundary_algebras.tex",
]
for number in range(1, 4):
    with (BUILD / f"pass-{number}.stdout").open("wb") as out:
        subprocess.run(command, cwd=ROOT, env=env, stdout=out, stderr=subprocess.STDOUT, check=True)
pdf = BUILD / "polynomial_boundary_algebras.pdf"
result = {"command": command, "cwd": str(ROOT), "passes": 3,
          "pdf": str(pdf), "sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
          "acceptance": "main-thread build only; mathematical acceptance pending"}
(REPORT / "build-result.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
