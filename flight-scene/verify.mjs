import {chromium} from '@playwright/test';
import assert from 'node:assert/strict';
const browser=await chromium.launch({headless:true});
const page=await browser.newPage({viewport:{width:1440,height:900}});const errors=[];page.on('pageerror',e=>errors.push(e.message));
await page.goto('http://127.0.0.1:5173');await page.waitForFunction(()=>window.__flight);
await page.evaluate(()=>window.__flight.seek(7.5));assert.equal(await page.locator('#chapter-name').textContent(),'THE SYNAPTIC STORE');
await page.keyboard.press('Space');assert.equal(await page.evaluate(()=>window.__flight.playing),true);
await page.keyboard.press('Space');assert.equal(await page.evaluate(()=>window.__flight.playing),false);
for(const [t,name] of [[9,'THE RETURN PATH'],[15,'THE MOVEMENT INPUTS'],[17.5,'THE COMPASS BRAKE']]){await page.locator(`[data-time="${t}"]`).click();assert.equal(await page.locator('#chapter-name').textContent(),name);}
await page.evaluate(()=>window.__flight.seek(20));await page.locator('#restart').click();assert.ok(await page.evaluate(()=>window.__flight.time)<1);
await page.locator('#timeline').fill('11.5');assert.equal(await page.evaluate(()=>window.__flight.playing),false);assert.equal(await page.evaluate(()=>window.__flight.time),11.5);
await page.setViewportSize({width:390,height:844});await page.evaluate(()=>window.__flight.seek(7.5));await page.screenshot({path:'/tmp/homing-mobile.png'});
assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
const reduced=await browser.newPage({reducedMotion:'reduce'});await reduced.goto('http://127.0.0.1:5173');await reduced.waitForFunction(()=>window.__flight);assert.equal(await reduced.evaluate(()=>window.__flight.playing),false);
console.log(JSON.stringify({errors,checks:'chapter boundaries, playback, restart, scrubbing, mobile layout, reduced motion passed'}));await browser.close();
