from pathlib import Path
from PIL import Image
import numpy as np,json,html,sys
ROOT=Path(__file__).resolve().parents[1];ART=ROOT/'assets/seq01/source-v6'
pages=json.loads((ROOT/'production/source-v6-approved-pages.json').read_text(encoding='utf-8'))
partial='--partial' in sys.argv;rows=[];proof=[]
timing_path=ART/'timing.json'
timing=json.loads(timing_path.read_text(encoding='utf-8')) if timing_path.exists() else {'duration':112*5,'panels':[dict(start=i*5,end=(i+1)*5,duration=5) for i in range(112)]}
video_panels={1:'city.mp4',2:'concert.mp4',66:'exchange.mp4'}
for strip,p in enumerate(pages,1):
 path=ART/f'{strip:02}.png'
 if not path.exists():
  if partial:break
  raise FileNotFoundError(path)
 im=Image.open(path).convert('RGB');im.save(ART/f'{strip:02}.webp',quality=92,method=6);a=np.asarray(im);h,w=a.shape[:2]
 whites=np.flatnonzero((a.min(axis=2)>235).mean(axis=1)>.975)
 groups=np.split(whites,np.flatnonzero(np.diff(whites)>1)+1)
 bands=[g for g in groups if len(g)>=2 and h*.09<g[0]<h*.93]
 if len(bands)!=3:raise ValueError(f'Strip {strip} must have 3 dividers, found {[(int(g[0]),int(g[-1])) for g in bands]}')
 cuts=[int((g[0]+g[-1])//2) for g in bands];edges=[0,*cuts,h]
 for local,(top,bottom) in enumerate(zip(edges,edges[1:])):
  n=(strip-1)*4+local+1;gap=24 if local else 72
  if n in [1,41,77]:gap=0 if n==1 else 130
  r=dict(strip=strip,sequence=p['seq'],src=f'/assets/seq01/source-v6/{strip:02}.webp',source_width=w,source_height=h,top=top,height=bottom-top,gap=gap,action=p['panels'][local][0],text=[s for s in p['panels'][local][1:] if s],**timing['panels'][n-1]);rows.append(r)
  if n in video_panels:
   frames=ROOT.parent/'video-frames';frames.mkdir(exist_ok=True)
   im.crop((0,top,w,bottom)).save(frames/f'{n:03}.png')
 thumb=im.copy();thumb.thumbnail((256,768));proof.append((strip,thumb))
if not partial:assert len(rows)==112
(ART/'panels.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
parts=[]
for r in rows:
 n=r['panel'];top=-100*r['top']/r['height'];style=f'aspect-ratio:{r["source_width"]}/{r["height"]};margin-top:clamp(12px,{r["gap"]/760*100:.5f}cqw,{r["gap"]}px)' if r['gap'] else f'aspect-ratio:{r["source_width"]}/{r["height"]};margin-top:0'
 video=f'<video muted playsinline preload="auto" src="/assets/seq01/source-v6/{video_panels[n]}"></video>' if n in video_panels and (ART/video_panels[n]).exists() else ''
 if n==1 and video:video+='<span class="motion-caption">그날 밤, 서울.</span>'
 text=html.escape(r['action']+' '+' '.join(r['text']),quote=True)
 if video and n in [2,66]:style=style.replace(f'aspect-ratio:{r["source_width"]}/{r["height"]}','aspect-ratio:16/9')
 parts.append(f'<figure class="panel" id="panel-{n}" data-panel="{n}" data-sequence="{r["sequence"]}" style="{style}" aria-label="{text}"><div class="frame"><div class="still" style="aspect-ratio:{r["source_width"]}/{r["height"]}"><img src="{r["src"]}" width="{r["source_width"]}" height="{r["source_height"]}" style="top:{top:.8f}%" alt="" decoding="async"></div>{video}</div><figcaption class="sr">{text}</figcaption></figure>')
transcript='<details class="transcript"><summary>대사로 다시 읽기</summary>'+''.join('<h3>'+html.escape(f'{i+1:02} · {p["title"]}')+'</h3>'+''.join('<p>'+html.escape(s)+'</p>' for a in p['panels'] for s in a[1:] if s) for i,p in enumerate(pages))+'</details>'
head='<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#0c1017"><meta name="description" content="백억짜리 장갑, 다섯 명의 팀. 데스페라도 1화."><title>DESPERADO · 백억짜리 한 손</title><link rel="stylesheet" href="/assets/seq01/source-v6-reader.css"></head><body data-source-version="6"><header><a href="/episodes/ep01/moving-v6">DESPERADO</a><small>EP.01 / 시퀀스 1–3</small></header>'
intro='<section class="intro"><span class="eyebrow">COMEDY · HEIST</span><h1>백억짜리 한 손</h1><p>잠긴 금고보다 어려운 건, 사람의 눈을 피하는 일.<br>다섯 명의 팀이 백억짜리 장갑을 노린다.</p><nav><button id="start" class="primary">소리 켜고 시작</button><a href="#panel-41">검수실로</a><a href="#panel-77">탈출</a><a href="/episodes/ep01/source-v6">정지 웹툰</a></nav><p>아래로 스크롤하면 진행되고, 위로 올리면 되감깁니다.</p></section>'
end='</main><footer><div class="ending">그날 밤은 끝났다.</div>다음 시퀀스 · 몇 년 뒤, 고해성사<br><a href="#panel-1">처음부터 다시 읽기 ↑</a></footer>'
controls='<div class="controls" role="region" aria-label="재생 제어"><button id="sound" aria-pressed="false">소리 켜기</button><button id="auto" aria-pressed="false">자동 재생</button><div class="control-main"><input type="range" id="timeline" min="0" max="1000" value="0" aria-label="이야기 위치"><div class="status-row"><span id="state">소리 없이 읽기</span><span id="counter">1 / 112컷</span></div></div></div><audio id="dialogue" preload="metadata" src="/assets/seq01/source-v6/dialogue.mp3"></audio><audio id="music" preload="metadata" loop src="/assets/seq01/source-v6/audio/music.mp3"></audio>'
reader_data=json.dumps({'duration':timing['duration'],'panels':rows},ensure_ascii=False).replace('</','<\\/')
moving=head+intro+'<main class="reader" aria-label="위에서 아래로 읽는 무빙툰">'+''.join(parts)+end+transcript+controls+'<script id="reader-data" type="application/json">'+reader_data+'</script><script src="/assets/seq01/source-v6-reader.js"></script></body></html>'
static=head+intro.replace('<button id="start" class="primary">소리 켜고 시작</button>','<a class="primary" href="/episodes/ep01/moving-v6">무빙툰으로 보기</a>').replace('<p>아래로 스크롤하면 진행되고, 위로 올리면 되감깁니다.</p>','')+'<main class="reader" aria-label="원본 웹툰">'+''.join(parts)+end+transcript+'</body></html>'
(ROOT/'episodes/ep01/moving-v6.html').write_text(moving,encoding='utf-8');(ROOT/'episodes/ep01/source-v6.html').write_text(static,encoding='utf-8')
if not partial:
 for p in [ROOT/'index.html',ROOT/'episodes/ep01/source.html']:
  p.write_text('<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0;url=/episodes/ep01/moving-v6"><title>DESPERADO</title></head><body><a href="/episodes/ep01/moving-v6">최신 무빙툰 보기</a></body></html>',encoding='utf-8')
 manifest=dict(version=6,panels=112,strips=28,sequences=[40,36,36],dialogue_segments=228,duration=timing['duration'],motion='scroll-scrubbed panel camera plus three animated scene clips',source_recovery='108 recovered approved panels with continuity edits plus reconstructed final four',videos=[n for n in video_panels if (ART/video_panels[n]).exists()])
 (ART/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
if proof:
 grid=Image.new('RGB',(256*4,800*((len(proof)+3)//4)),(235,235,235))
 from PIL import ImageDraw
 dr=ImageDraw.Draw(grid)
 for i,(num,thumb) in enumerate(proof):x=i%4*256;y=i//4*800;grid.paste(thumb,(x,y+24));dr.text((x+8,y+4),str(num),fill=(0,0,0))
 grid.save(ROOT.parent/'v6-contact-sheet.jpg',quality=88)
print(f'Built {len(rows)} panels, duration {timing["duration"]:.2f}s')
