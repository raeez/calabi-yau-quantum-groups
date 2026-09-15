"""Build the current native entrypoint with explicit compiler exit checks."""

import json
import os
from pathlib import Path
import subprocess


root = Path(__file__).resolve().parents[3]
out = Path(__file__).resolve().parent / "strict-build"
out.mkdir(exist_ok=False)
env = os.environ.copy()
env.update(
    TEXINPUTS=f"{root / 'platonic'}:{root}:/Users/raeez/latex-template:",
    BIBINPUTS=f"{root / 'platonic'}:{root}:",
    SOURCE_DATE_EPOCH="1789394400",
    FORCE_SOURCE_DATE="1",
)
commands = []


def run(command, cwd, logname):
    with (out / logname).open("w") as log:
        result = subprocess.run(command, cwd=cwd, env=env,
                                stdout=log, stderr=subprocess.STDOUT)
    commands.append({"command": command, "cwd": str(cwd), "exit_code": result.returncode})
    (out / "commands.json").write_text(json.dumps({
        "commands": commands,
        "environment": {key: env[key] for key in [
            "TEXINPUTS", "BIBINPUTS", "SOURCE_DATE_EPOCH", "FORCE_SOURCE_DATE"]},
    }, indent=2) + "\n")
    if result.returncode:
        raise SystemExit(result.returncode)


for number in range(1, 5):
    run(["pdflatex", "-no-shell-escape", "-interaction=nonstopmode",
         "-halt-on-error", "-file-line-error", "-recorder",
         "-jobname=native-cy3", "-output-directory=" + str(out), "main.tex"],
        root / "platonic", f"pass-{number}.stdout")
    if number == 1:
        run(["bibtex", "native-cy3"], out, "bibtex.stdout")
print("Four strict compiler passes and BibTeX completed successfully.")
