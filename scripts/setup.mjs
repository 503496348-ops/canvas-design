#!/usr/bin/env node
import { execFileSync } from 'node:child_process';

function run(title, command, args) {
  console.log(`\n▶ ${title}`);
  console.log(`$ ${[command, ...args].join(' ')}`);
  execFileSync(command, args, { stdio: 'inherit' });
}

console.log('Canvas Design 一键开箱安装');
console.log('目标：安装 Node 依赖、安装 Chromium、运行环境诊断。');

run('安装 Node.js 依赖', 'npm', ['ci']);
run('安装 Playwright Chromium 浏览器', 'npx', ['playwright', 'install', 'chromium']);
run('运行环境诊断', 'node', ['scripts/doctor.mjs']);

console.log('\n✅ 一键开箱完成。验证命令：npm test');
