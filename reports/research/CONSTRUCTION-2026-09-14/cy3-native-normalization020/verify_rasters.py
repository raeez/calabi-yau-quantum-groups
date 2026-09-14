from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess,hashlib,json
R=Path(__file__).resolve().parent;P=R/'build-candidate/cy3_candidate.pdf'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(item):
 page,dpi,path=item
 cmd=['pdftoppm','-f',str(page),'-l',str(page),'-r',str(dpi),'-singlefile','-png',str(P)]
 q=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE);assert q.returncode==0,q.stderr
 actual=hashlib.sha256(q.stdout).hexdigest();want=sha(path);assert actual==want,(page,dpi,actual,want)
 return {'page':page,'dpi':dpi,'sha256':actual,'match':True}
items=[(p,80,R/'render-native'/('page-%03d.png'%p)) for p in range(1,542)]+[(int(p.stem.split('-')[-1]),120,p) for p in sorted((R/'render-selected').glob('candidate-*.png'))]
with ThreadPoolExecutor(max_workers=8) as e:records=list(e.map(run,items))
(R/'final-native-raster-verification.json').write_text(json.dumps({'pdf_sha256':sha(P),'command_pattern':['pdftoppm','-f','PAGE','-l','PAGE','-r','DPI','-singlefile','-png',str(P)],'output':'PNG on stdout; no intermediate files','records':records,'all_match':True},indent=2)+'\n')
print('All',len(records),'final native page rasters match retained inspection images')
