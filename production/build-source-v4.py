"""Build the comic reader without modifying the generated artwork bytes."""
from pathlib import Path
import json, html, base64
import numpy as np
from PIL import Image
ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / 'assets/seq01/source-v4'
# An angled ink divider in strip 1 is verified visually rather than detected as white.
OVERRIDES = {1: [615,1143,1557]}
DESCRIPTIONS = [
'경비가 직원 출입구에서 딱지를 막고 출입증을 요구한다. 딱지는 치킨 배달이라고 설명한다.',
'외부인은 직원 동행이 필요하다. 딱지가 치킨은 있지만 출입증은 없다고 웃으며 답한다.',
'딱지가 락스에게 출입 규정이 바뀌었다고 무전한다. 락스는 들어갈 수 있겠냐고 묻는다.',
'딱지가 휴대전화를 꺼내며 배달부터 끝내겠다고 한다.',
'10분 전 공연장 뒤편 밴. 락스가 장갑 사진을 보여 주며 이번 의뢰의 표적이라고 말한다.',
'희귀 천연 핑크 다이아가 박힌 장갑. 감정가 100억 원이다.',
'가수가 공연에서 같은 장갑을 착용한다. 앙코르가 끝나면 장갑은 지하 2층 금고로 돌아간다.',
'금고 도착 후 반출까지 4분 동안 장갑만 가져와야 한다. 락스는 사람을 건드리지 말라고 당부한다.',
'딱지는 실제 운영팀 주문을 맡았다. 배달을 마치고 직원 통로의 뒷문을 열겠다고 한다.',
'원타치가 종이 포장 젓가락을 오른쪽 안주머니에 챙긴다. 찬호는 문도 부수지 말라고 하고 원타치는 젓가락을 챙기는 중이라고 답한다.',
'찬호가 치킨 봉투에 손을 뻗자 딱지가 제지한다. 고객님 것이라는 딱지에게 찬호는 냄새만 맡았다고 답한다.',
'현재 직원 출입구. 딱지가 주문 고객에게 전화해 직원이 동행하면 배달을 안까지 할 수 있다고 설명한다.',
'주문한 STAFF 직원이 출입증을 걸고 나와 딱지와 함께 들어가자고 한다.',
'경비가 직원의 출입증을 확인하고 휴게실까지만 동행하라고 안내한다.',
'휴게실에서 딱지가 직원에게 치킨 상자를 전달한다. 직원은 계속 못 먹었다며 반긴다.',
'직원 통로의 왼쪽은 휴게실, 오른쪽은 후문, 안쪽은 지하 2층 보관실로 이어진다. 딱지가 빈 봉투를 들고 통로로 나온다.',
'딱지가 안쪽에서 후문을 열고 찬호와 원타치에게 여기가 직원 통로라고 무전한다.',
'작은 검은 고무 문받침. 동료들이 들어올 때까지 문이 닫히지 않게 하려는 것이다.',
'딱지가 부츠로 고무 문받침을 열린 문 아래에 밀어 넣는다.',
'열린 후문에서 빛이 골목으로 흐른다. 찬호와 원타치는 바깥 골목에서 문을 향해 접근한다.',
'휴게실 직원이 배달기사에게 젓가락을 달라고 다시 부른다.',
'딱지가 직원 쪽으로 돌아서며 몸으로 열린 후문 방향을 가린다. 미소가 잠깐 굳는다.',
'문 밖 원타치가 준비해 둔 종이 포장 젓가락을 오른쪽 안주머니에서 꺼낸다.',
'원타치가 문틈으로 젓가락을 건네고 딱지가 등 뒤 손으로 받는다. 직원에게는 보이지 않는다.',
'딱지가 직원에게 젓가락을 건네며 맛있게 드시라고 한다. 직원은 고맙다고 한다.',
'직원이 휴게실로 돌아가 식사한다. 딱지가 동료들에게 지금 들어오라고 조용히 신호한다.',
'찬호와 원타치가 후문을 넘어 직원 통로에 들어온다. 딱지는 원타치에게 고맙다고 하고 원타치는 다음에는 직접 챙기라고 답한다.',
'딱지가 안쪽에서 문받침을 회수하고 후문을 닫는다.',
'딱지가 직원 출입구를 통해 밖으로 나와 밴에 복귀한다. 두 사람이 들어갔다고 락스에게 보고한다.',
'찬호와 원타치가 지하 2층 보관실 계단을 내려간다.',
'빈 운반 케이스를 든 반출팀이 지하 보안 구역에 먼저 와 있다. 찬호가 락스에게 무전한다.',
'두 사람은 계단 그림자에서 반출팀을 관찰한다. 앙코르도 끝나기 전에 반출팀이 왔다. 락스는 금고로 향하라고 지시한다.'
]
GAPS = [0,18,34,24,120,24,64,72,34,28,28,120,24,20,40,56,48,22,12,40,120,16,64,20,22,36,18,18,90,120,96,64]
WIDTHS = {18:.88,19:.94,22:.92,23:.94,24:.94,28:.94}
rows=[]
for strip in range(1,9):
 path=ART/f'{strip:02}.png'
 im=Image.open(path); im.verify(); a=np.asarray(Image.open(path).convert('RGB'))
 h,w=a.shape[:2]
 if strip in OVERRIDES:
  cuts=OVERRIDES[strip]
 else:
  whites=np.flatnonzero((a.min(axis=2)>235).mean(axis=1)>.985)
  groups=np.split(whites,np.flatnonzero(np.diff(whites)>1)+1)
  bands=[g for g in groups if len(g)>=2 and h*.10<g[0]<h*.92]
  if len(bands)!=3: raise ValueError(f'Strip {strip}: inspect dividers {[(int(g[0]),int(g[-1])) for g in bands]}')
  cuts=[int((g[0]+g[-1])//2) for g in bands]
 edges=[0,*cuts,h]
 for local,(top,bottom) in enumerate(zip(edges,edges[1:])):
  n=(strip-1)*4+local+1
  rows.append({'panel':n,'strip':strip,'src':f'/assets/seq01/source-v4/{strip:02}.png','source_width':w,'source_height':h,'top':top,'height':bottom-top,'gap':GAPS[n-1],'width_fraction':WIDTHS.get(n,1),'description':DESCRIPTIONS[n-1]})
parts=[]
for r in rows:
 top=-100*r['top']/r['height']
 style=f"aspect-ratio:{r['source_width']}/{r['height']};width:{r['width_fraction']*100:g}%;margin-top:clamp(12px,{r['gap']/760*100:.5f}cqw,{r['gap']}px)" if r['gap'] else f"aspect-ratio:{r['source_width']}/{r['height']};width:100%;margin-top:0"
 parts.append(f'<figure class="panel" id="panel-{r["panel"]}" data-panel="{r["panel"]}" style="{style}" aria-label="{html.escape(r["description"],quote=True)}"><img src="{r["src"]}" width="{r["source_width"]}" height="{r["source_height"]}" style="top:{top:.8f}%" alt="" aria-hidden="true" loading="eager" decoding="async"></figure>')
page='''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#12171d"><title>DESPERADO · 1화 · 문은 부수지 말 것</title><style>*{box-sizing:border-box}html{background:#12171d;scroll-behavior:smooth}body{margin:0;font-family:system-ui,sans-serif;color:#eef1f4}header,footer{max-width:var(--reader-width,760px);margin:auto;padding:18px 16px;display:flex;align-items:center;justify-content:space-between;gap:16px}header a{font-weight:700;letter-spacing:1px;text-decoration:none}header span,footer p{font-size:13px;color:#aab6c2}a{color:inherit}main{max-width:var(--reader-width,760px);margin:auto;background:#fff;container-type:inline-size;padding-bottom:64px;overflow:hidden}.panel{position:relative;margin-left:auto;margin-right:auto;margin-bottom:0;overflow:hidden;background:#fff}.panel img{position:absolute;left:0;width:100%;height:auto;display:block;max-width:none}footer a{font-size:14px} @media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}</style></head><body data-source-version="4"><header><a href="/">DESPERADO</a><span>1화 · 문은 부수지 말 것</span></header><main aria-label="데스페라도 시퀀스 1, 위에서 아래로 읽으세요">'''+''.join(parts)+'''</main><footer><p>시퀀스 1 · 원본 개작본</p><a href="#panel-1">맨 위로 ↑</a></footer></body></html>'''
page=page.replace('</head>','<script>if(new URLSearchParams(location.search).get("view")=="mobile")document.documentElement.style.setProperty("--reader-width","390px")</script></head>')
(ROOT/'episodes/ep01/source-v4.html').write_text(page)
(ART/'panels.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
(ART/'manifest.json').write_text(json.dumps({'version':4,'phase':'source-comic','panels':32,'strips':8,'motion_applied':False,'rendering':'CSS viewports of unmodified original comic artwork with editorial panel spacing'},ensure_ascii=False,indent=2))
# The user can also read the exact same comic without an internet connection.
offline=page.replace('href="/"','href="#panel-1"')
originals={}
for strip in range(1,9):
 src=f'/assets/seq01/source-v4/{strip:02}.png'
 offline=offline.replace(f'src="{src}"',f'data-strip="{strip:02}"')
 originals[f'{strip:02}']='data:image/png;base64,'+base64.b64encode((ART/f'{strip:02}.png').read_bytes()).decode()
script='<script>const originals='+json.dumps(originals)+';document.querySelectorAll("img[data-strip]").forEach(img=>{img.src=originals[img.dataset.strip]});</script>'
offline=offline.replace('</body>',script+'</body>')
(ROOT.parent/'DESPERADO_EP01_SOURCE_v4.html').write_text(offline)
print('Built 32-panel source reader and standalone original')
