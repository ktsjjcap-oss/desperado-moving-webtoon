import { chromium } from '@playwright/test';
import fs from 'node:fs/promises';
import crypto from 'node:crypto';
const base='https://desperado-moving-webtoon.ktsjjcap.workers.dev/episodes/ep01/webtoon-v18/';
const out='qa-v18';await fs.mkdir(out,{recursive:true});
const report={url:base,started:new Date().toISOString(),status:'running',checks:[],screenshots:[]};
const assert=(ok,msg)=>{if(!ok)throw Error(msg);report.checks.push(msg)};
const browser=await chromium.launch();
try{
 const request=await browser.newContext();const res=await request.request.get(base+'manifest.json');assert(res.status()===200,'Public manifest HTTP200');const m=await res.json();assert(m.pages===19&&m.narrative_cuts===90,'Manifest19pages90cuts');
 for(const a of m.assets){const r=await request.request.get(base+'images/'+a.file);assert(r.status()===200,'Image HTTP200 '+a.file);const b=await r.body();assert(crypto.createHash('sha256').update(b).digest('hex')===a.sha256,'Image hash matches selected art '+a.file)}
 for(const mode of ['mobile','desktop']){
  const context=await browser.newContext({viewport:mode==='mobile'?{width:390,height:844}:{width:1280,height:900},deviceScaleFactor:1,isMobile:mode==='mobile',hasTouch:mode==='mobile'});const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(String(e)));const response=await page.goto(base,{waitUntil:'load',timeout:60000});assert(response.status()===200,mode+' reader HTTP200');
  await page.waitForFunction(()=>[...document.querySelectorAll('main img')].every(i=>i.complete&&i.naturalWidth>0),{timeout:45000});assert(await page.locator('button.page').count()===19,mode+' all19pages loaded');
  const layout=await page.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth+1,images:[...document.querySelectorAll('main img')].map(i=>({n:i.naturalWidth,w:i.clientWidth,ratio:i.clientHeight/i.clientWidth,source:i.naturalHeight/i.naturalWidth}))}));assert(!layout.overflow,mode+' no horizontal body overflow');assert(layout.images.every(i=>Math.abs(i.ratio-i.source)<.003),mode+' all19images preserve aspect ratio');
  await page.screenshot({path:`${out}/${mode}-opening.png`});report.screenshots.push(`${mode}-opening.png`);
  const pages=mode==='mobile'?Array.from({length:19},(_,i)=>i+1):[6,13,17,19];
  for(const n of pages){const name=`${mode}-page-${String(n).padStart(2,'0')}.png`;await page.locator(`#page-${n}`).screenshot({path:`${out}/${name}`});report.screenshots.push(name)}
  await page.locator('#page-17').click();assert(await page.locator('dialog').evaluate(d=>d.open),mode+' zoom opens');await page.locator('#double').click();assert(await page.locator('.zoomview').evaluate(v=>v.classList.contains('big')),mode+'2x zoom');await page.screenshot({path:`${out}/${mode}-zoom.png`});report.screenshots.push(`${mode}-zoom.png`);await page.locator('#close').click();assert(!(await page.locator('dialog').evaluate(d=>d.open)),mode+'zoom closes');
  assert(errors.length===0,mode+' no JS runtime errors');await context.close();
 }
 const page=await request.newPage();await page.goto(base+'transcript.html');assert(await page.locator('article').count()===90,'Public transcript90cuts');await page.goto(base+'production.html');assert(await page.locator('h1').textContent()==='v18 · 각색과 실제 원화 검토','Public production report');
 report.status='passed';
}catch(e){report.status='failed';report.error=String(e);process.exitCode=1}finally{report.finished=new Date().toISOString();await fs.writeFile(out+'/report.json',JSON.stringify(report,null,2));await browser.close();console.log(JSON.stringify(report,null,2))}
