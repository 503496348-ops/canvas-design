#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

node - <<'NODE'
const fs = require('fs');
const pkg = JSON.parse(fs.readFileSync('package.json', 'utf8'));
const requiredScripts = ['setup', 'doctor', 'test', 'check:syntax'];
for (const name of requiredScripts) {
  if (!pkg.scripts || !pkg.scripts[name]) {
    throw new Error(`package.json missing npm script: ${name}`);
  }
}
for (const file of ['scripts/setup.mjs', 'scripts/doctor.mjs', 'install.sh']) {
  if (!fs.existsSync(file)) {
    throw new Error(`missing one-click file: ${file}`);
  }
}
const readme = fs.readFileSync('README.md', 'utf8');
for (const snippet of ['npm run setup', 'npm run doctor', 'npm test']) {
  if (!readme.includes(snippet)) {
    throw new Error(`README missing one-click command: ${snippet}`);
  }
}
console.log('one-click contract ok');
NODE
