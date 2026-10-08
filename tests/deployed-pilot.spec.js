const {test,expect}=require('@playwright/test');
test('video supports seeking ranges',async({request})=>{
 const response=await request.get('/assets/seq01/story-v2.mp4',{headers:{Range:'bytes=0-1'}});
 expect(response.status()).toBe(206);
 expect(response.headers()['content-range']).toMatch(/^bytes 0-1\/\d+$/);
 expect((await response.body()).length).toBe(2);
});
test('sequence master loads and scroll direction controls playback',async({page})=>{
 await page.goto('/episodes/ep01/pilot');
 await expect(page.locator('body')).toHaveAttribute('data-story-version','2');
 await expect(page.locator('#film')).toHaveJSProperty('readyState',4,{timeout:60000});
 await expect.poll(()=>page.evaluate(()=>document.querySelector('#film').duration)).toBeGreaterThan(188);
 await expect.poll(()=>page.evaluate(()=>document.querySelector('#film').duration)).toBeLessThan(190);
 await page.locator('#sound').click();
 await expect(page.locator('#film')).toHaveJSProperty('muted',false);
 await page.evaluate(()=>scrollTo(0,innerHeight*1.1+20));
 await expect.poll(()=>page.evaluate(()=>seq01.state.index)).toBe(1);
 await expect.poll(()=>page.evaluate(()=>document.querySelector('#film').currentTime)).toBeGreaterThanOrEqual(12.2);
 await page.evaluate(()=>scrollTo(0,innerHeight*.6));
 await expect.poll(()=>page.evaluate(()=>seq01.state.reverse)).toBe(true);
 await expect(page.locator('#film')).toHaveJSProperty('paused',true);
 await expect.poll(()=>page.evaluate(()=>document.querySelector('#film').currentTime)).toBeLessThan(12.2);
 await page.evaluate(()=>scrollTo(0,innerHeight*.7));
 await expect(page.locator('#film')).toHaveJSProperty('paused',false);
 await page.locator('#mode').click();
 await expect.poll(()=>page.evaluate(()=>seq01.state.continuous)).toBe(true);
 await page.locator('#restart').click();
 await expect.poll(()=>page.evaluate(()=>seq01.state.index)).toBe(0);
 await expect.poll(()=>page.evaluate(()=>document.querySelector('#film').currentTime)).toBeLessThan(3);
 await expect.poll(()=>page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
});

test('story bridges explain target, doors, wedge and destination',async({request,page})=>{
 const response=await request.get('/assets/seq01/captions-v2.json');
 expect(response.ok()).toBe(true);
 const captions=await response.json();
 const story=captions.map(c=>c.text).join(' ');
 for(const phrase of ['다이아 장갑','보석 자체가 값어치','A문','B문','문고임','관계자 통로','지하 2층 금고']) expect(story).toContain(phrase);
 await page.goto('/episodes/ep01/pilot');
 await expect(page.locator('#film')).toHaveJSProperty('readyState',4,{timeout:60000});
 await page.evaluate(()=>scrollTo(0,innerHeight*1.1*6+20));
 await expect.poll(()=>page.evaluate(()=>seq01.state.index)).toBe(6);
 await expect.poll(()=>page.evaluate(()=>document.querySelector('#film').currentTime),{timeout:15000}).toBeGreaterThanOrEqual(153.8);
});
