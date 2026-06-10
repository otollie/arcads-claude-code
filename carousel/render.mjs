import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';

const dir = path.dirname(fileURLToPath(import.meta.url));
const files = process.argv.slice(2);
if (files.length === 0) {
  console.error('usage: node render.mjs slide-01.html [slide-02.html ...]');
  process.exit(1);
}

const browser = await chromium.launch();
const page = await browser.newPage({
  viewport: { width: 1080, height: 1350 },
  deviceScaleFactor: 2, // 2160x2700 export for crispness
});

for (const f of files) {
  const input = path.resolve(dir, f);
  const output = input.replace(/\.html$/, '.png');
  await page.goto('file://' + input);
  await page.waitForTimeout(300); // let fonts settle
  await page.screenshot({ path: output });
  console.log('rendered', output);
}

await browser.close();
