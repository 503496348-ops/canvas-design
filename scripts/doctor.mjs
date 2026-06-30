#!/usr/bin/env node
import { execFileSync, spawnSync } from 'node:child_process';
import { existsSync } from 'node:fs';
import { join } from 'node:path';

const root = new URL('..', import.meta.url).pathname.replace(/\/$/, '');
const checks = [];
let failed = 0;

function ok(name, detail) {
  checks.push({ name, ok: true, detail });
  console.log(`✅ ${name}${detail ? ` — ${detail}` : ''}`);
}

function bad(name, detail, fix) {
  failed += 1;
  checks.push({ name, ok: false, detail, fix });
  console.log(`❌ ${name}${detail ? ` — ${detail}` : ''}`);
  if (fix) console.log(`   修复：${fix}`);
}

function commandVersion(command, args = ['--version']) {
  const result = spawnSync(command, args, { encoding: 'utf8' });
  if (result.error || result.status !== 0) return null;
  return (result.stdout || result.stderr || '').trim().split('\n')[0];
}

function parseNodeMajor(version) {
  const m = version?.match(/v?(\d+)\./);
  return m ? Number(m[1]) : 0;
}

console.log('Canvas Design Doctor · 一键开箱环境检查\n');

const nodeVersion = commandVersion('node');
if (!nodeVersion) {
  bad('Node.js', '未安装或不可执行', '安装 Node.js 20+，然后重新运行 npm run setup');
} else if (parseNodeMajor(nodeVersion) < 20) {
  bad('Node.js', `${nodeVersion}，版本过低`, '升级到 Node.js 20+');
} else {
  ok('Node.js', nodeVersion);
}

const npmVersion = commandVersion('npm');
if (!npmVersion) bad('npm', '未安装或不可执行', '安装 Node.js 官方版会自带 npm');
else ok('npm', npmVersion);

const pythonVersion = commandVersion('python3', ['--version']) || commandVersion('python', ['--version']);
if (!pythonVersion) bad('Python', '未检测到 python3/python', '安装 Python 3.10+；仅使用 PPTX 导出时可暂不需要');
else ok('Python', pythonVersion);

for (const file of [
  'package.json',
  'package-lock.json',
  'scripts/export_deck_pptx.mjs',
  'scripts/html2pptx.js',
  'tests/smoke-pptx-export.sh',
]) {
  if (existsSync(join(root, file))) ok(file, '存在');
  else bad(file, '缺失', '请确认仓库 clone 完整，或重新 git pull');
}

if (existsSync(join(root, 'node_modules', 'pptxgenjs'))) ok('pptxgenjs', '已安装');
else bad('pptxgenjs', '未安装', '运行 npm run setup 或 npm ci');

if (existsSync(join(root, 'node_modules', 'playwright'))) ok('playwright', '已安装');
else bad('playwright', '未安装', '运行 npm run setup 或 npm ci');

try {
  const output = execFileSync('npx', ['playwright', 'install', '--dry-run', 'chromium'], {
    cwd: root,
    encoding: 'utf8',
    stdio: ['ignore', 'pipe', 'pipe'],
  });
  if (/browser: chromium/i.test(output) || /Install location:/i.test(output) || output.trim()) {
    ok('Playwright Chromium', '可解析浏览器安装任务');
  } else {
    ok('Playwright Chromium', '检查通过');
  }
} catch (error) {
  bad('Playwright Chromium', '浏览器检查失败', '运行 npx playwright install chromium；Linux 若缺系统库，按 Playwright 提示安装依赖');
}

console.log('\n诊断结果：');
if (failed === 0) {
  console.log('✅ 环境可用。下一步运行：npm test');
} else {
  console.log(`❌ 发现 ${failed} 个问题。先按上面的“修复”处理，再运行：npm run setup && npm run doctor`);
  process.exit(1);
}
