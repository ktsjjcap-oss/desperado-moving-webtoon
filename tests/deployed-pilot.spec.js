const { test, expect } = require('@playwright/test');

test('video-scrub moving-toon commercial gate', async ({ page }, info) => {
  const errors=[],bad=[];
  page.on('console',message=>message.type()==='error'&&errors.push(message.text()));
  page.on('pageerror',error=>errors.push(error.message));
  page.on('response',response=>response.status()>=400&&bad.push(`${response.status()} ${response.url()}`));
  await page.goto('/episodes/ep01/pilot',{waitUntil:'domcontentloaded'});
  await expect(page.locator('.scene')).toHaveCount(8);
  await expect(page.locator('video.sequence')).toHaveCount(8);
  await expect(page.locator('#sc00 video')).toHaveAttribute('data-time',/\d+\.\d+/,{timeout:30000});
  const metrics=await page.evaluate(()=>({ratio:document.querySelector('main').scrollHeight/innerHeight,scenes:[...document.querySelectorAll('.scene')].map(scene=>scene.offsetHeight/innerHeight)}));
  expect(metrics.ratio).toBeLessThanOrEqual(7.5);
  expect(Math.max(...metrics.scenes)).toBeLessThanOrEqual(1.15);
  for(const id of ['#sc00','#sc01','#sc02','#sc03','#sc04','#sc05','#sc06','#sc07']){
    const scene=page.locator(id); await scene.scrollIntoViewIfNeeded(); await page.waitForTimeout(220);
    await expect(scene.locator('video')).toHaveAttribute('data-time',/\d+\.\d+/);
  }
  await page.locator('#sc01').scrollIntoViewIfNeeded(); await page.waitForTimeout(180);
  const before=Number(await page.locator('#sc01 video').getAttribute('data-time'));
  await page.mouse.wheel(0,240); await page.waitForTimeout(180);
  const after=Number(await page.locator('#sc01 video').getAttribute('data-time'));
  expect(after).toBeGreaterThanOrEqual(before);
  await page.mouse.wheel(0,-240); await page.waitForTimeout(180);
  const reversed=Number(await page.locator('#sc01 video').getAttribute('data-time'));
  expect(reversed).toBeLessThanOrEqual(after);
  await page.locator('#sound-gate').click();
  await expect(page.locator('#sound')).toContainText('VOICE · SCORE · FOLEY');
  await expect(page.locator('body')).toHaveClass(/audio-enabled/);
  const assets=await page.evaluate(async()=>{
    const urls=['/assets/ep01-video/sc00.mp4','/assets/ep01-video/sc03.mp4','/assets/ep01-video/sc05.mp4','/assets/ep01-video/sc06.mp4','/assets/ep01-video/sc07.mp4','/assets/ep01-audio/tension-score-v3.ogg','/assets/ep01-audio/handle-lock-v3.ogg','/assets/ep01-audio/sc01-chano.mp3'];
    return Promise.all(urls.map(async url=>({url,status:(await fetch(url,{headers:{Range:'bytes=0-1'}})).status})));
  });
  expect(assets.every(asset=>[200,206].includes(asset.status))).toBeTruthy();
  await page.locator('#sc05').scrollIntoViewIfNeeded(); await page.waitForTimeout(250);
  await page.screenshot({path:`qa-evidence/${info.project.name}-sc05-video.png`,fullPage:false});
  expect(errors).toEqual([]); expect(bad).toEqual([]);
});
