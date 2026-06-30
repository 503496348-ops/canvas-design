#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if ! command -v node >/dev/null 2>&1; then
  echo "❌ 未检测到 Node.js。请先安装 Node.js 20+：https://nodejs.org/" >&2
  exit 1
fi

if ! command -v npm >/dev/null 2>&1; then
  echo "❌ 未检测到 npm。请安装 Node.js 官方版，它会自带 npm。" >&2
  exit 1
fi

npm run setup
