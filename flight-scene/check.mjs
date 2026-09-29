import {chromium} from '@playwright/test';
const browser=await chromium.launch({headless:true});
const page=await browser.newPage({viewport:{width:1440,height:1000},deviceScaleFactor:1});const errors=[];page.on('pageerror',e=>errors.push(e.message));
await page.goto('http://127.0.0.1:5173');await page.waitForFunction(()=>window.__flight);
for(const t of [0,1.5,4.5,6.3,8.1,11.8,16.2,19.2]){await page.evaluate(t=>window.__flight.seek(t),t);await page.screenshot({path:`/tmp/homing-${t}.png`});}
console.log(JSON.stringify({errors}));await browser.close();
