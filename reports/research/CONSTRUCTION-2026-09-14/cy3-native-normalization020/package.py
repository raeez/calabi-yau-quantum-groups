from pathlib import Path
import hashlib,json,subprocess,re,sys,difflib,tarfile,gzip,io,collections
R=Path(__file__).resolve().parent;W=R.parents[3];S=W/'research-candidates/cy3-native-normalization020/source';O=R/'baseline-source'
assert not (R/'source-freeze.json').exists()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rec(p):return {'path':str(p.relative_to(W)) if p.is_relative_to(W) else str(p),'sha256':sha(p),'bytes':p.stat().st_size}
def save(name,obj):(R/name).write_text(json.dumps(obj,indent=2)+'\n')
# Freeze inputs to the build without treating generated aux files as source dependencies.
deps={};diagnostics={};pdfs={}
for mode in ['baseline','candidate','focused']:
 B=R/('build-'+mode);BS=O if mode=='baseline' else S;cwd=BS/'platonic';fls=B/('cy3_'+mode+'.fls');rows=[];outputs=set()
 def resolve(line):
  p=Path(line);return (cwd/p).resolve() if not p.is_absolute() else p.resolve()
 for line in fls.read_text().splitlines():
  if line.startswith('OUTPUT '):outputs.add(resolve(line[7:]))
 files={resolve(l[6:]) for l in fls.read_text().splitlines() if l.startswith('INPUT ')}
 for p in sorted(files):
  if p in outputs or p.is_relative_to(B):continue
  assert p.is_file(),p
  row=rec(p)
  if p.is_relative_to(BS):category='reader_source'
  elif '/latex-template/worktrees/manuscript-source-clean-20260914/' in str(p):
   category='pinned_shared_template';assert sha(p)=='07336dc2503195a619a5b566e8730e891d4c81b2465530873214d7087b83e4b5'
  elif str(p).startswith(('/usr/local/texlive/','/Users/raeez/Library/texlive/','/Library/TeX/')):category='tex_distribution_or_format'
  else:raise RuntimeError('Unclassified reader input '+str(p))
  row['category']=category;rows.append(row)
 generated=[dict(rec(p),category='generated_build_input') for p in sorted(files) if (p in outputs or p.is_relative_to(B)) and p.is_file()]
 deps[mode]={'recorder':rec(fls),'files':rows,'generated_inputs':generated,'input_aggregate_sha256':hashlib.sha256(json.dumps(rows+generated,sort_keys=True,separators=(',',':')).encode()).hexdigest(),'count':len(rows),'generated_count':len(generated),'full_recorder_count':len(rows)+len(generated)}
 bibinputs=[]
 if mode!='focused':
  blg=(B/('cy3_'+mode+'.blg')).read_text()
  for name in re.findall(r'Database file #[0-9]+: (.+)',blg):bibinputs.append(dict(rec(cwd/name),category='bibtex_database'))
  style=re.search(r'The style file: (.+)',blg).group(1)
  stylepath=Path(subprocess.check_output(['/Library/TeX/texbin/kpsewhich',style],text=True).strip()).resolve()
  bibinputs.append(dict(rec(stylepath),category='bibtex_style'))
 deps[mode]['additional_bibtex_inputs']=bibinputs
 deps[mode]['complete_build_input_count']=len(rows)+len(generated)+len(bibinputs)
 deps[mode]['complete_build_input_aggregate_sha256']=hashlib.sha256(json.dumps(rows+generated+bibinputs,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 log=(B/('cy3_'+mode+'.log')).read_text(encoding='latin1')
 fatal=re.findall(r'^!.*|^.*(?:undefined references|undefined citations|multiply defined|LaTeX Error|Package .* Error).*',log,re.M)
 assert not fatal,fatal
 warnings=json.loads((B/'diagnostics.json').read_text())
 diagnostics[mode]={'fatal_or_reference_errors':fatal,'warnings':warnings,'convergence':json.loads((B/'convergence.json').read_text()),'log_decoding':'latin1: TeX font diagnostics contain non-UTF-8 bytes'}
 pdf=B/('cy3_'+mode+'.pdf');info=(B/'pdfinfo.txt').read_text()
 pdfs[mode]={**rec(pdf),'page_count':int(re.search(r'Pages:\s+(\d+)',info).group(1)),'text':rec(B/'reader.txt'),'metadata':rec(B/'pdfinfo.txt'),'mathematical_status':'unaccepted normalization comparison candidate' if mode!='baseline' else 'unchanged predecessor; known normalization defect'}
 subprocess.run(['pdfinfo','-dests',str(pdf)],stdout=(B/'destinations.txt').open('w'),check=True)
save('dependency-manifest.json',deps);save('build-diagnostics.json',diagnostics);save('pdf-records.json',pdfs)
# Native reader patch from the exact preserved predecessor source.
changes=[];patch=''
for p in sorted(S.rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(S);old=O/rel
 assert old.is_file(),rel
 if p.read_bytes()!=old.read_bytes():
  changes.append({'relative':str(rel),'old':rec(old),'new':rec(p)})
  patch+=''.join(difflib.unified_diff(old.read_text().splitlines(True),p.read_text().splitlines(True),fromfile='a/'+str(rel),tofile='b/'+str(rel)))
assert len(changes)==4
(R/'normalization-integration.patch').write_text(patch)
cmd=['git','apply','--check','--directory='+str(O.relative_to(W)),str(R/'normalization-integration.patch')]
q=subprocess.run(cmd,cwd=W,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True);assert q.returncode==0,q.stdout
save('patch-check.json',{'command':cmd,'exit':q.returncode,'output':q.stdout,'applied':False})
# Independently replay every text hunk in memory.
sections=re.split(r'(?m)(?=^--- a/)',patch);replayed=[]
for sec in sections:
 if not sec:continue
 lines=sec.splitlines(True);rel=lines[0][6:].rstrip('\n');old=(O/rel).read_text().splitlines(True);result=[];cursor=0;i=2
 while i<len(lines):
  h=re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',lines[i]);assert h,lines[i]
  start=int(h.group(1))-1;result.extend(old[cursor:start]);cursor=start;i+=1
  while i<len(lines) and not lines[i].startswith('@@ '):
   l=lines[i];tag=l[0]
   if tag in ' -':assert old[cursor]==l[1:];cursor+=1
   if tag in ' +':result.append(l[1:])
   i+=1
 result.extend(old[cursor:]);assert ''.join(result)==(S/rel).read_text();replayed.append(rel)
save('changed-paths.json',{'changes':changes,'unchanged_source_files':len([p for p in S.rglob('*') if p.is_file()])-len(changes),'all_patch_hunks_replayed_in_memory':replayed})
# All source bytes, including unchanged complete proof inputs, in a reproducible archive.
archive=R/'reader-source.tar.gz'
with archive.open('wb') as raw:
 with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0) as gz:
  with tarfile.open(fileobj=gz,mode='w',format=tarfile.PAX_FORMAT) as tar:
   for p in sorted(S.rglob('*')):
    if not p.is_file():continue
    data=p.read_bytes();ti=tarfile.TarInfo(str(p.relative_to(S)));ti.size=len(data);ti.mode=0o644;ti.mtime=0;tar.addfile(ti,io.BytesIO(data))
archive_rows=[]
with tarfile.open(archive,'r:gz') as tar:
 for member in tar.getmembers():
  data=tar.extractfile(member).read();assert data==(S/member.name).read_bytes()
  archive_rows.append({'path':member.name,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
save('archive-manifest.json',{'archive':rec(archive),'entries':archive_rows,'all_entries_match_source':True,'extracted_to_disk':False})
# Reader-only firewall, with mathematical bibliography fields distinguished from operational text.
pattern=re.compile(r'agent|worktree|review packet|audit|repair task|checkpoint|workflow|acceptance|prompt|GPT|Claude|ChatGPT|source.freeze|commit hash|task.owner|TODO|roadmap|/Users/|~/ecosystem|kernel/formal|centcom/',re.I)
sourcehits=[]
for p in sorted(S.rglob('*')):
 if p.is_file():
  for n,line in enumerate(p.read_text().splitlines(),1):
   if pattern.search(line):sourcehits.append({'path':str(p.relative_to(S)),'line':n,'text':line})
expected=[x for x in sourcehits if x['path']=='platonic/platonic.sty' and r'\newenvironment{roadmap}' in x['text']]
assert sourcehits==expected,sourcehits
pdfhits=[];metahits=[]
for mode in ['candidate','focused']:
 B=R/('build-'+mode)
 for n,line in enumerate((B/'reader.txt').read_text().splitlines(),1):
  if pattern.search(line):pdfhits.append({'mode':mode,'line':n,'text':line})
 for line in (B/'pdfinfo.txt').read_text().splitlines():
  if pattern.search(line):metahits.append({'mode':mode,'text':line})
assert not pdfhits and not metahits,(pdfhits,metahits)
save('firewall-check.json',{'source_hits':sourcehits,'source_disposition':'Only inherited unused roadmap environment identifier; mathematical layout definition, no operational prose','pdf_hits':pdfhits,'metadata_hits':metahits,'all_reader_sources_scanned':True,'passed':True})
# Anchors and destination pages, read from converged aux and PDF destinations.
anchors=[]
for change in changes:
 p=S/change['relative']
 for n,line in enumerate(p.read_text().splitlines(),1):
  if r'\label{' in line:anchors.append({'source':str(p.relative_to(W)),'line':n,'label':line.strip()})
save('source-anchors.json',anchors)
labelrows=[]
for mode in ['candidate','focused']:
 B=R/('build-'+mode);aux=(B/('cy3_'+mode+'.aux')).read_text();dest=(B/'destinations.txt').read_text()
 for label in ['thm:hall-coefficient-compatibility','ts22:thm:assoc211','ts22:prop:normalization','fl221:thm:assoc','fl221:lem:cyclic','fl221:prop:gluing']:
  m=re.search(r'\\newlabel\{'+re.escape(label)+r'\}\{\{([^{}]*)\}\{([^{}]*)\}\{[^\n]*\}\{([^{}]*)\}\{\}\}',aux);assert m,label
  lines=[l for l in dest.splitlines() if '"'+m.group(3)+'"' in l];assert len(lines)==1,(label,lines)
  labelrows.append({'mode':mode,'label':label,'number':m.group(1),'printed_page':m.group(2),'destination':m.group(3),'pdf_destination':lines[0]})
save('label-check.json',{'labels':labelrows,'undefined_or_duplicate_reference_errors':False,'gluing_destination':'Current native destination is on PDF369 where Proposition134.4 starts. Predecessor destination offset no longer manifests after the new mathematical paragraph; template unchanged.'})
# All full native/focused renders retained; only assigned pages inspected mathematically.
render_records=[]
for root in [R/'render-native',R/'render-focused',R/'render-selected',R/'inspection-sheets']:
 for p in sorted(root.glob('*.png')):render_records.append(rec(p))
assert len(list((R/'render-native').glob('*.png')))==541
assert len(list((R/'render-focused').glob('*.png')))==22
plan=json.loads((R/'render-commands.json').read_text())
save('render-manifest.json',{'pdfs':pdfs,'renders':render_records,'full_native_render_dpi':80,'full_focused_render_dpi':115,'selected_native_and_baseline_dpi':120,'all_native_pages_rendered':541,'all_focused_pages_rendered':22,'visual_inspection':{'native_pages':plan['selected_native_pages'],'baseline_pages':plan['baseline_pages'],'focused_pages':list(range(1,23)),'inspection_method':'Direct images for decisive new pages, two-page sheets for every listed page and transitions; direct final focused page also inspected','clipping_or_overlap':False,'firewall_violations':False,'whole_book_mathematical_acceptance':False}})
versions={}
for key,cmd in [('pdflatex',['/Library/TeX/texbin/pdflatex','--version']),('bibtex',['/Library/TeX/texbin/bibtex','--version']),('pdftoppm',['pdftoppm','-v']),('pdfinfo',['pdfinfo','-v']),('git',['git','--version'])]:
 p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True);versions[key]={'command':cmd,'exit':p.returncode,'output':p.stdout}
versions['python']=sys.version;save('tool-versions.json',versions)
print(json.dumps({'dependencies':{k:v['count'] for k,v in deps.items()},'source_changes':[x['relative'] for x in changes],'archive_entries':len(archive_rows),'render_files':len(render_records),'pdfs':{k:{'sha256':v['sha256'],'pages':v['page_count']} for k,v in pdfs.items()}},indent=2))
