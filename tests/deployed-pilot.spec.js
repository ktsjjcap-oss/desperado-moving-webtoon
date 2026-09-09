const { test, expect } = require('@playwright/test');

test('commercial moving-webtoon closeout', async ({ page }, info) => {
  const errors = [], bad = [];
  page.on('console', m => m.type() === 'error' && errors.push(m.text()));
  page.on('pageerror', e => errors.push(e.message));
  page.on('response', r => r.status() >= 400 && bad.push(`${r.status()} ${r.url()}`));
  await page.goto('/episodes/ep01/pilot', { waitUntil: 'load' });
  await expect(page.locator('.scene')).toHaveCount(8);
  const m = await page.evaluate(() => ({vh: innerHeight,total: document.querySelector('main').scrollHeight,scenes: [...document.querySelectorAll('.scene')].map(s => s.offsetHeight / innerHeight)}));
  expect(m.total / m.vh).toBeLessThanOrEqual(7.4);
  expect(Math.max(...m.scenes)).toBeLessThanOrEqual(1.16);
  async function center(id) { await page.locator(id).scrollIntoViewIfNeeded(); await page.waitForTimeout(1050); }
  async function state(id) { return page.locator(id).getAttribute('data-state'); }
  for (const id of ['#sc00','#sc01','#sc02','#sc03','#sc04','#sc05','#sc06','#sc07']) { await center(id); expect(await state(id)).toBe('active'); }
  const loaded = await page.evaluate(() => [...document.images].map(i => i.complete && i.naturalWidth === 941 && i.naturalHeight === 1672));
  expect(loaded.every(Boolean)).toBeTruthy();
  await center('#sc01');
  const hand1 = await page.locator('#sc01 .hand-stop').evaluate(e => getComputedStyle(e).transform);
  await page.screenshot({ path: `qa-evidence/${info.project.name}-sc01.png` });
  for (const id of ['#sc02','#sc03','#sc05','#sc06']) { await center(id); await page.screenshot({ path: `qa-evidence/${info.project.name}-${id.slice(1)}.png` }); }
  await page.evaluate(() => scrollTo(0, 0)); await page.waitForTimeout(1100);
  expect(await state('#sc01')).toBe('idle');
  expect(await page.locator('#sc01 .hand-stop').evaluate(e => getComputedStyle(e).transform)).not.toBe(hand1);
  await page.locator('#sound').click(); await expect(page.locator('#sound')).toHaveText('SOUND ON');
  await page.locator('#sound').click(); await expect(page.locator('#sound')).toHaveText('SOUND OFF');
  expect(await page.locator('meta[name="build-sha"]').getAttribute('content')).toBe(process.env.EXPECTED_BUILD_SHA || await page.locator('meta[name="build-sha"]').getAttribute('content'));
  expect(errors).toEqual([]); expect(bad.filter(x => !x.includes('api.github.com'))).toEqual([]);
});
