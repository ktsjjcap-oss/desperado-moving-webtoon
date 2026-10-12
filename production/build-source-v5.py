"""Publish the 80-panel source comic; preserve original generated raster bytes."""
from pathlib import Path
import json, html, base64
import numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
ART=ROOT/'assets/seq01/source-v5'
DESCRIPTIONS=json.loads((ROOT/'production/source-v5-descriptions.json').read_text())
rows=[]
for strip in range(1,21):
    path=ART/f'{strip:02}.png'
    with Image.open(path) as im: im.verify()
    a=np.asarray(Image.open(path).convert('RGB')); h,w=a.shape[:2]
    whites=np.flatnonzero((a.min(axis=2)>235).mean(axis=1)>.985)
    groups=np.split(whites,np.flatnonzero(np.diff(whites)>1)+1)
    bands=[g for g in groups if len(g)>=2 and h*.10<g[0]<h*.92]
    if len(bands)!=3: raise ValueError(f'Strip {strip}: inspect panel dividers')
    cuts=[int((g[0]+g[-1])//2) for g in bands]; edges=[0,*cuts,h]
    for local,(top,bottom) in enumerate(zip(edges,edges[1:])):
        n=(strip-1)*4+local+1
        sequence=1 if n<=28 else 2 if n<=48 else 3
        gap=18 if local else 54
        if n in [4,13,29,41,49,53,57,65,73,80]: gap=110
        if n in [3,50,54,66,70]: gap=60
        if n==1:gap=0
        rows.append(dict(panel=n,strip=strip,sequence=sequence,src=f'/assets/seq01/source-v5/{strip:02}.png',source_width=w,source_height=h,top=top,height=bottom-top,gap=gap,description=DESCRIPTIONS[n-1]))
assert len(rows)==80 and len(DESCRIPTIONS)==80
parts=[]
for r in rows:
    top=-100*r['top']/r['height']
    style=f"aspect-ratio:{r['source_width']}/{r['height']};margin-top:clamp(12px,{r['gap']/760*100:.5f}cqw,{r['gap']}px)" if r['gap'] else f"aspect-ratio:{r['source_width']}/{r['height']};margin-top:0"
    parts.append(f'<figure class="panel" id="panel-{r["panel"]}" data-panel="{r["panel"]}" data-sequence="{r["sequence"]}" style="{style}" aria-label="{html.escape(r["description"],quote=True)}"><img src="{r["src"]}" width="{r["source_width"]}" height="{r["source_height"]}" style="top:{top:.8f}%" alt="" aria-hidden="true" loading="eager" decoding="async"></figure>')
page='''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#12171d"><title>DESPERADO · 1화 · 백억짜리 한 손</title><style>*{box-sizing:border-box}html{background:#12171d;scroll-behavior:smooth}body{margin:0;font-family:system-ui,sans-serif;color:#eef1f4}header,nav,footer{max-width:var(--reader-width,760px);margin:auto;padding:16px;display:flex;align-items:center;justify-content:space-between;gap:12px}header a{font-weight:800;letter-spacing:1px;text-decoration:none}header span,footer p{font-size:13px;color:#aab6c2}nav{padding-top:0;justify-content:flex-start;flex-wrap:wrap}nav a{font-size:13px;border:1px solid #42515e;border-radius:20px;padding:6px 12px;text-decoration:none}a{color:inherit}main{max-width:var(--reader-width,760px);margin:auto;background:#fff;container-type:inline-size;padding-bottom:64px;overflow:hidden}.panel{position:relative;width:100%;margin-left:0;margin-right:0;margin-bottom:0;overflow:hidden;background:#fff;scroll-margin-top:12px}.panel img{position:absolute;left:0;width:100%;height:auto;display:block;max-width:none}footer{align-items:flex-start}footer a{font-size:14px;white-space:nowrap}@media(max-width:420px){header{gap:8px}header a{font-size:14px}header span{font-size:11px}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}</style><script>if(new URLSearchParams(location.search).get("view")=="mobile")document.documentElement.style.setProperty("--reader-width","390px")</script></head><body data-source-version="5"><header><a href="/episodes/ep01/source-v5">DESPERADO</a><span>1화 · 백억짜리 한 손</span></header><nav aria-label="장면 바로가기"><a href="#panel-1">처음부터</a><a href="#panel-29">금고 접근</a><a href="#panel-49">장갑 탈취</a><a href="#panel-65">옥상 탈출</a></nav><main aria-label="데스페라도 1화 시퀀스 1~3 원본 웹툰, 위에서 아래로 읽으세요">'''+''.join(parts)+'''</main><footer><p>시퀀스 1~3 · 원본 개작본<br>다음 시퀀스: 몇 년 뒤, 고해성사</p><a href="#panel-1">맨 위로 ↑</a></footer></body></html>'''
(ROOT/'episodes/ep01/source-v5.html').write_text(page)
(ART/'panels.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
(ART/'manifest.json').write_text(json.dumps(dict(version=5,phase='source-comic',panels=80,strips=20,sequences=[dict(sequence=1,panels=28),dict(sequence=2,panels=20),dict(sequence=3,panels=32)],motion_applied=False,fictional_appraisal_krw=10000000000,rendering='CSS viewports of unmodified generated artwork with editorial white spacing'),ensure_ascii=False,indent=2))
# Store each source image only once in the offline original.
offline=page.replace('href="/episodes/ep01/source-v5"','href="#panel-1"'); originals={}
for strip in range(1,21):
    src=f'/assets/seq01/source-v5/{strip:02}.png'
    offline=offline.replace(f'src="{src}"',f'data-strip="{strip:02}"')
    originals[f'{strip:02}']='data:image/png;base64,'+base64.b64encode((ART/f'{strip:02}.png').read_bytes()).decode()
offline=offline.replace('</body>','<script>const originals='+json.dumps(originals)+';document.querySelectorAll("img[data-strip]").forEach(img=>{img.src=originals[img.dataset.strip]});</script></body>')
output=ROOT.parent/'DESPERADO_EP01_SOURCE_v5.html';output.write_text(offline)
for p in [ROOT/'index.html',ROOT/'episodes/ep01/source.html']:
    p.write_text('<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0;url=/episodes/ep01/source-v5"><title>DESPERADO 원본 웹툰</title></head><body><a href="/episodes/ep01/source-v5">최신 원본 웹툰 보기</a></body></html>')
old=ROOT/'episodes/ep01/source-v4.html';text=old.read_text()
if '/episodes/ep01/source-v5' not in text:
    text=text.replace('<main aria-label=', '<nav style="max-width:760px;margin:auto;padding:12px 16px"><a href="/episodes/ep01/source-v5">새 개작본 · 시퀀스 1~3 보기 →</a></nav><main aria-label=')
old.write_text(text)
print(f'Built 80 panels, 20 strips; offline bytes {output.stat().st_size}')
