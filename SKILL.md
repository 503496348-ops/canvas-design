---
name: canvas-design
description: "视觉创作工具 — AI 图片生成、HTML Deck 制作、参考图检查"
license: MIT
metadata:
  author: 503496348-ops
  version: 1.0.0
triggers:
  - "画布"
  - "图片生成"
  - "HTML Deck"
  - "演示文稿"
  - "参考图"
  - "canvas"
  - "幻灯片"
---

# Canvas Design — 视觉创作工具

AI 图片生成 + HTML 演示文稿制作 + 参考图质量检查。

## 核心能力

| 命令 | 说明 |
|------|------|
| `canvas-design generate` | AI 图片生成（text2img/img2img/inpaint） |
| `canvas-design deck` | 生成 HTML 演示文稿 |
| `canvas-design check` | 检查参考图片质量 |
| `canvas-design pipeline` | 查看 pipeline 模板注册表 |

## 快速开始

```bash
# AI 图片生成
python3 scripts/cli.py generate --prompt "一只猫在月球上" --mode text2img

# 生成 HTML Deck
python3 scripts/cli.py deck --template default --slides 10 -o demo.html

# 检查参考图
python3 scripts/cli.py check ref1.jpg ref2.jpg
```

## 架构

- `scripts/gpt_image_api.py` — GPT Image API 封装
- `scripts/wanderix_pipeline_engine.py` — Pipeline 引擎
- `scripts/check_reference.py` — 参考图诊断
- `modules/controlnet/` — ControlNet 模块

## 测试

```bash
python3 -m pytest tests/ -q
```
