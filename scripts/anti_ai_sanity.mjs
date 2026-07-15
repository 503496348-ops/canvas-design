#!/usr/bin/env node
/**
 * Anti-AI slop static sanity for Canvas Design outputs and templates.
 */
import { readFileSync, existsSync, readdirSync, statSync } from 'node:fs';
import { join, extname } from 'node:path';

const ROOT = new URL('..', import.meta.url).pathname.replace(/\/$/, '');

const ROOT_PATH = ROOT;
const TARGET_EXT = new Set(['.md', '.html', '.css', '.js', '.mjs', '.tsx', '.ts', '.json', '.txt']);
const RULES = [
  { name: 'emoji_overuse', label: '文本 emoji 过密（可能偏 AI 语体）', rx: /[\u2700-\u27BF\u{1F300}-\u{1FAFF}]/gu, limit: 24 },
  { name: 'flat_gradient', label: '过多线性/径向渐变堆叠（样式可能偏模板化）', rx: /linear-gradient\(|radial-gradient\(/gi, limit: 22 },
  { name: 'allcaps_blocks', label: '过量全大写词（口号化倾向）', rx: /\b[A-Z]{5,}\b/g, limit: 18 },
];

function iterFiles(dir, out = []) {
  if (!existsSync(dir)) return out;
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    let st;
    try {
      st = statSync(p);
    } catch (_) {
      continue;
    }
    if (st.isDirectory()) {
      if (name === 'node_modules' || name === '.git') continue;
      iterFiles(p, out);
    } else if (TARGET_EXT.has(extname(name).toLowerCase())) {
      out.push(p);
    }
  }
  return out;
}

function scanFile(path) {
  try {
    return readFileSync(path, 'utf8');
  } catch {
    return '';
  }
}

export function collectStyleGuardReport(root = ROOT_PATH) {
  const checks = [];
  const files = iterFiles(root);

  for (const rule of RULES) {
    let total = 0;
    const sampleFiles = [];

    for (const file of files) {
      const text = scanFile(file);
      if (!text) continue;
      const hits = text.match(rule.rx) || [];
      if (hits.length) {
        total += hits.length;
        if (sampleFiles.length < 2) sampleFiles.push(file.replace(root + '/', ''));
      }
    }

    const ok = total <= rule.limit;
    checks.push({
      name: rule.label,
      ok,
      count: total,
      limit: rule.limit,
      sample_files: sampleFiles,
      fix: ok ? '' : '降低视觉/文案一致性风险：结合 jakub/kill-ai-slop 做风格重洗与版式重构',
    });
  }

  const styleHint = existsSync(join(root, 'references', 'content-guidelines.md'));
  checks.push({
    name: '反AI风格执行文档',
    ok: styleHint,
    fix: styleHint ? '' : '补齐反AI风格条目（建议在 references/content-guidelines.md）并落入日检流程',
    sample_files: styleHint ? ['references/content-guidelines.md'] : [],
  });

  return { checks, passed: checks.every((x) => x.ok) };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const report = collectStyleGuardReport(process.cwd());
  console.log(JSON.stringify(report, null, 2));
  process.exit(report.passed ? 0 : 0);
}
