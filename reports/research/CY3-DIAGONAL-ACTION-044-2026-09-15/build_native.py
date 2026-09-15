from pathlib import Path
import json
import os
import subprocess

ROOT=Path(__file__).resolve().parents[3]
REPORT=Path(__file__).resolve().parent
BUILD=REPORT/"native-build"
BUILD.mkdir(exist_ok=True)
env=dict(os.environ,SOURCE_DATE_EPOCH="1789394400",FORCE_SOURCE_DATE="1",
         TEXINPUTS=".:..:/Users/raeez/latex-template:",
         BIBINPUTS=str(ROOT/"platonic")+":"+str(ROOT)+":")
tex=["pdflatex","-no-shell-escape","-interaction=nonstopmode",
     "-halt-on-error","-file-line-error","-recorder",
     "-output-directory="+str(BUILD),"-jobname=native-cy3","main.tex"]
commands=[tex,["bibtex","native-cy3"],tex,tex,tex]
results=[]
for i,command in enumerate(commands,1):
    with (BUILD/f"command-{i}.stdout").open("wb") as out:
        cwd=BUILD if command[0]=="bibtex" else ROOT/"platonic"
        run=subprocess.run(command,cwd=cwd,env=env,
                           stdout=out,stderr=subprocess.STDOUT)
    results.append({"command":command,"cwd":str(cwd),"returncode":run.returncode})
    if run.returncode:
        break
result={"cwd":str(ROOT/"platonic"),"commands":results,
        "completed":len(results)==len(commands) and all(r["returncode"]==0 for r in results),
        "scope":"Actual native entrypoint build. No whole-book mathematical or editorial acceptance."}
(REPORT/"native-build-result.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result))
