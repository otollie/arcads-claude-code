import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';

const dir = path.dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
const sizeArg = args.find(a => a.startsWith('--size='));
const files = args.filter(a => !a.startsWith('--'));
if (files.length === 0) {
  console.error('usage: node render.mjs [--size=1080x1920] slide-01.html [...]');
  process.exit(1);
}
const [w, h] = (sizeArg ? sizeArg.split('=')[1] : '1080x1350').split('x').map(Number);

// remote env pre-installs chromium; avoids playwright-version browser downloads
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const page = await browser.newPage({
  viewport: { width: w, height: h },
  deviceScaleFactor: 2, // 2x export for crispness
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
