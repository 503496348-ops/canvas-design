#!/usr/bin/env python3
"""source_intake.py — create a structured source brief for Canvas Design.

Usage:
  python scripts/source_intake.py --input source.md --out source-brief.md
  python scripts/source_intake.py --input https://example.com/article --out source-brief.md

This is intentionally conservative: it extracts observable text and creates a
brief scaffold. It does not invent summaries when extraction fails.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html.parser
import pathlib
import re
import sys
import urllib.request
from dataclasses import dataclass


class TextExtractor(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.skip = False

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "noscript", "svg"}:
            self.skip = True
        if tag in {"p", "h1", "h2", "h3", "li", "br"}:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in {"script", "style", "noscript", "svg"}:
            self.skip = False
        if tag in {"p", "h1", "h2", "h3", "li"}:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip:
            data = data.strip()
            if data:
                self.parts.append(data + " ")

    def text(self) -> str:
        raw = "".join(self.parts)
        raw = re.sub(r"[ \t]+", " ", raw)
        raw = re.sub(r"\n{3,}", "\n\n", raw)
        return raw.strip()


@dataclass
class SourceDoc:
    source: str
    text: str
    confidence: str


def read_source(value: str) -> SourceDoc:
    if re.match(r"^https?://", value):
        req = urllib.request.Request(value, headers={"User-Agent": "Mozilla/5.0 CanvasDesignSourceIntake/1.0"})
        with urllib.request.urlopen(req, timeout=25) as resp:
            content_type = resp.headers.get("content-type", "")
            data = resp.read(2_000_000)
        if "html" in content_type or data.lstrip().startswith(b"<"):
            parser = TextExtractor()
            parser.feed(data.decode("utf-8", errors="ignore"))
            text = parser.text()
        else:
            text = data.decode("utf-8", errors="ignore")
        return SourceDoc(value, text, "medium" if text else "low")

    path = pathlib.Path(value).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"Input not found: {path}")
    if path.suffix.lower() not in {".md", ".txt", ".html", ".htm", ".csv", ".json"}:
        return SourceDoc(str(path), "", "low")
    data = path.read_text(encoding="utf-8", errors="ignore")
    if path.suffix.lower() in {".html", ".htm"}:
        parser = TextExtractor()
        parser.feed(data)
        data = parser.text()
    return SourceDoc(str(path), data, "high" if data else "low")


def top_lines(text: str, limit: int = 8) -> list[str]:
    lines = []
    for line in re.split(r"[\n。！？!?]+", text):
        line = line.strip(" -#\t")
        if 12 <= len(line) <= 140:
            lines.append(line)
        if len(lines) >= limit:
            break
    return lines


def visual_clues(text: str) -> list[str]:
    clues = []
    if re.search(r"\d+(\.\d+)?%|\d+倍|\d+万|\d+亿|\$\d+", text):
        clues.append("存在数字/比例/金额，可做数据大字报或趋势页。")
    if re.search(r"步骤|流程|阶段|第一|第二|第三|pipeline|workflow", text, re.I):
        clues.append("存在流程结构，可做时间线/泳道图/系统流程页。")
    if re.search(r"对比|优缺点|区别|versus|vs\.?", text, re.I):
        clues.append("存在对比关系，可做双栏/矩阵/雷达页。")
    if re.search(r"问题|痛点|挑战|风险|失败", text):
        clues.append("存在问题叙事，可做问题-原因-方案三幕结构。")
    return clues or ["未检测到明确可视化线索，建议人工补充重点数据/图例。"]


def build_brief(doc: SourceDoc) -> str:
    text = doc.text.strip()
    lines = top_lines(text)
    title = lines[0] if lines else "待确认主题"
    excerpt = "\n".join(f"{i+1}. {line}" for i, line in enumerate(lines[:6])) or "- 未能提取有效正文。"
    clues = "\n".join(f"- {c}" for c in visual_clues(text))
    recommended = "HTML Deck"
    if len(text) < 800:
        recommended = "Poster / Image Deck"
    if re.search(r"演讲|分享|speaker|keynote", text, re.I):
        recommended = "HTML Deck + Presenter Mode"
    if re.search(r"可编辑|PowerPoint|pptx", text, re.I):
        recommended = "Editable PPTX"

    return f"""# Source Brief

## 来源
- source: {doc.source}
- fetched_at: {dt.datetime.now().isoformat(timespec='seconds')}
- confidence: {doc.confidence}
- chars: {len(text)}

## 一句话主题
{title}

## 核心观点候选
{excerpt}

## 可视化线索
{clues}

## 推荐输出形态
- {recommended}

## 待确认问题
- 目标受众是谁？
- 最终交付要 HTML / PDF / PPTX / 图片 / 视频中的哪几种？
- 是否有品牌资产、参考风格或禁用元素？

## 原文摘录

```text
{text[:4000] if text else '未提取到正文。若输入是 PDF/DOCX/PPTX/音视频，请先用对应文档/转写工具提取为 Markdown。'}
```
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--out", default="source-brief.md")
    args = ap.parse_args()
    doc = read_source(args.input)
    out = pathlib.Path(args.out).expanduser().resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_brief(doc), encoding="utf-8")
    print(f"✓ wrote {out}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as e:
        print(f"✗ source intake failed: {e}", file=sys.stderr)
        raise SystemExit(1)
