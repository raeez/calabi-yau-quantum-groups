from pathlib import Path
import os,subprocess,hashlib,sys,json
R=Path(__file__).resolve().parent;W=R.parents[3]
mode=sys.argv[1];assert mode in ['baseline','candidate','focused']
S=R/'baseline-source' if mode=='baseline' else W/'research-candidates/cy3-native-normalization020/source'
B=Path(sys.argv[2]).resolve() if len(sys.argv)>2 else R/('build-'+mode)
assert B.is_relative_to(R), 'Build outputs must remain inside this evidence directory'
if (R/'source-freeze.json').exists() and B.exists():
 raise RuntimeError('Frozen output exists; select a new output directory')
B.mkdir(exist_ok=True)
T=Path('/Users/raeez/latex-template/worktrees/manuscript-source-clean-20260914/coordination/source-clean-20260914/candidate002/source')
assert hashlib.sha256((T/'raeez-math-template.sty').read_bytes()).hexdigest()=='07336dc2503195a619a5b566e8730e891d4c81b2465530873214d7087b83e4b5'
job='cy3_'+mode
entry='focused_hall.tex' if mode=='focused' else 'collision_geometry.tex'
cmd=['/Library/TeX/texbin/pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-file-line-error','-recorder','-output-directory='+str(B),'-jobname='+job,entry]
env=dict(os.environ,SOURCE_DATE_EPOCH='1789344000',FORCE_SOURCE_DATE='1',TEXINPUTS='.:'+str(T)+'//:',BIBINPUTS=str(S/'platonic')+':')
records=[];previous=None
for i in range(6):
 with (B/('pass%d.log'%(i+1))).open('w') as log:r=subprocess.run(cmd,cwd=S/'platonic',env=env,stdout=log,stderr=subprocess.STDOUT)
 records.append({'pass':i+1,'exit':r.returncode})
 if r.returncode:raise SystemExit(r.returncode)
 if i==0 and mode!='focused':
  with (B/'bibtex.log').open('w') as log:r=subprocess.run(['/Library/TeX/texbin/bibtex',job],cwd=B,env=env,stdout=log,stderr=subprocess.STDOUT)
  if r.returncode:raise SystemExit(r.returncode)
 signature={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for ext in ['aux','toc','out'] for p in B.glob('*.'+ext)}
 if i>=2 and signature==previous:break
 previous=signature
else:raise RuntimeError('Auxiliary files did not converge in six passes')
(B/'convergence.json').write_text(json.dumps({'mode':mode,'passes':records,'auxiliary_signature':signature,'command':cmd,'cwd':str(S/'platonic'),'environment':{'TEXINPUTS':env['TEXINPUTS'],'BIBINPUTS':env['BIBINPUTS']},'shell_escape':False,'SOURCE_DATE_EPOCH':env['SOURCE_DATE_EPOCH'],'FORCE_SOURCE_DATE':env['FORCE_SOURCE_DATE']},indent=2)+'\n')
print(mode,len(records),B/(job+'.pdf'))
