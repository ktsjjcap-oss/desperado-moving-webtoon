import { chromium } from '@playwright/test';
import fs from 'node:fs/promises';
import crypto from 'node:crypto';
const base='https://desperado-moving-webtoon.ktsjjcap.workers.dev/episodes/ep01/webtoon-v18/';
const out='qa-v18';await fs.mkdir(out,{recursive:true});
const report={url:base,started:new Date().toISOString(),status:'running',checks:[],screenshots:[]};
const assert=(ok,msg)=>{if(!ok)throw Error(msg);report.checks.push(msg)};
const browser=await chromium.launch();
try{
 const request=await browser.newContext();let m;for(let i=0;i<24;i++){const res=await request.request.get(base+'manifest.json?qa='+Date.now());if(res.status()===200){const candidate=await res.json();if(candidate.build_tag==='v18-reflow-4heroes'){m=candidate;break}}await new Promise(r=>setTimeout(r,5000))}assert(!!m,'Published final reflow manifest');assert(m.pages===19&&m.narrative_cuts===90&&m.reading_blocks===24,'Manifest19sheets24blocks90cuts');assert(JSON.stringify(m.blocks.flatMap(b=>b.ids))===JSON.stringify(Array.from({length:90},(_,i)=>i+1)),'90cuts each exactly once');
 for(const a of m.assets){const r=await request.request.get(base+'images/'+a.file);assert(r.status()===200,'Image HTTP200 '+a.file);const b=await r.body();assert(crypto.createHash('sha256').update(b).digest('hex')===a.sha256,'Image hash matches selected art '+a.file)}
 for(const mode of ['mobile','desktop']){
  const context=await browser.newContext({viewport:mode==='mobile'?{width:390,height:844}:{width:1280,height:900},deviceScaleFactor:1,isMobile:mode==='mobile',hasTouch:mode==='mobile'});const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(String(e)));const response=await page.goto(base,{waitUntil:'load',timeout:60000});assert(response.status()===200,mode+' reader HTTP200');
  await page.waitForFunction(()=>[...document.querySelectorAll('main img')].every(i=>i.complete&&i.naturalWidth>0),null,{timeout:45000});assert(await page.locator('button.page').count()===24,mode+' all24reading blocks loaded');
  const layout=await page.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth+1,images:[...document.querySelectorAll('main img')].map(i=>({n:i.naturalWidth,w:i.clientWidth,ratio:i.clientHeight/i.clientWidth,source:i.naturalHeight/i.naturalWidth}))}));assert(!layout.overflow,mode+' no horizontal body overflow');assert(layout.images.every(i=>Math.abs(i.ratio-i.source)<.003),mode+' all19images preserve aspect ratio');
  await page.screenshot({path:`${out}/${mode}-opening.png`});report.screenshots.push(`${mode}-opening.png`);
  const indices=mode==='mobile'?Array.from({length:24},(_,i)=>i):[0,14,19,23];
  for(const n of indices){const name=`${mode}-block-${String(n+1).padStart(2,'0')}.png`;await page.locator(`button[data-block="${n}"]`).screenshot({path:`${out}/${name}`});report.screenshots.push(name)}
  const fragments=await page.locator('.page.fragment').evaluateAll(es=>es.map(e=>({actual:e.clientHeight/e.clientWidth,expected:Number(e.style.getPropertyValue('--h'))/Number(e.style.getPropertyValue('--w'))})));assert(fragments.every(e=>Math.abs(e.actual-e.expected)<.004),mode+' frame clipping ratios correct');
  await page.locator('#cut-78').click();assert(await page.locator('dialog').evaluate(d=>d.open),mode+' zoom opens');await page.locator('#double').click();assert(await page.locator('.zoomview').evaluate(v=>v.scrollWidth>=v.clientWidth*1.9),mode+'2x zoom scroll width');await page.screenshot({path:`${out}/${mode}-zoom.png`});report.screenshots.push(`${mode}-zoom.png`);await page.locator('#close').click();assert(!(await page.locator('dialog').evaluate(d=>d.open)),mode+'zoom closes');
  await page.locator('#cut-79').click();const clip=await page.locator('.zoomcanvas').evaluate(e=>({top:e.style.getPropertyValue('--top'),height:Number(e.style.getPropertyValue('--h'))}));assert(clip.top.startsWith('-')&&clip.height===1044,mode+' zoom excludes replaced source panel');await page.locator('#close').click();
  assert(errors.length===0,mode+' no JS runtime errors');await context.close();
 }
 const page=await request.newPage();await page.goto(base+'transcript.html');assert(await page.locator('article').count()===90,'Public transcript90cuts');await page.goto(base+'production.html');assert(await page.locator('h1').textContent()==='v18 · 각색과 실제 원화 검토','Public production report');
 report.status='passed';
}catch(e){report.status='failed';report.error=String(e);process.exitCode=1}finally{report.finished=new Date().toISOString();await fs.writeFile(out+'/report.json',JSON.stringify(report,null,2));await browser.close();console.log(JSON.stringify(report,null,2))}
