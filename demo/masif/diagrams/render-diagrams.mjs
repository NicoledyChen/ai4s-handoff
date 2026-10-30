import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import fs from 'node:fs/promises';

const require = createRequire(import.meta.url);
const sharp = require('/Users/a1/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp/dist/index.cjs');
const directory = path.dirname(fileURLToPath(import.meta.url));
const stems = ['01-infra-architecture', '02-agent-framework'];
for (const stem of stems) {
  const input = path.join(directory, `${stem}.svg`);
  const output = path.join(directory, `${stem}.png`);
  await fs.access(input);
  const result = await sharp(input, { density: 144 }).png().toFile(output);
  console.log(JSON.stringify({ file: output, width: result.width, height: result.height }));
}
