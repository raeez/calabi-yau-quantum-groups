"""Build the isolated scalar Hall restriction source and record all inputs."""

from pathlib import Path
import hashlib
import json
import os
import subprocess


report = Path(__file__).resolve().parent
workspace = report.parents[3]
source = workspace / "research-candidates/cy3_hall026/candidate004"
build = report / "build"
build.mkdir(exist_ok=True)
template = report / "frozen-inputs/raeez-math-template.sty"
assert hashlib.sha256(template.read_bytes()).hexdigest() == (
    "07336dc2503195a619a5b566e8730e891d4c81b2465530873214d7087b83e4b5")
environment = dict(os.environ)
environment.update(TEXINPUTS=str(template.parent)+"//:"+str(source)+"//:",
                   BIBINPUTS=str(source)+"//:", SOURCE_DATE_EPOCH="1789344000",
                   FORCE_SOURCE_DATE="1")
command = ["/Library/TeX/texbin/pdflatex", "-no-shell-escape",
           "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "-recorder",
           "-output-directory="+str(build), "-jobname=scalar-restriction",
           str(source/"integrated-main.tex")]
previous = None
passes = []
for iteration in range(1, 7):
    run = subprocess.run(command, cwd=source, env=environment,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (build/f"pass{iteration}.txt").write_bytes(run.stdout)
    passes.append({"pass": iteration, "exit": run.returncode})
    if run.returncode:
        print(run.stdout.decode(errors="replace")[-5000:])
        raise SystemExit(run.returncode)
    if iteration == 1:
        bib = subprocess.run(["/Library/TeX/texbin/bibtex", "scalar-restriction"],
                             cwd=build, env=environment,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (build/"bibtex.txt").write_bytes(bib.stdout)
        if bib.returncode:
            print(bib.stdout.decode(errors="replace"))
            raise SystemExit(bib.returncode)
    state = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
             for pattern in ("*.aux", "*.toc", "*.out") for p in build.glob(pattern)}
    if iteration >= 3 and state == previous:
        break
    previous = state
else:
    raise RuntimeError("Auxiliary files did not converge in six passes")
closure = {}
for line in (build/"scalar-restriction.fls").read_text().splitlines():
    if line.startswith("INPUT "):
        path = Path(line[6:])
        if not path.is_absolute():
            path = source/path
        path = path.resolve()
        if path.is_file():
            closure[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
(report/"tex-input-closure.json").write_text(json.dumps(closure, indent=2, sort_keys=True)+"\n")
record = {"command": command, "cwd": str(source), "passes": passes,
          "TEXINPUTS": environment["TEXINPUTS"], "BIBINPUTS": environment["BIBINPUTS"],
          "SOURCE_DATE_EPOCH": environment["SOURCE_DATE_EPOCH"],
          "FORCE_SOURCE_DATE": environment["FORCE_SOURCE_DATE"],
          "auxiliary_hashes": state, "input_count": len(closure),
          "pdf_sha256": hashlib.sha256((build/"scalar-restriction.pdf").read_bytes()).hexdigest()}
(report/"build-command.json").write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))
