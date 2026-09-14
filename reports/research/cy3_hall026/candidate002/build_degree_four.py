"""Build the scalar Hall module with the frozen shared template."""

from pathlib import Path
import hashlib
import json
import os
import subprocess

report = Path(__file__).resolve().parent
workspace = report.parents[3]
source = workspace / "research-candidates/cy3_hall026/candidate002"
build = report / "build-degree-four"
build.mkdir(exist_ok=True)
template = report.parent / "frozen-inputs/raeez-math-template.sty"
assert hashlib.sha256(template.read_bytes()).hexdigest() == (
    "07336dc2503195a619a5b566e8730e891d4c81b2465530873214d7087b83e4b5")
environment = dict(os.environ)
environment.update(TEXINPUTS=str(report.parent / "frozen-inputs") + "//:" + str(source) + "//:",
                   SOURCE_DATE_EPOCH="1789344000", FORCE_SOURCE_DATE="1", BIBINPUTS=str(source)+":")
command = ["/Library/TeX/texbin/pdflatex", "-no-shell-escape",
           "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "-recorder",
           "-output-directory=" + str(build), "-jobname=scalar-hall", str(source / "degree-four-main.tex")]
passes = []
previous = None
for iteration in range(1, 7):
    run = subprocess.run(command, cwd=source, env=environment,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (build / f"pass{iteration}.txt").write_bytes(run.stdout)
    passes.append({"pass": iteration, "exit": run.returncode})
    if run.returncode:
        raise SystemExit(run.returncode)
    if iteration == 1:
        bib = subprocess.run(["/Library/TeX/texbin/bibtex", "scalar-hall"], cwd=build, env=environment, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (build / "bibtex.txt").write_bytes(bib.stdout)
        if bib.returncode:
            raise SystemExit(bib.returncode)
    state = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
             for pattern in ("*.aux", "*.toc", "*.out") for p in build.glob(pattern)}
    if iteration >= 3 and state == previous:
        break
    previous = state
else:
    raise RuntimeError("Auxiliary files did not converge in six passes")
record = {"command": command, "cwd": str(source), "passes": passes,
          "TEXINPUTS": environment["TEXINPUTS"], "SOURCE_DATE_EPOCH": "1789344000",
          "FORCE_SOURCE_DATE": "1", "auxiliary_hashes": state,
          "pdf_sha256": hashlib.sha256((build / "scalar-hall.pdf").read_bytes()).hexdigest()}
(report / "degree-four-build-command.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"passes": len(passes), "pdf_sha256": record["pdf_sha256"]}, indent=2))
