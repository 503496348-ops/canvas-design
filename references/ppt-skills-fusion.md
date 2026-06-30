# PPT Skills 融合增强路线

> 目标：把一念成画从“高审美视觉生成”升级为“全链路演示内容生产引擎”：资料输入 → 内容结构 → 视觉设计 → HTML/PDF/PPTX/图片/视频 → 演讲现场交付。

## 融合边界

本轮只吸收可验证的能力模式和可重写实现，不做外部品牌搬运。

| 模块 | 融合方向 | 进入一念成画的位置 | 优先级 |
|---|---|---|---|
| 原生可编辑 PPTX | 每页按 PPTX 物理约束创作，导出原生 shape/text/image，而不是整页截图 | `references/editable-pptx.md` + `scripts/html2pptx.js` + `export_deck_pptx.mjs` | P0 |
| 演讲者模式 | 当前页/下一页/逐字稿/计时器/双窗口同步 | `references/presenter-mode.md` + `assets/presenter-runtime.js` | P1 |
| 图片型社交 Deck | 一页一张图，阅读型/转发型，适合小红书/公众号/课程卡片 | `references/image-deck-mode.md` | P1 |
| 资料摄取适配器 | B站/YouTube/PDF/网页/Markdown/本地文件 → structured brief | `references/source-intake-adapter.md` + `scripts/source_intake.py` | P2 |
| 旧有审美体系校准 | 既有设计模式已基本覆盖，只保留增量校准 | SKILL.md 能力表与质量门禁 | P2 |

## 五条生产路线

```text
Canvas Art Mode          海报 / 单图 / 信息图
HTML Deck Mode           高审美网页 PPT，优先视觉表现
Editable PPTX Mode       原生可编辑 PowerPoint，优先客户后续编辑
Presenter Mode           讲者窗口 / 计时器 / 逐字稿 / 双屏同步
Image Deck Mode          图片型社交幻灯片，优先阅读传播
Source Intake Adapter    多源资料 → brief / outline / speaker script
```

## 路由规则

1. 用户说“要可编辑 PPTX / 客户还要改 / PowerPoint 里继续编辑” → 走 **Editable PPTX Mode**，从第一行 HTML 就遵守 `editable-pptx.md`。
2. 用户说“线下分享 / 演讲 / 讲稿 / 提词器 / 计时器 / speaker notes” → 在 HTML Deck 或 Editable PPTX 外额外生成 **Presenter Mode** 数据。
3. 用户说“小红书 / 朋友圈 / 公众号图文 / 知识卡片 / 一页一图” → 走 **Image Deck Mode**。
4. 用户给 B站/YouTube/网页/PDF/公众号/长文 → 先跑 **Source Intake Adapter**，产出 `source-brief.md`，再进入视觉路线。
5. 用户只说“做个好看的 PPT”且无编辑要求 → 默认 **HTML Deck Mode**，先做 2 页 showcase。

## 许可证与去污染

- MIT 来源可以学习实现与结构，但对外文档不得保留第三方品牌、作者名、仓库 URL。
- AGPL 来源只允许吸收思想和重新实现，禁止复制代码/模板/CSS/JS。
- 融合后必须 grep 验证生成物里无外部仓库名、作者名、URL 残留。

## 验收门禁

每次做 Deck 必须按目标形态验收：

| 目标形态 | 必验项 |
|---|---|
| HTML Deck | 浏览器打开、console error=0、每页截图、无溢出 |
| PDF | `export-pdf.sh` 或 `export_deck_pdf.mjs` 成功，页数一致 |
| Editable PPTX | `export_deck_pptx.mjs` 成功，文本框可编辑，非整页截图 |
| Presenter | `S` 打开讲者窗口，当前/下一页/notes/timer 同步 |
| Image Deck | 每页图片尺寸一致，文字可读，合并 PDF/PPTX 后页数一致 |
| Source Intake | `source-brief.md` 含来源、关键点、证据、待确认问题 |
